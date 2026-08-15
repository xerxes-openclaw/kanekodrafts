import json, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
meta = json.load(open("data/meta.json", encoding="utf-8"))

# WHY strings: patch 2.55.17 SL win rates + reasoning. Shown in the UI.
WHY = {
"garrosh":"53.6% wr + 39% ban: throw into your team is a free kill",
"johanna":"52.3% wr + 55% ban, most banned hero: safe, blind-pickable, unkillable",
"tyrael":"56.2% wr on a real sample: sanctification answers every engage",
"illidan":"57.3% wr two patches running: sustain meta suits him, feed him a healer",
"kerrigan":"57.2% wr: combo one-shots squishies, snowballs hard",
"sylvanas":"54.1% wr + 27% ban on a big sample: deletes structures, wins every map",
"whitemane":"57.4% wr: infinite mana healing through damage",
"hogger":"54.2% wr, unanimous S in every source: rage sustain + wall slams",
"gazlowe":"55.2% wr: turret zone control bullies most solo laners",
"blaze":"52.5% wr: tanky waveclear, strong on nearly every map",
"dva":"51.5% wr: two health bars, self-peel, objective stalling",
"deathwing":"52.2% wr: unstoppable stat monster, punishes cc-light comps",
"malthael":"55.4% wr: percent damage shreds tanks and bruisers",
"rexxar":"57.9% wr but thin sample: misha controls the solo lane",
"thrall":"51.4% wr on a big sample: reliable sustain bruiser",
"yrel":"56.0% wr this patch (volatile): unkillable with a healer",
"thebutcher":"51.5% wr: snowballs off stacks, punishes squishy comps",
"auriel":"52.7% wr: free healing scales with your damage dealers",
"lili":"52.2% wr: blinds shut down auto-attack comps, hard to punish",
"rehgar":"51.5% wr: ancestral denies picks, bloodlust wins brawls",
"tyrande":"52.1% wr: healer that helps delete people",
"uther":"55.5% wr: armor + stuns, best clutch healer right now",
"ana":"51.4% wr: high skill, sleep dart flips fights",
"alarak":"52.2% wr: silence combo deletes mages",
"falstad":"51.8% wr + 29% ban: global value on every big map",
"liming":"51.8% wr on a big sample: resets snowball teamfights",
"orphea":"51.8% wr: safe burst with self-sustain",
"tracer":"54.4% wr (thin sample): untouchable in good hands",
"tychus":"52.6% wr: best tank-shredder in the game",
"qhira":"51.7% wr: sustain + chain cc, underrated",
"deckard":"47.4% wr: cc toolkit is real but healing output lags",
"brightwing":"46.8% picked-wr BUT 40% ban rate: feared global healer, wins maps not fights",
"abathur":"47.3% wr BUT 20% ban: in capable hands far above his stats",
"muradin":"47.8% wr on a huge sample, but the safest tank floor in the game",
"lostvikings":"53.9% wr on 104 games: macro gods in expert hands, useless otherwise",
"etc":"48.6% wr: Mosh into a stacked team still swings games",
"malfurion":"46.8% wr, worst healer bracket this patch",
"lucio":"43.8% wr, bottom three in the game right now",
"nazeebo":"43.2% wr, second worst in the game",
"kaelthas":"45.5% wr: burst mages are down across the board",
"zuljin":"44.4% wr, falling two patches",
"stukov":"44.7% wr: silence arm is good, everything else lags",
"greymane":"45.1% wr and falling",
"genji":"48.3% wr: needs coordination solo queue rarely gives",
"diablo":"45.9% wr: needs a coordinated follow-up",
"anubarak":"47.8% wr: fine into mages, outclassed otherwise",
"stitches":"47.2% wr: hook value is real, everything else is slow",
"alexstrasza":"45.9% wr: clunky, dives eat her",
"cassia":"46.0% wr: needs ball setups",
"nova":"47.6% wr: burst without follow-through",
"medivh":"45.2% wr: pro-play hero, solo queue trap",
"probius":"below the games threshold entirely: niche zone mage",
"sgthammer":"47.7% wr: immobile siege, feast or famine",
"zagara":"48.5% wr: lane bully, falls off in fights",
"chogall":"46.0% wr duo-only oddity",
"gall":"46.0% wr duo-only oddity",
"ltmorales":"48.7% wr: single-target lock-on, dies to dive",
"mei":"47.9% wr: stall kit, low kill pressure",
"artanis":"48.0% wr: solid duelist, no engage",
"chen":"48.0% wr but 27% ban: brew sustain bullies melee, very strong lately",
"malganis":"49.6% wr: sleep + sustain, fell off after nerfs",
"varian":"50.9% wr: flexible tank or damage, jack of all trades",
"xul":"47.6% wr: push machine, weak in fights",
"imperius":"49.7% wr: solid lane, telegraphed engage",
"leoric":"50.6% wr: undying pressure, low burst",
"ragnaros":"49.2% wr: lava wave wins push maps",
"sonya":"48.3% wr: classic solo laner, dives well",
"dehaka":"50.7% wr + 14% ban: global bruiser, drags win games",
"anduin":"49.0% wr + 23% ban: pull saves, solid all-rounder",
"kharazim":"50.3% wr: dive-following healer, palm saves",
"tassadar":"49.6% wr: beam melts, needs peel",
"zarya":"51.5% wr (thin): shields eat burst combos",
"azmodan":"50.5% wr: siege + globals of dunk",
"chromie":"50.9% wr: long-range poke, punishes immobile comps",
"fenix":"49.3% wr: shield cycling, strong autos",
"guldan":"48.9% wr: sustain mage, drain tanks",
"hanzo":"50.8% wr: poke + waveclear, up this patch",
"jaina":"49.7% wr: burst + slows, classic mage",
"junkrat":"48.5% wr: zone chaos, tire picks",
"kelthuzad":"50.8% wr: chain combo one-shots, high skill",
"lunara":"49.2% wr: poison pressure, hard to catch",
"mephisto":"46.9% wr (thin sample, sources split)",
"raynor":"49.3% wr: simple, consistent, never bad",
"samuro":"45.1% wr this patch (volatile): split-push specialist",
"valeera":"54.8% wr (thin, volatile): silence bullies mages",
"valla":"49.5% wr on the biggest sample: reliable ranged damage",
"zeratul":"47.9% wr: high skill wormhole burst",
"murky":"52.0% wr (thin): egg pressure, tilts enemies",
"arthas":"49.4% wr: melee-killer aura, slows win brawls",
"maiev":"46.9% wr this patch (volatile): cage plays still win fights",
"hanamura": None,
}
WHY.pop("hanamura")

# Common-sense adjustments where raw stats mislead (ban pressure, sample size, skill floor)
ADJUST = {
"brightwing": "B",   # 40% ban rate = respect; global healer wins maps
"abathur": "B",      # 20% ban, skill floor drags wr; elite in good hands
"muradin": "B",      # huge-sample wr underrates the safest tank floor
"lostvikings": "B",  # thin sample + extreme skill floor for solo queue
"chen": "A",         # 27% ban + operator judgment (Zep): very strong lately
}

missing = [h for h in meta if h not in WHY]
extra = [h for h in WHY if h not in meta]
assert not missing and not extra, (missing, extra)

for h, m in meta.items():
    m["why"] = WHY[h]
    if h in ADJUST:
        m["tier"] = ADJUST[h]

json.dump(meta, open("data/meta.json", "w", encoding="utf-8"), ensure_ascii=False)
print("why strings:", len(WHY), "| adjustments:", ADJUST)
