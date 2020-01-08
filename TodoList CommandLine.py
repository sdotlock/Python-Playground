import sys

# Creates item class
class Item(object):
    def __init__ (self, text, complete=False):
        self.text = text
        self.complete = complete
    
    def __str__(self):
        return self.text

    # Changes todo item status to complete
    def markComplete(self):
        self.complete = True

# Adds a new Item to the ToDo list, default not complete(false)
def addCommand():
    print("What would you like to add?")
    text = sys.stdin.readline().strip()
    items.append(Item(text))

# Prints entire list of todos
def listCommand():
    n = 0
    for item in items:
        print('{}: {}: {}'.format(n,item.text, item.complete))
        n += 1

# Changes status of item to complete
def markDoneCommand():
    listCommand()
    print("Mark which item (0..) as done?")
    index = int(sys.stdin.readline().strip())
    items[index].markComplete()

# Removes command from list.
def removeCommand():
    listCommand()
    print("Mark which item (0..) as done?")
    index = int(sys.stdin.readline().strip())
    del items[index]

# Counts items in todo list.
def countList():
    print(len(items) - 1)

# Prints dictionary of commands
def printCommands():
    for cmd in commands:
        print(cmd)

# Zips items into an indexed array. Unused method. 
def zipItems():
    zipped = zip(range(1,100), items)
   
# Dictionary of commands.
commands = {
    'add' : addCommand,
    'count' : countList,
    'commands' : printCommands, 
    'zip' : zipItems,
    'mark-done' : markDoneCommand,
    'remove' : removeCommand
}
commands['list'] = listCommand

items = [] 


# Loads todos from a text file, along with their current status.  
try:       
    with open('todo.txt') as fp:
        for line in fp.readlines():
            it = line.split(', ')
            
            if "True" in it[1]:
                items.append(Item(it[0].strip(), True))
            elif "False" in it[1]:
                items.append(Item(it[0].strip()))       
except FileNotFoundError:
    print("loading file failed")
finally:
    pass

print("write a to-do list")

# Gets input from user; runs command from dictionary.
while True:
    user_cmd  = sys.stdin.readline().strip()
    if user_cmd == 'quit':
        break
    elif user_cmd in commands:
        commands[user_cmd]()

# Saves to text file.
with open('todo.txt', 'w') as fp:
    for item in items:
        fp.write(item.text + ", " + str(item.complete) + '\n')
        
# Says goodbye, thanks for reading.     
print("bye")