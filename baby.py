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

#happy
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
Sprite(mouth, (256,178))
Sprite(mouth2, (256,177))
Sprite(earout, (224,126))
Sprite(earout, (280,126))
Sprite(earin, (225,129))
Sprite(earin, (285,129))
Sprite(leg, (226,240))
Sprite(leg, (273,240))
#sad
Sprite(body, (420,377))
Sprite(arm, (417,390))
Sprite(arm, (492,390))
Sprite(head, (423, 324))
Sprite(eye, (430, 350))
Sprite(eye, (470, 350))
Sprite(highlight, (433, 351))
Sprite(highlight, (473, 351))
Sprite(shadow, (434, 352))
Sprite(shadow, (474, 352))
Sprite(eyebrow1, (432,349))
Sprite(eyebrow2, (478,349))
Sprite(mouth, (456,378))
Sprite(mouth2, (456,379))
Sprite(earout, (424,326))
Sprite(earout, (480,326))
Sprite(earin, (425,329))
Sprite(earin, (485,329))
Sprite(leg, (426,440))
Sprite(leg, (473,440))
#tired
Sprite(body, (320,277))
Sprite(arm, (317,290))
Sprite(arm, (392,290))
Sprite(head, (323, 224))
Sprite(eye, (330, 250))
Sprite(eye, (370, 250))
Sprite(eyelid, (330, 248))
Sprite(eyelid, (370, 248))
Sprite(mouth3, (356,278))
Sprite(earout, (324,226))
Sprite(earout, (380,226))
Sprite(earin, (325,229))
Sprite(earin, (385,229))
Sprite(leg, (326,340))
Sprite(leg, (373,340))
#bored
Sprite(body, (220,377))
Sprite(arm, (217,390))
Sprite(arm, (292,390))
Sprite(head, (223, 324))
Sprite(eye, (230, 350))
Sprite(eye, (270, 350))
Sprite(eyelid2, (230, 350))
Sprite(eyelid2, (270, 350))
Sprite(mouth4, (254,378))
Sprite(earout, (224,326))
Sprite(earout, (280,326))
Sprite(earin, (225,329))
Sprite(earin, (285,329))
Sprite(leg, (226,440))
Sprite(leg, (273,440))

myapp = App()
myapp.run()
