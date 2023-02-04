# Bubble/Sinking Sort

In this algorithm you'll go through the array side by side. For example consider an array 

[8, 3, 1, 7, 0] 

When we compare the first two elements [8,3], we need to switch the 3 to 8 position then we get [3,8]
next we compare the element with the next digit / index hence [8,1], and then we change it again to [1,8] and since 
the array has 5 elements the overall comparisons done here are n-1 that is 4 comparisons. This is the worst case 
scenario that we need to consider for getting the first element to the last one.