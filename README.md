# hackathon_dec2016


SECTION - A

PROBLEM - 1 (two parts) : 

(i) Write a function which accepts 2 params - a string and a word and computes the following:

A. Count occurrences of the word in the string
B. Remove that word from string
C. Append same word equal to number of occurrences in string.


(ii) Write a program that reads a json file , performs following edits and store json back to the same file. update following fields - 

A. Change firewall - protocol - from tcp to udp
B. Change 3rd vnics- portgroup name to EXT_VLAN_201b
C. Change ospf- enabled = false to true 
D. Update holddowntimer = holddowntimer +keepalivetimer

-------------------------------------------------------------------------------------------------------------------------


SECTION : B

PROBLEM - 2 : 

A boy fell down from 2nd floor and suffered serious Brain Damage. Now he's gone crazy. He can only walk 2x step forward or 1 step backward where x is his current position. So if he is at 5th position and he has to reach 8th position, He will go 1 step backward to 4th position and then he will Jump 2*4 step forward to reach 8th position.

Example:

Input
First line will contain an integer T denoting the number of test cases ,
Next T lines will contain 2 integers st and dt denoting the starting and destination point.
Output
Output the minimum steps required to reach destination in a new line.
Constraints
1<=t<=10
1<=st,dt<=1000

SAMPLE INPUT   		SAMPLE OUTPUT
2
1 3				3
3 1				2

Explanation
For First Test case: He can jump to 2nd position and again to 4th position, now he can move to 3rd position by taking a step backward.
For Second Test case: He can directly take 1 step backward, twice to reach his destination.

-------------------------------------------------------------------------------------------------------------------------


PROBLEM - 3

Sonam Gupta Kyu Bewafa hai ?
Our Special detective Mashoor Gulati has found out that Sonam Gupta is "Bewafa" because she is marrying CHITVAN by betraying her boyfriend . Seeing this her boyfriend jumped from the building in PREVIOUS question .

NOW ... CHITVAN lives in special city where if you travel in pair it is free but if you travel single you have to pay according to distance traveled (1 unit distance = 1 unit money). CHITVAN has invited N people (N is even) to his wedding . They may or may not be located at different places. CHITVAN is paying all of there travel expenses.

Now CHITVAN is busy in preparation of wedding so he need your help. He want to pay MINIMUM travel expense, so he want to make pair of everyone.

Help CHITVAN to find MINIMUM expense in making pair. Position of every person is given according in 2-D Cartesian plane .

 
Hard
Input:
First line contain integer N denoting number of 	.
Next N lines contain two integer Xi and Yi denoting position of ith person.
Output:
Output the MINIMUM amount rounded to 2 decimal places CHITVAN have to pay.

Constraints:
2<=N<=16
1<=Xi,Yi <= 1000

Example :
Input:
4
10 3
2 7
5 8
6 7

Output:
8.82

Explanation:
The pair formed is of (1st,4th) and (2nd,3rd) .
The distance traveled by 1st person to go to 4th person or vice-versa = 5.6568
The distance traveled by 2nd person to go to 3rd person or vice-versa = 3.1622
Total distance or Total money = 5.6568 + 3.1622 = 8.81907
Rounded to 8.82

SAMPLE INPUT 
4
10 3
2 7
5 8
6 7

SAMPLE OUTPUT
8.82
-------------------------------------------------------------------------------------------------------------------------

