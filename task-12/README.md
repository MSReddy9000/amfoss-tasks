# **12. If maths was fun :P**
## **Initial Approach to the problem**
My first thought was to somehow use differentiation but, since the computer is doing all the work for me, I settled on brute-forcing all the values, i.e. find all the values of x for given b,c; store them in an array and use min() on it in the end :p Unfortunately, CodeChef was timing me out for such a long execution. It was during this time that I discovered PyPy3 when I googled "how to make python code run fast". So I ran the code in PyPy3 and it "kinda" worked. The execution time was still super high so, I tried to approach the problem differently.
## **New Approach to the problem**
So, thinking for a long time I went to desmos and plotted a graph for the function. Turns out that in the given interval, it was always a parabola no matter the b,c. So, I went to drawing lots of parabolas on paper. Suddenly, a different approach came to my mind. I configured the startDomain and endDomain. I would find the sum and divide it by 2. Then, I would see if the function decreased or increased for a small increase in x. If it decreased, the new startDomain would be (startDomain + endDomain)/2. If it increased, the new endDomain would be (startDomain + endDomain)/2. I ran the code 150 times to make sure the technique worked. It did. The PyPy3 execution time was 0.57 seconds. The irony is that I used the concept of differentiation anyway.

My CodeChef username is "msreddy9000" without the quotes. The .py file I wrote will be uploaded to this folder.

P.S. This had to be my FAVOURITE task in ALL of the 15. Totally wrecked my brain!
