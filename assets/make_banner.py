# -*- coding: utf-8 -*-
"""프로필 배너(assets/banner.gif)를 굽는다.

fornaxworks.com 의 og.py 와 같은 모티프 — 화로자리 마크, 담금질 산화색
스펙트럼, 입자로 그린 고리 — 를 쓰되 고리를 도는 열을 한 바퀴 돌린다.

    python assets/make_banner.py

프레임마다 random.Random(7) 을 다시 만들어 입자 위치를 고정하고,
밝기만 각도에 따라 흔든다. 위치가 흔들리면 잔상이 지저분해진다.
"""
import math
import os
import random

from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1000, 416
FRAMES = 36
MS = 110
COLORS = 128
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "banner.gif")

BG = (8, 9, 13)
RING = (782, 205, 172)          # cx, cy, R

# og.py 의 --spectrum 과 같은 정지점
STOPS = [(0.00, (255, 176, 32)), (0.18, (255, 138, 43)), (0.34, (255, 107, 53)),
         (0.54, (232, 70, 124)), (0.76, (168, 85, 247)), (1.00, (59, 158, 255))]

FONT_R = "C:/Windows/Fonts/malgun.ttf"
FONT_B = "C:/Windows/Fonts/malgunbd.ttf"


def spectrum(t):
    t = min(1.0, max(0.0, t))
    for i in range(len(STOPS) - 1):
        a, ca = STOPS[i]
        b, cb = STOPS[i + 1]
        if a <= t <= b:
            u = 0 if b == a else (t - a) / (b - a)
            return tuple(int(ca[j] + (cb[j] - ca[j]) * u) for j in range(3))
    return STOPS[-1][1]


def band(w, h, lo=0.0, hi=1.0):
    """가로 그러데이션 타일 — 글자·마크를 마스크로 뚫어 쓴다"""
    g = Image.new("RGB", (w, h))
    px = g.load()
    for x in range(w):
        c = spectrum(lo + (hi - lo) * (x / max(1, w - 1)))
        for y in range(h):
            px[x, y] = c
    return g


def glow(im, cx, cy, r, color, a):
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(lay).ellipse([cx - r, cy - r, cx + r, cy + r], fill=color + (a,))
    im.alpha_composite(lay.filter(ImageFilter.GaussianBlur(r * 0.42)))


def heat(ang, phase):
    """고리를 한 바퀴 도는 열 — 0..1 을 한 번 돌면 제자리라 이음매가 없다"""
    return 0.42 + 0.58 * (0.5 + 0.5 * math.cos(ang - math.tau * phase)) ** 1.6


def particles(im, phase):
    rnd = random.Random(7)
    d = ImageDraw.Draw(im, "RGBA")
    cx, cy, R = RING

    def put(x, y, dim=1.0):
        if not (490 < x < W + 34 and -34 < y < H + 34):
            return
        rr = rnd.choice([1, 1, 1.5, 1.5, 2, 2, 2.5, 3, 3.5])
        t = (x - (cx - R)) / (2.0 * R)
        c = spectrum(min(0.78, max(0.0, t * 0.78)))
        a = rnd.uniform(70, 235) * dim * heat(math.atan2(y - cy, x - cx), phase)
        d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=c + (int(min(255, a)),))

    for _ in range(1500):                       # 고리
        th = rnd.uniform(0, math.tau)
        j = rnd.gauss(0, 9.5)
        put(cx + (R + j) * math.cos(th), cy + (R + j) * math.sin(th))
    for _ in range(520):                        # 가로로 지나는 선
        x = rnd.uniform(cx - R - 26, cx + R + 26)
        put(x, cy + rnd.gauss(0, 8.5))
    for _ in range(300):                        # 흩어진 잔별
        put(rnd.uniform(510, W + 16), rnd.uniform(16, H - 16), 0.5)

    d2 = ImageDraw.Draw(im, "RGBA")             # 배경 별 — 움직이지 않는다
    for _ in range(150):
        x, y = rnd.uniform(0, W), rnd.uniform(0, H)
        rr = rnd.choice([0.7, 0.9, 1.2])
        d2.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(244, 246, 250, rnd.randint(18, 70)))


