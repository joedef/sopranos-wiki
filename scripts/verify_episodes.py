"""
Verify the Sopranos episode tables against Wikipedia's structured wikitext.

Fetches the raw wikitext of "The Sopranos season N" (1..6), parses the
{{Episode list}} templates (Title / DirectedBy / WrittenBy / OriginalAirDate),
and diffs against the markdown tables in docs/series/season-N.md.

Report-only. Prints every mismatch for human review.
"""
import json, re, sys, urllib.parse, urllib.request, html, unicodedata

ROOT = sys.argv[1]
UA = {"User-Agent": "wiki-builder-verify/1.0 (fact-check pass)"}

MONTHS = {m: i + 1 for i, m in enumerate(
    ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])}


def wikitext(title):
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "revisions",
        "rvprop": "content", "rvslots": "main", "titles": title})
    req = urllib.request.Request("https://en.wikipedia.org/w/api.php?" + q, headers=UA)
    pages = json.load(urllib.request.urlopen(req, timeout=40))["query"]["pages"]
    page = next(iter(pages.values()))
    return page["revisions"][0]["slots"]["main"]["*"]


def strip_wiki(s):
    """Reduce wiki markup to plain display text."""
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\{\{sic\|?[^}]*\}\}", "", s)
    s = re.sub(r"\{\{nowrap\|([^}]*)\}\}", r"\1", s)
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)   # [[A|B]] -> B
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)            # [[A]]   -> A
    s = s.replace("'''", "").replace("''", "")
    s = html.unescape(s)
    return s.strip()


def norm_text(s):
    s = strip_wiki(s)
    s = unicodedata.normalize("NFKD", s)
    s = s.replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = s.replace("…", "...").replace("—", "-").replace("–", "-")
    s = s.replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", " ", s.lower())
    return " ".join(s.split())


def names(s):
    """Credit string -> normalized set of person names (order/format tolerant)."""
    s = strip_wiki(s)
    s = re.sub(r"(?i)\b(story|teleplay|written)\s+by\b", " ", s)
    parts = re.split(r"\s*(?:&|,| and )\s*", s)
    return {norm_text(p) for p in parts if norm_text(p)}


def split_credit(s):
    """Return (story_set, teleplay_set) or (None, flat_set) if not split.

    Handles Wikipedia's {{StoryTeleplay|s=...|t=...}} and our own
    '*Story:* A · *Teleplay:* B' rendering.
    """
    m = re.search(r"\{\{\s*StoryTeleplay\s*\|(.*?)\}\}", s, re.S | re.I)
    if m:
        body = m.group(1)
        sm = re.search(r"\bs\s*=\s*(.*?)(?=\|\s*t\s*=|\Z)", body, re.S)
        tm = re.search(r"\bt\s*=\s*(.*?)(?=\|\s*[a-z]+\s*=|\Z)", body, re.S)
        return (names(sm.group(1)) if sm else set(),
                names(tm.group(1)) if tm else set())
    if re.search(r"(?i)\bstory\s*:", s) and re.search(r"(?i)\bteleplay\s*:", s):
        parts = re.split(r"·|\|", s)
        story = teleplay = set()
        for p in parts:
            if re.search(r"(?i)story\s*:", p):
                story = names(re.sub(r"(?i).*story\s*:", "", p))
            elif re.search(r"(?i)teleplay\s*:", p):
                teleplay = names(re.sub(r"(?i).*teleplay\s*:", "", p))
        return story, teleplay
    return None, names(s)


def credits_match(mine, wiki):
    ms, mt = split_credit(mine)
    ws, wt = split_credit(wiki)
    if ws is None and ms is None:
        return mt == wt
    # if either side is split, both story and teleplay must agree
    return (ms or set()) == (ws or set()) and mt == wt


def parse_wiki_episodes(text):
    """Extract Episode list template fields."""
    eps = []
    for m in re.finditer(r"\{\{\s*Episode list(.*?)\n\}\}", text, re.S | re.I):
        body = m.group(1)
        f = {}
        for fm in re.finditer(r"\n\s*\|\s*([A-Za-z0-9_]+)\s*=\s*(.*?)(?=\n\s*\|\s*[A-Za-z0-9_]+\s*=|\Z)",
                              body, re.S):
            f[fm.group(1).strip()] = fm.group(2).strip()
        if "Title" not in f:
            continue
        d = f.get("OriginalAirDate", "")
        dm = re.search(r"\{\{\s*[Ss]tart date\|(\d{4})\|(\d{1,2})\|(\d{1,2})", d)
        date = (int(dm.group(1)), int(dm.group(2)), int(dm.group(3))) if dm else None
        eps.append(dict(title=f.get("Title", ""), director=f.get("DirectedBy", ""),
                        writer=f.get("WrittenBy", ""), date=date))
    return eps


def parse_md_episodes(path):
    """Extract rows from the markdown episode tables."""
    rows = []
    for line in open(path, encoding="utf-8"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        if not re.match(r"^\**\d+\**$", cells[0]):     # skip header/separator rows
            continue
        dm = re.match(r"([A-Za-z]{3})\w*\s+(\d{1,2}),\s*(\d{4})", cells[4])
        date = (int(dm.group(3)), MONTHS[dm.group(1)[:3]], int(dm.group(2))) if dm else None
        rows.append(dict(num=cells[0].strip("*"), title=cells[1], director=cells[2],
                         writer=cells[3], date=date, raw=cells[4]))
    return rows


def main():
    total_issues = 0
    for season in range(1, 7):
        wt = wikitext(f"The Sopranos season {season}")
        wiki = parse_wiki_episodes(wt)
        md = parse_md_episodes(f"{ROOT}/docs/series/season-{season}.md")

        print(f"\n===== SEASON {season} =====")
        print(f"  wikipedia episodes: {len(wiki)}   wiki-page rows: {len(md)}")
        if len(wiki) != len(md):
            print(f"  !! COUNT MISMATCH")
            total_issues += 1

        for i, row in enumerate(md):
            if i >= len(wiki):
                break
            w = wiki[i]
            issues = []
            if norm_text(row["title"]) != norm_text(w["title"]):
                issues.append(f"TITLE   mine={strip_wiki(row['title'])!r}  wiki={strip_wiki(w['title'])!r}")
            if names(row["director"]) != names(w["director"]):
                issues.append(f"DIRECTOR mine={strip_wiki(row['director'])!r}  wiki={strip_wiki(w['director'])!r}")
            if not credits_match(row["writer"], w["writer"]):
                issues.append(f"WRITER  mine={strip_wiki(row['writer'])!r}  wiki={w['writer']!r}")
            if row["date"] != w["date"]:
                issues.append(f"DATE    mine={row['raw']!r}({row['date']})  wiki={w['date']}")
            if issues:
                total_issues += len(issues)
                print(f"  ep row {row['num']:>3} — {strip_wiki(w['title'])}")
                for s in issues:
                    print(f"      {s}")

    print(f"\n================ TOTAL DISCREPANCIES: {total_issues} ================")


main()
