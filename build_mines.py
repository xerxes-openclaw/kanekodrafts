import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))
# Haunted Mines: small 2-lane map, big grouped fights underground, golem push.
# Strong: AoE teamfighters, camp/push heroes, waveclear that defends the golem lane.
MINES = ["etc", "malfurion", "kaelthas", "jaina", "azmodan", "zagara", "gazlowe",
         "sonya", "hogger", "xul", "stitches", "anubarak", "guldan", "leoric"]
missing = [h for h in MINES if h not in meta]
assert not missing, missing
for h in MINES:
    if "Haunted Mines" not in meta[h]["maps"]:
        meta[h]["maps"].append("Haunted Mines")
json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("Haunted Mines affinity added to", len(MINES), "heroes")
