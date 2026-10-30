import random
class Fruit:
    fruit_colours={"orange":"orange","apple":"red","pear":"green","watermelon":"green"}
    def __init__(self,fruit_colours):
        self.fruit_colours=fruit_colours    
    def quiz(self):
        for i in range(3):
            print("Welcome to the fruit quiz!!!")       
            randomy=list(self.fruit_colours.keys())
            key=random.choice(randomy)
            print(key)
            value=self.fruit_colours[key]
            choice=input("What colour is this fruit: ")
            if choice.lower()==value:
                print("Correct")
            else:
                print("Try again")
                choice=input("What colour is this fruit: ")
                if choice!=value:
                    print("Wrong.The answer is",value)
                else:
                    print("Correct")
f=Fruit(Fruit.fruit_colours)
f.quiz()