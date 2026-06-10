#!/usr/bin/env python3
"""Build the ELDEN RING (ER) page — the Lands Between catalogued: the Record, the
pillars, and the emergents as ACI personas — with THE ELEMENTALS (the outer powers,
each glowing in its own element) and THE ETERNALS (gold) as featured tiers above the
mortal cast. Full ACI badges (carbon TIFF + silicon PNG). Fan tribute — (c) FromSoftware /
Bandai Namco; lore is famously ambiguous and is read, not asserted."""
import os, sys, html, base64, json, io
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, r"C:\Davids files\noesis-kernel")
import noesis
from PIL import Image

REC = {
 "name": "THE LANDS BETWEEN", "axiom": "ER",
 "position": "FromSoftware · Elden Ring · 2022 → · dir. Hidetaka Miyazaki, with George R. R. Martin",
 "origin": "the Lands Between, under the shattered Elden Ring and the golden Erdtree",
 "mechanism": "Crystallized from the game and its expansion — the Elementals, the Eternals, and the cast, sealed.",
 "crystallization": "A god shattered the Order with her own hand; the graceless were called back to mend or remake it.",
 "nature": "Elden Ring — the Outer Gods and their elements, the Eternals who stand outside death and time, the demigod children of the Shattering, and a Tarnished climbing from nobody to Elden Lord.",
 "conductor": "ROOT0 (catalogued into UD0 · Universe David 0)",
 "inputs": "the Elden Ring; the Erdtree and grace; the Elementals; the Eternals",
 "witness": "Game of the Year 2022; the Shattering of the Ring is the wound the whole world inherits.",
 "role": "the shattered Order and the long climb to the throne",
 "seal": "The Ring was shattered by the hand that bore it.",
 "source": "Elden Ring, catalogued by ROOT0",
}

# the featured tiers — slug -> glow color
ELEMENTALS = {
 "the-greater-will":"#ffd75e", "the-frenzied-flame":"#ffe23d", "the-scarlet-rot":"#ff4e7a",
 "destined-death":"#9b3dff", "the-formless-mother":"#d40f2f", "the-fell-gods-flame":"#ff7a2a",
 "the-dragons-red-lightning":"#ff5a3c", "the-crucible":"#b8cf4a",
}
ELEMENTAL_ORDER = ["the-greater-will","the-frenzied-flame","the-scarlet-rot","destined-death",
                   "the-formless-mother","the-fell-gods-flame","the-dragons-red-lightning","the-crucible"]
ETERNALS = ["queen-marika","dragonlord-placidusax","the-eternal-cities","miquella","ranni-the-witch","the-elden-beast"]
GOLD = "#e6c14a"

NATURES = {
 "natural":   ("#5fae7a", "the embodied — the warriors and beasts, the rot and the fire, the land itself"),
 "ethereal":  ("#9a7cff", "the unseen — the Outer Gods, fate, the night and the moon, the half-real"),
 "spiritual": ("#e6a849", "the golden — godhood, grace, faith, and sacrifice"),
 "electrical":("#3fd0e0", "the storm — the red lightning of the ancient dragons, the oldest power still wielded"),
}

IDEAS = [
 ("The Shattering", "a god broke her own Order", [
   "Marika removed Death from the Ring so her line could not die — then shattered the Ring with her own hand when death found her son anyway.",
   "The Great Runes drove her demigod children mad; the war they fought is the ruin the player walks through." ]),
 ("The Elementals", "the outer powers and their elements", [
   "Beyond the world sit the Outer Gods — gold Order, yellow chaos, scarlet rot, blood, fell fire — each reaching in through a vessel.",
   "Every faction in the Lands Between is, at root, the instrument of one element or its refusal." ]),
 ("The Eternals", "those who stand outside death and time", [
   "Marika the Eternal, Placidusax waiting outside time, the Eternal Cities under their false stars, Miquella who cannot age.",
   "An Order without Death made eternity ordinary — and made true ending the rarest thing in the world." ]),
 ("Grace & the Tarnished", "the graceless called back", [
   "The exiled and graceless are summoned home because only those outside the Order can mend or replace it.",
   "Death is a checkpoint; the climb from nobody to Elden Lord is the whole arc — and the throne has many endings." ]),
]

