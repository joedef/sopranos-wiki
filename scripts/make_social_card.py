"""
Generate the 1200x630 Open Graph card.

Deliberately typographic — no film stills, no poster art, nothing owned by
Paramount. Just the wiki's own name in the trilogy's palette (near-black with
a single amber accent), which is both legally clean and on-brand.
"""

import os
import sys

from PIL import Image, ImageDraw, ImageFont

REPO = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
OUT = os.path.join(REPO, "docs", "assets", "social-card.png")

W, H = 1200, 630
BG = (16, 14, 15)
GOLD = (158, 32, 32)
GOLD_BRIGHT = (207, 59, 59)
CREAM = (244, 241, 236)
MUTED = (150, 140, 124)

FONT_DIRS = [
    r"C:\Windows\Fonts",
    "/usr/share/fonts/truetype/dejavu",
    "/Library/Fonts",
]
CANDIDATES = {
    "bold": ["georgiab.ttf", "timesbd.ttf", "DejaVuSerif-Bold.ttf", "arialbd.ttf"],
    "regular": ["georgia.ttf", "times.ttf", "DejaVuSerif.ttf", "arial.ttf"],
}


def load_font(kind, size):
    for name in CANDIDATES[kind]:
        for directory in FONT_DIRS:
            path = os.path.join(directory, name)
            if os.path.exists(path):
                return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def text_width(draw, text, font):
    return draw.textbbox((0, 0), text, font=font)[2]


def main():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # Subtle vertical vignette — lighter at top, like top-lit Willis interiors
    for y in range(H):
        t = y / float(H)
        shade = int(20 * (1 - t) ** 2)
        if shade:
            d.line([(0, y), (W, y)], fill=(BG[0] + shade, BG[1] + shade, BG[2] + shade))

    # Gold rule top and bottom
    d.rectangle([0, 0, W, 8], fill=GOLD)
    d.rectangle([0, H - 4, W, H], fill=(GOLD[0] // 2, GOLD[1] // 2, GOLD[2] // 2))

    f_kicker = load_font("regular", 28)
    f_title = load_font("bold", 108)
    f_sub = load_font("regular", 34)
    f_foot = load_font("regular", 25)

    # Kicker
    kicker = "A N   O P E N   S O U R C E   W I K I"
    d.text((80, 116), kicker, font=f_kicker, fill=GOLD)

    # Title
    d.text((80, 168), "The Sopranos", font=f_title, fill=CREAM)

    # Accent rule under the title
    d.rectangle([80, 306, 80 + 190, 310], fill=GOLD_BRIGHT)

    # Subtitle
    sub_lines = [
        "All 86 episodes, the characters,",
        "the people, and the ending.",
    ]
    y = 348
    for line in sub_lines:
        d.text((80, y), line, font=f_sub, fill=MUTED)
        y += 48

    # Footer
    footer = "joedef.github.io/sopranos-wiki"
    d.text((80, H - 92), footer, font=f_foot, fill=GOLD)

    # Right-hand section chips
    chips = ["SERIES", "CHARACTERS", "PEOPLE", "ANALYSIS", "DATA", "MEDIA"]
    f_chip = load_font("regular", 22)
    cy = 176
    for chip in chips:
        cw = text_width(d, chip, f_chip)
        x1 = W - 80 - cw - 36
        d.rounded_rectangle(
            [x1, cy, W - 80, cy + 42], radius=4, outline=(70, 60, 44), width=2
        )
        d.text((x1 + 18, cy + 9), chip, font=f_chip, fill=MUTED)
        cy += 56

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, "PNG", optimize=True)
    print("Wrote {0} ({1:,} bytes, {2}x{3})".format(
        OUT, os.path.getsize(OUT), img.width, img.height))


if __name__ == "__main__":
    main()
