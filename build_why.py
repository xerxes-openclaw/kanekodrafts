import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

why = {}
for f in "123456":
    part = json.load(open("data/why_%s.json" % f, encoding="utf-8"))
    dupes = set(part) & set(why)
    assert not dupes, ("hero in two files", f, dupes)
    why.update(part)

missing = sorted(set(meta) - set(why))
extra = sorted(set(why) - set(meta))
assert not missing and not extra, ("coverage", missing, extra)

errs = []
for h, m in meta.items():
    reasons = why[h]
    row = []
    for name in m["build"]:
        r = reasons.get(name, "")
        row.append(r)
        if not r:
            errs.append((h, "missing reason", name))
        elif len(r) > 160:
            errs.append((h, "len", name, len(r)))
        elif "—" in r or "–" in r:
            errs.append((h, "dash", name))
    m["build_why"] = row
if errs:
    for e in errs[:30]:
        print("ERR", e)
    raise SystemExit("%d errors" % len(errs))

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("build_why merged for", len(why), "heroes")
print("etc sample:")
for n, r in zip(meta["etc"]["build"], meta["etc"]["build_why"]):
    print("  ", n, "::", r)
