# Section 1: Introduction 


1
00:00:00,150 --> 00:00:03,720
Before we get started with the schools, let's understand why.

2
00:00:03,990 --> 00:00:06,480
Why use both Raspberry Pi and Arduino?

3
00:00:06,780 --> 00:00:09,900
And why not just Raspberry Pi, all just Arduino?

4
00:00:10,320 --> 00:00:15,660
In this video, I would explain this to you with a practical mindset so you can start with a better

5
00:00:15,660 --> 00:00:18,480
understanding which will help you throughout the course.

6
00:00:18,480 --> 00:00:19,200
Use the first.

7
00:00:19,200 --> 00:00:25,380
And maybe the biggest difference is that Arduino is run by a microcontroller, whereas the Raspberry

8
00:00:25,380 --> 00:00:28,110
Pi is run by a microprocessor.

9
00:00:28,290 --> 00:00:31,860
So the microcontroller on the Arduino is quite simple.

10
00:00:32,200 --> 00:00:36,990
It's going to run just one program at the maximum speed capacity.

11
00:00:37,230 --> 00:00:37,730
That's it.

12
00:00:38,190 --> 00:00:43,470
On the Raspberry Pi, you have a microprocessor, which is something completely different.

13
00:00:43,890 --> 00:00:50,730
A microprocessor is what you also have on your computer, on your phone, etc. You usually install an

14
00:00:50,730 --> 00:00:55,800
operating system on it and then you can run many programs to do many different things.

15
00:00:55,980 --> 00:01:02,100
If you compare the specs on the microcontroller, Arduino, Uno and the microprocessor on the Raspberry

16
00:01:02,100 --> 00:01:02,730
Pi four.

17
00:01:03,030 --> 00:01:05,490
Well, there is a world of difference.

18
00:01:05,760 --> 00:01:10,620
But and that's what we're going to see now with those specs and a few more details.

19
00:01:10,620 --> 00:01:11,640
I'm going to add later.

20
00:01:11,910 --> 00:01:17,670
You will see that the Arduino is better suited for controlling hardware components in the Raspberry

21
00:01:17,670 --> 00:01:22,920
Pi is better suited for software applications with more processing power.

22
00:01:23,280 --> 00:01:29,610
Now, you might say, well, there are some applications that you can do with either an Arduino or Rutenberg

23
00:01:29,610 --> 00:01:33,900
by, for example, if you try to control an eddy with a push button.

24
00:01:34,140 --> 00:01:37,590
This can be done with both modes with the same result.

25
00:01:37,980 --> 00:01:42,420
So, yes, for a few applications, both modes are going to overlap.

26
00:01:42,870 --> 00:01:47,160
And for both kinds of applications, there is no right or wrong solution.

27
00:01:47,310 --> 00:01:52,260
Now, let's focus on what the Arduino can do better than the Raspberry Pi.

28
00:01:52,590 --> 00:01:57,560
First, there are some hardware functionalities that are only possible with aluminum.

29
00:01:57,900 --> 00:02:04,740
The GPIO panel on the Raspberry Pi is great, but quite limited when you compare it to the pins on the

30
00:02:04,740 --> 00:02:07,950
Arduino, for example, only with Arduino.

31
00:02:08,100 --> 00:02:14,550
You can read from an analog sensor that can be a potential meter, a photo resistor, etc. There is

32
00:02:14,550 --> 00:02:17,160
no way to do that directly with the Raspberry Pi.

33
00:02:18,090 --> 00:02:25,650
Also, some of the pins have a P.W. in functionality, which very basically allows you to send a custom

34
00:02:25,650 --> 00:02:32,040
voltage to a component instead of just, for example, zero and five volt on Arduino B. The value is

35
00:02:32,040 --> 00:02:38,220
native and is handled by the hardware, which means that it's not going to take away any software resources

36
00:02:38,550 --> 00:02:39,600
on the Raspberry Pi.

37
00:02:39,960 --> 00:02:43,320
You could use P.W in, but this is not a hardware one.

38
00:02:43,500 --> 00:02:49,680
This is a software Peter Godwin, which means that it's going to take resources from your CPU, and

39
00:02:49,680 --> 00:02:53,190
it's maybe not going to be as stable as on the Arduino.

40
00:02:53,310 --> 00:02:57,030
Then the adeno is best suited to control models.

41
00:02:57,330 --> 00:03:03,780
And one additional thing here, which is quite important, is the capability to respect real time constraints.

42
00:03:04,050 --> 00:03:06,000
So what is the real time constraint?

43
00:03:06,210 --> 00:03:07,800
Let's use an example here.

44
00:03:07,980 --> 00:03:14,940
So let's say that you are controlling a model and you need to give a command to the model every 20 microseconds.

45
00:03:15,120 --> 00:03:21,870
If you fail to give the next command before 20 microseconds, the model will not behave very smoothly.

46
00:03:22,020 --> 00:03:27,780
So we are, you know, no problem because of the nature of the microcontroller is just running one per

47
00:03:27,810 --> 00:03:28,140
run.

48
00:03:28,350 --> 00:03:35,220
And it's what we call deterministic, which means that you know exactly how long a command will take

49
00:03:35,220 --> 00:03:37,020
to execute every time.

50
00:03:37,380 --> 00:03:43,110
So if you write your code well, you can respect the 20 microseconds delay every time.

51
00:03:43,350 --> 00:03:46,710
On the Raspberry Pi, things are completely different.

52
00:03:47,100 --> 00:03:53,790
The operating system you are running has a scheduler for all the tasks the scheduler will try its best

53
00:03:54,000 --> 00:04:00,930
to make all the tasks run as smoothly as possible, but it can't guarantee that one particular program

54
00:04:01,140 --> 00:04:06,150
is going to respect exactly 20 microseconds between each command sense.

55
00:04:06,510 --> 00:04:12,120
If, for example, another independent program is taking too much resources, then the first program

56
00:04:12,120 --> 00:04:14,700
which controls your model is going to slow down.

57
00:04:14,880 --> 00:04:19,170
And that's a problem, especially when you control physical hardware components.

58
00:04:19,410 --> 00:04:25,350
So in this course of activities and project, we won't have to deal with this real time constraint.

59
00:04:25,560 --> 00:04:31,920
But I wanted to explain it briefly here so you can understand that it's a very important parameter which

60
00:04:31,920 --> 00:04:35,610
you will need to take into account for some of your future project.

61
00:04:35,820 --> 00:04:36,210
All right.

62
00:04:36,300 --> 00:04:42,540
You can already see that the Ardoino is superior to the Raspberry Pi for quite a few things that are

63
00:04:42,540 --> 00:04:45,090
related to hardware control.

64
00:04:45,450 --> 00:04:51,750
Now, let's give a chance to the Raspberry Pi and see when it is better than the Arduino on the Raspberry

65
00:04:51,750 --> 00:04:52,020
Pi.

66
00:04:52,230 --> 00:04:58,620
You get a complete operating system, for example, Linux with the Raspberry Pi OS, and you can install

67
00:04:58,620 --> 00:04:59,630
many more OS.

68
00:04:59,970 --> 00:05:06,120
For example, you went to Android and even some editions of Windows, if you want to, with a complete

69
00:05:06,120 --> 00:05:07,410
operating system will.

70
00:05:07,410 --> 00:05:13,470
Instead of running just one program, you can see that we have a world of possibilities that are not

71
00:05:13,470 --> 00:05:16,030
available on the Arduino, on the Raspberry Pi.

72
00:05:16,050 --> 00:05:22,140
You can program with C++, but also with Python, which we are actually going to do in this course.

73
00:05:22,410 --> 00:05:26,940
In fact, you could use any programming language you want and know a few more examples.

74
00:05:27,330 --> 00:05:34,170
With Raspberry Pi, you can control a camera, for example, the Pi camera or any USB camera, a webcam

75
00:05:34,380 --> 00:05:35,910
that you just need to plug in.

76
00:05:36,120 --> 00:05:42,720
And do that, you can add computer vision, artificial intelligence with machine learning, etc. You

77
00:05:42,720 --> 00:05:46,080
can also host a complete web server if you want to.

78
00:05:46,500 --> 00:05:51,570
And well, on the Raspberry Pi, basically, you can just run many different applications and programs

79
00:05:51,570 --> 00:05:55,140
simultaneously with scaling and multithreading.

80
00:05:55,380 --> 00:05:57,750
Multi-threading is super powerful.

81
00:05:57,960 --> 00:06:00,780
And it's something that doesn't exist on the original.

82
00:06:01,200 --> 00:06:07,230
Well, now, you know, by writing your code, well, you can kind of fake it and create a multitask

83
00:06:07,230 --> 00:06:11,100
program, but nothing to see what you can do with the Raspberry Pi.

84
00:06:11,370 --> 00:06:16,020
OK, I'm going to stop here because the list could go on and on and on forever.

85
00:06:16,380 --> 00:06:23,580
But what you can see here is that the Raspberry Pi is superior to the Arduino when it comes to software.

86
00:06:24,000 --> 00:06:31,290
To recap, Arduino is better for hardware, low level control and Raspberry Pi is better for application

87
00:06:31,290 --> 00:06:33,690
software, a high level of control.

88
00:06:33,930 --> 00:06:38,160
So depending on your project, maybe you just need one bolt.

89
00:06:38,460 --> 00:06:45,150
If your application is to take some photos, process them and publish them on a web page, then just

90
00:06:45,150 --> 00:06:46,290
go with a Raspberry Pi.

91
00:06:46,740 --> 00:06:52,800
If, however, you want to just open the door with a model when you detect a prison nearby, Arduino

92
00:06:52,800 --> 00:06:54,240
will do 100 percent.

93
00:06:54,630 --> 00:07:02,160
But if you need to combine both hardware control and high level software applications, then why not

94
00:07:02,190 --> 00:07:04,140
use the best of both worlds?

95
00:07:04,410 --> 00:07:09,960
And use the combination Raspberry Pi and Arduino with this combination?

96
00:07:10,110 --> 00:07:16,830
You can do a much more complete and complex project by taking advantage of each board supermajority.

97
00:07:16,890 --> 00:07:21,870
That's what we're going to do in the intercom project, where we will use the Raspberry Pi to handle

98
00:07:21,870 --> 00:07:24,150
a Telegram bot and take some photos.

99
00:07:24,420 --> 00:07:30,270
And the Arduino to control has several model as well as other hardware components that use, for example,

100
00:07:30,270 --> 00:07:37,020
P.W. In the Raspberry Pi, you will send commands to the Arduino, and Arduino will also send some data

101
00:07:37,230 --> 00:07:38,680
back to the Raspberry Pi.

102
00:07:38,910 --> 00:07:45,210
And you may not be aware of it, but this combination of microprocessor plus microcontroller is actually

103
00:07:45,210 --> 00:07:46,290
used everywhere.

104
00:07:46,590 --> 00:07:53,010
If you have a phone, a computer, a TV, well, all of them are using a microprocessor on the main

105
00:07:53,010 --> 00:07:54,120
software control.

106
00:07:54,330 --> 00:08:00,210
And then this microprocessor is connected to many microcontrollers, which are handling the hardware

107
00:08:00,570 --> 00:08:01,950
a small robotic example.

108
00:08:01,950 --> 00:08:08,400
Maybe if you take a mobile robot with autonomous navigation, well, you would have a microprocessor

109
00:08:08,400 --> 00:08:15,270
to handle localization, how you live in motion planning, image processing, etc. and you have some

110
00:08:15,270 --> 00:08:21,390
microcontrollers to control the wheels with real time constraints and also get data from different sensors.

111
00:08:21,870 --> 00:08:29,610
To conclude, you can see the Raspberry Pi microprocessor and the brain of your application and Arduino

112
00:08:29,760 --> 00:08:33,570
or microcontroller as the muscles of your application.

113
00:08:33,960 --> 00:08:34,380
All right.

114
00:08:34,560 --> 00:08:39,860
Now that you have a better understanding of the big picture, you are ready to start the course.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 2: Installation Steps


1
00:00:05,160 --> 00:00:12,330
The very first step before using Dubai is to flush an operating system on the SD card you have and to

2
00:00:12,330 --> 00:00:18,690
do some configuration in this lesson, I will show you how you can easily install the Raspberry Pi operating

3
00:00:18,690 --> 00:00:26,820
system on your micro SD card, but also how to set up the Wi-Fi and an SSA connection so we can get

4
00:00:26,820 --> 00:00:30,180
access to the Bay for further configuration.

5
00:00:30,480 --> 00:00:37,170
So to install Raspberry Pi always the first thing you do is you go on Raspberry Pi dot org or you have

6
00:00:37,170 --> 00:00:43,320
the URL and then you can click on software, OK, and you're going to get this page or something that

7
00:00:43,320 --> 00:00:44,640
is maybe similar.

8
00:00:44,910 --> 00:00:45,240
OK?

9
00:00:45,420 --> 00:00:50,820
And you're going to have he installed a Raspberry Pi OS using Raspberry Pi?

10
00:00:50,850 --> 00:00:51,440
Imagine.

11
00:00:51,780 --> 00:00:57,240
So we are going to download the Raspberry Pi imager, which is a software that is going to do everything

12
00:00:57,240 --> 00:00:57,660
for us.

13
00:00:57,960 --> 00:01:00,120
So that's going to make our life simpler.

14
00:01:00,870 --> 00:01:06,720
So you can click here on download for Windows if you're on Windows currently on Microsoft's Ubuntu.

15
00:01:06,780 --> 00:01:13,680
OK, I'm going to download for Windows because I'm going to say you fine, and once it's done, I'm

16
00:01:13,680 --> 00:01:15,960
going to install the Raspberry Pi.

17
00:01:15,990 --> 00:01:16,530
Imagine.

18
00:01:18,900 --> 00:01:22,650
So you click on yes, if you have a pop up and then click on install.

19
00:01:25,330 --> 00:01:26,320
OK, finish.

20
00:01:29,350 --> 00:01:35,380
And if you want to find it easily, well, you just type Raspberry Pi imager on your bar here on the

21
00:01:35,380 --> 00:01:37,630
bottom and you just find the application here.

22
00:01:38,140 --> 00:01:41,020
Maybe it's on your desktop, so once you're here.

23
00:01:42,850 --> 00:01:47,710
Clothes that once you're here, you're going to first choose an operating system that you're going won't

24
00:01:47,710 --> 00:01:48,940
flush into as they go.

25
00:01:49,030 --> 00:01:49,360
OK?

26
00:01:49,720 --> 00:01:53,230
And you're going to choose the first Raspberry Pi choice here.

27
00:01:53,590 --> 00:01:56,800
So just choose the first one you're going to see you have many different ones.

28
00:01:57,400 --> 00:01:57,790
OK?

29
00:01:58,030 --> 00:02:05,110
For example, you can choose whether you can see many different operating system, but we're going to

30
00:02:05,110 --> 00:02:10,130
go with the main one, Raspberry Pi Ice, which was previously named Brazilian.

31
00:02:10,150 --> 00:02:14,200
OK, so if you are looking into installing Rise of Young, well, that's not the new name.

32
00:02:14,470 --> 00:02:17,500
Raspberry Pi voice and then what you are going to do.

33
00:02:17,830 --> 00:02:24,160
So I'm going to put I'm going to physically put my SD card in the computer.

34
00:02:26,610 --> 00:02:31,080
They maybe that's going to open something like this when you don't you don't care about that, OK,

35
00:02:31,080 --> 00:02:35,100
you just close the windows, you can see I already have stuff on that.

36
00:02:35,610 --> 00:02:41,750
I'm going to just close and I'm not going to vomit anything from now, and I'm going to click on, Choose

37
00:02:41,780 --> 00:02:44,400
the Rage and choose the come here.

38
00:02:44,910 --> 00:02:46,050
And you have the addiction.

39
00:02:46,350 --> 00:02:50,960
And one more thing I'm going to do now, and this is a configuration that you can't see on the screen.

40
00:02:50,970 --> 00:02:55,470
I'm going to need to use a shortcut control shift and X.

41
00:02:56,130 --> 00:03:03,150
OK, so you do control shift and X and you see we have a new window here with more configuration.

42
00:03:03,690 --> 00:03:09,600
And so what I'm going to do is I'm going to click on Enable Essence each, and we're going to use use

43
00:03:09,610 --> 00:03:15,420
password authentication with the password for the by user, which is raspberry.

44
00:03:15,420 --> 00:03:21,900
So you can just type raspberry here, OK, to set the password for the user, that's the default password.

45
00:03:22,560 --> 00:03:27,540
And then you can go down and you are going to click also on Configure Wi-Fi.

46
00:03:27,990 --> 00:03:32,280
And these maybe is going to show you the current wife and your connected install.

47
00:03:32,280 --> 00:03:35,940
Make sure that well, here on Windows.

48
00:03:36,210 --> 00:03:42,210
You can see I have, so I have named my network your Wi-Fi network, OK for simplicity, for schools,

49
00:03:42,570 --> 00:03:47,340
and the password is for me, your password because we just replace that.

50
00:03:47,430 --> 00:03:52,750
And so those values have to be the same ones you are using here for your computer.

51
00:03:52,770 --> 00:03:58,470
OK, so that then you can access the Raspberry Pi from your computer because you're going to be in the

52
00:03:58,470 --> 00:03:59,730
same network.

53
00:04:00,900 --> 00:04:07,890
OK, and well, that's OK, so you can click on Save and then you can click on the right, but before

54
00:04:07,890 --> 00:04:13,650
you do that, make sure the SD card doesn't contain anything that you wanted to keep because once you

55
00:04:13,650 --> 00:04:16,530
click on right, that's going to erase everything.

56
00:04:17,400 --> 00:04:18,330
So you keep going, right?

57
00:04:18,670 --> 00:04:18,960
OK.

58
00:04:19,050 --> 00:04:20,410
Everything will be erased.

59
00:04:20,520 --> 00:04:21,210
Are you sure?

60
00:04:21,480 --> 00:04:21,990
Yes.

61
00:04:22,620 --> 00:04:26,160
And then it's going to download the operating system.

62
00:04:29,710 --> 00:04:34,720
So you can kick on cancer if you need to, and it's going to download the Raspberry Pi operating system,

63
00:04:34,720 --> 00:04:40,750
if it's already downloaded before it's going to keep it in retreat from the cash and then he's going

64
00:04:40,750 --> 00:04:47,380
to write it inside the SDK and then you can wait until it's done and that's going to take a few minutes.

65
00:04:52,230 --> 00:04:58,500
OK, and once it is done, if you have any of that, you can just click on OK, cancel.

66
00:04:58,830 --> 00:04:59,190
OK.

67
00:05:00,000 --> 00:05:07,680
Just don't click on format anything and then you can see successfully written OK as you can't continue

68
00:05:08,100 --> 00:05:08,460
it in.

69
00:05:08,460 --> 00:05:13,950
What you can do is remove the SD card from your computer and well, that's it.

70
00:05:14,380 --> 00:05:19,470
No, you will be able to boot your Raspberry Pi with the Raspberry Pi operating system.

71
00:05:24,970 --> 00:05:31,930
With the configuration from the last step on boot, your Raspberry Pi should automatically try to connect

72
00:05:31,930 --> 00:05:34,630
to the Wi-Fi network you've provided.

73
00:05:35,080 --> 00:05:41,620
So what you can do now is first, make sure that your Raspberry Pi is pulled out of OK, this is very

74
00:05:41,620 --> 00:05:42,220
important.

75
00:05:42,700 --> 00:05:48,110
Now you can put the SD card in the SD card slot of the PI.

76
00:05:48,130 --> 00:05:51,670
OK, make sure it is directly inside the slot.

77
00:05:52,000 --> 00:05:58,240
Like you can see here on the screen and then and only then you can pull on your Raspberry Pi.

78
00:05:58,540 --> 00:06:06,100
So what you should see is first, you will have the red LCD, which should be powered on, and then

79
00:06:06,100 --> 00:06:11,220
you should also see just next to it the green LCD blinking quite randomly.

80
00:06:11,230 --> 00:06:18,190
And if it's blinking randomly, it means simply that the Raspberry Pi is booting and so you can wait

81
00:06:18,190 --> 00:06:18,640
a little bit.

82
00:06:18,640 --> 00:06:25,480
And after a few seconds, maybe one minute stop, the Raspberry Pi should be connected to your Wi-Fi

83
00:06:25,480 --> 00:06:26,070
network.

84
00:06:26,680 --> 00:06:33,460
And no, that is where we need to actually find the IP address of the Raspberry Pi and a network so

85
00:06:33,460 --> 00:06:35,170
we can get access to it.

86
00:06:35,890 --> 00:06:39,770
So to find the IP address, we are going to use a tool.

87
00:06:39,790 --> 00:06:44,050
OK, this is another software you can download here.

88
00:06:44,050 --> 00:06:46,580
I'm using the angry IP scanner.

89
00:06:46,600 --> 00:06:53,440
OK, so this tool is quite good to find all the IP addresses and hosts inside a network.

90
00:06:53,830 --> 00:07:01,270
So I've chosen this one because simply it's available for Windows, Mac, all Linux, so anyone can

91
00:07:01,420 --> 00:07:02,000
use it.

92
00:07:02,050 --> 00:07:08,260
We discussed you may have already used some specific software, for example, for Windows, you have

93
00:07:08,650 --> 00:07:12,640
advanced IP scanner, which is as good as angry IP scanner.

94
00:07:12,670 --> 00:07:19,510
Even better so if you already know other IP scanner software for your operating system, free free to

95
00:07:19,510 --> 00:07:20,080
use them.

96
00:07:21,100 --> 00:07:26,530
And if you are going to use angry IP scanner, as I'm doing here, you can simply here.

97
00:07:26,950 --> 00:07:33,550
Well, you can click on that and download and install the software just like you would install any software.

98
00:07:34,210 --> 00:07:43,120
And you will also have to install Java here because the software uses Java, so you can click on here

99
00:07:43,360 --> 00:07:49,270
and just download and install the latest version here.

100
00:07:50,080 --> 00:07:51,580
So you have to install Java.

101
00:07:51,610 --> 00:07:58,120
Plus this software, and if you are using Mac OS, you have the instructions here and Linux, you have

102
00:07:58,120 --> 00:07:59,560
the instructions here.

103
00:08:00,640 --> 00:08:07,660
And know that the software is installed, whether you simply have to start it and you may have another

104
00:08:07,660 --> 00:08:12,820
popup asking you to accept some stuff related to the network.

105
00:08:13,090 --> 00:08:18,190
And so you have to press, yes, OK, so otherwise it will not work.

106
00:08:18,850 --> 00:08:23,690
So you have this software started and before we even do anything.

107
00:08:23,980 --> 00:08:29,980
Please go back to check your Wi-Fi network here and make sure that your laptop.

108
00:08:29,980 --> 00:08:37,750
So this laptop of up there is connected to the same Wi-Fi network as the raspberry base, or has the

109
00:08:37,750 --> 00:08:41,830
configuration you have set up inside of me as the color of the Raspberry Pi?

110
00:08:41,840 --> 00:08:42,130
OK?

111
00:08:42,340 --> 00:08:48,220
If it's not in the same network, you will never be able to find the Raspberry Pi from this computer,

112
00:08:48,230 --> 00:08:51,070
so this is actually a very important first step.

113
00:08:51,100 --> 00:08:52,480
You need to check you.

114
00:08:52,660 --> 00:08:57,550
So once this is done well, go back to angry IP scanner.

115
00:08:57,970 --> 00:09:02,890
And before we price start, we have a little bit of configuration here.

116
00:09:03,190 --> 00:09:05,840
So as you can see, we have the hostname.

117
00:09:05,860 --> 00:09:10,000
The name is the actual the hostname of this nation.

118
00:09:10,000 --> 00:09:11,530
Hensel, that is my host name.

119
00:09:11,530 --> 00:09:18,370
It would be different for you and you are going to click on that IP, but only with a parent here.

120
00:09:18,730 --> 00:09:23,550
So you click on that and you will see different stuff here.

121
00:09:23,560 --> 00:09:32,830
So you may have just one or two or more like like me and you're going to select the one we've Wi-Fi

122
00:09:32,830 --> 00:09:33,120
here.

123
00:09:33,130 --> 00:09:40,060
So this is actually this is the IP address of that computer in the Wi-Fi network.

124
00:09:40,330 --> 00:09:43,720
I have a few other ones here, for example, that we've virtual machines.

125
00:09:44,080 --> 00:09:50,560
But if I chose them, we not be able to connect to the Raspberry Pi because it's not the same network.

126
00:09:50,560 --> 00:09:57,730
So I have to choose the Wi-Fi IP address and as you can see, this will automatically update the IP

127
00:09:57,730 --> 00:09:58,480
range here.

128
00:09:59,500 --> 00:10:05,620
OK, and what you're going to do is actually sort you have four different numbers for an IP address.

129
00:10:06,040 --> 00:10:13,210
You're going to change the last one here for the beginning of the range to, let's say, one and the

130
00:10:13,210 --> 00:10:16,420
last one here to 255.

131
00:10:16,990 --> 00:10:25,750
So when you will scan, this will scan between one and 255 in that network here, and your Raspberry

132
00:10:25,750 --> 00:10:28,960
Pi is somewhere between those two numbers.

133
00:10:29,560 --> 00:10:33,970
So when you scan, you will see the IP address, the hostname and port.

134
00:10:34,540 --> 00:10:43,270
But one thing actually you can do is also click on that here, and we are going to add the Mac vendor

135
00:10:43,300 --> 00:10:43,630
here.

136
00:10:43,750 --> 00:10:44,980
I will show you why later.

137
00:10:44,980 --> 00:10:46,240
So you click on the window.

138
00:10:46,840 --> 00:10:51,370
You put an ad here, so it should be on the left and you click on OK.

139
00:10:51,760 --> 00:10:52,610
So it should be.

140
00:10:52,630 --> 00:10:54,450
Yeah, that column should be here.

141
00:10:55,770 --> 00:10:56,880
And I'll just press that.

142
00:11:01,930 --> 00:11:09,730
OK, and once this is done, you will have that kind of window message, so for me to 30 seconds, it

143
00:11:09,730 --> 00:11:11,110
can take me all this time.

144
00:11:12,340 --> 00:11:18,460
So you can click on close and you have, as you can see, one two three four, five six, et cetera,

145
00:11:18,670 --> 00:11:20,460
until two 55.

146
00:11:21,000 --> 00:11:25,870
The what you can do is simply maybe click on ping and salt by Bing.

147
00:11:25,870 --> 00:11:32,950
So you have all of the different IP addresses which are actually corresponding to real machines.

148
00:11:32,980 --> 00:11:33,340
OK.

149
00:11:33,820 --> 00:11:39,460
So when it's blue, there is something when it's red, it means that nothing has been detected for this

150
00:11:39,460 --> 00:11:45,490
IP address, so we can see that actually, that is the first one here.

151
00:11:45,550 --> 00:11:55,240
This is the laptop I'm using here and I can see here the IP address finishing with fifty six for me.

152
00:11:55,240 --> 00:11:55,560
Sorry.

153
00:11:56,170 --> 00:11:58,210
Of course, this can be completely different for you.

154
00:11:58,210 --> 00:11:59,990
It can be a completely different number here.

155
00:12:00,460 --> 00:12:09,220
I can see a Mac under here Raspberry Pi trading, so it means I have found my Raspberry Pi on the network.

156
00:12:09,710 --> 00:12:15,700
OK, and the reason I have asked you to add to the Mac bundle here is because, well, for some reason

157
00:12:16,300 --> 00:12:16,870
it depends.

158
00:12:16,870 --> 00:12:21,310
Sometimes you may not be able to see the hostname, which would be your Raspberry Pi.

159
00:12:21,700 --> 00:12:27,250
So if you use, for example, the advanced IP scanning software on Windows, you will see the hostname,

160
00:12:27,250 --> 00:12:29,550
but not with angry IP scanner.

161
00:12:29,590 --> 00:12:33,340
I mean, at least not for my specific situation.

162
00:12:34,300 --> 00:12:38,470
So here you can clearly see that this is the Raspberry Pi you're looking for.

163
00:12:38,710 --> 00:12:44,980
If you don't have any information here, you can still get this by looking at the blue dots here because

164
00:12:44,980 --> 00:12:46,510
you will only have a few.

165
00:12:46,540 --> 00:12:48,670
OK, so this is my computer.

166
00:12:48,700 --> 00:12:51,400
The first one will not be Raspberry Pi.

167
00:12:51,400 --> 00:12:53,320
It will not finish with one.

168
00:12:53,590 --> 00:12:59,650
So here, even if I didn't have that, I could guess that these would be the Raspberry Pi IP address.

169
00:13:06,170 --> 00:13:06,590
Great.

170
00:13:06,620 --> 00:13:12,740
You've successfully installed the Raspberry Pi operating system, configured the right way and, you

171
00:13:12,740 --> 00:13:16,520
know, the IP address of the Raspberry Pi in the network.

172
00:13:16,940 --> 00:13:23,990
What we can do now is to use ESA's age to take control over the Raspberry Pi and really get access to

173
00:13:23,990 --> 00:13:24,320
it.

174
00:13:24,920 --> 00:13:33,860
So first of all, I'm going to open a file explorer here and go to my main partition here.

175
00:13:34,190 --> 00:13:37,680
Go to users to select your username.

176
00:13:37,700 --> 00:13:38,090
OK?

177
00:13:38,420 --> 00:13:46,790
And here you may see a Dot H folder here if you don't see it, whether you have nothing to do and you

178
00:13:46,790 --> 00:13:49,310
can just keep the next 20 seconds or so.

179
00:13:49,640 --> 00:13:55,670
If you have an H folder, you're going to go inside and you may have known hosts fine.

180
00:13:56,420 --> 00:14:03,380
What you can do is if you don't know SSA Trost, if you can just simply remove that five note.

181
00:14:03,980 --> 00:14:08,030
It may prevent some errors when you try to connect to your Raspberry Pi.

182
00:14:08,630 --> 00:14:12,290
OK, I know what you can do is to open a terminal.

183
00:14:12,350 --> 00:14:12,800
OK.

184
00:14:12,860 --> 00:14:21,410
So Windows key and then C and a command and click on that and this will open a terminal on windows.

185
00:14:21,650 --> 00:14:25,400
So if you are using Linux, I guess you know how to use a terminal.

186
00:14:25,640 --> 00:14:29,000
And if you're using Mac, you can also open a new terminal.

187
00:14:29,300 --> 00:14:29,660
OK.

188
00:14:29,960 --> 00:14:30,440
And.

189
00:14:31,970 --> 00:14:39,860
If you're using Windows 10, Windows 10 with a quite recently updated version, you can simply connect

190
00:14:39,860 --> 00:14:43,010
to the Raspberry Pi, a siege on the terminal.

191
00:14:43,700 --> 00:14:52,190
So you can easily check if you have HP the available for you on Windows 10 or simply you can type it

192
00:14:52,190 --> 00:14:53,920
page on the terminal and price.

193
00:14:53,930 --> 00:14:54,470
Enter.

194
00:14:54,890 --> 00:14:57,200
OK, here I have a message.

195
00:14:57,200 --> 00:15:02,300
User age is his age, so if you have that, it means you have this age and you don't need to do anything

196
00:15:02,300 --> 00:15:09,020
else if you don't have that, and if instead you have a message like message command not found, then

197
00:15:09,020 --> 00:15:13,430
it means you won't be able to use his message in the Windows Terminal.

198
00:15:13,640 --> 00:15:19,820
So in that case, in that very specific case on windows, you will need to install another software

199
00:15:19,820 --> 00:15:22,940
to use this page and you can, for example, use.

200
00:15:22,940 --> 00:15:29,510
But you know, you can go on putting on and you can simply download it, install the software and then

201
00:15:29,750 --> 00:15:30,260
started.

202
00:15:30,560 --> 00:15:33,320
So pretty is an SSA client.

203
00:15:33,530 --> 00:15:38,330
You can use it the same way we are going to use these command line here.

204
00:15:38,450 --> 00:15:44,630
This will just make you use a good tool, so you would have to fill up the IP address, the username

205
00:15:44,630 --> 00:15:46,850
and password as we are going to do here.

206
00:15:47,690 --> 00:15:53,660
So coming back to the terminal, which you can do to get access to your raspberry bank is to type a

207
00:15:53,670 --> 00:15:58,840
space age and in space, and then you need to provide the user name.

208
00:15:58,850 --> 00:16:01,060
So what is the username fault?

209
00:16:01,760 --> 00:16:03,370
Raspberry Pi for your Raspberry Pi?

210
00:16:03,380 --> 00:16:11,540
Well, the default username that is already here when you flush the OS into the card is named simply

211
00:16:11,540 --> 00:16:11,990
by.

212
00:16:12,110 --> 00:16:12,440
OK.

213
00:16:13,010 --> 00:16:20,120
So there is no way for you to discover that it's simply the default one that I'm giving it to you.

214
00:16:20,480 --> 00:16:23,450
Here you can also find it on the Raspberry Pi website.

215
00:16:24,440 --> 00:16:28,040
So we are going to be connected as the user named Byte.

216
00:16:28,430 --> 00:16:35,330
Then you can put it and the IP address that you found here with your IP scanner software.

217
00:16:35,840 --> 00:16:44,870
So for me, it would be 192, that 168, the 43 Dot 56.

218
00:16:45,170 --> 00:16:47,990
So of course, that would be different for you.

219
00:16:48,050 --> 00:16:48,380
OK.

220
00:16:48,800 --> 00:16:54,720
So just use the IP address you found there and then you can simply price enter.

221
00:16:55,340 --> 00:16:55,640
OK.

222
00:16:56,180 --> 00:16:59,390
For the very first connection, you will have that message.

223
00:16:59,420 --> 00:17:01,970
Are you sure you want to continue connecting?

224
00:17:02,210 --> 00:17:09,320
Because actually the host here your machine doesn't know has not been connected to your Raspberry Pi

225
00:17:09,320 --> 00:17:10,880
before, so you can just price.

226
00:17:11,090 --> 00:17:11,750
Yes.

227
00:17:11,930 --> 00:17:12,230
OK.

228
00:17:12,650 --> 00:17:15,810
And now it's asking you for the password.

229
00:17:15,830 --> 00:17:20,180
OK, so we have the user pi and we need to give the password.

230
00:17:20,540 --> 00:17:21,610
So what is the password?

231
00:17:21,950 --> 00:17:23,930
The password is simply raspberry.

232
00:17:24,080 --> 00:17:24,830
OK, like that?

233
00:17:25,160 --> 00:17:26,660
No uppercase, no space.

234
00:17:26,660 --> 00:17:27,740
No nothing.

235
00:17:28,100 --> 00:17:29,870
Just a raspberry like that.

236
00:17:29,870 --> 00:17:33,650
So you can go ahead and type raspberry.

237
00:17:35,390 --> 00:17:37,200
You will not see anything.

238
00:17:37,230 --> 00:17:37,530
OK?

239
00:17:37,550 --> 00:17:43,640
As you can see, when I typed, you will not see anything written on the screen and then you press enter.

240
00:17:47,000 --> 00:17:52,670
And if it works, if you've provided the correct password, then you're in.

241
00:17:53,120 --> 00:18:01,730
You can see here you have the pipe user and then the host name is Raspberry Pi and you are connected

242
00:18:01,730 --> 00:18:04,370
to the Raspberry Pi for the first time.

243
00:18:04,550 --> 00:18:05,000
Great.

244
00:18:11,500 --> 00:18:14,320
Let us know, install and configure the ANC.

245
00:18:14,800 --> 00:18:20,170
The ANC will simply allow you to use the Raspberry Pi desktop from your own computer.

246
00:18:20,350 --> 00:18:23,260
This is great, so you don't need to only use the terminal.

247
00:18:23,270 --> 00:18:24,450
We've come online, Zain.

248
00:18:24,700 --> 00:18:31,750
You also don't need to have a monitor plugged to your Raspberry Pi, and even if you have a monitor,

249
00:18:31,990 --> 00:18:36,280
you will see that it's sometimes more convenient to work with it.

250
00:18:36,790 --> 00:18:44,890
So the reason why we set up SSA just before is simply because we need to access the Raspberry Pi through

251
00:18:44,890 --> 00:18:48,520
S.H. so we can actually set up the ANC.

252
00:18:48,790 --> 00:18:50,200
So that's what we are going to do.

253
00:18:50,570 --> 00:18:58,570
Q So H, then you put the user name, which is buy here at an IP address.

254
00:18:58,720 --> 00:19:01,540
So of course, this will be different for you.

255
00:19:04,050 --> 00:19:08,570
Take centre and the buzz word is still a raspberry.

256
00:19:09,290 --> 00:19:15,750
OK, don't worry about the warning message here, the password, we are just going to change the bus

257
00:19:15,750 --> 00:19:16,650
will later.

258
00:19:18,200 --> 00:19:24,380
So here, to enable the ANC and make it work correctly, there are a few different steps that we need

259
00:19:24,380 --> 00:19:27,020
to do in the order, so please follow along.

260
00:19:27,290 --> 00:19:31,610
First, you are going to type, so here you are in a terminal inside the rosemary bank.

261
00:19:31,880 --> 00:19:34,460
You are going to type pseudo space.

262
00:19:35,000 --> 00:19:37,860
Raspy dash config, OK?

263
00:19:37,880 --> 00:19:44,030
And if you see that, for example, if a price tag here, I can have the auto completion to make sure

264
00:19:44,030 --> 00:19:45,500
it is the right command.

265
00:19:45,890 --> 00:19:52,430
So Sudo will make you run the command as an administrator on the mission, which is required here.

266
00:19:52,760 --> 00:19:58,340
And there must be configured interests so you can get access to a configuration so you press, enter

267
00:19:59,210 --> 00:20:05,600
and it will bring you to that menu here so you can navigate using the arrows OK from your keyboard.

268
00:20:05,900 --> 00:20:06,740
This is very simple.

269
00:20:06,950 --> 00:20:09,980
And then just press enter to choose whatever you want.

270
00:20:10,520 --> 00:20:14,870
And the first thing we are going to do is go to interface options.

271
00:20:15,260 --> 00:20:19,070
OK, press enter and then go to the ANC.

272
00:20:19,370 --> 00:20:20,450
Press enter again.

273
00:20:21,050 --> 00:20:23,570
And would you like to be an C-7 to be enabled?

274
00:20:23,570 --> 00:20:30,140
You are going to select Yes, press enter and you can see the V.A. server is enabled.

275
00:20:30,890 --> 00:20:37,520
So I'm going to use the right, the wrong get to go to select and then finish and then press enter on

276
00:20:37,520 --> 00:20:37,940
finish.

277
00:20:38,330 --> 00:20:43,610
And I am going to reboot the Raspberry Pi with the command sudo route.

278
00:20:44,000 --> 00:20:47,810
So you do see the reboot enter and you can see now.

279
00:20:48,440 --> 00:20:53,200
So the Raspberry Pi is rebooting and we are back to where we were before.

280
00:20:53,210 --> 00:20:55,180
So here I'm back on Windows, OK?

281
00:20:55,610 --> 00:20:59,990
I lost the connection to the Raspberry Pi because of course it's rebooting.

282
00:21:00,320 --> 00:21:07,190
So now you have to wait a few seconds until the Raspberry Pi has boots again and is connected to the

283
00:21:07,220 --> 00:21:08,330
Wi-Fi network.

284
00:21:08,750 --> 00:21:14,600
OK, I'm going to use the same command as before and wait a bit and then press enter.

285
00:21:15,800 --> 00:21:20,270
And you can see when you have the bust world, it means that the Raspberry Pi has correctly earned.

286
00:21:21,470 --> 00:21:26,870
So you just put the password raspberry once more and you are back to a space age, OK?

287
00:21:26,930 --> 00:21:28,880
On the Raspberry Pi would debate.

288
00:21:28,880 --> 00:21:29,330
Use it.

289
00:21:29,840 --> 00:21:33,310
And now you're going to go back to recipe config.

290
00:21:33,700 --> 00:21:35,030
We see the recipe complete.

291
00:21:35,540 --> 00:21:41,060
And so he and the DNC server is enabled, but that's not going to just work like that.

292
00:21:41,360 --> 00:21:42,350
So you need to go.

293
00:21:42,380 --> 00:21:44,620
Here we are in one swing rice.

294
00:21:44,630 --> 00:21:48,310
Enter OK and go to boot.

295
00:21:48,530 --> 00:21:49,250
Auto logging.

296
00:21:50,710 --> 00:21:57,400
And I'm going to choose so by default, that may be one of those cons. But you're going to choose desktop

297
00:21:57,730 --> 00:21:59,480
or desktop ontology.

298
00:21:59,530 --> 00:22:05,590
OK, so it means that it's going to boot on the desktop and you've used auto logging is going to put

299
00:22:05,590 --> 00:22:09,730
on a desktop and it's not going to ask you for the password to boot.

300
00:22:10,450 --> 00:22:14,650
I'm going to use that because it's just simpler like press enter.

301
00:22:16,290 --> 00:22:20,820
OK, and then what I can do is I can just go to finish again.

302
00:22:21,180 --> 00:22:26,190
Would you like to reboot now, OK, they ask you that because you have changed notion that needs their

303
00:22:26,190 --> 00:22:26,550
roots.

304
00:22:26,820 --> 00:22:28,110
So do you like to it now?

305
00:22:28,140 --> 00:22:29,000
Yes, you press.

306
00:22:29,010 --> 00:22:30,270
Yes, and he's going to reboot.

307
00:22:30,610 --> 00:22:30,870
Oh yeah.

308
00:22:31,650 --> 00:22:37,770
Yes, I'm going to make the steps one by one key and everything so that you can't see each step.

309
00:22:38,460 --> 00:22:38,820
OK.

310
00:22:38,910 --> 00:22:39,870
One by one.

311
00:22:39,880 --> 00:22:43,410
So now you have to wait a bit until the Raspberry Pi has.

312
00:22:45,200 --> 00:22:47,390
So I put the password, the raspberry again.

313
00:22:49,960 --> 00:22:57,190
OK, and I'm going back to raspy coughing and the last step we are going to go on display options,

314
00:22:57,550 --> 00:22:59,500
OK and resolution.

315
00:23:00,370 --> 00:23:05,830
OK, and you're going to choose a different screen resolution than the default work because for some

316
00:23:05,830 --> 00:23:12,760
reasons, if you have the default resolution, the Vinci saver may not walk, so you have to choose

317
00:23:12,760 --> 00:23:15,080
a different resolution here.

318
00:23:15,310 --> 00:23:16,630
And which one to choose?

319
00:23:16,810 --> 00:23:20,590
Well, basically choose the one that corresponds to your current screen.

320
00:23:21,310 --> 00:23:28,450
So on my laptop here, I have a full HD resolution on the screen, so I'm going to choose the full HD

321
00:23:28,450 --> 00:23:29,110
resolution.

322
00:23:29,410 --> 00:23:35,530
OK, so you press enter on the resolution you want, OK, the resolution is set down or not.

323
00:23:35,560 --> 00:23:38,080
OK, and then go back to finish.

324
00:23:38,410 --> 00:23:39,670
Would you like to reboot now?

325
00:23:39,670 --> 00:23:42,040
And yes, and you're about one more time.

326
00:23:43,300 --> 00:23:50,080
OK, so those are the three steps we need to do so we can enable the ANC and make it work.

327
00:23:50,710 --> 00:23:55,360
So now we have set up the ANC on the Raspberry Pi, so this is the central site.

328
00:23:55,600 --> 00:23:58,450
What we need to do now is to get the count.

329
00:23:58,600 --> 00:24:00,550
So here I'm using windows.

330
00:24:00,790 --> 00:24:06,820
I need to get a client so I can actually connect to the Raspberry Pi and get access to the desktop and

331
00:24:06,820 --> 00:24:07,390
to do that.

332
00:24:08,610 --> 00:24:15,070
We are going to actually install the real DNC, DNC, if you will.

333
00:24:15,240 --> 00:24:23,010
OK, so you can go to that you are here real DNC dot com, you can simply also dive into your real DNC

334
00:24:23,010 --> 00:24:25,050
and it's basically the first link.

335
00:24:26,400 --> 00:24:31,950
And as you can see, it is is multi-platform, so you can choose whatever awaits you using the right.

336
00:24:31,960 --> 00:24:34,410
No Windows, macOS and Linux.

337
00:24:35,280 --> 00:24:39,180
As you can see, there is the Raspberry Pi here, but don't mix things up, OK?

338
00:24:39,570 --> 00:24:43,820
If you choose this, this is the client to connect to the Raspberry Pi.

339
00:24:43,840 --> 00:24:50,850
So if you choose this, basically it means that you are controlling the Raspberry Pi from another Raspberry

340
00:24:50,850 --> 00:24:51,060
Pi.

341
00:24:51,090 --> 00:24:58,170
OK, here we are controlling Raspberry Pi from Windows here because my laptop is running windows at

342
00:24:58,170 --> 00:25:03,240
the moment, so I'm going to choose the Windows client and simply download it.

343
00:25:05,220 --> 00:25:06,400
OK, David.

344
00:25:06,420 --> 00:25:15,360
And when it is done, you can or is done it before, so you can just run it and go through the installation

345
00:25:15,360 --> 00:25:21,330
setup, and once it is installed, you simply have to launch the application.

346
00:25:21,730 --> 00:25:23,340
OK, and you will get that.

347
00:25:23,500 --> 00:25:25,380
You hear so.

348
00:25:26,930 --> 00:25:28,430
What are we going to do now?

349
00:25:28,730 --> 00:25:33,890
First, make sure that your Raspberry Pi has been revoked, so it is powered on, it is running.

350
00:25:34,520 --> 00:25:39,410
And also make sure that I'm going back to my network configuration.

351
00:25:40,160 --> 00:25:46,250
You should have the correct configuration because you could just previously connect to Assange, but

352
00:25:46,250 --> 00:25:51,100
make sure you always have your computer and your Raspberry Pi on the same network.

353
00:25:51,110 --> 00:25:55,370
Otherwise, you won't be able to connect to your Raspberry Pi from your laptop.

354
00:25:56,150 --> 00:26:03,180
So, no, I'm going to go here to find a new connection, or you can just press control and issue.

355
00:26:04,750 --> 00:26:09,550
And Kyung, I'm going to put the IP address of near Rosemary by.

356
00:26:12,830 --> 00:26:16,730
OK, so, Mary, make sure that you know that somewhere, so you don't forget it.

357
00:26:17,360 --> 00:26:23,300
And I'm giving names to just the name so we can recognize the connection here.

358
00:26:23,510 --> 00:26:25,640
Just Raspberry Pi.

359
00:26:26,450 --> 00:26:28,220
You can put whatever name you want here.

360
00:26:28,400 --> 00:26:28,700
OK.

361
00:26:29,480 --> 00:26:34,880
And let's click on OK, and I'm going to double click on that.

362
00:26:36,740 --> 00:26:40,930
OK, you may have a warning like that, and let's don't worry about that.

363
00:26:41,210 --> 00:26:41,930
We can continue.

364
00:26:41,930 --> 00:26:43,820
If you don't have the warning, it's fine too.

365
00:26:44,450 --> 00:26:47,570
And no, you have to give the username and password.

366
00:26:47,990 --> 00:26:53,110
So the username here is fine and the password is raspberry.

367
00:26:53,600 --> 00:26:57,590
OK, just like we did, for instance, OK?

368
00:26:58,100 --> 00:27:00,440
You can choose to remember the password or not.

369
00:27:00,530 --> 00:27:03,590
I'm not going to do that now because we are going to change password later.

370
00:27:06,630 --> 00:27:07,020
OK.

371
00:27:07,560 --> 00:27:12,320
You can now have access to your Raspberry Pi desktop without any external money on.

372
00:27:17,780 --> 00:27:24,290
So first, OK, you may have that warning, a system is enabled in the default password, followed by

373
00:27:24,290 --> 00:27:26,930
user has not be changed, so you only get that.

374
00:27:27,320 --> 00:27:35,450
Of course, if you have previously said this is age like we did, just click on OK and you have the

375
00:27:35,450 --> 00:27:38,780
welcome screen to set everything up.

376
00:27:39,050 --> 00:27:41,930
So I'm just going to get you through the different steps here.

377
00:27:42,470 --> 00:27:43,190
Click on Next.

378
00:27:43,760 --> 00:27:50,120
So you choose your country and for example, for me, it is.

379
00:27:54,880 --> 00:28:03,070
Friends, OK, choose a language, I'm going to use the English language so you can just associate your

380
00:28:03,070 --> 00:28:03,610
keyboard.

381
00:28:04,270 --> 00:28:06,850
Anything that is related to your country.

382
00:28:07,570 --> 00:28:08,260
OK, next.

383
00:28:13,330 --> 00:28:18,850
OK, and Hugh, they will ask you to enter a new password, so we could have done that before, but

384
00:28:19,120 --> 00:28:21,880
because we have this option to do that here.

385
00:28:22,290 --> 00:28:25,510
I didn't do it before, so we can just change the password now.

386
00:28:25,810 --> 00:28:33,890
So simply simply choose the password that you want and that will become the new password for the by

387
00:28:33,910 --> 00:28:34,220
user.

388
00:28:34,240 --> 00:28:36,620
OK, so your user is still named by.

389
00:28:37,100 --> 00:28:40,600
OK, but then the password will not be raspberry anymore.

390
00:28:40,630 --> 00:28:43,810
The password will be the password that you set here.

391
00:28:44,050 --> 00:28:44,280
OK.

392
00:28:44,470 --> 00:28:47,170
So make sure that you remember the password after you said it here.

393
00:28:47,740 --> 00:28:48,760
Then you click on next.

394
00:28:50,760 --> 00:28:56,490
If you OK, if the screen shows a black border around this dog, you can click on that.

395
00:28:56,730 --> 00:29:01,250
For me, in my situation, I don't have the black models.

396
00:29:01,260 --> 00:29:08,280
I'm just going to click on next and then they will search for wireless network.

397
00:29:09,000 --> 00:29:13,770
So if it is the first time you boot your Raspberry Pi with an external monitor, of course, here you

398
00:29:13,830 --> 00:29:19,650
have to choose which network you want to connect to and set up to provide the password.

399
00:29:20,320 --> 00:29:26,040
Here, I'm not going to do that because I'm already connected to that network because that's what we

400
00:29:26,040 --> 00:29:32,820
previously did in one another step and going to click on Skip here, but you can.

401
00:29:33,840 --> 00:29:39,300
Because next, if you're not connected and a data software, you can click next.

402
00:29:40,310 --> 00:29:41,940
OK, it will check for updates.

403
00:29:43,770 --> 00:29:52,230
So after fetching the new update, it will download the new packages so we can install the packages

404
00:29:52,650 --> 00:29:56,610
may take some time here, depending on your internet connection speed.

405
00:29:59,600 --> 00:30:06,470
And after all, the debates have been downloaded, download the Raspberry Pi, we install those updates.

406
00:30:07,880 --> 00:30:15,020
But here again, you have to wait a few minutes, OK, and finally, you will get this message system

407
00:30:15,020 --> 00:30:24,830
is up to date, so you click on OK and now the setup is complete so you can actually press restart.

408
00:30:30,050 --> 00:30:35,630
And as you can see, when a press restart here, because I'm using Vinci, I get a message attempting

409
00:30:35,630 --> 00:30:41,090
to reconnect to the ever again because of course, the Raspberry Pi know is shutting down.

410
00:30:41,420 --> 00:30:45,500
So the V.A. clients can't connect to the V.A. Center.

411
00:30:45,860 --> 00:30:46,940
So what are you going to do here?

412
00:30:47,020 --> 00:30:48,450
Just need to wait.

413
00:30:48,470 --> 00:30:54,410
OK, if the Raspberry Pi is disconnected, the client, the agency client will continue to try to connect

414
00:30:54,410 --> 00:30:56,270
to the Raspberry Pi.

415
00:30:56,510 --> 00:31:03,680
And when the Raspberry Pi will boot again, it will enable deviancy server and the client would be able

416
00:31:03,680 --> 00:31:04,190
to connect.

417
00:31:06,800 --> 00:31:13,190
And here, as you can see, we have a message, either the user name was not recognized, all the password

418
00:31:13,190 --> 00:31:18,770
was incorrect and you get this in the first time because the password actually you have changed the

419
00:31:18,770 --> 00:31:19,100
passport.

420
00:31:19,130 --> 00:31:21,350
OK, the password is not raspberry anymore.

421
00:31:21,350 --> 00:31:23,480
The password is the new password that you have set.

422
00:31:23,480 --> 00:31:31,610
So you click on OK and you can now double click on the link again and you can put your new password.

423
00:31:33,550 --> 00:31:38,710
OK, and then you can actually click on remember password icon, OK?

424
00:31:39,040 --> 00:31:42,760
And it will connect again as the user.

425
00:31:43,300 --> 00:31:43,630
Right?

426
00:31:44,140 --> 00:31:52,240
OK, so now if I click here, I close it, I can connect again, and it will not ask for the password.

427
00:31:52,840 --> 00:32:00,940
And one thing that you may experience is, OK, if I tried to put fullscreen, as you can see, it doesn't

428
00:32:01,390 --> 00:32:01,810
really.

429
00:32:03,090 --> 00:32:04,670
Work, OK.

430
00:32:07,780 --> 00:32:12,490
It's not good, as you can see, that the resolution is not really.

431
00:32:13,590 --> 00:32:14,790
But they did correctly.

432
00:32:14,880 --> 00:32:15,210
OK.

433
00:32:15,690 --> 00:32:21,330
It's either too big or not fitting the screen, so to fix that simply for what I'm doing here.

434
00:32:21,600 --> 00:32:26,100
You can click here to open eight a.m. so you can use the command.

435
00:32:27,450 --> 00:32:27,750
Do.

436
00:32:29,530 --> 00:32:34,630
And then Nano Nano, which is a text editor and then slash.

437
00:32:36,200 --> 00:32:39,380
But slash config that.

438
00:32:41,030 --> 00:32:48,050
OK, so you can just type this exact command in this will open the file and then configured the city,

439
00:32:48,150 --> 00:32:53,450
which is located in slush mode, so slashes the roots of the fight system.

440
00:32:53,810 --> 00:32:55,550
So this is where the file is located.

441
00:32:57,760 --> 00:32:58,090
OK.

442
00:32:58,300 --> 00:33:05,380
And what you can do is use the arrows from the keyboard to navigate in the final so you can use the

443
00:33:05,380 --> 00:33:10,450
don't arrow to go down until the end of the fight.

444
00:33:10,600 --> 00:33:10,930
OK?

445
00:33:11,260 --> 00:33:16,060
At the end of the file, you will see that like obviously this before, et cetera, et cetera.

446
00:33:16,360 --> 00:33:18,990
What you can do is add a hashtag before.

447
00:33:19,000 --> 00:33:22,450
See, this will simply command the line.

448
00:33:23,660 --> 00:33:23,930
OK.

449
00:33:24,110 --> 00:33:28,310
And you can price control, as you will see.

450
00:33:28,580 --> 00:33:34,880
Let me say to you, control this will save the fight and then control it will exit the fight.

451
00:33:35,390 --> 00:33:37,250
So know that we have changed that.

452
00:33:37,250 --> 00:33:42,350
As you can see, it's in boot directories, or you can guess that it will apply on boot.

453
00:33:42,680 --> 00:33:49,370
So you can reboot your Raspberry Pi so you have two choices you can do a pseudo reboot like we did before

454
00:33:49,490 --> 00:33:50,380
with each.

455
00:33:50,660 --> 00:33:58,550
And you can also go here and click on Look Out and should not just like you would should don't any computer.

456
00:33:59,360 --> 00:34:03,440
OK, so if you want to actually run, would you have to pick on route?

457
00:34:03,730 --> 00:34:05,720
Here I have clicked on shut down.

458
00:34:05,960 --> 00:34:11,300
So what it will do is simply shut down the Raspberry Pi and so you have to wait a few seconds.

459
00:34:11,540 --> 00:34:13,720
Let's say that when you shut down the Raspberry Pi, like this?

460
00:34:14,060 --> 00:34:18,710
Wait, something like 10 to 20 seconds after night.

461
00:34:18,980 --> 00:34:25,700
What you do is you take off the power cable from your Raspberry Pi, OK, and then you put the power

462
00:34:25,700 --> 00:34:29,030
cable back in the Raspberry Pi, so it will boot again.

463
00:34:29,090 --> 00:34:29,420
OK.

464
00:34:30,720 --> 00:34:33,800
For now, this is the only solution you have to boot.

465
00:34:33,900 --> 00:34:35,450
Raspberry Pi it is.

466
00:34:35,450 --> 00:34:40,490
When its shutdown is, you take off the power cable and you put it back in sight.

467
00:34:41,270 --> 00:34:43,460
So the pie is no rebooting.

468
00:34:43,910 --> 00:34:48,110
You can wait again a few seconds, so maybe up to one minute.

469
00:34:54,320 --> 00:35:02,630
OK, and now the Vinci client has connected again to the Raspberry Pi, and no, it's much better.

470
00:35:02,660 --> 00:35:10,520
OK, so you can go here and click on into full screen mode, OK, and know you have your Raspberry Pi

471
00:35:10,550 --> 00:35:14,570
flat screen with the same resolution as your monitor.

472
00:35:15,200 --> 00:35:17,790
And you can click here to exit full screen.

473
00:35:17,810 --> 00:35:19,970
OK, so great.

474
00:35:20,090 --> 00:35:21,680
You have set up everything.

475
00:35:21,980 --> 00:35:28,490
And one last very important thing is actually when you want to shut down and pull off the Raspberry

476
00:35:28,490 --> 00:35:35,510
Pi, don't just take off your cable when it's running because you just don't unplug your computer when

477
00:35:35,510 --> 00:35:35,920
it's running.

478
00:35:35,930 --> 00:35:42,650
OK, first, which you do is you go here, you shut down your computer, and then when it's completely

479
00:35:42,650 --> 00:35:44,450
shut down, you can remove the power cable.

480
00:35:44,480 --> 00:35:44,780
OK.

481
00:35:45,080 --> 00:35:48,680
So if you don't do that, you may correct the SD card.

482
00:35:48,680 --> 00:35:51,860
And when you boot again, you might have an error.

483
00:35:52,100 --> 00:35:56,420
And in that case, you would have to completely reinstall your Raspberry Pi.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,210 --> 00:00:06,240
In this lesson, I will show you how to install the Arduino I.D. on the Raspberry Pi so you can program

2
00:00:06,240 --> 00:00:07,980
your Arduino directly from there.

3
00:00:08,130 --> 00:00:13,350
And let's first understand very quickly why this can save you a lot of pain.

4
00:00:14,010 --> 00:00:20,010
So if you already have the original I.D. on your computer, what you can do is to write some programs

5
00:00:20,010 --> 00:00:20,930
for your Arduino.

6
00:00:20,940 --> 00:00:23,430
Let's say you are on Windows, Mac or Linux.

7
00:00:23,430 --> 00:00:24,510
It doesn't really matter.

8
00:00:24,810 --> 00:00:27,630
And then you upload the program to the Arduino.

9
00:00:28,110 --> 00:00:33,870
Then when we will make the Raspberry Pi and Arduino communicate between each other, you will need to

10
00:00:33,870 --> 00:00:41,010
unplug Arduino from your computer, plug it to your Raspberry Pi and then run a Python program to communicate

11
00:00:41,310 --> 00:00:42,780
on the Raspberry Pi.

12
00:00:43,320 --> 00:00:49,530
And every time you need to modify something in the Arduino code, you will need to do this process again,

13
00:00:49,740 --> 00:00:57,540
which is basically to unplug from debate plug to the computer, upload, unplug and plug to the Raspberry

14
00:00:57,540 --> 00:00:58,260
Pi again.

15
00:00:58,950 --> 00:01:04,090
Now what you can do is directly install the Arduino ID on the Raspberry Pi OS.

16
00:01:04,410 --> 00:01:10,080
By doing that, you can keep the original board plugged to your Raspberry Pi book any time you need

17
00:01:10,080 --> 00:01:12,060
to modify the original program.

18
00:01:12,270 --> 00:01:18,000
You simply need to stop any current program running on the rise of Bay, which is communicating with

19
00:01:18,000 --> 00:01:22,890
the Arduino, and then you just upload the code and run the program again.

20
00:01:23,100 --> 00:01:23,700
That's it.

21
00:01:24,150 --> 00:01:24,570
All right.

22
00:01:24,600 --> 00:01:30,000
Now let's go to the Raspberry Pi OS desktop and install the Arduino IEEE.

23
00:01:31,370 --> 00:01:36,620
So Raspberry Pi desktop is actually Linux, so we are going to do the Linux installation.

24
00:01:37,070 --> 00:01:44,340
And if you open a terminal where you could install Arduino directly, we AAPT, but don't do that.

25
00:01:44,360 --> 00:01:44,660
OK.

26
00:01:44,870 --> 00:01:47,920
So you could do sudo apt get install Arduino.

27
00:01:47,930 --> 00:01:53,570
You may see that in some tutorials, but don't do that because this version is actually old and not

28
00:01:53,810 --> 00:01:54,380
dated.

29
00:01:54,860 --> 00:01:58,760
So you're not going to have the new features, and maybe that's not going to work.

30
00:01:59,270 --> 00:02:03,500
So instead, we are going to open a web browser here on the Raspberry Pi.

31
00:02:04,550 --> 00:02:07,640
And just type of, you know, I.

32
00:02:09,800 --> 00:02:15,110
So just search on to go on Google on whatever search online you want.

33
00:02:15,590 --> 00:02:17,990
Let's go to the original web site.

34
00:02:19,310 --> 00:02:25,130
And here we are, not on the right page, so let's go to software, so you click on software.

35
00:02:26,930 --> 00:02:28,700
And you have downloads, OK?

36
00:02:28,730 --> 00:02:29,390
How do you know?

37
00:02:29,960 --> 00:02:36,680
So just download the latest version of it doesn't really matter which Russian you have or not.

38
00:02:37,070 --> 00:02:39,590
So on the right, you can see the download options.

39
00:02:39,660 --> 00:02:46,160
OK, so if you were to use windows on microwaves instead of the Raspberry Pi to actually program you,

40
00:02:46,200 --> 00:02:48,080
Arenal, then download one of those.

41
00:02:48,320 --> 00:02:49,870
But here we are on Linux.

42
00:02:49,910 --> 00:02:52,220
OK, we on Raspberry Pi, so we are on links.

43
00:02:52,220 --> 00:02:59,360
So we are going to download one of those here of Linux and to know if you have 32 of 64 bits.

44
00:02:59,600 --> 00:03:01,280
Well, it's simple.

45
00:03:01,280 --> 00:03:07,250
Just open the terminal again and the you name Space Dash.

46
00:03:08,990 --> 00:03:10,810
This is going to show you that.

47
00:03:10,820 --> 00:03:16,160
And if you see a L m v seven L, it means you have a 32 bit.

48
00:03:16,700 --> 00:03:21,530
If you have something like x eighty six 64, you have 64 bit.

49
00:03:21,890 --> 00:03:23,900
So we know we have 32 bit here.

50
00:03:25,890 --> 00:03:31,980
And we are going to use that and M32, so you don't know that one.

51
00:03:33,490 --> 00:03:35,980
OK, you can just click on Just Download.

52
00:03:38,650 --> 00:03:41,080
And you can see it's going to download downloaded here.

53
00:03:41,410 --> 00:03:44,710
So you just wait until it has been downloaded.

54
00:03:45,430 --> 00:03:45,730
Yeah.

55
00:03:46,240 --> 00:03:46,650
All right.

56
00:03:46,660 --> 00:03:56,110
We now have the Arduino I downloaded, so I'm going to close this web browser and let's open the terminal

57
00:03:56,110 --> 00:03:56,560
again.

58
00:03:57,100 --> 00:03:57,460
All right.

59
00:03:57,500 --> 00:04:02,200
And as a reminder, here you have to have some basics on the Raspberry Pi, including the terminal.

60
00:04:02,200 --> 00:04:08,380
So I'm going to show you exactly what commands I use, but I'm not going to explain everything 100 percent

61
00:04:08,560 --> 00:04:09,490
from scratch.

62
00:04:09,940 --> 00:04:11,750
So we are in the home directorate.

63
00:04:11,770 --> 00:04:20,160
I'm going to go to the Downloads folder in the Downloads folder, we have this, so that's OK.

64
00:04:20,170 --> 00:04:22,450
We have downloaded from the Arduino website.

65
00:04:23,050 --> 00:04:23,890
This is it.

66
00:04:24,670 --> 00:04:33,760
OK, so we are going to do the space Dash X if we have the name of the OK?

67
00:04:34,860 --> 00:04:39,000
So you can just use the at the completion with Typekit if you want to go faster.

68
00:04:39,540 --> 00:04:44,220
You press enter, you wait a few seconds, maybe even a few minutes.

69
00:04:45,800 --> 00:04:46,220
All right.

70
00:04:46,370 --> 00:04:53,600
And when the comment returns, and as you see, we have a new folder which contains the Arduino I.D.

71
00:04:53,960 --> 00:05:00,550
know what you are going to do is to move this inside the slush or folder of your Raspberry Pi.

72
00:05:00,890 --> 00:05:06,890
So you're going to do pseudo pseudo because we are going to put that somewhere else than in your home

73
00:05:06,890 --> 00:05:07,460
directory.

74
00:05:08,120 --> 00:05:16,160
So Sudo M. V. To move, you just use the data compilation to select the folder and then you do slash

75
00:05:17,000 --> 00:05:17,370
of it.

76
00:05:18,560 --> 00:05:21,560
We've got the completion or so you press enter.

77
00:05:22,430 --> 00:05:22,740
All right.

78
00:05:22,760 --> 00:05:23,930
Now the folder is gone.

79
00:05:23,960 --> 00:05:25,100
You go to Sydney.

80
00:05:25,310 --> 00:05:29,000
So city slash property Dennis, we have.

81
00:05:29,000 --> 00:05:32,600
So we have other stuff here as well, and we have the Arduino.

82
00:05:32,870 --> 00:05:39,950
And so we are going to go inside this own folder and know you can see we have this.

83
00:05:40,010 --> 00:05:43,850
We have a few script here and some folders.

84
00:05:44,240 --> 00:05:53,900
But basically what we're going to do is to run this install each so pseudo docs forward slash, install

85
00:05:54,440 --> 00:05:56,920
each and you wait a few seconds.

86
00:05:59,730 --> 00:05:59,960
OK.

87
00:06:00,030 --> 00:06:01,240
And when you sit down.

88
00:06:01,260 --> 00:06:04,710
Well, I don't know, it is successfully installed.

89
00:06:05,160 --> 00:06:11,700
Just one more thing is if you want to uninstall it, you just go back to this folder here and you just

90
00:06:11,700 --> 00:06:16,980
run an installed script and then you can also remove that folder if you want to.

91
00:06:17,430 --> 00:06:17,790
All right.

92
00:06:18,060 --> 00:06:19,980
But let's keep out Android installed.

93
00:06:20,280 --> 00:06:27,600
I'm going to close the terminal now, and you can see here we should have under menu programming and

94
00:06:27,600 --> 00:06:30,360
we have a new Arduino icon here.

95
00:06:30,510 --> 00:06:31,740
So I'm going to click on that.

96
00:06:33,980 --> 00:06:34,340
OK.

97
00:06:34,400 --> 00:06:39,620
And out in the open and you see you have a new program here.

98
00:06:40,580 --> 00:06:47,730
And no, just one or two things about configuration, OK, so that you can have a better looking I.D.

99
00:06:48,020 --> 00:06:50,020
and that the code can be more reliable.

100
00:06:50,540 --> 00:06:53,330
You're going to go in fine preferences.

101
00:06:54,840 --> 00:06:59,010
And you can edit here different things, for example, edit font size.

102
00:06:59,430 --> 00:07:06,900
I'm going to put 14 here, I'm going also to use display line numbers because I'm going to change those

103
00:07:06,900 --> 00:07:07,890
two options here.

104
00:07:08,730 --> 00:07:12,360
Let's click on OK, and you can see it's already better.

105
00:07:12,780 --> 00:07:17,520
I'm going to go back to preclearance is where you already have another information.

106
00:07:17,520 --> 00:07:20,400
Here is where your sketchbook is.

107
00:07:20,400 --> 00:07:24,270
So Sketchbook is basically where, you know, programs are going to be saved.

108
00:07:24,630 --> 00:07:31,260
So you have a new Arduino folder here on your home directory.

109
00:07:32,810 --> 00:07:39,380
And the last thing I'm going to do is I'm going to go down here, more preferences can be edited directly

110
00:07:39,380 --> 00:07:42,320
in the fight here, so I'm going to click on that.

111
00:07:42,740 --> 00:07:47,900
This is going to open a new file manager and I'm going to close.

112
00:07:47,900 --> 00:07:48,890
That's very important.

113
00:07:48,920 --> 00:07:51,380
You going to close it?

114
00:07:51,950 --> 00:07:55,430
OK, we are going to modify preferences here.

115
00:07:55,970 --> 00:07:58,630
And before you open that file, you closed the.

116
00:08:00,050 --> 00:08:00,920
Very important.

117
00:08:01,100 --> 00:08:02,420
So you don't click.

118
00:08:03,400 --> 00:08:07,840
It's going to open the file, and this is because we're going to find this line.

119
00:08:08,100 --> 00:08:10,340
OK, ed, not front.

120
00:08:10,480 --> 00:08:13,420
OK, so you can just crawl and find this line.

121
00:08:14,270 --> 00:08:15,280
Any thought out front?

122
00:08:15,790 --> 00:08:22,450
You see, we have A. Beast by default, and this may actually not be the most readable front for us.

123
00:08:23,080 --> 00:08:29,110
So what you can do if you want to change to console us here like this, you're right.

124
00:08:29,110 --> 00:08:29,560
Like this?

125
00:08:29,560 --> 00:08:33,820
Console us and then you have planes that don't touch anything here anyway.

126
00:08:33,830 --> 00:08:35,680
Don't sitting doesn't work.

127
00:08:35,890 --> 00:08:39,220
And then you see, you also have the font size that we have just said before.

128
00:08:39,580 --> 00:08:44,800
But for the font, basically, there is no way to change it under Arduino settings, so we have to open.

129
00:08:44,800 --> 00:08:47,750
This preference is not to activate.

130
00:08:48,100 --> 00:08:57,100
So I'm going to say we have control as in no, I quit the file and quit that and let's go back to undo

131
00:08:57,100 --> 00:08:57,720
no I.D..

132
00:09:00,040 --> 00:09:03,640
All right, now, we have a new font size.

133
00:09:04,850 --> 00:09:10,220
And a new font, and we have the line numbers, so everything is good for the goose.

134
00:09:10,760 --> 00:09:19,070
Now if you plug your Arduino to your Raspberry Pi with the USB cable, then you go on to you, select

135
00:09:19,070 --> 00:09:20,600
board Arduino Uno.

136
00:09:20,930 --> 00:09:25,160
So if you have an oven, we know, of course, if you have something different, like a nano omega,

137
00:09:25,160 --> 00:09:30,500
you choose the correct bond and then on a you're going to choose the aluminum unibody.

138
00:09:30,510 --> 00:09:38,750
So usually that's going to be something like 7:52 a.m. zero TDY, USB zero with one or something like

139
00:09:38,750 --> 00:09:38,920
that.

140
00:09:38,930 --> 00:09:39,230
OK?

141
00:09:39,470 --> 00:09:45,110
So you select this and then let's just upload an empty program to see if it works.

142
00:09:45,950 --> 00:09:51,410
So compiling, uploading down, uploading great everything is currently working.

143
00:09:51,740 --> 00:09:52,070
All right.

144
00:09:52,070 --> 00:09:54,200
So now we have all the tools we need.

145
00:09:54,590 --> 00:10:00,680
Let's jump straight into the cellular communication so we can make the Raspberry Pi and the Arduino

146
00:10:00,680 --> 00:10:02,420
balls talk to each other.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: PART 1 - Serial Communication Between Raspberry Pi and Arduino

1
00:00:00,210 --> 00:00:05,250
Let's directly dive in and make the Raspberry Pi communicate with the Arduino.

2
00:00:05,760 --> 00:00:12,900
This first bout of the goose will lay the foundations you need in order to build any project using both

3
00:00:12,900 --> 00:00:14,690
Arduino and the Raspberry Pi.

4
00:00:15,180 --> 00:00:19,500
Now, how are we going to make those two boats communicate between each other?

5
00:00:19,950 --> 00:00:23,490
Well, we are going to use cellular communication.

6
00:00:23,880 --> 00:00:25,680
And what is cell communication?

7
00:00:26,160 --> 00:00:32,490
Basically, cellular communication is simply a way to transfer data between two devices.

8
00:00:33,000 --> 00:00:40,980
More specifically, cellular is based on the UART protocol, which means universal asynchronous reception

9
00:00:40,980 --> 00:00:42,330
and transmission.

10
00:00:43,050 --> 00:00:47,300
If this sounds complicated, well, this is not asynchronous.

11
00:00:47,310 --> 00:00:53,970
Reception in transmission simply means that you can talk from the Raspberry Pi to the Arduino and from

12
00:00:53,970 --> 00:00:56,850
the Arduino to the Raspberry Pi at the same time.

13
00:00:57,150 --> 00:01:03,000
Just like when you are chatting with someone in your phone, you can send messages and the other person

14
00:01:03,000 --> 00:01:05,430
can send messages on the same time.

15
00:01:05,790 --> 00:01:07,230
Now, don't worry too much.

16
00:01:07,470 --> 00:01:13,980
We won't need to dive into the low level details because there are some high level libraries that we

17
00:01:13,980 --> 00:01:18,540
can directly use in our code and which will make things easier.

18
00:01:19,020 --> 00:01:22,290
In fact, you probably already know cellular communication.

19
00:01:22,800 --> 00:01:30,330
If you were using to say and monitor on the Arduino Amy to develop your Arduino, well, this is cellular

20
00:01:30,330 --> 00:01:36,210
communication between you are in the world and your Arduino IEEE on your computer.

21
00:01:36,600 --> 00:01:43,470
What we do know is that instead of communicating between Arduino and Assaad monitor, we would create

22
00:01:43,470 --> 00:01:49,290
a communication between Arduino and a Python program on the Raspberry Pi.

23
00:01:49,950 --> 00:01:55,950
So in this section, we first show you how to do the required setup for sale communication to won't.

24
00:01:56,400 --> 00:02:03,480
We will then initiate a communication between the Raspberry Pi and Arduino, bold and by step through

25
00:02:03,480 --> 00:02:05,070
several code iterations.

26
00:02:05,370 --> 00:02:09,450
You will discover the different ways to communicate with Syria.

27
00:02:10,020 --> 00:02:15,390
After this, I will give you some activities so you can practice on everything you will see now.

28
00:02:15,930 --> 00:02:17,810
All right, and let's get started.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:04,050
Let's start with the hardware set up for sale communication.

2
00:00:04,440 --> 00:00:08,910
So you have your Raspberry Pi here and you can see it's already powered on for me.

3
00:00:08,940 --> 00:00:09,210
OK.

4
00:00:09,480 --> 00:00:12,090
And you have your avenue and the USB cable.

5
00:00:12,450 --> 00:00:19,710
So what you're simply going to do is connect the Arduino to the Raspberry Pi with the USB cable, as

6
00:00:19,710 --> 00:00:20,200
you can see.

7
00:00:20,220 --> 00:00:23,150
You can do that when the Raspberry Pi is put up on.

8
00:00:23,220 --> 00:00:25,890
Apple will offer it doesn't really matter.

9
00:00:26,310 --> 00:00:27,510
And that's pretty much it.

10
00:00:27,540 --> 00:00:31,950
Now you can see also on the old, you know, here I'm going to unplug it here.

11
00:00:32,340 --> 00:00:35,200
You're going to see you have some pins here on the Arduino.

12
00:00:35,260 --> 00:00:43,370
You know, you have zero and one, which are X and T X, and those are also pins for telecommunications.

13
00:00:43,380 --> 00:00:47,420
So you could use those eventually, which some use on the Raspberry Pi.

14
00:00:47,430 --> 00:00:54,660
But this is much more complex because you need a voltage level shifter between five volts and 3.3 volt.

15
00:00:55,050 --> 00:01:01,020
It's also less robust, less reliable and usually cables are already working well.

16
00:01:01,080 --> 00:01:01,380
OK.

17
00:01:01,410 --> 00:01:05,040
I've never had any problem with cellular communication that way.

18
00:01:05,400 --> 00:01:08,430
And one more thing is that so here I have an Arduino uno.

19
00:01:08,430 --> 00:01:11,460
You may have a different kind of bond, OK?

20
00:01:11,490 --> 00:01:15,090
And depending on the Bond USB-C connector, you may be different.

21
00:01:15,090 --> 00:01:20,280
So I have like a standard classic one, but you may have a micro USB.

22
00:01:20,580 --> 00:01:22,140
Well, it doesn't really matter.

23
00:01:22,140 --> 00:01:28,560
As long as you can connect the USB connector here to the USB connector here on the Raspberry Pi, everything

24
00:01:28,560 --> 00:01:30,120
is going to work correctly.

25
00:01:31,470 --> 00:01:37,170
Now that the hardware setup is down, let's do the software setup, and for that, you go to your Raspberry

26
00:01:37,170 --> 00:01:42,810
Pi desktop, so make sure, of course, that you have correctly plugged your out in the world to the

27
00:01:42,810 --> 00:01:45,090
Raspberry Pi using the USB cable.

28
00:01:45,780 --> 00:01:52,770
And so for the audio side, there is nothing to sale, is already configured and ready to be used with

29
00:01:52,770 --> 00:01:56,350
the cellular library under Raspberry Pi board.

30
00:01:56,370 --> 00:01:58,860
We will need to do a few setup steps.

31
00:01:59,400 --> 00:02:02,970
So first of all, you can open a terminal here.

32
00:02:04,320 --> 00:02:11,880
Click on the icon and do unless Dash then does T y.

33
00:02:12,420 --> 00:02:16,920
And in this, we can list all of the stuff that starts.

34
00:02:17,220 --> 00:02:20,520
We've slashed Dave Slash, did you what you press enter.

35
00:02:20,730 --> 00:02:22,470
And you can see all of that.

36
00:02:22,470 --> 00:02:23,430
So what is this?

37
00:02:23,610 --> 00:02:29,690
Well, basically we are going to try to find the port of the Arduino on the Raspberry Pi.

38
00:02:29,700 --> 00:02:36,990
OK, so the plot is basically the name that is given to the port here so that we can recognize it and

39
00:02:36,990 --> 00:02:38,400
then we can connect to it.

40
00:02:39,060 --> 00:02:40,650
And will you have quite a few?

41
00:02:41,490 --> 00:02:43,170
I'm going to give you the answer to both.

42
00:02:43,170 --> 00:02:44,050
Is that one?

43
00:02:44,070 --> 00:02:47,250
OK, slash Dave slash TDY ACM zero.

44
00:02:47,490 --> 00:02:49,260
So you should have something like this.

45
00:02:49,500 --> 00:02:52,680
Did you, I assume, are two white USB depends.

46
00:02:53,070 --> 00:02:56,000
We have a number that can be zero one.

47
00:02:56,100 --> 00:02:58,860
What usually you will start with this.

48
00:02:59,220 --> 00:03:02,370
Know how to be sure you have this port?

49
00:03:02,520 --> 00:03:05,820
Well, you simply disconnect your Arduino.

50
00:03:05,820 --> 00:03:08,790
So I just unplugged my out in the world.

51
00:03:08,940 --> 00:03:09,270
OK?

52
00:03:09,630 --> 00:03:13,830
I just unplugged the USB cable, and now I'm going to run this command again.

53
00:03:15,560 --> 00:03:17,790
And you can see that here.

54
00:03:18,710 --> 00:03:22,100
We don't have the white patient zero anymore.

55
00:03:22,730 --> 00:03:25,100
I'm going to read like the Arduino.

56
00:03:25,970 --> 00:03:30,320
Now, don't always plug IRA in the Quran, and you can see now we have this.

57
00:03:30,320 --> 00:03:35,660
So basically you just disconnect your Arduino, you rendered command, you connect your Arduino and

58
00:03:35,660 --> 00:03:38,900
you just find what is the Newport that is here.

59
00:03:39,200 --> 00:03:41,240
So now we know that this is the name of the port.

60
00:03:41,540 --> 00:03:46,670
What you could also do is if you have the Arduino IEEE installed.

61
00:03:49,490 --> 00:03:55,670
You can see here on tools and what we can find also the same name.

62
00:03:55,760 --> 00:03:56,180
All right.

63
00:03:59,060 --> 00:04:02,230
So now we have to put hungering to to clear on a terminal.

64
00:04:02,660 --> 00:04:08,930
The second step we need to do is to make sure that our users of debate user, which is here, you can

65
00:04:08,930 --> 00:04:13,550
see how the permission to access to cellular communication.

66
00:04:14,360 --> 00:04:18,440
So we're going to do groups to see all the groups we are in.

67
00:04:18,480 --> 00:04:18,800
OK.

68
00:04:18,890 --> 00:04:24,020
So other by use it, you can see we are already in the dial out group.

69
00:04:24,140 --> 00:04:28,520
And this is the one that gives you access to cellular communication.

70
00:04:28,910 --> 00:04:36,980
So if you don't have this when you type groups, so what you can do is sudo add user and then the name

71
00:04:36,980 --> 00:04:37,760
of your user.

72
00:04:37,760 --> 00:04:43,910
So it's PI and the name of the group you press enter and you can see here.

73
00:04:43,940 --> 00:04:48,620
The user is already a member of bail out, but it was not the case.

74
00:04:48,620 --> 00:04:55,730
It would add you to the group, OK, if you just added your user to the dialogue, you need to log out

75
00:04:55,730 --> 00:04:56,390
and login.

76
00:04:56,390 --> 00:04:58,070
So what you can do is look at logging on.

77
00:04:58,070 --> 00:05:00,860
You can also watch a Raspberry Pi, so you can be sure.

78
00:05:01,190 --> 00:05:01,490
All right.

79
00:05:01,520 --> 00:05:02,800
That was the second step.

80
00:05:02,810 --> 00:05:06,860
The third step is to install a Python library.

81
00:05:07,460 --> 00:05:12,650
So on the other side, we have the civil service library called Cellular, which is already installed

82
00:05:12,650 --> 00:05:13,310
on the I don't know.

83
00:05:13,580 --> 00:05:20,420
But on the Raspberry Pi side, we need a Python module and this Python module is by.

84
00:05:21,050 --> 00:05:24,980
OK, so we are going to use the PI serial module and to install it.

85
00:05:24,980 --> 00:05:27,500
So first, make sure you have IP three.

86
00:05:27,680 --> 00:05:33,790
So if you don't have the IP three sudo apt, get install Python three.

87
00:05:33,800 --> 00:05:35,180
Dash the IP.

88
00:05:37,180 --> 00:05:45,100
OK, it's already here, and then IP three installed by serial like that.

89
00:05:45,250 --> 00:05:45,580
OK.

90
00:05:46,150 --> 00:05:47,050
Press Enter.

91
00:05:49,490 --> 00:05:50,690
And already installed.

92
00:05:50,930 --> 00:05:57,110
So actually, it may already be installed on your raspberry base, so if that's the case, that's wonderful.

93
00:05:57,260 --> 00:06:01,970
And then you can do Pipe three show by Cellule.

94
00:06:02,410 --> 00:06:02,720
OK.

95
00:06:04,590 --> 00:06:11,250
To see the version, to see more details and maybe the page with documentation and everything for this

96
00:06:11,700 --> 00:06:12,270
library.

97
00:06:12,840 --> 00:06:14,160
And that's pretty much it.

98
00:06:14,640 --> 00:06:15,330
OK, great.

99
00:06:15,420 --> 00:06:17,610
So now everything is correctly set up.

100
00:06:18,030 --> 00:06:20,700
The original word is plug it to the Raspberry Pi.

101
00:06:20,700 --> 00:06:26,670
With the USB cable, you have the correct permission on the Raspberry Pi and you also have a cellular

102
00:06:26,670 --> 00:06:30,210
library ready to be used on both sides.

103
00:06:30,540 --> 00:06:31,190
Let us know.

104
00:06:31,200 --> 00:06:32,820
Initiate the communication.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:02,760
No, not everything's correctly configured.

2
00:00:02,940 --> 00:00:09,570
Let's start the communication in this lesson, we would just initiate the communication and in the following

3
00:00:09,570 --> 00:00:13,370
lessons we would exchange some data between the two boats.

4
00:00:13,680 --> 00:00:16,990
So we are going to open it.

5
00:00:17,340 --> 00:00:19,140
The how do you know any?

6
00:00:21,540 --> 00:00:24,240
So we can upload some code to the world.

7
00:00:26,310 --> 00:00:28,740
And we are also going to open.

8
00:00:29,820 --> 00:00:35,490
The Sydney, based on an Easter weekend to write some Python code on the Raspberry Pi.

9
00:00:36,270 --> 00:00:39,360
So I'm going to organize like this.

10
00:00:42,010 --> 00:00:46,650
So I can have call on one side and the Python code on the other side.

11
00:00:46,830 --> 00:00:51,330
OK, so this is going to run on the other know this is going to run on the Raspberry Pi.

12
00:00:51,720 --> 00:00:55,950
And as you can see, that's very practical that we have no idea on the Raspberry Pi.

13
00:00:56,220 --> 00:01:02,920
So we can directly into two programs on the same, please, and we are going to start with the original

14
00:01:02,920 --> 00:01:02,940
of.

15
00:01:03,480 --> 00:01:03,730
OK.

16
00:01:03,750 --> 00:01:05,430
Usually that's what we're going to do.

17
00:01:05,610 --> 00:01:09,180
We're going to start from, I don't know, because that's going to be easier to debug.

18
00:01:09,360 --> 00:01:18,060
So to start cellular communication, will you just do sanyal that begin with a bold right?

19
00:01:18,330 --> 00:01:20,430
So that is a quite classic both, right?

20
00:01:20,460 --> 00:01:22,590
Nine thousand six hundred.

21
00:01:23,250 --> 00:01:23,530
OK.

22
00:01:23,550 --> 00:01:27,780
And you put this line in sight devoid of your argument.

23
00:01:27,960 --> 00:01:33,090
You have void setup, which is going to be executed once and void loop, which is going to be executed

24
00:01:33,330 --> 00:01:35,250
an infinite number of time.

25
00:01:35,580 --> 00:01:40,170
So with this, we have initialized cellular on the Odin, so that's very simple.

26
00:01:40,260 --> 00:01:44,170
What we can do also, and this is going to depend on the order.

27
00:01:44,180 --> 00:01:52,420
The ball that you have is the wine and then exclamation mark from that sale.

28
00:01:53,550 --> 00:01:57,240
And then just open close curly brackets.

29
00:01:57,600 --> 00:02:04,260
So this basically on the original Uno, for example, nano omega, you don't need this line, but if

30
00:02:04,260 --> 00:02:12,150
you are using an onion with a native USB, for example Arduino Leonardo Arduino zero, then you may

31
00:02:12,150 --> 00:02:13,220
need to use this line.

32
00:02:13,230 --> 00:02:15,840
Otherwise, the sale is not going to work correctly.

33
00:02:15,850 --> 00:02:20,900
So basically, this is going to wait until the sale is ready.

34
00:02:21,390 --> 00:02:27,750
So I'm just going to include it here and in every program I do so that this code is going to work on

35
00:02:27,750 --> 00:02:29,280
pretty much any Arduino board.

36
00:02:29,700 --> 00:02:33,240
But if you are using Arduino Uno like me, you don't need this.

37
00:02:34,050 --> 00:02:34,350
All right.

38
00:02:34,350 --> 00:02:36,030
So that's the code for the Arduino part.

39
00:02:36,420 --> 00:02:41,550
Now I'm going to go on the Raspberry Pi part and write some Python program.

40
00:02:42,210 --> 00:02:49,170
So let's we'll start with this user bee and with Python three.

41
00:02:49,200 --> 00:02:55,650
OK, so if we ever execute this from the terminal directly, we give the information that the interpreter

42
00:02:55,650 --> 00:02:56,710
is buying from three.

43
00:02:57,210 --> 00:02:58,470
Now what are we going to do?

44
00:02:58,470 --> 00:03:02,460
Is We're gonna first import Syria.

45
00:03:02,580 --> 00:03:08,030
OK, so the name of the library is by cellular, but you're going to import sell.

46
00:03:08,310 --> 00:03:08,660
OK.

47
00:03:09,240 --> 00:03:12,780
On the original, you have nothing to import, which is Syria is already there.

48
00:03:13,080 --> 00:03:16,290
But on the Raspberry Pi, you have to import that module.

49
00:03:16,530 --> 00:03:22,770
And then when the first thing we're going to do is to open the cellular communication and the cell communication

50
00:03:22,770 --> 00:03:28,920
is going to give us something that I'm going to save us for saying, OK, I do this because that's quite

51
00:03:28,920 --> 00:03:29,370
common.

52
00:03:29,370 --> 00:03:33,450
And if you find any help on the internet, I need to tell you any documentation.

53
00:03:33,450 --> 00:03:34,740
That's what you're going to see.

54
00:03:34,740 --> 00:03:39,390
So I'm going to keep the convention that is on the internet, right?

55
00:03:39,720 --> 00:03:42,030
And so is equal to Syria.

56
00:03:42,120 --> 00:03:42,630
Don't.

57
00:03:43,820 --> 00:03:49,160
Syria uppercase with uppercase, you open close parentheses.

58
00:03:49,490 --> 00:03:52,470
And first, we are going to give the quotes.

59
00:03:53,180 --> 00:04:00,770
OK, so if you remember the plot was slush, then slush TDY eight, the zero.

60
00:04:01,130 --> 00:04:04,560
So that is the quote I have found actually in the previous listen.

61
00:04:05,100 --> 00:04:09,710
So if you are not sure what's what is yours because that may be something different here.

62
00:04:10,040 --> 00:04:16,070
Please go back to the previous lesson and how to set up same communication and then come back with the

63
00:04:16,070 --> 00:04:20,060
quotes that corresponds to your order, not the next parameter.

64
00:04:20,060 --> 00:04:21,260
Is the board right?

65
00:04:21,590 --> 00:04:24,530
So the bond rate is actually what you can see here.

66
00:04:24,860 --> 00:04:27,110
That's the speed of communication, basically.

67
00:04:27,560 --> 00:04:30,140
And this is super, super important.

68
00:04:30,150 --> 00:04:35,040
You have to have the same bond rate on both sides of the communication key.

69
00:04:35,060 --> 00:04:40,220
If you have a different body rate, then the two parents can't understand each other.

70
00:04:40,370 --> 00:04:46,040
And actually, speaking of both rate, this is the pretty common classic both rate you're going to have

71
00:04:46,040 --> 00:04:49,700
in every tutorial, but it's also a pretty slow one.

72
00:04:50,030 --> 00:04:56,930
You can go up to 150 and fifteen thousand two hundred bode, OK, and that's double the rate I'm going

73
00:04:56,930 --> 00:04:57,260
to use.

74
00:04:57,500 --> 00:05:01,520
So if I use this here, I use this here also.

75
00:05:02,150 --> 00:05:04,310
OK, so you're going to have different values, OK?

76
00:05:04,310 --> 00:05:11,570
You have different common values and this is one of the most common one and also quite fast one.

77
00:05:11,570 --> 00:05:14,480
And it's better than the classic nine thousand six hundred.

78
00:05:14,930 --> 00:05:19,280
And I'm going to add a third parameter, which is time out.

79
00:05:19,310 --> 00:05:20,900
Let's see, one point zero.

80
00:05:21,140 --> 00:05:24,350
So timeout here is reads timeout.

81
00:05:24,380 --> 00:05:26,900
I'm going to come back to that a bit later in the call.

82
00:05:26,900 --> 00:05:28,560
So, OK, so don't worry about that for now.

83
00:05:29,030 --> 00:05:29,360
All right.

84
00:05:29,360 --> 00:05:33,080
So with this line, we open the cellular communication.

85
00:05:33,710 --> 00:05:38,930
And if it works, OK, we're going to get the sale inside this SIM.

86
00:05:39,320 --> 00:05:43,340
If it doesn't work, we're going to get an error and the program is going to exit.

87
00:05:43,820 --> 00:05:50,120
Then what they recommend you to do is to wait a few seconds here after opening the communication.

88
00:05:50,120 --> 00:06:00,050
So I'm going to do input time and the time that slick three signals, so I recommend at least two signals.

89
00:06:00,140 --> 00:06:07,040
Three is even better because when you open the cell communication on that side, the thing is that on

90
00:06:07,040 --> 00:06:12,950
the Arduino side, the original for audio, for example, is going to restart.

91
00:06:12,960 --> 00:06:14,810
So the program is going to be restarted.

92
00:06:15,170 --> 00:06:21,470
So what you want to do on the Raspberry Pi side is to give enough time for the Arduino to have the sail

93
00:06:21,470 --> 00:06:23,600
completely ready to communicate.

94
00:06:23,900 --> 00:06:29,030
And so we give three seconds here, and I recommend you do that because if you don't do that and you

95
00:06:29,030 --> 00:06:33,410
try to read some data, I'll just send some data just after that.

96
00:06:33,770 --> 00:06:38,780
You're going to experience some weird bugs in your program, and that's going to be hard actually to

97
00:06:38,780 --> 00:06:40,100
do so better.

98
00:06:40,100 --> 00:06:51,020
Have a time, not sleep with two or three, and then I'm going to do that reset input buffer.

99
00:06:52,130 --> 00:06:53,210
So what is this?

100
00:06:53,240 --> 00:06:59,510
So basically, we cellular both sides can communicate with the other, OK, so I can send data from

101
00:06:59,510 --> 00:07:05,570
the Raspberry Pi to the out, you know, and I can send data from the adeno to the Raspberry Pi when

102
00:07:05,570 --> 00:07:06,800
the data arrives.

103
00:07:07,100 --> 00:07:08,560
It's not directly in the code.

104
00:07:08,580 --> 00:07:11,390
When the data arrives, it's in a buffer.

105
00:07:11,900 --> 00:07:16,070
And when you're going to read, that's what we're going to see in the next lesson.

106
00:07:16,310 --> 00:07:19,990
So when you're going to read, you're going to read actually from the buffet.

107
00:07:20,240 --> 00:07:28,580
So he reads that input buffer, which means that if the Ardoino sends us some data before this, so

108
00:07:28,580 --> 00:07:32,420
when the program is actually paused, we're going to erase everything.

109
00:07:32,420 --> 00:07:37,610
So we start after this line, we refresh buffer that has nothing in it.

110
00:07:37,640 --> 00:07:37,970
OK.

111
00:07:38,210 --> 00:07:41,930
And I'm going to come back also later in the course to explain more about it.

112
00:07:42,230 --> 00:07:42,530
All right.

113
00:07:42,530 --> 00:07:42,970
So that's it.

114
00:07:42,980 --> 00:07:44,930
Now let's maybe put print.

115
00:07:46,610 --> 00:07:47,870
Sale, OK.

116
00:07:49,340 --> 00:07:52,910
Who have a nice confirmation and then well done wrong, he's going to exit.

117
00:07:53,690 --> 00:07:54,950
OK, now what to do?

118
00:07:54,950 --> 00:07:57,440
Because we have the Arduino program here.

119
00:07:57,470 --> 00:07:59,080
The Raspberry Pi program here.

120
00:07:59,570 --> 00:08:04,280
But what you need to do first is to upload the original code on the Arduino.

121
00:08:04,940 --> 00:08:05,330
OK.

122
00:08:05,570 --> 00:08:09,350
That's the first thing to do always is to have the original ready.

123
00:08:09,560 --> 00:08:11,090
So I'm going to go on tools.

124
00:08:12,290 --> 00:08:15,020
Change that I have the correct bald, the correct spot.

125
00:08:15,830 --> 00:08:18,410
And let's do applaud.

126
00:08:20,000 --> 00:08:24,860
Let's save it as first communication.

127
00:08:27,180 --> 00:08:31,530
OK, you can see her compiling and uploading and down uploading.

128
00:08:31,830 --> 00:08:36,420
So the code is now in the oven, know that the code is in the oven.

129
00:08:36,870 --> 00:08:41,790
We go back here and I'm going to say the fine, so savons.

130
00:08:43,320 --> 00:08:46,210
So let's create a new folder, actually here.

131
00:08:46,290 --> 00:08:48,420
So I'm going to enter directly from file manager.

132
00:08:48,990 --> 00:08:49,290
OK?

133
00:08:49,950 --> 00:08:51,540
Right click New Folder.

134
00:08:52,050 --> 00:08:53,310
Let's call it Python.

135
00:08:55,520 --> 00:08:56,150
Programs.

136
00:08:56,870 --> 00:08:57,510
OK.

137
00:08:58,310 --> 00:09:02,750
And let's go back here, let's save as.

138
00:09:03,930 --> 00:09:05,250
In Python program.

139
00:09:06,770 --> 00:09:11,240
First communication that way.

140
00:09:11,420 --> 00:09:13,220
So that's fight and flight.

141
00:09:13,730 --> 00:09:14,840
Click on, OK.

142
00:09:14,960 --> 00:09:19,150
So the program is saved and no, I can run it for to run it.

143
00:09:19,160 --> 00:09:21,680
I can just click on the play button here.

144
00:09:22,140 --> 00:09:23,210
Run from the terminal.

145
00:09:23,420 --> 00:09:25,190
So I'm just going to click here.

146
00:09:27,250 --> 00:09:29,560
And you can see we have.

147
00:09:30,100 --> 00:09:36,550
So we run the script, and after three seasons, we have cellulite, OK, which means that the Raspberry

148
00:09:36,550 --> 00:09:39,310
Pi could correctly connect to that board.

149
00:09:39,430 --> 00:09:39,760
OK.

150
00:09:40,000 --> 00:09:45,220
So it could correctly connect to the Arduino, not one input on thing you have to do.

151
00:09:45,220 --> 00:09:51,900
Also on the Python side is that so he would directly exit after this.

152
00:09:51,910 --> 00:09:55,900
So we open a communication and then exit what you have to do.

153
00:09:55,900 --> 00:10:04,390
And what is better is to close the communication so you can do not close, OK, before you exit the

154
00:10:04,390 --> 00:10:07,540
program whenever you want to close the communication.

155
00:10:07,600 --> 00:10:11,680
So with this, you're going to open the communication with this, you're going to close it.

156
00:10:11,920 --> 00:10:16,150
And on the ordinal side, you don't need to actually close the communication.

157
00:10:16,330 --> 00:10:20,850
The communication is going to be closed simply when you pull it off the audio.

158
00:10:21,100 --> 00:10:23,310
But here are the best practice.

159
00:10:23,590 --> 00:10:29,530
It's better to close it because then if it's not closed correctly and you try to run non-Apple run,

160
00:10:30,010 --> 00:10:31,200
you may have some troubles.

161
00:10:31,720 --> 00:10:33,220
OK, so let's run that again.

162
00:10:34,120 --> 00:10:37,750
You can see we wait three seconds, you OK?

163
00:10:37,750 --> 00:10:39,680
And then we close the communication here.

164
00:10:40,030 --> 00:10:41,530
Everything is good now.

165
00:10:41,530 --> 00:10:42,070
Let's say that.

166
00:10:42,070 --> 00:10:49,960
For example, I don't have my Arduino board connected to the Raspberry Pi, so I have physically removed

167
00:10:49,960 --> 00:10:53,830
the USB cable from the Arduino side of the Raspberry Pi side.

168
00:10:53,830 --> 00:10:54,820
He doesn't really matter.

169
00:10:55,090 --> 00:10:57,190
And I'm going to run the script again.

170
00:10:58,450 --> 00:11:00,850
And you can see we have an error, OK?

171
00:11:01,090 --> 00:11:06,550
We have an error, which is quite big, but at the end you can see some exception.

172
00:11:07,810 --> 00:11:12,460
Could not open ports slams, David 7:52 a.m. Zero.

173
00:11:12,880 --> 00:11:18,080
OK, so basically the port is not found wide because the Arduino is not connected.

174
00:11:18,610 --> 00:11:25,290
If I plugged in to the Raspberry Pi again, let's run the code and now it's working.

175
00:11:27,140 --> 00:11:27,560
Great.

176
00:11:29,620 --> 00:11:32,710
So to recap on the steps here, it's very important.

177
00:11:33,010 --> 00:11:39,220
First, you will need to write some code for the Arduino where you initialize signal of goods and you

178
00:11:39,220 --> 00:11:45,070
need to upload that to Arduino when you upload to the owner to make sure that you are not currently

179
00:11:45,070 --> 00:11:48,720
talking to the Arduino from another program of your Raspberry Pi.

180
00:11:48,730 --> 00:11:49,000
OK?

181
00:11:49,270 --> 00:11:54,310
Because when you upload and when you communicate, you use the same cellular communication.

182
00:11:54,370 --> 00:11:54,730
OK.

183
00:11:55,180 --> 00:12:00,130
So if you are sending data from your Raspberry Pi to the Arduino, we were both on program and you tried

184
00:12:00,130 --> 00:12:00,790
to upload.

185
00:12:00,850 --> 00:12:02,380
You may have some problems.

186
00:12:02,980 --> 00:12:08,740
OK, now that the code is on the Arduino, the code is going to run as soon as the ordinary power on.

187
00:12:09,040 --> 00:12:13,990
And then you can run your Python script where you open the cellular communication.

188
00:12:13,990 --> 00:12:20,110
So make sure you have this thing by the right key and make sure you have the correct both here and basically

189
00:12:20,110 --> 00:12:26,710
in some both like Arduino, Uno Nano Media, for example, when you open the sign communication from

190
00:12:27,010 --> 00:12:32,080
the outside of the Arduino, the audio program is going to be, or is it going to be restarted?

191
00:12:32,530 --> 00:12:38,050
So at this point of the code, this is going to be restarted from scratch.

192
00:12:38,470 --> 00:12:41,060
So that's why you want to wait a few seconds.

193
00:12:41,080 --> 00:12:42,790
So here we wait three seconds.

194
00:12:42,790 --> 00:12:48,640
That is very safe so that the cell communication can currently be initialized, then everything can

195
00:12:48,640 --> 00:12:50,830
be initialized on the Arduino side.

196
00:12:51,130 --> 00:12:52,840
Then you resend input buffer.

197
00:12:53,260 --> 00:12:55,350
You do whatever you want to do here.

198
00:12:55,370 --> 00:12:56,920
You can send and receive data.

199
00:12:56,920 --> 00:12:59,980
That's what we're going to see directly in the following lesson.

200
00:13:00,340 --> 00:13:06,910
And then you close the sale communication here on the rise, the very by side, and you can exit the

201
00:13:06,910 --> 00:13:07,390
program.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,750
Great, you have now successfully initiated cellular communication between your Raspberry Pi and orange

2
00:00:06,750 --> 00:00:07,230
bolts.

3
00:00:07,620 --> 00:00:14,070
Let's now see how to send some data starting from the mountainside to your Raspberry Pi.

4
00:00:14,460 --> 00:00:15,930
So this is going to send data.

5
00:00:15,960 --> 00:00:17,580
This is going to receive data.

6
00:00:18,060 --> 00:00:23,170
So once again, we're going to start on the RNA side because that's going to be easier to do it.

7
00:00:23,580 --> 00:00:28,620
So on the Void said that we initially the communication with that both right, and we make sure the

8
00:00:28,620 --> 00:00:29,810
cell is ready.

9
00:00:30,640 --> 00:00:31,590
But that's pretty much it.

10
00:00:32,040 --> 00:00:34,740
Now what we want to do is to send some string.

11
00:00:34,740 --> 00:00:37,590
Let's say hello, avery, one signal.

12
00:00:38,010 --> 00:00:40,020
So we're going to do that interval loop.

13
00:00:41,170 --> 00:00:51,180
We are going to say a lot print and then we handle from everyone, as you can see when you use standard

14
00:00:51,220 --> 00:00:57,130
print and then all if you use standard print, if you have ever used that before to debate your know,

15
00:00:57,130 --> 00:01:00,910
well, that's the same thing to send data over cellular.

16
00:01:01,120 --> 00:01:09,760
And I'm going to use a printer in here so we can add a new line character after this string, and I'm

17
00:01:09,760 --> 00:01:11,090
going to add a sort of delay.

18
00:01:11,110 --> 00:01:18,430
So let's use delay for simplicity here of one second, so we can send that every second and not all

19
00:01:18,430 --> 00:01:18,850
the time.

20
00:01:19,060 --> 00:01:19,390
All right.

21
00:01:19,570 --> 00:01:23,050
Make sure that nothing is running on the raspberry base and no Python script.

22
00:01:23,530 --> 00:01:25,270
Let's upload the code to the original.

23
00:01:26,810 --> 00:01:27,090
OK.

24
00:01:27,470 --> 00:01:28,070
Applauding.

25
00:01:28,310 --> 00:01:35,510
And now what we can do before we write anything with Python, we can open the say and monitor to debug

26
00:01:35,510 --> 00:01:36,290
what we have.

27
00:01:36,560 --> 00:01:40,370
And you can see we have hello from our new every second.

28
00:01:42,350 --> 00:01:48,860
So by starting on the hour, you know, when you use sound communication, you can make sure that this

29
00:01:48,860 --> 00:01:53,780
site is working with the same monitor, so this tool is super useful.

30
00:01:54,020 --> 00:01:59,780
So now we know that the code is correctly working and correctly sending this string of a set.

31
00:02:00,260 --> 00:02:05,150
So that's going to be easier to debug when we actually tried the Python program because we know that

32
00:02:05,150 --> 00:02:06,470
this site is working.

33
00:02:06,800 --> 00:02:09,470
So no, Hugh, what are we going to do?

34
00:02:09,860 --> 00:02:16,430
So we want to be able to read this string beans will receive and to print it on the temple.

35
00:02:16,730 --> 00:02:17,750
How can we do that?

36
00:02:18,090 --> 00:02:22,070
We're going to create an infinite loop here to read the string.

37
00:02:22,370 --> 00:02:28,940
And if you see him basically on the outing of we have a vault set up, which is going to run wants to

38
00:02:28,940 --> 00:02:29,960
initialize stuff.

39
00:02:30,440 --> 00:02:33,240
And here that's pretty much what we have also.

40
00:02:33,260 --> 00:02:33,560
OK.

41
00:02:33,800 --> 00:02:37,430
Well, going to run that wants to initialize sale communications.

42
00:02:37,430 --> 00:02:43,040
So this part of the code on the Raspberry Pi with Python is actually similar to the void set that we

43
00:02:43,040 --> 00:02:43,880
have on the owner.

44
00:02:44,270 --> 00:02:48,590
And then we have an infinite loop to read and send data.

45
00:02:48,740 --> 00:02:57,140
So we're going to also create our own infinite loop, our own void loop on the Raspberry Pi with Python.

46
00:02:57,350 --> 00:03:03,020
OK, so we can have a structure that is similar to what we have on the Arduino and how do we create

47
00:03:03,170 --> 00:03:07,040
a void loop where we simply do ride through?

48
00:03:07,730 --> 00:03:08,550
And that's it.

49
00:03:08,570 --> 00:03:09,860
We have an infinite loop.

50
00:03:10,160 --> 00:03:10,460
OK.

51
00:03:10,580 --> 00:03:10,910
Right?

52
00:03:10,940 --> 00:03:11,240
True.

53
00:03:11,510 --> 00:03:15,170
And in this loop, we are going to read cycle communication.

54
00:03:15,410 --> 00:03:19,700
And actually the first thing I'm going to do is do time that sleep.

55
00:03:20,000 --> 00:03:22,880
We've let see zero point zero one second.

56
00:03:23,150 --> 00:03:29,600
OK, so here you can run the void loop as fast as you can, basically as fast as the microcontroller

57
00:03:29,600 --> 00:03:29,820
can.

58
00:03:29,870 --> 00:03:35,480
That's not a problem because any way that Arduino is just doing that, but on the Raspberry Pi, if

59
00:03:35,480 --> 00:03:42,440
you run an infinite loop at full speed, what's going to happen is that is going to take all the resources

60
00:03:42,440 --> 00:03:45,590
of your CPU for just one Python per run.

61
00:03:45,770 --> 00:03:51,050
And it may make the Python program very slow or anything else that you do very slow.

62
00:03:51,350 --> 00:03:54,020
So that's why I'm going to the time of sleep.

63
00:03:54,410 --> 00:04:01,730
We let's use this, which means that this is going to be executed 100 times per second, which is more

64
00:04:01,730 --> 00:04:04,460
than enough for this listen and also follow its course.

65
00:04:04,790 --> 00:04:07,730
So we have our own kind of void loop.

66
00:04:08,090 --> 00:04:10,070
What do we do in that void loop?

67
00:04:10,340 --> 00:04:15,200
Well, we're going to check first if we have received something from the Arduino.

68
00:04:15,500 --> 00:04:18,350
And if, yes, we are going to read that thing.

69
00:04:18,380 --> 00:04:21,040
OK, so we can do this set.

70
00:04:21,080 --> 00:04:27,110
So we use the and we have created here nuts in waiting.

71
00:04:27,740 --> 00:04:33,290
This is going to write down the number of bytes that have been received from the Arduino.

72
00:04:33,740 --> 00:04:36,020
So we don't really care what the number of bytes.

73
00:04:36,230 --> 00:04:39,980
What we care about is how we received some data.

74
00:04:40,130 --> 00:04:45,290
If we have received some data, it means that the number of byte is simply greater than zero.

75
00:04:45,530 --> 00:04:51,560
We don't need to count them, but just knowing that it's greater than zero means we have received something.

76
00:04:51,980 --> 00:04:53,930
OK, one very important thing here.

77
00:04:53,960 --> 00:04:55,620
Don't put parentheses.

78
00:04:55,820 --> 00:04:56,180
OK.

79
00:04:56,570 --> 00:04:57,650
This is not a function.

80
00:04:57,680 --> 00:05:00,140
This is an attribute of say it.

81
00:05:00,860 --> 00:05:03,500
So press enter with the indentation here.

82
00:05:03,800 --> 00:05:09,620
If we have received something, let's say here we are going to read the next line.

83
00:05:09,950 --> 00:05:14,420
OK, so line is equal to say Don't read line.

84
00:05:15,170 --> 00:05:16,160
We guarantee this.

85
00:05:16,610 --> 00:05:18,110
This is going to read the next line.

86
00:05:18,140 --> 00:05:19,880
What is the next line?

87
00:05:19,910 --> 00:05:28,250
So basically, the next line is going to be everything until we get this backslash in character, which

88
00:05:28,250 --> 00:05:30,710
is basically a new line character.

89
00:05:30,980 --> 00:05:32,930
And no, you can see that it's very important here.

90
00:05:33,320 --> 00:05:36,580
That's why I have added elements of print and in.

91
00:05:36,980 --> 00:05:40,310
So basically, this is going to send a handle from Arduino.

92
00:05:40,730 --> 00:05:43,550
We have a new line character after this.

93
00:05:44,030 --> 00:05:47,240
And so on the Raspberry Pi, we've read line.

94
00:05:47,900 --> 00:05:53,390
It's going to read hello from Arduino until that new line character that's going to be here.

95
00:05:53,870 --> 00:05:57,200
So now we have our line, but basically this is encoded, OK?

96
00:05:57,530 --> 00:06:03,560
Sale is not just going to send a string like this, it's going to encode it so it can better communicate.

97
00:06:03,600 --> 00:06:06,770
OK, so basically what you're receiving here are just bytes.

98
00:06:07,160 --> 00:06:07,410
OK?

99
00:06:07,820 --> 00:06:10,940
If you want to read them on the train, you can do that.

100
00:06:11,940 --> 00:06:16,320
Decode ending UTF eight.

101
00:06:17,730 --> 00:06:24,720
That is going to decode what you get, we've read line into a correct string that you can read here

102
00:06:25,620 --> 00:06:27,990
and then let's do print line.

103
00:06:28,770 --> 00:06:29,160
All right.

104
00:06:29,640 --> 00:06:36,750
So basically, this is going to run forever until you press conference C at 100, it's just going to

105
00:06:36,750 --> 00:06:39,090
check if you have received something of a sale.

106
00:06:39,120 --> 00:06:43,260
If yes, it's good now, read it and decode it and print it.

107
00:06:43,710 --> 00:06:44,880
Now I'm going to do something.

108
00:06:44,880 --> 00:06:50,010
Here is, of course, and we're not going to close the communication before we actually start to use

109
00:06:50,010 --> 00:06:50,140
it.

110
00:06:50,140 --> 00:06:54,450
So I'm going to put that at the end of the program.

111
00:06:55,020 --> 00:07:01,560
And maybe you would see your program here is that if we press controlled, see inside this way loop,

112
00:07:02,160 --> 00:07:08,370
we are never going to go to line 16 and we are never going to close correctly to cell communication.

113
00:07:08,690 --> 00:07:11,970
OK, so if I put this down here, it's never going to be cold.

114
00:07:12,360 --> 00:07:19,170
So what I am going to do before I run the program is then going to put this one up inside.

115
00:07:19,200 --> 00:07:20,970
It's right, except structure.

116
00:07:21,330 --> 00:07:24,780
OK, so I can catch the keyboard interact exception.

117
00:07:25,290 --> 00:07:29,190
And basically when price control, see, we are going to close the communication.

118
00:07:29,310 --> 00:07:35,310
OK, so let's do that now as do try and put that with one more indentation.

119
00:07:35,310 --> 00:07:45,510
So you select everything and you press down and then come back to New Line, except keyboard interrupt

120
00:07:45,510 --> 00:07:46,020
ladies.

121
00:07:46,020 --> 00:07:55,560
This basically, for example, when we press control C and we do see the close inside the handle of

122
00:07:55,560 --> 00:07:56,310
the interrupt.

123
00:07:56,580 --> 00:07:59,610
And I'm going also to just add here.

124
00:07:59,640 --> 00:08:05,490
Print close cell communication.

125
00:08:06,300 --> 00:08:08,940
OK, so we know that this has been executed.

126
00:08:09,270 --> 00:08:09,600
All right.

127
00:08:09,600 --> 00:08:11,020
So now let's run this.

128
00:08:11,130 --> 00:08:16,140
So the code here is already running on the audio and go not run here from the Raspberry Pi.

129
00:08:18,430 --> 00:08:23,740
OK, so you can see saleyard, OK, and then hello from Andrew, not every second.

130
00:08:24,400 --> 00:08:24,790
Great.

131
00:08:25,570 --> 00:08:27,080
No, I'm going to price controls.

132
00:08:27,080 --> 00:08:28,870
See, I'm going to click here and price controls.

133
00:08:28,870 --> 00:08:29,260
See?

134
00:08:30,920 --> 00:08:33,740
And you can see closed cellular communication.

135
00:08:33,860 --> 00:08:39,710
OK, so if you are running discrete from the terminal all the way to kill the script, you just do control

136
00:08:39,740 --> 00:08:40,040
C.

137
00:08:40,520 --> 00:08:46,940
And if you are running it directly from fully based on 80, well, you need to click you and press control.

138
00:08:46,940 --> 00:08:47,750
See OK.

139
00:08:47,750 --> 00:08:53,540
If you click on the stop button, it's not going to do the same, so make sure that you click here and

140
00:08:53,540 --> 00:08:56,330
you press controls to close cell communication.

141
00:08:56,780 --> 00:09:00,200
As you can see what we were seeing destroying string every single.

142
00:09:00,210 --> 00:09:06,950
That's great, but we still have some new line in some characters that actually are not part of that

143
00:09:06,950 --> 00:09:07,370
string.

144
00:09:07,730 --> 00:09:13,460
So when you receive something we've read line, you may often have some new line characters that are

145
00:09:13,460 --> 00:09:15,800
added, some courage written.

146
00:09:16,070 --> 00:09:21,670
And in that case, what you can do is after Decode, you can do it up straight.

147
00:09:22,730 --> 00:09:28,550
So this function is going to remove any new line character of any carriage region that you have on a

148
00:09:28,550 --> 00:09:28,940
string.

149
00:09:29,210 --> 00:09:32,210
So you just have to hello from Arduino and nothing else.

150
00:09:32,690 --> 00:09:34,040
OK, let's run that again.

151
00:09:37,270 --> 00:09:44,200
Say, OK, you can see hello from every scene without any other character, I click here.

152
00:09:44,290 --> 00:09:47,320
Press control, see closed cellular communication.

153
00:09:47,890 --> 00:09:52,630
And one thing I want to show you is if you look at the Sun, I'm going to run the script.

154
00:09:52,930 --> 00:09:54,640
If you look at the underworld.

155
00:09:56,670 --> 00:10:01,380
You will see the it is going to blink every one second.

156
00:10:01,560 --> 00:10:03,870
At the same time that you send this training.

157
00:10:04,380 --> 00:10:04,740
All right.

158
00:10:05,190 --> 00:10:12,900
And see here and now I'm going to do cultural sea and it stops blinking and no, where it's just put

159
00:10:12,920 --> 00:10:13,080
on.

160
00:10:13,520 --> 00:10:21,120
And so basically, you have this T.X energy that's going to help you also see when you are sending data

161
00:10:21,120 --> 00:10:23,220
from Arduino to Raspberry Pi.

162
00:10:23,430 --> 00:10:25,290
So Tepe means transmission.

163
00:10:25,650 --> 00:10:30,990
And so it's yet another tool to help you see what's going on in your application.

164
00:10:31,350 --> 00:10:36,480
And one last thing I want to show you is that actually, let's say you use a different booth right here.

165
00:10:36,810 --> 00:10:39,150
So let's say I use 9600.

166
00:10:40,050 --> 00:10:44,070
I still use this one on the original, but they use that one on the Raspberry Pi.

167
00:10:44,550 --> 00:10:45,810
So let's run the program.

168
00:10:48,280 --> 00:10:50,890
And let's see what happens, Sergeant.

169
00:10:50,920 --> 00:11:00,100
OK, so the communication can be studied great, but then well, it seems that we don't perceive anything.

170
00:11:00,490 --> 00:11:05,770
OK, the communication is not working, so you can see that if you don't have the same boy right, you're

171
00:11:05,770 --> 00:11:10,060
going to have weird behavior because the communication is going to be open.

172
00:11:10,390 --> 00:11:13,030
But then anything else he is not going to watch?

173
00:11:13,150 --> 00:11:13,450
OK?

174
00:11:13,720 --> 00:11:18,250
A press control c close cell communication, but we haven't received anything.

175
00:11:19,690 --> 00:11:23,140
I go back to this one.

176
00:11:24,140 --> 00:11:27,140
That's wrong, script and sale.

177
00:11:27,800 --> 00:11:28,240
OK.

178
00:11:28,580 --> 00:11:32,960
Hello from I don't know, it's it's a press conference and it's working correctly.

179
00:11:33,320 --> 00:11:34,520
So both, right?

180
00:11:34,880 --> 00:11:37,700
Super, super, super important.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:00,480
OK.

2
00:00:00,510 --> 00:00:03,600
You can send some data from your Arduino to your Raspberry Pi.

3
00:00:03,840 --> 00:00:08,550
And let's start again to see how to send data from the Raspberry Pi to the.

4
00:00:09,030 --> 00:00:11,410
And so we are going to start from scratch.

5
00:00:11,430 --> 00:00:16,440
OK, I'm just going to remove that code here and that code?

6
00:00:16,890 --> 00:00:17,180
Yeah.

7
00:00:18,330 --> 00:00:23,730
So we came to the same structure on the Arduino, we're going to initialize Sanyo and make sure it's

8
00:00:24,030 --> 00:00:26,470
up and on the Raspberry Pi.

9
00:00:26,490 --> 00:00:27,360
Well, the same thing.

10
00:00:27,360 --> 00:00:28,350
We are buying the cell.

11
00:00:28,350 --> 00:00:36,480
Yeah, we wait a bit reset input buffer and then we have this infinite wide loop, which is basically

12
00:00:36,720 --> 00:00:44,100
the same as we look with except keyboard interrupt to close the sale communication when we killed the

13
00:00:44,100 --> 00:00:44,720
program.

14
00:00:45,070 --> 00:00:45,810
Get in here.

15
00:00:45,820 --> 00:00:47,730
We're going to do our stuff here.

16
00:00:48,030 --> 00:00:49,440
So other ways.

17
00:00:49,530 --> 00:00:52,260
Let's start with Arduino here.

18
00:00:52,280 --> 00:00:58,980
What we want to do is we don't want to send data, we want to receive data and to receive these are

19
00:00:59,030 --> 00:01:05,610
we're going to do basically the same as what we did previously were derisory pay, which is to first

20
00:01:05,730 --> 00:01:07,770
check if we have received some data.

21
00:01:07,770 --> 00:01:10,920
And if you read the next line.

22
00:01:11,340 --> 00:01:12,540
OK, so what are we going to do?

23
00:01:12,540 --> 00:01:15,270
Is if cellular?

24
00:01:15,690 --> 00:01:25,290
Not so we have a function which is standard available because you can see it should arrange so parenthesis.

25
00:01:25,770 --> 00:01:30,900
If this is strictly greater than zero, then we have received some data.

26
00:01:31,080 --> 00:01:37,830
So this function is going to retain the number of bytes that the algorithm has received in the buffer,

27
00:01:38,010 --> 00:01:43,800
which is the same thing as the cellular in waiting attribute we had in the Raspberry Pi.

28
00:01:43,810 --> 00:01:44,100
OK?

29
00:01:44,400 --> 00:01:45,240
That's the same thing.

30
00:01:45,510 --> 00:01:50,700
So this is the number of bytes we don't really care about the number of bytes which are scared that

31
00:01:50,700 --> 00:01:54,750
the number of bytes is greater than zero, which means we have received something.

32
00:01:55,230 --> 00:02:02,070
If this is the case, what I'm going to just string the message is equal to.

33
00:02:02,100 --> 00:02:06,540
We can do cellular that read string.

34
00:02:07,680 --> 00:02:14,760
This is going to read the next stream, so it's going to also decode it and put that inside a string

35
00:02:14,940 --> 00:02:15,480
message.

36
00:02:15,720 --> 00:02:16,740
So very simple.

37
00:02:17,070 --> 00:02:20,940
Now if you do that, and that's where I'm going to talk about the timeout.

38
00:02:21,330 --> 00:02:26,460
So basically, there is a reading time out of one second by default.

39
00:02:26,790 --> 00:02:32,730
So when you use this, the program is going to be stuck for at least one second.

40
00:02:32,760 --> 00:02:39,660
OK, so basically, as long as you receive some strings, it's going to wait one second to be sure that

41
00:02:39,660 --> 00:02:43,440
it hasn't received more than what you've already received.

42
00:02:44,010 --> 00:02:49,200
And so if we just run like this and then we send data from the Raspberry Pi to the Arduino, well,

43
00:02:49,560 --> 00:02:53,080
we're going to see some delay in the processing on the outer.

44
00:02:53,790 --> 00:02:54,870
So what we can do?

45
00:02:55,080 --> 00:02:56,110
There are two options.

46
00:02:56,130 --> 00:03:02,910
The third option is to do stereo nuts set came out with.

47
00:03:03,300 --> 00:03:08,520
So the default is 1000 milliseconds, which we can do is maybe 10 milliseconds.

48
00:03:09,210 --> 00:03:10,650
So that's going to be much faster.

49
00:03:10,650 --> 00:03:13,950
But still, it's going to be stuck for at least 10 milliseconds.

50
00:03:14,640 --> 00:03:22,140
And the lower you go, actually, the higher the risk of missing some data, all of just reading so

51
00:03:22,140 --> 00:03:26,670
fast that you don't receive everything and you'll receive an incomplete message.

52
00:03:27,000 --> 00:03:29,280
So 10 minutes to go should work.

53
00:03:29,910 --> 00:03:34,090
But I'm not going to spend too much time on this because we are not going to use that timeout.

54
00:03:34,110 --> 00:03:42,320
Instead, I'm going to use another function, which is string until and I'm going to put the backslash

55
00:03:42,810 --> 00:03:44,400
in character with.

56
00:03:44,400 --> 00:03:48,990
And this is important single quotes and not double quotes.

57
00:03:49,060 --> 00:03:50,540
OK, single quotes.

58
00:03:50,550 --> 00:03:52,530
Again, this is super, super important.

59
00:03:52,980 --> 00:03:59,520
So this function is going to read the string until it gets to this character, and this function is

60
00:03:59,520 --> 00:04:03,690
going to return as soon as it detects this character.

61
00:04:03,720 --> 00:04:06,090
So the timeout still applies.

62
00:04:06,090 --> 00:04:10,050
So we still have a timeout one second that's going to block this one second.

63
00:04:10,530 --> 00:04:15,990
But if you receive that character, the timeout doesn't apply anymore and you just get the string.

64
00:04:15,990 --> 00:04:22,290
So basically, if we send here from the Raspberry Pi a string, we've added backslash and character

65
00:04:22,290 --> 00:04:22,800
at the end.

66
00:04:22,800 --> 00:04:28,120
So a new line, then we're going to be able to read it immediately with this function.

67
00:04:28,140 --> 00:04:34,770
And so this is basically the function I'm going to use for all the calls read string and in which it's

68
00:04:34,770 --> 00:04:41,340
quite beautiful, quite efficient, and it's going to give us directly a string that we can process

69
00:04:41,340 --> 00:04:41,940
afterwards.

70
00:04:42,540 --> 00:04:48,300
OK, and then once we have received Dismiss End, where we can process it and do whatever we want in

71
00:04:48,300 --> 00:04:53,190
the output right now, I'm going to go back to the Python code on the Raspberry Pi.

72
00:04:53,760 --> 00:04:59,370
So first, I'm going to prove that trigger to how do we know when it's running?

73
00:04:59,400 --> 00:05:03,320
Then it's waiting for data on Python.

74
00:05:03,330 --> 00:05:07,830
If you want to send something on the same, what you can do is set.

75
00:05:07,860 --> 00:05:14,610
So you do object we have here, OK from sale, send don't right?

76
00:05:15,570 --> 00:05:16,740
And then you're going to.

77
00:05:17,010 --> 00:05:17,560
But what?

78
00:05:17,740 --> 00:05:22,360
You want to write, let's say hello from Raspberry Pi.

79
00:05:23,610 --> 00:05:30,210
And we're going to add a backslash and character din, so that is very important, OK, because if you

80
00:05:30,210 --> 00:05:33,810
don't send that, this is going to wait one second.

81
00:05:34,260 --> 00:05:36,660
So it's still going on to receive hello from Raspberry Pi.

82
00:05:36,660 --> 00:05:43,810
But after one second, if you add the backslash in as soon as this function detects the backslash and

83
00:05:43,830 --> 00:05:50,730
is going to return with this exact string and nothing is going to be stopped, and then we're coming

84
00:05:50,730 --> 00:05:57,540
back here, as you have seen previously, when we read data from Sanyal, we need to decode it when

85
00:05:57,810 --> 00:06:00,960
here, when we write data, we need to encode it.

86
00:06:00,960 --> 00:06:03,480
So you're going to do DUT encode.

87
00:06:04,140 --> 00:06:07,260
We've UTF eight.

88
00:06:07,290 --> 00:06:16,080
So the same UTF eight as before, and it's very important here that the duct encode is directly on the

89
00:06:16,080 --> 00:06:16,590
string.

90
00:06:16,950 --> 00:06:17,280
OK.

91
00:06:17,700 --> 00:06:19,830
You don't do this, OK?

92
00:06:20,160 --> 00:06:25,710
You don't do that right and then don't include not do said what's right with the string?

93
00:06:25,710 --> 00:06:32,270
Don't encode and then you end up parenthesis here because so make sure you have the correct order for

94
00:06:32,280 --> 00:06:34,350
parentis as sucrose have been put on here.

95
00:06:35,280 --> 00:06:39,330
All right, so this is going to send hello from rosemary bye to the Albu.

96
00:06:39,720 --> 00:06:44,730
Maybe we can change the time sleep here, but once again, so we send this everything.

97
00:06:45,210 --> 00:06:47,180
Now the code is running on the original.

98
00:06:47,190 --> 00:06:48,540
I'm going to her undercook.

99
00:06:48,600 --> 00:06:50,300
Also on the Raspberry Pi.

100
00:06:50,370 --> 00:06:51,630
Let's see what we get.

101
00:06:53,900 --> 00:06:54,220
OK.

102
00:06:54,790 --> 00:06:56,680
OK, so it's running, actually.

103
00:06:57,010 --> 00:07:07,260
Let's do a controlled seat and let's have a printer you print, send a message to everyone.

104
00:07:08,170 --> 00:07:08,590
All right.

105
00:07:09,250 --> 00:07:12,600
So we can have a better idea of what's going on.

106
00:07:15,410 --> 00:07:18,860
Sandgate, send a message to send a message to, et cetera.

107
00:07:22,630 --> 00:07:30,520
No, well, what we did before when we actually sent some data from all of you to a Raspberry Pi, you

108
00:07:30,790 --> 00:07:37,330
could directly print the data we got on the terminal here on the show, but not we recent data from

109
00:07:37,330 --> 00:07:38,350
Raspberry Pi to our.

110
00:07:38,890 --> 00:07:45,250
And how can we actually check and print and debug these data we've received?

111
00:07:45,580 --> 00:07:51,190
We could do say, don't drink Ellen with the message.

112
00:07:52,060 --> 00:07:57,190
But the thing is that he and I don't know, we are using print Ellen to send message to the Raspberry

113
00:07:57,190 --> 00:07:58,410
Pi and also to David.

114
00:07:59,260 --> 00:08:05,110
So you can just use these to print the message, for example, on the same monitor because you're already

115
00:08:05,290 --> 00:08:08,350
using to out of communication with the Raspberry Pi.

116
00:08:08,800 --> 00:08:15,250
So that's one thing that is very important is that on the Arduino side, when when you receive something

117
00:08:15,250 --> 00:08:17,980
from Signal, don't just print it out.

118
00:08:18,040 --> 00:08:23,680
You can just print it like this if you want to test just with the Arduino and the same printer.

119
00:08:24,100 --> 00:08:29,890
But then when you communicate with the Raspberry Pi, don't just print some logs, some day books,

120
00:08:29,890 --> 00:08:30,340
for example.

121
00:08:30,340 --> 00:08:37,090
Here you should print same communication ready here if you print received some string when everything

122
00:08:37,090 --> 00:08:41,410
that you print actually is going to be sent back to the Raspberry Pi J, and that's something you don't

123
00:08:41,410 --> 00:08:43,060
want if it's just for Dimmock.

124
00:08:43,870 --> 00:08:49,960
So, well, we are left with this and when how to debug that?

125
00:08:50,470 --> 00:08:51,760
That's actually a good question.

126
00:08:52,060 --> 00:08:53,590
And there are different ways to do this.

127
00:08:53,590 --> 00:08:59,410
So first, of course, as I told you, you could just print what you received from we decided monitor,

128
00:08:59,470 --> 00:09:02,320
check if everything good you dress, remove the print.

129
00:09:03,190 --> 00:09:09,520
Another option would be to use an external component, for example, an LCD screen that you plug to

130
00:09:09,520 --> 00:09:10,250
your output.

131
00:09:10,270 --> 00:09:13,270
And that's actually what we're going to do in the following discourse.

132
00:09:13,600 --> 00:09:17,890
So you could receive some stuff from sale and print that's on the LCD screen.

133
00:09:18,370 --> 00:09:24,400
And what you can also see as a confirmation that things are working is that you'll receive data.

134
00:09:24,400 --> 00:09:29,020
Here is so let's run the script again, and let's look at the RNA world.

135
00:09:30,650 --> 00:09:38,900
And you can see the R X is blinking every one second, and I'm going to kill this guy and he's not blinking

136
00:09:38,900 --> 00:09:39,320
anymore.

137
00:09:39,740 --> 00:09:42,200
So are these for reception?

138
00:09:42,800 --> 00:09:49,100
So as you can see, the lady is on, it means that you are receiving data on the outer rim.

139
00:09:49,520 --> 00:09:49,870
All right.

140
00:09:49,880 --> 00:09:54,290
And now that we have seen how to send data only from one side to the other.

141
00:09:54,680 --> 00:09:58,640
Let's check how to do a bi directional communication.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,420 --> 00:00:05,700
Let's now see how to combine together the two sides of cellular communication.

2
00:00:06,330 --> 00:00:11,370
And we're going to start from the previous program where we send something from the Raspberry Pi to

3
00:00:11,370 --> 00:00:12,000
the Arduino.

4
00:00:12,270 --> 00:00:16,640
What we are going to do is we're going to send back the message to the Raspberry Pi.

5
00:00:16,770 --> 00:00:18,750
We have something that we are the kit.

6
00:00:18,780 --> 00:00:21,330
OK, so this program is already working.

7
00:00:21,510 --> 00:00:24,330
If you don't have this, please go back to the previous view.

8
00:00:24,630 --> 00:00:28,920
So what I'm going to do is I'm going to add something to the message here.

9
00:00:29,310 --> 00:00:36,480
For example, a counter that we're going to increase every time so we can see a progression on the message.

10
00:00:37,350 --> 00:00:44,490
So I'm going to create here and global viral and counter is equal to zero.

11
00:00:44,500 --> 00:00:46,050
Let's initialize it to zero.

12
00:00:46,830 --> 00:00:56,250
And so once we receive the message, what we are going to do is to do this, each is equal to so message.

13
00:00:56,970 --> 00:00:59,340
Plus, let's add a space.

14
00:01:00,150 --> 00:01:06,330
Plus, let's add to counter the counter is an integer, so we're going to need to convert it to a string.

15
00:01:06,330 --> 00:01:09,270
So we use string we've come to.

16
00:01:10,720 --> 00:01:18,100
So if we receive hello from Raspberry Bay, we're going to know transform it to hello from Raspberry

17
00:01:18,100 --> 00:01:21,160
Pi Zero and then one two three four two.

18
00:01:21,640 --> 00:01:28,210
So of course, if we want to increase the content we encounter plus plus after we have used it and then,

19
00:01:28,510 --> 00:01:31,210
well, here we receive some data.

20
00:01:31,810 --> 00:01:37,490
We transform the data and we can do cellular print elements, do and print.

21
00:01:37,540 --> 00:01:40,600
Then another time we've missed each.

22
00:01:41,380 --> 00:01:41,750
All right.

23
00:01:41,770 --> 00:01:44,460
And let's run that on the audio.

24
00:01:44,510 --> 00:01:45,550
It's this.

25
00:01:48,140 --> 00:01:53,690
Don't applauding and actually before we write anything on the Raspberry Pi side, we can already debug

26
00:01:53,690 --> 00:01:59,060
this program because, yeah, we would be able to see the message we've printed and which means that

27
00:01:59,270 --> 00:02:01,850
we can do with the say and monitor.

28
00:02:02,030 --> 00:02:02,270
OK.

29
00:02:02,570 --> 00:02:07,820
So I opened a site in moneyto and I'm going to send the stream, let's say ABC.

30
00:02:08,930 --> 00:02:12,710
And you can see I have ABC zero eight.

31
00:02:12,920 --> 00:02:15,290
I sent another stream, a random stream.

32
00:02:16,370 --> 00:02:18,320
I have one a hello.

33
00:02:18,770 --> 00:02:20,570
Hello to hello.

34
00:02:20,900 --> 00:02:21,260
Three.

35
00:02:22,040 --> 00:02:24,870
So we know that the original programs correct.

36
00:02:24,870 --> 00:02:25,520
Keep walking.

37
00:02:26,090 --> 00:02:27,590
So we send this train.

38
00:02:27,860 --> 00:02:28,670
We also have.

39
00:02:28,760 --> 00:02:29,560
So that's very important.

40
00:02:29,570 --> 00:02:31,970
We have new lines with New Line.

41
00:02:32,570 --> 00:02:34,880
Was going to add a backslash thing at the end.

42
00:02:35,060 --> 00:02:36,230
OK, and new line character.

43
00:02:36,650 --> 00:02:40,310
If you want to add nothing, you go with no line ending, but I'm going to keep new name.

44
00:02:40,850 --> 00:02:46,250
So you send a stream and you received a stream space and we will counter it increases every time.

45
00:02:46,850 --> 00:02:47,240
All right.

46
00:02:47,600 --> 00:02:50,240
So no, that we know it's working on the other side.

47
00:02:50,270 --> 00:02:52,100
Let's go to the Raspberry Pi sign side.

48
00:02:52,490 --> 00:02:53,180
And here what?

49
00:02:53,180 --> 00:02:55,070
We're going to send a message to the area.

50
00:02:55,700 --> 00:02:57,680
So let's keep yellow from Raspberry Pi.

51
00:02:57,950 --> 00:02:58,370
Great.

52
00:02:58,910 --> 00:03:01,670
And then we're going to receive this message.

53
00:03:02,390 --> 00:03:08,090
So as you can see here, we directly read the string we modified and we send it back.

54
00:03:08,090 --> 00:03:10,010
So it should be almost immediate.

55
00:03:10,130 --> 00:03:10,430
OK.

56
00:03:10,820 --> 00:03:14,840
So I'm going to stay just off to the right and then read the string.

57
00:03:15,260 --> 00:03:20,930
But before that, as let's see a way to be sure, we have received the data I'm going to do.

58
00:03:22,010 --> 00:03:33,290
While Sara notes in waiting is a lower or equal than zero, which means that here we check if we have

59
00:03:33,290 --> 00:03:36,350
received some byte if this is equal to zero.

60
00:03:36,890 --> 00:03:38,610
Well, I'm going to do time.

61
00:03:38,630 --> 00:03:39,920
Don't sleep.

62
00:03:41,270 --> 00:03:44,030
0.01 OK, so we're going to wait.

63
00:03:44,360 --> 00:03:52,070
Zero point zero one Second in an infinite loop as long as we haven't received any data once we have

64
00:03:52,070 --> 00:03:53,540
received data.

65
00:03:53,960 --> 00:03:56,720
What I'm going to do is I'm going to do Sara.

66
00:03:56,780 --> 00:04:00,830
So basically, the way loop is going to exit, I'm going to do set a red line.

67
00:04:03,290 --> 00:04:08,840
Don't decode we've UTF eight.

68
00:04:10,430 --> 00:04:21,950
But a trick, and I'm going to put that inside a viable named, let's say a response is equal to that

69
00:04:21,980 --> 00:04:25,910
and then let's sprint response.

70
00:04:26,990 --> 00:04:32,960
OK, so every one second we send a message to the other know we wait until we receive something.

71
00:04:33,680 --> 00:04:35,960
We read that thing we've printed.

72
00:04:36,470 --> 00:04:37,970
We go back to the beginning.

73
00:04:38,660 --> 00:04:43,760
What you can see on the rise of the right and I'm coming to that know is we also have a timeout is equal

74
00:04:43,760 --> 00:04:47,060
to one here when we open the cell communication.

75
00:04:47,630 --> 00:04:53,030
So basically, we set a one second timeout, the same that we have under Arduino.

76
00:04:53,030 --> 00:04:57,140
But on the, you know, we don't need to write it to have one second, if you don't.

77
00:04:57,140 --> 00:05:00,980
But this it means you have infinite timeout.

78
00:05:01,280 --> 00:05:04,400
And the timeout is actually not the timeout for everything.

79
00:05:04,550 --> 00:05:07,640
It's a timeout for when you read, we said.

80
00:05:07,970 --> 00:05:13,310
So when you use this red line, basically it's going to do the same thing as here.

81
00:05:13,610 --> 00:05:18,790
He's going to read the next line, OK, until basically this backslash and character.

82
00:05:19,490 --> 00:05:25,730
So if you receive something that ends with a backslash and character, it's going to return immediately.

83
00:05:26,210 --> 00:05:30,110
If not, it's going to wait at least one second.

84
00:05:30,410 --> 00:05:36,830
So normally, if you correctly put backslash in with print L.A., you should not have any timeout problem.

85
00:05:37,010 --> 00:05:40,400
But I have still included it here just in case.

86
00:05:40,400 --> 00:05:46,070
So we don't have an infinite timeout that's going to completely block our code if we have one error

87
00:05:46,220 --> 00:05:47,450
coming from the Arduino.

88
00:05:48,110 --> 00:05:48,380
OK.

89
00:05:48,500 --> 00:05:51,860
The Arduino is correctly running the codes.

90
00:05:52,070 --> 00:05:54,170
Let's bring the cool in the Raspberry Pi.

91
00:05:56,960 --> 00:05:58,570
Say, OK, send a message.

92
00:05:58,850 --> 00:05:59,300
You can see.

93
00:05:59,330 --> 00:06:02,880
And hello from Raspberry Pi one two three four.

94
00:06:02,900 --> 00:06:03,860
Etc., etc..

95
00:06:04,160 --> 00:06:04,700
Voice control.

96
00:06:04,720 --> 00:06:05,090
See?

97
00:06:08,020 --> 00:06:14,560
And you can see it is currently working, so now you have a bi directional communication, so great.

98
00:06:14,800 --> 00:06:21,400
Now you can communicate from Raspberry Pi to Arduino and from other the Raspberry Pi in the same program.

99
00:06:21,580 --> 00:06:28,960
And so to conclude on that, the examples we have seen here are actually super super simple, OK, but

100
00:06:28,960 --> 00:06:34,960
they are good to make you familiar with cellular in the following in the course, you will practice

101
00:06:34,960 --> 00:06:41,920
more real applications so that you can better understand how to use cellular in a more complex situation.

102
00:06:42,460 --> 00:06:48,820
There are so many possibilities, and so instead of listing them all here, which is going to be quite

103
00:06:48,820 --> 00:06:55,660
boring, well, you will simply discover them while going through the course and through the activities.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,210 --> 00:00:05,820
There is one more thing I wanted to add in this section, which I think is quite important.

2
00:00:06,270 --> 00:00:11,460
So basically what to do if the cellular communication can't be established?

3
00:00:12,060 --> 00:00:17,250
So let's say you have something like this is a wrong thought.

4
00:00:17,580 --> 00:00:18,720
The idea is not connected.

5
00:00:19,020 --> 00:00:22,560
You run the script and you have this error.

6
00:00:22,590 --> 00:00:24,720
We've so huge stuff.

7
00:00:25,110 --> 00:00:28,800
We basically say an exception could not open ports.

8
00:00:28,980 --> 00:00:29,220
OK.

9
00:00:30,300 --> 00:00:32,040
Something that is similar.

10
00:00:33,560 --> 00:00:40,280
Well, in this lesson, I'm first going to go through the different things you can do to debug and then

11
00:00:40,280 --> 00:00:45,120
you will see how to make your Python program automatically or retry to connect.

12
00:00:45,140 --> 00:00:49,190
So here through the app, you know when it fails the first time.

13
00:00:49,340 --> 00:00:49,670
All right.

14
00:00:49,670 --> 00:00:51,260
So let's start with the debugging part.

15
00:00:51,620 --> 00:00:58,470
First of all, make sure of cool that your Arduino board is correctly plugged to your Raspberry Pi with

16
00:00:58,470 --> 00:00:59,300
the USB cable.

17
00:00:59,780 --> 00:01:05,420
That sounds quite obvious, but it has happened to me a few times that I was like, Why is not working

18
00:01:05,420 --> 00:01:05,780
well?

19
00:01:06,080 --> 00:01:08,480
If you look on the side now, I do know is not connected.

20
00:01:08,510 --> 00:01:09,080
That's right.

21
00:01:09,350 --> 00:01:09,740
OK.

22
00:01:09,920 --> 00:01:15,830
Then, of course, make sure that you have the correct port here that you can check on the terminal.

23
00:01:15,830 --> 00:01:26,060
So we've alleged slush, then slash you white like this and check the properties here so you can connect,

24
00:01:26,060 --> 00:01:29,180
disconnect and find what is the difference in here.

25
00:01:29,180 --> 00:01:30,350
You're going to find this port.

26
00:01:31,360 --> 00:01:33,340
Make sure so you have the same both, right?

27
00:01:33,790 --> 00:01:39,520
OK, well, if you have a different body rate, the communication is going to be opened anyway, but

28
00:01:39,520 --> 00:01:42,430
then everything is going to not work basically.

29
00:01:42,880 --> 00:01:49,140
Also, wait a few seconds, OK, after opening the same communication so you don't get any garbage and

30
00:01:49,150 --> 00:01:50,830
reset the inputs buffer.

31
00:01:51,070 --> 00:01:56,020
So you start here the way loop with fresh input on the Raspberry Pi.

32
00:01:56,410 --> 00:02:03,070
And then when you run your program, well, if you are currently, for example, uploading the minutes,

33
00:02:03,310 --> 00:02:05,140
let's say used to say and monitor here.

34
00:02:05,500 --> 00:02:10,990
So I have to say and monitor, which is the of communication with the aluminum on this.

35
00:02:10,990 --> 00:02:13,330
But you can see on this boat knowing when I run.

36
00:02:15,140 --> 00:02:21,740
The script you can see, we have the same era when actually we don't have the exact same era we have

37
00:02:21,740 --> 00:02:29,060
there era that sees device, our resource is busy, y is busy because we are currently using just say,

38
00:02:29,060 --> 00:02:32,420
a moneyto, or maybe we are currently uploading your code.

39
00:02:32,880 --> 00:02:39,830
OK, so if I close, I say a monitor, and if I run again now it's going to work.

40
00:02:40,250 --> 00:02:40,630
Why?

41
00:02:40,670 --> 00:02:43,070
Because the sale is actually free.

42
00:02:45,520 --> 00:02:51,700
So make sure you have only one program at a time that is using cell communication so that can be applauding

43
00:02:52,150 --> 00:02:57,070
the sketch that can be using the same weneedto all that can be using the Python program here.

44
00:02:57,910 --> 00:02:58,220
All right.

45
00:02:58,240 --> 00:03:04,060
And one more thing also is, of course, make sure that the program here is correctly uploaded to the

46
00:03:04,060 --> 00:03:04,510
Arduino.

47
00:03:05,170 --> 00:03:11,680
Don't forget to upload it before you try to communicate with it and make sure you have this line of

48
00:03:11,800 --> 00:03:12,700
sight to begin.

49
00:03:13,390 --> 00:03:17,830
OK, if you don't begin to say it on the Arduino anyway, as I'm going to work on the rise of our brain,

50
00:03:18,280 --> 00:03:22,330
so we're basically for respect all of that, it should work fine.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:07,020
And now let's see how to make your Python program right, try to connect to sail after it has failed.

2
00:00:07,510 --> 00:00:09,000
That can be super useful.

3
00:00:09,720 --> 00:00:16,230
So basically when you start to program so any program where you to connect to the Arduino, we've sailed

4
00:00:16,230 --> 00:00:16,980
communication.

5
00:00:17,460 --> 00:00:22,610
You can choose what you want to do if the communication is not successfully working.

6
00:00:22,980 --> 00:00:25,200
So you can leave it like that, of course.

7
00:00:25,200 --> 00:00:28,350
And if it's not working, you're just going to get an error.

8
00:00:28,590 --> 00:00:30,810
And then you need to start the program again.

9
00:00:31,050 --> 00:00:32,520
All you can add a mechanism.

10
00:00:32,740 --> 00:00:38,640
OK, just on that line here to try again if it can't connect.

11
00:00:38,640 --> 00:00:40,890
And that's what I'm going to show you here.

12
00:00:41,190 --> 00:00:43,320
So how to do that?

13
00:00:43,500 --> 00:00:44,310
Well, first.

14
00:00:44,850 --> 00:00:48,180
So I'm going to unplug my Arduino so the ordinary is not connected.

15
00:00:48,390 --> 00:00:50,760
Let's see again, what error do we have?

16
00:00:51,000 --> 00:00:53,880
We have a cellular exception here.

17
00:00:54,240 --> 00:00:58,860
OK, so we are going to get this section.

18
00:00:59,250 --> 00:00:59,610
All right.

19
00:00:59,910 --> 00:01:01,170
So I'm going to try.

20
00:01:02,300 --> 00:01:12,840
What this and then accept, and the exception is cereal, that serial exception, you can use that.

21
00:01:12,860 --> 00:01:13,190
OK.

22
00:01:13,550 --> 00:01:19,190
So if you have a say on execution, which means that you have a problem when you connect, which can

23
00:01:19,190 --> 00:01:26,480
be, for example, that the board is not in all that the pot is already busy, then instead of exiting

24
00:01:26,480 --> 00:01:30,980
the program right now, you're going to go inside this code to handle the exception.

25
00:01:31,370 --> 00:01:35,840
And so what you want to do is that if you reach, don't you want to go back to him.

26
00:01:36,380 --> 00:01:40,550
And if you want to go back to here, then I'm going to use a while loop.

27
00:01:40,970 --> 00:01:43,340
So let's do while true.

28
00:01:44,780 --> 00:01:49,220
I'm going to put that inside to what I loop, of course, with a column here.

29
00:01:49,880 --> 00:01:54,620
So while true, it means that first we're going to enter these anyway.

30
00:01:54,950 --> 00:02:01,670
We're going to execute this code if this is successful, which means that we don't have the exception

31
00:02:01,970 --> 00:02:06,260
that in that case, what we want to do is we want to break out of the loop.

32
00:02:06,800 --> 00:02:07,100
OK.

33
00:02:07,460 --> 00:02:08,750
So I'm going to add Brent.

34
00:02:08,870 --> 00:02:15,130
So if this is successful, we directly go after the while loop and we go to timed out sleep.

35
00:02:16,070 --> 00:02:21,620
And if it is not successful, we are going to get the exception and the exception.

36
00:02:21,780 --> 00:02:22,940
Well, let's bring something.

37
00:02:22,940 --> 00:02:23,480
Let's see.

38
00:02:23,480 --> 00:02:34,310
Print could not connect to cellular trying again.

39
00:02:35,720 --> 00:02:41,590
And let's add, let's say time, don't sleep one.

40
00:02:41,600 --> 00:02:50,450
So if it's not working, we're going to bring something sleep for one second and then come back to the

41
00:02:50,450 --> 00:02:51,170
beginning of the loop.

42
00:02:51,710 --> 00:02:54,540
So we try again every one second.

43
00:02:55,070 --> 00:02:55,330
OK.

44
00:02:56,190 --> 00:03:03,350
I'm just going to add another point here so we can know directly after we have successfully connected

45
00:03:03,350 --> 00:03:05,510
that the clinician is OK.

46
00:03:05,780 --> 00:03:13,610
So let's see success fully connected to cellular.

47
00:03:15,980 --> 00:03:16,370
OK.

48
00:03:16,460 --> 00:03:18,830
And that should be it.

49
00:03:19,160 --> 00:03:22,040
So, no, I'm going to run this call.

50
00:03:22,520 --> 00:03:27,680
The Arduino is still disconnected so you can see what we're going to have.

51
00:03:27,680 --> 00:03:29,900
Is could not connect to, say, training again.

52
00:03:30,350 --> 00:03:33,950
And now I'm going to connect the Arduino, the prime minister, to running.

53
00:03:34,490 --> 00:03:39,670
And you can see successfully connected to cellular say, OK.

54
00:03:39,680 --> 00:03:42,300
And then we have the application which is starting.

55
00:03:42,350 --> 00:03:45,230
I press control C to kill the application.

56
00:03:46,270 --> 00:03:52,690
OK, so we this go, it's going to try again and again and again until the connection can be established,

57
00:03:53,170 --> 00:03:55,100
and that can be very useful.

58
00:03:55,120 --> 00:03:58,060
We're going to use that actually in the final project of this course.

59
00:03:58,330 --> 00:04:04,900
I'm not going to use it in every activity, OK, because that adds a bit of code if we want to just

60
00:04:04,900 --> 00:04:07,240
focus on one or two functionalities.

61
00:04:07,450 --> 00:04:13,210
But for the final project, we're going to use that and actually as an improvement that I'm not going

62
00:04:13,210 --> 00:04:15,430
to quote here, but you could try to do that.

63
00:04:15,880 --> 00:04:18,840
You could try to add a maximum number of trees.

64
00:04:18,850 --> 00:04:25,600
OK, let's say you want to try for maximum 10 times, which means that after 10 seconds, the problem

65
00:04:25,600 --> 00:04:26,830
is going to exit anyway.

66
00:04:26,860 --> 00:04:33,220
So you could add a mechanism here with another valuable that would keep the number of trees and continue

67
00:04:33,220 --> 00:04:37,090
to try again until you reach the maximum number of trees.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: PART 1 - Practice

1
00:00:00,180 --> 00:00:03,990
Let us know practice on celluloid with a few activities.

2
00:00:04,380 --> 00:00:10,740
What you have seen for now is super important because that's the foundation for any program we would

3
00:00:10,740 --> 00:00:12,420
right in the future of the course.

4
00:00:12,930 --> 00:00:18,540
But still, you may be a bit lost and wonder how you're going to apply this to your own project.

5
00:00:18,990 --> 00:00:22,830
Maybe you don't really know how to put this knowledge into a real application.

6
00:00:23,280 --> 00:00:27,730
And, well, don't worry, because that's exactly what I'm going to focus on from none.

7
00:00:28,170 --> 00:00:32,070
Apply this knowledge to real applications and improve the code.

8
00:00:32,280 --> 00:00:38,970
Step by step first through activities all the way up to the complete intercom project and the end of

9
00:00:38,970 --> 00:00:39,510
the course.

10
00:00:40,020 --> 00:00:41,370
All right and off talking.

11
00:00:41,370 --> 00:00:43,710
Let's just start with the first activity.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:02,730
This is the first activity of this goose.

2
00:00:03,120 --> 00:00:07,550
What I'm going to do now is to give you a challenge and explain some steps.

3
00:00:07,580 --> 00:00:09,900
I'll give you some tips to solve the challenge.

4
00:00:10,200 --> 00:00:13,110
In the next video, you will find the solution.

5
00:00:13,620 --> 00:00:19,440
Of course, I really encourage you to try to do the activity by yourself before you go to the solution.

6
00:00:19,680 --> 00:00:22,620
That's the only way to make progress.

7
00:00:23,070 --> 00:00:27,600
And if you have some doubts in free to rewatch some of the previous lessons.

8
00:00:28,230 --> 00:00:28,590
All right.

9
00:00:28,590 --> 00:00:36,510
So your challenge for this activity is to go up on a full will, often now on the Arduino from the Raspberry

10
00:00:36,510 --> 00:00:36,780
Pi.

11
00:00:37,500 --> 00:00:43,680
So on the other note, we actually well, we haven't created a secret yet, but we have the built in

12
00:00:43,680 --> 00:00:44,100
LCD.

13
00:00:44,100 --> 00:00:52,060
So you have the built in LTE, which is on thin 30 day.

14
00:00:52,180 --> 00:00:59,250
So you can first create, for example, the define for that and then use ping mode with 13 and output.

15
00:00:59,730 --> 00:01:08,460
And then what you are going to do in the void loop is basically to read string from cellular.

16
00:01:08,670 --> 00:01:14,250
So you're going to check if you have some data Wi-Fi Cellular available, you're going to read the stream.

17
00:01:14,790 --> 00:01:21,810
And then depending on the value of that string, you are going to go on up to anything.

18
00:01:22,080 --> 00:01:28,560
So of course, you will need to agree on a common value you, you here and the value you send to heat.

19
00:01:28,570 --> 00:01:31,710
OK, you need to send the same value that you're going to receive here.

20
00:01:31,890 --> 00:01:34,740
So, for example, that can be on end.

21
00:01:34,740 --> 00:01:39,660
That can be oh, so when you receive on from cellular, you were on energy.

22
00:01:39,870 --> 00:01:43,860
When you receive off from cellular, you pull of the energy.

23
00:01:44,160 --> 00:01:44,580
All right.

24
00:01:44,910 --> 00:01:49,220
So that would be the code on the Arduino now on the Raspberry Pi.

25
00:01:49,230 --> 00:01:53,940
So first you are going to need communication.

26
00:01:54,840 --> 00:01:56,610
So you have two choices do we need the communication?

27
00:01:56,610 --> 00:02:00,000
You can just open the cellular and see what's happening if it works or not.

28
00:02:00,280 --> 00:02:05,940
Or you can also use the try again mechanism that you have just got it in the previous section.

29
00:02:06,480 --> 00:02:10,110
And then will what you are going to do is you're going to send.

30
00:02:10,710 --> 00:02:12,510
So you're going to send on.

31
00:02:13,900 --> 00:02:21,790
All of and how you are going to send that will what you could do is, for example, send on every second

32
00:02:21,790 --> 00:02:25,810
and then send off and then send on again, send off everything, right?

33
00:02:26,020 --> 00:02:31,210
But what we are going to do here is we're going to use the input function.

34
00:02:31,220 --> 00:02:37,480
Okay, so the input function in Python, as a reminder, we ask for the user also in the terminal.

35
00:02:37,480 --> 00:02:40,420
We asked for the user to give some data.

36
00:02:40,420 --> 00:02:46,660
So for example, the string and then you can get the string into your code so you can put, for example,

37
00:02:46,660 --> 00:02:52,540
input we've select on all of this.

38
00:02:53,140 --> 00:02:54,580
We've maybe some quotes.

39
00:02:55,780 --> 00:02:59,410
So you can ask the user to select up and then you read that.

40
00:02:59,710 --> 00:03:06,840
And if the user gives on, you send on to the I don't know if the user gives off, you send off to the

41
00:03:06,850 --> 00:03:07,200
other.

42
00:03:07,420 --> 00:03:14,260
OK, so what you can do is put that input function inside like a true loop to make kind of avoid look

43
00:03:14,860 --> 00:03:20,260
like we have on our, you know, so you feel initialized communication and then you create a way look

44
00:03:20,710 --> 00:03:23,530
to continuously get the user input.

45
00:03:23,530 --> 00:03:27,790
And whenever you get the user input, you send that input to the audio.

46
00:03:28,330 --> 00:03:28,630
All right.

47
00:03:28,630 --> 00:03:35,740
So here what we are going to be able to do is to get user input on the Raspberry Pi to pull on hardware

48
00:03:35,740 --> 00:03:37,540
components on the avenue.

49
00:03:37,560 --> 00:03:37,990
All right.

50
00:03:38,620 --> 00:03:43,550
And now, once again, make sure to watch on the challenge before you watch the solution.

51
00:03:43,570 --> 00:03:43,870
OK.

52
00:03:44,080 --> 00:03:46,570
So spend some time working on this.

53
00:03:47,050 --> 00:03:52,480
However, don't stay stuck for hours and hours, OK, if you can't make it work.

54
00:03:52,810 --> 00:03:58,390
No worries at all because, well, for this, school activities I've picked can be quite challenging.

55
00:03:58,660 --> 00:04:04,090
So in this case, if you can't make it work, just what the solution and then try to do the activity

56
00:04:04,090 --> 00:04:05,260
again on your own.

57
00:04:05,470 --> 00:04:06,760
A bit later.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:06,310
This is the solution of the first activity of any schools where you have to put on a program of an Indian,

2
00:00:06,310 --> 00:00:11,670
you need to know from a user input you get from the Raspberry Pi and let's get started.

3
00:00:11,680 --> 00:00:20,440
So I have created a new project file in Python here on Sony Python II and also a new project on adding

4
00:00:20,460 --> 00:00:23,160
I can sort of start from a blank page.

5
00:00:23,550 --> 00:00:29,250
Now, the first thing before we even start to write some code is to define the protocol.

6
00:00:29,460 --> 00:00:34,560
So I've already done that actually for you in the first activity, and I'm going to talk about that

7
00:00:34,560 --> 00:00:36,330
just a few more seconds.

8
00:00:36,360 --> 00:00:36,660
OK.

9
00:00:37,560 --> 00:00:43,650
So as you can see, it's super important to know in advance what data you are going to send and receive

10
00:00:43,650 --> 00:00:44,820
from both sides.

11
00:00:44,970 --> 00:00:45,300
OK.

12
00:00:45,960 --> 00:00:48,330
As you can see here, we've on and off.

13
00:00:48,330 --> 00:00:51,390
We send that and we receive that.

14
00:00:52,050 --> 00:00:58,170
If we don't agree on both sides, OK to send the same data, then we are going to have some problems.

15
00:00:58,500 --> 00:01:04,140
OK, think about what data you need to send and receive and then write this in advance in, for example,

16
00:01:04,140 --> 00:01:05,910
the document in a comment.

17
00:01:06,540 --> 00:01:12,150
This is the protocol you're going to use, and for each application you are going to do what you are

18
00:01:12,150 --> 00:01:15,870
going to define a custom protocol before you write any code.

19
00:01:16,240 --> 00:01:20,960
Let's say, for example, here I want you to send early on in and off.

20
00:01:20,960 --> 00:01:28,380
Well, if I send this and if I try to read on, well, you can see that if I send any, I'm not going

21
00:01:28,380 --> 00:01:32,730
to be able to detect on because this is not the same string.

22
00:01:33,030 --> 00:01:38,280
So I need to make sure that I send something that is the same on both sides.

23
00:01:38,970 --> 00:01:39,380
All right.

24
00:01:39,390 --> 00:01:42,330
So now let's start with the Arduino code.

25
00:01:42,750 --> 00:01:47,690
OK, so once again, we start from Arduino, because that's simply easier to depict.

26
00:01:47,820 --> 00:01:52,860
We can start with this code debated within, say, a minute to make sure that the same communication

27
00:01:52,860 --> 00:01:54,420
is correctly working on that side.

28
00:01:54,420 --> 00:01:58,350
And then we can create the other side.

29
00:01:59,040 --> 00:02:01,950
So here we have two things to do.

30
00:02:01,980 --> 00:02:05,910
We have to set up the eddy and we have to set up the cell communication.

31
00:02:06,030 --> 00:02:08,000
I'm going to start with the eddy.

32
00:02:08,010 --> 00:02:11,400
OK, so we will start with Eddy and then we use the sail.

33
00:02:11,400 --> 00:02:16,470
And from this idea, we can directly make any blink so that we can check that the sail is correctly

34
00:02:16,470 --> 00:02:16,890
working.

35
00:02:17,220 --> 00:02:23,760
So let's create the defined energy being 13 for the 80.

36
00:02:23,760 --> 00:02:31,340
And then in the setup, I am going to do the mode, any B output.

37
00:02:32,490 --> 00:02:32,940
All right.

38
00:02:33,930 --> 00:02:37,590
So we have a defined we have set output modes for the LG.

39
00:02:37,590 --> 00:02:40,230
So now we can do digital rights on the ADT.

40
00:02:40,230 --> 00:02:41,640
We've high or low.

41
00:02:42,180 --> 00:02:45,090
And so when are we going to do digital rights?

42
00:02:45,090 --> 00:02:46,170
We have high and low.

43
00:02:46,170 --> 00:02:49,650
We are going to do that when we receive some data from the sale.

44
00:02:50,010 --> 00:02:56,310
So in the volume, what I'm going to do is I'm going to read from Ceja, but before I'm going to of

45
00:02:56,310 --> 00:03:06,230
course, initialize, say we say in the beginning, let's use these the paint and let's do while I'm

46
00:03:07,060 --> 00:03:09,480
saying I like this extension, not.

47
00:03:11,860 --> 00:03:17,650
So not needed, and you know, you know, but for example, if you have a Leonardo, a zero bolt, well,

48
00:03:17,830 --> 00:03:18,640
you're going to need that.

49
00:03:18,640 --> 00:03:19,930
So I'm going to put that anyway.

50
00:03:20,530 --> 00:03:22,180
All right, so is initialized.

51
00:03:23,080 --> 00:03:25,600
We have everything in the void said, not in a void loop.

52
00:03:25,870 --> 00:03:29,710
I'm going to if sailboat.

53
00:03:31,010 --> 00:03:38,630
They label like this with parentheses is greater, strictly greater than zero means that we have received

54
00:03:38,630 --> 00:03:43,460
some data on a sale, then we can read this and we are going to string.

55
00:03:44,390 --> 00:03:48,600
Let's create a C and D viable, which means command.

56
00:03:48,620 --> 00:03:52,430
So usually I prefer to write the full name for the variables.

57
00:03:52,910 --> 00:03:57,530
But when you have something like command with C and it's pretty clear, and because we are going to

58
00:03:57,530 --> 00:04:00,530
use the C and D valuable a lot in the following.

59
00:04:00,530 --> 00:04:03,050
So I'm just going to go with string symbol.

60
00:04:03,290 --> 00:04:05,510
OK, so Sonya, don't.

61
00:04:07,160 --> 00:04:15,200
Read Stream until and backslash with important single quotes.

62
00:04:16,580 --> 00:04:17,780
All right and cynical.

63
00:04:18,920 --> 00:04:25,370
So basically, we use the same function as before and now where we have the comment, so we will receive

64
00:04:25,370 --> 00:04:26,650
a comment from CEO.

65
00:04:27,020 --> 00:04:29,620
What we are going to do is we are going to take that coming.

66
00:04:29,630 --> 00:04:34,560
So if the content is equal to one.

67
00:04:35,450 --> 00:04:41,330
So if you want to do a comparison with string, with the other string, you can simply use the two equals

68
00:04:41,330 --> 00:04:41,690
sign.

69
00:04:42,590 --> 00:04:47,120
So if the command is own, what do we do?

70
00:04:47,780 --> 00:04:51,470
Well, we do digital rights.

71
00:04:54,360 --> 00:04:57,630
We've any dip in and hi.

72
00:04:58,770 --> 00:05:10,830
And if the command is off, so let's do it, and if actually command is off, we are going to do digital

73
00:05:11,730 --> 00:05:14,970
rights any thing we've lowered.

74
00:05:15,450 --> 00:05:18,020
So if we receive, we both on anything.

75
00:05:18,390 --> 00:05:26,940
If we receive off, we pull off the enemy and then I'm going to add an else because when you go to receive

76
00:05:26,940 --> 00:05:32,520
any string here, you could receive and you could receive off, but you could receive anything OK?

77
00:05:32,910 --> 00:05:34,790
You don't know what's going to happen.

78
00:05:34,800 --> 00:05:37,590
You don't know what the other side is going to send.

79
00:05:37,650 --> 00:05:37,970
OK.

80
00:05:38,280 --> 00:05:44,280
And as a basic principle, when you write some code like this, you don't trust the other side.

81
00:05:44,310 --> 00:05:44,630
OK.

82
00:05:45,090 --> 00:05:46,380
You are writing your eyesight.

83
00:05:46,380 --> 00:05:51,210
So that's good, but usually don't trust what the other side since you OK?

84
00:05:51,960 --> 00:05:53,520
So make sure to always check.

85
00:05:53,520 --> 00:05:58,020
You'll receive all you'll receive after you receive something, and it's not going to happen.

86
00:05:58,050 --> 00:06:05,040
OK, so if you receive something else, what are we going to do in that case is just, well, nothing.

87
00:06:05,790 --> 00:06:07,170
So I'm going to keep it like that for now.

88
00:06:07,180 --> 00:06:12,840
But for example, you could print an earring so you can send back an arrow, for example, or you can

89
00:06:12,840 --> 00:06:15,480
print an arrow on an LCD screen.

90
00:06:15,840 --> 00:06:20,940
All you could do in other behavior, for example, you could flush the input to buffer.

91
00:06:21,120 --> 00:06:23,310
We're going to do that a little bit later, OK?

92
00:06:23,700 --> 00:06:26,790
But finally, you can see we check if we have some data.

93
00:06:26,800 --> 00:06:30,780
If yes, we read the data, that's going to be our comment stream.

94
00:06:31,230 --> 00:06:34,620
We check if it's equal to us, then we do an action.

95
00:06:34,890 --> 00:06:39,110
We check if it's equal to of the nation and then everything else.

96
00:06:39,480 --> 00:06:43,050
We can do something else that we want with fun or we do nothing.

97
00:06:43,410 --> 00:06:43,740
All right.

98
00:06:43,860 --> 00:06:47,550
Let's not try this code and we don't need to write the python got.

99
00:06:47,550 --> 00:06:49,320
We can just stop this.

100
00:06:50,250 --> 00:06:53,550
Let's make sure that we have the other plugged.

101
00:06:55,100 --> 00:07:03,230
OK, let's oops, I have so the wrong bolt, so to either know, you know, and the port is correct.

102
00:07:04,340 --> 00:07:05,960
No, I'm going to upload this.

103
00:07:06,770 --> 00:07:11,450
So let's save it as activity one.

104
00:07:12,320 --> 00:07:13,130
OK, enter.

105
00:07:14,390 --> 00:07:15,170
Compiling.

106
00:07:17,900 --> 00:07:25,010
Applauding and now that the code on the other is running, what we can do is we can already try this

107
00:07:25,010 --> 00:07:25,740
behavior.

108
00:07:25,860 --> 00:07:28,250
We saved money, though, so we're going to open.

109
00:07:29,180 --> 00:07:34,460
So instead of having a Python program running on the Raspberry Pi, we just have to say money, don't

110
00:07:34,460 --> 00:07:37,130
run on the Raspberry Pi and we can send come on from there.

111
00:07:37,160 --> 00:07:37,550
All right.

112
00:07:37,850 --> 00:07:39,770
So make sure that you have the same button right here.

113
00:07:40,130 --> 00:07:40,460
OK.

114
00:07:41,710 --> 00:07:42,700
Jake, this is correct.

115
00:07:42,850 --> 00:07:43,300
All right.

116
00:07:43,660 --> 00:07:49,690
And then new line, because we are going to send a new line corrected again, so we don't need to write

117
00:07:49,690 --> 00:07:50,470
it manually.

118
00:07:50,740 --> 00:07:52,390
And then I'm going to send some comments.

119
00:07:52,400 --> 00:07:54,880
So let's say I send one.

120
00:07:55,870 --> 00:07:58,790
You can see the edit in here is poor.

121
00:07:58,820 --> 00:08:00,460
Oh no, I sent off.

122
00:08:01,270 --> 00:08:02,840
The enemy is put off.

123
00:08:03,280 --> 00:08:06,550
I send on again and they put it on the editing.

124
00:08:06,730 --> 00:08:07,530
Not if I send.

125
00:08:07,550 --> 00:08:09,880
Let's set the on, which is not correct.

126
00:08:10,280 --> 00:08:12,340
Nothing's going to happen in the US.

127
00:08:13,000 --> 00:08:14,050
Nothing is going to happen.

128
00:08:14,320 --> 00:08:15,370
Any other thing.

129
00:08:15,790 --> 00:08:16,690
Nothing is going to happen.

130
00:08:16,690 --> 00:08:23,560
You can see we still have the X, which is blinking because we are receiving some data, but then the

131
00:08:23,560 --> 00:08:30,370
data is processed in the code and goes directly to the end, which does nothing.

132
00:08:30,400 --> 00:08:30,700
OK.

133
00:08:30,940 --> 00:08:34,450
So you have to send exactly the on and off command to do something.

134
00:08:34,720 --> 00:08:40,290
And you can see that with our experimentation, the behavior is correct here.

135
00:08:40,600 --> 00:08:47,200
So we can know that the original code is correct and now we can write the code on the Raspberry Pi.

136
00:08:48,130 --> 00:08:52,780
So let's start by initializing the communication so I'm going to go with.

137
00:08:53,080 --> 00:08:59,320
So this is a of Python three for the interpreter.

138
00:08:59,590 --> 00:09:02,010
And then let's import Cellule.

139
00:09:02,050 --> 00:09:04,900
Let's also import time because we're going to need that library.

140
00:09:06,610 --> 00:09:15,040
And I am going to do, sir is equal to say, I'll do it so you'll weave the pork, so the pot is still

141
00:09:15,040 --> 00:09:15,760
the same for me.

142
00:09:16,500 --> 00:09:16,870
It's large.

143
00:09:16,870 --> 00:09:17,910
Dave slash you.

144
00:09:17,950 --> 00:09:21,160
Why ACM zero?

145
00:09:21,700 --> 00:09:23,360
OK, the border rate very important.

146
00:09:24,040 --> 00:09:25,630
Exact same here.

147
00:09:26,620 --> 00:09:28,300
And then there are time out.

148
00:09:29,230 --> 00:09:34,360
Let's put one cigarette went for this case.

149
00:09:34,360 --> 00:09:39,190
We don't really need the time out here in the retail world because we're not going to read anything

150
00:09:39,460 --> 00:09:40,320
but still pretty.

151
00:09:40,740 --> 00:09:47,560
Anyway, so here we open the sale communication and we get the sale in the object here.

152
00:09:48,430 --> 00:09:54,970
I'm not going to do the retry code just to keep it simple for this activity, but you can do it if you

153
00:09:54,970 --> 00:09:55,480
want to.

154
00:09:55,840 --> 00:09:58,530
So once we have this, I'm going to do it time.

155
00:09:58,540 --> 00:10:01,870
Don't sleep with three seconds.

156
00:10:01,990 --> 00:10:07,740
OK, wait, because this is going to connect to the albino and he only know.

157
00:10:07,780 --> 00:10:12,070
We know it's going to restart the program, so we make sure that we have spent enough time.

158
00:10:12,080 --> 00:10:16,190
So the Arduino is right, and then we're going to do so.

159
00:10:16,540 --> 00:10:27,340
Don't reset input buffer, which is, well, not needed as well here because we don't have anything

160
00:10:27,340 --> 00:10:30,340
in the input buffer because the Arduino doesn't send anything.

161
00:10:30,340 --> 00:10:36,250
But still, I'm going to keep it for best practice because we're going to initialize the sail the same

162
00:10:36,250 --> 00:10:36,570
way.

163
00:10:36,580 --> 00:10:37,180
Everything.

164
00:10:37,210 --> 00:10:37,540
All right.

165
00:10:38,050 --> 00:10:40,630
And let's see print sail.

166
00:10:40,870 --> 00:10:43,330
OK, ladies.

167
00:10:43,750 --> 00:10:48,630
Now what we can do is we can do our way through.

168
00:10:48,880 --> 00:10:49,210
OK.

169
00:10:50,050 --> 00:10:54,700
So this is kind of the void setup of the Raspberry Pi, and this is the whole look.

170
00:10:54,910 --> 00:10:55,300
All right.

171
00:10:56,230 --> 00:10:57,580
Voice it the way you look.

172
00:10:57,610 --> 00:10:58,810
Voice into Android.

173
00:10:59,470 --> 00:11:00,030
So why?

174
00:11:00,100 --> 00:11:00,520
True.

175
00:11:00,940 --> 00:11:05,110
So what I'm going to do is, of course, I'm going to do a try and exit.

176
00:11:05,620 --> 00:11:14,500
So let's just press here, try exit, keyboard, interrupt.

177
00:11:15,400 --> 00:11:18,730
And when we press control, see, I'm going to do so.

178
00:11:18,730 --> 00:11:29,690
I'm going to see print closed cellular communication and said, don't close before we exit the program.

179
00:11:29,710 --> 00:11:30,070
OK.

180
00:11:31,120 --> 00:11:36,580
So again, this is going to be the same every time and in the way, true, what do we do?

181
00:11:36,610 --> 00:11:42,460
So this is the behavior of our voice loop when basically we want the user input and from that user input,

182
00:11:42,460 --> 00:11:44,170
we send data to the ROV.

183
00:11:44,530 --> 00:11:50,200
So I am going to do, let's say, user input is equal to inputs.

184
00:11:50,860 --> 00:11:51,190
OK.

185
00:11:51,550 --> 00:11:55,120
I can put some text here to send some instruction.

186
00:11:55,510 --> 00:12:02,220
So, for example, select on or off.

187
00:12:02,830 --> 00:12:03,280
All right.

188
00:12:03,850 --> 00:12:06,220
With a call and space.

189
00:12:06,820 --> 00:12:08,860
So we have this instruction.

190
00:12:09,100 --> 00:12:12,910
The input is going to block the program until we give something.

191
00:12:13,210 --> 00:12:17,650
Then we press enter and we're going to get that inside the user input volume.

192
00:12:18,010 --> 00:12:24,100
Once we have this, we could directly send the string to the Albarino because we validate the data here

193
00:12:24,100 --> 00:12:24,550
also.

194
00:12:24,790 --> 00:12:33,580
But we can also see, for example, if user input and how to validate this, well, we want it to be

195
00:12:33,580 --> 00:12:34,660
on off.

196
00:12:34,810 --> 00:12:36,940
So what we can do is in.

197
00:12:38,700 --> 00:12:41,110
All of.

198
00:12:42,270 --> 00:12:48,660
So basically, even a user input is in that list, which contains two values.

199
00:12:49,440 --> 00:12:53,730
Then we're going to do something, if not so else.

200
00:12:54,180 --> 00:12:55,560
Basically, we don't do anything.

201
00:12:55,560 --> 00:12:57,080
So here I'm not going to put an answer.

202
00:12:57,960 --> 00:13:05,790
So if the user input is correct, then we do not right and well, actually, I'm just going to send

203
00:13:05,790 --> 00:13:06,620
user input.

204
00:13:06,660 --> 00:13:09,030
I'm going to add backslash in, OK?

205
00:13:09,240 --> 00:13:17,750
So let's do, for example, steer to sense, which you can string to send equal to user input.

206
00:13:18,810 --> 00:13:20,910
Plus backslash in.

207
00:13:21,360 --> 00:13:21,690
OK.

208
00:13:22,080 --> 00:13:23,940
And we sent Estia.

209
00:13:25,540 --> 00:13:29,200
Sent so we were right, asked to send that code.

210
00:13:30,130 --> 00:13:39,640
We've UTF eight can make shoot to do the encode on the string and not on the write function during bottom.

211
00:13:39,650 --> 00:13:45,890
So you should have open parentheses here up in front of this here and close and close at the end.

212
00:13:45,910 --> 00:13:48,520
Well, it seems that pretty much it.

213
00:13:48,790 --> 00:13:54,910
Maybe we could add a print queue so we can see under the Raspberry Pi side what's happening?

214
00:13:55,210 --> 00:13:57,190
So let's see.

215
00:13:57,850 --> 00:13:59,920
It's printed print.

216
00:14:00,940 --> 00:14:04,540
Send comments to admin.

217
00:14:05,320 --> 00:14:10,780
We've so plus using put.

218
00:14:13,010 --> 00:14:18,650
So we know that we are sending a command to the original and then we can check if that works.

219
00:14:18,980 --> 00:14:22,600
And if we correctly bring the regiment, we already know it works.

220
00:14:22,880 --> 00:14:24,770
So let's run that.

221
00:14:25,790 --> 00:14:29,720
I'm going to click on Run here and let's see this as.

222
00:14:31,370 --> 00:14:36,100
Activity one that bite.

223
00:14:36,410 --> 00:14:40,280
OK, so we have that activity, one sketch for, I don't know.

224
00:14:40,310 --> 00:14:44,640
And activity one by some fine, that's research into.

225
00:14:45,860 --> 00:14:47,840
And let's see what we got here.

226
00:14:48,470 --> 00:14:48,770
OK.

227
00:14:49,100 --> 00:14:50,060
Sail OK.

228
00:14:50,520 --> 00:14:52,000
Select on off.

229
00:14:52,010 --> 00:14:53,480
You can see the prime minister now.

230
00:14:54,050 --> 00:14:58,720
The original has a reboot and I'm going to send on.

231
00:14:59,660 --> 00:15:03,020
And you can see we have the energy here, which is brought on.

232
00:15:03,260 --> 00:15:04,230
I sent off.

233
00:15:04,790 --> 00:15:06,230
The energy is off.

234
00:15:06,500 --> 00:15:07,940
Let's send anything else.

235
00:15:07,940 --> 00:15:09,110
Let's set it on.

236
00:15:09,860 --> 00:15:10,820
Nothing happens.

237
00:15:11,140 --> 00:15:12,170
That's an Onegin.

238
00:15:12,470 --> 00:15:13,040
It works.

239
00:15:13,850 --> 00:15:18,590
I know if I press control, see you can see close cellular communication.

240
00:15:19,310 --> 00:15:19,640
All right.

241
00:15:19,640 --> 00:15:21,980
So that's the end of the first activity of this course.

242
00:15:22,160 --> 00:15:25,700
No, if you have a slightly different code than me on both sides.

243
00:15:26,030 --> 00:15:28,700
And if it still works well, that's great too.

244
00:15:28,700 --> 00:15:29,030
OK?

245
00:15:29,240 --> 00:15:30,950
This is my solution.

246
00:15:30,950 --> 00:15:33,090
Is just one possible solution.

247
00:15:33,110 --> 00:15:33,450
All right.

248
00:15:33,480 --> 00:15:35,600
It is not the solution.

249
00:15:36,200 --> 00:15:42,380
And if you couldn't find a solution by yourself, well, don't me, because I told you, the activities

250
00:15:42,380 --> 00:15:48,440
here in this course are quite challenging, and what they recommend you to do is to actually come back

251
00:15:48,440 --> 00:15:54,800
to this activity, maybe in one or two days or one week, just watch the introduction of the activity

252
00:15:54,800 --> 00:15:57,890
again and then do it by yourself.

253
00:15:57,890 --> 00:16:02,600
And you will see that's going to be much easier for you and you're going to get more understanding.

254
00:16:03,020 --> 00:16:03,350
All right.

255
00:16:03,360 --> 00:16:05,150
And now let's go to the next activity.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:06,300
This is activity two of these schools, and in this new activity, what you are going to do is you're

2
00:00:06,300 --> 00:00:13,170
going to send some data from the Arduino to the Raspberry Pi and then process that data on the Raspberry

3
00:00:13,170 --> 00:00:16,470
Pi and send back something to the audience.

4
00:00:16,530 --> 00:00:23,760
OK, so that's something new because what we've done before is to just send data directly from one side

5
00:00:23,760 --> 00:00:29,130
to the other one, all to send some data from the Raspberry Pi and response from the Arduino.

6
00:00:29,370 --> 00:00:34,680
Here we initiate the communication from the albino and we respond from the Raspberry Pi.

7
00:00:34,890 --> 00:00:38,950
But as you will see, that is not more complicated than what we have done before.

8
00:00:39,570 --> 00:00:43,890
So if you correctly understood to previous things, that's going to be OK for you.

9
00:00:44,430 --> 00:00:46,410
So what is your challenge?

10
00:00:46,410 --> 00:00:51,030
Your challenge is to send some temperature from the original to the Raspberry Pi.

11
00:00:51,300 --> 00:00:52,720
So the temperature here.

12
00:00:52,740 --> 00:00:56,460
We don't have a temperature sensor and I'm not going to use one.

13
00:00:56,460 --> 00:00:59,760
We are just going to fake some temperatures, OK, for this example.

14
00:01:00,180 --> 00:01:05,940
And so you send a temperature from the Arduino and then you're going to check this temperature in the

15
00:01:05,940 --> 00:01:08,160
Raspberry Pi in the Python program.

16
00:01:08,400 --> 00:01:14,780
And if this temperature is lower than a certain threshold, you are going to put on the 80.

17
00:01:15,090 --> 00:01:20,670
So the built in entity on the don't if the temperature is above the threshold, you're going to pull

18
00:01:20,710 --> 00:01:22,200
off the end.

19
00:01:23,220 --> 00:01:35,730
So on the outside is to send temperature and then on parole is to receive data from cell and blue upon

20
00:01:36,990 --> 00:01:38,420
of the end.

21
00:01:40,020 --> 00:01:46,590
So he I have given you some code structure you can already use.

22
00:01:47,040 --> 00:01:51,570
So basically to send the temperature, let's say we want to send the temperature every one second,

23
00:01:51,570 --> 00:01:53,220
so every 1000 millisecond.

24
00:01:53,550 --> 00:01:58,740
We are not going to use the delay because if we use the delay in the volume and then we try to receive

25
00:01:58,740 --> 00:02:04,110
data from cellular when the delay is going to block the program and we are going to receive data from

26
00:02:04,110 --> 00:02:04,560
cell.

27
00:02:05,070 --> 00:02:06,060
Some delay, actually.

28
00:02:06,120 --> 00:02:11,340
OK, so if you block the problem for one thing, then you're going to have a delay of maximum one second

29
00:02:11,610 --> 00:02:13,340
to receive data from the site.

30
00:02:13,350 --> 00:02:14,400
And you don't want that.

31
00:02:14,400 --> 00:02:17,250
You want to receive data as soon as it is here.

32
00:02:17,310 --> 00:02:17,640
OK?

33
00:02:17,910 --> 00:02:21,510
So what we're going to do is we're going to do some kind of multitasking.

34
00:02:21,840 --> 00:02:26,160
And as a recap, I have shown you is here for multitasking.

35
00:02:26,160 --> 00:02:28,160
So basically, that's very simple.

36
00:02:28,170 --> 00:02:29,040
Can you create?

37
00:02:29,400 --> 00:02:36,090
So for an action you want to do you create this viable and long with the last time you have done the

38
00:02:36,090 --> 00:02:40,000
action, you initialize it to zero minutes doesn't matter.

39
00:02:40,020 --> 00:02:46,800
And then you have an action delay, which is a delay you want to spend between two actions that you

40
00:02:46,800 --> 00:02:49,410
do so here or you put 1000 milliseconds.

41
00:02:50,040 --> 00:02:56,310
Then in the volume, you get the current time with minutes and then you take the difference between

42
00:02:56,310 --> 00:02:57,060
the current time.

43
00:02:57,060 --> 00:02:59,910
So the time now and the last time you have done the action.

44
00:03:00,220 --> 00:03:01,710
This give you a duration.

45
00:03:02,100 --> 00:03:06,300
And if this duration is greater than the action delay, then you can do the action.

46
00:03:06,420 --> 00:03:12,870
And of course, you added the last time the action was done to do your own thing and then you do the

47
00:03:12,870 --> 00:03:13,210
action.

48
00:03:13,230 --> 00:03:18,870
So here you can select a random number for the temperature and send it to the Senate.

49
00:03:19,260 --> 00:03:27,750
And here on parallel, you can do so three cellular, basically.

50
00:03:28,950 --> 00:03:30,300
So this is going to be very fast.

51
00:03:30,300 --> 00:03:31,350
This is going to be very fast.

52
00:03:31,350 --> 00:03:33,510
So it's going to go very, very, very fast.

53
00:03:33,510 --> 00:03:39,630
So it's just like if you were doing some kind of multi-threading on your RV and to get the random number,

54
00:03:39,630 --> 00:03:42,360
I have given you the random function here of the RV.

55
00:03:42,540 --> 00:03:46,800
So basically, if you want the random number between, for example, five and twenty five, you just

56
00:03:46,800 --> 00:03:49,260
do random five come up tonight.

57
00:03:49,800 --> 00:03:53,190
I'm going to use Celsius degrees here, but doesn't really matter.

58
00:03:53,490 --> 00:03:58,710
So if you do this, the random number will be between five and twenty five known the Raspberry Pi.

59
00:03:58,710 --> 00:04:06,540
What you going to do is read cellular, OK, and then you're going to receive some temperatures to receive

60
00:04:07,930 --> 00:04:10,430
the number and then process that number.

61
00:04:10,440 --> 00:04:18,620
So basically, you're going to see if no is, for example, lower than 15, you're going to have to

62
00:04:18,620 --> 00:04:23,550
work on the energy and else you are going to pull off the energy.

63
00:04:24,090 --> 00:04:32,550
So in your own kind of void loop on the Raspberry Pi you first read from cellular, and once you have

64
00:04:32,550 --> 00:04:36,930
gotten some data, you process the data and you write directly to the algae.

65
00:04:37,170 --> 00:04:44,430
OK, and well, what I'm going to do is I'm going to actually get the call from activity one.

66
00:04:44,910 --> 00:04:45,840
I'm going to get that.

67
00:04:46,080 --> 00:04:49,210
I'm not going to read or write everything in this case.

68
00:04:49,230 --> 00:04:50,040
Why is that?

69
00:04:51,110 --> 00:04:54,320
Because simply, we're going to need to use this.

70
00:04:54,800 --> 00:04:59,720
We are going to need to initialize the same communication with the exact same code.

71
00:04:59,960 --> 00:05:03,090
And then we have the exact same way true, true.

72
00:05:03,260 --> 00:05:06,950
I'm just going to remove all of that's let's put bus here.

73
00:05:07,610 --> 00:05:12,650
And while this code is going to be the same, okay, for the previous activity and this one, so I'm

74
00:05:12,650 --> 00:05:20,480
not going to write it every time because we have basically here 14 lines of code that are identical.

75
00:05:20,960 --> 00:05:21,290
All right.

76
00:05:21,560 --> 00:05:22,970
And now we'll see you in the next.

77
00:05:23,300 --> 00:05:25,070
Listen, the solution?



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:06,480
This is the solution of the activity to where you have to send some random temperature from the Albarino

2
00:00:06,870 --> 00:00:13,290
process that's in the Raspberry Pi so that you can choose to put on power of the enemy.

3
00:00:13,470 --> 00:00:17,610
If, for example, you can pull under any heat, the temperature is too low.

4
00:00:18,090 --> 00:00:20,910
So let's start with the advent of side once again.

5
00:00:21,810 --> 00:00:23,010
I'm going to remove that.

6
00:00:24,060 --> 00:00:26,950
So I already have this.

7
00:00:27,300 --> 00:00:27,720
OK.

8
00:00:28,090 --> 00:00:29,640
Unsigned long last time.

9
00:00:30,030 --> 00:00:35,160
Actually, I'm going to move this and just rename it last time.

10
00:00:36,090 --> 00:00:39,420
That's the temperature sent.

11
00:00:39,570 --> 00:00:39,900
OK.

12
00:00:40,290 --> 00:00:41,820
Which makes more sense.

13
00:00:41,940 --> 00:00:46,950
And then I'm going to do temperature since.

14
00:00:51,730 --> 00:00:53,080
And let's keep one thing.

15
00:00:53,280 --> 00:01:00,070
OK, so now, boy, look, I'm saying long, we get the time now with Mills and we check even the time.

16
00:01:00,070 --> 00:01:07,780
No, minus the last time temperature scent is greater than temperature and delay.

17
00:01:08,560 --> 00:01:14,400
And in that case, we don't forget the last time temperature sent to the time now.

18
00:01:14,410 --> 00:01:20,320
So basically this year, this good heat is going to be called every one second.

19
00:01:20,680 --> 00:01:22,090
And we don't blog the boy.

20
00:01:22,100 --> 00:01:30,940
Look, we did so to get the temperature I'm going to do in temperature is equal to.

21
00:01:31,300 --> 00:01:34,120
And it's using the random five to 25.

22
00:01:35,850 --> 00:01:36,900
And it's remove that.

23
00:01:39,070 --> 00:01:45,220
And what we're going to do now is we're going to send these to the sale, so I'm going to do in the

24
00:01:45,220 --> 00:01:48,010
void, set the sale, but begin.

25
00:01:49,550 --> 00:01:51,110
So same code.

26
00:01:52,200 --> 00:01:56,960
And then why so young like this?

27
00:01:59,290 --> 00:02:05,110
And here I can say that print, Alan, we've temperature.

28
00:02:08,160 --> 00:02:08,550
All right.

29
00:02:08,910 --> 00:02:14,910
Let's actually test this quote, so I'm going to do applaud activity

30
00:02:17,520 --> 00:02:17,790
to.

31
00:02:22,140 --> 00:02:23,010
Don't applauding.

32
00:02:23,250 --> 00:02:31,350
And how to take this go, too, I just open Sam Alito and let's see what we receive 12, 12, 14, 18,

33
00:02:31,740 --> 00:02:40,530
23, 15, 17, nine so you can see it's currently working, will receive a random number between five

34
00:02:40,530 --> 00:02:42,270
and 25 every second.

35
00:02:42,480 --> 00:02:47,400
OK, so the first part of the record is done now in parallel.

36
00:02:47,500 --> 00:02:53,390
So I think parallel because we're going to do the two actions one after the other, but very fast.

37
00:02:53,400 --> 00:02:55,770
So it's just like we are doing them in Poland.

38
00:02:56,370 --> 00:03:00,900
I'm going to do if I say I'm not available

39
00:03:03,900 --> 00:03:05,220
is greater than zero.

40
00:03:07,800 --> 00:03:13,500
So if we have received some data, what we're going to do is the same thing we did in the previous activity.

41
00:03:13,740 --> 00:03:19,290
So I'm going to do the very first stream command is equal to say, I'll do it.

42
00:03:20,070 --> 00:03:26,370
Read Stream until vaccination with one single quote.

43
00:03:26,820 --> 00:03:37,620
And then if command is equal to one, we are going to put on the entity and it's if command is equal

44
00:03:37,620 --> 00:03:38,010
to.

45
00:03:39,230 --> 00:03:50,120
If we pull of the energy and then it's we can process the other comment and, for example, print an

46
00:03:50,120 --> 00:03:56,690
era or something like, OK, now for the energy we need to initialize energy.

47
00:03:56,690 --> 00:03:58,910
So it's great to define energy.

48
00:03:59,420 --> 00:04:05,300
Being 13 units do so I can do the pin mode before after sale.

49
00:04:05,300 --> 00:04:13,490
It doesn't really matter heat be mode, energy being with output.

50
00:04:15,260 --> 00:04:19,150
And here I do digital, right?

51
00:04:19,760 --> 00:04:31,130
I think we've high because we put in digital right energy being low because we put all of the energy.

52
00:04:31,430 --> 00:04:36,170
OK, so we have this action and this action running separately.

53
00:04:36,170 --> 00:04:38,630
As you can see here, we send data.

54
00:04:39,240 --> 00:04:41,930
We've seen the print in and we receive data.

55
00:04:41,930 --> 00:04:44,450
We've secured the string until.

56
00:04:44,870 --> 00:04:46,820
But the two are not directly linked.

57
00:04:47,180 --> 00:04:50,420
We don't just send data when we receive data, OK?

58
00:04:50,600 --> 00:04:52,880
We have separated the two actions.

59
00:04:53,510 --> 00:04:55,510
Let's upload this book to the audio.

60
00:04:58,400 --> 00:05:01,790
Again, what you can do, for example, is you can just open Sam Alito.

61
00:05:02,030 --> 00:05:05,060
You're going to see that you'll receive some numbers, OK?

62
00:05:05,270 --> 00:05:12,770
And let's just give on and let's see that end is OK, that's working.

63
00:05:14,450 --> 00:05:21,590
And as you may see, they're random here is maybe not that's random because we have the same data as

64
00:05:21,590 --> 00:05:22,010
before.

65
00:05:22,280 --> 00:05:26,110
So you couldn't make it more random, but I'm not going to spend time on this.

66
00:05:26,120 --> 00:05:28,430
OK, that's outside of the scope of discourse.

67
00:05:28,580 --> 00:05:30,710
If you want, you can search more about this space.

68
00:05:31,490 --> 00:05:31,760
All right.

69
00:05:31,760 --> 00:05:33,470
So the original code is dumb.

70
00:05:34,340 --> 00:05:36,210
Let's go to the Raspberry Pi sign.

71
00:05:36,860 --> 00:05:36,990
Okay.

72
00:05:37,050 --> 00:05:39,650
So we read from sale and we receive a number.

73
00:05:40,130 --> 00:05:50,180
So if we want to read from cellular, what we are going to do is to do if say that in waiting is greater

74
00:05:50,240 --> 00:05:51,050
than zero.

75
00:05:51,320 --> 00:05:53,290
And here no parentheses.

76
00:05:53,300 --> 00:05:56,090
OK, you have parentheses here.

77
00:05:56,720 --> 00:05:59,420
We're still a available no parentheses here.

78
00:06:00,650 --> 00:06:04,890
So if we have received something, then we read that thing.

79
00:06:04,940 --> 00:06:10,220
OK, so let's see temperature is equal to.

80
00:06:11,350 --> 00:06:13,300
Set that red line.

81
00:06:14,630 --> 00:06:20,870
Don't decode with UTF eight.

82
00:06:22,430 --> 00:06:24,160
And it's true.

83
00:06:26,930 --> 00:06:31,880
OK, so the same thing we did before, so we were in the line we decoded because he eats bytes, so

84
00:06:31,880 --> 00:06:38,630
we decode it into a string and we remove any other special character we have at the end.

85
00:06:39,020 --> 00:06:47,180
And what I'm going to do is I'm also going to cast this into an integer, OK, because we want to process

86
00:06:47,180 --> 00:06:50,960
the temperature as an integer so iconoclastic as an integer.

87
00:06:51,500 --> 00:06:55,130
And to do that, I simply do it and I put everything in the parentheses.

88
00:06:55,820 --> 00:07:06,560
And no, if the temperature is lower serotonin 15, let's see, then we are going to pull on the enemy.

89
00:07:07,400 --> 00:07:12,380
So it's the Committee on Energy and then else.

90
00:07:12,830 --> 00:07:16,430
So basically, the temperature is greater or equal than 15.

91
00:07:16,790 --> 00:07:21,270
We are going to pull off any.

92
00:07:21,390 --> 00:07:24,200
So let's actually do a print print.

93
00:07:25,950 --> 00:07:30,890
Don't try to lower than 15.

94
00:07:32,950 --> 00:07:35,610
The UN and here.

95
00:07:37,510 --> 00:07:37,990
Prince.

96
00:07:39,750 --> 00:07:47,280
Temperature lower, greater than 15.

97
00:07:48,270 --> 00:07:49,350
Any of.

98
00:07:51,060 --> 00:07:56,040
And then, of course, we sent the command, so the command is on and off.

99
00:07:56,280 --> 00:08:06,720
OK, so say don't write we've done and backslash end, don't encode.

100
00:08:07,260 --> 00:08:16,060
We've UTF eight like this and then I'm going to copy this here in the end.

101
00:08:16,410 --> 00:08:19,110
And instead of on, we sent off.

102
00:08:19,950 --> 00:08:26,010
So as you can see the structure here, so we continue with our line at trousseau, the infinite loop.

103
00:08:26,430 --> 00:08:29,670
If we have received some data, we read that data.

104
00:08:30,180 --> 00:08:31,440
So we guessed it as an.

105
00:08:31,740 --> 00:08:37,230
So here it's very important, as you see here, that we also have defined a protocol.

106
00:08:37,470 --> 00:08:44,850
The protocol is simply that here we send that number, we receive a number, OK, and here we send on

107
00:08:45,120 --> 00:08:45,840
and off.

108
00:08:45,840 --> 00:08:48,030
Here we will receive on and off.

109
00:08:48,150 --> 00:08:48,420
OK.

110
00:08:48,930 --> 00:08:53,790
So on both sides, we know what we receive and what we think.

111
00:08:54,510 --> 00:08:54,780
OK.

112
00:08:54,810 --> 00:08:55,790
Let's know.

113
00:08:55,830 --> 00:08:56,520
Try this code.

114
00:08:56,520 --> 00:08:59,290
So it's already uploaded on the Arduino.

115
00:08:59,310 --> 00:09:02,490
I am going to run that on the Raspberry Pi.

116
00:09:05,250 --> 00:09:11,490
So activity to the way it's going to be added automatically.

117
00:09:14,040 --> 00:09:15,330
And let's see what we get.

118
00:09:16,800 --> 00:09:23,610
OK, you can see that when the temperature is lower than 15, we have the energy on.

119
00:09:23,790 --> 00:09:27,330
And when the temperature is greater than 15, we have the energy of.

120
00:09:29,310 --> 00:09:31,980
All right, and that's the end of this activity.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,210 --> 00:00:05,730
Here is yet another activity for you to practice more on sale in this activity.

2
00:00:05,760 --> 00:00:07,680
Here is what you are going to do.

3
00:00:08,520 --> 00:00:13,830
So from the Arduino, you are going to send a counter, so you're going to initialize a counter.

4
00:00:13,890 --> 00:00:22,890
OK, so you need a counter and then send it every five hundred milliseconds.

5
00:00:23,250 --> 00:00:28,520
So every time, of course, you're going to increase the contact and so increment.

6
00:00:29,910 --> 00:00:32,490
So you send zero one to three inches.

7
00:00:33,750 --> 00:00:35,790
And that, of course, from the main look.

8
00:00:37,080 --> 00:00:42,870
On the Raspberry Pi, what you're going to do is, of course, receive and print the content.

9
00:00:43,440 --> 00:00:44,670
So that is the first action.

10
00:00:45,450 --> 00:00:48,240
No, this would be a little bit too easy for you at this point.

11
00:00:48,600 --> 00:00:57,990
So what you're going to do is also that every 10 seconds, so every 10 seconds, you are going to reset

12
00:00:58,590 --> 00:00:59,160
the content.

13
00:01:00,900 --> 00:01:05,040
So to reset the content, you're going to need to send a special comment to the audio.

14
00:01:05,370 --> 00:01:10,290
And on the other note is that when you receive when receive

15
00:01:13,050 --> 00:01:19,560
reset content, come and then you reset the content, of course, so you'll reset it to zero.

16
00:01:19,950 --> 00:01:24,690
And the thing is that those two actions here are completely independent.

17
00:01:24,810 --> 00:01:25,140
OK.

18
00:01:25,350 --> 00:01:32,250
So here, as you did in the previous activity, you're going to send the content every 500 milliseconds

19
00:01:32,670 --> 00:01:38,460
without using delete and you're going up in parallel and in a different action check.

20
00:01:38,460 --> 00:01:44,310
If you have received that reset, come to a comment on the Raspberry Pi, you're going to do the same.

21
00:01:44,730 --> 00:01:45,030
OK.

22
00:01:45,480 --> 00:01:51,420
So in Python, you are not going to use time to sleep for 10 seconds, of course, because if you do

23
00:01:51,420 --> 00:01:56,320
that, you're not going to be able to print the content for 10 seconds.

24
00:01:56,350 --> 00:01:56,670
OK.

25
00:01:57,090 --> 00:02:02,730
So in Python, you're going to need to do also a non blocking action every 10 second.

26
00:02:03,090 --> 00:02:06,780
We've basically the same structure as we did previously on the original.

27
00:02:07,290 --> 00:02:14,910
So in your while true, in the void loop of your Python program, the first action of the second, OK,

28
00:02:14,910 --> 00:02:15,590
it doesn't matter.

29
00:02:15,600 --> 00:02:22,890
The other is to receive and print the content and decision action is to reset the content whenever you

30
00:02:22,890 --> 00:02:24,240
have past 10 seconds.

31
00:02:24,630 --> 00:02:27,540
All right, and then we see you in the next video for the solution.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:05,250
This is the solution of the produce committee where you need to send a counter from the Arduino to the

2
00:00:05,250 --> 00:00:11,310
Raspberry Pi and then every 10 seconds so independently from that first action, you're going to read

3
00:00:11,310 --> 00:00:16,640
it that content from the Raspberry Pi to the Arduino and then get started in other ways.

4
00:00:16,650 --> 00:00:18,600
I'm going to start with the Arduino code.

5
00:00:19,320 --> 00:00:26,730
So let's create a bean counter is equal to zero here as a global view, and then I'm going to initialize.

6
00:00:26,940 --> 00:00:35,940
So I'm going to set up the sales of sale that begin to moderate and wide.

7
00:00:37,470 --> 00:00:41,850
Sale latest sale is ready.

8
00:00:42,420 --> 00:00:49,530
I am going to create two new vials here on site long last time.

9
00:00:50,130 --> 00:00:53,880
Let's see counter cent is equal to.

10
00:00:56,290 --> 00:01:08,920
Mills are zero and then unsigned long counter, so actually sent come to delay is equal to 500 milliseconds

11
00:01:09,970 --> 00:01:25,750
in the value unsigned long time now is equal to mills, which is the current time if the time not minus

12
00:01:25,930 --> 00:01:27,790
the last time we have sent to consent.

13
00:01:28,180 --> 00:01:32,020
So this is a duration is greater or equal than the delay.

14
00:01:33,280 --> 00:01:41,050
What we do is so we enter the if and we say that the last time we have sent the counter is equal to

15
00:01:41,140 --> 00:01:42,210
time now.

16
00:01:42,220 --> 00:01:47,860
So you pretty faced with that because, well, that's a common structure we have already used before.

17
00:01:48,130 --> 00:01:52,390
And then what I do is I simply do sayang that print, Ellen.

18
00:01:53,700 --> 00:01:54,510
With the content.

19
00:01:55,350 --> 00:02:01,230
So it's going to send zero the first time and then they do come to this place.

20
00:02:02,100 --> 00:02:09,180
So basically this is going to send zero and then one two three four five every five hundred milliseconds

21
00:02:09,450 --> 00:02:12,450
again, the country is going to increase indefinitely.

22
00:02:13,350 --> 00:02:19,560
Now let's add the second action, which is when we received the reset counter command, we reset the

23
00:02:19,560 --> 00:02:25,860
content and here we need to choose exactly the stream which would correspond to that comment.

24
00:02:26,180 --> 00:02:30,810
Naturally, let's just use that string reset underscore content.

25
00:02:30,990 --> 00:02:31,290
OK.

26
00:02:32,040 --> 00:02:40,500
So what I usually do when I send data over a saying like that we've commenced is I put underscore keep

27
00:02:40,500 --> 00:02:41,820
I need to separate two.

28
00:02:41,820 --> 00:02:42,270
What's?

29
00:02:43,310 --> 00:02:49,070
So here we have the first action, which is going very fast and is none blocking, and then we do,

30
00:02:49,070 --> 00:02:55,850
if, say, are not available quickly greater than zero.

31
00:02:57,200 --> 00:02:58,070
And then we do.

32
00:02:59,030 --> 00:03:09,650
Screen command is equal to say I don't read string until backslash in.

33
00:03:10,830 --> 00:03:19,320
We've seen good quotes and semicolon, and then if command is equal to or is it content?

34
00:03:20,910 --> 00:03:24,240
So this comments should be exactly equal to reset content.

35
00:03:24,510 --> 00:03:29,970
So you should send, for example, countries that are any other string, it's not going to work.

36
00:03:31,540 --> 00:03:38,730
So open close curly brackets and then what we do is simply do content is equal to zero.

37
00:03:40,870 --> 00:03:41,530
And that's it.

38
00:03:42,310 --> 00:03:43,330
And then we have the end.

39
00:03:44,110 --> 00:03:49,030
But as we do nothing here.

40
00:03:49,720 --> 00:03:55,200
So any comment that you send that is not a reset counter, it's just going to go nowhere.

41
00:03:55,360 --> 00:03:56,980
OK, we are not going to process that.

42
00:03:57,280 --> 00:03:59,350
We're just going to process the reset counter.

43
00:03:59,890 --> 00:04:01,360
So that's it for the RNA code.

44
00:04:01,810 --> 00:04:04,000
What we can do is we can already trace.

45
00:04:04,210 --> 00:04:09,730
So let's run this on the, I don't know, activity three.

46
00:04:13,310 --> 00:04:14,630
Compiling, uploading.

47
00:04:15,650 --> 00:04:16,940
OK, don't uploading.

48
00:04:17,720 --> 00:04:19,430
I'm going to open Sam Alito.

49
00:04:19,940 --> 00:04:21,020
We receive zero.

50
00:04:22,670 --> 00:04:28,250
OK, you can see here we have restarted the program actually, and we have zero one, two or three,

51
00:04:28,250 --> 00:04:28,820
etc..

52
00:04:29,450 --> 00:04:29,780
Great.

53
00:04:30,080 --> 00:04:31,280
Not if I sent anything.

54
00:04:32,240 --> 00:04:33,050
Nothing happens.

55
00:04:33,050 --> 00:04:40,700
If I or is it content, but the content is being reset to zero.

56
00:04:41,360 --> 00:04:42,380
So it's working.

57
00:04:43,040 --> 00:04:50,210
Now, let's go to the Python program and I'm going to go back to the previous activity and just.

58
00:04:51,550 --> 00:04:53,610
Could be this for this trip to OK.

59
00:04:55,480 --> 00:04:58,420
And it's from everything in the way true.

60
00:05:00,800 --> 00:05:07,100
OK, so once again, I use the same structure here, so I'm not going to write it everything and into

61
00:05:07,100 --> 00:05:08,510
why look, what do we do?

62
00:05:08,540 --> 00:05:13,160
So the first thing we need to do is to print the content that we receive.

63
00:05:13,250 --> 00:05:21,080
OK, so if said ducks in waiting is tricky greater than zero once again, don't forget there is no parenthesis

64
00:05:21,080 --> 00:05:21,380
here.

65
00:05:21,950 --> 00:05:32,150
So if we have received something, we do, so content is equal to say, let's read a line that decode

66
00:05:32,600 --> 00:05:35,480
with UTF eight.

67
00:05:36,500 --> 00:05:38,500
That is Drake.

68
00:05:39,890 --> 00:05:47,480
And it's just that two integer also, because content is an integer and we simply do print.

69
00:05:49,250 --> 00:05:53,580
Let's say received come to blows.

70
00:05:54,170 --> 00:05:59,840
And we print the counter and we cut it back to a string, of course, because no, that's an integer.

71
00:06:00,110 --> 00:06:01,760
All right, let's already trade is good.

72
00:06:02,780 --> 00:06:04,520
So the code here is running on the order.

73
00:06:04,520 --> 00:06:05,630
No, let's try this code.

74
00:06:05,990 --> 00:06:08,240
I assume this creates its name.

75
00:06:08,420 --> 00:06:11,270
Activity three.

76
00:06:13,750 --> 00:06:20,140
It's going to open this sale, OK, roasted counter two, three, four, etc. So as you can see, I'm

77
00:06:20,140 --> 00:06:22,690
going to get it when I start again.

78
00:06:25,300 --> 00:06:30,640
So we have a sale, OK, and we start to receive the counter at 2:00 here.

79
00:06:31,000 --> 00:06:31,570
Why is that?

80
00:06:31,570 --> 00:06:37,960
Because when you have the time that slip who give the time for you, how do we know to actually start

81
00:06:37,960 --> 00:06:39,610
and settle the sale correctly?

82
00:06:40,660 --> 00:06:43,540
And then how do you know it's going to directly start to send data?

83
00:06:43,570 --> 00:06:50,500
OK, so it's going to start to send zero and then one to etc. But basically, the time that you sleep,

84
00:06:50,920 --> 00:06:54,880
the Arduino already has sent zero and one at that time.

85
00:06:54,880 --> 00:06:58,930
After time that slip, you do say the reset input buffer.

86
00:06:59,170 --> 00:07:08,030
So the zero and one heat are not processed because basically they are sent before you reach that line.

87
00:07:08,050 --> 00:07:12,430
OK, so actually, let's run this increments that reset input buffer.

88
00:07:13,210 --> 00:07:14,740
We don't run that again.

89
00:07:18,560 --> 00:07:22,010
And you can see now we receive zero and one.

90
00:07:22,220 --> 00:07:28,640
But if you check very carefully, we receive that directly at once, OK, the zero and one is going

91
00:07:28,640 --> 00:07:29,720
to go in the buffer.

92
00:07:30,050 --> 00:07:37,190
And this is going to be trigger for zero, one and two directly without any delay because zero and one

93
00:07:37,190 --> 00:07:39,440
are actually already inside the buffer.

94
00:07:39,440 --> 00:07:45,590
So what's going to happen is that if you do not reset the input buffer, any data and equipment, anything

95
00:07:45,590 --> 00:07:52,940
that going to be received basically during this time that sleep is going to be processed at once, everything,

96
00:07:52,940 --> 00:07:54,200
basically at the same time.

97
00:07:54,920 --> 00:08:01,760
So that's why I basically also had the reset button is that you don't process many commands at the same

98
00:08:01,760 --> 00:08:05,750
time at the beginning and you start from this point.

99
00:08:06,590 --> 00:08:12,650
You start with a clear input buffer and then you only process any command that you receive after that.

100
00:08:13,220 --> 00:08:13,490
OK.

101
00:08:13,850 --> 00:08:15,350
So we're going to continue like this.

102
00:08:20,400 --> 00:08:27,540
OK, you can see received contact two, three, etc. and not went to see them, but is that so we received

103
00:08:27,540 --> 00:08:28,560
the contact correctly?

104
00:08:28,560 --> 00:08:33,150
Not what we're going to do is we're going to reset that contact every 10 second.

105
00:08:33,660 --> 00:08:39,270
And to do that, we are not going to use time to sleep because if we use time to sleep well, what's

106
00:08:39,270 --> 00:08:43,710
going to happen is that this program is going to be stuck for 10 seconds.

107
00:08:44,640 --> 00:08:48,300
We are not going to go with this line.

108
00:08:48,750 --> 00:08:53,820
And so when we go to this line after 10 seconds, this is going to process everything in before.

109
00:08:54,120 --> 00:09:01,560
So we're going to see received contact, for example, two until 11 at once and not just when we receive

110
00:09:01,560 --> 00:09:01,680
it.

111
00:09:01,740 --> 00:09:08,760
OK, we're going to see that late and all at once because they are going to be stuck in the input booth.

112
00:09:09,360 --> 00:09:17,040
So what we do is I'm going to see, I'm going to add viable last time.

113
00:09:17,160 --> 00:09:24,240
Reset counter is equal to time that time.

114
00:09:25,340 --> 00:09:35,450
If you do that, you get the current time with Python and then reset come to delay is equal to 10 seats.

115
00:09:36,080 --> 00:09:37,670
So here we use cigarettes, OK?

116
00:09:38,330 --> 00:09:41,360
And then here you have why look so white?

117
00:09:41,380 --> 00:09:44,450
True, if you have this, you enter this book.

118
00:09:44,450 --> 00:09:46,220
Of course, this is going to be very fast.

119
00:09:46,730 --> 00:09:49,110
And what I'm going to do is I'm going to add another action.

120
00:09:49,760 --> 00:09:52,610
So here will be action to.

121
00:09:54,310 --> 00:09:56,960
And he action one.

122
00:09:58,030 --> 00:10:05,780
So we get the current time, so time now is equal to time that time.

123
00:10:06,070 --> 00:10:10,840
So as you can see, the structure is very similar to what we do in C++ without, you know.

124
00:10:10,870 --> 00:10:11,230
All right.

125
00:10:12,130 --> 00:10:18,190
If time now, minus the last time, where is the counter?

126
00:10:18,730 --> 00:10:30,130
If this is greater equal, then the delay we entered is if we do last time or is it is equal to time

127
00:10:30,130 --> 00:10:30,490
now?

128
00:10:31,270 --> 00:10:32,800
OK, so exact same structure.

129
00:10:33,190 --> 00:10:36,640
And what is the action the action is to send?

130
00:10:36,730 --> 00:10:37,320
So said.

131
00:10:37,330 --> 00:10:38,710
That's right.

132
00:10:40,420 --> 00:10:42,220
Recent content.

133
00:10:42,220 --> 00:10:43,930
So the exact same thing here.

134
00:10:45,100 --> 00:10:52,340
Backslash in that encode with you to f eight.

135
00:10:54,100 --> 00:10:54,610
All right.

136
00:10:54,970 --> 00:10:57,640
And that should be it.

137
00:10:58,480 --> 00:11:00,370
That's actually to print.

138
00:11:01,850 --> 00:11:04,180
Since or is it down to command?

139
00:11:06,500 --> 00:11:11,930
So we knew exactly when it has been sent from the Raspberry Bay and let's try this program.

140
00:11:12,060 --> 00:11:12,740
OK, let's see.

141
00:11:12,740 --> 00:11:13,460
It works.

142
00:11:13,700 --> 00:11:14,420
Transcript?

143
00:11:17,910 --> 00:11:19,700
OK, received counter.

144
00:11:20,340 --> 00:11:22,800
So basically, we're going to wait 10 seconds.

145
00:11:23,880 --> 00:11:24,770
We should be around.

146
00:11:25,390 --> 00:11:28,340
OK, you can see sentries at counter-claim and we receive zero.

147
00:11:30,290 --> 00:11:31,550
OK, let's continue.

148
00:11:33,550 --> 00:11:35,090
And you can see a wrong toe.

149
00:11:35,110 --> 00:11:41,640
So just before 20, what is it going to come on so we can actually see that it's currently working OK?

150
00:11:41,660 --> 00:11:44,620
Because here we send the counter every 500 milliseconds.

151
00:11:45,040 --> 00:11:51,430
So 10 seconds means that we have send 20 times the counter, which is what we have done here from zero

152
00:11:51,490 --> 00:11:52,570
to 19.

153
00:11:52,780 --> 00:11:57,190
And then we send the results come in from the Raspberry Pi to the Arduino.

154
00:11:57,610 --> 00:11:58,210
On the Arduino.

155
00:11:58,210 --> 00:12:04,090
We reset the counter to zero and we still continue to send the contact and receive on the Raspberry

156
00:12:04,090 --> 00:12:04,390
Pi.

157
00:12:04,900 --> 00:12:05,270
All right.

158
00:12:05,290 --> 00:12:09,060
And that's the end of this activity and also the end of this section.

159
00:12:09,490 --> 00:12:16,030
Let's now continue by adding more functionality to the Arduino and use them in collaboration with the

160
00:12:16,030 --> 00:12:16,780
Raspberry Pi.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: PART 2 - Arduino Functionalities (Hardware Components)

1
00:00:00,180 --> 00:00:00,670
Great.

2
00:00:00,690 --> 00:00:07,470
You can make a Raspberry Pi and Arduino molds, communicate between each other using cellular communication.

3
00:00:08,070 --> 00:00:10,770
This is already a strong foundation you have.

4
00:00:11,010 --> 00:00:15,300
And with this foundation, you will be able to create all kinds of applications.

5
00:00:15,810 --> 00:00:22,230
So what are we going to do from now on is to make progress towards the final project, which is a complete

6
00:00:22,230 --> 00:00:25,980
intercom system using both Arduino and Raspberry Pi.

7
00:00:26,490 --> 00:00:32,520
First, we would focus on Arduino functionalities, then Raspberry Pi functionalities enough so that

8
00:00:32,550 --> 00:00:35,040
we would be ready to start the final project.

9
00:00:35,670 --> 00:00:38,760
So let's begin this path on Arduino.

10
00:00:39,240 --> 00:00:41,310
There are actually two sections here.

11
00:00:41,580 --> 00:00:45,510
First, we will add all the components that we need for the project.

12
00:00:45,840 --> 00:00:50,760
One by one, for each component, I will give you some basic explanation.

13
00:00:51,000 --> 00:00:57,330
OK, and I'm not going to dive into details here because knowing how to create basic circuits and code

14
00:00:57,600 --> 00:01:00,840
with Arduino is part of the prerequisites of the course.

15
00:01:01,290 --> 00:01:06,050
The goal of this section is just to do some recaps and make sure that you have the correct secrets,

16
00:01:06,300 --> 00:01:12,450
and also that we can reach the next practice section where you will create programs to interact with

17
00:01:12,450 --> 00:01:16,200
the original functionalities from the Raspberry Pi.

18
00:01:16,770 --> 00:01:22,440
So for some components, if you already know how to use them, feel free to skip the coding.

19
00:01:22,440 --> 00:01:27,150
But if not, then watch the video to expand your original knowledge.

20
00:01:27,570 --> 00:01:34,860
You can also see those following videos as a quick help to come to if you are stuck in some of the following

21
00:01:34,860 --> 00:01:36,570
activities of project.

22
00:01:37,230 --> 00:01:38,580
All right, let's get started.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:05,010
Let's start with the first component, we're going to add to the secret the algae.

2
00:00:05,370 --> 00:00:11,940
And so basically what I'm going to do for the listeners on creating the secret is I'm going to create

3
00:00:11,940 --> 00:00:18,960
a secret first on a simulation here on a tin can and then I'm going to show you the real secret.

4
00:00:19,180 --> 00:00:25,500
I use this simulation here because it's simply easier to show you how to connect to the components.

5
00:00:25,920 --> 00:00:29,760
I'm not going to use the simulation for the goose just to create the secret.

6
00:00:30,090 --> 00:00:36,340
And if you want to create an account on Tinker Cancer, that's free, that's free to you.

7
00:00:36,360 --> 00:00:38,520
Go on Tinker dot com.

8
00:00:38,530 --> 00:00:45,870
OK, you just create your account and then you go to a secret and you can to create new secrets here.

9
00:00:46,470 --> 00:00:49,140
And that is where I am right now.

10
00:00:49,680 --> 00:00:53,310
The first thing I'm going to do is to add an Arduino both here.

11
00:00:53,310 --> 00:00:57,760
So Arduino, Uno and I'm going to add breadboard.

12
00:00:58,530 --> 00:00:59,550
So let's use a break.

13
00:00:59,970 --> 00:01:02,140
Let's use a full side Red Bull.

14
00:01:03,330 --> 00:01:11,550
So the components you can see here, you have all the components you just search and you have the different

15
00:01:11,550 --> 00:01:11,970
components.

16
00:01:12,000 --> 00:01:14,700
I'm going to put you here like that.

17
00:01:15,090 --> 00:01:20,610
And before we actually add algae, I'm going to connect those two lines here.

18
00:01:20,910 --> 00:01:27,060
So the minus line, I'm going to connect key like that to the ground.

19
00:01:28,560 --> 00:01:30,450
So let's first connect the ground.

20
00:01:31,410 --> 00:01:41,120
So let's make a line for ground and line for a fold, OK, between the ordinal and the Bible.

21
00:01:41,200 --> 00:01:48,780
Okay, so the ground line will be black and five volt line would be right.

22
00:01:50,070 --> 00:01:55,980
OK, so that's important first, you connect the ground key of the breadboard to the ground of the adeno

23
00:01:56,280 --> 00:02:02,670
and five of the breadboard to five volt of the audience who can just are the black wire here and the

24
00:02:02,670 --> 00:02:06,550
red wire, you know that we have this down.

25
00:02:06,570 --> 00:02:14,690
I'm going to search for DB anything and just take it here and plug it here.

26
00:02:15,240 --> 00:02:17,210
So actually, it's played here.

27
00:02:18,920 --> 00:02:23,930
So one thing is that if you don't have an algae energy, you can also use three different energy.

28
00:02:24,170 --> 00:02:30,410
You probably know how to create a secret with one energy so you could create a secret with three entities.

29
00:02:30,410 --> 00:02:38,210
If you don't have algae RGV, well, you can see that you have four legs, OK?

30
00:02:38,450 --> 00:02:41,720
And here we see red cathode blue green.

31
00:02:42,140 --> 00:02:48,020
So here the although you can see is red, blue and green, but maybe the other for the corals on new

32
00:02:48,050 --> 00:02:51,560
algae and form might actually be ready for the physical one.

33
00:02:51,560 --> 00:02:56,860
And I'm going to show you just after is not bright blue, green, but red, green and blue.

34
00:02:56,870 --> 00:03:01,820
OK, so that you can, of course, experiment with the corals and then find out.

35
00:03:02,150 --> 00:03:08,810
And then being here, the energy catalog, which is actually the longer leg of the algae.

36
00:03:08,810 --> 00:03:13,220
OK, so you just take what is the long delay and this is the cathode.

37
00:03:13,250 --> 00:03:14,960
All this is the anode depends.

38
00:03:15,290 --> 00:03:21,650
If this is a cathode, what you're going to do is you're going to simply link this to the ground.

39
00:03:21,950 --> 00:03:23,420
So let's use a black way.

40
00:03:23,420 --> 00:03:29,810
You can use black wire, if possible, for the ground and right for reasons of fabled.

41
00:03:30,710 --> 00:03:34,070
So not that I have this Green Line, I can just leave the cathode to the ground.

42
00:03:35,060 --> 00:03:41,000
If this isn't another, you would need to link to five volt and how to know that well, you have to

43
00:03:41,000 --> 00:03:46,490
take the manual on description of what your boat because you can just find out from the component.

44
00:03:46,880 --> 00:03:52,210
And if you are not sure, then try it with the cathode mode like this and then make the code need to

45
00:03:52,220 --> 00:03:53,120
experimentation.

46
00:03:53,510 --> 00:03:58,370
And if it doesn't work, then try to plug these to fail and see if that works.

47
00:03:58,910 --> 00:03:59,240
All right.

48
00:03:59,390 --> 00:04:03,780
And no went for each of the colors here.

49
00:04:03,800 --> 00:04:13,010
I'm going to add the resistant, so resist to let's either register here between, for example, the

50
00:04:13,250 --> 00:04:22,520
red and a digital pin here, and we are going to use a two hundred and twenty sheet on raised.

51
00:04:24,260 --> 00:04:25,100
You can see here.

52
00:04:26,450 --> 00:04:31,010
The caller is right, right, and Brown for a full been raising story.

53
00:04:31,460 --> 00:04:37,160
If you haven't five been resistant, that's going to be read red and in black, in black, and I'm going

54
00:04:37,160 --> 00:04:44,720
to he connect these two digital pin number 11 on the Arduino Una.

55
00:04:45,530 --> 00:04:47,260
So let's change the color, actually.

56
00:04:49,090 --> 00:04:51,690
Let's use well, let's use Orange, OK?

57
00:04:52,510 --> 00:05:00,070
Let's avoid black and right, and I'm going to have cookies and cookies here.

58
00:05:01,180 --> 00:05:02,500
I'm going to click the blue line.

59
00:05:04,020 --> 00:05:05,610
Two in 10.

60
00:05:07,200 --> 00:05:12,030
This one, it's pretty new, so it's easier to recognize it and the green.

61
00:05:13,240 --> 00:05:13,690
To.

62
00:05:15,740 --> 00:05:20,450
In nine minutes, but also, all right.

63
00:05:20,480 --> 00:05:22,730
And the secret is done.

64
00:05:24,170 --> 00:05:30,560
So one thing that is very important is to make sure that you connect the three and it is all the three

65
00:05:30,560 --> 00:05:38,480
legs of the two pins where you have a tilde here, as you can see, so that you can use the P.W. in

66
00:05:38,600 --> 00:05:42,860
functionality because we are going to use the analog write function.

67
00:05:43,160 --> 00:05:50,180
So here I have chosen 11, 10 and nine, which are all P.W. compatible, which can see, for example,

68
00:05:50,180 --> 00:05:53,030
on the Arduino, we know we have also six and five and three.

69
00:05:53,450 --> 00:05:56,240
And it may also depend on the board you have.

70
00:05:56,250 --> 00:06:02,700
So make sure you have P.W. in functionality and this is the real secret with the answer, and it is

71
00:06:02,700 --> 00:06:03,620
so very important.

72
00:06:03,620 --> 00:06:09,800
First of all, before you do anything we already know, just make sure to unplug your Arduino from the

73
00:06:09,800 --> 00:06:10,460
Raspberry Pi.

74
00:06:10,640 --> 00:06:17,300
So the Raspberry Pi you still own, as you can see the edges here, but we have pulled off the audio.

75
00:06:17,630 --> 00:06:17,870
OK.

76
00:06:18,080 --> 00:06:19,180
And then you can see we have.

77
00:06:19,190 --> 00:06:21,530
So here we have the red and the black.

78
00:06:22,220 --> 00:06:26,540
Why is looking to make the common ground and common five volt on the bright bowl?

79
00:06:26,960 --> 00:06:28,790
I have glued my arm to be here.

80
00:06:29,510 --> 00:06:37,310
The longer leg is actually the second one on the left, so I can take this to a ground line here with

81
00:06:37,310 --> 00:06:38,840
this small black wire.

82
00:06:39,170 --> 00:06:44,210
And then for each of the other legs, I have a 220Nm ready store.

83
00:06:44,540 --> 00:06:49,790
And then this other part of the reason it all goes to a digital twin here.

84
00:06:50,150 --> 00:06:51,740
This one is actually out.

85
00:06:52,070 --> 00:06:57,690
Put it in and you can see I have connected from 11, 10 and nine.

86
00:06:58,310 --> 00:07:05,660
And one difference from the Tinker Cat simulation is that here my colors are actually red, green and

87
00:07:05,660 --> 00:07:05,990
blue.

88
00:07:06,020 --> 00:07:07,080
OK, how to know that what?

89
00:07:07,130 --> 00:07:09,470
I have just made some experimentations.

90
00:07:09,920 --> 00:07:14,090
So I have used a wire, which is white, green and blue.

91
00:07:14,600 --> 00:07:15,890
OK, just for the three colors.

92
00:07:15,890 --> 00:07:16,780
It doesn't really matter.

93
00:07:16,790 --> 00:07:23,240
The color of the wires is just to give you some, maybe some indication so you don't make more mistakes

94
00:07:23,240 --> 00:07:23,810
in the future.

95
00:07:24,410 --> 00:07:24,710
All right.

96
00:07:24,800 --> 00:07:27,200
So you can see that's the secret.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:04,560
Let's quickly see how to control the algae energy with your Arduino.

2
00:00:04,890 --> 00:00:08,220
Once again, in this section, I'm going to go quite fast.

3
00:00:08,610 --> 00:00:14,820
The goal is not to go into details about each Arduino functionality, but to reach the next activity

4
00:00:14,820 --> 00:00:21,750
path where you can practice on how to know functionalities controlled by the Raspberry Pi using cellular

5
00:00:21,750 --> 00:00:22,410
communication.

6
00:00:22,920 --> 00:00:23,670
So let's start in.

7
00:00:23,670 --> 00:00:27,320
Let's directly write some basic code for the Ogbe entity.

8
00:00:27,660 --> 00:00:33,210
So what you can do here already is to connect your audience once the secret is correctly done.

9
00:00:33,450 --> 00:00:39,000
You can connect your Arduino back to the Raspberry Pi with the USB cable and then check that you have

10
00:00:39,000 --> 00:00:45,870
the Arduino connected you with the Chromebook, of course, and not with basically how to control.

11
00:00:45,870 --> 00:00:48,090
And arguably LG is very simple.

12
00:00:48,450 --> 00:00:54,660
If you already know and you probably already know how to control an entity, well, an LGB is nothing

13
00:00:54,660 --> 00:00:56,760
more than three different entities.

14
00:00:57,120 --> 00:01:04,050
When we speak about the code, so we are going to control each leg, OK, each color separately.

15
00:01:04,560 --> 00:01:06,720
So I'm going to create some define here.

16
00:01:06,730 --> 00:01:12,710
So define RGV right being which pin number 11?

17
00:01:12,900 --> 00:01:17,850
So make sure that you use the pins you have selected if you have selected different pins.

18
00:01:18,480 --> 00:01:19,860
Define Ogbe.

19
00:01:21,210 --> 00:01:30,440
So green bean then and define IGB Blue B9.

20
00:01:30,450 --> 00:01:35,700
And if you have some doubt about the other of those pins for you, well, just start with this.

21
00:01:36,240 --> 00:01:40,830
And then you will be able to change that after you experiment with some code.

22
00:01:41,190 --> 00:01:48,480
So we have to define then what we do is we simply do P mode on each leg.

23
00:01:48,810 --> 00:01:49,110
OK?

24
00:01:49,650 --> 00:01:54,120
Just like we were controlling three different entities.

25
00:01:54,630 --> 00:02:03,530
So pin mode for the red pin been mode for the green bin mode for the loop.

26
00:02:06,510 --> 00:02:06,870
OK.

27
00:02:07,500 --> 00:02:08,940
Everything is correctly set up.

28
00:02:09,300 --> 00:02:14,120
And then when I'm not going to do anything in the loop, I'm just going to show you how to just pull

29
00:02:14,250 --> 00:02:15,290
on this RGV.

30
00:02:16,020 --> 00:02:23,640
So if you do digital right here, you can do digital rights and you can also do either right because

31
00:02:23,640 --> 00:02:27,360
we are using being set up P.W. in compatible.

32
00:02:27,750 --> 00:02:29,250
I'm going to start with digital, right?

33
00:02:29,950 --> 00:02:30,270
OK.

34
00:02:31,140 --> 00:02:35,970
So you can put, for example, high and then digital.

35
00:02:35,970 --> 00:02:37,650
Let's just use the same here.

36
00:02:39,950 --> 00:02:45,200
So for the rent and then for the green and then for the blue.

37
00:02:47,200 --> 00:02:55,690
So let's say we want only to go on so low, only the green and the blue grid to make a combination of

38
00:02:55,690 --> 00:02:56,800
green and blue collar.

39
00:02:57,040 --> 00:03:04,930
So those are going to be put on with full intensity and this one with zero intensity.

40
00:03:05,530 --> 00:03:06,640
So let's.

41
00:03:07,240 --> 00:03:09,160
So is connected.

42
00:03:09,700 --> 00:03:11,200
Let's offload.

43
00:03:14,240 --> 00:03:14,570
All right.

44
00:03:14,600 --> 00:03:21,080
And you can see we have this coral, which is not exactly blue, not exactly green, but in the middle.

45
00:03:21,710 --> 00:03:24,320
So we did, you can do different combinations, OK?

46
00:03:24,350 --> 00:03:29,800
Up to seven different combinations, and then I'm going to commence this.

47
00:03:32,150 --> 00:03:33,890
And now let's see an example.

48
00:03:34,130 --> 00:03:34,760
Analog.

49
00:03:36,110 --> 00:03:36,560
All right.

50
00:03:36,680 --> 00:03:37,040
OK.

51
00:03:38,150 --> 00:03:41,420
So I'm going to use also being like this.

52
00:03:41,840 --> 00:03:45,620
And then you need to give a number between zero and 255.

53
00:03:45,650 --> 00:03:48,830
So here you have more control over the colors, OK?

54
00:03:49,130 --> 00:03:54,220
So if you put zero, that is going to be pulled out of it, you put 255.

55
00:03:54,230 --> 00:03:56,290
It's just like you use digital, right?

56
00:03:56,300 --> 00:03:56,900
We tie.

57
00:03:57,200 --> 00:04:05,030
And then if you any any of the 180, this is going to be built into each of the brightness because you

58
00:04:05,030 --> 00:04:11,900
can between zero and 255, that's going to be applied to the red color of the RGV.

59
00:04:12,500 --> 00:04:13,460
So let's do this.

60
00:04:15,500 --> 00:04:20,750
I'm going to use the same for the green, but I'm going to put zero here.

61
00:04:20,750 --> 00:04:23,150
I'm going to try to make a purple color.

62
00:04:23,540 --> 00:04:28,050
So I'm going to do blue and let's say 200.

63
00:04:28,070 --> 00:04:28,400
OK.

64
00:04:28,970 --> 00:04:33,340
So we're going to do a mix of red and blue, which should be.

65
00:04:34,490 --> 00:04:35,360
And let's see that.

66
00:04:35,370 --> 00:04:37,250
So let's run the code.

67
00:04:38,500 --> 00:04:41,670
Upload uploading and don't uploading.

68
00:04:42,270 --> 00:04:49,950
OK, and we have a column that is one, so that's pretty much it's for the Pajiba anything you first

69
00:04:49,950 --> 00:04:58,410
create some define content and then you do pick mode for each bin and then you can use either digital

70
00:04:58,410 --> 00:05:00,450
rights or analog rights.

71
00:05:00,810 --> 00:05:06,620
So this only if you have the PWI functionality, of course, and you can create any combination of color

72
00:05:06,810 --> 00:05:09,050
and this you can use in the set setup in the loop.

73
00:05:09,060 --> 00:05:11,580
Well, you can use that anywhere you want.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:05,970
Now that we have our MGB energy undersecretary Gorecki working, let's add a.

2
00:00:06,780 --> 00:00:09,780
So here you will see that it's going to be very simple.

3
00:00:09,930 --> 00:00:14,100
So you find a button here on the right.

4
00:00:14,520 --> 00:00:20,650
You take the pearl button and you are going to put it somewhere here in the middle of the breadboard.

5
00:00:20,670 --> 00:00:22,500
That's what they usually do.

6
00:00:22,890 --> 00:00:23,530
And then what?

7
00:00:23,560 --> 00:00:27,030
We will need to add some connections to that push button.

8
00:00:27,330 --> 00:00:30,000
So first, we need to add a connection to the ground.

9
00:00:30,300 --> 00:00:33,540
And for that, I'm going to add also a resistor.

10
00:00:35,020 --> 00:00:38,530
Raised here, that's sort of directly connect.

11
00:00:39,310 --> 00:00:47,110
For example, the leg on the right here to the ground and it's choose a 10 kilo on resistance, so that's

12
00:00:47,110 --> 00:00:51,560
going to be brown, black and orange for a full blown resistor.

13
00:00:51,970 --> 00:00:58,690
And that's going to be brown, black, black and red for a five band resistant.

14
00:00:59,320 --> 00:01:02,530
So this result will act as they pulled on the resistant.

15
00:01:02,890 --> 00:01:09,340
So basically with this, we can make sure that the push-button state will be low, basically zero volt

16
00:01:09,520 --> 00:01:10,330
by default.

17
00:01:10,330 --> 00:01:14,060
And when we press on the push button, the stage is going to be high.

18
00:01:14,320 --> 00:01:15,670
All five volt.

19
00:01:16,030 --> 00:01:22,150
OK, so that's very important to either use a an external register or use the internal pull, a pretty

20
00:01:22,150 --> 00:01:26,680
strong Arduino, which is going to do the opposite, which means that the state is going to be high

21
00:01:26,680 --> 00:01:29,140
by default and low when you press on the button.

22
00:01:29,140 --> 00:01:32,110
But all right, so we have no connection to the ground now.

23
00:01:32,110 --> 00:01:38,140
So if the connection to the grant is on the right side here, the left side is going to be connected

24
00:01:38,140 --> 00:01:43,330
to five volt and I'm going to use it right here because that's five volt connection.

25
00:01:43,930 --> 00:01:48,160
OK, so the push button is now correctly going to fight volt and ground.

26
00:01:48,670 --> 00:01:52,360
And now we are going to add a connection to a digital beat.

27
00:01:52,360 --> 00:01:59,080
So you'd think the side OK, which is also connected to the ground and from the same line here you take

28
00:01:59,080 --> 00:02:04,690
a wire and let's connect to pin number seven.

29
00:02:05,210 --> 00:02:06,820
I'm going to double click here.

30
00:02:07,530 --> 00:02:08,470
Just going to do this.

31
00:02:10,370 --> 00:02:11,560
You make it nicer.

32
00:02:14,950 --> 00:02:17,770
OK, ladies, and let's choose.

33
00:02:17,980 --> 00:02:19,090
OK, thank you.

34
00:02:19,840 --> 00:02:27,240
So from the same side as where you collect the registrar here, you're going to put a wire to pin number

35
00:02:27,250 --> 00:02:27,820
seven.

36
00:02:27,850 --> 00:02:29,760
OK, so we won't use interrupting.

37
00:02:29,770 --> 00:02:32,560
You can choose any pin you want.

38
00:02:32,560 --> 00:02:33,550
It doesn't really matter.

39
00:02:33,910 --> 00:02:34,210
All right.

40
00:02:34,220 --> 00:02:35,500
And the secret is done.

41
00:02:36,490 --> 00:02:44,040
And here is the physical circuit with the push button that I added also alongside with the AGP.

42
00:02:44,800 --> 00:02:50,290
So you can see we have the push button on the middle of the breadboard and then on the left, I have

43
00:02:50,290 --> 00:02:54,550
this wireless, this red wire to the five volt line here.

44
00:02:55,060 --> 00:03:02,290
And then on the right side, I have this raised on these 10km east, all connected to the ground and

45
00:03:02,290 --> 00:03:07,870
then a wire from the same light here connected to digital pin number seven.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:05,910
Let's now see how to read data from the bush button and more specifically, how to know when we have

2
00:00:05,910 --> 00:00:07,200
pressed on the button.

3
00:00:07,210 --> 00:00:10,020
So the exact moment when we have pressed on the button.

4
00:00:10,440 --> 00:00:14,940
This is something you should already know how to do as per the prerequisites of the course, but I'm

5
00:00:14,940 --> 00:00:17,280
still going to do it quickly as a recap.

6
00:00:17,640 --> 00:00:19,740
Also, we will bounce the button.

7
00:00:20,160 --> 00:00:29,310
So first of all, what you're going to do is to create a defined here button, so define our constant

8
00:00:29,340 --> 00:00:29,730
ins.

9
00:00:30,330 --> 00:00:32,850
And so that is number seven.

10
00:00:33,990 --> 00:00:42,000
And then if you want to initialize the push button, you do P mode with button being indent inputs.

11
00:00:42,780 --> 00:00:49,050
So the button is initialized, not if you want to read from the push button you're going to do digital

12
00:00:49,890 --> 00:00:52,770
read button pin.

13
00:00:52,860 --> 00:00:55,920
And this is going to return you the date.

14
00:00:55,950 --> 00:00:58,230
OK, that is high ordered is low.

15
00:00:58,620 --> 00:01:03,720
So, for example, Bytes State is equal to digital right button B.

16
00:01:04,380 --> 00:01:09,480
Now, if we want to check if we have pressed on the bottom button, what we need to do is we need to

17
00:01:09,480 --> 00:01:10,770
save the previous state.

18
00:01:10,780 --> 00:01:15,960
So we need to read the state, save the previous state and then read again and take if we have something

19
00:01:15,960 --> 00:01:16,500
different.

20
00:01:16,530 --> 00:01:26,250
OK, so I'm going to add here Byte previews button state, and I'm simply going to initialize that here

21
00:01:26,910 --> 00:01:30,990
to the current state of the button, just up to initialize it.

22
00:01:31,350 --> 00:01:33,630
So that would be the first state of the pushbutton.

23
00:01:33,930 --> 00:01:39,870
And so now what we need to do in the volume is to read the button again with digital read and then compare

24
00:01:40,050 --> 00:01:43,200
to the previous button state and see if we have something different.

25
00:01:43,620 --> 00:01:50,100
But what I'm also going to do is I'm going to d balance the budget because if we just compare the produce

26
00:01:50,100 --> 00:01:55,200
and the current state, what is going to happen is we're going to have the bounce mechanism, so the

27
00:01:55,200 --> 00:01:56,580
physical bounce of the button.

28
00:01:57,240 --> 00:02:00,000
And this will give us some wrong measurements.

29
00:02:00,390 --> 00:02:07,440
OK, so we need to balance the button to make sure that when we actually press, we get just one price

30
00:02:07,440 --> 00:02:11,280
undercoat and not multiple presses because the button is bouncing.

31
00:02:11,880 --> 00:02:16,170
So to do that, I'm going to create two new variables here.

32
00:02:16,500 --> 00:02:23,380
You're unsigned, long last time button priced is equal to.

33
00:02:23,400 --> 00:02:25,480
So let's initialize two minutes out to zero.

34
00:02:25,480 --> 00:02:26,280
It doesn't matter.

35
00:02:26,610 --> 00:02:31,290
And then unsigned long, let's say, button.

36
00:02:32,130 --> 00:02:35,730
The balance is equal to endless, but 50 milliseconds.

37
00:02:36,270 --> 00:02:37,500
So what are we going to do here?

38
00:02:37,950 --> 00:02:42,690
Basically, we're going to first individually look, get the time so unsigned.

39
00:02:43,110 --> 00:02:46,830
Long time now is equal to minutes.

40
00:02:47,610 --> 00:02:54,750
And then we're going to do if time no, minus last time the button has been priced.

41
00:02:55,260 --> 00:03:02,520
If this is greater equal than the button demands duration here, then we can enter this thief.

42
00:03:03,030 --> 00:03:08,190
So we will see that when the state of the button changes, we're going to update the last time the button

43
00:03:08,190 --> 00:03:10,650
was pressed during different time.

44
00:03:11,190 --> 00:03:14,880
And so that the next time we enter the void loop, we're going to check the condition.

45
00:03:14,880 --> 00:03:17,810
So time not minus last time the button has been priced.

46
00:03:18,270 --> 00:03:24,570
And if this is lower than the delay, so basically if this is lower than fifty milliseconds, then we

47
00:03:24,570 --> 00:03:27,060
are not going to read the state again.

48
00:03:27,070 --> 00:03:32,460
So basically, we are going to ignore the button for 15 milliseconds every time the button has been

49
00:03:32,460 --> 00:03:32,820
pressed.

50
00:03:33,030 --> 00:03:38,000
So we don't read all the balances of the button, so not enough time has passed.

51
00:03:38,010 --> 00:03:44,760
What we can do is the right button states the current one is equal to digital read.

52
00:03:45,880 --> 00:03:47,170
We've been.

53
00:03:49,240 --> 00:03:49,810
Like this?

54
00:03:51,000 --> 00:04:00,600
We were in the state and then we do if button state is different from the previous button state in that

55
00:04:00,600 --> 00:04:01,020
case.

56
00:04:01,560 --> 00:04:10,080
We know that the state has changed and what we can do is to now update the last time the button pressed.

57
00:04:10,320 --> 00:04:14,850
So actually, let's name it different last time button changed.

58
00:04:15,000 --> 00:04:15,360
OK.

59
00:04:16,260 --> 00:04:17,390
Because it's not pressed.

60
00:04:17,400 --> 00:04:23,110
He's just changed because if we are here, it could be priced out early.

61
00:04:23,160 --> 00:04:25,800
So I'm just going to use changed, which is for both.

62
00:04:26,160 --> 00:04:29,100
OK, so last time the button has changed is actually.

63
00:04:29,950 --> 00:04:30,240
OK.

64
00:04:30,330 --> 00:04:37,800
Because that's what just happened and also beat the previous button state, which is now the current

65
00:04:38,430 --> 00:04:38,990
button state.

66
00:04:39,480 --> 00:04:44,280
And so the next time we enter the void, look, we're going to first check if enough time has passed

67
00:04:44,370 --> 00:04:52,800
since the last time button changed, and we're only going to enter this if again after 50 milliseconds.

68
00:04:53,010 --> 00:04:58,410
And then when when we are here in the code, we know that the button state has changed.

69
00:04:58,710 --> 00:05:02,780
So to know if the button has actually been priced are released.

70
00:05:02,790 --> 00:05:10,450
We do if button state is equal to high in our case because we have a pool don register.

71
00:05:10,950 --> 00:05:13,390
This means that the button has been priced.

72
00:05:13,620 --> 00:05:17,250
And if it's low, it means the button has been released.

73
00:05:17,640 --> 00:05:18,930
So here we could do so.

74
00:05:18,930 --> 00:05:21,870
Let's actually do say on the beginning.

75
00:05:22,890 --> 00:05:31,030
So can we use Sanyo to be like and say No, don't print Elon.

76
00:05:31,050 --> 00:05:35,070
Say Button has been pressed.

77
00:05:36,060 --> 00:05:42,240
So when we enter this, if we know that the button has been priced so just priced and we don't have

78
00:05:42,240 --> 00:05:48,210
any bounce because the next thing we are going to read the button is 50 milliseconds later.

79
00:05:48,690 --> 00:05:50,610
So let's applaud the code.

80
00:05:52,300 --> 00:05:53,890
And actually, we have an.

81
00:05:54,220 --> 00:05:55,330
Why do I have this error?

82
00:05:55,660 --> 00:06:01,840
You can see open device because I have simply not played my ordering up to the Raspberry Pi or to the

83
00:06:01,840 --> 00:06:06,370
computer if you are using, you know, one computer and no eject tools.

84
00:06:07,060 --> 00:06:07,430
OK.

85
00:06:07,720 --> 00:06:08,380
Upload.

86
00:06:10,640 --> 00:06:15,800
And Don, imploding, I'm going to happen to see a monitor, make sure the Blue Ridge is correct and

87
00:06:15,800 --> 00:06:20,540
I'm going to press on the push button button has been priced a press again.

88
00:06:20,990 --> 00:06:29,150
And you can see every time I press or press again, Button has been pressed one more time and, well,

89
00:06:29,150 --> 00:06:30,050
look what is working.

90
00:06:30,980 --> 00:06:36,920
So this is the structure that you're going to use often, you know, when you have pressed are released

91
00:06:37,040 --> 00:06:40,360
on push button and with the debone mechanism.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:04,440
We now have the AGP and the judgment in our secret.

2
00:00:04,770 --> 00:00:12,720
Let's now add a buzzer so we can make some sound, so buzzer can also be named sometime.

3
00:00:12,720 --> 00:00:16,980
Pitzl OK, so you take your buzzer and you just blow it.

4
00:00:17,490 --> 00:00:23,580
For example, here and when you have two pings, a positive and a negative.

5
00:00:24,060 --> 00:00:29,250
So you just put that just plug the negative to the ground.

6
00:00:30,440 --> 00:00:36,920
Is like that, and you plug the positive directly to a digital pin.

7
00:00:37,310 --> 00:00:45,620
Let's use he the digital pin number eight, which is available in Let's take a little yellow color.

8
00:00:46,250 --> 00:00:49,310
OK, you don't need any register here and you.

9
00:00:49,520 --> 00:00:50,510
So that's very busy.

10
00:00:50,580 --> 00:00:55,100
Can you just plug negative to the ground and the positive to a digital pin?

11
00:00:55,430 --> 00:00:56,960
It doesn't matter which one.

12
00:00:57,040 --> 00:01:00,710
OK, you don't need to have P.W. went for the button.

13
00:01:01,760 --> 00:01:03,260
And here is the secret.

14
00:01:03,410 --> 00:01:05,260
We've Bosaso, of course.

15
00:01:05,270 --> 00:01:07,880
Make sure you're just going to and you go off the avenue.

16
00:01:08,210 --> 00:01:10,430
You can see I have the buzzer here.

17
00:01:10,640 --> 00:01:12,920
And so one important thing you can see.

18
00:01:13,280 --> 00:01:15,110
You should have a passive buzzer.

19
00:01:15,140 --> 00:01:16,520
How to know this is a passive.

20
00:01:16,700 --> 00:01:23,810
But if you look at the back, you should see the PC be like, this should be green or something similar.

21
00:01:24,080 --> 00:01:28,040
If it's completely black, it means you have an active buzz.

22
00:01:28,220 --> 00:01:30,860
OK, so here I'm using a passive and they see the PC.

23
00:01:31,270 --> 00:01:35,300
You can see I have a minus and plus you have the plus here.

24
00:01:35,330 --> 00:01:36,950
So the plus is the positive side.

25
00:01:37,340 --> 00:01:39,770
So I'm just going to put it back here.

26
00:01:40,490 --> 00:01:47,780
And so you have the negative side connected to the line of the ground line and the positive, which

27
00:01:47,780 --> 00:01:51,890
is connected to digital pin number eight on the.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:05,400
And let's quickly check how to control the buzzer, so that's going to be the easiest component to control,

2
00:00:05,400 --> 00:00:05,820
actually.

3
00:00:06,030 --> 00:00:16,590
OK, so first you do define key buzzer beater, which is pin number eight here, and then you are going

4
00:00:16,590 --> 00:00:23,220
to use pin mode, pin pin mode with buzzer pin.

5
00:00:23,220 --> 00:00:27,570
And this is output because this is something we control from the Arduino.

6
00:00:28,260 --> 00:00:32,960
And then whether you have one function that is super useful is the function tone.

7
00:00:33,450 --> 00:00:37,170
So the tone function will basically create the sound on the buzzer.

8
00:00:37,380 --> 00:00:45,360
And so you first need to put the pin in a pin and then the frequency and the duration, so the frequency

9
00:00:45,360 --> 00:00:46,320
will be enhanced.

10
00:00:46,650 --> 00:00:51,390
So for example, if I play 440, that's a sound.

11
00:00:51,780 --> 00:00:56,860
I'm going to play that sound for, let's say, 500 milliseconds.

12
00:00:57,030 --> 00:01:01,110
OK, so frequency and then duration in milliseconds.

13
00:01:01,410 --> 00:01:03,810
I'm just going to try this program like this.

14
00:01:04,380 --> 00:01:05,700
Let's applaud the program.

15
00:01:08,160 --> 00:01:08,440
OK?

16
00:01:08,460 --> 00:01:13,330
And as you can hear, we have a sound for five hundred milliseconds.

17
00:01:13,500 --> 00:01:17,250
All that's changed, for example, a lower frequency.

18
00:01:17,250 --> 00:01:18,840
And let's see what we get.

19
00:01:22,920 --> 00:01:29,730
OK, you can see the sound is different now if I want to play that for two seconds.

20
00:01:29,850 --> 00:01:31,350
I'm going to put two thousand.

21
00:01:39,000 --> 00:01:39,430
All right.

22
00:01:39,450 --> 00:01:43,770
And that's pretty much it, not what you can do is you can use, of course, the tone in the set up

23
00:01:43,770 --> 00:01:46,230
in the loop when anywhere you want.

24
00:01:46,980 --> 00:01:51,030
So you first provide the pin, the frequency and the duration.

25
00:01:51,570 --> 00:01:59,100
And so this component is going to be useful for our project to inform the user for something went good

26
00:01:59,100 --> 00:02:03,210
at something went, but we can play different kinds of sounds.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:03,950
Let's us know an LCD screen to our secret.

2
00:00:04,010 --> 00:00:12,080
So the screen will be super useful so we can display some text directly from the Arduino, so density

3
00:00:12,090 --> 00:00:14,220
we are going to use a 16 by two.

4
00:00:14,250 --> 00:00:17,820
OK, and well, I'm going to put it there on tin can.

5
00:00:17,820 --> 00:00:24,930
And then you will see that I'm going to directly plug it here on the bread board when I do the real

6
00:00:24,930 --> 00:00:25,350
secret.

7
00:00:25,350 --> 00:00:30,780
But for the just for the simulation and to show you the connections for the beans, there's going to

8
00:00:30,780 --> 00:00:32,760
be easier like this funnel.

9
00:00:33,180 --> 00:00:38,370
So you have many connectors here and let's go step by step one by one.

10
00:00:38,400 --> 00:00:44,040
First, you have a GNT, so ground you're going to connect to the ground line.

11
00:00:44,310 --> 00:00:46,210
Let's make sure that is ground light.

12
00:00:46,230 --> 00:00:46,530
OK.

13
00:00:47,290 --> 00:00:48,810
It's actually pretty, ladies.

14
00:00:50,310 --> 00:00:57,720
So ground is going to be black and then you have this ESI and this is you connect to.

15
00:00:58,780 --> 00:01:01,540
The this is your line here.

16
00:01:01,630 --> 00:01:09,940
Five volt line, then we have V0, V0 is going to be used to calibrate the luminosity of the screen,

17
00:01:10,240 --> 00:01:12,550
OK, using a potential meter.

18
00:01:12,970 --> 00:01:15,840
So basically here we need to also add a potent emitter.

19
00:01:16,990 --> 00:01:19,300
So I'm going to put it put on soumettre here.

20
00:01:20,230 --> 00:01:24,040
And so the potential, do you have three legs?

21
00:01:24,340 --> 00:01:29,350
You want to put one of the leg, for example, the left one connected to the ground.

22
00:01:30,750 --> 00:01:34,020
Blackwell and then the opposite one connected to.

23
00:01:35,710 --> 00:01:36,310
My vote.

24
00:01:37,350 --> 00:01:41,970
We've all read the wire and then you're going to connect this V0 here.

25
00:01:43,220 --> 00:01:46,570
To the middle pin of the potential middle.

26
00:01:48,770 --> 00:01:50,810
And but it OK.

27
00:01:52,160 --> 00:02:00,440
The next thing is the art has been and, well, this one, you're going to plug it in to a digital pin.

28
00:02:00,650 --> 00:02:06,080
But because we will not have enough digital print, I'm going to plug it into an analog pin instead.

29
00:02:06,440 --> 00:02:15,380
So I'm going to plug it to a phone because, well, you can use actually analog pins as digital pins.

30
00:02:15,830 --> 00:02:22,610
So if you ever run out of digital pins, just use an analog instead and into just use it as a digital

31
00:02:22,610 --> 00:02:31,940
pin, and it's changed color green and then R.W other where he was going to be connected to the ground

32
00:02:33,230 --> 00:02:37,260
with a black wire and for enable.

33
00:02:37,880 --> 00:02:44,720
He is going to a five the same reason as for a spin.

34
00:02:45,050 --> 00:02:47,330
Let's use a different color, for example, purple.

35
00:02:47,930 --> 00:02:54,010
We're going to use this as a digital pin because we won't have enough digital pins here on the secret

36
00:02:54,020 --> 00:02:55,010
for all the components.

37
00:02:55,610 --> 00:02:59,780
Then you have the zero, one, two and three.

38
00:03:00,320 --> 00:03:04,040
You're not going to put anything for those things here.

39
00:03:04,280 --> 00:03:09,920
And then before default, we're going to plug it to the digital pin number two.

40
00:03:11,150 --> 00:03:14,390
So let's use another color for the yellow.

41
00:03:15,870 --> 00:03:20,010
OK, DeFi is the next one two digital pin number three.

42
00:03:21,860 --> 00:03:22,970
Let's use.

43
00:03:24,790 --> 00:03:37,780
Grass and then six to digital in full, so we just follow, we think, the seven to.

44
00:03:39,780 --> 00:03:41,690
Digital been five, all right.

45
00:03:41,820 --> 00:03:42,680
Use a range.

46
00:03:43,800 --> 00:03:44,460
OK.

47
00:03:44,910 --> 00:03:47,120
And then we have energy, so we have to.

48
00:03:48,540 --> 00:03:53,400
The first one is going to be connected to five volt, but with a variety store.

49
00:03:54,210 --> 00:03:57,790
So that's going to be the energy of the LCD screen.

50
00:03:57,820 --> 00:03:58,070
OK.

51
00:03:58,140 --> 00:04:03,660
Because when you use actually and it is here, you can see we use arises also.

52
00:04:03,750 --> 00:04:05,310
That's the same reason here.

53
00:04:05,580 --> 00:04:15,300
I'm going to add every store here to 120 on, and I'm just going to connect it between.

54
00:04:16,600 --> 00:04:23,860
Yet this reaction on the LCD, we read wire and then connected to the.

55
00:04:25,690 --> 00:04:32,590
He line the five volt line, and then we have that one connected to the ground.

56
00:04:34,240 --> 00:04:34,700
All right.

57
00:04:36,400 --> 00:04:43,180
One thing to make sure that you don't do is so don't connect anything to those beings here.

58
00:04:43,540 --> 00:04:45,130
Digital been zero and one.

59
00:04:45,520 --> 00:04:46,060
Why is that?

60
00:04:46,060 --> 00:04:48,100
You can see we have Alex and Tina.

61
00:04:48,520 --> 00:04:51,970
So those pins are also actually used for cellular communication.

62
00:04:52,210 --> 00:04:55,870
So when later on, we use cell communication with the USB cable?

63
00:04:56,110 --> 00:05:00,430
If you have anything plugged here, you're going to have some weird behavior.

64
00:05:00,460 --> 00:05:05,380
OK, so you're going to have some arrows on the same communication and maybe also on the components

65
00:05:05,380 --> 00:05:08,470
that you use on those pins to leave those pins and.

66
00:05:09,790 --> 00:05:16,120
And here is the secret with the LCD screen, so this can look a bit messy, but well, actually, if

67
00:05:16,120 --> 00:05:20,530
you just follow all the steps that I did on Tinker, you should not have any problem.

68
00:05:20,740 --> 00:05:26,030
So I have blinked as you see the screen directly on one of the line here.

69
00:05:26,050 --> 00:05:32,280
So each should each pin each leg of the LCD on a different line.

70
00:05:32,290 --> 00:05:32,620
OK?

71
00:05:32,800 --> 00:05:35,770
This is not connected on the blue.

72
00:05:35,770 --> 00:05:36,730
All of the red line.

73
00:05:36,740 --> 00:05:37,810
This is connected here.

74
00:05:38,500 --> 00:05:45,580
Separated lines on the right book and then you can see each connection here.

75
00:05:45,880 --> 00:05:47,590
So I have the first one.

76
00:05:48,730 --> 00:05:50,530
Maybe you will have lots of different names.

77
00:05:50,920 --> 00:05:53,650
OK, on the on the LCD.

78
00:05:53,650 --> 00:05:59,260
So you have, for example, as we did at the end, I have eight and Kate.

79
00:05:59,530 --> 00:06:04,240
So the name can be different, but the other is going to be the same as what I did before.

80
00:06:04,570 --> 00:06:06,640
So the first one is connected to the ground here.

81
00:06:07,780 --> 00:06:12,910
The second one she does right away is connected to this, you see.

82
00:06:13,450 --> 00:06:15,430
And then the third one is V0.

83
00:06:15,430 --> 00:06:18,100
So v0 is he connected?

84
00:06:18,520 --> 00:06:25,510
So this blue connected to the output been off the potential meter and the potential meter also has.

85
00:06:25,870 --> 00:06:32,740
So for the two extreme legs, a black way out to the ground and the right wire to this issue.

86
00:06:33,310 --> 00:06:35,680
After that, we have the.

87
00:06:37,050 --> 00:06:48,480
R s R s, which is going to take you to a fall and then we have the RW RW connected to the ground here

88
00:06:48,510 --> 00:06:55,470
with this black wire, the E for Enable connected to A5.

89
00:06:56,430 --> 00:06:59,850
And then we have nothing for zero until three.

90
00:07:00,420 --> 00:07:08,210
And then you can see D4 device connected to digital pin number two and then D5 to digital P three.

91
00:07:08,850 --> 00:07:15,390
The six two digital twin full and the seven two digital pin number five.

92
00:07:15,960 --> 00:07:23,220
At the end, we have so for the A here, which is basically the positive side of the energy of the screen.

93
00:07:23,550 --> 00:07:33,780
I have one 220 Ohm Restall connected from here to a different line, and then this red wire connected

94
00:07:33,780 --> 00:07:41,910
to the plus lanky and the bright block and the last connection here is a black way up to the ground.

95
00:07:42,540 --> 00:07:42,960
All right.

96
00:07:43,590 --> 00:07:45,690
And that's it for the LCD screen.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:05,610
Let's not write the code to just print something simple on the LCD screen.

2
00:00:05,910 --> 00:00:11,130
So first of all, we're going to use a defined for each of the pin that we need.

3
00:00:11,160 --> 00:00:21,090
OK, so define I'm going to put LCD, so we will need the as pin, which has been no pay for and then

4
00:00:21,660 --> 00:00:27,920
define LCD being, which is pin number a five.

5
00:00:28,500 --> 00:00:39,810
Then we need the pins from salt and see the full bin, which is two, and we would need the four, the

6
00:00:39,810 --> 00:00:41,700
five, the six and these seven.

7
00:00:42,060 --> 00:00:43,560
So let's change that.

8
00:00:44,280 --> 00:00:51,030
Five, six seven which up in them are two, three, four and five.

9
00:00:51,240 --> 00:00:54,870
OK, so we have six things that we need in our program.

10
00:00:55,560 --> 00:01:03,840
Then to initialize the LCD screen, we will need first to include the liquid crystal.

11
00:01:05,760 --> 00:01:13,140
Libraries, liquid crystal age like this with angled brackets, then we can add salt not in the void

12
00:01:13,140 --> 00:01:22,860
setup, but in the global scope here, liquid crystal, let's name its LCD and we are going to initialize

13
00:01:22,860 --> 00:01:29,280
it by providing different beams here in the other sort of space ending then.

14
00:01:31,200 --> 00:01:37,590
And then default, and then I'm going to go to a new line here.

15
00:01:38,370 --> 00:01:47,700
That's the five, that's the line this year, the six and the seven.

16
00:01:50,440 --> 00:02:00,460
So we have our LC object and not to finish initialization in the void said that we do NCT don't begin

17
00:02:00,460 --> 00:02:09,100
with 16 and two, so we are going to use 16 columns and two lines, which is basically what the screen

18
00:02:09,100 --> 00:02:09,580
has.

19
00:02:10,000 --> 00:02:16,930
And then, well, if you want to print something on the screen, you just do LCD, dot print.

20
00:02:17,080 --> 00:02:19,600
And let's see, starting.

21
00:02:20,380 --> 00:02:21,460
We've done done.

22
00:02:22,870 --> 00:02:25,000
Let's say we want to print that at the beginning.

23
00:02:26,940 --> 00:02:31,800
So let's make sure that the boat is connected, let's upload the code.

24
00:02:33,330 --> 00:02:34,300
I forgot here.

25
00:02:34,380 --> 00:02:36,930
So well, they're always here, but I forgot here.

26
00:02:37,440 --> 00:02:38,190
They come up.

27
00:02:40,310 --> 00:02:41,240
Let's run again.

28
00:02:43,630 --> 00:02:49,060
OK, and this is what you can see here, so maybe you will not have anything is because you need to

29
00:02:49,450 --> 00:02:55,840
move the product shipment until you find you can sit here until you find the correct angle for the potential

30
00:02:55,840 --> 00:02:59,320
meter to correctly calibrate the screen.

31
00:03:01,440 --> 00:03:04,530
So it looks good.

32
00:03:04,570 --> 00:03:07,620
OK, we have starting corrected displayed.

33
00:03:07,860 --> 00:03:12,930
So make sure that for the first time you actually moved the potential meter so that you can see something.

34
00:03:12,930 --> 00:03:15,240
Once you see something, then we can go further.

35
00:03:16,200 --> 00:03:22,230
OK, and now, for example, if you want to clear the screen, let's say we do delay 2000.

36
00:03:22,230 --> 00:03:25,980
So we want to print for two seconds and then we do LCD.

37
00:03:26,020 --> 00:03:27,360
Don't clear.

38
00:03:27,900 --> 00:03:33,450
This is going to print starting and after two seconds, it's going to clear the entire screen and it's

39
00:03:33,880 --> 00:03:34,230
this.

40
00:03:37,170 --> 00:03:42,810
So you can see it starting and after two seconds, the next is gone.

41
00:03:43,350 --> 00:03:46,800
All right, so let's try to comment on that.

42
00:03:47,880 --> 00:03:50,800
And one other thing is that you can actually play with the cursor.

43
00:03:50,810 --> 00:03:56,800
So by default, the Q, so he's going to be at zero and zero so you can do anything you don't set.

44
00:03:58,080 --> 00:04:02,640
Q So and by default, is going to be year zero and zero.

45
00:04:03,540 --> 00:04:05,520
Here you can see you have 16 by two.

46
00:04:05,610 --> 00:04:09,420
So if you put, for example, three, that's going to be on the third column.

47
00:04:09,720 --> 00:04:13,730
If you put one here, that's going to be on the second line.

48
00:04:13,740 --> 00:04:15,780
OK, so we start to count at zero.

49
00:04:16,020 --> 00:04:19,770
So you can go from zero to 15 here and zero to one here.

50
00:04:20,460 --> 00:04:23,640
And so here we are going to print starting, but let's see where.

51
00:04:24,090 --> 00:04:25,200
So the payload?

52
00:04:27,730 --> 00:04:34,930
And you can see we print starting on the second line, starting from the fourth column because this

53
00:04:34,930 --> 00:04:38,690
is the three and one, so that's second line, fourth column.

54
00:04:39,220 --> 00:04:44,830
And so every time we want to change the queue so you just do anything, you set yourself and then you

55
00:04:44,830 --> 00:04:49,510
start to print something and that's going to start to print from where the cursor is.

56
00:04:50,290 --> 00:04:51,970
OK, so basically, that's pretty much it.

57
00:04:51,980 --> 00:04:59,200
First, you initialize the LCD, you the LCD that begin with 16 by two and then we've set just so you

58
00:04:59,200 --> 00:05:01,120
can set it closer to a different place.

59
00:05:01,120 --> 00:05:07,390
With print you print some text and LCD is very useful, so you can also clear that onto your screen

60
00:05:07,660 --> 00:05:09,460
before you write something.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:05,910
All right, and let's finish this section with a several motto, and just after that, we are going

2
00:00:05,910 --> 00:00:11,430
to practice with the abdominal components, the sound communication and the Raspberry Pi.

3
00:00:11,970 --> 00:00:14,520
So I'm going to add a server here.

4
00:00:15,120 --> 00:00:16,830
So micro several.

5
00:00:17,100 --> 00:00:19,650
OK, let's actually flip it.

6
00:00:21,090 --> 00:00:22,380
Like that?

7
00:00:22,470 --> 00:00:22,860
OK.

8
00:00:23,250 --> 00:00:32,070
So on a classic hobby, seven, we'll you will have here, you will see three different pins and three

9
00:00:32,070 --> 00:00:34,380
wires, so you will have a brown one.

10
00:00:34,500 --> 00:00:41,070
The right one and an orange one or something that is similar to the brown one corresponds to the ground.

11
00:00:41,310 --> 00:00:47,310
So we are going to first connect the ground to the ground of the know.

12
00:00:47,310 --> 00:00:50,370
So let's connect to common ground here.

13
00:00:50,640 --> 00:00:54,330
Let's put that in black and then we have power.

14
00:00:54,780 --> 00:01:00,830
So foil, we can give five volt here and it's cool.

15
00:01:00,850 --> 00:01:01,230
Hit.

16
00:01:03,590 --> 00:01:05,290
That's going to be all right.

17
00:01:05,930 --> 00:01:13,460
And then we have the signal, so the signal is basically to be connected to a digital pin.

18
00:01:13,670 --> 00:01:14,750
I'm going to use Twitter.

19
00:01:15,020 --> 00:01:23,120
So for this digital team, you don't need any P.W. in being any special in just any digital pin.

20
00:01:23,120 --> 00:01:23,540
We do.

21
00:01:24,370 --> 00:01:26,210
Let's use a different color.

22
00:01:26,460 --> 00:01:28,460
Let's use Brown.

23
00:01:29,970 --> 00:01:34,120
Again, that suits for a seven, we're told, but I'm going to explain you something a bit extra here.

24
00:01:34,390 --> 00:01:37,410
So here what you're doing is you're going to control the seven window.

25
00:01:37,420 --> 00:01:41,020
We've been number 12, so that's going to give the command to the seven.

26
00:01:41,260 --> 00:01:44,230
The decision is power, OK from our neighbors.

27
00:01:44,560 --> 00:01:48,720
The thing is that the seven one two oh, so if you use a hobby, one is done up one.

28
00:01:48,730 --> 00:01:51,790
It's completely fine is going to be pulled out on front.

29
00:01:52,460 --> 00:01:53,950
OK, that's obvious here.

30
00:01:54,190 --> 00:01:58,510
But there are several may draw more power than other companies.

31
00:01:59,110 --> 00:02:06,310
So if you want to add multiple symbols or give more strength to several, you may also want to add an

32
00:02:06,310 --> 00:02:07,770
external power supply.

33
00:02:07,780 --> 00:02:09,160
So I'm just going to show you.

34
00:02:09,850 --> 00:02:14,620
So I'm just going to use this name for battery here, just as an example.

35
00:02:14,640 --> 00:02:16,240
So yours is not going to be.

36
00:02:16,570 --> 00:02:19,000
That's one that any other power supply.

37
00:02:19,270 --> 00:02:24,310
But basically, what you can do is you can see when you have an external power supply, you have a negative

38
00:02:24,310 --> 00:02:25,300
and positive.

39
00:02:25,510 --> 00:02:34,400
So let's actually connect these to this side of the breadboard piece.

40
00:02:34,500 --> 00:02:38,290
I'm going to put that in black and in, right?

41
00:02:39,280 --> 00:02:44,050
So now we have this side of the bright board with the ground connected to the other.

42
00:02:44,080 --> 00:02:47,020
No key, the line with five volt.

43
00:02:47,740 --> 00:02:49,450
And now the other sign here.

44
00:02:49,720 --> 00:02:54,590
So do the kids, though here is not in this OK is just on top.

45
00:02:54,610 --> 00:02:55,900
It is just a visual.

46
00:02:56,740 --> 00:03:02,380
So you have another lane with another ground and another plus line, which is this time the external

47
00:03:02,380 --> 00:03:03,130
power supply.

48
00:03:03,430 --> 00:03:07,210
And what you can do is that instead you can just.

49
00:03:08,420 --> 00:03:09,640
But we're on the same.

50
00:03:10,250 --> 00:03:11,480
So I'm just going to do this.

51
00:03:15,770 --> 00:03:17,690
So but the grounds here.

52
00:03:19,080 --> 00:03:22,110
And then the power supply is going to come from.

53
00:03:23,820 --> 00:03:24,210
The.

54
00:03:27,330 --> 00:03:37,290
External power supply and one very important thing to do is to actually connect the grounds of everything,

55
00:03:37,290 --> 00:03:42,180
okay, because if you don't connect the ground of everything, then the command you're going to say

56
00:03:42,210 --> 00:03:44,260
here on pin number 12 is not going to work.

57
00:03:44,580 --> 00:03:46,220
It's going to be some garbage comment.

58
00:03:46,240 --> 00:03:50,760
So you're going to connect the ground of this to the ground of the.

59
00:03:52,160 --> 00:03:57,650
How do you make sure you can hit the ground, OK, not the ground to do this because you may have some

60
00:03:57,800 --> 00:03:58,550
problems.

61
00:03:59,770 --> 00:04:00,070
OK.

62
00:04:01,160 --> 00:04:05,600
And now you have the same seven, what are you going to give the same command, but it's externally

63
00:04:05,600 --> 00:04:09,260
polled by another battery or another?

64
00:04:09,260 --> 00:04:10,040
Possibly.

65
00:04:10,550 --> 00:04:12,110
So all the grounds are connected.

66
00:04:12,350 --> 00:04:14,530
Everything here is powered by the acronym.

67
00:04:14,990 --> 00:04:16,730
The seven were totally spoiled by this.

68
00:04:17,840 --> 00:04:22,280
And then we still have the comment from Pinnacle 12 that goes to the with two.

69
00:04:22,280 --> 00:04:30,230
And just one last thing is don't use PIN number 13 here on the Arduino because PIN number 13 is also

70
00:04:30,230 --> 00:04:32,570
connected to the built in energy.

71
00:04:32,870 --> 00:04:39,010
And if you connect anything to that, well, you may have some unexpected behavior because this thing

72
00:04:39,080 --> 00:04:42,410
is going to be triggered automatically at some point.

73
00:04:42,770 --> 00:04:49,490
So just don't use the pin number 13 so you can use PIN to 12 on Arduino.

74
00:04:49,490 --> 00:04:55,430
We know because those ones are reserved better to reserve them for sale communication and these for

75
00:04:55,430 --> 00:04:56,420
the built in energy.

76
00:04:57,230 --> 00:04:57,560
All right.

77
00:04:57,610 --> 00:04:58,790
And that's it for a second.

78
00:05:00,060 --> 00:05:06,840
Ben, is there a real secret with the seven would you can see she uses very small wand and the gear

79
00:05:06,840 --> 00:05:09,240
is in a plastic here.

80
00:05:09,750 --> 00:05:12,990
It's very low quality one, but that's going to do for this cause.

81
00:05:13,440 --> 00:05:19,200
That's basically the standard one, the cheapest you can find and maybe the one you have on your know.

82
00:05:19,740 --> 00:05:25,830
And you can see I have some kind of stuff like this that I'm going to use on the several for the final

83
00:05:25,830 --> 00:05:26,220
project.

84
00:05:26,580 --> 00:05:29,870
So you can see we have these wires here.

85
00:05:29,890 --> 00:05:37,440
So this cable with a brown, bright and orange, so brown and right are connected here to ground and

86
00:05:37,650 --> 00:05:38,820
five vote of the Arduino.

87
00:05:39,240 --> 00:05:40,920
I'm not going to use an external power supply.

88
00:05:40,920 --> 00:05:46,650
I'm just going to pull out the seven from the I mean, this is completely fine, OK for this circuit.

89
00:05:46,950 --> 00:05:52,500
It's just that if you want more several, if you want to use that in a real application where you need

90
00:05:52,500 --> 00:05:56,690
to put a lot of talk on the cell.

91
00:05:56,700 --> 00:06:00,090
So a lot of force on the cell maybe use an external, possibly.

92
00:06:00,520 --> 00:06:07,710
So I've just moved the beats, the ground and the final line here on the right so I can put the cell

93
00:06:07,710 --> 00:06:12,750
he on the left, and then this is connected to pin number 12.

94
00:06:13,380 --> 00:06:19,170
OK, just to show you have another several, so you can see that's completely different.

95
00:06:19,180 --> 00:06:25,110
Yeah, I bought another one and the gear here is in metal and you can see when you buy your several,

96
00:06:25,110 --> 00:06:27,510
usually you have stuff like this that comes with it.

97
00:06:27,810 --> 00:06:36,420
OK, so you can just plug this to the cell so you can basically plug the cell to something mechanical,

98
00:06:36,420 --> 00:06:41,640
for example, the door mechanism or anything like a camera, anything that you want.

99
00:06:41,910 --> 00:06:44,580
So you can plug the several here with the mechanical path.

100
00:06:44,610 --> 00:06:51,840
With those tools here and you can see any hobby, several well has the same OK, same connector.

101
00:06:51,840 --> 00:06:58,100
So I'm maybe going to use that one for the rest of the crews, but that's the exact same sim.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:01,300
And let's not right.

2
00:00:01,590 --> 00:00:04,710
How did you go to control several motto?

3
00:00:05,170 --> 00:00:13,920
So first of all, I am going to, of course, at a define several thing which is number 12.

4
00:00:14,220 --> 00:00:21,300
Then to initialize the several, I will need to include the several libraries, so several don't each.

5
00:00:21,340 --> 00:00:26,640
OK, so we needed to include library for the LCD screen as well for the cell.

6
00:00:26,970 --> 00:00:31,320
And then we're going to create a symbol here in the global scope sort of symbol.

7
00:00:32,040 --> 00:00:33,720
We use the name of the library.

8
00:00:34,020 --> 00:00:35,100
And then let's name it.

9
00:00:35,610 --> 00:00:37,480
So we as lowercase.

10
00:00:37,500 --> 00:00:37,770
OK.

11
00:00:38,880 --> 00:00:40,470
But we just created like this.

12
00:00:40,830 --> 00:00:41,790
No parentheses.

13
00:00:41,970 --> 00:00:44,070
Nothing in the void setup.

14
00:00:44,940 --> 00:00:49,250
I'm going to do several that attach.

15
00:00:49,620 --> 00:00:54,300
So we're going to basically attach a pin to control the seven dot.

16
00:00:54,300 --> 00:00:58,470
And of course, that's the selfie and notice of what is initialized.

17
00:00:58,980 --> 00:01:03,570
So if I want to give a command to several, I can do several notes, right?

18
00:01:03,810 --> 00:01:04,980
And what can I give?

19
00:01:04,980 --> 00:01:06,150
I can give a number.

20
00:01:06,360 --> 00:01:10,230
So an integer number between zero and 180.

21
00:01:10,950 --> 00:01:11,610
So what is that?

22
00:01:11,610 --> 00:01:16,510
Basically, a seven window is not unlimited, OK, and what it can do?

23
00:01:16,530 --> 00:01:19,650
It can go from zero to 180 degrees.

24
00:01:19,860 --> 00:01:22,290
So basically, it can make half the rotation.

25
00:01:22,590 --> 00:01:25,230
You can do more than that with a 7.2, OK.

26
00:01:25,440 --> 00:01:31,230
So, for example, if you want to control, will weave your Arduino when that's not the kind of toy

27
00:01:31,230 --> 00:01:31,680
you want.

28
00:01:31,830 --> 00:01:35,250
You want a model that can make more than one term.

29
00:01:35,610 --> 00:01:35,910
OK.

30
00:01:36,120 --> 00:01:43,530
So you basically zero is going to be one extreme position and 100, and she's going to be the other

31
00:01:43,530 --> 00:01:44,490
extreme position.

32
00:01:44,790 --> 00:01:46,200
Let's put 50.

33
00:01:46,530 --> 00:01:46,860
OK.

34
00:01:47,040 --> 00:01:53,310
So we're going to put the seven footer at 50 when actually, let's go to the middle, let's go to 90.

35
00:01:53,640 --> 00:01:57,640
So that's going to be that should be the middle position of the seven with them.

36
00:01:58,050 --> 00:01:59,200
And let's applaud that.

37
00:01:59,200 --> 00:02:01,080
Go to the Arduino.

38
00:02:01,380 --> 00:02:06,330
So guaranteed upload and let's see what this level is doing.

39
00:02:08,260 --> 00:02:12,640
Compiling imploding, OK, and you can see here the civil has moved.

40
00:02:13,030 --> 00:02:14,720
This is the middle position.

41
00:02:15,160 --> 00:02:24,640
So maybe if I want the middle position, I can change that plastic, but to be around something like

42
00:02:24,640 --> 00:02:29,620
around the middle position, OK, so it's going to be like this under extreme position, and he is going

43
00:02:29,620 --> 00:02:33,130
to be like that on the lowest position.

44
00:02:33,850 --> 00:02:36,910
And maybe you several can make a little bit of nose.

45
00:02:37,480 --> 00:02:38,840
It's just that well, here.

46
00:02:38,880 --> 00:02:47,500
The plastic gear is not great quality and the several might force a beat, but that's not really a problem

47
00:02:47,500 --> 00:02:47,800
here.

48
00:02:47,980 --> 00:02:51,520
Again, if you want to have a better quality, you can buy another of several.

49
00:02:51,520 --> 00:02:54,160
But for now, that's all we need.

50
00:02:54,460 --> 00:02:59,890
If you have that from your starter kit and then, well, I want to show you something more just because

51
00:02:59,890 --> 00:03:00,630
we're going to use that.

52
00:03:00,790 --> 00:03:04,720
The following is how to make the smooth sweep.

53
00:03:04,870 --> 00:03:10,570
So basically the sweep examples, so we're going to go from zero to 180 and from one hundred eighty

54
00:03:10,570 --> 00:03:12,640
two zero and that indefinitely.

55
00:03:13,030 --> 00:03:16,000
So you can see the several move from one side to the other.

56
00:03:16,120 --> 00:03:17,410
So I'm going to remove that.

57
00:03:17,830 --> 00:03:20,470
And in the void loop, I'm going to add a full loop.

58
00:03:20,660 --> 00:03:23,800
So four, it is equal to zero.

59
00:03:24,670 --> 00:03:27,960
I lower than 180.

60
00:03:28,570 --> 00:03:36,490
And I so basically we go from zero to 180 and we do several knots right eye.

61
00:03:36,940 --> 00:03:39,970
And we had a delay of, let's say, 10 milliseconds.

62
00:03:40,390 --> 00:03:45,850
So every 10 milliseconds, we increment the position from zero to 180.

63
00:03:46,000 --> 00:03:49,720
And once we reach 180 degrees, we do four.

64
00:03:51,020 --> 00:04:03,170
It is equal to 180, it is greater than its greater equal than zero I minus minus.

65
00:04:03,710 --> 00:04:07,550
So with this follow, we go from one hundred eighty to zero.

66
00:04:07,820 --> 00:04:16,070
OK, because we decrease, we discriminate the counter every time several human experiments correctly

67
00:04:16,080 --> 00:04:17,990
spelled right.

68
00:04:18,770 --> 00:04:19,130
I.

69
00:04:20,140 --> 00:04:27,010
And DeLay 10, so what this is going to make to several go from zero to one hundred eighty degrees every

70
00:04:27,010 --> 00:04:28,420
10 milliseconds.

71
00:04:28,780 --> 00:04:32,650
This is going to make the several go from one hundred eighty to zero.

72
00:04:33,130 --> 00:04:35,830
And then we come back and we start at zero again.

73
00:04:36,250 --> 00:04:38,740
And let's see what it does.

74
00:04:38,770 --> 00:04:43,150
So let's upload on this change of civil motor.

75
00:04:43,690 --> 00:04:49,690
OK, and you can see the symbol is going from the minimum to the maximum position and coming back.

76
00:04:50,020 --> 00:04:56,200
So now if you want to stop this, what you can do is you can upload another program that doesn't use

77
00:04:56,200 --> 00:04:58,780
the several are what I usually do.

78
00:04:58,780 --> 00:05:00,460
It is quite safe to do.

79
00:05:00,850 --> 00:05:04,790
I just disconnect the wire on the opinion of a 12.

80
00:05:04,790 --> 00:05:07,840
Here you can see the command wire that seat.

81
00:05:08,260 --> 00:05:09,550
I don't disconnect the ground.

82
00:05:09,550 --> 00:05:15,280
I don't disconnect to push a major, disconnect the command, and I make sure that this doesn't touch

83
00:05:15,280 --> 00:05:16,050
anything else.

84
00:05:16,060 --> 00:05:21,670
OK, so I can continue with my experiment and I don't need to upload an empty code.

85
00:05:22,450 --> 00:05:22,930
All right.

86
00:05:23,350 --> 00:05:29,350
And well, that's the end of the section where we built the original circuit for the following in the

87
00:05:29,350 --> 00:05:29,770
course.

88
00:05:30,040 --> 00:05:35,680
Let's not get some practice with those components, which we are going to control from the Raspberry

89
00:05:35,680 --> 00:05:36,070
Pi.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: PART 2 - Practice

1
00:00:00,120 --> 00:00:06,570
You know, have all the components you need for the final project of this course, and before we go

2
00:00:06,570 --> 00:00:10,800
there, let's get some practice first in the following activities.

3
00:00:10,920 --> 00:00:16,470
You will create some programs to control some know components from the Raspberry Pi.

4
00:00:16,890 --> 00:00:23,250
You will see some examples that are going to make you understand better what you can achieve using Sergio

5
00:00:23,430 --> 00:00:28,320
and how to put what you want to do into real code that works.

6
00:00:28,800 --> 00:00:29,700
And let's start.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,450 --> 00:00:06,000
This activity number four, we are going to start from the cone actually of the activity.

2
00:00:06,210 --> 00:00:06,960
Number three.

3
00:00:07,110 --> 00:00:11,500
So we have the Python code on the Raspberry Pi here and the Cypress Press Code on the adeno.

4
00:00:11,820 --> 00:00:16,620
So first thing, I'm going to just copy this inside a new project.

5
00:00:17,150 --> 00:00:27,150
OK, who that because I have this new project and it's removing the logs here, and let's copy this

6
00:00:27,240 --> 00:00:36,450
inside this new five also, and I'm just gonna add here time that's slipped 0.01.

7
00:00:36,450 --> 00:00:40,930
That was missing and I previously forgot this or not.

8
00:00:40,950 --> 00:00:47,020
Well, basically, that's going to be the same, but this program is going to consume less resources,

9
00:00:47,070 --> 00:00:48,690
OK, and much less CPU.

10
00:00:49,320 --> 00:00:50,680
So what is your challenge?

11
00:00:51,360 --> 00:00:54,520
Your challenge is simply to deliver what you receive.

12
00:00:54,540 --> 00:00:54,870
OK.

13
00:00:55,080 --> 00:01:01,770
And what you do on the albino with the LCD screen that we have added, OK, if you remember before I

14
00:01:01,770 --> 00:01:06,540
told you that it was kind of difficult to debug what's going on in the Arduino.

15
00:01:06,540 --> 00:01:13,560
So what you'll receive, etc. Well, what we can do now is when we receive something we can print that's

16
00:01:13,560 --> 00:01:15,210
on the LCD.

17
00:01:15,450 --> 00:01:21,630
When we send something, we can also bring that on the LCD, for example, with a log message sent counter

18
00:01:21,630 --> 00:01:22,740
and come to.

19
00:01:23,700 --> 00:01:31,830
So what you can do here in this activity is first the initial the LCD here and then when whenever you

20
00:01:31,830 --> 00:01:35,430
receive something or you send something, you bring that on the LCD.

21
00:01:35,430 --> 00:01:38,550
So you print a nice message and you can play with your cursor.

22
00:01:38,600 --> 00:01:42,210
OK, so you can make sure that all the text is on the screen.

23
00:01:42,390 --> 00:01:47,220
And so of course, here you are more limited because you only have a screen that is 16 by two.

24
00:01:47,430 --> 00:01:50,920
So you can only put 32 characters max at a time.

25
00:01:51,090 --> 00:01:52,890
So that's a bit limited.

26
00:01:52,890 --> 00:01:57,420
But still, you can get good information from what is going on in your program.

27
00:01:58,080 --> 00:02:01,980
And well, on the Raspberry Pi side, there is nothing to change.

28
00:02:02,280 --> 00:02:05,340
We are just going to use the exact same program.

29
00:02:05,760 --> 00:02:06,040
All right.

30
00:02:06,060 --> 00:02:08,580
I would see you in the next video for the solution.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1
00:00:00,180 --> 00:00:06,180
This is the solution of the previous activity where you have to start from the previous activities of

2
00:00:06,180 --> 00:00:13,260
activity number three again, but this time we are going to put some logs from the Arduino to the LCD

3
00:00:13,260 --> 00:00:13,800
screen.

4
00:00:14,100 --> 00:00:17,520
And so first of all, we are going to initialize the LCD screen.

5
00:00:17,670 --> 00:00:28,740
So I'm going to include the liquid crystal libraries, a liquid crystal, each with angled brackets

6
00:00:29,010 --> 00:00:43,320
and then add some define for the Pixel LCD s bin, which is a four and then LCD bin, which is a five,

7
00:00:44,360 --> 00:00:45,830
and it's actually this.

8
00:00:47,660 --> 00:00:50,420
Four more times we've differ.

9
00:00:51,870 --> 00:00:56,940
Defied the six decision, which are things No.

10
00:00:56,940 --> 00:01:01,200
Two, three, four and five.

11
00:01:02,990 --> 00:01:10,560
And so we can now create that density objects will it's created here, liquid crystal, its name density,

12
00:01:10,580 --> 00:01:17,540
again, we've all the beings so obvious and so make sure you respect the other, OK?

13
00:01:18,030 --> 00:01:18,680
During bottom.

14
00:01:20,060 --> 00:01:20,750
And then.

15
00:01:22,310 --> 00:01:25,610
And it's good to here, the five.

16
00:01:28,870 --> 00:01:33,150
And the six industry.

17
00:01:35,320 --> 00:01:39,340
OK, not in the set up, so we have sales that begin.

18
00:01:39,610 --> 00:01:44,950
We can also do density, don't begin with 16.

19
00:01:47,040 --> 00:01:47,420
And to.

20
00:01:49,790 --> 00:01:54,860
So here again, the order doesn't really matter, because as soon as the NCD started, well, you can

21
00:01:54,860 --> 00:01:59,850
start to print something and know when we're going to use the engine here.

22
00:01:59,890 --> 00:02:06,400
So let's say that when we send the counter at the same time, we do say that print and some just after

23
00:02:06,410 --> 00:02:09,710
it, maybe we do LCD does clear.

24
00:02:10,490 --> 00:02:14,090
So we clear the screen from anything that was on the screen.

25
00:02:14,360 --> 00:02:17,180
Before we do, the LCD sits.

26
00:02:18,650 --> 00:02:28,280
Q So zero zero to go back to the beginning of the screen and we say, let's see, LCD does print.

27
00:02:28,550 --> 00:02:29,180
We've.

28
00:02:30,860 --> 00:02:32,840
Cents counter.

29
00:02:35,220 --> 00:02:39,700
OK, and let's do LCD, not print with the content.

30
00:02:40,350 --> 00:02:46,680
So here, as you can see, if we do print and then another print, when the cursor starts from zero

31
00:02:46,680 --> 00:02:54,120
zero and then is going to go to one two three four five six seven eight nine 10, 11, 12, 13, 14.

32
00:02:54,420 --> 00:02:59,430
So we just have two more characters that are possible here.

33
00:02:59,790 --> 00:03:06,300
So basically, as long as the content doesn't reach 100, we're going to get all the characters if you

34
00:03:06,300 --> 00:03:06,840
want.

35
00:03:07,110 --> 00:03:14,400
You can also do LCD that sits just so we've zero and one.

36
00:03:14,790 --> 00:03:18,660
So basically, you're going to print that on the first line and that on the second line, OK, let's

37
00:03:18,660 --> 00:03:19,980
keep it like this.

38
00:03:20,790 --> 00:03:25,020
And no, when we receive something here.

39
00:03:25,530 --> 00:03:30,360
Well, for example, what we could do is directly when we receive content, just print that comment.

40
00:03:30,660 --> 00:03:35,520
All we could do a different LCD print for each command.

41
00:03:35,730 --> 00:03:37,740
OK, we've a custom text that we want.

42
00:03:38,040 --> 00:03:38,340
Let's see.

43
00:03:38,340 --> 00:03:40,050
I'm just going to do this LCD.

44
00:03:40,050 --> 00:03:41,430
That's clear.

45
00:03:42,120 --> 00:03:48,390
OK, if I don't do LCD to clear, everything is going to be written on top of what's what has been written

46
00:03:48,390 --> 00:03:52,140
before, but it's not going to remove the other characters.

47
00:03:52,440 --> 00:03:55,080
So you may have something that is quite weird on the screen.

48
00:03:55,080 --> 00:04:01,770
So that's why when I write something here with the logs, I'm going to do LCD clean and LCD don't sits

49
00:04:03,000 --> 00:04:09,180
just sort of zero zero LCD screens, see?

50
00:04:09,270 --> 00:04:09,480
And.

51
00:04:10,860 --> 00:04:15,600
OK, so whenever we send something up, we receive a reset command.

52
00:04:16,290 --> 00:04:21,200
The screen is going to be clear and we're going to get the new logo daddy's printing.

53
00:04:21,540 --> 00:04:22,590
So let's try.

54
00:04:22,620 --> 00:04:23,440
That's OK.

55
00:04:23,460 --> 00:04:29,070
I'm gonna upload the code first, let's name it, activity or.

56
00:04:32,620 --> 00:04:36,250
I'm going to also save this, find this path and find as.

57
00:04:37,840 --> 00:04:40,660
Activity as well.

58
00:04:42,230 --> 00:04:48,350
Even if that's the same code, and then let's start the Python program.

59
00:04:51,610 --> 00:04:55,210
OK, so say OK, and you can see he sent content.

60
00:04:55,990 --> 00:04:56,320
OK.

61
00:04:57,700 --> 00:05:03,160
You can see and we have reset contact and then send contact because it goes very fast and we just received

62
00:05:03,160 --> 00:05:03,340
it.

63
00:05:03,760 --> 00:05:06,460
We were just waiting to come in before we sent another content.

64
00:05:07,390 --> 00:05:11,860
You can see up to 20 and then reset contacts and counting.

65
00:05:12,250 --> 00:05:16,360
OK, so you can see basically what's happening from the original.

66
00:05:18,520 --> 00:05:20,350
I'm going to kill this.

67
00:05:20,680 --> 00:05:27,010
And so as you can see, this system is not the best ideal system because, for example, here on the

68
00:05:27,010 --> 00:05:35,560
Raspberry Pi, the logs that we see here are kind of better, but that's always something you can do

69
00:05:35,560 --> 00:05:36,760
to the limit.

70
00:05:37,120 --> 00:05:40,570
And you can see also that it's not just about digging.

71
00:05:40,960 --> 00:05:46,450
Now, you can see that you can control that entities coming directly from your Raspberry Pi, OK, because

72
00:05:46,510 --> 00:05:51,010
you just send some text and you can print that text on the inside.

73
00:05:51,520 --> 00:05:57,970
So you can already control some Arduino components from the Raspberry Pi going through the cellular

74
00:05:57,970 --> 00:05:58,780
communication.

75
00:05:59,110 --> 00:06:01,840
And that's the end of this activity in the form.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,660
In this new activity, you are going to do a bi directional communication between the Arduino and the

2
00:00:06,660 --> 00:00:12,630
Raspberry Pi and new challenges that when you press on the button on the Arduino side.

3
00:00:12,630 --> 00:00:18,600
So you're going to read and button when you detect that the push button is priced, you send a message

4
00:00:18,600 --> 00:00:20,760
to the Raspberry Pi, the Raspberry Pi.

5
00:00:20,760 --> 00:00:22,170
We receive that message.

6
00:00:22,710 --> 00:00:30,720
We check that it corresponds to a button priced message and then it will choose a random entry so the

7
00:00:30,720 --> 00:00:35,940
red, the green and blue, and it will choose a random number between zero and 255.

8
00:00:36,270 --> 00:00:42,770
And it will send that back to the Arduino, and an algorithm is going to process this command and caller

9
00:00:42,780 --> 00:00:44,070
on accordingly.

10
00:00:44,400 --> 00:00:50,340
One of the color of the ending weaved a number that we have received with analog, right?

11
00:00:50,640 --> 00:00:54,420
OK, so on the original site, you're going to have two actions.

12
00:00:54,450 --> 00:00:57,120
The first is to read the pushbutton.

13
00:00:57,330 --> 00:00:59,730
The second is to read the sale.

14
00:00:59,940 --> 00:01:02,930
So you read the pushbutton, you send a message to the API.

15
00:01:02,940 --> 00:01:03,870
So the Raspberry Pi.

16
00:01:04,320 --> 00:01:09,150
And he went, I'm not going to tell you what exact message you need to send.

17
00:01:09,180 --> 00:01:16,290
OK, I'll leave that up to you so you can practice on defining a good protocol for sending and receiving

18
00:01:16,290 --> 00:01:16,770
data.

19
00:01:17,100 --> 00:01:21,930
And then when it further ogbia LDI have given you an example here, because that's maybe a little bit

20
00:01:21,930 --> 00:01:22,760
more complex.

21
00:01:22,770 --> 00:01:24,540
So I give you an example first.

22
00:01:25,080 --> 00:01:31,050
What you can do, for example, if you send a command to pull on sort of changed the color on red and

23
00:01:31,590 --> 00:01:36,630
then you can send something that starts with red color and then the color, for example.

24
00:01:37,410 --> 00:01:38,040
56.

25
00:01:38,040 --> 00:01:38,400
Like this?

26
00:01:38,400 --> 00:01:44,400
OK, if you send something with the green, then you're going to get a green call on Kunhardt, OK and

27
00:01:44,400 --> 00:01:49,620
blue color, etc. And so you can send out from the Raspberry Pi and then on the old, you know what

28
00:01:49,620 --> 00:01:51,480
you can do instead of comparing.

29
00:01:51,510 --> 00:01:57,150
So the equality with string, which you can't do because you don't actually know what number you're

30
00:01:57,150 --> 00:01:58,740
going to get, this is valuable.

31
00:01:59,010 --> 00:02:04,810
You can do come that starts with and then the name of the command color.

32
00:02:05,220 --> 00:02:10,320
OK, if this starts with this, then you're going to process this and how to extract it.

33
00:02:10,320 --> 00:02:11,490
The number that is here.

34
00:02:11,850 --> 00:02:13,890
Well, you can feel the command that removed.

35
00:02:14,340 --> 00:02:19,020
So this is going to remove the first here, the first part of the string.

36
00:02:19,030 --> 00:02:22,470
So you have index zero, one, two, three and four.

37
00:02:22,800 --> 00:02:28,290
So this is going to remove completely this path and you're just left with the number, but the number

38
00:02:28,290 --> 00:02:29,190
is still a string.

39
00:02:29,400 --> 00:02:29,760
OK?

40
00:02:29,790 --> 00:02:32,070
Because you receive a string of the number is still a string.

41
00:02:32,340 --> 00:02:34,380
So then you do come in to end.

42
00:02:34,540 --> 00:02:38,700
The result of that is going to go inside an integer right that you can use.

43
00:02:38,700 --> 00:02:40,140
Then we are all right.

44
00:02:40,420 --> 00:02:40,650
OK.

45
00:02:40,680 --> 00:02:43,020
And you can do the same with green in the same with blue.

46
00:02:43,500 --> 00:02:49,170
Now on the Raspberry Pi side, so you're going to initialize cellular and then you're going to do a

47
00:02:49,170 --> 00:02:51,060
white room like we did before.

48
00:02:51,720 --> 00:02:56,610
And you're going to check if you receive some command from the Arduino, if you receive something you

49
00:02:56,610 --> 00:03:01,770
take, if the button has been priced, if yes, then you're going to choose the random number.

50
00:03:01,770 --> 00:03:03,810
So between zero and two?

51
00:03:04,440 --> 00:03:10,110
OK, so that you can have zero, one or two, which means bright green on blue, and then you're going

52
00:03:10,110 --> 00:03:13,980
to choose another number with zero and 255.

53
00:03:14,010 --> 00:03:20,550
You're going to construct a string that correspond to the command you're going to send to the oven.

54
00:03:20,640 --> 00:03:27,090
So to choose a random number, you can, well, just import the random and then do random that run into

55
00:03:27,090 --> 00:03:29,340
like this with the minimum and the maximum.

56
00:03:29,640 --> 00:03:35,370
OK, and this activity is actually a good example of how to use the combination of Raspberry Pi, an

57
00:03:35,370 --> 00:03:41,050
Arduino by complete application where the output is basically the muzzle of the application.

58
00:03:41,070 --> 00:03:41,370
OK.

59
00:03:41,610 --> 00:03:43,230
It's going to read from Sense, though.

60
00:03:43,230 --> 00:03:47,190
It's going to actually some sense, though, but it's not going to decide what to do.

61
00:03:47,340 --> 00:03:50,820
And then the Raspberry Pi he decides on what to do.

62
00:03:51,000 --> 00:03:54,210
So the Raspberry Pi is actually the brain of the application.

63
00:03:54,220 --> 00:04:01,320
So you have the brain and Amazon, and basically that's how things work in many different project windows

64
00:04:01,530 --> 00:04:01,830
box.

65
00:04:02,280 --> 00:04:06,450
OK, so now I'm going to see you in the next video form the solution.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:06,690
This is the solution of the activity and the five, when you have to send a message from the other to

2
00:00:06,690 --> 00:00:14,340
the Raspberry Pi, when you press on the push button and then receive a call for one of the ends, so

3
00:00:14,340 --> 00:00:18,930
basically one of the core of the LGB entity and then change that color from the other.

4
00:00:19,410 --> 00:00:25,920
So once again, let's start to do the original code and then we're going to debate it at 10:00 with

5
00:00:25,920 --> 00:00:26,720
the same when you talk.

6
00:00:27,000 --> 00:00:30,390
And then we're going to write the Python program under Iceberg Pine.

7
00:00:30,960 --> 00:00:34,070
So let's initialize and remove these.

8
00:00:34,650 --> 00:00:41,280
Let's initialize the how to a component, so define button pin, which has been number seven.

9
00:00:41,980 --> 00:00:42,300
Nine.

10
00:00:42,600 --> 00:00:43,170
Define.

11
00:00:44,100 --> 00:00:49,230
I'll be right, PIN, which is 11.

12
00:00:50,500 --> 00:00:53,230
Let's do the same for the green and the blue.

13
00:00:55,020 --> 00:00:55,470
Green.

14
00:00:57,520 --> 00:01:01,510
Blue and we have 10 and we have nine.

15
00:01:02,320 --> 00:01:02,570
OK.

16
00:01:02,990 --> 00:01:07,920
He never said that what we do is being mowed.

17
00:01:08,320 --> 00:01:14,560
We button being input.

18
00:01:16,510 --> 00:01:17,470
And then being mode.

19
00:01:18,810 --> 00:01:29,940
On the red pin to output and then to sing for the green, to sing for.

20
00:01:31,510 --> 00:01:37,750
Blue, so I go quite fast with that, because we've already done that multiple times.

21
00:01:38,590 --> 00:01:45,400
And then I'm going to open communications with Sam to begin with.

22
00:01:45,940 --> 00:01:47,290
Let's keep this thing straight.

23
00:01:49,350 --> 00:01:50,130
And why?

24
00:01:53,190 --> 00:01:55,410
Sarah, let's wait.

25
00:01:56,130 --> 00:01:56,490
All right.

26
00:01:57,780 --> 00:01:58,980
Now what do we do?

27
00:01:59,130 --> 00:02:02,010
I'm going to also remove that.

28
00:02:03,490 --> 00:02:07,630
So we have two things to do, which are, well, actually completely independent.

29
00:02:08,260 --> 00:02:15,570
First, we need to read the budget and check when it is priced and send a message to the sale.

30
00:02:16,300 --> 00:02:20,760
The second action is to receive something from the sale and check what's coming.

31
00:02:20,770 --> 00:02:25,740
We have it's red, green and blue and then apply the command to the AGP.

32
00:02:26,380 --> 00:02:31,540
So while there is no particular order to do that, you can do both independently.

33
00:02:31,540 --> 00:02:37,510
But let's start with let's see the president OK, so I'm going to do the debone code for the president

34
00:02:37,510 --> 00:02:45,460
and wants more unsigned long last time, but button changed.

35
00:02:46,690 --> 00:02:52,030
Let's see minutes and then unsigned long button.

36
00:02:53,830 --> 00:03:01,030
It's a dearborn's delay is let's put 50 milliseconds over time.

37
00:03:01,600 --> 00:03:06,820
And then so I'm saying long time now is equal to.

38
00:03:07,630 --> 00:03:15,910
Minister, we get the current time, which is time now minus last time put on has changed.

39
00:03:16,780 --> 00:03:20,020
If this is greater or equal, then that becomes delay.

40
00:03:21,730 --> 00:03:34,090
Then we can enter this if and what we can do is the bite button state is equal to digital read from

41
00:03:34,570 --> 00:03:35,140
button.

42
00:03:36,580 --> 00:03:37,800
Then we will need to.

43
00:03:38,800 --> 00:03:42,760
So we will need to compare the button state can be produced button state.

44
00:03:43,090 --> 00:03:49,180
So I'm going to add he might produce button state.

45
00:03:50,320 --> 00:03:56,620
And just after we do the pin modes, I'm going to do previews buttons.

46
00:03:56,620 --> 00:04:02,350
State is equal to digital right from button been.

47
00:04:03,280 --> 00:04:11,200
So we have the first stage here at the beginning and then we are going to compare button states.

48
00:04:11,530 --> 00:04:19,710
So if this is different than the previous one, then we need to do two things we need to update.

49
00:04:19,710 --> 00:04:23,530
The last time to put on has changed to time now.

50
00:04:24,070 --> 00:04:26,500
OK, so then the debate is going to happen.

51
00:04:26,500 --> 00:04:30,760
Another time we're going to do the but button state.

52
00:04:32,060 --> 00:04:35,420
Is equal to one state.

53
00:04:36,780 --> 00:04:45,810
And then we can check if button state is equal to high here because we have a pool, don't register,

54
00:04:46,560 --> 00:04:51,180
then the bottom button is pressed.

55
00:04:52,180 --> 00:04:52,450
OK.

56
00:04:52,780 --> 00:04:56,470
And as you say, that's print, Alan.

57
00:04:58,250 --> 00:05:00,290
And well, what do we send here?

58
00:05:00,560 --> 00:05:02,900
I'm not going to do Button is pressed, OK?

59
00:05:03,140 --> 00:05:04,040
This is not a log.

60
00:05:04,100 --> 00:05:08,030
This is the same communication from the Arduino to the Raspberry Pi.

61
00:05:08,750 --> 00:05:18,050
So let's it, we're going to send button priced like this, and here we're going to receive button press,

62
00:05:18,110 --> 00:05:18,440
OK?

63
00:05:19,570 --> 00:05:24,790
So very important to agree on what you said and what you'll receive and when.

64
00:05:25,150 --> 00:05:29,050
I'm going to just check you that code is working.

65
00:05:29,620 --> 00:05:32,590
So activity five.

66
00:05:33,910 --> 00:05:35,500
Compiling, uploading.

67
00:05:36,760 --> 00:05:43,450
OK, let's open and say and monitor, and let's press on the push button button, pressed the time button

68
00:05:43,450 --> 00:05:45,150
pressed button priced.

69
00:05:45,400 --> 00:05:47,530
It is working great.

70
00:05:47,920 --> 00:05:51,140
So now let's do the code for the algae added.

71
00:05:51,970 --> 00:05:53,980
So we have this already.

72
00:05:54,580 --> 00:06:00,760
We have the initialization, which is OK, now let's do so here and avoid loop.

73
00:06:01,000 --> 00:06:06,850
Make sure you don't make a mistake and that you don't put the code in the wrong block of code.

74
00:06:07,330 --> 00:06:10,870
So that's going to be key if.

75
00:06:13,460 --> 00:06:20,450
Say I'm not really even greater than zero, so that doesn't change, right?

76
00:06:22,550 --> 00:06:24,950
Then so if we have received something.

77
00:06:26,260 --> 00:06:27,190
We're going to string.

78
00:06:30,320 --> 00:06:34,520
Simply command is equal to say no doubt, and guess what?

79
00:06:34,850 --> 00:06:41,580
Read string until backslash and one single quote.

80
00:06:43,340 --> 00:06:47,070
And then if and that's where we are going to check what's coming.

81
00:06:47,090 --> 00:06:50,930
We have received it because here we can receive three different comment.

82
00:06:51,350 --> 00:07:00,980
So if command that starts with so the government can start, we, for example, raid like this, then

83
00:07:00,980 --> 00:07:02,750
we're going to process the right comment.

84
00:07:03,200 --> 00:07:14,190
And then as if Cindy, not that we've we have green, OK?

85
00:07:15,350 --> 00:07:22,780
And if CMT don't stop, we blue.

86
00:07:25,400 --> 00:07:29,270
And then let's do another and like I did before.

87
00:07:30,560 --> 00:07:37,400
Nothing from or maybe what we could do if we receive an error is just to, for example, pull off completely

88
00:07:37,700 --> 00:07:38,300
the RGV.

89
00:07:38,300 --> 00:07:39,740
Anyway, OK, it's up to you.

90
00:07:41,130 --> 00:07:49,560
So if we receive the right color, what we can do with the command is first to do see and not remove

91
00:07:49,950 --> 00:07:51,930
and then zero for.

92
00:07:53,560 --> 00:07:56,920
We removed so zero one, two, three four.

93
00:07:57,160 --> 00:08:00,820
We remove all of that and we are left with the No.

94
00:08:01,090 --> 00:08:09,910
But de novo executives strengths that we do, for example, eat raid is equal to see and the good to

95
00:08:11,230 --> 00:08:15,810
eat like this and an analogue right.

96
00:08:16,410 --> 00:08:24,820
We've GB right in and with the red number that we got from the command.

97
00:08:25,750 --> 00:08:30,220
And what we can do the same with every other comment.

98
00:08:30,520 --> 00:08:32,560
So certainly not boring.

99
00:08:32,890 --> 00:08:38,500
But here we don't do zero four because if we do zero four, we're going to remove one two three four.

100
00:08:38,740 --> 00:08:43,420
And we are going to be left with any column and a number.

101
00:08:43,810 --> 00:08:44,410
So we do.

102
00:08:44,440 --> 00:08:47,920
Zero one two three four five six.

103
00:08:48,040 --> 00:08:48,340
OK.

104
00:08:48,790 --> 00:08:54,010
So as you can see each command, you would need to process it independently and make sure that it's

105
00:08:54,010 --> 00:08:54,520
working.

106
00:08:55,270 --> 00:08:59,530
It's green is equal to him, to it.

107
00:08:59,650 --> 00:09:04,780
This doesn't change in an analog, so let's use another right the same.

108
00:09:04,780 --> 00:09:05,110
But.

109
00:09:07,120 --> 00:09:07,570
We've.

110
00:09:09,630 --> 00:09:11,190
Green and.

111
00:09:13,020 --> 00:09:13,380
Green.

112
00:09:15,520 --> 00:09:16,660
Oh, okay.

113
00:09:17,450 --> 00:09:18,530
And then for the blue.

114
00:09:20,440 --> 00:09:24,610
We do see to remove and how many do we need to remove?

115
00:09:25,150 --> 00:09:29,260
One two three four five four zero five.

116
00:09:29,710 --> 00:09:35,050
And then in blue is equal to CND, not to it.

117
00:09:35,590 --> 00:09:42,760
And let's do another the right we've the blue pin and the blue colour.

118
00:09:44,020 --> 00:09:45,470
OK, and now we can try.

119
00:09:45,530 --> 00:09:52,510
It is good actually to check if it's correctly working and well if you want an additional debug stick

120
00:09:52,510 --> 00:09:56,410
because maybe well, let's say you want to send the rhino the green on the blue component.

121
00:09:56,410 --> 00:09:57,250
It doesn't work.

122
00:09:57,490 --> 00:10:00,360
You don't necessarily know why it doesn't work.

123
00:10:00,370 --> 00:10:06,850
So what you can do, for example, let's see here say, yeah, print Ellen, for example, red.

124
00:10:07,330 --> 00:10:11,500
So we can just use this when we did the same moneyto.

125
00:10:11,650 --> 00:10:13,310
And then, of course, that's very important.

126
00:10:13,330 --> 00:10:17,980
Don't forget to remove any log that you have, but first for the other of.

127
00:10:18,730 --> 00:10:21,070
So let's upload the code to the original.

128
00:10:23,560 --> 00:10:31,150
Let's open the ceremony tall, so we still have the push button that will show button pressed and then

129
00:10:31,150 --> 00:10:34,320
let's do a red column 200.

130
00:10:35,110 --> 00:10:41,940
You can see it is currently working and we have 200 OK at the Green 100.

131
00:10:42,700 --> 00:10:49,780
OK, we have a different color than blue and 50 red to blue, actually 200.

132
00:10:50,920 --> 00:10:51,250
OK.

133
00:10:51,400 --> 00:10:52,420
And maybe red.

134
00:10:53,020 --> 00:10:56,350
Zero right green.

135
00:10:57,610 --> 00:11:00,910
Zero blue to 100.

136
00:11:01,300 --> 00:11:03,100
Well, there is something wrong with blue.

137
00:11:05,390 --> 00:11:11,580
And well, actually, I have children I have used, I don't know why, but 19 for the RGV blueprints.

138
00:11:11,600 --> 00:11:12,920
Of course, that doesn't work.

139
00:11:13,190 --> 00:11:14,900
So you can see here that didn't work.

140
00:11:14,900 --> 00:11:16,520
We didn't see the coming blue change.

141
00:11:16,670 --> 00:11:20,780
And then it helped us to actually see that we had an error in our codes.

142
00:11:20,780 --> 00:11:23,150
And now let's run that again.

143
00:11:25,990 --> 00:11:34,420
I'm going to have to say, and when you go in and just the blue with 200 hundred and well, the blue

144
00:11:34,420 --> 00:11:38,890
is working great, so I can just close that.

145
00:11:39,190 --> 00:11:43,660
I can also do a sail print with the blue to make sure that we receive from sail.

146
00:11:44,110 --> 00:11:45,070
And I'm going to run.

147
00:11:45,130 --> 00:11:45,940
This is very important.

148
00:11:46,000 --> 00:11:51,730
Any luggage that I have, but which have nothing to do with the same communication with the Rozenberg

149
00:11:51,730 --> 00:11:51,970
Pi.

150
00:11:52,420 --> 00:11:56,170
OK, so no, the Arduino code is working.

151
00:11:56,170 --> 00:12:01,270
I'm going to upload also the new code, of course, without the standard print in it.

152
00:12:02,410 --> 00:12:02,710
OK.

153
00:12:03,570 --> 00:12:04,630
The side is working.

154
00:12:05,230 --> 00:12:07,750
Let's go to the Raspberry Pi side.

155
00:12:08,680 --> 00:12:15,190
So first of all, we need to initialize cellular and everything, but I'm going to use the code from

156
00:12:15,280 --> 00:12:20,950
the previous activity, so select everything so you can do this by yourself.

157
00:12:21,400 --> 00:12:25,390
But I'm going to do this so it goes a bit faster.

158
00:12:26,020 --> 00:12:30,040
Anyway, we have already done that multiple times.

159
00:12:30,550 --> 00:12:31,240
So what?

160
00:12:31,240 --> 00:12:32,260
I'm going to remove that.

161
00:12:32,380 --> 00:12:33,010
So.

162
00:12:34,990 --> 00:12:43,990
Just the import initialization and then the infinite loop with the timed slip very important.

163
00:12:44,590 --> 00:12:51,670
And I'm going to say I'm going to import random here and let's remove that.

164
00:12:52,870 --> 00:12:53,350
OK.

165
00:12:54,460 --> 00:12:56,890
So what do we do on the Raspberry Pi?

166
00:12:56,920 --> 00:13:03,490
Well, we don't send anything without receiving anything, so we first need to check that we have received

167
00:13:03,490 --> 00:13:04,000
something.

168
00:13:04,270 --> 00:13:14,350
So in the way true, if say, that's in waiting is greater than zero again without parentheses, then

169
00:13:14,350 --> 00:13:14,740
we do.

170
00:13:15,250 --> 00:13:20,130
Let's say mrJ is equal to and from.

171
00:13:20,200 --> 00:13:25,430
We said we could also do a mzgee, for example, as the same as using C in this document.

172
00:13:25,430 --> 00:13:26,680
OK, that's pretty explicit.

173
00:13:27,010 --> 00:13:29,140
And that's something you're going to use very often.

174
00:13:29,530 --> 00:13:31,450
So that's not a big deal.

175
00:13:32,140 --> 00:13:34,840
And so said that great line.

176
00:13:35,020 --> 00:13:35,470
But.

177
00:13:37,580 --> 00:13:38,300
Decode.

178
00:13:39,770 --> 00:13:41,210
UTF eight.

179
00:13:42,920 --> 00:13:44,360
That's a trick.

180
00:13:46,400 --> 00:13:53,690
OK, and then what we do is we check if MRJ is equal to is equal to what is equal to.

181
00:13:54,290 --> 00:13:55,130
Button pressed.

182
00:13:55,820 --> 00:13:58,010
OK, we send button pressed.

183
00:13:58,010 --> 00:13:59,180
We check if we receive.

184
00:13:59,370 --> 00:14:00,140
Button pressed.

185
00:14:00,350 --> 00:14:05,570
If we have received button priced, then we are going to process the action.

186
00:14:05,810 --> 00:14:12,500
And what is the action is to choose a random color so bright green and blue and then the random number

187
00:14:12,500 --> 00:14:13,160
for that color.

188
00:14:13,760 --> 00:14:25,640
OK, so let's do it is equal to random that brand int we zero and two.

189
00:14:27,990 --> 00:14:39,450
And then the number is equal to random, don't run it from zero to two hundred and fifty five.

190
00:14:40,600 --> 00:14:44,100
OK, and then we're going to constrict the stream that we're going to send.

191
00:14:44,230 --> 00:14:49,920
OK, so the command and so let's start we've seen is equal to an empty string.

192
00:14:50,250 --> 00:15:02,220
And then if energy is equal to one, we see on the plus red.

193
00:15:03,610 --> 00:15:09,280
And then let's do, if any, is equal to two we see in the.

194
00:15:10,900 --> 00:15:20,980
Plus Green and then as seen the plus the.

195
00:15:22,420 --> 00:15:29,230
So we have the first parts of the command, and then we add so the plus.

196
00:15:30,690 --> 00:15:39,090
No, but actually as train, so we cast the number as train and then see the plus.

197
00:15:40,420 --> 00:15:47,590
Backslash, and if we start from an empty string, then we construct it, we first.

198
00:15:48,610 --> 00:15:55,690
The common name right, green and blue and then the number we want to read that we're going to get here

199
00:15:56,560 --> 00:16:00,430
and in backslash name for the red string until we've been backslash in.

200
00:16:01,190 --> 00:16:05,010
OK, and then we can do set that right.

201
00:16:06,590 --> 00:16:09,320
CNN did not include YouTube.

202
00:16:10,780 --> 00:16:13,180
They'd like this.

203
00:16:14,260 --> 00:16:17,140
And let's see if that works.

204
00:16:17,590 --> 00:16:21,610
Maybe we can add some prints here because it's easier to devote on Python.

205
00:16:21,970 --> 00:16:22,960
We can add, some bring.

206
00:16:22,960 --> 00:16:24,610
So let's see here.

207
00:16:24,700 --> 00:16:25,150
Brent.

208
00:16:27,230 --> 00:16:28,550
Button has been priced.

209
00:16:31,050 --> 00:16:33,240
OK, and then maybe.

210
00:16:34,740 --> 00:16:40,320
Print send comment plus comment.

211
00:16:41,550 --> 00:16:44,160
So we're going to make sure that we send the correct comment.

212
00:16:44,550 --> 00:16:46,950
OK, because we knew that our site is working.

213
00:16:47,490 --> 00:16:53,580
So if we send something from the Raspberry Pi to the remote and if it doesn't work well, we probably

214
00:16:53,580 --> 00:16:56,680
know that this is because we send the wrong thing.

215
00:16:56,700 --> 00:17:00,180
So if we just print the thing, it's easier to debug.

216
00:17:00,840 --> 00:17:03,810
Let's save this as activity.

217
00:17:05,370 --> 00:17:05,940
Five.

218
00:17:07,950 --> 00:17:12,050
And so the Arduino is already uploaded.

219
00:17:12,120 --> 00:17:16,080
Let's run it on the Raspberry Pi.

220
00:17:18,290 --> 00:17:18,650
OK.

221
00:17:18,680 --> 00:17:20,150
You can see Sergio, OK?

222
00:17:20,570 --> 00:17:23,810
I know what what I need to do is I need to press on the power button and let's see.

223
00:17:25,370 --> 00:17:30,590
OK, we have an error and we're actually OK.

224
00:17:30,620 --> 00:17:32,920
The modular random has no attribute run.

225
00:17:32,930 --> 00:17:38,570
It's simply because what I have to use, I lowercase here.

226
00:17:39,950 --> 00:17:43,610
I have used uppercase, but it is a lowercase.

227
00:17:43,610 --> 00:17:44,630
I made a mistake.

228
00:17:45,110 --> 00:17:46,490
So no, let's run again.

229
00:17:50,490 --> 00:17:57,810
Sale, OK, let's press on the push button and you can see Button has been pressed, send comment,

230
00:17:57,810 --> 00:17:58,230
right?

231
00:17:58,530 --> 00:18:00,830
125, I press again.

232
00:18:02,080 --> 00:18:06,290
Send comments or write again here, right again.

233
00:18:06,310 --> 00:18:10,300
We've study and you can you can see Blue 237.

234
00:18:11,470 --> 00:18:19,330
Green, 36, green 200, because everything would change one color, 174 for blue.

235
00:18:19,540 --> 00:18:26,050
Etc., etc. Then I breast control see OK, and you can see adding some.

236
00:18:28,090 --> 00:18:34,690
Print here on the Python site is very, very useful to see what you send, and then you can check that

237
00:18:34,840 --> 00:18:38,500
it's correctly doing what you want to do on the original site.

238
00:18:38,890 --> 00:18:40,870
And that's the end of this activity.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,990
In this new activity, and just before we go to check the Raspberry Pi functionalities, we are going

2
00:00:06,990 --> 00:00:09,720
to use the seven model panels NASA the push button.

3
00:00:09,990 --> 00:00:17,070
So basically, the Raspberry Pi here will be responsible to do a sweep of the seven so you can take

4
00:00:17,070 --> 00:00:18,210
one of the premier's listen.

5
00:00:18,210 --> 00:00:24,870
When I did the code for the seven wutah and basically to sweep is that you're going to go from the angle

6
00:00:24,880 --> 00:00:33,180
zero to angle 180 on the seven model and then come back from one hundred eighty two zero with a small

7
00:00:33,180 --> 00:00:36,630
delay in between, for example, 10 milliseconds.

8
00:00:36,900 --> 00:00:38,370
That was our example.

9
00:00:38,770 --> 00:00:43,890
And so you will see the several going from the minimum position to the maximum coming back to the minimum,

10
00:00:43,890 --> 00:00:46,260
etc., etc. in an infinite loop.

11
00:00:47,100 --> 00:00:50,730
But this time we are not going to sweep on the Arduino.

12
00:00:50,730 --> 00:00:53,820
We we're going to do the sweep under a Raspberry Pi with Python code.

13
00:00:54,300 --> 00:00:54,570
OK.

14
00:00:54,720 --> 00:00:58,140
So I'm going to say the code is going to be actually quite simple.

15
00:00:58,570 --> 00:01:04,350
OK, so you're going to read from sale and receive a seven command, which contains an angle between

16
00:01:04,350 --> 00:01:06,120
zero and 180.

17
00:01:06,630 --> 00:01:07,350
So what is?

18
00:01:07,680 --> 00:01:14,250
I don't give you the protocol, but you can get some inspiration from what we did with the RGV Energy

19
00:01:14,430 --> 00:01:16,780
to send a simple command and a number.

20
00:01:16,830 --> 00:01:19,200
OK, so you can do something similar for the simple.

21
00:01:19,650 --> 00:01:24,660
You're also going to read from the pushbutton like we did before and when it's priced.

22
00:01:24,660 --> 00:01:27,740
You send a message to the Raspberry Pi and on the Raspberry Pi.

23
00:01:27,750 --> 00:01:30,540
So that is where actually we would have the most code here.

24
00:01:30,840 --> 00:01:35,460
So I have given you some few code examples to help you get started.

25
00:01:35,790 --> 00:01:36,870
So you're going to do a sweep.

26
00:01:36,910 --> 00:01:39,510
Here we have, for example, five milliseconds.

27
00:01:39,540 --> 00:01:41,490
OK, so here we use seven.

28
00:01:41,590 --> 00:01:49,230
OK, so five minutes signal is zero point zero zero five SIM in your kind of voi loop here in the way

29
00:01:49,260 --> 00:01:56,460
true, once you're going to do is so I am first time to sleep with zero zero zero one.

30
00:01:56,850 --> 00:02:01,560
So again, we don't want to make the way to go at full speed.

31
00:02:01,860 --> 00:02:06,690
We're going to reduce the speed a bit, which is going to reduce a lot the CPU usage.

32
00:02:07,500 --> 00:02:14,790
And so here before we used zero point zero one, which is going to make the Wailuku at 100 hits here,

33
00:02:14,790 --> 00:02:18,270
I'm going to use zero point zero zero one.

34
00:02:18,600 --> 00:02:21,480
So the loop is going to run at one thousand hits.

35
00:02:21,810 --> 00:02:24,090
OK, because we're going to use that kind of time.

36
00:02:24,120 --> 00:02:24,420
OK.

37
00:02:24,690 --> 00:02:25,710
Five millisecond.

38
00:02:26,220 --> 00:02:30,300
So we need a loop that runs faster than the delay action.

39
00:02:30,340 --> 00:02:30,630
OK.

40
00:02:31,290 --> 00:02:37,500
And we can do this here is because, well, we are not going to use time that slip to wait between two

41
00:02:37,500 --> 00:02:38,910
changes in the angle.

42
00:02:38,940 --> 00:02:39,300
OK.

43
00:02:39,780 --> 00:02:40,350
Why is that?

44
00:02:40,350 --> 00:02:48,010
Because we will also need to read from the set so we don't want to use timelessly to block the program.

45
00:02:48,390 --> 00:02:54,900
And so the only time that sleep is going to be the one that reduces a bit the speed of the loop here.

46
00:02:55,350 --> 00:02:57,000
And basically, we are going to do the same.

47
00:02:57,000 --> 00:02:58,110
As for that, I don't know.

48
00:02:58,120 --> 00:03:06,030
So in the a.m. when we wanted to do an action every x amount of time without using the delay, we use

49
00:03:06,030 --> 00:03:11,490
this trick to when we compare the previous time with the current time, and that's what we do here also.

50
00:03:11,760 --> 00:03:18,190
So what you can do is import a module and then we find the time you get the current time in seconds.

51
00:03:18,210 --> 00:03:18,510
OK.

52
00:03:18,940 --> 00:03:26,550
And so you can initiate last time action down to the runtime and put an action delay in second and then

53
00:03:26,640 --> 00:03:34,680
in the loop every time simply, you get the time and you do it on time, minus the last time, the previous

54
00:03:34,680 --> 00:03:39,690
time, which gives you a duration and you have this duration is greater than the delay.

55
00:03:39,900 --> 00:03:45,900
Then you do your action and you, of course, update the time when the action was down to the current

56
00:03:45,900 --> 00:03:46,230
time.

57
00:03:46,710 --> 00:03:52,380
OK, and after that, even before that, if you can also check if you have received something from cellular

58
00:03:52,950 --> 00:03:58,320
and then went to make several sweep, what you can do is you can add a valuable that is going to be,

59
00:03:58,320 --> 00:03:58,920
for example.

60
00:03:59,460 --> 00:04:00,210
Let's see.

61
00:04:01,420 --> 00:04:04,030
Several going up.

62
00:04:05,650 --> 00:04:06,890
Like, for example, a bullion.

63
00:04:06,910 --> 00:04:13,930
OK, so if it's going up every time you're going to add plus one to the angle and send plus one from

64
00:04:13,930 --> 00:04:21,590
the current angle until you reach 180 and then you put that to false.

65
00:04:22,000 --> 00:04:26,500
And if you are false, you're going to go down from 180 to zero.

66
00:04:26,860 --> 00:04:31,540
And when you reach zero, you put that to troop so you can go up again.

67
00:04:31,840 --> 00:04:33,370
OK, so that's how you do this week.

68
00:04:33,700 --> 00:04:39,430
And I have added another functionality that actually, when you press the push button on the Arduino,

69
00:04:39,670 --> 00:04:42,120
you're going to send a message to the Raspberry Pi here.

70
00:04:42,130 --> 00:04:45,910
You received a message and you're going to change the speed.

71
00:04:46,150 --> 00:04:49,060
So this bit is basically the delay.

72
00:04:49,900 --> 00:04:52,810
So the shorter the delay, of course, the higher the speed.

73
00:04:53,380 --> 00:04:59,560
And so here to make it simple, you can just create a list with different speeds of five milliseconds

74
00:04:59,560 --> 00:05:01,240
10, 15 20.

75
00:05:01,660 --> 00:05:08,410
And when you receive a message that the button has been pressed, you just go to the next speed, OK,

76
00:05:08,420 --> 00:05:10,570
and when you reach that one, you go back to the beginning.

77
00:05:11,050 --> 00:05:17,740
And so when you update actually the delay, well, that's going to also update this code because now

78
00:05:17,740 --> 00:05:21,460
you're going to check with the new action delay and you don't need to do anything else.

79
00:05:22,300 --> 00:05:22,630
All right.

80
00:05:22,640 --> 00:05:26,680
So to recap, here you do a sweep with Python.

81
00:05:26,920 --> 00:05:34,360
You send the several commands to the Arduino and for that, use a non blocking structure.

82
00:05:35,080 --> 00:05:41,560
And you also read from sale so that when you press on the buzzer button, you send a message from Arduino

83
00:05:41,560 --> 00:05:42,560
to Raspberry Pi.

84
00:05:42,820 --> 00:05:50,200
And when you receive that message, you change the delay with one of the data that is in that list and

85
00:05:50,200 --> 00:05:53,500
I will see you in the next the and follow the solution.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,030
All right, this is the solution of the previous activity where you need to make the several sweep from

2
00:00:06,030 --> 00:00:11,400
the raspberry pipe and then you're going to change the speed when you press on the button, on the atrium.

3
00:00:11,520 --> 00:00:15,030
And so, well, once again, let's start with the aluminum side.

4
00:00:15,600 --> 00:00:24,150
So I'm going to do the button priced code and actually open the previous activity, which was five.

5
00:00:26,780 --> 00:00:34,520
So I am not going to write the complete code for the push button because we just did it in the activity

6
00:00:34,520 --> 00:00:40,220
and in one of the previous listen, so what if you want more explanation, please go back.

7
00:00:42,090 --> 00:00:46,650
In a previous video to get the explanations of that, I'm just going to repeat.

8
00:00:48,960 --> 00:00:55,740
The cut that we already are before, so that doesn't come from nowhere, that comes from something we

9
00:00:55,740 --> 00:00:56,610
have or we don't.

10
00:00:57,750 --> 00:01:03,120
OK, and I'm going to also initialize the cellular as always.

11
00:01:03,570 --> 00:01:08,970
And then, well, you see, that's the part of the code I want to copy here because we're not going

12
00:01:08,970 --> 00:01:10,710
to write that again.

13
00:01:12,070 --> 00:01:14,860
He and I set out to do that.

14
00:01:15,130 --> 00:01:22,180
So in our crowdfunder, we have so defined for the buttons and variables, we initialize the button

15
00:01:22,180 --> 00:01:23,110
and the produce state.

16
00:01:24,470 --> 00:01:30,680
And then in the void, look to make sure you have the correct blocks of code here, so well, in the

17
00:01:30,920 --> 00:01:36,260
look, we read the current time, which had a duration since the time the button has changed.

18
00:01:36,910 --> 00:01:43,490
This is greater than the demons delay and read the budget, but then we compare it with the valuables

19
00:01:43,490 --> 00:01:47,630
and if it's high in the button has been priced and we send button priced.

20
00:01:48,230 --> 00:01:52,880
So just to be sure, let's look back to the original activity.

21
00:01:54,620 --> 00:01:55,070
Six.

22
00:01:59,300 --> 00:02:00,230
Don't imploding.

23
00:02:00,530 --> 00:02:07,320
Let's open the ceremony, throw a press on the push button button, press free, press multiple times.

24
00:02:07,340 --> 00:02:08,060
OK, great.

25
00:02:09,050 --> 00:02:10,650
Now let's do the code.

26
00:02:10,890 --> 00:02:11,840
I'll do several.

27
00:02:12,710 --> 00:02:20,210
So I am going to initialize with several, so define several Pentwyn.

28
00:02:20,960 --> 00:02:22,490
Let's include

29
00:02:26,240 --> 00:02:28,850
the several, but each library.

30
00:02:29,720 --> 00:02:33,740
And let's create so we can create it before that or after I do the matter.

31
00:02:34,340 --> 00:02:37,580
Several several semicolon.

32
00:02:39,380 --> 00:02:50,450
And here let's do several that attach several pin OK to several is initialized and now in the volume

33
00:02:50,450 --> 00:02:53,480
look after we have right before it does matter again.

34
00:02:53,900 --> 00:03:04,790
So after we have right on the pushbutton, let's do if Cellulant available greater than zero.

35
00:03:06,740 --> 00:03:07,920
And then let's check.

36
00:03:08,570 --> 00:03:10,940
So what come we're going to receive?

37
00:03:11,390 --> 00:03:18,560
This dual stream is equal to read string until backslash end.

38
00:03:20,810 --> 00:03:22,530
And then if command.

39
00:03:22,590 --> 00:03:22,970
But.

40
00:03:23,270 --> 00:03:25,420
So why do we want to receive?

41
00:03:25,430 --> 00:03:28,250
We want to receive the several command with a number.

42
00:03:28,820 --> 00:03:31,400
So let's say that we're going to receive something that starts.

43
00:03:32,960 --> 00:03:33,440
We've.

44
00:03:36,690 --> 00:03:40,050
Several column like this.

45
00:03:41,830 --> 00:03:44,200
And then the anger that we want.

46
00:03:45,010 --> 00:03:47,220
And so we can do command that ring.

47
00:03:48,640 --> 00:03:55,210
OK, we start at zero one two three four five six zero six.

48
00:03:56,650 --> 00:03:58,480
We are left with the numbers.

49
00:03:59,380 --> 00:04:04,720
Anger is equal to seem not to beat.

50
00:04:06,070 --> 00:04:10,930
What we could do also now, I'm not going to do it, but what we could do as an improvement is to check

51
00:04:10,930 --> 00:04:14,350
that the angle is actually between zero and 180.

52
00:04:14,470 --> 00:04:22,750
OK, so that we don't receive values that are negative, for example, are valued at greater than 180.

53
00:04:23,590 --> 00:04:29,650
And then we do several that right angle, and that's pretty much it.

54
00:04:30,190 --> 00:04:37,330
We have to go to send the button Christ's message, and we have the code to receive and execute the

55
00:04:37,330 --> 00:04:38,730
several command.

56
00:04:40,300 --> 00:04:41,070
That's Jack.

57
00:04:41,440 --> 00:04:41,890
Yes.

58
00:04:42,400 --> 00:04:46,630
I'm going to upload the code and test this code.

59
00:04:48,490 --> 00:04:55,840
And what actually do better if I do say the string until because this is part of the same library,

60
00:04:55,930 --> 00:05:00,040
not just a random function like this, it's blowed.

61
00:05:02,550 --> 00:05:05,040
Bloating down and bloating.

62
00:05:06,150 --> 00:05:07,920
That's up on the same monitor.

63
00:05:08,520 --> 00:05:09,780
And let's see what we have in the soup.

64
00:05:10,200 --> 00:05:17,700
First, what if you have like like me, if you have disconnected to several people helping to put it

65
00:05:17,700 --> 00:05:21,030
back, OK, because it's not, that's not going to work.

66
00:05:21,420 --> 00:05:27,660
So if I pressing the pause button still working, button pressed and then I'm going to do several,

67
00:05:27,660 --> 00:05:28,760
for example, zero.

68
00:05:29,610 --> 00:05:30,720
And let's press enter.

69
00:05:31,290 --> 00:05:32,430
OK, goes to zero.

70
00:05:32,580 --> 00:05:40,560
And then several wave one hundred fifty three, for example, it goes to one hundred fifty three.

71
00:05:41,010 --> 00:05:42,330
That's correctly walking.

72
00:05:42,990 --> 00:05:48,990
So I'm going to close that and what I think we are done with the original code.

73
00:05:49,020 --> 00:05:50,970
Let's now switch to the Raspberry Pi.

74
00:05:51,270 --> 00:05:54,940
So you could see that on the other well, we didn't have many things to do.

75
00:05:54,960 --> 00:05:55,310
OK.

76
00:05:56,770 --> 00:05:59,090
We just sent something here.

77
00:05:59,110 --> 00:06:00,650
We just received something here.

78
00:06:00,670 --> 00:06:03,470
There is no link between the two actions.

79
00:06:03,490 --> 00:06:03,760
Okay.

80
00:06:04,030 --> 00:06:07,720
The link between the two action is going to be on the Python site.

81
00:06:08,740 --> 00:06:11,300
So let's remove what?

82
00:06:11,320 --> 00:06:12,520
Let's remove all of that.

83
00:06:12,760 --> 00:06:14,500
Can we know what to do?

84
00:06:15,280 --> 00:06:20,350
Let's start from a blank page where a blank page, you know, because I'm going to use, of course,

85
00:06:20,350 --> 00:06:20,880
the structure.

86
00:06:20,890 --> 00:06:28,360
So let's go to any of the previous activity and let's just paste the structure, remove what we don't

87
00:06:28,360 --> 00:06:28,720
need.

88
00:06:30,480 --> 00:06:31,200
Like this?

89
00:06:32,580 --> 00:06:33,000
OK.

90
00:06:33,030 --> 00:06:35,850
That's District two to import stuff.

91
00:06:36,980 --> 00:06:42,010
Initialize cell communication and then our own kind of you.

92
00:06:42,620 --> 00:06:44,730
I'm going to put zero point zero one.

93
00:06:44,780 --> 00:06:51,740
OK, so we can run this loop at 1000 hits and no, well, let's do the seven sweep first.

94
00:06:52,040 --> 00:06:53,800
So we're going to start here.

95
00:06:53,820 --> 00:07:04,880
I'm going to put last time several move, for example, is equal to Typekit time and we have the time

96
00:07:04,880 --> 00:07:05,870
already embodied.

97
00:07:06,200 --> 00:07:11,720
And then let's see, several delay is equal to.

98
00:07:12,560 --> 00:07:19,550
So we're going to put the different delays after I'm going to start with zero zero five or let's do

99
00:07:20,030 --> 00:07:27,710
actually this, which is 10 milliseconds, not in our wild true after the timed slip.

100
00:07:27,920 --> 00:07:31,010
So I usually put this at the beginning, OK?

101
00:07:31,460 --> 00:07:36,560
Because if you put this at the end of your program and then you have something that is quite beat,

102
00:07:36,860 --> 00:07:38,100
then you might miss it.

103
00:07:38,390 --> 00:07:40,310
You might put a wrong indentation.

104
00:07:40,550 --> 00:07:43,640
So that's why I usually put that first OK as a best practice.

105
00:07:43,640 --> 00:07:48,560
So I don't remove it by mistake item, protein notation by mistake.

106
00:07:48,560 --> 00:07:49,490
I don't do any mistake.

107
00:07:49,820 --> 00:07:52,310
So any code I write after this time?

108
00:07:53,240 --> 00:07:54,110
And so, no, I do.

109
00:07:54,410 --> 00:08:02,770
Time now is equal to time to time, which is occurring time and second, if time.

110
00:08:02,930 --> 00:08:09,260
But now minus the last thing several move ends is greater than the several delay.

111
00:08:09,530 --> 00:08:12,650
So you can see this is very similar to what we did here.

112
00:08:12,650 --> 00:08:18,920
For example, with a perfect final minus last time is greater than the DNA.

113
00:08:19,250 --> 00:08:21,860
That's the exact same code, but with Python.

114
00:08:22,130 --> 00:08:24,380
So we do last time.

115
00:08:24,380 --> 00:08:31,400
Several move is equal to time now and then we can do the action.

116
00:08:31,730 --> 00:08:33,020
So what is the action?

117
00:08:33,320 --> 00:08:35,720
We're going to start from somewhere.

118
00:08:35,750 --> 00:08:36,980
OK, so let's see.

119
00:08:37,730 --> 00:08:41,900
Several angle is equal to 90.

120
00:08:42,020 --> 00:08:46,820
Let's start at 19, which is at the middle, and we're going to do several.

121
00:08:47,090 --> 00:08:49,640
Going up is equal to true.

122
00:08:49,940 --> 00:08:54,050
So we start at 90 and we go until 180 first.

123
00:08:54,320 --> 00:09:09,050
And so what we do is so if several going up, then we do several angle plus one and then else.

124
00:09:09,170 --> 00:09:17,090
So even if several is not going up, which means is going down several angles minus one.

125
00:09:17,540 --> 00:09:20,420
And so here the angle was 90.

126
00:09:20,810 --> 00:09:22,430
We put through here.

127
00:09:22,430 --> 00:09:23,480
So we go here.

128
00:09:23,600 --> 00:09:26,030
This angle is going to be 91.

129
00:09:26,480 --> 00:09:29,210
Now we also need to check, of course, when we reach the max.

130
00:09:29,810 --> 00:09:39,620
So if several angle is equal to 180 in that case, we're going to do several.

131
00:09:41,000 --> 00:09:50,510
Going up is equal to Fox so that the next time what we the next time is, we don't go here, the next

132
00:09:50,510 --> 00:09:51,190
time we go here.

133
00:09:51,560 --> 00:09:55,910
And then so the seven goal would be 180, but we do minus one.

134
00:09:56,420 --> 00:10:04,940
So one hundred seventy nine and then 178, etc. And then we also need to check here if several angle

135
00:10:04,970 --> 00:10:16,320
is equal to zero and we don't go lower and we do several, going up is equal to true.

136
00:10:16,580 --> 00:10:23,410
So the next time we don't go inside this block of code, we go inside this one and we start from zero

137
00:10:23,420 --> 00:10:28,130
one two three four five, etc. until we reach 180.

138
00:10:28,730 --> 00:10:31,170
And then we go back here until we reach zero.

139
00:10:31,190 --> 00:10:34,490
We go back, etc., etc. OK.

140
00:10:34,670 --> 00:10:41,060
And now that we have the several angles, so let's give the indentation we are in that if I'm going

141
00:10:41,090 --> 00:10:45,110
to come in is equal to seven.

142
00:10:47,040 --> 00:10:50,730
Minus plus several angles.

143
00:10:50,820 --> 00:11:02,100
But as a stream plus backslash end pay, so we make sure that we have the same comment as you several.

144
00:11:03,190 --> 00:11:12,910
Problem and in a number in backslash and full strength until backslash and OK, things are good, so

145
00:11:12,910 --> 00:11:21,040
we just need not to send the commands of say that's right, commands in code UTF eight.

146
00:11:22,810 --> 00:11:25,480
OK, so we have the delay mechanism with that.

147
00:11:26,440 --> 00:11:34,180
If in the time now and we have the sweep mechanism where we change the angle here and then we send the

148
00:11:34,180 --> 00:11:34,750
command.

149
00:11:35,380 --> 00:11:38,470
So here we are, going to send the command every 10 milliseconds.

150
00:11:39,040 --> 00:11:46,510
OK, let's save this as activity six p y.

151
00:11:47,590 --> 00:11:49,690
Let's first try this, actually.

152
00:11:49,710 --> 00:11:50,050
OK.

153
00:11:50,740 --> 00:11:54,070
So I am going to run the script.

154
00:11:54,220 --> 00:11:54,790
OK.

155
00:11:54,830 --> 00:11:55,900
The cell is connected.

156
00:11:56,520 --> 00:12:02,160
And what you can see, this level is sweeping grace.

157
00:12:02,230 --> 00:12:02,890
It's working.

158
00:12:04,330 --> 00:12:08,830
I'm just going to just going to get fired up so he doesn't make noise and will.

159
00:12:09,070 --> 00:12:12,000
Let's continue with the following parts of the code.

160
00:12:12,610 --> 00:12:13,010
All right.

161
00:12:13,920 --> 00:12:14,860
Controls here.

162
00:12:16,420 --> 00:12:21,550
So you can see here we already have a sweep command from the Raspberry Pi to the Arduino, and we do

163
00:12:21,550 --> 00:12:23,920
this sweep instead of in the oven.

164
00:12:24,670 --> 00:12:30,960
Now I'm going to add a list, so let's see the list here.

165
00:12:31,000 --> 00:12:36,760
Let's do several delays is equal to and so we had zero point.

166
00:12:37,790 --> 00:12:44,390
Zero and zero, five and zero point zero one, so that's all the delays in milliseconds.

167
00:12:46,320 --> 00:12:47,690
So 15 and.

168
00:12:48,880 --> 00:12:55,630
Prince, let's go with that, and let's say that the several well, actually, let's put that before

169
00:12:56,770 --> 00:12:57,970
several delays.

170
00:12:58,900 --> 00:13:00,880
Several delays.

171
00:13:01,630 --> 00:13:02,020
Zero.

172
00:13:02,180 --> 00:13:03,700
The first one.

173
00:13:05,320 --> 00:13:06,880
OK, so we start here.

174
00:13:06,880 --> 00:13:11,020
We don't start at 10 milliseconds and we start at five.

175
00:13:11,050 --> 00:13:11,350
OK?

176
00:13:12,250 --> 00:13:13,210
And no.

177
00:13:13,810 --> 00:13:17,170
Well, in order to change that, I'm going to read from the set.

178
00:13:17,560 --> 00:13:20,410
So we have this first block of code.

179
00:13:21,540 --> 00:13:23,660
So that's the comment here.

180
00:13:26,100 --> 00:13:26,550
Sweep.

181
00:13:27,120 --> 00:13:35,370
So to put some species to make it more readable and then let's do change.

182
00:13:36,840 --> 00:13:38,020
Several speak.

183
00:13:39,900 --> 00:13:44,670
So although here doesn't matter, you could do that before, do that before because we're going to go

184
00:13:44,670 --> 00:13:46,110
very fast in this loop.

185
00:13:46,740 --> 00:13:52,410
And so what do we do if Senate votes in waiting greater than zero?

186
00:13:53,970 --> 00:14:01,920
Then we do is equal to say that red line, that's the UTF.

187
00:14:03,530 --> 00:14:06,410
Hate does not restrict.

188
00:14:09,240 --> 00:14:13,920
We check if Missy is equal to button priced.

189
00:14:14,880 --> 00:14:16,200
Let's use that directly.

190
00:14:18,260 --> 00:14:26,690
Then what we simply need to do is to do a change here under several delay.

191
00:14:27,470 --> 00:14:35,600
And so we need to keep an index, actually, so let's do several delay index is equal to zero.

192
00:14:35,990 --> 00:14:42,530
Let's put that here and we're going to increment this.

193
00:14:43,100 --> 00:14:46,490
So we're going to do several.

194
00:14:48,430 --> 00:14:51,400
DeLay index just one.

195
00:14:51,970 --> 00:15:02,500
And of course, we need to check if several delay index is greater or equal, so just equal should be

196
00:15:02,500 --> 00:15:11,500
enough, but let's just use that as a more general condition to the length of several delays.

197
00:15:12,370 --> 00:15:17,350
So basically, here we are at zero, we do +1.

198
00:15:17,710 --> 00:15:24,040
We are at one plus one, we are two plus one, we are at three and +1.

199
00:15:24,040 --> 00:15:25,450
We are at index four.

200
00:15:25,450 --> 00:15:26,590
That doesn't exist.

201
00:15:26,790 --> 00:15:27,040
OK.

202
00:15:27,520 --> 00:15:30,280
The length of the list is four.

203
00:15:30,520 --> 00:15:30,820
OK.

204
00:15:31,060 --> 00:15:33,820
With the index zero one two three four.

205
00:15:34,510 --> 00:15:36,250
Well, actually zero one, two and three.

206
00:15:36,490 --> 00:15:43,570
If we reach number fall, which corresponds to the length of the list, then we are out of the list

207
00:15:43,570 --> 00:15:45,130
and we are going to get an error.

208
00:15:45,460 --> 00:15:49,090
So we check that if we arrive at the length, we simply do.

209
00:15:49,600 --> 00:15:55,540
Several delay index is equal to zero.

210
00:15:55,630 --> 00:15:56,710
We come back to zero.

211
00:15:57,550 --> 00:16:00,640
And now we are sure that we have a correct index and we simply do.

212
00:16:01,060 --> 00:16:10,330
Zero delay is equal to several delays with the several delay index.

213
00:16:11,530 --> 00:16:18,790
And so when we receive the button, we are simply going to change this value here with the next value

214
00:16:18,790 --> 00:16:19,780
on the list.

215
00:16:20,200 --> 00:16:25,810
And this is used where this is used here on this action.

216
00:16:25,990 --> 00:16:28,660
So we are going to change the speed of the action basically.

217
00:16:28,720 --> 00:16:30,790
OK, let's try that.

218
00:16:31,420 --> 00:16:35,050
So I am going to assume the other new code doesn't change.

219
00:16:35,050 --> 00:16:37,750
I'm going to run this again.

220
00:16:41,090 --> 00:16:48,020
So this is sweeping, you can see a little bit faster now every five minutes a pressing the push them.

221
00:16:49,140 --> 00:16:50,310
He's going slower.

222
00:16:51,510 --> 00:16:52,870
I'm pressing the button again.

223
00:16:53,610 --> 00:17:02,980
It's going slower, not every 15 milliseconds I press again, it's going slower every 20 millisecond.

224
00:17:03,390 --> 00:17:09,130
And I'm going to price and he's going to come back to the first element, which is five milliseconds,

225
00:17:09,870 --> 00:17:18,420
five, 10, 15 and 20 and five again.

226
00:17:18,960 --> 00:17:23,670
All right, I'm going to disconnect this just so it doesn't make any noise.

227
00:17:24,360 --> 00:17:25,620
And the code is working.

228
00:17:25,620 --> 00:17:27,270
So I'm going to press controlled, see?

229
00:17:27,480 --> 00:17:30,120
So I didn't put any log on the Python side.

230
00:17:30,720 --> 00:17:36,480
You could put some logs here when you actually change the delay, OK, to make sure that you have the

231
00:17:36,480 --> 00:17:37,320
correct delete.

232
00:17:38,070 --> 00:17:40,380
Adding some logs here may be too much.

233
00:17:40,580 --> 00:17:46,320
OK, if you print along every five milliseconds to show the angle, you may do that for debugging.

234
00:17:46,320 --> 00:17:49,920
But then, well, maybe that's too much for a normal use of the application.

235
00:17:49,920 --> 00:17:53,250
But here, for all the change of the delay, why not?

236
00:17:53,880 --> 00:17:55,980
OK, and that's the end of this activity.

237
00:17:56,190 --> 00:18:01,920
So here you can see that basically a code that you could do on the Arduino, which is so the application

238
00:18:01,920 --> 00:18:06,890
to make it several sweep, you can do that also from the Raspberry Pi.

239
00:18:06,900 --> 00:18:12,030
Okay, so you can choose basically where you control the logic of different parts of your application.

240
00:18:12,330 --> 00:18:19,200
So actually, here I did the sweep on the Raspberry Pi python as a good practice exercise, but maybe

241
00:18:19,590 --> 00:18:20,580
the best option?

242
00:18:20,760 --> 00:18:27,780
Well, depends on your application, but maybe the best option would be to do the sweep on the Arduino.

243
00:18:27,780 --> 00:18:33,960
So to handle this and the Arduino and then just sent from the Raspberry Pi, the delay that you want

244
00:18:33,960 --> 00:18:34,530
to use.

245
00:18:34,650 --> 00:18:35,040
OK.

246
00:18:35,730 --> 00:18:39,810
And the application would be exactly the same, and the result will be the same.

247
00:18:40,080 --> 00:18:44,640
But the code to sweep the several would be on the Arduino.

248
00:18:44,870 --> 00:18:52,530
So here you can see we are in the example where we could do this here on Python or this on C++.

249
00:18:53,040 --> 00:18:59,580
And so sometimes it's not necessarily super clear where you should, but which code and what you're

250
00:18:59,580 --> 00:19:02,900
going to simply learn more about that when you practice.

251
00:19:02,940 --> 00:19:07,950
We discuss and also after discourse, when you practice more and you do more projects, you're going

252
00:19:07,950 --> 00:19:12,930
to have a better idea of what to put on your Raspberry Pi, what to put on the Arduino.

253
00:19:13,140 --> 00:19:13,500
All right.

254
00:19:13,500 --> 00:19:17,280
And that's the end of the section on the Arduino functionalities.

255
00:19:17,490 --> 00:19:23,610
Now we are going to go to the Raspberry Pi functionalities and continue to explore the different things

256
00:19:23,620 --> 00:19:28,920
we can do with Raspberry Pi, an original and enough that we're going to start the final project.

257
00:19:29,080 --> 00:19:29,370
Other.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: PART 3 - Raspberry Pi Functionalities (Camera and Telegram Bot)

1
00:00:00,150 --> 00:00:05,730
You now have successfully built the outing, a secret for schools, which we will use for the final

2
00:00:05,730 --> 00:00:06,330
project.

3
00:00:06,780 --> 00:00:14,040
Also, you have practiced on controlling outdoor component from the Raspberry Pi right now in this section.

4
00:00:14,190 --> 00:00:21,120
We are going to focus on a few Raspberry Pi functionalities that we are going to use in the final project.

5
00:00:21,780 --> 00:00:23,130
The Arduino functionality functionalities.

6
00:00:23,140 --> 00:00:24,630
We are closer to the hardware.

7
00:00:24,930 --> 00:00:29,610
You will see that for Raspberry Pi, we would be much closer to the software.

8
00:00:30,240 --> 00:00:32,100
And what are we going to do?

9
00:00:32,400 --> 00:00:38,760
Well, first we will take some pictures with the Raspberry Pi camera and then something super fun.

10
00:00:38,920 --> 00:00:45,960
We will create a Telegram bot running on the bay so that we can, for example, send a notification

11
00:00:45,960 --> 00:00:52,830
to our phone and control the Raspberry Pi from the Telegram app on desktop or on mobile.

12
00:00:53,130 --> 00:01:00,930
If you don't know Telegram, well, this is just a messaging app like WhatsApp or Slack, etc. for both

13
00:01:00,930 --> 00:01:02,820
the camera and the Telegram modes.

14
00:01:03,120 --> 00:01:09,030
I'm going to keep things simple here and just use the functionalities that we will need for the project

15
00:01:09,330 --> 00:01:11,280
so we don't waste time.

16
00:01:11,940 --> 00:01:14,820
And then after that, I have added some more practice for you.

17
00:01:15,000 --> 00:01:21,540
So you can, for example, make the bridge from Arduino to Telegram going through the Raspberry Pi.

18
00:01:22,080 --> 00:01:23,370
Let's get started.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:02,470
Let's start with the Raspberry Pi camera.

2
00:00:02,730 --> 00:00:07,140
And in this lesson, I will show you how to correctly plug it to your Raspberry Pi.

3
00:00:07,470 --> 00:00:10,590
Just before that, a quick parenthesis on the camera.

4
00:00:10,890 --> 00:00:13,860
So you have to have enabled cameras for the Raspberry Pi.

5
00:00:14,280 --> 00:00:20,340
The standard camera, which is mounted on a green board, is a quite well standout and normal camera.

6
00:00:20,610 --> 00:00:24,150
It gives you good images when the light of the room is good enough.

7
00:00:24,810 --> 00:00:29,040
Then you have the Nuar camera, which is mounted on a black board.

8
00:00:29,490 --> 00:00:35,400
This camera works great in low light environments and actually doesn't need light to operate.

9
00:00:35,610 --> 00:00:39,870
So you can use it in a completely dark room or at night, for example.

10
00:00:40,380 --> 00:00:46,440
Note, however, that in daylight, the images will not look as good as the stand out camera.

11
00:00:46,620 --> 00:00:47,380
So what dissection?

12
00:00:47,380 --> 00:00:53,790
And for the final project, I will be using the standard PI camera and I suggest you do the same.

13
00:00:54,240 --> 00:00:58,320
If, however, you only have the black version, well, no problem at all.

14
00:00:58,590 --> 00:01:02,100
You can follow the same instructions in your images.

15
00:01:02,100 --> 00:01:06,230
We just have a slightly different look, which is not a problem for these course.

16
00:01:06,660 --> 00:01:11,490
And now let's see how the way and let's blow the camera to our Raspberry Pi.

17
00:01:12,650 --> 00:01:14,210
So first of all, and that's important.

18
00:01:14,480 --> 00:01:19,680
Make sure you correctly shut down the Raspberry Pi like you shade on a normal computer, OK, so don't

19
00:01:19,820 --> 00:01:21,200
just remove the cable.

20
00:01:21,440 --> 00:01:22,940
Shut it down from the software.

21
00:01:23,270 --> 00:01:24,950
Then you remove the power cable.

22
00:01:25,340 --> 00:01:31,190
And what we're going to do also is to remove the SD card for any manipulation we do on the Raspberry

23
00:01:31,190 --> 00:01:36,890
Pi, so we don't have the risk of breaking as the government was going to put that on the site here

24
00:01:37,160 --> 00:01:38,080
and put it back.

25
00:01:38,130 --> 00:01:42,770
And then I'm also going to disconnect anything from the Raspberry Pi, so.

26
00:01:44,290 --> 00:01:44,620
OK.

27
00:01:44,860 --> 00:01:46,300
We are better.

28
00:01:46,330 --> 00:01:51,350
Ladies, and we are going to take the camera, so I have the camera here.

29
00:01:51,370 --> 00:01:57,700
You can see, well, this is a very simple stuff with the wire here and you can see you have a blue

30
00:01:57,700 --> 00:02:02,140
box and hit the clinic talking metallic connector.

31
00:02:03,640 --> 00:02:07,270
So we're going to use this boat here.

32
00:02:07,400 --> 00:02:07,720
OK.

33
00:02:07,960 --> 00:02:12,940
You have another one that is similar here, but this is for the display screen that is compatible with

34
00:02:12,940 --> 00:02:13,630
Raspberry Pi.

35
00:02:13,840 --> 00:02:19,050
So we're going to use that one here so you can just take out bit.

36
00:02:19,840 --> 00:02:23,410
You can see the black, but this is close.

37
00:02:23,410 --> 00:02:28,490
And if you pull a little bit, this is open.

38
00:02:29,530 --> 00:02:38,020
Now what you do is you take this connector of the camera and the blue path is going to face the USB

39
00:02:38,020 --> 00:02:42,880
port here, OK, and the connector here is going to face this side.

40
00:02:43,570 --> 00:02:44,880
So you plug it here.

41
00:02:46,470 --> 00:02:48,420
And you make sure it goes.

42
00:02:50,030 --> 00:02:51,140
It goes to the end.

43
00:02:52,340 --> 00:02:59,600
It's very important to make sure it's correctly plugged and then you're going to push back the black.

44
00:03:01,870 --> 00:03:03,310
The black plastic pouch.

45
00:03:06,130 --> 00:03:13,480
So that the camera is plugged and you can see now, OK, nothing should go out, OK, it should be exactly

46
00:03:13,600 --> 00:03:14,260
like this.

47
00:03:14,800 --> 00:03:19,330
So now you have the camera, which is correctly plug.

48
00:03:19,480 --> 00:03:22,660
Let's put back as the card.

49
00:03:23,500 --> 00:03:23,950
All right.

50
00:03:24,310 --> 00:03:31,410
And what you can do is you can put the camera like this facing facing the well, if you put the camera

51
00:03:31,430 --> 00:03:36,220
like this is going to face here and is going to take a photo of what's in front of it, of course.

52
00:03:37,030 --> 00:03:45,730
And one thing is that when trying not to take this connector out and put it back too often because as

53
00:03:45,730 --> 00:03:48,100
you can see, that's not like a USB cable news.

54
00:03:48,160 --> 00:03:49,540
B cable is very robust.

55
00:03:49,810 --> 00:03:53,170
It's been tested to be plugged unplugged like thousands of times.

56
00:03:53,560 --> 00:03:56,710
But this one, if you plug it, unplug it.

57
00:03:57,070 --> 00:04:00,760
Many times you may break the connector.

58
00:04:01,060 --> 00:04:04,060
So I really recommend that once it is plugged.

59
00:04:04,420 --> 00:04:09,460
You really don't unplug it unless you have to like trouble with your Raspberry Pi, or unless you have

60
00:04:09,460 --> 00:04:11,380
to move it some way or put it in books.

61
00:04:11,830 --> 00:04:12,160
OK.

62
00:04:12,460 --> 00:04:15,820
So just keep it like this and know everything is good.

63
00:04:16,180 --> 00:04:23,530
You can just pull up on your Raspberry Pi and let's take some photos.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:03,750
The camera is now correctly plugged to the Raspberry Pi board.

2
00:00:04,110 --> 00:00:05,940
Let's now take some photos.

3
00:00:05,970 --> 00:00:07,780
We base them again.

4
00:00:07,800 --> 00:00:12,600
Before that, we just need to enable the camera on the Raspberry Pi operating system.

5
00:00:12,900 --> 00:00:15,240
So, no, the Raspberry Pi has boots.

6
00:00:15,250 --> 00:00:16,530
You are back on the desktop.

7
00:00:16,980 --> 00:00:21,300
I'm going to show you how to enable we've the menu here and also from the terminal.

8
00:00:21,810 --> 00:00:25,350
So you go to preferences here.

9
00:00:26,400 --> 00:00:28,200
Raspberry Pi configuration.

10
00:00:31,020 --> 00:00:35,070
You go on interfaces and you can see camera here.

11
00:00:35,310 --> 00:00:43,860
So if it's disabled, you click on Enable, it's already enabled for me and you click on OK, then if

12
00:00:43,860 --> 00:00:50,910
you want to use the terminal, you can also do pseudo raspy dash config.

13
00:00:51,420 --> 00:00:51,750
OK?

14
00:00:52,110 --> 00:00:56,660
Press, enter and go to interface options.

15
00:00:56,670 --> 00:01:00,750
So that's basically the same menu just from the terminal you click on.

16
00:01:01,240 --> 00:01:05,580
So camera enter, would you like the camera interface to be enabled?

17
00:01:05,820 --> 00:01:06,480
Yes.

18
00:01:07,710 --> 00:01:08,430
Is enabled.

19
00:01:08,670 --> 00:01:09,180
OK.

20
00:01:09,900 --> 00:01:13,470
And then right arrow to go to select and finish.

21
00:01:13,740 --> 00:01:14,550
Press enter.

22
00:01:15,060 --> 00:01:16,500
And the camera is enabled.

23
00:01:16,950 --> 00:01:21,950
So if the camera was previously disabled or if you just want to make sure it's working, just do a pseudo

24
00:01:22,050 --> 00:01:23,170
reboot, right?

25
00:01:23,550 --> 00:01:26,400
Enter and then just wait a few seconds.

26
00:01:26,400 --> 00:01:32,160
So here I'm using VR and think, OK, so I'm just waiting that the Raspberry Pi is going to boot again,

27
00:01:32,430 --> 00:01:36,030
and the Vinci client is going to connect automatically to Rozenberg by.

28
00:01:36,030 --> 00:01:36,330
You get.

29
00:01:39,490 --> 00:01:43,960
OK, now we are sure that the cameras correctly enabled and that we can use.

30
00:01:44,200 --> 00:01:50,290
So let's open funny by so we can write some Python code.

31
00:01:50,680 --> 00:01:53,770
And let's start with this line.

32
00:01:58,530 --> 00:02:04,620
So we give the interpreter and spoken three and then well, there is a module, there is a Python module

33
00:02:04,620 --> 00:02:07,020
that is already installed on a Raspberry Pi, always.

34
00:02:07,500 --> 00:02:11,160
Then you're going to do it from by camera.

35
00:02:11,310 --> 00:02:17,070
So this is the Bhide camera module and you're going to do so from by camera.

36
00:02:17,070 --> 00:02:24,740
All lowercase input by camera like this will be uppercase c a bookie's.

37
00:02:25,140 --> 00:02:33,720
And then what we're going to do is we're going to create a camera, OK, from my camera like this,

38
00:02:33,720 --> 00:02:41,160
we've parentheses and from that camera object here, we will be able to take some photos and we can

39
00:02:41,160 --> 00:02:45,830
add some settings, for example, camera that resolution.

40
00:02:45,870 --> 00:02:47,940
So this is a great input on setting.

41
00:02:48,600 --> 00:02:56,670
And let's give, for example, 1080 by seven 20.

42
00:02:57,220 --> 00:03:00,490
OK, so this is HD photo for the resolution.

43
00:03:00,520 --> 00:03:03,360
Make sure you give a tuple, maybe some parentheses.

44
00:03:03,900 --> 00:03:07,650
And then we need to choose where we want to save the photos, actually.

45
00:03:08,010 --> 00:03:16,350
So in this open file manager here, then when we are in our own directory here, maybe we could create

46
00:03:16,350 --> 00:03:17,610
a camera folder.

47
00:03:17,910 --> 00:03:22,650
So instead of just creating a camera folder here, that's due from the Python.

48
00:03:23,220 --> 00:03:28,710
So we're having to import oase and then let's provide image.

49
00:03:29,730 --> 00:03:36,430
Folder name is equal to slash home slash file.

50
00:03:36,510 --> 00:03:40,410
OK, this is where we are here and then slash camera.

51
00:03:41,520 --> 00:03:46,620
Then we're going to check if this follow doesn't exist, then we are going to create it.

52
00:03:46,620 --> 00:03:48,630
So if not, voice.

53
00:03:50,070 --> 00:03:53,840
That Bath don't exist.

54
00:03:54,170 --> 00:03:57,750
OK, is how to check that something exists.

55
00:03:58,880 --> 00:04:10,010
If it doesn't exist, we do voice notes, m k d i r like in the terminal, we the image folder name.

56
00:04:11,050 --> 00:04:17,000
OK, so if we were that this is going to create a camera folder here the first time and then the second

57
00:04:17,000 --> 00:04:20,060
time is going to skip it because it already exists.

58
00:04:20,690 --> 00:04:27,890
OK, and then let's do it time that slipped to OK.

59
00:04:28,010 --> 00:04:29,240
So why is that?

60
00:04:29,570 --> 00:04:30,380
Let's do first.

61
00:04:30,480 --> 00:04:32,520
Input time because we use Thank you.

62
00:04:33,200 --> 00:04:33,920
So why is that?

63
00:04:34,010 --> 00:04:39,190
Simply because the camera needs a bit of time to adjust to the luminosity.

64
00:04:39,200 --> 00:04:39,500
OK?

65
00:04:39,740 --> 00:04:45,710
So if you want to have a correct picture when you take a picture next, should you wait, at least,

66
00:04:45,860 --> 00:04:47,230
let's say two seconds, OK?

67
00:04:47,570 --> 00:04:53,300
So you create the camera, you set the settings, you created a folder and you wait for two seconds

68
00:04:53,300 --> 00:04:55,640
and then you can take a photo.

69
00:04:56,000 --> 00:04:58,010
So you know not to take your photo.

70
00:04:58,020 --> 00:05:00,560
We need to provide a file name.

71
00:05:00,590 --> 00:05:05,420
OK, so that's the image file name is equal to.

72
00:05:05,600 --> 00:05:11,350
So let's use the image folder name and let's so slash.

73
00:05:11,810 --> 00:05:14,870
Let's name each new image dot.

74
00:05:16,220 --> 00:05:19,760
OK, we are going to use this extension.

75
00:05:20,360 --> 00:05:22,330
And then you can do camera.

76
00:05:22,340 --> 00:05:29,510
So the camera we have created here that capture your image file name.

77
00:05:30,150 --> 00:05:32,690
Let's now run that code.

78
00:05:34,080 --> 00:05:43,030
So we see it as, let's see, test camera, press enter and OK.

79
00:05:43,080 --> 00:05:45,540
You can see now the program has grown.

80
00:05:45,960 --> 00:05:47,550
We have not printed anything.

81
00:05:48,510 --> 00:05:53,880
We could have printed some log here to say that we have actually taken a photo.

82
00:05:54,480 --> 00:06:01,650
And you can see here on this one minute, we have a new folder camera and go on the camera folder and

83
00:06:01,650 --> 00:06:02,580
we have a new image.

84
00:06:03,000 --> 00:06:05,400
And well, that's the current image.

85
00:06:05,400 --> 00:06:06,850
Not actually it's quite dark in here.

86
00:06:06,870 --> 00:06:11,760
I'm going to turn on the light and let's take the photo again.

87
00:06:13,280 --> 00:06:20,840
OK, so let's wait, just two seconds, maybe we can out of print, you print, take a photo.

88
00:06:22,820 --> 00:06:24,860
OK, so we can see.

89
00:06:26,970 --> 00:06:27,270
OK.

90
00:06:27,480 --> 00:06:33,180
But a date for so we know when we have the food that's just going to fall again, so you can see that's

91
00:06:33,180 --> 00:06:40,290
actually when you take a photo with the finding it's going to replace any other photo was taken before

92
00:06:40,290 --> 00:06:41,580
with the same fake name, OK?

93
00:06:42,330 --> 00:06:44,660
And you can see whether that's a photo.

94
00:06:44,670 --> 00:06:49,710
And we have one problem here is that the photo is upside down.

95
00:06:50,220 --> 00:07:01,740
So what I'm going to do is I'm going to add a new sitting here, which is camera not rotation is equal

96
00:07:01,740 --> 00:07:03,720
to 180 degrees.

97
00:07:03,960 --> 00:07:06,860
So this depends actually on the photo you see.

98
00:07:06,870 --> 00:07:11,220
But if you see the photo is upside down, then you can use the setting.

99
00:07:11,430 --> 00:07:16,280
And then if you change the position of the camera, you can just adjust this to make sure that you have

100
00:07:16,290 --> 00:07:17,210
a correct image.

101
00:07:17,220 --> 00:07:19,170
So let's think the photo again.

102
00:07:21,540 --> 00:07:24,720
Take photo and know the photo is correctly.

103
00:07:25,980 --> 00:07:26,700
Orientated.

104
00:07:27,570 --> 00:07:33,660
One thing I'm going to do also now is to test a different resolution because, well, when you take

105
00:07:33,660 --> 00:07:38,370
a photo with a big resolution like this, so this is not the biggest, but it's quite big.

106
00:07:38,760 --> 00:07:43,860
Then let's say here you see the file is 562 kilobytes.

107
00:07:44,040 --> 00:07:46,740
OK, so 500 kilobytes.

108
00:07:47,250 --> 00:07:54,710
Now let's take a photo with six hundred forty and 480.

109
00:07:54,720 --> 00:07:56,310
So this is a lower resolution.

110
00:07:56,670 --> 00:07:59,370
Let's name it, new image to get.

111
00:07:59,400 --> 00:08:00,990
So we're going to have the image on the side.

112
00:08:01,650 --> 00:08:03,630
Let's run again the same photo.

113
00:08:05,650 --> 00:08:08,920
OK, and let's check this image OK.

114
00:08:09,310 --> 00:08:14,950
The resolution is smaller, as you can see, but we still see clearly, and now the photo is just 200

115
00:08:14,950 --> 00:08:15,460
kilobytes.

116
00:08:15,520 --> 00:08:20,440
So we have 500 and we went from 500 to 200 kilobyte.

117
00:08:20,740 --> 00:08:22,490
And this is quite important.

118
00:08:22,510 --> 00:08:22,900
OK.

119
00:08:23,200 --> 00:08:29,710
Because then when we take a photo and we send photos to the internet, it's better actually to try to

120
00:08:29,710 --> 00:08:30,850
have size that.

121
00:08:30,850 --> 00:08:31,900
It's quite small.

122
00:08:32,230 --> 00:08:35,080
So it goes faster and it doesn't take too much space.

123
00:08:35,470 --> 00:08:35,800
All right.

124
00:08:35,800 --> 00:08:38,620
And that's pretty much it from now for the camera.

125
00:08:38,890 --> 00:08:44,710
We are going to come back to it in the following practice activities and also in the final product of

126
00:08:44,710 --> 00:08:45,170
the games.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:03,180
OK, you can now take photos using the Raspberry Pi.

2
00:00:03,210 --> 00:00:06,240
Come on, let's know, switch to Telegram bots.

3
00:00:06,480 --> 00:00:07,650
So why are you getting wrong?

4
00:00:08,040 --> 00:00:15,330
Well, Telegram is a quite good and open messaging app with the possibility of creating useful bots

5
00:00:15,900 --> 00:00:22,920
about basically is a program that will interact with the chat on the Telegram application and debate

6
00:00:22,920 --> 00:00:27,900
with me or anywhere with your running in the Raspberry Pi as a Python program.

7
00:00:28,320 --> 00:00:34,860
For example, you can send a message to a chat from the Raspberry Pi, and you can also respond to some

8
00:00:34,860 --> 00:00:37,380
commands that you type directly on the chat.

9
00:00:37,590 --> 00:00:43,680
We are going to see both cases in the following listeners, but first, we need to do a few configuration

10
00:00:43,680 --> 00:00:47,370
steps to create these bot on the telegram up.

11
00:00:48,060 --> 00:00:52,380
The very first step is to create a Telegram account from your phone.

12
00:00:52,830 --> 00:00:54,030
Telegram is three.

13
00:00:54,300 --> 00:00:55,980
So no problem with that.

14
00:00:56,490 --> 00:01:06,620
So you go to the Telegram website here with Telegram dot org and you download one of the application,

15
00:01:06,630 --> 00:01:07,020
OK?

16
00:01:07,380 --> 00:01:14,850
So if you have like an Android phone, a iPhone or a Windows Phone, for example, so you download the

17
00:01:14,850 --> 00:01:17,250
application and you just follow the set.

18
00:01:17,550 --> 00:01:22,860
OK, so Telegram, you need to link your account to your phone number.

19
00:01:23,130 --> 00:01:23,380
OK.

20
00:01:23,400 --> 00:01:26,520
That's why you need to start the account from your phone.

21
00:01:26,970 --> 00:01:30,870
Then you are free to use any of the phone, tablet or desktop application.

22
00:01:31,080 --> 00:01:32,970
So I'm not going to show you the setup.

23
00:01:32,970 --> 00:01:37,410
You just basically will you just download an application and you just click on next.

24
00:01:37,800 --> 00:01:45,330
Until you get to the chat and then wait, you can use the application from anywhere if you want to use

25
00:01:45,330 --> 00:01:46,770
your application from your phone.

26
00:01:47,010 --> 00:01:49,880
You can do that if you want to use the application.

27
00:01:49,890 --> 00:01:51,900
Also, you can download it for windows.

28
00:01:52,170 --> 00:01:53,920
You can download it for macOS.

29
00:01:53,940 --> 00:01:55,410
You can download it for Linux.

30
00:01:55,620 --> 00:02:01,020
And that's what actually I'm going to do here is I'm going to use the application, so I have the application

31
00:02:01,020 --> 00:02:08,520
on my phone as well, but I'm going to use the application, the desktop application also from the Raspberry

32
00:02:08,520 --> 00:02:09,870
Pi desktop.

33
00:02:10,170 --> 00:02:16,110
Just so it is simpler for me to record the video basically so I can have the Python program out in the

34
00:02:16,110 --> 00:02:18,960
program and I can also have the Telegram application.

35
00:02:19,170 --> 00:02:22,280
OK, but you don't need to use the Telegraph application here.

36
00:02:22,290 --> 00:02:24,570
You just use it anywhere you want.

37
00:02:24,840 --> 00:02:30,900
And so if you want to use the Telegram app from Windows on Mac OS, you just downloaded from the website.

38
00:02:31,320 --> 00:02:37,530
And if you want to use it from Linux, well, you can just do sudo aptitude.

39
00:02:37,860 --> 00:02:43,740
Install Telegram Desktop with auto completion.

40
00:02:44,370 --> 00:02:49,620
OK, and what from it's already installed on any Linux?

41
00:02:50,160 --> 00:02:59,490
You just do this and then you will see that if you go to the menu and internet, you have the web browser

42
00:02:59,490 --> 00:03:01,770
and you have Telegram desktop.

43
00:03:04,960 --> 00:03:12,010
OK, and now you have to drum up, so this will look exactly the same on mobile, on the desktop application,

44
00:03:12,020 --> 00:03:12,670
so that's great.

45
00:03:12,910 --> 00:03:15,970
Basically, you have a list of jobs, you can have to contact everything.

46
00:03:15,970 --> 00:03:22,270
So I'm not going to explain to you how messaging app works and not well, your account is correctly

47
00:03:22,450 --> 00:03:23,080
configured.

48
00:03:23,590 --> 00:03:25,210
We can create a bot.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:06,450
Now that your account is correctly set up and configured, let's create a bot on the Telegram up.

2
00:00:06,810 --> 00:00:11,850
We first need to do that and then we be able to use this box in a Python program.

3
00:00:12,180 --> 00:00:16,110
So you're going to so cheerful, but father ladies.

4
00:00:17,400 --> 00:00:22,920
So you type exactly like this and you're going to go with the first one, the certified one, because

5
00:00:22,920 --> 00:00:29,700
you can see you have many, well, fake but father with slightly different usani, but you just go with

6
00:00:29,700 --> 00:00:29,910
the.

7
00:00:30,660 --> 00:00:31,140
Father.

8
00:00:32,340 --> 00:00:33,560
And then what?

9
00:00:33,560 --> 00:00:39,690
Father is basically going to allow you to create new books so you click on Start.

10
00:00:40,170 --> 00:00:41,520
You just send slush.

11
00:00:41,970 --> 00:00:46,710
You can see slashed start if you don't have a start button and you have help here.

12
00:00:47,070 --> 00:00:52,860
I can help you to create and manage turning around boats, etc., etc. And so you can create both.

13
00:00:52,870 --> 00:00:58,340
You can edit boats, you have settings, etc. You're going to do new books.

14
00:00:58,590 --> 00:01:00,240
OK, so slash new books.

15
00:01:00,240 --> 00:01:02,780
You can either click on this address, right?

16
00:01:03,300 --> 00:01:03,690
New.

17
00:01:03,960 --> 00:01:04,380
But.

18
00:01:05,920 --> 00:01:14,890
All right, animals, so you choose a name for the but let's name it, of course, but that's just the

19
00:01:14,890 --> 00:01:18,550
name we're going to see and then we need to choose a username.

20
00:01:19,330 --> 00:01:20,980
It needs to end in.

21
00:01:21,430 --> 00:01:26,920
But as you can see, so let's try RPI Arduino course.

22
00:01:27,910 --> 00:01:28,360
But.

23
00:01:30,330 --> 00:01:38,340
OK, so if it turns you that name is already taken, then you try another name, OK, until you have

24
00:01:38,340 --> 00:01:39,810
a name that is unique.

25
00:01:39,810 --> 00:01:43,440
So this name doesn't have to be unique, but this name will be unique.

26
00:01:43,440 --> 00:01:47,790
So if you try, of course, to have the same as me, well, that's not going to work.

27
00:01:47,880 --> 00:01:51,030
And then you see Don, congratulations, et cetera, et cetera.

28
00:01:51,240 --> 00:01:55,710
And you have a token that is the most important thing.

29
00:01:56,160 --> 00:01:56,490
OK?

30
00:01:56,700 --> 00:02:00,090
And you can see keep your token secure and steroids safely.

31
00:02:00,360 --> 00:02:01,980
These should be secret.

32
00:02:02,490 --> 00:02:08,640
So why I'm showing you this now is simply because, well, I'm going to use this token when I record

33
00:02:08,640 --> 00:02:10,680
the videos and then I'm going to change it.

34
00:02:10,920 --> 00:02:14,940
So if you try to use this exact token, you're not going to be able to use my book.

35
00:02:15,210 --> 00:02:15,510
OK?

36
00:02:16,080 --> 00:02:20,970
The token basically will allow you to connect to the Bolt from your Python program.

37
00:02:21,420 --> 00:02:22,620
So what about your other name?

38
00:02:22,980 --> 00:02:26,310
You have a username that is unique and a token.

39
00:02:26,970 --> 00:02:30,750
Now let's do that, for example, again, to get the help.

40
00:02:31,500 --> 00:02:38,130
You can see, for example, what they can do is revoked boat token access for that boat.

41
00:02:38,910 --> 00:02:43,020
You can see your token was replaced with a new one and then you have this.

42
00:02:43,260 --> 00:02:47,790
OK, so this token here is not valid anymore.

43
00:02:48,480 --> 00:02:49,380
This is the new one.

44
00:02:49,710 --> 00:02:53,880
And so basically, I'm going to revoke my token after a second eclipse.

45
00:02:54,510 --> 00:02:55,580
OK, so we have a token.

46
00:02:55,590 --> 00:03:02,070
We're going to come back to this token just a bit later and know what we are going to do wending to

47
00:03:02,070 --> 00:03:03,510
create a group chat.

48
00:03:03,660 --> 00:03:08,190
OK, and we are going to use for sending notifications.

49
00:03:08,490 --> 00:03:10,950
So you click here.

50
00:03:11,640 --> 00:03:12,300
New Group.

51
00:03:14,240 --> 00:03:19,520
Let's name these group, of course, group, so you name it as you want.

52
00:03:20,640 --> 00:03:22,340
You can add numbers.

53
00:03:22,700 --> 00:03:26,300
Let's search for RPI, Arduino.

54
00:03:27,720 --> 00:03:31,980
Of course, but so I find the box and I create the group.

55
00:03:32,890 --> 00:03:36,300
OK, so you can see in the group view group info.

56
00:03:37,450 --> 00:03:42,880
We have two numbers, so me and the but we have just created OK.

57
00:03:43,150 --> 00:03:46,300
And so you can add other persons if you want.

58
00:03:47,980 --> 00:03:52,450
And we are going to communicate with the board through this group here.

59
00:03:53,620 --> 00:03:56,170
So the Telegram configuration is done for the boat.

60
00:03:56,500 --> 00:04:05,170
Now let's go back to what, father, if you don't have it, he just searched for it and let's copy the

61
00:04:06,100 --> 00:04:06,550
token.

62
00:04:07,240 --> 00:04:11,590
Now what I'm going to do is I'm going to show you how basically to stop the token somewhere on your

63
00:04:11,590 --> 00:04:15,640
Raspberry Pi and just get it on your Python code.

64
00:04:15,940 --> 00:04:19,300
And then in the next, listen, we're going to control the bot with Python.

65
00:04:19,600 --> 00:04:23,040
So just a bit more of configuration, and that's it.

66
00:04:23,050 --> 00:04:25,150
So let's open a terminal, actually.

67
00:04:26,840 --> 00:04:32,960
And what I'm going to do this is basically we are in Hungary, Greece, we have this.

68
00:04:33,260 --> 00:04:36,320
But if I do arrest, does a tourist all?

69
00:04:36,560 --> 00:04:37,940
I have also the in.

70
00:04:38,870 --> 00:04:39,140
OK.

71
00:04:39,800 --> 00:04:45,100
And there is one hidden directory here local, not local.

72
00:04:45,120 --> 00:04:47,330
We're going to go in to.

73
00:04:48,730 --> 00:04:50,280
Of local officials.

74
00:04:50,780 --> 00:04:54,440
And it's a wedding to go in.

75
00:04:54,720 --> 00:04:55,190
Share.

76
00:04:56,620 --> 00:05:02,290
OK, and I'm going to create a new fight here and put the token inside.

77
00:05:02,470 --> 00:05:08,350
So here we won't be able to make you 100 percent secure file for the token, but basically by hiding

78
00:05:08,350 --> 00:05:11,050
the fly somewhere that is a bit hard to find.

79
00:05:11,650 --> 00:05:17,320
This is a bit more secure than just putting, for example, the token on the desktop, putting in the

80
00:05:17,560 --> 00:05:21,640
directory directly hardcoded the token in the code.

81
00:05:21,910 --> 00:05:23,520
So I am going to create here.

82
00:05:23,530 --> 00:05:29,950
So no, no, let's name that we we're going to create the hidden file as well.

83
00:05:30,580 --> 00:05:31,240
Telegram.

84
00:05:32,650 --> 00:05:38,920
But token press enter and I'm going to paste the token.

85
00:05:38,920 --> 00:05:45,310
We've control shift and we could see the token that I got from here.

86
00:05:46,420 --> 00:05:51,420
And I'm going to save it with control s and Control X to quit it.

87
00:05:51,640 --> 00:06:00,130
Now you can see if I do less well, nothing if they I can see I have my teddy run, but look at me.

88
00:06:00,910 --> 00:06:04,250
So once again, this is not 100 percent secure solution.

89
00:06:04,780 --> 00:06:09,850
If you want something completely secure, you would need to use, for example, the oath to protocol,

90
00:06:09,850 --> 00:06:13,910
but that's something really more complex and outside of the scope of discourse.

91
00:06:14,530 --> 00:06:19,630
So now that we have our token saved here, let's open.

92
00:06:24,150 --> 00:06:25,050
By some 80.

93
00:06:27,140 --> 00:06:28,250
And let's create a new.

94
00:06:29,570 --> 00:06:30,020
I.

95
00:06:31,490 --> 00:06:34,700
A bin and Python three.

96
00:06:38,490 --> 00:06:41,870
And let's just try to go to get the token.

97
00:06:42,360 --> 00:06:44,610
So what we need to do, we just need to open the fight.

98
00:06:44,610 --> 00:06:48,000
We have just created and saved the took inside of violence.

99
00:06:48,030 --> 00:07:02,400
So we've open and then so slash home slash by slush, not local slush -- and slush that telegram.

100
00:07:03,360 --> 00:07:03,750
But.

101
00:07:05,520 --> 00:07:05,820
OK.

102
00:07:06,390 --> 00:07:09,090
OK, so make sure you have the correct path here.

103
00:07:09,630 --> 00:07:18,120
The file we've redemption, we don't need to write as if, OK, so we're going to open this file and

104
00:07:18,120 --> 00:07:22,470
get it as if it is book of code and we do Telegram.

105
00:07:25,030 --> 00:07:37,810
Token is equal to, if not, read that this trick and no, well, this is important is that you don't

106
00:07:37,810 --> 00:07:39,910
print the trigger on torture.

107
00:07:40,210 --> 00:07:46,540
Basically, if you design a more secure application and then you just print the token, you got in the

108
00:07:46,540 --> 00:07:50,050
code where all the security you are going is just useless.

109
00:07:50,500 --> 00:07:52,330
So I'm still going to print.

110
00:07:52,330 --> 00:07:55,330
It just wants to make sure that it's working

111
00:07:58,270 --> 00:07:58,610
OK.

112
00:07:58,870 --> 00:08:05,110
I use our book because maybe at the end of the fight, we have some new line character, some carriage

113
00:08:05,110 --> 00:08:06,190
rides and that we don't want.

114
00:08:06,190 --> 00:08:11,320
So we make sure that they are gone because if we have, for example, a new run character, then that's

115
00:08:11,320 --> 00:08:13,100
not going to work after.

116
00:08:13,120 --> 00:08:14,620
So let's just run this.

117
00:08:16,360 --> 00:08:17,530
That's name Telegram.

118
00:08:18,790 --> 00:08:19,180
But.

119
00:08:20,940 --> 00:08:27,300
OK, we have the token, and now I'm going to do this in a room with the print and we are not going

120
00:08:27,300 --> 00:08:30,570
to print the token anymore now that we know it's working.

121
00:08:31,050 --> 00:08:32,670
And let's not use this book.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,210 --> 00:00:07,710
So, you know, half of account, your account is correctly configured and you have created a bot with

2
00:00:07,710 --> 00:00:08,730
the father.

3
00:00:09,030 --> 00:00:10,910
You also have a group here.

4
00:00:10,920 --> 00:00:14,370
We've at least you and the bot.

5
00:00:15,090 --> 00:00:21,750
Now in this lesson, we're going to write some Python code so that the bots can respond to some commands.

6
00:00:21,750 --> 00:00:28,890
So for example, if I do slush stocks here, so nothing happens, but we are going to respond to that

7
00:00:28,890 --> 00:00:30,750
command from the Raspberry Pi.

8
00:00:31,230 --> 00:00:37,200
So what you're going to see when you send Slashdot from the Tehran application that can be from the

9
00:00:37,200 --> 00:00:41,310
desktop, from your phone or from anywhere, you're going to get the response here.

10
00:00:41,890 --> 00:00:42,820
OK, let's do that.

11
00:00:42,840 --> 00:00:45,750
So we already have the token, OK?

12
00:00:45,750 --> 00:00:50,940
In the previous listen, we have gotten the token here from the bot father.

13
00:00:51,120 --> 00:00:58,980
We have stalled the token inside of file and now we get the token inside our Python quorum now to be

14
00:00:58,980 --> 00:01:00,930
able to write on quorum for the.

15
00:01:00,930 --> 00:01:08,850
But we will install a Python module and this Python module is named Python today around booked.

16
00:01:09,300 --> 00:01:13,530
So first of all, make sure you have IP three, so you do pretty.

17
00:01:15,050 --> 00:01:18,370
Installed base, some three Dash B, I B.

18
00:01:20,130 --> 00:01:20,400
OK.

19
00:01:20,770 --> 00:01:23,070
For me, it's already done, and then I'd be three.

20
00:01:25,530 --> 00:01:30,260
Installed Base One Dush Telegram.

21
00:01:31,500 --> 00:01:36,150
But and then you can also add Dash Dash agreed.

22
00:01:39,770 --> 00:01:49,280
OK, and for me, that was actually already in stock know that you have the Python Telegram bot module.

23
00:01:49,760 --> 00:01:51,230
Let's use it in the code.

24
00:01:52,010 --> 00:02:01,610
So you're going to do from Telegram that you import that data and command.

25
00:02:02,090 --> 00:02:06,950
And look, I'm just going to explain to you what this is and what it does.

26
00:02:07,880 --> 00:02:10,350
So we have the token here.

27
00:02:10,370 --> 00:02:17,930
I'm going to first create a lot of data from data is equal to other data and you need to give the tokens

28
00:02:18,080 --> 00:02:20,690
token is equal to.

29
00:02:21,760 --> 00:02:28,420
Telegram took it, so the Telegram token you have read from the file.

30
00:02:28,960 --> 00:02:37,030
So basically of data with below this per I'm here to wellbeing, keep updated of what's happening in

31
00:02:37,030 --> 00:02:43,030
the Telegram application when you send some message to the bot and then on top of the data we are going

32
00:02:43,030 --> 00:02:52,120
to add, a dispatcher is a quota of data that dispatcher.

33
00:02:53,440 --> 00:02:58,300
So data will keep track of what's happening in the application.

34
00:02:58,630 --> 00:03:06,580
The dispatcher basically will take the that you send, for example, start and will dispatch them to

35
00:03:06,700 --> 00:03:10,820
the correct callback function that we are going to right now.

36
00:03:10,900 --> 00:03:11,260
OK.

37
00:03:11,920 --> 00:03:15,850
So for each world that you want the bot to respond to?

38
00:03:16,150 --> 00:03:27,970
You can add a comment handler so we can do dispatcher dot, add handler and then use the command handler

39
00:03:28,870 --> 00:03:30,550
command handler.

40
00:03:31,780 --> 00:03:33,700
We first DOUKI world.

41
00:03:34,390 --> 00:03:36,820
So the key word will be start, for example.

42
00:03:37,690 --> 00:03:41,560
This is a common keyword that we will use for everybody to start with.

43
00:03:42,010 --> 00:03:44,830
And then, let's say, starts handler.

44
00:03:45,190 --> 00:03:47,740
OK, this is a function we will need to create.

45
00:03:48,280 --> 00:03:50,170
I close the two current is issue.

46
00:03:50,830 --> 00:03:55,120
So when the code here, there is very nothing to understand.

47
00:03:55,120 --> 00:04:01,210
This is just light as you create of data and a dispatcher and you add for each key what you want.

48
00:04:01,690 --> 00:04:05,870
You add a command handler with add handler and that's going to be the same every time.

49
00:04:05,890 --> 00:04:06,160
OK.

50
00:04:06,730 --> 00:04:11,710
And now that we have this well, we need to create our so that's created you.

51
00:04:12,550 --> 00:04:16,840
We need to create def stat handler.

52
00:04:17,820 --> 00:04:26,100
So we need to create the callback function that will be called when we send this document on the application.

53
00:04:26,820 --> 00:04:34,050
And you are going to receive two parameters which are out of date and context.

54
00:04:36,120 --> 00:04:44,400
And when I hear what you can do is you can process the requests and you can also actually respond to

55
00:04:44,850 --> 00:04:48,480
the request, so he had to respond to the request where you need to do context.

56
00:04:51,040 --> 00:05:02,320
Not, but can you get the book from the context parameter that send a message you need to give to argument

57
00:05:02,590 --> 00:05:05,570
chat, I.D. and text?

58
00:05:05,590 --> 00:05:10,030
So for a check, you're going to check a is equal to update.

59
00:05:10,960 --> 00:05:12,700
That's effective.

60
00:05:14,780 --> 00:05:24,170
Chucked that idea, and for the next YouTube fixed equal to engines, the text you want to let's say

61
00:05:24,560 --> 00:05:28,100
hello from Python.

62
00:05:30,190 --> 00:05:34,890
OK, now to know you need to do that, well, that's basically what they say in the documentation,

63
00:05:34,900 --> 00:05:37,930
OK, there is not really any logic here.

64
00:05:38,290 --> 00:05:40,030
This is just how to use the books.

65
00:05:40,570 --> 00:05:47,140
So context, but the same message with the chat idea, which is basically the chat idea we got.

66
00:05:48,510 --> 00:05:55,980
Q So Avery chats to this group chat here has an idea, and this is the idea we get, so we send the

67
00:05:55,980 --> 00:06:01,530
message to this chat lady with this text, OK, know that we have the handler.

68
00:06:01,830 --> 00:06:10,260
We need to do a data that starts falling, OK, so it will start being updated.

69
00:06:10,560 --> 00:06:12,570
And then what if we just leave it like this?

70
00:06:12,570 --> 00:06:17,940
The program is going to end, so I'm going to start with the data that I do.

71
00:06:18,840 --> 00:06:26,610
OK, ladies, this is going to make the program blush here and continue to start pulling from the book

72
00:06:26,790 --> 00:06:30,480
so that when we receive a command, it goes to the dispatcher.

73
00:06:30,840 --> 00:06:36,660
And then we have, for example, the Dutch key word which is going to call the start handler callback

74
00:06:36,660 --> 00:06:37,380
function here.

75
00:06:37,680 --> 00:06:39,510
So let's run that.

76
00:06:40,290 --> 00:06:41,280
Let's run the script.

77
00:06:42,210 --> 00:06:46,080
Actually, maybe we can just add, let's say here the print.

78
00:06:48,620 --> 00:06:51,500
KG but ready.

79
00:06:53,110 --> 00:06:56,790
Ladies, so we have an output, so let's run that with the print.

80
00:06:58,850 --> 00:07:04,730
OK, we can see Telegram, but ready and no, you can see the pyramid stick, so it's waiting for comments

81
00:07:04,730 --> 00:07:06,700
that you sent under Chad.

82
00:07:06,980 --> 00:07:13,730
So then you go on the the weather, on the desktop, into mobile and you do slush that.

83
00:07:15,490 --> 00:07:18,910
And you can see we received help from Python.

84
00:07:19,300 --> 00:07:23,500
So this is currently working, and you can do that as many times as you want.

85
00:07:24,010 --> 00:07:24,480
Stop.

86
00:07:25,330 --> 00:07:25,590
OK.

87
00:07:25,630 --> 00:07:26,590
Hello from Python.

88
00:07:26,800 --> 00:07:31,030
If you sent anything else, anything else, for example?

89
00:07:31,630 --> 00:07:36,790
Well, you have nothing because you don't have a command handler.

90
00:07:37,330 --> 00:07:42,790
And so here we start with the Scott Key one, which is usually what you're going to do with a box,

91
00:07:43,450 --> 00:07:48,190
but then you can basically duplicate this line for every key one that you want.

92
00:07:48,790 --> 00:07:54,340
So you add the key world and then you create a callback for this key.

93
00:07:55,330 --> 00:07:59,410
And usually what I do is I just put the key word with Handler.

94
00:07:59,410 --> 00:08:01,690
OK, so that is pretty explicit.

95
00:08:02,050 --> 00:08:04,240
And no, when when you run this.

96
00:08:05,790 --> 00:08:10,980
If you want to stop the program, can you just do control see and you wait a bit?

97
00:08:12,360 --> 00:08:16,290
You wait a few seconds and you can see now the program has exited.

98
00:08:18,120 --> 00:08:18,520
All right.

99
00:08:18,550 --> 00:08:24,750
And one last thing is, if you want to get more documentation, you're just a Python dig, but on Google

100
00:08:24,750 --> 00:08:29,490
or any search engine and you're going to find the documentation here.

101
00:08:31,020 --> 00:08:35,850
So you have the page, that's the page, and you're going to find the introduction, the condition,

102
00:08:37,140 --> 00:08:39,420
the API, every comment that you can use.

103
00:08:40,380 --> 00:08:45,750
OK, so in this course, I'm going to keep things quite simple so we can reach the final project quite

104
00:08:45,750 --> 00:08:48,330
quickly with the minimum functionalities we need.

105
00:08:48,330 --> 00:08:51,840
And then you can refer to the documentation for more complex behaviors.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,210
So you have seen how to respond to some comments that you sent from the Telegram chat with the boat,

2
00:00:06,720 --> 00:00:11,130
but not what if you just want to send a message to the group, for example?

3
00:00:11,880 --> 00:00:15,480
Because here we can send a message to the group when we have a callback function.

4
00:00:15,490 --> 00:00:20,790
So basically when we first receive a message from the group, so you need to send something from the

5
00:00:20,790 --> 00:00:24,450
group, get that in the Python program and send a message back.

6
00:00:24,810 --> 00:00:31,140
Now what if you just want to send a message without waiting for any input from the application?

7
00:00:31,380 --> 00:00:32,850
Well, that's what I'm going to show.

8
00:00:32,850 --> 00:00:35,490
You know, I'm going to create a new program.

9
00:00:37,380 --> 00:00:40,950
You just think what we need from here.

10
00:00:41,400 --> 00:00:42,990
So the interpreter?

11
00:00:44,710 --> 00:00:46,960
We are going to need also this.

12
00:00:48,450 --> 00:00:50,010
To get the token.

13
00:00:52,340 --> 00:00:52,700
OK.

14
00:00:53,120 --> 00:01:01,010
And no, when we are not going to need data on the comment handler, we are going to simply do from

15
00:01:01,430 --> 00:01:03,180
Telegram import.

16
00:01:04,170 --> 00:01:13,130
But we are going to create a but these is equal to but we can is equal to.

17
00:01:13,580 --> 00:01:23,720
Telegram took it and then from that boat, we can just do but not send a message.

18
00:01:24,740 --> 00:01:28,130
And Hugh, like we did before, we need to.

19
00:01:28,340 --> 00:01:30,260
So that's the same function here.

20
00:01:30,830 --> 00:01:36,650
We need to give the chat, ID and text chats equal to.

21
00:01:37,130 --> 00:01:39,740
Well, what is the idea of this group?

22
00:01:40,190 --> 00:01:41,000
How do we know that?

23
00:01:41,600 --> 00:01:48,860
So you could go on the internet and there are some methods to find a chat ID for this specific chat.

24
00:01:49,250 --> 00:01:55,610
But now that we have already a program that can receive command from the chat, what we can do is just

25
00:01:55,610 --> 00:02:00,740
use this prompt to get the chat and then use the chat and in this other person.

26
00:02:01,430 --> 00:02:03,320
OK, let me show you how to do that.

27
00:02:03,800 --> 00:02:10,460
So in the start handler, that's a good place because we receive some context and some of these from

28
00:02:11,000 --> 00:02:11,570
the chat.

29
00:02:12,260 --> 00:02:18,440
And as you can see, we respond by using a date that effective chat dot Amy.

30
00:02:18,450 --> 00:02:24,440
So basically effective chat is the chat you are using here to send this document here.

31
00:02:24,830 --> 00:02:26,750
And then the idea is the idea of this.

32
00:02:27,050 --> 00:02:29,390
So I'm just going to select this.

33
00:02:30,140 --> 00:02:31,960
I'm going to do here.

34
00:02:32,510 --> 00:02:36,340
Print update that effective chat that.

35
00:02:37,580 --> 00:02:38,690
I'm going to run that.

36
00:02:41,290 --> 00:02:42,460
Telegram about ready.

37
00:02:42,820 --> 00:02:44,680
And I think that.

38
00:02:46,750 --> 00:02:51,620
OK, you can see hello from Python, and we also have here the chat idea.

39
00:02:53,040 --> 00:02:57,940
So a group, usually you would have something that starts with the Dash.

40
00:02:57,960 --> 00:03:04,570
OK, so minus sign with the chat ID so you can just copy this.

41
00:03:05,940 --> 00:03:07,860
And then go in the other program.

42
00:03:08,670 --> 00:03:16,920
Let's create a viable, he said it is equal to this, so we keep it here.

43
00:03:17,640 --> 00:03:20,280
Actually, we don't just keep it as an integer.

44
00:03:20,280 --> 00:03:23,580
This is a string, OK, so we make sure this is a string.

45
00:03:24,270 --> 00:03:26,400
And then today is equal to check it.

46
00:03:27,210 --> 00:03:28,400
It's a no problem with this.

47
00:03:28,410 --> 00:03:30,660
This is the name of the parameter.

48
00:03:30,660 --> 00:03:32,970
And this is the argument that we give.

49
00:03:33,840 --> 00:03:40,170
So we give digitally and then the text is equal to let's use something different.

50
00:03:40,500 --> 00:03:46,210
Let's send from French Bovril, and let's just add a print here.

51
00:03:46,230 --> 00:03:46,680
OK.

52
00:03:46,830 --> 00:03:49,540
So we can know from the Python program that we have sent something.

53
00:03:49,540 --> 00:03:52,380
So send a message to Chuck.

54
00:03:54,330 --> 00:03:56,880
Let's run this, and let's look at the chart here.

55
00:03:57,780 --> 00:04:00,120
Run script, let's name it.

56
00:04:00,570 --> 00:04:02,220
Send a notification.

57
00:04:05,940 --> 00:04:11,880
OK, send message to Chet and you can see Bozo, and we also have the notification here for the desktop

58
00:04:11,880 --> 00:04:12,450
application.

59
00:04:12,900 --> 00:04:17,300
If you are using your phone, you should also receive a notification.

60
00:04:17,310 --> 00:04:20,940
I just received a notification on my phone for this chat.

61
00:04:21,450 --> 00:04:27,030
OK, if you don't have the notification on your phone, make sure you have correctly followed notification

62
00:04:27,030 --> 00:04:27,750
for Telegram.

63
00:04:28,050 --> 00:04:30,000
But this is specific to your phone.

64
00:04:30,370 --> 00:04:38,220
OK, now you can see we can both respond to comment that we send from the chat, and we can also send

65
00:04:38,580 --> 00:04:44,040
independent messages directly to the chat from a baseline program.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:00,810
OK, great.

2
00:00:00,840 --> 00:00:05,610
You can send notification from the Python program to the chat.

3
00:00:06,240 --> 00:00:11,130
And you can also add some callbacks so you can respond to some commands.

4
00:00:11,460 --> 00:00:14,010
But no, let's mix those two.

5
00:00:14,310 --> 00:00:21,780
OK, so we can have a program that sends independent notifications and that also responds to comments

6
00:00:21,780 --> 00:00:22,140
here.

7
00:00:22,530 --> 00:00:26,490
So I'm going to show you the program, Churchill, we're going to use, and this is also some theme

8
00:00:26,490 --> 00:00:29,700
we're going to use for the next activities and for the final project.

9
00:00:30,240 --> 00:00:33,410
So I'm going to start, I'm going to start from scratch.

10
00:00:33,420 --> 00:00:40,230
I'm going to start from this Telegram bots program here, which is already working, and I'm going to

11
00:00:40,230 --> 00:00:43,860
add simply this into that program.

12
00:00:44,400 --> 00:00:48,750
And so what we do here is we create some handler, OK?

13
00:00:48,780 --> 00:00:54,740
We have data that going to keep an eye on the chat, a dispatcher that is going to dispatch any comment

14
00:00:54,750 --> 00:00:56,220
or receive to its handler.

15
00:00:56,610 --> 00:01:01,290
We start pulling and then we use idle to stop the program here.

16
00:01:02,340 --> 00:01:06,900
Well, I'm going to do is I'm going to remove this idle and we are going to use instead.

17
00:01:07,360 --> 00:01:09,270
But while loop?

18
00:01:09,360 --> 00:01:13,420
OK, so basically we are going to use an infinite loop just like we did before.

19
00:01:13,470 --> 00:01:15,750
This is kind of the void setup.

20
00:01:16,050 --> 00:01:20,250
And then we're going to create a void loop like we have on the Arduino.

21
00:01:20,610 --> 00:01:25,920
And I'm going to do white through it.

22
00:01:25,950 --> 00:01:30,450
And this is where we are going to do our program.

23
00:01:30,810 --> 00:01:33,330
And, for example, send some notifications.

24
00:01:33,330 --> 00:01:40,050
So if we want to send some notification, I'm going to do this from tree input, but I'm going to put

25
00:01:40,050 --> 00:01:45,210
it there and I'm also going to create a bunch.

26
00:01:46,810 --> 00:01:51,400
So we already have the token so agreed to.

27
00:01:51,430 --> 00:01:59,350
But here just before that of data, for example, so we have the boat and a data, and for each we give

28
00:01:59,350 --> 00:02:00,400
the trailer and took it.

29
00:02:00,880 --> 00:02:01,130
OK.

30
00:02:01,150 --> 00:02:03,750
I'm also going to do this chart.

31
00:02:04,360 --> 00:02:04,750
OK.

32
00:02:05,830 --> 00:02:09,910
And to put it there, so we can use the chat ID with the book.

33
00:02:10,720 --> 00:02:17,110
We could use this strategy actually here so that anytime you send come into the.

34
00:02:17,110 --> 00:02:21,090
But we cannot respond to this group, but I'm going to keep it like this.

35
00:02:21,100 --> 00:02:27,520
So basically, this means that if you have another group, if you just send a message directly from

36
00:02:27,520 --> 00:02:35,260
your user to the boat, well, by using a date that effective chat the 80, you're going to respond

37
00:02:35,260 --> 00:02:37,630
to whoever is sending the message.

38
00:02:38,050 --> 00:02:43,240
Whoever is sending stuff OK, so from this group or from another group or from you, use it.

39
00:02:43,720 --> 00:02:48,910
If you use this chat tragedy, when every time you receive something, you're just going to send back

40
00:02:48,910 --> 00:02:50,230
a message, but to this group.

41
00:02:50,470 --> 00:02:56,020
So if you send a command from another group, you are still going to reply to this group instead.

42
00:02:56,190 --> 00:02:57,370
OK, so we're going to keep this.

43
00:02:57,910 --> 00:03:02,170
So we directly respond to the one who sends the command.

44
00:03:02,980 --> 00:03:07,140
I'm going to remove this printed and then with it, we still have this strategy.

45
00:03:07,160 --> 00:03:11,680
So when we send a notification, however, that's always going to be in this group.

46
00:03:12,130 --> 00:03:18,070
And so no, let's say we want to send a notification every 10 seconds, for example.

47
00:03:18,550 --> 00:03:23,670
What we can do is do, but don't send message.

48
00:03:24,370 --> 00:03:29,920
We've chat 80 is equal to check I.D. and text.

49
00:03:31,870 --> 00:03:33,520
That's pretty high.

50
00:03:35,440 --> 00:03:37,120
Something you.

51
00:03:38,850 --> 00:03:47,430
And let's at a time, I'm going to add the time that slip here for 10 seconds, that's important time

52
00:03:48,360 --> 00:03:49,410
because he had no problem.

53
00:03:49,410 --> 00:03:55,320
We can use time to sleep, so we are not going to use that in the future if we want to do many things

54
00:03:55,320 --> 00:03:56,340
in the way.

55
00:03:56,490 --> 00:03:56,700
True.

56
00:03:57,090 --> 00:04:02,040
But for this simple example, if we just want to send a message of written seguem, that's OK.

57
00:04:02,310 --> 00:04:10,080
And that's not going to be a problem for the data because this is going to pull the Telegram chats in

58
00:04:10,080 --> 00:04:11,100
a different thread.

59
00:04:11,130 --> 00:04:17,190
OK, so the stuff handler is going to be in a different thread, not on the same thread as this.

60
00:04:17,190 --> 00:04:18,780
So this is not a problem.

61
00:04:18,780 --> 00:04:20,070
We can block the application.

62
00:04:20,880 --> 00:04:26,450
The polling data is still going to work, but then, well, the program is still not complete.

63
00:04:26,460 --> 00:04:27,120
Why is that?

64
00:04:27,120 --> 00:04:33,300
Because now when we start polling and then we do this, and if I do control, see I'm going to exit

65
00:04:33,300 --> 00:04:34,230
from the application.

66
00:04:34,470 --> 00:04:37,950
But first, I need to close the data.

67
00:04:37,950 --> 00:04:42,240
OK, just like when you use Cellule, you need to close cell communication.

68
00:04:42,510 --> 00:04:47,790
Here we need to close the updated with the function idol that was already done for you.

69
00:04:48,210 --> 00:04:49,360
But now we need to do this.

70
00:04:49,360 --> 00:04:56,480
So I'm simply going to do what we did before is to put this while true inside try.

71
00:04:56,520 --> 00:04:57,120
Except.

72
00:04:58,780 --> 00:05:07,510
We've keyboard interrupt, and when we have the keyboard interrupt, I'm going to grab data.

73
00:05:07,960 --> 00:05:09,640
Don't stop.

74
00:05:10,240 --> 00:05:12,640
We use the stop function data.

75
00:05:14,320 --> 00:05:15,730
This can take some time.

76
00:05:15,730 --> 00:05:21,920
So we are also going to print print, stop being a data.

77
00:05:22,960 --> 00:05:23,350
These.

78
00:05:25,310 --> 00:05:27,860
Wait, a few seconds.

79
00:05:29,570 --> 00:05:34,250
OK, so we know we have to wait a bit and not price controversy multiple times.

80
00:05:34,730 --> 00:05:36,650
And let's also other print here.

81
00:05:37,220 --> 00:05:39,170
Same message, so it's easier to do it.

82
00:05:40,490 --> 00:05:43,970
OK, now let's run that code.

83
00:05:46,010 --> 00:05:49,550
OK, so we have to dig around Brooks ready.

84
00:05:50,030 --> 00:05:55,100
We can start to send some coming weeks that we receive hello from Python.

85
00:05:55,460 --> 00:05:59,490
And we also everything single received send message.

86
00:06:00,170 --> 00:06:05,100
So we actually receive high something new and we have to send a message here on the terminal.

87
00:06:05,120 --> 00:06:05,910
Let's wait a bit.

88
00:06:05,940 --> 00:06:06,860
OK, send message.

89
00:06:06,860 --> 00:06:08,710
You can see something.

90
00:06:08,720 --> 00:06:13,880
You and I have also received a notification on my phone and on the desktop.

91
00:06:14,840 --> 00:06:17,560
And so you can see how something new.

92
00:06:17,570 --> 00:06:25,820
I can send a command, receive responses from the callback, and I can also receive independent notifications

93
00:06:26,120 --> 00:06:27,680
all that at this time.

94
00:06:28,300 --> 00:06:30,050
You know, I can go there.

95
00:06:30,080 --> 00:06:30,830
Press control.

96
00:06:30,830 --> 00:06:32,990
See, stop being a data.

97
00:06:32,990 --> 00:06:34,250
Please wait a few signals.

98
00:06:34,250 --> 00:06:35,270
So we wait.

99
00:06:36,690 --> 00:06:43,170
And the abductor is not stopped and apparent exit, you look great.

100
00:06:43,200 --> 00:06:50,040
No, you have a complete Python program structure to communicate between your Raspberry Pi and a Telegram

101
00:06:50,040 --> 00:06:50,430
chat.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: PART 3 - Practice

1
00:00:00,150 --> 00:00:06,060
Let's practice on what you have just seen before, the final project is now very, very close.

2
00:00:06,270 --> 00:00:08,880
Just a few activities and we can start.

3
00:00:09,420 --> 00:00:15,480
So you have learned how to use the Raspberry Pi camera to take some photos and also how to set up a

4
00:00:15,480 --> 00:00:19,980
Telegram bot and control it from your Raspberry Pi in a Python program.

5
00:00:20,280 --> 00:00:26,520
In the following activities you are going to mix the Raspberry Pi functionalities seen with the Arduino

6
00:00:26,520 --> 00:00:29,440
functionalities that we saw in the previous section.

7
00:00:30,030 --> 00:00:36,330
You will be able to send some messages to a Telegram chat with a command that comes from the Arduino,

8
00:00:36,630 --> 00:00:42,780
and you will also be able to remotely control the original from commands you type in the Telegram chat.

9
00:00:43,200 --> 00:00:44,550
Let's get started.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:07,020
In this activity, your challenge is to send a notification to Telegram when your Python program has

2
00:00:07,020 --> 00:00:09,300
successfully connected to the Arduino.

3
00:00:09,510 --> 00:00:15,420
We've cellular communication and also a notification when the communication is closed.

4
00:00:15,900 --> 00:00:20,340
OK, so the code for the communication between the audio and the Raspberry Pi is very simple.

5
00:00:20,580 --> 00:00:20,940
OK.

6
00:00:21,030 --> 00:00:31,380
In the article, you are just going to it in communication and in the Raspberry Pi, you just try to

7
00:00:31,380 --> 00:00:42,120
connect to Arduino and then so you're going to use the retry block that we have seen in a previous lesson

8
00:00:42,120 --> 00:00:42,750
in this course.

9
00:00:43,230 --> 00:00:44,670
And then when connected?

10
00:00:46,330 --> 00:00:56,140
Send a message to Telegram, so you're going to use the bots and also when you are close.

11
00:00:57,340 --> 00:01:00,190
Send also message to Telegram.

12
00:01:00,190 --> 00:01:01,120
So the same thing.

13
00:01:01,810 --> 00:01:03,770
This activity should not be that hard.

14
00:01:03,820 --> 00:01:08,830
You have everything you need to make it work, and I will see you in the next video from the solution.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:06,780
This is the solution of the previous activity where you need to basically inform Telegram when the Python

2
00:00:06,780 --> 00:00:10,130
program has connected and disconnected from the Android.

3
00:00:10,860 --> 00:00:15,660
Let's start with the Arduino and well, the code will be super, super easy.

4
00:00:15,990 --> 00:00:16,770
We just do.

5
00:00:18,330 --> 00:00:24,160
Say that name, and let's use this.

6
00:00:24,180 --> 00:00:30,930
Why not say, OK, well, compatibility with some out new the.

7
00:00:31,890 --> 00:00:33,180
And that's it.

8
00:00:33,780 --> 00:00:36,380
OK, we just want to initialize the communication.

9
00:00:36,390 --> 00:00:39,420
We don't want to send or receive any message here.

10
00:00:39,720 --> 00:00:44,730
So I'm going to just to make sure it's connected and upload the code.

11
00:00:45,870 --> 00:00:49,080
Activity number seven.

12
00:00:52,480 --> 00:00:52,880
OK.

13
00:00:52,900 --> 00:00:54,850
We should not have any error here.

14
00:00:55,000 --> 00:00:55,540
I hope.

15
00:00:57,820 --> 00:00:58,840
And don't imploding.

16
00:00:59,320 --> 00:00:59,830
Great.

17
00:01:00,640 --> 00:01:04,140
So now let's do the interesting part on the Raspberry Pi side.

18
00:01:04,690 --> 00:01:06,250
So here we need to do two things.

19
00:01:07,000 --> 00:01:10,810
First, try to connect to the original ending, send a message to Tehran.

20
00:01:10,810 --> 00:01:13,350
So let's actually do that.

21
00:01:14,020 --> 00:01:16,930
Let's write the serial code before.

22
00:01:17,950 --> 00:01:19,450
So use it.

23
00:01:20,410 --> 00:01:21,610
And buy three.

24
00:01:23,220 --> 00:01:29,250
Let's imports Syria, and let's import time because we will need it.

25
00:01:30,060 --> 00:01:33,430
And then we are going to try to connect.

26
00:01:33,450 --> 00:01:42,540
So basically, we have the line I'm going to right here, sir, is equal to say on Syria, we default.

27
00:01:42,870 --> 00:01:48,120
So the key to what they see in zero, let's check, is correct.

28
00:01:48,250 --> 00:01:51,480
You can check on the terminal also here.

29
00:01:52,290 --> 00:01:54,230
OK, ACM zero.

30
00:01:56,380 --> 00:01:59,260
The board rate the same.

31
00:02:00,630 --> 00:02:08,220
On the aluminum and then started reading out of one things which we are not going to use here.

32
00:02:09,060 --> 00:02:13,320
OK, and before we do anything here, let's put that inside a try.

33
00:02:14,310 --> 00:02:17,160
And so let's indentation here.

34
00:02:17,730 --> 00:02:22,020
Try except say no.

35
00:02:23,990 --> 00:02:27,230
Don't so exceptional.

36
00:02:30,130 --> 00:02:39,790
And before I write the code to handle the exception, let's also put this try except in new wine loops

37
00:02:39,790 --> 00:02:40,690
or an infinite.

38
00:02:43,640 --> 00:02:46,350
So, no, we're going to enter the wild.

39
00:02:46,370 --> 00:02:46,910
True.

40
00:02:46,940 --> 00:02:49,940
We're going to try to connect to cellular if it works.

41
00:02:50,240 --> 00:02:59,000
We print success fully connected to cellular and we break.

42
00:03:00,660 --> 00:03:06,260
Out of the loop, because if we don't break, we're going to continue to try to connect to say.

43
00:03:06,900 --> 00:03:08,720
But we already connected to OK.

44
00:03:09,360 --> 00:03:11,940
And if it doesn't work, that if we have the exception.

45
00:03:13,250 --> 00:03:19,070
We print could not connect to Saddam.

46
00:03:21,310 --> 00:03:32,670
Route trying in, let's say, one segment that in time that sleep with one.

47
00:03:33,250 --> 00:03:36,790
So if we have the exception, we don't break out of the loop.

48
00:03:36,790 --> 00:03:39,340
So we come back here and we try again.

49
00:03:39,730 --> 00:03:46,720
Basically, if we manage to go out of this loop, it means we have connected to sail and I'm going to

50
00:03:46,720 --> 00:03:50,320
do a time that sleep through here.

51
00:03:51,610 --> 00:03:57,420
And then it's not reset inputs, but.

52
00:03:58,870 --> 00:04:03,820
OK, and then well, we have our code, which funnel does nothing.

53
00:04:04,120 --> 00:04:10,780
So what we could do is just maybe directly close the cell communication or maybe add another time to

54
00:04:10,780 --> 00:04:14,050
sleep, for example, for 10 seconds and then close the communication.

55
00:04:14,410 --> 00:04:17,980
I'll just add her voice look kind of a bowl loop here.

56
00:04:18,370 --> 00:04:21,820
So an infinite loop to keep the program up.

57
00:04:22,060 --> 00:04:24,940
And then just close the cell communication when we press control.

58
00:04:24,940 --> 00:04:26,620
See, that's what I'm going to do here.

59
00:04:27,370 --> 00:04:29,080
Another while true.

60
00:04:30,790 --> 00:04:39,310
We've done that, don't sleep well, we can put zero point zero one or whatever, because here we don't

61
00:04:39,310 --> 00:04:47,110
do anything in that white look, and I'm going to put this time that way look inside, tried.

62
00:04:47,340 --> 00:04:55,390
Except except so it's going to be keyboard into it.

63
00:04:56,080 --> 00:05:08,140
So in the keyboard, in direct print clothing sale, then we do send out clothes in.

64
00:05:08,140 --> 00:05:12,850
Note that here to connect, we have Detroit except inside in a way true.

65
00:05:13,480 --> 00:05:16,630
But here we have the white inside Detroit exit.

66
00:05:16,630 --> 00:05:17,950
OK, that's something different.

67
00:05:18,430 --> 00:05:19,120
So no.

68
00:05:19,120 --> 00:05:21,400
Well, the sale code is working.

69
00:05:21,760 --> 00:05:27,520
We can add to the ground, but let's just run it.

70
00:05:29,350 --> 00:05:31,750
Activity seven.

71
00:05:33,800 --> 00:05:41,360
Successfully going to Syria and in controlled sea closing sale, if I disconnect the Arduino board.

72
00:05:42,470 --> 00:05:43,520
Let's try again.

73
00:05:45,110 --> 00:05:51,410
Retraining once again and connection, they are going bold and successfully connected to, say, a control

74
00:05:51,410 --> 00:05:51,810
seat.

75
00:05:53,270 --> 00:05:54,110
OK, it works.

76
00:05:54,740 --> 00:05:55,520
Here we have.

77
00:05:55,550 --> 00:05:55,820
OK.

78
00:05:56,060 --> 00:05:58,790
I did control to see when we were in the time of sleep.

79
00:05:59,330 --> 00:06:00,170
I didn't wait.

80
00:06:02,160 --> 00:06:05,400
The correct amount of time, maybe that's just an print here.

81
00:06:07,910 --> 00:06:09,810
So, OK.

82
00:06:12,170 --> 00:06:12,680
And.

83
00:06:13,890 --> 00:06:18,100
You wait three seconds.

84
00:06:19,110 --> 00:06:24,960
OK, and now let's right into Telegram, but so important Telegram.

85
00:06:25,170 --> 00:06:27,630
So here we just want to send some notification.

86
00:06:27,630 --> 00:06:30,750
We don't want to interact with the user on the chat.

87
00:06:31,000 --> 00:06:37,650
OK, so let's just do actually from telegram imports.

88
00:06:39,120 --> 00:06:48,540
But let's create a Telegram bot so we can create it when we could create it before saying I'm just going

89
00:06:48,540 --> 00:06:55,350
to create it here after we have connected to sail, but is equal to but.

90
00:06:57,130 --> 00:07:02,410
We've spoken and whether we need to give the talking, so let's do.

91
00:07:04,050 --> 00:07:12,990
We've opened and then it's fine, this fine where we have the talking, actually, which is in slush

92
00:07:13,290 --> 00:07:21,840
or slush by slush that look our slush shack and Slashdot Telegram.

93
00:07:23,680 --> 00:07:27,990
But look, so if you don't have this, please go back and watch.

94
00:07:28,630 --> 00:07:37,840
Listen, when I say the talking and then we are as if and we can do.

95
00:07:39,670 --> 00:07:40,330
Telegram.

96
00:07:42,130 --> 00:07:42,590
OK, can.

97
00:07:44,380 --> 00:07:45,330
It is equal to.

98
00:07:46,690 --> 00:07:52,220
If that read to read all the fine, because we just have to conduct asked trip.

99
00:07:54,190 --> 00:08:02,560
So remove any unwanted character and token is equal to Telegram token.

100
00:08:03,460 --> 00:08:05,710
OK, we have the bot ready.

101
00:08:06,220 --> 00:08:08,770
Let's just chat it.

102
00:08:10,000 --> 00:08:12,940
So actually what we have, I'm going to open.

103
00:08:14,550 --> 00:08:24,180
Our Telegram centrifugation program we just used before, and I'm just going to use this chat 80 here.

104
00:08:25,050 --> 00:08:27,480
So use the same as we used previously.

105
00:08:30,000 --> 00:08:37,110
OK, but he is now correctly setup and no, we can send a message, so basically we need to send a message

106
00:08:37,110 --> 00:08:42,270
when the cellular is connected, so the cell is actually connected here.

107
00:08:42,270 --> 00:08:45,140
But then in the code, we wait for three signals.

108
00:08:45,150 --> 00:08:48,660
We reset the input and we consider that it is OK here.

109
00:08:48,870 --> 00:08:54,780
So I'm going to wait OK to send a message to Telegram after this timelessly.

110
00:08:55,020 --> 00:08:56,610
OK, so let's do that here.

111
00:08:56,880 --> 00:09:00,330
Let's do but that send a message.

112
00:09:01,470 --> 00:09:15,990
Chad is equal to Chad, and text is equal to, let's say, connected to our, you know, we say, let's

113
00:09:15,990 --> 00:09:17,400
go to a new line here.

114
00:09:21,290 --> 00:09:27,470
Higginson, whatever you want, maybe you can send information such as the port, the board, right?

115
00:09:28,520 --> 00:09:30,680
OK, but here we keep things simple.

116
00:09:31,490 --> 00:09:37,670
So we send a message when we have the communication ready to be used and then we also going to send

117
00:09:37,670 --> 00:09:41,660
a message here just before we close the sale or maybe just after we close it.

118
00:09:41,660 --> 00:09:47,310
It doesn't really matter here, but that send message.

119
00:09:47,450 --> 00:09:50,720
We've checked an easy call to check it.

120
00:09:53,240 --> 00:09:55,760
And fixed equals to.

121
00:09:57,550 --> 00:09:58,330
Disconnected

122
00:10:01,090 --> 00:10:03,810
from outer.

123
00:10:06,510 --> 00:10:10,080
All right, now, we can try this code.

124
00:10:11,010 --> 00:10:18,510
So I'm going to use the Telegram app on the Raspberry Pi, you can use the three up on any desktop environment

125
00:10:18,520 --> 00:10:20,980
you want on your computer, on your phone.

126
00:10:21,000 --> 00:10:26,370
It doesn't really matter if you use if you have the Telegram app on your phone, you're going to receive

127
00:10:26,370 --> 00:10:27,480
some notifications.

128
00:10:29,100 --> 00:10:32,010
Let's put that here, and let's run scripts.

129
00:10:34,350 --> 00:10:41,340
Wait three seconds and then say, OK, we have an inspiration here connected to Arduino Wi-Fi Cellular.

130
00:10:42,240 --> 00:10:48,600
And if I press control, see closing cellular, you can see disconnected from Arduino.

131
00:10:48,930 --> 00:10:55,650
OK, so using this can be a good way to actually know, for example, if your program is currently working.

132
00:10:56,070 --> 00:11:02,070
So if you have a project with Arduino and Raspberry Pi and for example, you want to keep the connection

133
00:11:02,070 --> 00:11:03,870
alive for a long time.

134
00:11:04,620 --> 00:11:10,050
You could try to detect when the communication is down and then send a message to the telegram up so

135
00:11:10,050 --> 00:11:15,780
you can be notified as soon as possible and then you can eventually fix this problem by yourself.

136
00:11:16,260 --> 00:11:16,590
All right.

137
00:11:16,620 --> 00:11:18,270
And that's the end of this activity.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:06,600
In this new activity, you are going to control your adrenal from Telegram and, of course, going through

2
00:00:06,600 --> 00:00:07,590
the Raspberry Pi.

3
00:00:07,980 --> 00:00:13,500
So basically what you have to do is go when you are going to send some commands from the jets.

4
00:00:13,770 --> 00:00:17,530
So you're going to control the algae end LCD screens.

5
00:00:17,530 --> 00:00:24,990
So for example, you type slush LCD, that's going to be the command and then some text, you're going

6
00:00:24,990 --> 00:00:25,620
to type this.

7
00:00:25,830 --> 00:00:27,180
So far, it doesn't do anything.

8
00:00:27,450 --> 00:00:34,740
And this text heat should appear on the LCD screen and also a command fault that olujimi editing.

9
00:00:35,370 --> 00:00:38,220
OK, so now we arrive at things a little bit more complex.

10
00:00:38,220 --> 00:00:42,600
But again, if you have corrections understood the following it should not be a problem.

11
00:00:42,600 --> 00:00:44,070
You can manage to do it by yourself.

12
00:00:44,370 --> 00:00:51,420
So on the outermost side, what you're going to do is just open sail and handle sail commands for RGV

13
00:00:51,870 --> 00:00:53,130
and LCD screen.

14
00:00:53,400 --> 00:00:57,060
So for LCD screen, I will let you define a protocol.

15
00:00:57,060 --> 00:01:01,770
So what kind of comment you can send from what we have done before?

16
00:01:01,770 --> 00:01:03,210
You should be able to do that.

17
00:01:03,540 --> 00:01:09,450
And for the Artemis element, what we have done previously was to set each color independently because

18
00:01:09,450 --> 00:01:12,680
you would send Rajputs and green and you would send blue.

19
00:01:13,250 --> 00:01:19,800
Here we are going to improve a little bit and instead of sending green blue red, we are going to just

20
00:01:19,800 --> 00:01:22,770
send one command for the three columns, OK?

21
00:01:23,430 --> 00:01:27,930
And here I have shown you an example to use Chroma.

22
00:01:29,880 --> 00:01:36,340
So we have to commend sit like this and then we have three numbers.

23
00:01:36,720 --> 00:01:38,880
So this is going to be sent as a string, of course.

24
00:01:39,600 --> 00:01:45,870
And so you take the documents that we've set and you remove the first one two three four five six seven

25
00:01:45,870 --> 00:01:52,980
eight characters and then you are left with this and then you have the substring function that you can

26
00:01:52,980 --> 00:01:58,140
use on the string on the string to just get one part of the string.

27
00:01:58,160 --> 00:02:06,270
So there's no zero one two three OK and then four, five, six seven and an eight to the end, and you're

28
00:02:06,270 --> 00:02:07,950
going to guess that to an integer.

29
00:02:08,370 --> 00:02:09,550
And so you have red green.

30
00:02:10,320 --> 00:02:16,320
One very important thing is that when you send the command and from the Raspberry Pi and also from Telegram,

31
00:02:16,590 --> 00:02:19,510
you have to respect the number of characters here.

32
00:02:19,530 --> 00:02:19,920
OK.

33
00:02:20,430 --> 00:02:21,580
So I am showing you an example.

34
00:02:21,630 --> 00:02:27,210
So if you send 200 for red, you just for 200 if you want, but zero for green, you don't just put

35
00:02:27,300 --> 00:02:28,160
zero like this.

36
00:02:28,440 --> 00:02:31,260
You have to put three zero for it to work.

37
00:02:31,980 --> 00:02:34,680
And for 80, you just don't send anti-U.S..

38
00:02:35,760 --> 00:02:36,440
We will zero.

39
00:02:36,450 --> 00:02:39,510
So you make sure you have three characters for each.

40
00:02:39,510 --> 00:02:40,200
Kunal, OK?

41
00:02:40,860 --> 00:02:43,830
And that's the way we are going to be able to read the colors.

42
00:02:44,190 --> 00:02:48,390
You could do something different, of course, to improve it, but we're going to stay with that.

43
00:02:48,390 --> 00:02:52,290
And that's a pretty efficient way actually to set to any.

44
00:02:52,980 --> 00:02:55,920
OK, so that's it for the out on a site on the Raspberry Pi sides.

45
00:02:55,920 --> 00:02:57,150
Are you going to connect to cellular?

46
00:02:57,600 --> 00:02:58,970
You're going to create some.

47
00:02:58,980 --> 00:03:01,530
So here you don't send notification to Telegram.

48
00:03:01,530 --> 00:03:02,910
You will receive some comments.

49
00:03:02,910 --> 00:03:06,970
So you're going to create a command handler within a data dispatcher.

50
00:03:07,440 --> 00:03:13,840
And then when you receive a command, you directly pass it to the original OK with the correct comment.

51
00:03:13,880 --> 00:03:25,680
So for example, if I send here, let's say Ogbe, and then so to 100 comma zero zero zero zero 18,

52
00:03:26,250 --> 00:03:33,090
if I send this in exactly this, you're going to receive that on the Raspberry Pi and you're not going

53
00:03:33,090 --> 00:03:38,910
to send RGV, you're going to send set any column, you're going to add this and you're going to add

54
00:03:39,150 --> 00:03:40,980
a new line character.

55
00:03:41,310 --> 00:03:45,750
So you're received a coming from three on the Raspberry Pi and you make sure that you send the correct

56
00:03:45,750 --> 00:03:50,790
command for the Arduino so that you can understand what you're asking to do.

57
00:03:51,660 --> 00:03:53,910
OK, I will see you in the next lesson.

58
00:03:53,910 --> 00:03:54,990
Fault the solution.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:06,240
This is the solution of the previous activities of activity, but Pete, where you have to control Arduino

2
00:00:06,240 --> 00:00:12,470
from Telegram so you can send some text on the LCD screen and you can also choose the colour for the

3
00:00:12,480 --> 00:00:14,880
RGV and you're just one command.

4
00:00:15,390 --> 00:00:16,660
So we have a few things to do.

5
00:00:16,680 --> 00:00:21,510
Let's start as always with the Arduino side and let's.

6
00:00:22,320 --> 00:00:24,420
OK, let's initialize Sergio here

7
00:00:27,660 --> 00:00:28,500
with the other right?

8
00:00:29,520 --> 00:00:36,030
Why not say, OK, that's pretty fast to do?

9
00:00:36,660 --> 00:00:42,210
And then we will need to initialize the LCD and the Ogbe.

10
00:00:42,720 --> 00:00:50,760
So let's create the defined define RGV right being, which is 11 define.

11
00:00:52,580 --> 00:01:02,750
RGV green pin, which is then let's not make a mistake thing on the Blue Blue Pea, which is nine and

12
00:01:02,770 --> 00:01:11,890
not 19 like I did before, and then define LCD as being.

13
00:01:12,200 --> 00:01:21,620
I'm going to put the number just after the fine LCD been defined LCD default.

14
00:01:24,500 --> 00:01:30,650
So we have the four five six seven five.

15
00:01:32,280 --> 00:01:34,140
Six seven.

16
00:01:35,060 --> 00:01:43,800
We've a four, a five, two, three, four and five.

17
00:01:44,880 --> 00:01:47,280
Can you make sure are correctly configured?

18
00:01:48,690 --> 00:01:54,720
We include the liquid crystal, but.

19
00:01:55,720 --> 00:01:56,740
We've y here.

20
00:01:57,900 --> 00:02:03,510
Each and then we create the liquid crystal here, so liquid.

21
00:02:05,400 --> 00:02:11,040
Crystal and City, so that initialization is always the same, you can even copy paste the code from

22
00:02:11,040 --> 00:02:11,760
the previous.

23
00:02:14,550 --> 00:02:19,740
Listen, if you want to address it before.

24
00:02:21,500 --> 00:02:22,040
And then.

25
00:02:25,300 --> 00:02:28,210
Five, the six.

26
00:02:30,470 --> 00:02:30,890
And.

27
00:02:33,500 --> 00:02:34,040
This over.

28
00:02:36,810 --> 00:02:38,010
OK, let's do.

29
00:02:39,800 --> 00:02:42,950
LCD to begin 16 by two.

30
00:02:45,410 --> 00:02:53,690
And let's also do the pin mode we've Ogbe parade.

31
00:02:57,260 --> 00:02:58,040
To output.

32
00:03:00,280 --> 00:03:02,950
And then same for the green.

33
00:03:06,570 --> 00:03:07,710
And the sing for the Blue.

34
00:03:11,410 --> 00:03:17,530
And we are done with initialization of the Arduino components, not in the void loop.

35
00:03:18,850 --> 00:03:23,620
So we're now running that and I'm going to do this again, explaining it step by step.

36
00:03:24,850 --> 00:03:29,890
So in the view, look, we don't have any other thing to do than checking the same.

37
00:03:30,190 --> 00:03:36,400
So you're saying that they label greater strictly than zero?

38
00:03:37,300 --> 00:03:46,240
We are going to read the command is equal to say good read string until.

39
00:03:48,210 --> 00:03:49,050
Backslash and.

40
00:03:50,460 --> 00:03:54,540
And then we're going to check if command is equal to.

41
00:03:54,750 --> 00:03:56,910
OK, let's start with the LCD.

42
00:03:57,330 --> 00:04:01,440
What government do we recipe and what command do we send here?

43
00:04:02,070 --> 00:04:07,680
So this command will contain first something that we can recognize, for example, print text, but

44
00:04:07,680 --> 00:04:11,850
then it's going to contain something that we don't know yet from the order of sight.

45
00:04:11,880 --> 00:04:12,210
OK.

46
00:04:12,840 --> 00:04:19,530
So instead of just checking the equality for the command, I'm going to if commander starts wave.

47
00:04:19,530 --> 00:04:27,090
And let's say that the command starts with print text column and then we have the text.

48
00:04:27,510 --> 00:04:32,980
So if it starts with this, we are going to do commands a remove.

49
00:04:33,810 --> 00:04:44,370
So we remove the first commands of one two three four five six seven eight nine 10 11, so we remove

50
00:04:44,380 --> 00:04:45,860
from zero to 11.

51
00:04:47,900 --> 00:04:55,100
And we are left with the text to print, and let's do density, don't print command.

52
00:04:55,730 --> 00:04:59,480
And before we print the we could also, for example, do LCD not clear.

53
00:05:00,920 --> 00:05:04,640
And Anthony said Salt.

54
00:05:06,520 --> 00:05:08,020
Zero zero.

55
00:05:08,590 --> 00:05:09,050
We clear.

56
00:05:09,070 --> 00:05:11,440
We come back to the beginning, we print the text.

57
00:05:12,400 --> 00:05:15,520
OK, let's go to the next.

58
00:05:16,480 --> 00:05:23,690
And if command starts, we know we have to sit and.

59
00:05:25,330 --> 00:05:30,390
OK, so we check if it's a print command opposite any command.

60
00:05:31,930 --> 00:05:39,280
If this is the case, OK, before I forget, I'm just going to add else where we do nothing for now.

61
00:05:41,350 --> 00:05:47,000
And when I would a best practice in the final project, what I this is that we're going to see later.

62
00:05:47,020 --> 00:05:48,250
One thing at a time.

63
00:05:48,790 --> 00:05:55,060
So if we have to commend the staff, we've said then one two three four five six seven eight.

64
00:05:55,490 --> 00:05:56,980
We commend that.

65
00:05:57,550 --> 00:05:59,230
Remove zero eight.

66
00:06:00,160 --> 00:06:11,050
And then we get each column so inch right is equal to come in that said strain from zero to three and

67
00:06:11,050 --> 00:06:13,450
dots to it.

68
00:06:14,470 --> 00:06:15,160
OK, you can.

69
00:06:15,310 --> 00:06:17,860
But this doesn't help if you want to count.

70
00:06:18,910 --> 00:06:19,900
Let's say we have this.

71
00:06:21,810 --> 00:06:26,820
So zero, one, two, three and then four, five, six seven.

72
00:06:27,810 --> 00:06:30,210
So we do things great.

73
00:06:30,360 --> 00:06:37,290
Of course, it's important that when you send to criminal respect to other red green blue commandos

74
00:06:37,560 --> 00:06:38,370
substring.

75
00:06:41,480 --> 00:06:43,410
From four to seven.

76
00:06:43,910 --> 00:06:51,290
So we just ignore the command to it in blue is equal to commended

77
00:06:54,500 --> 00:06:55,300
substring.

78
00:06:56,200 --> 00:07:04,310
OK, if this is seven and eight but eight and we don't need to provide end if we just want to go and

79
00:07:04,310 --> 00:07:12,410
Indian, OK, so we're just going the three last characters to insert the two into because we have a

80
00:07:12,410 --> 00:07:22,490
string we need to convert in so we can use in analogue right and then overwrite with the right first.

81
00:07:24,540 --> 00:07:26,070
And we give right call.

82
00:07:26,550 --> 00:07:31,170
I mean, it's the same for green and blue.

83
00:07:33,530 --> 00:07:38,870
Green with green and blue.

84
00:07:42,530 --> 00:07:43,700
We do.

85
00:07:44,060 --> 00:07:52,880
We just got, OK, let's remove that, and I think our program is complete.

86
00:07:53,270 --> 00:07:54,440
Let's just try it.

87
00:07:54,730 --> 00:08:02,450
OK, let's blow the code activity eight.

88
00:08:03,730 --> 00:08:04,630
And let's right.

89
00:08:07,380 --> 00:08:09,420
Can we first have an error here?

90
00:08:11,320 --> 00:08:12,940
Yes, because I forgot.

91
00:08:13,060 --> 00:08:15,960
So she's quite a sneaky error here.

92
00:08:16,000 --> 00:08:16,750
I forgot.

93
00:08:18,740 --> 00:08:24,830
The practice is because we open practices with open ones, so we have to close to and for the same here.

94
00:08:26,340 --> 00:08:26,700
Alone.

95
00:08:28,460 --> 00:08:35,390
OK, the compiling works, no, the blogging should work as well, and well, let's try something here.

96
00:08:35,510 --> 00:08:40,940
So I'm going to open the science monitor and let's send some comment.

97
00:08:40,940 --> 00:08:48,800
For example, we want to bring something so print text we oh, let's put a space here, for example.

98
00:08:48,810 --> 00:08:49,330
Hello.

99
00:08:50,120 --> 00:08:58,010
What you can see we have Helloworld on the screen here, and we have we have actually one space before

100
00:08:58,040 --> 00:08:58,400
it goes.

101
00:08:58,610 --> 00:09:03,710
You can see we have added one space, so everything that we have after print text, Conan is going to

102
00:09:03,710 --> 00:09:05,090
be printed.

103
00:09:05,570 --> 00:09:08,810
Let's change the string with ABC, for example.

104
00:09:09,410 --> 00:09:15,110
You can see now everything has been cleared, which starts back at the beginning and we print ABC eight.

105
00:09:15,620 --> 00:09:19,710
If I do Jimmy, no actually set any.

106
00:09:20,300 --> 00:09:25,900
We've got 200, then zero and then 180.

107
00:09:27,560 --> 00:09:31,090
We have a purple, a purple color.

108
00:09:31,370 --> 00:09:32,600
So it's correctly working.

109
00:09:33,140 --> 00:09:39,710
OK, so now that we know the original code is working, let's write the code so that we can actually

110
00:09:39,710 --> 00:09:41,690
control this from Telegram.

111
00:09:41,990 --> 00:09:50,210
OK, so on the Raspberry Pi, let's first connect to cellular and I'm going to see I'm going to write

112
00:09:50,210 --> 00:09:51,590
the code entirely.

113
00:09:52,980 --> 00:09:56,600
I'm going to use the code we did previously.

114
00:09:57,360 --> 00:09:58,450
We do try.

115
00:09:58,560 --> 00:09:58,800
OK.

116
00:10:01,230 --> 00:10:02,370
So like this.

117
00:10:03,780 --> 00:10:04,470
And then.

118
00:10:06,700 --> 00:10:07,240
This.

119
00:10:09,770 --> 00:10:17,770
So we connect, we try to connect to sail, and then we wait for three seconds, so OK.

120
00:10:18,140 --> 00:10:27,020
And we have this infinite loop running inside try except block.

121
00:10:28,010 --> 00:10:31,430
And now I am going to add, so I'm just going to leave it there.

122
00:10:32,450 --> 00:10:39,590
I'm just going to comment that this is a comment and I'm going to add the Telegram functionality.

123
00:10:39,710 --> 00:10:53,120
So from Telegram that we are going to import this type of data and comment handler, I'm going to get

124
00:10:53,120 --> 00:10:55,910
the token like we need before.

125
00:10:55,910 --> 00:10:57,620
So I'm just going to get the token.

126
00:10:59,030 --> 00:10:59,630
Like this?

127
00:11:01,630 --> 00:11:11,380
So, for example, here and then we are going to create not a but object, but update us when data is

128
00:11:11,380 --> 00:11:13,150
equal to the data.

129
00:11:15,350 --> 00:11:20,390
We've token equals Telegram token.

130
00:11:20,780 --> 00:11:24,120
OK, so we did that after we have correctly initialized the sale here.

131
00:11:25,340 --> 00:11:35,870
We added a dispatcher, which is a data that dispatcher and then we are going to add some callbacks.

132
00:11:36,680 --> 00:11:42,260
So let's add the callbacks right here before this code.

133
00:11:42,740 --> 00:11:53,520
So this let's say we have this Dot's handler, OK, let's always create a stop handler date context.

134
00:11:54,590 --> 00:12:03,440
And in this dart handler, we do context that, but that send message.

135
00:12:05,060 --> 00:12:08,210
We've checked it is equal to update.

136
00:12:08,420 --> 00:12:12,320
That's effective chat.

137
00:12:12,500 --> 00:12:13,280
That's aid.

138
00:12:14,090 --> 00:12:17,780
And next is equal to let's say hello.

139
00:12:21,180 --> 00:12:23,790
Now, maybe just one car.

140
00:12:24,640 --> 00:12:32,810
OK, we have Scott Handler, then we create a let's name it's LCT handler, OK?

141
00:12:34,270 --> 00:12:36,820
The context.

142
00:12:38,220 --> 00:12:42,210
And what do we do when we receive a comment from Anthony?

143
00:12:42,480 --> 00:12:46,650
We are going to send that coming to the Rosemary Barton.

144
00:12:47,040 --> 00:12:56,910
So how to get the text text is a date that message, not texts.

145
00:12:57,270 --> 00:12:58,200
I'm going to remove that.

146
00:12:58,200 --> 00:13:01,080
No and no.

147
00:13:02,120 --> 00:13:12,050
The string to send to the command is going to be equal to print text because we need to send print text

148
00:13:12,050 --> 00:13:12,410
here.

149
00:13:13,560 --> 00:13:18,650
And plus text and then plus backslash pen.

150
00:13:19,850 --> 00:13:21,770
And we do say that.

151
00:13:23,180 --> 00:13:29,600
Right, command notes don't encode we've UTF eight.

152
00:13:31,580 --> 00:13:32,020
OK.

153
00:13:32,600 --> 00:13:40,760
And also what we could do is just send back a message to our vote to confirm that we have gone operational,

154
00:13:41,540 --> 00:13:44,500
context notes, but that.

155
00:13:45,380 --> 00:13:47,090
So actually, that's going to be the same as you.

156
00:13:50,190 --> 00:13:53,520
And text that's just saying, OK.

157
00:13:54,880 --> 00:14:02,680
All right, now we have this Ogbe handler, so you just name it as you want, that's just a function

158
00:14:03,340 --> 00:14:05,430
of the context.

159
00:14:06,100 --> 00:14:12,500
But as you can see, I usually put Handler, OK, I put the name of the command and in handler so that

160
00:14:12,520 --> 00:14:15,400
it's easier to navigate the code.

161
00:14:16,560 --> 00:14:25,680
OK, we have the text, which is also of the note message, does text we create the command is equal

162
00:14:25,680 --> 00:14:26,040
to.

163
00:14:27,540 --> 00:14:30,030
So the command this time is that any?

164
00:14:32,170 --> 00:14:40,090
We'll call on and we expect to use from Telegram to give us the correct format for the comment.

165
00:14:40,140 --> 00:14:42,790
We're going to think so this, I'm just going to leave it like that.

166
00:14:43,080 --> 00:14:50,430
But as an improvement, what you could do is to validate the data here also and then try to find another

167
00:14:50,430 --> 00:14:57,870
way to send data with a less strict format, less backslash in.

168
00:14:58,180 --> 00:14:59,820
And then let's not forget that.

169
00:15:00,270 --> 00:15:02,610
And then we just do the same thing here.

170
00:15:04,530 --> 00:15:08,790
We write the comment and we send back a message to the chat.

171
00:15:09,480 --> 00:15:17,100
OK, now let's not forget to add those handlers or dispatcher the ad handler.

172
00:15:19,230 --> 00:15:30,430
Comment handler, and we have so the key word that is going to go with stock handler and then let's

173
00:15:30,480 --> 00:15:32,880
add another two of those.

174
00:15:35,130 --> 00:15:40,410
We will have the command inside, which is going to go with Nancy Handler.

175
00:15:40,950 --> 00:15:46,740
So you don't necessarily have to put the same command here and same name for the function.

176
00:15:46,740 --> 00:15:47,130
It doesn't.

177
00:15:47,370 --> 00:15:48,300
It is not linked.

178
00:15:48,330 --> 00:15:54,300
OK, I just use it for simplicity and RGV command for the Ogbe handler.

179
00:15:55,170 --> 00:15:55,470
OK.

180
00:15:55,530 --> 00:16:05,320
After we have all the documents that are ready to be dispatched, we do a data that starts pulling.

181
00:16:06,480 --> 00:16:14,280
And the last thing is that when we actually close the program, we do closing sale and we then do print.

182
00:16:16,880 --> 00:16:31,370
Stopping Telegram data where we have to wait a few signals and data that stuck here, so we stopped

183
00:16:31,370 --> 00:16:32,000
and we stopped.

184
00:16:32,840 --> 00:16:34,820
All right, let's try this code.

185
00:16:36,200 --> 00:16:44,120
So we have written to more than 50 lines of code, and it's just trying to see if it works activity.

186
00:16:46,950 --> 00:16:47,280
Eight.

187
00:16:50,650 --> 00:16:51,860
So let's see what we get.

188
00:16:51,890 --> 00:16:55,020
He successfully connected to sail.

189
00:16:55,100 --> 00:16:55,830
Sail took.

190
00:16:57,210 --> 00:17:04,170
Now, let's open Telegram and let's just send some comments or LCD.

191
00:17:05,340 --> 00:17:05,730
Hello.

192
00:17:06,060 --> 00:17:07,290
Let's see what we get.

193
00:17:08,460 --> 00:17:08,680
OK?

194
00:17:08,700 --> 00:17:13,010
You can see on the screen we have not just hello, but we have slush LCD space.

195
00:17:13,020 --> 00:17:13,350
Hello.

196
00:17:14,010 --> 00:17:16,050
So we need to come back to our program.

197
00:17:16,590 --> 00:17:23,580
And while we haven't tested, so press kind of look if it was going to work or not, but when you see

198
00:17:23,580 --> 00:17:28,410
that we get that message to text, we get the complete text.

199
00:17:28,650 --> 00:17:28,980
OK?

200
00:17:29,670 --> 00:17:32,160
Even with the comment and this piece.

201
00:17:33,000 --> 00:17:35,350
So we need to remove that before we send it.

202
00:17:35,370 --> 00:17:35,910
Of course.

203
00:17:36,570 --> 00:17:42,840
So what we can do is actually something similar, and that we did in under Arduino is to remove the

204
00:17:42,840 --> 00:17:45,330
first and characters can do that.

205
00:17:45,690 --> 00:17:47,150
It's going to be simpler.

206
00:17:47,760 --> 00:17:48,930
So he will receive.

207
00:17:51,150 --> 00:17:55,260
So we received slush and sea space and then comment.

208
00:17:57,600 --> 00:18:02,370
So we have one two three four five characters to remove.

209
00:18:02,790 --> 00:18:07,350
So what we can do is just do five and column and write it.

210
00:18:07,350 --> 00:18:10,870
So the string is also an array of characters.

211
00:18:10,940 --> 00:18:14,820
OK, so if you do that, you're going to remove the first five characters.

212
00:18:14,850 --> 00:18:17,580
OK, let's run again.

213
00:18:21,910 --> 00:18:24,550
And once it is connected, let's send.

214
00:18:25,960 --> 00:18:26,620
The same.

215
00:18:27,590 --> 00:18:28,520
And Sydney, hello.

216
00:18:31,760 --> 00:18:34,280
And you can see now we have.

217
00:18:35,450 --> 00:18:37,010
On the screen.

218
00:18:37,850 --> 00:18:45,330
And so I'm going to come back to the program to change, of course, here for the energy analyst, for

219
00:18:45,330 --> 00:18:46,160
the energy handler.

220
00:18:46,180 --> 00:18:46,640
We have.

221
00:18:48,570 --> 00:18:57,180
Slush RGV and then coming, so we have also one two, three four five characters to remove, so we do

222
00:18:57,180 --> 00:19:03,540
this by column brackets to take everything after the chief character.

223
00:19:04,500 --> 00:19:05,460
Let's run down.

224
00:19:10,070 --> 00:19:23,510
Say up, OK, and let's say we slash up meat, let's give synchronize beef pork to 100 zero 180 and

225
00:19:23,510 --> 00:19:24,440
let's see what we get.

226
00:19:24,710 --> 00:19:29,030
You can see now the object is purple.

227
00:19:29,390 --> 00:19:33,990
OK, let's bring some text and see it works.

228
00:19:35,030 --> 00:19:36,890
And will it correctly works?

229
00:19:38,180 --> 00:19:42,620
We can control the Arduino components from Telegram chat.

230
00:19:43,310 --> 00:19:43,630
All right.

231
00:19:43,640 --> 00:19:45,980
And this is the end of this activity.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:08,030
And he is yet another activity, and we are just a few steps before the final project and this activity,

2
00:00:08,040 --> 00:00:10,470
we are going to walk, we do a Raspberry Pi camera.

3
00:00:10,740 --> 00:00:14,970
So you're having to take a photo with the Raspberry Pi camera every two seconds.

4
00:00:15,000 --> 00:00:15,330
OK.

5
00:00:15,870 --> 00:00:20,970
And I put the looking because you're not going to use time sleep do you're going to use an unblocking

6
00:00:20,970 --> 00:00:24,420
way to take the photo every two seconds like we did before?

7
00:00:24,540 --> 00:00:30,390
And then the goal is to send this photo on to run when you are some condition that is triggered so you

8
00:00:30,390 --> 00:00:34,160
could receive a button message from the astronauts on the Arduino.

9
00:00:34,200 --> 00:00:37,830
You're going to read from the push button and just send button pressed.

10
00:00:37,840 --> 00:00:39,660
So we already did that before.

11
00:00:40,020 --> 00:00:45,210
And also, if you receive a get photo comment from Telegram, you send the photo.

12
00:00:45,300 --> 00:00:52,230
So basically, this is a way to keep taking photos and just send a photo to Telegram when you are requested.

13
00:00:52,470 --> 00:00:55,830
So when you request the photo, you get the latest photo.

14
00:00:56,190 --> 00:00:58,140
All right, and now we see you in the next lesson.

15
00:00:58,140 --> 00:00:59,250
Fault the solution.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:05,790
This is the solution of the produce activity where you have to take a photo every two seconds on the

2
00:00:05,790 --> 00:00:11,380
Raspberry Pi and then send the photo when you're requested, either from Tehran off from the.

3
00:00:12,600 --> 00:00:14,700
And it dealt with this Oudin account, actually.

4
00:00:15,210 --> 00:00:18,660
And well, this what we've already done that multiple times.

5
00:00:18,660 --> 00:00:27,450
So I'm going to open activity number six, for example, in on the activity number six, I have the

6
00:00:27,450 --> 00:00:29,370
code to read from the pulpit.

7
00:00:29,470 --> 00:00:38,040
I'm just going to copy this and put that here, and I'm just going to remove what I don't need.

8
00:00:39,140 --> 00:00:43,040
So we were using the seven motor, but I'm not going to use several.

9
00:00:43,100 --> 00:00:44,390
You just push a button.

10
00:00:45,840 --> 00:00:52,260
So I'm going to prove that I'm going to keep the CIA, of course, where it is both the right and then

11
00:00:52,260 --> 00:00:54,060
I'm going to remove this part.

12
00:00:56,220 --> 00:01:00,570
So as you can see, we've say, all the crude that we need is quite module.

13
00:01:00,630 --> 00:01:05,430
But look, we can just take some but remove some other parts and it's quite easy.

14
00:01:05,880 --> 00:01:12,660
And now when we have the complete code to read from the press button and send button pressed when the

15
00:01:12,660 --> 00:01:15,270
button has been priced with the £d mechanism.

16
00:01:15,540 --> 00:01:20,070
OK, I am going to blow this to you directly.

17
00:01:21,450 --> 00:01:23,430
Activity nine.

18
00:01:25,440 --> 00:01:25,800
That's the.

19
00:01:28,650 --> 00:01:34,430
And what happened with my ordinary is not it to a Raspberry Pi.

20
00:01:35,460 --> 00:01:37,020
So that's not going to work.

21
00:01:38,800 --> 00:01:39,820
You can see, no, OK.

22
00:01:39,850 --> 00:01:41,320
That's something very interesting.

23
00:01:41,980 --> 00:01:46,570
This time, I don't have to wait ACM zero, I have did wait ACM one.

24
00:01:47,050 --> 00:01:53,170
OK, let's try to disconnect again and connect back.

25
00:01:54,250 --> 00:01:58,210
Let's see again what we have, and we still have ACM one.

26
00:01:58,210 --> 00:01:59,680
So I'm going to use ACM one.

27
00:02:00,010 --> 00:02:04,270
And that's something to know when we try to connect from the Raspberry Pi.

28
00:02:04,280 --> 00:02:07,000
OK, so upload.

29
00:02:10,430 --> 00:02:18,020
Down applauding, let's just check that if I press on the push button and get button pressed.

30
00:02:18,260 --> 00:02:19,250
That's correct.

31
00:02:19,910 --> 00:02:21,920
Now let's go to the Raspberry Pi side.

32
00:02:22,280 --> 00:02:23,590
So we need to do a few things.

33
00:02:23,600 --> 00:02:27,290
We need to read the sale to get the push button notification.

34
00:02:27,770 --> 00:02:34,230
We need to take a photo every two seconds, and we need to also send it to Telegram and receive callbacks

35
00:02:34,250 --> 00:02:35,030
from Tehran.

36
00:02:35,870 --> 00:02:41,360
Let's do the first thing here, maybe to take a photo every two seconds when I remove that.

37
00:02:47,030 --> 00:02:48,420
OK, let's import.

38
00:02:48,440 --> 00:02:54,990
So from my camera import by camera like this?

39
00:02:55,640 --> 00:02:58,010
And then let's create a camera.

40
00:02:58,030 --> 00:03:02,090
So camera is equal to my camera.

41
00:03:02,510 --> 00:03:04,040
Let's put the settings directly.

42
00:03:05,030 --> 00:03:06,440
Camera Dot.

43
00:03:07,740 --> 00:03:16,080
Resolution, and I'm going to use a quite small one because when we don't need more actually for what

44
00:03:16,530 --> 00:03:26,430
we want to in camera rotation is equal to 180 because I have seen before that the images I take are

45
00:03:26,430 --> 00:03:27,450
upside down.

46
00:03:27,990 --> 00:03:33,450
So check that for yourself before and in and maybe use the camera that the rotation setting that's had

47
00:03:33,450 --> 00:03:41,970
an image full name, which is slash home slash by slash camera.

48
00:03:42,000 --> 00:03:51,990
OK, let's actually go in the file manager and see we have the camera folder here already with new image

49
00:03:52,380 --> 00:03:53,370
and new image too.

50
00:03:53,910 --> 00:03:55,440
Well, let's get this like that.

51
00:03:56,580 --> 00:04:02,700
So the folder exists, but I'm just going to make sure it exists just in case, OK?

52
00:04:03,000 --> 00:04:06,630
If you remove it later on and if you try to run this program again.

53
00:04:07,440 --> 00:04:16,680
So it's import voice if voice does not exist.

54
00:04:17,970 --> 00:04:25,970
We've image problem, the name, actually, if it doesn't exist, we do.

55
00:04:26,280 --> 00:04:30,120
I don't think we've.

56
00:04:31,300 --> 00:04:33,400
The shoulder network that's very quick to do.

57
00:04:35,110 --> 00:04:37,900
And now we have the folder and it's the image.

58
00:04:39,430 --> 00:04:48,010
Financing is equal to image folder name plus slush, let's just call it for the GOP.

59
00:04:50,920 --> 00:04:55,930
OK, so every time we're going to take a photo here, we're going to replace the previous one.

60
00:04:56,380 --> 00:05:04,660
Then we need time, but slick to actually maybe if I close the string, can I be better?

61
00:05:04,990 --> 00:05:09,790
And we need the time to slip to to allow the camera to adjust to the luminosity.

62
00:05:10,150 --> 00:05:13,000
And then, well, let's take a photo every two seconds.

63
00:05:13,600 --> 00:05:17,770
Let's divide through its two camera.

64
00:05:18,880 --> 00:05:25,150
Don't capture we image by name.

65
00:05:25,990 --> 00:05:30,100
And when I'm not going to use time slip to here, why?

66
00:05:30,100 --> 00:05:35,710
When I could use that actually just to take your photo every two seconds, but then we are going to

67
00:05:35,710 --> 00:05:37,360
need to read from.

68
00:05:38,290 --> 00:05:40,720
I need to do a non blocking slip.

69
00:05:41,140 --> 00:05:43,030
So I'm going to add here.

70
00:05:44,860 --> 00:05:46,330
Last time.

71
00:05:47,050 --> 00:05:52,600
Photo taken equal to and imports time.

72
00:05:53,240 --> 00:05:54,880
Time to time.

73
00:05:55,210 --> 00:05:56,290
And let's see.

74
00:05:57,490 --> 00:06:00,460
Photo delay is equal to.

75
00:06:02,140 --> 00:06:03,060
Two signals.

76
00:06:03,910 --> 00:06:08,470
And so now what I'm going to do, I'm not doing it at a time to slip through, but I'm still going to

77
00:06:08,470 --> 00:06:12,610
add to the sleep thing of sleep.

78
00:06:13,210 --> 00:06:20,350
Zero one, which means that we are still going to block a bit, but basically just 10 milliseconds,

79
00:06:20,740 --> 00:06:22,550
so we don't use too much sleep.

80
00:06:23,200 --> 00:06:25,660
And that's going to be completely fine for the rest.

81
00:06:26,530 --> 00:06:29,710
And then we do if time don't.

82
00:06:30,970 --> 00:06:36,820
So let's actually create a time now viable time to time.

83
00:06:37,980 --> 00:06:47,940
So if time no, minus lost time, photo taken greater equal than the photo delay hit, you've done that

84
00:06:47,940 --> 00:06:50,100
before, then we do.

85
00:06:50,430 --> 00:06:52,650
Last time a photo taken is equal.

86
00:06:54,700 --> 00:06:58,000
To time now, and we take the.

87
00:06:59,150 --> 00:06:59,840
Or two?

88
00:07:00,590 --> 00:07:00,870
All right.

89
00:07:00,890 --> 00:07:04,490
Let's try just let's just try this part of the code.

90
00:07:04,970 --> 00:07:10,430
Let's run this so we don't have any communication with cell phone or activity.

91
00:07:11,300 --> 00:07:11,720
Nine.

92
00:07:14,390 --> 00:07:15,980
And we don't have anything printed.

93
00:07:16,100 --> 00:07:17,690
Of course, so we don't have any outputs.

94
00:07:18,140 --> 00:07:22,910
But let's go to our folder, he camera.

95
00:07:23,180 --> 00:07:23,960
We have a photo.

96
00:07:25,010 --> 00:07:26,210
That's one photo.

97
00:07:26,540 --> 00:07:30,590
And it's week two segments, and let's click on this.

98
00:07:31,980 --> 00:07:34,730
OK, let's open it.

99
00:07:35,540 --> 00:07:37,370
We have a program here.

100
00:07:37,880 --> 00:07:39,020
Let's just refresh.

101
00:07:40,220 --> 00:07:40,760
OK.

102
00:07:40,790 --> 00:07:42,980
We have another photo and it was taken.

103
00:07:42,980 --> 00:07:43,730
That's different.

104
00:07:43,970 --> 00:07:44,600
Same five.

105
00:07:44,610 --> 00:07:45,770
It has been rewritten.

106
00:07:46,190 --> 00:07:52,850
Maybe you need to just refresh the view undefined manager and then you have the photo.

107
00:07:53,360 --> 00:07:53,690
Great.

108
00:07:53,700 --> 00:07:55,550
So this part is working.

109
00:07:56,180 --> 00:07:59,210
And though what we need to do, we need to send that to sitting around.

110
00:07:59,300 --> 00:08:04,160
So we're going to first use the way that we can requests from three.

111
00:08:04,400 --> 00:08:04,730
OK.

112
00:08:05,870 --> 00:08:08,630
So for that, I'm going to go back to a teacher's aide.

113
00:08:08,930 --> 00:08:11,240
I'm just going to use the code we did before.

114
00:08:11,960 --> 00:08:15,590
So we're going to import data and the comment handler.

115
00:08:19,040 --> 00:08:21,020
We are going to create.

116
00:08:25,350 --> 00:08:31,420
And the data, a dispatcher and then we're going to add some handlers and start pulling.

117
00:08:31,440 --> 00:08:32,910
I'm going to go to all of that.

118
00:08:34,880 --> 00:08:36,020
And where do we put it?

119
00:08:36,620 --> 00:08:42,890
Well, let's just put that after we have initialize the camera and after it painlessly sleep, so we

120
00:08:42,890 --> 00:08:48,880
open the fire with the but then again, but can we create an air of data?

121
00:08:48,890 --> 00:08:52,610
We create the dispatcher and then we have some common handler.

122
00:08:52,640 --> 00:08:53,750
I'm going to remove that.

123
00:08:55,750 --> 00:08:57,220
And I'm just going to put that.

124
00:08:58,330 --> 00:09:01,460
And we want to get a photo.

125
00:09:01,570 --> 00:09:07,340
And I'm just going to put that photo, so we have a stealth handler and a get photo handler.

126
00:09:07,360 --> 00:09:09,220
Let's create those handlers here.

127
00:09:09,730 --> 00:09:13,210
Actually, the stealth handler is going to be the same as before.

128
00:09:13,420 --> 00:09:14,860
Let's just welcome.

129
00:09:19,400 --> 00:09:22,430
And let's create the.

130
00:09:27,240 --> 00:09:32,790
Get a photo handler with complete context.

131
00:09:35,050 --> 00:09:40,870
And so what we need to do is we need to retrieve the photo that it was taken and we need to send it

132
00:09:41,320 --> 00:09:43,800
with, but don't send photo.

133
00:09:44,410 --> 00:09:46,480
So let's do with open.

134
00:09:47,380 --> 00:09:50,380
And that's going to be image file name.

135
00:09:50,800 --> 00:09:56,310
OK, we already have it and we are big eyes.

136
00:09:56,920 --> 00:10:06,160
So let's ask a photo, then we do context not, but don't send photo.

137
00:10:06,730 --> 00:10:07,390
We've checked.

138
00:10:07,750 --> 00:10:09,910
It is equal to.

139
00:10:09,910 --> 00:10:11,230
Let's just reply to the.

140
00:10:12,780 --> 00:10:22,560
Of the effective Chad, any so whoever is triggering the boats and then we don't have the but we have

141
00:10:23,010 --> 00:10:26,760
for photo is equal to four.

142
00:10:27,360 --> 00:10:28,560
All right, this seems OK.

143
00:10:29,100 --> 00:10:34,530
Let's actually had it pretty print camera, OK?

144
00:10:36,790 --> 00:10:45,640
And maybe he print sending photos to Telegram.

145
00:10:48,780 --> 00:10:55,350
And one other thing is we need to stop the data, so I'm going to try here.

146
00:10:58,380 --> 00:11:00,660
With the keyboard interrupt exception.

147
00:11:03,130 --> 00:11:05,170
Except keyboard.

148
00:11:07,980 --> 00:11:08,670
Interrupt.

149
00:11:11,300 --> 00:11:24,560
And we do that through Prince stopping kg of data and a data, not stock.

150
00:11:25,250 --> 00:11:26,480
OK, let's try this.

151
00:11:26,930 --> 00:11:28,050
Let's try this.

152
00:11:28,190 --> 00:11:28,910
I'm going to run.

153
00:11:32,220 --> 00:11:33,090
We have camera.

154
00:11:33,120 --> 00:11:33,730
OK.

155
00:11:33,930 --> 00:11:35,970
So it's going to take photo every two seconds.

156
00:11:36,600 --> 00:11:42,570
And it's going from the new slush get photo.

157
00:11:43,930 --> 00:11:45,820
Sending for the Telegram, you can see here.

158
00:11:46,840 --> 00:11:52,840
And we received the product so may take some time depends on your internet connection speed also and

159
00:11:53,200 --> 00:11:57,440
where different things, but you can see we have the freedom to start.

160
00:11:57,460 --> 00:12:02,350
Also, I have to start message Welcome, OK.

161
00:12:02,740 --> 00:12:09,670
If I do get photo again, so you can see here we have an error.

162
00:12:09,700 --> 00:12:14,950
Well, because probably we are just requesting the photo when it has been updated.

163
00:12:15,730 --> 00:12:16,900
So let's try again.

164
00:12:22,830 --> 00:12:25,710
OK, and now it's working with a different photo.

165
00:12:27,220 --> 00:12:33,910
And so when you can see it's walking, maybe an improvement could be that you make sure that the file

166
00:12:33,910 --> 00:12:39,250
can be opened because, well, if you actually take a photo and a data file and try to send the file

167
00:12:39,250 --> 00:12:40,840
at the same time, that's not going to work.

168
00:12:41,200 --> 00:12:46,420
So that could be an improvement you could do or maybe try to use a different file name for each photo.

169
00:12:46,940 --> 00:12:50,500
Just leave that up to you as an improvement of this activity.

170
00:12:50,950 --> 00:12:56,320
And then when we still need to do something else here is that when we have pressed on the button, we

171
00:12:56,320 --> 00:12:57,700
need to send a photo as well.

172
00:12:58,420 --> 00:13:01,390
So I'm going to initialize the sale communication.

173
00:13:02,320 --> 00:13:09,790
And I'm going to just take from actually eight, which is going to take this code, and let's put it.

174
00:13:12,170 --> 00:13:13,580
So we initialize the camera.

175
00:13:14,910 --> 00:13:16,410
Let's just.

176
00:13:18,030 --> 00:13:19,830
But the Salkeld here.

177
00:13:20,430 --> 00:13:25,260
So first, we connect to scale and then we're going to put that.

178
00:13:27,790 --> 00:13:33,820
He may be after the camera, so we initially say when you shut the camera and then we give some time

179
00:13:34,240 --> 00:13:40,540
for both to be said and he, I don't need to do a sleep two and three, there's going to be five and

180
00:13:40,540 --> 00:13:43,090
just keep three for both of them.

181
00:13:43,300 --> 00:13:45,430
That's going to be OK and then just bring it.

182
00:13:47,260 --> 00:13:49,910
Camera, OK, you say OK here.

183
00:13:50,680 --> 00:13:52,540
And I raise it the inputs buffer.

184
00:13:53,110 --> 00:13:57,040
OK, so everything is going, OK, you said the first sale then?

185
00:13:58,560 --> 00:14:10,560
Camera and I am going to before I forget, I'm going to close you print, closing celluloid and I'm

186
00:14:10,560 --> 00:14:14,760
going to send it close, so we don't forget.

187
00:14:15,750 --> 00:14:19,040
And I'm going to read key from sales.

188
00:14:19,070 --> 00:14:26,880
So we have this action, which is to take a photo and I'm going to add another action.

189
00:14:27,540 --> 00:14:28,770
It can be after or before.

190
00:14:28,770 --> 00:14:29,520
It doesn't matter.

191
00:14:30,720 --> 00:14:32,340
Read from site.

192
00:14:33,130 --> 00:14:46,080
So if sick note in waiting is greater than zero, we do miss is equal to say don't read liner notes

193
00:14:46,470 --> 00:14:47,070
decode.

194
00:14:48,830 --> 00:14:51,530
UTF eight.

195
00:14:52,430 --> 00:14:53,660
And asked trick.

196
00:14:56,210 --> 00:15:01,580
And then we check if this siege is equal to button.

197
00:15:01,850 --> 00:15:04,180
Let's check this again button priced.

198
00:15:09,750 --> 00:15:16,860
Maybe this is button pressed, what we do is we send the message so to send a message to Tehran, so

199
00:15:16,860 --> 00:15:21,030
we send the photo actually to send the photo to Telegram, we need to add.

200
00:15:21,180 --> 00:15:29,130
But so I'm going to add from Telegram import, but object.

201
00:15:29,970 --> 00:15:33,540
And let's go where we initialize Telegram.

202
00:15:33,540 --> 00:15:42,780
Here we have a data I'm going to create but is equal to, but with the token with the same token.

203
00:15:45,190 --> 00:15:47,650
We have both a boat and a daytime.

204
00:15:47,950 --> 00:15:55,920
Now we can use this boat to do but not send photo chat aid.

205
00:15:56,170 --> 00:15:57,790
So what is the tragedy here?

206
00:15:57,970 --> 00:15:59,470
We don't respond.

207
00:16:00,440 --> 00:16:01,810
We don't respond.

208
00:16:04,320 --> 00:16:10,200
To a middle age where we have updates, we've the effective chart I.D. So we need to know what is the

209
00:16:10,210 --> 00:16:12,240
strategy of where we want to send.

210
00:16:13,170 --> 00:16:15,970
And so I'm going to just use the chat I.D..

211
00:16:17,810 --> 00:16:19,420
That it was human activity seven.

212
00:16:20,540 --> 00:16:23,600
I am just going to use the one that we found previously.

213
00:16:25,580 --> 00:16:29,630
So let's put the truck 80.

214
00:16:33,010 --> 00:16:36,410
And so I do chat is equal to chat, Heidi.

215
00:16:37,540 --> 00:16:40,570
And then when I need to also open the photo.

216
00:16:42,900 --> 00:16:44,960
I'm going to do this.

217
00:16:47,310 --> 00:16:48,660
Actually, this.

218
00:16:50,210 --> 00:16:51,680
Some ground to weave.

219
00:16:53,220 --> 00:16:54,950
That's correct, indentation.

220
00:16:56,280 --> 00:17:03,650
So when the button is priced, we opened image file name as a photo and then we send photo is equal

221
00:17:03,660 --> 00:17:06,870
to what we send a photo to the chat ID.

222
00:17:07,350 --> 00:17:16,290
So to the chat, to the group chat the same way we send it when we request we to get photo comment.

223
00:17:17,370 --> 00:17:19,410
So no, let's run that code again.

224
00:17:23,420 --> 00:17:24,950
OK, we have an error here.

225
00:17:25,700 --> 00:17:30,650
Sale is not defined here at the beginning.

226
00:17:35,090 --> 00:17:41,480
Well, actually, this is the point of when you take some quotes from all the programs that maybe you

227
00:17:41,900 --> 00:17:46,700
forget to take everything so input, you say that's going to be better like this.

228
00:17:50,030 --> 00:18:01,040
OK, we're not going to say what, because actually, I have to put one, because sure, remember here

229
00:18:01,130 --> 00:18:01,610
I have.

230
00:18:02,060 --> 00:18:03,000
Did you wait a year?

231
00:18:03,230 --> 00:18:07,100
So it's important you check the sale before I'm going to use.

232
00:18:07,100 --> 00:18:09,500
Did you write ACM one here?

233
00:18:10,670 --> 00:18:16,010
Run the script successfully connected to cell camera, OK, cell.

234
00:18:16,040 --> 00:18:16,670
OK.

235
00:18:17,510 --> 00:18:19,880
So it's taking a photo every two seconds.

236
00:18:21,080 --> 00:18:26,150
Up they run up and this Bryce on the push button.

237
00:18:28,010 --> 00:18:29,600
Sending photo to Tehran.

238
00:18:30,950 --> 00:18:32,990
And you can see we receive a new photo.

239
00:18:33,230 --> 00:18:35,930
Well, that is me pressing on the president.

240
00:18:36,470 --> 00:18:41,450
And if I do get photo, I can also get a photo.

241
00:18:41,630 --> 00:18:46,040
So here we can see that this is not the right timing.

242
00:18:46,070 --> 00:18:50,000
Let's try again and we get a new photo.

243
00:18:50,570 --> 00:18:50,900
All right.

244
00:18:50,910 --> 00:18:53,510
So in this program, you have mixed.

245
00:18:53,990 --> 00:19:00,290
So on the Python program, the Raspberry Pi, you have used cellular communication with the camera,

246
00:19:00,950 --> 00:19:07,070
with the Telegram box, and now you can mix Raspberry Pi functionalities and Arduino functionalities

247
00:19:07,370 --> 00:19:08,900
in a more complex program.

248
00:19:09,410 --> 00:19:14,060
And this is perfect because we are just about to start the final project of this course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: PART 4 - Complete Intercom System (Final Project)

1
00:00:00,180 --> 00:00:03,540
It's now time to start the final project of these goods.

2
00:00:03,900 --> 00:00:09,360
You have now completed all the learning steps and have a great knowledge foundation you can use for

3
00:00:09,360 --> 00:00:13,290
any new project, including the one we are about to do right now.

4
00:00:13,770 --> 00:00:18,330
This project will be great for you to practice on everything you have seen in this course.

5
00:00:18,750 --> 00:00:20,610
So what is this project about?

6
00:00:20,850 --> 00:00:23,820
We will create a complete intercom system.

7
00:00:24,150 --> 00:00:26,520
Here is the result you will get at the end.

8
00:00:27,390 --> 00:00:31,440
So this is the complete secret, including the outer snow and the raspberry.

9
00:00:31,440 --> 00:00:35,850
But here it you can see with all the components and the functionalities in the class.

10
00:00:36,180 --> 00:00:42,000
So if the energy would be blue and the intercom and we have a message push on the button to call.

11
00:00:42,270 --> 00:00:50,640
So I'm going to push the button to call and this is going to send a message to the Raspberry Pi and

12
00:00:50,640 --> 00:00:55,200
you can see that we receive a message here on the Telegram chat.

13
00:00:55,770 --> 00:00:59,670
So if you have installed Telegram on your phone, you will receive a notification.

14
00:00:59,970 --> 00:01:04,680
Someone is ringing the bell and then you can send open are denied and will.

15
00:01:05,100 --> 00:01:09,090
This gentleman looks very nice, so I'm going to just open the door for him.

16
00:01:09,630 --> 00:01:15,600
OK, so I click on open and this is going to send back the message to the Arduino from the Raspberry

17
00:01:15,600 --> 00:01:15,930
Pi.

18
00:01:16,830 --> 00:01:17,840
The door is opened.

19
00:01:17,850 --> 00:01:23,670
We have the green energy and you can see the seven has moved to open the door after 10 seconds.

20
00:01:25,930 --> 00:01:30,590
We come back to the initial state, OK, we've the blue energy and push on the button to call.

21
00:01:31,720 --> 00:01:32,950
Now I'm going to call again.

22
00:01:34,570 --> 00:01:36,100
This is going to send another photo.

23
00:01:36,640 --> 00:01:42,580
So this is going to send another notification to the diagram up and went, Who is this guy?

24
00:01:42,670 --> 00:01:43,900
I don't even see his face.

25
00:01:44,530 --> 00:01:46,030
I'm not going to open the door for him.

26
00:01:46,270 --> 00:01:47,620
I'm going to deny him.

27
00:01:49,750 --> 00:01:55,480
OK, and when it's denied, you have another different song, the right energy and then you have access

28
00:01:55,480 --> 00:02:01,600
denied for five seconds and then it comes back to normal and you can call again to ask to open the door.

29
00:02:02,110 --> 00:02:06,130
And so here is a quick overview of what we have in the hallway it.

30
00:02:06,130 --> 00:02:10,050
But so we have the Raspberry Pi first with the Raspberry Pi camera.

31
00:02:10,340 --> 00:02:16,600
This Raspberry Pi would be responsible to control the global logic of the application and will also

32
00:02:16,600 --> 00:02:18,010
interact with the Telegram.

33
00:02:18,010 --> 00:02:24,160
But OK, so it can send some notification to your phone or your computer, and it can also receive some

34
00:02:24,160 --> 00:02:26,410
commands for open or deny.

35
00:02:27,160 --> 00:02:28,600
Then we have the Arduino.

36
00:02:28,990 --> 00:02:32,710
The Arduino will be responsible for basically all the hardware components.

37
00:02:33,130 --> 00:02:34,500
It will open and close the door.

38
00:02:34,510 --> 00:02:34,750
We do.

39
00:02:34,750 --> 00:02:37,810
Seven model came to a quick bar into this here.

40
00:02:38,080 --> 00:02:42,940
The seven model I directed pull out it from the Aminul and it is not mounted on any door.

41
00:02:42,950 --> 00:02:48,760
So what you could improve is to externally pull it and mounted on a real door mechanism.

42
00:02:49,540 --> 00:02:56,620
So then we have an entity, a buzzer, OK, to make some light and some sound when we open close are

43
00:02:56,950 --> 00:02:57,790
denied access.

44
00:02:57,790 --> 00:03:06,220
For example, we have an LCD also to give some instruction to the user and a push button so we can make

45
00:03:06,220 --> 00:03:07,990
the call for the intercom.

46
00:03:08,320 --> 00:03:11,290
And so everything you see here is going to be controlled by the outer ring.

47
00:03:11,440 --> 00:03:15,310
But the command, the main command is going to come from the Raspberry Pi.

48
00:03:15,580 --> 00:03:21,070
And when you press on the button, the algorithm reiterated, but would send it to the Raspberry Pi

49
00:03:21,400 --> 00:03:26,290
and then the Raspberry Pi will communicate with the three remote and then coming back to the Raspberry

50
00:03:26,290 --> 00:03:28,120
Pi and coming back to the algorithm.

51
00:03:29,100 --> 00:03:35,370
This project is a very good example of how to use both Raspberry Bay and Island, we know in one single

52
00:03:35,370 --> 00:03:36,060
application.

53
00:03:36,450 --> 00:03:42,720
Some of the functionalities are only possible with Raspberry Pi and others only possible with Arduino

54
00:03:43,050 --> 00:03:44,790
by using the combination of both.

55
00:03:45,030 --> 00:03:51,280
You can build a more complex project with Raspberry Pi as the brain and Arduino as the muscles.

56
00:03:51,720 --> 00:03:57,390
You can also download a PDF for the project as an additional Russa's, which contains all the specs

57
00:03:57,660 --> 00:04:03,180
and all the functionalities you have to implement, as well as an overview of the steps you can take

58
00:04:03,180 --> 00:04:04,410
to finish the project.

59
00:04:04,950 --> 00:04:08,790
I got all the instructions in this PDF, so it's going to be easier for you.

60
00:04:09,090 --> 00:04:15,480
You can just download the PDF, read as many times as you want and keep it on the side when you work

61
00:04:15,540 --> 00:04:16,440
on the project.

62
00:04:17,130 --> 00:04:20,850
This project is a bit challenging, but this is the way to progress.

63
00:04:21,210 --> 00:04:25,020
I didn't want to create something super easy just to make you feel good.

64
00:04:25,320 --> 00:04:30,060
You will need to use your brain at full capacity here, but this is totally doable.

65
00:04:30,210 --> 00:04:35,790
If you have correctly understood what we have done so far and I can guarantee you that when you finish

66
00:04:35,800 --> 00:04:39,330
the project, you will have a great feeling of achievement.

67
00:04:39,690 --> 00:04:44,610
And not only that, but you will be ready to start your next project with confidence.

68
00:04:45,210 --> 00:04:47,940
So make sure you take some time to work on the project.

69
00:04:48,300 --> 00:04:51,150
Also, try to design the steps by yourself.

70
00:04:51,540 --> 00:04:55,790
Think about what you need to do first and how to get to the final result.

71
00:04:55,830 --> 00:05:02,850
One step at a time your step design may be different than mine, and that's totally fine if it makes

72
00:05:02,850 --> 00:05:06,120
sense and if it allows you to finish the project.

73
00:05:06,720 --> 00:05:11,970
Now, don't stay stuck for weeks if you really don't find a solution to the next step.

74
00:05:12,240 --> 00:05:15,810
Then watch the step solution and don't feel bad about this.

75
00:05:16,200 --> 00:05:22,530
So you want you to step in on this one and then you continue to work on the project a few days later.

76
00:05:22,710 --> 00:05:24,960
Come back to this step and try to do it again.

77
00:05:25,680 --> 00:05:30,420
You can also come back to watch any previous listener activity on the course.

78
00:05:30,660 --> 00:05:38,100
If you have some doubt, or if you need some clarification on a specific point, the solution I provide

79
00:05:38,100 --> 00:05:44,550
next is a complete step-by-step solution where I explain everything and give you some additional tips

80
00:05:44,550 --> 00:05:47,400
and best practices for your future project.

81
00:05:47,820 --> 00:05:51,870
For each step, you can also download the project code until that stick.

82
00:05:52,260 --> 00:05:58,110
Note that this solution will probably not be identical to the one you will have, but please note that

83
00:05:58,110 --> 00:06:00,480
this is just one solution.

84
00:06:00,720 --> 00:06:03,240
It is not necessarily the solution.

85
00:06:03,510 --> 00:06:07,170
If you get the same result with a different code, then it's OK.

86
00:06:07,200 --> 00:06:07,500
Two.

87
00:06:08,010 --> 00:06:13,590
All right now, download the instructions VIDEO And let's get started with this intercom project.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:06,750
This is the first step of the final project where we build a complete intercom system, and for this

2
00:00:06,750 --> 00:00:09,840
step, well, we are not going to write any code.

3
00:00:10,110 --> 00:00:16,290
We are going to define the protocol that we will use to communicate between the Arduino and the Raspberry

4
00:00:16,290 --> 00:00:20,050
Pi and also between the Raspberry Pi and the Telegram application.

5
00:00:20,070 --> 00:00:20,400
OK.

6
00:00:20,580 --> 00:00:26,610
Because when you communicate between both sides, you need to agree on what you send and what you'll

7
00:00:26,610 --> 00:00:27,060
receive.

8
00:00:27,090 --> 00:00:30,660
So you can correctly process the comments and the messages.

9
00:00:31,020 --> 00:00:32,670
So I'm just going to open.

10
00:00:33,000 --> 00:00:37,980
Well, just want to open June here just to write some text.

11
00:00:39,990 --> 00:00:45,960
So once you can do what they recommend is just right and the protocol on paper first can just a pen

12
00:00:45,960 --> 00:00:46,700
and paper.

13
00:00:46,710 --> 00:00:47,880
That's it all.

14
00:00:48,120 --> 00:00:55,230
Just open any text editor you want on the Raspberry Pi, all on your phone, on windows went basically

15
00:00:55,230 --> 00:00:56,370
anywhere you want to get.

16
00:00:56,370 --> 00:00:57,300
It doesn't really matter.

17
00:00:57,420 --> 00:01:03,210
It's just the kind of protocol that then you keep on the side for the duration of the project.

18
00:01:03,720 --> 00:01:08,310
So first of all, we're going to focus on cellular communication.

19
00:01:10,700 --> 00:01:12,150
We're not getting full size.

20
00:01:12,170 --> 00:01:12,560
OK.

21
00:01:13,520 --> 00:01:18,350
And then on Telegram communication.

22
00:01:21,860 --> 00:01:25,850
So what do we need for sale, so basically between the Arduino and the Raspberry Pi?

23
00:01:26,630 --> 00:01:31,550
First, let's do the comments that are going to go from adeno to Raspberry Pi.

24
00:01:31,560 --> 00:01:32,980
I'm going to write up.

25
00:01:33,080 --> 00:01:33,860
I like this.

26
00:01:34,430 --> 00:01:35,210
What do we have?

27
00:01:35,240 --> 00:01:37,130
Well, we have just one.

28
00:01:37,130 --> 00:01:42,140
Outputs we want to send is when we press on the push button and when we pressing the president, then

29
00:01:42,140 --> 00:01:49,940
we can send a comment, for example, button priced with backslash saying, OK, I'm going to add backslash

30
00:01:49,940 --> 00:01:50,510
in here.

31
00:01:50,930 --> 00:01:53,030
So that document is complete.

32
00:01:53,840 --> 00:01:55,190
So we send this.

33
00:01:55,190 --> 00:01:58,640
So we've already done that actually in some of the previous activities.

34
00:01:58,910 --> 00:02:00,380
We send these from the outer know.

35
00:02:00,380 --> 00:02:02,810
We will receive that on the Raspberry Pi, then that's it.

36
00:02:02,810 --> 00:02:08,690
For this side of the communication, we have named RPI to the audio here.

37
00:02:08,690 --> 00:02:09,920
We have a few more comments.

38
00:02:10,010 --> 00:02:17,600
So we are going to control the algebra, the buzzer, the 7.0 end LCD screen from the Raspberry Pi.

39
00:02:17,870 --> 00:02:20,810
And so what commands exactly are we going to send?

40
00:02:21,200 --> 00:02:23,750
Let's first think about the seven model.

41
00:02:24,080 --> 00:02:30,260
So basically, the comment we want to do is not to move to seven wutah in a at a high level is not to

42
00:02:30,260 --> 00:02:35,750
open the door to close the door because this is an intercom project when the settlement always linked

43
00:02:35,750 --> 00:02:36,320
to the door.

44
00:02:37,130 --> 00:02:41,270
So what I'm going to do is I'm going to send a comment open door.

45
00:02:42,530 --> 00:02:51,080
Baxter and closed don't backslash, and the Arduino would be responsible for moving the cable to the

46
00:02:51,080 --> 00:02:59,000
correct position when it receives Open-door and moving the cell to the closed position when it receives

47
00:02:59,000 --> 00:03:00,470
the closed door comment.

48
00:03:00,700 --> 00:03:05,900
OK, I could send directly the angle of the cell to the original, but with actually this way may be

49
00:03:05,900 --> 00:03:06,270
better.

50
00:03:06,290 --> 00:03:11,450
OK, we sent, opened or closed door and the Arduino knows because they are no closer to hardware.

51
00:03:11,660 --> 00:03:17,960
The Arduino knows what is the angle to send a cell to, what is the speed to move, assemble, etc.

52
00:03:18,140 --> 00:03:19,070
OK, so we are done.

53
00:03:19,070 --> 00:03:22,340
We've done several and we've the open and closed door functionalities.

54
00:03:22,910 --> 00:03:27,920
Then when we open and we close the door, we also want to set the Ogilvie Energy, the buzzer.

55
00:03:27,920 --> 00:03:30,460
And so let's start with LCD.

56
00:03:30,470 --> 00:03:40,030
We are going to send Prince text column and then it said this is some text backslash.

57
00:03:40,040 --> 00:03:44,630
And so we have already done that before we send the print text command.

58
00:03:44,660 --> 00:03:49,760
We call on and then we're going to extract this from the command.

59
00:03:50,270 --> 00:03:54,800
So this is the exact command we are going to check if it's equal to a bundle.

60
00:03:55,070 --> 00:04:00,950
Here we going to check in the comments that we've printed text and then extract this and print this

61
00:04:00,950 --> 00:04:02,150
on the screen.

62
00:04:02,480 --> 00:04:03,620
No, for the buzzer.

63
00:04:03,850 --> 00:04:09,380
We haven't used the buzzer in any activity before, so that's something new.

64
00:04:09,740 --> 00:04:12,500
What can we do to send comment to the buzzer?

65
00:04:12,500 --> 00:04:19,370
So we want to play a sound and the buzzer and to play a sound, we need to give two things the frequency

66
00:04:19,730 --> 00:04:21,110
and the duration.

67
00:04:21,470 --> 00:04:29,780
And so I'm going to put equipment at see play, buzzer column and then frequency.

68
00:04:32,130 --> 00:04:35,130
Coma, duration, backslash, pain.

69
00:04:35,550 --> 00:04:40,920
So, Eleanor, we're going to first check that we have a command that starts with Playbuzz, a colon,

70
00:04:41,430 --> 00:04:48,750
and then we're going to extract this and we're going to find index of the coma and then everything before

71
00:04:48,750 --> 00:04:49,950
the index of the frequency.

72
00:04:49,950 --> 00:04:52,170
Everything after the index is the duration.

73
00:04:52,440 --> 00:04:58,770
OK, so the frequency can be anything from, let's say, 20 to 20000 hits and a duration also can be

74
00:04:58,770 --> 00:05:02,700
anything from one millisecond to whatever milliseconds you want.

75
00:05:03,030 --> 00:05:08,060
And then we have set energy because we want to set the odds of the enemy.

76
00:05:08,480 --> 00:05:15,020
We've all red, green and blue backslash.

77
00:05:15,030 --> 00:05:21,540
And and so here we are going to follow the protocol we have used previously in one of the other activity,

78
00:05:21,780 --> 00:05:25,860
which is to say that each color will be exactly three characters.

79
00:05:26,130 --> 00:05:38,280
So as an example, we have set any let's say you want to give three for the right and then 255 for the

80
00:05:38,280 --> 00:05:42,840
green and then zero 50 for the blue.

81
00:05:43,530 --> 00:05:48,510
You're going to make sure that each coral gets three characters.

82
00:05:49,320 --> 00:05:57,180
OK, let's just actually do an example for the play buzzer the buzzer, let's say, for example, two,

83
00:05:57,180 --> 00:06:04,320
100 and 1000 to 100 frequency, 1000 milliseconds.

84
00:06:04,770 --> 00:06:09,760
And so we're going to handle actually those two commands a bit differently in the code in the outing

85
00:06:09,760 --> 00:06:10,140
of code.

86
00:06:10,590 --> 00:06:18,210
So we have covered all the functionalities here and all the components between the Arduino and the Raspberry

87
00:06:18,210 --> 00:06:18,400
Pi.

88
00:06:18,900 --> 00:06:20,550
So we're going to keep this on the site.

89
00:06:21,270 --> 00:06:26,130
So when we work on the Arduino, we know what to send and what to receive.

90
00:06:26,460 --> 00:06:32,220
And when we work on the Raspberry Pi, we know what to receive and what to send if we don't need to

91
00:06:32,220 --> 00:06:34,080
always compare the two codes.

92
00:06:34,350 --> 00:06:40,010
We can just refer to this document and then we also need to define what's coming.

93
00:06:40,020 --> 00:06:43,830
We are going to send and receive from Telegram so well.

94
00:06:43,850 --> 00:06:48,300
When we actually send a notification, we have a message and a photo.

95
00:06:48,690 --> 00:06:55,290
There is no specific command to agree on because we're just going to send a message on a chat using

96
00:06:55,290 --> 00:06:55,740
the chat.

97
00:06:56,820 --> 00:07:01,050
But when we receive command, we need to check what command we receive so we can process.

98
00:07:01,050 --> 00:07:07,470
Then we have a handler in the Python code, and so we're going to have to start going as always and

99
00:07:07,470 --> 00:07:08,430
then to open the door.

100
00:07:08,460 --> 00:07:14,910
We're going to use open like you can see in the demo, and to close the door actually to deny access,

101
00:07:14,910 --> 00:07:18,260
not to close the door, but to deny access, just deny.

102
00:07:19,080 --> 00:07:25,500
So we start, we can get a welcome message when we receive a notification, we can send open to open

103
00:07:25,500 --> 00:07:25,950
the door.

104
00:07:26,400 --> 00:07:29,040
All we can send denied to deny access.

105
00:07:29,520 --> 00:07:32,580
And well, that's pretty much it.

106
00:07:33,530 --> 00:07:42,270
So I'm going to say control as this as protocol, that's OK.

107
00:07:42,650 --> 00:07:45,470
And keep it under state for the duration of the project.

108
00:07:45,740 --> 00:07:50,540
And now that we have this, we are ready to start writing some code.

109
00:07:50,690 --> 00:07:51,920
We have the next step.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:07,320
This is the two of the final project of the intercom system and this that we are going to start to write

2
00:00:07,360 --> 00:00:08,640
the Arduino code.

3
00:00:09,030 --> 00:00:15,240
I'm going to write out including three steps first to initialize all the components and then to focus

4
00:00:15,240 --> 00:00:16,300
on the output.

5
00:00:16,320 --> 00:00:23,640
So what we send from the Arduino to the Raspberry Pi and a third step would be to focus on the input

6
00:00:23,640 --> 00:00:24,060
command.

7
00:00:24,070 --> 00:00:29,640
So basically what to receive from the Raspberry Pi and apply those commands to the hardware we have

8
00:00:29,640 --> 00:00:33,010
previously initialized and doing it this way?

9
00:00:33,030 --> 00:00:33,430
Why?

10
00:00:33,450 --> 00:00:37,890
Because when we already have all the hardware components plugged to the out, we know on the circuit,

11
00:00:37,890 --> 00:00:40,800
we know it's working because we already have tested them.

12
00:00:41,400 --> 00:00:48,420
And also in this project, where there is no relation between all the components in the original program,

13
00:00:48,870 --> 00:00:56,400
only the Raspberry Pi, we know how to combine them, when to power on the entity, when to give some

14
00:00:56,400 --> 00:01:02,160
text to the screen, when to ask to open the door, etc. But Arduino doesn't know any of that.

15
00:01:02,310 --> 00:01:02,790
I don't know.

16
00:01:02,790 --> 00:01:10,200
Just sends outputs, messages and receives input commands and execute them independently for each component.

17
00:01:10,410 --> 00:01:12,810
So that's why I'm going with this order.

18
00:01:12,990 --> 00:01:20,310
What you could also do in which is also a valid option is to do two steps, so one step for each component.

19
00:01:20,760 --> 00:01:26,040
For example, if you were to start the circuit from scratch, you could either component to the circuit

20
00:01:26,040 --> 00:01:32,550
on the other, you know, this component and add this component into the Arduino program until you have

21
00:01:32,550 --> 00:01:35,760
tested and added all the components one by one.

22
00:01:36,390 --> 00:01:36,790
All right.

23
00:01:36,840 --> 00:01:38,850
So now let's start in here.

24
00:01:38,850 --> 00:01:45,120
In this step, I'm going to just initialize all the components and print something on the LCD screen

25
00:01:45,570 --> 00:01:49,740
like a starting message to just know that we have started the application.

26
00:01:50,280 --> 00:01:56,160
Also for each step I'm going to save, and the project has a different file with the name of the steps

27
00:01:56,160 --> 00:02:00,600
that you can just download each program from each step independently.

28
00:02:01,230 --> 00:02:02,340
All right, let's start.

29
00:02:03,360 --> 00:02:11,100
So first, I'm going to include the libraries we need and so Hajji be the buzzer and the push-button.

30
00:02:11,100 --> 00:02:14,190
We don't need anything, but we need something for the liquid crystal.

31
00:02:15,060 --> 00:02:25,590
So liquid crystal dot age and includes several dot h.

32
00:02:26,490 --> 00:02:28,650
All right, we have all the libraries we need.

33
00:02:28,950 --> 00:02:33,090
And then I am going to do a define for each of the pin.

34
00:02:33,720 --> 00:02:45,000
So rg b, let's start with RGV Red Bean, which has been number 11 and then Ogbe Green Bean, which

35
00:02:45,000 --> 00:02:45,780
is number 10.

36
00:02:46,190 --> 00:02:51,060
OK, in this project here in the solution of this project, I'm going to write all the code from scratch.

37
00:02:52,030 --> 00:02:57,120
Define hijabi blue bean, which is nine.

38
00:02:57,300 --> 00:02:57,630
OK.

39
00:02:57,990 --> 00:03:01,050
We have the algae B. Let's do the buzzer.

40
00:03:01,270 --> 00:03:12,450
Define buzzer bean, which is bean eight and then define Button Bean, which is been seven.

41
00:03:12,690 --> 00:03:16,950
There is no order for this, which is do all the different, then?

42
00:03:16,950 --> 00:03:18,570
Well, let's add the several here.

43
00:03:18,630 --> 00:03:22,640
Define several bean 12.

44
00:03:23,320 --> 00:03:35,070
We have several RGV buzzer button, and then we need a series of NC R s been a four and then define

45
00:03:35,070 --> 00:03:46,230
and c d e bean, which is a five, and we have four more LCD d for PIN, which is number two.

46
00:03:47,340 --> 00:03:50,340
Just copy these three times.

47
00:03:52,030 --> 00:03:56,140
The five, the six, the seven.

48
00:03:57,980 --> 00:04:05,330
And we have two, three, four and five who can make sure you have the correct defiance that's going

49
00:04:05,330 --> 00:04:08,270
to save you a lot of time in the future.

50
00:04:08,900 --> 00:04:14,330
Now let's create the global objects we need for the liquid crystal end-december.

51
00:04:15,050 --> 00:04:21,290
So it's not liquid crystal LCD we need to give.

52
00:04:22,800 --> 00:04:38,580
All those pins in the other office before and then it's the line here with your the five, the six and

53
00:04:39,300 --> 00:04:40,590
the seven.

54
00:04:43,050 --> 00:04:45,390
And let's do also several.

55
00:04:47,250 --> 00:04:52,380
So that's naming several Anthony and several we just have one.

56
00:04:52,740 --> 00:04:56,860
So let's name it, LCD and several, if we had multiple ones, you would give.

57
00:04:56,880 --> 00:04:58,560
Of course, more meaningful names.

58
00:04:58,650 --> 00:04:58,900
OK.

59
00:04:59,490 --> 00:05:03,110
For example, right, dorsal and left dot several.

60
00:05:03,240 --> 00:05:06,540
You know, we're just have one now in the void set up.

61
00:05:06,540 --> 00:05:08,310
So us handle, the voice said.

62
00:05:09,660 --> 00:05:14,700
I'm going to initially say in the next step, OK, because he would just initialize hardware components.

63
00:05:15,100 --> 00:05:19,290
Well, let's start with the seven several that attach.

64
00:05:20,330 --> 00:05:30,290
We've several people what we can also look for on several immediately is to put it in the close position,

65
00:05:30,290 --> 00:05:32,930
so basically to close the door to lock the door.

66
00:05:33,230 --> 00:05:34,370
So we're going to do several.

67
00:05:35,060 --> 00:05:36,230
That's right.

68
00:05:36,500 --> 00:05:42,590
And he went, You can play we've the seven or you can just give different angles and put the plastic

69
00:05:42,590 --> 00:05:46,670
back on it to see which positions are going to shoot your project.

70
00:05:47,690 --> 00:05:53,360
And what you can do is you can create it's creates another two defines you.

71
00:05:54,570 --> 00:06:01,250
Define several open door position.

72
00:06:02,430 --> 00:06:13,470
And let's define several closed door position so that if we have this right now, then when we receive

73
00:06:13,470 --> 00:06:17,610
the command, we can just ask the cell to go to this position.

74
00:06:18,120 --> 00:06:25,590
And for me, I'm going to use 50 and 100 40 degrees.

75
00:06:26,190 --> 00:06:28,770
We are not going to go from zero to 180 here.

76
00:06:29,340 --> 00:06:34,590
I have just put two values in the middle and you can see the difference here is 90 degrees.

77
00:06:35,190 --> 00:06:41,770
And so this is the position where the plastic parts that I've put on my subway is going to be straight.

78
00:06:42,240 --> 00:06:49,410
So the door is not locked and here we rotate it by 90 degrees to close the door.

79
00:06:49,680 --> 00:06:50,010
OK.

80
00:06:50,340 --> 00:06:54,890
A quick tip I recommend if you use a hobby seven motto don't go to the extreme.

81
00:06:55,110 --> 00:06:56,370
Don't go close to zero.

82
00:06:56,640 --> 00:06:59,400
And don't go close to 180.

83
00:06:59,940 --> 00:07:01,670
Try to stay somewhere in the middle.

84
00:07:01,770 --> 00:07:02,070
OK.

85
00:07:02,280 --> 00:07:03,660
You can make your own experiment.

86
00:07:03,660 --> 00:07:06,240
You can use those values to continue with the project.

87
00:07:06,240 --> 00:07:11,310
But if you installed a cell on a real note, then you might just experiment and choose different things.

88
00:07:11,760 --> 00:07:17,010
All right, so I'm going to first write the several closed door position.

89
00:07:17,550 --> 00:07:20,270
OK, we don't want the door to be open by default.

90
00:07:20,280 --> 00:07:22,740
We want the door to be closed by default.

91
00:07:23,940 --> 00:07:26,220
So we have the civil initialized.

92
00:07:26,880 --> 00:07:36,840
Now let's initialize the budget button, for example, which mode button, pin input and then pin mode

93
00:07:37,260 --> 00:07:41,330
buzzer pin output.

94
00:07:42,360 --> 00:07:44,700
Let's do the RGV editing mode.

95
00:07:45,450 --> 00:07:54,360
We've Ogbe right the output, and let's do also the two other legs.

96
00:07:56,890 --> 00:08:00,970
So we have green and we have blue.

97
00:08:02,470 --> 00:08:04,930
And then we are left with the inside.

98
00:08:06,850 --> 00:08:08,880
Screens for LCD don't begin.

99
00:08:09,940 --> 00:08:11,140
16 by two.

100
00:08:11,950 --> 00:08:15,670
And we're going to bring a welcome message, I'll just starting.

101
00:08:15,820 --> 00:08:21,130
LCD dot print starting like this?

102
00:08:22,310 --> 00:08:28,940
And what I'm going to do is I'm going to add just a delay here worth 1000 milliseconds, so just one

103
00:08:28,940 --> 00:08:31,660
thing and then instead, you know it cleanup.

104
00:08:32,390 --> 00:08:37,280
So this are usually do in my ordinary applications when I have an LCD is bring something like stunting

105
00:08:37,280 --> 00:08:43,730
for one second two seconds, something like that and then clear the screen so that we know when the

106
00:08:43,730 --> 00:08:47,060
prime is studying and we know what we get when we enter the void loop.

107
00:08:47,420 --> 00:08:49,820
And that's always a nice message to print for the user.

108
00:08:50,150 --> 00:08:50,600
All right.

109
00:08:50,630 --> 00:08:52,550
No, that we have all of that.

110
00:08:52,880 --> 00:08:56,090
Let's try and explore the code here.

111
00:08:56,120 --> 00:08:58,820
So we should have the several that goes to the closed position.

112
00:08:59,150 --> 00:09:02,420
We should have also starting printing on the LCD screen.

113
00:09:02,690 --> 00:09:03,740
So I'm going to applaud.

114
00:09:03,740 --> 00:09:07,610
Let's make sure the board is here and upload.

115
00:09:07,850 --> 00:09:08,810
Let's name it.

116
00:09:10,280 --> 00:09:16,490
Intercom step to create a step one was to define the protocol.

117
00:09:17,660 --> 00:09:21,320
Compiling and then uploading.

118
00:09:23,410 --> 00:09:30,070
Starting, you can see we had starting and will do several is in the closed position, it was already

119
00:09:30,070 --> 00:09:37,690
here, so it didn't move, but you can see the closed position is that the the lock mechanism would

120
00:09:37,690 --> 00:09:47,340
be like this and the open position, the lock mechanism would be up like this, closed and open, OK,

121
00:09:47,350 --> 00:09:52,390
and we have just finished to step two of the products or not the most interesting one, of course,

122
00:09:52,390 --> 00:09:53,860
but a necessary one.

123
00:09:54,100 --> 00:09:59,440
So then we can focus on the application because we have everything correctly initialized.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,180 --> 00:00:04,860
This is step number three on the final product of the intercom system.

2
00:00:05,340 --> 00:00:11,230
And now that we have initialized all of the hardware components on the Arduino, we're going to write

3
00:00:11,230 --> 00:00:17,910
the code so we can send the output messages to the Raspberry Pi when we have something that happens

4
00:00:17,910 --> 00:00:18,570
with the hardware.

5
00:00:18,750 --> 00:00:23,010
So I'm already here, we have just the button code to write.

6
00:00:23,430 --> 00:00:28,590
And so first of all, I'm going to save this as intercom.

7
00:00:28,590 --> 00:00:29,400
Step three.

8
00:00:29,820 --> 00:00:31,900
OK, OK, it's safe.

9
00:00:32,970 --> 00:00:36,570
And let's actually open again the protocol that we have written here.

10
00:00:36,960 --> 00:00:38,480
So for me, right?

11
00:00:38,490 --> 00:00:38,900
And.

12
00:00:40,610 --> 00:00:46,820
So we can see here from Arduino to Raspberry Pi, we just have the button priced command to send it

13
00:00:46,820 --> 00:00:47,280
back to us.

14
00:00:47,300 --> 00:00:49,370
And so that's what we are going to do.

15
00:00:51,750 --> 00:00:56,070
And so, well, this we have already done that before, but I'm still going to do it again.

16
00:00:56,480 --> 00:01:01,790
And right there is to read from the push-button button and detects when we have pressed on the measurement.

17
00:01:02,550 --> 00:01:06,840
So I'm going to create two or three new variables here.

18
00:01:07,350 --> 00:01:10,630
Let's do that right there as the global variables.

19
00:01:11,250 --> 00:01:21,750
So unsigned long last time button changed with the to merely are zero doesn't matter and unsigned,

20
00:01:22,470 --> 00:01:26,190
long rebounds delay.

21
00:01:26,190 --> 00:01:29,790
Let's put 15 milliseconds you can adjust.

22
00:01:29,790 --> 00:01:33,150
That's a bit more a bit less, depending on how it works with your circuit.

23
00:01:33,930 --> 00:01:36,240
So this is going to be for the debunked mechanism.

24
00:01:36,870 --> 00:01:46,260
And then I'm going to also add based on previous button state and the previous button state, I initialize

25
00:01:46,260 --> 00:01:46,980
it here.

26
00:01:47,790 --> 00:01:52,080
Previous button states is equal to digital.

27
00:01:53,190 --> 00:01:54,930
Read from the button.

28
00:01:56,580 --> 00:02:04,350
And of course, I do that after I have put the bin mode with button input now into void look.

29
00:02:06,400 --> 00:02:12,400
So in the void, look, we can reach from the pleasure button, but before we read from verbatim, we're

30
00:02:12,400 --> 00:02:15,910
going to do the the bounce mechanism to be sure we can read from the belly button.

31
00:02:15,920 --> 00:02:21,490
So unsigned long time now is equal to me.

32
00:02:21,490 --> 00:02:26,950
So we get the time every every time we enter the void loop, which is going to be right at first.

33
00:02:28,270 --> 00:02:37,150
If so, if the current time came not minus the last time the button state has change here is greater

34
00:02:37,150 --> 00:02:41,140
or equal, then the debone delay.

35
00:02:43,170 --> 00:02:49,590
So if we have spent enough time since the button has changed for the last time, then we can read the

36
00:02:49,590 --> 00:03:02,490
bill state so might, but state is equal to digital red button been and then we can compare the button

37
00:03:02,490 --> 00:03:06,030
state sort of current when we read from the previous one.

38
00:03:06,300 --> 00:03:13,740
So from previous button state, if those are different, then we have either priced or released the

39
00:03:13,740 --> 00:03:14,220
button.

40
00:03:14,580 --> 00:03:18,690
And in that case, first we can beat this.

41
00:03:19,440 --> 00:03:22,080
So the last time the button has changed is actually no.

42
00:03:22,350 --> 00:03:23,670
So we put the time now.

43
00:03:24,390 --> 00:03:29,520
We also see that the premiers button state is the current one for the next time we look.

44
00:03:31,130 --> 00:03:38,390
And then we can do an action so we can check if, for example, button state is equal to high, which

45
00:03:38,390 --> 00:03:44,390
means that we have pressed on the button because we have a pull down register.

46
00:03:44,750 --> 00:03:49,580
And if it's low, we have just released the button, Matthew, we want to know when we press and but

47
00:03:50,150 --> 00:03:55,040
and once we have this, we can send to say it.

48
00:03:55,040 --> 00:04:03,950
So send a message to sail and to send a message to say I'm going to insulate cellule here cilia that

49
00:04:04,490 --> 00:04:10,400
begin with this Mod. We're going to use the same in the Raspberry Pi, Nadezhda.

50
00:04:10,400 --> 00:04:16,730
Do why not say oh OK for compatibility with some adding balls?

51
00:04:17,150 --> 00:04:22,910
And he I'm going to add something else that I didn't do before, and we probably won't need it in that

52
00:04:22,910 --> 00:04:29,750
product, but that can be a good best practice to add it to the wild cellular data available.

53
00:04:31,260 --> 00:04:33,180
Is greater than zero.

54
00:04:34,290 --> 00:04:41,520
You do say I don't read, so read is going to read only one bite.

55
00:04:41,880 --> 00:04:45,330
So here we just read it and we don't start it, we don't do anything with it.

56
00:04:45,570 --> 00:04:49,340
But basically what we do here is we just clear the inputs buffer.

57
00:04:49,950 --> 00:04:55,740
If you remember we sail in Python, you have the requisite input buffer function.

58
00:04:56,160 --> 00:05:03,090
We don't have one in Arduino, but we can easily implement it by just checking that, well, why do

59
00:05:03,090 --> 00:05:05,610
we still have bytes on the input method?

60
00:05:05,640 --> 00:05:07,860
We read them so we clear them from the bus.

61
00:05:08,520 --> 00:05:13,440
So we are sure that when we start here, we don't have anything in the input button.

62
00:05:13,980 --> 00:05:17,790
And so I say for these projects is not going to be useful because why is that?

63
00:05:18,270 --> 00:05:24,150
Because when we start the Python program and initialize the same communication with the Arduino when

64
00:05:24,270 --> 00:05:26,190
I don't know is going to be ready first.

65
00:05:26,520 --> 00:05:33,720
So by the time that we enter this block of code and that we enter the void loop, the Python program

66
00:05:33,720 --> 00:05:36,880
is still not going to be sending data.

67
00:05:36,900 --> 00:05:43,740
OK, so this is should not be called, but that can be a best practice for other projects of your own.

68
00:05:44,070 --> 00:05:44,460
OK.

69
00:05:44,640 --> 00:05:50,430
If you want to make different boards, communicate between each other and know that this signal is initialized,

70
00:05:50,430 --> 00:05:51,960
let's actually do here.

71
00:05:52,440 --> 00:05:55,290
So you are not trained.

72
00:05:55,410 --> 00:06:02,310
L.N. OK, because we need to backslash in the end button priced exactly like that.

73
00:06:03,000 --> 00:06:05,280
This should be eight to let's check.

74
00:06:06,480 --> 00:06:09,400
So we have those three variables here.

75
00:06:10,260 --> 00:06:14,160
We correctly initialize the state of the button.

76
00:06:14,160 --> 00:06:18,090
We the state, we have to say an initialization.

77
00:06:18,570 --> 00:06:22,260
And then we read from the button with the D bounce mechanism.

78
00:06:22,650 --> 00:06:33,970
And when the button is price we send but priced, let's connect the you know, okay, let's not.

79
00:06:33,990 --> 00:06:34,770
So it's good.

80
00:06:34,770 --> 00:06:37,050
Let's not blow the code.

81
00:06:38,880 --> 00:06:44,190
And when actually I have forward just made a typo here.

82
00:06:47,950 --> 00:06:54,620
The blowing down, the clouding lights up and missile monitor, and I'm going to press on the push button.

83
00:06:55,080 --> 00:06:59,580
So starting pressing the button button pressed the button price button price.

84
00:06:59,760 --> 00:07:05,130
Every time a price, I receive a button price message on the same monitor.

85
00:07:05,730 --> 00:07:07,140
Everything is correct.

86
00:07:07,380 --> 00:07:09,570
And that's the end of this step number three.

87
00:07:09,840 --> 00:07:14,830
We can now focus on the input commands that we receive from the Raspberry Pi.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,150 --> 00:00:06,180
This is step number nine of the final project, and that will be the last step where we write Python

2
00:00:06,180 --> 00:00:06,600
code.

3
00:00:06,960 --> 00:00:10,440
After this, our Python program is going to be complete for this project.

4
00:00:10,560 --> 00:00:17,610
And so what we still need to do now is to handle the deny deny command from Citigroup.

5
00:00:18,150 --> 00:00:25,140
So when we have an open door request, we can't deny so that we don't open the door and we print an

6
00:00:25,140 --> 00:00:26,700
error message for the user.

7
00:00:27,210 --> 00:00:31,350
And as you would see, this step is going to be quite quick and quite easy now because the way all the

8
00:00:31,350 --> 00:00:32,790
hard work was done before.

9
00:00:33,030 --> 00:00:37,650
So now we just need to add one functionality on top of what we have done.

10
00:00:38,070 --> 00:00:39,600
I'm going to also do new.

11
00:00:42,130 --> 00:00:44,950
And just paste that here.

12
00:00:46,900 --> 00:00:49,300
It's remove the lines that we don't need here.

13
00:00:53,020 --> 00:00:58,480
Just one here, and let's name it, so let's save it as.

14
00:01:02,020 --> 00:01:04,990
Intercom step nine.

15
00:01:06,400 --> 00:01:13,300
So what we need to do now is to add a callback for the dinner equipment we already have the data, everything

16
00:01:13,300 --> 00:01:16,180
is correctly set up, so we do need to do that again.

17
00:01:16,480 --> 00:01:19,430
We just need to create another callback.

18
00:01:19,990 --> 00:01:28,720
So after the open, for example, they deny Access Handler a date and context.

19
00:01:30,540 --> 00:01:35,880
But first, and let's let's not forget that, because if you forget, that's of course, not going to

20
00:01:35,880 --> 00:01:42,390
watch this much notes add another comment.

21
00:01:43,490 --> 00:01:46,070
And we've denied.

22
00:01:46,290 --> 00:01:48,720
OK, let's check again.

23
00:01:48,990 --> 00:01:50,100
We ask for denial.

24
00:01:50,340 --> 00:02:01,500
So let's get exactly DNA and the function is going to be denied access and allow me and I'm going to

25
00:02:01,500 --> 00:02:04,230
come back to the in just in a second.

26
00:02:05,130 --> 00:02:07,280
So why do we want to do this?

27
00:02:07,290 --> 00:02:09,120
Deny access handler.

28
00:02:09,330 --> 00:02:14,820
Well, first, what we don't want to do is to open the door, so we're not going to send opened up and

29
00:02:14,820 --> 00:02:16,600
we are not going to think closed door.

30
00:02:17,320 --> 00:02:21,660
So because when I have put some print here, so let's do print.

31
00:02:23,070 --> 00:02:25,590
Denying them access.

32
00:02:27,060 --> 00:02:36,510
And to deny the access we send to our renewal, so we're going to send something for the LCD screen,

33
00:02:36,990 --> 00:02:40,240
the sound and also the energy to render.

34
00:02:41,460 --> 00:02:42,930
OK, so let's put three.

35
00:02:44,280 --> 00:02:52,080
The first command is print text access denied.

36
00:02:53,850 --> 00:02:58,820
And then the second one is going to be Lee Buzzer.

37
00:02:59,640 --> 00:03:04,010
So this time we can use, let's say, 200 so well, 300.

38
00:03:04,020 --> 00:03:06,480
He heads for 500 milliseconds.

39
00:03:06,480 --> 00:03:08,160
So how a second here.

40
00:03:08,160 --> 00:03:11,790
When we close the door, we have 200, so that's lower pitch.

41
00:03:12,270 --> 00:03:14,010
We've had four seconds.

42
00:03:14,400 --> 00:03:19,650
Now we are going to send 200 with four one complete second.

43
00:03:20,070 --> 00:03:20,430
OK.

44
00:03:20,490 --> 00:03:25,140
You can experiment with different frequencies to find what you like best.

45
00:03:25,170 --> 00:03:25,470
OK.

46
00:03:25,710 --> 00:03:36,240
I'm just going to keep things simple here and sit, and we've 255, zero and zero.

47
00:03:38,400 --> 00:03:42,640
OK, after we send those commands, we're going to wait a few seconds.

48
00:03:42,690 --> 00:03:44,970
Time to sleep, let's wait for five seconds.

49
00:03:45,930 --> 00:03:52,200
OK, so we can leave some time for the user to see that the access is denied and after five seconds,

50
00:03:52,590 --> 00:03:54,210
we come back to the initial state.

51
00:03:54,960 --> 00:04:00,420
So we were sent to Reno three times.

52
00:04:06,350 --> 00:04:10,610
And what we do here, where we do print text.

53
00:04:11,900 --> 00:04:14,150
Push on button to call.

54
00:04:15,020 --> 00:04:17,900
So the exact same message.

55
00:04:18,200 --> 00:04:25,340
And then when actually we don't need to play the buzzer anymore because here we play a sound when we

56
00:04:25,340 --> 00:04:26,150
open the door.

57
00:04:26,600 --> 00:04:27,670
When we close the door.

58
00:04:27,690 --> 00:04:30,470
So that's a physical action, all when we deny access.

59
00:04:30,470 --> 00:04:33,770
But after that, no need to add another sound.

60
00:04:34,310 --> 00:04:42,630
So let's do set and indirectly we've zero zero zero and then so red, green and blue on.

61
00:04:43,400 --> 00:04:51,920
And what we can do also is like we need for the open command is that when we deny access from Telegram,

62
00:04:51,920 --> 00:04:52,420
we can speak.

63
00:04:52,430 --> 00:04:59,580
But that sent me sage chat I.D. is equal to the

64
00:05:02,120 --> 00:05:02,840
effective.

65
00:05:04,050 --> 00:05:04,530
Checked.

66
00:05:06,070 --> 00:05:21,010
The I.D. text denying access so that when we do the deny crewmen here from Tehran, we also have a confirmation.

67
00:05:21,040 --> 00:05:24,820
OK, here we have a confirmed mission opening the door, so we know that's happening.

68
00:05:25,330 --> 00:05:27,160
And we've denied access.

69
00:05:27,190 --> 00:05:31,810
We have no confirmation that we are denying the access and no will.

70
00:05:32,200 --> 00:05:36,630
We're going to have the same problem as we have the open door handle there.

71
00:05:37,000 --> 00:05:40,990
So basically here, if you don't run async.

72
00:05:42,210 --> 00:05:47,940
All the cutbacks, so all the deny access you're going to call are going to be put in acute and are

73
00:05:47,940 --> 00:05:54,060
going to be executed one by one instead of in power, and you don't want that because you have the time

74
00:05:54,060 --> 00:05:55,200
to sleep for fear.

75
00:05:55,530 --> 00:06:00,840
So if you price faultlines, then you're just going to do that for five seconds and then five seconds,

76
00:06:00,840 --> 00:06:01,530
et cetera.

77
00:06:01,800 --> 00:06:05,280
So you're going to continue to run the COVAX for 20 seconds.

78
00:06:06,550 --> 00:06:07,360
So we do.

79
00:06:08,770 --> 00:06:16,030
Right, async also for the deny request.

80
00:06:16,630 --> 00:06:20,870
And we're also going to use those two flags here.

81
00:06:20,890 --> 00:06:30,620
OK, so global open door requests and global handling door.

82
00:06:31,480 --> 00:06:39,580
So we are first going to do if open the request and put that inside if.

83
00:06:41,490 --> 00:06:45,570
Why is that because we don't want to deny an access if we don't have the request?

84
00:06:45,770 --> 00:06:52,110
OK, imagine that your intercom at your home is just printing access denied by itself without anyone

85
00:06:52,110 --> 00:06:53,640
to request to open the door.

86
00:06:53,820 --> 00:06:55,030
That's going to be a bit weird.

87
00:06:55,050 --> 00:07:03,150
OK, so if we have an open door request, well, actually from Telegram, we can either open or deny

88
00:07:03,150 --> 00:07:03,510
comment.

89
00:07:03,930 --> 00:07:10,200
So we're either going to go here or to go here and then at the end we can do open.

90
00:07:11,010 --> 00:07:14,850
The request is false.

91
00:07:15,180 --> 00:07:18,180
OK, so then we can try it again.

92
00:07:18,840 --> 00:07:25,770
And also, we are not going to deny the access if we have the handling door differently.

93
00:07:26,340 --> 00:07:31,800
So basically, if we are opening the door, we're not going to deny access at the same time.

94
00:07:32,010 --> 00:07:32,370
OK.

95
00:07:32,610 --> 00:07:38,310
So I'm going to put in not handling this in just a question of logic here.

96
00:07:38,670 --> 00:07:43,950
And the same thing is that if we are currently denying the access, we are not going to open the door,

97
00:07:43,950 --> 00:07:48,960
we're going to wait and the discussion is finished to start another action.

98
00:07:49,170 --> 00:08:00,840
And so I'm going up here and going door is equal to true and here handling, though, is equal to false.

99
00:08:01,080 --> 00:08:08,670
So even if we don't physically handle the door, we handle the door mechanism, OK, we just keep it

100
00:08:08,820 --> 00:08:10,590
locked for five seconds.

101
00:08:10,980 --> 00:08:16,830
So if you send a deny command, you're going to have handling door is equal to true for the duration

102
00:08:16,830 --> 00:08:17,220
of.

103
00:08:18,560 --> 00:08:25,490
This so basically five seconds and then if you try to open the door wide, you are in this, that's

104
00:08:25,490 --> 00:08:28,490
not going to work because the handling is going to be true.

105
00:08:28,880 --> 00:08:30,670
OK, so we've those two flags.

106
00:08:30,690 --> 00:08:36,830
We make sure that we only process equipment from Telegram when we have the request and that we only

107
00:08:36,830 --> 00:08:38,270
process one comment.

108
00:08:38,300 --> 00:08:46,940
Either we open the door once we denied access once and then we need to wait for another open door request.

109
00:08:47,540 --> 00:08:47,840
OK.

110
00:08:47,870 --> 00:08:56,240
And here we don't send requests if we are currently inside a request or if we are currently handling

111
00:08:56,240 --> 00:08:56,690
the door.

112
00:08:57,230 --> 00:08:59,150
All right, so now is the time to try this.

113
00:08:59,690 --> 00:09:00,890
Let's run down.

114
00:09:00,890 --> 00:09:04,960
So the know is still the same could not connect.

115
00:09:04,970 --> 00:09:08,570
Yes, if I actually click there, you know.

116
00:09:11,190 --> 00:09:18,170
OK, starting and then main loop is starting, so that's OK.

117
00:09:18,690 --> 00:09:26,260
Pressing the push button, we have the notification someone is ringing the bell and that someone is

118
00:09:26,280 --> 00:09:28,110
when we don't see that person.

119
00:09:28,560 --> 00:09:32,790
So let's deny the access and let's look at what we have.

120
00:09:34,050 --> 00:09:36,270
OK, we have a sound from the buzzer, right?

121
00:09:36,690 --> 00:09:37,500
Access denied.

122
00:09:37,890 --> 00:09:41,640
And after five seconds, we have again the initial state.

123
00:09:41,940 --> 00:09:43,350
So that's currently working.

124
00:09:43,350 --> 00:09:43,710
Know what?

125
00:09:43,710 --> 00:09:44,130
You can do it.

126
00:09:44,130 --> 00:09:51,480
You can try again and you can deny the access again, or you can accept and open the door, etc., etc.

127
00:09:51,660 --> 00:09:56,950
So let's quickly stop this problem with control c key, and you can see that it was quite faster.

128
00:09:57,150 --> 00:09:57,520
OK?

129
00:09:57,540 --> 00:10:02,970
Depends on the data, I guess, and when our Python code is now finished.

130
00:10:03,510 --> 00:10:07,920
So this code is actually you can see a hundred and thirty lines.

131
00:10:08,940 --> 00:10:13,380
And as a quick recap, we have so we have system in bots.

132
00:10:13,930 --> 00:10:17,660
Then some global variables, we initialize the cellule.

133
00:10:17,670 --> 00:10:23,790
We have a function for the schedule, we initialize the camera and then we have our today run callbacks.

134
00:10:23,970 --> 00:10:28,800
So three callbacks, we initialize the bot and a data.

135
00:10:30,300 --> 00:10:33,930
And after everything has been initialized, we wait for three seconds.

136
00:10:34,230 --> 00:10:40,320
We get the initial state of the application and we start the main look in the main loop.

137
00:10:40,830 --> 00:10:45,180
Well, basically we just read from cellular and if we have received something, we check if we have

138
00:10:45,180 --> 00:10:46,440
a button priced comment.

139
00:10:46,950 --> 00:10:53,820
And if we have a button press comment, we try to send the requests to Telegram with a message, a photo

140
00:10:54,300 --> 00:10:57,900
and some instructions so that the user can be open on the night.

141
00:10:57,900 --> 00:11:00,270
And that's going to call the Telegram callback.

142
00:11:00,780 --> 00:11:01,130
All right.

143
00:11:01,140 --> 00:11:04,740
And that is the end of this step number nine of the final project.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,090 --> 00:00:05,520
This is step number 10 and also the final step of this intercom project.

2
00:00:05,910 --> 00:00:11,460
So at this point, we have correctly written the complete out in your program and the complete Python

3
00:00:11,460 --> 00:00:11,870
program.

4
00:00:11,880 --> 00:00:13,660
So what else do we need to do, actually?

5
00:00:13,920 --> 00:00:18,830
Well, if you have noticed whenever you want to start the Python project on the Raspberry Pi, well,

6
00:00:18,990 --> 00:00:22,710
you need to put the Raspberry Pi, you need to logging in the desktop.

7
00:00:23,490 --> 00:00:29,460
We just come online with each and then you need to start the script, so you need to start Python scripts

8
00:00:29,460 --> 00:00:30,900
manually every time.

9
00:00:31,080 --> 00:00:35,040
Not a Raspberry Pi is nice because it's very small and you can put it anywhere.

10
00:00:35,370 --> 00:00:39,210
So what if we make the program just start on boots?

11
00:00:39,390 --> 00:00:43,440
So when you put the Raspberry Pi, the program is just also starting.

12
00:00:43,950 --> 00:00:45,060
That would be nice, right?

13
00:00:45,300 --> 00:00:46,590
And that's what we're going to do.

14
00:00:46,740 --> 00:00:52,200
So then the next time you put your Raspberry Pi, you don't need to log into the desktop.

15
00:00:52,500 --> 00:00:54,150
The application is just going to work.

16
00:00:54,840 --> 00:00:57,030
And to do that, we are going to use system.

17
00:00:57,330 --> 00:00:59,640
So this is not the coolest about system here.

18
00:00:59,790 --> 00:01:04,500
This is just a small improvement for the project as a kind of bonus step.

19
00:01:04,800 --> 00:01:09,840
So I'm just going to show you what you need to do step-by-step but very simplified explanation.

20
00:01:10,110 --> 00:01:12,000
I'm not going to dive into the details.

21
00:01:12,660 --> 00:01:15,390
And so first of all, we are going to go.

22
00:01:16,580 --> 00:01:26,250
In them, a where we have our intercom step nine, I'm going to put it as executable with C-H mode plus

23
00:01:26,250 --> 00:01:29,530
specs intercom step nine.

24
00:01:30,640 --> 00:01:32,680
And you can see turn green.

25
00:01:33,160 --> 00:01:38,860
OK, that's something that's going to be important for this step and then I can do, for example, inter-club

26
00:01:39,430 --> 00:01:41,620
step nine can launch it like this.

27
00:01:42,310 --> 00:01:43,450
So this is working.

28
00:01:43,630 --> 00:01:47,770
I have not connected the outing world actually here, and I can also launch it with Python.

29
00:01:47,770 --> 00:01:48,400
Three.

30
00:01:49,270 --> 00:01:54,610
Intercom Step nine OK, that is the same thing.

31
00:01:54,910 --> 00:01:57,210
So know that your script is at your table.

32
00:01:57,220 --> 00:02:06,030
Let's go to slash lib slash system slash system.

33
00:02:06,430 --> 00:02:08,860
Press Enter to Clear.

34
00:02:09,610 --> 00:02:12,130
And what do we have when we have a lot of things?

35
00:02:13,180 --> 00:02:19,090
And basically those you can see, many of those files are something dot semi's.

36
00:02:19,720 --> 00:02:26,800
And so we're going to create another file, another service and then make this start on boot.

37
00:02:27,610 --> 00:02:29,350
So let's just follow the steps here.

38
00:02:29,410 --> 00:02:33,280
So you do sudo nano to create fire.

39
00:02:33,280 --> 00:02:36,850
You need sudo because we are not in the home directory, right?

40
00:02:37,390 --> 00:02:39,170
And then let's name it.

41
00:02:39,220 --> 00:02:45,760
Intercom the project that so it's OK.

42
00:02:45,770 --> 00:02:47,170
And what are we going to write?

43
00:02:47,200 --> 00:02:50,200
So this is a specific structure you need to follow.

44
00:02:50,620 --> 00:02:54,940
First, we have brackets, unit description.

45
00:02:56,590 --> 00:03:05,470
So the description is anything you want, for example, intercom system, it doesn't really matter here.

46
00:03:06,310 --> 00:03:07,930
And then you have after.

47
00:03:07,990 --> 00:03:14,680
So right, exactly like this, you're going to put multi rush user don't target.

48
00:03:15,910 --> 00:03:20,410
So this is just to say that the program, the service is going to run after this.

49
00:03:20,410 --> 00:03:22,870
So you have many different steps in the boot.

50
00:03:23,080 --> 00:03:23,440
OK.

51
00:03:23,980 --> 00:03:28,840
And if you want to run the Python on program, you're just going to get you're just going to use multi

52
00:03:28,840 --> 00:03:30,370
user to target.

53
00:03:30,910 --> 00:03:35,380
So that is going to wait a bit until the environment is ready to start the script.

54
00:03:35,860 --> 00:03:39,600
After unit, you have service.

55
00:03:39,790 --> 00:03:49,240
So that's what you actually want to start and you're going to use exec start and exec started the command

56
00:03:49,240 --> 00:03:52,270
you want to run with the service.

57
00:03:52,510 --> 00:03:54,220
What is the command we want to run?

58
00:03:54,550 --> 00:03:56,230
We want to run the Python script.

59
00:03:56,710 --> 00:04:00,460
And so I went up when a new terminal here.

60
00:04:01,750 --> 00:04:04,000
So basically, we want to run Python three.

61
00:04:04,270 --> 00:04:08,610
We've got a script, but here we need to give the exact command with exact path.

62
00:04:08,620 --> 00:04:10,390
And what do I mean by the exact path?

63
00:04:10,690 --> 00:04:17,830
So if you do which by from three, you can see that Python three is actually discriminant slash user

64
00:04:17,830 --> 00:04:19,990
slash robin slash Python three.

65
00:04:20,170 --> 00:04:25,180
So when you use this in a terminal, actually that's a simplification for that.

66
00:04:25,750 --> 00:04:29,470
So I'm just going to control shift and see and control shift.

67
00:04:29,470 --> 00:04:32,210
And here we're going to use Python three.

68
00:04:32,230 --> 00:04:32,920
We've.

69
00:04:33,580 --> 00:04:42,610
So let's do Python arrives with this and how to get the correct absolute path.

70
00:04:42,730 --> 00:04:43,420
Bit of a unique.

71
00:04:45,560 --> 00:04:56,960
Some jobs are going to be this year with a space slush and could be the name of the fire.

72
00:04:57,140 --> 00:05:03,110
So we're going to run Python three with this script, with the absolute bat for the equipment and absolutely

73
00:05:03,120 --> 00:05:04,700
path for the fire.

74
00:05:05,480 --> 00:05:09,530
Then you can choose to use so user is equal to PI.

75
00:05:09,770 --> 00:05:14,830
So basically, you're going to run this as the PI user.

76
00:05:14,840 --> 00:05:18,490
So as the user, you are currently connected us.

77
00:05:18,980 --> 00:05:19,340
OK.

78
00:05:19,400 --> 00:05:21,830
So that's very important here to use the PI user.

79
00:05:22,520 --> 00:05:26,210
If you don't put that, it's going to use the route user.

80
00:05:26,810 --> 00:05:32,060
And well, I guess for this program, we shouldn't have any problem, but that may give you some issues

81
00:05:32,240 --> 00:05:33,380
with some programs.

82
00:05:33,380 --> 00:05:39,110
For example, if you have relative or fine names, or if you just use something that is only set up

83
00:05:39,290 --> 00:05:45,500
on the by user environment and not on the root user side, I recommend to use user is equal to pay.

84
00:05:45,890 --> 00:05:49,570
And then the last thing is install like this.

85
00:05:50,520 --> 00:05:59,260
Wanted by is equal to and in the same multi user that I get.

86
00:06:00,080 --> 00:06:02,080
OK, and that's the complete description.

87
00:06:02,090 --> 00:06:04,310
That's the complete structure for the service.

88
00:06:04,790 --> 00:06:06,230
You need service install.

89
00:06:06,590 --> 00:06:09,380
You can do control s control x.

90
00:06:10,400 --> 00:06:10,770
OK.

91
00:06:10,820 --> 00:06:13,280
And no defined is going to be somewhere here.

92
00:06:14,090 --> 00:06:25,370
What you can do now to clear what you can do is pseudo system TTL with Daemon Reload.

93
00:06:29,230 --> 00:06:33,040
And then, well, what you can do if you want to just stop the service.

94
00:06:33,280 --> 00:06:36,160
So not a service exists, but it's not going to start en route.

95
00:06:36,370 --> 00:06:36,630
OK.

96
00:06:37,000 --> 00:06:41,950
So in Phil's going to show you how you can do it, he started right now and then how you can enable

97
00:06:41,950 --> 00:06:43,240
it so it can start.

98
00:06:43,630 --> 00:06:46,620
So if you want, you can do studio system.

99
00:06:47,500 --> 00:06:56,110
So let's actually do Sydney to have more space studio system still stuck intercom.

100
00:06:56,650 --> 00:07:01,960
Let's actually press tab and will it's finding the service.

101
00:07:02,710 --> 00:07:03,730
And if I run this?

102
00:07:07,320 --> 00:07:10,200
You will see we have starting here, OK?

103
00:07:10,290 --> 00:07:15,780
And then we have the blue energy and when the application is actually starting, but we don't have any

104
00:07:15,780 --> 00:07:16,110
logs.

105
00:07:16,260 --> 00:07:18,720
OK, that's just the service that's going to start.

106
00:07:18,930 --> 00:07:27,090
But in a background process now, if you want to stop, you can do pseudo systems CTA Stop Intercom

107
00:07:27,090 --> 00:07:30,060
Project, then you stop the service.

108
00:07:30,480 --> 00:07:37,440
OK, so start and stop allow you to just start and stop the service as you want manually, but know

109
00:07:37,440 --> 00:07:43,440
what you can do is so let's do pseudo actually system client list.

110
00:07:44,250 --> 00:07:51,550
You need to find my center and we have a long list.

111
00:07:52,470 --> 00:07:56,400
OK, I'm just going to prosecute and once we can do instead is.

112
00:07:57,930 --> 00:08:07,290
Police unit finds and then by great intercom to just find what we need and you can see we have the intercom

113
00:08:07,290 --> 00:08:17,970
project service, which is disabled, so I'm going to do sudo systemctl enable intercom project service.

114
00:08:18,960 --> 00:08:25,080
You can see here created, similarly, etc., etc. If I do, the list unifies.

115
00:08:25,080 --> 00:08:26,820
You see note enabled.

116
00:08:27,240 --> 00:08:28,410
And so know what I'm going to do.

117
00:08:28,410 --> 00:08:35,610
And when I do know Reboot, let's reboot the Raspberry Pi and I'm currently on VMC, so you can see

118
00:08:35,610 --> 00:08:37,110
it's attempting to rebooting.

119
00:08:37,380 --> 00:08:40,620
And when the Raspberry Pi is rebooting, you can see starting.

120
00:08:46,570 --> 00:08:54,610
So starting again and you can see push on button to call, so actually what happened here is that first

121
00:08:54,790 --> 00:08:58,990
the Arduino was foiled again, and so the program started.

122
00:08:59,170 --> 00:09:05,020
So that was not from the Raspberry Pi and then the service started on, but on the Raspberry Pi.

123
00:09:05,380 --> 00:09:11,860
And when connecting to the Arduino, we're saying this actually had the effect to reboot the Arduino.

124
00:09:12,250 --> 00:09:14,140
And so you so starting again.

125
00:09:14,350 --> 00:09:19,510
But then the Raspberry Pi was communicating with the Arduino, and you can see that everything is set

126
00:09:19,510 --> 00:09:23,470
up and we can start to just press on the push button.

127
00:09:23,480 --> 00:09:30,190
Please wait for a few seconds, and we have just received a notification to open all denied access.

128
00:09:30,910 --> 00:09:31,300
All right.

129
00:09:31,310 --> 00:09:35,180
And as you see here, I have not manually launched the program.

130
00:09:35,200 --> 00:09:36,760
It has been launched automatically.

131
00:09:37,030 --> 00:09:39,220
Now let's go back to the terminal.

132
00:09:39,760 --> 00:09:48,700
OK, so if you want to stop, you can do pseudo systems that yell stop intercom service.

133
00:09:48,700 --> 00:09:54,160
So if you want to stop it, you can do that and he's going to stop and also know if you want to disable

134
00:09:54,160 --> 00:09:59,440
it, you can do to your system and disable intercom project.

135
00:09:59,680 --> 00:10:01,440
You can see this.

136
00:10:01,690 --> 00:10:14,770
And now, if you do see the systemctl list, you need files with great intercom just in there when we

137
00:10:14,770 --> 00:10:16,960
have the intercom project, which is disabled.

138
00:10:17,710 --> 00:10:23,200
OK, so you can easily restart and start with the starting to come in and then enable disable with the

139
00:10:23,200 --> 00:10:27,640
disable and enable criminals are easy and so know that it is disabled.

140
00:10:27,640 --> 00:10:32,470
The next time I'm going to reboot the Raspberry Pi, it's not going to start the service.

141
00:10:32,920 --> 00:10:35,380
If I put enable Israel to start the service.

142
00:10:35,710 --> 00:10:36,220
All right.

143
00:10:36,220 --> 00:10:44,140
And no, the project is complete so you can create the service, enable it and then just put your Arduino

144
00:10:44,140 --> 00:10:47,230
and your Raspberry Pi system wherever you want.

145
00:10:47,530 --> 00:10:52,870
OK, as long as the Raspberry Pi can connect Wi-Fi, of course, then you can just leave your application,

146
00:10:52,870 --> 00:10:58,090
run like that and wait for notifications on your phone with the Telegram application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:01,020
Congratulations.

2
00:00:01,200 --> 00:00:04,610
You have finished the final project on this course.

3
00:00:05,040 --> 00:00:11,160
This is yet another great achievement on your journey with Raspberry Pi and Arduino and NowIn.

4
00:00:11,280 --> 00:00:17,190
Even if this project is finished and currently working, there are many things you could work on to

5
00:00:17,190 --> 00:00:20,190
improve it or add new functionalities.

6
00:00:20,460 --> 00:00:26,130
The most interesting thing you could do is to adapt the project for your own needs.

7
00:00:26,430 --> 00:00:33,270
For example, if you want to implement an intercom system where you live and then if you are still craving

8
00:00:33,270 --> 00:00:38,370
some more practice, here are a few suggestions of things you could work on.

9
00:00:38,970 --> 00:00:45,480
So, for instance, screen you could make the text move if you have more than 32 characters.

10
00:00:46,040 --> 00:00:49,710
OK, so you can display everything even longer texts.

11
00:00:50,010 --> 00:00:57,120
You could also add a sitting callback so you can send custom texts from Telegram to the LCD.

12
00:00:57,130 --> 00:01:02,250
So we've already done that actually before in your previous activity, but you could add that to the

13
00:01:02,250 --> 00:01:02,760
project.

14
00:01:03,150 --> 00:01:08,670
So, for example, if you recognize someone on the photo, you can say, for example, Hello, John,

15
00:01:08,700 --> 00:01:09,240
how are you?

16
00:01:09,950 --> 00:01:16,950
Oh, just send a message like after the door, just go right in the door on the left, then about the

17
00:01:16,950 --> 00:01:17,660
several.

18
00:01:17,670 --> 00:01:24,840
So I've told it before, but you can attach it to a real door mechanism and define the opening and closing

19
00:01:24,840 --> 00:01:25,350
speed.

20
00:01:25,710 --> 00:01:28,560
So this would be a more mechanical part to the project.

21
00:01:28,950 --> 00:01:35,220
OK, well, you will have to basically experiment to find out how you can attach to a door mechanism

22
00:01:35,220 --> 00:01:39,030
or just any mechanism that's going to allow a door to be opened.

23
00:01:39,330 --> 00:01:44,160
And then when maybe they find an opening and closing speed because for some mechanism, if you try to

24
00:01:44,160 --> 00:01:49,080
go too fast, that's going to apply too much talk on the cell and it's not going to like it.

25
00:01:49,080 --> 00:01:50,760
So maybe you need to go slower.

26
00:01:50,770 --> 00:01:54,350
But these are, of course, there are millions possibilities.

27
00:01:54,360 --> 00:02:00,460
Trade depends on the physical configuration you have for your door or the mechanism for the camera.

28
00:02:00,490 --> 00:02:06,150
You could take a video instead of a photo so you send a few seconds video to Tillegra.

29
00:02:06,750 --> 00:02:08,930
You could also, and that's something different.

30
00:02:08,940 --> 00:02:15,420
You can also diffuse a video stream with the MJI big streamer, so that's something you can check on

31
00:02:15,420 --> 00:02:16,140
the internet.

32
00:02:16,650 --> 00:02:19,980
And that's also something you could use for a surveillance system.

33
00:02:20,160 --> 00:02:26,040
So basically, with this streamer, you can have and you are, you're going to check in this.

34
00:02:26,040 --> 00:02:31,950
You are you're going to have a constant stream of video, which is maybe better than just one photo,

35
00:02:32,130 --> 00:02:33,480
but is also more complex.

36
00:02:33,480 --> 00:02:35,010
And I will leave you to it.

37
00:02:35,400 --> 00:02:37,290
You can decide to do this if you want to.

38
00:02:37,860 --> 00:02:42,720
You can also enable or disable the message sending from Telegram.

39
00:02:43,080 --> 00:02:49,890
So basically, what I mean by that is that from Telegram, you have the option to deny and distort comments.

40
00:02:49,920 --> 00:02:55,680
You could also enable or disable so that basically you don't receive any notification from the Raspberry

41
00:02:55,680 --> 00:02:56,010
Pi.

42
00:02:56,220 --> 00:03:01,770
So when you send disable in the Raspberry Pi whenever someone presses on the push-button well, you're

43
00:03:01,770 --> 00:03:05,850
not going to do anything because you don't want to receive messages on Telegram.

44
00:03:06,240 --> 00:03:13,590
And when you send enable, well, you allow the application to send you some messages and send photos.

45
00:03:13,980 --> 00:03:18,510
Another improvement here could be that if you don't have any response after you press the button, for

46
00:03:18,510 --> 00:03:24,180
example, after 30 seconds, you could come back to the default state because what's happening here

47
00:03:24,510 --> 00:03:30,210
is that once you have pressed on the button, you're only going to come back to the default state after

48
00:03:30,210 --> 00:03:35,070
you have received a response or opened or denied access response.

49
00:03:35,310 --> 00:03:40,980
And so if no one is answering well, the state is just going to be stuck in the please wait.

50
00:03:41,290 --> 00:03:46,110
Okay, so maybe you want to come back to the initial state with another message, for example, that

51
00:03:46,110 --> 00:03:52,530
no one could answer your request and then come back to the initial state after 30 seconds one minute

52
00:03:53,100 --> 00:03:53,700
as you want.

53
00:03:53,820 --> 00:03:58,500
And one thing you could also do and this has nothing to do with the functionalities, but more with

54
00:03:58,500 --> 00:04:02,100
the code is to optimize the code with multiple fives.

55
00:04:02,100 --> 00:04:06,900
So we have just used one file for Arduino and one side for the Python program.

56
00:04:07,110 --> 00:04:13,110
OK, what you could do is to separate the different functionalities and implement them on different

57
00:04:13,110 --> 00:04:16,710
files that you're going to call from your main file and use them here.

58
00:04:17,250 --> 00:04:22,770
And so you're going to have a better organization, and new code is also going to be more scalable in

59
00:04:22,770 --> 00:04:23,370
the future.

60
00:04:23,640 --> 00:04:28,950
And when this list is not exhaustive, those who had just a few ideas and suggestions.

61
00:04:29,430 --> 00:04:36,180
I encourage you to come up with your own ideas and implement them so you can practice more and improve

62
00:04:36,180 --> 00:04:42,330
the project for your own needs and will once again congratulations for finishing this project.

63
00:04:42,660 --> 00:04:43,950
This is the end of the project.

64
00:04:44,310 --> 00:04:46,090
Let's go to the conclusion section.

65
00:04:46,110 --> 00:04:46,820
Alex.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: Conclusion

1
00:00:00,180 --> 00:00:02,220
You have just finished the course.

2
00:00:02,670 --> 00:00:03,780
Congratulations.

3
00:00:04,110 --> 00:00:08,940
If you've made it until that point, it means that you also have made huge progress.

4
00:00:09,390 --> 00:00:15,570
You can now apply your knowledge to any project of your own about any other project from scratch.

5
00:00:15,960 --> 00:00:21,840
And before we wrap things up, just a quick recap on how to build an application with both Raspberry

6
00:00:21,840 --> 00:00:28,590
Pi and the step by step process is kind of a best practice you can follow, which will help you progress

7
00:00:28,590 --> 00:00:30,330
faster when doing a project.

8
00:00:30,540 --> 00:00:37,800
So once you have a project idea, start by finding what functionalities do you need to implement in

9
00:00:37,800 --> 00:00:39,330
order to achieve the project.

10
00:00:39,600 --> 00:00:45,900
Then from those functionalities, choose which ones are going to be on the Arduino side and which ones

11
00:00:45,930 --> 00:00:51,960
are going to be on the Raspberry Pi site for some functionalities, like taking a photo with the Pi

12
00:00:51,960 --> 00:00:52,500
camera.

13
00:00:52,620 --> 00:00:58,530
Well, this is kind of obvious, but for other functionalities is going to be quite challenging to know

14
00:00:58,530 --> 00:01:02,700
on which side you should implement them to correctly choose.

15
00:01:03,030 --> 00:01:09,420
Remember that the application logic is on the Raspberry Pi and the execution of hardware equipment is

16
00:01:09,420 --> 00:01:15,750
under Agrium and will if you realize that you need to change one functionality later on when doing the

17
00:01:15,750 --> 00:01:16,260
project.

18
00:01:16,650 --> 00:01:17,380
No problem.

19
00:01:17,430 --> 00:01:20,100
OK, you can still modify it after that.

20
00:01:20,130 --> 00:01:25,680
The functionalities are clear to you and you know, on which side they are going to be implemented,

21
00:01:25,950 --> 00:01:29,070
then it's time to define a communication protocol.

22
00:01:29,610 --> 00:01:34,950
Basically, what commands and messages you're going to send and receive on both sides?

23
00:01:35,190 --> 00:01:40,140
It's important to do this now, so you know what to do when you are going to write to code.

24
00:01:40,800 --> 00:01:47,250
And finally, we arrive at the coding, but at this point, you have a good idea of what you need to

25
00:01:47,250 --> 00:01:47,490
do.

26
00:01:48,030 --> 00:01:54,090
I recommend you start with the Arduino code, implement the Arduino functionalities, and we say you'll

27
00:01:54,330 --> 00:02:00,990
send some messages and process the commands that you'll receive if you correctly down to previous steps.

28
00:02:01,230 --> 00:02:04,810
This should not be hard to do when writing the annual code.

29
00:02:04,830 --> 00:02:11,250
You can debug using the style monitor once this part of the application is working, then write the

30
00:02:11,250 --> 00:02:12,840
code on the Raspberry Bay.

31
00:02:13,140 --> 00:02:18,900
You will implement the functionalities that are specific to the Raspberry Pi and also the application

32
00:02:18,900 --> 00:02:19,410
logic.

33
00:02:19,650 --> 00:02:26,580
I suggest you iterate on the code one step at a time with a clear intermediate goal where you can see

34
00:02:26,580 --> 00:02:33,300
a real result after you've done and tested one step right the next one until you finish the application

35
00:02:33,750 --> 00:02:34,470
and will.

36
00:02:34,470 --> 00:02:41,490
If you follow this work structure, you should be able to create any product you want in no time.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:05,520
This is another great step you've taken towards the mastery of Arduino and the Raspberry Pi.

2
00:00:06,150 --> 00:00:08,280
No, you're not going to stop there, right?

3
00:00:08,490 --> 00:00:13,080
You probably want to progress more and also to build cool and useful products.

4
00:00:13,620 --> 00:00:16,860
So here are a few examples of what you could do next.

5
00:00:17,280 --> 00:00:23,940
You can start by improving the intercom project with the suggestions I gave you and also implement your

6
00:00:23,940 --> 00:00:31,140
own ideas and your personal touch to the project and maybe try to make it fit into your home then.

7
00:00:31,140 --> 00:00:33,690
And this is probably the best way to make progress.

8
00:00:33,990 --> 00:00:36,240
Find a completely new project.

9
00:00:36,750 --> 00:00:41,130
Maybe you already have an idea, or you can browse project ideas on the internet.

10
00:00:41,490 --> 00:00:45,300
Once you've selected the project, start with the step by step process.

11
00:00:45,300 --> 00:00:49,860
You just learn in the schools and apply the knowledge you got to finish the application.

12
00:00:50,340 --> 00:00:53,460
By doing this, you would really practice and improve your skills.

13
00:00:53,820 --> 00:00:59,250
And of course, don't hesitate to search on Google whenever you don't know how to do something new.

14
00:00:59,520 --> 00:01:05,220
On top of that, you could also explore more Arduino in the Raspberry Pi functionalities and see how

15
00:01:05,220 --> 00:01:08,640
you can use them with the combination of both moulds.

16
00:01:09,060 --> 00:01:09,520
And then.

17
00:01:09,660 --> 00:01:13,110
For example, why not take a look at the robot operating system?

18
00:01:13,470 --> 00:01:18,270
This is a great framework you can use to build more complex robotic applications.

19
00:01:18,780 --> 00:01:23,260
Actually, robot operating system in the Raspberry Pi are a great match.

20
00:01:23,640 --> 00:01:31,140
You can use the ROS Plus Raspberry Pi Plus Arduino combo to create a complete robot software, and that's

21
00:01:31,140 --> 00:01:34,110
what I did actually in your previous work experience.

22
00:01:34,320 --> 00:01:39,840
All right, those points are a few ideas you could work on, and of course, the list is not exhaustive.

23
00:01:40,080 --> 00:01:42,480
Finally, don't forget to have fun.

24
00:01:42,840 --> 00:01:48,420
This is super important if you have fun when building projects and learning new skills, you will make

25
00:01:48,420 --> 00:01:52,950
much more progress and this will lead to more fun and greater projects.

26
00:01:53,190 --> 00:01:56,160
And now I want to say thank you again for taking this course.

27
00:01:56,460 --> 00:01:58,290
I wish you the best for your next.

28
00:01:58,290 --> 00:02:02,070
I'll do note and Raspberry Pi project, and I hope to see you soon.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


==================================================================================
