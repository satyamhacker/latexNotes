# Section 1: Introduction to Cloud Computing For Hackers

1
00:00:00,080 --> 00:00:06,200
Now, before we dive into the course content, I'd like to give you a teaser or a taste of what you'll

2
00:00:06,200 --> 00:00:08,870
be able to do by the end of the course.

3
00:00:09,620 --> 00:00:10,070
Now.

4
00:00:10,070 --> 00:00:17,000
Usually in my teaser lectures, I'd give one example to show students what they'll be able to do once

5
00:00:17,000 --> 00:00:18,140
done with the course.

6
00:00:18,140 --> 00:00:21,950
But in this course you're going to learn so many cool things.

7
00:00:21,950 --> 00:00:26,810
So it's unfair and it's really hard for me to pick only one example.

8
00:00:26,810 --> 00:00:33,050
Therefore, instead, I'm going to show you three examples taken from the three main sections of the

9
00:00:33,050 --> 00:00:33,710
course.

10
00:00:34,220 --> 00:00:39,890
Now keep in mind each one of these sections is divided into a number of subsections.

11
00:00:39,890 --> 00:00:46,010
So these examples are only a small fraction of what you'll be able to do once done with the course,

12
00:00:46,010 --> 00:00:52,730
but I think they'll work really well to give you a taste of what you'll be able to achieve once done.

13
00:00:53,440 --> 00:00:59,320
Now, because this is a teaser lecture, I'm not going to explain the technical aspect of how am I doing

14
00:00:59,320 --> 00:00:59,650
this?

15
00:00:59,650 --> 00:01:03,550
Because I'm going to teach you how to do this as you go through the course.

16
00:01:03,550 --> 00:01:06,820
For now, just sit back and enjoy this lecture.

17
00:01:06,820 --> 00:01:12,010
And after this lecture, we're going to dive into the course content where you'll learn how to do things

18
00:01:12,010 --> 00:01:14,230
like this and much, much more.

19
00:01:14,230 --> 00:01:19,780
So first of all, actually before I show you any examples, you're going to learn how to install Kali

20
00:01:19,780 --> 00:01:25,600
Linux, which is a penetration testing operating system on the cloud, and you'll be able to use it

21
00:01:25,600 --> 00:01:27,910
from the terminal using Linux commands.

22
00:01:27,910 --> 00:01:34,000
And you'll also be able to access it from a phone, a tablet, a computer, from any kind of device

23
00:01:34,000 --> 00:01:35,800
that has a web browser.

24
00:01:35,800 --> 00:01:40,450
And that's not even what I wanted to show you in this teaser, guys, what I wanted to show you.

25
00:01:40,450 --> 00:01:44,170
The first example is this Facebook login page.

26
00:01:44,170 --> 00:01:49,870
Now, as you can see, this page is indistinguishable from the actual login page to Facebook.

27
00:01:49,870 --> 00:01:52,690
And you can see that you have the lock icon in here.

28
00:01:52,690 --> 00:01:54,520
The domain name is pretty good.

29
00:01:54,520 --> 00:01:56,500
It's called Facebook login Co.

30
00:01:56,530 --> 00:01:58,720
It's using https.

31
00:01:58,720 --> 00:02:02,260
The only thing is this page is not a real Facebook page.

32
00:02:02,260 --> 00:02:06,010
This is a fishing page that I'm going to show you how to create step by step.

33
00:02:06,010 --> 00:02:11,500
And if the user enter their username and password, it will save them for you, which will allow you

34
00:02:11,500 --> 00:02:13,720
to basically hack their Facebook account.

35
00:02:13,720 --> 00:02:18,100
But I'm going to show you how to do this to any type of account, not just Facebook.

36
00:02:18,100 --> 00:02:21,160
So right here we have an example of a Gmail login page.

37
00:02:21,160 --> 00:02:24,310
And this time it's using two factor authentication.

38
00:02:24,310 --> 00:02:29,110
So even after the user enter their password it's sending them a text message to their phone.

39
00:02:29,110 --> 00:02:33,460
And only if they enter that text message they will gain access to their account.

40
00:02:33,460 --> 00:02:36,970
But again, this is not the real Gmail login page.

41
00:02:36,970 --> 00:02:42,550
This is a phishing page that is registering all of this information, including the cookies, which

42
00:02:42,550 --> 00:02:47,470
will allow you to steal the login information and will also give you access to the account.

