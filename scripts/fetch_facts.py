"""Fetch raw Wikipedia wikitext and print targeted extracts for fact-checking.

Usage: python fetch_facts.py "Title" [infobox|lead|section:REGEX] ...
Prints losslessly (no summarization) so claims can be checked against source text.
"""
import json, re, sys, urllib.parse, urllib.request

UA = {"User-Agent": "wiki-builder-factcheck/1.0"}
INFOBOX_KEYS = re.compile(
    r"^(name|runtime|budget|gross|released|starring|director|writer|producer|"
    r"num_episodes|num_seasons|first_aired|last_aired|network|company|"
    r"country|language|based_on|music|cinematography|editing|distributor)$", re.I)


def wikitext(title):
    q = urllib.parse.urlencode({
        "action": "query", "format": "json", "prop": "revisions",
        "rvprop": "content", "rvslots": "main", "titles": title, "redirects": "1"})
    req = urllib.request.Request("https://en.wikipedia.org/w/api.php?" + q, headers=UA)
    pages = json.load(urllib.request.urlopen(req, timeout=45))["query"]["pages"]
    p = next(iter(pages.values()))
    if "missing" in p:
        return None
    return p["revisions"][0]["slots"]["main"]["*"]


def clean(s):
    s = re.sub(r"<ref[^>]*/>", "", s)
    s = re.sub(r"<ref.*?</ref>", "", s, flags=re.S)
    s = re.sub(r"\[\[[^\]|]*\|([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]*)\]\]", r"\1", s)
    s = re.sub(r"\{\{(?:nowrap|nobr)\|([^}]*)\}\}", r"\1", s)
    s = s.replace("'''", "").replace("''", "")
    return re.sub(r"[ \t]+", " ", s).strip()


def infobox(text):
    i = text.find("{{Infobox")
    if i < 0:
        return []
    depth, j = 0, i
    while j < len(text):
        if text[j:j + 2] == "{{":
            depth += 1; j += 2; continue
        if text[j:j + 2] == "}}":
            depth -= 1; j += 2
            if depth == 0: break
            continue
        j += 1
    body = text[i:j]
    out = []
    for m in re.finditer(r"\n\s*\|\s*([A-Za-z0-9_]+)\s*=\s*(.*?)(?=\n\s*\|\s*[A-Za-z0-9_]+\s*=|\Z)", body, re.S):
        k, v = m.group(1).strip(), clean(m.group(2))
        if INFOBOX_KEYS.match(k) and v:
            out.append(f"    {k:16} {v[:300]}")
    return out


def lead(text, n=1400):
    t = re.sub(r"^\{\{.*?\n\}\}\n", "", text, flags=re.S)
    t = re.split(r"\n==", t)[0]
    return clean(t)[:n]


def section(text, pattern, n=2000):
    parts = re.split(r"\n(==+)\s*(.*?)\s*==+", text)
    out = []
    for i in range(1, len(parts) - 1, 3):
        head, body = parts[i + 1], parts[i + 2]
        if re.search(pattern, head, re.I):
            out.append(f"  ## {head}\n" + clean(body)[:n])
    return out


def main():
    title = sys.argv[1]
    text = wikitext(title)
    print(f"\n{'='*70}\n{title}\n{'='*70}")
    if text is None:
        print("  !! PAGE MISSING"); return
    for arg in sys.argv[2:]:
        if arg == "infobox":
            print("  [INFOBOX]"); print("\n".join(infobox(text)) or "    (none)")
        elif arg == "lead":
            print("  [LEAD]\n   ", lead(text))
        elif arg.startswith("section:"):
            for s in section(text, arg.split(":", 1)[1]) or ["  (no matching section)"]:
                print(s)


main()
