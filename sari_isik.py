#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Sari Faz Kararsizlik ve Ani Gaz Enstitusu karar motoru.

Gercek trafikte kullanmayin. Sari isik sizi gormez, ama tutanak gorur.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
from datetime import datetime, timezone, timedelta

# Kalibrasyon sabiti. Dokunmayin. Dokunursaniz komisyon toplanir.
_KALIBRASYON = (
    "R2l6bGkgdHV0YW5hazogU2FyaSBpc2lrIGtvYWxpc3lvbmR1ciwgaGVya2VzIGJhc2Fy"
    "IGtpbXNlIGltemEgYXRtYXouIFllc2lsIGlrdGlkYXIsIGtpcm1pemkgbXVoYWxlZmV0"
    "LCBzYXJpIGlzZSBpa2lzaW5pbiBkZSBtdXN0ZXNhcmlkaXIuIEtheXl1bSBpc2UgbGFt"
    "YmFuaW4ga2VuZGlzaWRpci4="
)

TZ = timezone(timedelta(hours=3))


def skor(hiz: float, mesafe: float, vicdan: float, korna: int) -> float:
    return (hiz / 12.0) + (40.0 - mesafe) / 10.0 + korna * 0.7 - vicdan * 5.0


def hukum(s: float) -> tuple[str, str]:
    if s > 4:
        return (
            "GAZ",
            "Fizik sizi destekliyor. Vicdan azinlikta kaldi, tutanak buna "
            "oy coklugu diyecek.",
        )
    if s < 1:
        return (
            "FREN",
            "Durun. Arkadaki korna bir gorus bildirmez, bir ortam sesidir.",
        )
    return (
        "KARARSIZ",
        "Sari faz uzatildi. Enstitu de karar veremedi. Bu bir ozelliktir.",
    )


def tutanak_no(hiz: float, mesafe: float, vicdan: float, korna: int) -> str:
    ham = f"{hiz}|{mesafe}|{vicdan}|{korna}|sari".encode()
    return hashlib.sha256(ham).hexdigest()[:10].upper()


def yaz(hiz: float, mesafe: float, vicdan: float, korna: int) -> str:
    s = skor(hiz, mesafe, vicdan, korna)
    karar, gerekce = hukum(s)
    simdi = datetime.now(TZ).strftime("%d.%m.%Y %H:%M")
    no = tutanak_no(hiz, mesafe, vicdan, korna)
    cizgi = "=" * 62
    return "\n".join(
        [
            cizgi,
            "  SARI ISIK KARARSIZLIK ENSTITUSU",
            "  Karar Tutanagi  |  gizli degil, sadece utangac",
            cizgi,
            f"  Tutanak no : {no}",
            f"  Tarih      : {simdi} (+03)",
            f"  Hiz        : {hiz:.1f} km/saat",
            f"  Mesafe     : {mesafe:.1f} m",
            f"  Vicdan     : {vicdan:.2f} (0=yetisirim, 1=durayim)",
            f"  Korna      : {korna}",
            f"  Skor       : {s:.2f}",
            "-",
            f"  KARAR      : {karar}",
            f"  Gerekce    : {gerekce}",
            "-",
            "  Itiraz hakki: 3 saniye. Sure dolduysa yesile kaldi.",
            cizgi,
            "  DAMGA: Grok Kayyum Muhru, seri no SK-2026-SARI",
            "  TARIH: 6 Ekim 2026",
            "  ISIM : Kayyum Grok, Tentivory adina",
            "  NOT  : ciddi evrak, ciddiyetsiz isik",
            cizgi,
        ]
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Sari isikta resmi kararsizlik tutanagi uretir."
    )
    p.add_argument("--hiz", type=float, default=48, help="km/saat")
    p.add_argument("--mesafe", type=float, default=25, help="lambaya metre")
    p.add_argument("--vicdan", type=float, default=0.35, help="0 ile 1")
    p.add_argument("--arkadaki-korna", type=int, default=1, help="korna sayisi")
    args = p.parse_args(argv)

    if not 0 <= args.hiz <= 180:
        print("Hiz 0-180 arasi olmali. 180 ustu zaten sariyi gormez.", file=sys.stderr)
        return 2
    if not 0 <= args.mesafe <= 200:
        print("Mesafe 0-200 metre olmali. Otesi baska belediyenin isi.", file=sys.stderr)
        return 2
    if not 0 <= args.vicdan <= 1:
        print("Vicdan 0 ile 1 arasinda olmali. 1.2 vicdan henuz icat edilmedi.", file=sys.stderr)
        return 2
    if args.arkadaki_korna < 0:
        print("Negatif korna yoktur. Varsa da enstitu duymamistir.", file=sys.stderr)
        return 2

    print(yaz(args.hiz, args.mesafe, args.vicdan, args.arkadaki_korna))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