43
00:02:47,470 --> 00:02:53,920
Even with two factor or multifactor authentication is used and without the need to even put in the password.

44
00:02:53,920 --> 00:02:56,200
And you'll see all of that step by step.

45
00:02:56,200 --> 00:02:58,900
And this will even work on mobile phones.

46
00:02:58,900 --> 00:03:04,090
So as you can see right here, we have an example of a target that is logging in from their mobile phone,

47
00:03:04,090 --> 00:03:08,080
again with two factor authentication with the text message authentication.

48
00:03:08,080 --> 00:03:12,100
And once they log in you're going to get full access to their computer.

49
00:03:12,640 --> 00:03:18,850
This is a sophisticated attack guys, but I will walk you through it step by step and show you exactly

50
00:03:18,850 --> 00:03:22,120
how to achieve this level of perfection.

51
00:03:22,120 --> 00:03:25,690
Now, this is only one example of one thing that you'll learn in the course guys.

52
00:03:25,690 --> 00:03:29,620
But another example that I want to show you right here is this page.

53
00:03:29,620 --> 00:03:35,260
Again, this page looks identical to the security, which is my own website, my own company.

54
00:03:35,260 --> 00:03:38,950
And as you can see, it's got the lock icon on the top.

55
00:03:38,950 --> 00:03:42,730
It's using Https and we have a proper domain name used on it.

56
00:03:42,730 --> 00:03:46,390
But this page in the background, it runs evil code.

57
00:03:46,390 --> 00:03:50,350
So it will actually allow me to hack any browser that loads this page.

58
00:03:50,350 --> 00:03:56,410
And as a result, I'll be able to execute so many commands on it and even potentially gain full control

59
00:03:56,410 --> 00:03:56,980
over it.

60
00:03:56,980 --> 00:04:02,680
But just as a quick example in here, as you can see, I'm able to see the exact location of the user.

61
00:04:02,680 --> 00:04:06,370
And also I am able to access the webcam.

62
00:04:06,370 --> 00:04:07,090
And here you go.

63
00:04:07,090 --> 00:04:10,510
I have a picture of the target which is myself in this example.

64
00:04:11,070 --> 00:04:17,370
Now, both of these examples are cool, but none of them allow us to gain full remote control over the

65
00:04:17,370 --> 00:04:18,300
target computer.

66
00:04:18,330 --> 00:04:24,090
We're still limited with both of these examples, so how about hacking a computer and gaining the same

67
00:04:24,090 --> 00:04:27,180
control that a normal user has on their computer?

68
00:04:27,210 --> 00:04:28,530
We'll have a look at this.

69
00:04:28,530 --> 00:04:34,350
We have a download link in here that will allow you to download a PDF, which we're claiming is the

70
00:04:34,350 --> 00:04:35,490
manual for Chrome.

71
00:04:35,490 --> 00:04:39,870
And again, as you can see the domain name is very believable download IO.

72
00:04:39,900 --> 00:04:42,900
You can see it's using Https and we have the lock.

73
00:04:42,930 --> 00:04:44,550
Now if you download the PDF.

74
00:04:44,550 --> 00:04:47,940
So this right here is the evil PDF with the backdoor.

75
00:04:47,940 --> 00:04:51,060
And this right here is a clean PDF.

76
00:04:51,060 --> 00:04:53,910
And as you can see the two files look identical.

77
00:04:53,910 --> 00:05:00,090
But if we execute this one right here you'll see again I'll also get the normal behavior that you would

78
00:05:00,090 --> 00:05:01,410
expect from a PDF.

79
00:05:01,410 --> 00:05:04,890
So we're getting a normal file that is the manual for Chrome.

80
00:05:04,890 --> 00:05:10,740
But at the same time it's going to give me full remote control over this computer and I'll be able to

81
00:05:10,740 --> 00:05:12,780
do this again from the cloud.

82
00:05:12,780 --> 00:05:15,780
So the cloud basically enhances everything that we do.

83
00:05:15,780 --> 00:05:19,770
Because right now I can control this computer from any device.

84
00:05:19,770 --> 00:05:21,090
I can do it from my phone.

85
00:05:21,090 --> 00:05:25,530
I can do it from my tablet, from my computer, from any device that has a web browser.

86
00:05:25,530 --> 00:05:30,420
So as you can see through this interface, I actually don't need to execute any commands.

87
00:05:30,420 --> 00:05:34,740
I can control it from this web interface that works on any web browser.

