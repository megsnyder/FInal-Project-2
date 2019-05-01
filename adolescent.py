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

head = EllipseAsset(40,37, noline, bodyC)
eye=CircleAsset(7,noline,black)
highlight=CircleAsset(4,noline,white)
shadow=CircleAsset(4,noline,black)
mouth=EllipseAsset(5,3,noline,black)
mouth2=EllipseAsset(5,3,noline,bodyC)
mouth3=EllipseAsset(5,1,noline,black)
mouth4=EllipseAsset(7,1,noline,black)
body=EllipseAsset(40,50, noline, bodyC)
earout=EllipseAsset(7,6, noline, bodyC)
earin=EllipseAsset(4,3, noline, pink)
stalk=EllipseAsset(3,5,noline,bodyC)
leg=EllipseAsset(20,7,noline,bodyC)
eyebrow1=PolygonAsset([(0,0),(12,0),(0,6),(0,0)], noline, bodyC)
eyebrow2=PolygonAsset([(0,0),(12,0),(12,6),(0,0)], noline, bodyC)
eyelid=CircleAsset(10,noline,bodyC)
eyelid2=RectangleAsset(20,7,noline,bodyC)
arm=EllipseAsset(5,10,noline,bodyC)

Sprite(body, (223,177))
Sprite(arm, (220,194))
Sprite(arm, (295,194))
Sprite(head, (223, 124))
Sprite(eye, (235, 150))
Sprite(eye, (275, 150))
Sprite(highlight, (236, 151))
Sprite(highlight, (276, 151))
Sprite(shadow, (237, 152))
Sprite(shadow, (277, 152))
Sprite(earout, (227,119))
Sprite(earout, (283,119))
Sprite(stalk, (236,124))
Sprite(stalk, (283,124))
Sprite(earin, (228,122))
Sprite(earin, (288,122))
Sprite(leg, (226,265))
Sprite(leg, (260,265))
#happy
Sprite(mouth, (258,178))
Sprite(mouth2, (258,177))
#sad
Sprite(eyebrow1, (233,149))
Sprite(eyebrow2, (279,149))
Sprite(mouth, (258,178))
Sprite(mouth2, (258,179))
'''
#tired
Sprite(eyelid, (232, 142))
Sprite(eyelid, (272, 142))
Sprite(mouth3, (258, 178))
#bored
Sprite(eyelid2, (232, 150))
Sprite(eyelid2, (272, 150))
Sprite(mouth4, (256, 178))
'''
myapp = App()
myapp.run()
