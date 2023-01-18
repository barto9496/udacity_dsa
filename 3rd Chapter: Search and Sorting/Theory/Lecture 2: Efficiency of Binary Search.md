# Efficiency of Binary Search

Let's talk about the efficiency of Binary search algorithm with an example.

Here we have an array of 8 elements, and we're going to find the no 10

[1,2,3,4,5,6,7,8] => 10?

The problem with this array is there are even no of elements in the array 
So, we can start with either 4 or 5 

When you're designing your algorithm you need decide whether you're going to 
err on the lower side or the higher side when you are hit with a case like this. 
Let's say I decide to err on the lower side of the array. 

In that case i would have to check if 10 is greater than / less than or equal to 4 

Since our number is bigger, you'll only have to look at the second half of the array. 
Again there are an even number of elements in our array. So we compare with the n/2 - 1 
element of the array which in this case it would be 6 and 10 is greater than 6. 
Similarly, when you go with the array [7,8] you consider 7 in your case which is 
lower than 10 and then ending up on the last element which is 8. 

So the time efficiency of the algorithm isn't really O(n) instead it is O(n/2) as for 
an array of 8 elements we had 4 iterations 
