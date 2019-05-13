from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
from math import floor, sin, cos
import random
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

brown = Color(0x88bbFF, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
pink = Color(0xffa5eb, 1.0)

noline = LineStyle(0, white)
ground_asset = RectangleAsset(self.width, 400, noline, green)
bed = RectangleAsset(37,35, noline, brown)
leg = RectangleAsset(37,35, noline, brown)
blanket = RectangleAsset(37,35, noline, purple)
lump = EllipseAsset(37,35, noline, purple)
Sprite(ground_asset, (223, 124))
Sprite(head, (223, 124))

myapp = App()
myapp.run()