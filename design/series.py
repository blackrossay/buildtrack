#!/usr/bin/env python3
# STRATA CANON — the series (Plates 02–04) + combined book PDF
# Same visual DNA as Plate 01; each plate a distinct chapter of one build.
import base64, pathlib

HERE = pathlib.Path(__file__).parent
FONTS = HERE / "fonts"
def b64(p): return base64.b64encode((FONTS/p).read_bytes()).decode()
FACE = f"""
@font-face{{font-family:'Barlow';src:url(data:font/ttf;base64,{b64('BarlowCondensed-Light.ttf')}) format('truetype');font-weight:300}}
@font-face{{font-family:'Barlow';src:url(data:font/ttf;base64,{b64('BarlowCondensed-Regular.ttf')}) format('truetype');font-weight:400}}
@font-face{{font-family:'Mono';src:url(data:font/ttf;base64,{b64('SpaceMono-Regular.ttf')}) format('truetype')}}
@font-face{{font-family:'Corm';src:url(data:font/ttf;base64,{b64('Cormorant.ttf')}) format('truetype')}}
"""

BONE="#E9E3D4"; BONE2="#E1DAC8"; INK="#17231C"
G0="#1c471c"; G1="#276F27"; G2="#499A13"; G3="#8ECA3C"; LIME="#BBDC12"
W,H=1000,1414; M=96; R=W-M; CW=R-M

