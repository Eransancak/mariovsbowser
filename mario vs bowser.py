from gamelib import*

game = Game(800,600,"mario vs bowser")     #game name 
bk1 = Image("images\\castleback.jpg",game)    
bk1.resizeTo(800,600)
game.setBackground(bk1)


mario = Animation("images\\mariowalk\\mario",3,game)  
bell = Image("images\\bellformario.png",game)       
bowser = Image("images\\bowser1.png",game)
bridge = Image("images\\bridge.jpg",game)
lava = Image("images\\lava.jpg",game)
mario.resizeTo(40,50)
mario.moveTo(150,360)
mario.stop()
bell.resizeTo(43,53)
bell.moveTo(730,314.5)
bowser.resizeTo(100,90)
bowser.moveTo(650,340)
bridge.resizeTo(520,50)
bridge.moveTo(445,410)
lava.moveTo(450,550)
lava.resizeTo(520,50)

bk2 = Image("images\\endtitle.jpg",game)
bk3 = Image("images\\end screen.png",game)

while not game.over:
     game.processInput()
     bk1.draw()
     mario.draw()
     bell.draw()
     bridge.draw()
     bowser.draw()
     lava.draw()


     
    
           #these are all resizes and change positions of objects
    
     if keys.Pressed[K_LEFT]:
        mario.nextFrame()
        mario.moveX(-8)
     elif keys.Pressed[K_RIGHT]:
        mario.prevFrame()
        mario.moveX(8)
     elif keys.Pressed[K_UP]:
        mario.moveTo(mario.x - 10,mario.y - 30)
     elif keys.Pressed[K_DOWN]:
        mario.moveTo(mario.x + 30,mario.y + 40)
     if mario.collidedWith(bell,"rectangular"):
         bridge.moveTo(x=2000,y=1000)
         bowser.moveTo(450,500)
         
     

     if keys.Pressed[K_0]:
          bowser.moveTo(bowser.x -10,bowser.y-25)
     if keys.Pressed[K_9]:
          bowser.moveTo(bowser.x+10,bowser.y+25)
     if mario.collidedWith(bowser,"rectangular"):
         game.over = True
         bk2.resizeTo(800,600)
         bk2.draw()
      
         game.setBackground(bk2)

     if bk1.x + bk1.width/2 < 0:
        bk1.moveTo(bk2.x + bk2.width,bk2.y)
     if bk2.x + bk2.width/2 < 0:
        bk2.moveTo(bk1.x + bk1.width,bk1.y)
     if bowser.collidedWith(lava,"rectangular"):
          bk3.resizeTo(800,600)
          bk3.draw()

      

     game.update(30)





