#!/usr/bin/env python3
# STRATA CANON — Plate Nº 01  (BuildTrack / Murehwa villa, worn as subtle soul)
import base64, pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "fonts"

def b64(p):
    return base64.b64encode((FONTS / p).read_bytes()).decode()

face = f"""
@font-face{{font-family:'Barlow';src:url(data:font/ttf;base64,{b64('BarlowCondensed-Light.ttf')}) format('truetype');font-weight:300}}
@font-face{{font-family:'Barlow';src:url(data:font/ttf;base64,{b64('BarlowCondensed-Regular.ttf')}) format('truetype');font-weight:400}}
@font-face{{font-family:'Mono';src:url(data:font/ttf;base64,{b64('SpaceMono-Regular.ttf')}) format('truetype')}}
@font-face{{font-family:'Corm';src:url(data:font/ttf;base64,{b64('Cormorant.ttf')}) format('truetype')}}
"""

# ---------- palette ----------
BONE   = "#E9E3D4"   # warm vellum
BONE2  = "#E1DAC8"
INK    = "#17231C"
FAINT  = "#17231C"   # used with opacity
G0     = "#1c471c"   # deepest sediment
G1     = "#276F27"
G2     = "#499A13"
G3     = "#8ECA3C"
LIME   = "#BBDC12"   # spent exactly once

W, H = 1000, 1414
M = 96
R = W - M            # 904
CW = R - M           # 808

el = []
def add(s): el.append(s)

