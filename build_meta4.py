import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

m3 = json.load(open("data/meta3.json", encoding="utf-8"))
m2 = json.load(open("data/meta2.json", encoding="utf-8"))
# key fixes
m3["lostvikings"] = m3.pop("vikings")
m2["ltmorales"] = m2.pop("morales")

# missing heroes
m4 = {
"arthas": {"tier":"B","tags":{"wc":1,"cc":2,"sustain":1},"scale":"mid","maps":["Battlefield of Eternity","Braxis Holdout","Infernal Shrines"],"syn":["jaina","kaelthas","guldan"],"beats":["illidan","tracer","genji","valla"],"loses":["greymane","tychus","fenix"],"build":["Eternal Hunger","Icy Talons","Immortal Coil","Summon Sindragosa","Frostmourne Feeds","Remorseless Winter","Legion of Northrend"],"note":"Melee-killer aura, slows win brawls"},
"hogger": {"tier":"B","tags":{"wc":1,"cc":1,"sustain":1,"camps":1},"scale":"mid","maps":["Towers of Doom","Cursed Hollow","Garden of Terror"],"syn":["deckard","malfurion"],"beats":["hanzo","junkrat"],"loses":["johanna","cassia","lili"],"build":["On the Prowl","Journeyman Cooking","Dense Blasting Powder","Hoardapult","Garbage Fire","Secret Stash","Pummel"],"note":"Rage bruiser, wall-slam combos"},
"maiev": {"tier":"A","tags":{"cc":1,"dive":1,"burst":1},"scale":"mid","maps":["Sky Temple","Cursed Hollow","Tomb of the Spider Queen"],"syn":["etc","stitches","malfurion"],"beats":["kaelthas","liming","chromie"],"loses":["johanna","lili","uther"],"build":["Sudden Vengeance","Pin Down","Bonds of Corruption","Containment Disc","Armored Assault","Shadow Strike","Warden's Fury"],"note":"Cage the fight, umbral bind cleave"},
"mei": {"tier":"A","tags":{"cc":2,"peel":2,"sustain":1},"scale":"mid","maps":["Volskaya Foundry","Hanamura Temple","Alterac Pass"],"syn":["kaelthas","jaina","garrosh"],"beats":["illidan","thebutcher","greymane"],"loses":["tychus","leoric","malthael"],"build":["Ice Storm","Heavy Pack","Crystallize","Avalanche","Cooling Servos","Icy Bribe","Flash Freeze"],"note":"Blizzard setup queen, unkillable peel"},
}

json.dump(m3, open("data/meta3.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(m2, open("data/meta2.json", "w", encoding="utf-8"), ensure_ascii=False)
json.dump(m4, open("data/meta4.json", "w", encoding="utf-8"), ensure_ascii=False)

# final merge + reconcile
talents = json.load(open("data/talents.json", encoding="utf-8"))
meta = {}
for i in (1, 2, 3, 4):
    meta.update(json.load(open("data/meta%d.json" % i, encoding="utf-8")))
missing = [k for k in talents if k not in meta]
bad = [k for k in meta if k not in talents]
print("meta:", len(meta), "| missing:", missing, "| bad keys:", bad)
json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("merged meta.json written")
