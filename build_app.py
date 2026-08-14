import json, os, sys
os.chdir(os.path.dirname(os.path.abspath(__file__)))
TPL = sys.argv[1] if len(sys.argv) > 1 else "app_template.html"
OUT = sys.argv[2] if len(sys.argv) > 2 else "index.html"

talents = json.load(open("data/talents.json", encoding="utf-8"))
meta = json.load(open("data/meta.json", encoding="utf-8"))

data = json.dumps({"talents": talents, "meta": meta}, ensure_ascii=False, separators=(",", ":"))
# ponytail: escape </script> inside JSON strings so the inline block can't be terminated early
data = data.replace("</", "<\\/")

tpl = open(TPL, encoding="utf-8").read()
marker = "/*__DATA__*/"
assert tpl.count(marker) == 1
out = tpl.split(marker)  # never .replace() with $-laden content
html = out[0] + data + out[1]
open(OUT, "w", encoding="utf-8").write(html)
print(OUT, ":", len(html), "bytes | heroes:", len(meta))
