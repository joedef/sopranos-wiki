# Monetization & SEO — activation guide

The scaffolding is in place. The site is **ready** to earn and to be indexed; a few values only you can provide finish the job. Nothing here is live-broken in the meantime — the placeholders degrade gracefully.

Read the honest caveats at the bottom before flipping anything on.

---

## The four values to fill in

| # | What | Where it goes | Effect until filled |
| - | ---- | ------------- | ------------------- |
| 1 | **Google Search Console** verification token | `mkdocs.yml` → `extra.google_site_verification` | No verification meta tag is emitted. Harmless. |
| 2 | **Amazon Associates** tracking tag | Shopping links in `docs/support.md` | Links work and are useful; they just earn nothing. |
| 3 | **GitHub Sponsors** username | `.github/FUNDING.yml` → uncomment `github:` | Sponsor button points at the Support page. |
| 4 | **Ko-fi / Buy Me a Coffee** handle *(optional)* | `.github/FUNDING.yml` | As above. |

---

## 1. Google Search Console (do this first — it's free and pure upside)

1. Go to <https://search.google.com/search-console> and add a **URL-prefix** property for `https://joedef.github.io/sopranos-wiki/`.
2. Choose the **HTML tag** verification method. Copy the token — the `content="..."` value.
3. Paste it into `mkdocs.yml`:
   ```yaml
   extra:
     google_site_verification: "PASTE_TOKEN_HERE"
   ```
4. Commit, let the site redeploy, then click **Verify**.
5. In Search Console, **submit the sitemap**: `sitemap.xml`. (Full URL: `https://joedef.github.io/sopranos-wiki/sitemap.xml`.)

This is the single highest-value action for discoverability. Do it even if you do nothing else here.

---

## 2. Amazon Associates

1. Apply at <https://affiliate-program.amazon.com>. Approval requires a few qualifying sales within 180 days, so apply once the site has some traffic.
2. You'll get a **tracking tag** like `joedef-20`.
3. In `docs/support.md`, the shopping links are Amazon search URLs. Add your tag by appending `&tag=YOURTAG-20` to each, e.g.:
   ```
   https://www.amazon.com/s?k=the+sopranos+complete+series+blu+ray&tag=joedef-20
   ```
   (For bulk, a find-and-replace across `docs/support.md` does it in one pass.)
4. **Keep the affiliate-disclosure admonition** that's already on that page. The FTC requires it, and so does Amazon's operating agreement.

---

## 3 & 4. Donations (optional)

- **GitHub Sponsors:** enrol at <https://github.com/sponsors>. Once approved, uncomment `github: [joedef]` in `.github/FUNDING.yml`.
- **Ko-fi / BMAC:** create an account, then uncomment the matching line with your handle.

The `custom:` link already gives you a working Sponsor button pointing at the Support page, so there's no rush and nothing is broken if you skip this.

---

## Before you turn on the money — read this

These points were covered in the planning conversation; they're repeated here so they don't get lost.

- **The "non-commercial" wording has been removed** from the README, the content licence, and the homepage disclaimer, because affiliate links and donations make that claim untrue. The **non-affiliation** disclaimer stays — it's protective and still accurate.
- **This wiki is about property that HBO / Warner Bros. Discovery own.** Original commentary and criticism is well protected, and commercial use doesn't by itself defeat fair use — but these are rights holders with deep legal resources. Risk scales with revenue and visibility, not with how right you are.
- **CC BY-SA gives you no exclusivity.** Anyone may legally clone the content and monetize their copy. A paywall strategy can't work and isn't attempted here.
- **This is not legal advice.** Twenty minutes with an IP lawyer before you scale past the low-risk tier (affiliate + small donations) is cheap insurance.
- **Realistic expectations:** at low traffic this earns coffee money. The wiki's real value is as a portfolio piece. See the planning notes.

---

## Ad networks (later, not now)

Display ads are deliberately not set up. Don't add AdSense yet — at low traffic it pays pennies and makes the site worse, which suppresses the sharing that would grow it. Revisit at ~25k pageviews/month; the good networks (Mediavine, Raptive) need 50k–100k sessions/month.
