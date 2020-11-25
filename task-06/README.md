# **6. Geddit**
## **Method of Approach**
Okay, so this was "kinda" a tricky one. Especially due to the fact that I had no idea where the documentation to the whole Go-Reddit thing was in. So, I decided on a much simpler approach. I'd divide the whole task into 2 different parts:
1. Conducting a query for "memes" or just about anything 
2. Upvoting upto a 100 of last week's posts
### **2. Upvoting upto a 100 of last week's posts**
This was about as simple it could get. I created a reddit app, copied all it's credentials and used the custom HTML client provided by vartanbeno. He already put up examples for extracting 5 posts and upvoting posts. I set the limit to 100 and changed the time to "week". I looped through the whole "posts" variable to upvote each and every post in it. Once, that was done it would print "All ze posts have been upvoted m'Lord!"
### **1. Conducting a query for "memes" or just about anything**
I couldn't have possibly solved this by myself. I used weird techniques like html.Get() and so many other useless things that came to my mind. I searched A LOT for proper documentation on Go-Reddit but, all those that showed up were for Python. I was almost going to give up on this task. Then I asked a friend, Geo Jolly Cheramvelil, how he solved the task. He sent me this [file](https://github.com/vartanbeno/go-reddit/blob/master/reddit/subreddit.go) and asked me to go through it. I couldn't believe my eyes. It was the .go file where each and every useful function for subreddits were defined. I quickly 'Ctrl+F'ed for 'Search' and found a function specifically designed for that. It took me less than a minute after that to set up the query and extracting the 1st element from the list (index 0) and adjust it with the rest of the script. So, hurray! The task was finally complete lmao
#### **NOTE: I removed my Client-ID, Secret, Username and Password from the script for obv. reasons. Just replace those fields with ones of ur own to test the script**
