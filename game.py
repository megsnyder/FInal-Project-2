from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset, ImageAsset, Frame
import random

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

class Screen(Sprite):
    asset = RectangleAsset(1000, 800, noline, black)
    def __init__(self, position):
        super().__init__(Screen.asset, position)
        self.visible=False

class Creature1(Sprite):
    asset=ImageAsset("images/Screenshot 2019-04-30 at 10.png")
    
    def __init__(self, position):
        super().__init__(Creature1.asset, position)
        self.visible=True

class Creature1sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (1).png")
    
    def __init__(self, position):
        super().__init__(Creature1sad.asset, position)
        self.visible=False

class Creature1bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (3).png")
    
    def __init__(self, position):
        super().__init__(Creature1bored.asset, position)
        self.visible=False

class Creature1tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9 (2).png")
    
    def __init__(self, position):
        super().__init__(Creature1tired.asset, position)
        self.visible=False
        
class Creature2(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 9.png")
    
    def __init__(self, position):
        super().__init__(Creature2.asset, position)
        self.visible=False

class Creature2sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (3).png")
    
    def __init__(self, position):
        super().__init__(Creature2sad.asset, position)
        self.visible=False

class Creature2bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10.png")
    
    def __init__(self, position):
        super().__init__(Creature2bored.asset, position)
        self.visible=False

class Creature2tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (2).png")
    
    def __init__(self, position):
        super().__init__(Creature2tired.asset, position)
        self.visible=False
        
class Creature3(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (5).png")
    
    def __init__(self, position):
        super().__init__(Creature3.asset, position)
        self.visible=False

class Creature3sad(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (4).png")
    
    def __init__(self, position):
        super().__init__(Creature1sad.asset, position)
        self.visible=False

class Creature3bored(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (6).png")
    
    def __init__(self, position):
        super().__init__(Creature1bored.asset, position)
        self.visible=False

class Creature3tired(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-01 at 10 (1).png")
    
    def __init__(self, position):
        super().__init__(Creature1tired.asset, position)
        self.visible=False

class Food(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-03 at 10.png")
    def __init__(self, position):
        super().__init__(Food.asset, position)
        self.visible=False
class BFood(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-03 at 10.png")
    def __init__(self, position):
        super().__init__(BFood.asset, position)

class Food2(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-20 at 10.png")
    def __init__(self, position):
        super().__init__(Food2.asset, position)
        self.visible=False
class Food3(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-20 at 10 (1).png")
    def __init__(self, position):
        super().__init__(Food3.asset, position)
        self.visible=False
class Trampoline(Sprite):
    asset=ImageAsset("images/Screenshot 2019-05-06 at 9.png")
    def __init__(self, position):
        super().__init__(Trampoline.asset, position)
        
class Day(Sprite):
    asset = RectangleAsset(1000, 800, noline, day)
    def __init__(self, position):
        super().__init__(Day.asset, position)

class Night(Sprite):
    asset = RectangleAsset(1000, 800, noline, night)
    def __init__(self, position):
        super().__init__(Night.asset, position)
        self.visible=False
        
class Feed(Sprite):
    asset = CircleAsset(20, noline, red)
    def __init__(self, position):
        super().__init__(Feed.asset, position)
        
class Sleep(Sprite):
    asset = CircleAsset(20, noline, yellow)
    def __init__(self, position):
        super().__init__(Sleep.asset, position)

class Play(Sprite):
    asset = CircleAsset(20, noline, blue)
    def __init__(self, position):
        super().__init__(Play.asset, position)

class Bed(Sprite):
    asset = ImageAsset("images/Screenshot 2019-05-13 at 10.png")
    def __init__(self, position):
        super().__init__(Bed.asset, position)
        self.visible=False
        
class Game(App):
    def __init__(self,width,height):
        super().__init__(width,height)
        self.x=300
        self.y=300
        self.a=0
        self.vx = 0
        self.vy = 0
        self.m = 0
        self.n=False
        self.c=True
        self.d=False
        self.e=False
        self.fi=False
        self.fo=0
        self.pi=False
        self.po=0
        self.f=1000
        self.s=1000
        self.p=1000
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
        self.bfood=BFood((100,200))
        self.bfood=BFood((60,250))
        self.bfood=BFood((20,220))
        self.bfood=BFood((950,300))
        self.bfood=BFood((920,350))
        self.creature1=Creature1((self.x,self.y))
        self.creature3=Creature3((self.x - 10,self.y - 75))
        self.creature3sad=Creature3sad((self.x - 3,self.y - 5))
        self.creature3tired=Creature3tired((self.x - 28,self.y - 3))
        self.creature3bored=Creature1bored((self.x - 9,self.y))
        self.creature2=Creature2((self.x,self.y - 30))
        self.creature2sad=Creature2sad((self.x - 3,self.y - 5))
        self.creature2tired=Creature2tired((self.x - 28,self.y - 3))
        self.creature2bored=Creature2bored((self.x - 9,self.y))
        self.creature1sad=Creature1sad((self.x - 3,self.y - 5))
        self.creature1tired=Creature1tired((self.x - 28,self.y - 3))
        self.creature1bored=Creature1bored((self.x - 9,self.y))
        self.bed=Bed((self.x + 10,self.y + 10))
        self.feed=Feed((20,500))
        self.sleep=Sleep((60,500))
        self.play=Play((100,500))
        self.screen=Screen((0,0))
        Game.listenKeyEvent("keydown", "f", self.dofeed)
        Game.listenKeyEvent("keydown", "s", self.dosleep)
        Game.listenKeyEvent("keydown", "p", self.doplay)

    def dofeed(self, event):
        if self.f<750:
            self.fi=True
            self.food3=Food3((self.x + 37,self.y + 67))
            self.food2=Food2((self.x + 35,self.y + 60))
            self.food=Food((self.x + 36,self.y + 43))
            self.food3.visible=True
            self.food2.visible=True
            self.food.visible=True

    def dosleep(self, event):
        self.night.visible=True
        self.bed.visible=True
        self.creature1.visible=False
        self.creature1sad.visible=False
        self.creature1tired.visible=False
        self.creature1bored.visible=False
        self.creature2.visible=False
        self.creature2sad.visible=False
        self.creature2tired.visible=False
        self.creature2bored.visible=False
        self.creature3.visible=False
        self.creature3sad.visible=False
        self.creature3tired.visible=False
        self.creature3bored.visible=False
        self.n=True
        self.a+=1  
        if 3<self.a<=6:
            self.c=False
            self.d=True
            self.creature1.visible=False
            self.creature1sad.visible=False
            self.creature1tired.visible=False
            self.creature1bored.visible=False
            self.creature2.visible=True
        elif self.a>6:
            self.c=False
            self.d=False
            self.e=True
            self.creature2.visible=False
            self.creature2sad.visible=False
            self.creature2tired.visible=False
            self.creature2bored.visible=False
            self.creature3.visible=True
                        
    def doplay(self, event):
        self.pi=True
        self.trampoline=Trampoline((self.x ,self.y + 100))
                    
    def step(self):
        if self.n==False and self.fi==False and self.pi==False:
            self.f-=.25
            self.s-=.25
            self.p-=.25
        
        self.m+=1
        if self.m==80:
            self.m=0
            self.vx = random.randint(-1,1)
            self.vy = random.randint(-1,1)
        if self.m==50:
            self.vx = 0
            self.vy = 0
            
        if -10 < self.x <1000 and self.fi ==False and self.n==False and self.pi==False:
            self.x += self.vx

        if 130 < self.y < 700 and self.fi ==False and self.n==False and self.pi==False:
            self.y += self.vy

        self.creature1.x=self.x
        self.creature1sad.x=self.x
        self.creature1bored.x=self.x
        self.creature1tired.x=self.x
        self.creature2.x=self.x
        self.creature2sad.x=self.x
        self.creature2bored.x=self.x
        self.creature2tired.x=self.x
        self.creature3.x=self.x
        self.creature3sad.x=self.x
        self.creature3bored.x=self.x
        self.creature3tired.x=self.x
        
        self.creature1.y=self.y
        self.creature1sad.y=self.y
        self.creature1bored.y=self.y
        self.creature1tired.y=self.y
        self.creature2.y=self.y
        self.creature2sad.y=self.y
        self.creature2bored.y=self.y
        self.creature2tired.y=self.y
        self.creature3.y=self.y
        self.creature3sad.y=self.y
        self.creature3bored.y=self.y
        self.creature3tired.y=self.y
        
        #baby
        if self.c==True and self.n==False and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature1sad.visible=True
            self.creature1.visible=False
            self.creature1bored.visible=False
            self.creature1tired.visible=False
        elif self.c==True and self.n==False and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature1tired.visible=True
            self.creature1.visible=False
            self.creature1bored.visible=False
            self.creature1sad.visible=False
        elif self.c==True and self.n==False and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature1bored.visible=True
            self.creature1.visible=False
            self.creature1sad.visible=False
            self.creature1tired.visible=False
        elif self.c==True and self.n==False and self.f>750 and self.s>750 and self.p>750:
            self.creature1.visible=True

        #adolescent    
        if self.d==True and self.n==False and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature2sad.visible=True
            self.creature2.visible=False
            self.creature2bored.visible=False
            self.creature2tired.visible=False
        elif self.d==True and self.n==False and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature2tired.visible=True
            self.creature2.visible=False
            self.creature2bored.visible=False
            self.creature2sad.visible=False
        elif self.d==True and self.n==False and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature2bored.visible=True
            self.creature2.visible=False
            self.creature2sad.visible=False
            self.creature2tired.visible=False
        elif self.d==True and self.n==False and self.f>750 and self.s>750 and self.p>750:
            self.creature2.visible=True

        #adult    
        if self.e==True and self.n==False and self.f<750 and self.f<=self.s and self.f<=self.p:
            self.creature3sad.visible=True
            self.creature3.visible=False
            self.creature3bored.visible=False
            self.creature3tired.visible=False
        elif self.e==True and self.n==False and self.s<750 and self.s<=self.f and self.f<=self.p:
            self.creature3tired.visible=True
            self.creature3.visible=False
            self.creature3bored.visible=False
            self.creature3sad.visible=False
        elif self.e==True and self.n==False and self.p<750 and self.p<=self.s and self.p<=self.f:
            self.creature3bored.visible=True
            self.creature3.visible=False
            self.creature3sad.visible=False
            self.creature3tired.visible=False
        elif self.e==True and self.n==False and self.f>750 and self.s>750 and self.p>750:
            self.creature3.visible=True
        

        if self.fi==True:
            if self.f<750:
                self.f+=50
                self.fo+=50
            
            if self.f>=1000:
                self.fi=False
        if self.fo==100:
            self.food.visible=False
        if self.fo==200:
            self.food2.visible=False
        if self.fo==250:
            self.food3.visible=False
            self.fo=0
            
        if self.pi==True and self.p>=1000:
            self.pi=False
        if self.pi==True and self.f<750:
            self.p+=10   
            
        if self.n==True and self.s<1000:
            self.s+=.25
        if self.s>=1000:
            self.night.visible=False
            self.bed.visible=False
            self.n=False
    
        if self.f==0 or self.s==0 or self.p==0:
            print("game over")
            self.screen.visible=True
myapp = Game(SCREEN_WIDTH,SCREEN_HEIGHT)
myapp.run()