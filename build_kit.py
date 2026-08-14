import json, os, re, urllib.request
os.chdir(os.path.dirname(os.path.abspath(__file__)))

talents = json.load(open("data/talents.json", encoding="utf-8"))
meta = json.load(open("data/meta.json", encoding="utf-8"))

RAW = "https://raw.githubusercontent.com/heroespatchnotes/heroes-talents/master/hero/%s.json"
CC_RE = re.compile(r"\b(stun|root|silenc|sleep|polymorph|time stop|freez|mind control|taunt)\w*", re.I)

# ltmorales/lostvikings live under different filenames upstream
FILE_OF = {"ltmorales": "ltmorales", "lostvikings": "lostvikings"}

abilities = {}
for slug in talents:
    fn = FILE_OF.get(slug, slug)
    with urllib.request.urlopen(RAW % fn, timeout=30) as r:
        d = json.load(r)
    flat = []
    for unit, abs_ in d.get("abilities", {}).items():
        for a in abs_:
            if a.get("type") in ("basic", "heroic", "trait"):
                flat.append({"name": a["name"], "desc": a.get("description", ""), "type": a["type"]})
    abilities[slug] = flat

json.dump(abilities, open("data/abilities.json", "w", encoding="utf-8"), ensure_ascii=False)
print("abilities fetched:", len(abilities))

def classify_heroic(desc):
    d = desc.lower()
    if re.search(r"stun|root|silenc|polymorph|sleep|time stop|imprison|cage|pull", d): return "lockdown"
    if re.search(r"heal|restor|shield|protect|invulnerab", d): return "save"
    if re.search(r"damage", d): return "burst"
    return "utility"

for slug, m in meta.items():
    kit = {}
    # base-kit cc ability (basic only, not heroic) for "save X for Y" goals
    cc = next((a["name"] for a in abilities[slug] if a["type"] == "basic" and CC_RE.search(a["desc"])), None)
    if cc: kit["cc"] = cc
    h10 = m["build"][3] if len(m["build"]) > 3 else None
    if h10:
        tinfo = next((t for t in talents[slug]["talents"].get("10", []) if t["name"] == h10), None)
        kit["h10"] = h10
        kit["h10type"] = classify_heroic(tinfo["description"] if tinfo else "")
    m["kit"] = kit

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
cc_count = sum(1 for m in meta.values() if m["kit"].get("cc"))
print("kits built | heroes with cc ability:", cc_count, "| sample brightwing:", meta["brightwing"]["kit"], "| etc:", meta["etc"]["kit"])
