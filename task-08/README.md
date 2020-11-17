# **8. Sir Perceval’s quest**
## **Method of Approach**
*This task was pretty straightforward. I went ahead and downloaded the perceval tool and all it's dependencies. This .py script I used has a LOT of shell commands for creating and deleting files and they're specific to Linux-based systems. This is how I approached the task:*
1. Using the os package provided by Python, I made use of "curl" to download the .json file listing all repositories in the organization "amfoss". I named the .json file "repo_list.json" This script works for any organization, just have to change the starting organization variable.
2. Using the json package, I loaded the whole file into a Python list and stored in the "data" variable. Here I deleted the repo_list.json file as I had no more use for it.
3. Then, I went searching through the list for the name of each repository and stored it into another list called "res"
4. At this point, I created a shell script "sirPercevalsJourney.sh" and added into it the required commands created by concatenating multiple variables. I stored each of those commands into a "perceval_request" variable and added it into the script along with "cat task-8.json" I created a task-8.json previously (though tbh I have no idea why that cat command is used).
5. Now all the commands required for fetching all the commits using perceval were in the sirPercevalsJourney.sh file. I changed it's permission to execute using "chmod +x" and executed the script.
6. After some time, a commits.json file remained along with the shell script and the task-8.json file. I deleted both of them using the terminal as they no longer have any use.
7. The only files that remain now are the commits.json and the Python script. All the commits in all the repositories of the organization "amfoss" are now stored in the commits.json file
### **NOTE: This .py script CANNOT be run on Windows systems**
