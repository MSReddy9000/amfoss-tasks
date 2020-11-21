# **4. Debugging Derbies**
## **List of all the bugs I encountered while compiling/running the .java file, how I found them and how I fixed them**
1. 1st set of Syntax Errors when I tried to compile the file:\
\
   $javac MathQuiz.java\
-> MathQuiz.java:22: error: ';' expected\
       ButtonGroup levelGroup = new ButtonGroup()\
-> MathQuiz.java:75: error: '(' or '[' expected\
	   JPanel panel1 = new JPanel; // types + levels\
-> MathQuiz.java:96: error: ';' expected\
           panel31.setBorder(new TitledBorder("Correct Count"))\
-> MathQuiz.java:226: error: ';' expected\
           gameOver.setLocationRelativeTo(null)\
-> MathQuiz.java:332: error: ';' expected\
                   question = ("" + num1 + "*" + num2) // question label content\
-> MathQuiz.java:442: error: ';' expected\
                   radioButton8.setText("Select the interval") // cleaning radio button of interval\
-> MathQuiz.java:457: error: ';' expected\
           frame.pack()\
-> MathQuiz.java:461: error: ';' expected\
           frame.setVisible(true)\
   8 errors
### **How I found them**
I just ran the code in an online Java IDE
### **The fix**
I added a semicolon at the end of all the lines that required one and I added a () to the end of the 75th line before the semicolon judging by the similar code above it.\

2. 2nd set of Syntax Errors:

   $javac MathQuiz.java\
-> MathQuiz.java:61: error: cannot find symbol\
       Font font = new Font("Verdana", Font.BOLD, 50);\
     symbol:   class Font\
     location: class MathQuiz\
-> MathQuiz.java:61: error: cannot find symbol\
       Font font = new Font("Verdana", Font.BOLD, 50);\
     symbol:   class Font\
     location: class MathQuiz\
-> MathQuiz.java:61: error: cannot find symbol\
       Font font = new Font("Verdana", Font.BOLD, 50);\
     symbol:   variable Font\
     location: class MathQuiz\
-> MathQuiz.java:15: error: cannot find symbol\
           panel211.add(questionLabel);\
     symbol:   variable questionLabel\
     location: class MathQuiz\
   4 errors
### **How I found them**
I just ran the code in an online Java IDE after fixing the issues in the 1st set
### **The fix** 
I found this line at the beginning of the program "//import java.awt.Font;" I just removed the two slashes at the beginning to uncomment the line\

3. 3rd set of Syntax Errors:

   $javac MathQuiz.java\
-> MathQuiz.java:15: error: cannot find symbol\
           panel211.add(questionLabel);\
     symbol:   variable questionLabel\
     location: class MathQuiz\
   1 error
### **How I found it**
I just ran the code in an online Java IDE after fixing the issues in the 2nd set
### **The fix**
So, this wasn't solved by the java.awt.Font thingy. So, to figure out where the problem was: I "Ctrl+F" ed the program and searched for questionLabel and didn't find the declaration of that variable. So, I searched for Label and right in the beginning of the program "QuestionLabel" was declared. I changed it to "questionLabel"\
 
#### **By this point, I could get the program running, so all errors from here on out are either logical ones or typos**

**4. If a correct answer is input, the Correct counter decreases by one while the Wrong counter increases by 23**
### **How I found it**
I just entered a lot of inputs with my calculator in my hand for verification
### **The fix**
I searched through the program for counters and sure enough I found both the counters of the program with wrong increase intervals. I changed both of them to increment by 1 depending on the input (+=1)

**5. Multiply is displayed as Multipy**
### **How I found it**
It was like right in the middle of the screen
### **The fix**
I searched for "multipy" and found 3 instances. I added an 'l' to all of them

**6. The operations displayed in the checkboxes didn't match the question being displayed on the screen. Addition was displaying and accepting "multiplication", Subtract was displaying "-" but accepting "/", multiplication was displaying and accepting "+", division was displaying "multiplication".**
### **How I found it**
I may have mashed my LMB on Start and Stop too many times
### **The fix*
I searched the program to see the if statement used to decide the output. I found the "operator" variable handling all that. I searched for operator and found all the abnormalities in the code. There were two such pieces of code in the file. One for the first time and one for regenerating. I replaced all the wrong operators with the proper ones including the ones being displayed on the screen\

**7. The division operator was accepting the "quotient" of the answer, not the answer with decimal places.**
### **How I found it**
While fixing the 6th bug, I saw that "/" was being used properly in the script. So, I figured the problem had to be with how Java dealt with division.
### **The fix**
I had no idea (Still don't have......... lol) of what Java was or how it was used or it's syntax or anything about it, So I hit up Google to see if there was a way to convert the integer division into a float one. I found out that if you convert either of the numerator or denominator into a float, the final answer will also be a float. So, I converted the numerator into one and got a proper double answer. I stored it in a variable called "temp". Now, the issue was to round the answer. I figured 2 decimal places should be quite enough. So, I googled again and found a solution using Math.round() so, I implemented it using the temp variable I stored the division into. I changed all the values for both the generation and re-generation pieces. I also searched for "division" in the code and changed the display text to "Divison (Round the answer to 2 decimal places)"

**8. The program was sometimes choosing "0" as num2 meaning that, in some cases division by zero was expected.**
### **How I found it**
This one took some time to find, I just kept pressing Enter after randomly entering some number and found a few cases where zero was being chosen as num2
### **The fix**
I searched the code for num2 and found the piece where the random number was chosen. Wherever the range was starting with 0, I added "1" to it so, now there's no chance of division by zero being shown as a question.

#### **These were all the bugs I could find in the program. I'm confident that these were the only bugs present. I'm very sorry if I missed any other bug/s. I tested for a ton of cases with all the operations**
