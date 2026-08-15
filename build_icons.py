import json, os, re, urllib.request
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))
TIERS = ["1","4","7","10","13","16","20"]
RAW = "https://raw.githubusercontent.com/heroespatchnotes/heroes-talents/master/hero/%s.json"
FILE_OF = {}  # slugs match upstream filenames for all 90 (verified in build_kit)

# map each build talent name -> its upstream icon filename, per hero
icons_needed = set()
missing = []
for slug, m in meta.items():
    with urllib.request.urlopen(RAW % FILE_OF.get(slug, slug), timeout=30) as r:
        d = json.load(r)
    tree = d.get("talents", {})
    byname = {}
    for tier in TIERS:
        for t in tree.get(tier, []):
            byname[t["name"]] = t.get("icon", "")
    build_icons = []
    for name in m["build"]:
        ic = byname.get(name, "")
        build_icons.append(ic)
        if ic:
            icons_needed.add(ic)
        else:
            missing.append((slug, name))
    m["build_icons"] = build_icons

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("icons mapped | uniques:", len(icons_needed), "| build talents with no icon:", len(missing))
if missing[:10]:
    print("sample missing:", missing[:10])

# download the unique icons to img/talents/
os.makedirs("img/talents", exist_ok=True)
ok = fail = 0
IMG = "https://raw.githubusercontent.com/heroespatchnotes/heroes-talents/master/images/talents/%s"
for ic in sorted(icons_needed):
    dest = os.path.join("img/talents", ic)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        ok += 1; continue
    try:
        with urllib.request.urlopen(IMG % ic, timeout=30) as r:
            data = r.read()
        if data:
            open(dest, "wb").write(data); ok += 1
        else:
            fail += 1
    except Exception:
        fail += 1
print("icons downloaded ok:", ok, "| failed:", fail)
