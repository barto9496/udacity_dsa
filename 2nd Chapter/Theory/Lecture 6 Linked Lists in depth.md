# Linked Lists in Depth

In higher level programming there is no distinction between linked list and array. However interview questions about 
this data structure are fairly common in interviews. So, it's important to know the distinction. Both Linked List and 
array store a single element or the actual information. So, if you have an array or Linked List of numbers it will be a 
single number. In both cases we store some extra info in the data.

In many languages it will look actually assigning next element within this element. So the address of the next element 
is stored in this element. One thing you need to know about linked lists is that when you add the new value the next 
reference of the new element should point to the previously pointing next element and the current new element is being 
pointed by the previous element. The changing of the elements in linked list just takes a constant time and not a 
traversal function time as they are just shifting pointers and looping / iterating through the array or linked list.
|----------------------------------------|
|Linked List        |Linked List         |
|----------------------------------------|
|value: 8            |value: 8           |
|next: 0x112         |next: null         |
|address: 0x111      |address: 0x112     |
|----------------------------------------|

Doubly linked lists:
In this the elements not only point to the next element but also point to the previous element.
|----------------------------------------|
|Linked List         |Linked List        |
|----------------------------------------|
|value: 8            |value: 8           |
|next: 0x112         |next: null         |
|address: 0x111      |address: 0x112     |
|previous: null      |previous: 0x111    |
|----------------------------------------|