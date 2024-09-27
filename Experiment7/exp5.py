name = "Global Name"

def function():
    name = "Local Name"
    print("Inside function, name:", name)  

class Module:
    name = "Module Name"
    
    @staticmethod
    def show_name():
        print("Inside module, name:", Module.name)

# Main program
print("In global namespace, name:", name) 

function()

Module.show_name()

print("After function call, in global namespace, name:", name) 
