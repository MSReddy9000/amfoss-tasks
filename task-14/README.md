# **14. Bandit**
## **Method of Approach**
*I thought these were pretty difficult questions but, they weren't at all. They took me less than an hr to research and complete. The password of each level will be uploaded to their respective folder. All the commands I used to arrive to the solution will be posted here.*
### **level-0**
Commands used:\
ls\
cat readme
### **level-1**
Commands used:\
ls\
cat ./-
### **level-2**
Commands used:\
ls\
cat "spaces in this filename"
### **level-3**
Commands used:\
ls\
cd inhere\
ls\
find\
cat ./.hidden
### **level-4**
Commands used:\
ls\
cd inhere\
ls\
cat ./-file00\
reset\
cat ./-file01\
reset\
cat ./-file02\
reset\
cat ./-file03\
reset\
cat ./-file04\
reset\
cat ./-file05\
reset\
cat ./-file06\
reset\
cat ./-file07\
reset
### **level-5**
Commands used:\
ls\
cd inhere\
ls\
find
#### **After a ton of googling about find**\
find ./ -type f -size 1033c ! - executable\
cd maybehere07\
ls\
cat ./.file2
### **level-6**
Commands used:\
ls\
ls -a\
ls -l -a\
cd ..\
ls -l -a\
find -user bandit7 -group bandit6\
cd\
find / -user bandit7 -group bandit6 -size 33c
#### **all files had permission denied except for /var/lib/dpkg/info/bandit7.password So, I figured that was the only place the password could be**\
cd /var/lib/dpkg/info/ \
cat bandit7.password
### **level-7**
Commands used:\
ls\
cat data.txt\
grep millionth data.txt
### **level-8**
Commands used:\
ls\
cat data.txt
#### **After googling what each function does for a lot of time**
sort data.txt
#### **By simple visual inspection I found that UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR is repeated only once**
### **level-9**
Commands used:\
ls\
cat data.txt\
sort data.txt\
grep "======" data.txt
#### **After a lot of research on strings**
strings data.txt | grep =========
### **level-10**
Commands used:\
ls\
cat data.txt
#### **I literally googled "decode base64 on Linux terminal" and straight up got hit with the command lmao**
base64 -d data.txt
