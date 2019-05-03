from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

red = Color(0xd90000, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
brown = Color(0xa07251, 1.0)
green = Color(0x3ddb33, 1.0)

noline = LineStyle(0, white)

apple=CircleAsset(10,noline,red)
stem=RectangleAsset(2,7,noline,brown)
leaf=EllipseAsset(5,2,noline,green)
shine=CircleAsset(5,noline,white)
shadow=CircleAsset(7,noline,red)

Sprite(apple, (220,177))
Sprite(stem, (230,173))
Sprite(leaf, (230,170))
Sprite(shine, (222,179))
Sprite(shadow, (224,181))


myapp = App()
myapp.run()