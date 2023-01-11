# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy(object):
    def __init__(self):
        self.items = []
        self.classiness = 0

    global classy_list
    classy_list = []

    def getClassiness(self):
        classiness = 0
        for x in classy_list:
            match x:
                case "tophat":
                    classiness = classiness + 2
                case "bowtie":
                    classiness = classiness + 4
                case "monocle":
                    classiness = classiness + 5
                case _:
                    classiness = classiness + 0
        return classiness

    def addItem(self, item):
        classy_list.append(item)


# Test cases
me = Classy()

# Should be 0
print(me.getClassiness())

me.addItem("tophat")
# Should be 2
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")
# Should be 11
print(me.getClassiness())

me.addItem("bowtie")
me.addItem("bowtie")
# Should be 15
print(me.getClassiness())
