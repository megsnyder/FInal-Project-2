from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

bodyC = Color(0x88bbFF, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
pink = Color(0xffa5eb, 1.0)

noline = LineStyle(0, white)

head = EllipseAsset(45,40, noline, bodyC)
eye=CircleAsset(5,noline,black)
highlight=CircleAsset(3,noline,white)
shadow=CircleAsset(3,noline,black)
mouth=EllipseAsset(6,3,noline,black)
mouth2=EllipseAsset(6,3,noline,bodyC)
mouth3=EllipseAsset(6,1,noline,black)
mouth4=EllipseAsset(6,1,noline,black)
body=EllipseAsset(45,70, noline, bodyC)
earout=EllipseAsset(7,6, noline, bodyC)
earin=EllipseAsset(4,3, noline, pink)
stalk=EllipseAsset(3,8,noline,bodyC)
leg=EllipseAsset(30,7,noline,bodyC)
eyebrow1=PolygonAsset([(0,0),(12,0),(0,6),(0,0)], noline, bodyC)
eyebrow2=PolygonAsset([(0,0),(12,0),(12,6),(0,0)], noline, bodyC)
eyelid=CircleAsset(10,noline,bodyC)
eyelid2=RectangleAsset(20,7,noline,bodyC)
arm=EllipseAsset(5,20,noline,bodyC)

Sprite(body, (225,177))
Sprite(arm, (222,194))
Sprite(arm, (307,194))
Sprite(head, (223, 124))
Sprite(eye, (240, 150))
Sprite(eye, (282, 150))
Sprite(highlight, (241, 151))
Sprite(highlight, (283, 151))
Sprite(shadow, (242, 152))
Sprite(shadow, (284, 152))
Sprite(mouth, (260,178))
Sprite(mouth2, (260,177))
Sprite(earout, (227,119))
Sprite(earout, (293,119))
Sprite(stalk, (236,124))
Sprite(stalk, (293,124))
Sprite(earin, (228,122))
Sprite(earin, (298,122))
Sprite(leg, (226,305))
Sprite(leg, (256,305))
#sad
Sprite(body, (423,377))
Sprite(arm, (420,394))
Sprite(arm, (495,394))
Sprite(head, (423, 324))
Sprite(eye, (435, 350))
Sprite(eye, (475, 350))
Sprite(highlight, (436, 351))
Sprite(highlight, (476, 351))
Sprite(shadow, (437, 352))
Sprite(shadow, (477, 352))
Sprite(eyebrow1, (434,349))
Sprite(eyebrow2, (478,349))
Sprite(mouth, (456,378))
Sprite(mouth2, (456,379))
Sprite(earout, (427,319))
Sprite(earout, (483,319))
Sprite(stalk, (436,324))
Sprite(stalk, (483,324))
Sprite(earin, (428,322))
Sprite(earin, (488,322))
Sprite(leg, (426,465))
Sprite(leg, (460,465))
#tired
Sprite(body, (323,277))
Sprite(arm, (320,294))
Sprite(arm, (395,294))
Sprite(head, (323, 224))
Sprite(eye, (335, 250))
Sprite(eye, (375, 250))
Sprite(eyelid, (332, 242))
Sprite(eyelid, (372, 242))
Sprite(mouth3, (358,278))
Sprite(earout, (327,219))
Sprite(earout, (383,219))
Sprite(stalk, (336,224))
Sprite(stalk, (383,224))
Sprite(earin, (328,222))
Sprite(earin, (388,222))
Sprite(leg, (326,365))
Sprite(leg, (360,365))
#bored
Sprite(body, (223,377))
Sprite(arm, (220,394))
Sprite(arm, (295,394))
Sprite(head, (223, 324))
Sprite(eye, (235, 350))
Sprite(eye, (275, 350))
Sprite(eyelid2, (232, 350))
Sprite(eyelid2, (272, 350))
Sprite(mouth4, (256,378))
Sprite(earout, (227,319))
Sprite(earout, (283,319))
Sprite(stalk, (236,324))
Sprite(stalk, (283,324))
Sprite(earin, (228,322))
Sprite(earin, (288,322))
Sprite(leg, (226,465))
Sprite(leg, (260,465))

myapp = App()
myapp.run()
