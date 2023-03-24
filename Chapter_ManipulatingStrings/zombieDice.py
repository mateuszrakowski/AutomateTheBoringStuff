import zombiedice, random


class RandomZombie:
    def __init__(self, name):
        self.name = name
    
    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() # first roll

        while True:
            if random.randint(0, 1) == 0:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break


class TwoBrainZombie:
    def __init__(self, name):
        self.name = name

    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]
            
            if brains == 2:
                break
            diceRollResults = zombiedice.roll()


class TwoShotgunsZombie:
    def __init__(self, name):
        self.name = name


    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        shotguns = 0
        while diceRollResults is not None:
            shotguns += diceRollResults["shotgun"]
                
            if shotguns == 2:
                break
            diceRollResults = zombiedice.roll()


class OneToFourZombie:
    def __init__(self, name):
        self.name = name


    def turn(self, gameState):
        shotguns = 0

        for _ in range(random.randint(1, 4)):
            diceRollResults = zombiedice.roll()

            if diceRollResults is not None:
                shotguns += diceRollResults["shotgun"]
            if shotguns == 2:
                break


class MoreShotguns:
    def __init__(self, name):
        self.name = name

    
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()

        brains, shotguns = 0, 0
        while diceRollResults is not None:
            brains += diceRollResults["brains"]
            shotguns += diceRollResults["shotgun"]
    
            if shotguns > brains:
                break
            diceRollResults = zombiedice.roll()


zombies = (
    RandomZombie(name="Random Zombie"),
    TwoBrainZombie(name="Two brains Zombie"),
    TwoShotgunsZombie(name="Two shotguns Zombie"),
    OneToFourZombie(name="OneToFour Zombie"),
    MoreShotguns(name="MoreShotguns Zombie")
)


zombiedice.runWebGui(zombies=zombies, numGames=10000)