import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

tips = {}
for f in ("a", "b", "c"):
    part = json.load(open("data/traits_%s.json" % f, encoding="utf-8"))
    dupes = set(part) & set(tips)
    assert not dupes, ("hero in two files", f, dupes)
    tips.update(part)

missing = sorted(set(meta) - set(tips))
extra = sorted(set(tips) - set(meta))
assert not missing and not extra, ("coverage", missing, extra)

errs = []
for h, tip in tips.items():
    if tip and len(tip) > 200:
        errs.append((h, "len", len(tip)))
    if tip and ("—" in tip or "–" in tip):
        errs.append((h, "dash"))
if errs:
    for e in errs[:20]:
        print("ERR", e)
    raise SystemExit("%d errors" % len(errs))

active = 0
for h, tip in tips.items():
    meta[h]["trait_tip"] = tip
    if tip:
        active += 1
json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("trait tips merged | active:", active, "| passive/empty:", 90 - active)
print("rehgar:", repr(meta["rehgar"]["trait_tip"]))
