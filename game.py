from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

class Creature(Sprite):
    def __init__(self, position):
        super().__init__(Player.asset, position)
        
        self.vx = 0
        self.vy = 0
class Game(App):
    
    def __init__(self,width,height):
        bg_asset = RectangleAsset(self.width, self.height, noline, winter)
        ground_asset = RectangleAsset(self.width, 400, noline, white)
        bg = Sprite(bg_asset, (0,0))
        ground = Sprite(ground_asset, (0,400))

myapp = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()
