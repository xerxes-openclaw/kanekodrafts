import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))
MAPS = ["Alterac Pass","Battlefield of Eternity","Braxis Holdout","Cursed Hollow","Dragon Shire","Garden of Terror","Hanamura Temple","Haunted Mines","Infernal Shrines","Sky Temple","Tomb of the Spider Queen","Towers of Doom","Volskaya Foundry","Warhead Junction"]

data = {}
for f in ("1", "2"):
    part = json.load(open("data/mapdata_%s.json" % f, encoding="utf-8"))
    data.update(part)

miss = [m for m in MAPS if m not in data]
assert not miss, ("missing maps", miss)

# validate slugs; sig must be a subset of strong (a definer is also strong)
bad = []
mapsig = {}
for mp, d in data.items():
    sig, strong = d.get("sig", []), d.get("strong", [])
    for s in sig + strong:
        if s not in meta:
            bad.append((mp, s))
    strong = list(dict.fromkeys(strong + sig))  # ensure sig heroes are in strong too
    data[mp]["strong"] = strong
    mapsig[mp] = sig
if bad:
    print("BAD SLUGS:", bad[:20]); raise SystemExit("bad slugs")

# rebuild each hero's maps[] from the strong lists
for h in meta:
    meta[h]["maps"] = [mp for mp in MAPS if h in data[mp]["strong"]]

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(mapsig, open("data/mapsig.json", "w", encoding="utf-8"), ensure_ascii=False)
print("maps rebuilt | BoE sig:", mapsig["Battlefield of Eternity"])
print("BoE strong:", data["Battlefield of Eternity"]["strong"])