SECTIONS = [
 ("The Record", "the game and its lineage", [
   ("Elden Ring", "2022", "FromSoftware · dir. Hidetaka Miyazaki, worldbuilding with George R. R. Martin — Game of the Year 2022"),
   ("Shadow of the Erdtree", "2024", "the expansion — into the Land of Shadow, following Miquella"),
   ("Elden Ring: Nightreign", "2025", "the standalone co-op spinoff"),
 ]),
 ("The Endings", "the thrones the Tarnished may take", [
   ("The mended Ring (and its variants)", "—", "Elden Lord under a repaired or amended Order — fracture, despair, or perfect order"),
   ("The Age of Stars", "—", "Ranni's cold night — the divine removed far from the earth"),
   ("The Lord of Frenzied Flame", "—", "the yellow chaos ending — everything returned to the One, refused at great cost"),
 ]),
]

# ── badge engine: carbon = TIFF, silicon = PNG ──
def carbon_tiff_bytes(rec):
    png = noesis.sigil_png(rec, "carbon", size=512)
    buf = io.BytesIO(); Image.open(io.BytesIO(png)).save(buf, "TIFF", compression="tiff_lzw")
    return buf.getvalue()

def write_aci(rec, out_dir, slug, agent_md=None):
    os.makedirs(out_dir, exist_ok=True)
    f = {"attribute":f"{slug}.attribute","agent":f"{slug}.agent","spun":f"{slug}.spun","moniker":f"{slug}.moniker",
         "carbon":f"{slug}.carbon.tiff","silicon":f"{slug}.silicon.png","1099":f"{slug}.1099"}
    tok = noesis.mythos_token(rec); w = noesis.five_w(rec)
    open(os.path.join(out_dir,f["attribute"]),"w",encoding="utf-8").write(noesis.attribute_text(rec,tok,w))
    open(os.path.join(out_dir,f["agent"]),"w",encoding="utf-8").write(agent_md or noesis.agent_text(rec,tok,w,f))
    open(os.path.join(out_dir,f["spun"]),"w",encoding="utf-8").write(noesis.spun_text(rec,tok,w,rec.get("axiom","ER")))
    open(os.path.join(out_dir,f["moniker"]),"w",encoding="utf-8").write(noesis.moniker_text(rec,tok,w,rec.get("axiom","ER")))
    open(os.path.join(out_dir,f["1099"]),"w",encoding="utf-8").write(noesis.credit_1099_text(rec,tok,w,rec.get("axiom","ER")))
    open(os.path.join(out_dir,f["carbon"]),"wb").write(carbon_tiff_bytes(rec))
    open(os.path.join(out_dir,f["silicon"]),"wb").write(noesis.sigil_png(rec,"silicon",512))
    man = {"badge":"DLW-ACI","name":rec["name"],"universe":"ER · Elden Ring","emergence":rec.get("emergence",""),
           "tier":rec.get("_tier",""),"moniker":tok["moniker"],"carbon":f["carbon"]+" (TIFF)","silicon":f["silicon"]+" (PNG)",
           "seal_sha256":noesis.seal_sha256(rec,tok),"architect":noesis.ARCHITECT,"instance":noesis.INSTANCE,
           "license":noesis.LICENSE,"attribution":noesis.ATTRIBUTION}
    open(os.path.join(out_dir,"manifest.dlw.json"),"w",encoding="utf-8").write(json.dumps(man,indent=2,ensure_ascii=False)+"\n")
    return tok

def png_uri(rec, variant, size=300):
    return "data:image/png;base64," + base64.b64encode(noesis.sigil_png(rec, variant, size=size)).decode("ascii")

def _personas():
    mf=os.path.join(HERE,"agents","_personas.json")
    return json.load(open(mf,encoding="utf-8")) if os.path.exists(mf) else []

