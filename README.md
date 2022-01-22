# DATA-STRUCTURES-CSE-220-BRACU

# LAB ASSIGNMENTS

<h3 align="left">Languages:</h3>
<p align="left"> <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>


# LAB 1 - Arrays 📝

1. Shift Left k Cells   
Consider an array named source. Write a method/function named shiftLeft( source, k) that shifts all the elements of the source array to the left by 'k' positions. You must execute the method by passing an array and number of cells to be shifted. After calling the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
shiftLeft(source,3)
After calling shiftLeft(source,3), printing the array should give the output as: 
 [ 40, 50, 60, 0, 0, 0 ]

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%201.py">Task 1</a> <br>


2. Rotate Left k cells 
 Consider an array named source. Write a method/function named rotateLeft( source, k) that rotates all the elements of the source array to the left by 'k' positions. You must execute the method by passing an array and number of cells to be shifted. After calling the method, print the array to show whether the elements have been shifted properly.
Example:
source=[10,20,30,40,50,60]
rotateLeft(source,3)
After calling rotateLeft(source,3), printing the array should give the output as: 
 [ 40, 50, 60, 10, 20, 30]

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%202.py">Task 2</a>  <br>

3. Remove an element from an array
 Consider an array named source. Write a method/function named remove( source, size, idx) that removes the element in index idx of the source array. You must execute the method by passing an array, its size and the idx( that is the index of the element to be removed). After calling the method, print the array to show whether the element of that particular index has been removed properly.
Example:
source=[10,20,30,40,50,0,0]
remove(source,5,2)
After calling remove(source,5,2) , printing the array should give the output as: 
 [ 10,20,40,50,0,0,0]

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%203.py">Task 3</a> <br>

4. Remove all occurrences of a particular element from an array
Consider an array named source. Write a method/function named removeAll( source, size, element) that removes all the occurrences of the given element in the source array. You must execute the method by passing an array, its size and the element to be removed. After calling the method, print the array to show whether all the occurrences of the element have been removed properly.
Example:
source=[10,2,30,2,50,2,2,0,0]
removeAll(source,7,2)
After calling removeAll(source,7,2), all the occurrences of 2 must be removed. Printing the array afterwards should give the output as: 
 [ 10,30,50,0,0,0,0,0,0]
 
Ans: ⚡  <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%204.py">Task 4</a> <br>

5. Splitting an Array
Suppose the elements of an array A containing positive integers, denote the weights in kilograms. And we have a beam balance. We want to put the weights on both pans of the balance in such a way that for some index 0 < i < A.length - 1, all values starting from A[0], A[1], upto A[ i - 1], should be on the left pan. And all values starting from A[ i ] upto A[ A.length - 1] should be on the right pan and the left and right pan should be balanced. If such an i exists, return true. Else, return false. 
Input: [1, 1, 1, 2, 1]	Output : true
Explanation: (summation of [1, 1, 1] = summation of [2,1])
Input: [2, 1, 1, 2, 1] Output: false
Input: [10, 3, 1, 2, 10]  Output: true 
Explanation: (summation of [10, 3] = summation of [1,2,10]))

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%205.py">Task 5</a> <br>

6. Array series
Write a method that takes an integer value n as a parameter. Inside the method, you should create an array of length n squared (n*n) and fill the array with the following pattern. Return the array at the end and print it.
If,
n=2: { 0,1,   2,1 } (spaces have been added to show two distinct groups).
n=3 : { 0, 0, 1,    0, 2, 1,    3, 2, 1 } ((spaces have been added to show three distinct 
groups).
n=4 : {0, 0, 0, 1,   0, 0, 2, 1,    0, 3, 2, 1,   4, 3, 2, 1}  (spaces have been added to show four distinct groups).

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%206.py">Task 6</a> <br>

7. Max Bunch Count
A "bunch" in an array is a consecutive chain of two or more adjacent elements of the same value. Write a method that returns the number of elements in the largest bunch found in the given array.
Input: [1, 2, 2, 3, 4, 4, 4]   Output: 3
Explanation: There are two bunches here {2,2} and {4,4,4}. The largest bunch is {4,4,4} containing 3 elements so 3 is returned.
Input: [1,1,2, 2, 1, 1,1,1] Output:4
 Explanation: There are three bunches here {1,1} and {2,2} and {1,1,1,1}. The largest bunch is {1,1,1,1} containing 4 elements so 4 is returned.

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%207.py">Task 7</a> <br>
 
8. Repetition
 Write a method that takes in an array as a parameter and counts the repetition of each element. That is, if an element has appeared in the array more than once, then its ‘repetition’ is its number of occurrences. The method returns true if there are at least two elements with the same number of ‘repetition’. Otherwise, return false.
Input: {4,5,6,6,4,3,6,4} Output: True
Explanation: Two numbers repeat in this array: 4 and 6. 4 has a repetition of 3, 6 has a repetition of 3. Since two numbers have the same repetition output is True.
Input: {3,4,6,3,4,7,4,6,8,6,6} Output: False
Explanation: Three numbers repeat in this array:3,4 and 6 .3 has a repetition of 2, 4 has a repetition of 3, 6 has a repetition of 4. Since no two numbers have the same repetition output is False.

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%208.py">Task 8</a> <br>

9. Circular Array
NB: You need to implement circular arrays to solve the following problems. You cannot convert them to linear arrays.
 Palindrome
Write a method/function that takes in a circular array, its size and start index and finds whether the elements in the array form a palindrome or not. Return true if the elements form a palindrome, otherwise, return false.
Example:

Input: [20,10,0,0,0,10,20,30] (start =5, size=5) Output: True.

Input:[10,20,0,0,0,10,20,30] (start =5, size=5) Output: False

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%209.py">Task 9</a> <br>

10. Intersection
Write a method/function that takes two circular arrays, their sizes and start indexes and returns a linear array containing the common elements between the two circular arrays.
Input: 
Circular array 1 : [40,50,0,0,0,10,20,30] (start_1 =5, size_1 =5)
[10 20 30 40 50]
Circular array 2 : [10,20,5,0,0,0,0,0,5,40,15,25] (start_2=8, size_2 =7)
[5 40 15 25 10 20 5]
Output:[10,20,40]

Ans: ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%2010.py">Task 10</a> <br>

11. Suppose you have been hired to develop a musical chair game. In this game there will be 7 participants and all of them will be moving clockwise around a set of 7 chairs organized in a circular manner while music will be played in the background. You will control the music using random numbers between 0-3.If the generated random number is 1, you will stop the music and if the number of participants who are still in the game is n, the participants at position (n/2) will be eliminated. Each time a participant is eliminated, a chair will be removed and you have to print the player names who are still in the game.The game will end when there will be only one participant left. At the end of the game,display the name of the winner.
[Hint: You will need to invoke a method to generate a random number between 0
(inclusive) to 3 (inclusive)]

Ans:  ⚡ <a href="https://github.com/AnonXarkA/DATA-STRUCTURES-CSE220-BRACU/blob/main/LAB%201/task%2011.py">Task 11</a> <br>
