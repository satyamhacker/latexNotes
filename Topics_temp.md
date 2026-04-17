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

