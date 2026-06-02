# Section 1: Introduction

1
00:00:00,540 --> 00:00:00,900
Okay.

2
00:00:00,900 --> 00:00:03,180
So let's continue with details of the course content.

3
00:00:03,720 --> 00:00:08,280
The application we're creating will include the following features an extendable wireless local area

4
00:00:08,280 --> 00:00:14,400
network application that supports device connection to the SB 32 access point in order to access in

5
00:00:14,550 --> 00:00:15,480
FTP server.

6
00:00:15,870 --> 00:00:20,010
And the FTP server will support over the firmware updates via a web page.

7
00:00:20,280 --> 00:00:25,950
And connecting and disconnecting the ESP 32 with an external access point will display data on the web

8
00:00:25,950 --> 00:00:32,880
page such as temperature and humidity sensor data local time using P as well as the ESB 30 two's own

9
00:00:32,880 --> 00:00:33,710
SSD.

10
00:00:34,230 --> 00:00:40,890
The over the year firmware update or OTA update mechanism allows the ISP 32 to update itself wirelessly

11
00:00:40,890 --> 00:00:44,040
based on data received while the normal firmware is running.

12
00:00:44,280 --> 00:00:50,910
In our case, we'll do this over Wi-Fi via a web page, and the Dash 22 sensor will be used for getting

13
00:00:50,910 --> 00:00:56,430
the temperature and humidity data and will use non-volatile storage for saving and loading Wi-Fi credentials.

14
00:00:56,730 --> 00:01:01,320
And we'll have an RG bleed and create different colors to indicate the application status.

15
00:01:01,680 --> 00:01:07,460
S&amp;P will be used for getting local time and additionally we'll have a button with interrupt and Semaphore

16
00:01:07,470 --> 00:01:10,980
uses another method for disconnecting Wi-Fi and clearing credentials.

17
00:01:11,490 --> 00:01:15,990
And once we have the wireless local area network up and running, well then configure the project so

18
00:01:15,990 --> 00:01:23,640
that we can connect to a WSU T and go through the basic processes in a WC Iot core so that we can subscribe

19
00:01:23,640 --> 00:01:30,600
and publish data to and from the WC dashboard and we'll view the published data from the ESP 32 using

20
00:01:30,600 --> 00:01:36,720
the MQ T test client and the general steps that will take to accomplish this will include integrating

21
00:01:36,720 --> 00:01:42,450
the ESP RWC LTE framework, which will include updating the project to include the framework into the

22
00:01:42,450 --> 00:01:48,840
project build, which enables us to connect to a society will then go through a few processes in a WC

23
00:01:48,840 --> 00:01:54,120
society core to get things going, like creating a thing and creating a policy which will need to be

24
00:01:54,120 --> 00:01:58,830
attached to the thing and then generating the device, certificate, routes and keys.

25
00:01:59,070 --> 00:02:05,850
And on the east side will embed the device certificate root, CAA and private key so that the ECP 32

26
00:02:05,850 --> 00:02:08,310
can be authenticated with a W society.

27
00:02:08,760 --> 00:02:14,130
And then we'll also update the source code so that we can publish data from the ESP 32 such as the temperature,

28
00:02:14,160 --> 00:02:20,640
humidity and Wi-Fi received signal strength indicator or RSA say of the ISPs Wi-Fi connection so that

29
00:02:20,640 --> 00:02:25,320
we can view this data from a WC Iot core using the empty test client.

30
00:02:25,710 --> 00:02:31,980
And about the ESPN pdf, the ESPN pdf is express its official IOT Development Framework.

31
00:02:32,460 --> 00:02:35,070
It's open source and freely available on GitHub.

32
00:02:35,340 --> 00:02:40,530
It supports Windows, Mac and Linux and allows for development in C and C++.

33
00:02:40,800 --> 00:02:46,140
It's production ready and has a well-defined release process and support policy, and each release undergoes

34
00:02:46,140 --> 00:02:47,630
a rigorous Q&amp;A process.

35
00:02:47,940 --> 00:02:53,850
The ADF is feature rich and includes an Archos peripheral drivers networking stack and various protocol

36
00:02:53,850 --> 00:02:54,720
implementations.

37
00:02:55,380 --> 00:03:00,720
Additionally, the idea is version of the free Archos kernel is modified from multicore support and

38
00:03:00,720 --> 00:03:03,690
will utilize both course of the ESP 32 in this course.

39
00:03:04,440 --> 00:03:07,020
So let's talk about what you'll learn by taking this course.

40
00:03:07,380 --> 00:03:13,140
You will learn how to create an extensible modular application using the SBA, PDF and free Archos will

41
00:03:13,140 --> 00:03:18,870
program this application step by step, and I'll provide brief explanations of the SPF APIs that we'll

42
00:03:18,870 --> 00:03:19,260
use.

43
00:03:19,590 --> 00:03:25,620
And I must be clear that the focus of this course is not on theory or about the ESP 32 itself, as this

44
00:03:25,620 --> 00:03:28,290
is a hands on programming project based course.

45
00:03:28,590 --> 00:03:34,140
Additionally will utilize free artists and we'll have several free ARTAS tasks running within the application

46
00:03:34,530 --> 00:03:40,680
and we'll employ message cues for test communication between and within the FTP server and wi fi application.

47
00:03:40,980 --> 00:03:45,500
And we'll also have event groups in our state machine for the wi fi application and we'll also implement

48
00:03:45,510 --> 00:03:47,430
a binary semaphore for our button task.

49
00:03:48,270 --> 00:03:51,000
Now let's take a look at the programming languages used in this course.

50
00:03:51,480 --> 00:03:57,420
The C programming language is predominantly used in this course, but we'll also write HTML JavaScript

51
00:03:57,420 --> 00:03:59,490
and access to implement the web page.

52
00:03:59,880 --> 00:04:04,470
I should also mention that while using the C language throughout the course, I am not going to slow

53
00:04:04,470 --> 00:04:07,470
down and explain all of the aspects of the C language that we use.

54
00:04:07,770 --> 00:04:12,960
The reason for this approach is to maintain focus on implementing the application itself, which allows

55
00:04:12,960 --> 00:04:16,050
for a smoother, more efficient progression through the application code.

56
00:04:16,350 --> 00:04:22,380
That being said, experience with C is helpful and or willingness to stop and research topics that you

57
00:04:22,380 --> 00:04:23,340
do not understand.

58
00:04:24,120 --> 00:04:25,470
So why take this course?

59
00:04:26,190 --> 00:04:31,860
If you're working with the SB 32, then using the ESP IDF directly is the way to go for more serious

60
00:04:31,860 --> 00:04:33,150
embedded software development.

61
00:04:33,540 --> 00:04:37,290
Arduino for the ESP 32 is just a wrap around the IDF.

62
00:04:37,510 --> 00:04:40,020
It works well for those that just want to get something running.

63
00:04:40,320 --> 00:04:45,360
However, if you want to have a better understanding of what goes on under the hood of the ESP and if

64
00:04:45,360 --> 00:04:49,800
you want to become a better programmer, then moving away from the Arduino is worth considering.

65
00:04:50,040 --> 00:04:55,050
Also, the ESPN RDF is used in professional, commercial and industrial projects.

66
00:04:55,500 --> 00:04:59,550
Additionally, project setup is easier than ever using the eclipse idea plug in.

67
00:05:00,120 --> 00:05:05,910
Also I've selected commonly used components of the ESP ADF, which are often the basis of many Iot and

68
00:05:05,910 --> 00:05:11,160
industrial Iot applications, which involve a wireless local area network which often includes connecting

69
00:05:11,160 --> 00:05:17,520
to the internet, an HDB server, a web page for connecting and disconnecting the ISP and for OTA updates.

70
00:05:17,970 --> 00:05:23,550
Additionally, not spending time on lectures about the ESP 32 and other highly general topics may be

71
00:05:23,550 --> 00:05:24,600
beneficial to some.

72
00:05:24,900 --> 00:05:29,310
There is plenty of information available directly from impressive about the ESP 32.

73
00:05:29,490 --> 00:05:34,170
However, even though the focus is on physically programming this application, I'll try to fill the

74
00:05:34,170 --> 00:05:37,350
gaps by briefly covering the ESP ADF components used.

75
00:05:37,650 --> 00:05:42,900
I'll try to balance the South while maintaining focus on the application code because ultimately my

76
00:05:42,900 --> 00:05:46,890
goal is to provide you with something that you can actually use, learn from and enjoy.

77
00:05:47,250 --> 00:05:52,770
And yes, I do provide slides and code for all code changes implemented in each section of the course.

78
00:05:53,070 --> 00:05:57,180
So you can always refer back to the links in the slides later as we're writing the code.

79
00:05:57,360 --> 00:06:00,930
And you can always check your code by comparing yours with the resource files.

80
00:06:01,740 --> 00:06:02,100
Okay.

81
00:06:02,100 --> 00:06:04,800
So next, we'll take a look at the hardware and software requirements.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,600 --> 00:00:01,590
Hello and welcome back.

2
00:00:01,770 --> 00:00:04,350
Now let's take a look at the hardware and software used in the course.

3
00:00:05,040 --> 00:00:10,680
If you're not already aware of the ESB 32 by now, I'll just mentioned that the ESB 32 is a series of

4
00:00:10,680 --> 00:00:17,340
low cost, low power SLC or system on a CHIP series of microcontrollers with integrated Wi-Fi and dual

5
00:00:17,340 --> 00:00:18,120
mode Bluetooth.

6
00:00:18,450 --> 00:00:21,420
And for this course, we'll use an ESP 32 depth kit.

7
00:00:21,690 --> 00:00:26,610
Any ESP 32 dev kit will work for this course and I personally have a few decades.

8
00:00:26,820 --> 00:00:29,460
However, I do prefer working with the rubber dev kit.

9
00:00:29,970 --> 00:00:34,860
You can find information about it if you follow this link and you can find information about all the

10
00:00:34,860 --> 00:00:37,080
SPECIF dev kits via the following link.

11
00:00:39,090 --> 00:00:45,060
Other hardware components include an arguably either the package type here or the common NATO.

12
00:00:45,060 --> 00:00:52,710
A common cathode type also will use an AM to 302 DHT 22 sensor for temperature and humidity data.

13
00:00:53,370 --> 00:00:58,050
And you'll also want to have jumper wires and a breadboard available to connect these components to

14
00:00:58,050 --> 00:00:59,580
the ESP 32 dev kit.

15
00:01:00,300 --> 00:01:05,880
So moving on to the software requirements, we'll use the Eclipse RDF plugin which is available for

16
00:01:05,880 --> 00:01:09,570
Linux, Mac and Windows and I'll demonstrate the Windows installation.

17
00:01:09,900 --> 00:01:14,520
However, in the documentation they provide, you'll find instructions for both Linux and Mac as well.

18
00:01:15,000 --> 00:01:21,300
The Windows installation is an all in one install and gives you the ESPN PDF Idea of tools and Eclipse

19
00:01:21,300 --> 00:01:21,750
as well.

20
00:01:22,230 --> 00:01:26,220
You can also install it as a plug in to an existing Eclipse installation if you prefer.

21
00:01:26,490 --> 00:01:29,220
It's quite easy to do and you can find details here.

22
00:01:30,290 --> 00:01:35,960
With the eclipse idea, you can easily create, see, make ideas projects, create launch targets for

23
00:01:35,960 --> 00:01:42,110
different variants of the ESP, compile, flash and debug as well as view the serial output, which

24
00:01:42,110 --> 00:01:44,390
will be our main method of debugging in this course.

25
00:01:45,320 --> 00:01:45,680
Okay.

26
00:01:45,680 --> 00:01:47,690
So next we'll take a look at the core structure.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,550 --> 00:00:07,240
Hi, everyone.

2
00:00:07,450 --> 00:00:11,950
So before we get started, let's take a look at the cost structure for the wireless local area network

3
00:00:11,950 --> 00:00:15,520
that we'll create, which will then use to connect to a society.

4
00:00:16,270 --> 00:00:21,250
I'll start off by taking a very brief look at the impressive dev kits and the related documentation

5
00:00:21,250 --> 00:00:22,450
provided by Impressive.

6
00:00:23,360 --> 00:00:27,530
Will then go through the eclipse idea for the installation process in Windows.

7
00:00:27,890 --> 00:00:32,720
However, if you're using Linux or Mac, you can easily follow instructions within the resources I provided

8
00:00:32,930 --> 00:00:35,570
to complete the installation for you operating system on your own.

9
00:00:36,050 --> 00:00:41,090
And the first task will be to set up a template project which will use going forward and to set up the

10
00:00:41,090 --> 00:00:43,490
project configuration so that we can build in flesh.

11
00:00:43,970 --> 00:00:48,740
Then we'll go through some introductory supplemental lessons for getting our feet wet by taking a look

12
00:00:48,740 --> 00:00:54,170
at how we can set up the example projects provided by expressive and direct provided additional resources

13
00:00:54,170 --> 00:00:56,660
which are helpful in getting started with application development.

14
00:00:56,990 --> 00:01:03,260
Using the SPF index will proceed with some background information on the SPF EDF version of free artus

15
00:01:03,560 --> 00:01:05,300
and go through the Free Artas basics.

16
00:01:05,660 --> 00:01:09,320
Then I'll provide a briefing on the coding style that we'll use so that you know what to expect in the

17
00:01:09,320 --> 00:01:09,710
course.

18
00:01:10,250 --> 00:01:13,040
And it'll also share the location of the Git repository with you.

19
00:01:13,490 --> 00:01:16,070
And from that point, we'll proceed with application development.

20
00:01:16,340 --> 00:01:19,050
We'll create the status slide colors using an LED.

21
00:01:19,730 --> 00:01:24,140
Then we'll create the basis for the wi fi application that we'll build upon throughout the course.

22
00:01:24,380 --> 00:01:28,340
And the lessons that follow will include the initial development of the HTTP server.

23
00:01:28,760 --> 00:01:34,580
And I should mention that the wi fi application and HTTP server will communicate using free are message

24
00:01:34,580 --> 00:01:37,370
queues and we'll expand those throughout the course as well.

25
00:01:38,300 --> 00:01:43,280
Next, we'll move on to the over the year firmware update which works over the wireless local area network

26
00:01:43,610 --> 00:01:49,140
using a mobile device, laptop or any device with wi fi and a web browser that you can use to connect

27
00:01:49,140 --> 00:01:49,730
to your ISP.

28
00:01:49,730 --> 00:01:57,770
32 Dev Kit A.L. Provide boilerplate HTML JavaScript and CSV file templates that we'll continue to build

29
00:01:57,770 --> 00:01:58,850
upon throughout the course.

30
00:01:59,930 --> 00:02:05,450
The application will then be expanded to display data from the DHT 22 temperature and humidity sensor.

31
00:02:06,450 --> 00:02:12,360
And then we'll update the web page and server to enable connecting and disconnecting the ISP 32 with

32
00:02:12,360 --> 00:02:16,170
an access point, as well as displaying the connection information on the web page.

33
00:02:17,110 --> 00:02:20,860
And we'll use non-volatile storage for saving and loading Wi-Fi credentials.

34
00:02:21,900 --> 00:02:27,120
Then we'll implement a wi fi reset button using the boot button on the death kit, which employs the

35
00:02:27,120 --> 00:02:33,300
use of an interrupt and binary semaphore and and PTP time synchronization will be used to display the

36
00:02:33,300 --> 00:02:34,680
local time on the webpage.

37
00:02:35,820 --> 00:02:40,260
And we'll also display the ESP 32 axis point S's I.D. on the Web page as well.

38
00:02:41,130 --> 00:02:44,370
And currently the last section involves a society.

39
00:02:44,820 --> 00:02:50,520
For this section, I'll provide a general introduction to society and our implementation, as well as

40
00:02:50,520 --> 00:02:55,800
some information about account setup and where to find a society resources and documentation.

41
00:02:56,130 --> 00:03:00,690
The next lesson will include some technical background information that is useful to know about prior

42
00:03:00,690 --> 00:03:06,870
to getting into a WSU team will then configure the project so that we're able to connect to a society

43
00:03:06,870 --> 00:03:11,040
core and publish data to and from the MQ test console.

44
00:03:11,550 --> 00:03:18,060
And then we'll do a thorough review of the WC Iot subscribe published source code and updated to publish

45
00:03:18,060 --> 00:03:23,550
the temperature, humidity and the wi fi RSS psi, which is the received signal strength indicator of

46
00:03:23,550 --> 00:03:24,570
the Wi-Fi connection.

47
00:03:24,870 --> 00:03:29,790
And lastly, I should mention that I tested the web page functionality in this course using Google Chrome,

48
00:03:30,150 --> 00:03:34,020
so I suggest that you use the same info about the course organization.

49
00:03:34,170 --> 00:03:39,270
So before starting step by step programming sessions, I'll provide a PowerPoint presentation with relevant

50
00:03:39,270 --> 00:03:44,220
information about the implementation and an overview of general requirements for the programming section.

51
00:03:44,550 --> 00:03:49,350
I'll also provide suggested reading with links to the relevant expressive documentation, and I'll also

52
00:03:49,350 --> 00:03:54,090
outline the steps that we'll go through to implement the tasks at hand with brief explanations of the

53
00:03:54,090 --> 00:03:57,450
selected ESP ADF APIs used for each section.

54
00:03:58,170 --> 00:04:01,530
The provided resources for this course will include the PowerPoint slides.

55
00:04:01,980 --> 00:04:06,450
There you'll find links to the suggested reading and expressive documentation for the APIs that we're

56
00:04:06,450 --> 00:04:06,900
using.

57
00:04:07,320 --> 00:04:11,670
Also, you may want to have this information on hand to review while we're going through the programming

58
00:04:11,670 --> 00:04:17,190
sections, and I encourage you to pause the videos at any time to take a look at these as this may help

59
00:04:17,190 --> 00:04:20,430
you in getting more familiar with this recipes IOT Development Framework.

60
00:04:20,850 --> 00:04:25,860
Also, in each section I've provided you with code that we've implemented, you'll find this in the

61
00:04:25,860 --> 00:04:29,850
section overview if there is an overview for that particular section.

62
00:04:30,240 --> 00:04:33,900
Otherwise I'll include the resources directly in the lesson as shown here.

63
00:04:35,250 --> 00:04:40,410
And in case of any errors, you can always refer back to the attachments provided and compare the code

64
00:04:40,410 --> 00:04:41,040
with yours.

65
00:04:41,370 --> 00:04:43,830
And I do suggest that you type it out as we go along.

66
00:04:45,320 --> 00:04:46,820
All right, so I'll see you in the course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
==================================================================================

# Section 2: Espressif Hardware ESP32 DevKits

1
00:00:07,270 --> 00:00:09,220
Before we set up the development environment.

2
00:00:09,220 --> 00:00:13,780
I just want to talk about the dev kits available from Espressif and also mentioned the dev kits that

3
00:00:13,780 --> 00:00:15,730
I've used while creating this course.

4
00:00:15,970 --> 00:00:20,740
If you open the link in the resources available for this video called Development Board Overviews,

5
00:00:20,770 --> 00:00:23,740
you'll find a list of available dev kits from espressif.

6
00:00:23,770 --> 00:00:26,040
Any esp32 should work fine.

7
00:00:26,050 --> 00:00:30,970
However, just so you're fully aware, I've created this course using the first three in the list.

8
00:00:31,000 --> 00:00:31,690
The dev kit.

9
00:00:31,720 --> 00:00:35,110
See the rover kit as well as the pico kit.

10
00:00:35,230 --> 00:00:39,880
So be sure to look into the Getting Started guide for yours and browse through the information provided.

11
00:00:40,000 --> 00:00:44,680
Here you'll find just about everything that you need to know about your hardware, including the functional

12
00:00:44,680 --> 00:00:45,520
description.

13
00:00:46,370 --> 00:00:47,930
And how to power your board.

14
00:00:48,960 --> 00:00:54,720
The header block which includes the name and function of the i o header pins as well as the pin layout.

15
00:00:54,870 --> 00:00:57,330
This is a good way to get familiar with your hardware.

16
00:00:57,690 --> 00:01:02,130
Also, you can find the schematics and the datasheet at the bottom of the page.

17
00:01:04,350 --> 00:01:09,090
And if you happen to use the rover kit, there's additional points of interest to take note of.

18
00:01:09,120 --> 00:01:13,110
The functional description provides you with labels for each component, which is nice.

19
00:01:13,110 --> 00:01:16,560
But what's really worth noting are the setup options shown here.

20
00:01:16,740 --> 00:01:22,890
Be sure to include jumpers where necessary, as shown, as well as the jumpers shown further down under

21
00:01:22,890 --> 00:01:25,890
the initial setup for enabling USB and Uart.

22
00:01:26,960 --> 00:01:28,430
Further to the dev kit.

23
00:01:28,610 --> 00:01:34,460
If you open the second link in the resources you may need to install and configure USB drivers so that

24
00:01:34,460 --> 00:01:37,760
the ESP 32 is recognized by your machine.

25
00:01:37,850 --> 00:01:41,750
You can follow instructions specific to your operating system shown here.

26
00:01:41,780 --> 00:01:47,210
However, this should be taken care of by the Eclipse installation that will do in the following lessons.

27
00:01:47,450 --> 00:01:52,820
But just know that you can come back here if the development kit isn't recognized by your computer.

28
00:01:52,850 --> 00:01:56,540
Just follow the instructions step by step and you should be good to go.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Development Environment Setup, and ESP-IDF Build System & CMake Overview


1
00:00:06,690 --> 00:00:11,430
In this lesson, we'll go through the Windows installation for the expressive video, also known as

2
00:00:11,430 --> 00:00:17,490
the Eclipse IDF Plug in, which is an all in one installation that includes the ESP 32 Toolchain, Build

3
00:00:17,490 --> 00:00:21,060
Tools and the ESP IDF and full disclosure.

4
00:00:21,090 --> 00:00:26,700
This lesson is actually a rerecord, which I decided to do to avoid confusion as the pages have changed

5
00:00:26,700 --> 00:00:29,580
a bit and there are now new installations available.

6
00:00:30,090 --> 00:00:34,740
So if you're not using Windows, you can find instructions for both Linux and Mac OS within the same

7
00:00:34,740 --> 00:00:37,500
links I provided, which you can easily follow on your own.

8
00:00:38,010 --> 00:00:39,690
So now open the getting started guide link.

9
00:00:39,690 --> 00:00:40,980
Then I'm standing on now.

10
00:00:41,310 --> 00:00:46,680
This page gives you the rundown of the entire setup process and assuming you already have the ESP 32

11
00:00:46,680 --> 00:00:47,460
hardware.

12
00:00:47,610 --> 00:00:49,140
Let's take a look at the software.

13
00:00:50,800 --> 00:00:58,330
So here in the software it says to start using the ESP on the ESP 30 to install the following software,

14
00:00:58,360 --> 00:01:00,910
the toolchain, build tools and the ESP.

15
00:01:01,960 --> 00:01:03,730
And there are different ways to do that.

16
00:01:04,000 --> 00:01:06,520
So let's continue by going to the installation section.

17
00:01:07,620 --> 00:01:12,420
And with regards to the installation, you have the choice to install the required software through

18
00:01:12,420 --> 00:01:17,760
your favorite ID, or you can go ahead with the manual installation, but we'll go with the recommended

19
00:01:17,760 --> 00:01:20,790
route and I'm going to choose the eclipse plug in.

20
00:01:20,940 --> 00:01:26,460
But other students have mentioned that they prefer the code extension, so feel free to do that if you

21
00:01:26,490 --> 00:01:27,390
know what you're doing.

22
00:01:27,690 --> 00:01:30,990
Otherwise, let's go ahead and follow the Eclipse plugin link.

23
00:01:33,700 --> 00:01:39,700
And here we are at the idea of Eclipse plugin page, which also contains instructions for both Linux

24
00:01:39,700 --> 00:01:40,690
and Mac OS.

25
00:01:40,960 --> 00:01:43,300
But we'll go through the Windows installation now.

26
00:01:43,660 --> 00:01:46,150
So let's go down to installing prerequisites.

27
00:01:49,920 --> 00:01:55,980
And the prerequisites listed here are required for the IDF Eclipse plugin, but we'll bypass installing

28
00:01:55,980 --> 00:01:59,640
each of these one by one by using an all in one installer.

29
00:01:59,940 --> 00:02:03,870
So let's go to the expressive IDE offline installer page.

30
00:02:06,950 --> 00:02:10,220
And now we're standing directly on the offline installer section.

31
00:02:10,400 --> 00:02:15,140
And I've tested the course source code with most of these, including the latest version here.

32
00:02:15,190 --> 00:02:16,400
It all works fine.

33
00:02:16,580 --> 00:02:22,760
But for the majority of the course, aside from the sensors demos and the A Iot section, I've used

34
00:02:22,760 --> 00:02:27,800
an older version, so you can either choose one of these or if you want everything to look the same

35
00:02:27,800 --> 00:02:28,460
as what I'm using.

36
00:02:28,460 --> 00:02:36,710
In the core of the course from the GB led lesson up to a Iot, then you can use the older version here.

37
00:02:37,160 --> 00:02:43,010
And when it comes to versions, the differences would be the look and feel of the ID and of course the

38
00:02:43,010 --> 00:02:46,230
ESP ID version that comes with the installation package.

39
00:02:46,250 --> 00:02:51,200
So feel free to choose a newer version if you like, but for the sake of maintaining consistency with

40
00:02:51,200 --> 00:02:56,690
the core lessons and the project setup lesson coming up, I'll download the older version here.

41
00:02:56,930 --> 00:02:59,660
So I'll click download for this offline installer.

42
00:03:00,640 --> 00:03:05,680
And this may take a while, so I'll go ahead and speed up the video and you can feel free to pause and

43
00:03:05,680 --> 00:03:07,840
come back once yours is downloaded.

44
00:03:12,180 --> 00:03:14,010
Okay, now let's run the installer.

45
00:03:15,270 --> 00:03:16,470
And just give it a moment.

46
00:03:20,120 --> 00:03:22,880
Then choose your language and click okay.

47
00:03:24,720 --> 00:03:26,280
Then accept the agreement.

48
00:03:27,840 --> 00:03:28,980
And click next.

49
00:03:30,000 --> 00:03:33,360
Now let the system check finish, then hit next.

50
00:03:34,830 --> 00:03:39,900
Here you can choose the SB IDF version and I'll go with version 4.3.1.

51
00:03:39,900 --> 00:03:43,980
But if you have a new installation, you'll see that there's other versions listed here.

52
00:03:44,010 --> 00:03:46,020
So feel free to choose whatever you like.

53
00:03:46,910 --> 00:03:51,080
And then here I'm going to change the directory where the ESP is downloaded.

54
00:03:52,610 --> 00:03:54,500
And you could change yours to whatever you like.

55
00:03:55,250 --> 00:03:55,800
Okay.

56
00:03:55,970 --> 00:03:57,110
And then go next.

57
00:03:58,440 --> 00:04:02,910
So now I'll let the ESP tools be installed in the default location there.

58
00:04:03,180 --> 00:04:04,080
Click next.

59
00:04:05,180 --> 00:04:07,310
And here I'll go with the full installation.

60
00:04:07,760 --> 00:04:09,230
Everything here looks fine.

61
00:04:12,830 --> 00:04:15,120
And this is what's actually going to be installed.

62
00:04:15,140 --> 00:04:20,960
Just so you know, you're also getting Git and there's the version of the IDF that's going to be downloaded.

63
00:04:21,440 --> 00:04:23,180
And then the tools here as well.

64
00:04:23,780 --> 00:04:25,040
So let's install.

65
00:04:26,500 --> 00:04:28,030
Just let the installer run.

66
00:04:28,060 --> 00:04:30,010
This process may take some time.

67
00:04:30,760 --> 00:04:36,220
And go ahead and speed up the video and you can feel free to pause here and come back once you see the

68
00:04:36,220 --> 00:04:37,750
completing setup dialog.

69
00:04:52,010 --> 00:04:54,230
All right, so the setup is finished installing.

70
00:04:54,320 --> 00:04:58,580
Now let's check the box to run the ESP ADF eclipse environment.

71
00:04:59,120 --> 00:05:00,050
Click, finish.

72
00:05:04,490 --> 00:05:10,160
And here we see that the installation has set the IDF path at the location of the ESP IDF.

73
00:05:11,000 --> 00:05:15,170
And it's added the ESP IDF tools to the path environment variable.

74
00:05:16,750 --> 00:05:22,330
And the two command prompts here, which come with the installation package, are the ESP, ADF command

75
00:05:22,330 --> 00:05:28,690
line and the ESP ADF PowerShell, which you can use to run, build and flash commands and you can also

76
00:05:28,690 --> 00:05:30,430
run what's called a menu config.

77
00:05:30,760 --> 00:05:35,110
But I'll touch on this in the next lesson where we discuss the ESP ADF build system.

78
00:05:35,960 --> 00:05:38,360
Let's now change over to the eclipse launcher.

79
00:05:39,580 --> 00:05:43,990
And here I'm going to choose a workspace, and I've already created a workspace folder.

80
00:05:44,200 --> 00:05:46,000
And you should create one too.

81
00:05:46,840 --> 00:05:49,180
So now I'll copy the path to my workspace.

82
00:05:50,460 --> 00:05:51,660
And that's mine here.

83
00:05:52,080 --> 00:05:55,680
I've just created a folder at this path and called it Workspace.

84
00:05:55,860 --> 00:05:59,880
So feel free to do something similar and I'll just copy the path.

85
00:06:00,790 --> 00:06:02,260
And go back to the launcher.

86
00:06:04,100 --> 00:06:05,840
And paste in the workspace path.

87
00:06:06,720 --> 00:06:08,190
And then we could click launch.

88
00:06:11,650 --> 00:06:13,630
Just give the idea a moment to start.

89
00:06:13,630 --> 00:06:17,500
And in the next lesson we'll review the ESP build system.

90
00:06:17,620 --> 00:06:22,210
Then in the lesson that follows, we'll set up the Eclipse project template that will work with going

91
00:06:22,210 --> 00:06:22,780
forward.

92
00:06:23,140 --> 00:06:23,650
All right.

93
00:06:23,650 --> 00:06:24,610
I'll see you soon.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,540 --> 00:00:11,940
Before we set up the project template, let's review and get familiar with how an ESP IDF project is

2
00:00:11,940 --> 00:00:13,170
organized and built.

3
00:00:13,710 --> 00:00:18,630
So in this lesson, we're going to review the impressive documentation and get into details about the

4
00:00:18,630 --> 00:00:22,290
following topics which relate to the ESP, IDF build system.

5
00:00:22,470 --> 00:00:28,230
But first, let's put this into context by taking a look at what components can be included in an ESP

6
00:00:28,230 --> 00:00:31,920
IDF project for a web server application that shows the humidity.

7
00:00:31,920 --> 00:00:39,180
For this example, you could have the ESP, IDF base libraries, WiFi drivers, TCP IP stack, the free

8
00:00:39,180 --> 00:00:45,960
auto's operating system, a web server and a driver for the humidity sensor and the main code tying

9
00:00:45,960 --> 00:00:46,770
it all together.

10
00:00:47,040 --> 00:00:52,560
So the ESP, IDF components are configurable and the build system will compile the project based on

11
00:00:52,560 --> 00:00:54,090
the configuration settings.

12
00:00:54,150 --> 00:00:59,040
Also, the build system needs to know where your custom components and application code are located.

13
00:00:59,840 --> 00:01:05,810
So to get to know that ESP IDF Build System, we'll review the basic build system concepts and various

14
00:01:05,810 --> 00:01:08,120
methods of using the build system and CMYK.

15
00:01:08,150 --> 00:01:12,890
Then we'll take a look at an example, see, make project setup and look further into the project,

16
00:01:12,920 --> 00:01:16,060
see, make list file and also how to create a minimal component.

17
00:01:16,100 --> 00:01:17,210
C Make this file.

18
00:01:18,520 --> 00:01:18,820
All right.

19
00:01:18,820 --> 00:01:23,410
So this link provides a description of the concepts listed here, and this may seem pretty basic to

20
00:01:23,410 --> 00:01:25,190
some, but this is important.

21
00:01:25,210 --> 00:01:27,370
ESP IDF Project terminology.

22
00:01:28,390 --> 00:01:34,780
So a project is a directory that contains all the files and configuration to build a single app or executable,

23
00:01:34,780 --> 00:01:41,770
as well as supporting elements such as the partition table data, file system partitions and a bootloader.

24
00:01:41,980 --> 00:01:45,640
So the project directory is the top level directory here.

25
00:01:45,880 --> 00:01:51,550
And regarding the partition table, we get into more details in the OTA firmware update section, but

26
00:01:51,550 --> 00:01:58,240
it's basically a CSV file stored in the flash that designates various kinds of data to specific partitions.

27
00:01:58,240 --> 00:02:03,100
And these tables can be found with your toolchain is installed and mine is installed to the path here.

28
00:02:03,400 --> 00:02:09,880
And just to give you a basic idea, I've modified this partition table to contain two OTA partitions,

29
00:02:09,880 --> 00:02:12,820
one for the update and one for the application to run on.

30
00:02:12,820 --> 00:02:18,370
And it also contains sections for nonvolatile storage OTA data, which the bootloader consults to know

31
00:02:18,370 --> 00:02:24,010
which OTA app to execute and fight init data which is responsible for the physical layer of network

32
00:02:24,010 --> 00:02:25,000
communications.

33
00:02:25,000 --> 00:02:28,390
And again, we'll look further into this in the OTA update section.

34
00:02:29,350 --> 00:02:35,170
So we also have the project configuration which is held in a single file called the SDK config, which

35
00:02:35,170 --> 00:02:37,600
is located in the root directory of the project.

36
00:02:37,630 --> 00:02:43,870
This configuration file is modified via the IDF py menu config to customize the configuration of the

37
00:02:43,870 --> 00:02:44,590
project.

38
00:02:44,590 --> 00:02:50,020
But for our convenience, instead of using the command line menu config, we'll use the ID for modifying

39
00:02:50,020 --> 00:02:54,550
the Sdhc config file and we'll actually update this during the project template setup.

40
00:02:54,790 --> 00:03:00,880
But if you're curious and you want to know how to invoke IDF py menu config, you can go to the ESP

41
00:03:00,880 --> 00:03:07,000
IDF command line or the ESP IDF PowerShell, which comes with the installation you've already completed.

42
00:03:08,040 --> 00:03:10,230
And first you go to your project directory.

43
00:03:12,620 --> 00:03:15,710
Then use the IDF py menu config command.

44
00:03:19,960 --> 00:03:23,920
And here's the menu config which you can use to update the sdhc config file.

45
00:03:24,670 --> 00:03:29,920
Next we have an app which is an executable that is built by the ESP, IDF, a single project.

46
00:03:29,920 --> 00:03:35,020
We usually build two apps, a project app which is the main executable that is your custom firmware

47
00:03:35,020 --> 00:03:40,030
and a bootloader app, which is the initial bootloader program which launches the project application.

48
00:03:40,690 --> 00:03:45,520
Also, there are components which are modular pieces of standalone code which are compiled into static

49
00:03:45,520 --> 00:03:48,950
libraries or files and linked into an app.

50
00:03:48,970 --> 00:03:54,070
Some are provided by the ISP itself, while others may be sourced from other places.

51
00:03:54,340 --> 00:04:00,670
For example, this ESP IDF Libs Sensors Library here contains a number of components and whether you

52
00:04:00,670 --> 00:04:05,650
integrate components like this into your project or write custom code that you want to divide into separate

53
00:04:05,650 --> 00:04:10,390
components, you could do it in a similar way that it's done here, and we'll see how to accomplish

54
00:04:10,390 --> 00:04:11,590
this later in the lesson.

55
00:04:12,310 --> 00:04:15,010
And the target is the hardware for which the application is built.

56
00:04:15,040 --> 00:04:21,590
In our case, that's the ESP 32, and some things that are not part of the project is the ESP IDF itself.

57
00:04:21,610 --> 00:04:27,520
Instead, it is standalone and linked into the project via the IDF path environment variable, which

58
00:04:27,520 --> 00:04:29,920
holds the path of the ESP IDF directory.

59
00:04:30,130 --> 00:04:35,420
This allows the IDF framework to be decoupled from your project in the path where mine is installed

60
00:04:35,420 --> 00:04:38,980
this year and yours may be similar depending on your installation.

61
00:04:39,340 --> 00:04:42,640
Also, the toolchain for compilation is not part of the project.

62
00:04:42,670 --> 00:04:47,590
The toolchain should be installed in the system command line path which is taken care of by the all

63
00:04:47,590 --> 00:04:50,770
in one installation you've already completed in the previous lesson.

64
00:04:52,210 --> 00:04:52,480
All right.

65
00:04:52,480 --> 00:04:56,140
So here are the different methods of using the build system and we'll start with IDF.

66
00:04:56,140 --> 00:05:02,500
PY The IDF py command line tool provides a frontend for easily managing your project builds and it manages

67
00:05:02,500 --> 00:05:03,670
the following tools.

68
00:05:03,820 --> 00:05:07,090
It manages CMYK which configures the project to be built in.

69
00:05:07,090 --> 00:05:10,180
The link here will take you to the C make page and see.

70
00:05:10,330 --> 00:05:15,520
It could easily be another course on its own, but in general Mark is used to control the software compilation

71
00:05:15,520 --> 00:05:22,210
process and we'll get to know the basics by using the C make lists txt files as we progress in the course.

72
00:05:22,810 --> 00:05:28,930
In another tool managed by EDF Pius Ninja, which builds the project and Ninja, it's a small build

73
00:05:28,930 --> 00:05:33,850
system with the focus on speed and it differs from other build systems in two major respects.

74
00:05:33,850 --> 00:05:39,010
It is designed to have its input files generated by a higher level build system and it is designed to

75
00:05:39,010 --> 00:05:40,840
run builds as fast as possible.

76
00:05:40,840 --> 00:05:44,530
And for our purposes in this course, that's really all we need to know about Ninja.

77
00:05:45,310 --> 00:05:52,840
And ESP toolkit PY is used for flashing the target and it's a python based open source platform independent

78
00:05:52,840 --> 00:05:56,440
utility to communicate with the ROM bootloader and expressive chips.

79
00:05:57,100 --> 00:05:59,470
And then there's the option to use Quake directly.

80
00:05:59,530 --> 00:06:04,540
And it's mentioned here that IDF dot pie is a wrapper around C make for convenience.

81
00:06:04,660 --> 00:06:10,870
For example, when EDF Pi does something, it prints each command that it runs for easy reference.

82
00:06:10,870 --> 00:06:17,950
For example, the EDF Pi build command is the same as running these commands in a bash shell or similar

83
00:06:17,950 --> 00:06:19,720
commands for Windows Command prompt.

84
00:06:20,260 --> 00:06:26,530
But the way that we're going to use the build system, including CMYK Ninja and the ESP tool PY is by

85
00:06:26,530 --> 00:06:32,200
simply using the expressive ID, so we'll be able to build flash and monitor the application directly

86
00:06:32,200 --> 00:06:34,600
from the eclipse based expressive ID.

87
00:06:35,370 --> 00:06:40,140
And even though the ID offers us a lot of convenience, we still have to set up the C make list files

88
00:06:40,140 --> 00:06:43,260
properly to tell the build system how to build the project.

89
00:06:43,290 --> 00:06:48,210
The documentation here shows with an example project directory tree might look like, which contains

90
00:06:48,210 --> 00:06:52,920
the following elements, including a top level project c make list txt file.

91
00:06:53,040 --> 00:06:58,170
And this is the primary file which C make uses to learn how to build the project and may set project

92
00:06:58,170 --> 00:06:58,440
wide.

93
00:06:58,440 --> 00:06:59,550
C Make variables.

94
00:06:59,790 --> 00:07:05,280
It includes the file project that C make which implements the rest of the build system and it also sets

95
00:07:05,280 --> 00:07:12,320
the project name and defines the project and the sdhc config project configuration file is created slash

96
00:07:12,390 --> 00:07:18,030
updated when the IDF py menu config runs and it holds the configuration for all the components in the

97
00:07:18,030 --> 00:07:20,940
project, including the ESP, IDF itself.

98
00:07:21,390 --> 00:07:27,000
And as I mentioned, we can configure all components by accessing the Sdhc config here directly from

99
00:07:27,000 --> 00:07:27,750
the ID.

100
00:07:28,850 --> 00:07:33,800
Then there is the optional components directory which contains components that are part of the project,

101
00:07:33,800 --> 00:07:38,870
and the project does not have to contain custom components, but it can be useful for structuring reusable

102
00:07:38,870 --> 00:07:43,440
code or including third party components that aren't part of the ESP ADF.

103
00:07:43,460 --> 00:07:49,910
And again, here's an example of this within the ESP ADF Lib Sensors library where there are many components

104
00:07:49,910 --> 00:07:56,030
and within the BM six eight folder, you have the source files and C make this file which is a similar

105
00:07:56,030 --> 00:07:58,820
structure to what's shown in the impressive documentation.

106
00:07:59,390 --> 00:08:04,730
And in fact it's mentioned here that the component directories each contain a component C make list,

107
00:08:04,850 --> 00:08:11,300
txt file and this file contains variable definitions to control the build process of the component and

108
00:08:11,300 --> 00:08:13,340
its integration into the overall project.

109
00:08:13,670 --> 00:08:18,590
We also have the main directory, which is a special component that contains source code for the project

110
00:08:18,590 --> 00:08:19,250
itself.

111
00:08:19,370 --> 00:08:24,170
And in fact we'll add most of our new files here and we also have the build directory where the build

112
00:08:24,170 --> 00:08:27,590
output is created and this directory is created by RDF.

113
00:08:27,590 --> 00:08:33,680
PY if it doesn't already exist and Cimatu configures the project and generates interim build files here,

114
00:08:33,830 --> 00:08:39,830
then after the main build process is run, it will also contain interim object files and libraries as

115
00:08:39,830 --> 00:08:41,990
well as the final binary output files.

116
00:08:42,820 --> 00:08:47,860
And just briefly about the config project build file, this file allows you to include configuration

117
00:08:47,860 --> 00:08:48,550
options.

118
00:08:48,550 --> 00:08:52,810
And instead of reading this because it might be a little confusing, I'll just give you a preview of

119
00:08:52,810 --> 00:08:54,280
how it's used here.

120
00:08:54,280 --> 00:08:59,230
We have a cake and fig project build file with the menu option called example configuration.

121
00:08:59,230 --> 00:09:05,740
And from the sdhc config we have these defines available to us there which can be used from the source

122
00:09:05,740 --> 00:09:09,910
code and you'll see how this works in the sensor library integration section.

123
00:09:10,770 --> 00:09:11,010
All right.

124
00:09:11,010 --> 00:09:13,530
So let's come back to the Project Chemicals file.

125
00:09:13,800 --> 00:09:18,810
If we recall this top level C make list file contains build settings for the entire project.

126
00:09:18,990 --> 00:09:22,290
And at a minimum, this file should contain these mandatory parts.

127
00:09:22,530 --> 00:09:27,390
The C make minimum required version command tell c make the minimum version that is required to build

128
00:09:27,390 --> 00:09:28,140
the project.

129
00:09:28,440 --> 00:09:34,740
The PDF is designed to work with C make 3.16 or newer and this line must be the first line in the c

130
00:09:34,770 --> 00:09:35,370
make list.

131
00:09:35,490 --> 00:09:36,570
TXT file.

132
00:09:36,930 --> 00:09:41,970
Then there's the include project at c make line which pulls in the rest of the C, make functionality

133
00:09:41,970 --> 00:09:47,580
to configure the project and discover all components, etc. and we also have the project command in

134
00:09:47,580 --> 00:09:52,860
this command creates the project itself and specifies the project name and the project name is used

135
00:09:52,860 --> 00:09:58,110
for the final binary output files of the application that is the Elf and Bin files.

136
00:09:58,620 --> 00:10:03,960
In this example here, the project command takes the Project ID, which is derived from these commands,

137
00:10:03,960 --> 00:10:09,690
which gives us the project name here as the project ID in this action specifies the name of the final

138
00:10:09,690 --> 00:10:11,130
binary output files.

139
00:10:11,130 --> 00:10:16,950
As mentioned in the documentation, you also have optional project variables and if you're interested,

140
00:10:16,980 --> 00:10:19,740
you could take a look at the implementation of each of these.

141
00:10:19,740 --> 00:10:25,650
But the one that we'll actually use in the course is extra component diers and this project variable

142
00:10:25,650 --> 00:10:31,170
provides an optional list of additional directories to search for components and paths can be relative

143
00:10:31,170 --> 00:10:33,300
to the project directory or absolute.

144
00:10:33,360 --> 00:10:38,520
For example, in the upcoming Sensor Library Integration section will include the library using the

145
00:10:38,520 --> 00:10:45,870
set command to the ESP Lib Slash Components folder with the path relative to the project directory.

146
00:10:46,470 --> 00:10:51,780
And the documentation recommends that the set commands be placed after the C make minimum line, but

147
00:10:51,780 --> 00:10:54,360
before the include line as shown here.

148
00:10:55,820 --> 00:10:56,750
For our list.

149
00:10:56,750 --> 00:11:02,390
File in main, we're going to use a minimal component to make lists file and to provide you with context.

150
00:11:02,390 --> 00:11:03,440
Here's an example.

151
00:11:04,300 --> 00:11:11,110
This scene make list txt file in domain is used to register the source or c files and the includes to

152
00:11:11,110 --> 00:11:11,920
be compiled.

153
00:11:12,280 --> 00:11:18,130
So this minimal component C make list file simply registers the component to the build system using

154
00:11:18,130 --> 00:11:23,110
EDF component register and the documentation provides definitions for these arguments.

155
00:11:23,440 --> 00:11:26,500
After sources, we'll add our source files throughout the course.

156
00:11:26,680 --> 00:11:30,160
Then for include dirs we'll use for our includes and requires.

157
00:11:30,160 --> 00:11:32,080
We won't use, at least not yet.

158
00:11:32,080 --> 00:11:37,090
And it's not required to use this, but it's very often required to declare what other components this

159
00:11:37,090 --> 00:11:38,290
component will use.

160
00:11:38,710 --> 00:11:40,840
And you can follow this link here to learn more.

161
00:11:41,700 --> 00:11:43,530
And don't worry if this all seems confusing.

162
00:11:43,530 --> 00:11:48,630
Now, once we're updating the make list files and project configuration throughout the course, it will

163
00:11:48,630 --> 00:11:49,560
all come together.

164
00:11:50,250 --> 00:11:53,760
So let's continue to the next lesson and set up the project template.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,980 --> 00:00:09,470
OK, so let's start the SPDR eclipse.

2
00:00:11,430 --> 00:00:15,810
And launch from the workspace we'd previously chosen, by the way.

3
00:00:15,840 --> 00:00:20,250
Now you can connect your dev kit and turn it on, give you clips a moment to start.

4
00:00:21,180 --> 00:00:22,530
And now let's maximize.

5
00:00:24,270 --> 00:00:27,120
And close this welcome tab and go to file.

6
00:00:28,410 --> 00:00:28,830
New.

7
00:00:30,200 --> 00:00:36,770
Impressive IDF project in so-called the project, you, Demi, underscore ESP 32.

8
00:00:37,830 --> 00:00:38,760
And click finish.

9
00:00:43,520 --> 00:00:48,200
Now, close out the read me, and for the launch target, choose ESP 32.

10
00:00:48,950 --> 00:00:50,660
And while we're here, let's set the computer.

11
00:00:52,060 --> 00:00:56,650
And I have the rover Typekit connected, so I have two components here, and I'll just choose the higher

12
00:00:56,650 --> 00:00:57,010
number.

13
00:00:57,640 --> 00:01:02,350
If you don't have the rover kit, just choose the single port shown and then click finish.

14
00:01:04,940 --> 00:01:08,630
Expand the project files and go into the see make lists here.

15
00:01:09,730 --> 00:01:11,380
And change the project name to.

16
00:01:12,460 --> 00:01:16,390
You, Demi, underscore SPF 30 to underscore at.

17
00:01:17,830 --> 00:01:20,920
And this will be the name of the application binary produced by the build.

18
00:01:22,210 --> 00:01:26,320
Next, let's expand the main folder and go to this see make list file.

19
00:01:27,430 --> 00:01:28,780
And let's get rid of all of this.

20
00:01:30,470 --> 00:01:33,800
And dead IDF component register.

21
00:01:35,780 --> 00:01:36,920
And then add sources.

22
00:01:39,520 --> 00:01:40,450
I mean, that scene.

23
00:01:42,630 --> 00:01:46,440
And let's also Ed include underscore deer's.

24
00:01:47,770 --> 00:01:51,400
With the period between quotations and close parentheses.

25
00:01:54,210 --> 00:01:55,530
Now, let's go to mean that sea.

26
00:01:57,920 --> 00:01:59,000
And let's clean this up.

27
00:01:59,840 --> 00:02:01,010
Let's just delete this.

28
00:02:02,950 --> 00:02:04,510
And all of this here as well.

29
00:02:09,870 --> 00:02:11,010
And delete this as well.

30
00:02:13,400 --> 00:02:14,810
And we can leave it like this for now.

31
00:02:16,410 --> 00:02:17,430
Now go to project.

32
00:02:19,530 --> 00:02:22,920
And build all, you can also use control, be as shown.

33
00:02:24,890 --> 00:02:29,300
And by building the project, we're going to generate what's called an SDK config file.

34
00:02:29,870 --> 00:02:34,880
The SDK config contains the project configuration that will need to adjust based on the project needs.

35
00:02:35,940 --> 00:02:41,340
Also, there is one error that may arise depending on your version of the SPF that will need to resolve

36
00:02:41,340 --> 00:02:43,260
by adjusting the SDK config file.

37
00:02:44,890 --> 00:02:50,260
So just give the build a moment to finish, and I'll point out this air here regarding the invalid certificate.

38
00:02:58,540 --> 00:03:01,090
So here's the error, and we'll resolve it shortly.

39
00:03:01,780 --> 00:03:04,810
For now, let's just open up the SDK config.

40
00:03:13,490 --> 00:03:18,860
And the first thing we'll need to do is go to serial flasher config and change the flash size to four

41
00:03:18,860 --> 00:03:19,460
megabytes.

42
00:03:21,700 --> 00:03:23,290
Next, go to Partition Table.

43
00:03:25,590 --> 00:03:31,650
And change it to factory up to 0.8 definitions, and that's to enable OTA updates.

44
00:03:32,400 --> 00:03:34,860
And then let's go down to HTP Server.

45
00:03:36,210 --> 00:03:40,860
And change, the MAX http request had a link to one thousand twenty four.

46
00:03:42,520 --> 00:03:44,140
As well as the Max, your length.

47
00:03:46,410 --> 00:03:49,950
Next, let's solve the certificate issue by going to embed tools.

48
00:03:51,960 --> 00:03:52,680
And choose.

49
00:03:53,830 --> 00:03:55,900
Use only the most common certificates.

50
00:03:59,320 --> 00:04:01,060
Now we'll do controls to save.

51
00:04:02,300 --> 00:04:03,470
And go to build the project.

52
00:04:08,550 --> 00:04:10,260
Just give the project a minute to build.

53
00:04:18,520 --> 00:04:20,260
And we can ignore this warning here.

54
00:04:22,180 --> 00:04:22,990
And it looks good.

55
00:04:23,140 --> 00:04:23,530
Great.

56
00:04:23,890 --> 00:04:27,550
So now let's flash the deficit by hitting the green arrow in the top left corner.

57
00:04:31,380 --> 00:04:33,400
And now the image is being written to the deficit.

58
00:04:35,690 --> 00:04:36,470
And all looks good.

59
00:04:38,490 --> 00:04:42,000
So I've updated the project configuration lesson to include one more step.

60
00:04:43,130 --> 00:04:47,930
After progressing into the development of this application, I noticed that the ESP log information

61
00:04:47,930 --> 00:04:52,010
macro wasn't recognized by the IEEE, and these red squiggly lines appeared.

62
00:04:52,610 --> 00:04:54,380
The application itself isn't affected.

63
00:04:54,710 --> 00:04:56,000
However, I wanted to get rid of them.

64
00:04:56,900 --> 00:04:57,920
So let's do that now.

65
00:04:58,580 --> 00:04:59,630
Let's go to project.

66
00:05:00,580 --> 00:05:01,300
Properties.

67
00:05:03,160 --> 00:05:06,190
And under C C++ general go to indexer.

68
00:05:09,220 --> 00:05:16,180
And to change, the default options will check enable project specific settings and then Check Index

69
00:05:16,180 --> 00:05:17,260
all had a variance.

70
00:05:20,040 --> 00:05:23,990
And also check index source and --'s opened in the editor.

71
00:05:24,960 --> 00:05:25,560
And that's it.

72
00:05:26,190 --> 00:05:27,360
So let's apply in close.

73
00:05:28,880 --> 00:05:29,720
And if we build.

74
00:05:33,880 --> 00:05:34,480
They go away.

75
00:05:35,540 --> 00:05:35,850
Great.

76
00:05:35,870 --> 00:05:36,770
That looks much better.

77
00:05:38,920 --> 00:05:40,660
All right, so I'll see you in the upcoming lessons.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
==================================================================================

# Section 4: Supplemental Lessons

1
00:00:06,780 --> 00:00:12,180
In this lesson, we'll review how to access the example projects from oppressive via the API reference

2
00:00:12,180 --> 00:00:13,140
and via GitHub.

3
00:00:13,560 --> 00:00:19,500
Also, we'll use the SPF eclipse to access and build and flash an example from the SPF.

4
00:00:20,490 --> 00:00:27,030
OK, so if you're new to using the SPF 30 two and or the SPF, the example projects can help you get

5
00:00:27,030 --> 00:00:32,430
started as they demonstrate features and provide code that you can adapt for your own projects.

6
00:00:33,060 --> 00:00:37,830
OK, so I'm standing on the programming side now, and I'll just head over to the API reference.

7
00:00:39,640 --> 00:00:40,900
And this is the complete list.

8
00:00:41,290 --> 00:00:45,970
And later, we'll go through the API reference of various features relevant to the application, we're

9
00:00:45,970 --> 00:00:53,140
developing the API reference often or perhaps always includes links to ESP IDF examples.

10
00:00:53,590 --> 00:00:55,900
For example, if we go over to Ethernet.

11
00:00:57,850 --> 00:01:04,360
We see that code examples for the Ethernet API are provided in the Ethernet directory of the Aespa RDF

12
00:01:04,360 --> 00:01:04,990
examples.

13
00:01:05,350 --> 00:01:06,370
So let's follow that.

14
00:01:09,020 --> 00:01:12,140
And here are the Ethernet examples, and the read me with details.

15
00:01:12,740 --> 00:01:15,620
This is a depressives GitHub for the Aespa PDF.

16
00:01:16,070 --> 00:01:21,380
And if you open the link in the resources that I've provided called expressive ESP, IDF GitHub.

17
00:01:23,310 --> 00:01:27,150
Which is here you'll find the full list of example projects.

18
00:01:28,680 --> 00:01:35,190
OK, so another convenient way to access the examples is directly from the SPF eclipse, you have created

19
00:01:35,190 --> 00:01:40,260
a separate workspace just to demonstrate how to access the examples so you don't have to do what I'm

20
00:01:40,260 --> 00:01:40,830
doing now.

21
00:01:41,490 --> 00:01:43,290
So first, I'll close this welcome tab.

22
00:01:45,150 --> 00:01:46,500
And then I'll go to file.

23
00:01:48,230 --> 00:01:48,680
New.

24
00:01:50,020 --> 00:01:51,580
Oppressive IDF project.

25
00:01:53,320 --> 00:01:54,700
And then I'll give it a name.

26
00:01:56,220 --> 00:01:57,270
And then click next.

27
00:01:59,600 --> 00:02:01,970
And I'll just maximize this so you can see it better.

28
00:02:04,420 --> 00:02:09,940
And then if I check this box, create a project using one of the templates, we can access the examples

29
00:02:09,940 --> 00:02:12,430
directly and create the project in Eclipse.

30
00:02:13,000 --> 00:02:15,610
So all the examples are here, including peripherals.

31
00:02:17,130 --> 00:02:21,390
But I'll just load the Blink project swell, select it, then click Finish.

32
00:02:25,720 --> 00:02:28,900
And first, update, the target to ESP 30 to.

33
00:02:30,380 --> 00:02:32,030
And then I'll select the serial port.

34
00:02:33,240 --> 00:02:34,350
From my rover dev kit.

35
00:02:38,250 --> 00:02:40,200
So I'll just expand the project files.

36
00:02:42,570 --> 00:02:44,130
And I'll open the blinkered see.

37
00:02:48,500 --> 00:02:52,160
An update, the Blink GPIO to one of the LEDs on my death kit.

38
00:02:54,770 --> 00:02:56,120
And then I'll build the project.

39
00:02:58,360 --> 00:03:03,490
And we want to build now so that we can generate the SDK config file so that we can make the change

40
00:03:03,490 --> 00:03:04,600
regarding the certificate.

41
00:03:06,730 --> 00:03:09,040
OK, so now the SDK config is generated.

42
00:03:09,550 --> 00:03:12,490
So now let's do the update regarding the certificate.

43
00:03:20,410 --> 00:03:23,680
And we'll say use only the most common certificate.

44
00:03:26,610 --> 00:03:27,870
And then now we can rebuild.

45
00:03:35,440 --> 00:03:37,330
OK, so now I'll flash the example.

46
00:03:39,680 --> 00:03:44,480
And now I can see that the red lady on my death kit is blinking based on the interval from the example.

47
00:03:45,390 --> 00:03:48,810
All right, and also, we can open a monitor to view the print messages.

48
00:03:57,080 --> 00:04:01,790
And we see the lead turning off and then turning on over and over based on the interval.

49
00:04:02,420 --> 00:04:02,810
All right.

50
00:04:02,810 --> 00:04:03,560
So there you have it.

51
00:04:04,130 --> 00:04:06,260
So that's all for now and see you in the next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,680 --> 00:00:09,140
All right, so continuing with the supplemental lessons.

2
00:00:09,320 --> 00:00:15,110
Let's briefly review the ESP IDF Riotous as a precursor to what's to come in the application development

3
00:00:15,110 --> 00:00:15,650
lessons.

4
00:00:16,220 --> 00:00:20,240
So the scope of this lesson won't be too exhaustive and will be limited to the following.

5
00:00:20,540 --> 00:00:25,310
I'll show you where to find documentation if you want to go more in-depth into free photos, and then

6
00:00:25,310 --> 00:00:31,100
we'll review some differences from the ESP IDF version of free autos with the vanilla or regular free

7
00:00:31,100 --> 00:00:31,670
autos.

8
00:00:32,120 --> 00:00:39,020
And then we'll take a look at Teske states test creation and the X Test Create Penta Core API and the

9
00:00:39,020 --> 00:00:40,550
V task delay as well.

10
00:00:40,910 --> 00:00:42,230
All right, so let's jump right in.

11
00:00:42,860 --> 00:00:48,680
OK, so in the case that you're new to free autos, Free Autos is a real time operating system kernel

12
00:00:48,680 --> 00:00:54,650
for embedded devices, and the following page from free auto storage provides a clear description of

13
00:00:54,650 --> 00:00:55,370
an arthouse.

14
00:00:56,360 --> 00:01:02,570
So to summarize, the scheduler in a Real-Time Operating System is designed to provide a predictable

15
00:01:02,570 --> 00:01:08,480
execution pattern, and often embedded systems have real time requirements, which means that they must

16
00:01:08,480 --> 00:01:12,650
respond to a certain event within a strictly defined time or deadline.

17
00:01:12,950 --> 00:01:18,740
The guarantee to meet these requirements can only be made if the behavior of the operating system scheduler

18
00:01:18,740 --> 00:01:21,050
can be predicted or is deterministic.

19
00:01:21,620 --> 00:01:22,010
All right.

20
00:01:22,430 --> 00:01:27,590
So you may want to bookmark this link for the free or books available from Free Autostart.

21
00:01:27,590 --> 00:01:28,370
Org here.

22
00:01:29,400 --> 00:01:31,710
They're nice to have as an additional resource.

23
00:01:32,250 --> 00:01:38,850
And if you go to the free those fundamentals link, you'll find that this page contains background information

24
00:01:38,850 --> 00:01:43,710
on multitasking and basic real time concepts, which is intended for beginners.

25
00:01:44,070 --> 00:01:47,520
So if you want to get more into theory, this is also a good resource.

26
00:01:48,150 --> 00:01:53,670
Additionally, you can find impressive documentation about their version of Free Artus by following

27
00:01:53,670 --> 00:01:56,430
this link, and we'll take a look at parts of that shortly.

28
00:01:57,180 --> 00:02:03,240
OK, so there are a few apparent differences between the aespa, ID3 autos and the regular or vanilla

29
00:02:03,240 --> 00:02:06,120
free autos that affect the application development.

30
00:02:06,450 --> 00:02:12,300
Firstly, the ESP 32 extends the MCU contains two extensive processor cores.

31
00:02:13,760 --> 00:02:20,660
And the IDF uses its own version of the extensive port of frittatas, which provides multicore support.

32
00:02:21,020 --> 00:02:26,480
And so in the case that you are already familiar with free autos, but not the IDF version, we do not

33
00:02:26,480 --> 00:02:32,440
have to call the V task start schedule or API when using the ESP IDF free autos.

34
00:02:32,870 --> 00:02:39,860
Also, the free autos task stack size is specified in bytes when using the IDF, not words as you would

35
00:02:39,860 --> 00:02:41,420
do with regular free autos.

36
00:02:41,870 --> 00:02:47,330
Additionally, the application Start-Up Flow is relevant here, which covers everything that happens

37
00:02:47,330 --> 00:02:53,870
after the application starts executing and before the main function starts running inside the main task.

38
00:02:54,140 --> 00:02:57,860
You can find details here with a high level view of the startup.

39
00:02:57,860 --> 00:03:00,410
Process is described first.

40
00:03:00,590 --> 00:03:07,010
The first stage bootloader and rom loads the second stage bootloader image to RAM from the Flash Offset

41
00:03:07,040 --> 00:03:09,320
Hex one thousand and the second step.

42
00:03:09,800 --> 00:03:14,990
The second stage bootloader loads the partition table and the main application image from Flash.

43
00:03:15,290 --> 00:03:20,570
The main application incorporates both RAM segments and read on these segments via flash cache.

44
00:03:21,080 --> 00:03:27,560
Then the application startup executes, and at this point, the second CPU and auto scheduler are started.

45
00:03:28,010 --> 00:03:32,240
You can read up on the details of each of these steps, so feel free to come here if you're interested.

46
00:03:32,540 --> 00:03:35,720
But for now, let's go over to the application startup details.

47
00:03:36,530 --> 00:03:41,900
And so everything that happens after the application starts and before the app main is called involves

48
00:03:41,900 --> 00:03:48,110
the following port initialization of hardware and Basic C runtime environment system, initialization

49
00:03:48,110 --> 00:03:53,570
of software services and free autos, and running the main task and calling App Main, which will be

50
00:03:53,570 --> 00:03:55,100
our application entry point.

51
00:03:55,550 --> 00:03:59,810
All right, so I think that's enough details about the application startup for purposes.

52
00:04:00,840 --> 00:04:06,570
OK, so in another toast implementation of a design, the program is divided into different tasks and

53
00:04:06,570 --> 00:04:09,930
each task runs continuously in an infinite loop.

54
00:04:10,470 --> 00:04:15,270
OK, so we can create free toast tasks using the X test, create APIs.

55
00:04:15,630 --> 00:04:20,250
And to do that, we'll need to include free autos, slash tasks, storage.

56
00:04:20,730 --> 00:04:22,950
And there are two API options available.

57
00:04:23,310 --> 00:04:30,540
We can use X Test Create, which lets the ESP IDF riotous choose which core of the ESP thirty two to

58
00:04:30,540 --> 00:04:31,710
the task should run on.

59
00:04:32,460 --> 00:04:37,980
Then this is the basic structure of a free toast task with an infinite loop as the main body of the

60
00:04:37,980 --> 00:04:38,490
task.

61
00:04:39,090 --> 00:04:42,330
And here the X Task Create API creates the task.

62
00:04:43,220 --> 00:04:49,760
And so its task rate pinned to core allows specifying which core the tasks should run on in the next.

63
00:04:49,790 --> 00:04:52,580
I'll summarize the description of the API parameters.

64
00:04:53,450 --> 00:04:59,870
All right, the first parameter PV test code is the custom C function or riotous task that runs in an

65
00:04:59,870 --> 00:05:00,560
infinite loop.

66
00:05:01,010 --> 00:05:06,740
And PC name is the descriptive name that you can give a task and is only used as a debugging aid.

67
00:05:07,160 --> 00:05:12,770
US stack depth is the memory and bytes that should be allocated by the kernel to the task.

68
00:05:13,190 --> 00:05:18,530
PV parameters is an optional parameter that is a pointer that can be used by the task.

69
00:05:18,920 --> 00:05:25,430
UX priority is the priority at which the task should run on in the higher priority number takes precedence

70
00:05:25,910 --> 00:05:31,760
and P created task is an optional task handle by which the created task can be referenced.

71
00:05:32,120 --> 00:05:38,870
For example, if you need to use various free auto KPIs like V Task Delete, as shown here with the

72
00:05:38,870 --> 00:05:40,460
task handle is referenced.

73
00:05:41,760 --> 00:05:49,290
And then core idea is the core of the ESP 32 that the task is to be assigned to, which can be core

74
00:05:49,290 --> 00:05:50,820
zero or core one.

75
00:05:52,160 --> 00:05:57,320
And this link will take you to a description of task states as well as a state transition diagram.

76
00:05:58,320 --> 00:06:03,090
OK, so let's take a look at the state diagram, and I'll briefly summarize the tasks states.

77
00:06:03,630 --> 00:06:09,360
So the running state means that the task is executing and utilizing the processor and the ready state

78
00:06:09,360 --> 00:06:15,780
here means that the task is able to execute but is not currently running because the task with an equal

79
00:06:15,780 --> 00:06:17,820
or higher priority is currently running.

80
00:06:18,270 --> 00:06:22,200
So if a task is blocked, this can be caused by a temporal event.

81
00:06:22,200 --> 00:06:28,410
For example, a call to V task delay that causes the task to be placed into the block state until the

82
00:06:28,410 --> 00:06:29,910
delay period has expired.

83
00:06:30,300 --> 00:06:34,950
Or it can be blocked due to an external event, which means that the task is waiting to receive from

84
00:06:34,950 --> 00:06:38,520
a Q event group or notification or a similar event.

85
00:06:38,940 --> 00:06:45,060
And this differs from tasks in the suspended state where there is no timeout in tasks only enter and

86
00:06:45,060 --> 00:06:52,860
exit the suspended state when explicitly commanded to do so using V tasks suspend and X task resume

87
00:06:52,860 --> 00:06:53,880
API calls.

88
00:06:54,180 --> 00:06:54,570
All right.

89
00:06:55,020 --> 00:06:55,980
And these are linked.

90
00:06:56,010 --> 00:06:58,140
So feel free to read up on those as well.

91
00:06:59,180 --> 00:07:05,030
And about Vitesse DeLay, it's used to send a task into the black state for a set number of ticks.

92
00:07:05,570 --> 00:07:11,840
The actual time that the task remains blocked depends on the tick rate and the constant port tick period.

93
00:07:11,840 --> 00:07:15,980
Milliseconds can be used to calculate real time from the tick rate.

94
00:07:16,310 --> 00:07:23,810
For example, if the free tortoise tick rate in the SDK config is set to 100 hertz as it's shown here,

95
00:07:24,530 --> 00:07:32,510
then this port tick period is 10 milliseconds and 500 divided by 10 is 50 ticks, which is what we passed

96
00:07:32,510 --> 00:07:35,160
to test delay and that is x delay.

97
00:07:35,180 --> 00:07:41,090
In this example, and with 50 ticks at a period of 10 milliseconds, we end up with the five hundred

98
00:07:41,090 --> 00:07:42,110
millisecond delay.

99
00:07:43,290 --> 00:07:45,840
All right, so that's it for this quick overview of free autos.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,490 --> 00:00:11,300
So error handling is important to consider when creating a robust application.

2
00:00:11,300 --> 00:00:14,430
And here we'll cover error handling using the ESP ADF.

3
00:00:15,380 --> 00:00:20,450
And we'll start with an overview of error handling and then we'll talk about error codes, converting

4
00:00:20,450 --> 00:00:26,990
error codes to error messages using the ESP Error Check macro and error handling patterns or strategies

5
00:00:26,990 --> 00:00:29,030
that you may want to consider in your development.

6
00:00:29,690 --> 00:00:33,170
So to get started, let's take a look at the impressive documentation.

7
00:00:33,380 --> 00:00:36,320
So the errors we're discussing here are runtime errors.

8
00:00:36,320 --> 00:00:41,210
And again, handling these errors is an important aspect of developing robust applications.

9
00:00:41,720 --> 00:00:44,300
And we can have a couple of different types of errors.

10
00:00:44,300 --> 00:00:49,790
The first type mentioned here are categorized as recoverable errors, which are errors indicated by

11
00:00:49,790 --> 00:00:52,940
functions through return values or error codes.

12
00:00:53,390 --> 00:00:59,960
Unrecoverable or fatal errors can result from failed assertions, for example, using the assert macro

13
00:00:59,960 --> 00:01:01,430
and equivalent methods.

14
00:01:01,430 --> 00:01:07,310
And if we follow the assertions link, you may be familiar with the assert function defined in assert

15
00:01:07,310 --> 00:01:13,610
dot h, but when asserting a value of the type esp error type is equal to ESP OC.

16
00:01:13,640 --> 00:01:17,270
The ESP error check macro is used instead of assert.

17
00:01:18,110 --> 00:01:24,110
And so CPU exceptions are considered fatal, which could be access to protected regions of memory,

18
00:01:24,140 --> 00:01:26,180
illegal instructions, etc..

19
00:01:26,420 --> 00:01:32,840
Then you also have system level checks like watchdog timeout cache access, error, stack overflow,

20
00:01:32,840 --> 00:01:39,920
stack smashing heap corruption, etc. And this guide explains ESP IDF error handling mechanisms related

21
00:01:39,920 --> 00:01:44,090
to recoverable errors and provide some common error handling patterns.

22
00:01:44,090 --> 00:01:47,150
And I'll show you some patterns used in the course source code as well.

23
00:01:47,450 --> 00:01:51,860
And you could always check out this link for instructions on diagnosing unrecoverable errors.

24
00:01:52,490 --> 00:01:57,830
And you may want to mark this as a favorite in your ESP 32 resources as you're eventually bound to run

25
00:01:57,830 --> 00:02:01,010
into the panic handler which handles these fatal errors.

26
00:02:01,860 --> 00:02:03,840
So let's move on to our codes.

27
00:02:04,110 --> 00:02:09,750
Most ESP specific functions use ESP error type to return error codes.

28
00:02:10,560 --> 00:02:19,710
And ESP type is assigned integer type, which you can find in the esp h file from the ESP and success

29
00:02:19,710 --> 00:02:25,230
or no error is indicated with the ESP code, which is defined as zero.

30
00:02:25,950 --> 00:02:32,610
And common error codes for generic failures like out of memory, invalid argument and timeout etc. are

31
00:02:32,610 --> 00:02:33,840
defined here as well.

32
00:02:34,410 --> 00:02:39,100
And you also have other error codes defined in various ESP EDF header files.

33
00:02:39,120 --> 00:02:43,320
Also using preprocessor defines starting with the ESP prefix.

34
00:02:43,350 --> 00:02:49,530
For example, there are NVS related error codes defined in the nonvolatile storage file, and here the

35
00:02:49,530 --> 00:02:55,590
ESP error NVS base is defined as the starting number for the error codes and then each subsequent error

36
00:02:55,590 --> 00:02:57,900
code is defined as an offset from the base.

37
00:02:58,910 --> 00:03:04,760
And converting codes to error messages can also be useful when debugging by displaying the error messages

38
00:03:04,760 --> 00:03:06,500
as strings on the terminal monitor.

39
00:03:07,070 --> 00:03:14,090
This is possible for each error code defined in ESP ADF components, and the ESP error type can be converted

40
00:03:14,090 --> 00:03:20,870
to an error code name using the ESP error to name or ESP error to name underscore our functions.

41
00:03:20,870 --> 00:03:26,720
For example, we'll use ESP error to name for our non-volatile storage functions and in this example

42
00:03:26,720 --> 00:03:31,430
we call NVS Open, which returns its status to ESP error.

43
00:03:31,640 --> 00:03:39,020
And if it didn't return successful or ESP OC, we can then use ESP error to name and display its result

44
00:03:39,020 --> 00:03:41,210
using print def or esp log.

45
00:03:41,960 --> 00:03:46,430
So if you want to find out the exact reason that a function fails, try using these functions.

46
00:03:46,880 --> 00:03:52,640
And the way it works is, is it finds the error code in a pre generated lookup table and returns it

47
00:03:52,640 --> 00:03:54,020
string representation.

48
00:03:54,290 --> 00:03:56,930
And here you have the lookup table defined here.

49
00:03:57,730 --> 00:04:04,240
Where each entry in the table is an error code in message pair and ESP error to name underscore r can

50
00:04:04,240 --> 00:04:07,660
be used when you need to also consider system error codes.

51
00:04:07,990 --> 00:04:13,270
So here, if the error code is not found, then str error underscore r is used.

52
00:04:14,480 --> 00:04:21,380
So back to the ESP air check macro, the ESP error check macro checks, the ESP error type value rather

53
00:04:21,380 --> 00:04:22,550
than a bull condition.

54
00:04:22,880 --> 00:04:29,150
And if the argument of ESP error check is not equal to ESP, then the error message is printed on the

55
00:04:29,150 --> 00:04:32,990
console and the abort function is called and on the console.

56
00:04:33,020 --> 00:04:34,880
Your error message will look like this.

57
00:04:35,150 --> 00:04:41,540
So here in the documentation it says that if the ADF monitor is used, addresses in the backtrace will

58
00:04:41,540 --> 00:04:43,850
be converted to file names and line numbers.

59
00:04:44,390 --> 00:04:50,390
And the first line mentions the error code as a hexadecimal value and the identifier used for this error

60
00:04:50,390 --> 00:04:56,360
in the source code and the subsequent lines show the location in the program where ESP Error Check Macro

61
00:04:56,360 --> 00:05:00,650
was called and the expression which was passed to the macro as an argument.

62
00:05:01,160 --> 00:05:06,800
Then the backtrace is printed, which is part of the panic handler output common to all fatal errors.

63
00:05:08,100 --> 00:05:13,500
And if you don't want to abort but still have the convenience of this macro, you can always use the

64
00:05:13,500 --> 00:05:16,020
ESP error check without abort macro.

65
00:05:17,470 --> 00:05:20,200
Now let's review some strategies for handling these errors.

66
00:05:20,500 --> 00:05:23,440
So the documentation recommends the following strategies.

67
00:05:23,650 --> 00:05:25,660
You can first attempt to recover.

68
00:05:25,930 --> 00:05:29,650
And depending on the situation, we may want to try the following methods.

69
00:05:29,890 --> 00:05:35,230
You can retry the call like in the below where the function call is re attempted while the result is

70
00:05:35,230 --> 00:05:35,980
timed out.

71
00:05:36,670 --> 00:05:42,610
Or you can attempt to d initialize the driver and re initialize it again and or fix the error condition

72
00:05:42,610 --> 00:05:44,440
using an out of band mechanism.

73
00:05:44,590 --> 00:05:49,960
For example, reset an external peripheral which is not responding and for an example of where we attempt

74
00:05:49,960 --> 00:05:51,320
to recover from errors.

75
00:05:51,340 --> 00:05:54,760
I'd like to show you the inverse initialization that we use in main.

76
00:05:55,550 --> 00:06:01,730
So here, if the NBS flash init function returns with either of the following errors, then we erase

77
00:06:01,730 --> 00:06:03,440
the flash and re initialize it.

78
00:06:03,980 --> 00:06:09,320
So this is one example of attempting to recover and another possible response would be to propagate

79
00:06:09,320 --> 00:06:10,400
the error to the caller.

80
00:06:10,700 --> 00:06:12,410
And here's an example of that.

81
00:06:14,350 --> 00:06:20,650
And finally, you can designate certain functions as unrecoverable errors by using ESP check.

82
00:06:21,160 --> 00:06:25,750
So you'll need to decide for yourself when using ESP or check makes sense in your application.

83
00:06:26,080 --> 00:06:32,920
As mentioned here, many ESP ADF examples and I often do this myself use ESP error checks to handle

84
00:06:32,920 --> 00:06:39,280
errors from various APIs and this is not the best practice for applications and is done to make example

85
00:06:39,280 --> 00:06:42,930
code more concise so it may be convenient to use.

86
00:06:42,940 --> 00:06:47,500
However, you'll need to put more thought into error handling and apply the appropriate error handling

87
00:06:47,500 --> 00:06:50,530
patterns when you need your firmware to be production ready.

88
00:06:51,400 --> 00:06:51,790
All right.

89
00:06:51,790 --> 00:06:52,890
So that's it for now.

90
00:06:52,900 --> 00:06:54,370
And see you in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,780 --> 00:00:11,580
Before we get into the C programming lessons, I think it's a good idea to quickly review the C coding

2
00:00:11,580 --> 00:00:13,410
style that I'll be using throughout the course.

3
00:00:13,980 --> 00:00:18,930
Many companies and individual programmers have a preferred coding style, so the style that I utilize

4
00:00:18,930 --> 00:00:23,340
in this course may or may not align with the style that you're used to, which is the reason for this

5
00:00:23,340 --> 00:00:24,000
brief lesson.

6
00:00:24,870 --> 00:00:28,250
So let's first focus on the head of file coding style Dot H.

7
00:00:28,920 --> 00:00:33,330
And the first information that we'll include in the header, if required or any includes.

8
00:00:33,870 --> 00:00:37,350
And this example I've included ESP if Dot H.

9
00:00:38,010 --> 00:00:44,190
Next will include any macros and defines, and then we can include any external variables and then type

10
00:00:44,190 --> 00:00:50,280
tips regarding type device will provide a description for the type def and add any special notes if

11
00:00:50,280 --> 00:00:50,910
necessary.

12
00:00:51,540 --> 00:00:54,750
Also, we want to postfix E NUM's with an underscore E.

13
00:00:55,440 --> 00:01:01,470
And similarly, for type def structs, we'll postfix them with an underscore T and at the bottom of

14
00:01:01,470 --> 00:01:04,380
the header files will include any public function prototypes.

15
00:01:04,710 --> 00:01:09,780
We'll add a comment for each prototype that includes a description and any notes, if necessary.

16
00:01:10,320 --> 00:01:15,690
Additionally, we'll include a description for each function parameter as well as the return.

17
00:01:16,050 --> 00:01:18,810
If there is a return and it's a non void function.

18
00:01:19,710 --> 00:01:22,890
Next, let's take a look at the coding style for the C source files.

19
00:01:24,160 --> 00:01:28,060
So at the top of the file, we'll provide any necessary includes for the source file.

20
00:01:28,630 --> 00:01:33,970
First of all, include any standard library header files, such as standard bool for Boolean standard

21
00:01:33,970 --> 00:01:37,750
ale for print def and such in string dates, for example.

22
00:01:38,530 --> 00:01:41,620
Next will include any required header files from the ESP IDF.

23
00:01:42,400 --> 00:01:47,890
The examples I've used here are ESP Log Duddridge, which is used for logging messages to the terminal,

24
00:01:48,370 --> 00:01:53,290
ESB error for error handling and envious flash for non-volatile storage.

25
00:01:53,710 --> 00:01:57,700
Then we can include our application files in here as an example.

26
00:01:57,820 --> 00:01:59,890
We have the coding style h header.

27
00:02:00,670 --> 00:02:01,900
Following the includes.

28
00:02:02,200 --> 00:02:08,320
We can lists any global variables and we'll define them with an underscore prefix and use the static

29
00:02:08,320 --> 00:02:08,920
keyword.

30
00:02:09,310 --> 00:02:14,920
If the variable is restricted for use only within the same file, and so if there are global variables

31
00:02:14,920 --> 00:02:19,210
intended to be used outside of this file, then we won't use the static keyword.

32
00:02:20,180 --> 00:02:25,070
Next, in the source files will include any private or static functions, which are functions that are

33
00:02:25,070 --> 00:02:28,010
restricted for use within the file where they are defined.

34
00:02:28,430 --> 00:02:33,440
We'll include a comment for each static function definition and to specify the function aesthetic.

35
00:02:33,680 --> 00:02:35,450
We'll use the static keyword as shown.

36
00:02:36,260 --> 00:02:41,180
Also, I should mention that if you want to call static functions in the file prior to their definition,

37
00:02:41,630 --> 00:02:43,580
then you'll need to include prototypes for them.

38
00:02:43,910 --> 00:02:47,750
However, I will not do this as this is just the style that I'm used to.

39
00:02:47,990 --> 00:02:53,540
It's perfectly fine to include prototypes for static functions, and many programmers actually do prefer

40
00:02:53,540 --> 00:02:53,690
it.

41
00:02:54,200 --> 00:02:59,390
And another aspect of the coding style is that will prefix the file name to the function name.

42
00:02:59,750 --> 00:03:03,410
For example, the coding style static names shown here.

43
00:03:04,130 --> 00:03:09,350
Additionally, within the comments section for the static function definition, we'll provide a description

44
00:03:09,350 --> 00:03:13,550
for the parameters as well as the return if the function is non void.

45
00:03:14,650 --> 00:03:21,160
Lastly, below the static functions will include any public function definitions, and for these, there

46
00:03:21,160 --> 00:03:24,460
is no need for a description as it's already included in the header file.

47
00:03:25,180 --> 00:03:30,100
All right, so that's it for the briefing on the coding style used, and I'll see you in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Components & Sensors Library  (Optional)

1
00:00:06,510 --> 00:00:10,230
Hello and welcome to the SPF Components Library section.

2
00:00:10,410 --> 00:00:16,710
And in this section I'll introduce the ESP IDF Components Library, which is a library with an abundance

3
00:00:16,710 --> 00:00:22,110
of sensor drivers and drivers for other components that may come in handy in your future projects or

4
00:00:22,110 --> 00:00:23,580
within this course, if you like.

5
00:00:23,580 --> 00:00:29,340
And all of these components and sensor drivers will be at your disposal once we integrate this library

6
00:00:29,340 --> 00:00:31,320
and I'll show you how to get started with it.

7
00:00:32,510 --> 00:00:37,160
So our plan for the lesson includes an introduction to the library and I'll show you how to integrate

8
00:00:37,160 --> 00:00:37,430
it.

9
00:00:37,430 --> 00:00:41,210
And in the next lesson we'll actually do the integration and run an example.

10
00:00:41,210 --> 00:00:46,460
But I should be clear that using this library is completely optional and not necessary to complete the

11
00:00:46,460 --> 00:00:47,090
course.

12
00:00:47,090 --> 00:00:51,020
So you can always come back to this lesson whenever you'd like, if you want to use it.

13
00:00:51,460 --> 00:00:51,740
All right.

14
00:00:51,740 --> 00:00:56,180
So we'll start with the brief introduction of the library to show you where to find the documentation

15
00:00:56,180 --> 00:00:57,200
and examples.

16
00:00:57,200 --> 00:01:02,120
And then we'll take a look at our project structure and where this library fits into it, which will

17
00:01:02,120 --> 00:01:06,590
then lead us into reviewing the steps that will take for the integration, and that will segue us into

18
00:01:06,590 --> 00:01:08,420
the demonstration for the next lesson.

19
00:01:09,770 --> 00:01:13,730
So the components library contains an abundance of drivers for sensors and more.

20
00:01:14,030 --> 00:01:15,440
In the first link here.

21
00:01:16,300 --> 00:01:20,290
Takes you to the SB Lib Components GitHub page.

22
00:01:20,800 --> 00:01:23,050
Here you'll find information to help you get started.

23
00:01:24,000 --> 00:01:26,910
Links to documentation and frequently asked questions.

24
00:01:27,820 --> 00:01:34,390
As well as descriptions for all of the components included in the list is quite extensive and the library

25
00:01:34,390 --> 00:01:38,770
seems to be actively maintained with contributions made by the list of developers here.

26
00:01:39,860 --> 00:01:40,370
All right.

27
00:01:40,370 --> 00:01:42,290
And if we go back to the documentation.

28
00:01:44,440 --> 00:01:45,730
And then follow the link.

29
00:01:48,410 --> 00:01:50,480
And again, first we have how to use it.

30
00:01:52,650 --> 00:01:55,650
Then they provided links for all of the available components.

31
00:01:55,770 --> 00:02:01,290
For example, if we're looking for the BM 680, which is for temperature, humidity as well as pressure.

32
00:02:02,740 --> 00:02:08,230
They provided in-depth information about the sensor as well as documentation about the implementation.

33
00:02:09,110 --> 00:02:15,260
And much like the documentation provided for the SBA itself, they've provided example, usage scenarios

34
00:02:15,260 --> 00:02:17,090
and details about the results.

35
00:02:18,310 --> 00:02:22,200
Measurement settings and other useful information about the beam.

36
00:02:22,210 --> 00:02:23,020
680.

37
00:02:24,160 --> 00:02:30,160
As well as full source code documentation and this is really nicely done and is a great resource.

38
00:02:31,030 --> 00:02:36,250
So now let's go back to the repository and I'll show you where to find the examples from the GitHub

39
00:02:36,250 --> 00:02:36,750
page.

40
00:02:36,760 --> 00:02:42,070
Go to the examples folder, then here you'll find examples for all components which you can use to get

41
00:02:42,070 --> 00:02:42,850
started with.

42
00:02:43,700 --> 00:02:46,690
Now let's take a look at the BMS 680 sensor example.

43
00:02:48,400 --> 00:02:50,440
And there we have everything we need to know.

44
00:02:50,470 --> 00:02:56,830
We see what it does, how to connect the eye, to see serial clock and serial data lines, and then

45
00:02:56,830 --> 00:02:58,510
example code in the main folder.

46
00:03:00,650 --> 00:03:01,910
In not see.

47
00:03:03,010 --> 00:03:04,870
We can simply take this file.

48
00:03:05,140 --> 00:03:11,470
And what I would do is just create a function based on App Main here and integrate it into the application.

49
00:03:12,010 --> 00:03:12,400
All right.

50
00:03:12,400 --> 00:03:14,410
So let's go back up to the main folder.

51
00:03:15,070 --> 00:03:19,540
And what I'm going to do is I'm going to show you how these macros are defined and brought into the

52
00:03:19,540 --> 00:03:20,410
application.

53
00:03:22,150 --> 00:03:22,420
Okay.

54
00:03:22,510 --> 00:03:25,450
So let's go to this k config project build file.

55
00:03:26,410 --> 00:03:32,410
And they've provided this file for us which we can utilize in our project, and it enables access to

56
00:03:32,410 --> 00:03:39,100
define these settings directly from the SDK config menu from the expressive ID and I'll show you how

57
00:03:39,100 --> 00:03:42,460
that works in the next lesson when we integrate the library.

58
00:03:43,850 --> 00:03:47,390
And so that we can visualize where this component fits into our project.

59
00:03:47,780 --> 00:03:51,920
Here's our course project structure without the sensor library component.

60
00:03:53,100 --> 00:03:56,460
And the library will take its place as part of our extra components.

61
00:03:56,670 --> 00:03:59,370
And there are some steps that we'll need to take to achieve this.

62
00:04:00,520 --> 00:04:03,610
And we'll integrate the library by cloning the repository.

63
00:04:03,970 --> 00:04:06,700
And we have the Git Clone Command for that right here.

64
00:04:07,920 --> 00:04:13,860
And we'll also adjust the top level see list, text file, which is the see make list file in the project

65
00:04:13,860 --> 00:04:14,580
folder.

66
00:04:14,940 --> 00:04:19,440
And we'll add this line to include the ESP ADF sensor library component.

67
00:04:20,070 --> 00:04:26,040
Then we'll integrate an example and you can either use mine or choose one from the library itself and

68
00:04:26,040 --> 00:04:31,650
we'll need to adjust the make list file within the main folder to include the example files.

69
00:04:32,220 --> 00:04:39,000
Also, we'll add the K config project build file from the example into the main folder and I'll show

70
00:04:39,000 --> 00:04:41,310
you how that works with the sdhc config.

71
00:04:41,820 --> 00:04:46,470
And lastly, I'll walk you through a few adjustments that will need to make for the application files.

72
00:04:46,740 --> 00:04:52,830
We'll adjust Main C and we'll add this tasks common header file as well, which will eventually add

73
00:04:52,830 --> 00:04:54,600
to your course source files anyway.

74
00:04:56,120 --> 00:05:01,430
So again, any lessons added to this section are completely optional and you can consider these as bonus

75
00:05:01,430 --> 00:05:06,950
lessons as this section will not include step by step programming, since we're simply integrating the

76
00:05:06,950 --> 00:05:09,290
library along with example code.

77
00:05:09,410 --> 00:05:14,720
And the idea here is that you can either use my code directly based on these examples, or you can watch

78
00:05:14,720 --> 00:05:18,280
the lesson to learn by example for inspiration for your own projects.

79
00:05:18,290 --> 00:05:22,490
If you plan on using the library or you can skip these lessons entirely.

80
00:05:23,150 --> 00:05:27,590
So I'll start with the BM 680, which will communicate with override to see.

81
00:05:28,360 --> 00:05:32,920
And I also plan on adding one or two more examples to this section in the case that anyone finds it

82
00:05:32,920 --> 00:05:33,580
useful.

83
00:05:35,260 --> 00:05:35,500
All right.

84
00:05:35,500 --> 00:05:38,560
So let's continue to the next lesson if you'd like to integrate the library.

85
00:05:38,590 --> 00:05:40,570
Otherwise, I'll see you in the section after.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,240 --> 00:00:13,510
So here I have a blank specified project and we'll start off by cloning the ESP off sensor and Components

2
00:00:13,510 --> 00:00:16,390
Library into the project folder right here.

3
00:00:17,050 --> 00:00:18,940
So let's go to the project folder.

4
00:00:19,650 --> 00:00:20,760
And right click.

5
00:00:25,110 --> 00:00:26,940
Then go to get Bashir.

6
00:00:29,520 --> 00:00:31,350
Now let's grab the Clone Command.

7
00:00:33,450 --> 00:00:35,040
So just copy this line.

8
00:00:37,230 --> 00:00:39,240
And then paste it into get bash.

9
00:00:42,350 --> 00:00:43,660
And just let it finish.

10
00:00:46,970 --> 00:00:50,510
And now we can close it and let's check out the project folder.

11
00:00:53,390 --> 00:00:55,190
And there's a component we've cloned.

12
00:00:55,490 --> 00:00:58,310
All right, so let's go back and check the ID.

13
00:01:00,480 --> 00:01:05,070
Then let's right click on the project folder and go down to refresh.

14
00:01:07,470 --> 00:01:09,750
And other components is visible here as well.

15
00:01:10,620 --> 00:01:11,260
All right.

16
00:01:11,280 --> 00:01:16,140
So now we need to include this component into the project build by adjusting the top level.

17
00:01:16,140 --> 00:01:19,050
See Make List file, which is this one right here.

18
00:01:19,770 --> 00:01:20,880
So let's open it.

19
00:01:22,260 --> 00:01:27,420
And you need to add this line to the file and you could put it just underneath the first include statement

20
00:01:27,420 --> 00:01:28,770
here as I have.

21
00:01:29,070 --> 00:01:30,960
So I'll just give you a moment to type it.

22
00:01:31,440 --> 00:01:35,700
And then we're including the additional component as shown in the how to use section that we saw in

23
00:01:35,700 --> 00:01:36,750
the previous lesson.

24
00:01:37,290 --> 00:01:39,780
And what we're doing is quite similar to the instructions.

25
00:01:40,020 --> 00:01:45,690
We're just including this part here in the quotations, which is our path to the make list file to include

26
00:01:45,690 --> 00:01:46,800
the components folder.

27
00:01:47,280 --> 00:01:51,090
And once you've done that, you've successfully integrated the library into the project.

28
00:01:51,090 --> 00:01:56,010
But to see how to work with the examples included in this library, let's continue by going to the resource

29
00:01:56,010 --> 00:02:00,750
files I provided for this lesson and we're going to drop those files into the main folder here.

30
00:02:01,830 --> 00:02:08,820
So within the resource files, what I've given you is the BMS 680 sensor dot C file, which is based

31
00:02:08,820 --> 00:02:11,190
on the main dot C provided from the library.

32
00:02:13,530 --> 00:02:18,720
And the BM 680 header filed just contains a function prototype so that we can run the example from our

33
00:02:18,720 --> 00:02:25,830
main dot C and the C make list file includes our source files into the build and will replace our existing

34
00:02:25,830 --> 00:02:26,880
file here with it.

35
00:02:27,480 --> 00:02:33,570
And the k config project build file contains configuration defines and was also taken from the example

36
00:02:34,110 --> 00:02:34,950
in this file.

37
00:02:34,950 --> 00:02:37,260
We'll also replace our existing file here.

38
00:02:38,380 --> 00:02:39,850
And we'll also have an updated main.

39
00:02:40,810 --> 00:02:45,490
And this is the task common header file, which we'll update throughout the course to include all free

40
00:02:45,490 --> 00:02:51,910
auto's tasks, definition information like the stack size priority and the core idea of the ESP 32 that

41
00:02:51,910 --> 00:02:53,200
the task should run on.

42
00:02:53,200 --> 00:02:57,970
So just know that we'll make use of this file as we progress in the course, not just the current lesson.

43
00:02:58,150 --> 00:03:02,620
All right, so now let's select all of these files and we can drag them over to the main folder.

44
00:03:06,160 --> 00:03:08,510
And then choose copy files OC.

45
00:03:09,970 --> 00:03:11,800
And then select overwrite all.

46
00:03:14,360 --> 00:03:17,090
And now let's check out the main quake list file here.

47
00:03:18,990 --> 00:03:24,420
And there we have two source files listed that we need to build into the project main dot C and the

48
00:03:24,420 --> 00:03:26,400
beam CCD sensor dot C.

49
00:03:27,330 --> 00:03:30,030
And first, let's take a look at our main C file.

50
00:03:32,340 --> 00:03:33,720
In our main Dead Sea.

51
00:03:33,780 --> 00:03:40,410
We have an include for the BM 60 sensor header file and including that gives us access to the beam 680

52
00:03:40,410 --> 00:03:43,830
task start function, which starts the example task.

53
00:03:44,670 --> 00:03:46,530
So let's check out this header file.

54
00:03:47,870 --> 00:03:53,150
And there we have the function prototype which replaces what was in App Main from the example.

55
00:03:53,930 --> 00:03:55,430
So let's go ahead and take a look.

56
00:03:58,230 --> 00:04:04,080
So we have this function definition here for the BM 680 test start, which is what we are calling from

57
00:04:04,080 --> 00:04:05,070
main see.

58
00:04:05,370 --> 00:04:13,290
And here the beam 680 test task is created using the x task create Penta Core API which takes our definitions

59
00:04:13,290 --> 00:04:15,600
provided by the task common header file.

60
00:04:15,780 --> 00:04:21,210
And those definitions are for the beam 680 task stack size the task priority.

61
00:04:22,030 --> 00:04:25,000
And the core ID that the task should run on.

62
00:04:25,390 --> 00:04:26,890
So let's take a look at those.

63
00:04:27,850 --> 00:04:32,500
And there we have the stack size priority and core ID given by the example.

64
00:04:33,280 --> 00:04:37,600
So I've kept all these values the same as what was provided by the example.

65
00:04:38,020 --> 00:04:39,160
So let's go back.

66
00:04:40,310 --> 00:04:47,750
And now let's check out the BMV 63 autos task, which is the function specified here.

67
00:04:48,880 --> 00:04:54,250
So again, this is from the example provided by the library, and I won't go into too much detail here

68
00:04:54,250 --> 00:04:55,840
because this isn't our code.

69
00:04:56,110 --> 00:05:00,160
But you can see that they've done some initialization for eye to see communication.

70
00:05:01,650 --> 00:05:07,170
And then they've initialized the sensor and then they've set the sampling rates for temperature, humidity

71
00:05:07,170 --> 00:05:12,510
and pressure and then set the air filter size for temperature and pressure.

72
00:05:12,990 --> 00:05:16,920
Then they've changed the heater profile and set the ambient temperature.

73
00:05:16,950 --> 00:05:18,900
Then they get the measurement duration.

74
00:05:20,270 --> 00:05:25,610
And in the wild one loop, the measurement cycle is triggered with the reference to the sensor settings

75
00:05:25,610 --> 00:05:27,260
that were previously applied.

76
00:05:28,220 --> 00:05:30,890
So that gives you a general idea of how this works.

77
00:05:31,100 --> 00:05:35,990
The sensor is triggered based on those settings and that we have a delay until the measurement results

78
00:05:35,990 --> 00:05:40,670
are available and then we get the results from this values instance.

79
00:05:41,600 --> 00:05:43,370
Of the BM 60 values.

80
00:05:43,370 --> 00:05:53,690
TYPEDEF So here we access values for the temperature, humidity, pressure and gas resistance and those

81
00:05:53,690 --> 00:05:55,910
are all accessible via the typedef here.

82
00:05:56,920 --> 00:06:02,740
And the floating point sensor values are all here in the BMB 680 head of file from the library that

83
00:06:02,740 --> 00:06:03,640
we've integrated.

84
00:06:04,450 --> 00:06:05,590
So let's go back.

85
00:06:06,590 --> 00:06:10,850
And I'll just show you the other slight modifications I've made to this file, and that's at the top

86
00:06:10,850 --> 00:06:11,630
of the file.

87
00:06:13,960 --> 00:06:17,440
And there we have an included far ahead of file for our function prototype.

88
00:06:17,800 --> 00:06:22,060
And then we also have the task common to access our free auto definitions.

89
00:06:22,060 --> 00:06:27,940
And then we have these config example I to see definitions and this one is for the sensor address.

90
00:06:28,270 --> 00:06:30,790
And then we have another here for the serial data line.

91
00:06:32,130 --> 00:06:33,990
And this one is for the serial clock.

92
00:06:34,560 --> 00:06:37,290
And these come from the K config project build file.

93
00:06:37,290 --> 00:06:43,320
So we'll go ahead and open that because this file enables us to set various options from the sdhc config.

94
00:06:43,710 --> 00:06:45,360
So let's see how this works.

95
00:06:46,380 --> 00:06:50,400
Now I'll open this with the C C++ editor.

96
00:06:52,700 --> 00:06:57,710
And this config file provides us with this example configuration menu option.

97
00:06:57,740 --> 00:07:04,430
And when we build the project using this config file, the SDK config will then contain the menu configuration

98
00:07:04,430 --> 00:07:05,780
items that we see here.

99
00:07:06,260 --> 00:07:11,390
And this menu contains a choice for the example I to see address and the options for that.

100
00:07:11,840 --> 00:07:17,540
And there's also the example I to see master serial clock and serial data as well.

101
00:07:18,750 --> 00:07:23,730
So let's build the project and then we can view the config by going to project.

102
00:07:23,760 --> 00:07:25,410
Then go to build all.

103
00:07:28,640 --> 00:07:29,810
And this may take a moment.

104
00:07:29,810 --> 00:07:31,760
So I'll go ahead and speed up the video now.

105
00:07:38,840 --> 00:07:42,290
And once it's done, let's open the SDK config.

106
00:07:42,440 --> 00:07:44,150
So just double click on that.

107
00:07:49,760 --> 00:07:52,610
And the example configuration is right here.

108
00:07:54,280 --> 00:07:58,060
Where we have the BM 60 I to see address options.

109
00:07:58,900 --> 00:08:03,730
And we had the GPIO numbers for the serial clock and the serial data as well.

110
00:08:04,150 --> 00:08:08,950
So that's how the SDHC config and the CÉ config project build file work together.

111
00:08:09,340 --> 00:08:13,990
And I've already made the connections to the BMS 680 sensor based on the settings here.

112
00:08:15,300 --> 00:08:19,740
So now I'll go ahead and flash to my dev kit by going to launch and run mode.

113
00:08:23,490 --> 00:08:25,140
And again, I'll speed up the video.

114
00:08:30,230 --> 00:08:34,520
Now that that's done, we can open a monitor and view those printf statements from the while loop.

115
00:08:34,730 --> 00:08:36,230
Here we can open a terminal.

116
00:08:45,690 --> 00:08:49,260
And there we have the values printed at the duration, determined by the wild loop.

117
00:08:51,270 --> 00:08:51,840
Okay.

118
00:08:51,990 --> 00:08:53,490
So that's all for this one.

119
00:08:53,520 --> 00:08:58,710
And now that you know how to integrate the ESP lib, you now have an abundance of sensors and other

120
00:08:58,710 --> 00:09:00,270
components at your disposal.

121
00:09:00,270 --> 00:09:02,280
And I really hope you found this useful.

122
00:09:02,280 --> 00:09:04,020
And I'll see you in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
==================================================================================

# Section 6: Course Source Code

1
00:00:06,630 --> 00:00:10,080
OK, so just a brief word about the jet repository for this course.

2
00:00:10,560 --> 00:00:15,480
The link within the resources here will take you to the master branch, which contains the finalized

3
00:00:15,480 --> 00:00:19,650
source code everything that was typed and shown in the course in its final state.

4
00:00:20,130 --> 00:00:25,180
And if you go to the dropdown here, there was another branch called Contribution Station Improvements.

5
00:00:26,130 --> 00:00:30,900
And I created this branch in the case that anyone happens to find ways to improve the source code.

6
00:00:31,470 --> 00:00:37,020
So if you do find something that can be improved, please feel free to message me with details and I'll

7
00:00:37,020 --> 00:00:40,710
test it out as soon as I can and then add the changes to this branch here.

8
00:00:42,020 --> 00:00:47,480
And if you'd like to get notifications about the course repository, just come here and adjust the watch

9
00:00:47,480 --> 00:00:48,350
notifications.

10
00:00:48,980 --> 00:00:49,340
OK?


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: RGB Application Status LED


1
00:00:06,880 --> 00:00:07,060
Hi.

2
00:00:07,060 --> 00:00:08,180
Welcome back, everyone.

3
00:00:08,200 --> 00:00:12,760
We're going to begin development of our wireless local area network application by implementing the

4
00:00:12,760 --> 00:00:14,110
RGB status Led.

5
00:00:14,590 --> 00:00:17,440
Here, we'll briefly review the implementation details.

6
00:00:18,440 --> 00:00:21,080
So let's take a look at our implementation overview.

7
00:00:22,320 --> 00:00:27,630
We're going to create different colors by using the RGB led to indicate the application status.

8
00:00:27,750 --> 00:00:31,920
First, we'll create a function to initialize the RGB led settings per channel.

9
00:00:31,950 --> 00:00:36,210
The Gpio used for each channel and configure the timer as well.

10
00:00:36,480 --> 00:00:41,280
We'll create another function for setting the colors based on the duty cycle for each channel.

11
00:00:41,310 --> 00:00:44,940
Each channel being the red, green and blue channels.

12
00:00:45,120 --> 00:00:52,290
We'll then create functions that set the color of the RGB led to be used as our application status indicators.

13
00:00:52,560 --> 00:00:58,350
Finally, we'll test these functions in the Main.c file and will actually use them later to indicate

14
00:00:58,350 --> 00:01:05,460
statuses such as wi fi application started, Http server started and Wi-Fi connected.

15
00:01:07,240 --> 00:01:11,410
Now let's talk about the Led control component of the ESP IDF.

16
00:01:12,140 --> 00:01:18,290
I suggest you visit the impressive documentation here about the DC component and API reference.

17
00:01:18,320 --> 00:01:22,520
Here you can find all you need to know about Led control using the ADF.

18
00:01:22,550 --> 00:01:29,690
You'll find that this component is primarily designed for Led intensity control and signal generation.

19
00:01:29,690 --> 00:01:32,030
So just browse through here if you can.

20
00:01:32,060 --> 00:01:38,960
Also, you'll find that both high speed and low speed channels are available and there's 16 channels

21
00:01:38,960 --> 00:01:42,320
total, eight for high speed and eight for low speed.

22
00:01:43,180 --> 00:01:49,000
Our configuration steps include three main parts the timer and channel configurations and then setting

23
00:01:49,000 --> 00:01:50,680
and updating the duty cycle.

24
00:01:50,710 --> 00:01:52,090
So about the timer.

25
00:01:52,120 --> 00:01:57,310
Each timer counts up and the bits defined determines the count number before it resets.

26
00:01:57,310 --> 00:02:01,390
And the frequency determines the amount of time that it takes to count to the number.

27
00:02:01,420 --> 00:02:08,020
For example, for eight bits, the count number is from 0 to 255, and for ten bits it will be from

28
00:02:08,020 --> 00:02:12,520
0 to 1023 and the bit number in frequency.

29
00:02:12,550 --> 00:02:14,740
Those are key members of the Led.

30
00:02:14,740 --> 00:02:20,710
See timer config structure that we'll set, including other members such as the speed mode and timer

31
00:02:20,710 --> 00:02:21,580
number as well.

32
00:02:21,610 --> 00:02:27,100
And we'll pass this information to the Led see timer config function to set the config.

33
00:02:27,700 --> 00:02:29,420
For the channel configuration.

34
00:02:29,440 --> 00:02:36,760
The Gpio pin that the PWM output signal appears on is specified to a specific channel along with the

35
00:02:36,760 --> 00:02:37,420
timer.

36
00:02:37,570 --> 00:02:44,830
We'll set members of the C channel config structure and pass the configuration to C channel config.

37
00:02:45,420 --> 00:02:50,580
And then next we can create different colors by adjusting the duty cycle, which is the time duration

38
00:02:50,580 --> 00:02:55,250
within the period that the output signal will be high before it goes low.

39
00:02:55,260 --> 00:03:00,900
And we'll do this using the LEDs, set duty and LEDs update duty functions.

40
00:03:02,470 --> 00:03:06,670
Now, let's briefly get into the status led color functions that we're going to create.

41
00:03:07,960 --> 00:03:08,230
All right.

42
00:03:08,230 --> 00:03:12,490
So we'll have one function that sets the color by updating the duty cycle per channel.

43
00:03:12,520 --> 00:03:14,740
The red, green and blue channels.

44
00:03:15,100 --> 00:03:21,820
And then the status function will simply call the set color function at the duty cycle that we specified

45
00:03:21,850 --> 00:03:22,580
per channel.

46
00:03:22,600 --> 00:03:28,660
Depending on the color that we want, you can go to this link here or any other similar website.

47
00:03:28,660 --> 00:03:36,010
Just search for RGB led color selection and you can customize the status LEDs as you wish.

48
00:03:36,040 --> 00:03:42,820
However, for the three statuses, Wi-Fi started, Http server started and Wi-Fi connected.

49
00:03:42,850 --> 00:03:45,040
I've chosen the following values.

50
00:03:45,070 --> 00:03:46,180
WI fi started.

51
00:03:46,180 --> 00:03:47,620
Is this color here?

52
00:03:50,590 --> 00:03:53,350
An Http server looks like this.

53
00:03:55,440 --> 00:03:58,650
And Wi-Fi connected looks similar to this color here.

54
00:04:02,450 --> 00:04:04,940
So feel free to set the colors as you wish.

55
00:04:04,940 --> 00:04:09,680
Or better yet, create your own status functions as we develop the application further.

56
00:04:10,780 --> 00:04:13,060
Now, let's briefly talk about the hardware options.

57
00:04:14,420 --> 00:04:16,790
There are different flavors of RGB LEDs.

58
00:04:16,820 --> 00:04:21,740
You can obtain the package type on a PCB or the common cathode or common anode type.

59
00:04:21,830 --> 00:04:26,930
Whichever you obtain, be sure to check the datasheet and verify the required resistor values and you

60
00:04:26,930 --> 00:04:29,780
can make the connections based on the gpios we define.

61
00:04:30,140 --> 00:04:36,050
Also, if you're using the common anode or common cathode type, be sure to follow the diagram and note

62
00:04:36,050 --> 00:04:37,250
the long leg difference.

63
00:04:37,280 --> 00:04:39,230
Ground versus positive voltage.

64
00:04:41,070 --> 00:04:43,860
All right, so let's get started with programming in the upcoming lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,420 --> 00:00:07,660
All right.

2
00:00:07,660 --> 00:00:10,870
So the first thing we need to do here is to create two new files.

3
00:00:11,350 --> 00:00:13,510
So let's expand the project folder.

4
00:00:14,020 --> 00:00:19,990
And at the main folder, right click and go to new source file.

5
00:00:20,970 --> 00:00:24,600
And call it rugby underscore led see.

6
00:00:25,350 --> 00:00:26,290
And choose default.

7
00:00:26,310 --> 00:00:27,240
See Source.

8
00:00:29,400 --> 00:00:31,050
And now create a head of file.

9
00:00:33,680 --> 00:00:38,810
And call it rugby underscore led and choose default.

10
00:00:38,840 --> 00:00:40,340
See header template.

11
00:00:42,710 --> 00:00:43,040
OC.

12
00:00:43,040 --> 00:00:50,870
Next, we need to update the C list file and add the GB led source file so be sure that it's the C list

13
00:00:50,870 --> 00:00:52,640
file here on the main.

14
00:00:53,560 --> 00:00:59,470
And add g B underscore led C and save it.

15
00:01:00,370 --> 00:01:02,260
So now let's head over to the header file.

16
00:01:03,640 --> 00:01:11,320
So here in the header file, we'll define the rugby led GPO as the number of rugby channels, the configuration

17
00:01:11,320 --> 00:01:14,150
structure and the prototypes for the color statuses.

18
00:01:14,170 --> 00:01:17,950
So let's start by defining the rugby led GPOs.

19
00:01:18,900 --> 00:01:20,340
And we'll say define.

20
00:01:21,480 --> 00:01:26,580
GP led read GPIO and will use IO 21.

21
00:01:28,310 --> 00:01:32,570
Now define the rugby led green GPIO.

22
00:01:34,150 --> 00:01:35,680
As I oh 22.

23
00:01:36,310 --> 00:01:38,500
So now let's define the blue one.

24
00:01:42,600 --> 00:01:44,100
And we can use 23.

25
00:01:45,480 --> 00:01:48,000
So now here we can define the number of channels.

26
00:01:48,000 --> 00:01:51,900
So we'll say rugby led colour mix channels.

27
00:01:54,170 --> 00:01:55,610
And we'll say define.

28
00:01:57,350 --> 00:01:59,830
G b led channel num.

29
00:02:01,270 --> 00:02:04,600
And we'll have three, right for red, green and blue.

30
00:02:04,930 --> 00:02:07,780
So now let's define the configuration structure.

31
00:02:08,590 --> 00:02:11,320
We'll say ruby led configuration.

32
00:02:14,880 --> 00:02:16,740
And we'll make it a typedef struct.

33
00:02:20,370 --> 00:02:22,320
And we'll have here a channel.

34
00:02:24,030 --> 00:02:26,910
It GPIO and INT mode.

35
00:02:28,030 --> 00:02:29,500
And timer index.

36
00:02:32,000 --> 00:02:36,050
So now let's call it ldl-c info underscore RT.

37
00:02:36,560 --> 00:02:42,110
Now copy this and we can create an array with the same length as the number of channels.

38
00:02:45,810 --> 00:02:49,410
We could do that using our GP led channel num.

39
00:02:54,550 --> 00:02:55,290
Okay, great.

40
00:02:55,300 --> 00:02:58,390
So now we need the prototypes for the color statuses.

41
00:02:58,390 --> 00:03:04,240
So the first one we can do is the color to indicate that the wi fi application has started.

42
00:03:05,030 --> 00:03:08,210
So let's just make a comment here colored to indicate.

43
00:03:09,690 --> 00:03:12,420
WI fi application started.

44
00:03:18,420 --> 00:03:26,160
And let's say void RG be led wi fi app started and it takes no input parameters.

45
00:03:27,630 --> 00:03:33,060
Okay, So the next one will be the color to indicate that the HTTP server has started.

46
00:03:40,890 --> 00:03:45,990
And we'll say void our Gbps led http server started.

47
00:03:46,750 --> 00:03:48,280
And this is void as well.

48
00:03:50,990 --> 00:03:57,020
In the last one is the color to indicate that the ESP 32 is connected to an access point.

49
00:04:10,040 --> 00:04:11,420
And this will be void.

50
00:04:11,540 --> 00:04:17,210
RG be led wi fi connected and it's void as well.

51
00:04:18,870 --> 00:04:20,340
All right, so that's it.

52
00:04:20,340 --> 00:04:24,210
So now we can move on to the implementation and the GB LMDC file.

53
00:04:26,640 --> 00:04:26,910
Okay.

54
00:04:26,910 --> 00:04:29,250
So first let's include std bool.

55
00:04:31,640 --> 00:04:35,270
And then also include the driver for DCH.

56
00:04:38,800 --> 00:04:40,780
And this is for legacy driver.

57
00:04:42,270 --> 00:04:46,440
And also include the rugby LED header file here as well.

58
00:04:48,560 --> 00:04:53,690
So first we need to create a function that initializes the rugby led settings per channel.

59
00:04:55,920 --> 00:04:58,320
Including the GPIO for each color.

60
00:05:01,310 --> 00:05:03,800
The mode and the time of configuration.

61
00:05:05,620 --> 00:05:12,340
So this is going to be a static function, meaning it's restricted to this file and it returns void.

62
00:05:13,720 --> 00:05:18,490
Call it rg be led p w m in it and it's void.

63
00:05:20,800 --> 00:05:25,510
And then I'll here define a variable that we'll use to iterate through the rugby channels and that can

64
00:05:25,510 --> 00:05:27,700
be an int, call it rugby underscore.

65
00:05:29,050 --> 00:05:32,090
And at this point we can configure the rugby channel structures.

66
00:05:32,110 --> 00:05:33,640
Let's do the read first here.

67
00:05:33,970 --> 00:05:36,150
So it's C underscore, c.

68
00:05:36,170 --> 00:05:36,700
H.

69
00:05:37,760 --> 00:05:40,450
Which is the array that we created in the header file.

70
00:05:40,460 --> 00:05:43,760
So at the first position, update the channel.

71
00:05:45,540 --> 00:05:46,590
And from the LDCs.

72
00:05:46,620 --> 00:05:49,710
DRIVER We'll use Channel Zero.

73
00:05:50,220 --> 00:05:50,520
All right.

74
00:05:50,520 --> 00:05:51,870
So choose Channel Zero.

75
00:05:53,540 --> 00:05:55,250
And let's copy this.

76
00:05:57,190 --> 00:06:05,310
Update the GPIO as RG be led, read GPIO and set the mode.

77
00:06:05,320 --> 00:06:06,670
Here is high speed mode.

78
00:06:15,540 --> 00:06:16,560
And the timer.

79
00:06:17,530 --> 00:06:19,150
Is going to be time or zero.

80
00:06:21,690 --> 00:06:24,240
All right, So choose a time or zero.

81
00:06:24,840 --> 00:06:27,000
We can now take care of the Green Channel.

82
00:06:30,390 --> 00:06:33,480
So for the Green Channel, this is going to be Channel one.

83
00:06:33,480 --> 00:06:36,480
So update all the members to channel one.

84
00:06:40,830 --> 00:06:42,840
And that'll be EDC Channel one.

85
00:06:43,110 --> 00:06:45,150
And the GPIO should be green.

86
00:06:47,370 --> 00:06:49,560
So next, let's update the blue channel.

87
00:06:50,350 --> 00:06:52,120
And this is the same story here.

88
00:06:52,810 --> 00:06:55,510
So update the channel for each structure member.

89
00:06:57,900 --> 00:07:00,540
The channel number as well should be channeled to.

90
00:07:01,710 --> 00:07:03,210
The GPIO is blue.

91
00:07:05,620 --> 00:07:07,960
And at this point here we can configure the timer.

92
00:07:08,740 --> 00:07:10,570
So configure timer zero.

93
00:07:14,450 --> 00:07:17,750
And will specify the timer config struct.

94
00:07:19,360 --> 00:07:20,950
From the LMDC driver.

95
00:07:22,740 --> 00:07:23,160
All right.

96
00:07:23,160 --> 00:07:25,740
And call it EDC underscore timer.

97
00:07:28,480 --> 00:07:31,660
And we'll update the first member duty resolution.

98
00:07:35,060 --> 00:07:37,310
As la EDC timer.

99
00:07:37,400 --> 00:07:38,330
Eight bits.

100
00:07:40,080 --> 00:07:44,670
And then now the frequency member here, 100 hertz should be fast enough.

101
00:07:46,470 --> 00:07:47,820
And for the speed mode.

102
00:07:50,300 --> 00:07:52,880
Use led DC high speed mode.

103
00:07:55,110 --> 00:07:56,430
And the time a number.

104
00:07:57,990 --> 00:08:00,900
Will be led DC Timer zero.

105
00:08:06,080 --> 00:08:07,850
All right, so that's all for the timer.

106
00:08:09,060 --> 00:08:11,730
And now we can call EDC timer config.

107
00:08:12,940 --> 00:08:16,270
This one here and then pass a reference to the structure.

108
00:08:18,960 --> 00:08:19,200
All right.

109
00:08:19,200 --> 00:08:23,580
So lastly, let's configure the channels based on the rugby channel settings that we've just done.

110
00:08:23,580 --> 00:08:28,860
So we'll grab this variable here and we're going to use it to increment through the channels.

111
00:08:29,370 --> 00:08:32,130
So here we'll say configure channels.

112
00:08:35,060 --> 00:08:39,920
And say for the FF variable equals zero.

113
00:08:41,220 --> 00:08:44,760
Four rugby channels less than the total number of channels.

114
00:08:49,800 --> 00:08:52,380
We're going to increment through the channels.

115
00:08:54,490 --> 00:08:58,930
And here we need to update the EDC channel config struct from the driver.

116
00:09:04,430 --> 00:09:06,320
And call it channel.

117
00:09:09,030 --> 00:09:11,160
And we're going to update the channel member.

118
00:09:11,950 --> 00:09:13,930
Using that increment variable.

119
00:09:16,110 --> 00:09:17,100
Like so.

120
00:09:20,570 --> 00:09:23,030
And for the duty, we can leave it as zero.

121
00:09:25,020 --> 00:09:28,860
And for the H point member, we can make that zero as well.

122
00:09:29,820 --> 00:09:35,220
And next, we can update the GPIO number using our settings and the increment variable.

123
00:09:46,230 --> 00:09:50,850
And the interrupt type should be disabled, which we can take from the driver.

124
00:09:53,010 --> 00:09:54,180
Interrupt, disable.

125
00:09:55,800 --> 00:09:59,850
OC and for the speed mode, we could take that from our settings as well.

126
00:10:00,910 --> 00:10:03,880
Using the rugby channel variable.

127
00:10:06,260 --> 00:10:07,850
Also four timers select.

128
00:10:10,840 --> 00:10:13,390
This can be updated using our settings above.

129
00:10:16,220 --> 00:10:17,720
From the timer index.

130
00:10:22,390 --> 00:10:22,900
Okay, great.

131
00:10:22,900 --> 00:10:26,350
So now we can call the DC channel config function.

132
00:10:28,140 --> 00:10:30,210
And then pass a reference to the struct.

133
00:10:32,880 --> 00:10:39,960
This will be done for each iteration through the loop and next takes care of our p w m GB channels initialization.

134
00:10:40,560 --> 00:10:43,350
So next we'll take care of the set colour function.

135
00:10:46,030 --> 00:10:47,530
So let's make a comment here.

136
00:10:49,080 --> 00:10:50,790
Sets the rugby colour.

137
00:10:54,300 --> 00:10:57,240
All right, So here's, say, static void.

138
00:10:58,140 --> 00:11:07,140
Rugby led set colour and that's a UNT eight type for the red and also for the green and blue channels

139
00:11:07,140 --> 00:11:07,770
as well.

140
00:11:14,870 --> 00:11:20,150
So here we specified the input type as you went eight because we've specified the duty resolution is

141
00:11:20,150 --> 00:11:21,070
eight bits.

142
00:11:21,080 --> 00:11:25,220
Therefore the duty cycle values can range from 0 to 255.

143
00:11:25,250 --> 00:11:25,820
All right.

144
00:11:25,820 --> 00:11:27,740
So let's make a comment here.

145
00:11:27,770 --> 00:11:29,060
Value should be.

146
00:11:30,370 --> 00:11:33,910
0 to 255 for an eight bit number.

147
00:11:35,670 --> 00:11:38,880
And we'll use the D.C. set duty function.

148
00:11:39,700 --> 00:11:44,650
From the driver and for the speed passer, see Channel Zero.

149
00:11:46,810 --> 00:11:50,980
For the speed mode and the EDC Channel Zero.

150
00:11:53,030 --> 00:11:54,080
As the channel.

151
00:11:54,810 --> 00:11:56,460
And this is the Red Channel.

152
00:11:57,860 --> 00:11:59,900
OC so now call DC.

153
00:11:59,960 --> 00:12:01,940
Update duty from the driver.

154
00:12:02,790 --> 00:12:06,060
And for the speed, it's again see Channel Zero.

155
00:12:08,340 --> 00:12:09,670
And let's see.

156
00:12:09,690 --> 00:12:12,450
Channel zero for the channel as well.

157
00:12:15,740 --> 00:12:16,200
Okay.

158
00:12:16,490 --> 00:12:23,390
So just copy these two lines and we can take care of Channel one as well and just update the color parameter

159
00:12:23,420 --> 00:12:26,930
as green and then the channel as one.

160
00:12:32,480 --> 00:12:34,410
So now do the same for the blue channel.

161
00:12:34,430 --> 00:12:36,170
Change this to channel two.

162
00:12:41,350 --> 00:12:42,730
And now this is for blue.

163
00:12:44,710 --> 00:12:48,160
Okay, so that's our GB set color function.

164
00:12:48,190 --> 00:12:51,220
Now let's create the status colors that we'll use in the application.

165
00:12:51,220 --> 00:12:52,570
So go to the head of file.

166
00:12:54,570 --> 00:12:56,100
And copy these prototypes.

167
00:12:57,870 --> 00:12:59,760
And then paste them into the C file.

168
00:13:00,850 --> 00:13:05,410
Let's get rid of these comments as they're already in the header file so we don't need them here.

169
00:13:07,330 --> 00:13:13,060
So for wi fi started we'll call our GB led p w init function.

170
00:13:14,790 --> 00:13:16,530
And then we'll set the color.

171
00:13:19,840 --> 00:13:26,550
I mentioned in the intro video, and that is 250 5102 and 255.

172
00:13:28,790 --> 00:13:31,820
That's the magenta type color that I showed in the intro.

173
00:13:33,980 --> 00:13:36,420
And this function, we only need to call it once.

174
00:13:36,440 --> 00:13:41,150
So we need a global variable to indicate whether it's already been initialized.

175
00:13:41,420 --> 00:13:44,450
So we'll say handle for RGV.

176
00:13:45,420 --> 00:13:47,280
Led P.W. and in it.

177
00:13:48,230 --> 00:13:55,610
And say bull and call it g, underscore p w and it handle and initialize it to false.

178
00:13:59,430 --> 00:14:03,180
And let's use this here and set it to true before the function is completed.

179
00:14:06,100 --> 00:14:06,580
All right.

180
00:14:06,790 --> 00:14:08,530
And then let's come back here.

181
00:14:09,360 --> 00:14:11,490
And check if it hasn't been initialized.

182
00:14:12,840 --> 00:14:14,010
And if it hasn't?

183
00:14:15,010 --> 00:14:18,520
Then we'll go ahead and initialize by calling the function.

184
00:14:26,440 --> 00:14:30,250
So copied the same and do this for the http server started.

185
00:14:33,170 --> 00:14:34,870
And then update the color as you like.

186
00:14:34,880 --> 00:14:38,000
I'll use the yellowish color that I had shown previously.

187
00:14:50,510 --> 00:14:50,870
Again.

188
00:14:50,870 --> 00:14:52,640
Set your wi fi connected color.

189
00:14:53,830 --> 00:14:56,740
I'll use the blueish greenish colors I had previously shown.

190
00:15:03,680 --> 00:15:03,920
All right.

191
00:15:03,920 --> 00:15:04,160
Yes.

192
00:15:04,160 --> 00:15:04,700
So that's it.

193
00:15:04,700 --> 00:15:09,350
You could probably define some macros for these color values when you know what you want, just so you're

194
00:15:09,350 --> 00:15:12,020
not using these magic numbers as we're doing here.

195
00:15:12,020 --> 00:15:15,980
So for now, let's test these out in the main file.

196
00:15:19,380 --> 00:15:23,400
And to do that, we'll need to include the GP led file.

197
00:15:24,740 --> 00:15:26,750
And just put the status function here.

198
00:15:26,780 --> 00:15:30,410
Say rg be led wi fi up started.

199
00:15:32,910 --> 00:15:35,640
And change the delay to 1000 milliseconds.

200
00:15:37,150 --> 00:15:41,950
And then now we can put in the GP led HTTP server started.

201
00:15:43,550 --> 00:15:45,020
And then add another delay.

202
00:15:46,750 --> 00:15:50,580
And then we also want to test the rugby led wi fi connected function.

203
00:15:57,790 --> 00:15:59,590
And we can include another delay here.

204
00:16:01,660 --> 00:16:03,910
So the color should change at this interval.

205
00:16:04,210 --> 00:16:06,520
So now go ahead and build the project.

206
00:16:09,390 --> 00:16:10,530
And just give it a minute.

207
00:16:15,610 --> 00:16:18,520
So once the build is complete, let's go flash the dev kit.

208
00:16:23,230 --> 00:16:26,350
And I've plugged mine into a different port, but that's not a problem.

209
00:16:26,350 --> 00:16:31,480
I can update it easily by coming up here and then changing the port from my rover kit.

210
00:16:33,290 --> 00:16:35,150
And then we can just hit flash again.

211
00:16:43,100 --> 00:16:45,320
All right, so now let's check out the rugby led.

212
00:16:47,890 --> 00:16:48,190
Cool.

213
00:16:48,190 --> 00:16:54,070
So we have the wi fi up started, web server started and wi fi connected status is all shining, so

214
00:16:54,070 --> 00:16:56,680
our status LEDs are good to go in the next section.

215
00:16:56,680 --> 00:16:58,180
Let's get wi fi up and running.

216
00:16:58,180 --> 00:16:59,530
So I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: WiFi Application


1
00:00:07,170 --> 00:00:12,330
Everyone and welcome to the whitefly implementation section will provide an overview of the implementation

2
00:00:12,330 --> 00:00:16,170
and some APIs that we'll use from the impressive Viotti development framework.

3
00:00:18,100 --> 00:00:20,440
So first, let's take a look at our implementation overview.

4
00:00:21,840 --> 00:00:26,190
From a high level perspective, meaning what the Abilify application is supposed to do without getting

5
00:00:26,190 --> 00:00:32,520
into too much detail is, first of all, the ESP 32 should start its access point so that other devices

6
00:00:32,520 --> 00:00:33,270
can connect to it.

7
00:00:33,870 --> 00:00:39,720
This enables users to connect to it in order to access information such as sensor data, device information,

8
00:00:39,720 --> 00:00:46,140
connection status and connection information like the IP address, gateway and netmask assigned to the

9
00:00:46,140 --> 00:00:47,070
ESP 32.

10
00:00:47,760 --> 00:00:53,280
Also, we'll have a user option to connect and disconnect from an access point and to display the local

11
00:00:53,280 --> 00:00:54,300
time, etc..

12
00:00:55,410 --> 00:01:02,190
Next, the Wi-Fi application will start an HTTP server and will program this after the wi fi programming

13
00:01:02,190 --> 00:01:07,980
sections, and that web server will support a web page to do everything that I've just mentioned.

14
00:01:09,170 --> 00:01:15,410
Also, the application contains a free autos task that receives cue messages that will use to coordinate

15
00:01:15,410 --> 00:01:19,230
Wi-Fi and web server events, and we'll see more about this later.

16
00:01:19,760 --> 00:01:28,220
By the way, feel free to check out these photos APIs to create, which creates the Q and Q send to

17
00:01:28,220 --> 00:01:36,560
send data to the Q and Q received to receive data which again will use to coordinate the order of events

18
00:01:36,560 --> 00:01:38,180
that occur in our application.

19
00:01:38,930 --> 00:01:43,790
So I won't go into too much details about these because I'm confident that you'll have a general understanding

20
00:01:43,790 --> 00:01:44,600
of how they work.

21
00:01:44,990 --> 00:01:51,620
Once we implement them in the application and later in the course will connect the ESP 32 using previously

22
00:01:51,620 --> 00:01:52,610
saved credentials.

23
00:01:53,360 --> 00:01:56,150
So here's a simplified overview of the Wi-Fi application.

24
00:01:56,840 --> 00:02:03,000
Basically, you'll have a connecting device, either your mobile phone or laptop, etc., which becomes

25
00:02:03,000 --> 00:02:05,750
the station of the ESB 32 soft tape.

26
00:02:05,780 --> 00:02:13,970
When connected, the DHP service from the ESP 32 soft app will dynamically assign an IP to your device

27
00:02:14,900 --> 00:02:19,880
and you'll interact with the ESP 32 via the web page served by the web server.

28
00:02:21,340 --> 00:02:28,960
Also, the P32 itself will start an access point slash station mode and will statically assign an IP

29
00:02:28,960 --> 00:02:30,400
address to the soft API.

30
00:02:31,180 --> 00:02:38,740
The DHP service dynamically assigns an IP address for connecting stations also will specify a maximum

31
00:02:38,740 --> 00:02:40,510
number of stations that are allowed to connect.

32
00:02:41,720 --> 00:02:47,690
And eventually, we'll update the application so that we can connect the SB 32 to an external access

33
00:02:47,690 --> 00:02:50,480
point or router where there's an internet connection.

34
00:02:51,050 --> 00:02:56,420
And this enables us to get the local time using Simple Network Time Protocol or S&amp;P.

35
00:02:57,410 --> 00:03:04,280
And also did keep service from the access point will dynamically assign an IP address to the SPF 30

36
00:03:04,280 --> 00:03:05,960
to an hour application.

37
00:03:06,590 --> 00:03:10,580
Now let's briefly talk about the Wi-Fi driver APIs from the ESB IDF.

38
00:03:11,820 --> 00:03:17,340
So I suggest you visit the impressive documentation here about the Wi-Fi driver and take a couple of

39
00:03:17,340 --> 00:03:18,600
minutes to browse through this.

40
00:03:19,870 --> 00:03:25,120
Also, take a look at the programming model, as well as the fi events that occur in the background.

41
00:03:25,840 --> 00:03:28,570
These events will be picked up by our event handler.

42
00:03:29,880 --> 00:03:36,150
Also, check out the API reference here and feel free to browse through it, but I'll talk about selected

43
00:03:36,150 --> 00:03:37,170
API shortly.

44
00:03:38,450 --> 00:03:42,260
And also look into the network interface documentation here as well.

45
00:03:42,980 --> 00:03:48,920
Just try to take note of the idea behind it and the architecture and scroll down to the programmers

46
00:03:48,920 --> 00:03:53,810
manual, where the Wi-Fi event modes and default initialization I mentioned.

47
00:03:54,380 --> 00:03:56,780
I'll discuss some APIs later from here as well.

48
00:03:57,690 --> 00:04:02,670
All right, so we'll start configuring our Wi-Fi application by defining Wi-Fi settings in the header

49
00:04:02,670 --> 00:04:10,890
file like the side of the USB to the password, the IP address, gateway and netmask, et cetera.

50
00:04:11,640 --> 00:04:17,880
We'll also define the Wi-Fi application for the arduous task, and we can use either API here, but

51
00:04:17,880 --> 00:04:23,520
will actually use the PIN to code version here so that we can specify which core that we want to allocate

52
00:04:23,520 --> 00:04:27,030
the work to as we have two cores available on the ESB 32.

53
00:04:27,900 --> 00:04:33,420
We'll also create an event handler so that certain Wi-Fi and IP events are automatically accounted for

54
00:04:33,420 --> 00:04:34,620
by the Wi-Fi driver.

55
00:04:35,580 --> 00:04:41,010
And at the start of your Wi-Fi application, we'll set up the default configuration by initializing

56
00:04:41,010 --> 00:04:46,620
the TCP IP stack using the ESB network interface and IT function.

57
00:04:48,290 --> 00:04:54,890
And will also create the basic Wi-Fi configuration settings by using the ESP Wi-Fi in IT function.

58
00:04:55,520 --> 00:05:00,470
And by the way, this one must be called before any other Wi-Fi API is called.

59
00:05:01,510 --> 00:05:08,170
Additionally, we'll need to use ISP Wi-Fi set storage, which sets the storage configuration type.

60
00:05:09,130 --> 00:05:11,830
In which case will set the storage type to RAM?

61
00:05:13,100 --> 00:05:18,800
Will then create the default configurations for both the default app and default station interfaces.

62
00:05:19,460 --> 00:05:25,190
Please feel free to follow these links and read up on them in more detail and follow the link for the

63
00:05:25,190 --> 00:05:27,890
default app and default station.

64
00:05:28,430 --> 00:05:33,080
As the API mentioned, we need these to register the default Wi-Fi handlers.

65
00:05:34,850 --> 00:05:41,900
The start of the application also includes defining the SPF 30 to soft day peak configuration will define

66
00:05:41,900 --> 00:05:49,010
the AP settings for members of the wi fi config structure, which in this case will want to update selected

67
00:05:49,220 --> 00:05:51,610
soft AP structure members listed here.

68
00:05:53,060 --> 00:06:02,020
And the ESPN network interface said IP info sets the IP address of the soft AP and ESPN network interface,

69
00:06:02,030 --> 00:06:11,060
D.H. CPS starts the DHP service for any connecting stations to the ESPN Thirty two so that IP addresses

70
00:06:11,060 --> 00:06:13,760
can be dynamically assigned by the ESPN.

71
00:06:15,060 --> 00:06:23,430
Also, S.P. Rifai, I said mode sets the mode, whether it's a mode, station mode or a station mode,

72
00:06:23,730 --> 00:06:31,920
which is the mode that we will use and ESP Wi-Fi said Config sets the configuration of the access point

73
00:06:31,920 --> 00:06:35,730
based on the Wi-Fi config structure members that we have previously set.

74
00:06:36,940 --> 00:06:42,160
And S.P. Wi-Fi set bandwidth will use to set the bandwidth at 20 megahertz.

75
00:06:42,940 --> 00:06:49,570
Additionally, we'll use ISP Wi-Fi, said Power Save, and we're going to set it to none because we

76
00:06:49,570 --> 00:06:52,240
will not use power saving in this application.

77
00:06:53,240 --> 00:07:00,620
Finally, we can call ISP wi fi start once we have done all of this, which starts wi fi in the mode

78
00:07:00,620 --> 00:07:05,480
pre-specified, which in our case is wi fi mode app station mode.

79
00:07:09,510 --> 00:07:14,250
All right, so feel free to keep this document open as we go through the programming section, if you

80
00:07:14,250 --> 00:07:17,190
need to refer back to what's going on and I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,820 --> 00:00:07,180
Okay.

2
00:00:07,180 --> 00:00:10,870
So we're going to set up the wi fi programming section by adding a few new files.

3
00:00:11,410 --> 00:00:13,300
So first, let's add a new source file.

4
00:00:13,660 --> 00:00:15,700
So let's add a new source file in the main here.

5
00:00:20,470 --> 00:00:22,660
And call it wi fi app dot c.

6
00:00:25,000 --> 00:00:26,530
And now let's add a new header file.

7
00:00:29,870 --> 00:00:32,000
And call it wi fi app h.

8
00:00:34,700 --> 00:00:36,170
And let's add another header file.

9
00:00:39,040 --> 00:00:40,790
And call it tasks common.

10
00:00:43,300 --> 00:00:47,740
And in this set of file, we'll keep all the information for the free autos tasks that will create throughout

11
00:00:47,740 --> 00:00:48,220
the course.

12
00:00:50,880 --> 00:00:56,070
And now let's head over to the C make list file and now we're going to add the wi fi app source file.

13
00:00:59,350 --> 00:00:59,650
Okay.

14
00:00:59,650 --> 00:00:59,980
Great.

15
00:01:01,400 --> 00:01:06,500
And now let's head over to the wife of a --, and he will define the wifely application settings

16
00:01:06,800 --> 00:01:09,500
and create the network interface objects for the access point.

17
00:01:09,500 --> 00:01:14,810
And the station also will add some preliminary message IDs for the application tasks and a structure

18
00:01:14,810 --> 00:01:15,740
for the message queue.

19
00:01:16,010 --> 00:01:20,600
Additionally, we'll have a prototype for a function to send a message to the cube and another for starting

20
00:01:20,600 --> 00:01:22,070
the wi fi application task.

21
00:01:22,370 --> 00:01:23,750
So first we need to include.

22
00:01:25,430 --> 00:01:30,680
ESPN network interface, and that's necessary for the network interface objects.

23
00:01:32,190 --> 00:01:34,770
So here, let's define the Wi-Fi application settings.

24
00:01:36,780 --> 00:01:39,780
And let's first define the wi fi app as a side.

25
00:01:42,770 --> 00:01:45,620
And we'll call it SB 32 AP.

26
00:01:48,600 --> 00:01:49,830
And that's the access point.

27
00:01:49,860 --> 00:01:50,190
Name.

28
00:01:51,560 --> 00:01:57,230
And in case you need a little clarification, the SSA D is the service set identifier and you'll encounter

29
00:01:57,230 --> 00:01:59,150
this when trying to connect to a wireless network.

30
00:01:59,420 --> 00:02:05,240
So when we connect later, you'll see the ISP 32 SSI ID to show up in the list of wireless networks

31
00:02:05,240 --> 00:02:07,130
on your PC or mobile device.

32
00:02:07,670 --> 00:02:07,970
Okay.

33
00:02:07,970 --> 00:02:11,030
So next, let's define the wi fi AP password.

34
00:02:14,950 --> 00:02:20,410
And this is the password that you'll into when connecting to the ESP via the Asus I.D. we had just defined

35
00:02:20,750 --> 00:02:24,820
the now call it password for simplicity, but you can call it whatever you like.

36
00:02:27,800 --> 00:02:30,860
So this will be the Wi-Fi access point password.

37
00:02:33,900 --> 00:02:34,200
Okay.

38
00:02:34,200 --> 00:02:36,900
So now let's define the Wi-Fi app channel.

39
00:02:40,900 --> 00:02:44,320
And we'll use Channel one as the Access Point Channel.

40
00:02:46,850 --> 00:02:53,480
And regarding Wi-Fi channels, the ISP 32 operates in the 2.4 gigahertz range, where there are 14 channels

41
00:02:53,480 --> 00:02:57,980
spaced five megahertz apart, except for a 12 megahertz base before Channel 14.

42
00:02:58,760 --> 00:03:01,370
So to guarantee no interference in any circumstances.

43
00:03:01,520 --> 00:03:07,880
The Wi-Fi protocol requires 16.25 to 22 megahertz of channel separation, as shown here.

44
00:03:09,900 --> 00:03:14,490
And if you check the impressive documentation and the resources that I've provided, it's mentioned

45
00:03:14,490 --> 00:03:18,540
that there are some factors that should be considered by the developer when programming channel selection

46
00:03:18,540 --> 00:03:25,200
behavior, which are interference concerns, legal considerations and FCC rules and transmit power.

47
00:03:25,470 --> 00:03:29,340
For example, one eight or 2.11 transmitter is using Channel one.

48
00:03:29,580 --> 00:03:35,220
The other may use Channel five or six, and using Channel two or three is not recommended in about legal

49
00:03:35,220 --> 00:03:36,150
considerations.

50
00:03:36,420 --> 00:03:39,750
Channels one through 11 may be used safely in most countries in the world.

51
00:03:39,900 --> 00:03:41,850
So we went with Channel one in this course.

52
00:03:42,090 --> 00:03:47,160
But feel free to check out this document or any other resources for additional information if you have

53
00:03:47,160 --> 00:03:48,750
concerns about channel selection.

54
00:03:49,320 --> 00:03:56,910
So next, we'll define the wi fi app visibility, which we'll call wi fi app assisted hidden.

55
00:04:03,140 --> 00:04:04,250
And this will be zero.

56
00:04:05,240 --> 00:04:07,520
And this defines the Wi-Fi access point.

57
00:04:07,520 --> 00:04:13,520
Visibility of the ISP 32 and zero makes it visible, which means that you will actually see the ISP

58
00:04:13,520 --> 00:04:17,510
32 SSD in your list of networks when trying to connect to it.

59
00:04:17,930 --> 00:04:18,290
All right.

60
00:04:18,290 --> 00:04:19,250
So let's comment.

61
00:04:19,280 --> 00:04:20,420
App visibility.

62
00:04:22,700 --> 00:04:23,030
Okay.

63
00:04:23,030 --> 00:04:26,180
So next, let's define the FI app.

64
00:04:27,090 --> 00:04:28,110
Max connection's.

65
00:04:30,180 --> 00:04:31,500
And I'll into five here.

66
00:04:31,650 --> 00:04:33,090
But you can make it whatever you like.

67
00:04:33,270 --> 00:04:35,940
For example, you may only want to allow one device to connect.

68
00:04:36,600 --> 00:04:38,910
All right, so this is our app, max clients.

69
00:04:42,250 --> 00:04:46,630
The next will define the wi fi app beacon interval.

70
00:04:50,470 --> 00:04:52,150
As 100 milliseconds.

71
00:04:53,050 --> 00:04:57,880
And the beacon broadcasts interval is the time lag between each of the beacons sent by your router or

72
00:04:57,880 --> 00:04:58,630
access point.

73
00:04:58,960 --> 00:05:00,940
In the case it's the ESB 32.

74
00:05:01,150 --> 00:05:05,740
So by definition, the lower the value, the smaller the time lag, which means that the beacon is sent

75
00:05:05,740 --> 00:05:10,300
more frequently in, the higher the value, the bigger the time lag, which means that the beacon is

76
00:05:10,300 --> 00:05:11,560
sent less frequently.

77
00:05:12,040 --> 00:05:16,270
So the beacon is needed for your devices to receive information about the particular router.

78
00:05:16,450 --> 00:05:22,120
When our case, the ISP in the beacon includes some information such as the side timestamp and other

79
00:05:22,120 --> 00:05:27,490
various parameters, and most of the routers out of the box has a default beacon interval function value

80
00:05:27,500 --> 00:05:33,100
set at 100 milliseconds, and the implications of the high beacon interval may be that you'll achieve

81
00:05:33,100 --> 00:05:35,800
better throughput and thus better speed and performance.

82
00:05:36,280 --> 00:05:41,410
And a lower beacon interval allows for faster discovery of the routers because it sends beacons more

83
00:05:41,410 --> 00:05:42,100
frequently.

84
00:05:42,250 --> 00:05:45,430
And this can help with catching the beacon in poor reception environments.

85
00:05:45,760 --> 00:05:51,790
And if we check the impressive documentation, the beacon intervals available range from 100 to 60000

86
00:05:51,790 --> 00:05:55,120
milliseconds with the default being 100 milliseconds.

87
00:05:55,360 --> 00:05:57,700
So we'll go with 100 milliseconds in this course.

88
00:05:58,740 --> 00:05:59,130
Okay.

89
00:05:59,130 --> 00:06:00,030
So let's comment.

90
00:06:00,810 --> 00:06:02,340
AP Beacon interval.

91
00:06:03,500 --> 00:06:05,060
As 100 milliseconds.

92
00:06:06,440 --> 00:06:07,400
As recommended.

93
00:06:09,140 --> 00:06:09,890
Or default.

94
00:06:10,640 --> 00:06:11,000
Okay.

95
00:06:11,000 --> 00:06:12,140
So now let's define.

96
00:06:13,980 --> 00:06:16,500
The wi fi access point IP address.

97
00:06:18,430 --> 00:06:22,930
As 192.168.0.1

98
00:06:23,830 --> 00:06:25,990
and this will be our default IP.

99
00:06:28,910 --> 00:06:34,670
And again, this is the IP that we assigned to the soft tape and we are statically configuring the interface

100
00:06:34,670 --> 00:06:35,870
of the ISP 32.

101
00:06:39,010 --> 00:06:43,420
So next, let's define the Wi-Fi app, Gateway.

102
00:06:48,690 --> 00:06:54,120
Which is also 192.168.0.1.

103
00:06:55,630 --> 00:06:57,400
And that's our AP default.

104
00:06:58,560 --> 00:06:59,130
Gateway.

105
00:07:00,800 --> 00:07:03,890
Which should be the same as the IP address.

106
00:07:05,600 --> 00:07:05,930
Okay.

107
00:07:05,930 --> 00:07:08,210
So next, let's define.

108
00:07:09,130 --> 00:07:10,960
The wi fi app net mask.

109
00:07:17,230 --> 00:07:22,180
As to 55.255.255.0.

110
00:07:25,750 --> 00:07:27,550
And that's a peanut mask.

111
00:07:28,650 --> 00:07:29,850
So next, let's define.

112
00:07:31,210 --> 00:07:32,890
The wi fi app bandwidth.

113
00:07:35,140 --> 00:07:43,150
And we can use the wi fi underscore BW underscore HD 20, and that's from the wi fi driver for a 20

114
00:07:43,150 --> 00:07:44,230
megahertz bandwidth.

115
00:07:44,440 --> 00:07:46,420
And 40 megahertz is also an option.

116
00:07:46,960 --> 00:07:52,510
And if you check the impressive documentation, the default bandwidth for station and AP mode is HD

117
00:07:52,510 --> 00:07:52,990
40.

118
00:07:53,230 --> 00:07:59,530
And in AP mode, the actual bandwidth is negotiated between the AP and the stations that connect to

119
00:07:59,530 --> 00:08:02,040
the AP and it is HD 40.

120
00:08:02,050 --> 00:08:06,820
If the AP in one of the stations supports HD 40, otherwise it's HD 20.

121
00:08:07,180 --> 00:08:10,300
And there are various options for stations slash AP mode.

122
00:08:10,510 --> 00:08:12,070
So feel free to read up on that.

123
00:08:12,460 --> 00:08:18,190
And I'll just summarize the last paragraph here that theoretically the HD 40 can gain better throughput

124
00:08:18,340 --> 00:08:25,360
because the maximum data rate can be up to 150 megabits per second or 72 megabits per second for HD

125
00:08:25,360 --> 00:08:25,750
20.

126
00:08:26,200 --> 00:08:31,510
So just summarizing and based on what I've read through, out of the resources, 20 megahertz minimizes

127
00:08:31,510 --> 00:08:35,500
channel interference but is not suitable for applications with high data rates.

128
00:08:35,770 --> 00:08:40,180
So feel free to choose the bandwidth that best suits your application while considering the surrounding

129
00:08:40,180 --> 00:08:40,690
environment.

130
00:08:40,810 --> 00:08:46,360
But I would go with 20 megahertz, so our AP bandwidth will be 20 megahertz.

131
00:08:50,530 --> 00:08:52,960
And 40 megahertz is the other option.

132
00:08:58,320 --> 00:08:58,620
Okay.

133
00:08:58,620 --> 00:09:02,820
So next let's define the WI by state power save.

134
00:09:06,220 --> 00:09:08,860
And from the driver, we'll use wi fi power.

135
00:09:08,860 --> 00:09:09,730
Save none.

136
00:09:12,420 --> 00:09:18,360
And again, let's go to the documentation and I'll just highlight that when we call S.P. Wife, I said

137
00:09:18,360 --> 00:09:19,140
power save.

138
00:09:19,140 --> 00:09:25,020
With wi fi power saved, none will disable modem sleep entirely and this has much higher power consumption

139
00:09:25,200 --> 00:09:28,980
but provides minimum latency for receiving wi fi data in real time.

140
00:09:29,430 --> 00:09:35,820
In the default mode, modem sleep mode is wi fi power save minimum modem, but will use flight five

141
00:09:35,820 --> 00:09:36,630
power save none.

142
00:09:36,990 --> 00:09:37,410
Okay.

143
00:09:37,620 --> 00:09:39,780
So Power Save is not used.

144
00:09:43,270 --> 00:09:43,660
Okay.

145
00:09:43,660 --> 00:09:45,730
So next, let's provide a definition.

146
00:09:47,580 --> 00:09:49,710
For the maximum assisted length.

147
00:09:51,530 --> 00:09:53,000
And that length is 32.

148
00:09:54,580 --> 00:09:57,430
Which is the I Tripoli standard maximum.

149
00:10:00,250 --> 00:10:04,590
Right now, let's define the maximum password length.

150
00:10:08,270 --> 00:10:09,530
And that is 64.

151
00:10:10,650 --> 00:10:12,870
And that's also the, I believe, standard.

152
00:10:16,470 --> 00:10:17,610
And next, we'll define.

153
00:10:18,650 --> 00:10:20,510
The maximum connection retrace.

154
00:10:23,640 --> 00:10:25,380
And I will use five tries.

155
00:10:26,400 --> 00:10:28,710
And this pertains to the retried number.

156
00:10:29,690 --> 00:10:30,590
On Disconnect.

157
00:10:33,320 --> 00:10:35,750
So this will take care of our basic wildfire settings.

158
00:10:36,500 --> 00:10:41,660
And just so you know where this definition comes from, this comes from the ISP, Wi-Fi types header

159
00:10:41,660 --> 00:10:42,020
file.

160
00:10:42,770 --> 00:10:47,240
And also, just so you're aware, these are the power safe mode options available.

161
00:10:48,110 --> 00:10:48,440
Okay.

162
00:10:48,440 --> 00:10:53,300
So here, let's create the network interface objects for the station and access point.

163
00:10:56,080 --> 00:10:58,950
And we'll extend this so that it's visible everywhere.

164
00:11:00,070 --> 00:11:07,960
And that's the ISP network interface structure as a pointer and call it ISP net if I stay.

165
00:11:09,110 --> 00:11:11,070
And now we'll do the same for the access point.

166
00:11:15,030 --> 00:11:17,820
And call it ESP that if AP.

167
00:11:20,230 --> 00:11:23,530
Next we'll create the message IDs for the wi fi application task.

168
00:11:32,770 --> 00:11:35,950
And I'll just make a note here for you that you can expand this.

169
00:11:37,960 --> 00:11:39,760
Based on your application requirements.

170
00:11:42,430 --> 00:11:46,990
And we'll actually expand this in the course and we'll say typedef enum.

171
00:11:49,200 --> 00:11:50,980
And we can create a tag here for it.

172
00:11:51,000 --> 00:11:55,890
It's really not necessary, but let's tag this as wi fi app message.

173
00:11:57,910 --> 00:12:00,760
And say wi fi app message.

174
00:12:01,930 --> 00:12:03,640
Start HTTP server.

175
00:12:06,160 --> 00:12:07,250
And said, it's zero.

176
00:12:08,090 --> 00:12:13,070
And we're going to send this photo SKU message where it will be received by a Wi-Fi application for

177
00:12:13,070 --> 00:12:14,000
your autos test.

178
00:12:14,210 --> 00:12:17,270
And when it's received, will handle starting the HTP server.

179
00:12:18,130 --> 00:12:21,290
Okay, so we'll also have a wi fi app message.

180
00:12:23,130 --> 00:12:25,170
Connecting from HTTP server.

181
00:12:30,000 --> 00:12:34,380
And that's to let the wife by application know when we are connecting via the HTP server.

182
00:12:34,980 --> 00:12:35,260
Okay.

183
00:12:35,260 --> 00:12:38,010
And let's also create a wi fi app message.

184
00:12:40,060 --> 00:12:41,050
Stay connected.

185
00:12:42,620 --> 00:12:43,160
IP.

186
00:12:44,840 --> 00:12:50,240
And we'll use this message to let the Wi-Fi application know when the ISP is connected to the external

187
00:12:50,240 --> 00:12:53,600
access point or router and has been assigned an IP address.

188
00:12:53,870 --> 00:12:54,230
Okay.

189
00:12:54,770 --> 00:12:57,740
And let's call this wi fi app message.

190
00:12:59,500 --> 00:13:01,060
Underscore E for Enam.

191
00:13:01,540 --> 00:13:01,870
All right.

192
00:13:01,870 --> 00:13:03,760
So we'll start with these messages for now.

193
00:13:04,180 --> 00:13:09,100
And again, these messages will be handled by a Wi-Fi application for your Toast Task State machine

194
00:13:09,220 --> 00:13:11,440
and will expand expanded as we progress in the course.

195
00:13:12,190 --> 00:13:13,150
So now let's create.

196
00:13:14,700 --> 00:13:16,010
A structure for the message.

197
00:13:16,020 --> 00:13:16,350
Q.

198
00:13:20,590 --> 00:13:25,120
And now we're really not doing much with this structure now other than sending the inner messages.

199
00:13:25,540 --> 00:13:29,620
Well, I'll leave a note here for you as a reminder that you can expand it as you like.

200
00:13:30,430 --> 00:13:33,640
So expand this based on your application requirements.

201
00:13:36,190 --> 00:13:40,870
E.g. add another type and parameter as required.

202
00:13:44,010 --> 00:13:45,780
So this will be a type to obstruct.

203
00:13:48,680 --> 00:13:50,600
Why fight up Q message.

204
00:13:54,410 --> 00:13:56,000
And we'll use our enum here.

205
00:13:56,300 --> 00:13:58,310
WI fi app message enum.

206
00:13:59,610 --> 00:14:00,870
And call it message ID.

207
00:14:02,900 --> 00:14:03,230
All right.

208
00:14:03,400 --> 00:14:05,270
Now, let's call it wi fi app.

209
00:14:07,010 --> 00:14:07,850
Q message.

210
00:14:10,240 --> 00:14:11,290
Underscore team.

211
00:14:14,380 --> 00:14:14,680
Okay.

212
00:14:14,680 --> 00:14:14,970
Good.

213
00:14:14,980 --> 00:14:16,510
So now let's make our prototype.

214
00:14:19,320 --> 00:14:21,150
Which sends a message to the Q.

215
00:14:23,900 --> 00:14:25,940
Let's add a note about the parameter here.

216
00:14:27,270 --> 00:14:28,320
And that's message it.

217
00:14:29,680 --> 00:14:33,730
Which is the message idea from the wi fi message enum.

218
00:14:38,000 --> 00:14:39,950
And the return will be true.

219
00:14:41,330 --> 00:14:43,760
If an item was successfully sent to the queue.

220
00:14:49,360 --> 00:14:50,830
Otherwise PD false.

221
00:14:55,610 --> 00:14:57,740
And this is actually all caps you.

222
00:15:00,320 --> 00:15:00,620
Okay.

223
00:15:00,650 --> 00:15:04,160
And let's add a note here, because you may want to expand this on your own.

224
00:15:05,210 --> 00:15:07,880
And I will say expand the parameter list.

225
00:15:09,950 --> 00:15:11,210
Based on your requirements.

226
00:15:13,690 --> 00:15:17,800
E.g. how you've expanded the wi fi app cube message structure.

227
00:15:29,990 --> 00:15:30,350
Okay.

228
00:15:30,350 --> 00:15:30,680
Good.

229
00:15:31,130 --> 00:15:34,760
So for the function prototype, it'll return base type T.

230
00:15:37,980 --> 00:15:39,960
And we'll call it wi fi app.

231
00:15:41,150 --> 00:15:42,080
Send message.

232
00:15:44,520 --> 00:15:47,420
And it'll take the wi fi app message enum.

233
00:15:49,440 --> 00:15:50,610
And call it message ID.

234
00:15:53,430 --> 00:15:53,710
Okay.

235
00:15:53,730 --> 00:15:54,240
It looks good.

236
00:15:55,490 --> 00:15:56,630
And the next prototype.

237
00:15:57,810 --> 00:15:58,620
It starts the way.

238
00:15:58,660 --> 00:15:59,050
Fine.

239
00:16:00,230 --> 00:16:01,250
Auto task.

240
00:16:03,860 --> 00:16:07,430
And let's say void wi fi app start.

241
00:16:08,780 --> 00:16:10,130
And it takes no parameters.

242
00:16:12,150 --> 00:16:12,450
All right.

243
00:16:12,450 --> 00:16:15,180
So for the head of file, that should be all we need for now.

244
00:16:15,960 --> 00:16:18,330
And it looks like there's a typo here, so let's fix that.

245
00:16:18,630 --> 00:16:24,240
It should be 2552552550 for the net mask.

246
00:16:25,630 --> 00:16:25,720
And.

247
00:16:25,810 --> 00:16:26,320
Okay, great.

248
00:16:26,320 --> 00:16:31,150
So I'll stop right here and we'll continue programming the wi fi application that C file for the next

249
00:16:31,150 --> 00:16:31,450
one.

250
00:16:31,900 --> 00:16:36,460
And be sure to check the resources for this lesson if you need further clarification on the topics covered.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,620 --> 00:00:06,890
All right.

2
00:00:06,890 --> 00:00:11,290
So first in the Task's common header file, we're going to define the task information for the Wi-Fi

3
00:00:11,300 --> 00:00:13,310
application freertos task.

4
00:00:13,770 --> 00:00:14,090
Okay.

5
00:00:14,090 --> 00:00:18,140
So here we'll define details for the Wi-Fi application task.

6
00:00:21,030 --> 00:00:25,290
And we'll define here the Wi-Fi app task stack size.

7
00:00:28,390 --> 00:00:30,430
As 4096 bytes.

8
00:00:32,630 --> 00:00:36,500
Next to find the Wi-Fi app task priority.

9
00:00:39,400 --> 00:00:40,810
And we can make it five.

10
00:00:41,530 --> 00:00:44,530
Next to find the Wi-Fi app Task Core ID.

11
00:00:48,260 --> 00:00:49,250
As core zero.

12
00:00:50,620 --> 00:00:51,610
All right, so that's it.

13
00:00:51,610 --> 00:00:55,990
So now we can head over to the Wi-Fi APK file and we need Freertos.

14
00:00:55,990 --> 00:00:58,300
So let's include Freertos.

15
00:01:01,880 --> 00:01:03,750
Slash free auto stage.

16
00:01:06,150 --> 00:01:07,830
And will eventually use event groups.

17
00:01:07,830 --> 00:01:09,750
So include freertos.

18
00:01:11,030 --> 00:01:13,070
Slash event group stage.

19
00:01:16,140 --> 00:01:18,570
Next include Freertos.

20
00:01:20,380 --> 00:01:26,500
Slash task H And we'll also need to include esp error dot h.

21
00:01:30,000 --> 00:01:32,010
Let's also include the ESP log.

22
00:01:36,650 --> 00:01:39,680
And next include the ISP Wi-Fi.

23
00:01:42,530 --> 00:01:45,110
Dot h for our Wi-Fi driver.

24
00:01:46,200 --> 00:01:47,820
And let's also include.

25
00:01:49,240 --> 00:01:52,380
Lightweight IP slash net d.b.h.

26
00:01:53,950 --> 00:01:56,110
And include here the RGB.

27
00:01:57,920 --> 00:01:58,340
Led.

28
00:02:00,590 --> 00:02:04,180
We also need our tasks underscore common dot h.

29
00:02:06,690 --> 00:02:09,290
And of course, we need our Wi-Fi app, which.

30
00:02:11,450 --> 00:02:15,590
Next we'll create a tag use for ESP serial console messages.

31
00:02:17,930 --> 00:02:21,620
And we'll say static const char tag.

32
00:02:25,020 --> 00:02:27,480
And call it wifi underscore app.

33
00:02:30,230 --> 00:02:32,330
And here, let's create a handle.

34
00:02:34,410 --> 00:02:36,990
Used to manipulate the main queue of events here.

35
00:02:40,940 --> 00:02:43,220
And we'll say static cue handle.

36
00:02:45,970 --> 00:02:47,080
Underscore t.

37
00:02:48,130 --> 00:02:50,830
And call it wi fi app handle.

38
00:02:55,180 --> 00:02:57,970
And next we'll need the network interface objects.

39
00:02:58,650 --> 00:03:00,930
For the station and access point.

40
00:03:03,660 --> 00:03:12,600
And that'll be esp net if underscore t pointer to our extend esp net if sta variable.

41
00:03:13,410 --> 00:03:15,240
And let's initialize that to null.

42
00:03:15,660 --> 00:03:19,200
We also need our ASP.Net if app variable.

43
00:03:25,090 --> 00:03:26,950
Initialize to null as well.

44
00:03:27,720 --> 00:03:28,560
All right, good.

45
00:03:28,800 --> 00:03:31,410
So now let's head over to the Wi-Fi app header file.

46
00:03:32,910 --> 00:03:34,680
And we can grab our prototypes.

47
00:03:37,440 --> 00:03:39,690
And let's define them here in the dot C file.

48
00:03:45,270 --> 00:03:48,600
So let's first define our wi fi app start function.

49
00:03:49,240 --> 00:03:54,820
And in this function we'll handle some initializations and also define the Wi-Fi app RTOs task.

50
00:03:54,940 --> 00:04:02,230
So first here, we're going to log a message and we're going to use ESP log info and say Tag.

51
00:04:03,100 --> 00:04:05,020
Starting Wi-Fi application.

52
00:04:08,830 --> 00:04:15,370
Okay so this is log information will take our tag and our message string and log it to the serial console.

53
00:04:15,970 --> 00:04:16,600
All right.

54
00:04:16,870 --> 00:04:19,540
So next, we'll start our wi fi started.

55
00:04:20,840 --> 00:04:26,030
Led and say RGB led Wi-Fi app started.

56
00:04:28,560 --> 00:04:32,190
And next, we'll need to disable default Wi-Fi logging messages.

57
00:04:36,170 --> 00:04:39,280
Because we don't want so many messages logged to the console.

58
00:04:39,290 --> 00:04:43,220
And for that we'll say ESP log level.

59
00:04:47,840 --> 00:04:51,380
WI fi and the level is esp log none.

60
00:04:56,420 --> 00:04:59,210
All right, so now we'll create a message queue.

61
00:05:01,610 --> 00:05:04,130
Using our Wi-Fi app handle.

62
00:05:06,660 --> 00:05:08,610
And use SSC create.

63
00:05:12,430 --> 00:05:15,670
To create a queue capable of holding the size of three.

64
00:05:17,730 --> 00:05:24,030
A var wi fi app message structures so we can just simply grab our wi fi app message struct.

65
00:05:24,920 --> 00:05:25,910
Place it here.

66
00:05:27,700 --> 00:05:31,870
And next, let's start the Wi-Fi application task.

67
00:05:34,950 --> 00:05:38,010
And for that we'll use X task, create PIN two core.

68
00:05:40,940 --> 00:05:44,300
And here we'll put a reference to the task function that will create.

69
00:05:45,220 --> 00:05:47,290
Call it Wi-Fi app task.

70
00:05:49,270 --> 00:05:52,000
And here add the name Wi-Fi App task.

71
00:05:53,910 --> 00:05:57,600
Next, we'll enter the Wi-Fi app stack size.

72
00:06:01,400 --> 00:06:05,840
And here this is null as we're not passing any parameters.

73
00:06:06,800 --> 00:06:08,390
And now put the Wi-Fi app.

74
00:06:09,520 --> 00:06:10,900
Task priority.

75
00:06:15,750 --> 00:06:19,620
And the next one is null as we aren't using a task handle.

76
00:06:20,550 --> 00:06:24,360
And here this is our Wi-Fi app Task Core ID.

77
00:06:28,470 --> 00:06:28,710
Right.

78
00:06:28,710 --> 00:06:30,690
So now let's head over to the wi fi app.

79
00:06:30,690 --> 00:06:32,100
Send message function.

80
00:06:33,160 --> 00:06:37,210
So first we'll create an instance of our Wi-Fi app message struct.

81
00:06:44,800 --> 00:06:46,180
And call it message.

82
00:06:46,660 --> 00:06:51,670
And then we'll set the message ID to the message ID passed into the function.

83
00:06:54,580 --> 00:07:01,480
And we're going to return the result of sending to our queue using ZK send.

84
00:07:04,110 --> 00:07:06,240
And we have to specify the handle.

85
00:07:08,850 --> 00:07:10,890
And the reference to the message.

86
00:07:11,670 --> 00:07:14,310
And the timeout will be Port Max DeLay.

87
00:07:20,050 --> 00:07:24,970
So here we're going to pass a message to the function and then send it through the queue specifying

88
00:07:24,970 --> 00:07:25,750
our handle.

89
00:07:27,760 --> 00:07:33,610
And like I said, so far, we're only we only have these messages here available.

90
00:07:37,390 --> 00:07:37,690
Right.

91
00:07:37,690 --> 00:07:41,920
So now let's define the main task for the Wi-Fi application.

92
00:07:44,140 --> 00:07:47,590
And the parameters is a pointer variable parameter.

93
00:07:50,220 --> 00:07:52,020
Which can be passed to the function.

94
00:07:54,410 --> 00:07:58,640
And here we're going to say static void Wi-Fi app task.

95
00:08:00,600 --> 00:08:02,190
And it's a void pointer.

96
00:08:02,520 --> 00:08:03,870
PV parameter.

97
00:08:06,440 --> 00:08:11,990
And now this will be our main task for the Wi-Fi application, where we initialize Wi-Fi and receive

98
00:08:11,990 --> 00:08:15,020
all messages which determines the flow of the application.

99
00:08:15,640 --> 00:08:23,110
So we'll need to define some set up functions which initialize the event handler and the TCP IP stack

100
00:08:23,110 --> 00:08:26,980
and the Wi-Fi config, as well as the soft AP config.

101
00:08:26,980 --> 00:08:30,670
Before we start Wi-Fi and send the first message to the queue.

102
00:08:30,820 --> 00:08:36,040
So I'll lay them all out right here first and then we'll define them one by one.

103
00:08:36,040 --> 00:08:41,470
So let's create an instance of the Wi-Fi app queue message struct and call it message.

104
00:08:43,530 --> 00:08:46,860
Then next, we'll initialize the event handler.

105
00:08:49,470 --> 00:08:53,310
And we'll create a function called Fi app event handler in it.

106
00:09:00,130 --> 00:09:03,670
Also, we'll need to initialize the TCP IP stack.

107
00:09:06,540 --> 00:09:08,520
And wi fi config.

108
00:09:09,220 --> 00:09:12,160
And we're going to call it wi fi app default.

109
00:09:12,190 --> 00:09:13,240
WI fi.

110
00:09:14,010 --> 00:09:14,700
In it.

111
00:09:16,480 --> 00:09:19,480
And then next we'll do the same for the soft app.config.

112
00:09:22,920 --> 00:09:24,360
And call it fi app.

113
00:09:24,460 --> 00:09:26,130
Soft Appconfig.

114
00:09:29,260 --> 00:09:31,090
And then here we can start wi fi.

115
00:09:35,070 --> 00:09:39,600
And here let's esp error check so we'll know if the function returns an error.

116
00:09:44,750 --> 00:09:46,700
So call esp wi fi.

117
00:09:46,700 --> 00:09:47,510
Start now.

118
00:09:54,170 --> 00:09:57,260
Then next we can send the first event message.

119
00:09:59,080 --> 00:10:01,060
And we'll use a Wi-Fi app.

120
00:10:01,060 --> 00:10:02,110
Send message.

121
00:10:03,620 --> 00:10:07,880
And send the Wi-Fi app start http server message.

122
00:10:13,670 --> 00:10:16,150
All right, so now we can create our endless loop.

123
00:10:16,160 --> 00:10:17,360
So come here.

124
00:10:18,010 --> 00:10:22,510
And we're going to say four with two semicolons in parentheses.

125
00:10:24,460 --> 00:10:28,060
And then say if X receive.

126
00:10:30,700 --> 00:10:33,550
And for the first parameter we need our queue handle.

127
00:10:37,450 --> 00:10:40,810
For the second parameter, we need a reference to the message.

128
00:10:42,500 --> 00:10:43,610
Our message right here.

129
00:10:43,610 --> 00:10:44,180
Right.

130
00:10:44,980 --> 00:10:48,040
And for the third parameter, it will be Port Max DeLay.

131
00:10:53,340 --> 00:10:54,990
And now we'll say switch.

132
00:10:55,260 --> 00:10:56,850
Message Dot.

133
00:10:56,850 --> 00:10:57,720
Message ID.

134
00:11:01,550 --> 00:11:05,480
In the first case will be Wi-Fi app message start Http server.

135
00:11:09,850 --> 00:11:10,660
Okay, great.

136
00:11:12,780 --> 00:11:16,680
And here we can log a message using esp log information.

137
00:11:18,070 --> 00:11:19,360
With our tag.

138
00:11:20,750 --> 00:11:23,350
And our message, which will be the message.

139
00:11:25,880 --> 00:11:29,810
And then we'll create a function called Http server start.

140
00:11:33,800 --> 00:11:35,030
And we'll define this later.

141
00:11:35,030 --> 00:11:37,130
So just comment it out for now.

142
00:11:38,650 --> 00:11:43,300
And then we'll call our RGB led Http server started function here.

143
00:11:44,200 --> 00:11:45,790
And then we can include a break.

144
00:11:46,810 --> 00:11:50,710
And the next case for Wi-Fi app message.

145
00:11:52,190 --> 00:11:54,710
Connecting from Http server.

146
00:11:54,980 --> 00:11:58,280
And then just log a message for this case for now.

147
00:12:06,590 --> 00:12:07,940
And then include the break.

148
00:12:08,840 --> 00:12:12,620
In the next case will be the Wi-Fi app message.

149
00:12:13,400 --> 00:12:14,440
Stay connected.

150
00:12:14,450 --> 00:12:15,290
Got IP?

151
00:12:16,820 --> 00:12:17,990
Log the message here.

152
00:12:25,930 --> 00:12:29,170
And then we're going to call RGB led Wi-Fi connected.

153
00:12:33,450 --> 00:12:34,620
And then we're going to break.

154
00:12:36,130 --> 00:12:38,440
And also we can leave a default break right here.

155
00:12:44,360 --> 00:12:46,640
Okay, next we can start defining these functions.

156
00:12:46,640 --> 00:12:48,760
But I think now is a good time to take a break.

157
00:12:48,770 --> 00:12:53,510
So let's continue with defining the Wi-Fi app event handler init function in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,090 --> 00:00:11,140
Okay, let's pick up where we left off and define the event handler init function.

2
00:00:11,140 --> 00:00:12,370
So copy it.

3
00:00:14,480 --> 00:00:16,130
And let's make a comment here.

4
00:00:17,590 --> 00:00:19,810
Initializes the Wi-Fi application.

5
00:00:22,570 --> 00:00:26,710
Event handler for wi fi and IP events.

6
00:00:29,730 --> 00:00:33,780
In this function will be static, void or function name.

7
00:00:34,580 --> 00:00:36,320
And it takes no parameters.

8
00:00:39,130 --> 00:00:42,760
And here we'll say event loop for the wi fi driver.

9
00:00:44,730 --> 00:00:46,680
And now let's check.

10
00:00:49,730 --> 00:00:51,620
ESP event loop create.

11
00:00:53,490 --> 00:00:55,080
And choose create default.

12
00:00:59,210 --> 00:00:59,870
All right.

13
00:01:00,510 --> 00:01:04,410
And next, we'll create the event handler for the connection.

14
00:01:06,760 --> 00:01:10,240
And then we'll need an ESP event handler instance type.

15
00:01:18,680 --> 00:01:21,290
And call it instance wi fi event.

16
00:01:25,260 --> 00:01:27,060
And now copy the instance type.

17
00:01:28,270 --> 00:01:29,290
And paste it.

18
00:01:30,120 --> 00:01:32,820
And now here, call it instance IP event.

19
00:01:35,830 --> 00:01:37,780
And next esp error check.

20
00:01:40,500 --> 00:01:42,060
ESP event handler.

21
00:01:42,870 --> 00:01:44,190
Instance, register.

22
00:01:47,710 --> 00:01:50,320
And the event base is wi fi event.

23
00:01:53,520 --> 00:01:56,790
The event id is esp event id.

24
00:02:01,000 --> 00:02:07,240
And the event handler is a reference to the function name, which we'll call Wi-Fi app Eventhandler.

25
00:02:12,540 --> 00:02:14,280
The handler arguments are null.

26
00:02:16,190 --> 00:02:19,880
And instance, will be a reference to instance wi fi event.

27
00:02:22,120 --> 00:02:23,590
And now copy this line.

28
00:02:26,150 --> 00:02:27,320
And paste below.

29
00:02:28,740 --> 00:02:30,570
And now we want IP events.

30
00:02:35,030 --> 00:02:36,920
And the ID is the same.

31
00:02:37,990 --> 00:02:41,260
The handler is the same and this is null.

32
00:02:42,040 --> 00:02:44,980
And change the reference to instance IP event.

33
00:02:47,520 --> 00:02:48,540
And that's it.

34
00:02:49,360 --> 00:02:51,610
So now we need to define this event handler.

35
00:02:53,860 --> 00:02:55,120
So let's come here.

36
00:02:59,010 --> 00:03:00,240
And let's comment.

37
00:03:00,600 --> 00:03:03,720
WI fi application event handler.

38
00:03:07,910 --> 00:03:10,880
And the first parameter is data.

39
00:03:10,910 --> 00:03:12,590
Aside from event data.

40
00:03:14,650 --> 00:03:16,480
That is passed to the handler.

41
00:03:17,610 --> 00:03:18,900
When it is called.

42
00:03:21,010 --> 00:03:24,250
And the second parameter event base.

43
00:03:25,890 --> 00:03:30,360
Is the base ID of the event to register the handler for.

44
00:03:34,190 --> 00:03:36,410
In the third parameter event ID.

45
00:03:38,340 --> 00:03:41,520
Is the idea of the event to register the handler for.

46
00:03:47,070 --> 00:03:49,770
And the fourth parameter event data.

47
00:03:51,060 --> 00:03:52,440
Is the event data.

48
00:03:56,650 --> 00:03:58,720
So this function is static void.

49
00:03:59,390 --> 00:04:00,290
WI fi app.

50
00:04:00,320 --> 00:04:01,280
Event Handler.

51
00:04:01,870 --> 00:04:05,050
In the first parameter is a void pointer arg.

52
00:04:05,710 --> 00:04:09,040
The next parameter is esp event based type.

53
00:04:11,220 --> 00:04:12,660
And its event base.

54
00:04:13,270 --> 00:04:15,130
The next is in 32.

55
00:04:16,220 --> 00:04:17,000
Event ID.

56
00:04:18,380 --> 00:04:20,480
And the last is a void pointer.

57
00:04:20,510 --> 00:04:21,590
Event Data.

58
00:04:24,000 --> 00:04:25,740
Then here we'll say if.

59
00:04:26,550 --> 00:04:27,660
Event base.

60
00:04:29,090 --> 00:04:30,500
Is a wi fi event.

61
00:04:33,680 --> 00:04:34,970
Then we'll switch.

62
00:04:35,710 --> 00:04:36,580
Event ID.

63
00:04:38,880 --> 00:04:40,560
And then now we'll open a case.

64
00:04:42,270 --> 00:04:43,800
For wi fi event.

65
00:04:45,550 --> 00:04:46,420
AP start.

66
00:04:51,520 --> 00:04:55,990
And now let's log the message for this case with esp log info.

67
00:04:56,810 --> 00:04:57,620
Our tag.

68
00:04:58,880 --> 00:05:02,030
And the messages wi fi event app start.

69
00:05:03,670 --> 00:05:04,990
And then include a break.

70
00:05:08,080 --> 00:05:11,040
And this wi fi event here is just one of many.

71
00:05:11,050 --> 00:05:16,150
So come here and look over the type of events you can include and just create them in the event handler

72
00:05:16,150 --> 00:05:18,250
and you can handle them in your application.

73
00:05:18,990 --> 00:05:20,550
So let's copy this event.

74
00:05:21,660 --> 00:05:22,770
And we'll create another.

75
00:05:24,450 --> 00:05:25,480
For Wi-Fi.

76
00:05:25,530 --> 00:05:26,550
AP Stop.

77
00:05:29,110 --> 00:05:30,790
And now let's create another event.

78
00:05:35,080 --> 00:05:36,700
For Star Start.

79
00:05:41,770 --> 00:05:43,060
And now let's do the same.

80
00:05:47,800 --> 00:05:49,120
For stay connected.

81
00:05:54,400 --> 00:05:55,800
Now let's do another one.

82
00:05:59,490 --> 00:06:01,200
For stay disconnected.

83
00:06:01,970 --> 00:06:03,980
Let's come back up here and make another one.

84
00:06:08,140 --> 00:06:10,420
For AP stay connected.

85
00:06:16,060 --> 00:06:17,710
And now let's make another one.

86
00:06:20,230 --> 00:06:22,600
For app stay disconnected.

87
00:06:30,870 --> 00:06:31,410
All right, good.

88
00:06:31,410 --> 00:06:33,540
So that should cover our basic needs for now.

89
00:06:34,170 --> 00:06:38,030
And now let's come down here and say if.

90
00:06:39,230 --> 00:06:40,310
Event base.

91
00:06:41,670 --> 00:06:43,050
Is an event.

92
00:06:46,670 --> 00:06:49,190
Then say switch event ID.

93
00:06:52,400 --> 00:06:54,110
And let's create a new case here.

94
00:06:55,620 --> 00:06:56,710
IP event.

95
00:06:57,180 --> 00:06:57,660
SDA.

96
00:06:58,630 --> 00:06:59,410
Got IP.

97
00:07:08,150 --> 00:07:10,240
And now let's plug info.

98
00:07:12,380 --> 00:07:13,490
The message.

99
00:07:14,340 --> 00:07:16,710
For the star gossip event.

100
00:07:18,100 --> 00:07:19,210
And then let's break.

101
00:07:20,900 --> 00:07:21,260
All right.

102
00:07:21,260 --> 00:07:22,550
So that's it for this one.

103
00:07:24,040 --> 00:07:27,040
Now we can define the default Wi-Fi init function.

104
00:07:30,310 --> 00:07:31,540
And let's comment.

105
00:07:32,310 --> 00:07:34,440
Initializes the TCP stack.

106
00:07:36,450 --> 00:07:38,550
In default Wi-Fi configuration.

107
00:07:42,370 --> 00:07:46,480
And it's static void our function and it's void.

108
00:07:47,910 --> 00:07:51,220
And first we'll say initialize the TCP stack.

109
00:07:56,230 --> 00:07:57,970
And esp error check.

110
00:08:00,290 --> 00:08:02,270
The ESP net if.

111
00:08:03,000 --> 00:08:04,080
Init function.

112
00:08:07,960 --> 00:08:10,780
And next we'll do the default Wi-Fi config.

113
00:08:13,870 --> 00:08:17,590
And I'll just mention that operations must be in this order.

114
00:08:20,760 --> 00:08:24,300
Now we need an instance of the Wi-Fi init config type.

115
00:08:28,790 --> 00:08:31,040
And call it wi fi init config.

116
00:08:33,030 --> 00:08:36,510
And initialize it with wi-fi init config.

117
00:08:37,450 --> 00:08:38,620
Default function.

118
00:08:40,190 --> 00:08:42,410
And so here is error check.

119
00:08:45,250 --> 00:08:46,780
ESP wi fi in it.

120
00:08:48,000 --> 00:08:51,060
And pass a reference to this wi fi in it config.

121
00:08:56,660 --> 00:08:58,760
And the next will be check.

122
00:09:00,720 --> 00:09:01,620
ESP wi fi.

123
00:09:01,650 --> 00:09:03,900
Set storage as.

124
00:09:03,930 --> 00:09:05,400
WI fi storage ram.

125
00:09:11,750 --> 00:09:15,080
And now let's grab our network interface star object.

126
00:09:18,290 --> 00:09:19,760
And let's initialize it.

127
00:09:23,190 --> 00:09:25,290
Using esp net if.

128
00:09:26,160 --> 00:09:27,750
Create default Wi-Fi.

129
00:09:29,060 --> 00:09:29,480
Stay.

130
00:09:32,370 --> 00:09:34,740
Then let's initialize the object.

131
00:09:36,680 --> 00:09:38,740
Using esp net if.

132
00:09:39,710 --> 00:09:41,090
Create default.

133
00:09:41,900 --> 00:09:43,070
WI fi app.

134
00:09:45,770 --> 00:09:46,100
Great.

135
00:09:46,100 --> 00:09:46,730
That's it.

136
00:09:47,550 --> 00:09:49,770
Now let's create the soft config.

137
00:09:52,870 --> 00:09:54,040
And let's comment.

138
00:09:54,720 --> 00:09:57,300
Configures the Wi-Fi access point settings.

139
00:09:59,110 --> 00:10:00,880
And assigns the static IP.

140
00:10:03,250 --> 00:10:04,420
To the soft AP.

141
00:10:07,920 --> 00:10:13,980
And it's a static void Wi-Fi app, soft app config, and it's void.

142
00:10:15,400 --> 00:10:20,460
Right now, let's say Softap Wi-Fi access point configuration.

143
00:10:23,750 --> 00:10:26,450
And now create the Wi-Fi config structure.

144
00:10:29,470 --> 00:10:31,300
And call it Appconfig.

145
00:10:34,830 --> 00:10:38,010
And here we'll need to specify the access point config.

146
00:10:43,410 --> 00:10:44,250
Like so.

147
00:10:45,400 --> 00:10:47,050
And then set the skid.

148
00:10:49,910 --> 00:10:51,480
To our Wi-Fi app.

149
00:10:51,670 --> 00:10:52,220
Sid.

150
00:10:57,010 --> 00:10:59,440
Next, set the side length.

151
00:11:01,050 --> 00:11:05,010
Using strlen of Wi-Fi ssid.

152
00:11:08,740 --> 00:11:10,090
And then the password.

153
00:11:14,400 --> 00:11:16,860
Will be our Wi-Fi password.

154
00:11:20,270 --> 00:11:21,500
And next, the channel.

155
00:11:22,710 --> 00:11:24,780
Will be our wi fi channel.

156
00:11:29,020 --> 00:11:30,850
And then side hidden.

157
00:11:34,120 --> 00:11:37,630
Is Wi-Fi ssid hidden?

158
00:11:38,810 --> 00:11:40,370
An authorization mode.

159
00:11:44,050 --> 00:11:46,120
We'll use wi fi auth.

160
00:11:47,800 --> 00:11:49,240
WPA to.

161
00:11:55,610 --> 00:11:56,360
And now Max.

162
00:11:56,360 --> 00:11:57,200
Connections.

163
00:11:59,840 --> 00:12:01,490
Will be wi fi app.

164
00:12:02,940 --> 00:12:04,350
Max connections.

165
00:12:07,270 --> 00:12:08,830
And then beacon interval.

166
00:12:12,760 --> 00:12:16,240
Will be Wi-Fi app beacon interval.

167
00:12:20,930 --> 00:12:22,910
This should be actually be a comma here.

168
00:12:25,380 --> 00:12:26,430
Now, let's.

169
00:12:27,070 --> 00:12:28,510
Configure Dhcp.

170
00:12:29,830 --> 00:12:31,240
For the access point.

171
00:12:33,430 --> 00:12:37,630
And now let's create an instance of the ESP net if IP info type.

172
00:12:42,690 --> 00:12:45,450
And call it app IP info.

173
00:12:46,670 --> 00:12:48,620
And now let's set this.

174
00:12:50,220 --> 00:12:51,690
AP IP info.

175
00:12:55,120 --> 00:12:59,620
To zero for the size of the apip info.

176
00:13:01,370 --> 00:13:01,640
All right.

177
00:13:01,640 --> 00:13:03,500
Because we want this cleared out first.

178
00:13:04,410 --> 00:13:06,360
And now call ESPN net.

179
00:13:06,390 --> 00:13:06,930
If.

180
00:13:08,210 --> 00:13:09,230
Dhcp.

181
00:13:09,650 --> 00:13:10,340
Stop.

182
00:13:12,350 --> 00:13:14,840
And that's for our ISP net if app.

183
00:13:20,290 --> 00:13:27,250
And this function stops the Dhcp server and we want to do this before making any Dhcp related updates.

184
00:13:27,870 --> 00:13:31,500
And again that's for our net if AP object here.

185
00:13:33,750 --> 00:13:37,020
And we'll say, must call this first.

186
00:13:37,680 --> 00:13:40,650
Because we want to call this first before making any changes.

187
00:13:41,380 --> 00:13:42,790
And then let's call init.

188
00:13:45,530 --> 00:13:47,570
And specify afinet.

189
00:13:49,410 --> 00:13:50,500
Then wifi.

190
00:13:50,550 --> 00:13:51,390
AP IP.

191
00:13:53,820 --> 00:13:56,820
With the reference to our AP IP info.

192
00:13:58,850 --> 00:14:00,170
That IP address.

193
00:14:02,140 --> 00:14:05,160
And I'll say here, assign access points.

194
00:14:05,170 --> 00:14:06,010
Static IP.

195
00:14:08,720 --> 00:14:11,120
Gateway and Netmask.

196
00:14:11,980 --> 00:14:17,410
And what this function does is, is it converts an Internet address in its standard text format into

197
00:14:17,410 --> 00:14:18,970
its numeric binary form.

198
00:14:18,970 --> 00:14:20,350
And that's what we want here.

199
00:14:20,710 --> 00:14:25,750
So now let's copy this line, then let's do the same for Gateway.

200
00:14:31,320 --> 00:14:32,430
And Gateway here.

201
00:14:33,760 --> 00:14:35,350
And then again for Netmask.

202
00:14:40,160 --> 00:14:41,390
And that mask here.

203
00:14:43,910 --> 00:14:44,720
All right, great.

204
00:14:46,900 --> 00:14:48,940
So now let's esp error check.

205
00:14:51,350 --> 00:14:53,750
ESP net if set.

206
00:14:53,780 --> 00:14:54,740
IP info.

207
00:14:56,560 --> 00:15:01,870
And specify our ISP net if AP and a reference to our AP IP info.

208
00:15:04,450 --> 00:15:06,100
And now esp error check.

209
00:15:08,680 --> 00:15:10,030
ESP net if.

210
00:15:11,530 --> 00:15:13,540
Dhcp start.

211
00:15:15,130 --> 00:15:19,210
And again use our ASP.Net if app object.

212
00:15:22,270 --> 00:15:23,770
And here I'll just comment.

213
00:15:25,100 --> 00:15:28,430
Statically configures the network interface.

214
00:15:31,210 --> 00:15:32,230
And this one.

215
00:15:33,250 --> 00:15:34,330
Starts the AP.

216
00:15:35,940 --> 00:15:37,650
Dhcp server.

217
00:15:39,100 --> 00:15:40,690
For connecting stations.

218
00:15:43,820 --> 00:15:45,890
E.g. your mobile device.

219
00:15:49,780 --> 00:15:51,640
And now let's check.

220
00:15:53,150 --> 00:15:54,680
ESP set mode.

221
00:15:58,110 --> 00:16:00,390
In the mode we want is wi fi mode.

222
00:16:01,290 --> 00:16:02,370
AP star.

223
00:16:07,860 --> 00:16:13,380
And here we are setting the mode as access point.

224
00:16:15,320 --> 00:16:16,820
Slash station mode.

225
00:16:18,590 --> 00:16:20,510
And then let's check.

226
00:16:22,630 --> 00:16:23,740
ESP wi fi.

227
00:16:25,600 --> 00:16:26,740
Set config.

228
00:16:30,160 --> 00:16:32,380
For ISP interface.

229
00:16:34,730 --> 00:16:36,530
Wi-Fi access point.

230
00:16:38,060 --> 00:16:40,070
And reference the AP config.

231
00:16:43,030 --> 00:16:43,750
And here.

232
00:16:44,660 --> 00:16:46,700
We've set our configuration.

233
00:16:48,820 --> 00:16:50,610
And then check.

234
00:16:53,660 --> 00:16:55,730
ESP wi fi set bandwidth.

235
00:16:56,550 --> 00:16:59,190
For our Wi-Fi interface access point.

236
00:17:02,950 --> 00:17:05,410
And use our Wi-Fi bandwidth.

237
00:17:09,770 --> 00:17:11,780
And that's for our default bandwidth.

238
00:17:13,950 --> 00:17:15,150
20MHz.

239
00:17:23,050 --> 00:17:25,000
And again, let's check.

240
00:17:28,590 --> 00:17:29,610
ESP wi fi.

241
00:17:30,460 --> 00:17:31,270
Set power.

242
00:17:31,270 --> 00:17:31,960
Save.

243
00:17:32,620 --> 00:17:35,050
To our Wi-Fi star power save.

244
00:17:41,520 --> 00:17:43,860
And that's our power save set to none.

245
00:17:49,570 --> 00:17:52,930
Which we previously defined here in the header file.

246
00:17:55,820 --> 00:17:57,710
Okay, so now I'll just inspect this.

247
00:17:58,040 --> 00:17:59,240
This looks good.

248
00:18:01,770 --> 00:18:05,040
And up here, this message, This should be disconnected.

249
00:18:05,640 --> 00:18:07,050
So let's log it correctly.

250
00:18:07,640 --> 00:18:09,260
And so just be sure of that.

251
00:18:10,000 --> 00:18:11,620
And then now this should be static.

252
00:18:13,900 --> 00:18:16,600
Okay, now let's build to be sure there's no errors.

253
00:18:26,690 --> 00:18:26,940
Okay.

254
00:18:26,940 --> 00:18:27,920
And that looks good.

255
00:18:28,070 --> 00:18:30,680
So let's finalize and test this in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,900 --> 00:00:10,270
Okay, now we're going to start the Wi-Fi application so we can test it.

2
00:00:10,290 --> 00:00:13,350
So first let's go down to the Wi-Fi app, Start function.

3
00:00:15,040 --> 00:00:17,970
And copy it and then go to Main.c.

4
00:00:19,970 --> 00:00:23,630
And first, let's clean this up and make a comment.

5
00:00:24,450 --> 00:00:26,160
Application entry point.

6
00:00:29,900 --> 00:00:32,480
And now let's include knbs.

7
00:00:32,480 --> 00:00:33,200
Fleshpot.

8
00:00:36,020 --> 00:00:37,850
And we also want to include.

9
00:00:39,560 --> 00:00:40,550
Our Wi-Fi app.

10
00:00:44,560 --> 00:00:46,330
And now let's clear out the main.

11
00:00:47,080 --> 00:00:50,110
And say initialize NVS.

12
00:00:52,670 --> 00:00:58,070
And here we're going to initialize non-volatile storage in the recommended manner because it actually

13
00:00:58,070 --> 00:01:03,920
attempts to handle errors by erasing the flash and retrying instead of simply aborting as the ESP error

14
00:01:03,950 --> 00:01:04,880
check would do.

15
00:01:04,910 --> 00:01:07,940
So here, let's say esp error type.

16
00:01:08,820 --> 00:01:12,030
Return equals envz flush init.

17
00:01:15,060 --> 00:01:17,010
And then say if return.

18
00:01:17,740 --> 00:01:21,100
Is esp error nvs.

19
00:01:21,130 --> 00:01:22,570
No free pages.

20
00:01:25,000 --> 00:01:26,260
Or the return.

21
00:01:27,060 --> 00:01:28,530
Is esp error.

22
00:01:30,030 --> 00:01:32,400
Enb's new version found.

23
00:01:36,400 --> 00:01:38,500
Then we'll error check.

24
00:01:42,140 --> 00:01:43,790
Envious, flashy race.

25
00:01:47,150 --> 00:01:48,760
Then Now set the return.

26
00:01:49,410 --> 00:01:51,870
To the result of flesh in it.

27
00:01:56,930 --> 00:01:58,880
Then let's esp error check.

28
00:02:01,650 --> 00:02:03,270
The final return result.

29
00:02:05,890 --> 00:02:10,480
And we're only checking for these specific errors as not all errors can be resolved by flashing and

30
00:02:10,480 --> 00:02:11,290
retrying.

31
00:02:11,640 --> 00:02:12,010
Right.

32
00:02:12,010 --> 00:02:14,650
So if we follow the no free pages error.

33
00:02:16,120 --> 00:02:21,670
This happens when the partition doesn't contain any empty pages, and here it's recommended to erase

34
00:02:21,670 --> 00:02:25,240
the whole partition and call NVS flash init again.

35
00:02:29,740 --> 00:02:31,540
And the new version found.

36
00:02:32,330 --> 00:02:38,960
This happens when the partition contains data in a new format that's not recognized by this version

37
00:02:38,990 --> 00:02:39,710
of code.

38
00:02:41,950 --> 00:02:42,480
Right.

39
00:02:42,480 --> 00:02:43,700
So now let's start.

40
00:02:43,710 --> 00:02:44,490
WI fi.

41
00:02:45,370 --> 00:02:47,350
By calling Wi-Fi app Start.

42
00:02:50,920 --> 00:02:51,280
And then.

43
00:02:51,280 --> 00:02:52,270
Now let's build.

44
00:03:01,810 --> 00:03:03,280
And flash when you're ready.

45
00:03:14,270 --> 00:03:19,040
And now let's keep our event handler messages handy here while we open a terminal.

46
00:03:20,080 --> 00:03:22,420
So let's come here and open a terminal.

47
00:03:30,990 --> 00:03:36,510
And here the terminal shows a couple of messages from the event handler and also a few messages here.

48
00:03:38,330 --> 00:03:40,070
So there's our AP start.

49
00:03:44,110 --> 00:03:47,230
And our start Http server message as well.

50
00:03:49,870 --> 00:03:51,400
All right, great.

51
00:03:53,180 --> 00:03:54,800
So now let's try to connect.

52
00:03:55,840 --> 00:04:00,550
So just go to your available Wi-Fi networks and find your esp32.

53
00:04:01,290 --> 00:04:02,760
And then type your password.

54
00:04:06,250 --> 00:04:06,820
I just left.

55
00:04:06,850 --> 00:04:08,770
Mine is password, so I'll connect.

56
00:04:11,680 --> 00:04:16,510
And now we can see that the event handler captured the event for a connected event.

57
00:04:21,120 --> 00:04:22,710
Which is the event right here.

58
00:04:26,040 --> 00:04:31,860
And also we can see that our Dhcp server setup has assigned an IP to our station in the same network.

59
00:04:34,140 --> 00:04:35,040
All right, great.

60
00:04:35,250 --> 00:04:36,450
So that's it for now.

61
00:04:36,450 --> 00:04:39,180
And we'll continue to expand Wi-Fi throughout the course.

62
00:04:39,180 --> 00:04:42,390
And in the next section, we'll talk about the Http server.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: HTTP Server

1
00:00:06,990 --> 00:00:11,760
In this section, we'll take a look at the Http server implementation, which is a key component of

2
00:00:11,760 --> 00:00:14,040
the wireless local area network application.

3
00:00:14,040 --> 00:00:16,260
And of course, it supports the web page.

4
00:00:17,400 --> 00:00:19,770
So let's get into the implementation overview.

5
00:00:20,010 --> 00:00:25,830
First of all, the Web server supports the web page files, which includes the HTML document, the CSS

6
00:00:25,830 --> 00:00:28,080
file and the JavaScript file.

7
00:00:28,260 --> 00:00:35,040
And we'll use this web page to interact with the ESP 32 and that includes support for OTA or over-the-air

8
00:00:35,070 --> 00:00:39,480
firmware updates and also displaying temperature and humidity sensor readings.

9
00:00:39,480 --> 00:00:44,760
And the web server will also be able to respond to connection and disconnection buttons, for example,

10
00:00:44,790 --> 00:00:50,490
by entering the Ssid and password into text fields for the access point or router where you want to

11
00:00:50,490 --> 00:00:54,390
connect and by clicking connect, the connection attempt will be made.

12
00:00:54,390 --> 00:00:58,960
And in the case that the ESP 32 is already connected to an access point.

13
00:00:58,980 --> 00:01:04,890
Clicking disconnect will trigger an action on the web server side that forces the ESP 32 to disconnect.

14
00:01:05,680 --> 00:01:11,020
Also, the web server will be able to handle sending connection information to the web page, such as

15
00:01:11,020 --> 00:01:19,720
the ID of the access point that the ESP 32 is connected to and the IP and Gateway and Netmask assigned

16
00:01:19,720 --> 00:01:20,410
to the ESP.

17
00:01:20,920 --> 00:01:27,310
And later in the course we'll display the ID of the ESP 32 itself on the web page.

18
00:01:27,400 --> 00:01:32,920
So once you learn how to do all of these tasks, you'll know how to send data to the web page and receive

19
00:01:32,950 --> 00:01:38,500
data from the page as well, which enables you to write your own custom applications.

20
00:01:39,160 --> 00:01:41,350
Now let's talk about the Web page files.

21
00:01:41,470 --> 00:01:46,900
The resource files in this section includes an HTML file that already includes the markup for the OTA

22
00:01:46,930 --> 00:01:47,620
update.

23
00:01:47,650 --> 00:01:50,310
Basically, it is just a couple of buttons at this point.

24
00:01:50,320 --> 00:01:56,440
However, we'll expand upon this file throughout the course and the app dot CSS file is the style sheet

25
00:01:56,440 --> 00:02:02,140
for the index HTML document and that will also continue to expand as we go along in the course.

26
00:02:02,140 --> 00:02:05,230
And it already has the styling for the template that I've provided.

27
00:02:05,440 --> 00:02:11,500
And also the App.js file is the JavaScript file which already includes the OTA functions.

28
00:02:11,770 --> 00:02:15,490
And we'll also expand this by adding functions throughout the course.

29
00:02:15,790 --> 00:02:22,240
And the Favicon.ico file is the icon that gets displayed in the address bar of the browser.

30
00:02:22,660 --> 00:02:29,290
And lastly, the jQuery file is the JavaScript library that enables the JavaScript functionality that

31
00:02:29,290 --> 00:02:30,310
we'll be using.

32
00:02:31,660 --> 00:02:35,910
Now let's briefly talk about the Http server components of the ESP IDF.

33
00:02:37,070 --> 00:02:39,630
So here's the suggested reading for this section.

34
00:02:39,710 --> 00:02:43,760
Be sure to check out the Http server and API reference link here.

35
00:02:44,060 --> 00:02:48,560
The overview here covers a lot of what we're actually going to be doing in the course and the functions

36
00:02:48,560 --> 00:02:49,250
used.

37
00:02:49,640 --> 00:02:55,160
And if you follow the second link, it just takes you to an example further down on the same page.

38
00:02:55,190 --> 00:02:59,870
You'll find that our implementation follows a very similar structure to this example shown here.

39
00:03:00,660 --> 00:03:04,650
So let's take a look at some of the steps we'll have to take to get the Web server up and running.

40
00:03:04,890 --> 00:03:07,950
One of the first steps we'll take is embedding binary data.

41
00:03:07,980 --> 00:03:10,920
The HTML, CSS and JavaScript files.

42
00:03:10,950 --> 00:03:12,720
So follow the link for detail.

43
00:03:12,900 --> 00:03:17,760
Basically, we're going to edit the Cmakelist file and list our web page files there.

44
00:03:17,880 --> 00:03:23,730
Then in the Http server file, we're going to add the file's contents to the read only section in the

45
00:03:23,730 --> 00:03:25,290
flash as shown here.

46
00:03:25,440 --> 00:03:31,230
We'll then include our basic Http server, start and stop functions and wrap those functions so that

47
00:03:31,230 --> 00:03:35,280
we can use them in the application similar to how it's done in the example here.

48
00:03:35,940 --> 00:03:41,820
Next, we'll then create the default Http server configuration where some of these structure members

49
00:03:41,820 --> 00:03:47,520
will be initialized using the default config function, but we'll adjust some of these members to our

50
00:03:47,520 --> 00:03:48,150
needs.

51
00:03:48,180 --> 00:03:51,390
Then we'll call the Http start function.

52
00:03:51,420 --> 00:03:57,090
Things will turn out looking similar to the examples shown and throughout the course we'll create Uri

53
00:03:57,120 --> 00:04:01,230
handlers and this is a Uri Handler structure here.

54
00:04:01,470 --> 00:04:08,700
And in the first lesson, we'll just register Uri handlers for the resource files and we'll create this

55
00:04:08,730 --> 00:04:10,830
in a very similar way as shown here.

56
00:04:11,490 --> 00:04:18,330
And the last thing that I want to mention is that we'll also create a task called Http server monitor,

57
00:04:18,360 --> 00:04:22,680
which can send and receive messages to respond to certain events.

58
00:04:22,770 --> 00:04:25,680
It's similar to what we have in the Wi-Fi application.

59
00:04:25,770 --> 00:04:31,650
For now, we'll handle inter task communication between the Wi-Fi application and the web server in

60
00:04:31,650 --> 00:04:34,260
this manner by using the message queues.

61
00:04:34,290 --> 00:04:37,230
If any of this seems confusing, don't worry.

62
00:04:37,230 --> 00:04:40,300
Once we get to coding, it should start to make more sense.

63
00:04:40,320 --> 00:04:44,820
I just like providing a quick overview so that you have some sort of reference before we get into using

64
00:04:44,820 --> 00:04:46,440
the Http server API.

65
00:04:47,800 --> 00:04:49,990
All right, so let's get to coding in the next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,020 --> 00:00:07,290
Okay.

2
00:00:07,290 --> 00:00:10,110
So the first thing we'll do is create a new folder under Main.

3
00:00:14,590 --> 00:00:15,970
And call it Web page.

4
00:00:20,460 --> 00:00:20,790
Okay.

5
00:00:20,790 --> 00:00:23,010
And here we'll include our Web page files.

6
00:00:23,010 --> 00:00:27,720
So we have the Web page files handy that were provided from the resources for this section so that we

7
00:00:27,720 --> 00:00:29,400
can include them in this folder.

8
00:00:29,400 --> 00:00:30,600
And I have mine right here.

9
00:00:30,600 --> 00:00:34,890
So I'll just take all of these files and then copy them to the web page folder like so.

10
00:00:36,410 --> 00:00:38,930
And here, just choose copy files.

11
00:00:39,830 --> 00:00:40,460
Okay.

12
00:00:41,740 --> 00:00:45,350
So now let's open the files that we're going to develop further throughout the course.

13
00:00:45,370 --> 00:00:52,660
First, go to apks and right click and go to open with and then choose other.

14
00:00:54,560 --> 00:00:57,590
And I'll just choose the CC plus plus editor.

15
00:00:57,950 --> 00:01:02,450
But if you happen to have something better like VS code, then by all means please use that instead.

16
00:01:04,150 --> 00:01:04,690
Okay.

17
00:01:05,380 --> 00:01:10,540
And then now let's choose the App.js file and bring up the internal editors again.

18
00:01:19,120 --> 00:01:21,880
And again, I'll choose c, c plus plus editor.

19
00:01:24,270 --> 00:01:27,900
And then open up the index.html document in the same manner.

20
00:01:36,740 --> 00:01:38,690
And I'll choose the same editor.

21
00:01:42,500 --> 00:01:45,650
And this is the template that we'll expand upon throughout the course.

22
00:01:46,430 --> 00:01:53,720
Here we have our app.css file specified as the stylesheet and our app.js file here, and we have a jQuery

23
00:01:53,720 --> 00:01:56,000
here as our JavaScript library.

24
00:01:56,270 --> 00:01:58,640
And if we go over to App.js.

25
00:01:59,340 --> 00:02:04,560
We already have the functions there which will handle the firmware update on the web page side.

26
00:02:04,800 --> 00:02:10,500
So feel free to look at this and get a basic understanding of it and we'll add quite a bit of code to

27
00:02:10,500 --> 00:02:11,190
it later.

28
00:02:11,580 --> 00:02:17,790
Also, there is a very basic stylesheet here and there's some button styling already here as well as

29
00:02:17,790 --> 00:02:19,410
some color and fonts as well.

30
00:02:19,440 --> 00:02:22,260
You can always customize this so that it suits your needs.

31
00:02:23,600 --> 00:02:25,940
All right, So let's head over to CMake list file.

32
00:02:27,390 --> 00:02:31,110
And here we're going to say embed files.

33
00:02:32,190 --> 00:02:39,840
Because we need to embed the web page files so we'll say the path web page slash app dot CSS.

34
00:02:41,020 --> 00:02:43,870
And then web page slash app.js.

35
00:02:45,030 --> 00:02:48,450
And web page slash favicon.ico.

36
00:02:50,900 --> 00:02:52,280
And then web page.

37
00:02:52,910 --> 00:02:55,040
index.HTML.

38
00:02:55,070 --> 00:02:57,260
And then lastly, web page slash.

39
00:02:58,200 --> 00:03:00,180
And then let's copy the jQuery.

40
00:03:02,650 --> 00:03:03,910
And paste it here.

41
00:03:04,270 --> 00:03:05,830
And then we can save it.

42
00:03:07,360 --> 00:03:10,930
Okay, so now let's head over to the main folder and then a new source file.

43
00:03:15,470 --> 00:03:17,900
And call it Http server dot c.

44
00:03:24,990 --> 00:03:25,620
All right.

45
00:03:27,150 --> 00:03:28,950
And now create a new header file.

46
00:03:32,550 --> 00:03:34,230
And call it Http server.

47
00:03:39,930 --> 00:03:45,390
Okay, So first, let's head back over to CMake lists and add the Http server source file.

48
00:03:47,850 --> 00:03:48,840
And save it.

49
00:03:51,410 --> 00:03:53,180
So now let's go to tasks common.

50
00:03:55,080 --> 00:03:59,820
And here we're going to define the Http server task info.

51
00:04:01,700 --> 00:04:04,730
So now let's define the Http server.

52
00:04:06,220 --> 00:04:07,810
Task stack size.

53
00:04:09,990 --> 00:04:12,480
As 8192 bytes.

54
00:04:15,920 --> 00:04:17,450
And then to find the.

55
00:04:18,880 --> 00:04:21,130
Http server task priority.

56
00:04:24,760 --> 00:04:26,500
And we'll define it As for.

57
00:04:28,170 --> 00:04:32,490
Which is just one priority level under the WiFi application task.

58
00:04:33,860 --> 00:04:34,400
All right.

59
00:04:34,400 --> 00:04:38,960
And here we can define the Http server task.

60
00:04:39,970 --> 00:04:40,930
Core ID.

61
00:04:42,550 --> 00:04:44,230
And we'll make it zero as well.

62
00:04:45,190 --> 00:04:50,680
So now here we can define the http server monitor task info.

63
00:04:55,870 --> 00:04:57,640
And first, we'll define the.

64
00:04:58,750 --> 00:05:00,610
Http server monitor.

65
00:05:02,850 --> 00:05:04,080
Stack size.

66
00:05:05,430 --> 00:05:07,620
As 4096 bytes.

67
00:05:09,020 --> 00:05:13,370
And then for the Http server monitor.

68
00:05:16,660 --> 00:05:17,500
Priority.

69
00:05:20,470 --> 00:05:21,490
We'll say three.

70
00:05:23,170 --> 00:05:24,730
And then let's do the.

71
00:05:26,110 --> 00:05:28,270
Http server monitor core ID.

72
00:05:32,550 --> 00:05:34,050
And this we can leave it zero.

73
00:05:35,460 --> 00:05:35,730
Okay.

74
00:05:35,730 --> 00:05:37,740
So that's takes care of our task info.

75
00:05:38,100 --> 00:05:46,110
So now let's go over to the header file and here we'll create messages for the Http monitor.

76
00:05:52,350 --> 00:05:54,810
And let's typedef enum.

77
00:05:56,010 --> 00:05:57,960
Http server message.

78
00:05:59,460 --> 00:06:04,290
And the first one will be http message wi fi connect init.

79
00:06:06,670 --> 00:06:08,950
And we'll explicitly set it to zero.

80
00:06:10,010 --> 00:06:10,340
Okay.

81
00:06:10,340 --> 00:06:14,180
And then the http message wi fi connect success.

82
00:06:17,600 --> 00:06:22,190
And then we'll also have Http message Wi-Fi connect fail.

83
00:06:26,130 --> 00:06:31,320
And then also Http message OTA update successful.

84
00:06:35,850 --> 00:06:39,930
And then Http message OTA update failed.

85
00:06:44,480 --> 00:06:49,340
And also Http message to update initialized.

86
00:06:54,320 --> 00:06:58,790
All right, so let's name it as Http server message.

87
00:07:00,050 --> 00:07:02,380
Underscore E for enum.

88
00:07:02,390 --> 00:07:06,830
And so these are the messages that the Http server monitor will handle for now.

89
00:07:06,860 --> 00:07:09,380
The monitor really doesn't do anything complex.

90
00:07:09,710 --> 00:07:15,260
I just had the idea to include it, to react to events and update global variables within the monitor

91
00:07:15,290 --> 00:07:21,680
only so that it's easier to track what's going on in the Http server as you'll see later, and you can

92
00:07:21,680 --> 00:07:23,990
easily modify this as you wish.

93
00:07:24,080 --> 00:07:28,670
Okay, so now let's create a structure for the message queue.

94
00:07:36,030 --> 00:07:38,940
And here we'll say typedef struct.

95
00:07:41,510 --> 00:07:44,840
Antagonize http server message.

96
00:07:49,030 --> 00:07:51,640
And here we'll just include the enum.

97
00:07:54,680 --> 00:07:56,300
And call it message ID.

98
00:07:59,680 --> 00:08:02,920
Then let's call this http server message.

99
00:08:02,920 --> 00:08:03,910
Underscore T.

100
00:08:09,850 --> 00:08:12,250
And don't forget the semicolon here.

101
00:08:13,010 --> 00:08:18,410
And similar to the Wi-Fi app messages, this is something that you can easily expand upon based on your

102
00:08:18,440 --> 00:08:18,860
needs.

103
00:08:18,890 --> 00:08:24,590
Okay, so now let's come down here and create a prototype for a function that sends a message to the

104
00:08:24,590 --> 00:08:25,070
queue.

105
00:08:29,050 --> 00:08:31,690
And so the first parameter is message ID.

106
00:08:33,620 --> 00:08:36,740
From the Http server message enum.

107
00:08:41,540 --> 00:08:44,000
And the return is true.

108
00:08:44,690 --> 00:08:47,420
If an item was successfully sent to the queue.

109
00:08:50,420 --> 00:08:52,100
Otherwise p d false.

110
00:08:55,900 --> 00:09:01,600
And I'll leave a note here for you to expand the parameter list based on your requirements.

111
00:09:07,800 --> 00:09:12,930
E.g. how you've expanded the Http server message structure.

112
00:09:22,230 --> 00:09:25,560
Okay, so just expand the struct and function however you like.

113
00:09:28,350 --> 00:09:31,520
Now, let's say basetype underscore t.

114
00:09:32,370 --> 00:09:34,290
Http server monitor.

115
00:09:36,050 --> 00:09:37,280
Send message.

116
00:09:40,110 --> 00:09:44,970
And then let's just grab the enum and drop it here.

117
00:09:48,390 --> 00:09:52,860
And we'll create another prototype that starts the Http server.

118
00:09:57,580 --> 00:10:00,850
And say void http server start.

119
00:10:02,140 --> 00:10:03,190
And it's void.

120
00:10:05,170 --> 00:10:05,500
All right.

121
00:10:05,500 --> 00:10:09,130
So now create another prototype that stops the Http server.

122
00:10:12,060 --> 00:10:15,240
And its void http server stop.

123
00:10:16,620 --> 00:10:17,130
Void.

124
00:10:19,170 --> 00:10:20,760
So now that's it for now.

125
00:10:20,760 --> 00:10:25,170
And in the next section we'll code the http server dot c file.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,220 --> 00:00:09,230
Okay, so let's go over to the C file.

2
00:00:10,520 --> 00:00:12,010
And we're going to include.

3
00:00:12,910 --> 00:00:15,160
ESP http servers.

4
00:00:18,200 --> 00:00:20,780
And that's for Http server component.

5
00:00:22,180 --> 00:00:25,120
And we can also include esp log.

6
00:00:28,190 --> 00:00:31,100
And we'll also include here http server.

7
00:00:35,410 --> 00:00:36,490
And include.

8
00:00:38,030 --> 00:00:39,740
Tasks common.

9
00:00:42,250 --> 00:00:45,000
And also include Wi-Fi apps.

10
00:00:49,150 --> 00:00:53,860
And now let's add a tag used for ESP serial console messages.

11
00:00:57,760 --> 00:01:01,420
And say static const char tag.

12
00:01:04,020 --> 00:01:06,810
And call it Http server.

13
00:01:10,300 --> 00:01:13,780
Okay, now we'll create an Http server task handle.

14
00:01:19,170 --> 00:01:23,280
And it'll be static httpd handle underscore t.

15
00:01:26,780 --> 00:01:29,750
And call it http server handle.

16
00:01:30,650 --> 00:01:32,030
And set it to null.

17
00:01:33,480 --> 00:01:38,670
And this is the Http server instance handle that we'll need to use when we call various functions from

18
00:01:38,670 --> 00:01:42,620
the API such as Http start and stop.

19
00:01:42,630 --> 00:01:49,050
And when we register our Uri handlers using the Http register Uri handler function.

20
00:01:49,680 --> 00:01:52,800
Okay, so now let's take care of the embedded files.

21
00:01:54,180 --> 00:01:55,980
Which includes jQuery.

22
00:01:58,770 --> 00:02:00,420
index.HTML.

23
00:02:01,850 --> 00:02:05,240
App.css and App.js.

24
00:02:05,240 --> 00:02:07,970
And the Favicon.ico files.

25
00:02:11,880 --> 00:02:12,120
Okay.

26
00:02:12,120 --> 00:02:15,690
So now we need to extern const uint8 type.

27
00:02:17,580 --> 00:02:20,040
And notice how the files need to be typed here.

28
00:02:20,040 --> 00:02:22,080
So we'll say jQuery.

29
00:02:23,510 --> 00:02:26,210
Underscore and just follow me here.

30
00:02:31,990 --> 00:02:33,160
For the start.

31
00:02:33,910 --> 00:02:35,320
And then use.

32
00:02:36,180 --> 00:02:38,790
ESM and then quotes.

33
00:02:39,620 --> 00:02:41,570
And just follow me the rest of the way.

34
00:02:46,260 --> 00:02:48,270
And just paste the rest of the name here.

35
00:02:49,710 --> 00:02:51,400
And that's how we handle the start.

36
00:02:51,420 --> 00:02:53,160
So now just copy it.

37
00:02:54,390 --> 00:02:57,750
And then paste it here and change this to end.

38
00:03:00,340 --> 00:03:01,750
And the end here.

39
00:03:05,420 --> 00:03:05,900
Next.

40
00:03:05,900 --> 00:03:08,570
Let's just do the same for index.html.

41
00:03:15,540 --> 00:03:16,920
And that's for the start.

42
00:03:20,140 --> 00:03:21,880
And then do the same like before.

43
00:03:30,510 --> 00:03:33,630
So now just copy that and paste it.

44
00:03:35,140 --> 00:03:36,400
And let's do the end.

45
00:03:41,770 --> 00:03:42,070
And then.

46
00:03:42,070 --> 00:03:43,000
Now let's do the app.

47
00:03:43,570 --> 00:03:44,560
Start here.

48
00:04:01,010 --> 00:04:02,780
And then they'll do the end portion.

49
00:04:11,020 --> 00:04:13,930
Okay, so now let's do the start for App.js.

50
00:04:28,750 --> 00:04:28,990
Then.

51
00:04:28,990 --> 00:04:31,060
Now let's do the end for the App.js.

52
00:04:39,950 --> 00:04:41,420
And then do the last one.

53
00:04:42,230 --> 00:04:44,210
For favicon.ico start.

54
00:05:00,340 --> 00:05:00,820
Okay.

55
00:05:00,820 --> 00:05:03,160
And then we'll also do favicon.ico and.

56
00:05:11,740 --> 00:05:12,160
Okay.

57
00:05:12,160 --> 00:05:13,060
That looks good.

58
00:05:14,300 --> 00:05:16,400
So now we can head over to the header file.

59
00:05:19,000 --> 00:05:21,940
And then just grab our start and stop prototypes for now.

60
00:05:33,460 --> 00:05:36,430
And then now first we can go to Http server start.

61
00:05:39,040 --> 00:05:46,780
And let's grab the Http server handle and say if http server handle is null.

62
00:05:49,110 --> 00:05:56,610
Then we'll say http server handle equals the result of http server configure.

63
00:06:00,500 --> 00:06:03,200
And this function will need to create later.

64
00:06:03,680 --> 00:06:07,190
So for now, let's go over to the Http server stop.

65
00:06:07,800 --> 00:06:14,970
And say if Http server handle meaning that the Http server has been initialized already.

66
00:06:16,810 --> 00:06:18,680
Then we'll call Httpd.

67
00:06:18,730 --> 00:06:19,360
Stop.

68
00:06:20,410 --> 00:06:22,270
And insert the handle parameter.

69
00:06:26,490 --> 00:06:28,860
And now esp log information.

70
00:06:31,590 --> 00:06:33,390
Http server stop.

71
00:06:35,960 --> 00:06:38,930
Colon stopping Http server.

72
00:06:43,020 --> 00:06:46,830
And then we can set the Http server handle back to null.

73
00:06:53,530 --> 00:06:53,980
Okay.

74
00:06:53,980 --> 00:06:54,880
That looks good.

75
00:06:55,530 --> 00:07:02,010
Now let's create the Http server, configure function and come here and say sets up the default.

76
00:07:03,310 --> 00:07:05,980
Httpd server configuration.

77
00:07:08,400 --> 00:07:12,390
And returns http server instance handle.

78
00:07:14,090 --> 00:07:15,440
If successful.

79
00:07:16,850 --> 00:07:18,380
Null otherwise.

80
00:07:26,810 --> 00:07:31,550
So we'll say static httpd handle underscore t.

81
00:07:33,640 --> 00:07:37,630
And it's the Http server configure function and it's void.

82
00:07:41,320 --> 00:07:45,280
And now we'll generate the default configuration.

83
00:07:49,960 --> 00:07:56,740
So here we'll need an instance of the handle httpd config type and we'll call it config.

84
00:07:57,830 --> 00:08:01,220
Equals httpd default config function.

85
00:08:05,020 --> 00:08:07,120
And here I'll write to do.

86
00:08:09,440 --> 00:08:13,370
That we should create Http server monitor task.

87
00:08:14,630 --> 00:08:15,950
So we'll do that later.

88
00:08:16,610 --> 00:08:20,180
And also write another to do to create the message queue.

89
00:08:24,400 --> 00:08:29,650
And now we can specify the code that the Http server will run on.

90
00:08:33,710 --> 00:08:37,310
And for that say config dot core ID.

91
00:08:40,510 --> 00:08:43,210
Equals our Http server.

92
00:08:44,200 --> 00:08:45,490
Task core ID.

93
00:08:49,170 --> 00:08:52,230
And next we'll adjust the default priority.

94
00:08:54,120 --> 00:08:58,230
To one less than the Wi-Fi application task.

95
00:09:03,120 --> 00:09:05,790
And do config dot task priority.

96
00:09:13,790 --> 00:09:17,210
Equals Http server task priority.

97
00:09:21,780 --> 00:09:24,300
And now we'll bump up the stack size.

98
00:09:26,420 --> 00:09:30,020
Because the default is 4096 bytes.

99
00:09:31,380 --> 00:09:34,320
So we'll do config dot stack size.

100
00:09:37,600 --> 00:09:41,350
Equals our Http server task stack size.

101
00:09:44,850 --> 00:09:48,330
And next, we'll increase our Uri handlers.

102
00:09:52,390 --> 00:09:55,300
Which is the maximum amount of Uri handlers.

103
00:09:56,070 --> 00:09:59,880
And say config dot max uri handlers.

104
00:10:04,160 --> 00:10:05,960
And 20 should be good enough.

105
00:10:07,620 --> 00:10:08,220
All right.

106
00:10:08,400 --> 00:10:11,430
And now we'll increase the timeout limits.

107
00:10:15,860 --> 00:10:19,550
And do config dot receive wait timeout.

108
00:10:20,320 --> 00:10:21,700
As 10s.

109
00:10:23,600 --> 00:10:29,870
And then next do config dot send wait timeout as 10s as well.

110
00:10:32,140 --> 00:10:32,740
All right.

111
00:10:33,100 --> 00:10:36,160
And now let's log the config information.

112
00:10:42,440 --> 00:10:47,060
And for the message we'll say Http can server configure.

113
00:10:49,460 --> 00:10:51,230
Starting server on port.

114
00:10:53,750 --> 00:10:55,520
And we'll print the port number.

115
00:10:56,700 --> 00:10:59,520
And then we'll say with task priority.

116
00:11:01,480 --> 00:11:03,370
And we'll give the priority here.

117
00:11:07,130 --> 00:11:07,490
All right.

118
00:11:07,490 --> 00:11:10,010
And then we'll give the config server port.

119
00:11:12,650 --> 00:11:15,740
And the config task priority.

120
00:11:18,890 --> 00:11:19,190
Okay.

121
00:11:19,190 --> 00:11:23,000
So we'll see this information on the terminal monitor when the Web server starts.

122
00:11:23,030 --> 00:11:31,130
Next, let's start the Httpd server and we'll say if httpd start.

123
00:11:33,700 --> 00:11:37,240
With the reference to the Http server handle.

124
00:11:42,650 --> 00:11:44,690
In a reference to the config.

125
00:11:47,970 --> 00:11:49,590
And if it returns esp.

126
00:11:49,650 --> 00:11:50,370
Okay.

127
00:11:54,400 --> 00:11:57,490
Then we want to log information.

128
00:12:01,090 --> 00:12:03,790
That the http server configure.

129
00:12:05,440 --> 00:12:08,050
Is now registering the Uri handlers.

130
00:12:13,310 --> 00:12:17,120
And then first we'll say register the jQuery handler.

131
00:12:21,620 --> 00:12:25,280
And here we need the httpd uri struct.

132
00:12:27,590 --> 00:12:30,590
And call it jQuery underscore JS.

133
00:12:34,700 --> 00:12:35,360
And let's set the.

134
00:12:39,260 --> 00:12:42,080
As forward slash in the file name here.

135
00:12:50,500 --> 00:12:53,020
And then next we'll specify the method.

136
00:12:55,170 --> 00:12:57,090
As an Http get.

137
00:12:59,990 --> 00:13:01,820
And now we need to provide a handler.

138
00:13:05,070 --> 00:13:08,670
And give it a function name as Http server.

139
00:13:09,890 --> 00:13:11,390
jQuery handler.

140
00:13:15,310 --> 00:13:17,530
And now let's set this user underscore.

141
00:13:21,470 --> 00:13:22,430
As null.

142
00:13:27,810 --> 00:13:28,890
All right, so that looks good.

143
00:13:28,890 --> 00:13:33,960
So now we can register this Uri Handler using the Httpd register.

144
00:13:33,960 --> 00:13:35,220
Uri Handler.

145
00:13:37,040 --> 00:13:40,550
And then we'll pass the Http server handle.

146
00:13:42,170 --> 00:13:46,130
In a reference to the jQuery underscore JS structure.

147
00:13:49,420 --> 00:13:50,270
Okay, cool.

148
00:13:50,290 --> 00:13:52,420
So now let's copy this one.

149
00:13:55,320 --> 00:13:56,730
And then paste it down.

150
00:13:58,320 --> 00:14:02,430
So we can register the index dot HTML handler.

151
00:14:04,380 --> 00:14:08,760
And now change this name here to index underscore HTML.

152
00:14:10,140 --> 00:14:13,020
And the or is just a forward slash.

153
00:14:15,630 --> 00:14:18,540
And now let's update the handler name like so.

154
00:14:25,140 --> 00:14:27,030
And also copy and paste.

155
00:14:27,870 --> 00:14:33,810
To register the index HTML handler and now just copy and paste.

156
00:14:35,440 --> 00:14:37,060
To the next Uri Handler.

157
00:14:37,770 --> 00:14:40,650
And change the name to ABC's handler.

158
00:14:43,000 --> 00:14:44,500
And then update the name here.

159
00:14:47,540 --> 00:14:48,260
And then update the.

160
00:14:52,210 --> 00:14:54,370
And now we can update the handler function name.

161
00:14:57,240 --> 00:15:01,050
And then register the app underscore CSS handler.

162
00:15:02,410 --> 00:15:04,720
So now let's do the App.js.

163
00:15:07,790 --> 00:15:09,980
And then change it to App.js.

164
00:15:11,230 --> 00:15:13,090
And then update the rest the same way.

165
00:15:27,170 --> 00:15:27,650
Okay, good.

166
00:15:27,650 --> 00:15:30,560
So now let's register the favicon dot ICO.

167
00:15:35,160 --> 00:15:36,750
And then we'll update it like so.

168
00:16:01,210 --> 00:16:03,970
Now we can return the Http server handle.

169
00:16:10,640 --> 00:16:11,210
Okay.

170
00:16:11,820 --> 00:16:13,800
And outside this if block.

171
00:16:16,480 --> 00:16:17,800
We can return Null.

172
00:16:19,080 --> 00:16:19,650
Right here.

173
00:16:19,680 --> 00:16:20,340
Great.

174
00:16:25,070 --> 00:16:27,260
So next, we'll define the Uri handlers.

175
00:16:27,260 --> 00:16:31,430
But I think now is a good time to take a short break and we'll regroup in the next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,270 --> 00:00:10,030
Okay, so let's start by defining the jQuery handler.

2
00:00:14,040 --> 00:00:15,510
And we'll define it here.

3
00:00:19,540 --> 00:00:21,730
And we'll say jQuery.

4
00:00:21,760 --> 00:00:22,720
Get handler.

5
00:00:25,120 --> 00:00:27,550
Is requested when accessing the web page.

6
00:00:30,860 --> 00:00:32,690
In the perimeter rec.

7
00:00:33,960 --> 00:00:38,430
Is the Http request for which the Uri needs to be handled.

8
00:00:43,230 --> 00:00:45,660
And the return is ESP.

9
00:00:45,720 --> 00:00:46,080
Okay.

10
00:00:50,920 --> 00:00:55,030
And this will be static and returns esp error type.

11
00:00:56,680 --> 00:01:02,470
And it's the jQuery handler which takes a pointer to the Httpd request structure.

12
00:01:03,800 --> 00:01:05,210
And call it RCB.

13
00:01:07,730 --> 00:01:12,140
And the Httpd request data structure holds all the information for the request.

14
00:01:13,690 --> 00:01:14,020
Okay.

15
00:01:14,020 --> 00:01:15,850
So here, log a message.

16
00:01:17,500 --> 00:01:18,640
That says.

17
00:01:19,680 --> 00:01:21,570
jQuery requested.

18
00:01:28,030 --> 00:01:32,500
And then the response type using Httpd response.

19
00:01:32,500 --> 00:01:33,640
Set type.

20
00:01:35,590 --> 00:01:37,210
Which takes the request.

21
00:01:38,120 --> 00:01:41,750
And the type is application slash JavaScript.

22
00:01:44,970 --> 00:01:46,980
And if you follow the function definition.

23
00:01:47,780 --> 00:01:53,120
You'll find that there are some commonly used types defined here, but we'll use others in addition

24
00:01:53,120 --> 00:01:54,380
to these as well.

25
00:01:57,270 --> 00:02:04,860
Okay, so next, we'll send the response using Httpd, underscore response, underscore, send and pass

26
00:02:04,860 --> 00:02:05,640
the request.

27
00:02:05,640 --> 00:02:08,220
Then the const char pointer type.

28
00:02:09,110 --> 00:02:11,420
So we can pass the jQuery start.

29
00:02:20,300 --> 00:02:22,700
And then pass the jQuery end.

30
00:02:25,070 --> 00:02:26,420
Minus the start.

31
00:02:32,100 --> 00:02:34,230
And if we follow the function definition.

32
00:02:36,100 --> 00:02:37,180
You'll see that here.

33
00:02:37,180 --> 00:02:40,630
We're just passing the request, the buffer and the buffer length.

34
00:02:46,320 --> 00:02:46,770
Okay.

35
00:02:46,770 --> 00:02:48,690
So then just return ESP.

36
00:02:48,730 --> 00:02:49,380
Okay.

37
00:02:51,660 --> 00:02:54,990
All right, so now let's define the next handler by copying this one.

38
00:02:56,310 --> 00:02:57,870
And pasting it beneath.

39
00:03:00,980 --> 00:03:06,230
And here we'll update the comment by saying since the index.html page.

40
00:03:11,320 --> 00:03:14,590
And then just come down and grab the handler.

41
00:03:17,560 --> 00:03:19,570
So that we can update the function name.

42
00:03:22,930 --> 00:03:26,260
And then just change this to index.html.

43
00:03:29,140 --> 00:03:33,580
And then we'll set the type as text slash HTML.

44
00:03:37,780 --> 00:03:41,920
And then let's copy the start and give it as the buffer.

45
00:03:43,960 --> 00:03:48,820
And the length will take the end to complete the length parameter.

46
00:03:49,480 --> 00:03:50,530
And that's it.

47
00:03:50,740 --> 00:03:52,990
So now let's keep going and copy.

48
00:03:55,800 --> 00:03:57,090
And then paste it again.

49
00:04:00,180 --> 00:04:01,890
And then update the comment.

50
00:04:02,710 --> 00:04:04,780
To say Apks.

51
00:04:08,410 --> 00:04:13,630
And then I'll just fix this here and up here as well.

52
00:04:18,770 --> 00:04:20,510
So we'll get the function name.

53
00:04:26,700 --> 00:04:27,780
And place it here.

54
00:04:30,180 --> 00:04:31,980
And then update the log message.

55
00:04:36,570 --> 00:04:38,640
And then we can grab the CSS start.

56
00:04:44,740 --> 00:04:47,710
And then we can also take care of the end as well right here.

57
00:04:51,630 --> 00:04:55,530
And then also we should remember to update the type as well.

58
00:04:57,010 --> 00:04:59,740
Which is CSS so we can say.

59
00:05:01,460 --> 00:05:04,280
Text forward slash CSS.

60
00:05:06,220 --> 00:05:08,200
Okay, So let's let's keep it moving.

61
00:05:12,840 --> 00:05:14,100
Let's just do the same.

62
00:05:17,770 --> 00:05:20,140
And then here we'll do the App.js.

63
00:05:24,350 --> 00:05:26,600
All right, so now let's just get the function name.

64
00:05:35,090 --> 00:05:36,080
Place it here.

65
00:05:37,400 --> 00:05:39,500
And update the message.

66
00:05:43,620 --> 00:05:44,490
And the type here.

67
00:05:44,490 --> 00:05:45,400
That's fine.

68
00:05:45,420 --> 00:05:47,850
So let's get the app.js start.

69
00:05:52,090 --> 00:05:53,860
And update the send function.

70
00:06:01,980 --> 00:06:03,330
Okay, That looks good.

71
00:06:04,590 --> 00:06:05,040
Okay, let's.

72
00:06:05,040 --> 00:06:06,270
Let's do the last one.

73
00:06:11,880 --> 00:06:14,900
And here we'll say since the ICO.

74
00:06:16,200 --> 00:06:17,040
Icon.

75
00:06:18,030 --> 00:06:20,190
File when accessing the web page.

76
00:06:25,820 --> 00:06:27,560
So let's update the function name.

77
00:06:29,230 --> 00:06:30,130
Copy that.

78
00:06:33,220 --> 00:06:34,150
Place it.

79
00:06:35,860 --> 00:06:37,390
Then log the message.

80
00:06:41,620 --> 00:06:44,470
And the type here that will be image.

81
00:06:45,310 --> 00:06:47,800
Slash x dash icon.

82
00:06:51,300 --> 00:06:53,280
So now get the favicon start.

83
00:06:56,500 --> 00:06:58,420
And we can update the response.

84
00:07:08,280 --> 00:07:09,420
Okay, that's it.

85
00:07:09,510 --> 00:07:13,290
So at this point we can call the Http server start function.

86
00:07:13,390 --> 00:07:15,900
We can do that by heading over to the Wi-Fi APK.

87
00:07:18,020 --> 00:07:19,640
Uncomment the function call.

88
00:07:23,020 --> 00:07:24,100
And that looks good.

89
00:07:24,700 --> 00:07:26,320
So build the project.

90
00:07:34,460 --> 00:07:35,990
And let's just give it a minute.

91
00:07:55,140 --> 00:07:55,530
Okay, then.

92
00:07:55,530 --> 00:07:56,550
Now let's flesh.

93
00:08:08,080 --> 00:08:10,330
Okay, then let's open a serial monitor here.

94
00:08:17,880 --> 00:08:20,130
And we can see that the web server has started.

95
00:08:20,870 --> 00:08:23,060
Now we can connect to the ESP.

96
00:08:30,260 --> 00:08:32,030
And now let's open up Google Chrome.

97
00:08:38,420 --> 00:08:45,170
And then navigate to our IP, which is 192.168.0.1 and hit enter.

98
00:08:46,750 --> 00:08:47,200
Great.

99
00:08:47,200 --> 00:08:49,360
The web server responds with a web page.

100
00:08:50,710 --> 00:08:51,310
Great.

101
00:08:51,310 --> 00:08:52,510
Everything looks good.

102
00:08:53,260 --> 00:08:57,050
And on the monitor our handler messages are logged for the HTML.

103
00:08:58,110 --> 00:08:59,130
jQuery.

104
00:08:59,310 --> 00:09:01,680
CSS and JavaScript.

105
00:09:01,860 --> 00:09:04,410
And also the five icon ICO as well.

106
00:09:06,770 --> 00:09:08,120
And this icon.

107
00:09:08,150 --> 00:09:09,590
It shows up right here.

108
00:09:10,690 --> 00:09:16,990
And the select button already has the JavaScript functionality to select the bin file and the update

109
00:09:16,990 --> 00:09:21,970
firmware button also reacts via the JavaScript functions included in the template files.

110
00:09:22,210 --> 00:09:23,920
All right, so that's all for now.

111
00:09:23,920 --> 00:09:26,590
In the next lesson, we'll continue to expand the web server.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,950 --> 00:00:10,820
In this lesson, we'll create the Http server monitor task.

2
00:00:10,850 --> 00:00:17,030
As I mentioned previously, this task simply receives messages from the queue and updates global variables

3
00:00:17,030 --> 00:00:22,220
within the monitor task, which affects certain actions of the web server and the web page.

4
00:00:22,550 --> 00:00:25,040
And there are probably multiple ways to do this.

5
00:00:25,040 --> 00:00:30,500
I just thought it might be useful to update the global variables in one place and also use this as an

6
00:00:30,500 --> 00:00:35,380
opportunity to demonstrate just one way of accomplishing inter task communication between the Wi-Fi

7
00:00:35,390 --> 00:00:37,670
application and the web server.

8
00:00:38,890 --> 00:00:43,450
All right, so now let's start by creating the Http server.

9
00:00:44,150 --> 00:00:45,800
Monitor task handle.

10
00:00:47,850 --> 00:00:50,370
And that will be a static task handle type.

11
00:00:51,870 --> 00:00:55,380
And call it task http server monitor.

12
00:00:57,610 --> 00:00:59,110
And set that to null.

13
00:01:02,850 --> 00:01:05,160
Next, we'll create the handle.

14
00:01:06,710 --> 00:01:09,470
Used to manipulate the main queue of events.

15
00:01:14,000 --> 00:01:16,370
And it's a static cue handle type.

16
00:01:17,880 --> 00:01:22,470
And call it Http server monitor handle.

17
00:01:27,670 --> 00:01:29,980
And now let's come down to our to dos.

18
00:01:33,790 --> 00:01:40,420
We have our to dos right here and let's create the Http server monitor task.

19
00:01:41,600 --> 00:01:43,580
And also create the message queue.

20
00:01:44,840 --> 00:01:48,380
Okay, so here we can use ECS task, create pin to core.

21
00:01:52,930 --> 00:01:56,770
And we'll call the function http server monitor.

22
00:02:00,640 --> 00:02:02,260
And the tag can be the same.

23
00:02:08,630 --> 00:02:12,260
And the stack size will be http server monitor.

24
00:02:13,830 --> 00:02:15,060
Stack size.

25
00:02:16,090 --> 00:02:18,430
And PV parameters will be null.

26
00:02:19,310 --> 00:02:22,100
And the priority will be Http server.

27
00:02:22,920 --> 00:02:24,360
Monitor priority.

28
00:02:27,770 --> 00:02:32,690
And our test candle is a reference to the task http server monitor.

29
00:02:37,090 --> 00:02:40,560
And now the core ID is Http server monitor.

30
00:02:40,570 --> 00:02:41,350
Core ID.

31
00:02:46,920 --> 00:02:47,230
Okay.

32
00:02:47,230 --> 00:02:47,820
It looks good.

33
00:02:47,820 --> 00:02:52,230
So later we'll define the Http server monitor task here.

34
00:02:52,380 --> 00:02:52,800
Okay.

35
00:02:52,800 --> 00:02:58,650
Now let's create the message and it will be http server monitor handle.

36
00:03:02,260 --> 00:03:05,050
Equals x cube create.

37
00:03:06,760 --> 00:03:10,180
And it's three here and the size of.

38
00:03:11,660 --> 00:03:14,960
Http server kube message types.

39
00:03:21,510 --> 00:03:21,930
All right.

40
00:03:21,930 --> 00:03:25,710
So next, let's define the Http server monitor task.

41
00:03:25,710 --> 00:03:27,090
So we'll head up here.

42
00:03:30,810 --> 00:03:32,370
And let's make a comment.

43
00:03:34,450 --> 00:03:38,490
That says Http server monitor task.

44
00:03:39,210 --> 00:03:42,470
Used to track events of the Http server.

45
00:03:46,120 --> 00:03:48,130
And the parameter is a pointer.

46
00:03:48,130 --> 00:03:49,360
Variable parameter.

47
00:03:49,640 --> 00:03:51,100
PV parameter.

48
00:03:56,190 --> 00:03:58,620
Which can be passed to the task.

49
00:04:01,380 --> 00:04:03,180
And this is a static void.

50
00:04:04,500 --> 00:04:06,390
Http server monitor.

51
00:04:07,050 --> 00:04:09,450
And that's a void pointer parameter.

52
00:04:12,300 --> 00:04:15,600
And here first we need an instance of the cube message handle.

53
00:04:15,600 --> 00:04:19,530
So http server monitor message type.

54
00:04:21,770 --> 00:04:24,050
And call it message.

55
00:04:25,870 --> 00:04:27,850
And next, we'll create our endless loop.

56
00:04:32,850 --> 00:04:35,580
And then say if X receive.

57
00:04:40,590 --> 00:04:42,480
And let's include our handle here.

58
00:04:48,200 --> 00:04:50,030
And the reference to the message.

59
00:04:50,030 --> 00:04:51,630
Then Port Max DeLay.

60
00:04:59,210 --> 00:05:00,620
Then say switch.

61
00:05:02,780 --> 00:05:04,700
Message Dot message ID.

62
00:05:05,950 --> 00:05:07,600
And then let's open a case.

63
00:05:09,940 --> 00:05:11,980
And we want to use our messages here.

64
00:05:11,980 --> 00:05:15,310
So let's come here and grab the first one.

65
00:05:17,270 --> 00:05:18,800
And then let's drop it right here.

66
00:05:20,110 --> 00:05:22,630
And then let's log a message for this message.

67
00:05:30,450 --> 00:05:31,590
And then we can break.

68
00:05:33,450 --> 00:05:35,580
All right, So let me just fix this indentation.

69
00:05:37,060 --> 00:05:38,320
And then Copy that.

70
00:05:39,950 --> 00:05:41,690
So we can paste it down.

71
00:05:42,710 --> 00:05:44,720
Then let's grab the next message.

72
00:05:46,260 --> 00:05:48,060
And then update this case.

73
00:05:49,800 --> 00:05:52,170
And we'll just do the same procedure for the next.

74
00:05:58,040 --> 00:05:59,240
Copy the message.

75
00:06:00,450 --> 00:06:01,740
And update the case.

76
00:06:03,740 --> 00:06:05,120
And let's keep it going.

77
00:06:10,190 --> 00:06:11,420
For this message.

78
00:06:17,740 --> 00:06:18,130
Okay.

79
00:06:18,130 --> 00:06:19,330
And on to the next.

80
00:06:24,550 --> 00:06:25,780
Get the message.

81
00:06:27,780 --> 00:06:28,920
Update the case.

82
00:06:31,480 --> 00:06:32,950
And one more time.

83
00:06:37,360 --> 00:06:38,530
Grab the message.

84
00:06:39,810 --> 00:06:41,460
And update this case.

85
00:06:44,270 --> 00:06:48,770
Okay, so now let's just leave a default break here.

86
00:06:53,110 --> 00:06:54,100
Okay, great.

87
00:06:54,100 --> 00:07:01,000
So we'll want to be able to stop the Http server monitor if the Http server is stopped as well.

88
00:07:01,000 --> 00:07:02,650
So let's grab the handle.

89
00:07:04,200 --> 00:07:08,010
And then let's come down to the Http server stop function.

90
00:07:10,950 --> 00:07:16,590
And then we'll say if task http server monitor.

91
00:07:18,040 --> 00:07:20,110
Then we will task delete.

92
00:07:24,980 --> 00:07:26,960
And insert that same handle here.

93
00:07:27,770 --> 00:07:28,260
Okay.

94
00:07:28,280 --> 00:07:29,690
Now log a message.

95
00:07:33,740 --> 00:07:36,620
That says Http server stop.

96
00:07:38,820 --> 00:07:42,690
Stopping Http server monitor.

97
00:07:46,610 --> 00:07:49,610
All right, Now let's set the handle to null.

98
00:07:54,230 --> 00:07:54,540
Okay.

99
00:07:54,540 --> 00:07:55,100
It looks good.

100
00:07:55,100 --> 00:07:56,900
So that completes our stop function.

101
00:07:57,110 --> 00:07:59,210
Now let's head over to the header file.

102
00:08:01,090 --> 00:08:03,610
So we can copy the sin message prototype.

103
00:08:09,240 --> 00:08:10,950
And we could define it right here.

104
00:08:12,680 --> 00:08:16,940
So first, create an instance of the Http server message type.

105
00:08:25,430 --> 00:08:30,770
Then we want the message ID set to the message ID passed to the function.

106
00:08:34,030 --> 00:08:37,780
And then we'll return the result of X to send.

107
00:08:42,690 --> 00:08:44,100
In past the handle.

108
00:08:50,080 --> 00:08:53,380
And the reference to the message and Port Max DeLay.

109
00:08:59,720 --> 00:09:00,220
Okay.

110
00:09:00,230 --> 00:09:00,860
All looks good.

111
00:09:00,860 --> 00:09:02,090
So now we can build.

112
00:09:17,210 --> 00:09:17,690
Okay.

113
00:09:17,690 --> 00:09:18,680
And we have no errors.

114
00:09:18,680 --> 00:09:20,810
So we're ready for firmware updates.

115
00:09:20,810 --> 00:09:24,470
So we'll talk about that in the next section and I'll see you then.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: OTA Firmware Update


1
00:00:06,810 --> 00:00:11,080
In this section, we'll take a look at the over-the-air firmware update implementation.

2
00:00:11,100 --> 00:00:16,590
This firmware update will be implemented over the wireless local area network, and we'll simply upload

3
00:00:16,590 --> 00:00:19,920
the binary file to the ISP using the web page.

4
00:00:20,930 --> 00:00:26,910
So before we go deeper into details, let's talk about OTA updates in general using the IDF.

5
00:00:26,930 --> 00:00:31,860
So OTA updates allow a device to update itself based on data received.

6
00:00:31,880 --> 00:00:33,830
For example, over Wi-Fi.

7
00:00:33,830 --> 00:00:39,680
While the normal firmware is running and enabling firmware updates requires configuring a partition

8
00:00:39,680 --> 00:00:48,560
table with at least two application slots called OTA zero and OTA one, as well as an OTA data partition

9
00:00:48,560 --> 00:00:50,900
and the OTA operation functions.

10
00:00:50,900 --> 00:00:57,650
Write a new application firmware image to whichever OTA application slot is currently not selected for

11
00:00:57,650 --> 00:00:58,370
booting.

12
00:00:58,400 --> 00:01:05,510
So once the image is verified, the OTA data partition is updated to specify that this image should

13
00:01:05,510 --> 00:01:06,890
be used for the next boot.

14
00:01:07,920 --> 00:01:13,440
And further to the partition table, the flash of the ESP can contain multiple applications in different

15
00:01:13,440 --> 00:01:14,160
kinds of data.

16
00:01:14,160 --> 00:01:18,860
For example, calibration data, file systems, parameter storage, et cetera.

17
00:01:18,870 --> 00:01:25,680
And for this purpose, a partition table is flashed to hex 8000 in flash memory, and each entry of

18
00:01:25,680 --> 00:01:31,260
the partition table has a label, a type subtype, and an offset in the flash where the partition is

19
00:01:31,260 --> 00:01:31,950
loaded.

20
00:01:32,190 --> 00:01:39,480
And also the simplest way to use the partition table is to open the project configuration or SDK config

21
00:01:39,480 --> 00:01:45,510
in Eclipse and choose factory app to OTA definitions as we've already done in the project configuration

22
00:01:45,510 --> 00:01:46,230
section.

23
00:01:47,410 --> 00:01:50,150
And here is what a partition table looks like.

24
00:01:50,170 --> 00:01:54,720
Here we have names, types, subtypes, offsets and sizes.

25
00:01:54,730 --> 00:02:00,070
And in this table, which is the same as the one we are currently using, we have three applications.

26
00:02:00,070 --> 00:02:07,420
We have the factory application at offset X 10,000 and the next two OTA applications are apps with OTA

27
00:02:07,420 --> 00:02:10,060
zero and OTA one subtypes.

28
00:02:10,800 --> 00:02:16,500
And there is also a new OTA data slot which holds the data for OTA updates.

29
00:02:16,530 --> 00:02:22,530
The bootloader will check this OTA data slot to know which app to execute, so if it is empty, the

30
00:02:22,530 --> 00:02:24,570
factory application will be executed.

31
00:02:24,600 --> 00:02:28,380
And also you can customize the partition table to suit your needs.

32
00:02:28,410 --> 00:02:33,960
For example, if your application takes up more space, you can adjust the size and remove the factory

33
00:02:33,960 --> 00:02:39,420
application and just use only OTA zero and OTA one partitions if you need.

34
00:02:40,540 --> 00:02:42,670
Okay, now let's talk about our implementation.

35
00:02:43,440 --> 00:02:49,710
The user can start the OTA update by uploading the application binary over the web page, and the firmware

36
00:02:49,710 --> 00:02:54,630
update is then performed on the web server side, and the web page will display the status whether it

37
00:02:54,630 --> 00:02:56,040
was successful or not.

38
00:02:56,220 --> 00:03:02,820
And once the update is complete, the web page is no longer available and the ESP 32 will then restart

39
00:03:03,150 --> 00:03:08,820
and we can then test the firmware update by making just a couple of simple changes like changing the

40
00:03:08,850 --> 00:03:15,870
side of the ESP 32 access point and maybe the web page background just to verify that the new firmware

41
00:03:15,870 --> 00:03:17,130
is indeed running.

42
00:03:17,720 --> 00:03:21,630
So now let's discuss how we can accomplish this using the ESP IDF.

43
00:03:23,200 --> 00:03:28,570
I suggest you browse the expressive documentation to get a better grasp on the OTA update topics here

44
00:03:28,600 --> 00:03:30,790
as well as the API reference.

45
00:03:30,820 --> 00:03:35,590
Check out the process overview and other features available that will not be using in our example.

46
00:03:35,680 --> 00:03:39,130
You can also find more details about the partition table here.

47
00:03:39,310 --> 00:03:45,070
Take a look at the overview as well as other details like creating partition tables if you're interested.

48
00:03:46,570 --> 00:03:51,550
So the steps that we'll have to take on the Web server side starts with receiving the file from the

49
00:03:51,550 --> 00:03:55,860
web page and we'll call httpd request receive for this.

50
00:03:55,870 --> 00:04:02,890
So this API will read Http content data from the http request into the provided buffer.

51
00:04:03,100 --> 00:04:09,100
We'll then have to make multiple calls to this function each time fetching buffer length a number of

52
00:04:09,100 --> 00:04:14,500
bytes while the pointer to the content data is incremented internally by the same number.

53
00:04:15,100 --> 00:04:21,130
Then we'll have to identify where the binary file content actually starts by checking the escape characters,

54
00:04:21,160 --> 00:04:28,060
the slash slash ends that are present when receiving the file from the web page and then call ESP to

55
00:04:28,090 --> 00:04:36,520
begin the ESP OTA Begin function commences the OTA update by writing to the specified partition and

56
00:04:36,520 --> 00:04:43,930
when successful it allocates memory that remains in use until the ESP OTA end function is called.

57
00:04:44,630 --> 00:04:47,370
So next we call ESP to write.

58
00:04:47,390 --> 00:04:47,990
To write.

59
00:04:47,990 --> 00:04:51,140
The first chunk of data that we've received from the web page.

60
00:04:51,170 --> 00:04:57,500
The write function writes data to the specified partition that can be called multiple times as data

61
00:04:57,500 --> 00:05:00,790
is received during the OTA operation.

62
00:05:00,800 --> 00:05:02,870
Which brings us to the next point.

63
00:05:03,140 --> 00:05:11,450
We'll continue receiving the rest of the file by calling Httpd request, receive and esp OTA write until

64
00:05:11,450 --> 00:05:13,460
all of the content is received.

65
00:05:13,490 --> 00:05:20,480
Then we'll finish the OTA update and validate the application image by calling esp OTA end.

66
00:05:20,570 --> 00:05:27,500
So here it's mentioned that the handle associated with the OTA update is no longer valid and that the

67
00:05:27,500 --> 00:05:31,400
memory associated with it is freed regardless of the result.

68
00:05:31,580 --> 00:05:38,600
And next we'll need to configure the OTA data from the partition table for the new boot partition by

69
00:05:38,600 --> 00:05:41,690
calling esp OTA set boot partition.

70
00:05:42,080 --> 00:05:49,590
And here it's mentioned that after this calling esp restart will boot the newly configured application

71
00:05:49,590 --> 00:05:50,430
partition.

72
00:05:50,550 --> 00:05:54,240
Which brings us to the next function esp restart.

73
00:05:54,270 --> 00:06:02,610
This function will restart both CPUs, both the pro and application CPUs will be restarted and the function

74
00:06:02,610 --> 00:06:04,200
does not return of course.

75
00:06:05,090 --> 00:06:05,450
All right.

76
00:06:05,450 --> 00:06:09,260
So let's put this plan into action and I'll see you in the programming sections.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,890 --> 00:00:11,870
We're going to start the OTA update section by defining a few status definitions pertaining to whether

2
00:00:11,870 --> 00:00:15,260
the update is pending, successful or it's failed.

3
00:00:15,260 --> 00:00:20,440
And our JavaScript function for getting the status is already prepared for reacting to these statuses.

4
00:00:20,450 --> 00:00:24,050
So let's head over to the App.js file and take a look.

5
00:00:25,220 --> 00:00:31,160
And here in the Git status function it says if flashing was complete, the status is one else, it's

6
00:00:31,160 --> 00:00:32,150
a negative one.

7
00:00:32,150 --> 00:00:34,730
And here we have the successful situation.

8
00:00:35,630 --> 00:00:38,540
And the unsuccessful situation is right here.

9
00:00:38,930 --> 00:00:45,200
Okay, so we need to send the statuses accordingly on the web server side so that this JavaScript function

10
00:00:45,200 --> 00:00:46,790
reacts in the appropriate manner.

11
00:00:46,910 --> 00:00:49,010
So let's head over to the header file now.

12
00:00:51,220 --> 00:00:55,180
And here we'll define OTA update pending.

13
00:00:57,960 --> 00:00:58,800
A zero.

14
00:01:00,080 --> 00:01:01,400
And then define.

15
00:01:03,210 --> 00:01:05,160
OTA updates successful.

16
00:01:07,560 --> 00:01:08,550
As one.

17
00:01:12,250 --> 00:01:14,950
And now let's define OTA.

18
00:01:14,980 --> 00:01:16,180
Update failed.

19
00:01:18,290 --> 00:01:19,490
As negative one.

20
00:01:20,390 --> 00:01:24,560
Also, we actually don't need the last enum status here, so let's get rid of it.

21
00:01:30,620 --> 00:01:31,700
And in the C file.

22
00:01:31,700 --> 00:01:33,620
Let's remove the case for it as well.

23
00:01:38,940 --> 00:01:41,280
Okay, so now back to the header file.

24
00:01:42,900 --> 00:01:46,110
Let's define a timer callback function.

25
00:01:50,960 --> 00:01:55,070
Which calls esp restart upon successful firmware update.

26
00:02:01,880 --> 00:02:06,980
And here we'll say firmware update, reset callback.

27
00:02:08,910 --> 00:02:11,430
And it takes a void pointer argument.

28
00:02:12,860 --> 00:02:13,550
Okay.

29
00:02:13,550 --> 00:02:18,620
And let's actually name it properly and add the Http server to it.

30
00:02:22,140 --> 00:02:23,340
Okay, that's better.

31
00:02:23,880 --> 00:02:25,920
Now we'll head over to the C file.

32
00:02:27,990 --> 00:02:29,100
And include.

33
00:02:30,280 --> 00:02:32,020
DSP OTA ops.

34
00:02:33,880 --> 00:02:36,250
And that's for OTA functions.

35
00:02:37,110 --> 00:02:44,670
And also include CIS per MH, and that's for our min macro.

36
00:02:45,900 --> 00:02:50,100
And then we want to create a global variable for firmware update status.

37
00:02:53,210 --> 00:03:01,040
Which is a static int and call it global underscore firmware, underscore, update underscore status

38
00:03:01,160 --> 00:03:04,550
and set it to OTA update pending.

39
00:03:09,150 --> 00:03:18,300
And now let's copy this variable and let's bring it to the monitor under OTA update successful and let's

40
00:03:18,300 --> 00:03:19,440
set it to OTA.

41
00:03:19,470 --> 00:03:20,970
Update Successful.

42
00:03:22,460 --> 00:03:23,030
Okay.

43
00:03:23,720 --> 00:03:26,060
And then under OTA update failed.

44
00:03:26,060 --> 00:03:27,710
Let's set it to OTA.

45
00:03:27,740 --> 00:03:28,850
Update failed.

46
00:03:34,800 --> 00:03:39,570
So now in the app.js, let's see what handlers we need to define.

47
00:03:41,770 --> 00:03:43,510
Within update firmware.

48
00:03:44,210 --> 00:03:47,180
We have a post for OTA update.

49
00:03:47,690 --> 00:03:48,440
Okay.

50
00:03:48,560 --> 00:03:53,150
And when the web page is accessed, get update status is called.

51
00:03:55,240 --> 00:04:01,120
And there we have the forward slash OTA status and that's also a post method.

52
00:04:01,450 --> 00:04:07,180
So here we have two post methods, OTA update and OTA status to be handled.

53
00:04:07,510 --> 00:04:09,580
So let's go back to the C file.

54
00:04:10,330 --> 00:04:12,610
And down to our Uri handlers.

55
00:04:18,210 --> 00:04:20,310
All right, So here, let's register.

56
00:04:21,690 --> 00:04:23,310
OTA update handler.

57
00:04:26,170 --> 00:04:31,150
And we need an instance of the structure and call it OTA.

58
00:04:31,210 --> 00:04:32,590
Underscore update.

59
00:04:35,500 --> 00:04:36,040
And the.

60
00:04:37,850 --> 00:04:40,880
Will be forward slash OTA update.

61
00:04:45,780 --> 00:04:49,530
And the method will be http post.

62
00:04:52,310 --> 00:04:58,760
And the handler will call Http server OTA update handler.

63
00:05:04,880 --> 00:05:07,580
And we can set the user ctcs to null.

64
00:05:11,090 --> 00:05:11,570
Okay.

65
00:05:11,570 --> 00:05:16,820
And then call Httpd, register Uri Handler and pass the handle.

66
00:05:17,730 --> 00:05:20,490
And then a reference to the OTA update struct.

67
00:05:22,870 --> 00:05:23,530
Okay.

68
00:05:24,200 --> 00:05:27,410
Now we'll register the OTA status handler.

69
00:05:32,330 --> 00:05:34,310
And call it OTA status.

70
00:05:39,870 --> 00:05:44,130
And for the Uri that will be forward slash OTA status.

71
00:05:50,700 --> 00:05:55,560
And then the method will be Http post as well.

72
00:05:58,220 --> 00:05:59,330
And the handler.

73
00:06:00,810 --> 00:06:05,220
We'll call Http server OTA status handler.

74
00:06:08,650 --> 00:06:10,870
User is is null.

75
00:06:14,590 --> 00:06:16,840
And then we'll register the handler.

76
00:06:21,090 --> 00:06:24,300
Pass the handle and a reference to the OTA struct.

77
00:06:29,200 --> 00:06:32,560
Okay, next, let's define the OTA update handler.

78
00:06:36,420 --> 00:06:38,010
And let's make a comment here.

79
00:06:38,670 --> 00:06:40,500
Receives the bin file.

80
00:06:43,300 --> 00:06:47,140
Via the web page and handles the firmware update.

81
00:06:49,200 --> 00:06:51,080
And the parameter req.

82
00:06:51,330 --> 00:06:55,530
Is the Http request for which the Uri needs to be handled.

83
00:07:03,340 --> 00:07:05,440
And the return is spoke.

84
00:07:06,550 --> 00:07:12,820
Otherwise esp fail if timeout occurs and the update cannot be started.

85
00:07:19,010 --> 00:07:27,290
And the return is ESP error type and it's our OTA update handler which takes a pointer to the Httpd

86
00:07:27,320 --> 00:07:29,810
request type and its req.

87
00:07:32,040 --> 00:07:36,210
And here we need an instance of the ESP to handle structure.

88
00:07:39,030 --> 00:07:41,010
And we'll call it to handle.

89
00:07:42,500 --> 00:07:46,160
And next we need a buffer to hold data received from the web page.

90
00:07:46,160 --> 00:07:51,680
So say char to buffer and it's 1024 bytes.

91
00:07:53,350 --> 00:07:56,110
And also we need a variable to hold the content length.

92
00:07:56,110 --> 00:07:58,390
So say int content length.

93
00:08:00,610 --> 00:08:05,740
Equals the request content length and we can access that like so.

94
00:08:07,140 --> 00:08:10,350
And also we need to track the content received.

95
00:08:12,400 --> 00:08:13,870
And set it to zero.

96
00:08:14,200 --> 00:08:20,780
And let's add another variable to receive data from each Http request function call and call it int

97
00:08:20,800 --> 00:08:22,330
receive length.

98
00:08:24,830 --> 00:08:30,020
And also we need a variable to tell us when the actual firmware update file content is found.

99
00:08:30,020 --> 00:08:33,920
So we'll say bool is request bodies started.

100
00:08:36,010 --> 00:08:37,490
And set it to false.

101
00:08:37,510 --> 00:08:40,210
And also, we need to track the flash status.

102
00:08:40,210 --> 00:08:46,210
So call this one flash successful and set it to false.

103
00:08:50,210 --> 00:08:50,540
Okay.

104
00:08:50,540 --> 00:08:53,900
Now we need an instance of the esp partition struct.

105
00:08:54,110 --> 00:08:58,760
And that's a pointer to a constant esp partition type.

106
00:09:02,680 --> 00:09:04,870
And call it update partition.

107
00:09:07,370 --> 00:09:10,880
Which equals the result of esp OTA.

108
00:09:11,090 --> 00:09:13,370
Get next update partition.

109
00:09:15,050 --> 00:09:16,730
And the parameter is null.

110
00:09:18,990 --> 00:09:19,650
Okay.

111
00:09:19,650 --> 00:09:21,540
And if we follow this function.

112
00:09:22,340 --> 00:09:28,280
We can see that it returns the next application partition, which should be written with new firmware.

113
00:09:28,280 --> 00:09:35,540
And to call this function to find an application partition which can be passed to ESP to begin.

114
00:09:36,570 --> 00:09:41,100
So next, let's create a do while loop to receive the update file.

115
00:09:44,480 --> 00:09:47,780
And it's while receive length.

116
00:09:48,930 --> 00:09:52,590
Is greater than zero and content received.

117
00:09:54,710 --> 00:09:57,080
Is less than content length.

118
00:10:02,070 --> 00:10:02,640
Okay.

119
00:10:02,640 --> 00:10:06,900
And the first thing we'll do here is read the data for the request.

120
00:10:11,710 --> 00:10:14,200
And say if receive length.

121
00:10:16,520 --> 00:10:20,210
Equals Httpd requests receive.

122
00:10:23,590 --> 00:10:25,630
In the first parameter is RK.

123
00:10:26,260 --> 00:10:32,950
The second is OTA buffer and the third is the minimum between the content length.

124
00:10:35,700 --> 00:10:38,400
And the size of the buffer.

125
00:10:41,140 --> 00:10:43,990
And if this result is less than zero.

126
00:10:45,000 --> 00:10:47,960
Then we need to handle the timeout error case here.

127
00:10:47,970 --> 00:10:51,180
So let's say check if timeout occurred.

128
00:10:55,310 --> 00:10:57,920
And then we'll write if received length.

129
00:11:00,790 --> 00:11:04,510
Is httpd socket error timeout.

130
00:11:10,350 --> 00:11:12,270
Then we will log a message.

131
00:11:16,260 --> 00:11:18,960
That the OTA update handler function.

132
00:11:24,550 --> 00:11:27,520
Has experienced a socket timeout.

133
00:11:31,690 --> 00:11:33,820
And then, let's say, continue.

134
00:11:35,600 --> 00:11:39,470
And will comment retry receiving if timeout occurred.

135
00:11:45,390 --> 00:11:48,000
Otherwise we can log a message.

136
00:11:51,670 --> 00:11:53,290
That there were some other error.

137
00:11:54,100 --> 00:12:00,640
So we'll say that the OTA update handler experienced OTA other error.

138
00:12:03,860 --> 00:12:06,530
And we can actually print the received length.

139
00:12:14,600 --> 00:12:18,200
Okay, so then at this point we can return esp fail.

140
00:12:24,420 --> 00:12:26,280
All right, so now we can continue.

141
00:12:26,610 --> 00:12:28,500
And here, let's print.

142
00:12:31,110 --> 00:12:32,010
Let's print that.

143
00:12:32,010 --> 00:12:37,920
The OTA update handler has received some bytes of the content.

144
00:12:40,000 --> 00:12:44,290
And we'll give it the content received and the content length.

145
00:12:56,890 --> 00:12:57,340
All right.

146
00:12:57,340 --> 00:12:58,500
And then we can check.

147
00:12:58,510 --> 00:13:01,060
Is this the first data we are receiving?

148
00:13:04,140 --> 00:13:05,160
If so.

149
00:13:06,910 --> 00:13:09,700
It will have the information in the header that we need.

150
00:13:15,760 --> 00:13:20,290
And first we'll say if the request body is not started.

151
00:13:22,630 --> 00:13:25,630
Then we'll set request body started to true.

152
00:13:31,440 --> 00:13:35,880
And then we'll come here and get the location of the bin file content.

153
00:13:38,990 --> 00:13:43,880
Meaning we'll remove the web form data from the request.

154
00:13:44,270 --> 00:13:54,860
Okay, so now let's say char pointer body start, underscore p equals string string of the buffer.

155
00:13:57,530 --> 00:14:01,910
And we need to find these slash, slash n slash, slash n.

156
00:14:03,110 --> 00:14:05,690
And then increment the pointer by four.

157
00:14:06,430 --> 00:14:07,810
For the length of the slash.

158
00:14:07,990 --> 00:14:08,970
Slash ends.

159
00:14:10,860 --> 00:14:14,010
All right, so now we'll get the body part length.

160
00:14:15,710 --> 00:14:17,360
From the received length.

161
00:14:20,340 --> 00:14:24,570
Minus the difference between the body start pointer.

162
00:14:25,690 --> 00:14:27,940
And the beginning of the buffer.

163
00:14:30,350 --> 00:14:35,630
Okay, so here we needed to get the body start pointer to point to the beginning of the data that we

164
00:14:35,630 --> 00:14:38,110
want without the web form junk data.

165
00:14:38,120 --> 00:14:44,160
And we also need the length of data that we want so that we can pass this information to ESP OTA.

166
00:14:44,180 --> 00:14:44,720
Right.

167
00:14:44,750 --> 00:14:45,980
And we'll do that later.

168
00:14:46,010 --> 00:14:46,670
Okay.

169
00:14:46,880 --> 00:14:49,730
So next, let's print some information.

170
00:14:53,390 --> 00:14:58,370
About the OTA file size so that it shows up while we're receiving the file.

171
00:15:01,270 --> 00:15:03,090
And give it the content length.

172
00:15:15,170 --> 00:15:19,010
And then here we can say ESP error type error.

173
00:15:19,710 --> 00:15:22,020
Equals ESP to begin.

174
00:15:23,100 --> 00:15:28,950
And give it the update partition and then the file size is OTA size unknown.

175
00:15:31,400 --> 00:15:34,130
And then give a reference to the IATA handle.

176
00:15:35,870 --> 00:15:39,640
Okay, then we'll say if error is not equal to ESP.

177
00:15:39,650 --> 00:15:40,400
Okay.

178
00:15:45,260 --> 00:15:47,360
Then print that there was an error.

179
00:15:52,710 --> 00:15:54,420
And we'll say error with.

180
00:15:54,420 --> 00:15:55,740
Oh, to begin.

181
00:16:00,190 --> 00:16:01,440
Canceling OTA.

182
00:16:08,520 --> 00:16:11,220
Okay then return esp fail.

183
00:16:14,850 --> 00:16:16,590
All right, then we'll say else.

184
00:16:17,470 --> 00:16:18,640
And then we'll print that.

185
00:16:18,640 --> 00:16:21,010
We're writing to partition subtype.

186
00:16:23,160 --> 00:16:25,710
And will say writing to partition subtype.

187
00:16:31,340 --> 00:16:32,450
At offset.

188
00:16:39,670 --> 00:16:42,280
And give the update partition subtype.

189
00:16:45,550 --> 00:16:48,310
And the update partition address.

190
00:16:54,350 --> 00:16:59,120
So now let's say right this first part.

191
00:17:00,430 --> 00:17:01,450
Of the data.

192
00:17:02,520 --> 00:17:04,770
And say esp OTA.

193
00:17:04,800 --> 00:17:05,490
Right?

194
00:17:06,570 --> 00:17:08,610
Then pass the otta handle.

195
00:17:10,900 --> 00:17:12,640
The body start pointer.

196
00:17:17,240 --> 00:17:18,830
And the body part length.

197
00:17:24,360 --> 00:17:25,980
And then we'll say else.

198
00:17:27,450 --> 00:17:31,080
In the case that the body data has already been found.

199
00:17:31,080 --> 00:17:37,740
And it's not the first part of the data that we've received and written with ESP OTA write and that

200
00:17:37,740 --> 00:17:40,260
we want to write to data.

201
00:17:42,150 --> 00:17:43,470
So let's comment.

202
00:17:44,530 --> 00:17:49,020
Right OTA data and we'll use esp OTA.

203
00:17:49,030 --> 00:17:49,780
Right.

204
00:17:51,740 --> 00:17:56,690
And then pass the handle and give it the OTA buffer this time.

205
00:17:57,540 --> 00:18:00,300
And we want the received length this time.

206
00:18:01,840 --> 00:18:04,990
And now we want to increment the content received.

207
00:18:08,820 --> 00:18:10,410
By the received length.

208
00:18:14,620 --> 00:18:21,790
So we are going to do this while the receive length is greater than zero and the content received is

209
00:18:21,790 --> 00:18:28,990
less than the content length as we're incrementing the content received with each call to receive data.

210
00:18:30,840 --> 00:18:35,640
So once that's done we can say if esp to end.

211
00:18:40,080 --> 00:18:41,610
In past the handle.

212
00:18:45,000 --> 00:18:47,490
And if Thatrillioneturns is okay.

213
00:18:49,380 --> 00:18:51,690
Then let's update the partition.

214
00:18:55,410 --> 00:18:56,430
And right.

215
00:18:56,610 --> 00:19:02,700
If esp OTA set boot partition and give it the update partition.

216
00:19:05,230 --> 00:19:07,410
If that is okay.

217
00:19:09,270 --> 00:19:13,530
Then the const esp partition type.

218
00:19:15,580 --> 00:19:17,920
Pointer boot partition.

219
00:19:19,970 --> 00:19:24,110
Equals esp OTA get boot partition.

220
00:19:25,210 --> 00:19:29,590
And now let's log information that about the next boot partition.

221
00:19:36,180 --> 00:19:39,480
And say next boot partition subtype.

222
00:19:40,270 --> 00:19:42,370
Is at offset.

223
00:19:46,450 --> 00:19:49,120
And then give the boot partition subtype.

224
00:19:51,730 --> 00:19:53,950
And the boot partition address.

225
00:19:56,660 --> 00:19:59,840
Okay then set flash successful to true.

226
00:20:05,370 --> 00:20:09,450
Else we need to log an error that says flashed error.

227
00:20:12,540 --> 00:20:14,670
So let's log it about this function.

228
00:20:16,340 --> 00:20:18,350
And we'll say flashed error.

229
00:20:23,620 --> 00:20:27,130
And then if esp OTA n didn't go well.

230
00:20:29,270 --> 00:20:30,650
We also have an error.

231
00:20:33,210 --> 00:20:34,170
In that air.

232
00:20:34,290 --> 00:20:36,660
That's from ESP OTA and.

233
00:20:42,900 --> 00:20:43,230
Okay.

234
00:20:43,230 --> 00:20:46,830
And lastly, we won't update global variables throughout the file.

235
00:20:53,380 --> 00:20:56,140
So let's send the message about the status.

236
00:20:57,170 --> 00:20:59,630
And we can say if successful.

237
00:21:01,650 --> 00:21:06,930
And then we could one line this http server monitor send message.

238
00:21:13,720 --> 00:21:17,290
Http message ota update successful.

239
00:21:25,770 --> 00:21:26,460
Else.

240
00:21:29,640 --> 00:21:31,380
We'll send a message.

241
00:21:36,330 --> 00:21:40,110
That http message OTA update failed.

242
00:21:46,970 --> 00:21:47,510
All right.

243
00:21:47,510 --> 00:21:49,070
And now we can return.

244
00:21:49,580 --> 00:21:49,970
Okay.

245
00:21:55,470 --> 00:21:56,780
Okay, well done.

246
00:21:56,790 --> 00:22:00,090
So we have a bit more to do, but I think that's enough time for now.

247
00:22:00,090 --> 00:22:03,330
So let's take a short break and let's continue in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,040 --> 00:00:08,540
Okay, let's continue.

2
00:00:09,240 --> 00:00:12,510
And grab the OTA status handler function name.

3
00:00:13,940 --> 00:00:15,650
And let's define it up here.

4
00:00:20,010 --> 00:00:25,590
And comment that OTA status handler responds with the firmware update status.

5
00:00:26,400 --> 00:00:29,400
After the OTA update is started.

6
00:00:31,680 --> 00:00:34,050
And response with the compile time.

7
00:00:36,730 --> 00:00:37,570
And date.

8
00:00:38,810 --> 00:00:41,060
When the page is first requested.

9
00:00:44,360 --> 00:00:50,840
And the parameter req is Http request for which the Uri needs to be handled.

10
00:01:00,140 --> 00:01:01,800
And the return is ESP.

11
00:01:01,850 --> 00:01:02,270
Okay.

12
00:01:05,270 --> 00:01:05,720
All right.

13
00:01:05,720 --> 00:01:07,760
And this is an ESP error type.

14
00:01:08,480 --> 00:01:13,880
And it's our OTA status handler which takes the Httpd request type.

15
00:01:14,870 --> 00:01:16,400
Pointer to rec.

16
00:01:17,840 --> 00:01:21,080
And let's create a Json buffer.

17
00:01:22,630 --> 00:01:24,520
With length 100.

18
00:01:26,820 --> 00:01:30,900
And then log that OTA status is requested.

19
00:01:39,670 --> 00:01:44,110
Now we're going to print F into Json.

20
00:01:45,570 --> 00:01:50,790
And now just follow me as we enter the Jason escape sequence that's required.

21
00:01:52,070 --> 00:01:56,960
Just like so and into our OTA update status.

22
00:01:59,080 --> 00:02:00,490
And then continue.

23
00:02:05,730 --> 00:02:08,040
And then enter the compile time.

24
00:02:16,400 --> 00:02:18,530
And then next, the compiled date.

25
00:02:24,100 --> 00:02:28,900
And then we can close it and then give it the global firmware update status.

26
00:02:30,640 --> 00:02:33,190
And then give it the time definition.

27
00:02:34,350 --> 00:02:35,730
And the date.

28
00:02:39,430 --> 00:02:41,080
And that's it for the Json.

29
00:02:41,110 --> 00:02:43,720
So now let's set the response type.

30
00:02:48,150 --> 00:02:51,720
For this request as application Json.

31
00:02:56,010 --> 00:02:59,070
And then we're going to send the response for the request.

32
00:03:04,500 --> 00:03:12,390
From the Json and we want strlen of the Json.

33
00:03:15,810 --> 00:03:17,670
And then now just return ESP.

34
00:03:17,700 --> 00:03:18,090
Okay.

35
00:03:23,760 --> 00:03:24,090
All right.

36
00:03:24,090 --> 00:03:30,120
So here we just updated the web page with the OTA update status, compile time and compile date using

37
00:03:30,120 --> 00:03:31,320
the values from here.

38
00:03:33,700 --> 00:03:40,300
So now let's see how this works by going over to App.js and go to Git update status.

39
00:03:43,630 --> 00:03:44,050
Here.

40
00:03:44,050 --> 00:03:52,090
We need the compiled date and time is updated for this latest firmware element ID, which is here in

41
00:03:52,090 --> 00:03:54,010
the index.html.

42
00:03:56,790 --> 00:03:57,360
All right.

43
00:03:57,360 --> 00:04:04,470
And then depending on the OTA update status, we respond with either the reboot timer is started or

44
00:04:04,470 --> 00:04:07,080
the upload error message is shown on the page.

45
00:04:08,970 --> 00:04:16,110
And the reboot timer updates with a message here and the reboot timer is called recursively here Decrementing

46
00:04:16,110 --> 00:04:16,890
each time.

47
00:04:17,280 --> 00:04:17,970
All right.

48
00:04:17,970 --> 00:04:21,930
So we'll need to configure this timer on the web server side as well.

49
00:04:21,960 --> 00:04:25,320
So let's go back to the Http server C file.

50
00:04:25,990 --> 00:04:27,730
And at the top of the file.

51
00:04:31,750 --> 00:04:35,980
We can create the ESP 32 timer configuration.

52
00:04:38,680 --> 00:04:40,530
Which is passed to ESP.

53
00:04:40,570 --> 00:04:41,680
Timer create.

54
00:04:46,620 --> 00:04:51,390
And then say const esp timer create args type.

55
00:04:56,590 --> 00:04:59,050
And call it firmware update reset.

56
00:05:06,250 --> 00:05:07,780
And now we need a callback.

57
00:05:09,180 --> 00:05:13,380
Which is our firmware update reset callback.

58
00:05:15,860 --> 00:05:16,850
Right here.

59
00:05:22,280 --> 00:05:30,740
And then our ARG is null and the dispatch method is esp timer task.

60
00:05:34,650 --> 00:05:38,460
And the name is firmware update Reset.

61
00:05:42,520 --> 00:05:43,150
Okay.

62
00:05:43,630 --> 00:05:46,960
Now say esp timer handle type.

63
00:05:48,630 --> 00:05:50,970
Is firmware update reset.

64
00:05:54,240 --> 00:05:56,850
And next, we need another function.

65
00:05:57,530 --> 00:05:59,510
And we'll define another function here.

66
00:06:01,780 --> 00:06:04,660
Which checks the global firmware update status.

67
00:06:06,960 --> 00:06:09,390
Which is this variable right here.

68
00:06:13,650 --> 00:06:18,840
So we're going to check it and it creates the firmware update reset timer.

69
00:06:25,230 --> 00:06:28,350
If the global firmware update status is true.

70
00:06:30,270 --> 00:06:32,400
And that'll be a static void.

71
00:06:33,640 --> 00:06:35,140
Http server.

72
00:06:36,090 --> 00:06:38,490
Firmware Update Reset timer.

73
00:06:40,290 --> 00:06:41,340
And it's void.

74
00:06:43,220 --> 00:06:43,670
All right.

75
00:06:43,670 --> 00:06:50,450
So say if global firmware update status is OTA update successful?

76
00:06:56,460 --> 00:06:58,350
Then log.

77
00:07:03,380 --> 00:07:04,220
That.

78
00:07:05,940 --> 00:07:07,050
For more updates.

79
00:07:07,050 --> 00:07:08,100
Successful.

80
00:07:18,740 --> 00:07:23,600
And then we'll give the Web page a chance to receive and acknowledge back.

81
00:07:31,230 --> 00:07:33,060
And initialize the timer.

82
00:07:35,720 --> 00:07:37,880
Then esp error check.

83
00:07:39,580 --> 00:07:41,440
ESP timer create.

84
00:07:44,550 --> 00:07:50,400
And pass a reference to the reset args and a reference to the firmware update reset.

85
00:07:52,630 --> 00:07:55,120
Now we need to esp error check.

86
00:07:56,190 --> 00:07:58,320
ESP timer start once.

87
00:08:02,060 --> 00:08:07,310
And pass the firmware update reset and the time in microseconds.

88
00:08:08,660 --> 00:08:09,530
Which we can do.

89
00:08:09,560 --> 00:08:11,300
Maybe eight seconds here.

90
00:08:12,230 --> 00:08:14,180
So we'll say else.

91
00:08:15,670 --> 00:08:16,930
ESP log.

92
00:08:24,840 --> 00:08:28,230
That the firmware update was unsuccessful.

93
00:08:35,700 --> 00:08:38,430
Okay, so now let's grab this function.

94
00:08:39,610 --> 00:08:43,690
And we're going to call it here under the firmware update.

95
00:08:43,690 --> 00:08:45,250
Successful case.

96
00:08:48,370 --> 00:08:48,760
All right.

97
00:08:48,790 --> 00:08:50,350
Next, let's go down.

98
00:08:51,920 --> 00:08:54,050
And we need to define our callback.

99
00:08:54,770 --> 00:08:57,080
So let's take the prototype here.

100
00:09:00,330 --> 00:09:02,310
And then let's drop it right here.

101
00:09:04,390 --> 00:09:06,610
And we'll say esp log.

102
00:09:14,570 --> 00:09:16,340
That the timer timed out.

103
00:09:20,480 --> 00:09:22,220
Restarting the device.

104
00:09:27,360 --> 00:09:30,420
All right then call esp restart.

105
00:09:32,370 --> 00:09:34,290
Okay, so that looks good.

106
00:09:36,420 --> 00:09:38,790
And one more thing that I forgot here.

107
00:09:41,480 --> 00:09:47,090
In the update handler was to increment the content received by the body part length.

108
00:09:47,600 --> 00:09:49,070
So let's do that.

109
00:09:55,290 --> 00:09:57,210
Now let's build the project.

110
00:10:08,120 --> 00:10:09,410
And we have no errors.

111
00:10:09,440 --> 00:10:09,740
Great.

112
00:10:09,740 --> 00:10:11,810
So let's test this out in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,940 --> 00:00:07,210
All right.

2
00:00:07,210 --> 00:00:11,320
So let's test this out by first going over to the project CMake list file.

3
00:00:11,680 --> 00:00:16,120
And here let's change the project file name to firmware update test.

4
00:00:18,930 --> 00:00:25,350
All right, now let's go to wi fi approach and let's change the Ssid to firmware update test.

5
00:00:29,500 --> 00:00:29,770
All right.

6
00:00:29,770 --> 00:00:33,820
Now let's go to the style sheet and we can change the background color to something else.

7
00:00:34,150 --> 00:00:38,950
I'll just use two, two, two, two, two, two, and then just build the project.

8
00:00:46,860 --> 00:00:49,600
All right, so now let's just give this a chance to build.

9
00:00:49,630 --> 00:00:55,540
And meanwhile, I can show you where the application file is, so just follow me here.

10
00:00:56,840 --> 00:00:58,460
We're going to go to the build folder.

11
00:01:00,520 --> 00:01:00,850
All right.

12
00:01:00,850 --> 00:01:02,260
So that's the build folder.

13
00:01:02,410 --> 00:01:08,140
We're just going to wait for the build to finish so we can grab our firmware update test bin file.

14
00:01:12,560 --> 00:01:13,610
Okay, so now it's done.

15
00:01:13,610 --> 00:01:15,230
Let's go grab the test file.

16
00:01:19,220 --> 00:01:20,300
All right, So here it is.

17
00:01:20,330 --> 00:01:22,490
Let's just keep that somewhere easy to find.

18
00:01:26,200 --> 00:01:28,930
Okay, so now we can just go undo all of our changes.

19
00:01:28,930 --> 00:01:32,380
So let's undo what we did to the style sheet.

20
00:01:34,400 --> 00:01:38,000
And change the side back as well in here.

21
00:01:38,390 --> 00:01:43,280
And let's also change the file name back to normal.

22
00:01:43,430 --> 00:01:44,930
And then let's build again.

23
00:01:53,880 --> 00:01:56,310
Okay, so now we can open up Google Chrome.

24
00:02:05,860 --> 00:02:06,210
All right.

25
00:02:06,210 --> 00:02:09,900
So once the build finishes, we can flash it.

26
00:02:10,110 --> 00:02:11,640
So go ahead and flash.

27
00:02:26,170 --> 00:02:31,030
Okay, so we've fleshed and now we can open up a monitor so we can check out what's going on while we

28
00:02:31,030 --> 00:02:32,590
have the web page open as well.

29
00:02:37,780 --> 00:02:40,660
All right, So now we need to connect to the ISP.

30
00:02:41,470 --> 00:02:44,710
So let's go down to the available Wi-Fi networks.

31
00:02:47,440 --> 00:02:49,000
Let's connect to our ISP.

32
00:02:49,420 --> 00:02:50,770
The normal side.

33
00:02:54,870 --> 00:02:57,390
Okay, so now let's go to our IP address.

34
00:03:04,630 --> 00:03:04,990
Okay.

35
00:03:04,990 --> 00:03:05,410
Very cool.

36
00:03:05,410 --> 00:03:07,930
We have our date and time showing up right here.

37
00:03:08,710 --> 00:03:10,390
Now let's select the file.

38
00:03:13,790 --> 00:03:16,130
And mine is here somewhere on the desktop.

39
00:03:18,770 --> 00:03:20,360
Okay, there's my firmware update.

40
00:03:20,390 --> 00:03:21,170
Test bin.

41
00:03:22,190 --> 00:03:24,290
Okay, so now we have the file size right there.

42
00:03:24,320 --> 00:03:26,030
Now let's click update firmware.

43
00:03:31,110 --> 00:03:34,950
And now we can see in the monitor that we're receiving the file.

44
00:03:35,040 --> 00:03:39,360
But on the Web page, it's already showing that the firmware update is completed.

45
00:03:39,360 --> 00:03:43,200
So the monitor is lagging, probably due to the repeated print deaths.

46
00:03:43,200 --> 00:03:44,370
So anyway, great.

47
00:03:44,370 --> 00:03:46,140
The ESP is now rebooting.

48
00:03:49,750 --> 00:03:51,670
And if we reconnect.

49
00:03:53,390 --> 00:03:57,470
So now let's let's reconnect to the firmware update test side.

50
00:03:59,380 --> 00:04:01,840
That's our test side, so connect to it.

51
00:04:03,220 --> 00:04:05,950
And then let's open up the web page again.

52
00:04:06,800 --> 00:04:07,430
All right, great.

53
00:04:07,430 --> 00:04:11,240
So now we can confirm that our firmware update application is indeed running.

54
00:04:11,240 --> 00:04:12,050
Well done.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: DHT22 Sensor


1
00:00:06,530 --> 00:00:07,450
Hey, welcome back.

2
00:00:07,460 --> 00:00:11,900
In this section, we'll implement the Dht22 sensor portion of the project.

3
00:00:11,900 --> 00:00:13,700
So let's take a look at the overview.

4
00:00:14,610 --> 00:00:21,420
In this course we are using the A2302 Dht22 temperature and humidity sensor module.

5
00:00:21,570 --> 00:00:26,970
This is a very popular, easy to find module, and if you do an online search for this sensor, you

6
00:00:26,970 --> 00:00:30,420
should be able to find an online store that can ship it to your home country.

7
00:00:30,540 --> 00:00:36,450
This module outputs a single digital signal and contains a calibrated temperature and humidity combined

8
00:00:36,480 --> 00:00:37,230
sensor.

9
00:00:37,620 --> 00:00:43,200
It only requires three connections, so you'll just connect the data line to the Gpio that we'll define

10
00:00:43,200 --> 00:00:50,730
in the firmware and also connect the VCC and ground lines on the Esp32 to VCC and the ground lines on

11
00:00:50,730 --> 00:00:52,710
the Dht22 sensor.

12
00:00:52,980 --> 00:00:55,470
Also a couple of more notes about the sensor.

13
00:00:55,500 --> 00:01:03,990
It provides higher accuracy than the Dht11 variant and the temperature range is from -40 to 80°C and

14
00:01:03,990 --> 00:01:07,230
the humidity range is from 20 to 90%.

15
00:01:07,290 --> 00:01:11,760
And here is how I've connected the Dht22 to my rover dev kit.

16
00:01:11,790 --> 00:01:20,650
The blue wire 3.3V on the dev kit is connected to VCC on the dht22 and the gray wire ground on the dev

17
00:01:20,650 --> 00:01:29,440
kit is connected to ground on the dht22 and the purple wire is Gpio 25 on the dev kit and connected

18
00:01:29,440 --> 00:01:32,080
to data on the dht22.

19
00:01:32,440 --> 00:01:35,020
All right, so that's the three connections that we need.

20
00:01:36,020 --> 00:01:36,320
All right.

21
00:01:36,320 --> 00:01:39,530
So let's take a look at how we'll accomplish getting the sensor data.

22
00:01:39,560 --> 00:01:45,350
The sensor data readings will be handled by an existing library for the Dht22 sensor.

23
00:01:45,470 --> 00:01:51,710
I've attached the Dht22 dot C and H files to the resources for this section.

24
00:01:51,830 --> 00:01:54,890
We'll include these files directly under the main folder.

25
00:01:54,980 --> 00:02:01,520
We'll create a freertos task to read the Dht22 data at a specified interval and we'll test it.

26
00:02:01,550 --> 00:02:09,530
Next, we'll update the web page files, the index.html, app.css and App.js files in order to display

27
00:02:09,530 --> 00:02:15,560
the updated data, and the web server will then need to be updated to respond to the get requests with

28
00:02:15,560 --> 00:02:19,100
temperature and humidity data from the Dht22 sensor.

29
00:02:20,600 --> 00:02:21,320
And that's it.

30
00:02:21,320 --> 00:02:22,820
So now let's get the programming.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,030 --> 00:00:12,490
Okay, so let's start off by inserting the Dht22 sensor driver files into our project.

2
00:00:12,520 --> 00:00:16,570
Be sure to have the resource files handy and we'll include them now.

3
00:00:16,930 --> 00:00:22,420
I have my resources folder here, so I'm going to copy the source and header files and paste them under

4
00:00:22,420 --> 00:00:23,470
the main folder.

5
00:00:28,570 --> 00:00:31,150
Okay, so now let's maximize eclipse.

6
00:00:32,410 --> 00:00:37,060
And then let's refresh the project by right clicking and going down to refresh.

7
00:00:38,870 --> 00:00:45,290
Then let's go to the CMake list file and add the Dht22 dot c file to the list.

8
00:00:49,600 --> 00:00:53,300
Now, save that and let's open the Dht22 files.

9
00:00:57,390 --> 00:00:59,280
Okay, now let's go to tasks common.

10
00:01:01,950 --> 00:01:06,120
And let's enter the information for the Dht22 sensor task.

11
00:01:11,650 --> 00:01:16,060
Next to find the Dht22 task stack size.

12
00:01:18,710 --> 00:01:20,780
As 4096 bytes.

13
00:01:23,010 --> 00:01:25,980
Now define the dht22.

14
00:01:27,640 --> 00:01:28,480
Priority.

15
00:01:30,950 --> 00:01:32,480
And we can make it five.

16
00:01:34,070 --> 00:01:38,720
And now let's define the DHT 22 task core ID.

17
00:01:42,640 --> 00:01:43,660
As core one.

18
00:01:45,510 --> 00:01:51,300
Okay, so now all of the other tasks are on core zero and the Dht22 is on core one.

19
00:01:51,540 --> 00:01:51,840
All right.

20
00:01:51,840 --> 00:01:54,350
So next go to dht22 dot.

21
00:01:56,170 --> 00:01:57,850
And here let's define.

22
00:01:58,800 --> 00:02:00,930
DHT Gpio.

23
00:02:03,670 --> 00:02:05,380
As I owe 25.

24
00:02:06,690 --> 00:02:09,060
Then let's create a prototype that.

25
00:02:10,030 --> 00:02:13,210
Starts the Dht22 sensor task.

26
00:02:21,490 --> 00:02:23,110
And this will be a void.

27
00:02:23,500 --> 00:02:26,350
DHT 22 Task start.

28
00:02:27,760 --> 00:02:28,750
And it's void.

29
00:02:32,560 --> 00:02:33,940
Okay, so copy that.

30
00:02:35,110 --> 00:02:36,340
Go to the C file.

31
00:02:37,080 --> 00:02:39,960
But first let's include the tasks comment.

32
00:02:45,200 --> 00:02:47,120
And then we'll go to the bottom of the file.

33
00:02:48,830 --> 00:02:50,930
And define the task start function.

34
00:02:54,750 --> 00:02:59,280
Okay, now write void and it's our task start and it's void.

35
00:03:00,300 --> 00:03:04,140
And first we'll use the ECS task create PIN to core.

36
00:03:08,370 --> 00:03:12,420
And we'll call the task function DBT 22 task.

37
00:03:14,790 --> 00:03:16,440
And the tag can be the same.

38
00:03:19,640 --> 00:03:22,430
And the stack depth is DHT 22.

39
00:03:22,460 --> 00:03:24,050
Task Stack size.

40
00:03:29,380 --> 00:03:31,270
The PV parameters is null.

41
00:03:32,230 --> 00:03:34,680
The priority is DHT 22.

42
00:03:34,700 --> 00:03:35,960
Task Priority.

43
00:03:40,550 --> 00:03:42,200
And also the handle is null.

44
00:03:43,560 --> 00:03:47,250
And the core ID is DHT 22 Task Core ID.

45
00:03:54,760 --> 00:03:58,390
And now we can define the Dht22 sensor task.

46
00:04:01,230 --> 00:04:01,500
All right.

47
00:04:01,500 --> 00:04:04,590
So we could say Dht22 sensor task.

48
00:04:07,350 --> 00:04:08,970
Which is a static void.

49
00:04:10,450 --> 00:04:13,060
And it's our 22 task.

50
00:04:13,820 --> 00:04:16,640
And it takes a void pointer PV parameter.

51
00:04:21,260 --> 00:04:23,870
Then we'll call set DHT, Gpio.

52
00:04:27,500 --> 00:04:30,470
And this is a function from the driver which sets the Gpio.

53
00:04:30,470 --> 00:04:33,470
So let's pass our defined DTE Gpio.

54
00:04:38,910 --> 00:04:40,230
Then let's print.

55
00:04:41,550 --> 00:04:43,470
Starting DBT task.

56
00:04:47,770 --> 00:04:49,840
Next, we'll make an endless four loop.

57
00:04:52,190 --> 00:04:53,390
And then print.

58
00:04:54,570 --> 00:04:55,920
Reading DBT.

59
00:05:05,210 --> 00:05:12,050
They now say int return equals and call read DHT function from the driver.

60
00:05:14,950 --> 00:05:19,870
Then we'll use the air handler from the driver, which is air handler.

61
00:05:22,320 --> 00:05:23,730
And give it the return.

62
00:05:26,080 --> 00:05:29,260
And now let's print out humidity and temperature.

63
00:05:30,330 --> 00:05:33,930
So we'll print the humidity to one decimal place.

64
00:05:37,560 --> 00:05:42,090
And give it the result of the Jit humidity function from the driver.

65
00:05:43,440 --> 00:05:46,140
And also print the temperature in the same manner.

66
00:05:50,380 --> 00:05:54,340
And give it the result of the jet temperature function from the driver.

67
00:05:59,100 --> 00:06:03,120
Now, let's wait at least two seconds before reading again.

68
00:06:08,750 --> 00:06:13,520
And I'll also say the interval of the whole process must be more than two seconds.

69
00:06:18,580 --> 00:06:18,970
All right.

70
00:06:18,970 --> 00:06:22,390
And that is simply what is recommended by the creators of this driver.

71
00:06:22,420 --> 00:06:25,570
So here we can try a delay of four seconds.

72
00:06:28,410 --> 00:06:29,820
So 4000.

73
00:06:30,800 --> 00:06:32,000
Milliseconds.

74
00:06:37,250 --> 00:06:38,960
And see how that works for now.

75
00:06:39,870 --> 00:06:44,370
Now call the task start function from Main, so we'll copy this.

76
00:06:46,500 --> 00:06:47,340
Go to Main.

77
00:06:48,190 --> 00:06:51,520
And now we'll include the dht22 dot h file.

78
00:06:58,450 --> 00:07:02,470
And then now let's say start Dht22 sensor task.

79
00:07:04,890 --> 00:07:06,660
Well, let's paste our function here.

80
00:07:07,690 --> 00:07:09,160
And then build the project.

81
00:07:12,590 --> 00:07:14,270
Let's let the build finish.

82
00:07:14,480 --> 00:07:20,180
And in the meantime, be sure that you've connected the Dht22 sensor to your dev kit because we're going

83
00:07:20,180 --> 00:07:24,080
to test our functions to be sure that we can read and print the sensor data.

84
00:07:32,470 --> 00:07:33,550
Now flesh.

85
00:07:33,980 --> 00:07:35,000
Once you're ready.

86
00:07:38,550 --> 00:07:45,000
And we can ignore that because it's only referring to some unresolved includes from the DHT 22 files

87
00:07:45,000 --> 00:07:45,510
here.

88
00:07:49,170 --> 00:07:50,400
Now it's resolved.

89
00:07:50,400 --> 00:07:51,840
And this one.

90
00:07:51,870 --> 00:07:53,430
This one is resolved to.

91
00:07:55,090 --> 00:07:57,100
Okay, Now let's open the monitor.

92
00:08:04,690 --> 00:08:06,130
And we have sensor data readings.

93
00:08:06,130 --> 00:08:06,760
Great.

94
00:08:07,120 --> 00:08:09,820
And in my home, the humidity is under 55%.

95
00:08:09,820 --> 00:08:11,350
So that's also good news.

96
00:08:11,860 --> 00:08:12,190
All right.

97
00:08:12,190 --> 00:08:16,270
So let's continue in the next lesson and we'll send the sensor data to the Web page.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,740 --> 00:00:07,040
All right.

2
00:00:07,040 --> 00:00:11,890
So first we need to update the HTML document for the Dht22 sensor data.

3
00:00:11,900 --> 00:00:14,240
So let's create a section for it right here.

4
00:00:14,630 --> 00:00:16,010
Let's create a div ID.

5
00:00:18,660 --> 00:00:21,330
And call it Dht22 sensor.

6
00:00:24,390 --> 00:00:30,960
Now let's create an H two and say Dht22 sensor readings.

7
00:00:33,530 --> 00:00:34,790
Now close that.

8
00:00:37,590 --> 00:00:39,660
Then we need a label for.

9
00:00:40,900 --> 00:00:42,190
Temperature reading.

10
00:00:47,420 --> 00:00:48,950
And right temperature.

11
00:00:50,320 --> 00:00:52,930
Colon and close the label.

12
00:00:54,870 --> 00:00:58,050
Next to the div ID for temperature reading.

13
00:01:03,450 --> 00:01:04,980
And then close the div.

14
00:01:09,070 --> 00:01:09,310
Then.

15
00:01:09,310 --> 00:01:13,090
Now we can create a label for humidity reading.

16
00:01:17,640 --> 00:01:22,110
And then let's write humidity colon and then close the label.

17
00:01:25,960 --> 00:01:26,290
Then.

18
00:01:26,290 --> 00:01:29,560
Now let's create the div ID for humidity reading.

19
00:01:34,960 --> 00:01:36,430
And then close the div.

20
00:01:39,890 --> 00:01:43,100
Now we can close the Dht22 sensor div.

21
00:01:44,530 --> 00:01:47,230
And then let's put a horizontal rule right here.

22
00:01:47,440 --> 00:01:50,800
Next, let's grab the temperature reading and go to the style sheet.

23
00:01:52,000 --> 00:01:54,700
And here we'll give it the same styling as some of the other elements.

24
00:01:54,700 --> 00:01:57,610
So let's create the styling for it right here.

25
00:02:00,570 --> 00:02:03,210
And we want to display in line.

26
00:02:03,210 --> 00:02:05,700
So let's grab this one and paste it here.

27
00:02:06,650 --> 00:02:08,490
And we also want to give it the same color.

28
00:02:08,510 --> 00:02:09,890
So let's paste that there.

29
00:02:11,850 --> 00:02:13,350
So now let's copy this.

30
00:02:14,920 --> 00:02:16,270
And then paste it here.

31
00:02:17,070 --> 00:02:18,960
And now we want the humidity reading.

32
00:02:23,320 --> 00:02:24,880
So now just include it there.

33
00:02:26,620 --> 00:02:27,370
All right, that's fine.

34
00:02:27,370 --> 00:02:29,800
So now we can go to App.js.

35
00:02:31,750 --> 00:02:34,060
And now let's go down to the bottom of the file.

36
00:02:38,400 --> 00:02:40,680
So now let's create a function.

37
00:02:41,750 --> 00:02:45,140
That gets the dht22 sensor temperature.

38
00:02:47,580 --> 00:02:49,200
And humidity values.

39
00:02:51,020 --> 00:02:52,890
For display on the Web page.

40
00:02:56,320 --> 00:03:00,910
And we'll say function get DBT sensor values.

41
00:03:05,150 --> 00:03:07,130
Here, we'll use the get Json method.

42
00:03:07,130 --> 00:03:16,190
So say dollar sign dot get Json parentheses, single quotes, forward slash DHT sensor dot Json.

43
00:03:19,260 --> 00:03:21,810
And then function parentheses data.

44
00:03:23,770 --> 00:03:25,690
And then open curly braces.

45
00:03:26,590 --> 00:03:28,510
And say dollar sign.

46
00:03:30,120 --> 00:03:34,020
In quotations pound temperature underscore reading.

47
00:03:36,460 --> 00:03:39,670
And then say dot text in parentheses.

48
00:03:39,670 --> 00:03:43,720
Data brackets in quotes say temp.

49
00:03:47,910 --> 00:03:48,200
Then.

50
00:03:48,200 --> 00:03:49,820
Now let's just copy this.

51
00:03:50,810 --> 00:03:54,650
And then paste it and then just change this to humidity reading.

52
00:03:56,090 --> 00:03:57,200
And now this one, too.

53
00:03:57,230 --> 00:03:58,010
Humidity.

54
00:04:00,400 --> 00:04:02,530
Now, just close it with the semicolon.

55
00:04:04,860 --> 00:04:05,250
All right.

56
00:04:05,250 --> 00:04:10,020
So next, let's create another function that sets the interval.

57
00:04:11,140 --> 00:04:12,640
For getting the updated.

58
00:04:13,670 --> 00:04:16,200
Dht22 sensor values.

59
00:04:18,080 --> 00:04:22,520
And write function start date sensor interval.

60
00:04:26,590 --> 00:04:29,260
And then here we'll use set interval.

61
00:04:31,230 --> 00:04:37,440
And pass the get DHT sensor values function name and we'll call it every five seconds.

62
00:04:41,390 --> 00:04:43,070
Now let's copy this function.

63
00:04:44,340 --> 00:04:48,690
And let's go up to the Document.ready function and paste it right there.

64
00:04:49,630 --> 00:04:50,620
Okay, cool.

65
00:04:51,510 --> 00:04:54,630
So next, let's go over to the Http server dot c.

66
00:04:56,770 --> 00:05:02,260
And first here we want to include the dht22 dot h file.

67
00:05:03,370 --> 00:05:06,310
And now we could go down to register the handler.

68
00:05:13,180 --> 00:05:18,880
And right here we'll say register DBT sensor dot Json handler.

69
00:05:23,470 --> 00:05:26,830
And now I'll go to App.js just to make sure I have the right name.

70
00:05:28,270 --> 00:05:29,440
Okay, good.

71
00:05:29,440 --> 00:05:30,460
So let's go back.

72
00:05:33,270 --> 00:05:34,620
And create the handler.

73
00:05:37,700 --> 00:05:40,600
For the DHT sensor Json.

74
00:05:43,180 --> 00:05:43,390
Okay.

75
00:05:43,390 --> 00:05:48,550
And here the Uri is forward slash DHT sensor Json.

76
00:05:50,810 --> 00:05:53,720
In the method is http get.

77
00:05:56,310 --> 00:05:57,360
And the handler.

78
00:05:59,860 --> 00:06:05,230
We can call Http server, get Dhcp sensor readings.

79
00:06:07,450 --> 00:06:08,830
Jason Handler.

80
00:06:10,630 --> 00:06:12,610
End user ctcss is null.

81
00:06:17,330 --> 00:06:17,630
Then.

82
00:06:17,630 --> 00:06:19,280
Now let's register the handler.

83
00:06:23,650 --> 00:06:29,830
And pass the Http server handle and a reference to the DHT sensor json struct.

84
00:06:32,260 --> 00:06:34,660
All right, so now let's go and define this handler.

85
00:06:34,660 --> 00:06:35,770
So copy it.

86
00:06:40,160 --> 00:06:42,260
And here we'll say.

87
00:06:43,300 --> 00:06:45,460
DHT sensor readings.

88
00:06:46,440 --> 00:06:52,290
Jason Handler responds with Dht22 sensor data.

89
00:06:55,630 --> 00:06:59,530
And for the parameter and the return, let's just copy from up here.

90
00:07:00,170 --> 00:07:01,610
And then just paste it.

91
00:07:06,900 --> 00:07:08,970
Okay, then let's just grab the name again.

92
00:07:13,590 --> 00:07:21,720
And now we can say static esp error type and our handler name and it takes the http request type.

93
00:07:23,440 --> 00:07:24,760
Pointer rk.

94
00:07:26,580 --> 00:07:27,180
Next week.

95
00:07:27,180 --> 00:07:28,800
An ESP log.info.

96
00:07:30,760 --> 00:07:35,200
That DHT sensor Dodgson requested.

97
00:07:37,330 --> 00:07:40,870
And then we need a care DHT sensor Json buffer.

98
00:07:44,240 --> 00:07:45,650
Of 100 bytes.

99
00:07:46,260 --> 00:07:47,490
That should be enough.

100
00:07:47,760 --> 00:07:52,530
And then we can now sprint into the DHT sensor Json buffer.

101
00:07:54,070 --> 00:07:56,810
Then we can do the escape sequence here for the Json.

102
00:07:56,810 --> 00:07:58,520
So just follow what I do now.

103
00:08:00,830 --> 00:08:02,480
So first for the temp.

104
00:08:04,960 --> 00:08:06,730
To one decimal place.

105
00:08:08,900 --> 00:08:10,490
And next to the humidity.

106
00:08:14,700 --> 00:08:17,250
And that is also to one decimal place.

107
00:08:20,280 --> 00:08:23,760
And now we can close it and call get temperature.

108
00:08:26,500 --> 00:08:28,150
And also get humidity.

109
00:08:31,290 --> 00:08:33,180
Then let's set the response type.

110
00:08:38,500 --> 00:08:43,240
For the request and its application slash Json.

111
00:08:47,900 --> 00:08:49,460
Then send the response.

112
00:08:53,600 --> 00:08:54,770
For the request.

113
00:08:55,440 --> 00:08:57,780
And DHT sensor Json.

114
00:08:58,740 --> 00:09:02,360
And strlen of the DHT sensor Json.

115
00:09:05,390 --> 00:09:06,900
Then return esp.

116
00:09:06,950 --> 00:09:07,290
Okay.

117
00:09:12,730 --> 00:09:13,010
Okay.

118
00:09:13,010 --> 00:09:13,560
It looks good.

119
00:09:13,570 --> 00:09:14,710
Now let's build.

120
00:09:26,830 --> 00:09:27,140
Okay.

121
00:09:27,280 --> 00:09:27,810
Where is here?

122
00:09:27,820 --> 00:09:29,080
So then let's flesh.

123
00:09:32,160 --> 00:09:33,570
And don't worry about this.

124
00:09:33,570 --> 00:09:38,070
There's a problem recognizing ESP log and there's a fix for this that I'll provide to you.

125
00:09:38,670 --> 00:09:40,650
Okay, so let's just proceed.

126
00:09:55,970 --> 00:09:56,270
Okay.

127
00:09:56,270 --> 00:09:56,780
We're flesh.

128
00:09:56,780 --> 00:09:58,250
So now let's open the monitor.

129
00:10:05,240 --> 00:10:06,620
And now connect to the ESP.

130
00:10:17,040 --> 00:10:21,240
Let's now use Google Chrome and then navigate to the ISPs IP.

131
00:10:26,610 --> 00:10:29,760
And give the JavaScript functions a moment to be invoked.

132
00:10:29,790 --> 00:10:30,930
And there you have it.

133
00:10:30,960 --> 00:10:34,190
We have dht22 sensor data displayed on the web page.

134
00:10:34,200 --> 00:10:34,980
Excellent.

135
00:10:35,220 --> 00:10:40,680
And the data is updated on the page at the interval that we specified in App.js.

136
00:10:41,590 --> 00:10:41,980
All right.

137
00:10:41,980 --> 00:10:45,640
So we can see our handler requested and the DHT sensor readings.

138
00:10:45,640 --> 00:10:46,390
Perfect.

139
00:10:47,710 --> 00:10:53,260
So now let's comment out these print F's because we no longer need them now that the Web page shows

140
00:10:53,260 --> 00:10:54,230
the data there.

141
00:10:54,250 --> 00:10:55,600
So let's get rid of that.

142
00:10:59,410 --> 00:11:03,190
And in the next section, we'll talk about connecting and disconnecting Wi-Fi.

143
00:11:03,640 --> 00:11:04,000
All right.

144
00:11:04,000 --> 00:11:05,050
So see you there.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: WiFi Connect Implementation



1
00:00:06,970 --> 00:00:07,880
Hey, welcome back.

2
00:00:07,900 --> 00:00:12,850
In this section, I'll give a brief overview of how we're going to connect the ESP 32 to an access point

3
00:00:12,850 --> 00:00:14,020
via the web page.

4
00:00:16,150 --> 00:00:19,030
So let's jump right into discussing our implementation.

5
00:00:19,930 --> 00:00:24,430
We'll create text fields in the web page where we can enter the credentials of the access point that

6
00:00:24,430 --> 00:00:29,260
we want to connect to and the connect button to trigger the action to connect on the server side.

7
00:00:29,380 --> 00:00:34,900
The web server will handle receiving the credentials we've entered, updating the Wi-Fi configuration

8
00:00:34,900 --> 00:00:36,850
and then attempt the connection.

9
00:00:37,060 --> 00:00:42,100
And our application will let the user know the connection status by displaying the connection result

10
00:00:42,100 --> 00:00:45,160
on the web page, whether it was successful or not.

11
00:00:45,430 --> 00:00:49,230
Additionally, we'll display the connection details on the web page.

12
00:00:49,240 --> 00:00:56,590
The access point name that the ESP 32 is connected to and the IP information assigned to the ESP 32.

13
00:00:56,800 --> 00:01:02,590
Furthermore, we'll implement a disconnect button that the user can use to disconnect Wi-Fi via the

14
00:01:02,590 --> 00:01:03,530
web page.

15
00:01:03,550 --> 00:01:10,630
And lastly, we'll use our RGB led to indicate the connection status when the ESP 32 is connected to

16
00:01:10,630 --> 00:01:11,860
another access point.

17
00:01:13,950 --> 00:01:14,250
All right.

18
00:01:14,250 --> 00:01:18,720
So let's take a look at some of the Espressif APIs we'll use in this section.

19
00:01:19,230 --> 00:01:19,500
Okay.

20
00:01:19,500 --> 00:01:24,900
So once the Connect button is pressed on the Web page side, our Uri handler for receiving credentials

21
00:01:24,900 --> 00:01:30,210
will be triggered and the Http request get header value length function will be invoked.

22
00:01:30,240 --> 00:01:36,360
This function returns the length if the field is found in the request URL or zero if the field is not

23
00:01:36,360 --> 00:01:38,490
found or it's an invalid request.

24
00:01:38,760 --> 00:01:46,230
Next, the Http request get header value string function is used which gets values from the text fields.

25
00:01:46,470 --> 00:01:52,680
After that, we'll need to update the Wi-Fi configuration and will update the data in the Wi-Fi config

26
00:01:52,680 --> 00:01:53,420
structure.

27
00:01:53,430 --> 00:01:58,830
In this case, we'll need to update the station details because this pertains to the ESP acting as a

28
00:01:58,830 --> 00:02:00,650
station connected to another AP.

29
00:02:01,020 --> 00:02:07,200
In our case, we'll need to update the Ssid and password of the access point that we're connecting to.

30
00:02:07,560 --> 00:02:14,190
Then we will set the configuration using the ESP Wi-Fi set configuration function.

31
00:02:14,190 --> 00:02:20,970
And again, in this case the ESP is acting as a station because it's connecting to another access point.

32
00:02:21,000 --> 00:02:26,130
So we'll specify the ESP interface Wi-Fi station when doing this.

33
00:02:26,400 --> 00:02:34,290
Then we'll need to call the ESP Wi-Fi Connect to attempt the connection which connects the ESP 32 station

34
00:02:34,290 --> 00:02:40,140
to an access point using the Ssid and password we've set the configuration for.

35
00:02:40,320 --> 00:02:43,610
And later we'll implement the disconnect button.

36
00:02:43,620 --> 00:02:47,790
In this case, we'll use the ESP Wi-Fi disconnect function.

37
00:02:47,910 --> 00:02:52,830
This function will disconnect the ESP from an access point that it's connected to.

38
00:02:54,300 --> 00:02:59,290
In upcoming programming sections, we'll get the ID for display on the Web page.

39
00:02:59,310 --> 00:03:05,370
We'll take the Wi-Fi access point record structure, which holds the description of the Wi-Fi app and

40
00:03:05,370 --> 00:03:07,890
pass it to the ESP Wi-Fi station.

41
00:03:07,890 --> 00:03:12,870
Get access point information function to get the ID of the connected app.

42
00:03:13,560 --> 00:03:20,160
We'll also get the IP connection information by using an instance of the ESP network interface, IP

43
00:03:20,190 --> 00:03:24,560
info structure and passing it to the ESP network interface.

44
00:03:24,570 --> 00:03:26,580
Get IP info function.

45
00:03:26,670 --> 00:03:33,450
The IP Gateway and Netmask information obtained from this function will be in numeric form and will

46
00:03:33,450 --> 00:03:36,060
need to be converted to dotted decimal Ascii.

47
00:03:36,360 --> 00:03:45,060
And we will do that by using the ESP IPv4 address intoa function which again converts the IP address

48
00:03:45,060 --> 00:03:46,950
into dotted decimal Ascii.

49
00:03:47,160 --> 00:03:52,830
And at this point we'll have the strings that we need after using ESP printf and we'll send the response

50
00:03:52,830 --> 00:03:56,050
to the web page using httpd response send.

51
00:03:56,080 --> 00:03:58,780
As we have been doing in our Uri handlers.

52
00:04:00,300 --> 00:04:07,410
So just to refresh, the ESP 32 will be an access point slash station mode, an access point in that

53
00:04:07,410 --> 00:04:12,840
other devices can connect to it and a station and that it will be connected to another access point.

54
00:04:13,870 --> 00:04:15,620
So that's all for the background info.

55
00:04:15,640 --> 00:04:16,720
Let's get started.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


1
00:00:06,940 --> 00:00:11,380
In order to connect wi fi via the web page, we need to make a few updates to index.html.

2
00:00:11,500 --> 00:00:13,420
So let's create a new section here.

3
00:00:14,870 --> 00:00:16,580
And here let's create a div.

4
00:00:17,970 --> 00:00:20,370
And call it wi fi connect.

5
00:00:22,990 --> 00:00:24,520
Then create an H to.

6
00:00:25,650 --> 00:00:28,800
That says ESP 32 Wi-Fi Connect.

7
00:00:30,210 --> 00:00:31,620
And close the to.

8
00:00:33,830 --> 00:00:35,300
Then let's make a section.

9
00:00:37,610 --> 00:00:38,690
And copy it.

10
00:00:39,360 --> 00:00:41,040
So we can close the section.

11
00:00:45,250 --> 00:00:55,270
And within the section right input ID equals connect, underscore id and specify the type as text.

12
00:00:56,450 --> 00:00:57,890
And the max length.

13
00:00:58,600 --> 00:00:59,770
As 32.

14
00:01:00,850 --> 00:01:03,520
And the placeholder that says CID.

15
00:01:05,570 --> 00:01:07,730
And the value can be blank.

16
00:01:10,820 --> 00:01:11,900
Now, let's copy that.

17
00:01:13,370 --> 00:01:16,250
And paste below for the password information.

18
00:01:17,840 --> 00:01:19,940
Change the input ID to pass.

19
00:01:20,710 --> 00:01:22,720
And the type as password.

20
00:01:23,800 --> 00:01:26,020
And the max length should be 64.

21
00:01:26,810 --> 00:01:29,030
And placeholder as password.

22
00:01:31,410 --> 00:01:35,850
All right, now let's do input type for a checkbox.

23
00:01:40,710 --> 00:01:42,990
Which on click shows the password.

24
00:01:42,990 --> 00:01:48,540
So let's specify a function here by saying on click show password.

25
00:01:50,420 --> 00:01:51,320
Function.

26
00:01:51,650 --> 00:01:57,020
And now on the Web page, let's write here some text that says show password.

27
00:02:00,390 --> 00:02:03,450
Next, let's use our div class for buttons.

28
00:02:08,440 --> 00:02:10,540
And first, let's close this div.

29
00:02:14,090 --> 00:02:16,580
And within here we'll have an input ID.

30
00:02:18,860 --> 00:02:20,470
For connect Wi-Fi.

31
00:02:22,250 --> 00:02:24,230
And this type will be button.

32
00:02:25,940 --> 00:02:28,340
And the value will say connect.

33
00:02:31,490 --> 00:02:33,530
Then do a div ID for.

34
00:02:34,350 --> 00:02:37,040
Wi-Fi Connect Credentials.

35
00:02:37,050 --> 00:02:37,770
Errors.

36
00:02:42,040 --> 00:02:43,540
Then make an H for.

37
00:02:45,840 --> 00:02:48,150
For Wi-Fi Connect status.

38
00:02:52,880 --> 00:02:56,300
All right, now we can close our wi fi connect div.

39
00:02:57,750 --> 00:02:59,250
And let's fix that.

40
00:03:00,960 --> 00:03:02,250
And now that looks okay.

41
00:03:02,640 --> 00:03:06,420
All right, so now we can go to Apks and add the styling.

42
00:03:07,290 --> 00:03:09,570
And now we want some red and green lettering.

43
00:03:09,570 --> 00:03:10,920
So let's come right here.

44
00:03:12,250 --> 00:03:12,940
And say.

45
00:03:16,640 --> 00:03:17,480
And right.

46
00:03:18,100 --> 00:03:18,790
Color.

47
00:03:19,120 --> 00:03:20,650
Colon, green.

48
00:03:23,150 --> 00:03:25,460
Okay, next, let's do one for red.

49
00:03:27,400 --> 00:03:29,800
And say color, colon, red.

50
00:03:33,060 --> 00:03:33,950
And that's it.

51
00:03:33,960 --> 00:03:36,330
So now we can go over to App.js.

52
00:03:37,050 --> 00:03:39,480
And first, let's set up our onClick function.

53
00:03:40,050 --> 00:03:41,670
And here, just follow me.

54
00:03:41,940 --> 00:03:48,600
And that's for our connect underscore wi fi and then say dot onClick.

55
00:03:50,630 --> 00:03:52,370
Comma function.

56
00:03:53,110 --> 00:03:56,530
And open the curly braces and its checked credentials.

57
00:03:59,410 --> 00:04:01,180
And now close it with the semicolon.

58
00:04:02,040 --> 00:04:04,380
Okay, so now let's go down to the bottom of the file.

59
00:04:05,100 --> 00:04:06,960
And let's create a function here.

60
00:04:08,160 --> 00:04:10,620
Which clears the connection status interval.

61
00:04:13,470 --> 00:04:14,760
And say function.

62
00:04:15,640 --> 00:04:18,250
Stop Wi-Fi Connect Status interval.

63
00:04:21,770 --> 00:04:24,450
And let's not define it yet because we need a few more.

64
00:04:24,470 --> 00:04:26,330
So let's create another function below it.

65
00:04:28,830 --> 00:04:32,220
And this one gets the wi fi connection status.

66
00:04:34,390 --> 00:04:35,770
So say function.

67
00:04:36,680 --> 00:04:38,870
Get wi fi connect status.

68
00:04:42,410 --> 00:04:43,670
And let's create another.

69
00:04:45,030 --> 00:04:46,800
And this one starts the interval.

70
00:04:47,590 --> 00:04:49,600
For checking the connection status.

71
00:04:51,940 --> 00:04:53,200
And its function.

72
00:04:54,010 --> 00:04:56,710
Start Wi-Fi Connect Status interval.

73
00:05:02,580 --> 00:05:03,780
Now let's do another.

74
00:05:05,310 --> 00:05:06,510
Let's right here.

75
00:05:06,750 --> 00:05:08,520
Connect wi fi function.

76
00:05:11,120 --> 00:05:14,930
Called using the Ssid and password.

77
00:05:15,560 --> 00:05:17,540
Entered into the text fields.

78
00:05:20,560 --> 00:05:23,510
And that's function connect Wi-Fi.

79
00:05:28,050 --> 00:05:28,830
Next.

80
00:05:28,830 --> 00:05:30,300
Let's do the last one.

81
00:05:32,220 --> 00:05:34,620
And this one checks credentials.

82
00:05:35,810 --> 00:05:37,340
On Connect Wi-Fi.

83
00:05:38,110 --> 00:05:38,650
Button.

84
00:05:38,650 --> 00:05:39,220
Click.

85
00:05:41,750 --> 00:05:44,630
And that's a function check credentials.

86
00:05:48,060 --> 00:05:51,330
Okay, now let's define this one and then work our way up the file.

87
00:05:51,360 --> 00:05:53,940
So first, let's say error list.

88
00:05:55,250 --> 00:05:57,440
Equals and leave it blank.

89
00:05:58,030 --> 00:05:59,430
Then let's write creeds.

90
00:05:59,440 --> 00:06:00,180
Okay.

91
00:06:00,190 --> 00:06:01,570
And set it to true.

92
00:06:02,730 --> 00:06:08,760
And now selected sed equals and just follow what I do here.

93
00:06:08,760 --> 00:06:13,140
It's dollar sign from the connect sed.

94
00:06:14,080 --> 00:06:15,430
Dot value.

95
00:06:15,790 --> 00:06:16,570
Okay.

96
00:06:16,570 --> 00:06:24,640
So we want the value from that element and then say password equals the connect pass element value.

97
00:06:31,620 --> 00:06:34,650
Now let's write if selected.

98
00:06:34,740 --> 00:06:35,370
Sid.

99
00:06:36,800 --> 00:06:38,060
Is blank.

100
00:06:39,690 --> 00:06:41,760
Then we'll set the error list.

101
00:06:45,340 --> 00:06:47,200
And just follow what I do here.

102
00:06:47,770 --> 00:06:49,240
It's an H for.

103
00:06:50,740 --> 00:06:56,530
And let's use our red color and then say CID cannot be empty.

104
00:06:59,330 --> 00:07:00,620
And then close it.

105
00:07:04,500 --> 00:07:05,850
Then creds.

106
00:07:05,850 --> 00:07:06,540
Okay.

107
00:07:06,720 --> 00:07:08,130
Equals false.

108
00:07:10,620 --> 00:07:12,510
Now copy this block of code.

109
00:07:14,070 --> 00:07:17,550
And then let's paste it and then write password here.

110
00:07:18,600 --> 00:07:19,920
And password here.

111
00:07:23,910 --> 00:07:27,000
Then say if Creed's okay.

112
00:07:27,240 --> 00:07:28,710
Equals false.

113
00:07:30,450 --> 00:07:33,660
Then we want the wi fi connect credentials.

114
00:07:33,690 --> 00:07:34,470
Errors.

115
00:07:40,100 --> 00:07:43,250
We want the credentials errors to display the error list.

116
00:07:47,400 --> 00:07:49,110
All right, so now let's copy this.

117
00:07:50,070 --> 00:07:51,480
And then right else.

118
00:07:53,340 --> 00:07:56,130
The credentials errors are blank.

119
00:07:58,980 --> 00:08:01,980
And then we can call the connect Wi-Fi function.

120
00:08:06,390 --> 00:08:11,100
Okay, so to recap, this function only checks if the Ssid and password are empty.

121
00:08:11,190 --> 00:08:14,160
And if they are, we display some error messages.

122
00:08:14,160 --> 00:08:16,980
And if not, it calls the connect Wi-Fi function.

123
00:08:17,010 --> 00:08:22,890
Also, we're already enforcing the maximum length in the index.html for the text fields so we don't

124
00:08:22,890 --> 00:08:24,270
have to check for that here.

125
00:08:24,690 --> 00:08:26,670
Now let's go to connect Wi-Fi.

126
00:08:27,480 --> 00:08:30,300
And say get the Ssid and password.

127
00:08:32,100 --> 00:08:33,930
And then selected side.

128
00:08:35,230 --> 00:08:38,350
Equals the value from Kinect side.

129
00:08:44,220 --> 00:08:45,480
And then password.

130
00:08:46,570 --> 00:08:48,970
Is the value from Connect Pass.

131
00:08:55,740 --> 00:08:59,100
And now just follow me and we'll use Ajax here.

132
00:09:02,480 --> 00:09:02,960
Okay.

133
00:09:02,960 --> 00:09:03,260
And the.

134
00:09:05,620 --> 00:09:08,080
Is forward slash wi fi connect.

135
00:09:11,660 --> 00:09:13,010
And the data type.

136
00:09:14,880 --> 00:09:15,960
Is Jason.

137
00:09:17,170 --> 00:09:19,120
And the method is post.

138
00:09:22,180 --> 00:09:24,970
And cash set it to false.

139
00:09:25,970 --> 00:09:27,260
And the headers.

140
00:09:29,350 --> 00:09:32,590
Are called my Connect Sid.

141
00:09:34,610 --> 00:09:37,460
From selected side.

142
00:09:39,340 --> 00:09:40,570
And the password?

143
00:09:40,570 --> 00:09:42,760
You can call my connect password.

144
00:09:44,710 --> 00:09:46,150
From food.

145
00:09:47,800 --> 00:09:48,910
And data.

146
00:09:50,980 --> 00:09:52,090
Timestamp.

147
00:09:53,610 --> 00:09:55,770
Is date.now.

148
00:09:57,590 --> 00:09:59,630
All right, then close that with the semicolon.

149
00:10:00,110 --> 00:10:03,920
And then now we can call start Wi-Fi Connect status interval.

150
00:10:12,410 --> 00:10:17,000
Okay, so connect wi fi calls, start wi fi connect status interval.

151
00:10:17,150 --> 00:10:19,630
So let's go define that now just above.

152
00:10:19,640 --> 00:10:27,320
But first, let's go to the top of the file and let's create a variable to hold the wi fi connect interval.

153
00:10:29,330 --> 00:10:30,680
And set it to null.

154
00:10:33,140 --> 00:10:36,260
All right, so now let's copy that and let's go back.

155
00:10:42,600 --> 00:10:48,510
And in the function, let's say wi fi connect interval equals set interval.

156
00:10:49,180 --> 00:10:52,090
And pass the get Wi-Fi connect status.

157
00:10:53,740 --> 00:10:56,890
And let's call it every 2.8 seconds.

158
00:10:59,990 --> 00:11:05,800
Okay, So here we're saying call the get Wi-Fi connect status function every 2.8 seconds.

159
00:11:05,810 --> 00:11:09,290
So next, let's go to get Wi-Fi Connect status.

160
00:11:09,290 --> 00:11:15,470
And let's say var XR equals new XML http request.

161
00:11:18,000 --> 00:11:20,820
And then var request URL.

162
00:11:22,300 --> 00:11:25,960
Equals forward slash wi fi connect status.

163
00:11:29,350 --> 00:11:33,940
And then let's XR open post.

164
00:11:35,910 --> 00:11:38,460
Then say request you are well.

165
00:11:39,140 --> 00:11:40,370
And false.

166
00:11:41,390 --> 00:11:43,880
And now let's xhr send.

167
00:11:44,770 --> 00:11:46,690
WI fi connect status.

168
00:11:50,360 --> 00:11:54,470
And then write if x dot ready state.

169
00:11:57,060 --> 00:11:57,990
Is for.

170
00:11:58,690 --> 00:12:03,550
Meaning that it's been sent and ZR status is 200.

171
00:12:07,210 --> 00:12:09,010
Meaning that it's okay.

172
00:12:10,270 --> 00:12:19,570
Then let's say var response equals Json.parse parentheses xhr dot response text.

173
00:12:21,640 --> 00:12:25,870
And now we can document dot get element by ID.

174
00:12:27,340 --> 00:12:29,530
For wi fi connect status.

175
00:12:33,010 --> 00:12:34,660
Dot inner HTML.

176
00:12:35,950 --> 00:12:37,780
Equals connecting.

177
00:12:40,830 --> 00:12:45,540
And then write if response dot Wi-Fi connect status.

178
00:12:51,770 --> 00:12:52,730
Is to.

179
00:12:54,630 --> 00:12:57,840
Then we'll say document get element by ID.

180
00:13:00,680 --> 00:13:02,660
Wi-Fi connect status.

181
00:13:05,600 --> 00:13:09,530
Dot inner HTML equals.

182
00:13:09,530 --> 00:13:12,500
And then we'll write a message in red.

183
00:13:18,120 --> 00:13:20,400
That says failed to connect.

184
00:13:21,610 --> 00:13:25,120
Please check your AP credentials and compatibility.

185
00:13:37,430 --> 00:13:39,280
Okay, then stop.

186
00:13:39,290 --> 00:13:41,270
Wi-Fi Connect Status interval.

187
00:13:45,100 --> 00:13:46,990
All right, now, copy this.

188
00:13:48,370 --> 00:13:53,560
And let's say else if response dot Wi-Fi Connect status.

189
00:13:58,470 --> 00:13:59,550
Is three.

190
00:14:01,910 --> 00:14:03,680
Then let's paste below.

191
00:14:10,120 --> 00:14:11,980
And now change this to green.

192
00:14:15,860 --> 00:14:17,720
And change the message to.

193
00:14:18,280 --> 00:14:19,090
Connections.

194
00:14:19,090 --> 00:14:20,020
Success.

195
00:14:26,170 --> 00:14:26,680
All right.

196
00:14:26,680 --> 00:14:31,150
So here in this function, we are checking the status response on the Web server side.

197
00:14:31,150 --> 00:14:36,820
And depending on that response, we write a message to the user and stop the connection status interval

198
00:14:37,150 --> 00:14:40,480
and we'll create those responses in the Web server later.

199
00:14:42,120 --> 00:14:48,990
Okay, so now let's go to Stop Wi-Fi Connect status interval and we'll say if Wi-Fi connect interval.

200
00:14:52,510 --> 00:14:53,740
Is not null.

201
00:14:56,170 --> 00:14:58,240
Then we will use clear interval.

202
00:15:00,540 --> 00:15:02,430
For the interval variable.

203
00:15:07,950 --> 00:15:10,650
And we will set this variable here.

204
00:15:13,180 --> 00:15:14,440
We'll set it to null.

205
00:15:17,170 --> 00:15:17,610
Okay.

206
00:15:17,620 --> 00:15:18,640
Just like that.

207
00:15:18,850 --> 00:15:21,910
And lastly, let's define the show password function.

208
00:15:25,610 --> 00:15:28,940
And that one shows the Wi-Fi password.

209
00:15:30,160 --> 00:15:31,660
If the box is checked.

210
00:15:35,110 --> 00:15:37,720
And it's a function show password.

211
00:15:41,300 --> 00:15:44,660
And write var x equals document.

212
00:15:44,660 --> 00:15:46,100
Get element by ID.

213
00:15:49,400 --> 00:15:50,000
Connect.

214
00:15:50,000 --> 00:15:51,350
Underscore, pass.

215
00:15:54,360 --> 00:15:56,910
And then say if X type.

216
00:15:59,110 --> 00:16:00,550
Is password.

217
00:16:04,750 --> 00:16:08,440
Then x type equals text.

218
00:16:10,940 --> 00:16:12,160
Then say else.

219
00:16:13,420 --> 00:16:16,780
X type equals password.

220
00:16:18,960 --> 00:16:19,830
That's it.

221
00:16:19,830 --> 00:16:22,200
So if the box is checked, we show the password.

222
00:16:22,200 --> 00:16:23,640
Otherwise we don't show it.

223
00:16:23,910 --> 00:16:27,360
Okay, so I have one mistake up here, so let's fix that.

224
00:16:27,360 --> 00:16:29,340
This should be innerhtml.

225
00:16:33,880 --> 00:16:34,210
All right.

226
00:16:34,210 --> 00:16:36,520
So be sure that you don't have any errors here either.

227
00:16:36,520 --> 00:16:39,100
And in the next lesson, we'll program the Web server.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,020 --> 00:00:12,930
So let's pick up where we left off, because next we need to define the handlers for the Wi-Fi connect

2
00:00:12,930 --> 00:00:16,440
Json as well as the Wi-Fi Connect status.

3
00:00:17,840 --> 00:00:19,760
And we'll do that in the Http server.

4
00:00:19,760 --> 00:00:21,290
So let's go to the C file.

5
00:00:22,280 --> 00:00:27,590
And just as a refresher, we have our Wi-Fi connect status messages.

6
00:00:27,620 --> 00:00:30,560
We go from initialize to success to fail.

7
00:00:30,710 --> 00:00:31,370
All right.

8
00:00:31,370 --> 00:00:31,910
Here.

9
00:00:32,060 --> 00:00:32,750
Okay.

10
00:00:32,900 --> 00:00:39,380
And since we need to deal with the Wi-Fi configuration within the Web server and within the Wi-Fi application,

11
00:00:39,380 --> 00:00:42,080
we need a way to pass the Wi-Fi configuration around.

12
00:00:42,080 --> 00:00:44,840
So let's go to the Wi-Fi APK file.

13
00:00:46,210 --> 00:00:47,770
And let's handle that here.

14
00:00:48,130 --> 00:00:51,490
So at the top of the file, let's say.

15
00:00:53,350 --> 00:00:56,230
Used for returning the wi fi configuration.

16
00:00:59,500 --> 00:01:02,170
And it's a wi fi config type.

17
00:01:02,790 --> 00:01:08,430
And we need a pointer and call it wi fi config and set it to null.

18
00:01:10,530 --> 00:01:12,540
Next, let's say.

19
00:01:14,360 --> 00:01:16,790
Used to track the number of retries.

20
00:01:18,830 --> 00:01:20,780
When a connection attempt fails.

21
00:01:24,900 --> 00:01:26,910
And that's a static int.

22
00:01:27,150 --> 00:01:29,220
Global retry number.

23
00:01:32,030 --> 00:01:37,490
And next, let's allocate memory for the Wi-Fi config and we'll do that in the start function.

24
00:01:40,410 --> 00:01:43,920
And here, let's say, allocate memory.

25
00:01:45,440 --> 00:01:47,300
For the Fi configuration.

26
00:01:50,860 --> 00:01:52,750
And it's wifi config.

27
00:01:53,230 --> 00:01:55,420
Equals wi fi config.

28
00:01:55,750 --> 00:02:01,990
Typecast pointer and malloc the size of the wi fi config structure.

29
00:02:09,050 --> 00:02:10,670
Then we'll set.

30
00:02:12,010 --> 00:02:13,480
The wi fi config.

31
00:02:14,430 --> 00:02:18,630
Two zero for the size of the wi fi config.

32
00:02:23,410 --> 00:02:27,010
Okay, Next, let's define a function that returns this wi fi config.

33
00:02:27,220 --> 00:02:29,200
So now we'll go to the header file.

34
00:02:31,680 --> 00:02:33,030
And here we'll say.

35
00:02:34,430 --> 00:02:36,500
Gets the wi fi configuration.

36
00:02:39,770 --> 00:02:42,440
And it returns the wi fi config type.

37
00:02:43,200 --> 00:02:46,140
Pointer and call it wi fi app.

38
00:02:46,470 --> 00:02:48,180
Get wi fi config.

39
00:02:49,430 --> 00:02:50,450
And it's void.

40
00:02:53,370 --> 00:02:54,750
So copy that.

41
00:02:55,540 --> 00:02:57,190
And go to the C file.

42
00:02:59,380 --> 00:03:00,730
And drop it here.

43
00:03:01,510 --> 00:03:04,600
And simply say return wi fi config.

44
00:03:09,160 --> 00:03:12,100
Next, let's go to the http server header file.

45
00:03:14,570 --> 00:03:15,800
And comment here.

46
00:03:17,350 --> 00:03:19,520
Connection statuses for Wi-Fi.

47
00:03:23,690 --> 00:03:26,480
And that can be a typedef enum.

48
00:03:27,370 --> 00:03:28,780
Http server.

49
00:03:28,820 --> 00:03:30,790
Wi-Fi Connect Status.

50
00:03:37,030 --> 00:03:38,500
The first one can be none.

51
00:03:38,500 --> 00:03:40,750
And let's explicitly set it to zero.

52
00:03:40,780 --> 00:03:44,110
Then http Wi-Fi status connecting.

53
00:03:46,490 --> 00:03:49,820
And also Http Wi-Fi status.

54
00:03:51,240 --> 00:03:52,320
Connect failed.

55
00:03:55,000 --> 00:03:59,560
And http wi fi status connect success.

56
00:04:03,610 --> 00:04:04,960
And let's name it.

57
00:04:05,680 --> 00:04:06,970
With an underscore e.

58
00:04:09,550 --> 00:04:11,290
Now, let's go to the C file.

59
00:04:13,510 --> 00:04:15,640
And here let's create a global variable.

60
00:04:18,160 --> 00:04:21,400
And say wi fi connect status.

61
00:04:22,870 --> 00:04:27,280
And that is a static int global Wi-Fi connect status.

62
00:04:28,250 --> 00:04:29,510
And set it to none.

63
00:04:33,640 --> 00:04:35,560
Okay, now let's copy that variable.

64
00:04:37,750 --> 00:04:43,930
And in the monitor under connect in it set it to status connecting.

65
00:04:52,940 --> 00:04:54,170
And now copy it.

66
00:04:55,380 --> 00:05:01,260
And then under the success case, let's paste it and change it to connect success.

67
00:05:05,370 --> 00:05:07,470
All right and then now under connect failed.

68
00:05:08,180 --> 00:05:10,850
Let's change it to connect Failed.

69
00:05:14,530 --> 00:05:17,140
And now we can define our Uri handlers.

70
00:05:17,650 --> 00:05:18,850
So let's head down there.

71
00:05:25,540 --> 00:05:27,670
And here, let's copy this one.

72
00:05:33,150 --> 00:05:37,470
Let's use it to define our wi fi connect Json handler.

73
00:05:39,800 --> 00:05:42,270
And call it wi fi connect Json.

74
00:05:44,000 --> 00:05:47,750
And the Uri is wi fi connect Json.

75
00:05:51,280 --> 00:05:53,890
And the method is http post.

76
00:05:55,390 --> 00:06:00,520
And the handler we can call Http server Wi-Fi connect.

77
00:06:01,270 --> 00:06:02,410
Jason Handler.

78
00:06:04,620 --> 00:06:07,020
Next, let's pass the structure name.

79
00:06:08,510 --> 00:06:10,040
To register the handler.

80
00:06:10,460 --> 00:06:12,050
Okay, now let's copy this one.

81
00:06:15,470 --> 00:06:18,800
And now let's do the wi fi connect status handler.

82
00:06:21,310 --> 00:06:26,710
And call it wi fi connect status Json and the Uri is.

83
00:06:26,740 --> 00:06:28,330
WI fi connect status.

84
00:06:30,560 --> 00:06:33,860
And then change the handler to Wi-Fi Connect status.

85
00:06:35,120 --> 00:06:37,740
And now pass the name to register it.

86
00:06:41,660 --> 00:06:46,430
So now let's proceed by defining our Wi-Fi Connect Json handler.

87
00:06:54,310 --> 00:06:55,510
So now we'll write.

88
00:06:57,030 --> 00:07:00,120
Wi-Fi Connect Json handler.

89
00:07:01,250 --> 00:07:04,640
Is invoked after the Kinect button is pressed.

90
00:07:06,400 --> 00:07:10,420
And handles receiving the Ssid and password.

91
00:07:17,460 --> 00:07:18,840
Entered by the user.

92
00:07:20,280 --> 00:07:27,450
And the parameter RCX is the Http request for which the Uri needs to be handled.

93
00:07:30,190 --> 00:07:31,980
And return is ESP.

94
00:07:32,050 --> 00:07:32,410
Okay.

95
00:07:34,430 --> 00:07:41,900
And then it's a static ESP error type and it's our Wi-Fi connect handler and it takes an Http request

96
00:07:41,900 --> 00:07:43,670
type pointer req.

97
00:07:45,530 --> 00:07:47,570
So let's first log.

98
00:07:50,370 --> 00:07:53,160
That Wi-Fi connect Json requested.

99
00:08:01,000 --> 00:08:07,650
Now let's define some variables for the Ssid and password length received and say size underscore t

100
00:08:08,140 --> 00:08:14,050
Len ssid equals zero comma Len pass.

101
00:08:16,100 --> 00:08:17,990
And set that 1 to 0 as well.

102
00:08:19,470 --> 00:08:22,470
And next, we need care pointers to hold the strings.

103
00:08:22,470 --> 00:08:27,870
So here say care pointer side string equals null.

104
00:08:28,810 --> 00:08:32,590
Comma pass string and that's also null.

105
00:08:35,170 --> 00:08:35,380
All right.

106
00:08:35,380 --> 00:08:37,720
So next we'll say git side header.

107
00:08:40,510 --> 00:08:47,260
And it's Len id equals httpd request get header value length.

108
00:08:50,030 --> 00:08:53,990
For the request and from my Kinect side.

109
00:08:59,650 --> 00:09:01,840
Okay, now let's add one to the length.

110
00:09:07,930 --> 00:09:11,620
And then say if length.

111
00:09:13,150 --> 00:09:14,500
Is greater than one.

112
00:09:15,950 --> 00:09:18,260
Then our side string.

113
00:09:19,870 --> 00:09:23,410
Should be allocated memory for the length of the Sid.

114
00:09:26,390 --> 00:09:30,770
And then we'll say if Http request get header value string.

115
00:09:38,520 --> 00:09:42,660
For the request and the my connect Sid Field.

116
00:09:48,900 --> 00:09:50,790
For the side string.

117
00:09:52,750 --> 00:09:53,740
And sizes.

118
00:09:53,740 --> 00:09:55,030
Length of the side.

119
00:09:57,830 --> 00:09:59,300
And if that equals ESP.

120
00:09:59,360 --> 00:10:00,070
Okay.

121
00:10:01,670 --> 00:10:02,660
Then we'll log.

122
00:10:06,300 --> 00:10:07,710
From this handler.

123
00:10:10,720 --> 00:10:11,650
Found header.

124
00:10:12,720 --> 00:10:13,710
For my Kinect.

125
00:10:13,870 --> 00:10:14,430
Sid.

126
00:10:17,300 --> 00:10:20,000
And then pass the side string.

127
00:10:31,680 --> 00:10:31,980
All right.

128
00:10:31,980 --> 00:10:34,350
So we could do the same procedure for the password.

129
00:10:34,650 --> 00:10:36,300
So let's copy this.

130
00:10:38,420 --> 00:10:39,740
And then paste below.

131
00:10:39,860 --> 00:10:41,240
Change this to password.

132
00:10:42,790 --> 00:10:44,400
And change this to P.w.d..

133
00:10:47,660 --> 00:10:49,490
And then let's copy this header.

134
00:10:51,190 --> 00:10:53,290
I'm going to double check that this is all correct.

135
00:10:56,490 --> 00:10:57,030
Okay?

136
00:10:57,030 --> 00:10:57,690
Yes.

137
00:10:57,690 --> 00:10:58,680
Yes, it's the same.

138
00:10:58,680 --> 00:11:01,440
So we should be all good.

139
00:11:02,570 --> 00:11:03,710
Okay, let's go back.

140
00:11:05,800 --> 00:11:07,720
And change this to Len Pass.

141
00:11:10,260 --> 00:11:11,220
And.

142
00:11:12,010 --> 00:11:13,390
And this one as well.

143
00:11:14,630 --> 00:11:17,570
And then change this to pass string.

144
00:11:21,210 --> 00:11:21,690
Okay.

145
00:11:21,690 --> 00:11:23,280
And copy it and paste it here.

146
00:11:24,230 --> 00:11:25,220
And here.

147
00:11:27,140 --> 00:11:27,590
Okay.

148
00:11:27,620 --> 00:11:28,730
Did we do everything?

149
00:11:32,080 --> 00:11:33,730
Yes, that all looks good.

150
00:11:34,270 --> 00:11:34,930
Okay.

151
00:11:35,590 --> 00:11:36,760
And change this here.

152
00:11:41,610 --> 00:11:41,970
All right.

153
00:11:41,970 --> 00:11:45,630
So now let's update the Wi-Fi networks configuration.

154
00:11:50,640 --> 00:11:52,680
And let the Wi-Fi application know.

155
00:11:55,270 --> 00:11:57,940
Okay, we'll make a wi fi config type pointer.

156
00:11:58,300 --> 00:12:02,770
WI fi config equals the return of our wi fi app.

157
00:12:04,030 --> 00:12:05,980
Git wifi config function.

158
00:12:07,470 --> 00:12:08,010
All right then.

159
00:12:08,020 --> 00:12:10,500
Memset Wi-Fi config.

160
00:12:12,020 --> 00:12:13,060
Two zeros.

161
00:12:13,840 --> 00:12:16,270
For the size of wi fi config type.

162
00:12:20,670 --> 00:12:22,170
Then let's mem copy.

163
00:12:23,890 --> 00:12:25,750
Into the wi fi config.

164
00:12:27,060 --> 00:12:27,540
Stay.

165
00:12:28,890 --> 00:12:29,520
Sad.

166
00:12:32,040 --> 00:12:34,290
And that's from the side string.

167
00:12:35,540 --> 00:12:37,730
For the length of the side.

168
00:12:40,790 --> 00:12:42,350
And now let's copy that line.

169
00:12:43,610 --> 00:12:46,100
Paste below and we'll do the password.

170
00:12:48,750 --> 00:12:50,430
And this is past string.

171
00:12:51,890 --> 00:12:53,420
And this is Len Pesce.

172
00:12:58,460 --> 00:13:01,160
Now we can send the Wi-Fi app message.

173
00:13:04,850 --> 00:13:10,880
And the id is wi fi app message connecting from Http server.

174
00:13:13,880 --> 00:13:18,540
And now let's free the allocated memory for CID string.

175
00:13:19,670 --> 00:13:23,000
And also free for the password string.

176
00:13:27,430 --> 00:13:29,550
Now we can return ESP.

177
00:13:29,590 --> 00:13:30,220
Okay.

178
00:13:33,230 --> 00:13:35,420
And actually, there's one mistake here.

179
00:13:35,630 --> 00:13:37,220
This should be password.

180
00:13:37,940 --> 00:13:38,240
All right.

181
00:13:38,240 --> 00:13:39,080
So p.w.d..

182
00:13:40,220 --> 00:13:40,490
Okay.

183
00:13:40,490 --> 00:13:44,240
I think it's time for a short break and we're going to continue in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,250 --> 00:00:07,580
All right.

2
00:00:07,580 --> 00:00:13,040
So let's continue and let's grab this message and then let's head over to Wi-Fi apps.

3
00:00:14,420 --> 00:00:22,780
And then here under the connecting from Http server case, let's make a comment here and say attempt

4
00:00:22,790 --> 00:00:23,690
a connection.

5
00:00:25,150 --> 00:00:28,690
And then write Wi-Fi app connect to.

6
00:00:30,440 --> 00:00:32,600
And this function will define that later.

7
00:00:33,460 --> 00:00:33,700
All right.

8
00:00:33,730 --> 00:00:36,790
Now, let's say set current number of retries to zero.

9
00:00:40,500 --> 00:00:42,360
And the global reach by number.

10
00:00:43,530 --> 00:00:44,820
Just set it to zero.

11
00:00:46,100 --> 00:00:49,160
Okay, next let's let the Http server know.

12
00:00:50,800 --> 00:00:52,300
About the connection attempt.

13
00:00:54,750 --> 00:00:57,030
And then call Http server monitor.

14
00:00:57,030 --> 00:00:58,110
Send message.

15
00:01:02,590 --> 00:01:06,250
With a Http message Wi-Fi connect in it.

16
00:01:13,050 --> 00:01:16,110
And then next, let's define the Kinect star function.

17
00:01:20,250 --> 00:01:24,840
And now let's comment here connects the ESP 32.

18
00:01:25,660 --> 00:01:30,550
To an external access point using the updated station configuration.

19
00:01:34,030 --> 00:01:35,590
And it's a static void.

20
00:01:36,750 --> 00:01:40,200
Wi-Fi app Connect star and its void.

21
00:01:41,200 --> 00:01:43,360
Okay, now let's check.

22
00:01:46,010 --> 00:01:47,780
ESP wi fi config.

23
00:01:53,160 --> 00:01:56,260
And pass the ESP interface Wi-Fi star.

24
00:01:59,360 --> 00:02:03,620
And for the config we can call wifi app git wifi config.

25
00:02:09,140 --> 00:02:09,590
Next.

26
00:02:09,590 --> 00:02:11,180
Let's check.

27
00:02:12,530 --> 00:02:14,300
ESP wi fi connect.

28
00:02:18,030 --> 00:02:18,870
And that's all.

29
00:02:19,980 --> 00:02:22,200
All right, so now let's go to the event handler.

30
00:02:27,060 --> 00:02:29,820
And under the stay disconnected case.

31
00:02:30,730 --> 00:02:34,180
We're going to print some some disconnect error codes.

32
00:02:34,720 --> 00:02:38,140
So come here and let's use Wi-Fi event.

33
00:02:38,200 --> 00:02:40,120
Stay disconnected, type.

34
00:02:42,800 --> 00:02:45,820
And that's a pointer Wi-Fi event.

35
00:02:45,890 --> 00:02:47,300
Stay disconnected.

36
00:02:49,290 --> 00:02:52,570
And now let's type cast Wi-Fi event.

37
00:02:52,590 --> 00:02:54,150
Stay disconnected.

38
00:02:59,520 --> 00:03:03,960
And now memory allocate the size of Wi-Fi event.

39
00:03:04,050 --> 00:03:05,400
Stay disconnected.

40
00:03:10,390 --> 00:03:10,840
Okay.

41
00:03:10,840 --> 00:03:13,720
And then let's set the value that this points to.

42
00:03:15,700 --> 00:03:16,150
All right.

43
00:03:16,150 --> 00:03:17,770
And then just follow me here.

44
00:03:17,860 --> 00:03:21,370
It's the value, and we're typecasting.

45
00:03:25,870 --> 00:03:26,530
Right.

46
00:03:26,530 --> 00:03:29,740
And we want the we want the event data.

47
00:03:32,840 --> 00:03:33,200
All right.

48
00:03:33,200 --> 00:03:35,360
And now let's just print the information.

49
00:03:38,200 --> 00:03:39,640
Stay disconnected.

50
00:03:42,410 --> 00:03:43,730
Reason code.

51
00:03:46,010 --> 00:03:46,970
Goes here.

52
00:03:48,560 --> 00:03:49,750
And is from Wi-Fi.

53
00:03:50,270 --> 00:03:51,860
Stay disconnected.

54
00:03:52,960 --> 00:03:56,140
And let's access the reason like so.

55
00:03:58,500 --> 00:03:59,220
Okay.

56
00:04:00,720 --> 00:04:01,860
And then right.

57
00:04:01,890 --> 00:04:08,610
If global retry number is less than max connection retries.

58
00:04:09,970 --> 00:04:13,000
Then let's call ESP Wi-Fi connect again.

59
00:04:17,660 --> 00:04:18,320
Okay.

60
00:04:18,320 --> 00:04:21,170
And just increment the global retry number here.

61
00:04:28,750 --> 00:04:29,500
Else.

62
00:04:30,160 --> 00:04:32,740
We're going to send a disconnect message.

63
00:04:32,740 --> 00:04:34,330
So do wi fi app.

64
00:04:34,330 --> 00:04:35,500
Send message.

65
00:04:36,240 --> 00:04:39,540
WI fi app message Stay disconnected.

66
00:04:44,940 --> 00:04:48,120
So let's copy this message because it's not a message.

67
00:04:50,160 --> 00:04:51,970
And let's include it to our message.

68
00:04:55,280 --> 00:04:56,120
All right, that's it.

69
00:04:56,120 --> 00:04:57,350
So now let's go back.

70
00:04:59,480 --> 00:05:01,730
And now let's go on to the gut IP case.

71
00:05:02,680 --> 00:05:05,370
And now here we can send our IP message.

72
00:05:05,380 --> 00:05:08,290
So Wi-Fi app send message.

73
00:05:09,430 --> 00:05:11,020
WI fi app message.

74
00:05:11,080 --> 00:05:12,010
Stay connected.

75
00:05:12,290 --> 00:05:12,640
IP.

76
00:05:18,430 --> 00:05:21,070
Okay, now let's go down to the IP case.

77
00:05:27,230 --> 00:05:30,980
And here we need to send a message to the Http server monitor.

78
00:05:31,850 --> 00:05:34,580
So we'll say http server monitor.

79
00:05:36,280 --> 00:05:37,540
Send message.

80
00:05:38,640 --> 00:05:41,490
Http message Wi-Fi Connect Success.

81
00:05:49,070 --> 00:05:49,880
Okay, good.

82
00:05:52,660 --> 00:05:54,370
So now let's copy this case.

83
00:05:55,660 --> 00:05:57,400
And let's paste it just below.

84
00:05:58,870 --> 00:06:01,570
Let's define the stay disconnected case.

85
00:06:04,340 --> 00:06:06,410
So let's just log this message.

86
00:06:06,890 --> 00:06:08,990
Let's remove the RGB led.

87
00:06:09,020 --> 00:06:10,070
Function call.

88
00:06:13,120 --> 00:06:15,190
And then now let's send a fail message.

89
00:06:19,890 --> 00:06:21,960
So now let's briefly review.

90
00:06:22,710 --> 00:06:24,570
What's going on here in the handler?

91
00:06:25,600 --> 00:06:30,060
Okay, so if there's a disconnect, we'll retry for maximum retries.

92
00:06:30,070 --> 00:06:33,460
And once we reach the maximum, we send the disconnect message.

93
00:06:36,520 --> 00:06:39,550
Then we let the web server know about the connection.

94
00:06:39,550 --> 00:06:40,210
Failure.

95
00:06:41,580 --> 00:06:45,090
And in the web server when that happens.

96
00:06:49,230 --> 00:06:56,790
The global status variable is updated and it's also updated for the success case and in App.js.

97
00:06:57,850 --> 00:07:00,940
Our statuses reflect what happens on the web server side.

98
00:07:01,210 --> 00:07:03,460
Back to the user with the messages here.

99
00:07:06,710 --> 00:07:08,090
So let's continue.

100
00:07:11,580 --> 00:07:13,800
So now go to Http server.

101
00:07:15,130 --> 00:07:17,230
And let's go down to the handlers.

102
00:07:21,400 --> 00:07:24,160
And let's get the connect status Json handler.

103
00:07:24,750 --> 00:07:26,010
So we can define it.

104
00:07:27,010 --> 00:07:28,750
And first, let's comment that.

105
00:07:30,030 --> 00:07:32,130
Wi-Fi Connect Status handler.

106
00:07:35,530 --> 00:07:37,990
Updates the connection status for the web page.

107
00:07:43,520 --> 00:07:46,100
And it's a static esp error type.

108
00:07:47,620 --> 00:07:51,340
Connect status handler, which takes the pointer to the request.

109
00:07:57,120 --> 00:08:00,480
And first, let's fix this comment and I'll just copy this one.

110
00:08:01,740 --> 00:08:02,820
And leave it here.

111
00:08:08,010 --> 00:08:09,320
Let's log.

112
00:08:11,890 --> 00:08:14,230
That Wi-Fi connect status requested.

113
00:08:19,930 --> 00:08:21,100
And we need a care.

114
00:08:22,280 --> 00:08:25,280
That is Json of 100 bytes.

115
00:08:28,080 --> 00:08:30,150
And then sprint into it.

116
00:08:33,270 --> 00:08:34,710
Our escape sequence.

117
00:08:38,560 --> 00:08:40,600
For Wi-Fi Connect status.

118
00:08:47,960 --> 00:08:51,440
And here, just give it the Global Wi-Fi Connect status variable.

119
00:08:58,980 --> 00:09:00,510
I'll set the response type.

120
00:09:04,770 --> 00:09:08,760
For the request and its application slash Json.

121
00:09:09,960 --> 00:09:11,670
Now let's send the response.

122
00:09:15,560 --> 00:09:16,790
For the request.

123
00:09:18,180 --> 00:09:19,850
From the status Json.

124
00:09:20,870 --> 00:09:23,600
For str Len of status Json.

125
00:09:26,540 --> 00:09:27,980
And then let's return.

126
00:09:29,080 --> 00:09:29,660
Spoke.

127
00:09:31,260 --> 00:09:32,310
And that's it.

128
00:09:32,580 --> 00:09:39,540
And as for our Wi-Fi connect status and the index.html, that is just right down here.

129
00:09:41,530 --> 00:09:43,500
And also we have the credentials errors.

130
00:09:46,760 --> 00:09:49,040
So let's just test it out and build.

131
00:09:54,200 --> 00:09:54,400
Right.

132
00:09:54,400 --> 00:09:55,570
So now we can flesh.

133
00:10:06,380 --> 00:10:08,390
Okay, Now let's open up a monitor.

134
00:10:19,560 --> 00:10:20,940
Okay, now connect to the ESP.

135
00:10:28,490 --> 00:10:30,420
And then now let's go to the Web page.

136
00:10:38,390 --> 00:10:39,900
Right now if we hit connect.

137
00:10:40,560 --> 00:10:45,480
We get our error messages for both the Ssid and the password and if we type something in the password

138
00:10:45,480 --> 00:10:46,140
field.

139
00:10:47,990 --> 00:10:49,940
Only the skid warning shows.

140
00:10:51,730 --> 00:10:52,120
Okay.

141
00:10:52,120 --> 00:10:55,190
And then just the Ssid and the password warning appears.

142
00:10:55,210 --> 00:10:55,780
Great.

143
00:10:58,100 --> 00:11:00,590
And next I'll try connecting to an access point.

144
00:11:05,800 --> 00:11:07,660
Now enter a fake password here.

145
00:11:08,920 --> 00:11:09,790
And I'll show it.

146
00:11:10,440 --> 00:11:11,700
And then I'll try to connect.

147
00:11:16,340 --> 00:11:17,630
Now it shows connecting.

148
00:11:19,370 --> 00:11:21,620
And now it's attempting for each retry.

149
00:11:22,890 --> 00:11:25,260
And some reason codes are now printed here.

150
00:11:26,450 --> 00:11:28,160
Which you can feel free to look up.

151
00:11:31,040 --> 00:11:36,920
And after the max retries, the web page is updated with our failure message as expected.

152
00:11:36,950 --> 00:11:37,610
Nice.

153
00:11:41,060 --> 00:11:43,460
Okay, so now I'll try to connect with the real password.

154
00:11:56,210 --> 00:11:57,530
And now try to connect.

155
00:12:01,070 --> 00:12:02,090
And.

156
00:12:03,820 --> 00:12:04,870
Very nice.

157
00:12:04,870 --> 00:12:06,720
We have the connection success message.

158
00:12:06,730 --> 00:12:07,360
Awesome.

159
00:12:07,360 --> 00:12:10,210
And the terminal messages confirm what we expect to see.

160
00:12:11,290 --> 00:12:12,650
So that's it for this one.

161
00:12:12,670 --> 00:12:13,870
I'll see you in the next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 13: Displaying WiFi Connection Information on the Web Page


1
00:00:07,070 --> 00:00:11,690
In order to display the connection information, a few updates are required to the webpage files.

2
00:00:12,110 --> 00:00:16,880
So we'll start here and indexed HTML and make a few updates so that we can display the Access Point,

3
00:00:16,880 --> 00:00:19,460
IP Gateway and netmask info.

4
00:00:19,970 --> 00:00:24,440
Also will include a disconnect button to allow users to disconnect Wi-Fi via the web page.

5
00:00:25,070 --> 00:00:29,510
So let's start off you by creating another div and call it connect info.

6
00:00:33,480 --> 00:00:34,530
Now close the div.

7
00:00:38,450 --> 00:00:39,350
And that a section.

8
00:00:46,320 --> 00:00:48,360
And now within the section, let's create a divide.

9
00:00:50,280 --> 00:00:52,020
For Connected AP label.

10
00:00:55,580 --> 00:00:56,390
And then close it.

11
00:00:58,280 --> 00:00:59,600
Now, create another divide.

12
00:01:00,900 --> 00:01:02,070
For Connected app.

13
00:01:05,410 --> 00:01:06,130
And close that.

14
00:01:11,000 --> 00:01:12,230
And under this section.

15
00:01:13,640 --> 00:01:14,690
Make another divide.

16
00:01:16,730 --> 00:01:18,290
For IP address label.

17
00:01:22,740 --> 00:01:23,460
And close it.

18
00:01:25,240 --> 00:01:26,530
Let's make another four.

19
00:01:27,580 --> 00:01:29,020
WI fi connect IP.

20
00:01:32,570 --> 00:01:33,380
And close that.

21
00:01:36,930 --> 00:01:39,360
Now we'll do another pair of did, so copy this line.

22
00:01:40,330 --> 00:01:41,230
And paste below.

23
00:01:44,880 --> 00:01:47,340
And let's change this one to netmask label.

24
00:01:50,060 --> 00:01:52,910
And this one to wi fi connect netmask.

25
00:01:55,880 --> 00:01:57,160
Now, let's make another blow.

26
00:01:58,810 --> 00:02:00,970
And change this one to Gateway label.

27
00:02:03,190 --> 00:02:05,200
And here it's why Fi Connect Gateway.

28
00:02:08,030 --> 00:02:09,530
Next, let's make our button.

29
00:02:10,860 --> 00:02:13,010
And right here, say, did class buttons.

30
00:02:20,470 --> 00:02:21,730
And now let's close the div.

31
00:02:26,130 --> 00:02:27,840
Then here, let's do an input I'd.

32
00:02:30,120 --> 00:02:31,740
As disconnect, we find.

33
00:02:33,860 --> 00:02:34,640
With the type.

34
00:02:36,090 --> 00:02:36,840
As button.

35
00:02:39,080 --> 00:02:41,240
And the value as disconnect.

36
00:02:43,550 --> 00:02:44,960
And now let's close the input I'd.

37
00:02:47,340 --> 00:02:49,350
And lastly, let's make a horizontal rule.

38
00:02:54,640 --> 00:02:56,350
And that's it for index HTML.

39
00:02:56,950 --> 00:03:01,160
So next, we can go to the stylesheet and let's add some styling to these elements.

40
00:03:01,180 --> 00:03:03,160
So let's go over to access.

41
00:03:08,050 --> 00:03:09,100
Let's move over here.

42
00:03:12,760 --> 00:03:15,160
And right here, let's do the styling for.

43
00:03:16,230 --> 00:03:17,550
Connected AP label.

44
00:03:20,120 --> 00:03:23,660
And a comma for connected AP.

45
00:03:26,570 --> 00:03:29,480
And then here, let's add display in line.

46
00:03:34,490 --> 00:03:35,630
And then let's copy that.

47
00:03:40,430 --> 00:03:41,240
And pasted.

48
00:03:43,690 --> 00:03:45,610
And do IP address label.

49
00:03:50,750 --> 00:03:52,790
And this one as netmask label.

50
00:03:53,860 --> 00:03:56,500
Add a comma for Gateway label.

51
00:04:00,710 --> 00:04:03,590
And this ensures that all of these elements are in line together.

52
00:04:06,660 --> 00:04:07,860
So copy paste.

53
00:04:10,820 --> 00:04:14,420
And now let's do the same with the Wi-Fi Connect IP.

54
00:04:16,910 --> 00:04:18,680
The wi fi connects netmask.

55
00:04:23,750 --> 00:04:25,430
And the Wi-Fi Connect Gateway.

56
00:04:30,470 --> 00:04:31,880
Next, let's add the styling.

57
00:04:32,980 --> 00:04:34,990
Down here for connected AP.

58
00:04:40,010 --> 00:04:42,800
Now, let's add the color, so we can just copy this one.

59
00:04:45,140 --> 00:04:45,920
And paste it.

60
00:04:50,880 --> 00:04:52,470
Now, let's copy this one.

61
00:04:54,000 --> 00:04:54,690
Pace below.

62
00:04:56,220 --> 00:04:58,920
Now we can change it to wi fi connect IP.

63
00:05:01,920 --> 00:05:03,000
And also copy this.

64
00:05:05,080 --> 00:05:08,410
Paced changes to wi fi connect netmask.

65
00:05:11,320 --> 00:05:14,560
Paste and change it to why if I connect Gateway.

66
00:05:15,540 --> 00:05:18,060
Then had the styling for the disconnect, why fi?

67
00:05:23,830 --> 00:05:26,110
And then here, right, display none.

68
00:05:31,080 --> 00:05:36,150
OK, because we only want to display the disconnect button when there's an active connection.

69
00:05:37,320 --> 00:05:39,060
So now let's go to James.

70
00:05:42,280 --> 00:05:46,390
And first, we'll call the Get Connect info from the document ready function.

71
00:05:51,830 --> 00:05:53,060
OK, so let's copy that.

72
00:05:54,380 --> 00:05:56,060
And define it at the bottom of the file.

73
00:06:00,260 --> 00:06:03,080
And comment gets the connection information.

74
00:06:05,180 --> 00:06:06,920
For displaying on the Web page.

75
00:06:11,090 --> 00:06:12,140
And then its function.

76
00:06:13,370 --> 00:06:14,510
Get Connect info.

77
00:06:15,470 --> 00:06:15,900
All right.

78
00:06:15,920 --> 00:06:17,600
And here you'll get Jason.

79
00:06:21,710 --> 00:06:25,100
And it's forward slash wi fi connect info.

80
00:06:26,400 --> 00:06:26,990
Jason?

81
00:06:28,530 --> 00:06:29,220
Function.

82
00:06:32,730 --> 00:06:34,110
And open the curly braces.

83
00:06:35,670 --> 00:06:38,910
And then in here, we want the connected app label.

84
00:06:45,060 --> 00:06:47,280
So, right, connected app label.

85
00:06:54,470 --> 00:06:55,040
HTML.

86
00:06:56,210 --> 00:06:57,800
And right connected to.

87
00:06:59,160 --> 00:07:00,750
Colon with the space.

88
00:07:01,670 --> 00:07:02,690
And that's for our label.

89
00:07:03,970 --> 00:07:04,900
And the next we want.

90
00:07:07,070 --> 00:07:08,360
We want connected AP.

91
00:07:13,550 --> 00:07:14,020
Text.

92
00:07:16,780 --> 00:07:17,590
And for data.

93
00:07:18,710 --> 00:07:19,880
We'll call it AP.

94
00:07:23,650 --> 00:07:25,810
So then we can copy and paste.

95
00:07:30,550 --> 00:07:34,450
And then here we could just change this to IP address label.

96
00:07:37,690 --> 00:07:40,150
And then the text to IP address.

97
00:07:42,690 --> 00:07:45,120
And change this to wi fi connect IP.

98
00:07:49,780 --> 00:07:51,130
And the data is IP.

99
00:07:53,370 --> 00:07:54,690
Now, let's copy paste this one.

100
00:07:58,280 --> 00:08:00,290
And make this one that mask label.

101
00:08:02,700 --> 00:08:05,100
And the text as netmask, Colin.

102
00:08:07,040 --> 00:08:09,950
And change this to wi fi connect netmask.

103
00:08:12,170 --> 00:08:13,520
And the data as netmask.

104
00:08:17,900 --> 00:08:19,390
And let's do this one more time.

105
00:08:20,340 --> 00:08:22,770
For the Gateway, so its gateway label.

106
00:08:24,950 --> 00:08:27,410
And the text to Gateway Colon.

107
00:08:29,550 --> 00:08:33,480
Notes update this one also to Gateway, the data is GW.

108
00:08:37,700 --> 00:08:41,270
And then let's write document get element by ID..

109
00:08:47,970 --> 00:08:49,140
Disconnect why fi?

110
00:08:52,120 --> 00:08:54,340
Dutch style Dutch display.

111
00:08:57,450 --> 00:08:58,320
Equals block.

112
00:09:01,500 --> 00:09:06,390
And this allows us to toggle between showing and hiding the disconnect button element, depending on

113
00:09:06,390 --> 00:09:08,340
whether or not there is connection information.

114
00:09:09,700 --> 00:09:12,130
OK, so now let's close this one with the semicolon.

115
00:09:13,370 --> 00:09:14,900
And now let's copy this function.

116
00:09:17,770 --> 00:09:22,690
And we're going to call it under the successful case within the get why fi status function.

117
00:09:25,440 --> 00:09:29,580
All right, so that's it in the next section, we'll continue programming on the web server side.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,230 --> 00:00:12,030
So let's continue the display and connect info section by further developing the Web server to send

2
00:00:12,030 --> 00:00:13,170
the connection information.

3
00:00:13,890 --> 00:00:16,800
So let's now head over to HTP server does seem.

4
00:00:19,760 --> 00:00:25,880
And first, we need to include ESP wife died because we need functions there to get the app and IP info.

5
00:00:26,330 --> 00:00:27,530
So here let's include.

6
00:00:29,520 --> 00:00:32,330
DSP wi fi Duddridge.

7
00:00:34,250 --> 00:00:36,620
All right, and now let's head down to the you are right handlers.

8
00:00:42,160 --> 00:00:43,330
And let's copy this one.

9
00:00:44,740 --> 00:00:45,850
So we can use it below.

10
00:00:49,580 --> 00:00:52,100
You know, update the name to Wi-Fi Connect info.

11
00:00:53,790 --> 00:00:55,050
And the structure name as well.

12
00:00:57,290 --> 00:01:00,290
And let's update that you are right to Wi-Fi Connect info.

13
00:01:00,740 --> 00:01:01,250
Jason.

14
00:01:02,610 --> 00:01:04,470
And the method is to get.

15
00:01:06,160 --> 00:01:10,990
And the handler will call FTP server life.I get connect info.

16
00:01:16,510 --> 00:01:20,770
And then take the name of the structure and let's pass it down to the euro handler.

17
00:01:23,090 --> 00:01:24,970
And now let's go up and define the handler.

18
00:01:27,340 --> 00:01:28,930
So first, let's take this comment.

19
00:01:30,970 --> 00:01:32,050
And pasted down here.

20
00:01:33,060 --> 00:01:36,300
And change this to wi fi connect info Dot, Jason.

21
00:01:40,140 --> 00:01:43,200
And it updates the Web page with connection information.

22
00:01:46,250 --> 00:01:48,080
Now, let's go back and grab the function name.

23
00:01:51,440 --> 00:01:52,760
And now back to the definition.

24
00:01:57,230 --> 00:01:58,280
And stay static.

25
00:01:59,420 --> 00:02:00,620
Espera type.

26
00:02:02,620 --> 00:02:05,710
Our handler name and it's the request type pointer.

27
00:02:07,270 --> 00:02:07,900
Our HQ.

28
00:02:10,600 --> 00:02:12,730
Now, let's first ESP log info.

29
00:02:17,060 --> 00:02:19,790
WI fi connect info that JSON requested.

30
00:02:27,270 --> 00:02:30,300
And next, we need a care IP and Phil Jason.

31
00:02:31,870 --> 00:02:33,070
Of 200 bytes.

32
00:02:34,610 --> 00:02:35,840
And that should be more than enough.

33
00:02:36,500 --> 00:02:37,670
And then let's set.

34
00:02:38,660 --> 00:02:40,010
IP info, Jason.

35
00:02:42,260 --> 00:02:42,890
Two zero.

36
00:02:44,240 --> 00:02:45,230
For the size of.

37
00:02:46,260 --> 00:02:47,550
IP info, Jason.

38
00:02:50,940 --> 00:02:55,290
And now we need a buffer to hold the IP address, so say care IP.

39
00:02:56,380 --> 00:03:01,960
And the size is IP for address star Len Max.

40
00:03:03,330 --> 00:03:07,080
And this definition will give us the maximum length for an IPv4 address.

41
00:03:07,590 --> 00:03:08,700
So now let's copy that.

42
00:03:10,370 --> 00:03:11,450
And pasted twice.

43
00:03:13,730 --> 00:03:15,080
Now, let's do the netmask.

44
00:03:17,980 --> 00:03:18,730
And the Gateway.

45
00:03:21,800 --> 00:03:26,480
Then let's say if global Wi-Fi Connect status.

46
00:03:30,040 --> 00:03:33,670
Is HTP Wi-Fi status connect success?

47
00:03:37,820 --> 00:03:40,370
Then we need wi fi, AP record type.

48
00:03:43,790 --> 00:03:45,170
And call it Wi-Fi data.

49
00:03:47,160 --> 00:03:49,350
And now let's espero check.

50
00:03:53,300 --> 00:03:54,560
ISP, Wi-Fi.

51
00:03:56,060 --> 00:04:01,010
To get a info and then pass a reference to Wi-Fi data.

52
00:04:03,580 --> 00:04:03,970
OK.

53
00:04:04,450 --> 00:04:08,320
Next, we need a care pointer as a side equals.

54
00:04:09,340 --> 00:04:10,900
Care pointer type cast.

55
00:04:12,450 --> 00:04:14,910
To the Wi-Fi data, Typekit as a side.

56
00:04:17,800 --> 00:04:22,750
And if we follow that, we can view the entire description for the wi fi app record.

57
00:04:28,020 --> 00:04:32,790
So now use the ESP net if IP info typedef.

58
00:04:35,510 --> 00:04:37,040
And call it IP info.

59
00:04:39,220 --> 00:04:39,940
Then do.

60
00:04:40,970 --> 00:04:42,260
Espérer, check.

61
00:04:45,020 --> 00:04:47,600
ESPN net if get IP info.

62
00:04:52,330 --> 00:04:55,420
And then pass or ISP net if state object.

63
00:04:59,020 --> 00:05:01,120
And then a reference to IP info.

64
00:05:04,790 --> 00:05:08,090
And if you recall, this is our station object.

65
00:05:08,960 --> 00:05:16,340
OK, so next, let's convert this IP info to human readable form using ISP.

66
00:05:17,490 --> 00:05:19,020
IPv4 address.

67
00:05:20,990 --> 00:05:22,180
Network to ask you.

68
00:05:25,630 --> 00:05:28,960
And pass a reference to the IP info that IP.

69
00:05:32,240 --> 00:05:33,440
And the IP buffer.

70
00:05:34,640 --> 00:05:37,280
And the length, which is IPv4 address.

71
00:05:38,570 --> 00:05:39,760
Starlin Max.

72
00:05:40,870 --> 00:05:42,040
So copy this line.

73
00:05:43,630 --> 00:05:44,910
Then let's paste it twice.

74
00:05:47,070 --> 00:05:49,230
And then first to the IP in Phil Netmask.

75
00:05:51,080 --> 00:05:52,400
In the netmask buffer.

76
00:05:55,490 --> 00:06:01,220
And then do then do IP Info, Dot Gateway and then pass the gateway buffer.

77
00:06:02,520 --> 00:06:06,190
Next, Sprint Deaf and to IP and Phil Jason.

78
00:06:08,600 --> 00:06:09,800
The escape sequence.

79
00:06:11,560 --> 00:06:12,790
First for the AP.

80
00:06:18,340 --> 00:06:19,570
Then for the netmask.

81
00:06:25,020 --> 00:06:26,400
And then also for the Gateway.

82
00:06:30,400 --> 00:06:31,810
And lastly, for the AP.

83
00:06:35,530 --> 00:06:36,430
And then close it.

84
00:06:38,340 --> 00:06:41,880
And then let's provide variables for the IP netmask.

85
00:06:43,010 --> 00:06:44,990
Gateway and suicide.

86
00:06:51,270 --> 00:06:54,720
And then use the HPD response, said type.

87
00:06:57,150 --> 00:07:00,060
For the request as application JSON.

88
00:07:04,520 --> 00:07:07,430
And then use a speedy response, send.

89
00:07:09,360 --> 00:07:15,660
For the request from AP and Phil Jason for this story, Lin of AP and Phil Jason.

90
00:07:18,730 --> 00:07:20,650
And then I'll return ESP, OK.

91
00:07:22,660 --> 00:07:24,220
All right, so that's it for the handler.

92
00:07:24,550 --> 00:07:29,620
However, I would like to rename it, and let's just do just this white flight part.

93
00:07:29,980 --> 00:07:31,060
So right click here.

94
00:07:32,270 --> 00:07:36,740
You've got to refactor factor, rename and change it to get Wi-Fi.

95
00:07:40,720 --> 00:07:42,940
Connect info and then hit Enter.

96
00:07:45,640 --> 00:07:46,090
OK.

97
00:07:46,120 --> 00:07:46,600
That's it.

98
00:07:47,690 --> 00:07:53,840
Now to recap, this handler checks the global Wi-Fi Connect status, and if it's connect success, meaning

99
00:07:53,840 --> 00:07:59,540
that there is a connection, then we get the connection information and update the IP info JSON with

100
00:07:59,540 --> 00:08:01,700
the connection info and then we send it.

101
00:08:02,360 --> 00:08:07,820
Otherwise, the IP info JSON is sent blank, in which case nothing is displayed on the web page.

102
00:08:08,330 --> 00:08:10,100
OK, so now let's build.

103
00:08:21,600 --> 00:08:22,530
OK, now, flesh.

104
00:08:31,820 --> 00:08:32,890
Now open a monitor.

105
00:08:40,440 --> 00:08:42,060
And then connect to the ESP.

106
00:08:51,100 --> 00:08:52,690
And then go to the Web page with Chrome.

107
00:08:59,170 --> 00:09:00,910
And now let's connect the ESP.

108
00:09:13,540 --> 00:09:14,590
No connect.

109
00:09:18,300 --> 00:09:18,960
And.

110
00:09:20,760 --> 00:09:26,190
There you go, the access point that the ESP is connected to is displayed as well as our assigned IP

111
00:09:26,190 --> 00:09:26,850
information.

112
00:09:27,030 --> 00:09:28,050
All right, well done.

113
00:09:30,750 --> 00:09:34,380
Now, if you refresh the page, the connection success should go away.

114
00:09:34,980 --> 00:09:35,820
So let's try that.

115
00:09:36,940 --> 00:09:37,900
Refresh the page.

116
00:09:40,170 --> 00:09:41,830
And yes, that looks good.

117
00:09:41,880 --> 00:09:42,360
Great.

118
00:09:42,570 --> 00:09:44,460
The connection success message went away.

119
00:09:45,270 --> 00:09:45,600
All right.

120
00:09:45,600 --> 00:09:48,810
So I'll see you in the next lesson and we'll implement the disconnect button here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 14: WiFi Disconnect Button


1
00:00:07,050 --> 00:00:10,410
And this lesson will implement the functionality behind the Disconnect button.

2
00:00:10,860 --> 00:00:15,840
We'll start off here and abduct James, and under the document ready function, we'll make another on

3
00:00:15,840 --> 00:00:16,650
click function.

4
00:00:17,280 --> 00:00:18,840
So let's copy this one right here.

5
00:00:21,160 --> 00:00:22,090
And pace below.

6
00:00:24,740 --> 00:00:26,780
And change it to disconnect, why fine?

7
00:00:28,620 --> 00:00:31,080
And change the function name to disconnect by phone.

8
00:00:34,210 --> 00:00:35,650
All right, so copy this function.

9
00:00:38,200 --> 00:00:39,970
And let's go down to the bottom of the file.

10
00:00:45,220 --> 00:00:46,540
And now let's make a comment.

11
00:00:48,440 --> 00:00:49,670
Disconnects swipe five.

12
00:00:51,610 --> 00:00:53,470
Once the disconnect button is pressed.

13
00:00:55,380 --> 00:00:56,730
And reloads the Web page.

14
00:01:00,480 --> 00:01:01,440
And it's a function.

15
00:01:02,430 --> 00:01:03,510
Disconnect wi fi.

16
00:01:06,620 --> 00:01:08,060
And here will use Ajax.

17
00:01:13,070 --> 00:01:18,380
And for the Irwell, it's forward slash Wi-Fi disconnect, Jason.

18
00:01:24,790 --> 00:01:25,660
And the data type.

19
00:01:28,510 --> 00:01:29,320
This, Jason.

20
00:01:31,560 --> 00:01:32,310
And the method.

21
00:01:33,330 --> 00:01:34,080
Is delete.

22
00:01:39,760 --> 00:01:40,450
This false.

23
00:01:42,390 --> 00:01:42,900
Data.

24
00:01:44,970 --> 00:01:46,080
Is timestamp.

25
00:01:48,840 --> 00:01:49,770
Data now.

26
00:01:52,280 --> 00:01:53,420
Now at a semicolon.

27
00:01:54,870 --> 00:01:57,600
And here will update the Web page.

28
00:02:00,010 --> 00:02:01,330
And use set timeout.

29
00:02:03,040 --> 00:02:04,150
And just follow me here.

30
00:02:04,840 --> 00:02:07,130
Location, don't reload.

31
00:02:08,860 --> 00:02:11,770
Is true with a semicolon inside.

32
00:02:12,730 --> 00:02:17,470
Then comma, and let's set the page to reload after 20 milliseconds.

33
00:02:19,720 --> 00:02:20,080
OK.

34
00:02:21,070 --> 00:02:26,020
So when the disconnect button is pressed, this function is invoked and it refreshes the page after

35
00:02:26,020 --> 00:02:26,770
two seconds.

36
00:02:27,400 --> 00:02:33,310
Meanwhile, in the web server side, Wi-Fi is disconnected and that'll be implemented in the a handler.

37
00:02:35,170 --> 00:02:39,250
All right, so let's implement that now and head over to HTP, Server does see.

38
00:02:41,820 --> 00:02:45,000
So we'll start by copying this your eye handler information.

39
00:02:49,210 --> 00:02:50,470
And let's reuse it below.

40
00:02:51,890 --> 00:02:54,710
And first, let's change this to Wi-Fi disconnect.

41
00:02:55,990 --> 00:02:56,800
That, Jason.

42
00:02:58,050 --> 00:03:00,330
And the structure name to Wi-Fi disconnect.

43
00:03:05,470 --> 00:03:06,400
And the urine.

44
00:03:07,650 --> 00:03:10,200
Is Wi-Fi disconnect, Jason?

45
00:03:14,540 --> 00:03:16,640
The method is HTP delete.

46
00:03:19,960 --> 00:03:24,310
And the handler, it's HTP server, Wi-Fi disconnect.

47
00:03:25,750 --> 00:03:26,680
Jason Handler.

48
00:03:29,170 --> 00:03:32,710
OK, so let's pass the structure name to register that you are a handler.

49
00:03:33,550 --> 00:03:34,870
And let's go up and define it.

50
00:03:37,440 --> 00:03:38,760
Now, let's copy this comment.

51
00:03:42,020 --> 00:03:42,770
And it.

52
00:03:44,040 --> 00:03:47,190
And change this to Wi-Fi disconnect, Jason.

53
00:03:52,680 --> 00:03:57,990
And we'll say responds by sending a message to the wife by application to disconnect.

54
00:04:09,660 --> 00:04:10,770
Then let's grab the name.

55
00:04:12,430 --> 00:04:13,060
Copy it.

56
00:04:16,650 --> 00:04:26,400
And now say static espérer tape, let's drop the name and its age http request type pointer.

57
00:04:27,990 --> 00:04:28,650
Ari Kim.

58
00:04:30,520 --> 00:04:31,810
And now S.P. log.

59
00:04:37,330 --> 00:04:39,790
Why fi disconnect, Jason requested?

60
00:04:45,090 --> 00:04:48,480
In next year's wi fi apps and message.

61
00:04:50,430 --> 00:04:53,520
And we'll say here, wi fi message.

62
00:04:55,480 --> 00:04:57,760
User requested state disconnect.

63
00:05:04,970 --> 00:05:06,200
And will define that later.

64
00:05:07,280 --> 00:05:09,650
Now, let's just return ESP, OK?

65
00:05:15,230 --> 00:05:16,820
Next, let's copy this.

66
00:05:17,820 --> 00:05:19,530
And we'll create a message in the Wi-Fi app.

67
00:05:20,310 --> 00:05:22,020
So go to Wi-Fi app Dunwich.

68
00:05:24,910 --> 00:05:26,370
And let's just drop it right here.

69
00:05:29,570 --> 00:05:32,860
OK, now let's head over to the message handling section of the see file.

70
00:05:35,120 --> 00:05:37,040
And now let's copy this case message.

71
00:05:39,210 --> 00:05:40,170
And pasted here.

72
00:05:42,200 --> 00:05:48,930
And first, let's remove this, and now let's update the case to message user requested stay disconnect.

73
00:05:49,820 --> 00:05:52,040
And now let's update the log message as well.

74
00:05:54,830 --> 00:05:57,740
And now here will update the global retry number.

75
00:06:00,760 --> 00:06:03,070
And we'll set it to Max Connection Retrace.

76
00:06:06,060 --> 00:06:10,140
Because we don't want to re attempt to connection when the disconnect button is pressed.

77
00:06:10,770 --> 00:06:16,500
OK, so next we're going to call the disconnect function, which will result in the case below and then

78
00:06:16,500 --> 00:06:21,840
the failed message to be sent to the web server and we'll need to adjust our state machine here to compensate

79
00:06:21,840 --> 00:06:22,560
for this later.

80
00:06:23,010 --> 00:06:24,600
For now, let's just continue.

81
00:06:25,200 --> 00:06:27,360
And that's espero check.

82
00:06:29,660 --> 00:06:31,580
ESP Wi-Fi disconnect.

83
00:06:35,340 --> 00:06:38,340
And now let's change the Ogbe led status to.

84
00:06:39,410 --> 00:06:42,950
Our GB led FTP server started.

85
00:06:46,930 --> 00:06:53,410
OK, so I'm not sure if this name makes sense anymore, so I'll just make a comment for you or to do.

86
00:06:56,270 --> 00:06:59,690
To rename this status leaded to a name more meaningful.

87
00:07:07,730 --> 00:07:08,780
Or to your liking.

88
00:07:12,400 --> 00:07:15,040
So it might be a good idea to change it if you like.

89
00:07:15,400 --> 00:07:17,290
For now, let's just build the project.

90
00:07:26,330 --> 00:07:27,830
And once you flesh it.

91
00:07:37,960 --> 00:07:39,630
Now, connect to the ESPN.

92
00:07:51,630 --> 00:07:53,430
Then now I'll head over to the Web page.

93
00:08:04,070 --> 00:08:06,080
And now, actually, we want to open the monitor.

94
00:08:09,520 --> 00:08:12,700
And also, I did this backwards, so don't do it this way.

95
00:08:12,820 --> 00:08:15,250
You'll want to do the monitor first, then go to the web page.

96
00:08:16,830 --> 00:08:18,980
Because now I'll probably have to reload the Web page.

97
00:08:20,890 --> 00:08:21,760
So let me do that.

98
00:08:26,590 --> 00:08:28,140
And then I'll just make sure I'm connected.

99
00:08:31,140 --> 00:08:31,710
OK.

100
00:08:34,810 --> 00:08:36,790
And now we're back, OK?

101
00:08:40,390 --> 00:08:42,640
So let's connect, you know, the password.

102
00:08:49,930 --> 00:08:50,740
And connect.

103
00:09:00,220 --> 00:09:02,290
All right, good, so now let's reload to test it.

104
00:09:05,630 --> 00:09:07,090
OK, so now let's disconnect.

105
00:09:12,650 --> 00:09:13,170
Nice.

106
00:09:13,190 --> 00:09:18,200
The Page Reloaded and the Connect info is cleared, and we're no longer connected to an access point.

107
00:09:18,230 --> 00:09:18,770
Excellent.

108
00:09:19,370 --> 00:09:19,730
Great.

109
00:09:19,730 --> 00:09:21,860
So let's continue our development in the next lesson.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 15: Non-Volatile Storage (NVS)


1
00:00:06,830 --> 00:00:10,550
Hello and welcome to the Non-Volatile Storage Implementation section.

2
00:00:10,550 --> 00:00:16,070
In this section, I'll give a brief overview of the ESP, IDF and NVS Library and how we're going to

3
00:00:16,070 --> 00:00:18,440
use it to save and load Wi-Fi credentials.

4
00:00:20,210 --> 00:00:22,880
So first, let's take a look at the implementation.

5
00:00:24,060 --> 00:00:28,560
After the Esp32 successfully connects to an access point via the web page.

6
00:00:28,590 --> 00:00:35,970
The Ssid and password used to connect will be saved to flash and upon startup the esp32 will check the

7
00:00:35,970 --> 00:00:41,970
flash for any saved credentials, and if there are any, they will be used to attempt a connection immediately.

8
00:00:42,000 --> 00:00:45,150
This is a very common setup in Wi-Fi applications.

9
00:00:45,180 --> 00:00:51,450
Also upon startup, if after the max connection retry is reached and a connection attempt cannot be

10
00:00:51,450 --> 00:00:56,580
established, we will clear the flash so those credentials won't be used to connect anymore.

11
00:00:57,390 --> 00:01:02,340
If the disconnect button on the web page is used to disconnect, the credentials will also be cleared

12
00:01:02,340 --> 00:01:04,170
from the flash in this case as well.

13
00:01:04,470 --> 00:01:09,030
And once you have an idea of setting up the state machine and the Wi-Fi application so that these actions

14
00:01:09,030 --> 00:01:13,560
can be handled, you'll be able to customize or adjust the application to your needs.

15
00:01:16,500 --> 00:01:16,800
All right.

16
00:01:16,800 --> 00:01:22,770
So let's take a look at some of the APIs from the Espressif NVS Library and how we can use them.

17
00:01:24,410 --> 00:01:24,680
All right.

18
00:01:24,680 --> 00:01:30,810
So here is a link to expressive documentation for the non-volatile storage library and API reference.

19
00:01:30,830 --> 00:01:36,170
I do suggest you do some reading on your own here and at least browse over the introduction underlying

20
00:01:36,170 --> 00:01:39,890
storage keys and values and namespace sections.

21
00:01:39,920 --> 00:01:44,990
You can also find examples and information about other features that we will not use in this course.

22
00:01:48,360 --> 00:01:55,140
In general NVS components save and load data from storage that is preserved between boots so you can

23
00:01:55,170 --> 00:02:00,690
turn the device off or if it loses power, the data that you've stored will still be there for retrieval

24
00:02:00,690 --> 00:02:01,950
when it starts up again.

25
00:02:02,590 --> 00:02:08,560
In the documentation, it's noted that NVS, using the expressive development framework, works best

26
00:02:08,560 --> 00:02:12,850
for storing small values, e.g. Wi-Fi credentials in our case.

27
00:02:13,420 --> 00:02:15,760
And about keys and values.

28
00:02:15,940 --> 00:02:19,330
NVS operates on the key value pairs.

29
00:02:19,390 --> 00:02:22,690
Keys are Ascii strings and values are the types.

30
00:02:22,720 --> 00:02:29,440
For example, integer types, strings and variable length binary data also known as blobs.

31
00:02:30,100 --> 00:02:31,870
And about namespaces.

32
00:02:31,900 --> 00:02:39,390
We assign each key value pair to a namespace and we specify this namespace when using certain APIs.

33
00:02:39,430 --> 00:02:40,320
For example.

34
00:02:40,330 --> 00:02:41,410
Envs open.

35
00:02:43,560 --> 00:02:43,860
Okay.

36
00:02:43,860 --> 00:02:48,360
So let's take a look at some more specifics regarding saving and retrieving wi fi credentials.

37
00:02:48,390 --> 00:02:53,370
To begin with, saving credentials, we'll need to open the storage area with the given namespace.

38
00:02:53,400 --> 00:02:57,130
We'll call envs open and specify the namespace name.

39
00:02:57,150 --> 00:03:04,110
Open in read write mode in our case and pass a handle to be used for subsequent calls to Envs set and

40
00:03:04,110 --> 00:03:04,440
Envs.

41
00:03:04,530 --> 00:03:07,920
Commit functions to set the Ssid and password.

42
00:03:08,160 --> 00:03:14,700
And for the Envs open function, the first parameter taken is the namespace, then the mode which is

43
00:03:14,700 --> 00:03:17,190
Envs, read, write or envs read only.

44
00:03:17,220 --> 00:03:23,010
And the third parameter is the handle and if successful, the return code is zero.

45
00:03:24,090 --> 00:03:31,350
We will then set the variable length binary value for the Ssid and password using NVS set blob, which

46
00:03:31,350 --> 00:03:34,350
takes the handle obtained from the NVS open function.

47
00:03:34,500 --> 00:03:39,270
Note We cannot use the set function if the handle was opened in read only mode.

48
00:03:40,070 --> 00:03:40,430
All right.

49
00:03:40,430 --> 00:03:45,470
So then the key name, for example, will say CID in quotation marks.

50
00:03:45,830 --> 00:03:52,700
Then the next parameter is the actual value to set, which is the Ssid and password, and then we'll

51
00:03:52,700 --> 00:03:53,990
specify the length.

52
00:03:55,460 --> 00:04:02,090
After setting the values we need to write the changes to non-volatile storage using NVS commit, which

53
00:04:02,090 --> 00:04:04,220
takes the handle as the only parameter.

54
00:04:04,670 --> 00:04:09,380
And for getting the credentials on startup, we'll also need to call NVS open.

55
00:04:09,380 --> 00:04:16,460
And then in our case we'll call NVS, get Blob, which takes the handle, the key name that we had previously

56
00:04:16,460 --> 00:04:23,270
used when saving and the alt value which we'll have to dynamically allocate memory for and the size

57
00:04:23,270 --> 00:04:24,500
or length as well.

58
00:04:27,470 --> 00:04:32,150
When we need to clear the credentials, we'll again open the storage area using NVS.

59
00:04:32,180 --> 00:04:33,980
Open in read write mode.

60
00:04:34,130 --> 00:04:39,530
Then we'll erase the key value pairs using NVS array store, which only takes the handle.

61
00:04:39,740 --> 00:04:44,750
And after erasing, we'll commit the changes to NVS using NVS commit.

62
00:04:48,550 --> 00:04:51,400
So that's all we need to cover for now, let's get to coding.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,930 --> 00:00:12,090
We'll start off the India implementation by adding a couple of new files to go over to the main folder,

2
00:00:12,120 --> 00:00:14,430
right click and add a new head of file.

3
00:00:16,800 --> 00:00:18,930
And call it at Investment H.

4
00:00:23,200 --> 00:00:24,610
Now, let's add a new source file.

5
00:00:28,140 --> 00:00:30,690
And call it app and voice, Dorsey.

6
00:00:34,450 --> 00:00:36,070
Now go over to see make lists.

7
00:00:38,730 --> 00:00:42,450
Into the sources, let's add up in voice gutsy.

8
00:00:45,940 --> 00:00:47,350
And now let's get organized you.

9
00:00:48,530 --> 00:00:51,320
Because now we'll start off in the EPP and vice head of file.

10
00:00:52,900 --> 00:00:55,240
And he will create a few functional prototypes.

11
00:00:56,200 --> 00:00:57,640
So let's first comment you.

12
00:01:00,520 --> 00:01:01,900
Safe station mode.

13
00:01:03,430 --> 00:01:04,780
WI fi credentials.

14
00:01:05,990 --> 00:01:06,860
To envious.

15
00:01:08,590 --> 00:01:11,170
And the return is OK.

16
00:01:12,570 --> 00:01:13,530
If successful.

17
00:01:16,630 --> 00:01:18,520
And it's Espero type.

18
00:01:20,780 --> 00:01:24,170
App and voice save state creds.

19
00:01:25,480 --> 00:01:26,230
And it's void.

20
00:01:29,580 --> 00:01:30,600
Now, let's make another.

21
00:01:33,520 --> 00:01:36,790
Which loads the previously saved.

22
00:01:38,340 --> 00:01:39,240
Credentials.

23
00:01:40,730 --> 00:01:41,810
From Vice.

24
00:01:44,340 --> 00:01:45,180
And the return.

25
00:01:46,450 --> 00:01:51,910
Is true, if previously saved credentials were found.

26
00:01:55,260 --> 00:01:56,570
And the return is bull.

27
00:01:57,930 --> 00:02:00,960
And its app and voice load.

28
00:02:02,390 --> 00:02:03,380
Stay creds.

29
00:02:04,640 --> 00:02:05,390
And it's void.

30
00:02:07,920 --> 00:02:08,940
Now, let's make another.

31
00:02:11,100 --> 00:02:14,460
Which clears station mode credentials.

32
00:02:15,870 --> 00:02:16,920
From NCVHS.

33
00:02:19,820 --> 00:02:20,720
And the return.

34
00:02:22,030 --> 00:02:24,850
Is ESP OK, if successful?

35
00:02:27,190 --> 00:02:29,200
So the return is Espirito.

36
00:02:30,290 --> 00:02:32,240
And we'll name it app and voice.

37
00:02:33,850 --> 00:02:35,390
Clear state creds.

38
00:02:36,960 --> 00:02:37,680
And it's void.

39
00:02:40,870 --> 00:02:45,090
All right, so that's our three prototypes now, let's copy them so we can define them in the C file.

40
00:02:51,630 --> 00:02:52,590
And let's paste them here.

41
00:02:54,810 --> 00:02:56,010
Now we need to include.

42
00:02:57,800 --> 00:02:59,390
Vestibule, that edge.

43
00:03:01,570 --> 00:03:03,250
We also need to include here.

44
00:03:05,700 --> 00:03:06,590
Studio.

45
00:03:10,750 --> 00:03:14,200
And let's also include String Derrick.

46
00:03:17,040 --> 00:03:17,910
And now include.

47
00:03:19,050 --> 00:03:20,430
VSP looked Dunwich.

48
00:03:23,530 --> 00:03:26,980
We also need to include envious flesh.

49
00:03:28,160 --> 00:03:28,750
Duddridge.

50
00:03:30,690 --> 00:03:31,710
And we also need our.

51
00:03:33,660 --> 00:03:35,320
Our app and vestige.

52
00:03:37,050 --> 00:03:38,100
And also include.

53
00:03:39,040 --> 00:03:40,960
Why fi app Duddridge?

54
00:03:43,540 --> 00:03:45,040
And next, let's add a tag.

55
00:03:46,720 --> 00:03:48,040
For logging to the monitor.

56
00:03:51,960 --> 00:03:55,320
And it's a static const care tag.

57
00:03:57,530 --> 00:03:59,570
And let's call it envious.

58
00:04:04,430 --> 00:04:10,790
OK, now we need our NCVHS name space used for station mode credentials.

59
00:04:13,520 --> 00:04:19,190
And it's Konst Chair, app and voice star creds namespace.

60
00:04:21,690 --> 00:04:23,910
And let's call it state creds.

61
00:04:29,000 --> 00:04:36,140
OK, so next, let's define the save state creds function, and we'll need an envious handle.

62
00:04:37,520 --> 00:04:38,600
And call it handle.

63
00:04:40,300 --> 00:04:41,890
And then ESPN aired tape.

64
00:04:43,350 --> 00:04:44,220
Esper.

65
00:04:45,940 --> 00:04:47,290
And now S.P. lug.

66
00:04:50,750 --> 00:04:51,680
That this function.

67
00:04:55,130 --> 00:04:57,770
Is saving station mode credentials.

68
00:04:58,710 --> 00:04:59,370
To flesh.

69
00:05:03,240 --> 00:05:05,110
Now we need a Wi-Fi config type.

70
00:05:07,540 --> 00:05:10,480
Pointer and call it wi fi SDH config.

71
00:05:13,770 --> 00:05:15,450
Now, let's use our wi fi app.

72
00:05:16,350 --> 00:05:18,210
Get wi fi config function.

73
00:05:20,500 --> 00:05:25,340
Right, and if you recall that this function will return the Wi-Fi configuration like some.

74
00:05:27,770 --> 00:05:32,660
And you will need to confirm the validity of this point to before continuing to use it to save credentials

75
00:05:32,660 --> 00:05:33,260
to flesh.

76
00:05:33,770 --> 00:05:37,610
So he will say if we fight state config.

77
00:05:39,170 --> 00:05:43,340
And in here, we'll begin our investor operations and say Esper.

78
00:05:44,990 --> 00:05:46,730
Equals and vice open.

79
00:05:48,910 --> 00:05:50,500
And they'll pass the name space.

80
00:05:51,940 --> 00:05:54,070
And then open in voice read write mode.

81
00:05:58,830 --> 00:06:00,840
Out handle is a reference to the handle.

82
00:06:03,870 --> 00:06:06,810
And then say, if ESB error.

83
00:06:07,950 --> 00:06:10,200
Is not equal to ESP, OK?

84
00:06:12,150 --> 00:06:13,170
Then we'll print.

85
00:06:16,500 --> 00:06:17,490
That R function.

86
00:06:21,090 --> 00:06:21,510
There.

87
00:06:25,010 --> 00:06:26,450
Opening envious handle.

88
00:06:33,140 --> 00:06:36,350
And let's use the spare to name function to get the error.

89
00:06:36,710 --> 00:06:40,220
All right, so say ESP error to name.

90
00:06:41,900 --> 00:06:43,310
In Pass, Esper.

91
00:06:45,430 --> 00:06:47,410
And then we'll return to ESPÉRER.

92
00:06:53,120 --> 00:06:56,570
OK, so now, let's say, set aside.

93
00:06:59,830 --> 00:07:04,060
And it's Esper equals and vice set blub.

94
00:07:08,210 --> 00:07:09,260
And passed the handle.

95
00:07:10,840 --> 00:07:12,130
And then the key is.

96
00:07:14,440 --> 00:07:19,450
And the value is why fi SDR config, SDR.

97
00:07:22,380 --> 00:07:27,390
Aside, and the length is our max assisted length.

98
00:07:30,770 --> 00:07:33,740
And now we'll check the air status and say if.

99
00:07:35,600 --> 00:07:39,360
ESP error is not equal to ESP, OK?

100
00:07:41,100 --> 00:07:42,570
Then let's print the error.

101
00:07:42,900 --> 00:07:45,150
The same as before, so we can copy this.

102
00:07:47,620 --> 00:07:52,090
And then say they're setting aside to invest.

103
00:07:55,600 --> 00:07:56,020
All right.

104
00:07:56,440 --> 00:07:58,690
And next, we can set the password in the same manner.

105
00:07:58,750 --> 00:08:00,070
So let's copy this one.

106
00:08:04,840 --> 00:08:05,770
And pace below.

107
00:08:07,740 --> 00:08:09,450
And let's change this to password.

108
00:08:11,830 --> 00:08:13,510
And change the key to password.

109
00:08:15,570 --> 00:08:17,400
And the value is the password.

110
00:08:20,610 --> 00:08:23,220
All right, in the print message is password.

111
00:08:27,250 --> 00:08:27,940
So next.

112
00:08:29,240 --> 00:08:31,280
We can commit credentials.

113
00:08:32,580 --> 00:08:33,480
Two knives.

114
00:08:35,080 --> 00:08:39,610
So let's do ESP air equals envious commit.

115
00:08:40,710 --> 00:08:41,520
Pass the handle.

116
00:08:45,700 --> 00:08:53,380
And now let's do the checking, let's say, if spare is not equal to ESP, OK?

117
00:08:55,410 --> 00:08:57,360
Then let's print the message and return the error.

118
00:09:01,980 --> 00:09:05,310
It will change this to committing credentials to.

119
00:09:12,440 --> 00:09:12,770
Right.

120
00:09:12,980 --> 00:09:17,480
And next, let's call envy as close in past the handle.

121
00:09:20,040 --> 00:09:21,570
Now, S.P. Lug.

122
00:09:25,190 --> 00:09:26,060
That the function.

123
00:09:29,160 --> 00:09:31,950
Wrote Why five state config?

124
00:09:33,610 --> 00:09:34,990
Station, as you said.

125
00:09:37,470 --> 00:09:40,260
And we'll print it and password.

126
00:09:41,300 --> 00:09:42,150
Animal print that.

127
00:09:44,580 --> 00:09:48,090
And then we'll pass wi fi esta config.

128
00:09:49,630 --> 00:09:56,170
Staked aside and why fi SCA config stay.

129
00:09:57,480 --> 00:09:58,080
Password.

130
00:10:01,390 --> 00:10:01,750
All right.

131
00:10:03,130 --> 00:10:04,360
And now let's print that.

132
00:10:06,120 --> 00:10:06,810
The function.

133
00:10:10,160 --> 00:10:11,680
Returned ESP, OK.

134
00:10:15,210 --> 00:10:17,610
Now, actually, let's return ESB, OK?

135
00:10:19,660 --> 00:10:21,880
OK, so we return, OK, if all went well.

136
00:10:22,970 --> 00:10:25,790
All right, so next, let's do the load state credits function here.

137
00:10:31,870 --> 00:10:33,580
All right, so now I'll get this interview.

138
00:10:37,540 --> 00:10:39,610
And first, let's create an invoice handle here.

139
00:10:41,720 --> 00:10:42,500
And its handle.

140
00:10:45,020 --> 00:10:48,140
And we needed spare time, ESP Air.

141
00:10:49,790 --> 00:10:51,230
And now let's ISP lug.

142
00:10:54,260 --> 00:10:55,280
That the function here.

143
00:10:59,020 --> 00:11:01,870
Is loading Wi-Fi credentials?

144
00:11:04,230 --> 00:11:04,920
From flesh.

145
00:11:09,090 --> 00:11:10,320
And I will say if.

146
00:11:11,130 --> 00:11:14,190
Envious is open in past the space.

147
00:11:21,000 --> 00:11:22,470
And it's envious, read only.

148
00:11:24,480 --> 00:11:25,920
Pass a reference to the handle.

149
00:11:27,460 --> 00:11:29,470
And if that returns, ESP, OK.

150
00:11:30,890 --> 00:11:32,510
Then we'll open up the curly braces.

151
00:11:34,430 --> 00:11:35,510
And then we'll say else.

152
00:11:36,850 --> 00:11:38,290
Put our return false you.

153
00:11:41,900 --> 00:11:46,300
Now, let's go back up to the successful case, and we need a Wi-Fi config type pointer.

154
00:11:48,970 --> 00:11:55,570
WI fi SJ config, and let's use a wi fi app, get wi fi config function.

155
00:11:56,820 --> 00:12:03,150
And now we need to check the point to and say, if we stay config, there's no.

156
00:12:05,860 --> 00:12:07,660
Then we'll want to allocate memory for it.

157
00:12:07,900 --> 00:12:10,270
So say we fight stay config.

158
00:12:13,360 --> 00:12:14,080
Equals.

159
00:12:15,260 --> 00:12:19,490
Why fi config type cast pointer and now, Malak?

160
00:12:20,580 --> 00:12:21,660
For the size of.

161
00:12:22,750 --> 00:12:24,070
Why fi config type?

162
00:12:28,120 --> 00:12:32,290
Next, we need to set the five star config.

163
00:12:33,880 --> 00:12:34,540
Two zero.

164
00:12:35,820 --> 00:12:38,820
For the size of Wi-Fi config type.

165
00:12:42,760 --> 00:12:45,730
OK, so next, we need to allocate a buffer.

166
00:12:49,570 --> 00:12:51,030
And let's use size T.

167
00:12:52,800 --> 00:12:54,390
Why fi config size?

168
00:12:55,590 --> 00:12:59,310
Equals size of the white flight config type.

169
00:13:02,860 --> 00:13:07,810
And now we need a U.S. aid point to call it white flight config buffer.

170
00:13:09,730 --> 00:13:12,550
Equals UNT eight typecast.

171
00:13:14,160 --> 00:13:14,820
Malak.

172
00:13:15,780 --> 00:13:16,710
Signs of.

173
00:13:18,220 --> 00:13:19,720
UNT a type.

174
00:13:21,110 --> 00:13:24,740
Multiplied by the wi fi config size.

175
00:13:27,240 --> 00:13:27,750
OK.

176
00:13:27,780 --> 00:13:29,700
And that ensures our buffer is large enough.

177
00:13:30,800 --> 00:13:33,890
So now Mims said the Wi-Fi config buffer.

178
00:13:35,280 --> 00:13:36,030
Two zero.

179
00:13:37,540 --> 00:13:38,620
For the size of.

180
00:13:39,540 --> 00:13:41,040
Wife iwconfig says.

181
00:13:42,190 --> 00:13:43,930
And that ensures that buffer is clear.

182
00:13:46,250 --> 00:13:48,170
Right, so next, let's load the suicide.

183
00:13:49,130 --> 00:13:51,530
And we'll see if I can fix size.

184
00:13:53,030 --> 00:13:57,440
Equals the size of wi fi star config.

185
00:13:59,920 --> 00:14:02,320
As to that essence, I'd.

186
00:14:03,710 --> 00:14:08,720
OK, next, use Espérer equals envious, get love.

187
00:14:09,760 --> 00:14:10,930
Now past the handle.

188
00:14:12,210 --> 00:14:13,440
Key is the suicide.

189
00:14:14,660 --> 00:14:16,970
And the value as a wife, I can see buffer.

190
00:14:18,620 --> 00:14:21,560
And the length is a reference to a wife iwconfig size.

191
00:14:22,740 --> 00:14:23,100
OK.

192
00:14:23,550 --> 00:14:28,790
And then say, if Esper is not equal to ESP, OK?

193
00:14:30,440 --> 00:14:35,330
Then we need to free the memory, so say free wi fi config buffer.

194
00:14:39,040 --> 00:14:40,080
And then let's print.

195
00:14:42,210 --> 00:14:43,170
That dysfunction.

196
00:14:46,200 --> 00:14:47,400
Now, let's give the air.

197
00:14:49,890 --> 00:14:53,910
And say no station, as the side found in Vice.

198
00:14:56,140 --> 00:14:58,630
And then use the air to name.

199
00:15:01,110 --> 00:15:02,490
And pass the SPRO.

200
00:15:06,000 --> 00:15:07,200
And now return false.

201
00:15:09,850 --> 00:15:15,280
All right, so now we need to copy the suicide retrieved from flesh to our application by config.

202
00:15:15,970 --> 00:15:17,620
So here let's use MEMC copy.

203
00:15:18,800 --> 00:15:20,780
To our Wi-Fi star config.

204
00:15:22,990 --> 00:15:28,060
Stay put aside from the wife iwconfig buffer.

205
00:15:29,680 --> 00:15:31,420
For the Wi-Fi config size.

206
00:15:35,260 --> 00:15:35,980
OK, great.

207
00:15:36,730 --> 00:15:38,860
So next, we need to load the password.

208
00:15:39,490 --> 00:15:43,450
So let's just use the same routine here so we can copy this one above.

209
00:15:46,330 --> 00:15:47,410
And now let's use it below.

210
00:15:48,560 --> 00:15:51,440
Now, let's change this comment here to load password.

211
00:15:53,240 --> 00:15:55,190
And change this to password as well.

212
00:15:57,170 --> 00:16:01,430
And just so you're aware this is our accessing the information from this structure.

213
00:16:02,470 --> 00:16:03,010
Right here.

214
00:16:04,050 --> 00:16:04,440
OK.

215
00:16:06,800 --> 00:16:09,260
So next, let's change the key to password.

216
00:16:12,880 --> 00:16:15,250
And for the printed text, let's change that.

217
00:16:16,810 --> 00:16:18,340
And let's just change it to.

218
00:16:20,720 --> 00:16:22,400
Change it to retrieving password.

219
00:16:26,810 --> 00:16:27,140
All right.

220
00:16:27,320 --> 00:16:28,970
So now we want to copy.

221
00:16:30,740 --> 00:16:31,730
To the password.

222
00:16:33,670 --> 00:16:39,370
OK, so here we're using the password key to load the password into our Wi-Fi config buffer.

223
00:16:39,910 --> 00:16:44,170
And if successful, we copy it to state that password config.

224
00:16:45,220 --> 00:16:49,990
So next, let's free the memory, so we'll say free wi fi config buffer.

225
00:16:54,460 --> 00:16:57,850
And then let's call in as close in past the handle.

226
00:16:59,450 --> 00:17:00,560
And now we'll print that.

227
00:17:04,550 --> 00:17:05,540
The dysfunction.

228
00:17:10,130 --> 00:17:14,480
Found a suicide email printed here and password.

229
00:17:15,590 --> 00:17:16,580
And we'll printed you.

230
00:17:19,260 --> 00:17:21,840
And now give it the wife stay config.

231
00:17:23,460 --> 00:17:27,210
Stay DUT assisted in the fight.

232
00:17:27,330 --> 00:17:28,380
Stay config.

233
00:17:29,370 --> 00:17:31,010
A state that password.

234
00:17:33,320 --> 00:17:36,680
And now it's confirmed that the credentials loaded by returning.

235
00:17:38,240 --> 00:17:39,860
Why fight state config?

236
00:17:41,760 --> 00:17:48,120
Staked aside in the first position, and if it's not equal to a no character.

237
00:17:49,290 --> 00:17:50,790
Then we'll know that it returned true.

238
00:17:53,080 --> 00:17:57,160
OK, so this return statement confirms that we actually have an SSD loaded.

239
00:17:58,830 --> 00:18:00,120
All right, so let's continue.

240
00:18:01,560 --> 00:18:03,450
To the clear state creds function.

241
00:18:05,720 --> 00:18:08,780
And let's start here by creating an envious handle.

242
00:18:14,040 --> 00:18:15,900
We also need an SPRO type.

243
00:18:17,040 --> 00:18:17,940
He espérer.

244
00:18:19,080 --> 00:18:20,220
Now, let's log.

245
00:18:23,550 --> 00:18:25,800
That the clear state creds function.

246
00:18:27,910 --> 00:18:33,400
Is clearing Wi-Fi station mode credentials from flesh?

247
00:18:36,950 --> 00:18:38,600
And first of all, ESB Air.

248
00:18:39,640 --> 00:18:41,680
Equals in vice open.

249
00:18:43,130 --> 00:18:47,360
Pass the name space and it's envious, read write mode.

250
00:18:49,890 --> 00:18:51,750
And it's a reference to our handle.

251
00:18:54,620 --> 00:18:59,480
Now we'll see if the is not equal to ESP, OK?

252
00:19:00,680 --> 00:19:01,730
And then we'll print that.

253
00:19:03,230 --> 00:19:04,220
That a function.

254
00:19:06,770 --> 00:19:09,830
Resulted in error and will print the error.

255
00:19:11,330 --> 00:19:14,780
And we'll say opening envious handle.

256
00:19:16,700 --> 00:19:19,220
And then use ESP Air to name.

257
00:19:20,710 --> 00:19:22,060
Past the ESB air.

258
00:19:25,160 --> 00:19:26,840
Pass the ESPOIR here.

259
00:19:30,250 --> 00:19:31,690
Now we return the error.

260
00:19:35,100 --> 00:19:35,490
OK.

261
00:19:36,700 --> 00:19:38,680
So next, we'll erase credentials.

262
00:19:40,410 --> 00:19:44,640
And then do ESB error equals in race all?

263
00:19:46,090 --> 00:19:47,080
And pass the handle.

264
00:19:48,260 --> 00:19:52,760
And say, if aespa error is not equal to ESP, OK?

265
00:19:54,680 --> 00:19:55,520
Then let's print.

266
00:19:58,710 --> 00:19:59,190
And say.

267
00:20:00,880 --> 00:20:04,060
Error erasing station mode credentials.

268
00:20:05,270 --> 00:20:06,880
And then I'll fix the spelling here.

269
00:20:09,790 --> 00:20:12,010
Now, let's return the air.

270
00:20:15,420 --> 00:20:15,780
OK.

271
00:20:16,650 --> 00:20:21,420
And next, we can commit clearing credentials from envious.

272
00:20:25,370 --> 00:20:26,810
And then do ESB Air.

273
00:20:28,020 --> 00:20:29,760
Equals envious commit.

274
00:20:31,100 --> 00:20:32,120
In pass the handle.

275
00:20:33,530 --> 00:20:35,450
And say, if Esper.

276
00:20:36,550 --> 00:20:38,800
It's not equal to ESP, OK?

277
00:20:40,360 --> 00:20:41,230
Then we'll print.

278
00:20:44,770 --> 00:20:45,810
This time will say.

279
00:20:46,910 --> 00:20:48,640
Air envious commit.

280
00:20:51,740 --> 00:20:52,160
OK.

281
00:20:53,850 --> 00:20:55,620
So now we can envy as close.

282
00:20:56,790 --> 00:20:57,390
The handle.

283
00:20:59,620 --> 00:21:00,580
And then we can print.

284
00:21:03,090 --> 00:21:05,250
There are clear state creds function.

285
00:21:07,100 --> 00:21:08,540
Returned ESP, OK.

286
00:21:13,580 --> 00:21:15,590
And now we can return ESP, OK?

287
00:21:19,490 --> 00:21:19,850
All right.

288
00:21:20,030 --> 00:21:20,750
That looks good.

289
00:21:21,810 --> 00:21:24,720
OK, so but I have one mistake up here.

290
00:21:26,930 --> 00:21:30,830
This password length, this should actually be Max password length.

291
00:21:37,040 --> 00:21:40,460
And one more thing, the spelling up here should be const.

292
00:21:42,300 --> 00:21:45,240
All right, so now let's build a project to make sure there's no errors.

293
00:22:05,270 --> 00:22:06,350
OK, so that looks good.

294
00:22:06,500 --> 00:22:08,750
So in the next lesson, we'll put these functions to use.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,550 --> 00:00:12,920
We'll start off this programming lesson in the wife, a --, so come over here, and the first

2
00:00:12,920 --> 00:00:15,770
thing we need is a new message case for loading saved credentials.

3
00:00:16,610 --> 00:00:19,880
So let's come here to our wi fi up messages.

4
00:00:20,960 --> 00:00:23,030
And let's say wi fi app message.

5
00:00:24,240 --> 00:00:25,710
Load saved credentials.

6
00:00:30,320 --> 00:00:32,240
OK, now let's go to the C file.

7
00:00:35,020 --> 00:00:36,310
And first, let's include.

8
00:00:37,840 --> 00:00:38,980
Investor shortage.

9
00:00:40,890 --> 00:00:43,200
But now let's go down to the global section here.

10
00:00:44,870 --> 00:00:50,570
And now we'll create a section here for free art event group handle and status bits, which we'll use

11
00:00:50,570 --> 00:00:55,400
to control the transition of events in our state machine where our message cases are handled in the

12
00:00:55,410 --> 00:00:57,530
Wi-Fi application free autos task.

13
00:00:59,180 --> 00:01:04,100
So let's say we find application event group handle.

14
00:01:05,420 --> 00:01:06,500
And status bits.

15
00:01:08,720 --> 00:01:15,380
And it's a static event group handle type and call it wi fi app event group.

16
00:01:19,000 --> 00:01:21,910
And then the first bit is a constant.

17
00:01:23,100 --> 00:01:26,700
And call it wi fi, a connecting.

18
00:01:28,180 --> 00:01:29,590
Using saves creds.

19
00:01:31,860 --> 00:01:32,250
Bit.

20
00:01:34,790 --> 00:01:35,930
And say equals.

21
00:01:36,940 --> 00:01:37,660
But zero.

22
00:01:39,010 --> 00:01:40,020
Now, let's do another.

23
00:01:40,170 --> 00:01:41,430
So say constant.

24
00:01:42,890 --> 00:01:43,730
WI fi app.

25
00:01:44,720 --> 00:01:46,910
Connecting from HTP server a bit.

26
00:01:53,710 --> 00:01:55,570
Equals bit one.

27
00:01:58,440 --> 00:02:03,570
And we'll use these bits to signify to the application whether we are connecting, using safe credentials

28
00:02:03,570 --> 00:02:05,400
or connecting from the FTP server.

29
00:02:06,860 --> 00:02:09,350
So let's go down to the Wi-Fi start function, no.

30
00:02:11,300 --> 00:02:13,160
And Hugh will create an event group.

31
00:02:14,470 --> 00:02:15,220
So let's say.

32
00:02:16,620 --> 00:02:19,650
Create wi fi application event group.

33
00:02:23,770 --> 00:02:26,860
And let's use our wi fi app, event group.

34
00:02:29,220 --> 00:02:29,850
Equals.

35
00:02:31,010 --> 00:02:32,600
X event group create.

36
00:02:39,780 --> 00:02:40,200
OK.

37
00:02:40,530 --> 00:02:42,000
And that creates the event group.

38
00:02:43,110 --> 00:02:44,130
And if you follow this.

39
00:02:46,200 --> 00:02:49,170
It'll take you to the event group's head of file from photos.

40
00:02:50,140 --> 00:02:55,810
And on the frittatas website, you can read up on event bits and event groups and event bits are used

41
00:02:55,810 --> 00:03:02,470
to indicate if an event has occurred or not, and an event group is a set of event bits and individual

42
00:03:02,470 --> 00:03:08,260
bits within the event group, a reference by a bit number so they can always find out more information

43
00:03:08,260 --> 00:03:10,570
about event groups from the theater's website.

44
00:03:12,680 --> 00:03:14,120
OK, so let's go up.

45
00:03:15,810 --> 00:03:18,980
And check out the bit definitions, and if you follow this one.

46
00:03:20,080 --> 00:03:24,220
You'll see that impressive has these defined and esprit bit deaf studies.

47
00:03:25,050 --> 00:03:27,160
So now let's head down to the free autos task.

48
00:03:31,840 --> 00:03:35,320
And now here, let's create an instance of the event bits type.

49
00:03:38,300 --> 00:03:39,890
And let's call it event bits.

50
00:03:42,620 --> 00:03:47,510
And if you follow the event bits tape, you'll see that this is a type that holds event bits.

51
00:03:49,620 --> 00:03:56,790
OK, so now let's just adjust our first message here to wi fi app message loads, say its credentials.

52
00:04:01,470 --> 00:04:04,860
So now let's create a new case for it here by copying this one.

53
00:04:06,900 --> 00:04:07,950
And pasting above.

54
00:04:11,300 --> 00:04:13,010
All right, so now let's update the case.

55
00:04:14,670 --> 00:04:18,720
And the message that's logged, and let's get rid of this, and let's say if.

56
00:04:20,550 --> 00:04:22,650
Spin vs load state creds.

57
00:04:25,130 --> 00:04:30,530
And if it returns true, meaning it loaded station credentials, then we'll ESP log.

58
00:04:33,250 --> 00:04:34,960
Loaded station configuration.

59
00:04:39,060 --> 00:04:43,020
And now he will call our Wi-Fi app Connect SDK function.

60
00:04:44,390 --> 00:04:46,850
And now let's use our X event group set bits.

61
00:04:49,250 --> 00:04:51,260
And pass over Wi-Fi app event group.

62
00:04:52,970 --> 00:04:55,640
And set the connecting using saved crowds bit.

63
00:04:57,550 --> 00:04:58,810
And then let's say else.

64
00:04:59,890 --> 00:05:01,540
Then we'll ESB lug.

65
00:05:04,830 --> 00:05:06,960
Unable to load station configuration.

66
00:05:11,450 --> 00:05:12,650
Then we can say next.

67
00:05:14,380 --> 00:05:15,550
Start the Web server.

68
00:05:18,980 --> 00:05:21,410
And let's use wi fi apps send message.

69
00:05:23,860 --> 00:05:26,980
And let's pass these start http server message you.

70
00:05:29,650 --> 00:05:31,720
OK, so that takes care of this case for now.

71
00:05:32,200 --> 00:05:35,290
Next, let's go down to the user requested disconnect case.

72
00:05:37,270 --> 00:05:41,980
And here, let's call the app and voice clear state creds function.

73
00:05:44,860 --> 00:05:49,960
Now, in the gut IP case, we need to save credentials disconnecting, connecting from the HTP server.

74
00:05:50,530 --> 00:05:53,080
So here, let's say event bits.

75
00:05:55,280 --> 00:05:58,580
Equals X event group get its.

76
00:06:00,780 --> 00:06:02,850
And pass the wi fi app event group.

77
00:06:06,760 --> 00:06:09,520
So let's say if event bids.

78
00:06:11,090 --> 00:06:14,840
And wi fi app connecting using saved credit.

79
00:06:21,370 --> 00:06:24,340
Then let's use X Event Group Clear Bits.

80
00:06:29,170 --> 00:06:33,730
In past the event group and then past connecting using saved crowds bit.

81
00:06:35,830 --> 00:06:37,510
And now I'll make a comment here.

82
00:06:38,860 --> 00:06:40,570
Save state creds.

83
00:06:41,320 --> 00:06:43,900
Only if connecting from HTTP server.

84
00:06:48,740 --> 00:06:50,660
And not loaded from envious.

85
00:06:55,880 --> 00:07:02,360
OK, in here, I'll also say clear the bits in case we want to disconnect.

86
00:07:04,780 --> 00:07:05,800
And reconnect.

87
00:07:07,360 --> 00:07:08,380
And then start again.

88
00:07:11,890 --> 00:07:13,270
And now we can say else.

89
00:07:15,230 --> 00:07:18,650
And call app and voice save star creds.

90
00:07:20,800 --> 00:07:22,900
All right, so that takes care of this case for now.

91
00:07:22,990 --> 00:07:25,600
Basically, we only want to save credentials if it's required.

92
00:07:26,050 --> 00:07:26,320
All right.

93
00:07:26,320 --> 00:07:31,990
So now let's go up to the connecting from HTP server case and Use X Event Group said it's.

94
00:07:33,180 --> 00:07:34,500
And Passau Event Group.

95
00:07:35,660 --> 00:07:38,150
And they are connecting from HTP server a bit.

96
00:07:40,430 --> 00:07:43,490
All right, so if we connect from the Web server, we want to set this bit.

97
00:07:44,520 --> 00:07:46,710
All right, so now let's go to the gut IP case.

98
00:07:48,130 --> 00:07:51,340
And here will say if event bits.

99
00:07:52,370 --> 00:07:56,240
And wi fi connecting from HTP server bit.

100
00:08:01,650 --> 00:08:04,470
Then Will X event group clear bits.

101
00:08:07,310 --> 00:08:11,240
In past soybean group and the connecting from HTP server bit.

102
00:08:13,680 --> 00:08:16,470
OK, so now this event is accounted for.

103
00:08:18,030 --> 00:08:23,190
OK, so next, let's go to the state disconnected case, and here we need to account for whether this

104
00:08:23,190 --> 00:08:28,770
event occurred using Sade's credentials or not, so we'll need to check the event pitch and react accordingly.

105
00:08:29,130 --> 00:08:32,040
So first, let's say event bits.

106
00:08:34,230 --> 00:08:39,000
Equals X event group get bits in past the event group.

107
00:08:44,420 --> 00:08:46,520
And then we'll say if event bids.

108
00:08:47,840 --> 00:08:51,500
And wi fi connecting using saved creds bit.

109
00:08:55,390 --> 00:08:57,040
Then we'll ESB lug.

110
00:09:00,300 --> 00:09:01,230
That this case.

111
00:09:04,470 --> 00:09:07,190
And attempt using saved credentials.

112
00:09:10,840 --> 00:09:13,240
And then we'll x event group clear bits.

113
00:09:15,650 --> 00:09:16,820
Passing the event group.

114
00:09:21,410 --> 00:09:25,100
And wi fi app connecting using saved crowds bit.

115
00:09:30,860 --> 00:09:33,620
OK, and then let's invest clear stay creds.

116
00:09:38,170 --> 00:09:39,730
And then we'll say else if.

117
00:09:41,260 --> 00:09:47,080
Event bits and wi fi app connecting from HTTP server bit.

118
00:09:50,680 --> 00:09:52,180
Then we'll ESG lug.

119
00:09:55,750 --> 00:09:56,920
That in our case here.

120
00:10:00,700 --> 00:10:02,590
Attempt from the FTP server.

121
00:10:09,220 --> 00:10:10,540
And then we'll need to clear the bits.

122
00:10:11,930 --> 00:10:13,250
So let's just use this one.

123
00:10:15,720 --> 00:10:18,120
And paste it and then change it to.

124
00:10:20,560 --> 00:10:22,510
From HTP server a bit.

125
00:10:24,880 --> 00:10:29,350
And now in here, we can call HTP Server Monitor.

126
00:10:30,530 --> 00:10:35,300
Send message and pass HTP message, wi fi connect fail.

127
00:10:41,880 --> 00:10:45,480
All right, so we only send that message if we're connecting from the Web server.

128
00:10:45,930 --> 00:10:52,830
However, I do think we should expand both the HTP server and Wi-Fi application to handle the user requested

129
00:10:52,830 --> 00:10:54,090
disconnect situation.

130
00:10:54,690 --> 00:11:01,290
So now let's go to HTP server Duddridge and create a new Wi-Fi status for HTP.

131
00:11:01,290 --> 00:11:03,060
Wi-Fi status disconnected?

132
00:11:08,750 --> 00:11:13,640
And also create a new monitor message and call it 8TB message.

133
00:11:15,310 --> 00:11:16,780
User disconnect.

134
00:11:19,950 --> 00:11:22,290
And now go to HTP Server Dot, see?

135
00:11:23,930 --> 00:11:26,210
And here, let's create a new case for our message.

136
00:11:27,170 --> 00:11:28,490
So here we can use this one.

137
00:11:33,400 --> 00:11:36,080
Now, update the case to user disconnect.

138
00:11:38,950 --> 00:11:40,030
And the message.

139
00:11:41,420 --> 00:11:45,980
Now we'll update the global Wi-Fi status to Wi-Fi status disconnected.

140
00:11:49,640 --> 00:11:51,810
And now we can go back to the at sea.

141
00:11:52,460 --> 00:11:53,300
And now let's go up.

142
00:11:56,420 --> 00:11:59,090
All the way up here and create a new status bit.

143
00:12:00,890 --> 00:12:06,350
And it's constant wi fi app user requested stay disconnected, but.

144
00:12:13,440 --> 00:12:14,370
And it's a bit, too.

145
00:12:17,300 --> 00:12:20,540
OK, so now let's go back to the free autos task state machine.

146
00:12:25,260 --> 00:12:28,240
Another user requested state disconnect.

147
00:12:29,190 --> 00:12:29,850
Right here.

148
00:12:30,120 --> 00:12:31,050
Let's set the bit.

149
00:12:34,030 --> 00:12:34,960
Or event group.

150
00:12:39,030 --> 00:12:40,440
And it's a WI Wi-Fi app.

151
00:12:41,410 --> 00:12:42,430
User requested.

152
00:12:43,890 --> 00:12:45,210
Stay disconnect, but.

153
00:12:47,850 --> 00:12:50,160
OK, so now let's go down to the disconnect case.

154
00:12:51,880 --> 00:12:53,020
And say else if.

155
00:12:54,020 --> 00:12:59,300
Event bits and wi fi app user requested stay disconnected.

156
00:13:01,960 --> 00:13:03,340
Then ESB log.

157
00:13:06,030 --> 00:13:07,440
From the disconnected case.

158
00:13:10,560 --> 00:13:12,480
User requested disconnection.

159
00:13:17,920 --> 00:13:20,950
And now ex event group Clear Bits.

160
00:13:23,780 --> 00:13:24,650
Our event group.

161
00:13:26,000 --> 00:13:27,860
And our state disconnect bit.

162
00:13:32,710 --> 00:13:37,600
Next, let's let the Web server know using a CTP server monitor send message.

163
00:13:42,910 --> 00:13:46,450
And it's to be message why fi user disconnect?

164
00:13:50,230 --> 00:13:55,210
And this covers all of the obvious scenarios for the disconnected case, but there is one more case

165
00:13:55,210 --> 00:13:57,430
where perhaps the access point is unavailable.

166
00:13:57,610 --> 00:13:58,690
So let's say else.

167
00:14:01,620 --> 00:14:02,480
ESP log.

168
00:14:05,050 --> 00:14:06,130
That from our case.

169
00:14:09,310 --> 00:14:10,300
Attempt failed.

170
00:14:11,260 --> 00:14:13,660
Check Wi-Fi access point to availability.

171
00:14:19,920 --> 00:14:20,280
All right.

172
00:14:20,940 --> 00:14:22,510
So then I'll write a message for you here.

173
00:14:22,860 --> 00:14:25,850
Adjust this case to your needs.

174
00:14:27,000 --> 00:14:29,430
And maybe you want to keep trying to connect.

175
00:14:34,240 --> 00:14:34,990
For example.

176
00:14:37,220 --> 00:14:40,940
OK, now we can remove this message, send call, so get rid of that.

177
00:14:42,790 --> 00:14:43,870
And now let's build.

178
00:14:58,830 --> 00:15:00,690
OK, so then when you're ready, you can flush.

179
00:15:10,440 --> 00:15:12,150
All right, and next, let's open the monitor.

180
00:15:19,410 --> 00:15:21,030
And now we can connect to the ESP.

181
00:15:32,570 --> 00:15:34,040
Right now, let's go to the Web page.

182
00:15:41,580 --> 00:15:44,310
Right now, let's connect and start testing the new functions.

183
00:16:02,310 --> 00:16:03,090
And now connect.

184
00:16:10,980 --> 00:16:11,700
OK, great.

185
00:16:12,660 --> 00:16:15,270
And from the monitor, we could see that the credentials were saved.

186
00:16:15,810 --> 00:16:19,620
So now, of course, a reboot using the Enable button on the ESP.

187
00:16:20,070 --> 00:16:21,210
OK, and you could do the same.

188
00:16:22,290 --> 00:16:26,070
And now we see that we've automatically reconnected using our saved credentials.

189
00:16:26,370 --> 00:16:26,880
Nice.

190
00:16:29,170 --> 00:16:30,430
So now refresh the page.

191
00:16:34,610 --> 00:16:35,450
And all looks great.

192
00:16:36,730 --> 00:16:38,830
So now I'll disconnect my access point.

193
00:16:46,630 --> 00:16:48,970
OK, so now the ECB is really trying to connect.

194
00:16:55,740 --> 00:16:57,960
And after Max Re tries.

195
00:16:59,200 --> 00:17:02,680
Our last statement is reached in the messages looked perfect.

196
00:17:04,080 --> 00:17:06,690
OK, so it's the message right here.

197
00:17:09,730 --> 00:17:11,660
All right, so now we could try another scenario.

198
00:17:12,530 --> 00:17:17,570
And now I'll leave my access point disconnected and I'll reboot the ESP again.

199
00:17:18,050 --> 00:17:22,310
Then on startup, if it fails to connect, the credentials should be deleted.

200
00:17:23,090 --> 00:17:24,260
OK, so let's try it.

201
00:17:25,100 --> 00:17:26,390
So just give me a moment.

202
00:17:37,990 --> 00:17:43,570
OK, now the ECB is trying to connect, using saved credentials and retrying.

203
00:17:44,520 --> 00:17:45,270
And retrying.

204
00:17:50,160 --> 00:17:56,290
And after maximum retrace, the clear stay creds function is called exactly what we expected.

205
00:17:56,310 --> 00:17:56,670
Great.

206
00:17:57,030 --> 00:17:58,470
And here is the logged message.

207
00:18:04,420 --> 00:18:09,400
And here is our corresponding message case with the clear state creds function is called.

208
00:18:10,900 --> 00:18:11,590
All right, great.

209
00:18:12,310 --> 00:18:13,930
So that's it for this lesson.

210
00:18:14,050 --> 00:18:15,220
Let's continue in the next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 16: Button with Interrupt & Semaphore

1
00:00:06,860 --> 00:00:09,440
Welcome to the Wi-Fi reset button section.

2
00:00:09,440 --> 00:00:15,440
In this section, I'll describe how we're going to use the boot button to disconnect the esp32 and clear

3
00:00:15,440 --> 00:00:16,490
the credentials.

4
00:00:18,050 --> 00:00:20,420
So let's jump right into the implementation.

5
00:00:21,280 --> 00:00:24,160
In order to accomplish this, we'll take a few steps.

6
00:00:24,190 --> 00:00:28,600
The boot button will be configured to generate an interrupt on Gpio zero.

7
00:00:28,930 --> 00:00:35,020
And when the interrupt occurs, a message will be sent to the Wi-Fi application about the user request

8
00:00:35,020 --> 00:00:37,420
to disconnect and clear the credentials.

9
00:00:37,630 --> 00:00:43,660
Upon receiving the message, the Wi-Fi application will check if there really is an active connection

10
00:00:43,660 --> 00:00:49,870
prior to disconnecting and clearing the credentials because we don't want to call ESP Wi-Fi disconnect

11
00:00:49,870 --> 00:00:52,120
unless there is an active connection.

12
00:00:54,100 --> 00:00:54,400
All right.

13
00:00:54,400 --> 00:00:59,260
So let's take a look at some information about Gpio interrupts and binary semaphores.

14
00:01:00,130 --> 00:01:00,460
Okay.

15
00:01:00,460 --> 00:01:06,610
So just very briefly, an interrupt signal is a signal that indicates the occurrence of a specific event

16
00:01:06,610 --> 00:01:12,550
that requires immediate attention and blocks the normal program execution to run an interrupt service

17
00:01:12,550 --> 00:01:16,990
routine or ISR, which reacts to the event that occurred.

18
00:01:17,110 --> 00:01:21,670
Also note that ISRS must have a short execution time.

19
00:01:21,700 --> 00:01:24,730
We want to get in and out as quickly as possible.

20
00:01:24,970 --> 00:01:26,470
The Gpio interrupt.

21
00:01:26,470 --> 00:01:32,290
In our case, we are configuring the interrupt to trigger on the falling edge signal because when you

22
00:01:32,290 --> 00:01:39,520
press the boot button, the pin connects to ground as shown here and the esp32 dev kit C schematic.

23
00:01:39,760 --> 00:01:43,930
You should see something similar in the schematic for all espressif dev kits.

24
00:01:44,980 --> 00:01:52,690
And additionally, due to the short execution of Icers, a binary semaphore will be used to notify the

25
00:01:52,690 --> 00:01:57,580
Freertos task which will handle the actions performed when the button is pressed.

26
00:01:59,270 --> 00:02:01,650
And about binary semaphores.

27
00:02:01,670 --> 00:02:07,370
Binary semaphores are semaphores which can assume the value of zero and one only.

28
00:02:07,400 --> 00:02:10,430
Hence they can be used as a signalling mechanism.

29
00:02:11,300 --> 00:02:15,380
The ESP IDF API for semaphores can be found here.

30
00:02:17,030 --> 00:02:23,660
I recommend you browse through here briefly and we'll use the semaphore, create binary function to

31
00:02:23,660 --> 00:02:24,990
create our semaphore.

32
00:02:25,010 --> 00:02:27,770
And you can find an example usage of this below.

33
00:02:29,520 --> 00:02:36,840
Also within the interrupt service routine, we'll need to use the API x semaphore give from ISR.

34
00:02:37,570 --> 00:02:40,390
And we'll use this to notify the button task.

35
00:02:40,510 --> 00:02:43,840
There's an example usage of this that you can check out as well.

36
00:02:45,310 --> 00:02:50,290
And within the freertos task we'll use x semaphore take.

37
00:02:51,210 --> 00:02:56,340
And at this point the task has been notified and will handle the required actions there.

38
00:02:59,230 --> 00:02:59,520
All right.

39
00:02:59,530 --> 00:03:04,450
Now let's briefly review the APIs we'll use for the reset button Gpio configuration.

40
00:03:06,380 --> 00:03:10,700
First of all, I can recommend that you review the espresso API reference here.

41
00:03:10,910 --> 00:03:14,870
Here you'll find an overview of the 34 physical Gpio pads.

42
00:03:15,140 --> 00:03:21,200
Each pad can be used as general purpose i o or can be connected to an internal peripheral signal.

43
00:03:21,410 --> 00:03:29,030
So check out this table and other comments, especially before getting into using ADC, SPI or RTC.

44
00:03:29,510 --> 00:03:32,720
Also, you can check application examples here as well.

45
00:03:33,630 --> 00:03:36,930
Part of our configuration will include setting the direction of the Gpio.

46
00:03:36,960 --> 00:03:41,160
We are working with as an input using Gpio set direction.

47
00:03:41,750 --> 00:03:47,720
This function will take the Gpio number of the Wi-Fi reset button, which is zero, and the mode as

48
00:03:47,720 --> 00:03:49,460
well, which is input mode.

49
00:03:51,160 --> 00:03:55,270
Then we'll set the interrupt type of the Gpio as falling edge.

50
00:03:55,300 --> 00:04:03,010
We'll use the Gpio intr neg edge as an input parameter to Gpio set interrupt type.

51
00:04:03,780 --> 00:04:09,960
Again, this one takes the Gpio number, the WiFi reset button in our case, and the interrupt type

52
00:04:09,960 --> 00:04:11,610
which will be negative edge.

53
00:04:13,420 --> 00:04:17,480
Next we'll need to install the ESR service using Gpio.

54
00:04:17,500 --> 00:04:19,630
Install ESR service.

55
00:04:19,750 --> 00:04:27,670
This function installs the drivers Gpio ESR handler service which allows per pin Gpio interrupt handlers.

56
00:04:27,940 --> 00:04:36,160
Also note if this function is used, the ESR service provides a global Gpio, ESR and individual pin

57
00:04:36,160 --> 00:04:40,990
handlers are registered via the Gpio ESR handler add function.

58
00:04:42,300 --> 00:04:47,700
Which is actually the next API that we'll use to specify the interrupt service routine that will run

59
00:04:47,700 --> 00:04:49,860
when the interrupt for that pin is triggered.

60
00:04:50,040 --> 00:04:57,660
For this function we'll need the Gpio number and ISR handler or name of the ISR that we'll define in

61
00:04:57,660 --> 00:05:00,120
any arguments if we'd like to use any.

62
00:05:01,040 --> 00:05:08,780
And lastly, when we define the ESR, we can place it into the ihram section by using the ihram attribute.

63
00:05:08,810 --> 00:05:11,700
We'll use this just as the example shows below.

64
00:05:11,720 --> 00:05:16,460
And if you're interested in learning more, please feel free to browse through this information before

65
00:05:16,460 --> 00:05:17,360
we get started.

66
00:05:19,230 --> 00:05:19,530
All right.

67
00:05:19,530 --> 00:05:20,460
So that's it for now.

68
00:05:20,460 --> 00:05:21,600
Let's get started.




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,880 --> 00:00:09,940
We'll start off this lesson by adding a couple of new files and domain.

2
00:00:10,210 --> 00:00:11,910
So let's first add the new source file.

3
00:00:13,610 --> 00:00:15,860
And call it Wi-Fi reset button.

4
00:00:16,870 --> 00:00:17,470
Don't seem.

5
00:00:19,060 --> 00:00:20,500
And then let's add a new head of file.

6
00:00:23,880 --> 00:00:26,070
And call this Wi-Fi reset button.

7
00:00:27,680 --> 00:00:28,220
But each.

8
00:00:31,320 --> 00:00:32,850
OK, so we'll get organized to you.

9
00:00:36,810 --> 00:00:38,310
And then go to see make lists.

10
00:00:39,720 --> 00:00:42,900
And to the sources, let's add the wi fi reset button.

11
00:00:44,320 --> 00:00:45,250
That see file.

12
00:00:46,820 --> 00:00:47,240
All right.

13
00:00:47,300 --> 00:00:49,010
And now let's go to tasks common.

14
00:00:51,780 --> 00:00:57,300
And Sheer will add the information for the Wi-Fi reset button task.

15
00:00:59,410 --> 00:01:02,890
And define why fi reset button.

16
00:01:06,540 --> 00:01:07,830
And I'll copy this part.

17
00:01:09,350 --> 00:01:11,030
And it's the stack size.

18
00:01:12,210 --> 00:01:14,460
And make it 20, 48 bytes.

19
00:01:15,330 --> 00:01:17,610
And next is the priority.

20
00:01:19,310 --> 00:01:20,030
As six.

21
00:01:20,950 --> 00:01:21,670
And the next.

22
00:01:22,980 --> 00:01:23,610
The caller ID.

23
00:01:24,940 --> 00:01:25,810
And make it zero.

24
00:01:27,900 --> 00:01:28,830
OK, it looks good.

25
00:01:29,640 --> 00:01:32,580
So next, let's go to the Wi-Fi reset button header file.

26
00:01:34,930 --> 00:01:40,720
And the first thing that we'll do here is create the default interrupt flag.

27
00:01:43,770 --> 00:01:48,960
And define it as ESP into our flag default.

28
00:01:50,310 --> 00:01:51,150
And it's zero.

29
00:01:51,960 --> 00:01:59,160
OK, next, let's define the GPIO and first say wi fi reset button is the boot button.

30
00:02:01,060 --> 00:02:01,900
On the delicate.

31
00:02:04,060 --> 00:02:07,600
And define it as why fi reset button.

32
00:02:08,850 --> 00:02:10,860
And it's A0, right?

33
00:02:11,940 --> 00:02:15,750
OK, nuts, let's make a function prototype and make a comment here.

34
00:02:16,470 --> 00:02:18,570
Configures wi fi reset button.

35
00:02:20,550 --> 00:02:22,320
And interrupt configuration.

36
00:02:25,710 --> 00:02:28,320
And it's void fi reset button.

37
00:02:29,950 --> 00:02:30,580
Config.

38
00:02:31,390 --> 00:02:32,080
And it's void.

39
00:02:34,050 --> 00:02:34,380
All right.

40
00:02:34,830 --> 00:02:38,430
And now let's copy this so we can define it in the C file.

41
00:02:41,660 --> 00:02:44,300
And in the C file, let's just drop it right here.

42
00:02:47,230 --> 00:02:49,090
OK, now let's include fructose.

43
00:02:49,990 --> 00:02:51,070
And the first include.

44
00:02:52,440 --> 00:02:53,460
This free autos.

45
00:02:54,440 --> 00:02:56,990
Slash and I'll just copy this part.

46
00:02:59,500 --> 00:03:01,030
And this one is free autos.

47
00:03:02,210 --> 00:03:02,570
Courage.

48
00:03:04,440 --> 00:03:07,230
And next include Trescothick.

49
00:03:08,420 --> 00:03:10,850
And also include Reata SIM for.

50
00:03:14,330 --> 00:03:17,240
And make sure you note the proper spelling here, it's simple.

51
00:03:19,710 --> 00:03:20,760
And now let's include.

52
00:03:21,830 --> 00:03:24,650
Driver slash GPIO Duddridge.

53
00:03:26,780 --> 00:03:30,080
And also include our ESP lug tonnage.

54
00:03:31,460 --> 00:03:32,900
And that's for our log functions.

55
00:03:33,800 --> 00:03:40,190
And next, let's include our application headers, so first include tasks common.

56
00:03:44,660 --> 00:03:47,960
And also include Wi-Fi app storage.

57
00:03:50,350 --> 00:03:51,880
And of course, we want to include.

58
00:03:53,110 --> 00:03:54,820
Our new wi fi reset button.

59
00:03:57,930 --> 00:03:59,520
All right, and let's do a tag.

60
00:04:00,720 --> 00:04:02,280
Static const care.

61
00:04:04,940 --> 00:04:07,190
And call it wi fi reset button.

62
00:04:13,800 --> 00:04:14,370
And next.

63
00:04:15,260 --> 00:04:16,670
We need a semaphore handle.

64
00:04:19,980 --> 00:04:27,270
And it's semaphore handle underscore T and call it Y5 reset semaphore.

65
00:04:29,820 --> 00:04:30,780
And said it to no.

66
00:04:32,980 --> 00:04:36,400
OK, and now let's go to the Wi-Fi reset button config.

67
00:04:37,500 --> 00:04:39,990
And first, we'll create the binary semaphore.

68
00:04:43,070 --> 00:04:45,140
And that's a wi fi reset, semaphore.

69
00:04:47,920 --> 00:04:51,220
Equals x semaphore create binary.

70
00:04:58,640 --> 00:04:59,030
OK.

71
00:04:59,480 --> 00:05:01,940
And next, let's configure the button.

72
00:05:03,020 --> 00:05:04,070
And set the direction.

73
00:05:06,550 --> 00:05:09,490
And use GPIO pad, select GPIO.

74
00:05:13,570 --> 00:05:15,400
And pass the Wi-Fi reset button.

75
00:05:18,480 --> 00:05:20,580
And then use GPIO set direction.

76
00:05:24,030 --> 00:05:25,830
And then pass the Wi-Fi reset button.

77
00:05:31,240 --> 00:05:34,000
And set the mode as GPIO mode input.

78
00:05:39,670 --> 00:05:41,620
Next, let's enable interrupt.

79
00:05:44,810 --> 00:05:45,860
On the negative edge.

80
00:05:47,980 --> 00:05:50,530
And use of set interrupt tape.

81
00:05:51,740 --> 00:05:53,480
And pass the Wi-Fi reset button.

82
00:05:57,380 --> 00:06:01,700
And for the insert type, it's GPIO into your neck edge.

83
00:06:07,610 --> 00:06:10,520
And next, let's create the Wi-Fi reset button Teske.

84
00:06:14,390 --> 00:06:16,850
With X task creates pinned to core.

85
00:06:22,130 --> 00:06:25,700
And call it with the reference to Wi-Fi reset button.

86
00:06:29,660 --> 00:06:32,660
And the tag is the same fi reset button.

87
00:06:35,460 --> 00:06:38,670
And the depth is a Wi-Fi reset button to ask.

88
00:06:41,060 --> 00:06:41,840
Stack size.

89
00:06:43,100 --> 00:06:44,570
PV parameters are no.

90
00:06:45,710 --> 00:06:49,010
And the priority is a Wi-Fi reset button desk.

91
00:06:54,140 --> 00:06:55,550
And the task handle is no.

92
00:06:56,480 --> 00:06:59,970
And the caller ID is our Wi-Fi reset button to ask.

93
00:07:02,190 --> 00:07:02,850
Korede.

94
00:07:08,330 --> 00:07:12,480
Next will install GPIO, our service.

95
00:07:14,560 --> 00:07:22,750
And use GPIO and still by Assad's service and pass or ISP into your flag default.

96
00:07:26,280 --> 00:07:29,070
OK, next, let's attach the interrupt service routine.

97
00:07:34,710 --> 00:07:36,840
With ISI Handler.

98
00:07:37,870 --> 00:07:38,320
Add.

99
00:07:40,390 --> 00:07:42,190
And pass the Wi-Fi reset button.

100
00:07:45,320 --> 00:07:50,060
And then the ISI handler will define it as wi fi reset button ISI Handler.

101
00:07:54,840 --> 00:07:55,890
And the dogs are no.

102
00:07:58,560 --> 00:08:03,630
OK, so next, we'll have to define the ISI handler and the wi fi reset button to ask.

103
00:08:04,410 --> 00:08:05,760
OK, so let's come up you.

104
00:08:08,400 --> 00:08:11,670
And let's say why fi reset button desk.

105
00:08:12,690 --> 00:08:14,610
Reacts to a boot button event.

106
00:08:18,280 --> 00:08:20,920
By sending a message to the Wi-Fi application.

107
00:08:25,830 --> 00:08:27,720
To disconnect from Wi-Fi.

108
00:08:29,670 --> 00:08:31,200
And clear the saved credentials.

109
00:08:34,860 --> 00:08:37,350
All right, so the parameter TV program.

110
00:08:39,630 --> 00:08:42,030
Is a parameter which can be passed to the task.

111
00:08:48,390 --> 00:08:49,380
So this is a void.

112
00:08:50,290 --> 00:08:55,870
A Wi-Fi reset button test, and it's a void pointer TV program.

113
00:08:58,230 --> 00:09:00,210
OK, now let's create our endless for loop.

114
00:09:04,240 --> 00:09:06,640
And you will need to check if we can obtain the semaphore.

115
00:09:07,270 --> 00:09:08,230
So say if.

116
00:09:09,230 --> 00:09:10,220
Semaphore, take.

117
00:09:15,530 --> 00:09:17,510
And it's the Wi-Fi reset semaphore.

118
00:09:21,250 --> 00:09:22,270
Port Max DeLay.

119
00:09:27,340 --> 00:09:29,110
And if that returns true.

120
00:09:33,770 --> 00:09:35,120
Then let's ESV log.

121
00:09:39,200 --> 00:09:41,990
That wi fi reset button interrupt occurred.

122
00:09:49,160 --> 00:09:52,970
And then we'll say send a message to disconnect wi fi.

123
00:09:57,820 --> 00:09:58,900
And clear credentials.

124
00:10:00,640 --> 00:10:02,860
Let's use our wi fi app, send message.

125
00:10:06,390 --> 00:10:08,370
And pass the Wi-Fi message.

126
00:10:09,860 --> 00:10:11,960
User requested state disconnect.

127
00:10:15,040 --> 00:10:20,140
And now we'll put a delay here, so that quick button presses won't result in sending messages in rapid

128
00:10:20,140 --> 00:10:20,770
succession.

129
00:10:21,430 --> 00:10:23,590
So let's use the task delay.

130
00:10:27,050 --> 00:10:29,180
With the delay of two thousand milliseconds.

131
00:10:37,900 --> 00:10:38,830
All right, that's it.

132
00:10:39,340 --> 00:10:43,020
So next, let's define our ISO handler, and we'll do it up here.

133
00:10:44,670 --> 00:10:46,620
And say ISI Handler.

134
00:10:47,800 --> 00:10:50,350
For the Wi-Fi reset boot button.

135
00:10:54,610 --> 00:10:55,750
And the parameter ARG.

136
00:10:57,960 --> 00:10:59,700
Is a parameter which can be passed.

137
00:11:03,740 --> 00:11:04,880
To the ISI handler.

138
00:11:09,690 --> 00:11:12,060
And it's void, I attribute.

139
00:11:13,240 --> 00:11:14,660
And it's a reset button.

140
00:11:14,680 --> 00:11:15,610
I saw a handler.

141
00:11:16,720 --> 00:11:18,910
And it takes a valid point to ask.

142
00:11:20,880 --> 00:11:24,000
And in here will notify the button to ask.

143
00:11:28,380 --> 00:11:34,740
Using eczema for GIF from ISO and pass a wi fi reset semaphore.

144
00:11:37,360 --> 00:11:38,860
And the second parameter is no.

145
00:11:41,980 --> 00:11:48,550
So to recap, we're going to call the public function wi fi reset button config from Maine Dot C, and

146
00:11:48,550 --> 00:11:53,470
when the user presses the boot button, the interrupt service routine will be invoked, which gives

147
00:11:53,470 --> 00:11:54,210
the semaphore.

148
00:11:54,790 --> 00:12:00,970
Then the wi fi reset button task takes the semaphore, which allows the button task to unblock so that

149
00:12:00,970 --> 00:12:03,910
the message can be sent to the Wi-Fi application to disconnect.

150
00:12:04,660 --> 00:12:05,440
OK, that's it.

151
00:12:06,070 --> 00:12:08,860
But we have to make a couple of changes to the Wi-Fi app that see.

152
00:12:10,840 --> 00:12:13,420
So come here and let's add another status bit.

153
00:12:14,230 --> 00:12:19,330
And we need another status bit to indicate to the application that the ESB thirty two is indeed connected

154
00:12:19,330 --> 00:12:25,000
to an access point before reacting to the Wi-Fi disconnect button press and calling the disconnect function.

155
00:12:25,690 --> 00:12:26,090
OK.

156
00:12:26,830 --> 00:12:28,450
So let's say consent.

157
00:12:30,660 --> 00:12:33,360
WI fi app Stay Connected.

158
00:12:36,380 --> 00:12:37,370
But IP bit.

159
00:12:39,850 --> 00:12:40,990
Equals bid three.

160
00:12:42,960 --> 00:12:48,420
All right, so first, we need to set this bid when the ESP 32 has a connection and is assigned an IP.

161
00:12:49,110 --> 00:12:53,420
So let's first go down to the gut IP case and the Wi-Fi application task.

162
00:12:59,110 --> 00:13:02,290
And Hugh will say X Event Group set bids.

163
00:13:06,850 --> 00:13:07,810
For the event group.

164
00:13:09,360 --> 00:13:10,950
And then passed the gut IP bit.

165
00:13:14,940 --> 00:13:17,790
Now, let's go down to the user request to disconnect case.

166
00:13:19,370 --> 00:13:21,320
And here, let's say event bits.

167
00:13:23,560 --> 00:13:26,590
Equals X event group get bits.

168
00:13:31,090 --> 00:13:32,140
From our event group.

169
00:13:39,730 --> 00:13:41,000
And now let's say if.

170
00:13:42,170 --> 00:13:46,040
Event bits and the gut IP bid.

171
00:13:52,310 --> 00:13:55,820
Then we'll simply take the call we've already written and inserted here.

172
00:13:58,070 --> 00:13:59,030
All right, so let's cut it.

173
00:14:00,130 --> 00:14:00,880
And pasted here.

174
00:14:04,000 --> 00:14:10,210
OK, so whether we arrive here due to a disconnect button press and the web page or via a Wi-Fi reset

175
00:14:10,210 --> 00:14:16,000
button, press here will check if there is indeed an active connection first before setting the user

176
00:14:16,000 --> 00:14:22,540
request to disconnected, setting the retry number to Max tries, disconnecting Wi-Fi, clearing the

177
00:14:22,540 --> 00:14:25,480
station credentials and changing the LTE status.

178
00:14:25,960 --> 00:14:28,570
So now we need to update the disconnected case below.

179
00:14:28,750 --> 00:14:29,610
So let's go there.

180
00:14:31,290 --> 00:14:37,320
And down here, let's say, if event bits and the gut IP bit.

181
00:14:41,820 --> 00:14:43,430
Then we'll go ahead and clear the bits.

182
00:14:49,290 --> 00:14:52,620
From a prevent group, and it's to gut IP bit.

183
00:14:54,660 --> 00:14:57,150
OK, so now let's go to main that can test this out.

184
00:15:00,090 --> 00:15:03,600
First, let's include the Wi-Fi reset button.

185
00:15:08,830 --> 00:15:10,840
And then here, let's configure.

186
00:15:11,860 --> 00:15:13,210
The wi fi reset button.

187
00:15:15,320 --> 00:15:17,750
And call Wi-Fi reset button config.

188
00:15:21,450 --> 00:15:23,160
OK, now let's build and test it.

189
00:15:38,400 --> 00:15:39,480
And flash, when you're ready.

190
00:15:47,860 --> 00:15:48,910
Then open a monitor.

191
00:15:57,180 --> 00:15:58,620
And then connect to the ESP.

192
00:16:03,300 --> 00:16:04,440
I'm already connected here.

193
00:16:05,900 --> 00:16:07,190
So now go to the Web page.

194
00:16:12,300 --> 00:16:13,740
And then I'll connect the ESPN.

195
00:16:33,330 --> 00:16:35,490
OK, we're connected a refresh here.

196
00:16:36,910 --> 00:16:39,700
And now press the boot button on the dead kid.

197
00:16:41,140 --> 00:16:41,920
And there you have it.

198
00:16:42,280 --> 00:16:47,440
We've disconnected Wi-Fi and the station credentials are cleared, and there's our log message.

199
00:16:50,380 --> 00:16:51,340
And if we refresh.

200
00:16:53,570 --> 00:16:55,190
The connection information goes away.

201
00:16:55,550 --> 00:16:56,030
Nice.

202
00:16:56,690 --> 00:16:59,150
OK, so let's continue our development in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 17: SNTP Time Synchronization

1
00:00:06,990 --> 00:00:10,110
Welcome to the S&amp;P Time Synchronization section.

2
00:00:10,200 --> 00:00:15,330
Here I'll describe the implementation and provide some very brief background information about simple

3
00:00:15,330 --> 00:00:19,980
network time protocol and discuss the relevant esp-idf APIs as well.

4
00:00:21,220 --> 00:00:23,440
So let's get right into the implementation.

5
00:00:25,140 --> 00:00:31,260
Once the ESP 32 has a connection, meaning you've connected to an access point with an internet connection.

6
00:00:31,290 --> 00:00:34,170
The Smtp task Start function will be called.

7
00:00:34,440 --> 00:00:40,620
The task start function will set up the Freertos time synchronization task which will call a function

8
00:00:40,620 --> 00:00:42,510
which obtains the updated time.

9
00:00:42,840 --> 00:00:48,720
Also, I should mention that in this implementation the task will keep synchronizing and checking that

10
00:00:48,720 --> 00:00:50,070
the time is up to date.

11
00:00:50,940 --> 00:00:53,300
Regarding the obtained time function.

12
00:00:53,310 --> 00:00:59,790
This function will initialize the Smtp service to query an Smtp server for the universal time.

13
00:00:59,910 --> 00:01:05,850
Furthermore, the obtained time function will reinitialize in case the time is not up to date.

14
00:01:06,420 --> 00:01:10,980
The local time zone will be set once the Smtp service has been initialized.

15
00:01:11,630 --> 00:01:16,580
The web server will be alerted upon initialization and will respond with the updated time.

16
00:01:23,190 --> 00:01:23,460
All right.

17
00:01:23,460 --> 00:01:27,420
So let's take a look at some additional information about simple network time protocol.

18
00:01:29,520 --> 00:01:31,560
Smtp or simple network time.

19
00:01:31,560 --> 00:01:36,690
Protocol is a protocol designed to synchronize the clock of devices connected to the Internet.

20
00:01:36,810 --> 00:01:39,030
The basic operation is as follows.

21
00:01:39,060 --> 00:01:45,840
The client or ESP 32 connects to the server using the UDP protocol on port 123.

22
00:01:46,080 --> 00:01:48,960
The client transmits a request packet to the server.

23
00:01:49,200 --> 00:01:52,200
Then the server responds with a timestamp packet.

24
00:01:52,700 --> 00:01:56,060
The client can then parse out the current date and time values.

25
00:01:56,180 --> 00:02:02,510
So in general, if the ESP 32 is connected to the internet, it can get the time and date using Smtp.

26
00:02:03,290 --> 00:02:09,500
Also, I should mention that Smtp and the ESP IDF is supported by lightweight IP functions.

27
00:02:11,440 --> 00:02:16,660
Now let's review how the ESP IDF can help us with getting Smtp up and running.

28
00:02:19,020 --> 00:02:22,890
I suggest you review the Smtp documentation from Espressif.

29
00:02:22,920 --> 00:02:28,260
You can find all of the relevant information here as well as some of the functions we'll be using.

30
00:02:29,390 --> 00:02:34,020
Also, I should mention that we'll set the time zone using the following functions here.

31
00:02:34,040 --> 00:02:42,560
Set env we'll use to set the particular time zone and t set to initialize the time zone conversion routine.

32
00:02:42,770 --> 00:02:45,140
More on this in a moment in the next slides.

33
00:02:47,110 --> 00:02:47,410
All right.

34
00:02:47,410 --> 00:02:50,740
So some of this may not come together until we actually start writing the code.

35
00:02:50,770 --> 00:02:53,590
But I think a quick review may help when we actually do that.

36
00:02:54,490 --> 00:02:54,760
All right.

37
00:02:54,760 --> 00:03:01,090
So after the Freertos task kicks off and the obtain time function is called the initialize Smtp function

38
00:03:01,090 --> 00:03:07,480
is called with the first Smtp function is used which configures the client in pull mode to query the

39
00:03:07,480 --> 00:03:09,220
server every n seconds.

40
00:03:09,310 --> 00:03:13,880
The function that accomplishes this is the Smtp set operating mode function.

41
00:03:13,900 --> 00:03:18,610
Using the Smtp up mode pull as the input parameter.

42
00:03:20,560 --> 00:03:25,870
Also within the initialize Smtp function, we'll tell the client which server to use.

43
00:03:25,900 --> 00:03:30,650
A common choice is a cluster of servers from Poole at npr.org.

44
00:03:30,670 --> 00:03:35,470
We'll specify this in the function Smtp set server name.

45
00:03:36,450 --> 00:03:40,530
Then we'll initialize the service using Smtp initialize.

46
00:03:40,830 --> 00:03:46,890
Once that's done, we can then set the time zone variable and initialize the time zone conversion.

47
00:03:47,010 --> 00:03:54,360
We'll set the time zone using the set env function specifying ts for the time zone and your local time

48
00:03:54,360 --> 00:03:55,410
zone string.

49
00:03:55,410 --> 00:04:00,750
And then call the time zone set function to initialize the time zone conversion routine.

50
00:04:04,470 --> 00:04:10,410
After the service is initialized, we'll need to check if the system clock has updated the time to get

51
00:04:10,410 --> 00:04:12,390
the actual time from the system clock.

52
00:04:12,420 --> 00:04:16,590
We'll use the time function which updates the time type variable.

53
00:04:17,250 --> 00:04:21,480
And to split the variable into different time values such as year, month and day.

54
00:04:21,510 --> 00:04:27,810
The local time underscore R function is used which updates the team structure as shown in the image

55
00:04:27,810 --> 00:04:28,380
here.

56
00:04:29,290 --> 00:04:33,220
We'll then check the information from the HTM struct to see if the time was set.

57
00:04:33,310 --> 00:04:35,320
Just like in the image shown below.

58
00:04:38,160 --> 00:04:39,510
All right, so that's enough for now.

59
00:04:39,510 --> 00:04:41,430
Let's get to coding in the next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,190 --> 00:00:10,070
All right, so let's start off by creating a new source file under Maine.

2
00:00:15,280 --> 00:00:17,530
And call it S&amp;P Time Sink.

3
00:00:19,400 --> 00:00:19,910
Gutsy.

4
00:00:22,250 --> 00:00:23,570
And now create a new header file.

5
00:00:27,140 --> 00:00:29,150
And it's S&amp;P time sink.

6
00:00:35,710 --> 00:00:37,300
And now let's go to see make lists.

7
00:00:38,920 --> 00:00:41,350
And let's add here, the S&amp;P time sync.

8
00:00:43,290 --> 00:00:44,100
That see file.

9
00:00:45,620 --> 00:00:47,570
All right, so now we can go to tasks coming.

10
00:00:51,090 --> 00:00:53,580
And here let's go to the very bottom in here.

11
00:00:54,730 --> 00:00:56,080
And let's add the information.

12
00:00:57,050 --> 00:00:59,900
For the S&amp;P Time Sync Task.

13
00:01:03,210 --> 00:01:05,940
And now let's define S&amp;P time sink.

14
00:01:09,770 --> 00:01:12,830
And now a copy this part and its stack size.

15
00:01:14,860 --> 00:01:16,660
And make it four thousand ninety six.

16
00:01:18,620 --> 00:01:21,320
The next defined priority as for.

17
00:01:23,780 --> 00:01:24,740
And the core idea.

18
00:01:26,420 --> 00:01:26,990
As one.

19
00:01:29,350 --> 00:01:30,490
OK, so we're good to go.

20
00:01:31,150 --> 00:01:33,010
So now we can go to the time sink header.

21
00:01:33,960 --> 00:01:36,870
And now here we're going to define a couple of function prototypes.

22
00:01:37,620 --> 00:01:41,910
And first, let's define a prototype that starts the A.P. server.

23
00:01:44,260 --> 00:01:45,550
Synchronization task.

24
00:01:47,800 --> 00:01:51,940
And it's a void S&amp;P time sink Teske start.

25
00:01:53,600 --> 00:01:54,290
And it's void.

26
00:01:58,170 --> 00:02:03,090
OK, now let's define another prototype, which returns local time.

27
00:02:04,020 --> 00:02:07,710
If set and the return is the local time buffer.

28
00:02:14,170 --> 00:02:16,270
OK, so the return is a point to.

29
00:02:17,450 --> 00:02:19,390
And it's S&amp;P time sink.

30
00:02:20,210 --> 00:02:20,870
Get time.

31
00:02:21,960 --> 00:02:22,680
And it's void.

32
00:02:26,320 --> 00:02:27,250
All right, so that's it.

33
00:02:27,790 --> 00:02:29,050
So now we can copy this.

34
00:02:30,360 --> 00:02:32,520
And we can head over to the see file and to find them there.

35
00:02:34,790 --> 00:02:38,330
And let's first just put them here, and I'll clean them up a bit.

36
00:02:45,950 --> 00:02:47,300
All right, so we'll define those later.

37
00:02:47,330 --> 00:02:51,610
Now let's just go up and include here ESP luggage.

38
00:02:53,020 --> 00:02:53,950
And now include.

39
00:02:55,320 --> 00:02:58,110
Free autos slash free auto, Sturridge.

40
00:03:00,060 --> 00:03:01,020
And also include.

41
00:03:02,510 --> 00:03:03,350
Free autos.

42
00:03:04,770 --> 00:03:06,180
Slash task, dunwich.

43
00:03:08,160 --> 00:03:09,090
And next include.

44
00:03:10,410 --> 00:03:14,820
Lightweight IP apps, S.A. Pietrowicz.

45
00:03:16,770 --> 00:03:20,970
And now for our application includes let's include tasks common.

46
00:03:24,490 --> 00:03:25,750
And we also need to include.

47
00:03:27,120 --> 00:03:28,080
FTP server.

48
00:03:30,070 --> 00:03:31,660
We also need to include our.

49
00:03:32,770 --> 00:03:34,240
S&amp;P time sink.

50
00:03:35,200 --> 00:03:35,650
Courage.

51
00:03:37,370 --> 00:03:38,600
And lastly, let's include.

52
00:03:39,590 --> 00:03:41,690
Include the wife at that age.

53
00:03:43,010 --> 00:03:46,070
OK, now I'll just build to resolve these unresolved includes you.

54
00:03:48,560 --> 00:03:49,800
Whoops, I tried to save.

55
00:03:49,820 --> 00:03:52,970
Well, it's building, so that's OK, I'll just let it continue.

56
00:04:05,280 --> 00:04:09,960
OK, so we're back, right, so here, let's do a static const care.

57
00:04:14,440 --> 00:04:16,600
And call it S&amp;P Time Sink.

58
00:04:20,680 --> 00:04:24,610
And because I had prefer having the task start function at the bottom of the file.

59
00:04:25,880 --> 00:04:26,810
I'll just move it there.

60
00:04:28,210 --> 00:04:32,620
And then here we'll use X to create PIN to Core.

61
00:04:35,130 --> 00:04:38,460
And the tax code is a reference to S&amp;P time sink.

62
00:04:40,940 --> 00:04:43,430
And the name is also S&amp;P time sync.

63
00:04:45,610 --> 00:04:49,090
When the stack depth S&amp;P time sync task.

64
00:04:52,610 --> 00:04:53,450
Stack size.

65
00:04:55,100 --> 00:04:56,840
PV parameters are no.

66
00:04:57,980 --> 00:05:02,630
And the priority is as interview time sink to ask priority.

67
00:05:04,860 --> 00:05:10,710
And the test scandal is now in the core idea is the S&amp;P time sync task.

68
00:05:12,110 --> 00:05:12,600
Caller ID.

69
00:05:16,950 --> 00:05:19,950
Now, let's create the S&amp;P Time Sync function.

70
00:05:22,760 --> 00:05:23,730
And let's do it here.

71
00:05:24,710 --> 00:05:28,610
It'll be the soon to be time synchronization task.

72
00:05:31,340 --> 00:05:35,170
And the parameter ARG is a point of variable parameter.

73
00:05:39,150 --> 00:05:40,260
It's a static void.

74
00:05:41,480 --> 00:05:43,130
And it's our time sync task.

75
00:05:44,690 --> 00:05:45,950
And it's a void pointer.

76
00:05:47,020 --> 00:05:47,860
PV Perram.

77
00:05:49,970 --> 00:05:53,360
Now here, let's create an infinite loop and we can use a wild one.

78
00:05:56,210 --> 00:06:01,910
And in here, we'll call the centipede time sink, obtain time function, and we'll define this shortly.

79
00:06:02,270 --> 00:06:06,710
So it's the S&amp;P time sink, obtain time.

80
00:06:11,560 --> 00:06:17,020
And now we can add a delay here and in our implementation, we'll continue checking if the time is updated

81
00:06:17,020 --> 00:06:18,100
based on this delay.

82
00:06:18,760 --> 00:06:23,350
But of course, you can adjust this to your needs, or maybe you even want to kill the task once the

83
00:06:23,350 --> 00:06:24,910
time is up to date, for example.

84
00:06:25,900 --> 00:06:28,030
So here, let's use B tasks delay.

85
00:06:31,550 --> 00:06:34,310
And let's do this every ten thousand milliseconds.

86
00:06:45,000 --> 00:06:51,030
OK, and should the task implementation of a breakout of the above loop, we can call vortex delete.

87
00:06:51,510 --> 00:06:52,350
So let's do that.

88
00:06:54,770 --> 00:06:55,910
In personal to it.

89
00:06:59,740 --> 00:07:02,680
OK, so next, let's define the uptick in time function.

90
00:07:03,920 --> 00:07:05,720
And up here, let's say.

91
00:07:07,170 --> 00:07:08,370
Gets the current time.

92
00:07:09,650 --> 00:07:12,830
And if the current time is not up to date.

93
00:07:15,070 --> 00:07:17,020
The S&amp;P time sync.

94
00:07:18,220 --> 00:07:19,630
And S&amp;P.

95
00:07:20,800 --> 00:07:21,760
Function is called.

96
00:07:26,490 --> 00:07:30,780
And it's a static void up to in time, and it's void.

97
00:07:33,380 --> 00:07:38,510
And first of all, say, time type now equals zero.

98
00:07:39,880 --> 00:07:47,500
And next will create the time infrastructure in here, use struct Tim and call it time info and now

99
00:07:47,500 --> 00:07:48,370
set it to zero.

100
00:07:49,790 --> 00:07:50,390
Like so.

101
00:07:51,800 --> 00:07:56,780
And now we'll call the time function and pass a reference to our time type variable.

102
00:07:56,810 --> 00:07:57,230
Now.

103
00:08:00,260 --> 00:08:05,210
The next use, the local time underscore our function to update the TM structure.

104
00:08:05,280 --> 00:08:08,090
So let's call local time, underscore I.

105
00:08:09,280 --> 00:08:10,600
And pass a reference to now.

106
00:08:11,660 --> 00:08:13,430
And a reference to time info.

107
00:08:17,550 --> 00:08:19,530
All right, so next, we'll check the time.

108
00:08:21,660 --> 00:08:23,790
In case we need to initialize.

109
00:08:25,260 --> 00:08:26,940
Slash re initialize.

110
00:08:29,820 --> 00:08:33,420
So, right, if time info does you.

111
00:08:37,360 --> 00:08:41,620
Is less than twenty sixteen minus 9500.

112
00:08:46,430 --> 00:08:49,100
Then we should S&amp;P time sink.

113
00:08:50,470 --> 00:08:52,150
In it, S&amp;P.

114
00:08:54,320 --> 00:08:58,790
So we'll call this function if the time is not up to date, and we'll define it shortly.

115
00:08:59,180 --> 00:09:02,000
So next, we'll set the local time zone.

116
00:09:04,580 --> 00:09:07,790
And you set envy and specify to.

117
00:09:09,700 --> 00:09:13,630
And now I'll into my time zone, and so you can just into yours as well.

118
00:09:23,480 --> 00:09:25,430
And you could set the last parameter as one.

119
00:09:27,730 --> 00:09:28,090
All right.

120
00:09:28,720 --> 00:09:33,250
So you can check the file that I've attached in the resources and look for your time zone there and

121
00:09:33,250 --> 00:09:34,150
then just enter it here.

122
00:09:35,300 --> 00:09:37,070
OK, next call to set.

123
00:09:39,380 --> 00:09:42,200
And that's to initialize the time zone conversion routine.

124
00:09:43,500 --> 00:09:49,800
OK, so next, we need a global variable here for the S&amp;P operating mode status.

125
00:09:53,140 --> 00:09:57,190
And we need this variable because we only want to set the operating mode once.

126
00:09:57,700 --> 00:09:59,230
So it's a static pool.

127
00:10:01,020 --> 00:10:03,420
S&amp;P Up mode set.

128
00:10:04,690 --> 00:10:05,800
Instead, it's a false.

129
00:10:07,050 --> 00:10:07,550
OK.

130
00:10:07,590 --> 00:10:15,300
And next, let's define the initialize S&amp;P function will come into you, initialize S&amp;P service.

131
00:10:17,080 --> 00:10:21,580
Using S&amp;P Up mode poll mode.

132
00:10:24,390 --> 00:10:26,340
OK, so I'll copy the function.

133
00:10:28,110 --> 00:10:29,580
And here it's static void.

134
00:10:31,440 --> 00:10:32,220
And it's void.

135
00:10:34,750 --> 00:10:37,030
And first, let's S.P. lug.

136
00:10:39,500 --> 00:10:41,000
And say initializing.

137
00:10:44,040 --> 00:10:45,690
The centrepiece service.

138
00:10:50,130 --> 00:10:54,900
Now, right, if not, S&amp;P Up mode said.

139
00:10:57,830 --> 00:11:01,310
So if it's not set, will set the operating mode.

140
00:11:04,550 --> 00:11:11,630
Using S&amp;P set operating mode and then pass S&amp;P Up mode pull.

141
00:11:17,480 --> 00:11:20,600
And then now we can set this variable to true.

142
00:11:24,700 --> 00:11:28,660
And then next, we can call S&amp;P set ServerName.

143
00:11:31,740 --> 00:11:33,330
And the first parameter is zero.

144
00:11:34,460 --> 00:11:37,520
And the second is pool that A.P. talk.

145
00:11:40,960 --> 00:11:44,020
And now we can initialize the servers.

146
00:11:46,210 --> 00:11:48,130
Using S&amp;P in it.

147
00:11:51,000 --> 00:11:54,660
And then we can let the FTP server know.

148
00:11:55,860 --> 00:11:57,300
Service is initialized.

149
00:12:00,240 --> 00:12:02,670
By calling a CTB server monitor.

150
00:12:04,660 --> 00:12:12,790
Send a message and we'll create a new message for this and call it HTP message time service initialized.

151
00:12:18,820 --> 00:12:23,620
All right, so that will be our new message for the FTP server, and we'll define it later.

152
00:12:23,770 --> 00:12:26,260
For now, let's just go to the get time function.

153
00:12:29,020 --> 00:12:35,380
And will return a buffer here, so it needs to be a static care and call it time buffer.

154
00:12:37,240 --> 00:12:41,740
And one hundred bytes should be enough and set it to zero.

155
00:12:45,080 --> 00:12:45,430
All right.

156
00:12:46,010 --> 00:12:47,270
So I'll make a little room here.

157
00:12:52,100 --> 00:12:55,750
Then let's use the time type now instead of two zero.

158
00:12:56,990 --> 00:13:00,050
And we also need our struct. team time info.

159
00:13:01,820 --> 00:13:02,870
And set that to zero.

160
00:13:05,490 --> 00:13:08,610
And then call the time function with a reference to now.

161
00:13:10,210 --> 00:13:12,640
The now called local time underscored our.

162
00:13:13,700 --> 00:13:16,760
In reference now and then reference time for.

163
00:13:19,090 --> 00:13:24,110
Then let's do a check and say if time info that TMU.

164
00:13:26,290 --> 00:13:27,100
Is less than.

165
00:13:28,600 --> 00:13:31,570
Twenty sixteen, minus nineteen hundred.

166
00:13:34,140 --> 00:13:35,370
Then we'll ESP log.

167
00:13:38,160 --> 00:13:39,600
Time is not set yet.

168
00:13:43,590 --> 00:13:44,670
Then they'll say else.

169
00:13:47,420 --> 00:13:49,850
And then now we can call CRF Time.

170
00:13:52,070 --> 00:13:56,960
And this function is similar to aspirin death, which enables formatting the time and date string.

171
00:13:57,140 --> 00:13:59,780
OK, so first we'll do this to the time buffer.

172
00:14:01,230 --> 00:14:02,250
For the size of.

173
00:14:03,580 --> 00:14:04,480
The time buffer.

174
00:14:06,610 --> 00:14:08,530
And then now will format the day.

175
00:14:10,450 --> 00:14:11,050
The month.

176
00:14:13,040 --> 00:14:13,550
The year.

177
00:14:15,280 --> 00:14:16,000
And the hour.

178
00:14:20,490 --> 00:14:21,180
And the second.

179
00:14:24,240 --> 00:14:26,850
OK, and we'll get the information from time info.

180
00:14:31,740 --> 00:14:33,240
And then let's S.P. lug.

181
00:14:35,340 --> 00:14:36,630
The current time info.

182
00:14:42,830 --> 00:14:44,450
From the time buffer.

183
00:14:48,750 --> 00:14:51,480
And then we can return the time buffer.

184
00:14:56,580 --> 00:14:58,410
So now we can copy our new message.

185
00:15:01,310 --> 00:15:04,040
And then let's go define it in the HTTP server header.

186
00:15:06,860 --> 00:15:08,840
And let's just included as a message right here.

187
00:15:13,190 --> 00:15:14,630
All right, so that's it for now.

188
00:15:14,660 --> 00:15:15,950
Let's continue in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,180 --> 00:00:11,350
Now, we'll need to update the Web page files in order to display the time.

2
00:00:11,470 --> 00:00:14,930
So let's start off at the top of index.html.

3
00:00:15,070 --> 00:00:18,490
And under the header here, let's add a new div ID.

4
00:00:21,730 --> 00:00:23,230
And call it local time.

5
00:00:26,820 --> 00:00:28,140
And now let's close it.

6
00:00:31,010 --> 00:00:33,080
And also create a horizontal rule.

7
00:00:34,890 --> 00:00:41,160
And then inside the div let's create an H2 for Smtp time synchronization.

8
00:00:47,170 --> 00:00:48,730
And then make a label for.

9
00:00:51,790 --> 00:00:53,020
For local time.

10
00:00:55,370 --> 00:00:57,290
And right connect to Wi-Fi.

11
00:00:59,180 --> 00:01:00,350
For local time.

12
00:01:02,990 --> 00:01:04,420
Then let's close the label.

13
00:01:07,320 --> 00:01:08,700
Then let's create a div ID.

14
00:01:09,880 --> 00:01:11,080
For the local time.

15
00:01:12,890 --> 00:01:14,210
And then close the div.

16
00:01:17,530 --> 00:01:20,970
So that takes care of our label and our div ID for local time.

17
00:01:20,980 --> 00:01:24,100
So now we can update the styling and app.css.

18
00:01:26,610 --> 00:01:29,610
So let's come here and copy this one.

19
00:01:31,330 --> 00:01:33,010
And let's just pace it up here.

20
00:01:34,350 --> 00:01:36,600
And let's change it to local time.

21
00:01:40,010 --> 00:01:40,940
And that's it.

22
00:01:41,830 --> 00:01:43,990
So now we can go to App.js.

23
00:01:46,130 --> 00:01:49,700
And now go to the top of the file within the ready function.

24
00:01:50,580 --> 00:01:52,260
And we'll call the new function here.

25
00:01:53,960 --> 00:01:56,270
And call it start local time interval.

26
00:02:01,860 --> 00:02:06,270
Okay, so now let's copy this because we're going to define it at the bottom of the file.

27
00:02:09,940 --> 00:02:13,720
And here let's comment that this function sets the interval.

28
00:02:15,210 --> 00:02:16,860
For displaying local time.

29
00:02:20,750 --> 00:02:21,870
You write function.

30
00:02:22,650 --> 00:02:24,330
Start local time interval.

31
00:02:27,120 --> 00:02:29,130
And then here we'll use the set interval.

32
00:02:31,010 --> 00:02:36,350
And then we'll set the interval to call a function to get the local time and we'll call it get local

33
00:02:36,350 --> 00:02:36,920
time.

34
00:02:39,670 --> 00:02:41,710
And we'll call it every 10s.

35
00:02:45,990 --> 00:02:47,460
Okay, so now let's go to find it.

36
00:02:49,670 --> 00:02:52,520
And this function gets the local time.

37
00:02:55,780 --> 00:02:56,830
And I'll make a note.

38
00:02:57,540 --> 00:03:00,330
And say connect the 32.

39
00:03:02,070 --> 00:03:03,330
To the Internet.

40
00:03:03,980 --> 00:03:05,660
And the time will be updated.

41
00:03:11,260 --> 00:03:12,610
And then write function.

42
00:03:14,090 --> 00:03:15,260
Get local time.

43
00:03:19,620 --> 00:03:21,630
And then here we'll use Getjson.

44
00:03:25,120 --> 00:03:27,730
And we'll say forward slash local time.

45
00:03:28,570 --> 00:03:29,590
Dodgson.

46
00:03:30,880 --> 00:03:32,950
Comma function.

47
00:03:33,520 --> 00:03:34,120
Data.

48
00:03:35,340 --> 00:03:36,780
And open the curly braces.

49
00:03:36,810 --> 00:03:40,710
And here we'll specify our div ID local time.

50
00:03:42,740 --> 00:03:44,690
And then say text.

51
00:03:47,220 --> 00:03:48,300
And it's time.

52
00:03:51,480 --> 00:03:51,750
Okay.

53
00:03:51,750 --> 00:03:53,430
And then close it with the semicolon.

54
00:03:55,090 --> 00:03:56,150
And that's it.

55
00:03:56,170 --> 00:03:58,300
And that's all for the Web page programming.

56
00:03:58,300 --> 00:04:01,240
And in the next lesson, we'll continue with the Http server.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,920 --> 00:00:09,350
So let's continue in Http server c.

2
00:00:10,620 --> 00:00:14,550
And here let's include Smtp time sync.

3
00:00:18,050 --> 00:00:21,290
And now let's go down and register a new Uri Handler.

4
00:00:26,380 --> 00:00:28,210
And we'll start by copying this one.

5
00:00:32,220 --> 00:00:34,980
And let's update the comment to local time.

6
00:00:37,410 --> 00:00:40,140
And update the structure to local time.

7
00:00:43,050 --> 00:00:47,850
And the Uri here is local time dot Json.

8
00:00:48,850 --> 00:00:51,700
And the method is http get.

9
00:00:53,440 --> 00:00:56,980
And then update the handler to get local time.

10
00:00:58,620 --> 00:00:59,790
Just like this.

11
00:01:00,460 --> 00:01:02,020
And then let's pass the name.

12
00:01:03,170 --> 00:01:04,460
To register the handler.

13
00:01:05,830 --> 00:01:06,030
Right.

14
00:01:06,030 --> 00:01:07,710
So now let's go to find it up here.

15
00:01:11,490 --> 00:01:13,500
And I'll start by copying this comment.

16
00:01:17,450 --> 00:01:19,310
Then here, I'll change it to local time.

17
00:01:23,600 --> 00:01:24,290
And I'll say here.

18
00:01:24,290 --> 00:01:25,250
Response.

19
00:01:25,820 --> 00:01:27,410
By sending the local time.

20
00:01:31,410 --> 00:01:31,710
Okay.

21
00:01:31,710 --> 00:01:33,510
Now let's go grab the function name.

22
00:01:38,510 --> 00:01:39,470
And then go back.

23
00:01:43,420 --> 00:01:48,700
And then write static esp error type of function name.

24
00:01:49,550 --> 00:01:52,340
And it's Httpd request type.

25
00:01:53,470 --> 00:01:55,450
Pointer, Rick.

26
00:01:59,020 --> 00:02:00,790
And then we'll first plug.

27
00:02:05,160 --> 00:02:05,910
Good time.

28
00:02:06,060 --> 00:02:07,560
Jason requested.

29
00:02:15,790 --> 00:02:17,050
And now we need a care.

30
00:02:17,080 --> 00:02:17,920
Local time.

31
00:02:17,920 --> 00:02:18,700
Jason.

32
00:02:20,490 --> 00:02:21,990
100 byte buffer.

33
00:02:23,070 --> 00:02:24,270
And set it to zero.

34
00:02:26,070 --> 00:02:31,380
And then say if and we'll define a global variable later that we'll use here to check if the time was

35
00:02:31,380 --> 00:02:36,450
set and we'll call it G underscore is local time set?

36
00:02:41,760 --> 00:02:48,420
And if it is set, then here we'll update the Json with the local time and use sprintf into local time

37
00:02:48,420 --> 00:02:49,200
json.

38
00:02:52,460 --> 00:02:53,900
And we'll do the time here.

39
00:03:05,160 --> 00:03:10,950
And then we'll get the time using our git time function and that's Smtp time sync.

40
00:03:17,300 --> 00:03:19,070
And now let's set the response type.

41
00:03:25,190 --> 00:03:26,480
For the request.

42
00:03:27,420 --> 00:03:29,280
As application Json.

43
00:03:33,860 --> 00:03:36,500
And next Httpd response Send.

44
00:03:39,630 --> 00:03:42,240
For the request from the buffer.

45
00:03:43,010 --> 00:03:46,400
For the strlen of the local time Json.

46
00:03:51,950 --> 00:03:53,210
And then let's return.

47
00:03:54,290 --> 00:03:54,920
Spoke.

48
00:03:58,380 --> 00:04:00,750
Okay, so now let's create this global variable.

49
00:04:00,810 --> 00:04:02,070
So let's go up.

50
00:04:07,940 --> 00:04:09,410
And make a comment here.

51
00:04:10,120 --> 00:04:11,680
Local time status.

52
00:04:13,820 --> 00:04:15,260
And it's a static bull.

53
00:04:17,000 --> 00:04:18,290
And set it to false.

54
00:04:20,780 --> 00:04:22,340
And now let's add a case for it.

55
00:04:24,340 --> 00:04:25,630
And we can use this one.

56
00:04:31,840 --> 00:04:32,920
And change it to.

57
00:04:34,020 --> 00:04:36,450
Change it to time service Initialized.

58
00:04:38,320 --> 00:04:40,570
Now let's update the log message as well.

59
00:04:43,520 --> 00:04:48,530
And then change this global variable to global is local time set?

60
00:04:50,750 --> 00:04:52,520
And then here we set it to true.

61
00:04:56,760 --> 00:04:57,030
All right.

62
00:04:57,030 --> 00:04:58,560
So now let's go to Wi-Fi apps.

63
00:05:00,240 --> 00:05:06,360
Because in here I want to create a callback function so that the Smtp time sync task start function

64
00:05:06,360 --> 00:05:12,690
can be called via a custom callback and this will be called when the ESP 32 has an IP address.

65
00:05:12,720 --> 00:05:18,180
So instead of explicitly calling it buried somewhere in the code, we can do it from main and you'll

66
00:05:18,180 --> 00:05:19,870
see how this works once we're done.

67
00:05:19,890 --> 00:05:22,560
So first here, let's comment.

68
00:05:23,100 --> 00:05:23,700
Callback.

69
00:05:23,730 --> 00:05:24,540
TypeDef.

70
00:05:27,420 --> 00:05:28,790
And it's typedef.

71
00:05:30,090 --> 00:05:30,750
Void.

72
00:05:32,840 --> 00:05:34,310
Wi-Fi connected.

73
00:05:35,860 --> 00:05:37,270
Event callback.

74
00:05:38,940 --> 00:05:39,900
Underscore t.

75
00:05:41,690 --> 00:05:42,740
And it's void.

76
00:05:46,360 --> 00:05:46,690
All right.

77
00:05:46,690 --> 00:05:53,680
So this creates a type named wi fi connected event callback, underscore T for a pointer to a function

78
00:05:53,680 --> 00:05:56,230
that takes no arguments and returns nothing.

79
00:05:56,590 --> 00:05:59,620
Okay, so now let's go to the bottom of the file.

80
00:06:01,330 --> 00:06:02,740
And create a prototype.

81
00:06:04,730 --> 00:06:06,890
Which sets the callback function.

82
00:06:11,740 --> 00:06:12,880
And it's a void.

83
00:06:13,780 --> 00:06:16,530
WI fi app set callback.

84
00:06:18,500 --> 00:06:20,900
And it takes the Wi-Fi connected.

85
00:06:22,800 --> 00:06:24,120
Event callback.

86
00:06:27,080 --> 00:06:27,680
CB.

87
00:06:31,860 --> 00:06:36,600
Okay, now let's create another prototype that calls the callback function.

88
00:06:43,260 --> 00:06:46,020
And it'll be a void Wi-Fi app.

89
00:06:47,880 --> 00:06:49,500
Call callback.

90
00:06:51,580 --> 00:06:52,600
And it's void.

91
00:06:55,960 --> 00:06:56,740
Okay, Now let's go.

92
00:06:56,740 --> 00:06:57,820
Define these two.

93
00:07:01,260 --> 00:07:03,090
But first, let's go to the top.

94
00:07:04,290 --> 00:07:10,590
And here, let's write a comment wi fi application callback.

95
00:07:12,250 --> 00:07:13,420
And it's static.

96
00:07:14,220 --> 00:07:16,830
Wi-Fi connected event callback.

97
00:07:19,910 --> 00:07:22,430
And call it WiFi connected event.

98
00:07:24,300 --> 00:07:24,960
CB.

99
00:07:27,280 --> 00:07:27,580
All right.

100
00:07:27,580 --> 00:07:28,120
Looks good.

101
00:07:28,120 --> 00:07:31,630
So let's go down to the bottom where the public functions are.

102
00:07:37,510 --> 00:07:38,710
And let's define them here.

103
00:07:42,820 --> 00:07:44,590
And for the set callback.

104
00:07:45,560 --> 00:07:47,700
We'll just set our wi fi connected event.

105
00:07:54,990 --> 00:07:58,650
To the callback passed to the function and that's just CB.

106
00:08:00,960 --> 00:08:01,730
That's it.

107
00:08:01,740 --> 00:08:03,840
Okay, so next, let's go define this one.

108
00:08:08,960 --> 00:08:11,240
And here we'll just call the callback.

109
00:08:18,210 --> 00:08:18,990
Like so.

110
00:08:20,760 --> 00:08:23,010
Now let's go up to the God IP case.

111
00:08:27,410 --> 00:08:28,910
And let's first comment.

112
00:08:29,270 --> 00:08:31,160
Check for connection callback.

113
00:08:35,080 --> 00:08:38,650
And say if wi fi connected event callback.

114
00:08:43,710 --> 00:08:46,100
Then call wi fi app.

115
00:08:46,740 --> 00:08:47,970
Call callback.

116
00:08:50,510 --> 00:08:53,720
All right, So if the callback is set, then we call the callback.

117
00:08:54,140 --> 00:08:56,000
Okay, so let's go to Main.c.

118
00:08:58,340 --> 00:09:00,020
And first, let's include.

119
00:09:00,750 --> 00:09:01,860
ESP log.

120
00:09:07,030 --> 00:09:08,830
And then let's also include.

121
00:09:10,800 --> 00:09:11,290
Smtp.

122
00:09:11,340 --> 00:09:12,240
Time Sync.

123
00:09:17,450 --> 00:09:18,350
And then here.

124
00:09:19,160 --> 00:09:20,360
It will create a tag.

125
00:09:26,110 --> 00:09:27,220
And call it main.

126
00:09:29,620 --> 00:09:35,230
And next we'll create our callback as Floyd Wi-Fi Application Connected Events.

127
00:09:38,780 --> 00:09:39,830
And it's void.

128
00:09:42,930 --> 00:09:45,030
And then here we'll log.

129
00:09:47,780 --> 00:09:49,730
Wi-Fi application connected.

130
00:09:56,000 --> 00:10:00,020
And then now we can call Smtp time sync.

131
00:10:02,540 --> 00:10:03,590
Tasks start.

132
00:10:06,600 --> 00:10:09,570
And let's proceed by setting this function as our callback.

133
00:10:09,570 --> 00:10:10,680
So copy it.

134
00:10:12,790 --> 00:10:16,710
And then down here we'll set connected event callback.

135
00:10:20,250 --> 00:10:22,110
Using our Wi-Fi app.

136
00:10:23,010 --> 00:10:24,210
Set callback.

137
00:10:25,080 --> 00:10:27,750
And pass a reference to the function name.

138
00:10:31,250 --> 00:10:32,120
And that's it.

139
00:10:32,120 --> 00:10:33,080
So let's build.

140
00:10:38,600 --> 00:10:39,670
The flesh.

141
00:10:48,320 --> 00:10:49,460
Then open a monitor.

142
00:11:02,680 --> 00:11:04,090
And then connect to the ISP.

143
00:11:11,620 --> 00:11:13,480
And go to the Web page with Chrome.

144
00:11:21,550 --> 00:11:22,810
Now connect the ISP.

145
00:11:40,920 --> 00:11:41,940
And let's see.

146
00:11:50,730 --> 00:11:51,360
Nice.

147
00:11:51,360 --> 00:11:53,010
The local time is already displayed.

148
00:11:53,010 --> 00:11:53,940
That's great.

149
00:11:54,180 --> 00:11:56,640
And the monitor shows the message from Main.

150
00:11:57,850 --> 00:12:00,190
And all the expected messages that follow.

151
00:12:04,130 --> 00:12:06,590
So let's do some more programming in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 18: Displaying the ESP32's Access Point SSID on the Web Page


1
00:00:07,000 --> 00:00:13,210
In the last lesson, we added the local time to the web page, and in this lesson we'll send the Esp32

2
00:00:13,540 --> 00:00:19,990
side to the page and we'll handle this in a similar manner as we did for the local time so we can copy

3
00:00:19,990 --> 00:00:21,460
this block of HTML.

4
00:00:23,240 --> 00:00:26,660
And we can put it wherever we like, but I'll put it right up here.

5
00:00:29,910 --> 00:00:30,150
Okay.

6
00:00:30,150 --> 00:00:33,510
And let's update the div to esp sid.

7
00:00:36,310 --> 00:00:37,600
And the age to.

8
00:00:39,300 --> 00:00:41,850
Two ESP 32 CID.

9
00:00:43,260 --> 00:00:49,050
In the label to ape underscore sid and the div ID as well.

10
00:00:51,940 --> 00:00:53,350
And let's change the label.

11
00:00:55,620 --> 00:00:57,120
Two access point.

12
00:00:58,630 --> 00:00:59,200
Sad.

13
00:01:01,350 --> 00:01:02,190
And that's it.

14
00:01:02,190 --> 00:01:04,170
So let's go to ABC's.

15
00:01:06,530 --> 00:01:08,000
And then copy this one.

16
00:01:10,090 --> 00:01:11,080
And paste.

17
00:01:12,340 --> 00:01:15,550
And update the ID to AP id.

18
00:01:16,680 --> 00:01:17,640
And that's all.

19
00:01:17,970 --> 00:01:19,920
So let's go to App.js.

20
00:01:22,100 --> 00:01:23,180
And let's go up.

21
00:01:23,810 --> 00:01:29,240
To the document ready function and we'll let a new function and we'll call it get sed.

22
00:01:32,980 --> 00:01:34,300
And now we'll go define it.

23
00:01:39,100 --> 00:01:40,270
And comment.

24
00:01:40,960 --> 00:01:42,490
Gets the ESP 32.

25
00:01:44,350 --> 00:01:45,850
Access point, Sid.

26
00:01:47,600 --> 00:01:49,460
For displaying on the web page.

27
00:01:53,050 --> 00:01:55,750
And its function get sed.

28
00:01:59,120 --> 00:02:00,680
And use Getjson.

29
00:02:01,670 --> 00:02:06,440
And specify forward slash AP sid dot json.

30
00:02:08,600 --> 00:02:10,100
Comma function.

31
00:02:12,640 --> 00:02:14,380
And open the curly braces.

32
00:02:16,030 --> 00:02:19,390
And our ID is app underscore id.

33
00:02:20,860 --> 00:02:22,960
Dot text data.

34
00:02:23,880 --> 00:02:25,410
And we'll call it Sid.

35
00:02:29,050 --> 00:02:30,190
Add the semicolon.

36
00:02:31,580 --> 00:02:33,410
And let's go create the Uri Handler.

37
00:02:36,260 --> 00:02:37,520
So let's go down.

38
00:02:40,220 --> 00:02:41,660
And let's copy this one.

39
00:02:43,230 --> 00:02:44,340
And paste it.

40
00:02:45,880 --> 00:02:48,480
And change this to AP sed.

41
00:02:49,920 --> 00:02:51,060
And here as well.

42
00:02:53,600 --> 00:02:57,800
And the Uri is AP sid Json.

43
00:02:58,620 --> 00:03:03,300
And then we just need to update the handler name to get app ID.

44
00:03:05,190 --> 00:03:08,190
And I'll copy the struct name and register it.

45
00:03:09,860 --> 00:03:10,550
All right, Now let's go.

46
00:03:10,550 --> 00:03:11,570
Define the handler.

47
00:03:14,850 --> 00:03:16,530
And we'll take this comment.

48
00:03:19,800 --> 00:03:22,230
And we'll change this to a side.

49
00:03:24,290 --> 00:03:27,890
And it responds by sending the AP CID.

50
00:03:32,300 --> 00:03:33,830
Now, let's go grab the name.

51
00:03:40,520 --> 00:03:41,750
And it's static.

52
00:03:42,600 --> 00:03:43,910
ESP error type.

53
00:03:45,210 --> 00:03:51,000
Our handler and it's httpd request type pointer req.

54
00:03:52,390 --> 00:03:54,190
And we'll plug info.

55
00:03:57,160 --> 00:03:59,980
AP sid Json requested.

56
00:04:03,610 --> 00:04:04,840
And we need a care.

57
00:04:05,550 --> 00:04:06,400
Jason.

58
00:04:07,290 --> 00:04:09,210
And 50 bytes should be enough.

59
00:04:11,530 --> 00:04:14,500
And then we need the wi fi config type pointer.

60
00:04:15,850 --> 00:04:17,470
Call it wi fi config.

61
00:04:18,180 --> 00:04:20,300
And we'll get that with wi fi app.

62
00:04:20,310 --> 00:04:21,870
Get wi fi config.

63
00:04:24,550 --> 00:04:27,370
And then we'll use the ESP Wi-Fi get.

64
00:04:28,680 --> 00:04:29,580
Config.

65
00:04:31,640 --> 00:04:35,450
And pass the ISP interface Wi-Fi app.

66
00:04:37,430 --> 00:04:39,650
And then let's pass our Wi-Fi config.

67
00:04:43,580 --> 00:04:46,640
And now we want to extract the Ssid from the config.

68
00:04:46,820 --> 00:04:50,330
So let's create a pointer ssid.

69
00:04:52,000 --> 00:04:54,670
And now we'll carry pointer typecast.

70
00:04:55,950 --> 00:04:57,570
For the wi fi config.

71
00:04:59,160 --> 00:05:00,540
And we want the app.

72
00:05:02,350 --> 00:05:02,980
Sid.

73
00:05:07,000 --> 00:05:10,420
And now we can print f into sed json.

74
00:05:14,660 --> 00:05:16,370
For the side here.

75
00:05:25,310 --> 00:05:27,950
And that comes from our side variable.

76
00:05:29,610 --> 00:05:31,320
And then set the response type.

77
00:05:36,230 --> 00:05:39,290
For the request as application Json.

78
00:05:43,040 --> 00:05:45,680
And then Httpd response Send.

79
00:05:47,810 --> 00:05:55,100
For the request from sid json for the str Len of sid json.

80
00:05:56,850 --> 00:05:59,190
And then we can return ESP.

81
00:05:59,280 --> 00:05:59,660
Okay.

82
00:06:01,270 --> 00:06:07,000
So here we use the esp Wi-Fi git config to get the information about the access point.

83
00:06:07,000 --> 00:06:14,590
And from that information we extracted the Ssid into a separate variable called Ssid and then we printed

84
00:06:14,590 --> 00:06:18,730
that into our Json buffer and sent this as a response.

85
00:06:19,810 --> 00:06:20,500
All right.

86
00:06:20,500 --> 00:06:23,710
So let's see how this looks on the Web page and build the project.

87
00:06:26,980 --> 00:06:28,120
And they'll flash it.

88
00:06:36,570 --> 00:06:37,980
And open the monitor.

89
00:06:51,710 --> 00:06:53,720
And I will get the Web page ready.

90
00:06:56,380 --> 00:06:56,620
Then.

91
00:06:56,620 --> 00:06:57,760
Now I can connect.

92
00:07:03,310 --> 00:07:05,350
Now, I'll open the Web page.

93
00:07:07,020 --> 00:07:07,980
And great.

94
00:07:08,010 --> 00:07:10,710
The access point ID is displayed right here.

95
00:07:12,560 --> 00:07:17,780
So this is how we can create a simple wireless local area network application and display various data

96
00:07:17,780 --> 00:07:21,350
on a web page and respond to these requests via a web server.

97
00:07:23,400 --> 00:07:23,670
All right.

98
00:07:23,670 --> 00:07:25,530
So I really hope you enjoyed these lessons.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================


# Section 19: AWS IoT

1
00:00:07,100 --> 00:00:10,310
Hello and welcome to the Amazon Web Services Iot section.

2
00:00:10,850 --> 00:00:16,670
In this section, we'll configure the project to enable communication with a US Iot core, which is

3
00:00:16,670 --> 00:00:20,240
a cloud service that will allow us to communicate with the ISP from anywhere.

4
00:00:20,630 --> 00:00:27,260
And in our implementation, we'll go through the basic processes of Iot core and from the AWG dashboard

5
00:00:27,260 --> 00:00:32,720
we'll subscribe to and publish the temperature and humidity sensor data as well as the received signal

6
00:00:32,720 --> 00:00:34,550
strength of our local Wi-Fi connection.

7
00:00:35,390 --> 00:00:41,210
Okay, so in this lesson, I'll just provide a high level brief introduction to a WSI Iot core, and

8
00:00:41,210 --> 00:00:46,490
then I'll share some a WC Iot core resources that are beneficial when first getting started, which

9
00:00:46,490 --> 00:00:49,070
should also help with clarifying more technical details.

10
00:00:49,550 --> 00:00:53,960
And just as a heads up in the next lesson, I'll discuss a few technical topics that should provide

11
00:00:53,960 --> 00:00:55,130
even more clarification.

12
00:00:55,490 --> 00:01:01,760
I'll also mention the ESP, AWB Iot SDK, which will integrate into the project and also provide the

13
00:01:01,760 --> 00:01:03,590
AWB account setup link.

14
00:01:04,070 --> 00:01:08,690
And then at the end I'll mention the steps it will take for our public subscribed implementation and

15
00:01:08,690 --> 00:01:11,090
testing using the MQ t test client.

16
00:01:11,330 --> 00:01:11,600
All right.

17
00:01:11,600 --> 00:01:18,410
So for now, let's continue with the AWB Safety Overview and to visualize AWB Iot Communication at a

18
00:01:18,410 --> 00:01:19,430
very basic level.

19
00:01:19,760 --> 00:01:25,220
We'll have our thing as it's called in AWB, which is our device that will connect to the cloud via

20
00:01:25,220 --> 00:01:33,170
AWB Iot core using the NQT protocol, which is a lightweight published subscribe protocol compatible

21
00:01:33,170 --> 00:01:34,850
with a society.

22
00:01:35,390 --> 00:01:36,620
I'll touch on this more in a bit.

23
00:01:37,640 --> 00:01:41,390
Now let's review some basic information about a U.S. Safety Corps.

24
00:01:42,230 --> 00:01:48,920
The U.S. Safety Corps is a platform that connects Iot devices to US, Iot services.

25
00:01:49,370 --> 00:01:53,600
And to get started, let's go through some key resources for US safety.

26
00:01:54,260 --> 00:02:00,050
And I would first suggest that you follow this link to the US Iot Getting Started page as it's worth

27
00:02:00,050 --> 00:02:05,960
going through all of this information because there's much to learn regarding a society, which is why

28
00:02:05,960 --> 00:02:12,500
I also suggest going to the learn more about a website link and bookmarking it for future reference.

29
00:02:13,510 --> 00:02:18,670
And if you're looking for additional resources regarding technical aspects, I also suggest watching

30
00:02:18,670 --> 00:02:24,910
this introduction to a WSU tee and just follow the link and you can log in with your Amazon account.

31
00:02:25,540 --> 00:02:29,890
And this is a really good introduction to the basics where each of these components are described.

32
00:02:30,340 --> 00:02:35,200
And in fact, I would even come back to this after we've completed the project setup if you really want

33
00:02:35,200 --> 00:02:35,920
to nail it down.

34
00:02:36,610 --> 00:02:38,920
However, for now, let's just continue with the basics here.

35
00:02:39,610 --> 00:02:47,350
A WSU core includes the device gateway, which enables devices to communicate with a WSU securely and

36
00:02:47,350 --> 00:02:49,150
efficiently in the device.

37
00:02:49,150 --> 00:02:58,060
Gateway supports NQT web sockets and HTTP 1.1 protocols, and the device Gateway hosts a message broker

38
00:02:58,660 --> 00:03:02,920
which connects and processes messages between your Iot device and the cloud.

39
00:03:03,610 --> 00:03:09,040
The message broker is a published subscribe broker service that allows you to send messages addressed

40
00:03:09,040 --> 00:03:13,210
to a topic like the topic I've created here, which we'll use later.

41
00:03:16,550 --> 00:03:21,830
So the act of sending the message is referred to as publishing and the act of registering to receive

42
00:03:21,830 --> 00:03:25,490
messages for a topic filter is referred to as subscribing.

43
00:03:26,180 --> 00:03:33,230
And in this course we'll use the muted test client here to monitor muted messages being passed into

44
00:03:33,230 --> 00:03:36,440
Amazon Web Services accounts from the ESP 32.

45
00:03:37,280 --> 00:03:44,300
So the ESP 32 will publish imputed messages that are identified by topic to communicated state to a

46
00:03:44,310 --> 00:03:51,980
WSU team and will also subscribe to messages on the ESP 32 side and test sending them using the published

47
00:03:51,980 --> 00:03:53,390
to a topic option here.

48
00:03:54,110 --> 00:04:00,830
So publishing and subscribing using the MQ test client is a good way to get started with a society.

49
00:04:01,070 --> 00:04:03,770
And once you've done this, you can then dive deeper on your own.

50
00:04:04,800 --> 00:04:06,900
And just briefly about nQt.

51
00:04:07,440 --> 00:04:13,920
nQt is a lightweight, published subscribed network protocol that transports messages between devices.

52
00:04:14,340 --> 00:04:21,390
To learn more about Iot core communication protocols and the details of each, you can use the FWC Iot

53
00:04:21,540 --> 00:04:27,030
device communication protocols link here where you can examine the details and capabilities of each.

54
00:04:30,500 --> 00:04:36,230
And the next link is quite useful for learning more about using MQ with a society.

55
00:04:37,520 --> 00:04:41,030
And you'll find that there are two different levels of quality of service available.

56
00:04:41,690 --> 00:04:47,750
Quality of service level zero messages are sent zero or more times and should be used for messages that

57
00:04:47,750 --> 00:04:52,040
are sent over reliable communication links or that can be missed without a problem.

58
00:04:52,790 --> 00:04:59,060
And quality of service level one messages are sent at least one time and then repeatedly until the public

59
00:04:59,060 --> 00:05:00,170
response is received.

60
00:05:00,980 --> 00:05:05,600
And you'll see how the different quality of service options are used and implemented in the source code.

61
00:05:06,880 --> 00:05:12,760
Now let's take a look at how we're going to enable AWG sale TE Core communication on the ESB 32.

62
00:05:13,600 --> 00:05:20,110
So of course we're going to use IWC or TE, but I wanted to point out that SB 32 supports multiple cloud

63
00:05:20,110 --> 00:05:20,710
frameworks.

64
00:05:21,250 --> 00:05:25,360
So if you're interested, you can follow the additional links here to get started with the basics for

65
00:05:25,360 --> 00:05:26,500
any of these frameworks.

66
00:05:26,860 --> 00:05:31,420
For example, Google Iot provides its own examples that you can get started with.

67
00:05:32,200 --> 00:05:34,840
And they provide a getting started guide for theirs as well.

68
00:05:35,470 --> 00:05:35,830
All right.

69
00:05:35,830 --> 00:05:37,240
So that's all I'll mention about that.

70
00:05:37,300 --> 00:05:39,160
Now let's go back to IWC.

71
00:05:39,430 --> 00:05:47,080
The ESP 32 IWC sale team is based on Amazon Web Services, Iot Device SDK and embedded.

72
00:05:47,080 --> 00:05:51,370
See which you can find here and we'll set this up in the next lesson.

73
00:05:51,730 --> 00:05:54,970
But first, you'll need to set up your IWC Iot account.

74
00:05:56,340 --> 00:05:57,720
So let's review the process.

75
00:05:58,440 --> 00:06:00,510
You can use the link here to set up your account.

76
00:06:00,840 --> 00:06:03,600
And the process is the typical registration process.

77
00:06:04,170 --> 00:06:09,600
You'll just provide your email address and create an account name, confirm it and create a password,

78
00:06:09,870 --> 00:06:15,270
and then into your name, phone number and address and credit card information for identity verification

79
00:06:15,270 --> 00:06:15,900
purposes.

80
00:06:16,380 --> 00:06:18,690
And then you'll see a message like this when doing so.

81
00:06:19,550 --> 00:06:22,850
And then you may need to verify your identity with your phone number as well.

82
00:06:23,210 --> 00:06:25,520
And the whole process should take around 5 minutes.

83
00:06:26,060 --> 00:06:30,620
And I'll also just mention that when I signed up, I chose the basic support free plan.

84
00:06:31,070 --> 00:06:33,350
And you could check out details when you get to this part.

85
00:06:34,100 --> 00:06:38,090
And then once you're done, you can always get back to the management console via the link here.

86
00:06:38,510 --> 00:06:40,610
So feel free to bookmark this one as well.

87
00:06:42,100 --> 00:06:45,520
Now let's talk about the implementation and configuration steps that we'll take.

88
00:06:46,030 --> 00:06:52,720
First, we're going to clone the ESP WC Iot repository and add it to the project by updating the CE

89
00:06:52,720 --> 00:06:54,850
make list file in the project directory.

90
00:06:55,180 --> 00:06:59,530
And then we'll add the template files that are provided in the resources for this section and we'll

91
00:06:59,530 --> 00:07:05,200
include them into the project build by updating the CE make list file under the main folder and then

92
00:07:05,200 --> 00:07:10,960
we'll go into the Iot core management console and create a thing in Amazon Web Services.

93
00:07:11,110 --> 00:07:17,170
And we'll also create a policy and attach it to the device certificate and then we'll generate the certificates

94
00:07:17,170 --> 00:07:22,780
in public and private keys, and then we'll need to add the certificates and private key as embedded

95
00:07:22,780 --> 00:07:24,400
components on the East Side.

96
00:07:24,790 --> 00:07:32,560
Then we'll update the source code to accommodate the AWG Iot Freitas task and adding the Iot core component

97
00:07:32,890 --> 00:07:37,960
will increase our application size, so we'll need to adjust the partition table accordingly.

98
00:07:38,320 --> 00:07:44,350
Well then update the SDK config to include the device data endpoint from your Amazon Web Services account.

99
00:07:44,680 --> 00:07:50,290
And then we can flash to the ESB 32 connected to the Internet and subscribe and publish data to and

100
00:07:50,290 --> 00:07:52,000
from the RWC dashboard.

101
00:07:52,510 --> 00:07:57,070
And I also just want to mention that we'll use our connected event callback function and main that C

102
00:07:57,340 --> 00:08:04,150
to start the US Iot free task as we want to kick off that task when the ESP is connected to the internet.

103
00:08:04,570 --> 00:08:09,970
And as a second step we'll get the received signal strength indicator of the Wi-Fi connection using

104
00:08:09,970 --> 00:08:17,260
the ESP Wi-Fi to get AP info API and will publish it to a WSU team.

105
00:08:17,860 --> 00:08:22,330
This will enable you to monitor the health of the connection from anywhere and then also will publish

106
00:08:22,330 --> 00:08:23,980
the temperature and humidity sensor data.

107
00:08:25,210 --> 00:08:29,350
All right, so be sure to set up UAW Society Core Account and LC as soon.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,150 --> 00:00:13,080
In this lesson, we'll review a few technical details about the basic processes of a society, and this

2
00:00:13,080 --> 00:00:16,170
will prepare us for the next lessons where we carry out the implementation.

3
00:00:16,890 --> 00:00:23,880
So in this briefing, we'll review a bit more about Kuti as well as the basics of a WC Iot authentication.

4
00:00:24,180 --> 00:00:27,960
And we'll also take a look at mutual TLS or MTA less for short.

5
00:00:28,260 --> 00:00:33,030
And then we'll take a look at a WC security in touch on the device certificates and keys.

6
00:00:33,480 --> 00:00:38,910
And that will lead us into the WC Iot policies, which will then segway us into JSON.

7
00:00:39,150 --> 00:00:40,170
So let's dive right in.

8
00:00:41,010 --> 00:00:42,900
Okay, now back to empty.

9
00:00:43,320 --> 00:00:46,560
Empty stands for MQ Telemetry Transport.

10
00:00:46,920 --> 00:00:51,720
And again, it's a simple lightweight messaging protocol designed for resource constrained devices on

11
00:00:51,720 --> 00:00:52,680
constrained networks.

12
00:00:53,280 --> 00:00:56,310
And muted is the standard for Iot messaging.

13
00:00:57,060 --> 00:01:02,400
And it's used because it requires minimal resources and network bandwidth while ensuring reliability

14
00:01:02,400 --> 00:01:04,350
and some degree of delivery assurance.

15
00:01:05,100 --> 00:01:11,670
And this is what makes mq t ideal in machine to machine or internet of Things connected devices where

16
00:01:11,670 --> 00:01:13,860
both bandwidth and battery power can be limited.

17
00:01:15,110 --> 00:01:22,190
So MQ t uses a client server model where every Iot device is a client and is connected to a server called

18
00:01:22,190 --> 00:01:26,030
an NQT broker, like an AWB Stewart, for example.

19
00:01:26,360 --> 00:01:30,560
So in this model, clients send messages to an address called a topic.

20
00:01:30,860 --> 00:01:35,660
Then the MQ broker will forward that message to all clients subscribed to that topic.

21
00:01:36,110 --> 00:01:41,330
For example, here we have Thing X which publishes the lead on status to the lead topic.

22
00:01:41,660 --> 00:01:46,850
The MQ broker then forwards the lead on status message to the thing y and things.

23
00:01:46,850 --> 00:01:50,000
The clients which are both subscribed to the lead topic.

24
00:01:51,550 --> 00:01:51,870
Okay.

25
00:01:51,880 --> 00:01:59,140
Now let's take a look at a WSI Iot device authentication basics, a WC Iot devices authenticated using

26
00:01:59,140 --> 00:02:08,560
mutual TLS authentication with x509 certificates and then cryptography x509 is an International Telecommunication

27
00:02:08,560 --> 00:02:12,190
Union standard defining the format of public key certificates.

28
00:02:12,610 --> 00:02:17,200
So once the certificate is provisioned inactivated, it can be installed on a device.

29
00:02:17,470 --> 00:02:23,710
The device will then use that certificate for all requests to a society and we're going to generate

30
00:02:23,710 --> 00:02:28,990
the required certificates in a WC and embed them into the ESP 32 in the next lesson.

31
00:02:29,650 --> 00:02:32,400
Now let's cover mutual TLS MTA.

32
00:02:32,470 --> 00:02:37,300
Less is used to establish trust between two parties and ensures that the parties at each end of the

33
00:02:37,300 --> 00:02:38,920
network are who they claim to be.

34
00:02:39,220 --> 00:02:44,230
By verifying that they both have the correct private key and the information in their respective TLS

35
00:02:44,230 --> 00:02:46,750
certificates provides additional verification.

36
00:02:47,200 --> 00:02:51,970
And we see later that we did what's called a root certificate, authority certificate, and the root

37
00:02:51,970 --> 00:02:58,120
TLS certificate is necessary for MTA less, and this enables an organization to be their own certificate

38
00:02:58,120 --> 00:02:58,690
authority.

39
00:02:59,140 --> 00:03:04,240
The certificates used by authorized clients and servers have to correspond to the root certificate,

40
00:03:04,570 --> 00:03:09,520
and this root certificate is self signed, meaning that the organization creates it themselves.

41
00:03:10,060 --> 00:03:14,530
And again, in the next lesson we'll download the root CAA directly from a WC.

42
00:03:15,220 --> 00:03:21,910
And in the case of a WC, they provide the device certificates and keys as A.W. as the certificate authority

43
00:03:21,910 --> 00:03:23,080
for Iot devices.

44
00:03:23,410 --> 00:03:28,660
So in this scenario, the certificates and keys are installed on the device and the device will use

45
00:03:28,660 --> 00:03:32,950
that certificate and key to authenticate itself with a society.

46
00:03:33,310 --> 00:03:39,370
Additionally, in this scenario, to perform a WSOP operations with your device, you must create an

47
00:03:39,370 --> 00:03:45,370
AWG Iot policy and attach it to your device certificate and we'll go through this process in the next

48
00:03:45,370 --> 00:03:45,790
lesson.

49
00:03:45,970 --> 00:03:50,650
Now let's discuss the policies so about the US Iot policies.

50
00:03:51,010 --> 00:03:56,830
These policies are JSON documents that authorize your device for performing AWG Iot operations.

51
00:03:57,160 --> 00:04:03,190
IWC IOT defines a set of policy actions describing the operations and resources for which you can grant

52
00:04:03,190 --> 00:04:04,210
or deny access.

53
00:04:04,540 --> 00:04:06,250
And here are just a couple of examples.

54
00:04:06,550 --> 00:04:13,300
Iot Connect represents permission to connect to an Iot message broker and Iot subscribe represents permission

55
00:04:13,300 --> 00:04:16,360
to connect to an empty topic or topic filter.

56
00:04:16,750 --> 00:04:22,900
So the policy document is in JSON or JavaScript object notation, which is an open standard lightweight

57
00:04:22,900 --> 00:04:24,280
data interchange format.

58
00:04:24,610 --> 00:04:29,470
And as a text document, it's easier for users to read and write and for machines to parse and generate.

59
00:04:29,740 --> 00:04:34,690
And we'll also do this in the next lesson, but we don't have to create the JSON policy document manually.

60
00:04:35,020 --> 00:04:38,140
We'll use the builder here and allow each action to then.

61
00:04:39,410 --> 00:04:39,710
Okay.

62
00:04:39,710 --> 00:04:41,180
So let's continue in the next lesson.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,940 --> 00:00:07,250
Okay.

2
00:00:07,270 --> 00:00:13,180
Be sure that your account is set up and open the github page for esp rwc iot.

3
00:00:14,170 --> 00:00:19,180
Because now we're going to clone this repository and we're going to use this command here.

4
00:00:20,110 --> 00:00:22,210
So let's copy it using this button.

5
00:00:24,280 --> 00:00:26,020
And then let's go to the workspace folder.

6
00:00:28,580 --> 00:00:30,440
Now right click on the project folder.

7
00:00:31,300 --> 00:00:33,040
And let's go to get here.

8
00:00:34,300 --> 00:00:35,440
Which is right here.

9
00:00:35,680 --> 00:00:36,100
Okay.

10
00:00:38,520 --> 00:00:40,440
And then let me pull it back into view.

11
00:00:43,710 --> 00:00:47,400
Now let's insert the command that we've copied and hit enter.

12
00:00:49,670 --> 00:00:50,730
And just let it finish.

13
00:00:50,750 --> 00:00:52,160
I'll speed up the video a bit here.

14
00:01:25,840 --> 00:01:26,110
Okay.

15
00:01:26,110 --> 00:01:26,950
Now we can close.

16
00:01:26,960 --> 00:01:27,580
Get back.

17
00:01:30,130 --> 00:01:33,250
And here is the ESPN Society.

18
00:01:33,460 --> 00:01:34,360
So let's take a look.

19
00:01:36,600 --> 00:01:40,380
And this is the embedded C, a society device SDK.

20
00:01:40,710 --> 00:01:42,240
So let's go in here and take a look around.

21
00:01:43,700 --> 00:01:47,660
You can find the include files here and the source files here as well.

22
00:01:48,410 --> 00:01:52,190
And if we go back to ESP a WC Iot folder.

23
00:01:53,710 --> 00:01:56,290
Here, you'll find the examples that you can get started with.

24
00:01:57,370 --> 00:02:01,330
And this is the subscribe publish example and in the main folder.

25
00:02:02,480 --> 00:02:02,990
The file.

26
00:02:02,990 --> 00:02:05,270
Here is what I've based the code on in the resources.

27
00:02:07,150 --> 00:02:07,480
Okay.

28
00:02:07,480 --> 00:02:12,700
So now we'll continue in the Eclipse A.D. And now I'm just getting back to the project folder.

29
00:02:15,800 --> 00:02:20,360
Because next we'll need to include the esp nws iot into the build.

30
00:02:21,020 --> 00:02:22,700
So now let's switch over to Eclipse.

31
00:02:23,980 --> 00:02:29,200
And let's go to the C make list file in the project directory here and we'll tell C make where to find

32
00:02:29,200 --> 00:02:30,550
a society.

33
00:02:31,210 --> 00:02:32,620
So here, let's write set.

34
00:02:32,890 --> 00:02:35,740
And in parentheses, it's extra.

35
00:02:36,790 --> 00:02:37,510
Component.

36
00:02:38,790 --> 00:02:39,390
Dears.

37
00:02:40,440 --> 00:02:40,790
Okay.

38
00:02:40,800 --> 00:02:49,020
And then in quotations it's ISP, dash, FWC, dash, Iot and close parentheses.

39
00:02:49,890 --> 00:02:51,360
And then control this to save.

40
00:02:52,050 --> 00:02:54,240
All right, now let's include the resource files.

41
00:02:54,450 --> 00:02:55,440
So have yours ready.

42
00:02:56,190 --> 00:02:57,090
Minor right here.

43
00:02:58,260 --> 00:03:00,420
And I'll just control C to copy them.

44
00:03:01,580 --> 00:03:04,580
And then let's go to the main folder and paste them in.

45
00:03:07,460 --> 00:03:11,210
And now you need to add the source file to the main CMA list file here.

46
00:03:12,790 --> 00:03:14,260
So now let's add it to the list.

47
00:03:15,350 --> 00:03:19,370
And that's the IWC, IATA, that IATSE.

48
00:03:20,890 --> 00:03:21,610
And save that.

49
00:03:23,060 --> 00:03:27,140
Next, we'll need to go to a website and generate the certificates.

50
00:03:27,590 --> 00:03:30,410
But while we're here, let's create a folder for the certificates.

51
00:03:31,100 --> 00:03:34,130
So under the main folder, let's create a new folder.

52
00:03:37,750 --> 00:03:38,890
And call it certs.

53
00:03:41,960 --> 00:03:44,960
And now we can head over to the IWC management console.

54
00:03:45,620 --> 00:03:45,950
All right.

55
00:03:45,950 --> 00:03:50,690
So this is the link here which you can find in the resources and we'll log in using the button here.

56
00:03:54,830 --> 00:03:55,130
Okay.

57
00:03:55,130 --> 00:03:58,100
So I'm a root user, so enter my email address.

58
00:04:04,060 --> 00:04:05,050
And then click next.

59
00:04:06,100 --> 00:04:07,450
Then do the security check.

60
00:04:14,490 --> 00:04:16,020
And now sign in with your password.

61
00:04:24,290 --> 00:04:24,560
All right.

62
00:04:24,560 --> 00:04:26,210
So this is the console home screen.

63
00:04:26,660 --> 00:04:30,620
And first off, I just want to point out that you can easily retrieve your account number here.

64
00:04:31,740 --> 00:04:32,700
Which we'll need later.

65
00:04:33,640 --> 00:04:37,090
And also your region, which you can adjust, you can retrieve here as well.

66
00:04:38,020 --> 00:04:44,560
So now let's go over to Iot Core, which I've recently visited, and we can pull that up by searching

67
00:04:44,560 --> 00:04:45,580
Iot core.

68
00:04:48,830 --> 00:04:50,330
And here, just follow the link.

69
00:04:57,130 --> 00:05:01,750
And this is the main page and there's additional resources directly linked here.

70
00:05:02,230 --> 00:05:08,050
For example, there's an interactive tutorial here, as well as video resources.

71
00:05:09,180 --> 00:05:10,350
And to develop a good.

72
00:05:11,430 --> 00:05:11,880
Okay.

73
00:05:12,480 --> 00:05:17,760
So now let's get started and go to the managed dropdown right here and then choose things.

74
00:05:20,990 --> 00:05:23,150
And now we want to go to create things.

75
00:05:27,350 --> 00:05:29,180
Then choose, create a single thing.

76
00:05:30,210 --> 00:05:31,110
And click next.

77
00:05:33,450 --> 00:05:33,830
Okay.

78
00:05:33,840 --> 00:05:35,700
And in this step, we'll give the thing a name.

79
00:05:36,180 --> 00:05:39,780
And the name that we choose has to reflect how it's defined in the source code.

80
00:05:40,350 --> 00:05:45,270
So let's go over to the source code and I'll show you where that is so you can rename it to your liking

81
00:05:45,270 --> 00:05:45,780
if you wish.

82
00:05:46,840 --> 00:05:47,140
Okay.

83
00:05:47,140 --> 00:05:52,000
So now let's open the aid wc iot ahead of file and this is the define.

84
00:05:52,030 --> 00:05:55,840
So go ahead and change it however you like and I'll just stick with this one.

85
00:05:55,990 --> 00:05:59,230
So I'll just copy it and paste it as the thing.

86
00:05:59,230 --> 00:05:59,580
Name.

87
00:06:00,750 --> 00:06:05,280
And then we won't touch the additional configurations so we can just click next.

88
00:06:06,880 --> 00:06:09,880
And now we want to auto generate a new certificate.

89
00:06:10,390 --> 00:06:11,140
Click next.

90
00:06:13,370 --> 00:06:16,070
Now we'll create and attach a policy to the certificate.

91
00:06:16,310 --> 00:06:21,710
And I already have an old policy here, so we can just ignore that and click on Create Policy.

92
00:06:26,530 --> 00:06:29,500
Now I'll just give you a policy, a name, and I'll call.

93
00:06:29,500 --> 00:06:30,610
Mind you, Demi.

94
00:06:31,740 --> 00:06:32,940
VSP 32.

95
00:06:34,690 --> 00:06:35,560
Test policy.

96
00:06:40,660 --> 00:06:40,990
All right.

97
00:06:40,990 --> 00:06:45,850
So we're going to create the policy document here, which will be formatted into JSON.

98
00:06:47,460 --> 00:06:49,620
And we could do that by going over to the building.

99
00:06:50,720 --> 00:06:55,640
And just so you know, you can include all actions by including the asterisk like so.

100
00:06:56,540 --> 00:06:59,840
And then include another asterisk as the policy resource.

101
00:07:00,320 --> 00:07:05,150
But we're going to be more specific and let's first allow for iottie connect.

102
00:07:06,310 --> 00:07:09,820
And the policy resource needs to be formatted as it's shown here.

103
00:07:10,360 --> 00:07:15,250
And I'll include a text document that you can copy from and adjust, or you can just follow my typing

104
00:07:15,250 --> 00:07:15,550
here.

105
00:07:16,270 --> 00:07:22,660
So first it's a R in colon, A.W. s colon, IATA colon.

106
00:07:23,380 --> 00:07:27,340
And here you'll need to include your region and I'll show you again where you can find it in a minute.

107
00:07:27,730 --> 00:07:29,290
And so I'll just type mine for now.

108
00:07:35,220 --> 00:07:37,380
And you can find yours from the dropdown here.

109
00:07:37,650 --> 00:07:38,160
Okay.

110
00:07:38,700 --> 00:07:39,950
And it's on the right side there.

111
00:07:41,810 --> 00:07:47,180
And also now you can copy your account number from here because we'll need to include that here, too.

112
00:07:47,990 --> 00:07:48,530
Okay.

113
00:07:48,560 --> 00:07:49,490
After the colon.

114
00:07:49,610 --> 00:07:50,420
Just paste it.

115
00:07:52,200 --> 00:07:57,270
In this first part, you can go ahead and copy because we'll use it for the next policy statement.

116
00:07:57,990 --> 00:07:58,410
All right.

117
00:07:58,650 --> 00:08:00,150
And then next type client.

118
00:08:01,710 --> 00:08:02,200
Okay.

119
00:08:02,220 --> 00:08:04,560
And then we need to include the name of our thing.

120
00:08:05,190 --> 00:08:07,200
So here that'll be forward slash.

121
00:08:08,180 --> 00:08:12,620
You Demi underscore SB 32 underscore test.

122
00:08:14,690 --> 00:08:16,370
Now let's add a new statement.

123
00:08:17,430 --> 00:08:18,840
So just use the button here.

124
00:08:20,230 --> 00:08:21,160
And will allow.

125
00:08:21,580 --> 00:08:23,430
And this time it's for Iot.

126
00:08:23,620 --> 00:08:24,310
Subscribe.

127
00:08:26,350 --> 00:08:33,100
And just follow me for the policy resource and just paste the first part and then type topic filter.

128
00:08:35,340 --> 00:08:38,610
Forward Slash and I'll show you where to get the topic from.

129
00:08:39,090 --> 00:08:40,740
So let's go over to the source code.

130
00:08:42,070 --> 00:08:43,690
And then go to the C file.

131
00:08:44,700 --> 00:08:45,870
And let's scroll down.

132
00:08:50,930 --> 00:08:52,640
And the topic name is right here.

133
00:08:53,180 --> 00:08:56,650
So let's copy that and go back to a WSI hottie.

134
00:08:57,760 --> 00:09:00,220
And let's paste it like so.

135
00:09:01,780 --> 00:09:02,170
Okay.

136
00:09:02,290 --> 00:09:03,010
That looks good.

137
00:09:03,370 --> 00:09:04,960
And let's copy the relevant part.

138
00:09:06,730 --> 00:09:11,080
And then let's add a new statement for iota you receive.

139
00:09:13,750 --> 00:09:15,370
Then paste the resource.

140
00:09:16,390 --> 00:09:17,620
And then it's topic.

141
00:09:19,150 --> 00:09:20,110
Forward slash.

142
00:09:20,970 --> 00:09:22,440
And we need the topic name.

143
00:09:22,950 --> 00:09:24,390
So it's the same as before.

144
00:09:24,840 --> 00:09:27,390
So let's copy it from the previous resource.

145
00:09:30,810 --> 00:09:32,730
And let's spend it for Iot.

146
00:09:32,880 --> 00:09:33,450
Receive.

147
00:09:35,310 --> 00:09:37,970
And this time, let's copy the entire field.

148
00:09:38,690 --> 00:09:40,490
And now let's add the final statement.

149
00:09:41,700 --> 00:09:43,980
And this will be for IATA publish.

150
00:09:46,780 --> 00:09:53,020
And then just paste the resource as its contents are the same as the previous field and then the policy

151
00:09:53,020 --> 00:09:54,130
document is complete.

152
00:09:54,730 --> 00:09:55,150
Okay.

153
00:09:55,330 --> 00:09:57,910
And then scroll down and let's click on Create.

154
00:09:59,020 --> 00:10:01,300
And you have to be sure to give it a unique name.

155
00:10:01,720 --> 00:10:04,750
In my case, the name already exists, so I'll just change it.

156
00:10:06,900 --> 00:10:08,340
And then again click Create.

157
00:10:11,640 --> 00:10:13,710
So I'll go ahead and delete this old policy.

158
00:10:14,040 --> 00:10:18,210
And if you ever need to do that, you can select it and then click Delete.

159
00:10:19,700 --> 00:10:21,080
And then type delete you.

160
00:10:26,260 --> 00:10:26,590
Okay.

161
00:10:26,590 --> 00:10:28,390
So now let's attach this policy.

162
00:10:28,870 --> 00:10:31,180
And to do that, we'll go back to the previous tab.

163
00:10:33,450 --> 00:10:38,370
Then we'll select the created policy to attach and then click create thing.

164
00:10:39,890 --> 00:10:42,830
And here are the certificates and keys that we need to download.

165
00:10:43,220 --> 00:10:45,740
So first, let's download the device certificate.

166
00:10:49,610 --> 00:10:51,530
And then we also need the private key.

167
00:10:54,670 --> 00:10:59,560
And we also need the root certificate, authority certificate and we'll just use the RC.

168
00:10:59,950 --> 00:11:00,940
So let's download it.

169
00:11:02,490 --> 00:11:03,450
And then click done.

170
00:11:05,560 --> 00:11:08,050
But it actually wants us to download the public key, too.

171
00:11:08,080 --> 00:11:08,830
So let's do that.

172
00:11:10,900 --> 00:11:11,270
Okay.

173
00:11:11,300 --> 00:11:12,940
Now we can move on, but clicking done.

174
00:11:16,140 --> 00:11:21,780
And just so you're aware, you can always view your certificates over here under the secure tab.

175
00:11:23,300 --> 00:11:23,690
All right.

176
00:11:23,990 --> 00:11:26,270
So now let's add the certificates to the project.

177
00:11:26,720 --> 00:11:27,980
So let's open the folder.

178
00:11:30,890 --> 00:11:35,180
And here I have the project folder ready and here's the main project folder.

179
00:11:36,180 --> 00:11:37,890
So I'll just set these side by side.

180
00:11:40,380 --> 00:11:40,750
Okay.

181
00:11:40,770 --> 00:11:42,480
Now, let's be sure that we select the route.

182
00:11:42,480 --> 00:11:42,990
See a.

183
00:11:44,470 --> 00:11:51,160
As well as the device certificate and the private key, and I'll just control X to cut them and then

184
00:11:51,160 --> 00:11:52,990
I'll paste them here into the search folder.

185
00:11:55,290 --> 00:11:55,620
Okay.

186
00:11:55,630 --> 00:11:58,620
Now let's go to the source file and take a look at how they're defined.

187
00:12:00,710 --> 00:12:01,010
All right.

188
00:12:01,010 --> 00:12:05,930
So here we have the root certificate, the device certificate, as well as the private key.

189
00:12:06,230 --> 00:12:11,360
And the embedded certificates are loaded from the search folder and embedded into the application binary.

190
00:12:12,520 --> 00:12:14,560
So we need the file names to match these here.

191
00:12:16,150 --> 00:12:19,360
So let's refresh the folders so that the certificates appear.

192
00:12:20,670 --> 00:12:21,510
Let's refresh.

193
00:12:23,090 --> 00:12:24,650
And expand the search folder.

194
00:12:27,230 --> 00:12:27,740
Okay.

195
00:12:29,030 --> 00:12:29,960
Let's copy the route.

196
00:12:29,970 --> 00:12:30,680
See a name.

197
00:12:32,640 --> 00:12:34,620
And I'll just bring the file names into view.

198
00:12:37,570 --> 00:12:37,990
Okay.

199
00:12:38,110 --> 00:12:40,510
Now right click and rename.

200
00:12:42,140 --> 00:12:43,550
And then let's just paste the name.

201
00:12:44,970 --> 00:12:45,410
Then click.

202
00:12:45,410 --> 00:12:45,800
Okay.

203
00:12:48,830 --> 00:12:50,720
And let's grab the device certificate name.

204
00:12:55,820 --> 00:12:56,930
And let's right click.

205
00:12:57,720 --> 00:12:58,320
Rename.

206
00:13:00,250 --> 00:13:01,000
Paste the name.

207
00:13:04,170 --> 00:13:04,830
And click.

208
00:13:04,830 --> 00:13:05,200
Okay.

209
00:13:06,790 --> 00:13:09,130
All right, now let's copy the private key file name.

210
00:13:13,690 --> 00:13:14,590
And rename.

211
00:13:16,870 --> 00:13:17,590
And paste.

212
00:13:22,930 --> 00:13:23,140
Now.

213
00:13:23,140 --> 00:13:23,830
Let's continue.

214
00:13:26,900 --> 00:13:33,410
Go to the main C, make this file here and now we'll tell C make to embed these files and we'll do that

215
00:13:33,410 --> 00:13:34,670
using the following command.

216
00:13:36,130 --> 00:13:39,160
Say target add binary data.

217
00:13:42,270 --> 00:13:43,140
Parentheses.

218
00:13:43,440 --> 00:13:47,280
Dollar Sign open curly braces component.

219
00:13:48,490 --> 00:13:49,090
Target.

220
00:13:50,550 --> 00:13:52,980
Close curly braces and then in quotes.

221
00:13:53,250 --> 00:13:57,580
We need the path which is certs forward slash nwc.

222
00:13:57,960 --> 00:13:58,770
See a pen.

223
00:14:04,330 --> 00:14:07,330
And it's text and close parentheses.

224
00:14:07,930 --> 00:14:10,990
Then let's copy this line and paste below.

225
00:14:12,290 --> 00:14:14,120
And then just update the name of the file.

226
00:14:25,280 --> 00:14:25,700
Okay.

227
00:14:25,730 --> 00:14:26,840
Then add the private key.

228
00:14:35,290 --> 00:14:36,260
All right, that looks good.

229
00:14:36,280 --> 00:14:37,810
So now let's go to the C file.

230
00:14:41,340 --> 00:14:42,870
And go to the bottom of the file.

231
00:14:44,230 --> 00:14:48,160
And this function here starts the IWC 83 arduous task.

232
00:14:48,610 --> 00:14:50,980
It will need to add these defines to the tasks.

233
00:14:50,980 --> 00:14:51,910
Common header file.

234
00:14:52,240 --> 00:14:53,050
So let's go them.

235
00:14:54,350 --> 00:14:58,130
And we'll define for a U.S. Iot task.

236
00:15:02,440 --> 00:15:03,940
In first do the stack size.

237
00:15:07,540 --> 00:15:09,820
As 9216 bytes.

238
00:15:12,950 --> 00:15:13,790
Then let's add.

239
00:15:22,280 --> 00:15:23,060
As six.

240
00:15:24,750 --> 00:15:25,650
And then let's add.

241
00:15:27,010 --> 00:15:27,880
The core I.D..

242
00:15:34,460 --> 00:15:35,270
We'll make it one.

243
00:15:38,040 --> 00:15:38,470
Okay.

244
00:15:38,470 --> 00:15:39,170
It looks good.

245
00:15:39,180 --> 00:15:42,330
Now let's save it and then go back to the C file.

246
00:15:44,330 --> 00:15:45,980
And now defines updated.

247
00:15:46,670 --> 00:15:47,050
Okay.

248
00:15:47,060 --> 00:15:51,680
Next, we need to build the project and generate the updated SDK config file.

249
00:15:52,010 --> 00:15:55,850
But first, I'll make sure to save the C make list file that I forgot to save here.

250
00:15:59,530 --> 00:15:59,890
Okay.

251
00:15:59,890 --> 00:16:00,820
Now that's saved.

252
00:16:01,030 --> 00:16:07,630
And before we build, let's first go to main dot C and let's include a w s Iot that h.

253
00:16:14,400 --> 00:16:19,050
All right, then we want to call the task start function when we have a Wi-Fi connection.

254
00:16:19,830 --> 00:16:21,960
So let's go ahead and copy that function name.

255
00:16:24,660 --> 00:16:25,440
Then paste it.

256
00:16:27,230 --> 00:16:27,590
Okay.

257
00:16:27,590 --> 00:16:32,900
So again, this task should only start when the ESP 32 is connected to the Internet, and that's why

258
00:16:32,900 --> 00:16:33,860
we want to call it here.

259
00:16:34,760 --> 00:16:35,060
All right.

260
00:16:35,060 --> 00:16:40,430
So also, before we build, we need to increase the partition table sizes for the otus slots.

261
00:16:40,790 --> 00:16:43,400
And I've included the partition table in the resources.

262
00:16:43,820 --> 00:16:46,970
So please have that file ready and I'll show you where to include it.

263
00:16:47,780 --> 00:16:48,110
Okay.

264
00:16:48,110 --> 00:16:55,130
So with the latest IDF installation, my IDF is now located in this location, so I'll just go to frameworks

265
00:16:55,730 --> 00:16:56,840
esp IDF.

266
00:16:58,190 --> 00:16:59,390
Then go to components.

267
00:17:00,510 --> 00:17:02,520
And then go down to partition table.

268
00:17:06,850 --> 00:17:13,450
And you'll want to replace your old partitions to add to that CSV file with the one that I've provided

269
00:17:13,720 --> 00:17:15,190
and I've already updated mine.

270
00:17:15,610 --> 00:17:18,940
So let's go ahead and take a look at that and let's review this from the top.

271
00:17:19,630 --> 00:17:25,330
In this here is the same motor data is the same and this is the same.

272
00:17:25,840 --> 00:17:31,780
But here I've removed the factory app to make more room for the voter slots and I've maxed out both

273
00:17:31,780 --> 00:17:34,600
of them for my SB 32 rover, and that's it.

274
00:17:35,200 --> 00:17:38,530
And we could swap between these two OTA slots for firmware updates.

275
00:17:39,070 --> 00:17:40,300
Okay, now let's go back.

276
00:17:41,990 --> 00:17:43,970
And just be sure to update yours as well.

277
00:17:45,090 --> 00:17:51,450
Now we're going to build the project so that we can update the SDK config file for AWG satellite communication.

278
00:17:51,780 --> 00:17:53,010
So go ahead and build all.

279
00:17:56,390 --> 00:17:58,760
And this may take a bit small speed up the video now.

280
00:18:05,910 --> 00:18:08,010
And now let's open the SDK config.

281
00:18:20,030 --> 00:18:21,500
And go all the way to the bottom.

282
00:18:24,140 --> 00:18:27,770
And open Amazon Web Services Iot platform settings.

283
00:18:29,750 --> 00:18:37,130
And now we need to update the IWC iota endpoint hostname, which we can get from the AWB Iot account.

284
00:18:37,370 --> 00:18:41,090
But first, I'll show you where this variable is located in the source code.

285
00:18:41,420 --> 00:18:45,860
So in AWB Iot that C go towards the top of the file.

286
00:18:48,690 --> 00:18:53,040
And take a look at this variable fwc, iata kuti host.

287
00:18:53,730 --> 00:19:02,160
This is the default and Kuti host url that is pulled from AWG sale t config that h and if we hover we

288
00:19:02,160 --> 00:19:03,250
can see that it's empty.

289
00:19:03,420 --> 00:19:07,890
So let's follow this definition and we can see that this definition originates from here.

290
00:19:08,310 --> 00:19:09,270
So let's follow that.

291
00:19:10,410 --> 00:19:13,290
And this takes us to the SDK config file.

292
00:19:13,560 --> 00:19:15,210
And of course, this variable is empty.

293
00:19:15,720 --> 00:19:16,980
So let's go ahead and update it.

294
00:19:17,370 --> 00:19:25,620
So let's go back to a WSU T and first let's go into the thing, click on the thing and choose, interact.

295
00:19:26,070 --> 00:19:28,050
And from there, go to view settings.

296
00:19:30,920 --> 00:19:36,410
And here we have the device data endpoint and here it tells us that your devices can use your accounts

297
00:19:36,410 --> 00:19:39,230
device data endpoint to connect to a WC.

298
00:19:39,590 --> 00:19:42,980
Each of your things has a rest API available at this endpoint.

299
00:19:43,100 --> 00:19:48,170
nQt clients in a WSI Iot devices case also use this endpoint.

300
00:19:48,590 --> 00:19:50,300
All right, so that's exactly what we need.

301
00:19:50,300 --> 00:19:53,120
So let's copy that by clicking here and then.

302
00:19:53,120 --> 00:19:54,570
Now let's go back to the idea.

303
00:19:55,860 --> 00:19:58,110
So go back to the SDK configuration.

304
00:19:58,950 --> 00:19:59,790
And pasted here.

305
00:20:01,520 --> 00:20:02,540
And be sure to save it.

306
00:20:04,700 --> 00:20:05,840
And then we can close it out.

307
00:20:07,340 --> 00:20:07,690
Okay.

308
00:20:07,700 --> 00:20:09,410
Now let's build so we can test it out.

309
00:20:13,460 --> 00:20:15,350
And again, I'll speed up the video for this.

310
00:20:22,490 --> 00:20:22,870
Okay.

311
00:20:22,880 --> 00:20:23,720
Now let's flesh.

312
00:20:29,490 --> 00:20:31,860
And here I have a message that you've probably seen before.

313
00:20:32,340 --> 00:20:37,410
In this case, it looks like intelligence didn't recognize a variable in wi fi apt c.

314
00:20:37,710 --> 00:20:38,790
So let's just proceed.

315
00:20:42,440 --> 00:20:44,390
And if I click on fi app dot c.

316
00:20:45,370 --> 00:20:46,210
Now it goes away.

317
00:20:48,210 --> 00:20:48,500
All right.

318
00:20:48,500 --> 00:20:50,030
So now just let flesh and complete.

319
00:20:52,210 --> 00:20:52,600
Okay.

320
00:20:52,630 --> 00:20:56,770
Now let's have a society that see and view and open a monitor.

321
00:21:03,540 --> 00:21:06,420
All right, so just give me a moment to connect the ISP 32.

322
00:21:11,500 --> 00:21:11,800
Okay.

323
00:21:11,800 --> 00:21:18,760
So now I'm connected and the callback function is called and the IWC vr tas task is started.

324
00:21:23,540 --> 00:21:26,300
And now a society is subscribing.

325
00:21:27,160 --> 00:21:29,230
And now I'm getting the messages logged right here.

326
00:21:31,890 --> 00:21:32,310
Okay.

327
00:21:32,610 --> 00:21:34,650
And let's see where this happens in the source code.

328
00:21:35,910 --> 00:21:36,870
So just follow me.

329
00:21:40,890 --> 00:21:45,090
And these are the sprint F messages into the C payload variable.

330
00:21:48,270 --> 00:21:49,260
For quality of service.

331
00:21:49,260 --> 00:21:49,710
Zero.

332
00:21:52,400 --> 00:21:54,350
And for quality of service one.

333
00:21:56,100 --> 00:21:57,360
And for quality of service.

334
00:21:57,360 --> 00:22:02,760
One, we're checking the error status in which this error would imply that.

335
00:22:03,030 --> 00:22:05,490
Q OS one acknowledgement was received.

336
00:22:05,850 --> 00:22:10,710
All right, so now let's go to NWA Society and view these messages there.

337
00:22:11,760 --> 00:22:12,090
Okay.

338
00:22:12,320 --> 00:22:13,670
MWC City.

339
00:22:13,740 --> 00:22:15,030
Let's go back to things.

340
00:22:24,480 --> 00:22:26,010
And now just click in to your thing.

341
00:22:27,540 --> 00:22:29,130
Now go down to activity.

342
00:22:30,820 --> 00:22:33,340
Then to the mktg test client.

343
00:22:43,940 --> 00:22:48,710
First we need to enter the topic filter and the topic filter describes the topics to which you want

344
00:22:48,710 --> 00:22:51,530
to subscribe, and this is defined in the source code.

345
00:22:51,710 --> 00:22:52,930
So let's go to the I.D..

346
00:22:54,460 --> 00:22:55,990
And follow me just up here.

347
00:22:58,330 --> 00:23:00,340
And that is our topic defined right here.

348
00:23:01,150 --> 00:23:03,040
So copy it and let's go back.

349
00:23:04,080 --> 00:23:04,980
And pasted here.

350
00:23:06,310 --> 00:23:08,650
And now let's go down to additional configuration.

351
00:23:10,040 --> 00:23:12,620
And Select display payloads as strings.

352
00:23:13,750 --> 00:23:19,420
And then click subscribe and then you'll see the messages start to appear and it may take a second or

353
00:23:19,420 --> 00:23:19,750
two.

354
00:23:20,050 --> 00:23:20,740
And there we go.

355
00:23:21,370 --> 00:23:28,210
Our test topic is alive and the data from the ESP 32 is populating right here and the messages are populated

356
00:23:28,210 --> 00:23:30,220
at the defined interval from the source code.

357
00:23:30,850 --> 00:23:35,830
And we can set this as a favorite so that we can do it any time we go to a society.

358
00:23:36,160 --> 00:23:39,400
So Set is a favorite here and now.

359
00:23:39,400 --> 00:23:41,260
Let's test publishing to the topic.

360
00:23:42,170 --> 00:23:45,230
And he will just click publish to publish this message.

361
00:23:46,420 --> 00:23:47,800
And that'll be for a topic.

362
00:23:48,250 --> 00:23:52,510
And the message payload will be published to this topic with the quality of service zero.

363
00:23:52,630 --> 00:23:53,080
Okay.

364
00:23:54,290 --> 00:23:55,550
All right, so now let's test it.

365
00:23:57,450 --> 00:24:02,130
And back in the IDB, we can see that it was sent successfully right there.

366
00:24:03,300 --> 00:24:08,160
Right there in our subscribe callback function, and that's where the message is logged into the console.

367
00:24:08,550 --> 00:24:09,360
So let's see that.

368
00:24:11,190 --> 00:24:12,540
And that is right up here.

369
00:24:17,230 --> 00:24:21,430
And that's from our subscribe callback handler where the console messages are locked.

370
00:24:22,410 --> 00:24:22,730
Okay.

371
00:24:22,740 --> 00:24:27,960
So in the next lesson, we'll do a brief walkthrough of the source code and also will expand it to include

372
00:24:27,960 --> 00:24:32,910
received signal strength of the Wi-Fi connection as well as the temperature and humidity sensor data.

373
00:24:33,270 --> 00:24:33,580
All right.

374
00:24:33,580 --> 00:24:36,330
So I really hope you enjoyed this lesson and I'll see you in the next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Policy effect		Policy action		Policy resource
Allow				iot:Connect			arn:aws:iot:REGION:ACCOUNT:client/Udemy_ESP32_Test
Allow				iot:Subscribe		arn:aws:iot:REGION:ACCOUNT:topicfilter/test_topic/esp32
Allow				iot:Receive			arn:aws:iot:REGION:ACCOUNT:topic/test_topic/esp32
Allow				iot:Publish			arn:aws:iot:REGION:ACCOUNT:topic/test_topic/esp32

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,140 --> 00:00:07,530
Okay.

2
00:00:07,530 --> 00:00:12,960
Now we're going to review the source code for the IWC publish subscribed implementation and we're going

3
00:00:12,960 --> 00:00:17,940
to expand it to publish the temperature and humidity sensor data as well as the received signal strength

4
00:00:17,940 --> 00:00:22,680
of the Wi-Fi connection so that we can view this data from the MQ RTT test client.

5
00:00:23,250 --> 00:00:23,610
All right.

6
00:00:23,610 --> 00:00:30,510
So starting from main that see here we're calling a WAC Iot start so go ahead and control left click

7
00:00:30,510 --> 00:00:31,470
to follow that function.

8
00:00:33,280 --> 00:00:39,760
And here I've added the test candle for the WC Iot task and to check for null to ensure that it's created

9
00:00:39,760 --> 00:00:43,600
only once in the event that the callback function is invoked multiple times.

10
00:00:44,200 --> 00:00:47,230
And here the test candle is created and initialized to null.

11
00:00:48,100 --> 00:00:49,180
Okay, let's continue.

12
00:00:50,020 --> 00:00:54,070
And here we have our certificates, which doesn't need much explanation as we dealt with this in the

13
00:00:54,070 --> 00:01:00,130
previous lesson where we saw that the embedded certificates are required by a WSU T and these are actually

14
00:01:00,130 --> 00:01:06,790
included as part of the NQT initialization in the AWB Iot task, which we'll see shortly.

15
00:01:07,600 --> 00:01:12,880
And then we have the nQt host URL, which we've updated via the SDK config.

16
00:01:13,270 --> 00:01:16,330
But this could also be defined directly in the source code, if you prefer.

17
00:01:17,830 --> 00:01:22,360
And then next we have the amputee port, which is port eight eight, eight three.

18
00:01:23,110 --> 00:01:25,930
And then there are the subscribe and disconnect callback handlers.

19
00:01:26,260 --> 00:01:31,930
And we saw how the subscribe callback logs, the topic data and the disconnect handler either attempts

20
00:01:31,930 --> 00:01:34,390
to reconnect automatically or manually.

21
00:01:34,840 --> 00:01:39,280
And I'll show you where the auto reconnect functionality is enabled when we get further down the file.

22
00:01:41,190 --> 00:01:48,210
Then we have the WC Iot task and first an array for the payload is created and there's also the variable

23
00:01:48,210 --> 00:01:50,070
AI, which is used as a message counter.

24
00:01:50,400 --> 00:01:54,450
But I won't use this variable as we make adjustments, but you can feel free to keep it if you like.

25
00:01:55,440 --> 00:02:01,620
And then here we have some instances that originate from the MWC Iot Device SDK, and that's for the

26
00:02:01,620 --> 00:02:09,900
AWB Society client, NQT initialization parameters, connection parameters and parameters for both quality

27
00:02:09,900 --> 00:02:15,720
of service level zero and quality of service level one messages and then the lines that follow.

28
00:02:15,720 --> 00:02:20,290
Take care of the NQT in it parameters such as auto reconnect.

29
00:02:20,340 --> 00:02:27,840
Host You are will the port are embedded certificates NQT command time out in milliseconds, the TLS

30
00:02:27,840 --> 00:02:34,410
handshake timeout, the SSL hostname verify and then the disconnect callback handler is provided.

31
00:02:34,950 --> 00:02:43,170
And then the disconnect handler data is null and once the NQT parameters are initialized then the WC

32
00:02:43,170 --> 00:02:51,060
Iot nQt init function is called and a reference to the AWB Iot client is passed to the function along

33
00:02:51,060 --> 00:02:53,340
with the NQT in IT parameters.

34
00:02:54,060 --> 00:03:00,240
Then the connection parameters are initialized for the Iot client connection along with our config AWB

35
00:03:00,270 --> 00:03:05,250
example client ID, which is defined in the AWB Iot header file.

36
00:03:05,670 --> 00:03:08,670
And this is also your things name in a society.

37
00:03:09,210 --> 00:03:13,830
And just as a reminder, this is the client I did that I had given in the head of file.

38
00:03:14,790 --> 00:03:16,560
Okay, now let's go back to where we were.

39
00:03:18,810 --> 00:03:24,600
So after the connection parameters are initialized here, we then attempt the connection to a wc using

40
00:03:24,630 --> 00:03:33,420
a wc iet nqt connect and we do this at a 1/2 interval while the RC variable is not equal to success.

41
00:03:34,950 --> 00:03:41,140
And then here is where the auto reconnect functionality is enabled and that's done using a WSU T and

42
00:03:41,160 --> 00:03:43,290
duty auto reconnect set status.

43
00:03:43,830 --> 00:03:48,510
And this is the same auto reconnect functionality that I had mentioned for the disconnect callback handler.

44
00:03:49,630 --> 00:03:55,670
Then the topic name is defined and its length is obtained so that we could use it in the wc iet mq to

45
00:03:55,810 --> 00:03:56,770
subscribe function.

46
00:03:57,400 --> 00:04:02,500
And this function also takes the Iot subscribe callback handler function name as a parameter.

47
00:04:03,010 --> 00:04:04,270
So this is how we subscribe.

48
00:04:05,020 --> 00:04:05,410
Okay.

49
00:04:05,410 --> 00:04:10,570
Next, the quality of service zero and quality of service one parameters are initialized and the payload

50
00:04:10,570 --> 00:04:11,680
variable is required.

51
00:04:11,680 --> 00:04:14,170
Here it is casted as a void pointer.

52
00:04:15,140 --> 00:04:18,230
And the payload variable is what we pass our data into in publishing.

53
00:04:20,610 --> 00:04:25,110
Next we drop into the wild loop and we stay there as long as we have one of the mentioned status is

54
00:04:25,110 --> 00:04:29,670
returned and then the a wc iet kuti yield function.

55
00:04:30,090 --> 00:04:34,410
We'll wait for the red messages and then they get stack high watermark.

56
00:04:34,410 --> 00:04:40,230
Free Auto API is used to get the remaining stack in bytes and another API is used to return the name

57
00:04:40,230 --> 00:04:45,690
of the task and it's log to the console and then we have a delay which controls how often we want to

58
00:04:45,690 --> 00:04:46,440
publish data.

59
00:04:46,920 --> 00:04:49,560
So I'll go ahead and increase that to 3000 milliseconds.

60
00:04:50,340 --> 00:04:54,450
And then here we use as printf to update the payload for quality of service zero.

61
00:04:55,200 --> 00:04:59,940
So now let's go ahead and updated to include the received signal strength of the Wi-Fi connection and

62
00:04:59,940 --> 00:05:02,340
I'll include the function here, which will define shortly.

63
00:05:02,670 --> 00:05:07,170
But for now, let's just update the text and we'll update the text to, say, wi fi or a.

64
00:05:12,190 --> 00:05:15,970
And then here we'll include the function wi fi app, get RSS side.

65
00:05:28,670 --> 00:05:30,250
And this function will return an end.

66
00:05:30,470 --> 00:05:35,270
So the rest of the sprint def statement is fine and the next we'll need to update the payload length

67
00:05:35,480 --> 00:05:41,300
and then call a WC iota in Q2 to publish to publish data for quality of service zero.

68
00:05:41,570 --> 00:05:44,930
And this takes care of publishing data for quality of service zero messages.

69
00:05:45,200 --> 00:05:50,270
Next, let's update the payload for quality of service level one messages, which will include a temperature

70
00:05:50,270 --> 00:05:51,500
and humidity sensor data.

71
00:05:51,770 --> 00:05:54,110
So now let's just add the text for temperature.

72
00:06:00,610 --> 00:06:02,710
Then let's add the get temperature function.

73
00:06:10,460 --> 00:06:17,480
Then let's also update the sprint def type for the return of get temperature to a float type with one

74
00:06:17,480 --> 00:06:18,260
decimal point.

75
00:06:19,450 --> 00:06:25,900
Then let's add another string for humidity and let's also include the type for the get humidity function

76
00:06:25,900 --> 00:06:26,290
return.

77
00:06:27,880 --> 00:06:28,230
Okay.

78
00:06:28,240 --> 00:06:30,400
Now we'll just need to add the text for humidity.

79
00:06:38,910 --> 00:06:40,470
And then let's add the function as well.

80
00:06:44,660 --> 00:06:45,030
Okay.

81
00:06:45,050 --> 00:06:50,270
Then the next step includes updating the payload length once again, but this time for quality of service

82
00:06:50,270 --> 00:06:55,820
one and then calling a wc iut in Q2 to publish to publish the data.

83
00:06:56,270 --> 00:07:00,050
Then, since it's quality of service one, we check for the acknowledgement.

84
00:07:01,040 --> 00:07:02,030
Okay, that looks good.

85
00:07:02,210 --> 00:07:07,460
So now let's add the HD 22 dot H for our temperature and humidity functions.

86
00:07:17,830 --> 00:07:18,310
All right.

87
00:07:18,370 --> 00:07:23,160
Now we can go to wi fi updates and create the prototype for the get RSA function.

88
00:07:28,200 --> 00:07:28,550
Okay.

89
00:07:28,560 --> 00:07:31,980
And this function gets the RSS value.

90
00:07:35,480 --> 00:07:36,710
Of the Wi-Fi connection.

91
00:07:41,050 --> 00:07:41,830
In the return.

92
00:07:43,110 --> 00:07:44,940
Is the current RSI level.

93
00:07:50,670 --> 00:07:52,530
And the return is a type.

94
00:07:55,110 --> 00:07:56,670
And it's called wi fi app.

95
00:07:57,940 --> 00:07:58,960
Get on a suicide.

96
00:08:01,870 --> 00:08:02,590
And that's void.

97
00:08:04,220 --> 00:08:04,510
Okay.

98
00:08:04,520 --> 00:08:06,170
Now let's go to the C file and define it.

99
00:08:06,590 --> 00:08:08,900
So let's first copy the name and the return type.

100
00:08:14,130 --> 00:08:14,370
Now.

101
00:08:14,370 --> 00:08:15,810
Let's go all the way down to the bottom.

102
00:08:17,600 --> 00:08:18,800
And paste it down here.

103
00:08:22,840 --> 00:08:26,020
And now we need an instance of the wi fi app record type.

104
00:08:31,050 --> 00:08:32,490
And call it wi fi data.

105
00:08:36,330 --> 00:08:38,160
And then let's ESP check.

106
00:08:40,900 --> 00:08:44,080
ESP wifi stay get app info.

107
00:08:51,690 --> 00:08:54,630
And then we're going to pass the Wi-Fi app record type.

108
00:08:55,530 --> 00:08:55,960
Okay.

109
00:08:56,010 --> 00:08:58,170
And that is a reference to Wi-Fi data.

110
00:09:01,940 --> 00:09:04,340
And then we simply return the Wi-Fi data.

111
00:09:07,200 --> 00:09:09,130
An access to RSI structure.

112
00:09:09,130 --> 00:09:09,540
A member.

113
00:09:11,950 --> 00:09:12,390
All right.

114
00:09:12,400 --> 00:09:14,980
And here is where we could find the wi fi app record.

115
00:09:16,440 --> 00:09:18,090
Along with the RSI member.

116
00:09:18,660 --> 00:09:19,050
Okay.

117
00:09:19,260 --> 00:09:20,910
Now let's build this and test it out.

118
00:09:32,040 --> 00:09:32,880
In a flash it.

119
00:09:45,280 --> 00:09:47,080
All right, now let's bring up the console.

120
00:10:03,660 --> 00:10:04,260
Okay.

121
00:10:04,620 --> 00:10:05,640
And this all looks good.

122
00:10:07,620 --> 00:10:07,890
Yep.

123
00:10:07,890 --> 00:10:08,580
That looks all right.

124
00:10:09,030 --> 00:10:13,920
So now let's go to the WC and cu t test client and confirm that the values are logged.

125
00:10:15,070 --> 00:10:15,910
Okay, perfect.

126
00:10:16,270 --> 00:10:21,450
Our published data now includes the temperature, humidity and RSA side, and that's really great.

127
00:10:21,460 --> 00:10:26,800
So now we can check the strength of the Wi-Fi connection as well as the temperature, humidity or whatever

128
00:10:26,800 --> 00:10:28,930
other data you want to publish from anywhere in the world.

129
00:10:29,200 --> 00:10:30,310
And that is really awesome.

130
00:10:30,700 --> 00:10:35,170
And now that you had the foundation of the wireless local area network and now you know how to integrate

131
00:10:35,170 --> 00:10:41,140
a cloud framework like a WC, you can now confidently explore other cloud frameworks if a WC isn't the

132
00:10:41,140 --> 00:10:41,770
one for you.

133
00:10:42,220 --> 00:10:45,190
All right, so I really hope you enjoyed this, and I hope to see you again soon.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:06,740 --> 00:00:12,050
Hello and welcome to the updated lesson on using a US Iot with the updated sdhc.

2
00:00:12,290 --> 00:00:19,340
In the previous lessons we'd integrated the ESP a US Iot released version 3.1 and this was the latest

3
00:00:19,340 --> 00:00:24,770
version at the time of the recording, but has since released a newer version and I'm going to keep

4
00:00:24,770 --> 00:00:29,000
the old version as part of the configuration lesson as some people are still using it.

5
00:00:29,000 --> 00:00:32,990
But for those that want to check out an example of publishing and subscribing using the new version

6
00:00:32,990 --> 00:00:35,420
here, then this lesson is for you.

7
00:00:35,900 --> 00:00:41,240
However, before moving on, please be sure that you've already set up your account, created a thing

8
00:00:41,240 --> 00:00:45,320
in US generated certificates and attach the policy.

9
00:00:45,530 --> 00:00:49,280
Basically, everything we did in the configuration lesson.

10
00:00:49,580 --> 00:00:52,340
So go back and watch that if you haven't already.

11
00:00:53,000 --> 00:00:58,610
So let's get started here by going to the project folder and let's change the name of the existing US

12
00:00:58,670 --> 00:00:59,870
Iot folder.

13
00:01:00,020 --> 00:01:01,730
In case you want to keep this version.

14
00:01:02,330 --> 00:01:04,340
So that is version 3.1.

15
00:01:09,160 --> 00:01:12,580
Now let's copy the clone command they provided for us here.

16
00:01:12,820 --> 00:01:13,660
So copy that.

17
00:01:13,660 --> 00:01:14,380
Like so.

18
00:01:14,920 --> 00:01:16,570
And then go to the project folder.

19
00:01:19,110 --> 00:01:22,590
Because we want to clone it to this folder and right click here.

20
00:01:26,020 --> 00:01:27,700
And then go to get Bashir.

21
00:01:31,740 --> 00:01:33,480
And then paste in the clone command.

22
00:01:37,940 --> 00:01:41,660
And just give it a few moments to finish as it may take a little while.

23
00:01:44,630 --> 00:01:45,770
And now we can close get.

24
00:01:47,240 --> 00:01:52,460
And let's just briefly check out what we have here and our cloned ESP a society folder.

25
00:01:53,640 --> 00:01:58,410
Here are the top level structure looks pretty simple with the examples folder and the libraries folder,

26
00:01:58,410 --> 00:02:03,750
and we'll look into the examples shortly and we'll actually implement the mktg example.

27
00:02:04,470 --> 00:02:09,330
And in the libraries folder, we'll need to include these by adjusting our make list file.

28
00:02:09,690 --> 00:02:13,770
So feel free to get familiar with these files and folders here, especially if you're interested in

29
00:02:13,770 --> 00:02:16,190
diving deeper into a society.

30
00:02:16,410 --> 00:02:16,710
All right.

31
00:02:16,710 --> 00:02:19,440
So now let's review into the example that we're going to implement.

32
00:02:19,890 --> 00:02:21,810
Let's go back to the examples folder.

33
00:02:23,390 --> 00:02:28,880
And the example that we want is an example where we can simply publish and subscribe data.

34
00:02:28,910 --> 00:02:34,070
However, you can always explore the other examples once you know how to integrate this example.

35
00:02:34,160 --> 00:02:39,260
So let's go into MQTT, then let's go into TLS mutual authentication.

36
00:02:41,370 --> 00:02:45,360
And first, let's take a look at the read me that's provided here, because there's a few important

37
00:02:45,360 --> 00:02:46,110
notes there.

38
00:02:46,890 --> 00:02:54,450
First, it says we need to find and set the US endpoint hostname and it says Your Iot account has a

39
00:02:54,450 --> 00:02:56,580
unique endpoint hostname to connect to.

40
00:02:56,610 --> 00:03:02,790
To find it open the US Iot console and click the settings button on the bottom left side and using the

41
00:03:02,790 --> 00:03:04,350
K config project build file.

42
00:03:04,350 --> 00:03:10,200
From this example, we can enter the endpoint host name into the example configuration and the sdhc

43
00:03:10,200 --> 00:03:10,860
config.

44
00:03:11,070 --> 00:03:18,630
So also we need to set the client ID and it says here that the client ID is used in the MQTT Protocol

45
00:03:18,630 --> 00:03:26,490
to send messages to and from a society and a Iot requires that each connected device within a single

46
00:03:26,820 --> 00:03:33,210
US account uses a unique client ID, and if we recall from the configuration lesson, this is the name

47
00:03:33,210 --> 00:03:35,820
of our thing in a society.

48
00:03:35,970 --> 00:03:41,100
And in this example, these definitions are compiled into the menu config, which we can adjust via

49
00:03:41,100 --> 00:03:42,630
the sdhc config file.

50
00:03:42,930 --> 00:03:47,760
All right, so let's just grab that information for now, just as a quick refresher of where we can

51
00:03:47,760 --> 00:03:50,190
find it so that we can easily retrieve it later.

52
00:03:50,430 --> 00:03:54,750
So I'll just create a new text file and from our AWS account.

53
00:03:56,800 --> 00:03:58,840
We can go to Iot core.

54
00:04:02,340 --> 00:04:04,080
And then I'll just set my location.

55
00:04:11,910 --> 00:04:13,530
And then we can go into settings.

56
00:04:16,950 --> 00:04:18,900
And let's grab the endpoint hostname.

57
00:04:19,860 --> 00:04:21,090
Copy it like so.

58
00:04:22,790 --> 00:04:24,530
And then I'll just make a note of it here.

59
00:04:27,250 --> 00:04:27,640
Next.

60
00:04:27,640 --> 00:04:29,110
We want the client to ID.

61
00:04:34,310 --> 00:04:36,230
Let's go to all devices.

62
00:04:37,000 --> 00:04:38,250
Didn't go to things.

63
00:04:40,970 --> 00:04:42,320
And I'll just copy mine.

64
00:04:44,990 --> 00:04:47,720
And then make a note of it here and now.

65
00:04:47,720 --> 00:04:52,640
Let's start integrating the framework and we'll start off by adjusting the top level CMYK list file

66
00:04:52,760 --> 00:04:56,840
and we can actually use the C make list file provided by the example for reference.

67
00:04:58,590 --> 00:05:01,260
So let's just open the make list file provided.

68
00:05:05,840 --> 00:05:08,480
And then let's copy the entire set command right here.

69
00:05:10,210 --> 00:05:13,330
Now go to the top level C make list file in the project.

70
00:05:19,830 --> 00:05:24,810
And we can actually move the set command to the recommended location so we can get rid of this one.

71
00:05:27,620 --> 00:05:29,030
And then pace the command to.

72
00:05:30,840 --> 00:05:34,380
But let's adjust the path here so that it aligns with our folder structure.

73
00:05:34,770 --> 00:05:36,510
We can select this part here.

74
00:05:37,730 --> 00:05:39,150
Then use control f.

75
00:05:40,000 --> 00:05:45,610
And then we could replace it with the correct path to the ESP a US Iot folder here.

76
00:05:46,180 --> 00:05:48,730
All right, so just enter ESP.

77
00:05:50,020 --> 00:05:52,410
A Iot.

78
00:05:53,500 --> 00:05:54,610
Then replace all.

79
00:05:57,930 --> 00:05:58,450
Och.

80
00:05:58,500 --> 00:05:59,580
And that all looks good.

81
00:05:59,580 --> 00:06:06,150
Except we forgot to do one thing and that's to refresh the project as I noticed that a USB Iot version

82
00:06:06,150 --> 00:06:08,340
3.1 folder is missing here.

83
00:06:08,370 --> 00:06:15,060
So what we could do is go to the top level project folder and right click and then go down to refresh

84
00:06:15,630 --> 00:06:17,130
and refresh the project.

85
00:06:18,540 --> 00:06:21,090
Now we have the old version in the new version right here.

86
00:06:22,950 --> 00:06:28,560
Next, let's copy the necessary files over to the ID by going into the main folder of the example.

87
00:06:28,800 --> 00:06:31,110
So let's head over to the example folder.

88
00:06:34,010 --> 00:06:35,450
Go into the main folder.

89
00:06:37,030 --> 00:06:39,170
And we already have our own app main.

90
00:06:39,190 --> 00:06:41,890
So let's just take the demo config header file.

91
00:06:42,750 --> 00:06:47,970
The config project build file and the MK PT demo source file.

92
00:06:48,660 --> 00:06:49,830
Copy those over.

93
00:06:54,500 --> 00:06:57,920
Choose overwrite for the k config project build file.

94
00:07:00,870 --> 00:07:05,550
Okay, Next we can update the main CMYK list file by copying the name of our new source file.

95
00:07:06,000 --> 00:07:07,680
Go over to the new source file.

96
00:07:10,330 --> 00:07:11,560
And right click on it.

97
00:07:12,760 --> 00:07:13,480
To copy.

98
00:07:14,050 --> 00:07:16,300
Then let's open up the main make list file.

99
00:07:18,150 --> 00:07:21,810
And we can override the old a society source file.

100
00:07:22,710 --> 00:07:24,210
With the new file name here.

101
00:07:25,700 --> 00:07:27,110
And just be sure to save that.

102
00:07:27,590 --> 00:07:29,510
Next, let's update our main see.

103
00:07:30,700 --> 00:07:34,150
And let's use the app and see from the example it's a reference.

104
00:07:36,270 --> 00:07:37,740
Go ahead and open that file.

105
00:07:40,490 --> 00:07:46,130
And the only thing that we need here is the entry point to the demo application, and that is this function

106
00:07:46,130 --> 00:07:46,640
here.

107
00:07:47,150 --> 00:07:50,840
So copy the prototype and let's go back and paste it in.

108
00:07:54,160 --> 00:07:54,610
Okay.

109
00:07:54,740 --> 00:07:56,350
Now just adjust it like so.

110
00:08:00,060 --> 00:08:01,800
Let's also grab the function call.

111
00:08:03,580 --> 00:08:05,050
And the function call is here.

112
00:08:06,940 --> 00:08:12,700
Just copy that and let's go back and paste it into our wi fi application.

113
00:08:12,700 --> 00:08:14,440
Connected events callback function.

114
00:08:15,430 --> 00:08:20,260
And that's because we'll need an Internet connection prior to connecting to a society.

115
00:08:21,460 --> 00:08:25,930
We can also comment out the old US Iot start function call.

116
00:08:27,770 --> 00:08:33,860
Comment this out and we can also get rid of the include for the old a US Iot header.

117
00:08:36,700 --> 00:08:38,440
And that's all we'll need to do here.

118
00:08:38,770 --> 00:08:43,510
Next, let's briefly review the code provided by the example and make some changes wherever necessary.

119
00:08:44,080 --> 00:08:46,330
Let's start with a demo config header file.

120
00:08:47,080 --> 00:08:48,790
And let's just go through this briefly.

121
00:08:49,830 --> 00:08:53,220
The endpoint here will come from the sdhc config once we update it.

122
00:08:54,190 --> 00:08:57,700
And the MQTT port will come from the configuration as well.

123
00:08:59,900 --> 00:09:05,300
And the client identifier also comes from the sdhc config and that will be updated with our thing.

124
00:09:05,300 --> 00:09:05,780
Name.

125
00:09:06,710 --> 00:09:13,070
And the network buffer size also comes from the sdhc config as well as the hardware platform name.

126
00:09:13,070 --> 00:09:17,440
And we'll see how these definitions are defined when we update the sdhc config shortly.

127
00:09:18,110 --> 00:09:22,880
So now let's take a look at the MQTT demo mutual authentication C file.

128
00:09:24,100 --> 00:09:26,980
And this file contains everything that we need to run the demo.

129
00:09:26,980 --> 00:09:32,730
But of course we need to update it so that we can publish the temperature, humidity and the wi fi RSI

130
00:09:32,740 --> 00:09:36,220
and so that it works with our AWS Iot accounts.

131
00:09:36,700 --> 00:09:42,700
So first let's add the include for the PH 22 sensor, and that is so that we can publish the temperature

132
00:09:42,700 --> 00:09:43,450
and humidity.

133
00:09:49,050 --> 00:09:54,210
And let's include the wi fi app as well and that so that we can publish the wi fi RSI.

134
00:10:01,920 --> 00:10:07,740
So also at the top of the file, we have to adjust the root CA definition, the client certificate and

135
00:10:07,740 --> 00:10:09,060
the private key as well.

136
00:10:09,660 --> 00:10:16,170
So let's go ahead and copy the US root CA file name and we can get that from our certs folder.

137
00:10:17,600 --> 00:10:18,800
And then right click.

138
00:10:20,720 --> 00:10:21,650
Then copy.

139
00:10:23,350 --> 00:10:26,620
And let's paste it in for the root CA binary data start.

140
00:10:28,560 --> 00:10:30,810
And for the binary data end as well.

141
00:10:36,680 --> 00:10:38,870
Now we can do the same for the client certificate.

142
00:10:39,050 --> 00:10:43,370
So let's go back to the search folder and then I will just control see.

143
00:10:44,980 --> 00:10:46,630
And then we could paste it in for the start.

144
00:10:52,850 --> 00:10:54,140
Let's do the end as well.

145
00:10:59,030 --> 00:11:00,380
Now for the private key.

146
00:11:02,210 --> 00:11:05,540
Control C to copy and paste it in for the start.

147
00:11:08,700 --> 00:11:09,600
And the end.

148
00:11:13,750 --> 00:11:15,430
Now let's continue down the file.

149
00:11:16,560 --> 00:11:24,300
We have some more defines here for the endpoint link and also the client identifier length and so on.

150
00:11:25,110 --> 00:11:30,300
And then there's also connection re tris and then some others that you may want to look into for customizing

151
00:11:30,300 --> 00:11:31,230
this example.

152
00:11:31,620 --> 00:11:34,110
And here's an important one, which we'll have to update.

153
00:11:34,290 --> 00:11:40,590
This is our topic name, which we had used in the previous a Iot example for publishing of subscribing

154
00:11:40,620 --> 00:11:45,510
to and previously we had defined it in the US Iot C file.

155
00:11:45,540 --> 00:11:46,890
So let's head over there.

156
00:11:49,300 --> 00:11:51,370
And I will just control left to search for it.

157
00:11:55,600 --> 00:11:57,280
And this is how I define mine.

158
00:11:58,220 --> 00:11:58,460
All right.

159
00:11:58,460 --> 00:11:59,900
So I'll go ahead and copy this.

160
00:12:01,630 --> 00:12:03,610
And then go back to the new example file.

161
00:12:05,410 --> 00:12:07,120
And then update the definition here.

162
00:12:09,120 --> 00:12:12,060
And again, this is the topic to subscribe and publish to.

163
00:12:12,720 --> 00:12:19,200
And let's keep moving this example message here we actually won't use as we're going to publish the

164
00:12:19,200 --> 00:12:22,020
temperature humidity and we fire our Cici.

165
00:12:22,380 --> 00:12:24,330
And as we can see from the outline here.

166
00:12:26,530 --> 00:12:31,690
There are quite a few definitions and function prototypes, and I suggest that you go through these

167
00:12:31,690 --> 00:12:32,650
on your own.

168
00:12:32,650 --> 00:12:37,270
If you're interested in customizing this example and adapting it to suit your application needs.

169
00:12:38,080 --> 00:12:42,430
Because what's important for us right now is publishing data to this topic.

170
00:12:42,730 --> 00:12:47,470
We don't want to publish this Hello world message, so let's find out where this definition is used

171
00:12:47,470 --> 00:12:48,740
by using control f.

172
00:12:53,970 --> 00:12:59,580
And here we find that it's used within the published atomic function where the payload and the payload

173
00:12:59,580 --> 00:13:02,310
length are updated with these macro definitions.

174
00:13:02,850 --> 00:13:08,910
So instead of sending the Hello world, let's give it the temperature, humidity and wi fi r a C and

175
00:13:08,910 --> 00:13:10,560
give it the new payload length as well.

176
00:13:10,830 --> 00:13:15,150
And in order to do that, we can grab our print def statement from the old example.

177
00:13:15,480 --> 00:13:18,600
So let's head back over to society.

178
00:13:19,950 --> 00:13:23,070
And we could find that in the a society task.

179
00:13:23,340 --> 00:13:25,020
And let's just copy this line here.

180
00:13:32,620 --> 00:13:34,870
And let's just paste it towards the top of the function.

181
00:13:36,640 --> 00:13:38,890
And we also want the wi fi outside.

182
00:13:39,220 --> 00:13:40,930
So let's add in the text for that.

183
00:13:45,140 --> 00:13:48,390
And then let's give it the function that is wi fi app.

184
00:13:48,410 --> 00:13:49,730
Get RC.

185
00:13:53,460 --> 00:13:55,800
And then why fi RSI is a string.

186
00:13:58,160 --> 00:14:01,100
And the result from the function is an integer.

187
00:14:03,780 --> 00:14:06,600
And let's define the C payload variable up here as well.

188
00:14:17,090 --> 00:14:17,420
All right.

189
00:14:17,420 --> 00:14:20,900
And then we want to update the payload with our C payload variable.

190
00:14:22,870 --> 00:14:26,230
Which will now contain the RSI, temperature and humidity.

191
00:14:26,680 --> 00:14:31,570
And then we also want to provide the length of the payload and we can use str len for that.

192
00:14:34,940 --> 00:14:36,200
And that's all we need to do.

193
00:14:36,770 --> 00:14:41,180
And again, if you want to dig deeper, I suggest reviewing this source file in more detail.

194
00:14:41,210 --> 00:14:47,600
But for now, let's take a look at the US Iot demo main function and check out the description for a

195
00:14:47,600 --> 00:14:48,500
quick overview.

196
00:14:49,370 --> 00:14:56,900
And here it says that the example shown below uses MQTT APIs to send and receive MQTT packets over the

197
00:14:56,900 --> 00:14:59,930
TLS connection established using OpenSSL.

198
00:15:00,170 --> 00:15:04,580
The example is single threaded and uses statically allocated memory.

199
00:15:04,610 --> 00:15:10,340
It uses quality of service level one and therefore implements a retransmission mechanism for published

200
00:15:10,340 --> 00:15:11,060
messages.

201
00:15:12,330 --> 00:15:13,860
So that covers the basics.

202
00:15:14,070 --> 00:15:19,740
And now let's move on to build the project so that we can generate the SDK config file and update the

203
00:15:19,740 --> 00:15:21,030
necessary variables.

204
00:15:21,240 --> 00:15:23,010
So let's go ahead and build the project.

205
00:15:39,650 --> 00:15:41,960
So now let's continue to the sdhc config.

206
00:15:51,510 --> 00:15:57,180
And then here in the example configuration, we can update the client identifier and the endpoint of

207
00:15:57,180 --> 00:15:59,250
the MQTT broker to connect to.

208
00:15:59,280 --> 00:16:00,870
So let's copy the endpoint.

209
00:16:08,880 --> 00:16:10,080
And just paste it in.

210
00:16:12,220 --> 00:16:14,200
But now let's grab the client identify identifier.

211
00:16:17,820 --> 00:16:19,080
And paste it in here.

212
00:16:21,100 --> 00:16:23,110
And be sure to save the configuration.

213
00:16:23,110 --> 00:16:23,710
All right.

214
00:16:24,640 --> 00:16:26,470
So now we can go ahead and flesh it.

215
00:16:26,470 --> 00:16:32,530
Once we're flesh, we'll open the monitor and then head over to the US Iot MQTT Test client.

216
00:16:32,950 --> 00:16:34,270
So let's go ahead and flesh.

217
00:16:41,750 --> 00:16:42,450
So that's okay.

218
00:16:42,470 --> 00:16:42,980
I can just hit.

219
00:16:42,980 --> 00:16:43,670
Proceed.

220
00:16:46,410 --> 00:16:48,180
And I actually forgot to choose my port.

221
00:16:49,250 --> 00:16:50,600
So I'll go ahead and do that.

222
00:16:54,140 --> 00:16:55,370
And then I'll flash again.

223
00:17:00,880 --> 00:17:01,300
Okay, then.

224
00:17:01,300 --> 00:17:02,620
Now we can open the monitor.

225
00:17:15,190 --> 00:17:17,110
Now I'm connecting with the save credentials.

226
00:17:19,870 --> 00:17:21,430
And I'm already showing the published data.

227
00:17:21,460 --> 00:17:22,000
Great.

228
00:17:22,420 --> 00:17:27,790
So next, we can head over to a society and we can check out the activity from that end.

229
00:17:28,150 --> 00:17:29,350
So let's head over there.

230
00:17:32,280 --> 00:17:33,600
And let's click on our thing.

231
00:17:35,200 --> 00:17:36,730
Let's go to the activity tab.

232
00:17:38,040 --> 00:17:41,010
And then here we see the subscribed and connected events.

233
00:17:41,160 --> 00:17:43,440
So that's what our subscribed event looks like.

234
00:17:43,560 --> 00:17:44,610
And the connected.

235
00:17:45,850 --> 00:17:48,400
So now let's go to the MQTT test client.

236
00:17:54,090 --> 00:17:55,470
And then select the topic.

237
00:17:56,770 --> 00:18:03,190
And there we have our published data, the wi fi, RSI, the temperature and the humidity being published

238
00:18:03,190 --> 00:18:06,340
at the interval provided by the example that looks great.

239
00:18:06,940 --> 00:18:12,400
So next, if you want to test publishing from the MQTT test client, we can set the monitors side by

240
00:18:12,400 --> 00:18:16,990
side with a society and then view the activity from the monitor side.

241
00:18:17,140 --> 00:18:19,330
So let's go ahead and put these side by side.

242
00:18:22,100 --> 00:18:22,400
And then.

243
00:18:22,400 --> 00:18:23,780
Now let's hit publish.

244
00:18:30,210 --> 00:18:31,200
And there we go.

245
00:18:31,930 --> 00:18:36,520
The messages are being received on the ESP 332 from a W society.

246
00:18:36,550 --> 00:18:37,930
And that is very cool.

247
00:18:39,330 --> 00:18:45,690
So now that you know how to integrate an example from this version of the ESP a AWS Iot SDK, then you

248
00:18:45,690 --> 00:18:48,720
should have a solid foundation for exploring further on your own.

249
00:18:49,080 --> 00:18:49,350
All right.

250
00:18:49,350 --> 00:18:52,950
So thanks for joining me this far into the course and I hope to see you again soon.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================
