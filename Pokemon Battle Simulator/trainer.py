#st. num: 12751571
import random
class Trainer(object):
    """ Args:
            Class trainer crate a trainer object. This object have a name and a team of 2 pokemon. In particular 
            we can see a has-a relationship. Every trainer has a pokemon.

                self._naem --> initialize the name of the trainer
                self._pokemon_team --> initialize the team. It is a python list

            Since those variables are private the only way to access them is using the properties name and pokemon_team.

    """
    def __init__(self, name):
        self._name = name
        self._pokemon_team = []

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_pokemon_team(self):
        if len(self._pokemon_team) == 0:
            raise(ValueError(f"{self._name} does not have a team"))
        else:
            return self._pokemon_team

    def set_pokemon_team(self, pokemon_team):
        self._pokemon_team = pokemon_team

    def choosePokemon(self):
        """Args:
                Here we randomly choose a pokemon from the pokemon team. The idea is to simulate that the trainer
                choose the pokemon by itself.
                
            Return:
                If the length of the trainer list is zero so i other words the team of the trainer is empty then we
                reaise an error that says the traner doesn't have a team.
                Else it will return a random string in the pokemon team or in other words a random pokemon.
        
        """
        if len(self._pokemon_team) == 0:
            raise(ValueError(f"{self._name} does not have a team"))
        else:
            return random.choice(self._pokemon_team) #return pokemon chosen form the list
    
    def addPokemon(self, pokemon):
        """ Args:
                This will add the pokemon given to the team. Since a tram can be maximum of two 
                pokemon if the number of the pokemon exceed it will print "Team full"
        """
        if len(self._pokemon_team)<3:
            self._pokemon_team.append(pokemon)
        else:
            print("Team full") #this is for when the temam is full

    #properties
    name = property(get_name, set_name)
    pokemon_team = property(get_pokemon_team, set_pokemon_team)

if __name__ == "__main__":
 
        trainer1 = Trainer("Ash")
        trainer1.addPokemon("Pikachu")  
        trainer1.addPokemon("Charmander")  
        trainer1.addPokemon("Bulbsaur")  
        

        print(trainer1.pokemon_team) 

        empty_trainer = Trainer("Brook")

        try:
            print(empty_trainer.get_pokemon_team())  
        except ValueError as e:
            print(e)

        try:
             print(empty_trainer.choosePokemon())

        except ValueError as e:
             print(e)
