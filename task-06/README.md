# **6. Geddit**
## **Method of Approach**
Okay, so this was "kinda" a tricky one. Especially since I had no idea where the documentation to the whole Go-Reddit thing was. So, I decided on a much simpler approach. I'd divide the task into two different parts:
1. Conducting a query for "memes" or just about anything 
2. Upvoting up to 100 of last week's posts
### **2. Upvoting up to 100 of last week's posts**
This was about as simple it could get. I created a Reddit app, copied all its credentials, and used the custom HTML client provided by vartanbeno. He already put up examples for extracting five posts and upvoting posts. I set the limit to 100 and changed the time to "week"  I looped through the whole "posts" variable to upvote every post in it. After that was done the program would print "All ze posts have been upvoted, m'Lord!"
### **1. Conducting a query for "memes" or just about anything**
I couldn't have possibly solved this by myself. I used weird techniques like html.Get() and so many other useless things that came to my mind. I searched A LOT for proper documentation on Go-Reddit but, all those that showed up were for Python. I was almost going to give up on this task. Then I asked a friend, Geo Jolly Cheramvelil, how he solved the task. He sent me this [file](https://github.com/vartanbeno/go-reddit/blob/master/reddit/subreddit.go) and asked me to go through it. I couldn't believe my eyes. It was the .go file where every useful function for subreddits was defined. I quickly 'Ctrl+F'ed for 'Search' and found a function specifically designed for that. It took me less than a minute after that to set up the query and extracting the 1st element from the list (index 0). I quickly adjusted it with the rest of the script. So, hurray! The task was finally complete
#### **NOTE: I removed my Client-ID, Secret, Username, and Password from the script for obv reasons. Just replace those fields with ones of your own to test the script**
