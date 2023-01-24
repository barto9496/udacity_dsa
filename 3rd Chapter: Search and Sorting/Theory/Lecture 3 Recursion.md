# Recursion

The idea here is to create a function that calls itself. Here is a code that shows recursion.

## Code
function recursive(input):
    if input <= 0:
        return input
    else:
        output = recursive(input-1)
        return output

1. First of all the Recursive function needs to call itself
2. A recursive function needs a base case; Think of it like a while loop you keep going again and again. Here the base case is basically the exit scenario for the system.
3. Without a base case you'll keep stuck in an Infinite Recursion. As it won't exit.
4. You need to alter your input 

Recursive can be very confusing so when you're trying to think through recursion. It's good to create out a table or a list of steps, as the value can be kept track of

Also remember to consider infinite Recursive loops and not fall into it.

Lastly if you are really not sure where your recursive function, you can use a print function, and then you'll know where your program is at.