88
00:05:34,740 --> 00:05:40,620
And I can access the file system, take screenshots, access the camera, the keyboard, and even run

89
00:05:40,620 --> 00:05:43,050
ransomware on the target computer.

90
00:05:43,290 --> 00:05:46,920
Like I said, guys, these are only small examples from the whole course.

91
00:05:46,920 --> 00:05:51,870
You will be learning much more throughout this course, and also I'll be teaching you how to do this

92
00:05:51,870 --> 00:05:53,730
step by step, so don't worry about it.

93
00:05:53,730 --> 00:05:55,410
Don't feel like it's complicated.

94
00:05:55,410 --> 00:05:57,750
I will show you exactly how to do this.

95
00:05:57,750 --> 00:06:01,020
And as usual, you can ask me as many questions as you want.

96
00:06:01,020 --> 00:06:06,060
And also keep in mind these all of these attacks are running from the cloud, so you can use them to

97
00:06:06,060 --> 00:06:10,260
target anybody that has internet access, regardless of where they are.

98
00:06:10,260 --> 00:06:12,360
They can be anywhere in the world.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,350 --> 00:00:03,440
The cloud we hear of this time often.

2
00:00:03,440 --> 00:00:08,840
But what does it really mean and why is it important for us to learn as hackers?

3
00:00:09,080 --> 00:00:14,960
In my opinion, the terms the cloud is just a marketing terms or a buzzword because we had the cloud

4
00:00:14,960 --> 00:00:18,170
years before it was even called the cloud.

5
00:00:18,770 --> 00:00:26,000
The terms the cloud or cloud computing refers to the idea of using remote computers to provide services

6
00:00:26,000 --> 00:00:27,170
on the internet.

7
00:00:27,200 --> 00:00:30,650
These services could be web applications websites.

8
00:00:30,650 --> 00:00:36,800
You can even use it to store data or run normal applications, because at the end of the day, this

9
00:00:36,800 --> 00:00:41,150
is just a computer that exists in a remote location.

10
00:00:41,150 --> 00:00:47,720
So the key word here is remote computers on the internet, because everything that you can do on cloud

11
00:00:47,720 --> 00:00:52,430
computers can actually be done on personal local computers.

12
00:00:52,430 --> 00:00:59,750
So it's very important to understand that the cloud is simply made up of a number of normal computers

13
00:00:59,750 --> 00:01:06,410
running normal operating systems, and normal applications that can be installed on normal personal

14
00:01:06,410 --> 00:01:07,790
local computers.

15
00:01:07,790 --> 00:01:15,530
The only difference is cloud computers or servers are designed to be always connected to the internet,

16
00:01:15,530 --> 00:01:22,400
and therefore they'll be always available to any device that is also connected to the internet.

17
00:01:22,400 --> 00:01:29,870
So if you run a service or a website on any of these computers, they'll be accessible to anybody that

18
00:01:29,870 --> 00:01:31,880
is connected to the internet.

19
00:01:31,880 --> 00:01:38,570
Unlike what happens if you run a service on a website, on a computer, on a local network.

20
00:01:38,570 --> 00:01:45,860
That service or website will only be accessible to other computers within the local network, but it

21
00:01:45,860 --> 00:01:49,340
will not be accessible to other local networks.

22
00:01:49,340 --> 00:01:54,800
So if you run a website on this computer, it will only be accessible to computers within this network.

23
00:01:54,800 --> 00:01:55,910
Same goes here.

24
00:01:55,910 --> 00:02:02,450
If you run a service on this computer, it will only be accessible to computers within this network.

25
00:02:02,450 --> 00:02:10,040
On the other hand, if a service or website is run on a cloud computer in here, this service will be

26
00:02:10,040 --> 00:02:16,490
accessible to computers in this network and in this network, and to any other network that is connected

27
00:02:16,490 --> 00:02:17,570
to the internet.

28
00:02:17,570 --> 00:02:23,780
Because these networks are connected to the internet, and these cloud servers are designed to expose

29
00:02:23,780 --> 00:02:30,350
their services to the internet, and therefore will be accessible to any device that is connected to

30
00:02:30,350 --> 00:02:31,220
the internet.

31
00:02:32,080 --> 00:02:39,010
So basically the cloud is just a terme to make it easier for people to visualize how some services can

32
00:02:39,010 --> 00:02:43,570
be accessed remotely from anywhere in the world because they are in the cloud.