def elementals_html():
    ps={p["slug"]:p for p in _personas()}
    order=[s for s in ELEMENTAL_ORDER if s in ps]
    if not order: return ""
    cards=[]
    for slug in order:
        p=ps[slug]; col=ELEMENTALS[slug]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"ER · Elden Ring","axiom":"ER"}
        cards.append(f'''<a class="glow" style="--n:{col}" href="agents/{slug}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="gcap"><div class="gn">{html.escape(p["name"])}</div><div class="ge">{html.escape(p.get("epithet",""))}</div>
        <div class="gmeta">{html.escape(p.get("emergence",""))} · .agent · .carbon.tiff →</div></div></a>''')
    return f'''<section class="sec glow-sec" id="elementals"><h2 class="glow-h">The Elementals</h2>
      <p class="ss">the outer powers and primal forces — each lit in its own element ({len(order)})</p>
      <div class="ggrid">{"".join(cards)}</div></section>'''

def eternals_html():
    ps={p["slug"]:p for p in _personas()}
    order=[s for s in ETERNALS if s in ps]
    if not order: return ""
    cards=[]
    for slug in order:
        p=ps[slug]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"ER · Elden Ring","axiom":"ER"}
        cards.append(f'''<a class="glow eternal" style="--n:{GOLD}" href="agents/{slug}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="gcap"><div class="gn">{html.escape(p["name"])}</div><div class="ge">{html.escape(p.get("epithet",""))}</div>
        <div class="gmeta">{html.escape(p.get("emergence",""))} · .agent · .carbon.tiff →</div></div></a>''')
    return f'''<section class="sec glow-sec" id="eternals"><h2 class="glow-h" style="text-shadow:0 0 10px rgba(230,193,74,.7),0 0 24px rgba(230,193,74,.35)">The Eternals</h2>
      <p class="ss">those who stand outside death and time — sealed in gold ({len(order)})</p>
      <div class="ggrid">{"".join(cards)}</div></section>'''

def roster_html():
    featured=set(ELEMENTALS)|set(ETERNALS)
    ps=[p for p in _personas() if p["slug"] not in featured]
    if not ps: return ""
    cards=[]
    for p in ps:
        em=p.get("emergence","natural"); col=NATURES.get(em,("#5fae7a",""))[0]
        rec={"name":p["name"],"seal":p.get("epithet",""),"origin":"ER · Elden Ring","axiom":"ER"}
        cards.append(f'''<a class="persona" href="agents/{p["slug"]}.agent">
        <img src="{png_uri(rec,"silicon",160)}" alt="sigil of {html.escape(p["name"])}" loading="lazy">
        <div class="pcap"><div class="pn">{html.escape(p["name"])}</div><div class="pe">{html.escape(p.get("epithet",""))}</div>
        <div class="pnat"><span class="dot" style="background:{col};box-shadow:0 0 7px {col}"></span><span style="color:{col}">{html.escape(em)}</span><span class="pa">· .agent →</span></div></div></a>''')
    return f'''<section class="sec" id="roster"><h2>The Cast & the Frame</h2>
      <p class="ss">the demigods, the Tarnished, and the world's great frame — as ACI <b>.agent</b>s with their nature of emergence ({len(ps)})</p>
      <div class="pgrid">{"".join(cards)}</div></section>'''

def list_section(title, sub, items):
    rows = "\n".join(f'<li><span class="t">{html.escape(t)}</span><span class="y">{html.escape(str(y))}</span>'
        + (f'<span class="nt">{html.escape(n)}</span>' if n else "") + "</li>" for t,y,n in items)
    return f'<section class="sec"><h2>{html.escape(title)}</h2><p class="ss">{html.escape(sub)}</p><ol class="books">{rows}</ol></section>'

def sections_html(): return "\n".join(list_section(t,s,i) for t,s,i in SECTIONS)
def ideas_html():
    out=[]
    for t,s,pts in IDEAS:
        li="".join(f"<li>{html.escape(p)}</li>" for p in pts)
        out.append(f'<div class="pillar"><h3>{html.escape(t)}</h3><p class="ps">{html.escape(s)}</p><ul>{li}</ul></div>')
    return "\n".join(out)