def line(x1,y1,x2,y2,stroke=INK,w=1,op=1,dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{w}" stroke-opacity="{op}"{d}/>')

def txt(x,y,s,size,fam="Mono",fill=INK,weight=400,anchor="start",ls=0,op=1,style=""):
    st=f'letter-spacing:{ls}px;' if ls else ""
    st+=style
    add(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" '
        f'fill="{fill}" fill-opacity="{op}" text-anchor="{anchor}" style="{st}">{s}</text>')

def cross(x,y,s=9,w=1,op=.75):
    line(x-s,y,x+s,y,INK,w,op); line(x,y-s,x,y+s,INK,w,op)

# ---------- background ----------
add(f'<rect width="{W}" height="{H}" fill="{BONE}"/>')
# subtle vertical vellum tone on the right third
add(f'<rect x="{W*0.62:.0f}" y="0" width="{W*0.38:.0f}" height="{H}" fill="{BONE2}" opacity="0.5"/>')
# faint framing rule
add(f'<rect x="{M-16}" y="{M-16}" width="{CW+32}" height="{H-2*(M-16)}" fill="none" stroke="{INK}" stroke-opacity="0.16" stroke-width="1"/>')

# ---------- top register ----------
txt(M, M-30, "PLATE&#160;Nº&#160;01", 12.5, "Mono", INK, ls=2)
txt(M, M-14, "STRATA CANON", 12.5, "Mono", INK, ls=2, op=.55)
txt(R, M-30, "17.6478°&#8201;S", 12.5, "Mono", INK, anchor="end", ls=1)
txt(R, M-14, "31.6353°&#8201;E", 12.5, "Mono", INK, anchor="end", ls=1, op=.55)
line(M, M+2, R, M+2, INK, 1, .55)
# margin ticks along the top rule
for i in range(0,49):
    x = M + CW*i/48
    line(x, M+2, x, M+ (7 if i%6==0 else 4), INK, 1, .32)

# ---------- monumental word ----------
txt(W/2, 158, "A SECTION THROUGH THE MAKING OF A DWELLING", 12.5, "Mono", INK, anchor="middle", ls=4, op=.6)
txt(W/2, 300, "IMBA", 176, "Barlow", INK, weight=300, anchor="middle", ls=26)
txt(W/2, 345, "n. &#8194;the raised shelter&#8194;·&#8194;chiShona", 26, "Corm", INK, anchor="middle", op=.85,
    style="font-variation-settings:'wght' 400;font-style:italic;")

# ============================================================
#   THE SECTION PLATE
# ============================================================
cx = 500
bw = 300
bx0, bx1 = cx-bw/2, cx+bw/2      # 350 .. 650
GL = 980                          # ground line y

# strata geometry (y-top, y-bottom, colour, brick, roman, label, sub)
strata = [
    # parapet + hidden roof
    (585, 650, G3, False, "V",   "PARAPET · HIDDEN ROOF", "0.47&#8201;mm IBR · 12° fall"),
    # first floor
    (660, 810, G2, True,  "IV",  "FIRST FLOOR", "Y16 / Y12 · 8 bedrooms"),
    # ground floor
    (824, 962, G1, True,  "III", "GROUND FLOOR", "3.00&#8201;m · deck 225&#8201;m²"),
    # slab
    (962, 980, G0, False, "II",  "GROUND SLAB", "100&#8201;mm · 295&#8201;m²"),
    # foundation (below ground)
    (980, 1044, G0, "rubble", "I", "SUBSTRUCTURE", "1.00&#8201;m · strip footing"),
]

# brick pattern defs
defs = ['<defs>']
defs.append(
 f'<pattern id="brick" width="17" height="10" patternUnits="userSpaceOnUse">'
 f'<rect width="17" height="10" fill="none"/>'
 f'<rect x="0.6" y="0.6" width="15.8" height="3.8" fill="#ffffff" fill-opacity="0.10"/>'
 f'<rect x="-7.9" y="5.6" width="15.8" height="3.8" fill="#ffffff" fill-opacity="0.10"/>'
 f'<rect x="8.9" y="5.6" width="15.8" height="3.8" fill="#ffffff" fill-opacity="0.10"/>'
 f'<path d="M0 5 H17 M0 0 H17 M8.5 5 V10 M0 5 V10 M17 5 V10 M0.5 0 V5 M17 0 V5" '
 f'stroke="{INK}" stroke-opacity="0.16" stroke-width="0.5"/>'
 f'</pattern>')
defs.append(
 f'<pattern id="rubble" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(0)">'
 f'<rect width="14" height="14" fill="none"/>'
 f'<circle cx="4" cy="4" r="2.1" fill="{INK}" fill-opacity="0.22"/>'
 f'<circle cx="10" cy="9" r="1.6" fill="{INK}" fill-opacity="0.18"/>'
 f'<circle cx="1" cy="11" r="1.3" fill="{INK}" fill-opacity="0.16"/>'
 f'</pattern>')
defs.append('</defs>')
add("".join(defs))
add('<g transform="translate(0,-82)">')

# --- earth below ground line ---
for i in range(0, 34):
    x = 300 + (400)*i/33
    line(x, GL, x-14, GL+26, INK, 1, .28)
line(300, GL, 700, GL, INK, 1.4, .9)   # ground datum

# --- draw strata bands ---
for (yt,yb,col,brick,rom,lab,sub) in strata:
    if rom == "I":
        # stepped footing wider
        add(f'<rect x="{bx0-15:.1f}" y="{yt:.1f}" width="{bw+30:.1f}" height="{yb-yt:.1f}" fill="{col}"/>')
        add(f'<rect x="{bx0-15:.1f}" y="{yt:.1f}" width="{bw+30:.1f}" height="{yb-yt:.1f}" fill="url(#rubble)"/>')
    else:
        add(f'<rect x="{bx0:.1f}" y="{yt:.1f}" width="{bw:.1f}" height="{yb-yt:.1f}" fill="{col}"/>')
        if brick is True:
            add(f'<rect x="{bx0:.1f}" y="{yt:.1f}" width="{bw:.1f}" height="{yb-yt:.1f}" fill="url(#brick)"/>')

# --- suspended mid-slab deck + ring beam (ink seams) ---
add(f'<rect x="{bx0:.1f}" y="810" width="{bw:.1f}" height="14" fill="{INK}"/>')      # mid deck
add(f'<rect x="{bx0:.1f}" y="650" width="{bw:.1f}" height="10" fill="{INK}"/>')      # ring beam

# --- parapet stepped top (hiding roof) ---
steps = 6
sw = bw/steps
top_y = 585
path = [f"M{bx0:.1f} {top_y+18:.1f}"]
for i in range(steps):
    x = bx0 + i*sw
    hy = top_y + (6 if i%2 else 0)
    path.append(f"L{x:.1f} {hy:.1f} L{x+sw:.1f} {hy:.1f}")
path.append(f"L{bx1:.1f} {top_y+18:.1f} Z")
add(f'<path d="{"".join(path)}" fill="{G3}"/>')
# recolor thin cap line
line(bx0, top_y, bx1, top_y, INK, 1, .35)

# --- hidden roof: dashed pitched line inside upper storey ---
line(bx0+10, 612, bx1-10, 646, INK, 1, .8, dash="2 4")

# --- window openings (bone cuts) : ground + first floor ---
def window(x,y,w,h):
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="{BONE}"/>')
    add(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="0.8"/>')
    line(x+w/2, y, x+w/2, y+h, INK, .8, .5)
    line(x, y+h/2, x+w, y+h/2, INK, .8, .5)
for wx in (375, 430, 512, 567):
    window(wx, 700, 30, 40)   # first floor
for wx in (375, 512, 567):
    window(wx, 872, 30, 46)   # ground floor
# a doorway
add(f'<rect x="432" y="900" width="34" height="62" fill="{BONE}"/>')
add(f'<rect x="432" y="900" width="34" height="62" fill="none" stroke="{INK}" stroke-opacity="0.5" stroke-width="0.8"/>')

# --- building outline ---
add(f'<rect x="{bx0:.1f}" y="{top_y:.1f}" width="{bw:.1f}" height="{980-top_y:.1f}" fill="none" stroke="{INK}" stroke-opacity="0.55" stroke-width="1.2"/>')

# ---------- left vertical scale ----------
sx = 300
line(sx, 585, sx, 1044, INK, 1, .5)
# metres: ground=0 at GL(980); above +, below -
def y_for_m(m):  # 60 px per metre
    return GL - m*60.0
for m in range(-1, 7):
    y = y_for_m(m)
    if y < 580 or y > 1050: continue
    long = (m % 1 == 0)
    line(sx-8 if long else sx-5, y, sx, y, INK, 1, .5)
    txt(sx-14, y+3.5, f"{m:+d}" if m else "0", 10.5, "Mono", INK, anchor="end", op=.7)
    if m == 0:  # the single lime accent — datum benchmark, spent once
        add(f'<path d="M{sx:.0f} {y-7:.0f} l14 7 l-14 7 Z" fill="{LIME}"/>')
        add(f'<circle cx="{sx}" cy="{y:.0f}" r="1.6" fill="{INK}"/>')
txt(sx-14, 566, "m", 10.5, "Mono", INK, anchor="end", op=.6)

# ---------- right annotations (leaders) ----------
ax = 690
for (yt,yb,col,brick,rom,lab,sub) in strata:
    my = (yt+yb)/2
    line(bx1+ (15 if rom=='I' else 0), my, ax, my, INK, 1, .55)
    add(f'<circle cx="{ax}" cy="{my:.1f}" r="2.4" fill="{INK}"/>')
    txt(ax+12, my-4, f"{rom}", 12, "Mono", INK, op=.9, ls=1)
    txt(ax+40, my-4, lab, 12.5, "Barlow", INK, weight=400, ls=1.5)
    txt(ax+40, my+11, sub, 10.5, "Mono", INK, op=.62)

# section caption
txt(cx, 1072, "SECTION&#8201;A—A&#8194;·&#8194;DOUBLE-STOREY VILLA&#8194;·&#8194;SCALE 1:100", 10.5, "Mono", INK, anchor="middle", op=.6, ls=1)
add('</g>')  # close section group

# ============================================================
#   FIGURES  (clinical marginalia)
# ============================================================
fy = 1150
line(M, fy, R, fy, INK, 1, .5)
figs = [("80,000","FIRED UNITS"),("295 m²","GROSS FOOTPRINT"),("USD 36,160","STRUCTURAL SHELL"),("06","STRATA")]
for i,(n,l) in enumerate(figs):
    cxf = M + CW*(i+0.5)/4
    txt(cxf, fy+40, n, 25, "Mono", INK, anchor="middle", ls=1)
    txt(cxf, fy+60, l, 10, "Mono", INK, anchor="middle", op=.6, ls=2)
    if i>0:
        line(M+CW*i/4, fy+8, M+CW*i/4, fy+70, INK, 1, .3)
line(M, fy+82, R, fy+82, INK, 1, .5)

# ---------- accumulation legend : tiny brick swatch ----------
lgx, lgy = M, 1268
for r in range(2):
    for c in range(9):
        add(f'<rect x="{lgx+c*17:.0f}" y="{lgy+r*10:.0f}" width="15.8" height="3.8" fill="{INK}" fill-opacity="0.28"/>')
txt(lgx+9*17+10, lgy+7, "▸&#8194;each course &#8194;≈&#8194;patient repetition", 9.5, "Mono", INK, op=.6)

# ---------- colophon ----------
txt(W/2, 1298, "BUILDTRACK&#8194;·&#8194;MUREHWA VILLA&#8194;·&#8194;MASHONALAND EAST&#8194;·&#8194;MMXXVI",
    11, "Mono", INK, anchor="middle", op=.7, ls=2)

# ---------- corner registration ----------
for (x,y) in [(M,M),(R,M),(M,H-M),(R,H-M)]:
    cross(x,y,9,1,.7)

svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
       f'viewBox="0 0 {W} {H}"><style>{face}text{{-webkit-font-smoothing:antialiased}}</style>'
       + "".join(el) + "</svg>")

html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{face}'
        f'*{{margin:0;padding:0}}html,body{{width:{W}px;height:{H}px}}'
        f'@page{{size:264.58mm 374.11mm;margin:0}}'
        f'</style></head><body>{svg}</body></html>')
(HERE/"poster.html").write_text(html)
(HERE/"poster.svg").write_text(svg)
print("wrote poster.html / poster.svg")
