# -*- coding: utf-8 -*-
"""견본실 데모 9개를 썸네일로 굽는다 (assets/gallery/*.png).

fornaxworks.com/gallery.html 에 걸린 데모를 그대로 찍는다.
데모가 바뀌면 다시 돌리면 된다.

    python assets/make_gallery.py
"""
import os

from PIL import Image
from playwright.sync_api import sync_playwright

BASE = "https://fornaxworks.com/"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gallery")

SHOTS = [
    # 파일명,       경로,            뷰포트
    ("pallet", "pallet.html",  (1440, 900)),
    ("shop",   "shop.html",    (1440, 900)),
    ("mat",    "mat.html",     (1440, 900)),
    ("beacon", "landing.html", (1440, 900)),
    ("tally",  "board.html",   (1440, 900)),
    ("stamp",  "stamp.html",   (1440, 900)),
    ("bridge", "bridge.html",  (1440, 900)),
    ("index",  "guide.html",   (1440, 900)),
    ("clerk",  "clerk.html",   (1440, 900)),
]

THUMB = (720, 450)      # 2x 로 두고 README 에서 절반으로 줄여 쓴다


def main():
    os.makedirs(OUT, exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for name, path, (w, h) in SHOTS:
            pg = b.new_page(viewport={"width": w, "height": h}, device_scale_factor=1)
            pg.goto(BASE + path, wait_until="networkidle", timeout=60000)
            pg.wait_for_timeout(1200)            # 진입 애니메이션이 끝나기를 기다린다
            raw = os.path.join(OUT, name + ".raw.png")
            pg.screenshot(path=raw)
            pg.close()

            im = Image.open(raw).convert("RGB")
            # 16:10 을 8:5 썸네일로 — 위쪽을 남기고 자른다
            tw, th = THUMB
            crop_h = int(im.width * th / tw)
            im = im.crop((0, 0, im.width, min(crop_h, im.height)))
            im = im.resize(THUMB, Image.LANCZOS)
            im.quantize(colors=192, method=Image.MEDIANCUT, dither=Image.FLOYDSTEINBERG) \
              .save(os.path.join(OUT, name + ".png"), optimize=True)
            os.remove(raw)
            kb = os.path.getsize(os.path.join(OUT, name + ".png")) / 1024
            print("  %-7s %6.0fKB" % (name, kb))
        b.close()

    total = sum(os.path.getsize(os.path.join(OUT, f)) for f in os.listdir(OUT))
    print("합계 %.0fKB" % (total / 1024))


if __name__ == "__main__":
    main()
