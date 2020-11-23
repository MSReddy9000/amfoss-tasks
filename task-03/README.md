# **3. Programming**
My hackerrank username is "ashishreddy9000" without the quotation marks. All the solutions I came up with will be uploaded to this folder :)
#### **NOTE: Some of these problems were attempted in the very beginning, some of them in the middle and some of them in the very end of the time given for submitting this repo so, I have LOTS of submissions for a few problems. Like DOZENS of submissions. I hope you guys will excuse me for so many submissions. I will give a brief explanation of the FINAL algorithm that I arrived to for each problem here**
#### **NOTE: Tasks were submitted in both Python 3 and PyPy3.**
## **1. Great Eye --> GreatEye.py**
### **Final Submission Interpreter/Compiler**
PyPy3 Compiler
### **Algorithm Used**
1. I checked whether a kth word existed or not. If not, it would print "-1" straight away
2. I located the kth word using the initial list I took the input into
3. I wrote a loop to iterate through the word and add all it's ascii values.
### **Points obtained**
100/100
## **2. Good strings. --> Goodstrings..py**
### **Final Submission interpreter/compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This algorithm was rather simple, A string is bad if it has equal no. of 0's and 1's. Otheriwse, it's ALWAYS a good string. Those are the only 2 possible cases. So, if a string is bad, it needs to be divided into 2 parts and that's about it!
2. I iterated through the string and appended all 1's to one list and 0's to another list.
3. I finally compared their lengths to check if they're equal or not and then, printed 1 or 2 acc. to it
### **Points Obtained**
100/100
## **3. Ryuk and His Death Notes --> RyukandHisDeathNotes.py**
### **Final Submission interpreter/compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This algorithm was simple as well. I just kept subtracting the required no. of notes from the total no. of available notes.
2. I checked if any of the values were less than zero after subtraction. If not, 1 would be added to the note count. Else, the loop would be broken and the note number will be printed out
### **Points Obtained**
100/100
## **4. Rich Tony Poor Spidey --> RichTonyPoorSpidey.py**
### **Final Submission interpreter/compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This problem didn't really have a medium difficulty. It was just about as easy as any of the above. 
2. Since Tony told Spidey that he could pick any number of bags, obv. he should pick ALL the bags. But, the question is which bag should the college tuition be subtracted from?
3. That's actually pretty simple, I sorted the list in ascending order and removed the college tuition from the largest bag,i.e. money[-1]. ez
### **Points Obtained**
100/100
## **5. Jack Jack Codes --> JackJackCodes.py**
### **Final Submission Interpreter/Compiler**
PyPy3 Compiler
### **Algorithm Used**
1. I personally think that this is the toughest question in the whole set, right alongside Pizza Fest.
2. I just crudely added every element in the list that's not itself and checked if it was equal to m or not. If a match is found, the loop will break
3. It works for smaller lists but, is horrifyingly slow for large lists. I'm at my wit's end here and decided that this was the best I could do. 
### **Points obtained**
80/100
## **6. Infinity Stones --> InfinityStones.py**
### **Final Submission Interpreter/Compiler**
PyPy3 Compiler
### **Algorithm Used**
1. As easy as this problem was... I read the whole question wrong and wasted HOURS of time trying to figure out a way. I thought there were n infinity stones PLUS the infinity stones already in the boxes. After reading the whole question clearly again, I finally understood that there were only n infinity stones which were ALREADY in the boxes :facepalm:
2. The implementation is quite simple, I checked if the total no. of boxes is less than or equal to the no. of boxes the Avengers can protect. If so, True would be immediately printed
3. Now, if the total no. of boxes was greater, I sorted the max capacities of the boxes in descending order and took out the largest boxes "k" times. So, I would have k of the largest boxes from the total. I summed those k max capacities with the total no. of infinity stones that needed to be protected. If they're equal, they can be protected. Else, Thanos wins. Well tbh he's gonna win anyway but, that's a story for another day.
### **Points Obtained**
100/100
## **7. Pizza Fest --> PizzaFest.py**
### **Final Submission Interpreter/Compiler**
PyPy3 Compiler
### **Algorithm Used**
1. I gotta hand it to PyPy3 here, it got me 12 extra points for the exact same code when compared to Python 3 :kek:
### **Points Obtained**
42.86/100
## **8. The D --> TheD.py**
### **Final Submission Interpreter/Compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This was the only question that COMPLETELY stumped me,i.e. I couldn't think of a SINGLE algorithm to apply here. Like I HAD NO IDEA how to solve this problem and still don't have.
2. I just manually typed out the D's for n=3 to n=29...............................................no comments here
### **Points Obtained**
100/100
## **9. Homework Time --> HomeworkTime.py**
### **Final Submission Interpreter/Compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This is another one of those questions which cost me hours of valuable time because I was too lazy to read the question properly
2. The question CLEARLY asked us to use the remainder of the series number when it was divided with 10^9 + 7 and somehow every time I managed to TOTALLY ignore it
3. Well, turns out that was really the only thing that was failing my code. I created two lists with 1,2,3 in them. One of them will be used as a buffer to add the three elements. Once the addition was complete, the sum would be appended to both the buffer and Series lists.
4. The 0th index of the buffer will be popped and the cycle will go on and on for 1000000 times (999997 to be precise)
5. The required index will be called and reversed using [::-1] and all the leading zeros will be popped off using .lstrip("0")
### **Points Obtained**
100/100
## **10. Minimum Ninja Sum --> MinimumNinjaSum.py**
### **Final Submission Interpreter/Compiler**
Python 3 Interpreter
### **Algorithm Used**
1. This was a rather simple problem, It just took me a bit of time (or 12 submissions) to understand where I was going wrong.
2. The problem itself is pretty straightforward. Add some k digits, calculate the same for the next digit, subtract them and store them, and finally print the least of all such subtractions.
3. If a ninja sum didn't exist, the program would automatically print "-1"
4. So I calculated the no. of ninja sums actually possible by the forumla "len(n) - k" and repeated the below operation that many times
5. So, the logic here is that you don't really need to add all the digits together. It took me quite a while to realize that. I only had to subtract the first digit of the first ninja sum and the last digit of the adjacent ninja sum. All the numbers in the middle would be the exact same, so they'll get subtracted during the sum anyway. 
6. So, I subtracted all such first and last digits and added the absolute difference to the list if the obtained mns was less than the one already in the list. So, in the end I only had to print out the last index of the mns_list.
### **Points Obtained**
100/100

### **Total Accumulated Points at time of writing**
922.86/1000
