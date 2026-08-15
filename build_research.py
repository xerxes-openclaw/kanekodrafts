import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

research = {}
for f in ("a", "b", "c", "d", "e"):
    part = json.load(open("data/research_%s.json" % f, encoding="utf-8"))
    dupes = set(part) & set(research)
    assert not dupes, ("duplicate heroes across files", f, dupes)
    research.update(part)

missing = sorted(set(meta) - set(research))
extra = sorted(set(research) - set(meta))
assert not missing and not extra, ("coverage", missing, extra)

errors = []
for slug, r in research.items():
    for field in ("syn", "beats", "loses"):
        vals = r.get(field, [])
        if not (2 <= len(vals) <= 5):
            errors.append((slug, field, "count", len(vals)))
        for v in vals:
            if v not in meta:
                errors.append((slug, field, "bad slug", v))
        if slug in vals:
            errors.append((slug, field, "self-reference"))
    plan = r.get("plan", {})
    for ph in ("early", "mid", "fight", "late"):
        line = plan.get(ph, "")
        if not line:
            errors.append((slug, "plan." + ph, "empty"))
        if len(line) > 150:
            errors.append((slug, "plan." + ph, "too long", len(line)))
        if "—" in line or "–" in line:
            errors.append((slug, "plan." + ph, "em/en dash"))
    if "—" in r.get("solo", ""):
        errors.append((slug, "solo", "em dash"))

if errors:
    for e in errors[:30]:
        print("ERROR:", e)
    raise SystemExit("validation failed: %d errors" % len(errors))

for slug, r in research.items():
    m = meta[slug]
    m["syn"] = r["syn"]
    m["beats"] = r["beats"]
    m["loses"] = r["loses"]
    m["plan"] = r["plan"]
    m["solo"] = r.get("solo", "")

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("merged", len(research), "heroes | sample etc.plan.fight:", meta["etc"]["plan"]["fight"])
print("sample illidan.plan:", meta["illidan"]["plan"])