def mark(im, x, y, size):
    """화로자리 — 크기 다른 별 셋을 옅은 선으로 잇는다"""
    S, ss = size / 24.0, 4      # 계단이 안 보이게 4배로 그린 뒤 줄인다
    m = Image.new("L", (int(size * ss), int(size * ss)), 0)
    dm = ImageDraw.Draw(m)
    P = [(11.60, 8.62, 4.06), (4.41, 16.74, 2.90), (19.96, 13.02, 2.44)]
    q = lambda i: (P[i][0] * S * ss, P[i][1] * S * ss)
    for a, b in ((1, 0), (0, 2)):
        dm.line([q(a), q(b)], fill=204, width=int(1.70 * S * ss))
    for px, py, pr in P:
        cx, cy, r = px * S * ss, py * S * ss, pr * S * ss
        dm.ellipse([cx - r, cy - r, cx + r, cy + r], fill=255)
    m = m.resize((int(size), int(size)), Image.LANCZOS)
    im.paste(band(int(size), int(size), 0.0, 0.85).convert("RGBA"), (x, y), m)


def spaced(d, xy, text, font, fill, extra):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill)
        x += d.textlength(ch, font=font) + extra
    return x


def frame(phase, fonts):
    f_word, f_lede, f_head, f_site = fonts
    im = Image.new("RGBA", (W, H), BG + (255,))

    # 고리를 도는 열을 배경 빛무리도 같이 따라간다
    gx = RING[0] + RING[2] * 0.42 * math.cos(math.tau * phase)
    gy = RING[1] + RING[2] * 0.42 * math.sin(math.tau * phase)
    glow(im, gx, gy, 250, (255, 138, 43), 60)
    glow(im, 124, 392, 216, (232, 70, 124), 24)
    particles(im, phase)

    d = ImageDraw.Draw(im)
    mark(im, 64, 46, 35)
    spaced(d, (113, 50), "FORNAX", f_word, (244, 246, 250), 4)

    d.text((65, 140), "아이디어를", font=f_lede, fill=(150, 158, 176))
    d.text((65, 195), "출하 가능한 제품으로", font=f_head, fill=(244, 246, 250))

    last = "벼립니다."                          # 마지막 줄만 담금질색
    wl = int(d.textlength(last, font=f_head)) + 8
    mk = Image.new("L", (wl, 68), 0)
    ImageDraw.Draw(mk).text((0, 0), last, font=f_head, fill=255)
    im.paste(band(wl, 68, 0.02, 0.80).convert("RGBA"), (65, 258), mk)

    d.rectangle([65, 340, 215, 343], fill=(255, 176, 32))
    d.text((65, 358), "fornaxworks.com", font=f_site, fill=(255, 176, 32))
    return im.convert("RGB")


def main():
    fonts = (ImageFont.truetype(FONT_B, 33), ImageFont.truetype(FONT_R, 40),
             ImageFont.truetype(FONT_B, 45), ImageFont.truetype(FONT_B, 20))
    frames = [frame(i / FRAMES, fonts) for i in range(FRAMES)]

    # 팔레트를 첫 장으로 한 번만 뽑아 프레임끼리 색이 튀지 않게 한다
    pal = frames[0].quantize(colors=COLORS, method=Image.MEDIANCUT)
    frames = [f.quantize(palette=pal, dither=Image.FLOYDSTEINBERG) for f in frames]

    frames[0].save(OUT, save_all=True, append_images=frames[1:],
                   duration=MS, loop=0, optimize=True, disposal=1)
    print("banner.gif %dx%d · %d frames · %.1fMB"
          % (W, H, FRAMES, os.path.getsize(OUT) / 1048576))


if __name__ == "__main__":
    main()
