from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

brown = Color(0xa07251, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
purple = Color(0xdd55ff, 1.0)
green=Color(0x4fff85, 1.0)
bodyC = Color(0x88bbFF, 1.0)

noline = LineStyle(0, white)
ground_asset = RectangleAsset(1000, 400, noline, green)
bed = RectangleAsset(170,35, noline, brown)
leg = RectangleAsset(15,80, noline, brown)
blanket = RectangleAsset(170,35, noline, purple)
lump = EllipseAsset(60,20, noline, purple)
head = EllipseAsset(20,10,noline, bodyC)
ear=EllipseAsset(7,6, noline, bodyC)
pillow = EllipseAsset(20,10,noline, white)
Sprite(ground_asset, (0, 50))
Sprite(bed, (223, 124))
Sprite(head, (340,90))
Sprite(ear, (370, 85))
Sprite(blanket, (223, 100))
Sprite(lump, (230, 85))
Sprite(leg, (223, 90))
Sprite(leg, (378, 90))

myapp = App()
myapp.run()