33
00:02:43,570 --> 00:02:50,560
But basically it just means that they are connected to the internet, have a real IP address, and therefore

34
00:02:50,560 --> 00:02:54,400
any computer that is connected to the internet can communicate with them.

35
00:02:55,620 --> 00:03:02,610
So from what we said earlier, it is clear you can expose any computer to the cloud or to the internet,

36
00:03:02,610 --> 00:03:08,160
and you can even have web servers and databases or any kind of server installed on your own personal

37
00:03:08,160 --> 00:03:14,190
computer, just like what we have in here, and just configure it to be accessible over the internet

38
00:03:14,190 --> 00:03:15,510
or over the cloud.

39
00:03:16,020 --> 00:03:22,080
But that brings a number of issues, because you want the services to be always accessible over the

40
00:03:22,080 --> 00:03:22,650
internet.

41
00:03:22,650 --> 00:03:28,290
Therefore, this computer needs to always be on and it also always needs to have internet.

42
00:03:28,290 --> 00:03:33,930
And if this service is used by a lot of people, it needs to have fast and reliable internet connection.

43
00:03:33,930 --> 00:03:38,070
And obviously all of that adds up to a lot of bills and you have to maintain it.

44
00:03:38,070 --> 00:03:42,960
Therefore, we have companies that basically give you servers on the internet.

45
00:03:42,960 --> 00:03:49,410
So it's not your own computer, it's just a computer that is pre-configured pre hosted by a certain

46
00:03:49,410 --> 00:03:50,220
company.

47
00:03:50,220 --> 00:03:53,250
And it's also connected to really fast internet.

48
00:03:53,250 --> 00:03:55,320
It's always well maintained and so on.

49
00:03:55,320 --> 00:03:59,940
And all you have to do is simply pay a subscription to use this computer.

50
00:03:59,940 --> 00:04:05,460
So you're basically renting this computer to host your own services, your own servers and so on.

51
00:04:06,000 --> 00:04:10,650
And usually these companies don't only have one server, they have a cluster of servers.

52
00:04:10,650 --> 00:04:12,720
And you basically just rent one.

53
00:04:12,720 --> 00:04:18,390
And then if your server or website becomes more popular and you get more users, you can actually start

54
00:04:18,390 --> 00:04:19,740
renting more and more.

55
00:04:19,740 --> 00:04:25,170
And that's one of the main reasons why people use these services, because it's very scalable.

56
00:04:25,170 --> 00:04:30,450
So you can start with something small that doesn't cost you much and then build it up as you go.

57
00:04:30,450 --> 00:04:35,700
And like I said, you don't have to worry about things such as the internet connection, having it always

58
00:04:35,700 --> 00:04:38,640
on, keeping it well maintained and so on.

59
00:04:39,210 --> 00:04:43,020
Now there is a lot of services that do that and you probably heard them.

60
00:04:43,020 --> 00:04:46,470
The most popular one is Amazon AWS.

61
00:04:46,500 --> 00:04:52,860
This is the most popular cloud provider in the world, but there are a lot of other cloud providers

62
00:04:52,860 --> 00:04:57,120
such as Microsoft, linode, DigitalOcean, and so on.

63
00:04:57,360 --> 00:04:59,220
Basically, all of them do the same.

64
00:04:59,220 --> 00:05:04,470
They allow you to use servers on the internet, but obviously each one of them has their own packages,

65
00:05:04,470 --> 00:05:06,540
their on pros and cons.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:05,970
So now that we understand the meaning of cloud computing, its importance for hacking should be very

2
00:00:05,970 --> 00:00:06,600
clear.

3
00:00:06,600 --> 00:00:10,950
So first of all, it's going to allow us to understand how websites work.

4
00:00:11,100 --> 00:00:15,120
You'll also understand how other cloud services work in general.

5
00:00:15,120 --> 00:00:20,640
For example any application, whether it's running on your mobile, on your computer, or even on your

6
00:00:20,640 --> 00:00:26,910
TV, if it's communicating with the internet and asking for internet access, then it's actually communicating

7
00:00:26,910 --> 00:00:28,620
with a cloud application.

8
00:00:28,620 --> 00:00:34,710
A lot of the time, what runs locally on your device is simply an interface, and the actual work is

9
00:00:34,710 --> 00:00:36,000
done on the cloud.

