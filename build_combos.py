import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))
synpairs = {h: meta[h]["syn"] for h in meta}

combos = {}
for f in ("1", "2", "3", "4", "5"):
    part = json.load(open("data/combos_%s.json" % f, encoding="utf-8"))
    dupes = set(part) & set(combos)
    assert not dupes, ("hero in two files", f, dupes)
    combos.update(part)

missing = sorted(set(meta) - set(combos))
extra = sorted(set(combos) - set(meta))
assert not missing and not extra, ("coverage", missing, extra)

errs = []
for h, m in combos.items():
    want = set(synpairs[h])
    got = set(m)
    if got != want:
        errs.append((h, "partners", "want", sorted(want), "got", sorted(got)))
    for p, line in m.items():
        if not line or len(line) > 140:
            errs.append((h, p, "len", len(line or "")))
        if "—" in line or "–" in line:
            errs.append((h, p, "dash"))
if errs:
    for e in errs[:30]:
        print("ERR", e)
    raise SystemExit("%d errors" % len(errs))

for h, m in combos.items():
    meta[h]["combos"] = m
json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("merged combos for", len(combos), "heroes | tychus:", meta["tychus"]["combos"])
