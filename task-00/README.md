# **0. Install Ubuntu 20.04 [Desktop]**
## **Attempt 1: Dual-boot Installation**
I used Rufus to flash the .iso to a flash drive. I successfully managed to boot through the USB. Not long after, I got a prompt that my hard drives used Intel RST and, I had to disable it. I referred to the official guide offered by Canonical, although they did mention that there was a pretty good chance of soft-bricking the PC. I went ahead and disabled RST anyway. Now, Windows refused to boot. So, Attempt 1 is a failure.
## **Attempt 2: Installing Ubuntu 18.04.5 LTS**
So a lot of people mentioned on the internet that they didn't face the problem while installing the 18.04 version so, I did the same again. Only this time, the Ubuntu installer didn't recognize the Operating System present(Windows). So, I went to Google again. This time, I had to disable Secure Boot, Fast Boot, and then boot the OS in Legacy mode. After doing the first two, the bios of my laptop gave me a prompt that legacy type booting wasn't available on this device. Attempt 2 is a failure.
## **Attempt 3: Installing Ubuntu 20.04.1 LTS as a Virtual Machine**
I downloaded VMware Player 16 and downloaded the .iso to use Ubuntu as a Virtual Machine. Now, the only problem was that both of my hard disks had Bitlocker encryption. So, partitioning was not feasible. So I had to wait for 8 hrs for Windows to decrypt both the drives. Still, I wasn't able to partition my C drive. So I downloaded a 3rd party partition manager and finally managed to set up Ubuntu as a Virtual Machine. Attempt 3 is "kind of"successful?
### **Customising Ubuntu**
Since Ubuntu is so customizable, I decided why not make it look like a Macbook? So I went ahead and did that :P