10
00:00:36,300 --> 00:00:41,700
You're also going to be able to run and host your own websites and cloud services, and use them for

11
00:00:41,700 --> 00:00:42,540
any use you want.

12
00:00:42,540 --> 00:00:47,820
They can be normal websites, or you can be running phishing websites, or fake websites or websites

13
00:00:47,820 --> 00:00:53,820
with malicious code that allow you to control the browser of the target or clone login pages and bypass

14
00:00:53,820 --> 00:00:57,090
two factor authentication and steal usernames and passwords.

15
00:00:57,240 --> 00:01:03,480
You'll be able to run your own hacking services, such as file sharing services that are tailored to

16
00:01:03,480 --> 00:01:05,400
be used to deliver malware.

17
00:01:05,400 --> 00:01:12,000
You'll be able to run your own VPN service or your own proxies to hide yourself and protect your privacy

18
00:01:12,000 --> 00:01:13,290
and anonymity.

19
00:01:13,320 --> 00:01:18,840
You can even host your own hacking machine, so this could be any operating system, like I said.

20
00:01:18,840 --> 00:01:23,670
Or you can even host a hacking operating system such as Kali Linux on the cloud.

21
00:01:23,670 --> 00:01:28,980
And that way you'll be able to run these programs from that cloud computer instead of running them from

22
00:01:28,980 --> 00:01:30,420
your own local computer.

23
00:01:30,420 --> 00:01:34,860
So that comes with a number of benefits, again, protecting your privacy and anonymity.

24
00:01:34,860 --> 00:01:40,980
If it's done properly, you can run EC2 or a command and control server and use it to control all of

25
00:01:40,980 --> 00:01:42,330
the computers that you hacked.

26
00:01:42,330 --> 00:01:47,400
So your backdoors send the connection back to your computer on the cloud instead of sending them to

27
00:01:47,400 --> 00:01:48,690
your local computer.

28
00:01:48,690 --> 00:01:52,350
That way it's always on and it's always ready to receive connections.

29
00:01:52,350 --> 00:01:58,260
And you're also not limited to the resources of your own local computer because like I said, the cloud

30
00:01:58,260 --> 00:01:59,310
is very scalable.

31
00:01:59,310 --> 00:02:04,740
So you can actually use computers that are much more powerful than your own computer and run programs

32
00:02:04,740 --> 00:02:06,720
that cannot run on your computer.

33
00:02:06,720 --> 00:02:09,060
You can even use that for password cracking.

34
00:02:09,060 --> 00:02:14,340
And with the power of the cloud, you're going to be able to crack passwords much faster than you would

35
00:02:14,340 --> 00:02:16,110
on your own local computer.

36
00:02:16,110 --> 00:02:18,270
So the uses of this are endless.

37
00:02:18,270 --> 00:02:24,120
And that's why I think it is essential for an ethical hacker to learn how to use the cloud for hacking.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 2: Cloud Basics

1
00:00:00,080 --> 00:00:03,230
Now there is a lot of cloud providers out there.

2
00:00:03,230 --> 00:00:08,600
But anyway, the stuff that we're going to cover is pretty much the same, regardless of what cloud

3
00:00:08,600 --> 00:00:09,860
provider you go with.

4
00:00:09,890 --> 00:00:15,680
Obviously, the interface might be slightly different the way you sign up, and the pricing will be

5
00:00:15,680 --> 00:00:16,550
slightly different.

6
00:00:16,550 --> 00:00:22,550
But then once you get over that, the general idea of what we're doing is going to be the same regardless

7
00:00:22,550 --> 00:00:24,710
of what cloud provider you choose.

8
00:00:25,190 --> 00:00:28,490
Amazon is the most popular cloud provider out there.

9
00:00:28,490 --> 00:00:30,860
It offers so many cloud services.

10
00:00:30,860 --> 00:00:35,840
It might seem a bit tricky to start with, but we're still going to start with it because first of all,

11
00:00:35,840 --> 00:00:41,390
it allows us to use their service for free for a whole year if you stick with the low end servers.

12
00:00:41,390 --> 00:00:46,970
So not with the ones that have a lot of resources, and it's the only one that I know of that we can

13
00:00:46,970 --> 00:00:49,550
deploy a Kali machine in it straight away.

14
00:00:49,580 --> 00:00:54,440
Now, I'm not saying that you can't do it with the others, but it's much easier with Amazon.

15
00:00:55,040 --> 00:01:00,920
In general, though in terms of ease of use, linode would probably be better, and even depending on

