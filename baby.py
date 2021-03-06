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

head = EllipseAsset(37,35, noline, bodyC)
eye=CircleAsset(10,noline,black)
highlight=CircleAsset(4,noline,white)
shadow=CircleAsset(7,noline,black)
mouth=EllipseAsset(4,3,noline,black)
mouth2=EllipseAsset(4,3,noline,bodyC)
mouth3=EllipseAsset(4,1,noline,black)
mouth4=EllipseAsset(6,1,noline,black)
body=EllipseAsset(40,35, noline, bodyC)
earout=EllipseAsset(7,6, noline, bodyC)
earin=EllipseAsset(4,3, noline, pink)
leg=EllipseAsset(10,4,noline,bodyC)
eyebrow1=PolygonAsset([(0,0),(12,0),(0,6),(0,0)], noline, bodyC)
eyebrow2=PolygonAsset([(0,0),(12,0),(12,6),(0,0)], noline, bodyC)
eyelid=CircleAsset(10,noline,bodyC)
eyelid2=RectangleAsset(20,7,noline,bodyC)
arm=EllipseAsset(5,5,noline,bodyC)

Sprite(body, (220,177))
Sprite(arm, (217,190))
Sprite(arm, (292,190))
Sprite(head, (223, 124))
Sprite(eye, (230, 150))
Sprite(eye, (270, 150))
Sprite(highlight, (233, 151))
Sprite(highlight, (273, 151))
Sprite(shadow, (234, 152))
Sprite(shadow, (274, 152))
Sprite(earout, (224,126))
Sprite(earout, (280,126))
Sprite(earin, (225,129))
Sprite(earin, (285,129))
Sprite(leg, (226,240))
Sprite(leg, (273,240))
#happy
Sprite(mouth, (256,178))
Sprite(mouth2, (256,177))
#sad
Sprite(eyebrow1, (232,149))
Sprite(eyebrow2, (278,149))
Sprite(mouth, (256,178))
Sprite(mouth2, (256,179))
#tired
Sprite(eyelid, (230, 148))
Sprite(eyelid, (270, 148))
Sprite(mouth3, (256, 178))
#bored
Sprite(eyelid2, (230, 150))
Sprite(eyelid2, (270, 150))
Sprite(mouth4, (254, 178))

myapp = App()
myapp.run()
