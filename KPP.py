#Krabby Patty Party
#Mery,Lingxiao,Tszching
from gamelib import*#imports the game library of classes and functions
game = Game (800,600,"Krabby patty party",20)#game object
bk = Image("bk3.jpg",game)#image object
bk.resizeTo(800,600)
game.setBackground(bk)
sb = Image("spongebob.png",game)
sb.resizeBy(-45)
sb.moveTo(400,500)
bomb = Image("bomb.png",game)
bomb.resizeBy(-85)
bomb.moveTo(100,50)
clock = Image("clock.gif",game)                                                                                                                                                                                                                                                                          
clock.resizeBy(-60)
clock.moveTo(100,100)


#magnet = Image("magnet.png",game)


kp = []
for index in range(40):
    kp.append( Image( "krabbypatty1.png",game))
    
for index in range(40):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,8)
    kp[index].resizeBy(-85)
    kp[index].moveTo(x, -y)
    kp[index].setSpeed(s,180)

bomb = []
for index in range(30):
    bomb.append( Image( "bomb.png",game))
    
for index in range(30):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(2,6)
    bomb[index].resizeBy(-85)
    bomb[index].moveTo(x, -y)
    bomb[index].setSpeed(s,180)

clock = []
for index in range(25):
    clock.append( Image( "clock.gif",game))
    
for index in range(25):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(4,7)
    clock[index].resizeBy(-60)
    clock[index].moveTo(x, -y)
    clock[index].setSpeed(s,180)

ice = []
for index in range(25):
    ice.append( Image( "ice.jpg",game))
    
for index in range(25):
    x = randint(100,800)
    y = randint(100,3000)
    s = randint(7,8)
    ice[index].resizeBy(-65)
    ice[index].moveTo(x, -y)
    ice[index].setSpeed(s,180)

kpPassed = 0
kpcount = 0
bombPassed = 0
bombcount = 0
icePassed = 0
icecount = 0
clockPassed = 0
clockcount = 0
while not game.over:#while loops runs until game is over
    game.processInput()#process Input
    bk.draw()
    sb.draw()
    
    for index in range(40):
        kp[index].move()
        if kp[index].collidedWith(sb):
            game.score+= 1
            kp[index].visible = False
        if kp[index].isOffScreen("bottom") and kp[index].visible:
            kpPassed += 1
            kp[index].visible = False

    for index in range(30):
        bomb[index].move()
        if bomb[index].collidedWith(sb):
             game.score-=3
             bomb[index].visible = False
        if bomb[index].isOffScreen("bottom") and bomb[index].visible:
            bombPassed += 1
            bomb[index].visible = False

    for index in range(25):
        ice[index].move()
        if ice[index].collidedWith(sb):
            kp[index].speed-=1
            ice[index].visible = False
        if ice[index].isOffScreen("bottom") and ice[index].visible:
            icePassed += 1
            ice[index].visible = False           


    for index in range(20):
        clock[index].move()
        if clock[index].collidedWith(sb):
            game.time+= 5
            clock[index].visible = False
        if clock[index].isOffScreen("bottom") and clock[index].visible:
            clockPassed += 1
            clock[index].visible = False    
 

   
    if keys.Pressed[K_RIGHT]:
        sb.x += 8
    if keys.Pressed[K_LEFT]:
        sb.x -= 8

    if game.score>=8:
        game.drawText("Level Clear",250,5)
        game.over = True
     
        
    if game.score<0:
        game.drawText("YOU ARE FIRED",250,5)
        game.over = True
        
    game.displayScore()
    game.displayTime(100,5)

     
    game.update(30)

game.quit()