16
00:01:00,920 --> 00:01:03,710
your application, it might be better overall.

17
00:01:04,330 --> 00:01:07,510
But we're going to start with Amazon because it's the most popular.

18
00:01:07,510 --> 00:01:11,860
They give us a year free with the low end server, which is enough for what we want to do.

19
00:01:11,860 --> 00:01:18,190
And it's the only one that allows us to deploy Kali straight away without having to do any extra steps.

20
00:01:19,090 --> 00:01:24,610
So first of all, you're going to have to sign up to an account with Amazon AWS.

21
00:01:24,610 --> 00:01:28,000
So you need to go to Aws.amazon.com.

22
00:01:28,390 --> 00:01:32,470
And then we're simply going to click on Get Started for free or sign up.

23
00:01:32,470 --> 00:01:36,940
If the page layout changes we're going to click on Create a Free account.

24
00:01:38,210 --> 00:01:41,150
And you want to fill this up with your own information.

25
00:01:41,150 --> 00:01:44,210
Now it will ask you for credit card information.

26
00:01:44,210 --> 00:01:48,680
You need that for them to verify that you're a real person and you're not just somebody that is just

27
00:01:48,680 --> 00:01:50,450
going to use the services and go.

28
00:01:50,480 --> 00:01:53,630
They will not charge you if you stick with the free servers.

29
00:01:53,630 --> 00:01:55,550
And I'm going to show you how to use the free servers.

30
00:01:55,550 --> 00:01:57,050
So don't worry about that.

31
00:01:57,050 --> 00:02:02,510
You can put your credit card information and they won't charge you as long as you don't actually purchase

32
00:02:02,510 --> 00:02:03,710
paid servers.

33
00:02:04,310 --> 00:02:05,570
Signing up is very simple.

34
00:02:05,570 --> 00:02:08,990
I'm going to skip it, but if you face any questions, obviously ask me.

35
00:02:08,990 --> 00:02:10,070
We'll be happy to help.

36
00:02:10,070 --> 00:02:12,290
But it's just like signing up to any other service.

37
00:02:12,290 --> 00:02:17,090
You fill up the information they request and you verify your account and you'll be good to go.

38
00:02:17,750 --> 00:02:23,210
As you're going through the signup process, make sure you always select the options that say free beside

39
00:02:23,210 --> 00:02:23,540
it.

40
00:02:23,540 --> 00:02:29,180
This process changes often, so it's important to make sure that you always look for whatever it says

41
00:02:29,180 --> 00:02:31,550
free, and make sure you select the free option.

42
00:02:32,260 --> 00:02:36,160
Once you're done with everything, you're going to get a success message like this.

43
00:02:36,160 --> 00:02:43,750
And you can simply click on go to AWS Management Console to go to your home or main account page.

44
00:02:44,330 --> 00:02:48,440
As usual, when you're doing this, it's not always a perfect scenario.

45
00:02:48,470 --> 00:02:53,360
When I was signing up, it showed me a message saying that this signup process is taking longer than

46
00:02:53,360 --> 00:02:53,930
usual.

47
00:02:53,930 --> 00:02:59,480
It could take up to 24 hours, so contact us if the account is not activated within 24 hours.

48
00:02:59,480 --> 00:03:03,200
So I actually had to wait about half an hour for the account to be activated.

49
00:03:03,200 --> 00:03:05,660
So these delays are to be expected.

50
00:03:05,960 --> 00:03:11,540
Now what I'm going to do is I'm actually just going to sign out, and I just want to show you how you

51
00:03:11,540 --> 00:03:16,610
would log in into this again, because as you saw earlier, we just got pretty much redirected to it.

52
00:03:16,610 --> 00:03:24,650
So once you sign up, if you want to sign in to your account, all you have to do is go to Aws.amazon.com

53
00:03:24,650 --> 00:03:27,080
same domain that we use to sign up.

54
00:03:27,410 --> 00:03:29,330
We're going to click on Sign in.

55
00:03:31,360 --> 00:03:34,330
You're going to put the email that you signed up with.

56
00:03:36,260 --> 00:03:37,910
Put the password.

57
00:03:39,510 --> 00:03:41,010
And you're back where we were.

58
00:03:41,010 --> 00:03:42,210
This is your home.

59
00:03:42,210 --> 00:03:46,230
Your control panel to your Amazon cloud account.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================
