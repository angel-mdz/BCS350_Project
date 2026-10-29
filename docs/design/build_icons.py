"""Original 16px grid motifs, exported as SVG and a review sheet."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
P=Path(__file__).resolve().parent
patterns={
'about':['0000011110000000','0000111111000000','0000111111000000','0000011110000000','0000000000000000','0001111111100000','0011100001110000','0011000000110000','0011000000110000'],
'skills':['0001000000001000','0011000010001100','0110000110000110','1100001100000011','0110011000000110','0011110000001100','0001100000001000'],
'projects':['0111110000000000','1100011111111100','1100000000000110','1111111111111110','1100000000000110','1100000000000110','1100000000000110','1111111111111110'],
'contact':['1111111111111111','1100000000000011','1011000000001101','1000110000110001','1000001111000001','1000000000000001','1000000000000001','1111111111111111']}
sheet=Image.new('RGB',(800,180),'#101814'); d=ImageDraw.Draw(sheet)
for i,(name,rows) in enumerate(patterns.items()):
    rects=[]
    for y,row in enumerate(rows):
        for x,c in enumerate(row):
            if c=='1':
                rects.append(f'<rect x="{x}" y="{y+3}" width="1" height="1"/>')
                xx=60+i*200+x*4; yy=25+(y+3)*4
                d.rectangle((xx,yy,xx+3,yy+3),fill='#34D399')
    (P/f'icon-{name}.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 16 16" fill="currentColor" shape-rendering="crispEdges">'+''.join(rects)+'</svg>',encoding='utf-8')
    d.text((45+i*200,120),name.title(),fill='#E8F0EA',font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',22))
sheet.save(P/'pixel-icons.png')
