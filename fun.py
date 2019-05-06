from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

grey = Color(0x515979, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
green2 = Color(0x40793a, 1.0)

noline = LineStyle(0, white)

leg=RectangleAsset(3,20,noline,black)
jump=EllipseAsset(40,16,noline,grey)
outline=EllipseAsset(50,20,noline,green2)


Sprite(leg, (120,208))
Sprite(leg, (172,220))
Sprite(leg, (215,208))
Sprite(outline, (120,190))
Sprite(jump, (130,193))



myapp = App()
myapp.run()