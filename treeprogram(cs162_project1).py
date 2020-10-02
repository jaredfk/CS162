# Jared Knowlton
# CS 162
# Project 1
'''a simple program with a menu (user input and output, text in a console is perfectly acceptable) to interact with one of the components that you came up with that:
Instantiates an object from a class that you write that has attributes and behaviors reflecting your design,
gets basic input from a user that fills in the attributes of your object,
displays basic info about your object and its behaviors,
A menu item that allows the user to quit the program; saying goodbye when selected,
Note: Be sure to use a loop to get back to the menu after finishing an item (other than quitting) to ask the user what to do next.'''

'''It has been a bit since I have used this stuff so I am a bit rusty! I'm sure there is a way to implement the class more effeciently and effectively
classes and how the syntax work still doesn't quite click in my brain. 
but I feel this code demonstrates the skills asked for in the assignment'''

'''In order to test this program, run it, and enter in integers when asked by the program, at the end you can type Y or N when prompted
to repeat user entry. With more time and development this program could not only collect data about trees, but sort and analyze said data.'''


# Creates the class tree, In future iterations of code I can add more attributes than just the trunk into the tree class.
class Tree:
    # This method within Tree prints the values of the trunk radius, height, and hardness
    def trunk(self):
        print('\nTrunk radius = ' + self.tradius)
        print('Trunk height = ' + self.theight)
        print('Trunk hardness = ' + self.thardness)
    
# This is the user input collection method for the drunk data of each tree
def trunkdata(tree1):
    tree1.tradius = input('What is the radius of your tree trunk?: ')
    tree1.theight =  input('\nHow tall is your tree trunk?: ')
    tree1.thardness = input('\nIs the bark on your tree trunk soft, medium, or hard?: ')
    return tree1

# This is the message that displays at the beginning of the program, explaining its purpose
def startingmenu():
    print('''\nHello, welcome to tree logger, the only program that lets you catalogue and compute all aspects of your trees.
    It's still a work in progress, so for now only trunk data collection is functional.\n''')

# My main function creates a tree object and then collects and records the data about the trunk entered into the list alltrees
def main():
    startingmenu()
    tree1 = Tree()
    trunkdata(tree1)
    tree1.trunk()

    # I couldnt remember how to print the entire list for the user, that will be something I will need to tinker with more and add later.
    alltrees = []
    alltrees.append(tree1)

    # This portion of the code repeats the data collection, I'm sure there is a less messy way to do this, but this is what I have for now. 
    repeat = input('would you like to log another tree? (Y/N): ')
    while repeat == 'Y':
        startingmenu()
        tree1 = Tree()
        trunkdata(tree1)
        tree1.trunk()
        alltrees.append(tree1)
        repeat = input('would you like to log another tree? (Y/N): ')
    
    print('\nThank you for using tree logger, have a great day!')


main()










