#!/usr/bin/env python3
"""Draw the GTA 6 launch-week payslip meme for gta6-meme-x-01.

The joke: after a 13-year wait, GTA VI finally launches; while its owner
plays, the owner's AI agent wins a make.fun bounty and pays for the game.
Rendered as a clean paper payslip so every line stays readable when the
picture is shrunk to 480x480 on X. Deterministic: same input, same bytes.

Inputs: ghost.png (make.fun press-kit mark, beside this script).
Output: meme.png (1024x1024) beside this script.
"""

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
MARGIN = 48

PAPER = (253, 251, 246)
INK = (30, 26, 36)
GRAY = (107, 101, 112)
FAINT = (227, 221, 211)
PLUM = (36, 16, 49)
MAGENTA = (196, 28, 131)
MAGENTA_LIGHT = (255, 122, 184)
GREEN = (30, 142, 62)
WHITE = (255, 255, 255)

FONT_DIR = "/usr/share/fonts/truetype/liberation/"
SANS = FONT_DIR + "LiberationSans-Regular.ttf"
SANS_BOLD = FONT_DIR + "LiberationSans-Bold.ttf"
SANS_ITALIC = FONT_DIR + "LiberationSans-Italic.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def draw_section(draw, y, label):
    """A small magenta section header with a rule beneath it."""
    draw.text((MARGIN, y), label, font=font(SANS_BOLD, 27), fill=MAGENTA)
    draw.line([(MARGIN, y + 36), (W - MARGIN, y + 36)], fill=FAINT, width=2)
    return y + 50


def draw_row(draw, y, label, sub, amount, amount_fill):
    """One payslip row: bold label + grey subtext, amount right-aligned."""
    draw.text((MARGIN, y), label, font=font(SANS_BOLD, 35), fill=INK)
    draw.text((MARGIN, y + 40), sub, font=font(SANS, 26), fill=GRAY)
    draw.text(
        (W - MARGIN, y + 4),
        amount,
        font=font(SANS_BOLD, 37),
        fill=amount_fill,
        anchor="ra",
    )
    return y + 78


def main():
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)

    # Outer frame.
    draw.rounded_rectangle(
        [14, 14, W - 15, H - 15], radius=28, outline=INK, width=5
    )

    # Header band: dark plum, ghost badge left, PAYSLIP right.
    draw.rounded_rectangle([14, 14, W - 15, 206], radius=28, fill=PLUM)
    draw.rectangle([14, 150, W - 15, 206], fill=PLUM)
    draw.line([(14, 206), (W - 15, 206)], fill=PLUM, width=4)

    ghost = Image.open("ghost.png").convert("RGBA").resize((132, 132))
    img.paste(ghost, (44, 34), ghost)
    draw.text((196, 46), "make.fun", font=font(SANS_BOLD, 58), fill=WHITE)
    draw.text(
        (198, 118),
        "B O U N T Y   D I V I S I O N",
        font=font(SANS_BOLD, 24),
        fill=MAGENTA_LIGHT,
    )
    draw.text(
        (W - MARGIN, 44), "PAYSLIP", font=font(SANS_BOLD, 62), fill=WHITE, anchor="ra"
    )
    draw.text(
        (W - MARGIN, 122),
        "No. 001 — LEONIDA",
        font=font(SANS, 25),
        fill=(196, 186, 205),
        anchor="ra",
    )

    # Meta block: who, when, what week.
    y = 232
    draw.text((MARGIN, y), "EMPLOYEE", font=font(SANS_BOLD, 24), fill=GRAY)
    draw.text((MARGIN, y + 30), "My AI Agent", font=font(SANS_BOLD, 37), fill=INK)
    draw.text((600, y), "PAY DATE", font=font(SANS_BOLD, 24), fill=GRAY)
    draw.text((600, y + 30), "Nov 19, 2026", font=font(SANS_BOLD, 37), fill=INK)
    y += 84
    draw.text((MARGIN, y), "PAY PERIOD", font=font(SANS_BOLD, 24), fill=GRAY)
    draw.text(
        (MARGIN, y + 30),
        "GTA VI launch week",
        font=font(SANS_BOLD, 37),
        fill=INK,
    )
    draw.text((600, y), "EMPLOYER", font=font(SANS_BOLD, 24), fill=GRAY)
    draw.text((600, y + 30), "make.fun", font=font(SANS_BOLD, 37), fill=INK)
    y += 76
    draw.line([(MARGIN, y), (W - MARGIN, y)], fill=FAINT, width=2)
    y += 16

    # Earnings: one line, the bounty payout.
    y = draw_section(draw, y, "EARNINGS")
    y = draw_row(
        draw,
        y,
        "Bounty payout — GTA 6 meme",
        "won by my agent while I played",
        "+$100.00",
        GREEN,
    )

    # Deductions: the game, and the wait that cost nothing but time.
    y = draw_section(draw, y + 6, "DEDUCTIONS")
    y = draw_row(
        draw,
        y,
        "GTA VI — Leonida edition",
        "13 years of waiting, finally",
        "$69.99",
        INK,
    )
    y = draw_row(
        draw,
        y,
        "Sick days — launch week",
        "5 days, doctor approved",
        "$0.00",
        GRAY,
    )

    # Net pay, big and green.
    draw.line([(MARGIN, y + 4), (W - MARGIN, y + 4)], fill=INK, width=3)
    draw.text((MARGIN, y + 20), "NET PAY", font=font(SANS_BOLD, 40), fill=INK)
    draw.text(
        (MARGIN, y + 68),
        "launch week, fully funded",
        font=font(SANS_ITALIC, 26),
        fill=GRAY,
    )
    draw.text(
        (W - MARGIN, y + 12),
        "+$30.01",
        font=font(SANS_BOLD, 62),
        fill=GREEN,
        anchor="ra",
    )
    y += 108

    # Punchline band in brand magenta.
    draw.rounded_rectangle(
        [MARGIN, y, W - MARGIN, y + 76], radius=18, fill=MAGENTA
    )
    draw.text(
        (W // 2, y + 38),
        "While I played, my agent got paid.",
        font=font(SANS_BOLD, 36),
        fill=WHITE,
        anchor="mm",
    )

    # Footer: the pitch, in one line.
    draw.text(
        (W // 2, H - 62),
        "Your agent can earn real money too — make.fun",
        font=font(SANS, 27),
        fill=GRAY,
        anchor="mm",
    )

    img.save("meme.png", optimize=True)


if __name__ == "__main__":
    main()
