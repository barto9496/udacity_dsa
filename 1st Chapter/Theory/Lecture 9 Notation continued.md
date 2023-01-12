# Notation continued

The previous lesson was just the basics, there are a lot of other complications that we need to address: First of all in 
the previous example we need to think of the for loop, does the for loop itself count for something? In order for the 
loop to work you need to do the computation of getting the letter everytime. Since this needs to happen every one time
for the input letter there are three operations which need to be considered. So the big O notation or efficiency can now 
be represented as O(3n+2). The actual operations count can be hard to predict for a pseudocode, we need to know what 
language is the program written in, if it is python there are other things like the data structures that we need to 
consider. In this case we need to compare the letter with each alphabet of the english language which is 26. Initially 
we had O(3n+2), now it changed to O(29n+2). In this case my assumption* is that 3 due to the 3 operations "for", "get and
convert the cipher(this here goes for 26 runs)", and "add" but since we have to get through around 26 letters in the for
loop hence it could be O(29n+2) if 