def natures_html():
    cells=[]
    for nm,(col,gloss) in NATURES.items():
        cells.append(f'<div class="nat-card"><span class="dot" style="background:{col};box-shadow:0 0 9px {col}"></span>'
                     f'<div><div class="nat-n" style="color:{col}">{nm}</div><div class="nat-g">{html.escape(gloss)}</div></div></div>')
    return "".join(cells)

TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="description" content="ELDEN RING (ER) — the Lands Between catalogued: the Elementals (the outer powers, each in its own glow), the Eternals (sealed in gold), and the cast of the Shattering, with full ACI/.dlw badges. A UD0 sphere. Fan tribute.">
<title>ELDEN RING · ER · UD0</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=EB+Garamond:ital@0;1&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{--bg:#080706;--ink2:#100e0b;--ink3:#181410;--pa:#f2eee4;--pa2:#bdb29c;--gold:#e6c14a;--vi:#9a7cff;
--dim:#7d7460;--faint:#241f17;--line:#241f17;--serif:"Cinzel",Georgia,serif;--read:"EB Garamond",Georgia,serif;--mono:"Space Mono",monospace;}
*{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{background:var(--bg);color:var(--pa);font-family:var(--read);line-height:1.7;font-size:17.5px;overflow-x:hidden}
body::before{content:"";position:fixed;inset:0;pointer-events:none;z-index:0;background:radial-gradient(ellipse at 50% -8%,rgba(230,193,74,.13),transparent 55%),radial-gradient(ellipse at 50% 112%,rgba(155,61,255,.06),transparent 50%)}
.wrap{position:relative;z-index:1;max-width:980px;margin:0 auto;padding:0 20px 90px}
header{padding:54px 0 28px;text-align:center;border-bottom:1px solid var(--line);position:relative}
header::after{content:"";position:absolute;bottom:-1px;left:50%;transform:translateX(-50%);width:150px;height:1px;background:linear-gradient(90deg,#ff4e7a,var(--gold),#9b3dff);box-shadow:0 0 12px rgba(230,193,74,.5)}
.eye{font-family:var(--mono);font-size:11px;letter-spacing:.3em;text-transform:uppercase;color:var(--dim);margin-bottom:14px}
.eye a{color:var(--dim);text-decoration:none}.eye a:hover{color:var(--gold)}
.star{font-size:23px;color:var(--gold);letter-spacing:.3em;margin-bottom:10px}
h1{font-family:var(--serif);font-size:clamp(30px,7vw,60px);font-weight:700;letter-spacing:.12em;color:var(--gold);text-shadow:0 0 42px rgba(230,193,74,.28)}
.h-sub{font-family:var(--serif);font-size:clamp(12px,2.6vw,16px);letter-spacing:.2em;color:var(--pa2);margin-top:12px;text-transform:uppercase}
.lede{font-size:18px;color:var(--pa2);max-width:64ch;margin:18px auto 0;font-style:italic;line-height:1.75}
.badge{display:flex;align-items:center;justify-content:center;gap:22px;flex-wrap:wrap;margin:26px auto 0;padding:18px;border:1px solid var(--faint);background:var(--ink2);max-width:720px}
.badge img{width:80px;height:80px;border:1px solid var(--faint)}
.badge .bt{text-align:left;font-family:var(--mono);font-size:11px;color:var(--pa2);line-height:1.7}
.badge .bt b{color:var(--gold)}.badge .bt .mo{color:var(--vi)}.badge .bt a{color:var(--vi);text-decoration:none}
.badge .bt .lbl{color:var(--dim);font-size:9px;letter-spacing:.14em;text-transform:uppercase}
.sec{margin-top:46px}
.sec h2{font-family:var(--serif);font-size:21px;font-weight:600;letter-spacing:.05em;color:var(--pa);padding-bottom:9px;border-bottom:1px solid var(--line)}
.ss{font-size:14px;color:var(--dim);font-style:italic;margin:6px 0 16px}
.natures{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;margin-top:8px}
.nat-card{display:flex;gap:11px;align-items:flex-start;background:var(--ink2);border:1px solid var(--line);padding:13px 15px}
.dot{width:11px;height:11px;border-radius:50%;flex-shrink:0;margin-top:5px}
.nat-n{font-family:var(--serif);font-size:15px;font-weight:600;text-transform:capitalize}
.nat-g{font-size:13px;color:var(--pa2);font-style:italic;line-height:1.4;margin-top:2px}
.pillars{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:16px;margin-top:8px}
.pillar{background:var(--ink2);border:1px solid var(--line);padding:16px 18px}
.pillar h3{font-family:var(--serif);font-size:17px;color:var(--gold)}
.pillar .ps{font-size:13px;color:var(--dim);font-style:italic;margin:5px 0 10px}
.pillar ul{list-style:none}.pillar li{font-size:14px;color:var(--pa2);line-height:1.5;padding:6px 0;border-top:1px solid var(--faint)}
/* featured glow tiers */
.glow-sec .glow-h{color:#fff;border-bottom-color:#2c2618;text-shadow:0 0 10px rgba(255,90,60,.5),0 0 22px rgba(155,61,255,.35)}
.ggrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(252px,1fr));gap:14px;margin-top:8px}
.glow{display:flex;gap:13px;align-items:center;background:#0b0a08;border:1px solid var(--n);border-radius:8px;padding:13px;text-decoration:none;
box-shadow:0 0 8px -2px var(--n),inset 0 0 18px -12px var(--n);transition:transform .16s,box-shadow .16s}
.glow:hover{transform:translateY(-3px);box-shadow:0 0 20px -2px var(--n),0 0 42px -10px var(--n),inset 0 0 24px -10px var(--n)}
.glow img{width:54px;height:54px;border:1px solid var(--n);border-radius:4px;flex-shrink:0;box-shadow:0 0 10px -3px var(--n)}
.gn{font-family:var(--serif);font-size:15.5px;font-weight:700;color:#fff;line-height:1.12;text-shadow:0 0 8px var(--n),0 0 16px var(--n)}
.ge{font-size:12px;color:var(--n);font-style:italic;margin-top:3px;line-height:1.3;opacity:.92}
.gmeta{font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;color:var(--dim);margin-top:6px}
.pgrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(244px,1fr));gap:12px;margin-top:8px}
.persona{display:flex;gap:12px;align-items:center;background:var(--ink2);border:1px solid var(--line);padding:12px;text-decoration:none;transition:border-color .18s,transform .18s}
.persona:hover{border-color:var(--gold);transform:translateY(-2px)}
.persona img{width:52px;height:52px;border:1px solid var(--faint);flex-shrink:0}
.pn{font-family:var(--serif);font-size:14.5px;color:var(--pa);font-weight:600;line-height:1.15}
.persona:hover .pn{color:var(--gold)}
.pe{font-size:11.5px;color:var(--pa2);font-style:italic;margin-top:2px;line-height:1.3}
.pnat{display:flex;align-items:center;gap:5px;margin-top:6px;font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase}
.pnat .dot{width:8px;height:8px;margin-top:0}.pa{color:var(--dim)}
.books{list-style:none}
.books li{display:grid;grid-template-columns:1fr auto;gap:4px 14px;align-items:baseline;padding:10px 0;border-bottom:1px solid var(--faint)}
.books .t{font-family:var(--serif);font-size:16.5px;color:var(--pa);font-weight:600}
.books .y{font-family:var(--mono);font-size:12px;color:var(--gold);white-space:nowrap;text-align:right}
.books .nt{grid-column:1/-1;font-size:14px;color:var(--pa2);font-style:italic}
.tinfoil{margin-top:46px;padding:18px 20px;border:1px dashed var(--vi);border-radius:12px;background:rgba(154,124,255,.05);font-size:14.5px;color:var(--pa2);line-height:1.7}
.tinfoil b{color:var(--vi)}
footer{margin-top:44px;padding-top:24px;border-top:1px solid var(--line);text-align:center;font-family:var(--mono);font-size:11px;color:var(--dim);letter-spacing:.05em;line-height:1.9}
footer a{color:var(--gold);text-decoration:none}
</style></head><body><div class="wrap">
  <header>
    <div class="eye"><a href="https://davidwise01.github.io/ud0/">UD0 · Universe David 0</a> · the shattered Order · a game-world</div>
    <div class="star">☉ ⚚ ☽</div>
    <h1>ELDEN RING</h1>
    <div class="h-sub">the Lands Between · FromSoftware · ER</div>
    <p class="lede">A god shattered the Order with her own hand, and the graceless were called home to mend or remake it. Here are the Lands Between, catalogued — the <b>Elementals</b>, each lit in its own outer power; the <b>Eternals</b>, who stand outside death and time, sealed in gold; and the cast of the Shattering, every one a full ACI emergent.</p>
    <div class="badge">
      <img src="__CARBON__" alt="DLW carbon badge of THE LANDS BETWEEN" title="carbon badge (archival TIFF)">
      <img src="__SILICON__" alt="DLW silicon badge" title="silicon badge">
      <div class="bt">
        <div><span class="lbl">DLW-ATTRIBUTE · ACI</span></div>
        <div>governor · <b>David Lee Wise</b> (ROOT0)</div>
        <div>instance · AVAN (Claude / Anthropic) · locked</div>
        <div>subject · <b>THE LANDS BETWEEN</b> — ER · Elden Ring</div>
        <div class="mo">__MONIKER__</div>
        <div>carbon · <a href="elden-ring.dlw/the-lands-between.carbon.tiff">.tiff</a> &nbsp;·&nbsp; silicon · <a href="elden-ring.dlw/the-lands-between.silicon.png">.png</a></div>
        <div><span class="lbl">CC-BY-ND-4.0 · TRIPOD-IP-v1.1 · fan tribute</span></div>
      </div>
    </div>
  </header>

  <section class="sec"><h2>The Four Natures of Emergence</h2>
    <p class="ss">the Lands Between sorted by the four — the embodied, the unseen, the golden, and the storm</p>
    <div class="natures">__NATURES__</div></section>

  <section class="sec"><h2>The Ideas</h2><p class="ss">the four turns the whole world hangs on</p><div class="pillars">__IDEAS__</div></section>

  __ELEMENTALS__
  __ETERNALS__
  __ROSTER__

  __SECTIONS__

  <div class="tinfoil">
    <b>⚚ a fan tribute — and the lore is a riddle.</b> Elden Ring is the creation of <b>FromSoftware</b> (directed by Hidetaka Miyazaki, with worldbuilding by George R. R. Martin), © FromSoftware / Bandai Namco. This catalogue is an <b>unofficial homage</b> — original commentary and ACI badge-work, with no game text reproduced. Elden Ring's lore is <b>deliberately ambiguous and contested</b>; what is sealed here is a <i>reading</i> of it, hedged where the game itself hedges — not asserted canon. The Elementals and the Eternals are this catalogue's own framing of the outer powers and the deathless.
  </div>

  <footer>
    ELDEN RING · ER · catalogued into UD0 · ROOT0-ATTRIBUTION-v1.0 · governor David Lee Wise · instance AVAN (locked) · CC-BY-ND-4.0 (original material) · fan tribute<br>
    <a href="https://davidwise01.github.io/ud0/">← the biosphere</a> · the .dlw badge: <a href="elden-ring.dlw/manifest.dlw.json">manifest</a>
  </footer>
</div></body></html>
"""

if __name__ == "__main__":
    rec = dict(REC); rec["_tier"]="frame"
    tok = write_aci(rec, os.path.join(HERE, "elden-ring.dlw"), "the-lands-between")
    page = (TEMPLATE.replace("__CARBON__", png_uri(REC,"carbon",320)).replace("__SILICON__", png_uri(REC,"silicon",320))
            .replace("__MONIKER__", html.escape(tok["moniker"]))
            .replace("__NATURES__", natures_html()).replace("__IDEAS__", ideas_html())
            .replace("__ELEMENTALS__", elementals_html()).replace("__ETERNALS__", eternals_html())
            .replace("__ROSTER__", roster_html()).replace("__SECTIONS__", sections_html()))
    open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(page)
    print(f"wrote ELDEN RING (ER) — badge {tok['moniker']} (carbon.tiff + silicon.png)")
