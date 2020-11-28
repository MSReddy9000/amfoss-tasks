# **9. Spammer_Spaghetti**
## **Learning Javascript and HTML**
This wasn't particularly challenging, as I already knew a bit of how HTML worked. Javascript seemed like a mash of C and Python so, didn't take long for me to figure out a way to approach the task
## **Method of Approach**
So this is what came to my mind when I read the task statement: First, change the text in the text box to "Hi". Second, automate the clicking process. Third, implement a loop to do it again and again. Fourth, add a timer to send messages slowly and not alarm telegram or something. Figured a message every 100 milliseconds would be enough.
## **Learning the Commands needed**
Wasn't too difficult, I opened Telegram Web on two different webpages and went to the text box on one page and send button on another. Right clicked on them and went to inspect element. So I figured out changing the text in the text box. Next, was the clicking. I did a bit of googling and found out that I had to use getElementsById along with click() but when I inspected the element of the send button it didn't contain an id. So more research led me to use trigger with mousedown. The rest of the loop and delaying was pretty similar to C. The messages will be spammed until I close the window.
