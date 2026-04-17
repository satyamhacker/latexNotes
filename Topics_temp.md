section 1--introduction

1
00:00:00,080 --> 00:00:05,920
Welcome to my course AI driven Test Automation for playwright and Selenium using local large language

2
00:00:05,920 --> 00:00:08,440
model with Ola and cloud models.

3
00:00:09,080 --> 00:00:13,600
So what exactly is this course and what do we learn in this course?

4
00:00:13,800 --> 00:00:19,360
Well, this course help you understand how to effectively use artificial intelligence and automated

5
00:00:19,400 --> 00:00:22,560
testing together to leverage the best of both worlds.

6
00:00:23,360 --> 00:00:28,920
And this course teaches you how to maintain the control over artificial intelligence in your code,

7
00:00:28,960 --> 00:00:32,720
rather than letting the vibe coding tool to take charge of it.

8
00:00:32,760 --> 00:00:38,240
We know that there are many vibe coding tools available these days, like GitHub, Copilot, Cloud Code,

9
00:00:38,280 --> 00:00:44,560
and also there are many tools available like MCP servers of playwright as well as the Chrome dev tool

10
00:00:44,600 --> 00:00:45,160
MCP.

11
00:00:45,480 --> 00:00:52,320
These tools will let you do the code generation as well as do the code execution on behalf of you.

12
00:00:52,320 --> 00:00:57,720
But these tools are taking way more of our controls and changing our code in such a way that we can't

13
00:00:57,720 --> 00:01:00,640
really understand what's really going on behind the scene.

14
00:01:00,800 --> 00:01:08,000
And that's why this code will let you to take control of your code and you can be in control while you

15
00:01:08,000 --> 00:01:10,080
work with the artificial intelligence there.

16
00:01:10,320 --> 00:01:15,480
And for all of these operations happen, you don't need any fancy tool to enhance your existing.

17
00:01:15,520 --> 00:01:21,240
Test code with just a few code changes, your current code will already be an AI powered tool.

18
00:01:21,280 --> 00:01:23,800
That is the real crux of this particular course.

19
00:01:24,440 --> 00:01:27,160
And because we have seen what this course is.

20
00:01:27,200 --> 00:01:32,400
And what this course is for, we also need to understand what this course is not for as well.

21
00:01:32,440 --> 00:01:38,240
Well, if you are wanting to learn playwright and Selenium Basic along with the AI testing, then this

22
00:01:38,240 --> 00:01:42,880
course is unfortunately not for you because we are not going to learn anything.

23
00:01:42,880 --> 00:01:48,400
Basics or the foundation elements of playwright, like how the elements need to be found and how to

24
00:01:48,440 --> 00:01:52,320
perform an operation, how to open a browser, and how to do the assertions.

25
00:01:52,320 --> 00:01:55,280
Those are the things that will not be discussed in this particular course.

26
00:01:55,280 --> 00:02:00,760
And the same thing goes for selenium as well, because this course is going to focus fully on how we

27
00:02:00,760 --> 00:02:07,280
can enhance our existing test like playwright as well as selenium with the power of AI and make the

28
00:02:07,280 --> 00:02:08,960
test more smarter.

29
00:02:08,960 --> 00:02:13,870
And if you really wanted to learn the basics of Selenium and playwright, you can head over to my Udemy

30
00:02:13,870 --> 00:02:19,510
courses where I have talked about selenium with C-sharp dotnet basic for complete beginners, and also

31
00:02:19,550 --> 00:02:24,470
I have talked about how you can do the framework development of the playwright in C-sharp dotnet in

32
00:02:24,470 --> 00:02:25,110
this course.

33
00:02:25,310 --> 00:02:30,070
And also, if you want focusing on building your complete framework for enterprise grade, you can also

34
00:02:30,350 --> 00:02:34,790
go and look for this course in selenium which is going to talk about those details.

35
00:02:34,870 --> 00:02:37,550
So these courses are exclusively built for that.

36
00:02:37,550 --> 00:02:43,470
And this course that we're talking about is not going to be for playwright and selenium with framework

37
00:02:43,470 --> 00:02:44,550
development kind of things.

38
00:02:44,550 --> 00:02:46,590
Because that's not this course is for.

39
00:02:46,870 --> 00:02:52,230
Well as I said, what do I mean by the AI powered test to existing code?

40
00:02:52,230 --> 00:02:54,270
And how do this course really help?

41
00:02:54,270 --> 00:03:00,190
If you are puzzled about this, then let's see some of the use cases for the AI driven testing, which

42
00:03:00,190 --> 00:03:03,190
will give you some idea of what I really mean about that.

43
00:03:03,230 --> 00:03:08,630
Well, if you are one of the million concerned about the fragile UI automation test that frequently

44
00:03:08,630 --> 00:03:15,550
fails due to unstable user interface, then this course will help you fix that particular problem.

45
00:03:15,550 --> 00:03:22,190
And similarly, if you wanted to do a real visual testing, which gives a logical difference of your

46
00:03:22,190 --> 00:03:27,390
application, if there is going to be any failure happens, then this course is going to be helping

47
00:03:27,390 --> 00:03:27,630
you.

48
00:03:27,630 --> 00:03:34,830
That, and if you want to leverage further with your API testing to ensure that you get the entire automated

49
00:03:34,870 --> 00:03:40,070
testing done with just the API schema, then this course is going to be helpful for you.

50
00:03:40,070 --> 00:03:48,030
So we are going to see how we can use our existing test and empower them with visual testing, self-healing,

51
00:03:48,230 --> 00:03:54,350
and making them more smart and intelligent with the power of artificial intelligence and large language

52
00:03:54,350 --> 00:03:54,910
model.

53
00:03:55,070 --> 00:03:57,350
That is the crux of this particular course.

54
00:03:57,830 --> 00:04:01,910
Well, as that said, let's understand why we need self-healing test in first place.

55
00:04:01,910 --> 00:04:07,350
For instance, you can see that we have got a page developed by the developers, and he's giving to

56
00:04:07,350 --> 00:04:10,470
us, and he has made some changes on the UI.

57
00:04:10,510 --> 00:04:14,230
Well, now our test gets obsolete and our tests immediately fail.

58
00:04:14,670 --> 00:04:20,180
But what if we are passing the page as well as the cord to the large language model.

59
00:04:20,460 --> 00:04:27,860
And we are going to get a real time feed of what has changed on the page, as well as whether our page

60
00:04:27,860 --> 00:04:30,900
object model code that we have got any obsolete look error.

61
00:04:31,100 --> 00:04:37,460
Then we can ask the large language model to return as if there is any matching page look errors that

62
00:04:37,460 --> 00:04:39,580
we have got, then go and run it.

63
00:04:39,580 --> 00:04:46,300
But if there is any breaking change, then report that breaking change as a file and still don't fail

64
00:04:46,300 --> 00:04:46,780
the test.

65
00:04:46,780 --> 00:04:53,700
Rather, just run the test for the remaining scenarios and then report the failed locaters to the developers

66
00:04:53,700 --> 00:04:59,660
in a slack, or maybe in a format which the developers can understand and tell them that these has made

67
00:04:59,660 --> 00:05:01,780
the test locator to fail.

68
00:05:01,820 --> 00:05:08,620
But still, the test execution continued in order to not abruptly stop the entire test, but still continue

69
00:05:08,620 --> 00:05:09,540
from then on.

70
00:05:09,540 --> 00:05:16,700
So this is one of the way that you can see that automation test can leverage the power of LM to self-heal

71
00:05:16,700 --> 00:05:22,220
the test and continue the test execution and report the failures to the developer so that they can go

72
00:05:22,220 --> 00:05:22,900
and fix it.

73
00:05:22,900 --> 00:05:27,180
And the next time, while we run the entire test, it is still going to work without any problem.

74
00:05:27,300 --> 00:05:30,860
This is the power of how we can use the self-healing approach.

75
00:05:31,100 --> 00:05:36,540
Well, as I said, we are going to be doing all of these operations with quite a lot of different operation,

76
00:05:36,540 --> 00:05:40,780
and you will see that it starts off with complete basic, and then we'll go all the way to complete

77
00:05:40,780 --> 00:05:44,660
complex approach, something like this, and then we'll see how things work.

78
00:05:44,700 --> 00:05:49,300
I'm going to quickly show you a demo before we get started with this course, so that you can understand

79
00:05:49,300 --> 00:05:51,500
how amazing this course is being built.

80
00:05:51,540 --> 00:05:56,100
As I told you, this particular course supports both playwright and selenium.

81
00:05:56,100 --> 00:06:01,860
That's the reason why we have the code for both playwright and selenium, as you can see over here.

82
00:06:01,860 --> 00:06:04,980
And I'm going to quickly show you the how the code are going to be.

83
00:06:05,020 --> 00:06:10,100
As you can see, this particular code for the page object model in selenium, it looks pretty familiar.

84
00:06:10,100 --> 00:06:12,380
It looks pretty much exactly the same way.

85
00:06:12,380 --> 00:06:16,860
How like the page object model code with the WebDriver over here.

86
00:06:16,900 --> 00:06:21,700
The only change we have made in here is we have got a method called as AI find element, which is going

87
00:06:21,740 --> 00:06:28,730
to call the large language model to find an alternative locator if this error is wrong at the moment,

88
00:06:28,730 --> 00:06:30,410
you can see that all these data are correct.

89
00:06:30,410 --> 00:06:32,330
That's the reason why it's just going to work fine.

90
00:06:32,330 --> 00:06:38,010
But if you see the login page there, all the locators are entirely wrong and this test should eventually

91
00:06:38,010 --> 00:06:38,490
fail.

92
00:06:38,730 --> 00:06:43,730
But what is going to happen is this test is still going to run, because it is going to use the power

93
00:06:43,730 --> 00:06:50,290
of large language model, but it is going to report to the developers and test engineer that these are

94
00:06:50,290 --> 00:06:56,410
the failures in the locators, which needs to be fixed before you do the next run.

95
00:06:56,530 --> 00:07:01,330
I'm going to quickly show you a demo like how this is done, but before that I'm going to also show

96
00:07:01,330 --> 00:07:07,610
you that this particular code has got a healed locator or JSON file, which is going to hold all the

97
00:07:07,610 --> 00:07:09,090
healed locator for us.

98
00:07:09,130 --> 00:07:13,290
But before I even show that file, I'm going to just delete the file.

99
00:07:13,490 --> 00:07:16,290
And I'm going to run this specific test alone.

100
00:07:16,290 --> 00:07:18,730
And I will show you how the execution is going to happen.

101
00:07:19,010 --> 00:07:23,850
The test is going to be pretty much exactly the same, like how you do the traditional test, but just

102
00:07:23,850 --> 00:07:26,490
that it has got the AI power in it.

103
00:07:26,490 --> 00:07:32,410
And now I'm going to run this particular test, and it is going to use the OpenAI model for now, because

104
00:07:32,410 --> 00:07:35,530
it is going to be quite faster, as you can see over here.

105
00:07:35,530 --> 00:07:41,570
But you can use your local large language model, or you can also use any other model which you are

106
00:07:41,570 --> 00:07:42,530
interested in.

107
00:07:42,570 --> 00:07:46,450
You see that now the test is executed for 15 seconds for us over here.

108
00:07:46,490 --> 00:07:52,930
The reason why it took so much of time is because there is a failure in the locator, because you see

109
00:07:52,930 --> 00:07:55,370
that we have just scrambled the locators.

110
00:07:55,690 --> 00:08:00,170
And now if I'm going to go to the bin folder, you will notice that we have got a healed locator, a

111
00:08:00,170 --> 00:08:01,130
JSON file.

112
00:08:01,410 --> 00:08:06,170
And if I open that particular file, you will notice that it has got the original locator which is the

113
00:08:06,170 --> 00:08:10,410
broken locator, and also tells you what is the working locator over here.

114
00:08:10,770 --> 00:08:16,410
This is the file that you can share to your developer and tell them that the test has failed, but still

115
00:08:16,410 --> 00:08:21,330
it continued executing the rest of the scenario because it is healed by the AI.

116
00:08:21,530 --> 00:08:26,130
But we need to fix these locator like why this is failing, which is quite amazing.

117
00:08:26,170 --> 00:08:31,250
And the next thing is we have also implemented the caching as well as the persistency approach over

118
00:08:31,250 --> 00:08:31,530
here.

119
00:08:31,570 --> 00:08:33,650
Like this one is a cached locator.

120
00:08:33,690 --> 00:08:39,160
The next time we're going to run the same exact test, which took 15 seconds, will take less than this

121
00:08:39,160 --> 00:08:43,000
particular time because it is going to be using the caching approach over here.

122
00:08:43,040 --> 00:08:47,320
Now you can see that the test execution happens over here, but it is quite faster.

123
00:08:47,360 --> 00:08:53,120
The reason why this is happening is because now it is using the persistent locator that we have got

124
00:08:53,120 --> 00:08:57,040
over here, and it works as expected, which is quite amazing.

125
00:08:57,400 --> 00:09:01,280
This is the first power of the healed locator for us.

126
00:09:01,320 --> 00:09:05,240
Now the next thing that we will do in this particular course is the visual testing.

127
00:09:05,240 --> 00:09:11,240
So we can see that we can use the power of the vision model to see how the visual testings can be done.

128
00:09:11,240 --> 00:09:17,800
And this testing is going to be helping you to ensure that you can build a visual approach of testing

129
00:09:17,800 --> 00:09:24,280
your application by every single pixel, as well as every single functionalities, is working as expected.

130
00:09:24,560 --> 00:09:25,720
That's the power.

131
00:09:26,040 --> 00:09:28,760
These are things that we are going to be covering in this particular course.

132
00:09:28,800 --> 00:09:31,480
I'm quite excited to see you joining this course.

133
00:09:31,520 --> 00:09:34,600
Like how I got excited while building this entire course.

134
00:09:34,640 --> 00:09:37,800
Once again, thank you so much for choosing this course.

135
00:09:37,880 --> 00:09:40,360
See you in our first section of this course.

==================================================================================


section 2. Running LLMs locally using Ollama


video-1--introduction

1
00:00:00,160 --> 00:00:01,880
Welcome to the next section of our course.

2
00:00:01,880 --> 00:00:06,720
And in this section we'll be talking about running local large language model using Lama.

3
00:00:07,000 --> 00:00:15,520
So we are going to be using the Lama to run the local large language model instead of running the large

4
00:00:15,520 --> 00:00:17,440
language model from an API.

5
00:00:17,640 --> 00:00:20,280
So this is going to save quite a lot of money for us.

6
00:00:20,280 --> 00:00:27,760
While we are going to be using the large language model while testing our large language model applications

7
00:00:27,760 --> 00:00:29,720
internally from within our machine.

8
00:00:29,800 --> 00:00:37,120
So if you just go to the Lama website over here, this is the page which I'm talking about, or this

9
00:00:37,120 --> 00:00:41,880
is the application that I'm talking about, which is going to be helpful for you to run the large language

10
00:00:41,880 --> 00:00:44,400
models locally within your own machine.

11
00:00:44,400 --> 00:00:50,120
So if you have a mac OS or Linux or Windows, you can just go ahead and download this particular application

12
00:00:50,120 --> 00:00:51,040
within your machine.

13
00:00:51,040 --> 00:00:54,440
And then you can start using all the models within your machine.

14
00:00:54,440 --> 00:00:55,760
That is amazing, right?

15
00:00:55,800 --> 00:01:02,800
You don't really have to, uh, sign up with the OpenAI's, uh, API to call an API for accessing the

16
00:01:02,800 --> 00:01:07,680
larger language models like how you usually do by paying so much of money, those things are not even

17
00:01:07,680 --> 00:01:08,080
required.

18
00:01:08,080 --> 00:01:13,960
So if you just go to the openai.com and we just go to their API platform over here, you see that there

19
00:01:13,960 --> 00:01:15,520
is this API login comes in.

20
00:01:15,520 --> 00:01:20,960
So if you just go and hit this API login, uh, I have already signed up for this particular OpenAI

21
00:01:21,160 --> 00:01:22,240
login over here.

22
00:01:22,280 --> 00:01:24,360
I mean you can see there are some pricings available.

23
00:01:24,360 --> 00:01:31,240
So for every single, uh, model that you use with their signed up, uh, models, uh, API, you're

24
00:01:31,240 --> 00:01:36,520
going to be paying this much money for these many input that you're going to be, uh, entering like

25
00:01:36,520 --> 00:01:37,680
for 1 million tokens.

26
00:01:37,680 --> 00:01:43,000
These are things that these are the money that you have to pay for these particular large language models

27
00:01:43,000 --> 00:01:48,960
while you're going to use that, if it is hosted in their own platform, like OpenAI platform or Cloud

28
00:01:48,960 --> 00:01:51,480
Anthropic Platform or Google Gemini platform.

29
00:01:51,480 --> 00:01:54,440
So you have to sign up and you have to pay money to them.

30
00:01:54,440 --> 00:01:58,600
But if you're going to be building a large language model application, and if you don't want to spend

31
00:01:58,600 --> 00:02:05,430
these many money, then you can just host or maybe just can, um, run your large language model within

32
00:02:05,430 --> 00:02:07,150
your local machine itself.

33
00:02:07,550 --> 00:02:11,830
And that is the power of this particular olama, because it will let you do that for you.

34
00:02:11,950 --> 00:02:17,150
So I have already downloaded the olama within my local machine in my Mac operating system.

35
00:02:17,150 --> 00:02:20,230
So it is very, very easy for me to just start using it.

36
00:02:20,510 --> 00:02:22,070
Uh, I mean, it's very straightforward.

37
00:02:22,070 --> 00:02:24,870
Just go ahead and click this download based on your operating system.

38
00:02:24,870 --> 00:02:26,550
The download is going to happen for you.

39
00:02:26,550 --> 00:02:29,470
And because I am using Mac OS, I can go and click this one.

40
00:02:29,510 --> 00:02:33,590
If you're going to use Linux or Windows, just go ahead and select the relevant operating system and

41
00:02:33,590 --> 00:02:35,430
download the tools that you're looking for.

42
00:02:35,910 --> 00:02:37,830
And finally the models.

43
00:02:37,870 --> 00:02:39,910
This is the most important part over here.

44
00:02:39,950 --> 00:02:41,630
We just go to the models over there.

45
00:02:42,150 --> 00:02:47,310
This particular models that you are seeing over here are the all the models, like the full blown models

46
00:02:47,310 --> 00:02:50,750
available within the Ola map site itself.

47
00:02:50,750 --> 00:03:02,190
So you can use a deep C, R1 or R3 or Pi four or Lambda theta r2, um, and Mistral quan uh Qn 2.5.

48
00:03:02,230 --> 00:03:06,030
You see that all the models that you name it, it's available over here.

49
00:03:06,230 --> 00:03:12,030
And most importantly, you can also see that there are option where you can just select specific model

50
00:03:12,030 --> 00:03:16,430
which are specific for embedding or vision or even tool support.

51
00:03:16,430 --> 00:03:21,470
So if you have uh, any of the agents that you're going to be building, and then if you wanted to use

52
00:03:21,470 --> 00:03:24,070
the model for tool support, you can use that as well.

53
00:03:24,070 --> 00:03:30,070
Guys, you see that 3.3 70 billion parameter has got the tool support model over here, which is amazing.

54
00:03:30,110 --> 00:03:31,230
You can use that as well.

55
00:03:31,590 --> 00:03:37,430
And uh, if I'm going to use this deep CR1, the most popular model to date is going to be very, very

56
00:03:37,430 --> 00:03:38,190
straightforward as well.

57
00:03:38,190 --> 00:03:41,470
You can choose uh a specific uh billion parameter.

58
00:03:41,470 --> 00:03:44,790
And then you can start working with this particular model as well.

59
00:03:44,790 --> 00:03:50,710
If you're going to be using this model for building your local large language model applications, that

60
00:03:50,710 --> 00:03:52,670
is about the whole AMA for you.

61
00:03:52,670 --> 00:03:56,710
And I have already downloaded it and I have already installed it, so please go ahead and install it

62
00:03:56,710 --> 00:04:01,270
before our next lecture because we are going to start using it from our next lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 2-- Understanding different AI Models

1
00:00:00,080 --> 00:00:03,920
All right, so hopefully you have already downloaded the Ola within your local machine and you have

2
00:00:03,920 --> 00:00:04,680
installed it.

3
00:00:04,680 --> 00:00:05,800
So which is great.

4
00:00:05,800 --> 00:00:10,000
And if you have not please go ahead and do it again, because that is something required for our next

5
00:00:10,000 --> 00:00:12,320
discussion that we are going to be doing in this particular lecture.

6
00:00:12,560 --> 00:00:18,680
So as you can see over here, I can choose the model that I wanted to run within my local machine.

7
00:00:18,680 --> 00:00:24,640
So I can choose 7 billion parameter or 8 billion parameters, 14 billion parameter, 32 billion parameter,

8
00:00:24,680 --> 00:00:28,600
all the way up to seven 671 billion parameter within my machine.

9
00:00:28,920 --> 00:00:30,680
You see that there is a drop down over here.

10
00:00:30,880 --> 00:00:35,120
It's going to show you the size of this particular parameter and the model.

11
00:00:35,440 --> 00:00:38,160
So 7 billion parameter has got 4.7 gig.

12
00:00:38,280 --> 00:00:45,040
And if you see 617 billion parameter it is 404 GB that you have to have within your machine.

13
00:00:45,360 --> 00:00:51,200
I'm telling you based on the parameter, the complexity of the transformer model increases and based

14
00:00:51,200 --> 00:00:56,520
on the complexity, it also increases the the processing power.

15
00:00:56,520 --> 00:01:00,600
And also you need to have quite a lot of quantization execution support.

16
00:01:00,600 --> 00:01:04,560
So you can see that for a 7 billion parameter I have the model over here.

17
00:01:04,560 --> 00:01:09,280
And you see that the model has got a quantization version of two.

18
00:01:09,740 --> 00:01:15,300
and also has got the the total head count over here, which is 28.

19
00:01:15,300 --> 00:01:19,700
So totally it's going to have 28 different types of head counts like classifications that it's going

20
00:01:19,740 --> 00:01:21,220
to support in this particular model.

21
00:01:21,420 --> 00:01:26,100
And also has got a label of 7 billion because it's a 7 billion parameter.

22
00:01:26,100 --> 00:01:31,380
And the same thing is going to keep changing based on the type of uh, parameter they're going to choose.

23
00:01:31,380 --> 00:01:34,580
For instance, if you're going to choose like 671 billion parameter.

24
00:01:34,900 --> 00:01:39,820
And if you choose this one over here, you see the number of head counts might have increased quite

25
00:01:39,860 --> 00:01:41,220
a lot this time.

26
00:01:41,220 --> 00:01:44,900
So the head count right now is 128 as opposed to 14.

27
00:01:44,940 --> 00:01:45,780
It was before.

28
00:01:46,060 --> 00:01:48,940
And the head count kV is also 128.

29
00:01:49,060 --> 00:01:52,860
Uh, so it is going to support quite a lot of different classifications.

30
00:01:52,860 --> 00:01:58,540
Uh, while you're going to be using this particular model within your machine, and also uh, the size

31
00:01:58,540 --> 00:02:01,820
is also increases based on that the quantization increases.

32
00:02:01,820 --> 00:02:08,060
And if the quantization increases, obviously you need to have a lot of GPU power, CPU power, Ram

33
00:02:08,060 --> 00:02:09,340
power within your machine.

34
00:02:09,380 --> 00:02:15,540
I will say most of our machines are not really built to run this 617 billion parameter or 70 billion

35
00:02:15,540 --> 00:02:21,750
parameter and even 32 billion parameter we can probably limit until 14 billion or 8 billion at the max.

36
00:02:21,950 --> 00:02:25,270
And I'm using Apple M1 Max machine over here.

37
00:02:25,270 --> 00:02:28,030
And I have got 64 GB of memory.

38
00:02:28,030 --> 00:02:30,430
And it is quite good in the inferencing.

39
00:02:30,430 --> 00:02:32,310
So I'm just going to use this particular machine.

40
00:02:32,310 --> 00:02:38,230
But if you have uh, a windows machine or same kind of machine.

41
00:02:38,230 --> 00:02:41,110
So probably we can just limit with the eight GB.

42
00:02:41,310 --> 00:02:47,430
And if you don't really have a powerful machine, I will recommend you to use uh, a lower version of

43
00:02:47,430 --> 00:02:48,510
the parameter.

44
00:02:48,510 --> 00:02:54,430
But the more lower parameter that you use in the model, the less predictable output that you can actually

45
00:02:54,430 --> 00:02:59,390
get out from the particular model, because the model really doesn't perform quite well if you use smaller

46
00:02:59,390 --> 00:03:01,670
model within your local machine.

47
00:03:01,670 --> 00:03:09,710
So either try to get a GPU for that matter, like 2080 or 30 80 or 40, 90, 40, 90 is going to be

48
00:03:09,710 --> 00:03:10,990
very costly for you for sure.

49
00:03:11,030 --> 00:03:17,030
3080 at least max, or maybe 2080 if you just get any of these Nvidia graphics card within your machine,

50
00:03:17,030 --> 00:03:18,310
you can probably use that.

51
00:03:18,310 --> 00:03:22,710
And then you can try to run whatever that we're going to be discussing in this particular course.

52
00:03:23,110 --> 00:03:25,030
Well, as I said, that's about it.

53
00:03:25,030 --> 00:03:30,010
That's the thing that we are going to be using within our machine, and we'll see how we can.

54
00:03:30,410 --> 00:03:33,690
Download this particular model and then how we can work with it.

55
00:03:33,690 --> 00:03:34,450
So that is how.

56
00:03:34,530 --> 00:03:38,650
You can understand how these models are really working behind the scene.

57
00:03:39,250 --> 00:03:39,730
So if I.

58
00:03:39,770 --> 00:03:44,010
Choose any other model, not just the deep sea, let's say a llama 3.3.

59
00:03:44,170 --> 00:03:44,890
They also have.

60
00:03:44,930 --> 00:03:47,930
Got like 70 billion parameter as you can see over here.

61
00:03:48,130 --> 00:03:52,770
And if I'm going to choose some other models like you see that llama 3.1.

62
00:03:52,810 --> 00:03:58,570
There is a 405 billion parameter which is 243 gig of storage itself.

63
00:03:58,570 --> 00:04:02,650
And it is going to, uh, it's going to have quite a lot of different operation that you are going to

64
00:04:02,650 --> 00:04:03,730
be doing over there.

65
00:04:04,010 --> 00:04:09,850
And let's see, what is the total, uh, headcount that I have got like 128 headcount, as you can see

66
00:04:09,850 --> 00:04:10,410
over here.

67
00:04:10,410 --> 00:04:15,290
And the headcount KB is just eight, whereas in deep sea it was 128, as you know.

68
00:04:15,610 --> 00:04:17,930
So yeah, it depends upon the model.

69
00:04:17,930 --> 00:04:21,050
Uh, the things are going to keep changing and also the complexity changes.

70
00:04:21,050 --> 00:04:26,930
And so is your machine's performance reduces based on the type of parameter and the model that you really

71
00:04:26,930 --> 00:04:27,490
use.

72
00:04:27,890 --> 00:04:32,450
Well, as I said in our next lecture, we are going to see how we can start using any one of the models

73
00:04:32,450 --> 00:04:36,050
in our local machine and also try to play around with that.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 3. Running LLMs locally using Ollama

1
00:00:00,080 --> 00:00:00,680
All right.

2
00:00:00,680 --> 00:00:06,160
So now we are going to start using an Anova model which is available within the Alama website over here.

3
00:00:06,160 --> 00:00:10,720
And then we will see how we can run this particular model within our machine.

4
00:00:11,040 --> 00:00:18,040
So in order for me to do that, I'm going to just go to uh, my hyper or terminal or any terminal that

5
00:00:18,040 --> 00:00:19,160
you are really using.

6
00:00:19,160 --> 00:00:24,160
And I use hyper terminal, uh, in my Mac operating system because it's quite clean and neat.

7
00:00:24,400 --> 00:00:28,680
And this is one of the terminal that you can download it from the internet and then start using it as

8
00:00:28,680 --> 00:00:28,800
well.

9
00:00:28,840 --> 00:00:29,880
It's pretty straightforward.

10
00:00:30,160 --> 00:00:34,160
Uh, and this terminal over here, I'm just going to say uh oh llama.

11
00:00:34,720 --> 00:00:40,920
And if I just say list over here, it is going to list me all the models, which is available over here

12
00:00:40,920 --> 00:00:42,480
the moment I run this all llama list.

13
00:00:42,480 --> 00:00:46,480
As you can see there is this llama is also up and running for me over here.

14
00:00:47,000 --> 00:00:53,560
So all you have to do is you need to, uh, either run the llama first and then use the command llama

15
00:00:53,560 --> 00:00:59,720
list, which is going to show you the list of all the models which is already available within your,

16
00:01:00,000 --> 00:01:00,800
uh, machine.

17
00:01:00,800 --> 00:01:05,070
So that is what is the model that is, have already downloaded within my machine and it is running.

18
00:01:05,110 --> 00:01:08,150
I mean, it's not running, but it is already there within my machine.

19
00:01:08,150 --> 00:01:14,070
I can use this models, uh, within my machine, but if I wanted to, maybe you can see that I don't

20
00:01:14,070 --> 00:01:17,510
really have the Pi for, um, over here.

21
00:01:17,510 --> 00:01:19,190
This particular, uh, model.

22
00:01:19,190 --> 00:01:22,190
So if I want to use this particular model, I can really use that as well.

23
00:01:22,230 --> 00:01:26,550
So let's say if there is any smaller model that I can show you as a demo, probably.

24
00:01:26,870 --> 00:01:28,430
Um, maybe.

25
00:01:28,470 --> 00:01:30,150
What is this model?

26
00:01:30,230 --> 00:01:31,830
Uh, this looks.

27
00:01:32,070 --> 00:01:32,230
Yeah.

28
00:01:32,230 --> 00:01:34,790
I'm just going to download this for the demonstration purpose.

29
00:01:34,790 --> 00:01:39,950
So if I want to use this particular model, like 1.8 billion parameter model, I have to just run this

30
00:01:39,950 --> 00:01:44,190
command Olama run QN1 and colon 1.8 billion.

31
00:01:44,230 --> 00:01:46,910
Just copy this whole thing and paste it over here.

32
00:01:47,150 --> 00:01:51,750
And if I hit enter, you'll notice that pretty much like if you have used Docker before, it is going

33
00:01:51,790 --> 00:01:54,510
to download the image from Docker.

34
00:01:54,670 --> 00:01:59,270
Remember from the Docker Hub you can download the image similarly over here in the olama.

35
00:01:59,270 --> 00:02:05,670
If you just do olama run QN1 point 8 billion, it is going to go and uh, pull the manifest first,

36
00:02:05,670 --> 00:02:11,390
and then it's going to start downloading the the entire model for you within your local machine.

37
00:02:11,550 --> 00:02:14,150
And you see that I have downloaded within my local machine.

38
00:02:14,270 --> 00:02:18,390
And once it is downloaded it is going to get all the metadata and everything.

39
00:02:18,390 --> 00:02:23,590
And then it is going to start running because we have specified run here, you can start seeing that

40
00:02:23,590 --> 00:02:26,670
this particular model can be even executed over here.

41
00:02:26,670 --> 00:02:32,110
And you can start typing the command and ask the question pretty much like how you do with the ChatGPT.

42
00:02:32,990 --> 00:02:36,150
So if you have the ChatGPT account, that's what you do, right?

43
00:02:36,190 --> 00:02:40,070
You go to the ChatGPT and then you're going to start asking the question over here.

44
00:02:40,190 --> 00:02:43,710
The same thing is going to happen with this as well over here.

45
00:02:43,790 --> 00:02:48,710
See, now you have got a prompt, uh, ready for you to type so that you can get answers.

46
00:02:48,710 --> 00:02:51,830
So if I ask, like, how are you doing?

47
00:02:52,190 --> 00:02:54,590
Uh, and you see that it's going to start responding.

48
00:02:54,590 --> 00:02:56,190
I'm an artificial intelligence language model.

49
00:02:56,190 --> 00:02:58,950
I don't have feeling in this, uh, traditional sense.

50
00:02:59,190 --> 00:03:03,110
However, I am functional, properly ready to assist any of the questions or task.

51
00:03:03,150 --> 00:03:03,750
Amazing.

52
00:03:04,030 --> 00:03:04,470
Great.

53
00:03:04,470 --> 00:03:11,180
So that is how you actually pull, uh, a model and then run the model within your local machine.

54
00:03:11,300 --> 00:03:16,980
And let's say if you want to, uh, if you're going to ask some question like write a selenium with

55
00:03:17,020 --> 00:03:23,780
a C sharp dotnet code for, for uh, google.com website.

56
00:03:24,140 --> 00:03:29,060
And if I ask this question, you see that now it is going to immediately start writing the code.

57
00:03:29,100 --> 00:03:31,020
I mean, the code itself is entirely wrong.

58
00:03:31,020 --> 00:03:33,300
As you can see, it is doing HTTP client.

59
00:03:33,340 --> 00:03:34,100
HTTP client.

60
00:03:34,140 --> 00:03:35,740
HTTP client or SSL protocol?

61
00:03:36,020 --> 00:03:37,620
Uh, something like that.

62
00:03:37,620 --> 00:03:41,740
I don't even understand what this is writing because it's not even a selenium code to be honest.

63
00:03:41,740 --> 00:03:44,380
It's completely messed up with selenium code.

64
00:03:44,380 --> 00:03:52,660
So it's just writing, uh, is using the system dot net http uh package and then is writing a code from

65
00:03:52,660 --> 00:03:52,980
that.

66
00:03:53,020 --> 00:03:53,860
It's crazy.

67
00:03:53,900 --> 00:03:55,380
Like it's completely wrong code.

68
00:03:55,620 --> 00:04:02,180
So this is because as I told you, the model that we are using, uh, over here is actually a very,

69
00:04:02,180 --> 00:04:08,260
very small, uh, I mean, old SH1 1.5 series, uh, from Alibaba Cloud.

70
00:04:08,420 --> 00:04:13,010
Uh, and it is also having less, uh, less parameters over here.

71
00:04:13,890 --> 00:04:20,610
But if I'm going to use some other models, then I will have even more, uh, even accurate answer.

72
00:04:20,650 --> 00:04:26,170
Like if I use some model which has got maybe the deep set model, and if I try to ask the same question,

73
00:04:26,170 --> 00:04:27,970
things will be entirely different.

74
00:04:27,970 --> 00:04:32,050
So I will quickly show you how it is going to look like if I'm going to use the deep model.

75
00:04:32,410 --> 00:04:37,490
So if I want to quit this particular prompt, all I have to do is I want to just say by like slash by.

76
00:04:37,730 --> 00:04:41,170
So it will just quit the prompt execution over here.

77
00:04:41,530 --> 00:04:47,050
And now, as I told you in the Olama list, I can see all my models coming up over here.

78
00:04:47,050 --> 00:04:52,570
And if I want to use any one of the other model, for instance, I have got a deep seek R1, um, uh,

79
00:04:52,570 --> 00:04:54,090
8 billion parameter.

80
00:04:54,290 --> 00:04:55,650
So if I want to use that.

81
00:04:55,650 --> 00:05:01,970
So I'm just going to say olama, uh, and if I hit says space, there is going to show me all the different

82
00:05:01,970 --> 00:05:03,130
model that I have got.

83
00:05:03,290 --> 00:05:07,930
You may not be getting this option over here within your machine, because you may need to install some

84
00:05:07,930 --> 00:05:10,170
third party plugin to get this kind of answer.

85
00:05:10,210 --> 00:05:12,600
If you don't get it, don't worry, you just have to do this.

86
00:05:12,640 --> 00:05:16,840
Copy this entire thing from here like deep sea.

87
00:05:17,160 --> 00:05:19,280
And then paste it over here.

88
00:05:19,560 --> 00:05:20,760
Like deep sea.

89
00:05:20,840 --> 00:05:23,000
Uh, hyphen R1 8 billion.

90
00:05:23,000 --> 00:05:27,840
And if I hit enter, you'll notice that because it is already downloaded in my machine, it doesn't

91
00:05:27,840 --> 00:05:34,200
really download it once again, but it will start running this particular model within my local machine.

92
00:05:34,200 --> 00:05:36,760
So you see that it's a big, um, model.

93
00:05:36,760 --> 00:05:43,400
And it has got a lot of things to be inferred to be set up before we start inferencing.

94
00:05:43,440 --> 00:05:47,200
That's the reason why taking a bit of time while it was initiating things.

95
00:05:47,200 --> 00:05:47,720
Right.

96
00:05:48,040 --> 00:05:53,800
And now if I'm going to ask the same question that I asked to this, uh, model, uh, so I'm gonna

97
00:05:53,800 --> 00:05:56,840
just copy this whole thing and I'm going to paste it over here.

98
00:05:56,840 --> 00:05:57,000
Right.

99
00:05:57,000 --> 00:05:59,400
Selenium, C-sharp code for google.com website.

100
00:05:59,400 --> 00:06:06,640
You see that the moment I ask this question now, because this deep sea R1 model is a reasoning model,

101
00:06:06,640 --> 00:06:09,640
it is first starting to think like what it has to do.

102
00:06:10,000 --> 00:06:12,360
You see that it is writing all the thinking process.

103
00:06:12,400 --> 00:06:15,440
Um, before you start writing the answer.

104
00:06:15,720 --> 00:06:19,440
And look at that now it's writing a selenium C-sharp code for us guys.

105
00:06:19,560 --> 00:06:25,400
It has thought a lot of things before it answered the question, and then it is writing the correct

106
00:06:25,440 --> 00:06:26,720
selenium C-sharp code.

107
00:06:26,720 --> 00:06:32,840
I'm 100% sure this code, if I'm going to use it within my local Visual Studio or Visual Studio Code,

108
00:06:33,240 --> 00:06:38,840
it is just going to work because the the answer is quite right and this is what you should be doing

109
00:06:38,840 --> 00:06:40,680
while you use this particular model.

110
00:06:40,840 --> 00:06:45,680
Um, and that's the reason why, as I told you, if you're going to be using an effective model, if

111
00:06:45,680 --> 00:06:52,760
you're going to be using a hyper parameter model, then you should be using then you should be getting

112
00:06:52,920 --> 00:06:58,080
a good response as opposed to a smaller model with a lesser parameter support on that.

113
00:06:58,760 --> 00:07:05,440
Well, as I said, this is how you can actually run a deep spec model or other types of model within

114
00:07:05,440 --> 00:07:06,960
your local machine.

115
00:07:07,360 --> 00:07:12,120
Even without even having an internet connectivity, you can run all these operations for you.

116
00:07:12,240 --> 00:07:16,600
That is the power of running the local large language model using Ola.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 4. Using Ollama Models in GUI

1
00:00:00,160 --> 00:00:07,800
So now that we saw how we can run the LM like Deep Sea or Qnh 1.8 billion parameter models within our

2
00:00:07,800 --> 00:00:08,840
local machine.

3
00:00:09,040 --> 00:00:13,400
Now we're going to see how we can make use of the user interface.

4
00:00:13,400 --> 00:00:14,080
Looks better.

5
00:00:14,120 --> 00:00:16,040
Pretty much like the ChatGPT interface.

6
00:00:16,040 --> 00:00:17,480
Like how you are going to see that.

7
00:00:17,720 --> 00:00:18,280
Guess what?

8
00:00:18,320 --> 00:00:24,800
We are going to be building these kind of interfaces using our Lang chain agent in our upcoming section

9
00:00:24,800 --> 00:00:30,920
of this course, like chatbots, but just wanted to give you a flavor of how you can use these models

10
00:00:30,920 --> 00:00:32,800
as a GUI interface to your machine.

11
00:00:32,840 --> 00:00:33,520
You can also use.

12
00:00:33,520 --> 00:00:35,240
There are so many different tools available.

13
00:00:35,360 --> 00:00:39,120
Uh, something like uh, Misty over here, dot app, as you can see over here.

14
00:00:39,120 --> 00:00:43,600
So this is the easiest way to use the local and online AI model within your machine.

15
00:00:43,600 --> 00:00:46,960
So you can just use this particular tool over here.

16
00:00:46,960 --> 00:00:51,080
Or you can also use something called as the GPT for all.

17
00:00:51,080 --> 00:00:53,000
So just go search for GPT four dot.

18
00:00:53,040 --> 00:00:54,920
Uh GPT for all I o.

19
00:00:55,160 --> 00:01:02,000
This is also another tool that you can use, uh, in order for, uh, using the model within your,

20
00:01:02,160 --> 00:01:02,760
uh, machine.

21
00:01:02,760 --> 00:01:07,400
So you see that they also support the, um, the AR1 model over here.

22
00:01:07,400 --> 00:01:11,800
And then the thinking is going to come up over there, and then it is going to start answering the questions

23
00:01:11,800 --> 00:01:12,120
for you.

24
00:01:12,120 --> 00:01:13,640
So you can use that as well.

25
00:01:13,680 --> 00:01:16,640
I'm going to quickly show you the Misti that I was talking about.

26
00:01:16,640 --> 00:01:22,120
So if I just say the MSD like Misti, this is going to come up over here.

27
00:01:22,320 --> 00:01:25,040
See that this is the interface looks pretty familiar for you.

28
00:01:25,080 --> 00:01:26,720
You can use for inferencing.

29
00:01:26,720 --> 00:01:28,840
You can also upload the document if you wanted to.

30
00:01:28,880 --> 00:01:36,120
You can also attach YouTube links and also images to uh, to also get the response from the vision models

31
00:01:36,120 --> 00:01:36,840
if you wanted to.

32
00:01:36,880 --> 00:01:38,520
So those things you can do it as well.

33
00:01:38,560 --> 00:01:39,280
And look at that.

34
00:01:39,280 --> 00:01:44,080
It is also automatically detecting all the models is available within my machine.

35
00:01:44,120 --> 00:01:51,000
See that it's telling me that there is an active queue and uh, 8.1 billion parameter, um, model over

36
00:01:51,000 --> 00:01:54,240
here, but you can also choose the different model within my machine.

37
00:01:54,280 --> 00:01:57,200
You see that it's showing me all the different models that I have got.

38
00:01:57,240 --> 00:02:02,320
And if I'm going to choose the deep sea R1 model over here, and if I'm going to ask the same question

39
00:02:02,320 --> 00:02:08,120
that I just asked, uh, over here, if you remember which is the right, the selenium C-sharp code,

40
00:02:08,400 --> 00:02:10,840
uh, I can do that as well if I wanted to.

41
00:02:10,880 --> 00:02:16,480
So let's say I'm going to copy this whole thing, but this time I'm going to ask for a different website,

42
00:02:16,480 --> 00:02:27,470
let's say app.suomi.com, uh, website uh, and I'm going to say write a playwright uh, with uh c sharp

43
00:02:27,470 --> 00:02:28,270
dotnet code.

44
00:02:28,670 --> 00:02:32,950
And the moment I ask it, you see that now the deep C R1 is going to start running it.

45
00:02:32,950 --> 00:02:33,470
And guess what?

46
00:02:33,470 --> 00:02:35,870
I'm also going to stop the internet over here.

47
00:02:35,870 --> 00:02:39,830
So it's going to just work on my local large language model.

48
00:02:39,830 --> 00:02:46,750
And it's going to give you the response, uh, as you can see over here, uh, and it's also doing every

49
00:02:46,750 --> 00:02:52,830
single thing from the local large language model without going to the internet for that matter.

50
00:02:52,870 --> 00:02:55,590
Is that thing is now created over here.

51
00:02:56,070 --> 00:03:00,110
And now it is starting to write the code for me, uh, which is amazing.

52
00:03:00,550 --> 00:03:02,710
And look at that.

53
00:03:02,750 --> 00:03:05,070
It's doing quite a lot of different operation.

54
00:03:05,070 --> 00:03:11,510
So this is how you can see that we can run a local large language model and also make use of the, uh,

55
00:03:11,510 --> 00:03:19,230
pretty much uh, with the chat bots or the tools is available over here to use as a chatbot, uh, for

56
00:03:19,230 --> 00:03:21,710
our respondents that are looking for.

57
00:03:21,710 --> 00:03:24,990
So that's the thing that you can do within your local machine.

58
00:03:25,590 --> 00:03:28,790
And now you have got the idea of how these things are working.

59
00:03:28,790 --> 00:03:34,110
Starting our next lecture, we'll also see how we can, uh, play around with this Olama tool even further,

60
00:03:34,110 --> 00:03:39,710
so that we are going to be making use of the Olama starting our next section while we start working

61
00:03:39,710 --> 00:03:40,670
with the long chain.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 5. Understanding Ollama with few more command line interface commands

1
00:00:00,080 --> 00:00:00,720
All right.

2
00:00:00,720 --> 00:00:05,000
So now we're going to explore this tool even further in this particular lecture.

3
00:00:05,000 --> 00:00:06,880
And we'll see how we can make use of them.

4
00:00:06,880 --> 00:00:13,520
So let me just say bye to this already running model which is the deep C R1 model.

5
00:00:13,520 --> 00:00:15,120
We don't even need this anymore.

6
00:00:15,400 --> 00:00:20,240
And now if I want to see what are the things that I can do from this alarm itself, you see that the

7
00:00:20,240 --> 00:00:25,560
moment I type o llama and space is going to show me all the different command that I can run with this

8
00:00:25,560 --> 00:00:26,600
particular o llama.

9
00:00:26,720 --> 00:00:29,920
So it's going to show me the RM to remove a model.

10
00:00:29,920 --> 00:00:34,400
So if you want to say if you want to remove a model like RM and let's say if I want to remove this Qnh

11
00:00:34,440 --> 00:00:39,280
1.8 billion parameter, and if I hit enter, you see that the moment I do it, it is going to be deleted

12
00:00:39,280 --> 00:00:40,920
from my machine.

13
00:00:41,160 --> 00:00:47,620
So now if I just say o llama and list, it is going to not show that particular model, the Qnh 1.8

14
00:00:47,620 --> 00:00:49,800
billion parameter, because it's completely gone.

15
00:00:50,000 --> 00:00:53,320
And similarly, if I want to delete this particular model, I know this is completely useless.

16
00:00:53,320 --> 00:01:02,080
So I can just say O llama and then RM and I can just say this particular model to delete, it's gone.

17
00:01:02,080 --> 00:01:06,920
And now if I just say llama list, that particular model is not there anymore.

18
00:01:07,120 --> 00:01:12,280
And if I wanted to do something like, uh, gonna get some information on this particular model.

19
00:01:12,280 --> 00:01:13,920
I can also do that as well.

20
00:01:13,920 --> 00:01:21,640
So I can just say show and any one of the model, let's say this, uh, deep sea R1 model, you see

21
00:01:21,640 --> 00:01:24,920
that it's going to show me what architecture this model, uh, is.

22
00:01:25,040 --> 00:01:32,200
And um, what is the parameter support and what is the context length and what is the embedding length.

23
00:01:32,200 --> 00:01:33,680
What is the quantization.

24
00:01:34,400 --> 00:01:37,680
And also what are the parameter supports available over there.

25
00:01:37,680 --> 00:01:40,960
So all these informations are going to be shown for me over there.

26
00:01:40,960 --> 00:01:44,840
So these are the things that you can see that you can see using this Olama tool.

27
00:01:44,840 --> 00:01:50,000
And I mean this olama is pretty much like how you can use like the Docker container.

28
00:01:50,040 --> 00:01:52,360
How do you manage the docker, how do you run the docker?

29
00:01:52,360 --> 00:01:56,720
Everything that you do in the Docker world, same thing you can do with the Olama.

30
00:01:56,720 --> 00:02:00,760
It's pretty much like the docker of the large language model.

31
00:02:00,880 --> 00:02:04,600
You can run everything from this particular olama over here.

32
00:02:04,800 --> 00:02:06,560
That's about this olama tool, guys.

33
00:02:06,560 --> 00:02:12,200
And starting our next lecture, we're going to see how we can make use of this Ola mass large language

34
00:02:12,200 --> 00:02:19,120
model from our local machine, and then use it with the Lang chain for building our large language model.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 6. Starting Ollama with API to run as a API server

1
00:00:00,040 --> 00:00:06,600
In this lecture, we are going to see how we can use this Ola to act as an API server, which you can

2
00:00:06,600 --> 00:00:12,840
use to retrieve the the model or communicate with the model using an API request.

3
00:00:12,840 --> 00:00:20,600
So basically you can see that using this Ola and you can see that they have got this option called as

4
00:00:20,880 --> 00:00:22,200
uh serve.

5
00:00:22,320 --> 00:00:23,840
So Ola serve.

6
00:00:24,280 --> 00:00:26,600
So we just hit uh enter.

7
00:00:26,600 --> 00:00:31,520
You will see that uh, currently my uh port is bound with this particular IP address.

8
00:00:31,520 --> 00:00:37,600
So basically I'm already running the Ola in the service, uh, as like up and running all the time.

9
00:00:37,600 --> 00:00:40,680
That's the reason why it says that the the address is already bound.

10
00:00:40,920 --> 00:00:46,840
Uh, but if you're going to be running this Ola serve in your terminal, you will notice that it is

11
00:00:46,840 --> 00:00:51,080
going to be starting as a service for you by listening to this particular port.

12
00:00:51,080 --> 00:00:52,560
Number 11434.

13
00:00:52,560 --> 00:00:57,560
So this is the port number that we are going to be using quite a lot, starting our next section while

14
00:00:57,560 --> 00:00:58,680
we communicate with the Ola.

15
00:00:59,040 --> 00:01:01,240
So the way we are going to write the code in our starting.

16
00:01:01,240 --> 00:01:07,160
Our next section is going to be talking to the large language model with the Olama only using the API

17
00:01:07,200 --> 00:01:09,120
server, which is this API server.

18
00:01:09,120 --> 00:01:13,000
So when I say API server, we're just going to go over here.

19
00:01:13,000 --> 00:01:21,640
And if I just type localhost of the port number 11434, and if I just say API and if I hit enter oh

20
00:01:21,680 --> 00:01:22,080
sorry.

21
00:01:23,600 --> 00:01:26,440
And if I hit enter like that, you see that the olama is running.

22
00:01:26,440 --> 00:01:28,840
So you get the response like Olama is running.

23
00:01:28,840 --> 00:01:35,800
And if you see just go to the uh, 143 API generate and you can also pass the body over here.

24
00:01:36,000 --> 00:01:43,840
So if I just go to my browser and if I just search for Olama, you'll notice that these are the API

25
00:01:43,880 --> 00:01:45,760
documentation of the Olama.

26
00:01:45,760 --> 00:01:52,200
And you can see that they have got all the details of the API's that you can use with the Olama over

27
00:01:52,200 --> 00:01:52,400
here.

28
00:01:52,440 --> 00:01:57,360
You see that, uh, they have got the uh, in the generate, you can pass the model and the prompt that

29
00:01:57,360 --> 00:02:01,030
you want to ask, and then you get the response from the particular model.

30
00:02:01,030 --> 00:02:07,470
So if I just go to the postman over here and let's say if I'm going to ask the question, uh, something

31
00:02:07,470 --> 00:02:11,510
like this, and the model is going to be llama 3.2 that they have used.

32
00:02:11,590 --> 00:02:12,870
Let's see if I have got the model.

33
00:02:12,870 --> 00:02:14,510
Yeah I have got llama 3.2.

34
00:02:14,910 --> 00:02:17,190
So I'm just going to leave that as it is.

35
00:02:17,430 --> 00:02:24,870
And I'm going to say why is sky blue and this is going to be a post operation that we have to do.

36
00:02:25,190 --> 00:02:31,230
And if I just ask this question, you'll notice that we are going to get a response from the model over

37
00:02:31,230 --> 00:02:31,750
here.

38
00:02:32,030 --> 00:02:35,070
This is a large language model that we are getting over here.

39
00:02:35,070 --> 00:02:42,190
But you see that we are getting response in like one by one, uh, like one word at a time as a response.

40
00:02:42,190 --> 00:02:45,310
But we can stream this particular response as well if you wanted to.

41
00:02:45,350 --> 00:02:49,670
So if you just go back to the documentation over here, this is the response that you get.

42
00:02:49,710 --> 00:02:55,030
And over here they also have got something called as stream as a false over here.

43
00:02:55,070 --> 00:02:57,430
And I'm just going to leave the stream as false over here.

44
00:02:57,430 --> 00:03:01,230
And now if I try to send it over here, you will notice that it's not really streaming the data, but

45
00:03:01,230 --> 00:03:05,070
it's going to send you all the data in a chunk for you immediately.

46
00:03:05,070 --> 00:03:05,630
Something like this.

47
00:03:05,630 --> 00:03:07,750
And you see that we get the response over here.

48
00:03:07,750 --> 00:03:10,270
So this is how we get the entire response.

49
00:03:10,270 --> 00:03:11,790
So why is the sky blue?

50
00:03:11,830 --> 00:03:15,990
Is that the reason why the sky appears blue is a fascinating phenomenon that involves a combination

51
00:03:15,990 --> 00:03:19,110
of physics, lights and our atmosphere, and it gives all the details.

52
00:03:19,590 --> 00:03:28,150
So this is how we can see that we can use the the APIs of the llama to communicate with our large language

53
00:03:28,150 --> 00:03:30,270
model, uh, using Olama.

54
00:03:30,270 --> 00:03:30,910
So Olama.

55
00:03:30,950 --> 00:03:35,390
So you need to run, uh, to make sure that you can communicate with your Olama.

56
00:03:35,390 --> 00:03:39,430
So starting our next session, we are going to communicate with this Olama with a large language model

57
00:03:39,430 --> 00:03:40,710
only using this API.

58
00:03:40,710 --> 00:03:46,190
So either you run them as a service like me, like how I'm doing it, or you can run this olama serve

59
00:03:46,190 --> 00:03:52,870
command in the terminal so that you can now start communicating with your, uh, with the long chain

60
00:03:52,870 --> 00:03:54,870
with the olama starting in our next section.

61
00:03:54,870 --> 00:04:00,910
So this ends the section of the Olama and how you can use Olama to run your large language models.


==================================================================================

section 3. Fundamentals Understanding Prompt Engineering, Context Engineering & Vibe Code

video 1.introduction

1
00:00:00,120 --> 00:00:02,440
Welcome to the first lecture of this section.

2
00:00:02,440 --> 00:00:07,640
And in this lecture we are going to talk about an introduction to this entire section.

3
00:00:07,640 --> 00:00:10,400
So what are we going to talk about in this particular section itself.

4
00:00:10,400 --> 00:00:16,320
Well we are going to talk about a lot of details in theory as well as in practical way.

5
00:00:16,480 --> 00:00:23,480
We are going to talk about what exactly is prompt engineering and how effective on powerful prompt engineering

6
00:00:23,480 --> 00:00:23,840
are.

7
00:00:24,200 --> 00:00:29,440
And then we are going to talk about the evolution of prompt engineering to context engineering, and

8
00:00:29,480 --> 00:00:32,920
how context engineering is making so much difference.

9
00:00:32,920 --> 00:00:40,720
While we work with the AI agents, large language models, and how these context plays a key role to

10
00:00:40,760 --> 00:00:42,480
this entire application.

11
00:00:42,480 --> 00:00:48,640
So make sure that you understand these concepts very clearly in this particular section, because this

12
00:00:48,640 --> 00:00:52,760
entire course is going to relay on these two concepts a lot.

13
00:00:52,960 --> 00:00:59,720
The moment you understand these two and how you are going to be using them effectively to prompt your

14
00:00:59,720 --> 00:01:04,100
large language model and get the effective response out of it.

15
00:01:04,300 --> 00:01:10,700
That's exactly what we're going to be doing while we build our self-healing code in our upcoming section

16
00:01:10,700 --> 00:01:11,540
of this course.

17
00:01:11,900 --> 00:01:18,420
And then we'll be talking about understanding the AI agents and how AI agents is useful by getting the

18
00:01:18,420 --> 00:01:24,780
information to the large language models and how it has the tools which does those operation.

19
00:01:25,020 --> 00:01:30,340
We'll also be talking about the vibe coding by writing an entire automation test code, like even a

20
00:01:30,340 --> 00:01:34,140
framework level code using one single prompt.

21
00:01:34,140 --> 00:01:40,140
And then we'll be seeing how we can write the test case requirements document and also BDD test cases

22
00:01:40,140 --> 00:01:42,260
and everything using vibe coding.

23
00:01:42,380 --> 00:01:49,420
The reason why we're talking about vibe coding in here is because we are going to insist the power of

24
00:01:49,420 --> 00:01:55,740
the context and the prompt, while we are going to do all these operation in any of the vibe coding

25
00:01:55,780 --> 00:01:56,140
tool.

26
00:01:56,140 --> 00:01:59,020
So these are things that we are going to be discussing in this particular section.

27
00:01:59,140 --> 00:02:04,100
So let's jump right in with the prompt engineering starting our next lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


video 2. Understanding Prompt Engineering

1
00:00:00,240 --> 00:00:03,440
In this lecture we're going to talk about understanding prompt engineering.

2
00:00:03,440 --> 00:00:08,640
So this is one of the first and foremost basic fundamental details that we need to know about.

3
00:00:08,800 --> 00:00:10,480
What is prompt engineering.

4
00:00:10,720 --> 00:00:17,160
Well, prompt engineering is the process of designing and optimizing prompts to get better output from

5
00:00:17,160 --> 00:00:18,960
generative AI models.

6
00:00:18,960 --> 00:00:24,520
Well, as you know, that prompt engineering is something which is getting more and more common these

7
00:00:24,520 --> 00:00:24,840
days.

8
00:00:24,840 --> 00:00:30,960
While we are using these generative AI tools like ChatGPT for that matter, or cloud desktop for that

9
00:00:30,960 --> 00:00:37,640
matter, or even in our phones while we try to generate some of the image, or maybe to make our text

10
00:00:37,680 --> 00:00:42,400
look more grammatically free, then we try to do the prompt as much as possible.

11
00:00:42,400 --> 00:00:46,520
So prompt engineering is now getting an embedded part of our everyday life.

12
00:00:46,920 --> 00:00:53,320
And prompt engineering is mainly going to focus on crafting the right instruction inside a prompt.

13
00:00:53,720 --> 00:01:01,610
It's a static, and it's a one shot text that you are passing in, which will help to assign the role

14
00:01:01,610 --> 00:01:06,330
or instruction to an AI agent or a large language model.

15
00:01:06,690 --> 00:01:08,450
To get the job done.

16
00:01:08,490 --> 00:01:11,810
Well, I'm certainly talking about AI agent or multi-agent systems.

17
00:01:11,810 --> 00:01:15,450
I'm going to talk about that in our upcoming lectures of this section.

18
00:01:15,450 --> 00:01:16,290
But guess what?

19
00:01:16,450 --> 00:01:22,450
If you are really not heard about these terminologies before, like AI agents or multi-agent systems,

20
00:01:22,450 --> 00:01:23,370
don't worry about it.

21
00:01:23,370 --> 00:01:23,890
Don't sweat.

22
00:01:23,930 --> 00:01:26,450
I, I am going to talk about that pretty soon.

23
00:01:26,650 --> 00:01:27,410
But guess what?

24
00:01:27,690 --> 00:01:29,130
For the prompt engineering.

25
00:01:29,170 --> 00:01:36,610
Yes, even for an AI agents or multi-agent systems, prompts are some of the most fundamental things

26
00:01:36,610 --> 00:01:37,730
that you are going to give.

27
00:01:37,770 --> 00:01:43,650
Pretty much like the large language models like cloud, sonnet model or the GPT models.

28
00:01:43,970 --> 00:01:50,410
These prompts are like a series of text which you are going to pass in to get the output from them.

29
00:01:50,690 --> 00:01:53,050
That's what is the prompt engineering over here.

30
00:01:53,050 --> 00:01:54,810
Just think of that as of now.

31
00:01:54,970 --> 00:02:00,020
And if you're going to be working with the AI agents or multi-agent systems, Prompt engineering is

32
00:02:00,020 --> 00:02:02,140
way beyond these these days.

33
00:02:02,500 --> 00:02:07,220
We call them as context engineering, which we are going to talk about that as well in our upcoming

34
00:02:07,260 --> 00:02:08,620
lectures of this section.

35
00:02:09,420 --> 00:02:15,740
So just take this simple example, which I have taken as a screenshot from the cloud desktop over here.

36
00:02:15,740 --> 00:02:21,500
Well, I'm going to talk about what I'm asking here that get me the locators for the page, this particular

37
00:02:21,500 --> 00:02:21,860
page.

38
00:02:22,260 --> 00:02:27,700
And you will notice that the moment I ask this question, the large language model, which is the sonnet

39
00:02:27,700 --> 00:02:34,260
4.5 model, which I'm using during the time of recording over here, you will notice that this particular

40
00:02:34,820 --> 00:02:39,140
website is something that the model wouldn't have trained with.

41
00:02:39,500 --> 00:02:46,900
So you will notice that now the model is invoking certain tools to go and search online to get the information

42
00:02:46,900 --> 00:02:47,620
about.

43
00:02:47,620 --> 00:02:54,820
So it's also fetching the entire HTML source code of the page so that it can go and find the locators

44
00:02:55,180 --> 00:02:56,180
of that page.

45
00:02:56,620 --> 00:02:58,270
So you will notice that now?

46
00:02:58,590 --> 00:03:06,190
With a single prompt that you just gave, the large language model is trying to invoke certain tools,

47
00:03:06,670 --> 00:03:10,190
like an AI agents, to perform these operations.

48
00:03:10,670 --> 00:03:14,790
And because I have not talked about the AI agents yet, I'm going to talk about that in our upcoming

49
00:03:14,790 --> 00:03:15,990
lectures pretty soon.

50
00:03:15,990 --> 00:03:20,870
But you will notice that just with single prompt, many operations are now taken care.

51
00:03:21,270 --> 00:03:22,190
But guess what?

52
00:03:22,190 --> 00:03:27,030
The locators that you have got over here may not be the format that you are looking for.

53
00:03:27,350 --> 00:03:33,830
So the moment we give more and more context to the large language model, we get more out of it and

54
00:03:33,830 --> 00:03:35,510
we get what we are looking for.

55
00:03:35,550 --> 00:03:42,750
Because at the moment you saw that the text that we are getting over here, like a locators are not

56
00:03:42,750 --> 00:03:44,870
in the format that we are looking for.

57
00:03:44,910 --> 00:03:50,350
Probably you are looking for locators, not just with the username field, password fields with all

58
00:03:50,350 --> 00:03:56,030
the locators you may be looking for locators like a JSON format for that matter, so that it can be

59
00:03:56,030 --> 00:04:02,590
used for your test automation code to see what exactly is this locator and what exactly is the value

60
00:04:02,590 --> 00:04:03,910
for that locator element.

61
00:04:04,390 --> 00:04:10,030
So if you want to get these kind of information, your prompt that you have got over here may not be

62
00:04:10,030 --> 00:04:10,510
enough.

63
00:04:11,150 --> 00:04:16,310
So for that matter, we can fine tune our prompt to get the information that we're looking for something

64
00:04:16,310 --> 00:04:17,110
like this.

65
00:04:17,110 --> 00:04:23,870
And as you can see, I'm here asking get me the locator for the page, this one in JSON format with

66
00:04:23,910 --> 00:04:25,710
the schema something like this.

67
00:04:26,110 --> 00:04:31,110
And this way it is going to go and do the exact same operation to go and fetch the locators from the

68
00:04:31,110 --> 00:04:33,110
page using the HTML content.

69
00:04:33,110 --> 00:04:37,430
But this time it's going to get you the information in JSON format, as you can see.

70
00:04:37,790 --> 00:04:44,670
So this is how you can see that one single prompt with a bit of a change can get you a very different

71
00:04:44,670 --> 00:04:51,070
result, which you may not be obtaining from the earlier prompt, because the earlier prompt was just

72
00:04:51,070 --> 00:04:52,110
very, very bland.

73
00:04:52,110 --> 00:04:55,670
By not giving enough details to the large language model.

74
00:04:55,670 --> 00:05:00,400
And now with this small change in the prompt, you are getting the information that you're looking for,

75
00:05:00,400 --> 00:05:01,280
which is amazing.

76
00:05:01,280 --> 00:05:06,160
And this is how you can see that the prompt engineering is going to get you the details that you're

77
00:05:06,160 --> 00:05:08,280
looking for in a very, very better way.

78
00:05:08,520 --> 00:05:15,880
But with prompt engineering alone, you won't be getting all the informations or details that you're

79
00:05:15,880 --> 00:05:16,600
looking for.

80
00:05:16,640 --> 00:05:23,080
That's why these days now, the prompt engineering has been superseded by what is called as context

81
00:05:23,080 --> 00:05:28,200
engineering, because we are now not just dealing with the large language model alone, but we are also

82
00:05:28,200 --> 00:05:31,640
dealing with a lot of different AI agents and tooling.

83
00:05:31,640 --> 00:05:35,160
And then the context engineering becomes super important.

84
00:05:35,520 --> 00:05:40,080
I will talk about the context engineering as well, but I know it's going to take a bit of head around

85
00:05:40,080 --> 00:05:45,920
for you to understand what exactly that I'm talking about, like prompt engineering and context engineering

86
00:05:46,120 --> 00:05:46,840
suddenly.

87
00:05:46,840 --> 00:05:53,240
But while you get all this detail and while we talk about the AI agents, you are going to get the complete

88
00:05:53,240 --> 00:05:55,920
picture of what exactly these puzzles are.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 3. Understanding Context Engineering

1
00:00:00,080 --> 00:00:00,600
All right.

2
00:00:00,640 --> 00:00:02,880
Now let's talk about context engineering.

3
00:00:02,880 --> 00:00:07,320
If you really watched about the prompt engineering before, this context engineering is going to give

4
00:00:07,320 --> 00:00:11,040
you even more information while we start talking about this.

5
00:00:11,040 --> 00:00:13,040
So what exactly is context engineering?

6
00:00:13,200 --> 00:00:18,960
Well, context engineering is a practice of strategically designing and structuring the information

7
00:00:18,960 --> 00:00:26,240
provided to the AI systems, particularly large language model and AI agents, to optimize their performance,

8
00:00:26,400 --> 00:00:28,880
accuracy and reliability.

9
00:00:29,360 --> 00:00:31,840
Think of this as a prompt engineering plus.

10
00:00:31,840 --> 00:00:39,120
So it's encompassing you, not just what you ask, but how you frame the entire informational environment.

11
00:00:39,320 --> 00:00:41,920
That's what exactly is the context engineering.

12
00:00:41,960 --> 00:00:47,800
See, last time when we asked in the prompt engineering like, can you get me the locators of a page?

13
00:00:47,800 --> 00:00:56,120
It got us the information by getting the information from an external page, reading all the information

14
00:00:56,120 --> 00:00:57,560
and then getting us the page.

15
00:00:57,600 --> 00:00:59,160
At least you just saw in the screenshot.

16
00:00:59,200 --> 00:01:04,980
We did not see any demo as such, which I'm going to show you pretty quickly, but you might see, like

17
00:01:05,020 --> 00:01:07,500
how amazing everything was happening.

18
00:01:07,500 --> 00:01:11,020
Like the large language model itself did not had any information.

19
00:01:11,020 --> 00:01:17,540
Then it went and invoked certain AI agents and toolings to get those information out.

20
00:01:17,860 --> 00:01:19,140
This was quite amazing.

21
00:01:19,340 --> 00:01:26,860
And in order to get that context, actually the large language model by itself took a brave approach

22
00:01:26,860 --> 00:01:28,580
to go and invoke the tools.

23
00:01:29,020 --> 00:01:35,300
But what if you're going to have a lot of information that you need for your project, which the large

24
00:01:35,300 --> 00:01:39,060
language model cannot just go and invoke by searching online?

25
00:01:39,780 --> 00:01:46,460
So during that time, context engineering becomes a paramount important technique for the large language

26
00:01:46,460 --> 00:01:48,900
model and AI agent to get all these information.

27
00:01:48,940 --> 00:01:51,500
And that is what is context engineering is all about.

28
00:01:52,100 --> 00:01:55,140
But why context engineering is so much essential?

29
00:01:55,500 --> 00:02:01,060
Well, context engineering will not only help the large language model to get all the information,

30
00:02:01,060 --> 00:02:07,800
but also it improves the accuracy of your large language model to get a well structured Shared context

31
00:02:07,800 --> 00:02:10,920
and get exactly what the information that you need.

32
00:02:11,120 --> 00:02:16,640
And also, it reduces the hallucination for the large language model because you provide a lot of relevant

33
00:02:16,640 --> 00:02:22,640
information and data, which can help you get the relevant output from the LMS as well.

34
00:02:23,040 --> 00:02:28,480
And similarly, the context is going to help to get the task specialization for your large language

35
00:02:28,480 --> 00:02:28,760
model.

36
00:02:28,760 --> 00:02:34,720
For example, you can get a domain specific information to the large language model, and you will get

37
00:02:34,720 --> 00:02:41,840
the output from the LMS based on that, pretty much like a domain specific tools, without retraining

38
00:02:41,840 --> 00:02:43,800
your entire large language model.

39
00:02:44,080 --> 00:02:50,360
And finally, you're also going to get the output in a guided format and tones and structures pretty

40
00:02:50,360 --> 00:02:53,520
much like how you wanted to get like a JSON format for that matter.

41
00:02:53,640 --> 00:02:57,120
That's all going to happen because of the context engineering.

42
00:02:57,640 --> 00:03:00,600
And I hope you got the idea how this context engineering really works.

43
00:03:00,760 --> 00:03:07,600
And just to give you an example of that, let's say you want to get a context for the large language

44
00:03:07,600 --> 00:03:09,720
model, like how we just saw in the demo.

45
00:03:10,040 --> 00:03:14,940
But here we're going to go a little further where we are going to say, hey, large language model.

46
00:03:14,940 --> 00:03:19,020
Can you write a test for me in selenium for the given page?

47
00:03:19,020 --> 00:03:25,260
So basically you are going to give the entire page as a context to a large language model, and the

48
00:03:25,260 --> 00:03:31,260
large language model is going to process the entire locators and the scenarios that it can test.

49
00:03:31,460 --> 00:03:37,140
And then it is going to write the test in the selenium format, something like this as a code.

50
00:03:37,500 --> 00:03:42,540
So this is how you can see that this is the context that you are giving to your large language model

51
00:03:42,540 --> 00:03:44,380
to get the informations out.

52
00:03:44,380 --> 00:03:50,940
But you may now ask what is the better way of doing it other than just giving the entire page?

53
00:03:50,940 --> 00:03:52,460
As you can see over here?

54
00:03:52,860 --> 00:03:53,740
Well guess what?

55
00:03:53,900 --> 00:04:00,060
You can improve the context of your large language model with many different techniques, not just parsing

56
00:04:00,060 --> 00:04:05,020
the entire page as you can see over here, but you can also do it in a many different way.

57
00:04:05,140 --> 00:04:07,580
Something like system prompts and instructions.

58
00:04:07,580 --> 00:04:12,860
So you can do a preloaded instruction for your large language model so that you can always follow.

59
00:04:12,900 --> 00:04:18,880
What exactly is the part of the page that the elements need to go and look at.

60
00:04:20,040 --> 00:04:26,080
And also you can see that these days the large language model gets the context, not just using the

61
00:04:26,080 --> 00:04:31,480
system prompts or the page that you gave it, but also with the conversation history so that you can

62
00:04:31,480 --> 00:04:36,320
get you the relevant information based on the conversation that you did with the large language model

63
00:04:36,320 --> 00:04:39,880
earlier, or if you want to do even further information.

64
00:04:39,880 --> 00:04:45,800
For example, the page that you gave may help you write a test with the power of llms.

65
00:04:45,960 --> 00:04:52,200
But what if the application has got some of the functionalities which the LMS has no idea about?

66
00:04:52,440 --> 00:04:57,920
So if you get more information like the requirement documents or the scenario documents to the large

67
00:04:57,920 --> 00:05:04,840
language model, then it can write the test based on the information which is available on those context.

68
00:05:04,840 --> 00:05:11,480
And those things you can retrieve using a document or Rag operation like retrieval, augmented generation,

69
00:05:11,480 --> 00:05:13,240
or maybe a search results.

70
00:05:13,240 --> 00:05:18,780
So all of these can be helpful for the large language model to get you the relevant code that you are

71
00:05:18,780 --> 00:05:19,500
looking for.

72
00:05:19,500 --> 00:05:24,660
And similarly, if you give the large language model some structured context file like instruction.md

73
00:05:24,660 --> 00:05:32,100
file or chat modes or agent.md files, these are going to be even more helpful for the llms to perform

74
00:05:32,100 --> 00:05:33,180
all these operations.

75
00:05:33,220 --> 00:05:38,940
And finally, the real time environment like the file system database access, could also be helping

76
00:05:38,940 --> 00:05:41,980
the large language model to get more and more information.

77
00:05:42,220 --> 00:05:47,020
I know it's a lot of things to digest in this particular lecture, as well as in this section.

78
00:05:47,300 --> 00:05:53,060
We are going to talk all of these information as a demo, and then you will understand how amazing the

79
00:05:53,060 --> 00:05:59,540
context engineering plays a key role for you to write a better test code with the power of large language

80
00:05:59,540 --> 00:05:59,780
model.

81
00:05:59,820 --> 00:06:04,420
Well, if you have got all the ideas so far about the prompt engineering and context engineering so

82
00:06:04,420 --> 00:06:09,500
far, in our next lecture, I'll quickly show you a demo of how the context engineering plays a key

83
00:06:09,540 --> 00:06:16,060
role in how your prompt plays a key role while you try to interact with your large language models.

84
00:06:16,060 --> 00:06:21,940
And then we'll talk about the AI agents, and you will see how everything is going to make much sense.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 4. Demo on Prompt Engineering

1
00:00:00,080 --> 00:00:05,240
In this lecture, we're going to see how the Claude Sonet model can get you the information that you're

2
00:00:05,240 --> 00:00:10,680
looking for, using prompt, as well as the context engineering that we were talking in our earlier

3
00:00:10,680 --> 00:00:12,240
lectures of this section.

4
00:00:12,440 --> 00:00:17,160
Well, in order to do that, I'm going to do the exact same prompting this time, and it will show you

5
00:00:17,160 --> 00:00:21,000
how the large language model is going to get those information out for you.

6
00:00:21,120 --> 00:00:24,240
So let's say I'm going to automate this particular application.

7
00:00:24,240 --> 00:00:28,680
And I wanted to get all the locators of this particular page that I wanted to test.

8
00:00:29,040 --> 00:00:33,760
And you will notice that this particular application has got quite some locators in the home page.

9
00:00:33,880 --> 00:00:35,600
But let's see the login page.

10
00:00:35,600 --> 00:00:39,880
Really this particular login page has got some textbox over here.

11
00:00:39,920 --> 00:00:41,320
It has got some label.

12
00:00:41,360 --> 00:00:47,440
It also has got a Remember Me checkbox, a login button and there is a register as a new page link over

13
00:00:47,440 --> 00:00:47,880
here.

14
00:00:48,040 --> 00:00:52,280
It has got some text over there as well and there are some menu items.

15
00:00:52,520 --> 00:00:57,680
Let's say I wanted to really get all the locators of this particular page so that I can start testing

16
00:00:57,680 --> 00:00:58,000
it.

17
00:00:58,280 --> 00:01:05,360
And what we usually do for asking the question or prompting the large language model is we just go to

18
00:01:05,400 --> 00:01:08,000
the window over here in the cloud desktop.

19
00:01:08,000 --> 00:01:13,400
If you are using ChatGPT or local large language model, you can do the exact same thing that I'm doing

20
00:01:13,400 --> 00:01:14,240
over here.

21
00:01:14,240 --> 00:01:16,080
I am using the cloud desktop.

22
00:01:16,080 --> 00:01:18,800
That is the reason why you can see that this particular window comes in.

23
00:01:18,800 --> 00:01:23,200
But if you are someone who is fan of the ChatGPT, you can also do that.

24
00:01:23,200 --> 00:01:26,280
It's going to do the exact same operation that you're going to be doing over here.

25
00:01:26,600 --> 00:01:32,600
And note that within this cloud desktop, there is a knob over here where it tells you that it has the

26
00:01:32,600 --> 00:01:39,520
ability to do a web search, which means it can go and search online to get the information for you.

27
00:01:39,520 --> 00:01:46,200
But if I turn this web search off as well as the file system off over here, you will notice that it

28
00:01:46,200 --> 00:01:52,720
is going to get you the information from what it has already trained or nothing, but what the large

29
00:01:52,720 --> 00:01:58,720
language model, which is a sonnet 4.5 model, has already been trained to get you the responses.

30
00:01:58,920 --> 00:02:00,240
That is what is going to happen.

31
00:02:00,800 --> 00:02:08,560
But the moment you gonna enable this web search feature, it can go and search online to get the information

32
00:02:08,560 --> 00:02:09,120
for you.

33
00:02:09,120 --> 00:02:14,720
That is, what is this particular web search tool, or this is the tool that I'm really going to talk

34
00:02:14,720 --> 00:02:16,840
about when we talk about the AI agents.

35
00:02:16,840 --> 00:02:24,440
But this is already a tool which is built by the cloud team to show you like how it is going to go and

36
00:02:24,440 --> 00:02:25,520
search online.

37
00:02:25,520 --> 00:02:32,240
But because I have disabled the, uh, the web search capability right now, and if I'm going to say,

38
00:02:32,400 --> 00:02:42,200
can you get me the locators of the page and if I'm going to and if I'm going to just copy this particular

39
00:02:42,200 --> 00:02:44,320
URL and paste it over here.

40
00:02:44,480 --> 00:02:51,240
And because you will see that now the large language model is kind of handicapped to get the information

41
00:02:51,280 --> 00:03:00,760
online, it is going to start doing a code writing for you for the locators, just by doing whatever,

42
00:03:00,760 --> 00:03:02,960
that it has the information already.

43
00:03:03,000 --> 00:03:08,000
You see that now it says that I can't directly access the external website or extract locators from

44
00:03:08,000 --> 00:03:08,880
the live page.

45
00:03:08,880 --> 00:03:11,800
However, I can help you, uh, in a few ways.

46
00:03:12,000 --> 00:03:14,560
Just going to guide me like how you can do it.

47
00:03:14,560 --> 00:03:17,590
And it's also telling me, like how you can actually do these operations.

48
00:03:17,590 --> 00:03:23,910
It's really not even generating the code, but it's trying to guide me these days because it don't have

49
00:03:23,910 --> 00:03:30,310
any real time information, because we have just made it handicapped to not do any of these operations.

50
00:03:30,310 --> 00:03:36,350
But the moment I'm going to enable this web search and if I'm going to do a try again, and if I hit

51
00:03:36,350 --> 00:03:42,390
enter now, what's going to happen is the cloud desktop has got the access to the external world, and

52
00:03:42,390 --> 00:03:44,830
it's going to start doing a fetch operation.

53
00:03:44,870 --> 00:03:50,150
It's also going to get the full HTML structure of the complete page to get the locators.

54
00:03:50,310 --> 00:03:55,270
And you can see that it is starting to get all the information, like a real time information.

55
00:03:55,270 --> 00:04:01,750
You can see that the same name ID, CSS selectors and XPath are available for these particular controls.

56
00:04:01,750 --> 00:04:07,790
So if I'm going to go inspect this particular page and if I'm going to see what is the ID, you see

57
00:04:07,790 --> 00:04:10,830
that the ID is username, the name is username.

58
00:04:10,830 --> 00:04:16,390
And you can also find the thing using the XPath that it has given over here, and also using the CSS

59
00:04:16,390 --> 00:04:16,950
selector.

60
00:04:16,990 --> 00:04:18,630
These are all quite right.

61
00:04:19,350 --> 00:04:25,790
So these are all the real information or real time information that we are getting out from the cloud

62
00:04:25,830 --> 00:04:26,590
desktop.

63
00:04:26,590 --> 00:04:34,830
So this is the power of how we can use the Toolings or the AI agents of Cloud Desktop, which is configured

64
00:04:34,830 --> 00:04:38,070
to get a real time information for the large language model.

65
00:04:38,110 --> 00:04:43,190
See, even though the large language model is not trained with the page that we have just given over

66
00:04:43,190 --> 00:04:49,950
here, it is still getting us the information because it is now using the tools or the AI agents to

67
00:04:49,990 --> 00:04:51,390
get these information.

68
00:04:51,390 --> 00:04:56,150
So that gets the contexts for the large language model already.

69
00:04:56,190 --> 00:05:01,830
But now I'm going to give even more context to the large language model to get the formulated data that

70
00:05:01,830 --> 00:05:02,670
I'm looking for.

71
00:05:02,670 --> 00:05:08,750
For instance, I don't just want to get the locators like this, but rather I want to do like I want

72
00:05:08,750 --> 00:05:11,670
to get the locators for the username field.

73
00:05:11,870 --> 00:05:16,070
And what is the locator and what is its value.

74
00:05:16,110 --> 00:05:16,350
Right.

75
00:05:16,350 --> 00:05:17,230
That's what I want to get.

76
00:05:17,230 --> 00:05:19,910
So basically I want to get three items over there.

77
00:05:19,910 --> 00:05:25,470
So I'm going to say can you get me the locators of the page.

78
00:05:25,750 --> 00:05:27,430
And I'm going to pass this particular pitch.

79
00:05:27,870 --> 00:05:31,950
Get me in the JSON format.

80
00:05:31,950 --> 00:05:35,390
So I'm telling that I want to get the JSON format over here.

81
00:05:35,590 --> 00:05:40,590
And I'm going to say the format should be the locator name.

82
00:05:41,670 --> 00:05:42,230
Right.

83
00:05:42,510 --> 00:05:47,030
And I also want to get the locator value.

84
00:05:47,230 --> 00:05:52,430
And I want it to get based on the locator type as well.

85
00:05:52,430 --> 00:05:56,350
So basically we just say locator type and then locator value, which I think that is the better way

86
00:05:56,350 --> 00:06:04,230
of saying it, because let's say you wanted to get the details of this particular username.

87
00:06:04,230 --> 00:06:08,390
Then you can say I want to get the locator name as the username.

88
00:06:08,390 --> 00:06:12,870
And the type is going to be let's say name or ID or the XPath.

89
00:06:12,990 --> 00:06:20,270
And then the value of them like hash username or dot username or slash uh XPath username, something

90
00:06:20,270 --> 00:06:20,830
like that.

91
00:06:20,870 --> 00:06:22,950
That is what I really wanted to get it right.

92
00:06:22,990 --> 00:06:29,750
And I'm also going to say get me the locators in a unique format.

93
00:06:30,430 --> 00:06:32,630
So I'm just going to say like a unique locator, probably.

94
00:06:32,630 --> 00:06:34,190
So get me the unique locator.

95
00:06:34,230 --> 00:06:35,710
That's better way of saying it.

96
00:06:36,030 --> 00:06:41,230
Um, for each element in the page.

97
00:06:41,950 --> 00:06:45,350
And I'm gonna hit run over here.

98
00:06:45,710 --> 00:06:50,630
See, this is the context which I'm going to give in for the large language model.

99
00:06:50,790 --> 00:06:53,790
And now it is going to go and fetch the information.

100
00:06:53,910 --> 00:06:57,670
And then it is going to query the data that is looking for.

101
00:06:57,670 --> 00:07:03,470
So this is a bit of a structured prompt that we have given to get the output.

102
00:07:03,510 --> 00:07:07,430
I mean even though I have not really given the context because the context itself is being searched

103
00:07:07,470 --> 00:07:13,030
online by the large language model, automatically it is going to get all the informations over here.

104
00:07:13,070 --> 00:07:13,390
See that?

105
00:07:13,390 --> 00:07:19,070
Now it says locator name is a username input field and the locator type is ID and locator value is this

106
00:07:19,070 --> 00:07:19,430
one.

107
00:07:19,470 --> 00:07:21,190
See this is pretty cool.

108
00:07:21,190 --> 00:07:23,510
So this is the two unique way of identifying it.

109
00:07:23,550 --> 00:07:29,390
Similarly for the password for the Remember Me checkbox and all of these operations see.

110
00:07:29,390 --> 00:07:33,950
Now it's also getting the navigation as well for me over here, which is pretty cool.

111
00:07:34,350 --> 00:07:41,020
But now uh, you can ask like you have just modified the prompt a bit and you got the information,

112
00:07:41,020 --> 00:07:47,340
but the context of this particular page is being given by the large language model itself by fetching

113
00:07:47,340 --> 00:07:48,020
online.

114
00:07:48,260 --> 00:07:50,820
But what if I don't have online access?

115
00:07:51,020 --> 00:07:54,740
I still want to give the context to the large language model.

116
00:07:54,780 --> 00:07:55,900
How can I actually do that?

117
00:07:56,140 --> 00:08:01,060
Well guess what, you can actually do that using the page source code itself.

118
00:08:02,180 --> 00:08:07,220
Basically, you can get the entire page source code, which is nothing but over here.

119
00:08:07,260 --> 00:08:12,900
See, this is the block for instance, you are interested in, not the entire page, but just this particular

120
00:08:12,900 --> 00:08:17,860
block of the page that you're interested in, which you want to supply as a context to your large language

121
00:08:17,860 --> 00:08:18,300
model.

122
00:08:18,540 --> 00:08:19,740
You can also do that.

123
00:08:19,780 --> 00:08:20,580
Well guess what?

124
00:08:20,860 --> 00:08:28,060
You can just copy the element that you wanted, and then you can paste it to the cloud desktop over

125
00:08:28,060 --> 00:08:30,260
here and you can get the output.

126
00:08:30,300 --> 00:08:36,300
I will let you to do it right now and see if you can able to do it by disabling this particular web

127
00:08:36,300 --> 00:08:39,500
search, and see if you're going to get the same kind of locators.

128
00:08:39,580 --> 00:08:42,860
If not, we are going to do that in our next lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 5. Demo on Context Engineering

1
00:00:00,080 --> 00:00:00,880
All right.

2
00:00:00,920 --> 00:00:07,040
Hopefully you tried passing the entire page as a context, or at least a section of the page as a context,

3
00:00:07,040 --> 00:00:12,320
so that you can get the relevant locators from the page if you have really not done that.

4
00:00:12,360 --> 00:00:13,160
No worries.

5
00:00:13,160 --> 00:00:14,400
Let's try doing it.

6
00:00:14,440 --> 00:00:15,080
Well guess what?

7
00:00:15,080 --> 00:00:16,160
My idea is this.

8
00:00:16,200 --> 00:00:22,040
In this particular page I don't want to get the login register, employee list and all these links,

9
00:00:22,040 --> 00:00:28,040
but I just interested in to get this particular locators from this particular page.

10
00:00:28,280 --> 00:00:33,800
See these things are going to be the foundation element that we are going to be taking as an input.

11
00:00:33,800 --> 00:00:40,120
While we are going to start doing automation test like a smarter automation test using selenium or playwright

12
00:00:40,400 --> 00:00:46,800
for a self-correcting mechanisms in our upcoming sections of this course.

13
00:00:46,800 --> 00:00:52,400
So make sure that you understand these concepts clearly, so that you can get to know how important

14
00:00:52,400 --> 00:00:59,120
the contexts and prompts are while we start designing them in our automation test code later on.

15
00:00:59,280 --> 00:01:02,320
Well, as I said, I'm going to go and take this particular block.

16
00:01:02,320 --> 00:01:06,640
As you can see, it has got all the locators, which I'm looking for in this particular due control.

17
00:01:06,640 --> 00:01:11,130
So I'm going to go and grab this information, I'm going to copy this element.

18
00:01:11,130 --> 00:01:16,890
And then I can pass this as a context to our large language model to get the locators I'm looking for.

19
00:01:16,890 --> 00:01:20,250
So maybe I'm going to copy the same prompt that I wanted.

20
00:01:20,250 --> 00:01:22,090
And I'm going to paste it over here.

21
00:01:22,210 --> 00:01:26,370
But I need to pass this particular element as well.

22
00:01:26,370 --> 00:01:28,250
So I'm going to go copy this element.

23
00:01:28,250 --> 00:01:31,610
I'm going to probably disable the web search this time.

24
00:01:31,610 --> 00:01:34,050
So I'm not going to get any real time information.

25
00:01:34,090 --> 00:01:39,370
Rather I'm going to pass this information over here as a contexts.

26
00:01:39,530 --> 00:01:46,730
And now if I'm going to try entering it over here, you will notice that it should not ideally go and

27
00:01:46,730 --> 00:01:49,170
get the page from online.

28
00:01:49,170 --> 00:01:54,610
Rather, you see that now it's going to get the same information right from the context that we gave

29
00:01:54,970 --> 00:01:57,010
and got the information that we're looking for.

30
00:01:57,370 --> 00:01:58,290
Look at that.

31
00:01:58,410 --> 00:02:00,130
It is quite amazing.

32
00:02:00,130 --> 00:02:06,690
So it has got the logo of the image, the form and the request verification token as well, which is

33
00:02:06,690 --> 00:02:12,050
nice because I have not even asked it to do it, but it also gave me the username input, the username

34
00:02:12,050 --> 00:02:18,180
label, the user validation message, the password input password label and whatnot.

35
00:02:18,180 --> 00:02:22,380
So it has given me all the locators alone, which is quite neat.

36
00:02:22,420 --> 00:02:24,580
Now it is not even doing an online search.

37
00:02:24,620 --> 00:02:31,820
Rather, it is getting all the information from the input of HTML source code that I gave, and it just

38
00:02:31,820 --> 00:02:33,300
gave me all the information.

39
00:02:33,460 --> 00:02:34,460
This is fast.

40
00:02:34,740 --> 00:02:40,940
This is how you can see that you can give the context to your large language model, and it gets you

41
00:02:40,940 --> 00:02:42,500
the information that you're looking for.

42
00:02:42,980 --> 00:02:49,860
And now in order to demonstrate this a little further, you can actually use other AI agents and toolings

43
00:02:49,860 --> 00:02:57,380
as well, using the power of model context protocols and other details and other stuffs, which makes

44
00:02:57,380 --> 00:02:59,580
your cloud even more smarter.

45
00:02:59,860 --> 00:03:07,260
For example, you can even let the cloud desktop to harness the power of model context protocols to

46
00:03:07,300 --> 00:03:09,700
get the real time information of your page.

47
00:03:09,820 --> 00:03:17,060
And then it will start getting the locators not just using the web search functionality, but also using

48
00:03:17,180 --> 00:03:20,740
the third party tools which are available to make that happen.

49
00:03:20,740 --> 00:03:26,550
For example, if you just go to the cloud desktop over here, there's something called as add connectors

50
00:03:26,790 --> 00:03:32,230
and using this connectors you can also see that they also have got something like Control Chrome.

51
00:03:32,390 --> 00:03:36,470
So this control chrome can help you do a lot of different operations.

52
00:03:36,470 --> 00:03:42,630
For instance opening the URL, get the current tab, list the tabs, close the tab, switch tab, get

53
00:03:42,630 --> 00:03:45,790
page content, execute JavaScript, and more.

54
00:03:45,990 --> 00:03:57,350
So if you install this particular extension or maybe a tool, an agent, it can actually make your large

55
00:03:57,350 --> 00:04:03,150
language model to get even more context that is used to perform those operations.

56
00:04:03,150 --> 00:04:10,270
And let's say if you wanted to test this particular UI of your application and you have a business requirement

57
00:04:10,270 --> 00:04:17,110
like how the username should be, how the password format should be, and how the Remember Me checkbox

58
00:04:17,110 --> 00:04:20,070
really works, and how the register as a new user really works.

59
00:04:20,070 --> 00:04:27,190
And if you have many business scenarios and you want the cloud desktop to really understand how it can

60
00:04:27,190 --> 00:04:28,750
be done, well guess what?

61
00:04:28,750 --> 00:04:35,960
You can actually give a lot of contexts to the large language model by passing the the file that you

62
00:04:36,000 --> 00:04:36,560
are looking for.

63
00:04:36,560 --> 00:04:38,920
So you can also upload a file over here.

64
00:04:39,080 --> 00:04:41,880
Uh, for instance, you have all the requirement documents.

65
00:04:41,880 --> 00:04:44,640
You can pass it over here in the upload a file.

66
00:04:44,760 --> 00:04:52,680
Or you can also use your GitHub where you have got all the code, which helps you, uh, test this particular

67
00:04:52,680 --> 00:04:54,040
application in a better way.

68
00:04:54,080 --> 00:04:56,840
Maybe even a unit test can also help do that.

69
00:04:56,840 --> 00:05:01,920
Also, you can also pass the SharePoint page of your application so that it can get you that information

70
00:05:01,920 --> 00:05:02,320
as well.

71
00:05:02,320 --> 00:05:04,600
So you can do all sort of things over here.

72
00:05:04,600 --> 00:05:05,480
And guess what?

73
00:05:05,520 --> 00:05:12,400
Even with the power of the chat conversation, the large language model can understand what exactly

74
00:05:12,400 --> 00:05:17,680
you're talking about so that it can get you the information that you are exactly looking for instead

75
00:05:17,680 --> 00:05:20,080
of just getting an hallucinated message.

76
00:05:20,080 --> 00:05:23,320
So these are going to be the context for your large language model.

77
00:05:23,320 --> 00:05:29,160
While it gets the information that you are looking for in real time and hope you got the idea of what

78
00:05:29,160 --> 00:05:34,440
context engineering are and what prompts engineering are now next lecture, we'll talk about the AI

79
00:05:34,480 --> 00:05:41,320
agents and how a simple AI agent can actually perform so many wonderful operations.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 6. Understanding AI Agents and how it works !

1
00:00:00,080 --> 00:00:02,120
Understanding AI agents.

2
00:00:02,680 --> 00:00:08,280
This is one of the most important lecture that you need to understand how this AI agents really works.

3
00:00:08,440 --> 00:00:11,840
Well, we know that 2025 is the year of AI agents.

4
00:00:11,880 --> 00:00:18,000
Every big company on the planet wants to harness the power of large language models, and use AI agents

5
00:00:18,000 --> 00:00:19,200
as the way to do it.

6
00:00:19,200 --> 00:00:22,080
And if you ask me why exactly this is happening?

7
00:00:22,200 --> 00:00:23,080
Well guess what?

8
00:00:23,520 --> 00:00:28,960
AI agents are rapidly becoming the future of building large language model based AI application.

9
00:00:29,120 --> 00:00:35,360
And every single company, as I told you on the slide, is harnessing the power of AI agents and large

10
00:00:35,360 --> 00:00:36,240
language model.

11
00:00:36,280 --> 00:00:42,000
Even though they have not really achieved the full potential or gained the full potential of the AI

12
00:00:42,040 --> 00:00:42,880
agents yet.

13
00:00:43,080 --> 00:00:46,520
Already companies are building so many applications on top of it.

14
00:00:46,520 --> 00:00:53,920
For instance, the Microsoft 365 copilot already has got an agent stores, which has got so many agents,

15
00:00:53,920 --> 00:00:59,040
which is evolving every single day like a visual creator, agent, prompt coach, agent.

16
00:00:59,080 --> 00:01:01,980
Writing coach, agent, career coach, agent.

17
00:01:01,980 --> 00:01:08,340
You can see that there are so many agents these days, and every single agent is making a lot of different

18
00:01:08,380 --> 00:01:14,820
operation for you, which are very task oriented and very much focused on a specific goal to get the

19
00:01:14,820 --> 00:01:16,180
operation done for you.

20
00:01:16,180 --> 00:01:20,340
This is quite amazing and there are many more stores available as well.

21
00:01:20,340 --> 00:01:26,020
You will be wondering like how these are just coming up, for example, ServiceNow and Salesforce and

22
00:01:26,020 --> 00:01:32,220
any company that you take, it has got an AI agent store these days, and even postman has got the agent

23
00:01:32,220 --> 00:01:32,780
stores.

24
00:01:32,940 --> 00:01:39,340
And even like zebra for example, they have got invoice validation agent, the order entry management

25
00:01:39,340 --> 00:01:41,340
agent, contract validation agent.

26
00:01:41,460 --> 00:01:45,380
So many agent does exist and these things are going to keep on changing.

27
00:01:45,380 --> 00:01:48,780
If you're going to be watching this video probably another couple of years.

28
00:01:48,820 --> 00:01:55,420
These things might be completely obsolete by then because the agents are just evolving in a rocket speed

29
00:01:55,420 --> 00:01:56,020
these days.

30
00:01:56,820 --> 00:02:02,890
And if you see this particular company does despite they also have got an agent, especially for testing.

31
00:02:02,930 --> 00:02:08,370
Operation which can just do our end to end test operation by giving the application.

32
00:02:08,410 --> 00:02:09,610
Like an MCP server.

33
00:02:09,730 --> 00:02:11,850
And it's going to do all these operations for you.

34
00:02:11,890 --> 00:02:13,970
This is how the agents are right now.

35
00:02:14,010 --> 00:02:19,650
And now if you want to really learn about the building of AI agents and how do you test these AI agents,

36
00:02:19,650 --> 00:02:24,490
I probably recommend you to go and watch my other course, which is available in Udemy already, which

37
00:02:24,490 --> 00:02:29,490
is called as build AI and Multi-agent Systems Tools for Software Testing.

38
00:02:29,650 --> 00:02:34,610
This course actually is available in Udemy and also part of the Udemy for business, where you can see

39
00:02:34,610 --> 00:02:40,610
that you can actually understand how this AI agents really works, how the multi-agent system works,

40
00:02:40,610 --> 00:02:47,090
and how you can build your own agents using long chain and other tools to perform document reading.

41
00:02:47,290 --> 00:02:52,850
Uh, storing in the vector data stores using the Rag operation, building your own AI agents and MCP

42
00:02:52,890 --> 00:02:54,050
servers and tools.

43
00:02:54,370 --> 00:02:56,770
This course is quite amazing.

44
00:02:56,810 --> 00:03:02,430
And not only that, you can build your own enterprise grade applications and AI agents using this particular

45
00:03:02,430 --> 00:03:06,430
course called as build and test AI agents, chatbots, Rag and Olama.

46
00:03:06,630 --> 00:03:07,510
But guess what?

47
00:03:07,790 --> 00:03:13,070
The moment you start getting into this particular field, you will start to know so many details are

48
00:03:13,070 --> 00:03:14,870
really evolving as a mushroom.

49
00:03:15,070 --> 00:03:19,870
Well, as I said, this is what is this AI agents is all about.

50
00:03:19,870 --> 00:03:25,670
And understanding the concept of AI agents, at least for this course, is also very important because

51
00:03:25,670 --> 00:03:27,270
you will be dealing with AI agent.

52
00:03:27,270 --> 00:03:32,830
Anyways, while we start talking about the vibe coding in our upcoming lectures of this particular section.

53
00:03:32,830 --> 00:03:36,870
Well, as that said, an AI agent can be defined in several ways.

54
00:03:36,870 --> 00:03:42,830
Some define agent as a fully autonomous system that operates independently or extended period using

55
00:03:42,830 --> 00:03:45,150
various tools to accomplish the complex task.

56
00:03:45,510 --> 00:03:52,510
Others use the term to describe more prospective implementation that follows predefined workflow, and

57
00:03:52,510 --> 00:03:58,540
the AI agent enhances the effectiveness of an AI systems overall, which will enable the large language

58
00:03:58,540 --> 00:04:00,580
model to interact with the external world.

59
00:04:00,620 --> 00:04:04,460
Remember, this is the exact same thing that we just did in our cloud desktop.

60
00:04:04,460 --> 00:04:09,540
While we were asking the cloud desktop to go and get the locators of a specific page.

61
00:04:09,820 --> 00:04:17,700
While we enabled the web search agent, it went and fetched the real time information of the page by

62
00:04:17,740 --> 00:04:23,340
getting the source code of the page, by getting the HTML of the page, and then got the locators details

63
00:04:23,380 --> 00:04:29,020
automatically because it enhanced the effectiveness of the AI system overall.

64
00:04:29,380 --> 00:04:31,380
That is the power of the AI agent.

65
00:04:31,380 --> 00:04:34,300
That's why I was telling you AI agents are awesome.

66
00:04:34,580 --> 00:04:39,620
You don't even need to fine tune your large language model or train your large language model with all

67
00:04:39,660 --> 00:04:41,340
the information available on the planet.

68
00:04:41,340 --> 00:04:47,060
Rather, just get the AI agent to do it for the large language model, because now the AI agent can

69
00:04:47,060 --> 00:04:53,060
go and step in, sneak in your real file systems or the websites, and get the information that you're

70
00:04:53,060 --> 00:04:59,080
looking for, which can be used for the large language model to understand, to get a whole picture

71
00:04:59,240 --> 00:05:04,080
of the application before it starts getting you the information, which is quite awesome.

72
00:05:04,080 --> 00:05:11,800
Well, as that said, an AI agent really thinks, desired and acts on behalf of the large language model.

73
00:05:11,800 --> 00:05:15,960
And now all these operations just magically happens for you.

74
00:05:15,960 --> 00:05:20,640
Well, even though thinking and deciding is not part of the AI agent, the Act operation is certainly

75
00:05:20,640 --> 00:05:24,560
is the operation of the AI agent which does everything for you.

76
00:05:24,600 --> 00:05:31,320
Well, as that said, I'll quickly talk about how these AI agents really works with various different

77
00:05:31,320 --> 00:05:33,440
tools to perform these operations.

78
00:05:33,440 --> 00:05:39,080
So we saw that in AI agent systems, there is this concept of toolings very, very important.

79
00:05:39,080 --> 00:05:46,120
For example, the web search actually has got a tool to go and search online to perform the operation

80
00:05:46,120 --> 00:05:46,920
in the internet.

81
00:05:46,920 --> 00:05:50,840
So that is basically a tool which does all these functionality for you.

82
00:05:50,880 --> 00:05:57,860
Similarly, you can build your own custom tools and Techniques to read a file, query a database running

83
00:05:57,860 --> 00:05:59,660
the test script, or calling an API.

84
00:05:59,660 --> 00:06:04,100
So all these can be performed using these tools in the AI agent.

85
00:06:04,300 --> 00:06:10,260
And one of the example of the Toolings and the AI agents is the model contest protocol, or otherwise

86
00:06:10,260 --> 00:06:11,420
called as MCP.

87
00:06:11,820 --> 00:06:19,660
Well, MCP is a newly open source standard which is designed to help the AI assistants work more effectively

88
00:06:19,660 --> 00:06:24,260
by connecting them to the systems and tools where relevant data really resides.

89
00:06:24,780 --> 00:06:29,900
And we have already used a bit of MCP, not exactly the MCP itself.

90
00:06:29,900 --> 00:06:35,780
I showed you briefly about the Chrome tool of the cloud desktop using the connector.

91
00:06:36,140 --> 00:06:38,380
That's actually an MCP itself.

92
00:06:38,740 --> 00:06:48,060
It can work in a server client architecture, where your cloud desktop will act as a client, and the

93
00:06:48,180 --> 00:06:54,130
Chrome is basically a server which performs the operation, which is going to be basically going on

94
00:06:54,130 --> 00:06:56,130
the internet and searching it for you.

95
00:06:56,130 --> 00:06:58,490
But you can also have many different servers.

96
00:06:58,490 --> 00:07:04,090
For instance, if you can have MCP server to access a local file system, you can also have MCP server

97
00:07:04,130 --> 00:07:08,250
to connect to the slack or even the browsers and things.

98
00:07:08,250 --> 00:07:11,690
So all of these can be done with the power of the MCP server.

99
00:07:11,730 --> 00:07:16,690
And as I told you again, this particular course already has got those information where you can build

100
00:07:16,690 --> 00:07:23,410
your own MCP servers as well, like playwright, MCP server or file system, MCP servers and things.

101
00:07:23,410 --> 00:07:29,010
But again, these things are something which are going to make your life even more easier while you

102
00:07:29,010 --> 00:07:31,290
build your own MCP servers as well.

103
00:07:31,330 --> 00:07:32,250
But guess what?

104
00:07:32,290 --> 00:07:38,170
Even though it is not relevant for this course, it is super important for you to understand that MCP

105
00:07:38,210 --> 00:07:45,330
servers are the way how you interact with these toolings and how large language model access those toolings

106
00:07:45,330 --> 00:07:46,530
with MCP server.

107
00:07:46,570 --> 00:07:51,410
I'll quickly show you a demo in our next lecture, like how these things work, but this is what is

108
00:07:51,410 --> 00:07:53,570
all about the AI agents.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 7. Working with MCP (Model Context Protocol) Server of Playwright

1
00:00:00,120 --> 00:00:05,040
In this lecture, I'm going to quickly show you an MCP server, which can help you interact with the

2
00:00:05,040 --> 00:00:09,880
web page and also write some test code, which is going to be amazing, right?

3
00:00:09,920 --> 00:00:11,640
We'll see how it can be achieved.

4
00:00:11,680 --> 00:00:16,640
In order to show you, I'm going to use an MCP server called as playwright MCP server.

5
00:00:16,720 --> 00:00:18,240
We're going to go and search online.

6
00:00:18,240 --> 00:00:22,800
You can see that this is the page which is going to come in the Microsoft Playwright MCP server.

7
00:00:22,800 --> 00:00:25,000
So you can go and click this particular link over here.

8
00:00:25,040 --> 00:00:30,760
It's going to take you to this particular GitHub page over here where you can see that how you can configure

9
00:00:30,760 --> 00:00:31,960
an MCP server.

10
00:00:32,120 --> 00:00:35,360
This is the configuration that you need in order to make this happen.

11
00:00:35,400 --> 00:00:39,840
As I told you, the MCP server act as a client server architecture.

12
00:00:39,840 --> 00:00:43,000
You need a client and then you need a bunch of servers.

13
00:00:43,640 --> 00:00:50,920
And this MCP server is basically an server, which you can just use it as an server to perform the operation

14
00:00:50,920 --> 00:00:51,880
that you're looking for.

15
00:00:52,080 --> 00:00:58,760
And over here, it is going to be helping you to perform a browser automation using playwright tool,

16
00:00:59,160 --> 00:01:00,200
which is awesome.

17
00:01:00,760 --> 00:01:04,760
And we now need a client to perform this operation.

18
00:01:04,760 --> 00:01:10,160
And the client, as I told you, it can be even a cloud desktop for that matter.

19
00:01:10,160 --> 00:01:12,800
But you can have any client.

20
00:01:12,840 --> 00:01:22,080
The client can be a Visual Studio Code, GitHub Copilot or cursor IDE or windsurf IDE, or even Gemini

21
00:01:22,080 --> 00:01:22,640
CLI.

22
00:01:23,280 --> 00:01:28,520
It can be of anything which can interact with your MCP server.

23
00:01:28,520 --> 00:01:32,240
So it can be of any client which supports the MCP server protocol.

24
00:01:32,960 --> 00:01:41,000
And now, because the cloud desktop already supports this MCP server, I am going to go copy this particular

25
00:01:41,000 --> 00:01:43,480
command and I'm going to do it.

26
00:01:43,480 --> 00:01:47,600
I know it's going to be a bit confusing at the start like hey Karthik, why do you need to configure

27
00:01:47,600 --> 00:01:48,080
this?

28
00:01:48,120 --> 00:01:54,320
Well guess what, this particular cloud desktop don't have the playwright MCP server yet.

29
00:01:54,600 --> 00:01:58,640
The only tool that it had and has is the web search tool.

30
00:01:58,640 --> 00:02:05,000
As you can see over here, which is also something we just disabled, but you can configure many different

31
00:02:05,040 --> 00:02:11,480
MCP servers over here in order to make use of these tools, and the large language model will be more

32
00:02:11,480 --> 00:02:16,360
intelligent enough to go and choose the tools if it needs those capabilities.

33
00:02:16,560 --> 00:02:18,720
That is what we are going to be seeing over here.

34
00:02:18,960 --> 00:02:23,320
So I'll quickly show you how you can configure it on this cloud desktop.

35
00:02:23,720 --> 00:02:28,720
The way you can do it is just going to go to the cloud over here, and you can see that there is something

36
00:02:28,720 --> 00:02:29,760
called as settings.

37
00:02:29,880 --> 00:02:34,200
The same things applicable for the windows version as well.

38
00:02:34,600 --> 00:02:39,600
Just go to the developers over here and see there is something called as Edit configuration where you

39
00:02:39,600 --> 00:02:41,720
can see these are the local MCP servers.

40
00:02:42,280 --> 00:02:47,400
If you click this edit config you can see we have got this cloud desktop configuration.

41
00:02:47,920 --> 00:02:49,800
This is the file that you need.

42
00:02:50,080 --> 00:02:52,640
The moment you just double click it it is going to be empty.

43
00:02:52,680 --> 00:02:58,200
If you don't really have any MCP server like me in this case, but if you have MCP servers, you will

44
00:02:58,200 --> 00:03:00,760
see a bunch of MCP servers coming in.

45
00:03:02,160 --> 00:03:08,400
And now let me just go and install this MCP server to my cloud desktop.

46
00:03:08,680 --> 00:03:14,970
And the way I can do it is I can just copy over here and paste this MCP server.

47
00:03:14,970 --> 00:03:20,730
And you will notice that this MCP server starts with MCP servers as the root.

48
00:03:20,730 --> 00:03:23,410
And then there are the name of MCP servers.

49
00:03:23,410 --> 00:03:26,090
So you can have any number of MCP server.

50
00:03:26,130 --> 00:03:28,370
At the moment I only have one MCP server.

51
00:03:28,370 --> 00:03:35,490
But you can also have MCP servers like the file system, MCP server or the Chrome dev tool, MCP server

52
00:03:35,530 --> 00:03:36,890
database, MCP server.

53
00:03:36,890 --> 00:03:43,810
You can have any MCP server for that matter, and I only have the playwright MCP server this time,

54
00:03:43,810 --> 00:03:45,770
so I'm just going to save this file.

55
00:03:46,130 --> 00:03:47,210
And guess what?

56
00:03:47,210 --> 00:03:51,570
The moment you add this MCP server it won't be listed over here.

57
00:03:51,610 --> 00:03:57,250
So it's only having my file system MCP server right now and doesn't have any MCP server.

58
00:03:58,010 --> 00:04:05,450
In order for you to see the MCP server, you got to close the cloud desktop one time and to restart

59
00:04:05,450 --> 00:04:05,690
this.

60
00:04:05,690 --> 00:04:12,570
Unfortunately, it's not real time by now, and the moment I restart the cloud desktop, you will notice

61
00:04:12,570 --> 00:04:16,530
that you will going to have an MCP server.

62
00:04:17,170 --> 00:04:17,810
Guess what?

63
00:04:17,850 --> 00:04:22,370
If you want to go to the settings this time, and if I go to the developers look at that.

64
00:04:22,370 --> 00:04:29,330
We have a playwright MCP server and it's also up and running, which means now this particular MCP server

65
00:04:29,330 --> 00:04:34,010
is configured for you to do the browser automation, which is fabulous.

66
00:04:34,290 --> 00:04:35,930
So let's see how that can be achieved.

67
00:04:36,290 --> 00:04:41,770
Well, in order to do that I'm going to go and click this new chat over here.

68
00:04:42,130 --> 00:04:48,130
And if I'm going to go to the knob this time earlier, you remember we only had the web search feature.

69
00:04:48,130 --> 00:04:51,570
But now we also has got a playwright feature.

70
00:04:51,970 --> 00:04:56,690
This is a tool and an AI agent that we have got, which is amazing.

71
00:04:56,930 --> 00:05:02,370
And the moment I go and click this arrow there, you will see a bunch of tools which are created by

72
00:05:02,370 --> 00:05:06,370
this playwright tool or playwright MCP server.

73
00:05:06,570 --> 00:05:08,130
It has got so many different tools.

74
00:05:08,170 --> 00:05:08,850
Look at that.

75
00:05:09,250 --> 00:05:10,650
See how many tools it has got.

76
00:05:10,650 --> 00:05:12,890
Closing the browser, resizing the browser window.

77
00:05:13,130 --> 00:05:14,610
Get the console message.

78
00:05:14,610 --> 00:05:15,730
Handle dialogues.

79
00:05:15,970 --> 00:05:18,450
Upload a file form filling.

80
00:05:18,490 --> 00:05:20,290
Install the browser specification.

81
00:05:20,290 --> 00:05:23,010
Oh my God, this is quite amazing.

82
00:05:23,210 --> 00:05:29,770
All the options that you can think of for doing test automation as well as the browser automation.

83
00:05:29,770 --> 00:05:32,610
You can do everything using this playwright MCP server.

84
00:05:32,890 --> 00:05:34,810
And now let me go and do this.

85
00:05:35,210 --> 00:05:43,170
Can you navigate to this particular website that we were just trying to do the login operation.

86
00:05:43,810 --> 00:05:56,490
So I'm going to do over here and perform login and also try creating user from the employee list page.

87
00:05:56,610 --> 00:06:01,650
So I'm also saying that once you log in, you can go to the employee list page and try to create me

88
00:06:01,650 --> 00:06:02,770
an employee there.

89
00:06:03,050 --> 00:06:09,690
So I'm just going to give all this information and I'm going to do a uh enter there.

90
00:06:10,050 --> 00:06:15,250
And you can also ask it to generate the code if you wanted to, which I'm going to reserve it for our

91
00:06:15,290 --> 00:06:20,370
WIP coding session, but I'm just going to hit re-enter this time and we'll see how that works.

92
00:06:20,370 --> 00:06:25,970
And because we have enabled the playwright MCP server, you will notice that it's going to invoke the

93
00:06:25,970 --> 00:06:28,730
playwright MCP server for me automatically.

94
00:06:29,450 --> 00:06:30,410
This is magic.

95
00:06:30,730 --> 00:06:33,490
This is all happening because of our cloud LLM.

96
00:06:33,730 --> 00:06:34,730
And now look at that.

97
00:06:34,730 --> 00:06:37,090
It has opened the browser for me there.

98
00:06:37,570 --> 00:06:39,970
And it's going to do a login operation.

99
00:06:39,970 --> 00:06:45,370
And I'm just going to keep these things side by side because it is going to do a lot of question and

100
00:06:45,370 --> 00:06:48,730
answering with me during this interactive session.

101
00:06:49,290 --> 00:06:51,290
I'm just going to put this guy over here.

102
00:06:51,690 --> 00:06:52,250
Look at that.

103
00:06:52,290 --> 00:06:54,050
It says that it has taken a screenshot.

104
00:06:54,050 --> 00:06:55,850
I'm just going to say always hello.

105
00:06:56,210 --> 00:07:02,130
Let him take the screenshot because it needs to take a screenshot and save it for the for the reason

106
00:07:02,130 --> 00:07:06,170
why it needs it, which is especially to understand how the page is up.

107
00:07:06,410 --> 00:07:08,850
And now you can see that it has gone through here.

108
00:07:08,890 --> 00:07:13,930
It says that I can see the login page is loaded, but you need to pass the username and password to

109
00:07:13,970 --> 00:07:16,530
me, which I forgot actually, which is correct.

110
00:07:16,530 --> 00:07:22,090
So I'm going to say username is admin and password is password.

111
00:07:23,010 --> 00:07:24,140
And I'm going to hit enter.

112
00:07:24,540 --> 00:07:30,860
And now what's going to happen is the cloud desktop is going to start filling up the username for me.

113
00:07:30,860 --> 00:07:31,940
So let's see what's going to happen.

114
00:07:31,940 --> 00:07:32,540
Look at that.

115
00:07:32,540 --> 00:07:33,340
So immediate.

116
00:07:33,340 --> 00:07:40,300
It just filled it up uh there uh and now it's gonna perform the login operation by clicking the button

117
00:07:40,300 --> 00:07:40,540
there.

118
00:07:40,540 --> 00:07:42,420
So I'm gonna say always allow.

119
00:07:43,500 --> 00:07:44,020
Look at that.

120
00:07:44,020 --> 00:07:52,860
It has performed a login and now it is gonna perform the employee list operation, which is great.

121
00:07:53,340 --> 00:07:56,460
Uh, and also it's going to go and create an employee.

122
00:07:56,460 --> 00:07:57,620
So let's see how it's going to do.

123
00:07:57,660 --> 00:08:00,580
It's going to click the Create New link on the top.

124
00:08:00,780 --> 00:08:08,140
Because I didn't even told the MCP server, uh, in my prompt to go and click the create new button

125
00:08:08,140 --> 00:08:09,500
to perform this operation.

126
00:08:09,500 --> 00:08:10,460
But look at that.

127
00:08:10,460 --> 00:08:17,020
It has already clicked it, and now it's gonna create a new employee with some realistic information

128
00:08:17,020 --> 00:08:17,740
for me there.

129
00:08:18,580 --> 00:08:19,260
Look at that.

130
00:08:20,260 --> 00:08:23,020
So it's filling a sample data for me this time.

131
00:08:23,580 --> 00:08:28,700
See Sarah Johnson just filled up all the information, and it missed.

132
00:08:28,700 --> 00:08:29,620
The duration worked.

133
00:08:29,620 --> 00:08:32,460
So now it is going to do fill the duration worked as well.

134
00:08:32,460 --> 00:08:33,380
If I'm not wrong.

135
00:08:34,140 --> 00:08:34,820
Look at that.

136
00:08:35,140 --> 00:08:36,900
And now it's creating the employee.

137
00:08:37,420 --> 00:08:44,420
These are all happening because we have got the power of the MCP server and the AI agent to perform

138
00:08:44,420 --> 00:08:45,460
these operation.

139
00:08:45,620 --> 00:08:46,660
So this is pretty cool.

140
00:08:46,660 --> 00:08:52,460
So now that you know that how the AI agents is going to work, and these are all happening because now

141
00:08:52,460 --> 00:08:59,700
the large language model is getting all the context which is needed for performing the operation using

142
00:08:59,700 --> 00:09:04,380
the tools that we have got, as well as the AI agents that we have got.

143
00:09:04,860 --> 00:09:08,740
And now we have got a new employee added over here.

144
00:09:09,180 --> 00:09:16,260
This is how we can see how the AI agents works, and how the large language model is getting the context

145
00:09:16,300 --> 00:09:18,140
to perform all these operations.

146
00:09:18,500 --> 00:09:21,620
So this is the MCP server for you.

147
00:09:22,060 --> 00:09:28,380
And with all these knowledge that we have, we are going to see how we can start doing the WIP coding

148
00:09:28,420 --> 00:09:31,460
using GitHub Copilot in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 8. Vibe Code  Creating Manual Test Scenarios Plan using Playwright MCP Server

1
00:00:00,120 --> 00:00:04,240
In this lecture, we're going to talk about how we can start doing a vibe coding.

2
00:00:04,240 --> 00:00:09,920
And if you really not heard about the term vibe coding, you can just head over to Google over here

3
00:00:09,920 --> 00:00:11,920
and search for vibe coding.

4
00:00:11,920 --> 00:00:14,680
So I'm going to just go and search in Google over here.

5
00:00:14,920 --> 00:00:17,960
And I'm going to say, what is vibe coding?

6
00:00:18,720 --> 00:00:23,920
And I'm going to ask in the AI mode this time and let's see what AI mode returns.

7
00:00:23,920 --> 00:00:29,400
So Vibe Coding is an AI assisted software development workflow where a user guides a large language

8
00:00:29,400 --> 00:00:35,160
model to generate, refine and debug code and application through natural language prompts.

9
00:00:35,400 --> 00:00:41,800
That is what is vibe coding, which is amazing because now all we can do is we don't really have to

10
00:00:41,800 --> 00:00:42,560
write a code.

11
00:00:42,600 --> 00:00:49,960
Rather, the large language model will help us do the coding and also refining the code and also debugging

12
00:00:49,960 --> 00:00:52,960
the code through just the natural language prompt.

13
00:00:52,960 --> 00:00:56,080
But you may wonder, Karthik, then why do we need this course?

14
00:00:56,080 --> 00:00:59,440
Because we don't even need to self-heal our locators.

15
00:00:59,440 --> 00:01:04,230
We don't even need to understand how to test our application because it's all going to be done by the

16
00:01:04,230 --> 00:01:04,590
AI.

17
00:01:04,830 --> 00:01:05,430
But guess what?

18
00:01:05,470 --> 00:01:10,990
Just reserve your thoughts on that, because we are going to see how the opposite is going to happen

19
00:01:10,990 --> 00:01:17,910
in this course, because you need to know what exactly is the code being generated by these AI applications,

20
00:01:18,310 --> 00:01:24,590
as well as how you need to be in control while you are going to be working with a larger project, because

21
00:01:24,590 --> 00:01:31,350
you are not really building an test for a startup application, or maybe a single page application,

22
00:01:31,350 --> 00:01:37,390
you will be building test automation code for a enterprise grade application, and during that time,

23
00:01:37,390 --> 00:01:43,870
it is important that you have all the knowledge as well as how you test your application itself.

24
00:01:43,870 --> 00:01:47,190
And that is exactly what we are going to be doing in this course.

25
00:01:47,510 --> 00:01:54,870
And we will see how we can able to make sure that we are not just going to rely fully on the generated

26
00:01:54,870 --> 00:02:00,790
code, rather how we can optimize the code which is generated by the AI and also use the assistance

27
00:02:00,790 --> 00:02:05,260
of AI while writing the test automation code, because that is how things are going to happen.

28
00:02:05,260 --> 00:02:11,460
And you're not just going to depend on the code which is generated by the GitHub copilot or cursor or

29
00:02:11,580 --> 00:02:13,100
cloud desktop for that matter.

30
00:02:13,140 --> 00:02:19,180
We are going to use the power of large language model to perform all of these operations ourself while

31
00:02:19,180 --> 00:02:20,380
we write the test code.

32
00:02:20,660 --> 00:02:24,060
So we'll see how we can able to start writing a simple web code.

33
00:02:24,060 --> 00:02:29,580
In our next section, we'll understand how we can start using the power of large language model to do

34
00:02:29,620 --> 00:02:35,260
even further optimization and better coding with our existing test automation code.

35
00:02:35,260 --> 00:02:42,300
Well, as I said, I'm going to go to my terminal over here and I'm going to just open the Visual Studio

36
00:02:42,300 --> 00:02:45,300
Code, and I'm going to start doing a WIP coding this time.

37
00:02:45,580 --> 00:02:46,420
Well guess what?

38
00:02:46,460 --> 00:02:49,900
I am using the GitHub copilot within my Visual Studio code.

39
00:02:49,900 --> 00:02:54,660
So if you don't really have Visual Studio Code with GitHub Copilot, I would highly recommend you to

40
00:02:54,700 --> 00:03:00,980
go ahead and use the copilot, which you can actually install from the extensions over here.

41
00:03:00,980 --> 00:03:02,940
So just go and search for Copilot.

42
00:03:03,420 --> 00:03:08,360
In Visual Studio Code Extensions, you will see that there is something called as copilot, uh, of

43
00:03:08,400 --> 00:03:11,000
the GitHub and also the GitHub copilot chat.

44
00:03:11,000 --> 00:03:15,720
So make sure that you install these two extensions as I have already did that over here.

45
00:03:15,920 --> 00:03:20,320
And once you install it, you can sign up with your GitHub account.

46
00:03:20,520 --> 00:03:24,440
If you don't really have one, I highly recommend you go and create that one as well.

47
00:03:24,480 --> 00:03:28,720
And once you register it, you can use the free tier of GitHub copilot.

48
00:03:28,720 --> 00:03:32,400
But over here I am using the paid version of GitHub Copilot.

49
00:03:32,400 --> 00:03:34,760
And that's the reason why I'm seeing a lot of model.

50
00:03:34,920 --> 00:03:40,440
But if you're using the free version of copilot, you'll be seeing fewer model than what I am seeing

51
00:03:40,480 --> 00:03:41,800
at the moment over here.

52
00:03:42,000 --> 00:03:47,000
Well, in this entire demonstration, I'm going to be using the class and 4.5 model because this is

53
00:03:47,000 --> 00:03:54,480
quite powerful model as of today, which is also claimed as the world's most capable and powerful large

54
00:03:54,480 --> 00:03:55,160
language models.

55
00:03:55,160 --> 00:04:00,280
I'm going to be using this particular model over here, and we'll start writing the, uh, the code

56
00:04:00,280 --> 00:04:01,080
this time.

57
00:04:01,080 --> 00:04:09,070
So for doing the vibe coding, I am actually going to use the same playwright MCP server that I was

58
00:04:09,070 --> 00:04:16,910
just using even earlier in our last lecture of this particular section, where we just went to the copilot

59
00:04:16,910 --> 00:04:18,270
and then start working with it.

60
00:04:18,270 --> 00:04:24,030
So the same thing I'm going to do over here as well, uh, so I'm just going to go and copy the same

61
00:04:24,030 --> 00:04:29,470
copilot that we have, which is this one, and we're going to configure it with the GitHub copilot and

62
00:04:29,470 --> 00:04:31,110
then start using it.

63
00:04:31,110 --> 00:04:38,870
But in order to do that configuration, all you have to do it is uh, go to your Visual Studio Code,

64
00:04:39,070 --> 00:04:44,110
hit Command shift P or Control shift P if you're using Windows Machine and you see that we have got

65
00:04:44,110 --> 00:04:46,550
something called as MCP list server.

66
00:04:46,790 --> 00:04:51,150
So if I'm going to type MCP there, you see that there is going to be list server and add server comes

67
00:04:51,150 --> 00:04:51,430
in.

68
00:04:51,670 --> 00:04:56,470
If I'm going to hit the list server, you see that I already have three MCP server which are currently

69
00:04:56,470 --> 00:05:01,390
in stopped state at the moment, but I can go ahead and install an MCP server as well.

70
00:05:01,590 --> 00:05:02,270
Like this.

71
00:05:02,470 --> 00:05:05,630
Uh, and then I can add the MCP server.

72
00:05:05,630 --> 00:05:09,070
I can also do something like browse MCP server over here.

73
00:05:09,070 --> 00:05:14,300
So I'm you want to go and click this browse MCP server, you see that there are going to be uh, like

74
00:05:14,340 --> 00:05:16,740
an extension for the MCP server comes in.

75
00:05:16,780 --> 00:05:22,260
You can go and click this enable MCP Server Marketplace, which is going to show you all the MCP servers

76
00:05:22,260 --> 00:05:24,260
which are available at the moment.

77
00:05:24,500 --> 00:05:28,260
And you will notice that there are so many MCP server today at the time of recording.

78
00:05:28,460 --> 00:05:29,820
But guess what?

79
00:05:30,060 --> 00:05:35,980
The moment you are going to be watching this particular video, maybe in another year or so you will

80
00:05:35,980 --> 00:05:39,260
see quite a lot of MCP server evolving like mushrooms.

81
00:05:39,260 --> 00:05:42,420
But I'm going to go ahead and install this MCP server over here.

82
00:05:42,420 --> 00:05:44,380
Installation is very straightforward.

83
00:05:44,420 --> 00:05:46,860
Just click this MCP two MCP server.

84
00:05:46,900 --> 00:05:47,980
Hit this install.

85
00:05:48,500 --> 00:05:49,020
Done.

86
00:05:49,180 --> 00:05:52,020
Your MCP server is already installed over here.

87
00:05:52,020 --> 00:05:57,580
You don't need to restart Visual Studio Code or as such just do command shift P or Ctrl shift P one

88
00:05:57,580 --> 00:06:03,300
more time list MCP server and you'll notice that the MCP server, the Microsoft Player MCP server is

89
00:06:03,300 --> 00:06:05,620
up and running, which is this one.

90
00:06:06,220 --> 00:06:09,660
You can click this MCP server, click this show configuration.

91
00:06:09,700 --> 00:06:15,730
It will show you the MCP server which is currently running, and it shows all of these details over

92
00:06:15,730 --> 00:06:16,290
here.

93
00:06:16,330 --> 00:06:16,810
Right.

94
00:06:16,850 --> 00:06:20,210
These are the already configured MCP servers sitting in my machine.

95
00:06:20,330 --> 00:06:23,690
Uh, I don't really need to care about that because I'm not going to use it for now.

96
00:06:23,850 --> 00:06:26,770
And this is the only MCP server which I'm going to be using.

97
00:06:26,770 --> 00:06:33,050
This is the same kind of configuration that we did for the cloud desktop as well in our last lecture.

98
00:06:33,050 --> 00:06:38,730
So what I'm going to do this time is I'm going to go, uh, and start doing a web coding.

99
00:06:38,730 --> 00:06:44,490
This time when I say vibe coding, I'm going to just use this MCP server to generate the code for me

100
00:06:44,530 --> 00:06:45,890
for my application.

101
00:06:45,890 --> 00:06:50,370
Well guess what, I'm going to go to my application, which is this one, one more time over here,

102
00:06:50,730 --> 00:06:53,890
and I'm going to give this particular link to this guy.

103
00:06:54,130 --> 00:06:57,730
And I'm going to say, can you go ahead and generate the test cases for me.

104
00:06:57,730 --> 00:06:58,170
Yeah.

105
00:06:58,370 --> 00:07:04,770
So I'm going to say can you generate test cases for me.

106
00:07:05,050 --> 00:07:11,490
Uh, I'm going to say generate the manual test cases for me because this is what we're going to be doing

107
00:07:11,610 --> 00:07:15,960
in this particular lecture, and in the next lecture we're going to use the same manual test cases,

108
00:07:16,240 --> 00:07:19,600
uh, for generating the automated test cases.

109
00:07:19,600 --> 00:07:29,280
So I'm going to just do that can generate the manual test cases for me uh, by uh by understanding the

110
00:07:29,520 --> 00:07:30,560
application.

111
00:07:30,560 --> 00:07:38,640
And I'm going to give the link over here, uh, try to, uh, write all the permutations and combinations

112
00:07:38,640 --> 00:07:47,720
of test cases, including positive and negative scenarios, create and test case.md file with all of

113
00:07:47,720 --> 00:07:54,440
these information, which can be used for me to generate automated test cases later on, make sure you

114
00:07:54,440 --> 00:07:59,960
include all the information which can be used by the AI agent to perform these operations.

115
00:08:01,920 --> 00:08:07,400
So you can see that I have given enough information this time, so hopefully AI agent can generate things

116
00:08:07,400 --> 00:08:07,680
for me.

117
00:08:07,680 --> 00:08:10,360
And you see that I'm currently in the agent mode this time.

118
00:08:10,360 --> 00:08:17,470
So that's the reason why you need to know what agent is even Claude Bard, as well as in Kurzer and

119
00:08:17,470 --> 00:08:19,430
in GitHub Copilot.

120
00:08:19,430 --> 00:08:24,630
As you can see over here, we all have the agent mode, which is going to do the a genetic operation,

121
00:08:24,830 --> 00:08:26,030
which is amazing.

122
00:08:26,030 --> 00:08:30,030
So having knowledge of AI agents is super an utmost important.

123
00:08:30,030 --> 00:08:32,630
That's the reason why we had the lecture earlier.

124
00:08:32,990 --> 00:08:37,950
Well, I am going to give all this information and you see that there is this gear symbol like the tool

125
00:08:37,950 --> 00:08:44,110
gear symbol, which is especially to tell you what are the tools which are being used by this particular

126
00:08:44,390 --> 00:08:46,150
agent, where it generates the code.

127
00:08:46,190 --> 00:08:51,550
I can go ahead and uncheck the unnecessary, uh, extensions, which I'm not even going to be using,

128
00:08:51,590 --> 00:08:54,070
which are these things because I don't even need them.

129
00:08:54,270 --> 00:08:55,950
I'm going to remove all of these over here.

130
00:08:55,950 --> 00:08:58,950
I'm just going to let the plate MCP server to be there for now.

131
00:08:59,350 --> 00:09:01,510
Uh, and I'm going to hit enter.

132
00:09:01,750 --> 00:09:09,150
And the moment I run this, you will notice that, uh, the, uh, class 3.4.5 model is going to invoke

133
00:09:09,150 --> 00:09:14,990
the playwright MCP server this time, and it is going to run the browser, as you can see over here

134
00:09:15,230 --> 00:09:21,660
and now the MCP server is going to go and figure out what are the different kinds of tests that it can

135
00:09:21,660 --> 00:09:22,140
write.

136
00:09:22,180 --> 00:09:29,340
I'm going to allow in workspace, which means it is going to not ask me the same operation or same question

137
00:09:29,340 --> 00:09:32,620
for me every single time, what it's going to do, any of the operation.

138
00:09:32,620 --> 00:09:35,420
So I'm just going to let that to happen.

139
00:09:35,420 --> 00:09:36,060
And you see that.

140
00:09:36,060 --> 00:09:42,700
Now the playwright MCP server is trying to figure out what are the different kinds of tests that it

141
00:09:42,700 --> 00:09:43,180
can write.

142
00:09:43,180 --> 00:09:47,820
So it is just navigating to the application as if like a, like a user.

143
00:09:48,180 --> 00:09:52,780
And it is doing all sort of, uh, monkey testing, kind of navigation this time.

144
00:09:52,820 --> 00:09:57,540
See, what are the things it is doing is navigating to the login page, creating a new account page,

145
00:09:57,660 --> 00:10:01,500
and also going to the employee list page.

146
00:10:01,860 --> 00:10:07,180
And also it figured out that it could able to, uh, perform a search operation as well.

147
00:10:07,220 --> 00:10:08,980
See that it's searching for Karthik there.

148
00:10:09,180 --> 00:10:14,740
Uh, and then it is going to, uh, get the information like how the search functionality is working.

149
00:10:14,740 --> 00:10:21,040
So it is just doing all the brainstorming this time, uh, to see how it can generate a better test

150
00:10:21,040 --> 00:10:27,280
code, and for that, it also need to create a requirement because that is what we have told it to do

151
00:10:27,320 --> 00:10:27,760
there.

152
00:10:27,920 --> 00:10:31,600
So it's gonna understand the entire application this time.

153
00:10:31,600 --> 00:10:36,920
And now it's creating a comprehensive test case document based on the analysis of the application that

154
00:10:36,920 --> 00:10:38,440
it has just did over here.

155
00:10:38,480 --> 00:10:43,400
See how many analysis it has did by navigating to the entire application.

156
00:10:43,840 --> 00:10:45,280
And it is doing that.

157
00:10:45,280 --> 00:10:49,640
So let's just wait for the comprehensive test case document to be created.

158
00:10:49,640 --> 00:10:50,200
All right.

159
00:10:50,200 --> 00:10:55,640
As you can see, now that the test case has been generated by this particular cloud desktop.

160
00:10:55,640 --> 00:11:01,160
And as you can see that the test case has got the home page test case which is going to say verify the

161
00:11:01,160 --> 00:11:02,240
home page loaded.

162
00:11:02,240 --> 00:11:05,200
And it is going to say the details of the home page which has been loaded.

163
00:11:05,600 --> 00:11:12,400
Verify the navigation menu, verify the link about link, verify the employee list link.

164
00:11:12,400 --> 00:11:15,960
And then user registration operation is going to give that information there.

165
00:11:16,080 --> 00:11:20,270
And then the successful user registration registration with empty fields.

166
00:11:20,270 --> 00:11:23,870
Registered with invalid email, registered with mismatched password.

167
00:11:23,910 --> 00:11:29,990
So you see that so many test cases are now being written just with one single prompt that we just gave.

168
00:11:29,990 --> 00:11:34,790
Like this can generate a manual test case for me to understand the application, uh, by understanding

169
00:11:34,790 --> 00:11:35,430
the application.

170
00:11:35,470 --> 00:11:37,270
So this is the same prompt that we gave.

171
00:11:37,270 --> 00:11:42,790
And we also gave the, the the application detail, which is this particular URL.

172
00:11:42,790 --> 00:11:49,870
And because we have given or enabled the large language model with the playwright MCP server, it gets

173
00:11:49,910 --> 00:11:52,350
all the contexts immediately.

174
00:11:52,350 --> 00:11:55,270
That is the reason why it could able to get all the information there.

175
00:11:55,390 --> 00:12:01,670
So hope you got the idea of how we can do the WIP coding, uh, with this particular, uh, playwright

176
00:12:01,710 --> 00:12:03,950
MCP server as well as with GitHub copilot.

177
00:12:03,990 --> 00:12:09,470
I know we have not done any coding yet as it is a WIP manual test probably, but we are going to see

178
00:12:09,470 --> 00:12:17,430
how we can use this idea to extend it to write the automated test cases, by giving this test case as

179
00:12:17,430 --> 00:12:22,430
the context while writing the test cases, which we'll be doing in our next lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 9. Vibe Code Creating Automated Test Scenarios using Test Plan

1
00:00:00,080 --> 00:00:00,640
All right.

2
00:00:00,640 --> 00:00:05,520
So now that because we have the test cases being generated by our, uh.

3
00:00:05,640 --> 00:00:12,280
Class 4.5 model, as well as the playwright MCP server agent, we are going to see how we can use this

4
00:00:12,280 --> 00:00:19,160
test case as a context for our test case generation, and how you will be mind blown to see how that

5
00:00:19,160 --> 00:00:25,480
a single context, which is the test case MD file, can generate so much of test case for you, even

6
00:00:25,480 --> 00:00:28,320
like a framework level code if you wanted to.

7
00:00:28,360 --> 00:00:34,360
So you can do every single thing using this particular, uh, test case MD file.

8
00:00:34,360 --> 00:00:42,960
So I'm going to say, can you write a automated test framework code using I'm going to just probably

9
00:00:42,960 --> 00:00:47,600
say uh, selenium with C sharp dotnet.

10
00:00:47,600 --> 00:00:51,320
So I'm basically going to do using selenium this time not with playwright.

11
00:00:51,320 --> 00:00:52,880
So I'm just going to use selenium.

12
00:00:53,040 --> 00:01:00,400
And I'm going to say uh, understand the test case MD file that I have attached for the context.

13
00:01:00,560 --> 00:01:07,020
And then try to generate the test cases with the Page Object model code, as well as better reusable

14
00:01:07,020 --> 00:01:12,660
code with configurations to hold the website information.

15
00:01:12,780 --> 00:01:18,780
And if you are using any of the weighting mechanism, then also try to use that along with it so that

16
00:01:18,780 --> 00:01:24,180
I can do a configurable weighting as well as configurable website over there.

17
00:01:24,460 --> 00:01:27,860
You see that now I have given so much of information this time.

18
00:01:28,100 --> 00:01:28,580
Oops, sorry.

19
00:01:28,620 --> 00:01:30,180
Even this is also being typed.

20
00:01:30,340 --> 00:01:31,980
Uh, now I'm going to.

21
00:01:32,100 --> 00:01:37,060
You see that now I've attached this test case empty as the context over here, because this whole empty

22
00:01:37,060 --> 00:01:41,820
file can be now used, and because it is nothing to do with the playwright itself, because it's just

23
00:01:41,820 --> 00:01:43,060
a manual test case.

24
00:01:43,060 --> 00:01:47,180
Now, this can act as a context for doing the WIP coding.

25
00:01:47,380 --> 00:01:54,060
And now the moment I'm going to send this information to the sonnet 4.5 model.

26
00:01:54,100 --> 00:02:00,260
Now you see that we are going to see the entire test case being generated like a framework level code,

27
00:02:00,260 --> 00:02:05,810
and see that it has created, uh, a five to dos for us over here.

28
00:02:05,810 --> 00:02:08,250
And I'm just going to expand this five to dos.

29
00:02:08,610 --> 00:02:13,250
You'll also notice that it's going to have like a create project structure and configuration file.

30
00:02:13,290 --> 00:02:15,730
Create a base class and utilities file.

31
00:02:15,730 --> 00:02:18,090
Implement a page object model class.

32
00:02:18,090 --> 00:02:22,970
Create the test cases sorry test classes and add a helper utilities and extension.

33
00:02:22,970 --> 00:02:26,370
So it's going to do all of these operations for me over here.

34
00:02:26,690 --> 00:02:31,810
And you will notice that with just one single prompt we're going to get all of these operations.

35
00:02:31,810 --> 00:02:35,730
So I'll just wait for this entire operation to happen and I'll be back.

36
00:02:40,410 --> 00:02:41,090
There you go.

37
00:02:41,130 --> 00:02:43,810
You can see that it is already working for us.

38
00:02:43,810 --> 00:02:48,370
But in the meantime, I've already seen that so much of code is being generated.

39
00:02:48,370 --> 00:02:54,490
You can see that all the to dos has been completed over here, and you can see that it has started all

40
00:02:54,490 --> 00:02:56,690
the way with a configuration file.

41
00:02:56,690 --> 00:02:59,370
And also there is a folder for the core.

42
00:02:59,770 --> 00:03:02,850
There are pages, tests, utilities and whatnot.

43
00:03:03,050 --> 00:03:07,130
And if you just go and expand this configuration there is a test configuration over here.

44
00:03:07,230 --> 00:03:11,350
So basically it's going to be reading from the configuration file.

45
00:03:11,350 --> 00:03:12,950
I'm going to go and accept this.

46
00:03:12,990 --> 00:03:18,430
And you can notice that there are 24 files being added this time like 26 files to be honest.

47
00:03:18,430 --> 00:03:20,870
And all of these have been done in a couple of minutes now.

48
00:03:20,870 --> 00:03:25,390
So you have see that it has got all of the informations over here which is generated.

49
00:03:25,630 --> 00:03:32,270
Uh, and also you see that there is a core which is a base page which has got all the page information

50
00:03:32,270 --> 00:03:32,990
over here.

51
00:03:33,190 --> 00:03:38,350
There are also waiting mechanism like wait for element, wait for element to be clicked, wait for element

52
00:03:38,350 --> 00:03:39,230
to disappear.

53
00:03:39,390 --> 00:03:43,550
Wait for page load is element present is element displayed.

54
00:03:43,910 --> 00:03:45,030
Look at that.

55
00:03:45,070 --> 00:03:46,030
That is amazing.

56
00:03:46,030 --> 00:03:48,190
It's already a lot of details in the base page.

57
00:03:48,430 --> 00:03:55,030
And then there is a test base as well which has got the information over there, which is going to be

58
00:03:55,030 --> 00:03:58,030
for the uh, playwright setup.

59
00:03:58,030 --> 00:04:05,270
And then the playwright tier down selenium setup and these selenium tier down for us over here.

60
00:04:05,470 --> 00:04:07,670
Uh, and then there is a navigate to URL.

61
00:04:08,190 --> 00:04:10,330
And then there is a WebDriver factory.

62
00:04:10,330 --> 00:04:15,250
So it has also written like a factory class, which can be used for performing all the operations for

63
00:04:15,250 --> 00:04:16,290
different browsers.

64
00:04:16,530 --> 00:04:22,930
And you see that the page object model code is also being written for the employee create page, and

65
00:04:22,930 --> 00:04:26,250
it has inherited the base page over here, which is amazing.

66
00:04:26,610 --> 00:04:28,690
And now it is doing all of these operations.

67
00:04:28,730 --> 00:04:29,330
Look at that.

68
00:04:29,370 --> 00:04:35,210
How much of code it has generated in like a couple of minutes, to be honest, that's mind blowing.

69
00:04:36,170 --> 00:04:37,210
Do you see that?

70
00:04:37,250 --> 00:04:43,530
It is already writing all the test cases for me, like all the framework level code, which I used to

71
00:04:43,570 --> 00:04:46,810
teach people in my selenium is dotnet course earlier.

72
00:04:47,050 --> 00:04:52,690
Uh, if you just go to this particular course, you see that the selenium with absolute beginner as

73
00:04:52,690 --> 00:04:56,370
well the selenium with framework development with dotnet.

74
00:04:56,370 --> 00:05:00,530
This particular course I used to cover all of these information in this particular course.

75
00:05:00,730 --> 00:05:07,890
Uh, and it takes almost like hours uh, before they can learn these concepts over here.

76
00:05:08,090 --> 00:05:11,520
Now it's all available, uh, in like couple of minutes.

77
00:05:11,520 --> 00:05:17,920
So you have a full blown functional framework, which has also got the entire tests for every single

78
00:05:17,960 --> 00:05:20,000
operation, just like matter of Second.

79
00:05:20,040 --> 00:05:27,680
It also has got like screenshot utilities like test generator utilities as well, like random data generation.

80
00:05:27,680 --> 00:05:29,520
And then there is a web driver extensions.

81
00:05:29,520 --> 00:05:31,560
There is an extension methods as well.

82
00:05:32,160 --> 00:05:37,840
Do you notice that how much of informations are sitting over here in just like a matter of second.

83
00:05:37,920 --> 00:05:39,560
That is the power of context guys.

84
00:05:39,560 --> 00:05:45,920
Like with just a context of a manual test case context that you gave it could able to generate so many

85
00:05:45,920 --> 00:05:51,400
information without again needing to open the browser and get the information because it already knows

86
00:05:51,760 --> 00:05:53,560
what are those controls and things.

87
00:05:53,560 --> 00:05:59,800
So it gets all the informations for you to to perform all these operations, which is pretty cool and

88
00:05:59,800 --> 00:06:00,440
pretty neat.

89
00:06:00,680 --> 00:06:08,360
So this is how we can see that we could able to do a web coding of all the test cases, which can be

90
00:06:08,360 --> 00:06:11,840
written using the GitHub copilot itself.

91
00:06:11,840 --> 00:06:14,240
And that's the power of the context.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 10. Vibe Code Creating BDD Test Scenarios using the Automated Test Context

1
00:00:00,120 --> 00:00:01,080
The last operation.

2
00:00:01,080 --> 00:00:08,440
Probably we have to do for the vibe coding to end completely is to see how we can add an BDD test cases.

3
00:00:08,440 --> 00:00:16,200
So at the moment we have generated the test cases, uh, with the test and uh, with the end unit framework,

4
00:00:16,200 --> 00:00:17,800
as you can see over here.

5
00:00:17,800 --> 00:00:21,640
But what if I want to do the same operation with BDD framework.

6
00:00:21,640 --> 00:00:26,840
So all I can do in here is I need to give the context for the test.

7
00:00:26,840 --> 00:00:29,040
So I'm going to go and select the folders.

8
00:00:29,040 --> 00:00:31,400
And I'm going to choose the tests over here.

9
00:00:31,400 --> 00:00:44,680
And I'm going to say can you read all the tests and the requirement from test case.md file and generate

10
00:00:44,720 --> 00:00:48,280
the BDD format test cases.

11
00:00:48,920 --> 00:00:54,840
And the moment I'm going to do this, what's going to happen is now the cloud solid has got all the

12
00:00:54,840 --> 00:01:01,040
context for the uh, the test case.md file because it's going to read that over here.

13
00:01:01,040 --> 00:01:07,320
And also it has got the context of the employee app dot tests folder, which is going to have all the

14
00:01:07,320 --> 00:01:08,360
tests as well.

15
00:01:08,600 --> 00:01:15,200
Now it is going to start generating the BDD, uh, like spec flow driven tests for us over here.

16
00:01:15,200 --> 00:01:18,720
So it's going to go and update, uh, the package for me.

17
00:01:18,760 --> 00:01:20,760
And now it's generating the test as well.

18
00:01:20,760 --> 00:01:26,640
So this is also one more thing that you can see that using the WIP coding, we can not only just add

19
00:01:26,800 --> 00:01:33,880
the tests, uh, like a framework, we can also do a BDD based test executions and generation by giving

20
00:01:33,880 --> 00:01:40,120
the enough contexts now for the large language model and through the AI agent.

21
00:01:40,120 --> 00:01:45,880
So you will now notice that the power of the context engineering already, because the more and more

22
00:01:45,920 --> 00:01:51,480
information that you give to the large language model, the more and more mature you can start building

23
00:01:51,480 --> 00:01:57,320
your test framework and how you can start testing your application in even more faster way.

24
00:01:57,640 --> 00:02:01,080
That is what is the real essence of this section itself.

25
00:02:01,080 --> 00:02:06,970
Because now you see that with all of these information in place, we can do quite a lot of different

26
00:02:06,970 --> 00:02:08,050
things over here.

27
00:02:08,170 --> 00:02:14,770
Well, as I said, once you have started building or start doing the web coding, you now know, like

28
00:02:14,810 --> 00:02:24,130
how amazing you can start use these operations to perform your automation test code with just few natural

29
00:02:24,130 --> 00:02:28,970
language prompts, and everything is going to be just coming up for you over here.

30
00:02:28,970 --> 00:02:35,250
And you'll also notice that now it is starting to add the feature files for, uh, the home page registration

31
00:02:35,250 --> 00:02:37,090
page, and the login page.

32
00:02:37,090 --> 00:02:38,370
Let me just go and see that.

33
00:02:38,370 --> 00:02:38,810
Look at that.

34
00:02:38,850 --> 00:02:43,330
How many test cases it's generating with the entire table structures and things.

35
00:02:43,370 --> 00:02:46,570
It's also adding a tag for me, which is quite kind of neat.

36
00:02:46,770 --> 00:02:50,530
And you see that how much things it is testing doing security testing as well.

37
00:02:50,690 --> 00:02:55,490
Um, user login testing, user registration testings and stuff, which is quite amazing.

38
00:02:55,490 --> 00:02:58,050
It's also going to generate the step definition at the same time.

39
00:02:58,050 --> 00:03:03,370
Well, now that you have understood the entire detail about the power of the context engineering and

40
00:03:03,370 --> 00:03:09,850
how the prompt engineering is all going to make your coding or the test automation.

41
00:03:09,850 --> 00:03:10,970
More amazing.

42
00:03:11,210 --> 00:03:19,930
Starting our next sections of this course, we are going to understand how we can use these ideas to

43
00:03:19,970 --> 00:03:24,250
build our own intelligent test automation code.

44
00:03:24,250 --> 00:03:31,690
With the power of large language models and using the power of local large language model to perform

45
00:03:31,690 --> 00:03:32,890
this operation.

46
00:03:32,890 --> 00:03:39,450
Because all these time we have been using the power of the large language model which is running on

47
00:03:39,490 --> 00:03:45,450
the cloud, which is nothing but the cloud 4.5 model or 3.7 model or any of these models.

48
00:03:45,570 --> 00:03:54,850
But we have never seen how we can make our test automation code more and more secure, running all grounded

49
00:03:54,850 --> 00:04:01,490
within our local machine, and also make use of the AI along with our existing test code.

50
00:04:01,530 --> 00:04:06,810
Instead of writing every single test fully driven by the AI itself.

51
00:04:06,810 --> 00:04:10,530
That is what is the whole idea which we are going to be starting to discuss.

52
00:04:10,530 --> 00:04:12,970
Starting our next section of the course.


==================================================================================


section 4. Understanding the Current Automation Test Problem and Solution with AI and LLMs

video 1. Introduction

1
00:00:00,160 --> 00:00:02,160
Welcome to the next section of our course.

2
00:00:02,160 --> 00:00:08,480
And in this section we are going to talk about why AI first versus AI assisted testing.

3
00:00:09,000 --> 00:00:15,720
If you remember, until our last section, we were talking about the AI first testing, meaning we tried

4
00:00:15,720 --> 00:00:22,160
writing a test code using the cloud desktop, and then we did a wipe coding using Visual Studio code

5
00:00:22,280 --> 00:00:25,120
for generating the test cases manually.

6
00:00:25,120 --> 00:00:31,920
And also we use the same MD file or the markdown file for generating the automated test cases.

7
00:00:31,920 --> 00:00:35,560
And we also saw how we can of course add BDD test on that.

8
00:00:35,560 --> 00:00:37,520
So we saw how everything was working.

9
00:00:37,640 --> 00:00:42,800
That approach that we discussed in the last section is called as the AI first testing, because we used

10
00:00:42,800 --> 00:00:48,760
everything using the artificial intelligence, using the AI agents and the toolings like playwright

11
00:00:48,800 --> 00:00:50,040
MCP servers and stuff.

12
00:00:50,040 --> 00:00:52,880
That's how it was all just working for us over there.

13
00:00:52,880 --> 00:01:00,000
But using this approach, we know that there are so many advantages, but there are also a list of disadvantages

14
00:01:00,070 --> 00:01:07,070
using the wipe coding approach, which almost every single company and every single person on the planet

15
00:01:07,110 --> 00:01:07,950
appreciate.

16
00:01:07,950 --> 00:01:14,470
But we also need to see the downside of using that particular approach, especially if you're going

17
00:01:14,470 --> 00:01:20,230
to see if you're going to use this approach within your organization, you will have to think about

18
00:01:20,270 --> 00:01:28,630
these problems as you know that using the AI first approach, you are always on, meaning you always

19
00:01:28,630 --> 00:01:33,710
need to rely on an automation test to generate the code for you.

20
00:01:33,910 --> 00:01:40,070
And of course, you can generate code for one time and then start customizing your test from there.

21
00:01:40,070 --> 00:01:45,630
But what happens if the code, which is generated using the artificial intelligence or the large language

22
00:01:45,630 --> 00:01:50,910
model is way too much, and if you want to customize it, it is going to take a long time.

23
00:01:51,030 --> 00:01:57,870
If you know the recent report from community, it said that the code generated from the AI takes the

24
00:01:57,870 --> 00:02:03,780
less time, but maintaining them is going to take a long time, which is another problem that we have.

25
00:02:03,820 --> 00:02:07,900
And that is going to be same thing applicable for the automation test cases as well.

26
00:02:08,100 --> 00:02:15,380
So not always on is going to be making you always 100% efficient, but you are going to end up paying

27
00:02:15,380 --> 00:02:20,700
even more cost for the high token usage due to the always on.

28
00:02:20,700 --> 00:02:26,140
Because the moment you start talking with your large language model, you will notice that there are

29
00:02:26,140 --> 00:02:32,100
going to be a long list of usage which is going to happen within your large language model.

30
00:02:32,140 --> 00:02:37,300
For example, if you see, in my case, I was trying to generate the entire test cases until here in

31
00:02:37,300 --> 00:02:41,820
our last section, and you notice that we have got this usage over here.

32
00:02:41,820 --> 00:02:47,660
The premium request was spiked up to 42%, and it was just 20% before.

33
00:02:47,860 --> 00:02:50,820
And you see that the number of usage has just increased over there.

34
00:02:50,900 --> 00:02:55,140
You may now defend saying, Karthik, if I don't want to use my premium request, I can probably use

35
00:02:55,180 --> 00:03:01,090
like the other model which are not the premium models, then you will still end up paying a lot of money,

36
00:03:01,090 --> 00:03:03,530
because you are these models that are free.

37
00:03:03,570 --> 00:03:04,850
Models that are available over.

38
00:03:04,850 --> 00:03:11,250
There may not be as efficient as what you are going to get with the cloud 4.5 model, so you are going

39
00:03:11,290 --> 00:03:15,370
to end up paying a lot of money for the premium request usage.

40
00:03:15,370 --> 00:03:18,690
That is going to be a high token usage that you're going to be doing.

41
00:03:18,690 --> 00:03:26,170
And also you are now fully dependent on the AI generated code, because now you don't have the control

42
00:03:26,170 --> 00:03:28,210
of how the codes are being generated.

43
00:03:28,210 --> 00:03:33,290
And most importantly, I've heard from students asking this question, if you're going to be relying

44
00:03:33,290 --> 00:03:40,290
on too much of AI over here, then we are starting to forget how this code is even being written, because

45
00:03:40,290 --> 00:03:46,730
even the code which we write is starting to get more obsolete, or maybe completely new or alien.

46
00:03:46,730 --> 00:03:49,770
If you're going to look at the same code after some time.

47
00:03:49,770 --> 00:03:55,690
Or maybe if you come back from holiday, we don't even recognize our own code that we have written.

48
00:03:55,690 --> 00:03:59,720
But if you're going to give all the control to the large language model and AI.

49
00:03:59,760 --> 00:04:04,640
In this case, then we don't even know what exactly these codes are being generated, because it's too

50
00:04:04,640 --> 00:04:10,040
much of code over here, and we don't even know whether these codes are boilerplate code, or even necessary

51
00:04:10,040 --> 00:04:12,040
code, or even an unnecessary code.

52
00:04:12,280 --> 00:04:14,720
So these are the problem that we have over here.

53
00:04:14,720 --> 00:04:20,200
So that's the full dependency problem that we have got over the AI first approach.

54
00:04:20,400 --> 00:04:22,120
And then of course the cost.

55
00:04:22,120 --> 00:04:25,000
Because the more and more usage of token happens.

56
00:04:25,000 --> 00:04:30,240
And always on that you are, you are going to end up more and more cost which is being spent for that.

57
00:04:30,280 --> 00:04:34,400
Well, as that said, it's all going to be the problem that you are going to end up.

58
00:04:34,400 --> 00:04:39,120
But the good thing is, if you are going to be starting this project for the first time, like an initial

59
00:04:39,120 --> 00:04:42,800
startup, like how we did in our last section, it is going to be good.

60
00:04:42,840 --> 00:04:48,680
But if you are going to start relying on the AI for long run, then you are going to end up paying these

61
00:04:48,680 --> 00:04:49,600
massive cost.

62
00:04:49,600 --> 00:04:55,760
And not every single company is also going to allow you to use the latest and greatest models, because

63
00:04:55,760 --> 00:05:01,630
the companies will have an agreement with the companies to only use certain models in this case.

64
00:05:01,630 --> 00:05:07,230
And those are the problem that we are going to have, and these are the problems with the AI first approach.

65
00:05:07,510 --> 00:05:14,790
Well, as that said, let's quickly do a cost comparison of the AI first approach versus the AI assisted

66
00:05:14,790 --> 00:05:15,350
approach.

67
00:05:15,350 --> 00:05:21,910
So you will notice over here for one test, if you're going to be doing a 50 actions, then the cost

68
00:05:21,910 --> 00:05:26,070
of let's say the model is 0.003 per call, which is highly unlikely.

69
00:05:26,630 --> 00:05:32,110
Then you are going to be paying $0.15 for one test that you're executing.

70
00:05:32,390 --> 00:05:35,070
Let's assume that you're going to be executing 1000 tests per day.

71
00:05:35,110 --> 00:05:39,310
It's not just you, but in your whole team within your company who is going to be executing it.

72
00:05:39,310 --> 00:05:45,630
So you'll be paying $150 per day for the test execution, like 1000 test, which is being executed.

73
00:05:45,870 --> 00:05:50,710
And if you think of the same in per month, it's going to be around 4500 freaking dollars.

74
00:05:51,110 --> 00:05:54,270
And it is going to work all the time, which is no doubt.

75
00:05:54,270 --> 00:05:59,460
But the problem is you are going to end up a lot of money, so you're just going to burn the whole money

76
00:05:59,460 --> 00:06:01,180
just for executing the test cases.

77
00:06:01,540 --> 00:06:07,300
In turn, the company is already paying you the salary to build these automation test, and you're also

78
00:06:07,300 --> 00:06:10,420
going to burn the money because of the AI usage.

79
00:06:10,420 --> 00:06:13,460
These are the problems that we have with the AI first approach.

80
00:06:13,460 --> 00:06:21,700
But if you see the same with the AI assisted approach, you are going to use the one healing test for

81
00:06:21,700 --> 00:06:23,420
your test, for that matter.

82
00:06:23,420 --> 00:06:27,700
And let's say your cost is 0.3003 for that.

83
00:06:27,700 --> 00:06:31,700
The same cost that I have put over here and 1000 tests you're going to be running.

84
00:06:31,700 --> 00:06:34,780
So you're going to be essentially calling 50 healing test per day.

85
00:06:35,180 --> 00:06:38,300
And then the per month cost is going to be just 4.5.

86
00:06:38,340 --> 00:06:40,740
See the amount that you have reduced over here.

87
00:06:41,020 --> 00:06:45,020
And finally it is 1000 times cheaper than compared to this car.

88
00:06:45,020 --> 00:06:49,020
So this is like a picture that I have painted over here.

89
00:06:49,020 --> 00:06:52,380
As if that the one healing test is going to happen for one single test.

90
00:06:52,380 --> 00:06:56,570
But what if there are going to be multiple healing going to happen, like multiple locators change at

91
00:06:56,570 --> 00:06:57,490
the same time.

92
00:06:57,490 --> 00:07:03,010
Then of course the cost may increase, but it is still cheaper than what you can do it with the fully

93
00:07:03,050 --> 00:07:04,690
AI dependent approach.

94
00:07:05,050 --> 00:07:12,890
That is one way you can see how the AI first versus the AI assisted approach is going to help you differentiate

95
00:07:12,890 --> 00:07:14,730
with the cost over there.

96
00:07:15,050 --> 00:07:21,290
But again, even in this case, I have actually used the AI assisted with the models which are running

97
00:07:21,290 --> 00:07:22,490
on the cloud.

98
00:07:22,490 --> 00:07:28,130
But what if you're going to be running the same approach using the local large language model, which

99
00:07:28,130 --> 00:07:32,930
are going to be running fully offline, and you don't even have to pay a single penny for that.

100
00:07:33,810 --> 00:07:40,050
So using local large language models, as we already discussed in our earlier section of this course,

101
00:07:40,490 --> 00:07:44,930
the local large language model, which is running within the olama within your local machine, will

102
00:07:44,930 --> 00:07:51,690
have zero request cost that you are going to be spending, and you can run unlimited healing tests no

103
00:07:51,690 --> 00:07:52,410
matter what.

104
00:07:52,810 --> 00:07:58,200
And you don't even need an internet dependency because it just runs without any problem.

105
00:07:58,200 --> 00:08:03,960
And you can have your model running within your own premises, and then you can work on the CI CD behind

106
00:08:03,960 --> 00:08:04,760
the firewall.

107
00:08:04,760 --> 00:08:07,040
It is not going to be of any problem as well.

108
00:08:07,040 --> 00:08:14,240
It is 100% data privacy for a company, especially on insurance, healthcare, banking, and even for

109
00:08:14,240 --> 00:08:21,080
the company which don't want to expose the details to the third party companies like OpenAI, they can

110
00:08:21,080 --> 00:08:25,280
fully use the power of local large language model within their own premises.

111
00:08:25,280 --> 00:08:27,880
So it is 100% is data privacy as well.

112
00:08:27,920 --> 00:08:34,440
It also has got lower latency if you are using no network round trip, if you are using a model which

113
00:08:34,440 --> 00:08:39,120
is very close to your own organization, which is also going to happen, and also it is a very, very

114
00:08:39,120 --> 00:08:43,720
predictable cost because it's going to be one time hardware setup that you are going to be doing.

115
00:08:43,720 --> 00:08:48,120
But the moment you do it fully run up and running, then you don't really have to spend a lot of cost.

116
00:08:48,120 --> 00:08:53,480
Maybe just a hardware upgrade is going to happen, but your local large language model is going to run

117
00:08:53,480 --> 00:08:58,160
for you all the time, and you can run unlimited healing tests for that matter.

118
00:08:58,160 --> 00:09:02,880
And you may ask, hey Karthik, this sounds very good on the paper, but how do we even run if you are

119
00:09:02,880 --> 00:09:05,080
running within our own machine?

120
00:09:05,080 --> 00:09:10,720
Because what if I want to really try out within my machine before I even propose this to my company?

121
00:09:10,720 --> 00:09:17,120
Well guess what, you can run models like GPT Oasis 20 billion parameter or three quarter 30 billion

122
00:09:17,120 --> 00:09:22,760
parameter, which works quite well for coding and working with the Dom based testing, which we are

123
00:09:22,760 --> 00:09:25,800
probably going to be doing entirely in this course.

124
00:09:25,800 --> 00:09:30,760
We're going to be using these two models while we work with the coding approach, using self-healing

125
00:09:30,760 --> 00:09:33,120
coatings and stuff in this particular course.

126
00:09:33,120 --> 00:09:41,640
And if you have a powerful GPU like 40, 90 or 50, uh, 90, uh, or 5080 for that matter, you can

127
00:09:41,640 --> 00:09:48,280
also run even more hyper parameters, uh, models within your own machine, like 70 billion parameter

128
00:09:48,280 --> 00:09:54,790
can be easily executed these days, uh, using those GPUs, and also using the devices like the Nvidia

129
00:09:54,790 --> 00:09:58,830
Spark DGX or AMD Ryzen AI Max.

130
00:09:58,830 --> 00:10:03,550
As you are seeing over here, the GM tech model and also the MacBook Pro Max.

131
00:10:03,590 --> 00:10:08,550
If you're using M1 like me or M5, which is going to be coming pretty soon.

132
00:10:08,910 --> 00:10:14,510
So you can see those models can be easily executed in these machines without any problem.

133
00:10:14,510 --> 00:10:19,030
So these are the way that you can run your local large language model on machine.

134
00:10:19,030 --> 00:10:24,070
But let's say you have purchased this course and you don't have even any of these machine at the moment.

135
00:10:24,110 --> 00:10:27,950
You may ask Karthik, you know what, we have wrongly purchased this course because we don't even have

136
00:10:27,950 --> 00:10:29,830
these hardware requirement over there.

137
00:10:30,030 --> 00:10:30,830
Guess what?

138
00:10:30,830 --> 00:10:38,550
You can still run the lower version of the models with an own machine to do that and see how that works.

139
00:10:38,550 --> 00:10:46,390
If not, there are also cloud alternative of running these language models using Lama as well as well

140
00:10:46,390 --> 00:10:52,580
as the OpenAI model to complete this course because you don't even need to purchase a costly hardware

141
00:10:52,580 --> 00:10:57,060
for that matter, because the moment you get the idea, like how things are working, it is so much

142
00:10:57,060 --> 00:11:03,020
easier for you to fuse these workflow within your testing, and then you don't even need to spend so

143
00:11:03,020 --> 00:11:08,860
much of money to purchase this course, because the idea is not to just use your local large language

144
00:11:08,860 --> 00:11:15,820
model within your company, but the idea is to use the local large language model at scale within your

145
00:11:15,820 --> 00:11:19,980
organization, especially if your company has AWS SageMaker.

146
00:11:20,020 --> 00:11:27,100
It supports latest open source model, including Meta's Llama four, Google three, Alibaba model,

147
00:11:27,140 --> 00:11:29,220
Mistral AI, and Deep Seek R model.

148
00:11:29,220 --> 00:11:34,740
So everything runs on this AWS SageMaker, so you can go and propose them that these are the way that

149
00:11:34,740 --> 00:11:36,220
you can run these models.

150
00:11:36,220 --> 00:11:38,780
If not, you can also use AWS bedrock.

151
00:11:38,780 --> 00:11:42,180
But again this provides access to the latest model though.

152
00:11:42,220 --> 00:11:47,980
But you will have limited customization, uh, because your company has to do all those customization

153
00:11:47,980 --> 00:11:49,780
with the AWS bedrock.

154
00:11:49,780 --> 00:11:57,490
But if you want to go full scale with a self-managed models within your AWS EC2 SKUs, then you can

155
00:11:57,490 --> 00:11:58,370
also do that.

156
00:11:58,370 --> 00:12:01,370
But again, this is going to be very, very costly approach.

157
00:12:01,410 --> 00:12:06,970
Even you can just go and buy an open AI models license for that to do it.

158
00:12:06,970 --> 00:12:12,010
But the problem is you will still lose the privacy and all those stuffs over there.

159
00:12:12,010 --> 00:12:18,010
But in here you have full control of the privacy and also you have full control of the cost as well.

160
00:12:18,050 --> 00:12:24,450
That's how you can use these local large language models to run on the cloud based system.

161
00:12:24,450 --> 00:12:25,210
Something like this.

162
00:12:25,210 --> 00:12:31,370
So this is what really happens if you're going to be using the local large language model at scale within

163
00:12:31,370 --> 00:12:38,770
the cloud premises, and finally using these model just to picture it out, you can give the entire

164
00:12:38,770 --> 00:12:45,330
page context, like a secure page that you have got within your organization, like banking or insurance

165
00:12:45,330 --> 00:12:50,720
or something, which is related to client sensitive information like healthcare for that matter.

166
00:12:50,720 --> 00:12:57,920
You can pass those secure page to your 100% secure local large language model, and then you can ask

167
00:12:57,920 --> 00:13:01,680
the model to go and figure out how to heal the page.

168
00:13:01,800 --> 00:13:07,560
Get the code that you need to write for while you do the inferencing, and then you can generate the

169
00:13:07,560 --> 00:13:14,000
selenium test code out from it and see everything is going to happen for you within your local machine,

170
00:13:14,000 --> 00:13:17,080
without you even sending any data to the cloud.

171
00:13:17,080 --> 00:13:21,360
And that's how things are going to happen if you're going to be using these models, which is quite

172
00:13:21,360 --> 00:13:22,040
amazing.

173
00:13:22,040 --> 00:13:29,440
Well, as that said, in this course we are going to be building a self-healing page object model selenium

174
00:13:29,440 --> 00:13:35,320
code, where you are going to be passing a full UI page along with your page object model code.

175
00:13:35,320 --> 00:13:41,720
And then you are going to ask the large language model to go and analyze the, uh, the page object

176
00:13:41,720 --> 00:13:47,960
model against the UI page that you have got and see if there is any change and if the locators are still

177
00:13:47,960 --> 00:13:52,030
matching with the page object model code that you have with a UI page.

178
00:13:52,190 --> 00:13:56,710
Then yes, it is going to run the test for you in selenium and then it's going to get passed.

179
00:13:56,870 --> 00:14:05,230
But if, let's say there is a change in the UI object and the page object model code has got an obsolete

180
00:14:05,230 --> 00:14:10,790
locator, then it is going to go and update the test code for you and rerun the test.

181
00:14:10,790 --> 00:14:12,750
And then it is going to go from there.

182
00:14:12,910 --> 00:14:15,710
You may have a question now here saying hey Karthik, you know what?

183
00:14:15,710 --> 00:14:22,190
This seems to be wrong because if you are going to be automatically healing the test code, even if

184
00:14:22,190 --> 00:14:27,110
there is a problem in the application's UI locator, how are we going to identify?

185
00:14:27,150 --> 00:14:29,830
Well, guess what, we are going to be talking about that as well.

186
00:14:29,830 --> 00:14:34,870
We're going to be addressing that issue in a way that if there is going to be any mismatch in the locator,

187
00:14:34,870 --> 00:14:40,310
it is going to tell you these are the locators which has got changed and this caused the test to fail.

188
00:14:40,470 --> 00:14:42,550
But then it went and fixed that issue.

189
00:14:42,550 --> 00:14:47,430
And now you have a report which you can get to your developer and then say that these are located which

190
00:14:47,430 --> 00:14:53,460
has been changed, but still the test has got passed because these are the places where the locator

191
00:14:53,460 --> 00:14:54,020
has changed.

192
00:14:54,020 --> 00:14:54,740
But guess what?

193
00:14:54,740 --> 00:15:00,340
In order to make all of these to happen, it's a long process to go through and I'm sure you are going

194
00:15:00,340 --> 00:15:04,900
to be coming up in the background where you have worked in automation testing before, but not really

195
00:15:04,900 --> 00:15:07,020
building a smart system like these.

196
00:15:07,020 --> 00:15:12,940
So it is going to take a long journey before we get to this particular point, and I will ensure that

197
00:15:12,940 --> 00:15:19,180
I am not going to talk faster, and I'm not going to make you bored on this whole journey, and I'm

198
00:15:19,180 --> 00:15:25,340
not going to make you uncomfortable in any sense, saying this is what is the code, just copy paste

199
00:15:25,340 --> 00:15:26,220
it and work.

200
00:15:26,220 --> 00:15:28,100
No, that's not the way we are going to deal with.

201
00:15:28,140 --> 00:15:31,980
We are going to write every single code and we'll see how we can achieve this point.

202
00:15:32,020 --> 00:15:37,420
Well, as that said, in our next lecture, we'll first talk about what are the components that we are

203
00:15:37,420 --> 00:15:40,380
going to be building in this particular course.

204
00:15:40,740 --> 00:15:45,500
And following that, we are going to do all of these operations manually, and then we are going to

205
00:15:45,540 --> 00:15:47,700
start writing the code one by one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 2. Understanding the Components to build for Self Healing Intelligent AI Test Code

1
00:00:00,040 --> 00:00:05,080
In this lecture, we can talk about the components which are needed to build the solution that we just

2
00:00:05,080 --> 00:00:06,880
talked in our last lecture.

3
00:00:07,080 --> 00:00:12,520
So essentially, in order to build this entire component, we have to break down the code in such a

4
00:00:12,520 --> 00:00:19,880
way that you can talk with your code as well as with your large language model in a more sensible manner.

5
00:00:20,000 --> 00:00:22,480
So we are going to build the code something like this.

6
00:00:22,520 --> 00:00:26,240
We are going to see how we can talk with the large language model.

7
00:00:26,360 --> 00:00:32,320
Essentially, there can be an HTTP way of talking with the large language model, because you know that

8
00:00:32,320 --> 00:00:36,080
we can access the local large language model using the API.

9
00:00:36,240 --> 00:00:42,280
We can do the exact same thing to talk with the cloud large language models as well.

10
00:00:42,280 --> 00:00:47,520
So you can talk with the local large language model with an HTTP request and cloud large language model

11
00:00:47,520 --> 00:00:49,760
using some other libraries for that matter.

12
00:00:49,800 --> 00:00:56,040
Let's say we're going to talk with the OpenAI model, so we can just use the OpenAI NuGet package for

13
00:00:56,040 --> 00:00:56,720
that matter.

14
00:00:56,720 --> 00:01:02,920
And similarly, we are going to be formatting the prompt in such a way that we get the response like

15
00:01:02,960 --> 00:01:04,280
what we are looking for.

16
00:01:04,320 --> 00:01:08,670
Remember the prompt engineering and the context engineering that we were talking earlier.

17
00:01:08,830 --> 00:01:11,270
It's all going to come up right now.

18
00:01:11,350 --> 00:01:17,550
So that's where we are going to implement all the logics and the ideas that we were talking in our last

19
00:01:17,550 --> 00:01:22,390
section, and bring it to life, and we'll see how we can format those prompts over here.

20
00:01:22,390 --> 00:01:26,870
So we need to prompt in such a way that we get the response of what we are looking for.

21
00:01:27,750 --> 00:01:34,710
And then we are going to write some logic of how we can do self-healing of the code, which we got out

22
00:01:34,710 --> 00:01:39,070
from the formatted prompts response from the large language model.

23
00:01:39,070 --> 00:01:43,670
And that's what we are going to be doing over here in this particular place.

24
00:01:43,670 --> 00:01:49,910
And finally, we are going to be updating our existing code in such a way that it gets all the self-healing

25
00:01:49,910 --> 00:01:51,270
locator updated.

26
00:01:51,270 --> 00:01:54,230
So these are things which are going to happen for us over here.

27
00:01:54,230 --> 00:01:57,470
And the entire code is going to look something like this.

28
00:01:57,470 --> 00:02:03,990
I know this diagram makes no sense right now, so I'm just going to ignore this for now because it is

29
00:02:03,990 --> 00:02:06,030
going to surely confuse you a lot.

30
00:02:06,150 --> 00:02:11,510
But as I said, let's see what are the technologies and libraries that we are going to be using in this

31
00:02:11,650 --> 00:02:12,730
entire course.

32
00:02:12,730 --> 00:02:17,090
Well we are going to be using C sharp DotNet as the programming language.

33
00:02:17,250 --> 00:02:24,610
And we are going to be building the test using the selenium with dotnet core or playwright with c dotnet

34
00:02:24,610 --> 00:02:25,010
code.

35
00:02:25,090 --> 00:02:29,930
And also we'll be using Ides like Visual Studio or Writer IDE.

36
00:02:29,970 --> 00:02:30,650
It doesn't matter.

37
00:02:30,650 --> 00:02:33,890
You can use any of the IDE of your choice.

38
00:02:33,930 --> 00:02:37,570
You can also use Ola and Ola cloud models.

39
00:02:37,570 --> 00:02:39,970
While we use the local large language models.

40
00:02:40,610 --> 00:02:47,170
We can also use the OpenAI models if we wanted because it could be super fast if you have those models,

41
00:02:47,370 --> 00:02:48,370
API keys.

42
00:02:48,610 --> 00:02:52,650
And also we are going to be using Selenium and Playwright as the testing tool.

43
00:02:52,690 --> 00:02:56,210
Of course, while we do these self-healing tests.

44
00:02:56,330 --> 00:03:01,650
Well, as I said, this is going to be an extensive list of libraries that we are going to be using.

45
00:03:01,810 --> 00:03:07,570
And I'm telling you, this particular course is going to be so much fun because while I'm building this

46
00:03:07,570 --> 00:03:10,650
entire code, it was really, really awesome.

47
00:03:10,690 --> 00:03:14,890
In our next lecture, I'm going to quickly show you a demo of how all of these are going to work, so

48
00:03:14,890 --> 00:03:17,970
that you can get a feel of what you are going to be building.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 3. Traditional Automation Test and its Problems

1
00:00:00,200 --> 00:00:05,960
In this lecture, I'm going to show you a traditional test, which you can actually execute without

2
00:00:05,960 --> 00:00:08,480
any of the AI source in it.

3
00:00:08,720 --> 00:00:16,200
And in our next test, I'm going to show you how you can run the same test using a artificial intelligence

4
00:00:16,200 --> 00:00:18,120
based self-healing approach.

5
00:00:18,400 --> 00:00:24,760
So you can see that this particular code over here is essentially a traditional test, which has got

6
00:00:24,800 --> 00:00:25,960
no AI in it.

7
00:00:26,000 --> 00:00:31,640
It's been written using selenium, C-sharp, dotnet, and I am using a writer IDE for that matter.

8
00:00:31,640 --> 00:00:36,520
So if you're just going to go to the writer ID over here and if you hit about JetBrains IDE over here,

9
00:00:36,520 --> 00:00:43,480
you can see that I'm using a non-commercial use only license over here, which means this particular

10
00:00:43,480 --> 00:00:50,760
license is a free version of the IDE, which you can use in Mac, Windows and Linux operating system.

11
00:00:50,760 --> 00:00:56,000
So if you have never used the writer IDE before, I highly recommend you to do so because it's a super

12
00:00:56,000 --> 00:01:01,000
awesome IDE, and it is far more better than Visual Studio itself.

13
00:01:01,040 --> 00:01:06,880
Well, as I said, because I'm using Mac operating system, I am inclined towards using this particular

14
00:01:06,880 --> 00:01:12,660
IDE ID because it is better than the VS code, because you don't have all the features that you can

15
00:01:12,660 --> 00:01:13,980
get it from this particular IDE.

16
00:01:14,300 --> 00:01:19,380
So this is the ID that I'm currently using, and I'm going to quickly show you what code I have written

17
00:01:19,380 --> 00:01:20,220
over here.

18
00:01:20,260 --> 00:01:22,540
You see that I'm just setting the Chrome options.

19
00:01:22,540 --> 00:01:23,940
Nothing fancy there.

20
00:01:23,940 --> 00:01:31,380
And I'm also passing the chrome driver over here in the selenium, which is going to invoke the browser

21
00:01:31,380 --> 00:01:32,140
driver.

22
00:01:32,140 --> 00:01:37,740
And then I'm going to navigate to this particular website over here, which is the app.com.

23
00:01:37,940 --> 00:01:44,460
And I have written a simple page object model code for the home page, which has got the login link

24
00:01:44,860 --> 00:01:51,300
and the employee details link, manage user link and the log of link over here is all sitting on the

25
00:01:51,340 --> 00:01:52,100
home page.

26
00:01:52,220 --> 00:01:55,420
And the only operation which I'm performing over here is clicking them.

27
00:01:55,700 --> 00:01:58,260
That's all the other thing that I'm doing over here.

28
00:01:58,460 --> 00:02:05,500
And for the login page, all I have done over here is selecting a username password, clicking the submit

29
00:02:05,500 --> 00:02:11,100
button and then Remember Me checkbox, which I'm currently not using so I can even get rid of that so

30
00:02:11,100 --> 00:02:12,940
that I can reduce the number of lines of code.

31
00:02:13,140 --> 00:02:18,000
And you see that it is just doing a simple constructor operation over here, which I can essentially

32
00:02:18,000 --> 00:02:19,200
put it on the top.

33
00:02:19,600 --> 00:02:25,080
Uh, and then it is clicking uh, is entering the username and password for me over here.

34
00:02:25,120 --> 00:02:25,800
That's all.

35
00:02:25,800 --> 00:02:27,680
This is the super simple code.

36
00:02:27,880 --> 00:02:29,480
Two classes over here.

37
00:02:29,480 --> 00:02:33,000
And there is an enhanced tests which has got a traditional test in it.

38
00:02:33,000 --> 00:02:34,560
It's really not enhanced, to be honest.

39
00:02:34,840 --> 00:02:38,080
And if I'm going to run this test, you know what is going to happen, right?

40
00:02:38,120 --> 00:02:42,400
It is just going to execute like any other selenium test.

41
00:02:42,440 --> 00:02:48,240
It's going to open the application logs in, and then it's going to perform all the operations that

42
00:02:48,240 --> 00:02:49,120
I have specified.

43
00:02:49,120 --> 00:02:54,280
And the test has got passed over here, which we know how it works in selenium.

44
00:02:54,280 --> 00:02:59,280
If you really have not worked in selenium before, I highly recommend you to watch my other videos where

45
00:02:59,280 --> 00:03:05,720
I've talked about the selenium v dotnet from Complete Basics, so that course will help you how you

46
00:03:05,720 --> 00:03:08,040
can get up and running with selenium.

47
00:03:08,680 --> 00:03:13,160
And now coming back to the traditional tests problems.

48
00:03:13,400 --> 00:03:16,880
So what exactly is the problem that we have got with the traditional tests.

49
00:03:17,080 --> 00:03:23,540
Well let's say in the login page over here or maybe in the home page over here if I'm going to go and

50
00:03:23,540 --> 00:03:30,580
change the locator, maybe the UI of the locator has changed from like a login link to maybe login link

51
00:03:30,580 --> 00:03:31,260
or something like that.

52
00:03:31,260 --> 00:03:37,060
I know it's never going to happen, but just for the hypothetical case over here, I've made it to logins

53
00:03:37,100 --> 00:03:39,140
for some reason, right?

54
00:03:39,180 --> 00:03:43,340
And that's what has changed in the UI of the application for that matter.

55
00:03:43,340 --> 00:03:50,380
Or maybe your test code has got an obsolete locator and it has changed, uh, in the application.

56
00:03:50,380 --> 00:03:53,420
And you may need to now go and fix your test code.

57
00:03:53,420 --> 00:03:54,620
It can happen either way.

58
00:03:54,980 --> 00:03:57,820
But let's say this is changing over here.

59
00:03:57,980 --> 00:04:02,340
And now if we're going to run this particular traditional test, guess what's going to happen?

60
00:04:02,340 --> 00:04:05,060
Just think about it before you answer it.

61
00:04:06,540 --> 00:04:07,380
That's right.

62
00:04:07,380 --> 00:04:09,740
The test is eventually going to fail.

63
00:04:09,940 --> 00:04:13,420
So the the moment I run this test over here look at that.

64
00:04:13,460 --> 00:04:14,940
It's not going to click the login.

65
00:04:14,940 --> 00:04:17,620
And immediately the selenium is going to give up.

66
00:04:17,620 --> 00:04:25,180
And saying no element found or unable to locate the element logins because it doesn't exist.

67
00:04:25,420 --> 00:04:26,060
Amazing.

68
00:04:26,380 --> 00:04:27,580
So what is the solution.

69
00:04:27,890 --> 00:04:28,610
Me?

70
00:04:28,650 --> 00:04:29,890
Are you as a test engineer?

71
00:04:29,970 --> 00:04:33,650
Go and do we go and change the locator?

72
00:04:34,090 --> 00:04:38,010
Or we just go and see that the locator has something gone wrong?

73
00:04:38,010 --> 00:04:44,490
So we go to the Chrome browser and then we figure out the locator link has changed from login to logins.

74
00:04:44,490 --> 00:04:48,450
So we go and inspect the element something like this from Chrome dev tool.

75
00:04:48,730 --> 00:04:52,730
We see that oh I guess what we can use an ID for that matter to make it work.

76
00:04:52,730 --> 00:04:55,810
If not, this is just going to fail, right?

77
00:04:56,250 --> 00:05:01,570
But what if we have an more elegant approach to take care of?

78
00:05:01,570 --> 00:05:03,770
The locator changes automatically.

79
00:05:04,690 --> 00:05:05,810
Is it even possible?

80
00:05:06,130 --> 00:05:11,410
Well guess what, there were many tool came out to fix this particular problem.

81
00:05:11,450 --> 00:05:14,850
One of the tool which I worked previously was the test projects.

82
00:05:14,850 --> 00:05:18,570
I'm not sure whether you have heard about the tool or not.

83
00:05:18,610 --> 00:05:24,410
That tool really had an option to go and self-heal the locators automatically.

84
00:05:24,570 --> 00:05:31,410
The way they do it is they store all the different combinations of locators for one single locator.

85
00:05:31,450 --> 00:05:38,070
For example, the login link can be identified using the link text as login, or they can also be identified

86
00:05:38,070 --> 00:05:41,790
using the ID as login link.

87
00:05:41,830 --> 00:05:47,270
They can also be identified using the CSS locator or using the XPath and using name.

88
00:05:47,270 --> 00:05:53,150
If there is any right, you can identify the same using four combinations of locator.

89
00:05:53,310 --> 00:05:58,950
The same thing goes for the text box as well, where you can identify using its ID, its name, its

90
00:05:58,950 --> 00:06:01,670
CSS, its XPath, something like that.

91
00:06:01,990 --> 00:06:05,830
So these are the four ways you can control this particular.

92
00:06:05,870 --> 00:06:07,790
You can locate this particular element.

93
00:06:07,790 --> 00:06:12,430
And then you can store all of them into a collection and iterate through all the elements in the collection

94
00:06:12,430 --> 00:06:14,230
and find which one is working.

95
00:06:15,190 --> 00:06:17,310
That's one possible way of doing it.

96
00:06:17,310 --> 00:06:19,150
That's a classical approach.

97
00:06:19,590 --> 00:06:26,630
But now we are going to see how we can actually enhance the entire test with the power of large language

98
00:06:26,630 --> 00:06:31,270
model, the Overlord, which is going to do all these operation for you.

99
00:06:31,270 --> 00:06:36,630
And I'm going to show you how everything is going to happen with super minimal code change with the

100
00:06:36,630 --> 00:06:42,230
power of large language model, and we will see how the same test can be enhanced from there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 4. How AI will do Self Healing of Locators in Selenium with the Power of AI

1
00:00:00,160 --> 00:00:02,920
All right, so now it's magic time.

2
00:00:02,920 --> 00:00:07,400
We are gonna see how a simple locator change actually failed.

3
00:00:07,400 --> 00:00:14,280
Our entire test with a traditional test approach can be fixed using the self-healing approach that I

4
00:00:14,280 --> 00:00:15,160
have built.

5
00:00:15,160 --> 00:00:20,440
And we are going to build this together in the course of time in this course.

6
00:00:20,680 --> 00:00:22,560
So you can see that this is the code.

7
00:00:22,560 --> 00:00:25,680
I'm not going to get into the utilities section over here.

8
00:00:25,680 --> 00:00:28,880
It's going to be super confusing if I'm going to show you right now.

9
00:00:29,000 --> 00:00:34,760
But there is an app settings which is going to give you some context already, and you can see that

10
00:00:34,760 --> 00:00:40,680
this particular app settings over here is going to tell you that we are using a provider as local large

11
00:00:40,680 --> 00:00:41,800
language model.

12
00:00:41,800 --> 00:00:46,160
And because we are using local large language model, we don't need to have an API key for that matter.

13
00:00:46,160 --> 00:00:47,320
So it's just empty.

14
00:00:47,720 --> 00:00:54,120
And we also have a base URL of our olama that we is that is currently running within our local machine.

15
00:00:54,120 --> 00:00:57,560
You remember the Olama serve that you do the same exact thing.

16
00:00:57,600 --> 00:01:03,400
And I'm using a model which is actually a combination of the model running on the cloud.

17
00:01:03,400 --> 00:01:08,000
So I'm using a Q1 three quarter model with a 480 billion parameter.

18
00:01:08,040 --> 00:01:12,160
You may ask, hey Karthik, you know what you just told about the privacy and all those things, but

19
00:01:12,160 --> 00:01:13,800
now you're using the cloud model.

20
00:01:13,800 --> 00:01:15,840
So where is your privacy thing that is gone?

21
00:01:15,880 --> 00:01:17,720
Guess what I totally understand.

22
00:01:17,760 --> 00:01:27,520
We can change this model to the GPT Oasis 20 billion parameter and the three quarter with just 30 billion

23
00:01:27,520 --> 00:01:28,320
parameter as well.

24
00:01:28,360 --> 00:01:29,880
We are going to do that in this course.

25
00:01:29,880 --> 00:01:34,440
But for now, for this demonstration, I'm just going to use this particular model over here.

26
00:01:34,640 --> 00:01:37,920
And I'm setting the temperature and the max tokens over here.

27
00:01:38,200 --> 00:01:43,520
And I'm not going to let more tokens to be flown to burn my cars there.

28
00:01:44,640 --> 00:01:47,000
But as I said, how about the coding part?

29
00:01:47,040 --> 00:01:49,000
This is exactly the same code you remember.

30
00:01:49,240 --> 00:01:50,480
Same code.

31
00:01:50,640 --> 00:01:51,680
No change.

32
00:01:51,800 --> 00:01:56,840
But the only change which has happened is in the utilities, which we are going to be building anyways.

33
00:01:57,160 --> 00:01:58,920
And look at the home page.

34
00:01:58,920 --> 00:02:01,240
This time a bit changed.

35
00:02:01,280 --> 00:02:03,040
It is definitely a bit changed.

36
00:02:03,080 --> 00:02:08,080
You see, we are using a task of web element, pretty much like if you're using playwright before,

37
00:02:08,360 --> 00:02:12,880
you might have seen that every single code is asynchronous in playwright.

38
00:02:12,880 --> 00:02:17,520
And that's exactly we are going to be implementing in selenium for the first time.

39
00:02:17,760 --> 00:02:18,360
There we go.

40
00:02:18,800 --> 00:02:20,080
And look at that.

41
00:02:20,080 --> 00:02:24,840
We have got the same find element, but you have got a friendly name there.

42
00:02:25,240 --> 00:02:28,840
Look at the the locator there logins.

43
00:02:29,440 --> 00:02:31,280
It's two three years now.

44
00:02:31,760 --> 00:02:34,280
So we are going to see how that is going to work.

45
00:02:34,280 --> 00:02:35,120
And guess what.

46
00:02:35,520 --> 00:02:38,440
The code of the rest of thing remains exactly the same.

47
00:02:38,440 --> 00:02:43,520
But only thing is because we're using an asynchronous coding, it is going to be async of task.

48
00:02:43,800 --> 00:02:50,120
That is the only change has happened over here and login page.

49
00:02:50,680 --> 00:02:51,640
Look at that.

50
00:02:51,680 --> 00:02:53,720
How bad the locators can be.

51
00:02:53,760 --> 00:02:55,320
You can just imagine it.

52
00:02:55,320 --> 00:02:58,800
But they are all just going to work because we have got a friendly name.

53
00:02:58,800 --> 00:03:03,600
It's going to say that username field, password field and you can even give like use.

54
00:03:03,640 --> 00:03:06,240
It is a username field, something like that.

55
00:03:06,280 --> 00:03:08,760
It will still going to go and identify for you.

56
00:03:08,960 --> 00:03:11,040
That's how this system is being designed.

57
00:03:12,240 --> 00:03:16,640
And the code remains exactly the same for both of them.

58
00:03:16,640 --> 00:03:17,880
No change on that.

59
00:03:18,160 --> 00:03:20,440
And let's go to the enhanced test over here.

60
00:03:20,440 --> 00:03:24,760
It is still the exact same code that we just executed over here.

61
00:03:24,800 --> 00:03:28,800
If you just see this is the same code, no change on that.

62
00:03:29,000 --> 00:03:35,200
The only change which we did is on the locator side and of course on the utilities over here.

63
00:03:36,120 --> 00:03:38,840
Now let's try to run this code and see what is going to happen.

64
00:03:39,120 --> 00:03:44,240
So I'm going to run this code and you will notice that the locators are all super bad.

65
00:03:44,280 --> 00:03:50,110
It is all just like username passwords, some thing over there.

66
00:03:50,110 --> 00:03:54,670
And look at the at the logins over there, which is quite bad as well.

67
00:03:54,950 --> 00:04:00,790
So if I'm going to run this particular test this time, you will notice that it is going to open the

68
00:04:00,790 --> 00:04:01,510
application.

69
00:04:01,510 --> 00:04:06,950
But the login is going to take some time before it clicks, because there is some process going on there.

70
00:04:07,430 --> 00:04:14,030
And the admin username and password has took some time as well before it performs an operation and see

71
00:04:14,190 --> 00:04:16,950
the login button is also been clicked this time.

72
00:04:17,470 --> 00:04:17,910
Boom!

73
00:04:18,310 --> 00:04:25,670
It took 18 seconds 953 milliseconds to perform this operation, as opposed to just for a second while

74
00:04:25,670 --> 00:04:28,030
we were executing with a failing test.

75
00:04:28,070 --> 00:04:32,470
Of course, go and fix this particular test and see what's going to happen if I'm going to run the working

76
00:04:32,510 --> 00:04:35,710
test, uh, which is of no self-healing.

77
00:04:35,950 --> 00:04:40,190
It was running, I think, quite faster because it has got all the locators.

78
00:04:40,710 --> 00:04:47,310
Boom, It took seven seconds, but with the AI it took 18.9 seconds.

79
00:04:47,510 --> 00:04:47,950
Hmm.

80
00:04:48,630 --> 00:04:55,990
I know there is a delay, but it has actually managed to run the test without any issue.

81
00:04:56,030 --> 00:05:01,870
It is not really going to update your page object model code there, but it is trying to run the test

82
00:05:01,910 --> 00:05:05,270
even with a sensible locator strategy.

83
00:05:05,310 --> 00:05:07,510
So that's how it is really going to work.

84
00:05:07,710 --> 00:05:08,510
And look at that.

85
00:05:08,550 --> 00:05:09,670
How fast it is.

86
00:05:09,670 --> 00:05:14,990
14 seconds just double the amount of execution, but it's still going to work.

87
00:05:15,630 --> 00:05:17,350
This is the power of AI guys.

88
00:05:17,350 --> 00:05:20,990
It's all running with a local large language model over there.

89
00:05:21,230 --> 00:05:26,910
I know it is not truly local large language model, but we can change the model and see how that works.

90
00:05:26,910 --> 00:05:34,510
So I'm going to open a terminal over here, and I'm going to see if I'm going to use the Q1 quarter

91
00:05:34,510 --> 00:05:38,910
330 billion parameter model instead of the cloud model that we were using.

92
00:05:38,910 --> 00:05:46,790
So I go to the app settings over here, and I'm going to change this model to 30 billion parameter model.

93
00:05:46,790 --> 00:05:48,230
And now I'm going to run.

94
00:05:48,510 --> 00:05:54,870
I know it is going to take some time because it is not really using the cloud model.

95
00:05:55,030 --> 00:06:01,350
Uh, so it is going to be slower as opposed to the 18 milliseconds which was working before.

96
00:06:01,590 --> 00:06:06,470
It is going to take some time because it depends on the machine's performance as well.

97
00:06:07,310 --> 00:06:08,310
And there we go.

98
00:06:08,350 --> 00:06:10,870
It took 45 seconds this time.

99
00:06:10,950 --> 00:06:16,950
Um, I know this is going to happen because my machine is of course M1 Max.

100
00:06:16,950 --> 00:06:24,830
It still can pull out the speed, but it is not as great model because M1 Max was introduced way back

101
00:06:24,830 --> 00:06:32,950
in 2021, and during that time, the large language model was not even a thing because the large language

102
00:06:32,950 --> 00:06:42,590
model was started to introduce only in 2021, where the ChatGPT was released, and then people started

103
00:06:42,590 --> 00:06:44,470
getting crazy during that time.

104
00:06:44,470 --> 00:06:47,470
So Apple didn't even know that these things are going to happen.

105
00:06:47,470 --> 00:06:53,310
That's the reason why these machines, like M1 machines, don't have the capability to run a bigger

106
00:06:53,310 --> 00:06:53,830
model.

107
00:06:53,830 --> 00:07:00,510
But of course, as I told you, if you're using the latest generation of the Nvidia spark machine or

108
00:07:00,630 --> 00:07:07,510
maybe the upcoming M5 machines, those machines are very better in the NPU processing, so you will

109
00:07:07,510 --> 00:07:11,310
see a better performance during that time using these models.

110
00:07:11,310 --> 00:07:12,470
But hey, what?

111
00:07:12,710 --> 00:07:15,030
The self-healing is already happening.

112
00:07:15,070 --> 00:07:23,390
It's running even for an completely scrambled, jeopardized locator without any issue.

113
00:07:23,630 --> 00:07:25,710
That's the power that we are talking about.

114
00:07:25,710 --> 00:07:29,070
This is what we are going to be building in this entire course.

115
00:07:29,070 --> 00:07:30,710
And you have already seen the.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 5. Prompting LLMs to get Self Healed Alternative Locators

1
00:00:00,360 --> 00:00:01,640
All right.

2
00:00:01,640 --> 00:00:09,040
So now that you have seen a demo of how the AI self-healing code really works, and now we are going

3
00:00:09,040 --> 00:00:12,680
to see how we can achieve the same thing manually.

4
00:00:12,880 --> 00:00:16,720
And then we will try to start optimizing it from there on.

5
00:00:16,920 --> 00:00:23,800
So the way we are going to do it manually is we need to now pass a page to the large language model,

6
00:00:23,800 --> 00:00:29,680
and then we need to get the page locators from the large language model.

7
00:00:29,680 --> 00:00:33,960
So for instance I'm going to go to my page over here for that matter.

8
00:00:34,080 --> 00:00:41,120
And I wanted to pass this page to the large language model, which is nothing but the sonnet 4.5 model

9
00:00:41,440 --> 00:00:45,440
using the cloud desktop, and then get the locators out from it.

10
00:00:45,960 --> 00:00:46,960
How can I do it?

11
00:00:47,000 --> 00:00:54,000
Well guess what, you can either paste this page over here and then ask, because nowadays these large

12
00:00:54,000 --> 00:00:59,640
language model comes with the web search feature or even the playwright MCP server.

13
00:00:59,680 --> 00:01:03,560
You remember these were the things that we were discussing in our last section of this course.

14
00:01:03,560 --> 00:01:06,220
So you can get those information out from there.

15
00:01:06,660 --> 00:01:10,940
Or you can also pass the entire source code of the page.

16
00:01:10,980 --> 00:01:12,340
You know why we are doing it?

17
00:01:12,340 --> 00:01:19,900
Because the local large language model may not have internet access, so you can't really pass the URL

18
00:01:19,940 --> 00:01:25,700
something like this and get the locators out from the local large language models.

19
00:01:26,220 --> 00:01:31,060
There is still a way to do a web search in Olama, which I'm not going to talk about.

20
00:01:31,060 --> 00:01:37,620
You can do a web search and web fetch operation using Olama using local large language models.

21
00:01:37,620 --> 00:01:47,780
So if you go and search for Olama web search and web fetch tool and you see that they have got a way

22
00:01:47,780 --> 00:01:53,860
you can do it, and I have already talked about that as well in my YouTube channel before, which you

23
00:01:53,860 --> 00:02:01,740
can actually do it as well over here, uh, using this search operation, which guess what?

24
00:02:01,780 --> 00:02:06,140
Because we have told and I have promised you that we are going to be working with a local large language

25
00:02:06,140 --> 00:02:06,780
model.

26
00:02:06,780 --> 00:02:09,840
I'm not going gonna incline toward those operations.

27
00:02:10,200 --> 00:02:14,320
So what we're going to do is we are going to pass the entire page source itself.

28
00:02:14,320 --> 00:02:16,320
So I'm going to do an inspect over here.

29
00:02:16,640 --> 00:02:19,240
And let's say I'm going to pass the entire page source.

30
00:02:19,280 --> 00:02:19,480
Right.

31
00:02:19,520 --> 00:02:20,560
So view page source.

32
00:02:20,560 --> 00:02:22,320
This is the page source that I have got.

33
00:02:22,480 --> 00:02:26,080
I'm going to copy this whole page source by just doing copy.

34
00:02:26,480 --> 00:02:30,440
And I'm going to go to the cloud desktop over here.

35
00:02:30,760 --> 00:02:35,480
And I'm going to ask it to um get me the locators.

36
00:02:35,480 --> 00:02:43,880
So I'm going to say, can you get me the locators for the page source.

37
00:02:43,920 --> 00:02:53,400
And I'm going to paste that over here, and I'm going to say I want the locators for uh ID, XPath,

38
00:02:53,800 --> 00:03:02,920
uh, CSS and name, uh, and whatever that you have even link text for that matter, whatever that you

39
00:03:02,920 --> 00:03:10,720
think that you need to get it so you can just pass them all over here and then you can, uh, say that

40
00:03:10,760 --> 00:03:19,700
I get them all in a JSON object or JSON format, whatever that you want to name it.

41
00:03:20,020 --> 00:03:22,900
And I'm going to hit run over here.

42
00:03:22,900 --> 00:03:29,380
And the moment I do this, uh, you are going to see that, uh, it is going to get the locators for

43
00:03:29,380 --> 00:03:30,340
you over here.

44
00:03:30,380 --> 00:03:31,540
Oh look at that.

45
00:03:31,580 --> 00:03:33,660
It's going to say navigation link.

46
00:03:33,860 --> 00:03:35,180
And then there is this home.

47
00:03:35,180 --> 00:03:42,180
And within the home you have got the locators which can be identified using link text, XPath and CSS.

48
00:03:42,220 --> 00:03:49,060
Similarly, the about can be identified using link text as about an XPath and CSS and the employee list,

49
00:03:49,380 --> 00:03:52,380
which is this particular URL that we're talking about.

50
00:03:52,420 --> 00:03:55,100
The employee list can be identified using this.

51
00:03:55,380 --> 00:03:58,100
And the register, which is this one.

52
00:03:58,100 --> 00:04:03,460
I think the register link and login link can be identified using these and the login form you can identify

53
00:04:03,460 --> 00:04:04,900
using this particular locators.

54
00:04:05,260 --> 00:04:09,540
And the username can be identified using these uh and look at that.

55
00:04:09,580 --> 00:04:14,440
It's also identify using some CSS alt and CSS type which is?

56
00:04:14,840 --> 00:04:15,440
Guess what?

57
00:04:15,480 --> 00:04:18,200
Are not the locators which selenium can support.

58
00:04:18,200 --> 00:04:23,440
So these locators are kind of something that you don't even care while you work with selenium.

59
00:04:23,440 --> 00:04:30,840
So you only thing which works is probably the ID name XPath, uh, CSS and class name for that matter.

60
00:04:30,840 --> 00:04:34,000
So not the XPath alt which is being supported.

61
00:04:34,280 --> 00:04:39,200
And similarly, uh, you can see that other locators are also going to come up over there.

62
00:04:39,360 --> 00:04:42,840
So these are the ways that you can get the locators.

63
00:04:42,840 --> 00:04:44,080
But guess what.

64
00:04:44,120 --> 00:04:50,240
Now you may think Karthik, this particular prompt that we have got can be improved because it is giving

65
00:04:50,240 --> 00:04:51,800
me a lot of information.

66
00:04:51,800 --> 00:04:53,800
How can I improve this particular prompt?

67
00:04:53,840 --> 00:04:59,040
You know what, I'm going to ask this to the large language model itself so that we can get what we

68
00:04:59,080 --> 00:04:59,840
are looking for.

69
00:05:00,080 --> 00:05:13,280
So I'm going to say can you write me a prompt which I can use to get the locators, uh, from the given

70
00:05:13,320 --> 00:05:14,400
page source.

71
00:05:15,360 --> 00:05:28,930
And I'm also going to say get me the locators for ID name, XPath, CSS selector and maybe class name

72
00:05:29,250 --> 00:05:30,330
and link.

73
00:05:30,370 --> 00:05:32,130
Text only these right?

74
00:05:32,170 --> 00:05:42,690
And I'm also going to say format uh as a, a proper uh JSON with probably double quotes if possible,

75
00:05:42,730 --> 00:05:45,170
because that's what it has done already.

76
00:05:45,170 --> 00:05:49,970
But still make sure that you say all of these and I'm going to hit enter.

77
00:05:50,090 --> 00:05:52,370
And now guess what is going to happen.

78
00:05:52,530 --> 00:05:57,810
This particular large language model is going to start writing a prompt for you.

79
00:05:58,010 --> 00:05:59,690
Ooh look at that.

80
00:05:59,730 --> 00:06:06,130
Saying analyze the provided HTML page source and extract all the locators for the interactive elements

81
00:06:06,130 --> 00:06:07,090
like all of these.

82
00:06:07,090 --> 00:06:09,050
So it's adding some more ideas for me.

83
00:06:09,090 --> 00:06:14,410
It's also saying that for each element provide the following locator types where applicable like ID

84
00:06:14,450 --> 00:06:15,730
name, XPath.

85
00:06:15,770 --> 00:06:20,170
It's also saying provide multiple variations by ID name attributes by text.

86
00:06:20,210 --> 00:06:20,750
Ooh Oof!

87
00:06:21,070 --> 00:06:22,430
That I don't think we need it.

88
00:06:22,630 --> 00:06:27,070
And CSS selector class name link text for the anchor tags.

89
00:06:27,470 --> 00:06:33,630
And it also says that output the locators in a well structured JSON format with a proper double quotes.

90
00:06:33,830 --> 00:06:36,310
Organize the element logically by their purpose.

91
00:06:36,310 --> 00:06:36,790
Example.

92
00:06:36,790 --> 00:06:37,630
Navigation.

93
00:06:37,790 --> 00:06:40,910
I think these things are not even required, but still it is adding it.

94
00:06:41,230 --> 00:06:42,870
And it's also saying uh.

95
00:06:42,870 --> 00:06:43,430
Requirement.

96
00:06:43,430 --> 00:06:45,350
Use the proper JSON syntax.

97
00:06:45,350 --> 00:06:48,350
Include all the interactive elements, provide multiple locators.

98
00:06:48,470 --> 00:06:50,910
Ooh, just pretty cool right?

99
00:06:51,230 --> 00:06:53,550
This is already amazing.

100
00:06:54,430 --> 00:06:55,270
And look at that.

101
00:06:55,270 --> 00:06:56,310
There is a page source.

102
00:06:56,310 --> 00:06:57,910
It's also adding it over here.

103
00:06:57,910 --> 00:07:00,110
So we can use this prompt now.

104
00:07:00,310 --> 00:07:03,710
And we can ask the question and see how that works.

105
00:07:03,710 --> 00:07:08,590
So I'm going to go and paste this over here, this particular uh prompt.

106
00:07:08,790 --> 00:07:13,590
And I'm going to get the page source one more time, which is this one.

107
00:07:13,870 --> 00:07:19,190
And I'm going to paste it, and I'm going to run the same prompt that we have got.

108
00:07:19,190 --> 00:07:22,030
And let's see what we are going to get this time.

109
00:07:22,190 --> 00:07:23,350
And look at that.

110
00:07:23,390 --> 00:07:24,690
It's immediate.

111
00:07:25,050 --> 00:07:28,930
We have got it perfectly over here like XPath.

112
00:07:29,130 --> 00:07:31,050
These are the locator CSS.

113
00:07:31,090 --> 00:07:34,250
These are the locators and ID and the link text is this one.

114
00:07:34,970 --> 00:07:36,290
This is for the home link.

115
00:07:36,730 --> 00:07:45,650
Similarly for the about link employee list link, register link login links and all of these.

116
00:07:45,930 --> 00:07:49,850
So this is how you can write a prompt to get this happen.

117
00:07:49,970 --> 00:07:53,210
And you see that this is going to be always consistent.

118
00:07:53,210 --> 00:07:57,010
Every single time you are going to be asking that question.

119
00:07:57,410 --> 00:07:58,850
It is never going to change.

120
00:07:58,970 --> 00:08:04,250
I think we just missed out the prompt with one thing that while we were copying that, you remember

121
00:08:04,610 --> 00:08:07,370
that we don't need a variations of the XPath.

122
00:08:07,570 --> 00:08:12,610
Uh, I think that's the reason why it is just bringing up this time, which we can probably change this

123
00:08:12,610 --> 00:08:13,250
over here.

124
00:08:13,330 --> 00:08:19,130
So let me go and copy one more time, and I'm going to paste that over here.

125
00:08:19,370 --> 00:08:23,210
And I'm just going to say just provide the XPath with multiple variations.

126
00:08:23,210 --> 00:08:24,370
We don't need it.

127
00:08:25,010 --> 00:08:32,630
And similarly for the class name, which is fine, and also for CSS, don't provide the multiple variations.

128
00:08:32,630 --> 00:08:33,350
We don't need it.

129
00:08:33,350 --> 00:08:39,150
Just give the CSS class and do not organize the element locator by their purpose.

130
00:08:39,150 --> 00:08:41,070
We don't need that over here.

131
00:08:41,390 --> 00:08:45,910
Uh, and I think the remaining things looks pretty much exactly the same.

132
00:08:46,110 --> 00:08:48,670
And I think the structure is also fine.

133
00:08:48,870 --> 00:08:53,830
It has given a structure like how it should be, uh, generated as well.

134
00:08:53,830 --> 00:08:59,630
So this is proving to the point that it is always going to be the same for us every single time.

135
00:08:59,910 --> 00:09:07,990
And now I'm going to run this code and you will see that this code is just going to work over here.

136
00:09:08,510 --> 00:09:09,270
Look at that.

137
00:09:09,590 --> 00:09:15,950
So this is the way that we can actually fine tune our prompts and we can get how we are looking for

138
00:09:15,990 --> 00:09:16,910
which is amazing.

139
00:09:17,630 --> 00:09:23,350
So hope you got the idea of how we can start doing the prompt and how we are getting the locators that

140
00:09:23,350 --> 00:09:24,230
we're looking for.

141
00:09:24,230 --> 00:09:31,250
So even if the locators in the UI changes dynamically for some reason, we can go and prompt the large

142
00:09:31,250 --> 00:09:35,890
language model and get the output that we are looking for immediately over here.

143
00:09:35,890 --> 00:09:44,010
And this way we can start aligning our current test approach or current locator finding approach with

144
00:09:44,010 --> 00:09:50,170
the latest locator that we have got over here, and then start using them while performing the operation.

145
00:09:50,570 --> 00:09:57,410
These are the things we are going to be doing starting our next lecture of this particular course.

146
00:09:57,410 --> 00:10:04,370
But before that, we'll first need to figure out how we can talk with the large language model using

147
00:10:04,490 --> 00:10:05,650
C sharp code.

148
00:10:05,770 --> 00:10:11,250
And that is what is going to be the starting point to work with large language model, which we are

149
00:10:11,250 --> 00:10:15,050
going to be doing everything starting our next section.

150
00:10:15,050 --> 00:10:19,530
So this is the foundation element that you have learned so far in this particular section.

151
00:10:19,530 --> 00:10:23,330
In our next section, we are going to start writing the actual code.

152
00:10:23,330 --> 00:10:29,690
So get ready and put your developer hats right now while you are still doing testing, because right

153
00:10:29,690 --> 00:10:35,250
now you are going to be writing quite some code to achieve the operation that we just saw as a demo.


==================================================================================


section 5. Building Foundational Component Talking with Local LLMs and Cloud AI LLMs

video 1. introduction

1
00:00:00,160 --> 00:00:02,120
Welcome to the next section of our course.

2
00:00:02,120 --> 00:00:07,080
And in this section we are going to start talking about building AI driven, self-healing, intelligent

3
00:00:07,120 --> 00:00:08,400
test automation code.

4
00:00:08,600 --> 00:00:13,440
So starting this section is where we are going to start fusing all the knowledge that we have gained

5
00:00:13,440 --> 00:00:15,560
in our earlier sections of this course.

6
00:00:15,760 --> 00:00:22,360
So we have been talking about how the prompt works and how the context engineering works, and how you

7
00:00:22,360 --> 00:00:29,960
can do WIP coding and how AI agents are involved on giving the large language model the ability to go

8
00:00:29,960 --> 00:00:31,320
and generate the code.

9
00:00:31,320 --> 00:00:39,400
And then we also saw how we can do a prompt, and then we can perform a code execution like automatic

10
00:00:39,400 --> 00:00:43,920
self-healing code using the power of local large language models.

11
00:00:44,000 --> 00:00:47,280
So with that, we have understood how things are going to work.

12
00:00:47,320 --> 00:00:51,280
At least we now know the context of how exactly we are going to start building it.

13
00:00:51,280 --> 00:00:57,920
But now we wanted to see how that we are going to put all of the learnings into action.

14
00:00:58,080 --> 00:01:04,880
Well, as I said in our last section, we saw how the prompting of a large language model works by giving

15
00:01:04,920 --> 00:01:08,130
a fine tuned prompt and we got the response.

16
00:01:08,130 --> 00:01:10,370
Something like this, as you can see over here.

17
00:01:10,370 --> 00:01:15,170
So we saw how things were working at least until our last section.

18
00:01:15,170 --> 00:01:22,130
So with this knowledge in place now, we know that if we pass a full blown, uh, source code of the

19
00:01:22,170 --> 00:01:29,450
page, we can get the response something like this from a large language model, this is going to be

20
00:01:29,450 --> 00:01:33,010
the same, even if you are going to try with our local large language model as well.

21
00:01:33,010 --> 00:01:39,610
So if you are going to have the Ola client, you can do the exact same prompt and then you can get the

22
00:01:39,610 --> 00:01:41,210
same response as well.

23
00:01:41,210 --> 00:01:43,250
And there is no difference on that.

24
00:01:43,250 --> 00:01:50,650
Just to show you an example of how this works, I'm going to go and copy this entire prompt from here,

25
00:01:50,810 --> 00:01:53,410
and I'm going to open the Ola client.

26
00:01:53,410 --> 00:01:55,650
And then I'm going to paste this over here.

27
00:01:55,650 --> 00:02:02,570
And I'm going to be using the uh, 30 billion parameter, the quarter 30 billion parameter over here.

28
00:02:02,770 --> 00:02:07,530
And I'm going to pass the source code of the page, which is this one as you remember.

29
00:02:07,530 --> 00:02:13,610
So I'm going to pass exactly the same thing like how I did pass to the cloud desktop.

30
00:02:13,770 --> 00:02:19,460
I'm going to go and copy this one over here, and I'm going to paste this and I'm going to run.

31
00:02:19,460 --> 00:02:26,020
So the moment I do this now you see that I'm actually using the local large language model, which is

32
00:02:26,020 --> 00:02:29,500
running within my own machine in the olama over here.

33
00:02:29,700 --> 00:02:35,740
And we are going to get the similar kind of responses where we are not even using the internet over

34
00:02:35,740 --> 00:02:42,340
here, and you see that it's getting the same exact response, like how we were getting even from the

35
00:02:42,740 --> 00:02:43,620
cloud desktop.

36
00:02:43,660 --> 00:02:47,940
See that now it is actually giving us this pretty much exactly the same response.

37
00:02:48,100 --> 00:02:54,060
This is the power that we are talking about, where we don't have to worry about whether this large

38
00:02:54,060 --> 00:02:59,260
language model is running on the cloud or within our local machine, we are going to get the similar

39
00:02:59,260 --> 00:03:04,700
responses, and you can see that it is still in the JSON format, and it has the details like register

40
00:03:04,700 --> 00:03:08,980
link has got the ID of register link name as register, it is the XPath.

41
00:03:09,020 --> 00:03:10,940
This is the hyperlink it contains.

42
00:03:10,940 --> 00:03:13,260
And this is how you can identify using its XPath.

43
00:03:13,260 --> 00:03:15,780
And similarly it goes for the rest of things as well.

44
00:03:15,980 --> 00:03:22,270
So the same thing we could achieve like how we did in the cloud desktop over here, which is pretty

45
00:03:22,270 --> 00:03:22,670
cool.

46
00:03:23,230 --> 00:03:27,550
So we now know how we can prompt the large language model and get the response.

47
00:03:27,710 --> 00:03:34,910
But next we need to see how we can build this entire system where we are going to pass the complete

48
00:03:34,910 --> 00:03:41,190
source code of the page, or the complete source of the page, and the page object model code that we

49
00:03:41,190 --> 00:03:43,150
have to the large language model.

50
00:03:43,150 --> 00:03:47,510
And then we are going to see how we can match whether there is an obsolete locator.

51
00:03:47,670 --> 00:03:52,310
If there is no obsolete locator, then the selenium test is going to run, but if not, it is going

52
00:03:52,310 --> 00:03:59,070
to go and start updating the latest version of the code from the code logic that we're going to write.

53
00:03:59,070 --> 00:04:01,470
And then we're going to start seeing how things are going to work.

54
00:04:01,470 --> 00:04:04,070
That is how things are going to work over here.

55
00:04:04,070 --> 00:04:09,230
But now, to build this from the complete ground up, we are going to do these operation.

56
00:04:09,430 --> 00:04:15,590
So we are going to start formatting the prompt like how we wanted the local large language model or

57
00:04:15,630 --> 00:04:18,350
the cloud large language model to respond.

58
00:04:18,350 --> 00:04:22,110
And the formatting of the prompt is nothing but this one, as you can see over here.

59
00:04:22,110 --> 00:04:28,800
So we can do the exact similar syntax which we can pass in to our local large language model.

60
00:04:28,800 --> 00:04:33,120
Or we can also use the cloud based large language model systems.

61
00:04:33,240 --> 00:04:39,200
And once we pass to any one of these, we can then see that this large language model is going to return

62
00:04:39,200 --> 00:04:40,840
as a JSON response.

63
00:04:40,880 --> 00:04:45,120
Of course, we need to do some sort of deserialization over here because this is JSON.

64
00:04:45,120 --> 00:04:50,680
So we need to do a JSON serialization over here because that is something very very important.

65
00:04:50,680 --> 00:04:52,480
So we need to do it over here.

66
00:04:52,640 --> 00:04:59,960
And based on the deserialized response from this particular JSON, we are then going to perform a locator

67
00:04:59,960 --> 00:05:01,640
selection strategy.

68
00:05:01,920 --> 00:05:05,680
This is the piece of code that we may need to end up writing bit more.

69
00:05:05,680 --> 00:05:10,720
Because once you write this, this is never going to change because the locators in selenium are not

70
00:05:10,720 --> 00:05:11,480
too much.

71
00:05:11,480 --> 00:05:16,080
So we can just use the same similar locator strategy all the time.

72
00:05:16,120 --> 00:05:18,280
It's regardless like how you're going to do it.

73
00:05:18,280 --> 00:05:20,880
So that's something we are going to build over here.

74
00:05:21,000 --> 00:05:27,160
And once we find the locator, for example, if the ID has changed and we get from the large language

75
00:05:27,160 --> 00:05:33,440
model that you can use something like maybe the name or the CSS or the XPath, something like that.

76
00:05:33,440 --> 00:05:39,090
So then we are going to see whether this strategy can be used, let's say name for that matter.

77
00:05:39,330 --> 00:05:48,210
And then we are going to use that strategy to perform the location of that particular element to run

78
00:05:48,210 --> 00:05:49,450
the test over here.

79
00:05:49,450 --> 00:05:51,330
That is how things are going to flow.

80
00:05:51,330 --> 00:05:53,210
So we're going to find the locate our strategy.

81
00:05:53,210 --> 00:05:56,850
And then we're going to use that particular location within our page object model code.

82
00:05:56,850 --> 00:05:59,050
And finally we are going to run the test.

83
00:05:59,050 --> 00:06:01,130
That is what we are going to be doing over here.

84
00:06:01,130 --> 00:06:07,490
So this is the entire operation that we are going to be doing in this section and upcoming section of

85
00:06:07,490 --> 00:06:08,850
this particular course.

86
00:06:08,850 --> 00:06:12,010
But for now, this is what it's going to look like.

87
00:06:12,170 --> 00:06:16,930
And once we have everything, we are going to see how complex the system is going to be, like something

88
00:06:16,930 --> 00:06:17,410
like this.

89
00:06:17,410 --> 00:06:19,330
And we are going to start building everything.

90
00:06:19,330 --> 00:06:24,650
And once again, just to remind you one more time, we are going to be using these libraries over here.

91
00:06:24,650 --> 00:06:32,170
So make sure you have C sharp Dot net, Visual Studio or Writer ID in my case, and Ola, Ola cloud,

92
00:06:32,170 --> 00:06:34,490
OpenAI, selenium and playwright.

93
00:06:34,490 --> 00:06:39,490
Everything available with you because we are now going to start writing everything from the complete

94
00:06:39,490 --> 00:06:42,290
ground up, starting our next lecture.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 2. Accessing Local LLMs with APIs using Ollama

1
00:00:00,200 --> 00:00:01,240
All right.

2
00:00:01,240 --> 00:00:04,120
So now we are going to see how we can start.

3
00:00:04,120 --> 00:00:11,160
First of all building the way to talk with the large language model, which is nothing but by creating

4
00:00:11,200 --> 00:00:18,960
a C-sharp code within our test automation code, which can go and talk with the large language model.

5
00:00:18,960 --> 00:00:23,080
But now you may have a question that hey Karthik, why are we even doing this?

6
00:00:23,320 --> 00:00:28,200
Aren't there any library which can do that for us directly to talk with the large language model?

7
00:00:28,480 --> 00:00:31,040
Well guess what, you are 100 percentage, right?

8
00:00:31,080 --> 00:00:33,320
There are tons of libraries available.

9
00:00:33,320 --> 00:00:39,760
In fact, you can just use the HTTP client to do the same operation as well because as you know, you

10
00:00:39,760 --> 00:00:48,000
can talk with the local large language model as well as the OpenAI models using the HTTP request itself,

11
00:00:48,000 --> 00:00:50,560
which is nothing but an HTTP client of C.

12
00:00:51,040 --> 00:00:53,320
Net you can use to perform this operation.

13
00:00:53,320 --> 00:00:56,240
But why are we even just building everything from the scratch?

14
00:00:56,240 --> 00:00:57,240
But guess what?

15
00:00:57,480 --> 00:01:04,360
In order to just streamline the process of how you can access the models using these clients.

16
00:01:04,360 --> 00:01:09,320
We are going to be building the code because once you build this code, pretty much like how you build

17
00:01:09,320 --> 00:01:15,120
and test automation framework, you don't necessarily need to worry about how they are going to be working.

18
00:01:15,120 --> 00:01:17,320
That's what we are going to be doing over here.

19
00:01:17,320 --> 00:01:22,880
So the first thing that we are going to be doing this time is going to be building the method, which

20
00:01:22,880 --> 00:01:30,080
can actually talk with the OpenAI large language model as well as the local large language model, as

21
00:01:30,080 --> 00:01:31,640
we can see over here.

22
00:01:31,920 --> 00:01:37,720
Actually, if you are talking with the cloud based large language model, then you can use some libraries

23
00:01:37,720 --> 00:01:39,840
which the company has built as well.

24
00:01:39,840 --> 00:01:43,920
For example, if you're going to be working with the OpenAI model, then you can just go and search

25
00:01:43,920 --> 00:01:49,800
for the OpenAI dotnet NuGet package, which is this one, and where here you can see that this particular

26
00:01:49,800 --> 00:01:57,360
library provides all the details and ways that you can work with the OpenAI models, like the GPT 4.5

27
00:01:57,360 --> 00:02:02,080
or GPT five Pde5 model or GPT 5.5 model or six model that you have.

28
00:02:02,080 --> 00:02:05,240
So you can do any of these model while you really use them.

29
00:02:05,240 --> 00:02:12,080
But if you wanted to go a level further, and if you wanted to just streamline even the process, not

30
00:02:12,080 --> 00:02:17,800
just relying on the OpenAI model, but you wanted to access it with any model for that matter, then

31
00:02:17,840 --> 00:02:20,200
why not just use the HTTP client?

32
00:02:20,240 --> 00:02:26,560
As I told you before, you can access all these models just using the HTTP clients itself.

33
00:02:26,760 --> 00:02:33,000
You don't necessarily need to use any of these library, because all these model can be accessed using

34
00:02:33,120 --> 00:02:36,640
the HTTP client of the C net itself.

35
00:02:36,640 --> 00:02:40,320
So we're just going to go and search for HTTP client C sharp.

36
00:02:40,360 --> 00:02:46,480
Over here you can see that this is the class which is available in the system dot net dot HTTP which

37
00:02:46,480 --> 00:02:48,520
can really help you do all these operations.

38
00:02:48,520 --> 00:02:50,280
It's so straightforward.

39
00:02:50,280 --> 00:02:52,160
So we are going to stick with this approach.

40
00:02:52,160 --> 00:02:54,600
This is going to keep our life more simpler.

41
00:02:54,600 --> 00:03:01,520
And we can do the exact same approach to access the models on the cloud as well as in our local machine.

42
00:03:01,520 --> 00:03:06,560
At the same time, we can also see that it is so much easier while we write the code, because we would

43
00:03:06,560 --> 00:03:12,200
have already been exposed writing these kind of code in automation testing while trying to do the automation

44
00:03:12,200 --> 00:03:14,520
test with an API for that matter.

45
00:03:14,520 --> 00:03:18,120
That's why I wanted to keep things as simple as possible.

46
00:03:18,440 --> 00:03:22,080
Well, as that said, we are going to see how we can really do that.

47
00:03:22,280 --> 00:03:28,320
In order to achieve this operation, I'm going to go and create a simple method in our existing code

48
00:03:28,320 --> 00:03:33,760
that I was just showing you in our last section, where this code is like a selenium test code, which

49
00:03:33,760 --> 00:03:35,480
has got zero intelligence.

50
00:03:35,480 --> 00:03:39,760
So if we go and change any of the locator, the test is eventually going to fail.

51
00:03:39,920 --> 00:03:42,600
But we are going to add intelligence to this test.

52
00:03:42,600 --> 00:03:46,240
From the traditional test to an self-healing test.

53
00:03:46,280 --> 00:03:47,600
You will see how that goes.

54
00:03:48,400 --> 00:03:52,560
So what I'm going to do is I'm going to go and create a folder here.

55
00:03:52,720 --> 00:03:55,160
I'm going to call this as utilities.

56
00:03:55,440 --> 00:03:56,800
And this particular folder.

57
00:03:56,800 --> 00:03:59,360
I'm going to go and create a class file.

58
00:03:59,360 --> 00:04:05,600
And I'm going to name this as LM client or the large language model client.

59
00:04:05,840 --> 00:04:12,240
So this particular class file is responsible for talking with the local large language model as well

60
00:04:12,240 --> 00:04:14,680
as the cloud based language model.

61
00:04:14,680 --> 00:04:17,840
So it can be of anything that you are going to be talking with.

62
00:04:18,120 --> 00:04:24,200
So in order to first talk with the, uh, open AI model or the local large language model, you don't

63
00:04:24,200 --> 00:04:28,240
necessarily have to do anything very, very, uh, amazing over there.

64
00:04:28,400 --> 00:04:33,040
All you have to do it is we just need to streamline the process, like how you're going to be talking

65
00:04:33,040 --> 00:04:37,960
with your large language model, and then you're going to see how you can work with them.

66
00:04:38,080 --> 00:04:43,080
But in order to demonstrate how you can talk with the local large language model using API, like how

67
00:04:43,080 --> 00:04:48,680
we did in our last section, you can just use the postman to do the exact same operation, but again,

68
00:04:48,720 --> 00:04:54,480
in order to do the same with the code, all you have to do it is you just need to formulate the body

69
00:04:54,480 --> 00:04:56,160
that you wanted to pass in.

70
00:04:56,160 --> 00:05:02,240
And once again, you just need to use the endpoints of the llama to make this happen.

71
00:05:02,240 --> 00:05:07,200
So if I'm just going to go to the llama over here one more time, oh llama.

72
00:05:07,880 --> 00:05:12,920
And then API endpoints, which kind of give you all the ideas that you need.

73
00:05:12,920 --> 00:05:18,480
So if you just go to the API reference over here, you can see that there is a generate a completion

74
00:05:18,480 --> 00:05:18,960
endpoint.

75
00:05:18,960 --> 00:05:27,120
So you just need to call this slash API slash generate endpoint in the post operation which is going

76
00:05:27,120 --> 00:05:29,440
to perform the operation for you.

77
00:05:29,440 --> 00:05:33,080
So let's say I'm going to open the postman client over here.

78
00:05:33,240 --> 00:05:40,000
And I'm going to use the URL, which is nothing but the http localhost colon 11434, which is going

79
00:05:40,040 --> 00:05:44,920
to be the port number that you need to access for the local large language model.

80
00:05:45,120 --> 00:05:53,040
And then I'm going to use the endpoint that the company has given from the slash API slash generate.

81
00:05:53,040 --> 00:05:56,160
So I'm going to go and copy that, and I'm going to paste it over here.

82
00:05:56,520 --> 00:05:57,480
And guess what?

83
00:05:57,480 --> 00:05:59,800
You need to pass the post operation.

84
00:05:59,800 --> 00:06:01,920
So I'm going to pass the post over here.

85
00:06:02,200 --> 00:06:07,960
And the parameter that you need to pass in order to get the details over there, in order to get the

86
00:06:07,960 --> 00:06:14,120
generation for this is you need to pass the model, you need to pass the prompt, and then you need

87
00:06:14,120 --> 00:06:18,160
to pass the, uh, the image if you really wanted to.

88
00:06:18,200 --> 00:06:22,960
And if you want, you can also pass the stream, which is going to get you the stream of the responses.

89
00:06:23,160 --> 00:06:27,520
And then you can also pass the optional, uh, options and things of that nature.

90
00:06:27,520 --> 00:06:33,720
So let me go and just pass the body over here, which is going to be a raw body JSON.

91
00:06:34,440 --> 00:06:39,320
And over here I'm going to say uh, sorry, I'm just going to be model.

92
00:06:39,320 --> 00:06:44,640
And the model which I wanted to use, which is sitting in my local machine, uh, is going to be this

93
00:06:44,640 --> 00:06:49,320
guy, the three, uh, model, which is this one.

94
00:06:49,320 --> 00:06:53,400
So I'm going to pass that in a double quotes as well because remember this is a JSON.

95
00:06:53,800 --> 00:07:04,480
And then I'm going to pass the stream, uh, as probably true, which is going to be like a stream response

96
00:07:04,480 --> 00:07:05,440
that I want to get.

97
00:07:05,760 --> 00:07:08,720
And then I can pass the prompt over here.

98
00:07:08,720 --> 00:07:10,280
So I'm going to say prompt.

99
00:07:10,520 --> 00:07:20,800
And in the prompt I'm just going to say, uh, write a selenium with C-sharp dotnet code for google.com

100
00:07:20,800 --> 00:07:23,320
search operation alone.

101
00:07:23,520 --> 00:07:24,200
Something like that.

102
00:07:24,200 --> 00:07:24,400
Right.

103
00:07:24,400 --> 00:07:26,000
This is what I wanted to do.

104
00:07:26,360 --> 00:07:29,280
And now I'm going to do a send operation over here.

105
00:07:29,720 --> 00:07:36,720
The moment I send this, you will notice that it is going to go and send this particular prompt to the

106
00:07:36,760 --> 00:07:42,160
local large language model, which is currently running within my machine.

107
00:07:42,320 --> 00:07:44,640
And then it is going to get you the responses.

108
00:07:44,640 --> 00:07:48,640
Just wait and see what is going to happen over here.

109
00:07:48,640 --> 00:07:53,560
This is pretty much exactly the same thing that we discussed in our earlier sections of this course,

110
00:07:53,560 --> 00:07:56,560
and you will notice that it is getting us the response over here.

111
00:07:56,560 --> 00:08:02,040
So you see that it is getting us the response here saying here is a selenium code.

112
00:08:02,080 --> 00:08:05,800
I know that the response is going to be super big over here.

113
00:08:05,840 --> 00:08:10,480
See how much detail that it has put through in order to get this particular response.

114
00:08:10,480 --> 00:08:16,040
But once you set the stream as false over here, and then if you try to send this, you will see that

115
00:08:16,040 --> 00:08:19,920
the response is going to be different from what we just got over here.

116
00:08:19,920 --> 00:08:23,560
And as you can see that it has generated the code because I've just set the stream as false.

117
00:08:23,560 --> 00:08:28,000
So here is the complete selenium C code for performing search operation in Google.

118
00:08:28,000 --> 00:08:30,280
And has written some code for us over here.

119
00:08:30,320 --> 00:08:30,800
Right.

120
00:08:30,840 --> 00:08:37,800
So this is exactly what we are going to be doing from this particular, uh, normal manual operation

121
00:08:37,800 --> 00:08:39,640
to a C sharp dotnet code.

122
00:08:39,640 --> 00:08:44,160
And we can achieve the exact same thing using the HTTP client itself.

123
00:08:44,160 --> 00:08:46,720
I don't need any special library to do that.

124
00:08:46,720 --> 00:08:51,840
So we will see how we could able to achieve this operation in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 3. Building Code to access Local LLMs via Ollama using API Endpoints

1
00:00:00,120 --> 00:00:00,680
All right.

2
00:00:00,680 --> 00:00:06,200
So now that we have seen how we can call the local large language model using this particular endpoint,

3
00:00:06,200 --> 00:00:08,480
and we get the response that we're looking for.

4
00:00:08,800 --> 00:00:14,400
Now we're going to do the exact similar operation and see how we can able to achieve this.

5
00:00:14,440 --> 00:00:17,200
Just note closely over here on the response.

6
00:00:17,200 --> 00:00:23,440
You can see that the moment we ask this question or the prompt over here to write the code for this

7
00:00:23,440 --> 00:00:28,760
particular website, which is google.com, in here you see that we are getting the response with the

8
00:00:29,440 --> 00:00:32,440
the model created at response.

9
00:00:32,440 --> 00:00:37,680
And then you will see there is a dun dun reason contexts over here.

10
00:00:37,880 --> 00:00:44,400
And then we have total duration load duration, prompt valve count, prompt eval duration, eval count

11
00:00:44,400 --> 00:00:45,640
and eval duration.

12
00:00:45,840 --> 00:00:51,160
So these are the response that we are actually getting out from the large language model itself.

13
00:00:51,200 --> 00:00:53,760
The one that we are looking for are not these.

14
00:00:53,760 --> 00:00:56,200
Rather we are looking for the response from here.

15
00:00:56,200 --> 00:01:02,720
This is exactly what we need to get out from this particular response of a local large language model.

16
00:01:03,120 --> 00:01:04,840
And that is exactly going to be similar.

17
00:01:04,840 --> 00:01:10,160
While we even try to do with the OpenAI model as well, which we will discussing pretty soon once we

18
00:01:10,160 --> 00:01:10,840
get there.

19
00:01:10,840 --> 00:01:16,920
But for now, just focus on how this response is coming up from this particular model while we try to

20
00:01:16,960 --> 00:01:18,120
call from the API.

21
00:01:18,320 --> 00:01:23,720
So we are going to see how we can get this response that we are getting out from the large language

22
00:01:23,720 --> 00:01:26,000
model with our C sharp dotnet code.

23
00:01:26,040 --> 00:01:28,160
So let's see how we can able to achieve that.

24
00:01:28,280 --> 00:01:32,000
So in order to do that, you remember the class that we created in our last lecture.

25
00:01:32,040 --> 00:01:34,920
We're going to do the exact similar operation over here.

26
00:01:34,920 --> 00:01:37,880
And we then start writing the code itself.

27
00:01:38,200 --> 00:01:42,120
So in order to do that, I'm going to create a method over here.

28
00:01:42,360 --> 00:01:46,280
And I'm going to call this as public async of task.

29
00:01:46,280 --> 00:01:49,880
So basically I'm going to write everything in an asynchronous fashion this time.

30
00:01:49,880 --> 00:01:58,120
Because the way you start writing code as asynchronous, you are going to see a lot of benefit, especially

31
00:01:58,320 --> 00:02:02,960
while you are going to be aligning the code with your playwright code.

32
00:02:03,000 --> 00:02:07,650
Maybe in future if you're going to be dealing with the playwright code, which we are going to do in

33
00:02:07,650 --> 00:02:08,610
this course anyway.

34
00:02:08,610 --> 00:02:12,850
So that's why I am writing everything as an asynchronous code.

35
00:02:12,850 --> 00:02:16,610
So you see that I have written an asynchronous method over here.

36
00:02:16,770 --> 00:02:20,490
And now I'm going to start doing things from here itself.

37
00:02:20,730 --> 00:02:27,010
So what I'm going to do in here, if you remember in this particular code I have passed the the body

38
00:02:27,050 --> 00:02:28,290
over here as this.

39
00:02:28,290 --> 00:02:31,090
So I'm going to do the exact similar thing in C sharp dotnet.

40
00:02:31,330 --> 00:02:35,090
The way you can do it is just say var request body.

41
00:02:35,490 --> 00:02:39,930
And in the request body I'm just going to create an anonymous class as new.

42
00:02:39,930 --> 00:02:42,730
So this is an anonymous type as you can see over here.

43
00:02:43,050 --> 00:02:46,690
And I am going to pass the model name.

44
00:02:46,850 --> 00:02:50,330
So the model name is going to be the same thing that we have got.

45
00:02:50,330 --> 00:02:55,050
So I'm just going to say quarter 3.3 billion parameters is this one.

46
00:02:55,370 --> 00:03:01,330
And I'm going to pass the uh the prompt which is going to be the prompt we are going to get from the

47
00:03:01,330 --> 00:03:01,930
method.

48
00:03:02,290 --> 00:03:07,010
And then we are going to uh, stream as false over there.

49
00:03:07,010 --> 00:03:09,730
So I'm just going to say stream as false.

50
00:03:10,210 --> 00:03:14,490
And finally we are going to pass some option if you really wanted to.

51
00:03:14,530 --> 00:03:17,610
So this is going to set the temperatures if you really wanted to as well.

52
00:03:17,610 --> 00:03:24,810
So we can just say the temperature is equal to something like 0.1 or something like that.

53
00:03:24,810 --> 00:03:27,450
So you can set whatever that you wanted to write.

54
00:03:27,450 --> 00:03:30,450
So once you set all of these, you are pretty much good to go.

55
00:03:30,450 --> 00:03:36,250
And then you are you can pass this entire operation to your large language model.

56
00:03:36,250 --> 00:03:38,650
So this is the body that we have got over here.

57
00:03:38,650 --> 00:03:42,410
This is the same body that I'm passing in this time over here.

58
00:03:42,690 --> 00:03:48,690
And once I pass it, I then need to serialize this to a, uh, like a string.

59
00:03:48,810 --> 00:03:50,530
If not, this is not going to work.

60
00:03:50,530 --> 00:03:54,010
So in order to do that, I'm just going to say var JSON.

61
00:03:54,010 --> 00:04:00,610
And then I'm going to use a uh, JSON serializer which is from the system dot txt over here.

62
00:04:00,970 --> 00:04:06,410
And I'm going to call the serialize method with the request body that I have got, which is this one.

63
00:04:06,410 --> 00:04:10,540
And finally I'm going to pass this to an HTTP client.

64
00:04:10,580 --> 00:04:14,780
You remember the one that we were expecting to use for this particular demonstration.

65
00:04:14,780 --> 00:04:16,380
So I'm going to do that as well.

66
00:04:16,380 --> 00:04:21,980
So HTTP client is something that you'll always get as a part of any of the dotnet code.

67
00:04:22,020 --> 00:04:25,700
So you are going to create an HTTP client over here.

68
00:04:25,860 --> 00:04:30,460
And because I wanted to make use of the HTTP client even further methods later on.

69
00:04:30,460 --> 00:04:38,060
So I'm just going to create a private read only HTTP client over here.

70
00:04:38,060 --> 00:04:39,740
So I'm just going to say HTTP client.

71
00:04:39,980 --> 00:04:43,300
So I can just use the same HTTP client here as well.

72
00:04:43,340 --> 00:04:44,980
So I'm going to say HTTP client.

73
00:04:44,980 --> 00:04:48,900
And because remember we are doing a post operation which is this one.

74
00:04:48,900 --> 00:04:56,060
As you can see over here for this particular API call I'm going to call the post async operation over

75
00:04:56,060 --> 00:04:56,260
here.

76
00:04:56,260 --> 00:05:02,220
So this way it's going to do a post operation for me for the call which I am going to make.

77
00:05:02,220 --> 00:05:03,780
So it's going to be post async.

78
00:05:04,180 --> 00:05:09,980
And finally we need to get the local large language models base URL.

79
00:05:10,020 --> 00:05:11,580
Remember this is the same thing.

80
00:05:11,580 --> 00:05:17,100
I'm just going to copy that, paste it over here, and then you can see that we need to pass an HTTP

81
00:05:17,100 --> 00:05:19,900
content over here for the post operation.

82
00:05:19,900 --> 00:05:27,060
So because the next parameter expects us to pass HTTP content, this particular JSON, we cannot directly

83
00:05:27,060 --> 00:05:28,060
pass over here.

84
00:05:28,060 --> 00:05:29,060
Let's say like this.

85
00:05:29,060 --> 00:05:32,380
So if I try to pass this this code is not going to really work.

86
00:05:32,620 --> 00:05:38,260
So in order to make this code to really work, we are going to create a content over here.

87
00:05:38,260 --> 00:05:39,380
And the content is nothing.

88
00:05:39,380 --> 00:05:45,700
But I'm going to create something called as string content because this will return you an HTTP content

89
00:05:45,700 --> 00:05:47,100
return type over there.

90
00:05:47,100 --> 00:05:51,300
So I'm going to call this one and I'm going to pass a JSON.

91
00:05:51,620 --> 00:05:55,300
And I'm going to create an encoding as UTF eight.

92
00:05:55,620 --> 00:06:02,140
And I'm going to make this as application JSON because that is what I'm trying to pass it over here.

93
00:06:02,540 --> 00:06:05,700
So this is something that we need to follow for the HTTP client.

94
00:06:05,740 --> 00:06:10,540
This is not kind of new or anything like that, but I'm just doing it because this is what is the requirement

95
00:06:10,540 --> 00:06:15,390
that we have to Ensure that we need to pass in while we try to do it.

96
00:06:15,430 --> 00:06:21,830
If you are familiar with, let's say, Rest Sharp or even playwright, you can also do that as well.

97
00:06:21,870 --> 00:06:23,350
Instead of the HTTP client.

98
00:06:23,350 --> 00:06:27,070
But I stick with HTTP client because this is very, very straightforward library.

99
00:06:27,270 --> 00:06:29,630
That is why I'm using this one over here.

100
00:06:29,910 --> 00:06:34,230
And once I do that over here now I will get a response.

101
00:06:34,230 --> 00:06:39,390
So I can even verify the response whether it is going to be working or not using the ensure status code

102
00:06:39,550 --> 00:06:40,110
method.

103
00:06:40,310 --> 00:06:48,150
And finally, I can read the content and return that particular value as a JSON element.

104
00:06:48,270 --> 00:06:56,670
So I'm just going to show you how this is going to look like by just saying, uh, return var of the

105
00:06:57,150 --> 00:06:59,150
response text or something like that.

106
00:06:59,150 --> 00:07:03,510
And then I'm going to say await of the response dot.

107
00:07:03,670 --> 00:07:05,350
There is something called as content.

108
00:07:05,350 --> 00:07:12,510
And then you can use this read as string async method, which is going to basically return you the string

109
00:07:12,510 --> 00:07:13,750
of that particular text.

110
00:07:13,950 --> 00:07:16,470
So I'm just going to hold this for now.

111
00:07:16,510 --> 00:07:22,070
Maybe I can even return this one so I can just say return the response text over here so that this method

112
00:07:22,070 --> 00:07:23,150
will be fully done.

113
00:07:23,310 --> 00:07:27,230
So now we will see whether this method is really going to work or not.

114
00:07:27,510 --> 00:07:32,590
So in order to do that, I'm going to go to our test over here somewhere like this.

115
00:07:32,590 --> 00:07:39,470
And I'm just going to create a simple test to see if the large language model can be the methods can

116
00:07:39,470 --> 00:07:40,350
be called or not.

117
00:07:40,350 --> 00:07:45,710
So I'm going to say calling or LMS client something like that.

118
00:07:45,710 --> 00:07:56,550
And I'm going to create a a client something like this as client is equal to new LM client.

119
00:07:56,830 --> 00:08:00,710
And then I'm going to call the call local LM.

120
00:08:00,870 --> 00:08:03,990
And here I'm going to pass the prompt that we just passed.

121
00:08:04,030 --> 00:08:04,870
Just this guy.

122
00:08:05,230 --> 00:08:05,550
Right.

123
00:08:05,550 --> 00:08:08,190
So I'm going to do the exact same thing over here.

124
00:08:08,670 --> 00:08:12,150
And we will see if we could able to get the response.

125
00:08:12,150 --> 00:08:17,190
And because this is an async method, you need to call an async of task in your test code.

126
00:08:17,190 --> 00:08:19,110
If not, it is not going to work.

127
00:08:19,390 --> 00:08:26,910
So I'm going to use the await keyword and I'm gonna say result because I want to see what is the result

128
00:08:26,910 --> 00:08:27,870
of this call.

129
00:08:27,870 --> 00:08:34,310
Local method I want to really print this kind of operation that we are getting as a string there.

130
00:08:34,630 --> 00:08:41,950
And I can just say console, dot, write, line, or maybe write whatever.

131
00:08:42,150 --> 00:08:43,870
And then I'm going to put a result there.

132
00:08:43,870 --> 00:08:47,310
So I'm going to save this and I'm going to put a breakpoint here.

133
00:08:47,310 --> 00:08:50,870
And let's try to debug this code and see if that really works or not.

134
00:08:51,190 --> 00:08:58,870
Uh, so if we just go to the call local method as well, and I'm going to put a breakpoint here and

135
00:08:58,870 --> 00:09:01,270
I'm going to resume the execution.

136
00:09:01,270 --> 00:09:06,790
So you'll notice that now this time it is going to go to the local large language model.

137
00:09:06,790 --> 00:09:11,790
Because we have did the post operation in this particular operation over here.

138
00:09:12,030 --> 00:09:17,030
So we should hopefully see that this code should be executed for us.

139
00:09:17,430 --> 00:09:20,280
Uh, and let's wait for the execution to happen.

140
00:09:20,480 --> 00:09:25,320
And oops, I think we I forgot to do one more thing while I was trying to do that, because we're getting

141
00:09:25,320 --> 00:09:30,720
an object reference exception, uh, for the HTTP client, because as you see, I have just created

142
00:09:30,720 --> 00:09:33,840
the HTTP client, but I have really not initialized that so far.

143
00:09:34,200 --> 00:09:37,320
Uh, which I would was expecting to do it on the constructor.

144
00:09:37,320 --> 00:09:39,160
And I completely missed that part.

145
00:09:39,160 --> 00:09:40,720
So let's try to do that.

146
00:09:40,720 --> 00:09:42,920
If not, this code is just going to fail.

147
00:09:42,920 --> 00:09:46,680
So I was just saying that new of the HTTP client.

148
00:09:46,680 --> 00:09:47,000
Yes.

149
00:09:47,000 --> 00:09:50,080
That is something that I need to do and I completely missed that part.

150
00:09:50,080 --> 00:09:53,600
I apologize for that and let me try to debug it one more time.

151
00:09:53,640 --> 00:09:55,440
And hopefully this time it is going to work.

152
00:09:55,720 --> 00:09:58,920
Uh, and let me try to resume the execution.

153
00:09:59,440 --> 00:10:06,040
And now if you just go to this particular code, we should see the code execution to happen.

154
00:10:06,040 --> 00:10:06,720
And there we go.

155
00:10:06,760 --> 00:10:08,920
You see that we got a response over here.

156
00:10:08,920 --> 00:10:14,840
And this response actually has got response from the large language model.

157
00:10:15,080 --> 00:10:20,880
And if you just want to see what is the content over there, you see that we have got the entire content,

158
00:10:20,880 --> 00:10:21,760
which is fine.

159
00:10:21,760 --> 00:10:24,960
We are going to see what content is going to be over here.

160
00:10:24,960 --> 00:10:29,480
So if I'm going to do a read as string async, we should get an entire response.

161
00:10:29,480 --> 00:10:30,240
Look at that.

162
00:10:30,280 --> 00:10:32,720
See, we get the entire response this time.

163
00:10:32,960 --> 00:10:36,360
This is the same response that we were getting in the postman.

164
00:10:36,360 --> 00:10:39,720
If you remember this one, the model created that response.

165
00:10:39,720 --> 00:10:42,560
The same thing we were actually getting over here as well.

166
00:10:42,800 --> 00:10:49,320
Uh, if you just look closely the same thing and here is the response coming out for us over here,

167
00:10:49,920 --> 00:10:50,920
which is great.

168
00:10:50,920 --> 00:10:57,200
So we are already seeing that we could able to talk to the large language model using this simple code

169
00:10:57,200 --> 00:10:59,360
that we have written, which is pretty amazing.

170
00:10:59,360 --> 00:11:02,600
So this is already working for us, which is pretty cool.

171
00:11:02,600 --> 00:11:07,520
So now that we have did this entire thing and it is working fine for us, the last operation that I

172
00:11:07,520 --> 00:11:14,920
wanted to make sure that I do it before I complete this particular lecture, is to read just the specific

173
00:11:14,920 --> 00:11:21,200
operation, which is nothing but the response from this particular response that we are getting in,

174
00:11:21,200 --> 00:11:26,570
because now we're getting the entire response like the model created at response over here.

175
00:11:26,570 --> 00:11:28,490
I want to just get the response.

176
00:11:28,890 --> 00:11:35,130
And you can actually do that very, very simply in C sharp because you can just say var of the JSON

177
00:11:35,130 --> 00:11:37,490
response over here, something like this.

178
00:11:37,770 --> 00:11:42,210
And then you can just use the class called as JSON serializer.

179
00:11:42,410 --> 00:11:50,850
And you can deserialize this particular object using a JSON element class which is also part of the

180
00:11:51,010 --> 00:11:52,290
system dot txt.

181
00:11:52,290 --> 00:11:55,170
And then you can pass the response text over there.

182
00:11:55,410 --> 00:11:59,410
This will actually pass the entire response over there.

183
00:11:59,650 --> 00:12:03,610
And with this you can get a specific response if you wanted to.

184
00:12:03,650 --> 00:12:10,010
For example, you can just say return the JSON response and get the property.

185
00:12:10,050 --> 00:12:13,930
So this property method will actually choose which property that you wanted to choose.

186
00:12:14,250 --> 00:12:19,330
And because you are going to get a different properties over here and one of the property is nothing

187
00:12:19,330 --> 00:12:22,690
but the response property from this particular thing.

188
00:12:22,690 --> 00:12:24,210
You can also get that.

189
00:12:24,210 --> 00:12:29,410
And there is a method called as get string, which can actually get the string.

190
00:12:29,450 --> 00:12:33,530
If you're not really getting that response string, then return the empty over there.

191
00:12:33,810 --> 00:12:35,450
See, this is pretty cool.

192
00:12:35,770 --> 00:12:38,730
Let me try to run this code and show you what this really does.

193
00:12:38,770 --> 00:12:45,170
So if I'm going to go here and debug this particular code, I know I'm running this quite faster this

194
00:12:45,170 --> 00:12:51,770
time, but you will eventually understand how easy it is while you try to run the code every single

195
00:12:51,770 --> 00:12:52,290
time.

196
00:12:52,450 --> 00:12:57,530
And then once you start debugging this code, you will start to get this more and more familiar.

197
00:12:57,570 --> 00:12:57,930
See that?

198
00:12:57,930 --> 00:12:59,490
Now the code has reached here.

199
00:12:59,770 --> 00:13:02,050
And if I'm going to go look at that.

200
00:13:02,050 --> 00:13:06,890
So we have got the entire response like the one that we saw in the postman.

201
00:13:07,250 --> 00:13:15,170
And now if I try to deserialize this with JSON element, you will notice that we have got this entire

202
00:13:15,170 --> 00:13:22,690
response as the JSON elements, where you will see all of these operations will now be holding like

203
00:13:22,730 --> 00:13:27,220
a value keys for the model created at and the response.

204
00:13:27,220 --> 00:13:33,140
And if I want to just get this particular response, I can just do this JSON dot getproperty of response

205
00:13:33,420 --> 00:13:36,940
and get string, which will get me just that particular response.

206
00:13:36,940 --> 00:13:42,340
If I want to go and inspect or evaluate this expression, something like this.

207
00:13:42,380 --> 00:13:47,900
See, you just get that response alone instead of getting the full operation.

208
00:13:47,900 --> 00:13:48,700
Look at that now.

209
00:13:48,700 --> 00:13:50,980
It is so much formatted code.

210
00:13:51,020 --> 00:13:53,060
It's on the markdown file that we have got.

211
00:13:53,460 --> 00:13:59,180
And now I'm going to see what is the output of this particular method over here.

212
00:13:59,220 --> 00:13:59,980
Look at that.

213
00:13:59,980 --> 00:14:02,140
We have just got the response alone.

214
00:14:02,180 --> 00:14:04,020
This was our quest to get it.

215
00:14:04,020 --> 00:14:07,540
And now we have got that already which is pretty cool.

216
00:14:07,540 --> 00:14:15,820
So this is how you can actually get the response from the local large language model using C-sharp dotnet

217
00:14:15,820 --> 00:14:18,220
code with the HTTP client.

218
00:14:18,220 --> 00:14:22,020
That is what we have done all these time so far over here.

219
00:14:22,140 --> 00:14:28,860
It is so much easier and we are going to do the exact similar operation for the OpenAI as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 4. Accessing Cloud LLMs (OpenAI GPT Models) with APIs

1
00:00:00,120 --> 00:00:06,520
So now that hopefully you have got the idea of how this code has been written, I know it's not easy

2
00:00:06,520 --> 00:00:11,040
if you're writing this code or similar kind of code for the very first time.

3
00:00:11,640 --> 00:00:17,560
But if you have really worked with the API testing with Rest Sharp, you know this is the same exact

4
00:00:17,560 --> 00:00:24,040
kind of code which you do it, you do a post operation, you also create a body, uh, which is going

5
00:00:24,040 --> 00:00:29,080
to be holding the body that you're passing in, and then you're going to get the response, which you're

6
00:00:29,080 --> 00:00:34,760
going to do the read as string async or maybe the content, and then you deserialize it based on what

7
00:00:34,760 --> 00:00:35,360
you're looking for.

8
00:00:35,400 --> 00:00:37,480
That is how you usually do it.

9
00:00:37,520 --> 00:00:43,560
If you are using the rest sharp client, you can also deserialize it directly in the post async.

10
00:00:43,560 --> 00:00:47,280
But because we are not using rest sharp, we are just using the HTTP client.

11
00:00:47,320 --> 00:00:52,880
You just have to deserialize it over here for the first time, which is fine because that is also very

12
00:00:52,880 --> 00:00:54,200
straightforward over here.

13
00:00:54,200 --> 00:00:59,950
And once you have understood this particular code that we have got over here now, it is going to be

14
00:00:59,950 --> 00:01:05,830
even more simpler while we try to do that with our open AI client.

15
00:01:05,830 --> 00:01:08,030
So I'm going to show you how we can actually do it.

16
00:01:08,030 --> 00:01:13,790
So the way we're going to do it is we are going to go to the open AI portal over here, and then we

17
00:01:13,830 --> 00:01:16,230
are going to start writing the code again.

18
00:01:16,230 --> 00:01:19,790
You need to have an open AI account to do that.

19
00:01:20,030 --> 00:01:24,710
This is because we are using the paid version of the open AI platform.

20
00:01:24,950 --> 00:01:28,070
So make sure that you have access to it.

21
00:01:28,230 --> 00:01:35,230
And I'm really showing you this because you may be using the GPT models or the cloud model or Gemini

22
00:01:35,270 --> 00:01:37,790
model, or it can be even deep seek model.

23
00:01:37,790 --> 00:01:44,910
You can use any of the model, but the underlying way to access these model remains exactly the same.

24
00:01:44,910 --> 00:01:46,870
Like how I'm going to show you right now.

25
00:01:47,070 --> 00:01:52,350
And because I already have some money in the open AI account, I'm going to show you over here.

26
00:01:52,590 --> 00:01:54,910
Okay, so how did I get to this particular point?

27
00:01:54,910 --> 00:01:58,260
Well, you just have to go to OpenAI.

28
00:01:58,300 --> 00:01:59,100
Com.

29
00:01:59,140 --> 00:02:05,420
This particular website over here, you might have used the ChatGPT before, but now you are a developer

30
00:02:05,420 --> 00:02:11,700
kind of guy who is going to use the API to access the models using OpenAI.

31
00:02:11,860 --> 00:02:20,780
Remember how we actually did access the model using the llama client, which is this one from this particular

32
00:02:20,820 --> 00:02:21,260
UI?

33
00:02:21,740 --> 00:02:28,780
Or you can also access the same using the API, like how we just saw with this code, as well as from

34
00:02:28,780 --> 00:02:32,140
the postman code over here using the API.

35
00:02:32,380 --> 00:02:37,620
The similar thing is going to happen where we are going to access the OpenAI using its API.

36
00:02:37,660 --> 00:02:40,060
So I'll show you how we can able to access it.

37
00:02:40,180 --> 00:02:44,140
So you just have to log in over here like how I have already did.

38
00:02:44,180 --> 00:02:47,940
I'm going to go to the API platform there and it's going to take me there.

39
00:02:47,980 --> 00:02:48,940
See I have already logged in.

40
00:02:48,940 --> 00:02:50,420
That's the reason why I'm getting it.

41
00:02:50,420 --> 00:02:53,660
But if you have really not signed up, you need to sign up for the first time.

42
00:02:53,660 --> 00:02:54,820
It is totally free.

43
00:02:55,020 --> 00:03:01,440
But once you sign up there, you need to pay the money, which you need to go to the settings over there.

44
00:03:01,560 --> 00:03:07,920
You will see that you are going to have, uh, like how much of the billings that you have got currently.

45
00:03:07,920 --> 00:03:12,720
I think I have a credit of 7.33 over here, but you need to recharge it.

46
00:03:12,720 --> 00:03:17,160
So you need to add the credit card balance over here to have money.

47
00:03:17,200 --> 00:03:20,920
I mean, this is the amount that I have topped up in my account.

48
00:03:20,920 --> 00:03:24,880
But if you don't really have topped up, you're just going to see 0.00 there.

49
00:03:24,880 --> 00:03:26,440
So that is how it is going to be.

50
00:03:26,440 --> 00:03:29,400
So make sure that you top up for this particular demonstration.

51
00:03:29,400 --> 00:03:32,800
But if you still think that hey Karthik, I don't even need OpenAI.

52
00:03:32,800 --> 00:03:35,200
I'm just going to work with local large language model.

53
00:03:35,200 --> 00:03:36,360
I'm totally fine with that.

54
00:03:36,360 --> 00:03:42,040
You can completely skip this particular part, but I'm just going to cover this because this local large

55
00:03:42,040 --> 00:03:47,800
language model, even though you are going to be access it within your local machine while you start

56
00:03:47,800 --> 00:03:55,670
deploying the local large language model on the cloud, like the AWS SageMaker or Bedrock, then you

57
00:03:55,670 --> 00:03:57,390
may need to access it from there.

58
00:03:57,390 --> 00:04:02,310
So this part is going to be pretty much related to that part, which I'm talking about.

59
00:04:02,310 --> 00:04:04,550
So that's why I'm going to still cover it over here.

60
00:04:04,550 --> 00:04:10,870
So it's totally fine for you to whether to watch this lecture or not, but I will be happy for you to

61
00:04:10,910 --> 00:04:14,070
watch it for the first time because it is super important.

62
00:04:14,310 --> 00:04:18,950
Well, as I said, I already have the money over there and I'm going to access this particular API.

63
00:04:19,190 --> 00:04:21,670
So how do we access this particular API there?

64
00:04:21,670 --> 00:04:28,110
Well, you need to first of all create an API key over here, which you can just go create a new secret

65
00:04:28,150 --> 00:04:28,470
key.

66
00:04:28,630 --> 00:04:34,070
And then I'm going to say uh, the course API key, uh, something like that.

67
00:04:34,070 --> 00:04:36,390
And I'm going to select the default project.

68
00:04:36,390 --> 00:04:39,470
And I'm going to create a uh API key.

69
00:04:39,470 --> 00:04:41,950
So that's going to create an API key for me.

70
00:04:42,110 --> 00:04:47,230
And I can just go over here uh, and have that API key somewhere.

71
00:04:47,230 --> 00:04:51,270
So I'm going to put an API key um somewhere here.

72
00:04:51,270 --> 00:05:02,300
So I'm going to say uh, Private read only, uh, string of the open AI API key.

73
00:05:02,340 --> 00:05:02,900
This is something.

74
00:05:02,900 --> 00:05:07,780
I'm just putting it over here, but we are going to be replacing that quite sooner the moment we are

75
00:05:07,780 --> 00:05:09,260
going to introduce configuration.

76
00:05:09,260 --> 00:05:13,260
So all of these hard coded values will be replaced with the configurations later.

77
00:05:13,260 --> 00:05:15,740
But for now I'm just going to hard code it over here.

78
00:05:15,780 --> 00:05:16,340
Right.

79
00:05:16,380 --> 00:05:19,740
And once I have this particular key uh, just done.

80
00:05:19,860 --> 00:05:23,500
And then we are going to access this particular open AI as well.

81
00:05:23,500 --> 00:05:25,780
So how do we actually access the open AI.

82
00:05:26,020 --> 00:05:26,500
Guess what.

83
00:05:26,500 --> 00:05:27,700
It's very straightforward.

84
00:05:27,900 --> 00:05:34,140
All you have to do it uh, is you just go to the API reference, uh, over here, this particular page,

85
00:05:34,620 --> 00:05:38,580
uh, you see that they will give you an idea of how you can access them.

86
00:05:38,580 --> 00:05:46,460
You just have to use this particular URL like, uh, open AI uh, dot com slash v1 slash model, which

87
00:05:46,460 --> 00:05:48,500
will give you the models which are available.

88
00:05:48,500 --> 00:05:51,060
And there is something called as chat completion as well.

89
00:05:51,060 --> 00:05:54,050
So if I'm just going to go and search for the chat completion, look at that.

90
00:05:54,050 --> 00:05:58,490
So this is going to be the one that we are going to be using this particular endpoint, which is going

91
00:05:58,530 --> 00:06:00,410
to perform the chat completion for us.

92
00:06:00,410 --> 00:06:05,930
And this is something which you can use to perform the operation that we are going to be using.

93
00:06:05,930 --> 00:06:09,370
So that is the endpoint that we are going to use to see how that works.

94
00:06:09,370 --> 00:06:12,530
So I'll quickly show you how we can do that with the postman.

95
00:06:12,530 --> 00:06:15,290
And then we will see how we could able to achieve it.

96
00:06:15,290 --> 00:06:23,930
So in order to do that I'm just going to say http colon double slash uh over here and I'm going to say

97
00:06:24,090 --> 00:06:26,410
API dot open

98
00:06:27,010 --> 00:06:34,050
api.com/v1/chat/completion.

99
00:06:34,050 --> 00:06:38,170
So this is going to be the key that we are going to be using over here.

100
00:06:38,490 --> 00:06:41,210
So this is going to be the endpoint that we are going to be using over here.

101
00:06:41,570 --> 00:06:44,290
And I need to pass the authorization.

102
00:06:44,290 --> 00:06:47,490
You remember the the token that we have actually passed in.

103
00:06:47,490 --> 00:06:48,970
So I'm going to pass that as well.

104
00:06:49,130 --> 00:06:55,920
So I'm going to say authorization, and it's going to be basically a bearer token with the token that

105
00:06:55,920 --> 00:06:57,200
I have got over here.

106
00:06:57,200 --> 00:06:58,560
So I'm going to pass that.

107
00:06:58,840 --> 00:07:07,200
And in the body I'm actually going to do a pass the similar body that we were trying to pass for the

108
00:07:07,200 --> 00:07:08,720
local large language models.

109
00:07:08,720 --> 00:07:12,320
Do you remember the same thing I'm going to do over here as well?

110
00:07:12,440 --> 00:07:19,400
Let's say I'm going to use the model as maybe the GPT four or mini model that I wanted to.

111
00:07:19,440 --> 00:07:22,280
And then I need to pass the prompt over here.

112
00:07:22,280 --> 00:07:28,880
And the way I can pass the prompt over here is using what is called as messages.

113
00:07:28,880 --> 00:07:32,160
So this is how you actually pass the message over here.

114
00:07:32,200 --> 00:07:36,520
This is how the prompts are basically passed over here.

115
00:07:36,640 --> 00:07:38,880
And then I'm going to say an array.

116
00:07:38,880 --> 00:07:45,160
Because somehow this is going to be an array because it says messages over here and over here, I'm

117
00:07:45,160 --> 00:07:48,360
just going to pass the role.

118
00:07:48,360 --> 00:07:53,940
And here we need to pass the role as the user, because this is a user who is going to be prompting.

119
00:07:54,140 --> 00:07:57,980
So that is what that is how it is done in the OpenAI way.

120
00:07:58,260 --> 00:08:00,140
So that's what I'm trying to do over here.

121
00:08:00,340 --> 00:08:02,940
Uh, and I need to pass the thing over there.

122
00:08:02,940 --> 00:08:03,220
So.

123
00:08:03,220 --> 00:08:03,740
Right.

124
00:08:04,100 --> 00:08:05,500
Uh, a selenium.

125
00:08:07,540 --> 00:08:13,540
Uh, with C-sharp dotnet code for google.com, just for search.

126
00:08:13,740 --> 00:08:14,420
That's it.

127
00:08:14,620 --> 00:08:16,940
And now I'm going to perform a send operation.

128
00:08:16,940 --> 00:08:19,420
So this is the only thing that is changing over there.

129
00:08:19,420 --> 00:08:22,700
Because in local large language model we just pass the prompt directly.

130
00:08:22,700 --> 00:08:25,700
But over here I'm just going to pass it something like this.

131
00:08:26,100 --> 00:08:29,340
And now I'm going to do a send operation over here.

132
00:08:29,540 --> 00:08:36,260
So you will see that the moment I try to send this particular operation over here, it says an error

133
00:08:36,260 --> 00:08:40,220
because I have just forgot to change it to a post.

134
00:08:40,220 --> 00:08:41,980
And now I'm going to send it again.

135
00:08:42,220 --> 00:08:47,970
And now this time it is actually going to the OpenAI to get the response over there.

136
00:08:48,010 --> 00:08:53,930
So it's taking a bit of a time because it definitely have to pass it to the model and then get the response

137
00:08:53,930 --> 00:08:55,170
and look at that.

138
00:08:55,450 --> 00:09:01,730
We are getting the response this time from the OpenAI's GPT four mini model.

139
00:09:02,370 --> 00:09:03,250
Look at that.

140
00:09:03,290 --> 00:09:09,770
It has got pretty much exactly the similar kind of content as well over here, just that it has got

141
00:09:09,770 --> 00:09:11,810
a different response object.

142
00:09:11,850 --> 00:09:19,530
See, it has got an ID object created at model choices, and within the choice it has got uh, the index

143
00:09:19,530 --> 00:09:20,090
as zero.

144
00:09:20,090 --> 00:09:22,050
And there is a message over there.

145
00:09:22,250 --> 00:09:24,850
This is what is the response that we are looking for.

146
00:09:25,130 --> 00:09:27,290
The content within the message.

147
00:09:27,770 --> 00:09:29,370
That's what we need.

148
00:09:29,370 --> 00:09:33,530
So unfortunately we have to go a bit deep to get this particular response.

149
00:09:33,530 --> 00:09:34,650
But hey there we go.

150
00:09:34,690 --> 00:09:37,770
We already got the response, this time from the OpenAI model.

151
00:09:38,170 --> 00:09:42,210
Now the question is how can we get this response from the C.

152
00:09:42,730 --> 00:09:43,410
Net code?

153
00:09:43,850 --> 00:09:46,610
We are going to do that in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 5. Building Code to access Cloud LLMs via OpenAI using API Endp
oints

1
00:00:00,120 --> 00:00:06,520
All right, so hope you have tried doing all of these yourself before you start this big journey of

2
00:00:06,520 --> 00:00:13,520
how you can write the C dotnet code to perform the similar operation, like how we did for the local

3
00:00:13,520 --> 00:00:14,680
large language model.

4
00:00:14,960 --> 00:00:19,960
I highly recommend you to do it manually before you start writing the code, because that is going to

5
00:00:19,960 --> 00:00:22,760
give you an idea of how these things are really working.

6
00:00:22,800 --> 00:00:29,760
And again, as I told you in our last lecture, using OpenAI model for your test is completely optional.

7
00:00:29,760 --> 00:00:31,120
You can use it.

8
00:00:31,120 --> 00:00:33,600
Or if you don't want, you can just ignore it completely.

9
00:00:33,600 --> 00:00:40,320
But I recommend you to do it because you may need to access these kinds of model later from your, uh,

10
00:00:40,320 --> 00:00:46,000
from your Azure, uh, or your AWS bedrock or SageMaker.

11
00:00:46,000 --> 00:00:50,400
So in those times, you may need to write the code like how I am doing it over here.

12
00:00:50,400 --> 00:00:52,760
That's how I'm just trying to replicate this time.

13
00:00:53,320 --> 00:00:58,360
Well that's great, but you may have a question here saying, hey Karthik, you know what?

14
00:00:58,400 --> 00:01:02,920
Last time while we tried doing with the local large language model, the response did not had so much

15
00:01:02,920 --> 00:01:03,760
of complexity.

16
00:01:03,890 --> 00:01:09,330
We got the response, which was the output of the large language model using this response property

17
00:01:09,530 --> 00:01:16,290
of this particular response object over here, even though it's bigger, the the, the way that we got

18
00:01:16,290 --> 00:01:18,330
this particular response was straightforward.

19
00:01:18,330 --> 00:01:21,330
We just used this get property of response.

20
00:01:21,570 --> 00:01:22,130
There we go.

21
00:01:22,130 --> 00:01:23,170
And we got it.

22
00:01:23,170 --> 00:01:28,810
But now how can I do the exact similar thing for the, uh, OpenAI model?

23
00:01:28,850 --> 00:01:34,810
Because we also need to pass like the header with the authorization and the body, we have to pass it

24
00:01:34,810 --> 00:01:35,770
a different way.

25
00:01:35,770 --> 00:01:41,570
At the same time, we we are getting this particular message content, uh, very deep inside, like

26
00:01:41,610 --> 00:01:42,250
choice.

27
00:01:42,490 --> 00:01:47,250
Then we need to get an array of the message, and then we need to get the content inside it.

28
00:01:47,250 --> 00:01:48,890
So choice message content.

29
00:01:48,890 --> 00:01:52,250
So we need to go three levels deep to get this particular content.

30
00:01:52,250 --> 00:01:54,050
So how can I write this particular code.

31
00:01:54,090 --> 00:01:56,770
I can actually give you a trick of how you can do it.

32
00:01:56,770 --> 00:01:58,130
But just stick with me.

33
00:01:58,170 --> 00:02:02,450
Before we get there, let's start to write the code in first place.

34
00:02:02,690 --> 00:02:07,740
So what I'm going to do is I'm going to copy this entire code that we have written before, And I'm

35
00:02:07,740 --> 00:02:13,180
going to paste that over here because the coding is going to be pretty much exactly the similar for

36
00:02:13,180 --> 00:02:20,940
the OpenAI as well, just that I'm going to name this as call, uh, OpenAI, uh, async, something

37
00:02:20,940 --> 00:02:21,500
like that.

38
00:02:21,500 --> 00:02:24,300
And the request body has changed a bit as well.

39
00:02:24,300 --> 00:02:30,020
So the model which we are using, uh, is basically, uh, this guy, the GPT four or mini model.

40
00:02:30,060 --> 00:02:33,820
So we are going to move all of these, uh, in the configuration later.

41
00:02:34,060 --> 00:02:36,340
But for now, just hard code all of these.

42
00:02:36,900 --> 00:02:40,740
And then we have got the message instead of the prompt.

43
00:02:40,740 --> 00:02:45,980
So I'm just going to say uh, messages as an array.

44
00:02:45,980 --> 00:02:47,860
So I'm going to say a new array.

45
00:02:47,900 --> 00:02:49,700
This is how you write in the C sharp world.

46
00:02:50,020 --> 00:02:55,900
And then you say new uh of role is equal to user.

47
00:02:56,220 --> 00:03:01,460
And then you have something called as content, which is going to be the prompt that you are passing

48
00:03:01,460 --> 00:03:01,860
in.

49
00:03:01,860 --> 00:03:03,420
That's going to be your message.

50
00:03:03,900 --> 00:03:07,940
And you can pass the temperature, uh, if you want as well.

51
00:03:08,100 --> 00:03:16,800
So I'm going to say the temperature as probably 0.1, like how we passed over there, 0.1.

52
00:03:17,120 --> 00:03:22,960
And you can also configure the, um, the max token if you really wanted to, but I'm just going to

53
00:03:23,000 --> 00:03:24,040
ignore it for now.

54
00:03:24,360 --> 00:03:26,640
Uh, so just put a comma there.

55
00:03:26,720 --> 00:03:29,000
That's going to be the request body we have got.

56
00:03:29,360 --> 00:03:33,280
And the URL also changes here because that's not the URL that we used.

57
00:03:33,280 --> 00:03:34,880
So I'm going to copy this URL.

58
00:03:35,120 --> 00:03:37,760
And I'm going to paste this particular URL over here.

59
00:03:37,920 --> 00:03:40,680
So these things are going to remain exactly the same.

60
00:03:40,920 --> 00:03:41,440
Right.

61
00:03:41,920 --> 00:03:50,160
And you remember we actually passed what is called as the uh the authorization header as well, which

62
00:03:50,160 --> 00:03:52,720
we need to pass it as well, which is this header.

63
00:03:52,760 --> 00:03:53,960
Remember this one.

64
00:03:54,320 --> 00:03:55,000
We need to do that.

65
00:03:55,000 --> 00:03:59,240
So how can we do that in the C-sharp dotnet HTTP code.

66
00:03:59,280 --> 00:04:00,080
Well guess what.

67
00:04:00,160 --> 00:04:06,760
There is a way you can pass it using what is called as HTTP of default request headers.

68
00:04:07,000 --> 00:04:14,970
Oh this particular uh this particular class uh has got something called as add method, which is where

69
00:04:14,970 --> 00:04:19,890
you can actually add the, uh, the authorization.

70
00:04:19,890 --> 00:04:27,010
So I'm going to say authorize and I'm going to pass the bearer token.

71
00:04:27,010 --> 00:04:29,610
And you remember we were actually passing the bearer token.

72
00:04:29,610 --> 00:04:33,930
We stored the bearer token somewhere on the top of this particular code, just this one.

73
00:04:34,450 --> 00:04:36,690
So I'm going to go grab that.

74
00:04:36,890 --> 00:04:41,490
And I'm just doing a string interpolation here where I can copy paste this particular code.

75
00:04:41,530 --> 00:04:43,770
See that's how the authorization really works.

76
00:04:43,770 --> 00:04:57,530
So this is where you add the authorization header with the open AI key, which is nothing but the API

77
00:04:57,530 --> 00:04:57,890
key.

78
00:04:58,010 --> 00:04:58,370
Right.

79
00:04:58,370 --> 00:05:00,290
That's what we have did over here.

80
00:05:00,450 --> 00:05:03,930
And the rest of the things is just going to remain exactly the same.

81
00:05:03,930 --> 00:05:04,730
And guess what?

82
00:05:04,770 --> 00:05:07,850
In here is where things will get a bit more messy.

83
00:05:07,850 --> 00:05:10,410
So because we're not going to do this way over here, right.

84
00:05:10,410 --> 00:05:13,610
We're going to not get the response, but the property will change.

85
00:05:13,770 --> 00:05:18,500
So how do we deserialize Serialize the response to get this particular content.

86
00:05:18,500 --> 00:05:23,740
So what I'm going to do is I'm going to copy this particular, um, particular response.

87
00:05:23,940 --> 00:05:28,620
And I'm going to go to the alama, which is even the local large language model can do it.

88
00:05:28,620 --> 00:05:39,820
I'm going to say, can you help me deserialize, uh, in HTTP client code or maybe not HTTP client code

89
00:05:39,980 --> 00:05:50,700
in JSON serializer of system dot text class for this response.

90
00:05:51,220 --> 00:05:52,860
And I'm going to put this over here.

91
00:05:53,260 --> 00:06:00,980
I want it to get the the one that we are looking for is this particular, uh, big gigantic content.

92
00:06:00,980 --> 00:06:01,340
Right.

93
00:06:01,340 --> 00:06:11,340
So I'm going to say can you get the content which is inside the I'm going to say inside the choice and

94
00:06:11,340 --> 00:06:19,910
message choice and message C, I'm going to give all the information to the large language model so

95
00:06:19,910 --> 00:06:21,510
that it can write things for me.

96
00:06:22,030 --> 00:06:23,310
And I'm going to hit enter.

97
00:06:23,310 --> 00:06:28,430
So let's wait for the large language model to return me how to deserialize it.

98
00:06:28,590 --> 00:06:32,510
Um, and I think it will deserialize it very fast.

99
00:06:32,510 --> 00:06:33,950
It's not that harder.

100
00:06:33,990 --> 00:06:34,390
There we go.

101
00:06:34,430 --> 00:06:36,430
It has given me the class over here.

102
00:06:36,470 --> 00:06:39,790
Oh, it's writing a choice class as well, which is great.

103
00:06:39,790 --> 00:06:41,230
And writing a message class.

104
00:06:41,550 --> 00:06:49,230
Writing an usage class is writing an entire class for me, which I can do the deserialization, which

105
00:06:49,230 --> 00:06:49,990
is great.

106
00:06:50,350 --> 00:06:56,110
Or we can directly extract the content, uh, from this particular code.

107
00:06:56,150 --> 00:07:01,830
Ah, this code looks pretty neat because I don't even need to create all these classes because it could

108
00:07:01,990 --> 00:07:03,150
eventually change.

109
00:07:03,190 --> 00:07:06,230
Maybe if the OpenAI decided to change it.

110
00:07:06,230 --> 00:07:11,190
So rather I can just do this way because this is quite straightforward.

111
00:07:11,190 --> 00:07:13,150
If I wanted to, uh, do it.

112
00:07:13,150 --> 00:07:20,030
So I'm going to say don't create the class, but just try to get it, uh, using JSON element.

113
00:07:20,070 --> 00:07:20,550
Yeah.

114
00:07:20,910 --> 00:07:28,640
I want to say don't create the class, just use the JSON element to do it.

115
00:07:29,680 --> 00:07:32,880
Which is nothing but the way that we tried doing it last time.

116
00:07:33,000 --> 00:07:36,680
Using the JSON element, you remember we just got the property directly.

117
00:07:36,920 --> 00:07:37,440
The same thing.

118
00:07:37,440 --> 00:07:42,240
I wanted up the large language model to do it as well.

119
00:07:42,560 --> 00:07:48,360
Okay, now it says okay, so you can use JSON element to parse the JSON and extract the content without

120
00:07:48,360 --> 00:07:49,840
defining the classes.

121
00:07:50,120 --> 00:07:51,680
And here is how you do it.

122
00:07:51,720 --> 00:07:56,840
See now it's doing this particular code which is quite awesome.

123
00:07:57,160 --> 00:07:59,280
This is exactly what I was looking for.

124
00:07:59,840 --> 00:08:00,880
Oh look at that.

125
00:08:00,880 --> 00:08:02,200
It's saying enumerate array.

126
00:08:02,480 --> 00:08:04,440
And then it is going to get the property.

127
00:08:04,720 --> 00:08:08,960
Um it's going to get the first value which is going to be the message.

128
00:08:09,120 --> 00:08:10,480
Uh, and then the string.

129
00:08:10,520 --> 00:08:12,760
Um, this is what I really needed.

130
00:08:13,440 --> 00:08:14,280
Fabulous.

131
00:08:14,560 --> 00:08:16,680
Uh, so let's try doing it this time.

132
00:08:16,800 --> 00:08:22,920
So it has got the JSON document dot parse, but I'm going to leave everything there.

133
00:08:22,920 --> 00:08:28,250
But I'm just going to Gonna get this part, which is what I really needed to do it.

134
00:08:28,250 --> 00:08:31,930
So this is the idea that I really wanted to see how this actually works.

135
00:08:31,930 --> 00:08:36,810
So I'm just gonna copy this whole thing and I'm going to go to my code.

136
00:08:37,050 --> 00:08:39,970
So this is going to be the response text over here.

137
00:08:40,330 --> 00:08:46,250
Uh, and in the JSON, I'm just going to say paste this particular code.

138
00:08:46,610 --> 00:08:47,250
Look at that.

139
00:08:47,530 --> 00:08:55,330
So I'm going to say get the property uh for the choice uh and then enumerate the array.

140
00:08:55,690 --> 00:08:59,050
First I'm going to stop this execution I think it's running.

141
00:08:59,370 --> 00:09:01,370
And then it's going to get that particular string.

142
00:09:01,690 --> 00:09:07,130
If it doesn't get the string then just return string dot empty for that matter.

143
00:09:07,690 --> 00:09:08,330
There we go.

144
00:09:08,370 --> 00:09:10,370
I think that's the code that I need to add.

145
00:09:10,610 --> 00:09:11,210
That's it.

146
00:09:11,210 --> 00:09:15,730
You can see that this is the very, very super simple code that I have to paste over here.

147
00:09:15,730 --> 00:09:22,090
I also got the idea from the, uh, local large language model itself, because it gave me how we can

148
00:09:22,090 --> 00:09:23,490
actually do it as well.

149
00:09:23,490 --> 00:09:25,050
So I just copy pasted it.

150
00:09:25,050 --> 00:09:28,710
So get property of choice enumerate array First message content.

151
00:09:28,710 --> 00:09:29,310
And this.

152
00:09:29,470 --> 00:09:29,950
Cool.

153
00:09:30,310 --> 00:09:33,910
And now let me call this method and see how this works.

154
00:09:33,910 --> 00:09:36,310
So I'm going to go to the enhanced test.

155
00:09:37,430 --> 00:09:46,310
And instead of the local elements that I was calling in before I'm going to say result is equal to await

156
00:09:46,590 --> 00:09:50,110
client dot call open async.

157
00:09:50,470 --> 00:09:54,030
And I'm going to do the exact similar prompt.

158
00:09:54,190 --> 00:09:56,990
I'll try to run this code and let's see what's going to happen.

159
00:09:57,870 --> 00:10:02,430
So it's going to get to this point and we're going to run it.

160
00:10:04,830 --> 00:10:07,110
Oops I think I should have put a breakpoint here.

161
00:10:07,470 --> 00:10:09,590
So this time it's actually running on the open AI.

162
00:10:09,630 --> 00:10:13,510
So it's pretty faster as opposed to the local large language model.

163
00:10:14,030 --> 00:10:16,430
Uh and hopefully it just works.

164
00:10:16,430 --> 00:10:17,510
And we got a result.

165
00:10:17,830 --> 00:10:18,630
Look at that.

166
00:10:18,630 --> 00:10:20,230
Here is the result.

167
00:10:20,670 --> 00:10:26,390
Certainly below is the simple example of how to use selenium with C sharp to perform the search operation.

168
00:10:26,510 --> 00:10:31,440
And it has given me all the code Fabulous.

169
00:10:31,880 --> 00:10:37,720
It's already deserialized perfectly like how I was looking for to get directly from the content of the

170
00:10:37,720 --> 00:10:38,440
choices.

171
00:10:39,200 --> 00:10:40,080
Pretty cool.

172
00:10:40,360 --> 00:10:41,200
That worked.

173
00:10:41,640 --> 00:10:48,880
This is how we can actually access the large language model, which is sitting on the OpenAI with the

174
00:10:48,880 --> 00:10:53,080
GPT models way more easily using this particular code.

175
00:10:53,080 --> 00:11:00,280
So now you have got the idea of how you can prompt your local large language model as well as the OpenAI

176
00:11:00,320 --> 00:11:06,120
model and then talk with it, get the response that you're looking for, which is quite amazing.

177
00:11:06,520 --> 00:11:14,840
Now, the last operation that I wanted to do it is I wanted to, uh, move all of these into a configuration

178
00:11:14,840 --> 00:11:20,040
because that is something very, very important, because all of these values are hard coded.

179
00:11:20,040 --> 00:11:25,880
I want them all to be moved to a configuration so that I can access it way more easily, just from the

180
00:11:25,880 --> 00:11:28,200
configuration and change in one single place.

181
00:11:28,200 --> 00:11:34,120
I don't really have to, uh, go and switch this knob by commenting them out.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 6. Creating Configurations to control Models, URLs, Temperatures from one place

1
00:00:00,080 --> 00:00:00,920
All right.

2
00:00:00,920 --> 00:00:07,960
So now we are going to see how we can read the configurations from the JSON file instead of just holding

3
00:00:07,960 --> 00:00:09,360
everything over here.

4
00:00:09,400 --> 00:00:12,840
Remember you can see that we have got so many things hardcoded.

5
00:00:12,880 --> 00:00:15,280
The one is the open API key is hard coded.

6
00:00:15,280 --> 00:00:18,240
And we also have got the models as hardcoded.

7
00:00:18,400 --> 00:00:21,240
We have got the temperatures hardcoded.

8
00:00:21,280 --> 00:00:25,840
We also have got the base URLs hardcoded over here.

9
00:00:26,000 --> 00:00:33,120
And we also have got uh some other details hardcoded for example the max tokens and something like that.

10
00:00:33,120 --> 00:00:37,960
So if you want to hard code any of these over here, it's going to be trouble to be honest, because

11
00:00:37,960 --> 00:00:40,840
we need to manage all of them from one single place.

12
00:00:41,040 --> 00:00:43,400
So how can we get rid of this particular problem?

13
00:00:43,520 --> 00:00:50,480
Well, we need to create a class called as LM config over here where this class is going to represent

14
00:00:50,520 --> 00:00:53,120
what exactly that we are looking for.

15
00:00:53,280 --> 00:00:57,400
So for instance I'm going to be looking for um, the provider.

16
00:00:57,440 --> 00:00:57,680
Right.

17
00:00:57,720 --> 00:01:03,950
The provider is going to be uh, like a local large language model or the OpenAI model.

18
00:01:04,190 --> 00:01:07,230
Whatever that you are going to be using, you can do that as well.

19
00:01:07,350 --> 00:01:14,390
So you can by default set it to local, but you can actually set it to, uh, to OpenAI.

20
00:01:14,630 --> 00:01:15,990
For the OpenAI model.

21
00:01:15,990 --> 00:01:20,350
Or you can just say local uh, for the local large language model.

22
00:01:20,590 --> 00:01:22,470
That's the provider that we're talking about.

23
00:01:22,590 --> 00:01:26,790
And similarly, uh, you can set the API key.

24
00:01:26,830 --> 00:01:32,750
If you really wanted to I mean, the API key is going to be there for the OpenAI model.

25
00:01:32,830 --> 00:01:39,430
But for the normal local large language model, it is just going to be an empty over there.

26
00:01:39,750 --> 00:01:46,670
And similarly, you can also set uh, the base URL over here, which is going to be string as well.

27
00:01:46,750 --> 00:01:53,790
Uh, so you can just say base URL, uh, and then the base URL string for the local large language model

28
00:01:53,790 --> 00:01:56,950
is going to be obviously, uh, you know what it is.

29
00:01:56,990 --> 00:01:58,590
Let me just go copy that.

30
00:01:58,630 --> 00:02:00,830
Which is going to be this one.

31
00:02:00,870 --> 00:02:02,750
This is the base URL that we have got.

32
00:02:02,750 --> 00:02:06,950
So I'm going to go copy that over here and I'm going to paste it.

33
00:02:07,150 --> 00:02:10,390
But it's going to change for the OpenAI model.

34
00:02:10,790 --> 00:02:17,750
And similarly you can set the models as well uh, over here uh, which is also going to be kind of interesting.

35
00:02:18,030 --> 00:02:19,750
So I'm going to do that.

36
00:02:19,750 --> 00:02:24,110
And because I've already written that particular code, I'm just going to paste it to save some time

37
00:02:24,110 --> 00:02:24,830
over there.

38
00:02:24,990 --> 00:02:25,870
And look at that.

39
00:02:25,870 --> 00:02:27,870
We have got the entire class over here.

40
00:02:27,870 --> 00:02:31,310
So this is the, uh, this is the configuration that I'm talking about.

41
00:02:31,550 --> 00:02:37,310
Once we have this particular configuration, then we can create a JSON file which represents pretty

42
00:02:37,310 --> 00:02:39,470
much exactly the similar structure.

43
00:02:39,750 --> 00:02:46,230
So for instance, uh, you can create a JSON file over here, uh something like this.

44
00:02:46,550 --> 00:02:49,550
And you can name it uh, like probably.

45
00:02:49,830 --> 00:02:50,030
Yeah.

46
00:02:50,030 --> 00:02:54,150
You can just say app settings if you really wanted to, but it can be of anything to be honest.

47
00:02:54,430 --> 00:02:57,710
So I'm just going to say app settings dot JSON file.

48
00:02:57,990 --> 00:03:05,060
And in that app settings we can put all of these, uh, over here that I just represented in the configuration

49
00:03:05,060 --> 00:03:10,100
like provider, API key, base URL model and whatnot.

50
00:03:10,100 --> 00:03:15,140
So because you just saw me before, like how I was doing it in the demonstration.

51
00:03:15,420 --> 00:03:16,940
So I'm going to do the exact same thing.

52
00:03:16,940 --> 00:03:19,100
I'm just going to copy paste that over here.

53
00:03:19,100 --> 00:03:20,500
So it's going to be provided as local.

54
00:03:20,900 --> 00:03:22,020
This is the base URL.

55
00:03:22,220 --> 00:03:23,860
And I'm going to do it all here.

56
00:03:24,340 --> 00:03:25,100
Pretty cool.

57
00:03:25,340 --> 00:03:31,060
But how do we read this particular uh uh app settings file.

58
00:03:31,340 --> 00:03:37,540
The first thing is I wanted to do it is I need to go to the properties over here, make sure that you

59
00:03:37,820 --> 00:03:40,580
say copy if newer over here.

60
00:03:40,580 --> 00:03:44,620
If not, this particular app settings file is not going to be copied into a bin folder.

61
00:03:45,260 --> 00:03:46,820
If you really not did that before.

62
00:03:46,980 --> 00:03:49,140
I will try to explain you what I really mean about that.

63
00:03:49,500 --> 00:03:52,020
Let's say I want to build this particular solution.

64
00:03:52,300 --> 00:03:58,660
And now if I'm going to go to the bin directory, which is going to be on the finder, and if I'm going

65
00:03:58,700 --> 00:04:00,540
to go to the bin debug.

66
00:04:00,780 --> 00:04:04,940
Net nine, you see that we don't really have the app settings here.

67
00:04:04,940 --> 00:04:07,010
Even if you search it, it won't be there.

68
00:04:07,330 --> 00:04:13,010
The reason why is because it has not been copied to the bin folder and all your test is going to run

69
00:04:13,010 --> 00:04:18,970
from the bin folder, because that's where the dynamically linked library or DLLs are sitting, which

70
00:04:18,970 --> 00:04:25,130
is the one which is executing while you run the test or while you run the application in dotnet world.

71
00:04:25,890 --> 00:04:32,810
And now, because this app setting has not been copied, you need to force the dotnet to be copied to

72
00:04:33,490 --> 00:04:37,650
the output directory every single time while you build the application.

73
00:04:37,770 --> 00:04:40,090
So I have just changed that over here.

74
00:04:40,090 --> 00:04:42,890
This is going to be the same thing even in Visual Studio as well.

75
00:04:43,170 --> 00:04:44,570
And hit okay.

76
00:04:45,010 --> 00:04:52,250
And if I'm going to build the solution this time, and if I'm going to go to this particular project,

77
00:04:52,250 --> 00:04:57,210
which is going to be open in finder, you will go to the bin debug.

78
00:04:57,210 --> 00:04:58,050
Net nine.

79
00:04:58,250 --> 00:05:01,930
And you will also see that there's going to be appsettings.json file this time.

80
00:05:02,210 --> 00:05:03,730
This is coming over here.

81
00:05:03,730 --> 00:05:08,530
Because now that we have copied it over here, this is a is similar thing in Visual Studio.

82
00:05:08,530 --> 00:05:13,890
Just go to the properties and there is something called as just go and right click on the properties.

83
00:05:13,890 --> 00:05:20,530
In Visual Studio 2022, you will see similar kind of window where you can do a copy to output directory.

84
00:05:20,570 --> 00:05:22,050
Just make sure that you do that.

85
00:05:22,610 --> 00:05:23,450
All right.

86
00:05:23,450 --> 00:05:31,290
And once you have copied that, the next quest is to read from this particular app settings file and

87
00:05:32,210 --> 00:05:42,090
do a Deserialization to the LM configuration class file, and then call the LM configuration, uh,

88
00:05:42,290 --> 00:05:50,170
within your LM client class, uh, so that you can change all the hard coded value to the LM client

89
00:05:50,170 --> 00:05:50,570
class.

90
00:05:50,570 --> 00:05:57,210
That is the entire idea that we are going to be doing, which we are going to do in our next lecture.

91
00:05:57,210 --> 00:06:03,610
But if you want to try doing this, uh, see how that goes, try to do it yourself and see if you could

92
00:06:03,650 --> 00:06:04,730
able to achieve that.

93
00:06:04,850 --> 00:06:06,690
If you couldn't able to achieve that.

94
00:06:06,690 --> 00:06:07,650
Not a problem.

95
00:06:07,650 --> 00:06:09,570
We are going to do that in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 7. Reading Configuration from appSetting and deserializing it to LLMConfig

1
00:00:00,080 --> 00:00:01,120
All right.

2
00:00:01,120 --> 00:00:06,480
So now we are going to see how we can read the configuration from the Appsettings.json file.

3
00:00:06,800 --> 00:00:08,640
And then we created over here.

4
00:00:08,640 --> 00:00:11,000
There are many different ways available in C-sharp.

5
00:00:11,000 --> 00:00:11,520
To do it.

6
00:00:11,520 --> 00:00:17,640
You can directly read the JSON file from the file dot read all text method.

7
00:00:17,640 --> 00:00:23,360
Or you can also use the configuration extensions of Microsoft to do it.

8
00:00:23,400 --> 00:00:27,960
I mean, using the Microsoft's configuration extensions, the code will be very, very streamlined and

9
00:00:27,960 --> 00:00:28,760
straightforward.

10
00:00:28,760 --> 00:00:35,240
So the first thing which I'm going to do it over here is I'm going to create a super simple method within

11
00:00:35,240 --> 00:00:41,200
the configuration client class, so that you can see how you can read that configuration.

12
00:00:41,400 --> 00:00:41,800
Right.

13
00:00:41,800 --> 00:00:45,440
So I'm going to go over here I'm going to create a method.

14
00:00:45,480 --> 00:00:48,960
Maybe I'm just going to say public LM config.

15
00:00:49,520 --> 00:00:52,920
And then I'm going to say read JSON file.

16
00:00:53,240 --> 00:00:53,520
Right.

17
00:00:53,520 --> 00:00:57,680
So basically it's going to return me the config uh type.

18
00:00:57,680 --> 00:00:59,600
Once it reads that right.

19
00:00:59,600 --> 00:01:02,040
And once it's read that it is going to have all these value.

20
00:01:02,080 --> 00:01:04,440
That is the whole idea for this particular method.

21
00:01:04,440 --> 00:01:06,800
So how do we actually read the JSON file.

22
00:01:06,840 --> 00:01:14,430
You remember the JSON file is now sitting within the bin folder, which means you can do something like

23
00:01:14,430 --> 00:01:16,030
this in C sharp dotnet.

24
00:01:16,030 --> 00:01:22,310
And I'm not going to talk about that because these are something very, very uh, straightforward code

25
00:01:22,310 --> 00:01:25,430
that how you do it uh, in the dotnet world.

26
00:01:25,590 --> 00:01:28,910
So I'm just going to read the base directory which is the bin folder.

27
00:01:29,110 --> 00:01:36,310
And within this bin folder, uh, we have got what is called as a app settings dot JSON, which is going

28
00:01:36,310 --> 00:01:37,870
to have that JSON value.

29
00:01:38,230 --> 00:01:42,750
That's the path of our JSON file that we have got.

30
00:01:42,870 --> 00:01:43,470
Right.

31
00:01:43,470 --> 00:01:47,150
And once I read it I can then try to do this.

32
00:01:47,150 --> 00:01:52,950
I can just say string JSON data is equal to file.

33
00:01:53,070 --> 00:01:56,270
This is the class file in C sharp to read the file.

34
00:01:56,270 --> 00:01:58,510
And I'm going to say read all text.

35
00:01:58,710 --> 00:02:01,910
And I'm going to pass the JSON file path.

36
00:02:02,670 --> 00:02:11,230
And once I read it now I need to convert the app settings dot JSON file this particular properties from

37
00:02:11,230 --> 00:02:21,900
the JSON file into This configuration properties, because these are all matching the same name in the

38
00:02:21,940 --> 00:02:23,140
app settings as well.

39
00:02:23,180 --> 00:02:32,780
Look at that same case, same spellings and same, uh, properties that can be deserialized so much

40
00:02:32,780 --> 00:02:33,460
easily.

41
00:02:33,660 --> 00:02:37,780
Uh, in the uh, C sharp as we just did over here as well.

42
00:02:37,820 --> 00:02:42,220
Like deserialization the same thing I'm going to do, uh, over here as well.

43
00:02:42,220 --> 00:02:45,260
So once I read the entire text, I want to deserialize it.

44
00:02:45,260 --> 00:02:50,860
And the way I'm going to do it is I'm just going to say JSON serializer, dot deserialize.

45
00:02:50,900 --> 00:02:55,540
See, I'm going to pass the type here last time we passed JSON element.

46
00:02:55,540 --> 00:03:03,820
But I'm going to pass the LM configuration which is going to do the serialization for this particular

47
00:03:03,820 --> 00:03:04,980
JSON data.

48
00:03:05,540 --> 00:03:06,860
Oh that's easy.

49
00:03:07,460 --> 00:03:11,940
That's all three lines of code made this whole thing happen.

50
00:03:12,340 --> 00:03:17,300
And once you read this, you can now call this particular method anywhere that you wanted to.

51
00:03:17,340 --> 00:03:18,900
And then you can start using it.

52
00:03:19,500 --> 00:03:21,020
I'll tell you how you can do that.

53
00:03:21,420 --> 00:03:23,980
Let's go to the constructor of this particular class file.

54
00:03:24,140 --> 00:03:27,540
And I'm going to probably read the configuration over here.

55
00:03:27,580 --> 00:03:29,660
Let's assume that's what my plan is.

56
00:03:29,940 --> 00:03:36,980
So I'm just going to say uh, private read only because I'm just going to read it through.

57
00:03:37,380 --> 00:03:41,820
Uh, and I'm going to read the uh LM configuration.

58
00:03:41,820 --> 00:03:48,580
So LM configuration, uh, and I'm going to say LM configuration, something like that.

59
00:03:49,020 --> 00:03:55,340
So within this LM configuration so lm configuration I'm going to call the read JSON.

60
00:03:55,460 --> 00:03:56,020
That's it.

61
00:03:56,420 --> 00:04:02,180
If I call this method over here this is going to read the Appsettings file.

62
00:04:02,340 --> 00:04:06,420
And then it's going to get me the value from the app settings file.

63
00:04:06,580 --> 00:04:13,100
And it is going to store that with the LM configurations property over here.

64
00:04:14,300 --> 00:04:16,980
Hope you got the idea what I'm trying to do over here.

65
00:04:16,980 --> 00:04:17,220
Right.

66
00:04:17,220 --> 00:04:18,940
So this is very straightforward.

67
00:04:19,220 --> 00:04:25,460
If I call the constructor because you know that in C sharp or even Java, the moment you call the LM

68
00:04:25,620 --> 00:04:30,650
client class, it is going to initialize the HTTP client, and similarly is going to initialize the

69
00:04:30,650 --> 00:04:33,290
read JSON file method as well.

70
00:04:33,330 --> 00:04:35,050
I'm going to initialize this particular value.

71
00:04:35,090 --> 00:04:39,730
I'm going to put a break point here, and let me run this test so that you will understand what I'm

72
00:04:39,730 --> 00:04:40,770
really talking about.

73
00:04:41,210 --> 00:04:44,290
See the moment I run this particular code over here.

74
00:04:44,330 --> 00:04:50,450
See, it's going to invoke the client which is going to call the constructor, which is going to be

75
00:04:50,450 --> 00:04:51,410
coming over here.

76
00:04:51,570 --> 00:04:54,570
See now it's going to read the JSON for me.

77
00:04:54,570 --> 00:04:56,130
I'm going to put a break point here.

78
00:04:56,810 --> 00:04:57,730
Let's do that.

79
00:04:58,250 --> 00:05:02,330
Um and hopefully we have read that particular value.

80
00:05:02,730 --> 00:05:10,050
Um so maybe it's not let me do it one more time because we have to see how that reading is happening.

81
00:05:11,570 --> 00:05:12,930
So I'm going to put a break point.

82
00:05:12,970 --> 00:05:14,450
Yeah in this place.

83
00:05:14,890 --> 00:05:23,130
And let's try to debug this again just here and look at that.

84
00:05:23,130 --> 00:05:24,970
Now it's calling the read configuration.

85
00:05:25,010 --> 00:05:26,450
So it's going to read that value.

86
00:05:26,690 --> 00:05:29,010
And looks like this is failing at the moment.

87
00:05:29,050 --> 00:05:29,890
Ah look at that.

88
00:05:29,890 --> 00:05:31,970
It says Appsettings.json.

89
00:05:31,970 --> 00:05:36,040
But what I have got the file name is app setting which is wrong.

90
00:05:36,280 --> 00:05:41,840
So I should either change the file name or on the test code over there.

91
00:05:42,080 --> 00:05:48,840
Uh, let me go and modify the, uh, modify the code over here so it's not appsettings.

92
00:05:48,840 --> 00:05:49,240
Sorry.

93
00:05:49,280 --> 00:05:50,280
It's upsetting.

94
00:05:50,800 --> 00:05:53,120
Uh, hopefully that time this will work.

95
00:05:53,360 --> 00:05:54,480
Let me debug it again.

96
00:05:56,240 --> 00:05:57,720
Just added a plural there.

97
00:05:57,880 --> 00:06:00,480
That's how it's going to be in the dotnet world anyways.

98
00:06:00,520 --> 00:06:01,880
Oh look at that now it worked.

99
00:06:02,320 --> 00:06:04,800
Now it's going to deserialize this particular value.

100
00:06:05,600 --> 00:06:11,680
And now if you go to the configuration you should see we have got all the values which is amazing.

101
00:06:11,920 --> 00:06:17,400
Now I can use these values within my code and see how that works.

102
00:06:17,640 --> 00:06:20,320
So hope you got the idea how we are doing this.

103
00:06:20,880 --> 00:06:24,040
Now next lecture I'm just going to replace all the value.

104
00:06:24,200 --> 00:06:30,720
And that way we will have a configuration for all of these, uh, code that we have written as a hard

105
00:06:30,760 --> 00:06:31,560
coded value.

106
00:06:31,680 --> 00:06:35,000
I will let you to do it yourself and see how that goes.

107
00:06:35,200 --> 00:06:39,200
Uh, but if not, we are going to do that exact same thing in our next lecture.

108
00:06:39,200 --> 00:06:39,880
But guess what?

109
00:06:39,920 --> 00:06:41,360
This is very, very straightforward.

110
00:06:41,640 --> 00:06:42,960
I will let you do it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 8. Replacing hardcoded values in LLMClient in favor of Configuration

1
00:00:00,120 --> 00:00:01,000
All right.

2
00:00:01,240 --> 00:00:04,640
The last operation, as I told you, was to read from the configuration.

3
00:00:04,640 --> 00:00:06,440
I hope you have modified that.

4
00:00:06,440 --> 00:00:09,280
If not, I'm just going to go and modify it over here.

5
00:00:09,280 --> 00:00:14,440
So I'm just going to say LM configuration dot and then just pass the model.

6
00:00:14,440 --> 00:00:17,160
So that's where it's going to get the model for me.

7
00:00:17,160 --> 00:00:22,760
And if you're going to change the temperature then you're going to just say LM configuration dot.

8
00:00:22,880 --> 00:00:29,720
And then you can say the model that's going to get the sorry the temperature that's going to get the

9
00:00:29,720 --> 00:00:30,840
temperature over here.

10
00:00:30,880 --> 00:00:33,680
So now we are not really hard coding any of these.

11
00:00:34,040 --> 00:00:39,640
And the same thing goes for uh the base URL as well which is over here.

12
00:00:39,640 --> 00:00:49,560
So just put a string interpolation uh and just replace that from this to uh a braces over here and say

13
00:00:49,600 --> 00:00:52,680
lm configuration dot base URL.

14
00:00:52,680 --> 00:00:55,560
That's going to get the base URL for this particular API.

15
00:00:56,200 --> 00:01:02,960
And you can also replace the same thing over here with a model.

16
00:01:03,320 --> 00:01:10,380
Uh, and the temperature you can just say the LM configuration temperature, which is pretty cool.

17
00:01:10,540 --> 00:01:16,300
And you can also pass the max token if you really wanted to, because we have really not passed the

18
00:01:16,740 --> 00:01:18,060
Max token over here.

19
00:01:18,060 --> 00:01:27,180
I can also set that max tokens is equal to LM configuration dot max tokens, which is going to be the

20
00:01:27,180 --> 00:01:29,940
number of tokens that you wanted to spend.

21
00:01:29,940 --> 00:01:33,500
And this is especially useful while you're using a paid version of the model.

22
00:01:33,500 --> 00:01:35,380
That's why this is very important.

23
00:01:35,700 --> 00:01:39,540
Uh, and now this particular base URL will change as well.

24
00:01:40,020 --> 00:01:41,340
So I'm just going to say.

25
00:01:43,420 --> 00:01:44,220
Like this.

26
00:01:44,700 --> 00:01:47,260
And we need to make a string interpolation.

27
00:01:47,260 --> 00:01:52,100
So configuration dot base URL something like this.

28
00:01:52,660 --> 00:02:01,140
Uh and finally we have to modify the OpenAI key as well which is going to be LM configuration dot API

29
00:02:01,140 --> 00:02:01,460
key.

30
00:02:01,780 --> 00:02:02,020
Right.

31
00:02:02,020 --> 00:02:03,300
Because this requires an API key.

32
00:02:03,300 --> 00:02:09,060
So this API key that you have got over here can be completely moved out because this is going to come

33
00:02:09,060 --> 00:02:10,620
from the configuration now.

34
00:02:10,780 --> 00:02:12,930
So we don't even need this guy anymore.

35
00:02:13,130 --> 00:02:17,650
So I can just have this in my app setting file.

36
00:02:18,090 --> 00:02:23,970
So let me go copy this whole thing, cut this out, and I'm going to delete this because we don't need

37
00:02:23,970 --> 00:02:24,650
this anymore.

38
00:02:25,210 --> 00:02:28,130
And I'm going to put this over here.

39
00:02:28,690 --> 00:02:33,490
But this is only required if it is going to be on the OpenAI.

40
00:02:33,650 --> 00:02:37,650
Not for the local model.

41
00:02:37,890 --> 00:02:41,210
So I'm going to save this particular code and done.

42
00:02:41,250 --> 00:02:41,850
Look at that.

43
00:02:41,850 --> 00:02:47,490
Now we already have everything moved to a configuration which is pretty cool.

44
00:02:47,490 --> 00:02:53,770
So the client is already so much mature and it has got everything configured.

45
00:02:53,930 --> 00:02:56,730
Uh, all of them are coming from a configuration.

46
00:02:56,930 --> 00:03:02,130
But now you may have a question saying, hey Karthik, we are still trying to hard code the value like

47
00:03:02,130 --> 00:03:06,650
column message, uh, async or the call OpenAI async.

48
00:03:06,810 --> 00:03:13,970
Is there a method where I can control both of them in one single place, like based on the the configuration,

49
00:03:14,010 --> 00:03:15,530
like what provider that I'm passing in?

50
00:03:15,530 --> 00:03:19,910
Because we also have got a property called as provider.

51
00:03:19,910 --> 00:03:21,590
We have not really even used that.

52
00:03:21,590 --> 00:03:24,310
So how are we going to use that particular code?

53
00:03:24,470 --> 00:03:30,310
Well guess what, we are going to write one more method over here which does that operation.

54
00:03:30,310 --> 00:03:34,270
For me, the way that particular method is going to look like is going to be like this.

55
00:03:34,270 --> 00:03:42,710
I'm going to say public async task, and I'm going to just say, uh, probably, uh, just going to

56
00:03:42,710 --> 00:03:43,630
be a task for now.

57
00:03:43,670 --> 00:03:45,990
It's not going to return you anything at the moment.

58
00:03:45,990 --> 00:03:47,910
And then I'm going to just say string.

59
00:03:47,950 --> 00:03:53,390
Of course, it needs to return something and then I'm going to say get completion async, something

60
00:03:53,390 --> 00:03:53,950
like that.

61
00:03:54,190 --> 00:03:56,630
And here I'm going to pass the prompt.

62
00:03:56,750 --> 00:04:07,190
So basically what this method is going to do is based on your uh, your actual configurations with a

63
00:04:07,190 --> 00:04:11,950
provider, it is going to choose the method for you.

64
00:04:12,390 --> 00:04:13,750
Ooh, look at that.

65
00:04:13,750 --> 00:04:17,750
That's why we have that particular, uh, code over there.

66
00:04:17,750 --> 00:04:21,990
So I'm going to use a switch expression of the C sharp dotnet over here.

67
00:04:22,300 --> 00:04:24,580
and I will show you how you can actually write that.

68
00:04:24,940 --> 00:04:35,540
So the way you can do it is if you see it is going to be an open AI model, then you return me a call

69
00:04:35,580 --> 00:04:46,980
to open AI async method and pass the prompt, or else if it is local that you're passing in in the provider

70
00:04:47,020 --> 00:04:56,860
code over here, then you need to use the method, call local LMS and then call this particular method.

71
00:04:57,380 --> 00:05:01,540
If nothing is there, uh, then you can actually put a comma there.

72
00:05:02,100 --> 00:05:09,460
If nothing is going to be there, then you are going to throw a new, uh, not supported exception,

73
00:05:09,460 --> 00:05:10,340
something like that.

74
00:05:10,380 --> 00:05:11,460
Uh, it can be anything.

75
00:05:11,780 --> 00:05:19,860
And over here you can just say the provider, uh, and uh, you can just say underscore lm config dot

76
00:05:20,140 --> 00:05:23,900
provider, uh, is not supported something like that.

77
00:05:26,740 --> 00:05:32,320
See this is what is this particular get completion async method is going to do for you.

78
00:05:32,640 --> 00:05:38,920
So if you use this method now it is going to go and choose based on what you're going to pass in.

79
00:05:38,920 --> 00:05:44,440
So if I'm going to say local then it will automatically go and choose the local method.

80
00:05:44,440 --> 00:05:46,000
And then it's going to run for you.

81
00:05:46,000 --> 00:05:48,480
And you don't necessarily have to do it over here.

82
00:05:48,480 --> 00:05:53,200
All you have to do it in your test code is just called that get completion.

83
00:05:53,200 --> 00:05:54,800
You don't even have to comment the code.

84
00:05:54,800 --> 00:05:56,440
Something like how we did over here.

85
00:05:56,480 --> 00:05:58,800
See, this code will completely go away.

86
00:05:59,080 --> 00:06:03,120
And rather I'm just going to say get completion async.

87
00:06:03,160 --> 00:06:05,600
See, this is what I have to pass over here.

88
00:06:06,040 --> 00:06:11,720
And I don't even need another line which is commented right now because based on what I have passed

89
00:06:11,720 --> 00:06:14,920
over here, it is going to choose things for you.

90
00:06:14,920 --> 00:06:22,800
So because now I have chosen local over here, it is going to automatically run the test using the local

91
00:06:22,800 --> 00:06:27,440
large language model instead of using the open AI language model.

92
00:06:27,440 --> 00:06:28,400
So I'm running it.

93
00:06:28,400 --> 00:06:30,520
You will notice that it is a bit slower.

94
00:06:31,040 --> 00:06:37,030
The reason why is because it is using the local large language model right now, not the OpenAI model.

95
00:06:37,350 --> 00:06:37,790
Right?

96
00:06:37,830 --> 00:06:43,590
So this is how things are going to work with that small, uh, method that we have written, which is

97
00:06:43,590 --> 00:06:46,230
nothing but the get completion async method.

98
00:06:46,430 --> 00:06:53,750
But now, hey, we have used all the configurations, uh, element that we have got, which is these,

99
00:06:54,030 --> 00:07:04,550
uh, and we have also seen how we have replaced our existing hardcoded values, uh, into a configuration,

100
00:07:05,270 --> 00:07:13,670
uh, method so that now this can be act as a stepping stone for you to perform all the operation that

101
00:07:13,670 --> 00:07:16,910
you can do to talk with your large language model.

102
00:07:17,190 --> 00:07:19,870
But now we have few more things to do as well.

103
00:07:19,870 --> 00:07:27,190
We now need to see how the responses are going to come out from the large language model, and how we

104
00:07:27,190 --> 00:07:35,790
need to massage the message, which can always be always similar and always same all the time, regardless

105
00:07:36,030 --> 00:07:39,310
which we are going to be doing in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 9. Understanding the Problem statement to use Self Healing Strategies

1
00:00:00,160 --> 00:00:01,080
All right.

2
00:00:01,400 --> 00:00:08,240
Now that we have seen how we can talk with the local large language models as well as the cloud based

3
00:00:08,240 --> 00:00:11,160
large language model using the C sharp.

4
00:00:11,400 --> 00:00:14,600
Net code with just the HTTP client.

5
00:00:14,920 --> 00:00:23,240
And we have also seen how easy it is to customize all of these operations, get the Deserialized responses,

6
00:00:23,520 --> 00:00:30,760
and we can also set the configurations like app settings to control these large language model settings

7
00:00:30,760 --> 00:00:35,360
like different models as well as weights and temperature that we wanted to.

8
00:00:35,600 --> 00:00:36,840
So we have seen everything.

9
00:00:36,840 --> 00:00:40,960
How we can do that until our last lecture of this section.

10
00:00:40,960 --> 00:00:49,080
But now we are going to see how we can fine tune our prompt a bit, so that we can make use of what

11
00:00:49,080 --> 00:00:52,560
we are going to achieve with the self-healing of the locator.

12
00:00:53,400 --> 00:00:58,680
But again, we still have to see there are so many places which are still pending over here.

13
00:00:58,680 --> 00:01:04,500
This is going to be a long journey before we achieve this particular point, but at least now we are

14
00:01:04,500 --> 00:01:09,460
going to talk about the formatting of the prompt before we wind up this particular section.

15
00:01:09,700 --> 00:01:12,380
So let's see how we are going to format the prompt.

16
00:01:12,380 --> 00:01:16,340
But before that, let's first of all understand the problem statement a bit.

17
00:01:17,300 --> 00:01:23,700
We know that these locators that we write in the page object model code in selenium may get brittle

18
00:01:23,700 --> 00:01:24,980
over the period of time.

19
00:01:24,980 --> 00:01:31,500
If there is any change in the application's user interface, maybe the locator type could change, the

20
00:01:31,500 --> 00:01:37,660
locator itself could change, or maybe the element could completely be disappeared from the UI.

21
00:01:38,180 --> 00:01:45,500
We need to ensure that any of these locator if it changes for any reason, we also self heal them,

22
00:01:45,500 --> 00:01:50,540
which we can do by finding an alternative locators of this particular element.

23
00:01:50,740 --> 00:01:54,900
But when and how are we going to find the alternative locators?

24
00:01:54,900 --> 00:02:01,870
Well guess what, we can do this by supplying the complete page of our application, along with the

25
00:02:01,870 --> 00:02:05,750
Page Object model code that we have got to the large language model.

26
00:02:05,750 --> 00:02:08,510
It can be even the local large language model.

27
00:02:08,510 --> 00:02:14,310
And based on that, we can ask the large language model to tell us if there is any alternative locators

28
00:02:14,310 --> 00:02:17,230
available for this particular element.

29
00:02:17,630 --> 00:02:24,670
This is the only way that we can self-heal the locators within our code that we have got.

30
00:02:24,830 --> 00:02:32,390
So what if this login link text doesn't work, but it has got an ID as we saw earlier for our application.

31
00:02:32,630 --> 00:02:41,390
So if we pass the page and the page object model code over here, we can now get the ID because the

32
00:02:41,390 --> 00:02:44,910
large language model knows what is the locator for that.

33
00:02:44,910 --> 00:02:47,310
And then it will give you the alternative locator.

34
00:02:47,310 --> 00:02:53,350
And then your code will start working with the alternative locator instead of the locator which is there

35
00:02:53,350 --> 00:02:54,430
in your code.

36
00:02:54,550 --> 00:02:59,450
That is what we are going to be building over the period of time, but at least now we need to first

37
00:02:59,450 --> 00:03:00,250
of all, battle.

38
00:03:00,290 --> 00:03:02,410
How do we do this operation?

39
00:03:02,610 --> 00:03:08,570
But then next question naturally comes is how are we going to pass the page object model locators and

40
00:03:08,570 --> 00:03:12,130
the page to the large language model itself?

41
00:03:12,810 --> 00:03:13,730
Well guess what?

42
00:03:13,770 --> 00:03:21,850
We can pass the entire page source from our selenium code using the driver dot page source property.

43
00:03:21,850 --> 00:03:23,330
That is very, very straightforward.

44
00:03:23,330 --> 00:03:24,370
We can do that.

45
00:03:24,370 --> 00:03:30,450
But how are we going to pass the page object model locators to the large language model.

46
00:03:30,730 --> 00:03:35,890
Are we going to pass the entire C sharp class file to make that happen?

47
00:03:36,930 --> 00:03:37,850
Well guess what.

48
00:03:38,010 --> 00:03:39,610
We are not going to do that.

49
00:03:39,890 --> 00:03:47,650
We are actually going to pass the locator along with the locator type and the page source, and ask

50
00:03:47,650 --> 00:03:52,290
the large language model to return the alternative locator for the failing locators.

51
00:03:52,890 --> 00:04:04,030
So essentially if you see here we have got the locator type, which is this one, as you can see over

52
00:04:04,030 --> 00:04:04,630
here.

53
00:04:04,990 --> 00:04:15,030
And the locator itself, which is this one, we are going to pass both of them along with the page source

54
00:04:15,070 --> 00:04:19,830
of our application, which is this one to the large language model.

55
00:04:19,830 --> 00:04:25,910
So basically we are going to pass one, two and three items to the large language model.

56
00:04:26,270 --> 00:04:32,670
And then we are going to get an alternative locator if this locator fails for some reason.

57
00:04:33,310 --> 00:04:41,470
So if this guy fails for some reason, then we are going to invoke the large language model to get as

58
00:04:41,470 --> 00:04:44,230
an alternative locator, which is this one.

59
00:04:44,710 --> 00:04:46,310
That is, what is the expectation.

60
00:04:46,310 --> 00:04:51,270
That is the way that we can self-heal our entire code.

61
00:04:51,990 --> 00:04:55,590
That's the crux that we are going to be seeing how we are going to achieve it.

62
00:04:55,670 --> 00:05:02,680
So in order to achieve this way better, we are going to make use of a trick to make this happen.

63
00:05:02,680 --> 00:05:08,760
We know how we can get the page source from using driver dot page source property, but how are we going

64
00:05:08,800 --> 00:05:12,360
to pass the locator and the locator type?

65
00:05:12,760 --> 00:05:18,160
Well, there is a very, very simple trick which is available in selenium with C dot net where you can

66
00:05:18,160 --> 00:05:27,480
actually use the two string method of the locator to get the locator type and the locator itself.

67
00:05:27,480 --> 00:05:33,560
You can get both of them separately, and you need to do a bit of a massage to get these things out.

68
00:05:33,760 --> 00:05:38,680
I'm going to quickly show you how that's going to happen in our next lecture, and I will also show

69
00:05:38,680 --> 00:05:45,760
you how we can format our prompt to get the alternative locators from a large language model.

70
00:05:46,000 --> 00:05:51,560
If you get that idea, I'm telling you, the rest of the lectures are going to be like a cakewalk for

71
00:05:51,560 --> 00:05:56,720
you because you have already got the crux of what we are going to be achieving pretty soon.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 10. Getting LocatorType and LocatorValue from POM Code of Selenium using ToString()

1
00:00:00,280 --> 00:00:03,800
All right, now, let's get back to our code over here.

2
00:00:03,880 --> 00:00:06,760
I'm going to quickly show you the trick of what I was talking about.

3
00:00:06,760 --> 00:00:14,400
To get the locator type, as well as the locator value and the page source that we can pass to the large

4
00:00:14,400 --> 00:00:15,440
language model.

5
00:00:15,760 --> 00:00:20,560
So in order to do that, I'm going to go back to our enhanced test over here one more time.

6
00:00:20,720 --> 00:00:24,440
But before that I'm going to go and copy this particular locator that I have got.

7
00:00:24,800 --> 00:00:27,640
And then I'm going to go to the enhanced test over here.

8
00:00:28,000 --> 00:00:32,680
And I'm going to uh, just uh, pass the locator over here.

9
00:00:32,680 --> 00:00:40,520
So I'm going to say, uh, the locator, uh, and over here I'm going to pass this.

10
00:00:41,280 --> 00:00:41,920
Right.

11
00:00:41,920 --> 00:00:44,280
And now I need to get the page source.

12
00:00:44,280 --> 00:00:49,360
And the way I can get the page source is by using selenium, as you already know.

13
00:00:49,480 --> 00:00:54,040
So I'm going to go and copy the code which is invoking the selenium code.

14
00:00:54,040 --> 00:00:57,200
So no shame just copying this particular code.

15
00:00:57,480 --> 00:00:59,960
And I'm going to paste that over here.

16
00:01:00,000 --> 00:01:05,000
You don't need a try catch block, because we know that this is going to just work, and that's going

17
00:01:05,000 --> 00:01:08,120
to go and identify the page for me.

18
00:01:08,760 --> 00:01:16,520
And I'm just going to say, maybe I'm just going to cut this code and paste it over here.

19
00:01:17,040 --> 00:01:21,160
Uh, and I'm going to get the page source as well, the page source I can get.

20
00:01:21,160 --> 00:01:25,560
So I'm going to say page source I'm going to get using the driver dot.

21
00:01:25,760 --> 00:01:27,640
And then there is something called as page source.

22
00:01:27,640 --> 00:01:30,960
This is going to get the entire page source of our application.

23
00:01:31,000 --> 00:01:33,720
So this is going to get the source code of our page.

24
00:01:34,040 --> 00:01:39,240
And this is the locator that we are going to be identifying as an alternative locator.

25
00:01:39,280 --> 00:01:39,760
Right.

26
00:01:39,800 --> 00:01:41,920
I want to see if I can able to get that.

27
00:01:41,920 --> 00:01:47,520
So if I going to go to the Google Chrome and if I'm going to go to the login, this is what I'm trying

28
00:01:47,520 --> 00:01:49,440
to see if there is any alternative locator.

29
00:01:49,520 --> 00:01:54,960
If I'm going to do an inspect, you can see that there is an alternative locator of ID as the login

30
00:01:54,960 --> 00:01:55,320
link.

31
00:01:55,320 --> 00:01:59,750
And that is what I want to identify if the large language model can go and identify for me.

32
00:02:00,150 --> 00:02:00,870
Right.

33
00:02:00,870 --> 00:02:03,110
So I have got both of them over here.

34
00:02:03,310 --> 00:02:09,550
But now we need to pass what is the current locator type and the locator value.

35
00:02:09,750 --> 00:02:16,190
Only then the large language model can go and identify what is the alternative locators for that.

36
00:02:16,190 --> 00:02:23,710
So in order to get the locator type and locator value, you can actually do a small C sharp dotnet code

37
00:02:23,710 --> 00:02:24,390
over here.

38
00:02:24,710 --> 00:02:28,670
As I told you, just use what is called as two string.

39
00:02:28,670 --> 00:02:35,790
So I'm going to say var as strategy is called as strategy string.

40
00:02:35,830 --> 00:02:39,590
Probably because I'm going to identify the strategy using that.

41
00:02:39,630 --> 00:02:47,270
So I'm going to say um this guy the locator that we have the locator dot two string.

42
00:02:47,270 --> 00:02:48,910
So if I'm going to do a two string.

43
00:02:48,950 --> 00:02:51,190
So this is essentially like this guy dot two string.

44
00:02:51,230 --> 00:02:52,070
It's not big deal.

45
00:02:52,070 --> 00:02:57,230
I'm just saying uh this as two string or located at it can be of anything.

46
00:02:57,270 --> 00:02:57,830
Right.

47
00:02:57,830 --> 00:02:59,310
So I'm going to say two string.

48
00:02:59,670 --> 00:03:02,950
When I do this I'll tell you how this code is going to be.

49
00:03:02,950 --> 00:03:04,630
Let me put a break point here.

50
00:03:04,950 --> 00:03:10,550
Uh, and let me try to, uh, run this particular code.

51
00:03:10,550 --> 00:03:17,990
So if I'm going to say debug this unit test, of course, this is going to open the application and

52
00:03:17,990 --> 00:03:19,510
navigate to the page for now.

53
00:03:19,510 --> 00:03:21,470
And I'm just going to let that happen.

54
00:03:22,990 --> 00:03:23,830
All right.

55
00:03:24,190 --> 00:03:29,190
And you can see that now it has got to this strategy string I'm going to put a breakpoint here as well.

56
00:03:29,190 --> 00:03:38,230
And if I try to uh just select this and evaluate the expression, you will notice that how this particular

57
00:03:38,510 --> 00:03:40,510
locator is getting us.

58
00:03:41,470 --> 00:03:49,430
So this buy dot link text is the locator type and login is the locator value.

59
00:03:50,750 --> 00:03:51,230
See.

60
00:03:51,790 --> 00:03:56,380
So now we can pass this as a locator type and then the locator value.

61
00:03:56,380 --> 00:04:04,060
If we pass both of them over here, then we could just identify things so much easily.

62
00:04:04,380 --> 00:04:06,820
So that is what we are going to be passing in over here.

63
00:04:06,820 --> 00:04:09,300
This is the strategy string that we have got.

64
00:04:09,500 --> 00:04:17,700
So what I'm going to say is I want to get the locator value as well as the locator type.

65
00:04:17,700 --> 00:04:25,700
So the way I can actually get out is I can first get the index of the uh, the separator that we have

66
00:04:25,740 --> 00:04:26,020
got.

67
00:04:26,020 --> 00:04:32,820
So int uh separator uh index something like this separator I think the spelling is wrong.

68
00:04:33,020 --> 00:04:40,260
So I'm going to just say separator index as the strategy string uh dot index of and we know that the

69
00:04:40,260 --> 00:04:42,860
separator is an a colon there.

70
00:04:42,860 --> 00:04:44,980
So I'm going to get that particular colon there.

71
00:04:45,220 --> 00:04:48,380
That's going to get the, the the index.

72
00:04:48,540 --> 00:04:54,100
And now I'm going to get the uh, the type as well as the values is the type.

73
00:04:54,100 --> 00:05:01,900
So I'm going to say locator type, which is going to be the strategy string dot.

74
00:05:01,940 --> 00:05:08,100
And there is a method called as substring or which can get you the string that you are looking for.

75
00:05:08,140 --> 00:05:10,180
So I'm going to say separator index.

76
00:05:10,180 --> 00:05:12,940
So that's going to get you the locator type.

77
00:05:12,940 --> 00:05:15,500
And I also need to get the locator value.

78
00:05:15,780 --> 00:05:19,580
So I'm just going to say strategy string dot substring.

79
00:05:19,900 --> 00:05:29,420
And I'm going to say the separator index plus one uh with um I think that should be good enough to get

80
00:05:29,420 --> 00:05:31,380
that particular value.

81
00:05:33,180 --> 00:05:36,940
I know this kind of codes are kind of a logic in C sharp dot net that you have to do.

82
00:05:36,980 --> 00:05:41,900
It's nothing to do with the automation itself, but this is how you can write the logics very clearly.

83
00:05:41,940 --> 00:05:42,460
Right.

84
00:05:42,500 --> 00:05:44,780
So that is what's going to happen over here.

85
00:05:44,780 --> 00:05:48,220
So we are going to get the page source locator type and look at our value.

86
00:05:48,220 --> 00:05:52,770
All of them this time so that our prompt is going to be ready.

87
00:05:52,770 --> 00:05:58,570
But for now, just let's try to execute this code and see what is the output of this particular code

88
00:05:58,810 --> 00:06:00,810
so that you can understand how things are working.

89
00:06:01,330 --> 00:06:02,410
Uh pretty cool.

90
00:06:02,410 --> 00:06:06,210
So we have got that and look at that.

91
00:06:06,210 --> 00:06:11,690
So we have got the locator type as by dot link text and the locator value as login.

92
00:06:11,690 --> 00:06:17,330
So we have got all of these and we have of course got the page source as well as you can see the entire

93
00:06:17,330 --> 00:06:18,050
page source.

94
00:06:18,290 --> 00:06:21,010
And now I'm going to pass the page source.

95
00:06:21,290 --> 00:06:27,730
And then I'm going to ask the large language model that I have got a locator type as this with its locator

96
00:06:27,730 --> 00:06:29,050
value as this one.

97
00:06:29,610 --> 00:06:37,850
But can you go and identify me an alternative locator, uh, using this particular page source, if

98
00:06:37,850 --> 00:06:43,170
I'm going to ask this question to the large language model, then it is going to get me the alternative

99
00:06:43,170 --> 00:06:44,770
locators hopefully.

100
00:06:45,210 --> 00:06:49,570
So we'll see how that is going to be working in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 11. Passing PageSource and Locator Context to LLMs to get Alternative Locators

1
00:00:00,040 --> 00:00:00,840
All right.

2
00:00:00,840 --> 00:00:06,120
So now is the prime time for us to see how our large language model is going to respond to us.

3
00:00:06,400 --> 00:00:12,840
So the way I'm going to do it is I'm going to get the page source and then the locator type and the

4
00:00:12,880 --> 00:00:17,120
locator value, and then I'm going to pass it to the large language model.

5
00:00:17,120 --> 00:00:21,920
And then I'm going to ask the question to give me an alternative locator.

6
00:00:22,120 --> 00:00:26,280
So let's go and try first with the cloud desktop and see how that works.

7
00:00:26,280 --> 00:00:28,520
So this is the thing that we did already.

8
00:00:28,960 --> 00:00:32,200
And now let's go and see how we can do it.

9
00:00:32,320 --> 00:00:37,160
So what I'm going to do it is I'm going to tell it the large language model over here.

10
00:00:37,160 --> 00:00:47,720
Is that the web element uh, with maybe uh, locator type and locator type is going to be by dot.

11
00:00:48,080 --> 00:00:58,200
Um, I think we got it like by dot link text locator value, which is going to be uh login.

12
00:00:59,000 --> 00:01:05,630
And I'm going to say cannot be found in the page source.

13
00:01:06,150 --> 00:01:10,230
Um, I'm going to say which is attached.

14
00:01:11,390 --> 00:01:13,350
So we need to attach that over there.

15
00:01:13,670 --> 00:01:19,030
And I'm going to say based on the page source.

16
00:01:19,190 --> 00:01:25,270
Can you suggest me an alternative locator that could really work.

17
00:01:25,430 --> 00:01:27,750
Oops I have actually pressed the enter there.

18
00:01:27,750 --> 00:01:28,630
Sorry about that.

19
00:01:28,630 --> 00:01:30,390
I'm going to copy it one more time.

20
00:01:30,390 --> 00:01:31,910
I'm going to paste it over here.

21
00:01:32,310 --> 00:01:43,070
Uh, and I'm also going to say that important because I want to only return the, um, uh, valid JSON

22
00:01:43,230 --> 00:01:43,830
as well.

23
00:01:43,830 --> 00:01:53,070
So I'm going to say return only a valid JSON object for, for the keys.

24
00:01:53,830 --> 00:02:03,700
Um, and I'm going to say the key is going to be ID uh name, uh XPath uh CSS selector and then class

25
00:02:03,700 --> 00:02:06,500
name uh and link text.

26
00:02:06,500 --> 00:02:08,060
That is what I wanted to return.

27
00:02:08,340 --> 00:02:20,140
And I'm also going to say format as uh, proper uh JSON with uh, double quotes because I wanted to

28
00:02:20,140 --> 00:02:22,140
get the double quotes of the JSON.

29
00:02:22,380 --> 00:02:25,420
And I'm also going to say one more thing, which is very, very important.

30
00:02:25,580 --> 00:02:36,220
Do not include explanations or commons, just return the JSON object.

31
00:02:36,220 --> 00:02:41,300
The reason why I wanted to say this is because you might have seen many times when you try to ask the

32
00:02:41,300 --> 00:02:47,580
large language model for any of these suggestions, it will start giving you the explanations and comments

33
00:02:47,580 --> 00:02:50,180
and reasons for that which we don't even need.

34
00:02:50,420 --> 00:02:52,340
We just need the JSON object.

35
00:02:52,340 --> 00:02:54,740
So make sure that you do that over here as well.

36
00:02:54,740 --> 00:02:56,260
This is very, very important.

37
00:02:56,260 --> 00:03:02,210
And I'm also telling that return only the valid JSON object for the keys, which is id name, XPath,

38
00:03:02,250 --> 00:03:05,250
CSS, and something like that because we don't need anything else as well.

39
00:03:05,690 --> 00:03:09,130
And as that said, I'm also going to pass the page source.

40
00:03:09,130 --> 00:03:18,090
So I need to go to our app which is this one, and let's go and inspect the page source which is this

41
00:03:18,090 --> 00:03:18,450
guy.

42
00:03:18,490 --> 00:03:20,210
So I'm going to copy this page source.

43
00:03:20,530 --> 00:03:23,450
And I'm going to attach it over here.

44
00:03:23,650 --> 00:03:26,450
And I'm going to send it to the large language model.

45
00:03:26,490 --> 00:03:30,130
And we'll see what we are going to get the result out from this.

46
00:03:30,450 --> 00:03:31,490
Look at that.

47
00:03:31,930 --> 00:03:41,290
We are just getting the locators alternative for this particular locator type over there like ID name,

48
00:03:42,210 --> 00:03:49,730
XPath, CSS selector class name, as well as the link text login, which was fantastic.

49
00:03:50,130 --> 00:03:52,410
See, this is what we wanted.

50
00:03:52,610 --> 00:04:00,190
And now we have already found out that there is a way that we can find an alternative locator or alternative

51
00:04:00,190 --> 00:04:06,310
locators for this particular locator that we have got, which is this one.

52
00:04:06,550 --> 00:04:14,390
So if we have this kind of ability, we have already completed like 90 percentage of our self-healing

53
00:04:14,390 --> 00:04:20,710
operation, because just with the locator type and locator value and the page source that we have attached,

54
00:04:20,870 --> 00:04:24,790
we could able to obtain the alternative locators already.

55
00:04:25,110 --> 00:04:31,110
Now all we have to do it is we need to somehow massage the large language model response in such a way

56
00:04:31,270 --> 00:04:39,550
that we get the locators, and then we pass this locator to the locator strategy identifier, or somebody

57
00:04:39,550 --> 00:04:45,070
which can go and get the locator and then perform the rest of the operation in selenium.

58
00:04:45,430 --> 00:04:47,990
This is the idea of self-healing.

59
00:04:48,270 --> 00:04:50,950
We are not really updating the test code.

60
00:04:50,990 --> 00:04:57,020
Rather we are actually identifying an alternative locator to self-heal our test execution.

61
00:04:57,300 --> 00:04:58,380
This is the power.

62
00:04:58,420 --> 00:05:01,580
Guys, this is how we are going to achieve it over here.

63
00:05:01,580 --> 00:05:04,980
And hope you already got the idea of what we are trying to achieve.

64
00:05:05,140 --> 00:05:11,300
This is really interesting to be honest, because we have found the very amazing way of doing this,

65
00:05:11,300 --> 00:05:12,500
which is pretty cool.

66
00:05:12,540 --> 00:05:17,860
I'm still intrigued that to see whether this is going to work with our local large language model as

67
00:05:17,860 --> 00:05:18,420
well.

68
00:05:18,420 --> 00:05:21,660
So I'm going to go and open my O llama here.

69
00:05:21,900 --> 00:05:24,180
And remember this is something which we are doing earlier.

70
00:05:24,380 --> 00:05:26,540
So I'm just still on the same screen.

71
00:05:26,540 --> 00:05:28,980
And over here I'm going to paste this guy.

72
00:05:29,340 --> 00:05:34,860
And I'm also going to copy paste this page source as well, uh, which is this one.

73
00:05:35,220 --> 00:05:43,460
And I'm going to run and let's see if this large language model also returns how the cloud desktop return.

74
00:05:43,460 --> 00:05:50,820
And I'm sure this is going to return as well, because that's exactly how I use this model to perform

75
00:05:50,860 --> 00:05:53,930
the login operations and selection operation.

76
00:05:53,970 --> 00:05:54,690
Look at that.

77
00:05:55,130 --> 00:05:56,090
There you go.

78
00:05:56,130 --> 00:05:57,250
We got the alternative.

79
00:05:57,250 --> 00:05:57,850
Look here.

80
00:05:58,330 --> 00:05:59,370
This is fabulous.

81
00:05:59,570 --> 00:06:05,170
And now, regardless of whichever language model that you use, the output is always going to be consistent

82
00:06:05,170 --> 00:06:10,850
and same because that's how we have formulated our prompt over here.

83
00:06:11,650 --> 00:06:18,210
So prompt engineering context engineering is really really important while we do all of these operations.

84
00:06:18,490 --> 00:06:24,730
So once we have all of these ready now, the last operation that we have to do to end this section is

85
00:06:24,730 --> 00:06:32,770
to write a simple prompt and pass it to our large language model and see how the response is going to

86
00:06:32,770 --> 00:06:35,330
come up, like how we are seeing over here.

87
00:06:35,570 --> 00:06:40,970
We are going to face some issue in terms of getting the responses, which I am sure which is going to

88
00:06:40,970 --> 00:06:43,290
happen, but I'm expecting that to happen.

89
00:06:43,290 --> 00:06:46,810
But I will show you how it is going to happen in our next lecture.

90
00:06:46,810 --> 00:06:52,010
And with that, we are going to end this section and then we are going to deal fixing them in our next

91
00:06:52,010 --> 00:06:53,450
section of this course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 12. Getting Alternative Locators in JSON Format (which can be used for Self Healing)

1
00:00:00,120 --> 00:00:00,920
All right.

2
00:00:00,920 --> 00:00:05,600
So now that we are going to write the prompt and we'll see how we could able to achieve that.

3
00:00:05,840 --> 00:00:09,640
So in order to do that I'm going to go to my writer ID one more time.

4
00:00:09,840 --> 00:00:13,560
And this is the same place the execution is currently stopped.

5
00:00:13,560 --> 00:00:15,600
So I'm just going to continue from there.

6
00:00:15,720 --> 00:00:18,000
So I'm going to write a simple prompt.

7
00:00:18,000 --> 00:00:18,560
Right.

8
00:00:18,640 --> 00:00:23,080
So let's write a small method over here so that it makes more sense.

9
00:00:23,360 --> 00:00:26,520
And then I'm going to see how we could able to achieve that.

10
00:00:26,520 --> 00:00:36,160
So I'm just going to say uh maybe get healed uh locator or something like that.

11
00:00:36,160 --> 00:00:41,000
And I'm going to pass the string of the page source.

12
00:00:41,360 --> 00:00:50,320
And then I'm also going to pass the string, uh, locator type and then string, uh, the original locator

13
00:00:50,320 --> 00:00:53,080
itself right over here.

14
00:00:53,080 --> 00:00:54,800
So I'm going to pass all of these.

15
00:00:54,840 --> 00:00:57,440
And now I'm going to write the prompt over here.

16
00:00:57,680 --> 00:01:03,920
And the way I'm going to write the prompt itself is I'm going to use the here symbol.

17
00:01:04,360 --> 00:01:06,120
Uh over here.

18
00:01:06,400 --> 00:01:08,440
This way in C sharp dotnet.

19
00:01:08,440 --> 00:01:16,360
You can write like a multi line strings as well, which is going to be way more easier in, in selenium.

20
00:01:16,360 --> 00:01:18,280
Like this is how you should do it.

21
00:01:18,320 --> 00:01:27,400
And over here uh I'm going to do this the web element with and I'm going to pass the locator type.

22
00:01:27,560 --> 00:01:38,400
And I'm going to say with locator type and it's locator which is going to be the original locator that

23
00:01:38,400 --> 00:01:45,080
we have got cannot be found in the page, something like this.

24
00:01:45,280 --> 00:01:54,680
And I want to say, uh, over here based on the current page source such as the alternative locator.

25
00:01:54,680 --> 00:01:58,640
So I'm just going to copy some of the code that I have already written.

26
00:01:58,720 --> 00:02:00,560
This is the prompt that I have already written.

27
00:02:00,560 --> 00:02:03,200
So I'm just going to do that over here.

28
00:02:03,200 --> 00:02:07,920
So I don't really need to retype it over here and see that this is the exact same thing that we were

29
00:02:07,920 --> 00:02:14,200
trying to do that before, but I have just formatted a bit over there and this is the prompt that we

30
00:02:14,200 --> 00:02:14,800
have got.

31
00:02:14,800 --> 00:02:15,320
Right.

32
00:02:15,560 --> 00:02:24,000
And now I'm just going to return this prompt so that it is going to be used within our code over here.

33
00:02:24,360 --> 00:02:28,960
So now I'm just going to maybe this is not even an asynchronous code.

34
00:02:28,960 --> 00:02:35,960
So maybe this is just an um string because this is just going to return, uh, not really an asynchronous

35
00:02:36,000 --> 00:02:36,840
operation there.

36
00:02:37,040 --> 00:02:41,440
So I'm just going to get the healed locator and we'll see how that actually works.

37
00:02:41,440 --> 00:02:48,880
So I'm just going to call this particular method over here var prompt is equal to and I'm going to say

38
00:02:48,880 --> 00:02:50,320
get healed locators.

39
00:02:50,480 --> 00:02:55,040
And I need to pass the page source which is going to be the page source that we have got which is this

40
00:02:55,040 --> 00:02:56,440
page source as you can see.

41
00:02:56,680 --> 00:02:59,960
And then I'm going to pass locator type and the locator.

42
00:02:59,960 --> 00:03:01,360
So I'm going to pass locator type.

43
00:03:01,800 --> 00:03:05,520
and the original error is going to be the locator value.

44
00:03:05,840 --> 00:03:10,560
So the moment I pass all of these, we are going to get the formulated prompt over here.

45
00:03:10,560 --> 00:03:14,560
And I will show you how it's going to look like, uh, which is this one.

46
00:03:15,480 --> 00:03:18,840
And let's get to this particular method.

47
00:03:19,320 --> 00:03:23,320
And hopefully oh, maybe this code is not even executed.

48
00:03:23,320 --> 00:03:23,720
Sorry.

49
00:03:23,720 --> 00:03:28,680
I'm going to stop all of these and rerun that because we have made the code change there.

50
00:03:28,920 --> 00:03:30,920
So definitely it is going to be different.

51
00:03:32,120 --> 00:03:36,440
And also we need to pass the prompt to our large language model.

52
00:03:36,440 --> 00:03:42,640
So I'm going to just say prompt over here and we'll see what is going to be the response.

53
00:03:43,400 --> 00:03:45,320
So let's try to debug it again.

54
00:03:47,400 --> 00:03:52,920
So this is the prompt that we are trying to formulate this time and see what response that we're going

55
00:03:52,960 --> 00:03:53,640
to get in.

56
00:03:54,720 --> 00:03:55,360
There we go.

57
00:03:56,240 --> 00:03:59,760
And we're going to remove the breakpoint from there because we have seen it working.

58
00:04:01,320 --> 00:04:02,440
And look at that.

59
00:04:02,480 --> 00:04:04,480
See this is the prompt that we are passing in.

60
00:04:04,480 --> 00:04:06,640
So if I'm going to expand this whole prompt.

61
00:04:06,760 --> 00:04:08,360
See it has prompt.

62
00:04:08,480 --> 00:04:16,080
It has passed the locator type as by dot link text and it's locator as login and cannot be found in

63
00:04:16,080 --> 00:04:19,000
the page based on the current page source.

64
00:04:19,200 --> 00:04:23,000
See that that's what we are going to pass in, which is amazing.

65
00:04:23,240 --> 00:04:30,600
And the page source, uh, is not being passed for some reason, which I'm expecting it to be passed

66
00:04:30,600 --> 00:04:31,040
there.

67
00:04:31,760 --> 00:04:32,840
Oh, look at that.

68
00:04:32,840 --> 00:04:35,520
There are two, uh, square brackets.

69
00:04:35,520 --> 00:04:37,800
That's the reason why the page source is not there.

70
00:04:38,280 --> 00:04:39,400
I think that's my bad.

71
00:04:39,440 --> 00:04:41,600
I should have passed the page source correctly.

72
00:04:42,440 --> 00:04:46,400
Let me save it and let me try to debug it again.

73
00:04:46,440 --> 00:04:48,720
Maybe it's because of the copy paste I missed.

74
00:04:49,080 --> 00:04:54,080
I see there are two braces there which is not going to work out in C sharp.

75
00:04:54,080 --> 00:04:56,000
And let me try doing it again.

76
00:04:56,520 --> 00:04:58,920
And I'm expecting the page source to be there.

77
00:04:58,960 --> 00:04:59,800
Ah look at that.

78
00:04:59,800 --> 00:05:03,160
Now I have got the full page source, which means it's correct.

79
00:05:03,480 --> 00:05:10,520
Now I'm going to pass this to our large language model, and I'm expecting the local large language

80
00:05:10,520 --> 00:05:11,880
model to be executed.

81
00:05:12,080 --> 00:05:15,160
And we'll see what response that we're going to get out of it.

82
00:05:15,200 --> 00:05:17,040
So let me try to run that.

83
00:05:17,560 --> 00:05:18,200
There we go.

84
00:05:18,520 --> 00:05:22,120
And we are going to get some response if I'm not wrong.

85
00:05:22,240 --> 00:05:22,560
There we go.

86
00:05:22,600 --> 00:05:24,360
We got a response text there.

87
00:05:24,560 --> 00:05:26,960
And if I'm going to view that look at that.

88
00:05:26,960 --> 00:05:32,320
We are going to get a response over here and see that this is the same exact response.

89
00:05:32,320 --> 00:05:32,800
Guys.

90
00:05:32,800 --> 00:05:39,920
You can see that we have got the ID, the name of the locator and the XPath to identify that login link.

91
00:05:40,200 --> 00:05:47,280
The CSS selector is this one and the class name is nothing and the link text is login perfect.

92
00:05:47,720 --> 00:05:53,360
So our prompt that we wrote is working as expected which is fabulous.

93
00:05:53,760 --> 00:05:58,840
And let's see if the Deserialization is going to happen over there and looks like it is.

94
00:05:59,040 --> 00:06:06,600
And we're going to get a response which is great, and we are going to get the response out from the

95
00:06:06,600 --> 00:06:07,040
result.

96
00:06:07,040 --> 00:06:16,160
And you see that we have got the same JSON, which we are actually getting out from the, uh, olama

97
00:06:16,160 --> 00:06:16,880
over here.

98
00:06:17,200 --> 00:06:19,720
And we're running the local large language model as well.

99
00:06:19,720 --> 00:06:21,440
So we got the same response.

100
00:06:21,440 --> 00:06:26,240
And if I'm going to print the console right line, it is going to be the same thing as well as you can

101
00:06:26,240 --> 00:06:28,520
see, which is pretty great.

102
00:06:28,560 --> 00:06:32,720
We did not see any failure as such, but it is working as expected.

103
00:06:32,720 --> 00:06:39,960
So this proves the point that we could able to prompt and we could able to chat, and we could get an

104
00:06:39,960 --> 00:06:45,160
alternative locator out from our large language model by passing the page source.

105
00:06:45,160 --> 00:06:47,480
So with this, this section ends.

106
00:06:47,480 --> 00:06:54,800
And now we are going to see how we can customize this alternative locator and create a self-healing

107
00:06:54,800 --> 00:06:55,560
element.

108
00:06:55,560 --> 00:07:02,520
If there happens, any failure in the locator which we are going to be doing starting our next section.


==================================================================================


section 6. Building Intelligent Locator Strategy using AI for Selenium


video 1.introduction

1
00:00:00,240 --> 00:00:02,320
Welcome to the next section of our course.

2
00:00:02,360 --> 00:00:06,160
And in this section we are going to talk about building locator strategies.

3
00:00:06,680 --> 00:00:10,040
This is one of the most fundamental part that we need to discuss.

4
00:00:10,040 --> 00:00:15,880
While we are going to start building a smart AI driven test automation intelligent test code.

5
00:00:15,960 --> 00:00:18,320
So let's see how we could able to achieve that.

6
00:00:18,720 --> 00:00:25,520
Well, so far until our last section, we discussed how we can create and format the prompts, which

7
00:00:25,520 --> 00:00:31,800
can be passed to the local large language model as well as the Cloud large language model and get the

8
00:00:31,800 --> 00:00:32,920
response out.

9
00:00:33,120 --> 00:00:36,200
And we saw how the response was coming out as a JSON.

10
00:00:36,200 --> 00:00:36,680
So far.

11
00:00:36,680 --> 00:00:38,880
So we have seen all of these operations.

12
00:00:39,120 --> 00:00:44,400
But the next step that we need to do right now is to see how we can deserialize the response, which

13
00:00:44,400 --> 00:00:51,720
is coming out as a JSON from these cloud LMS, which is this part that we need to see how we could able

14
00:00:51,720 --> 00:00:52,480
to achieve it.

15
00:00:53,080 --> 00:00:58,360
And once we have this deserialized value, we can do the rest of them, which I'm going to talk once

16
00:00:58,360 --> 00:00:59,160
we get there.

17
00:00:59,320 --> 00:01:00,400
So guess what?

18
00:01:00,440 --> 00:01:05,740
The next part that we need to focus right now is the deserialization of the JSON elements, which we

19
00:01:05,740 --> 00:01:08,380
get from the large language model itself.

20
00:01:08,580 --> 00:01:14,620
If you remember, in our last section, while we were trying to query or prompt the large language model

21
00:01:14,620 --> 00:01:21,700
for the locator type, locator value and page source, we got a response something like this from the

22
00:01:21,700 --> 00:01:22,980
large language model.

23
00:01:23,660 --> 00:01:27,940
And this particular value that we're getting, it is actually a JSON format.

24
00:01:27,940 --> 00:01:32,100
And it has got an ID name, XPath, CSS selectors.

25
00:01:32,620 --> 00:01:37,740
And then it's going to have as classname class name, link text and things.

26
00:01:37,740 --> 00:01:43,900
So we need to deserialize all these value into a class type something like this.

27
00:01:43,900 --> 00:01:47,420
So this is the locator suggestions class that we are going to build.

28
00:01:47,420 --> 00:01:52,620
And we're going to see how we can easily deserialize it, like how we did even before while we were

29
00:01:52,620 --> 00:01:56,860
trying to deserialize the response from a large language model.

30
00:01:56,860 --> 00:01:59,700
That's exactly what we are going to be doing over here.

31
00:01:59,940 --> 00:02:05,560
But why exactly are we doing the deserialization of this particular response that we are getting?

32
00:02:05,560 --> 00:02:07,640
It is still a JSON value, right?

33
00:02:07,680 --> 00:02:10,880
Why do we need to now deserialize it to this particular class type?

34
00:02:11,040 --> 00:02:12,400
Well guess what?

35
00:02:12,440 --> 00:02:20,440
Once we have the response in the strongly typed class, which means like a class with a name of locator

36
00:02:20,440 --> 00:02:21,600
suggestions over here.

37
00:02:21,640 --> 00:02:29,560
Like all these values that we wanted to store in, we can use the object for storing different locator

38
00:02:29,560 --> 00:02:32,440
strategies, performing action on these strategies.

39
00:02:32,440 --> 00:02:34,000
So we can do a lot of things.

40
00:02:34,000 --> 00:02:34,640
From there.

41
00:02:34,760 --> 00:02:38,000
You are going to understand everything once we get to that point.

42
00:02:38,000 --> 00:02:41,040
But for now, this is the most important thing that we have to do.

43
00:02:41,080 --> 00:02:49,400
We definitely need to store the locators from JSON to C sharp class type, so that we can do whatever

44
00:02:49,400 --> 00:02:52,000
that we can in the C sharp net world as well.

45
00:02:52,000 --> 00:02:57,880
As that said, let's see how we can achieve the deserialization part in this particular section.

46
00:02:58,080 --> 00:03:02,400
And followed by that, we are going to talk about the different locator strategies that we are going

47
00:03:02,400 --> 00:03:04,240
to implement in this section.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 2. Understanding Deserialization of response from LLMs

1
00:00:00,200 --> 00:00:01,040
All right.

2
00:00:01,040 --> 00:00:06,520
So now we are going to see how we can deserialize the response, which is coming out from the large

3
00:00:06,520 --> 00:00:09,880
language model into a class type.

4
00:00:10,040 --> 00:00:16,720
So just for this particular demonstration, I'm actually using the three quarter 480 billion parameter

5
00:00:16,720 --> 00:00:17,400
model.

6
00:00:17,400 --> 00:00:21,040
And you may wonder like why are you using the cloud based model over here?

7
00:00:21,160 --> 00:00:21,840
Guess what?

8
00:00:22,000 --> 00:00:26,840
Actually, just for this demonstration, I also wanted to show you that this is the model that you can

9
00:00:26,840 --> 00:00:32,800
use to perform quite some operation in much, much faster fashion because it's all going to be running

10
00:00:32,800 --> 00:00:33,720
on the cloud.

11
00:00:33,960 --> 00:00:40,200
And also this is going to be a free model which you can use for your testing purpose.

12
00:00:40,560 --> 00:00:42,920
I mean, locally really, but not in the company.

13
00:00:42,920 --> 00:00:47,000
You can't just use it, but at least for local testing, you can use this model.

14
00:00:47,000 --> 00:00:49,440
And this is a free model as well.

15
00:00:49,480 --> 00:00:53,280
I mean, you get a free SKU for some time while you are going to use them.

16
00:00:53,280 --> 00:00:55,400
That's why I am actually going to use that.

17
00:00:55,400 --> 00:00:59,560
So you can just go to our website over there.

18
00:00:59,760 --> 00:01:05,080
They have got the models which can now available in the cloud as well.

19
00:01:05,120 --> 00:01:06,240
So there are cloud models.

20
00:01:06,240 --> 00:01:10,420
If you go and click this cloud models over here, there are some details available and they have got

21
00:01:10,420 --> 00:01:13,860
models in these, uh, in the cloud way.

22
00:01:14,020 --> 00:01:19,340
So you can just go and select the models over here and see that they have got the cloud models.

23
00:01:19,340 --> 00:01:22,860
So you can use the cloud models as well, something like this.

24
00:01:22,860 --> 00:01:27,540
And you see that the number of billion parameter that it supports GPT Oasis has got 20 billion, which

25
00:01:27,540 --> 00:01:28,900
we can use locally.

26
00:01:28,900 --> 00:01:33,100
But they also have 120 billion parameter which can run in the cloud as well.

27
00:01:33,100 --> 00:01:36,260
The same thing goes for the rest of the models you are seeing over here.

28
00:01:36,260 --> 00:01:39,460
And the one I'm using is the three quarter model.

29
00:01:39,740 --> 00:01:43,180
And you just have to select this particular model, which is this one.

30
00:01:43,620 --> 00:01:46,900
Just copy this particular command and run it in your terminal.

31
00:01:46,900 --> 00:01:49,460
You are going to have this in your local machine.

32
00:01:49,460 --> 00:01:55,140
So if I'm going to go over here on my terminal and if I hit run, you see that now it's already connected

33
00:01:55,140 --> 00:01:57,620
to a cloud based model for me over there.

34
00:01:57,620 --> 00:02:02,940
And this is going to be way faster as well because this is running on the cloud and that's why it is

35
00:02:02,940 --> 00:02:04,420
going to be super duper faster.

36
00:02:04,420 --> 00:02:07,780
So that's the power of this particular, uh, large language model.

37
00:02:07,780 --> 00:02:10,500
And I'm just going to use this particular model over here.

38
00:02:10,540 --> 00:02:12,420
There is no setting needed to be changed.

39
00:02:12,420 --> 00:02:15,060
It's going to be still remain the provider as local.

40
00:02:15,060 --> 00:02:17,100
And the model is going to be this particular model.

41
00:02:17,100 --> 00:02:18,790
And you are pretty much done with that.

42
00:02:18,790 --> 00:02:22,830
So that's the only change I made while you guys were not here around.

43
00:02:22,990 --> 00:02:29,110
Well, as that said, I'm going to see how we can start doing the deserialization of the response from

44
00:02:29,110 --> 00:02:30,270
the AI model.

45
00:02:30,270 --> 00:02:37,190
So if we again try to put a breakpoint over here and let's try to run this test just to show you what

46
00:02:37,190 --> 00:02:39,270
is going to be the JSON.

47
00:02:39,270 --> 00:02:44,510
If you have forgotten, like how we were doing all of these in our last section of this course, you

48
00:02:44,510 --> 00:02:50,070
will realize that the data that we are getting is essentially a JSON itself.

49
00:02:50,070 --> 00:02:55,750
So you see that now the speed will be like super duper fast because running on the cloud see so fast,

50
00:02:56,150 --> 00:02:57,630
it just came instantly.

51
00:02:57,910 --> 00:02:59,150
And here we go.

52
00:02:59,190 --> 00:03:02,390
We have the JSON response over here.

53
00:03:02,390 --> 00:03:07,310
So this response is what I wanted to deserialize to a class type.

54
00:03:07,670 --> 00:03:08,190
Guess what?

55
00:03:08,190 --> 00:03:11,670
You can just copy this particular JSON value.

56
00:03:11,910 --> 00:03:17,870
And if you want to convert this to a class type in C sharp dotnet, you can go to your Google Chrome

57
00:03:17,870 --> 00:03:23,950
over here, search for JSON to C sharp class, something like that.

58
00:03:23,950 --> 00:03:28,410
You will see there are so many websites available to do it, and one of the website is to convert JSON

59
00:03:28,410 --> 00:03:29,050
to C sharp.

60
00:03:29,050 --> 00:03:32,970
Over here we can paste the JSON and hit convert.

61
00:03:33,130 --> 00:03:38,370
It is going to convert the uh, the entire JSON into a class type.

62
00:03:38,410 --> 00:03:39,130
Look at that.

63
00:03:39,170 --> 00:03:40,290
It's very straightforward.

64
00:03:40,290 --> 00:03:41,450
You can do that as well.

65
00:03:41,770 --> 00:03:50,450
If you wanted to do this way you can just copy this particular class over here to, uh, the place where

66
00:03:50,450 --> 00:03:51,090
you want it to.

67
00:03:51,090 --> 00:03:51,730
Really.

68
00:03:51,730 --> 00:03:54,770
So let's say I want to create it, uh, over here.

69
00:03:54,770 --> 00:04:00,570
So I'm going to call this as, uh, locator, uh, suggestions, something like that.

70
00:04:00,690 --> 00:04:02,530
Uh, and then I'm going to hit enter.

71
00:04:02,530 --> 00:04:04,330
So that's going to create that class for me.

72
00:04:04,610 --> 00:04:06,650
And I'm going to paste this particular class.

73
00:04:06,650 --> 00:04:09,530
Let's remove the class because we already have the class name there.

74
00:04:10,050 --> 00:04:11,850
And boom look at that.

75
00:04:12,170 --> 00:04:14,530
That's all we have got already.

76
00:04:14,530 --> 00:04:21,730
So we already have got the class that we needed which can be used for doing the, uh, I mean, deserialization

77
00:04:21,770 --> 00:04:22,490
operation.

78
00:04:22,850 --> 00:04:25,330
So this is what you have to do.

79
00:04:25,370 --> 00:04:29,730
And once you have it, all you have to do it is, um, you can just do it.

80
00:04:29,770 --> 00:04:32,530
Use it for the dieselisation.

81
00:04:32,530 --> 00:04:34,090
I just forgot one more thing.

82
00:04:34,290 --> 00:04:39,980
Uh, we can call this, Or we can put this under a folder called as a model if we wanted to.

83
00:04:40,020 --> 00:04:45,420
That way all the models like because these are like a model classes which can sit under that particular

84
00:04:45,420 --> 00:04:45,940
folder.

85
00:04:45,940 --> 00:04:49,220
You can do that as well, which is a good practice to do it.

86
00:04:49,260 --> 00:04:55,500
But what if in future you're going to interact with large language model and get another kind of responses

87
00:04:55,500 --> 00:04:56,300
all the time?

88
00:04:56,460 --> 00:05:00,340
You can also store that in a class type in a models folder.

89
00:05:00,540 --> 00:05:02,420
It's all up to you how you want to do it.

90
00:05:02,460 --> 00:05:03,660
But guess what?

91
00:05:03,700 --> 00:05:10,340
It's something you have to think seriously while you write the code in a more better aligned fashion.

92
00:05:10,380 --> 00:05:11,020
Like a framework.

93
00:05:11,020 --> 00:05:13,500
To be honest, that's what developers does as well.

94
00:05:13,660 --> 00:05:16,700
So yeah, I'm just going to leave this with you guys.

95
00:05:16,740 --> 00:05:20,020
Like how you want to figure it out, but I'm just going to leave it as it is.

96
00:05:20,060 --> 00:05:25,980
And I'm going to go over here and I'm going to start doing the deserialization within my test.

97
00:05:26,100 --> 00:05:31,500
But before I do that, I'm going to let you to try it out and see how you could able to achieve the

98
00:05:31,500 --> 00:05:32,620
Dieselisation.

99
00:05:32,620 --> 00:05:39,340
I know it's very straightforward because we have did many times, uh, in our code, which I'm not really

100
00:05:39,340 --> 00:05:42,900
going to show you at all, I will let you to do it.

101
00:05:44,020 --> 00:05:45,300
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 3. Deserialize LLM Response to Class Type

1
00:00:00,120 --> 00:00:00,680
All right.

2
00:00:00,680 --> 00:00:05,080
So hopefully you have already done how things are going to happen there.

3
00:00:05,080 --> 00:00:08,440
So I'm just going to start writing the code right now.

4
00:00:08,440 --> 00:00:10,880
So I'm going to go to the enhanced test over here.

5
00:00:10,880 --> 00:00:12,640
And we're going to do the Deserialization.

6
00:00:12,680 --> 00:00:18,040
You remember the response was coming as uh, coming to us as a JSON value there, and now we need to

7
00:00:18,040 --> 00:00:19,800
do the deserialization part.

8
00:00:19,800 --> 00:00:20,840
So how do we do it?

9
00:00:20,840 --> 00:00:22,200
Well, guess what?

10
00:00:22,240 --> 00:00:28,160
As I told you in our last videos, you have already done that many times.

11
00:00:28,200 --> 00:00:29,240
Something like this.

12
00:00:29,240 --> 00:00:31,160
So I'm going to do the exact similar operation.

13
00:00:31,160 --> 00:00:34,400
This time I'm going to copy this particular code from line number 36.

14
00:00:34,720 --> 00:00:40,240
And I'm going to go to the enhanced test over here, and I'm going to do a deserialization.

15
00:00:40,240 --> 00:00:46,880
So let's say uh var uh and then I'm going to say locate our strategy.

16
00:00:50,080 --> 00:00:54,240
To G uh as this particular code over here.

17
00:00:54,240 --> 00:01:02,590
And instead of the JSON element we are going to use the locator, uh, suggestions class file, which

18
00:01:02,590 --> 00:01:04,510
is the one that we created in our last lecture.

19
00:01:04,950 --> 00:01:09,270
And for the response text I'm going to get the, uh, result.

20
00:01:09,310 --> 00:01:13,110
Probably we just say response uh, here.

21
00:01:13,470 --> 00:01:15,910
This is basically a response from the large language model.

22
00:01:15,950 --> 00:01:16,110
Right.

23
00:01:16,150 --> 00:01:18,190
So I'm going to pass that particular response over here.

24
00:01:18,550 --> 00:01:20,430
And this is going to be the look at our strategy.

25
00:01:20,630 --> 00:01:25,430
And because we have deserialized and now we can just say look at our strategy Dot.

26
00:01:25,590 --> 00:01:29,630
See we get all the different locators from this particular class file.

27
00:01:30,310 --> 00:01:31,950
Um, which is great.

28
00:01:31,950 --> 00:01:35,670
So let's just use the XPath over here and see what is going to be the result.

29
00:01:35,910 --> 00:01:44,990
Uh, so I'm going to go debug this test one more time and see what's going to be the response generated.

30
00:01:45,310 --> 00:01:48,950
Uh, and if are we really getting that Deserialized.

31
00:01:49,350 --> 00:01:52,470
See, it's going to run through the large language model.

32
00:01:52,510 --> 00:01:54,510
It's going to get it immediately for us.

33
00:01:54,710 --> 00:01:57,150
And you see that the response is coming up.

34
00:01:57,150 --> 00:01:59,190
And now I'm going to see the Deserialization.

35
00:01:59,230 --> 00:02:00,590
Oh that's done.

36
00:02:00,630 --> 00:02:01,630
Look at that.

37
00:02:01,950 --> 00:02:06,700
We have got all of these deserialized amazingly over here.

38
00:02:07,100 --> 00:02:13,380
See, class name is nothing but class letter CSS selector is there ID is there link text is there name

39
00:02:13,380 --> 00:02:15,540
is nothing, but XPath is also there.

40
00:02:15,540 --> 00:02:18,540
So if you're going to go and see the XPath you get this particular XPath.

41
00:02:19,180 --> 00:02:22,740
Now you have already got the idea right.

42
00:02:22,740 --> 00:02:29,460
So you have found the alternative locator right now for any given locator.

43
00:02:29,460 --> 00:02:37,260
So if you're going to pass the locator as for example login over here you can get the alternative locator

44
00:02:37,420 --> 00:02:39,540
something like this with an XPath.

45
00:02:39,820 --> 00:02:40,460
This.

46
00:02:40,460 --> 00:02:48,140
To be honest I have been struggling for past 20 years for that matter to make this happen because I

47
00:02:48,140 --> 00:02:51,860
used to build these kinds of framework for the companies I work for.

48
00:02:51,860 --> 00:02:54,260
I do a lot of consulting with different companies.

49
00:02:54,380 --> 00:03:01,340
I used to build this kind of strategy manually by having all the locators being recorded, and then

50
00:03:01,380 --> 00:03:06,970
have them as a collection, and then we can use that as a collections to iterate through every single

51
00:03:06,970 --> 00:03:07,290
time.

52
00:03:07,290 --> 00:03:12,050
If any one of the locator matches from that collection and it goes and work.

53
00:03:12,050 --> 00:03:17,410
That's how the auto healing was done by me long time before, and I have been using that particular

54
00:03:17,570 --> 00:03:18,410
operation.

55
00:03:18,410 --> 00:03:25,570
But now, thanks to AI, because now this AI is going to get the page source in real time, and it is

56
00:03:25,570 --> 00:03:31,090
going to find the locators alternative in real time, and then it is identifying it for us.

57
00:03:31,290 --> 00:03:32,250
This is amazing.

58
00:03:32,930 --> 00:03:38,050
And now you may ask a question here saying hey Karthik, we have got the locators here, but there are

59
00:03:38,050 --> 00:03:39,610
some locators which are missing.

60
00:03:39,650 --> 00:03:44,090
Like for example class name is null and similarly the name is null over here.

61
00:03:44,090 --> 00:03:45,330
So what is going to happen?

62
00:03:45,330 --> 00:03:49,210
But still we have got the CSS selector and id and link text there.

63
00:03:49,530 --> 00:03:51,130
So what can we do on that.

64
00:03:51,170 --> 00:03:51,890
Guess what.

65
00:03:51,930 --> 00:03:58,690
We are going to build the locator strategy in such a way that the logic is going to iterate through

66
00:03:58,690 --> 00:04:07,400
all the locators, and it is going to run the, uh, run the execution for the locator Are in every

67
00:04:07,400 --> 00:04:08,960
single type that we have.

68
00:04:09,000 --> 00:04:14,280
If any one of them match in the order, then we are going to operate on that.

69
00:04:14,280 --> 00:04:16,520
If any one of them fails, we mark them.

70
00:04:16,520 --> 00:04:22,040
The locator strategy has failed, and then we hop on to the next one, and then we keep moving on from

71
00:04:22,040 --> 00:04:22,360
there.

72
00:04:22,400 --> 00:04:23,840
This is how we are going to work.

73
00:04:23,840 --> 00:04:28,640
So we are going to identify any one of these locator and see if any one of them really works.

74
00:04:28,640 --> 00:04:33,280
If none of them works, then which means there is something really wrong with the Dom and then the test

75
00:04:33,280 --> 00:04:34,600
is eventually going to fail.

76
00:04:34,840 --> 00:04:41,120
But now you see that it's not only just a waiting mechanism, it's a locator identification mechanism

77
00:04:41,120 --> 00:04:44,800
that we have found over here for the locator that you have got.

78
00:04:44,800 --> 00:04:48,840
This is an alternative locator that you have got, which is fabulous.

79
00:04:49,200 --> 00:04:50,080
We got that.

80
00:04:50,360 --> 00:04:56,760
And now we are going to see how we can build the locator strategy, uh, which is the workflow, to

81
00:04:56,760 --> 00:05:00,480
be honest, using the locator alternatives that we have got.

82
00:05:00,680 --> 00:05:01,960
That's the big one.

83
00:05:01,960 --> 00:05:06,680
But you already got the idea how we are going to be building from this on.

84
00:05:06,960 --> 00:05:08,480
Catch you in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 4. Understanding building of Locator Strategy of each phase


1
00:00:00,120 --> 00:00:01,240
All right.

2
00:00:01,280 --> 00:00:08,440
Now we are going to see how we can start building the locator strategy from this particular lecture.

3
00:00:08,440 --> 00:00:10,280
So this is a big process to be honest.

4
00:00:10,560 --> 00:00:16,720
But it is going to be really, really an amazingly cakewalk style that I have built this course so that

5
00:00:16,720 --> 00:00:18,520
you can understand things more clearly.

6
00:00:18,720 --> 00:00:24,360
I know for the first time it feels a bit more awkward because we have not really used to building these

7
00:00:24,360 --> 00:00:29,680
kind of strategies before in our automation, but thanks to AI, now they are letting us to do some

8
00:00:29,680 --> 00:00:36,080
of the amazing operations that we couldn't have even thought about before, like a couple of years from

9
00:00:36,080 --> 00:00:36,480
now.

10
00:00:36,560 --> 00:00:38,640
But now everything is possible.

11
00:00:38,840 --> 00:00:40,760
Thanks to AI for making this happen.

12
00:00:40,800 --> 00:00:48,120
That's the reason why we are going to take a bit of hard effort to make this auto healing operation.

13
00:00:48,120 --> 00:00:49,240
Just stick with me.

14
00:00:49,360 --> 00:00:55,480
If you think that this particular lectures are going way faster, try to, you know, run this in slow

15
00:00:55,760 --> 00:01:02,160
mode or maybe re watch the same video one more time, it will start making more sense, but I will try

16
00:01:02,160 --> 00:01:07,920
to make sure that I will deliver this particular ideas as clean as possible.

17
00:01:08,160 --> 00:01:13,640
Well, as I said, we are going to discuss about this locator strategy approach from this particular

18
00:01:13,640 --> 00:01:14,280
lecture.

19
00:01:14,280 --> 00:01:17,320
So we have completed these many phases so far.

20
00:01:17,520 --> 00:01:20,680
And now we are in this particular phase over here.

21
00:01:20,680 --> 00:01:22,400
And this is a big iteration process.

22
00:01:22,400 --> 00:01:24,920
That is the reason why I have got this iteration over here.

23
00:01:25,160 --> 00:01:27,960
And then we're going to use the locator which is going to be very, very straightforward.

24
00:01:27,960 --> 00:01:34,280
So this part is your part which you're going to be spending some time to understand and think and how

25
00:01:34,280 --> 00:01:34,960
it works.

26
00:01:35,720 --> 00:01:41,120
But once you get it, you are there to make everything happen way more faster.

27
00:01:41,400 --> 00:01:46,520
Well, as that said, let's understand what is this select locator strategy.

28
00:01:46,880 --> 00:01:48,360
Well, you know what?

29
00:01:48,400 --> 00:01:55,680
I have built a whole big diagram over here to explain you how we are going to make this process happen.

30
00:01:55,680 --> 00:02:01,840
And this is the diagram which was made, diagram generated by the, uh, by the class while writing

31
00:02:01,840 --> 00:02:02,440
the code.

32
00:02:02,440 --> 00:02:07,120
But I don't want to go through this process, because if I'm going to show you this particular diagram,

33
00:02:07,120 --> 00:02:08,920
it's going to be a bit more confusing.

34
00:02:08,920 --> 00:02:13,800
So I want to dissect this particular diagram in a more and more simpler fashion.

35
00:02:13,960 --> 00:02:16,360
Well I'm going to say this one.

36
00:02:16,360 --> 00:02:19,680
So I'm going to even split that particular diagram into phases.

37
00:02:19,680 --> 00:02:22,080
So I'm going to split that into two phases.

38
00:02:22,080 --> 00:02:27,800
So this is the first phase one that we are going to build for the locator strategy that we have got

39
00:02:27,800 --> 00:02:34,960
over here in this particular phase one, you can see that we are going to build a locator strategy method

40
00:02:35,520 --> 00:02:41,760
where in this particular method we are going to first call a method called as find locator in page object

41
00:02:41,760 --> 00:02:42,280
model.

42
00:02:42,280 --> 00:02:43,560
So you know what.

43
00:02:43,560 --> 00:02:48,640
In our code we know that there is going to be a page object model code over here, which is the home

44
00:02:48,640 --> 00:02:49,200
page.

45
00:02:49,200 --> 00:02:54,960
So you are going to pass the page to uh to your test, uh, over here.

46
00:02:54,960 --> 00:02:58,760
And then you're going to be invoking it, and then you're going to see whether that works or not If

47
00:02:58,760 --> 00:03:05,120
it works, then yes, it is going to perform the operation using selenium and everything is going to

48
00:03:05,120 --> 00:03:05,800
be fine.

49
00:03:05,840 --> 00:03:06,520
Amazing.

50
00:03:06,520 --> 00:03:08,800
So it's going to do that on the Dom for you.

51
00:03:09,680 --> 00:03:17,000
But if the locator in the page object model is obsolete or failing for some reason, then it is going

52
00:03:17,040 --> 00:03:19,600
to go and check the alternative locators.

53
00:03:19,640 --> 00:03:27,680
We have did that many times already, uh, to call the healed locator like a prompt and then uh, get

54
00:03:27,680 --> 00:03:33,000
the compilation, uh, method where we are going to get the response, where we're going to get the

55
00:03:33,000 --> 00:03:38,320
alternative locator, which is great, but it's all just sitting in one single method.

56
00:03:38,320 --> 00:03:43,880
We are going to split them into isolated method pretty soon in this particular section.

57
00:03:43,880 --> 00:03:46,840
But yes, it is going to go and check the alternative locators.

58
00:03:46,840 --> 00:03:51,840
So there is going to be a collection of alternative locators that we just found.

59
00:03:51,880 --> 00:03:52,200
Right.

60
00:03:52,240 --> 00:03:57,920
Because you know that in this particular code, as you saw, we have got different locator Are strategies

61
00:03:57,920 --> 00:03:58,720
that we have.

62
00:03:58,920 --> 00:04:02,480
So we need to go and choose any one of the locator strategy from this.

63
00:04:02,480 --> 00:04:08,800
So we need to have some other means to get any one of the locator from here.

64
00:04:08,800 --> 00:04:12,320
That is what is this check alternative locators method.

65
00:04:12,560 --> 00:04:15,400
So we are going to see if there is any alternative locator.

66
00:04:15,560 --> 00:04:16,240
You know what.

67
00:04:16,320 --> 00:04:20,600
For the very first time there is not going to be any alternative locators.

68
00:04:20,640 --> 00:04:20,840
Right.

69
00:04:20,880 --> 00:04:24,000
Because we have not even called AI so far.

70
00:04:24,160 --> 00:04:26,640
This is going to run the test and see if that works.

71
00:04:26,640 --> 00:04:29,520
If it fails, then it's going to go and call this guy.

72
00:04:30,400 --> 00:04:35,120
So this alternative locator is not going to be there for the first time.

73
00:04:35,120 --> 00:04:41,720
So it is going to go and invoke the AI healing process to find the alternative locator, which is this

74
00:04:41,720 --> 00:04:42,080
code.

75
00:04:42,080 --> 00:04:45,400
As you are seeing over here, that is what going to happen over here.

76
00:04:45,680 --> 00:04:49,640
And this AI healing process is going to find all the locators.

77
00:04:50,040 --> 00:04:54,120
And then it is going to store that in some sort of collections or something.

78
00:04:54,360 --> 00:05:01,410
And then it is going to again In invoke the locator strategy process, which is going to again do the

79
00:05:01,410 --> 00:05:02,170
same operation.

80
00:05:02,170 --> 00:05:05,570
So it's going to go and call one more time the find locators in Pom.

81
00:05:06,010 --> 00:05:08,290
Because the locator is still going to be wrong.

82
00:05:08,330 --> 00:05:09,410
It's going to fail.

83
00:05:09,410 --> 00:05:11,890
And then it's going to go and check the alternative locators.

84
00:05:12,050 --> 00:05:16,410
This time you are going to have an alternative locator in the collection.

85
00:05:16,450 --> 00:05:21,330
The particular DB because this particular AI has already found one.

86
00:05:21,330 --> 00:05:25,570
So it is going to use that locator and then perform an operation.

87
00:05:25,570 --> 00:05:27,370
And the test is just going to pass.

88
00:05:28,210 --> 00:05:29,370
This is what is going to happen.

89
00:05:30,210 --> 00:05:37,690
But if the locator still fails, which is something like for instance, uh, we are using the class

90
00:05:37,690 --> 00:05:41,530
name for the first time and we see that the class name is empty.

91
00:05:41,690 --> 00:05:43,770
So definitely this guy is going to fail.

92
00:05:43,770 --> 00:05:45,970
So it is going to invoke the AI healing process.

93
00:05:45,970 --> 00:05:48,770
But AI healing process will not be invoked directly.

94
00:05:48,770 --> 00:05:52,210
Rather it is going to call the collections there to make that happen.

95
00:05:52,330 --> 00:05:53,690
This diagram could be changed.

96
00:05:53,730 --> 00:05:57,330
I just have to call the collections there instead of a healing process.

97
00:05:57,650 --> 00:06:02,090
Uh, this is going to be the last step in this whole execution to get through there.

98
00:06:02,210 --> 00:06:03,850
But you got the idea, right.

99
00:06:03,890 --> 00:06:07,410
This is what is going to happen in the locator strategy, the phase one.

100
00:06:07,570 --> 00:06:10,770
You are going to first call the locator strategy method.

101
00:06:10,810 --> 00:06:13,410
It's going to find the locators in the page object model.

102
00:06:13,570 --> 00:06:18,170
If the locator in the page model is working it's going to perform the operation on the UI.

103
00:06:18,330 --> 00:06:20,770
If not it's going to check the locator.

104
00:06:20,970 --> 00:06:22,850
It will be empty for the first time.

105
00:06:22,850 --> 00:06:25,010
So it's going to call the AI healing process.

106
00:06:25,410 --> 00:06:28,610
And then it's going to do call the same method one more time.

107
00:06:28,850 --> 00:06:30,090
Do the same process.

108
00:06:30,130 --> 00:06:31,890
It's going to find an locator.

109
00:06:31,890 --> 00:06:33,610
And then it is going to run through that.

110
00:06:33,610 --> 00:06:36,450
So this is how things are going to work right.

111
00:06:36,490 --> 00:06:38,850
This is the phase one process.

112
00:06:39,090 --> 00:06:42,090
This is already too much to take and digest.

113
00:06:42,130 --> 00:06:47,970
I highly recommend you to rewatch this video one more time if it doesn't make any sense.

114
00:06:47,970 --> 00:06:49,810
Or maybe I'm talking too fast.

115
00:06:50,330 --> 00:06:56,890
Sorry about that, but this is the most slowest way I can really think of talking, but I think I have

116
00:06:56,890 --> 00:07:02,130
made this diagram as clear as possible for you to understand this.

117
00:07:02,130 --> 00:07:05,970
This is phase one, and the next one is the phase two approach.

118
00:07:06,290 --> 00:07:13,250
Or this is even more intelligent phase where what happens if the alternative locator, uh, is also

119
00:07:13,250 --> 00:07:14,530
going to fail, right?

120
00:07:14,570 --> 00:07:20,370
As I told you, if the alternate locator completely fails, uh, from the locator collection that we

121
00:07:20,370 --> 00:07:26,650
have, then it's going to reinvoke the AI healing process one more time to see if the, uh, if the

122
00:07:26,650 --> 00:07:34,290
locator that we have got over there is, um, is can be found in some other mean, if the AI is still

123
00:07:34,290 --> 00:07:38,530
going to think that this is what is the locator that you have got, then it is going to completely give

124
00:07:38,530 --> 00:07:40,210
up and then it is going to fail.

125
00:07:40,210 --> 00:07:46,890
So this there is going to be like one more path over here, which is this one where if the locator could

126
00:07:46,890 --> 00:07:52,210
not be found by the AI anymore, then it is going to completely fail and your test is eventually going

127
00:07:52,210 --> 00:07:56,170
to fail because there is something seriously wrong with your Dom.

128
00:07:56,250 --> 00:07:58,970
So we are not going to do any of the process.

129
00:07:58,970 --> 00:08:00,410
So this is the phase two.

130
00:08:00,450 --> 00:08:03,330
I mean, there is no big difference between the phase one and phase two.

131
00:08:03,650 --> 00:08:05,650
They are quite exactly the same.

132
00:08:05,650 --> 00:08:07,570
Just that we have got an alternative look here.

133
00:08:07,570 --> 00:08:08,730
Our failures as well.

134
00:08:09,330 --> 00:08:09,930
Right.

135
00:08:10,410 --> 00:08:11,730
These are the phases.

136
00:08:11,930 --> 00:08:19,370
And once you have everything in this place, you can just picture them all using this big, gigantic

137
00:08:19,410 --> 00:08:23,050
approach that we were talking uh, before, which is this one.

138
00:08:23,050 --> 00:08:26,530
And that is what is really going to happen over there, right?

139
00:08:26,690 --> 00:08:32,890
So I am going to show you how we are going to approach all of these operation face by face and make

140
00:08:32,890 --> 00:08:33,930
this happen.

141
00:08:34,090 --> 00:08:39,330
So we are going to start writing what is called as the locator strategy method first and perform all

142
00:08:39,330 --> 00:08:40,370
these operation.

143
00:08:40,410 --> 00:08:41,810
It is going to be a long journey.

144
00:08:41,850 --> 00:08:42,930
Just stick with me.

145
00:08:42,930 --> 00:08:47,810
But we are going to see the light at the end of the tunnel, which is really, really bright and you

146
00:08:47,850 --> 00:08:53,650
are going to be fascinated how everything is going to be coming up together once you bring all the puzzles

147
00:08:53,650 --> 00:08:54,370
together.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 5. Creating CurrentLocatorStrategy which gets locator from Selenium POM


1
00:00:00,200 --> 00:00:01,120
All right.

2
00:00:01,120 --> 00:00:10,160
So now we are going to see how we can start building the self-healing elements that we can find for

3
00:00:10,160 --> 00:00:12,560
our, uh, locator that we have got.

4
00:00:12,560 --> 00:00:17,960
So we can say self-healing element or self-healing locator, whatever name that you prefer.

5
00:00:17,960 --> 00:00:22,000
You can have that over there and it is going to perform this operation.

6
00:00:22,000 --> 00:00:27,760
So in order to achieve that, we are going to bring some of the codes that we have split and put them

7
00:00:27,760 --> 00:00:28,640
all over here.

8
00:00:28,640 --> 00:00:31,520
So we need to bring them up into like a method.

9
00:00:31,520 --> 00:00:36,760
And then we are going to just make it like a more like a library fashion so that it becomes more reusable

10
00:00:36,760 --> 00:00:41,200
because we can't have all of these, uh, over here, uh, in this particular code.

11
00:00:41,240 --> 00:00:41,720
Right.

12
00:00:41,760 --> 00:00:45,480
So I'm going to stop this execution that we are doing in our last lecture.

13
00:00:45,600 --> 00:00:50,840
And over here I'm going to go to the utilities folder and I'm going to create a class.

14
00:00:50,840 --> 00:00:56,320
I'm going to call this as self healing locators.

15
00:00:56,680 --> 00:00:57,320
Right.

16
00:00:57,320 --> 00:01:02,960
And this particular class over here I'm going to start performing the self-healing operation.

17
00:01:02,960 --> 00:01:05,520
So the idea is very, very simple.

18
00:01:05,760 --> 00:01:09,760
In this particular class I'm going to create a constructor over here.

19
00:01:09,960 --> 00:01:17,400
And I'm going to pass some elements, which is like I'm going to pass the WebDriver because I need the

20
00:01:17,440 --> 00:01:20,200
driver to be in place just for selenium driver.

21
00:01:20,520 --> 00:01:28,640
And I'm also going to pass the locator over here, which is going to be the primary locator for that

22
00:01:28,640 --> 00:01:29,000
matter.

23
00:01:29,000 --> 00:01:30,840
So I'm going to say primary locator.

24
00:01:30,840 --> 00:01:35,640
So these are the two things I really need which I'm going to pass from the page object model code.

25
00:01:35,640 --> 00:01:37,640
If you remember the bi elements right.

26
00:01:37,680 --> 00:01:40,080
This is what I'm very much interested in.

27
00:01:40,800 --> 00:01:43,200
So those are the two things I'm going to pass in over here.

28
00:01:43,640 --> 00:01:45,160
And I'm going to initialize them.

29
00:01:45,160 --> 00:01:48,320
So you can do it in C sharp by just hitting command enter.

30
00:01:48,360 --> 00:01:50,600
This is going to bring you up this particular option.

31
00:01:50,600 --> 00:01:54,840
Or you can also click this particular bulb symbol to bring the same exact thing.

32
00:01:54,880 --> 00:01:57,240
They both are exactly the same one right.

33
00:01:57,280 --> 00:02:05,160
And I'm going to create a read only field for both of them because I need them to be there in place.

34
00:02:05,160 --> 00:02:08,560
So read only fields are being created, which is awesome.

35
00:02:08,880 --> 00:02:15,560
And we are also going to create some of these strategies over there.

36
00:02:15,760 --> 00:02:21,080
I know it's going to be confusing for the first time, so I'm not going to talk about that yet, but

37
00:02:21,080 --> 00:02:27,120
I'm going to create some method to understand or make you understand how you can create those strategy.

38
00:02:27,160 --> 00:02:35,520
See, essentially we are going to, first of all, uh, identify the locator using the current working

39
00:02:35,520 --> 00:02:40,240
locator, which is nothing but the locator which is coming up from this particular page object model

40
00:02:40,240 --> 00:02:40,680
code.

41
00:02:41,160 --> 00:02:41,880
Right.

42
00:02:41,880 --> 00:02:48,680
So in order to achieve that, I am going to, uh, first of all, use the, uh, try.

43
00:02:51,040 --> 00:02:54,280
Current strategy or current finding strategy.

44
00:02:54,280 --> 00:02:59,640
So in order to do that, I'm going to say I'm going to create a method over here.

45
00:02:59,640 --> 00:03:05,240
I'm going to call this as uh public I element over here.

46
00:03:05,320 --> 00:03:09,920
I'm going to say try find with current strategy.

47
00:03:09,920 --> 00:03:16,400
So this is the current strategy which I'm going to be implementing, uh, or using in order to find

48
00:03:16,440 --> 00:03:17,200
the element.

49
00:03:17,200 --> 00:03:19,320
So I'm going to write this in a try catch block.

50
00:03:19,320 --> 00:03:22,400
Because what if that particular element does not work.

51
00:03:22,400 --> 00:03:25,720
So I'm going to say uh, no such element exception.

52
00:03:25,720 --> 00:03:27,600
I'm just going to throw that throw that as well.

53
00:03:27,800 --> 00:03:33,000
And I'm going to return probably null if that's going to happen.

54
00:03:33,000 --> 00:03:33,520
Right.

55
00:03:33,600 --> 00:03:35,440
So I'm just because I'm returning null.

56
00:03:35,440 --> 00:03:40,760
So I'm just going to make the question mark here like nullable type so that it's going to return null

57
00:03:40,800 --> 00:03:41,320
as well.

58
00:03:41,600 --> 00:03:48,000
And over here I'm going to use the driver with the find element of the locator.

59
00:03:48,200 --> 00:03:53,160
But now you may ask hey Karthik, how am I going to pass the locator over here?

60
00:03:53,160 --> 00:03:58,880
Because we don't even have the locator that we can pass in to this particular, uh, method.

61
00:03:58,880 --> 00:04:04,160
You remember we have got the primary locators that we have passed in over here.

62
00:04:04,360 --> 00:04:12,690
We can pass that, uh, as well, but for the naming convention, I'm just going to keep them as the

63
00:04:12,690 --> 00:04:16,730
strategy because it's all going to be working on the strategy level.

64
00:04:16,730 --> 00:04:22,370
So I'm going to say current strategy, something like this.

65
00:04:22,570 --> 00:04:27,490
And this current strategy is going to hold the primary locator that we have got.

66
00:04:27,690 --> 00:04:28,290
Right.

67
00:04:28,330 --> 00:04:29,370
That's the strategy.

68
00:04:29,410 --> 00:04:33,650
We are going to use this current strategy quite a lot uh, this time.

69
00:04:33,650 --> 00:04:39,090
So I'm not even going to make this as read only because it is something I will be changing, uh, as

70
00:04:39,090 --> 00:04:39,610
well.

71
00:04:39,610 --> 00:04:44,530
So I'm going to hold this current strategy over here.

72
00:04:44,530 --> 00:04:48,010
And this is the strategy that we have got over here.

73
00:04:48,010 --> 00:04:51,330
So this is going to be the try find current strategy.

74
00:04:52,090 --> 00:04:54,450
So we are going to do this.

75
00:04:54,490 --> 00:04:57,090
We are going to create a method over here.

76
00:04:57,210 --> 00:05:03,410
And I'm going to call this method as probably an asynchronous operation that we are going to be doing.

77
00:05:03,570 --> 00:05:10,050
And I'm going to return an uh IB element after we find that particular element.

78
00:05:10,050 --> 00:05:15,090
So I'm going to create a method over here called as find element.

79
00:05:15,570 --> 00:05:22,330
And in this particular find element, uh, I'm going to be calling this operation.

80
00:05:22,330 --> 00:05:25,010
So I'm going to probably write this as step approach.

81
00:05:25,010 --> 00:05:34,650
So the step one is I'm going to try finding the element using current strategy, which is the locator

82
00:05:34,650 --> 00:05:37,970
that I'm going to be passing in from our page object model code.

83
00:05:37,970 --> 00:05:40,690
This is exactly what we are going to be doing here.

84
00:05:40,730 --> 00:05:41,250
Right.

85
00:05:41,290 --> 00:05:44,050
So I'm going to say var element is equal.

86
00:05:44,050 --> 00:05:47,970
To try find with current strategy I'm going to pass that.

87
00:05:48,490 --> 00:05:59,410
And I'm going to say if the element that we have got is not equal to null, then you return the element

88
00:05:59,410 --> 00:06:00,130
that we have got.

89
00:06:00,130 --> 00:06:03,450
So this is going to be like an element that I'm trying to return.

90
00:06:03,450 --> 00:06:06,530
So this is what is going to happen over here.

91
00:06:06,610 --> 00:06:13,130
So this is the first step to find the element using the try find with current strategy.

92
00:06:13,130 --> 00:06:14,890
And this is every time I'm going to work.

93
00:06:14,890 --> 00:06:16,210
Because you know what?

94
00:06:16,210 --> 00:06:19,610
If the locators are correct, then this is going to go and find it.

95
00:06:19,610 --> 00:06:26,970
But what if the element is not really going to match and if it is failing then we have problem.

96
00:06:27,010 --> 00:06:30,170
We need to go to the step two by then.

97
00:06:30,170 --> 00:06:37,370
In this particular step two we are going to find the alternative strategy.

98
00:06:37,650 --> 00:06:45,130
Oh yeah, we know how to do that because we have already found it, uh, within our code, in our last

99
00:06:45,330 --> 00:06:52,010
uh, lectures that we were discussing, which is using this get completion async and then we can find

100
00:06:52,010 --> 00:06:52,490
it.

101
00:06:52,490 --> 00:06:55,690
But the answer is no, we're not going to do that one yet.

102
00:06:55,690 --> 00:07:01,290
We're not going to call the healing operation yet, but we are going to first go and check if there

103
00:07:01,290 --> 00:07:03,730
is any alternative locators available.

104
00:07:03,930 --> 00:07:09,450
Uh, within the locator strategy, uh, that I'm going to store as a collection.

105
00:07:09,450 --> 00:07:14,130
And I'll tell you why we need to do that, so that you will get a clear understanding of how you can

106
00:07:14,130 --> 00:07:15,450
actually do that as well.

107
00:07:15,490 --> 00:07:18,970
We'll be discussing about that in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 6. Building AlternativeLocatorStrategy from collection

1
00:00:01,720 --> 00:00:02,680
All right.

2
00:00:02,680 --> 00:00:12,880
So now we have seen how we can build a locator strategy where we also built the locator from the locator

3
00:00:12,880 --> 00:00:16,880
strategy which was using the locator from the page object model code.

4
00:00:17,280 --> 00:00:20,640
And if that works we could able to perform an operation.

5
00:00:20,640 --> 00:00:24,960
So we wrote a method called as try find with current strategy which is going to do that operation.

6
00:00:24,960 --> 00:00:27,120
So this is what that particular method is all about.

7
00:00:27,120 --> 00:00:30,160
So this is something that we have done over here.

8
00:00:30,160 --> 00:00:31,920
But what if this guy is fail.

9
00:00:31,920 --> 00:00:36,480
And what if the element is going to be returned to as as null over there.

10
00:00:36,480 --> 00:00:40,400
So now we need to find the step two which is the alternative strategy.

11
00:00:40,680 --> 00:00:43,480
So we are going to go and do this operation right now.

12
00:00:43,480 --> 00:00:44,960
But over here guess what.

13
00:00:45,000 --> 00:00:48,120
The alternative locators are going to be found.

14
00:00:48,160 --> 00:00:56,040
If the alternative locator collection that we have got is kind of empty or it is not really there for

15
00:00:56,040 --> 00:00:56,200
us.

16
00:00:56,200 --> 00:00:58,560
So that is something that we have to do over there.

17
00:00:58,560 --> 00:01:03,800
So we need to go and check if there is any locator in the collection.

18
00:01:03,840 --> 00:01:04,840
But guess what?

19
00:01:04,880 --> 00:01:06,720
We don't even have a collection at the moment.

20
00:01:06,720 --> 00:01:09,160
We have not even stored anything in the collection.

21
00:01:09,160 --> 00:01:12,040
So how are we going to do that part right now?

22
00:01:12,040 --> 00:01:12,760
Because that's part.

23
00:01:12,800 --> 00:01:15,040
That part is not even done so far.

24
00:01:15,280 --> 00:01:18,160
So how are we actually going to do that?

25
00:01:18,320 --> 00:01:25,920
Well guess what, we are going to be creating a collection right now like this and store all the different

26
00:01:25,920 --> 00:01:33,120
types of locators, which the AI healing process is going to find it and hold it for us.

27
00:01:33,600 --> 00:01:38,440
As I told you before, for the very first time, this guy is always going to be empty.

28
00:01:39,200 --> 00:01:43,440
The collection will not have any one of the value, so it is going to be empty.

29
00:01:43,640 --> 00:01:48,520
So it is going to eventually going to fail and it's going to invoke the healing process, uh, over

30
00:01:48,520 --> 00:01:48,960
here.

31
00:01:49,200 --> 00:01:50,880
But at the moment, guess what?

32
00:01:51,120 --> 00:01:56,120
Since we didn't even build this particular, uh, dictionary or the collection, we are going to do

33
00:01:56,120 --> 00:01:56,960
it right now.

34
00:01:57,000 --> 00:02:01,080
That is what is the whole idea of this particular lecture.

35
00:02:01,080 --> 00:02:03,040
So let's see how we can build it.

36
00:02:03,040 --> 00:02:09,350
So I'm going to say private uh and a read only dictionary I'm going to build.

37
00:02:09,550 --> 00:02:17,630
And I'm going to build a dictionary in such a way that it is going to have a string, uh, and the locator

38
00:02:17,830 --> 00:02:19,070
strategy.

39
00:02:20,310 --> 00:02:23,910
So this is going to be the locator strategies that I'm going to be building this time.

40
00:02:24,270 --> 00:02:28,710
And this locator strategies that we have got is basically like a collection.

41
00:02:28,710 --> 00:02:28,910
Right.

42
00:02:28,910 --> 00:02:34,230
It is going to have, uh, the locators and then all the different types of locator strategies.

43
00:02:34,590 --> 00:02:41,310
For the very first time, we are going to have a locator strategies as well, which is going to be a

44
00:02:41,350 --> 00:02:45,150
new dictionary of string, something like this.

45
00:02:45,630 --> 00:02:50,950
And in order to initialize this in the C-sharp dotnet world, you can just open two double braces.

46
00:02:50,950 --> 00:02:52,950
And here you can pass the key.

47
00:02:53,110 --> 00:02:55,870
And then the value you can initialize them.

48
00:02:55,870 --> 00:02:58,670
So the key for the very first time is going to be primary.

49
00:02:58,670 --> 00:03:03,110
Because this is the first time uh, we found from the page object model code itself.

50
00:03:03,110 --> 00:03:05,670
So we're going to call this as primary locator.

51
00:03:05,870 --> 00:03:08,630
Uh so I'm going to pass the primary locator over there.

52
00:03:09,590 --> 00:03:13,070
So this is the locator strategies that I'm storing it as a collection.

53
00:03:13,070 --> 00:03:17,590
So this is for the very first time that you are going to be getting from this particular page, which

54
00:03:17,590 --> 00:03:24,350
is the buy dot link text of login, which is going to be stored into the collection over here as the

55
00:03:24,350 --> 00:03:25,870
primary locator.

56
00:03:26,390 --> 00:03:26,670
Right.

57
00:03:26,670 --> 00:03:28,270
So that is the locator strategies.

58
00:03:28,670 --> 00:03:33,990
And now if you come back here it is going to check the alternative locator.

59
00:03:33,990 --> 00:03:39,470
So for the very first time the collection is not going to have any one of the value there.

60
00:03:39,470 --> 00:03:39,590
Right.

61
00:03:39,630 --> 00:03:41,910
It's going to be just like empty there.

62
00:03:41,910 --> 00:03:44,630
So we are just going to skip that particular operation.

63
00:03:44,630 --> 00:03:48,910
So let's see how we're going to write that particular method over here.

64
00:03:49,230 --> 00:03:58,950
So I'm going to write a method uh over here, something like public uh I web element.

65
00:03:59,150 --> 00:04:04,390
And of course I'm going to make this as an nullable element as well because this could fail as well.

66
00:04:04,430 --> 00:04:04,950
Right.

67
00:04:04,950 --> 00:04:10,710
So I'm going to say try alternative, uh, strategies, something like that.

68
00:04:11,070 --> 00:04:18,100
And this particular method over here I'm going to say if see this is the locator strategy that we have

69
00:04:18,100 --> 00:04:18,340
got.

70
00:04:18,380 --> 00:04:25,260
If the locator strategies that we have got which has got the count which is less than or equal to one,

71
00:04:25,260 --> 00:04:30,820
which means you know that every single time while the locator is going to be initialized in the constructor

72
00:04:30,820 --> 00:04:35,740
of this particular, uh, class, it is always going to have a primary locator.

73
00:04:35,740 --> 00:04:40,260
So it's going to be one value all the time in this particular collection.

74
00:04:40,260 --> 00:04:45,540
Regardless, it is always going to be one because you are initializing it all the time.

75
00:04:45,540 --> 00:04:46,620
So that is going to be one.

76
00:04:46,620 --> 00:04:53,020
So if the locator strategies dot count is less than or equal to one, then you just return null.

77
00:04:53,060 --> 00:04:54,580
Because you know what?

78
00:04:54,620 --> 00:04:59,580
Uh, this is nothing to do with the operation because locator strategy, if it is, the count is less

79
00:04:59,580 --> 00:05:03,900
than or equal to one, which means it is always the primary locator that we have got.

80
00:05:03,900 --> 00:05:07,660
So there is no point even getting to the try alternative locator strategy.

81
00:05:07,700 --> 00:05:11,100
Just return null because it is not going to work out that time.

82
00:05:11,100 --> 00:05:14,100
So that is what this particular line of code is really saying.

83
00:05:14,220 --> 00:05:15,740
Hope you got the idea right.

84
00:05:15,780 --> 00:05:21,220
Because if the count is less than or equal to one, this is essentially the current primary locator

85
00:05:21,220 --> 00:05:22,940
that you have got, which is this one.

86
00:05:22,940 --> 00:05:29,660
So there is no point in using or iterating through the next line of code in this particular method.

87
00:05:29,660 --> 00:05:31,900
So that's the reason why I'm returning a null there.

88
00:05:31,900 --> 00:05:33,580
So the element is going to be null.

89
00:05:33,860 --> 00:05:38,940
But if there are some values in the locator strategy how do we get it.

90
00:05:38,940 --> 00:05:41,780
So I'm going to write a foreach loop over here.

91
00:05:42,180 --> 00:05:47,940
And I'm going to actually write some advanced code which is using tuples.

92
00:05:47,940 --> 00:05:56,140
So I'm going to say var uh strategy name and a strategy itself.

93
00:05:56,700 --> 00:05:58,460
I'll tell you what I really mean about that.

94
00:05:58,860 --> 00:06:00,460
Let me delete this particular code.

95
00:06:00,580 --> 00:06:05,340
And the collection is nothing but in locator strategies okay.

96
00:06:05,660 --> 00:06:10,380
What is this Karthik I have really not written this kind of code ever before.

97
00:06:10,540 --> 00:06:11,580
Well guess what?

98
00:06:11,620 --> 00:06:14,580
You know this particular dictionary that we have got this guy.

99
00:06:14,860 --> 00:06:18,660
It is of a type type string and a by type.

100
00:06:18,740 --> 00:06:24,100
So basically the string that we have got is essentially a strategy name.

101
00:06:24,100 --> 00:06:29,780
Or we can also call this as like a locator value that we have got, which I'm going to call this as

102
00:06:29,780 --> 00:06:30,780
strategy name.

103
00:06:30,780 --> 00:06:38,340
And by is basically your actual, uh, actual locator itself that you are actually storing it over here.

104
00:06:38,380 --> 00:06:42,060
See the primary and the primary locator.

105
00:06:42,060 --> 00:06:47,860
So essentially you are storing locator in this particular collection.

106
00:06:47,860 --> 00:06:48,260
Right.

107
00:06:48,340 --> 00:06:51,020
So that is what I'm actually getting it from the tuple.

108
00:06:51,020 --> 00:06:56,540
So if you do this way you are going to get uh from the iteration every single time.

109
00:06:56,540 --> 00:07:01,900
The strategy name and the strategy I know this particular piece of code might confuse you if you are

110
00:07:01,900 --> 00:07:03,900
really not used it before, but guess what?

111
00:07:03,900 --> 00:07:08,660
If you try to debug this particular code, you will understand how amazing this code really works.

112
00:07:08,660 --> 00:07:15,060
So it is going to return both of them from your, uh, dictionary, uh, while you do the iteration.

113
00:07:15,380 --> 00:07:25,690
And now here I'm going to say if the strategy that you have got is this one, uh, is going to be equal

114
00:07:25,850 --> 00:07:29,130
to the current strategy that we have got.

115
00:07:29,170 --> 00:07:31,690
The current strategy is going to be nothing but the primary locator.

116
00:07:31,690 --> 00:07:36,010
You remember this one, the primary locator which is coming from the page object model code.

117
00:07:36,050 --> 00:07:38,890
If it is exactly the same then guess what?

118
00:07:39,170 --> 00:07:42,170
There is no point in, uh, being here.

119
00:07:42,210 --> 00:07:43,810
Just do a continue.

120
00:07:45,250 --> 00:07:45,610
Right.

121
00:07:45,610 --> 00:07:47,890
You can just ignore that guy for now.

122
00:07:48,250 --> 00:07:55,490
But if not, I mean, if the if the locator is not this guy because, uh, in the current strategy,

123
00:07:55,530 --> 00:07:59,690
you're going to have the, the primary locator as well for the very first time.

124
00:07:59,690 --> 00:08:05,770
If it is the second locator that you have got in the collection, then you do this, you are going to

125
00:08:05,810 --> 00:08:08,970
do a try catch block, uh, over here.

126
00:08:09,010 --> 00:08:13,210
So I'm going to say catch and no such element exception.

127
00:08:13,570 --> 00:08:16,770
And uh, I'm gonna just leave that guy as it is.

128
00:08:17,290 --> 00:08:21,250
And probably I'm going to return null as well if nothing is going to happen.

129
00:08:21,250 --> 00:08:21,810
Right.

130
00:08:21,810 --> 00:08:27,130
So this is the place where we are going to start implementing the rest of the code, which is even more

131
00:08:27,130 --> 00:08:28,410
straightforward as well.

132
00:08:28,410 --> 00:08:34,530
But for now, just to reiterate what we have done so far in the try alternative strategy, all we have

133
00:08:34,530 --> 00:08:41,210
done over here is we have created a collection of all the locator strategies, which is going to store

134
00:08:41,250 --> 00:08:47,290
different types of locator coming from the A's healing process, and it's going to store them all.

135
00:08:47,290 --> 00:08:53,170
And because we don't have that process yet, it is always going to be like the dictionary value is always

136
00:08:53,170 --> 00:08:54,970
going to be of a count one.

137
00:08:54,970 --> 00:08:58,370
So that is what we have stored over here, which is the primary locator.

138
00:08:58,650 --> 00:09:03,850
And now in this particular code we are saying that if the locator strategies count is less than or equal

139
00:09:03,850 --> 00:09:09,930
to one, then return null, which means it is always going to be the same exact primary locator.

140
00:09:09,930 --> 00:09:12,490
So don't even dare to use this guy.

141
00:09:12,810 --> 00:09:20,250
But if the collection has got more, then you try to iterate through them and try to perform the operation.

142
00:09:20,290 --> 00:09:23,570
That is what is the entire idea over here.

143
00:09:23,810 --> 00:09:31,680
So now we need to call this particular try alternative strategy in the second step over here and see

144
00:09:31,680 --> 00:09:33,000
how that can be done.

145
00:09:33,360 --> 00:09:41,960
And again guys, we have really not seen how the, uh, how the, uh, try block needs to be written.

146
00:09:41,960 --> 00:09:47,800
So far it is not even written yet, but I'm just trying to put the puzzles over here so that you can

147
00:09:47,800 --> 00:09:49,280
understand what I'm trying to do.

148
00:09:49,320 --> 00:09:55,680
And I'm going to say, even if this guy is going to fail, then you need to call the step three, which

149
00:09:55,680 --> 00:10:03,920
is essentially our, uh, AI based auto healing, uh, approach.

150
00:10:04,400 --> 00:10:06,400
That is what we're going to be doing over here.

151
00:10:06,400 --> 00:10:10,240
But we still have a hollow there, which is how are we going to write this?

152
00:10:10,240 --> 00:10:10,960
Try block.

153
00:10:11,440 --> 00:10:16,600
The reason why I have not written this code is because I want you to, first of all, try out and understand

154
00:10:16,600 --> 00:10:20,760
what this current code is doing and how you can build your own.

155
00:10:20,760 --> 00:10:24,120
Try block over here, see if you can able to achieve it.

156
00:10:24,440 --> 00:10:29,880
If it doesn't work, then we are going to do the exact similar thing in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 7. Building AlternativeLocatorStrategy from Collection (Contd.)

1
00:00:00,200 --> 00:00:01,000
All right.

2
00:00:01,360 --> 00:00:07,880
So now we are going to see how we can start building the alternative locators even further within our

3
00:00:07,880 --> 00:00:09,080
try catch block code.

4
00:00:09,120 --> 00:00:10,520
We have not done that yet.

5
00:00:10,560 --> 00:00:13,160
I hope you would have attempted to build that.

6
00:00:13,160 --> 00:00:14,560
I highly recommend you to do it.

7
00:00:14,560 --> 00:00:18,160
If not, we are going to do the exact same thing in this particular lecture.

8
00:00:18,200 --> 00:00:19,400
I'll show you how we can do it.

9
00:00:19,800 --> 00:00:22,560
So essentially, I'm just revisiting one more time.

10
00:00:22,560 --> 00:00:27,640
I know this concept is a bit more complex, so I'm trying to make sure that you are clear as much as

11
00:00:27,640 --> 00:00:28,240
possible.

12
00:00:28,400 --> 00:00:34,720
So we have been building this locator strategy in such a way that we wanted to build a locator that

13
00:00:34,720 --> 00:00:41,400
we are going to first build a method to use the usual locator from the page object model code.

14
00:00:41,640 --> 00:00:46,000
And if that works directly, then it's going to perform the operation on the UI.

15
00:00:46,320 --> 00:00:51,280
But if it doesn't work, then we are going to call an alternative locator method, which is going to

16
00:00:51,280 --> 00:00:58,200
first go and check if there is going to be a locator in the collection, which is the locator strategies

17
00:00:58,200 --> 00:00:59,800
collection that we actually built.

18
00:01:00,050 --> 00:01:05,890
If the locator strategy collection does not have that particular data, then it is going to invoke the

19
00:01:05,890 --> 00:01:06,970
AI healing process.

20
00:01:06,970 --> 00:01:10,490
We have not got through that particular process or point yet.

21
00:01:10,850 --> 00:01:16,610
We are still in this point where we are going to use the locators from this particular collection.

22
00:01:16,610 --> 00:01:18,130
That is what we have been building.

23
00:01:18,130 --> 00:01:23,650
And we also saw that for the very first time in the constructor, we are going to be initializing the

24
00:01:23,650 --> 00:01:29,610
primary locator into this particular dictionary, which is on this particular constructor over here.

25
00:01:29,610 --> 00:01:35,570
So always the count of this particular locator is going to be one which is this one.

26
00:01:35,570 --> 00:01:39,810
So if it is the count of one which means it is still the same primary locator.

27
00:01:39,810 --> 00:01:41,890
So there is no point in iterating.

28
00:01:41,890 --> 00:01:45,290
So just return the element as null for us over here.

29
00:01:45,290 --> 00:01:46,850
That is what is going to happen.

30
00:01:46,850 --> 00:01:51,650
And then it's going to perform the next operation, which is the AI healing operation within our code.

31
00:01:51,970 --> 00:01:52,410
Right.

32
00:01:52,450 --> 00:01:56,490
We saw all of these in our last lecture, like how we did that.

33
00:01:56,490 --> 00:02:04,340
And this is how the code we end up writing, and now we are going to see how we can write the try catch

34
00:02:04,340 --> 00:02:05,500
block over here.

35
00:02:05,540 --> 00:02:07,940
I mean, the try catch block is way more simpler.

36
00:02:07,980 --> 00:02:08,620
Right.

37
00:02:08,660 --> 00:02:15,220
So once we find any one of the locator from this particular strategy, because if it is not this part

38
00:02:15,220 --> 00:02:18,540
as well, then we have got a new strategy that we can try out.

39
00:02:18,540 --> 00:02:28,540
So we are going to say var element is equal to I'm going to just call our driver dot find element.

40
00:02:28,540 --> 00:02:32,460
And we are going to use this strategy that we have got right.

41
00:02:32,460 --> 00:02:36,540
So I'm going to pass this strategy over here just this one.

42
00:02:37,060 --> 00:02:39,420
And we're going to try to find that particular element.

43
00:02:40,140 --> 00:02:47,900
And I'm also going to update that the current strategy that we have is not the primary locator that

44
00:02:47,900 --> 00:02:49,060
we have passed in.

45
00:02:49,340 --> 00:02:56,220
Rather, the current strategy is going to be the new strategy that we have got, which is this particular

46
00:02:56,220 --> 00:02:57,060
strategy.

47
00:02:57,060 --> 00:02:57,070
RTG.

48
00:02:57,110 --> 00:02:59,550
Oh, look at that.

49
00:02:59,870 --> 00:03:08,990
This is the place we are where we are updating our strategy to a successful strategy.

50
00:03:09,030 --> 00:03:09,630
It is.

51
00:03:09,670 --> 00:03:15,870
I hope this makes you more sense this time, because now this is the, uh, this is the full, successful

52
00:03:15,870 --> 00:03:19,830
strategy that we are going to be using over here moving forward.

53
00:03:19,830 --> 00:03:21,550
So this is the current strategy.

54
00:03:21,590 --> 00:03:26,950
See now next time, while this particular code is going to be executed, the strategy is going to be

55
00:03:26,950 --> 00:03:29,190
different for the strategy.

56
00:03:29,190 --> 00:03:29,830
You remember.

57
00:03:29,830 --> 00:03:32,670
Because now the strategy has been updated.

58
00:03:33,110 --> 00:03:33,550
Right.

59
00:03:33,550 --> 00:03:35,310
That is what is going to happen over here.

60
00:03:35,310 --> 00:03:37,190
We are just updating this particular strategy.

61
00:03:38,070 --> 00:03:43,430
And now I can even write a console message if I wanted to.

62
00:03:43,470 --> 00:03:47,910
If not, I'm just going to say, uh, return the element.

63
00:03:48,270 --> 00:03:49,150
Look at that.

64
00:03:49,390 --> 00:03:51,190
That's the way that we do it.

65
00:03:51,190 --> 00:03:55,070
This is the try alternative strategy for us over here.

66
00:03:55,070 --> 00:04:00,120
So now we have updated the current strategy to the new strategy that we have got.

67
00:04:00,240 --> 00:04:04,000
So this way this code is just going to work for us.

68
00:04:04,800 --> 00:04:07,280
And the last operation.

69
00:04:07,760 --> 00:04:12,680
What if this alternative strategy does not work as well, right.

70
00:04:12,720 --> 00:04:18,400
Because for the very first time as we know, the collection is going to be empty there.

71
00:04:18,480 --> 00:04:20,160
So it's not going to be doing anything.

72
00:04:20,160 --> 00:04:23,880
So we are going to fail in this steps already.

73
00:04:23,880 --> 00:04:25,960
So it is going to be null and it's going to fail.

74
00:04:26,280 --> 00:04:33,960
This locator strategy is going to have more data only if we are going to be filling that locator strategy

75
00:04:33,960 --> 00:04:36,440
with our AI auto healing approach.

76
00:04:36,760 --> 00:04:38,920
That's what we are going to be doing next.

77
00:04:39,360 --> 00:04:46,760
So the way we are going to do it is we are going to create one more method which is going to, uh,

78
00:04:46,800 --> 00:04:49,440
perform the auto healing operation.

79
00:04:49,560 --> 00:04:52,680
So I'm going to build a method to do that.

80
00:04:52,680 --> 00:04:55,960
But for that you need to wait until our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 8. Building AI Healing to get Alternative Locator from LLMs

1
00:00:00,080 --> 00:00:07,680
All right, so now that you have seen how we could able to perform the operation of identifying the

2
00:00:07,680 --> 00:00:11,440
current strategy and using the alternative strategy.

3
00:00:11,480 --> 00:00:15,120
And the last approach is the AI based auto healing approach.

4
00:00:15,120 --> 00:00:16,200
So this is the process.

5
00:00:16,200 --> 00:00:17,080
This is the point.

6
00:00:17,120 --> 00:00:19,440
Now we are in to make that happen.

7
00:00:19,800 --> 00:00:26,120
I know it's not easy to get through until here, but thank you for making this so far and you are going

8
00:00:26,120 --> 00:00:28,840
to see how amazing we are going to write this particular method.

9
00:00:28,840 --> 00:00:31,240
And this method is going to be very, very straightforward.

10
00:00:31,240 --> 00:00:34,440
We have already written all the bits and pieces earlier.

11
00:00:34,480 --> 00:00:38,440
We just have to bundle all the puzzles together to make it work.

12
00:00:38,680 --> 00:00:41,000
So let's see how we can actually build it.

13
00:00:41,200 --> 00:00:46,640
Well I'm going to create a method over here and I'm going to call this as guess what?

14
00:00:46,640 --> 00:00:50,640
We can just make all the method as private to be honest, because these methods are just going to be

15
00:00:50,640 --> 00:00:54,480
sitting, uh, just on this particular class file.

16
00:00:54,480 --> 00:00:56,480
So not anywhere it's going.

17
00:00:56,480 --> 00:01:00,680
So I'm just going to make all the methods as private, um, app.

18
00:01:00,920 --> 00:01:03,480
And we're going to invoke this find element outside.

19
00:01:03,480 --> 00:01:05,000
So let it be public for now.

20
00:01:05,720 --> 00:01:11,560
And I'm going to go over here and I'm going to call the healing operation.

21
00:01:11,560 --> 00:01:18,640
So I'm going to say private async of task and then heal using AI.

22
00:01:18,800 --> 00:01:23,560
So that's the method that we are going to be writing this time okay.

23
00:01:23,880 --> 00:01:27,000
So let's see how we're going to do all these operation.

24
00:01:27,000 --> 00:01:30,680
Well in order to heal using the artificial intelligence.

25
00:01:30,680 --> 00:01:36,360
You remember we were trying to do the exact similar thing in our last section over here.

26
00:01:36,640 --> 00:01:40,120
We need to give the context to the large language model.

27
00:01:40,160 --> 00:01:44,120
Again, remember the context engineering and the prompt engineering that we were discussing so many

28
00:01:44,120 --> 00:01:44,960
times before.

29
00:01:45,200 --> 00:01:47,520
We are now going to bring them all in action there.

30
00:01:47,880 --> 00:01:56,920
We wanted to pass in the locator type, the locator value and the page source so that it can be used

31
00:01:56,920 --> 00:02:03,120
for the large language model to get as the required locator that we're looking for.

32
00:02:03,120 --> 00:02:05,920
So we need to pass all of these two.

33
00:02:06,520 --> 00:02:10,640
This method, which is nothing but the heel using AI locator method.

34
00:02:10,640 --> 00:02:14,200
So we need to build that particular logic there in order to do that.

35
00:02:14,600 --> 00:02:16,080
So how do I actually do it?

36
00:02:16,080 --> 00:02:16,840
But guess what.

37
00:02:16,880 --> 00:02:22,720
We already have the locator within our Self Healing locator class over here.

38
00:02:22,760 --> 00:02:28,720
See we have got the locator which has got the locator as well as the locator type.

39
00:02:28,720 --> 00:02:30,840
So that's not going to be of any problem.

40
00:02:30,840 --> 00:02:32,440
We can just use that.

41
00:02:32,440 --> 00:02:35,840
So we can use that method to perform the operation.

42
00:02:35,840 --> 00:02:42,720
So if I'm going to go this particular code over here where we were trying to get the uh the locator

43
00:02:42,720 --> 00:02:44,200
strategies, which is this one.

44
00:02:44,240 --> 00:02:49,840
So I'm going to copy this whole code, go over here, paste it instead of this locator, I can just

45
00:02:49,840 --> 00:02:54,040
say current strategy which is going to get me the locator.

46
00:02:54,080 --> 00:02:55,120
You know this current locator.

47
00:02:55,120 --> 00:03:00,640
Our current strategy is nothing but a by type which we have passed as a primary locator before the same

48
00:03:00,640 --> 00:03:07,080
thing I'm passing in over here and I'm going to, uh, get that particular value, which is going to

49
00:03:07,080 --> 00:03:09,530
get me the locator type as well as locator value.

50
00:03:09,930 --> 00:03:16,810
Again, guys, please go ahead and watch the earlier sessions if you have forgot how we did that or

51
00:03:16,810 --> 00:03:17,930
if you still remember it.

52
00:03:17,930 --> 00:03:19,650
Amazing if you did not.

53
00:03:19,690 --> 00:03:24,010
I know this code is not very straightforward like how we do right in automation.

54
00:03:24,050 --> 00:03:29,810
Please try to refer it back before you come here because it will confuse you if you are seeing it for

55
00:03:29,810 --> 00:03:34,730
the very first time, or if you have really skipped that session, I highly recommend you to first watch

56
00:03:34,730 --> 00:03:39,770
that so that you will make this particular line of code more sensible there, right?

57
00:03:39,850 --> 00:03:41,650
So that is what we are doing over here.

58
00:03:41,650 --> 00:03:45,250
So we are going to first get the locator type and locator value.

59
00:03:45,250 --> 00:03:48,570
And now we also need to get the page source you remember.

60
00:03:48,890 --> 00:03:50,050
Where do we get that.

61
00:03:50,090 --> 00:03:56,970
Well in order to get the page source we just have to say var page source is equal to.

62
00:03:57,690 --> 00:04:01,650
Remember we have a driver object already and we can just call the page source.

63
00:04:01,650 --> 00:04:05,370
So we have got the locator type locator value and the page source.

64
00:04:05,370 --> 00:04:07,210
We have got all of these right now.

65
00:04:07,210 --> 00:04:09,210
That's what we're going to do right now.

66
00:04:09,650 --> 00:04:13,890
And finally, you remember what we did in our enhanced test over there.

67
00:04:14,090 --> 00:04:22,450
We actually called the LM client class, and we also called this particular method to get the healed

68
00:04:22,450 --> 00:04:23,090
locator.

69
00:04:23,490 --> 00:04:28,930
Uh, and then we called the get completion, uh, async over there.

70
00:04:29,210 --> 00:04:32,250
I'm actually going to copy all of these from here.

71
00:04:32,530 --> 00:04:35,050
And I'm going to paste them all here.

72
00:04:35,290 --> 00:04:37,210
So we need to get the healed locator.

73
00:04:37,250 --> 00:04:38,610
Oh where is that sitting.

74
00:04:39,290 --> 00:04:39,690
Ah.

75
00:04:39,930 --> 00:04:40,410
This one.

76
00:04:40,410 --> 00:04:42,210
The healed locator over here.

77
00:04:42,530 --> 00:04:48,090
We can actually have this healed locator in the LM client class itself.

78
00:04:48,090 --> 00:04:56,410
But because this is not part of the client class, we can have them as a separate place where we can

79
00:04:56,410 --> 00:04:58,850
maintain all the prompts.

80
00:04:59,250 --> 00:05:01,770
That way, it is going to be even more straightforward.

81
00:05:01,770 --> 00:05:03,370
So we can do that as well.

82
00:05:03,770 --> 00:05:08,650
So in order to do that, I'm going to go and create a class over here.

83
00:05:08,890 --> 00:05:13,410
Uh, and I'm going to name this as uh Get.

84
00:05:13,730 --> 00:05:17,570
Locate our from LMS or something like that.

85
00:05:17,610 --> 00:05:19,210
I mean, you can name whatever that you want.

86
00:05:19,250 --> 00:05:24,810
I'm just thinking loud over here to see what name I can give, but I don't really have any name preference

87
00:05:24,810 --> 00:05:29,410
over here, but I'm just going to say get locators from the LM.

88
00:05:29,890 --> 00:05:35,530
So the reason why I wanted to do this is because now this particular class is the one which is responsible

89
00:05:35,530 --> 00:05:39,050
for sending the prompt to the large language model.

90
00:05:39,050 --> 00:05:41,570
And then it's also going to get us the response that we're looking for.

91
00:05:41,610 --> 00:05:45,050
That's the reason why this particular class does exist.

92
00:05:45,050 --> 00:05:45,690
And guess what?

93
00:05:45,690 --> 00:05:52,330
In future you can have any number of classes and you can have them all in a separate folders if you

94
00:05:52,330 --> 00:05:53,210
really wanted to.

95
00:05:53,250 --> 00:05:59,250
That way you can maintain all the prompts which talks with the large language model in a separate class

96
00:05:59,250 --> 00:05:59,730
file.

97
00:05:59,930 --> 00:06:00,330
Right.

98
00:06:00,370 --> 00:06:01,690
So I'm going to do that.

99
00:06:01,690 --> 00:06:05,530
And I'm going to make this as a static class because it's not really doing anything.

100
00:06:05,570 --> 00:06:11,010
Apart from that I'm going to paste the code that I've just copied from the enhanced tests class already.

101
00:06:11,210 --> 00:06:14,490
And I'm going to make this as static as well.

102
00:06:15,170 --> 00:06:15,690
right?

103
00:06:15,730 --> 00:06:21,770
I think there is a spelling mistake on the original, so I'm going to go add an eye there to make this

104
00:06:21,810 --> 00:06:22,450
perfect.

105
00:06:22,730 --> 00:06:24,090
Uh, which is great.

106
00:06:24,290 --> 00:06:29,370
Uh, and now I'm going to, uh, have this particular method to have a prompt.

107
00:06:29,770 --> 00:06:36,930
And the last thing is not just returning the prompt, but also we can ask this particular code to go

108
00:06:36,930 --> 00:06:43,010
and talk with the large language model and return as the deserialized response, like how we were doing

109
00:06:43,010 --> 00:06:43,770
over here.

110
00:06:44,850 --> 00:06:46,610
See these two operations?

111
00:06:46,610 --> 00:06:52,210
We can ask this piece of code to to do it for us, because that's what this is essentially doing, right.

112
00:06:52,250 --> 00:06:54,650
So I'm going to go and paste that over here.

113
00:06:55,050 --> 00:07:00,330
And this is going to be an public static async of the task.

114
00:07:00,650 --> 00:07:05,930
Uh, and we are going to return a locator suggestion from this guy.

115
00:07:06,050 --> 00:07:11,330
So I'm just going to add or import the missing piece uh over here.

116
00:07:11,650 --> 00:07:16,250
Uh, and we also need to pass the LM client because we do need it.

117
00:07:16,330 --> 00:07:23,010
So let me also pass the LLM client, which is going to be the client that we need to pass in.

118
00:07:23,370 --> 00:07:24,850
Uh, and we are done.

119
00:07:24,890 --> 00:07:25,610
Look at that.

120
00:07:25,610 --> 00:07:27,730
This code is now very straightforward.

121
00:07:27,730 --> 00:07:29,730
So that is what this guy is doing.

122
00:07:30,050 --> 00:07:32,450
I'm also going to return this particular value.

123
00:07:32,450 --> 00:07:38,010
If it is null then it is going to just say maybe uh null right.

124
00:07:38,050 --> 00:07:41,090
So it is going to be null for us, which is going to be returning for us over there.

125
00:07:41,090 --> 00:07:44,290
I can just make this as a nullable type as well.

126
00:07:44,290 --> 00:07:47,490
So that way it is going to not complain us anything.

127
00:07:47,530 --> 00:07:49,090
See this is what this particular code is doing.

128
00:07:49,090 --> 00:07:56,450
So essentially I've just stripped down all of these code from here, just not even required anymore.

129
00:07:57,050 --> 00:08:05,090
All of these code from here into uh, this particular code that we have got, which is nothing but on

130
00:08:05,090 --> 00:08:10,210
the git locators from LLM, which means I don't even need these code that I have got over here.

131
00:08:10,250 --> 00:08:10,530
Right.

132
00:08:10,570 --> 00:08:15,170
Because now I have moved them all, uh, out from this so I can just get rid of that.

133
00:08:15,170 --> 00:08:19,820
So it's all sitting on the git locator from lms CS class file.

134
00:08:19,860 --> 00:08:20,660
Just this one.

135
00:08:21,340 --> 00:08:25,620
And now we are going to if I'm just going to call this get healed locator.

136
00:08:25,620 --> 00:08:32,300
If I'm going to pass all of these, I'm going to get the response from, uh, this guy in a locator

137
00:08:32,300 --> 00:08:37,820
suggestions class type itself because it's going to be deserializing it for us there, which is even

138
00:08:37,820 --> 00:08:38,540
more amazing.

139
00:08:39,100 --> 00:08:44,660
Let me also remove this method from the enhanced tests because now this is obsolete code.

140
00:08:44,660 --> 00:08:49,540
So I'm going to just do a cleanup as well just in case because we don't need them and we don't even

141
00:08:49,540 --> 00:08:54,580
need these, uh, codes from here because these are all moved away right now.

142
00:08:54,780 --> 00:08:58,660
So I'm going to get rid of that because it is not required anymore.

143
00:08:59,620 --> 00:09:00,300
Pretty cool.

144
00:09:00,540 --> 00:09:05,860
So now we have did some cleanup as well as we have created a class file which is going to have the,

145
00:09:06,220 --> 00:09:10,580
uh, the prompt as well as the deserialization from the large language model.

146
00:09:10,580 --> 00:09:12,900
So everything is sitting for us over there.

147
00:09:13,180 --> 00:09:20,780
Uh, and now the last operation we have to do it is to call this, uh, get generated get locator from

148
00:09:20,820 --> 00:09:22,420
LMS class over here.

149
00:09:22,420 --> 00:09:23,820
So let's see how we can actually do that.

150
00:09:23,860 --> 00:09:25,580
Well it's very, very straightforward.

151
00:09:25,580 --> 00:09:36,540
So I'm going to say VAR and I'm going to call this what is called as a suggested locators which is the

152
00:09:36,540 --> 00:09:38,580
AI locators that we are looking for.

153
00:09:38,780 --> 00:09:40,500
And I'm going to call await.

154
00:09:40,940 --> 00:09:47,940
And I'm going to call the get locators from LMS Dot Get healed locator.

155
00:09:48,420 --> 00:09:49,020
See.

156
00:09:49,420 --> 00:09:50,220
Awesome.

157
00:09:50,540 --> 00:09:56,740
And now we need to pass this LM client page source locator type original locators and everything which

158
00:09:56,740 --> 00:10:01,180
we are going to be doing in our next lecture where we're going to be passing all of these.

159
00:10:01,460 --> 00:10:05,220
I know that the client is currently not there in this particular class file.

160
00:10:05,220 --> 00:10:10,340
We need to initialize that and rest of the things we have as a parameter that we can pass in, because

161
00:10:10,340 --> 00:10:12,140
we have all of these already.

162
00:10:12,460 --> 00:10:19,660
So try to do this thing yourself and see if you can able to call the heal locator yourself.

163
00:10:19,860 --> 00:10:21,540
If it works, amazing.

164
00:10:21,580 --> 00:10:25,140
If it does not work, we are going to be covering that in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


video 9. Building AI Healing Locator Types for different locators (XPath, CSS, ID, Name)

1
00:00:00,080 --> 00:00:06,360
All right, so now that I hope you would have already figured out how to pass the LM client, if you

2
00:00:06,360 --> 00:00:10,200
have not done that yet, it's going to be very, very straightforward.

3
00:00:10,200 --> 00:00:16,520
All we did last time was we created an instance of the LM client, which is something like this client

4
00:00:17,360 --> 00:00:20,760
or client is equal to new of the LM client.

5
00:00:20,760 --> 00:00:26,680
That's what we did because while we call the LM client over here, it is going to configure things for

6
00:00:26,680 --> 00:00:28,560
us over here, which is the HTTP client.

7
00:00:28,560 --> 00:00:32,160
And reading the configuration from the JSON over here.

8
00:00:32,320 --> 00:00:34,160
That's the reason why we have to do it.

9
00:00:34,320 --> 00:00:37,800
Uh, and once we have it we can pass this particular object directly.

10
00:00:37,800 --> 00:00:41,800
There is even more elegant way of doing it using a dependency injections and stuff.

11
00:00:41,960 --> 00:00:43,440
And I don't want it to complicate.

12
00:00:43,440 --> 00:00:48,240
That's the reason why I'm not really writing that code yet, but we can move that around as well.

13
00:00:48,560 --> 00:00:54,840
And I'm going to write the client over here and we need to pass the page source, look at our type virtual

14
00:00:54,840 --> 00:00:55,320
locator.

15
00:00:55,320 --> 00:00:59,160
And the page source is this variable that we have already.

16
00:00:59,160 --> 00:01:00,400
So I'm going to pass that.

17
00:01:00,400 --> 00:01:02,240
And the locator type is locator type.

18
00:01:02,480 --> 00:01:05,810
And the locator value is going to be the locator value.

19
00:01:05,850 --> 00:01:06,290
Right.

20
00:01:06,330 --> 00:01:13,810
So the original locator we have got C I have passed all of them over here in this particular method.

21
00:01:13,810 --> 00:01:21,170
So we are going to get the suggested locator while we are going to call the healed heal using the I

22
00:01:21,530 --> 00:01:22,250
over here.

23
00:01:22,450 --> 00:01:31,410
So once we have it we can now add this particular locator as the suggested locator within our collection,

24
00:01:31,410 --> 00:01:36,290
which is nothing but within our locator strategies over here.

25
00:01:36,290 --> 00:01:42,810
So now I need to add this particular code, which is the locator strategies that we have got over here.

26
00:01:43,050 --> 00:01:50,250
And I need to somehow add this suggested locator that we are getting in with the key and value pair.

27
00:01:50,610 --> 00:01:52,530
So how do we actually do that.

28
00:01:53,050 --> 00:01:55,330
Have you think like how that's going to happen.

29
00:01:55,330 --> 00:02:01,810
Because the suggested locator that we are getting over there, it is just going to have the type as

30
00:02:01,850 --> 00:02:08,290
the locator suggestions, which is going to have the ID and it's going to have the Uh, relevant data

31
00:02:08,290 --> 00:02:13,170
is there and the name and relevant, um, locator, XPath relevant locator or something like that.

32
00:02:13,170 --> 00:02:14,490
That's how it is going to be.

33
00:02:14,810 --> 00:02:15,890
Uh, over here.

34
00:02:16,090 --> 00:02:21,610
Uh, the moment we are going to be invoking this suggested locator, because it is of the type locator

35
00:02:21,610 --> 00:02:23,570
suggestions, as you are seeing over here.

36
00:02:23,850 --> 00:02:29,090
So how can I add that within the locator suggestions over here?

37
00:02:29,090 --> 00:02:31,410
Because it is not of this particular type.

38
00:02:31,410 --> 00:02:31,890
Right.

39
00:02:31,930 --> 00:02:38,250
The if I'm going to pass the locator suggestions over here like locator strategies with uh sorry suggested

40
00:02:38,250 --> 00:02:39,930
locators, something like this.

41
00:02:39,930 --> 00:02:41,090
This is not going to work.

42
00:02:41,090 --> 00:02:42,930
You can't really add it over here.

43
00:02:43,050 --> 00:02:50,690
You need to somehow write a code in such a way that you you find the locator, which can be added to

44
00:02:50,730 --> 00:02:52,650
this particular locator strategy.

45
00:02:52,730 --> 00:02:54,530
So how can I actually do that?

46
00:02:54,570 --> 00:02:56,730
Well, that's a bit of a code as well.

47
00:02:56,730 --> 00:03:01,290
One more time that you have to write it so that you can make sure that that could happen as well.

48
00:03:01,410 --> 00:03:03,290
So I'll tell you how we can actually write that.

49
00:03:03,650 --> 00:03:08,610
I am going to write a method over here as private.

50
00:03:08,810 --> 00:03:16,340
Uh, and then I'm going to Gonna return an integer and I'm gonna say try add locator strategy.

51
00:03:16,340 --> 00:03:22,340
So this is like a method which is going to, uh, basically, uh, maybe this is called as try create

52
00:03:22,380 --> 00:03:27,060
locator strategy because this is going to basically create a locator strategy for me.

53
00:03:27,420 --> 00:03:34,100
And over here I'm just going to say locator type and then string of locator value.

54
00:03:34,100 --> 00:03:40,100
So I need to pass these two things so that it can do things for me over here.

55
00:03:40,140 --> 00:03:41,940
I'll tell you what I really mean about that.

56
00:03:41,940 --> 00:03:45,260
So I'm going to also add a if condition over here.

57
00:03:45,260 --> 00:03:53,580
So if the string is uh null or whitespace for the locator value, because there are chances that locator

58
00:03:53,580 --> 00:03:55,220
value can be empty as well.

59
00:03:55,220 --> 00:03:59,340
You remember while we try getting some locators for the class name was empty.

60
00:03:59,580 --> 00:04:01,260
So it could happen as well.

61
00:04:01,260 --> 00:04:04,220
So I'm going to return zero for that.

62
00:04:04,220 --> 00:04:09,780
But if not I'm going to write a try catch block over here um, in this fashion.

63
00:04:09,780 --> 00:04:12,060
So let me just do that over here.

64
00:04:12,060 --> 00:04:15,670
So I'm going to write a switch Which statement?

65
00:04:15,950 --> 00:04:17,950
In the switch statement, I'm going to write something like this.

66
00:04:17,950 --> 00:04:19,950
I'm going to say locate a type.

67
00:04:20,390 --> 00:04:22,030
So what I locate a type that you are getting.

68
00:04:22,030 --> 00:04:25,910
So I'm going to say two lower invariant.

69
00:04:26,030 --> 00:04:33,110
So whatever locator type that you are going to be getting over there based on that you create a a case

70
00:04:33,510 --> 00:04:43,950
something like if it the locator type is going to be an ID, then the BI is going to be bi.id and I'm

71
00:04:43,950 --> 00:04:47,790
going to pass the locator value for that OU.

72
00:04:48,350 --> 00:04:49,750
So hope you got the idea right.

73
00:04:49,750 --> 00:04:57,350
So now I can get whatever that I'm passing in to this tri create locator strategy method.

74
00:04:57,350 --> 00:05:02,110
And I can pass the suggested locators there which is amazing.

75
00:05:02,390 --> 00:05:05,510
And similarly I can do for the rest of the things as well.

76
00:05:05,510 --> 00:05:09,910
For example, uh, let me just break this over here.

77
00:05:10,430 --> 00:05:17,630
And similarly I'm going to do for the name, which is going to be this one, uh, and the bi by the

78
00:05:17,720 --> 00:05:26,760
time it's going to be by dot name, and I'm going to get the locator value, and I'm going to break

79
00:05:26,800 --> 00:05:33,520
over there, and I'm going to do the exact similar operation for the rest of the code as well.

80
00:05:33,520 --> 00:05:37,680
So I'm not just going to write that, but I'm just going to copy paste the code that I have already

81
00:05:37,680 --> 00:05:41,640
written, because that's going to be way more easier for me to do it.

82
00:05:41,640 --> 00:05:44,080
And I hope you already got the idea right with this.

83
00:05:44,080 --> 00:05:47,440
Try create locator strategy is going to do that for you.

84
00:05:47,440 --> 00:05:53,520
So it is going to have the locator type and locator value that you have got from the large language

85
00:05:53,520 --> 00:05:54,120
model.

86
00:05:54,120 --> 00:06:00,800
And you can pass it through so that you can formulate a by type, which you can actually store in the

87
00:06:01,040 --> 00:06:03,480
locator strategies over here.

88
00:06:03,520 --> 00:06:10,240
See basically I have moved the locator strategies which is trying to store the things from here, which

89
00:06:10,240 --> 00:06:15,440
I don't need to store anywhere in here like locator strategies of the locator type.

90
00:06:15,440 --> 00:06:20,800
So you are going to be passing the locator type, uh, which is going to be uh, this one.

91
00:06:21,080 --> 00:06:25,360
And then I'm going to store the by type there.

92
00:06:25,400 --> 00:06:27,640
That is how things are going to happen.

93
00:06:27,640 --> 00:06:33,280
So uh, if you're going to be saying look at our strategies of the locator type over there.

94
00:06:33,680 --> 00:06:37,400
So I am going to store that, uh, in the key.

95
00:06:37,800 --> 00:06:40,480
And this is the value which I'm going to be storing in.

96
00:06:40,840 --> 00:06:47,000
So this is how the locator strategies array is going to store things for us over here.

97
00:06:47,000 --> 00:06:48,960
So we don't even need to pass it over here.

98
00:06:49,000 --> 00:06:49,520
Right.

99
00:06:49,560 --> 00:06:53,080
So now that's amazingly done which is great.

100
00:06:53,320 --> 00:06:59,080
The last operation that we have to do is is to call the try create locator strategy within our code

101
00:06:59,080 --> 00:07:01,840
over here to see how we could able to achieve it.

102
00:07:01,880 --> 00:07:04,720
Well, that's something we are going to be discussing in our next lecture.

103
00:07:04,960 --> 00:07:10,040
I know it's kind of confusing for the very first time, try to go through the code like how it's written

104
00:07:10,040 --> 00:07:15,400
over here, and once you have seen it all, you will notice that the code is just going to be like a

105
00:07:15,440 --> 00:07:16,000
cakewalk.

106
00:07:16,040 --> 00:07:19,640
But once again, I highly recommend you to go through the code one more time.

107
00:07:19,680 --> 00:07:25,200
Try doing it all by yourself before we are going to say done in next couple of lectures.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 10. Building AI Healing Locator Type (Contd.)

1
00:00:00,200 --> 00:00:01,080
All right.

2
00:00:01,080 --> 00:00:07,640
So now that we have created the try create locator strategy method over here, which is also storing

3
00:00:07,680 --> 00:00:13,760
the locator type and the locator value into the collection which is the locator strategies collection.

4
00:00:13,960 --> 00:00:19,120
And now we need to invoke this guy within our heal using AI method.

5
00:00:19,120 --> 00:00:25,880
And we'll see how we can store the locator that we have obtained from the large language model.

6
00:00:25,880 --> 00:00:26,920
And guess what?

7
00:00:26,920 --> 00:00:29,960
We don't have just one single locator from the large language model.

8
00:00:29,960 --> 00:00:37,440
We also used to get quite some locators like ID name, XPath, CSS link text, whatever it is.

9
00:00:37,440 --> 00:00:43,560
So we need to store all the locator types, not just one locator type, but all the locator types within

10
00:00:43,720 --> 00:00:47,680
the collection which is the locator strategies collection over here.

11
00:00:47,920 --> 00:00:49,400
So how can we actually do it?

12
00:00:49,440 --> 00:00:50,480
Well guess what.

13
00:00:50,520 --> 00:00:51,840
We are going to do this.

14
00:00:51,840 --> 00:00:56,200
I am going to say int added account is equal to zero.

15
00:00:56,200 --> 00:00:59,040
So I'm just going to just set an integer over there.

16
00:00:59,040 --> 00:01:01,290
And you understand what I'm trying to do over here?

17
00:01:01,290 --> 00:01:04,170
So I'm going to say, uh, added count.

18
00:01:04,450 --> 00:01:06,090
I'm just going to increment it over here.

19
00:01:06,090 --> 00:01:10,450
So I'm going to call that try create locator strategy something like this.

20
00:01:10,890 --> 00:01:18,290
And over here I need to pass the locator type which is going to be um which is going to be ID for that

21
00:01:18,290 --> 00:01:18,690
matter.

22
00:01:18,770 --> 00:01:25,930
So if it is ID then the suggested locator.id is what I'm going to pass in.

23
00:01:26,930 --> 00:01:27,890
Look at that.

24
00:01:27,890 --> 00:01:31,810
So now the added count is going to increase for us over here right.

25
00:01:32,090 --> 00:01:38,490
And I'm going to say if the I'm going to say one more time added count.

26
00:01:38,490 --> 00:01:40,770
So I'm just going to increment it as well.

27
00:01:40,770 --> 00:01:51,010
If the locator type is equal to XPath for that matter, then you are going to give the suggested locators

28
00:01:51,050 --> 00:01:52,330
as XPath.

29
00:01:52,770 --> 00:01:57,170
And I'm going to do the similar thing for the uh, the rest of the things as well.

30
00:01:57,170 --> 00:01:59,130
So I'm going to copy this whole thing.

31
00:02:00,260 --> 00:02:01,660
Paste it over here.

32
00:02:03,060 --> 00:02:07,460
I'm just going to rename that quickly so that I don't have to run through one more time.

33
00:02:09,540 --> 00:02:10,500
Something like this.

34
00:02:10,740 --> 00:02:12,580
And now you see that all of them are added.

35
00:02:12,580 --> 00:02:18,700
The reason why I have just included this added count over here is I wanted to, uh, show in the console

36
00:02:19,100 --> 00:02:24,860
dot write line over here to say that how many, uh, element has been added for us over here.

37
00:02:24,860 --> 00:02:32,460
So I healing uh, completed with uh total.

38
00:02:35,020 --> 00:02:47,900
Added locators are and then I'm gonna say um like the added count over here as alternative locators.

39
00:02:48,100 --> 00:02:48,340
Right.

40
00:02:48,380 --> 00:02:48,860
Something like this.

41
00:02:48,860 --> 00:02:50,860
So this is what I wanted to print over here.

42
00:02:50,900 --> 00:02:52,140
Once the execution is done.

43
00:02:52,420 --> 00:02:57,540
And there are chances that this could also go wrong, like it could fail as well.

44
00:02:57,540 --> 00:03:03,080
So it's better that we can also add a try catch block over here.

45
00:03:03,600 --> 00:03:04,600
Something like this.

46
00:03:04,880 --> 00:03:06,840
And I'm going to say catch.

47
00:03:06,840 --> 00:03:09,760
And there is going to be an exception.

48
00:03:10,880 --> 00:03:16,760
Uh and I'm going to say the exception is that console dot write line.

49
00:03:17,520 --> 00:03:26,560
Uh I healing failed or something like that I healing failed.

50
00:03:28,800 --> 00:03:29,680
Something like this.

51
00:03:29,680 --> 00:03:30,120
Right.

52
00:03:30,120 --> 00:03:33,160
So that is what I'm going to be, uh, giving over here.

53
00:03:33,160 --> 00:03:35,360
So now that's all done for us over here.

54
00:03:35,360 --> 00:03:41,840
The last operation is to call this particular heal using AI method, uh, within our code and see how

55
00:03:41,840 --> 00:03:43,280
that can be achieved.

56
00:03:43,280 --> 00:03:45,800
So that is what is the last operation that we have to do.

57
00:03:46,000 --> 00:03:50,320
And then once we have it, then we can try performing the rest of the operation.

58
00:03:50,360 --> 00:03:50,880
Right.

59
00:03:50,920 --> 00:03:53,080
So I'm going to do that over here.

60
00:03:53,080 --> 00:03:56,480
So I'm gonna copy this particular heal using AI.

61
00:03:56,680 --> 00:04:03,410
And I'm going to go over here and I'm going to say await heal using AI.

62
00:04:04,050 --> 00:04:04,810
There we go.

63
00:04:04,850 --> 00:04:06,610
That's going to do it for me.

64
00:04:07,050 --> 00:04:16,810
And I'm going to again call our find element method that we have just created, which is this same method

65
00:04:16,810 --> 00:04:23,730
that I'm calling over here, like an, uh, method which can actually be called second time.

66
00:04:23,770 --> 00:04:28,530
See, this is the same thing which is going to be called over and over again for us to ensure that the

67
00:04:28,530 --> 00:04:30,570
the whole operation is going to be done.

68
00:04:30,570 --> 00:04:32,930
But there is a caveat in this particular code.

69
00:04:33,730 --> 00:04:36,770
Just think about what is the caveat that we have in this particular code.

70
00:04:37,770 --> 00:04:39,930
See, I'm going to call this auto healing.

71
00:04:39,930 --> 00:04:42,690
And then I'm calling the same method recursively.

72
00:04:43,130 --> 00:04:45,370
And this is going to run forever.

73
00:04:45,530 --> 00:04:47,850
So how do we solve this particular problem.

74
00:04:47,850 --> 00:04:52,530
If this this recursion is going to happen all the time and is never going to end.

75
00:04:52,890 --> 00:04:53,890
That is the problem.

76
00:04:53,890 --> 00:04:55,690
And how do we fix this particular approach?

77
00:04:55,730 --> 00:04:57,570
We'll be doing that in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 11. Invoking AIHealing Code within Self Healing Logic

1
00:00:00,160 --> 00:00:00,720
All right.

2
00:00:00,720 --> 00:00:06,600
I'm sure that you would have figured out the way how you can actually get out of the recursion problem

3
00:00:06,600 --> 00:00:08,200
that we have got over here.

4
00:00:08,200 --> 00:00:17,240
The way you can do it is just add and retry attempts over here and make is like 2 or 3, whatever that

5
00:00:17,240 --> 00:00:23,080
you want to do based on how much capacity and, uh, the compute power you have got, because I'm not

6
00:00:23,080 --> 00:00:24,680
going to let more than two, to be honest.

7
00:00:24,680 --> 00:00:26,360
So I'm just going to leave that guy as it is.

8
00:00:26,560 --> 00:00:30,440
And over here I'm going to write a condition, uh, over here.

9
00:00:30,440 --> 00:00:35,640
So if the retry attempts, uh, is greater than zero, right.

10
00:00:35,640 --> 00:00:40,720
So if the greater than if it is going to be greater than zero, then try doing it over here.

11
00:00:41,240 --> 00:00:42,680
Something like this.

12
00:00:43,000 --> 00:00:44,600
Uh, because it's two currently.

13
00:00:44,600 --> 00:00:46,080
So it's going to keep running it.

14
00:00:46,080 --> 00:00:51,880
But over here I'm going to set the retry attempts as minus one, which means it's going to keep reducing

15
00:00:51,880 --> 00:00:54,760
the number of attempts for us over here.

16
00:00:55,240 --> 00:00:57,280
That is what I'm trying to do this time.

17
00:00:57,760 --> 00:00:58,400
That's it.

18
00:00:58,440 --> 00:01:01,000
See this is going to do things for me.

19
00:01:01,760 --> 00:01:05,280
And this is the place where you're going to be calling the heel using AI.

20
00:01:05,960 --> 00:01:06,840
All right.

21
00:01:07,240 --> 00:01:12,760
And finally, if none of these steps work like step one fails, step two failed, and even step three

22
00:01:12,800 --> 00:01:21,060
after even two retry failed, I'm going to throw a new, uh, no such element exception, because I

23
00:01:21,100 --> 00:01:24,020
have no idea now how to handle this over here.

24
00:01:24,020 --> 00:01:33,940
So I'm going to say I'm going to say failed to locate the element after.

25
00:01:34,460 --> 00:01:37,100
And we can also say the number of attempts that we have did.

26
00:01:37,100 --> 00:01:37,340
Right.

27
00:01:37,340 --> 00:01:45,780
So after all healing attempts and we can even pass the attempts over here like retry, um, attempts

28
00:01:46,100 --> 00:01:48,020
as well, then we're done.

29
00:01:48,580 --> 00:01:49,060
Right?

30
00:01:49,100 --> 00:01:52,380
This is going to be the find element method that we have got over here.

31
00:01:52,900 --> 00:01:53,820
We have completed.

32
00:01:53,820 --> 00:01:55,620
Guys, congratulations.

33
00:01:55,620 --> 00:01:59,460
We have fully written the code right now to do all of these operations.

34
00:01:59,460 --> 00:02:05,300
This is already the most important and the hardest part of the entire code that we have written.

35
00:02:05,420 --> 00:02:07,700
This is where all the logic really sits in.

36
00:02:08,020 --> 00:02:13,020
I know this is a bit complex for the very first time, but the moment you start looking at what idea

37
00:02:13,020 --> 00:02:19,180
that we are trying to do over here, it's all starting to make you more and more sense because now it

38
00:02:19,180 --> 00:02:21,500
is more straightforward, right?

39
00:02:21,500 --> 00:02:23,540
So we have done everything over here.

40
00:02:23,860 --> 00:02:26,780
I think we have completed everything right now.

41
00:02:27,060 --> 00:02:34,100
And now the last part that we have to do is to use the self-healing locator within our test and see

42
00:02:34,100 --> 00:02:38,900
how this actually works, which will be doing in our next lecture.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

video 12. DebuggingRunning the Test to understand how the AI Self Healing works !

1
00:00:00,280 --> 00:00:06,200
And now we need to call this find element method and see how it actually works.

2
00:00:06,320 --> 00:00:13,680
And the way I'm going to do it is I'm going to go to the test code that we have got over here, and

3
00:00:13,720 --> 00:00:18,720
I'm going to see if I could able to call that particular method, which is nothing but the find element

4
00:00:18,720 --> 00:00:19,800
method that we have got.

5
00:00:19,840 --> 00:00:20,440
Right.

6
00:00:20,480 --> 00:00:25,080
So I'm going to say self healing locator.

7
00:00:25,400 --> 00:00:31,840
Uh, as self locator is equal to nu of the self healing locator.

8
00:00:32,080 --> 00:00:35,840
And I need to pass the driver and the primary locator over here.

9
00:00:35,960 --> 00:00:40,720
So the primary locator that I have got over here from the page object model code, which is the same

10
00:00:40,720 --> 00:00:42,840
one that I have just highlighted.

11
00:00:43,000 --> 00:00:45,000
So I'm just wanting to test how this works.

12
00:00:45,000 --> 00:00:48,280
So this is going to be the var element.

13
00:00:48,640 --> 00:00:54,880
So I'm going to pass this particular element this time and see how that actually works right.

14
00:00:55,120 --> 00:01:01,490
So I'm going to say uh so this is basically looking for the driver and the primary element, which is

15
00:01:01,490 --> 00:01:02,010
great.

16
00:01:02,010 --> 00:01:05,730
So let's pass the driver which is going to be the driver.

17
00:01:05,730 --> 00:01:08,930
And the primary element is going to be the element over here.

18
00:01:09,650 --> 00:01:10,130
Right.

19
00:01:10,530 --> 00:01:13,970
That's the self uh healing locator that we have got.

20
00:01:13,970 --> 00:01:18,090
And now I'm going to say self dot find element.

21
00:01:18,530 --> 00:01:20,850
Uh and I'm not going to pass any attempts there.

22
00:01:21,130 --> 00:01:24,530
And I'm going to perform a click operation.

23
00:01:24,530 --> 00:01:30,490
So I think I need to use an await keyword there because this is an async method.

24
00:01:30,770 --> 00:01:34,050
If it's an async method, I think I should call this as async.

25
00:01:34,090 --> 00:01:36,090
If not, this code is not quite right.

26
00:01:36,410 --> 00:01:38,890
Uh, let me go fix that code as well.

27
00:01:39,850 --> 00:01:40,570
Something like this.

28
00:01:40,570 --> 00:01:42,170
So this is an asynchronous operation.

29
00:01:42,170 --> 00:01:47,050
So we need to make sure that the suffix has got async which is a best practice while we write the code.

30
00:01:47,410 --> 00:01:49,290
So find element async.

31
00:01:49,850 --> 00:01:57,690
Uh, and uh I'm going to uh see if I could able to click that particular element.

32
00:01:57,690 --> 00:02:04,610
Because now we have got the equivalent type there so I could able to perform a click operation.

33
00:02:04,610 --> 00:02:06,490
So this is going to find the element.

34
00:02:06,490 --> 00:02:11,210
So this is an AI element that we have got.

35
00:02:11,730 --> 00:02:16,170
Let's put a var there and AI element dot.

36
00:02:16,410 --> 00:02:20,090
And then I can see if I could able to click that right.

37
00:02:20,130 --> 00:02:21,890
This is what I'm trying to see if that works.

38
00:02:21,890 --> 00:02:27,090
But I also need to ensure that if I'm going to run this particular code, if this guy works, then.

39
00:02:27,130 --> 00:02:29,690
But yeah, I think this is just going to work anyway.

40
00:02:29,690 --> 00:02:33,970
So I don't think this is not going to fail any time for us.

41
00:02:33,970 --> 00:02:39,210
But if this fails for some reason, then we can see how that actually works.

42
00:02:39,210 --> 00:02:39,610
Right?

43
00:02:39,610 --> 00:02:42,290
So I'm going to put a breakpoint over here right now.

44
00:02:42,290 --> 00:02:45,010
And let's try to run and see how this actually works.

45
00:02:45,010 --> 00:02:47,490
So I'm going to go do a debug.

46
00:02:47,610 --> 00:02:51,770
So it's going to open the browsers and everything which is going to be just pretty much like how it

47
00:02:51,770 --> 00:02:52,890
was doing before.

48
00:02:52,930 --> 00:02:55,010
So I'm just going to let that guy to work.

49
00:02:55,490 --> 00:02:56,130
There you go.

50
00:02:56,410 --> 00:03:00,100
Uh, and now it is going gonna look at that.

51
00:03:00,100 --> 00:03:06,220
So we got the element from this particular uh try find with current strategy itself.

52
00:03:06,220 --> 00:03:11,980
So we get the element because you see that the element is not null because the element locator is correct.

53
00:03:11,980 --> 00:03:14,460
So the step one is already correct for us.

54
00:03:14,460 --> 00:03:17,220
So it is just going to return that particular element.

55
00:03:17,220 --> 00:03:19,140
And it is going to do a click operation.

56
00:03:19,140 --> 00:03:19,860
Look at that.

57
00:03:19,860 --> 00:03:22,540
The clicking is working because the locator is correct.

58
00:03:22,900 --> 00:03:24,660
So that first test is passing.

59
00:03:25,020 --> 00:03:29,100
The second test is I'm going to make the locator to be wrong this time.

60
00:03:29,140 --> 00:03:29,540
Yay!

61
00:03:29,860 --> 00:03:34,420
This is the place where I wanted to see if AI is going to be invoked.

62
00:03:34,700 --> 00:03:37,940
And we're going to run this test one more time.

63
00:03:38,620 --> 00:03:40,660
And look at that.

64
00:03:40,660 --> 00:03:42,540
We have gone in here.

65
00:03:42,740 --> 00:03:46,220
It's going to call the try find with current element.

66
00:03:46,220 --> 00:03:53,020
But this guy is going to throw an exception because there is no such element there like login like logins.

67
00:03:53,220 --> 00:03:57,500
That's why it's going to throw you an error and it's going to return you null there.

68
00:03:57,540 --> 00:03:57,820
Right.

69
00:03:57,860 --> 00:03:59,990
So the first step is failing.

70
00:04:00,270 --> 00:04:05,070
And now it's going to the second one which is basically going to be the locator strategy.

71
00:04:05,270 --> 00:04:07,990
And it's going to check if the count is equal to one.

72
00:04:08,430 --> 00:04:14,670
As I told you for the first time, because we're initializing this strategy in the constructor as the

73
00:04:14,670 --> 00:04:22,230
primary of the link text over here, this count is always going to be one.

74
00:04:22,230 --> 00:04:24,750
So this is going to return null as well.

75
00:04:24,750 --> 00:04:27,630
So eventually this step also fails.

76
00:04:28,750 --> 00:04:31,950
And next is our AI based auto healing approach.

77
00:04:31,950 --> 00:04:34,630
This is where things are going to be interesting.

78
00:04:34,830 --> 00:04:36,910
This is where our AI is going to come in.

79
00:04:37,070 --> 00:04:40,870
Now we are going to get the current strategy.

80
00:04:40,910 --> 00:04:42,750
We know that we have seen this before.

81
00:04:42,790 --> 00:04:48,710
This is the locator strategy that we have got, where we're going to get the locator type and the locator

82
00:04:48,750 --> 00:04:49,470
value.

83
00:04:49,710 --> 00:04:52,590
And we're also going to get the page source all of these.

84
00:04:53,110 --> 00:04:58,070
And then we are going to pass it to our Get healed.

85
00:04:58,070 --> 00:05:06,110
Look at our, uh, class or method that we have got, which is in turn going to call the execution from

86
00:05:06,150 --> 00:05:09,910
our large language model as well that we have built over there.

87
00:05:10,110 --> 00:05:10,390
Right.

88
00:05:10,430 --> 00:05:12,790
So we have built a lot of things there.

89
00:05:13,070 --> 00:05:16,070
So that's why it is all going to come up and look at that.

90
00:05:16,070 --> 00:05:21,950
We have got a look at our strategy for logins that we have like an alternative look at our strategy

91
00:05:21,950 --> 00:05:25,870
that we have got over here which we can now pass it through.

92
00:05:26,110 --> 00:05:31,630
See because it has got a lot of things like um like ID XPath as well.

93
00:05:31,630 --> 00:05:35,310
So it's going to go through each and every line there.

94
00:05:35,550 --> 00:05:41,830
Uh, you see that total number of uh count which is added is four instead of six because there were

95
00:05:41,830 --> 00:05:43,030
some empty as well.

96
00:05:43,670 --> 00:05:47,270
And now it is saying the total number of uh, count is six.

97
00:05:47,270 --> 00:05:54,390
But if you just go and see the locator strategy this time, you will notice that locator strategy count

98
00:05:54,470 --> 00:05:57,560
would have already increased to five.

99
00:05:57,640 --> 00:06:03,000
See the primary locator, which is this one, and the rest of the locator, which is which was not empty,

100
00:06:03,200 --> 00:06:07,840
is also added over here in the locator strategy, which is amazing.

101
00:06:07,880 --> 00:06:14,720
See all the alternative locators that we have got uh, apart from the primary is also sitting over there

102
00:06:14,720 --> 00:06:17,440
for us now, which is fabulous.

103
00:06:17,640 --> 00:06:21,000
And now we have all of these added thanks to the logic.

104
00:06:21,240 --> 00:06:26,120
And now we are going to do the find element async one more time.

105
00:06:26,120 --> 00:06:28,840
So this is the recursion that we are doing over here.

106
00:06:28,840 --> 00:06:32,120
So we are again getting back to the same uh method.

107
00:06:32,280 --> 00:06:37,480
Uh, and we know that this current strategy is going to fail because this is not correct.

108
00:06:37,480 --> 00:06:39,600
So it is just going to fail one more time.

109
00:06:39,800 --> 00:06:41,040
And I know that.

110
00:06:41,080 --> 00:06:43,160
So it's going to be failing.

111
00:06:43,160 --> 00:06:46,920
But the try alternative strategy is going to work this time.

112
00:06:46,960 --> 00:06:47,600
You know why?

113
00:06:47,880 --> 00:06:53,000
Because the count has increased from less than or equal to 1 to 5.

114
00:06:53,000 --> 00:06:56,530
So it is going to go to this for loop there for the first time.

115
00:06:56,650 --> 00:07:00,890
The current strategy is going to be there, which is equal to the strategy.

116
00:07:00,890 --> 00:07:02,410
So it is going to hit continue.

117
00:07:03,130 --> 00:07:09,290
And the second loop, it's going to come in with a new look here that it has found, which is nothing

118
00:07:09,290 --> 00:07:16,370
but the, uh, login link that it has got with the ID as login link there.

119
00:07:16,370 --> 00:07:19,690
So we are going to see if that is going to be working for us for clicking.

120
00:07:20,050 --> 00:07:22,930
So it is going to go look at that.

121
00:07:22,930 --> 00:07:25,370
It has found a strategy for the login link.

122
00:07:25,610 --> 00:07:30,170
And now it is going to go and see if the element can be identified.

123
00:07:30,330 --> 00:07:31,730
Oh look at that.

124
00:07:31,770 --> 00:07:37,690
The driver can able to identify the element using the new locator strategy which is fabulous.

125
00:07:37,930 --> 00:07:45,130
So it is working and now it is going to update the current strategy for us over there as the login link

126
00:07:45,170 --> 00:07:45,490
text.

127
00:07:45,490 --> 00:07:48,210
That is how it can identify the locator there.

128
00:07:48,210 --> 00:07:51,330
And now it's returning that element for us over here.

129
00:07:51,890 --> 00:07:56,530
Uh, the alternative element which is great.

130
00:07:56,530 --> 00:08:01,050
And now it doesn't even have to run this particular code, because it's going to return the element

131
00:08:01,050 --> 00:08:08,970
right now, and it is going to go and click the login link, this time with the healed method as well.

132
00:08:09,170 --> 00:08:12,570
Ooh, look at that guys, this is working.

133
00:08:13,250 --> 00:08:21,010
You have written a successful AI auto healing code without doing much of a sweating there, because

134
00:08:21,050 --> 00:08:27,730
just you have called the self-healing locator find element async and boom, you're done.

135
00:08:27,770 --> 00:08:29,610
Your code is already there.

136
00:08:29,610 --> 00:08:29,970
Guys.

137
00:08:29,970 --> 00:08:36,050
We have built a successful locator strategy approach already in our next section.

138
00:08:36,170 --> 00:08:39,730
The reason why I wanted to go with next section is because we have been sitting in this section for

139
00:08:39,730 --> 00:08:46,010
a long time, is we are going to move this code to the page object model code, and we are going to

140
00:08:46,010 --> 00:08:53,290
see how we can start using it with our existing page object model code over here, which we are going

141
00:08:53,330 --> 00:08:55,850
to be doing in our next section.


==================================================================================


section 7. Using Self Healing Locator in Page Object Model code of Selenium


