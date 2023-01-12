# Lecture 10 Worst case and approximation

Since the amount of steps can vary widely based on the specific implementation, we normally use approximations when talking 
about efficiency or big O notation. The efficiency can be O(n), when you are running a code in production you need to keep
in mind the efficiency of the code running. We need to make sure that for some cases all the computations are performed.
Say you have to compute the secret decipher again. You need to consider that one of the letters might be z and need to go
all the way till the end of the letters enum/array for decoding the array. There are more things you need to consider, 
In reality there is a small possibility that you will go through all the computations. But when talking about efficiency 
we talk about worst case scenario where we would have to check all letters till z. In most cases you can also talk about 
best case and average case scenarios. The worst case would be all 26, the best case would be 1, and the average 
case would be about 13th letter, in a perfect world the computations would be around the avg efficiency, sometimes more 
and sometimes less if we're going try and calculate the efficiency for the average case we get O((13+3)n + n). We've been 
talking about time efficiency, but you can use the same notation to define space efficiency, space efficiency isn't that 
commonly asked, but you still need to read about it. For ex: copying a 3 length string from one place to another would 
require 3 spaces of the particular data type.