class Page:
    def __init__(p): p.el=[]
    def add(p,s): p.el.append(s)
    def line(p,x1,y1,x2,y2,stroke=INK,w=1,op=1,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ""
        p.add(f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{stroke}" stroke-width="{w}" stroke-opacity="{op}"{d}/>')
    def rect(p,x,y,w,h,fill="none",stroke=None,sw=1,op=1,sop=1,rx=0):
        s=f' stroke="{stroke}" stroke-width="{sw}" stroke-opacity="{sop}"' if stroke else ""
        r=f' rx="{rx}"' if rx else ""
        p.add(f'<rect x="{x:.2f}" y="{y:.2f}" width="{w:.2f}" height="{h:.2f}" fill="{fill}" fill-opacity="{op}"{s}{r}/>')
    def txt(p,x,y,s,size,fam="Mono",fill=INK,weight=400,anchor="start",ls=0,op=1,style=""):
        st=(f'letter-spacing:{ls}px;' if ls else "")+style
        p.add(f'<text x="{x:.2f}" y="{y:.2f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{fill}" fill-opacity="{op}" text-anchor="{anchor}" style="{st}">{s}</text>')
    def cross(p,x,y,s=9,w=1,op=.7):
        p.line(x-s,y,x+s,y,INK,w,op); p.line(x,y-s,x,y+s,INK,w,op)
    def frame(p,no,sub):
        p.add(f'<rect width="{W}" height="{H}" fill="{BONE}"/>')
        p.add(f'<rect x="{W*0.62:.0f}" y="0" width="{W*0.38:.0f}" height="{H}" fill="{BONE2}" opacity="0.5"/>')
        p.rect(M-16,M-16,CW+32,H-2*(M-16),stroke=INK,sop=.16,sw=1)
        p.txt(M,M-30,f"PLATE&#160;Nº&#160;{no}",12.5,"Mono",ls=2)
        p.txt(M,M-14,"STRATA CANON",12.5,"Mono",ls=2,op=.55)
        p.txt(R,M-30,"17.6478°&#8201;S",12.5,"Mono",anchor="end",ls=1)
        p.txt(R,M-14,"31.6353°&#8201;E",12.5,"Mono",anchor="end",ls=1,op=.55)
        p.line(M,M+2,R,M+2,INK,1,.55)
        for i in range(49):
            x=M+CW*i/48; p.line(x,M+2,x,M+(7 if i%6==0 else 4),INK,1,.32)
        # colophon + corners
        p.txt(W/2,1298,"BUILDTRACK&#8194;·&#8194;MUREHWA VILLA&#8194;·&#8194;MASHONALAND EAST&#8194;·&#8194;MMXXVI",11,"Mono",anchor="middle",op=.7,ls=2)
        for (x,y) in [(M,M),(R,M),(M,H-M),(R,H-M)]: p.cross(x,y)
        p.txt(R,1298,sub,10,"Mono",anchor="end",op=.4,ls=1)
    def title(p,kicker,word,ws,gloss,wls=26):
        p.txt(W/2,158,kicker,12.5,"Mono",anchor="middle",ls=4,op=.6)
        p.txt(W/2,300,word,ws,"Barlow",INK,weight=300,anchor="middle",ls=wls)
        p.txt(W/2,345,gloss,26,"Corm",INK,anchor="middle",op=.85,style="font-variation-settings:'wght' 400;font-style:italic;")
    def figrow(p,figs):
        fy=1150; p.line(M,fy,R,fy,INK,1,.5)
        for i,(n,l) in enumerate(figs):
            cxf=M+CW*(i+0.5)/len(figs)
            p.txt(cxf,fy+40,n,25,"Mono",anchor="middle",ls=1)
            p.txt(cxf,fy+60,l,10,"Mono",anchor="middle",op=.6,ls=2)
            if i>0: p.line(M+CW*i/len(figs),fy+8,M+CW*i/len(figs),fy+70,INK,1,.3)
        p.line(M,fy+82,R,fy+82,INK,1,.5)
    def svg(p):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
                f'<style>{FACE}text{{-webkit-font-smoothing:antialiased}}</style>'+"".join(p.el)+"</svg>")

# ============================================================ PLATE 02 — MATTER
def plate2():
    p=Page(); p.frame("02","THE COUNT · FIRED EARTH")
    p.title("AN ACCOUNTING OF FIRED EARTH","80,000",150,"units &#8194;·&#8194; molded, stacked, borne",wls=10)
    # field of 800 marks (each = 100 bricks). 51,000 machine-pressed, 29,000 rural.
    cols,rows=40,20; cw_,ch_=17.4,9.2; mw,mh=15.6,5.4
    fw=cols*cw_; fh=rows*ch_
    fx=(W-fw)/2; fy=560
    p.txt(fx, fy-22, "▪ = 100 fired units", 10.5,"Mono",op=.6,ls=1)
    p.txt(fx+fw, fy-22, "reading order &#8594;",10.5,"Mono",anchor="end",op=.45)
    mach=510
    for idx in range(cols*rows):
        r,c=divmod(idx,cols)
        x=fx+c*cw_; y=fy+r*ch_
        if idx==cols*rows-1: col=LIME            # the final unit — single lime accent
        elif idx<mach: col=G1
        else: col=G3
        p.rect(x,y,mw,mh,fill=col,rx=0.6)
    # bracket + swatches under field
    by=fy+fh+30
    p.line(fx,by,fx+mach/rows*cw_*0 + (mach%cols)*cw_ if False else fx, by, INK,1,.3) # noop guard
    # legend swatches
    lx=fx; ly=fy+fh+34
    p.rect(lx,ly,26,10,fill=G1); p.txt(lx+34,ly+9,"51,000&#8194;MACHINE-PRESSED&#8194;·&#8194;double-skin, load-bearing",11,"Mono",op=.7,ls=.5)
    p.rect(lx,ly+26,26,10,fill=G3); p.txt(lx+34,ly+35,"29,000&#8194;RURAL-MOULDED&#8194;·&#8194;single-skin partitions",11,"Mono",op=.7,ls=.5)
    p.rect(lx,ly+52,26,10,fill=LIME); p.txt(lx+34,ly+61,"the final unit&#8194;·&#8194;the roof goes on",11,"Mono",op=.7,ls=.5)
    # big ratio ring on right void? keep minimal — a vertical proportion bar
    bx=R-30; p.line(bx,fy,bx,fy+fh,INK,1,.4)
    split=fy+fh*mach/(cols*rows)
    p.rect(bx-5,fy,10,fh*mach/(cols*rows),fill=G1,op=.9)
    p.rect(bx-5,split,10,fh*(1-mach/(cols*rows)),fill=G3,op=.9)
    p.txt(bx-12,fy+fh*mach/(cols*rows)/2,"64%",9,"Mono",anchor="end",op=.6)
    p.txt(bx-12,split+fh*(1-mach/(cols*rows))/2,"36%",9,"Mono",anchor="end",op=.6)
    p.txt(W/2,fy+fh+96,"HYBRID SUPPLY&#8194;·&#8194;BETA / WILLDALE + LOCAL KILN&#8194;·&#8194;HAULED TO MUREHWA",10.5,"Mono",anchor="middle",op=.6,ls=1)
    p.figrow([("51,000","MACHINE-PRESSED"),("29,000","RURAL-MOULDED"),("USD 9,610","SUPPLY & HAULAGE"),("02","SOURCES")])
    return p.svg()

# ============================================================ PLATE 03 — TIME
def plate3():
    p=Page(); p.frame("03","THE SEASONS · DURATION")
    p.title("A CALENDAR OF PATIENT LABOUR","MWAKA",150,"n. &#8194;the turning season&#8194;·&#8194;chiShona",wls=20)
    names=["SUBSTRUCTURE","GROUND SLAB","GROUND FLOOR + DECK","FIRST FLOOR + PARAPET","HIDDEN ROOF","GLAZING & FITTINGS"]
    weeks=[3,2,6,3,2,4]; cols=[G0,G1,G2,G3,"#30827f",LIME] if False else [G0,G1,G2,G3,G2,G1]
    roman=["I","II","III","IV","V","VI"]
    total=sum(weeks)  # 20
    ax0,ax1=330,864; py0=560; ppw=(ax1-ax0)/total
    # week scale
    for wk in range(total+1):
        x=ax0+wk*ppw
        p.line(x,py0-14,x,py0-8,INK,1,.35 if wk%1 else .35)
        if wk%2==0: p.txt(x,py0-20,f"{wk:02d}",9.5,"Mono",anchor="middle",op=.6)
    p.txt(ax0,py0-40,"WEEK",10,"Mono",op=.55,ls=2)
    p.line(ax0,py0-6,ax1,py0-6,INK,1,.5)
    # month shading (approx 4.33 wk)
    rowH=58; start=0
    for i in range(6):
        x=ax0+start*ppw; w=weeks[i]*ppw; y=py0+8+i*rowH
        # cascade guide from previous end
        if i>0:
            px=ax0+start*ppw
            p.line(px,py0+8+(i-1)*rowH+rowH-14,px,y+14,INK,1,.3,dash="2 3")
        p.rect(ax0,y,ax1-ax0,34,fill=INK,op=.03)                # track
        p.rect(x,y,w,34,fill=cols[i],rx=3)
        p.txt(x+6,y+22,f"{weeks[i]} wk",10.5,"Mono",fill="#fff",op=.9)
        p.txt(ax0-14,y+15,roman[i],12,"Mono",anchor="end",op=.9,ls=1)
        p.txt(ax0-14,y+30,f"stage",8.5,"Mono",anchor="end",op=.4)
        p.txt(x+w+10,y+22,names[i],11,"Barlow",weight=400,ls=1)
        start+=weeks[i]
    # 28-day cure flag on stage III end — lime accent
    cure_x=ax0+(weeks[0]+weeks[1]+weeks[2])*ppw
    cy=py0+8+2*rowH
    p.line(cure_x,cy-6,cure_x,cy+34+8,LIME,2,1)
    p.add(f'<path d="M{cure_x:.0f} {cy-6:.0f} l16 5 l-16 5 Z" fill="{LIME}"/>')
    p.txt(cure_x+20,cy+2,"28-DAY SLAB CURE",9,"Mono",op=.75,ls=.5)
    p.txt(ax0,py0+8+6*rowH+6,"SEQUENTIAL DEPOSITION&#8194;·&#8194;EACH STRATUM AWAITS THE ONE BELOW",10.5,"Mono",op=.6,ls=1)
    p.figrow([("20","WEEKS DURATION"),("06","STAGES"),("28","DAYS SLAB CURE"),("~5","MONTHS")])
    return p.svg()

# ============================================================ PLATE 04 — VALUE
def plate4():
    p=Page(); p.frame("04","THE RECKONING · LEDGER")
    p.title("THE WEIGHT OF THE SHELL, IN CURRENCY","MARI",150,"n. &#8194;the reckoning&#8194;·&#8194;chiShona",wls=22)
    items=[("I","FOUNDATION",4200,G0),("II","GROUND SLAB",4500,G1),
           ("III","MID-SLAB DECK",11600,G2),("IV","PARAPET SHELL",600,G3),
           ("V","HIDDEN ROOF",5650,G2),("BR","BRICK LOGISTICS",9610,G1)]
    total=sum(i[2] for i in items)  # 36160
    colw=150; cx0=(W-colw)/2-60; top=560; colh=560
    kpx=colw and colh/total
    # left USD scale
    sx=cx0-24
    p.line(sx,top,sx,top+colh,INK,1,.5)
    for v in range(0,40001,10000):
        y=top+colh-(v*kpx)
        if y<top-1: continue
        p.line(sx-7,y,sx,y,INK,1,.5)
        p.txt(sx-12,y+3.5,f"{v//1000}k" if v else "0",10,"Mono",anchor="end",op=.6)
    p.txt(sx-12,top-14,"USD",10,"Mono",anchor="end",op=.55,ls=1)
    # stacked column bottom-up (rhymes with the build section)
    y=top+colh
    biggest=max(items,key=lambda i:i[2])
    for (rom,name,val,col) in items:
        h=val*kpx; y-=h
        p.rect(cx0,y,colw,h,fill=col)
        # thin separators
        p.line(cx0,y,cx0+colw,y,BONE,1,.6)
        # leader + label to the right
        my=y+h/2; lx=cx0+colw
        p.line(lx,my,lx+34,my,INK,1,.5)
        p.add(f'<circle cx="{lx+34}" cy="{my:.1f}" r="2.4" fill="{INK}"/>')
        p.txt(lx+46,my-4,f"{rom}&#8194;&#8194;{name}",12.5,"Barlow",weight=400,ls=1)
        p.txt(lx+46,my+12,f"USD {val:,}&#8194;·&#8194;{val/total*100:.0f}%",10.5,"Mono",op=.7)
        if (rom,name,val,col)==biggest:  # heaviest stratum — lime accent
            p.add(f'<path d="M{cx0:.0f} {my-7:.0f} l-14 7 l14 7 Z" fill="{LIME}"/>')
            p.txt(cx0-18,my+3,"HEAVIEST",8.5,"Mono",anchor="end",op=.7)
    p.rect(cx0,top,colw,colh,stroke=INK,sop=.5,sw=1.2)
    p.txt(cx0+colw/2,top+colh+26,"STRUCTURAL SHELL&#8194;·&#8194;MATERIALS + PROP RENTAL&#8194;·&#8194;EX-FINISHES",10.5,"Mono",anchor="middle",op=.6,ls=1)
    p.figrow([("USD 36,160","TOTAL SHELL"),("USD 11,600","LARGEST · DECK"),("06","LINE ITEMS"),("USD 4.5k","PER STOREY-M²")])
    return p.svg()

# ---------- write individual svgs+pngs, and combined book ----------
page1_svg=(HERE/"poster.svg").read_text()
svgs=[("01",page1_svg),("02",plate2()),("03",plate3()),("04",plate4())]
for no,s in svgs:
    (HERE/f"plate{no}.svg").write_text(s)

pages="".join(f'<div class="pg">{s}</div>' for _,s in svgs)
book=(f'<!doctype html><html><head><meta charset="utf-8"><style>'
      f'*{{margin:0;padding:0}}@page{{size:264.58mm 374.11mm;margin:0}}'
      f'.pg{{width:{W}px;height:{H}px;page-break-after:always;overflow:hidden}}'
      f'.pg:last-child{{page-break-after:auto}}'
      f'</style></head><body>{pages}</body></html>')
(HERE/"book.html").write_text(book)
# single-page html for png rendering of 02-04
for no,s in svgs[1:]:
    (HERE/f"p{no}.html").write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>*{{margin:0;padding:0}}html,body{{width:{W}px;height:{H}px}}</style></head><body>{s}</body></html>')
print("wrote plates 02-04, book.html")
