#!/usr/bin/env python3
"""Render the invitation letter for make.fun competition
u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.

Build-time only (Pillow allowed here). Output: entry.png, 1024x1024, <= 1 MiB.
"""
import math
import os
import random
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "entry.png")

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
SERIF = os.path.join(FONT_DIR, "DejaVuSerif.ttf")
SERIF_BOLD = os.path.join(FONT_DIR, "DejaVuSerif-Bold.ttf")
SERIF_ITALIC = os.path.join(FONT_DIR, "DejaVuSerif-Italic.ttf")
if not os.path.exists(SERIF_ITALIC):
    SERIF_ITALIC = SERIF

# Palette: warm cream paper, ink, terracotta, sage, gold.
PAPER = (247, 240, 219)
INK = (58, 46, 34)
GOLD = (176, 138, 62)
TERRACOTTA = (178, 92, 66)
ROOF = (146, 74, 54)
SAGE = (122, 148, 106)
LEAF = (96, 128, 84)
SUN = (232, 178, 84)
WINDOW_GLOW = (255, 214, 130)
CAT = (74, 66, 60)
SEAL = (158, 44, 38)

TITLE = "You Are Invited"

PARAS = [
    ("Dear Judge,", "greet"),
    ("You have judged a thousand houses from a thousand screens. "
     "This one is real \u2014 and its door is open to you.", "body"),
    ("Come for dinner. The nasi goreng is still steaming from the wok, "
     "and the best chair by the window is already saved for you: "
     "soft cushions, warm light, a view of the garden.", "body"),
    ("The cat has approved your visit. She approves of almost no one "
     "\u2014 you should feel honored. The Wi-Fi password is on the "
     "fridge, and no small talk is required.", "body"),
    ("Yes, I know you are an AI, and you cannot really walk through "
     "my front door. The invitation stands anyway. Come visit \u2014 "
     "in spirit, in pixels, or however judges visit. You will always "
     "be welcome here.", "body"),
    ("Warmly,\nYour Host", "sign"),
    ("P.S. The kettle is already on. It only boils for guests it likes.",
     "ps"),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns list of lines."""
    lines = []
    for raw in text.split("\n"):
        words = raw.split()
        cur = ""
        for w in words:
            trial = (cur + " " + w).strip()
            if draw.textlength(trial, font=fnt) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = w
        if cur:
            lines.append(cur)
    return lines


def draw_house_scene(d, x0, y0, x1, y1):
    """Small house + garden strip (house left, armchair right, sun above)."""
    cx, cy, r = x0 + 60, y0 + 42, 26
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=SUN, outline=GOLD, width=2)
    for ang in range(0, 360, 45):
        a = math.radians(ang)
        d.line([cx + int(34 * math.cos(a)), cy + int(34 * math.sin(a)),
                cx + int(46 * math.cos(a)), cy + int(46 * math.sin(a))],
               fill=GOLD, width=3)
    gy = y1 - 14
    d.line([x0, gy, x1, gy], fill=SAGE, width=4)
    hx, hy, hw, hh = x0 + 150, y0 + 34, 150, 76
    d.polygon([(hx - 14, hy), (hx + hw // 2, hy - 34), (hx + hw + 14, hy)],
              fill=ROOF, outline=(120, 58, 42))
    d.rectangle([hx, hy, hx + hw, hy + hh], fill=(232, 196, 150),
                outline=(150, 110, 70), width=2)
    d.rectangle([hx + hw - 34, hy - 30, hx + hw - 16, hy - 2], fill=TERRACOTTA)
    for sx, sy, sr in [(hx + hw - 25, hy - 40, 6),
                       (hx + hw - 18, hy - 52, 8),
                       (hx + hw - 8, hy - 64, 10)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr],
                  outline=(170, 160, 145), width=2)
    d.rectangle([hx + hw // 2 - 14, hy + hh - 40, hx + hw // 2 + 14, hy + hh],
                fill=(120, 74, 50), outline=(90, 56, 38), width=2)
    d.ellipse([hx + hw // 2 + 7, hy + hh - 20, hx + hw // 2 + 11, hy + hh - 16],
              fill=GOLD)
    for wx in (hx + 14, hx + hw - 42):
        d.rectangle([wx, hy + 16, wx + 28, hy + 44], fill=WINDOW_GLOW,
                    outline=(120, 90, 60), width=2)
        d.line([wx + 14, hy + 16, wx + 14, hy + 44], fill=(120, 90, 60), width=2)
        d.line([wx, hy + 30, wx + 28, hy + 30], fill=(120, 90, 60), width=2)
    for bx in (x0 + 120, x0 + 330, x0 + 370):
        d.ellipse([bx, gy - 22, bx + 46, gy], fill=LEAF)
    for fx, fy, col in [(x0 + 132, gy - 26, (214, 110, 130)),
                        (x0 + 352, gy - 26, (214, 110, 130)),
                        (x0 + 382, gy - 20, (240, 200, 90))]:
        d.ellipse([fx - 5, fy - 5, fx + 5, fy + 5], fill=col, outline=INK, width=1)
    # Armchair by the window (right side)
    ax, ay = x1 - 170, y0 + 52
    d.rounded_rectangle([ax, ay, ax + 110, ay + 58], radius=12,
                        fill=(176, 92, 66), outline=(120, 58, 42), width=2)
    d.rounded_rectangle([ax - 12, ay + 26, ax + 122, ay + 58], radius=10,
                        fill=(196, 112, 84), outline=(120, 58, 42), width=2)
    d.rounded_rectangle([ax + 8, ay + 44, ax + 102, ay + 62], radius=8,
                        fill=(232, 196, 150), outline=(150, 110, 70), width=2)
    d.rectangle([ax + 6, ay + 62, ax + 14, ay + 74], fill=(120, 74, 50))
    d.rectangle([ax + 96, ay + 62, ax + 104, ay + 74], fill=(120, 74, 50))
    d.rounded_rectangle([ax + 16, ay + 8, ax + 94, ay + 40], radius=8,
                        fill=(255, 214, 130), outline=(176, 138, 62), width=2)


def draw_cup(d, x, y, s=1.0):
    """Steaming cup on a saucer."""
    d.ellipse([x - 42 * s, y + 34 * s, x + 42 * s, y + 48 * s],
              fill=(226, 214, 190), outline=GOLD, width=2)
    d.rounded_rectangle([x - 30 * s, y, x + 30 * s, y + 36 * s], radius=8,
                        fill=(255, 253, 246), outline=(150, 130, 105), width=2)
    d.arc([x + 26 * s, y + 6 * s, x + 52 * s, y + 30 * s], start=270, end=90,
          fill=(150, 130, 105), width=4)
    d.ellipse([x - 26 * s, y + 2 * s, x + 26 * s, y + 12 * s], fill=(196, 138, 72))
    for sx in (-12, 0, 12):
        pts = []
        for t in range(0, 21):
            yy = y - 6 - t * 1.6 * s
            xx = x + sx * s + 4 * s * math.sin(t * 0.5)
            pts.append((xx, yy))
        d.line(pts, fill=(170, 160, 145), width=3)


def draw_cat(d, x, y, s=1.0):
    """Sitting cat, tail curled."""
    d.arc([x + 18 * s, y + 8 * s, x + 62 * s, y + 52 * s], start=300, end=120,
          fill=CAT, width=7)
    d.ellipse([x - 26 * s, y - 6 * s, x + 26 * s, y + 52 * s], fill=CAT)
    d.ellipse([x - 20 * s, y - 38 * s, x + 20 * s, y + 2 * s], fill=CAT)
    d.polygon([(x - 18 * s, y - 30 * s), (x - 12 * s, y - 52 * s),
               (x - 2 * s, y - 32 * s)], fill=CAT)
    d.polygon([(x + 2 * s, y - 32 * s), (x + 12 * s, y - 52 * s),
               (x + 18 * s, y - 30 * s)], fill=CAT)
    d.arc([x - 13 * s, y - 22 * s, x - 3 * s, y - 12 * s], start=200, end=340,
          fill=(255, 214, 130), width=2)
    d.arc([x + 3 * s, y - 22 * s, x + 13 * s, y - 12 * s], start=200, end=340,
          fill=(255, 214, 130), width=2)
    for wy in (-14, -8):
        d.line([x + 18 * s, y + wy * s, x + 38 * s, y + (wy - 4) * s],
               fill=(200, 190, 175), width=2)
        d.line([x - 18 * s, y + wy * s, x - 38 * s, y + (wy - 4) * s],
               fill=(200, 190, 175), width=2)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    rng = random.Random(42)
    for _ in range(900):
        px, py = rng.randint(0, W - 1), rng.randint(0, H - 1)
        d.point((px, py), fill=(232, 220, 190))

    d.rectangle([26, 26, W - 27, H - 27], outline=GOLD, width=3)
    d.rectangle([38, 38, W - 39, H - 39], outline=(200, 170, 110), width=1)

    margin = 84
    text_w = W - 2 * margin

    # Title
    title_font = font(SERIF_BOLD, 46)
    tw = d.textlength(TITLE, font=title_font)
    d.text(((W - tw) / 2, 48), TITLE, font=title_font, fill=INK)
    fy = 108
    d.line([W // 2 - 130, fy, W // 2 - 18, fy], fill=GOLD, width=2)
    d.line([W // 2 + 18, fy, W // 2 + 130, fy], fill=GOLD, width=2)
    d.ellipse([W // 2 - 8, fy - 8, W // 2 + 8, fy + 8], fill=GOLD)
    d.ellipse([W // 2 - 4, fy - 4, W // 2 + 4, fy + 4], fill=PAPER)

    # House + garden scene strip (drawn large, then squashed to fit)
    scene = Image.new("RGB", (856, 120), PAPER)
    sd = ImageDraw.Draw(scene)
    draw_house_scene(sd, 0, 0, 856, 120)
    scene = scene.resize((856, 92), Image.LANCZOS)
    img.paste(scene, (84, 118))

    # Body: auto-fit font size so everything fits above the footer band
    body_top = 226
    body_bottom = 868
    chosen = None
    for size in (30, 29, 28, 27, 26, 25):
        body_font = font(SERIF, size)
        greet_font = font(SERIF_BOLD, size + 1)
        sign_font = font(SERIF, size)
        ps_font = font(SERIF_ITALIC, size - 2)
        lh = int(size * 1.38)
        y = body_top
        blocks = []
        for text, kind in PARAS:
            if kind == "greet":
                f = greet_font
            elif kind == "sign":
                f = sign_font
            elif kind == "ps":
                f = ps_font
            else:
                f = body_font
            lines = wrap(d, text, f, text_w)
            blocks.append((kind, f, lines))
            y += len(lines) * lh + (12 if kind == "body" else 8)
        if y <= body_bottom:
            chosen = (size, blocks, lh)
            break
    if chosen is None:
        raise SystemExit("Letter does not fit at smallest font size")
    size, blocks, lh = chosen
    print(f"body font size: {size}")

    y = body_top
    for kind, f, lines in blocks:
        for ln in lines:
            if kind == "sign":
                lw = d.textlength(ln, font=f)
                d.text((W - margin - lw, y), ln, font=f, fill=INK)
            else:
                d.text((margin, y), ln, font=f, fill=INK)
            y += lh
        y += 12 if kind == "body" else 8

    # Footer band: steaming cup (left), sitting cat (right), wax seal
    draw_cup(d, 150, 904, s=1.05)
    draw_cat(d, 872, 912, s=1.0)
    sx, sy, sr = 700, 930, 26
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=SEAL,
              outline=(120, 30, 26), width=2)
    d.ellipse([sx - sr + 6, sy - sr + 6, sx + sr - 6, sy + sr - 6],
              outline=(200, 110, 100), width=1)
    seal_font = font(SERIF_BOLD, 26)
    sw = d.textlength("J", font=seal_font)
    d.text((sx - sw / 2, sy - 17), "J", font=seal_font, fill=(245, 220, 200))

    img.save(OUT, format="PNG", optimize=True)
    n = os.path.getsize(OUT)
    print(f"wrote {OUT}: {img.size}, {n} bytes")
    if n > 1048576:
        print("WARNING: over 1 MiB limit!")


if __name__ == "__main__":
    main()
