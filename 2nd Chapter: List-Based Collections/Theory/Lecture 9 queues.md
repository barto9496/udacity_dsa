# Queues

Imagine a line of people waiting in a line for the best 
chocolate pancake ever, here the person who has been in the 
line the longest gets the pancake first and gets out of the 
line first (Also known as the First in first out or a queue). 
Queue is kind of opposite in this way the first one entering 
leaves first whereas in stacks the last one entering leaves 
first in stacks. 

The first element / the oldest element in the queue is called 
the head and the last element(new element) is called the tail.

## Enqueue and Dequeue

When and elements enters the queue it is called Enqueue and 
when the element leaves the queue it is called dequeue. There 
is another method called peek where you look at the head, but 
not remove it again this data structure can be implemented with 
a linked list where you also save references to head and tail. 
So you can look them up in constant times. There are two special 
types of queue that show up a lot 

1. Deques: Can enqueue and deque from both front and the back. If you think about it a Deques is a generalised structure of stacks, it can be treated as stacks and Que at the same time, meaning that you can add the element at one end, while also being able to remove the element from that end or else a que where you add at one end and remove at the other 
2. Priority queue: This element has a numerical priority assigned to each element that are being added to the queue, when you remove an element you remove the element with the highest priority. This doesn't necessarily follow the rules of queues. If the elements have the same priority the oldest element gets removed first.



![Screenshot 2023-01-17 at 3.12.08 PM.png](..%2F..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2F6l%2F880slxf52mq_wtsyg3t566dh0000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_koAalb%2FScreenshot%202023-01-17%20at%203.12.08%20PM.png)