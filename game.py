from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
day=Color(0xb9f5ff, 1.0)
night=Color(0x5056a2, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
green=Color(0x4fff85, 1.0)
leaves=Color(0x31e34f, 1.0)
bodyC = Color(0x88bbFF, 1.0)
pink = Color(0xffa5eb, 1.0)
noline = LineStyle(0, white)


class Creature(Sprite):
    asset=ImageAsset("images/Screenshot 2019-04-30 at 10.png")
    
    def __init__(self, position):
        super().__init__(Creature.asset, position)
        self.vx = 0
        self.vy = 0
        
class Food(Sprite):
    def __init__(self, position):
        super().__init__(Food.asset, position)
        self.vx = 0
        self.vy = 0 

class Trampoline(Sprite):
    def __init__(self, position):
        super().__init__(Trampoline.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Game(App):
    
    def __init__(self,width,height):
        super().__init__(width,height)
        bg_asset = RectangleAsset(self.width, self.height, noline, day)
        ground_asset = RectangleAsset(self.width, 400, noline, green)
        bushes = CircleAsset(50,noline,leaves)
        Sprite(bg_asset, (0,0))
        Sprite(ground_asset, (0,240))
        Sprite(bushes, (0,200))
        Sprite(bushes, (50,180))
        Sprite(bushes, (25,220))
        Sprite(bushes, (925,280))
        Sprite(bushes, (900,300))
        Sprite(bushes, (950,320))
        self.creature=Creature((300,300))
        
myapp = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()
