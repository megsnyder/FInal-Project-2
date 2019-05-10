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
        self.visible=True
        self.vx = 0
        self.vy = 0
class Creature1sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (1).png")
    
    def __init__(self, position):
        super().__init__(Creature1sad.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature1bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (3).png")
    
    def __init__(self, position):
        super().__init__(Creature1bored.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature1tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (2).png")
    
    def __init__(self, position):
        super().__init__(Creature1tired.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
        
class Creature2(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9.png")
    
    def __init__(self, position):
        super().__init__(Creature2.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature2sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (3).png")
    
    def __init__(self, position):
        super().__init__(Creature2sad.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature2bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10.png")
    
    def __init__(self, position):
        super().__init__(Creature2bored.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature2tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (2).png")
    
    def __init__(self, position):
        super().__init__(Creature2tired.asset, position)
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
class Creature3sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (4).png")
    
    def __init__(self, position):
        super().__init__(Creature1sad.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature3bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (6).png")
    
    def __init__(self, position):
        super().__init__(Creature1bored.asset, position)
        self.visible=False
        self.vx = 0
        self.vy = 0
class Creature3tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (1).png")
    
    def __init__(self, position):
        super().__init__(Creature1tired.asset, position)
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
    asset=ImageAsset("images/Screenshot 2019-05-06 at 9.png")
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
    
        self.creature3=Creature3((290,225))
        self.creature3sad=Creature3sad((297,295))
        self.creature3tired=Creature3tired((272,297))
        self.creature3bored=Creature1bored((291,300))
        self.creature2=Creature2((300,270))
        self.creature2sad=Creature2sad((297,295))
        self.creature2tired=Creature2tired((272,297))
        self.creature2bored=Creature2bored((291,300))
        self.creature1=Creature1((300,300))
        self.creature1sad=Creature1sad((297,295))
        self.creature1tired=Creature1tired((272,297))
        self.creature1bored=Creature1bored((291,300))
        self.food=Food((100,200))
        self.food=Food((60,250))
        self.food=Food((20,220))
        self.food=Food((950,300))
        self.food=Food((920,350))
        self.feed=Feed((20,500))
        self.sleep=Sleep((60,500))
        self.play=Play((100,500))
        Game.listenKeyEvent("keydown", "f", self.dofeed)
        Game.listenKeyEvent("keydown", "s", self.dosleep)
        Game.listenKeyEvent("keydown", "p", self.doplay)
        Game.listenKeyEvent("keydown", "right arrow", self.right)
        Game.listenKeyEvent("keyup", "right arrow", self.right2)
        Game.listenKeyEvent("keydown", "left arrow", self.left)
        Game.listenKeyEvent("keyup", "left arrow", self.left2)
        #Game.listenKeyEvent("keydown", "up arrow", self.up)
        self.a=0
        self.b=False
        self.c=False
        self.d=False
        self.e=False
        self.f=1000
        self.s=1000
        self.p=1000

    def dofeed(self, event):
        print("self.f=" + str(self.f))
        if self.f<750:
            self.f+=250
        elif self.f<1000:
            self.f=1000
        self.food=Food((335,360))
        
    def dosleep(self, event):
        print("self.s=" + str(self.s))
        self.night.visible=True
        self.b=True
        self.a+=1  
        if self.a<3:
            self.creature1.visible=True
        elif self.a<6:
            self.c=False
            self.creature1.visible=False
            self.creature1sad.visible=False
            self.creature1tired.visible=False
            self.creature1bored.visible=False
            self.creature2.visible=True
        else:
            self.c=False
            self.d=False
            self.creature2.visible=False
            self.creature2sad.visible=False
            self.creature2tired.visible=False
            self.creature2bored.visible=False
            self.creature3.visible=True
                        
    def doplay(self, event):
        print("self.p=" + str(self.p))
        if self.p<750:
            self.p+=250
        elif self.p<1000:
            self.p=1000
        self.trampoline=Trampoline((435,360))
        
    def right(self, event):
        self.creature1.vx = 2
        self.creature1sad.vx = 2
        self.creature1bored.vx = 2
        self.creature1tired.vx = 2
        self.creature2.vx = 2
        self.creature2sad.vx = 2
        self.creature2bored.vx = 2
        self.creature2tired.vx = 2
        self.creature3.vx = 2
        self.creature3sad.vx = 2
        self.creature3bored.vx = 2
        self.creature3tired.vx = 2
        
    def left(self, event):
        self.creature1.vx = -2
        self.creature1sad.vx = -2
        self.creature1bored.vx = -2
        self.creature1tired.vx = -2
        self.creature2.vx = -2
        self.creature2sad.vx = -2
        self.creature2bored.vx = -2
        self.creature2tired.vx = -2
        self.creature3.vx = -2
        self.creature3sad.vx = -2
        self.creature3bored.vx = -2
        self.creature3tired.vx = -2
        
    def right2(self, event):
        self.creature1.vx = 0
        self.creature1sad.vx = 0
        self.creature1bored.vx = 0
        self.creature1tired.vx = 0
        self.creature2.vx = 0
        self.creature2sad.vx = 0
        self.creature2bored.vx = 0
        self.creature2tired.vx = 0
        self.creature3.vx = 0
        self.creature3sad.vx = 0
        self.creature3bored.vx = 0
        self.creature3tired.vx = 0
        
    def left2(self, event):
        self.creature1.vx = 0
        self.creature1sad.vx = 0
        self.creature1bored.vx = 0
        self.creature1tired.vx = 0
        self.creature2.vx = 0
        self.creature2sad.vx = 0
        self.creature2bored.vx = 0
        self.creature2tired.vx = 0
        self.creature3.vx = 0
        self.creature3sad.vx = 0
        self.creature3bored.vx = 0
        self.creature3tired.vx = 0
       
    #def up(self, event):
        #player.vy = -10
                    
    def step(self):
        self.f-=.5
        self.s-=.5
        self.p-=.5
        self.creature1.vx += self.creature1.x
        self.creature1sad.vx += self.creature1sad.x
        self.creature1bored.vx += self.creature1bored.x
        self.creature1tired.vx += self.creature1tired.x
        self.creature2.vx += self.creature2.x
        self.creature2sad.vx += self.creature2sad.x
        self.creature2bored.vx += self.creature2bored.x
        self.creature2tired.vx += self.creature2tired.x
        self.creature3.vx += self.creature3.x
        self.creature3sad.vx += self.creature3sad.x
        self.creature3bored.vx += self.creature3bored.x
        self.creature3tired.vx += self.creature3tired.x
        
        #baby
        if self.creature1.visible==True and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature1sad.visible=True
            self.creature1.visible=False
            self.c=True
        elif self.creature1.visible==True and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature1tired.visible=True
            self.creature1.visible=False
            self.c=True
        elif self.creature1.visible==True and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature1bored.visible=True
            self.creature1.visible=False
            self.c=True
        elif self.c==True and self.f>750 and self.s>750 and self.p>750:
            self.creature1.visible=True

        #adolescent    
        if self.creature2.visible==True and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature2sad.visible=True
            self.creature2.visible=False
            self.d=True
        elif self.creature2.visible==True and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature2tired.visible=True
            self.creature2.visible=False
            self.d=True
        elif self.creature2.visible==True and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature2bored.visible=True
            self.creature2.visible=False
            self.d=True
        elif self.d==True and self.f>750 and self.s>750 and self.p>750:
            self.creature2.visible=True

        #adult    
        if self.creature3.visible==True and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature3sad.visible=True
            self.creature3.visible=False
            self.e=True
        elif self.creature3.visible==True and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature3tired.visible=True
            self.creature3.visible=False
            self.e=True
        elif self.creature3.visible==True and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature3bored.visible=True
            self.creature3.visible=False
            self.e=True
        elif self.e==True and self.f>750 and self.s>750 and self.p>750:
            self.creature3.visible=True

            
        if self.b==True and self.s<1000:
            self.s+=.75
        if self.s==1000:
            self.night.visible=False
            b=0
        if self.f==0 or self.s==0 or self.p==0:
            print("game over")
myapp = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()