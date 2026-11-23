#!/usr/bin/env python3
"""Porovná cs.json s anglickým originálem nainstalované noctalie.

Použití: ./kontrola.py [cesta/k/en.json]   (výchozí /usr/share/noctalia/assets/translations/en.json)
Vypíše chybějící a přebytečné klíče a texty s jinými zástupnými symboly ({name} apod.).
Návratový kód 1, pokud něco chybí nebo nesedí.
"""
import json
import os
import re
import sys

EN = sys.argv[1] if len(sys.argv) > 1 else "/usr/share/noctalia/assets/translations/en.json"
CS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cs.json")
PH = re.compile(r"\{[^{}]*\}")


def flat(d, p=""):
    out = {}
    for k, v in d.items():
        q = f"{p}.{k}" if p else k
        out.update(flat(v, q) if isinstance(v, dict) else {q: v})
    return out


en, cs = flat(json.load(open(EN))), flat(json.load(open(CS)))
chybi = sorted(en.keys() - cs.keys())
navic = sorted(cs.keys() - en.keys())
zast = sorted(k for k in en.keys() & cs.keys()
              if isinstance(en[k], str) and isinstance(cs[k], str)
              and sorted(PH.findall(en[k])) != sorted(PH.findall(cs[k])))
print(f"přeloženo {len(en.keys() & cs.keys())}/{len(en)} ({EN})")
for nadpis, seznam in (("chybí", chybi), ("navíc (v en už není)", navic),
                       ("jiné zástupné symboly", zast)):
    if seznam:
        print(f"\n{nadpis} ({len(seznam)}):")
        for k in seznam:
            print(f"  {k}" + (f"\n    en: {en[k]}\n    cs: {cs[k]}" if nadpis.startswith("jiné") else
                              f"  = {en[k]!r}" if k in en else ""))
sys.exit(1 if chybi or zast else 0)
