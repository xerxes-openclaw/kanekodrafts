import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

# Evidence-based tiers, patch 2.55.17 SL win rates (hotspatchnotes/HeroesProfile data)
# blended with hpn + Icy Veins tier lists; researched 2026-08-14
TIERS = {
"anubarak":"C","artanis":"B","blaze":"A","chen":"B","dva":"A","diablo":"C","etc":"B","garrosh":"S",
"johanna":"S","malganis":"B","muradin":"C","stitches":"C","tyrael":"S","chogall":"C","dehaka":"B",
"deathwing":"A","gazlowe":"S","imperius":"B","leoric":"B","malthael":"A","ragnaros":"B","rexxar":"A",
"sonya":"B","thrall":"A","varian":"B","xul":"B","yrel":"A","thebutcher":"A","alexstrasza":"C",
"anduin":"B","auriel":"A","brightwing":"C","deckard":"C","kharazim":"B","lili":"A","lucio":"C",
"malfurion":"C","rehgar":"A","stukov":"C","tyrande":"A","uther":"A","whitemane":"S","ana":"B",
"abathur":"C","medivh":"C","tassadar":"B","zarya":"B","ltmorales":"C","alarak":"A","azmodan":"B",
"cassia":"C","chromie":"B","falstad":"A","fenix":"B","gall":"C","genji":"C","greymane":"C",
"guldan":"C","hanzo":"B","illidan":"S","jaina":"B","junkrat":"B","kaelthas":"C","kelthuzad":"B",
"kerrigan":"S","liming":"A","lunara":"B","mephisto":"B","nazeebo":"C","nova":"C","orphea":"A",
"probius":"C","raynor":"B","samuro":"B","sgthammer":"C","sylvanas":"S","tracer":"A","tychus":"A",
"valeera":"B","valla":"B","zagara":"C","zeratul":"B","zuljin":"C","murky":"B","qhira":"A",
"lostvikings":"A","arthas":"B","hogger":"S","maiev":"B","mei":"C",
}
missing = [h for h in meta if h not in TIERS]
extra = [h for h in TIERS if h not in meta]
assert not missing and not extra, (missing, extra)

changed = 0
for h, t in TIERS.items():
    if meta[h]["tier"] != t:
        changed += 1
    meta[h]["tier"] = t

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
from collections import Counter
print("tiers applied | changed:", changed, "| distribution:", dict(Counter(TIERS.values())))
