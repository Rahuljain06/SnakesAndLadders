import random

class Snakes:
    def __init__(self,st,end):
        self.snake={}
        self.snake[st]=end




class board():
    Snakes={27:8,34:7,29:3,69:31,72:36,77:46}
    Ladders={4:16,6:25,12:49,30:60,38:88,58:62}
    def __init__(self,players,verbose=False):
        self.players=players
        self.n_players=[0]*players
        self.turn=0
        self.verbose=verbose
        self.winner=None
        self.last_pos=100
    def die_roll(self):
        return random.randrange(1,6)
    
    def move_player(self,player_i):
        prev_pos=self.n_players[player_i]
        new_pos=prev_pos+self.die_roll()

        if new_pos==self.last_pos:
            self.winner=player_i
            new_pos=self.last_pos
        elif new_pos>self.last_pos:
            new_pos=prev_pos
        elif new_pos in self.Snakes:
            new_pos=self.Snakes[new_pos]
        elif new_pos in self.Ladders:
            new_pos=self.Ladders[new_pos]
        self.n_players[player_i]=new_pos

    def move_players(self):
        for player_i in range(self.players):
            self.move_player(player_i)
            if self.winner is not None:
                break
    
    def play(self):
        while self.winner is None:
            self.turn+=1
            self.move_players()
            if self.verbose:
                self.PrintTurn()
        return f" Player #{self.winner+1} is won" 
    def PrintTurn(self):
        print(f" Turn {self.turn}:")

        #print players with position
        player_pos=" | ".join([f" ({player_i+1}) at {pos}" for player_i,pos in enumerate(self.n_players)])
        print(player_pos)
        


if __name__=="__main__":
    s1=Snakes(2,4)

    game=board(4,True)
    print(game.play())
    










    


 



