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
1. I personally think that this is the toughest question in the whole set, right alongside the Pizza one.
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
3. Now, if the total no. of boxes was greater, I sorted the max capacities of the boxes in descending order and took out the largest boxes "k" times. So, I would have k of the largest boxes from the total. I summed those k max capacities with the total no. of infinity stones that needed to be protected. If they're equal, they can be protected. Else, Thanos wins. Well........ tbh he's gonna win anyway but, that's a story for another day
100/100
