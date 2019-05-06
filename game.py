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
red = Color(0xd90000, 1.0)
yellow = Color(0xe5ff18, 1.0)
blue = Color(0x1ca0ff, 1.0)
brown = Color(0xa07251, 1.0)
green1 = Color(0x3ddb33, 1.0)
noline = LineStyle(0, white)
grey = Color(0x515979, 1.0)
green2 = Color(0x40793a, 1.0)

class Creature1(Sprite):
    asset=ImageAsset("images/Screenshot 2019-04-30 at 10.png")
    
    def __init__(self, position):
        super().__init__(Creature1.asset, position)
        self.vx = 0
        self.vy = 0
        
class Creature2(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9.png")
    
    def __init__(self, position):
        super().__init__(Creature2.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
        
class Creature3(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (5).png")
    
    def __init__(self, position):
        super().__init__(Creature3.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
        
class Food(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-03 at 10.png")
    def __init__(self, position):
        super().__init__(Food.asset, position)
        self.vx = 0
        self.vy = 0 

class Trampoline(Sprite):
    def __init__(self, position):
        super().__init__(Trampoline.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Day(Sprite):
    asset = RectangleAsset(1000, 800, noline, day)
    def __init__(self, position):
        super().__init__(Day.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Night(Sprite):
    asset = RectangleAsset(1000, 800, noline, night)
    def __init__(self, position):
        super().__init__(Night.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0 
        
class Feed(Sprite):
    asset = CircleAsset(20, noline, red)
    def __init__(self, position):
        super().__init__(Feed.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Sleep(Sprite):
    asset = CircleAsset(20, noline, yellow)
    def __init__(self, position):
        super().__init__(Sleep.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Play(Sprite):
    asset = CircleAsset(20, noline, blue)
    def __init__(self, position):
        super().__init__(Play.asset, position)
        self.vx = 0
        self.vy = 0 
        
class Game(App):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.day=Day((0,0))
        self.night=Night((0,0))
        ground_asset = RectangleAsset(self.width, 400, noline, green)
        bushes = CircleAsset(50,noline,leaves)
        Sprite(ground_asset, (0,240))
        Sprite(bushes, (0,200))
        Sprite(bushes, (50,180))
        Sprite(bushes, (25,220))
        Sprite(bushes, (925,280))
        Sprite(bushes, (900,300))
        Sprite(bushes, (950,320))
    
        self.creature1=Creature1((300,300))
        self.creature2=Creature2((300,300))
        self.creature3=Creature3((300,300))
        self.food=Food((100,200))
        self.food=Food((60,250))
        self.food=Food((20,220))
        self.food=Food((950,300))
        self.food=Food((920,350))
        self.feed=Feed((20,500))
        self.sleep=Sleep((60,500))
        self.play=Play((100,500))
        #Game.listenKeyEvent("keydown", "f", self.dofeed)
        Game.listenKeyEvent("keydown", "s", self.dosleep)
        #Game.listenKeyEvent("keydown", "p", self.doplay)
        self.a=0

    #def dofeed(self, event):
        
    def dosleep(self, event):
        for night in self.getSpritesbyClass(Night):
            night.visible=True
        self.a+=1  
        for creature1 in self.getSpritesbyClass(Creature1):
            for creature2 in self.getSpritesbyClass(Creature2):
                for creature3 in self.getSpritesbyClass(Creature3):
                    if self.a<3:
                        creature1.visible=True
                    elif self.a<6:
                        creature1.visible=False
                        creature2.visible=True
                    else:
                        creature1.visible=False
                        creature2.visible=False
                        creature3.visible=True
    #def doplay(self, event):
        
myapp = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()
