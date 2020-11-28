# **7. Ubiquitous UI**
## **Learning to use Flutter**
I had no idea of what either Flutter or Dart was before starting this project. I looked up a few courses on YouTube for Dart. It seemed pretty similar to C, so I didn't struggle much. Instead of watching hrs of videos on Flutter, I decided to start coding the app right away.
## **Method of Approach**
So, I took a first look at the Sample .gif and soon enough decided on an approach.\
a. Make a new Flutter project and delete most of its code,\
b. Add a "Create an account" button to the UI,\
c. Create two tabs/pages as shown in the UI,\
d. Add the pictures to each page,\
e. Create those animated dots,\
And that's it! Right?
### **a. Make a new Flutter project and delete most of its code**
Nothing to say here lol, just create a new Flutter project in Android Studio
### **b. Add a "Create an account" button to the UI**
I googled a lot about buttons in Flutter and decided to settle on a Floating Action Button(FAB) instead of say, a raw material button. Reason? FABs are retained over pages, unlike raw material buttons. I found that out the hard way ;_; So, I aligned the FAB and changed its color. But, it wouldn't change its size. The workaround I found on Google was to wrap it in a SizedBox with a proper border, and it was large enough now.
### **c. Create two tabs/pages as shown in the UI**
So, this part is where I understood that you guys intentionally mislead us with the resources. I spent a lot of time figuring out Tabs and TabControllers and how to get them into different screens. In the end, I had to use Pageview and not Tabs, so Lesson Learnt!
### **d. Add the pictures to each page**
So, after downloading the assets provided. I got them each(1x,2x,3x) into the app only to realize that they were way too small to be useful. Upon closer inspection of the sample UI, I realized that I HAD to do some image editing to make the UI look like that. So, I downloaded GIMP. I imported the Canvas of the 3x images, deleted them, and opened the 2x ones in layers. I left the .xcf files for both the pages in the assets/images/ folder for you guys to confirm.
### **e. Create those animated dots**
This was ironically the most time taking part for me. Why? Cuz the resource provided were indicators all right. The fact remained that they were NOT ANIMATED. So, I spent a LOT of time setting up the dots_indicator. I got everything set up pretty fast except for the position factor. I TRIED and TRIED and TRIED to store the current page position into a global variable..... I forgot that I wasn't dealing with Python. SO, that's on me. Anyway, after that, I looked it up on Google, and apparently, I had to use setState() so, I changed my project from a Stateless Widget to a Stateful Widget. And when I FINALLY got it working, the dots weren't getting animated. I was almost going to give up on this project. Again, Google bailed me out pointing me to a [different package altogether](https://pub.dev/packages/smooth_page_indicator) So, ummmmm. It got set up in no more than a few minutes and, the dot was being perfectly animated. So, I wasted 4 hrs dealing with the wrong package....... I removed dots_indicator from the project and added smooth_page_indicator instead, and finally, everything was perfect
## **Setting up the project**
I am running Ubuntu as a VM so, I couldn't use Android Studio's emulator. I connected my phone and debugged the app. I ran "flutter clean" and "flutter build apk"  I installed the app on my phone, so the recording I upload will be on my phone instead of on an emulator.

