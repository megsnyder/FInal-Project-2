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
Sprite(earout, (227,119))
Sprite(earout, (293,119))
Sprite(stalk, (236,124))
Sprite(stalk, (293,124))
Sprite(earin, (228,122))
Sprite(earin, (298,122))
Sprite(leg, (226,305))
Sprite(leg, (256,305))
#happy
Sprite(mouth, (260,178))
Sprite(mouth2, (260,177))
#sad
Sprite(eyebrow1, (239,148))
Sprite(eyebrow2, (281,148))
Sprite(mouth, (260,178))
Sprite(mouth2, (260,179))
#tired
Sprite(eyelid, (235, 138))
Sprite(eyelid, (277, 138))
Sprite(mouth3, (260, 180))
#bored
Sprite(eyelid2, (232, 148))
Sprite(eyelid2, (272, 148))
Sprite(mouth4, (261, 180))

myapp = App()
myapp.run()
