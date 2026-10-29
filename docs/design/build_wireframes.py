"""Generate review-only layout drawings; this is not website source."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'docs' / 'wireframes'
OUT.mkdir(parents=True, exist_ok=True)
FONT = 'C:/Windows/Fonts/arial.ttf'
BG, PANEL, TEXT, MUTED, GREEN = '#101814', '#19251E', '#E8F0EA', '#A9B8AE', '#34D399'

def make(mobile=False):
    w = 420 if mobile else 1200
    h = 2650 if mobile else 2140
    im = Image.new('RGB', (w,h), BG)
    d = ImageDraw.Draw(im)
    def text(x,y,s,size=18,color=TEXT):
        d.text((x,y),s,font=ImageFont.truetype(FONT,size),fill=color)
    def box(x,y,bw,bh,label):
        d.rectangle((x,y,x+bw,y+bh), fill=PANEL,outline=MUTED)
        text(x+16,y+20,label,16)
    def heading(y,s):
        d.rectangle((24,y+5,32,y+13),fill=GREEN)
        text(44,y,s,26,GREEN)
    text(24,20,'ANGEL / PORTFOLIO',18,GREEN)
    text(24,54,'Home  About  Skills  Projects  Contact',14)
    text(24,96,'LAYOUT DRAFT / review pending',14,MUTED)
    text(24,145,'Angel Mendez Reyes',28 if mobile else 44)
    text(24,205,'Software & Data Engineering',18,MUTED)
    text(24,240,'Introduction and career interests',16,MUTED)
    box(24,285,145,50,'Contact Me')
    box(185,285,155,50,'View Projects')
    ay = 365 if mobile else 140
    ax = 24 if mobile else 680
    aw = 372 if mobile else 470
    box(ax,ay,aw,250,'' if (ROOT/'docs/design/cozy-pc-concept.png').exists() else 'Cozy PC illustration')
    art=ROOT/'docs/design/cozy-pc-concept.png'
    if art.exists():
        a=Image.open(art).convert('RGB'); a.thumbnail((aw-8,242))
        im.paste(a,(ax+(aw-a.width)//2,ay+4))
    y=670 if mobile else 470
    heading(y,'About')
    text(24,y+55,'Approved professional bio',18)
    text(24,y+90,'Education + research summary',18)
    box(24,y+130,180,46,'Resume PDF')
    y+=230
    heading(y,'Skills')
    text(24,y+55,'Languages / Backend / Tools',18)
    text(24,y+88,'Readable text; no proficiency scores',16,MUTED)
    y+=170
    heading(y,'Projects & Research')
    projects=[('Soft Steps','Screenshot supplied later'),('SMS Spam Classifier','Actual output supplied later'),('2D Mystery Game','Screenshot supplied later')]
    for i,(title,label) in enumerate(projects):
        y+=65
        if mobile:
            text(24,y,title,24)
            text(24,y+42,'Description + my contributions',16,MUTED)
            text(24,y+72,'Technology / approved links',16,MUTED)
            box(24,y+110,372,175,label)
            y+=280
        else:
            vx,tx=(24,590) if i%2==0 else (650,24)
            box(vx,y,500,210,label)
            text(tx,y+10,title,27)
            text(tx,y+60,'Description + individual contributions',18,MUTED)
            text(tx,y+100,'Technology / approved project links',18,MUTED)
            y+=220
    y+=85
    heading(y,'Contact')
    text(24,y+55,'Job and research opportunities',18)
    text(24,y+90,'Email / GitHub / LinkedIn',18,GREEN)
    text(24,y+135,'Contact interaction decided in Phase 3',14,MUTED)
    im=im.crop((0,0,w,min(h,y+200)))
    im.save(OUT/('mobile.png' if mobile else 'desktop.png'))

make(); make(True)
