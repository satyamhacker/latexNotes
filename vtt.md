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

1
00:00:00,110 --> 00:00:05,810
The first operating system that we're going to install is Kali Linux.

2
00:00:06,170 --> 00:00:10,910
See, throughout the course we're going to use a number of hacking tools.

3
00:00:11,300 --> 00:00:14,210
You can install each of these tools manually.

4
00:00:14,210 --> 00:00:21,620
Or you can do what most hackers do, including myself, and save time and effort and use an operating

5
00:00:21,620 --> 00:00:23,810
system designed for hacking.

6
00:00:24,440 --> 00:00:28,040
We're going to use an operating system called Kali Linux.

7
00:00:28,070 --> 00:00:35,780
It's a Linux distro based on Debian, and the only difference between Kali and the actual original Debian

8
00:00:35,780 --> 00:00:43,370
Linux distro is the fact that Kali has a lot of hacking and penetration testing tools, pre-installed

9
00:00:43,370 --> 00:00:45,260
and pre-configured in it.

10
00:00:45,290 --> 00:00:52,250
Therefore, once you install Kali, you will have access to so many hacking tools without the need to

11
00:00:52,250 --> 00:00:57,710
install or configure any of them, which will save you a lot of time and a lot of effort.

12
00:00:58,220 --> 00:01:03,920
Obviously, if you do that, you'll be able to achieve all of this because Kali has its own web server,

13
00:01:03,920 --> 00:01:07,700
so you'll be able to use it to host your own website and cloud services.

14
00:01:07,700 --> 00:01:12,110
You'll be able to run your own hacking tools because it comes with a lot of hacking tools.

15
00:01:12,110 --> 00:01:19,130
As you know, it is a hacking machine, and if you install it on a cloud server that has a lot of resources,

16
00:01:19,130 --> 00:01:25,100
then you'll be able to use the password crackers, the cracking tools that come with Kali to crack passwords

17
00:01:25,100 --> 00:01:26,330
very, very quickly.

18
00:01:26,600 --> 00:01:30,020
I cover this in a YouTube video, but don't watch it now.

19
00:01:30,020 --> 00:01:33,500
Watch it at the end of this section because it will make more sense then.

20
00:01:33,890 --> 00:01:34,790
And you're back.

21
00:01:34,790 --> 00:01:40,040
This is your home, your control panel to your Amazon Cloud account.

22
00:01:40,990 --> 00:01:42,790
So we're going to scroll down.

23
00:01:43,240 --> 00:01:47,200
And in here it's giving you a number of options to build a solution.

24
00:01:47,200 --> 00:01:51,070
And the first one is to launch a virtual machine, which is what we want to do.

25
00:01:51,100 --> 00:01:53,110
We want to start a Kali machine.

26
00:01:53,560 --> 00:01:55,780
So let's open this in a new tab.

27
00:01:57,210 --> 00:02:02,850
And even though this looks pretty cluttered and it might seem complex, it's actually very, very simple.

28
00:02:03,240 --> 00:02:08,670
Basically, first of all, it's asking you to give a name to this computer, to this virtual machine

29
00:02:08,670 --> 00:02:13,770
that you're going to create, and let's call it Kali, because it's going to be a Kali machine.

30
00:02:14,130 --> 00:02:20,190
And if you scroll down, it's giving you the application or the OS, the operating system that you want

31
00:02:20,190 --> 00:02:20,880
to start.

32
00:02:21,330 --> 00:02:26,730
So in here, it's giving you a nice slider that contains the most common operating systems that people

33
00:02:26,730 --> 00:02:27,600
usually use.

34
00:02:27,600 --> 00:02:32,100
So you've got ubuntu, windows, Red hat, Mac OS and so on.

35
00:02:32,670 --> 00:02:36,300
Alternatively, you can click on Browse More Amis.

36
00:02:36,300 --> 00:02:43,560
Basically, an Ami is an Amazon Virtual machine, so you could use the search bar in here to search

37
00:02:43,560 --> 00:02:47,520
the marketplace for whatever virtual machine you want to start.

38
00:02:47,520 --> 00:02:55,890
So you can see in the quick start we only have 44, but in the marketplace we got 5000 and 485 machines.

39
00:02:55,890 --> 00:03:01,470
So you could simply just in here type hacking and you'll get all the virtual machines that you could

40
00:03:01,470 --> 00:03:04,440
start that contain the word hacking in them.

41
00:03:04,860 --> 00:03:06,330
You could read the description.

42
00:03:06,330 --> 00:03:10,140
You could even look up on Google what features these virtual machines have.

43
00:03:10,140 --> 00:03:12,300
But we want to run a Kali machine.

44
00:03:12,300 --> 00:03:13,890
So I'm just going to type Kali.

45
00:03:13,890 --> 00:03:17,520
And as you can see, we have a Kali machine in here.

46
00:03:17,520 --> 00:03:20,280
You'll always see the latest current version in here.

47
00:03:20,890 --> 00:03:23,890
So we're just going to click on select.

48
00:03:24,520 --> 00:03:27,670
And as you can see it's saying it's eligible for the free tier.

49
00:03:27,670 --> 00:03:28,720
So that's perfect.

50
00:03:28,720 --> 00:03:30,280
So we can go ahead with it.

51
00:03:30,280 --> 00:03:32,200
We're going to click on continue.

52
00:03:33,670 --> 00:03:37,780
And we're back to the same page where we were selecting the operating system.

53
00:03:37,780 --> 00:03:41,350
But as you can see now, Kali Linux is selected for us.

54
00:03:41,350 --> 00:03:47,740
So once we finish this process, Amazon is going to create a Kali machine for us on their servers.

55
00:03:48,480 --> 00:03:52,440
Now, if we scroll down, it's asking us for the instance type.

56
00:03:52,440 --> 00:03:58,320
So the machine type or the resources of the machine that we will install Kali on.

57
00:03:59,390 --> 00:04:01,730
So we can use the drop down to change that.

58
00:04:01,730 --> 00:04:04,160
And we want to make sure we go for the free one.

59
00:04:04,160 --> 00:04:07,460
So as you can see, we can go for this one and this one.

60
00:04:07,460 --> 00:04:10,820
These are the only two that are eligible for free.

61
00:04:10,820 --> 00:04:13,370
If you go for the others, you will be charged.

62
00:04:13,730 --> 00:04:17,480
So we're going to go with this one because it has the higher spec than this one.

63
00:04:17,480 --> 00:04:20,900
So it's going to come with one CPU and one gigabyte of memory.

64
00:04:20,900 --> 00:04:24,050
So not a lot of resources, but it should do for now.

65
00:04:25,150 --> 00:04:32,980
Next, we'll have to create a key pair, which will be used to log in to this computer that we are creating

66
00:04:32,980 --> 00:04:33,910
on the cloud.

67
00:04:34,570 --> 00:04:42,130
So basically what we're doing is we're creating a Kali machine on Amazon's cloud servers.

68
00:04:42,130 --> 00:04:45,730
But we don't have physical access to this computer.

69
00:04:45,730 --> 00:04:47,680
It's at Amazon's servers.

70
00:04:47,680 --> 00:04:54,340
Therefore for us to be able to use it, we're going to have to communicate with it using a service or

71
00:04:54,340 --> 00:04:57,310
using a tunnel that is called SSH.

72
00:04:58,050 --> 00:05:04,800
So SSH is a service that allows us to remotely control computers on the internet.

73
00:05:05,310 --> 00:05:08,610
Now, obviously you can't control any computer you want.

74
00:05:08,610 --> 00:05:12,990
There has to be some kind of authentication between you and the server.

75
00:05:12,990 --> 00:05:15,720
And we do that using keys.

76
00:05:15,840 --> 00:05:24,120
So we create a public key on the server and a private key that will be kept by you by the user.

77
00:05:24,450 --> 00:05:27,270
Now this private key serves like a password.

78
00:05:27,270 --> 00:05:29,640
So you should never share it with anybody.

79
00:05:29,640 --> 00:05:35,790
And you're going to use it in order to authenticate with the server, with the computer that we're creating

80
00:05:35,790 --> 00:05:36,660
on the cloud.

81
00:05:36,660 --> 00:05:43,860
And it will only allow you to control it over SSH if your private key matches the public key.

82
00:05:44,860 --> 00:05:51,820
So in here, it's asking us whether we want to use an existing key pair or if we want to create a new

83
00:05:51,820 --> 00:05:52,450
key pair.

84
00:05:52,480 --> 00:05:57,190
Now, I've never created one, so I'm going to click on create a new key pair.

85
00:05:57,640 --> 00:06:00,160
We're going to set a name for this key pair.

86
00:06:00,160 --> 00:06:03,580
So we're just going to name it curly key pair.

87
00:06:04,850 --> 00:06:07,310
We're going to keep the options in here the same.

88
00:06:07,310 --> 00:06:09,950
And we're going to click on create a key pair.

89
00:06:10,460 --> 00:06:14,360
So as you can see now Amazon automatically downloaded a file.

90
00:06:14,360 --> 00:06:17,540
For me it's called Kali dash Keypair pem.

91
00:06:18,170 --> 00:06:23,690
And this is the private key which I'm going to use to authenticate with the server.

92
00:06:24,050 --> 00:06:28,880
And it automatically stored the public key in the server in the right location.

93
00:06:28,880 --> 00:06:31,130
So I don't need to worry about this key.

94
00:06:31,130 --> 00:06:36,680
But later on, once the machine is created, I'm going to use the private key that I have in my downloads.

95
00:06:36,680 --> 00:06:43,970
Right now it's called Kali Keypair PEM to authenticate and log in to my Kali machine that is stored

96
00:06:43,970 --> 00:06:44,930
on the cloud.

97
00:06:45,650 --> 00:06:50,210
If you scroll down, it'll give you some network settings that you can modify, but we're going to leave

98
00:06:50,210 --> 00:06:51,830
everything the same in here.

99
00:06:51,830 --> 00:06:57,410
You could tick these boxes to allow connections to the web server, but I'm going to show you how to

100
00:06:57,410 --> 00:07:00,980
do that later on anyway, so you don't need to take any of this.

101
00:07:01,970 --> 00:07:07,370
Scrolling down, you're going to get to the storage configuration, where you could configure the amount

102
00:07:07,370 --> 00:07:10,280
of storage that your computer is going to have.

103
00:07:10,310 --> 00:07:14,840
You could also set advanced settings in here, but we're going to leave that for now.

104
00:07:14,870 --> 00:07:19,070
You could also see a summary of everything that we selected so far.

105
00:07:19,070 --> 00:07:21,590
So we're creating a Kali Linux machine.

106
00:07:21,590 --> 00:07:23,030
This is the instance type.

107
00:07:23,030 --> 00:07:25,010
We selected this because it's the free one.

108
00:07:25,010 --> 00:07:27,080
It's not the most powerful but it's free.

109
00:07:27,110 --> 00:07:29,210
You can see we have no firewall settings.

110
00:07:29,210 --> 00:07:30,740
We'll talk about that later.

111
00:07:30,740 --> 00:07:33,380
The amount of storage we have 12GB.

112
00:07:33,380 --> 00:07:35,600
Now we're actually eligible for 30.

113
00:07:35,600 --> 00:07:38,360
So I'm actually going to change that here to 30.

114
00:07:38,360 --> 00:07:43,850
But make sure you stick with whatever you're allowed for for the free tier if you don't want to spend

115
00:07:43,850 --> 00:07:44,630
anything.

116
00:07:45,050 --> 00:07:47,510
And we're going to click on Launch Instance.

117
00:07:49,250 --> 00:07:52,850
So now Amazon is going to do everything automatically for you.

118
00:07:52,850 --> 00:07:59,390
It's going to create a new computer on their cloud servers, install the latest Kali on it and install

119
00:07:59,390 --> 00:08:00,980
the public key on it.

120
00:08:00,980 --> 00:08:08,330
So then you can log in to that computer using SSH using the private key that we just downloaded in here.

121
00:08:08,330 --> 00:08:11,330
And I'm going to show you how to do that in the next lecture.

122
00:08:11,690 --> 00:08:17,480
Now I'm getting another message similar to what I got when I was signing up with the verification problem.

123
00:08:17,480 --> 00:08:19,280
It was telling me it might take some time.

124
00:08:19,280 --> 00:08:20,030
So same here.

125
00:08:20,030 --> 00:08:23,570
It's saying that this machine is taking a little bit extra time than usual.

126
00:08:23,570 --> 00:08:24,620
Give it some time.

127
00:08:24,620 --> 00:08:27,260
Try again in about half an hour or so.

128
00:08:27,260 --> 00:08:28,190
That's what I'm going to do.

129
00:08:28,190 --> 00:08:30,710
I'm going to pause the video, keep trying until it works.

130
00:08:30,710 --> 00:08:32,840
And then we're going to resume and continue.

131
00:08:33,200 --> 00:08:38,450
You can also click on the launch log to see where it's failing or where it's getting stuck.

132
00:08:38,450 --> 00:08:41,840
And we can see we're getting stuck at the subscription marketplace.

133
00:08:41,840 --> 00:08:43,520
But anyway, I gave it some time.

134
00:08:43,520 --> 00:08:49,400
So I'm going to click on View All Instances in here to see if my instance is ready.

135
00:08:49,400 --> 00:08:53,330
And as you can see, my Kali machine right now is actually running.

136
00:08:53,330 --> 00:08:56,690
And I can actually go ahead and connect to it and use it.

137
00:08:56,690 --> 00:08:59,840
And I'm going to show you how to do that in the next lecture.

138
00:08:59,840 --> 00:09:05,750
If you ever wanted to come back to this page where you can see your machines after you log in, all

139
00:09:05,750 --> 00:09:10,280
you have to do is simply click on services and click on EC2.

140
00:09:10,730 --> 00:09:16,730
Amazon has a number of categories for their cloud services, and the Kali machine that we created falls

141
00:09:16,730 --> 00:09:18,650
under the EC2 category.

142
00:09:18,650 --> 00:09:23,960
Therefore, all you have to do is click in here and you will end up in this page where you can see it

143
00:09:23,960 --> 00:09:24,830
and manage it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:05,810
Now that we have the Kali machine installed and it's running on the cloud, let's go ahead and see how

2
00:00:05,810 --> 00:00:10,040
we can connect to it, control it, and maybe hack some computers.

3
00:00:10,040 --> 00:00:16,670
As mentioned previously, we're going to use a program called SSH to connect from our local computer

4
00:00:16,670 --> 00:00:19,490
to the remote Kali machine and control it.

5
00:00:19,490 --> 00:00:26,750
Now SSH is a command line program, which means that we can only use it to control the cloud computer

6
00:00:26,750 --> 00:00:28,730
using the system commands.

7
00:00:28,730 --> 00:00:35,600
We are limited to this at the moment because we just installed our cloud computer, and it actually

8
00:00:35,600 --> 00:00:38,210
does not have a graphical user interface.

9
00:00:38,210 --> 00:00:44,660
I will show you how to install a graphical user interface on it in the future, but for now we're going

10
00:00:44,660 --> 00:00:46,700
to have to use it using SSH.

11
00:00:46,700 --> 00:00:52,580
And we're actually going to communicate with this computer using SSH often because it is actually much

12
00:00:52,580 --> 00:00:54,020
quicker and faster.

13
00:00:54,020 --> 00:00:58,100
So you're going to get very comfortable with the command line as we go through the course.

14
00:00:58,550 --> 00:01:04,610
So first of all, before we can use SSH we're going to have to change the permissions of the key file

15
00:01:04,610 --> 00:01:11,930
that we downloaded so that it can be used with SSH in order to authenticate us with our cloud computer.

16
00:01:12,350 --> 00:01:16,850
Usually on windows the key file should have the correct permissions when downloaded.

17
00:01:16,850 --> 00:01:21,890
But just to make sure that it does, we're going to go to the downloads folder where we downloaded it

18
00:01:21,890 --> 00:01:23,660
and I'm going to right click it.

19
00:01:23,780 --> 00:01:30,980
Go to properties and under the security tab select the username that you are logged in with from this

20
00:01:30,980 --> 00:01:31,940
list in here.

21
00:01:31,940 --> 00:01:38,570
Currently I'm logged in as user and you want to make sure that all of these permissions are ticked.

22
00:01:38,570 --> 00:01:44,930
If they are not, you can simply click the edit in here and make sure you tick all of the boxes that

23
00:01:44,930 --> 00:01:47,420
you see in here, except for the last one.

24
00:01:48,100 --> 00:01:52,630
As you can see, in my case, it's already set properly, so I don't need to edit anything.

25
00:01:52,630 --> 00:01:58,180
And we can actually go ahead and connect to our server using SSH from the command prompt.

26
00:01:58,180 --> 00:02:02,200
So you want to go to the start menu and look for CMD.

27
00:02:02,680 --> 00:02:04,420
You're going to get the command prompt here.

28
00:02:04,420 --> 00:02:06,940
Simply click it or hit enter to run it.

29
00:02:06,940 --> 00:02:09,760
So in here you're going to be able to execute the commands.

30
00:02:09,760 --> 00:02:11,410
And we're going to be using SSH.

31
00:02:11,410 --> 00:02:15,010
And you'll be able to see the results of your commands here as well.

32
00:02:15,010 --> 00:02:17,050
And I'll show you that command next.

33
00:02:17,050 --> 00:02:20,890
But before we do that let me show you how to also change the permissions.

34
00:02:20,890 --> 00:02:28,240
If you are using Linux or Apple Mac OS on Linux, depending on the distribution that you have installed,

35
00:02:28,240 --> 00:02:30,610
you should see it in the dock in here.

36
00:02:30,610 --> 00:02:33,850
If you don't see it, you can go to all applications.

37
00:02:33,850 --> 00:02:36,190
And again simply look for terminal.

38
00:02:36,190 --> 00:02:37,750
And in my case I have it here.

39
00:02:37,750 --> 00:02:42,340
Again, if you click it, you'll get a similar application to what we have here on windows.

40
00:02:42,340 --> 00:02:45,760
Again you can run the commands in here and you'll see the results in here.

41
00:02:46,390 --> 00:02:53,530
And finally on macOS, if you don't have it in your dock in here, you should go to all applications

42
00:02:53,530 --> 00:02:55,270
and look for terminal.

43
00:02:55,360 --> 00:02:58,900
See an icon similar to the icons on Windows and Linux.

44
00:02:58,900 --> 00:03:00,940
And again, the program looks very similar.

45
00:03:00,940 --> 00:03:04,690
You run the command in here and you see the results in here as well.

46
00:03:04,690 --> 00:03:06,340
So we're going to do chmod.

47
00:03:06,340 --> 00:03:09,010
We're going to select the permissions which is 700.

48
00:03:09,010 --> 00:03:12,610
And then we're going to give it the location where that file is stored.

49
00:03:12,610 --> 00:03:20,140
And as we mentioned it's in my downloads and it's called kali dash keypair dot pem.

50
00:03:20,470 --> 00:03:24,340
So a very simple command chmod to change the permissions of a file.

51
00:03:24,340 --> 00:03:26,680
The permissions that we want are 700.

52
00:03:26,680 --> 00:03:29,470
And then we're selecting the location of the file.

53
00:03:29,920 --> 00:03:31,060
We're going to hit enter.

54
00:03:31,060 --> 00:03:36,550
And the command runs with no issues at all meaning that the command got executed successfully.

55
00:03:36,880 --> 00:03:41,410
Next we want to connect to the Kali machine using this private key file.

56
00:03:41,410 --> 00:03:44,080
And we're going to do that using a service called SSH.

57
00:03:44,110 --> 00:03:45,520
As mentioned earlier.

58
00:03:45,520 --> 00:03:50,860
From here onwards I'll be using SSH from this computer from my Apple Mac OS.

59
00:03:50,860 --> 00:03:55,330
But the command that I'm going to use is identical on all operating systems.

60
00:03:55,330 --> 00:04:00,520
We're going to use the dash I argument to specify the location of our private key.

61
00:04:00,520 --> 00:04:04,450
So this is similar to you inputting a password to a computer.

62
00:04:04,450 --> 00:04:07,060
We're using this to authenticate with that computer.

63
00:04:07,060 --> 00:04:12,370
And we will only be allowed to connect to it if our private key matches the public key.

64
00:04:12,760 --> 00:04:14,920
So I'm going to input the location again.

65
00:04:14,920 --> 00:04:16,270
It's in my downloads.

66
00:04:16,270 --> 00:04:19,720
Kali dash keypair dot pem.

67
00:04:20,430 --> 00:04:23,160
And finally we need to give it the username.

68
00:04:23,160 --> 00:04:26,610
So we want to log in with the default username which is Carly.

69
00:04:27,090 --> 00:04:34,230
And then we need to specify the IP of the machine that we want to connect to after the at sign.

70
00:04:34,620 --> 00:04:38,040
So again we're connecting to a remote computer.

71
00:04:38,040 --> 00:04:40,260
And we're doing that from my local computer.

72
00:04:40,260 --> 00:04:46,590
So we need to tell it the IP of that computer so that we can establish that connection.

73
00:04:46,740 --> 00:04:48,900
So we gave it the username which is Carly.

74
00:04:48,900 --> 00:04:51,690
We gave it the key that is serving as the password.

75
00:04:51,690 --> 00:04:56,580
And now we need to give it the IP so we can communicate with that computer.

76
00:04:57,120 --> 00:05:00,060
Now we can get the IP in here from our control panel.

77
00:05:00,060 --> 00:05:01,830
And it's right here.

78
00:05:01,830 --> 00:05:05,460
So I'm just going to select it control C to copy it.

79
00:05:05,460 --> 00:05:07,680
And we're going to paste it in here.

80
00:05:08,330 --> 00:05:10,610
So a very very simple command.

81
00:05:10,610 --> 00:05:12,020
We're using SSH.

82
00:05:12,050 --> 00:05:15,380
That's the service that we're using to log in to our remote computer.

83
00:05:15,380 --> 00:05:17,450
From our current local computer.

84
00:05:17,450 --> 00:05:24,620
We're using the Dash I argument to specify the location of our private key that is associated with the

85
00:05:24,620 --> 00:05:26,990
target machine so that we can connect to it.

86
00:05:26,990 --> 00:05:29,300
So that's serving as our password.

87
00:05:29,600 --> 00:05:33,710
And then we're giving it the username that we want to log in with which is Carly.

88
00:05:33,710 --> 00:05:41,180
And we're giving it the IP of that computer so that this program SSH knows where to send that connection

89
00:05:41,180 --> 00:05:41,660
to.

90
00:05:42,350 --> 00:05:43,820
We're going to hit enter.

91
00:05:44,180 --> 00:05:47,270
It might ask you if you want to trust that machine.

92
00:05:47,270 --> 00:05:50,150
So we're going to have to say yes, but I've already done that.

93
00:05:50,150 --> 00:05:53,810
So as you can see, I automatically got signed in into Kali.

94
00:05:53,810 --> 00:05:56,060
And as you can see now my prompt is different.

95
00:05:56,060 --> 00:05:56,990
It's not the same.

96
00:05:56,990 --> 00:05:58,970
And I am inside Kali.

97
00:05:58,970 --> 00:06:05,000
So you can simply just do uname a just to get more information about your current machine.

98
00:06:05,000 --> 00:06:10,790
And as you can see, I am inside my Kali machine right now and I can use it to do anything that I showed

99
00:06:10,790 --> 00:06:11,930
you in my courses.

100
00:06:11,930 --> 00:06:17,540
So basically it's a fully functional Kali machine that is installed for you now on the cloud.

101
00:06:17,540 --> 00:06:24,170
And as I mentioned earlier, any services that you run on this machine will be accessible to any computer

102
00:06:24,170 --> 00:06:26,090
that is connected to the internet.

103
00:06:26,360 --> 00:06:28,880
Now, please don't worry about the command line.

104
00:06:28,880 --> 00:06:34,250
We'll spend a full lecture next to familiarize you with it and cover the basics.

105
00:06:34,250 --> 00:06:39,020
And then as we go through the course, I'll be teaching you how to use it step by step.

106
00:06:39,020 --> 00:06:44,630
So by the end of the course, you'll automatically find yourself very comfortable with using it, and

107
00:06:44,630 --> 00:06:50,000
will probably prefer using it over the graphical user interface, which I will also show you how to

108
00:06:50,000 --> 00:06:52,730
install and use on cloud computers.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:06,260
So now that we have a machine installed on the cloud and we learned how to remotely connect to it using

2
00:00:06,260 --> 00:00:07,070
SSH.

3
00:00:07,070 --> 00:00:13,430
In this lecture, I want to introduce you to the Linux command line and cover some of the basics so

4
00:00:13,430 --> 00:00:19,580
that you have a basic understanding on how to use it, the file system structure, and so on.

5
00:00:20,000 --> 00:00:24,050
Then as we go through the course we'll be using this command line often.

6
00:00:24,050 --> 00:00:29,330
So by the end of the course you're going to be pretty good at using it and pretty comfortable with it.

7
00:00:29,870 --> 00:00:36,590
Now the Linux terminal is actually very, very powerful because it can be used to do anything that you

8
00:00:36,590 --> 00:00:37,280
can think of.

9
00:00:37,280 --> 00:00:44,420
Really, a lot of the applications in Linux that have a graphical interface where command prompt programs

10
00:00:44,420 --> 00:00:48,470
first, and then people made a graphical interface for it.

11
00:00:48,470 --> 00:00:54,350
So a lot of the time, maybe the graphical interface will be buggy or crash, and the terminal program

12
00:00:54,350 --> 00:00:55,460
will still work.

13
00:00:56,150 --> 00:01:01,970
Also, a lot of the penetration testing tools do not even have a graphical interface.

14
00:01:01,970 --> 00:01:05,630
A lot of them can only be used throughout the terminal.

15
00:01:05,630 --> 00:01:10,970
So you need to know how to use this command prompt in order to achieve your goals.

16
00:01:11,900 --> 00:01:18,800
Now I'm doing this from a desktop computer, not a cloud computer, because I want to compare the results

17
00:01:18,800 --> 00:01:24,950
that I'm going to get in the command line with the graphical user interface to help you visualize the

18
00:01:24,950 --> 00:01:27,860
results that we're going to get from the commands.

19
00:01:28,190 --> 00:01:34,340
Now, the basic idea is you type a command and the result will be displayed for you on screen.

20
00:01:34,850 --> 00:01:39,680
So let's have a look on a very, very simple command which is p w d.

21
00:01:40,640 --> 00:01:46,040
Now this command prints the current working directory, hence the name pwd.

22
00:01:46,490 --> 00:01:51,020
So if I hit enter you can see it's printing forward slash route.

23
00:01:51,020 --> 00:01:54,920
Which means right now I am in the root directory.

24
00:01:54,920 --> 00:01:57,740
So basically I am in here.

25
00:01:57,740 --> 00:01:58,670
This is the root.

26
00:01:58,670 --> 00:01:59,480
It's home.

27
00:02:00,400 --> 00:02:07,600
So if I do LZ, which is a command to list all the directories and files in the current working directory,

28
00:02:07,600 --> 00:02:11,440
we should get all of these directories that we see in here.

29
00:02:12,380 --> 00:02:19,280
So if I hit enter, as you can see, I can see all these directories in the current working directory.

30
00:02:20,000 --> 00:02:23,630
Now another very useful command is the CD command.

31
00:02:23,660 --> 00:02:28,490
This command allows us to navigate into another directory.

32
00:02:28,490 --> 00:02:32,810
So for example let's say I want to navigate into the downloads.

33
00:02:33,380 --> 00:02:40,550
All we have to do is type CD followed by the name of the directory that I want to navigate to.

34
00:02:40,550 --> 00:02:42,590
So I'm going to type downloads.

35
00:02:43,960 --> 00:02:45,670
Now if I hit enter.

36
00:02:46,310 --> 00:02:48,740
I should be inside the downloads now.

37
00:02:48,740 --> 00:02:55,550
So if I do PWD to see my current working directory, you'll see that it's saying I'm in root forward

38
00:02:55,550 --> 00:02:56,930
slash downloads.

39
00:02:57,410 --> 00:03:03,320
So if I do LS here, it should show me all the directories and files inside downloads.

40
00:03:03,320 --> 00:03:08,840
So if I do enter, as you can see I have a directory and a file in here.

41
00:03:08,840 --> 00:03:13,610
And these are the exact same files that you'll see if you double click the downloads here.

42
00:03:15,520 --> 00:03:22,660
Now, if you want to go back one directory so similar to pressing the back button in here, all you

43
00:03:22,660 --> 00:03:24,070
have to do is do CD.

44
00:03:24,070 --> 00:03:28,630
Again, the command to change the working directory followed by dot dot.

45
00:03:29,440 --> 00:03:33,580
And now if I do CD, you'll see I'm back in root.

46
00:03:33,580 --> 00:03:37,960
And if I do ls you'll see all the directories and files in root.

47
00:03:38,880 --> 00:03:40,620
So that's all good.

48
00:03:40,770 --> 00:03:44,850
And there's actually a huge number of commands that you can use.

49
00:03:44,850 --> 00:03:49,170
So I'm going to include a link in the resources of this lecture.

50
00:03:49,170 --> 00:03:53,820
Of all the Linux commands that you can use, you don't need to know them by heart.

51
00:03:53,820 --> 00:03:56,520
We're actually going to be using a lot of them throughout the course.

52
00:03:56,520 --> 00:04:00,930
So you're going to naturally learn them as you go through the course.

53
00:04:01,770 --> 00:04:07,770
Now, if you are using a command and you're not sure about how this command works, you can just use

54
00:04:07,770 --> 00:04:11,940
the command command to display the manual of this command.

55
00:04:12,420 --> 00:04:17,670
For example, we've used the LHS command here to list the files and directories in the current working

56
00:04:17,670 --> 00:04:18,510
directory.

57
00:04:18,510 --> 00:04:26,520
But if I do man followed by LHS, this basically means I'm requesting the manual of LHS.

58
00:04:26,520 --> 00:04:29,370
So I'm asking how can I use the LHS command.

59
00:04:29,940 --> 00:04:35,430
So if I hit enter you'll see I'll get a screen similar to a text file.

60
00:04:35,430 --> 00:04:41,100
And basically it's giving me a lot of information on how to use the LHS command.

61
00:04:41,610 --> 00:04:46,500
So you can see that it's telling us that this command will list the directory contents.

62
00:04:46,950 --> 00:04:51,870
You can see the way it works by typing LHS, followed by the options followed by a file.

63
00:04:51,870 --> 00:04:59,220
If you if you want to run it on a file, you can see a longer description of the command.

64
00:05:00,070 --> 00:05:06,790
And then you can see all the options and the arguments that we can use with this command.

65
00:05:07,640 --> 00:05:09,170
Now in Linux.

66
00:05:09,170 --> 00:05:16,490
Most of the time the options will always follow the same syntax, so you either use dash letter or dash

67
00:05:16,490 --> 00:05:19,820
dash award to specify the argument.

68
00:05:19,850 --> 00:05:27,080
For example, in here the dash a and dash dash all will ignore entries starting with dot.

69
00:05:27,970 --> 00:05:34,540
So if you keep going down in here, you'll see all the options and arguments you can use with the RLS

70
00:05:34,540 --> 00:05:35,380
command.

71
00:05:36,010 --> 00:05:43,990
And we have another example here we have the dash L which means it's going to use a long listing format

72
00:05:43,990 --> 00:05:48,940
which will display more information about the files in the current working directory.

73
00:05:49,630 --> 00:05:51,070
So let's have a look on that.

74
00:05:51,070 --> 00:05:53,350
I'm going to press Q to exit this.

75
00:05:53,530 --> 00:05:56,230
And then we're going to do RLS as usual.

76
00:05:56,230 --> 00:06:02,920
And since we read the manual we know we can do dash L to see more information about the files.

77
00:06:02,920 --> 00:06:08,920
And if I hit enter now you can see I'm still getting the same directories, but it's also showing me

78
00:06:08,920 --> 00:06:13,150
the permissions, the users, the date created and so on.

79
00:06:13,900 --> 00:06:19,210
So you can use the man command on any command you want, not only on the RLS.

80
00:06:19,210 --> 00:06:21,520
So you can use it on the PWD.

81
00:06:21,550 --> 00:06:28,510
You can use it on the CD or any other command, and it will show you full description or the manual

82
00:06:28,510 --> 00:06:31,420
page of how to use this command.

83
00:06:32,840 --> 00:06:36,530
Now I'm going to clear the screen by typing clear.

84
00:06:37,870 --> 00:06:40,570
And the next thing that I want to show you is the dash.

85
00:06:40,570 --> 00:06:41,470
Dash help.

86
00:06:41,470 --> 00:06:47,830
So this is something that you can use again in almost all commands, in all programs in Linux.

87
00:06:47,830 --> 00:06:54,010
So you can just type the program name or the command name followed by dash dash help.

88
00:06:55,290 --> 00:07:01,350
As you might think, this will show you a health message telling you what this command is or what this

89
00:07:01,350 --> 00:07:08,190
program is, the arguments that it takes, how to use these arguments and examples at the bottom.

90
00:07:09,020 --> 00:07:11,300
Now another useful thing with the terminal.

91
00:07:11,300 --> 00:07:14,030
So I'm going to clear this again is the arrows.

92
00:07:14,030 --> 00:07:19,280
So you can press up to go up to see all the commands that we executed before.

93
00:07:19,280 --> 00:07:24,980
And again you can go down to navigate between the commands that you executed previously.

94
00:07:25,700 --> 00:07:29,360
You can also use the tab for autocomplete.

95
00:07:29,360 --> 00:07:32,750
So again let's do LZ and you can see all the files.

96
00:07:32,750 --> 00:07:35,600
And let's say we want to go into documents.

97
00:07:36,110 --> 00:07:39,380
So we can do CD followed by documents.

98
00:07:39,380 --> 00:07:41,210
You can type documents.

99
00:07:41,210 --> 00:07:46,820
Or if you're lazy like me you can just do doc and press tab.

100
00:07:46,820 --> 00:07:52,010
And as you can see it's automatically completing the rest of the word for me.

101
00:07:52,710 --> 00:07:58,260
So this is something that comes very, very handy when you're using the terminal for a long time.

102
00:07:59,270 --> 00:08:05,120
Now, before I let you go, I just want to show you two websites that I'm going to include in the resources

103
00:08:05,120 --> 00:08:06,230
of this lecture.

104
00:08:06,410 --> 00:08:12,410
First of all, we have a website here that includes the most common Linux commands, if not all.

105
00:08:12,410 --> 00:08:15,800
So you can go through them and familiarize yourself with them.

106
00:08:15,800 --> 00:08:19,160
But keep in mind, you don't need to know them all by heart.

107
00:08:19,160 --> 00:08:25,220
Like I said, as you go through my course and as you continue on with your journey, you will learn

108
00:08:25,220 --> 00:08:27,650
the commands that you need as you go.

109
00:08:28,750 --> 00:08:34,240
Another really useful resource that I'm going to include is Explain Shell Comm.

110
00:08:34,240 --> 00:08:38,050
This website is designed to explain Linux commands to you.

111
00:08:38,050 --> 00:08:40,600
So all you have to do is type the commands in here.

112
00:08:40,600 --> 00:08:50,110
So for example, if you just type ls and hit explain, it'll explain that LS will list directory content.

113
00:08:50,110 --> 00:08:53,830
You could make it more complex and do ls la.

114
00:08:53,890 --> 00:08:59,860
And if we hit enter now, it'll break all the arguments and explain every single argument.

115
00:08:59,860 --> 00:09:02,230
So again LZ this contents.

116
00:09:02,230 --> 00:09:03,700
If we highlight the L.

117
00:09:03,700 --> 00:09:09,460
As you can see, it's telling us that it's going to use a long listing format as we seen earlier.

118
00:09:09,460 --> 00:09:16,600
And the A at the end is the same as Dash A, which is all, which means that we do not want to ignore

119
00:09:16,600 --> 00:09:18,340
entries starting with a dot.

120
00:09:18,340 --> 00:09:20,860
So we do not want to ignore hidden files.

121
00:09:21,280 --> 00:09:25,810
So if you ever see a Linux command that you don't understand, you can always just come in here, put

122
00:09:25,810 --> 00:09:30,520
the command and it will break it down to you and explain it really nicely.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Phishing

1
00:00:00,080 --> 00:00:05,360
Now that we understand the basics of the cloud and how to create servers and control them and communicate

2
00:00:05,360 --> 00:00:09,620
with them, it's time to go ahead and start hacking and start having some fun.

3
00:00:09,620 --> 00:00:12,590
So in this section we're going to be focusing on phishing.

4
00:00:12,590 --> 00:00:18,650
And I'm going to show you how to replicate any website that exists on the internet and host it on your

5
00:00:18,650 --> 00:00:20,180
own server on the cloud.

6
00:00:20,420 --> 00:00:23,300
Now this can be very useful in so many scenarios.

7
00:00:23,690 --> 00:00:27,950
So first of all, you're going to be able to host your own websites on your own servers.

8
00:00:27,950 --> 00:00:33,410
Then I'm going to teach you how to use this knowledge to steal the login information of any web page

9
00:00:33,410 --> 00:00:35,900
and hack the web browsers that load that page.

10
00:00:35,900 --> 00:00:38,960
Then we'll take our phishing game to the next level.

11
00:00:38,960 --> 00:00:43,550
And I'm going to teach you how to bypass multi-factor or two factor authentication.

12
00:00:43,550 --> 00:00:47,060
Using evil links and the browser in-browser attack.

13
00:00:47,060 --> 00:00:53,780
You'll even be able to use this to hack into WhatsApp accounts or any other account that has a web interface.

14
00:00:53,780 --> 00:00:59,120
And of course, this is going to work against all devices mobile phones, computers, tablets.

15
00:00:59,120 --> 00:01:00,080
It doesn't really matter.

16
00:01:00,080 --> 00:01:07,760
And against all operating systems windows, Linux, Apple macOS, iOS or even Android as we do this,

17
00:01:07,760 --> 00:01:10,250
I'm going to teach you more concepts about the cloud.

18
00:01:10,250 --> 00:01:15,410
So I'm going to teach you how to transfer files between your local computer and your cloud server.

19
00:01:15,410 --> 00:01:19,970
And I'm going to teach you how to manage the file system on your cloud server.

20
00:01:19,970 --> 00:01:25,580
So you'll be able to download and upload and edit and rename and move files exactly the same way that

21
00:01:25,580 --> 00:01:29,390
you communicate or interact with files on your local computer.

22
00:01:29,390 --> 00:01:35,870
You'll also learn what do we mean by DNS and how to register a domain name, such as the security comm,

23
00:01:35,870 --> 00:01:41,780
and link that domain name to your cloud server so that when people enter it in their browser, it will

24
00:01:41,780 --> 00:01:48,110
lead to your website that is hosted on your cloud server, which could be a phishing page, or it could

25
00:01:48,110 --> 00:01:53,840
be a page with an evil code or a replica of any other page, which will allow you to further exploit

26
00:01:53,840 --> 00:01:57,350
the target or steal sensitive information from their computer.

27
00:01:57,350 --> 00:02:03,200
Finally, I will teach you how to enable Https on your website, whether they are phishing websites

28
00:02:03,200 --> 00:02:04,550
or normal websites.

29
00:02:04,550 --> 00:02:08,390
As a result, you're going to see https before the URL.

30
00:02:08,390 --> 00:02:13,070
You will see the lock icon and secure beside the URL of the website.

31
00:02:13,070 --> 00:02:19,070
This increases the user trust, the browser trust and search engine trust, increasing the chances of

32
00:02:19,070 --> 00:02:21,590
you executing a successful attack.

33
00:02:21,590 --> 00:02:25,580
Last but not least, I'm going to teach you some basic PHP programming.

34
00:02:25,580 --> 00:02:26,960
But don't worry about it.

35
00:02:26,960 --> 00:02:31,670
I don't expect you to know any programming and I'm going to take you through it step by step.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:06,200
Okay, so now that we have a Kali machine installed on Amazon's servers, let's go ahead and start doing

2
00:00:06,200 --> 00:00:07,370
some useful stuff.

3
00:00:07,370 --> 00:00:12,710
So as mentioned previously, you can use any program that comes pre-installed in Kali, or you can install

4
00:00:12,710 --> 00:00:13,670
whatever you want.

5
00:00:13,670 --> 00:00:19,550
But first I want to introduce you to the web server that is pre-installed in Kali, which is called

6
00:00:19,550 --> 00:00:20,240
Apache.

7
00:00:20,270 --> 00:00:26,090
Now the web server is pretty useful in so many scenarios because you can use it to first of all, host

8
00:00:26,090 --> 00:00:32,150
your own websites, whether they're fake websites to lure people to put their login information or if

9
00:00:32,150 --> 00:00:34,460
they're malicious websites that contain beef code.

10
00:00:34,460 --> 00:00:35,930
And we'll talk about that later.

11
00:00:35,930 --> 00:00:38,750
Or you can even use it to deliver malware.

12
00:00:38,750 --> 00:00:41,960
The cool thing about this is because this is hosted on the cloud.

13
00:00:41,960 --> 00:00:45,170
As mentioned, you won't need to enable port forwarding or anything.

14
00:00:45,170 --> 00:00:50,450
Whatever malware you host on it will be accessible to anybody connected to the internet.

15
00:00:50,930 --> 00:00:58,880
So assuming this is my Kali installation on the cloud and it has Apache running on it, and by default

16
00:00:58,880 --> 00:01:00,500
Apache runs on port 80.

17
00:01:00,500 --> 00:01:07,550
So you can think of this as a socket that is listening for incoming connections from the internet on

18
00:01:07,550 --> 00:01:08,330
port 80.

19
00:01:08,630 --> 00:01:14,570
Now, assuming we have a user that is connected to the internet and they open up their web browser and

20
00:01:14,570 --> 00:01:22,070
input the IP in their URL bar, this request will go to the internet and eventually end up at the IP

21
00:01:22,070 --> 00:01:23,330
that they're requesting.

22
00:01:23,330 --> 00:01:31,460
And because they put Http colon forward slash, forward slash, and because they did not specify a port,

23
00:01:31,460 --> 00:01:36,770
this request will be connected to port 80 by default.

24
00:01:37,340 --> 00:01:43,100
Now like I said, on port 80 we have Apache running on our computer.

25
00:01:43,100 --> 00:01:51,650
And Apache by default is configured to load a certain path on the file system whenever it gets a request

26
00:01:51,650 --> 00:01:55,880
on port 80, that path is known as the web route.

27
00:01:55,880 --> 00:02:02,540
And in our Kali installation that is set to var ww HTML.

28
00:02:02,540 --> 00:02:10,580
So whenever a user puts the IP of the Kali machine in their URL bar and precede it with Http and not

29
00:02:10,580 --> 00:02:17,660
specify a port, that request is going to go over port 80 to Apache, and Apache by default, is going

30
00:02:17,660 --> 00:02:25,310
to load whatever files and directories that exist within its web route path, and the web route path

31
00:02:25,310 --> 00:02:28,910
is set to var ww HTML.

32
00:02:29,480 --> 00:02:36,350
Now also to take this one step further, if the user does not specify a file that they want to load

33
00:02:36,350 --> 00:02:43,460
after the IP address, Apache is going to load a file that is called index.html.

34
00:02:44,000 --> 00:02:50,300
Now, as mentioned, Apache two should be pre-installed in Kali, but just to make sure that it's actually

35
00:02:50,300 --> 00:02:53,060
installed, we're going to run the installation command.

36
00:02:53,060 --> 00:02:58,790
I'm doing this because the creators of Kali changed the pre-installed packages all the time.

37
00:02:58,790 --> 00:03:03,620
So it's a good idea for me to teach you how to install packages through the terminal.

38
00:03:03,620 --> 00:03:09,590
Now in Kali, because it's Debian based, we installed packages using a program called APT.

39
00:03:09,950 --> 00:03:15,890
And before we go ahead and install anything, we're going to do update to update the sources that we

40
00:03:15,890 --> 00:03:17,810
can download packages from.

41
00:03:17,810 --> 00:03:20,570
And we want to run this command as admin.

42
00:03:20,570 --> 00:03:25,730
And that's why we're going to do sudo so that we can run the command as root.

43
00:03:25,730 --> 00:03:30,530
You can think of the root account as the administrator account on the system.

44
00:03:30,530 --> 00:03:36,710
And when we put sudo before the command that we want to run, we're telling the system that we want

45
00:03:36,710 --> 00:03:38,930
to run this command as admin.

46
00:03:39,470 --> 00:03:40,880
So I'm going to hit enter.

47
00:03:41,270 --> 00:03:45,440
And as you can see it's updating the sources where we can download packages from.

48
00:03:45,440 --> 00:03:47,240
So we're going to give it a minute.

49
00:03:47,660 --> 00:03:50,360
And once this is done I'm going to clear the screen.

50
00:03:50,360 --> 00:03:58,160
And then I'm going to use the same command apt to install a package that is called Apache two.

51
00:03:58,190 --> 00:04:04,790
I'm also going to install another package called PHP to install the PHP programming language on Apache,

52
00:04:04,790 --> 00:04:09,110
which will allow me to run PHP code on my Apache server.

53
00:04:09,110 --> 00:04:13,520
We're not going to need this in this lecture, but we will need it in future lectures.

54
00:04:13,520 --> 00:04:17,180
And like the previous command, we want to run this command as root.

55
00:04:17,180 --> 00:04:20,270
So I'm going to put the cursor at the start of the command.

56
00:04:20,270 --> 00:04:24,230
And I'm going to type sudo to run it as administrator.

57
00:04:24,230 --> 00:04:25,730
So it's a very simple command.

58
00:04:25,730 --> 00:04:29,930
We're using APT which is a package manager to install two packages.

59
00:04:29,930 --> 00:04:34,040
The first one is Apache two, which is the web server that I just spoke about.

60
00:04:34,040 --> 00:04:41,450
And PHP is simply the PHP programming language, so that we can run PHP on our Apache server, and you'll

61
00:04:41,450 --> 00:04:43,970
see why we're going to need that in the future.

62
00:04:44,540 --> 00:04:46,070
So I'm going to hit enter.

63
00:04:46,400 --> 00:04:51,890
And as you can see, it turns out that Apache and PHP both were not installed for me.

64
00:04:51,890 --> 00:04:56,900
So it's given me that the packages that will be installed in here, and it's telling me the amount of

65
00:04:56,900 --> 00:04:59,840
space it's going to take and it's asking me if I want to.

66
00:04:59,970 --> 00:05:01,170
Continue or not.

67
00:05:01,590 --> 00:05:06,270
If I just hit enter, it will mean that I'm going to choose the default option, which is yes, which

68
00:05:06,270 --> 00:05:07,230
is to install.

69
00:05:07,230 --> 00:05:09,900
So I'm going to hit return or enter from my keyboard.

70
00:05:09,900 --> 00:05:13,080
Give it some time and this should install it for you.

71
00:05:13,080 --> 00:05:17,940
If the packages were already installed, it actually would have said that everything is already installed

72
00:05:17,940 --> 00:05:19,590
and that there is nothing to do.

73
00:05:19,770 --> 00:05:24,750
So now that we have everything installed, I'm going to clear the screen again and I'm going to start

74
00:05:24,750 --> 00:05:28,140
the Apache web server by running a command as root.

75
00:05:28,140 --> 00:05:30,060
So we're going to do sudo again.

76
00:05:30,540 --> 00:05:34,140
And this time we want to run a service.

77
00:05:34,920 --> 00:05:39,720
That is called Apache two and we want to start this service.

78
00:05:39,870 --> 00:05:44,430
So we're using the sudo command to run a service that is called Apache two.

79
00:05:44,430 --> 00:05:47,610
And we're saying that we want to start this service.

80
00:05:48,180 --> 00:05:49,500
I'm going to hit enter.

81
00:05:50,190 --> 00:05:56,070
And if you don't see any error messages on the screen that means that the command got executed successfully,

82
00:05:56,070 --> 00:05:59,580
meaning that the Apache web server should be running at the moment.

83
00:06:00,240 --> 00:06:05,880
Now that the web server is running, all we have to do is simply copy the IP of the machine and we can

84
00:06:05,880 --> 00:06:08,400
get the IP from here from the control panel.

85
00:06:08,950 --> 00:06:11,530
And then we can load it into a web browser.

86
00:06:11,530 --> 00:06:15,160
So I have a windows machine in here and I'm going to hit enter to load it.

87
00:06:15,160 --> 00:06:21,370
And if everything is set correctly I should see the default page of Apache or the default website hosted

88
00:06:21,370 --> 00:06:22,330
by Apache.

89
00:06:22,330 --> 00:06:24,490
But as you can see, nothing is loading.

90
00:06:24,490 --> 00:06:32,050
And the reason for this is because there are security rules in here preventing Apache from responding

91
00:06:32,080 --> 00:06:35,650
to the requests that the windows machine is sending in here.

92
00:06:35,650 --> 00:06:42,010
So we're going to have to simply just click on the machine that we want to modify its security rules,

93
00:06:42,010 --> 00:06:43,720
which is the Kali machine in here.

94
00:06:43,720 --> 00:06:46,000
So we're going to click on the instance ID.

95
00:06:46,600 --> 00:06:50,470
We're going to scroll down and click on security in here.

96
00:06:51,010 --> 00:06:55,840
And as you can see in here we have inbound and outbound rules.

97
00:06:56,320 --> 00:07:01,900
In the inbound rule we already have a rule to allow connections to port 22.

98
00:07:01,930 --> 00:07:04,540
This is the port that is used by SSH.

99
00:07:04,540 --> 00:07:09,370
And that's why we're actually able to connect to the machine using SSH.

100
00:07:09,370 --> 00:07:11,530
Now Apache runs on port 80.

101
00:07:11,560 --> 00:07:16,330
Therefore we're going to have to add another rule to allow connections to port 80.

102
00:07:16,510 --> 00:07:19,600
To do that we're going to click on the security groups.

103
00:07:19,600 --> 00:07:21,010
We're going to scroll down.

104
00:07:21,010 --> 00:07:26,590
We're going to click on Edit Inbound Rules because we want to edit the inbound not the outbound rules.

105
00:07:26,590 --> 00:07:30,940
And as you can see, we already have the rule for the port 22 for SSH.

106
00:07:30,940 --> 00:07:34,270
And we're going to add a new one by clicking on add a rule.

107
00:07:34,270 --> 00:07:37,120
And this is going to be a Http rule.

108
00:07:37,120 --> 00:07:39,130
So for a Http server.

109
00:07:39,130 --> 00:07:41,620
So it will automatically set the port to 80.

110
00:07:41,620 --> 00:07:44,560
But you can leave this to custom and select whatever port.

111
00:07:44,560 --> 00:07:48,310
If you were using another port we're going to leave the source to custom.

112
00:07:48,310 --> 00:07:53,470
And we're going to put the IP to the first option, which is 0000.

113
00:07:54,040 --> 00:07:59,410
So that automatically selects the IP of the instance of the Kali machine.

114
00:07:59,800 --> 00:08:01,780
We're going to click on save rules.

115
00:08:02,230 --> 00:08:07,210
As you can see, we get a green message telling us that the rules were saved successfully.

116
00:08:07,210 --> 00:08:12,190
So now if we just go to any computer that is connected to the internet.

117
00:08:12,190 --> 00:08:17,680
So if you do this at the time of me recording this lecture, if you put that IP and hit enter, the

118
00:08:17,680 --> 00:08:22,000
default website for Apache should load to you, as you can see in here.

119
00:08:22,000 --> 00:08:28,930
So right now I expose the Apache home directory to the internet so I can put any website that I want

120
00:08:28,930 --> 00:08:34,870
in here, whether it's a fake Instagram or Facebook page, for example, to steal login credentials

121
00:08:34,870 --> 00:08:41,440
or whether it's a clone of another website with evil code embedded in it, or I can even have my backdoors

122
00:08:41,440 --> 00:08:44,860
hosted in here, or malware and then deliver it to the target.

123
00:08:44,860 --> 00:08:48,400
So the ideas and the uses of this is endless.

124
00:08:48,400 --> 00:08:54,130
And like I said, the cool thing about this is it's always running and it's always available to anybody

125
00:08:54,130 --> 00:08:56,050
that is connected to the internet.

126
00:08:56,910 --> 00:09:02,340
So the page that we see right here is stored on our web server.

127
00:09:02,340 --> 00:09:06,690
And a path that is called var ww HTML.

128
00:09:06,690 --> 00:09:13,080
And the name of the file that contains this page code is index.html.

129
00:09:13,380 --> 00:09:19,350
Now similarly, in the future when we want to deliver backdoors, we can store a backdoor in the same

130
00:09:19,350 --> 00:09:28,410
location in the web root in var HTML, just like so, and call it backdoor dot txt and then the user

131
00:09:28,410 --> 00:09:33,210
can simply download it by typing the file name after the IP.

132
00:09:33,720 --> 00:09:37,200
So if the user sends this request, no port is specified.

133
00:09:37,200 --> 00:09:38,190
It's going to go to here.

134
00:09:38,190 --> 00:09:41,520
It's going to go to port 80 by default to Apache.

135
00:09:41,550 --> 00:09:44,010
Apache is going to load the web root which is here.

136
00:09:44,010 --> 00:09:47,910
And it's going to look if there is a file called backdoor dot x.

137
00:09:48,120 --> 00:09:50,610
If there is it's going to serve them this file.

138
00:09:50,610 --> 00:09:54,510
If there isn't it will serve them the known 404 page.

139
00:09:54,510 --> 00:09:55,710
The not found page.

140
00:09:56,850 --> 00:10:04,830
Now, as I mentioned, the var ww HTML is just a path or a directory within the file system of this

141
00:10:04,830 --> 00:10:08,850
computer, so you can have another directory within this directory.

142
00:10:08,850 --> 00:10:11,490
For example this directory right here called files.

143
00:10:11,490 --> 00:10:15,870
And within it you can have even more directories or even more files.

144
00:10:15,870 --> 00:10:21,330
And the way to access this files directory you simply have to type its name in here.

145
00:10:21,330 --> 00:10:26,970
And then if you want to access another file within this directory, you put another forward slash and

146
00:10:26,970 --> 00:10:28,020
then you put the file name.

147
00:10:28,020 --> 00:10:30,090
So in this case it's one dot jpg.

148
00:10:30,090 --> 00:10:31,230
And there you go.

149
00:10:31,230 --> 00:10:33,420
You will get the one dot jpg file.

150
00:10:33,630 --> 00:10:38,340
So the request is going to be sent to the IP that we have in here.

151
00:10:38,340 --> 00:10:41,610
No port is specified in here therefore goes to 80.

152
00:10:41,610 --> 00:10:43,590
By default it goes to Apache.

153
00:10:43,620 --> 00:10:44,940
Apache is going to check.

154
00:10:44,940 --> 00:10:49,110
Is there a specific path that is being requested from my web route.

155
00:10:49,110 --> 00:10:50,400
And yes there is.

156
00:10:50,400 --> 00:10:52,650
We're looking for a directory called files.

157
00:10:52,650 --> 00:10:53,700
And we do have it.

158
00:10:53,700 --> 00:10:58,590
So we go in and we also are looking for a file that is called one dot jpg.

159
00:10:58,590 --> 00:10:59,910
And then we look for it.

160
00:10:59,910 --> 00:11:02,040
And if we do have it we're going to serve it.

161
00:11:02,040 --> 00:11:05,820
If we don't we're going to serve the 404 error message.

162
00:11:06,750 --> 00:11:12,390
Understanding this is very important for what we are going to do in the future, because once we're

163
00:11:12,390 --> 00:11:16,920
done with the introduction and the basics that we're covering in this section, we're going to start

164
00:11:16,920 --> 00:11:22,890
diving deeper into this, and I'm going to show you how to start hosting files like a pro and creating

165
00:11:22,890 --> 00:11:29,910
your own phishing pages that look identical to other popular pages, but contain malware, or even create

166
00:11:29,910 --> 00:11:35,430
your own phishing login pages that look identical to real websites like Facebook and Instagram, but

167
00:11:35,430 --> 00:11:40,350
at the same time store the data that the user enters for you so you can see it.

168
00:11:40,350 --> 00:11:45,930
All of this will require a little bit more understanding of how the web server and how the file structure

169
00:11:45,930 --> 00:11:51,000
works in here, because we're going to have to be playing with this and modifying it to achieve our

170
00:11:51,000 --> 00:11:51,570
goals.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,350 --> 00:00:05,300
Now this is all great, but we just did it in order to test that our configuration is right.

2
00:00:05,300 --> 00:00:08,240
But in a real life scenario, this is not good.

3
00:00:08,240 --> 00:00:12,410
You can't just send a page that looks like this and expect the target to run it.

4
00:00:12,410 --> 00:00:16,850
And even if they do click it, once they click it, they know that there is something wrong with this.

5
00:00:16,910 --> 00:00:22,760
So in a real life scenario, you want a social engineer them to opening a page that might be interesting

6
00:00:22,790 --> 00:00:23,240
to them.

7
00:00:23,240 --> 00:00:26,120
So it could be a page that contains useful articles.

8
00:00:26,120 --> 00:00:30,260
It could be a page of a website that they're interested in.

9
00:00:30,260 --> 00:00:35,630
Depending on whatever the target is interested in, you need to send them something that they are likely

10
00:00:35,630 --> 00:00:39,500
to click and not get suspicious when they load that page.

11
00:00:39,680 --> 00:00:44,660
So first, I'm going to teach you how to clone any page on the internet, whether it's a login page

12
00:00:44,660 --> 00:00:46,250
or a normal website.

13
00:00:46,250 --> 00:00:51,740
Then I'm going to teach you how to modify it to store the login information that the people will enter

14
00:00:51,740 --> 00:00:55,070
so that we can access it and steal usernames and passwords.

15
00:00:55,070 --> 00:01:01,220
And finally, in the next section, I'm going to show you how to embed evil code in these phishing pages

16
00:01:01,220 --> 00:01:03,380
and hack the browsers that load them.

17
00:01:03,770 --> 00:01:09,320
So first of all, I'm going to open Firefox and we're going to go to the page that we think that the

18
00:01:09,320 --> 00:01:11,030
target would be interested in.

19
00:01:11,030 --> 00:01:14,600
And for this example let's go to facebook.com.

20
00:01:15,950 --> 00:01:20,150
And all you have to do is right click save pages.

21
00:01:21,190 --> 00:01:25,540
And make sure that you select all files and save it.

22
00:01:26,390 --> 00:01:32,300
Now, if we go to my finder, which I have it right here, I'm going to go to the directory where I

23
00:01:32,300 --> 00:01:32,930
downloaded it.

24
00:01:32,930 --> 00:01:36,770
So I downloaded it to a directory in my downloads and it's called test.

25
00:01:36,770 --> 00:01:38,870
And we have the page right here.

26
00:01:39,020 --> 00:01:41,360
Now if we double click this page.

27
00:01:42,360 --> 00:01:46,080
You'll see that it is a replica of facebook.com.

28
00:01:46,260 --> 00:01:47,520
So that's very simple.

29
00:01:47,520 --> 00:01:49,770
You really don't need to use any tools for this.

30
00:01:49,770 --> 00:01:55,290
There are so many tools online that will download and create a clone or a replica for you for a website,

31
00:01:55,290 --> 00:01:56,940
but there really is no need for that.

32
00:01:56,940 --> 00:01:58,590
You can create that yourself.

33
00:01:58,740 --> 00:02:03,600
Now once we have this page, we actually need to host it on the cloud because as you can see, this

34
00:02:03,600 --> 00:02:07,500
is loaded locally on my computer and is only accessible on my computer.

35
00:02:07,500 --> 00:02:12,750
So we need to upload it to our cloud server that we created previously.

36
00:02:13,020 --> 00:02:21,090
You can actually look at the page code and copy paste it into a new file in your web root in var HTML.

37
00:02:21,090 --> 00:02:26,610
But I want to show you a better way of doing this that we will actually need in future lectures.

38
00:02:26,610 --> 00:02:31,680
When we start uploading bigger websites and actually start playing with these phishing pages.

39
00:02:31,950 --> 00:02:38,190
So what we're going to need is a program called FileZilla, and this is a client that will allow us

40
00:02:38,190 --> 00:02:46,470
to connect to our cloud server over SSH, but be able to browse its file system, upload and download

41
00:02:46,470 --> 00:02:49,290
files, and edit them using a graphical interface.

42
00:02:49,290 --> 00:02:55,470
So it will be very easy to use instead of having to do everything from the terminal from here.

43
00:02:56,010 --> 00:03:00,780
So there is versions for all operating systems for FileZilla.

44
00:03:00,780 --> 00:03:04,740
I'm going to include this download link in the resources of this lecture.

45
00:03:04,740 --> 00:03:08,760
I already have it downloaded, so I'm not going to cover how to download the file and install it.

46
00:03:08,760 --> 00:03:09,930
It's very, very simple.

47
00:03:09,930 --> 00:03:13,470
So simply I'm actually just gonna run it in here.

48
00:03:13,470 --> 00:03:19,260
So what we need to do right now is use this program to connect to our cloud server.

49
00:03:19,320 --> 00:03:22,440
So you can use the Quick Connect in here to do it.

50
00:03:22,440 --> 00:03:29,430
Or you can actually store the login information so you can connect to your server quickly.

51
00:03:29,430 --> 00:03:31,470
So we're going to go to the file.

52
00:03:31,470 --> 00:03:33,510
We're going to click on the site manager.

53
00:03:34,140 --> 00:03:38,940
And as you can see I already have the websites that I usually connect to using this program.

54
00:03:38,940 --> 00:03:42,210
And we want to create a new website or a new site.

55
00:03:42,210 --> 00:03:48,330
And we're going to call it AWS Kali because this is a Kali machine using AWS servers.

56
00:03:48,330 --> 00:03:54,180
I always like to use meaningful names when I'm creating stuff like this, so it's easy for me to find

57
00:03:54,180 --> 00:03:55,320
them and use them.

58
00:03:55,320 --> 00:04:01,020
Now on the right in here, you need to set the configuration in order to be able to connect to this

59
00:04:01,020 --> 00:04:01,920
cloud server.

60
00:04:01,920 --> 00:04:05,880
So we're going to need to set the protocol to SftP.

61
00:04:05,880 --> 00:04:09,210
So it's basically ftp FTP over SSH.

62
00:04:09,690 --> 00:04:13,500
You need to set the host to the IP of your server.

63
00:04:13,500 --> 00:04:18,210
So we can just get it from our management page in here.

64
00:04:18,330 --> 00:04:19,920
And I have it right here.

65
00:04:19,920 --> 00:04:23,220
So we're just going to copy it and paste it here.

66
00:04:24,070 --> 00:04:29,560
And in the log on we're going to change the ask for password to a key file.

67
00:04:29,560 --> 00:04:34,150
Because remember when we were logging in with the terminal we specified the IP.

68
00:04:34,180 --> 00:04:35,920
We specified the username.

69
00:04:35,920 --> 00:04:39,190
And then we specified the key file.

70
00:04:39,190 --> 00:04:41,800
So we never needed to actually input a password.

71
00:04:41,800 --> 00:04:47,980
And I mentioned in that video when I showed you how to use this is that this key file is used to authenticate

72
00:04:47,980 --> 00:04:49,180
us with the server.

73
00:04:49,180 --> 00:04:51,550
It's more secure than using a password.

74
00:04:51,550 --> 00:04:53,770
So you have to make sure you store it somewhere safe.

75
00:04:53,770 --> 00:04:57,310
And you'll always be able to use it to authenticate with that server.

76
00:04:57,310 --> 00:05:04,870
So I've already put the IP, and all we have to do right now is point FileZilla to the location of this

77
00:05:04,870 --> 00:05:05,410
key file.

78
00:05:05,410 --> 00:05:08,260
So it's in my downloads and it's called Kali key pair.

79
00:05:08,770 --> 00:05:13,540
So we're going to go back to FileZilla and we're going to select the key file.

80
00:05:13,540 --> 00:05:19,330
And I'm already in my downloads and I'm looking for Kali key pair.

81
00:05:19,330 --> 00:05:21,040
And we have it right here.

82
00:05:21,760 --> 00:05:24,160
And I'm going to set the user to Carly.

83
00:05:24,850 --> 00:05:27,580
Again, similar to the command that we have in here.

84
00:05:27,580 --> 00:05:29,500
So we specify the user to Carly.

85
00:05:30,100 --> 00:05:34,180
So basically what's this program is going to do what FileZilla is going to do.

86
00:05:34,180 --> 00:05:40,120
It's going to pretty much use the same commands that we were using when we're connecting over SSH,

87
00:05:40,120 --> 00:05:42,700
but using a graphical interface.

88
00:05:42,700 --> 00:05:48,130
So whenever we click on things and execute things, it's actually going to be running these commands

89
00:05:48,130 --> 00:05:48,520
in here.

90
00:05:48,520 --> 00:05:51,790
And you'll see the the command that it's executing and the result.

91
00:05:51,790 --> 00:05:58,090
But the nice thing is it has a nice graphical user interface that will make it much easier for us to

92
00:05:58,090 --> 00:06:01,990
navigate the file system, upload and download files, and edit them.

93
00:06:02,350 --> 00:06:05,530
So anyway, we filled all of the needed fields in here.

94
00:06:05,530 --> 00:06:09,520
We set the IP, we set the username and we set the key file.

95
00:06:09,520 --> 00:06:11,410
So we're going to click on connect.

96
00:06:13,570 --> 00:06:14,230
And perfect.

97
00:06:14,230 --> 00:06:21,430
As you can see now, I connected to my Kali instance on the cloud and you can actually see in here the

98
00:06:21,430 --> 00:06:22,960
commands that it's trying to do.

99
00:06:22,960 --> 00:06:26,350
So it's even telling you it was listing trying to list this directory.

100
00:06:26,350 --> 00:06:28,030
The listing is successful.

101
00:06:28,030 --> 00:06:33,340
And then it managed to list all of the files and directories in the path that is home.

102
00:06:33,340 --> 00:06:33,790
Kali.

103
00:06:34,600 --> 00:06:40,720
So if we just take a quick look on the interface in here, you have a tree of the file system in here

104
00:06:40,720 --> 00:06:42,250
that you can use to navigate.

105
00:06:42,250 --> 00:06:46,030
You can also navigate the file system in here of the cloud server.

106
00:06:46,030 --> 00:06:51,670
And in here on the left you have access to your local file system.

107
00:06:51,670 --> 00:06:55,840
So right here this is my local username on my current machine.

108
00:06:55,840 --> 00:07:00,490
And these are the local files that are stored in downloads test.

109
00:07:00,850 --> 00:07:07,540
Now these files actually don't exist in test right now because I deleted them and we downloaded the

110
00:07:07,540 --> 00:07:09,040
Facebook page.

111
00:07:09,040 --> 00:07:13,210
So I just need to right click and refresh to get an updated version of it.

112
00:07:13,210 --> 00:07:13,900
As you can see.

113
00:07:13,900 --> 00:07:15,220
And we have it right now.

114
00:07:15,550 --> 00:07:18,670
So basically this is your Kali installation on the cloud.

115
00:07:18,670 --> 00:07:25,120
And you can use it remotely using this graphical user interface and easily as if you have local access

116
00:07:25,120 --> 00:07:25,570
to it.

117
00:07:25,570 --> 00:07:32,140
So right click in a file will allow you to download it, add it to a queue view or edit the file.

118
00:07:32,140 --> 00:07:36,460
And if you're trying to edit it and will see it, it's going to open it in a text editor.

119
00:07:36,460 --> 00:07:39,460
You could create directories within this current directory.

120
00:07:39,460 --> 00:07:42,700
You could create new files obviously refresh.

121
00:07:42,700 --> 00:07:47,290
You can delete, rename, copy or change the file permissions as well.

122
00:07:47,290 --> 00:07:50,980
You can simply drag and drop files in here to upload them.

123
00:07:50,980 --> 00:07:53,980
You can drag and drop files from here to download.

124
00:07:53,980 --> 00:07:57,640
So all of these things can be done anyway using the command prompt.

125
00:07:57,640 --> 00:08:00,610
But you would have to manually write the commands and execute them.

126
00:08:00,610 --> 00:08:01,900
But using FileZilla.

127
00:08:01,900 --> 00:08:05,920
And here you can do them all using this very easy graphical interface.

128
00:08:05,920 --> 00:08:07,780
And you might think we don't really need it.

129
00:08:07,780 --> 00:08:11,920
And you're right, if you're doing quick things on the cloud similar to what I showed you previously.

130
00:08:11,920 --> 00:08:16,210
But from now on, we're actually going to be modifying the files and creating phishing pages.

131
00:08:16,210 --> 00:08:20,440
So using this tool will make it much easier for you to do that.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:03,020
So going back to what we are trying to do.

2
00:00:03,050 --> 00:00:11,660
We already downloaded a clone of this website and we have it right now in our downloads directory in

3
00:00:11,660 --> 00:00:12,920
a directory called test.

4
00:00:12,920 --> 00:00:18,140
We tested this website and we saw that it actually works perfectly, and it looks like an identical

5
00:00:18,140 --> 00:00:20,750
clone of the target website, which is this one.

6
00:00:20,750 --> 00:00:25,460
So all we have to do right now is upload it to our cloud instance.

7
00:00:25,460 --> 00:00:29,240
Now we need to make sure that we upload it to the right directory.

8
00:00:29,240 --> 00:00:34,730
We said previously that Apache's web directory is var ww HTML.

9
00:00:34,730 --> 00:00:38,330
So we need to make sure that we upload it to this location.

10
00:00:38,720 --> 00:00:44,060
Now to do that you don't have to do the CD command using the terminal like we were doing before.

11
00:00:44,060 --> 00:00:49,460
All you have to do is simply type that path in here, or you can even navigate to it from here by double

12
00:00:49,460 --> 00:00:50,870
clicking the directories.

13
00:00:51,050 --> 00:00:53,810
But easier for me, I'm going to just type it in here.

14
00:00:53,810 --> 00:00:57,680
So I'm going to do var ww HTML.

15
00:00:58,010 --> 00:00:59,480
I'm going to hit enter.

16
00:01:00,330 --> 00:01:04,860
And as you can see, it's loading the files that exist in that directory.

17
00:01:04,890 --> 00:01:10,440
If you want to upload anything to this directory, all you have to do is either drag drop this file

18
00:01:10,440 --> 00:01:15,330
to the cloud instance in here, or you could right click and upload.

19
00:01:16,820 --> 00:01:17,360
Right now.

20
00:01:17,360 --> 00:01:23,480
The upload was not successful because we don't have permissions to upload to this directory.

21
00:01:23,480 --> 00:01:29,090
So you can see here in red, it's telling us that we're not allowed to upload stuff to this directory.

22
00:01:29,090 --> 00:01:35,750
And the reason for this is if we go back one directory, you will see that this directory is owned by

23
00:01:35,750 --> 00:01:36,860
the user root.

24
00:01:36,860 --> 00:01:40,910
But when we logged in we logged in with the user Kali.

25
00:01:40,910 --> 00:01:46,460
So we have to change the ownership of this directory to the root user.

26
00:01:46,670 --> 00:01:50,960
So now there is no running from executing commands using SSH.

27
00:01:50,960 --> 00:01:56,870
So we're going to have to go back to the terminal and ssh into our cloud instance using the same command

28
00:01:56,870 --> 00:01:58,160
that we seen before.

29
00:01:58,160 --> 00:02:04,430
And once you're in here we're going to have to run one very simple command to change the ownership of

30
00:02:04,430 --> 00:02:08,570
the directory to Kali, because we're logging in with the user Kali.

31
00:02:08,720 --> 00:02:14,750
So we're going to have to do sudo first to run the command as root, because we're changing the ownership

32
00:02:14,750 --> 00:02:17,510
of a directory that is owned by root.

33
00:02:17,510 --> 00:02:19,790
As you can see here, it's owned by root.

34
00:02:19,790 --> 00:02:22,640
So we have to execute the command as root.

35
00:02:22,640 --> 00:02:29,210
And then we're going to use the clone command to change the ownership of a directory.

36
00:02:29,210 --> 00:02:35,750
And then we're going to say that we want it to be owned by the user Kali which is part of the Kali group.

37
00:02:35,750 --> 00:02:43,610
And the directory that we want to do this for is var w w w HTML.

38
00:02:44,000 --> 00:02:47,930
And we're going to do dash capital R to run this recursively.

39
00:02:47,930 --> 00:02:55,280
So this command applies to any files or directories that exist within the specified directory.

40
00:02:55,640 --> 00:03:00,380
So a very simple command we're doing sudo before it because we want to execute it as root.

41
00:03:00,380 --> 00:03:03,320
Because this directory is actually owned by root.

42
00:03:03,320 --> 00:03:06,830
We're saying we want to change the ownership of a directory.

43
00:03:06,830 --> 00:03:10,640
So this is the command that you would use to change the ownership of a directory.

44
00:03:10,640 --> 00:03:14,450
We're saying we want to change the ownership to a user called Kali.

45
00:03:14,450 --> 00:03:20,270
That is part of a group that is called Kali because that is the user that that we're using to log in

46
00:03:20,270 --> 00:03:22,850
and authenticate with the cloud instance.

47
00:03:22,850 --> 00:03:27,560
And we're giving it the directory that we want to apply this, this command to.

48
00:03:27,560 --> 00:03:29,030
And it is this directory.

49
00:03:29,030 --> 00:03:30,920
It's the home directory of Apache.

50
00:03:30,920 --> 00:03:36,260
And we're saying we want to do this recursively so that this command applies to any files and directories

51
00:03:36,260 --> 00:03:38,780
that exist within the current directory.

52
00:03:39,470 --> 00:03:42,140
We're going to hit enter and we get no errors.

53
00:03:42,140 --> 00:03:48,020
So now if I go to file zilla again and refresh the current directory.

54
00:03:49,130 --> 00:03:53,570
As you can see, the ownership changed to Cali Cali and I'm logged in as Cali.

55
00:03:53,570 --> 00:03:56,450
So I should be able to modify this directory.

56
00:03:56,450 --> 00:04:04,700
And I'm already in my downloads test where I downloaded the Facebook clone page, so I just need to

57
00:04:04,700 --> 00:04:06,530
refresh in here to see it.

58
00:04:06,920 --> 00:04:08,480
And we have it right here.

59
00:04:08,480 --> 00:04:12,170
And we can upload or drag and drop to have it uploaded.

60
00:04:12,500 --> 00:04:13,760
Give it a second.

61
00:04:13,760 --> 00:04:16,130
And as you can see, we have it right here.

62
00:04:16,460 --> 00:04:21,650
Now as I mentioned previously, when you request a website using its domain name.

63
00:04:21,650 --> 00:04:28,460
So we can actually use this domain right here, or the IP IP address like so without specifying a file.

64
00:04:28,460 --> 00:04:32,330
By default it loads the index dot HTML file.

65
00:04:32,330 --> 00:04:37,370
So this file that you see right now is actually this file right here.

66
00:04:37,370 --> 00:04:43,940
But instead of loading this file I want it to load this file the Facebook clone page.

67
00:04:44,630 --> 00:04:49,310
Therefore, we're going to right click the index file and we're going to delete it.

68
00:04:49,310 --> 00:04:51,680
And we're going to name this page.

69
00:04:52,900 --> 00:04:55,960
Index dot HTML, so it loads by default.

70
00:04:56,650 --> 00:05:02,650
So now if we go back to my website, as you can see we have the default page now.

71
00:05:02,650 --> 00:05:04,300
But if I refresh it.

72
00:05:05,480 --> 00:05:09,440
You'll see we'll have an identical Facebook login page.

73
00:05:10,400 --> 00:05:16,580
So right now we have a replica of a page that we're assuming that the target person is very interested

74
00:05:16,580 --> 00:05:16,910
in.

75
00:05:16,910 --> 00:05:23,840
So from here onwards, you could embed evil code within this page, or you can configure it to store

76
00:05:23,840 --> 00:05:26,810
the login information so that you can see it later on.

77
00:05:26,810 --> 00:05:29,210
And we're going to talk about all of that later on.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:07,520
So now that we have a cloned login page, what I want to do now is modify this page so that whenever

2
00:00:07,520 --> 00:00:13,820
the user enters a username and a password and click on login, the page will store the username and

3
00:00:13,820 --> 00:00:19,520
the password for me in a file so that I can see it and get their username and password.

4
00:00:19,940 --> 00:00:25,610
To do this, we're going to go back to FileZilla and we're going to go to the index.html, because that

5
00:00:25,610 --> 00:00:28,070
is the page that is being served to the target.

6
00:00:28,070 --> 00:00:31,100
We're going to right click it and we're going to click on edit.

7
00:00:31,400 --> 00:00:38,000
This will download this index file for you and allow you to edit it using your default text editor.

8
00:00:38,000 --> 00:00:42,920
Don't get overwhelmed with the amount of code that you see in here, because we don't really need to

9
00:00:42,920 --> 00:00:44,120
modify a lot of it.

10
00:00:44,120 --> 00:00:47,360
We're only interested in this part right here.

11
00:00:47,720 --> 00:00:53,810
So the way that most login pages work is that they have what we call a form.

12
00:00:53,810 --> 00:00:56,270
So this part of the page would be a form.

13
00:00:56,270 --> 00:01:03,320
And whenever you click on the login, this forum will be submitted somewhere else in order to validate

14
00:01:03,320 --> 00:01:04,040
the login.

15
00:01:04,550 --> 00:01:09,110
So we're going to right click this to find the name of this form.

16
00:01:09,700 --> 00:01:16,780
And when we do this, we're going to see the HTML code that is responsible for rendering this page right

17
00:01:16,780 --> 00:01:17,380
here.

18
00:01:17,380 --> 00:01:23,470
And as you can see, as I move my pointer over different parts of the page, different parts of the

19
00:01:23,470 --> 00:01:30,370
page gets highlighted in here telling me that, for example, this code right here is responsible for

20
00:01:30,370 --> 00:01:34,060
rendering the part of the page that you see on the left.

21
00:01:34,570 --> 00:01:39,550
Now, if I zoom in, you will see that we have a form tag in here.

22
00:01:39,550 --> 00:01:44,770
And this is the tag that encapsulates all of this login form in here.

23
00:01:45,340 --> 00:01:51,640
So what I want to do right now is find this login form in my code, in the index dot HTML page that

24
00:01:51,640 --> 00:01:52,510
I have in here.

25
00:01:52,510 --> 00:01:58,690
Because this code is basically an untidy version of what you see in here.

26
00:01:58,810 --> 00:02:00,640
So I want to find this form.

27
00:02:00,640 --> 00:02:04,870
So you want to select something unique from what you see in here.

28
00:02:04,870 --> 00:02:10,600
So anything that looks unique to you from here Royal login form in here that looks pretty unique to

29
00:02:10,600 --> 00:02:11,020
me.

30
00:02:11,020 --> 00:02:12,670
So I'm going to copy it.

31
00:02:12,670 --> 00:02:15,310
And I'm going to go to the code in here.

32
00:02:15,310 --> 00:02:19,240
I'm going to do control F to find and I'm going to paste it.

33
00:02:19,330 --> 00:02:25,180
And as you can see it's going to bring me directly to whatever portion of this code that contains what

34
00:02:25,180 --> 00:02:26,050
I'm looking for.

35
00:02:26,050 --> 00:02:30,970
And if I just go looking back for a little bit, you'll see we have the form tag in here.

36
00:02:31,330 --> 00:02:38,230
So I'm going to place my cursor here and just go down to separate it from the rest of the code and separate

37
00:02:38,230 --> 00:02:39,760
this part of it as well.

38
00:02:40,700 --> 00:02:47,900
Now, first of all, I'm going to remove this ID parameter right here because ID parameters such as

39
00:02:47,900 --> 00:02:54,830
this one can be used to manipulate this element altogether to implement custom behavior, which can

40
00:02:54,830 --> 00:02:58,340
potentially interfere with what we are trying to do.

41
00:02:58,370 --> 00:03:04,700
So it's better to remove it just in case it will prevent us from stealing information from this form.

42
00:03:04,700 --> 00:03:06,740
So I'm simply going to remove it.

43
00:03:07,490 --> 00:03:10,370
And I'm also going to look for the submit button.

44
00:03:10,370 --> 00:03:14,060
So I'm going to do control F again I'm going to look for submit.

45
00:03:14,510 --> 00:03:17,960
And as you can see we have a button of type submit.

46
00:03:17,960 --> 00:03:19,970
And it basically says log in.

47
00:03:19,970 --> 00:03:21,710
So this is the login button.

48
00:03:22,760 --> 00:03:28,940
And if we go back in the code all the way back to here, you'll see that this is the button that is

49
00:03:28,940 --> 00:03:29,900
used to submit.

50
00:03:29,900 --> 00:03:31,340
So that's the end of it.

51
00:03:32,360 --> 00:03:34,070
That's the start of the button tag.

52
00:03:34,070 --> 00:03:37,400
That's the end of the button tag and the type of it is submit.

53
00:03:37,400 --> 00:03:41,180
So this is the login button that you click in order to login.

54
00:03:41,180 --> 00:03:43,760
And I'm simply going to look for the ID as well.

55
00:03:43,760 --> 00:03:49,250
As you can see we have an ID in here and I'm going to remove it for the same reason just in case there

56
00:03:49,250 --> 00:03:55,940
is code implemented somewhere else in the page that would use this ID and prevent me from stealing information

57
00:03:55,940 --> 00:03:56,960
from this form.

58
00:03:57,710 --> 00:03:58,970
So I'm going to remove it.

59
00:03:58,970 --> 00:04:01,520
And these steps are not always necessary.

60
00:04:01,520 --> 00:04:07,430
It depends on the target website, but removing the ID from the login and from the form will allow you

61
00:04:07,430 --> 00:04:09,920
to steal data from most websites.

62
00:04:10,760 --> 00:04:16,490
Now, what I'm actually really interested in in this form is actually the action right here.

63
00:04:16,490 --> 00:04:24,350
So the action argument in here specifies what happens once the user clicks on the login button.

64
00:04:24,770 --> 00:04:33,080
So right now when the user clicks on the login button the page will send the request to this destination.

65
00:04:33,080 --> 00:04:36,080
So everything that you see between the two quotes.

66
00:04:36,080 --> 00:04:38,150
Now I don't want that to happen.

67
00:04:38,150 --> 00:04:43,400
I want it to send the login information to another page that I create.

68
00:04:43,400 --> 00:04:49,730
So it stores this login information for me, and therefore I'm going to get it to send the login information

69
00:04:49,730 --> 00:04:53,810
to a file that is called login dot PHP.

70
00:04:53,900 --> 00:04:58,460
Now this is not going to be a real login file and this file doesn't even exist.

71
00:04:58,460 --> 00:05:00,080
I'm going to create it next.

72
00:05:00,080 --> 00:05:05,450
So whatever login information that the user input will be posted to this file.

73
00:05:05,450 --> 00:05:10,250
And then we're going to program this file to store that data into another file.

74
00:05:11,180 --> 00:05:13,640
So we're going to save this file.

75
00:05:13,640 --> 00:05:19,670
And once you save it and go back to FileZilla, you'll see you'll get a prompt telling you that the

76
00:05:19,670 --> 00:05:21,410
index file got modified.

77
00:05:21,410 --> 00:05:26,570
And do you want to upload this modified file and overwrite the existing one.

78
00:05:26,690 --> 00:05:33,200
So I'm going to say yes so that we can upload the modified file and overwrite this index.html file.

79
00:05:33,200 --> 00:05:39,860
And next we're going to need to create this login.php file because we don't have it here in this server.

80
00:05:40,220 --> 00:05:43,730
So we're going to right click and we're going to create a new file.

81
00:05:43,730 --> 00:05:46,490
And we're going to call it Login.php.

82
00:05:49,270 --> 00:05:52,660
And we're going to right click and edit this file.

83
00:05:52,660 --> 00:06:00,340
And to create a PHP file you have to put two question marks between these signs and put PHP at the start.

84
00:06:00,700 --> 00:06:04,000
And then you want to put your PHP code in here.

85
00:06:04,030 --> 00:06:06,460
Now you don't need to be a PHP programmer.

86
00:06:06,460 --> 00:06:10,000
We're going to use very, very basic PHP code for this.

87
00:06:10,000 --> 00:06:14,020
So the first thing we want to do is store the username.

88
00:06:14,020 --> 00:06:18,130
So I'm going to create a new variable that will store the username.

89
00:06:18,760 --> 00:06:27,730
And I want this variable to get the value of the username that is posted to this login dot php file.

90
00:06:28,410 --> 00:06:33,000
Now we need to know what the username is posted as.

91
00:06:33,820 --> 00:06:36,880
So we're going to right click the username input box.

92
00:06:36,880 --> 00:06:42,970
In here we're going to click on inspect to see the code responsible for displaying this part of the

93
00:06:42,970 --> 00:06:43,660
page.

94
00:06:43,660 --> 00:06:47,350
And you can see it's already being highlighted for us in here.

95
00:06:47,350 --> 00:06:48,280
And the right.

96
00:06:48,280 --> 00:06:54,430
And you can see the name of this field of this input box is email.

97
00:06:54,430 --> 00:07:02,860
So that means whatever value that we put in here is going to be posted to the Login.php under the name

98
00:07:02,860 --> 00:07:03,520
email.

99
00:07:04,170 --> 00:07:11,160
So we're going to say the username variable is equal to whatever that gets posted to us.

100
00:07:11,160 --> 00:07:18,720
So whatever that is sent over the post method under the name email and put a semicolon at the end.

101
00:07:18,720 --> 00:07:23,220
Because in PHP you have to put a semicolon at the end of every line.

102
00:07:23,220 --> 00:07:27,810
So we're simply saying I want to create a new variable and I want to call it username.

103
00:07:27,810 --> 00:07:29,340
You can call it whatever you want.

104
00:07:29,340 --> 00:07:36,270
And the value of this variable should be set to whatever that is posted to this page under the name

105
00:07:36,270 --> 00:07:36,930
email.

106
00:07:36,930 --> 00:07:43,710
And we know from looking at the code of this page, is that once the login is clicked, it's going to

107
00:07:43,710 --> 00:07:45,420
send data to the store dot PHP.

108
00:07:45,420 --> 00:07:48,000
So it's going to send data to this file right here.

109
00:07:48,000 --> 00:07:53,640
And it's going to send whatever value that is inputted in here under the name email.

110
00:07:54,410 --> 00:07:56,390
Next we want to do this to the password.

111
00:07:56,390 --> 00:07:59,000
So we right click the password input box.

112
00:07:59,000 --> 00:08:00,950
And we click on inspect.

113
00:08:00,950 --> 00:08:03,200
And the name of this input box.

114
00:08:03,200 --> 00:08:06,110
As you can see in here the name is pass.

115
00:08:06,110 --> 00:08:09,680
So the value of the password is sent under the name pass.

116
00:08:09,920 --> 00:08:13,310
So all we have to do in here is duplicate this line.

117
00:08:13,310 --> 00:08:18,230
And we're going to say this time the name of the variable should be password.

118
00:08:18,230 --> 00:08:20,780
Again you can select whatever variable name you want.

119
00:08:20,780 --> 00:08:23,600
And that's going to be sent under the name pass.

120
00:08:24,320 --> 00:08:25,040
And that's it.

121
00:08:25,040 --> 00:08:30,650
So now in our PHP file we have two variables a variable called username that will store whatever value

122
00:08:30,650 --> 00:08:36,200
that is posted as email, and a variable that is called password that will store whatever value that

123
00:08:36,200 --> 00:08:38,420
is sent under the past name.

124
00:08:38,750 --> 00:08:46,070
Now once this PHP file has access to these values, we want it to write it to a text file so that we

125
00:08:46,070 --> 00:08:51,950
can read it and see the usernames and passwords that were inputted in our page.

126
00:08:51,950 --> 00:08:55,070
And I'll show you how to do that in the next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:08,270
So now that we have a cloned login page that is programmed to send the login data to a PHP file, in

2
00:00:08,270 --> 00:00:14,780
this lecture, I'm going to show you how to program this file to store the login data in a text file,

3
00:00:14,780 --> 00:00:20,240
allowing us to see the usernames and passwords that were used in this login page.

4
00:00:20,270 --> 00:00:26,870
Assuming we don't know how to do this, you can simply go to Google and search how to write files in

5
00:00:26,870 --> 00:00:27,650
PHP.

6
00:00:27,650 --> 00:00:32,420
And it's going to get you to this page right here, which is very, very useful.

7
00:00:32,450 --> 00:00:39,590
W3 school is a really good website to learn stuff like this from, and it shows you examples and even

8
00:00:39,590 --> 00:00:43,700
more complex examples right here of creating a file and writing to it.

9
00:00:44,030 --> 00:00:47,330
So first of all you want to create a file like so.

10
00:00:47,330 --> 00:00:50,270
So I'm going to copy this and paste it in here.

11
00:00:50,270 --> 00:00:53,210
So this will create a new file called new File.

12
00:00:53,210 --> 00:00:55,370
And it's going to open it for writing.

13
00:00:55,370 --> 00:01:02,570
Now I'm actually going to change this to a plus because I want it to open the file for writing.

14
00:01:02,570 --> 00:01:05,270
But append to the end of the file.

15
00:01:05,270 --> 00:01:06,770
The reason why I'm doing this.

16
00:01:06,770 --> 00:01:13,040
Because if we leave this to W, if we just open the file for writing, this file will get overwritten

17
00:01:13,040 --> 00:01:14,720
every time this page runs.

18
00:01:14,720 --> 00:01:21,140
But when we when we do a plus, it means I want to append to it so that we don't overwrite the existing

19
00:01:21,140 --> 00:01:21,560
file.

20
00:01:21,560 --> 00:01:28,700
We just start writing to the end of the file so we won't lose the data that exists in the file already.

21
00:01:29,210 --> 00:01:32,960
And I also want to name this file data dot txt.

22
00:01:32,960 --> 00:01:35,510
So this is simply just the file name in here.

23
00:01:35,510 --> 00:01:41,630
So this piece of code right here will basically create a file for me on the server that is called data

24
00:01:41,630 --> 00:01:42,560
dot txt.

25
00:01:42,920 --> 00:01:46,370
If it fails it's going to display this message right here.

26
00:01:46,700 --> 00:01:51,110
And all of this is nicely documented in this page right here.

27
00:01:51,110 --> 00:01:53,690
So I'm not really a genius that just knows all of this.

28
00:01:53,690 --> 00:01:56,420
All you have to do is simply read this documentation.

29
00:01:57,050 --> 00:02:01,490
Now once you create this file, you can write to it using the f write method.

30
00:02:01,490 --> 00:02:06,800
So I'm going to copy this part in here and we'll go through it now once I paste it.

31
00:02:06,800 --> 00:02:12,890
So basically this code right here creates a new variable and sets its value to this.

32
00:02:12,890 --> 00:02:17,270
And then it uses the f write function to write to the file.

33
00:02:17,270 --> 00:02:23,990
So it's saying I want to write the text that we created in here to the file that we created in here.

34
00:02:24,530 --> 00:02:30,560
And then this f close simply closes the file similar to you just clicking on the X in order to close

35
00:02:30,560 --> 00:02:31,220
a file.

36
00:02:31,580 --> 00:02:35,060
Now what we want to write to this file is not Jane Doe.

37
00:02:35,090 --> 00:02:41,210
We actually want to write the values of the email and the password, and the values of the email and

38
00:02:41,210 --> 00:02:45,140
the password are stored in my username and password variables.

39
00:02:45,140 --> 00:02:50,450
So this text is going to be equal to I'm going to remove this data from here.

40
00:02:50,450 --> 00:02:52,430
And I'm going to put a new line character.

41
00:02:52,430 --> 00:02:53,780
So it's nicely formatted.

42
00:02:53,780 --> 00:02:58,010
So backward slash N puts a new line in the file that we're writing.

43
00:02:58,010 --> 00:03:02,060
So it's similar to you hitting return or enter on your keyboard.

44
00:03:02,060 --> 00:03:05,450
And I'm going to say the username is.

45
00:03:05,450 --> 00:03:07,430
So I'm putting a colon a space.

46
00:03:07,430 --> 00:03:11,870
And then I want to put the value of my username variable.

47
00:03:11,870 --> 00:03:15,920
And because this is a variable I can't put it inside the quotes.

48
00:03:15,920 --> 00:03:17,870
So I have to exit the quotes.

49
00:03:17,870 --> 00:03:23,570
And I'm going to put a dot in order to concatenate or append this variable to the text.

50
00:03:23,570 --> 00:03:26,690
And I'm going to put the variable name which is username.

51
00:03:26,990 --> 00:03:32,270
Then I'm going to put another dot because I want to start typing normal text now not a variable.

52
00:03:32,270 --> 00:03:36,590
And I'm going to put a new line character backwards slash n like I said.

53
00:03:36,590 --> 00:03:42,410
And then I'm going to say the password is again a dot to concatenate.

54
00:03:42,410 --> 00:03:45,140
And then we're going to put the password variable.

55
00:03:45,840 --> 00:03:50,010
So we're setting the text variable to a text that says username colon.

56
00:03:50,010 --> 00:03:53,910
And then we append the value of the username variable in here.

57
00:03:53,910 --> 00:03:57,780
Then we say the password is whatever value we get in the password.

58
00:03:58,230 --> 00:04:00,060
Then we're going to write this data.

59
00:04:00,060 --> 00:04:05,070
So we're going to write to my file which we opened in here the text that we defined in here.

60
00:04:05,070 --> 00:04:07,080
And then we're going to close the file.

61
00:04:07,080 --> 00:04:08,490
Very very simple.

62
00:04:08,520 --> 00:04:11,100
So let's go ahead and test this.

63
00:04:11,100 --> 00:04:16,410
So I'm going to save this file I'm going to go to FileZilla I'm going to say yes we want to upload it.

64
00:04:16,410 --> 00:04:18,090
And that file should be uploaded.

65
00:04:18,090 --> 00:04:19,620
So we have it right here.

66
00:04:19,770 --> 00:04:22,320
And let's go ahead and test it.

67
00:04:22,320 --> 00:04:24,450
So we go to the target machine.

68
00:04:24,450 --> 00:04:28,530
Let's close this and let's refresh the page.

69
00:04:29,570 --> 00:04:31,490
And let's put a test user name.

70
00:04:31,490 --> 00:04:34,160
So let's just say test at test.com doesn't really matter.

71
00:04:34,160 --> 00:04:35,360
And let's put a password.

72
00:04:35,360 --> 00:04:37,280
So let's put whatever.

73
00:04:37,460 --> 00:04:39,920
And we're going to click on login.

74
00:04:40,250 --> 00:04:44,030
And as you can see we got redirected to Login.php.

75
00:04:44,300 --> 00:04:48,470
But we're getting a message saying unable to open file.

76
00:04:48,470 --> 00:04:54,200
So if we go back to our text you can see in here it's saying try to open this file.

77
00:04:54,200 --> 00:04:59,060
And if you can't then display this message saying unable to open file.

78
00:04:59,060 --> 00:05:06,260
And this is happening because we are trying to write to this directory in here, we're trying to create

79
00:05:06,260 --> 00:05:08,270
a file called Data.txt.

80
00:05:08,570 --> 00:05:11,750
But this directory is owned by a user named Kali.

81
00:05:11,750 --> 00:05:16,310
As you know we're logging in as Kali and we changed the ownership before to Kali.

82
00:05:16,310 --> 00:05:22,520
But we're trying to write to it as nobody, as somebody that is simply just loading the web server.

83
00:05:22,520 --> 00:05:24,530
Therefore it is not allowed.

84
00:05:24,530 --> 00:05:28,070
So what I'm going to do, I'm going to create a new folder in here.

85
00:05:28,490 --> 00:05:30,620
And I'm just going to call it data.

86
00:05:32,440 --> 00:05:35,050
And I'm going to set the permissions of this folder.

87
00:05:35,050 --> 00:05:38,980
So I'm going to right click it and change the file permissions.

88
00:05:38,980 --> 00:05:41,740
And I'm going to change it to 777.

89
00:05:41,740 --> 00:05:45,610
So as you can see it takes all of the boxes for everybody.

90
00:05:45,610 --> 00:05:51,880
So everybody can read, write and execute whatever files we put in this directory.

91
00:05:51,880 --> 00:05:53,080
That is called data.

92
00:05:53,730 --> 00:06:02,070
And then I'm going to edit my code in here to store this in data forward slash data dot txt.

93
00:06:02,100 --> 00:06:08,730
So instead of storing the data in this home directory, I'm going to store it in another directory that

94
00:06:08,730 --> 00:06:11,160
has permissions for everybody to write in.

95
00:06:11,160 --> 00:06:12,990
And that is called data.

96
00:06:13,500 --> 00:06:15,180
So I'm going to save this.

97
00:06:15,180 --> 00:06:19,260
And we're going to say yes in here to apply all the changes.

98
00:06:19,260 --> 00:06:23,580
We're going to go to the target computer, go back to the login page.

99
00:06:23,850 --> 00:06:29,040
And again we're logging in with test at test and put a username and a password.

100
00:06:29,040 --> 00:06:32,010
We're going to click on Log In and perfect.

101
00:06:32,010 --> 00:06:37,140
Now we don't see any error messages which means that it should probably have worked.

102
00:06:37,230 --> 00:06:39,540
So we're going to go back to FileZilla.

103
00:06:39,810 --> 00:06:42,300
We have the data directory in here.

104
00:06:43,460 --> 00:06:44,600
And inside it.

105
00:06:44,600 --> 00:06:46,700
Sure enough, we have a new text file.

106
00:06:46,730 --> 00:06:51,110
Now if we right click and click on View Edit.

107
00:06:52,290 --> 00:06:58,110
You will see that we have the username and the password stored for us in this directory.

108
00:06:58,890 --> 00:07:00,570
Now this is good.

109
00:07:00,570 --> 00:07:01,230
This is great.

110
00:07:01,230 --> 00:07:07,050
So now you can send this login page that looks identical to Facebook to anybody.

111
00:07:07,050 --> 00:07:12,600
And whenever they put their username and password you'll be able to capture it.

112
00:07:12,750 --> 00:07:19,260
And like I said we will talk about how to make this more believable and easier to deliver to the target.

113
00:07:19,260 --> 00:07:25,320
But once they log in, once they put their username and password, they're just getting a blank page,

114
00:07:25,320 --> 00:07:27,180
which is very, very suspicious.

115
00:07:27,180 --> 00:07:33,000
So let me show you how easy it is to actually get them to be redirected to wherever you want, depending

116
00:07:33,000 --> 00:07:34,620
on your situation.

117
00:07:34,620 --> 00:07:37,680
So in our example we have a clone of Facebook.

118
00:07:37,680 --> 00:07:43,530
So it would be appropriate to redirect them to Facebook to the real Facebook once they put their login

119
00:07:43,530 --> 00:07:44,460
information.

120
00:07:44,910 --> 00:07:47,610
And doing this again is very simple in PHP.

121
00:07:47,610 --> 00:07:50,400
And you don't have to be a genius or a great programmer.

122
00:07:50,400 --> 00:07:53,610
All you have to do is simply Google redirect PHP.

123
00:07:53,640 --> 00:08:00,600
You will get to this page that is actually part of the PHP manual, and it explains to you how to do

124
00:08:00,600 --> 00:08:04,230
this again with a very good example right here.

125
00:08:04,680 --> 00:08:12,540
So all you have to do is simply copy this example, go back to our PHP file and paste it at the end

126
00:08:12,540 --> 00:08:19,650
of the file, so that once we finish doing all of this, we're going to change the location of the browser

127
00:08:19,650 --> 00:08:22,440
to whatever website we specify in here.

128
00:08:22,440 --> 00:08:25,500
And I want them to go to facebook.com.

129
00:08:26,380 --> 00:08:27,970
It's as simple as that.

130
00:08:28,060 --> 00:08:30,640
And this is going to be Https.

131
00:08:31,570 --> 00:08:34,870
And we're going to save it and save this.

132
00:08:35,690 --> 00:08:37,310
And let's go ahead and test it.

133
00:08:37,910 --> 00:08:40,160
So we're going to do a refresh.

134
00:08:41,000 --> 00:08:44,240
And we're going to log in with the same username.

135
00:08:44,240 --> 00:08:46,430
And let's put another password this time.

136
00:08:46,430 --> 00:08:49,460
And note that this password will be appended to the file.

137
00:08:49,460 --> 00:08:53,840
The file will not be overwritten because we use the A plus in here.

138
00:08:54,230 --> 00:08:56,330
And we're going to click on log in.

139
00:08:57,340 --> 00:08:58,150
And perfect.

140
00:08:58,150 --> 00:09:01,450
As you can see, the user goes back to the official Facebook.

141
00:09:01,450 --> 00:09:05,740
But if we go back and look at our data again.

142
00:09:07,770 --> 00:09:12,120
As you can see, we have a new username and password with the new password.

143
00:09:12,120 --> 00:09:13,440
It was la la la la la.

144
00:09:13,440 --> 00:09:18,450
And now the user got redirected to the official original Facebook.

145
00:09:18,450 --> 00:09:21,870
So it is much less suspicious and much more believable.

146
00:09:22,680 --> 00:09:25,290
So with this, you don't really need to use any tools.

147
00:09:25,290 --> 00:09:28,590
You don't need to rely on all of these tools that break all of the time.

148
00:09:28,590 --> 00:09:31,500
You can simply do all of it yourself manually.

149
00:09:31,500 --> 00:09:36,420
So not only that, you'll understand every single aspect of it and be able to improve it.

150
00:09:36,420 --> 00:09:37,980
You will also never fail.

151
00:09:37,980 --> 00:09:43,350
You'll never have to wait for a developer to update their tool or ask them why it's failing.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:07,430
Previously, we learned how to create identical copies of existing legitimate websites or clone websites,

2
00:00:07,430 --> 00:00:14,360
and we also learned how to manually clone login pages, such as this one right here, and have it store

3
00:00:14,360 --> 00:00:18,980
the username and the password so that we can see them when the target logs in.

4
00:00:19,010 --> 00:00:24,020
Now all of that is great, but we actually have a little bit of a problem.

5
00:00:24,200 --> 00:00:30,560
If you look at the URL in here, first of all you can see it's basically just the IP address of our

6
00:00:30,560 --> 00:00:31,160
server.

7
00:00:31,160 --> 00:00:34,490
You can also see there is an icon in here saying dangerous.

8
00:00:34,490 --> 00:00:37,190
Again, this makes this website more suspicious.

9
00:00:37,190 --> 00:00:42,620
And to add to all of these issues, the first time that you load this website, you're actually going

10
00:00:42,620 --> 00:00:48,500
to get a warning such as this one a really intrusive bad warning telling you that this website could

11
00:00:48,500 --> 00:00:55,280
be dangerous and the only way for you to get in is if you click on more details and then click on visit

12
00:00:55,280 --> 00:00:56,660
this unsafe website.

13
00:00:57,110 --> 00:01:03,080
So all of these issues makes what we learned previously kind of useless, because the target will never

14
00:01:03,080 --> 00:01:05,210
actually put their username and password.

15
00:01:05,330 --> 00:01:11,540
So in this lecture and in the next lectures, I want to teach you how to remove this dangerous icon

16
00:01:11,540 --> 00:01:18,290
and actually have it say secure and how to have an actual domain name in here so that this website looks

17
00:01:18,290 --> 00:01:19,460
much more legit.

18
00:01:19,460 --> 00:01:24,800
And the information that I'm going to teach you can be used with any website you host.

19
00:01:24,800 --> 00:01:31,190
So whether it's a website with an evil code or if it's a login screen like what we have in here, or

20
00:01:31,190 --> 00:01:36,320
if it's even your own personal website, I'm going to show you how to have it say secure in here by

21
00:01:36,320 --> 00:01:38,180
enabling Https.

22
00:01:38,180 --> 00:01:43,910
And I'm going to show you how to link an actual real domain name in here, so that when it's loaded,

23
00:01:43,910 --> 00:01:47,660
you will see something similar to what you have in here, like facebook.com.

24
00:01:47,660 --> 00:01:52,850
This is the legitimate Facebook website, and you would also see the lock icon in here.

25
00:01:52,850 --> 00:01:59,060
This makes the website look much less suspicious and therefore increases the chances of having a successful

26
00:01:59,060 --> 00:01:59,780
attack.

27
00:02:00,250 --> 00:02:06,280
So what we're doing so far, we're putting the IP of our web server and our web browser, and therefore

28
00:02:06,280 --> 00:02:08,530
we're loading the website in our web server.

29
00:02:08,530 --> 00:02:10,000
So very, very simple.

30
00:02:10,000 --> 00:02:16,840
But the goal is to have this web server or this website load whenever the user types in an actual website

31
00:02:16,870 --> 00:02:18,730
name, like Z.com.

32
00:02:19,240 --> 00:02:25,240
And for us to do that, we have to first of all understand what happens when a user puts in a normal

33
00:02:25,240 --> 00:02:27,580
domain name in their web browser.

34
00:02:27,580 --> 00:02:32,350
So for example, we have a user in here and they want to go to facebook.com.

35
00:02:32,350 --> 00:02:39,460
Now the browser does not know where facebook.com is and can only communicate with it using the IP,

36
00:02:39,460 --> 00:02:41,920
but the user is only given the domain name.

37
00:02:41,920 --> 00:02:43,960
So what happens in that case?

38
00:02:43,960 --> 00:02:51,670
The web browser is going to make a DNS request to a DNS server, and the DNS server is basically just

39
00:02:51,670 --> 00:02:57,040
a computer on the cloud or on the internet that contains a number of records.

40
00:02:57,040 --> 00:03:01,540
And as you can see, each record has a domain name and an IP address.

41
00:03:01,540 --> 00:03:09,070
So it basically translates domain name to the IP address of the server hosting the website that is being

42
00:03:09,070 --> 00:03:09,910
requested.

43
00:03:10,550 --> 00:03:13,040
So the user is asking for facebook.com.

44
00:03:13,040 --> 00:03:19,430
The DNS server is going to go to the record that contains facebook.com and give a response with the

45
00:03:19,430 --> 00:03:21,740
IP of Facebook's server.

46
00:03:21,740 --> 00:03:27,950
So the user then is going to get the IP of Facebook, and therefore it's going to be able to make a

47
00:03:27,950 --> 00:03:33,740
direct request to the server hosting Facebook's website and therefore get access to Facebook.

48
00:03:33,740 --> 00:03:38,690
But the user never actually needed to remember the IP of Facebook.

49
00:03:38,690 --> 00:03:40,910
They basically typed facebook.com.

50
00:03:40,910 --> 00:03:46,640
They ask the DNS server, and the DNS server gives us the IP of facebook.com.

51
00:03:47,530 --> 00:03:53,440
So if we want to do the same with our hacker web server, we're going to have to register a new domain

52
00:03:53,440 --> 00:03:53,860
name.

53
00:03:53,860 --> 00:04:00,490
And let's say we're going to call it login page.com and have that domain name link to the IP address

54
00:04:00,490 --> 00:04:03,160
of our web server on the cloud.

55
00:04:03,820 --> 00:04:10,000
As a result, when the user types in login page.com, the web browser is not going to know where to

56
00:04:10,000 --> 00:04:10,390
go.

57
00:04:10,390 --> 00:04:17,050
So it's going to send a DNS request to the DNS server asking for the IP of login page.com.

58
00:04:17,500 --> 00:04:22,240
The DNS server is going to check its records, and it does actually have a record of that.

59
00:04:22,240 --> 00:04:23,530
And it has the IP.

60
00:04:23,530 --> 00:04:27,430
So it's going to respond with the IP of the hacker's server.

61
00:04:27,430 --> 00:04:33,550
And then as a result, the web browser is actually going to request the website or the web server that

62
00:04:33,550 --> 00:04:35,290
is running on this IP.

63
00:04:36,330 --> 00:04:43,230
So all we have to do for this to work is to actually purchase a domain name and have it link to our

64
00:04:43,230 --> 00:04:44,670
cloud server IP.

65
00:04:44,880 --> 00:04:50,100
Now, there are a large number of websites that you can use to buy domain names.

66
00:04:50,130 --> 00:04:56,970
They're called domain name registrars, and the price usually depends on the name that you pick.

67
00:04:56,970 --> 00:04:59,670
So some names are more expensive than others.

68
00:04:59,700 --> 00:05:06,120
I prefer using Name.com, but you can use any other website, and the steps of purchasing a domain name

69
00:05:06,120 --> 00:05:09,150
and linking it to a server is almost the same.

70
00:05:09,150 --> 00:05:13,440
The only difference is the theme or the user experience on the website.

71
00:05:13,440 --> 00:05:17,340
So once you learn how to do it, you can basically do it with any website.

72
00:05:17,340 --> 00:05:21,840
But like I said, I prefer using Name.com, so that's the one I'm going to use.

73
00:05:22,050 --> 00:05:26,820
So all you have to do is go to the website that you want to register the domain with.

74
00:05:26,820 --> 00:05:29,130
So I'm going to go to Name.com.

75
00:05:29,130 --> 00:05:34,830
And then all of these websites will have a search box like this one that allows you to search for a

76
00:05:34,830 --> 00:05:35,520
domain name.

77
00:05:35,520 --> 00:05:37,740
Because domain names have to be unique.

78
00:05:37,740 --> 00:05:43,560
So you can register any name you want, as long as the name is not taken, as long as the name is not

79
00:05:43,560 --> 00:05:45,450
registered by someone else.

80
00:05:45,450 --> 00:05:51,630
So you should try to register a name that looks similar to the name of the website that you're trying

81
00:05:51,630 --> 00:05:52,290
to clone.

82
00:05:52,290 --> 00:05:58,830
For example, if you're cloning the security, maybe try to register a domain that's called the security,

83
00:05:58,830 --> 00:06:04,350
but is missing an eye or has two eyes instead of one eye, so you can be a little bit creative with

84
00:06:04,350 --> 00:06:05,010
this.

85
00:06:05,010 --> 00:06:11,070
But in our case, we are serving a fake login page for Facebook, and all of the domains that sound

86
00:06:11,070 --> 00:06:13,680
similar to Facebook are actually already taken.

87
00:06:13,680 --> 00:06:19,710
That's why we're going to register a domain name that is a little bit generic, for example login form.

88
00:06:19,710 --> 00:06:22,680
And you don't actually need to say.com or.co.

89
00:06:22,680 --> 00:06:26,040
It's actually going to search for all of the possible tdls.

90
00:06:26,040 --> 00:06:32,340
So it's going to list a lot of other tdls that you never even heard of, such as.io, such as dot support,

91
00:06:32,340 --> 00:06:34,770
dot Rockstar, and the list goes on.

92
00:06:34,770 --> 00:06:39,240
So as you can see, we can by login form dot support for 821.

93
00:06:39,630 --> 00:06:42,840
And then we have all of the other options in here like.org.

94
00:06:42,870 --> 00:06:45,090
Dot io, dot limited.

95
00:06:45,330 --> 00:06:51,420
And as you can see the price is usually around the €10 mark, except if the domain name is really good.

96
00:06:51,420 --> 00:06:55,110
For example the.io in here will cost you €51.

97
00:06:56,080 --> 00:07:01,360
So I'm actually going to go with login form Co which is only €13.35.

98
00:07:01,360 --> 00:07:06,760
And then later on I'm going to show you how to play with this domain name, with a few tricks to make

99
00:07:06,760 --> 00:07:12,280
it look very, very believable and pass as an actual login page for Facebook.

100
00:07:12,280 --> 00:07:15,580
But for now we want to purchase this domain name or register it.

101
00:07:15,580 --> 00:07:19,930
So all you have to do just like any other shopping website, click on Add to Cart.

102
00:07:20,520 --> 00:07:22,920
Then we're going to click on checkout to check out.

103
00:07:24,160 --> 00:07:26,140
It's going to try to sell you a few add ons.

104
00:07:26,140 --> 00:07:28,060
We're just going to say continue to check out.

105
00:07:28,060 --> 00:07:34,180
And like I said, using this is very similar on any website that sells domains or domain registrars.

106
00:07:34,180 --> 00:07:36,760
The only thing that would be different is the theme.

107
00:07:36,760 --> 00:07:42,280
I'm actually going to keep the advanced privacy in here, because that will hide my personal information,

108
00:07:42,280 --> 00:07:48,160
because people can actually look up personal information of the person that registered a domain.

109
00:07:48,160 --> 00:07:51,490
So if you enable this option, your information will be hidden.

110
00:07:51,490 --> 00:07:54,040
So I highly recommend keeping this option.

111
00:07:54,040 --> 00:07:58,060
And then we're going to go to the next step which is going to ask me to log in.

112
00:07:58,060 --> 00:08:02,380
Now if you don't have an account with them you can click on register and sign up to an account.

113
00:08:02,380 --> 00:08:03,400
It's very, very easy.

114
00:08:03,400 --> 00:08:04,780
So I'm not going to cover that.

115
00:08:04,780 --> 00:08:07,870
I already have an account, so I'm just going to log in to my account.

116
00:08:09,280 --> 00:08:12,100
And now that I'm logged in, we have the payment page.

117
00:08:12,100 --> 00:08:16,390
Similar to any other checkout or payment page you want to fill up your information.

118
00:08:16,390 --> 00:08:19,990
I already have my information stored, so I'm just going to continue.

119
00:08:22,460 --> 00:08:23,330
And that's it.

120
00:08:23,330 --> 00:08:29,000
Now we actually own this domain name, so we don't even have to link it to any website.

121
00:08:29,000 --> 00:08:32,300
Some people buy domain names and keep them and sell them later on.

122
00:08:32,300 --> 00:08:37,520
But the idea is now we own this domain name and we can do whatever we want with it.

123
00:08:37,520 --> 00:08:44,600
And in the next lecture, I'm going to show you how to modify its settings so that it links to our web

124
00:08:44,600 --> 00:08:50,930
server, so that when people type this domain name in their web browser, they'll be directed to our

125
00:08:50,930 --> 00:08:51,890
web server.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,480 --> 00:00:06,150
Now that we have the domain name bought and registered in this lecture, I'm going to teach you how

2
00:00:06,150 --> 00:00:15,450
to modify its DNS settings and add a DNS record so that the requests sent to this domain name are translated

3
00:00:15,450 --> 00:00:23,130
and sent to the IP address that we specify, which is going to be the IP address of our cloud web hosting.

4
00:00:23,790 --> 00:00:28,170
And like I said previously, I'm going to be doing all of this on Name.com.

5
00:00:28,170 --> 00:00:30,240
But the steps are actually the same.

6
00:00:30,240 --> 00:00:33,810
And the way that DNS records work is exactly the same.

7
00:00:33,810 --> 00:00:39,150
So once you know how to do this with Name.com, you'll be able to do it with any other website that

8
00:00:39,150 --> 00:00:40,230
sells domains.

9
00:00:40,920 --> 00:00:46,410
So I'm going to go to my domains to get a list of all of the domains that I own.

10
00:00:46,410 --> 00:00:51,720
And I've registered, and I'm going to click on the domain that I want to modify its settings.

11
00:00:52,110 --> 00:00:55,170
And it's this one right here login form.co.

12
00:00:56,700 --> 00:01:04,440
So regardless of what website you use to buy the domain, modifying and editing DNS records is always

13
00:01:04,440 --> 00:01:05,010
the same.

14
00:01:05,010 --> 00:01:09,330
And that's what you want to do to edit the domain settings basically.

15
00:01:10,020 --> 00:01:11,520
So we're going to click on that.

16
00:01:11,520 --> 00:01:16,500
And as you can see you're going to get a few inputs that allow you to add records.

17
00:01:16,500 --> 00:01:19,740
And what we want to do we want to add an A record.

18
00:01:19,740 --> 00:01:25,200
So as you can see in the table in here, I always said we're going to be adding an A record.

19
00:01:26,250 --> 00:01:34,560
And this a record is going to redirect any request made to our domain, which is login from Co to the

20
00:01:34,560 --> 00:01:37,110
IP that we're going to specify in here.

21
00:01:37,110 --> 00:01:42,390
So we can get our IP from here from the cloud management page.

22
00:01:42,390 --> 00:01:44,730
And I'm just going to paste it in here.

23
00:01:45,330 --> 00:01:50,820
So we're saying we want to redirect any request made to this domain to this IP address.

24
00:01:51,240 --> 00:01:53,100
We're going to click on Add Record.

25
00:01:53,460 --> 00:01:54,390
And that's it.

26
00:01:54,390 --> 00:01:58,320
As you can see now we have a record similar to what I've actually said in here.

27
00:01:58,320 --> 00:02:01,530
The type is an A record as you can see in here.

28
00:02:01,770 --> 00:02:07,830
And it's redirecting any requests made to the domain name that specified in here to this IP address,

29
00:02:07,830 --> 00:02:11,190
which is the IP address of my cloud server.

30
00:02:11,580 --> 00:02:19,080
Now DNS changes can take hours and sometimes up to a full day to fully update across all of the DNS

31
00:02:19,080 --> 00:02:20,490
servers around the world.

32
00:02:20,490 --> 00:02:26,070
So once you apply the setting, do not expect this domain name to redirect to your server.

33
00:02:26,070 --> 00:02:29,010
You're going to have to give it a few minutes and sometimes hours.

34
00:02:29,010 --> 00:02:33,900
So I'm going to pause this video and I'm going to resume once the changes take effect.

35
00:02:34,830 --> 00:02:39,270
Okay, so I've waited actually for a few minutes and let's see if this is going to work.

36
00:02:39,270 --> 00:02:40,950
So we're going to copy the domain name.

37
00:02:40,950 --> 00:02:43,500
I'm going to open a new tab and we're going to paste it.

38
00:02:44,230 --> 00:02:45,310
Let's go ahead.

39
00:02:45,310 --> 00:02:49,630
And it looks like it's working because we're getting this warning saying deceptive site ahead.

40
00:02:49,630 --> 00:02:52,060
So like I said, this warning is really, really bad.

41
00:02:52,060 --> 00:02:57,280
And it's gonna basically make whatever website that you have in here very suspicious.

42
00:02:57,280 --> 00:03:00,670
And it will probably stop anybody from visiting your website.

43
00:03:00,670 --> 00:03:06,520
But don't worry, you're getting this warning because our website does not use Https, it only uses

44
00:03:06,520 --> 00:03:07,300
Http.

45
00:03:07,300 --> 00:03:12,670
So I'm going to cover how to bypass this warning and enable Https on the website later on.

46
00:03:12,670 --> 00:03:15,790
So for now just to test it we're going to click on details.

47
00:03:15,790 --> 00:03:18,400
We're going to say continue to this unsafe site.

48
00:03:18,400 --> 00:03:19,330
And perfect.

49
00:03:19,330 --> 00:03:24,850
As you can see we're getting our cloned website loading that looks identical to Facebook.

50
00:03:24,850 --> 00:03:26,770
So as you can see we have the login form.

51
00:03:26,770 --> 00:03:29,140
We have everything similar to what we've done before.

52
00:03:29,140 --> 00:03:33,640
If we log in, this will register the username and password and store them for me on file.

53
00:03:34,090 --> 00:03:35,680
Obviously I'm not going to cover that now.

54
00:03:35,680 --> 00:03:42,640
We've tested it before and the main thing is we're able to access it using a normal name login form.co

55
00:03:42,640 --> 00:03:47,110
instead of a suspicious IP address like what we have in here.

56
00:03:47,840 --> 00:03:55,190
Now, one thing that is worth mentioning is if you are cloning a website that is not as popular as Facebook,

57
00:03:55,190 --> 00:04:01,400
so something like Z security, for example, you might be able to purchase a name or buy a domain name

58
00:04:01,400 --> 00:04:04,760
that looks almost the same as the target domain name.

59
00:04:04,760 --> 00:04:09,050
So you could replace the I in the security with a number one.

60
00:04:09,050 --> 00:04:13,910
Or if you have a website that has O, then you can replace the O with a zero.

61
00:04:13,910 --> 00:04:19,010
So you could play with the name itself when you're buying the domain name to make it look even more

62
00:04:19,010 --> 00:04:21,380
legit and harder to spot.

63
00:04:21,650 --> 00:04:26,840
But in our example, we're trying to target Facebook, so all of the names that sound like Facebook

64
00:04:26,840 --> 00:04:28,130
are actually already bought.

65
00:04:28,130 --> 00:04:33,470
That's why we're going with something like Login form Co, but I'm actually going to show you a few

66
00:04:33,500 --> 00:04:37,130
URL manipulation ideas that will make this more believable.

67
00:04:37,130 --> 00:04:43,190
But before doing that, I'm going to show you how to add a sub domain to this, which also, in my opinion,

68
00:04:43,190 --> 00:04:47,690
makes it more believable and makes this website look more legit.

69
00:04:47,690 --> 00:04:50,060
So we're going to go back to the DNS settings.

70
00:04:50,060 --> 00:04:55,220
And this time, instead of adding an A record, we're actually going to add a C name.

71
00:04:55,460 --> 00:05:02,900
And the CNAME record allows us to create a sub domain and link it to another domain or sub domain.

72
00:05:02,900 --> 00:05:10,010
So what I mean by that is I can type Facebook in here and that's going to create a sub domain for me

73
00:05:10,010 --> 00:05:12,950
that is called Facebook login form.co.

74
00:05:12,950 --> 00:05:19,070
And it's going to link it to whatever domain I type in here which is going to be this domain.

75
00:05:19,070 --> 00:05:22,730
So I'm just going to do login form.co.

76
00:05:23,210 --> 00:05:25,190
We're going to click on Add Record.

77
00:05:26,250 --> 00:05:33,990
And as a result, all the requests made to Facebook login Form Co will be redirected to login form Co.

78
00:05:33,990 --> 00:05:40,470
And as a result, this website is going to load now again, just like any other DNS setting, this could

79
00:05:40,470 --> 00:05:43,170
take a few minutes up to hours to fully update.

80
00:05:43,170 --> 00:05:48,390
So I'm going to pause the video and resume the recording once these changes take effect.

81
00:05:49,400 --> 00:05:49,940
Okay.

82
00:05:49,940 --> 00:05:51,290
So let's go ahead and test it.

83
00:05:51,290 --> 00:05:55,670
So we're going to go to Facebook dot login form.co.

84
00:05:56,000 --> 00:05:57,170
And perfect.

85
00:05:57,170 --> 00:06:02,420
As you can see now again we're getting the normal login page for Facebook that will store the username

86
00:06:02,420 --> 00:06:03,140
and the password.

87
00:06:03,140 --> 00:06:04,430
We created this before.

88
00:06:04,430 --> 00:06:10,430
But the main cool thing in here is the URL is Facebook dot login form.co.

89
00:06:10,430 --> 00:06:13,640
So this is very very believable in my opinion.

90
00:06:13,640 --> 00:06:19,340
And even if you think it's not believable and not many people will fall for this, keep in mind that

91
00:06:19,340 --> 00:06:21,740
we still haven't enabled Https on it.

92
00:06:21,740 --> 00:06:26,870
So once you have the log in here and once it looks like this, so many people will fall for it.

93
00:06:26,870 --> 00:06:31,580
You might not fall for it because you are security savvy and you're doing this course and you're interested

94
00:06:31,580 --> 00:06:32,060
in this.

95
00:06:32,060 --> 00:06:37,910
But trust me, once we finish building up this believable website, you should go ahead and show it

96
00:06:37,910 --> 00:06:41,570
to a few friends or co-workers and see what they think of it.

97
00:06:41,570 --> 00:06:44,930
Don't tell them this is a fake website, just see what they're going to think of it.

98
00:06:44,930 --> 00:06:47,660
And I'm sure a lot of them are going to fall for it.

99
00:06:47,660 --> 00:06:50,630
And trust me, I'm speaking from experience.

100
00:06:50,630 --> 00:06:56,810
A lot of the phishing campaigns that you hear of in the news, they actually all use cheap or free domain

101
00:06:56,810 --> 00:06:57,050
names.

102
00:06:57,050 --> 00:07:01,310
So the domain name will just look something like gibberish or gibberish or whatever.

103
00:07:01,310 --> 00:07:03,710
So none of them looks this believable.

104
00:07:03,710 --> 00:07:09,470
So once we have this done, once I show you more URL manipulation tricks, and once we have the lock

105
00:07:09,470 --> 00:07:15,020
in here, you're going to be able to build your own phishing pages and malicious pages like the ones

106
00:07:15,020 --> 00:07:20,420
with the beef code that will look very, very believable and identical to real websites.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:04,460
Previously, we showed how to clone a website that looks identical to Facebook.

2
00:00:04,460 --> 00:00:08,060
And as you can see, if you go to our IP, you have the website loading.

3
00:00:08,060 --> 00:00:11,900
And then we showed you how to link a domain name to this website.

4
00:00:11,900 --> 00:00:15,710
So this is actually a different domain name than what I showed you in the previous lecture.

5
00:00:15,710 --> 00:00:17,000
But the idea is the same.

6
00:00:17,000 --> 00:00:19,010
This domain is called Facebook login.

7
00:00:19,280 --> 00:00:20,780
So I own that domain.

8
00:00:20,780 --> 00:00:24,470
So I linked it to this server on this IP address.

9
00:00:24,470 --> 00:00:29,180
And therefore when you go to this domain you are getting the cloned Facebook website.

10
00:00:29,730 --> 00:00:36,300
So from now onwards we want to take our fake websites to the next level so they look 100% legit.

11
00:00:36,330 --> 00:00:42,480
So if you compare this website to the real Facebook right here, you will notice a few differences.

12
00:00:42,510 --> 00:00:49,410
First of all, you can see that there is a red sign over the lock, meaning that this is not secure

13
00:00:49,410 --> 00:00:53,220
and the normal Facebook is loading over Https.

14
00:00:53,220 --> 00:00:57,630
And this website that we created is loading over plain Http.

15
00:00:57,630 --> 00:00:59,850
That's why you don't see the Https.

16
00:01:00,090 --> 00:01:06,660
And finally, if you select the input box, as you can see here, it's giving you a message saying that

17
00:01:06,660 --> 00:01:08,160
this connection is not secure.

18
00:01:08,190 --> 00:01:13,080
Now only Firefox shows this, but in Chrome you will still see not secure.

19
00:01:13,080 --> 00:01:14,220
If we double click it.

20
00:01:14,220 --> 00:01:17,550
There is no Https and there is no lock icon.

21
00:01:18,130 --> 00:01:24,520
So the goal is to add the lock icon similar to the Facebook in here, and to remove this message that

22
00:01:24,520 --> 00:01:28,030
we're getting in here, that it's saying the connection is not secure.

23
00:01:28,030 --> 00:01:32,320
And to see https beside the URL.

24
00:01:32,320 --> 00:01:38,410
As you can see in here, once you enable Https, everything else is going to happen by default.

25
00:01:38,410 --> 00:01:42,490
So once you enable Https, you're going to see the lock icon by default.

26
00:01:42,490 --> 00:01:46,480
And you're not going to see the warning messages when you click the input boxes.

27
00:01:47,420 --> 00:01:52,940
This knowledge is actually very, very useful because you don't have to use it with malicious pages

28
00:01:52,940 --> 00:01:57,410
only you can actually use it with any website that you're on, and you're going to be able to enable

29
00:01:57,440 --> 00:02:01,790
Https on it, which will increase user trust and make it more secure.

30
00:02:01,790 --> 00:02:05,420
You can also use it with other things that we're going to learn later on in the course.

31
00:02:05,420 --> 00:02:09,860
You can even use it with the malicious pages that contain BFS code.

32
00:02:09,860 --> 00:02:15,680
So you're going to be able to serve an identical page of any website that you want with Https enabled,

33
00:02:15,680 --> 00:02:20,480
and it's going to contain BFS code in the background that will hook the target to beef.

34
00:02:20,480 --> 00:02:28,790
But before learning how to enable Https on our server, let's talk about what is Https.

35
00:02:28,790 --> 00:02:32,870
So as we know, normally websites are loading over Http in here.

36
00:02:32,870 --> 00:02:36,620
And what we want to do is get them to load over Https.

37
00:02:36,620 --> 00:02:44,150
The s in here simply stands for secure, and this extra security is provided using SSL, which then

38
00:02:44,150 --> 00:02:47,120
got superseded by TLS.

39
00:02:47,120 --> 00:02:55,190
Basically, the added security will simply encrypt the data that is being sent between the client and

40
00:02:55,190 --> 00:02:55,640
the server.

41
00:02:55,640 --> 00:02:57,890
So between the user and the website.

42
00:02:57,890 --> 00:02:59,780
Let me show you a quick example.

43
00:02:59,780 --> 00:03:03,590
So right here we have an example of simply using Http.

44
00:03:03,590 --> 00:03:07,670
And this user is sending a password to google.com.

45
00:03:07,670 --> 00:03:12,230
Now using Http this password is being sent in plain text.

46
00:03:12,230 --> 00:03:17,660
So if anybody intercepts this password and I cover a lot of ways to become the man in the middle and

47
00:03:17,660 --> 00:03:23,870
intercept data in my other courses, if anybody intercepts this packet or this flow, they will actually

48
00:03:23,870 --> 00:03:25,490
be able to see the password.

49
00:03:26,000 --> 00:03:32,720
Now using Https because of the added security, this password is actually encrypted.

50
00:03:32,720 --> 00:03:37,910
So even if somebody intercepts the data, they will simply just see gibberish.

51
00:03:37,910 --> 00:03:41,480
They will not see the actual password in plain text.

52
00:03:41,900 --> 00:03:50,390
In order to encrypt the data in Https like so, we're going to have to create or install two keys on

53
00:03:50,390 --> 00:03:51,110
our server.

54
00:03:51,110 --> 00:03:56,870
So assuming we run Google or this is our server, we're going to have to create a private key and a

55
00:03:56,870 --> 00:03:57,800
public key.

56
00:03:57,830 --> 00:04:04,130
The private key as the name suggests, stays on the server and is never shared with anybody else.

57
00:04:04,130 --> 00:04:10,820
And the public key is shared with the user or the client or anybody that wants to load the website in

58
00:04:10,820 --> 00:04:17,030
order to establish a secure connection in which the data is securely encrypted.

59
00:04:17,720 --> 00:04:26,270
Now, this public key is actually included in a TLS certificate file, and usually the web browser requests

60
00:04:26,270 --> 00:04:30,590
this file in order to establish the Https connection.

61
00:04:30,590 --> 00:04:37,520
So the server gives the client a copy of this file, and then the user proceeds to creating a secure

62
00:04:37,520 --> 00:04:44,450
connection so that when the data is sent between the two, it will be encrypted using TLS, which is

63
00:04:44,450 --> 00:04:46,280
a very, very strong encryption.

64
00:04:46,280 --> 00:04:52,580
And therefore if anybody intercepts this data, they will not be able to read it because it's simply

65
00:04:52,580 --> 00:04:53,900
going to be gibberish.

66
00:04:53,900 --> 00:04:59,630
And the only person that can read this data is the server because it has the private key.

67
00:05:00,720 --> 00:05:04,110
So creating the private key is not very difficult.

68
00:05:04,110 --> 00:05:11,730
The main challenge in this is creating a TLS certificate, because the TLS certificate authorizes us

69
00:05:11,730 --> 00:05:16,530
and validates that we actually own google.com and we own Google's servers.

70
00:05:17,170 --> 00:05:24,430
Therefore, there is only a handful of entities that can generate these certificates for us.

71
00:05:24,880 --> 00:05:31,330
These entities are known as certificate authorities, and they usually charge money to do this and verify

72
00:05:31,330 --> 00:05:32,410
your ownership.

73
00:05:32,500 --> 00:05:40,210
Luckily, there is a non-profit organization called Letsencrypt that allows us to generate TLS certificates

74
00:05:40,210 --> 00:05:40,990
for free.

75
00:05:41,020 --> 00:05:48,070
The only thing they ask is we properly validate that we actually own this domain and own the server.

76
00:05:48,190 --> 00:05:53,020
And all of this is actually done using a very simple script called Certbot.

77
00:05:53,020 --> 00:05:59,830
And on top of all of that, Certbot will actually automatically install the TLS certificate on the Apache

78
00:05:59,830 --> 00:06:03,010
server so that everything is done easily.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:06,560
So Let's Encrypt is basically a certificate authority that will allow us to generate the TLS certificate

2
00:00:06,560 --> 00:00:07,220
for free.

3
00:00:07,220 --> 00:00:11,180
And to do that we're going to use a program that is called Certbot.

4
00:00:11,180 --> 00:00:17,030
And it will automatically generate the certificate for us and install it on Apache, literally with

5
00:00:17,030 --> 00:00:17,870
one command.

6
00:00:17,990 --> 00:00:23,870
So generally before Let's Encrypt existed, you would have had to go and purchase a TLS certificate

7
00:00:23,870 --> 00:00:28,460
from a website, pay for that, and then manually install it on your server.

8
00:00:28,460 --> 00:00:33,860
But thanks to Let's Encrypt, you can do all of that for free and it will automatically install it on

9
00:00:33,860 --> 00:00:34,550
your server.

10
00:00:34,970 --> 00:00:39,680
So first of all, you want to make sure that your domain is actually linked to your server.

11
00:00:39,680 --> 00:00:44,780
So as you can see if I go to Facebook login.co, it is taking me to the server that I control.

12
00:00:44,780 --> 00:00:46,010
This is very important.

13
00:00:46,010 --> 00:00:48,500
This whole thing will not work without this.

14
00:00:48,500 --> 00:00:53,240
And once you're at this stage, you want to go ahead and SSH into your server.

15
00:00:53,240 --> 00:00:54,830
And we covered how to do that before.

16
00:00:54,830 --> 00:00:56,660
So I'm not going to cover it right now.

17
00:00:56,660 --> 00:01:00,320
And we're going to elevate our privileges by doing sudo su.

18
00:01:00,320 --> 00:01:01,460
And you should know this by now.

19
00:01:01,460 --> 00:01:05,450
It gives us root privileges and it allows us to run root commands.

20
00:01:05,900 --> 00:01:09,170
Once you're in root we're going to update our libraries.

21
00:01:09,170 --> 00:01:13,010
So we're going to update the sources that we can download packages from.

22
00:01:13,010 --> 00:01:16,100
So we're doing this using the command apt update.

23
00:01:16,100 --> 00:01:23,900
And once this is done we're going to do apt to use the APT package manager to install a program that

24
00:01:23,900 --> 00:01:26,840
is called cert bot.

25
00:01:27,540 --> 00:01:30,720
We're going to hit enter, and I already have it installed.

26
00:01:30,720 --> 00:01:32,910
That's why it didn't install it for me.

27
00:01:32,910 --> 00:01:35,580
But in your case it's going to ask you do you want to install it.

28
00:01:35,580 --> 00:01:38,520
You're going to hit enter again and it'll install it for you.

29
00:01:39,160 --> 00:01:44,710
Once you have that installed, we also want to install another program that is needed to automatically

30
00:01:44,710 --> 00:01:46,120
install the certificate.

31
00:01:46,120 --> 00:01:49,150
So again we're going to use APT, the package manager.

32
00:01:49,150 --> 00:01:51,460
And we're going to say we want to install a package.

33
00:01:51,460 --> 00:01:56,890
And the name of this package is Python three certbot.

34
00:01:57,610 --> 00:01:58,450
Apache.

35
00:01:58,780 --> 00:02:00,250
We're going to hit enter.

36
00:02:00,250 --> 00:02:03,550
And again it's already installed for me as you can see.

37
00:02:03,730 --> 00:02:06,580
So in your case it'll ask you do you want to install this.

38
00:02:06,580 --> 00:02:08,920
You're going to hit enter and it will install it for you.

39
00:02:09,250 --> 00:02:14,920
Once you have the two packages installed, like I said, you can use Certbot to automatically create

40
00:02:14,920 --> 00:02:20,890
the TLS certificate for you and install it on your server with literally one command.

41
00:02:20,890 --> 00:02:25,480
And that command is Certbot, which is the name of the program.

42
00:02:25,480 --> 00:02:33,130
And we're telling it that we want to create a certificate for Apache because that's the server that

43
00:02:33,130 --> 00:02:33,790
we have.

44
00:02:34,210 --> 00:02:41,140
So Certbot is the name of the program that will create the TLS certificate and automatically install

45
00:02:41,140 --> 00:02:41,800
it for us.

46
00:02:41,800 --> 00:02:48,520
And we're telling it that we want you to install it on an Apache server by doing Dash dash Apache I'm

47
00:02:48,520 --> 00:02:49,480
going to hit enter.

48
00:02:50,150 --> 00:02:55,790
And it's going to ask you a number of questions that are needed in order to generate the TLS certificate.

49
00:02:55,790 --> 00:02:59,210
So you simply just have to answer the questions that it's asking you.

50
00:02:59,240 --> 00:03:04,670
You should also pay attention to the locations where it's going to store the data and the log.

51
00:03:04,670 --> 00:03:09,950
So if anything fails, you should read this log file and it will contain the reason why the process

52
00:03:09,950 --> 00:03:10,580
failed.

53
00:03:10,580 --> 00:03:16,520
But right now it's asking us for the domain names that we would like to create the certificate for.

54
00:03:16,520 --> 00:03:18,980
And the domain name I have it right here.

55
00:03:18,980 --> 00:03:20,900
It's Facebook login.co.

56
00:03:20,900 --> 00:03:25,070
So we're going to copy it and paste it here going to hit enter.

57
00:03:25,860 --> 00:03:26,850
Give it some time.

58
00:03:26,850 --> 00:03:33,900
So right now it's verifying that we actually own Facebook login and that it is linked to the server

59
00:03:33,900 --> 00:03:38,340
that we're initiating this command from, or that we are running this script from.

60
00:03:38,880 --> 00:03:46,410
So as you can see, if you go up and read the output, you can see that the certificate is saved in

61
00:03:46,410 --> 00:03:47,460
this location.

62
00:03:48,600 --> 00:03:51,570
And then the key is saved in this location.

63
00:03:52,050 --> 00:03:58,320
And it's also telling you that this certificate is only valid for three months from the time of creation,

64
00:03:58,320 --> 00:04:05,280
but it will automatically renew and create another one for you and install it once the certificate expires.

65
00:04:05,280 --> 00:04:07,500
So you really don't need to worry about this.

66
00:04:08,070 --> 00:04:15,570
So I'm going to copy these and put them in a text file because we're going to be using them in the next

67
00:04:15,570 --> 00:04:16,050
lecture.

68
00:04:16,050 --> 00:04:20,880
So it's important to remember or store the location of these certificates.

69
00:04:20,970 --> 00:04:23,640
And the next thing that we see in here.

70
00:04:23,640 --> 00:04:26,370
So first of all it created the certificates for us.

71
00:04:26,370 --> 00:04:29,610
And next it actually deployed the certificate.

72
00:04:29,610 --> 00:04:33,570
So like I said it will automatically install them on the server that we chose.

73
00:04:33,570 --> 00:04:34,770
And we chose Apache.

74
00:04:34,770 --> 00:04:40,050
So it automatically installed it for us in the Apache configuration file.

75
00:04:40,380 --> 00:04:46,200
And it then is just giving you a congratulations message that this website now supports Https.

76
00:04:46,200 --> 00:04:53,430
But if we go and try to load the website over Https, you'll notice that the website will fail and it

77
00:04:53,430 --> 00:04:54,300
will not load.

78
00:04:54,300 --> 00:05:02,970
And the reason for that, because this web server is running on port 80 by default, but port 443 is

79
00:05:02,970 --> 00:05:05,040
actually used for Https.

80
00:05:05,550 --> 00:05:09,840
Therefore, we're going to have to go to the control panel of our server.

81
00:05:09,840 --> 00:05:15,780
And I actually showed you how to allow ports in the security policy of our server before.

82
00:05:15,780 --> 00:05:18,270
But I'm still going to do it quickly here.

83
00:05:18,270 --> 00:05:19,530
Just a quick reminder.

84
00:05:19,530 --> 00:05:21,720
So you want to go to your control panel.

85
00:05:21,720 --> 00:05:23,040
You want to click on the instance.

86
00:05:23,040 --> 00:05:25,170
So we're inside the instance the Kali instance.

87
00:05:25,170 --> 00:05:28,620
As you can see we're going to go to the security settings.

88
00:05:28,620 --> 00:05:32,220
And we're going to select the security policy in here.

89
00:05:32,580 --> 00:05:37,710
And if you scroll down in here you can see the allowed ports right now.

90
00:05:37,710 --> 00:05:45,120
So previously I showed you how to allow port 3000 for beef, 444 for our interpreter server and 80 for

91
00:05:45,120 --> 00:05:46,110
our web server.

92
00:05:46,110 --> 00:05:51,660
But what we want to do, we want to add or edit the rules in order to allow another port.

93
00:05:51,660 --> 00:05:53,880
And we're going to click on add rule.

94
00:05:53,880 --> 00:05:57,930
And the port that we want to add is port 443.

95
00:05:59,370 --> 00:06:03,210
And we want to add this to all of the IPS.

96
00:06:03,210 --> 00:06:05,520
And we're going to save the rule.

97
00:06:06,720 --> 00:06:12,990
And now that this is saved, we can go back and try to load our server using Https.

98
00:06:14,810 --> 00:06:15,710
And perfect.

99
00:06:15,710 --> 00:06:20,060
As you can see, we have our website that looks identical to Facebook.

100
00:06:20,090 --> 00:06:21,770
We can see the lock icon.

101
00:06:21,770 --> 00:06:27,890
If you double click the URL, you're seeing the Https, and the domain name is pretty convincing as

102
00:06:27,890 --> 00:06:28,190
well.

103
00:06:28,190 --> 00:06:29,600
Facebook login.co.

104
00:06:29,600 --> 00:06:34,550
And as you know, if the user puts in the username and the password, it will be stored on file for

105
00:06:34,550 --> 00:06:35,060
me.

106
00:06:35,090 --> 00:06:41,120
Not only that, but if we go on Firefox, as you can see there is a red mark over the lock, meaning

107
00:06:41,120 --> 00:06:41,990
there is no lock.

108
00:06:41,990 --> 00:06:47,180
And if we click in here, you're getting this nasty warning saying that this connection is not secure.

109
00:06:47,210 --> 00:06:52,070
Now if we refresh this page it's actually going to load over Https.

110
00:06:52,850 --> 00:06:53,570
Again.

111
00:06:53,570 --> 00:06:54,920
You're getting the lock.

112
00:06:54,920 --> 00:06:57,110
You're seeing the Https in here.

113
00:06:57,110 --> 00:07:03,050
And if we click on the input boxes you're not going to get any warning which is pretty convincing.

114
00:07:03,050 --> 00:07:09,050
It's pretty identical to the actual Facebook website with the lock with the Https and without warning

115
00:07:09,050 --> 00:07:09,710
in here.

116
00:07:10,010 --> 00:07:14,990
So right now we basically have a legit website that's running over https.

117
00:07:14,990 --> 00:07:20,840
And this knowledge, the use of Let's Encrypt is actually very, very useful because you don't have

118
00:07:20,840 --> 00:07:23,270
to use it with malicious pages only.

119
00:07:23,270 --> 00:07:28,280
You can actually use it with any website that you run, and you're going to be able to enable Https

120
00:07:28,310 --> 00:07:31,670
on it, which will increase user trust and make it more secure.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Phishing - Bypassing 2  Multi Factor Authentication (2FA  MFA)

1
00:00:00,080 --> 00:00:05,750
Previously, we covered how to manually create our own phishing pages so that we can store the username

2
00:00:05,750 --> 00:00:08,510
and the password entered in them on the server.

3
00:00:08,540 --> 00:00:13,580
Now, in this lecture on the next few lectures, I'm going to show you how to do that using tools.

4
00:00:13,580 --> 00:00:18,680
And we're also going to take it one step further, and I'm going to show you how to bypass two factor

5
00:00:18,680 --> 00:00:19,730
authentication.

6
00:00:20,490 --> 00:00:24,510
So as you can see in here I'm loading my XZ xorg domain.

7
00:00:24,510 --> 00:00:28,710
So we said you can change this to whatever domain name you want to make it more believable.

8
00:00:28,710 --> 00:00:32,910
And as you can see we have the lock icon similar to what we saw before.

9
00:00:32,910 --> 00:00:41,640
And then if the user puts their username for example, let's say ZC security.org and put my password

10
00:00:41,640 --> 00:00:44,820
123123123 hit enter.

11
00:00:44,820 --> 00:00:46,500
It's going to give us an error.

12
00:00:46,500 --> 00:00:51,960
But if we go to our log you can see that I have the username and the password right here.

13
00:00:51,960 --> 00:00:55,560
So all of that is happening automatically using a tool.

14
00:00:55,560 --> 00:00:58,650
So I actually didn't have to manually create any of this.

15
00:00:58,650 --> 00:01:00,690
And I'm going to show you how to do that later.

16
00:01:01,440 --> 00:01:07,440
The really cool thing that this tool can do is allow us to bypass two factor authentication.

17
00:01:07,440 --> 00:01:11,880
So let me show you, I can go to the same domains that I saxhaug.

18
00:01:13,760 --> 00:01:17,480
As you can see, I'm getting redirected to the login of GitHub.

19
00:01:17,480 --> 00:01:21,140
So using the same tool I'm running a number of phishing pages.

20
00:01:21,140 --> 00:01:26,090
But the really cool thing is, like I said, it's going to allow me to bypass two factor authentication.

21
00:01:26,090 --> 00:01:29,480
So first of all, I'm going to log in with my username and password.

22
00:01:30,260 --> 00:01:33,170
And the tool is going to capture the username and the password.

23
00:01:33,170 --> 00:01:39,380
But as you can see, I've enabled two factor authentication in my GitHub account, which means that

24
00:01:39,380 --> 00:01:46,640
GitHub is going to send an SMS to my phone number, and I will have to input the code in that SMS in

25
00:01:46,640 --> 00:01:49,460
here in order to access my account.

26
00:01:49,460 --> 00:01:51,890
Now, a lot of websites do this, not just GitHub.

27
00:01:51,890 --> 00:01:57,920
So we're doing this as an example, but usually this is a really big issue when it comes to phishing

28
00:01:57,920 --> 00:01:58,280
pages.

29
00:01:58,280 --> 00:02:03,440
Or even if you manage to get the password of your target because the target website will use another

30
00:02:03,440 --> 00:02:07,040
method of authentication in order to authenticate the actual user.

31
00:02:07,040 --> 00:02:12,740
And that way, even if you have the password, somehow you're still not going to be able to log in because

32
00:02:12,740 --> 00:02:15,050
you don't have access to the target's phone.

33
00:02:15,500 --> 00:02:22,010
So anyway, GitHub sent me the code, which is 946202.

34
00:02:22,010 --> 00:02:23,390
I'm going to log in with it.

35
00:02:23,390 --> 00:02:26,150
So I'm pretending to be the victim right now, the target.

36
00:02:26,150 --> 00:02:29,210
And as you can see, I'm logged in to my GitHub account.

37
00:02:29,210 --> 00:02:37,460
But if we go to our console, you will see we have the username, we have the password and we have intercepted

38
00:02:37,460 --> 00:02:38,090
the token.

39
00:02:38,090 --> 00:02:43,940
So now if you go in and use the username and the password, you're not going to be able to log in because

40
00:02:43,940 --> 00:02:45,590
of the two factor authentication.

41
00:02:45,590 --> 00:02:47,180
And that's why we need the token.

42
00:02:47,180 --> 00:02:53,330
Because this is how GitHub is authenticating me right now and allowing me to access the account, because

43
00:02:53,330 --> 00:02:58,790
that's how it verified that I am the actual account holder using the two factor authentication.

44
00:02:59,540 --> 00:03:03,680
So using this tool I can just do sessions to see all of my sessions.

45
00:03:03,680 --> 00:03:09,680
And as you can see, I have the Facebook session in here and I can just do sessions three to get that

46
00:03:09,680 --> 00:03:10,370
session.

47
00:03:11,580 --> 00:03:17,610
So now we can log in to GitHub using this session on its own, without the need to use the username

48
00:03:17,610 --> 00:03:18,450
and the password.

49
00:03:18,450 --> 00:03:24,120
Because as you know, the username and the password are kind of useless because the user is using two

50
00:03:24,150 --> 00:03:25,350
factor authentication.

51
00:03:25,350 --> 00:03:29,970
And without the second factor of authentication, we're not going to be able to log in to the account

52
00:03:29,970 --> 00:03:31,440
even if we have the password.

53
00:03:31,440 --> 00:03:37,380
So instead, we managed to capture the session that allows the user to log in after they use the second

54
00:03:37,380 --> 00:03:39,570
factor or the second authentication.

55
00:03:39,570 --> 00:03:45,420
And all we're going to do is copy this and we're going to go to Firefox.

56
00:03:45,420 --> 00:03:48,180
As you can see I'm not logged in to GitHub right here.

57
00:03:48,180 --> 00:03:51,210
So if you refresh it I'm not logged into it.

58
00:03:51,210 --> 00:03:57,090
And what I'm going to do I'm going to go to this extension right here which basically allows me to import

59
00:03:57,090 --> 00:03:57,780
cookies.

60
00:03:57,780 --> 00:04:00,810
I'm going to click on import to import a new cookie.

61
00:04:00,810 --> 00:04:03,510
I'm going to put the whole session that I copied.

62
00:04:03,510 --> 00:04:06,390
I'm going to click on import that's created.

63
00:04:06,390 --> 00:04:09,630
And now we're going to refresh GitHub.

64
00:04:11,040 --> 00:04:11,940
And perfect.

65
00:04:11,940 --> 00:04:17,910
As you can see, I am logged in to the target's account without having to enter the username or the

66
00:04:17,910 --> 00:04:18,630
password.

67
00:04:18,660 --> 00:04:24,750
This way we manage to actually bypass two factor authentication, and at the same time we have the username

68
00:04:24,750 --> 00:04:25,500
and the password.

69
00:04:25,500 --> 00:04:30,240
So we can actually go to the account now and change the password, change the two factor authentication

70
00:04:30,240 --> 00:04:34,140
and basically gain full access and full control over that account.

71
00:04:34,820 --> 00:04:40,760
So the way this tool works, instead of the user directly accessing the target website, what we're

72
00:04:40,760 --> 00:04:45,140
doing right now is we're sending the target a link to our server.

73
00:04:45,140 --> 00:04:50,180
And on our server we have this tool running evil nginx or evil nginx.

74
00:04:50,180 --> 00:04:55,670
I'm not sure how you should pronounce it, but this tool is a reverse proxy and it will basically intercept

75
00:04:55,670 --> 00:04:59,960
the requests between the user and the actual target website.

76
00:04:59,960 --> 00:05:05,300
So previously when we were sending the user a fake website, we were basically just getting the username

77
00:05:05,300 --> 00:05:07,190
and the password and sitting here.

78
00:05:07,190 --> 00:05:13,070
But as you saw earlier, when the user sent us the right login information, they actually got logged

79
00:05:13,070 --> 00:05:13,970
in to the website.

80
00:05:13,970 --> 00:05:19,250
So basically whatever the user sends is actually going to be forwarded to the website.

81
00:05:19,610 --> 00:05:23,030
So what happens is the user is going to send this a username and a password.

82
00:05:23,030 --> 00:05:28,160
And this is a website that uses normal authentication without two factor authentication.

83
00:05:28,160 --> 00:05:31,370
We're just going to forward the username and the password to the website.

84
00:05:31,370 --> 00:05:35,540
And then the user is actually going to get access to their account on the website.

85
00:05:35,540 --> 00:05:39,830
And at the same time the tool is going to store the username and the password for us.

86
00:05:39,830 --> 00:05:41,210
So very, very good.

87
00:05:41,210 --> 00:05:42,770
The user is not suspicious.

88
00:05:42,770 --> 00:05:45,560
And we're going to get the username and the password.

89
00:05:45,860 --> 00:05:52,100
But if the user has enabled two factor authentication on their account, the website is going to send

90
00:05:52,100 --> 00:05:55,010
a two factor challenge to evil nginx.

91
00:05:55,010 --> 00:06:00,410
Because like I said, it's intercepting the flow between the user and the server and then evil nginx

92
00:06:00,410 --> 00:06:06,050
will not be able to solve this challenge because it requires the user to input a code sent to their

93
00:06:06,050 --> 00:06:08,780
phone number, or to authenticate using an app.

94
00:06:08,780 --> 00:06:14,270
Therefore, we're going to forward that challenge to the user and wait for them to actually solve the

95
00:06:14,270 --> 00:06:15,020
challenge.

96
00:06:15,020 --> 00:06:20,060
Once they solve the challenge, we're going to get it and we're going to forward it to the target website

97
00:06:20,060 --> 00:06:22,040
and if the solution is correct.

98
00:06:22,040 --> 00:06:27,740
So if the user inputted the right code or use the app properly in order to authenticate themselves,

99
00:06:27,740 --> 00:06:30,680
the target website is going to send a token.

100
00:06:30,680 --> 00:06:36,140
This is the token that will be used to authenticate the user, because the user, first of all, entered

101
00:06:36,140 --> 00:06:40,400
the right username and the password and solved the two factor challenge.

102
00:06:40,400 --> 00:06:45,770
Therefore, at this stage, we're going to forward the token to the user and the user will get access

103
00:06:45,770 --> 00:06:46,730
to the website.

104
00:06:46,730 --> 00:06:52,880
And at the same time, we're going to be able to reuse this token and access the website without the

105
00:06:52,880 --> 00:06:57,740
username and without the password, even though we're actually going to have them because the user sent

106
00:06:57,740 --> 00:06:59,570
them at an earlier stage.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,570
So now that we understand how evil nginx works, let me show you how to install it.

2
00:00:05,570 --> 00:00:11,570
And I'm actually going to be installing it on a fresh install of a Kali instance on the cloud on Amazon,

3
00:00:11,570 --> 00:00:17,210
because there is a few DNS settings that need to work correctly, and we're going to be generating new

4
00:00:17,240 --> 00:00:20,300
Https certificate for it using Letsencrypt.

5
00:00:20,300 --> 00:00:23,150
So it's nice to start with a fresh new environment.

6
00:00:24,010 --> 00:00:28,720
So the server that I have right now is the server right here.

7
00:00:28,720 --> 00:00:33,790
And I'm going to run it on the domain zaxcom instead of Zak's dot org.

8
00:00:33,820 --> 00:00:37,990
So I'm already at the settings page here for the domain that I want to use.

9
00:00:37,990 --> 00:00:40,180
And we're going to add an A record.

10
00:00:40,180 --> 00:00:43,540
And that a record is going to be for the W w w.

11
00:00:43,540 --> 00:00:47,110
And the answer is going to be the IP of my server.

12
00:00:47,470 --> 00:00:49,240
So we're going to add that.

13
00:00:50,130 --> 00:00:56,070
And we're also going to add an answer to the normal domain as well without the w WW.

14
00:00:56,070 --> 00:01:00,960
So that's straightforward enough for simply linking the domain name to the IP address.

15
00:01:02,000 --> 00:01:11,270
I also forgot to add two more records, so I need to add the NS1 dot Zacks.com and give it this IP so

16
00:01:11,270 --> 00:01:13,550
the same IP as our server.

17
00:01:13,550 --> 00:01:20,690
And we're also going to add an S2 dot Zacks.com and give it our server.

18
00:01:20,690 --> 00:01:26,600
And the reason why we added these two extra records, the NS1 and the NS2, because this tool comes

19
00:01:26,600 --> 00:01:35,240
with its own DNS server, and it also uses DNS in order to verify your ownership to the domain for Let's

20
00:01:35,240 --> 00:01:38,120
Encrypt in order to generate the TLS certificate.

21
00:01:38,120 --> 00:01:44,750
So these two records are sufficient enough if you're using Name.com to allow for that in other servers

22
00:01:44,750 --> 00:01:51,650
and on other domain providers, you might have to add what's called glue records and set them to point

23
00:01:51,650 --> 00:01:53,510
to the IP of your server.

24
00:01:53,510 --> 00:01:59,900
Set the NS1 and the NS2 dot your domain to point to the IP address of your server.

25
00:01:59,900 --> 00:02:03,860
Now, as you know, this can take a few minutes for the settings to propagate.

26
00:02:03,860 --> 00:02:10,760
So as we wait, we're going to go ahead and log in to our instance on the cloud and install evil nginx

27
00:02:10,760 --> 00:02:11,420
on it.

28
00:02:11,900 --> 00:02:16,310
So as you can see, I'm already logged in to my Kali instance on the cloud.

29
00:02:16,310 --> 00:02:20,330
And I'm going to elevate my privileges to root by doing sudo su.

30
00:02:20,330 --> 00:02:26,930
And then we're going to do apt update to update the list of sources that we can download packages from.

31
00:02:27,260 --> 00:02:33,320
And once that's over we're going to do apt install git make.

32
00:02:33,830 --> 00:02:34,670
And go.

33
00:02:34,700 --> 00:02:36,200
Lang go.

34
00:02:37,010 --> 00:02:39,230
So we've used this command a lot by now.

35
00:02:39,230 --> 00:02:41,060
APT is the package manager.

36
00:02:41,060 --> 00:02:47,690
We're using it to install these three packages git, make and Golang go because the tool is actually

37
00:02:47,690 --> 00:02:48,530
written in go.

38
00:02:48,530 --> 00:02:52,910
And we're going to need git and make in order to download and compile the tool.

39
00:02:53,300 --> 00:02:54,830
So we're going to hit enter.

40
00:02:54,830 --> 00:02:56,570
It's asking us do we really want to do this.

41
00:02:56,600 --> 00:02:58,250
We're going to say yes we do.

42
00:02:59,010 --> 00:03:02,640
And you want to give it its time to download and install all of these packages.

43
00:03:03,720 --> 00:03:06,210
It's asking us if it should restart services.

44
00:03:06,210 --> 00:03:07,080
We're going to say yes.

45
00:03:07,080 --> 00:03:08,430
Do that for us, please.

46
00:03:09,100 --> 00:03:15,190
And once this is installed, we're going to go to the opt directory using the CD command.

47
00:03:15,190 --> 00:03:19,300
And in here we're going to download and install evil nginx.

48
00:03:19,300 --> 00:03:22,960
So we're going to go to GitHub and get its link.

49
00:03:22,960 --> 00:03:26,560
We can just click in here and copy this.

50
00:03:26,560 --> 00:03:29,620
And we're just going to say git clone.

51
00:03:30,450 --> 00:03:31,260
The tool.

52
00:03:31,260 --> 00:03:33,300
So this will download the tool for us.

53
00:03:33,300 --> 00:03:37,230
If we list now we can see we have a new directory for the tool.

54
00:03:37,230 --> 00:03:42,930
And we're going to use the CD command to navigate inside this directory we're going to clear the screen

55
00:03:42,930 --> 00:03:46,110
and we're going to type make to install the tool.

56
00:03:46,830 --> 00:03:49,020
Now, as you can see, we get no errors.

57
00:03:49,020 --> 00:03:52,260
So that means that the program got executed successfully.

58
00:03:52,890 --> 00:03:59,280
So I'm going to clear the screen and we're going to download the phishing websites or login pages that

59
00:03:59,280 --> 00:04:00,540
this tool needs.

60
00:04:00,540 --> 00:04:04,380
You can download these phishing login page from this git repo.

61
00:04:04,410 --> 00:04:06,210
There is also this one right here.

62
00:04:06,210 --> 00:04:08,280
I'm going to include them both in the resources.

63
00:04:08,280 --> 00:04:10,320
And there is more if you look on GitHub.

64
00:04:10,320 --> 00:04:13,590
But this is the one that contains most of the basic websites.

65
00:04:13,590 --> 00:04:15,090
So I'm going to copy it.

66
00:04:15,090 --> 00:04:22,230
I'm going to go back to my terminal and I'm simply going to do git clone the URL of the repo to download

67
00:04:22,230 --> 00:04:23,940
all of these phishing websites.

68
00:04:24,240 --> 00:04:26,880
As you can see, everything is downloaded successfully.

69
00:04:26,880 --> 00:04:28,950
So I'm going to clear the screen again.

70
00:04:28,950 --> 00:04:36,270
And if I list and keep in mind that I'm inside opt Evil Jinx two, you'll see that we have two important

71
00:04:36,270 --> 00:04:37,080
directories.

72
00:04:37,080 --> 00:04:39,150
First of all is the build directory.

73
00:04:39,150 --> 00:04:42,330
This is where the actual program is contained.

74
00:04:42,420 --> 00:04:45,510
And second we have the fish list directory.

75
00:04:45,510 --> 00:04:46,530
This one right here.

76
00:04:46,530 --> 00:04:52,290
This is the phishing websites that we just downloaded that we're going to use with Evil Jinx.

77
00:04:52,650 --> 00:04:59,310
Therefore in order to run the program now that we are inside Opt Evil Jinx, which is the working directory

78
00:04:59,310 --> 00:05:04,560
of this program, we're simply going to call the program name inside the build directory.

79
00:05:04,560 --> 00:05:11,610
So we're going to type build followed by the program name which is Evil Jinx.

80
00:05:11,730 --> 00:05:18,240
And then we're going to do dash P to specify the location of the phishing websites that we want this

81
00:05:18,240 --> 00:05:19,290
program to use.

82
00:05:19,290 --> 00:05:23,220
And this is what we just downloaded in here in this directory.

83
00:05:23,220 --> 00:05:26,400
So we're simply going to specify the name of this directory.

84
00:05:26,400 --> 00:05:33,360
So you can simply copy paste it or just get the autocomplete to do it for you do EV and tab.

85
00:05:33,750 --> 00:05:40,350
So a very simple command we're calling the executable the actual program in here by doing build followed

86
00:05:40,350 --> 00:05:41,490
by the name of the program.

87
00:05:41,490 --> 00:05:47,250
Because this program is actually inside this build directory, we're using the dash p argument to specify

88
00:05:47,250 --> 00:05:49,440
the location of the phishing websites.

89
00:05:49,440 --> 00:05:51,870
We just downloaded them in the previous step.

90
00:05:51,870 --> 00:05:55,740
And all of these phishing websites or pages are included in this directory.

91
00:05:55,740 --> 00:05:58,710
Hence, we're putting the name of this directory in here.

92
00:05:59,370 --> 00:06:00,810
I'm going to hit enter.

93
00:06:01,260 --> 00:06:02,760
And you're going to get a bunch of warnings.

94
00:06:02,760 --> 00:06:04,050
But don't worry about them.

95
00:06:04,050 --> 00:06:07,440
They're actually not going to affect the execution of the program.

96
00:06:08,210 --> 00:06:10,640
But if we scroll up.

97
00:06:12,310 --> 00:06:15,460
The last two warnings in here are very important.

98
00:06:15,460 --> 00:06:21,730
So you can see the first one is telling us that the domain name is not set, and the second one is telling

99
00:06:21,730 --> 00:06:28,330
us that the IP is not set, and it's actually telling us how to configure the domain name and the IP

100
00:06:28,330 --> 00:06:28,960
address.

101
00:06:28,960 --> 00:06:33,400
We're going to use config domain name, followed by the domain name to set the domain name.

102
00:06:33,400 --> 00:06:38,920
And we're going to use config IP version four to set up our IP version four.

103
00:06:38,920 --> 00:06:40,420
So very simple.

104
00:06:40,420 --> 00:06:46,690
We're going to use the config command to set our domain name to Zacks.com.

105
00:06:47,310 --> 00:06:48,360
And that's perfect.

106
00:06:48,360 --> 00:06:50,400
As you can see, this is set.

107
00:06:50,400 --> 00:06:54,900
And we still have the second warning about the IP version four.

108
00:06:54,900 --> 00:07:01,560
So again we're going to use the config command to set the IP version four to my IP version four.

109
00:07:01,560 --> 00:07:04,920
So I can copy it from here and paste it.

110
00:07:05,610 --> 00:07:07,830
Hit enter and that's perfect.

111
00:07:07,830 --> 00:07:08,820
That's set up now.

112
00:07:08,820 --> 00:07:15,960
So if we run config now again just to see all of the configuration, you will see that my domain is

113
00:07:15,960 --> 00:07:17,310
set to this domain.

114
00:07:17,310 --> 00:07:24,390
And the external IP version four is set to this IP which is the IP of my cloud server.

115
00:07:24,390 --> 00:07:26,670
So now if we run fish let's.

116
00:07:27,380 --> 00:07:32,870
Which is the name that this tool uses for the phishing login pages or phishing websites, like I said,

117
00:07:32,870 --> 00:07:40,010
and hit enter, you're going to see a list of all of the pre-configured phishing pages that we can use

118
00:07:40,010 --> 00:07:45,140
in order to steal login information and bypass two factor authentication.

119
00:07:45,140 --> 00:07:47,870
And I'm going to show you how to do that in the next lecture.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:06,200
So these fish lists are pre-configured fishing websites that we can use in order to capture usernames

2
00:00:06,200 --> 00:00:09,320
and passwords and bypass two factor authentication.

3
00:00:09,620 --> 00:00:13,610
So before deploying a fish net, we're going to have to configure its hostname.

4
00:00:13,610 --> 00:00:15,620
So again you can do help.

5
00:00:16,270 --> 00:00:21,820
Facilites to see all of the options and all of the available commands for the fish slits, as you can

6
00:00:21,820 --> 00:00:22,210
see.

7
00:00:22,210 --> 00:00:27,250
So it's explaining to you how to list all of the fish slits, how to modify the hostname, which is

8
00:00:27,250 --> 00:00:28,510
what we need to do.

9
00:00:28,870 --> 00:00:33,220
It's showing you how to enable them, how to disable them, how to hide it and unhide it.

10
00:00:33,220 --> 00:00:38,980
This is very useful so that search engines don't flag you or flag your domain as a fishing domain.

11
00:00:38,980 --> 00:00:44,770
So what we want to do now, before we can even deploy it, before we can even enable it, we have to

12
00:00:44,770 --> 00:00:46,030
set its hostname.

13
00:00:46,030 --> 00:00:50,080
And as you can see you have to do figlet hostname.

14
00:00:51,420 --> 00:00:52,920
And select the fish lit.

15
00:00:52,920 --> 00:00:56,310
So the fish lit that we want to select is the GitHub one.

16
00:00:56,310 --> 00:00:58,560
So that means we want to start the GitHub page.

17
00:00:58,560 --> 00:01:00,450
So you can see it in here.

18
00:01:00,690 --> 00:01:03,120
And you can see it's actually disabled right now.

19
00:01:03,120 --> 00:01:05,100
So we're going to say GitHub.

20
00:01:06,060 --> 00:01:08,040
And we want to give it our host name.

21
00:01:08,040 --> 00:01:10,950
So it's set as hacks.com.

22
00:01:11,610 --> 00:01:17,550
So we're using the fish command to set the host name for the GitHub fish lit.

23
00:01:17,550 --> 00:01:22,800
And the host name is or the host name value is Zacks.com.

24
00:01:23,280 --> 00:01:24,690
I'm going to hit enter.

25
00:01:24,810 --> 00:01:26,010
And that is set.

26
00:01:26,010 --> 00:01:29,100
And the next thing that we want to do is enable this fish lit.

27
00:01:29,100 --> 00:01:30,960
So we're going to say fish let's.

28
00:01:31,700 --> 00:01:33,560
Enable GitHub.

29
00:01:34,130 --> 00:01:39,170
So again, we're using the Fishlegs command to enable a facility that is called GitHub.

30
00:01:39,200 --> 00:01:40,400
Very, very simple.

31
00:01:40,670 --> 00:01:41,840
I'm going to hit enter.

32
00:01:41,840 --> 00:01:46,760
And when you do that, as you can see, it's saying that there is no TLS certificate available.

33
00:01:46,760 --> 00:01:52,580
So it's going to create a new TLS certificate for us automatically using Letsencrypt.

34
00:01:52,580 --> 00:01:57,020
And then use it to deploy our new phishing page.

35
00:01:57,050 --> 00:02:02,750
Now as you can see, this failed and I wanted it to fail to show you this error message is telling us

36
00:02:02,750 --> 00:02:10,070
that there are subdomains such as the API ozarks.com and the GitHub ozarks.com.

37
00:02:10,100 --> 00:02:17,570
These subdomains do not have corresponding records, so depending on which facelet you choose to use.

38
00:02:17,570 --> 00:02:21,980
For example, if you use the Facebook wishlist, you will get different subdomains, so you'll always

39
00:02:21,980 --> 00:02:24,500
get that error the first time you try to run the tool.

40
00:02:24,500 --> 00:02:29,570
And then based on the subdomains that you have in here, you're going to have to go ahead to your domain

41
00:02:29,570 --> 00:02:32,750
management page again and add a records.

42
00:02:32,750 --> 00:02:36,110
So the first one that it complained about was the API.

43
00:02:36,650 --> 00:02:40,070
And you want to redirect it to the same IP as your server.

44
00:02:41,420 --> 00:02:42,830
And that's added there.

45
00:02:42,830 --> 00:02:46,040
And the next one that it complained about is GitHub.

46
00:02:46,460 --> 00:02:50,990
So again we're going to go back and add GitHub and give it the IP.

47
00:02:52,170 --> 00:02:53,130
Add record.

48
00:02:54,430 --> 00:03:00,220
And as usual, you might have to wait for this for maybe from one minute all the way up to a few hours.

49
00:03:00,460 --> 00:03:06,640
But I'm hoping that the DNS records updated in my server, so I'm actually just going to try it again.

50
00:03:06,640 --> 00:03:07,720
So we're just going to do fish.

51
00:03:07,720 --> 00:03:09,160
Let's enable GitHub.

52
00:03:09,160 --> 00:03:10,270
We're going to hit enter.

53
00:03:10,270 --> 00:03:13,960
And if the DNS records actually got updated this should work.

54
00:03:13,960 --> 00:03:16,180
So we will know now perfect.

55
00:03:16,180 --> 00:03:20,740
And as you can see we're getting a green message usually means stuff worked.

56
00:03:20,740 --> 00:03:25,360
And it's telling you that successfully set up SSL TLS certificates for my domains.

57
00:03:25,360 --> 00:03:32,410
So that basically means that the records updated and the tool now automatically created a TLS certificate,

58
00:03:32,410 --> 00:03:38,920
installed it on the web server, automatically created the web server, and automatically started a

59
00:03:38,920 --> 00:03:40,630
GitHub phishing clone.

60
00:03:40,930 --> 00:03:43,450
So now if I type fish, let's.

61
00:03:44,080 --> 00:03:45,910
To see all of my fish fillets.

62
00:03:45,910 --> 00:03:49,960
You can see the GitHub is saying enabled in here.

63
00:03:49,960 --> 00:03:53,830
So that means my GitHub fishing page is enabled.

64
00:03:53,920 --> 00:03:57,790
But even though it's enabled, it still doesn't have a URL.

65
00:03:57,790 --> 00:03:59,650
Nobody can actually access it.

66
00:03:59,650 --> 00:04:04,570
So in order to create a URL for it, we're going to have to create a lure.

67
00:04:04,570 --> 00:04:06,280
That's what the tool calls it.

68
00:04:06,280 --> 00:04:10,630
So if we do lures, you can see we have nothing in here.

69
00:04:10,630 --> 00:04:18,400
And in order to create a lure for the fish that we created, we're going to say lures create.

70
00:04:19,150 --> 00:04:19,960
GitHub.

71
00:04:21,610 --> 00:04:26,770
So are basically saying we want to create a lure or a link for GitHub.

72
00:04:26,770 --> 00:04:31,690
And now if we do lures, you can see we have a lure with ID zero.

73
00:04:31,690 --> 00:04:35,350
It's for the GitHub fish lit and the path is forward.

74
00:04:35,350 --> 00:04:38,560
Slash some random stuff and I don't like that.

75
00:04:38,560 --> 00:04:40,720
I want the path to be more believable.

76
00:04:40,720 --> 00:04:48,190
So if I just do lures zero, it's actually going to show me all of the parameters or all of the options

77
00:04:48,190 --> 00:04:55,000
that I can modify for this lure or for this URL, and I can change the path from this to anything I

78
00:04:55,000 --> 00:04:58,930
want so I can say lures edit zero.

79
00:04:58,930 --> 00:05:02,410
Remember I'm saying zero because that's the ID of this lure.

80
00:05:02,410 --> 00:05:07,270
And I'm going to say that I want to set the path to GitHub.

81
00:05:07,630 --> 00:05:10,720
So now I can actually get the URL for this lure.

82
00:05:10,720 --> 00:05:14,200
And to do that all I have to do is lures.

83
00:05:14,920 --> 00:05:18,610
Get URL for zero.

84
00:05:19,170 --> 00:05:24,630
And as you can see, this is going to be the phishing URL that you need to send to your targets.

85
00:05:24,630 --> 00:05:27,450
As you can see, it's using Https.

86
00:05:27,450 --> 00:05:29,430
It uses a real domain name.

87
00:05:29,430 --> 00:05:32,520
And like I said, you can make this domain name even more believable.

88
00:05:32,520 --> 00:05:37,590
For example, you can call it login page.co or login form.co or Facebook login.co.

89
00:05:37,620 --> 00:05:42,480
You've seen me do that previously and we have forward slash GitHub which is very very believable as

90
00:05:42,480 --> 00:05:42,750
well.

91
00:05:42,750 --> 00:05:47,550
So you want to make sure that the domain corresponds to whatever fish that you're using.

92
00:05:47,550 --> 00:05:50,310
So now that this is working let's go ahead and test it.

93
00:05:50,310 --> 00:05:56,280
So we're just going to open up a incognito page and let's load it.

94
00:05:56,670 --> 00:05:57,510
And perfect.

95
00:05:57,510 --> 00:06:04,320
As you can see we have our GitHub login page that will store the username and the password entered in

96
00:06:04,320 --> 00:06:04,860
here.

97
00:06:04,860 --> 00:06:11,280
And if the target account uses two factor authentication it will also capture the token.

98
00:06:11,280 --> 00:06:16,110
And then you can use the token to log in as I showed you at the start of this.

99
00:06:16,800 --> 00:06:22,020
So we're going to log in with the username I'm going to put my password I'm going to hit enter.

100
00:06:22,900 --> 00:06:26,920
So as you can see, we're prompted now with our two factor authentication.

101
00:06:26,920 --> 00:06:29,920
But before we do that, let me actually show you.

102
00:06:29,920 --> 00:06:33,040
As you can see, we already captured the username and the password.

103
00:06:33,040 --> 00:06:38,800
So in a case that two factor authentication is not used, you already have your username and the password.

104
00:06:38,800 --> 00:06:42,490
But in this case this is useless or it's not useful enough.

105
00:06:42,490 --> 00:06:44,710
You still need the code in order to log in.

106
00:06:44,710 --> 00:06:52,420
So as a user now I'm going to put the pin that I got on my phone which is 376689.

107
00:06:52,420 --> 00:06:56,350
It's going to verify and if it's correct it's going to log me in.

108
00:06:56,350 --> 00:06:58,060
As you can see I'm logged in.

109
00:06:58,060 --> 00:07:02,320
So at this stage the token is sent back to evil nginx.

110
00:07:02,320 --> 00:07:04,120
And the user also got logged in.

111
00:07:04,120 --> 00:07:06,850
As you can see in here I'm logged in to my account.

112
00:07:06,850 --> 00:07:13,180
But if we go to evil nginx, you can see it's telling you that the token intercepted.

113
00:07:13,180 --> 00:07:17,230
So now in order to see your tokens you can just do sessions.

114
00:07:17,850 --> 00:07:23,040
You can see that we have session ID, one is for the fish list called GitHub.

115
00:07:23,040 --> 00:07:24,270
The username is this.

116
00:07:24,270 --> 00:07:25,590
The password is this.

117
00:07:25,590 --> 00:07:29,400
It's giving you the IP and it's telling us that the token is captured.

118
00:07:29,550 --> 00:07:36,300
So all I have to do is again say sessions one to get the information in that session in the ID number

119
00:07:36,300 --> 00:07:36,960
one.

120
00:07:36,960 --> 00:07:42,990
So this is the cookie that includes the token that we can use to log in without the password.

121
00:07:42,990 --> 00:07:45,840
So all I have to do now is copy this.

122
00:07:46,350 --> 00:07:49,740
And as a hacker you're going to have to open up your own web browser.

123
00:07:49,740 --> 00:07:51,600
So now I'm going to go to Firefox.

124
00:07:51,840 --> 00:07:56,580
So if I go to GitHub comm you'll see I'm not logged in.

125
00:07:56,580 --> 00:07:57,930
I'm just trying to show you.

126
00:07:57,930 --> 00:08:00,000
As you can see I'm not logged in.

127
00:08:00,000 --> 00:08:03,900
And in order to log in I'm going to be using this cookie editor.

128
00:08:03,900 --> 00:08:05,250
So it's just a plugin.

129
00:08:05,250 --> 00:08:07,230
I'm going to share it with you in the resources.

130
00:08:07,230 --> 00:08:11,190
And it basically just allows me to import cookies into the browser.

131
00:08:11,370 --> 00:08:13,440
So I'm going to click on import.

132
00:08:13,440 --> 00:08:17,970
And I'm simply going to paste the token that I copied from evil nginx.

133
00:08:18,560 --> 00:08:20,030
I'm going to click on import.

134
00:08:20,030 --> 00:08:22,790
So that's imported and stored on my browser.

135
00:08:22,790 --> 00:08:29,330
And basically my browser right now has the exact same information or the exact same cookie that the

136
00:08:29,330 --> 00:08:32,720
target user browser has, and it's allowing him to log in.

137
00:08:33,140 --> 00:08:36,260
And that's why now if I refresh my browser.

138
00:08:37,770 --> 00:08:43,590
I will log in to the target account without using the username and without using the password.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Accessing Cloud Server Desktop

1
00:00:00,020 --> 00:00:00,500
Now.

2
00:00:00,500 --> 00:00:06,260
Evil jinx is a little bit limited because it does not work for all websites, and it actually doesn't

3
00:00:06,260 --> 00:00:11,570
work for some of the main websites like Google, like Facebook, and like Instagram and Twitter.

4
00:00:11,780 --> 00:00:15,170
Therefore, I'm actually showing you a better way of doing this.

5
00:00:15,170 --> 00:00:18,470
And this way we're actually not going to be using any hacking tools.

6
00:00:18,470 --> 00:00:20,630
We're actually just going to be using a few tricks.

7
00:00:20,630 --> 00:00:22,310
We're going to stitch them together.

8
00:00:22,310 --> 00:00:28,370
And as a result, we're going to be able to bypass two factor authentication on any website, regardless

9
00:00:28,370 --> 00:00:35,960
of how complicated that website is and regardless of how secure their login page is at the start, it's

10
00:00:35,960 --> 00:00:41,150
going to seem like we're doing nothing related to bypassing two factor authentication, but you'll see

11
00:00:41,150 --> 00:00:45,350
at the end how we're going to use that technique to bypass two factor authentication.

12
00:00:46,030 --> 00:00:53,470
Previously, we learned how to communicate with our cloud server using SSH, and as a result, we are

13
00:00:53,470 --> 00:00:59,380
able to execute system commands remotely on the target server using SSH.

14
00:00:59,680 --> 00:01:04,480
Now, even though this is the best and the quickest way of communicating with your target server, and

15
00:01:04,480 --> 00:01:09,940
you can pretty much do anything you want on it, there are other ways of communicating with your remote

16
00:01:09,940 --> 00:01:16,720
server, so you can even communicate with it and get a graphical user interface with a mouse cursor

17
00:01:16,720 --> 00:01:22,720
where you can actually use it and access it the same way you access your own computer using a service

18
00:01:22,720 --> 00:01:24,070
called VNC.

19
00:01:24,550 --> 00:01:32,200
So SSH allows us to remotely execute system commands on our server, and we can use VNC to actually

20
00:01:32,200 --> 00:01:39,610
access the desktop of a computer on the cloud with a cursor, and get a graphical user interface similar

21
00:01:39,610 --> 00:01:42,640
to the way that I communicate with my computer in here.

22
00:01:43,860 --> 00:01:50,400
Now communicating with the target server using SSH was very simple and did not require us to install

23
00:01:50,400 --> 00:01:57,000
any applications, because pretty much all servers come with SSH server pre-installed on them, and

24
00:01:57,000 --> 00:02:02,670
Linux and OS, X and Apple computers come with an SSH client pre-installed in them.

25
00:02:02,670 --> 00:02:07,710
And therefore we were able to just communicate with the target server without having to install any

26
00:02:07,710 --> 00:02:08,700
applications.

27
00:02:08,940 --> 00:02:14,460
On the other hand, if we want to communicate with our cloud server using VNC, we're going to have

28
00:02:14,460 --> 00:02:21,660
to first of all install a graphical user interface on that server because most cloud servers are designed

29
00:02:21,690 --> 00:02:23,220
to be used over SSH.

30
00:02:23,250 --> 00:02:26,010
Therefore, they do not have a graphical interface.

31
00:02:26,010 --> 00:02:28,470
They literally don't have a desktop environment.

32
00:02:28,470 --> 00:02:31,080
So we're going to have to install that first.

33
00:02:31,080 --> 00:02:38,250
Then we're going to have to install a VNC server that will basically expose this graphical interface

34
00:02:38,250 --> 00:02:39,690
to the internet.

35
00:02:39,690 --> 00:02:47,040
Then we're going to have to install a VNC client on our own computer to communicate with this VNC server,

36
00:02:47,040 --> 00:02:50,880
allowing us to access this graphical user interface remotely.

37
00:02:51,780 --> 00:02:57,720
So we have to install a graphical user interface and a VNC server on our server on the cloud to expose

38
00:02:57,720 --> 00:02:57,960
it.

39
00:02:57,960 --> 00:03:03,570
And then we're going to install a VNC client on our own computer so that we can communicate with the

40
00:03:03,570 --> 00:03:04,140
server.

41
00:03:04,140 --> 00:03:05,760
It's actually very, very easy.

42
00:03:05,760 --> 00:03:08,790
And now once I put it in practice, you're going to see how easy it is.

43
00:03:08,790 --> 00:03:14,190
And as a result, you're going to be able to access the desktop environment of your Kali machine on

44
00:03:14,190 --> 00:03:19,080
the cloud, and you're going to be able to interact with it using a normal graphical user interface

45
00:03:19,080 --> 00:03:24,240
and click using the mouse, and do whatever you want to do as if you're doing it on your own computer.

46
00:03:24,810 --> 00:03:27,270
And you can do this with any cloud server.

47
00:03:27,270 --> 00:03:32,040
It does not have to be Kali, but I'm just doing it for Kali because that's the one that we installed

48
00:03:32,040 --> 00:03:32,760
originally.

49
00:03:33,360 --> 00:03:38,310
So what I'm going to show you right now might be useful for many of you guys that prefer using a graphical

50
00:03:38,310 --> 00:03:41,310
user interface when interacting with their computer.

51
00:03:41,310 --> 00:03:48,420
And later on, I'm actually going to show you how to use this in order to steal usernames and passwords

52
00:03:48,420 --> 00:03:52,530
and create phishing login pages and bypass two factor authentication.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:05,930
So as mentioned earlier, we want to install a graphical user interface and a VNC server so that we

2
00:00:05,930 --> 00:00:09,830
can expose this graphical user interface to the internet.

3
00:00:10,430 --> 00:00:15,560
So let's go ahead to our installation on the cloud and start installing the needed software.

4
00:00:15,590 --> 00:00:18,320
Now I'm actually going to create a new instance.

5
00:00:18,620 --> 00:00:20,780
I'm just going to call this server Cali.

6
00:00:21,910 --> 00:00:24,490
Linux VNC.

7
00:00:25,530 --> 00:00:28,380
And as we've done before, we're going to browse for more.

8
00:00:28,380 --> 00:00:31,320
We're going to go to the marketplace.

9
00:00:32,100 --> 00:00:33,510
We're going to look for Carly.

10
00:00:33,510 --> 00:00:36,480
So I'm doing this very quick because I showed you how to do this before.

11
00:00:36,480 --> 00:00:39,330
Please revise that lecture if you don't remember how to do it.

12
00:00:39,690 --> 00:00:41,490
We're going to continue.

13
00:00:42,410 --> 00:00:43,550
And from here.

14
00:00:43,550 --> 00:00:49,280
Previously, we chose the free tier, the one with one gigabyte of memory and one CPU.

15
00:00:49,310 --> 00:00:53,930
What I'm going to show you right now will work for the free tier, but it's just going to be a little

16
00:00:53,930 --> 00:00:59,120
bit slow because VNC servers use more resources than usual.

17
00:00:59,390 --> 00:01:04,590
So if you want to get the most out of this, I would recommend going with four gigabytes or even eight

18
00:01:04,590 --> 00:01:05,120
gigabytes.

19
00:01:05,120 --> 00:01:08,240
This will be paid, so it really depends on you.

20
00:01:08,240 --> 00:01:11,030
You can try the free one if it didn't work well.

21
00:01:11,030 --> 00:01:15,470
If you thought that it's too slow, then you can upgrade the installation steps and everything that

22
00:01:15,470 --> 00:01:17,690
I'm going to show you will be the same anyway.

23
00:01:18,140 --> 00:01:23,600
So I'm going to go with this one and I'm going to select my key pair, which is the same that I've been

24
00:01:23,600 --> 00:01:24,500
using all the time.

25
00:01:24,500 --> 00:01:27,950
This is what we're going to use in order to connect over SSH.

26
00:01:27,950 --> 00:01:33,800
And I'm going to tick these two boxes to allow access to Https and Http ports.

27
00:01:33,800 --> 00:01:35,870
Port 80 and port 443.

28
00:01:35,870 --> 00:01:40,700
I showed you how to do all of this manually anyway, so I'm skipping over all of that and we're going

29
00:01:40,700 --> 00:01:42,260
to click on Launch Instance.

30
00:01:42,260 --> 00:01:45,980
And now AWS is going to create that machine for me on the cloud.

31
00:01:46,880 --> 00:01:52,880
Now that the machine is created, I'm going to go to my instances and I have the machine right here.

32
00:01:52,880 --> 00:01:55,100
I'm going to copy its IP.

33
00:01:55,790 --> 00:01:56,870
From here.

34
00:01:58,130 --> 00:02:03,770
And I'm going to go to my terminal and we're going to SSH into it the same way that we always do.

35
00:02:03,890 --> 00:02:08,030
SSH dash I give it the location of the key.

36
00:02:08,060 --> 00:02:11,900
The username is Carly at the IP that I just copied.

37
00:02:11,900 --> 00:02:14,750
I'm doing this quickly because I showed you how to do it before.

38
00:02:14,750 --> 00:02:16,820
It's asking us if we want to trust it.

39
00:02:16,820 --> 00:02:18,650
We're going to say yes, we do.

40
00:02:19,340 --> 00:02:20,120
And that's it.

41
00:02:20,120 --> 00:02:22,520
Now we're inside our Carly machine.

42
00:02:22,520 --> 00:02:27,650
So the first thing that we want to do is update the sources that we can download packages from.

43
00:02:27,650 --> 00:02:33,080
And as we know, we do this by doing sudo to run the command as root and the command is apt.

44
00:02:33,080 --> 00:02:38,810
Update apt is the package manager and update to tell it that we want to update the sources.

45
00:02:38,810 --> 00:02:45,230
I'm going to hit enter and as I always say, this only updates the sources that we can download applications

46
00:02:45,230 --> 00:02:45,770
from.

47
00:02:45,770 --> 00:02:49,340
It's actually not going to update any existing applications.

48
00:02:49,940 --> 00:02:54,920
And now that the sources are updated, we're going to go ahead and install the needed packages.

49
00:02:54,920 --> 00:03:01,250
So as mentioned earlier, we want to install a graphical user interface and a VNC server so that we

50
00:03:01,250 --> 00:03:05,150
can expose this graphical user interface to the internet.

51
00:03:05,480 --> 00:03:10,850
So to do that first of all we're going to run the command as root using sudo we're going to use apt

52
00:03:10,850 --> 00:03:12,380
which is the package manager.

53
00:03:12,380 --> 00:03:16,430
And we're going to say we want to install a graphical user interface.

54
00:03:16,430 --> 00:03:20,120
Now Linux has a number of graphical user interfaces.

55
00:03:20,120 --> 00:03:23,930
I'm going to install Xfce4 because it is lightweight.

56
00:03:23,930 --> 00:03:27,920
So it's not going to use much resources on the cloud server.

57
00:03:27,920 --> 00:03:31,370
And therefore I'll be able to communicate with it faster.

58
00:03:31,490 --> 00:03:38,810
So we're going to say we want to install Xfce4, and we want to install another package that has a lot

59
00:03:38,810 --> 00:03:41,390
of add ons for this graphical interface.

60
00:03:41,390 --> 00:03:46,460
This package is called Xfce4 goodies.

61
00:03:46,910 --> 00:03:51,020
And finally we also want to install a VNC server.

62
00:03:51,020 --> 00:03:54,080
Again, there is many VNC servers that you can install.

63
00:03:54,080 --> 00:03:59,480
The one that I'm going to use is called tight VNC server.

64
00:03:59,870 --> 00:04:02,780
So sudo to run the command as root.

65
00:04:02,780 --> 00:04:04,550
APT is the package manager.

66
00:04:04,550 --> 00:04:07,490
We want to install the following packages.

67
00:04:07,490 --> 00:04:12,950
The first package is Xfce4 which is a lightweight graphical user interface.

68
00:04:12,950 --> 00:04:18,530
We're installing another package that contains many components needed by this graphical interface.

69
00:04:18,530 --> 00:04:22,100
And lastly, we are installing our VPN server.

70
00:04:22,310 --> 00:04:26,720
I'm going to hit enter to let this go and hit enter again to install it.

71
00:04:27,230 --> 00:04:28,820
Now it's asking me for the language.

72
00:04:28,820 --> 00:04:30,080
I'm going to keep it at English.

73
00:04:30,080 --> 00:04:33,500
I'm going to hit enter and you want to give this installation some time.

74
00:04:33,500 --> 00:04:37,820
It will actually take a few minutes because it's downloading and installing our packages.

75
00:04:38,030 --> 00:04:38,720
Perfect.

76
00:04:38,720 --> 00:04:40,370
The installation is complete now.

77
00:04:40,370 --> 00:04:43,040
So right now our server looks like this.

78
00:04:43,040 --> 00:04:45,980
It's got a graphical user interface installed on it.

79
00:04:45,980 --> 00:04:48,740
So it actually has a desktop environment.

80
00:04:48,740 --> 00:04:50,930
And we installed the VNC server.

81
00:04:51,170 --> 00:04:57,320
So the VNC server will allow us to communicate with this graphical user interface with this desktop

82
00:04:57,320 --> 00:04:58,100
environment.

83
00:04:58,400 --> 00:05:06,290
So all we have to do right now is start this VNC server and then install a client on our current computer

84
00:05:06,290 --> 00:05:09,080
on my Mac so that I can communicate with it.

85
00:05:09,680 --> 00:05:12,080
So let's go ahead and start the VNC server.

86
00:05:12,080 --> 00:05:18,500
I'm going to clear the screen and we're going to say tight VNC server to start it.

87
00:05:18,500 --> 00:05:23,960
And I'm going to use dash geometry to specify the resolution.

88
00:05:23,960 --> 00:05:29,600
You can pick higher resolutions, but that will be slower to interact with because you're going to be

89
00:05:29,600 --> 00:05:31,730
transferring more data over the internet.

90
00:05:31,730 --> 00:05:38,990
So I'm going to use a smaller resolution so that I have a smoother experience with the desktop environment.

91
00:05:38,990 --> 00:05:44,330
So I'm going to set the geometry to one 280 x 720.

92
00:05:44,330 --> 00:05:46,250
So essentially 720p.

93
00:05:46,900 --> 00:05:51,730
I'm going to hit enter and it's going to ask me to set up a VNC password.

94
00:05:51,730 --> 00:05:56,650
Make sure you remember this because you will need this when you communicate with this VNC server.

95
00:05:56,650 --> 00:05:59,620
So I'm going to set my password to test test.

96
00:05:59,620 --> 00:06:03,610
And as you can see the password has not been displayed on the screen.

97
00:06:03,610 --> 00:06:05,740
This is just a security feature.

98
00:06:05,740 --> 00:06:10,090
So when you type you will not see the password but it's actually being registered.

99
00:06:10,090 --> 00:06:14,170
Once you hit enter it's going to ask you to input it again.

100
00:06:14,170 --> 00:06:14,980
Test.

101
00:06:14,980 --> 00:06:17,140
Test I'm going to hit enter.

102
00:06:17,140 --> 00:06:23,230
It's going to ask me if I want to set up a password for view only, so that you can only view the desktop

103
00:06:23,230 --> 00:06:25,510
environment, but not interact with it.

104
00:06:25,510 --> 00:06:29,980
I'm not interested in this, so I'm going to hit N and hit enter.

105
00:06:31,010 --> 00:06:31,940
And perfect.

106
00:06:31,970 --> 00:06:38,210
Now my desktop environment has started, as you can see in here, and I can actually go ahead and communicate

107
00:06:38,210 --> 00:06:38,810
with it.

108
00:06:38,810 --> 00:06:46,340
But before I do that, I actually need to go back to my instance and I need to allow the VNC port through

109
00:06:46,370 --> 00:06:47,930
my security policy.

110
00:06:47,930 --> 00:06:50,360
Remember, we do this every time we run a server.

111
00:06:50,360 --> 00:06:53,780
For example, when we run Apache we had to allow port 80.

112
00:06:53,870 --> 00:06:56,480
So I'm just going to go to the instance.

113
00:06:56,810 --> 00:06:58,730
I'm going to go to the security.

114
00:07:00,110 --> 00:07:02,630
I'm going to click on the security group.

115
00:07:02,780 --> 00:07:06,110
Again, I'm doing this quickly because I showed you how to do this before.

116
00:07:06,140 --> 00:07:08,810
We're going to click on Edit the inbound rules.

117
00:07:08,810 --> 00:07:10,970
We're going to add a new rule.

118
00:07:10,970 --> 00:07:12,530
This is going to be custom.

119
00:07:12,530 --> 00:07:14,720
And I'm going to put the VNC port.

120
00:07:14,720 --> 00:07:17,540
And that is 5901.

121
00:07:17,960 --> 00:07:20,360
We're going to put this for all IPS.

122
00:07:21,350 --> 00:07:23,420
And we're going to click on Save rule.

123
00:07:24,310 --> 00:07:29,620
So right now we installed the GUI, we installed the VNC server, we enabled the port.

124
00:07:29,620 --> 00:07:36,880
All we have to do is install a VNC client or my current computer so that I can communicate with this

125
00:07:36,880 --> 00:07:40,480
VNC server and access the graphical user interface.

126
00:07:41,550 --> 00:07:43,890
Now there are many VNC clients.

127
00:07:43,890 --> 00:07:47,640
I'm going to be using this client right here remote Repl.

128
00:07:47,640 --> 00:07:50,970
It's available for all operating systems.

129
00:07:50,970 --> 00:07:57,120
I've already downloaded and installed the Mac version, so all I have to do is just launch the program.

130
00:07:57,800 --> 00:08:04,670
I'm going to click on create a New Connection and I'm going to put the IP for my Cloud Kali machine

131
00:08:04,670 --> 00:08:06,560
so we can get that from here.

132
00:08:06,560 --> 00:08:11,330
It's 5490 126 96.

133
00:08:12,050 --> 00:08:13,670
We're going to put the port again.

134
00:08:13,670 --> 00:08:18,590
It's 5901 and the name and we're just going to call this Kali.

135
00:08:19,260 --> 00:08:20,550
I'm going to click on save.

136
00:08:20,550 --> 00:08:22,260
So I have it saved in here.

137
00:08:22,260 --> 00:08:27,000
And in order to connect to it I'm simply going to right click and click on connect.

138
00:08:28,990 --> 00:08:31,510
It's going to ask me for the password that we just set.

139
00:08:31,510 --> 00:08:32,710
I'm going to input it.

140
00:08:32,710 --> 00:08:35,530
Test, test I'm going to hit enter.

141
00:08:35,920 --> 00:08:40,840
And as you can see we managed to log in to our Cloud Kali machine.

142
00:08:40,840 --> 00:08:43,540
And I can communicate with it from here.

143
00:08:43,540 --> 00:08:48,190
This is exactly the same way that I would communicate with my own local machine.

144
00:08:48,190 --> 00:08:50,230
So I can open up the terminal.

145
00:08:50,230 --> 00:08:53,560
From here, I can go to my file manager.

146
00:08:53,560 --> 00:08:56,200
From here I can open up a web browser.

147
00:08:56,200 --> 00:09:02,050
I can edit files using a text editor, using a graphical text editor, so I can communicate with the

148
00:09:02,050 --> 00:09:06,160
target application using a normal graphical interface.

149
00:09:06,980 --> 00:09:13,400
Once done, you want to first of all, close the VNC client from here, and also you want to make sure

150
00:09:13,400 --> 00:09:16,100
you turn off the VNC server in here.

151
00:09:16,100 --> 00:09:20,300
And to do that we're going to use the same application Tightvnc server.

152
00:09:20,300 --> 00:09:23,360
But this time we're going to say we want to kill.

153
00:09:25,160 --> 00:09:28,640
The desktop that was created, which is Kylie one.

154
00:09:28,640 --> 00:09:31,250
So we're going to type Kylie one.

155
00:09:31,430 --> 00:09:34,490
I'm going to hit enter and that is killed right now.

156
00:09:34,490 --> 00:09:38,900
So nobody can communicate with my Kylie machine using VNC anymore.

157
00:09:38,900 --> 00:09:44,240
If I want to communicate with it again, I'm going to have to start the server like so and then go ahead

158
00:09:44,240 --> 00:09:46,280
and connect to it from my client.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: BitB - Browser In Browser Attack

1
00:00:00,290 --> 00:00:06,680
So far we know how to communicate with our Cloud Kali machine using VNC.

2
00:00:07,250 --> 00:00:13,940
As a result, we're able to access the graphical user interface installed on the Kali machine remotely.

3
00:00:14,630 --> 00:00:21,170
In this lecture, I want to show you how to use this exact setup in order to steal login information

4
00:00:21,170 --> 00:00:24,110
and bypass two factor authentication.

5
00:00:25,120 --> 00:00:29,020
To do this, we're not going to use a VNC client.

6
00:00:29,020 --> 00:00:33,070
Instead, we're going to use a program called no VNC.

7
00:00:33,670 --> 00:00:40,570
No VNC uses HTML and JavaScript in order to facilitate a VNC connection.

8
00:00:40,690 --> 00:00:48,790
Therefore, it simply gives us a URL that we can share with the target, and when they access this URL,

9
00:00:48,790 --> 00:00:57,250
they'll be able to communicate with my Kali machine with the graphical user interface using VNC through

10
00:00:57,250 --> 00:01:02,110
their web browser, so they will not need to install a VNC client.

11
00:01:02,470 --> 00:01:08,170
And then I'm going to load a login page on my own Kali installation on the cloud.

12
00:01:08,170 --> 00:01:09,820
Start the VNC server.

13
00:01:09,820 --> 00:01:17,620
So this login page will be displayed as soon as you connect to the VNC server, and then share the link

14
00:01:17,620 --> 00:01:20,950
that Novnc generates with the target.

15
00:01:21,670 --> 00:01:27,610
As a result, the target is actually going to be logging in to a real login page.

16
00:01:27,610 --> 00:01:30,490
Whether it's Google, Instagram, Facebook, it doesn't really matter.

17
00:01:30,490 --> 00:01:34,810
They're going to be login to the real Facebook page, for example.

18
00:01:34,810 --> 00:01:42,610
But once they log in, I can disconnect their connection and I will have their account on my own cloud

19
00:01:42,610 --> 00:01:45,580
computer, so I won't need to inject any cookies.

20
00:01:45,580 --> 00:01:47,530
I won't need to do anything fancy.

21
00:01:47,530 --> 00:01:53,050
I will simply have access to their account because they logged in through my own computer.

22
00:01:53,230 --> 00:01:58,900
Now we can also enhance this by installing a keylogger on this computer so that we can steal the username

23
00:01:58,900 --> 00:01:59,740
and the password.

24
00:02:00,070 --> 00:02:04,810
We can install a cookie manager as well so that we can dump the cookies once they log in.

25
00:02:04,810 --> 00:02:06,850
So the sky is the limit with this.

26
00:02:06,850 --> 00:02:12,280
But the main idea is we're actually letting them log in using our own cloud server.

27
00:02:12,280 --> 00:02:16,780
Once they log in, we disconnect them and then we have access to their account.

28
00:02:17,170 --> 00:02:20,470
So that is the idea of a browser in the middle attack.

29
00:02:20,860 --> 00:02:22,270
Let me show you a quick example.

30
00:02:22,270 --> 00:02:25,390
So this is very clear right here I have a URL.

31
00:02:25,390 --> 00:02:28,570
So this is a domain that I own which is Zacks.com.

32
00:02:29,020 --> 00:02:31,750
You can change this to any domain that you want, like I said.

33
00:02:31,750 --> 00:02:34,150
And you can pick something that is more believable.

34
00:02:34,750 --> 00:02:40,180
Assume when you send this link to the target, the target is going to go ahead and put their username.

35
00:02:40,180 --> 00:02:43,000
So I'm going to put my username hit enter.

36
00:02:43,960 --> 00:02:45,790
It's going to ask me for the password.

37
00:02:46,860 --> 00:02:50,190
And now we're going to go to the two factor part of this.

38
00:02:50,190 --> 00:02:52,740
So there's two factor enabled on this account.

39
00:02:52,740 --> 00:02:58,530
And it needs me to authenticate myself using another factor using another method.

40
00:02:58,530 --> 00:03:01,320
So it's going to send a text message to my phone number.

41
00:03:01,320 --> 00:03:04,140
I'm going to click on send so that it sends it.

42
00:03:04,260 --> 00:03:09,150
And I got the text message there I'm going to put the code hit enter.

43
00:03:11,390 --> 00:03:12,230
And perfect.

44
00:03:12,230 --> 00:03:14,090
Now I'm logged in to my account.

45
00:03:14,540 --> 00:03:19,640
So right now we're assuming that I am the target and I logged in to my account.

46
00:03:19,640 --> 00:03:22,610
So as an attacker you can go ahead in here.

47
00:03:22,610 --> 00:03:26,090
And all you have to do is control C to cut the connection.

48
00:03:26,420 --> 00:03:28,040
This is what the victim will see.

49
00:03:28,040 --> 00:03:29,600
They'll think something went wrong.

50
00:03:29,600 --> 00:03:30,770
But that is fine.

51
00:03:30,950 --> 00:03:35,960
As a hacker, if you want to go ahead and gain access to their account, you're going to have to go

52
00:03:35,960 --> 00:03:37,940
to a normal VNC client.

53
00:03:37,940 --> 00:03:43,220
And I already have my profile stored in here, so all I have to do is just connect to it.

54
00:03:44,410 --> 00:03:45,730
Put my password.

55
00:03:47,280 --> 00:03:48,090
And perfect.

56
00:03:48,120 --> 00:03:55,140
Now I have access to the target Gmail account or whatever account that you are trying to have access

57
00:03:55,140 --> 00:03:55,710
to.

58
00:03:56,420 --> 00:03:59,660
So that is the idea of a browser in the middle attack.

59
00:04:01,080 --> 00:04:03,900
So right now we already have a GUI installed.

60
00:04:03,900 --> 00:04:09,030
We already have a VNC server installed that's already covered, so please revise if you don't know how

61
00:04:09,030 --> 00:04:09,870
to do that.

62
00:04:09,870 --> 00:04:13,710
What I'm going to do is go ahead and install no VNC.

63
00:04:15,190 --> 00:04:18,850
So to do that, we're going to do sudo to run the command as root.

64
00:04:18,850 --> 00:04:25,120
We're going to use apt, which is our package manager, to install an application called Novnc.

65
00:04:25,240 --> 00:04:28,750
Very very simple I'm going to hit enter to install it.

66
00:04:29,530 --> 00:04:31,690
And perfect that is installed.

67
00:04:31,690 --> 00:04:36,430
I'm going to clear the screen and we're going to go ahead and start our VNC server.

68
00:04:36,430 --> 00:04:40,480
So we can do this using the command Tightvnc server.

69
00:04:42,190 --> 00:04:49,540
We're going to set the geometry and this time because we want the page to look as legit as possible.

70
00:04:49,570 --> 00:04:52,540
I'm actually going to run it in higher resolution than usual.

71
00:04:52,540 --> 00:04:58,930
So previously we run it in 1 to 80 by 720 because we wanted a smoother experience.

72
00:04:58,960 --> 00:05:03,190
Right now the main goal is to make the page look as legit as possible.

73
00:05:03,190 --> 00:05:08,020
Therefore, I'm going to run it at one 920 by 1080.

74
00:05:08,020 --> 00:05:09,700
So I'm running it at full HD.

75
00:05:09,910 --> 00:05:15,460
I'm also going to set the color depth to 30 so that you get more colors in the connection.

76
00:05:15,460 --> 00:05:18,880
Again, to make sure that the page looks as legit as possible.

77
00:05:19,650 --> 00:05:23,430
I'm going to hit enter to run the VNC server and perfect.

78
00:05:23,430 --> 00:05:30,660
As you can see, it's running on Kali one and the next step is to go ahead and use Novnc to create a

79
00:05:30,660 --> 00:05:36,900
link like this, so that we can share with our target so that they can use it to access our graphical

80
00:05:36,900 --> 00:05:39,090
user interface using a link.

81
00:05:39,540 --> 00:05:42,060
Now using Novnc is very, very easy.

82
00:05:42,060 --> 00:05:48,540
We're actually going to use the proxy that comes with Novnc which is stored in usr.

83
00:05:49,050 --> 00:05:50,250
Share.

84
00:05:50,950 --> 00:05:54,760
No VNC utils.

85
00:05:55,290 --> 00:05:58,230
And it's called no VNC proxy.

86
00:05:59,560 --> 00:06:06,520
So this is the program that we want to use and we want to tell it to listen on port 80.

87
00:06:06,520 --> 00:06:12,220
So as mentioned previously, if you run something on port 80 then you will be able to access it through

88
00:06:12,220 --> 00:06:15,010
the URL without having to specify the port.

89
00:06:15,010 --> 00:06:17,080
That's why we're running it on port 80.

90
00:06:17,590 --> 00:06:23,110
And we're going to tell it that my VNC server is running on my local host.

91
00:06:23,110 --> 00:06:31,330
So on my current computer, on this computer on the cloud, and it's running on port 5901.

92
00:06:31,990 --> 00:06:41,500
So basically Tightvnc right now the service that we already used is running on port 5901 on local host

93
00:06:42,040 --> 00:06:49,450
on the current computer, and we're using Novnc to proxy port 80 to this service.

94
00:06:49,810 --> 00:06:56,260
Now VNC will also give us a URL, and therefore we will be able to communicate with this VNC server

95
00:06:56,260 --> 00:06:57,640
using a link.

96
00:06:58,690 --> 00:07:00,670
So let me show you we're going to hit enter.

97
00:07:01,030 --> 00:07:05,020
And it's running right now as you can see on port 80.

98
00:07:05,020 --> 00:07:09,700
And it's giving you the URL and it's telling you to press control C to exit.

99
00:07:09,790 --> 00:07:14,260
Now unfortunately this URL doesn't work, but you can connect to it very easily.

100
00:07:14,260 --> 00:07:14,980
Anyway.

101
00:07:15,010 --> 00:07:23,170
All you need is the IP of our server followed by vnc dot HTML.

102
00:07:23,740 --> 00:07:24,880
I'm going to hit enter.

103
00:07:25,710 --> 00:07:28,950
And as you can see, we get a nice welcome screen for Novnc.

104
00:07:29,580 --> 00:07:33,720
If I click on connect it's going to ask me for the password.

105
00:07:33,720 --> 00:07:35,880
So we're going to put the password as test.

106
00:07:35,880 --> 00:07:36,510
Test.

107
00:07:37,150 --> 00:07:39,010
Send the credentials.

108
00:07:40,670 --> 00:07:41,810
And perfect.

109
00:07:41,810 --> 00:07:48,200
As you can see, we can now access the desktop environment, the graphical user interface of our cloud

110
00:07:48,200 --> 00:07:51,380
computer using a normal URL.

111
00:07:52,070 --> 00:07:56,810
Now I know we had to type the password, and I know it doesn't look very believable at the moment to

112
00:07:56,810 --> 00:07:57,710
use for phishing.

113
00:07:57,710 --> 00:08:01,010
But as you know, I like to build things step by step.

114
00:08:01,010 --> 00:08:07,430
And next I'm going to show you how to make this look identical to a normal login screen for any website

115
00:08:07,430 --> 00:08:08,270
that you want.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:04,940
The main problem now is once you connect to the server like so.

2
00:00:06,000 --> 00:00:08,400
You're getting a welcome screen first.

3
00:00:08,430 --> 00:00:11,670
You have to click and connect and then you have to put the password.

4
00:00:11,670 --> 00:00:13,470
That's not believable at all.

5
00:00:13,470 --> 00:00:18,150
So to get around this, all you have to do is put a question mark after this.

6
00:00:18,150 --> 00:00:25,320
And we're going to say auto connect is equal to true.

7
00:00:26,230 --> 00:00:28,840
And we're going to give it the password.

8
00:00:30,020 --> 00:00:30,980
Which is test.

9
00:00:31,010 --> 00:00:31,850
Test.

10
00:00:32,430 --> 00:00:38,460
So basically we're telling it that we want you to automatically connect by setting the auto connect

11
00:00:38,460 --> 00:00:39,840
parameter to true.

12
00:00:39,840 --> 00:00:43,110
And we're giving it the password which is test test.

13
00:00:43,380 --> 00:00:45,150
So let's hit enter.

14
00:00:46,690 --> 00:00:47,530
And perfect.

15
00:00:47,530 --> 00:00:54,010
Now, this link allows anybody to directly access the graphical user interface without having to put

16
00:00:54,010 --> 00:00:54,610
a password.

17
00:00:54,610 --> 00:00:58,120
So we're one step closer to achieving our goal.

18
00:00:59,150 --> 00:00:59,660
Now.

19
00:00:59,660 --> 00:01:05,360
Also, instead of using this file VNC, I'm going to use a lighter version of this file, which is called

20
00:01:05,360 --> 00:01:07,730
VNC light dot HTML.

21
00:01:07,730 --> 00:01:15,170
And I want this page to automatically resize to the correct size, because right now, as you can see,

22
00:01:15,170 --> 00:01:16,670
it's kind of zoomed in.

23
00:01:16,670 --> 00:01:19,100
So we're going to add another parameter.

24
00:01:20,070 --> 00:01:23,820
That is called scale, and we're going to set it to true.

25
00:01:23,820 --> 00:01:27,030
So it automatically resizes to the correct size.

26
00:01:27,210 --> 00:01:35,250
And I'm also going to set the quality to nine so that I get the best quality possible.

27
00:01:35,340 --> 00:01:37,290
So if I hit enter right now.

28
00:01:38,650 --> 00:01:45,610
As you can see, I get a desktop environment that is pretty much identical to a local installation of

29
00:01:45,610 --> 00:01:46,030
Kali.

30
00:01:46,060 --> 00:01:52,150
Now, this doesn't really matter if you're just using Kali, if you just want to get access to the desktop

31
00:01:52,150 --> 00:01:55,900
environment, but for what we're going to use it for in the future.

32
00:01:55,900 --> 00:02:02,620
To bypass two factor authentication, you want the login page to look as believable as possible to the

33
00:02:02,620 --> 00:02:03,490
target person.

34
00:02:03,490 --> 00:02:09,010
So we're going to be running a browser, and we want the graphics and the text in the browser to have

35
00:02:09,010 --> 00:02:13,840
really good quality so that it looks as believable as possible to the target.

36
00:02:14,440 --> 00:02:19,090
So the first thing that we want to do right now is to go ahead and install a web browser.

37
00:02:19,090 --> 00:02:21,610
And I'm going to go and install Firefox.

38
00:02:21,610 --> 00:02:23,440
So I'm going to launch my terminal.

39
00:02:23,440 --> 00:02:29,410
This is the terminal inside my cloud instance I can run commands from here similar to the way I run

40
00:02:29,410 --> 00:02:31,300
commands from my SSH.

41
00:02:31,510 --> 00:02:39,400
And as usual we do sudo apt update to update the sources of the programs that we can install.

42
00:02:39,400 --> 00:02:48,100
And now that the sources are updated, we can do sudo apt install Firefox ESR.

43
00:02:48,430 --> 00:02:56,020
So we're using apt to install a program called Firefox, and it's Firefox ESR because that is the name

44
00:02:56,020 --> 00:03:00,190
of the package in the package manager I'm going to hit enter to install it.

45
00:03:00,190 --> 00:03:02,740
We're going to say yes, install it for me please.

46
00:03:02,740 --> 00:03:03,670
And we're going to give it.

47
00:03:03,670 --> 00:03:06,940
It's time to download and install Firefox and perfect.

48
00:03:06,940 --> 00:03:08,230
Now Firefox is installed.

49
00:03:08,230 --> 00:03:11,230
So I can run it by simply type in Firefox.

50
00:03:14,360 --> 00:03:15,140
And great.

51
00:03:15,140 --> 00:03:15,770
As you can see.

52
00:03:15,770 --> 00:03:18,230
Now we have Firefox running in here.

53
00:03:18,380 --> 00:03:23,240
So to make this even better, we can simply just go to gmail.com.

54
00:03:24,700 --> 00:03:29,500
And as you can see, we have a normal login page for Gmail because this is actually the legit login

55
00:03:29,500 --> 00:03:30,550
page for Gmail.

56
00:03:30,550 --> 00:03:36,370
So simply the idea is now that we have the browser loaded in here, all you have to do is copy this

57
00:03:36,370 --> 00:03:40,330
link and social engineer your target to log in through this link.

58
00:03:40,330 --> 00:03:45,160
So if they go and load this link in their browser, for example in here.

59
00:03:47,290 --> 00:03:49,720
As you can see, they're going to get a login screen.

60
00:03:49,720 --> 00:03:56,200
Once they log in, you disconnect them from here and you will have full access to their account in here.

61
00:03:57,280 --> 00:03:59,830
Now, don't worry about the bar that you see in here.

62
00:03:59,860 --> 00:04:03,130
Don't worry about this and don't worry about the parameters.

63
00:04:03,130 --> 00:04:05,200
And don't worry about the IP in here.

64
00:04:05,230 --> 00:04:07,120
All of these things can be improved.

65
00:04:07,120 --> 00:04:12,610
But as you know, I like to dissect the problem into a number of small challenges or a number of small

66
00:04:12,610 --> 00:04:13,180
problems.

67
00:04:13,180 --> 00:04:19,660
Solve them one by one until we achieve the end goal, where we're going to be able to serve a target

68
00:04:19,660 --> 00:04:25,570
user, a login page that looks identical to the normal login page that they want to use.

69
00:04:25,570 --> 00:04:31,870
And also we'll be able to steal their username and password and bypass two factor authentication and

70
00:04:31,870 --> 00:04:33,730
gain access to their account.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,500 --> 00:00:05,300
Now the problem of the user goes ahead and puts their username and their password.

2
00:00:05,300 --> 00:00:09,800
You're going to gain access to their account, but you're not going to be able to see the password.

3
00:00:09,800 --> 00:00:17,510
That's why it's a really good idea to go ahead and install a keylogger on this browser, so that when

4
00:00:17,510 --> 00:00:20,750
they go ahead and put the password, you will be able to see it.

5
00:00:21,290 --> 00:00:26,630
Now I'm going to include in the resources of this lecture a link to a very good plugin that acts as

6
00:00:26,630 --> 00:00:28,190
a keylogger for Firefox.

7
00:00:28,190 --> 00:00:30,800
But we're going to go ahead and download it right now.

8
00:00:31,250 --> 00:00:33,080
So I'm just going to go to Google.

9
00:00:34,460 --> 00:00:37,760
And I'm going to look for Firefox keylogger.

10
00:00:40,360 --> 00:00:42,520
This is actually the one that I'm looking for.

11
00:00:42,520 --> 00:00:45,640
So I'm simply going to click on Add to Firefox.

12
00:00:46,930 --> 00:00:48,310
We're going to click on add.

13
00:00:48,790 --> 00:00:50,560
We're going to click okay.

14
00:00:50,800 --> 00:00:57,610
And basically right now this key logger is going to log every keystroke that you input on Firefox.

15
00:00:57,610 --> 00:01:06,220
And us as hackers will be able to see the captured keystrokes by clicking on Alt Shift and K or Alt

16
00:01:06,220 --> 00:01:07,180
Shift and O.

17
00:01:07,210 --> 00:01:09,430
So it's telling you here how to access it.

18
00:01:09,430 --> 00:01:16,090
So if you hold alt shift and K as you can see, I can see everything that was logged.

19
00:01:16,120 --> 00:01:19,420
Now nothing has been typed so obviously nothing has been logged.

20
00:01:20,170 --> 00:01:27,340
So now that we have that installed, the next thing that I want to install is a cookie manager so that

21
00:01:27,340 --> 00:01:30,160
I can save the cookies and then use them again.

22
00:01:30,160 --> 00:01:33,550
If I wanted to log in to the target account using the cookies.

23
00:01:33,580 --> 00:01:39,130
Now, I will never need to use this because remember, user is actually logging in into their account

24
00:01:39,130 --> 00:01:42,010
for me and all I'm going to do is disconnect their connection.

25
00:01:42,010 --> 00:01:44,560
So I'll automatically have their account with the cookies.

26
00:01:44,560 --> 00:01:46,660
The main thing that we want to get is the password.

27
00:01:46,660 --> 00:01:51,370
But in case you need that you can go ahead and install a cookie manager.

28
00:01:51,370 --> 00:01:54,370
So we're just going to look for cookie manager in here.

29
00:01:54,970 --> 00:01:56,140
First result is good.

30
00:01:56,140 --> 00:01:59,110
It's actually the same one that we used with Evil Jinx.

31
00:02:02,060 --> 00:02:02,690
And perfect.

32
00:02:02,690 --> 00:02:07,280
So now our browser is prepared and ready to be used as a browser in the middle.

33
00:02:07,280 --> 00:02:13,730
So first of all, it can log all the keystrokes entered whenever someone logs in to our login pages,

34
00:02:13,730 --> 00:02:19,550
and we're going to be able to use it to export the cookies so that we can use them to log in from any

35
00:02:19,550 --> 00:02:20,930
other browser we want.

36
00:02:21,710 --> 00:02:28,280
Now the problem is, if you look in here, you can see that the user is going to be able to see that

37
00:02:28,280 --> 00:02:30,800
there is a browser inside their browser.

38
00:02:30,800 --> 00:02:34,220
Hence the name of this attack is browser in the middle.

39
00:02:34,220 --> 00:02:39,380
So they'll be able to see that there's a browser inside the browser, and they'll also be able to see

40
00:02:39,380 --> 00:02:40,910
this status bar.

41
00:02:40,910 --> 00:02:43,070
They'll be able to see this application menu.

42
00:02:43,070 --> 00:02:46,070
And all of this obviously does not look very believable.

43
00:02:46,070 --> 00:02:50,060
So the goal now is to make this look as believable as possible.

44
00:02:50,450 --> 00:02:52,640
So we're going to quit Firefox.

45
00:02:53,030 --> 00:02:55,640
And I'm going to clear the screen in here.

46
00:02:55,640 --> 00:03:03,170
And instead of running it just like so by typing Firefox we're actually going to do dash dash kiosk.

47
00:03:03,170 --> 00:03:11,960
And that will basically run the Firefox browser in kiosk mode without any of the bars that you see around

48
00:03:11,960 --> 00:03:12,110
it.

49
00:03:12,110 --> 00:03:16,070
Without a window, you'll actually only see the website that we are requesting.

50
00:03:16,070 --> 00:03:19,040
And the website that we want is going to be Gmail.

51
00:03:19,040 --> 00:03:23,390
So it's going to be https gmail.com.

52
00:03:23,390 --> 00:03:26,030
Forward slash I'm going to hit enter.

53
00:03:27,610 --> 00:03:28,600
And perfect.

54
00:03:28,600 --> 00:03:34,240
As you can see right now, if we go back to our target, you can only see the website.

55
00:03:34,240 --> 00:03:40,240
You don't see the Firefox title bar, you don't see the URL bar, you don't see the bookmark bar.

56
00:03:40,240 --> 00:03:41,890
They only get the website.

57
00:03:41,890 --> 00:03:48,700
So again, if we click on sign in, you'll just see the sign in page without anything that will indicate

58
00:03:48,700 --> 00:03:50,560
that this is another browser.

59
00:03:50,890 --> 00:03:55,900
So right now the target will only see their browser and the content page.

60
00:03:56,600 --> 00:04:02,690
But this is still not perfect because if you look around, you will see that we have this bar right

61
00:04:02,690 --> 00:04:04,370
here, which is not believable.

62
00:04:04,370 --> 00:04:09,290
And you can see that we have in here this button that also is not believable.

63
00:04:09,290 --> 00:04:12,890
So they're going to be like, what is this thing that is saying connected to Cali?

64
00:04:13,400 --> 00:04:18,080
To improve this, we're going to have to manipulate the page that is being loaded in here.

65
00:04:18,470 --> 00:04:23,720
So we're going to go back to our terminal, and I'm actually going to do it from here because it's better.

66
00:04:23,720 --> 00:04:27,500
And I'm going to do control C to quit now VNC that's fine.

67
00:04:27,500 --> 00:04:31,550
I'm going to do sudo su because I want to elevate my privileges to root.

68
00:04:31,550 --> 00:04:35,150
I'm going to be modifying a file that I don't have permissions to modify.

69
00:04:35,150 --> 00:04:40,850
And then I'm going to do nano followed by the location of the file that I want to modify.

70
00:04:40,850 --> 00:04:48,050
And basically I want to modify this file right here VNC light dot HTML to remove this bar and this button

71
00:04:48,050 --> 00:04:48,680
from it.

72
00:04:49,880 --> 00:04:53,390
So I'm using Nano as the text editor to modify this file.

73
00:04:53,390 --> 00:05:05,030
And the path of this file is usr share novnc and it's called VNC underscore lite dot HTML.

74
00:05:05,570 --> 00:05:06,830
I'm going to hit enter.

75
00:05:06,830 --> 00:05:09,230
And as you can see we can see the file content.

76
00:05:09,260 --> 00:05:11,750
Now I know you might think that this is a bit scary.

77
00:05:11,750 --> 00:05:14,030
You don't know HTML and CSS.

78
00:05:14,030 --> 00:05:15,590
How are you going to modify this.

79
00:05:15,590 --> 00:05:18,020
But you're going to see that it is very, very simple.

80
00:05:18,020 --> 00:05:20,090
We're not really going to be styling anything.

81
00:05:20,090 --> 00:05:26,420
So if you scroll down you can see straight away we have something called title and the value is novnc.

82
00:05:27,640 --> 00:05:32,230
Now, if we go to the file in here, you can see that the title is now VNC.

83
00:05:32,620 --> 00:05:38,290
So basically modifying the title in here will modify the value displayed in here.

84
00:05:38,900 --> 00:05:43,160
Now we want to steal login information for Gmail and we're loading Gmail.

85
00:05:43,160 --> 00:05:46,070
Therefore we're going to change the title to Gmail.

86
00:05:46,460 --> 00:05:47,660
Very very simple.

87
00:05:48,650 --> 00:05:54,110
We're going to scroll down and you'll see something called style, and you can see the style of the

88
00:05:54,110 --> 00:05:56,750
body in here, which we don't need to modify.

89
00:05:56,750 --> 00:06:02,240
But if we keep scrolling down, you can see that we have the styling for the top bar.

90
00:06:02,270 --> 00:06:07,760
Now we can guess that the top bar is this bar, and we don't want that to be displayed.

91
00:06:08,060 --> 00:06:11,780
Therefore, we're going to go to the styles in here.

92
00:06:11,810 --> 00:06:13,820
I'm going to go to the end of the line.

93
00:06:13,970 --> 00:06:15,650
I'm going to add a new line.

94
00:06:15,650 --> 00:06:21,740
And in this new line I'm going to say I want the display option of this bar to be none.

95
00:06:21,740 --> 00:06:24,680
So basically I want to hide this bar.

96
00:06:25,040 --> 00:06:27,500
We can also see something called status bar.

97
00:06:27,500 --> 00:06:29,600
And I think this might be this.

98
00:06:29,600 --> 00:06:33,560
Or it might be a different status bar that displays the connection status.

99
00:06:33,590 --> 00:06:36,230
In any case, I don't want that to be displayed.

100
00:06:36,230 --> 00:06:39,020
And therefore again I'm going to add the same property.

101
00:06:39,020 --> 00:06:42,800
So I'm going to say I want to display none.

102
00:06:42,800 --> 00:06:45,500
Which basically means I don't want this to be displayed.

103
00:06:45,890 --> 00:06:53,480
You can see we have another option in here to set the style link of the send control and delete button.

104
00:06:53,480 --> 00:06:57,950
So again if we go here you can see that's the button that we want to hide.

105
00:06:57,950 --> 00:07:02,450
And we're going to add the same property that we've been adding before.

106
00:07:02,480 --> 00:07:04,910
Display none.

107
00:07:05,450 --> 00:07:09,170
Let's keep scrolling down and see if there is anything else we want to modify.

108
00:07:09,170 --> 00:07:11,210
But I think that's it for now.

109
00:07:11,210 --> 00:07:13,610
So I'm going to do control X to save.

110
00:07:13,610 --> 00:07:16,970
I'm going to press Y and I'm going to hit enter to override.

111
00:07:17,240 --> 00:07:20,090
And let's go ahead and run Novnc again.

112
00:07:20,090 --> 00:07:23,090
And that is it running for me now.

113
00:07:23,090 --> 00:07:26,570
So let's go and see what the page looks like.

114
00:07:26,570 --> 00:07:28,640
So we're going to refresh the page.

115
00:07:30,280 --> 00:07:31,270
And perfect.

116
00:07:31,270 --> 00:07:34,150
As you can see now, the page looks so much more believable.

117
00:07:34,150 --> 00:07:38,980
So this is the Gmail account loading in the Firefox in the cloud.

118
00:07:38,980 --> 00:07:42,190
So basically this is this page right here.

119
00:07:42,190 --> 00:07:47,230
And we're able to access it using a link as you can see in here.

120
00:07:47,530 --> 00:07:52,600
And you can see from here obviously the URL doesn't look believable but we will be talking about that

121
00:07:52,600 --> 00:07:53,500
in the future.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,290 --> 00:00:03,080
As you can see now, the page looks so much more believable.

2
00:00:03,080 --> 00:00:08,180
So this is the Gmail account loading in the Firefox in the cloud.

3
00:00:08,180 --> 00:00:10,910
But the problem is this link is not nice.

4
00:00:10,910 --> 00:00:15,560
As you can see, it's actually, first of all has an IP instead of a domain name.

5
00:00:15,560 --> 00:00:19,130
It has a file name and it's even exposing our password.

6
00:00:19,130 --> 00:00:23,960
So the person, if they're smart enough, they'll even know the password to our VNC server and they

7
00:00:23,960 --> 00:00:25,700
can go and log in and destroy it.

8
00:00:26,240 --> 00:00:27,740
So let's improve this.

9
00:00:27,740 --> 00:00:30,680
Let's go back control C to cancel.

10
00:00:30,680 --> 00:00:35,780
We're going to clear the screen and we're going to go back to the same light VNC file.

11
00:00:35,780 --> 00:00:39,110
So we're going to edit it using nano as we saw earlier.

12
00:00:39,230 --> 00:00:41,300
And I'm actually going to go down.

13
00:00:41,300 --> 00:00:45,200
And we can do control w to search through this file.

14
00:00:45,200 --> 00:00:48,620
And I want to see if the password is mentioned in this file.

15
00:00:48,620 --> 00:00:54,290
And if I can hard code it if I can include it in the code in this file so that we don't have to include

16
00:00:54,290 --> 00:00:55,130
it in here.

17
00:00:55,790 --> 00:01:00,740
So I'm going to do control W and I'm going to look for password.

18
00:01:00,740 --> 00:01:01,850
Can I hit enter.

19
00:01:01,940 --> 00:01:06,500
And as you can see this is the first instance where the password is being used.

20
00:01:06,530 --> 00:01:12,200
Now if you read the code in here, even if you're not a programmer, you can see this is just a prompt

21
00:01:12,200 --> 00:01:14,360
that will say that the password is required.

22
00:01:14,360 --> 00:01:18,050
So it's not really taken in the value of the password.

23
00:01:18,290 --> 00:01:22,100
So I'm going to do control W again to search for password again.

24
00:01:22,100 --> 00:01:25,700
And I'm going to hit enter to find the next occurrence of password.

25
00:01:25,700 --> 00:01:27,830
And it's obviously just the next one in here.

26
00:01:27,830 --> 00:01:31,250
So again control W and search.

27
00:01:32,680 --> 00:01:36,640
And this one is inside the comments, so we're not interested in it.

28
00:01:36,730 --> 00:01:39,370
Continue searching and perfect.

29
00:01:39,370 --> 00:01:45,610
As you can see in here, it seems like the password variable is being defined and it's been given a

30
00:01:45,610 --> 00:01:46,810
value of a function.

31
00:01:46,810 --> 00:01:49,690
So it's going to run this function and get the password from it.

32
00:01:49,690 --> 00:01:52,150
Now I don't want it to do any of that fancy stuff.

33
00:01:52,150 --> 00:01:54,970
All I wanted to do is to set the password to my password.

34
00:01:54,970 --> 00:02:00,370
So I'm going to remove all of this and I'm going to give it my password, which is test.

35
00:02:00,370 --> 00:02:01,180
Test.

36
00:02:02,400 --> 00:02:06,540
So now we're not going to need to include the password in the URL.

37
00:02:06,540 --> 00:02:09,090
We can simply just send the URL like so.

38
00:02:09,690 --> 00:02:15,210
Now the other thing that will also mean that we won't need to set the auto connect because it already

39
00:02:15,210 --> 00:02:18,330
has the password, so we don't need to tell it to auto connect.

40
00:02:18,330 --> 00:02:20,460
It's going to be able to connect by default.

41
00:02:20,460 --> 00:02:22,800
So we can remove that parameter as well.

42
00:02:22,860 --> 00:02:27,660
And the next parameter that I want to remove is the scale in here which is set to true.

43
00:02:27,840 --> 00:02:30,930
So let's go ahead and look for the scale.

44
00:02:30,930 --> 00:02:35,400
Now if you scroll down you should find it somewhere close to here as far as I remember.

45
00:02:35,400 --> 00:02:40,050
And as you can see in here we have the scale value set to false.

46
00:02:40,050 --> 00:02:42,300
And we actually want to set it to true.

47
00:02:42,300 --> 00:02:46,500
So again I'm going to remove this and I'm going to set it to true.

48
00:02:46,500 --> 00:02:49,650
And therefore as a result I'm not going to need the scale.

49
00:02:50,280 --> 00:02:54,750
And I'm actually going to remove the quality because right now it's actually going to load the quality

50
00:02:54,750 --> 00:02:56,970
to the highest if you have a git connection.

51
00:02:57,510 --> 00:03:00,150
So I'm going to do control X to store.

52
00:03:00,150 --> 00:03:00,960
Yes.

53
00:03:00,960 --> 00:03:02,940
Enter to overwrite the changes.

54
00:03:02,940 --> 00:03:06,750
And we're going to run our node VNC server again.

55
00:03:06,750 --> 00:03:08,010
And that is running.

56
00:03:08,010 --> 00:03:11,820
And let's go ahead and just request the page just like so.

57
00:03:13,860 --> 00:03:14,670
And perfect.

58
00:03:14,700 --> 00:03:20,730
Now, as you can see, we are getting the page loading again without the browser, so it looks like

59
00:03:20,730 --> 00:03:22,380
it's loading in my own browser.

60
00:03:22,380 --> 00:03:25,320
And now we're automatically connecting to the page.

61
00:03:25,320 --> 00:03:31,410
We don't have to specify the password in here, and we actually don't have any weird arguments in here

62
00:03:31,410 --> 00:03:33,900
that might make the target more suspicious.

63
00:03:34,230 --> 00:03:38,730
But we still have VNC Underscore Lite in here, which I don't like.

64
00:03:38,730 --> 00:03:41,100
Now, changing this is very, very easy.

65
00:03:41,100 --> 00:03:42,990
Again, Ctrl c just to quit it.

66
00:03:42,990 --> 00:03:44,490
We're going to clear the screen.

67
00:03:44,490 --> 00:03:54,120
And to fix this all we have to do is rename this file the VNC flight.html to index.html.

68
00:03:54,120 --> 00:04:00,270
As mentioned earlier, at the start of this course, the web browser by default looks for a file called

69
00:04:00,270 --> 00:04:02,430
index.html and loads it.

70
00:04:02,430 --> 00:04:10,080
So if I rename this file to index.html, I'll be able to access this file by simply requesting the IP

71
00:04:10,080 --> 00:04:11,070
of the server.

72
00:04:11,750 --> 00:04:17,870
So all I have to do right now is instead of using Nano to edit this file, I'm going to use the MV command

73
00:04:17,870 --> 00:04:19,310
to rename this file.

74
00:04:19,310 --> 00:04:25,130
So I'm saying I want to rename this file to the same file in the same path.

75
00:04:25,130 --> 00:04:27,650
But I want to call it index dot HTML.

76
00:04:28,400 --> 00:04:33,920
So I'm going to hit enter and that runs without issues, meaning that the command got executed successfully.

77
00:04:33,950 --> 00:04:38,300
We're going to run our node VNC server again.

78
00:04:38,300 --> 00:04:43,880
And let's go ahead and request the IP just like so and perfect.

79
00:04:43,910 --> 00:04:52,370
Now by simply requesting the IP, we are able to connect to our cloud computer through VNC without a

80
00:04:52,370 --> 00:04:59,540
client using the URL only, and we are able to see the login page for Google Load in inside Firefox,

81
00:04:59,540 --> 00:05:05,540
but you don't see anything that would alarm you or tell you that this is another browser loading in

82
00:05:05,540 --> 00:05:06,260
your browser.

83
00:05:06,260 --> 00:05:09,920
So this looks very, very realistic and very, very legit.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,170 --> 00:00:06,140
Now that we are able to load a login page that is perfect, that looks identical to the real login page,

2
00:00:06,140 --> 00:00:11,270
and there is no clues in it to indicate that this is loading inside another browser.

3
00:00:11,330 --> 00:00:15,650
We also removed all the scary parameters that get displayed in here.

4
00:00:15,680 --> 00:00:21,650
The only thing that I want to do is link this to a domain name, and have https enabled on it.

5
00:00:21,650 --> 00:00:24,800
As a result, we're going to be able to see the lock icon in here.

6
00:00:24,800 --> 00:00:30,260
And we're not going to see this not secure so that this will look very, very believable.

7
00:00:31,200 --> 00:00:35,730
Now, I covered how to do this previously, so that's why I'm actually just going to show you how to

8
00:00:35,730 --> 00:00:37,290
do it, but I'm not going to do it.

9
00:00:37,290 --> 00:00:40,590
So first of all you want to go to your domain name settings.

10
00:00:40,590 --> 00:00:42,210
You want to add an A record.

11
00:00:42,210 --> 00:00:43,890
And we explained how to do that.

12
00:00:43,890 --> 00:00:47,370
And you want to link the domain name to the IP of the instance.

13
00:00:47,370 --> 00:00:51,210
So the IP of the instance, as you can see in here is this.

14
00:00:51,210 --> 00:00:54,240
And I have that linked to my domain name.

15
00:00:54,720 --> 00:00:55,800
So that's good.

16
00:00:55,800 --> 00:01:01,410
The next thing that you want to do is to go ahead and enable Https on it.

17
00:01:01,410 --> 00:01:03,630
And we can do that using Certbot.

18
00:01:03,630 --> 00:01:09,600
So to do this you want to first of all install Certbot by doing apt install Certbot.

19
00:01:09,600 --> 00:01:12,720
And we covered that again in multiple lectures before.

20
00:01:12,720 --> 00:01:17,760
As you can see it's saying that it is already installed because I have installed it myself before.

21
00:01:18,030 --> 00:01:21,690
So the next thing you want to do is actually create a certificate.

22
00:01:21,690 --> 00:01:27,150
And you do this by doing Certbot we're going to say that we want cert only.

23
00:01:27,390 --> 00:01:33,900
We're going to use the dash D to specify the domain and in my case it's set as hacs.com.

24
00:01:34,170 --> 00:01:39,390
And we're going to tell it that we want you to do this using the standalone method, meaning that I

25
00:01:39,390 --> 00:01:42,510
want you to start your own server and do the authentication.

26
00:01:43,590 --> 00:01:45,510
Now I covered how to do this previously.

27
00:01:45,510 --> 00:01:48,990
We covered this command and how it works and why we need it.

28
00:01:48,990 --> 00:01:54,720
As a result of this command, you're going to get two certificates the private key and the full chain.

29
00:01:54,840 --> 00:02:01,980
So once you have that, this command will output the links to the full chain and to the private key.

30
00:02:01,980 --> 00:02:11,340
And once you have them, all you have to do is run your novnc with the dash dash cert option to specify

31
00:02:11,340 --> 00:02:19,470
the location of the certificate and the dash dash key option to specify the location of the private

32
00:02:19,470 --> 00:02:19,980
key.

33
00:02:19,980 --> 00:02:23,700
So I'm going to paste the path of my certificate in here.

34
00:02:25,790 --> 00:02:29,660
And I'm gonna paste the path of my key in here.

35
00:02:29,810 --> 00:02:31,670
So very, very simple.

36
00:02:31,670 --> 00:02:33,290
We're using the same command.

37
00:02:33,290 --> 00:02:39,770
We're just adding the dash dash cert and specifying the location of the cert that you get from the cert

38
00:02:39,770 --> 00:02:40,640
path command.

39
00:02:40,640 --> 00:02:46,430
And then we're doing dash dash key and specifying the location of the key again that you get from the

40
00:02:46,430 --> 00:02:47,600
cert part command.

41
00:02:47,600 --> 00:02:52,970
And I didn't actually execute the CERT part command because I've already generated these certificates

42
00:02:52,970 --> 00:02:57,980
to save you time, because I covered this previously, and I don't want to be doing the same thing over

43
00:02:57,980 --> 00:02:58,520
and over.

44
00:02:58,520 --> 00:03:04,220
So if you don't understand this, please go back and revise how to use cert bot to generate a certificate.

45
00:03:04,820 --> 00:03:15,020
We also have to change the IP in here from 80 to 443, because Https runs on port 443.

46
00:03:15,020 --> 00:03:19,700
And that's why instead of 80 for Http, we're using 443 now.

47
00:03:20,240 --> 00:03:21,740
So I'm going to hit enter.

48
00:03:23,210 --> 00:03:27,830
And we're going to go ahead and go to Https.

49
00:03:28,590 --> 00:03:31,710
Zacks.com and perfect.

50
00:03:31,710 --> 00:03:38,430
As you can see, the title already says Gmail in here, and we get a nice login page for Gmail that

51
00:03:38,430 --> 00:03:41,760
looks identical to a normal Gmail login page.

52
00:03:41,760 --> 00:03:47,400
There is nothing different in this page than the proper page, because it is actually the proper page

53
00:03:47,400 --> 00:03:49,620
loading inside another browser.

54
00:03:50,190 --> 00:03:55,500
Now, to make this attack more believable, you should change this name that attacks.

55
00:03:55,500 --> 00:03:58,170
Com to a name that is more believable.

56
00:03:58,170 --> 00:04:00,000
And we covered URL manipulation.

57
00:04:00,000 --> 00:04:04,110
Previously on how to add Gmail in there in the URL.

58
00:04:04,110 --> 00:04:09,330
And you can even pick a domain name that is easier to believe, like login form co.

59
00:04:09,360 --> 00:04:15,840
I actually own that domain, but you can be inventive with this to try to make it as believable as possible.

60
00:04:16,590 --> 00:04:19,950
So now that everything is working, this is the moment of truth.

61
00:04:19,950 --> 00:04:23,340
Let's go ahead and log in to a Gmail account and see how this works.

62
00:04:23,340 --> 00:04:29,880
So assume when you send this link to the target, the target is going to go ahead and put their username.

63
00:04:29,880 --> 00:04:36,480
So I'm going to put my username John Wick 70 at gmail.com.

64
00:04:38,310 --> 00:04:40,200
It's going to ask me for the password.

65
00:04:41,860 --> 00:04:45,190
And now we're going to go to the two factor part of this.

66
00:04:45,190 --> 00:04:47,740
So there's two factor enabled on this account.

67
00:04:47,740 --> 00:04:53,530
And it needs me to authenticate myself using another factor using another method.

68
00:04:53,530 --> 00:04:56,320
So it's going to send a text message to my phone number.

69
00:04:56,320 --> 00:04:59,140
I'm going to click on send so that it sends it.

70
00:04:59,260 --> 00:05:01,360
And I got the text message there.

71
00:05:01,360 --> 00:05:06,580
I'm going to put the code which is 855502.

72
00:05:06,610 --> 00:05:07,750
Hit enter.

73
00:05:10,370 --> 00:05:11,240
And perfect.

74
00:05:11,240 --> 00:05:16,430
Now I'm logged in to my account and as you can see, we get a security alert that somebody logged into

75
00:05:16,430 --> 00:05:16,850
the account.

76
00:05:16,850 --> 00:05:18,380
But that doesn't really matter.

77
00:05:18,380 --> 00:05:22,790
So right now we're assuming that I am the target, I am the victim.

78
00:05:22,790 --> 00:05:24,350
And I logged in to my account.

79
00:05:24,350 --> 00:05:27,320
So as an attacker you can go ahead in here.

80
00:05:27,320 --> 00:05:30,800
And all you have to do is control C to cut the connection.

81
00:05:31,070 --> 00:05:32,750
This is what the victim will see.

82
00:05:32,750 --> 00:05:34,280
They'll think something went wrong.

83
00:05:34,280 --> 00:05:35,480
But that is fine.

84
00:05:35,660 --> 00:05:40,670
As a hacker, if you want to go ahead and gain access to their account, you're going to have to go

85
00:05:40,670 --> 00:05:42,350
to a normal VNC client.

86
00:05:42,350 --> 00:05:47,900
So I covered how to install one previously, and I already have my profile stored in here.

87
00:05:47,900 --> 00:05:50,210
So all I have to do is just connect to it.

88
00:05:51,060 --> 00:05:52,410
Put my password.

89
00:05:53,680 --> 00:05:54,460
And perfect.

90
00:05:54,490 --> 00:06:01,210
Now I have access to the target Gmail account or whatever account that you are trying to have access

91
00:06:01,210 --> 00:06:01,720
to.

92
00:06:02,410 --> 00:06:05,740
Not only that, but I can also access my keylogger.

93
00:06:05,830 --> 00:06:13,840
So to access this you have to click on the alt in here and then click on shift and O from your keyboard.

94
00:06:13,870 --> 00:06:16,510
Now as you can see we have the key dumps in here.

95
00:06:16,510 --> 00:06:19,420
And if you scroll up you'll be able to find the password.

96
00:06:19,450 --> 00:06:23,770
Now I'm not scrolling up because I don't want to show my password, but you have all the keys that were

97
00:06:23,770 --> 00:06:24,100
pressed.

98
00:06:24,100 --> 00:06:28,930
You can even see the shifts and the controls and everything that the user has pressed.

99
00:06:29,080 --> 00:06:31,810
Now, obviously you can use any keylogger you want.

100
00:06:31,810 --> 00:06:36,340
You don't have to stick with this keylogger, but that just shows you how much freedom you have.

101
00:06:36,340 --> 00:06:41,200
You can install any plugins you want, you can install any software you want because this is actually

102
00:06:41,200 --> 00:06:47,080
your own computer, where you can prepare it any way or shape that you want, and then send it to the

103
00:06:47,080 --> 00:06:48,070
target user.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:04,460
Now, the next thing that I want to show you is how to gain access to a WhatsApp account with this.

2
00:00:04,460 --> 00:00:09,260
So the really cool thing about this method is, like I said, is the amount of freedom it gives you.

3
00:00:09,260 --> 00:00:18,740
So if we go to web.whatsapp.com, you'll see that you can access a WhatsApp account through a web browser

4
00:00:18,740 --> 00:00:21,380
by simply scanning this code right here.

5
00:00:21,380 --> 00:00:28,340
So if you have physical access to a phone, all you have to do is simply scan this QR code using that

6
00:00:28,340 --> 00:00:33,710
phone, and you'll be able to access all of the messages and even send messages through that WhatsApp

7
00:00:33,710 --> 00:00:34,430
account.

8
00:00:34,700 --> 00:00:41,960
So we can leverage this to our benefit, because we can simply go back to our computer, our hacker

9
00:00:41,960 --> 00:00:44,720
computer, and we're going to clear this.

10
00:00:44,990 --> 00:00:48,470
We're gonna run our no VNC server again.

11
00:00:50,240 --> 00:00:51,650
We're gonna connect to it.

12
00:00:54,350 --> 00:00:56,180
And let's quit this.

13
00:00:57,510 --> 00:01:01,470
And this time again we're going to run Firefox in kiosk mode.

14
00:01:01,470 --> 00:01:09,030
But instead of Gmail, we're going to say we want to load web.whatsapp.com.

15
00:01:10,020 --> 00:01:11,490
I'm going to hit enter.

16
00:01:13,620 --> 00:01:16,440
And we're going to get the same page that I just showed you.

17
00:01:16,470 --> 00:01:23,160
So now all you have to do is send this link to your target and tell the target that this is a new version

18
00:01:23,160 --> 00:01:23,850
of WhatsApp.

19
00:01:23,850 --> 00:01:28,230
Or maybe they don't even know that they can access WhatsApp through the web browser.

20
00:01:28,230 --> 00:01:33,420
So it can be like, oh, look at this cool new way of accessing WhatsApp using this website.

21
00:01:33,420 --> 00:01:38,880
So they come into this website, all they have to do is simply scan this code with their phone.

22
00:01:39,030 --> 00:01:40,950
So I'm going to do that real quick.

23
00:01:41,910 --> 00:01:47,400
And perfect now as a victim or a target, as you can see, you'll be, oh, this is really cool.

24
00:01:47,400 --> 00:01:52,290
I can use my WhatsApp from the web so you can let them use it for a while, even if you want to.

25
00:01:52,290 --> 00:01:58,620
And then once you're happy, you can go ahead control C in here to disconnect them so they'll be disconnected

26
00:01:58,620 --> 00:01:59,220
in here.

27
00:01:59,220 --> 00:02:02,580
But you can log in from your client as I showed you earlier.

28
00:02:02,580 --> 00:02:04,770
So this is using remote Repl.

29
00:02:04,770 --> 00:02:06,780
This is not using Novnc.

30
00:02:06,780 --> 00:02:10,470
And as you can see now I have access to their WhatsApp account.

31
00:02:10,470 --> 00:02:15,480
I can read all their messages, I can send any message I want and I have full control over it.

32
00:02:16,170 --> 00:02:19,830
So this is just another example of how powerful this method is.

33
00:02:19,830 --> 00:02:25,110
If you can load something in the browser, you're going to be able to social engineer your target into

34
00:02:25,110 --> 00:02:29,700
login into it, or accessing it by simply giving them a URL.

35
00:02:29,700 --> 00:02:33,570
This is so generic and can be used in so many scenarios.

36
00:02:33,570 --> 00:02:39,930
And that's why these browser in the middle or browser in browser attacks are very, very dangerous and

37
00:02:39,930 --> 00:02:46,170
very hard to protect against because you're actually giving the target a legit URL, you're giving them

38
00:02:46,170 --> 00:02:47,490
a legit website.

39
00:02:47,490 --> 00:02:54,450
For example, in the case of evil jinx or reverse proxies, the website owner can implement security

40
00:02:54,450 --> 00:02:56,400
features to prevent it from working.

41
00:02:56,400 --> 00:03:02,100
But when you're simply giving them the actual website to log in to, there is nothing that the website

42
00:03:02,100 --> 00:03:08,520
owner can implement to stop you from doing that because the user is actually logging in to a legit website.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Mobile BitB - Mobile Friendly Phishing & 2FA Bypass

1
00:00:00,200 --> 00:00:06,620
So previously we covered how to run a browser in browser attack, and as a result, we're able to load

2
00:00:06,620 --> 00:00:13,070
a browser inside a browser so we can give a link such as this link right here to the target.

3
00:00:13,070 --> 00:00:19,070
The link uses Https and runs on a normal domain name, and as a result, they're going to see a login

4
00:00:19,070 --> 00:00:25,430
page that if they log in, they'll actually be logging in to a browser that we fully control, and therefore

5
00:00:25,430 --> 00:00:28,940
we will be able to gain full access to their account.

6
00:00:29,800 --> 00:00:36,670
I previously mentioned that the main advantage of this attack is that we fully control this browser.

7
00:00:36,670 --> 00:00:38,830
That's why we can tailor it any way we want.

8
00:00:38,830 --> 00:00:45,400
We can install a keylogger, we can modify the pages, and we saw how we can hide all of this and basically

9
00:00:45,400 --> 00:00:47,500
just have the browser running directly.

10
00:00:47,830 --> 00:00:50,470
That looks like an exact login page.

11
00:00:50,470 --> 00:00:56,320
Now, what I want to cover from now onwards is how to get this attack to work on a mobile phone.

12
00:00:56,320 --> 00:01:03,760
So if my target user loads the link this link right here on a mobile phone, I want them to get a login

13
00:01:03,760 --> 00:01:10,450
page that is mobile friendly without seeing the mouse cursor, and I want them when they click in an

14
00:01:10,450 --> 00:01:15,820
input box to get a keyboard so that they can type in the username and the password.

15
00:01:15,820 --> 00:01:21,190
Remember, on mobile phones there is no keyboards, so automatically we need a keyboard to pop up so

16
00:01:21,190 --> 00:01:26,080
that the user can put their information so that they can log in without getting suspicious.

17
00:01:26,080 --> 00:01:32,110
And as a result, I'll be able again to bypass multi-factor authentication or two factor authentication

18
00:01:32,110 --> 00:01:34,780
and also gain access to their account.

19
00:01:35,460 --> 00:01:37,830
So there's going to be a number of steps to this.

20
00:01:37,830 --> 00:01:42,180
The first one is to actually get them to get the mobile friendly website.

21
00:01:42,180 --> 00:01:47,280
Because remember right here we are loading this inside a Linux computer.

22
00:01:47,280 --> 00:01:52,080
So right here I have a Linux computer with Firefox running in the background.

23
00:01:52,080 --> 00:01:58,950
And as a result, when we go to a login page, we're getting the desktop version of that login page.

24
00:01:58,950 --> 00:02:02,490
So the mobile version of Google doesn't look like this.

25
00:02:02,490 --> 00:02:05,430
Same goes for Instagram for example.

26
00:02:05,430 --> 00:02:06,750
And it's actually more noticeable.

27
00:02:06,750 --> 00:02:13,410
So if we go to instagram.com you're going to see that I'm going to get the desktop version of Instagram.

28
00:02:13,410 --> 00:02:16,530
The mobile version simply shows the login page only.

29
00:02:16,530 --> 00:02:23,070
And therefore if we give this link right now to a target mobile, it's going to work, but it's going

30
00:02:23,070 --> 00:02:26,340
to look more suspicious because they're getting the mobile version.

31
00:02:26,700 --> 00:02:29,880
Fixing this is very easy because of what I said earlier.

32
00:02:29,880 --> 00:02:35,730
I fully control this computer and I can modify it any way I want to make it suit the target.

33
00:02:35,730 --> 00:02:43,920
So what we need to understand is how is Instagram and Google know that right now I am accessing their

34
00:02:43,920 --> 00:02:47,340
website from a computer and not from a mobile phone.

35
00:02:47,910 --> 00:02:51,570
They know this by relying on the user agent.

36
00:02:51,660 --> 00:02:57,930
So when you try to access a website and in our example, Google or Instagram, your web browser sends

37
00:02:57,930 --> 00:02:59,040
a lot of data.

38
00:02:59,190 --> 00:03:02,760
Part of this data is what we refer to as the user agent.

39
00:03:02,790 --> 00:03:04,290
It looks like this.

40
00:03:04,290 --> 00:03:11,250
And it basically specifies the operating system, the rendering engine and the web browser.

41
00:03:11,250 --> 00:03:18,810
So this user agent right here is an example of a browser that is running on Windows 10 with Apple WebKit

42
00:03:18,810 --> 00:03:20,130
rendering engine.

43
00:03:20,130 --> 00:03:23,040
And that is running Chrome web browser.

44
00:03:23,430 --> 00:03:25,620
So this is what we mean by the user agent.

45
00:03:25,620 --> 00:03:31,470
And every time you access a website, your browser sends this data to that website.

46
00:03:31,470 --> 00:03:35,820
And then the website will parse this data, will read this data.

47
00:03:35,820 --> 00:03:40,950
And based on this data, it will serve you a certain version of that website.

48
00:03:40,950 --> 00:03:46,920
So if you tell this website that I am running an iPhone with Firefox, it's going to send you a version

49
00:03:46,920 --> 00:03:49,920
of that website that is friendly to that phone.

50
00:03:49,920 --> 00:03:55,290
That's why sometimes when you access a website from different devices, you'll see that you get different

51
00:03:55,290 --> 00:03:57,030
versions of these websites.

52
00:03:57,920 --> 00:04:04,430
So all we have to do right now is modify this user agent to say that I am running an iPhone because

53
00:04:04,430 --> 00:04:09,950
I'm going to be targeting an iPhone, and I'm going to tell it that this is a mobile running the Safari

54
00:04:09,950 --> 00:04:11,120
web browser.

55
00:04:11,830 --> 00:04:13,840
Now, how do we get all of this text?

56
00:04:13,840 --> 00:04:16,570
Because as you can see, this text is not very simple.

57
00:04:16,570 --> 00:04:20,860
There is a lot more data to it, and I don't expect you to simply remember all of this.

58
00:04:20,860 --> 00:04:23,500
But all of this data is publicly available.

59
00:04:23,500 --> 00:04:27,070
So all we have to do is basically go to Google.

60
00:04:27,670 --> 00:04:30,700
And look for user agent list.

61
00:04:31,730 --> 00:04:35,930
You get a lot of websites that have a lot of examples of user agents.

62
00:04:35,930 --> 00:04:38,240
The first one is actually very useful.

63
00:04:38,810 --> 00:04:44,720
I'm going to scroll down and I'm going to find the device that I want to mimic.

64
00:04:45,170 --> 00:04:48,020
So I'm like I said, I'm going to be targeting an iPhone.

65
00:04:48,020 --> 00:04:55,550
So I'm going to click on iPhone and I'm going to copy the user agent for an iPhone 13 Pro Max, because

66
00:04:55,550 --> 00:04:56,810
that has a really big screen.

67
00:04:56,810 --> 00:04:58,070
So it should be nice.

68
00:04:58,070 --> 00:04:59,720
So we're going to copy this.

69
00:05:00,520 --> 00:05:08,800
And then we're going to go and modify the Firefox settings so that instead of sending a user agent that

70
00:05:08,800 --> 00:05:15,700
basically says that I am running Firefox, I'm going to be sending a user agent that says I am running

71
00:05:15,700 --> 00:05:16,660
an iPhone.

72
00:05:16,960 --> 00:05:23,290
So to access the advanced configurations of Firefox, we're going to go to about colon config.

73
00:05:24,100 --> 00:05:28,810
I'm going to hit enter, and it's going to give you a warning that some of these settings might fully

74
00:05:28,810 --> 00:05:30,130
break the browser.

75
00:05:30,130 --> 00:05:31,840
We're going to say yes, that's fine.

76
00:05:31,840 --> 00:05:37,240
We understand what we're doing and we're going to add a new entry to the settings.

77
00:05:37,240 --> 00:05:43,660
The entry name is general dot user agent dot override.

78
00:05:43,840 --> 00:05:48,700
So we're basically saying we want to override the existing user agent.

79
00:05:48,700 --> 00:05:52,660
Now it's going to give you options of the value that you want to input in here.

80
00:05:52,660 --> 00:05:55,330
So boolean means it's a true or false value.

81
00:05:55,330 --> 00:05:56,500
Number is a number.

82
00:05:56,500 --> 00:05:59,770
And string basically means an array of characters.

83
00:05:59,770 --> 00:06:03,880
So I'm going to say string I want to put characters which is basically just text.

84
00:06:03,880 --> 00:06:07,570
And I'm going to click on the plus to get a text box to put this value.

85
00:06:07,570 --> 00:06:10,630
And I'm going to paste the value that I just copied.

86
00:06:10,900 --> 00:06:18,610
So the value that we just copied is going to say that I am running an iPhone on iOS 15, running Apple

87
00:06:18,610 --> 00:06:25,930
WebKit rendering engine, and if we scroll to the end, you'll see that we are running Safari web browser.

88
00:06:26,440 --> 00:06:29,500
So I'm going to click on the tick in here to save it.

89
00:06:29,500 --> 00:06:31,450
And now that should be saved.

90
00:06:31,450 --> 00:06:35,500
If it's not saved in your case you might want to go and restart the browser.

91
00:06:35,500 --> 00:06:40,120
But we can go ahead and double check by simply going to Google.

92
00:06:40,120 --> 00:06:42,760
And we can actually ask for our user agent.

93
00:06:43,060 --> 00:06:48,040
So I can just say what is my user agent?

94
00:06:49,580 --> 00:06:54,470
And as you can see, it is getting my user agent as an iPhone.

95
00:06:55,430 --> 00:07:01,400
We can also double check if this is working correctly by going to Instagram.

96
00:07:01,400 --> 00:07:05,330
And let's see if we get the mobile version of Instagram.

97
00:07:05,330 --> 00:07:06,260
And perfect.

98
00:07:06,260 --> 00:07:11,390
As you can see, we're getting a completely different version than the version that we saw earlier because

99
00:07:11,390 --> 00:07:13,880
the version that we saw earlier was the desktop version.

100
00:07:13,880 --> 00:07:16,610
But right now we are getting the mobile version.

101
00:07:16,880 --> 00:07:23,570
If I click on Log In again, you can see we're getting a much simpler version of Instagram, which is

102
00:07:23,570 --> 00:07:27,620
the exact version that you would get if you browse this website from a mobile.

103
00:07:27,620 --> 00:07:33,020
And the reason why we're getting this now, because we're simply telling Instagram that I am a mobile

104
00:07:33,020 --> 00:07:33,380
phone.

105
00:07:33,380 --> 00:07:34,910
I am an iPhone 14.

106
00:07:34,910 --> 00:07:41,510
Instead of sending the default identity or the default user agent, which tells Instagram that I am

107
00:07:41,510 --> 00:07:44,150
a Linux computer running on a desktop.

108
00:07:44,480 --> 00:07:49,160
So this is the first step of trying to get this attack to work against mobile phones.

109
00:07:49,160 --> 00:07:55,220
The next goal is going to be to hide the cursor, and to have a keyboard that automatically pops up,

110
00:07:55,220 --> 00:07:57,440
and I'm going to show you how to do that next.

111
00:07:58,340 --> 00:08:05,930
Once you are done with this, if you want to reset your user agent, you can simply go back to the about

112
00:08:05,930 --> 00:08:11,690
column config, and you can click on the edit in here and set it to a user agent of a desktop.

113
00:08:11,690 --> 00:08:17,210
If you want to pretend or to be a desktop, or you can simply delete it and restart Firefox.

114
00:08:17,210 --> 00:08:22,160
Sometimes, like I said, changing this would require you to restart Firefox and deleting the browser

115
00:08:22,160 --> 00:08:22,640
data.

116
00:08:22,640 --> 00:08:24,980
But all of that is very simple.

117
00:08:24,980 --> 00:08:30,050
But right now we are happy with pretending to be an iPhone, so that's why we are going to keep it the

118
00:08:30,050 --> 00:08:31,340
way it is right here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:05,600
Now that the website is loaded through this web browser, think that we are using a mobile phone.

2
00:00:05,600 --> 00:00:08,930
The next goal is to try to hide this mouse right here.

3
00:00:08,930 --> 00:00:15,830
Because if we give this link to a target and they load it from a mobile device, as we know mobile devices

4
00:00:15,830 --> 00:00:22,700
don't have a cursor, a mouse cursor, and therefore if they see a cursor, they will instantly feel

5
00:00:22,700 --> 00:00:28,190
like something fishy is happening and will probably not log in to this page.

6
00:00:28,730 --> 00:00:33,740
So to hide the cursor, we're going to be using a program called X banish.

7
00:00:33,740 --> 00:00:36,830
But this program relies on a number of packages.

8
00:00:36,830 --> 00:00:40,070
So first we're going to go ahead and install these packages.

9
00:00:40,070 --> 00:00:43,190
So first of all I'm just going to quit the novnc.

10
00:00:43,190 --> 00:00:45,110
And I'm going to clear my screen.

11
00:00:45,110 --> 00:00:49,370
And I'm going to elevate my privileges to root by doing sudo su.

12
00:00:49,370 --> 00:00:51,950
And now I am running commands as root.

13
00:00:51,950 --> 00:00:53,600
I'm going to update the sources.

14
00:00:53,600 --> 00:00:55,190
So I'm going to do apt update.

15
00:00:55,190 --> 00:00:57,140
And we know what this does.

16
00:00:57,140 --> 00:01:01,670
It simply updates the sources of packages that we can download applications from.

17
00:01:01,670 --> 00:01:06,590
And now that the sources are updated, we're going to be using APT to install packages.

18
00:01:06,590 --> 00:01:10,700
As you know, we're saying we want to install all of these packages.

19
00:01:10,700 --> 00:01:17,090
So GCC is a C compiler because the program that we want to install in the next step is programmed in

20
00:01:17,120 --> 00:01:20,480
C, make is needed to install such programs.

21
00:01:20,480 --> 00:01:24,560
And all of these packages are simply needed by the program.

22
00:01:24,560 --> 00:01:29,150
So the program relies on these packages and they do mention it on their GitHub page.

23
00:01:29,150 --> 00:01:31,520
So it's not like I'm a genius and I know this.

24
00:01:31,520 --> 00:01:37,910
And finally we're installing Unclutter because that is a program that actually does hide the mouse cursor.

25
00:01:37,910 --> 00:01:39,230
But it's not perfect.

26
00:01:39,230 --> 00:01:41,120
It still shows it every now and then.

27
00:01:41,120 --> 00:01:44,270
And that's why we're first of all going to be installing this program.

28
00:01:44,270 --> 00:01:48,740
And then we're installing X banish to fully hide the cursor.

29
00:01:49,370 --> 00:01:52,850
So I'm going to hit enter and it's asking me, do I really want to do this?

30
00:01:52,850 --> 00:01:55,970
I'm going to say yes, install all of these packages for me please.

31
00:01:55,970 --> 00:02:00,020
And it's going to take some time to download and install packages as usual.

32
00:02:00,820 --> 00:02:07,270
Now that we have all of the packages installed, I'm going to clear the screen and I'm going to go ahead

33
00:02:07,270 --> 00:02:10,180
and navigate to the opt directory.

34
00:02:10,180 --> 00:02:12,400
So Opt is short for optional.

35
00:02:12,400 --> 00:02:15,520
It's where you should be installing your optional applications.

36
00:02:15,520 --> 00:02:19,090
And the application that I'm going to be installing is technically optional.

37
00:02:19,090 --> 00:02:21,130
That's why I'm going to be installing it there.

38
00:02:21,130 --> 00:02:24,280
And I'm using the CD command to navigate to this directory.

39
00:02:25,020 --> 00:02:29,070
Next, I'm going to go ahead and download the program from their git repository.

40
00:02:29,070 --> 00:02:32,910
I will include its link in the resources of this lecture.

41
00:02:32,910 --> 00:02:38,700
So I'm simply going to do git clone the link of the git repository.

42
00:02:39,330 --> 00:02:43,320
So git is the command that we use to clone git repositories.

43
00:02:43,350 --> 00:02:49,440
Clone is used to download a repository, and we're given the link to the repository that we want to

44
00:02:49,440 --> 00:02:50,820
download or clone.

45
00:02:51,240 --> 00:02:54,210
I'm going to hit enter and that will download it for me.

46
00:02:54,240 --> 00:02:57,660
If I do ls you'll see I have the directory in here.

47
00:02:57,660 --> 00:03:01,290
And I can navigate into it by doing CD Spanish.

48
00:03:01,650 --> 00:03:06,420
And finally to install this application we're going to run the command make.

49
00:03:07,090 --> 00:03:12,850
As you can see, we see no errors at all, meaning that the command got executed properly and now we

50
00:03:12,850 --> 00:03:15,880
can go ahead and use this program to hide the mouse.

51
00:03:15,880 --> 00:03:22,930
But if you go ahead and try it, it's actually not going to work because Tightvnc server, the VNC server

52
00:03:22,930 --> 00:03:29,200
that we actually installed earlier, is lightweight and doesn't give us full control over the mouse

53
00:03:29,200 --> 00:03:35,080
and the keyboard, and therefore we can't really fully control it using programs such as Spanish.

54
00:03:35,560 --> 00:03:41,650
Therefore, I'm actually going to clear the screen and install another VNC wrapper that actually is

55
00:03:41,650 --> 00:03:48,400
based on Tightvnc, but gives us a bit more options and a bit more control over the mouse and the keyboard.

56
00:03:48,610 --> 00:03:56,590
Again, we're using APT to install this program and it is called Tigervnc, but the package name is

57
00:03:56,590 --> 00:04:02,380
actually Tigervnc stand alone server.

58
00:04:02,560 --> 00:04:11,710
And we also need the Tigervnc command package to also install some of the needed features that we're

59
00:04:11,710 --> 00:04:12,670
going to be using.

60
00:04:13,340 --> 00:04:18,200
So we're basically using APT to install a program called Tigervnc.

61
00:04:18,230 --> 00:04:25,160
The package name is Tigervnc standalone server, and Tigervnc is a set of tools that will be used by

62
00:04:25,160 --> 00:04:26,090
Tigervnc.

63
00:04:26,150 --> 00:04:31,610
And the reason why we're installing this, even though we have a VNC server, like I said, because

64
00:04:31,610 --> 00:04:37,520
this server actually is based on the VNC server that we already have, but it's going to give us more

65
00:04:37,520 --> 00:04:40,880
control over the input, such as the mouse and the keyboard.

66
00:04:41,270 --> 00:04:45,200
So I'm going to hit enter and I'm going to say yes, please install it for me.

67
00:04:45,650 --> 00:04:52,460
And now that everything is installed because again this VNC server is going to give us more control

68
00:04:52,460 --> 00:04:54,710
over the graphical user interface.

69
00:04:54,710 --> 00:04:59,600
Sometimes it works straight away, but it's a better idea to actually restart to make sure that it's

70
00:04:59,600 --> 00:05:01,100
going to work as expected.

71
00:05:01,100 --> 00:05:06,020
So I'm simply going to do reboot to restart the computer on the cloud.

72
00:05:06,020 --> 00:05:10,730
So because this computer is on the cloud, I have no way of checking whether it's up or not.

73
00:05:10,730 --> 00:05:16,700
We're simply just going to give it a minute or so to restart, and then we're simply going to run the

74
00:05:16,700 --> 00:05:18,980
SSH command to connect to it again.

75
00:05:19,310 --> 00:05:21,860
So we're going to hit enter to connect to it again.

76
00:05:22,510 --> 00:05:23,260
And perfect.

77
00:05:23,260 --> 00:05:28,870
We're back into our server and we're simply going to start the VNC server again.

78
00:05:28,870 --> 00:05:35,140
But remember we used to use the Tightvnc server command, this command right here to connect to the

79
00:05:35,140 --> 00:05:35,710
server.

80
00:05:35,740 --> 00:05:38,500
Now this time we installed a different server.

81
00:05:38,500 --> 00:05:40,570
Like I said it's the Tigervnc.

82
00:05:40,570 --> 00:05:45,880
And therefore we're simply going to run VNC server instead of Tightvnc server.

83
00:05:45,880 --> 00:05:51,220
So Tigervnc the program that we just installed is a little bit more strict with the depth options.

84
00:05:51,220 --> 00:05:54,310
So it actually needs to be 32 instead of 30.

85
00:05:54,310 --> 00:06:00,820
And also by default, this program is only going to allow you to connect to it from the local host.

86
00:06:00,820 --> 00:06:03,670
So that's not a problem if you're using no VNC.

87
00:06:03,760 --> 00:06:10,840
But remember, once the user logs into their account using no VNC, we usually kill no VNC and then

88
00:06:10,840 --> 00:06:14,650
connect using ripple in order to have access to their account.

89
00:06:14,650 --> 00:06:21,730
So that's why we need this VNC server to allow me to connect to it through outside of the local host,

90
00:06:21,730 --> 00:06:27,820
and that's why we're going to need this option which basically says local host no, which means that

91
00:06:27,820 --> 00:06:31,570
do not restrict this program to only work on the local host.

92
00:06:31,570 --> 00:06:37,300
Allow me to connect to it from outside of the local host using programs such as ripple, VNC.

93
00:06:37,720 --> 00:06:39,250
So I'm going to hit enter.

94
00:06:40,110 --> 00:06:43,050
And that's my VNC server running as expected.

95
00:06:43,050 --> 00:06:49,470
And then we're going to run our no VNC proxy exactly the same way that we did before.

96
00:06:49,470 --> 00:06:51,030
No changes at all in here.

97
00:06:51,030 --> 00:06:52,290
I'm going to hit enter.

98
00:06:53,200 --> 00:06:56,470
And let's go ahead and see if we can hide the mouse.

99
00:06:56,470 --> 00:07:00,700
So we're going to access our instance online.

100
00:07:00,700 --> 00:07:05,590
You're going to get this message asking you if you want to add a color management device.

101
00:07:05,590 --> 00:07:06,880
I'm just going to minimize it.

102
00:07:06,880 --> 00:07:09,310
Don't really need to deal with it right now.

103
00:07:09,310 --> 00:07:13,210
And we're going to go ahead and run X banish.

104
00:07:13,210 --> 00:07:14,860
That's the main thing that we want to do.

105
00:07:14,860 --> 00:07:16,870
The program that is going to hide the mass for me.

106
00:07:16,870 --> 00:07:19,210
So this is the mouse right here as you can see.

107
00:07:19,210 --> 00:07:25,300
And let's go ahead and run it by typing opt X banish.

108
00:07:25,300 --> 00:07:27,250
This is where the program is stored.

109
00:07:27,250 --> 00:07:29,980
Ex-spanish is actually the name of the program.

110
00:07:29,980 --> 00:07:36,550
And we're saying we want to run it using the Dash a option, which basically means that I want to hide

111
00:07:36,550 --> 00:07:40,630
the mouse all the time, regardless of what's happening on this computer.

112
00:07:41,020 --> 00:07:43,900
So as you can see, we have the mouse right here.

113
00:07:43,900 --> 00:07:46,690
And we're going to go ahead and run this command.

114
00:07:47,380 --> 00:07:48,280
And perfect.

115
00:07:48,280 --> 00:07:52,870
As you can see, the mouse has disappeared and you can see if I move it outside of the VNC.

116
00:07:52,900 --> 00:07:56,050
It comes up available in here on the right of the screen.

117
00:07:56,050 --> 00:07:59,260
But once I go inside the desktop it is hidden.

118
00:08:00,020 --> 00:08:06,620
So this is very, very useful in the next steps when we actually go ahead and run the attack.

119
00:08:06,620 --> 00:08:08,570
But this is only the second challenge.

120
00:08:08,570 --> 00:08:12,800
So like we said, first of all, we want the target to see the mobile version of the website.

121
00:08:12,800 --> 00:08:13,700
And we did that.

122
00:08:13,700 --> 00:08:16,700
The second goal was to hide the mouse and we did that.

123
00:08:16,700 --> 00:08:23,420
And the third goal is going to be getting a keyboard so that when the target taps on an input box,

124
00:08:23,420 --> 00:08:25,280
they will actually see a keyboard.

125
00:08:25,820 --> 00:08:31,250
So I'm going to quit this program, and we're just going to make sure that the terminal window is activated.

126
00:08:31,250 --> 00:08:33,260
And we're going to do control C to quit it.

127
00:08:33,260 --> 00:08:36,200
And as you can see I have my mouse back in here.

128
00:08:36,470 --> 00:08:42,650
And next I'm going to show you how to install a keyboard a virtual keyboard, an on screen keyboard

129
00:08:42,650 --> 00:08:48,890
on this computer so that our attack is going to be fully ready to be launched against mobile devices.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,900
So now that we are loading the mobile versions of all websites and we know how to hide the mouse cursor,

2
00:00:05,900 --> 00:00:12,980
we are getting very close to making this browser be very, very friendly and not suspicious at all for

3
00:00:12,980 --> 00:00:19,610
mobile devices, but as you know, mobile devices use an on screen keyboard, so when they tap on an

4
00:00:19,610 --> 00:00:25,910
input box, a keyboard is going to come up automatically from the bottom to allow them to input whatever

5
00:00:25,910 --> 00:00:27,470
data they want to input.

6
00:00:27,470 --> 00:00:31,520
Because mobile devices don't actually have a physical keyboard.

7
00:00:31,520 --> 00:00:37,850
So we're going to have to install a program on this computer so that it automatically displays an on

8
00:00:37,850 --> 00:00:41,870
screen keyboard once someone clicks an input box.

9
00:00:42,530 --> 00:00:45,290
Now again, this is the beauty of this attack.

10
00:00:45,290 --> 00:00:48,860
We control this computer and we can do whatever we want on it.

11
00:00:48,860 --> 00:00:55,340
So all we have to do is simply open up our terminal and install the needed programs from here.

12
00:00:55,340 --> 00:01:01,460
So I'm going to clear my screen and I'm going to use sudo to use the program apt to install packages,

13
00:01:01,460 --> 00:01:02,450
as you know.

14
00:01:02,480 --> 00:01:05,990
And we're going to install a package called On Board.

15
00:01:06,620 --> 00:01:14,150
Now on board is actually an on screen keyboard that we can configure to behave exactly like a mobile

16
00:01:14,150 --> 00:01:15,320
device keyboard.

17
00:01:15,350 --> 00:01:19,070
So I'm going to hit enter to install it, and we're going to hit enter again.

18
00:01:19,070 --> 00:01:21,080
It's only going to take a minute to install.

19
00:01:21,560 --> 00:01:22,370
And perfect.

20
00:01:22,370 --> 00:01:23,690
That should be installed now.

21
00:01:23,690 --> 00:01:27,710
So if we go to applications accessories.

22
00:01:28,280 --> 00:01:30,920
You can see that now we have two entries.

23
00:01:31,010 --> 00:01:34,910
So the first entry in here is the actual on screen keyboard.

24
00:01:34,910 --> 00:01:38,180
And the second entry is the settings for that keyboard.

25
00:01:38,210 --> 00:01:40,670
So first of all we're going to run the keyboard.

26
00:01:40,670 --> 00:01:42,500
And as you can see it looks hideous.

27
00:01:42,500 --> 00:01:44,630
And it's not behaving the way we want to.

28
00:01:44,630 --> 00:01:45,440
But it's fine.

29
00:01:45,440 --> 00:01:47,300
We can actually modify all of this.

30
00:01:47,300 --> 00:01:51,740
So we're just going to go to the applications again to the accessories.

31
00:01:51,740 --> 00:01:53,750
And we're going to load the settings.

32
00:01:55,090 --> 00:02:02,260
So from the settings, it's very important in the general to actually set it to auto show when editing

33
00:02:02,260 --> 00:02:03,010
a text box.

34
00:02:03,010 --> 00:02:11,080
So when a user clicks a text box, we want this keyboard to automatically pop from the bottom and the

35
00:02:11,080 --> 00:02:11,650
window.

36
00:02:11,650 --> 00:02:14,050
We're going to make sure that it docks to the screen.

37
00:02:14,050 --> 00:02:18,970
So that basically means I want it to fill both edges of the screen.

38
00:02:19,800 --> 00:02:22,380
And in the layout we're going to choose.

39
00:02:22,380 --> 00:02:29,040
So we can actually just click here to open up the keyboard to see what it looks like now.

40
00:02:29,040 --> 00:02:33,090
So as you can see, it's getting attached to the edges of the screen.

41
00:02:33,090 --> 00:02:36,450
And in the layout we're going to choose the phone layout.

42
00:02:36,450 --> 00:02:41,490
So as you can see again it's getting closer to a mobile phone looking keyboard.

43
00:02:41,490 --> 00:02:45,540
And in the theme I'm going to click the droid keyboard again.

44
00:02:45,540 --> 00:02:48,930
That makes it even closer to a mobile phone keyboard.

45
00:02:49,630 --> 00:02:53,230
Now in the auto show, you want to make sure that this is ticked.

46
00:02:53,230 --> 00:03:00,310
The auto show when editing a text again, and also just going back to the layout and to the window,

47
00:03:00,310 --> 00:03:05,050
you can see that you can play with the window transparency with the background.

48
00:03:05,050 --> 00:03:10,660
So you could make this look more or less similar to the target phone that you're targeting.

49
00:03:10,660 --> 00:03:16,750
But I think this settings right now are pretty good and pretty generic to many mobile phones.

50
00:03:16,780 --> 00:03:23,110
Now you can also, if you come here to the top of the keyboard, you can see the mouse is changing to

51
00:03:23,110 --> 00:03:25,600
allow you to edit the size of the keyboard.

52
00:03:25,600 --> 00:03:32,290
Again, as we know on mobile devices, the keyboard sometimes covers almost half of the page, so you're

53
00:03:32,290 --> 00:03:36,670
going to have to play with this to make it look as believable as possible.

54
00:03:36,910 --> 00:03:42,370
But let's go ahead and see if it's actually going to automatically show from the bottom when we click

55
00:03:42,370 --> 00:03:43,540
an input box.

56
00:03:43,540 --> 00:03:46,510
So I'm just going to click here to hide it again.

57
00:03:46,510 --> 00:03:52,420
And you can see as soon as I clicked on the terminal it showed up because the terminal is technically

58
00:03:52,420 --> 00:03:53,680
an input box.

59
00:03:53,680 --> 00:03:56,380
But let's run Firefox in here.

60
00:03:58,190 --> 00:04:00,860
And we're just going to say start a new session.

61
00:04:00,860 --> 00:04:04,790
And it automatically popped up because we have an input box here.

62
00:04:04,790 --> 00:04:07,700
But let's go, for example, to Instagram again.

63
00:04:08,840 --> 00:04:09,650
And perfect.

64
00:04:09,650 --> 00:04:11,960
If we click on Log In.

65
00:04:11,960 --> 00:04:14,090
As you can see, nothing shows up.

66
00:04:14,090 --> 00:04:20,780
But if we click in the input box, we're getting the keyboard automatically showing up from the bottom.

67
00:04:21,710 --> 00:04:27,200
Now I can also see that the background in here is showing up between the keyboard buttons.

68
00:04:27,200 --> 00:04:31,010
So I don't think this is very good when it comes to mobile devices.

69
00:04:31,010 --> 00:04:33,680
So I'm actually going to go back to the settings.

70
00:04:35,060 --> 00:04:40,130
And we're going to go on the transparency in here, and we're going to set this to zero.

71
00:04:40,890 --> 00:04:42,720
And we're going to untick this.

72
00:04:42,720 --> 00:04:43,440
And perfect.

73
00:04:43,440 --> 00:04:48,900
As you can see there is no background now you actually just have the color of the keyboard at the back.

74
00:04:49,990 --> 00:04:52,960
So right now we have everything that we need.

75
00:04:52,960 --> 00:04:54,280
We can hide the mouse.

76
00:04:54,280 --> 00:05:00,370
The website is loading in a mobile friendly manner, and we have a keyboard that will automatically

77
00:05:00,370 --> 00:05:02,980
show once we click an input box.

78
00:05:02,980 --> 00:05:06,970
And if we click away from the input box, the keyboard is getting hidden.

79
00:05:08,200 --> 00:05:15,280
Now, one more setting that I want to modify before we go ahead is the browser password manager.

80
00:05:15,280 --> 00:05:20,050
Because as you know, once you log in to a website, the browser is going to ask you if you want to

81
00:05:20,050 --> 00:05:21,280
save these passwords.

82
00:05:21,280 --> 00:05:28,450
This pop up will be suspicious to a user using a mobile phone, because you don't get this pop up from

83
00:05:28,450 --> 00:05:29,530
mobile phones.

84
00:05:29,530 --> 00:05:34,540
Now, modifying this is very easy, obviously, because it's our browser and we have full control over

85
00:05:34,540 --> 00:05:34,870
it.

86
00:05:34,870 --> 00:05:37,480
All we have to do is go to the settings.

87
00:05:39,370 --> 00:05:43,810
And we're going to search for password to see the settings for saving passwords.

88
00:05:43,810 --> 00:05:50,080
So as you can see for login for passwords, we're going to untick this box so that it doesn't ask us

89
00:05:50,080 --> 00:05:52,030
to save logins and passwords.

90
00:05:52,030 --> 00:05:58,090
And we're also going to untick this box so that it doesn't show us alerts for breaches and all of that.

91
00:05:58,090 --> 00:06:01,570
We don't want this browser to feel like a desktop browser.

92
00:06:01,570 --> 00:06:05,350
We want it to feel as much of a mobile browser as possible.

93
00:06:05,350 --> 00:06:10,330
And that's why we're removing these prompts, because once the user logs in, they're going to see a

94
00:06:10,330 --> 00:06:13,780
prompt asking them if you want to save this password or not.

95
00:06:13,780 --> 00:06:20,890
That's why it's very important to disable this option so that when the user logs in, they don't see

96
00:06:20,890 --> 00:06:23,740
a prompt asking them if they want to save the password.

97
00:06:24,330 --> 00:06:24,990
Next.

98
00:06:24,990 --> 00:06:29,970
All we have to do is simply test the attack and see how it works in a real life scenario.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,170 --> 00:00:07,940
Okay, so now that we learned how to customize our computer on the cloud to behave like a mobile phone,

2
00:00:07,940 --> 00:00:14,060
let's go ahead and run the attack against the mobile phone and try to target a user that is using a

3
00:00:14,060 --> 00:00:15,080
mobile phone.

4
00:00:15,080 --> 00:00:20,150
Now first of all, the actually there is one more step that we have to do, but it's very simple is

5
00:00:20,150 --> 00:00:24,200
to run the VNC server in a portrait mode.

6
00:00:24,200 --> 00:00:28,070
So first of all we're going to do VNC server.

7
00:00:29,530 --> 00:00:35,290
Dash kill to kill my existing running VNC instance.

8
00:00:35,560 --> 00:00:37,480
I'm going to hit enter and that's it.

9
00:00:37,480 --> 00:00:38,050
Killed.

10
00:00:38,050 --> 00:00:40,930
And next we're going to run the VNC server.

11
00:00:41,290 --> 00:00:46,720
The only difference this time we usually run it in this geometry right here.

12
00:00:46,720 --> 00:00:49,450
So we use one 920 by 1080.

13
00:00:49,720 --> 00:00:54,070
Now in order to run it in portrait mode we're going to have to flip this.

14
00:00:54,070 --> 00:00:59,560
So we're going to run it in 1080 X19 20.

15
00:01:00,790 --> 00:01:03,700
We're keeping everything else the same.

16
00:01:03,700 --> 00:01:05,980
I'm going to hit enter and that's it.

17
00:01:05,980 --> 00:01:06,610
Running.

18
00:01:06,970 --> 00:01:12,310
Next I'm going to go ahead and run my Novnc proxy.

19
00:01:12,790 --> 00:01:14,950
And that is running as expected.

20
00:01:14,950 --> 00:01:19,990
And if I go to a web browser just to show you what it's going to look like, perfect.

21
00:01:19,990 --> 00:01:22,930
As you can see, it's loading in portrait mode.

22
00:01:22,930 --> 00:01:28,780
So this is pretty much the last step to get this attack to work as expected on a mobile phone.

23
00:01:29,320 --> 00:01:33,400
Now you're going to have to use this screen while it's very small, but it should be easy enough for

24
00:01:33,400 --> 00:01:33,880
you.

25
00:01:33,910 --> 00:01:38,650
We're going to have to go ahead and run the on screen keyboard on board.

26
00:01:38,650 --> 00:01:40,450
So I'm just going to click it in here.

27
00:01:40,660 --> 00:01:41,470
And perfect.

28
00:01:41,470 --> 00:01:42,280
It's running here.

29
00:01:42,280 --> 00:01:43,660
One click just to see.

30
00:01:43,660 --> 00:01:45,520
As you can see it looks pretty good.

31
00:01:45,520 --> 00:01:46,600
Size is decent.

32
00:01:46,600 --> 00:01:49,780
Like I said you can go in here and move it up if you want.

33
00:01:49,780 --> 00:01:54,580
And even on the sides if it's not filling the screen, you can move it by going to the sides or the

34
00:01:54,580 --> 00:01:55,930
edges of the keyboard.

35
00:01:55,930 --> 00:01:57,610
But I'm happy with this.

36
00:01:57,910 --> 00:02:01,420
Next, I'm going to go ahead and hide my mouse, my cursor.

37
00:02:01,420 --> 00:02:03,340
So I'm going to open up my terminal.

38
00:02:03,340 --> 00:02:09,160
So as we know before we can do that by going to opt in Spanish.

39
00:02:09,310 --> 00:02:14,140
Spanish is the name of the program and dash a to hide the cursor under all circumstances.

40
00:02:14,740 --> 00:02:20,200
I'm also going to put the ampersand at the end of the command to basically say, I want to run this

41
00:02:20,200 --> 00:02:23,920
command in the background so that I can run other commands.

42
00:02:23,920 --> 00:02:25,300
So I'm going to hit enter.

43
00:02:25,300 --> 00:02:27,580
And as you can see, that's running in the background.

44
00:02:27,580 --> 00:02:29,980
But my mouse is still here.

45
00:02:29,980 --> 00:02:32,020
So I'm going to have to actually kill it.

46
00:02:32,350 --> 00:02:37,630
So I'm just going to do kill all Spanish and I'm going to run it again.

47
00:02:39,610 --> 00:02:40,390
And perfect.

48
00:02:40,390 --> 00:02:43,090
This time it's actually working as expected.

49
00:02:43,090 --> 00:02:44,410
I can't see the mouse.

50
00:02:44,500 --> 00:02:51,190
And next I'm going to need to go ahead and run Firefox, this time in kiosk mode, and we're going to

51
00:02:51,190 --> 00:02:52,660
load gmail.com.

52
00:02:52,930 --> 00:02:54,250
I'm going to hit enter.

53
00:02:56,470 --> 00:02:59,410
And we're going to go to the login page of Gmail.

54
00:02:59,410 --> 00:03:03,910
Now, as you can see, I don't have a mouse, but I can see what's getting highlighted and perfect.

55
00:03:03,910 --> 00:03:09,460
We have the Gmail page in here with the keyboard automatically being displayed because the input box

56
00:03:09,460 --> 00:03:10,690
is already selected.

57
00:03:10,690 --> 00:03:16,090
So again, I can just move the mouse a bit and click anywhere in the white space to remove the keyboard.

58
00:03:16,090 --> 00:03:22,660
And I can do Control Plus to zoom this page in to make it look again even more believable.

59
00:03:23,200 --> 00:03:24,850
So you can go with this design.

60
00:03:24,850 --> 00:03:27,610
This is what I actually usually get on my phone.

61
00:03:27,610 --> 00:03:31,780
If you zoom in more, you're going to get this kind of design right here.

62
00:03:31,780 --> 00:03:33,340
So let's keep it at this.

63
00:03:33,340 --> 00:03:39,070
And we're going to go ahead and go to Zacks.com from a mobile device.

64
00:03:39,940 --> 00:03:42,820
So I have a mobile device in here.

65
00:03:42,820 --> 00:03:44,200
This is actually my phone.

66
00:03:44,200 --> 00:03:45,640
It's just been streamed.

67
00:03:45,640 --> 00:03:49,030
And we're going to go to XSS.

68
00:03:49,820 --> 00:03:52,880
X-Com and perfect.

69
00:03:52,880 --> 00:03:58,490
As you can see, we get a page that looks very similar to the mobile version of Gmail.

70
00:03:58,490 --> 00:04:02,330
So let's actually go ahead and see what the mobile version of Gmail looks like.

71
00:04:02,330 --> 00:04:08,180
This is the actual mobile version of Gmail that loads on the iPhone, and this is the one that we are

72
00:04:08,180 --> 00:04:08,990
spoofing now.

73
00:04:08,990 --> 00:04:14,150
As you can see, the original, the proper one is a little bit more zoomed in, so it's very easy.

74
00:04:14,150 --> 00:04:15,050
I can go back.

75
00:04:15,050 --> 00:04:18,290
So obviously you're going to be experimenting with this yourself.

76
00:04:18,290 --> 00:04:21,560
So we can just go back in here and zoom in a little bit more.

77
00:04:22,180 --> 00:04:26,890
So now this is the cloned Gmail login page.

78
00:04:26,890 --> 00:04:30,580
And right here is the real login page.

79
00:04:30,580 --> 00:04:35,380
Now obviously this one looks a little bit different because of the fact that I logged in to this account

80
00:04:35,380 --> 00:04:38,830
before and it's automatically selecting it for me on the top.

81
00:04:39,190 --> 00:04:42,280
Other than that, the page looks pretty much identical.

82
00:04:42,640 --> 00:04:44,140
So let's go ahead and log in.

83
00:04:44,140 --> 00:04:47,680
And as you can see if I type in here I'm going to get the on screen keyboard.

84
00:04:47,680 --> 00:04:51,340
And I'm going to put the username tap next.

85
00:04:51,340 --> 00:04:53,590
And it's going to ask me for the password.

86
00:04:55,460 --> 00:04:59,090
And now, as you can see, it's doing the two step verification.

87
00:04:59,090 --> 00:05:01,580
It's going to send a text message to my mobile phone.

88
00:05:01,580 --> 00:05:03,440
I'm going to say yes, please do that.

89
00:05:03,440 --> 00:05:05,240
So I have the message right here.

90
00:05:05,240 --> 00:05:06,440
As you can see.

91
00:05:06,440 --> 00:05:09,950
And it is 190106.

92
00:05:10,460 --> 00:05:12,260
So we'll put it in here.

93
00:05:14,200 --> 00:05:15,190
And perfect.

94
00:05:15,190 --> 00:05:20,050
As you can see, we have full access to the account now and we can do whatever we want.

95
00:05:20,050 --> 00:05:28,060
So all we have to do at this stage is to go back to our novnc in here, control C to disconnect the

96
00:05:28,060 --> 00:05:28,480
user.

97
00:05:28,480 --> 00:05:31,300
So the user lost access in here, as you can see.

98
00:05:31,300 --> 00:05:33,940
And then we're going to go to remote Repl.

99
00:05:35,170 --> 00:05:38,770
Cover this before we're going to connect to our machine.

100
00:05:39,250 --> 00:05:44,620
And perfect as you can see now we have access to their account and we can do whatever we want.

101
00:05:44,620 --> 00:05:45,430
From here.

102
00:05:45,430 --> 00:05:50,980
We can delete, add, send messages, change the password, dump the cookies.

103
00:05:50,980 --> 00:05:56,650
We also should have the password in our keylogger because we installed the keylogger on this computer.

104
00:05:56,650 --> 00:06:02,050
So like I said before, the possibilities of this are actually endless.

105
00:06:02,050 --> 00:06:05,620
You can use it to hack into any type of an account you want.

106
00:06:07,330 --> 00:06:12,910
Keep in mind, guys, the main cool thing about the browser in browser attack is the fact that it's

107
00:06:12,910 --> 00:06:19,450
running on a computer that we fully control, so you can pretty much implement anything you can think

108
00:06:19,450 --> 00:06:19,810
of.

109
00:06:19,810 --> 00:06:24,910
So you could add a functionality where the page could be available to multiple people.

110
00:06:24,910 --> 00:06:29,140
Like as you can see in here, we're modifying the whole operating system.

111
00:06:29,140 --> 00:06:34,450
We're modifying the whole browser to make it seem like a mobile browser so that we can target mobiles.

112
00:06:34,450 --> 00:06:40,780
Previously, we installed a cookie manager and a keylogger so that we can collect everything that's

113
00:06:40,780 --> 00:06:44,050
happening on this browser and then maybe use the cookies to log in.

114
00:06:44,050 --> 00:06:49,900
So this attack is very, very customizable and can be used in so many scenarios.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: Multi-BitB Attack

1
00:00:00,200 --> 00:00:06,650
So far we covered how to clone any login page, steal the login information such as the username and

2
00:00:06,650 --> 00:00:12,860
the password, and even bypass two factor or multifactor authentication using the browser in-browser

3
00:00:12,860 --> 00:00:13,490
attack.

4
00:00:14,170 --> 00:00:20,230
We also built on this in the previous lectures and showed you how to make the login pages mobile friendly.

5
00:00:20,230 --> 00:00:25,750
So at this stage we can target pretty much all operating systems and all devices.

6
00:00:26,380 --> 00:00:33,250
The only limitation is that once we run a page on our server on the cloud, as you can see in here,

7
00:00:33,250 --> 00:00:37,510
anyone that access this link will actually see this login page.

8
00:00:37,510 --> 00:00:42,880
So once our target logs into this login page everybody is going to be able to see that.

9
00:00:43,090 --> 00:00:47,740
Therefore as a result we can only target one device at a time.

10
00:00:47,740 --> 00:00:51,250
And we can only have one login page running at a time.

11
00:00:51,250 --> 00:00:55,180
So we can only have, for example, a Gmail login or a Facebook login.

12
00:00:55,180 --> 00:01:00,220
And we can only target one person with that login, because we can't have multiple people trying to

13
00:01:00,220 --> 00:01:02,380
log in to the same login page.

14
00:01:02,920 --> 00:01:08,500
So once we have Gmail loaded in here, Gmail will be accessible using this link.

15
00:01:08,500 --> 00:01:13,810
And everybody that access this link will see the exact same Gmail login page.

16
00:01:13,810 --> 00:01:18,970
But if this guy starts filling up the login information, their login information, everybody's going

17
00:01:18,970 --> 00:01:21,070
to be able to see this login information.

18
00:01:21,070 --> 00:01:27,550
So that's why we can only target one person and we can only have one login page running at a time.

19
00:01:28,030 --> 00:01:33,970
Therefore, in this section I want to show you how to run multiple login pages at the same time.

20
00:01:34,210 --> 00:01:39,760
Each login page will have its own URL and can be configured in any way you want.

21
00:01:39,940 --> 00:01:45,370
Some of them could even load the mobile friendly version, as you can see in here, and as a result,

22
00:01:45,370 --> 00:01:48,490
we can target multiple devices at the same time.

23
00:01:48,490 --> 00:01:52,870
And also, like I said, have multiple login pages running at the same time.

24
00:01:53,530 --> 00:01:57,790
To achieve this, let's break the larger problem into smaller challenges.

25
00:01:57,790 --> 00:01:59,620
We'll start with the simplest one.

26
00:01:59,620 --> 00:02:07,600
So the first thing that we need to do is to be able to connect to our VNC server from two different

27
00:02:07,600 --> 00:02:08,440
computers.

28
00:02:08,860 --> 00:02:10,840
So we're going to forget about no VNC.

29
00:02:10,870 --> 00:02:13,960
We're going to forget about having different browsers running in here.

30
00:02:13,960 --> 00:02:18,970
We're going to forget about having different URLs for them to access the different login pages.

31
00:02:18,970 --> 00:02:21,760
We're going to simplify the problem as simple as possible.

32
00:02:21,760 --> 00:02:28,900
And the first thing we want to do is be able to have two different VNC sessions allowing us to connect

33
00:02:28,900 --> 00:02:30,580
to the same computer.

34
00:02:30,580 --> 00:02:33,610
And each one of these sessions need to be independent.

35
00:02:33,610 --> 00:02:34,780
It needs to be different.

36
00:02:34,780 --> 00:02:40,540
So if this guy opens up a browser window and this guy opens up a calculator, for example, they will

37
00:02:40,540 --> 00:02:43,210
have their own calculator and their own browser window.

38
00:02:43,210 --> 00:02:45,520
They will not be sharing the same desktop.

39
00:02:46,380 --> 00:02:50,160
So to do this, first of all, we're going to go to our terminal.

40
00:02:50,190 --> 00:02:55,740
I'm already logged in to my Cloud Kali machine and I'm going to elevate my privileges to root.

41
00:02:55,920 --> 00:03:02,370
And from here, before we do anything, we need to install a package called D-Bus, which is necessary

42
00:03:02,370 --> 00:03:08,550
for system communication so that we can run multiple VNC sessions without them interfering with each

43
00:03:08,550 --> 00:03:09,060
other.

44
00:03:09,060 --> 00:03:13,590
So to install a package, as you know, we first do apt update.

45
00:03:15,600 --> 00:03:18,870
And I'm just running this command so that the autocomplete will be white.

46
00:03:18,870 --> 00:03:20,130
So neglect this command.

47
00:03:20,130 --> 00:03:21,210
Don't worry about it.

48
00:03:21,210 --> 00:03:23,760
So next we want to install the D-Bus package.

49
00:03:23,760 --> 00:03:25,320
So we're going to do apt.

50
00:03:26,070 --> 00:03:27,300
Install.

51
00:03:28,180 --> 00:03:32,260
R sync and D-Bus X11.

52
00:03:33,590 --> 00:03:34,820
We're going to hit enter.

53
00:03:35,590 --> 00:03:41,110
And as you can see, it's telling me that these packages are already installed in my system for you.

54
00:03:41,140 --> 00:03:42,370
You're going to have to install them.

55
00:03:42,370 --> 00:03:46,600
Just wait, give it a few seconds and it will automatically download and install the package.

56
00:03:46,810 --> 00:03:50,890
Once you have that running, the next steps are actually very, very simple.

57
00:03:50,890 --> 00:03:55,870
I'm going to clear the screen and I'm going to run my VNC server using the exact same command.

58
00:03:55,870 --> 00:03:58,300
So we do VNC server.

59
00:03:58,300 --> 00:04:02,800
We select the geometry, we select the depth and we say localhost no.

60
00:04:02,800 --> 00:04:04,750
So we can remotely connect to it.

61
00:04:04,750 --> 00:04:06,310
I'm going to hit enter.

62
00:04:07,160 --> 00:04:11,150
And as you can see, I have my VNC server running right now.

63
00:04:11,150 --> 00:04:15,860
And as you can see, it's given us the port 5901 on display one.

64
00:04:15,860 --> 00:04:20,000
So right now we have one VNC session running right here.

65
00:04:20,000 --> 00:04:23,570
So you can visualize this VNC session running in here.

66
00:04:23,570 --> 00:04:26,450
And we can go ahead and connect to it using remote Repl.

67
00:04:26,900 --> 00:04:32,870
And what we want to do next is to have another VNC session running on another display, so that we can

68
00:04:32,870 --> 00:04:38,570
use different applications in each of these sessions without them interfering with each other.

69
00:04:39,080 --> 00:04:44,360
Now, to do this, because we installed the needed packages, we can simply run the exact same command

70
00:04:44,360 --> 00:04:45,020
again.

71
00:04:45,020 --> 00:04:50,000
But keep in mind, because this is going to be a completely different session, you can actually select

72
00:04:50,000 --> 00:04:51,080
a different resolution.

73
00:04:51,080 --> 00:04:57,980
So remember when we executed the attack against the mobile phone we use the 1080 by one 920 resolution.

74
00:04:57,980 --> 00:04:59,930
So you can modify this in here.

75
00:04:59,930 --> 00:05:03,260
And that's the beauty of what we're trying to do in this section.

76
00:05:03,260 --> 00:05:08,990
We're going to be able to run completely independent sessions, configure them any way we want and as

77
00:05:08,990 --> 00:05:12,350
a result target different devices and different login pages.

78
00:05:12,500 --> 00:05:15,290
But for now I'm going to keep everything the same.

79
00:05:15,290 --> 00:05:16,670
I'm going to hit enter.

80
00:05:16,670 --> 00:05:24,410
And as you can see we have another VNC session running right now on port 5902 on display two.

81
00:05:24,470 --> 00:05:29,330
So note how the port number here is two and the display is number two.

82
00:05:29,330 --> 00:05:33,170
And then the port here is one and the display is number one.

83
00:05:33,170 --> 00:05:37,340
And as we move on and run another VNC session you can guess it.

84
00:05:37,340 --> 00:05:41,270
It's going to run on 5903 on display three and so on.

85
00:05:41,270 --> 00:05:45,140
So each of these displays is independent.

86
00:05:45,140 --> 00:05:46,760
It's running on a different port.

87
00:05:46,760 --> 00:05:52,820
And therefore if we run any application on any of these displays they will be completely separate and

88
00:05:52,820 --> 00:05:53,420
independent.

89
00:05:53,420 --> 00:05:58,580
So I'll be able, for example, to run a browser in here and then run a calculator in here, and I'll

90
00:05:58,580 --> 00:06:01,100
be able to control them independently.

91
00:06:01,100 --> 00:06:06,560
And therefore in the future, once we build on this and have it accessible using a URL, we'll be able

92
00:06:06,560 --> 00:06:08,690
to target completely different people.

93
00:06:09,250 --> 00:06:16,360
So now to list all of the current running VNC sessions we can simply run VNC server list.

94
00:06:17,190 --> 00:06:19,740
And again, as you can see, it's giving us the displaying.

95
00:06:19,740 --> 00:06:23,010
Here we have a session on display one and a session on display two.

96
00:06:23,010 --> 00:06:24,570
And it's also given us the port.

97
00:06:24,570 --> 00:06:30,000
One of them is running on port 5901 and the next is running on port 5902.

98
00:06:30,390 --> 00:06:36,330
So let's go ahead and test this and see if we can connect to the same server and see if we can establish

99
00:06:36,330 --> 00:06:41,010
two completely independent VNC connections to the same server.

100
00:06:41,430 --> 00:06:43,830
So at the moment we're not using Novnc.

101
00:06:43,860 --> 00:06:46,710
We're going to have to connect to it using remote Repl.

102
00:06:46,710 --> 00:06:51,840
And therefore you want to make sure that this port is accessible over the internet in your security

103
00:06:51,840 --> 00:06:52,470
policy.

104
00:06:52,470 --> 00:06:56,730
So if you go here and you want to select your machine.

105
00:06:56,730 --> 00:06:59,220
So in my case, it's this machine right here.

106
00:07:00,070 --> 00:07:01,420
You want to go to security?

107
00:07:01,450 --> 00:07:02,380
We covered this before.

108
00:07:02,410 --> 00:07:04,060
That's why I'm doing it quickly.

109
00:07:04,060 --> 00:07:08,740
And in here you can edit the inbound rules if you want to add new rules.

110
00:07:08,740 --> 00:07:15,430
But I've already allowed 5901 and 5902, which are the ports that we have in here.

111
00:07:16,210 --> 00:07:18,670
So I can go ahead to my remote Repl again.

112
00:07:18,670 --> 00:07:20,110
I covered how to use this before.

113
00:07:20,110 --> 00:07:23,170
That's why I'm doing it very quickly and I'm going to be connecting.

114
00:07:23,170 --> 00:07:27,250
If I click on edit here, you'll see I'm connecting to the 5901.

115
00:07:27,250 --> 00:07:31,870
So I can simply right click and connect to it just to see if it works.

116
00:07:31,870 --> 00:07:33,190
Put my password.

117
00:07:34,140 --> 00:07:34,530
Perfect.

118
00:07:34,530 --> 00:07:36,210
As you can see, we're able to connect.

119
00:07:36,210 --> 00:07:39,960
We have the first VNC session, but so far we haven't done anything new.

120
00:07:39,990 --> 00:07:44,880
We already know how to do this, but just for the sake of demonstration, I'm going to just open a normal

121
00:07:44,880 --> 00:07:46,110
file browser in here.

122
00:07:46,110 --> 00:07:49,380
Let's just open up just any folder, as you can see in here.

123
00:07:49,380 --> 00:07:52,620
And we're going to go back to remote Repl.

124
00:07:53,700 --> 00:07:56,220
And I'm going to create a new connection.

125
00:07:56,220 --> 00:07:56,790
Again.

126
00:07:56,790 --> 00:07:59,430
The host is going to be Zacks.com.

127
00:07:59,850 --> 00:08:06,840
The port this time is going to be 5902, because I'm connecting to the second display and we're going

128
00:08:06,840 --> 00:08:08,400
to call this Carly two.

129
00:08:09,180 --> 00:08:12,090
We're gonna save and let's connect to it.

130
00:08:14,030 --> 00:08:16,550
But my password and perfect.

131
00:08:16,550 --> 00:08:22,970
As you can see, I have established another connection to the same Kali server on the internet, but

132
00:08:22,970 --> 00:08:26,450
this connection is completely independent to the other one.

133
00:08:26,450 --> 00:08:32,510
So as you can see in the other one in here, as you can see, you we have a browser window open in here.

134
00:08:32,510 --> 00:08:37,340
And if we go to the other session, as you can see we've got nothing running in here.

135
00:08:37,340 --> 00:08:40,580
And we can go ahead and for example, run a web browser.

136
00:08:41,340 --> 00:08:43,170
As you can see, we have the web browser in here.

137
00:08:43,170 --> 00:08:48,240
We could have a login page on it, and then on the other one we can run the web browser and run a completely

138
00:08:48,240 --> 00:08:50,070
different login page on it.

139
00:08:50,860 --> 00:08:57,430
But so far we've solved the first problem, which is to be able to establish two connections to the

140
00:08:57,430 --> 00:08:58,930
same server on the cloud.

141
00:08:58,930 --> 00:09:04,000
And these connections need to be completely independent and work at the same time.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,450 --> 00:00:08,250
So now that we are able to run multiple VNC sessions, the next goal is to run separate Firefox instances

2
00:00:08,250 --> 00:00:09,450
at the same time.

3
00:00:09,450 --> 00:00:16,350
Because as you know, once you log in to a certain account on Firefox, you'll remain logged in to that

4
00:00:16,350 --> 00:00:18,960
account even if you start a new window.

5
00:00:18,990 --> 00:00:20,550
So let me show you what I mean.

6
00:00:20,550 --> 00:00:24,150
So right now I am already connected to one of my sessions in here.

7
00:00:24,150 --> 00:00:28,800
We're going to log in and let me put the two factor.

8
00:00:28,920 --> 00:00:34,320
So now that I'm logged in to Firefox in here, if we go to the other session and even though this session

9
00:00:34,320 --> 00:00:38,190
is independent, if I go ahead and run Firefox in here.

10
00:00:38,860 --> 00:00:45,370
You'll either get an error like this, or this user in here will already be logged in in this session

11
00:00:45,370 --> 00:00:45,880
in here.

12
00:00:45,880 --> 00:00:51,790
So even if you go to Gmail, you're not going to be able to have someone else log in to Gmail because

13
00:00:51,790 --> 00:00:54,760
this user will already be logged into Gmail.

14
00:00:54,760 --> 00:00:59,020
So you'll basically just access this account from here.

15
00:00:59,740 --> 00:01:07,390
So what we want to do in this lecture is to run two different Firefox Windows that are completely independent,

16
00:01:07,390 --> 00:01:13,390
so that we can run different login pages, or even the same login page, and serve it to different people.

17
00:01:14,310 --> 00:01:16,170
Fixing this issue is actually very easy.

18
00:01:16,170 --> 00:01:20,640
So first of all, let's close this error and let's close Firefox here.

19
00:01:21,240 --> 00:01:25,920
And instead of running Firefox from the icon we're going to go to the terminal.

20
00:01:26,010 --> 00:01:28,950
And we're going to run Firefox from the terminal.

21
00:01:28,950 --> 00:01:31,980
And this time we're going to run the profile manager.

22
00:01:31,980 --> 00:01:36,450
And to do that we're going to do dash dash profile manager.

23
00:01:37,140 --> 00:01:41,640
So basically we're saying we want to run Firefox, but show me the profile manager first.

24
00:01:41,640 --> 00:01:44,790
Before you start Firefox we're going to hit enter.

25
00:01:45,300 --> 00:01:51,060
So once we do that, as you can see before Firefox starts, you're going to get this screen, which

26
00:01:51,060 --> 00:01:56,400
basically allows you to select which profile you want to start Firefox in.

27
00:01:56,610 --> 00:01:59,910
Alternatively, you can even create a new profile.

28
00:01:59,910 --> 00:02:02,430
And this is exactly what we want to do.

29
00:02:02,430 --> 00:02:07,020
So every time we're going to start Firefox we're going to create a new profile.

30
00:02:07,020 --> 00:02:12,750
And basically each profile is going to be a completely independent instance of Firefox.

31
00:02:13,370 --> 00:02:19,430
So going back to this diagram in here we're going to run one instance of Firefox here with a different

32
00:02:19,430 --> 00:02:20,030
profile.

33
00:02:20,030 --> 00:02:22,670
And then we'll run another profile in here.

34
00:02:22,670 --> 00:02:28,760
And therefore even if these two people both log in to different Gmail accounts, each one of them will

35
00:02:28,760 --> 00:02:30,440
get their own Gmail account.

36
00:02:30,440 --> 00:02:36,560
So if this guy logs in first and this guy goes to Gmail after him, he's not going to be able to access

37
00:02:36,560 --> 00:02:37,670
this guy's Gmail.

38
00:02:37,670 --> 00:02:43,130
Instead, he'll get another login screen, and once he logs in, he's going to get access to his own

39
00:02:43,130 --> 00:02:44,270
Gmail account.

40
00:02:44,330 --> 00:02:49,610
So this way, these browsers are going to be completely independent from each other.

41
00:02:50,380 --> 00:02:55,840
So all we have to do going back to this window is to create a new profile.

42
00:02:56,660 --> 00:02:58,310
We're going to click next.

43
00:02:58,310 --> 00:03:00,530
We're going to give the profile a name.

44
00:03:00,530 --> 00:03:03,230
So let's call it Gmail.

45
00:03:03,980 --> 00:03:06,050
Desktop one.

46
00:03:07,000 --> 00:03:08,920
And we're going to click finish.

47
00:03:09,860 --> 00:03:14,030
As you can see, we have Gmail desktop one is our new profile now.

48
00:03:14,030 --> 00:03:16,880
And in here we're actually going to untick this box.

49
00:03:16,880 --> 00:03:18,620
This is very very important.

50
00:03:18,620 --> 00:03:25,250
When you untick this box Firefox is going to automatically ask us to select the profile that we want

51
00:03:25,250 --> 00:03:29,870
to start with without having to add the profile manager argument.

52
00:03:29,870 --> 00:03:35,510
So now every time we start Firefox it's going to ask us which profile do we want to start Firefox in.

53
00:03:35,510 --> 00:03:39,290
And we can obviously create new profiles, rename them or delete them.

54
00:03:39,620 --> 00:03:42,770
So for now we're going to run it using Gmail Desktop one.

55
00:03:42,770 --> 00:03:44,870
This is the profile that we just created.

56
00:03:44,870 --> 00:03:47,150
And we're going to click on Start Firefox.

57
00:03:48,800 --> 00:03:50,990
So now let's go to gmail.com.

58
00:03:52,020 --> 00:03:53,340
And let's log in.

59
00:03:54,160 --> 00:03:55,690
Fill in the two factor.

60
00:03:56,480 --> 00:03:57,170
And perfect.

61
00:03:57,170 --> 00:03:59,870
As you can see, we're logged in to the Gmail account in here.

62
00:03:59,870 --> 00:04:02,990
So so far so good, but nothing new.

63
00:04:02,990 --> 00:04:06,920
Let's go ahead to the other VNC session that we have in here.

64
00:04:07,160 --> 00:04:11,120
And let's see if we can go to Gmail and get another login screen.

65
00:04:11,420 --> 00:04:16,070
So the goal is that we want to go to Gmail and not be logged in to this account.

66
00:04:16,930 --> 00:04:20,650
So we're going to go ahead and just run Firefox even from the menu in here.

67
00:04:20,650 --> 00:04:26,050
That's going to be fine because we said we want to be asked to select the profile every time we run

68
00:04:26,050 --> 00:04:27,880
Firefox, so that should be fine.

69
00:04:28,450 --> 00:04:29,200
And perfect.

70
00:04:29,200 --> 00:04:31,690
As you can see, Firefox doesn't run straight away.

71
00:04:31,690 --> 00:04:37,090
It actually asks us which profile we want to run, and we can already see the profile that we just created

72
00:04:37,090 --> 00:04:38,590
Gmail desktop one.

73
00:04:38,590 --> 00:04:40,630
So let's create another profile.

74
00:04:42,400 --> 00:04:46,990
And let's call this one Gmail Desktop two.

75
00:04:47,020 --> 00:04:50,320
So this is where we're going to be able to target two people at the same time.

76
00:04:50,320 --> 00:04:56,980
But this could also be for example, Gmail Mobile and then run this VNC session in a mobile orientation.

77
00:04:56,980 --> 00:04:59,050
And this way you'll be able to target mobiles.

78
00:04:59,050 --> 00:05:03,670
So as you can see this is very, very flexible and you can tailor it the way you want.

79
00:05:04,340 --> 00:05:06,380
So anyway we're going to click finish here.

80
00:05:06,380 --> 00:05:09,560
And we have our new profile in here Gmail desktop two.

81
00:05:09,590 --> 00:05:12,410
So we're going to just start Firefox with this profile.

82
00:05:14,610 --> 00:05:18,060
And now if we go to gmail.com.

83
00:05:19,950 --> 00:05:23,610
As you can see, we are not signed in to the account.

84
00:05:23,610 --> 00:05:30,150
So right now this user have already logged in and were able to access his account because he basically

85
00:05:30,150 --> 00:05:31,590
logged in to our computer.

86
00:05:31,590 --> 00:05:34,800
And in here we're able to target another user.

87
00:05:34,800 --> 00:05:37,230
As you can see, they can log in to their own account.

88
00:05:37,230 --> 00:05:41,010
Once they log in, they'll be able to control and do whatever they want to their account.

89
00:05:41,010 --> 00:05:45,150
But at the same time we're going to gain access to their account.

90
00:05:45,150 --> 00:05:51,900
So basically what we're doing right now is we're running two completely different profiles that are

91
00:05:51,900 --> 00:05:56,070
independent to each other on our cloud computer.

92
00:05:57,050 --> 00:06:04,550
So right now we are at the stage where we have two, or we can even have 3 or 4 different browser sessions

93
00:06:04,550 --> 00:06:09,350
or profiles running at the same time without interfering with each other.

94
00:06:09,350 --> 00:06:12,110
So this is another challenge that we solved.

95
00:06:12,110 --> 00:06:18,470
First of all, we managed to allow different people to connect to our server independently and get their

96
00:06:18,470 --> 00:06:19,490
own displays.

97
00:06:19,490 --> 00:06:24,860
And right now we manage to run different browsers that are independent to each other, again without

98
00:06:24,860 --> 00:06:26,210
interfering with each other.

99
00:06:26,210 --> 00:06:34,070
And the last challenge is going to be to have a different, unique URL to each of these browsers with

100
00:06:34,070 --> 00:06:40,190
their login pages so that we can basically give them these links and target them remotely.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:06,770
So, so far we've been configuring our server and improving it to ultimately be able to load different

2
00:00:06,770 --> 00:00:13,700
login pages that can be accessed using different URLs, so that we can target different people that

3
00:00:13,700 --> 00:00:15,110
run different devices.

4
00:00:15,970 --> 00:00:16,720
To do this.

5
00:00:16,750 --> 00:00:22,840
We broke the big problem into smaller problems, and the first challenge was to allow different people

6
00:00:22,840 --> 00:00:27,070
to establish independent VNC connections to the same server.

7
00:00:27,070 --> 00:00:29,080
And we did that at the start.

8
00:00:29,080 --> 00:00:35,170
And then the next challenge was to be able to run different browser profiles so that the browser profiles

9
00:00:35,170 --> 00:00:41,890
do not interfere with each other, so that these guys can log in to different accounts without accessing

10
00:00:41,890 --> 00:00:43,090
each other accounts.

11
00:00:43,090 --> 00:00:52,480
And finally, we need to use Novnc so that we can allow our targets to access our login pages using

12
00:00:52,480 --> 00:00:53,590
unique URLs.

13
00:00:53,590 --> 00:00:57,580
So as you can see, this guy is going to our domain name forward slash Facebook.

14
00:00:57,580 --> 00:00:59,710
And they should get a Facebook login page.

15
00:00:59,710 --> 00:01:04,060
If this guy goes in for Gmail, they should get a Gmail login page.

16
00:01:04,060 --> 00:01:10,120
And this guy's logging in from a mobile so they can go to Gmail mobile or Gmail M, we select whatever

17
00:01:10,120 --> 00:01:14,740
we want in here, and as a result, they should get the mobile version of Gmail and so on.

18
00:01:14,740 --> 00:01:17,140
You can run as many of these as you want.

19
00:01:17,740 --> 00:01:24,430
So basically what we want to do next is to use Novnc instead of remote Repl.

20
00:01:24,430 --> 00:01:30,040
So we've been using remote Repl in here because we were still configuring our servers and still understanding

21
00:01:30,040 --> 00:01:30,820
how it works.

22
00:01:30,820 --> 00:01:37,750
But once we get to run the attack, as you know, we need to go ahead and use Novnc so that our target

23
00:01:37,750 --> 00:01:42,490
can access the login page or the browser using a URL.

24
00:01:43,290 --> 00:01:49,800
Now the problem with Novnc, if you know, previously when we were accessing our login pages, we simply

25
00:01:49,800 --> 00:01:55,170
go to the domain name and we get the login page that is loaded in the browser straight away.

26
00:01:55,410 --> 00:02:02,010
But what we want to do right now is to actually have a unique name in the URL that will point the person

27
00:02:02,010 --> 00:02:04,860
to the right login page, or to the right browser.

28
00:02:06,030 --> 00:02:09,570
So we're actually going to have to use a tokens file.

29
00:02:09,720 --> 00:02:12,720
It might sound a little bit complicated but it's actually very simple.

30
00:02:12,720 --> 00:02:15,690
So let's go ahead and see how we're going to do that.

31
00:02:15,690 --> 00:02:19,890
We're going to go to the terminal and we're going to create a new file.

32
00:02:19,890 --> 00:02:23,670
So I'm going to use nano to actually create the file and edit it.

33
00:02:23,670 --> 00:02:26,130
And I'm going to call the file tokens.

34
00:02:26,130 --> 00:02:27,270
I'm going to hit enter.

35
00:02:27,270 --> 00:02:32,700
And as you can see I get an empty file because this is a new file that we just created.

36
00:02:32,700 --> 00:02:39,390
And in this file we're going to specify the name that we want the user to put in here after the forward

37
00:02:39,390 --> 00:02:39,750
slash.

38
00:02:39,750 --> 00:02:42,210
So the name that you have in here in yellow.

39
00:02:42,480 --> 00:02:46,020
So for example we want to have a Facebook login page.

40
00:02:46,020 --> 00:02:47,850
So I'm going to type Facebook.

41
00:02:48,000 --> 00:02:53,910
And I want to run this Facebook login page on the first VNC display.

42
00:02:53,910 --> 00:02:57,570
So the one that is running on the first port on 5901.

43
00:02:57,570 --> 00:03:01,050
And therefore we're going to say this is going to run on local host.

44
00:03:01,050 --> 00:03:08,640
So on the current computer I'm already logged in to my cloud computer and that is running on port 5901.

45
00:03:09,220 --> 00:03:16,960
Next, I want to have a Gmail login page, and that one is going to run on local host on five nine,

46
00:03:16,960 --> 00:03:19,570
zero, and this list can go on.

47
00:03:19,570 --> 00:03:23,410
So for example again you can do Instagram if you want or WhatsApp.

48
00:03:23,410 --> 00:03:25,450
And we covered how you can bypass WhatsApp.

49
00:03:25,450 --> 00:03:31,300
Again you're going to do local host colon the port that your VNC display is running on.

50
00:03:32,760 --> 00:03:41,190
So basically this part in here represents what we want the user to type after the domain name.

51
00:03:41,190 --> 00:03:46,200
And the rest of it basically points the user to the VNC connection.

52
00:03:46,200 --> 00:03:52,500
So we're going to be running Facebook on the first display running on port 5901.

53
00:03:52,500 --> 00:03:57,690
And we're going to be running Gmail on the VNC session that is running on five, nine, zero, two.

54
00:03:57,690 --> 00:04:00,360
And like I said, you can run multiple VNC sessions.

55
00:04:00,360 --> 00:04:01,980
They're going to go on the next port.

56
00:04:01,980 --> 00:04:05,640
So the third VNC session you'll run is going to be on five, nine zero, three.

57
00:04:05,640 --> 00:04:09,570
And again you can specify whatever website you want to run on that.

58
00:04:09,870 --> 00:04:15,270
So to quit this and save it we do control x y enter.

59
00:04:15,630 --> 00:04:20,610
So now if I do ls in my current working directory, as you can see I have this is the file.

60
00:04:20,610 --> 00:04:21,690
It's the tokens file.

61
00:04:21,690 --> 00:04:23,340
And right now I am in home.

62
00:04:23,340 --> 00:04:23,700
Kali.

63
00:04:23,700 --> 00:04:25,710
Just so that you know where is this file.

64
00:04:25,740 --> 00:04:28,230
Because we're going to need to use it in the next step.

65
00:04:28,230 --> 00:04:32,250
But first we actually need to get our IP to get the IP.

66
00:04:32,250 --> 00:04:34,650
We're going to run the ifconfig command.

67
00:04:34,650 --> 00:04:41,580
This will display the current interfaces on the computer and information about them including the IP

68
00:04:41,580 --> 00:04:42,900
as you can see in here.

69
00:04:42,900 --> 00:04:44,850
And we're going to need this for the next command.

70
00:04:44,850 --> 00:04:48,240
So you want to copy this and just keep it for the next command.

71
00:04:48,240 --> 00:04:57,120
Now usually in order to expose the vnp the VNC server and make it accessible using a URL, we use no

72
00:04:57,120 --> 00:05:00,690
VNC and we've been using it in all of the previous lectures.

73
00:05:00,690 --> 00:05:07,020
Now, no VNC cannot be used to have multiple URLs, as you can see in here.

74
00:05:07,020 --> 00:05:10,110
So we're going to be using a program called WebSocket file.

75
00:05:10,110 --> 00:05:15,660
And this is actually a program that no VNC relies on and uses itself.

76
00:05:15,750 --> 00:05:21,210
We're using the dash dash web argument to tell it to use no VNC in here.

77
00:05:21,210 --> 00:05:29,130
And then we're using the dash dash target config to specify the location of the tokens file that we

78
00:05:29,130 --> 00:05:32,070
just created in the previous step in home Kali.

79
00:05:32,070 --> 00:05:37,620
And it's called tokens, and we are giving it the full path to the location of this file.

80
00:05:38,660 --> 00:05:42,290
The rest of the command is actually pretty similar to the Novnc command.

81
00:05:42,290 --> 00:05:46,310
So we're using the dash dash cert to give it our full chain certificate.

82
00:05:46,310 --> 00:05:50,000
We're using the dash dash key to give it our private key.

83
00:05:50,000 --> 00:05:57,410
And finally we're giving it the IP that we can get from here in the ifconfig command followed by the

84
00:05:57,410 --> 00:05:57,830
port.

85
00:05:57,830 --> 00:06:00,350
And as you know we want to use Https.

86
00:06:00,350 --> 00:06:03,380
And that's why we're using the 443 port.

87
00:06:03,920 --> 00:06:05,180
We're going to hit enter.

88
00:06:05,180 --> 00:06:06,050
And perfect.

89
00:06:06,050 --> 00:06:08,510
As you can see it's running as expected.

90
00:06:08,600 --> 00:06:13,040
It's telling us that it's listening on the IP and the port that we selected.

91
00:06:13,040 --> 00:06:16,340
It is able to locate Novnc with no problems.

92
00:06:16,340 --> 00:06:21,410
It's running with SSL and TLS support and it is able to read my token file.

93
00:06:21,410 --> 00:06:23,420
So all of that is perfect.

94
00:06:23,420 --> 00:06:25,790
So I'm going to go ahead to my remote Repl.

95
00:06:25,790 --> 00:06:28,460
As you can see in here we've already used this.

96
00:06:28,460 --> 00:06:30,620
So I'm going to open up my terminal.

97
00:06:30,980 --> 00:06:34,070
We're going to do Firefox ESR.

98
00:06:34,100 --> 00:06:36,170
We're going to do dash dash kiosk.

99
00:06:36,170 --> 00:06:41,330
And we're going to load https facebook.com.

100
00:06:43,570 --> 00:06:46,120
And we're going to keep it at the same profile.

101
00:06:46,120 --> 00:06:47,770
It is saying Gmail, but that's fine.

102
00:06:47,770 --> 00:06:50,590
It's just a profile name and perfect.

103
00:06:50,590 --> 00:06:54,100
Now we have it running in kiosk mode loading Facebook login page.

104
00:06:54,100 --> 00:06:55,240
So that is perfect.

105
00:06:55,240 --> 00:06:58,510
And let's go ahead to the second instance in here.

106
00:06:58,810 --> 00:07:03,580
And we're going to run Firefox again in kiosk mode.

107
00:07:03,580 --> 00:07:07,180
And this time we're going to load https.

108
00:07:07,940 --> 00:07:15,830
Gmail.com, because this is going to be the Gmail page, and we're going to load it with the first profile.

109
00:07:17,540 --> 00:07:18,260
And perfect.

110
00:07:18,260 --> 00:07:23,000
We have the Gmail login page on this profile, so we actually don't need the remote Repl anymore.

111
00:07:23,000 --> 00:07:27,560
You can keep it connected so that you can quickly come in and access it when the target logs into their

112
00:07:27,560 --> 00:07:30,710
account, but you don't really need to use it anymore.

113
00:07:30,740 --> 00:07:34,070
The goal now is to see if our configuration works.

114
00:07:34,070 --> 00:07:40,010
So for this we have to let's go to a normal web browser and let's go to the target.

115
00:07:40,130 --> 00:07:45,350
So we're going to have to go to my domain which is Zacks.com forward slash.

116
00:07:45,350 --> 00:07:48,050
And we're going to put a question mark.

117
00:07:48,050 --> 00:07:51,980
We're going to set the path to nothing.

118
00:07:52,870 --> 00:07:58,990
And then token is going to be the token name that we specified in the token file.

119
00:07:59,020 --> 00:08:01,960
So remember in the token file we had Facebook and Gmail.

120
00:08:01,960 --> 00:08:08,800
So if we want access to Facebook page it's going to take us to the VNC session running on 5901 on the

121
00:08:08,800 --> 00:08:10,450
first display.

122
00:08:10,450 --> 00:08:12,490
So if we hit enter now.

123
00:08:13,220 --> 00:08:19,040
As you can see, we're getting the login page that is loaded on the first session in here, as you can

124
00:08:19,040 --> 00:08:19,610
see.

125
00:08:19,940 --> 00:08:25,460
And then to get the login page running on the second session, the Gmail one, if you remember, in

126
00:08:25,460 --> 00:08:30,140
the tokens file we set the name of this token to Gmail.

127
00:08:30,140 --> 00:08:32,780
So again we're going to go to the browser.

128
00:08:32,780 --> 00:08:35,600
We're going to have the exact same URL.

129
00:08:35,600 --> 00:08:39,230
But this time we're going to say Gmail and perfect.

130
00:08:39,230 --> 00:08:43,520
As you can see we are loading the second VNC session.

131
00:08:43,520 --> 00:08:50,930
So using this method you can actually run as many VNC connections as you want.

132
00:08:50,930 --> 00:08:56,420
You can run as many login pages as you want because all of them run in different profiles, and each

133
00:08:56,420 --> 00:08:59,030
one of them can have its own configuration.

134
00:08:59,030 --> 00:09:01,220
So you can run a mobile friendly version.

135
00:09:01,220 --> 00:09:04,760
As I showed you previously, you can have WhatsApp running on the other one.

136
00:09:04,760 --> 00:09:09,920
You can have Gmail running on the other one, and you can target the same person or different people.

137
00:09:09,920 --> 00:09:13,760
And each one of these is going to have its own URL.

138
00:09:13,760 --> 00:09:15,920
And as you can know, you can customize the URL.

139
00:09:15,920 --> 00:09:17,270
We covered that previously.

140
00:09:17,270 --> 00:09:21,080
And you can customize this bit in here using the tokens file.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: Hacking Web Browsers

1
00:00:00,080 --> 00:00:06,110
So far, we covered how to steal login information to any website and from any device, even if the

2
00:00:06,110 --> 00:00:09,860
website uses two factor or multifactor authentication.

3
00:00:09,860 --> 00:00:16,970
And we did this using websites that look identical to the original websites with Https enabled and with

4
00:00:16,970 --> 00:00:18,290
a proper domain name.

5
00:00:18,290 --> 00:00:24,140
So as a result, we can steal the login information to any website using a single link.

6
00:00:24,860 --> 00:00:25,850
In this section.

7
00:00:25,850 --> 00:00:31,190
We're going to take this even further, and I'm going to show you how to hack the whole browser that

8
00:00:31,190 --> 00:00:34,550
loads our phishing pages or malicious websites.

9
00:00:34,580 --> 00:00:40,250
To do this, I'm going to show you how to embed malicious or evil code into these websites that will

10
00:00:40,250 --> 00:00:41,840
allow us to hack the browser.

11
00:00:41,840 --> 00:00:45,740
It will allow us to execute any type of JavaScript on that browser.

12
00:00:45,740 --> 00:00:50,660
It will give us more information about the targets, such as their IP address, which we can use to

13
00:00:50,660 --> 00:00:51,890
get their location.

14
00:00:51,890 --> 00:00:58,160
It will also allow us to access the system resources, such as their webcam and their GPS coordinates,

15
00:00:58,160 --> 00:01:00,560
which will give us their exact location.

16
00:01:00,560 --> 00:01:07,700
We'll also be able to steal login information from their computer and potentially gain full remote access

17
00:01:07,700 --> 00:01:09,080
to their computer.

18
00:01:09,080 --> 00:01:14,090
At the end, I'm going to teach you a little bit more PHP and JavaScript programming, and we're going

19
00:01:14,090 --> 00:01:20,810
to create our own custom malicious page that will allow us to access the camera and the exact location

20
00:01:20,810 --> 00:01:22,520
of the target that loads it.

21
00:01:22,820 --> 00:01:27,980
And finally, at the end of this section, I'm going to teach you some URL manipulation tricks that

22
00:01:27,980 --> 00:01:34,460
will make our websites or our phishing pages more believable and more trustworthy, ultimately increasing

23
00:01:34,460 --> 00:01:37,070
the chances of our targets interacting with them.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,540
In this lecture, I'd like to introduce you to a really cool framework called beef.

2
00:00:06,020 --> 00:00:09,980
Beef is short for the Browser Exploitation Framework.

3
00:00:10,040 --> 00:00:17,420
It allows us to run a number of attacks on hooked browsers that would allow us to further exploit the

4
00:00:17,420 --> 00:00:24,230
target system, to steal passwords, or even gain full access or full control over the system.

5
00:00:24,680 --> 00:00:31,190
So we already have a Kali machine in here, but unfortunately beef is not pre-installed on it.

6
00:00:31,190 --> 00:00:35,900
So to install beef, we're going to do sudo first to run the command as root.

7
00:00:35,900 --> 00:00:39,740
And we're going to do apt update to update the resources.

8
00:00:40,500 --> 00:00:47,010
And once it's done, let's clear the screen and we're going to do sudo to again run the command as root.

9
00:00:47,010 --> 00:00:50,670
And we're going to do apt install to install a package.

10
00:00:50,670 --> 00:00:56,550
And the package that we want to install is called beef dash x.

11
00:00:56,550 --> 00:01:01,830
So we're using apt, the package manager that comes with Debian distros like Kali.

12
00:01:02,520 --> 00:01:07,110
We're telling it that we want to install a program called beef X.

13
00:01:07,650 --> 00:01:08,970
I'm going to hit enter.

14
00:01:09,600 --> 00:01:15,060
We're going to say yes, we want to install it and you just want to give it its time to download and

15
00:01:15,060 --> 00:01:16,680
install beef for you.

16
00:01:17,250 --> 00:01:21,030
Now the installation is complete, we're going to clear the screen again.

17
00:01:21,030 --> 00:01:28,830
And we're going to start beef by simply type in sudo to run the command as root service to run a service.

18
00:01:28,830 --> 00:01:32,730
And the service name is beef dash X.

19
00:01:32,730 --> 00:01:37,320
And we want to start this service we're going to hit enter.

20
00:01:38,160 --> 00:01:43,020
Let's double check the status of the service to make sure that everything is running properly.

21
00:01:43,020 --> 00:01:48,330
So we're going to do sudo service beef dash x.

22
00:01:49,380 --> 00:01:50,340
Status.

23
00:01:51,260 --> 00:01:53,780
And as you can see, it's actually saying failed.

24
00:01:53,780 --> 00:01:59,510
So it didn't start because we shouldn't be using the default username and password.

25
00:01:59,510 --> 00:02:03,770
It's also telling us that we can change the password in this file right here.

26
00:02:04,250 --> 00:02:07,280
So thank you very much for telling us that we're going to copy it.

27
00:02:08,070 --> 00:02:10,860
We're going to quit by pressing the cue button.

28
00:02:11,280 --> 00:02:17,880
We're going to clear the screen, and I'm going to use a terminal text editor called Nano so that I

29
00:02:17,880 --> 00:02:22,200
can modify text files within my terminal window in here.

30
00:02:22,740 --> 00:02:26,910
And I should actually type sudo before it so I can open it as root.

31
00:02:26,910 --> 00:02:31,890
And then I'm going to paste the file that I want to open using this text editor.

32
00:02:32,100 --> 00:02:34,830
So nano is the name of the text editor.

33
00:02:34,830 --> 00:02:40,140
And the file that I want to open is this file right here I'm going to hit enter.

34
00:02:40,700 --> 00:02:44,930
And this is loading up the configuration file for beef.

35
00:02:45,560 --> 00:02:48,110
All we want to do right now is change the password.

36
00:02:48,110 --> 00:02:54,260
Because as you saw earlier, the service failed to start because it was starting with the default password.

37
00:02:55,020 --> 00:03:00,000
So we're scrolling down and as you can see, the default username is beef.

38
00:03:00,000 --> 00:03:02,490
And the default password is also beef.

39
00:03:02,490 --> 00:03:04,350
And you want to change that to something else.

40
00:03:04,350 --> 00:03:06,990
So we're going to change it to beef 123.

41
00:03:07,470 --> 00:03:12,750
Now you could actually navigate through this text editor using the shortcuts in here.

42
00:03:13,290 --> 00:03:16,260
So now that I made my changes I want to exit.

43
00:03:16,260 --> 00:03:19,770
And to exit you have to press control X from my keyboard.

44
00:03:20,160 --> 00:03:23,760
Now it's asking me do I want to save the modified buffer?

45
00:03:23,760 --> 00:03:25,560
Yes, I do want to save the file.

46
00:03:25,560 --> 00:03:28,110
So I'm going to press Y from my keyboard.

47
00:03:28,110 --> 00:03:30,960
And then it's asking me the file name to overwrite.

48
00:03:30,960 --> 00:03:33,180
So are we keeping it called the same name?

49
00:03:33,180 --> 00:03:35,040
Yes I want to keep it the same name.

50
00:03:35,040 --> 00:03:36,450
So I'm going to hit enter.

51
00:03:37,050 --> 00:03:37,800
And perfect.

52
00:03:37,800 --> 00:03:39,390
Now the file is saved.

53
00:03:39,390 --> 00:03:45,870
So let's go ahead and run beef again using the exact same command that we used before service beef start.

54
00:03:46,110 --> 00:03:47,430
We're going to hit enter.

55
00:03:47,880 --> 00:03:53,580
And let's do the status again to make sure that everything got executed properly and perfect.

56
00:03:53,580 --> 00:03:56,670
As you can see it's telling us that the service is running.

57
00:03:57,030 --> 00:04:05,220
So now beef is running on my cloud Amazon computer and I can actually connect to it from any computer

58
00:04:05,220 --> 00:04:11,040
with a web browser, whether it's a normal computer, a phone, a tablet, it doesn't really matter

59
00:04:11,040 --> 00:04:14,190
because the beef control panel is web based.

60
00:04:14,190 --> 00:04:19,980
So all I need is a web browser, and beef itself is actually running on the cloud computer.

61
00:04:19,980 --> 00:04:22,260
It's not really running on my local machine.

62
00:04:22,260 --> 00:04:25,140
That's why I can simply use the phone to connect to it.

63
00:04:25,470 --> 00:04:31,200
And all I need is the IP of the machine in which beef is running on, which is this IP.

64
00:04:31,620 --> 00:04:37,560
We're going to have to paste it in here in the URL bar, and put the port that beef runs on, which

65
00:04:37,560 --> 00:04:38,820
is port 3000.

66
00:04:38,970 --> 00:04:42,840
Now this is going to send an inbound connection to this computer.

67
00:04:42,840 --> 00:04:49,200
When the user puts call on 3000 in their URL bar, they're actually going to get to the IP.

68
00:04:49,230 --> 00:04:51,630
The IP is going to check or the computer is going to check.

69
00:04:51,630 --> 00:04:53,700
Do I have anything running on port 3000?

70
00:04:53,700 --> 00:04:57,930
Yes I do, I have beef running on it and therefore they're going to get them to beef.

71
00:04:58,380 --> 00:05:03,630
Therefore, just like what we seen earlier, you're going to have to modify the security settings of

72
00:05:03,630 --> 00:05:04,650
that computer.

73
00:05:04,650 --> 00:05:06,450
We're going to click on the group.

74
00:05:06,960 --> 00:05:09,180
We're going to edit the inbound rules.

75
00:05:09,450 --> 00:05:14,160
And we're going to have to allow connections to port 3000.

76
00:05:15,170 --> 00:05:20,120
Also, we're going to set the IP to 0000 similar to what we did earlier.

77
00:05:20,120 --> 00:05:21,890
We're going to save the rules.

78
00:05:22,340 --> 00:05:26,810
And now that everything is saved we're going to go back here and hit enter.

79
00:05:27,020 --> 00:05:29,390
And as you can see we're getting the web server.

80
00:05:29,390 --> 00:05:36,980
Now I actually need to navigate to the login page of beef which is located at forward slash UI forward

81
00:05:36,980 --> 00:05:38,000
slash panel.

82
00:05:39,900 --> 00:05:40,620
And perfect.

83
00:05:40,620 --> 00:05:43,140
As you can see, we have the login page for beef.

84
00:05:43,140 --> 00:05:48,360
I'm going to log in with the username beef and the password that we just set in the text file.

85
00:05:48,360 --> 00:05:51,810
So it's beef 123 I'm going to hit enter.

86
00:05:53,060 --> 00:05:53,750
And perfect.

87
00:05:53,780 --> 00:05:56,000
Now I have the beef control panel.

88
00:05:56,270 --> 00:06:01,370
The main thing you can see here on the left is the online and the offline browsers.

89
00:06:01,370 --> 00:06:07,430
In the online browsers, you'll see the browsers that are hooked to beef right now that you can control.

90
00:06:07,430 --> 00:06:13,460
And in the offline browsers you'll see the browsers that you previously were able to control.

91
00:06:13,460 --> 00:06:17,090
So browsers that you previously hooked to beef.

92
00:06:17,910 --> 00:06:25,140
Now, in order to hook a browser to beef and be able to control it and run commands on it, you have

93
00:06:25,140 --> 00:06:29,880
to get that browser to execute a specific JavaScript code.

94
00:06:29,880 --> 00:06:35,070
For the sake of simplicity, we're actually just going to use the demo page that comes with beef.

95
00:06:35,070 --> 00:06:38,970
So if you click on this page, the browser will get hooked to it.

96
00:06:38,970 --> 00:06:43,620
Now I don't want to hook this current browser because this is the browser that we're using to control

97
00:06:43,620 --> 00:06:44,430
the target.

98
00:06:44,970 --> 00:06:47,880
So I'm going to right click this page and copy the link.

99
00:06:47,880 --> 00:06:52,020
And I'm going to load that page in here in the Target windows computer.

100
00:06:53,970 --> 00:06:57,420
Now, as you can see, you're going to get a normal page keeping in mind.

101
00:06:57,420 --> 00:07:02,700
Like I said, this could be a very attractive, nice page that the target would want to press on.

102
00:07:02,700 --> 00:07:05,460
And it doesn't even need to have the 3000 in here.

103
00:07:05,460 --> 00:07:11,040
Since this is running on the cloud, you could even have your own domain name pointing to this IP.

104
00:07:11,430 --> 00:07:14,340
So let's go back to the control panel and perfect.

105
00:07:14,340 --> 00:07:17,010
As you can see, we have a hooked browser.

106
00:07:17,010 --> 00:07:21,180
If we click on it we can get the information about that browser.

107
00:07:21,180 --> 00:07:24,870
The commands tab is the one that we're going to be using the most.

108
00:07:24,870 --> 00:07:30,690
Again, keeping things simple, let's just send an alert to make sure that everything is running as

109
00:07:30,690 --> 00:07:31,650
expected.

110
00:07:31,920 --> 00:07:34,350
So we're going to create an alert dialog.

111
00:07:34,350 --> 00:07:35,460
Keep it default.

112
00:07:35,460 --> 00:07:40,350
Just click on execute and let's go to the target and perfect.

113
00:07:40,350 --> 00:07:43,110
As you can see the alert code got executed.

114
00:07:43,110 --> 00:07:50,250
This is just proof to us that right now this browser is hooked and we can execute any command that beef

115
00:07:50,250 --> 00:07:51,840
allows us to execute.

116
00:07:52,110 --> 00:07:56,910
There are a few things that you need to learn to unleash the full potential of beef.

117
00:07:56,910 --> 00:08:02,850
I will be covering these things in the future, but let me show you what you'll be able to do once you

118
00:08:02,850 --> 00:08:04,710
go through the next few lectures.

119
00:08:04,830 --> 00:08:11,400
As you can see, I am getting a website that uses Https and we see the lock icon beside it.

120
00:08:11,400 --> 00:08:16,680
We see a normal domain name that is not suspicious at all, because it sounds similar to the target

121
00:08:16,680 --> 00:08:19,320
website, which is the security.org.

122
00:08:19,320 --> 00:08:24,870
And you can see that the website in here is pretty identical to the original website.

123
00:08:24,870 --> 00:08:30,690
The thing is, this website is actually malicious, and it actually contains code that will hack this

124
00:08:30,690 --> 00:08:33,420
browser and link it to beef.

125
00:08:33,420 --> 00:08:39,450
And as you can see in beef in here under online browsers, I can see that I have a new computer.

126
00:08:39,450 --> 00:08:46,710
And if I click on this computer, you can see straight away I get a lot of information about this computer,

127
00:08:46,710 --> 00:08:51,000
such as the browser that it's using, such as its IP.

128
00:08:51,000 --> 00:08:57,510
And this IP can actually be used to get a very good approximation of the location of this device.

129
00:08:57,510 --> 00:09:01,980
And like I said, this will work on all devices that have a web browser.

130
00:09:01,980 --> 00:09:05,910
So it will work on phones, on tablets, on Android or on iOS.

131
00:09:05,940 --> 00:09:10,230
It really doesn't matter as long as they have a web browser, this will work on them.

132
00:09:10,650 --> 00:09:14,970
So straight away you're going to be able to get the location of the device using the IP.

133
00:09:14,970 --> 00:09:23,490
So you can just go ahead and look for find IP location, for example, and you're going to get a lot

134
00:09:23,490 --> 00:09:24,090
of websites.

135
00:09:24,090 --> 00:09:29,460
And once you put the IP in there, you're actually going to get a very good approximation of the location

136
00:09:29,460 --> 00:09:30,480
of this person.

137
00:09:30,930 --> 00:09:33,090
So we haven't even done any hacking.

138
00:09:33,090 --> 00:09:36,960
And we're able to trace and find the location of the target device.

139
00:09:37,260 --> 00:09:43,920
Now if you go on the commands, you're going to see that you have a large number of categories, and

140
00:09:43,920 --> 00:09:48,270
each one of them has a large number of commands that can be very useful.

141
00:09:48,270 --> 00:09:54,120
And that could allow you to potentially gain full remote access on the target computer.

142
00:09:54,570 --> 00:09:57,270
So you have simple things like text, voice.

143
00:09:57,270 --> 00:10:00,480
You have things that will get you the geolocation as well.

144
00:10:00,480 --> 00:10:05,790
So if you look for Geo, you're going to get a lot of plugins that allow you to get the location of

145
00:10:05,790 --> 00:10:06,870
the target as well.

146
00:10:06,870 --> 00:10:08,520
But we've already seen that.

147
00:10:08,520 --> 00:10:15,300
For example, you can also go back to the social engineering my favorite category in here, you can

148
00:10:15,300 --> 00:10:17,940
see that you can display a fake notification bar.

149
00:10:17,940 --> 00:10:20,400
For example we can select for Firefox.

150
00:10:20,400 --> 00:10:25,350
And in here you can tell the target user that there is an additional plugin is needed.

151
00:10:25,350 --> 00:10:29,640
Or for example an update is needed.

152
00:10:29,640 --> 00:10:31,170
You can make this more believable.

153
00:10:31,170 --> 00:10:35,790
I'm just doing it real quickly and put a link to a backdoor in here.

154
00:10:35,790 --> 00:10:41,220
Once you click on execute, the target user is going to get a notification telling them that they need

155
00:10:41,220 --> 00:10:47,400
to install a plugin, or you can tell them that they need to install an update in this fake notification

156
00:10:47,400 --> 00:10:47,970
bar in here.

157
00:10:47,970 --> 00:10:53,610
For example, once they click install the plugin or the update, your back there will be downloaded

158
00:10:53,610 --> 00:10:58,200
which will allow you to hack the target computer and control it remotely.

159
00:10:58,740 --> 00:11:02,190
There are a number of exploits that would get you remote access.

160
00:11:02,190 --> 00:11:04,140
If the target is not patched.

161
00:11:04,500 --> 00:11:07,950
You could use the pretty theft command, which I really like.

162
00:11:07,950 --> 00:11:14,010
That will basically dim the window and ask the user to log in to the social media network that you select.

163
00:11:14,010 --> 00:11:19,830
From here, you can even set a custom logo for any other social media platforms that are not listed

164
00:11:19,830 --> 00:11:20,340
here.

165
00:11:20,340 --> 00:11:25,950
But if I click on execute, for example, you'll see the screen in here will dim, and the user is going

166
00:11:25,950 --> 00:11:30,450
to be told that their Facebook session timed out, and it's going to ask them to log in to Facebook.

167
00:11:31,680 --> 00:11:33,120
If they put their user name.

168
00:11:33,120 --> 00:11:41,490
For example, test at test.com and the password 123456 and click on log in.

169
00:11:41,520 --> 00:11:47,280
If we go back in here and click on the command, you can see we capture the username and the password.

170
00:11:47,580 --> 00:11:52,140
So as you can see there is so many useful commands in here.

171
00:11:52,140 --> 00:11:59,370
And the main thing is that you need the target user to not feel suspicious when they load this page,

172
00:11:59,370 --> 00:12:05,460
and they're not going to feel suspicious this time because we're loading the page using https with the

173
00:12:05,460 --> 00:12:12,480
lock icon with a real domain name, with a cloned website that looks very identical to the original

174
00:12:12,480 --> 00:12:13,200
website.

175
00:12:13,230 --> 00:12:18,960
Now I'll be showing you how to get to the stage step by step, so don't worry about it.

176
00:12:18,960 --> 00:12:23,850
I just wanted to show you how useful this can be and one more time.

177
00:12:23,850 --> 00:12:29,160
The coolest thing about this is the fact that beef is always going to be running on the server.

178
00:12:29,160 --> 00:12:35,430
People can connect to it and get hooked whenever you want, and you as a hacker can connect to it whenever

179
00:12:35,430 --> 00:12:41,010
you want from any computer, whether it's a computer, a phone, or a tablet, because the heavy lifting

180
00:12:41,010 --> 00:12:45,750
and beef is actually running on the cloud server, not on your own computer.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:06,590
Last time after we installed beef, we managed to hook a target windows computer right here by loading

2
00:00:06,590 --> 00:00:08,960
the demo page that we have in here.

3
00:00:08,960 --> 00:00:13,490
And this demo page is hosted on our IP colon 3000.

4
00:00:13,490 --> 00:00:19,400
Because beef is running on port 3000, it already contains beef hook because it's a beef demo page.

5
00:00:19,400 --> 00:00:22,190
And therefore we managed to hook the target to beef.

6
00:00:22,220 --> 00:00:27,650
Now this is all great, but we just did it in order to test that our configuration is right and that

7
00:00:27,650 --> 00:00:28,340
beef works.

8
00:00:28,340 --> 00:00:34,820
But in a real life scenario this is not good because first of all, the URL looks very suspicious.

9
00:00:34,820 --> 00:00:40,040
And second, you can't just send a page that looks like this and expect the target to run it.

10
00:00:40,040 --> 00:00:44,450
And even if they do click it, once they click it, they know that there is something wrong with this.

11
00:00:44,540 --> 00:00:50,390
So in a real life scenario, you want a social engineer them to opening a page that might be interesting

12
00:00:50,420 --> 00:00:50,840
to them.

13
00:00:50,840 --> 00:00:53,780
So it could be a page that contains useful articles.

14
00:00:53,780 --> 00:01:00,110
It could be a page of a website that they're interested in, depending on whatever the target is interested

15
00:01:00,110 --> 00:01:06,020
in, you need to send them something that they are likely to click and not get suspicious when they

16
00:01:06,020 --> 00:01:07,220
load that page.

17
00:01:07,220 --> 00:01:09,770
So that's very open and it depends on your target.

18
00:01:09,770 --> 00:01:14,690
But I'm going to show you how to first of all create a replica of any page.

19
00:01:14,690 --> 00:01:19,070
And then we will talk about how you can embed beef's code within that page.

20
00:01:19,070 --> 00:01:20,300
It's very very simple.

21
00:01:20,300 --> 00:01:21,950
So let me show you how to do it.

22
00:01:22,490 --> 00:01:25,280
So first of all I'm going to open Firefox.

23
00:01:25,430 --> 00:01:29,720
And we're going to go to the page that we think that the target would be interested in.

24
00:01:29,720 --> 00:01:34,100
And we're going to assume that the target is interested in cybersecurity.

25
00:01:34,100 --> 00:01:40,970
So we're going to create a phishing page that looks exactly like the security or a replica of the security.

26
00:01:40,970 --> 00:01:44,270
And to do this in Firefox is actually very, very simple.

27
00:01:44,270 --> 00:01:46,880
All you have to do is go to file.

28
00:01:47,890 --> 00:01:55,930
Save page as and you want to make sure you select all files in here when you're downloading the page.

29
00:01:55,930 --> 00:01:57,460
And you can leave this.

30
00:01:57,460 --> 00:01:58,570
This is the name of the page.

31
00:01:58,570 --> 00:02:00,370
You can leave it to whatever you want.

32
00:02:00,370 --> 00:02:02,050
And we're going to click on save.

33
00:02:02,050 --> 00:02:08,410
Now if we go to my finder which I have it right here, I'm going to go to the directory where I downloaded

34
00:02:08,410 --> 00:02:08,530
it.

35
00:02:08,530 --> 00:02:12,370
So I downloaded it to a directory in my downloads and it's called test.

36
00:02:12,370 --> 00:02:14,440
And we have the page right here.

37
00:02:14,620 --> 00:02:16,960
Now if we double click this page.

38
00:02:17,940 --> 00:02:21,600
You'll see that it is a replica of the security.

39
00:02:22,140 --> 00:02:27,180
Once this is downloaded, you want to upload it to your cloud server, similar to what we did before

40
00:02:27,180 --> 00:02:27,720
as well.

41
00:02:27,720 --> 00:02:35,160
And I'm already in var ww HTML, my web root and I'm already in my downloads test.

42
00:02:35,160 --> 00:02:38,820
So now if I right click this file and click on upload.

43
00:02:40,080 --> 00:02:46,230
As you can see, the file gets uploaded to my cloud install of Kali.

44
00:02:47,740 --> 00:02:51,760
We're going to right click the index file and we're going to delete it.

45
00:02:53,360 --> 00:02:57,020
And then we're going to right click this file the z security file.

46
00:02:57,620 --> 00:02:59,150
We're going to rename it.

47
00:03:00,330 --> 00:03:04,350
To index dot HTML, so it loads by default.

48
00:03:04,350 --> 00:03:07,200
We know all this by now from the previous lectures.

49
00:03:07,200 --> 00:03:13,350
So now if we go back to my website, as you can see we have the default page now.

50
00:03:13,350 --> 00:03:15,000
But if I refresh it.

51
00:03:17,290 --> 00:03:17,800
Perfect.

52
00:03:17,800 --> 00:03:25,030
Now I have a replica of the security running on my Kali install on the cloud, so anybody that has access

53
00:03:25,030 --> 00:03:32,500
to the internet will be able to load my Kali install by simply inputting the IP of my cloud instance.

54
00:03:33,740 --> 00:03:39,980
So right now we have a replica of a page that we're assuming that the target person is very interested

55
00:03:39,980 --> 00:03:40,310
in.

56
00:03:40,310 --> 00:03:44,840
So from here onwards, you could embed evil code within this page.

57
00:03:44,840 --> 00:03:51,320
So when we send it to the target user, instead of them seeing a demo page like this one that looks

58
00:03:51,320 --> 00:03:57,650
very suspicious, they will actually see a website that they are interested in and they trust, similar

59
00:03:57,650 --> 00:03:59,210
to the security right here.

60
00:03:59,210 --> 00:04:05,750
But at the same time, our hook code is going to be executed in the background, allowing us to remotely

61
00:04:05,750 --> 00:04:08,450
hook their browser and execute commands on it.

62
00:04:09,080 --> 00:04:10,940
Doing this is very, very simple.

63
00:04:10,940 --> 00:04:16,400
We're going to go back to FileZilla and we're going to go to the index.html, because that is the page

64
00:04:16,400 --> 00:04:18,200
that is being served to the target.

65
00:04:18,200 --> 00:04:21,260
We're going to right click it and we're going to click on edit.

66
00:04:21,560 --> 00:04:28,190
This will download this index file for you and allow you to edit it using your default text editor.

67
00:04:28,460 --> 00:04:31,970
Now don't get overwhelmed with the amount of code that you see in here.

68
00:04:31,970 --> 00:04:35,090
It's the code that is rendering the target web page.

69
00:04:35,090 --> 00:04:37,790
So it's the code that is rendering this page right here.

70
00:04:37,790 --> 00:04:40,400
And we don't really need to modify any of that.

71
00:04:40,400 --> 00:04:44,630
All you want to do is I like to embed it after the head tag.

72
00:04:44,630 --> 00:04:46,430
So you want to look for the head tag.

73
00:04:46,430 --> 00:04:49,070
So just control find head.

74
00:04:49,070 --> 00:04:50,600
You can see the head tag.

75
00:04:50,960 --> 00:04:54,260
This is a really good place for you to embed your JavaScript.

76
00:04:54,500 --> 00:04:58,460
So what I'm going to hit enter twice just to give me some space.

77
00:04:58,460 --> 00:05:02,150
And we're going to put the beef hook code in here.

78
00:05:02,150 --> 00:05:07,730
And all you have to do as shown in my other courses, is simply type script.

79
00:05:09,440 --> 00:05:10,340
S.r.c.

80
00:05:10,760 --> 00:05:14,780
And then the link to the hocus page.

81
00:05:14,780 --> 00:05:19,130
So the hook JS is the page that hooks the target user to beef.

82
00:05:19,130 --> 00:05:26,450
So that page is going to be stored at Http, followed by the address of our server.

83
00:05:26,450 --> 00:05:28,010
So it's this one right here.

84
00:05:28,010 --> 00:05:29,180
We're going to copy it.

85
00:05:29,180 --> 00:05:30,560
We're going to paste it.

86
00:05:30,560 --> 00:05:33,740
And this is going to be on port 3000.

87
00:05:33,740 --> 00:05:36,680
Because as you know beef runs on port 3000.

88
00:05:36,680 --> 00:05:40,520
And the file name is hook dot JS.

89
00:05:41,030 --> 00:05:44,060
Now once you do this you're going to have to close this tag.

90
00:05:44,060 --> 00:05:50,360
And you have to also open another tag, do a forward slash script and then close it.

91
00:05:50,360 --> 00:05:54,230
So it's very very simple beef actually a lot of the time gives you this.

92
00:05:54,230 --> 00:05:56,330
When you start it, it actually gives you this code.

93
00:05:56,330 --> 00:05:57,740
So you can copy and paste it.

94
00:05:57,740 --> 00:05:59,240
But it's very, very simple.

95
00:05:59,240 --> 00:06:01,190
You're simply creating a script tag.

96
00:06:01,190 --> 00:06:05,300
You're saying the source of this script is this file right here.

97
00:06:05,300 --> 00:06:07,880
So this file contains my beef code.

98
00:06:07,880 --> 00:06:14,270
And for you to make sure that this is working properly, you can simply copy this and paste it in the

99
00:06:14,270 --> 00:06:15,080
browser.

100
00:06:15,080 --> 00:06:17,030
And you should actually get this.

101
00:06:17,030 --> 00:06:20,210
So this is the code that will hook a browser to beef.

102
00:06:20,210 --> 00:06:23,690
So if you get this that means you're specifying the right URL.

103
00:06:23,720 --> 00:06:28,400
But it's basically the URL of the computer that is running beef.

104
00:06:28,400 --> 00:06:36,890
So I am running beef on my Kali cloud install on port 3000, and the name of the file is hooks JS.

105
00:06:37,580 --> 00:06:42,260
Just to make this easier to understand, our server looks like this.

106
00:06:42,290 --> 00:06:47,390
We're calling the server by putting the IP and then we're putting colon 3000.

107
00:06:47,390 --> 00:06:49,820
So it's going to go this way towards beef.

108
00:06:49,820 --> 00:06:53,750
And then we're requesting a file called hooks from beef.

109
00:06:54,320 --> 00:07:00,740
Once you do that you just have to close this tag and then do forward slash script tag again.

110
00:07:00,740 --> 00:07:03,080
That's just the way HTML is.

111
00:07:03,080 --> 00:07:07,010
It's nothing that we are creating or inventing and that's it.

112
00:07:07,010 --> 00:07:08,390
That's all you have to do.

113
00:07:08,390 --> 00:07:09,710
So I'm going to save this.

114
00:07:09,710 --> 00:07:13,220
I'm going to do control S or cmd s if you're on Mac.

115
00:07:13,220 --> 00:07:19,190
And once you save it and go back to FileZilla, you'll see you'll get a prompt telling you that the

116
00:07:19,190 --> 00:07:20,900
index file got modified.

117
00:07:20,900 --> 00:07:26,090
And do you want to upload this modified file and overwrite the existing one.

118
00:07:26,210 --> 00:07:32,660
So I'm going to say yes so that we can upload the modified file and overwrite this index.html file.

119
00:07:33,530 --> 00:07:39,770
So let's go ahead to the windows computer and paste the IP of my cloud install of Kali.

120
00:07:39,980 --> 00:07:41,390
We're going to hit enter.

121
00:07:42,990 --> 00:07:43,770
And perfect.

122
00:07:43,770 --> 00:07:48,240
As you can see, the security is loading and it looks identical to the security.

123
00:07:48,240 --> 00:07:49,050
Nothing different.

124
00:07:49,050 --> 00:07:53,280
But in the background it has the beef hook code running.

125
00:07:53,280 --> 00:07:58,920
And as you can see, we're actually not loading anything over port 3000 because we're simply loading

126
00:07:58,920 --> 00:08:02,490
the index dot HTML page from the web browser.

127
00:08:02,490 --> 00:08:05,250
And remember, the web browser runs on port 80.

128
00:08:05,250 --> 00:08:09,870
And if we don't specify a port in here, it loads whatever that is running on port 80.

129
00:08:09,870 --> 00:08:15,450
And we have this page running in the index dot HTML, so we don't have to specify a name after it.

130
00:08:15,450 --> 00:08:17,580
That's why this page is loading by default.

131
00:08:17,580 --> 00:08:22,980
But in the background it's loading the beef hook code on port 3000.

132
00:08:22,980 --> 00:08:27,000
So we kind of mask that by embedding it in here.

133
00:08:27,180 --> 00:08:33,690
And now if we go to beef and let me just go back to the home page.

134
00:08:33,690 --> 00:08:38,910
As you can see we have a the windows computer in here hooked to beef.

135
00:08:38,910 --> 00:08:46,500
So if I click it and go to the commands just to run something simple to make sure that it is working,

136
00:08:46,500 --> 00:08:52,200
I'm going to look for the alert and let's just run an alert dialog, just the default one, just to

137
00:08:52,200 --> 00:08:54,000
make sure that it is working.

138
00:08:54,860 --> 00:08:56,660
If we go to the target.

139
00:08:56,660 --> 00:08:59,330
As you can see, we have the Beef Alert dialog.

140
00:08:59,330 --> 00:09:07,010
So basically this browser in this windows computer is now hooked to beef by simply loading a page that

141
00:09:07,010 --> 00:09:11,690
looks identical to a page that the target user knows and trusts.

142
00:09:11,690 --> 00:09:16,490
And as you can see, the URL does not contain 3000, does not contain anything suspicious.

143
00:09:16,490 --> 00:09:21,980
And I'm actually going to show you in the future how to use an actual domain name instead of an IP and

144
00:09:21,980 --> 00:09:23,150
use Https.

145
00:09:23,150 --> 00:09:29,120
So it's going to look very believable and at the same time execute the beef code in the background.

146
00:09:29,120 --> 00:09:33,320
And therefore now you can run any beef command that you want.

147
00:09:33,320 --> 00:09:38,600
And as I shown in my previous courses, my other courses and I'll show you later with beef you can do

148
00:09:38,600 --> 00:09:39,110
so much.

149
00:09:39,110 --> 00:09:42,830
You can basically get the user to download and execute files.

150
00:09:42,830 --> 00:09:46,550
You can social engineer the user to enter their username and password.

151
00:09:46,550 --> 00:09:48,740
You can do so so much with beef.

152
00:09:48,740 --> 00:09:53,690
So this is a very convincing way of hooking someone to beef in my opinion.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:06,830
Now that we know how to use Let's Encrypt with the Certbot in order to enable https on our website,

2
00:00:06,830 --> 00:00:08,690
and we have it enabled on Apache.

3
00:00:08,690 --> 00:00:11,900
So everything we run on Apache now runs on Https.

4
00:00:11,930 --> 00:00:18,200
In this lecture, I'm going to show you how to use the same certificates with beef so that the Beef

5
00:00:18,200 --> 00:00:25,010
Hulk page can be loaded over Https, and therefore we will be able to embed it into any Https page that

6
00:00:25,010 --> 00:00:32,570
we have on our web server, and therefore our malicious pages will be more believable and less suspicious.

7
00:00:32,810 --> 00:00:39,830
So in the last lecture, I told you that we need to keep a note of the location of the files that were

8
00:00:39,830 --> 00:00:41,330
generated by Certbot.

9
00:00:41,330 --> 00:00:43,220
So we have the key file in here.

10
00:00:43,220 --> 00:00:47,210
This is the private key and we have the certificate file in here.

11
00:00:47,420 --> 00:00:52,820
This is important because we're going to need to manually point beef to use these files in order to

12
00:00:52,820 --> 00:00:54,170
enable Https.

13
00:00:54,170 --> 00:00:59,810
Because remember when we run Certbot, we told it that we want you to install it on Apache.

14
00:00:59,810 --> 00:01:04,010
So it created the certificates first and then it installed them on Apache.

15
00:01:04,010 --> 00:01:09,200
But Certbot doesn't have functionality for installing the certificates on beef.

16
00:01:09,200 --> 00:01:12,680
And that's why we're going to have to do the installation step manually.

17
00:01:13,670 --> 00:01:20,690
So the first thing that we're going to do is move the certificates to the beef certificate directory.

18
00:01:20,690 --> 00:01:23,870
So we're going to copy the key file.

19
00:01:25,230 --> 00:01:33,900
And we're going to use the CP command to copy it from its original location to usr share.

20
00:01:34,760 --> 00:01:36,800
Before access.

21
00:01:37,800 --> 00:01:39,810
So usr share beef.

22
00:01:39,810 --> 00:01:49,050
XSS is the path that beef requires its certificate to be located at, and this is the path of the certificate

23
00:01:49,050 --> 00:01:51,840
where the cert bot created them.

24
00:01:51,870 --> 00:01:58,800
So basically using the CP command to make a copy of the certificate in the path that beef wants, we're

25
00:01:58,800 --> 00:02:03,240
going to hit enter and we get no messages meaning the command got executed properly.

26
00:02:03,240 --> 00:02:08,340
And the next thing we're going to do is repeat the command with the certificate file.

27
00:02:08,850 --> 00:02:18,000
So we're going to do CP this file to usr share beef dash XSS.

28
00:02:18,360 --> 00:02:23,610
We're going to hit enter and we get no errors meaning the command got executed properly as well.

29
00:02:23,610 --> 00:02:29,370
And we're going to use the LHS command just to make sure that the files that we copied are actually

30
00:02:29,370 --> 00:02:34,200
inside the directory that we want, which is usr share beef xss.

31
00:02:34,680 --> 00:02:36,240
I'm going to hit enter.

32
00:02:37,160 --> 00:02:41,810
And we have the files in here, the full chain file and the private key right here.

33
00:02:42,480 --> 00:02:48,570
So now that the files are in the right directory, we need to modify beef's configuration to tell it

34
00:02:48,570 --> 00:02:56,400
to enable https on it and point it to these files so that it uses them in order to enable Https.

35
00:02:57,090 --> 00:02:59,880
So beef's config file is in e.t.c..

36
00:02:59,880 --> 00:03:02,580
So we're going to use nano which is a text editor.

37
00:03:02,580 --> 00:03:06,750
We covered it before and we used it before to modify configurations.

38
00:03:06,750 --> 00:03:14,070
And beef's configuration file is in e.t.c. bfc's config dot yaml.

39
00:03:14,070 --> 00:03:17,430
So nano is the program, the text editor that we want to use.

40
00:03:17,430 --> 00:03:20,040
And we're telling it that we want to edit this file.

41
00:03:20,910 --> 00:03:22,170
I'm going to hit enter.

42
00:03:22,170 --> 00:03:24,960
And it's going to load the configuration file for me.

43
00:03:25,410 --> 00:03:26,760
And this config file.

44
00:03:26,760 --> 00:03:30,150
You'll notice that some lines start with a hash.

45
00:03:30,240 --> 00:03:34,290
The hash is used to indicate that this line is a comment.

46
00:03:34,290 --> 00:03:41,760
Therefore it's used to either explain the options available in this config file or to disable some of

47
00:03:41,760 --> 00:03:42,510
these options.

48
00:03:42,960 --> 00:03:45,420
For example, in here you can see this line.

49
00:03:45,420 --> 00:03:47,790
It is a comment because it starts with a hash.

50
00:03:47,790 --> 00:03:53,190
And simply telling you these are the credentials that you're going to use to authenticate with beef.

51
00:03:53,280 --> 00:03:54,840
And if you scroll down.

52
00:03:54,840 --> 00:04:00,480
So I'm going to just scroll down using the arrows you can see you can set the username and the password.

53
00:04:00,480 --> 00:04:05,220
And you can simply modify the values in here to change the username and the password that you're going

54
00:04:05,220 --> 00:04:08,670
to use in order to log in to the beef control panel.

55
00:04:09,270 --> 00:04:16,440
Now what we want to do is to enable Https on beef and get it to use the certificates that we created

56
00:04:16,440 --> 00:04:17,760
and copied earlier.

57
00:04:17,760 --> 00:04:23,490
That's why we're simply just going to scroll down again using the arrows, read the comments and see

58
00:04:23,490 --> 00:04:27,330
which ones are applicable in order to enable Https.

59
00:04:27,900 --> 00:04:33,090
Now you can see this block of options allows you to use beef on the public internet.

60
00:04:33,090 --> 00:04:39,870
So it's not only needed for Https, but it's important in order to use beef on a real domain name.

61
00:04:40,290 --> 00:04:44,850
So this is an example where the hash is used to disable the option.

62
00:04:44,850 --> 00:04:49,290
So the public option is disabled right now because it is preceded with a hash.

63
00:04:49,290 --> 00:04:55,920
So to enable it I simply just have to move my cursor in here and remove it using the backspace.

64
00:04:56,220 --> 00:05:01,740
So as you can see now it's colored meaning that it is going to be taken into account as part of the

65
00:05:01,740 --> 00:05:02,610
configuration.

66
00:05:02,610 --> 00:05:05,250
And beef is going to try to run on the public.

67
00:05:05,250 --> 00:05:09,570
But as you can see, this is not enough because you need to set the host the port.

68
00:05:09,570 --> 00:05:16,170
And if Https is enabled and you can see beside each one of these options, you have a description of

69
00:05:16,170 --> 00:05:17,490
what this option does.

70
00:05:17,640 --> 00:05:22,440
So for example the host in here it is the domain name that we're going to be running beef on.

71
00:05:22,740 --> 00:05:26,940
So again to enable it I need to remove the hash from the start of the line.

72
00:05:26,940 --> 00:05:31,650
And then I'm going to place the host between the two quotation marks that I have in here.

73
00:05:31,650 --> 00:05:35,130
So the host that I have is Facebook login.co.

74
00:05:35,800 --> 00:05:40,960
I'm going to leave this hash in here because as you can see, this is simply a comment and it really

75
00:05:40,960 --> 00:05:43,420
should not be used as part of the configuration.

76
00:05:43,420 --> 00:05:44,800
It is just a comment.

77
00:05:45,720 --> 00:05:47,490
Next we have to set the port.

78
00:05:47,490 --> 00:05:50,850
So again I'm going to move my cursor to the start of the line.

79
00:05:51,780 --> 00:05:54,060
Remove the hash to enable the option.

80
00:05:54,060 --> 00:05:59,430
And then we're going to set the port to the port that beef uses, which we know is 3000.

81
00:06:00,090 --> 00:06:05,490
Last but not least, we're going to set the Https option in here again removing the hash to enable the

82
00:06:05,490 --> 00:06:05,970
option.

83
00:06:05,970 --> 00:06:11,340
And we because we want to use https, we're going to set this to true instead of false.

84
00:06:12,200 --> 00:06:17,270
Now that we're done with this section, we're going to continue moving on through the configuration

85
00:06:17,270 --> 00:06:17,780
file.

86
00:06:17,780 --> 00:06:23,330
Again, reading the comments, looking for the comments that are relevant for enabling Https on beef.

87
00:06:24,690 --> 00:06:29,460
So right here, clearly we have a block of options that is titled Https.

88
00:06:29,460 --> 00:06:32,010
So this is definitely applicable for us.

89
00:06:32,010 --> 00:06:34,710
And you can see the first option is actually enabled.

90
00:06:34,710 --> 00:06:38,100
It's not preceded with a hash but it is set to false.

91
00:06:38,100 --> 00:06:41,010
So Https is disabled right now on beef.

92
00:06:41,010 --> 00:06:43,560
So I'm going to remove this using the backspace.

93
00:06:43,560 --> 00:06:45,870
And I'm going to type true to enable it.

94
00:06:46,760 --> 00:06:48,770
The next option in here sets.

95
00:06:48,770 --> 00:06:54,410
If beef is used on the public internet again, it's set to false, meaning that it is disabled and therefore

96
00:06:54,410 --> 00:06:56,060
I'm going to need to set it to true.

97
00:06:57,020 --> 00:07:03,710
And finally, you can see that we have two options in here to set the key file and the certificate file.

98
00:07:03,920 --> 00:07:07,310
So we've already copied these files and put them in the right directory.

99
00:07:07,310 --> 00:07:12,200
So all we have to do is replace the file names in here with the file names that we have.

100
00:07:12,410 --> 00:07:16,940
So our key file is stored in a file that is called priv key.

101
00:07:17,780 --> 00:07:21,980
And our certificate file is stored in a file that is called.

102
00:07:22,700 --> 00:07:23,810
Full chain.

103
00:07:24,140 --> 00:07:29,720
And as I remember, there is nothing else to edit in the file to enable Https, but we're going to scroll

104
00:07:29,720 --> 00:07:35,030
through it quickly to make sure that there is nothing there that might interfere with us running Https.

105
00:07:35,030 --> 00:07:38,660
And now that we're happy, we can exit this text editor.

106
00:07:38,660 --> 00:07:44,810
As you know before control X to exit, then it's asking me, do I want to save the modified file?

107
00:07:44,810 --> 00:07:47,660
I'm going to type Y from my keyboard to say yes.

108
00:07:47,660 --> 00:07:49,340
It's asking me for the file name.

109
00:07:49,340 --> 00:07:51,560
We're going to keep it the same file name to overwrite.

110
00:07:51,560 --> 00:07:53,660
So I'm going to hit enter and that's it.

111
00:07:53,660 --> 00:07:56,870
Now my file is saved with the new configuration.

112
00:07:57,500 --> 00:08:02,000
But because we modified beef's configuration, we're going to have to restart it.

113
00:08:02,000 --> 00:08:04,580
So you're going to have to do service.

114
00:08:05,840 --> 00:08:10,100
Beef Dash X restart.

115
00:08:12,290 --> 00:08:16,400
And to make sure that we've started properly, we're going to do service.

116
00:08:17,310 --> 00:08:18,540
Beef excess.

117
00:08:18,540 --> 00:08:24,030
And this time we're going to say status instead of restart to get the status of this service.

118
00:08:24,030 --> 00:08:29,700
And as you can see, the service is running with no issues at all, meaning that now it should be running

119
00:08:29,700 --> 00:08:31,380
with Https enabled.

120
00:08:31,830 --> 00:08:38,640
So let's go ahead and access Bfas in Https just to make sure that it is actually working as expected.

121
00:08:38,730 --> 00:08:41,190
So we have the domain in here.

122
00:08:41,190 --> 00:08:45,000
We're just going to have to do colon 3000 because that's the port that beef runs on.

123
00:08:45,000 --> 00:08:50,670
And we have to go to UI panel because that's where the configuration is or the management panel is.

124
00:08:50,670 --> 00:08:53,670
And as you can see, beef is working with no issues at all.

125
00:08:53,670 --> 00:08:58,080
So I can log in using my username and the password.

126
00:08:58,920 --> 00:09:03,810
And as you can see, beef is working with no issues at all with no online browsers.

127
00:09:03,810 --> 00:09:09,810
Obviously, because we have not loaded the index or the home page that contains beef hook.

128
00:09:09,810 --> 00:09:16,740
And also we actually have to modify that page because the hook JS file now should be loaded using the

129
00:09:16,740 --> 00:09:20,160
domain name that we're using which is Facebook Login Co.

130
00:09:20,700 --> 00:09:26,310
So we're going to clear the screen and use nano to edit the index file.

131
00:09:26,310 --> 00:09:30,510
So it's in var ww HTML.

132
00:09:30,510 --> 00:09:34,380
And it's called index dot HTML.

133
00:09:35,170 --> 00:09:40,870
And in here we're going to put it inside the head, just like I did earlier.

134
00:09:40,870 --> 00:09:45,040
So we're going to do a script S or C.

135
00:09:46,200 --> 00:09:49,800
Https Facebook.

136
00:09:49,800 --> 00:09:56,610
Login echo port 3000 and hook dot js.

137
00:09:57,710 --> 00:10:01,970
Slash script and I accidentally removed this quote.

138
00:10:01,970 --> 00:10:09,260
So we're going to make sure that I added at the end control X to exit Y enter, and that should be saved.

139
00:10:09,260 --> 00:10:13,370
So let's go ahead and load this page from Firefox.

140
00:10:13,370 --> 00:10:17,210
So we're going to go Facebook Login Co.

141
00:10:19,190 --> 00:10:20,120
And perfect.

142
00:10:20,120 --> 00:10:23,120
As you can see, the website loads with https.

143
00:10:23,120 --> 00:10:24,770
With the lock icon.

144
00:10:25,310 --> 00:10:30,320
You can have this as any website you want, but right now we have the fake login page that will actually

145
00:10:30,320 --> 00:10:34,610
store the login information that the user would put in here and show it to you.

146
00:10:34,610 --> 00:10:40,580
If you click on the inputs, you're not seeing any warnings, but at the same time, this page should

147
00:10:40,580 --> 00:10:45,440
have hooked us to beef because we included the beef hook in this page.

148
00:10:45,440 --> 00:10:52,400
So if we go back to beef, as you can see, we have a new online browser in here.

149
00:10:52,400 --> 00:10:58,340
And if we click on the commands just to make sure that it works as expected, we're going to just run

150
00:10:58,340 --> 00:10:59,150
an alert.

151
00:10:59,150 --> 00:11:00,740
Just a simple command.

152
00:11:01,400 --> 00:11:02,660
I'm going to keep it the way it is.

153
00:11:02,660 --> 00:11:04,040
I'm going to execute.

154
00:11:04,040 --> 00:11:09,950
And if we go to the target website, as you can see, the alert code is being executed, which means

155
00:11:09,950 --> 00:11:16,310
that this browser right now is hooked to beef, and we can run all of the commands that beef allows

156
00:11:16,310 --> 00:11:16,850
us to run.

157
00:11:16,850 --> 00:11:20,780
And you've seen how dangerous they can be so we can steal more information.

158
00:11:20,780 --> 00:11:27,650
We can inject any JavaScript code we want, we can show them a fake update and fully hack or compromise

159
00:11:27,650 --> 00:11:28,430
their computer.

160
00:11:28,430 --> 00:11:33,290
And I actually cover a lot of this in my social engineering course and the general ethical hacking course.

161
00:11:33,350 --> 00:11:39,740
So it's really up to your imagination from here onwards, how to make this page more attractive and

162
00:11:39,740 --> 00:11:41,570
more believable to the target.

163
00:11:41,570 --> 00:11:45,710
Make sure you choose a domain name that suits whatever web page you're loading.

164
00:11:45,710 --> 00:11:50,150
And as I showed you before, you can clone any web page that you want, so make sure that you clone

165
00:11:50,150 --> 00:11:52,700
something that the target is interested to.

166
00:11:52,700 --> 00:11:58,250
And if you do that properly, the chances of the target actually loading the target page and not feeling

167
00:11:58,250 --> 00:12:00,800
suspicious are going to be very, very high.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,690
So previously at the start of this section, I showed you how we can use the pretty theft command to

2
00:00:05,690 --> 00:00:08,540
steal login information from hooked browsers.

3
00:00:08,540 --> 00:00:15,800
But now that we enabled Https and hooked a domain name to beef, we can actually run much more powerful

4
00:00:15,800 --> 00:00:21,740
attacks that the browser would otherwise block because Https was not enabled.

5
00:00:21,950 --> 00:00:27,500
So first of all, I have a windows computer in here, and I'm simply going to hook it to beef by going

6
00:00:27,500 --> 00:00:29,420
to Xbox.com.

7
00:00:31,750 --> 00:00:36,610
And now if we go back, we'll see our online browser in here.

8
00:00:36,790 --> 00:00:42,460
If we click it, you've already seen that we get a lot of really useful information in here, such as

9
00:00:42,460 --> 00:00:46,270
the web browser used, the operating system and the IP.

10
00:00:47,630 --> 00:00:52,760
And as mentioned before, we can simply go to Google and look for an IP finder.

11
00:00:53,060 --> 00:01:01,220
And using these IP finder websites, we can simply plug in this IP which is 89 1988 175.

12
00:01:01,220 --> 00:01:02,570
Click on lookup.

13
00:01:02,570 --> 00:01:07,760
And that's going to get us an approximation of the location of the target.

14
00:01:07,760 --> 00:01:11,840
So we can see that they are in Ireland in Dublin, which is correct.

15
00:01:11,840 --> 00:01:17,870
But this is not going to get you the exact location, because the IP only gives us a general idea of

16
00:01:17,870 --> 00:01:18,830
the location.

17
00:01:19,040 --> 00:01:26,330
But now that Https is enabled and we're linked a domain name to beef, we can actually go ahead and

18
00:01:26,330 --> 00:01:30,320
execute more intrusive commands that will give us better results.

19
00:01:30,320 --> 00:01:36,410
For example, if we wanted to know the exact location of the target, we can look for the geolocation

20
00:01:36,410 --> 00:01:37,220
module.

21
00:01:37,640 --> 00:01:43,460
And we have this module right here that will basically get us the exact location of the target.

22
00:01:43,460 --> 00:01:45,920
So let's just click on execute.

23
00:01:45,920 --> 00:01:52,250
And when you execute this the target will get a notification asking them if they want to allow this

24
00:01:52,250 --> 00:01:54,050
website to access their location.

25
00:01:54,050 --> 00:01:57,170
So it's going to be up to your social engineering techniques.

26
00:01:57,170 --> 00:02:02,480
The loaded websites need to be convincing so that the target allows the location when they get this

27
00:02:02,480 --> 00:02:08,690
pop up, but if they click allow and come back here, click on the command result.

28
00:02:08,690 --> 00:02:12,560
And as you can see, we have the exact location of the target.

29
00:02:12,560 --> 00:02:15,770
So this is our exact location of our office.

30
00:02:15,770 --> 00:02:20,270
If you look up this code, you'll basically come right to the doorstep of the office.

31
00:02:20,270 --> 00:02:25,520
And you even have the actual full address and the longitude and the latitude.

32
00:02:25,520 --> 00:02:32,330
So you can use these also to get the exact location if you plot them on Google or any other map application.

33
00:02:32,660 --> 00:02:34,340
So this is really, really cool.

34
00:02:34,340 --> 00:02:37,640
But this is only one command that beef allows us to do.

35
00:02:37,850 --> 00:02:42,050
I also want to cover a very cool module, the webcam module.

36
00:02:42,050 --> 00:02:44,870
So if we just look for cam.

37
00:02:45,620 --> 00:02:47,120
We have this one right here.

38
00:02:47,120 --> 00:02:51,530
It's going to use HTML5 to load the webcam of the target computer.

39
00:02:51,530 --> 00:02:54,890
And I'm actually going to do this on an Apple computer just for a change.

40
00:02:54,890 --> 00:03:00,680
So we're going to load these hacks in here because as mentioned before, beef works on all operating

41
00:03:00,680 --> 00:03:02,810
systems as long as they have a web browser.

42
00:03:02,810 --> 00:03:06,530
So we've already showed it in action here on a windows computer.

43
00:03:06,530 --> 00:03:10,310
Now, we loaded the book page on an Apple computer right here.

44
00:03:10,310 --> 00:03:15,620
So let's go ahead and have a look in here to see if this browser is going to come online.

45
00:03:15,620 --> 00:03:16,400
And perfect.

46
00:03:16,400 --> 00:03:19,640
As you can see we have the Apple browser here coming up online.

47
00:03:19,640 --> 00:03:20,690
We're going to click it.

48
00:03:20,690 --> 00:03:21,800
Go to the commands.

49
00:03:21,800 --> 00:03:27,050
And I'm going to run the camera module that I just told you about, which is basically going to use

50
00:03:27,290 --> 00:03:30,440
HTML5 to take a picture of the webcam.

51
00:03:30,440 --> 00:03:33,350
So we're simply going to click execute.

52
00:03:34,210 --> 00:03:39,520
Again, this module is going to ask the user if they want to allow this website to access the camera.

53
00:03:39,520 --> 00:03:44,350
So this goes to your social engineering skills if you're able to get them to accept it.

54
00:03:44,350 --> 00:03:51,370
But if they allow it in beef, if we click on the command, we are able to see a picture of the target.

55
00:03:51,370 --> 00:03:54,760
Now that's a previous picture that I took while I was testing.

56
00:03:54,760 --> 00:04:01,150
And if we click here, as you can see, the camera took a picture of myself because it's actually facing

57
00:04:01,150 --> 00:04:02,350
my face right now.

58
00:04:02,770 --> 00:04:08,680
And now again, I've mentioned this a few times now that we have Https enabled, a lot of these commands

59
00:04:08,680 --> 00:04:11,050
that used to not work will actually work for you.

60
00:04:11,050 --> 00:04:15,340
And all of these work on all operating systems as long as the target has a web browser.

61
00:04:15,340 --> 00:04:20,380
So I highly recommend spending some time with experimenting and playing with these commands.

62
00:04:20,380 --> 00:04:25,090
I've shown some of these in my other courses, where you can simply show a fake notification bar and

63
00:04:25,090 --> 00:04:29,770
get the target to download and update our program, and that program will hack their computer.

64
00:04:29,770 --> 00:04:32,860
We're actually going to be covering backdoors next in the next section.

65
00:04:32,860 --> 00:04:38,920
Or for example, here in the browser, you have other modules that will rewrite every single link on

66
00:04:38,920 --> 00:04:41,440
the page with whatever link you put in here.

67
00:04:41,440 --> 00:04:46,660
So if you had a download link in the page, you can replace it with your malware again and get the target

68
00:04:46,660 --> 00:04:47,830
to download your malware.

69
00:04:47,830 --> 00:04:50,350
So the sky is really the limit with this program.

70
00:04:50,350 --> 00:04:55,600
There are so many different modules that can be so useful and so many different scenarios.

71
00:04:55,600 --> 00:04:57,850
So it really comes down to your creativity.

72
00:04:57,850 --> 00:05:03,790
With this, there is no way for me to cover all of these options, but using these modules is very simple.

73
00:05:03,790 --> 00:05:09,610
All you have to do is click the module, read the description and click execute to see how it works.

74
00:05:10,030 --> 00:05:15,310
And the best part of it all is that all of this is happening through a page that the target trusts,

75
00:05:15,310 --> 00:05:17,980
because this can be any page that the target would trust.

76
00:05:17,980 --> 00:05:22,690
It's loading over Https and it's loading using a proper domain name.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,260 --> 00:00:06,860
So far, what we have done with beef is really, really cool, but it requires us to be online when

2
00:00:06,860 --> 00:00:10,310
the target loads this hook page that we have in here.

3
00:00:10,310 --> 00:00:12,350
So that is a bit of a limitation.

4
00:00:12,350 --> 00:00:18,590
And what I want to do in this lecture is show you how you can build your own pages that can execute

5
00:00:18,590 --> 00:00:25,220
useful commands on the target computer, and store the useful data on your cloud server so that you

6
00:00:25,220 --> 00:00:30,560
do not have to be online when they load the malicious page, and so that you can come back whenever

7
00:00:30,560 --> 00:00:30,920
you want.

8
00:00:30,920 --> 00:00:35,360
Log in to your cloud server and you will see the information that you wanted to see.

9
00:00:35,600 --> 00:00:42,770
Now this is very easy because if you think about it, beef is simply using normal JavaScript code and

10
00:00:42,770 --> 00:00:46,670
normal JavaScript functions to execute the commands that we saw.

11
00:00:46,670 --> 00:00:53,900
So there's nothing stopping us from manually putting the code that we want in our index.html in here

12
00:00:53,900 --> 00:01:00,800
on our cloud server, and program it in a way so that it stores this information on file, so that we

13
00:01:00,800 --> 00:01:04,250
can come back anytime in the future and see this information.

14
00:01:04,730 --> 00:01:06,710
We're going to keep everything very simple.

15
00:01:06,710 --> 00:01:09,470
So don't worry, you don't need to know any programming.

16
00:01:09,470 --> 00:01:12,080
And you're going to see how easy this can be done.

17
00:01:12,590 --> 00:01:14,900
So first let's define what we want to do.

18
00:01:14,900 --> 00:01:22,910
Let's modify this index dot HTML page this page right here so that when it loads, it automatically

19
00:01:22,910 --> 00:01:29,480
gets the location of the person that is loading it and automatically gets the operating system of the

20
00:01:29,480 --> 00:01:34,340
computer that is loading it, and automatically store this on the cloud server in a.

21
00:01:34,340 --> 00:01:38,810
TXT file, so that we can come back at any time and see this information.

22
00:01:39,020 --> 00:01:43,100
So the first task is to get the location of the target.

23
00:01:43,100 --> 00:01:48,950
So you can simply go to Google and look for find location using JavaScript.

24
00:01:49,610 --> 00:01:55,850
And we're choosing JavaScript as the programming language because it is a client side programming language

25
00:01:55,850 --> 00:01:58,850
that is supported by all modern web browsers.

26
00:01:58,850 --> 00:02:03,830
That's why beef actually uses this language to implement its modules, and that's why we're going to

27
00:02:03,830 --> 00:02:08,090
use it so that the code will work on any device that has a web browser.

28
00:02:08,750 --> 00:02:13,100
Now, if we look for this, you can see that the first result is actually going to be really good.

29
00:02:13,100 --> 00:02:18,920
It's from a website that is called W3 schools, which is a really good resource to learn programming.

30
00:02:19,250 --> 00:02:24,830
So you can see in here it's explaining to you how to get the location using the geolocation API.

31
00:02:24,830 --> 00:02:29,090
It explains everything to you, including the supported browsers.

32
00:02:29,090 --> 00:02:31,280
It even gives you an example code.

33
00:02:31,280 --> 00:02:36,980
And if you click on try it yourself, it will actually execute the code for you and show you how it's

34
00:02:36,980 --> 00:02:38,090
going to work.

35
00:02:38,090 --> 00:02:43,520
Now, even if you don't know programming, reading this document in here should teach you how to use

36
00:02:43,520 --> 00:02:45,620
JavaScript to get the location.

37
00:02:45,620 --> 00:02:48,620
Now, if we read the code, you can see that it's very simple.

38
00:02:48,620 --> 00:02:52,940
First of all, we have a function in here that is called get location.

39
00:02:52,940 --> 00:02:56,660
That will simply check if the location is available.

40
00:02:56,660 --> 00:03:01,040
If it is, it's going to call this method to get the current location.

41
00:03:01,040 --> 00:03:04,550
And you can see even the name of the method is Getcurrentposition.

42
00:03:04,550 --> 00:03:06,710
It's kind of self-explanatory.

43
00:03:06,710 --> 00:03:08,660
So this is the line that we want.

44
00:03:08,660 --> 00:03:09,890
So we're going to copy it.

45
00:03:11,140 --> 00:03:14,290
And we're going to go to our index.html page.

46
00:03:14,290 --> 00:03:19,930
We're going to remove the beef hook from it because we don't want to hook the target to beef anymore.

47
00:03:19,930 --> 00:03:25,540
And we're going to keep the script so that we can include the code that we just copied in here.

48
00:03:26,010 --> 00:03:29,010
Now let's go back to the code to understand how it works.

49
00:03:29,010 --> 00:03:33,570
And you can see, like I said, it explains to you how the code is going to work.

50
00:03:33,570 --> 00:03:38,640
And it's telling you that if the Getcurrentposition method is successful.

51
00:03:38,640 --> 00:03:45,120
So if this method is successful, it's going to call a function that is called show position, which

52
00:03:45,120 --> 00:03:46,320
is this call right here.

53
00:03:46,320 --> 00:03:49,890
And this function is defined in here this function right here.

54
00:03:51,160 --> 00:03:52,780
So we actually need this function.

55
00:03:52,780 --> 00:03:54,040
So I'm going to copy it.

56
00:03:54,040 --> 00:03:57,130
And we're going to paste it in here below the method.

57
00:03:57,700 --> 00:04:01,630
And I'm just going to tap it so it looks nicer and easier to read.

58
00:04:02,330 --> 00:04:07,760
And as you can see, this function right here is actually relying on x.

59
00:04:07,940 --> 00:04:11,150
X is a variable that was defined in here.

60
00:04:11,510 --> 00:04:13,520
Therefore we didn't actually copy that.

61
00:04:13,520 --> 00:04:15,770
So we're going to have to create it again.

62
00:04:15,770 --> 00:04:18,890
So we're going to say let to create it.

63
00:04:18,890 --> 00:04:23,330
And I don't want to call it x I'm going to call it something nicer I'm going to say location.

64
00:04:23,720 --> 00:04:31,880
So we're going to say let location equal to the text latitude followed by the actual latitude returned

65
00:04:31,880 --> 00:04:33,680
from this method right here.

66
00:04:33,680 --> 00:04:40,340
And then the text longitude followed by the actual longitude that is returned from this method in here.

67
00:04:41,020 --> 00:04:46,660
And they're actually using the BR tag in here because they are displaying it on a HTML page.

68
00:04:46,660 --> 00:04:48,160
But we're not doing that.

69
00:04:48,160 --> 00:04:50,260
We're going to be storing it in a text file.

70
00:04:50,260 --> 00:04:54,550
And that's why I'm simply just going to put a comma just so that it looks nicer.

71
00:04:55,970 --> 00:05:01,670
So now that we have the location stored in this variable right here, the next thing that we want to

72
00:05:01,670 --> 00:05:08,120
do is get the browser version and the operating system of the web browser that is loading our page.

73
00:05:08,120 --> 00:05:14,780
And we mentioned previously that every web browser sends this information as the user agent to the server.

74
00:05:14,780 --> 00:05:18,380
So all we have to do is simply read this user agent value.

75
00:05:18,380 --> 00:05:20,570
So again we don't know how to do this.

76
00:05:20,570 --> 00:05:25,670
We're going to go to Google and we're going to look for find user agent JavaScript.

77
00:05:27,330 --> 00:05:31,020
And again we have a result here from the W3 schools.

78
00:05:31,020 --> 00:05:34,530
Like I said, this is a great resource to learn this kind of stuff.

79
00:05:34,530 --> 00:05:37,080
And as you can see, you get the codes right away.

80
00:05:37,080 --> 00:05:38,580
And the code is very simple.

81
00:05:38,580 --> 00:05:41,550
It's defining a variable that is called agent.

82
00:05:41,550 --> 00:05:46,380
And this variable is storing the value of the navigator dot user agent.

83
00:05:46,380 --> 00:05:50,340
So this is basically the user agent that the browser is sending.

84
00:05:50,340 --> 00:05:55,320
And again if this is not clear enough you can actually go ahead and read all this description to learn

85
00:05:55,320 --> 00:05:57,060
exactly how this works.

86
00:05:57,060 --> 00:06:02,700
So I'm going to copy this and we're going to simply paste it in our code in here.

87
00:06:03,240 --> 00:06:03,990
And perfect.

88
00:06:03,990 --> 00:06:13,140
Now our index.html is going to store the location and the agent under the location and the agent variables.

89
00:06:14,110 --> 00:06:20,470
So the next and the final step is to actually store these values on our cloud server, so that I don't

90
00:06:20,470 --> 00:06:26,170
have to always be online, so that whenever somebody loads my page, it'll store it for me in a text

91
00:06:26,170 --> 00:06:32,230
file, and then I can come back at any time and read the values stored in there, and we will cover

92
00:06:32,230 --> 00:06:33,640
that in the next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,390 --> 00:00:07,260
In the previous lecture, we modified the code of this page so that it gets the location of any person

2
00:00:07,260 --> 00:00:12,750
that loads this page and stores their user agent, which will tell us their operating system and the

3
00:00:12,750 --> 00:00:14,220
web browser that they use.

4
00:00:14,250 --> 00:00:19,170
These values are going to be stored in the location and the agent variable that we have in here.

5
00:00:19,170 --> 00:00:25,050
So the next step is to go ahead and store these values on the cloud server so that we can come back

6
00:00:25,050 --> 00:00:26,640
at any time and read them.

7
00:00:26,760 --> 00:00:32,550
We're actually going to use PHP code that we written previously to store the username and the password

8
00:00:32,550 --> 00:00:36,060
that people enter when they log in to our fish and login pages.

9
00:00:36,060 --> 00:00:39,420
And we're going to modify it to suit our purpose in here.

10
00:00:39,870 --> 00:00:44,820
So if you don't remember how that code works, please go back and revise the fishing section of this

11
00:00:44,820 --> 00:00:45,390
course.

12
00:00:45,390 --> 00:00:48,930
But I have the file in here and I'll walk you through it quickly.

13
00:00:48,930 --> 00:00:55,620
As you can see, the file expects two arguments, an email and a pass, and it stores them in a username

14
00:00:55,620 --> 00:00:57,030
and a password variable.

15
00:00:57,390 --> 00:01:02,490
Then it creates a file called data.txt in a directory that is called data.

16
00:01:02,490 --> 00:01:06,480
And then it stores the username and the password to that file.

17
00:01:06,930 --> 00:01:13,200
And finally it will redirect the target person to the actual login page that they were logging in from.

18
00:01:13,620 --> 00:01:18,750
So straight away we know we don't need this line because we are not spoofing or phishing.

19
00:01:18,750 --> 00:01:20,370
Any login information.

20
00:01:20,370 --> 00:01:25,440
Next, I'm actually going to change the variable names in here because that doesn't really make sense.

21
00:01:25,440 --> 00:01:29,580
So right now it's expecting the username to be sent in here.

22
00:01:29,580 --> 00:01:31,980
And it's setting the username to the username.

23
00:01:31,980 --> 00:01:37,890
So I'm going to modify all of these values to location because that is the first value that we're going

24
00:01:37,890 --> 00:01:38,580
to send.

25
00:01:39,090 --> 00:01:42,540
And the second value that we're going to send is not the password.

26
00:01:42,540 --> 00:01:44,790
It's actually going to be the user agent.

27
00:01:44,790 --> 00:01:46,980
So again it's catching it in here.

28
00:01:46,980 --> 00:01:49,830
And then it's setting the password to the password.

29
00:01:50,070 --> 00:01:54,120
So we're going to change it to user agent.

30
00:01:54,720 --> 00:01:59,820
And we're also going to use meaningful names in here to catch the data that is being posted.

31
00:01:59,820 --> 00:02:03,150
So the location will be posted as location.

32
00:02:04,130 --> 00:02:07,880
And the user agent will be posted as user agent.

33
00:02:08,980 --> 00:02:12,370
So we actually haven't really modified the way that this code works.

34
00:02:12,370 --> 00:02:19,210
We've just been modifying the variable names so that the code just makes more sense and is more readable.

35
00:02:19,210 --> 00:02:23,740
So we're going to save this and we're going to go to File Zilla.

36
00:02:24,620 --> 00:02:30,620
And I already have the file here in my local storage, so I'm simply going to drag and drop it to my

37
00:02:30,620 --> 00:02:33,590
var ww HTML and perfect.

38
00:02:33,590 --> 00:02:36,050
We have the file in here also.

39
00:02:36,050 --> 00:02:38,630
As you can see the file is called Login.php.

40
00:02:38,630 --> 00:02:41,870
Again I just think that this is not representative enough.

41
00:02:41,870 --> 00:02:47,960
So we're just going to call it stored PHP instead of Login.php because it's simply going to store the

42
00:02:47,960 --> 00:02:49,550
information that we want.

43
00:02:50,970 --> 00:02:56,190
Also, if we go back to the code, you can see that it's going to store the data in a file that is called

44
00:02:56,190 --> 00:02:56,730
data dot.

45
00:02:56,730 --> 00:02:59,610
TXT in a directory that is called data.

46
00:02:59,640 --> 00:03:04,860
Now the code itself can create the file, but we have to create this directory for it.

47
00:03:04,890 --> 00:03:08,100
Again we did all of this previously in the fishing lecture.

48
00:03:08,100 --> 00:03:09,630
That's why I'm doing this quickly.

49
00:03:09,630 --> 00:03:12,450
So I'm just going to create a directory in here.

50
00:03:12,450 --> 00:03:14,340
We're going to call it data.

51
00:03:15,650 --> 00:03:21,890
And as shown in that lecture, we have to modify its permissions to seven, seven, seven so that anybody

52
00:03:21,890 --> 00:03:25,820
can write to this file and so that our code can actually write to it.

53
00:03:26,180 --> 00:03:33,050
So now that we have the PHP code that can receive this data and store it on file, we need to actually

54
00:03:33,050 --> 00:03:40,130
go back to our index dot HTML, because as you can see it is getting the location and the agent and

55
00:03:40,130 --> 00:03:41,780
it's storing them in variables.

56
00:03:41,780 --> 00:03:49,730
But we actually need this code, this page that we have right here to send these values to the store

57
00:03:49,730 --> 00:03:54,440
dot PHP so that it stores them for us in a text file.

58
00:03:54,950 --> 00:04:02,330
So we need to go back to Google and we need to ask it how do we send the requests using JavaScript so

59
00:04:02,330 --> 00:04:06,410
that we can send these values to the store dot php file.

60
00:04:07,030 --> 00:04:13,930
So we're going to look for send requests in JavaScript.

61
00:04:15,340 --> 00:04:16,000
Again.

62
00:04:16,000 --> 00:04:19,000
The first result is great from W3 schools.

63
00:04:19,360 --> 00:04:26,350
And as you can see, as usual you get really good description of how to send requests from HTML and

64
00:04:26,350 --> 00:04:28,600
JavaScript to a PHP file.

65
00:04:29,240 --> 00:04:33,020
Now there are two major types of Http requests.

66
00:04:33,020 --> 00:04:36,110
You can either send, Get, or Post requests.

67
00:04:36,110 --> 00:04:44,660
And as you can see in our code in here the store dot php file, it actually receives data that is sent

68
00:04:44,660 --> 00:04:46,220
as a Post request.

69
00:04:46,220 --> 00:04:49,190
So we need to make sure we send this data as post.

70
00:04:49,580 --> 00:04:56,090
So let's go ahead and see if there is an example in here that will teach us how to send data as post

71
00:04:56,630 --> 00:04:57,440
and perfect.

72
00:04:57,440 --> 00:05:02,330
As you can see we have it in here and it's explaining to us how to do it.

73
00:05:02,330 --> 00:05:07,520
Now this example in here is not actually sending any data, it's simply requesting a file.

74
00:05:07,520 --> 00:05:12,920
So we have a better example in here where the code is actually sending specific data.

75
00:05:12,920 --> 00:05:14,780
And this is what we want to do.

76
00:05:14,780 --> 00:05:16,910
So we're going to copy this.

77
00:05:16,910 --> 00:05:20,240
We're going to go to our code in here.

78
00:05:20,240 --> 00:05:23,780
And we're simply going to paste all of that code.

79
00:05:23,780 --> 00:05:26,930
And I'm just going to type it so it looks nicer.

80
00:05:26,930 --> 00:05:31,400
And we're going to have to modify it so that it suits our use in here.

81
00:05:31,400 --> 00:05:33,890
So as you can see the code is very simple.

82
00:05:33,890 --> 00:05:38,390
You can see it's as if it's a URL saying that it wants to open something.

83
00:05:38,390 --> 00:05:41,270
It's going to do it as post, which is what we want.

84
00:05:41,270 --> 00:05:44,990
And then you have the file that it's trying to open or request.

85
00:05:44,990 --> 00:05:49,670
And in our case it is called store dot PHP.

86
00:05:50,700 --> 00:05:52,170
This file right here.

87
00:05:52,680 --> 00:05:54,120
And then to this file.

88
00:05:54,120 --> 00:05:55,920
It's setting the request header.

89
00:05:55,920 --> 00:05:57,690
We don't need to play with this.

90
00:05:57,690 --> 00:05:59,400
You can keep it the way it is.

91
00:05:59,400 --> 00:06:04,110
And if you don't fully understand what this is again you can read what it means in here.

92
00:06:04,110 --> 00:06:07,860
But it basically specifies the type of content that you are sending.

93
00:06:08,430 --> 00:06:12,120
And finally, we have the values being sent in here.

94
00:06:12,510 --> 00:06:14,460
So you can see you have two types of this.

95
00:06:14,460 --> 00:06:16,170
First of all the argument.

96
00:06:16,760 --> 00:06:18,560
And then the value.

97
00:06:19,010 --> 00:06:25,460
So as you can see our code, it expects a location and a user agent as the arguments.

98
00:06:25,670 --> 00:06:27,920
So we're going to go back to the code in here.

99
00:06:27,920 --> 00:06:32,750
And we're going to modify the first argument and set it to location.

100
00:06:33,830 --> 00:06:40,700
And the second argument that we have in here after the ampersand is the user agent.

101
00:06:41,540 --> 00:06:43,160
Then we have to set the values.

102
00:06:43,160 --> 00:06:46,280
So right now the values are set to Henry and Ford.

103
00:06:46,280 --> 00:06:47,840
And we actually don't want that.

104
00:06:47,840 --> 00:06:52,400
We want the first value to be the location and the second value to be the agent.

105
00:06:53,030 --> 00:06:59,420
So we're going to remove Henry, and I'm actually going to close the quotation marks.

106
00:06:59,420 --> 00:07:01,520
I'm going to put two pluses.

107
00:07:01,520 --> 00:07:05,360
And inside it I'm going to put the location variable.

108
00:07:06,930 --> 00:07:08,940
And the reason why we're doing this.

109
00:07:08,940 --> 00:07:16,890
Because if I put this location inside the quotation mark, it will be treated as if it is a normal text.

110
00:07:17,310 --> 00:07:21,450
But I want to tell the programming language that this is not normal text.

111
00:07:21,450 --> 00:07:28,440
This is a variable that contains the whole value of the location, the latitude and the longitude.

112
00:07:28,440 --> 00:07:34,320
So that's why we had to break out of it by closing the quotations and adding the pluses in here.

113
00:07:34,930 --> 00:07:37,210
So we'll have to do the same here for Ford.

114
00:07:37,210 --> 00:07:40,150
So we're going to remove the value here of Ford.

115
00:07:40,150 --> 00:07:42,880
And in here we want to have the user agent.

116
00:07:42,880 --> 00:07:44,410
So I'm going to put a plus.

117
00:07:44,410 --> 00:07:50,650
And then I'm going to put the name of the variable that contains the user agent which is agent in here.

118
00:07:51,550 --> 00:07:53,410
So we're simply going to type it.

119
00:07:54,110 --> 00:07:55,580
And that is it.

120
00:07:55,580 --> 00:07:58,910
So this code is first going to request my store dot PHP.

121
00:07:58,910 --> 00:08:04,340
And then it's going to send it to values the location and the agent.

122
00:08:04,340 --> 00:08:09,590
And it's going to send them under the location argument and the user agent argument.

123
00:08:10,830 --> 00:08:16,320
So now that we're happy, we're going to do control S to save it and we're going to go back to FileZilla.

124
00:08:16,320 --> 00:08:18,750
It's going to ask us if we want to apply the changes.

125
00:08:18,750 --> 00:08:20,790
We're going to say yes, please apply them.

126
00:08:21,580 --> 00:08:28,150
And now that everything is working, let's go ahead and test our code and hopefully see if it works.

127
00:08:28,150 --> 00:08:33,070
So I have my target in here and we're simply going to refresh the page.

128
00:08:33,280 --> 00:08:34,210
And perfect.

129
00:08:34,210 --> 00:08:38,740
As you can see as the page loads it's asking for permission to get the location.

130
00:08:38,740 --> 00:08:45,010
Now this depends on your social engineering skills and also depends on the page that you get the target

131
00:08:45,010 --> 00:08:45,640
to load.

132
00:08:45,640 --> 00:08:54,220
But assuming that the target clicks on allow, let's go to our server and let's browse the data directory.

133
00:08:54,840 --> 00:08:56,070
We have nothing.

134
00:08:56,070 --> 00:08:58,200
Which means that I've done something wrong.

135
00:08:58,380 --> 00:09:03,720
So you can see in real life scenarios things aren't always going exactly as expected.

136
00:09:03,720 --> 00:09:11,850
But if we look at my code in here, I can straight away see that the location variable in here needs

137
00:09:11,850 --> 00:09:14,730
to be moved inside this curly bracket.

138
00:09:14,730 --> 00:09:21,570
Because as you can see in here, we are trying to access the location variable which is only available

139
00:09:21,570 --> 00:09:24,120
within these two curly brackets.

140
00:09:26,200 --> 00:09:28,090
So that's where I went wrong.

141
00:09:28,090 --> 00:09:31,660
We're going to cut this and paste it here.

142
00:09:32,780 --> 00:09:41,420
And I've also noticed that I am calling something that is called x http, but it's never defined anywhere.

143
00:09:42,150 --> 00:09:45,750
So this goes to me going through this page very quickly.

144
00:09:46,080 --> 00:09:53,190
If you read this page properly, you'll see that first of all, you actually have to define this Http

145
00:09:53,190 --> 00:09:54,390
method in here.

146
00:09:55,030 --> 00:09:56,650
So I need this line.

147
00:09:56,650 --> 00:10:00,760
So I've copied it and we're going to paste it in here.

148
00:10:02,180 --> 00:10:06,230
Before we actually go ahead and start using the Http.

149
00:10:06,230 --> 00:10:11,330
As you can see, it's first defining it so that the code knows what this is.

150
00:10:11,990 --> 00:10:13,790
So we're going to save it.

151
00:10:13,790 --> 00:10:16,130
We're going to save everything here.

152
00:10:16,460 --> 00:10:19,130
And let's go ahead and test it one more time.

153
00:10:19,130 --> 00:10:20,720
So we're going to refresh.

154
00:10:20,870 --> 00:10:22,130
We're going to allow.

155
00:10:23,160 --> 00:10:26,490
And let's go back in here and refresh the page.

156
00:10:26,760 --> 00:10:27,690
And perfect.

157
00:10:27,690 --> 00:10:30,750
As you can see we have our data text file.

158
00:10:30,750 --> 00:10:33,270
And if we open this file.

159
00:10:34,890 --> 00:10:41,430
As you can see, we got the latitude and the longitude, which can be translated to exact location of

160
00:10:41,430 --> 00:10:41,940
the target.

161
00:10:41,940 --> 00:10:44,580
And I'll show you how to do that in the in a minute.

162
00:10:44,580 --> 00:10:50,520
And then we also have the user agent which gives us the web browser, the operating system of the target

163
00:10:50,520 --> 00:10:54,210
and the architecture, and more information about the target.

164
00:10:54,890 --> 00:11:01,850
But let's go ahead and actually see how we can translate this longitude and latitude to an actual location.

165
00:11:01,850 --> 00:11:06,260
I'm simply going to copy them and we're going to go to Google.

166
00:11:07,310 --> 00:11:11,960
And we're going to look for GPS coordinate finder.

167
00:11:14,690 --> 00:11:16,670
Let's try the first result.

168
00:11:17,470 --> 00:11:20,290
And let's put the latitude first.

169
00:11:22,690 --> 00:11:25,480
And put the longitude next.

170
00:11:28,180 --> 00:11:30,790
Hit enter and perfect.

171
00:11:30,790 --> 00:11:38,770
It got us the exact location and if you zoom in, you will actually see that this is the exact location

172
00:11:38,770 --> 00:11:40,030
of our office.

173
00:11:40,030 --> 00:11:41,830
This is not an approximation.

174
00:11:41,830 --> 00:11:48,370
This is the exact location of the target computer that loaded this page.

175
00:11:48,370 --> 00:11:52,930
And as usual, the page loaded over Https with the lock icon.

176
00:11:52,930 --> 00:11:59,050
But the main benefit of this is that, like I said, you could be sharing this link with as many targets

177
00:11:59,050 --> 00:11:59,740
as you want.

178
00:11:59,740 --> 00:12:02,020
You can even use it in a phishing campaign.

179
00:12:02,020 --> 00:12:04,060
And you don't have to be always online.

180
00:12:04,060 --> 00:12:05,380
Like the case with beef.

181
00:12:05,380 --> 00:12:10,630
You could be just sitting around and then whenever you have the time, you can access your server,

182
00:12:10,630 --> 00:12:16,660
read your data file, and you'll be able to see the operating systems and the locations of all of the

183
00:12:16,660 --> 00:12:19,840
people that loaded your phishing page right here.

184
00:12:20,290 --> 00:12:26,410
You can also apply this information to do anything that you can think of, or extract any type of information

185
00:12:26,410 --> 00:12:27,880
that you want from the target.

186
00:12:27,880 --> 00:12:32,710
So you're not limited to extracting the GPS coordinates and the operating system.

187
00:12:32,710 --> 00:12:39,190
I try to show you how to do this from scratch, even by simply googling the codes that we need to use

188
00:12:39,190 --> 00:12:46,120
so that you can implement any idea or anything to extract any type of information, or launch any type

189
00:12:46,120 --> 00:12:48,040
of attack that you can think of.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,170 --> 00:00:06,920
So now that we learned how to register a domain name and how to link it to our web server, and how

2
00:00:06,920 --> 00:00:12,020
to enable Https so that when you double click it, you see Https, you see the lock.

3
00:00:12,020 --> 00:00:13,490
We're not getting any warning.

4
00:00:13,490 --> 00:00:15,260
We're not getting the dangerous icon.

5
00:00:15,260 --> 00:00:17,900
This website looks very, very believable.

6
00:00:17,900 --> 00:00:23,720
And like I said, if you're cloning a website that is not Facebook or Instagram, if it's a smaller

7
00:00:23,720 --> 00:00:29,660
website than these major websites, you can actually try to buy a domain name that sounds similar to

8
00:00:29,660 --> 00:00:30,710
the target website.

9
00:00:30,710 --> 00:00:36,710
And that way your domain name in here is going to be very believable and your website is going to be

10
00:00:36,710 --> 00:00:37,850
very trustworthy.

11
00:00:37,850 --> 00:00:43,310
But in this case, as you can see, we're using Facebook or Instagram or assuming the target is a very

12
00:00:43,310 --> 00:00:47,240
popular website that you can't buy a domain name that sounds like it.

13
00:00:47,240 --> 00:00:53,450
What you could do is you could, for example, have something like this login form or login page, or

14
00:00:53,450 --> 00:00:55,040
login or support.

15
00:00:55,040 --> 00:01:00,740
And then if you think that's not believable enough, you could set up a sub domain as we saw before

16
00:01:00,740 --> 00:01:01,730
using the key name.

17
00:01:01,730 --> 00:01:07,250
So now we have Facebook login.co and that is loading a login page for Facebook.

18
00:01:07,250 --> 00:01:10,790
So to many people this is very very very believable.

19
00:01:11,180 --> 00:01:16,130
Now in this lecture I actually want to show you a few more URL manipulation tricks.

20
00:01:16,130 --> 00:01:21,410
And then it's up to you to choose which is the most believable to your target.

21
00:01:21,940 --> 00:01:27,880
So the first method that I want to show you is by creating a directory on the server.

22
00:01:27,880 --> 00:01:31,360
So I'm already connected to the server here using FileZilla.

23
00:01:31,360 --> 00:01:32,500
We covered this before.

24
00:01:32,500 --> 00:01:35,590
So if you don't remember how to do that please revise the lecture.

25
00:01:35,590 --> 00:01:37,090
And what I'm going to do in here.

26
00:01:37,090 --> 00:01:40,090
I'm going to right click and create a new directory.

27
00:01:41,130 --> 00:01:43,320
I'm going to call this directory Facebook.

28
00:01:45,300 --> 00:01:47,970
And I'm going to double click it to access it.

29
00:01:48,570 --> 00:01:53,610
And in here I'm going to upload all of the website files for the fake Facebook page.

30
00:01:53,610 --> 00:01:55,140
And I have them already in here.

31
00:01:55,140 --> 00:02:02,370
I have my index, I have the login dot PHP, and I have the data directory that will contain the stored

32
00:02:02,370 --> 00:02:03,180
passwords.

33
00:02:03,330 --> 00:02:07,680
I'm going to drag and drop them all to my server and give it a minute to upload.

34
00:02:09,450 --> 00:02:15,690
And now that everything is uploaded inside a directory that is called Facebook, in our root directory,

35
00:02:15,690 --> 00:02:23,490
which is var ww HTML, we're going to be able to access this directory by simply typing Facebook.

36
00:02:24,490 --> 00:02:25,990
After the domain name.

37
00:02:25,990 --> 00:02:27,550
So if we hit enter.

38
00:02:28,560 --> 00:02:29,130
Again.

39
00:02:29,130 --> 00:02:33,810
As you can see, we get the page that we want, and anything that you're going to type in here is going

40
00:02:33,810 --> 00:02:38,070
to be stored in the data directory, because that's how we programmed it earlier.

41
00:02:38,700 --> 00:02:46,020
So now instead of doing Facebook login from.co now we have login form.co/facebook.

42
00:02:46,170 --> 00:02:51,360
Again depending on your target you might think this is more believable or this is more believable.

43
00:02:51,360 --> 00:02:52,680
You might want to do tests.

44
00:02:52,680 --> 00:02:53,910
It's up to you.

45
00:02:54,420 --> 00:02:59,880
And keep in mind, everything that I'm showing you in here applies regardless of what kind of website

46
00:02:59,880 --> 00:03:00,420
you have.

47
00:03:00,420 --> 00:03:06,330
Whether you have a website with a beef hook, whether you have a login page or a fishing page, or even

48
00:03:06,330 --> 00:03:11,130
if you have your own website and you want to just create some kind of a hierarchy within it.

49
00:03:12,180 --> 00:03:14,040
Now another trick that we can do.

50
00:03:14,040 --> 00:03:16,110
So let's just go back to the normal page.

51
00:03:17,060 --> 00:03:21,050
And this trick doesn't really require any settings, any back end settings.

52
00:03:21,080 --> 00:03:26,510
All you have to do is basically type whatever name you want, regardless of what it is.

53
00:03:26,510 --> 00:03:32,240
For example, again, we're going to type Facebook before the domain name, and we're going to put an

54
00:03:32,240 --> 00:03:33,500
ad after it.

55
00:03:33,500 --> 00:03:38,420
So when you do this you can actually see the browser is already kind of changing the color of it to

56
00:03:38,420 --> 00:03:39,050
gray.

57
00:03:39,320 --> 00:03:46,340
Because when you put the ad sign in here, the browser treats anything that comes before the ad sign

58
00:03:46,340 --> 00:03:47,540
as a username.

59
00:03:47,540 --> 00:03:53,570
So the browser is going to think you're trying to log in to a website called login form Co with a username

60
00:03:53,570 --> 00:03:54,800
that is called Facebook.

61
00:03:54,800 --> 00:04:01,100
Now this website doesn't really require any login of that sort, and therefore you'll simply be redirected

62
00:04:01,100 --> 00:04:02,660
to login form.co.

63
00:04:02,660 --> 00:04:05,420
But you could deliver this URL like this.

64
00:04:05,420 --> 00:04:10,430
And if we hit enter on it, as you can see we're going to go to login form.co.

65
00:04:10,430 --> 00:04:15,110
So you could even do something like instead of just Facebook you could say.

66
00:04:16,710 --> 00:04:17,760
Facebook.

67
00:04:18,660 --> 00:04:19,410
Com.

68
00:04:20,130 --> 00:04:23,100
Add login form co hit enter.

69
00:04:23,100 --> 00:04:25,800
And again as you can see we're back at login form.

70
00:04:25,800 --> 00:04:28,140
So depending on what domain name you bought.

71
00:04:28,140 --> 00:04:32,880
For example if you bought a domain name that is called support then you could have something like.

72
00:04:33,800 --> 00:04:37,160
Facebook at support.com.

73
00:04:37,190 --> 00:04:42,230
For example, if you manage to buy something like this and again, that's going to be very, very believable.

74
00:04:42,770 --> 00:04:47,300
Now I talk about a lot of delivery methods in my social engineering course.

75
00:04:47,300 --> 00:04:51,200
We're only going to cover a few in this course because this is not a social engineering course.

76
00:04:51,200 --> 00:04:52,820
This is a cloud course.

77
00:04:52,820 --> 00:04:55,850
And that's why we're focusing on the cloud aspect of it.

78
00:04:55,850 --> 00:04:58,670
But I will show you how to spoof emails later on.

79
00:04:59,000 --> 00:05:03,950
But if you want to learn more about delivery methods and how you're going to end up delivering the URLs

80
00:05:03,950 --> 00:05:09,230
of the pages that we created in here of the malicious pages or the phishing pages, or the beef hook

81
00:05:09,230 --> 00:05:13,490
pages, then I highly recommend checking out my social engineering course.

82
00:05:13,490 --> 00:05:18,980
You can check out the last lecture of this course to see all of my other courses, and to get exclusive

83
00:05:18,980 --> 00:05:23,090
discounts, because I always give my existing students special discounts.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: Command & Control Servers (C2  C&C)

1
00:00:00,050 --> 00:00:06,230
Previously, we covered a number of techniques to steal login information and to hack browsers to further

2
00:00:06,230 --> 00:00:07,700
exploit our targets.

3
00:00:08,060 --> 00:00:15,260
Now it's time to teach you how to hack or gain full remote control over any computer that is connected

4
00:00:15,260 --> 00:00:20,780
to the internet, regardless of their location and regardless of the operating system that they are

5
00:00:20,780 --> 00:00:24,680
running, whether it's running windows, Linux, or Apple Mac OS.

6
00:00:24,710 --> 00:00:32,540
What I mean by full remote control is the ability to fully and remotely control a target computer and

7
00:00:32,540 --> 00:00:40,100
access all of its resources from within the cloud, using what's known as C and C, or command and control

8
00:00:40,100 --> 00:00:40,850
servers.

9
00:00:41,150 --> 00:00:44,780
So you'll be able to execute any system commands that you want.

10
00:00:44,780 --> 00:00:51,410
You'll be able to access their file system, read, upload or download files, access system resources

11
00:00:51,410 --> 00:00:55,910
such as the camera and the keyboard, and even launch ransomware attacks.

12
00:00:56,390 --> 00:01:03,290
Or do anything on that computer as if it's your own computer, and do all of that from within the cloud.

13
00:01:03,320 --> 00:01:09,110
The main benefit of doing this through the cloud is that all of the heavy lifting is done on the cloud,

14
00:01:09,110 --> 00:01:12,830
and our cloud server is always online and always available.

15
00:01:12,860 --> 00:01:16,100
So once you set it up, you can continue about your day.

16
00:01:16,100 --> 00:01:20,480
And the targets that you hack will automatically connect to your cloud server.

17
00:01:20,480 --> 00:01:26,240
Then whenever you have the time, you can use your phone, computer or tablet, connect to your cloud

18
00:01:26,240 --> 00:01:29,960
server, and control all of the computers that you've hacked.

19
00:01:29,990 --> 00:01:34,160
Another added benefit is the increased privacy and anonymity.

20
00:01:34,160 --> 00:01:38,750
Because you'll never be communicating with these hacked computers directly.

21
00:01:38,750 --> 00:01:43,130
You will always be communicating with them through the cloud server.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,170 --> 00:00:05,630
Previously, we covered that the cloud consists of a number of computers.

2
00:00:05,810 --> 00:00:11,060
So a cloud server is basically just a computer that is accessible over the internet.

3
00:00:11,060 --> 00:00:16,580
And we saw that this computer is actually usually a cluster of computers that's hosted by Amazon or

4
00:00:16,580 --> 00:00:18,350
Linode or a cloud provider.

5
00:00:18,350 --> 00:00:22,790
And on that computer we are able to install any applications we want.

6
00:00:22,790 --> 00:00:28,100
And we saw previously that we installed Apache as a web server, which allowed us to run websites and

7
00:00:28,100 --> 00:00:29,450
host our own files.

8
00:00:29,450 --> 00:00:36,620
We installed beef, which allowed us to control browsers of the computers that visited our web pages.

9
00:00:36,620 --> 00:00:39,080
So the idea is basically it's just a computer.

10
00:00:39,080 --> 00:00:41,120
We can install any applications on it.

11
00:00:41,120 --> 00:00:44,660
And these applications listen on specific ports.

12
00:00:44,660 --> 00:00:51,500
And basically if a target goes to port 80, they'll be able to access my web server because Apache is

13
00:00:51,500 --> 00:00:52,490
running on 80.

14
00:00:52,490 --> 00:00:58,130
And then on port 3000, I had beef running, which allowed me to control their web browser through the

15
00:00:58,130 --> 00:00:59,720
browser exploitation framework.

16
00:00:59,720 --> 00:01:00,560
Beef.

17
00:01:00,560 --> 00:01:07,790
So what I want to cover in this series is to show you a number of examples of programs or frameworks

18
00:01:07,790 --> 00:01:12,740
that are only designed to be used as command and control servers.

19
00:01:12,860 --> 00:01:17,810
So C2 or CNC are short for Command and control Server.

20
00:01:17,810 --> 00:01:24,350
And basically it's a program that allows us to remotely communicate with computers that we hacked.

21
00:01:24,350 --> 00:01:26,900
So it allows us to execute commands.

22
00:01:26,900 --> 00:01:33,200
It allows us to access system resources like the file system, like the network interfaces, and so

23
00:01:33,200 --> 00:01:33,770
on.

24
00:01:33,770 --> 00:01:35,900
It allows us to receive sensitive data.

25
00:01:35,900 --> 00:01:40,160
So if you dump passwords or hashes, it allows us to pivot.

26
00:01:40,160 --> 00:01:44,630
So it allows us to use the computer that we hacked to hack into other computers.

27
00:01:44,630 --> 00:01:46,790
And obviously there's a lot more features.

28
00:01:46,790 --> 00:01:50,720
It really depends on the programmer of the C2 to implement these features.

29
00:01:50,720 --> 00:01:55,700
So there's a lot of different programs that can be used as c2's any type of C2.

30
00:01:55,730 --> 00:02:01,640
It typically is made up of two parts an agent or a client or a backdoor.

31
00:02:01,670 --> 00:02:05,960
That's basically a program that you will run on the target computer.

32
00:02:05,960 --> 00:02:10,670
So you need to social engineer the target person, or you might have to run it yourself after gaining

33
00:02:10,670 --> 00:02:11,660
initial access.

34
00:02:11,660 --> 00:02:15,620
But this program needs to be executed on the target system.

35
00:02:15,920 --> 00:02:17,870
The second part is the server.

36
00:02:17,870 --> 00:02:23,300
And that is installed on your cloud server, which will receive the connections from the agent or the

37
00:02:23,300 --> 00:02:24,800
client, or the backdoor.

38
00:02:25,630 --> 00:02:27,610
So just giving you a quick diagram.

39
00:02:27,610 --> 00:02:29,350
In here we have the hacker.

40
00:02:29,350 --> 00:02:31,150
You have your server on the cloud.

41
00:02:31,150 --> 00:02:32,230
This could be on linode.

42
00:02:32,230 --> 00:02:34,600
This could be on AWS.

43
00:02:34,630 --> 00:02:36,100
It can be on blue motion.

44
00:02:36,100 --> 00:02:37,180
It doesn't really matter.

45
00:02:37,180 --> 00:02:39,970
You have a C2 application installed on it.

46
00:02:39,970 --> 00:02:43,510
And like I said there is a lot of options and we will talk about them later.

47
00:02:43,510 --> 00:02:47,980
You're going to use the C2 to create an agent or a dropper or a backdoor.

48
00:02:47,980 --> 00:02:53,470
Like I said, this is the part of the C2 that needs to be executed on the target computer.

49
00:02:53,470 --> 00:02:55,960
You're going to need to use social engineering.

50
00:02:55,960 --> 00:03:02,080
Or maybe if you already have initial access to the target, you can go ahead and deliver it to the target

51
00:03:02,080 --> 00:03:03,010
computer.

52
00:03:03,490 --> 00:03:11,680
And once executed on the target computer, it's going to send a connection back to the C2 server.

53
00:03:11,680 --> 00:03:15,040
And this is where C2 is are very, very useful.

54
00:03:15,040 --> 00:03:18,250
First of all, you need that connection to be encrypted.

55
00:03:18,250 --> 00:03:20,890
You need it to bypass security.

56
00:03:20,890 --> 00:03:22,120
And they're really cool.

57
00:03:22,120 --> 00:03:28,780
Thing about it is that the connection is sent to a cloud server, and it's not sent to your own computer.

58
00:03:28,780 --> 00:03:33,700
So your computer could be off, you could be out on holidays, you could be sleeping.

59
00:03:33,700 --> 00:03:34,900
It doesn't really matter.

60
00:03:34,900 --> 00:03:42,100
Once your target execute the program, the the dropper or the backdoor, they will send the connection

61
00:03:42,100 --> 00:03:45,340
to the cloud server, which will keep that connection for you.

62
00:03:45,340 --> 00:03:50,560
Whenever you have the time, you can come back and log in using SSH or whatever service you want to

63
00:03:50,560 --> 00:03:53,980
use and communicate with your target or targets.

64
00:03:53,980 --> 00:03:58,360
So you can have multiple targets in here, all connected back to your C2.

65
00:03:58,360 --> 00:04:03,760
And whenever you want to go ahead and communicate with them, you connect to your C2 and then communicate

66
00:04:03,760 --> 00:04:09,100
to the targets, access their file system, access their resources, dump passwords, or do whatever

67
00:04:09,100 --> 00:04:10,060
you want to do.

68
00:04:10,570 --> 00:04:15,070
The really cool thing about this is that the connection is sent to the server, which is always on,

69
00:04:15,070 --> 00:04:17,680
always reliable, always has internet access.

70
00:04:17,680 --> 00:04:23,950
It doesn't require you to set up any forwarding or tunnels, and also adds a little bit of anonymity

71
00:04:23,950 --> 00:04:30,760
and privacy because the connection is sent back to the C2 server on the cloud and is not sent directly

72
00:04:30,760 --> 00:04:31,750
back to you.

73
00:04:32,140 --> 00:04:38,530
So there are many C2 frameworks, and it can be really hard to choose which one to use.

74
00:04:38,530 --> 00:04:44,260
I will be covering some of the best and the most unique ones, but you should also explore more once

75
00:04:44,260 --> 00:04:45,040
you have the time.

76
00:04:45,040 --> 00:04:49,660
Once you're done with this section, once you learn how to use the frameworks that I'm going to cover,

77
00:04:49,660 --> 00:04:54,280
you'll be able to play with other ones and discover their features easily.

78
00:04:54,310 --> 00:04:59,770
A really good resource to compare these C2 frameworks is the C2 matrix.

79
00:04:59,770 --> 00:05:05,530
Now, it might be a little bit outdated in terms of the comparisons that it has, but it's very useful

80
00:05:05,530 --> 00:05:10,600
in the way that it lays everything down in front of you, and you can compare them based on their features.

81
00:05:10,600 --> 00:05:13,090
I'll include it in the resources of this lecture.

82
00:05:13,090 --> 00:05:19,120
And basically if you scroll down by simply clicking here, you'll be able to access the actual matrix.

83
00:05:19,120 --> 00:05:22,540
So in here you can see all of the different C2 frameworks.

84
00:05:22,540 --> 00:05:25,870
Empire, for example, is the one that we're going to be covering very soon.

85
00:05:26,140 --> 00:05:27,940
You can see the version they tested.

86
00:05:27,940 --> 00:05:30,460
So we'll be using a much newer version than this.

87
00:05:30,460 --> 00:05:35,920
And then from here you can check what kind of UI they have, what kind of channels they use, what kind

88
00:05:35,920 --> 00:05:40,810
of agents, the capabilities or the features, the support and so on.

89
00:05:41,080 --> 00:05:47,680
If you go back to the home page, you can actually go to the questionnaire in here and it'll ask you

90
00:05:47,680 --> 00:05:50,950
a few questions on what you're expecting from your C2 framework.

91
00:05:50,950 --> 00:05:55,510
So you can say you want to be able to have multiple users using this framework.

92
00:05:55,510 --> 00:05:56,200
Click next.

93
00:05:56,200 --> 00:05:59,620
And then it's going to ask you what kind of channels you want to support.

94
00:05:59,620 --> 00:06:04,720
You want to say, I want to have TCP and Http, and then go ahead and then based on the answers you

95
00:06:04,720 --> 00:06:09,760
have, it will tell you which C2 frameworks you can actually use from here.

96
00:06:10,180 --> 00:06:12,820
Now some of this information might be outdated.

97
00:06:12,820 --> 00:06:18,730
For example, Empire, which is the C2 that we're going to cover soon, does actually have a GUI button

98
00:06:18,730 --> 00:06:18,970
here.

99
00:06:18,970 --> 00:06:19,840
It says it doesn't.

100
00:06:19,840 --> 00:06:25,480
So some of the information in here might be outdated, but like I said, it's a great resource to still

101
00:06:25,480 --> 00:06:29,080
compare the C2 frameworks and see which ones are worth trying.

102
00:06:29,500 --> 00:06:35,410
Also, if you want to actually see the full comparison between them, if we go back to the explorer

103
00:06:35,410 --> 00:06:42,250
in here and click on View Source, which is basically a Google sheet, again, you'll get all of the

104
00:06:42,250 --> 00:06:47,740
C2 frameworks in here, the different ones, you'll see the license, the price if they are paid, and

105
00:06:47,740 --> 00:06:49,960
you can see some of them are actually very expensive.

106
00:06:49,960 --> 00:06:55,510
You can see the links where you can get them from, and a list of all of the features that you can get

107
00:06:55,510 --> 00:06:56,470
with these frameworks.

108
00:06:56,470 --> 00:07:00,820
And then you can contrast and compare the features and see which ones you want to use.

109
00:07:01,270 --> 00:07:08,320
Now personally, my favorite free C2 framework is Empire, but before choosing to cover it, I actually

110
00:07:08,320 --> 00:07:13,300
posted a poll on our social media asking which one do people prefer?

111
00:07:13,300 --> 00:07:16,480
So as you can see, these are the top four in my opinion right now.

112
00:07:16,480 --> 00:07:20,950
Now there is more that I can put in here at number four, but you can only have four in the poll in

113
00:07:20,950 --> 00:07:21,400
here.

114
00:07:21,400 --> 00:07:24,100
And as you can see, most people preferred Empire.

115
00:07:24,100 --> 00:07:24,910
So that's why we're.

116
00:07:25,300 --> 00:07:27,580
Going to be covering Empire next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: Hacking Windows, Linux & Apple Mac OS From the Cloud

1
00:00:00,020 --> 00:00:03,980
In this lecture, and in the next few lectures, we're going to be covering Empire.

2
00:00:03,980 --> 00:00:05,870
Just like any other see2 framework.

3
00:00:05,870 --> 00:00:08,240
It allows us to remotely control computers.

4
00:00:08,240 --> 00:00:13,430
But one of the main cool things about Empire is that it allows us to control windows, Linux, and Apple

5
00:00:13,430 --> 00:00:14,000
Mac OS.

6
00:00:14,000 --> 00:00:16,940
So pretty much all operating systems on computers.

7
00:00:17,000 --> 00:00:20,330
It's got a console and a web interface, which is amazing.

8
00:00:20,330 --> 00:00:25,460
So you can actually use it using the terminal, or you can use it from any device that has a browser.

9
00:00:25,460 --> 00:00:27,740
So you can even use it from your mobile phone.

10
00:00:28,280 --> 00:00:33,380
It uses encrypted communication with AES and TLS as an option.

11
00:00:33,710 --> 00:00:40,070
It's got built in obfuscation and evasion, which helps to bypass antivirus programs and bypass intrusion

12
00:00:40,070 --> 00:00:42,020
systems and detection systems.

13
00:00:42,020 --> 00:00:48,230
And one of the really cool things also about it is the fact that it has a massive library of post-exploitation

14
00:00:48,230 --> 00:00:48,890
frameworks.

15
00:00:48,890 --> 00:00:55,010
So in many cases, gaining access to the target system is only the start of achieving your goal.

16
00:00:55,010 --> 00:01:00,230
Once you gain initial access, a lot of the time you need to pivot into different computers or you need

17
00:01:00,230 --> 00:01:04,790
to escalate your privileges, or you want to extract information from the target computer.

18
00:01:04,790 --> 00:01:10,850
And Empire agents have a huge library of modules that allow you to do so much, and you're going to

19
00:01:10,850 --> 00:01:14,330
see that once we go ahead and cover more of this tool.

20
00:01:14,690 --> 00:01:17,660
It's also got team collaboration or multiplayer.

21
00:01:17,660 --> 00:01:23,420
So if you're working within a team, you can actually have different users accessing this command and

22
00:01:23,420 --> 00:01:28,310
control server and controlling the computers that you guys are trying to hack or compromise.

23
00:01:28,460 --> 00:01:31,970
You can even program how the agent and the listener communicate.

24
00:01:31,970 --> 00:01:35,060
You can trigger actions based on certain events.

25
00:01:35,060 --> 00:01:37,250
There's so much that you can do with this.

26
00:01:37,250 --> 00:01:38,750
It's actually so huge.

27
00:01:38,750 --> 00:01:44,540
And the post exploitation aspect of it is so huge that it can actually make a full course on this tool.

28
00:01:44,780 --> 00:01:49,640
So imagine this you're going to have Empire installed on a cloud computer.

29
00:01:49,640 --> 00:01:54,860
You're going to use it to create backdoors when these backdoors are executed on a computer.

30
00:01:54,860 --> 00:01:57,020
For example, here we have a windows computer.

31
00:01:57,020 --> 00:02:00,890
It's going to send a reverse connection to your cloud server.

32
00:02:00,890 --> 00:02:07,130
And then whenever you want, you can come in from your phone, from a computer, from any device that

33
00:02:07,130 --> 00:02:13,280
has a browser and communicate with your cloud computer and communicate with the computer that you hacked.

34
00:02:13,280 --> 00:02:19,550
And like I said, it doesn't only support windows, it supports Linux and Mac OS X, and you can use

35
00:02:19,550 --> 00:02:22,490
it to actually control multiple devices at the same time.

36
00:02:22,490 --> 00:02:25,460
So that's the main thing about command and control servers.

37
00:02:25,670 --> 00:02:31,580
And not only it allows you to control multiple computers at the same time, it also allows you to work

38
00:02:31,580 --> 00:02:32,270
within a team.

39
00:02:32,270 --> 00:02:38,270
So you have multiple hackers controlling multiple computers all through the cloud, through a command

40
00:02:38,270 --> 00:02:39,650
and control server.

41
00:02:39,650 --> 00:02:43,430
And all of the communication is going to be encrypted.

42
00:02:43,430 --> 00:02:45,020
So that's why it's so cool.

43
00:02:45,020 --> 00:02:46,280
That's why it's so powerful.

44
00:02:46,280 --> 00:02:51,740
And like I said, there are so many tools, so many modules and so many features that it has that I

45
00:02:51,740 --> 00:02:53,630
can actually make a full course on this.

46
00:02:54,140 --> 00:02:58,040
So let's go ahead and install it on our cloud server.

47
00:02:58,550 --> 00:03:02,630
So I've already logged in to my Kali install on Amazon AWS.

48
00:03:02,630 --> 00:03:06,080
And to install it we're going to go to their git repository.

49
00:03:06,080 --> 00:03:08,780
Now there is many empire git repositories.

50
00:03:08,780 --> 00:03:11,570
I'm going to include this one in the resources of this lecture.

51
00:03:11,570 --> 00:03:13,970
This is the most updated recent one.

52
00:03:13,970 --> 00:03:15,680
It's from BK security.

53
00:03:15,680 --> 00:03:21,230
So we're simply going to click on the code, copy the repo URL.

54
00:03:21,230 --> 00:03:24,470
And we're simply going to come to our cloud server.

55
00:03:24,470 --> 00:03:29,390
We're going to navigate to the opt directory using the CD command.

56
00:03:29,420 --> 00:03:34,010
This is the directory where you should be installing optional programs, hence the name opt.

57
00:03:34,310 --> 00:03:40,880
And before writing or downloading stuff to this directory, we have to change its ownership to the user

58
00:03:40,880 --> 00:03:42,920
that we are logged in with, which is Kali.

59
00:03:43,040 --> 00:03:46,370
So to do that we're going to do c ch own.

60
00:03:47,470 --> 00:03:51,430
The user that we want to change the ownership to is Cali.

61
00:03:51,460 --> 00:03:58,540
It's part of the Cali user group and the directory that we want to change the ownership of is the opt

62
00:03:58,540 --> 00:03:59,320
directory.

63
00:03:59,830 --> 00:04:02,260
And we need to run this command as root.

64
00:04:02,260 --> 00:04:07,210
So we're going to put the cursor at the start and type sudo before the command.

65
00:04:07,810 --> 00:04:09,490
So it's a very simple command.

66
00:04:09,490 --> 00:04:14,020
We're running it as root because we are trying to change the ownership of this directory.

67
00:04:14,020 --> 00:04:19,300
We're saying that we're using the chmod command to change the ownership of the opt directory.

68
00:04:19,300 --> 00:04:23,860
And we want to give that ownership to a user that is called Cali, which is the user that we are logged

69
00:04:23,860 --> 00:04:24,370
in with.

70
00:04:24,370 --> 00:04:26,890
And it is part of the Cali user group.

71
00:04:27,340 --> 00:04:32,320
If we hit enter, you'll see that the command will get executed without displaying any errors, meaning

72
00:04:32,320 --> 00:04:34,600
that the command got executed properly.

73
00:04:34,600 --> 00:04:37,630
I also want to set a password for the Cal user.

74
00:04:37,630 --> 00:04:40,720
We've never done this and you're going to need that for the installation.

75
00:04:40,720 --> 00:04:47,200
So to set a password for a user, we're going to use the passwd command followed by the user that we

76
00:04:47,200 --> 00:04:48,610
want to set the password to.

77
00:04:48,610 --> 00:04:50,980
And in this case it's the Cali user.

78
00:04:51,100 --> 00:04:53,980
Again because we're trying to set a password for a user.

79
00:04:53,980 --> 00:04:58,000
We're going to have to run this command as sudo as admin or as root.

80
00:04:58,000 --> 00:05:02,320
And that's why we're putting sudo before the command I'm going to hit enter.

81
00:05:02,320 --> 00:05:04,270
And it's going to ask me for the new password.

82
00:05:04,270 --> 00:05:07,120
I'm going to type the password using my keyboard.

83
00:05:07,120 --> 00:05:10,030
But as you can see the password is not being displayed.

84
00:05:10,030 --> 00:05:11,110
That is completely fine.

85
00:05:11,110 --> 00:05:17,110
That's a security feature so that people beside you will not be able to see the password, but type

86
00:05:17,110 --> 00:05:19,300
the password using your keyboard, hit enter.

87
00:05:19,300 --> 00:05:21,040
It's going to ask you to type it again.

88
00:05:21,040 --> 00:05:23,830
I'm going to type it again and hit enter again.

89
00:05:23,830 --> 00:05:28,900
And as you can see, it's telling us that the password got updated successfully, which means that now

90
00:05:28,900 --> 00:05:32,020
we have set a password for this user, the Cali user.

91
00:05:32,590 --> 00:05:38,260
So now I'm going to clear the screen and we can actually go ahead and use the git clone command.

92
00:05:38,260 --> 00:05:45,400
And we're going to do dash dash recursive so that we can recursively download all the files that is

93
00:05:45,400 --> 00:05:46,900
within this repository.

94
00:05:46,900 --> 00:05:53,290
So we're using git to clone or download all the files on all the directories that exist within this

95
00:05:53,290 --> 00:05:54,040
repository.

96
00:05:54,040 --> 00:05:57,370
The one that we just copied that contains Empire's code.

97
00:05:57,370 --> 00:06:00,610
We're going to hit enter and just give it its time to download it.

98
00:06:02,120 --> 00:06:05,540
Now that everything is downloaded, I'm going to clear the screen.

99
00:06:05,540 --> 00:06:11,120
And if we list the files and directories in the current working directory, you'll see that we have

100
00:06:11,120 --> 00:06:13,340
another directory now called Empire.

101
00:06:13,370 --> 00:06:16,280
We can navigate to it using the CD command.

102
00:06:16,310 --> 00:06:17,720
CD Empire.

103
00:06:17,720 --> 00:06:23,510
And if we list again in here you'll see we have all the files in the directories needed to run this

104
00:06:23,510 --> 00:06:24,050
tool.

105
00:06:24,050 --> 00:06:30,620
And because we haven't installed a tool yet, the most important directory for us now is the setup directory.

106
00:06:30,620 --> 00:06:35,750
So if you want to list what's inside it you can simply do LS setup.

107
00:06:35,750 --> 00:06:38,480
And as you can see we have three executables.

108
00:06:38,480 --> 00:06:39,770
That's why they are green.

109
00:06:39,770 --> 00:06:45,710
And before running the install.sh we're going to run this script right here that will check the latest

110
00:06:45,710 --> 00:06:50,390
tag and make sure that we run the most stable version of Empire.

111
00:06:50,390 --> 00:06:56,690
So to do that we're simply going to do dot forward slash setup because the file is inside the setup

112
00:06:56,690 --> 00:06:57,320
directory.

113
00:06:57,320 --> 00:07:01,190
And we want to run a file that is called checkout latest Tagish.

114
00:07:01,220 --> 00:07:02,480
This file right here.

115
00:07:02,480 --> 00:07:04,190
That's why we're typing it like so.

116
00:07:04,190 --> 00:07:08,000
And we're putting the dot before it so that we run it as an executable.

117
00:07:08,540 --> 00:07:09,920
I'm going to hit enter.

118
00:07:10,250 --> 00:07:15,140
And as you can see it's checking the latest tag for me and switching to the most stable tag.

119
00:07:15,140 --> 00:07:19,970
And now that that's done we can simply go ahead and run the install script.

120
00:07:19,970 --> 00:07:23,180
So it's going to be very similar to the previous command.

121
00:07:23,180 --> 00:07:29,720
But instead of running the check latest Tagish, we're going to run the Install.sh.

122
00:07:30,320 --> 00:07:31,760
I'm going to hit enter.

123
00:07:32,540 --> 00:07:38,060
And right now it's simply asking me for the password for the user Kali, the one that we just set in

124
00:07:38,060 --> 00:07:39,020
the previous step.

125
00:07:39,020 --> 00:07:40,640
So I'm going to put the password.

126
00:07:40,640 --> 00:07:43,700
And as you type the password you're not going to see it on screen.

127
00:07:43,700 --> 00:07:44,870
That is completely fine.

128
00:07:44,870 --> 00:07:47,510
Like I said this is similar to when we set the password.

129
00:07:47,510 --> 00:07:51,680
When you type a password through the terminal, you won't actually see it on the screen.

130
00:07:51,680 --> 00:07:54,650
So now that I put the password in I'm going to hit enter.

131
00:07:54,650 --> 00:07:57,980
Now you want to give this some time to actually go ahead and install it.

132
00:07:57,980 --> 00:07:59,240
It's a huge framework.

133
00:07:59,240 --> 00:08:00,980
Like I said I've said this multiple times.

134
00:08:00,980 --> 00:08:04,460
So it will take some time to download a lot of packages and install them.

135
00:08:04,460 --> 00:08:10,280
But as it's doing that, I want to go ahead and show you the wiki of this framework.

136
00:08:10,280 --> 00:08:17,540
So if we click here on the wiki, on the GitHub page and it directs you to this website, and in here

137
00:08:17,540 --> 00:08:20,180
you can see that you get a quick start guide.

138
00:08:20,180 --> 00:08:25,340
If you go on the installation before the quick start, it'll actually tell you how to install it.

139
00:08:25,340 --> 00:08:30,260
So all the commands that I executed right here, it's going to explain to you what they do and why you

140
00:08:30,260 --> 00:08:30,740
do them.

141
00:08:30,740 --> 00:08:34,130
So I'm not really a genius that just knew what to do.

142
00:08:34,130 --> 00:08:38,450
Obviously you can see it by looking at what's inside the directories in there, what kind of commands

143
00:08:38,450 --> 00:08:39,140
you can run.

144
00:08:39,140 --> 00:08:44,990
But as you can see, everything is nicely documented and explained in here, and you even have very

145
00:08:44,990 --> 00:08:50,120
nice documentation on some of the main features of the framework and here on the left, so you can spend

146
00:08:50,120 --> 00:08:53,540
some time to get to know the framework and get to know how to use it.

147
00:08:54,100 --> 00:08:59,110
So as the installation goes ahead, it's going to ask you a few questions if you want to install extra

148
00:08:59,110 --> 00:08:59,800
packages.

149
00:08:59,800 --> 00:09:05,890
And usually your answer is going to be yes, because that's going to allow you to do more with the framework.

150
00:09:05,890 --> 00:09:12,280
For example, this question right here is asking us if we want to install XR and boom utils.

151
00:09:12,280 --> 00:09:14,950
These are packages and it's telling you what they're needed for.

152
00:09:14,950 --> 00:09:21,970
They're needed to generate dmg stagers, which basically mean the DMG is the package file format for

153
00:09:21,970 --> 00:09:23,440
Apple Mac OS computers.

154
00:09:23,440 --> 00:09:31,030
So basically these packages are needed to generate DMG backdoors that can be used on Apple Mac OS computers

155
00:09:31,030 --> 00:09:32,140
so that you can hack them.

156
00:09:32,140 --> 00:09:34,330
So obviously the answer is going to be yes.

157
00:09:34,600 --> 00:09:39,460
And it's going to ask you a few similar questions to these, which will allow you to generate more backdoors

158
00:09:39,460 --> 00:09:42,130
to more systems or do more post exploitation.

159
00:09:42,130 --> 00:09:47,440
So the answer is usually going to be yes, unless you know that you really don't want whatever package

160
00:09:47,440 --> 00:09:48,970
it's offering you to install.

161
00:09:49,700 --> 00:09:56,480
So again, now you're being asked if you want to install OpenJDK, which is needed to generate Jar or

162
00:09:56,480 --> 00:09:59,750
Java stagers which run on multiple operating systems.

163
00:09:59,750 --> 00:10:01,760
Again, obviously the answer is going to be yes.

164
00:10:01,760 --> 00:10:02,900
Please do that for me.

165
00:10:03,050 --> 00:10:10,610
Again, you're being asked if you want to install the Nim package and min GW, which is needed to generate

166
00:10:10,610 --> 00:10:11,300
Nim stagers.

167
00:10:11,300 --> 00:10:12,920
So the answer is going to be yes.

168
00:10:13,930 --> 00:10:14,860
So perfect.

169
00:10:14,860 --> 00:10:17,500
Now the installation is complete.

170
00:10:17,500 --> 00:10:21,700
It's telling you how to actually start Empire by running this command.

171
00:10:21,730 --> 00:10:23,440
PS Empire server start.

172
00:10:23,440 --> 00:10:27,190
This is the command to use the terminal based client.

173
00:10:27,190 --> 00:10:28,660
So we're not actually going to be using it.

174
00:10:28,660 --> 00:10:31,630
But if you ever wanted to use it, this is how you're going to use it.

175
00:10:31,630 --> 00:10:35,860
And basically right now we are at this stage.

176
00:10:35,860 --> 00:10:39,010
So now we have Empire running on the cloud.

177
00:10:39,010 --> 00:10:44,710
And next I'm going to show you how to listen for incoming connections, create a backdoor and then hack

178
00:10:44,710 --> 00:10:46,600
computers using this program.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,410 --> 00:00:06,200
So now that we have Empire installed on the cloud, it's telling us this is how we run empires.

2
00:00:06,230 --> 00:00:10,850
So first of all, you're going to have to go to the directory where you have Empire installed.

3
00:00:10,850 --> 00:00:12,410
So it's an opt empire.

4
00:00:12,440 --> 00:00:17,420
Obviously we're already at it because we already did the CD command to navigate to this directory.

5
00:00:17,420 --> 00:00:21,800
So right now to run it we're simply going to do the command that it's telling us to do.

6
00:00:21,800 --> 00:00:26,330
So it's dot forward slash PS dash empire.

7
00:00:26,630 --> 00:00:28,700
And we want to run the server.

8
00:00:29,520 --> 00:00:30,480
We're going to hit enter.

9
00:00:30,480 --> 00:00:33,630
And this is going to start the Empire server on the cloud.

10
00:00:33,630 --> 00:00:38,460
So it's basically going to start this component of the program on the cloud.

11
00:00:38,730 --> 00:00:43,140
Now because this is the first time we're starting it, it's going to take a little bit longer than usual

12
00:00:43,140 --> 00:00:47,670
to initialize itself and initialize all the packages that it uses.

13
00:00:47,670 --> 00:00:53,880
And once done, as you can see, it's telling us that the web interface can be accessed through this

14
00:00:53,880 --> 00:00:54,510
URL.

15
00:00:54,510 --> 00:01:00,870
Now you should substitute the zeros with the IP of your computer, of your cloud server, and this is

16
00:01:00,870 --> 00:01:04,980
the port that it runs on 1337 lead in hacker language.

17
00:01:05,130 --> 00:01:12,420
So we're going to go ahead to our server as usual because that port is not enabled on our server in

18
00:01:12,420 --> 00:01:13,350
our firewall.

19
00:01:13,350 --> 00:01:16,590
So we're going to click the cloud server that we created.

20
00:01:16,590 --> 00:01:18,450
We're going to go to the security.

21
00:01:18,450 --> 00:01:20,640
We're going to click on the security group.

22
00:01:20,640 --> 00:01:23,070
We're going to edit the inbound rules.

23
00:01:23,070 --> 00:01:24,690
We're going to add a new rule.

24
00:01:24,690 --> 00:01:26,670
And we're going to add that port to it.

25
00:01:26,670 --> 00:01:31,920
Now I'm doing this very quickly because we've done this to pretty much any tool that we installed on

26
00:01:31,920 --> 00:01:32,550
the server.

27
00:01:32,550 --> 00:01:34,140
I've covered it multiple times.

28
00:01:34,140 --> 00:01:35,550
So you should know how to do this.

29
00:01:35,550 --> 00:01:37,530
If you don't, you should go back and revise.

30
00:01:37,530 --> 00:01:38,400
What is this?

31
00:01:38,400 --> 00:01:46,620
But basically we simply allowed connections to the port that Empire server uses, which is port 1337.

32
00:01:47,380 --> 00:01:54,640
So now that we did that, we can go back to my instances and we can copy the IP of this instance, which

33
00:01:54,640 --> 00:01:55,600
is right here.

34
00:01:56,410 --> 00:02:02,140
And we're going to open it in a new tab, and we're going to put a colon one three, three, seven,

35
00:02:02,140 --> 00:02:04,960
which is where the Empire server runs.

36
00:02:04,960 --> 00:02:11,290
We're going to put a forward slash index dot HTML because that's the main login page for the tool.

37
00:02:11,830 --> 00:02:12,520
And perfect.

38
00:02:12,520 --> 00:02:18,700
As you can see, you get a nice normal web interface that is asking us for a username and a password.

39
00:02:18,700 --> 00:02:22,810
We're going to log in with the default username and password, but then we will change them after we

40
00:02:22,810 --> 00:02:23,440
log in.

41
00:02:23,440 --> 00:02:30,280
So the default username is Empire admin and the default password password 123.

42
00:02:30,280 --> 00:02:32,830
We're also going to copy this IP in here.

43
00:02:32,830 --> 00:02:35,800
And we're going to paste it in here instead of localhost.

44
00:02:35,800 --> 00:02:38,410
Because we're not running this on the local host.

45
00:02:38,410 --> 00:02:40,420
We're actually running it on the cloud.

46
00:02:40,570 --> 00:02:42,160
We're going to click submit.

47
00:02:42,910 --> 00:02:43,660
And perfect.

48
00:02:43,660 --> 00:02:45,910
Now we're logged in to Empire.

49
00:02:45,910 --> 00:02:51,460
This is the web interface of the tool, and as you can see, it can be fully controlled from the web.

50
00:02:51,460 --> 00:02:58,720
And that's why I said you can use this tool from any device as long as it has a web browser.

51
00:02:58,720 --> 00:03:03,190
So all of the hard work, all of the computation is done here.

52
00:03:03,190 --> 00:03:08,260
It's done on the cloud, and that's why you can connect to it using any device as long as you have a

53
00:03:08,260 --> 00:03:14,050
web interface, because your personal computer or your phone is simply rendering a website, and all

54
00:03:14,050 --> 00:03:17,680
of the code is being executed on the cloud, on the web server.

55
00:03:18,260 --> 00:03:24,350
So before we start using this tool, it's very important to go ahead and change our username and password,

56
00:03:24,350 --> 00:03:27,530
because we logged in with the default username and password.

57
00:03:27,530 --> 00:03:29,810
And this is exposed to the cloud.

58
00:03:29,810 --> 00:03:35,420
So if you hack computers anybody is going to be able to come in and put this IP, put this port and

59
00:03:35,420 --> 00:03:38,360
log in using the default username and password.

60
00:03:38,360 --> 00:03:41,690
So it's very very important to go ahead and change that.

61
00:03:41,690 --> 00:03:45,560
So to do that we're simply going to go here to the left menu.

62
00:03:45,620 --> 00:03:48,860
We're going to talk about all of these options in here later on.

63
00:03:48,860 --> 00:03:52,550
But we're interested in going to the users to add a new user.

64
00:03:52,550 --> 00:03:56,690
And as you can see in here we have the default user which is Empire Admin.

65
00:03:56,690 --> 00:03:59,960
We're going to click create to create a new user.

66
00:03:59,960 --> 00:04:03,380
You can put any username you want I'm going to put my username.

67
00:04:03,380 --> 00:04:05,600
You can put any password you want as well.

68
00:04:05,600 --> 00:04:07,040
So I'm going to put a password.

69
00:04:07,430 --> 00:04:09,530
You can also set this user to an admin.

70
00:04:09,530 --> 00:04:12,260
And I'm going to do that because that's going to be my main user.

71
00:04:12,260 --> 00:04:14,420
And I'm going to click submit to submit it.

72
00:04:14,750 --> 00:04:17,540
I'm also going to click enable to enable this user.

73
00:04:17,540 --> 00:04:17,990
Now.

74
00:04:17,990 --> 00:04:20,120
And we're going to submit to save this option.

75
00:04:20,120 --> 00:04:24,980
So now if we go to the users you'll see that we have two users.

76
00:04:24,980 --> 00:04:29,450
We have my own user and we have the default user and we're both admins.

77
00:04:29,450 --> 00:04:35,420
So I'm actually going to disable this user which is the Empire admin, so that no one can log in as

78
00:04:35,420 --> 00:04:36,170
this user.

79
00:04:36,170 --> 00:04:37,910
And that's pretty much it.

80
00:04:37,910 --> 00:04:41,150
So now nobody can log in using the default username and password.

81
00:04:41,150 --> 00:04:43,130
And we have our own user.

82
00:04:43,550 --> 00:04:46,220
So this is one of the features of this tool.

83
00:04:46,220 --> 00:04:51,740
Like I said it's got collaboration or it's got multiplayer which basically means that you can create

84
00:04:51,740 --> 00:04:54,320
many users in here using the create button.

85
00:04:54,320 --> 00:05:00,170
And then you can actually have a team that can come in and manage all the computers that you hack.

86
00:05:00,170 --> 00:05:06,410
So you'll be able to create different kinds of listeners, hack different kinds of computers, interact

87
00:05:06,410 --> 00:05:09,350
with them, and collaborate with other team members.

88
00:05:09,350 --> 00:05:14,510
You even have a chat feature here in the bottom right, where you can actually message each other and

89
00:05:14,510 --> 00:05:21,590
share information, or share strategies on how you want to attack a specific system or a specific network.

90
00:05:22,070 --> 00:05:26,420
Now, this is not loading for me because I actually disabled the user that I logged in with.

91
00:05:26,420 --> 00:05:29,780
So let's go ahead and log in with the new user that we created.

92
00:05:29,780 --> 00:05:32,210
So let's go to the settings.

93
00:05:32,210 --> 00:05:33,920
We're going to log out.

94
00:05:33,920 --> 00:05:35,180
Yes please.

95
00:05:35,180 --> 00:05:38,930
And again we're going to put the new IP in here.

96
00:05:38,930 --> 00:05:43,850
Put my username and put the new password submit.

97
00:05:44,430 --> 00:05:47,460
And we're now logged in as our own user.

98
00:05:47,460 --> 00:05:54,780
The default user is disabled, and now we are able to go ahead and use this program to hack into other

99
00:05:54,780 --> 00:05:55,530
computers.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,170 --> 00:00:06,290
So now that we have Empire installed on the cloud and we set up our username and password and everything

2
00:00:06,290 --> 00:00:10,190
is ready, let's go ahead and use it to hack some computers.

3
00:00:10,610 --> 00:00:14,540
So as mentioned earlier, every C2 is made out of two parts.

4
00:00:14,540 --> 00:00:20,030
One part runs on the target system, which is a backdoor basically, but everybody calls it something

5
00:00:20,030 --> 00:00:20,450
else.

6
00:00:20,450 --> 00:00:22,340
In Empire it's called the Stager.

7
00:00:22,340 --> 00:00:28,520
And the other part runs on the cloud, and that is the part that listens for incoming connections.

8
00:00:28,520 --> 00:00:32,810
Some frameworks call it a server, and Empire calls it a listener.

9
00:00:32,810 --> 00:00:38,690
So what we want to do right now is create a listener so that we can receive connections from the computers

10
00:00:38,690 --> 00:00:39,770
that we're going to hack.

11
00:00:39,770 --> 00:00:41,960
So basically we're at the stage.

12
00:00:41,960 --> 00:00:44,420
We just have empire installed on the cloud.

13
00:00:44,420 --> 00:00:50,630
And what we want to do, we want to run a listener so that computers, once we hack them, once we execute

14
00:00:50,630 --> 00:00:57,140
backdoors on their computers, they'll be able to go ahead and connect to us and then we'll be able

15
00:00:57,140 --> 00:00:58,220
to control them.

16
00:00:58,310 --> 00:01:01,340
So back to Empire in here.

17
00:01:01,340 --> 00:01:02,840
I'm already logged in.

18
00:01:02,840 --> 00:01:07,880
And the first thing actually, by default you'll be dropped into the listeners view.

19
00:01:07,880 --> 00:01:09,950
So this is where you can create new listeners.

20
00:01:09,950 --> 00:01:14,420
And you're going to see how easy this is because I actually cover Empire in my other courses.

21
00:01:14,420 --> 00:01:16,130
But we do it from the command line.

22
00:01:16,130 --> 00:01:21,200
But now the graphical user interface is actually really good and it's really easy to use.

23
00:01:21,200 --> 00:01:26,420
So to create a new listener, all you have to do is click on the create in here.

24
00:01:26,810 --> 00:01:31,040
Once you're here, it's going to ask you for the type of listener that you want to create.

25
00:01:31,040 --> 00:01:32,360
Drop down menu.

26
00:01:32,390 --> 00:01:34,370
Very nice, very easy to use.

27
00:01:34,370 --> 00:01:37,790
It lists the different types of listeners that you can use.

28
00:01:37,790 --> 00:01:42,770
A really cool one in here is the OneDrive, which basically uses OneDrive as the server.

29
00:01:42,770 --> 00:01:45,770
It's a little bit advanced, so we're going to leave that for later.

30
00:01:46,460 --> 00:01:51,650
You've got listeners that you can use to basically pivot so that they can be used as a proxy or just

31
00:01:51,650 --> 00:01:53,660
to forward data to another point.

32
00:01:53,660 --> 00:02:01,010
So an example would be this one right here, the port forward, the SMB, the http hop, and the Http

33
00:02:01,010 --> 00:02:01,400
foreign.

34
00:02:01,400 --> 00:02:06,380
All of these are used to actually redirect the data or the connection to another computer.

35
00:02:06,380 --> 00:02:08,240
So we're not interested in that.

36
00:02:08,240 --> 00:02:10,970
The Http malleable is very cool.

37
00:02:10,970 --> 00:02:16,820
This is one of the listeners where you can actually program it to interpret messages differently.

38
00:02:16,820 --> 00:02:20,120
So you can actually program how the listener communicate with the back door.

39
00:02:20,120 --> 00:02:21,830
So we're going to leave that for now.

40
00:02:21,830 --> 00:02:23,270
We're trying to keep it simple.

41
00:02:23,270 --> 00:02:28,220
So the two options that we have left are the Http and the Http comm.

42
00:02:28,220 --> 00:02:29,570
Both of them are great.

43
00:02:29,570 --> 00:02:31,460
Both of them work very reliably.

44
00:02:31,460 --> 00:02:37,670
The Http comm only works on windows because it uses a windows Com object.

45
00:02:37,670 --> 00:02:44,600
So actually if I click it here, you will see that it's showing you a description on how this listener

46
00:02:44,600 --> 00:02:45,590
is going to work.

47
00:02:45,590 --> 00:02:48,920
And if you click the drop down it even gives you more information.

48
00:02:48,920 --> 00:02:53,720
Sometimes it even gives you resources where you can go and learn more about this specific module.

49
00:02:53,720 --> 00:02:56,450
But right now, like I said, this will only work against windows.

50
00:02:56,450 --> 00:03:01,760
So we're going to leave it and we're actually going to go ahead with the Http because this is a basic

51
00:03:01,760 --> 00:03:05,390
Http listener that will work against all operating systems.

52
00:03:05,390 --> 00:03:08,300
And you can even configure it to use Https.

53
00:03:08,300 --> 00:03:15,290
But even the basic Http listener, like I said in the previous lecture, it still uses AES encryption,

54
00:03:15,290 --> 00:03:18,170
and that's why it is still pretty secure.

55
00:03:18,170 --> 00:03:24,290
But you can enable Https and add another layer of encryption to make it even harder to detect.

56
00:03:24,650 --> 00:03:29,210
So once you have the listener selected, as you can see, you get a number of fields that you'll have

57
00:03:29,210 --> 00:03:29,690
to fill.

58
00:03:29,690 --> 00:03:31,580
All very easy to fill.

59
00:03:31,580 --> 00:03:34,610
So first of all, it's asking you the name of the listener.

60
00:03:34,610 --> 00:03:35,990
It's set to Http.

61
00:03:36,020 --> 00:03:37,550
That's very informative.

62
00:03:37,550 --> 00:03:39,320
So I'm going to keep it the way it is.

63
00:03:39,320 --> 00:03:41,450
Next is asking you for the host.

64
00:03:41,450 --> 00:03:45,650
So this is the IP of the cloud server that's going to receive the connections.

65
00:03:45,650 --> 00:03:48,470
So this is wrong actually this is our IP.

66
00:03:48,470 --> 00:03:52,160
So I'm going to copy it from here and simply paste it here.

67
00:03:52,850 --> 00:03:57,200
Next it's going to ask you for the port that you you want to receive connections on.

68
00:03:57,200 --> 00:04:02,870
I'm actually going to set it to port 80, because 80 is the default port that is used with Http.

69
00:04:02,870 --> 00:04:05,780
So this is really good to avoid detection.

70
00:04:05,780 --> 00:04:10,940
But if you have a web server running then this will clash with the web server because web servers by

71
00:04:10,940 --> 00:04:12,320
default run on port 80.

72
00:04:12,320 --> 00:04:16,940
So just make sure you don't select a port that is already being used by another service.

73
00:04:17,770 --> 00:04:20,470
We're going to leave the bind IP to 0000.

74
00:04:20,500 --> 00:04:21,250
That is correct.

75
00:04:21,250 --> 00:04:25,240
That's the IP that the control server is going to bound to bind to.

76
00:04:25,270 --> 00:04:27,370
You can customize the launcher.

77
00:04:27,370 --> 00:04:31,600
So this is the command that will launch the stager or the backdoor.

78
00:04:31,630 --> 00:04:33,430
We're going to leave it the way it is.

79
00:04:33,430 --> 00:04:37,900
The staging key is the key that's going to be used to initialize the connection.

80
00:04:37,900 --> 00:04:40,120
Like I said earlier, encryption is used.

81
00:04:40,120 --> 00:04:46,720
Even if you use Http, you can set a delay for the communication between the listener and the backdoor.

82
00:04:46,720 --> 00:04:49,630
It's set to five by default, so I'm going to leave it at that.

83
00:04:49,630 --> 00:04:55,120
You can modify it again to just make it more different than other backdoors that have been analyzed.

84
00:04:55,150 --> 00:05:01,090
You can add the jitter, which is basically a value that will be added to the delay again, to just

85
00:05:01,090 --> 00:05:07,120
make it less predictable and potentially bypass more intrusion or detection systems.

86
00:05:07,480 --> 00:05:10,990
You can set the number of missed checkins before exiting.

87
00:05:10,990 --> 00:05:14,320
Basically the number of missed connections before quitting.

88
00:05:14,320 --> 00:05:19,870
You can set the default profile as you can see, it's set to Mozilla five by default.

89
00:05:19,870 --> 00:05:21,490
You can do whatever you want.

90
00:05:21,490 --> 00:05:27,310
The headers it's set to Microsoft IIs, which is a Microsoft server, can do whatever you want with

91
00:05:27,310 --> 00:05:27,880
it.

92
00:05:27,880 --> 00:05:35,050
The J3 evasion option only makes sense if you were using the listener in Https, not in Http, because

93
00:05:35,050 --> 00:05:42,760
it allows you to bypass J3, which is a method of profiling and potentially detecting malicious Https

94
00:05:42,760 --> 00:05:43,420
traffic.

95
00:05:44,080 --> 00:05:48,670
So we're going to keep that to false, because we're actually just going to use the listener as plain

96
00:05:48,670 --> 00:05:49,480
Http.

97
00:05:49,480 --> 00:05:51,880
We will cover the Https later.

98
00:05:51,880 --> 00:05:58,300
But as usual, as you know, I like to keep things as simple as possible and then build up on our attack.

99
00:05:58,300 --> 00:06:01,060
So right now we just want to make sure that this tool actually works.

100
00:06:01,060 --> 00:06:01,870
We don't even know.

101
00:06:01,870 --> 00:06:04,570
So we're keeping everything as simple as possible.

102
00:06:05,170 --> 00:06:08,560
Next we have some optional fields or optional options.

103
00:06:08,560 --> 00:06:09,880
This is the cert path.

104
00:06:09,880 --> 00:06:13,150
Again if you're using Https we're leaving that for later.

105
00:06:13,150 --> 00:06:18,460
You can set up a kill date so that the listener just gets killed after a certain date.

106
00:06:18,460 --> 00:06:24,130
You can set working hours so that it only works after working hours, for example, or during working

107
00:06:24,130 --> 00:06:24,460
hours.

108
00:06:24,460 --> 00:06:28,030
So again, it raises less detection and less intrusion systems.

109
00:06:28,030 --> 00:06:29,740
You can set the cookie.

110
00:06:29,770 --> 00:06:33,670
You can set a Uri for the stager for the backdoor.

111
00:06:33,670 --> 00:06:35,350
We're going to keep it the way it is.

112
00:06:35,470 --> 00:06:38,650
You can set the user agent keeping it at the default.

113
00:06:38,650 --> 00:06:41,770
You can use a proxy again keeping it at the default.

114
00:06:41,770 --> 00:06:47,050
If your proxy uses authentication, you'll have to put it here again keeping it at the default.

115
00:06:47,050 --> 00:06:51,250
And you can use a slack URL so that you get a notification on slack.

116
00:06:51,250 --> 00:06:54,760
Once you get a new backdoor connecting to this listener.

117
00:06:54,760 --> 00:06:56,110
Again, we're not using that.

118
00:06:56,110 --> 00:06:57,340
Keeping it at default.

119
00:06:57,370 --> 00:07:01,390
Didn't want to make this too long for you guys, but I just want to cover all the nice options that

120
00:07:01,390 --> 00:07:04,300
you have in here, and I don't want you to feel like I'm missing anything.

121
00:07:04,720 --> 00:07:11,110
But as you can see, the main things that we had to set is simply the IP, the port, and that's it.

122
00:07:11,110 --> 00:07:12,640
I'm going to click submit.

123
00:07:14,450 --> 00:07:15,320
And perfect.

124
00:07:15,320 --> 00:07:17,810
As you can see, it turned it on by default.

125
00:07:17,810 --> 00:07:21,530
So you have a nice toggle here to turn this listener on and off.

126
00:07:21,530 --> 00:07:27,110
You can also even use this dropdown menu to generate a backdoor for this listener, but we will talk

127
00:07:27,110 --> 00:07:28,970
about that in the next lecture.

128
00:07:29,360 --> 00:07:32,180
You can click on the trash can in here to delete it.

129
00:07:32,180 --> 00:07:36,860
And you can click the copy to create a new listener with the same options as these.

130
00:07:36,860 --> 00:07:39,200
So maybe you configured a lot of options in here.

131
00:07:39,200 --> 00:07:40,640
You can click on the copy.

132
00:07:40,640 --> 00:07:41,870
It'll create another one.

133
00:07:41,870 --> 00:07:46,520
And then you can modify 1 or 2 things, maybe change the port or change whatever you want to change.

134
00:07:46,520 --> 00:07:49,460
And then you can use that to easily create another listener.

135
00:07:49,460 --> 00:07:52,850
But for now, we're happy we created our listener already.

136
00:07:52,850 --> 00:07:58,700
And if we go back to the listener menu in here, you'll see it right here running.

137
00:07:58,700 --> 00:07:59,870
It's called Http.

138
00:07:59,870 --> 00:08:00,800
That's what we called it.

139
00:08:00,800 --> 00:08:06,230
It shows you the host it's running on, which is our host showing us the port, the time when it was

140
00:08:06,230 --> 00:08:07,040
created.

141
00:08:07,040 --> 00:08:12,410
You can actually use tags so that you can have different colors for different backdoors and different

142
00:08:12,410 --> 00:08:13,130
listeners.

143
00:08:13,130 --> 00:08:15,560
Again this is kind of a collaboration feature.

144
00:08:15,560 --> 00:08:21,170
So you can guys tag things a certain color, and only certain people are allowed to deal with certain

145
00:08:21,170 --> 00:08:21,890
tags.

146
00:08:22,250 --> 00:08:26,270
That's just an example of using it where you can use it to organize your workflow, really.

147
00:08:26,270 --> 00:08:32,150
And finally, here at the action, you can either view it, copy it, like I said, in order to create

148
00:08:32,150 --> 00:08:38,120
another listener with the same values or the same options, and then you just modify 1 or 2 to save

149
00:08:38,120 --> 00:08:40,610
you time from having to input everything else again.

150
00:08:40,610 --> 00:08:42,500
And you can click on delete to delete it.

151
00:08:42,500 --> 00:08:44,090
Very self-explanatory.

152
00:08:44,090 --> 00:08:48,170
Again, the green in here meaning that the listener is running right now.

153
00:08:48,170 --> 00:08:54,260
So basically you can visualize it that right now it is basically like this waiting for incoming connections

154
00:08:54,260 --> 00:08:55,280
on port 80.

155
00:08:55,280 --> 00:08:59,840
But for whatever reason, if you wanted to run a web server or if you wanted to run another service

156
00:08:59,840 --> 00:09:04,190
on port 80 temporarily, you can come in here, click this button in here.

157
00:09:04,190 --> 00:09:05,180
And now it's disabled.

158
00:09:05,180 --> 00:09:06,140
Right now it's not running.

159
00:09:06,140 --> 00:09:08,570
And then you can go ahead and run something on port 80.

160
00:09:08,570 --> 00:09:14,150
So you can see how easy it is to control everything through this very nice web interface.

161
00:09:14,150 --> 00:09:18,950
And also while it's off, you can actually go ahead and modify any options in here.

162
00:09:18,950 --> 00:09:22,940
So if you wanted to change the port or you wanted to change the host, you can just come in and change

163
00:09:22,940 --> 00:09:23,480
this.

164
00:09:23,480 --> 00:09:25,910
Once you're happy, click on enable.

165
00:09:25,910 --> 00:09:26,660
Yes.

166
00:09:26,660 --> 00:09:28,250
And that's it again saved.

167
00:09:28,250 --> 00:09:33,410
And going back to the listeners, you can see that it is running and waiting for incoming connections

168
00:09:33,410 --> 00:09:35,960
based on the settings that you set in here.

169
00:09:36,950 --> 00:09:42,500
So next I'm going to show you how we're going to create a backdoor that will connect back to this listener

170
00:09:42,500 --> 00:09:45,860
and remotely control a windows computer or hack it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:05,780
So now that we have Empire installed on the cloud and we started a listener, so we're waiting for computers

2
00:00:05,780 --> 00:00:07,130
to connect back to us.

3
00:00:07,160 --> 00:00:14,180
The next stage is to actually create a back door, or what Empire calls them a stager, so that when

4
00:00:14,180 --> 00:00:20,510
this back door is executed on a computer, it will send a reverse connection back to Empire.

5
00:00:20,510 --> 00:00:23,930
And at that stage, Empire can fully control this computer.

6
00:00:23,930 --> 00:00:26,960
Basically, this computer is hacked at this stage.

7
00:00:26,960 --> 00:00:33,230
And then whenever we want, we can connect to Empire and control this computer from any device.

8
00:00:33,230 --> 00:00:36,560
Like I said, you can use a phone, you can use a laptop, you can use a computer.

9
00:00:36,560 --> 00:00:41,390
It doesn't really matter because all of the heavy lifting is being done on the cloud server.

10
00:00:41,390 --> 00:00:44,690
Basically, you're just rendering the web interface on your computer.

11
00:00:44,690 --> 00:00:52,070
So basically we're going to be creating the second part of every C2, which is a back door, a client

12
00:00:52,070 --> 00:00:55,760
or an agent or a stager, which is what Empire calls them.

13
00:00:56,350 --> 00:01:00,970
So to do this, going back to the web interface again, it's going to be very, very easy.

14
00:01:01,000 --> 00:01:02,560
You can guess where we're going to go.

15
00:01:02,590 --> 00:01:04,510
We're going to go to the stages menu in here.

16
00:01:04,510 --> 00:01:06,670
Literally the second menu is telling you the order.

17
00:01:06,670 --> 00:01:08,080
First you have to create a listener.

18
00:01:08,080 --> 00:01:09,730
And next you have to create a stager.

19
00:01:10,030 --> 00:01:13,240
Again to create it you're going to click on the create here on the top right.

20
00:01:13,240 --> 00:01:15,880
Very very simple and similar to the listeners.

21
00:01:15,880 --> 00:01:20,560
We have a drop down menu where we can select the stager that we want to create.

22
00:01:20,590 --> 00:01:23,470
Now I mentioned earlier that a stager is a backdoor.

23
00:01:23,470 --> 00:01:26,050
And that's actually what we're going to create right now.

24
00:01:26,050 --> 00:01:28,300
But it does not have to be a backdoor.

25
00:01:28,330 --> 00:01:30,430
A stager is basically a piece of code.

26
00:01:30,430 --> 00:01:36,760
So it could be simply a command that you can execute on PowerShell or on Linux or on OS X, and it will

27
00:01:36,760 --> 00:01:38,920
send a reverse connection back to your computer.

28
00:01:39,460 --> 00:01:41,170
And that's exactly what we have in here.

29
00:01:41,170 --> 00:01:47,260
So by clicking on the multi bash in here it's basically going to give you a bash script or a command

30
00:01:47,260 --> 00:01:49,780
that you can execute on a Linux computer.

31
00:01:49,780 --> 00:01:52,480
And it will send a connection back to your server.

32
00:01:52,480 --> 00:01:57,310
And the nice thing about this, similar to what we had in the listener, you have a nice description

33
00:01:57,310 --> 00:02:00,040
about the stager that you selected.

34
00:02:00,040 --> 00:02:03,430
And if you click on the drop down it'll give you more information.

35
00:02:03,430 --> 00:02:05,740
Now this is a very simple stager.

36
00:02:05,740 --> 00:02:08,140
That's why you don't have more information in here.

37
00:02:08,650 --> 00:02:10,120
Now this is not what we want to do.

38
00:02:10,120 --> 00:02:11,710
We don't want to create a Linux backdoor.

39
00:02:11,710 --> 00:02:13,180
Not yet at least.

40
00:02:13,180 --> 00:02:15,370
We want to actually create a windows one.

41
00:02:15,370 --> 00:02:20,140
But before we do that, I want to just show you the different examples of stages we have.

42
00:02:20,140 --> 00:02:26,260
So you can see that the first few ones here start with multi, which basically means that they are generic

43
00:02:26,260 --> 00:02:30,760
and that they can be used in different scenarios and against different computers.

44
00:02:30,760 --> 00:02:37,960
So you have a multi bash multi generate agent which is basically just an agent, a launcher, a file,

45
00:02:37,960 --> 00:02:43,270
a macro which can be embedded in Microsoft Office documents.

46
00:02:43,270 --> 00:02:48,190
If we scroll down we have OSX specific stages for Apple computers.

47
00:02:48,190 --> 00:02:55,030
So you have an Apple script, an application, a Docky script, a jar which is basically a Java file,

48
00:02:55,030 --> 00:03:01,900
a macro or macro, which is a binary, a macro to be embedded in Microsoft Office documents, a package,

49
00:03:01,900 --> 00:03:03,070
a Safari launcher.

50
00:03:03,070 --> 00:03:08,260
Some of these require a specific exploit so they won't work against fully patched systems.

51
00:03:08,260 --> 00:03:12,790
But executables will always work because they don't require an exploit.

52
00:03:12,790 --> 00:03:17,140
And finally, if we scroll down, we have the windows stages in here again.

53
00:03:17,140 --> 00:03:22,900
So some of them will give you DLLs to be injected and some of them will give you an exe.

54
00:03:22,930 --> 00:03:24,490
As you can see in here.

55
00:03:24,490 --> 00:03:29,320
And the one that we actually want to run right now is the launcher, which will basically give us a

56
00:03:29,320 --> 00:03:35,260
batch file or a batch script that once executed on the target system, it will give us full control

57
00:03:35,260 --> 00:03:36,070
over it.

58
00:03:36,070 --> 00:03:39,460
And don't worry about all of the different types of stages.

59
00:03:39,460 --> 00:03:44,080
Like I said, if you click it, it will explain to you what it's going to do in here.

60
00:03:44,080 --> 00:03:47,440
And we're actually going to be covering more than this simple one.

61
00:03:47,440 --> 00:03:50,620
I'm just going to start with the simple one to warm you up.

62
00:03:50,890 --> 00:03:54,940
So again, similar to the listener, we have a few options to set the name.

63
00:03:54,940 --> 00:03:55,720
Very simple.

64
00:03:55,720 --> 00:03:57,310
You can choose whatever name you want.

65
00:03:57,310 --> 00:03:59,320
I like to use meaningful names.

66
00:03:59,320 --> 00:04:06,190
So I'm going to say windows, but kind of similar to the original name in here.

67
00:04:06,220 --> 00:04:11,200
It's going to ask you which listener do you want this backdoor to connect to because you can have multiple

68
00:04:11,200 --> 00:04:13,000
listeners, as we said previously.

69
00:04:13,000 --> 00:04:16,360
So right now we only have one listener, the Http listener.

70
00:04:16,360 --> 00:04:19,150
So we're going to just go with the Http listener.

71
00:04:19,150 --> 00:04:23,230
It's going to ask you the programming language that should be used in this stager.

72
00:04:23,230 --> 00:04:28,810
So if we click on the drop down you can see we can choose C sharp or Ironpython we're going to keep

73
00:04:28,810 --> 00:04:29,950
it at PowerShell.

74
00:04:30,310 --> 00:04:32,140
And now we have the optional fields.

75
00:04:32,140 --> 00:04:33,910
So you can basically just click submit.

76
00:04:33,910 --> 00:04:37,900
Now you don't really need to do anything, but I'm just going to quickly walk you through the optional

77
00:04:37,900 --> 00:04:40,420
fields where you can set the output file name.

78
00:04:40,420 --> 00:04:41,650
So it's set to launcher.

79
00:04:41,830 --> 00:04:44,050
But I'm just going to keep that the way it is.

80
00:04:44,050 --> 00:04:49,930
You can choose this option so that the file self-destruct or deletes itself once executed.

81
00:04:49,930 --> 00:04:52,990
I'm going to turn this off because I don't want that to happen.

82
00:04:53,170 --> 00:05:00,910
You can toggle this on so that the script gets obfuscated, which actually helps with bypassing detection.

83
00:05:01,420 --> 00:05:03,280
You can choose the obfuscation command.

84
00:05:03,280 --> 00:05:06,970
We're going to keep it the way it is and you can actually choose the bypasses.

85
00:05:06,970 --> 00:05:13,360
So these are scripts that will be appended to your backdoor or to your stager, which will help you

86
00:05:13,360 --> 00:05:15,340
bypass specific features.

87
00:05:15,340 --> 00:05:19,480
Now you can modify these bypasses in here from this menu.

88
00:05:19,480 --> 00:05:21,280
You can even add your own.

89
00:05:21,280 --> 00:05:26,200
And to use them you can simply tick whichever bypass you want to tick.

90
00:05:26,230 --> 00:05:31,480
You can also simply google any of these bypasses to learn exactly what they do, but we're actually

91
00:05:31,480 --> 00:05:32,770
going to leave that for later.

92
00:05:32,770 --> 00:05:37,150
Again, we're keeping everything as simple as possible, because we want to test the tool and make sure

93
00:05:37,150 --> 00:05:37,930
it works.

94
00:05:37,930 --> 00:05:42,400
So now that we're happy with all of the options, all you have to do is simply click submit.

95
00:05:43,060 --> 00:05:47,440
And as you can see, we get a message telling us that the stager is created, basically meaning that

96
00:05:47,440 --> 00:05:49,030
our backdoor got created.

97
00:05:49,510 --> 00:05:55,030
So now again, here on the top right, similar to what we saw with the listener, I can click the copy

98
00:05:55,030 --> 00:06:00,850
to create another stager with the same options that I selected here, so that I can easily maybe change

99
00:06:00,850 --> 00:06:01,390
one option.

100
00:06:01,390 --> 00:06:05,590
Just set it to use a different listener, or set it to use a different programming language, and then

101
00:06:05,590 --> 00:06:07,270
easily create another stager.

102
00:06:07,660 --> 00:06:13,570
We can click the trash can here to delete it, or click the download button to download the stager that

103
00:06:13,570 --> 00:06:14,620
we just created.

104
00:06:14,830 --> 00:06:21,370
Just going to call it Http 80, because it's going to send the connection on port 80 to the Http listener,

105
00:06:21,370 --> 00:06:23,200
just using a meaningful name.

106
00:06:23,200 --> 00:06:25,450
And that is downloaded here for me.

107
00:06:25,450 --> 00:06:31,900
So before I go ahead and send it to the target computer, I want to show you the stagers menu in here.

108
00:06:31,900 --> 00:06:36,520
So if we go back now to the stagers menu, you can see we have our stager.

109
00:06:36,520 --> 00:06:40,330
It's called windows but it uses the Http listener.

110
00:06:40,360 --> 00:06:42,310
This is the type of stager it is.

111
00:06:42,310 --> 00:06:46,150
We selected the windows launcher but it uses PowerShell.

112
00:06:46,150 --> 00:06:51,730
And if we click on the actions you can again download it from here or copy it or delete it similar to

113
00:06:51,730 --> 00:06:52,810
the options that we see.

114
00:06:52,810 --> 00:06:55,300
If we click into it that we see them in here.

115
00:06:55,300 --> 00:06:56,920
And we already talked about that.

116
00:06:57,700 --> 00:07:04,240
So next we will go ahead and execute this stager on a windows computer and see what we can do with it

117
00:07:04,240 --> 00:07:08,680
and how we can control this windows computer from this nice web interface.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:06,170
Okay, so now that we have our backdoor downloaded and we're ready to go ahead and hack a windows computer,

2
00:00:06,170 --> 00:00:08,480
let's say first of all upload it.

3
00:00:08,480 --> 00:00:13,070
So I'm gonna upload it using this file sharing service.

4
00:00:13,070 --> 00:00:17,540
So it was called http etcbut.

5
00:00:18,460 --> 00:00:20,410
And I'm going to copy the URL.

6
00:00:20,410 --> 00:00:24,100
And then we're going to go to the target windows computer right here.

7
00:00:24,100 --> 00:00:25,900
And we're going to download it.

8
00:00:28,470 --> 00:00:30,630
So we have the file downloaded in here.

9
00:00:30,630 --> 00:00:34,830
So all we have to do now is double click it just to see if it's going to work.

10
00:00:34,830 --> 00:00:39,600
Now you're going to get this message which you will get if you're on any unsigned program.

11
00:00:39,600 --> 00:00:44,130
So any program by unrecognized developer is going to show you this message.

12
00:00:44,130 --> 00:00:50,220
It's not because this is being detected by antivirus programs, although before I run it, actually

13
00:00:50,220 --> 00:00:54,750
if we go to the security settings on my windows computer.

14
00:00:55,560 --> 00:01:01,020
And if we go to Manage Settings, I'm actually going to turn off real time protection.

15
00:01:01,020 --> 00:01:04,170
And I have all of the other security settings off.

16
00:01:04,170 --> 00:01:11,040
And the reason for this is because bypass and antivirus programs is a completely different challenge

17
00:01:11,040 --> 00:01:16,080
than simply creating a backdoor or using a C2 framework.

18
00:01:16,080 --> 00:01:22,320
These C2 frameworks do try to bypass intrusion detection systems, and they encrypt their traffic so

19
00:01:22,320 --> 00:01:28,200
that they are less detected in the way that they communicate, and they even try to make an executable

20
00:01:28,200 --> 00:01:31,860
that is detected by as little antivirus programs as possible.

21
00:01:31,860 --> 00:01:37,830
The job of bypassing antivirus programs is not one of the goals for such programs.

22
00:01:37,830 --> 00:01:42,840
Bypass and antivirus programs is a completely different task that you as a hacker, should do.

23
00:01:42,870 --> 00:01:47,790
Once you pick a C2 framework that you want to use, we can cover that later on.

24
00:01:47,790 --> 00:01:48,030
Guys.

25
00:01:48,030 --> 00:01:52,710
If you want, we can even make a full series about it because it's such a big topic.

26
00:01:52,710 --> 00:01:57,990
I cover a lot of techniques in my social engineering course, so if you're interested in this, go check

27
00:01:57,990 --> 00:01:58,710
that out.

28
00:01:58,710 --> 00:02:01,020
And also before I run it.

29
00:02:01,200 --> 00:02:04,530
And as you can see in here, the backdoor looks a little bit suspicious.

30
00:02:04,530 --> 00:02:06,690
You can see that it is an executable.

31
00:02:06,750 --> 00:02:15,180
Again, making this stager look less suspicious is not one of the goals of the developers of C2 frameworks.

32
00:02:15,180 --> 00:02:21,990
This is your job as a hacker to disguise this stager and make it as believable as possible, or as attractive

33
00:02:21,990 --> 00:02:23,880
as possible to your target.

34
00:02:24,090 --> 00:02:29,250
So you can embed this into another file, such as another image or video.

35
00:02:29,250 --> 00:02:32,220
You can even embed it in Microsoft Office documents.

36
00:02:32,220 --> 00:02:34,860
And I do cover all of that in my social engineering course.

37
00:02:34,860 --> 00:02:37,560
Again, this all falls under social engineering.

38
00:02:37,560 --> 00:02:39,240
So it's not really part of this.

39
00:02:39,240 --> 00:02:42,030
And you shouldn't really try to do everything in one go.

40
00:02:42,120 --> 00:02:47,700
It's always best to divide a big problem into a number of small problems, solve them individually and

41
00:02:47,700 --> 00:02:50,460
then your big problem will be solved automatically.

42
00:02:50,550 --> 00:02:53,580
So right now we're trying to find a really good C2 framework.

43
00:02:53,580 --> 00:02:58,440
Once you find one that you like, you can go ahead and learn how to make the stager bypass antivirus

44
00:02:58,440 --> 00:03:02,520
programs, and then learn how to embed it into other types of files.

45
00:03:02,880 --> 00:03:05,580
So with that being said, let's go ahead and run the file.

46
00:03:06,790 --> 00:03:08,380
We're going to click on run anyway.

47
00:03:09,050 --> 00:03:11,660
And now the file should have been executed.

48
00:03:11,660 --> 00:03:18,800
So if we go back to Starkiller, to our web interface, and if we go to the agents, perfect.

49
00:03:18,800 --> 00:03:21,170
As you can see, we got a connection.

50
00:03:21,170 --> 00:03:25,760
So basically an agent is a connection from another computer.

51
00:03:25,760 --> 00:03:27,200
So right now this is an agent.

52
00:03:27,200 --> 00:03:30,500
Basically it's a backdoor that is running on a target computer.

53
00:03:30,500 --> 00:03:36,650
You can see when we last saw it or when it last communicated with us, when it first communicated with

54
00:03:36,650 --> 00:03:38,690
us, the computer that we hacked.

55
00:03:38,690 --> 00:03:41,660
So this is the name of the computer desktop, whatever.

56
00:03:41,690 --> 00:03:42,890
You can see the process.

57
00:03:42,890 --> 00:03:45,620
It's PowerShell because the language was PowerShell.

58
00:03:45,620 --> 00:03:50,660
We can see the username which is John on this computer desktop whatever.

59
00:03:51,290 --> 00:03:54,830
Now to communicate with this again, you don't have to run any commands.

60
00:03:54,830 --> 00:03:55,910
It's very, very easy.

61
00:03:55,940 --> 00:03:58,700
All we have to do is click it.

62
00:03:58,700 --> 00:04:03,560
And right now we are inside it and we are ready to execute quick actions.

63
00:04:03,560 --> 00:04:08,840
In here, for example, you can upload files or download files or import scripts, or you can pop this

64
00:04:08,840 --> 00:04:09,290
window.

65
00:04:09,290 --> 00:04:13,250
So you can just have a window to communicate with this specific computer.

66
00:04:13,250 --> 00:04:15,380
Or you can kill this agent from here.

67
00:04:16,140 --> 00:04:21,780
Now, it's very important to note that this is one of the cool things about Empire is that this is again

68
00:04:21,780 --> 00:04:22,770
running on the cloud.

69
00:04:22,770 --> 00:04:27,960
So when this connection happened, you could be away from your computer, your computer could be off,

70
00:04:27,960 --> 00:04:29,370
this window could be closed.

71
00:04:29,370 --> 00:04:33,840
It doesn't really matter because the connection is being sent to the server that is actually running

72
00:04:33,870 --> 00:04:34,710
to the cloud.

73
00:04:34,710 --> 00:04:39,150
Connection is actually being sent here, which is basically running on the cloud.

74
00:04:39,150 --> 00:04:45,540
And then we can come in whenever from any computer and control this windows computer that we just hacked.

75
00:04:45,540 --> 00:04:48,900
We're actually going to be having a lot of fun with this section next.

76
00:04:48,900 --> 00:04:55,380
And you're going to see how we can steal passwords, extract useful information, spy on the target

77
00:04:55,380 --> 00:05:00,300
access system resources, and even run ransomware on the target computer.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: Post Exploitation With StarKiller

1
00:00:00,050 --> 00:00:05,960
So now that you know how to gain access to windows computers or hack them in this class, we're going

2
00:00:05,960 --> 00:00:08,210
to focus on post exploitation.

3
00:00:08,210 --> 00:00:14,630
So we're going to focus on what can we do once we get access or hack these windows computers.

4
00:00:14,630 --> 00:00:20,750
So in many cases, gaining access to the target system is only the start of achieving your goal.

5
00:00:20,750 --> 00:00:25,940
Once you gain initial access, a lot of the time you need to pivot into different computers or you need

6
00:00:25,940 --> 00:00:30,500
to escalate your privileges, or you want to extract information from the target computer.

7
00:00:30,500 --> 00:00:37,280
And Empire agents have a huge library of modules that allow you to do so much, so you'll be able to

8
00:00:37,280 --> 00:00:39,710
execute any system commands that you want.

9
00:00:39,710 --> 00:00:46,310
You'll be able to access their file system, read, upload or download files, access system resources

10
00:00:46,310 --> 00:00:50,810
such as the camera and the keyboard, and even launch ransomware attacks.

11
00:00:51,080 --> 00:00:54,920
Now, I've already compromised a Windows 11 machine in here.

12
00:00:55,530 --> 00:00:59,550
So from here we can do more or get more information about the target.

13
00:00:59,550 --> 00:01:04,560
So if we click on the view here, just to keep it simple, you can see we have the agent name.

14
00:01:04,560 --> 00:01:07,500
We have the external and the internal IP.

15
00:01:07,650 --> 00:01:10,770
We have the host name which is the computer name.

16
00:01:10,770 --> 00:01:11,880
The user name.

17
00:01:11,880 --> 00:01:16,950
We saw all of that, the type of listener we got when we communicated with it.

18
00:01:16,950 --> 00:01:18,630
We can see the operating system.

19
00:01:18,630 --> 00:01:20,250
It's a Windows 11 Pro.

20
00:01:20,280 --> 00:01:25,980
You can see the architecture, the process ID we're running from, more information that we already

21
00:01:25,980 --> 00:01:26,670
know.

22
00:01:27,300 --> 00:01:29,730
You have a nice file browser in here.

23
00:01:29,730 --> 00:01:35,370
So again, you won't need to use the CD command to navigate between the directories and the files.

24
00:01:35,370 --> 00:01:38,310
We can simply interact with the file system in here.

25
00:01:38,310 --> 00:01:39,810
So we have the C directory.

26
00:01:39,810 --> 00:01:43,410
I can simply click it to load all the directories within C.

27
00:01:43,890 --> 00:01:45,840
And we have everything in here.

28
00:01:45,840 --> 00:01:51,300
For example again I have the users in here one click and it will load what's inside the users.

29
00:01:51,300 --> 00:01:53,130
We have all the users listed.

30
00:01:53,130 --> 00:01:55,680
Now I want to go to John click John.

31
00:01:55,680 --> 00:01:57,420
It'll load everything in here.

32
00:01:57,420 --> 00:02:00,990
If I want to go to the downloads one click it'll load it for me.

33
00:02:00,990 --> 00:02:04,770
And let's say that there is a file in here that I am interested in.

34
00:02:04,770 --> 00:02:07,200
For example, the passwords file in here.

35
00:02:07,200 --> 00:02:09,120
Again, don't need to run any commands.

36
00:02:09,120 --> 00:02:12,690
I can simply right click it and click Download to Empire.

37
00:02:13,550 --> 00:02:17,870
This is going to send it to the task list, which you can actually see in here.

38
00:02:17,870 --> 00:02:22,370
So if I click on the task list, you'll actually see every click I did.

39
00:02:22,370 --> 00:02:27,020
So when I listed the partitions, when I went to users, went to John, went to downloads.

40
00:02:27,020 --> 00:02:32,000
Everything can be seen in here and tracked to see if the command got executed properly.

41
00:02:32,420 --> 00:02:37,250
But the one that we're interested in is the last request or the last task that we asked for, which

42
00:02:37,250 --> 00:02:39,200
is to download the passwords file.

43
00:02:39,200 --> 00:02:42,800
If I click here, you'll see that the file got downloaded.

44
00:02:42,800 --> 00:02:44,600
So it got downloaded successfully.

45
00:02:44,600 --> 00:02:50,360
So if I just zoom out a little bit, I'll be able to click on the actions in here.

46
00:02:50,360 --> 00:02:54,980
And I can download passwords dot txt the file that I requested.

47
00:02:55,700 --> 00:03:02,150
And it's going to put it in my downloads, and I can simply open it and assume these are passwords of

48
00:03:02,150 --> 00:03:03,200
the target person.

49
00:03:03,200 --> 00:03:07,640
Then we manage to read them by simply just navigating and downloading them.

50
00:03:07,640 --> 00:03:10,010
We didn't have to execute a single command.

51
00:03:11,360 --> 00:03:14,630
It can also access your downloads here from the left menu.

52
00:03:14,630 --> 00:03:19,280
So if I click on downloads here, you will see the files that you might want to download.

53
00:03:19,280 --> 00:03:22,040
And you can see that I have the passwords file in here.

54
00:03:22,040 --> 00:03:25,790
So again I can simply click it and click download to download it.

55
00:03:26,990 --> 00:03:30,860
So going back to the interact tab in here.

56
00:03:30,860 --> 00:03:33,710
As you can see we have two subsections within it.

57
00:03:33,710 --> 00:03:34,940
I'm going to leave this one.

58
00:03:34,940 --> 00:03:36,530
We're going to come back to it in a bit.

59
00:03:36,530 --> 00:03:39,650
So I'm going to go to the terminal subsection in here.

60
00:03:39,650 --> 00:03:45,800
And basically this allows me to interact with the Empire agent using Empire commands.

61
00:03:46,040 --> 00:03:53,510
So it's identical to the access that I would get if I was using the terminal or the console interface

62
00:03:53,510 --> 00:03:54,410
of Empire.

63
00:03:54,410 --> 00:04:00,080
Right here we're using the GUI, but this gives me very similar access to the access that I get from

64
00:04:00,080 --> 00:04:00,800
the terminal.

65
00:04:00,800 --> 00:04:06,740
And basically it means that I can execute commands in here and see the result directly on the screen

66
00:04:06,740 --> 00:04:08,750
without having to go to the tasks.

67
00:04:08,750 --> 00:04:11,210
But the thing is, I can't just click on buttons.

68
00:04:11,210 --> 00:04:12,950
I'll have to execute commands.

69
00:04:12,950 --> 00:04:15,440
Now we don't know what commands we can execute.

70
00:04:15,440 --> 00:04:18,290
Therefore we can simply run help to see the commands.

71
00:04:18,290 --> 00:04:20,780
And as you can see, we get a nice help menu.

72
00:04:20,780 --> 00:04:25,880
And like I said, this is identical to the help menu that you would get if you're using the terminal

73
00:04:25,880 --> 00:04:27,140
version of Empire.

74
00:04:27,140 --> 00:04:32,870
So from here you can actually do everything that you can do from the graphical user interface, but

75
00:04:32,870 --> 00:04:36,020
using the command prompt or by executing the commands.

76
00:04:36,380 --> 00:04:40,340
And as you can see, we can simply run who am I to get the current user?

77
00:04:40,340 --> 00:04:43,400
We can run Sysinfo to get the system information.

78
00:04:43,400 --> 00:04:46,370
We can run PS to see the running processes.

79
00:04:46,370 --> 00:04:52,220
And obviously you can also run modules and everything that we are going to speak about in the next lectures

80
00:04:52,220 --> 00:04:52,790
as well.

81
00:04:52,880 --> 00:04:57,710
So let's just run some simple commands just to show you the difference or what you can do within this

82
00:04:57,710 --> 00:04:58,160
access.

83
00:04:58,160 --> 00:05:04,340
So we can just do PS as we saw earlier to get the running processes, give it a minute to execute the

84
00:05:04,340 --> 00:05:06,020
command and get you the result.

85
00:05:06,020 --> 00:05:12,050
And as you can see, we get a list of all of the running processes, their IDs, the description of

86
00:05:12,050 --> 00:05:12,980
the process.

87
00:05:12,980 --> 00:05:15,500
And we don't have to go to the tasks to see it.

88
00:05:15,500 --> 00:05:16,790
We can see the result within.

89
00:05:16,790 --> 00:05:21,680
Here again, we can simply do sysinfo to get the system information.

90
00:05:21,680 --> 00:05:24,380
And as you can see, we're getting the system information.

91
00:05:24,380 --> 00:05:25,370
It's a Windows 11.

92
00:05:25,370 --> 00:05:30,560
It's getting us the IP, the name of the computer, the username, the language, it's PowerShell and

93
00:05:30,560 --> 00:05:31,040
so on.

94
00:05:31,040 --> 00:05:34,640
We can also do who am I to get my current user.

95
00:05:34,790 --> 00:05:37,460
And as you can see, we're getting the right user.

96
00:05:37,460 --> 00:05:43,250
So the idea of this is that you can simply execute commands in here and see the results very quickly,

97
00:05:43,250 --> 00:05:48,950
instead of having to go ahead and execute, press buttons and then see the result in the tasks.

98
00:05:49,100 --> 00:05:54,200
If you wanted to execute system commands like there, you can't execute it directly like this.

99
00:05:54,200 --> 00:05:58,250
What we can do shell to be dropped into an operating system shell.

100
00:05:58,250 --> 00:06:04,250
So if I hit enter, you'll see I'll get a windows command prompt where I can directly execute windows

101
00:06:04,250 --> 00:06:04,880
commands.

102
00:06:04,880 --> 00:06:11,030
So in here I can simply do dare to list all of the directories and files within the current working

103
00:06:11,030 --> 00:06:14,000
directory, which is this one right here.

104
00:06:14,000 --> 00:06:18,500
And as you can see, we get a list of all the files and directories within the downloads.

105
00:06:18,500 --> 00:06:23,330
Assuming you want to read the file, I'm simply going to run a windows command to read the file so I

106
00:06:23,330 --> 00:06:26,090
can do more, followed by the file that I want to read.

107
00:06:26,090 --> 00:06:30,230
And just as an example, let's say we want to run or read the passwords file.

108
00:06:30,230 --> 00:06:34,430
In here we're simply going to type passwords dot txt.

109
00:06:35,900 --> 00:06:38,120
Give it a second and perfect.

110
00:06:38,120 --> 00:06:41,120
As you can see, we're able to read the file contents in here.

111
00:06:41,120 --> 00:06:47,630
So now that we have an operating system shell, we can execute any command that the operating system

112
00:06:47,630 --> 00:06:49,040
shell allows us to execute.

113
00:06:49,040 --> 00:06:51,020
So we have a windows command prompt in here.

114
00:06:51,020 --> 00:06:54,260
And we can execute any windows command that we want.

115
00:06:54,650 --> 00:06:56,960
Once we're done we can do control C.

116
00:06:56,960 --> 00:07:04,100
And that will get us out of this and bring us back to the Empire shell, where we can execute Empire

117
00:07:04,100 --> 00:07:05,180
commands again.

118
00:07:06,080 --> 00:07:11,990
Now also going back to the form in here, you can execute shell commands in here if you just want to

119
00:07:11,990 --> 00:07:17,060
execute one quick command and you don't really want to go in here and do shell and then execute the

120
00:07:17,060 --> 00:07:19,730
command, you can simply just in here, do it there.

121
00:07:19,730 --> 00:07:23,450
For example, to list the directories and files and the current working directory.

122
00:07:23,450 --> 00:07:29,480
You can tick this box if you want this command to be literal so that it executes the system command.

123
00:07:29,480 --> 00:07:34,010
So in case empire has another command that is called there, it's going to ignore that and execute your

124
00:07:34,010 --> 00:07:34,580
command.

125
00:07:35,090 --> 00:07:38,180
You can also tick this box if this command is within a script.

126
00:07:38,180 --> 00:07:38,720
But it's not.

127
00:07:38,720 --> 00:07:40,670
We're just executing a shell command.

128
00:07:40,670 --> 00:07:46,070
And if we hit run it's going to be queued for execution, which means that it's going to be displayed

129
00:07:46,070 --> 00:07:46,580
in here.

130
00:07:46,580 --> 00:07:47,750
And the tasks.

131
00:07:48,700 --> 00:07:54,580
And if we look at the last task that we have in here, we executed there, and we have all of the files

132
00:07:54,580 --> 00:07:57,430
and directories within the current working directory.

133
00:07:58,520 --> 00:08:01,880
So that's a basic overview of how to use the GUI.

134
00:08:01,910 --> 00:08:08,900
However, there is still so much more that we can do using the modules that Empire gives us in here.

135
00:08:09,380 --> 00:08:12,680
We're actually going to be having a lot of fun with this section next.

136
00:08:12,680 --> 00:08:18,380
As you can see, there are hundreds of modules in here that can be used for privilege escalation, for

137
00:08:18,380 --> 00:08:24,590
persistence, for accessing system resources, the camera, the keyboard, anything you can think of,

138
00:08:24,590 --> 00:08:26,330
you can execute it from here.

139
00:08:26,330 --> 00:08:31,430
You can even run ransomware from within this program, and we'll be covering all of that next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:07,250
So, as mentioned earlier, one of the best features of Empire is the fact that it has a huge library

2
00:00:07,250 --> 00:00:09,380
of Post-exploitation modules.

3
00:00:09,740 --> 00:00:15,620
These allow us to escalate our privileges, access system resources, spy on the target, and even run

4
00:00:15,620 --> 00:00:16,580
ransomware.

5
00:00:16,760 --> 00:00:22,640
The best thing about this is that this library is continually growing, so people are contributing to

6
00:00:22,640 --> 00:00:27,620
it all of the time, and you can even go ahead and create your own modules in the future.

7
00:00:27,890 --> 00:00:30,590
So as mentioned, this library is huge.

8
00:00:30,590 --> 00:00:36,290
Currently there is over 400 modules in this library, so there is no way for me to cover them all.

9
00:00:36,290 --> 00:00:39,830
But the good thing is using these modules is very similar.

10
00:00:39,830 --> 00:00:45,080
So I'm going to show you how to learn about these modules and how to follow resources and find information

11
00:00:45,080 --> 00:00:45,740
about them.

12
00:00:45,740 --> 00:00:51,050
And then once we run a few of them, you should be able to run any other module in your own time.

13
00:00:51,050 --> 00:00:56,150
So I highly recommend spending some time after this section to familiarize yourself with the rest of

14
00:00:56,150 --> 00:01:01,790
the modules, and just to see which ones are going to be the most useful for your use cases.

15
00:01:02,240 --> 00:01:06,890
So first of all, as you can see, all you have to do I'm just going to go back to the agents.

16
00:01:06,890 --> 00:01:11,030
If you click on the agent that you have, this is where you control your target.

17
00:01:11,030 --> 00:01:13,070
And we saw how to do that earlier.

18
00:01:13,070 --> 00:01:20,030
And under the interact under the form, we have a section in here that allow us to execute modules on

19
00:01:20,030 --> 00:01:21,140
the target agent.

20
00:01:21,140 --> 00:01:25,400
And if we click in here you'll see all of the modules that we have.

21
00:01:25,400 --> 00:01:30,200
So you can even use the search box to search for any module that you want.

22
00:01:30,200 --> 00:01:35,060
And even though you still don't know anything about modules, you can literally think of anything that

23
00:01:35,060 --> 00:01:37,370
you want to do on the target computer.

24
00:01:37,370 --> 00:01:39,950
And there is probably a module for that.

25
00:01:39,950 --> 00:01:43,100
For example, let's say I want to restart the target computer.

26
00:01:43,100 --> 00:01:44,810
I can look for restart.

27
00:01:44,810 --> 00:01:48,230
And as you can see I have a module that allows me to do that.

28
00:01:48,680 --> 00:01:54,980
If I want to log off the target computer or log the user out again, as you can see, we have a module

29
00:01:54,980 --> 00:01:55,850
for that.

30
00:01:55,850 --> 00:01:59,720
Let's say we want to troll the target computer.

31
00:01:59,720 --> 00:02:00,470
This is funny.

32
00:02:00,470 --> 00:02:04,640
So there is a specific category of modules called troll exploit.

33
00:02:05,320 --> 00:02:09,880
And as you can see, there are many modules that you can use to troll the target.

34
00:02:09,880 --> 00:02:16,240
For example, change their wallpaper, play a voice, send them a message which sending the message

35
00:02:16,240 --> 00:02:18,340
can actually be useful for social engineering.

36
00:02:18,340 --> 00:02:20,140
You can get them to go and do something.

37
00:02:20,140 --> 00:02:24,850
So I don't think it's only used for trolling, but there is a lot of other modules in here.

38
00:02:24,850 --> 00:02:27,700
Now let's do something that is actually kind of useful.

39
00:02:27,700 --> 00:02:31,120
I'm keeping it very simple because this is just an introduction to the modules.

40
00:02:31,120 --> 00:02:33,430
So let's say we want to take a screenshot.

41
00:02:33,430 --> 00:02:37,390
And again you have many modules that allow you to take a screenshot.

42
00:02:37,390 --> 00:02:40,930
Now our back door was a PowerShell back door.

43
00:02:40,930 --> 00:02:45,850
So that's why I'm going to select the module that has PowerShell as the programming language.

44
00:02:46,030 --> 00:02:47,830
So we're going to click that.

45
00:02:47,830 --> 00:02:53,500
And as you can see you're going to get a nice interface that allows you to execute the module.

46
00:02:53,590 --> 00:02:57,730
Now in here you can see there is a brief description of the module.

47
00:02:57,730 --> 00:02:58,900
Now this one is very simple.

48
00:02:58,900 --> 00:03:02,290
It's literally telling you that it's going to take a screenshot of the desktop.

49
00:03:02,440 --> 00:03:05,650
If you click it it's going to show you more information.

50
00:03:05,650 --> 00:03:10,030
And this is where it's really, really useful when it comes to more complicated modules.

51
00:03:10,030 --> 00:03:15,670
So you're always going to have comments or resources that will redirect you to the code of the module.

52
00:03:15,670 --> 00:03:21,340
And in many cases, in the complicated ones, it will actually redirect you to resources that will explain

53
00:03:21,340 --> 00:03:23,020
to you how to use this module.

54
00:03:23,020 --> 00:03:25,690
So this is very, very useful in the future.

55
00:03:25,870 --> 00:03:29,980
You can also see the language, the programming language that the module was written in.

56
00:03:29,980 --> 00:03:33,280
In this case it's PowerShell which is great minimum version.

57
00:03:33,280 --> 00:03:35,740
It needs to be PowerShell two at minimum.

58
00:03:35,830 --> 00:03:40,060
It's also telling you if this module is going to run in the background or not.

59
00:03:40,060 --> 00:03:44,560
This is referring within the context of Empire PowerShell.

60
00:03:44,560 --> 00:03:50,410
So if this is true, it means that you can execute other modules while this module is running.

61
00:03:50,410 --> 00:03:52,240
Hence the background is true.

62
00:03:52,240 --> 00:03:58,810
If it says false like this one, it means that you will not be able to execute other operations until

63
00:03:58,810 --> 00:04:01,150
this module finishes execution.

64
00:04:01,780 --> 00:04:06,670
The OpSec safe in here refers to operational security.

65
00:04:06,670 --> 00:04:11,050
This tells us whether this module is operationally secure or not.

66
00:04:11,050 --> 00:04:17,470
And what we mean by that is, if it is true, it means that this module leaves very little or no traces.

67
00:04:17,470 --> 00:04:23,410
It usually does this by avoiding actions that could raise alarms, like using the storage of the compromised

68
00:04:23,410 --> 00:04:24,010
machine.

69
00:04:24,310 --> 00:04:28,870
It's also telling us if it needs admin and this one doesn't need admin, it's false.

70
00:04:29,200 --> 00:04:34,900
And if the module outputs a number of extensions you'd be able to see it in here.

71
00:04:34,900 --> 00:04:41,260
But the main fields that you're going to see on every module are going to be the language, the background,

72
00:04:41,260 --> 00:04:43,690
the OP safe and the needs admin.

73
00:04:43,690 --> 00:04:46,540
So this is very important to understand what these mean.

74
00:04:46,540 --> 00:04:51,490
So even though we're running a very simple module in here, these values will be very important in the

75
00:04:51,490 --> 00:04:54,910
future when you get to running more complex modules.

76
00:04:55,580 --> 00:04:56,870
Finally in here.

77
00:04:56,870 --> 00:04:59,210
It's also giving you the miter.

78
00:04:59,240 --> 00:05:05,660
AT&amp;T technique miter AT&amp;T is a database of known hacking techniques.

79
00:05:05,660 --> 00:05:09,680
It's kind of a standard when it comes to C2 and command and control frameworks.

80
00:05:09,680 --> 00:05:16,310
So if you click this, it will explain to you what technique is going to be used by this module and

81
00:05:16,310 --> 00:05:19,520
how it's implemented in different scenarios and so on.

82
00:05:19,520 --> 00:05:26,420
So once you work as a red teamer, this becomes more important because companies, a lot of the time

83
00:05:26,420 --> 00:05:30,620
they have certain IDs or certain techniques that they prioritize.

84
00:05:30,620 --> 00:05:35,690
So you're going to have these fields and their values in every module regardless of what this module

85
00:05:35,690 --> 00:05:36,110
does.

86
00:05:36,110 --> 00:05:40,700
That's why it's very important to understand what they do or what they mean.

87
00:05:40,700 --> 00:05:45,170
Now right here we have the module that we're actually about to execute, which is a module that's simply

88
00:05:45,170 --> 00:05:48,740
going to take a screenshot as described in here.

89
00:05:49,340 --> 00:05:54,200
You can tick these boxes to ignore the admin check or ignore the language version check.

90
00:05:54,200 --> 00:05:55,520
We don't want to do that.

91
00:05:55,520 --> 00:05:59,390
You can specify the aspect ratio of the screenshot.

92
00:05:59,390 --> 00:06:02,060
I don't want to do this, so I simply just want to run it.

93
00:06:02,060 --> 00:06:03,650
So I'm going to click submit.

94
00:06:03,980 --> 00:06:06,470
And as you can see it's queued for execution.

95
00:06:06,470 --> 00:06:09,020
So we can track that in our tasks.

96
00:06:09,020 --> 00:06:11,690
In here we have it in here.

97
00:06:11,690 --> 00:06:14,330
We're going to click on the expand.

98
00:06:14,330 --> 00:06:19,160
So we can simply click on View Image in here to see the image that was captured.

99
00:06:19,220 --> 00:06:20,210
And perfect.

100
00:06:20,210 --> 00:06:26,060
As you can see we have a screenshot of the target computer which is this computer right here.

101
00:06:27,020 --> 00:06:29,990
And we can also see this image in our downloads.

102
00:06:29,990 --> 00:06:37,130
So if we go to the downloads here on the left, as you can see, we have a new file and we can click

103
00:06:37,130 --> 00:06:38,990
it here download.

104
00:06:40,880 --> 00:06:43,400
Click save and that's saved for me.

105
00:06:43,400 --> 00:06:48,230
So if I open it, as you can see, we have the screenshot in here.

106
00:06:48,230 --> 00:06:54,260
So I know this is a very simple module, but the idea was to familiarize you with how to use a module

107
00:06:54,260 --> 00:06:57,980
and all of the different fields that you're going to see in every module.

108
00:06:57,980 --> 00:07:02,000
This should make it much easier for you to run other modules in the future.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:05,780
Okay, so now that we have a basic understanding of how to use the modules, and we saw how we can actually

2
00:00:05,780 --> 00:00:11,750
use them from within the agent view in here, I want to dive deeper and just show you more and just

3
00:00:11,750 --> 00:00:14,060
spend a little bit more time about modules.

4
00:00:14,060 --> 00:00:19,220
And this time, instead of using a module from here, from the agent view, we're actually going to

5
00:00:19,220 --> 00:00:21,560
go to the modules here in the left.

6
00:00:21,680 --> 00:00:26,510
And as you can see in this view you're going to be able to see the full database of modules.

7
00:00:26,510 --> 00:00:30,320
So as you can see we've got 385 modules in here.

8
00:00:30,800 --> 00:00:37,130
And to some people this view is a little bit more user friendly because as you can see, instead of

9
00:00:37,130 --> 00:00:43,520
having to go inside the module similar to what we did before, we can see a lot of its information right

10
00:00:43,520 --> 00:00:44,570
here in front of us.

11
00:00:44,570 --> 00:00:49,910
So we can see the module name, the programming language that it was written on, if it needs admin,

12
00:00:49,910 --> 00:00:53,690
if it's operationally safe, and we explained what that is previously.

13
00:00:53,690 --> 00:00:59,660
So go back and revise that if you don't know what it is, if it can run in the background and the techniques

14
00:00:59,660 --> 00:01:00,530
used in it.

15
00:01:00,740 --> 00:01:06,440
Not only that, but if you click on the drop down in here, you'll actually also see the description

16
00:01:06,440 --> 00:01:07,490
of this module.

17
00:01:07,490 --> 00:01:11,960
So this is very, very useful if you were searching for a specific module.

18
00:01:11,960 --> 00:01:15,200
And also you can simply open them in a new tab.

19
00:01:15,200 --> 00:01:17,780
So right click new tab right click new tab.

20
00:01:17,780 --> 00:01:23,360
Again assuming that you want to run a number of modules, you can just open them all in a new tab.

21
00:01:23,360 --> 00:01:27,560
And then once you're done, you can go ahead and execute them one by one.

22
00:01:28,740 --> 00:01:33,870
So I know it might seem simple, but this saves you a lot of time when you're actually engaging with

23
00:01:33,870 --> 00:01:35,700
a lot of targets in the future.

24
00:01:35,850 --> 00:01:41,460
Another really useful feature of this view is the search and the filtering options that you have in

25
00:01:41,460 --> 00:01:42,090
here.

26
00:01:42,120 --> 00:01:48,330
So as you know, our agent is a PowerShell agent, meaning that we can only execute PowerShell modules.

27
00:01:48,330 --> 00:01:53,160
So you'd be wasting a lot of time if you'd be executing these Python modules, because they're not going

28
00:01:53,160 --> 00:01:56,940
to work because our backdoor or agent is a PowerShell agent.

29
00:01:56,970 --> 00:02:03,270
Therefore, you can simply come here to the language and untick all and select PowerShell.

30
00:02:03,270 --> 00:02:09,660
And now instead of seeing 385, you only have 252 modules that we can run from.

31
00:02:10,390 --> 00:02:14,560
Again, assuming that you have an environment that is very secure.

32
00:02:14,560 --> 00:02:19,090
So you might want to avoid the Non-safe modules.

33
00:02:19,090 --> 00:02:25,390
So again, instead of selecting all of them we're only going to select the ones that are operationally

34
00:02:25,390 --> 00:02:26,110
safe.

35
00:02:26,110 --> 00:02:31,360
And now this time you have 173 modules instead of the 258.

36
00:02:31,630 --> 00:02:34,630
So this way you'll be able to filter that much better.

37
00:02:34,630 --> 00:02:40,750
And also you can use the search functionality in here to search for whatever you want.

38
00:02:40,750 --> 00:02:47,080
So let's assume that you want to use a module that will help you find sensitive files on the target.

39
00:02:47,080 --> 00:02:54,850
I can simply look for find, and that has filtered all of the modules that use PowerShell, and that

40
00:02:54,850 --> 00:02:58,180
can be used to find sensitive files on the target.

41
00:02:58,180 --> 00:03:01,090
Again, let's say I want them to be operationally safe.

42
00:03:01,090 --> 00:03:02,500
I'm going to set that to true.

43
00:03:02,500 --> 00:03:09,760
And now I have the modules that are operationally safe that can help me find interesting files on the

44
00:03:09,760 --> 00:03:10,420
target.

45
00:03:11,100 --> 00:03:12,930
And I can simply run it from here.

46
00:03:12,930 --> 00:03:18,060
I don't actually have to go back to the agents to run it, so all I have to do, like I said, if I

47
00:03:18,060 --> 00:03:24,030
wasn't sure which one I want, I can simply open them in a new tab, or I can simply just open it in

48
00:03:24,030 --> 00:03:24,570
here.

49
00:03:25,080 --> 00:03:28,830
And then I get a very nice view, similar to what we saw earlier.

50
00:03:28,830 --> 00:03:35,490
But again, this time another feature is that you actually get to select which agent or agents that

51
00:03:35,490 --> 00:03:37,530
you want to execute this module on.

52
00:03:37,530 --> 00:03:44,850
So previously from the agent view, we were able to only execute the module on one agent or one target.

53
00:03:44,850 --> 00:03:51,510
But you could potentially have five, 10 or 50 targets that you have access to at the same time effectively

54
00:03:51,510 --> 00:03:52,620
having a botnet.

55
00:03:52,620 --> 00:03:57,630
So in that case, you can simply select the agents that you want from this dropdown menu.

56
00:03:57,630 --> 00:03:59,220
So right now I only have one.

57
00:03:59,220 --> 00:04:02,070
But you can select the 50 agents that you have.

58
00:04:02,070 --> 00:04:08,700
If you had access to 50 computers select them in here and you'll be able to execute this module on all

59
00:04:08,700 --> 00:04:10,830
of the agents that you're selecting in here.

60
00:04:11,930 --> 00:04:12,500
Now.

61
00:04:12,500 --> 00:04:16,730
This module allows us to discover interesting files in the target.

62
00:04:16,730 --> 00:04:21,950
So it's asking you for the path where you want to search for interesting files.

63
00:04:21,950 --> 00:04:26,510
You can simply just do C to search all of the C directory.

64
00:04:26,510 --> 00:04:34,010
But just to make this faster I'm going to look for files in C users John, because that is the user

65
00:04:34,010 --> 00:04:35,630
that we are logged in as.

66
00:04:36,140 --> 00:04:37,820
I'm going to keep everything the same.

67
00:04:37,820 --> 00:04:41,360
You have some optional fields, but you have a description for these optional fields.

68
00:04:41,360 --> 00:04:43,970
So I don't want to waste time just talking about all of them.

69
00:04:43,970 --> 00:04:47,510
You can spend your own time and learn about all of these options.

70
00:04:47,510 --> 00:04:49,130
We're keeping everything simple.

71
00:04:49,130 --> 00:04:53,780
I'm just going to click submit and that is queued for execution.

72
00:04:53,780 --> 00:04:56,180
So now we're going to go to the agents.

73
00:04:56,180 --> 00:04:58,010
We're going to go to our agent.

74
00:04:58,010 --> 00:04:59,930
We're going to go to the tasks.

75
00:04:59,930 --> 00:05:02,570
And we should have the task in here.

76
00:05:02,570 --> 00:05:07,160
As you can see we have the results of the execution of that module.

77
00:05:07,160 --> 00:05:11,330
And it's showing us all of the files that it thinks are interesting.

78
00:05:11,330 --> 00:05:15,830
So we have a file in here and the Chrome login data.

79
00:05:16,370 --> 00:05:23,330
We have an interesting file in here and the credentials and we have the passwords dot txt file that

80
00:05:23,330 --> 00:05:26,330
we've been loading in multiple examples previously.

81
00:05:26,330 --> 00:05:32,840
So assuming you've just discovered that you can simply copy that and access it from your file browser

82
00:05:32,840 --> 00:05:34,460
as I showed you previously.

83
00:05:34,460 --> 00:05:36,740
Or you can go to the interact.

84
00:05:36,740 --> 00:05:40,790
And like I said, you can execute a single shell command in here.

85
00:05:40,790 --> 00:05:44,750
So we can just do more followed by the file that we want to read.

86
00:05:44,750 --> 00:05:46,040
I'm going to run.

87
00:05:46,040 --> 00:05:50,690
And then if I go back to my tasks I should have the result in here.

88
00:05:51,350 --> 00:05:57,350
As you can see, we have the contents of the file that we were looking for, which has the username

89
00:05:57,350 --> 00:05:58,400
and the password.

90
00:05:59,650 --> 00:06:05,140
So I know this is another simple module, but the main goal was to familiarize you with the modules

91
00:06:05,140 --> 00:06:11,590
view in here, and to show you how useful it can be, especially with the use of the filters in here

92
00:06:11,590 --> 00:06:12,460
on the left.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:04,160
Okay, so now I want to show you how to use some collection modules.

2
00:00:04,160 --> 00:00:10,130
These are going to allow us to collect usernames and passwords, such as the username and the password

3
00:00:10,130 --> 00:00:13,040
of the logged in user or log keystrokes.

4
00:00:13,040 --> 00:00:17,390
Basically record every keystroke that the target enters on their keyboard.

5
00:00:17,390 --> 00:00:20,270
We're also going to see how to access the clipboard.

6
00:00:20,270 --> 00:00:24,740
And these are all going to be examples of the collection modules within Empire.

7
00:00:24,740 --> 00:00:29,330
But these modules can be used to do so much more on the target.

8
00:00:29,420 --> 00:00:31,460
So let me show you a quick example.

9
00:00:31,460 --> 00:00:32,870
We're going to go to the target.

10
00:00:32,870 --> 00:00:34,850
We're going to go to our agent.

11
00:00:34,970 --> 00:00:41,600
And in here if you simply type collection, you'll see all of the different collection modules that

12
00:00:41,600 --> 00:00:42,350
you can use.

13
00:00:42,350 --> 00:00:45,110
Now these are all in Python so we can't use them now.

14
00:00:45,110 --> 00:00:47,360
We can only use the PowerShell ones.

15
00:00:47,360 --> 00:00:53,000
And we have a really good example in here, PowerShell wiretap which allows you to basically access

16
00:00:53,000 --> 00:00:55,550
the camera, the mic, the keyboard and so on.

17
00:00:56,550 --> 00:01:01,440
You've got other modules in here that will prompt the user to enter a username and a password, like

18
00:01:01,440 --> 00:01:02,700
the prompt one in here.

19
00:01:02,700 --> 00:01:08,430
There are so many useful modules in here, and like I said, if you're not sure about a module, you

20
00:01:08,430 --> 00:01:11,370
can select it such as the toasted module in here.

21
00:01:11,370 --> 00:01:16,620
And if you're not sure how it works, you click the description and it's going to give you a detailed

22
00:01:16,620 --> 00:01:18,540
description of how it works.

23
00:01:18,540 --> 00:01:20,610
Comments or more information.

24
00:01:20,610 --> 00:01:24,240
You can simply load this blog post to learn about how to use it.

25
00:01:24,240 --> 00:01:27,600
Again, it tells you the programming language and so on in here.

26
00:01:27,600 --> 00:01:30,180
So using these modules is very, very simple.

27
00:01:30,180 --> 00:01:33,360
As long as you're willing to just do a little bit of reading.

28
00:01:34,150 --> 00:01:39,760
Now you can see that this module is going to display a notification to the target asking them for their

29
00:01:39,760 --> 00:01:41,020
username and password.

30
00:01:41,050 --> 00:01:44,590
Now this notification is going to be a windows notification.

31
00:01:44,590 --> 00:01:47,020
So it's going to be very very believable.

32
00:01:47,020 --> 00:01:48,730
Let me show you how to use it.

33
00:01:48,730 --> 00:01:50,620
Again using it is very simple.

34
00:01:50,620 --> 00:01:54,910
We just have to scroll down and fill up the fields as needed.

35
00:01:54,910 --> 00:01:58,120
So as you can see, you can set whatever title you want.

36
00:01:58,120 --> 00:02:03,160
But this title is actually pretty good because it's going to tell the user that the computer is going

37
00:02:03,160 --> 00:02:08,110
to restart in five minutes to install updates, and we know that windows does that all of the time.

38
00:02:08,110 --> 00:02:10,630
It shows you a prompt saying that it's going to restart.

39
00:02:10,630 --> 00:02:15,160
To install updates, you can set the message of the notification box.

40
00:02:15,160 --> 00:02:17,740
So this is the actual full length message.

41
00:02:17,740 --> 00:02:21,430
You can modify this as you want, but this message is actually pretty good.

42
00:02:21,820 --> 00:02:24,040
You can select the name of the application.

43
00:02:24,040 --> 00:02:27,520
So this is just the name of the application that's going to be displayed.

44
00:02:27,520 --> 00:02:29,050
We're keeping it the same.

45
00:02:29,440 --> 00:02:34,780
You can set the title of the box that's going to ask for the username and the password.

46
00:02:34,780 --> 00:02:39,220
And again going with the scenario that we're going with, it's going to ask them if they want to restart

47
00:02:39,220 --> 00:02:40,180
their computer.

48
00:02:40,180 --> 00:02:42,070
He can set the message.

49
00:02:42,070 --> 00:02:48,490
So in here it's basically telling them that they need to authenticate to put the username and the password

50
00:02:48,490 --> 00:02:51,280
in order to skip the restart.

51
00:02:51,280 --> 00:02:56,140
In order to postpone the restart, you can select the notification type.

52
00:02:56,140 --> 00:02:58,600
You can set it to system or application.

53
00:02:58,600 --> 00:03:03,340
But since we're asking them for credentials, it makes sense to keep it at system.

54
00:03:03,340 --> 00:03:10,630
And these optional fields here are actually very, very useful because you can set this value to true

55
00:03:10,630 --> 00:03:16,600
so that if the user enters the wrong credentials, it will actually ask the user to enter it again.

56
00:03:16,600 --> 00:03:21,760
So whenever they enter the credentials, empire is going to go ahead and verify that these are correct

57
00:03:21,760 --> 00:03:27,100
and only stop displaying the warning message once they enter the correct password.

58
00:03:27,100 --> 00:03:28,120
So let me show you.

59
00:03:28,120 --> 00:03:31,720
I'm going to click submit and we're going to go to the target windows.

60
00:03:31,720 --> 00:03:32,890
This one right here.

61
00:03:34,180 --> 00:03:39,700
And as you can see, we got a system notification in here telling us that windows is going to restart

62
00:03:39,700 --> 00:03:43,720
in five minutes unless I click on the postpone in here.

63
00:03:44,230 --> 00:03:48,850
Now, in order to postpone, it's asking me to put my username and my password.

64
00:03:48,850 --> 00:03:54,370
So I'm actually first I'm going to put the correct username and I'm going to put the wrong password.

65
00:03:54,370 --> 00:03:57,430
And you will see that it's actually not going to accept that.

66
00:03:57,430 --> 00:03:59,920
It's going to display the notification for me.

67
00:03:59,920 --> 00:04:00,610
Again.

68
00:04:01,150 --> 00:04:04,960
As you can see, we got the notification again because I put the wrong password.

69
00:04:04,960 --> 00:04:07,690
And now if I put the correct password.

70
00:04:08,730 --> 00:04:10,140
And hit okay.

71
00:04:10,140 --> 00:04:13,770
You will see that I will not get this notification again.

72
00:04:13,770 --> 00:04:16,770
And if we go back to our tasks.

73
00:04:17,680 --> 00:04:20,050
Look at the value and the last task.

74
00:04:20,410 --> 00:04:24,460
As you can see, we got the username and the password.

75
00:04:24,460 --> 00:04:30,040
And all of this was done using a very nice looking proper windows notification.

76
00:04:30,040 --> 00:04:36,250
It doesn't look suspicious at all, and it even verified that the password entered by the user was actually

77
00:04:36,250 --> 00:04:37,450
the correct password.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,230 --> 00:00:06,290
Okay, so now that we know how to ask the user in order to enter their actual normal username and password,

2
00:00:06,290 --> 00:00:12,230
let's have a look at some other collection modules that will allow us to register every keystrokes entered

3
00:00:12,230 --> 00:00:12,980
on the keyboard.

4
00:00:12,980 --> 00:00:15,230
So basically they will start a keylogger.

5
00:00:15,230 --> 00:00:19,250
And at the same time we're also going to monitor the clipboard.

6
00:00:19,250 --> 00:00:26,660
So if they copy a password from a text file or from a password manager will still be able to steal it.

7
00:00:26,660 --> 00:00:31,340
So even if they don't physically type the password using their keyboard, we're still going to be able

8
00:00:31,340 --> 00:00:33,680
to steal their password again.

9
00:00:33,680 --> 00:00:40,280
We're going to go back to the interact inside our agent, and we're going to look for collection.

10
00:00:40,580 --> 00:00:43,970
And you're going to see all of the possible collection modules.

11
00:00:43,970 --> 00:00:46,490
And what I'm looking for is key Log.

12
00:00:46,490 --> 00:00:48,920
We're going to click the module that we want.

13
00:00:48,920 --> 00:00:53,600
And again as usual this is usually not expanded collapsed like this.

14
00:00:53,600 --> 00:01:00,080
So you can press it to expand it and learn about how this specific module is going to run.

15
00:01:00,080 --> 00:01:01,550
But it's very simple.

16
00:01:01,550 --> 00:01:06,830
It's basically going to record every single keystroke the person enters on their keyboard.

17
00:01:06,830 --> 00:01:10,130
You can set up the sleep time between key presses.

18
00:01:10,130 --> 00:01:11,840
I'm going to keep it the way it is.

19
00:01:11,840 --> 00:01:13,850
I'm simply going to click submit.

20
00:01:13,850 --> 00:01:20,180
And before we go ahead and see how these keystrokes are recorded, I'm actually going to run another

21
00:01:20,180 --> 00:01:27,500
module in order to monitor the clipboard so that if the target copies a password from a text file or

22
00:01:27,500 --> 00:01:33,200
from a password manager, I'll still be able to collect that password and see it.

23
00:01:33,200 --> 00:01:38,300
So to do that, we're simply going to look for clipboard because that's what we want to monitor.

24
00:01:38,300 --> 00:01:43,490
Like I said at the start of this, if you can think of something that you want to do on the target,

25
00:01:43,490 --> 00:01:47,030
simply type it in the search box and you will probably find it.

26
00:01:47,390 --> 00:01:51,950
So as you can see, we have a module written in Python and one written in PowerShell.

27
00:01:51,950 --> 00:01:55,760
We're going to go with the PowerShell one because our backdoor is written in PowerShell.

28
00:01:55,760 --> 00:02:01,760
And as usual you got your information in here that you can use and read to learn more about this module.

29
00:02:01,940 --> 00:02:03,740
But we're going to be keeping everything the same.

30
00:02:03,740 --> 00:02:05,960
I'm not going to change anything here.

31
00:02:05,990 --> 00:02:08,690
I'm going to click on submit and that's it.

32
00:02:08,690 --> 00:02:11,810
So now I am running two modules at the same time.

33
00:02:11,810 --> 00:02:17,360
One of them is going to record every single keystroke entered physically on the keyboard, and the other

34
00:02:17,360 --> 00:02:23,210
one is going to record everything that gets copied in the clipboard, so that if the user is copying

35
00:02:23,210 --> 00:02:28,310
passwords from a text file or from a password manager, we're still going to be able to capture them.

36
00:02:29,050 --> 00:02:35,050
Now let's go to a target computer and let's say our user is simply just going to go to Gmail.

37
00:02:36,130 --> 00:02:39,100
And they're going to want to sign to their account.

38
00:02:39,100 --> 00:02:42,520
So let's say their account is John Wick.

39
00:02:43,490 --> 00:02:47,720
And then they're going to put their password 111111.

40
00:02:47,720 --> 00:02:48,560
Click next.

41
00:02:48,560 --> 00:02:49,640
Now that's the wrong password.

42
00:02:49,640 --> 00:02:50,300
But that's fine.

43
00:02:50,300 --> 00:02:52,460
It should have been recorded by the keylogger.

44
00:02:52,460 --> 00:02:58,130
And let's take another example where the user doesn't actually physically type their password.

45
00:02:58,130 --> 00:03:04,280
Maybe they have it in a text file, or maybe they actually use a password manager.

46
00:03:04,670 --> 00:03:09,710
So they're going to simply going to copy the password and they're never going to type it.

47
00:03:09,710 --> 00:03:12,500
So let's go ahead and paste it here.

48
00:03:13,660 --> 00:03:17,710
Hit enter and let's go ahead to the hacker machine.

49
00:03:17,710 --> 00:03:22,000
Go to the tasks and see if we manage to record these values.

50
00:03:22,870 --> 00:03:26,200
So first of all, let's look at the key strikes that we captured.

51
00:03:26,200 --> 00:03:27,460
And perfect.

52
00:03:27,460 --> 00:03:31,750
As you can see it's telling us it captured the following key strikes.

53
00:03:32,500 --> 00:03:35,620
From a mozilla Firefox browser.

54
00:03:36,840 --> 00:03:39,300
The person went to gmail.com.

55
00:03:39,300 --> 00:03:44,970
They typed this email and I actually made a mistake by writing this quote and then I deleted it.

56
00:03:44,970 --> 00:03:50,640
Then I wrote the at gmail.com and then I put the password 111111.

57
00:03:51,060 --> 00:03:56,100
And this keylogger continues to run as long as the computer is running.

58
00:03:56,580 --> 00:03:59,430
Now at the same time, we were also monitoring the clipboard.

59
00:03:59,430 --> 00:04:04,080
So as you can see, we have a notification here from the clipboard module.

60
00:04:04,080 --> 00:04:11,340
And as you can see, it's telling us that at this time it was able to capture this password or this

61
00:04:11,340 --> 00:04:13,110
value in the clipboard.

62
00:04:13,350 --> 00:04:19,230
So this is very, very useful because in many cases people say, well, a keylogger is not that useful

63
00:04:19,230 --> 00:04:23,130
because a lot of people these days, they simply use password managers.

64
00:04:23,130 --> 00:04:29,790
And as you can see, you can simply use a keyboard monitoring module like this one in order to still

65
00:04:29,790 --> 00:04:37,440
capture passwords that people copy from their password managers into the input boxes whenever they want

66
00:04:37,440 --> 00:04:37,950
to log in.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:03,260
So previously we covered a number of modules in Empire.

2
00:00:03,260 --> 00:00:06,350
And please note that these are not the only modules that you can run.

3
00:00:06,350 --> 00:00:07,820
Like I said, there are so many.

4
00:00:07,820 --> 00:00:12,170
I'm just focusing on some of the most unique modules to Empire.

5
00:00:12,170 --> 00:00:17,870
And like I said, I'm trying to cover different examples so that in the future you should be able to

6
00:00:17,870 --> 00:00:21,590
pick up any module and be able to use it yourself.

7
00:00:21,590 --> 00:00:27,290
Now, a very interesting module that Empire has built in is the ransomware module.

8
00:00:27,290 --> 00:00:30,620
And before we use that, let's just talk about ransomware for a minute.

9
00:00:30,620 --> 00:00:35,390
You probably already know what it is, but let me just walk you through how ransom works very, very

10
00:00:35,390 --> 00:00:35,990
quickly.

11
00:00:36,350 --> 00:00:42,050
So you have a computer right here, and it's got its normal file system, its normal directories, documents,

12
00:00:42,050 --> 00:00:42,920
downloads, pictures.

13
00:00:42,920 --> 00:00:50,510
Just as an example, once this computer gets infected by a ransomware malware, it's going to encrypt

14
00:00:50,510 --> 00:00:55,340
one of these directories or potentially the whole file system in many cases.

15
00:00:55,760 --> 00:01:01,160
Once it does that, the files that you have will still exist within this directory.

16
00:01:01,160 --> 00:01:05,510
But they are encrypted, so you will not be able to execute them.

17
00:01:05,510 --> 00:01:08,000
If they're pictures, you're not going to be able to see them.

18
00:01:08,000 --> 00:01:11,060
If they're text files are not going to be able to read the text.

19
00:01:11,060 --> 00:01:14,990
It's simply fully encrypted and it's unusable.

20
00:01:14,990 --> 00:01:20,690
And the only way for you to get it back is using the encryption key, which the hacker has.

21
00:01:21,140 --> 00:01:26,840
Therefore, they usually ask you to pay a certain amount of money a ransom.

22
00:01:26,840 --> 00:01:32,510
And if you do pay that, they will give you the key and as a result, you're going to get your file

23
00:01:32,540 --> 00:01:32,990
back.

24
00:01:32,990 --> 00:01:36,860
So if you pay the ransom, you're going to get your file back because they're going to give you the

25
00:01:36,860 --> 00:01:41,270
key which you will use to decrypt the encrypted file.

26
00:01:41,270 --> 00:01:42,860
So file gets encrypted.

27
00:01:42,860 --> 00:01:44,990
Only way to decrypt it is using the key.

28
00:01:44,990 --> 00:01:46,730
And the hacker has the key.

29
00:01:47,790 --> 00:01:50,010
Now you might ask, why am I covering this?

30
00:01:50,010 --> 00:01:53,070
This is definitely not ethical and you are very right.

31
00:01:53,070 --> 00:01:54,600
This is very, very bad.

32
00:01:54,600 --> 00:01:56,040
Nobody should do this.

33
00:01:56,040 --> 00:02:02,130
But the reason why we do it because as a red teamer or a pen tester, you will actually need to know

34
00:02:02,130 --> 00:02:08,460
how to do this because you will be asked if you're working at an environment to run disaster scenarios.

35
00:02:08,460 --> 00:02:13,290
And a very common threat that organizations face these days is ransomware.

36
00:02:13,290 --> 00:02:19,710
So your boss might come into you and ask you to go ahead and infect some computers and run ransomware

37
00:02:19,710 --> 00:02:24,690
on them in order to see how the disaster response team is going to respond to this.

38
00:02:24,810 --> 00:02:28,500
And that's why it is important for you to learn how to do this.

39
00:02:28,860 --> 00:02:31,140
So let's go ahead and do this in practice.

40
00:02:31,140 --> 00:02:36,510
Now I've already compromised a Windows 11 machine in here, this machine right here.

41
00:02:36,900 --> 00:02:40,740
And we're going to go ahead and look for a ransomware module.

42
00:02:40,740 --> 00:02:41,460
Like I said.

43
00:02:41,460 --> 00:02:45,660
And I've said this multiple times now, if you think of anything that you can do on a target machine,

44
00:02:45,660 --> 00:02:48,900
simply look for a module that does that and you will find one.

45
00:02:48,900 --> 00:02:51,480
So we're going to go with this module right here.

46
00:02:51,480 --> 00:02:54,270
And as you can see this one has quite a few options.

47
00:02:54,270 --> 00:02:58,320
And I'm actually going to walk you through them because they are different than other options that you

48
00:02:58,320 --> 00:02:59,880
would see in other modules.

49
00:02:59,880 --> 00:03:03,270
So first of all I'm going to turn on the demo option.

50
00:03:03,570 --> 00:03:10,050
This option is going to remove the wallpaper, make it red, and show a ransomware notification very

51
00:03:10,050 --> 00:03:12,420
similar to actual real ransomware.

52
00:03:12,930 --> 00:03:18,150
We're going to set the mode to encrypt because we want to simulate an actual ransomware attack.

53
00:03:18,180 --> 00:03:21,360
You can set this to decrypt to undo the attack.

54
00:03:21,360 --> 00:03:23,310
And we're going to do that at the end of the video.

55
00:03:23,310 --> 00:03:25,980
So for now we want to simulate an actual attack.

56
00:03:25,980 --> 00:03:28,380
And therefore we're going to be encrypting the files.

57
00:03:29,460 --> 00:03:34,920
The exfiltrate will allow you to download or exfiltrate the files to your command and control server.

58
00:03:34,920 --> 00:03:37,740
We're going to keep this the way it is for now or keep it off.

59
00:03:37,740 --> 00:03:43,350
And next you're going to specify the directory that you're going to encrypt in this attack.

60
00:03:43,350 --> 00:03:49,680
So we're going to set this to C users John documents.

61
00:03:50,440 --> 00:03:55,630
So we're basically encrypting the documents directory that we have in here.

62
00:03:55,630 --> 00:03:57,610
As you can see we have two images.

63
00:03:57,610 --> 00:04:01,780
We have the passwords file that I've already showed you, same one that is in the downloads.

64
00:04:01,780 --> 00:04:05,500
And we also have a file in here that just contain client names.

65
00:04:05,500 --> 00:04:07,570
This is just a sample file as well.

66
00:04:07,570 --> 00:04:12,790
So we're assuming that this is an important directory that contains very important information to the

67
00:04:12,790 --> 00:04:13,390
target.

68
00:04:15,180 --> 00:04:21,000
Next, you have some optional fields where you need to fill in the C2 server, the port if you are going

69
00:04:21,000 --> 00:04:22,530
to exfiltrate the files.

70
00:04:22,530 --> 00:04:25,860
But in here you also have to set the recovery key.

71
00:04:25,980 --> 00:04:31,080
This is the key that's going to be used to encrypt the files so you can put anything you want.

72
00:04:31,080 --> 00:04:33,210
I'm just going to do test test.

73
00:04:33,210 --> 00:04:34,830
And now with that we're happy.

74
00:04:34,830 --> 00:04:36,210
We're going to click submit.

75
00:04:36,660 --> 00:04:40,620
And let's go to the target computer and have a look at what's going to happen.

76
00:04:41,130 --> 00:04:43,230
So as you can see everything went red.

77
00:04:43,230 --> 00:04:46,800
And we got this scary ransomware notification.

78
00:04:46,800 --> 00:04:53,280
So this is great for an actual ransomware simulation because this looks identical to a normal ransomware

79
00:04:53,280 --> 00:04:54,060
attack.

80
00:04:54,060 --> 00:04:57,630
And as you can see, it's telling you that it encrypted your files.

81
00:04:57,630 --> 00:04:59,460
It's telling you that you don't need to worry.

82
00:04:59,460 --> 00:05:02,190
If you pay, you're going to get your files back.

83
00:05:02,190 --> 00:05:07,650
And then if you go ahead and look at the documents, as you can see in here, you can see that all of

84
00:05:07,650 --> 00:05:10,980
the files are encrypted and we're not going to be able to open them.

85
00:05:10,980 --> 00:05:17,310
So even if I, for example, double click the clients file, windows is going to say, I don't know

86
00:05:17,310 --> 00:05:18,480
how to open this file.

87
00:05:18,480 --> 00:05:20,520
We're going to say open it with notepad.

88
00:05:20,520 --> 00:05:26,550
And as you can see you're just going to see gibberish because the file now is encrypted and we do not

89
00:05:26,550 --> 00:05:27,690
have access to it.

90
00:05:28,380 --> 00:05:34,680
So this is great to test your incident response team to see how they would respond to an incident like

91
00:05:34,680 --> 00:05:35,430
this one.

92
00:05:36,060 --> 00:05:41,700
And like I said, as a pentester or a red teamer, you will be asked to simulate such attacks.

93
00:05:41,730 --> 00:05:47,760
Now, there are other tools that allow you to specifically simulate ransomware attacks only, but this

94
00:05:47,760 --> 00:05:51,360
is a really nice feature that we have here embedded within Empire.

95
00:05:52,260 --> 00:05:59,640
Now to undo these changes, and to fix this, you can simply decrypt all of these files using the recovery

96
00:05:59,640 --> 00:06:00,120
key.

97
00:06:00,210 --> 00:06:03,150
You can get that key in here from the tasks.

98
00:06:03,150 --> 00:06:08,130
So if you look at the tasks that you created, most of the time you'll actually find it in here.

99
00:06:08,130 --> 00:06:11,730
But for some reason sometimes you might not find it in here.

100
00:06:11,730 --> 00:06:16,920
And therefore you can actually just go back and you'll have this Readme file inside it.

101
00:06:16,920 --> 00:06:19,440
You will see the recovery key.

102
00:06:19,440 --> 00:06:23,760
So we can copy this key and go back.

103
00:06:25,030 --> 00:06:27,070
Use the same module.

104
00:06:27,100 --> 00:06:28,750
The ransomware module.

105
00:06:30,890 --> 00:06:39,200
And this time, instead of encryption, we're actually going to decrypt the same directory that we encrypted.

106
00:06:39,200 --> 00:06:42,110
So it's C users John.

107
00:06:42,110 --> 00:06:43,010
Documents.

108
00:06:44,560 --> 00:06:48,070
And finally you're going to put the recovery key in here.

109
00:06:48,070 --> 00:06:51,310
Click submit and maybe give it a second.

110
00:06:52,930 --> 00:06:56,200
And you'll see everything is back to the way it was.

111
00:06:56,200 --> 00:07:02,350
And now if we open up the clients file, as you can see, we are able to read its content.

112
00:07:02,920 --> 00:07:09,070
So like I said, there are more ransomware simulators out there that you can use to simulate a ransomware

113
00:07:09,070 --> 00:07:09,820
attack.

114
00:07:09,850 --> 00:07:12,670
This is not really the topic of this course.

115
00:07:12,670 --> 00:07:15,700
We're covering C2 servers that can be used on the cloud.

116
00:07:15,700 --> 00:07:21,280
And the reason why I included this because this is built in within Starkiller and Empire, which is

117
00:07:21,280 --> 00:07:22,720
the C2 that we're covering.

118
00:07:22,720 --> 00:07:27,760
And like I said, it's a very nice, handy feature that it has in there that you can literally launch

119
00:07:27,760 --> 00:07:30,970
and execute with a few clicks, as you saw.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 13: Hacking Windows Using Discord as a C2

1
00:00:00,140 --> 00:00:03,710
In this section we're going to be covering a C2 application.

2
00:00:03,710 --> 00:00:08,390
Like I said, there is a lot of examples of C2 applications in this section.

3
00:00:08,390 --> 00:00:13,280
We're going to be covering an application that is actually developed by Dimitris, which is one of the

4
00:00:13,280 --> 00:00:15,500
members of our team at the security.

5
00:00:15,500 --> 00:00:22,310
And the really cool thing about this program is that it eliminates the need to set up your own server

6
00:00:22,310 --> 00:00:29,060
so it still uses the cloud, but instead of you having to go and install a C2 application on Linode

7
00:00:29,060 --> 00:00:35,840
or Amazon or Blue Ocean or any other cloud provider, it actually uses existing services.

8
00:00:35,840 --> 00:00:38,960
So it uses discord or GitHub or telegram.

9
00:00:38,960 --> 00:00:44,330
And he's planning on adding more of these services as the C2 or as the server.

10
00:00:44,780 --> 00:00:50,990
When the target executes the dropper or the agent, the connection is going to be sent to Discord or

11
00:00:50,990 --> 00:00:57,350
Telegram or GitHub, and you'll be communicating to the target through one of these services, instead

12
00:00:57,350 --> 00:01:00,980
of having to do it through your own server in here.

13
00:01:00,980 --> 00:01:05,000
So it eliminates the need of installing and configuring your own server.

14
00:01:05,000 --> 00:01:08,270
And also it makes the connection more stealthy.

15
00:01:08,270 --> 00:01:14,060
It makes it harder to detect because the traffic looks like a traditional traffic that is generated

16
00:01:14,060 --> 00:01:16,550
by one of these services.

17
00:01:16,550 --> 00:01:19,880
It doesn't look like a traffic that a backdoor would generate.

18
00:01:20,500 --> 00:01:26,650
So let me show you how to install it first, and then I'll teach you how to use it to hack a windows

19
00:01:26,650 --> 00:01:29,290
computer through one of these services.

20
00:01:29,860 --> 00:01:32,830
So first let's download it from their git repository.

21
00:01:32,830 --> 00:01:36,220
I'm going to include its link in the resources of this lecture.

22
00:01:36,220 --> 00:01:42,730
And if you scroll down you'll first of all get some basic information about it, its main features.

23
00:01:42,730 --> 00:01:48,580
And then you'll actually get the installation instructions including the download command, the git

24
00:01:48,580 --> 00:01:49,030
clone.

25
00:01:49,030 --> 00:01:56,650
So all we have to do is just copy this, open up our terminal, and we're going to navigate to the opt

26
00:01:56,650 --> 00:01:58,660
directory using the CD command.

27
00:01:58,660 --> 00:02:01,600
So we're going to do CD forward slash opt.

28
00:02:02,930 --> 00:02:04,640
Opt is short for optional.

29
00:02:04,640 --> 00:02:07,850
So this is where you should be installing optional programs.

30
00:02:07,850 --> 00:02:11,210
And we're just going to paste the command that we just copied.

31
00:02:11,450 --> 00:02:15,950
So this command will basically use git to clone a repository.

32
00:02:15,950 --> 00:02:19,100
And we have the link of the dystopia C2 repository.

33
00:02:19,100 --> 00:02:22,490
So it's basically going to download the code for this program.

34
00:02:22,730 --> 00:02:23,960
I'm going to hit enter.

35
00:02:24,260 --> 00:02:29,510
And now that it's downloaded we can actually see the next command in here where we have to navigate

36
00:02:29,510 --> 00:02:35,510
to the dystopia directory, change the permissions of this setup and then run the setup bash script.

37
00:02:36,050 --> 00:02:37,880
So we're going to go back to the terminal.

38
00:02:37,880 --> 00:02:42,770
If we do ls you'll see that we have the dystopia C2 directory in here.

39
00:02:42,770 --> 00:02:45,290
So we're simply going to CD into it.

40
00:02:45,290 --> 00:02:47,390
Change our working directory into it.

41
00:02:47,390 --> 00:02:53,090
If we list in here you'll see we have the setup dot h bash script.

42
00:02:53,090 --> 00:02:58,310
Right now you can see that it's color is not green meaning that it is not executable.

43
00:02:58,310 --> 00:03:03,080
So we're going to change its permissions to an executable using the chmod command.

44
00:03:03,080 --> 00:03:06,260
We're going to do plus x to make it an executable.

45
00:03:06,260 --> 00:03:09,590
And we're going to give it the file name that we want to make an executable.

46
00:03:09,590 --> 00:03:14,030
And the file name is setup dot ssh I'm going to hit enter.

47
00:03:14,030 --> 00:03:20,510
If we do ls again you'll see setup.sh is green now meaning that it is an executable.

48
00:03:20,510 --> 00:03:26,450
And we can execute executables and Linux by simply doing dot forward slash followed by the file name

49
00:03:26,450 --> 00:03:28,370
which is setup dot h.

50
00:03:28,610 --> 00:03:29,630
We're going to hit enter.

51
00:03:29,630 --> 00:03:36,890
And this should download and install all the packages and dependencies needed by dystopia C2.

52
00:03:36,920 --> 00:03:40,940
So you want to give it some time to download and install all of these dependencies.

53
00:03:41,450 --> 00:03:46,340
During the installation, you're going to get this prompt asking you if it should restart the services

54
00:03:46,340 --> 00:03:47,630
that got upgraded.

55
00:03:47,630 --> 00:03:52,790
We're going to move to the yes using the arrows, and we're going to hit enter to say yes so that the

56
00:03:52,790 --> 00:03:56,660
upgrades take effect or the installed packages will also take effect.

57
00:03:57,350 --> 00:04:03,020
You might also get a window like this one to install Python for windows, because that is needed to

58
00:04:03,020 --> 00:04:08,420
generate the backdoors or the droppers that dystopia C2 generates.

59
00:04:08,450 --> 00:04:14,480
In my case, as you can see, it's asking me if I want to modify or repair the existing installation

60
00:04:14,480 --> 00:04:18,170
because I've already installed Python for windows on this machine.

61
00:04:18,170 --> 00:04:20,660
So in your case, it's going to be a brand new installation.

62
00:04:20,660 --> 00:04:23,000
You're just going to have to click next, next, next next.

63
00:04:23,000 --> 00:04:28,130
In my case I'm just going to click modify just so that I get a similar experience as yours.

64
00:04:28,130 --> 00:04:29,450
Installation is complete.

65
00:04:29,450 --> 00:04:31,070
We're going to click close.

66
00:04:32,550 --> 00:04:33,300
And perfect.

67
00:04:33,300 --> 00:04:35,820
As you can see, it's saying done.

68
00:04:35,820 --> 00:04:37,860
The installation is complete.

69
00:04:37,860 --> 00:04:43,050
So I'm going to clear the screen and we're going to do LZ again.

70
00:04:43,050 --> 00:04:49,140
And basically in the future we're going to be using this program right here, builder.py to generate

71
00:04:49,140 --> 00:04:55,740
the backdoors or the droppers or the agents, which we need the target to execute on their computer

72
00:04:55,740 --> 00:04:57,390
to hack their computer.

73
00:04:57,390 --> 00:04:59,730
So to run this this is written in Python.

74
00:04:59,730 --> 00:05:03,240
So we're going to have to type Python three to run it in Python three.

75
00:05:03,240 --> 00:05:07,650
And we're going to put the file name which is builder.py.

76
00:05:08,850 --> 00:05:14,880
Hit enter, and you're going to be dropped inside of dystopia, where you can use the help command to

77
00:05:14,880 --> 00:05:16,110
learn how to use it.

78
00:05:16,110 --> 00:05:17,790
But don't worry about this.

79
00:05:17,790 --> 00:05:23,310
I will be covering this in details in the future, and you're going to learn how to use it to hack and

80
00:05:23,310 --> 00:05:25,800
remotely control windows computers.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,020 --> 00:00:05,210
In this class, I'm going to show you how to hack windows computers and remotely control them through

2
00:00:05,210 --> 00:00:05,780
discord.

3
00:00:05,810 --> 00:00:11,360
So this method will use completely encrypted communications through discord and will not require port

4
00:00:11,360 --> 00:00:15,890
forwarding or tunneling, as the connection will be facilitated through discord.

5
00:00:15,920 --> 00:00:20,330
If you don't know what discord is, it's simply an instant messaging platform.

6
00:00:20,330 --> 00:00:26,060
We're going to use this platform as our command and control server to control the computers that we

7
00:00:26,090 --> 00:00:26,330
hack.

8
00:00:26,330 --> 00:00:31,880
So instead of having our own server with our own C2 or command and control program, we're going to

9
00:00:31,880 --> 00:00:34,190
use discord as the command and control.

10
00:00:34,190 --> 00:00:39,530
Whenever we hack a computer, the computer is going to send a message to discord telling us that we

11
00:00:39,530 --> 00:00:45,020
have access to this computer, and then if we wanted to execute commands on this computer, well, first

12
00:00:45,020 --> 00:00:46,820
of all, going to send it through discord.

13
00:00:46,820 --> 00:00:50,360
Discord will forward it to our back door running on the target machine.

14
00:00:50,360 --> 00:00:55,460
The result will be returned to discord as a message, and that's how we're going to be able to see it

15
00:00:55,460 --> 00:01:00,770
as the hacker, because we're using discord as our command and control server and everything is going

16
00:01:00,770 --> 00:01:01,460
through discord.

17
00:01:01,460 --> 00:01:03,560
The connection is going to be fully encrypted.

18
00:01:03,560 --> 00:01:09,170
We will not need to use tunneling or port forwarding, because the discord server is already exist on

19
00:01:09,170 --> 00:01:14,600
the cloud, and the commands and the results are going to be sent as normal messages through discord.

20
00:01:14,600 --> 00:01:21,050
An extra benefit is if the traffic is analyzed, it's going to seem identical to normal traffic of a

21
00:01:21,050 --> 00:01:22,700
user chatting to their friend.

22
00:01:22,700 --> 00:01:28,130
Because like I said, discord is an instant messaging application, and when we send messages, even

23
00:01:28,130 --> 00:01:32,810
if we're asking it to execute commands on this computer, and even though the result of the message

24
00:01:32,810 --> 00:01:38,870
is the result of the command execution, it's still part of a normal instant messaging conversation

25
00:01:38,870 --> 00:01:43,010
that looks identical to a normal conversation that happens between friends.

26
00:01:43,310 --> 00:01:49,520
We're going to be focusing on the discord version of dystopia, so dystopia allows us to create telegram

27
00:01:49,520 --> 00:01:52,670
and GitHub backdoors and control them through telegram and GitHub.

28
00:01:52,670 --> 00:01:57,710
But we're focusing on the discord version because it is the one with the most features.

29
00:01:57,710 --> 00:02:01,400
It's got the nicest interface, it's got even a web interface.

30
00:02:01,430 --> 00:02:06,020
It works on all operating systems windows, Linux, smartphones, and so on.

31
00:02:06,020 --> 00:02:11,600
It allows us to execute multiple commands on multiple computers, so effectively can be used as a botnet.

32
00:02:11,600 --> 00:02:13,460
It allows us to access the keyboard.

33
00:02:13,460 --> 00:02:14,720
It's got a keylogger.

34
00:02:14,720 --> 00:02:18,740
It can register all the key strikes on the target computer and send them to you.

35
00:02:18,740 --> 00:02:23,090
This way you'll be able to steal usernames, passwords, or whatever they type on their keyboard.

36
00:02:23,090 --> 00:02:28,130
And it's also got a really cool feature, which is a mass command execution on your botnet.

37
00:02:28,130 --> 00:02:33,050
So if you have a botnet and you're controlling a number of computers at the same time, you can simply

38
00:02:33,050 --> 00:02:38,750
send one command through discord, and that command will be sent to all of the computers that you hacked

39
00:02:38,750 --> 00:02:40,640
and it will be executed on them.

40
00:02:40,640 --> 00:02:43,580
So that's why we're going to be focusing on this backdoor.

41
00:02:43,580 --> 00:02:48,410
But in your own time, you can go ahead and experiment with the telegram and the GitHub backdoors.

42
00:02:48,410 --> 00:02:53,570
So to use a discord agent, first of all we're going to have to go ahead and install discord.

43
00:02:53,570 --> 00:02:58,640
Like I said, the instant messaging app that we're going to use as our command and control server.

44
00:02:58,790 --> 00:03:01,790
You can get it from discord dot com.

45
00:03:01,790 --> 00:03:07,280
There are applications for all operating systems that you can download from the download tab in here.

46
00:03:07,280 --> 00:03:12,650
It also supports all smartphones, so you can install it on Android or Apple mobile devices.

47
00:03:12,650 --> 00:03:16,610
You can even use it from the web by simply clicking on login in here.

48
00:03:16,610 --> 00:03:19,940
Now for me it's saying Open discord because I've already logged in.

49
00:03:19,940 --> 00:03:23,420
And if you don't have an account, you're going to have to click on sign up and sign up.

50
00:03:23,420 --> 00:03:26,720
The sign up process is very simple and it's free, so I'm not going to cover it.

51
00:03:26,720 --> 00:03:30,590
So I'm simply going to click on Open Discord to access my own discord.

52
00:03:30,590 --> 00:03:32,930
So right now it's going to let me access it from the web.

53
00:03:32,930 --> 00:03:36,920
But like I said you can simply download the application and use it from the application.

54
00:03:36,920 --> 00:03:39,350
The usage is exactly the same.

55
00:03:39,350 --> 00:03:44,840
So once you're logged in, you're going to need to create a discord server, which we will need in order

56
00:03:44,840 --> 00:03:48,500
to communicate with our targets or backdoors or agents.

57
00:03:48,500 --> 00:03:52,490
This server is going to need to have special channels or special features.

58
00:03:52,490 --> 00:03:59,480
And that's why they creator of dystopia, Dimitris, created a template that we can use in order to

59
00:03:59,480 --> 00:04:02,150
create this channel or this server.

60
00:04:02,150 --> 00:04:09,230
So you can go to the GitHub repository of dystopia here github.com Ektos dystopia I am at the wiki page

61
00:04:09,230 --> 00:04:12,170
and you simply want to click on this template in here.

62
00:04:12,440 --> 00:04:17,870
And as you can see, it's going to redirect you to discord and it's going to allow us to create a new

63
00:04:17,870 --> 00:04:19,190
server on discord.

64
00:04:19,190 --> 00:04:24,830
Like I said, this server is going to be our channel of communication with the backdoors and the agents

65
00:04:24,830 --> 00:04:28,280
that we are going to use to hack into windows computers.

66
00:04:28,280 --> 00:04:32,900
So it's asking us to choose a server name so we can simply call it dystopia.

67
00:04:32,900 --> 00:04:36,830
You can call it whatever you want, and we're going to simply click on Create Server.

68
00:04:36,830 --> 00:04:40,730
Once you do that, as you can see in here on the left, I have a new server.

69
00:04:40,730 --> 00:04:43,760
If you hover over it, you'll see the name of the server dystopia.

70
00:04:43,760 --> 00:04:49,340
And as you can see, it is completely empty because obviously we haven't hacked any computers yet.

71
00:04:49,340 --> 00:04:53,960
You can also see that we have two channels here on the left, a main channel and a keylogger.

72
00:04:53,990 --> 00:04:58,550
The main channel is where we're going to communicate with the backdoors or the agents that will allow

73
00:04:58,550 --> 00:04:59,630
us to remotely control.

74
00:04:59,950 --> 00:05:05,680
The windows computers, and the keylogger channel is where you're going to see every single strike that

75
00:05:05,680 --> 00:05:07,600
they type on their keyboard in here.

76
00:05:07,600 --> 00:05:11,110
So like I said, this will allow you to steal usernames, passwords and so on.

77
00:05:11,110 --> 00:05:16,390
So so far this is just a normal discord server, just like the security server that we have.

78
00:05:16,390 --> 00:05:21,190
And generally people use this to basically send instant messages between them.

79
00:05:21,190 --> 00:05:27,670
So in the next lecture I'm going to show you how to configure this normal server so that it can be used

80
00:05:27,670 --> 00:05:31,180
as a command and control server to control hacked computers.

81
00:05:31,180 --> 00:05:35,560
So I'm going to show you how to weaponize this server to be used as a C2 server.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:06,470
So, as mentioned before, discord servers allow us to send instant messages and not control computers

2
00:00:06,470 --> 00:00:07,400
on the internet.

3
00:00:07,400 --> 00:00:13,520
So in this lecture, I'm going to show you how to create a custom application or a bot and install it

4
00:00:13,520 --> 00:00:20,960
on our server so that it can be used as a command and control server and control windows computers remotely.

5
00:00:20,960 --> 00:00:25,940
So basically we have a normal discord server right now that we can use to send normal messages.

6
00:00:25,940 --> 00:00:33,680
And once we weaponize it, it's going to become our C2 server that we can use to control other computers.

7
00:00:34,070 --> 00:00:39,050
So in order to do this, we're going to go back to our web browser and we're going to go to discord

8
00:00:39,050 --> 00:00:41,780
Comm Developers applications.

9
00:00:41,780 --> 00:00:45,230
And in here you're going to need to create a new application.

10
00:00:45,230 --> 00:00:48,560
So I'm going to click on New Application here on the top right.

11
00:00:48,560 --> 00:00:50,780
And we're going to give the application a name.

12
00:00:50,780 --> 00:00:53,690
So let's call it Dystopia bot.

13
00:00:53,690 --> 00:00:56,120
We're going to have to agree to the terms and conditions.

14
00:00:56,120 --> 00:00:58,460
And we're simply going to click on create.

15
00:00:58,460 --> 00:01:01,880
And here you can actually customize your bot or application.

16
00:01:01,880 --> 00:01:04,670
You can upload an avatar image if you want to.

17
00:01:04,700 --> 00:01:05,870
You can give a description.

18
00:01:05,870 --> 00:01:07,610
We don't really want to do any of this.

19
00:01:07,640 --> 00:01:13,970
We want to go to the bot, however, and we're going to enable all of the communication privileges that

20
00:01:13,970 --> 00:01:20,900
we have in here so that the bot can effectively communicate properly to the agents or the computers

21
00:01:20,900 --> 00:01:22,820
that we're going to hack in the future.

22
00:01:22,820 --> 00:01:26,120
I'm also going to click here on Reset Access Token.

23
00:01:26,120 --> 00:01:27,560
I'm going to say yes to it.

24
00:01:27,560 --> 00:01:30,170
And that's actually going to give me my access token.

25
00:01:30,170 --> 00:01:31,910
This is very, very important.

26
00:01:31,910 --> 00:01:34,040
It is used to authenticate the bot.

27
00:01:34,070 --> 00:01:39,620
We're going to need to use it in the future in order to allow our backdoors to communicate with this

28
00:01:39,620 --> 00:01:40,370
application.

29
00:01:40,370 --> 00:01:43,220
So I'm going to copy it and we're going to save it somewhere safe.

30
00:01:43,220 --> 00:01:45,770
So I'm just going to open up a text editor.

31
00:01:45,770 --> 00:01:48,320
And I'm going to type my bot token.

32
00:01:48,320 --> 00:01:49,430
Is this.

33
00:01:49,730 --> 00:01:56,630
So now that we created this application or bot we actually need to go ahead and install it on our server.

34
00:01:56,630 --> 00:01:59,180
So right now it's not installed here on the server.

35
00:01:59,180 --> 00:02:01,940
To do that we're going to go on the Oauth2.

36
00:02:01,940 --> 00:02:07,700
We're going to go to the URL generator and we're going to tick the bot checkbox in here.

37
00:02:07,700 --> 00:02:10,700
And we're going to tick the administrator checkbox.

38
00:02:10,700 --> 00:02:15,170
Once we're happy we're going to copy the generated URL in here.

39
00:02:15,170 --> 00:02:18,050
And we're simply going to paste it in the URL bar.

40
00:02:18,530 --> 00:02:22,730
Once you do that, you can see that you're going to get a pop up which will tell you what's going to

41
00:02:22,730 --> 00:02:23,210
happen.

42
00:02:23,210 --> 00:02:29,210
So it's actually telling us that external application called Dystopia Bot, which is the application

43
00:02:29,210 --> 00:02:30,200
that we just created.

44
00:02:30,200 --> 00:02:35,330
And I told you that's what's going to weaponize my server, to control the agents that we're going to

45
00:02:35,330 --> 00:02:41,000
use to hack into windows computers is telling us that this server wants to access my discord account,

46
00:02:41,000 --> 00:02:42,080
and I am okay with that.

47
00:02:42,080 --> 00:02:44,240
It's going to be able to add a bot to this server.

48
00:02:44,240 --> 00:02:50,660
It's going to create commands in the server, and it's asking me which server do I want to add it to?

49
00:02:50,660 --> 00:02:56,330
And I'm selecting the dystopia server because that is the server that we created in the previous lecture.

50
00:02:56,330 --> 00:03:02,300
That is the server that I told you we're going to use in order to control other computers is the server

51
00:03:02,300 --> 00:03:03,290
that we have in here.

52
00:03:03,290 --> 00:03:05,090
As you can see, it's called dystopia.

53
00:03:05,090 --> 00:03:10,850
And like I said right now, the server is a normal server that can only be used for instant messaging.

54
00:03:10,850 --> 00:03:16,790
But once we go in here and we add this bot to it and we're going to authorize it as an admin, it's

55
00:03:16,790 --> 00:03:22,430
going to weaponize that server for me, and it's going to configure it so that it can be used as a command

56
00:03:22,430 --> 00:03:28,520
and control server or a C2 server, which will allow me to control windows computers that I'm going

57
00:03:28,520 --> 00:03:29,960
to hack in the next lecture.

58
00:03:29,960 --> 00:03:33,020
Now it's asking me to confirm that I am a human, just a captcha.

59
00:03:33,020 --> 00:03:36,080
So we're just going to tick that and actually got me no problem.

60
00:03:36,080 --> 00:03:41,630
We're going to click on go to dystopia, and it's simply just going to drop me back into the dystopia

61
00:03:41,630 --> 00:03:43,490
server that we just created.

62
00:03:43,490 --> 00:03:49,640
And if we go to the main channel now, you'll see that we have a new account, join the server, and

63
00:03:49,640 --> 00:03:55,430
it's called Dystopia Bot, which is the application that we created at the start of this lecture.

64
00:03:55,670 --> 00:04:01,430
So now our server has the bot, and this bot will allow us to communicate with the backdoor that we're

65
00:04:01,430 --> 00:04:03,020
going to generate in the next step.

66
00:04:03,020 --> 00:04:09,470
So that will allow us to basically control any computer that that backdoor gets executed on through

67
00:04:09,470 --> 00:04:11,390
this discord server in here.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:06,980
So now that we weaponized our discord server and we configured to control other computers, the next

2
00:00:06,980 --> 00:00:13,040
stage is to go ahead and create the actual backdoor that we're going to install on the target computer,

3
00:00:13,040 --> 00:00:16,700
so that we can control it through our discord bot.

4
00:00:16,880 --> 00:00:21,320
To do that, we're going to go ahead to Kali and we're going to run the builder in dystopia.

5
00:00:21,320 --> 00:00:27,260
So I've already downloaded and installed dystopia here, and to run it I'm simply going to do Python

6
00:00:27,260 --> 00:00:29,990
three builder dot Pi.

7
00:00:30,800 --> 00:00:35,300
We're going to say use discord because that's the back door that we want to use.

8
00:00:35,300 --> 00:00:39,470
And as you can see, we get the names of all of the options that we need to set.

9
00:00:39,470 --> 00:00:43,550
And if we do help set, you'll see the actual names that you need to set.

10
00:00:43,550 --> 00:00:46,820
So you can see that the first thing that we need to set is the name.

11
00:00:46,820 --> 00:00:49,940
So we're going to simply do set name.

12
00:00:49,940 --> 00:00:51,590
Dystopia.

13
00:00:51,800 --> 00:00:52,730
Discord.

14
00:00:53,350 --> 00:01:00,790
Next you need to set the guild ID and you can see the description of the guild ID it's the ID of the

15
00:01:00,790 --> 00:01:01,930
discord server.

16
00:01:02,260 --> 00:01:07,570
To get that, we're going to have to go back to our server, and we actually have to go to the settings

17
00:01:07,570 --> 00:01:08,860
of our account.

18
00:01:08,860 --> 00:01:11,680
And we need to go to the advanced right here.

19
00:01:11,680 --> 00:01:14,200
And you need to turn on developer mode.

20
00:01:14,200 --> 00:01:16,600
So as you can see, for me it's already turned on.

21
00:01:16,600 --> 00:01:18,910
If it's all for you, make sure you turn it on.

22
00:01:18,910 --> 00:01:21,670
And once it's on, you're going to come back in here.

23
00:01:21,670 --> 00:01:25,660
Right click the server and we're going to copy the server ID.

24
00:01:25,780 --> 00:01:28,420
So that's basically the guild ID.

25
00:01:28,420 --> 00:01:31,660
So we're going to do set guild ID to this.

26
00:01:32,500 --> 00:01:35,650
And the next thing that we need to set is the bot token.

27
00:01:35,950 --> 00:01:41,860
The bot token is the token of the discord bot, and we copy that and saved it in a text file before.

28
00:01:41,860 --> 00:01:44,770
So I have it right here, I'm going to copy it.

29
00:01:44,770 --> 00:01:48,850
And we're going to set the bot token to the token.

30
00:01:49,560 --> 00:01:56,070
Next we need to set the channel ID and this is the ID of the main discord channel.

31
00:01:56,070 --> 00:02:01,380
So if we go back in here we have the main channel in here right click copy the channel ID.

32
00:02:01,380 --> 00:02:05,430
And again we're going to set the channel ID to this.

33
00:02:06,310 --> 00:02:09,070
And finally you need to set the webhook.

34
00:02:09,070 --> 00:02:11,380
So this is the webhook for the keylogger.

35
00:02:11,380 --> 00:02:14,770
To get that we're going to go to the server settings.

36
00:02:14,770 --> 00:02:17,770
Right click the server, go to its settings.

37
00:02:17,860 --> 00:02:19,900
We're going to go to integrations.

38
00:02:19,900 --> 00:02:22,360
And we're going to create a webhook.

39
00:02:22,360 --> 00:02:24,040
Click this new webhook.

40
00:02:24,070 --> 00:02:27,580
You can call it anything you want keylogger webhook.

41
00:02:27,820 --> 00:02:32,500
And we're going to set it to the keylogger channel because that's going to be used for the keylogger.

42
00:02:32,500 --> 00:02:38,500
And basically this is needed to tell the backdoor which channel to send the key logs that it's going

43
00:02:38,500 --> 00:02:40,690
to register on the target computer.

44
00:02:40,690 --> 00:02:44,710
So we're going to save the changes and we're going to copy the webhook URL.

45
00:02:44,710 --> 00:02:46,000
Go to our backdoor.

46
00:02:46,000 --> 00:02:50,200
And we're going to set the webhook to the URL that we just copied.

47
00:02:50,200 --> 00:02:55,900
Basically once it's saved in the backdoor, the backdoor now knows whenever it registers key strikes

48
00:02:55,900 --> 00:02:59,260
on the target computer, it's going to send them to this URL.

49
00:02:59,260 --> 00:03:05,500
And this URL has been configured to display these key strikes in the keylogger channel that we have

50
00:03:05,500 --> 00:03:06,280
in here.

51
00:03:07,060 --> 00:03:08,920
So now we've set all of the settings.

52
00:03:08,920 --> 00:03:14,680
I can just run config to display the settings that I set and make sure that they are correct.

53
00:03:14,680 --> 00:03:17,890
So you can go ahead and double check that you did everything properly.

54
00:03:17,890 --> 00:03:20,800
So once you're happy, you can run build.

55
00:03:20,800 --> 00:03:24,820
In order to build this backdoor it's going to ask you, do you really want to do this?

56
00:03:24,820 --> 00:03:26,500
I'm going to say why yes.

57
00:03:26,500 --> 00:03:31,240
And hit enter and you want to give it a minute or so in order to build the backdoor for you.

58
00:03:31,240 --> 00:03:37,510
So as you can see that the backdoor is built successfully and it's stored in a directory called dist.

59
00:03:37,510 --> 00:03:39,100
So I'm going to clear my screen.

60
00:03:39,100 --> 00:03:45,190
And if we lose what's in the disk directory you'll see that we have it in here dystopia discord dot

61
00:03:45,190 --> 00:03:45,700
exe.

62
00:03:45,850 --> 00:03:51,940
And as usual you'd want to be able to use a method of social engineering or some kind of a smart delivery

63
00:03:51,940 --> 00:03:52,330
method.

64
00:03:52,330 --> 00:03:56,320
We cover a lot of these in the social engineering course and in my other courses.

65
00:03:56,320 --> 00:03:58,000
That's not the goal of this lecture.

66
00:03:58,000 --> 00:04:04,540
So I'm simply going to copy this backdoor to the local web server that I have on this machine and download

67
00:04:04,540 --> 00:04:07,900
it on the target machine, because the goal is simply to test the backdoor.

68
00:04:07,900 --> 00:04:13,540
We're not really learning any new delivery methods, and you want to make sure guys that you run this

69
00:04:13,540 --> 00:04:20,170
backdoor on a real computer, not on a virtual machine, because this backdoor has virtual machine detection.

70
00:04:20,170 --> 00:04:27,010
So it actually will not run on virtual machines on purpose to improve its stealth capabilities.

71
00:04:27,010 --> 00:04:30,250
Now that the backdoor is downloaded, I'm simply going to run it.

72
00:04:30,820 --> 00:04:33,010
You're going to get this blue windows screen.

73
00:04:33,010 --> 00:04:39,850
You get this with any executable with an unknown publisher, even if the executable was not malicious.

74
00:04:39,850 --> 00:04:41,950
So this is nothing to do with this backdoor.

75
00:04:42,040 --> 00:04:44,440
We're simply going to click run anyway.

76
00:04:44,440 --> 00:04:49,450
And even when you click run, the backdoor is not going to run properly because it's going to want to

77
00:04:49,450 --> 00:04:51,760
make sure that this is not a virtual machine.

78
00:04:51,760 --> 00:04:57,880
So you're going to have to click a few clicks, maybe move the window, and sometimes you want to give

79
00:04:57,880 --> 00:05:01,900
it a bit of time, a bit of a delay until you get the connection back.

80
00:05:01,900 --> 00:05:06,760
So I've actually clicked a little bit over ten clicks, because I think the default value might be set

81
00:05:06,760 --> 00:05:07,840
to ten clicks.

82
00:05:08,380 --> 00:05:14,020
As you can see in our discord server, the one that we call dystopia, we have a message.

83
00:05:14,020 --> 00:05:17,860
This is very important so that you actually understand how this is working properly.

84
00:05:17,860 --> 00:05:20,350
The message is coming from the dystopia bot.

85
00:05:20,350 --> 00:05:27,280
So it's the application or the bot that we created in the previous lecture, and that bot is basically

86
00:05:27,280 --> 00:05:29,680
telling us that we have an agent online.

87
00:05:29,680 --> 00:05:36,220
It's given us the time that this is happening at, and it gives us information about the target computer.

88
00:05:36,220 --> 00:05:42,970
So we have its IP, we have the architecture, we have the hostname of the computer, we have the operating

89
00:05:42,970 --> 00:05:46,240
system, we have the username, we have the CPU.

90
00:05:46,240 --> 00:05:51,940
And you got information if it's admin, if it's a VM and if the keylogger is running basically right

91
00:05:51,940 --> 00:05:57,670
now, we can remotely control this computer from this simple discord server.

92
00:05:57,670 --> 00:06:04,600
And the really, really cool thing about that is that this server is always online and will always be

93
00:06:04,600 --> 00:06:10,990
connected to the internet, so my computer could be completely off, but whenever the target computer

94
00:06:10,990 --> 00:06:17,080
runs my backdoor, it will communicate with my server and I will be able to come back whenever I want.

95
00:06:17,080 --> 00:06:23,350
Simply access this discord server from my phone, from my laptop, from the web, from their application.

96
00:06:23,350 --> 00:06:29,860
It doesn't really matter and I will be able to control my target hacked computer just to get a taste

97
00:06:29,860 --> 00:06:30,790
of what we can do.

98
00:06:30,820 --> 00:06:34,060
We will cover how to use the backdoor in a future class.

99
00:06:34,060 --> 00:06:39,850
So for now, if we just do help, you will see all of the commands that we can execute on the target

100
00:06:39,850 --> 00:06:45,970
server so you can simply interact with it, execute system commands, get picture of their camera,

101
00:06:45,970 --> 00:06:47,110
you can upload files.

102
00:06:47,110 --> 00:06:48,340
You can get the processes.

103
00:06:48,340 --> 00:06:49,960
You can access the file system.

104
00:06:49,960 --> 00:06:54,970
You can do anything that the target person can do on their computer.

105
00:06:54,970 --> 00:07:00,820
And a really, really cool interaction feature that we have with this discord server is if we do an

106
00:07:00,820 --> 00:07:07,150
escalation mark, an LZ, it will list all of the agents that I have access to.

107
00:07:07,150 --> 00:07:13,330
And as you can see, I can actually carry out quick actions by simply clicking on the buttons that I

108
00:07:13,330 --> 00:07:14,080
have in here.

109
00:07:14,080 --> 00:07:20,620
And like I said, all of this traffic looks like a normal traffic of a friend speaking to a friend.

110
00:07:20,620 --> 00:07:23,470
Because I'm sending the command to discord.

111
00:07:23,470 --> 00:07:25,360
Discord is sending it to the back door.

112
00:07:25,390 --> 00:07:29,230
The back door executes the command and sends the result as a normal message.

113
00:07:29,230 --> 00:07:35,140
So the traffic here looks identical to a traffic of two friends speaking to each other, and everything

114
00:07:35,140 --> 00:07:39,040
is encrypted and it doesn't require port forwarding or tunneling.

115
00:07:39,040 --> 00:07:44,260
I know I'm repeating myself at this stage, but these are very, very useful features that if you want

116
00:07:44,260 --> 00:07:46,450
to have, you usually need to run your own server.

117
00:07:46,450 --> 00:07:51,940
But in this case, you don't need to do that because we are relying on discord's infrastructure.

118
00:07:51,940 --> 00:07:58,180
And like I said, in the future we can spend a full class showing you how to control multiple computers

119
00:07:58,180 --> 00:08:04,630
through this, how to access the saved passwords, how to run the same command on multiple computers,

120
00:08:04,630 --> 00:08:05,950
get their location.

121
00:08:06,360 --> 00:08:07,080
And so on.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 14: Windows Post Exploitation via Discord

1
00:00:00,050 --> 00:00:06,590
So now that you know how to use dystopia to gain access to windows computers or hack them in this class,

2
00:00:06,590 --> 00:00:09,230
we're going to focus on post exploitation.

3
00:00:09,230 --> 00:00:15,710
So we're going to focus on what can we do once we get access or hack these windows computers.

4
00:00:15,710 --> 00:00:20,690
So you're going to see how we can execute system commands on the target computer.

5
00:00:20,690 --> 00:00:24,320
And that basically allow us to do anything that the target person can do.

6
00:00:24,320 --> 00:00:29,390
Because the command prompt is so powerful, will also be able to access the file system.

7
00:00:29,390 --> 00:00:34,070
So we'll be able to access the files, read them, delete them, upload and download files to the hacked

8
00:00:34,070 --> 00:00:34,790
system.

9
00:00:34,790 --> 00:00:38,360
You're going to be able to access the resources of the target system.

10
00:00:38,360 --> 00:00:40,730
So we'll be able to see what they type on their keyboard.

11
00:00:40,730 --> 00:00:44,150
We'll be able to access their camera or even record their microphone.

12
00:00:44,150 --> 00:00:47,030
And finally, we're going to have a look at some built in functions.

13
00:00:47,030 --> 00:00:52,130
So every C2 software or backdoor comes in with certain built in functions.

14
00:00:52,130 --> 00:00:58,880
For example, dystopia currently allow us to steal saved passwords from Chrome, get the location of

15
00:00:58,880 --> 00:01:01,580
the hacked computers, access the microphone.

16
00:01:01,580 --> 00:01:07,010
I already mentioned that making your access persistent so that you can maintain it even if they restart

17
00:01:07,010 --> 00:01:09,050
their computer, and much more.

18
00:01:09,050 --> 00:01:14,450
And I'm sure that Dimitri's the Creator would be adding more features to the built in functions.

19
00:01:14,450 --> 00:01:20,120
And we're also going to have a look at how to execute the same command on multiple computers that we

20
00:01:20,150 --> 00:01:23,840
hacked, effectively allowing us to control a botnet.

21
00:01:24,200 --> 00:01:28,010
We're going to be focusing on the discord version of dystopia.

22
00:01:28,010 --> 00:01:32,990
So as you know, dystopia allows us to create telegram and GitHub backdoors and control them through

23
00:01:32,990 --> 00:01:34,040
telegram and GitHub.

24
00:01:34,040 --> 00:01:39,080
But we're focusing on the discord version because it is the one with the most features.

25
00:01:39,080 --> 00:01:42,770
It's got the nicest interface, it's got even a web interface.

26
00:01:42,800 --> 00:01:47,360
It works on all operating systems windows, Linux, smartphones, and so on.

27
00:01:47,360 --> 00:01:52,400
It allows us to execute multiple commands on multiple computers, as you saw so effectively can be used

28
00:01:52,400 --> 00:01:53,420
as a botnet.

29
00:01:53,420 --> 00:01:55,250
It allows us to access the keyboard.

30
00:01:55,250 --> 00:02:01,040
It's a keylogger, and it allows us to execute multiple commands on the hacked computers on the botnet.

31
00:02:01,040 --> 00:02:04,010
So that's why we're going to be focusing on this backdoor.

32
00:02:04,010 --> 00:02:08,750
But in your own time, you can go ahead and experiment with the telegram and the GitHub backdoors.

33
00:02:08,750 --> 00:02:10,940
And what we're going to do is going to be similar.

34
00:02:10,940 --> 00:02:15,770
If you understand the tier, you should be able to do it through the other backdoor versions.

35
00:02:16,590 --> 00:02:22,950
So first let's have a look at the general commands before even interacting with a specific agent.

36
00:02:23,250 --> 00:02:29,610
So right here I have my discord and I am inside the server that we created previously.

37
00:02:29,610 --> 00:02:32,970
The server that we use to communicate with our back doors.

38
00:02:32,970 --> 00:02:37,440
I'm inside the main channel because that's the main channel that we interact with back doors through

39
00:02:37,440 --> 00:02:39,900
and in here where we execute the commands.

40
00:02:39,900 --> 00:02:46,500
If I do escalation Mark ls, it will list the computers that I have gained access to.

41
00:02:46,500 --> 00:02:49,200
So these are the computers that I have hacked.

42
00:02:49,200 --> 00:02:52,080
And as you can see I have two computers in here.

43
00:02:52,080 --> 00:02:54,960
We can see that both of them saying Windows 10.

44
00:02:54,960 --> 00:02:57,450
Now one of them is actually Windows 11, this computer.

45
00:02:57,450 --> 00:02:59,310
But it shows up as Windows 10.

46
00:02:59,310 --> 00:03:03,510
You can see the IPS of the computers and you can see the username.

47
00:03:03,510 --> 00:03:06,450
So this one is John and this one is Ektos.

48
00:03:06,690 --> 00:03:10,800
Now as you can see through this simple list, we can actually do so much.

49
00:03:10,800 --> 00:03:18,300
So we can click on any of these buttons to execute commands or operations on this specific computer.

50
00:03:18,690 --> 00:03:24,840
For example, I can get the location of this computer Jones computer by simply clicking on location

51
00:03:24,840 --> 00:03:25,440
in here.

52
00:03:26,510 --> 00:03:32,780
Now, as you can see, we get the location and Waterford in Ireland and we can even get the internet

53
00:03:32,780 --> 00:03:33,980
service provider.

54
00:03:34,130 --> 00:03:39,530
This is actually my own computer that I have right here, so that location is correct.

55
00:03:40,550 --> 00:03:43,370
We can also do it to the other computer in here.

56
00:03:43,370 --> 00:03:44,960
This is the matrices computer.

57
00:03:44,960 --> 00:03:46,670
So it's in Netherlands.

58
00:03:46,670 --> 00:03:50,930
And if we click on the location we get another message in here.

59
00:03:50,930 --> 00:03:51,920
And perfect.

60
00:03:51,920 --> 00:03:54,410
As you can see we have the location in Netherlands.

61
00:03:54,410 --> 00:03:57,290
And again we get the internet service provider.

62
00:03:57,590 --> 00:04:03,050
I can also see the running processes by simply clicking on processes again on my own computer.

63
00:04:03,050 --> 00:04:06,470
And we'll get the processes as a message here at the bottom.

64
00:04:06,920 --> 00:04:12,830
Last but not least, we can even get the stored passwords on the Chrome browser by simply clicking on

65
00:04:12,830 --> 00:04:13,880
creds in here.

66
00:04:13,880 --> 00:04:18,770
But before I do that, let me just show you an example of saving the password.

67
00:04:18,770 --> 00:04:23,120
So I'm just going to go to Chrome and let's just go to facebook.com.

68
00:04:24,350 --> 00:04:33,620
And let's just put a test user name test user at gmail.com and put the password 123123ABC.

69
00:04:33,770 --> 00:04:34,700
Doesn't really matter.

70
00:04:34,700 --> 00:04:35,720
I'm going to log in.

71
00:04:35,720 --> 00:04:37,580
Now this is not an actual account.

72
00:04:37,580 --> 00:04:39,290
So the login is going to fail.

73
00:04:39,650 --> 00:04:42,140
And we're actually just going to store the password.

74
00:04:42,140 --> 00:04:46,970
So you always get this pop up when you put the username and the password Chrome asking you if you want

75
00:04:46,970 --> 00:04:47,600
to save it.

76
00:04:47,600 --> 00:04:50,150
If you do go ahead and save this password.

77
00:04:50,570 --> 00:04:54,980
You're going to be able to get it in here by simply clicking on the creds.

78
00:04:54,980 --> 00:04:56,960
So I'm just going to click the creds.

79
00:04:56,990 --> 00:04:58,370
Give it a minute.

80
00:04:58,370 --> 00:04:59,360
And perfect.

81
00:04:59,360 --> 00:05:02,000
As you can see we got the creds in here.

82
00:05:02,000 --> 00:05:06,230
So we have a username that is test user at gmail.com.

83
00:05:06,230 --> 00:05:07,790
And this is their password.

84
00:05:08,180 --> 00:05:10,490
We can expand it by simply clicking here.

85
00:05:10,490 --> 00:05:13,730
Or we can even download it by clicking on the download button.

86
00:05:14,150 --> 00:05:17,870
So these are very basic commands but they're actually very useful.

87
00:05:17,870 --> 00:05:23,060
And the nice thing in here about the discord bot is as we mentioned, we can simply just click on these

88
00:05:23,060 --> 00:05:25,820
buttons to execute these useful commands.

89
00:05:26,480 --> 00:05:32,990
The really cool thing about these commands, as you can see, the responses are coming back as messages.

90
00:05:32,990 --> 00:05:36,650
So I actually mentioned this before when we started speaking about this backdoor.

91
00:05:36,650 --> 00:05:39,200
But I'm repeating it because it's very, very important.

92
00:05:39,200 --> 00:05:46,790
The interaction between me and the backdoor looks identical to an interaction that happens between two

93
00:05:46,790 --> 00:05:52,730
friends that are chatting together using discord, because all we're doing right here is sending messages.

94
00:05:52,730 --> 00:05:58,820
So when I click a button, I'm basically sending a message to the backdoor as a discord message, and

95
00:05:58,820 --> 00:06:04,160
then the backdoor executes whatever I want and returns the response again as a discord message.

96
00:06:04,160 --> 00:06:07,850
So all we're doing is simply sending and receiving messages through discord.

97
00:06:07,850 --> 00:06:12,170
So that's why dystopias agents are considered to be pretty stealth.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:07,280
So now that we had a quick look at the basic commands that we can execute with dystopia using the simple

2
00:00:07,280 --> 00:00:12,950
buttons that you get and this lecture, we're going to talk about executing actual system commands on

3
00:00:12,950 --> 00:00:13,580
the target.

4
00:00:13,580 --> 00:00:17,390
And we're going to learn how to interact with multiple targets at the same time.

5
00:00:17,900 --> 00:00:22,790
So right here I've already executed LZ to see the computers that I have control over.

6
00:00:22,790 --> 00:00:24,590
And I have the same two computers.

7
00:00:24,590 --> 00:00:29,000
And if I wanted to interact with a specific computer only.

8
00:00:29,000 --> 00:00:34,190
So if I want to run commands in here and only run them against a specific computer, all you have to

9
00:00:34,190 --> 00:00:36,020
do is click interact.

10
00:00:36,530 --> 00:00:38,780
So I click the join computer.

11
00:00:38,780 --> 00:00:45,320
And right now, as you can see, I am interacting with agent 457 which is this agent right here controlling

12
00:00:45,320 --> 00:00:46,370
Jones computer.

13
00:00:46,370 --> 00:00:49,910
And right now I'll be able to execute commands in here.

14
00:00:49,910 --> 00:00:53,750
And everything that I execute will only run on Jones computer.

15
00:00:53,750 --> 00:00:58,400
It will not run on the other computer that I have because I clicked on interact in here.

16
00:00:58,730 --> 00:01:01,970
Now to get a list of all of the commands that we can execute here.

17
00:01:01,970 --> 00:01:07,790
We can do forward slash help, and you'll get a list of all of the commands that you can execute on

18
00:01:07,790 --> 00:01:11,990
this computer, along with a description of what this command does.

19
00:01:11,990 --> 00:01:17,210
Now, as you can see, there are commands to navigate to get the processes to take a picture of the

20
00:01:17,210 --> 00:01:17,840
webcam.

21
00:01:17,840 --> 00:01:19,790
And we'll go through a lot of these later on.

22
00:01:19,790 --> 00:01:24,230
But this is a really good way to see what you can do through this backdoor, because I'm not going to

23
00:01:24,230 --> 00:01:25,730
be able to cover everything.

24
00:01:26,400 --> 00:01:31,680
Now, as I mentioned, right now we're inside John's computer and we can only execute commands on John's

25
00:01:31,680 --> 00:01:32,310
computer.

26
00:01:32,790 --> 00:01:41,220
So let's say I wanted to use the forward slash cmd to run a system command on the target computer on

27
00:01:41,220 --> 00:01:42,120
John's computer.

28
00:01:42,120 --> 00:01:47,940
So all I have to do is forward slash cmd followed by the command that I want to execute.

29
00:01:47,940 --> 00:01:54,720
And let's execute a very simple command called who am I to just tell me what user am I logged in at?

30
00:01:55,050 --> 00:01:56,460
And if I hit enter?

31
00:01:56,460 --> 00:02:01,320
As you can see, it's telling me I'm logged in to this computer and my user name is John.

32
00:02:01,410 --> 00:02:03,540
Now let's say you're inside John's computer.

33
00:02:03,540 --> 00:02:04,890
You did what you wanted to do.

34
00:02:04,920 --> 00:02:07,950
You executed the commands that you wanted to do and you're done.

35
00:02:07,950 --> 00:02:12,270
You want to go back and go into the next computer Ekta's computer.

36
00:02:12,270 --> 00:02:19,110
To do that, you simply have to do forward slash background, and that will basically background your

37
00:02:19,110 --> 00:02:21,570
session, bringing us back to where we were.

38
00:02:21,570 --> 00:02:27,360
So we can do forward slash LS again to list all of the computers that we have access to.

39
00:02:27,360 --> 00:02:34,230
And now if I wanted to execute a command on Ec2's computer again I can simply click on interact here.

40
00:02:34,230 --> 00:02:36,750
And I'm inside Ec2's computer.

41
00:02:36,750 --> 00:02:38,880
And let's execute the exact same command.

42
00:02:38,880 --> 00:02:45,450
Just for argument's sake, I'm going to do forward slash cmd and put the command who am I just to see

43
00:02:45,450 --> 00:02:47,250
what user I'm logged in as.

44
00:02:47,250 --> 00:02:48,690
And if I hit enter.

45
00:02:48,690 --> 00:02:54,030
As you can see, I'm logged in to this computer and I'm executing commands as Iquitos.

46
00:02:54,750 --> 00:02:59,910
Again, let's say I use this and I executed as many commands as I wanted and I'm done with it.

47
00:02:59,910 --> 00:03:04,560
If I wanted to exit forward slash background, that will take me out.

48
00:03:04,560 --> 00:03:11,040
And I am back at the main channel, let's say, where we can list our backdoors and interact with them.

49
00:03:11,680 --> 00:03:16,150
Now, this obviously looks very simple when we only have two computers or two agents, but when you

50
00:03:16,150 --> 00:03:21,040
have multiple agents, you want to be comfortable with getting in and out and executing different commands

51
00:03:21,040 --> 00:03:22,420
through these agents.

52
00:03:22,960 --> 00:03:28,090
Now, let's say you wanted to execute a command on all of the agents that you have.

53
00:03:28,090 --> 00:03:31,720
So let's say that you wanted to execute the same command that we spoke about.

54
00:03:31,720 --> 00:03:32,290
Who am I?

55
00:03:32,290 --> 00:03:36,460
And you wanted to see the username that you have on all of the computers that you hacked.

56
00:03:36,490 --> 00:03:39,250
To do that, we are outside of any of them.

57
00:03:39,250 --> 00:03:41,080
We're not interacting with any of them.

58
00:03:41,080 --> 00:03:44,770
We're simply going to do forward slash cmd all.

59
00:03:44,770 --> 00:03:48,040
So that means we want to execute the command on all of the agents.

60
00:03:48,040 --> 00:03:51,460
And the command that we want to execute is who am I?

61
00:03:51,460 --> 00:03:56,410
Again, if I hit enter, I'll get the response from the two computers that I've hacked and I have access

62
00:03:56,410 --> 00:04:00,520
to given me the computer names and their usernames.

63
00:04:01,060 --> 00:04:06,520
Now last but not least, you might not want to do cmd followed by the command that you want to run.

64
00:04:06,520 --> 00:04:08,260
Every time you want to run a command.

65
00:04:08,260 --> 00:04:13,990
Let's say you actually want to get a shell and interactive shell where you write the command and you

66
00:04:13,990 --> 00:04:16,030
get the response straight away on the shell.

67
00:04:16,030 --> 00:04:17,020
Well, you can do that.

68
00:04:17,020 --> 00:04:20,560
And it's also very, very easy in here in dystopia.

69
00:04:20,680 --> 00:04:26,200
First of all, we're going to have to open up our terminal to listen up for incoming connections, because

70
00:04:26,200 --> 00:04:32,230
what we're going to do is we're going to send a connection from the back door directly to my computer.

71
00:04:32,230 --> 00:04:34,360
So we're not going to be using discord anymore.

72
00:04:34,360 --> 00:04:39,700
We're going to get the discord agent to actually send us a connection back to our computer so that we

73
00:04:39,700 --> 00:04:41,680
can have an interactive shell.

74
00:04:41,680 --> 00:04:44,020
So we're going to go to our terminal first.

75
00:04:44,020 --> 00:04:47,410
And in here we're going to listen for incoming connections.

76
00:04:47,530 --> 00:04:50,770
And we're going to use a tool called netcat to do that.

77
00:04:50,770 --> 00:04:57,040
So we're going to do NC which is the name of the tool dash L to listen for incoming connections.

78
00:04:57,400 --> 00:04:59,470
And we're going to give it the port dash P.

79
00:04:59,470 --> 00:05:02,980
And the port that I want to listen on is 4444.

80
00:05:03,800 --> 00:05:05,600
So very very simple command.

81
00:05:05,600 --> 00:05:07,520
We're using a tool called netcat.

82
00:05:07,520 --> 00:05:08,930
Its command is NC.

83
00:05:08,960 --> 00:05:12,320
We're telling it that we want to listen for incoming connections.

84
00:05:12,320 --> 00:05:16,100
The port that we want to listen on is port 444, four.

85
00:05:16,460 --> 00:05:17,840
I'm going to hit enter.

86
00:05:17,930 --> 00:05:21,080
And now this computer is listening for incoming connections.

87
00:05:21,080 --> 00:05:24,680
So now we're going to go back to dystopia.

88
00:05:24,680 --> 00:05:31,250
And we're going to instruct it to send a reverse shell access to netcat in here.

89
00:05:31,880 --> 00:05:35,150
So we're going to actually have to get our IP.

90
00:05:35,150 --> 00:05:37,850
I'm just going to open up a new window to get the IP.

91
00:05:37,850 --> 00:05:41,540
And these commands are the same in Linux and in Apple Mac OS.

92
00:05:42,110 --> 00:05:44,510
So I'm just going to open up a new terminal window.

93
00:05:44,510 --> 00:05:48,410
And I'm going to do ifconfig to get the IP of my computer.

94
00:05:49,680 --> 00:05:53,940
And if we scroll up, we have my IP in here.

95
00:05:53,940 --> 00:05:56,580
1921680 12.

96
00:05:56,760 --> 00:05:59,430
So we're going to go to dystopia.

97
00:05:59,430 --> 00:06:02,760
We're going to interact with the backdoor that we want to use.

98
00:06:02,760 --> 00:06:05,520
So I want to use the backdoor on John's computer.

99
00:06:05,640 --> 00:06:06,150
Perfect.

100
00:06:06,150 --> 00:06:07,410
We're inside it now.

101
00:06:07,410 --> 00:06:12,210
And what we want to do now is forward slash rev shell.

102
00:06:12,210 --> 00:06:15,660
And you can see that the command in here is automatically telling you what it needs.

103
00:06:15,660 --> 00:06:18,210
So it wants an IP and it wants a port.

104
00:06:18,210 --> 00:06:20,010
Now we've already copied the IP.

105
00:06:20,010 --> 00:06:21,450
So I'm going to paste it.

106
00:06:21,450 --> 00:06:24,630
And the port is 4444.

107
00:06:24,660 --> 00:06:26,790
It's the port that we used in here.

108
00:06:26,790 --> 00:06:28,590
And our netcat command.

109
00:06:29,520 --> 00:06:31,260
So we're going to hit enter.

110
00:06:31,290 --> 00:06:35,880
It's telling us that it's attempting to establish a reverse shell on this agent.

111
00:06:35,880 --> 00:06:37,830
So let's go ahead and see if we got it.

112
00:06:37,830 --> 00:06:38,640
And perfect.

113
00:06:38,640 --> 00:06:45,690
As you can see we have a windows command prompt in here on John's computer and the downloads directory

114
00:06:45,690 --> 00:06:47,430
because that's where the backdoor is.

115
00:06:47,430 --> 00:06:53,700
And in here now we can execute system command straight away and get the results in here directly without

116
00:06:53,700 --> 00:07:00,150
having to do the forward slash cmd and doing it through discord so we can do who am I if I can spell

117
00:07:00,150 --> 00:07:07,140
it properly and we get the desktop name and the user name, we can do dare to list directories.

118
00:07:07,140 --> 00:07:08,820
And we have the directories in here.

119
00:07:08,820 --> 00:07:13,110
And you can execute any system command now directly through this.

120
00:07:13,110 --> 00:07:15,630
And you'll see the result again directly in here.

121
00:07:15,630 --> 00:07:18,930
Instead of it coming as a discord message in here.

122
00:07:19,260 --> 00:07:24,870
Now the discord method is better and it's more stealth because because you're not communicating with

123
00:07:24,870 --> 00:07:28,020
the backdoor directly, you're actually sending it as discord messages.

124
00:07:28,020 --> 00:07:29,370
As we said earlier.

125
00:07:29,370 --> 00:07:33,840
But if you ever wanted to execute commands this way, then you have the option.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,050 --> 00:00:03,920
Okay, so now we're getting better at using the dystopia backdoors.

2
00:00:03,920 --> 00:00:09,080
We know how to use the buttons and the quick commands, and we also learned how to interact with different

3
00:00:09,080 --> 00:00:14,690
agents and background them, and even get an interactive reverse shell through it.

4
00:00:14,690 --> 00:00:18,260
In this lecture, I'm going to cover how to access the file system.

5
00:00:18,260 --> 00:00:22,970
So how to navigate within the file system, maybe read files, delete them, upload and download.

6
00:00:22,970 --> 00:00:27,920
Which can be very very useful because you can use the upload to upload other types of malware.

7
00:00:27,920 --> 00:00:31,760
And you can use the download to download sensitive or important files.

8
00:00:32,030 --> 00:00:35,000
So again I'm back at my discord server.

9
00:00:35,000 --> 00:00:40,760
In here I have the computers that I'm controlling, and I'm going to interact with John's computer by

10
00:00:40,760 --> 00:00:42,350
clicking on interact.

11
00:00:42,500 --> 00:00:47,930
And in here we can simply do cmd, which is a command that we've covered before.

12
00:00:47,930 --> 00:00:55,160
And you can use there, which is a system command in windows to list the files and directories within

13
00:00:55,160 --> 00:00:56,780
the current working directory.

14
00:00:56,780 --> 00:00:59,450
So first of all we can see which directory we're in.

15
00:00:59,450 --> 00:01:00,620
We're in the downloads.

16
00:01:00,620 --> 00:01:03,710
This is John's computer or John's username as you know.

17
00:01:03,710 --> 00:01:07,130
And you can see the directories and files that we have in here.

18
00:01:07,130 --> 00:01:13,130
So if we wanted to go back one directory we can actually use the forward slash CD command straight away.

19
00:01:13,130 --> 00:01:16,340
So we don't have to use the forward slash cmd to do that.

20
00:01:16,340 --> 00:01:18,650
And let's say we want to go back one directory.

21
00:01:18,650 --> 00:01:21,230
We can do dot dot hit enter.

22
00:01:21,350 --> 00:01:27,710
And now if we do cmd there you'll see that we're back at the user John.

23
00:01:27,710 --> 00:01:30,530
And we can see all of the directories in here.

24
00:01:30,710 --> 00:01:33,500
Now let's go back into the downloads again.

25
00:01:33,500 --> 00:01:38,030
We're simply going to do forward slash CD directory name downloads.

26
00:01:38,030 --> 00:01:38,960
Hit enter.

27
00:01:38,960 --> 00:01:43,760
And if we do cmd there now to list the directories again.

28
00:01:43,760 --> 00:01:47,090
As you can see we are back in the downloads directory.

29
00:01:47,330 --> 00:01:52,130
Now if you're reading the files that we have in here, you can see that we have an interesting file

30
00:01:52,130 --> 00:01:53,180
called passwords.

31
00:01:53,180 --> 00:01:57,590
So if you want to read this file you can actually use a system command to read that.

32
00:01:57,590 --> 00:02:04,640
So forward slash cmd followed by the command to read files in windows which is more.

33
00:02:04,940 --> 00:02:11,630
And then the file name that we want to read which is passwords dot txt hit enter.

34
00:02:11,630 --> 00:02:14,930
So this is a basic system command that we're executing.

35
00:02:14,930 --> 00:02:20,750
And as you can see it's running that system command for us and allowing us to read the contents of passwords

36
00:02:20,750 --> 00:02:24,050
which potentially contains a username and a password.

37
00:02:24,410 --> 00:02:26,630
Now let's say these passwords are encrypted.

38
00:02:26,630 --> 00:02:30,170
So you want to download them and decrypt them at your own time later on.

39
00:02:30,170 --> 00:02:33,140
So you can use the forward slash download command.

40
00:02:33,350 --> 00:02:38,360
So as you can see it's telling you that it wants the path to the file that to download.

41
00:02:38,360 --> 00:02:43,220
So we're simply going to put the file name which is passwords dot txt.

42
00:02:44,470 --> 00:02:45,910
This file right here.

43
00:02:46,650 --> 00:02:48,090
And we're going to hit enter.

44
00:02:48,860 --> 00:02:49,670
And perfect.

45
00:02:49,670 --> 00:02:54,260
As you can see, it actually downloaded the file for me so we can see it in here.

46
00:02:54,260 --> 00:02:57,770
Or I can click on download in here to download it.

47
00:02:58,310 --> 00:02:59,180
And perfect.

48
00:02:59,180 --> 00:03:01,700
As you can see it's downloaded in here.

49
00:03:01,700 --> 00:03:04,970
One click and we have the contents in here.

50
00:03:05,570 --> 00:03:09,080
Now keep in mind all of this is happening through discord again.

51
00:03:09,080 --> 00:03:14,420
So you can even see that the download link that we got is on the discord app domain.

52
00:03:14,420 --> 00:03:18,290
So you're not downloading anything directly from the target computer.

53
00:03:18,290 --> 00:03:20,540
Everything is coming through discord.

54
00:03:20,540 --> 00:03:25,190
So this was actually sent as if a friend has sent you a txt file.

55
00:03:25,190 --> 00:03:31,370
That's the cool thing about dystopia, it is very stealth when it comes to communicating with the hacked

56
00:03:31,370 --> 00:03:32,240
computers.

57
00:03:32,840 --> 00:03:36,950
Next, let's say that you want to upload a file to this computer.

58
00:03:36,950 --> 00:03:41,840
Let's say you have more malware that you want to upload to it, or maybe you just want to change the

59
00:03:41,840 --> 00:03:43,700
password file for whatever reason.

60
00:03:43,700 --> 00:03:45,440
So we have a file in here.

61
00:03:45,440 --> 00:03:46,850
This is just a sample file.

62
00:03:46,850 --> 00:03:48,890
It needs to be a direct link as you can see.

63
00:03:48,890 --> 00:03:52,520
So we have a direct access to the file dot txt in here.

64
00:03:52,730 --> 00:03:55,100
So we're simply just going to copy it.

65
00:03:55,100 --> 00:03:58,010
We're going to go back to our access in here.

66
00:03:58,010 --> 00:04:00,200
We're going to do forward slash upload.

67
00:04:00,200 --> 00:04:03,410
So this is the upload command in dystopia.

68
00:04:03,410 --> 00:04:05,420
It's going to ask you for the URL.

69
00:04:05,420 --> 00:04:07,280
That's the URL that we want to upload.

70
00:04:07,280 --> 00:04:11,330
And the name let's say sample dot txt.

71
00:04:12,270 --> 00:04:14,430
Hit enter and give it a minute.

72
00:04:14,430 --> 00:04:18,030
And as you can see, it's saying that the file has been uploaded again.

73
00:04:18,030 --> 00:04:22,290
The file has been sent as a normal message to the target person.

74
00:04:22,470 --> 00:04:28,410
So when files are uploaded, they'll actually be uploaded into a directory called config.

75
00:04:28,410 --> 00:04:30,810
So this is the hacked computer in here.

76
00:04:30,810 --> 00:04:36,360
And if the upload was actually successful we should be able to find that file in the config directory.

77
00:04:36,480 --> 00:04:38,790
So we're going to go to this PC.

78
00:04:39,030 --> 00:04:44,850
We're going to go to C users our current user which is John.

79
00:04:45,030 --> 00:04:48,450
And in here there should be a folder called config.

80
00:04:48,450 --> 00:04:50,010
Now this folder is hidden.

81
00:04:50,010 --> 00:04:53,640
So we're going to put backward slash dot config.

82
00:04:55,320 --> 00:05:01,380
And inside the uploads directory, you're going to have files that has been uploaded to this computer.

83
00:05:01,650 --> 00:05:07,650
And if we click the sample, the file that we just uploaded, as you can see, the contents of this

84
00:05:07,650 --> 00:05:12,090
file are identical to the file that we uploaded, which is this file in here.

85
00:05:12,300 --> 00:05:18,420
So you can use this to upload malware and simply come in in here and execute it as a system command

86
00:05:18,420 --> 00:05:20,040
to run it on the target system.

87
00:05:20,040 --> 00:05:25,830
Or if you have an interactive shell, as I showed you previously, you can run it from the interactive

88
00:05:25,830 --> 00:05:26,340
shell.

89
00:05:26,970 --> 00:05:32,340
Now you can actually just use system commands to execute any other file system commands if you want.

90
00:05:32,340 --> 00:05:38,580
So you can delete files by simply doing forward slash cmd and executing the delete command.

91
00:05:38,580 --> 00:05:40,770
In windows, which is DLL.

92
00:05:40,770 --> 00:05:47,730
You can rename files by doing rename, so you have access to any windows command that you want through

93
00:05:47,730 --> 00:05:49,260
the CMD command.

94
00:05:49,260 --> 00:05:55,020
In dystopia, the main things that dystopia are offering to us are the download and the upload, which

95
00:05:55,020 --> 00:06:00,870
are really cool because like I said, they are facilitated through discord and they appear like normal

96
00:06:00,870 --> 00:06:05,010
messages or normal attachments that friends can send to each other through discord.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,150
The last thing that I want to cover about dystopia is the resource access.

2
00:00:05,150 --> 00:00:10,940
So it actually allows us to access the keyboard, the camera and the microphone at the moment and potentially

3
00:00:10,940 --> 00:00:15,530
in the future, more features could be added, but these are the main things that you'd want to access

4
00:00:15,530 --> 00:00:17,090
once you hack a computer.

5
00:00:17,270 --> 00:00:19,820
So let's go ahead and have a look.

6
00:00:19,910 --> 00:00:26,030
I already have my access in here as usual to my hacked computers, and access in the camera is actually

7
00:00:26,030 --> 00:00:27,020
very, very easy.

8
00:00:27,020 --> 00:00:28,280
There is a command to it.

9
00:00:28,280 --> 00:00:35,210
So you can do forward slash web shot to basically take a picture using the webcam.

10
00:00:35,210 --> 00:00:38,330
But alternatively you can simply use this button in here.

11
00:00:38,330 --> 00:00:44,210
So I'm just going to click Web Shot on John's computer and the camera should be pointing.

12
00:00:44,360 --> 00:00:45,020
This failed.

13
00:00:45,020 --> 00:00:46,010
Let's try it again.

14
00:00:46,010 --> 00:00:47,510
Sometimes it feels like this.

15
00:00:48,270 --> 00:00:53,730
So sometimes you might get this error message that tells you that it's didn't work.

16
00:00:53,730 --> 00:00:58,950
But if you just give it a bit of time, as you can see, you clearly will get the web shot that you

17
00:00:58,950 --> 00:00:59,580
asked for.

18
00:01:00,500 --> 00:01:06,140
Now, another, more useful resource that you might want to access instead of the camera is the keyboard.

19
00:01:06,140 --> 00:01:10,880
Because, as we know, we type all kinds of things using the keyboard, including passwords.

20
00:01:10,910 --> 00:01:13,640
Now, starting the keyboard is very, very easy.

21
00:01:13,640 --> 00:01:20,570
All you have to do is interact with the agent that you want to start the keyboard on and forward.

22
00:01:20,570 --> 00:01:22,580
Slash key log.

23
00:01:23,700 --> 00:01:29,280
And in the mode, you basically need to specify if you want to start or stop the keylogging.

24
00:01:29,280 --> 00:01:31,200
So we're going to say that we want to start it.

25
00:01:31,200 --> 00:01:37,410
And then in the interval you give it the interval of when it should send you the report of the captured

26
00:01:37,410 --> 00:01:38,130
keystrokes.

27
00:01:38,130 --> 00:01:39,120
So I can tell it.

28
00:01:39,120 --> 00:01:44,700
I want you to send me the capture keystrokes every 10s we're going to hit enter.

29
00:01:44,700 --> 00:01:47,820
And that's going to tell you that the keylogger has started.

30
00:01:47,820 --> 00:01:50,190
So let's go ahead to the target system.

31
00:01:50,190 --> 00:01:52,500
Let's open up a web browser.

32
00:01:52,650 --> 00:01:58,560
Let's for example, go to LinkedIn.com pretending that we want to log into LinkedIn.

33
00:01:58,560 --> 00:02:03,930
So everything I type on the keyboard now should be registered and logged by the backdoor.

34
00:02:03,930 --> 00:02:06,180
So let's say I'm logging into my account.

35
00:02:06,180 --> 00:02:10,320
Let's say Zaid at gmail.com.

36
00:02:10,320 --> 00:02:11,040
Doesn't really matter.

37
00:02:11,040 --> 00:02:12,330
Doesn't have to be a real account.

38
00:02:12,330 --> 00:02:15,570
And I'm going to put a password 123123123.

39
00:02:15,750 --> 00:02:17,400
Hit enter to log in.

40
00:02:17,400 --> 00:02:18,060
Doesn't really matter.

41
00:02:18,060 --> 00:02:19,050
It's not going to log me in.

42
00:02:19,050 --> 00:02:21,000
It's not correct information.

43
00:02:21,000 --> 00:02:27,480
But if we go back here to dystopia, as you remember, we actually set up a channel in here called keylogger.

44
00:02:27,480 --> 00:02:30,000
So your keystrokes are not going to appear in here.

45
00:02:30,000 --> 00:02:33,180
The logged keystrokes, they're going to appear in the keylogger.

46
00:02:33,180 --> 00:02:38,640
So if I click on keylogger in here, as you can see we have all of my keystrokes.

47
00:02:38,640 --> 00:02:42,300
So you can see I typed in LinkedIn.com followed by enter.

48
00:02:42,300 --> 00:02:44,910
Then I typed Zaid, I made a mistake.

49
00:02:44,910 --> 00:02:48,900
So you can see a quote in here because I made a mistake and I actually deleted it.

50
00:02:48,900 --> 00:02:56,640
And then I put the ad, and then I went ahead and I put Gmail, made a mistake, fixed it, and then

51
00:02:56,640 --> 00:03:00,060
I press tab to go into the password field.

52
00:03:00,060 --> 00:03:01,530
And then I put my password.

53
00:03:02,230 --> 00:03:09,250
So right now, every single keystroke that I input on this computer is being logged and sent to the

54
00:03:09,250 --> 00:03:10,330
keylogger channel.

55
00:03:10,690 --> 00:03:15,280
So this is very useful because you can actually harvest all kinds of information this way.

56
00:03:15,520 --> 00:03:19,600
And then once you're done, make sure that you come in and stop the keylogger.

57
00:03:19,600 --> 00:03:23,110
And you're going to do that by forward slash key log.

58
00:03:23,140 --> 00:03:25,810
The mode is going to be stop instead of start.

59
00:03:25,810 --> 00:03:28,000
And you don't need an interval for this one.

60
00:03:28,000 --> 00:03:31,690
You can just set it to zero and hit enter.

61
00:03:31,690 --> 00:03:33,640
And that will stop the keylogger.

62
00:03:34,350 --> 00:03:39,540
Now, in this section, I try to cover the basics and the most useful features of dystopia.

63
00:03:39,570 --> 00:03:44,130
There is more that you can do with this tool, and I recommend you spend more time with it and get to

64
00:03:44,130 --> 00:03:45,030
know it better.

65
00:03:45,030 --> 00:03:51,690
If you have some time, you can even try the telegram and the GitHub backdoors to get an idea of how

66
00:03:51,690 --> 00:03:52,260
they work.

67
00:03:52,260 --> 00:03:57,030
But like I said, we focused on the discord backdoor because it has this really nice interface.

68
00:03:57,030 --> 00:04:03,630
It's got the most features and it works on all operating systems, and you can even use it using a simple

69
00:04:03,630 --> 00:04:04,290
browser.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 15: Creating Windows Trojans

1
00:00:00,110 --> 00:00:06,470
So far, we covered a number of ways to create backdoors that will allow us to fully control the computers

2
00:00:06,470 --> 00:00:08,360
that they get executed on.

3
00:00:08,390 --> 00:00:14,720
The only problem is these backdoors look quite suspicious, so it would be very hard to convince a target

4
00:00:14,720 --> 00:00:17,030
to actually execute these backdoors.

5
00:00:17,330 --> 00:00:21,320
Therefore, in this section, I'm going to teach you how to create Trojans.

6
00:00:21,320 --> 00:00:27,470
Basically, I'm going to teach you how to backdoor legitimate files such as images, PDFs, or legitimate

7
00:00:27,470 --> 00:00:28,580
applications.

8
00:00:28,580 --> 00:00:35,030
As a result, you can social engineer the target to run an image or a PDF or an application that they

9
00:00:35,030 --> 00:00:36,080
are interested in.

10
00:00:36,080 --> 00:00:42,320
And when they run that application, our evil code or our backdoor will be executed in the background,

11
00:00:42,320 --> 00:00:45,950
allowing us to gain full control over their computer.

12
00:00:46,280 --> 00:00:51,800
Now, this topic doesn't really fall under hacking using the cloud, which is what this course is,

13
00:00:51,800 --> 00:00:56,300
but I felt like it's essential to cover it in here for the sake of completion.

14
00:00:56,300 --> 00:00:58,040
And just to give you the full picture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1
00:00:00,020 --> 00:00:05,030
In today's video, I'm going to show you how to easily and quickly create Trojans.

2
00:00:05,030 --> 00:00:11,510
What we mean by a Trojan is a file that opens up a normal file that the target person should be interested

3
00:00:11,510 --> 00:00:12,140
in.

4
00:00:12,140 --> 00:00:17,810
This can be an image, a PDF, or anything you want, but at the same time in the background.

5
00:00:17,810 --> 00:00:23,120
Execute code for a backdoor or anything that is useful to you as a hacker.

6
00:00:23,120 --> 00:00:25,670
Let me show you a quick example right here.

7
00:00:25,670 --> 00:00:29,810
I have two files and as you can see, both of them look like they are images.

8
00:00:29,810 --> 00:00:35,600
They are an image of the recent poster of the new matrix movie, but one of them is an actual image

9
00:00:35,600 --> 00:00:38,060
and the other is a Trojan.

10
00:00:38,060 --> 00:00:39,380
Let me show you the difference.

11
00:00:39,380 --> 00:00:43,610
So if I just run an image, you can see we're just going to see the image.

12
00:00:44,410 --> 00:00:49,210
Now, if I close this and run, the Trojan, which has the same icon, actually looks like an image,

13
00:00:49,210 --> 00:00:52,540
and if I double click it, I will also get the image.

14
00:00:52,540 --> 00:00:56,110
So the behavior is identical to an actual real image.

15
00:00:56,110 --> 00:01:01,540
But at the same time, running this file right here runs evil code in the background.

16
00:01:01,540 --> 00:01:07,450
It's code for a backdoor for an Empire stager, and sends a connection here to my Kali machine.

17
00:01:07,960 --> 00:01:15,190
And I have remote control over that computer and I can do anything I want on this windows computer.

18
00:01:15,190 --> 00:01:16,180
This one right here.

19
00:01:16,180 --> 00:01:21,160
So I can access its webcam, its file system, download and upload and do anything that the normal user

20
00:01:21,160 --> 00:01:21,790
can do.

21
00:01:21,790 --> 00:01:26,140
And as you can see, we did this using a normal file that looks like a normal image.

22
00:01:26,140 --> 00:01:31,390
And like I said earlier, you can do this with any file type, like a PDF or word document or anything

23
00:01:31,390 --> 00:01:32,140
else.

24
00:01:32,140 --> 00:01:35,890
Now, the idea of hacking computers using Trojans is not new.

25
00:01:35,890 --> 00:01:39,760
It existed for very long and there are so many ways to do it.

26
00:01:39,760 --> 00:01:42,160
I covered it in my ethical hacking course.

27
00:01:42,160 --> 00:01:47,860
I covered more ways in my social engineering course, and I even covered how to manually code everything

28
00:01:47,860 --> 00:01:50,110
in my Python and hacking course.

29
00:01:50,110 --> 00:01:54,490
So check them out if you want to learn more about this and learn it in details.

30
00:01:54,490 --> 00:01:59,710
But I'm going to teach you a quick way of doing that using PowerShell in this video.

31
00:02:00,040 --> 00:02:07,180
So all you'll need to do this is one PowerShell command or function that allows us to download a file

32
00:02:07,180 --> 00:02:12,520
from a specified URL and save it on disk as the name that you specify in here.

33
00:02:12,880 --> 00:02:18,430
Now we're going to run this command twice one time to download the actual image that we want the user

34
00:02:18,430 --> 00:02:22,240
to see, like the matrix image in here, or the PDF or anything you want.

35
00:02:22,240 --> 00:02:27,640
And the second time we're going to be downloading the evil file, which could be a backdoor or a keylogger

36
00:02:27,640 --> 00:02:30,310
or anything else you want to run in the background.

37
00:02:30,310 --> 00:02:31,480
Very, very easy.

38
00:02:31,480 --> 00:02:35,740
Let's do it step by step just to make sure that everything is going to work the way we want it.

39
00:02:35,740 --> 00:02:38,410
So let's test this functionality first of all.

40
00:02:38,410 --> 00:02:43,600
So I'm going to go to my browser and find an image or a PDF that I want to display to the user.

41
00:02:43,600 --> 00:02:47,830
And you want to make sure that the link that you use is the direct URL.

42
00:02:47,830 --> 00:02:50,080
So you can access that resource directly.

43
00:02:50,080 --> 00:02:53,050
It won't view the resource inside the HTML page.

44
00:02:53,050 --> 00:02:56,440
So right here I have a direct link to that matrix image.

45
00:02:56,440 --> 00:02:58,450
So I'm simply going to copy it.

46
00:02:58,450 --> 00:03:00,580
And I'm going to go back to my notepad.

47
00:03:00,580 --> 00:03:03,730
And we're just going to paste it in here as the URL.

48
00:03:05,150 --> 00:03:10,730
And finally we're going to store this the out file as and let's call it matrix dot png.

49
00:03:10,790 --> 00:03:13,190
So we're downloading a file from this URL.

50
00:03:13,190 --> 00:03:16,730
And we're storing it on disk with the following file name.

51
00:03:16,970 --> 00:03:21,560
So if we just copy this and open up a PowerShell prompt.

52
00:03:21,560 --> 00:03:23,360
So we're just going to type PowerShell.

53
00:03:25,430 --> 00:03:28,280
And right now we are in this specific path.

54
00:03:28,280 --> 00:03:31,160
So I'm actually just going to navigate to the desktop.

55
00:03:31,160 --> 00:03:34,370
So I'm going to do CD desktop to navigate to the desktop.

56
00:03:34,370 --> 00:03:36,530
You can see we are in the desktop now.

57
00:03:36,530 --> 00:03:38,990
And I'm just going to paste the command that I copied.

58
00:03:38,990 --> 00:03:40,700
So I'm just going to right click in here.

59
00:03:40,700 --> 00:03:43,160
And I'm going to hit enter to execute it.

60
00:03:43,160 --> 00:03:45,200
As you can see it's downloading the file.

61
00:03:45,200 --> 00:03:46,760
We can already see it in here.

62
00:03:46,760 --> 00:03:48,020
And here we go.

63
00:03:48,020 --> 00:03:50,570
Now we have the image downloaded on our desktop.

64
00:03:51,680 --> 00:03:57,410
So now we know that this function actually works as expected, and we can use it to download a file

65
00:03:57,410 --> 00:04:01,670
from the specified URL and stay and save it in the current working directory.

66
00:04:02,300 --> 00:04:04,010
So that's very very good.

67
00:04:04,010 --> 00:04:05,810
So I'm going to delete this file.

68
00:04:05,810 --> 00:04:09,770
And all we have to do right now is use this command twice.

69
00:04:09,770 --> 00:04:12,950
Like I said download the file that you want to display to the user.

70
00:04:12,950 --> 00:04:17,900
First open it and then download the file that you want to run in the background and open it.

71
00:04:17,900 --> 00:04:21,500
So this is basically a download and execute payload.

72
00:04:21,970 --> 00:04:24,850
Then we're going to start everything in a bat file.

73
00:04:24,880 --> 00:04:30,610
A bat file is a file that contains a number of commands that get automatically executed when the user

74
00:04:30,610 --> 00:04:31,570
double click it.

75
00:04:31,690 --> 00:04:35,830
But files can only run system commands, not PowerShell commands.

76
00:04:35,860 --> 00:04:41,680
Therefore, because this is a PowerShell and we executed it in the PowerShell prompt, we will have

77
00:04:41,680 --> 00:04:44,800
to actually type PowerShell before the command.

78
00:04:45,340 --> 00:04:50,350
And then we're going to say the PowerShell command that we want to run is this command.

79
00:04:50,350 --> 00:04:54,760
And we're going to enclose it by double quotes at the start and at the end.

80
00:04:55,000 --> 00:05:00,760
So basically all we're saying right here that we want to execute the following command.

81
00:05:00,760 --> 00:05:04,900
The command that we just run in the PowerShell prompt as a PowerShell command.

82
00:05:04,900 --> 00:05:08,410
And we're doing this by specifying the command argument.

83
00:05:08,770 --> 00:05:12,040
Then we know that this command is going to download the file.

84
00:05:12,040 --> 00:05:17,290
And it's actually going to store it on disk with the following name matrix dot png.

85
00:05:17,440 --> 00:05:20,650
So the next thing we will want to do is actually run that file.

86
00:05:20,650 --> 00:05:21,250
Execute it.

87
00:05:21,250 --> 00:05:23,350
So the user sees it on their screen.

88
00:05:23,350 --> 00:05:28,240
So we're simply just going to type the file name the matrix dot png because that file is downloaded

89
00:05:28,240 --> 00:05:29,200
now on disk.

90
00:05:29,890 --> 00:05:34,300
Next we're going to need to do the second step which is download the file that we want to run in the

91
00:05:34,300 --> 00:05:36,940
background and execute it on the system.

92
00:05:36,940 --> 00:05:41,620
So I'm first going to need to run the exact same command as we have in here.

93
00:05:41,680 --> 00:05:46,840
And we're going to replace the image URL, this time with the link to the Empire Stager.

94
00:05:46,840 --> 00:05:48,040
I'm using a ready one.

95
00:05:48,040 --> 00:05:54,220
It's already hosted on my own server, and obviously we don't want to store it as matrix dot png.

96
00:05:54,250 --> 00:05:57,070
We're actually going to store it as a batch file as well.

97
00:05:57,070 --> 00:06:00,010
So we're just going to call it Empire dot bat.

98
00:06:00,010 --> 00:06:02,140
Now obviously you can use different names.

99
00:06:02,140 --> 00:06:06,250
This file being a bat file we can actually embed all of the code in here within it.

100
00:06:06,250 --> 00:06:10,780
But I'm just trying to show you a generic way that you can use with multiple scenarios.

101
00:06:11,110 --> 00:06:17,140
So now this link is going to download the backdoor for us or the stager or the evil file.

102
00:06:17,140 --> 00:06:22,780
And the next step is going to be to execute that file again exactly like we did in here.

103
00:06:22,780 --> 00:06:25,450
We downloaded matrix dot png from this URL.

104
00:06:25,450 --> 00:06:26,440
And then we run it.

105
00:06:26,440 --> 00:06:28,300
And then we download the backdoor.

106
00:06:28,300 --> 00:06:31,390
In this line we're saving it as Empire dot bat.

107
00:06:31,390 --> 00:06:34,840
And we're going to run it by simply type in Empire dot bat.

108
00:06:35,570 --> 00:06:36,320
And that's it.

109
00:06:36,350 --> 00:06:37,040
We're ready.

110
00:06:37,070 --> 00:06:42,560
The only thing is, once this is executed, as we've seen when we executed this PowerShell command,

111
00:06:42,560 --> 00:06:46,490
the image was downloaded in the working directory in the desktop.

112
00:06:46,490 --> 00:06:52,430
Therefore, if the target downloads this in their downloads and run the Trojan, they will actually

113
00:06:52,430 --> 00:06:58,250
see the image file being downloaded and the backdoor being downloaded to that working directory.

114
00:06:58,250 --> 00:07:04,400
So they will see new files being displayed in their folder in here, and therefore that will be suspicious.

115
00:07:04,400 --> 00:07:09,440
So what we're going to do before doing anything, we're actually going to change our working directory

116
00:07:09,440 --> 00:07:13,250
exactly the same way that we did in here when we did CD desktop.

117
00:07:13,250 --> 00:07:19,340
But instead, instead of going to the desktop, which is a place that the user sees a lot, we're actually

118
00:07:19,340 --> 00:07:20,930
going to go to the temp directory.

119
00:07:20,930 --> 00:07:23,420
So we're going to do CD temp.

120
00:07:24,040 --> 00:07:30,700
And we're using the percentage signs in here to tell the operating system to navigate to the temp path,

121
00:07:30,700 --> 00:07:33,310
regardless of where that temp path is.

122
00:07:33,310 --> 00:07:37,360
So we're using the environment temp variable and that's it.

123
00:07:37,390 --> 00:07:38,500
We're actually ready to go.

124
00:07:38,500 --> 00:07:42,730
We're going to first of all go to the temp directory, download an image or any file that you want to

125
00:07:42,730 --> 00:07:43,870
display to the user.

126
00:07:43,870 --> 00:07:49,150
Open the file, download an evil file, open it again and you can do this multiple times.

127
00:07:49,150 --> 00:07:52,000
If you want to open a number of evil files or a number of things.

128
00:07:52,000 --> 00:07:54,820
So this can be used in so many scenarios.

129
00:07:55,240 --> 00:07:57,550
So once you're done, we're going to save this.

130
00:07:57,550 --> 00:08:04,690
And you just want to make sure that you set the type to all files and set the extension to to a batch

131
00:08:04,690 --> 00:08:05,080
file.

132
00:08:05,080 --> 00:08:06,760
So use whatever name you want.

133
00:08:06,760 --> 00:08:10,360
So let's say matrix Trojan this time.

134
00:08:10,360 --> 00:08:12,310
And we're just going to call it Dot.

135
00:08:12,310 --> 00:08:15,850
But now obviously you don't want to tell the user that this is a Trojan.

136
00:08:15,850 --> 00:08:17,530
We're just doing this in the video.

137
00:08:17,530 --> 00:08:18,490
And that's it.

138
00:08:18,490 --> 00:08:19,000
We're done.

139
00:08:19,000 --> 00:08:20,560
Let's select a place to save it.

140
00:08:20,560 --> 00:08:21,880
Let's save it on my desktop.

141
00:08:21,880 --> 00:08:22,630
That's fine.

142
00:08:22,630 --> 00:08:24,460
And I'm going to save it there.

143
00:08:24,460 --> 00:08:25,330
And that's it.

144
00:08:25,330 --> 00:08:25,900
We're ready.

145
00:08:25,900 --> 00:08:27,550
Let's go ahead and execute it.

146
00:08:29,220 --> 00:08:29,910
And perfect.

147
00:08:29,910 --> 00:08:32,850
As you can see, it's downloading the image first and then it's running it.

148
00:08:32,850 --> 00:08:37,740
Now obviously preferably you'd want to use a file that is not that big.

149
00:08:37,740 --> 00:08:40,350
So it's downloaded and executed quickly.

150
00:08:40,350 --> 00:08:42,990
But as you can see we can see the image on file.

151
00:08:42,990 --> 00:08:48,540
We don't see any strange files in here because we stored everything in the temp directory.

152
00:08:48,540 --> 00:08:54,360
And our if our evil code got executed in the background, I should have got an agent in here.

153
00:08:54,360 --> 00:08:57,780
And sure enough, as you can see, I get a connection through my empire.

154
00:08:57,780 --> 00:09:01,320
So now I can remotely control that windows machine from here.

155
00:09:02,090 --> 00:09:03,500
Now I know what you're thinking.

156
00:09:03,500 --> 00:09:06,410
This file right here looks very, very suspicious.

157
00:09:06,410 --> 00:09:10,010
It doesn't look like the Trojan that I showed you at the start of the video.

158
00:09:10,010 --> 00:09:11,810
But don't worry about that.

159
00:09:11,810 --> 00:09:16,910
In the next lecture, I'll teach you how to make this Trojan look and behave exactly like the Trojan

160
00:09:16,910 --> 00:09:18,440
that I showed you at the start.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,470 --> 00:00:04,790
As mentioned previously, this file right here looks very, very suspicious.

2
00:00:04,790 --> 00:00:08,540
It doesn't look like the Trojan that I showed you at the start of the video.

3
00:00:09,270 --> 00:00:14,610
Not only that, but if you right click this file and open it in a text editor, you will actually see

4
00:00:14,610 --> 00:00:16,650
the code inside it, which is not very good.

5
00:00:16,650 --> 00:00:19,710
The user is going to know that you're trying to do something suspicious.

6
00:00:19,950 --> 00:00:25,500
Therefore, in this lecture I'm going to teach you how to compile this trojan to an executable and give

7
00:00:25,500 --> 00:00:27,930
it an icon and also run it in the background.

8
00:00:27,930 --> 00:00:33,660
Because when we executed this, we had a terminal window that we seen, which is also very, very suspicious.

9
00:00:33,930 --> 00:00:38,580
So to address all of these issues, all you have to do is compile it to an executable.

10
00:00:38,580 --> 00:00:41,280
You can use a program like Bat to exe.

11
00:00:41,460 --> 00:00:43,830
I will include its links in the resources.

12
00:00:43,830 --> 00:00:46,800
So all you have to do is simply run the program.

13
00:00:48,170 --> 00:00:53,570
Open the bat file that you just created, or you can simply just drag and drop it in here you can already

14
00:00:53,570 --> 00:01:00,110
see the code, and all we want to do is tick the icon in here and select the icon that you want to use.

15
00:01:00,110 --> 00:01:06,470
Now if this was a PDF, you can simply just download a generic PDF icon or a generic image icon.

16
00:01:06,470 --> 00:01:12,920
But as you can see in windows, if the file is an image, you will actually see a thumbnail of the image

17
00:01:12,920 --> 00:01:14,600
similar to what we have in here.

18
00:01:14,600 --> 00:01:19,130
Therefore, we're going to have to manually create an icon that looks like this image.

19
00:01:19,130 --> 00:01:21,980
So to do that, we're going to use an online service.

20
00:01:21,980 --> 00:01:23,420
Again there's a lot of these.

21
00:01:23,420 --> 00:01:26,690
And simply you're just going to have to upload it.

22
00:01:26,690 --> 00:01:29,810
So we have the image in our downloads.

23
00:01:30,390 --> 00:01:31,800
And this is it.

24
00:01:31,830 --> 00:01:35,040
We're going to click on convert and download it.

25
00:01:36,790 --> 00:01:37,990
We're going to save it.

26
00:01:37,990 --> 00:01:39,700
It's going to go into my downloads.

27
00:01:39,700 --> 00:01:44,230
So if I just look at it here very quickly, you can see the icon in here.

28
00:01:45,010 --> 00:01:48,520
So we're going to go back to our bat to X.

29
00:01:48,550 --> 00:01:50,290
We already ticked the icon.

30
00:01:50,290 --> 00:01:54,910
We're going to select the icon that we want which is in my downloads.

31
00:01:55,710 --> 00:01:57,120
Double click it.

32
00:01:57,120 --> 00:02:00,360
And we're also going to change the X format.

33
00:02:00,390 --> 00:02:02,310
We're going to keep it at 32 bit.

34
00:02:02,310 --> 00:02:08,160
But we're going to select the invisible option which will basically run the executable in the background

35
00:02:08,160 --> 00:02:12,270
without showing a terminal window so that it is less suspicious.

36
00:02:12,300 --> 00:02:17,370
You can even ask it for UAC, and if you do, then the backdoor is going to run as admin.

37
00:02:17,370 --> 00:02:19,380
But we don't want to do that at this stage.

38
00:02:19,380 --> 00:02:24,690
So I'm just going to click on convert in here to convert it to an executable for me.

39
00:02:24,690 --> 00:02:28,290
And again we're just going to store this on the desktop.

40
00:02:28,290 --> 00:02:31,440
And this time let's call it Matrix poster.

41
00:02:31,890 --> 00:02:33,000
Save.

42
00:02:33,300 --> 00:02:34,440
Everything is fine.

43
00:02:34,440 --> 00:02:36,780
Let's minimize and look at the file.

44
00:02:36,780 --> 00:02:37,650
And perfect.

45
00:02:37,650 --> 00:02:39,480
As you can see the file looks perfect.

46
00:02:39,480 --> 00:02:44,070
It looks like an actual image with the thumbnail that's executed the file.

47
00:02:44,070 --> 00:02:49,260
As you can see, we did not see a terminal window, so everything got executed in the background.

48
00:02:49,260 --> 00:02:51,540
Again we can see the image in here.

49
00:02:51,540 --> 00:02:58,680
Icon looks not suspicious at all, but if we go to our Kali machine, we can see that we got a new connection.

50
00:02:58,680 --> 00:03:03,630
And from here, like I said, you have remote control over that computer and you can do anything you

51
00:03:03,630 --> 00:03:04,230
want.

52
00:03:04,230 --> 00:03:08,610
And like I said earlier, you don't have to always use an empire stager.

53
00:03:08,610 --> 00:03:12,570
You can use any file and you can display any file to the user as well.

54
00:03:12,570 --> 00:03:17,340
All you have to do is just simply download the files you want and execute them like so.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 16: Creating Apple Mac OS & Linux Trojans

1
00:00:00,050 --> 00:00:06,020
Previously, we covered how to generate windows backdoors through Empire and hack windows computers

2
00:00:06,020 --> 00:00:07,790
and control them from Empire.

3
00:00:07,790 --> 00:00:12,890
And as you saw, because this is all happening through the cloud, we're able to control these computers

4
00:00:12,890 --> 00:00:17,390
from any device that has a web browser, like a phone or a computer or a tablet.

5
00:00:17,570 --> 00:00:24,080
So in the next few lectures, I want to show you how to generate backdoors for Apple Mac OS and Linux

6
00:00:24,080 --> 00:00:24,800
computers.

7
00:00:24,800 --> 00:00:29,690
And that's one of the main things about Empire, is that it's a command and control server that you

8
00:00:29,690 --> 00:00:35,960
can basically use to build your own botnet and hack all operating systems, so we can distribute backdoors

9
00:00:35,960 --> 00:00:37,670
for all operating systems.

10
00:00:37,670 --> 00:00:43,070
And if any of these operating systems run our backdoors, they will send the connections back to Empire,

11
00:00:43,070 --> 00:00:48,440
where we're going to be able to control these computers through any device with a web browser.

12
00:00:49,060 --> 00:00:51,880
So to do this, we're going to go back to Empire.

13
00:00:51,880 --> 00:00:57,190
I already have it installed, and I already have my listener listening on my cloud server.

14
00:00:57,190 --> 00:01:03,160
And as you know, in order to create a stager or a back door, we go to the stagers menu in here.

15
00:01:03,670 --> 00:01:09,400
Now in here, as shown previously, I created a windows back door or a windows stager, and we used

16
00:01:09,400 --> 00:01:10,900
it to hack windows computers.

17
00:01:10,900 --> 00:01:15,400
So right now we want to create back doors for Apple Mac OS and for Linux.

18
00:01:15,400 --> 00:01:19,780
And to do that we're simply going to click on the create, just like we did before.

19
00:01:19,780 --> 00:01:26,260
And from the type, instead of selecting one of the windows back doors that we have in here, we're

20
00:01:26,260 --> 00:01:29,560
actually going to go ahead and use a multi back door.

21
00:01:29,560 --> 00:01:35,950
And if you remember when I first introduced back doors or stagers I said the multi back doors will work

22
00:01:35,950 --> 00:01:38,890
on all operating systems, hence the name multi.

23
00:01:38,890 --> 00:01:44,440
So they will work on Apple Mac OS computers and on Linux computers.

24
00:01:44,830 --> 00:01:46,390
So I'm going to select that.

25
00:01:46,390 --> 00:01:49,870
And as shown before the rest of this is very easy.

26
00:01:49,870 --> 00:01:52,330
First of all you have to set the back door name.

27
00:01:52,330 --> 00:01:57,160
So let's say multi bash agent.

28
00:01:57,580 --> 00:02:02,680
So the multi bash agent will work on any computer that has bash installed on it.

29
00:02:02,680 --> 00:02:06,640
So basically it will work on any Unix based operating system.

30
00:02:06,640 --> 00:02:11,530
And therefore it will work on both Apple Mac OS and Linux computers.

31
00:02:12,070 --> 00:02:14,170
Next we're going to select the listener.

32
00:02:14,170 --> 00:02:17,350
So we can actually use the same listener that we use previously.

33
00:02:17,350 --> 00:02:21,760
And I showed you at the start of the lecture the Http listener the language.

34
00:02:21,760 --> 00:02:23,350
We're going to keep it at Python.

35
00:02:23,350 --> 00:02:25,600
And we're going to keep everything the same.

36
00:02:26,450 --> 00:02:29,120
I'm going to click submit to create the backdoor.

37
00:02:29,120 --> 00:02:33,560
And as you know, this would be created and it can be displayed in the stagers menu.

38
00:02:33,560 --> 00:02:37,580
But if we want to download it I can simply click on download in here.

39
00:02:38,350 --> 00:02:42,880
So I'm just going to call it multi batch agent again.

40
00:02:43,060 --> 00:02:44,290
I'm going to save.

41
00:02:44,290 --> 00:02:46,300
And that's it saved here for me.

42
00:02:46,300 --> 00:02:51,430
So if we open it as you can see we have the code for this agent.

43
00:02:51,430 --> 00:02:55,990
And in the next lectures I'm going to show you how to package this in an executable.

44
00:02:55,990 --> 00:02:59,380
But for now I just want to test it and make sure that this works.

45
00:02:59,380 --> 00:03:01,870
So I'm going to copy all of this.

46
00:03:02,620 --> 00:03:07,000
And I'm going to go ahead to a Linux computer right here.

47
00:03:07,000 --> 00:03:09,100
I'm going to open up the terminal.

48
00:03:10,210 --> 00:03:13,870
And I'm simply going to paste all of that code in here.

49
00:03:13,990 --> 00:03:15,340
And I'm going to hit enter.

50
00:03:15,760 --> 00:03:21,400
So that should have executed the agent and should have allowed me to hack this computer.

51
00:03:21,400 --> 00:03:26,080
So let's go ahead to Empire and see if we receive the connection.

52
00:03:26,470 --> 00:03:28,180
So we're going to go to agents.

53
00:03:29,420 --> 00:03:30,230
And perfect.

54
00:03:30,230 --> 00:03:33,230
As you can see, we have a new connection in here.

55
00:03:33,230 --> 00:03:37,220
It's detecting that it's coming from a virtual machine, but it doesn't really matter.

56
00:03:37,700 --> 00:03:42,500
And if we click the agent, we can go ahead and communicate with it.

57
00:03:42,500 --> 00:03:45,890
If we click on the view, we're going to get the basic information.

58
00:03:45,890 --> 00:03:47,510
We have the computer name.

59
00:03:48,740 --> 00:03:51,410
We have the operating system details in here.

60
00:03:51,410 --> 00:03:55,940
It's running ubuntu and as usual you have the file browser in here.

61
00:03:55,940 --> 00:04:02,330
In order to access the file system, download, upload and edit files, you can go to the interact to

62
00:04:02,330 --> 00:04:07,340
actually interact with it and run all of the Post-exploitation modules that we saw earlier.

63
00:04:07,340 --> 00:04:11,150
You can go ahead to the terminal and run any command you want.

64
00:04:11,150 --> 00:04:15,800
We're just going to do sysinfo just to make sure that everything is running as expected.

65
00:04:15,800 --> 00:04:16,370
Perfect.

66
00:04:16,370 --> 00:04:19,280
As you can see, we got the system information.

67
00:04:19,280 --> 00:04:22,550
It's running Linux, the computer name and all of that.

68
00:04:22,880 --> 00:04:28,370
And we can again simply do shell, just like we seen before to be dropped into a system shell.

69
00:04:28,370 --> 00:04:31,760
And from here we'll be able to execute any commands we want.

70
00:04:31,760 --> 00:04:37,010
Like we can do LLS to list the files or execute any other Linux command, as you know.

71
00:04:37,190 --> 00:04:42,590
So basically right now we have full control over this Linux computer.

72
00:04:42,590 --> 00:04:49,040
But as I mentioned, the backdoor or the stager that we created in here is a multi bash agent.

73
00:04:49,040 --> 00:04:52,460
So it should work on any Unix based operating system.

74
00:04:52,460 --> 00:04:58,100
Therefore if we go ahead and run this on an Apple computer it should also allow us to control it.

75
00:04:58,100 --> 00:05:03,470
And like I said I'll teach you how to package this in an executable file in the next lectures.

76
00:05:03,470 --> 00:05:07,970
But for now we just test in this backdoor and making sure that it works as expected.

77
00:05:07,970 --> 00:05:14,180
So we're just going to go to an Apple computer, and we're simply going to go ahead and open up the

78
00:05:14,180 --> 00:05:16,670
terminal and paste the code.

79
00:05:18,730 --> 00:05:20,170
We're going to hit enter.

80
00:05:20,810 --> 00:05:28,880
And if we go back here to our agents, as you can see, we got a connection back from the Apple computer

81
00:05:28,880 --> 00:05:31,880
again just to verify that this works as expected.

82
00:05:31,880 --> 00:05:36,890
If we come here and click the view, we can see the computer information.

83
00:05:36,890 --> 00:05:43,640
We can see that it is running the Darwin kernel, which is the Apple kernel and file browser will allow

84
00:05:43,640 --> 00:05:49,640
us to browse the files as you saw earlier, and using the interact will be able to run the Post-exploitation

85
00:05:49,640 --> 00:05:50,390
modules.

86
00:05:50,390 --> 00:05:54,650
And from here again we can interact with the target using the terminal.

87
00:05:54,650 --> 00:05:58,460
Or we can use the shell command to be dropped into a system shell.

88
00:05:59,060 --> 00:06:04,880
So again right now from here, by simply clicking on the agents, I already managed to hack a Linux

89
00:06:04,880 --> 00:06:13,400
computer and an Apple Mac OS computer by simply executing the code of the multi bash generic stager

90
00:06:13,400 --> 00:06:14,660
that we created.

91
00:06:14,660 --> 00:06:19,850
So right now we're simply just testing this backdoor or stager and making sure that it works properly.

92
00:06:19,850 --> 00:06:26,540
And next I'm going to show you how to put this inside an executable and embed it with a legitimate application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,580 --> 00:00:08,260
So previously we saw how we can hack Apple macOS computers and Linux computers using the same multi

2
00:00:08,290 --> 00:00:09,460
bash stager.

3
00:00:10,230 --> 00:00:15,840
But as you can see, in order for this to work, we actually copied the stager code and executed it

4
00:00:15,840 --> 00:00:16,770
in the terminal.

5
00:00:16,770 --> 00:00:23,430
So that is only useful in a post-exploitation scenario if you already have access to the target computer,

6
00:00:23,430 --> 00:00:30,180
because it would be very difficult to convince a target to open a terminal and run this scary code on

7
00:00:30,180 --> 00:00:31,170
their computer.

8
00:00:31,380 --> 00:00:37,800
So in this lecture and the next lecture, I'm going to show you how to embed this code within a legitimate

9
00:00:37,800 --> 00:00:40,860
application, effectively creating a Trojan.

10
00:00:41,510 --> 00:00:46,910
So a Trojan is basically a file that looks and functions like a legitimate file.

11
00:00:46,910 --> 00:00:52,340
So when it's executed, it displays the file that the user is expecting.

12
00:00:52,340 --> 00:00:57,410
But at the same time it executes our evil code in the background.

13
00:00:57,410 --> 00:01:05,810
So the goal now is to embed the scary code that we have in here into an actual legitimate application,

14
00:01:05,810 --> 00:01:12,080
and social engineer our target to run it so you can pretend to be a friend or a company that the target

15
00:01:12,080 --> 00:01:14,960
trusts, or you can even serve it through beef.

16
00:01:14,960 --> 00:01:21,080
As an update, we covered beef previously, and I cover a lot of delivery methods in my social engineering

17
00:01:21,080 --> 00:01:24,680
course, so if you're interested in this, I highly recommend that course.

18
00:01:24,680 --> 00:01:31,520
But the bottom line is we're going to be embedding this stager code in a legitimate application.

19
00:01:31,520 --> 00:01:37,370
And then it's up to you how to deliver that application and convince the target and running this application.

20
00:01:37,880 --> 00:01:42,980
So first of all, we need to find an application that the target person would be interested in.

21
00:01:42,980 --> 00:01:48,200
So this is the front file or the legitimate file that they are interested in.

22
00:01:48,200 --> 00:01:51,560
Now we're going to be doing this for Mac OS in this lecture.

23
00:01:51,560 --> 00:01:57,530
So you can simply go to Google and look for whatever application that you think the target would be

24
00:01:57,530 --> 00:01:58,310
interested in.

25
00:01:58,310 --> 00:02:00,650
In my case, I'm going to look for Firefox.

26
00:02:00,650 --> 00:02:07,610
I'm going to say I want it for Mac OS, and I want it in the dot pkg format, because that's the format

27
00:02:07,610 --> 00:02:09,560
that we are going to be backdooring.

28
00:02:10,310 --> 00:02:13,370
And as you can see, the first result is going to be useful.

29
00:02:13,370 --> 00:02:15,470
Now, you don't have to do this for Firefox.

30
00:02:15,470 --> 00:02:17,660
I'm just doing it for Firefox in this lecture.

31
00:02:17,660 --> 00:02:23,180
And the steps are going to be exactly the same to any other PG file that you pick.

32
00:02:23,270 --> 00:02:26,180
So I'm going to click the download link in here.

33
00:02:26,180 --> 00:02:31,790
And as you can see it's going to take you directly to a DMG and to a PG file.

34
00:02:31,790 --> 00:02:33,770
So make sure you download the PG.

35
00:02:33,860 --> 00:02:35,780
Now I already have it downloaded.

36
00:02:35,780 --> 00:02:36,860
And here.

37
00:02:36,860 --> 00:02:42,410
So this is basically a package that contains all of the files needed to install Firefox.

38
00:02:42,410 --> 00:02:45,020
So first I'm going to uncompress this package.

39
00:02:45,020 --> 00:02:50,990
And then I'm going to embed my evil code in it and then compress it again into a malicious package.

40
00:02:50,990 --> 00:02:56,120
So to uncompress this package, first of all, we need to navigate to the location where this package

41
00:02:56,120 --> 00:02:56,990
is downloaded.

42
00:02:56,990 --> 00:03:00,620
And it's in my downloads in a directory called Trojan.

43
00:03:00,710 --> 00:03:05,540
So I have my terminal in here and I'm going to use the CD command to do that.

44
00:03:05,540 --> 00:03:07,880
So I'm going to do CD downloads.

45
00:03:07,880 --> 00:03:08,900
Trojan.

46
00:03:10,260 --> 00:03:14,100
And if we do LZ, as you can see, we have this file right here.

47
00:03:14,580 --> 00:03:21,060
And in order to decompress this file we're going to use a program called package util.

48
00:03:21,060 --> 00:03:30,450
So pkg util and we're going to say we want to expand the package that is called Firefox dot package.

49
00:03:30,450 --> 00:03:35,910
So we're basically saying we want to uncompress or expand this package this one right here.

50
00:03:35,910 --> 00:03:39,360
And we want to expand it into a new directory.

51
00:03:39,360 --> 00:03:45,330
The new directory I'm going to call it Firefox Expanded.

52
00:03:45,780 --> 00:03:47,220
I'm going to hit enter.

53
00:03:47,220 --> 00:03:50,520
And as you can see I'm going to get a new directory in here.

54
00:03:50,520 --> 00:03:57,210
And inside this directory we have all of the package contents that allow the user to install Firefox.

55
00:03:57,750 --> 00:04:04,770
So now all we have to do is simply put our evil code in here and then package this again into a new

56
00:04:04,770 --> 00:04:05,430
package.

57
00:04:06,550 --> 00:04:13,060
And I have my evil code or my stager code right here, and all I'm going to do is simply remove this

58
00:04:13,060 --> 00:04:18,280
line in here, because this line removes this file after it gets executed.

59
00:04:18,280 --> 00:04:20,050
So I don't want to do that anymore.

60
00:04:20,050 --> 00:04:21,550
I'm simply going to remove it.

61
00:04:21,550 --> 00:04:24,760
And then I'm going to go ahead and save this file.

62
00:04:24,880 --> 00:04:28,000
And I'm going to save it in a specific location.

63
00:04:28,000 --> 00:04:34,060
Like I said, we want to save it inside the package that we just extracted.

64
00:04:34,060 --> 00:04:37,570
So it's inside the directory called Firefox Expanded.

65
00:04:38,080 --> 00:04:44,770
So we're going to navigate to that location which is in my downloads in Trojan Firefox Expanded.

66
00:04:44,770 --> 00:04:47,650
And in here we're going to create a new directory.

67
00:04:47,650 --> 00:04:49,990
So I'm going to click on new folder in here.

68
00:04:49,990 --> 00:04:54,280
We want this code to run automatically once the package is installed.

69
00:04:54,280 --> 00:04:57,820
So we have to place it inside this directory called scripts.

70
00:04:59,750 --> 00:05:08,090
And we're going to name it Post install just like so again, we're naming it this specific name so that

71
00:05:08,090 --> 00:05:12,530
it automatically runs once the package finishes installing Firefox.

72
00:05:13,100 --> 00:05:16,520
So we're going to click on save and that is it saved.

73
00:05:16,520 --> 00:05:22,040
So if we look at our package content now as you can see we have a new directory called scripts.

74
00:05:22,040 --> 00:05:25,580
And inside it we have our post install script.

75
00:05:25,580 --> 00:05:32,360
And if we view it quickly, as you can see we have our evil code or backdoor or stager code in here.

76
00:05:32,360 --> 00:05:36,950
So that is all perfect and it should automatically run.

77
00:05:36,950 --> 00:05:41,480
And it actually should be called just post install, not post install.sh.

78
00:05:41,480 --> 00:05:44,900
So I'm just going to remove the dot ssh from the end of it in here.

79
00:05:45,350 --> 00:05:52,850
And finally, now that we have this in the correct location, all we have to do is reference it in this

80
00:05:52,850 --> 00:05:59,180
file right here the package info, so that once the package fully finishes installing, it will call

81
00:05:59,180 --> 00:06:01,100
my backdoor and execute it.

82
00:06:01,100 --> 00:06:04,790
So I'm going to need to open this using a text editor as well.

83
00:06:05,970 --> 00:06:10,980
And we're simply going to put at the end of this, we're going to open up a new tag.

84
00:06:10,980 --> 00:06:13,050
We're going to call it scripts.

85
00:06:13,410 --> 00:06:20,070
And just like HTML or any other markup language, once you open it, you have to close it by doing forward

86
00:06:20,070 --> 00:06:22,080
slash scripts.

87
00:06:22,260 --> 00:06:28,440
And then inside this scripts tag we're simply going to say we have.

88
00:06:29,270 --> 00:06:42,020
A post install and the file name is between two quotations dot forward slash post install so that it

89
00:06:42,020 --> 00:06:42,950
runs this file.

90
00:06:42,950 --> 00:06:48,350
So as you know we do dot forward slash to run the file or to specify a file within the same working

91
00:06:48,350 --> 00:06:49,070
directory.

92
00:06:49,070 --> 00:06:57,050
And now that this is done we're simply going to close this tag by doing a forward slash and close the

93
00:06:57,050 --> 00:06:57,680
tag.

94
00:06:58,500 --> 00:07:02,820
So all we're doing is basically creating a new tag in here.

95
00:07:02,850 --> 00:07:08,850
The tag is called scripts because we actually want to run a script in the scripts directory.

96
00:07:08,850 --> 00:07:12,660
And in there we're saying we have a post install script.

97
00:07:12,660 --> 00:07:16,710
This post install script is located inside a file.

98
00:07:16,710 --> 00:07:23,640
The file is also called post install, so that once the package finishes installing Firefox, it will

99
00:07:23,640 --> 00:07:24,600
call this file.

100
00:07:24,600 --> 00:07:31,290
And as you know, this file is actually the backdoor that we created previously.

101
00:07:31,830 --> 00:07:36,420
So all I have to do now is simply save this package information file.

102
00:07:36,420 --> 00:07:39,510
And we can close this and we can close this.

103
00:07:39,510 --> 00:07:44,700
We also need to change the permissions of the post install file in here.

104
00:07:45,670 --> 00:07:48,820
So we're going to do chmod to change the permissions.

105
00:07:48,820 --> 00:07:51,880
The permission that we want is 755.

106
00:07:52,270 --> 00:07:56,170
And then we're going to put the file name that we want to change its permissions.

107
00:07:56,170 --> 00:07:58,390
And it's this file right here.

108
00:07:58,390 --> 00:08:02,650
So it's in Firefox expanded scripts Post-install.

109
00:08:03,480 --> 00:08:05,400
So we're going to type that in here.

110
00:08:05,400 --> 00:08:10,230
Firefox expanded scripts post install.

111
00:08:10,470 --> 00:08:11,580
I'm going to hit enter.

112
00:08:11,580 --> 00:08:13,560
And that runs with no issues at all.

113
00:08:13,560 --> 00:08:19,980
And as you can see here the icon changed to an executable or a terminal icon meaning that this is an

114
00:08:19,980 --> 00:08:21,600
executable file now.

115
00:08:21,660 --> 00:08:25,080
And now that our package is ready.

116
00:08:25,080 --> 00:08:31,980
So everything is included in here inside the Firefox Expanded, we need to actually package all of this

117
00:08:31,980 --> 00:08:37,530
so that it looks like one file, like this one right here, like the original Firefox package.

118
00:08:37,980 --> 00:08:42,510
And to do that we're going to use the exact same tool package util.

119
00:08:42,960 --> 00:08:48,930
And this time instead of expand we're going to say we want to flatten this directory right here.

120
00:08:48,930 --> 00:08:52,620
So it's called Firefox Expanded.

121
00:08:52,620 --> 00:08:57,510
And then we're going to give it the name of the package that it's going to create.

122
00:08:57,510 --> 00:09:01,200
And we're going to call it Firefox Backdoored.

123
00:09:02,090 --> 00:09:04,400
Dot p k g.

124
00:09:04,910 --> 00:09:06,530
So very very simple.

125
00:09:06,530 --> 00:09:11,780
We use this command in order to expand an actual package.

126
00:09:11,780 --> 00:09:18,620
We modified the content, embedded our code into the post install script, and then referenced it into

127
00:09:18,620 --> 00:09:19,850
the package info.

128
00:09:19,850 --> 00:09:24,980
And then we're going to package this using the same tool using the flatten command.

129
00:09:24,980 --> 00:09:30,950
And all of this is going to go into a file that is called Firefox backdoored dot pkg.

130
00:09:31,730 --> 00:09:36,650
So if I hit enter now you'll see we have our Firefox Backdoored package.

131
00:09:36,650 --> 00:09:39,860
So now you can go ahead and share this with your target.

132
00:09:39,860 --> 00:09:46,310
If they execute this it will install Firefox on their system and also run the backdoor giving you full

133
00:09:46,310 --> 00:09:47,960
control over their computer.

134
00:09:48,320 --> 00:09:49,820
So let's go ahead and test it.

135
00:09:49,820 --> 00:09:54,260
So let's go to the target computer right here.

136
00:09:54,260 --> 00:10:00,200
And I should have it in my downloads right here we have it Firefox Backdoored.

137
00:10:00,230 --> 00:10:04,940
Now because we did not sign this package we actually have to right click and open.

138
00:10:04,940 --> 00:10:06,080
We can't double click it.

139
00:10:06,080 --> 00:10:09,680
But you'll get that with any package that you have not signed.

140
00:10:09,680 --> 00:10:11,420
Same as this warning message.

141
00:10:11,420 --> 00:10:15,200
You'll always get this with packages that are not signed properly.

142
00:10:15,200 --> 00:10:21,380
You can sign packages if you have an Apple Developer ID, but that is really completely outside of the

143
00:10:21,380 --> 00:10:23,720
scope of the current topic.

144
00:10:23,720 --> 00:10:29,030
So I'm simply just going to click open to go ahead and install this Backdoored Firefox.

145
00:10:29,030 --> 00:10:32,060
And as you can see you get a normal installation prompt.

146
00:10:32,060 --> 00:10:33,770
So we're just going to go next.

147
00:10:33,770 --> 00:10:36,260
We're going to say install it for me please.

148
00:10:36,650 --> 00:10:38,150
It's going to ask for the password.

149
00:10:38,150 --> 00:10:40,760
And this is normal for the Firefox installer.

150
00:10:40,760 --> 00:10:43,910
The password is actually being asked by the Firefox installer.

151
00:10:43,910 --> 00:10:48,020
And it's going to go ahead and actually install Firefox for us.

152
00:10:48,020 --> 00:10:48,980
And perfect.

153
00:10:48,980 --> 00:10:53,120
As you can see it's telling us the installation is successful.

154
00:10:53,120 --> 00:10:56,780
So if we go ahead to our applications.

155
00:10:57,480 --> 00:11:02,220
You'll actually see that Firefox is installed here for us, and you can go ahead and use it.

156
00:11:02,220 --> 00:11:05,370
So the target person is not going to feel suspicious at all.

157
00:11:05,370 --> 00:11:12,750
But at the same time, if we go back to Empire, you'll see that we just got a connection from our target.

158
00:11:12,750 --> 00:11:18,330
And as usual, if you execute it and interact with it, you'll be able to do everything that empires

159
00:11:18,330 --> 00:11:23,190
allows us to do, which basically give us full remote control over this computer.

160
00:11:23,190 --> 00:11:28,470
And this time we did it through a package that installs a legitimate application.

161
00:11:28,470 --> 00:11:30,510
The package actually installs Firefox.

162
00:11:30,510 --> 00:11:36,510
And like I said, you can replace Firefox with any other package that you think the target person might

163
00:11:36,510 --> 00:11:37,620
be interested in.

164
00:11:37,950 --> 00:11:43,440
So you can use this to deliver your back door as an update or as a new application that you developed.

165
00:11:43,440 --> 00:11:44,640
The sky's the limit.

166
00:11:44,640 --> 00:11:50,160
And like I said, you can send this as a email that comes from a friend or from a company that they

167
00:11:50,160 --> 00:11:50,550
trust.

168
00:11:50,550 --> 00:11:52,770
Or you can use beef as shown in this lecture.

169
00:11:52,770 --> 00:11:57,900
And the email technique and many other techniques are actually covered in my social engineering course.

170
00:11:57,900 --> 00:12:01,590
So if you're interested in this, I highly recommend doing that course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:07,700
So previously we covered how to embed our Empire Stager in a legitimate application for Apple Mac OS

2
00:00:07,700 --> 00:00:08,480
computers.

3
00:00:08,480 --> 00:00:13,220
And when that application got executed, it installed the application that the user wanted.

4
00:00:13,220 --> 00:00:18,110
But at the same time it ran our backdoor, giving us full control over their computer.

5
00:00:18,110 --> 00:00:23,660
So in this lecture, I want to show you how to do the exact same but for Linux computers.

6
00:00:23,660 --> 00:00:29,780
So I'm going to show you how to embed our Empire stager in a Linux package so that when the package

7
00:00:29,780 --> 00:00:35,360
is installed, it installs the program that the user is expecting, but at the same time runs our backdoor

8
00:00:35,360 --> 00:00:36,500
in the background.

9
00:00:36,680 --> 00:00:41,900
And you're going to see that the general idea is very similar to what we did with Apple Mac OS.

10
00:00:41,930 --> 00:00:46,610
The only difference is that we're going to be doing everything from the terminal now, because we're

11
00:00:46,610 --> 00:00:48,740
going to be using command line tools.

12
00:00:48,740 --> 00:00:50,870
So let's jump right into it.

13
00:00:50,870 --> 00:00:56,750
And as you know, the first thing that we need to get is the normal program or the legitimate application

14
00:00:56,750 --> 00:00:58,610
that we want to backdoor.

15
00:00:58,610 --> 00:01:03,800
And I'm going to be doing this for ubuntu, which is the most popular Linux distribution.

16
00:01:03,800 --> 00:01:09,170
But the steps that I'm going to show you will work for any Debian based Linux distribution.

17
00:01:09,170 --> 00:01:15,170
So that includes Debian Mint, Kali Linux and many other Debian based Linux distributions.

18
00:01:15,530 --> 00:01:20,150
So the first thing you want to do is get the right package for the target operating system.

19
00:01:20,150 --> 00:01:23,870
You want to make sure you get something that is compatible with their computer.

20
00:01:23,870 --> 00:01:31,520
So because I am targeting a ubuntu computer, I am at Packages.ubuntu.com in order to download a package,

21
00:01:31,520 --> 00:01:35,480
and I'm targeting the 22.04 LTS version.

22
00:01:35,480 --> 00:01:37,730
And that's why I'm going to click the jammie.

23
00:01:37,730 --> 00:01:40,100
That's the name of the distribution.

24
00:01:40,100 --> 00:01:46,910
And from here you have a list of categories of applications or packages that you can download for this

25
00:01:46,910 --> 00:01:47,840
distribution.

26
00:01:47,840 --> 00:01:55,100
And I want to download something for the web because in my opinion that makes it easy to deliver through

27
00:01:55,100 --> 00:01:55,370
beef.

28
00:01:55,370 --> 00:01:59,960
So you can deliver this as an update prompt, as I showed you previously through beef.

29
00:01:59,960 --> 00:02:02,510
So I'm going with the web category.

30
00:02:02,510 --> 00:02:07,250
And from here I'm actually going to look for something to do with Firefox.

31
00:02:07,250 --> 00:02:11,810
And as you can see, we actually have a lot of fonts that you can get the user to install.

32
00:02:11,810 --> 00:02:17,840
So you can simply get the target user to load a malicious page on that page, tell them that they need

33
00:02:17,840 --> 00:02:23,480
to install a font for the page to work properly, and then backdoor the font so that when they install

34
00:02:23,480 --> 00:02:27,470
the font, they get the font, but at the same time you will hack their computer.

35
00:02:27,470 --> 00:02:32,420
So I'm simply going to download the Firefox local on.

36
00:02:33,650 --> 00:02:37,010
And as you can see, there's only one package for all architectures.

37
00:02:37,010 --> 00:02:38,570
So we're just going to click that.

38
00:02:38,570 --> 00:02:42,500
And then you can select any of these links in here or in here.

39
00:02:42,500 --> 00:02:44,750
So I'm just going to select this one.

40
00:02:44,750 --> 00:02:49,940
And I'm actually instead of clicking it I'm going to right click and copy the link address because I

41
00:02:49,940 --> 00:02:52,220
don't want to download it to this computer.

42
00:02:52,220 --> 00:02:56,390
I actually want to download it in my Kali machine in here.

43
00:02:56,390 --> 00:02:59,870
And I'm going to do wget to download a file.

44
00:02:59,870 --> 00:03:03,110
And then I'm going to paste the download link.

45
00:03:03,260 --> 00:03:07,940
So the wget command can be used to download any file from the internet.

46
00:03:07,940 --> 00:03:12,680
And then I'm specifying the link to that file which is this file right here.

47
00:03:13,040 --> 00:03:16,850
And note that this file has a dot deb extension.

48
00:03:16,850 --> 00:03:20,480
That is the extension for Debian based packages.

49
00:03:20,540 --> 00:03:24,590
Like I said, this will work on all Debian based operating systems.

50
00:03:24,860 --> 00:03:26,240
So I'm going to hit enter.

51
00:03:28,650 --> 00:03:29,430
And perfect.

52
00:03:29,430 --> 00:03:30,750
Now the file is downloaded.

53
00:03:30,750 --> 00:03:35,190
So if I do RLS, as you can see we have the package in here.

54
00:03:35,900 --> 00:03:41,750
So next, just like what we did with Apple Mac OS, we're going to have to first of all decompress this

55
00:03:41,750 --> 00:03:49,010
package, embed our code within it as a post installation script, and then package it again in Apple

56
00:03:49,010 --> 00:03:49,580
Mac OS.

57
00:03:49,610 --> 00:03:53,720
You use the command line utility called package util.

58
00:03:53,720 --> 00:04:00,500
And in this example, because we are on a Debian operating systems, we're going to use the package

59
00:04:00,500 --> 00:04:01,490
dash Deb.

60
00:04:02,330 --> 00:04:09,800
And in order to uncompress or extract a package instead of the expand argument, we're actually going

61
00:04:09,800 --> 00:04:14,060
to do dash capital R, and then we're going to specify the file name.

62
00:04:14,060 --> 00:04:16,550
So in our case this is the file name.

63
00:04:16,550 --> 00:04:20,180
So you can simply copy it and paste it.

64
00:04:20,180 --> 00:04:26,060
And then we're going to specify the directory where we want to unpack the contents of this package.

65
00:04:26,060 --> 00:04:32,180
And we're simply going to call it Firefox Unpacked similar to what we did in the last lecture.

66
00:04:32,180 --> 00:04:32,990
Hit enter.

67
00:04:32,990 --> 00:04:38,960
And now if we list the files and directories, as you can see we have a new directory in here which

68
00:04:38,960 --> 00:04:42,050
is basically the contents of this package.

69
00:04:42,320 --> 00:04:47,990
So next we need to put our eval code in here as a Post-installation script.

70
00:04:48,350 --> 00:04:53,390
So we're going to use the CD command to navigate into Firefox and packed.

71
00:04:53,720 --> 00:04:58,700
If we list in here you'll see we have a directory called Debian and Apple Mac OS.

72
00:04:58,700 --> 00:05:02,090
We placed our script inside a directory called scripts.

73
00:05:02,090 --> 00:05:05,990
In this case we're going to be placing it inside the Debian directory.

74
00:05:05,990 --> 00:05:09,140
Now these are simply standards followed by these packages.

75
00:05:09,140 --> 00:05:11,780
So this is nothing that I am making up myself.

76
00:05:11,780 --> 00:05:15,920
So we're going to go ahead and navigate into the Debian directory.

77
00:05:16,340 --> 00:05:21,830
And if we list in here you'll see that we actually don't have a Post-installation script.

78
00:05:21,830 --> 00:05:23,540
If you do you can modify it.

79
00:05:23,540 --> 00:05:24,380
We don't have it.

80
00:05:24,380 --> 00:05:25,760
So we're going to create a new one.

81
00:05:25,760 --> 00:05:31,310
And to do that we're simply going to use nano, which is, as you know, a command line text editor.

82
00:05:31,310 --> 00:05:38,270
But because there is no file in here that has the name post inst, once I hit enter, it's going to

83
00:05:38,270 --> 00:05:43,610
open up an empty file for me, and when I save it, it's going to save it as a new file.

84
00:05:43,910 --> 00:05:48,410
So all I have to do is simply paste the code for my Empire stager in here.

85
00:05:49,190 --> 00:05:50,810
And I have that in here.

86
00:05:50,810 --> 00:05:55,250
So I'm simply going to copy it all and paste it here.

87
00:05:55,430 --> 00:06:01,520
And just like what we did with the Apple Post-installation script, we're actually going to remove this

88
00:06:01,520 --> 00:06:05,180
line, the mm line because it'll simply delete the script.

89
00:06:05,180 --> 00:06:06,380
We don't want to do that.

90
00:06:06,380 --> 00:06:11,450
And we're going to do control X to save it Y to say keep the same name.

91
00:06:11,450 --> 00:06:15,950
And as you can see this time the name is Post-install instead of Post-install.

92
00:06:15,950 --> 00:06:20,210
In the case of Apple we're going to hit enter and that is saved there.

93
00:06:20,210 --> 00:06:26,900
So if I list now as you can see, I have a new file here called Post-install inside the Debian inside

94
00:06:26,900 --> 00:06:28,280
the unpacked package.

95
00:06:28,280 --> 00:06:34,130
And just like what we did with Apple macOS, we actually need to change the permissions of this file

96
00:06:34,130 --> 00:06:35,570
to an executable.

97
00:06:35,570 --> 00:06:38,240
And to do that we use the chmod command.

98
00:06:38,240 --> 00:06:41,300
We want to set the permissions to seven, five, five.

99
00:06:41,300 --> 00:06:45,200
And the file that we want to change its permissions is the post.

100
00:06:46,240 --> 00:06:46,960
Inst.

101
00:06:46,960 --> 00:06:48,190
Can I hit enter?

102
00:06:48,190 --> 00:06:54,910
And if I list again, you'll see the post inst is listed as green, meaning that it is an executable.

103
00:06:55,360 --> 00:07:01,900
So now we're ready to go ahead and package this as a Debian package so that it can be installed on other

104
00:07:01,900 --> 00:07:03,370
Linux distributions.

105
00:07:03,370 --> 00:07:09,880
And because it has this post installation file, it will automatically run this file once the installation

106
00:07:09,880 --> 00:07:15,340
is complete, which will run my backdoor giving me full control over that computer.

107
00:07:16,000 --> 00:07:17,890
So let's go ahead and package this.

108
00:07:17,890 --> 00:07:23,260
I'm going to do CD dot dot to go back one level CD dot dot again to go back another level.

109
00:07:23,260 --> 00:07:26,650
And just going to clear the screen and list the files.

110
00:07:26,650 --> 00:07:29,470
And as you can see this is the original one.

111
00:07:29,470 --> 00:07:34,300
This is the directory that contains the post installation backdoor.

112
00:07:34,300 --> 00:07:38,650
So we need to create a Debian file from this directory.

113
00:07:38,650 --> 00:07:43,690
And we're going to use the same tool that we used to decompress the original package.

114
00:07:43,690 --> 00:07:46,990
So we're going to use the package Deb.

115
00:07:46,990 --> 00:07:49,540
And this time we're going to do dash B.

116
00:07:49,540 --> 00:07:54,850
In order to create the package we're going to tell it which directory we want to package.

117
00:07:54,850 --> 00:07:56,890
And it's the this directory right here.

118
00:07:56,890 --> 00:08:00,430
So it's called Firefox Unpacked.

119
00:08:00,430 --> 00:08:03,160
And then we're going to give it the name of the package.

120
00:08:03,160 --> 00:08:06,940
And we're going to call it Firefox Backdoored.

121
00:08:06,940 --> 00:08:09,490
And this is actually just a font for Firefox.

122
00:08:09,490 --> 00:08:13,300
It's not really Firefox but we're just going to keep it like this for now.

123
00:08:13,300 --> 00:08:20,680
And this is going to be a dot deb because dot Deb is the extension for Debian based packages.

124
00:08:21,190 --> 00:08:26,410
We're using the package dash Deb, which is the package utility for Debian.

125
00:08:26,410 --> 00:08:32,470
We're using the dash B to create a new package from the contents of this directory right here.

126
00:08:32,470 --> 00:08:34,750
And the new package name is this.

127
00:08:35,640 --> 00:08:37,230
I'm going to hit enter.

128
00:08:37,560 --> 00:08:42,360
And if we do LZ now as you can see we have a new package.

129
00:08:42,540 --> 00:08:47,280
So this package should contain our backdoor as a post installation script.

130
00:08:47,280 --> 00:08:51,000
So all we have to do now is share it with our target and test it.

131
00:08:51,390 --> 00:08:57,030
Now you know we can actually use post drop as I showed you previously or use Apache to share this.

132
00:08:57,030 --> 00:09:00,690
So now I can go ahead to my target Linux computer.

133
00:09:00,690 --> 00:09:02,460
This Linux computer right here.

134
00:09:02,460 --> 00:09:06,480
I already have the package downloaded in here and in Linux.

135
00:09:06,480 --> 00:09:10,740
In order to install a Debian package, you actually have to install it from the terminal.

136
00:09:10,740 --> 00:09:12,780
So this is nothing too suspicious.

137
00:09:12,780 --> 00:09:15,090
Linux users are used to do this.

138
00:09:15,090 --> 00:09:17,310
So I'm going to open up my terminal.

139
00:09:17,880 --> 00:09:22,140
So we're going to do CD downloads where the package is.

140
00:09:22,140 --> 00:09:30,030
If we do LZ this is where the package and usually in Linux to install a package you do the package dash

141
00:09:30,030 --> 00:09:34,860
I followed by the package name which is Firefox backdoor dot Deb.

142
00:09:35,010 --> 00:09:41,460
So this is a very normal command that most Linux users are used to do in order to install packages.

143
00:09:41,460 --> 00:09:45,690
And if we hit enter, it's going to tell us we need to run it as root.

144
00:09:45,690 --> 00:09:47,670
So we have to do sudo to run it.

145
00:09:47,670 --> 00:09:48,240
Again.

146
00:09:48,240 --> 00:09:52,320
Very normal for Linux packages to be executed as root.

147
00:09:52,470 --> 00:09:55,230
And so we're just going to put my password.

148
00:09:56,210 --> 00:10:00,350
And as you can see, it's going to go ahead and install the package for you.

149
00:10:00,470 --> 00:10:03,590
It's got the right package name which is Firefox Local.

150
00:10:03,920 --> 00:10:06,110
And like I said this is just the font.

151
00:10:06,140 --> 00:10:11,180
If this was any other application, it'll have that application name and it will actually install it

152
00:10:11,180 --> 00:10:12,740
for the target user.

153
00:10:12,770 --> 00:10:18,860
Now the main thing is we want to see if our backdoor got executed in the background once this installation

154
00:10:18,860 --> 00:10:19,970
was successful.

155
00:10:20,000 --> 00:10:22,070
So if we come here perfect.

156
00:10:22,070 --> 00:10:24,800
As you can see we got a new connection.

157
00:10:24,800 --> 00:10:28,280
If we click it, we have access now to the target computer.

158
00:10:28,280 --> 00:10:30,290
We have all the information in here.

159
00:10:30,290 --> 00:10:36,080
And we're actually logged in as root now because Linux packages have to be installed as root.

160
00:10:36,080 --> 00:10:41,300
So by default now we are the highest privileged users on the target operating system.

161
00:10:41,300 --> 00:10:47,090
And we managed to do this by getting the target to install a legitimate package, not a backdoor.

162
00:10:47,090 --> 00:10:50,450
And they would have actually got the application that they want.

163
00:10:50,450 --> 00:10:56,420
But at the same time, our backdoor got executed in the background, giving us full control over their

164
00:10:56,420 --> 00:10:57,200
computer.

165
00:10:57,320 --> 00:11:01,520
So from here we can go ahead and access the file system.

166
00:11:01,520 --> 00:11:07,130
We can execute all of the Post-exploitation modules, or we can go to the terminal and execute anything

167
00:11:07,130 --> 00:11:08,900
that we can do from the terminal.

168
00:11:08,900 --> 00:11:10,760
The sky is the limit from here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 17: Advanced Malware Delivery

1
00:00:00,050 --> 00:00:06,320
Now that you know how to create backdoors and Trojans to hack all types of operating system, we need

2
00:00:06,320 --> 00:00:12,200
a reliable and convincing method to share these backdoors and trojans with our targets.

3
00:00:12,200 --> 00:00:18,230
And with this course being a cloud course, I can't leave you without teaching you how to properly upload

4
00:00:18,230 --> 00:00:20,570
and host malware on the cloud.

5
00:00:20,690 --> 00:00:26,150
I'm also going to teach you how to hide the file extension or change it to anything that you want.

6
00:00:26,150 --> 00:00:32,090
And finally, I'm going to teach you how to create your own custom download page that will automatically

7
00:00:32,090 --> 00:00:37,940
detect the operating system of the computer that is loading it and serve it, the appropriate malware

8
00:00:37,940 --> 00:00:44,300
that will work with that operating system, basically allowing you to hack all operating systems windows,

9
00:00:44,300 --> 00:00:47,390
Linux, and Apple Mac OS using one link.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,020 --> 00:00:05,930
Previously, we covered how to host your own files using Apache, and we saw how you can clone websites.

2
00:00:05,930 --> 00:00:11,210
Or you can actually host malware such as backdoors, trojans, or whatever kind of files you want.

3
00:00:11,210 --> 00:00:16,460
And all you have to do is put it in your var HTML, which is the web root as we know.

4
00:00:16,460 --> 00:00:22,310
And when the user puts your website name followed by forward slash, the file name which is backdoor,

5
00:00:22,610 --> 00:00:28,070
it's going to connect to Apache on port 80, and it's going to download the file that the user is requesting

6
00:00:28,070 --> 00:00:28,460
here.

7
00:00:28,460 --> 00:00:30,950
And therefore they're going to get back to our dot exe.

8
00:00:31,760 --> 00:00:33,980
So that's really really good for sharing files.

9
00:00:33,980 --> 00:00:36,140
But we could do better.

10
00:00:36,140 --> 00:00:39,380
So there are two problems that we have with this link.

11
00:00:39,410 --> 00:00:43,580
The first problem is the website naming here Website.com.

12
00:00:43,580 --> 00:00:49,460
Now as I showed you before, you can purchase more convincing domain name based on your target.

13
00:00:49,460 --> 00:00:56,000
So you can go on Name.com or any name registrar and select a domain name that represents the file that

14
00:00:56,000 --> 00:01:00,200
you want the target to download, so that problem can be easily solved.

15
00:01:00,200 --> 00:01:05,660
The other problem that we have here is the actual file name in here backdoor dot exe.

16
00:01:05,690 --> 00:01:07,640
Now obviously you're not going to call it backdoor.

17
00:01:07,640 --> 00:01:10,670
But the problem here is the exe extension.

18
00:01:10,670 --> 00:01:12,020
This is an executable.

19
00:01:12,020 --> 00:01:14,330
And this scares off a lot of people.

20
00:01:14,330 --> 00:01:18,680
Unless you're actually social engineering the target to download an executable.

21
00:01:18,680 --> 00:01:24,650
So unless you're telling them this is a program or this is an update that you need to install to combat

22
00:01:24,650 --> 00:01:26,420
problem one in here.

23
00:01:26,420 --> 00:01:30,980
As I said before, you can purchase a domain name that can be more convincing.

24
00:01:30,980 --> 00:01:36,260
In order to download a file, for example, you can just purchase a domain name that is called g download

25
00:01:36,260 --> 00:01:42,650
so that it seems like it's short for Google download, and then give them a file that is called Chromadex

26
00:01:42,650 --> 00:01:45,680
and tell them that this is an update for Chrome, for example.

27
00:01:45,680 --> 00:01:51,350
Now we also covered a number of ways to manipulate URLs and make them seem more convincing.

28
00:01:51,350 --> 00:01:54,950
So you can create a subdomain and call the subdomain Google.

29
00:01:54,950 --> 00:02:00,230
Again, we showed that before you could create a directory and call the directory Google, so the link

30
00:02:00,230 --> 00:02:01,370
would look like this.

31
00:02:01,370 --> 00:02:08,090
Or you can use the add trick so you can put any name you want followed by an add, followed by the domain

32
00:02:08,090 --> 00:02:09,170
name that you bought.

33
00:02:09,170 --> 00:02:12,050
And then you can put the file that the user is going to download.

34
00:02:12,050 --> 00:02:13,400
And this should work.

35
00:02:13,910 --> 00:02:16,370
So all of these solutions have been covered before in details.

36
00:02:16,370 --> 00:02:20,000
If you don't remember them you can revise the URL manipulation lecture.

37
00:02:20,000 --> 00:02:25,040
But all of these solutions only address problem number one that we have in here.

38
00:02:25,730 --> 00:02:28,040
Problem two is a bit trickier.

39
00:02:28,040 --> 00:02:31,790
So in all of these cases you can see the file name in here.

40
00:02:31,790 --> 00:02:37,520
And as you can see it ends with an extension that is a little bit scary because we know that this is

41
00:02:37,520 --> 00:02:38,600
an executable.

42
00:02:39,170 --> 00:02:44,810
So what I want to show you today is a tool that you can use to create your own file hosting service.

43
00:02:44,810 --> 00:02:51,200
And instead of having the exe here at the end of the file name, you can actually serve the URL like

44
00:02:51,200 --> 00:02:51,740
so.

45
00:02:51,950 --> 00:02:56,930
Not only that, but you can even disguise or change the extension.

46
00:02:56,930 --> 00:03:03,500
So instead of exe, if you have a Trojan that for example loads an image or loads a PDF book, you can

47
00:03:03,500 --> 00:03:05,300
actually have the link look like this.

48
00:03:05,300 --> 00:03:10,970
So the link would be dot pdf or dot png or dot any extension you want.

49
00:03:10,970 --> 00:03:14,840
But when the user loads it, it will actually download an executable.

50
00:03:15,200 --> 00:03:16,550
Let me show you a quick example.

51
00:03:16,550 --> 00:03:19,670
So this is very clear right here I have a URL.

52
00:03:19,670 --> 00:03:22,820
So this is a domain that I own which is Zacks.com.

53
00:03:23,330 --> 00:03:26,060
You can change this to any domain that you want like I said.

54
00:03:26,060 --> 00:03:28,430
And you can pick something that is more believable.

55
00:03:28,550 --> 00:03:34,460
And in here we have a file that is called Chrome manual dot PDF.

56
00:03:34,460 --> 00:03:37,040
So the file extension is an e-book.

57
00:03:37,040 --> 00:03:41,480
Now if I hit enter to download this file it's going to download it for me.

58
00:03:41,480 --> 00:03:43,670
And if we look in the downloads.

59
00:03:44,950 --> 00:03:45,730
You'll see.

60
00:03:45,730 --> 00:03:47,740
I have the chrome manual in here.

61
00:03:47,740 --> 00:03:49,720
And this is actually a Trojan.

62
00:03:49,720 --> 00:03:52,270
So this file contains a backdoor.

63
00:03:52,270 --> 00:03:54,190
And this is the original manual.

64
00:03:54,190 --> 00:03:55,960
And as you can see they look identical.

65
00:03:55,960 --> 00:04:00,850
And I actually covered this in my ethical hacking course in the social engineering course and on the

66
00:04:00,850 --> 00:04:02,770
YouTube channel How to Create Trojans.

67
00:04:02,770 --> 00:04:08,380
So a Trojan is a file that will run something malicious in the background, but at the same time display

68
00:04:08,380 --> 00:04:09,970
something useful to the target.

69
00:04:09,970 --> 00:04:15,940
So right now we have a file that has a PDF icon that if you double click it will actually give you a

70
00:04:15,940 --> 00:04:16,840
PDF.

71
00:04:17,380 --> 00:04:19,300
Now there's ways to bypass this warning.

72
00:04:19,300 --> 00:04:21,910
This is just a warning that you're running an executable.

73
00:04:22,360 --> 00:04:27,550
But as you can see, once you run the file you actually get a normal PDF and it's actually a manual.

74
00:04:27,550 --> 00:04:31,240
So you have to select a file that the target person would be interested in.

75
00:04:31,240 --> 00:04:34,780
That all goes back to social engineering and information gathering.

76
00:04:34,780 --> 00:04:40,750
But at the same time, this file executed code that will give me full control over this computer.

77
00:04:40,750 --> 00:04:44,470
So if you go to the Kali machine in here, you can see we got a connection.

78
00:04:44,470 --> 00:04:49,600
And right now you can actually do anything that the normal user can do on their computer.

79
00:04:50,180 --> 00:04:58,190
So the goal here is to be able to deliver this file using a link that actually looks like a PDF.

80
00:04:58,190 --> 00:05:00,950
So as you can see here, we have a normal website name.

81
00:05:00,950 --> 00:05:03,320
This website actually uses Https.

82
00:05:03,320 --> 00:05:09,290
And as you can see the file name is a normal file name and the extension is the right extension.

83
00:05:09,290 --> 00:05:10,250
It's an e-book.

84
00:05:10,250 --> 00:05:11,690
It's not an executable.

85
00:05:11,690 --> 00:05:16,730
And therefore the chances of the user believing this and downloading this file and executing it are

86
00:05:16,730 --> 00:05:17,480
much higher.

87
00:05:18,420 --> 00:05:22,440
So all of this can be done using a tool called Pindrop.

88
00:05:22,470 --> 00:05:28,500
Now this tool, first of all, allows you to create your own file hosting service on the internet that

89
00:05:28,500 --> 00:05:32,940
you can upload any files to so that in its own is very, very useful.

90
00:05:32,940 --> 00:05:35,700
But that's not the only thing that it allows us to do.

91
00:05:35,700 --> 00:05:41,370
It allows us to disable and enable files with a single click, which is really good to bypass crawlers

92
00:05:41,370 --> 00:05:44,940
and to avoid having your website being flagged as malicious.

93
00:05:44,940 --> 00:05:50,160
You can serve different versions of the same file, so you can serve files that do not contain a backdoor.

94
00:05:50,160 --> 00:05:55,860
And then when you want to start attacking a certain company, or when you want to start a certain engagement,

95
00:05:55,860 --> 00:05:58,710
you can replace these files automatically or with a click.

96
00:05:58,710 --> 00:06:03,720
With Trojans, you can create custom paths again with just a number of clicks.

97
00:06:03,720 --> 00:06:10,440
And the coolest thing is, what I just showed you is to be able to rename or hide the file extension.

98
00:06:10,740 --> 00:06:16,200
And obviously all of that is linked to a nice domain name with Https enabled, as you saw earlier.

99
00:06:16,200 --> 00:06:18,810
And I'm going to show you how to do all of that next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:04,790
The next step is to actually go ahead and install poem drop the file hosting framework.

2
00:00:04,790 --> 00:00:08,270
So first of all we're going to go to the domain name settings.

3
00:00:08,270 --> 00:00:12,080
And I've actually already purchased a domain name that is called g download.

4
00:00:12,080 --> 00:00:15,500
Like I said that is more believable and looks less malicious.

5
00:00:15,500 --> 00:00:19,640
So we can say that the G is short for Google for example.

6
00:00:19,640 --> 00:00:26,390
And we're going to just add an A record and we're going to link that a record to the IP address of my

7
00:00:26,390 --> 00:00:27,350
Kali machine.

8
00:00:27,350 --> 00:00:30,560
And I've created a fresh Kali machine for this lecture in here.

9
00:00:30,560 --> 00:00:32,930
So I'm just going to copy this.

10
00:00:34,640 --> 00:00:36,320
And we're going to go back in here.

11
00:00:36,320 --> 00:00:37,520
We're going to paste it here.

12
00:00:37,520 --> 00:00:46,460
And as we said before, a records allow us to link the domain name to the IP address of our cloud server.

13
00:00:46,820 --> 00:00:48,710
So we're going to click on Add Record.

14
00:00:48,710 --> 00:00:51,740
And as we said before this could take a few minutes to propagate.

15
00:00:51,740 --> 00:00:57,020
But that's fine because the next step is to actually go ahead and install home drop the file hosting

16
00:00:57,020 --> 00:00:57,650
framework.

17
00:00:57,650 --> 00:01:00,020
So this is the GitHub repository.

18
00:01:00,020 --> 00:01:02,330
I'm going to include it in the resources of the lecture.

19
00:01:02,330 --> 00:01:05,030
And I'm just going to copy its link.

20
00:01:05,790 --> 00:01:08,130
I'm going to go to the terminal.

21
00:01:08,130 --> 00:01:13,800
I've already sshed into that Kali instance on the cloud, so I'm just going to elevate my privileges

22
00:01:13,800 --> 00:01:15,870
to root by doing sudo su.

23
00:01:15,870 --> 00:01:19,290
And then I'm going to go to the opt directory.

24
00:01:19,290 --> 00:01:24,750
This is the directory that you should be installing optional applications in, hence the name opt.

25
00:01:25,200 --> 00:01:31,380
So in the opt we're going to do git clone followed by the URL of the tool.

26
00:01:31,380 --> 00:01:35,430
So we're basically using git to download or clone a repository.

27
00:01:35,430 --> 00:01:39,600
And we're giving it the link to the repository that contains this framework clone drop.

28
00:01:40,320 --> 00:01:41,730
We're going to hit enter.

29
00:01:41,940 --> 00:01:45,450
And once it's there we're going to clear the screen.

30
00:01:45,450 --> 00:01:49,620
And if we do LS we can see that we have a new directory called Point Drop.

31
00:01:49,620 --> 00:01:51,900
So this is literally what we just downloaded.

32
00:01:51,900 --> 00:01:54,840
We're going to navigate into it using the CD command.

33
00:01:55,200 --> 00:01:59,160
And we're going to do make to install the tool.

34
00:02:00,170 --> 00:02:02,390
And as you can see, make is not installed.

35
00:02:02,390 --> 00:02:06,740
So I'm actually going to have to do apt update to update my sources.

36
00:02:06,740 --> 00:02:10,460
So I'm doing this really quickly because we've done this before multiple times.

37
00:02:10,910 --> 00:02:15,500
And then I'm going to do apt install make Golang.

38
00:02:16,310 --> 00:02:22,040
So we're installing make because we need this program make in order to install the framework.

39
00:02:22,040 --> 00:02:24,890
And the framework is written in a language called go.

40
00:02:24,890 --> 00:02:26,930
And that's why we're installing it in here.

41
00:02:27,320 --> 00:02:29,990
So we're using APT to install these two packages.

42
00:02:30,290 --> 00:02:33,440
We're going to hit enter to say yes we want to download and install this.

43
00:02:33,440 --> 00:02:36,260
And I'm doing this very quickly because we've done this before.

44
00:02:36,970 --> 00:02:43,120
Now that everything is installed, I'm going to clear the screen and I'm already in the right directory

45
00:02:43,120 --> 00:02:45,370
where we downloaded or cloned pawn drop.

46
00:02:45,370 --> 00:02:51,310
So I'm just going to type make to install this tool or to prepare this tool for installation.

47
00:02:52,390 --> 00:02:58,960
And now that everything is ready, we're actually going to say make install to install it.

48
00:03:00,540 --> 00:03:01,650
And that is it.

49
00:03:01,650 --> 00:03:03,570
The tool is actually installed.

50
00:03:03,570 --> 00:03:07,350
And not only that, it's already installed, it's actually already running.

51
00:03:07,350 --> 00:03:12,750
But I'm going to show you how to run it just in case in the future you want it to stop it or run it.

52
00:03:12,750 --> 00:03:16,380
So you can see here it's telling you copied point drop executable.

53
00:03:16,380 --> 00:03:18,870
So this is a keyword to this location.

54
00:03:19,470 --> 00:03:26,370
So basically you can stop or run this tool or even debug it by running this file in this path.

55
00:03:26,670 --> 00:03:28,680
So let me just clear it.

56
00:03:28,680 --> 00:03:33,840
And if I paste this path, this is the binary that actually runs the tool.

57
00:03:33,840 --> 00:03:35,670
And if I say status.

58
00:03:37,180 --> 00:03:39,340
You'll see that it's actually running.

59
00:03:39,990 --> 00:03:45,090
So we can stop it by running the same file and saying stop.

60
00:03:45,810 --> 00:03:51,570
And we can even run it again by calling the same file and type in start.

61
00:03:52,940 --> 00:03:53,810
And that's it.

62
00:03:53,810 --> 00:04:00,320
Now you have your own file hosting service running on the cloud, so you can use it to upload any file

63
00:04:00,320 --> 00:04:03,500
you want and share it with anybody over the internet.

64
00:04:03,800 --> 00:04:05,480
Now let me show you what it looks like.

65
00:04:06,170 --> 00:04:11,030
So all we have to do is go to our domain name which we created in here.

66
00:04:11,120 --> 00:04:15,590
So my domain name is g download.io.

67
00:04:16,880 --> 00:04:21,230
And we're going to put forward slash P1 drop.

68
00:04:21,230 --> 00:04:22,820
So this is very important.

69
00:04:22,820 --> 00:04:26,180
This is where the admin panel is for point drop.

70
00:04:26,180 --> 00:04:27,560
We're going to hit enter.

71
00:04:29,020 --> 00:04:34,600
And as you can see, because we're accessing this framework for the first time, it's asking you to

72
00:04:34,600 --> 00:04:37,120
set a username and a password.

73
00:04:37,360 --> 00:04:43,480
So let's set the username here and let's say Zeus and put the password.

74
00:04:44,650 --> 00:04:48,430
And now that we set it, now we can log in with this username and password.

75
00:04:48,430 --> 00:04:52,420
So again I'm going to put my username and I'm going to put the password.

76
00:04:52,780 --> 00:04:53,470
And that's it.

77
00:04:53,470 --> 00:04:57,880
Now we have our own file hosting service installed on the cloud.

78
00:04:57,880 --> 00:05:03,070
And as I said you can use it to upload and share files with everybody on the internet.

79
00:05:03,190 --> 00:05:06,070
You can use this big upload button to upload a file.

80
00:05:06,070 --> 00:05:07,600
So let's upload something.

81
00:05:07,600 --> 00:05:12,490
And just as an example, we can just upload an executable that I have in here somewhere.

82
00:05:12,490 --> 00:05:15,520
So this one bp2 dot exe.

83
00:05:15,520 --> 00:05:18,130
It doesn't really matter if you click on upload.

84
00:05:18,130 --> 00:05:21,220
As you can see you get a nice progress bar and this is it.

85
00:05:21,220 --> 00:05:22,810
The file is uploaded now.

86
00:05:22,930 --> 00:05:27,340
So if I click on the Http in here it's going to copy the link to clipboard.

87
00:05:27,340 --> 00:05:30,100
And you can share this with anybody on the internet.

88
00:05:30,100 --> 00:05:32,230
And they'll be able to download this file.

89
00:05:32,230 --> 00:05:37,180
So just to show you I'm going to paste it here download and perfect.

90
00:05:37,180 --> 00:05:40,960
As you can see the file got downloaded and now it's stored in my downloads.

91
00:05:41,660 --> 00:05:47,870
So this is how easy it is to host your own files or malware and have them available on the cloud so

92
00:05:47,870 --> 00:05:51,170
that anybody can access them from anywhere on the internet.

93
00:05:51,410 --> 00:05:56,720
Now, as I mentioned, this framework can be used to do so much more than hosting your own files.

94
00:05:56,720 --> 00:05:59,390
And I'm going to go through the rest of the features next.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,930
So now that we have the framework installed and ready to be used and actually use it to upload one file,

2
00:00:05,930 --> 00:00:11,060
let's just have a look on the interface that we have in front of us, and use it and show you some of

3
00:00:11,060 --> 00:00:12,440
its really cool features.

4
00:00:12,440 --> 00:00:16,190
First of all, you can upload files using this big upload button.

5
00:00:16,190 --> 00:00:22,820
As we said before, you can see the amount of free space and the amount of used space right now on your

6
00:00:22,820 --> 00:00:23,180
server.

7
00:00:23,180 --> 00:00:27,770
So this is very, very useful if you're actually using this in real life and you're uploading files,

8
00:00:27,770 --> 00:00:28,880
this is very useful.

9
00:00:28,880 --> 00:00:33,920
So even if you're not using this to deliver malware, instead of signing up to Dropbox or any of that,

10
00:00:33,920 --> 00:00:35,480
you can use something like this.

11
00:00:36,050 --> 00:00:42,260
You can log out of this using this button, and you can access the general settings of the framework

12
00:00:42,260 --> 00:00:44,840
using this cog right here on the top left.

13
00:00:44,840 --> 00:00:46,070
So let's click it.

14
00:00:46,070 --> 00:00:49,580
And as you can see you get a number of options that you can modify.

15
00:00:49,610 --> 00:00:52,460
These are the global options of the framework.

16
00:00:52,460 --> 00:00:54,500
The first thing is the redirect URL.

17
00:00:54,500 --> 00:01:02,090
This is the path that the people will be redirected to if they try to access a file that does not exist.

18
00:01:02,090 --> 00:01:03,410
So you can think of it.

19
00:01:03,410 --> 00:01:06,950
This is as the 404 or the not found page.

20
00:01:06,950 --> 00:01:12,860
Right now it takes you to a YouTube video, but you should modify this to take you to an actual 404

21
00:01:12,860 --> 00:01:15,200
page so that it is less suspicious.

22
00:01:15,440 --> 00:01:17,000
The secret path in here.

23
00:01:17,000 --> 00:01:21,530
This is the path that we used in order to access the admin panel of the framework.

24
00:01:21,530 --> 00:01:26,810
So remember we put our domain name forward slash point drop to access the admin page.

25
00:01:26,810 --> 00:01:28,250
That's why we have this in here.

26
00:01:28,250 --> 00:01:30,650
So you can modify this to any value you want.

27
00:01:30,650 --> 00:01:33,200
If you want your admin page to be more hidden.

28
00:01:33,920 --> 00:01:39,680
This is the secret cookie that you need to have in order to be able to access the admin, and this is

29
00:01:39,680 --> 00:01:41,270
the value of that secret cookie.

30
00:01:41,270 --> 00:01:46,400
So again, you can modify these things if you want to increase the security of this framework.

31
00:01:46,400 --> 00:01:52,040
So the main setting that you actually will probably want to modify is the redirect URL, because we

32
00:01:52,040 --> 00:01:58,730
want the users to be redirected to an actual 404 or not found page, instead of being redirected to

33
00:01:58,730 --> 00:02:00,350
this funny YouTube video.

34
00:02:00,770 --> 00:02:04,610
So we're going to use the features offered by this framework anyway.

35
00:02:04,610 --> 00:02:08,510
So we're going to just click on the upload to upload a 404 page.

36
00:02:08,510 --> 00:02:12,140
And I already have one in here called 404.

37
00:02:12,140 --> 00:02:15,290
So it's a very simple page, nothing fancy in there.

38
00:02:15,290 --> 00:02:16,790
We're just going to upload it.

39
00:02:17,370 --> 00:02:22,980
And now that it's uploaded, instead of copying its link as is, I'm actually going to click on this

40
00:02:22,980 --> 00:02:26,760
icon in here to change this individual file settings.

41
00:02:26,760 --> 00:02:31,560
So the big settings icon in here allows you to edit the global settings.

42
00:02:31,560 --> 00:02:37,260
And this small cog icon is individual or is specific to this file.

43
00:02:37,260 --> 00:02:39,600
So as you can see each file has its own settings.

44
00:02:39,600 --> 00:02:44,640
And if I click on this one you'll see that I have more settings that I can modify in this file.

45
00:02:45,830 --> 00:02:47,150
So you can edit the name.

46
00:02:47,150 --> 00:02:49,160
This is just the name that is displayed to you.

47
00:02:49,160 --> 00:02:50,930
It's not actually the file name.

48
00:02:50,930 --> 00:02:55,190
You can edit the Mime type and we will talk about that later.

49
00:02:55,190 --> 00:02:58,100
But what I really want to edit right now is the path.

50
00:02:58,100 --> 00:03:01,010
So right now this page is uploaded in this path.

51
00:03:01,010 --> 00:03:05,870
So you'll have this random path in the URL after the download.io.

52
00:03:05,870 --> 00:03:09,020
And then you'll have the 404 dot HTML.

53
00:03:09,020 --> 00:03:10,490
And I think that doesn't look great.

54
00:03:10,490 --> 00:03:12,410
And I think it looks a little bit suspicious.

55
00:03:12,410 --> 00:03:17,540
So to modify this all I have to do is remove it from here and click on save.

56
00:03:17,990 --> 00:03:20,450
So now I have my 404 page on this path.

57
00:03:20,450 --> 00:03:26,270
And if I just copy it by clicking on Http, we're going to go to the settings in here.

58
00:03:26,270 --> 00:03:30,590
And in the redirect URL we're going to put the URL for that page.

59
00:03:30,590 --> 00:03:32,330
We don't even have to put the full URL.

60
00:03:32,330 --> 00:03:33,650
We can just do this.

61
00:03:34,690 --> 00:03:36,580
And click on save.

62
00:03:36,730 --> 00:03:41,290
And now if somebody tries to access a file that it does not exist.

63
00:03:41,290 --> 00:03:44,980
So let's just copy this file, paste it here.

64
00:03:44,980 --> 00:03:46,930
And we're just going to add more stuff to it.

65
00:03:47,600 --> 00:03:50,510
As you can see, you're going to get the 404 page.

66
00:03:51,080 --> 00:03:57,650
So the main thing that I wanted to highlight is the ability to change the link to that file the path,

67
00:03:57,650 --> 00:04:03,110
by simply clicking the settings in here and then editing the value in the path in here.

68
00:04:04,110 --> 00:04:08,340
Each file also has a number of other icons, as you can see in here.

69
00:04:08,340 --> 00:04:12,240
So this one allows you to edit the individual settings of the file.

70
00:04:12,240 --> 00:04:18,480
As we mentioned earlier, this icon right here makes the file available or unavailable.

71
00:04:18,480 --> 00:04:21,030
So right now as you can see it's enabled.

72
00:04:21,030 --> 00:04:25,020
But if I click on it now it makes the file disabled.

73
00:04:25,020 --> 00:04:27,030
So it makes the file unavailable.

74
00:04:27,030 --> 00:04:29,430
So if I go and try to load the file.

75
00:04:30,310 --> 00:04:33,280
As you can see, it says that that file does not exist.

76
00:04:34,080 --> 00:04:42,450
Now this is very useful in order to avoid being flagged as suspicious and avoid crawlers so that you

77
00:04:42,450 --> 00:04:48,390
can make you can upload your backdoors or malware, make them unavailable, and only make them available

78
00:04:48,390 --> 00:04:54,150
when you start the engagement, or when you actually start trying to communicate with the target and

79
00:04:54,150 --> 00:04:56,070
try to get them to download your malware.

80
00:04:57,910 --> 00:05:02,860
Now if I click it again and load the file.

81
00:05:03,560 --> 00:05:05,690
As you can see, it works as expected.

82
00:05:05,690 --> 00:05:07,490
We got the file downloaded in here.

83
00:05:08,240 --> 00:05:13,190
Now, obviously you can also just delete the file by clicking on the X in here, which is very, very

84
00:05:13,190 --> 00:05:14,930
handy and very easy to do.

85
00:05:15,770 --> 00:05:22,550
And another really cool feature is instead of disabling the file by clicking on this button so that

86
00:05:22,550 --> 00:05:25,070
when you load it, nothing this gets displayed.

87
00:05:25,070 --> 00:05:27,710
You can actually set up a facade file.

88
00:05:27,710 --> 00:05:34,430
So when that feature is enabled, the link will serve another file that you choose.

89
00:05:34,430 --> 00:05:36,680
And this file is usually a nice file.

90
00:05:36,680 --> 00:05:37,550
It's not malware.

91
00:05:37,550 --> 00:05:41,330
It's a nice clean file that displays something that the user expects.

92
00:05:41,330 --> 00:05:47,510
And then again, when you want to start your engagement, you can toggle the malicious file again.

93
00:05:47,510 --> 00:05:54,740
That way you'll be able to bypass crawlers, and your website will be less likely to be flagged as suspicious

94
00:05:54,740 --> 00:05:56,360
or as malware.

95
00:05:56,630 --> 00:06:00,200
So to set this up, we're going to click on the settings.

96
00:06:00,200 --> 00:06:05,060
And as you can see you have an option in here to set a facade file.

97
00:06:05,060 --> 00:06:08,720
So if I upload something in here I click on the button.

98
00:06:08,720 --> 00:06:11,930
And let's just upload this logo for -- Drop.

99
00:06:11,930 --> 00:06:14,210
And we're going to click on open.

100
00:06:15,390 --> 00:06:18,900
And as you can see now, the facade file is set in here.

101
00:06:18,900 --> 00:06:22,560
And the type of the file is still set to an application.

102
00:06:22,560 --> 00:06:25,020
So this is the Mime type.

103
00:06:25,020 --> 00:06:31,920
The value of the Mime type is used by the browser to decide what to do with the file.

104
00:06:31,920 --> 00:06:36,900
So for example, if this value said this is an image, the browser will try to open that image.

105
00:06:36,900 --> 00:06:42,630
If it says that this is an executable, as you can see in here, the browser will simply just download

106
00:06:42,630 --> 00:06:42,900
it.

107
00:06:42,900 --> 00:06:47,220
So now, because we uploaded an image, we're actually going to have to modify this.

108
00:06:47,850 --> 00:06:54,360
So if we just click here on the Mime types, it's actually going to list all of the possible Mime types.

109
00:06:54,360 --> 00:06:56,490
And we uploaded a PNG image.

110
00:06:56,490 --> 00:06:58,140
So I'm just going to look for PNG.

111
00:06:58,740 --> 00:07:01,320
And as you can see we have the value in here.

112
00:07:01,320 --> 00:07:03,060
So I'm just going to copy it.

113
00:07:04,140 --> 00:07:06,540
And we're going to paste it in here.

114
00:07:06,930 --> 00:07:11,130
So now the facade file is a picture that I just uploaded.

115
00:07:11,130 --> 00:07:13,020
And we set its type to an image.

116
00:07:13,020 --> 00:07:22,770
And when I save it and click on this icon in here to enable the facade file, if you try to go to the

117
00:07:22,770 --> 00:07:24,660
link to this backdoor.

118
00:07:26,100 --> 00:07:27,660
You'll actually get an image.

119
00:07:27,690 --> 00:07:34,830
So again you can enable this like this to avoid being flagged as malicious and to avoid crawlers.

120
00:07:34,830 --> 00:07:39,540
And then when you start your engagement, when you communicate with your target, all you have to do

121
00:07:39,540 --> 00:07:43,200
is come back in here, click on this button to enable the real file.

122
00:07:43,200 --> 00:07:49,200
And then if you download this, if you access the exact same link, the file will be downloaded directly.

123
00:07:49,960 --> 00:07:55,300
So this feature could be more useful than simply clicking on the toggle in here to toggle it on and

124
00:07:55,330 --> 00:07:55,900
off.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,110 --> 00:00:05,240
Now I want to show you the coolest feature that we showed at the start of all of this, which allows

2
00:00:05,240 --> 00:00:10,400
you to either hide or change the extension of files.

3
00:00:10,400 --> 00:00:15,680
So what I want to show you today, instead of having the X here at the end of the file name, you can

4
00:00:15,680 --> 00:00:18,200
actually serve the URL like so.

5
00:00:18,500 --> 00:00:23,420
Not only that, but you can even disguise or change the extension.

6
00:00:23,420 --> 00:00:30,020
So instead of X, if you have a Trojan that for example loads an image or loads a PDF book, you can

7
00:00:30,020 --> 00:00:31,790
actually have the link look like this.

8
00:00:31,790 --> 00:00:37,490
So the link would be dot pdf or dot png or dot any extension you want.

9
00:00:37,490 --> 00:00:41,360
But when the user loads it, it will actually download an executable.

10
00:00:42,220 --> 00:00:47,230
So we're going to, first of all upload a file that is normal, that does not contain any malware.

11
00:00:47,230 --> 00:00:49,210
So we're going to click on upload.

12
00:00:49,210 --> 00:00:51,520
And I'm going to upload a normal e-book.

13
00:00:51,550 --> 00:00:53,200
A normal PDF right here.

14
00:00:53,200 --> 00:00:54,610
Just a Chrome manual.

15
00:00:54,610 --> 00:00:56,290
We're going to click on open.

16
00:00:56,840 --> 00:01:02,300
And once this is uploaded, as you can see, if we just copy this and access it in here, it's going

17
00:01:02,300 --> 00:01:03,830
to load the PDF for us.

18
00:01:03,830 --> 00:01:04,550
Perfect.

19
00:01:05,150 --> 00:01:10,010
Now what I'm going to do, I'm going to copy the link to the back door that we want to serve.

20
00:01:10,010 --> 00:01:14,480
And then I'm going to access the settings of the normal clean file.

21
00:01:15,080 --> 00:01:17,480
And we're going to set the redirect path.

22
00:01:17,480 --> 00:01:22,070
And in here we're simply going to put the URL for our backdoor.

23
00:01:22,520 --> 00:01:27,860
So what's going to happen now is once somebody tries to access this file the manual dot PDF.

24
00:01:27,860 --> 00:01:34,190
And instead of getting the manual PDF, they will be redirected to the backdoor that we are specifying

25
00:01:34,190 --> 00:01:34,910
in here.

26
00:01:35,060 --> 00:01:38,720
And that's what I actually showed you at the start of all of this.

27
00:01:38,720 --> 00:01:44,090
And I'm actually just going to change the path in here so that it's just forward slash manual dot PDF

28
00:01:44,090 --> 00:01:45,380
so it looks better.

29
00:01:45,680 --> 00:01:48,770
We're going to save I'm going to copy this link.

30
00:01:48,770 --> 00:01:51,230
And I'm going to open it in a new tab.

31
00:01:51,290 --> 00:01:55,520
And now as you can see I have a nice domain name.

32
00:01:55,520 --> 00:01:58,460
And we have a nice file name manual dot pdf.

33
00:01:58,460 --> 00:02:00,590
So it's not suspicious at all.

34
00:02:00,590 --> 00:02:05,300
But if we download we're actually going to end up downloading the backdoor.

35
00:02:05,300 --> 00:02:09,680
And as I showed you earlier, if this backdoor right here is a Trojan.

36
00:02:09,680 --> 00:02:12,830
So right now I'm simply just downloading a bad backdoor.

37
00:02:12,830 --> 00:02:19,340
But if this is a proper Trojan that looks and behaves like a PDF, as I showed you earlier, most users

38
00:02:19,340 --> 00:02:25,250
will actually believe that this is a normal PDF and will actually execute the file, especially that

39
00:02:25,250 --> 00:02:30,320
windows by default doesn't even show the file extension, so you won't even need to bypass the file

40
00:02:30,320 --> 00:02:33,800
extension once it's downloaded on the target computer.

41
00:02:34,540 --> 00:02:40,570
So as you can see, it's very, very useful in many cases because you're basically given a link that

42
00:02:40,570 --> 00:02:43,180
has a normal extension and you can put any extension in there.

43
00:02:43,180 --> 00:02:49,660
You can put PNG, you can put dot X, you can put any extension that the target person would be interested

44
00:02:49,660 --> 00:02:50,080
in.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,140 --> 00:00:05,450
So now that we know how to use this tool and seeing how useful it is, there is only one more thing

2
00:00:05,450 --> 00:00:12,950
that we can do to make this tool even more useful and even less suspicious, and that is to enable Https

3
00:00:12,950 --> 00:00:13,310
on it.

4
00:00:13,310 --> 00:00:19,610
Because as you can see right now, it's not loading using Https, it's loading using normal Http.

5
00:00:19,850 --> 00:00:23,510
And as you can see, you're getting the not secure icon in here.

6
00:00:23,510 --> 00:00:31,310
And again, lots of crawlers and browsers might flag it as unsafe simply because it doesn't have Https.

7
00:00:31,970 --> 00:00:35,660
So in order to do this we're actually going to use Certbot.

8
00:00:35,660 --> 00:00:37,250
So we covered that before.

9
00:00:37,250 --> 00:00:41,450
But we're going to have to manually install the certificate unlike what we showed before.

10
00:00:41,450 --> 00:00:43,100
So let me show you how to do that.

11
00:00:43,760 --> 00:00:45,560
We're going to go back to our Kali machine.

12
00:00:45,560 --> 00:00:48,470
And we're going to first of all stop port Drop.

13
00:00:48,470 --> 00:00:50,030
So I'm just going to say stop.

14
00:00:50,540 --> 00:00:56,300
I'm going to clear the screen and I'm going to use APT to install Certbot.

15
00:00:56,890 --> 00:01:02,170
So this is the program that we use to generate Https or SSL certificates.

16
00:01:03,130 --> 00:01:05,020
So Certbot is installed.

17
00:01:05,020 --> 00:01:09,370
Now we're going to clear the screen and we're going to use it by typing Certbot.

18
00:01:09,580 --> 00:01:14,410
We're going to say we want to create a certificate only.

19
00:01:14,410 --> 00:01:19,330
So previously we got Certbot to automatically install its certificate on Apache.

20
00:01:19,330 --> 00:01:24,970
But right now Certbot cannot automatically install the certificate on port drop.

21
00:01:24,970 --> 00:01:26,320
So we're going to have to do it manually.

22
00:01:26,320 --> 00:01:30,970
And that's why we're saying we want the certificate only and we will install it ourselves.

23
00:01:31,120 --> 00:01:34,870
We're going to have to give it the domain that we want the certificate for.

24
00:01:34,870 --> 00:01:40,270
And my domain is called g download.io.

25
00:01:40,270 --> 00:01:45,370
And we're going to say we want you to try the stand alone method.

26
00:01:45,370 --> 00:01:52,720
So it's going to start its own server in order to authenticate us and verify that we actually own this

27
00:01:52,720 --> 00:01:56,500
domain name so that it can issue an SSL certificate for us.

28
00:01:57,310 --> 00:01:58,600
So we're using Certbot.

29
00:01:58,630 --> 00:01:59,890
That's the name of the program.

30
00:01:59,890 --> 00:02:00,520
We're telling it.

31
00:02:00,520 --> 00:02:01,990
We want the certificate only.

32
00:02:01,990 --> 00:02:04,090
We will manually install it ourselves.

33
00:02:04,090 --> 00:02:08,650
We're giving it the domain name that we want the certificate for using the D option.

34
00:02:08,650 --> 00:02:15,100
And we're telling it we want you to verify my ownership to this domain using the stand alone method.

35
00:02:15,100 --> 00:02:19,900
So by creating or starting your own server on my current server.

36
00:02:20,500 --> 00:02:21,850
So I'm going to hit enter.

37
00:02:23,190 --> 00:02:26,790
And the first thing that it's doing is it's asking us for an email address.

38
00:02:26,790 --> 00:02:31,740
You should put a valid email address in here because it's going to email you whenever renewals are needed.

39
00:02:31,740 --> 00:02:35,760
And if things fail, I'm just going to put an email address that doesn't work.

40
00:02:35,760 --> 00:02:39,090
But that's fine for the purposes of this lecture.

41
00:02:39,090 --> 00:02:44,730
So we're just going to do info ATG download.io.

42
00:02:46,290 --> 00:02:50,790
It's asking us if we agree to the terms, we're going to say, yes, we do agree.

43
00:02:51,090 --> 00:02:55,650
And it's asking us if we want to get updates and notifications.

44
00:02:55,650 --> 00:02:57,000
We're going to say no.

45
00:02:57,000 --> 00:03:02,850
And now it's going to go ahead, request the certificate for us and try to verify our ownership to that

46
00:03:02,850 --> 00:03:03,480
domain.

47
00:03:04,570 --> 00:03:08,800
And as you can see, this was pretty quick and we already got the certificate.

48
00:03:08,800 --> 00:03:14,830
So you can say it's successfully received the certificates and it's given us the locations of my certificate.

49
00:03:14,830 --> 00:03:18,910
So we have the full chain file that contains all of the information.

50
00:03:18,910 --> 00:03:23,920
And we have the private key stored in the private key file in this path.

51
00:03:24,160 --> 00:03:30,160
So both of these files are actually needed in order to enable https on Pindrop.

52
00:03:30,160 --> 00:03:36,730
All we have to do is simply copy them and put them in the right path, which is in usr local pindrop

53
00:03:36,730 --> 00:03:37,450
data.

54
00:03:37,450 --> 00:03:40,510
So we're going to use the CPP command to do that.

55
00:03:40,510 --> 00:03:44,500
And I'm just going to copy this first path in here the full chain path.

56
00:03:45,850 --> 00:03:52,510
And I'm going to say I'm going to use the CP command to copy this file to the path where Point Drop

57
00:03:52,510 --> 00:03:54,100
wants this file to be.

58
00:03:54,100 --> 00:03:59,140
And like I said, that path is in usr local point drop data.

59
00:04:00,300 --> 00:04:01,590
I'm going to hit enter.

60
00:04:02,290 --> 00:04:03,520
And that is done.

61
00:04:03,520 --> 00:04:07,150
We're going to have to do the same for the second file, this one.

62
00:04:07,920 --> 00:04:09,510
So this is the private key.

63
00:04:09,510 --> 00:04:11,340
So again I'm going to copy it.

64
00:04:11,340 --> 00:04:15,330
And I'm going to use the CP command to copy it to the same path.

65
00:04:15,330 --> 00:04:22,050
So it was usr local point drop data I'm going to hit enter.

66
00:04:22,050 --> 00:04:23,430
And that should have worked.

67
00:04:23,430 --> 00:04:26,250
So I'm actually just going to clear the screen.

68
00:04:27,110 --> 00:04:29,060
And I'm going to navigate to that path.

69
00:04:29,060 --> 00:04:34,970
So it's again user local phone drop data.

70
00:04:34,970 --> 00:04:37,520
We're going to use the LS command to list the files.

71
00:04:37,520 --> 00:04:41,120
And as you can see we have the full chain and the private key in here.

72
00:04:41,300 --> 00:04:44,150
Now again this should work in most cases.

73
00:04:44,150 --> 00:04:48,470
But Point Drop expects these files to be named something else.

74
00:04:48,470 --> 00:04:54,170
So it wants the full chain dot PEM file to be called public dot CRT.

75
00:04:54,170 --> 00:04:58,640
And it wants the private key to be called private key.

76
00:04:58,670 --> 00:05:00,920
Now I knew this from analyzing their code.

77
00:05:00,920 --> 00:05:06,230
Unfortunately they didn't include it in their documentation, but I do think that they will eventually

78
00:05:06,230 --> 00:05:08,000
update it and include it in there.

79
00:05:08,870 --> 00:05:12,200
So to change your file name in Linux, we use the MV command.

80
00:05:12,200 --> 00:05:19,100
So we want to change the file name of the full chain file to public dot CRT.

81
00:05:20,420 --> 00:05:26,240
And we want to change the name of the private key file to private Key.

82
00:05:27,440 --> 00:05:32,030
So now that everything is set properly, we're going to go ahead and run Point drop.

83
00:05:32,030 --> 00:05:38,540
But this time, instead of just putting the path to the binary and saying start, we're actually just

84
00:05:38,540 --> 00:05:40,550
going to do dash debug.

85
00:05:40,550 --> 00:05:47,000
So this way it'll actually tell you if it faced any issues while it's starting and while it's enabling

86
00:05:47,000 --> 00:05:48,170
Https.

87
00:05:48,560 --> 00:05:49,790
So I'm going to hit enter.

88
00:05:49,790 --> 00:05:54,770
And as you can see this time we're getting so much more output than what we were getting before.

89
00:05:54,770 --> 00:06:00,860
And because we don't see any errors and we don't see any warnings, we know that the program or the

90
00:06:00,860 --> 00:06:03,410
framework is probably working as expected.

91
00:06:04,070 --> 00:06:06,590
So let's go ahead and test it with Https.

92
00:06:06,590 --> 00:06:08,780
So I'm just going to copy this link.

93
00:06:08,930 --> 00:06:10,100
Paste it here.

94
00:06:10,100 --> 00:06:11,990
Load it over https.

95
00:06:11,990 --> 00:06:13,010
Hit enter.

96
00:06:13,950 --> 00:06:14,790
And perfect.

97
00:06:14,790 --> 00:06:16,710
I can already see the lock icon.

98
00:06:16,710 --> 00:06:19,110
So now any link you copy from here?

99
00:06:19,110 --> 00:06:21,900
If you just click it and load it in here.

100
00:06:21,900 --> 00:06:29,850
As you can see the link is going to be loaded over Https, therefore increasing user trust and increasing

101
00:06:29,850 --> 00:06:30,780
crawlers trust.

102
00:06:30,780 --> 00:06:37,320
So again crawlers and search engines are going to be less likely to flag you as malicious or as spam,

103
00:06:37,320 --> 00:06:44,520
because now you are using your own proper certificate and your serving files and everything is loading

104
00:06:44,520 --> 00:06:46,110
over Https.

105
00:06:46,110 --> 00:06:52,440
And like I said, these features the features of disabling of the files and displaying a facade file

106
00:06:52,440 --> 00:06:59,190
can really, really help with avoiding crawlers and avoiding being marked as spam or as malicious.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


1
00:00:00,140 --> 00:00:07,220
In the previous lectures, we saw how useful point drop can be to host our own files, backdoors and

2
00:00:07,220 --> 00:00:13,730
trojans, and creating convincing links that will increase the chances of our targets downloading and

3
00:00:13,730 --> 00:00:15,560
executing our malware.

4
00:00:15,590 --> 00:00:23,150
However, you still might face one major problem what if we don't know the operating system of the target?

5
00:00:23,150 --> 00:00:28,670
What if you are targeting a large organization through a phishing campaign, and you want your malware

6
00:00:28,670 --> 00:00:32,240
to work on any computer that clicks the download link?

7
00:00:32,720 --> 00:00:36,020
We know that our malware is OS specific.

8
00:00:36,020 --> 00:00:37,550
It's not cross-platform.

9
00:00:37,550 --> 00:00:42,080
This means that it will only run on one specific operating system.

10
00:00:42,080 --> 00:00:45,770
So the Windows Backdoors or Windows malware will only run on windows.

11
00:00:45,770 --> 00:00:51,830
Linux will only run on Linux and Apple Mac OS backdoors will only run on Apple computers.

12
00:00:51,830 --> 00:00:59,840
Therefore, the best solution to this problem is to create a link that is cross-platform that will serve

13
00:00:59,840 --> 00:01:07,730
the correct executable based on the operating system of the computer that is loading the download page.

14
00:01:07,730 --> 00:01:12,410
And doing this is actually very, very simple and I'm going to walk you through it step by step.

15
00:01:12,500 --> 00:01:18,830
But before we go ahead and do it, let's just organize our ideas and see how we can actually go ahead

16
00:01:18,830 --> 00:01:20,810
and create this in real life.

17
00:01:20,810 --> 00:01:25,670
Basically a fancy name for organizing our ideas like this is an algorithm.

18
00:01:25,670 --> 00:01:27,080
So let's come up with one.

19
00:01:27,080 --> 00:01:28,820
First of all, let's talk about the goal.

20
00:01:28,820 --> 00:01:35,030
The goal is to serve an executable compatible with the operating system of the computer that is loading

21
00:01:35,030 --> 00:01:35,960
that page.

22
00:01:35,960 --> 00:01:41,000
So first of all we're going to need to create different versions of this executable, whether it's a

23
00:01:41,000 --> 00:01:45,800
backdoor or a keylogger or any type of malware, you want to create three versions of it, or even maybe

24
00:01:45,800 --> 00:01:46,100
more.

25
00:01:46,100 --> 00:01:51,020
So we're going to create one for windows, one for Apple Mac OS and one for Linux.

26
00:01:51,080 --> 00:01:54,590
Once you have that, we're going to go ahead and create our page.

27
00:01:54,590 --> 00:02:00,500
And in this page we're going to have to find the operating system of the computer or the client that

28
00:02:00,500 --> 00:02:01,730
is loading this page.

29
00:02:01,730 --> 00:02:03,650
And this is going to be very, very easy.

30
00:02:03,650 --> 00:02:07,250
We're going to rely on the user agent, which we talked about previously.

31
00:02:07,250 --> 00:02:08,990
But just a quick recap.

32
00:02:08,990 --> 00:02:14,450
Every browser sends its user agent basically its version and the operating system that it's running

33
00:02:14,450 --> 00:02:16,460
on whenever it loads a page.

34
00:02:16,460 --> 00:02:18,470
So we can read this in our page.

35
00:02:18,470 --> 00:02:24,890
And based on that, we're going to use a conditional or an if statement to serve the correct executable

36
00:02:24,890 --> 00:02:26,990
that we created in step one.

37
00:02:26,990 --> 00:02:32,600
So it's very, very simple and it's going to become even clearer once I show you how to do it in this

38
00:02:32,600 --> 00:02:33,260
lecture.

39
00:02:33,770 --> 00:02:37,670
So step one you want to create different versions of the executable.

40
00:02:37,670 --> 00:02:42,650
We covered how to create a Trojan for windows, and I actually even cover how to create Trojans for

41
00:02:42,650 --> 00:02:47,450
all of these operating systems for Linux and Apple Mac OS in my social engineering course.

42
00:02:47,450 --> 00:02:49,220
But it's not really part of this course.

43
00:02:49,220 --> 00:02:50,270
That's why I didn't cover it.

44
00:02:50,270 --> 00:02:56,090
I only focused on windows because that really dives into social engineering and has nothing to do with

45
00:02:56,090 --> 00:02:57,530
hacking using the cloud.

46
00:02:57,530 --> 00:03:02,210
So for this lecture, I basically just uploaded three different files.

47
00:03:02,210 --> 00:03:08,090
They're not actually even backdoors, but just for the sake of demonstration, I call them Apple Mac

48
00:03:08,090 --> 00:03:11,360
OS backdoor, Linux backdoor and windows backdoor.

49
00:03:11,750 --> 00:03:13,760
So I have them already uploaded in here.

50
00:03:13,760 --> 00:03:16,520
And that basically means step one is done.

51
00:03:17,210 --> 00:03:18,980
So moving on to step two.

52
00:03:19,010 --> 00:03:24,680
We need to find a way to read the user agent of the web browser that is loading the page.

53
00:03:24,680 --> 00:03:30,410
So as you've seen earlier, you'll easily find this by looking through Google how to find the user agent

54
00:03:30,410 --> 00:03:31,340
using JavaScript.

55
00:03:31,340 --> 00:03:34,820
Or even if you say using HTML, it will show it to you or even PHP.

56
00:03:35,000 --> 00:03:41,090
But we're actually going to go ahead to ChatGPT this time and use it to get the code.

57
00:03:41,090 --> 00:03:47,330
If you've never used this, all you have to do is simply go to ChatGPT Openai.com, log in with your

58
00:03:47,330 --> 00:03:49,580
Google account or any other account that you have.

59
00:03:49,580 --> 00:03:54,620
And basically the way this works is you can ask any question you want in here, and it usually gives

60
00:03:54,620 --> 00:03:59,300
you a really good answer, especially if you're asking a simple question like what we're going to do

61
00:03:59,300 --> 00:03:59,990
right now.

62
00:04:00,440 --> 00:04:04,490
So we're basically just going to tell it what we want to do, what we want to achieve.

63
00:04:04,490 --> 00:04:12,560
And we basically want a HTML page that can identify the operating system of the visitor and based on

64
00:04:12,560 --> 00:04:18,140
that, redirect them to a different link to allow them to download the right version of the software

65
00:04:18,140 --> 00:04:19,850
for their operating system.

66
00:04:19,850 --> 00:04:21,020
Simple as that.

67
00:04:21,410 --> 00:04:26,030
Hit enter, and as you can see straight away, it's going to start typing the code for you.

68
00:04:26,030 --> 00:04:31,670
And like I said, because this is a very simple code, it's going to run right out of the box.

69
00:04:31,670 --> 00:04:34,730
And not only that, it gave us the code in here.

70
00:04:34,730 --> 00:04:41,210
It's also explaining to you how this code works, explaining every single function and what you need

71
00:04:41,210 --> 00:04:42,920
to replace within the links.

72
00:04:42,920 --> 00:04:44,960
So let's first of all copy it.

73
00:04:45,830 --> 00:04:48,200
And paste it in a text editor.

74
00:04:49,670 --> 00:04:52,520
And then let's talk about how it's going to work.

75
00:04:52,550 --> 00:04:56,330
So basically here we have the basic structure of a HTML page.

76
00:04:56,330 --> 00:04:57,590
We don't really care about that.

77
00:04:57,590 --> 00:04:59,840
You have the title in here if you want to change it.

78
00:04:59,840 --> 00:05:03,290
And then in the body you have the bulk of the code.

79
00:05:03,290 --> 00:05:08,210
It's written in JavaScript, which is perfect because we can basically upload this code and have it

80
00:05:08,210 --> 00:05:11,360
run without the need to install any extra packages.

81
00:05:11,360 --> 00:05:16,250
And you can see in here we have the function that's going to determine the operating system based on

82
00:05:16,250 --> 00:05:17,120
the user agent.

83
00:05:17,120 --> 00:05:23,150
So first of all it's reading the user agent value based on this JavaScript function right here.

84
00:05:23,270 --> 00:05:28,670
And then based on the value in here, it's checking if that value contains the word windows.

85
00:05:28,670 --> 00:05:30,800
Then we're going to have the windows link in here.

86
00:05:30,800 --> 00:05:35,360
If it contains the word Macintosh it's going to serve the Mac OS link in here.

87
00:05:35,360 --> 00:05:39,710
And if it has the word Linux it's going to serve the Linux download link in here.

88
00:05:40,280 --> 00:05:45,470
So all we have to do right now is replace these links with the links for the malware that we created

89
00:05:45,470 --> 00:05:47,060
for these operating systems.

90
00:05:47,930 --> 00:05:49,970
So let's go back to Pound Drop.

91
00:05:50,510 --> 00:05:57,260
And we're going to copy the windows download link and paste it in the right location in here.

92
00:05:57,590 --> 00:06:02,570
Next, we'll copy the Apple macOS link and paste it in here.

93
00:06:02,690 --> 00:06:05,600
And finally we're going to copy the Linux link.

94
00:06:06,790 --> 00:06:08,680
And paste it in here.

95
00:06:10,590 --> 00:06:11,040
Now.

96
00:06:11,040 --> 00:06:13,650
It also included a final condition in here.

97
00:06:13,650 --> 00:06:19,140
If none of these conditions are satisfied, it's going to redirect the user to a page that's going to

98
00:06:19,140 --> 00:06:20,880
have a generic download link.

99
00:06:20,880 --> 00:06:26,400
So in this page you could have an error message, or you can have another phishing page that maybe will

100
00:06:26,400 --> 00:06:27,720
phish username and password.

101
00:06:27,720 --> 00:06:29,310
You can get creative with this.

102
00:06:29,310 --> 00:06:30,840
I'm going to leave this one empty.

103
00:06:30,840 --> 00:06:33,630
And based on that we're simply going to control S.

104
00:06:33,630 --> 00:06:36,660
To save this I'm going to save it in my downloads.

105
00:06:36,660 --> 00:06:40,140
And let's just call it download dot HTML.

106
00:06:40,140 --> 00:06:40,920
That's perfect.

107
00:06:40,920 --> 00:06:41,940
It's meaningful.

108
00:06:43,090 --> 00:06:48,160
And then we're going to go to Pawn Drop and upload this new download file.

109
00:06:49,480 --> 00:06:50,890
We have it right here.

110
00:06:50,920 --> 00:06:52,120
Can I click open?

111
00:06:52,830 --> 00:06:53,730
And that's perfect.

112
00:06:53,730 --> 00:06:55,470
That's uploaded in here.

113
00:06:55,470 --> 00:07:00,000
So we can copy this link and let's go ahead and load it from this computer.

114
00:07:00,000 --> 00:07:02,220
So this is an Apple Mac OS computer.

115
00:07:02,220 --> 00:07:07,590
And because of that I should be served the Apple Mac OS backdoor.

116
00:07:07,620 --> 00:07:08,400
Hit enter.

117
00:07:09,570 --> 00:07:15,720
And as you can see automatically, the download page has determined what operating system we're running.

118
00:07:15,720 --> 00:07:19,140
And based on that, it's serving us the correct backdoor.

119
00:07:19,710 --> 00:07:25,920
So let's go ahead to windows computer, load this link and see if it's going to determine the operating

120
00:07:25,920 --> 00:07:28,620
system and serve us the correct executable.

121
00:07:28,620 --> 00:07:33,660
So I have my browser already running here and I'm simply going to paste the download link.

122
00:07:33,660 --> 00:07:34,710
Hit enter.

123
00:07:36,570 --> 00:07:37,380
And perfect.

124
00:07:37,380 --> 00:07:43,080
As you can see, the file is already being downloaded, but I am downloading the windows version on

125
00:07:43,080 --> 00:07:44,070
the windows computer.

126
00:07:44,070 --> 00:07:49,290
So it automatically detected that I'm running windows and therefore served me the windows backdoor or

127
00:07:49,290 --> 00:07:49,920
malware.

128
00:07:50,490 --> 00:07:52,950
Now let's go ahead to a Linux computer right here.

129
00:07:52,950 --> 00:07:55,110
Again, I already have my browser running.

130
00:07:55,110 --> 00:07:57,480
I'm simply going to paste the download link.

131
00:07:57,480 --> 00:07:58,440
Hit enter.

132
00:07:59,710 --> 00:08:01,150
And perfect again.

133
00:08:01,150 --> 00:08:07,300
As you can see, it automatically detected my operating system and based on that, it is serving me

134
00:08:07,300 --> 00:08:10,450
the Linux malware or the Linux backdoor.

135
00:08:11,370 --> 00:08:16,920
So right now we have one download link that we created that we have right here.

136
00:08:16,920 --> 00:08:18,510
It's using Https.

137
00:08:18,510 --> 00:08:21,600
It's using a nice domain name like we seen before.

138
00:08:21,600 --> 00:08:24,240
And you can use this to share it with your target.

139
00:08:24,240 --> 00:08:27,630
And you don't have to worry about the operating system of the target.

140
00:08:27,630 --> 00:08:30,660
And you can share it in big phishing campaigns, like I said.

141
00:08:30,660 --> 00:08:36,840
And you don't have to worry that different operating systems might be loading this link or this URL,

142
00:08:36,870 --> 00:08:42,690
because the download link will automatically detect the operating system that they are running, and

143
00:08:42,690 --> 00:08:46,290
based on that, it will serve them the correct executable.

144
00:08:46,290 --> 00:08:52,440
And keep in mind, the code that we got from here was nicely generated using ChatGPT in here.

145
00:08:52,440 --> 00:08:58,440
So in the future, even if you have ideas that you don't know how to implement, you can simply look

146
00:08:58,440 --> 00:09:00,420
them up in Google as we saw before.

147
00:09:00,420 --> 00:09:03,150
Or you can come to ChatGPT and have a chat with it.

148
00:09:03,150 --> 00:09:08,700
And as you can see, not only that is going to give you the code, but it will also explain to you how

149
00:09:08,700 --> 00:09:10,440
this code works in details.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================


