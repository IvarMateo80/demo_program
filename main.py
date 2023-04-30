#create a pygame program that shows a bouncing ball (pelota rebotando)
#Game is a class that has the methods to run the logic for the bouncing ball

#main is responsible of creating an instance of class Game 
#then it calls method run for the instance of class Game
from game import Game


if __name__ == "__main__":
    #create instance (object) of class Game
    game = Game() 
    #call method run using the "game" object
    game.run()