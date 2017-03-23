from gamelib import *

game = Game(800,600,"mario vs bowser 2")
bk = Image("mario\\castle.png",game)
mario = Image("mario\\mariowalk ",game)
button = Image("mario\\button.png",game)
bridge = Image("mario\\bridge.png",game)
mario.resizeTo(50,25)
mario.moveto(-90,0)
bridge.resizeTo(150,80)
bridge.movetTo(360,150)


while not game.over:
     game.processInput()
     bk.draw()
     mario.draw()
     bridge.draw()
     button.draw()
     
     


if keys.Pressed[K_LEFT] and mario.left > game.left:
        mario.moveX(-4)
elif keys.Pressed[K_RIGHT] and mario.right < game.right:
        mario.moveX(4)


game.update(20)
game.quit()
