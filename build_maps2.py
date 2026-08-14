import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

# Researched per-map strength lists (Icy Veins current-patch map tier lists x heroescounters, 2026-08-14)
MAP_HEROES = {
"Alterac Pass": ["johanna","blaze","hogger","falstad","sylvanas","brightwing","rehgar","jaina","stukov","yrel","anduin"],
"Battlefield of Eternity": ["valla","zuljin","tychus","greymane","artanis","sylvanas","liming","yrel","raynor","lunara","imperius","whitemane"],
"Braxis Holdout": ["rexxar","garrosh","sylvanas","chromie","genji","zuljin","blaze","guldan","johanna","stukov","tassadar","fenix","ragnaros"],
"Cursed Hollow": ["falstad","brightwing","dehaka","zeratul","etc","abathur","liming","genji","johanna","sylvanas","lostvikings","rehgar"],
"Dragon Shire": ["falstad","brightwing","rexxar","dehaka","yrel","thrall","leoric","zeratul","johanna","rehgar","lunara","sylvanas"],
"Garden of Terror": ["johanna","sylvanas","rehgar","zeratul","blaze","brightwing","falstad","dehaka","samuro","lostvikings","valla","hogger","murky"],
"Hanamura Temple": ["blaze","sylvanas","zuljin","brightwing","falstad","genji","lucio","varian","dva","tracer","rexxar"],
"Haunted Mines": ["sylvanas","blaze","hogger","brightwing","johanna","jaina","sonya","yrel","arthas","ragnaros","malthael","tassadar"],
"Infernal Shrines": ["johanna","sonya","kerrigan","sylvanas","blaze","xul","guldan","kaelthas","ragnaros","leoric","rehgar","mephisto"],
"Sky Temple": ["falstad","brightwing","dehaka","zagara","samuro","sonya","johanna","zeratul","thrall","rehgar","sylvanas","blaze"],
"Tomb of the Spider Queen": ["sylvanas","johanna","blaze","garrosh","xul","jaina","kaelthas","ragnaros","azmodan","zagara","mephisto","guldan"],
"Towers of Doom": ["falstad","brightwing","dehaka","sylvanas","chromie","liming","johanna","garrosh","zagara","hogger","tracer","zeratul"],
"Volskaya Foundry": ["blaze","lucio","nazeebo","deckard","johanna","zeratul","kaelthas","hogger","garrosh","mei","dva","maiev"],
"Warhead Junction": ["falstad","brightwing","dehaka","zagara","abathur","lostvikings","nazeebo","zeratul","illidan","samuro","sylvanas","murky"],
}

bad = [h for hs in MAP_HEROES.values() for h in hs if h not in meta]
assert not bad, bad

# wholesale replacement: researched data supersedes hand-curation
for m in meta.values():
    m["maps"] = []
for mapname, heroes in MAP_HEROES.items():
    for h in heroes:
        meta[h]["maps"].append(mapname)

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
mapless = sum(1 for m in meta.values() if not m["maps"])
print("maps rebuilt | heroes with no map affinity:", mapless, "| falstad:", meta["falstad"]["maps"])
