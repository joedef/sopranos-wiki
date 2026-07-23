# The Sopranos Wiki

An open-source, wiki-style reference and critical analysis of **The Sopranos** — David Chase's HBO series, all 86 episodes across six seasons, the characters, the cast and writers' room, the 2021 prequel film, and the ending nobody has stopped arguing about since June 10, 2007.

**📺 Read it: <https://joedef.github.io/sopranos-wiki/>**

> *"All due respect, you got no fuckin' idea what it's like to be Number One."*

---

## What's in here

| Section | What it covers |
| --- | --- |
| **The Series** | Season-by-season guides with complete episode tables — every title, director, writer, and air date across all 86 episodes — plus *The Many Saints of Newark* and what happened after |
| **Characters** | 24 character pages, from Tony and Carmela down to Vito and Furio, with a family tree and the DiMeo organizational chart |
| **People** | Cast and crew biographies — Chase, Gandolfini, Falco, Imperioli, Bracco, Chianese, Sirico, Van Zandt, de Matteo, Marchand, plus the writers' room and the directors |
| **Analysis** | 14 essays: themes, Tony's arc, the therapy structure, the ending, dreams, the women, Italian-American identity, food, music, craft, comedy, decline, mob-movie self-awareness, and religion |
| **Data** | A timeline, complete awards tables, per-season ratings, a body count, a sourced quote index, and charts |
| **Reference** | Filming locations, a glossary, the real DeCavalcante family, legacy, and sources |

## Running it locally

```bash
pip install -r requirements.txt
mkdocs serve          # live-reload at http://127.0.0.1:8000
mkdocs build --strict # what CI runs
```

Pushing to `main` triggers `.github/workflows/deploy.yml`, which builds the site and publishes it to GitHub Pages.

## Contributing

Contributions welcome — corrections especially. Everything is plain Markdown in `docs/`. See **[CONTRIBUTING.md](CONTRIBUTING.md)** for house style, sourcing rules, and the one hard rule about copyrighted text.

`main` is protected: all changes go through a pull request that must pass the build and be approved.

Good first contributions:

- Fix a factual error and cite the correction
- Fill out a thin character page
- Add a filming location and its present-day status
- Replace a dead video embed

## Licensing

- **Prose, tables, and other content** — [CC BY-SA 4.0](LICENSE-CONTENT.md)
- **Configuration, CSS, and workflow code** — [MIT](LICENSE)

## Disclaimer

An independent, non-commercial fan project. **Not affiliated with, authorized by, or endorsed by** HBO, Warner Bros. Discovery, Chase Films, or any rights holder. *The Sopranos* and related marks belong to their owners. No script text or copyrighted imagery is reproduced here beyond brief quotation for commentary and criticism.
