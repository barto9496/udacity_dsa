# Notation

When you see two pieces of code you can say which one is faster and which one is slower. This can be solely based on human approximation. 

## How can we definitely say that a program is really efficient? 
We can define efficiency of code in something called big O notation. The expression always contains of O and an algebraic expression(usually a function). Ex: O(log(n)) O(n) O(n^3) O(n^2) O(1). O(1) is a valid expression as the data in the parenthesis doesn't really give a functional expression the O(1) represents O(Osubscript(n) + 1). 


## So what does the algebraic expression mean in this case? 
n represents the length of input to your program. Imagine your friend gives you a secret encoded program where you have to decode it and get the string which consists a secret message. You write a psuedocode


## Algorithm
function decode(input):
    create output_string
    for each letter in input:
        get new_letter from letters location in cipher
        add new letter to output
    return output_string

The big O notation for this program becomes(Here the algebraic expression turns out to be):
both creating and return the output string happens only once. So

O(_____ + 2) // 2 representing the two operations that happen creating and returning the string 
and for the two other operation in the for loop are run n number of times so: 

O(2n+2)

Ex: 

If our input string had 10 letters then our output or big O notation would result to:

2(10)+2 = 22

if the input had 1 million then to compute the overall value it would take

2(1 million)+ 2 ~ 2 million