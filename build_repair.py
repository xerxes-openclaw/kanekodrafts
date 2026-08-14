import json, os, difflib
os.chdir(os.path.dirname(os.path.abspath(__file__)))

talents = json.load(open("data/talents.json", encoding="utf-8"))
meta = json.load(open("data/meta.json", encoding="utf-8"))

TIERS = ["1", "4", "7", "10", "13", "16", "20"]
kept = fixed = defaulted = 0

for slug, m in meta.items():
    tree = talents[slug]["talents"]
    new_build = []
    for i, tier in enumerate(TIERS):
        tier_names = [t["name"] for t in tree.get(tier, [])]
        if not tier_names:
            continue
        want = m["build"][i] if i < len(m["build"]) else None
        if want in tier_names:
            new_build.append(want); kept += 1
            continue
        # try close match within this tier first, then across the tree mapped back to this tier
        close = difflib.get_close_matches(want or "", tier_names, n=1, cutoff=0.6)
        if close:
            new_build.append(close[0]); fixed += 1
            continue
        # cross-tier close match: maybe I put the right name on the wrong slot; find it anywhere
        all_names = {t["name"]: tr for tr in TIERS for t in tree.get(tr, [])}
        cross = difflib.get_close_matches(want or "", list(all_names.keys()), n=1, cutoff=0.75)
        if cross and all_names[cross[0]] == tier:
            new_build.append(cross[0]); fixed += 1
            continue
        new_build.append(tier_names[0]); defaulted += 1
    m["build"] = new_build
    for field in ("syn", "beats", "loses"):
        m[field] = ["ltmorales" if r == "morales" else r for r in m[field]]

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("slots kept:", kept, "| close-fixed:", fixed, "| defaulted:", defaulted)

# final validation: zero invalid names allowed
bad = 0
for slug, m in meta.items():
    tree = talents[slug]["talents"]
    for i, tier in enumerate(TIERS[:len(m["build"])]):
        names = [t["name"] for t in tree.get(tier, [])]
        if names and m["build"][i] not in names:
            bad += 1
            print("STILL BAD:", slug, i, m["build"][i])
refs_bad = [(s, f, r) for s, m in meta.items() for f in ("syn","beats","loses") for r in m[f] if r not in meta]
print("final invalid talent slots:", bad, "| invalid refs:", refs_bad)
