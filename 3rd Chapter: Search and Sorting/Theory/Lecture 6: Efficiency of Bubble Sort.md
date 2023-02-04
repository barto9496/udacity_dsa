# Efficiency of Bubble Sort

Iteration 1    2    3    4 
/# Comp  n-1  n-1  n-1  n-1

THis is the case where we need to compare the first with the second element, the worst case scenario is when we went 
through the whole array to sort the elements in it. So the worst case would be (n-1) * (n-1) = n^2 - 2n + 1, the 
constant or lower polynomial terms can be ignored. hence the worst case would be O(n^2)

