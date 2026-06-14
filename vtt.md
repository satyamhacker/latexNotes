# Section 1: Introduction

1
00:00:00,520 --> 00:00:04,300
(Transcribed by TurboScribe. Go Unlimited to remove this message.) API stands for Application Programming Interface, and in

2
00:00:04,300 --> 00:00:07,500
simple terms, APIs allow us to connect applications

3
00:00:07,500 --> 00:00:08,020
together.

4
00:00:08,340 --> 00:00:10,300
It sets the rules for which two entities

5
00:00:10,300 --> 00:00:13,640
can share information, almost like a mediator between

6
00:00:13,640 --> 00:00:15,460
one application and another.

7
00:00:16,040 --> 00:00:18,140
So if we think about an application, it's

8
00:00:18,140 --> 00:00:20,020
made up of lots of smaller pieces of

9
00:00:20,020 --> 00:00:23,300
code that do things and return some results.

10
00:00:23,900 --> 00:00:26,220
APIs allow us to connect these smaller pieces

11
00:00:26,220 --> 00:00:29,660
of code or applications together to create a

12
00:00:29,660 --> 00:00:30,840
larger application.

13
00:00:31,240 --> 00:00:33,420
For example, your phone may want to display

14
00:00:33,420 --> 00:00:36,180
the weather in your location and display an

15
00:00:36,180 --> 00:00:38,180
alert if you're likely to need an umbrella

16
00:00:38,180 --> 00:00:39,360
on your commute today.

17
00:00:39,600 --> 00:00:41,800
To do this, the application needs to know

18
00:00:41,800 --> 00:00:42,480
two things.

19
00:00:42,840 --> 00:00:45,760
Firstly, where you are, and secondly, what is

20
00:00:45,760 --> 00:00:47,220
the weather at that location.

21
00:00:47,860 --> 00:00:50,500
Your application can use API calls to gather

22
00:00:50,500 --> 00:00:53,820
this information, process it, and display the results

23
00:00:53,820 --> 00:00:54,360
for you.

24
00:00:54,700 --> 00:00:56,480
In this case, all the developer has to

25
00:00:56,480 --> 00:00:59,100
worry about is handling the information that comes

26
00:00:59,100 --> 00:01:01,880
back and the logic of calculating the umbrella

27
00:01:01,880 --> 00:01:02,360
alerts.

28
00:01:02,740 --> 00:01:04,300
They don't need to go out and build

29
00:01:04,300 --> 00:01:07,120
weather stations and create their own proprietary weather

30
00:01:07,120 --> 00:01:09,720
models or ask the user where they are.

31
00:01:10,260 --> 00:01:12,880
To give a more abstract example, my favourite

32
00:01:12,880 --> 00:01:14,220
so far is the restaurant.

33
00:01:14,820 --> 00:01:16,860
You have a menu and the kitchen prepares

34
00:01:16,860 --> 00:01:17,420
your food.

35
00:01:17,940 --> 00:01:20,220
Your waiter is the link between you and

36
00:01:20,220 --> 00:01:20,680
the kitchen.

37
00:01:21,080 --> 00:01:22,500
They are in fact the API.

38
00:01:22,500 --> 00:01:25,040
They take your order and return with the

39
00:01:25,040 --> 00:01:25,320
food.

40
00:01:25,760 --> 00:01:27,640
Everything that happens in the kitchen is hidden,

41
00:01:28,120 --> 00:01:30,620
which is called abstraction, and means that we

42
00:01:30,620 --> 00:01:32,520
don't actually need to worry about how the

43
00:01:32,520 --> 00:01:34,740
kitchen does its job, just as long as

44
00:01:34,740 --> 00:01:36,740
we get the response, in this case the

45
00:01:36,740 --> 00:01:37,920
food we ordered, back.

46
00:01:38,440 --> 00:01:40,560
We'll talk more about abstraction a little bit

47
00:01:40,560 --> 00:01:41,100
later on.

48
00:01:41,600 --> 00:01:43,160
That's it for this video, and in the

49
00:01:43,160 --> 00:01:44,860
next one, we'll be taking a closer look

50
00:01:44,860 --> 00:01:47,360
at some hands-on examples and how we

51
00:01:47,360 --> 00:01:49,020
interact with APIs.

52
00:01:49,920 --> 00:01:50,820
See you in the next video!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,260 --> 00:00:01,540
(Transcribed by TurboScribe. Go Unlimited to remove this message.) In this video we're going to take a

2
00:00:01,540 --> 00:00:03,760
quick look at some API endpoints so that

3
00:00:03,760 --> 00:00:05,800
we can get familiar with what to expect

4
00:00:05,800 --> 00:00:08,940
and how to interact with those API endpoints.

5
00:00:09,480 --> 00:00:11,200
You don't need to follow along right now,

6
00:00:11,380 --> 00:00:13,280
in the next section we'll go through setting

7
00:00:13,280 --> 00:00:15,300
up, configuring and how to use all of

8
00:00:15,300 --> 00:00:16,700
the tools that I'm about to show you,

9
00:00:16,980 --> 00:00:18,260
but this is just a hands-on demo

10
00:00:18,260 --> 00:00:20,620
to help you visualise the theory that we've

11
00:00:20,620 --> 00:00:21,220
talked about.

12
00:00:21,640 --> 00:00:24,660
So here we are at the CatFacts API

13
00:00:24,660 --> 00:00:28,700
or CatFacts.Ninja API and we have some

14
00:00:28,700 --> 00:00:30,880
documentation here and it gives us two main

15
00:00:30,880 --> 00:00:31,400
sections.

16
00:00:31,759 --> 00:00:33,740
One is the breeds and one is the

17
00:00:33,740 --> 00:00:35,380
facts, so we can click into these to

18
00:00:35,380 --> 00:00:37,180
see which endpoints exist.

19
00:00:37,920 --> 00:00:39,740
And the easiest way to get some data

20
00:00:39,740 --> 00:00:42,380
from an API endpoint is simply to browse

21
00:00:42,380 --> 00:00:42,960
to it.

22
00:00:43,180 --> 00:00:45,360
So if we look at this slash fact,

23
00:00:45,620 --> 00:00:47,280
it returns a random fact.

24
00:00:47,360 --> 00:00:49,720
So all I'm going to do is copy

25
00:00:49,720 --> 00:00:54,300
this URL, paste this and go to slash

26
00:00:54,300 --> 00:00:56,380
fact and see what comes back.

27
00:00:56,920 --> 00:00:58,220
And if I zoom in a little bit,

28
00:00:58,380 --> 00:01:01,500
we have the fact Abraham Lincoln loved cats.

29
00:01:01,820 --> 00:01:03,160
He had four of them while he lived

30
00:01:03,160 --> 00:01:04,180
in the White House.

31
00:01:04,740 --> 00:01:06,560
I didn't know that, so that's quite cool.

32
00:01:07,380 --> 00:01:10,280
We also get back this length as well

33
00:01:10,280 --> 00:01:12,300
and if we come back to the documentation

34
00:01:12,300 --> 00:01:16,300
here, we do have this max length parameter.

35
00:01:16,680 --> 00:01:18,700
So within the documentation it's telling us that

36
00:01:18,700 --> 00:01:20,920
we can specify a max length.

37
00:01:21,020 --> 00:01:23,960
So I'm just going to copy this, come

38
00:01:23,960 --> 00:01:26,140
back to the facts and then add this

39
00:01:26,140 --> 00:01:29,260
as a parameter and hit enter.

40
00:01:29,600 --> 00:01:32,880
And we can see that indeed the fact

41
00:01:32,880 --> 00:01:36,140
that's passed back cats have supersonic hearing is

42
00:01:36,140 --> 00:01:38,840
a length of 28, so less than 30

43
00:01:38,840 --> 00:01:39,820
that's specified.

44
00:01:40,040 --> 00:01:41,840
And if we hit enter again, we get

45
00:01:41,840 --> 00:01:44,100
a different one and all of them are

46
00:01:44,100 --> 00:01:45,420
less than 30.

47
00:01:45,680 --> 00:01:48,280
Another way we can interact with API endpoints

48
00:01:48,280 --> 00:01:49,560
is through burp suite.

49
00:01:49,860 --> 00:01:51,660
So I already have this set up and

50
00:01:51,660 --> 00:01:53,180
ready to go and in the next section

51
00:01:53,180 --> 00:01:54,600
I'll show you how to get this set

52
00:01:54,600 --> 00:01:55,240
up as well.

53
00:01:55,800 --> 00:01:57,700
And we just come into burp suite, we

54
00:01:57,700 --> 00:02:01,720
come into proxy, HTTP history, and you can

55
00:02:01,720 --> 00:02:04,660
see actually the requests that I've sent already.

56
00:02:05,260 --> 00:02:07,259
And I'm just going to move myself out

57
00:02:07,259 --> 00:02:07,759
of the way.

58
00:02:08,560 --> 00:02:09,039
Here we go.

59
00:02:11,780 --> 00:02:13,740
And you can see that we have our

60
00:02:13,740 --> 00:02:17,040
request here, get slash fact to cat facts

61
00:02:17,040 --> 00:02:19,880
dot ninja, and here is our response, 200

62
00:02:19,880 --> 00:02:22,580
okay, and here is the fact that is

63
00:02:22,580 --> 00:02:24,040
returned at the end.

64
00:02:25,380 --> 00:02:27,860
Now something that's really useful in burp suite

65
00:02:27,860 --> 00:02:29,740
that we'll be using a lot throughout the

66
00:02:29,740 --> 00:02:31,100
course is called the repeater.

67
00:02:31,360 --> 00:02:34,160
So you can press ctrl r or you

68
00:02:34,160 --> 00:02:37,200
can right click and send to repeater to

69
00:02:37,200 --> 00:02:39,880
send a request to the repeater tab.

70
00:02:40,420 --> 00:02:42,700
Now here what we have is we have

71
00:02:42,700 --> 00:02:45,240
the request but we don't have any response.

72
00:02:45,980 --> 00:02:47,480
And if we come back here, we actually

73
00:02:47,480 --> 00:02:50,040
look, we can't actually modify this request at

74
00:02:50,040 --> 00:02:50,200
all.

75
00:02:50,260 --> 00:02:51,200
We can't do anything with it.

76
00:02:51,220 --> 00:02:52,620
We can see what we sent and what

77
00:02:52,620 --> 00:02:54,940
we got back, but with the repeater we

78
00:02:54,940 --> 00:02:55,960
can modify things.

79
00:02:56,100 --> 00:02:58,460
So for example I can remove the cookie

80
00:02:58,460 --> 00:03:00,800
and then send the request again.

81
00:03:00,960 --> 00:03:02,140
And you can see that it tries to

82
00:03:02,140 --> 00:03:05,500
set a new cookie, but obviously in this

83
00:03:05,500 --> 00:03:07,600
way we can start to interact with the

84
00:03:07,600 --> 00:03:11,660
application in a manual way to test API

85
00:03:11,660 --> 00:03:12,540
endpoints.

86
00:03:12,860 --> 00:03:16,120
And for example here we have fact and

87
00:03:16,120 --> 00:03:17,480
we have the max length is 100.

88
00:03:18,060 --> 00:03:20,300
What happens if we pass minus one?

89
00:03:20,460 --> 00:03:21,760
Will this break the application?

90
00:03:22,180 --> 00:03:23,520
Will this have some strange behaviour?

91
00:03:24,260 --> 00:03:26,620
It seems like it handles it gracefully and

92
00:03:26,620 --> 00:03:28,800
just returns nothing, but this is a good

93
00:03:28,800 --> 00:03:31,920
way to start testing API endpoints.

94
00:03:33,160 --> 00:03:34,860
So the next way we're going to look

95
00:03:34,860 --> 00:03:37,540
at interacting with our API endpoints is by

96
00:03:37,540 --> 00:03:38,880
using postman.

97
00:03:39,380 --> 00:03:42,240
So I'll go through the interface and kind

98
00:03:42,240 --> 00:03:44,520
of an introduction to postman in the later

99
00:03:44,520 --> 00:03:46,880
section, because there's quite a lot to look

100
00:03:46,880 --> 00:03:48,720
at, but all we're going to do this

101
00:03:48,720 --> 00:03:54,920
time is grab this endpoint from here and

102
00:03:54,920 --> 00:03:56,920
put it into a get request.

103
00:03:57,160 --> 00:03:59,100
So we can just copy and paste this

104
00:03:59,100 --> 00:04:02,060
in, select get from here if it's set

105
00:04:02,060 --> 00:04:05,380
to something else, hit send, and you can

106
00:04:05,380 --> 00:04:07,960
see that we get some information back.

107
00:04:08,120 --> 00:04:10,620
So the average cat can jump eight feet

108
00:04:10,620 --> 00:04:13,540
in a single bound, so that's pretty impressive.

109
00:04:14,640 --> 00:04:16,320
And here of course, same as web suite,

110
00:04:16,399 --> 00:04:18,860
we can inspect things like the cookies, the

111
00:04:18,860 --> 00:04:22,120
headers, and we can also modify the request

112
00:04:22,120 --> 00:04:22,660
as well.

113
00:04:22,740 --> 00:04:24,760
So we can come back and put in

114
00:04:24,760 --> 00:04:27,960
our max length and the value, let's say

115
00:04:27,960 --> 00:04:32,240
30, send this back, and we get another

116
00:04:32,240 --> 00:04:33,120
cat fact.

117
00:04:33,760 --> 00:04:35,400
So this gives us a lot more control

118
00:04:35,400 --> 00:04:37,460
over than just using the browser.

119
00:04:37,940 --> 00:04:41,140
Obviously postman and burp suite both have pros

120
00:04:41,140 --> 00:04:43,560
and cons to them, and we'll be exploring

121
00:04:43,560 --> 00:04:46,320
both throughout this course, because I think you

122
00:04:46,320 --> 00:04:48,100
should always use the right tool for the

123
00:04:48,100 --> 00:04:48,980
right situation.

124
00:04:49,320 --> 00:04:51,740
And sometimes it's hard to make that call,

125
00:04:51,840 --> 00:04:53,100
but if we know how to use both,

126
00:04:53,160 --> 00:04:54,780
then we're going to be much better equipped

127
00:04:54,780 --> 00:04:57,940
to dealing with any APIs that come our

128
00:04:57,940 --> 00:04:58,240
way.

129
00:04:58,240 --> 00:05:00,300
So the final thing I want to share

130
00:05:00,300 --> 00:05:01,720
with you is curl.

131
00:05:01,940 --> 00:05:03,640
So I'm just going to come over to

132
00:05:03,640 --> 00:05:07,020
my terminal and open a new tab, and

133
00:05:07,020 --> 00:05:09,320
it's always useful to be able to use

134
00:05:09,320 --> 00:05:11,400
the terminal if you need to quickly test

135
00:05:11,400 --> 00:05:13,240
something or write a short script.

136
00:05:13,760 --> 00:05:15,300
Sometimes we need to be able to do

137
00:05:15,300 --> 00:05:17,300
something that doesn't come standard in the tools

138
00:05:17,300 --> 00:05:19,480
we use, so instead of messing around with

139
00:05:19,480 --> 00:05:22,380
extensions, we could just use tools like bash

140
00:05:22,380 --> 00:05:25,140
and curl and get the job done.

141
00:05:26,200 --> 00:05:33,560
So here I'm just going to curl https://catfact

142
00:05:33,560 --> 00:05:38,660
.ninja and call slash fact, and you can

143
00:05:38,660 --> 00:05:41,780
see that as before it comes back with

144
00:05:41,780 --> 00:05:42,660
a response.

145
00:05:43,340 --> 00:05:45,100
And if we want to see more information

146
00:05:45,100 --> 00:05:47,260
like the headers, we can use verbose mode.

147
00:05:47,320 --> 00:05:49,320
So we can just send the same request

148
00:05:49,320 --> 00:05:52,980
with "-v", and send it again, and we

149
00:05:52,980 --> 00:05:54,460
get all the information we need.

150
00:05:54,740 --> 00:05:56,640
And we can pass that to another command

151
00:05:56,640 --> 00:05:59,260
line tool, or save the output, or do

152
00:05:59,260 --> 00:06:00,780
whatever we want with it.

153
00:06:00,980 --> 00:06:02,340
And that's it for this video!

154
00:06:02,700 --> 00:06:04,160
Next up we're going to look at different

155
00:06:04,160 --> 00:06:06,620
types of APIs, and then a brief introduction

156
00:06:06,620 --> 00:06:10,420
to API security, before we go into setting

157
00:06:10,420 --> 00:06:12,200
up our lab in the next section.

158
00:06:12,460 --> 00:06:13,080
I'll see you there!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.340 --> 00:00:01.820
(Transcribed by TurboScribe. Go Unlimited to remove this message.) In this section, we'll run through a little

2
00:00:01.820 --> 00:00:04.040
bit of terminology and types of APIs.

3
00:00:04.640 --> 00:00:06.740
So far, we've been using the generic term

4
00:00:06.740 --> 00:00:09.280
API, but there are different ways of implementing

5
00:00:09.280 --> 00:00:09.640
them.

6
00:00:09.980 --> 00:00:11.620
Let's start with REST APIs.

7
00:00:12.000 --> 00:00:14.260
These are also known as RESTful APIs.

8
00:00:14.860 --> 00:00:18.600
REST stands for Representational State Transfer, and of

9
00:00:18.600 --> 00:00:20.920
course it's an API, all the same, except

10
00:00:20.920 --> 00:00:22.680
there are some constraints and rules you need

11
00:00:22.680 --> 00:00:25.560
to abide by when designing and building them.

12
00:00:25.560 --> 00:00:28.560
Some examples of these constraints for RESTful APIs

13
00:00:28.560 --> 00:00:31.960
are they must use a server-client architecture,

14
00:00:32.360 --> 00:00:34.780
so the server and clients are separate entities.

15
00:00:35.300 --> 00:00:38.560
They must also use HTTP methods, such as

16
00:00:38.560 --> 00:00:41.640
GET, POST, PUT, and DELETE to manipulate data.

17
00:00:42.260 --> 00:00:44.280
And finally, they must be stateless, so each

18
00:00:44.280 --> 00:00:47.120
individual request can be understood by the server.

19
00:00:47.620 --> 00:00:49.560
There's a little bit more to RESTful APIs

20
00:00:49.560 --> 00:00:51.900
than that, but this gives us enough to

21
00:00:51.900 --> 00:00:52.580
start with.

22
00:00:52.580 --> 00:00:54.820
Just try to remember that API is more

23
00:00:54.820 --> 00:00:57.640
of an architectural pattern rather than a standard.

24
00:00:58.040 --> 00:01:00.780
Next up, we have public, partner, and private

25
00:01:00.780 --> 00:01:02.840
APIs, and these are a little bit more

26
00:01:02.840 --> 00:01:03.379
straightforward.

27
00:01:04.019 --> 00:01:06.380
A public API is simply an API that

28
00:01:06.380 --> 00:01:09.000
anyone can use and interact with, like the

29
00:01:09.000 --> 00:01:11.000
previous CAS API that we looked at.

30
00:01:11.200 --> 00:01:13.700
Other popular examples might include Twitter or the

31
00:01:13.700 --> 00:01:14.840
Google Maps API.

32
00:01:15.240 --> 00:01:17.520
Partner APIs might be shared between a number

33
00:01:17.520 --> 00:01:18.120
of companies.

34
00:01:18.360 --> 00:01:20.780
For example, a central bank might publish data

35
00:01:20.780 --> 00:01:23.560
for other banks to access via an API.

36
00:01:23.960 --> 00:01:26.420
And finally, we have private APIs, which are

37
00:01:26.420 --> 00:01:28.620
generally used within a single organisation.

38
00:01:29.040 --> 00:01:30.860
Maybe you work for a tech company that

39
00:01:30.860 --> 00:01:33.780
publishes lots of applications, so you might want

40
00:01:33.780 --> 00:01:35.960
to consider one set of APIs to handle

41
00:01:35.960 --> 00:01:39.680
authentication and authorisation of customers across all of

42
00:01:39.680 --> 00:01:40.760
those applications.

43
00:01:42.460 --> 00:01:45.560
Next is the term endpoints, and I've used

44
00:01:45.560 --> 00:01:46.940
this a bunch of times already.

45
00:01:46.940 --> 00:01:49.260
This term gets thrown around a lot, and

46
00:01:49.260 --> 00:01:51.760
you'll hear it probably in every video in

47
00:01:51.760 --> 00:01:52.360
this course.

48
00:01:52.740 --> 00:01:54.540
When you're scoping pen tests, you might hear

49
00:01:54.540 --> 00:01:57.360
things like, ah, there are about 20 endpoints,

50
00:01:57.560 --> 00:01:59.760
or all the endpoints are rate limited.

51
00:02:00.120 --> 00:02:03.060
So an endpoint is a specific URL, uniform

52
00:02:03.060 --> 00:02:07.100
resource locator, that represents a resource or service

53
00:02:07.100 --> 00:02:09.860
that can be accessed by making requests to

54
00:02:09.860 --> 00:02:10.720
that API.

55
00:02:10.720 --> 00:02:13.280
For example, going back to our cat API,

56
00:02:13.560 --> 00:02:16.060
slash facts is an endpoint that returns a

57
00:02:16.060 --> 00:02:18.160
list of all of the cat facts known

58
00:02:18.160 --> 00:02:19.020
to humanity.

59
00:02:19.400 --> 00:02:20.660
Well, maybe not all of them.

60
00:02:21.080 --> 00:02:23.140
We could also make calls to the slash

61
00:02:23.140 --> 00:02:26.160
breeds endpoint, which would then return a list

62
00:02:26.160 --> 00:02:27.300
of known breeds.

63
00:02:28.200 --> 00:02:30.480
These are both API endpoints.

64
00:02:30.740 --> 00:02:33.000
Next up, we have methods that are often

65
00:02:33.000 --> 00:02:35.480
documented with a individual endpoint.

66
00:02:36.100 --> 00:02:38.320
So some of the basic ones are get

67
00:02:38.320 --> 00:02:42.000
method, which retrieves a resource, a post method,

68
00:02:42.140 --> 00:02:45.420
which creates a resource, put, which updates or

69
00:02:45.420 --> 00:02:49.180
creates within an existing resource, patch, which partially

70
00:02:49.180 --> 00:02:52.660
modifies an existing resource, and delete that removes

71
00:02:52.660 --> 00:02:53.300
a resource.

72
00:02:53.600 --> 00:02:54.860
So that's it for terminology.

73
00:02:55.220 --> 00:02:57.320
Next up, we have an overview of API

74
00:02:57.320 --> 00:02:57.980
security.

75
00:02:58.260 --> 00:02:59.240
So I'll catch you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.720 --> 00:00:03.480
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Realistically speaking, APIs can be subject to many

2
00:00:03.480 --> 00:00:07.380
common web attacks such as injection, IDOR, and

3
00:00:07.380 --> 00:00:08.640
broken access control.

4
00:00:09.160 --> 00:00:10.880
Now don't worry if you don't know what

5
00:00:10.880 --> 00:00:13.020
these attacks are yet, we will cover them

6
00:00:13.020 --> 00:00:14.200
in the coming modules.

7
00:00:14.700 --> 00:00:17.360
But something to remember here is that even

8
00:00:17.360 --> 00:00:19.480
though APIs tend to be more flexible and

9
00:00:19.480 --> 00:00:22.320
scalable, they are not inherently more secure than

10
00:00:22.320 --> 00:00:24.580
any other method of web development.

11
00:00:25.060 --> 00:00:27.060
It all comes down to how you design

12
00:00:27.060 --> 00:00:29.820
and build your APIs along with the security

13
00:00:29.820 --> 00:00:31.619
controls around them.

14
00:00:31.880 --> 00:00:34.340
If you look into API development and usage

15
00:00:34.340 --> 00:00:36.240
over the last few years, you'll see that

16
00:00:36.240 --> 00:00:37.820
it has increased dramatically.

17
00:00:38.280 --> 00:00:41.460
Unsurprisingly, this comes with more attacks on API

18
00:00:41.460 --> 00:00:42.280
endpoints.

19
00:00:43.120 --> 00:00:45.660
Coupled with rapid development and that an API

20
00:00:45.660 --> 00:00:48.520
might be updated weekly or even daily, the

21
00:00:48.520 --> 00:00:51.820
potential for security issues to arise is high.

22
00:00:52.480 --> 00:00:55.180
Another somewhat common issue is that of legacy

23
00:00:55.180 --> 00:00:56.840
or zombie APIs.

24
00:00:57.400 --> 00:01:00.360
Deprecated APIs can be left unchecked for long

25
00:01:00.360 --> 00:01:02.580
periods of time and they are a perfect

26
00:01:02.580 --> 00:01:05.880
target for an attacker, especially if they're not

27
00:01:05.880 --> 00:01:07.100
actively being monitored.

28
00:01:07.840 --> 00:01:12.160
So as penetration testers, security researchers, security engineers,

29
00:01:12.260 --> 00:01:14.260
or developers, we need to be able to

30
00:01:14.260 --> 00:01:18.460
effectively interact with, understand, and test our APIs

31
00:01:18.460 --> 00:01:20.380
against all sorts of attacks.

32
00:01:20.380 --> 00:01:22.380
And that's it for this short introduction.

33
00:01:22.820 --> 00:01:24.060
The rest of the course is going to

34
00:01:24.060 --> 00:01:26.460
be fully hands-on, and we're going to

35
00:01:26.460 --> 00:01:28.860
set up our lab and jump straight into

36
00:01:28.860 --> 00:01:32.340
how to attack and exploit API endpoints.

37
00:01:32.640 --> 00:01:33.200
I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
==================================================================================

# Section 2: Lab Setup

WEBVTT

1
00:00:00.380 --> 00:00:03.300
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Right, let's take a quick look at Postman.

2
00:00:03.580 --> 00:00:05.580
So if I bring you over to my

3
00:00:05.580 --> 00:00:08.860
VM, and you can see I've already loaded

4
00:00:08.860 --> 00:00:12.100
up Postman, and I've also signed in as

5
00:00:12.100 --> 00:00:12.420
well.

6
00:00:12.540 --> 00:00:15.020
So if your front page looks a little

7
00:00:15.020 --> 00:00:17.720
bit different, then feel free to create a

8
00:00:17.720 --> 00:00:20.740
free account, log yourself in, and that's going

9
00:00:20.740 --> 00:00:22.400
to enable workspaces.

10
00:00:22.980 --> 00:00:25.680
And workspaces are quite useful, they're basically like

11
00:00:25.680 --> 00:00:28.620
projects, and being able to create multiple workspaces

12
00:00:28.620 --> 00:00:31.439
for different applications is pretty handy.

13
00:00:31.640 --> 00:00:33.380
So I do recommend you sign up a

14
00:00:33.380 --> 00:00:35.340
free account and do this.

15
00:00:35.680 --> 00:00:37.540
So I'm just going to come in, and

16
00:00:37.540 --> 00:00:40.240
I'm just going to create a workspace, and

17
00:00:40.240 --> 00:00:42.340
I'm just going to call this API test,

18
00:00:43.020 --> 00:00:44.780
and then I'm just going to make it

19
00:00:44.780 --> 00:00:48.700
personal, and then create a workspace, and here

20
00:00:48.700 --> 00:00:49.100
we go.

21
00:00:49.780 --> 00:00:52.120
One thing I forgot to mention, if you

22
00:00:52.120 --> 00:00:54.240
load it up, and you're not in dark

23
00:00:54.240 --> 00:00:56.680
mode already, if you come into this cog

24
00:00:56.680 --> 00:00:59.620
here, and go settings, and come to themes,

25
00:00:59.900 --> 00:01:02.100
and you prefer dark mode, then click dark

26
00:01:02.100 --> 00:01:02.420
mode.

27
00:01:02.820 --> 00:01:05.100
Obviously I have my mindset to system default,

28
00:01:05.280 --> 00:01:08.640
so it's matching my system settings, but you

29
00:01:08.640 --> 00:01:09.780
can change that in here.

30
00:01:10.320 --> 00:01:12.240
I know that some people like to work

31
00:01:12.240 --> 00:01:15.840
late at night, and the bright version of

32
00:01:15.840 --> 00:01:17.960
Postman can be a little blinding.

33
00:01:18.260 --> 00:01:21.640
So if workspaces are basically projects, then collections

34
00:01:21.640 --> 00:01:23.740
are groups of requests.

35
00:01:24.120 --> 00:01:26.560
So we can come in here, and we're

36
00:01:26.560 --> 00:01:29.020
in our workspace, so we're in the API

37
00:01:29.020 --> 00:01:31.600
test workspace, and we can just click new,

38
00:01:31.980 --> 00:01:34.200
and what we want to do is a

39
00:01:34.200 --> 00:01:35.940
new HTTP request.

40
00:01:36.960 --> 00:01:39.520
In fact, actually let's create a new collection.

41
00:01:40.020 --> 00:01:44.000
So let's do new collection, and we'll edit

42
00:01:44.000 --> 00:01:45.980
this, I think you can rename with ctrl

43
00:01:45.980 --> 00:01:47.660
e, so I'm just going to call this

44
00:01:47.660 --> 00:01:50.520
cats, or you can click on the three

45
00:01:50.520 --> 00:01:55.260
dots, and yeah there's rename, duplicate, export, everything

46
00:01:55.260 --> 00:01:57.980
you need in here as well, and in

47
00:01:57.980 --> 00:01:59.920
here what we want to do is add

48
00:01:59.920 --> 00:02:00.880
a request.

49
00:02:02.160 --> 00:02:06.680
So I'm just going to call this cat

50
00:02:06.680 --> 00:02:10.700
breeds, and I already have a URL sitting

51
00:02:10.700 --> 00:02:12.660
on my clipboard, so we're going to go

52
00:02:12.660 --> 00:02:16.500
to catfacts.ninja slash breeds, and we don't,

53
00:02:16.600 --> 00:02:18.860
I think we don't need any other parameters,

54
00:02:19.280 --> 00:02:22.200
we can just send this request, and we

55
00:02:22.200 --> 00:02:23.800
get the response back.

56
00:02:24.180 --> 00:02:27.020
And if we want to create another request,

57
00:02:27.140 --> 00:02:30.080
we can just come into our collection, and

58
00:02:30.080 --> 00:02:34.040
add request, and we'll do the same.

59
00:02:34.280 --> 00:02:38.740
So we'll call this one cat facts, and

60
00:02:38.740 --> 00:02:42.340
instead of doing the breeds, all we want

61
00:02:42.340 --> 00:02:44.680
to do is paste this, and change this

62
00:02:44.680 --> 00:02:45.660
to fact.

63
00:02:47.320 --> 00:02:49.320
And as you can see, we can start

64
00:02:49.320 --> 00:02:52.780
to build out our collection, and you might

65
00:02:52.780 --> 00:02:56.780
want to create another collection called dogs for

66
00:02:56.780 --> 00:03:00.560
example, and personally what I tend to do

67
00:03:00.560 --> 00:03:03.680
on applications when I'm working with postman is,

68
00:03:04.180 --> 00:03:06.620
if I can't import a collection, which I'll

69
00:03:06.620 --> 00:03:08.080
show you how to do in a moment,

70
00:03:08.080 --> 00:03:12.800
I will create my collections based on functionality,

71
00:03:13.380 --> 00:03:16.300
or kind of logical groupings of endpoints.

72
00:03:16.460 --> 00:03:18.280
So if we have a forum, I might

73
00:03:18.280 --> 00:03:22.800
have endpoints like posting, and commenting, and editing

74
00:03:22.800 --> 00:03:25.540
posts in one collection, and I might have

75
00:03:25.540 --> 00:03:29.320
like administration activities such as update user, ban

76
00:03:29.320 --> 00:03:35.000
user, change user privileges in a separate collection

77
00:03:35.000 --> 00:03:35.580
as well.

78
00:03:35.660 --> 00:03:38.140
So that's my kind of personal workflow, but

79
00:03:38.140 --> 00:03:41.020
you can group your collections however you want.

80
00:03:41.640 --> 00:03:43.300
We'll get more into this later, but of

81
00:03:43.300 --> 00:03:45.320
course it's very easy to change the types

82
00:03:45.320 --> 00:03:47.800
of requests, and then add in a body,

83
00:03:48.200 --> 00:03:50.540
make it form data for example, but for

84
00:03:50.540 --> 00:03:52.440
now this is a very quick intro to

85
00:03:52.440 --> 00:03:52.960
postman.

86
00:03:53.740 --> 00:03:56.200
And something that we want to do is

87
00:03:56.200 --> 00:03:59.200
be able to import collections.

88
00:03:59.680 --> 00:04:02.800
So a lot of applications will have a

89
00:04:02.800 --> 00:04:05.760
collection of API endpoints ready to go, and

90
00:04:05.760 --> 00:04:07.420
so what we can do is we can

91
00:04:07.420 --> 00:04:08.200
choose files.

92
00:04:09.680 --> 00:04:13.300
I'm going to come to home, and then

93
00:04:13.300 --> 00:04:15.480
labs, and crappy.

94
00:04:15.820 --> 00:04:17.500
So this is one of the applications that

95
00:04:17.500 --> 00:04:19.720
we'll be looking at, not exclusively, but it

96
00:04:19.720 --> 00:04:23.160
is a pretty good open source API driven

97
00:04:23.160 --> 00:04:24.020
web application.

98
00:04:24.320 --> 00:04:28.000
And if we come into postman collections, you

99
00:04:28.000 --> 00:04:30.340
can see that we have the collection.json

100
00:04:30.340 --> 00:04:33.380
and the postman environment.json. So we want

101
00:04:33.380 --> 00:04:34.260
both of these.

102
00:04:34.840 --> 00:04:35.800
Now what we're going to do is click

103
00:04:35.800 --> 00:04:41.700
open, click import, and you can see that

104
00:04:41.700 --> 00:04:43.540
it's nicely separated out.

105
00:04:43.680 --> 00:04:48.310
So even though these are different applications, it's

106
00:04:48.310 --> 00:04:50.510
pulled them in as a collection, so our

107
00:04:50.510 --> 00:04:51.950
import is nice and clean.

108
00:04:53.390 --> 00:04:55.530
And then when we click down onto it,

109
00:04:55.630 --> 00:04:58.170
you can see all of the endpoints as

110
00:04:58.170 --> 00:04:58.450
well.

111
00:05:00.290 --> 00:05:02.750
So we can start using this and sending

112
00:05:02.750 --> 00:05:03.010
them.

113
00:05:03.410 --> 00:05:06.850
Now you'll notice that sometimes variables are used,

114
00:05:06.950 --> 00:05:08.210
and this says unresolved.

115
00:05:08.430 --> 00:05:11.130
If this is the case when you're working

116
00:05:11.130 --> 00:05:13.510
with your environment, you either need to import

117
00:05:13.510 --> 00:05:15.270
the environment, or you need to come to

118
00:05:15.270 --> 00:05:17.350
the top here, and you see how it

119
00:05:17.350 --> 00:05:20.670
says no environments, just click crappy, and then

120
00:05:20.670 --> 00:05:22.870
it will auto fill this as well.

121
00:05:23.290 --> 00:05:24.870
If we come back to no environment, you

122
00:05:24.870 --> 00:05:26.990
can manually set these variables as well by

123
00:05:26.990 --> 00:05:29.270
coming down and just clicking add new variable,

124
00:05:29.270 --> 00:05:31.630
and this will also do the trick.

125
00:05:32.050 --> 00:05:34.210
But there are a lot of variables and

126
00:05:34.210 --> 00:05:37.090
a lot of scripts used, which makes postman

127
00:05:37.090 --> 00:05:39.730
really really powerful for testing lots of APIs

128
00:05:39.730 --> 00:05:43.230
quickly, and it's good to get started with

129
00:05:43.230 --> 00:05:44.990
what the developers provided.

130
00:05:45.310 --> 00:05:47.790
So again, that was a very brief introduction

131
00:05:47.790 --> 00:05:50.850
to postman, and don't worry if you're new

132
00:05:50.850 --> 00:05:52.630
to postman and you're like, oh there's a

133
00:05:52.630 --> 00:05:53.870
lot of buttons and a lot of things

134
00:05:53.870 --> 00:05:55.050
to do and a lot of things to

135
00:05:55.050 --> 00:05:55.430
remember.

136
00:05:56.370 --> 00:05:57.790
We're going to go through all of it,

137
00:05:57.790 --> 00:06:00.430
and throughout the videos you'll get more and

138
00:06:00.430 --> 00:06:01.490
more comfortable with it.

139
00:06:01.670 --> 00:06:03.050
So we're going to kind of learn by

140
00:06:03.050 --> 00:06:04.590
doing, if that makes sense.

141
00:06:04.890 --> 00:06:06.710
I'll see you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.130 --> 00:00:02.250
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, we have one last thing to

2
00:00:02.250 --> 00:00:04.690
set up before we dive into the next

3
00:00:04.690 --> 00:00:05.230
section.

4
00:00:05.950 --> 00:00:08.050
So what I want you to do is,

5
00:00:08.170 --> 00:00:10.370
we're going to be utilizing a number of

6
00:00:10.370 --> 00:00:12.370
labs for the course.

7
00:00:12.610 --> 00:00:15.570
Some of them we've built as demonstrations to

8
00:00:15.570 --> 00:00:18.790
help you really understand vulnerabilities without the added

9
00:00:18.790 --> 00:00:22.010
complexity of large applications, and some of them

10
00:00:22.010 --> 00:00:22.810
open source.

11
00:00:22.810 --> 00:00:25.010
So the first thing I want you to

12
00:00:25.010 --> 00:00:26.710
do is come to Google.

13
00:00:32.040 --> 00:00:40.160
Oops, we'll switch off our proxy, and then

14
00:00:40.160 --> 00:00:44.460
we'll search for crappy API GitHub.

15
00:00:45.880 --> 00:00:48.520
And you can see this awasp slash crappy,

16
00:00:48.820 --> 00:00:50.600
completely ridiculous API.

17
00:00:52.560 --> 00:00:53.880
And I want you to come into here,

18
00:00:54.100 --> 00:00:57.040
and then click code, and then click this

19
00:00:57.040 --> 00:00:57.660
copy button.

20
00:00:57.820 --> 00:00:59.600
So this is going to click the link

21
00:00:59.600 --> 00:01:00.680
to the .git file.

22
00:01:02.020 --> 00:01:04.620
Come back to your terminal, and here we're

23
00:01:04.620 --> 00:01:05.580
in the home directory.

24
00:01:06.180 --> 00:01:07.960
So, whoops, no we're not, we're in the

25
00:01:07.960 --> 00:01:08.480
root directory.

26
00:01:08.820 --> 00:01:10.040
Now we're in the home directory.

27
00:01:10.660 --> 00:01:12.120
And what I like to do is, I

28
00:01:12.120 --> 00:01:13.600
don't like to dump loads of stuff in

29
00:01:13.600 --> 00:01:15.220
here, so I'm just going to make a

30
00:01:15.220 --> 00:01:18.660
directory called labs and cd labs.

31
00:01:19.500 --> 00:01:20.960
The rest of the labs that we're going

32
00:01:20.960 --> 00:01:22.560
to be using as part of the course,

33
00:01:22.680 --> 00:01:24.300
you'll see them as we go, and then

34
00:01:24.300 --> 00:01:26.160
you'll be able to pull them in, unzip

35
00:01:26.160 --> 00:01:27.500
them, and run them.

36
00:01:27.500 --> 00:01:29.080
So the only one we need to get

37
00:01:29.080 --> 00:01:31.680
up and running with is the crappy application

38
00:01:31.680 --> 00:01:32.500
for today.

39
00:01:33.000 --> 00:01:37.740
So git clone, and then paste, and we'll

40
00:01:37.740 --> 00:01:40.180
give this a minute to download the application.

41
00:01:41.400 --> 00:01:44.580
And before we can run this application, what

42
00:01:44.580 --> 00:01:46.000
we need to do is we need to

43
00:01:46.000 --> 00:01:48.680
install docker io and docker compose.

44
00:01:49.100 --> 00:01:52.080
So let's just clear this, and we'll just

45
00:01:52.080 --> 00:02:00.760
do sudo apt install docker.io. And we'll

46
00:02:00.760 --> 00:02:01.300
hit yes.

47
00:02:02.260 --> 00:02:03.980
You can also give it the dash y

48
00:02:03.980 --> 00:02:05.800
flag to automatically hit yes.

49
00:02:06.980 --> 00:02:08.660
And this will take a minute to install.

50
00:02:09.180 --> 00:02:11.060
Now if you get this error, this is

51
00:02:11.060 --> 00:02:12.520
quite easy to solve.

52
00:02:12.660 --> 00:02:14.280
So you can see that it gives us

53
00:02:14.280 --> 00:02:16.980
an error message saying unable to fetch some

54
00:02:16.980 --> 00:02:19.840
archives, maybe run sudo apt get update or

55
00:02:19.840 --> 00:02:21.320
try with fix missing.

56
00:02:21.620 --> 00:02:25.960
So we'll sudo apt update dash dash fix

57
00:02:25.960 --> 00:02:27.180
missing.

58
00:02:33.370 --> 00:02:34.750
Give this a minute to run.

59
00:02:37.330 --> 00:02:41.610
And now we can sudo apt install docker

60
00:02:41.610 --> 00:02:42.110
io.

61
00:02:44.520 --> 00:02:45.000
Yes.

62
00:02:47.850 --> 00:02:50.010
So here we get there are services installed

63
00:02:50.010 --> 00:02:52.170
on your system which need to be restarted.

64
00:02:52.270 --> 00:02:53.290
I'm just going to go with yes.

65
00:02:53.370 --> 00:02:55.010
I don't mind it restarting services.

66
00:02:58.640 --> 00:03:00.160
All right, and the next one we need

67
00:03:00.160 --> 00:03:04.260
is sudo apt install docker compose.

68
00:03:06.140 --> 00:03:07.360
And we'll go with yes.

69
00:03:10.940 --> 00:03:13.180
And which services should be restarted?

70
00:03:13.200 --> 00:03:14.740
I'm just going to hit enter to say

71
00:03:14.740 --> 00:03:15.020
okay.

72
00:03:16.100 --> 00:03:17.660
And then we should be good to go.

73
00:03:17.740 --> 00:03:19.340
Now we do get a little pop up

74
00:03:19.340 --> 00:03:22.500
in the top right hand corner saying that

75
00:03:22.500 --> 00:03:23.760
hey, we need to restart.

76
00:03:24.000 --> 00:03:25.840
So I'm just going to go ahead and

77
00:03:25.840 --> 00:03:27.040
restart my guest.

78
00:03:31.790 --> 00:03:34.410
And we can log ourselves back in.

79
00:03:38.240 --> 00:03:42.160
Come back to the terminal, cd labs, cd

80
00:03:42.160 --> 00:03:43.460
crappy.

81
00:03:44.100 --> 00:03:45.880
And for this one, most of the labs

82
00:03:45.880 --> 00:03:48.300
you'll just need to cd into the folder

83
00:03:48.300 --> 00:03:50.800
where the application is and sudo docker compose

84
00:03:50.800 --> 00:03:51.200
up.

85
00:03:51.620 --> 00:03:53.780
You'll see this in the following sections.

86
00:03:54.280 --> 00:03:56.020
But for crappy, we need to come into

87
00:03:56.020 --> 00:03:57.820
deploy slash docker.

88
00:03:59.300 --> 00:04:01.640
And then you can see the docker compose

89
00:04:01.640 --> 00:04:02.540
files are here.

90
00:04:02.680 --> 00:04:06.200
So sudo docker dash compose up.

91
00:04:11.560 --> 00:04:12.920
And this is going to take a little

92
00:04:12.920 --> 00:04:15.720
while to download everything it needs and spin

93
00:04:15.720 --> 00:04:16.720
up the application.

94
00:04:17.019 --> 00:04:18.899
The first time you do it, it'll take,

95
00:04:19.180 --> 00:04:20.140
you know, a little bit of time.

96
00:04:20.140 --> 00:04:22.240
But the next time you do it, because

97
00:04:22.240 --> 00:04:23.920
it doesn't need to download everything from the

98
00:04:23.920 --> 00:04:26.780
internet, it should spin up much, much faster.

99
00:04:27.040 --> 00:04:29.200
So within, you know, 20, 30 seconds, maybe.

100
00:04:42.170 --> 00:04:42.770
All right.

101
00:04:42.810 --> 00:04:44.890
So now it looks like everything is up

102
00:04:44.890 --> 00:04:45.490
and running.

103
00:04:45.630 --> 00:04:47.550
So we're going to come back into Firefox.

104
00:04:50.260 --> 00:04:54.600
And we're going to go to localhost 8888.

105
00:04:56.280 --> 00:04:58.360
And we get our login page.

106
00:04:58.360 --> 00:04:59.960
So if you don't see this just yet,

107
00:04:59.980 --> 00:05:01.780
make sure that everything is up and running.

108
00:05:01.860 --> 00:05:04.380
Usually you'll see crappy web requests like health

109
00:05:04.380 --> 00:05:05.220
checks and things.

110
00:05:06.120 --> 00:05:07.460
Give it a little bit more time.

111
00:05:07.700 --> 00:05:10.580
Otherwise, maybe spin it down again and try

112
00:05:10.580 --> 00:05:11.200
once more.

113
00:05:11.580 --> 00:05:13.700
So this is the main login page for

114
00:05:13.700 --> 00:05:15.740
the application that we'll be using throughout the

115
00:05:15.740 --> 00:05:16.040
course.

116
00:05:16.300 --> 00:05:17.920
And of course, we'll be using other applications

117
00:05:17.920 --> 00:05:18.520
as well.

118
00:05:19.160 --> 00:05:21.660
And just a heads up, this runs on

119
00:05:21.660 --> 00:05:22.480
8888.

120
00:05:22.540 --> 00:05:23.600
So don't forget that.

121
00:05:23.600 --> 00:05:26.500
And the other endpoint that you'll need is

122
00:05:26.500 --> 00:05:28.560
8025 as well.

123
00:05:28.680 --> 00:05:30.460
So this is the mail server that's connected

124
00:05:30.460 --> 00:05:31.500
to the application.

125
00:05:32.100 --> 00:05:34.040
So you'll see that once you log in,

126
00:05:34.200 --> 00:05:35.960
you'll get an email with some stuff.

127
00:05:36.500 --> 00:05:38.520
This is how you actually read the contents

128
00:05:38.520 --> 00:05:39.720
of that email.

129
00:05:40.080 --> 00:05:41.280
So that's really, really important.

130
00:05:42.140 --> 00:05:45.320
And if I close this, and I come

131
00:05:45.320 --> 00:05:47.060
back to Docker, and if I just hit

132
00:05:47.060 --> 00:05:49.680
control C, it's going to gracefully stop.

133
00:05:49.680 --> 00:05:51.940
We can force stop by hitting control C

134
00:05:51.940 --> 00:05:54.440
again, but better to let it spin down

135
00:05:54.440 --> 00:05:55.460
in its own time.

136
00:05:56.640 --> 00:05:58.500
Now, one other thing that I wanted to

137
00:05:58.500 --> 00:06:00.420
show you while it's doing that is if

138
00:06:00.420 --> 00:06:02.680
I come back into the labs folder, is

139
00:06:02.680 --> 00:06:05.000
that if we're running lots of different Docker

140
00:06:05.000 --> 00:06:08.780
containers, sometimes your file system can become full

141
00:06:08.780 --> 00:06:10.500
with Docker files.

142
00:06:11.060 --> 00:06:12.520
And if you have this problem and you

143
00:06:12.520 --> 00:06:13.900
want to clean out all of your old

144
00:06:13.900 --> 00:06:16.920
containers, I have a script to do that

145
00:06:16.920 --> 00:06:17.500
for you.

146
00:06:17.500 --> 00:06:19.860
So this is also included in the text

147
00:06:19.860 --> 00:06:21.240
notes as part of this section.

148
00:06:21.400 --> 00:06:22.700
So you can see it there.

149
00:06:23.220 --> 00:06:25.760
But here, I'm just going to vim cleanup

150
00:06:25.760 --> 00:06:28.680
.sh insert.

151
00:06:29.320 --> 00:06:31.380
And here you can see it stops all

152
00:06:31.380 --> 00:06:34.000
of the Docker containers, removes them all, and

153
00:06:34.000 --> 00:06:36.480
then removes all the volumes, etc, etc.

154
00:06:36.900 --> 00:06:40.380
So if I just save this, chmod plus

155
00:06:40.380 --> 00:06:42.640
x, you might not need this at all.

156
00:06:42.720 --> 00:06:44.500
But just in case, like I say, if

157
00:06:44.500 --> 00:06:46.140
Docker is filling up your whole file system,

158
00:06:46.140 --> 00:06:48.280
then you might want to remove the ones

159
00:06:48.280 --> 00:06:50.740
that you're not using anymore and rebuild the

160
00:06:50.740 --> 00:06:53.200
ones that you're using going forward.

161
00:06:53.320 --> 00:06:55.640
Just know, if you've been running other applications

162
00:06:55.640 --> 00:06:57.500
with Docker on your file system, this will

163
00:06:57.500 --> 00:06:58.340
remove all of them.

164
00:06:58.520 --> 00:07:02.320
So you'll still have, for example, the crappy

165
00:07:02.320 --> 00:07:03.320
application here.

166
00:07:03.480 --> 00:07:06.300
But when you sudo docker-compose up, it

167
00:07:06.300 --> 00:07:09.020
will rebuild the application, if that makes sense.

168
00:07:10.440 --> 00:07:12.560
So here, I'm just going to make sure

169
00:07:12.560 --> 00:07:14.800
that this is finished, which it is.

170
00:07:14.800 --> 00:07:22.180
And then sudo .slash cleanup.sh. And you

171
00:07:22.180 --> 00:07:24.080
can see that it's cleaned up everything.

172
00:07:24.300 --> 00:07:27.380
So the MongoDB Postgres data, this was all

173
00:07:27.380 --> 00:07:29.300
from the crappy application.

174
00:07:30.380 --> 00:07:31.440
And that's it for this section.

175
00:07:31.700 --> 00:07:33.300
So you should be all set up and

176
00:07:33.300 --> 00:07:34.000
ready to go.

177
00:07:34.220 --> 00:07:35.860
And I'll see you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
==================================================================================

# Section 3: Enumerating APIs

WEBVTT

1
00:00:00.670 --> 00:00:02.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, welcome to this section.

2
00:00:02.490 --> 00:00:04.310
So, the first thing we should do before

3
00:00:04.310 --> 00:00:06.530
we even consider the attacks we might try

4
00:00:06.530 --> 00:00:09.730
on a target application is to enumerate.

5
00:00:09.970 --> 00:00:12.470
Now, the objective here is to understand what

6
00:00:12.470 --> 00:00:14.550
application functionality exists.

7
00:00:14.750 --> 00:00:18.750
This includes intended functionality like registering, logging in,

8
00:00:19.010 --> 00:00:22.030
updating your profile, and potentially functionality that may

9
00:00:22.030 --> 00:00:24.610
have been overlooked, such as a file upload

10
00:00:24.610 --> 00:00:26.710
that is there but not ready yet for

11
00:00:26.710 --> 00:00:28.090
users to be accessing.

12
00:00:28.090 --> 00:00:30.230
We should also be on the lookout for

13
00:00:30.230 --> 00:00:32.790
things like special files that might have configuration

14
00:00:32.790 --> 00:00:36.950
information, or robots.txt and sitemaps that can

15
00:00:36.950 --> 00:00:39.030
provide further useful information.

16
00:00:39.670 --> 00:00:41.690
In this section, we'll do two things.

17
00:00:41.950 --> 00:00:44.610
The first is fuzzing to discover hidden content,

18
00:00:44.950 --> 00:00:47.530
and the second is manually reading some JavaScript

19
00:00:47.530 --> 00:00:51.530
files to harvest useful information from the application.

20
00:00:51.990 --> 00:00:52.770
Let's dive in.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.250 --> 00:00:03.750
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So fuzzing is simply sending different data in

2
00:00:03.750 --> 00:00:06.550
a number of requests and seeing what comes

3
00:00:06.550 --> 00:00:06.950
back.

4
00:00:07.410 --> 00:00:09.830
It can be really useful in discovering content

5
00:00:09.830 --> 00:00:13.070
or functionality, and in this video we're going

6
00:00:13.070 --> 00:00:15.770
to look at both Burp Suite's Intruder and

7
00:00:15.770 --> 00:00:18.870
also WFuzz, but there are actually many different

8
00:00:18.870 --> 00:00:19.970
tools you can use.

9
00:00:20.130 --> 00:00:21.830
I recommend you try out different ones to

10
00:00:21.830 --> 00:00:24.330
see what suits your workflow or methodology.

11
00:00:24.330 --> 00:00:26.710
In this demo I'm going to be using

12
00:00:26.710 --> 00:00:29.570
an endpoint from Bookstore, which you can see

13
00:00:29.570 --> 00:00:31.950
on screen now, and this is a free

14
00:00:31.950 --> 00:00:35.110
room available on TryHackMe, so by all means

15
00:00:35.110 --> 00:00:37.970
go ahead, sign up an account to TryHackMe

16
00:00:37.970 --> 00:00:40.150
and come to Bookstore if you want to

17
00:00:40.150 --> 00:00:40.890
follow along.

18
00:00:41.210 --> 00:00:45.350
So here we have some API documentation and

19
00:00:45.350 --> 00:00:47.930
we can see that we have api slash

20
00:00:47.930 --> 00:00:51.890
v2 slash resources and slash books, and the

21
00:00:51.890 --> 00:00:54.070
author here in this case, or in this

22
00:00:54.070 --> 00:00:57.210
example, is JK Rowling, and we can also

23
00:00:57.210 --> 00:01:00.290
filter by things like the publish date, and

24
00:01:00.290 --> 00:01:02.150
what I've done is I've set this up

25
00:01:02.150 --> 00:01:05.210
in repeater so you can see that I

26
00:01:05.210 --> 00:01:08.690
am sending a request to api v2 resources

27
00:01:08.690 --> 00:01:12.950
books and the parameter published and the value

28
00:01:12.950 --> 00:01:15.990
1993, and we do indeed get some data

29
00:01:15.990 --> 00:01:16.510
back.

30
00:01:17.210 --> 00:01:19.130
Now there are a few points here that

31
00:01:19.130 --> 00:01:21.370
I want to think about when I start

32
00:01:21.370 --> 00:01:24.930
fuzzing, so the first one is v2.

33
00:01:25.330 --> 00:01:27.210
So when I see this I always think,

34
00:01:27.610 --> 00:01:28.550
is there a v1?

35
00:01:28.650 --> 00:01:29.710
Is there a v0?

36
00:01:29.970 --> 00:01:31.350
Is there a beta?

37
00:01:31.730 --> 00:01:32.930
Is there a v3?

38
00:01:33.050 --> 00:01:34.010
Is there a v4?

39
00:01:34.210 --> 00:01:36.970
So this is probably our first point of

40
00:01:36.970 --> 00:01:39.210
call for fuzzing the endpoint.

41
00:01:40.630 --> 00:01:43.530
After that I want to look at the

42
00:01:43.530 --> 00:01:45.350
endpoint here, so we're in resources.

43
00:01:45.630 --> 00:01:48.410
There might be other endpoints available as well

44
00:01:48.410 --> 00:01:52.150
aside from books, for example authors, and then

45
00:01:52.150 --> 00:01:54.330
after that we look at the parameters.

46
00:01:54.630 --> 00:01:56.750
So what parameters will this endpoint take?

47
00:01:56.870 --> 00:01:57.750
Will it take published?

48
00:01:57.950 --> 00:01:59.570
Will it take unpublished?

49
00:01:59.690 --> 00:02:01.070
Will it take other things?

50
00:02:02.430 --> 00:02:05.290
And then finally after this we can look

51
00:02:05.290 --> 00:02:08.690
at the parameter values, and here we're probably

52
00:02:08.690 --> 00:02:11.790
looking for things like injection techniques or special

53
00:02:11.790 --> 00:02:14.050
characters to see whether our input is handled

54
00:02:14.050 --> 00:02:15.410
in an insecure way.

55
00:02:16.090 --> 00:02:18.810
So let's make a start with this, and

56
00:02:18.810 --> 00:02:20.550
to begin with all I'm going to do

57
00:02:20.550 --> 00:02:22.550
is change this.

58
00:02:22.710 --> 00:02:24.350
I'm going to do this manually because our

59
00:02:24.350 --> 00:02:27.950
data set is quite small, and we send

60
00:02:27.950 --> 00:02:31.550
v0 and we get 404 not found, and

61
00:02:31.550 --> 00:02:34.950
we get v1 and we get 200 OK,

62
00:02:34.950 --> 00:02:38.610
which is interesting because we also got 200

63
00:02:38.610 --> 00:02:39.730
OK on v2.

64
00:02:39.910 --> 00:02:41.450
So a couple of things that we want

65
00:02:41.450 --> 00:02:43.470
to look at here are the status code,

66
00:02:43.790 --> 00:02:46.190
so 200, and we want to see the

67
00:02:46.190 --> 00:02:49.390
content length as well, so this is 408.

68
00:02:49.770 --> 00:02:51.930
So if I then send the request to

69
00:02:51.930 --> 00:02:55.990
v2, we can see that we get the

70
00:02:55.990 --> 00:02:56.970
same content length.

71
00:02:56.990 --> 00:02:59.330
So I'm pretty sure that this data is

72
00:02:59.330 --> 00:03:01.950
the same as the previous one, and in

73
00:03:01.950 --> 00:03:03.250
this case it's quite easy to check.

74
00:03:03.250 --> 00:03:04.630
We can just go left and right and

75
00:03:04.630 --> 00:03:07.090
the only thing that changes is the time

76
00:03:07.090 --> 00:03:10.350
date stamp, or the time stamp here, but

77
00:03:10.350 --> 00:03:12.630
if we had a page with a content

78
00:03:12.630 --> 00:03:16.090
length of like 10, 20,000, then it

79
00:03:16.090 --> 00:03:18.070
would be a little bit harder to check.

80
00:03:18.490 --> 00:03:20.310
So next up we want to take a

81
00:03:20.310 --> 00:03:22.490
look at slash books, so I'm going to

82
00:03:22.490 --> 00:03:24.710
press ctrl i to send this to the

83
00:03:24.710 --> 00:03:27.550
intruder, and if you don't have burp suite

84
00:03:27.550 --> 00:03:29.230
professional, don't worry, we're going to do the

85
00:03:29.230 --> 00:03:31.630
exact same thing with wfuzz in just a

86
00:03:31.630 --> 00:03:31.770
minute.

87
00:03:32.030 --> 00:03:34.490
So we'll do burp suite first and then

88
00:03:34.490 --> 00:03:39.790
wfuzz afterwards, and we come to intruder, we

89
00:03:39.790 --> 00:03:43.750
clear this, we add our payload point here,

90
00:03:44.710 --> 00:03:47.670
we come to payloads, and then we load,

91
00:03:48.190 --> 00:03:50.750
and let's just do a small word list

92
00:03:50.750 --> 00:03:54.430
for now, and we'll click start attack.

93
00:03:55.210 --> 00:03:57.210
You can see that the content length of

94
00:03:57.210 --> 00:04:00.690
the original request is 620, and the other

95
00:04:00.690 --> 00:04:02.910
ones look like they're 292.

96
00:04:04.170 --> 00:04:05.410
So I'll give this a minute to run,

97
00:04:14.040 --> 00:04:15.200
and now it's finished.

98
00:04:15.300 --> 00:04:17.079
We can take a look at the results,

99
00:04:17.320 --> 00:04:19.579
and it doesn't look like we got anything

100
00:04:19.579 --> 00:04:19.940
else.

101
00:04:19.940 --> 00:04:22.420
We only have one request with a different

102
00:04:22.420 --> 00:04:25.900
length, and only one request with a status

103
00:04:25.900 --> 00:04:26.520
200.

104
00:04:26.680 --> 00:04:28.780
All of the rest were 404s.

105
00:04:29.100 --> 00:04:32.140
Unsuccessful here, but still useful to check.

106
00:04:32.820 --> 00:04:34.960
So I'm just going to discard this, and

107
00:04:34.960 --> 00:04:37.900
then come back, and then let's clear this

108
00:04:37.900 --> 00:04:43.180
selection, and let's change this published to something

109
00:04:43.180 --> 00:04:47.930
else, and let's attack the published field.

110
00:04:52.890 --> 00:04:55.330
Probably we can keep the same word list.

111
00:05:03.130 --> 00:05:06.070
Looks like it didn't find anything once again,

112
00:05:06.110 --> 00:05:08.450
so it looks like there's nothing too exciting

113
00:05:08.450 --> 00:05:10.230
to find against this endpoint.

114
00:05:10.930 --> 00:05:12.350
But what we're going to do is we're

115
00:05:12.350 --> 00:05:14.070
going to try the same thing against the

116
00:05:14.070 --> 00:05:17.450
v1 endpoint, and I'm just going to keep

117
00:05:17.450 --> 00:05:19.510
the attack the same, and just click start,

118
00:05:19.970 --> 00:05:21.970
and see what it comes back with.

119
00:05:30.070 --> 00:05:33.310
All right, so let's take a look, and

120
00:05:33.310 --> 00:05:35.910
we do actually get something that gave us

121
00:05:35.910 --> 00:05:39.190
a 500 response instead of 404, or a

122
00:05:39.190 --> 00:05:40.890
totally different content length.

123
00:05:41.330 --> 00:05:44.870
This was the parameter show, and we can

124
00:05:44.870 --> 00:05:46.250
come in here, take a look at the

125
00:05:46.250 --> 00:05:49.570
response, and we get an internal server error.

126
00:05:49.830 --> 00:05:52.690
So I suspect, given that we get this

127
00:05:52.690 --> 00:05:56.630
name error, name file name is not defined,

128
00:05:59.360 --> 00:06:01.780
what I think is happening here is that

129
00:06:01.780 --> 00:06:04.900
the parameter is then throwing the error.

130
00:06:05.100 --> 00:06:07.880
So we're passing this, sorry, the value is

131
00:06:07.880 --> 00:06:08.640
throwing the error.

132
00:06:08.820 --> 00:06:11.660
So we're passing this value into the parameter

133
00:06:11.660 --> 00:06:13.900
show, even though it says published here, and

134
00:06:13.900 --> 00:06:15.480
that's causing an issue.

135
00:06:15.740 --> 00:06:19.820
So let's discard this, come back to our

136
00:06:19.820 --> 00:06:23.380
repeater, change this to one, change this to

137
00:06:23.380 --> 00:06:27.260
show, click send, and we get 500.

138
00:06:28.400 --> 00:06:30.060
And let's see what happens if we give

139
00:06:30.060 --> 00:06:31.080
it a blank parameter.

140
00:06:31.700 --> 00:06:35.320
We get not found, and what we can

141
00:06:35.320 --> 00:06:43.760
now do is clear this, do show, hit

142
00:06:43.760 --> 00:06:48.800
the parameter value, and then start the attack

143
00:06:48.800 --> 00:06:49.200
again.

144
00:06:50.840 --> 00:06:52.780
And at this point we probably want to

145
00:06:52.780 --> 00:06:54.240
think about different word lists.

146
00:06:54.460 --> 00:06:56.820
So we're doing a kind of a generic

147
00:06:56.820 --> 00:06:58.580
word list at the moment that's good at

148
00:06:58.580 --> 00:07:01.380
finding directories, but we probably want to consider

149
00:07:01.380 --> 00:07:03.660
something that's a little bit more targeted based

150
00:07:03.660 --> 00:07:05.680
on the error message that we got.

151
00:07:06.300 --> 00:07:08.120
And since it said invalid file name, or

152
00:07:08.120 --> 00:07:10.200
file not found, or something like this if

153
00:07:10.200 --> 00:07:12.340
I recall, we might want to consider a

154
00:07:12.340 --> 00:07:15.640
list of common linux files, because the target

155
00:07:15.640 --> 00:07:17.360
system is a linux system.

156
00:07:31.160 --> 00:07:33.060
All right, so I'm actually going to close

157
00:07:33.060 --> 00:07:35.580
this because it seems like the application is

158
00:07:35.580 --> 00:07:38.260
struggling a little bit under our attack, which

159
00:07:38.260 --> 00:07:41.200
can happen when you're fuzzing, especially for vulnerable

160
00:07:41.200 --> 00:07:42.080
endpoints.

161
00:07:42.840 --> 00:07:44.540
And I'm just going to come back here,

162
00:07:45.040 --> 00:07:46.240
just do a quick refresh.

163
00:07:53.380 --> 00:07:55.720
So it actually seems like we've found a

164
00:07:55.720 --> 00:08:00.180
vulnerable endpoint, but we've unfortunately crashed the application,

165
00:08:00.340 --> 00:08:02.760
which is a great lesson to learn, because

166
00:08:02.760 --> 00:08:05.160
this can happen when we're fuzzing.

167
00:08:05.260 --> 00:08:06.860
Fuzzing can be quite destructive.

168
00:08:07.220 --> 00:08:08.820
So what I'm going to do is I'm

169
00:08:08.820 --> 00:08:12.020
going to come back here, I'm just going

170
00:08:12.020 --> 00:08:17.190
to terminate the machine, and then I'm just

171
00:08:17.190 --> 00:08:24.940
going to start it up again, and I'll

172
00:08:24.940 --> 00:08:26.400
see you back here in a minute so

173
00:08:26.400 --> 00:08:28.200
that we can review what's happened.

174
00:08:30.510 --> 00:08:34.950
All right, so I've just restarted the application,

175
00:08:35.909 --> 00:08:38.030
brought it back up, loaded in a new

176
00:08:38.030 --> 00:08:38.450
list.

177
00:08:38.710 --> 00:08:42.350
So I'm using common now in usershare wordlists

178
00:08:42.350 --> 00:08:45.850
-deb instead of this small list, and we're

179
00:08:45.850 --> 00:08:47.610
going to see how this goes.

180
00:08:48.290 --> 00:08:51.430
So I just click start attack, and instantly

181
00:08:51.430 --> 00:08:54.450
it actually gets some with different lengths.

182
00:08:54.750 --> 00:08:56.850
So I'm actually going to pause this quickly

183
00:08:56.850 --> 00:08:58.810
to take a look and see what's happening.

184
00:08:59.050 --> 00:09:03.270
So our initial request is 500, so we

185
00:09:03.270 --> 00:09:05.490
get a response back that says internal server

186
00:09:05.490 --> 00:09:08.330
error, and the error file name is not

187
00:09:08.330 --> 00:09:10.510
defined, which is the error that we got

188
00:09:10.510 --> 00:09:10.970
before.

189
00:09:11.950 --> 00:09:15.750
And then we have a request that has

190
00:09:15.750 --> 00:09:17.890
a blank payload, so this gives us a

191
00:09:17.890 --> 00:09:19.010
404 not found.

192
00:09:19.570 --> 00:09:22.310
And then interestingly, we get a 200 response

193
00:09:22.310 --> 00:09:23.510
for bash history.

194
00:09:23.990 --> 00:09:26.810
So we come back and we actually see

195
00:09:26.810 --> 00:09:28.930
that we have some data here.

196
00:09:28.970 --> 00:09:31.030
So it seems like it's reading from the

197
00:09:31.030 --> 00:09:32.490
.bash history file.

198
00:09:32.910 --> 00:09:35.630
So we have indeed found a vulnerable endpoint

199
00:09:35.630 --> 00:09:40.430
and managed to fuzz for local file inclusion

200
00:09:40.430 --> 00:09:41.150
vulnerability.

201
00:09:41.810 --> 00:09:44.550
So super interesting, and hopefully this gives you

202
00:09:44.550 --> 00:09:48.290
a good insight into how useful, but also

203
00:09:48.290 --> 00:09:51.730
sometimes how dangerous, fuzzing can actually be.

204
00:09:54.230 --> 00:09:58.030
So before we do this in wfuzz, let's

205
00:09:58.030 --> 00:10:00.570
just take another quick look at the positions.

206
00:10:00.930 --> 00:10:03.830
So first we looked at slash v1, while

207
00:10:03.830 --> 00:10:06.850
this was slash v2 before, and we guessed

208
00:10:06.850 --> 00:10:08.870
that there might be other versions of the

209
00:10:08.870 --> 00:10:10.270
API endpoint available.

210
00:10:10.730 --> 00:10:14.090
And then we looked at the books endpoints,

211
00:10:14.210 --> 00:10:16.910
we looked for other endpoints that were not

212
00:10:16.910 --> 00:10:18.370
listed on the documentation.

213
00:10:18.650 --> 00:10:22.150
So if you recall, we only had this

214
00:10:22.150 --> 00:10:24.590
documentation, which only gave us a few different

215
00:10:24.590 --> 00:10:25.190
endpoints.

216
00:10:26.570 --> 00:10:29.110
And then we looked at parameter names, which

217
00:10:29.110 --> 00:10:31.450
is where we found the show parameter, which

218
00:10:31.450 --> 00:10:33.490
wasn't listed in our documentation.

219
00:10:34.270 --> 00:10:37.790
And then we fuzzed the parameter value to

220
00:10:37.790 --> 00:10:41.170
discover that this was vulnerable to file inclusion.

221
00:10:41.650 --> 00:10:45.410
All right, so let's come over to our

222
00:10:45.410 --> 00:10:49.050
terminal, and let's try this with wfuzz.

223
00:10:49.170 --> 00:10:51.950
So all I'm going to do is type

224
00:10:51.950 --> 00:10:55.550
wfuzz, and we're going to add some color,

225
00:10:56.050 --> 00:10:57.730
and then "-z", for the type.

226
00:10:58.610 --> 00:11:00.850
And the file we're going to use is,

227
00:11:01.090 --> 00:11:02.590
I like to add a space here, so

228
00:11:02.590 --> 00:11:04.670
I can use autocomplete with the tab, and

229
00:11:04.670 --> 00:11:06.170
then I'll remove the space afterwards.

230
00:11:06.690 --> 00:11:10.750
So user, share, wordlists, derb.

231
00:11:11.430 --> 00:11:17.680
And I think we used the common, and

232
00:11:17.680 --> 00:11:19.820
then I'm just gonna come back and remove

233
00:11:19.820 --> 00:11:20.220
that.

234
00:11:20.890 --> 00:11:24.060
And then what we want to do is

235
00:11:24.060 --> 00:11:25.420
grab the target.

236
00:11:25.920 --> 00:11:29.480
So in this case, we can take the

237
00:11:34.580 --> 00:11:39.740
IP address, http//, and then take the endpoint

238
00:11:39.740 --> 00:11:50.010
here, and

239
00:11:50.010 --> 00:11:50.990
we type fuzz.

240
00:11:51.130 --> 00:11:52.810
And I think we need this in quotes

241
00:11:52.810 --> 00:11:53.890
as well.

242
00:11:55.900 --> 00:11:57.700
So I'm just going to run this to

243
00:11:57.700 --> 00:11:59.840
begin with, without any filtering.

244
00:12:02.050 --> 00:12:03.930
And you'll notice that we get a lot

245
00:12:03.930 --> 00:12:04.690
of data back.

246
00:12:04.910 --> 00:12:06.790
So what we actually want to do is

247
00:12:06.790 --> 00:12:09.450
we want to filter out the 500s.

248
00:12:09.770 --> 00:12:14.350
So here, we're only looking for the values

249
00:12:14.350 --> 00:12:17.910
of the HTTP response codes of 200.

250
00:12:18.290 --> 00:12:21.890
So I can just do "-sc 200".

251
00:12:21.890 --> 00:12:24.350
That didn't work as expected.

252
00:12:24.590 --> 00:12:26.170
Maybe it's hc?

253
00:12:26.370 --> 00:12:28.510
I can't remember off the top of my

254
00:12:28.510 --> 00:12:28.810
head.

255
00:12:33.870 --> 00:12:37.190
We might have to add this back here.

256
00:12:41.120 --> 00:12:42.680
Ah, okay, so the order matters.

257
00:12:43.080 --> 00:12:44.740
So you need to add this, I think,

258
00:12:44.900 --> 00:12:46.480
before our target.

259
00:12:46.640 --> 00:12:48.120
So the target needs to be the final

260
00:12:48.120 --> 00:12:50.560
thing in our list of inputs.

261
00:12:51.080 --> 00:12:52.940
And as you can see, this time around,

262
00:12:53.080 --> 00:12:55.800
we just get our three responses that we

263
00:12:55.800 --> 00:12:59.900
want, instead of lots of 500 errors.

264
00:13:03.360 --> 00:13:07.560
And we found "-rc profile", and "-history".

265
00:13:07.560 --> 00:13:09.280
And I suspect this is also a little

266
00:13:09.280 --> 00:13:11.860
bit faster than Verpsuite as well.

267
00:13:12.000 --> 00:13:13.520
So this can be a good option for

268
00:13:13.520 --> 00:13:13.740
you.

269
00:13:14.600 --> 00:13:16.380
Gives you a little bit more control out

270
00:13:16.380 --> 00:13:19.860
of what's coming out of the tool, rather

271
00:13:19.860 --> 00:13:22.780
than being bogged down with a user interface.

272
00:13:23.260 --> 00:13:25.160
And it's really up to you which tools

273
00:13:25.160 --> 00:13:26.760
you want to use going forward.

274
00:13:26.920 --> 00:13:28.600
And that's it for this video.

275
00:13:28.820 --> 00:13:30.800
So I hope this was a nice quick

276
00:13:30.800 --> 00:13:33.800
introduction to fuzzing, something that is really, really

277
00:13:33.800 --> 00:13:36.520
important to learn and understand how to do.

278
00:13:36.820 --> 00:13:38.720
But really, you only get better at it

279
00:13:38.720 --> 00:13:39.560
by doing it.

280
00:13:39.780 --> 00:13:41.540
And throughout the course, you'll have plenty of

281
00:13:41.540 --> 00:13:45.280
chances to try fuzzing against different applications that

282
00:13:45.280 --> 00:13:46.320
you'll have access to.

283
00:13:46.740 --> 00:13:47.840
I'll see you in the next video!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.150 --> 00:00:02.550
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, finally, before we dive into the

2
00:00:02.550 --> 00:00:06.170
next section where we'll be attacking authorization, we're

3
00:00:06.170 --> 00:00:08.290
going to just look a little bit at

4
00:00:08.290 --> 00:00:09.770
manual enumeration.

5
00:00:10.190 --> 00:00:13.450
So whenever I start attacking a new application,

6
00:00:13.650 --> 00:00:16.190
I switch on WebSuite and I try to

7
00:00:16.190 --> 00:00:18.150
test all of the functionality that I can

8
00:00:18.150 --> 00:00:20.530
find, and this helps me achieve two main

9
00:00:20.530 --> 00:00:20.990
things.

10
00:00:21.450 --> 00:00:24.110
Firstly, I can review the traffic afterwards, so

11
00:00:24.110 --> 00:00:26.950
I can understand how the application is working

12
00:00:26.950 --> 00:00:27.730
under the hood.

13
00:00:27.870 --> 00:00:30.830
And secondly, I can start to understand how

14
00:00:30.830 --> 00:00:33.330
the application is meant to behave, which helps

15
00:00:33.330 --> 00:00:36.430
when we're trying to find peculiar behavior that

16
00:00:36.430 --> 00:00:38.630
might indicate a security vulnerability.

17
00:00:39.050 --> 00:00:40.790
Here we're going to take a quick look

18
00:00:40.790 --> 00:00:42.890
at some of the JS files in the

19
00:00:42.890 --> 00:00:44.090
crappy application.

20
00:00:44.450 --> 00:00:46.670
So I'm just going to log in quickly.

21
00:00:46.890 --> 00:00:49.490
I already have a account set up and

22
00:00:49.490 --> 00:00:52.070
I'm going to bring up the developer tools

23
00:00:52.070 --> 00:00:53.770
and I'm just going to move myself out

24
00:00:53.770 --> 00:00:57.720
of the way so that you can easily

25
00:00:57.720 --> 00:00:58.100
see.

26
00:00:58.240 --> 00:00:59.520
I'll zoom in a little bit.

27
00:01:01.460 --> 00:01:03.920
And we might want to go through, test

28
00:01:03.920 --> 00:01:06.000
all of these endpoints, see what comes up

29
00:01:06.000 --> 00:01:06.500
in WebSuite.

30
00:01:06.600 --> 00:01:07.940
In fact, I'll just show you quickly.

31
00:01:08.180 --> 00:01:10.840
So we'll click through, click on some posts,

32
00:01:11.480 --> 00:01:12.940
we'd add some comments.

33
00:01:13.680 --> 00:01:15.340
I'm just going to do this very quickly.

34
00:01:16.900 --> 00:01:18.420
But you take a little bit of time

35
00:01:18.420 --> 00:01:19.180
to come through.

36
00:01:20.400 --> 00:01:21.480
Change video name.

37
00:01:25.850 --> 00:01:28.130
And then once you've understood all of the

38
00:01:28.130 --> 00:01:30.930
functionality in the application, you can come back

39
00:01:30.930 --> 00:01:36.110
to WebSuite and you can see everything is

40
00:01:36.110 --> 00:01:37.230
mapped in here.

41
00:01:37.270 --> 00:01:39.310
So we can start looking at what are

42
00:01:39.310 --> 00:01:42.230
these API endpoints and what kind of data

43
00:01:42.230 --> 00:01:43.330
do they return.

44
00:01:43.870 --> 00:01:45.650
But really what I wanted to show you

45
00:01:45.650 --> 00:01:48.490
and the main point of this video is

46
00:01:48.490 --> 00:01:50.710
coming to the developer tools.

47
00:01:51.210 --> 00:01:53.590
And I'm going to zoom in a little

48
00:01:53.590 --> 00:01:55.790
bit, come over to the debugger tab.

49
00:01:56.210 --> 00:01:57.830
And what I want to do is have

50
00:01:57.830 --> 00:01:59.050
a look through some of the files.

51
00:01:59.610 --> 00:02:01.870
And I'm not really trying to understand what's

52
00:02:01.870 --> 00:02:02.390
happening here.

53
00:02:02.410 --> 00:02:04.010
I'm not going to sit and do code

54
00:02:04.010 --> 00:02:07.669
review and dissect the code or dissect the

55
00:02:07.669 --> 00:02:09.449
JavaScript that's running in the front end.

56
00:02:09.550 --> 00:02:12.090
What I'm just looking for is information.

57
00:02:12.570 --> 00:02:15.610
So we can just drop down and we

58
00:02:15.610 --> 00:02:18.250
can see that there's a bunch of JavaScript

59
00:02:18.250 --> 00:02:19.130
files here.

60
00:02:19.870 --> 00:02:22.670
Some utilities, location utils.

61
00:02:23.050 --> 00:02:25.730
This might have had something like a bunch

62
00:02:25.730 --> 00:02:29.770
of locations hard-coded in, but unfortunately not.

63
00:02:32.320 --> 00:02:33.740
We'll have a look in source.

64
00:02:40.100 --> 00:02:42.240
Just skim through some of these.

65
00:02:44.880 --> 00:02:47.080
Doesn't look like exactly what we're after.

66
00:02:49.340 --> 00:02:53.320
Let's have a look in static.js and

67
00:02:54.890 --> 00:03:01.170
this config.js. So we get some top

68
00:03:01.170 --> 00:03:02.170
level endpoints.

69
00:03:02.430 --> 00:03:04.890
So identity workshop community.

70
00:03:05.270 --> 00:03:09.890
So Java microservices, Python microservices and Go microservices.

71
00:03:10.310 --> 00:03:12.950
This is actually really interesting and useful to

72
00:03:12.950 --> 00:03:13.150
know.

73
00:03:14.370 --> 00:03:17.270
So depending on the endpoint that we're attacking,

74
00:03:17.570 --> 00:03:20.510
we will basically need different payloads or potentially

75
00:03:20.510 --> 00:03:25.090
different exploits based on the underlying technology.

76
00:03:27.670 --> 00:03:29.310
Have a quick look in the index.

77
00:03:33.680 --> 00:03:34.900
Have a quick look in here.

78
00:03:34.900 --> 00:03:38.060
And this is basically unreadable.

79
00:03:38.200 --> 00:03:39.780
So if you have a file like this,

80
00:03:40.540 --> 00:03:41.660
what we can do is we can just

81
00:03:41.660 --> 00:03:46.380
control a copy and then come to Google

82
00:03:46.380 --> 00:03:52.990
and just search for JS formatter.

83
00:03:54.190 --> 00:03:56.050
And you can choose any of these online

84
00:03:56.050 --> 00:03:56.990
JavaScript beautifier.

85
00:03:57.170 --> 00:03:59.290
Obviously don't do this if there's sensitive information

86
00:03:59.290 --> 00:04:02.370
or something like that in your code or

87
00:04:02.370 --> 00:04:04.430
if this is like closed source application, don't

88
00:04:04.430 --> 00:04:06.110
go posting it to websites online.

89
00:04:06.630 --> 00:04:08.890
But let's just go to the beautifier code

90
00:04:08.890 --> 00:04:10.170
and we can have a look through.

91
00:04:22.350 --> 00:04:24.170
And here this looks quite interesting.

92
00:04:24.570 --> 00:04:27.490
We actually get a bunch of endpoints.

93
00:04:28.010 --> 00:04:30.330
So this is really useful information.

94
00:04:30.670 --> 00:04:33.630
So we could actually compare this to the

95
00:04:33.630 --> 00:04:36.250
postman file that we got so that we

96
00:04:36.250 --> 00:04:38.750
know whether there are any missing endpoints that

97
00:04:38.750 --> 00:04:40.150
weren't included for testing.

98
00:04:40.350 --> 00:04:42.110
And this might save us a little bit

99
00:04:42.110 --> 00:04:43.750
of time fuzzing as well.

100
00:04:43.930 --> 00:04:46.310
So this is a really great find and

101
00:04:46.310 --> 00:04:49.370
usually you can find information like this in

102
00:04:49.370 --> 00:04:51.410
the front end JavaScript files.

103
00:04:51.990 --> 00:04:53.710
So that was a little bit of a

104
00:04:53.710 --> 00:04:56.170
whirlwind tour and I hope you picked up

105
00:04:56.170 --> 00:04:59.150
some useful tips on how to approach enumerating

106
00:04:59.150 --> 00:05:00.930
API based applications.

107
00:05:01.750 --> 00:05:04.410
Your methodology doesn't need to be complicated, but

108
00:05:04.410 --> 00:05:06.010
it really does need to be thorough.

109
00:05:06.770 --> 00:05:08.310
And I think that a lot of people

110
00:05:08.310 --> 00:05:10.750
make mistakes trying to do complex things when

111
00:05:10.750 --> 00:05:13.370
actually the simple approach is the best.

112
00:05:13.590 --> 00:05:15.830
It's just that the simple approach needs to

113
00:05:15.830 --> 00:05:16.730
be done properly.

114
00:05:17.010 --> 00:05:19.230
Now let's start attacking some applications.

115
00:05:19.630 --> 00:05:20.970
I'll see you in the next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Attacking Authorization

WEBVTT

1
00:00:00.200 --> 00:00:02.820
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So before we dive into the vulnerabilities, we

2
00:00:02.820 --> 00:00:05.640
first need to understand what authorization is.

3
00:00:06.120 --> 00:00:08.720
Now, often people get mixed up between authorization

4
00:00:08.720 --> 00:00:10.060
and authentication.

5
00:00:11.180 --> 00:00:13.960
So authentication is who you are, it's your

6
00:00:13.960 --> 00:00:17.320
identity, and authorization is what you're allowed to

7
00:00:17.320 --> 00:00:17.540
do.

8
00:00:18.060 --> 00:00:19.180
I like to think of it as a

9
00:00:19.180 --> 00:00:19.540
hotel.

10
00:00:19.800 --> 00:00:22.120
When you check in, you show your passport

11
00:00:22.120 --> 00:00:24.680
or driving license to prove that the booking

12
00:00:24.680 --> 00:00:26.520
is yours, to prove you are who you

13
00:00:26.520 --> 00:00:27.020
say you are.

14
00:00:28.080 --> 00:00:30.460
Once you've checked in, you get given a

15
00:00:30.460 --> 00:00:33.040
room key, and this key gives you access

16
00:00:33.040 --> 00:00:35.460
to your room, maybe the lounge or bar,

17
00:00:35.720 --> 00:00:37.420
or maybe even the executive suite.

18
00:00:37.980 --> 00:00:39.580
This is your authorization.

19
00:00:40.680 --> 00:00:42.820
Now, in the OWASP Top 10, there are

20
00:00:42.820 --> 00:00:44.880
two vulnerabilities related to authorization.

21
00:00:45.480 --> 00:00:47.340
So it's really, really important that we understand

22
00:00:47.340 --> 00:00:49.120
how they work and that we can find

23
00:00:49.120 --> 00:00:49.940
and exploit them.

24
00:00:50.240 --> 00:00:52.640
It takes the number one spot with broken

25
00:00:52.640 --> 00:00:56.120
object level authorization, also known as BOLA, and

26
00:00:56.120 --> 00:00:58.680
it takes the fifth spot, which is broken

27
00:00:58.680 --> 00:01:02.260
function level authorization, also known as BAFLA.

28
00:01:03.019 --> 00:01:05.100
Now, these might sound a little bit confusing,

29
00:01:05.460 --> 00:01:07.040
so let's talk through an example.

30
00:01:07.640 --> 00:01:10.900
If we have a webshop, and let's say

31
00:01:10.900 --> 00:01:13.040
you go to your account page, and it

32
00:01:13.040 --> 00:01:17.920
says, hey, slash webshop and slash your user

33
00:01:17.920 --> 00:01:18.240
ID.

34
00:01:18.980 --> 00:01:21.500
If I change this ID to the ID

35
00:01:21.500 --> 00:01:23.860
of another user, and I can access their

36
00:01:23.860 --> 00:01:28.160
information, this is BOLA, broken objects level authorization.

37
00:01:29.220 --> 00:01:31.860
Within the same webshop, if I can carry

38
00:01:31.860 --> 00:01:35.600
out functions such as ordering on another user's

39
00:01:35.600 --> 00:01:39.760
behalf or accessing administrative functionality, this is BAFLA,

40
00:01:40.240 --> 00:01:41.920
broken function level authorization.

41
00:01:42.780 --> 00:01:44.700
So try to think of BOLA as access

42
00:01:44.700 --> 00:01:48.220
to objects referenced by their ID, such as

43
00:01:48.220 --> 00:01:51.140
a user ID or a GUID or something

44
00:01:51.140 --> 00:01:53.300
like this, and try to think of BAFLA

45
00:01:53.300 --> 00:01:56.060
as access to functionality that you shouldn't have

46
00:01:56.060 --> 00:01:56.740
access to.

47
00:01:57.720 --> 00:01:59.720
In the next video, we're gonna walk through

48
00:01:59.720 --> 00:02:01.400
an example, and then I'm gonna give you

49
00:02:01.400 --> 00:02:02.720
some challenges to work on.

50
00:02:03.260 --> 00:02:04.100
So I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.080 --> 00:00:01.620
(Transcribed by TurboScribe. Go Unlimited to remove this message.) In this video, we're going to walk through

2
00:00:01.620 --> 00:00:03.400
Ebola vulnerability together.

3
00:00:03.940 --> 00:00:06.180
Now, this one is slightly less obvious than

4
00:00:06.180 --> 00:00:08.520
finding an object ID and just changing it,

5
00:00:08.620 --> 00:00:10.540
so going from 1 to 2 to 3

6
00:00:10.540 --> 00:00:12.100
to 4, and seeing what we find.

7
00:00:12.540 --> 00:00:15.160
But it actually highlights the importance of keeping

8
00:00:15.160 --> 00:00:17.140
track of the information we find during a

9
00:00:17.140 --> 00:00:20.260
pen test, and keeping track of what endpoints

10
00:00:20.260 --> 00:00:23.420
return what information, and how we can use

11
00:00:23.420 --> 00:00:24.480
that in our attacks.

12
00:00:25.400 --> 00:00:27.160
So, feel free to follow along step by

13
00:00:27.160 --> 00:00:29.320
step, or you can watch the video all

14
00:00:29.320 --> 00:00:30.920
the way through and try and replicate the

15
00:00:30.920 --> 00:00:31.280
attack.

16
00:00:31.640 --> 00:00:34.360
Afterwards, I'll give you a Ebola challenge to

17
00:00:34.360 --> 00:00:36.480
do yourselves, so you can get some real

18
00:00:36.480 --> 00:00:37.460
hands-on experience.

19
00:00:37.980 --> 00:00:39.220
Let's dive straight in.

20
00:00:42.120 --> 00:00:44.980
So here, I have BupSuite open, and I

21
00:00:44.980 --> 00:00:48.440
have the Crapi API open, and I also

22
00:00:48.440 --> 00:00:51.620
have Mailhug open, running on AT25.

23
00:00:52.260 --> 00:00:54.400
So, I'm just going to sign up a

24
00:00:54.400 --> 00:00:56.040
new account, so I'm just going to call

25
00:00:56.040 --> 00:00:58.780
this Alex, and I already have an account,

26
00:01:00.140 --> 00:01:02.160
a.tcmsec.com, so I'm just going to

27
00:01:02.160 --> 00:01:05.140
put b.tcmsec.com, and then I'm just

28
00:01:05.140 --> 00:01:09.340
going to give it a random string for

29
00:01:09.340 --> 00:01:12.860
a random number for the phone number, password

30
00:01:12.860 --> 00:01:16.900
one exclamation mark, password one exclamation mark.

31
00:01:17.060 --> 00:01:21.480
So, very easy credentials, registered, and then b

32
00:01:21.480 --> 00:01:27.300
.tcmsec.com, password one, and then we click

33
00:01:27.300 --> 00:01:27.960
log in.

34
00:01:28.260 --> 00:01:30.620
So, we have no vehicles found.

35
00:01:31.660 --> 00:01:34.560
So, if we come to Mailhug and check

36
00:01:34.560 --> 00:01:37.500
the mail, we have the VIN and the

37
00:01:37.500 --> 00:01:38.960
PIN code, so I'm just going to copy

38
00:01:38.960 --> 00:01:44.280
and paste this, add vehicle, paste, copy and

39
00:01:44.280 --> 00:01:49.140
paste the PIN code in here, and verify

40
00:01:49.140 --> 00:01:51.120
vehicle details, and we get a success.

41
00:01:51.360 --> 00:01:51.620
Awesome.

42
00:01:52.320 --> 00:01:53.680
And we get a Lamborghini.

43
00:01:54.080 --> 00:01:56.100
Yeah, that's exactly what I wanted.

44
00:01:56.340 --> 00:01:57.260
That's my kind of car.

45
00:01:58.700 --> 00:02:01.620
And the vulnerability here is down in the

46
00:02:01.620 --> 00:02:02.740
refresh location.

47
00:02:03.000 --> 00:02:04.340
So, what I'm going to do is we're

48
00:02:04.340 --> 00:02:05.760
going to take a look at this request.

49
00:02:05.900 --> 00:02:07.380
So, I'm going to come to Foxy Proxy,

50
00:02:07.979 --> 00:02:10.640
switch on BupSuite, which is listening on 8080,

51
00:02:11.100 --> 00:02:12.900
and hit refresh location.

52
00:02:14.320 --> 00:02:15.620
And then I'm going to come over to

53
00:02:15.620 --> 00:02:17.940
BupSuite, come to my HTTP history.

54
00:02:18.300 --> 00:02:22.780
I'm just going to remove this Google request,

55
00:02:23.280 --> 00:02:25.020
and here we are.

56
00:02:25.740 --> 00:02:27.580
So, let's take a closer look at this,

57
00:02:27.620 --> 00:02:28.860
and I'm just going to move my face

58
00:02:28.860 --> 00:02:29.600
out of the way.

59
00:02:30.920 --> 00:02:34.120
Here we have the get identity API V2

60
00:02:34.120 --> 00:02:36.500
vehicle, and we have a vehicle ID.

61
00:02:36.920 --> 00:02:38.080
So, this looks like a GUID.

62
00:02:38.520 --> 00:02:42.600
Very long, probably difficult to guess, but nonetheless,

63
00:02:42.860 --> 00:02:44.240
we should make note of this because it's

64
00:02:44.240 --> 00:02:45.940
referencing the object directly.

65
00:02:46.500 --> 00:02:47.940
And then we have slash location.

66
00:02:48.600 --> 00:02:51.360
And in here, it returns some sensitive data.

67
00:02:51.920 --> 00:02:54.820
Now, if it didn't really return anything interesting,

68
00:02:55.180 --> 00:02:57.900
then maybe we wouldn't look so closely at

69
00:02:57.900 --> 00:02:59.620
this endpoint, but because we can see the

70
00:02:59.620 --> 00:03:03.500
latitude, longitude, and the name of the person

71
00:03:03.500 --> 00:03:05.820
it's assigned to, I would say this warrants

72
00:03:05.820 --> 00:03:07.080
some investigation.

73
00:03:07.900 --> 00:03:09.400
So, we're going to send this to repeater

74
00:03:09.400 --> 00:03:13.380
for later on, and actually, we're just going

75
00:03:13.380 --> 00:03:14.240
to do a quick test.

76
00:03:14.540 --> 00:03:16.940
So, we're just going to cut this, and

77
00:03:16.940 --> 00:03:20.220
I'm just going to put in 123123, and

78
00:03:20.220 --> 00:03:21.380
we get a 400.

79
00:03:21.720 --> 00:03:24.220
So, nothing interesting from there.

80
00:03:24.740 --> 00:03:26.480
And you can try a few different payloads,

81
00:03:26.580 --> 00:03:29.140
like zero, minus one, and some different things

82
00:03:29.140 --> 00:03:30.620
to try and trick the application.

83
00:03:31.420 --> 00:03:32.900
With code review, that might be a little

84
00:03:32.900 --> 00:03:34.460
bit easier to figure out if there is

85
00:03:34.460 --> 00:03:36.860
a payload that will trick this.

86
00:03:37.360 --> 00:03:41.760
But we don't get any successful results without

87
00:03:41.760 --> 00:03:43.040
a valid ID.

88
00:03:44.400 --> 00:03:46.200
So, if we come back to our application,

89
00:03:46.520 --> 00:03:49.060
we now need to think, hmm, where can

90
00:03:49.060 --> 00:03:53.000
we find a ID within this application?

91
00:03:53.700 --> 00:03:55.320
And it just so happens that when we

92
00:03:55.320 --> 00:03:57.880
come to the page, and we come to

93
00:03:57.880 --> 00:04:02.220
slash forum, this triggers a call to the

94
00:04:02.220 --> 00:04:02.720
endpoint.

95
00:04:05.540 --> 00:04:07.720
Community posts slash recent.

96
00:04:08.760 --> 00:04:10.560
And as we're going through and checking all

97
00:04:10.560 --> 00:04:13.260
of the API endpoints, this one is of

98
00:04:13.260 --> 00:04:17.240
particular interest, because actually, it gives us quite

99
00:04:17.240 --> 00:04:18.019
a lot of information.

100
00:04:18.019 --> 00:04:20.440
This is definitely excessive data exposure.

101
00:04:21.019 --> 00:04:24.040
So, we've got email addresses, we've got nicknames,

102
00:04:24.440 --> 00:04:26.260
and as we look on the page, we're

103
00:04:26.260 --> 00:04:30.760
only actually using the username and the post,

104
00:04:31.040 --> 00:04:34.020
like excerpt or some text.

105
00:04:34.360 --> 00:04:36.480
We don't need things like the email address

106
00:04:36.480 --> 00:04:38.280
and things like that of the users.

107
00:04:38.600 --> 00:04:41.560
So, this API endpoint, whoops, is sending back

108
00:04:41.560 --> 00:04:42.720
way too much data.

109
00:04:44.200 --> 00:04:45.780
And so, this is a finding in itself.

110
00:04:46.240 --> 00:04:49.280
And we'll talk about excessive data exposure later

111
00:04:49.280 --> 00:04:49.580
on.

112
00:04:49.880 --> 00:04:52.120
But here, it gives us the vehicle ID.

113
00:04:52.540 --> 00:04:55.840
So, our hunt, although it was very short,

114
00:04:56.000 --> 00:04:57.120
has been successful.

115
00:04:57.780 --> 00:05:00.100
And we can verify this by taking this

116
00:05:00.100 --> 00:05:03.180
ID, coming back over to the repeater, and

117
00:05:03.180 --> 00:05:04.320
pasting it in here.

118
00:05:05.240 --> 00:05:08.280
Now, in a correct implementation, when we send

119
00:05:08.280 --> 00:05:09.800
this request, it's going to come back and

120
00:05:09.800 --> 00:05:11.060
say, hey, you're not authorized.

121
00:05:11.280 --> 00:05:12.940
You're not allowed to see the location of

122
00:05:12.940 --> 00:05:14.420
cars that don't belong to you.

123
00:05:14.640 --> 00:05:17.460
But because we have the broken object level

124
00:05:17.460 --> 00:05:20.500
authorization vulnerability here, as long as I have

125
00:05:20.500 --> 00:05:23.620
the vehicle ID or the object ID, I

126
00:05:23.620 --> 00:05:25.600
can make this request and I can see

127
00:05:25.600 --> 00:05:27.700
the information of this car.

128
00:05:28.520 --> 00:05:30.420
So, that's the first vulnerability that we have

129
00:05:30.420 --> 00:05:32.080
that we've walked through together.

130
00:05:32.320 --> 00:05:33.460
And I hope that made sense.

131
00:05:33.800 --> 00:05:37.360
Every time you see a URL and you

132
00:05:37.360 --> 00:05:39.800
see a object ID being referenced, or if

133
00:05:39.800 --> 00:05:41.820
you see it being passed within the body

134
00:05:41.820 --> 00:05:44.900
of a request, we should look at we

135
00:05:44.900 --> 00:05:47.840
should consider, is this a BOLA vulnerability?

136
00:05:47.840 --> 00:05:49.760
Is this a vulnerability here?

137
00:05:50.860 --> 00:05:52.980
So, for your challenge, I'd like you to

138
00:05:52.980 --> 00:05:54.820
come back to the dashboard and take a

139
00:05:54.820 --> 00:05:56.460
look at the contact mechanic.

140
00:05:56.920 --> 00:06:01.040
So, if we just click dashboard, contact mechanic.

141
00:06:02.020 --> 00:06:05.200
With this, send some requests, inspect them, and

142
00:06:05.200 --> 00:06:07.140
see if you can identify the BOLA vulnerability.

143
00:06:08.120 --> 00:06:09.880
Try and spend at least 30 minutes on

144
00:06:09.880 --> 00:06:10.120
this.

145
00:06:10.340 --> 00:06:11.820
If you're really stuck, don't worry.

146
00:06:12.140 --> 00:06:13.580
We'll work through it together at the end

147
00:06:13.580 --> 00:06:14.040
of the module.

148
00:06:14.440 --> 00:06:14.860
Good luck.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.390 --> 00:00:04.930
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So, in a nutshell, Broken Function Level Authorization,

2
00:00:05.250 --> 00:00:08.390
BAFLA, is all about performing actions that you

3
00:00:08.390 --> 00:00:09.690
shouldn't be allowed to perform.

4
00:00:10.310 --> 00:00:12.910
For example, if you're not a moderator within

5
00:00:12.910 --> 00:00:15.350
a web application, you shouldn't be allowed to

6
00:00:15.350 --> 00:00:18.230
delete another user's posts if it's like a

7
00:00:18.230 --> 00:00:18.470
forum.

8
00:00:19.250 --> 00:00:21.470
Another example could be that you shouldn't be

9
00:00:21.470 --> 00:00:23.850
allowed to update the password of another user

10
00:00:23.850 --> 00:00:24.290
account.

11
00:00:24.550 --> 00:00:26.290
You should only be able to update your

12
00:00:26.290 --> 00:00:26.830
own password.

13
00:00:27.890 --> 00:00:30.610
So when we approach testing for BAFLA vulnerabilities,

14
00:00:31.110 --> 00:00:32.790
there are a few common techniques that we

15
00:00:32.790 --> 00:00:33.650
need to try out.

16
00:00:34.110 --> 00:00:37.110
We can test different HTTP methods, for example,

17
00:00:37.270 --> 00:00:40.250
changing a GET request to a PUT request.

18
00:00:40.870 --> 00:00:43.750
We can also manipulate the parameters within the

19
00:00:43.750 --> 00:00:46.470
request so that the action we're trying to

20
00:00:46.470 --> 00:00:49.450
perform is attempted on a different object or

21
00:00:49.450 --> 00:00:50.930
within a different context.

22
00:00:51.750 --> 00:00:54.770
So every time we come across functionality where

23
00:00:54.770 --> 00:00:57.850
something can be added, changed, or deleted, we

24
00:00:57.850 --> 00:01:00.050
should be checking for BAFLA vulnerabilities.

25
00:01:01.350 --> 00:01:03.230
So let's dive into a hands-on example.

26
00:01:03.810 --> 00:01:05.350
Now, I'm going to use VAPI for this,

27
00:01:05.790 --> 00:01:07.390
and this is because I want to give

28
00:01:07.390 --> 00:01:10.750
you a small challenge within the crappy application

29
00:01:10.750 --> 00:01:12.710
to find a BAFLA vulnerability.

30
00:01:13.910 --> 00:01:16.150
A quick side note about the challenges before

31
00:01:16.150 --> 00:01:16.810
we dive in.

32
00:01:17.490 --> 00:01:19.790
For these smaller ones, it's up to you

33
00:01:19.790 --> 00:01:21.530
how long you spend on them, or even

34
00:01:21.530 --> 00:01:22.770
if you complete them at all.

35
00:01:23.210 --> 00:01:25.290
But keep in mind that you'll be developing

36
00:01:25.290 --> 00:01:27.310
knowledge and skills that you need for the

37
00:01:27.310 --> 00:01:30.290
mid-course capstone and the final capstone challenges,

38
00:01:30.590 --> 00:01:33.910
and also for future penetration tests and your

39
00:01:33.910 --> 00:01:34.530
future career.

40
00:01:34.930 --> 00:01:37.770
So my advice is take them seriously, give

41
00:01:37.770 --> 00:01:39.850
them a good try, and if you get

42
00:01:39.850 --> 00:01:41.990
stuck, don't worry, we'll go through it together

43
00:01:41.990 --> 00:01:43.170
later on.

44
00:01:43.530 --> 00:01:46.630
Here, we're going to find and exploit some

45
00:01:46.630 --> 00:01:48.610
hidden admin functionality.

46
00:01:49.590 --> 00:01:51.570
Now, you might think to yourself as we're

47
00:01:51.570 --> 00:01:53.530
going through this, but how would I find

48
00:01:53.530 --> 00:01:53.850
this?

49
00:01:54.170 --> 00:01:56.070
This is kind of a tricky example.

50
00:01:56.690 --> 00:01:58.890
Well, if we go back to our enumeration

51
00:01:58.890 --> 00:02:02.170
section and we think about how we map

52
00:02:02.170 --> 00:02:05.350
endpoints, how we do directory busting, how we

53
00:02:05.350 --> 00:02:09.370
do enumeration discovery, coupled with potentially source code

54
00:02:09.370 --> 00:02:12.770
review and having a look at documentation if

55
00:02:12.770 --> 00:02:15.470
it's available, you should be able to find

56
00:02:15.470 --> 00:02:18.510
endpoints that maybe have been forgotten about or

57
00:02:18.510 --> 00:02:22.170
maybe just don't exist in the public documentation.

58
00:02:23.050 --> 00:02:24.630
So what I'm going to do is I'm

59
00:02:24.630 --> 00:02:27.030
just going to come to imports, and I'm

60
00:02:27.030 --> 00:02:29.790
just going to come to upload files, and

61
00:02:29.790 --> 00:02:32.830
then I'm going to come home, dev, VAPI,

62
00:02:33.270 --> 00:02:33.730
Postman.

63
00:02:34.030 --> 00:02:36.670
And so wherever you put your VAPI installation,

64
00:02:36.850 --> 00:02:38.530
if you want to follow along, you're welcome

65
00:02:38.530 --> 00:02:40.450
to do this, and you want to import

66
00:02:40.450 --> 00:02:41.650
these two files.

67
00:02:41.830 --> 00:02:45.750
So VAPI Postman collection and VAPI EMV Postman

68
00:02:45.750 --> 00:02:46.210
environment.

69
00:02:46.910 --> 00:02:49.730
So I'll just open these, click imports, and

70
00:02:49.730 --> 00:02:52.390
you'll see that it's created our collection here.

71
00:02:52.870 --> 00:02:55.050
And we're going to look at API number

72
00:02:55.050 --> 00:02:55.430
five.

73
00:02:55.610 --> 00:02:58.770
So we have create user and get user.

74
00:02:59.170 --> 00:03:01.830
Now, if I come to the VAPI documentation,

75
00:03:02.770 --> 00:03:05.930
oops, and I come to create user, we

76
00:03:05.930 --> 00:03:08.250
can see the documentation for this along with

77
00:03:08.250 --> 00:03:08.870
an example.

78
00:03:09.110 --> 00:03:13.730
So username, password, name, address, mobile number, and

79
00:03:13.730 --> 00:03:15.590
we should get a 200 back.

80
00:03:16.130 --> 00:03:19.570
And then when we get user, we should

81
00:03:19.570 --> 00:03:21.990
be able to post the user ID, as

82
00:03:21.990 --> 00:03:24.510
you can see here, and we should get

83
00:03:24.510 --> 00:03:27.330
a 200 back with the user information.

84
00:03:27.490 --> 00:03:28.490
So let's test this out.

85
00:03:29.490 --> 00:03:32.370
So let's come to create user, and it

86
00:03:32.370 --> 00:03:33.950
looks like this is all set up and

87
00:03:33.950 --> 00:03:34.510
ready to go.

88
00:03:34.890 --> 00:03:37.110
If it doesn't like this variable, you can

89
00:03:37.110 --> 00:03:39.550
right click and set it to local host,

90
00:03:40.210 --> 00:03:41.790
but in this case it's already set up

91
00:03:41.790 --> 00:03:42.470
and ready to go.

92
00:03:43.610 --> 00:03:44.750
And we click send.

93
00:03:45.490 --> 00:03:47.750
And we wanted to create test user two,

94
00:03:48.390 --> 00:03:50.590
and we have test user and ABC and

95
00:03:50.590 --> 00:03:52.890
mobile number, and the ID is number three.

96
00:03:53.930 --> 00:03:56.170
So now if we come to get user,

97
00:03:57.150 --> 00:03:59.230
and we test this, and it's going to

98
00:03:59.230 --> 00:04:02.090
pass in the current, it's automatically going to

99
00:04:02.090 --> 00:04:03.290
pass in the ID three.

100
00:04:03.790 --> 00:04:06.110
So everything's nicely set up for us for

101
00:04:06.110 --> 00:04:06.450
testing.

102
00:04:06.550 --> 00:04:09.070
Of course, we could manually change this, and

103
00:04:09.070 --> 00:04:11.690
we get a successful response, and we have

104
00:04:11.690 --> 00:04:15.730
our test user two, test user ABC 88888.

105
00:04:16.070 --> 00:04:17.870
So if I wanted to get a different

106
00:04:17.870 --> 00:04:21.870
user, for example user one, when I click

107
00:04:21.870 --> 00:04:26.090
send, I get false username or password incorrect.

108
00:04:26.670 --> 00:04:30.570
So there is correct authorization put in place

109
00:04:30.570 --> 00:04:34.150
here to stop me accessing other users.

110
00:04:34.910 --> 00:04:37.310
Now if I could access the other users,

111
00:04:37.470 --> 00:04:39.810
for example ID number one, this would probably

112
00:04:39.810 --> 00:04:42.330
be broken objects level authorization.

113
00:04:43.170 --> 00:04:45.090
But what we're going to do is we're

114
00:04:45.090 --> 00:04:48.130
going to list all of the users, and

115
00:04:48.130 --> 00:04:52.070
click send, and here we get a nice

116
00:04:52.070 --> 00:04:52.510
flag.

117
00:04:53.350 --> 00:04:55.050
If I move myself out of the way,

118
00:04:55.670 --> 00:04:58.410
and you can see that we've listed all

119
00:04:58.410 --> 00:05:00.970
of the users within the application.

120
00:05:01.330 --> 00:05:05.590
So the couple that we've created, and ID

121
00:05:05.590 --> 00:05:07.830
number one, which is the admin user as

122
00:05:07.830 --> 00:05:08.090
well.

123
00:05:08.550 --> 00:05:10.490
So being able to grab all of the

124
00:05:10.490 --> 00:05:16.090
users is administrative functionality, and therefore we shouldn't

125
00:05:16.090 --> 00:05:17.870
be able to do or carry out this

126
00:05:17.870 --> 00:05:21.530
function, and this counts as broken function level

127
00:05:21.530 --> 00:05:24.130
authorization, also known as bafla.

128
00:05:26.420 --> 00:05:28.960
All right, for the bafla challenge, I wanted

129
00:05:28.960 --> 00:05:31.220
to point you in the right direction.

130
00:05:31.560 --> 00:05:33.940
So if we check out postman here, we

131
00:05:33.940 --> 00:05:37.240
see we have some video functionality under the

132
00:05:37.240 --> 00:05:40.260
crappy postman collection.

133
00:05:41.140 --> 00:05:43.020
So if we just scroll down, we can

134
00:05:43.020 --> 00:05:45.220
see that we have add new video, delete

135
00:05:45.220 --> 00:05:48.300
video, delete video by admin, re-add new

136
00:05:48.300 --> 00:05:49.960
video, etc, etc.

137
00:05:50.960 --> 00:05:53.440
Now there is a short video test file

138
00:05:53.440 --> 00:05:55.820
that you can use that comes with crappy.

139
00:05:56.060 --> 00:05:58.880
So if you just come into crappy, and

140
00:05:58.880 --> 00:06:02.260
cd into postman collections, you'll see that you

141
00:06:02.260 --> 00:06:04.700
can use this car.mp4. So you don't

142
00:06:04.700 --> 00:06:06.240
need to go away and source your own

143
00:06:06.240 --> 00:06:08.120
video for this testing.

144
00:06:09.860 --> 00:06:12.400
So the challenge is try to add a

145
00:06:12.400 --> 00:06:14.620
video, then remove it, make sure the functionality

146
00:06:14.620 --> 00:06:17.360
works, and then do some testing across different

147
00:06:17.360 --> 00:06:17.820
users.

148
00:06:18.280 --> 00:06:20.000
So the challenge here is to see if

149
00:06:20.000 --> 00:06:22.800
you can remove the video of another user,

150
00:06:23.300 --> 00:06:26.960
so abusing that authorization that should be in

151
00:06:26.960 --> 00:06:27.320
place.

152
00:06:28.240 --> 00:06:29.920
Now it's up to you if you use

153
00:06:29.920 --> 00:06:32.440
burp suite, or postman, or any other tool.

154
00:06:32.700 --> 00:06:35.080
Personally, for most of my testing, I use

155
00:06:35.080 --> 00:06:35.640
burp suites.

156
00:06:36.260 --> 00:06:39.060
But as we've seen, different tools can help

157
00:06:39.060 --> 00:06:41.520
you out in different situations, and you might

158
00:06:41.520 --> 00:06:43.780
find that you settle more into postman, and

159
00:06:43.780 --> 00:06:45.880
it might work better with your workflow.

160
00:06:46.440 --> 00:06:48.740
So try them both, see what works for

161
00:06:48.740 --> 00:06:50.960
you, and keep an open mind when it

162
00:06:50.960 --> 00:06:53.720
comes to trying out new things.

163
00:06:54.560 --> 00:06:56.600
Once you've completed the challenge, I'll see you

164
00:06:56.600 --> 00:06:57.860
back here for the walkthrough.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.390 --> 00:00:02.510
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So, how did you get on with the

2
00:00:02.510 --> 00:00:03.050
challenges?

3
00:00:03.690 --> 00:00:06.510
If you solved them both, then congratulations, great

4
00:00:06.510 --> 00:00:06.870
job.

5
00:00:07.530 --> 00:00:09.410
If you didn't quite manage to find the

6
00:00:09.410 --> 00:00:11.850
solutions, then not to worry, we're going to

7
00:00:11.850 --> 00:00:14.110
walk through them together now, and the trick

8
00:00:14.110 --> 00:00:16.790
to being successful is to keep moving forward,

9
00:00:17.230 --> 00:00:19.350
learning new things, and apply what you learned

10
00:00:19.350 --> 00:00:20.050
next time.

11
00:00:20.490 --> 00:00:23.250
First, let's dive into the Ebola vulnerability.

12
00:00:24.830 --> 00:00:27.610
So here, I've just logged in as a

13
00:00:27.610 --> 00:00:30.130
normal user, and I've added the vehicle, and

14
00:00:30.130 --> 00:00:32.170
I think I pointed you guys in the

15
00:00:32.170 --> 00:00:35.470
direction of contact mechanics, so this is the

16
00:00:35.470 --> 00:00:37.090
endpoint that we're going to look at.

17
00:00:37.730 --> 00:00:39.170
So, first of all, I'm just going to

18
00:00:39.170 --> 00:00:41.710
make sure my proxy is switched on, and

19
00:00:41.710 --> 00:00:44.670
then I'm going to hit contact mechanic, and

20
00:00:44.670 --> 00:00:46.830
I'm just going to choose one randomly and

21
00:00:46.830 --> 00:00:48.790
put in some test data.

22
00:00:49.370 --> 00:00:51.130
Now, I always put something in that, you

23
00:00:51.130 --> 00:00:52.810
know, I can easily recognize, so that in

24
00:00:52.810 --> 00:00:55.370
the requests, I can see exactly what's happening,

25
00:00:55.810 --> 00:00:58.370
but you can put anything in here that

26
00:00:58.370 --> 00:00:58.870
you want.

27
00:00:59.730 --> 00:01:02.770
So, I just click send service request, and

28
00:01:02.770 --> 00:01:05.190
we get this pop-up back, and we

29
00:01:05.190 --> 00:01:08.110
click okay, and it brings us back to

30
00:01:08.110 --> 00:01:09.210
the main page.

31
00:01:09.690 --> 00:01:12.290
So, let's switch over to WebSuite and take

32
00:01:12.290 --> 00:01:14.410
a look, and I'm just going to clear

33
00:01:14.410 --> 00:01:19.470
out the Google API calls, just to make

34
00:01:19.470 --> 00:01:21.870
our UI a little bit easier to see,

35
00:01:25.250 --> 00:01:27.430
and what I want to look at is

36
00:01:27.430 --> 00:01:27.950
this.

37
00:01:28.010 --> 00:01:32.430
So, this request looks interesting, to say the

38
00:01:32.430 --> 00:01:34.870
least, and I'm just going to move myself

39
00:01:34.870 --> 00:01:35.710
out of the way.

40
00:01:36.250 --> 00:01:39.770
There we go, and what we can see

41
00:01:39.770 --> 00:01:42.810
here is when we make the request, we

42
00:01:42.810 --> 00:01:45.730
have the mechanic API, and this goes to

43
00:01:45.730 --> 00:01:50.690
HTTP local host 8888, workshop API mechanic, receive

44
00:01:50.690 --> 00:01:51.130
report.

45
00:01:51.850 --> 00:01:53.990
Now, whenever I see this, I always think,

46
00:01:54.270 --> 00:01:57.790
ah, maybe server-side request forgery, but we're

47
00:01:57.790 --> 00:01:59.050
going to do a module on that later

48
00:01:59.050 --> 00:02:03.510
on, so we'll test out that vulnerability then.

49
00:02:04.410 --> 00:02:07.389
Next up, I'm looking at the response, and

50
00:02:07.389 --> 00:02:09.229
what I can see is I can see

51
00:02:09.229 --> 00:02:10.090
a report link.

52
00:02:10.530 --> 00:02:12.930
Now, this wasn't reflected back to us in

53
00:02:12.930 --> 00:02:18.370
the UI, but it does indeed seem to

54
00:02:18.370 --> 00:02:20.670
exist, so I'm just going to copy this,

55
00:02:21.150 --> 00:02:22.810
and then I'm just going to paste this

56
00:02:22.810 --> 00:02:25.270
in here, and we can see this goes

57
00:02:25.270 --> 00:02:28.990
to API mechanic mechanic reports, and it passes

58
00:02:28.990 --> 00:02:32.690
an ID, which is equal to 6, and

59
00:02:32.690 --> 00:02:35.570
we can see the request, so we can

60
00:02:35.570 --> 00:02:39.110
see my information that I signed up with,

61
00:02:39.210 --> 00:02:42.270
so my email, my number, the problem data

62
00:02:42.270 --> 00:02:46.130
that I put in, and obviously, interestingly, we

63
00:02:46.130 --> 00:02:48.470
can see that we're passing an ID.

64
00:02:49.250 --> 00:02:51.050
So, let's test this for Bola.

65
00:02:51.190 --> 00:02:52.790
Let's just change this to 5.

66
00:02:53.850 --> 00:02:56.830
Success, and that's it.

67
00:02:57.550 --> 00:03:00.110
We managed to exploit this vulnerability.

68
00:03:00.410 --> 00:03:03.870
We can actually see Adam007 at example.com,

69
00:03:04.090 --> 00:03:08.790
and we can maybe see other reports as

70
00:03:08.790 --> 00:03:09.010
well.

71
00:03:09.350 --> 00:03:11.810
Looks like tests at example.com.

72
00:03:13.350 --> 00:03:17.630
So, this is broken object level authorization, and

73
00:03:17.630 --> 00:03:20.850
this API endpoint is kind of hidden.

74
00:03:21.310 --> 00:03:23.410
You don't really see it, at least I

75
00:03:23.410 --> 00:03:25.750
didn't see it in the user interface, so

76
00:03:25.750 --> 00:03:28.270
we had to inspect the traffic with burp

77
00:03:28.270 --> 00:03:31.010
suite, find out what's going on, and then

78
00:03:31.010 --> 00:03:34.110
check the request and response.

79
00:03:35.650 --> 00:03:38.010
So, that's the Bola challenge complete.

80
00:03:38.590 --> 00:03:41.190
Now, we discovered a hidden endpoint, and our

81
00:03:41.190 --> 00:03:42.930
Bola tests were successful.

82
00:03:43.770 --> 00:03:45.890
If this was a live application, that would

83
00:03:45.890 --> 00:03:46.930
be a really great finding.

84
00:03:47.370 --> 00:03:49.510
Next up, we have the Baffler challenge.

85
00:03:49.730 --> 00:03:51.890
So, let's do this one in Postman.

86
00:03:53.860 --> 00:03:56.720
I have my user here, and what I'm

87
00:03:56.720 --> 00:03:59.020
going to do is I'm going to upload

88
00:03:59.020 --> 00:04:01.940
a video to the dashboard, so I'm just

89
00:04:01.940 --> 00:04:05.180
going to quickly come into burp suite, clear

90
00:04:05.180 --> 00:04:10.200
history, and then an instant refills, and then

91
00:04:10.200 --> 00:04:13.320
come back, and I'm going to come to,

92
00:04:13.580 --> 00:04:16.220
if we hover over these three dots, if

93
00:04:16.220 --> 00:04:17.980
I move my face out of the way,

94
00:04:18.300 --> 00:04:20.000
if we hover over these three dots, we

95
00:04:20.000 --> 00:04:22.720
see this upload video functionality, which can be

96
00:04:22.720 --> 00:04:25.560
a little tricky to click on, and what

97
00:04:25.560 --> 00:04:26.360
I'm going to do is I'm going to

98
00:04:26.360 --> 00:04:30.060
come into my crappy installation, come to postman

99
00:04:30.060 --> 00:04:33.700
collections, and upload car.mp4, and we get

100
00:04:33.700 --> 00:04:36.440
a successful video upload, which is what we

101
00:04:36.440 --> 00:04:36.700
want.

102
00:04:37.840 --> 00:04:39.720
So, now what we're going to do is

103
00:04:39.720 --> 00:04:42.360
we're going to come over to burp suite,

104
00:04:42.880 --> 00:04:44.540
we're going to have a quick look at

105
00:04:44.540 --> 00:04:46.440
this, and we're just going to have a

106
00:04:46.440 --> 00:04:47.340
look at the id.

107
00:04:47.580 --> 00:04:50.240
So, this is id 36, and so we

108
00:04:50.240 --> 00:04:52.860
want to note this down for later, because

109
00:04:52.860 --> 00:04:54.940
this is the video we're going to try

110
00:04:54.940 --> 00:04:55.620
and delete.

111
00:04:57.080 --> 00:04:59.800
So, if we come over to postman, I'm

112
00:04:59.800 --> 00:05:01.000
just going to sign up a new account,

113
00:05:01.200 --> 00:05:05.740
so hit sign up, we're successfully registered, hit

114
00:05:05.740 --> 00:05:08.500
login, and then we can verify our token

115
00:05:08.500 --> 00:05:12.180
just for completeness, and we're good to go.

116
00:05:13.200 --> 00:05:15.440
So, if I come down here, what I'm

117
00:05:15.440 --> 00:05:16.960
going to do is I'm also going to

118
00:05:16.960 --> 00:05:19.740
upload a video for this new user to

119
00:05:19.740 --> 00:05:20.500
test.

120
00:05:21.440 --> 00:05:23.720
So, if I just come to add video,

121
00:05:24.280 --> 00:05:28.580
and hit send, we get a 400 bad

122
00:05:28.580 --> 00:05:32.700
request, and I presume it's because this video

123
00:05:32.700 --> 00:05:35.260
file doesn't like this for some reason.

124
00:05:35.400 --> 00:05:36.800
So, what I'm going to do is just

125
00:05:36.800 --> 00:05:42.080
remove this, click select files, home, dev, whoops,

126
00:05:42.220 --> 00:05:48.620
not fappy, crappy, postman collections, card.mp4, and

127
00:05:48.620 --> 00:05:50.620
then we hit send, and it works.

128
00:05:51.040 --> 00:05:53.480
So, sometimes when we're working with collections, or

129
00:05:53.480 --> 00:05:55.680
if we're working with information that we get

130
00:05:55.680 --> 00:05:59.160
from an engineering team, things aren't always going

131
00:05:59.160 --> 00:05:59.480
to work.

132
00:05:59.820 --> 00:06:02.120
Some things are going to be broken, you'll

133
00:06:02.120 --> 00:06:04.800
sometimes get misinformation, maybe you won't get as

134
00:06:04.800 --> 00:06:07.080
many accounts as you asked for, all sorts

135
00:06:07.080 --> 00:06:07.480
of things.

136
00:06:07.860 --> 00:06:09.340
And, you know, that's just part of being

137
00:06:09.340 --> 00:06:11.680
a security engineer, or working in tech in

138
00:06:11.680 --> 00:06:13.360
general, is that, you know, we have to

139
00:06:13.360 --> 00:06:15.860
be able to deal with misinformation or things

140
00:06:15.860 --> 00:06:17.760
sometimes troubleshoot some stuff.

141
00:06:18.240 --> 00:06:20.800
So, we got our video, we got our

142
00:06:20.800 --> 00:06:24.180
200 okay, and our video is successfully uploaded.

143
00:06:25.080 --> 00:06:27.180
And to test this, let's just do the

144
00:06:27.180 --> 00:06:27.780
get video.

145
00:06:28.140 --> 00:06:32.240
So, this is id 38, and then if

146
00:06:32.240 --> 00:06:33.780
we just hover over, we can see the

147
00:06:33.780 --> 00:06:35.420
current is id 38.

148
00:06:35.760 --> 00:06:38.980
Hit send, and we do indeed get our

149
00:06:38.980 --> 00:06:39.700
video back.

150
00:06:40.520 --> 00:06:42.180
Now, what I want to do is I

151
00:06:42.180 --> 00:06:43.560
want to test this delete video.

152
00:06:43.800 --> 00:06:44.940
So, we're just going to test it on

153
00:06:44.940 --> 00:06:46.080
ourselves first.

154
00:06:46.280 --> 00:06:48.820
So, I just hit send, and it kind

155
00:06:48.820 --> 00:06:49.880
of gives us a bit of a hint

156
00:06:49.880 --> 00:06:53.980
here, although some functionality or API endpoints will

157
00:06:53.980 --> 00:06:59.340
give us information as you're testing, but try

158
00:06:59.340 --> 00:07:03.160
to access the admin API is, if I

159
00:07:03.160 --> 00:07:05.300
move myself out the way, is quite a

160
00:07:05.300 --> 00:07:07.320
big hint for this challenge.

161
00:07:08.700 --> 00:07:11.460
So, I'm going to come over to delete

162
00:07:11.460 --> 00:07:14.240
video by admin, I'm going to click send,

163
00:07:15.220 --> 00:07:17.500
and we get an interesting error here.

164
00:07:17.860 --> 00:07:19.780
So, invalid token.

165
00:07:21.100 --> 00:07:23.720
Interesting that it doesn't say that we don't

166
00:07:23.720 --> 00:07:25.320
have privileges to do it.

167
00:07:25.360 --> 00:07:27.940
It actually says our token is invalid.

168
00:07:28.200 --> 00:07:30.900
So, I suspect there's something slightly off, again,

169
00:07:31.040 --> 00:07:33.240
with this request or this setup.

170
00:07:33.740 --> 00:07:35.580
So, what I'm going to do is instead

171
00:07:35.580 --> 00:07:38.260
of troubleshooting this and trying to fix it,

172
00:07:39.200 --> 00:07:42.400
I'm just going to pay attention to the

173
00:07:42.400 --> 00:07:46.940
URI, and it says here API slash V2

174
00:07:46.940 --> 00:07:49.960
slash admin slash videos, and this looks very

175
00:07:49.960 --> 00:07:54.020
similar to API slash V2 slash user slash

176
00:07:54.020 --> 00:07:54.420
videos.

177
00:07:54.940 --> 00:07:57.440
So, I know that this endpoint works correctly.

178
00:07:57.700 --> 00:07:58.940
So, I'm just going to type in slash

179
00:07:58.940 --> 00:08:02.460
admin and hit send, and it says our

180
00:08:02.460 --> 00:08:04.500
video is deleted successfully.

181
00:08:04.760 --> 00:08:06.000
Now, we need to verify this.

182
00:08:06.680 --> 00:08:09.240
So, we have video 38.

183
00:08:09.820 --> 00:08:12.240
If we come back to get video, we're

184
00:08:12.240 --> 00:08:13.820
still requesting video 38.

185
00:08:14.640 --> 00:08:16.560
We get video not found.

186
00:08:16.860 --> 00:08:17.260
Awesome.

187
00:08:17.600 --> 00:08:18.980
So, we can delete our own video.

188
00:08:19.640 --> 00:08:21.860
So, let's come back here, and we'll double

189
00:08:21.860 --> 00:08:22.720
check the ID.

190
00:08:22.900 --> 00:08:25.920
So, 36 is the one that appeared in

191
00:08:25.920 --> 00:08:26.420
burp suite.

192
00:08:27.660 --> 00:08:30.420
So, we'll come back, and then we'll do

193
00:08:30.420 --> 00:08:31.539
our delete video.

194
00:08:31.880 --> 00:08:34.700
So, I'm just going to type in 36.

195
00:08:35.600 --> 00:08:37.440
And then we're going to hit send, and

196
00:08:37.440 --> 00:08:40.100
it says, again, user video deleted successfully.

197
00:08:40.720 --> 00:08:41.580
Status 200.

198
00:08:42.780 --> 00:08:43.240
Huzzah.

199
00:08:43.480 --> 00:08:48.160
We have broken function level authorization, and we

200
00:08:48.160 --> 00:08:49.040
should double check this.

201
00:08:49.220 --> 00:08:51.200
We should make sure that this actually happened

202
00:08:51.200 --> 00:08:52.340
on the user profile.

203
00:08:52.540 --> 00:08:54.520
So, we come here, and we hit refresh,

204
00:08:55.220 --> 00:08:58.440
and interestingly, it looks like the video is

205
00:08:58.440 --> 00:08:59.120
still there.

206
00:09:00.300 --> 00:09:03.080
So, what we're actually going to do is

207
00:09:03.080 --> 00:09:06.020
front end frameworks can be quite complicated.

208
00:09:06.660 --> 00:09:08.300
There's a lot of stuff happening behind the

209
00:09:08.300 --> 00:09:11.700
scenes, especially with caching and all sorts of

210
00:09:11.700 --> 00:09:14.220
things that might be keeping stuff alive.

211
00:09:14.400 --> 00:09:17.240
So, what I'm going to do is I'm

212
00:09:17.240 --> 00:09:18.340
just going to log out.

213
00:09:19.000 --> 00:09:20.580
I'm going to log back in.

214
00:09:25.720 --> 00:09:27.940
Come back to the profile, and we can

215
00:09:27.940 --> 00:09:30.680
see we have indeed deleted the video.

216
00:09:31.240 --> 00:09:34.560
So, here we can delete videos of ourselves

217
00:09:34.560 --> 00:09:36.020
and of other users.

218
00:09:36.240 --> 00:09:39.540
So, we have broken function level authorization.

219
00:09:40.060 --> 00:09:43.300
So, that's it for this module.

220
00:09:43.600 --> 00:09:46.120
You've made tremendous progress so far, and I

221
00:09:46.120 --> 00:09:47.300
hope you can keep it up until the

222
00:09:47.300 --> 00:09:49.460
end of the course and into your continued

223
00:09:49.460 --> 00:09:50.420
study beyond.

224
00:09:51.160 --> 00:09:52.760
Now that you have the fundamentals down for

225
00:09:52.760 --> 00:09:55.120
these vulnerabilities, you should be looking always to

226
00:09:55.120 --> 00:09:57.540
expand your knowledge and build on these foundations.

227
00:09:58.080 --> 00:09:59.920
A good way to do this is by

228
00:09:59.920 --> 00:10:02.980
reading writeups of real world attacks and findings.

229
00:10:03.720 --> 00:10:06.300
And a good place to start is with

230
00:10:06.300 --> 00:10:07.320
Sam Curry's blog.

231
00:10:07.700 --> 00:10:09.720
You can access it at samcurry.net.

232
00:10:10.080 --> 00:10:12.140
It has a bunch of great writeups and

233
00:10:12.140 --> 00:10:14.540
features vulnerabilities that we've covered so far.

234
00:10:14.960 --> 00:10:17.220
I hope you enjoyed this module, and I'll

235
00:10:17.220 --> 00:10:18.020
see you in the next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Attacking Authentification

WEBVTT

1
00:00:00.170 --> 00:00:01.910
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome to the next section.

2
00:00:02.310 --> 00:00:04.210
Now we're going to talk about authentication.

3
00:00:04.850 --> 00:00:06.410
So what is authentication?

4
00:00:07.050 --> 00:00:09.630
Well, it's really all about who you are

5
00:00:09.630 --> 00:00:11.410
and proving your identity.

6
00:00:11.950 --> 00:00:14.110
So when you check into a hotel, you

7
00:00:14.110 --> 00:00:15.050
provide your ID.

8
00:00:15.650 --> 00:00:17.610
That might be a driving license or passport

9
00:00:17.610 --> 00:00:20.050
or some other form of identification.

10
00:00:20.670 --> 00:00:22.790
And this is authentication.

11
00:00:23.430 --> 00:00:27.070
So in web applications, particularly with APIs, there

12
00:00:27.070 --> 00:00:29.790
are a few different methods of authentication that

13
00:00:29.790 --> 00:00:30.830
we need to know about.

14
00:00:31.189 --> 00:00:33.950
So the first one is HTTP basic authentication.

15
00:00:34.330 --> 00:00:36.690
We also need to know about bearer tokens.

16
00:00:36.990 --> 00:00:40.370
So JSON web tokens, OAuth 2.0 and

17
00:00:40.370 --> 00:00:41.530
API keys.

18
00:00:41.990 --> 00:00:45.010
Now, basic authentication is not used quite as

19
00:00:45.010 --> 00:00:46.210
much as it used to be.

20
00:00:46.410 --> 00:00:48.170
And there's a good reason for this.

21
00:00:48.550 --> 00:00:51.490
The credentials are simply encoded and passed with

22
00:00:51.490 --> 00:00:52.270
every request.

23
00:00:52.630 --> 00:00:54.210
And this is not a good way to

24
00:00:54.210 --> 00:00:57.270
protect credentials, sending them with every request that

25
00:00:57.270 --> 00:00:57.730
we make.

26
00:00:58.190 --> 00:01:00.350
But they are very easy to implement and

27
00:01:00.350 --> 00:01:00.830
use.

28
00:01:01.850 --> 00:01:04.970
Now, bearer tokens, which are sometimes referred to

29
00:01:04.970 --> 00:01:08.250
as token authentication, are very popular when working

30
00:01:08.250 --> 00:01:08.950
with APIs.

31
00:01:09.410 --> 00:01:12.250
They're typically passed in the authorization header, but

32
00:01:12.250 --> 00:01:14.290
contain the requester's identity.

33
00:01:15.070 --> 00:01:18.270
One weakness of this approach, though, is that

34
00:01:18.270 --> 00:01:21.530
an application implicitly trusts that the token is

35
00:01:21.530 --> 00:01:23.490
owned by the supplier of the token.

36
00:01:23.810 --> 00:01:25.250
So when I make a request to an

37
00:01:25.250 --> 00:01:28.930
application with a token, the application assumes that

38
00:01:28.930 --> 00:01:30.550
that token belongs to me.

39
00:01:30.710 --> 00:01:32.310
It doesn't really have a way of checking

40
00:01:32.310 --> 00:01:34.850
that I've stolen it or generated it in

41
00:01:34.850 --> 00:01:35.390
some way.

42
00:01:35.810 --> 00:01:38.210
If we managed to steal or guess another

43
00:01:38.210 --> 00:01:40.710
user's token, then the application would be none

44
00:01:40.710 --> 00:01:41.210
the wiser.

45
00:01:42.870 --> 00:01:46.850
JWTs, JSON web tokens, OAuth 2.0 and

46
00:01:46.850 --> 00:01:49.790
API keys are all examples of bearer tokens.

47
00:01:50.410 --> 00:01:52.790
Over the next few sections, we'll look at

48
00:01:52.790 --> 00:01:55.750
how we can attack authentication mechanisms and the

49
00:01:55.750 --> 00:01:56.710
tokens themselves.

50
00:01:57.370 --> 00:01:59.430
Now, if you feel a little bit overwhelmed

51
00:01:59.430 --> 00:02:01.690
at this point about the different authentication schemes

52
00:02:01.690 --> 00:02:04.910
and types of tokens, then don't worry.

53
00:02:05.310 --> 00:02:07.190
We're going to go through and take a

54
00:02:07.190 --> 00:02:08.789
closer look at all of them in action

55
00:02:08.789 --> 00:02:11.050
and build a foundation that you can expand

56
00:02:11.050 --> 00:02:12.210
on going forwards.

57
00:02:12.410 --> 00:02:13.390
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.760 --> 00:00:02.040
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So, there are a number of common ways

2
00:00:02.040 --> 00:00:04.680
to attack authentication which apply to APIs.

3
00:00:05.100 --> 00:00:06.540
We'll take a quick look at these as

4
00:00:06.540 --> 00:00:08.740
a refresher, but then dive into how we

5
00:00:08.740 --> 00:00:11.360
can attack tokens more specifically in the next

6
00:00:11.360 --> 00:00:11.680
video.

7
00:00:12.520 --> 00:00:15.600
So, usually we can break authentication in two

8
00:00:15.600 --> 00:00:15.980
ways.

9
00:00:16.480 --> 00:00:19.740
Firstly, the target is unprotected against brute force

10
00:00:19.740 --> 00:00:20.160
attacks.

11
00:00:20.540 --> 00:00:22.260
Now, a finding I get all the time

12
00:00:22.260 --> 00:00:25.200
when assessing API endpoints is a lack of

13
00:00:25.200 --> 00:00:27.700
rate limiting or brute force protection, which is

14
00:00:27.700 --> 00:00:29.660
a little bit odd because these things are

15
00:00:29.660 --> 00:00:32.580
quite trivial to implement, but often forgotten about.

16
00:00:33.240 --> 00:00:36.040
Secondly, there is a logic issue with the

17
00:00:36.040 --> 00:00:37.220
authentication mechanism.

18
00:00:38.080 --> 00:00:40.020
Now, it's also worth noting that we may

19
00:00:40.020 --> 00:00:42.920
be able to bypass or break authentication with

20
00:00:42.920 --> 00:00:44.480
things like injection attacks.

21
00:00:45.100 --> 00:00:47.960
However, because the root cause of the issue

22
00:00:47.960 --> 00:00:50.220
in this case is injection, we tend to

23
00:00:50.220 --> 00:00:52.680
classify it as that rather than something like

24
00:00:52.680 --> 00:00:53.720
broken authentication.

25
00:00:54.720 --> 00:00:56.680
In these types of scenarios, it's best to

26
00:00:56.680 --> 00:00:58.880
try and identify the root cause and use

27
00:00:58.880 --> 00:00:59.660
your best judgments.

28
00:01:00.640 --> 00:01:02.760
Now, if you're already familiar with brute force

29
00:01:02.760 --> 00:01:04.580
attacks, then feel free to give this lab

30
00:01:04.580 --> 00:01:05.700
a go first on your own.

31
00:01:06.500 --> 00:01:08.520
Just another thing to note, I'll be showing

32
00:01:08.520 --> 00:01:10.240
you two ways to pull off this attack.

33
00:01:10.620 --> 00:01:12.680
One with Burp Suite Professional, and the other

34
00:01:12.680 --> 00:01:15.440
using the fuzzer FUF, or F-F-U

35
00:01:15.440 --> 00:01:15.780
-F.

36
00:01:16.680 --> 00:01:19.100
This is because not everyone has access to

37
00:01:19.100 --> 00:01:21.740
the Professional edition of Burp Suite.

38
00:01:21.740 --> 00:01:25.160
The Community edition is rate limited, which obviously

39
00:01:25.160 --> 00:01:27.540
for brute forcing makes things a little bit

40
00:01:27.540 --> 00:01:30.260
tricky, but if you're just beginning your journey

41
00:01:30.260 --> 00:01:32.880
into penetration testing, it's likely that you'll be

42
00:01:32.880 --> 00:01:35.980
ending up using the Professional edition at some

43
00:01:35.980 --> 00:01:38.320
point in the future, so it'll be good

44
00:01:38.320 --> 00:01:39.740
for you to see how it works even

45
00:01:39.740 --> 00:01:41.120
if you can't use it right now.

46
00:01:41.720 --> 00:01:44.920
Both techniques yield good results, so don't stress

47
00:01:44.920 --> 00:01:47.480
if you're strictly sticking to open source tools

48
00:01:47.480 --> 00:01:48.300
for the time being.

49
00:01:49.250 --> 00:01:51.220
Let's run through this attack together.

50
00:01:53.780 --> 00:01:58.100
So here I have the api-bruteforce-demo

51
00:01:58.100 --> 00:02:01.000
.zip in this folder, so I'm just going

52
00:02:01.000 --> 00:02:05.040
to simply unzip this and hit enter, and

53
00:02:05.040 --> 00:02:07.900
you can see it's created the folder api

54
00:02:07.900 --> 00:02:08.880
-bruteforce-demo.

55
00:02:09.120 --> 00:02:12.600
So I'm going to cd into this, clear

56
00:02:12.600 --> 00:02:14.900
my screen, and then I'm just going to

57
00:02:14.900 --> 00:02:20.300
sudo docker-compose and build, and then I'll

58
00:02:20.300 --> 00:02:23.060
just type in my password, and I'll give

59
00:02:23.060 --> 00:02:24.500
it a minute to build the application.

60
00:02:24.760 --> 00:02:26.720
This shouldn't take long, it's not too heavy.

61
00:02:34.560 --> 00:02:36.820
Alright, so that's built, and then we can

62
00:02:36.820 --> 00:02:38.800
just do the same, but instead of build,

63
00:02:38.960 --> 00:02:43.420
we can do up, like this, and it

64
00:02:43.420 --> 00:02:46.140
should be running on port 9000, so if

65
00:02:46.140 --> 00:02:49.640
I just fire up firefox and I come

66
00:02:49.640 --> 00:02:56.000
to maximize this localhost and 9000, we should

67
00:02:56.000 --> 00:03:00.200
see a bruteforce-me page with a login

68
00:03:00.200 --> 00:03:00.640
button.

69
00:03:01.680 --> 00:03:03.500
So I'm also gonna load up burp suite,

70
00:03:03.840 --> 00:03:06.200
so notice the professional edition, but you know,

71
00:03:06.220 --> 00:03:07.700
you can use the community edition as well,

72
00:03:07.860 --> 00:03:09.980
just know that you're rate limited, and we'll

73
00:03:09.980 --> 00:03:13.920
do burp suite first, and then ffuf or

74
00:03:13.920 --> 00:03:15.060
fuf afterwards.

75
00:03:17.200 --> 00:03:20.620
Alright, so what I want to do is

76
00:03:20.620 --> 00:03:24.240
first just test, so I'm just going to

77
00:03:24.240 --> 00:03:27.260
log in as admin-admin and click login,

78
00:03:27.820 --> 00:03:31.220
and we get invalid passwords, so interesting that

79
00:03:31.220 --> 00:03:33.820
we get a response, it seems like it's

80
00:03:33.820 --> 00:03:36.960
confirmed our username, so we can confirm this

81
00:03:36.960 --> 00:03:40.860
by just changing the username to something that

82
00:03:40.860 --> 00:03:42.420
is very unlikely to exist.

83
00:03:43.300 --> 00:03:46.100
And we get invalid username, so we do

84
00:03:46.100 --> 00:03:49.360
indeed know that admin is username, and of

85
00:03:49.360 --> 00:03:51.740
course the password is not admin, but that's

86
00:03:51.740 --> 00:03:52.440
what we sent.

87
00:03:53.080 --> 00:03:54.740
So I'm just going to close this for

88
00:03:54.740 --> 00:03:58.180
now, and then switch over to burp suite,

89
00:03:58.500 --> 00:04:02.040
and come to our proxy in HTTP history,

90
00:04:02.580 --> 00:04:04.500
and I forgot to turn my proxy on,

91
00:04:04.660 --> 00:04:06.740
so I'm going to come back, switch on

92
00:04:06.740 --> 00:04:10.780
my proxy, send another request of admin-admin,

93
00:04:11.560 --> 00:04:13.760
and then come back and have a look

94
00:04:13.760 --> 00:04:15.880
at this request in here.

95
00:04:16.260 --> 00:04:18.980
So we can see that it's saying email

96
00:04:18.980 --> 00:04:21.620
address and password, although this is actually username,

97
00:04:21.860 --> 00:04:23.580
so just a little bit of a coding

98
00:04:23.580 --> 00:04:26.680
error in terms of naming conventions, and all

99
00:04:26.680 --> 00:04:27.860
I'm going to do is I'm going to

100
00:04:27.860 --> 00:04:30.480
press control-i, or you can right-click

101
00:04:30.480 --> 00:04:32.460
and send to intruder.

102
00:04:33.940 --> 00:04:37.080
And in this case, we already know the

103
00:04:38.700 --> 00:04:41.320
username is admin, so I'm just going to

104
00:04:41.320 --> 00:04:44.680
clear these, not sure what this symbol is

105
00:04:44.680 --> 00:04:47.600
called, but clear the highlights, and then I'm

106
00:04:47.600 --> 00:04:49.420
going to come back in and then highlight

107
00:04:49.420 --> 00:04:51.600
the password field, because this is the field

108
00:04:51.600 --> 00:04:52.740
that we want to replace.

109
00:04:53.220 --> 00:04:54.820
If we wanted to replace the user agent,

110
00:04:54.920 --> 00:04:57.220
for example, we would highlight the user agent,

111
00:04:57.640 --> 00:04:59.300
and then we would click this, and then

112
00:04:59.300 --> 00:05:02.560
now that field is marked for our attack,

113
00:05:02.700 --> 00:05:04.700
but we don't want to clear the user

114
00:05:04.700 --> 00:05:05.640
agent in this case.

115
00:05:06.540 --> 00:05:09.400
I'll go over some more advanced brute-force

116
00:05:09.400 --> 00:05:11.460
attacks later on, but for now, we're just

117
00:05:11.460 --> 00:05:13.020
going to be using the sniper.

118
00:05:14.200 --> 00:05:16.900
Now, payloads-wise, what I'm going to do

119
00:05:16.900 --> 00:05:19.120
is I'm going to load in a word

120
00:05:19.120 --> 00:05:20.980
list, and I'm just going to click load,

121
00:05:21.260 --> 00:05:22.900
and then you can see I've been on

122
00:05:22.900 --> 00:05:27.620
TriHackMe recently, been live-streaming, and I think

123
00:05:27.620 --> 00:05:32.180
it will be in user share, whoops, not

124
00:05:32.180 --> 00:05:39.200
source, share cyclists, and I'm just going to

125
00:05:39.200 --> 00:05:41.640
go passwords, and then I want a list

126
00:05:41.640 --> 00:05:44.040
that's not too long, so even though we're

127
00:05:44.040 --> 00:05:47.600
attacking something locally, let's choose something with about

128
00:05:47.600 --> 00:05:51.080
10,000 in it, so the top 10

129
00:05:51.080 --> 00:05:53.260
million, and then we'll open this.

130
00:05:53.860 --> 00:05:56.040
Now, if you don't have cyclists already installed,

131
00:05:56.260 --> 00:05:58.540
you can just open the terminal, sudo apt

132
00:05:58.540 --> 00:06:01.420
install cyclists, and then you should be good

133
00:06:01.420 --> 00:06:01.680
to go.

134
00:06:02.080 --> 00:06:04.780
Obviously, I've already got it installed, but if

135
00:06:04.780 --> 00:06:06.320
you don't have it, you can just run

136
00:06:06.320 --> 00:06:08.760
that command, and then you should be all

137
00:06:08.760 --> 00:06:09.640
good from this point.

138
00:06:10.720 --> 00:06:12.000
And then all I'm going to do next

139
00:06:12.000 --> 00:06:14.680
is I'm going to hit start attack, and

140
00:06:14.680 --> 00:06:15.900
then I'm going to give it a minute

141
00:06:15.900 --> 00:06:16.940
to run through.

142
00:06:17.460 --> 00:06:20.100
Now, because, again, we're attacking something on localhost,

143
00:06:20.280 --> 00:06:21.040
that was very quick.

144
00:06:21.260 --> 00:06:23.680
If it was a live web service, could

145
00:06:23.680 --> 00:06:25.640
be much slower, could even take hours to

146
00:06:25.640 --> 00:06:27.040
get 10,000 requests.

147
00:06:27.680 --> 00:06:28.960
Now, the first thing I'm going to check

148
00:06:28.960 --> 00:06:31.120
for is the status code, and if I

149
00:06:31.120 --> 00:06:33.300
feel so about this, we can see that

150
00:06:33.300 --> 00:06:35.700
we do indeed have a 200 response here.

151
00:06:36.060 --> 00:06:38.260
Something else to check is also the length,

152
00:06:38.440 --> 00:06:41.140
so sometimes, when you log in, you might

153
00:06:41.140 --> 00:06:43.560
always get a 200 response, but the length

154
00:06:43.560 --> 00:06:46.120
of the response might be different, so sometimes

155
00:06:46.120 --> 00:06:48.460
there will be subtle differences between the different

156
00:06:48.460 --> 00:06:51.860
headers or what's returned.

157
00:06:53.380 --> 00:06:55.540
So, in here, it's saying Ramirez, so I'm

158
00:06:55.540 --> 00:06:58.440
just going to copy this, verify it by

159
00:06:58.440 --> 00:07:01.020
coming back to the application and hitting paste,

160
00:07:01.860 --> 00:07:04.400
and then we get, hey, success, here's your

161
00:07:04.400 --> 00:07:07.640
flag, TCM, and a flag as well.

162
00:07:07.800 --> 00:07:10.460
So, if you're answering the questions later on,

163
00:07:10.640 --> 00:07:11.920
you'll need this flag.

164
00:07:13.220 --> 00:07:16.960
So, let's do the same with Fuff, so

165
00:07:16.960 --> 00:07:19.760
I'm just going to come back to here,

166
00:07:20.060 --> 00:07:22.420
and, actually, we're going to start off in

167
00:07:22.420 --> 00:07:24.060
the same way, in that I'm going to

168
00:07:24.060 --> 00:07:26.000
come to burp suite.

169
00:07:26.880 --> 00:07:29.080
I'm going to close this attack.

170
00:07:30.220 --> 00:07:34.140
Then proxy, HTTP history, and I'm going to

171
00:07:34.140 --> 00:07:36.000
take this request, so I'm going to hit

172
00:07:36.000 --> 00:07:39.620
control A to select all, control C to

173
00:07:39.620 --> 00:07:42.500
copy, and then I'm just going to come

174
00:07:42.500 --> 00:07:46.060
into CD temp, and then I'm just going

175
00:07:46.060 --> 00:07:49.840
to vim rec.txt. You can use nano

176
00:07:49.840 --> 00:07:53.240
or mousepad or whatever editor you prefer, so

177
00:07:53.240 --> 00:07:55.200
I like vim, and I'm going to come

178
00:07:55.200 --> 00:07:59.660
in and change this to fuzz, because we

179
00:07:59.660 --> 00:08:01.320
want to fuzz the password field.

180
00:08:01.320 --> 00:08:04.520
So, I'm just going to save that, and,

181
00:08:04.700 --> 00:08:06.020
like I say, if you want something a

182
00:08:06.020 --> 00:08:07.720
little bit easier to get up and running

183
00:08:07.720 --> 00:08:09.600
with, mousepad is a good starting one.

184
00:08:09.780 --> 00:08:14.740
It's basically like notepad, but for Kali or

185
00:08:14.740 --> 00:08:15.060
Linux.

186
00:08:16.040 --> 00:08:19.980
So, next, I'm just going to type FFUF,

187
00:08:20.140 --> 00:08:22.400
and I'm going to pass the request flag

188
00:08:23.140 --> 00:08:26.060
to rec.txt. You can call this request

189
00:08:26.060 --> 00:08:29.460
or my file or anything you want, and

190
00:08:29.460 --> 00:08:32.419
then I'm going to pass the word list

191
00:08:32.419 --> 00:08:38.380
as user share word lists, actually, sorry, seclists

192
00:08:38.380 --> 00:08:43.780
passwords, and then the same one as before,

193
00:08:44.020 --> 00:08:47.880
so zetotop10000, and then I'm going to put

194
00:08:47.880 --> 00:08:50.240
the MC as 200.

195
00:08:50.780 --> 00:08:53.480
I think we also need to pass the

196
00:08:53.480 --> 00:08:59.310
protocol type as well, which I'm going to

197
00:08:59.310 --> 00:09:01.910
put just here, so I don't think the

198
00:09:01.910 --> 00:09:06.350
order matters too much, but request proto HTTP.

199
00:09:06.910 --> 00:09:08.930
Now, from our early attack, I know we're

200
00:09:08.930 --> 00:09:11.610
actually looking for a 200, so let's take

201
00:09:11.610 --> 00:09:13.410
this off for a second and see what

202
00:09:13.410 --> 00:09:15.130
comes back, so I'm just going to cancel

203
00:09:15.130 --> 00:09:17.210
this quickly, and you can see we're getting

204
00:09:17.210 --> 00:09:20.190
a lot of 401s, so all of these

205
00:09:20.190 --> 00:09:23.510
are failed requests, and if we want to

206
00:09:23.510 --> 00:09:27.010
check for a 200, we can just put

207
00:09:27.950 --> 00:09:30.250
MC200, and it's only going to show us

208
00:09:30.250 --> 00:09:33.550
the 200 responses, and you can see very

209
00:09:33.550 --> 00:09:36.310
quickly that it found the password, and actually,

210
00:09:36.430 --> 00:09:38.270
that was a lot quicker than Burp Suite,

211
00:09:38.470 --> 00:09:42.270
so this tool obviously is very, very fast,

212
00:09:42.590 --> 00:09:44.890
so from that perspective, it might even be

213
00:09:44.890 --> 00:09:47.730
a better tool to use than Burp Suite

214
00:09:47.730 --> 00:09:50.270
Pro, for example, and it does have the

215
00:09:50.270 --> 00:09:53.210
ability, if you change the mode, so you

216
00:09:53.210 --> 00:09:56.690
can, for example, put mode, and you can

217
00:09:56.690 --> 00:10:00.190
do, I think it's clusterbomb, I wrote most

218
00:10:00.190 --> 00:10:03.030
instead of mode, and this will mimic similar

219
00:10:03.030 --> 00:10:06.770
functionality to here, where when we have clusterbomb,

220
00:10:06.990 --> 00:10:09.010
we will have two inputs, and it will

221
00:10:09.010 --> 00:10:10.610
brute force both of them, so it will

222
00:10:10.610 --> 00:10:13.250
be like admin, password 1, password 2, password

223
00:10:13.250 --> 00:10:16.250
3, admin 1, password 1, password 2, password

224
00:10:16.250 --> 00:10:19.010
3, admin 2, password 1, password 2, password

225
00:10:19.010 --> 00:10:20.850
3, for example, so it will go over

226
00:10:20.850 --> 00:10:23.730
all the iterations of those if you don't

227
00:10:23.730 --> 00:10:24.330
know either.

228
00:10:24.850 --> 00:10:27.390
Now, I tend to, in most cases, brute

229
00:10:27.390 --> 00:10:29.410
force one field at a time, that tends

230
00:10:29.410 --> 00:10:31.390
to work for me, but, you know, you

231
00:10:31.390 --> 00:10:33.450
can try different things and see what happens

232
00:10:33.450 --> 00:10:34.690
with your workflow.

233
00:10:35.830 --> 00:10:38.790
So, this is a relatively simple scenario, and

234
00:10:38.790 --> 00:10:40.970
it's likely that you're going to be faced

235
00:10:40.970 --> 00:10:42.870
with challenges that will slow you down, such

236
00:10:42.870 --> 00:10:45.710
as rate limiting, such as tokens that you

237
00:10:45.710 --> 00:10:47.090
might need to pull out of the page

238
00:10:47.090 --> 00:10:49.950
and pass with requests, cross-site request forgery

239
00:10:49.950 --> 00:10:52.090
tokens, for example, you might need to include

240
00:10:52.090 --> 00:10:54.850
in your request, so I encourage you to

241
00:10:54.850 --> 00:10:56.450
learn a little bit more about brute force

242
00:10:56.450 --> 00:10:59.870
attacks generally, as these techniques will transfer nicely

243
00:10:59.870 --> 00:11:03.550
to your API penetration testing skills.

244
00:11:04.330 --> 00:11:06.230
Now, I have a little challenge for you.

245
00:11:06.550 --> 00:11:07.930
It's in the same lab.

246
00:11:08.350 --> 00:11:11.450
Now, there is another user that exists within

247
00:11:11.450 --> 00:11:14.230
this application, and so my challenge to you

248
00:11:14.230 --> 00:11:16.730
is to find out their username and then

249
00:11:16.730 --> 00:11:19.610
find out their password and retrieve the flag,

250
00:11:19.850 --> 00:11:22.510
similar to we did, as we did for

251
00:11:22.510 --> 00:11:25.690
the admin account, and yeah, spend a bit

252
00:11:25.690 --> 00:11:27.690
of time on that challenge, and as usual,

253
00:11:27.790 --> 00:11:29.990
we'll go through a walkthrough together in the

254
00:11:29.990 --> 00:11:31.330
final video of this section.

255
00:11:31.790 --> 00:11:32.830
That's it for now.

256
00:11:33.030 --> 00:11:33.910
I'll see you in the next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.410 --> 00:00:03.530
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Aside from attacking authentication mechanisms, we can also

2
00:00:03.530 --> 00:00:05.230
attack tokens themselves.

3
00:00:05.630 --> 00:00:07.930
This is to try and change our identity.

4
00:00:08.670 --> 00:00:11.330
For example, instead of being Jeremy the user,

5
00:00:11.630 --> 00:00:13.690
we might want to be Jessamy the admin.

6
00:00:14.390 --> 00:00:17.250
One of the requirements of REST APIs is

7
00:00:17.250 --> 00:00:18.030
statelessness.

8
00:00:18.330 --> 00:00:20.970
So, this means that with each request, something

9
00:00:20.970 --> 00:00:23.810
needs to be sent to identify who actually

10
00:00:23.810 --> 00:00:24.730
sent the request.

11
00:00:25.410 --> 00:00:27.830
And usually, that's a token, such as a

12
00:00:27.830 --> 00:00:30.050
session ID or JSON web token.

13
00:00:30.790 --> 00:00:33.610
Now, we'll look into attacking JWTs a little

14
00:00:33.610 --> 00:00:35.090
bit later on in the next video.

15
00:00:35.450 --> 00:00:37.290
But for now, let's take a look at

16
00:00:37.290 --> 00:00:39.130
how we can analyze tokens to get a

17
00:00:39.130 --> 00:00:41.630
better understanding of how random or secure they

18
00:00:41.630 --> 00:00:41.870
are.

19
00:00:43.130 --> 00:00:43.610
All right.

20
00:00:43.730 --> 00:00:45.670
So, if I just come into my labs

21
00:00:45.670 --> 00:00:47.870
folder, you can see that I have the

22
00:00:47.870 --> 00:00:50.610
API token analysis.zip. So, I'm just going

23
00:00:50.610 --> 00:00:53.110
to come in and unzip this.

24
00:00:55.230 --> 00:00:56.030
Clear my screen.

25
00:00:56.730 --> 00:01:00.410
And then CD it into API token analysis.

26
00:01:01.310 --> 00:01:02.990
So, we can see that there's some Docker

27
00:01:02.990 --> 00:01:03.370
files.

28
00:01:03.629 --> 00:01:07.030
So, I'll just sudo docker compose build.

29
00:01:08.490 --> 00:01:10.190
Looks like we're all good.

30
00:01:10.910 --> 00:01:14.150
And then sudo docker compose up.

31
00:01:15.730 --> 00:01:17.050
And while I was doing that, I'm also

32
00:01:17.050 --> 00:01:18.650
going to open up web suite.

33
00:01:18.950 --> 00:01:20.390
So, community edition is fine.

34
00:01:20.610 --> 00:01:22.510
Because we're just going to use the sequencer

35
00:01:22.510 --> 00:01:23.530
for our analysis.

36
00:01:26.800 --> 00:01:28.780
And then I'm also going to open up,

37
00:01:28.800 --> 00:01:31.660
whoops, Firefox as well.

38
00:01:32.480 --> 00:01:34.180
We get a little bit of a message,

39
00:01:34.320 --> 00:01:35.520
but we'll just click okay for now.

40
00:01:36.040 --> 00:01:39.620
And then we can browse to localhost 9000.

41
00:01:41.180 --> 00:01:43.020
So, if I just come in and hit

42
00:01:43.020 --> 00:01:45.900
login, and the username and password is the

43
00:01:45.900 --> 00:01:47.020
same as the last lab.

44
00:01:47.160 --> 00:01:49.700
So, the password is Ramirez.

45
00:01:49.980 --> 00:01:52.540
So, I just cut that, paste it in

46
00:01:52.540 --> 00:01:54.340
here, and click login.

47
00:01:54.720 --> 00:01:56.320
Now, before we do this, I'm just going

48
00:01:56.320 --> 00:01:57.560
to have a quick look to see whether

49
00:01:57.560 --> 00:01:59.240
I have any cookies set, which I don't.

50
00:01:59.360 --> 00:02:00.480
So, this is my cookie editor.

51
00:02:00.980 --> 00:02:02.740
And you can also do this in the

52
00:02:02.740 --> 00:02:03.680
console as well.

53
00:02:03.920 --> 00:02:07.160
So, we can just type document.cookie to

54
00:02:07.160 --> 00:02:09.580
verify that we have indeed no cookies.

55
00:02:09.780 --> 00:02:11.060
So, if you have some cookies set from

56
00:02:11.060 --> 00:02:13.880
the previous lab, then you can clear them

57
00:02:13.880 --> 00:02:14.300
out.

58
00:02:15.080 --> 00:02:16.740
So, yeah, back to the login.

59
00:02:16.920 --> 00:02:18.720
Admin Ramirez.

60
00:02:19.160 --> 00:02:20.440
And I hit login.

61
00:02:21.140 --> 00:02:23.300
And you see that we get this message

62
00:02:23.300 --> 00:02:26.320
that says you have successfully logged in.

63
00:02:27.040 --> 00:02:30.000
And if we click okay, we can then

64
00:02:30.000 --> 00:02:31.880
come back up to our cookie editor, and

65
00:02:31.880 --> 00:02:33.400
we can see that we have an access

66
00:02:33.400 --> 00:02:37.080
token, and we get a welcome admin as

67
00:02:37.080 --> 00:02:37.320
well.

68
00:02:37.920 --> 00:02:39.020
And same in the console.

69
00:02:40.280 --> 00:02:44.740
Document.cookie. We have access equals, and this

70
00:02:44.740 --> 00:02:46.400
is indeed our cookie.

71
00:02:46.720 --> 00:02:49.120
So, next up is to come over to

72
00:02:49.120 --> 00:02:51.260
Burp Suite, and we're just going to come

73
00:02:51.260 --> 00:02:54.180
over to proxy, HTTP history, and then we're

74
00:02:54.180 --> 00:02:56.240
going to come down and get the post

75
00:02:56.240 --> 00:02:59.680
request that was sent to get our cookie.

76
00:03:00.440 --> 00:03:02.680
So, let me just move myself out of

77
00:03:02.680 --> 00:03:02.940
the way.

78
00:03:03.720 --> 00:03:05.280
And you can see that we sent the

79
00:03:05.280 --> 00:03:08.860
email and password, and we got a token

80
00:03:08.860 --> 00:03:10.080
back in the response.

81
00:03:10.400 --> 00:03:12.660
And this is what we need for Sequencer.

82
00:03:13.140 --> 00:03:16.280
So, whenever you find an endpoint that returns

83
00:03:16.280 --> 00:03:18.860
a token to you, you can use this

84
00:03:18.860 --> 00:03:21.720
for the Sequencer, or for this attack or

85
00:03:21.720 --> 00:03:22.140
analysis.

86
00:03:22.940 --> 00:03:24.520
So, I'm just going to right click on

87
00:03:24.520 --> 00:03:28.620
the request, send to Sequencer, click on Sequencer,

88
00:03:29.200 --> 00:03:31.620
and before we start the live capture, we

89
00:03:31.620 --> 00:03:33.680
actually need to tell it where to find

90
00:03:33.680 --> 00:03:34.140
the token.

91
00:03:34.660 --> 00:03:37.920
So, we just hit configure, and then we

92
00:03:37.920 --> 00:03:40.380
can highlight the token in here, and you

93
00:03:40.380 --> 00:03:42.980
can see that it automatically says, hey, the

94
00:03:42.980 --> 00:03:46.200
start of the token begins with quotes, token,

95
00:03:46.400 --> 00:03:49.880
quote, colon, quote, and anything between this and

96
00:03:49.880 --> 00:03:54.500
the end, which is quotes, close braces, is

97
00:03:54.500 --> 00:03:55.180
our token.

98
00:03:55.320 --> 00:03:57.580
So, it knows how to basically grep for

99
00:03:57.580 --> 00:03:59.700
the token on each request.

100
00:04:00.220 --> 00:04:01.440
And then all we need to do is

101
00:04:01.440 --> 00:04:02.140
start live capture.

102
00:04:02.220 --> 00:04:03.420
Now, if you're doing this against a live

103
00:04:03.420 --> 00:04:05.160
website, this is going to send thousands and

104
00:04:05.160 --> 00:04:06.080
thousands of requests.

105
00:04:06.500 --> 00:04:08.560
So, make sure you're authorized to do it,

106
00:04:08.640 --> 00:04:10.380
and make sure that, you know, if it's

107
00:04:10.380 --> 00:04:12.740
against a production system, it can stand up

108
00:04:12.740 --> 00:04:14.420
to this kind of brute force.

109
00:04:15.680 --> 00:04:17.420
So, obviously, we're doing a local host, so

110
00:04:17.420 --> 00:04:18.540
it's going to be really fast.

111
00:04:18.880 --> 00:04:21.060
Again, a live host could take an hour

112
00:04:21.060 --> 00:04:23.920
to get through this many requests, could take

113
00:04:23.920 --> 00:04:24.860
shorter, longer.

114
00:04:25.280 --> 00:04:26.180
There are many variables.

115
00:04:27.280 --> 00:04:30.440
So, 20,000 tokens, it's collected, and we

116
00:04:30.440 --> 00:04:33.240
can click analyze now, and you can see

117
00:04:33.240 --> 00:04:35.020
it gives us some results.

118
00:04:35.260 --> 00:04:37.260
So, it says the overall quality of randomness

119
00:04:37.260 --> 00:04:40.500
within this sample is estimated to be extremely

120
00:04:40.500 --> 00:04:40.900
poor.

121
00:04:41.540 --> 00:04:44.340
So, this is grounds for further inspection or

122
00:04:44.340 --> 00:04:45.340
further analysis.

123
00:04:45.760 --> 00:04:48.120
If you saw that the quality of randomness

124
00:04:48.120 --> 00:04:51.320
was incredibly amazing, you'd be like, this is

125
00:04:51.320 --> 00:04:53.520
probably not an attack vector, unless there is

126
00:04:53.520 --> 00:04:55.260
something that you know about the token that

127
00:04:55.260 --> 00:04:57.740
maybe is overlooked by this tool.

128
00:04:58.620 --> 00:05:00.940
So, if we come to character analysis, now,

129
00:05:01.020 --> 00:05:03.860
this is quite interesting, because I actually know

130
00:05:03.860 --> 00:05:06.100
how this token is created, and I know

131
00:05:06.100 --> 00:05:08.420
how it's formed, because I wrote the code

132
00:05:08.420 --> 00:05:09.000
that did it.

133
00:05:09.980 --> 00:05:13.760
And this is not an accurate representation of

134
00:05:13.760 --> 00:05:15.740
the token, and this is a trap that

135
00:05:15.740 --> 00:05:17.920
I've seen a few people fall into before.

136
00:05:18.640 --> 00:05:20.940
The token we get back, if we inspect

137
00:05:20.940 --> 00:05:22.400
it, or if we look at it a

138
00:05:22.400 --> 00:05:26.640
little bit more closely, you might think, ah,

139
00:05:26.900 --> 00:05:29.700
looks like base 64, you know, and sometimes,

140
00:05:29.700 --> 00:05:31.800
if the padding is wrong, you'll have equals

141
00:05:31.800 --> 00:05:32.280
on the end.

142
00:05:33.060 --> 00:05:36.240
If we copy this, and just open up

143
00:05:38.680 --> 00:05:43.860
a new terminal page, and just echo-n

144
00:05:43.860 --> 00:05:49.780
this to base 64-d, you'll see that,

145
00:05:49.880 --> 00:05:51.520
yeah, it is indeed base 64.

146
00:05:52.160 --> 00:05:54.740
And interesting that, you know, we can come

147
00:05:54.740 --> 00:05:56.500
in and start to make some guesses as

148
00:05:56.500 --> 00:05:57.200
to what this is.

149
00:05:57.200 --> 00:05:59.620
Another way to do this is simply, if

150
00:05:59.620 --> 00:06:04.340
we head over to web suite, decoder, decode

151
00:06:04.340 --> 00:06:07.200
as base 64, and if you think it's,

152
00:06:07.280 --> 00:06:09.040
if you're doing a CTF, or if you

153
00:06:09.040 --> 00:06:11.700
think it's something, like, completely strange, if you

154
00:06:11.700 --> 00:06:15.660
just come to Google, and then CyberChef, I

155
00:06:15.660 --> 00:06:18.600
think it's CyberChef.io, yeah, this is the

156
00:06:18.600 --> 00:06:23.320
one, you can paste it in here, and,

157
00:06:23.520 --> 00:06:25.600
you know, if you search for base, you've

158
00:06:25.600 --> 00:06:28.640
got, like, from base 32, for example, from

159
00:06:28.640 --> 00:06:31.360
base 45, and combinations of them, so you

160
00:06:31.360 --> 00:06:34.620
can really dive deep into the string from

161
00:06:34.620 --> 00:06:34.920
here.

162
00:06:35.260 --> 00:06:37.640
But in most cases, it will be base

163
00:06:37.640 --> 00:06:38.080
64.

164
00:06:38.240 --> 00:06:40.000
Now, there's an easy way to combat this.

165
00:06:40.720 --> 00:06:44.860
Analysis options, base 64 decode string before analyzing,

166
00:06:45.140 --> 00:06:46.740
and then we can come back and hit

167
00:06:46.740 --> 00:06:47.680
analyze now.

168
00:06:48.520 --> 00:06:51.480
Now, if we save the tokens, let's say

169
00:06:51.480 --> 00:06:53.680
it's base 32 encoded, we could save the

170
00:06:53.680 --> 00:06:56.700
tokens, decode them, and then just load them

171
00:06:56.700 --> 00:06:59.460
in, and analyze them that way, so if

172
00:06:59.460 --> 00:07:00.920
we have a set of tokens, we can

173
00:07:00.920 --> 00:07:04.000
still use the sequencer, but often we just

174
00:07:04.000 --> 00:07:05.920
do a quick base 64 decode, and we're

175
00:07:05.920 --> 00:07:06.420
good to go.

176
00:07:07.020 --> 00:07:09.580
And now this is the analysis that I

177
00:07:09.580 --> 00:07:10.220
was expecting.

178
00:07:10.680 --> 00:07:13.640
So there's very little randomness between characters 0

179
00:07:13.640 --> 00:07:17.000
through 14, and a lot of randomness between

180
00:07:17.000 --> 00:07:18.440
15, 16, and 17.

181
00:07:19.120 --> 00:07:22.020
So this is really weak, because it just

182
00:07:22.020 --> 00:07:25.060
means that, in terms of our attack, instead

183
00:07:25.060 --> 00:07:28.200
of trying to brute force 17, 18 characters,

184
00:07:28.620 --> 00:07:30.700
we only need to brute force the last

185
00:07:30.700 --> 00:07:31.580
three characters.

186
00:07:31.840 --> 00:07:34.740
And looking at the token itself, it looks

187
00:07:34.740 --> 00:07:36.960
like the first five characters are the username,

188
00:07:37.380 --> 00:07:40.160
so it's likely that our token, when we're

189
00:07:40.160 --> 00:07:43.580
trying to brute force, will be Jeremy.

190
00:07:44.640 --> 00:07:46.680
And having a look at this, this looks

191
00:07:46.680 --> 00:07:48.640
like a time date stamp, so this looks

192
00:07:48.640 --> 00:07:51.140
like hours, minutes, and seconds.

193
00:07:52.200 --> 00:07:54.160
And I suspect what we can do is,

194
00:07:54.240 --> 00:07:56.440
if we save the tokens, and we save

195
00:07:56.440 --> 00:08:00.800
it to somewhere normal, let's just go into

196
00:08:00.800 --> 00:08:04.780
temp, and I save it as tokens.txt,

197
00:08:05.740 --> 00:08:10.600
and I come back, and let's just head

198
00:08:10.600 --> 00:08:12.960
-n the top 100.

199
00:08:13.180 --> 00:08:14.060
We're in the wrong place.

200
00:08:14.740 --> 00:08:20.280
Let's cd temp head-n 100.

201
00:08:20.660 --> 00:08:21.620
Oops, that's 1000.

202
00:08:24.040 --> 00:08:32.419
Tokens.txt. We can see that, obviously, the

203
00:08:32.419 --> 00:08:35.260
first part of the token is the same

204
00:08:35.260 --> 00:08:38.419
every time, and then the end is slightly

205
00:08:38.419 --> 00:08:41.760
different, and this is from the base64.

206
00:08:42.020 --> 00:08:44.280
Obviously, we want to see this decoded, so

207
00:08:44.280 --> 00:08:45.980
again, there's a few ways to do this.

208
00:08:48.180 --> 00:08:50.140
So I'm just going to copy and paste,

209
00:08:50.500 --> 00:08:54.400
and then come back to bubsuite, and come

210
00:08:54.400 --> 00:08:56.860
to decoder, paste it in, and you can

211
00:08:56.860 --> 00:09:00.520
see, indeed, that we have three lowercase characters

212
00:09:00.520 --> 00:09:02.740
at the end of every token.

213
00:09:04.140 --> 00:09:06.680
And if I come back, and let's say

214
00:09:06.680 --> 00:09:14.700
I grab tail, let's say 10 of tokens

215
00:09:14.700 --> 00:09:18.460
.txt, I want to grab the last few

216
00:09:18.460 --> 00:09:21.020
and compare them to basically the first few,

217
00:09:21.200 --> 00:09:25.620
so if I just come here, and remove

218
00:09:25.620 --> 00:09:28.240
a bunch of these, and paste in here,

219
00:09:28.940 --> 00:09:31.120
you can see the timestamp changes.

220
00:09:31.440 --> 00:09:32.960
Now, apologies if the text is a little

221
00:09:32.960 --> 00:09:35.000
bit small, but we've got 10.38.15

222
00:09:35.000 --> 00:09:38.000
and 10.38.21, so this looks like

223
00:09:38.000 --> 00:09:41.800
the seconds that are ticking up, but obviously,

224
00:09:42.000 --> 00:09:44.500
because our requests were very fast, we got

225
00:09:44.500 --> 00:09:46.420
quite a lot of tokens for each second

226
00:09:46.420 --> 00:09:47.080
that passed.

227
00:09:48.000 --> 00:09:51.240
All right, so, now we know that the

228
00:09:51.240 --> 00:09:54.080
start of the token is the username, the

229
00:09:54.080 --> 00:09:57.400
middle of the token is the timestamp, and

230
00:09:57.400 --> 00:09:59.340
the end of the token is three random

231
00:09:59.340 --> 00:09:59.960
characters.

232
00:10:00.440 --> 00:10:01.720
I have a challenge for you.

233
00:10:02.320 --> 00:10:05.140
Now, because this lab is created for learning

234
00:10:05.140 --> 00:10:07.580
purposes, I made it so that when the

235
00:10:07.580 --> 00:10:10.280
admin logs in, Jeremy also logs in.

236
00:10:10.700 --> 00:10:12.740
So, you can use that information to figure

237
00:10:12.740 --> 00:10:15.740
out the timestamp, or a very rough time

238
00:10:15.740 --> 00:10:17.760
of when Jeremy's about to log in.

239
00:10:18.340 --> 00:10:20.200
Obviously, if this was a real situation, and

240
00:10:20.200 --> 00:10:23.420
the token was created by a timestamp, we'd

241
00:10:23.420 --> 00:10:25.840
have to find other ways to figure out

242
00:10:25.840 --> 00:10:26.940
when the user logged in.

243
00:10:27.120 --> 00:10:28.900
Maybe on their profile, it gives them a

244
00:10:28.900 --> 00:10:31.940
last online time, or maybe we just need

245
00:10:31.940 --> 00:10:34.780
to create a much wider array of tokens

246
00:10:34.780 --> 00:10:36.340
so that we cover, you know, a few

247
00:10:36.340 --> 00:10:38.440
hours of the day when a user is

248
00:10:38.440 --> 00:10:39.360
likely to log in.

249
00:10:39.580 --> 00:10:40.940
It's very situational.

250
00:10:41.620 --> 00:10:43.760
But one last thing, don't forget that we

251
00:10:43.760 --> 00:10:45.300
learned how to brute force a couple of

252
00:10:45.300 --> 00:10:47.840
videos ago, so obviously, you'll need to utilize

253
00:10:47.840 --> 00:10:48.960
those skills here.

254
00:10:49.520 --> 00:10:52.180
And as usual, we'll walk through the challenge

255
00:10:52.180 --> 00:10:53.940
together at the end of the section.

256
00:10:54.520 --> 00:10:56.760
So, see if you can have a play

257
00:10:56.760 --> 00:10:59.500
with the token, decode it, understand how it's

258
00:10:59.500 --> 00:11:02.300
built, generate a bunch of tokens that you

259
00:11:02.300 --> 00:11:04.520
think might be legitimate for the user Jeremy,

260
00:11:05.040 --> 00:11:07.200
and then try and brute force the application

261
00:11:07.200 --> 00:11:09.100
to log in as Jeremy.

262
00:11:09.360 --> 00:11:12.140
And once you have the right token, and

263
00:11:12.140 --> 00:11:15.020
refresh the homepage, if I can find it,

264
00:11:15.320 --> 00:11:18.000
you should have a welcome message that says,

265
00:11:18.000 --> 00:11:19.020
welcome Jeremy.

266
00:11:19.480 --> 00:11:21.940
So, have a go at that, and I'll

267
00:11:21.940 --> 00:11:22.800
catch you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.380 --> 00:00:02.700
(Transcribed by TurboScribe. Go Unlimited to remove this message.) If you're working with web applications, it's likely

2
00:00:02.700 --> 00:00:05.580
that you've run into JSON Web Tokens, also

3
00:00:05.580 --> 00:00:07.220
known as JWTs.

4
00:00:07.520 --> 00:00:10.040
They're widely used with APIs and a great

5
00:00:10.040 --> 00:00:12.480
solution if you need a token that's flexible

6
00:00:12.480 --> 00:00:13.280
and secure.

7
00:00:13.940 --> 00:00:16.320
Although, as with most things, only if they're

8
00:00:16.320 --> 00:00:17.300
implemented securely.

9
00:00:17.880 --> 00:00:19.180
We're going to take a look at what

10
00:00:19.180 --> 00:00:21.600
JSON Web Tokens look like and some of

11
00:00:21.600 --> 00:00:23.920
the common attacks we can employ against them.

12
00:00:24.640 --> 00:00:26.240
After that, I'm going to give you some

13
00:00:26.240 --> 00:00:28.460
great free resources to further your study.

14
00:00:29.120 --> 00:00:30.760
So, let's dive in and take a look

15
00:00:30.760 --> 00:00:33.160
at what JWTs actually look like.

16
00:00:34.000 --> 00:00:35.060
There are three parts.

17
00:00:35.380 --> 00:00:37.380
The header, the payload, and the signature.

18
00:00:38.180 --> 00:00:41.480
Each part is encoded with base64 and separated

19
00:00:41.480 --> 00:00:42.400
by a full stop.

20
00:00:43.020 --> 00:00:45.700
Now, we can easily decode each piece to

21
00:00:45.700 --> 00:00:48.000
see the contents, but there is also a

22
00:00:48.000 --> 00:00:50.360
great tool that we can use at JWT

23
00:00:50.360 --> 00:00:51.880
.io to do this as well.

24
00:00:53.040 --> 00:00:55.220
When we take a closer look, we can

25
00:00:55.220 --> 00:00:57.560
see that the header contains some metadata about

26
00:00:57.560 --> 00:00:58.040
the token.

27
00:00:58.760 --> 00:01:01.340
The payload contains what we call claims, and

28
00:01:01.340 --> 00:01:03.420
these are pieces of information that we want

29
00:01:03.420 --> 00:01:05.460
to store about the bearer of the token

30
00:01:05.460 --> 00:01:07.640
or the person who supplied it.

31
00:01:08.560 --> 00:01:10.460
For example, we might want to store their

32
00:01:10.460 --> 00:01:11.160
username here.

33
00:01:12.340 --> 00:01:15.360
Now, the signature contains just that, a signature.

34
00:01:16.020 --> 00:01:17.220
Now, there are a bunch of different ways

35
00:01:17.220 --> 00:01:20.300
to sign a JWT, a JSON Web Token.

36
00:01:20.800 --> 00:01:23.420
For example, we can use symmetric encryption with

37
00:01:23.420 --> 00:01:26.240
just one secret to sign and verify, or

38
00:01:26.240 --> 00:01:28.900
we can use asymmetric encryption, so we can

39
00:01:28.900 --> 00:01:30.920
sign with a private key and then use

40
00:01:30.920 --> 00:01:32.880
a public key to verify it.

41
00:01:33.860 --> 00:01:35.960
One last thing to note is that when

42
00:01:35.960 --> 00:01:38.600
we're transferring JWTs, we send them via the

43
00:01:38.600 --> 00:01:39.660
authorization header.

44
00:01:40.380 --> 00:01:44.080
So, this will look like authorization, colon, bearer,

45
00:01:44.360 --> 00:01:45.580
and then the token value.

46
00:01:46.340 --> 00:01:49.100
Before we dive into attacking the tokens, let's

47
00:01:49.100 --> 00:01:50.620
take a quick look at what happens when

48
00:01:50.620 --> 00:01:53.540
we try to tamper with a signed token.

49
00:01:54.500 --> 00:01:56.920
So, I'm just going to quickly spin up

50
00:01:56.920 --> 00:01:59.980
the web server for the example.

51
00:02:00.660 --> 00:02:05.960
So, cd dev JWT demo and node server

52
00:02:05.960 --> 00:02:10.320
.js. So, here, I have a small web

53
00:02:10.320 --> 00:02:14.020
application that will basically issue and read JSON

54
00:02:14.020 --> 00:02:14.640
Web Tokens.

55
00:02:15.440 --> 00:02:17.300
So, I'm just going to make a request

56
00:02:17.300 --> 00:02:21.000
to the server, so curl post to the

57
00:02:21.000 --> 00:02:23.640
slash login end points, and you can see

58
00:02:23.640 --> 00:02:26.560
we're providing JSON, and the username is user,

59
00:02:26.560 --> 00:02:29.080
and the password is user in this case.

60
00:02:29.900 --> 00:02:32.020
And we get back a valid token.

61
00:02:32.780 --> 00:02:35.580
If we pass the wrong username and password,

62
00:02:35.760 --> 00:02:38.140
we get username and password you provided are

63
00:02:38.140 --> 00:02:38.600
invalid.

64
00:02:39.920 --> 00:02:41.900
So, what I want to do is quickly

65
00:02:41.900 --> 00:02:43.980
test this token, so I'm going to access

66
00:02:43.980 --> 00:02:47.780
the dashboard by making a get request to

67
00:02:47.780 --> 00:02:50.760
slash dashboard, and then I'm going to send

68
00:02:50.760 --> 00:02:55.400
the token that was provided previously from the

69
00:02:55.400 --> 00:03:00.030
login, and we get welcome to your dashboard

70
00:03:00.030 --> 00:03:00.690
user.

71
00:03:01.310 --> 00:03:03.690
Now, if I change this token or break

72
00:03:03.690 --> 00:03:04.890
it in some way, so I'm just going

73
00:03:04.890 --> 00:03:07.750
to quickly remove a character, and send this,

74
00:03:08.030 --> 00:03:10.510
you'll see that we get JSON Web Token

75
00:03:10.510 --> 00:03:12.270
error, invalid signature.

76
00:03:13.010 --> 00:03:15.570
So, let's take a quick look.

77
00:03:15.570 --> 00:03:18.130
Let's take a closer look at this token

78
00:03:18.130 --> 00:03:24.160
in JWT.io. So, what I do is

79
00:03:24.160 --> 00:03:27.460
I come to JWT.io, paste in the

80
00:03:27.460 --> 00:03:30.400
signature, and then you can see that the

81
00:03:30.400 --> 00:03:34.560
algorithm type is HS256, and the type is

82
00:03:34.560 --> 00:03:36.360
JWT, so this is our header.

83
00:03:36.940 --> 00:03:38.700
You can see that in the payload section,

84
00:03:38.820 --> 00:03:41.200
we have a user ID of user, and

85
00:03:41.200 --> 00:03:42.860
we have an issued at time, and this

86
00:03:42.860 --> 00:03:44.820
is the timestamp for the token for when

87
00:03:44.820 --> 00:03:45.400
it was issued.

88
00:03:46.380 --> 00:03:49.340
Often, you'll see things like expiry, and maybe

89
00:03:49.340 --> 00:03:51.540
some user properties, and some other things in

90
00:03:51.540 --> 00:03:52.180
here as well.

91
00:03:53.040 --> 00:03:55.820
And here, we have the signature in the

92
00:03:55.820 --> 00:03:56.580
last section.

93
00:03:57.380 --> 00:04:00.260
Now, if we don't know the secrets, we

94
00:04:00.260 --> 00:04:03.920
can sign this with anything, like I don't

95
00:04:03.920 --> 00:04:05.940
know 123, and you can see that the

96
00:04:05.940 --> 00:04:06.820
signature changes.

97
00:04:07.800 --> 00:04:09.980
So, what I actually want to do is

98
00:04:09.980 --> 00:04:13.120
I want, instead of being the user, I

99
00:04:13.120 --> 00:04:14.640
want to be the admin.

100
00:04:15.300 --> 00:04:17.000
So, I'm just going to update this token.

101
00:04:18.440 --> 00:04:19.060
Copy it.

102
00:04:19.920 --> 00:04:20.820
Come back to here.

103
00:04:21.280 --> 00:04:23.560
Let me just clear this so you can

104
00:04:23.560 --> 00:04:24.360
see a little bit better.

105
00:04:25.380 --> 00:04:27.520
And then I'm going to paste this token

106
00:04:27.520 --> 00:04:27.900
in.

107
00:04:28.140 --> 00:04:31.680
So, if the signature is not verified, then

108
00:04:31.680 --> 00:04:34.160
this should just return a message saying, hey,

109
00:04:34.240 --> 00:04:36.480
welcome to your dashboard admin, as it did

110
00:04:36.480 --> 00:04:37.260
with the user.

111
00:04:38.160 --> 00:04:41.060
But, unfortunately, it seems like we actually have

112
00:04:41.060 --> 00:04:43.120
an invalid signature, so we need to know

113
00:04:43.120 --> 00:04:45.820
the secret before we can sign this.

114
00:04:46.060 --> 00:04:48.920
So, I know that the secret used for

115
00:04:48.920 --> 00:04:52.140
this application is actually secret 123, and if

116
00:04:52.140 --> 00:04:54.900
I just do head dash n, it's probably

117
00:04:54.900 --> 00:04:58.020
within the top five lines of server.js,

118
00:04:58.460 --> 00:05:00.760
you can see that we have const secret,

119
00:05:01.160 --> 00:05:02.060
secret 123.

120
00:05:03.120 --> 00:05:05.280
So, obviously, usually, we wouldn't have access to

121
00:05:05.280 --> 00:05:06.860
this, but just so you can see how

122
00:05:06.860 --> 00:05:08.900
it works, if I come back in here,

123
00:05:09.180 --> 00:05:11.880
and I change the signature so that it's

124
00:05:11.880 --> 00:05:15.300
signed with secret 123, and then I copy

125
00:05:15.300 --> 00:05:19.340
this, and I send the same request, but

126
00:05:19.340 --> 00:05:22.780
with the updated token, we get welcome to

127
00:05:22.780 --> 00:05:24.340
your dashboard admin.

128
00:05:24.640 --> 00:05:27.240
So, you can see how the signature prevents

129
00:05:27.240 --> 00:05:29.680
tampering, but, of course, if you sign it

130
00:05:29.680 --> 00:05:34.140
with a weak secret, then, potentially, your token

131
00:05:34.140 --> 00:05:36.720
can be forged, or we can create new

132
00:05:36.720 --> 00:05:39.440
tokens as we please and sign them.

133
00:05:39.900 --> 00:05:41.500
What we're going to do is, in the

134
00:05:41.500 --> 00:05:43.360
next video, we'll look at how we can

135
00:05:43.360 --> 00:05:45.820
actually attack the token to try and extract

136
00:05:45.820 --> 00:05:48.060
a weak secret, and then we'll have a

137
00:05:48.060 --> 00:05:50.100
look at some other attacks after that in

138
00:05:50.100 --> 00:05:50.900
the following video.

139
00:05:51.300 --> 00:05:52.200
So, I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.220 --> 00:00:02.140
(Transcribed by TurboScribe. Go Unlimited to remove this message.) We know that sometimes the secret used for

2
00:00:02.140 --> 00:00:04.180
signing a JWT is weak.

3
00:00:04.640 --> 00:00:06.400
Coupled with the fact that we can perform

4
00:00:06.400 --> 00:00:09.000
this attack offline against just a single token

5
00:00:09.000 --> 00:00:11.220
makes it a really important test to carry

6
00:00:11.220 --> 00:00:11.540
out.

7
00:00:12.220 --> 00:00:13.940
Now of course if you have access to

8
00:00:13.940 --> 00:00:16.500
source code or are in direct contact with

9
00:00:16.500 --> 00:00:19.700
the developers of an application this is an

10
00:00:19.700 --> 00:00:22.420
easy thing to audit, but often we're attacking

11
00:00:22.420 --> 00:00:24.440
from the outside so we may not be

12
00:00:24.440 --> 00:00:27.400
privy to how the application creates and handles

13
00:00:27.400 --> 00:00:28.120
its secrets.

14
00:00:28.920 --> 00:00:31.820
You can use JWT tool to carry out

15
00:00:31.820 --> 00:00:33.800
this attack but Hashcat is a little bit

16
00:00:33.800 --> 00:00:35.040
more effective for cracking.

17
00:00:35.620 --> 00:00:37.720
We'll look more at JWT tool and its

18
00:00:37.720 --> 00:00:39.340
capabilities in the next video.

19
00:00:39.860 --> 00:00:42.180
Alright so we're just gonna quickly demo how

20
00:00:42.180 --> 00:00:45.080
we can use Hashcat to crack this token

21
00:00:45.080 --> 00:00:47.200
and extract this secret.

22
00:00:47.560 --> 00:00:50.040
So same as before I'm just going to

23
00:00:50.040 --> 00:00:52.200
send a post request to slash login.

24
00:00:52.720 --> 00:00:55.260
It's going to have some JSON data and

25
00:00:55.260 --> 00:00:57.700
the username is user and the password is

26
00:00:57.700 --> 00:01:00.040
user as well and this gives us a

27
00:01:00.040 --> 00:01:00.720
valid token.

28
00:01:01.220 --> 00:01:03.560
Of course your target application usually when you

29
00:01:03.560 --> 00:01:05.140
log in the response will have a token

30
00:01:05.140 --> 00:01:06.300
so you can just take it out of

31
00:01:06.300 --> 00:01:08.160
burp suite or take it from your cookies.

32
00:01:08.800 --> 00:01:09.900
You know there's lots of ways to get

33
00:01:09.900 --> 00:01:11.040
your hands on a token.

34
00:01:11.780 --> 00:01:14.420
So next up we just go hashcats and

35
00:01:14.420 --> 00:01:17.400
then oops I want the attack mode to

36
00:01:17.400 --> 00:01:19.400
be a dictionary attack so that's dash a

37
00:01:19.400 --> 00:01:19.740
zero.

38
00:01:20.060 --> 00:01:21.840
If you want to brute force that dictionary

39
00:01:21.840 --> 00:01:25.500
I think it's dash a three and then

40
00:01:25.500 --> 00:01:30.680
the mode is 16 500 for JWTs.

41
00:01:31.100 --> 00:01:32.580
So I'm just going to paste the token.

42
00:01:32.820 --> 00:01:33.980
Of course you could save this to a

43
00:01:33.980 --> 00:01:35.780
file and then just reference the file but

44
00:01:35.780 --> 00:01:37.080
I'm just going to paste it in for

45
00:01:37.080 --> 00:01:39.580
now and then I'm just going to use

46
00:01:39.580 --> 00:01:44.240
Rocky for this and then we can see

47
00:01:44.240 --> 00:01:46.160
it's loading up and it's done already.

48
00:01:46.280 --> 00:01:48.300
That was faster than I expected actually.

49
00:01:48.800 --> 00:01:50.280
So you can see the status is cracked.

50
00:01:50.560 --> 00:01:51.760
If it got through the whole word list

51
00:01:51.760 --> 00:01:53.360
and couldn't find it it would say exhausted

52
00:01:53.960 --> 00:01:55.880
and that might be an indication that you

53
00:01:55.880 --> 00:01:57.760
either need to use a different word list

54
00:01:57.760 --> 00:02:00.680
or more targeted word list or potentially switch

55
00:02:00.680 --> 00:02:02.560
to brute force mode and leave it running

56
00:02:02.560 --> 00:02:03.360
for a few hours.

57
00:02:04.420 --> 00:02:06.100
But you'll see that we don't actually see

58
00:02:06.100 --> 00:02:07.780
the password here so all we need to

59
00:02:07.780 --> 00:02:09.919
do is come back here dash dash show

60
00:02:09.919 --> 00:02:13.200
and then it will reveal to us the

61
00:02:13.200 --> 00:02:13.540
password.

62
00:02:13.680 --> 00:02:17.040
So very weak, six characters and the entropy

63
00:02:17.040 --> 00:02:18.180
is not very high.

64
00:02:18.400 --> 00:02:20.540
What I mean by entropy is the character

65
00:02:20.540 --> 00:02:23.000
set so here we only have lowercase characters

66
00:02:23.000 --> 00:02:23.760
and a number.

67
00:02:24.160 --> 00:02:26.260
If you have high entropy you might include

68
00:02:26.260 --> 00:02:29.220
uppercase characters, special characters, things like that.

69
00:02:29.520 --> 00:02:31.480
So what I'm going to do is I'm

70
00:02:31.480 --> 00:02:37.620
going to grab this token again and then

71
00:02:37.620 --> 00:02:41.280
we're going to come over to jwt.io

72
00:02:41.280 --> 00:02:43.780
and then the same as before we're going

73
00:02:43.780 --> 00:02:45.860
to use this as the secret.

74
00:02:46.200 --> 00:02:49.340
I'm just going to change this to admin,

75
00:02:50.760 --> 00:02:55.640
paste in the secret, copy this forged token

76
00:02:55.640 --> 00:02:58.360
and then I'm just going to make a

77
00:02:58.360 --> 00:03:01.520
request to the dashboard with my new token.

78
00:03:04.580 --> 00:03:12.920
So curl tack i http localhost dashboard and

79
00:03:12.920 --> 00:03:14.480
then we just want to pass the header

80
00:03:17.760 --> 00:03:21.260
authorization bearer and then we post in our

81
00:03:21.260 --> 00:03:21.740
token.

82
00:03:23.400 --> 00:03:25.880
And we have welcome to your dashboard admin

83
00:03:25.880 --> 00:03:29.920
and that's it so obviously if a JWT

84
00:03:29.920 --> 00:03:33.300
is signed with a weak key we can

85
00:03:33.300 --> 00:03:36.180
crack it and then forge our own tokens

86
00:03:36.180 --> 00:03:38.880
as we've seen a couple of times.

87
00:03:39.060 --> 00:03:40.680
In the next video we'll look at some

88
00:03:40.680 --> 00:03:43.540
other misconfigurations and how we can identify them

89
00:03:43.540 --> 00:03:46.380
with JWT tool and then we will walk

90
00:03:46.380 --> 00:03:48.060
through some of the challenges that we've had

91
00:03:48.060 --> 00:03:49.500
so far in this module.

92
00:03:50.260 --> 00:03:50.960
I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.360 --> 00:00:03.700
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, let's get started with JWT tools.

2
00:00:04.000 --> 00:00:05.980
So if you don't have it already installed,

3
00:00:06.140 --> 00:00:08.980
you can come over to the GitHub repository

4
00:00:09.680 --> 00:00:12.100
and I already have this open, but if

5
00:00:12.100 --> 00:00:14.940
you're on the homepage of the GitHub repo,

6
00:00:15.460 --> 00:00:18.400
you can come down to setup.txt and

7
00:00:18.400 --> 00:00:21.420
there are some setup instructions here ready to

8
00:00:21.420 --> 00:00:22.940
go that will get you up and running.

9
00:00:23.400 --> 00:00:25.720
Now with my setup, I just added one

10
00:00:25.720 --> 00:00:27.300
more extra command.

11
00:00:27.300 --> 00:00:30.980
I put a link between the opt-jwt

12
00:00:30.980 --> 00:00:35.040
-jwt-tool.py, which is the tool itself,

13
00:00:35.240 --> 00:00:37.820
and I just created a link in this

14
00:00:37.820 --> 00:00:39.880
directory, which is in my path.

15
00:00:40.060 --> 00:00:43.740
So I can access this JWT tool directly

16
00:00:43.740 --> 00:00:46.100
with JWT tool rather than having to go

17
00:00:46.100 --> 00:00:50.760
slash opt-slash-jwt-tool or jwt-tool

18
00:00:50.760 --> 00:00:52.140
.py, for example.

19
00:00:52.400 --> 00:00:54.820
So feel free to set up your environment

20
00:00:54.820 --> 00:00:56.100
however you want.

21
00:00:57.300 --> 00:00:59.480
So if we just type JWT tool and

22
00:00:59.480 --> 00:01:03.200
hit enter, we get the usage information, which

23
00:01:03.200 --> 00:01:04.319
is super helpful.

24
00:01:04.700 --> 00:01:07.700
And if we just, to begin with, grab

25
00:01:07.700 --> 00:01:09.860
a token and pass it in, it's gonna

26
00:01:09.860 --> 00:01:11.480
give us some information about it.

27
00:01:11.560 --> 00:01:13.320
So for this demo, I think what we're

28
00:01:13.320 --> 00:01:17.940
gonna do is we're gonna take a look

29
00:01:17.940 --> 00:01:21.820
at our friend crappy and then I'm just

30
00:01:21.820 --> 00:01:27.200
gonna log in quickly and I'm just gonna

31
00:01:27.200 --> 00:01:29.660
open up Bep Suite as well so that

32
00:01:29.660 --> 00:01:32.720
I can capture the token, although you could

33
00:01:32.720 --> 00:01:34.540
grab it from the developer tools.

34
00:01:35.560 --> 00:01:37.920
I'm just gonna hit next, start Bep Suite,

35
00:01:42.160 --> 00:01:47.020
and hit okay and proxy HTTP history.

36
00:01:47.560 --> 00:01:50.520
And I'm gonna come back and switch on

37
00:01:50.520 --> 00:01:53.820
my proxy and log in with any account

38
00:01:53.820 --> 00:01:54.600
that you've created.

39
00:01:54.920 --> 00:01:57.380
I'm just gonna use a.tcmsec.com that

40
00:01:57.380 --> 00:01:59.260
we created in a previous video.

41
00:02:00.200 --> 00:02:03.000
Click log in and yeah, our Lamborghini is

42
00:02:03.000 --> 00:02:04.060
back, which is nice.

43
00:02:04.880 --> 00:02:06.820
So I'm just gonna come back to here

44
00:02:07.160 --> 00:02:10.400
and have a look at the requests.

45
00:02:11.060 --> 00:02:13.540
So this is our initial post and then

46
00:02:13.540 --> 00:02:17.220
we've also got some get requests to API

47
00:02:17.220 --> 00:02:19.700
V2 user dashboard as well.

48
00:02:19.900 --> 00:02:22.220
Let's close this, make this a little bit

49
00:02:22.220 --> 00:02:22.840
easier to see.

50
00:02:22.980 --> 00:02:25.060
You can see we have our token here,

51
00:02:25.580 --> 00:02:28.740
authorization bearer and the token itself.

52
00:02:29.020 --> 00:02:32.100
So I'm just gonna grab this and then

53
00:02:32.100 --> 00:02:34.440
I'm gonna come back to JWT tool.

54
00:02:35.240 --> 00:02:37.960
Whoops, I clearly didn't copy it.

55
00:02:38.860 --> 00:02:40.900
I think I hit control shift C, which

56
00:02:40.900 --> 00:02:44.260
is copying from the terminal rather than application.

57
00:02:45.220 --> 00:02:48.620
And it gives us basically the same information

58
00:02:48.620 --> 00:02:50.960
that JWT IO would give us.

59
00:02:51.040 --> 00:02:53.620
So if I just grab this and pop

60
00:02:53.620 --> 00:02:55.440
it in here, you can see the algorithm

61
00:02:55.440 --> 00:02:59.040
and the payloads, sorry, the header which contains

62
00:02:59.040 --> 00:03:00.820
the algorithm and the payload data.

63
00:03:01.980 --> 00:03:04.080
And you can also basically see the same

64
00:03:04.080 --> 00:03:04.640
thing here.

65
00:03:05.220 --> 00:03:06.860
But if you prefer working in the terminal

66
00:03:06.860 --> 00:03:08.700
and you don't wanna switch out to JWT

67
00:03:08.700 --> 00:03:11.140
.IO, then this is a good way of

68
00:03:11.140 --> 00:03:12.860
quickly having a look at a token.

69
00:03:13.420 --> 00:03:15.440
Or if you're passing in lots of tokens

70
00:03:15.440 --> 00:03:17.580
and you're scripting something, this is a good

71
00:03:17.580 --> 00:03:19.140
way to pass in a lot of data

72
00:03:19.140 --> 00:03:22.280
and grep for stuff coming out or for

73
00:03:22.280 --> 00:03:22.660
example.

74
00:03:23.440 --> 00:03:27.140
So we can see sub is a.tcmsec

75
00:03:27.140 --> 00:03:30.040
.com, the role is user and the issue

76
00:03:30.040 --> 00:03:32.980
.time and the expiry time as well.

77
00:03:36.560 --> 00:03:39.360
So what I wanna do next is I'm

78
00:03:39.360 --> 00:03:42.080
just going to do JWT, the same thing,

79
00:03:42.240 --> 00:03:43.080
JWT tool.

80
00:03:44.000 --> 00:03:46.140
And then I'm gonna pass, oh, let me

81
00:03:46.140 --> 00:03:50.380
move myself out of the way, dash capital

82
00:03:50.380 --> 00:03:50.800
T.

83
00:03:51.120 --> 00:03:52.500
So you can see this.

84
00:03:53.260 --> 00:03:56.660
So what this does is this allows us

85
00:03:56.660 --> 00:03:58.120
to modify a token.

86
00:03:58.500 --> 00:04:00.940
So you can see here, we have the

87
00:04:00.940 --> 00:04:03.660
algorithm RS-256.

88
00:04:04.040 --> 00:04:05.920
Now with the header, we can add a

89
00:04:05.920 --> 00:04:09.720
value, delete a value or continue to next

90
00:04:09.720 --> 00:04:10.380
step.

91
00:04:10.880 --> 00:04:12.320
So let's just continue.

92
00:04:12.500 --> 00:04:14.340
I wanna add something into the payload.

93
00:04:14.780 --> 00:04:16.500
So here we are in the payload section

94
00:04:16.980 --> 00:04:18.940
and I want to add something.

95
00:04:18.940 --> 00:04:23.760
So let's do five and I want to

96
00:04:23.760 --> 00:04:28.820
add, I don't know, and the value is,

97
00:04:29.220 --> 00:04:30.520
I don't know, just for example.

98
00:04:31.760 --> 00:04:34.480
And then we want to continue to the

99
00:04:34.480 --> 00:04:34.960
next step.

100
00:04:35.500 --> 00:04:38.860
And then because we don't actually have the

101
00:04:38.860 --> 00:04:41.460
private key to sign this, and if you

102
00:04:41.460 --> 00:04:45.460
notice the key is RS-256, so this

103
00:04:45.460 --> 00:04:47.580
is asymmetric encryption.

104
00:04:49.300 --> 00:04:52.500
The signature is unchanged, so no signing method

105
00:04:52.500 --> 00:04:53.080
specified.

106
00:04:53.360 --> 00:04:55.160
So we haven't re-signed the token.

107
00:04:55.360 --> 00:04:57.880
So I suspect when we use this, we

108
00:04:57.880 --> 00:04:59.940
will get a signature invalid.

109
00:05:00.480 --> 00:05:03.120
But this is a way of modifying tokens

110
00:05:03.120 --> 00:05:05.620
if you prefer to be in the terminal,

111
00:05:05.820 --> 00:05:06.720
if that makes sense.

112
00:05:08.400 --> 00:05:10.740
Now what we want to do next is

113
00:05:10.740 --> 00:05:15.780
take a look at JWT, sorry, tool help.

114
00:05:17.180 --> 00:05:18.960
And have a look at some of the

115
00:05:18.960 --> 00:05:20.180
things that we can do.

116
00:05:20.480 --> 00:05:23.760
So what we want to look at is

117
00:05:23.760 --> 00:05:25.500
the dash M mode.

118
00:05:25.660 --> 00:05:27.900
So we can actually audit tokens.

119
00:05:28.500 --> 00:05:31.760
So we can do playbook audits, fuzz existing

120
00:05:31.760 --> 00:05:35.540
claims to force errors, fuzz common claims to

121
00:05:35.540 --> 00:05:38.340
see whether we get different results, or we

122
00:05:38.340 --> 00:05:39.400
can do all tests.

123
00:05:40.120 --> 00:05:43.860
Now, since crappy is running locally and it's

124
00:05:43.860 --> 00:05:45.480
not a production system, I'm not going to

125
00:05:45.480 --> 00:05:46.140
break anything.

126
00:05:46.740 --> 00:05:48.560
Why not just go ahead and do all

127
00:05:48.560 --> 00:05:49.100
tests?

128
00:05:49.800 --> 00:05:51.820
So to do this, we need a couple

129
00:05:51.820 --> 00:05:52.420
of things.

130
00:05:52.620 --> 00:05:56.320
So we're going to do JWT tool, and

131
00:05:56.320 --> 00:05:57.100
we need a target.

132
00:05:57.480 --> 00:05:59.440
So what I'm going to do is use

133
00:05:59.440 --> 00:06:01.440
the same endpoint as before.

134
00:06:01.700 --> 00:06:06.000
So this identity API V2 user dashboard, and

135
00:06:06.000 --> 00:06:09.220
it's important that the target processes the token

136
00:06:09.220 --> 00:06:11.420
in some way and gives back different results.

137
00:06:11.420 --> 00:06:14.300
So for example, if we provided a different

138
00:06:14.300 --> 00:06:17.720
token or no token at all, let's demonstrate

139
00:06:17.720 --> 00:06:18.760
this quickly in repeater.

140
00:06:19.340 --> 00:06:22.460
So I send this and I get the

141
00:06:22.460 --> 00:06:23.420
information back.

142
00:06:23.720 --> 00:06:27.440
If I don't provide a token, we get

143
00:06:27.440 --> 00:06:28.800
a different response.

144
00:06:28.960 --> 00:06:31.140
If you use an endpoint that doesn't process

145
00:06:31.140 --> 00:06:33.640
the token or the response doesn't change based

146
00:06:33.640 --> 00:06:35.260
on your input, then you're not going to

147
00:06:35.260 --> 00:06:37.260
get any results is basically what I mean.

148
00:06:38.220 --> 00:06:41.160
So a help page or an about page,

149
00:06:41.260 --> 00:06:44.140
for example, might not check whether you have

150
00:06:44.140 --> 00:06:45.220
a JWT.

151
00:06:45.620 --> 00:06:49.120
So I'm going to paste this in here

152
00:06:49.120 --> 00:06:52.360
and obviously I need to do HTTP slash

153
00:06:52.360 --> 00:06:53.820
slash localhost.

154
00:06:54.960 --> 00:06:57.680
And then it's 8888, I think, if I

155
00:06:57.680 --> 00:06:57.980
recall.

156
00:06:58.840 --> 00:07:01.540
And then what we need next is the

157
00:07:01.540 --> 00:07:02.700
authorization header.

158
00:07:02.880 --> 00:07:05.020
So we actually need to pass in our

159
00:07:05.020 --> 00:07:06.520
token as a header.

160
00:07:06.520 --> 00:07:09.740
So same, you can copy this from bub

161
00:07:09.740 --> 00:07:12.260
suite or you can just write it out.

162
00:07:12.600 --> 00:07:15.100
And then we want the authorization bearer.

163
00:07:15.220 --> 00:07:16.360
And actually, I'm just going to go ahead

164
00:07:16.360 --> 00:07:19.380
and copy this token, this whole thing.

165
00:07:20.920 --> 00:07:22.580
Because I think that's probably the easiest way

166
00:07:22.580 --> 00:07:23.600
to do it.

167
00:07:24.380 --> 00:07:25.720
And then we want the mode.

168
00:07:25.960 --> 00:07:28.360
So if we come back up to our

169
00:07:28.360 --> 00:07:30.380
help file, we can see the mode here

170
00:07:30.380 --> 00:07:32.680
and we're just going to do all tests.

171
00:07:33.300 --> 00:07:36.040
And also notice that there's also dash X

172
00:07:36.040 --> 00:07:36.700
exploits.

173
00:07:37.140 --> 00:07:39.700
So we can try and exploit known vulnerabilities.

174
00:07:42.920 --> 00:07:44.440
And we get a load of data back.

175
00:07:44.640 --> 00:07:47.300
So let's go from top to bottom.

176
00:07:48.000 --> 00:07:50.300
So it does an initial test.

177
00:07:50.660 --> 00:07:53.480
So sending the token and we get a

178
00:07:53.480 --> 00:07:55.140
200 back, which is good.

179
00:07:55.920 --> 00:07:58.100
And then we do some pre-scan checks.

180
00:07:58.840 --> 00:08:02.820
So pre-scan original token and our response

181
00:08:02.820 --> 00:08:06.180
code and we get 179 bytes back.

182
00:08:07.080 --> 00:08:09.760
And this is basically the content length of

183
00:08:09.760 --> 00:08:10.460
the response.

184
00:08:10.900 --> 00:08:12.300
So we can check this.

185
00:08:12.380 --> 00:08:15.100
If we come back to bub suites, we

186
00:08:15.100 --> 00:08:16.440
can see this is where I took the

187
00:08:16.440 --> 00:08:17.140
token from.

188
00:08:17.440 --> 00:08:22.280
And indeed here is the content length 179

189
00:08:22.760 --> 00:08:25.200
and the data that comes back with it.

190
00:08:25.700 --> 00:08:28.520
So this is important to know because when

191
00:08:28.520 --> 00:08:31.020
we look at other requests, we want to

192
00:08:31.020 --> 00:08:33.659
see whether the content length has changed and

193
00:08:33.659 --> 00:08:35.320
we also want to look at the response

194
00:08:35.320 --> 00:08:35.659
code.

195
00:08:36.000 --> 00:08:38.940
So the next check, no token, we get

196
00:08:38.940 --> 00:08:41.919
a 404 and 58 bytes and we can

197
00:08:41.919 --> 00:08:44.940
verify this in bub suites by coming in

198
00:08:44.940 --> 00:08:48.400
here, deleting this and we get a 404

199
00:08:48.400 --> 00:08:49.420
and 58 bytes.

200
00:08:49.580 --> 00:08:51.700
So it's actually doing a lot of tests

201
00:08:51.700 --> 00:08:52.240
for us.

202
00:08:52.360 --> 00:08:53.820
And then if we want to, we can

203
00:08:53.820 --> 00:08:55.020
verify them manually.

204
00:08:56.200 --> 00:08:59.700
So broken signature response code, 200179.

205
00:09:00.760 --> 00:09:04.100
So this is a very interesting finding in

206
00:09:04.100 --> 00:09:07.260
that we get a 200 back, which yeah,

207
00:09:07.400 --> 00:09:11.260
that seems okay but the bytes, the content

208
00:09:11.260 --> 00:09:12.240
length matches.

209
00:09:12.920 --> 00:09:15.100
And again, we can come back and verify

210
00:09:15.100 --> 00:09:17.360
this by breaking our signature.

211
00:09:17.620 --> 00:09:20.700
So I'm just going to remove some data

212
00:09:20.700 --> 00:09:23.940
out of this and we still get the

213
00:09:23.940 --> 00:09:24.860
same response.

214
00:09:25.640 --> 00:09:26.740
And this is really interesting.

215
00:09:26.880 --> 00:09:30.160
This says to me that, hey, the application

216
00:09:30.160 --> 00:09:33.080
is not checking the signature or it's not

217
00:09:33.080 --> 00:09:35.160
verifying the data that we're sending.

218
00:09:35.760 --> 00:09:38.360
And we need to do some further testing.

219
00:09:39.220 --> 00:09:41.840
So that's a really interesting finding right off

220
00:09:41.840 --> 00:09:42.260
the bat.

221
00:09:42.500 --> 00:09:45.080
And what it's now doing is repeating the

222
00:09:45.080 --> 00:09:46.000
original token.

223
00:09:46.320 --> 00:09:48.680
So it's just checking that even after sending

224
00:09:48.680 --> 00:09:53.340
broken or difference tokens, can we still use

225
00:09:53.340 --> 00:09:54.300
the original token?

226
00:09:54.840 --> 00:09:58.240
So some systems or some web applications may

227
00:09:58.240 --> 00:10:00.820
give you a new token each time you

228
00:10:00.820 --> 00:10:02.520
send a request, for example.

229
00:10:03.680 --> 00:10:08.300
All right, so launching the JWT attack playbook

230
00:10:08.300 --> 00:10:10.960
and we basically do the same as what

231
00:10:10.960 --> 00:10:12.240
we just kind of talked through.

232
00:10:12.800 --> 00:10:14.420
We look at what it did.

233
00:10:14.600 --> 00:10:15.860
We look at the response code.

234
00:10:16.000 --> 00:10:18.260
We look at the content length and then

235
00:10:18.260 --> 00:10:20.920
we think to ourselves, is this normal behavior

236
00:10:21.500 --> 00:10:23.500
based on what I know about the endpoints?

237
00:10:24.120 --> 00:10:26.100
And if it isn't, or if we need

238
00:10:26.100 --> 00:10:28.360
to verify it, we can come into Bubsuite

239
00:10:28.360 --> 00:10:30.840
and we can verify the behavior.

240
00:10:31.820 --> 00:10:34.300
So reading down these, if you're not sure

241
00:10:34.300 --> 00:10:36.660
what any of them are, you can actually

242
00:10:36.660 --> 00:10:40.580
come over to the JWT tool.

243
00:10:41.780 --> 00:10:43.860
And then if you scroll all the way

244
00:10:43.860 --> 00:10:46.080
down, and I definitely recommend you do this

245
00:10:46.080 --> 00:10:48.840
as kind of like extra study, keep going

246
00:10:48.840 --> 00:10:49.860
all the way down to the bottom.

247
00:10:50.040 --> 00:10:52.960
We have the JWT attack book for a

248
00:10:52.960 --> 00:10:55.380
detailed run through of JWT attacks.

249
00:10:56.400 --> 00:10:58.140
So in here, there's like a bit of

250
00:10:58.140 --> 00:11:00.180
a primer, which we've probably already covered quite

251
00:11:00.180 --> 00:11:01.040
a lot of already.

252
00:11:01.480 --> 00:11:04.920
Attack methodology, vulnerable claims, known exploits, finding public

253
00:11:04.920 --> 00:11:09.180
keys, tampering, fuzzing, stealing JWTs using JWT tools.

254
00:11:09.620 --> 00:11:12.620
So you can use this in conjunction with

255
00:11:12.620 --> 00:11:13.340
your findings.

256
00:11:13.340 --> 00:11:16.220
So if it flags and says, hey, you

257
00:11:16.220 --> 00:11:22.340
might be vulnerable to CVE-2015-9235-alg

258
00:11:22.340 --> 00:11:25.280
-non-attack, which when we go back, we

259
00:11:25.280 --> 00:11:28.640
actually see here that we get a valid

260
00:11:28.640 --> 00:11:33.060
response and the same content length for alg

261
00:11:33.060 --> 00:11:33.360
-non.

262
00:11:33.500 --> 00:11:34.900
So this is a super interesting finding.

263
00:11:35.280 --> 00:11:37.120
You can come in here and read more

264
00:11:37.120 --> 00:11:40.560
about the attack and how the attack works,

265
00:11:40.900 --> 00:11:42.600
how to replicate it and how to pull

266
00:11:42.600 --> 00:11:42.880
it off.

267
00:11:42.880 --> 00:11:45.840
Consider this your homework if you want to

268
00:11:45.840 --> 00:11:49.460
understand and learn more about JWT attacks.

269
00:11:49.960 --> 00:11:51.620
This is definitely a great place to go.

270
00:11:52.360 --> 00:11:54.600
One other place that actually I'll mention since

271
00:11:54.600 --> 00:11:58.840
we're here already, of course, is the Portswoga

272
00:11:58.840 --> 00:12:01.700
Web Security Academy.

273
00:12:03.080 --> 00:12:06.400
And if we come in here and go

274
00:12:06.400 --> 00:12:10.520
to Academy, and then I think we can

275
00:12:10.520 --> 00:12:17.760
just do all labs, search for JWT, and

276
00:12:17.760 --> 00:12:20.840
there's a load of labs for expanding your

277
00:12:20.840 --> 00:12:23.420
knowledge on JSON web token attacks as well.

278
00:12:23.540 --> 00:12:26.620
So a couple of resources to keep your

279
00:12:26.620 --> 00:12:27.200
study going.

280
00:12:27.780 --> 00:12:29.500
So let's explore this.

281
00:12:29.720 --> 00:12:32.200
And actually I want to also show off

282
00:12:32.200 --> 00:12:33.640
a very useful plugin.

283
00:12:34.080 --> 00:12:37.080
So if you come over to PubSuite, click

284
00:12:37.080 --> 00:12:41.960
Extender, BApp Store, and just search for JWT,

285
00:12:42.080 --> 00:12:46.080
of course, we have this JWT editor.

286
00:12:46.300 --> 00:12:47.480
And then there are a few other plugins

287
00:12:47.480 --> 00:12:49.760
that you can explore as well, but I'm

288
00:12:49.760 --> 00:12:51.220
just going to install this one.

289
00:12:52.160 --> 00:12:53.900
Only takes a second to install.

290
00:12:54.480 --> 00:12:56.420
And there's a couple of things that you

291
00:12:56.420 --> 00:12:59.900
should notice is that if we clear our

292
00:12:59.900 --> 00:13:04.720
history and we come back to our application,

293
00:13:04.720 --> 00:13:06.780
and let's say, I'm just going to log

294
00:13:06.780 --> 00:13:07.520
back in again.

295
00:13:16.170 --> 00:13:17.450
Oh, I really want a Lamborghini.

296
00:13:19.270 --> 00:13:21.310
You can see that it's actually, and now

297
00:13:21.310 --> 00:13:24.330
it's active, it's highlighting automatically in green posts

298
00:13:24.330 --> 00:13:26.790
that include our JWT.

299
00:13:26.970 --> 00:13:29.790
So we can really quickly map an application

300
00:13:30.490 --> 00:13:33.410
and see, have a look for endpoints that

301
00:13:33.410 --> 00:13:36.990
do or don't require a JSON web token

302
00:13:36.990 --> 00:13:40.130
to access or they're being passed within those

303
00:13:40.130 --> 00:13:40.650
requests.

304
00:13:41.930 --> 00:13:45.030
Next up, we can come back to the

305
00:13:45.030 --> 00:13:48.290
repeater and we can see that we have

306
00:13:48.290 --> 00:13:51.290
a JSON web token tab.

307
00:13:52.110 --> 00:13:55.530
And we can see, it decodes the token

308
00:13:55.530 --> 00:13:57.910
for us nicely and we can quickly have

309
00:13:57.910 --> 00:13:59.590
a look and inspect the token.

310
00:14:00.310 --> 00:14:03.550
So since we're investigating, whoops, the non-attack,

311
00:14:03.810 --> 00:14:05.770
the arg-non, I can come in here

312
00:14:05.770 --> 00:14:08.210
and I can just click attack and I

313
00:14:08.210 --> 00:14:10.630
can click non-signed algorithm.

314
00:14:10.630 --> 00:14:12.870
And you can see that it's changed the

315
00:14:12.870 --> 00:14:13.470
header for me.

316
00:14:13.710 --> 00:14:16.370
The algorithm has changed to none and I

317
00:14:16.370 --> 00:14:17.550
can hit send.

318
00:14:19.370 --> 00:14:22.570
And we do indeed still get back our

319
00:14:22.570 --> 00:14:23.470
user data.

320
00:14:23.850 --> 00:14:25.050
So this is very interesting.

321
00:14:25.230 --> 00:14:27.410
You notice that the signature is missing from

322
00:14:27.410 --> 00:14:28.370
this token.

323
00:14:29.130 --> 00:14:30.570
So what I want to do now is

324
00:14:30.570 --> 00:14:34.050
an interesting quirk of this is that the

325
00:14:34.050 --> 00:14:35.390
tab disappears.

326
00:14:35.530 --> 00:14:36.650
I'm not sure if this is a bug,

327
00:14:36.810 --> 00:14:38.370
but there's a way to fix this.

328
00:14:38.370 --> 00:14:41.350
So if you come to here, send this

329
00:14:41.350 --> 00:14:45.230
back to repeater, hit send initially, and then

330
00:14:45.230 --> 00:14:45.990
edit your token.

331
00:14:46.410 --> 00:14:50.110
And then if we do non and then

332
00:14:50.110 --> 00:14:52.450
send this again, you see that it disappears.

333
00:14:52.690 --> 00:14:54.510
But when we click the back to restore

334
00:14:54.510 --> 00:14:57.290
our original token, it comes back again.

335
00:14:57.410 --> 00:14:59.490
So I'm not sure if it's intended functionality,

336
00:14:59.950 --> 00:15:01.990
but yeah, make sure you just send an

337
00:15:01.990 --> 00:15:04.430
initial request before editing the token.

338
00:15:05.040 --> 00:15:07.610
So what I actually want to do here

339
00:15:07.610 --> 00:15:11.410
is test whether we can change this to

340
00:15:11.410 --> 00:15:13.830
none and see whether we can see a

341
00:15:13.830 --> 00:15:14.570
different user.

342
00:15:14.870 --> 00:15:18.330
So I think the user B exists and

343
00:15:18.330 --> 00:15:19.470
then we can hit send.

344
00:15:20.490 --> 00:15:22.430
Our given email is not registered.

345
00:15:23.250 --> 00:15:26.490
So let's come back to here.

346
00:15:26.630 --> 00:15:29.630
I think we know that the community page

347
00:15:29.630 --> 00:15:31.630
does leak some data.

348
00:15:32.630 --> 00:15:35.030
So let's come back to pubsuites.

349
00:15:36.150 --> 00:15:39.990
We could also just create an account, but

350
00:15:39.990 --> 00:15:42.950
we can very quickly just find an email

351
00:15:42.950 --> 00:15:43.910
address here.

352
00:15:44.490 --> 00:15:51.700
So I'm just going to copy this, paste,

353
00:15:53.020 --> 00:15:56.560
and we can indeed request information from other

354
00:15:56.560 --> 00:15:56.980
accounts.

355
00:15:57.260 --> 00:15:59.760
So note that we need their email address,

356
00:15:59.940 --> 00:16:01.660
but now we're leaking their phone number.

357
00:16:02.160 --> 00:16:05.120
And if they had a video available and

358
00:16:05.120 --> 00:16:08.540
some other information like their available credits is

359
00:16:08.540 --> 00:16:09.580
also leaked.

360
00:16:10.020 --> 00:16:11.740
Their picture URL, not sure if this is

361
00:16:11.740 --> 00:16:13.880
private or not, but maybe it would give

362
00:16:13.880 --> 00:16:15.840
us the full path to that picture.

363
00:16:17.380 --> 00:16:21.020
Now, interesting that actually I just demonstrated this

364
00:16:21.020 --> 00:16:24.100
attack and I did not switch the non

365
00:16:24.100 --> 00:16:26.640
-signing algorithm attack on.

366
00:16:26.860 --> 00:16:29.940
So actually this seems like even though it's

367
00:16:29.940 --> 00:16:34.640
flagged as algorithm none, I suspect the issue

368
00:16:34.640 --> 00:16:38.360
is that the JSON web token is being

369
00:16:38.360 --> 00:16:41.900
passed and the response is being generated and

370
00:16:41.900 --> 00:16:44.160
sent back without checking the signature.

371
00:16:44.700 --> 00:16:46.620
Now this happens a lot when, for example,

372
00:16:46.740 --> 00:16:49.360
if you're using node and you use the

373
00:16:49.360 --> 00:16:53.220
function decode instead of verify, you can pass

374
00:16:53.220 --> 00:16:56.900
a JSON web token without a valid signature

375
00:16:56.900 --> 00:16:58.660
and it will still process it.

376
00:16:58.660 --> 00:17:02.880
So when you're reporting this issue, the attack

377
00:17:02.880 --> 00:17:05.880
actually isn't the non-signing algorithm attack.

378
00:17:06.180 --> 00:17:08.460
It's actually just the fact that we're not

379
00:17:08.460 --> 00:17:10.339
checking the signature at all.

380
00:17:10.819 --> 00:17:12.740
At least that's what appears to be happening

381
00:17:12.740 --> 00:17:13.920
in this case.

382
00:17:14.980 --> 00:17:17.460
So that's it for JWT tool.

383
00:17:17.700 --> 00:17:19.099
Now, I hope this got you off to

384
00:17:19.099 --> 00:17:21.660
a good start with JWTs and how we

385
00:17:21.660 --> 00:17:22.380
can attack them.

386
00:17:22.740 --> 00:17:25.500
As I mentioned before, definitely consider furthering your

387
00:17:25.500 --> 00:17:25.859
study.

388
00:17:26.200 --> 00:17:28.660
Maybe after you finish this course in areas

389
00:17:28.660 --> 00:17:30.640
that are relevant to you and your day

390
00:17:30.640 --> 00:17:31.440
-to-day work.

391
00:17:31.940 --> 00:17:34.280
In the next section, we'll walk through some

392
00:17:34.280 --> 00:17:35.900
of the challenges and then move on.

393
00:17:36.500 --> 00:17:37.020
See you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.210 --> 00:00:02.670
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome to the final video of

2
00:00:02.670 --> 00:00:03.410
this section.

3
00:00:03.730 --> 00:00:06.470
Now, I'm really excited because you've made great

4
00:00:06.470 --> 00:00:08.790
progress so far, and it's a real honor

5
00:00:08.790 --> 00:00:10.410
for me to be able to support you

6
00:00:10.410 --> 00:00:11.330
on your journey.

7
00:00:11.690 --> 00:00:13.770
So let's take a look at the two

8
00:00:13.770 --> 00:00:15.970
challenges from earlier in this section.

9
00:00:16.130 --> 00:00:18.110
First, we'll find a way to brute force

10
00:00:18.110 --> 00:00:20.470
the second user from the brute force me

11
00:00:20.470 --> 00:00:23.530
application, and we'll do this with both burp

12
00:00:23.530 --> 00:00:27.410
suite and FFUF, and then we'll look at

13
00:00:27.410 --> 00:00:30.070
the analyze me challenge so that we can

14
00:00:30.070 --> 00:00:33.030
forge a token and log in as Jeremy

15
00:00:33.030 --> 00:00:34.950
on the second application.

16
00:00:35.470 --> 00:00:37.690
Let's dive straight in.

17
00:00:38.250 --> 00:00:41.570
So here I have the brute force me

18
00:00:41.570 --> 00:00:45.210
application up and running, and if we just

19
00:00:45.210 --> 00:00:47.690
come to login, and all I'm going to

20
00:00:47.690 --> 00:00:51.590
do is do Alex and Alex, and then

21
00:00:51.590 --> 00:00:53.990
double check that my proxy is on, which

22
00:00:53.990 --> 00:00:56.350
it is, and just click login, and we

23
00:00:56.350 --> 00:00:58.030
get invalid username.

24
00:00:58.990 --> 00:01:01.070
All right, so I'll close this, and then

25
00:01:01.070 --> 00:01:04.209
I'll come over to burp suite, proxy, HTTP

26
00:01:04.209 --> 00:01:06.730
history, and we can see the post request

27
00:01:06.730 --> 00:01:11.130
to slash v1 slash verify, and if we

28
00:01:11.130 --> 00:01:13.870
have a look, we can see the username,

29
00:01:14.130 --> 00:01:16.530
which apologies, yeah, it's still marked as email.

30
00:01:16.890 --> 00:01:18.350
When I update the labs, I'll get around

31
00:01:18.350 --> 00:01:19.010
to changing this.

32
00:01:19.150 --> 00:01:21.050
Originally, I was using email addresses, but then

33
00:01:21.050 --> 00:01:22.630
changed my mind for some reason.

34
00:01:23.150 --> 00:01:26.190
Forgot to update the attribute name, and we

35
00:01:26.190 --> 00:01:28.430
have the password as Alex, and we come

36
00:01:28.430 --> 00:01:30.350
back with invalid username.

37
00:01:31.210 --> 00:01:33.670
So let's just send this to intruder with

38
00:01:33.670 --> 00:01:36.130
ctrl i, or you can right click and

39
00:01:36.130 --> 00:01:39.470
click send to intruder, and what we want

40
00:01:39.470 --> 00:01:42.690
to do is first clear the selections, and

41
00:01:42.690 --> 00:01:44.770
we just want to add one on the

42
00:01:44.770 --> 00:01:45.250
usernames.

43
00:01:45.630 --> 00:01:47.430
So to begin with, we want to try

44
00:01:47.430 --> 00:01:49.490
and find the relevant username.

45
00:01:50.570 --> 00:01:53.690
So here, I'm going to think about what

46
00:01:53.690 --> 00:01:55.410
payload I want to use.

47
00:01:55.970 --> 00:01:58.970
So I know that there are some names

48
00:01:58.970 --> 00:02:05.470
in user, share, cyclists, usernames, names, here we

49
00:02:05.470 --> 00:02:07.990
are, and we have a few different to

50
00:02:07.990 --> 00:02:08.449
choose from.

51
00:02:08.650 --> 00:02:11.810
So we have family names USA, female names,

52
00:02:11.990 --> 00:02:15.730
four names India, male names USA, and names

53
00:02:15.730 --> 00:02:18.210
.txt, and I think if we just check

54
00:02:18.210 --> 00:02:21.990
the length of this, just make sure it's

55
00:02:21.990 --> 00:02:28.120
not too long, 10,100, so that should

56
00:02:28.120 --> 00:02:28.540
be okay.

57
00:02:28.700 --> 00:02:31.160
I think we'll go with this names.txt.

58
00:02:33.460 --> 00:02:36.840
So load, and then we'll come back up

59
00:02:36.840 --> 00:02:42.900
to usernames, names, names.txt, and we'll hit

60
00:02:42.900 --> 00:02:43.880
start attack.

61
00:02:44.620 --> 00:02:46.760
And of course, we're running locally, so it's

62
00:02:46.760 --> 00:02:48.040
not going to take too long to get

63
00:02:48.040 --> 00:02:51.840
through all of the 10,000 requests, and

64
00:02:51.840 --> 00:02:52.220
it's done.

65
00:02:52.760 --> 00:02:54.500
So first thing we want to check for

66
00:02:54.500 --> 00:02:55.520
is the status code.

67
00:02:56.420 --> 00:02:59.900
Everything is a 401, so unfortunately that's not

68
00:02:59.900 --> 00:03:01.300
going to give us a hint.

69
00:03:01.820 --> 00:03:03.520
And the next thing to check is the

70
00:03:03.520 --> 00:03:07.620
length, and as we can see, these two

71
00:03:07.620 --> 00:03:10.180
have a slightly different length, so it looks

72
00:03:10.180 --> 00:03:14.220
like admin, if we check the response, has

73
00:03:14.220 --> 00:03:18.300
invalid password, and Jeremy also has invalid password.

74
00:03:19.060 --> 00:03:21.800
Now, notice the response length is very close,

75
00:03:22.140 --> 00:03:24.700
and actually, if we take a little look

76
00:03:24.700 --> 00:03:27.380
at this, we can see that if we'd

77
00:03:27.380 --> 00:03:31.100
had a more consistent and better developer other

78
00:03:31.100 --> 00:03:35.100
than myself, the response length actually might have

79
00:03:35.100 --> 00:03:37.580
been the same, with the inconsistency here being

80
00:03:37.580 --> 00:03:38.820
the exclamation mark.

81
00:03:39.600 --> 00:03:42.900
Now, if we couldn't find these, but we

82
00:03:42.900 --> 00:03:44.520
had an inkling that they might be in

83
00:03:44.520 --> 00:03:45.940
there, we go through a big list, and

84
00:03:45.940 --> 00:03:47.660
we're like, hmm, no results, really?

85
00:03:47.960 --> 00:03:50.480
We might want to do something, for example,

86
00:03:50.680 --> 00:03:54.900
is take the normal, something that comes back

87
00:03:54.900 --> 00:04:00.360
in the response of the usual response, come

88
00:04:00.360 --> 00:04:03.820
up to filter, paste this in here, and

89
00:04:03.820 --> 00:04:05.580
do a negative search, so we want to

90
00:04:05.580 --> 00:04:07.820
search for everything that doesn't have the string

91
00:04:07.820 --> 00:04:11.100
invalid username, and when we press that, we

92
00:04:11.100 --> 00:04:12.820
get admin and Jeremy.

93
00:04:13.380 --> 00:04:16.820
So, if we were tricked and the content

94
00:04:16.820 --> 00:04:19.660
length was the same, then, yeah, this is

95
00:04:19.660 --> 00:04:22.200
a way to find responses, so don't just

96
00:04:22.200 --> 00:04:24.700
rely on status codes and length.

97
00:04:25.360 --> 00:04:26.840
I think a lot of people, a lot

98
00:04:26.840 --> 00:04:29.220
of security practitioners get a little bit frustrated

99
00:04:29.220 --> 00:04:32.120
when brute forcing doesn't work out, but there

100
00:04:32.120 --> 00:04:33.420
is technique to brute forcing.

101
00:04:33.840 --> 00:04:35.220
It is a skill, and it's a skill

102
00:04:35.220 --> 00:04:37.760
that you really need to learn, so, you

103
00:04:37.760 --> 00:04:40.200
know, don't get frustrated, hang in there, and

104
00:04:40.200 --> 00:04:41.520
try and work methodically.

105
00:04:43.400 --> 00:04:46.800
So, we have the user Jeremy, and I

106
00:04:46.800 --> 00:04:48.620
think we can just close this, discard that,

107
00:04:48.620 --> 00:04:51.880
and come back to the application, and go

108
00:04:51.880 --> 00:04:56.360
Jeremy, hit login, and, of course, we get

109
00:04:56.360 --> 00:04:59.000
the invalid password, so we will come back

110
00:04:59.000 --> 00:05:01.660
to web suites, grab this.

111
00:05:02.040 --> 00:05:04.300
I could just update the intruder setup that

112
00:05:04.300 --> 00:05:05.740
we have already, but I'm just going to

113
00:05:05.740 --> 00:05:06.300
create a new one.

114
00:05:06.760 --> 00:05:08.960
I like to separate my workspaces so if

115
00:05:08.960 --> 00:05:10.620
I need to go back, then I can

116
00:05:10.620 --> 00:05:12.320
go back and make changes.

117
00:05:14.220 --> 00:05:18.340
Add the payload field to this, and then

118
00:05:18.340 --> 00:05:22.300
think about the payloads, and, again, we need

119
00:05:22.300 --> 00:05:25.300
to think about what password list we might

120
00:05:25.300 --> 00:05:28.680
want to use, so if we just ls

121
00:05:28.680 --> 00:05:33.180
user share cyclists passwords, and there's quite a

122
00:05:33.180 --> 00:05:36.800
lot of lists here, so rocky is not

123
00:05:36.800 --> 00:05:37.580
too bad.

124
00:05:38.280 --> 00:05:41.000
Occasionally, I use this dark web 2017, but

125
00:05:41.000 --> 00:05:43.100
more often than not, I've found it not

126
00:05:43.100 --> 00:05:44.080
to be that useful.

127
00:05:44.740 --> 00:05:46.100
Zeta 1 is not too bad.

128
00:05:47.060 --> 00:05:49.360
I think the best thing to do is

129
00:05:49.360 --> 00:05:53.580
think about what your target is, what you're

130
00:05:53.580 --> 00:05:56.040
trying to brute force, and then think about

131
00:05:56.540 --> 00:05:59.540
a combination of lists that might help, and,

132
00:05:59.740 --> 00:06:01.100
to be honest, even with a little bit

133
00:06:01.100 --> 00:06:03.620
of Linux command line, not even that complicated,

134
00:06:04.220 --> 00:06:07.400
you could easily curate your own list that

135
00:06:07.400 --> 00:06:10.100
you can use in different situations, and that's

136
00:06:10.100 --> 00:06:12.320
probably going to be much more successful than

137
00:06:12.320 --> 00:06:14.100
just using a single list.

138
00:06:14.320 --> 00:06:19.020
So, let's try the zetotop10,000, I think,

139
00:06:19.220 --> 00:06:23.180
to begin with, and just load, come back

140
00:06:23.180 --> 00:06:31.190
up, passwords, and then 10,000 is a

141
00:06:31.190 --> 00:06:32.190
good place to start.

142
00:06:32.310 --> 00:06:35.210
Doesn't take too long, and we can see

143
00:06:35.210 --> 00:06:41.660
where we're at, and let's check for status

144
00:06:41.660 --> 00:06:45.000
codes, and, unfortunately, we didn't find it, and

145
00:06:45.000 --> 00:06:46.820
we'll just check the length for good measure

146
00:06:46.820 --> 00:06:47.640
as well.

147
00:06:48.120 --> 00:06:50.260
So, we should get a login if we

148
00:06:50.260 --> 00:06:52.280
find the valid one, so, in this case,

149
00:06:52.280 --> 00:06:54.380
I'm pretty confident that we didn't find the

150
00:06:54.380 --> 00:06:56.620
password based on the status code.

151
00:06:56.980 --> 00:07:02.020
So, let's discard this, clear the list, load

152
00:07:02.020 --> 00:07:04.640
it up again, and we have a choice.

153
00:07:04.760 --> 00:07:06.780
Maybe we could go for a longer list.

154
00:07:07.240 --> 00:07:09.520
So, we could go for this top 100

155
00:07:09.520 --> 00:07:12.460
,000, or we could go for a different

156
00:07:12.460 --> 00:07:12.840
list.

157
00:07:13.260 --> 00:07:17.000
So, let's try the dark web top 10

158
00:07:17.000 --> 00:07:20.220
,000, because it's only going to take a

159
00:07:20.220 --> 00:07:21.320
few seconds to check.

160
00:07:24.850 --> 00:07:25.650
Still nothing.

161
00:07:26.050 --> 00:07:29.770
So, let's discard this, clear, and let's step

162
00:07:29.770 --> 00:07:31.410
up to a bigger list.

163
00:07:34.600 --> 00:07:36.180
This one's going to take a little bit

164
00:07:36.180 --> 00:07:36.920
longer to run.

165
00:07:38.300 --> 00:07:39.260
All right.

166
00:07:39.980 --> 00:07:42.660
So, we can take a quick look, and

167
00:07:42.660 --> 00:07:44.020
we got lucky.

168
00:07:44.540 --> 00:07:49.380
So, on the 99,973rd request, we got

169
00:07:49.380 --> 00:07:50.740
a status 200.

170
00:07:51.700 --> 00:07:54.500
Interesting that the password is just a number.

171
00:07:54.740 --> 00:07:56.500
So, let's actually have a quick look to

172
00:07:56.500 --> 00:08:01.600
see whether, so, cat user share word list,

173
00:08:02.000 --> 00:08:03.760
Rocky, crap.

174
00:08:05.200 --> 00:08:06.880
Ah, it is in Rocky, so we would

175
00:08:06.880 --> 00:08:09.560
have found it, although Rocky is 14 million,

176
00:08:09.760 --> 00:08:11.620
and this was just 100,000.

177
00:08:11.840 --> 00:08:13.820
So, we'd probably be here for the next

178
00:08:13.820 --> 00:08:18.220
hour if we were just using the Rocky

179
00:08:18.220 --> 00:08:21.320
word list, which is why I generally avoid

180
00:08:21.320 --> 00:08:25.020
using Rocky on online brute forcing, unless I

181
00:08:25.020 --> 00:08:25.860
really have to use it.

182
00:08:26.140 --> 00:08:28.060
I mean, every situation is different, right?

183
00:08:28.840 --> 00:08:31.100
So, we just click log in, and success,

184
00:08:31.100 --> 00:08:33.299
here is your flag, and we get our

185
00:08:33.299 --> 00:08:35.280
flag and a pat on the back.

186
00:08:35.500 --> 00:08:39.880
So, that's our brute force challenge done, and

187
00:08:39.880 --> 00:08:42.919
I can close this, and let's try and

188
00:08:42.919 --> 00:08:47.760
do the same thing again, but with ffuf.

189
00:08:48.020 --> 00:08:49.400
So, I'll just clear this quickly.

190
00:08:50.240 --> 00:08:52.100
So, we're just coming to our temp directory,

191
00:08:52.100 --> 00:08:55.820
and what I want to do is grab

192
00:08:55.820 --> 00:09:01.820
a request from Burp, so, let's grab the

193
00:09:01.820 --> 00:09:04.360
invalid one and work from that, because that's

194
00:09:04.360 --> 00:09:07.660
more realistic, and so, we're going to delete

195
00:09:07.660 --> 00:09:10.100
the old one that we had from the

196
00:09:10.100 --> 00:09:13.180
previous video, and then we're just going to

197
00:09:13.180 --> 00:09:18.560
vim rack.txt, pop this in, and then

198
00:09:18.560 --> 00:09:21.900
first of all, we want to do the

199
00:09:21.900 --> 00:09:23.980
user names, so, I'm just going to put

200
00:09:23.980 --> 00:09:29.360
fuzz in here, save and close, clear, and

201
00:09:29.360 --> 00:09:38.360
then request rack, and then request proto HTTP,

202
00:09:39.240 --> 00:09:42.880
and then our word list, user share, cyclists,

203
00:09:43.240 --> 00:09:49.900
user names, names, names.txt, and then we

204
00:09:49.900 --> 00:09:54.700
want to ignore 401s, so, if we run

205
00:09:54.700 --> 00:09:56.720
this, we can see that we get tons

206
00:09:56.720 --> 00:10:00.380
and tons of 401 errors, or 401 responses.

207
00:10:01.660 --> 00:10:06.240
So, we can do this by doing fc

208
00:10:06.240 --> 00:10:09.280
401, and we can also, if we want

209
00:10:09.280 --> 00:10:12.880
to filter out the size, I think it's

210
00:10:12.880 --> 00:10:16.180
fs, and we'd put in 30, for example.

211
00:10:16.800 --> 00:10:18.840
Since we're going for the username in this

212
00:10:18.840 --> 00:10:20.800
case, we actually want to get rid of

213
00:10:20.800 --> 00:10:24.640
the size of 30 and filter that out.

214
00:10:24.860 --> 00:10:27.160
That's correct, sorry, because the response is still

215
00:10:27.160 --> 00:10:30.180
going to be 401, and, as you can

216
00:10:30.180 --> 00:10:32.600
see, we get admin and Jeremy.

217
00:10:33.780 --> 00:10:36.720
Now, in the next attack, so, let's update

218
00:10:36.720 --> 00:10:42.320
our payload, so we have Jeremy, and then

219
00:10:42.320 --> 00:10:47.220
the password is going to be fuzz, and

220
00:10:47.220 --> 00:10:49.320
then we're going to send the same one,

221
00:10:49.700 --> 00:10:53.680
but we're going to filter out 401s, and

222
00:10:53.680 --> 00:10:57.560
we're going to update the payload to passwords,

223
00:10:59.320 --> 00:11:01.060
and which list was it?

224
00:11:01.160 --> 00:11:05.320
It was the Zato, and it was a

225
00:11:05.320 --> 00:11:08.500
big one, so, top 100,000, I think,

226
00:11:08.920 --> 00:11:12.860
and the nice thing about FFUF is that

227
00:11:12.860 --> 00:11:15.220
it's a little bit faster than Bubsuite, so

228
00:11:15.220 --> 00:11:19.240
it should go a little bit quicker, although,

229
00:11:19.700 --> 00:11:21.900
oh, wow, a lot quicker!

230
00:11:21.900 --> 00:11:27.360
Yeah, this tool never fails to impress, and

231
00:11:27.360 --> 00:11:29.320
even though I've used it a lot, I'm

232
00:11:29.320 --> 00:11:30.640
always surprised by the speed.

233
00:11:31.700 --> 00:11:35.080
So, it's found a status code 200 with

234
00:11:35.080 --> 00:11:38.660
this payload, and, again, we can verify this

235
00:11:38.660 --> 00:11:41.600
by going to login, Jeremy, paste in the

236
00:11:41.600 --> 00:11:46.480
password, and we get our flag, so, again,

237
00:11:46.580 --> 00:11:48.360
knowing the tools that we're going to use,

238
00:11:48.440 --> 00:11:51.700
knowing how to filter results and pass them

239
00:11:51.700 --> 00:11:54.560
correctly is going to be really, really important

240
00:11:54.560 --> 00:11:58.320
for your AppSec journey in general, but also

241
00:11:58.320 --> 00:11:59.940
with hacking APIs.

242
00:12:01.660 --> 00:12:04.400
All right, so, here we are in token,

243
00:12:04.920 --> 00:12:09.620
API token analysis, so, sudo docker compose up,

244
00:12:10.660 --> 00:12:13.300
and we'll come to our browser, I've already

245
00:12:13.300 --> 00:12:20.160
got Bubsuite running, and then just localhost 9000,

246
00:12:20.160 --> 00:12:22.300
and we just want to double check, yeah,

247
00:12:22.360 --> 00:12:24.020
there's no cookies or anything that are going

248
00:12:24.020 --> 00:12:24.840
to mess with us.

249
00:12:25.500 --> 00:12:30.420
So, if we recall, we remember from the

250
00:12:30.420 --> 00:12:34.180
previous video, we'll remember that the token is

251
00:12:34.180 --> 00:12:39.380
the username dash timestamp dash three random characters,

252
00:12:39.640 --> 00:12:43.360
and the timestamp would also pose an issue,

253
00:12:43.540 --> 00:12:45.500
but I think I already shared the hints

254
00:12:45.500 --> 00:12:48.420
that Jeremy logs in at the same time

255
00:12:48.420 --> 00:12:52.240
as the admin, so, in this scenario, and

256
00:12:52.240 --> 00:12:55.400
so, if we just log in, and I

257
00:12:55.400 --> 00:12:58.940
think the password is Ramirez, and, yeah, we

258
00:12:58.940 --> 00:13:01.620
get successfully logged in, and we get welcome

259
00:13:01.620 --> 00:13:05.080
admin, so, let's come back to here, and

260
00:13:05.080 --> 00:13:09.720
go proxy, HTTP history, here's our post, and

261
00:13:09.720 --> 00:13:11.700
we get our token back, and we can

262
00:13:11.700 --> 00:13:14.460
see in the subsequent get request, we have

263
00:13:14.460 --> 00:13:18.420
access equals this token, so, let's take this

264
00:13:18.420 --> 00:13:21.520
token, I'm going to copy it, send it

265
00:13:21.520 --> 00:13:26.240
to the decoder, decoders base 64, and here

266
00:13:26.240 --> 00:13:28.040
we have our token.

267
00:13:28.580 --> 00:13:30.520
Now, how are we going to go about

268
00:13:30.520 --> 00:13:31.780
building a payload?

269
00:13:33.180 --> 00:13:37.960
So, if we send this to the intruder,

270
00:13:38.780 --> 00:13:42.600
control I, and then what we want to

271
00:13:42.600 --> 00:13:44.960
do is, sorry, that's the wrong one, if

272
00:13:44.960 --> 00:13:48.540
we send the get request to the intruder,

273
00:13:48.820 --> 00:13:52.460
control I, we actually need to be able

274
00:13:52.460 --> 00:13:56.820
to either have a list of tokens ready

275
00:13:56.820 --> 00:14:00.580
to go, or what we can do sometimes

276
00:14:00.580 --> 00:14:05.400
is just replace, like, individual values, for example,

277
00:14:05.940 --> 00:14:08.120
but then if we were to replace these

278
00:14:08.120 --> 00:14:10.540
individual values, we then need to base 64

279
00:14:10.540 --> 00:14:12.300
encode the token.

280
00:14:13.060 --> 00:14:14.760
So, there's a few different ways to solve

281
00:14:14.760 --> 00:14:17.060
this, but I think the easiest way is

282
00:14:17.060 --> 00:14:20.640
for us to just create a list of

283
00:14:20.640 --> 00:14:24.180
tokens that we can load in and attack

284
00:14:24.180 --> 00:14:26.880
the application with, so, let's go ahead and

285
00:14:26.880 --> 00:14:31.660
do that with Python, and here scripting skills

286
00:14:31.660 --> 00:14:35.680
obviously helpful, so, if I just vim, let's

287
00:14:35.680 --> 00:14:40.440
call this tokens.py, and instead of vim,

288
00:14:40.580 --> 00:14:46.480
let's use mousepad as an alternative, and it

289
00:14:46.480 --> 00:14:47.640
might be a little bit easier to work

290
00:14:47.640 --> 00:14:50.140
with if I'm moving around and making adjustments.

291
00:14:51.380 --> 00:14:56.680
Now, we could use eta tools, but I

292
00:14:56.680 --> 00:15:00.060
can't remember exactly how to use them, so,

293
00:15:00.060 --> 00:15:03.540
instead of doing that, what we want to

294
00:15:03.540 --> 00:15:06.860
do is let's import base 64.

295
00:15:08.700 --> 00:15:09.140
Whoops.

296
00:15:10.160 --> 00:15:14.340
And we also want our character sets, so,

297
00:15:14.540 --> 00:15:16.900
this is going to be, whoops.

298
00:15:17.280 --> 00:15:19.120
A, B, C, D, E, F, G, H,

299
00:15:19.220 --> 00:15:21.680
A, J, K, L, M, N, O, P,

300
00:15:21.940 --> 00:15:25.920
Q, I, S, T, Q, R, S, Q,

301
00:15:26.000 --> 00:15:28.080
V, W, X, Y, Z.

302
00:15:28.620 --> 00:15:30.280
I'm sure some people can type that a

303
00:15:30.280 --> 00:15:31.060
lot faster than I can.

304
00:15:31.140 --> 00:15:32.620
I probably should have just gone along the

305
00:15:32.620 --> 00:15:35.780
keyboard and done a keyboard walk, but, you

306
00:15:35.780 --> 00:15:36.600
know, it's fine.

307
00:15:37.280 --> 00:15:38.080
Whatever works.

308
00:15:38.400 --> 00:15:40.480
And we also want the prefix to be

309
00:15:40.480 --> 00:15:42.020
this as well.

310
00:15:43.060 --> 00:15:44.580
And note that we don't need to brute

311
00:15:44.580 --> 00:15:48.120
force the timestamp because we know that Jeremy

312
00:15:48.120 --> 00:15:49.720
logs in the same time as admin, although

313
00:15:49.720 --> 00:15:51.960
if we re-log in as admin, it

314
00:15:51.960 --> 00:15:54.380
may reset that token, so just be aware

315
00:15:54.380 --> 00:15:55.000
of that.

316
00:15:56.180 --> 00:15:57.580
So, yeah, instead of using its tools, I

317
00:15:57.580 --> 00:16:00.760
think we're just going to use for I

318
00:16:00.760 --> 00:16:04.800
in range, and we'll just do the length

319
00:16:04.800 --> 00:16:10.040
of the characters, and we're just going to

320
00:16:10.040 --> 00:16:10.900
nest some loops.

321
00:16:11.320 --> 00:16:13.040
I'm just going to use spaces for now

322
00:16:13.040 --> 00:16:15.780
because the tab inside of here is crazy.

323
00:16:16.120 --> 00:16:21.500
And then for J in range, and we'll

324
00:16:21.500 --> 00:16:28.860
just do the length again of characters, and

325
00:16:28.860 --> 00:16:29.840
if you don't want to watch me code

326
00:16:29.840 --> 00:16:33.080
this out, feel free to skip forward.

327
00:16:33.280 --> 00:16:35.380
I'm just basically going to make three loops,

328
00:16:35.820 --> 00:16:38.180
nested loops, so that we iterate through all

329
00:16:38.180 --> 00:16:41.940
of the permutations that can be generated.

330
00:16:42.400 --> 00:16:45.040
That's not a very good explanation.

331
00:16:46.260 --> 00:16:48.100
And, actually, I'm going to create a list,

332
00:16:48.300 --> 00:16:50.000
so I'm just going to call perms equals,

333
00:16:50.500 --> 00:16:52.920
and then I'm just going to do bracket

334
00:16:52.920 --> 00:16:56.660
bracket, and here, we're going to do perms

335
00:16:56.660 --> 00:17:00.340
.append, and then we're just going to add

336
00:17:00.340 --> 00:17:10.780
cars I, plus cars J, plus

337
00:17:10.780 --> 00:17:20.319
cars K, and then we should be good.

338
00:17:20.440 --> 00:17:21.200
Ah, we need the prefix.

339
00:17:22.819 --> 00:17:29.100
So, prefix plus this, and then at the

340
00:17:29.100 --> 00:17:31.980
end, once it's done that, we can do

341
00:17:31.980 --> 00:17:34.100
for perm in perms.

342
00:17:36.140 --> 00:17:38.020
Ah, God, this keyboard is crazy.

343
00:17:38.280 --> 00:17:40.260
I changed my keyboard recently, unfortunately.

344
00:17:40.900 --> 00:17:43.900
Print perm.

345
00:17:43.900 --> 00:17:46.700
So, let's just have a look, and then

346
00:17:46.700 --> 00:17:51.280
we need to base64 encode, and I can't

347
00:17:51.280 --> 00:17:52.720
remember how to do that off the top

348
00:17:52.720 --> 00:17:53.500
of my head.

349
00:17:54.280 --> 00:17:56.560
So, I can't remember.

350
00:17:56.800 --> 00:17:58.960
So, what we'll do, actually, is we'll use

351
00:17:58.960 --> 00:17:59.880
a perp suite option.

352
00:18:00.120 --> 00:18:01.040
I'm just going to leave it for now

353
00:18:01.040 --> 00:18:04.360
because we'll need it later on, but in

354
00:18:04.360 --> 00:18:07.000
the payloads here, you can see payload processing,

355
00:18:07.620 --> 00:18:10.160
and we can add a rule to encode

356
00:18:10.160 --> 00:18:11.000
our payload.

357
00:18:11.280 --> 00:18:14.320
So, let's just use that for the time

358
00:18:14.320 --> 00:18:16.660
being, and we'll do this again in a

359
00:18:16.660 --> 00:18:16.960
second.

360
00:18:17.680 --> 00:18:21.500
So, I'll just save this, and let's just

361
00:18:21.500 --> 00:18:24.900
close it, and then Python 3, tokens.py.

362
00:18:25.340 --> 00:18:27.900
Looks like that worked successfully.

363
00:18:28.780 --> 00:18:32.020
So, let's do the same again, and just

364
00:18:32.020 --> 00:18:37.020
output this to tokens.txt, and then come

365
00:18:37.020 --> 00:18:40.400
back into perp suites, and load in.

366
00:18:41.780 --> 00:18:48.420
We'll go to home, Kali, wherever we were

367
00:18:48.420 --> 00:18:52.020
in temp, and then we have tokens.txt,

368
00:18:52.320 --> 00:18:55.180
and here we have all of our tokens.

369
00:18:56.580 --> 00:18:59.520
And actually, we made a mistake, or I

370
00:18:59.520 --> 00:19:01.260
say we, I made a mistake.

371
00:19:01.780 --> 00:19:06.400
This needs to be Jeremy, not admin, before

372
00:19:06.400 --> 00:19:07.840
I do that.

373
00:19:07.960 --> 00:19:09.780
So, I'm just going to overwrite the tokens

374
00:19:09.780 --> 00:19:13.640
file, clear these, load it again.

375
00:19:15.320 --> 00:19:15.560
Whoops.

376
00:19:16.260 --> 00:19:20.500
I loaded the Python file.

377
00:19:21.100 --> 00:19:23.100
So, tokens.txt, and we have our Jeremy

378
00:19:23.100 --> 00:19:23.740
tokens.

379
00:19:24.540 --> 00:19:26.900
All right, and let's add our payload processing.

380
00:19:27.440 --> 00:19:30.160
So, we want to encode, and then we

381
00:19:30.160 --> 00:19:33.820
want to base64 encode, and click okay, and

382
00:19:33.820 --> 00:19:34.740
let's start the attack.

383
00:19:36.920 --> 00:19:43.200
You see, we have about 35,000 items

384
00:19:43.200 --> 00:19:45.320
in our attack.

385
00:19:46.520 --> 00:19:49.040
What I want to look for is different

386
00:19:49.040 --> 00:19:50.420
length.

387
00:19:50.420 --> 00:20:00.490
All right,

388
00:20:00.550 --> 00:20:02.270
looks like I messed it up.

389
00:20:02.970 --> 00:20:04.550
So, let me clear this quickly.

390
00:20:05.870 --> 00:20:10.950
Reset the payload position, sorry about that, and

391
00:20:10.950 --> 00:20:12.470
start the attack again.

392
00:20:15.790 --> 00:20:17.870
So, here, yes, because I only set one

393
00:20:17.870 --> 00:20:22.470
payload position, we have much less requests.

394
00:20:23.650 --> 00:20:24.590
Fewer requests.

395
00:20:26.070 --> 00:20:28.470
And then we can go and check the

396
00:20:28.470 --> 00:20:31.730
length, and we can see that, yes, so

397
00:20:31.730 --> 00:20:33.890
sending a blank request obviously had a different

398
00:20:33.890 --> 00:20:37.330
length to an invalid token, but we can

399
00:20:37.330 --> 00:20:41.890
see request 3800 with this one here, so

400
00:20:41.890 --> 00:20:45.410
I'm just going to copy this, and if

401
00:20:45.410 --> 00:20:47.890
we actually look at the response, we can

402
00:20:47.890 --> 00:20:51.130
just see, welcome, Jeremy, and says, hey, nice

403
00:20:51.130 --> 00:20:54.750
work, your flag is TCM, and we can

404
00:20:54.750 --> 00:20:56.850
verify this, so we can just update our

405
00:20:56.850 --> 00:20:57.990
access token here.

406
00:20:58.510 --> 00:21:01.310
Note that the percentage 3D are just equal

407
00:21:01.310 --> 00:21:04.250
signs, so I think this should work, because

408
00:21:04.250 --> 00:21:06.790
that's just URL encoding, so let's try.

409
00:21:07.610 --> 00:21:10.470
Yes, we get welcome, Jeremy, and we get

410
00:21:10.470 --> 00:21:11.290
our flag.

411
00:21:12.050 --> 00:21:14.810
So, yes, I think if you do see

412
00:21:14.810 --> 00:21:19.530
something like this, it's probably also going to

413
00:21:19.530 --> 00:21:19.870
work.

414
00:21:20.330 --> 00:21:21.650
Yes, so we're all good.

415
00:21:22.070 --> 00:21:24.350
It's just a little bit of URL encoding

416
00:21:24.350 --> 00:21:25.090
quirks there.

417
00:21:26.230 --> 00:21:30.570
All right, so next up, we need to

418
00:21:30.570 --> 00:21:36.290
update our code quickly, so that we have

419
00:21:36.290 --> 00:21:39.890
base64, and then we're going to pass it

420
00:21:39.890 --> 00:21:45.170
into ffuf.

421
00:21:46.010 --> 00:21:51.650
I realise this text is really small, sorry

422
00:21:51.650 --> 00:21:53.070
about that if you were looking at that

423
00:21:53.070 --> 00:21:57.190
earlier, and then we've already imported base64, so

424
00:21:57.190 --> 00:22:00.130
what we can do is just do base64

425
00:22:00.130 --> 00:22:07.650
.encode, and I think it's base64

426
00:22:07.650 --> 00:22:17.380
.base64.encode like this,

427
00:22:17.380 --> 00:22:23.440
and then we do .encode here, if I

428
00:22:23.440 --> 00:22:23.840
recall.

429
00:22:24.060 --> 00:22:24.800
Let's try it.

430
00:22:28.840 --> 00:22:30.960
Let's just run it and see.

431
00:22:31.260 --> 00:22:31.900
Ah, we get an error.

432
00:22:33.720 --> 00:22:36.860
Ah, my brackets are off, so let's try

433
00:22:36.860 --> 00:22:37.340
this again.

434
00:22:52.570 --> 00:22:54.630
All right, that looks like what we want,

435
00:22:54.730 --> 00:23:01.650
but it is a byte string, so I

436
00:23:01.650 --> 00:23:03.950
just did a quick Google, and, yes, I

437
00:23:03.950 --> 00:23:06.010
just need to add the decode, which I'd

438
00:23:06.010 --> 00:23:07.110
totally forgotten about.

439
00:23:07.750 --> 00:23:12.290
So, if we have this here, and then

440
00:23:12.290 --> 00:23:26.300
we have encode.decode here, we

441
00:23:26.300 --> 00:23:27.340
should be good to go.

442
00:23:28.120 --> 00:23:28.880
All right.

443
00:23:30.300 --> 00:23:34.840
So, let's put this out to tokens.text,

444
00:23:35.380 --> 00:23:39.260
and then let's do ffuf again.

445
00:23:42.700 --> 00:23:49.400
So, we want to do ffuf-request, and

446
00:23:49.400 --> 00:23:52.860
then we need our request.txt, so let's

447
00:23:52.860 --> 00:23:53.940
grab that.

448
00:23:53.940 --> 00:23:56.760
Oops.

449
00:24:03.010 --> 00:24:13.730
So, rm.req.txt. And here, we

450
00:24:13.730 --> 00:24:21.090
want to fuzz this request, and then ffuf

451
00:24:21.090 --> 00:24:29.970
-request.txt, and then request, oops, proto HTTP,

452
00:24:30.710 --> 00:24:32.870
and then dash W.

453
00:24:34.230 --> 00:24:41.050
We want, oops, tokens.txt, and then we

454
00:24:41.050 --> 00:24:42.670
also, I'm going to run it for a

455
00:24:42.670 --> 00:24:44.750
second, and then we're going to look at

456
00:24:47.350 --> 00:24:49.930
the response length, and then we're going to

457
00:24:49.930 --> 00:24:51.670
filter out the response length.

458
00:24:51.990 --> 00:24:57.610
So, if I just cancel this very quickly,

459
00:24:57.850 --> 00:25:01.150
and then the size here, we're just going

460
00:25:01.150 --> 00:25:03.730
to grab 384, and then we're just going

461
00:25:03.730 --> 00:25:08.350
to do dash FC, sorry, 834, not 384.

462
00:25:09.750 --> 00:25:11.490
Oops, that didn't work.

463
00:25:12.050 --> 00:25:13.310
Oh, it's FS, not FC.

464
00:25:14.490 --> 00:25:15.350
There we go.

465
00:25:16.350 --> 00:25:18.750
And we got it here, so this looks

466
00:25:18.750 --> 00:25:20.150
like our token.

467
00:25:20.490 --> 00:25:22.150
So, let's just check it.

468
00:25:22.610 --> 00:25:26.830
So, we can echo dash N, and then

469
00:25:26.830 --> 00:25:30.990
echo this to base64 dash decode.

470
00:25:31.390 --> 00:25:34.670
So, FQD looks like the same one as

471
00:25:34.670 --> 00:25:37.770
last time, but what we'll do is we'll

472
00:25:37.770 --> 00:25:42.370
just remove this, refresh the page, we're not

473
00:25:42.370 --> 00:25:47.790
logged in, add a token, call it access,

474
00:25:48.570 --> 00:25:53.390
hit save, refresh the page, and we've solved

475
00:25:53.390 --> 00:25:54.290
this lab.

476
00:25:54.550 --> 00:25:55.210
Good job.

477
00:25:56.350 --> 00:25:58.410
So, sorry, that might have been a little

478
00:25:58.410 --> 00:26:01.110
bit jittery along the way, but hopefully you

479
00:26:01.110 --> 00:26:04.210
got some insight into my troubleshooting process when

480
00:26:04.210 --> 00:26:06.090
I'm working on web applications.

481
00:26:06.910 --> 00:26:08.450
And that's it for this module.

482
00:26:08.990 --> 00:26:11.450
Authentication is not an easy topic, and there's

483
00:26:11.450 --> 00:26:13.130
still a lot to learn, but I really

484
00:26:13.130 --> 00:26:15.630
hope that you've gotten a good foundation that

485
00:26:15.630 --> 00:26:17.710
you can continue to expand on.

486
00:26:18.630 --> 00:26:20.350
Great job, and I'll see you in the

487
00:26:20.350 --> 00:26:20.830
next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: Injection

WEBVTT

1
00:00:00.760 --> 00:00:03.460
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Realistically speaking, injection attacks against APIs are not

2
00:00:03.460 --> 00:00:05.740
that different from traditional applications.

3
00:00:06.380 --> 00:00:09.440
However, unprotected APIs are often exposed when they

4
00:00:09.440 --> 00:00:11.960
shouldn't be, and the defense in depth principle

5
00:00:11.960 --> 00:00:14.000
is not always adhered to.

6
00:00:14.480 --> 00:00:17.680
So we can often find APIs with injection

7
00:00:17.680 --> 00:00:18.880
vulnerabilities present.

8
00:00:19.360 --> 00:00:22.560
Also, we should consider that NoSQL is becoming

9
00:00:22.560 --> 00:00:25.220
increasingly popular, and therefore we need to be

10
00:00:25.220 --> 00:00:27.480
able to not just find and exploit traditional

11
00:00:27.480 --> 00:00:32.000
SQL injection vulnerabilities, but also NoSQL injection vulnerabilities

12
00:00:32.000 --> 00:00:32.740
as well.

13
00:00:33.460 --> 00:00:35.060
We'll look at how to fuzz for these

14
00:00:35.060 --> 00:00:37.660
vulnerabilities in APIs and how to exploit them.

15
00:00:38.020 --> 00:00:40.000
This will give you a methodology to start

16
00:00:40.000 --> 00:00:41.120
using going forward.

17
00:00:41.680 --> 00:00:44.220
However, I strongly recommend that you continue your

18
00:00:44.220 --> 00:00:46.680
learning journey after the course, as there's always

19
00:00:46.680 --> 00:00:47.480
more to learn.

20
00:00:48.460 --> 00:00:50.260
Oh, and we'll be taking a quick look

21
00:00:50.260 --> 00:00:52.200
at getting up and running with the popular

22
00:00:52.200 --> 00:00:53.820
tool SQL Map as well.

23
00:00:54.120 --> 00:00:55.960
After this section, we'll be entering the mid

24
00:00:55.960 --> 00:00:56.840
-course capstone.

25
00:00:57.220 --> 00:00:59.100
So this will let you test what you've

26
00:00:59.100 --> 00:01:00.900
learned so far in the course and give

27
00:01:00.900 --> 00:01:02.440
you a chance to start dialing in your

28
00:01:02.440 --> 00:01:03.019
methodology.

29
00:01:03.640 --> 00:01:05.240
I recommend you treat this like a real

30
00:01:05.240 --> 00:01:07.120
-world engagement to get the most out of

31
00:01:07.120 --> 00:01:07.860
the exercise.

32
00:01:08.260 --> 00:01:10.000
Let's dive into our injection module.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.220 --> 00:00:01.620
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Before I give you a live demo and

2
00:00:01.620 --> 00:00:04.060
a challenge, let's walk through some theory of

3
00:00:04.060 --> 00:00:05.460
traditional SQL injection.

4
00:00:05.980 --> 00:00:09.340
In a nutshell, SQL injection lets us manipulate

5
00:00:09.340 --> 00:00:12.240
or change SQL queries that are made to

6
00:00:12.240 --> 00:00:12.780
a database.

7
00:00:13.680 --> 00:00:16.000
For example, if we have a simple SQL

8
00:00:16.000 --> 00:00:19.000
statement, our input might change it so that

9
00:00:19.000 --> 00:00:20.300
it returns a different result.

10
00:00:20.720 --> 00:00:24.320
Here we have select all from messages, where

11
00:00:24.320 --> 00:00:25.900
sender equals the username.

12
00:00:26.440 --> 00:00:28.640
So in our case, if our username is

13
00:00:28.640 --> 00:00:31.619
Jeremy, we have select all from messages where

14
00:00:31.619 --> 00:00:33.020
sender equals Jeremy.

15
00:00:33.640 --> 00:00:35.860
So this will return all of the messages

16
00:00:35.860 --> 00:00:37.820
where Jeremy is the sender.

17
00:00:38.560 --> 00:00:41.320
If we change this, if we can inject

18
00:00:41.320 --> 00:00:45.100
our own value into the username parameter, we

19
00:00:45.100 --> 00:00:47.800
might get something like select all from messages

20
00:00:47.800 --> 00:00:51.640
where sender equals Jeremy or sender equals admin.

21
00:00:52.260 --> 00:00:54.260
And of course, this will return all of

22
00:00:54.260 --> 00:00:57.080
the messages where the sender is Jeremy or

23
00:00:57.080 --> 00:00:58.840
the sender is the administrator.

24
00:01:00.140 --> 00:01:01.980
Fundamentally, it's really that simple.

25
00:01:02.460 --> 00:01:04.820
The situation becomes more complex when we have

26
00:01:04.820 --> 00:01:06.620
things like input filtering that we need to

27
00:01:06.620 --> 00:01:06.900
bypass.

28
00:01:07.400 --> 00:01:10.100
In this case, we can't simply assume our

29
00:01:10.100 --> 00:01:12.860
input is being directly appended to the SQL

30
00:01:12.860 --> 00:01:13.340
query.

31
00:01:14.260 --> 00:01:17.360
Different databases also have slightly different syntaxes, so

32
00:01:17.360 --> 00:01:20.120
enumerating the underlying technology is also part of

33
00:01:20.120 --> 00:01:20.800
our process.

34
00:01:21.520 --> 00:01:24.040
Sometimes a query will trigger an action that

35
00:01:24.040 --> 00:01:26.500
is not visible to us, so we're unsure

36
00:01:26.500 --> 00:01:28.020
whether it actually worked or not.

37
00:01:28.420 --> 00:01:30.220
This is called blind SQL injection.

38
00:01:30.960 --> 00:01:32.740
But don't worry, as long as we have

39
00:01:32.740 --> 00:01:35.280
solid fundamentals, take the time to understand what

40
00:01:35.280 --> 00:01:37.420
we see in practice will be successful.

41
00:01:38.060 --> 00:01:39.940
In this module, we're going to look at

42
00:01:39.940 --> 00:01:41.840
a few common ways to find and exploit

43
00:01:41.840 --> 00:01:42.680
SQL injection.

44
00:01:42.940 --> 00:01:46.300
We'll cover fuzzing for SQL injection, triggering error

45
00:01:46.300 --> 00:01:50.400
messages, verifying our SQL injection attack, using a

46
00:01:50.400 --> 00:01:53.120
union select attack to steal data from other

47
00:01:53.120 --> 00:01:53.660
tables.

48
00:01:54.180 --> 00:01:55.900
We'll then look at the logic of a

49
00:01:55.900 --> 00:01:59.540
common authentication bypass, and then of course, we'll

50
00:01:59.540 --> 00:02:02.160
also look at NoSQL injection too.

51
00:02:02.540 --> 00:02:03.560
I'll see you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.380 --> 00:00:02.200
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, so let's dive in.

2
00:00:02.360 --> 00:00:05.360
I'm here in my labs folder and we

3
00:00:05.360 --> 00:00:09.720
have the api-injection.zip, so I'm just

4
00:00:09.720 --> 00:00:15.020
going to unzip api-injection.zip, hit enter,

5
00:00:15.440 --> 00:00:17.940
and then you'll see that it created an

6
00:00:17.940 --> 00:00:19.920
api-injection folder.

7
00:00:20.520 --> 00:00:25.260
So, whoops, we'll just come into this and

8
00:00:25.260 --> 00:00:28.140
have a look, and then we'll just sudo

9
00:00:28.140 --> 00:00:34.160
docker-compose up, and this should build the

10
00:00:34.160 --> 00:00:35.860
image for us if it's not already built,

11
00:00:36.320 --> 00:00:39.220
and it will spin up our challenge.

12
00:00:45.640 --> 00:00:49.840
And then we come to localhost, turn off

13
00:00:49.840 --> 00:00:54.620
our proxy, and we have our lab.

14
00:00:55.040 --> 00:00:56.560
And you can see, you might get this

15
00:00:56.560 --> 00:00:59.400
message saying test data inserted successfully.

16
00:00:59.620 --> 00:01:02.400
This is just the initial populating the database

17
00:01:02.400 --> 00:01:05.500
with some products and some users and things

18
00:01:05.500 --> 00:01:07.460
like that, so when you refresh again, that

19
00:01:07.460 --> 00:01:08.360
should disappear.

20
00:01:08.920 --> 00:01:10.500
It's just a little script that I added

21
00:01:10.500 --> 00:01:12.260
so that we didn't have to manually set

22
00:01:12.260 --> 00:01:12.920
up the database.

23
00:01:14.080 --> 00:01:16.520
So, first thing I want to do is

24
00:01:16.520 --> 00:01:18.780
I'm going to open up burp suite, and

25
00:01:18.780 --> 00:01:20.140
we're going to do this two ways.

26
00:01:20.240 --> 00:01:22.560
Again, we're going to fuzz for SQL injection

27
00:01:22.560 --> 00:01:25.300
using burp suite first, so that I can

28
00:01:25.300 --> 00:01:26.460
show you, and you can do this on

29
00:01:26.460 --> 00:01:28.620
the community edition as well, just know that

30
00:01:28.620 --> 00:01:30.080
it's going to be rate limited, so it's

31
00:01:30.080 --> 00:01:31.900
going to be a little bit slower, and

32
00:01:31.900 --> 00:01:34.300
then we'll do the same thing with another

33
00:01:34.300 --> 00:01:35.380
tool as well.

34
00:01:36.440 --> 00:01:38.940
So, what I'm going to do is when

35
00:01:38.940 --> 00:01:42.120
we come to our SQL injection demo, get

36
00:01:42.120 --> 00:01:44.560
coffee by roast level, I'm going to follow

37
00:01:44.560 --> 00:01:47.420
what I usually follow on any web application

38
00:01:47.420 --> 00:01:49.260
assessment, which is I'm going to test the

39
00:01:49.260 --> 00:01:49.780
functionality.

40
00:01:50.480 --> 00:01:53.080
Usually, when I come to a web application,

41
00:01:53.360 --> 00:01:55.380
I'll go in and I'll step through everything.

42
00:01:55.840 --> 00:01:58.080
I'll send messages, I'll log in, I'll create

43
00:01:58.080 --> 00:02:01.220
users, multiple users, and I'll make sure that

44
00:02:01.220 --> 00:02:03.640
I understand how the website functions and what

45
00:02:03.640 --> 00:02:06.220
it's meant to do, what normal behavior looks

46
00:02:06.220 --> 00:02:06.500
like.

47
00:02:07.320 --> 00:02:08.800
In this case, we're just going to test

48
00:02:08.800 --> 00:02:11.980
this, and we press three, or enter three,

49
00:02:12.260 --> 00:02:13.700
and we get a coffee back.

50
00:02:13.980 --> 00:02:16.820
So, the coffee ID is five, the origin

51
00:02:16.820 --> 00:02:19.560
is Guatemala, and the roast level is three,

52
00:02:19.880 --> 00:02:22.120
and we can check for other roast levels

53
00:02:22.120 --> 00:02:24.480
as well, so four, we don't get anything

54
00:02:24.480 --> 00:02:28.400
back, five, we get two, so some Ethiopian

55
00:02:28.400 --> 00:02:31.980
coffee and some coffee from Indonesia as well.

56
00:02:33.760 --> 00:02:36.020
So, I'm just going to switch on my

57
00:02:36.020 --> 00:02:39.780
proxy, and then we're going to just send

58
00:02:39.780 --> 00:02:42.160
this request again, so that we capture it,

59
00:02:42.820 --> 00:02:46.720
come back to here, proxy, HTTP history, and

60
00:02:46.720 --> 00:02:49.320
we can see the request in Burp Suites.

61
00:02:50.160 --> 00:02:51.920
So, there's two ways we can do this.

62
00:02:52.020 --> 00:02:54.340
One is manual testing, and the second is

63
00:02:54.340 --> 00:02:54.820
fuzzing.

64
00:02:55.280 --> 00:02:56.920
So, what I'm going to do is, I'm

65
00:02:56.920 --> 00:02:59.160
going to fuzz first, so I'm going to

66
00:02:59.160 --> 00:03:01.120
press control-I, and you can see that

67
00:03:01.120 --> 00:03:03.620
I've sent it to Intruder, or you can

68
00:03:03.620 --> 00:03:06.520
right-click, send to Intruder, and then you

69
00:03:06.520 --> 00:03:08.800
can see that it automatically detects where I

70
00:03:08.800 --> 00:03:10.560
want to put my payload, which is good.

71
00:03:10.560 --> 00:03:13.720
I'm going to use the sniper, come to

72
00:03:13.720 --> 00:03:16.820
payloads, and then we have a choice of

73
00:03:16.820 --> 00:03:17.300
lists.

74
00:03:17.660 --> 00:03:20.300
Now, word lists are a personal preference.

75
00:03:20.600 --> 00:03:23.140
I definitely recommend testing out different word lists,

76
00:03:23.520 --> 00:03:25.360
see what has good results for you, see

77
00:03:25.360 --> 00:03:28.600
where their shortcomings are, and even develop your

78
00:03:28.600 --> 00:03:28.860
own.

79
00:03:29.220 --> 00:03:32.560
So, concatenate some word lists together, make some

80
00:03:32.560 --> 00:03:34.660
shorter if you think they're too long, and

81
00:03:34.660 --> 00:03:35.600
things like this.

82
00:03:35.920 --> 00:03:38.780
So, we have a few built into Burp

83
00:03:38.780 --> 00:03:39.300
Suite already.

84
00:03:39.500 --> 00:03:42.440
So, we have fuzzing, quick, full, usernames, passwords,

85
00:03:42.740 --> 00:03:44.220
and what we want to do is, we

86
00:03:44.220 --> 00:03:45.640
want to scroll down, and we want to

87
00:03:45.640 --> 00:03:46.860
come to SQL injection.

88
00:03:46.860 --> 00:03:48.720
So, you can see that there are a

89
00:03:48.720 --> 00:03:52.100
bunch of basic SQL injection payloads here as

90
00:03:52.100 --> 00:03:54.400
well, and all I'm going to do is

91
00:03:54.400 --> 00:03:57.460
hit start attack, and obviously, we're running locally,

92
00:03:57.620 --> 00:03:59.660
so it's very, very quick, and if you're

93
00:03:59.660 --> 00:04:01.640
on the community edition, this will take some

94
00:04:01.640 --> 00:04:04.240
time, and the fact that we're getting all

95
00:04:04.240 --> 00:04:07.740
sorts of different lengths in the response, and

96
00:04:07.740 --> 00:04:09.680
we're getting some different response codes, so we're

97
00:04:09.680 --> 00:04:13.360
getting 401 and 200s, this is an indication

98
00:04:13.360 --> 00:04:17.100
that we do indeed have some SQL injection

99
00:04:17.100 --> 00:04:17.779
vulnerability.

100
00:04:18.660 --> 00:04:19.899
So, if we have a look at the

101
00:04:19.899 --> 00:04:23.420
response here, we get unauthorized, no coffee found,

102
00:04:25.340 --> 00:04:28.080
and if we keep going down, we get

103
00:04:28.080 --> 00:04:33.260
this is just a blank response, and then

104
00:04:33.260 --> 00:04:37.080
this looks like we've got an error, which

105
00:04:37.080 --> 00:04:39.780
is a really telling thing for SQL injection.

106
00:04:40.100 --> 00:04:42.280
If you can throw a database error, the

107
00:04:42.280 --> 00:04:44.440
chances are you've got SQL injection.

108
00:04:45.000 --> 00:04:47.920
Obviously, in a lot of production environments, you're

109
00:04:47.920 --> 00:04:49.760
not going to have error messages switched on

110
00:04:49.760 --> 00:04:51.260
like this, or you won't have verbose error

111
00:04:51.260 --> 00:04:54.440
messages, you might get something generic back, but

112
00:04:54.440 --> 00:04:57.300
the even if it doesn't say fatal error,

113
00:04:57.440 --> 00:05:02.660
SQL exception, even if it comes back saying,

114
00:05:02.860 --> 00:05:05.780
hey, there was an error, versus your blank

115
00:05:05.780 --> 00:05:07.920
payload where there's no error, that could be

116
00:05:07.920 --> 00:05:10.180
an indication that we have SQL injection.

117
00:05:11.800 --> 00:05:13.400
And it gives us a stack trace, which

118
00:05:13.400 --> 00:05:14.000
is quite nice.

119
00:05:14.100 --> 00:05:16.160
This is good for troubleshooting if you're in

120
00:05:16.160 --> 00:05:17.200
a more complex scenario.

121
00:05:17.940 --> 00:05:21.400
And then we also get 1 or 7

122
00:05:21.400 --> 00:05:22.200
equals 7.

123
00:05:22.840 --> 00:05:26.280
So, this is a good indication that if

124
00:05:26.280 --> 00:05:28.480
we look for a coffee where the roast

125
00:05:28.480 --> 00:05:30.700
level is 1, or 7 equals 7 is

126
00:05:30.700 --> 00:05:33.280
a true statement, if we change this to

127
00:05:33.280 --> 00:05:37.200
7 equals 6, the DB shouldn't return any

128
00:05:37.200 --> 00:05:37.560
results.

129
00:05:37.720 --> 00:05:39.660
So, we're testing for true false statements, which

130
00:05:39.660 --> 00:05:40.680
is a great way to test.

131
00:05:40.780 --> 00:05:42.360
And we'll look at that in a second

132
00:05:42.360 --> 00:05:43.240
as well.

133
00:05:43.940 --> 00:05:47.260
So, just looking through the results, basically, you

134
00:05:47.260 --> 00:05:50.040
can be pretty sure that we are, indeed,

135
00:05:50.180 --> 00:05:52.120
vulnerable to SQL injection.

136
00:05:53.660 --> 00:05:55.880
So, let's switch over to manual testing.

137
00:05:56.460 --> 00:05:58.680
And we'll come back and we'll do it

138
00:05:58.680 --> 00:06:01.120
as though we didn't already fuzz and we

139
00:06:01.120 --> 00:06:03.120
don't already know that there is injection there.

140
00:06:03.240 --> 00:06:05.500
So, control R to send to repeater.

141
00:06:06.280 --> 00:06:08.520
And all I'm going to do is I'm

142
00:06:08.520 --> 00:06:10.280
going to send this as my initial request.

143
00:06:10.960 --> 00:06:11.980
And I'm going to pay attention.

144
00:06:12.240 --> 00:06:14.300
So, 159 is the content length.

145
00:06:14.780 --> 00:06:16.140
And we get two results back.

146
00:06:16.400 --> 00:06:19.420
So, it's a good idea to familiarize yourself

147
00:06:19.420 --> 00:06:21.660
with what a normal payload looks like and

148
00:06:21.660 --> 00:06:23.200
what a normal response looks like.

149
00:06:24.620 --> 00:06:26.600
So, now, I'm going to add a single

150
00:06:26.600 --> 00:06:29.120
quote because a lot of SQL queries will

151
00:06:29.120 --> 00:06:32.160
use quotes around their variables or their input.

152
00:06:32.760 --> 00:06:35.120
And so, sending a single quote or a

153
00:06:35.120 --> 00:06:37.600
double quote can break the SQL and that

154
00:06:37.600 --> 00:06:38.480
can trigger an error.

155
00:06:38.660 --> 00:06:40.260
So, this is a really simple way of

156
00:06:40.260 --> 00:06:41.520
testing for SQL injection.

157
00:06:42.380 --> 00:06:44.300
And you notice that, yeah, we get a

158
00:06:44.300 --> 00:06:48.260
fatal error because we've basically interrupted the query

159
00:06:48.260 --> 00:06:50.920
syntax and we've broken it and the database

160
00:06:50.920 --> 00:06:53.560
no longer understands this syntax.

161
00:06:54.560 --> 00:06:57.580
And we can also do things like where

162
00:06:57.580 --> 00:07:01.000
we saw all one equals seven equals seven,

163
00:07:01.160 --> 00:07:03.240
we can do all one equals one to

164
00:07:03.240 --> 00:07:05.400
test whether we have true false statements.

165
00:07:05.540 --> 00:07:07.780
So, I need to URL encode this because

166
00:07:07.780 --> 00:07:09.940
spaces in the request line here are very

167
00:07:09.940 --> 00:07:10.340
important.

168
00:07:11.340 --> 00:07:13.600
And you can see that we get more

169
00:07:13.600 --> 00:07:14.340
results back.

170
00:07:14.460 --> 00:07:15.740
So, our content length is higher.

171
00:07:16.020 --> 00:07:18.360
And we get one, two, three, four, five

172
00:07:18.360 --> 00:07:19.080
coffees back.

173
00:07:19.660 --> 00:07:22.020
And so, what we're saying here is select

174
00:07:22.020 --> 00:07:25.720
all from coffee where roast equals five or

175
00:07:25.720 --> 00:07:26.860
one equals one.

176
00:07:27.280 --> 00:07:29.340
And because one equals one is true, it's

177
00:07:29.340 --> 00:07:30.140
selecting all.

178
00:07:30.260 --> 00:07:31.880
So, this is forcing a true statement.

179
00:07:32.660 --> 00:07:34.580
And if we change this to, let's say,

180
00:07:34.640 --> 00:07:39.120
one equals two, we only get the ones

181
00:07:39.120 --> 00:07:41.180
that were originally selected back.

182
00:07:41.500 --> 00:07:45.120
So, select all from coffee where roast level

183
00:07:45.120 --> 00:07:48.100
equals five or one equals two.

184
00:07:48.340 --> 00:07:50.260
So, the roast level equals five is the

185
00:07:50.260 --> 00:07:50.740
true part.

186
00:07:50.840 --> 00:07:52.940
So, it's selecting those still and then not

187
00:07:52.940 --> 00:07:56.000
returning the false statement and the false part

188
00:07:56.000 --> 00:07:56.680
of the statement.

189
00:07:57.180 --> 00:07:58.800
And we'll use this again later on for

190
00:07:58.800 --> 00:08:00.140
the authentication bypass.

191
00:08:00.540 --> 00:08:02.100
This is also a technique that can be

192
00:08:02.100 --> 00:08:04.220
used when we're dealing with blind SQL injection,

193
00:08:04.380 --> 00:08:06.240
which we'll briefly talk about later on.

194
00:08:08.580 --> 00:08:09.000
All right.

195
00:08:09.100 --> 00:08:12.580
So, now we have SQL injection.

196
00:08:12.760 --> 00:08:14.480
What can we actually do with this?

197
00:08:14.920 --> 00:08:17.760
Well, one attack is union select.

198
00:08:18.320 --> 00:08:21.240
And what union select does is it allows

199
00:08:21.240 --> 00:08:24.980
us to grab data from different tables, which

200
00:08:24.980 --> 00:08:27.640
is very useful as a database administrator.

201
00:08:28.740 --> 00:08:30.760
And in this case, I'm going to tell

202
00:08:30.760 --> 00:08:32.380
you that there is a users table.

203
00:08:33.000 --> 00:08:35.460
And in the users table, there are users

204
00:08:35.460 --> 00:08:36.960
with a username and password.

205
00:08:37.559 --> 00:08:40.299
And so, instead of just returning the ID,

206
00:08:40.460 --> 00:08:44.080
name, origin, roast level, what we also want

207
00:08:44.080 --> 00:08:51.930
to return is union select username, password from

208
00:08:51.930 --> 00:08:52.610
users.

209
00:08:53.630 --> 00:08:57.310
So, it's saying select all from coffee where

210
00:08:57.310 --> 00:09:00.870
the roast level equals five and also select

211
00:09:00.870 --> 00:09:04.310
the username and password from the table users.

212
00:09:04.690 --> 00:09:06.050
That's what this statement means.

213
00:09:06.610 --> 00:09:10.890
And this actually probably won't work because when

214
00:09:10.890 --> 00:09:14.050
you do union select, there is a constraint.

215
00:09:14.410 --> 00:09:16.910
You must select the same number of columns

216
00:09:16.910 --> 00:09:18.490
as your original query.

217
00:09:18.750 --> 00:09:21.090
And you'll notice that here, we're selecting one,

218
00:09:21.490 --> 00:09:23.150
two, three, four columns.

219
00:09:23.730 --> 00:09:26.010
And afterwards, we're only selecting two columns.

220
00:09:26.150 --> 00:09:28.170
So, let's run this and see what happens.

221
00:09:28.350 --> 00:09:30.550
I'm just going to encode, control U, or

222
00:09:30.550 --> 00:09:34.210
you can right click, convert selection URL, URL

223
00:09:34.210 --> 00:09:35.410
encode key characters.

224
00:09:36.250 --> 00:09:37.150
Hit send.

225
00:09:37.390 --> 00:09:39.690
And we get this error, which we expected.

226
00:09:39.710 --> 00:09:41.690
And you can see that it says different

227
00:09:41.690 --> 00:09:43.290
number of columns.

228
00:09:44.210 --> 00:09:45.970
Now, if we didn't know the number of

229
00:09:45.970 --> 00:09:48.070
columns, we could test.

230
00:09:48.330 --> 00:09:50.190
So, we could just keep adding columns until

231
00:09:50.190 --> 00:09:52.010
we get our results.

232
00:09:52.750 --> 00:09:55.130
But if I just control shift U, by

233
00:09:55.130 --> 00:09:58.070
the way, undoes the URL encoding, we can

234
00:09:58.070 --> 00:10:00.850
add null and we can add null again.

235
00:10:01.350 --> 00:10:04.130
So, we're still selecting four columns, but two

236
00:10:04.130 --> 00:10:05.330
of our columns are null.

237
00:10:05.570 --> 00:10:07.770
We could also select other things that we

238
00:10:07.770 --> 00:10:11.930
want from the table users, such as the

239
00:10:11.930 --> 00:10:12.230
ID.

240
00:10:13.330 --> 00:10:16.570
So, in this case, let's URL encode this

241
00:10:16.570 --> 00:10:16.910
quickly.

242
00:10:18.030 --> 00:10:18.970
Send this.

243
00:10:19.550 --> 00:10:21.450
You can see that we get the coffee

244
00:10:21.450 --> 00:10:25.230
back as expected, but we also get admin

245
00:10:25.230 --> 00:10:28.950
and the admin's password and Jeremy and Jeremy's

246
00:10:28.950 --> 00:10:29.410
password.

247
00:10:30.010 --> 00:10:30.950
And if you want to kind of have

248
00:10:30.950 --> 00:10:32.470
a play with this, for example, if you

249
00:10:32.470 --> 00:10:34.950
change null here, you can kind of see

250
00:10:34.950 --> 00:10:37.610
how if we change the query and I

251
00:10:37.610 --> 00:10:40.490
put the password into the last column here,

252
00:10:41.130 --> 00:10:43.830
the password now appears in the roast level

253
00:10:43.830 --> 00:10:46.410
back here, rather than in the name.

254
00:10:46.410 --> 00:10:49.530
So, hopefully that gives you some understanding as

255
00:10:49.530 --> 00:10:52.170
to what's happening with the SQL query under

256
00:10:52.170 --> 00:10:52.630
the hood.

257
00:10:53.450 --> 00:10:54.890
So, this is a way that we can

258
00:10:54.890 --> 00:10:58.170
go from basic SQL injection to stealing data.

259
00:10:58.350 --> 00:11:00.150
And often, we'd try and steal things like

260
00:11:00.150 --> 00:11:03.130
the administrator password or the password hash, then

261
00:11:03.130 --> 00:11:05.570
go and crack it, or we'd try and

262
00:11:05.570 --> 00:11:08.750
steal other data from the database as well.

263
00:11:09.930 --> 00:11:12.170
And one last thing to consider is that

264
00:11:12.170 --> 00:11:14.830
some databases, we can actually get code execution

265
00:11:14.830 --> 00:11:18.670
from depending on the database user, their privileges,

266
00:11:18.890 --> 00:11:20.850
and how the database has been configured.

267
00:11:21.410 --> 00:11:23.670
Now, I know that's a lot, a lot

268
00:11:23.670 --> 00:11:25.370
to take in, especially if you're new to

269
00:11:25.370 --> 00:11:26.010
SQL injection.

270
00:11:26.270 --> 00:11:29.390
So, I highly recommend going and studying a

271
00:11:29.390 --> 00:11:32.490
little bit more on SQL injection generally, because

272
00:11:32.490 --> 00:11:35.310
it applies just as much to attacking APIs

273
00:11:35.310 --> 00:11:38.450
as it does to attacking traditional web applications.

274
00:11:39.330 --> 00:11:39.630
All right.

275
00:11:39.710 --> 00:11:42.170
So, let's take a quick look at fuzzing

276
00:11:42.170 --> 00:11:45.370
with FFUF, and all we're going to do

277
00:11:45.370 --> 00:11:47.150
is come into here, come into a new

278
00:11:47.150 --> 00:11:49.750
tab, and we're going to do the same

279
00:11:49.750 --> 00:11:52.030
thing as basically what we did in burp

280
00:11:52.030 --> 00:11:52.250
suite.

281
00:11:52.550 --> 00:11:55.930
So, first of all, we actually need this

282
00:11:55.930 --> 00:11:56.390
endpoint.

283
00:11:56.850 --> 00:11:59.070
So, we're going to grab this payload.

284
00:11:59.430 --> 00:12:02.810
So, slash V1, 001.PHP. And we're going

285
00:12:02.810 --> 00:12:07.650
to go FFUF dash U HTTP slash slash

286
00:12:07.650 --> 00:12:11.650
local host, and then, oops, I've got two

287
00:12:11.650 --> 00:12:12.990
slashes here.

288
00:12:13.170 --> 00:12:15.230
And then we're going to change this 5

289
00:12:15.230 --> 00:12:16.470
to fuzz.

290
00:12:16.690 --> 00:12:18.510
Now, because we have a question mark, I

291
00:12:18.510 --> 00:12:20.710
think we're going to need to put this

292
00:12:20.710 --> 00:12:23.750
in quotes, because Bash may not like this

293
00:12:23.750 --> 00:12:25.350
as a special character.

294
00:12:26.530 --> 00:12:27.550
I could be wrong.

295
00:12:27.890 --> 00:12:28.830
You'd have to check.

296
00:12:29.370 --> 00:12:30.930
And for the word list, what we're going

297
00:12:30.930 --> 00:12:33.730
to do is we're going to use I

298
00:12:33.730 --> 00:12:35.550
think there is a word list in cyclists.

299
00:12:36.010 --> 00:12:36.810
So, whoops.

300
00:12:37.650 --> 00:12:41.010
User share cyclists.

301
00:12:41.370 --> 00:12:46.500
And then if we go into fuzzing, and

302
00:12:46.500 --> 00:12:47.800
then there it is.

303
00:12:48.040 --> 00:12:48.600
SQLI.

304
00:12:48.600 --> 00:12:52.980
And then we have some SQLI word lists.

305
00:12:53.880 --> 00:12:57.660
So, let's go for the, oops, generic SQLI.

306
00:12:58.980 --> 00:13:00.540
And see what comes back.

307
00:13:01.180 --> 00:13:03.900
And you can see that it gives us

308
00:13:03.900 --> 00:13:06.920
the payload, and it gives us the status

309
00:13:06.920 --> 00:13:08.300
code and the size.

310
00:13:08.700 --> 00:13:10.620
And again, you can see that the fact

311
00:13:10.620 --> 00:13:13.720
that we're getting lots of different status codes

312
00:13:13.720 --> 00:13:17.500
and we're getting different response sizes probably means

313
00:13:17.500 --> 00:13:19.260
that we have SQL injection.

314
00:13:19.560 --> 00:13:21.920
It's not always the case, because it may

315
00:13:21.920 --> 00:13:23.780
be returning some value back.

316
00:13:23.880 --> 00:13:25.880
It may be saying, hey, this is not

317
00:13:25.880 --> 00:13:27.060
a valid request.

318
00:13:27.320 --> 00:13:29.100
Or, you know, this was rejected.

319
00:13:29.620 --> 00:13:32.140
And then if it includes the text within

320
00:13:32.140 --> 00:13:34.780
the response, the size may be different as

321
00:13:34.780 --> 00:13:34.980
well.

322
00:13:35.080 --> 00:13:37.060
So, you need to go in and verify

323
00:13:37.060 --> 00:13:38.580
that the actually works.

324
00:13:38.880 --> 00:13:40.920
But this is a quick way to understand

325
00:13:40.920 --> 00:13:44.180
whether an endpoint is likely to be vulnerable

326
00:13:44.180 --> 00:13:44.640
or not.

327
00:13:45.020 --> 00:13:47.340
And then you can go in, copy and

328
00:13:47.340 --> 00:13:49.880
paste some of these into burp suite repeater

329
00:13:49.880 --> 00:13:52.540
and test and make sure that it is.

330
00:13:52.940 --> 00:13:53.300
All right.

331
00:13:53.300 --> 00:13:55.980
So, next up, let's take a quick look

332
00:13:55.980 --> 00:13:57.040
at SQL map.

333
00:13:57.760 --> 00:13:58.980
And what I'm going to do is I'm

334
00:13:58.980 --> 00:14:00.400
going to come into burp suite.

335
00:14:00.720 --> 00:14:03.200
I'm just going to grab this request, the

336
00:14:03.200 --> 00:14:06.060
clean request, the one that doesn't have all

337
00:14:06.060 --> 00:14:08.140
of the injection on the end and just

338
00:14:08.140 --> 00:14:09.580
returns a couple of results.

339
00:14:10.580 --> 00:14:11.200
Come back here.

340
00:14:12.080 --> 00:14:14.520
And whatever text editor you want to use,

341
00:14:14.580 --> 00:14:16.920
you can use Vim, Nano, Notepad, doesn't matter.

342
00:14:17.040 --> 00:14:17.640
I like Vim.

343
00:14:17.840 --> 00:14:19.000
So, I'm just going to create a file

344
00:14:19.000 --> 00:14:22.300
called req or request.txt. You can call

345
00:14:22.300 --> 00:14:23.220
it anything you like.

346
00:14:24.200 --> 00:14:24.640
Insert.

347
00:14:24.960 --> 00:14:27.100
And I'm just going to paste this in.

348
00:14:28.220 --> 00:14:30.500
So, if I cap this, you can see

349
00:14:30.500 --> 00:14:30.920
it here.

350
00:14:31.700 --> 00:14:34.000
And all I'm going to do is I'm

351
00:14:34.000 --> 00:14:36.920
going to do SQL map dash R for

352
00:14:36.920 --> 00:14:41.060
request and then pass in the request.txt.

353
00:14:41.280 --> 00:14:43.020
Now, SQL map is quite a powerful tool,

354
00:14:43.320 --> 00:14:44.320
has a lot of options.

355
00:14:44.640 --> 00:14:47.880
So, I definitely recommend dash H, have a

356
00:14:47.880 --> 00:14:49.880
look, see what it can do and do

357
00:14:49.880 --> 00:14:50.400
some study.

358
00:14:50.820 --> 00:14:53.220
But for today, we'll just have a quick

359
00:14:53.220 --> 00:14:53.480
look.

360
00:14:53.980 --> 00:14:55.680
And it's going to ask us some questions.

361
00:14:55.820 --> 00:14:58.360
So, it's saying, it looks like the backend

362
00:14:58.360 --> 00:15:00.260
DB is MySQL.

363
00:15:00.540 --> 00:15:02.620
Do you want to skip payloads for other

364
00:15:02.620 --> 00:15:04.280
specific databases?

365
00:15:04.860 --> 00:15:07.580
So, it's basically saying, I think it's MySQL.

366
00:15:07.960 --> 00:15:09.380
Do you also want to test for Oracle?

367
00:15:09.660 --> 00:15:11.840
Do you also want to test from Microsoft

368
00:15:11.840 --> 00:15:13.580
SQL Server Postgres?

369
00:15:14.100 --> 00:15:16.780
And let's skip because we know that it

370
00:15:16.780 --> 00:15:18.180
is indeed MySQL.

371
00:15:19.240 --> 00:15:21.660
Do you want to include all tests?

372
00:15:22.000 --> 00:15:22.360
Yes.

373
00:15:23.400 --> 00:15:25.620
And then it comes back with not authorized.

374
00:15:25.880 --> 00:15:28.780
Try to provide the right HTTP credentials.

375
00:15:29.620 --> 00:15:31.300
And what we can do is we can

376
00:15:31.300 --> 00:15:33.220
just pass this ignore code.

377
00:15:34.020 --> 00:15:36.420
It's giving us some good advice there.

378
00:15:37.240 --> 00:15:37.460
Oops.

379
00:15:37.960 --> 00:15:39.520
Ignore code 401.

380
00:15:41.180 --> 00:15:43.260
And then we'll just do yes, yes.

381
00:15:43.460 --> 00:15:45.480
So, it's really important to read what's happening.

382
00:15:45.980 --> 00:15:49.740
And different applications will respond in different ways.

383
00:15:49.920 --> 00:15:53.260
In this case, that 401 unauthorized is probably

384
00:15:53.260 --> 00:15:56.160
not the correct response code for what's happening

385
00:15:56.160 --> 00:15:57.360
with the interaction.

386
00:15:58.020 --> 00:16:00.620
But each application will have its quirks, different

387
00:16:00.620 --> 00:16:04.580
response codes, different coding styles, different schemas in

388
00:16:04.580 --> 00:16:05.720
terms of structure.

389
00:16:06.340 --> 00:16:08.620
And this is why manual testing will always

390
00:16:08.620 --> 00:16:11.420
be more effective than automated testing.

391
00:16:11.880 --> 00:16:14.040
So, get parameter roast is vulnerable.

392
00:16:14.240 --> 00:16:16.320
Do you want to keep testing others?

393
00:16:16.540 --> 00:16:17.600
Let's not test.

394
00:16:18.060 --> 00:16:21.040
And then here, it gives us some payloads.

395
00:16:21.420 --> 00:16:24.000
So, it gives us the roast equals 5

396
00:16:24.000 --> 00:16:28.320
and 2373 equals 2373, which we already knew

397
00:16:28.320 --> 00:16:28.560
about.

398
00:16:28.660 --> 00:16:31.580
We saw the 7 equals 7 in our

399
00:16:31.580 --> 00:16:32.280
fuzzing list.

400
00:16:32.400 --> 00:16:34.400
And we also tested 1 equals 1 and

401
00:16:34.400 --> 00:16:35.160
1 equals 2.

402
00:16:35.940 --> 00:16:38.520
And it also has another error based payload

403
00:16:38.520 --> 00:16:41.020
and a time based payload as well.

404
00:16:41.360 --> 00:16:43.940
And I suspect we can actually just verify

405
00:16:43.940 --> 00:16:48.520
this and just go and sleep 10, for

406
00:16:48.520 --> 00:16:48.880
example.

407
00:16:49.600 --> 00:16:51.920
And it should give us 10 seconds before

408
00:16:51.920 --> 00:16:52.560
coming back.

409
00:16:52.780 --> 00:16:54.080
And you can see the fact that it

410
00:16:54.080 --> 00:16:56.860
hung and hasn't given us a response back

411
00:16:56.860 --> 00:16:59.500
does indeed show that we have time based

412
00:16:59.500 --> 00:17:00.400
SQL injection.

413
00:17:01.340 --> 00:17:02.740
I'll give that a few seconds.

414
00:17:03.140 --> 00:17:04.020
Hopefully, it will come back.

415
00:17:06.060 --> 00:17:06.760
There we go.

416
00:17:06.880 --> 00:17:07.180
Eventually.

417
00:17:07.460 --> 00:17:08.560
I think that was a lot more than

418
00:17:08.560 --> 00:17:09.099
10 seconds.

419
00:17:09.240 --> 00:17:09.760
I'm not sure.

420
00:17:10.440 --> 00:17:11.680
But we got a 401.

421
00:17:12.119 --> 00:17:14.540
And again, this is probably the incorrect response

422
00:17:14.540 --> 00:17:16.599
code for what we sent it.

423
00:17:16.859 --> 00:17:20.220
But each application is going to react differently.

424
00:17:21.240 --> 00:17:23.980
And we got a generic union query as

425
00:17:23.980 --> 00:17:24.260
well.

426
00:17:24.460 --> 00:17:27.119
So, here, this is quite a complex looking

427
00:17:27.119 --> 00:17:27.640
query.

428
00:17:28.160 --> 00:17:30.180
But you can use this as a foundation.

429
00:17:30.700 --> 00:17:33.000
So, roast equals 5, union select.

430
00:17:33.400 --> 00:17:36.560
And then we can start building targeted payloads

431
00:17:36.560 --> 00:17:37.440
based off this.

432
00:17:38.100 --> 00:17:40.660
And then one other thing that we can

433
00:17:40.660 --> 00:17:42.980
do is we can do something like dump,

434
00:17:43.580 --> 00:17:45.960
where it's just going to grab all of

435
00:17:45.960 --> 00:17:46.380
the data.

436
00:17:46.660 --> 00:17:49.640
It's going to use those identified vulnerabilities and

437
00:17:49.640 --> 00:17:51.220
it's going to spit out the data from

438
00:17:51.220 --> 00:17:51.680
the database.

439
00:17:52.120 --> 00:17:54.580
So, here we have the two users, admin

440
00:17:54.580 --> 00:17:56.260
and Jeremy, and their passwords.

441
00:17:56.640 --> 00:17:58.740
And we have all of the coffees as

442
00:17:58.740 --> 00:17:59.000
well.

443
00:18:00.280 --> 00:18:03.880
So, SQL map, really powerful tool, really useful,

444
00:18:04.140 --> 00:18:05.480
even if you're just using it for your

445
00:18:05.480 --> 00:18:08.460
initial recon to kind of see what payloads

446
00:18:08.460 --> 00:18:09.000
might work.

447
00:18:09.200 --> 00:18:10.120
And then you tune on that.

448
00:18:10.380 --> 00:18:12.100
Or if you use it just to dump

449
00:18:12.100 --> 00:18:13.880
the database or try and get a shell,

450
00:18:14.120 --> 00:18:16.980
which I don't think this will work.

451
00:18:17.180 --> 00:18:18.580
But let's give it a try.

452
00:18:19.840 --> 00:18:20.360
PHP.

453
00:18:21.600 --> 00:18:25.540
Yeah, unfortunately, because the user on the database

454
00:18:25.540 --> 00:18:28.560
doesn't have write privileges, we can't upload a

455
00:18:28.560 --> 00:18:28.780
shell.

456
00:18:29.020 --> 00:18:30.320
And tells us that here.

457
00:18:30.660 --> 00:18:33.740
So, process user has no write privileges, which

458
00:18:33.740 --> 00:18:34.840
I did on purpose.

459
00:18:35.440 --> 00:18:38.080
The user is only able to read the

460
00:18:38.080 --> 00:18:38.380
database.

461
00:18:38.620 --> 00:18:40.880
It's not able to insert new data, for

462
00:18:40.880 --> 00:18:41.300
example.

463
00:18:42.360 --> 00:18:42.780
All right.

464
00:18:42.860 --> 00:18:44.100
That was quite a lot to get through.

465
00:18:44.400 --> 00:18:46.500
So, don't worry if you need to go

466
00:18:46.500 --> 00:18:47.640
back and rewatch.

467
00:18:48.100 --> 00:18:50.620
Feel free to have a play with SQL

468
00:18:50.620 --> 00:18:54.480
map and burp suite and FFUF yourself.

469
00:18:55.120 --> 00:18:57.340
Doing is always going to help you reinforce

470
00:18:57.340 --> 00:18:58.400
everything you've learned.

471
00:18:58.940 --> 00:19:00.640
And in the next video, we'll have a

472
00:19:00.640 --> 00:19:02.700
look at a common authentication bypass.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.400 --> 00:00:03.059
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, so let's take a quick look

2
00:00:03.059 --> 00:00:05.900
at this login and I'll just move myself

3
00:00:05.900 --> 00:00:06.900
out of the way.

4
00:00:07.660 --> 00:00:08.900
And what we're going to try and do

5
00:00:08.900 --> 00:00:11.800
first is let's just log in as admin

6
00:00:11.800 --> 00:00:14.100
admin, something that's always worth trying.

7
00:00:14.920 --> 00:00:18.180
And we get, sorry, incorrect credentials, but that's

8
00:00:18.180 --> 00:00:18.400
okay.

9
00:00:19.120 --> 00:00:20.060
What we're going to do is we're going

10
00:00:20.060 --> 00:00:22.200
to come over to web suites, come to

11
00:00:22.200 --> 00:00:24.880
our proxy, HTTP history, and we can see

12
00:00:24.880 --> 00:00:29.200
that it's hitting the endpoint 002.php. And

13
00:00:29.200 --> 00:00:32.460
you can see our username and password and

14
00:00:32.460 --> 00:00:34.220
the response that comes back.

15
00:00:34.800 --> 00:00:36.980
So I'm going to send this to repeater.

16
00:00:37.400 --> 00:00:39.380
And we could do the same, we could

17
00:00:39.380 --> 00:00:42.620
send this to intruder, fuzz the for SQL

18
00:00:42.620 --> 00:00:45.640
injection, and we'd probably fuzz this area here.

19
00:00:45.800 --> 00:00:48.460
So we'd get, you know, do our usual

20
00:00:48.460 --> 00:00:50.120
quotes and things like this.

21
00:00:50.880 --> 00:00:53.600
And all I'm going to do is send

22
00:00:53.600 --> 00:00:56.400
this so I can see the response again.

23
00:00:56.520 --> 00:00:58.500
So I can see that the content length

24
00:00:58.500 --> 00:00:59.240
is 86.

25
00:00:59.620 --> 00:01:02.380
And I can see what the expected or

26
00:01:02.380 --> 00:01:03.860
normal response is.

27
00:01:04.660 --> 00:01:07.440
First, let's take a look at what we

28
00:01:07.440 --> 00:01:09.600
think the query might be.

29
00:01:09.800 --> 00:01:12.360
So this is just so I can try

30
00:01:12.360 --> 00:01:13.800
and explain this a little bit better and

31
00:01:13.800 --> 00:01:16.940
hopefully get you into the mindset of trying

32
00:01:16.940 --> 00:01:19.220
to understand what's happening behind the hood, and

33
00:01:19.220 --> 00:01:21.220
then testing your theory to see whether you're

34
00:01:21.220 --> 00:01:21.660
correct.

35
00:01:22.900 --> 00:01:26.460
So the theory probably looks something like select

36
00:01:26.460 --> 00:01:35.880
all from users, where username equals username and

37
00:01:35.880 --> 00:01:41.300
password equals password.

38
00:01:42.220 --> 00:01:43.800
And these are probably variables.

39
00:01:44.560 --> 00:01:47.460
So we'll just put them like this.

40
00:01:48.220 --> 00:01:49.900
So first off, what we can try and

41
00:01:49.900 --> 00:01:52.380
do is we can try and manipulate the

42
00:01:52.380 --> 00:01:55.940
username and add our all one equals one,

43
00:01:56.400 --> 00:01:58.920
and then comment out the rest of the

44
00:01:58.920 --> 00:01:59.300
code.

45
00:02:00.500 --> 00:02:02.660
Or we can try and add our payload

46
00:02:02.660 --> 00:02:05.280
to the end of the password and do

47
00:02:05.280 --> 00:02:07.820
all one equals one, and then we should

48
00:02:07.820 --> 00:02:08.699
be good to go.

49
00:02:09.300 --> 00:02:11.660
And let's just give this a try and

50
00:02:11.660 --> 00:02:12.540
see what happens.

51
00:02:14.000 --> 00:02:16.700
So we have all one equals one, and

52
00:02:16.700 --> 00:02:19.560
we'll send this and we get sorry, incorrect

53
00:02:19.560 --> 00:02:20.720
credentials still.

54
00:02:21.460 --> 00:02:22.320
Now that's interesting.

55
00:02:22.580 --> 00:02:25.240
So that means that we either didn't manipulate

56
00:02:25.240 --> 00:02:27.720
the query in the right way, or this

57
00:02:27.720 --> 00:02:29.480
isn't vulnerable to SQL injection.

58
00:02:30.380 --> 00:02:32.160
So we kind of got ahead of ourselves

59
00:02:32.160 --> 00:02:32.720
a little bit.

60
00:02:32.940 --> 00:02:34.660
And what I'm going to do is I'm

61
00:02:34.660 --> 00:02:36.520
actually going to just send a single quote

62
00:02:36.520 --> 00:02:39.400
here and see whether we do have SQL

63
00:02:39.400 --> 00:02:39.920
injection.

64
00:02:40.680 --> 00:02:43.160
And as you can see, we trigger an

65
00:02:43.160 --> 00:02:43.460
error.

66
00:02:43.940 --> 00:02:45.940
And so we probably do have SQL injection,

67
00:02:46.260 --> 00:02:48.300
but our payload is just incorrect.

68
00:02:48.820 --> 00:02:51.960
So my next theory is that this query

69
00:02:51.960 --> 00:02:56.260
here, instead of being unquoted, these may be

70
00:02:56.260 --> 00:02:57.700
put in quotes.

71
00:02:58.000 --> 00:03:00.060
And I know this just from having a

72
00:03:00.060 --> 00:03:01.840
background as a developer, there are many ways

73
00:03:01.840 --> 00:03:02.560
to write SQL.

74
00:03:03.320 --> 00:03:04.760
So what we can try and do is

75
00:03:04.760 --> 00:03:06.220
try and add our payload.

76
00:03:06.480 --> 00:03:09.160
So knowing that we can inject into here,

77
00:03:09.780 --> 00:03:13.280
so we can inject something like a, close

78
00:03:13.280 --> 00:03:17.760
this quote, and then put our all one

79
00:03:17.760 --> 00:03:18.560
equals one.

80
00:03:19.160 --> 00:03:21.180
And you'll notice that we have this trailing

81
00:03:21.180 --> 00:03:22.360
quotes at the end.

82
00:03:22.680 --> 00:03:24.560
So to deal with this, instead of doing

83
00:03:24.560 --> 00:03:26.640
all one equals one, we can do all

84
00:03:26.640 --> 00:03:29.620
one equals one like this to make sure

85
00:03:29.620 --> 00:03:31.240
the syntax is correct.

86
00:03:31.500 --> 00:03:32.960
And there are some other ways of dealing

87
00:03:32.960 --> 00:03:34.580
with this, we could do all one equals

88
00:03:34.580 --> 00:03:36.160
one, and then try and end the query

89
00:03:36.160 --> 00:03:38.680
so that this trailing quotes becomes a comment.

90
00:03:39.340 --> 00:03:41.580
But you can try out different ways and

91
00:03:41.580 --> 00:03:42.860
see what works for you.

92
00:03:43.500 --> 00:03:45.020
So I'm just going to copy and paste

93
00:03:45.020 --> 00:03:50.680
this, put this in here, hit send, and

94
00:03:50.680 --> 00:03:51.700
we get success.

95
00:03:51.700 --> 00:03:53.460
We're logged in as admin.

96
00:03:53.720 --> 00:03:56.180
Let's try this on the front end as

97
00:03:56.180 --> 00:03:56.560
well.

98
00:04:00.170 --> 00:04:01.370
We're logged in as admin.

99
00:04:01.910 --> 00:04:04.130
So this is a really powerful concept to

100
00:04:04.130 --> 00:04:06.250
know, as it can be used against many

101
00:04:06.250 --> 00:04:09.410
vulnerable endpoints, regardless of whether it's a login

102
00:04:09.410 --> 00:04:10.090
or not.

103
00:04:11.090 --> 00:04:13.030
So that's it for SQL injection.

104
00:04:13.330 --> 00:04:15.589
In the next video, we'll cover NoSQL injection,

105
00:04:15.870 --> 00:04:17.630
something that you're definitely going to run into

106
00:04:17.630 --> 00:04:19.110
if you do a lot of testing of

107
00:04:19.110 --> 00:04:19.610
APIs.

108
00:04:20.610 --> 00:04:22.270
After that, we have a nice challenge to

109
00:04:22.270 --> 00:04:25.070
tackle over on the crappy application, which will

110
00:04:25.070 --> 00:04:27.530
prepare us nicely for the mid-course capstone.

111
00:04:27.790 --> 00:04:28.230
See you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.300 --> 00:00:03.260
(Transcribed by TurboScribe. Go Unlimited to remove this message.) The general theory of NoSQL is similar to

2
00:00:03.260 --> 00:00:07.160
traditional SQL injection, in that we're interfering with

3
00:00:07.160 --> 00:00:08.960
the query that gets executed.

4
00:00:09.680 --> 00:00:12.300
However, the style of NoSQL is a little

5
00:00:12.300 --> 00:00:14.400
bit different, so we'll do a quick primer

6
00:00:14.400 --> 00:00:17.680
on NoSQL and MongoDB before taking a look

7
00:00:17.680 --> 00:00:18.360
at the lab.

8
00:00:18.800 --> 00:00:21.340
I've included this because of the increased popularity

9
00:00:21.340 --> 00:00:24.420
of NoSQL, and you'll find that many APIs

10
00:00:24.420 --> 00:00:28.100
are backed with MongoDB these days, and MongoDB

11
00:00:28.100 --> 00:00:30.960
is currently the most popular NoSQL database.

12
00:00:31.500 --> 00:00:32.280
So let's take a look.

13
00:00:33.900 --> 00:00:35.980
So I'm just going to drop into a

14
00:00:35.980 --> 00:00:39.620
Mongo shell to begin with, so mongo.sh,

15
00:00:40.560 --> 00:00:43.040
and here you can see we've connected, so

16
00:00:43.040 --> 00:00:45.140
don't worry too much about what's going on,

17
00:00:45.540 --> 00:00:48.340
but what we'll do first is we'll use

18
00:00:48.340 --> 00:00:49.500
DemoDB.

19
00:00:50.040 --> 00:00:53.380
So here we just type DemoDB, and you

20
00:00:53.380 --> 00:00:56.800
can see that we've switched to DemoDB, and

21
00:00:56.800 --> 00:00:58.000
I suspect I'm going to be in the

22
00:00:58.000 --> 00:01:00.020
way, so I'll just move myself out of

23
00:01:00.020 --> 00:01:01.300
the way for the time being.

24
00:01:02.860 --> 00:01:06.780
So now we're using this database called DemoDB.

25
00:01:07.240 --> 00:01:10.200
We actually need to create a collection, but

26
00:01:10.200 --> 00:01:13.600
MongoDB, because it's quite flexible, will create a

27
00:01:13.600 --> 00:01:15.920
collection for us when we try to add

28
00:01:15.920 --> 00:01:16.400
data.

29
00:01:17.160 --> 00:01:19.700
Now collections are like tables, but they're not

30
00:01:19.700 --> 00:01:21.200
constrained by the columns.

31
00:01:21.780 --> 00:01:23.800
So for example, if you add a user

32
00:01:23.800 --> 00:01:26.040
to a collection, you can give it a

33
00:01:26.040 --> 00:01:29.580
username, a password, an age, and other properties,

34
00:01:29.960 --> 00:01:31.860
and then if you add another user to

35
00:01:31.860 --> 00:01:34.060
the collection, maybe you just give it a

36
00:01:34.060 --> 00:01:36.080
username and password, and you don't give it

37
00:01:36.080 --> 00:01:37.180
an age, for example.

38
00:01:37.560 --> 00:01:40.220
Imagine that you can basically add columns on

39
00:01:40.220 --> 00:01:43.260
the fly, but they're not required by default.

40
00:01:44.420 --> 00:01:45.340
So let me show you quickly.

41
00:01:45.760 --> 00:01:48.580
So DB, which is the current DB, so

42
00:01:48.580 --> 00:01:51.360
we're DemoDB, and I'm going to call the

43
00:01:51.360 --> 00:01:53.760
collection users, and I'm just going to use

44
00:01:53.760 --> 00:01:56.060
the insert1 command like this.

45
00:01:56.700 --> 00:01:58.420
And I'm going to pass in a JSON

46
00:01:58.420 --> 00:02:00.900
object, so I'm just going to put name,

47
00:02:01.060 --> 00:02:05.020
and we're going to have Jeremy, and let's

48
00:02:05.020 --> 00:02:10.400
say Jeremy's password is cheesecake, like before, or

49
00:02:10.400 --> 00:02:11.060
I think before.

50
00:02:11.620 --> 00:02:13.380
And let's give him a country as well,

51
00:02:13.600 --> 00:02:17.400
so let's say that Jeremy is from, oops,

52
00:02:18.200 --> 00:02:18.440
Sweden.

53
00:02:23.710 --> 00:02:26.350
And now we get acknowledge true, and it's

54
00:02:26.350 --> 00:02:28.610
inserted it, and if we want to see

55
00:02:28.610 --> 00:02:33.590
the collection, we can do show collections, and

56
00:02:33.590 --> 00:02:35.510
we have our users collection, and if we

57
00:02:35.510 --> 00:02:37.470
want to list everything in there, we can

58
00:02:37.470 --> 00:02:40.930
do db.users.find, and it will list

59
00:02:40.930 --> 00:02:42.210
everything in there.

60
00:02:42.310 --> 00:02:44.470
So in this case, Jeremy has an object

61
00:02:44.470 --> 00:02:46.190
ID, and he has a name.

62
00:02:46.250 --> 00:02:48.510
This is automatically created and assigned, by the

63
00:02:48.510 --> 00:02:48.650
way.

64
00:02:49.230 --> 00:02:51.710
We didn't have to add this ourselves.

65
00:02:52.410 --> 00:02:54.390
So we have the name Jeremy, the password

66
00:02:54.390 --> 00:02:56.410
cheesecake, and the country Sweden.

67
00:02:57.330 --> 00:03:00.010
If we add another user, let's say that

68
00:03:00.010 --> 00:03:08.090
we add Jeremy, and Jeremy's password is tiramisu,

69
00:03:08.650 --> 00:03:13.550
and Jeremy is from Scotland, but Jeremy also

70
00:03:13.550 --> 00:03:16.030
has an age, and she's 35.

71
00:03:17.550 --> 00:03:19.850
And then now when we find, we see

72
00:03:19.850 --> 00:03:24.010
we have Jeremy, his password is cheesecake, his

73
00:03:24.010 --> 00:03:26.750
country is Sweden, but Jeremy is also in

74
00:03:26.750 --> 00:03:29.530
there with a name, password country, but also

75
00:03:29.530 --> 00:03:31.410
the age of 35.

76
00:03:32.770 --> 00:03:35.150
So if we want to find just one

77
00:03:35.150 --> 00:03:39.530
user, we can do db.users.find, and

78
00:03:39.530 --> 00:03:41.130
we can pass in some parameters.

79
00:03:41.510 --> 00:03:44.030
So for example, we can just say, I

80
00:03:44.030 --> 00:03:47.590
want all users of age 35.

81
00:03:48.610 --> 00:03:52.090
And it just returns Jessamy, because Jessamy is

82
00:03:52.090 --> 00:03:53.950
the only one with the age 25.

83
00:03:54.810 --> 00:03:57.970
Again, you might want all users with the

84
00:03:57.970 --> 00:04:04.240
name Jeremy, and it will pull Jeremy.

85
00:04:05.080 --> 00:04:07.120
And if we have some duplicate entries, so

86
00:04:07.120 --> 00:04:09.940
for example, there are two Jessamys, and this

87
00:04:09.940 --> 00:04:14.960
one prefers lemon tart, for example, but lives

88
00:04:14.960 --> 00:04:18.480
in Wales, and has the same age, you

89
00:04:18.480 --> 00:04:20.519
can see that it doesn't mind us having

90
00:04:20.519 --> 00:04:24.240
repeated fields, because these are not necessarily unique.

91
00:04:24.860 --> 00:04:28.040
And when we do find, we can find

92
00:04:28.040 --> 00:04:30.820
all the users with the name Jessamy, and

93
00:04:30.820 --> 00:04:32.840
it returns both Jessamys.

94
00:04:33.580 --> 00:04:36.400
Now one other thing to consider is that

95
00:04:36.400 --> 00:04:40.320
we also have JSON operators, and we're going

96
00:04:40.320 --> 00:04:42.740
to use these operators in our injection tag.

97
00:04:43.540 --> 00:04:46.360
So for example, a typical logging query might

98
00:04:46.360 --> 00:04:51.080
look something like db.users.find, and it

99
00:04:51.080 --> 00:04:56.410
might have name, and obviously we pass in

100
00:04:56.410 --> 00:04:59.150
the name Jeremy, and it might have the

101
00:04:59.150 --> 00:05:02.830
password, and we pass in Jeremy's password, which

102
00:05:02.830 --> 00:05:04.930
if I recall is cheesecake.

103
00:05:05.610 --> 00:05:08.510
If we don't supply the correct password, let's

104
00:05:08.510 --> 00:05:10.310
say we know he likes cheese but not

105
00:05:10.310 --> 00:05:12.570
cake, it doesn't find Jeremy.

106
00:05:12.790 --> 00:05:15.390
So this might be a typical login query

107
00:05:15.390 --> 00:05:17.430
that is part of our application.

108
00:05:18.650 --> 00:05:20.510
What we can do is if we have

109
00:05:20.510 --> 00:05:23.090
control over this, we might want to put

110
00:05:23.090 --> 00:05:26.550
input something like a JSON operator, so we

111
00:05:26.550 --> 00:05:29.710
could say something like the password is not

112
00:05:29.710 --> 00:05:35.870
equal to zero, for example, and this returns

113
00:05:35.870 --> 00:05:36.510
Jeremy.

114
00:05:37.250 --> 00:05:39.210
And obviously as long as we don't put

115
00:05:39.210 --> 00:05:42.010
the correct password in here, so not equal

116
00:05:42.010 --> 00:05:45.110
to undefined or blank, we'll also pass Jeremy.

117
00:05:45.990 --> 00:05:48.430
So in this case, we can use JSON

118
00:05:48.430 --> 00:05:52.210
operators to bypass the logic of the application's

119
00:05:52.210 --> 00:05:53.430
NoSQL queries.

120
00:05:54.050 --> 00:05:55.770
So let's take what we've learned here and

121
00:05:55.770 --> 00:05:57.170
apply this to the lab.

122
00:05:58.290 --> 00:06:00.910
All right, so I'm in the labs folder,

123
00:06:01.310 --> 00:06:04.330
and as you can see I have the

124
00:06:04.330 --> 00:06:08.130
API NoSQL injection zip, so I'm just going

125
00:06:08.130 --> 00:06:09.470
to unzip this.

126
00:06:10.490 --> 00:06:12.650
You can see there's quite a few modules

127
00:06:12.650 --> 00:06:12.950
in there.

128
00:06:12.990 --> 00:06:15.270
This is because it's using Node and Express,

129
00:06:15.630 --> 00:06:19.510
and we're just going to cd into this

130
00:06:20.890 --> 00:06:29.730
folder, clear ls sudo docker compose up, and

131
00:06:29.730 --> 00:06:31.650
we'll give it a minute to build the

132
00:06:31.650 --> 00:06:32.270
application.

133
00:06:33.930 --> 00:06:36.570
While it's doing that, I can load up

134
00:06:36.570 --> 00:06:43.470
Firefox and also Burp Suite, and it doesn't

135
00:06:43.470 --> 00:06:45.110
matter whether you have the professional or community

136
00:06:45.110 --> 00:06:47.710
edition, we're just going to use the repeater

137
00:06:47.710 --> 00:06:49.030
for this one.

138
00:06:53.350 --> 00:06:55.830
While this is loading up, actually, I should

139
00:06:55.830 --> 00:07:00.110
say that basically fuzzing for NoSQL vulnerabilities is

140
00:07:00.110 --> 00:07:02.830
exactly the same as fuzzing for SQL injection

141
00:07:02.830 --> 00:07:06.050
vulnerabilities, except that your word list may be

142
00:07:06.050 --> 00:07:07.050
a little bit different.

143
00:07:07.530 --> 00:07:09.670
So if you have Seqlists installed, if you

144
00:07:09.670 --> 00:07:11.090
don't have it installed, you can install it

145
00:07:11.090 --> 00:07:17.170
with sudo apt install Seqlists like this, and

146
00:07:17.170 --> 00:07:18.850
it's going to tell me that I've already

147
00:07:18.850 --> 00:07:21.750
installed it, and then if we come into

148
00:07:21.750 --> 00:07:26.850
Seqlists, so if we ls user share, oops,

149
00:07:26.970 --> 00:07:30.490
not word lists, Seqlists, and before we used

150
00:07:30.490 --> 00:07:34.190
the fuzzing, and I think we used the

151
00:07:35.250 --> 00:07:37.570
sqli, and there are some SQL word lists

152
00:07:37.570 --> 00:07:38.150
in here.

153
00:07:38.410 --> 00:07:40.510
If we come back, and we go back

154
00:07:40.510 --> 00:07:45.070
into fuzzing, and we come into databases, and

155
00:07:45.070 --> 00:07:48.250
you'll see that there is a nosql.txt

156
00:07:51.360 --> 00:07:52.820
file here.

157
00:07:53.080 --> 00:07:55.420
So if we just cat this, for example,

158
00:07:55.660 --> 00:07:57.540
you can see that this is full of

159
00:07:57.540 --> 00:07:59.720
NoSQL injection payloads.

160
00:08:00.040 --> 00:08:02.520
So if you're fuzzing for NoSQL injection, you'll

161
00:08:02.520 --> 00:08:04.660
want to use a list like this rather

162
00:08:04.660 --> 00:08:07.100
than the traditional SQL injection lists.

163
00:08:08.240 --> 00:08:10.420
So let's come back to here, and we

164
00:08:10.420 --> 00:08:11.640
got a warning.

165
00:08:12.020 --> 00:08:14.500
Ah, this is because I have Mongo already

166
00:08:14.500 --> 00:08:15.520
running, I think.

167
00:08:15.880 --> 00:08:23.090
So sudo systemctl stop, and let's try again.

168
00:08:24.770 --> 00:08:27.450
Trying to use the same ports that MongoDB

169
00:08:27.450 --> 00:08:29.190
was already using on my system.

170
00:08:30.310 --> 00:08:34.650
All right, so let's come into localhost, and

171
00:08:34.650 --> 00:08:36.770
we have our NoSQL injection.

172
00:08:37.350 --> 00:08:39.750
Now, if there are no current users, feel

173
00:08:39.750 --> 00:08:40.770
free to add some.

174
00:08:40.990 --> 00:08:43.250
So for example, we have jessemy, we can

175
00:08:43.250 --> 00:08:47.310
add the username, password, jessemy, and this will

176
00:08:47.310 --> 00:08:49.970
add it to the current users, but if

177
00:08:49.970 --> 00:08:52.090
there are already some there, then you can

178
00:08:52.090 --> 00:08:53.570
carry on with the exercise.

179
00:08:53.990 --> 00:08:56.590
And this is just to demonstrate NoSQL injection.

180
00:08:57.130 --> 00:09:00.190
So if I log in as alex, alex,

181
00:09:01.590 --> 00:09:03.990
you get a success logged in as alex,

182
00:09:04.150 --> 00:09:05.730
but if I log in with the wrong

183
00:09:05.730 --> 00:09:08.850
username or the wrong password, we get, sorry,

184
00:09:09.050 --> 00:09:11.050
you provided incorrect credentials.

185
00:09:11.910 --> 00:09:15.150
So let's switch on our proxy, and I'm

186
00:09:15.150 --> 00:09:18.310
just going to add in asd, asd, asd,

187
00:09:18.350 --> 00:09:22.170
asd, and hit log in, and then come

188
00:09:22.170 --> 00:09:26.710
to web suite, come to proxy, HTTP history,

189
00:09:27.190 --> 00:09:29.670
localhost, and we can see that this is

190
00:09:29.670 --> 00:09:31.830
kind of a bad practice, but I think

191
00:09:31.830 --> 00:09:34.050
it's okay just for our demonstration labs.

192
00:09:34.610 --> 00:09:36.850
But obviously, when you log in, you don't

193
00:09:36.850 --> 00:09:39.290
want your username and password being passed via

194
00:09:39.290 --> 00:09:39.890
the URI.

195
00:09:40.050 --> 00:09:41.370
If you ever see this in a web

196
00:09:41.370 --> 00:09:44.330
application, you should report this as an issue

197
00:09:44.330 --> 00:09:44.890
or a finding.

198
00:09:45.210 --> 00:09:48.510
So let's just send this to repeater, and

199
00:09:48.510 --> 00:09:50.430
then we'll send it once so that we

200
00:09:50.430 --> 00:09:54.830
can see, and I think the message that

201
00:09:54.830 --> 00:09:56.910
comes back is sorry.

202
00:09:57.150 --> 00:09:59.730
So I'm just going to add sorry into

203
00:09:59.730 --> 00:10:02.530
the search here, and if I move myself

204
00:10:02.530 --> 00:10:05.010
out of the way, you can see that

205
00:10:05.010 --> 00:10:07.270
we have one match down here in the

206
00:10:07.270 --> 00:10:07.510
corner.

207
00:10:08.050 --> 00:10:09.990
So if I send a request and I

208
00:10:09.990 --> 00:10:11.770
don't see this one match, I know that

209
00:10:11.770 --> 00:10:14.230
my request has been successful, or what you

210
00:10:14.230 --> 00:10:15.770
can do is you can render the page

211
00:10:15.770 --> 00:10:17.450
and look at it yourself.

212
00:10:19.750 --> 00:10:20.190
All right.

213
00:10:21.350 --> 00:10:24.050
So here, what we want to do is

214
00:10:24.050 --> 00:10:26.430
let's try and log in as admin.

215
00:10:26.710 --> 00:10:28.010
So we'll send another request.

216
00:10:28.830 --> 00:10:31.210
It comes back as 200 okay, but we

217
00:10:31.210 --> 00:10:33.850
have our one match saying sorry, you provided

218
00:10:33.850 --> 00:10:35.290
incorrect credentials.

219
00:10:35.950 --> 00:10:38.550
So what I'm going to do is instead

220
00:10:38.550 --> 00:10:43.030
of doing something like or one equals one

221
00:10:43.030 --> 00:10:45.930
here, I'm going to say that I know

222
00:10:45.930 --> 00:10:48.870
this is the incorrect password, because we get

223
00:10:48.870 --> 00:10:54.090
the sorry, your provided credentials are incorrect, and

224
00:10:54.090 --> 00:10:57.490
here I'm going to inject a not equals.

225
00:10:58.250 --> 00:11:00.930
So our query is going to say hey,

226
00:11:01.450 --> 00:11:06.570
db.users.find username equals admin, password not

227
00:11:06.570 --> 00:11:09.450
equals to asd asd.

228
00:11:10.190 --> 00:11:12.030
And you'll see that when we send this

229
00:11:12.030 --> 00:11:15.490
query, we get zero matches, and if we

230
00:11:15.490 --> 00:11:18.390
render it, we get a success, you logged

231
00:11:18.390 --> 00:11:19.630
in as admin.

232
00:11:20.650 --> 00:11:23.030
So as you can see, the theory is

233
00:11:23.030 --> 00:11:23.650
quite similar.

234
00:11:24.210 --> 00:11:26.770
We're manipulating the query to get the results

235
00:11:26.770 --> 00:11:28.230
that we want from the database.

236
00:11:29.650 --> 00:11:31.470
And if you want to know a little

237
00:11:31.470 --> 00:11:34.450
bit more about NoSQL payloads, you can come

238
00:11:34.450 --> 00:11:37.650
to payloads, all the things on the Swisskey

239
00:11:37.650 --> 00:11:40.590
repo, something that you probably already have bookmarked.

240
00:11:40.750 --> 00:11:42.690
If you don't have it bookmarked already, then

241
00:11:42.690 --> 00:11:45.090
please go ahead and check this resource out.

242
00:11:45.810 --> 00:11:48.170
And if we just search for NoSQL injection,

243
00:11:48.710 --> 00:11:51.290
you'll get a page where you have a

244
00:11:51.290 --> 00:11:53.110
number of payloads.

245
00:11:53.110 --> 00:11:56.470
If you're working in JSON, or PHP, for

246
00:11:56.470 --> 00:11:59.930
example, and also some scripts to deal with

247
00:11:59.930 --> 00:12:02.090
NoSQL injection as well.

248
00:12:02.970 --> 00:12:05.250
And as you can see, where we have

249
00:12:05.250 --> 00:12:07.990
a username is not equal to toto or

250
00:12:07.990 --> 00:12:10.950
tutu, and password is not equal to toto

251
00:12:10.950 --> 00:12:13.610
or tutu, and the JSON equivalent here.

252
00:12:13.810 --> 00:12:15.910
So the username is not equal to the

253
00:12:15.910 --> 00:12:18.930
null, and the password is not equal to

254
00:12:18.930 --> 00:12:21.250
the null, and this is our JSON operator

255
00:12:21.250 --> 00:12:22.070
here.

256
00:12:22.650 --> 00:12:25.270
So depending on the underlying technology, you need

257
00:12:25.270 --> 00:12:27.270
to decide which payload to use, and then

258
00:12:27.270 --> 00:12:27.970
go from there.

259
00:12:28.870 --> 00:12:31.650
All right, that's it for our SQL injection

260
00:12:31.650 --> 00:12:32.270
primer.

261
00:12:32.650 --> 00:12:35.150
I hope you got some insights into fuzzing,

262
00:12:35.350 --> 00:12:37.710
testing, and exploiting SQL injection.

263
00:12:38.210 --> 00:12:39.770
Of course, feel free to go over the

264
00:12:39.770 --> 00:12:42.310
labs we've done yourself to help you solidify

265
00:12:42.310 --> 00:12:44.850
the topics and test out different payloads and

266
00:12:44.850 --> 00:12:45.510
methodologies.

267
00:12:46.250 --> 00:12:48.190
I also have a small challenge for you

268
00:12:48.190 --> 00:12:50.650
as well, to make sure that we solidify

269
00:12:50.650 --> 00:12:51.390
what we've learned.

270
00:12:51.850 --> 00:12:53.650
Let me bring you to my VM.

271
00:12:55.210 --> 00:12:58.010
So here we have the dashboard of the

272
00:12:58.010 --> 00:13:03.030
crappy API application, and I'm going to take

273
00:13:03.030 --> 00:13:05.890
you over to the shop, and here we

274
00:13:05.890 --> 00:13:09.350
have the coupons or add coupons endpoints, and

275
00:13:09.350 --> 00:13:11.210
this is the endpoint that I'd like you

276
00:13:11.210 --> 00:13:13.550
to assess and see if you can achieve

277
00:13:13.550 --> 00:13:14.930
SQL injection.

278
00:13:15.710 --> 00:13:17.190
So one thing that I do want to

279
00:13:17.190 --> 00:13:19.750
mention, if you're using burp suite, is a

280
00:13:19.750 --> 00:13:21.610
little quirk that might catch you out.

281
00:13:22.330 --> 00:13:25.510
So when using intruder, burp suite usually has

282
00:13:25.510 --> 00:13:28.190
this payload encoding ticked automatically.

283
00:13:28.650 --> 00:13:31.450
So if you're fuzzing word lists and you've

284
00:13:31.450 --> 00:13:32.950
tried a bunch of things and you don't

285
00:13:32.950 --> 00:13:36.450
find anything, maybe try not using URL encoding,

286
00:13:36.670 --> 00:13:37.170
for example.

287
00:13:37.870 --> 00:13:40.710
And also with your payload, be careful with

288
00:13:40.710 --> 00:13:42.230
where you place your highlighting.

289
00:13:42.690 --> 00:13:45.030
So for example, if I have a payload

290
00:13:45.030 --> 00:13:50.010
that says Alex, like this, I might want

291
00:13:50.010 --> 00:13:53.250
to test adding something inside, but this may

292
00:13:53.250 --> 00:13:55.150
be passed as a string, so I may

293
00:13:55.150 --> 00:14:01.660
want to also test something, whoops, adding my

294
00:14:01.660 --> 00:14:04.720
payload over the top, including those two quotes.

295
00:14:05.160 --> 00:14:06.460
So have a play around with it.

296
00:14:06.620 --> 00:14:08.260
I know that these things can catch you

297
00:14:08.260 --> 00:14:10.540
out, so they're worth bearing in mind as

298
00:14:10.540 --> 00:14:11.040
you're testing.

299
00:14:11.380 --> 00:14:13.180
Good luck with the challenge, and I'll see

300
00:14:13.180 --> 00:14:13.860
you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.150 --> 00:00:02.290
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome to the final video of

2
00:00:02.290 --> 00:00:02.910
the section.

3
00:00:03.370 --> 00:00:05.190
I hope you got on well with the

4
00:00:05.190 --> 00:00:05.750
challenge.

5
00:00:06.150 --> 00:00:07.690
Congratulations if you solved it.

6
00:00:07.830 --> 00:00:09.710
If you didn't solve it, don't worry, we're

7
00:00:09.710 --> 00:00:10.690
going to walk through it together.

8
00:00:11.010 --> 00:00:12.670
Make sure that you take notes and learn

9
00:00:12.670 --> 00:00:15.129
from this experience so that you're successful next

10
00:00:15.129 --> 00:00:15.430
time.

11
00:00:15.970 --> 00:00:18.490
So let's dive straight in and I'm gonna

12
00:00:18.490 --> 00:00:21.410
jump to my VM and we're just gonna

13
00:00:21.410 --> 00:00:25.330
come in and enter a coupon code, ASDASD,

14
00:00:25.670 --> 00:00:26.770
and hit validate.

15
00:00:27.290 --> 00:00:30.850
And unsurprisingly, we get invalid coupon code.

16
00:00:31.409 --> 00:00:34.170
So I've already got traffic going to VEP

17
00:00:34.170 --> 00:00:36.510
suite, so I'll just switch over to here.

18
00:00:37.710 --> 00:00:41.490
And interestingly enough, we get a 500 internal

19
00:00:41.490 --> 00:00:42.330
server error.

20
00:00:42.690 --> 00:00:45.930
So let's send this straight over to intruder.

21
00:00:46.210 --> 00:00:50.810
So hit ctrl i and let's take a

22
00:00:50.810 --> 00:00:51.150
look.

23
00:00:51.470 --> 00:00:53.830
So I think I left a hint for

24
00:00:53.830 --> 00:00:55.230
this, but the first thing I want to

25
00:00:55.230 --> 00:00:58.450
think about is this payload that's been highlighted.

26
00:00:58.890 --> 00:01:01.970
If we send all of our payloads that

27
00:01:01.970 --> 00:01:05.030
are enclosed in quotes, it's probably going to

28
00:01:05.030 --> 00:01:06.650
be interpreted as a string.

29
00:01:07.190 --> 00:01:09.430
So what I'm going to do first is

30
00:01:09.430 --> 00:01:11.110
I'm going to clear this and I want

31
00:01:11.110 --> 00:01:14.170
my payload to be the whole thing.

32
00:01:14.470 --> 00:01:16.090
So that's one thing that I'm going to

33
00:01:16.090 --> 00:01:16.330
do.

34
00:01:16.670 --> 00:01:18.550
And the second is I'm going to come

35
00:01:18.550 --> 00:01:22.290
in and I'm going to load in a

36
00:01:22.290 --> 00:01:24.510
SQL injection payload list.

37
00:01:25.030 --> 00:01:27.370
So I'm just going to click add from

38
00:01:27.370 --> 00:01:33.100
list and if I can find it, SQL

39
00:01:33.100 --> 00:01:34.320
fuzzing, SQL injection.

40
00:01:34.780 --> 00:01:36.460
And then I'm just going to click start

41
00:01:36.460 --> 00:01:38.060
and see what comes back.

42
00:01:38.500 --> 00:01:40.600
And I'm looking for the same things that

43
00:01:40.600 --> 00:01:41.800
we looked for in the lab.

44
00:01:41.800 --> 00:01:44.520
So status code and length.

45
00:01:45.080 --> 00:01:46.580
And I think all we can really see

46
00:01:46.580 --> 00:01:49.400
is one status code of 500 if we

47
00:01:49.400 --> 00:01:53.480
send the initial request and then we get

48
00:01:53.480 --> 00:01:54.940
422 after that.

49
00:01:55.120 --> 00:01:57.040
So unprocessable entity.

50
00:01:57.640 --> 00:02:00.620
So it doesn't actually like our inputs, but

51
00:02:00.620 --> 00:02:03.620
interesting that we're getting some different results back,

52
00:02:04.480 --> 00:02:07.520
some different error messages back, which again hints

53
00:02:07.520 --> 00:02:09.580
that we might be able to get SQL

54
00:02:09.580 --> 00:02:10.320
injection.

55
00:02:10.320 --> 00:02:12.760
So error messages in this case are always

56
00:02:12.760 --> 00:02:13.540
a good thing.

57
00:02:14.140 --> 00:02:15.580
So what I'm going to do is I'm

58
00:02:15.580 --> 00:02:17.780
going to clear this and then there's not

59
00:02:17.780 --> 00:02:20.500
a NoSQL injection list included in bub suite.

60
00:02:20.880 --> 00:02:23.520
So I'm just going to load and then

61
00:02:23.520 --> 00:02:32.170
I'm going to go to user

62
00:02:32.170 --> 00:02:41.150
share stack lists and then we're going to

63
00:02:41.150 --> 00:02:43.430
try discovery.

64
00:02:43.970 --> 00:02:45.550
Nope, we're not going to try discovery.

65
00:02:45.690 --> 00:02:49.150
We're going to try fuzzing and databases and

66
00:02:49.150 --> 00:02:51.710
there is a NoSQL list here.

67
00:02:52.930 --> 00:02:54.490
And as you can see, this is all

68
00:02:54.490 --> 00:02:58.010
NoSQL and things like greater than are very

69
00:02:58.010 --> 00:02:59.650
similar to not equals.

70
00:03:00.130 --> 00:03:01.750
So these are some of the payloads or

71
00:03:01.750 --> 00:03:04.390
similar to the payloads that we used in

72
00:03:04.390 --> 00:03:04.830
the lab.

73
00:03:05.130 --> 00:03:06.510
So the list isn't very long.

74
00:03:07.150 --> 00:03:10.070
I'm just going to hit start attack and

75
00:03:10.070 --> 00:03:13.670
interestingly enough, we don't really see many results.

76
00:03:13.890 --> 00:03:15.350
So all the status codes are the same.

77
00:03:15.430 --> 00:03:17.090
We do get some different lengths.

78
00:03:18.230 --> 00:03:20.250
So, but they're all very close to get

79
00:03:20.250 --> 00:03:20.890
together.

80
00:03:21.090 --> 00:03:23.350
So four, five, nine, four, four, seven, four,

81
00:03:23.410 --> 00:03:23.870
four, nine.

82
00:03:25.550 --> 00:03:27.710
I'd want to see something a little bit

83
00:03:27.710 --> 00:03:31.250
more out there to verify this.

84
00:03:32.090 --> 00:03:33.530
So what I'm going to do is I'm

85
00:03:33.530 --> 00:03:35.570
going to come down and I wonder if

86
00:03:35.570 --> 00:03:38.990
the URL encoding is breaking this.

87
00:03:39.070 --> 00:03:40.530
So I'm just going to switch off URL

88
00:03:40.530 --> 00:03:43.110
encoding, always something to try if you're not

89
00:03:43.110 --> 00:03:45.670
getting any results or any luck with your

90
00:03:45.670 --> 00:03:46.130
results.

91
00:03:46.670 --> 00:03:47.990
Click start attack.

92
00:03:48.710 --> 00:03:51.250
So we can come down and again, we

93
00:03:51.250 --> 00:03:52.030
get 422.

94
00:03:52.630 --> 00:03:55.850
And actually, if we look closely, there is

95
00:03:55.850 --> 00:03:57.790
a 200 here in the list.

96
00:03:58.310 --> 00:04:01.450
So it looks like greater than blank actually

97
00:04:01.450 --> 00:04:04.630
yielded some results and we got our coupon

98
00:04:04.630 --> 00:04:05.070
code.

99
00:04:06.130 --> 00:04:07.650
We would have also seen this if we

100
00:04:07.650 --> 00:04:09.110
just skimmed down the list and you can

101
00:04:09.110 --> 00:04:11.650
see it kind of blink up, but the

102
00:04:11.650 --> 00:04:13.530
length isn't that different.

103
00:04:13.850 --> 00:04:15.550
So in this case, it would have been

104
00:04:15.550 --> 00:04:17.329
tricky to see from the length, but the

105
00:04:17.329 --> 00:04:18.670
status code gave it away.

106
00:04:19.810 --> 00:04:23.090
If we'd grepped for the reverse of invalid,

107
00:04:23.290 --> 00:04:24.910
we would have also found this as well.

108
00:04:24.990 --> 00:04:26.070
So let me show you this quickly.

109
00:04:26.470 --> 00:04:29.350
So we'll just go for invalid, negative search,

110
00:04:29.870 --> 00:04:32.370
hit apply, and you can see that we

111
00:04:32.370 --> 00:04:33.310
find our results.

112
00:04:33.430 --> 00:04:34.770
So if we had tens of thousands of

113
00:04:34.770 --> 00:04:37.090
results, this would be the most effective way

114
00:04:37.090 --> 00:04:39.430
of finding it or by filtering on the

115
00:04:39.430 --> 00:04:40.070
status code.

116
00:04:40.550 --> 00:04:42.130
Again, depends on the situation.

117
00:04:42.530 --> 00:04:45.450
We've got to exhaust all possibilities and being

118
00:04:45.450 --> 00:04:47.750
thorough is really a big part of web

119
00:04:47.750 --> 00:04:49.050
application security.

120
00:04:49.450 --> 00:04:52.290
So that's it for this section and I

121
00:04:52.290 --> 00:04:54.330
hope you're enjoying the journey as much as

122
00:04:54.330 --> 00:04:55.950
I enjoyed making these videos.

123
00:04:56.570 --> 00:04:58.530
Our next stop is the mid-course capstone,

124
00:04:58.690 --> 00:04:59.650
so I'll see you there.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Mid-course Capstone

WEBVTT

1
00:00:00.460 --> 00:00:03.780
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome to the mid-course capstone challenge.

2
00:00:04.180 --> 00:00:05.620
You've done a great job so far in

3
00:00:05.620 --> 00:00:08.100
this course and I hope that you're improving

4
00:00:08.100 --> 00:00:11.600
your workflow and learning about new vulnerabilities to

5
00:00:11.600 --> 00:00:12.080
test.

6
00:00:12.300 --> 00:00:13.680
In this section I'm going to give you

7
00:00:13.680 --> 00:00:15.440
a small application to test.

8
00:00:15.800 --> 00:00:18.320
This is built in a way where each

9
00:00:18.320 --> 00:00:21.000
individual part has kind of been created but

10
00:00:21.000 --> 00:00:23.320
the overall architecture and design of the system

11
00:00:23.320 --> 00:00:25.040
has been somewhat neglected.

12
00:00:25.860 --> 00:00:28.580
During this challenge you're free to use any

13
00:00:28.580 --> 00:00:30.920
tools or attacks that you'd like but remember

14
00:00:30.920 --> 00:00:33.380
that it's designed to demonstrate the topics we've

15
00:00:33.380 --> 00:00:34.320
covered so far.

16
00:00:34.900 --> 00:00:37.120
You'll likely find other common issues such as

17
00:00:37.120 --> 00:00:39.700
CSRF and lack of hashing and if you

18
00:00:39.700 --> 00:00:41.500
want to use this as an exercise to

19
00:00:41.500 --> 00:00:44.300
find those kinds of vulnerabilities then by all

20
00:00:44.300 --> 00:00:45.900
means feel free to do so.

21
00:00:46.340 --> 00:00:47.880
I'm just going to spin up the lab

22
00:00:47.880 --> 00:00:49.240
so that you know what it looks like

23
00:00:49.240 --> 00:00:50.880
and where your starting point is.

24
00:00:51.000 --> 00:00:51.860
Let's jump in.

25
00:00:52.280 --> 00:00:54.940
So as usual I just have the zip

26
00:00:54.940 --> 00:00:57.200
file here ready to go so I'm just

27
00:00:57.200 --> 00:01:03.060
going to unzip API mid-course capstone and

28
00:01:03.060 --> 00:01:07.020
here we have the API mid-course capstone

29
00:01:07.020 --> 00:01:07.620
folder.

30
00:01:08.080 --> 00:01:09.620
So I'm just going to come into this,

31
00:01:10.380 --> 00:01:12.540
clear my screen and you can see the

32
00:01:12.540 --> 00:01:15.260
files and then as usual we're going to

33
00:01:15.260 --> 00:01:19.280
sudo docker compose up and something to note

34
00:01:19.280 --> 00:01:22.400
that this web application runs on port 80

35
00:01:22.400 --> 00:01:25.140
so if you have Apache or something else

36
00:01:25.140 --> 00:01:27.880
running that's already using port 80 on your

37
00:01:27.880 --> 00:01:30.460
machine it might throw an error saying hey

38
00:01:30.460 --> 00:01:32.500
port's already in use and all you need

39
00:01:32.500 --> 00:01:35.580
to do is go in and close down

40
00:01:35.580 --> 00:01:37.720
Apache or whatever it is that you have

41
00:01:37.720 --> 00:01:39.480
running on port 80.

42
00:01:39.880 --> 00:01:41.620
So once we have this running we're just

43
00:01:41.620 --> 00:01:45.500
going to open Firefox and then we're just

44
00:01:45.500 --> 00:01:49.180
going to come to localhost, hit enter and

45
00:01:49.180 --> 00:01:50.900
we get this main page.

46
00:01:51.280 --> 00:01:53.060
So you can see we have some register,

47
00:01:53.400 --> 00:01:56.360
login, order coffee, track your order and a

48
00:01:56.360 --> 00:01:57.520
view stock buttons.

49
00:01:57.700 --> 00:01:59.940
So this is the application and it's up

50
00:01:59.940 --> 00:02:01.580
to you how much time you spend on

51
00:02:01.580 --> 00:02:02.840
this but make sure you have a good

52
00:02:02.840 --> 00:02:04.680
go at trying the techniques we've covered.

53
00:02:04.900 --> 00:02:06.360
Good luck and I'll see you in the

54
00:02:06.360 --> 00:02:06.860
next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.170 --> 00:00:01.790
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome back.

2
00:00:01.990 --> 00:00:04.790
Let's take a look at the application.

3
00:00:05.210 --> 00:00:06.830
I hope you got on well and found

4
00:00:06.830 --> 00:00:09.650
some interesting vulnerabilities along the way.

5
00:00:10.210 --> 00:00:12.210
So I'm going to walk you through some

6
00:00:12.210 --> 00:00:13.490
of the main things that I wanted you

7
00:00:13.490 --> 00:00:15.570
to find and things that we've looked at

8
00:00:15.570 --> 00:00:16.750
throughout the course.

9
00:00:16.930 --> 00:00:21.290
If you found extra stuff, then congratulations, and

10
00:00:21.290 --> 00:00:22.230
let's dive in.

11
00:00:22.650 --> 00:00:25.170
So here we are at the main page.

12
00:00:25.270 --> 00:00:26.950
So first thing I want to do is

13
00:00:26.950 --> 00:00:28.830
look at these buttons.

14
00:00:29.090 --> 00:00:32.170
So it seems like we have three major

15
00:00:32.170 --> 00:00:35.030
buttons plus a login and register.

16
00:00:35.350 --> 00:00:37.030
So I'm just going to click on view

17
00:00:37.030 --> 00:00:39.650
current stock, and it seems like we have

18
00:00:39.650 --> 00:00:41.270
three types of coffee.

19
00:00:41.490 --> 00:00:44.270
So revival, rise and shine, and chitters.

20
00:00:44.750 --> 00:00:46.670
And they come from different regions.

21
00:00:47.370 --> 00:00:50.890
And we can see Ethiopia, Ethiopia, Brazil, and

22
00:00:50.890 --> 00:00:52.350
they have different roast levels.

23
00:00:52.930 --> 00:00:54.330
So I'm just going to click this.

24
00:00:54.370 --> 00:00:56.510
This brings us back to the home page.

25
00:00:57.250 --> 00:00:59.130
And also what I'm going to do is

26
00:00:59.130 --> 00:01:00.210
just switch on my proxy.

27
00:01:00.350 --> 00:01:02.030
I probably should have done this straight away.

28
00:01:02.310 --> 00:01:03.410
So I'm just going to come back and

29
00:01:03.410 --> 00:01:05.450
browse here, and then come back.

30
00:01:05.750 --> 00:01:07.290
And this is just so I'm capturing all

31
00:01:07.290 --> 00:01:09.990
the traffic as I walk through the application.

32
00:01:11.190 --> 00:01:12.730
And I'm just going to go with track

33
00:01:12.730 --> 00:01:13.170
your order.

34
00:01:13.590 --> 00:01:15.530
Seems like we need an order ID.

35
00:01:16.210 --> 00:01:19.030
Nothing comes back if we just enter ASD.

36
00:01:20.550 --> 00:01:22.770
Order coffee gives me a login screen.

37
00:01:23.110 --> 00:01:24.870
Okay, so this is about the time where

38
00:01:24.870 --> 00:01:27.310
I think about registering, and I'm just going

39
00:01:27.310 --> 00:01:30.410
to register a user called Alex.

40
00:01:31.030 --> 00:01:32.030
New user created.

41
00:01:32.670 --> 00:01:33.490
Close this.

42
00:01:34.150 --> 00:01:36.230
Looks like we can just go ahead and

43
00:01:36.230 --> 00:01:37.070
log in.

44
00:01:38.450 --> 00:01:41.170
And we successfully log in, and we notice

45
00:01:41.170 --> 00:01:42.910
there's some slight UI changes.

46
00:01:43.070 --> 00:01:44.710
So we have a logout button instead.

47
00:01:45.970 --> 00:01:47.890
And again, just have a quick look around,

48
00:01:47.890 --> 00:01:53.640
see if anything interesting has changed, and come

49
00:01:53.640 --> 00:01:54.620
to order coffee.

50
00:01:55.000 --> 00:01:56.900
And looks like we can place an order

51
00:01:56.900 --> 00:01:57.320
here.

52
00:01:58.120 --> 00:01:59.680
So something that I also want to look

53
00:01:59.680 --> 00:02:01.500
at is I have this cookie plugin.

54
00:02:01.980 --> 00:02:03.940
So just have a look at this.

55
00:02:05.020 --> 00:02:07.520
This looks like we were given a session

56
00:02:07.520 --> 00:02:10.380
token, which looks like a JWT, because it's

57
00:02:10.380 --> 00:02:12.320
got two dots in it, and looks like

58
00:02:12.320 --> 00:02:13.400
it's base64.

59
00:02:13.660 --> 00:02:15.200
So this looks like the header up here,

60
00:02:15.200 --> 00:02:19.060
then the payload, and then the signature at

61
00:02:19.060 --> 00:02:19.580
the bottom.

62
00:02:20.100 --> 00:02:21.920
And I'm going to go ahead and order

63
00:02:21.920 --> 00:02:24.500
one kilogram of jitters.

64
00:02:26.500 --> 00:02:29.160
I'll get order placed, and we have an

65
00:02:29.160 --> 00:02:30.220
order ID.

66
00:02:30.540 --> 00:02:33.760
So I'm just going to load up mousepad,

67
00:02:34.780 --> 00:02:36.620
paste this in so that we can see,

68
00:02:36.880 --> 00:02:38.780
refer to this later if we need to,

69
00:02:39.280 --> 00:02:41.360
and then come back and click close.

70
00:02:41.440 --> 00:02:42.700
And what I'm actually going to do is

71
00:02:42.700 --> 00:02:44.340
I'm just going to paste in here to

72
00:02:44.340 --> 00:02:45.760
see if I can track my order.

73
00:02:46.720 --> 00:02:48.520
And it does look like we have an

74
00:02:48.520 --> 00:02:51.160
order, and the username is Alex, and it's

75
00:02:51.160 --> 00:02:51.440
pending.

76
00:02:51.600 --> 00:02:52.680
And this looks a little weak.

77
00:02:53.000 --> 00:02:56.280
It's not a very long, unique ID, and

78
00:02:56.280 --> 00:03:00.220
looks like it's mostly numbers with one letter

79
00:03:00.220 --> 00:03:00.720
as well.

80
00:03:00.780 --> 00:03:02.900
So we might think about testing that soon.

81
00:03:03.980 --> 00:03:05.560
So I'm just going to come over to

82
00:03:05.560 --> 00:03:07.960
Bubsuite, and we can have a quick look

83
00:03:07.960 --> 00:03:08.860
through the traffic.

84
00:03:09.200 --> 00:03:10.740
So I like to kind of see what's

85
00:03:10.740 --> 00:03:11.400
going on here.

86
00:03:12.840 --> 00:03:14.400
And I can see a lot of slash

87
00:03:14.400 --> 00:03:18.380
v1 and slash coffee.php. So let's take

88
00:03:18.380 --> 00:03:20.160
a look and see what this endpoints is

89
00:03:20.160 --> 00:03:20.720
giving us.

90
00:03:21.160 --> 00:03:23.180
And I will just move myself out of

91
00:03:23.180 --> 00:03:24.980
the way so that we can see what's

92
00:03:24.980 --> 00:03:25.480
going on.

93
00:03:26.900 --> 00:03:29.040
And this looks like it just returns the

94
00:03:29.040 --> 00:03:32.500
three available coffees from the system.

95
00:03:33.240 --> 00:03:38.940
We have a functions.js. This looks like

96
00:03:38.940 --> 00:03:41.120
this is the front end that's handling all

97
00:03:41.120 --> 00:03:42.080
of the requests.

98
00:03:43.140 --> 00:03:44.740
So yeah, you can see check if logged

99
00:03:44.740 --> 00:03:47.900
in, close buttons, stuff like this.

100
00:03:48.500 --> 00:03:50.500
We might come back and take a look

101
00:03:50.500 --> 00:03:51.440
at that later on.

102
00:03:52.600 --> 00:03:54.160
And we have this track.

103
00:03:54.740 --> 00:03:56.600
So id is asd.

104
00:03:58.640 --> 00:04:01.280
So this was the first tracking query that

105
00:04:01.280 --> 00:04:01.720
we did.

106
00:04:02.120 --> 00:04:04.060
So we can maybe try and brute force

107
00:04:04.060 --> 00:04:04.480
this.

108
00:04:04.640 --> 00:04:07.580
Because we have an order ID now that

109
00:04:07.580 --> 00:04:10.640
we can use, we might have an idea

110
00:04:10.640 --> 00:04:12.560
of how we can get other coffees.

111
00:04:15.310 --> 00:04:17.190
And we have slash auth.

112
00:04:18.070 --> 00:04:20.010
So this was our new user created.

113
00:04:20.370 --> 00:04:22.790
And there are multiple calls to slash auth.

114
00:04:22.970 --> 00:04:24.790
So this looks like this one was the

115
00:04:24.790 --> 00:04:27.470
login one, which returned our JSON web token.

116
00:04:29.720 --> 00:04:31.500
And then we have an order here.

117
00:04:32.980 --> 00:04:35.840
And this is quite interesting, because when I

118
00:04:35.840 --> 00:04:38.800
placed an order, I didn't specify my username

119
00:04:38.800 --> 00:04:40.260
or email address.

120
00:04:40.420 --> 00:04:43.000
So it seems like the front end actually

121
00:04:43.000 --> 00:04:44.180
generated this.

122
00:04:44.760 --> 00:04:46.660
Now, this isn't necessarily a problem.

123
00:04:46.800 --> 00:04:49.000
But what looks like has happened is it's

124
00:04:49.000 --> 00:04:53.420
taken the information from my session ID, placed

125
00:04:53.420 --> 00:04:54.300
it into the request.

126
00:04:54.400 --> 00:04:57.020
If this isn't verified in the back end,

127
00:04:57.260 --> 00:04:59.520
what might happen is we may be able

128
00:04:59.520 --> 00:05:02.840
to place users on the behalf of another

129
00:05:02.840 --> 00:05:03.340
user.

130
00:05:03.520 --> 00:05:05.720
So let's take a quick look at the

131
00:05:05.720 --> 00:05:06.940
token next.

132
00:05:07.040 --> 00:05:08.620
I don't think there's much else to look

133
00:05:08.620 --> 00:05:09.460
for in here.

134
00:05:09.840 --> 00:05:10.980
But I hope this kind of gives you

135
00:05:10.980 --> 00:05:12.440
an idea of how I like to approach

136
00:05:12.440 --> 00:05:13.100
an application.

137
00:05:13.360 --> 00:05:15.460
I click through everything, have a look and

138
00:05:15.460 --> 00:05:16.760
see what's in the requests.

139
00:05:17.100 --> 00:05:20.320
Something that I did forget is adding these

140
00:05:20.320 --> 00:05:22.020
images, other binaries, and CSS.

141
00:05:22.280 --> 00:05:23.760
I like to be able to see everything.

142
00:05:25.160 --> 00:05:28.760
And let's take a look at this JWT.

143
00:05:29.220 --> 00:05:31.660
So I'm just going to go JWT.io.

144
00:05:34.570 --> 00:05:35.590
Scroll down.

145
00:05:36.050 --> 00:05:36.290
Oops.

146
00:05:36.690 --> 00:05:38.190
Accept the cookies on here.

147
00:05:39.150 --> 00:05:39.930
Paste this in.

148
00:05:40.170 --> 00:05:42.090
And as you can see, we have a

149
00:05:42.090 --> 00:05:43.110
username, Alex.

150
00:05:43.630 --> 00:05:45.350
So I think what I'm going to do

151
00:05:45.350 --> 00:05:46.130
is I'm going to do a little bit

152
00:05:46.130 --> 00:05:47.090
of A-B testing.

153
00:05:47.270 --> 00:05:48.330
So I'm going to close this.

154
00:05:48.690 --> 00:05:49.230
Log out.

155
00:05:50.350 --> 00:05:53.090
Register a new user called Alex2.

156
00:05:53.630 --> 00:05:56.490
And the password is going to be Alex2.

157
00:05:57.690 --> 00:06:00.530
And hopefully I get a new cookie, which

158
00:06:00.530 --> 00:06:01.970
doesn't look like.

159
00:06:02.990 --> 00:06:04.150
I need to log in first.

160
00:06:04.850 --> 00:06:05.830
So Alex2.

161
00:06:06.990 --> 00:06:07.590
Alex2.

162
00:06:08.470 --> 00:06:09.070
Close.

163
00:06:10.050 --> 00:06:11.390
And I get a new cookie.

164
00:06:11.590 --> 00:06:13.350
So let's copy this.

165
00:06:16.080 --> 00:06:16.900
And paste.

166
00:06:18.040 --> 00:06:19.720
And here we have Alex2.

167
00:06:19.800 --> 00:06:21.240
If you don't have this plugin, by the

168
00:06:21.240 --> 00:06:24.180
way, you can also do things like..

169
00:06:24.180 --> 00:06:24.380
Whoops.

170
00:06:24.460 --> 00:06:25.520
Let's come into here.

171
00:06:26.140 --> 00:06:28.220
If you want to see the cookies, you

172
00:06:28.220 --> 00:06:32.420
can just do document.cookie. And you can

173
00:06:32.420 --> 00:06:34.840
grab the cookie from here as well.

174
00:06:34.920 --> 00:06:36.120
Let me zoom in so you can see

175
00:06:36.120 --> 00:06:36.340
that.

176
00:06:37.100 --> 00:06:38.980
So this is another way of grabbing the

177
00:06:38.980 --> 00:06:40.360
cookie from the console.

178
00:06:41.560 --> 00:06:43.900
But we can see we have Alex2.

179
00:06:44.080 --> 00:06:46.180
So since we're logged in as Alex2, what

180
00:06:46.180 --> 00:06:48.080
I'm going to do is try and order

181
00:06:48.080 --> 00:06:52.100
something as Alex1 and see whether this works.

182
00:06:52.400 --> 00:06:54.820
I would try just changing the name and

183
00:06:54.820 --> 00:06:55.480
then sending it.

184
00:06:55.720 --> 00:06:57.120
And then I would also try sending it

185
00:06:57.120 --> 00:06:59.480
without the signature to see whether it accepts

186
00:06:59.480 --> 00:07:01.080
a null signature.

187
00:07:01.420 --> 00:07:03.680
And I might then try other attacks like

188
00:07:03.680 --> 00:07:06.480
changing the algorithm and header injection and things

189
00:07:06.480 --> 00:07:06.920
like that.

190
00:07:07.000 --> 00:07:08.780
But to start off with, what I want

191
00:07:08.780 --> 00:07:11.240
to do is test the basic functionality of

192
00:07:11.240 --> 00:07:11.760
the website.

193
00:07:11.900 --> 00:07:12.940
And then I kind of go deeper and

194
00:07:12.940 --> 00:07:15.960
deeper based on the behavior and the responses

195
00:07:15.960 --> 00:07:16.800
I get.

196
00:07:16.960 --> 00:07:19.220
So I'm going to click order coffee.

197
00:07:20.140 --> 00:07:21.420
And then I'm going to come to burp

198
00:07:21.420 --> 00:07:21.640
suite.

199
00:07:22.220 --> 00:07:24.460
And I'm going to switch intercept on.

200
00:07:25.200 --> 00:07:28.260
And I'm just going to hit place order.

201
00:07:28.460 --> 00:07:30.740
And I don't think I actually need the

202
00:07:30.740 --> 00:07:32.260
token here.

203
00:07:32.420 --> 00:07:36.840
So I'm going to paste this token in,

204
00:07:37.040 --> 00:07:37.900
this updated token.

205
00:07:38.820 --> 00:07:41.060
Change the name to Alex because I'm currently

206
00:07:41.060 --> 00:07:42.060
logged in as Alex2.

207
00:07:42.300 --> 00:07:46.320
So I want to see if Alex1, if

208
00:07:46.320 --> 00:07:48.380
I can place an order on behalf of

209
00:07:48.380 --> 00:07:49.020
Alex1.

210
00:07:49.880 --> 00:07:51.740
Seems like it went okay.

211
00:07:54.880 --> 00:07:57.040
And you can ignore this green highlighting.

212
00:07:57.260 --> 00:07:59.800
It's just from this JWT editor keys if

213
00:07:59.800 --> 00:08:01.680
you want to install this plugin by all

214
00:08:01.680 --> 00:08:01.980
means.

215
00:08:02.660 --> 00:08:05.960
But it will highlight when it detects JSON

216
00:08:05.960 --> 00:08:08.140
web tokens and it does a bunch of

217
00:08:08.140 --> 00:08:08.960
other things as well.

218
00:08:09.740 --> 00:08:11.980
And I get this order place.

219
00:08:12.200 --> 00:08:15.160
Now if I check this order, so I

220
00:08:15.160 --> 00:08:17.320
can come back, track my order.

221
00:08:19.020 --> 00:08:22.200
I did indeed place an order on behalf

222
00:08:22.200 --> 00:08:25.220
of Alex, even though I was logged in

223
00:08:25.220 --> 00:08:26.120
as Alex2.

224
00:08:26.360 --> 00:08:30.620
So this is broken function level authorization.

225
00:08:31.020 --> 00:08:33.740
I'm able to carry out an action on

226
00:08:33.740 --> 00:08:36.740
the behalf of another user or create an

227
00:08:36.740 --> 00:08:39.640
action or do something that is tied to

228
00:08:39.640 --> 00:08:42.460
another user account, not necessarily mine.

229
00:08:42.559 --> 00:08:45.680
So this is definitely a really important finding

230
00:08:45.680 --> 00:08:48.640
and something that we should be reporting.

231
00:08:49.220 --> 00:08:51.380
So next up, what I'm going to do

232
00:08:51.380 --> 00:08:53.240
is I'm just going to grab a fresh

233
00:08:53.240 --> 00:08:53.600
token.

234
00:08:54.980 --> 00:08:58.160
So let's log back in as Alex2 again.

235
00:08:58.660 --> 00:09:00.980
And I want to test to see whether

236
00:09:00.980 --> 00:09:03.200
this is using a weak secret.

237
00:09:03.520 --> 00:09:05.100
So I'm just going to come here, copy

238
00:09:05.100 --> 00:09:05.460
this.

239
00:09:05.740 --> 00:09:07.120
And the reason I'm testing in this is

240
00:09:07.120 --> 00:09:10.520
because I saw HS256 here instead of the

241
00:09:10.520 --> 00:09:11.440
RSA version.

242
00:09:12.000 --> 00:09:14.960
And that means that we can try and

243
00:09:14.960 --> 00:09:15.960
crack this token.

244
00:09:16.540 --> 00:09:17.960
I'm going to come over to my terminal,

245
00:09:18.840 --> 00:09:20.640
control shift T to open a new tab.

246
00:09:21.660 --> 00:09:23.980
And then we could use hashcat for this,

247
00:09:24.080 --> 00:09:26.140
but I'm just going to use JWT tool

248
00:09:26.140 --> 00:09:29.320
and I'm going to do dash c to

249
00:09:29.320 --> 00:09:32.560
crack, dash d to specify a word list.

250
00:09:32.980 --> 00:09:35.980
So user share word lists.

251
00:09:36.160 --> 00:09:38.380
Let's just use rocky for the time being.

252
00:09:39.060 --> 00:09:41.980
And then I'm going to copy in the

253
00:09:41.980 --> 00:09:42.580
token.

254
00:09:43.140 --> 00:09:43.900
Hit enter.

255
00:09:44.720 --> 00:09:45.920
And that was very fast.

256
00:09:46.020 --> 00:09:48.880
It says here coffee is the correct key.

257
00:09:49.080 --> 00:09:52.000
So not only have we discovered that we

258
00:09:52.000 --> 00:09:54.880
can carry out actions on behalf of a

259
00:09:54.880 --> 00:09:57.200
user because the token is not correctly checked

260
00:09:57.200 --> 00:10:00.340
in the backend, we've also found that a

261
00:10:00.340 --> 00:10:02.040
weak secret is used.

262
00:10:02.120 --> 00:10:05.160
So that's two critical issues that we have

263
00:10:05.160 --> 00:10:05.740
found.

264
00:10:06.240 --> 00:10:09.620
Now we haven't done much discovery beyond clicking

265
00:10:09.620 --> 00:10:10.640
around the application.

266
00:10:10.860 --> 00:10:12.480
So I think it's about time that we

267
00:10:12.480 --> 00:10:15.220
come back to here and we take a

268
00:10:15.220 --> 00:10:17.540
look and see what else we can find.

269
00:10:18.020 --> 00:10:19.780
So I'm just going to copy and paste

270
00:10:19.780 --> 00:10:20.800
the URL.

271
00:10:21.340 --> 00:10:23.820
And we already know we have slash v1.

272
00:10:24.160 --> 00:10:29.080
So let's come back to here and use

273
00:10:29.080 --> 00:10:31.260
fuf dash u.

274
00:10:32.160 --> 00:10:33.780
And what I'm going to do is I

275
00:10:33.780 --> 00:10:36.740
want to see if there's anything else behind

276
00:10:36.740 --> 00:10:37.900
slash v1.

277
00:10:38.040 --> 00:10:40.080
So if there are any other endpoints, so

278
00:10:40.080 --> 00:10:43.980
we have coffee.php, auth.php. What else

279
00:10:43.980 --> 00:10:45.180
can we find?

280
00:10:45.880 --> 00:10:50.420
So come here, word list, user share, word

281
00:10:50.420 --> 00:10:50.900
lists.

282
00:10:52.020 --> 00:10:52.820
We use deb.

283
00:10:53.500 --> 00:10:54.580
We use the big one.

284
00:10:55.400 --> 00:10:58.080
And we want to use the extension php

285
00:10:58.080 --> 00:11:00.540
as well because we know that a lot

286
00:11:00.540 --> 00:11:05.040
of the endpoints have the .php extension on

287
00:11:05.040 --> 00:11:05.580
them too.

288
00:11:07.960 --> 00:11:11.480
So instantly we find coffee and track and

289
00:11:11.480 --> 00:11:12.020
admin.

290
00:11:12.240 --> 00:11:14.140
We haven't seen admin before.

291
00:11:14.140 --> 00:11:18.340
So let's just come back to here and

292
00:11:18.340 --> 00:11:23.180
do slash admin slash v1 slash admin.

293
00:11:23.520 --> 00:11:25.140
And we get a forbidden, which is not

294
00:11:25.140 --> 00:11:25.680
surprising.

295
00:11:26.140 --> 00:11:27.740
But we can continue our attack.

296
00:11:27.880 --> 00:11:30.340
So we can do something like recursion and

297
00:11:30.340 --> 00:11:31.260
turn on recursion.

298
00:11:31.640 --> 00:11:34.160
But often I just like to step through

299
00:11:34.160 --> 00:11:35.420
and see.

300
00:11:35.500 --> 00:11:37.740
It depends on how many endpoints we're dealing

301
00:11:37.740 --> 00:11:38.280
with, really.

302
00:11:38.460 --> 00:11:40.640
So let's do admin slash fuzz.

303
00:11:43.660 --> 00:11:46.820
And we do hit this result, orders.php.

304
00:11:50.960 --> 00:11:54.360
And this looks like it returns all of

305
00:11:54.360 --> 00:11:56.100
the orders for us.

306
00:11:57.300 --> 00:12:00.700
So this is a endpoint without any protection

307
00:12:00.700 --> 00:12:01.540
at all.

308
00:12:01.680 --> 00:12:03.800
So this is a really, really important finding.

309
00:12:04.140 --> 00:12:06.800
And we'd say that, hey, even though it

310
00:12:06.800 --> 00:12:10.340
looks like the frontend application isn't accessing admin,

311
00:12:10.480 --> 00:12:12.740
we didn't see it anywhere in our logs.

312
00:12:12.960 --> 00:12:15.440
That's kind of security through obscurity.

313
00:12:15.920 --> 00:12:18.940
It's hidden in a directory, but we know

314
00:12:18.940 --> 00:12:21.680
that it's quite easy to discover and browse

315
00:12:21.680 --> 00:12:22.760
to directories.

316
00:12:23.220 --> 00:12:25.580
And in the real world, you'll find things

317
00:12:25.580 --> 00:12:29.600
like configuration files in random directories, and you

318
00:12:29.600 --> 00:12:32.940
will find stuff that isn't intended for the

319
00:12:32.940 --> 00:12:35.240
end user, but it's still live on the

320
00:12:35.240 --> 00:12:38.500
site because the frontend simply doesn't point to

321
00:12:38.500 --> 00:12:38.640
it.

322
00:12:38.760 --> 00:12:40.520
Maybe somebody hasn't found it yet.

323
00:12:40.880 --> 00:12:43.320
And I think the last major vulnerability for

324
00:12:43.320 --> 00:12:45.820
us is these order IDs.

325
00:12:46.440 --> 00:12:49.280
So if we grab one of these, we

326
00:12:49.280 --> 00:12:52.900
need to test for broken object level authorization.

327
00:12:53.400 --> 00:12:55.980
So if we come back to localhost, because

328
00:12:55.980 --> 00:12:59.200
we have a track order functionality, we should

329
00:12:59.200 --> 00:13:01.860
only be able to see the orders that

330
00:13:01.860 --> 00:13:02.980
we created.

331
00:13:03.240 --> 00:13:05.080
So if I just log out and I

332
00:13:05.080 --> 00:13:08.460
log in as Alex to make sure that

333
00:13:08.460 --> 00:13:13.260
I'm testing correctly, come to track order, and

334
00:13:13.260 --> 00:13:16.100
if we grab an ID that belongs to

335
00:13:16.100 --> 00:13:18.960
a different email, so we can see this

336
00:13:18.960 --> 00:13:26.090
one belongs to ASD2, paste this in, and

337
00:13:26.090 --> 00:13:28.830
we can indeed see the orders of other

338
00:13:28.830 --> 00:13:29.250
users.

339
00:13:29.390 --> 00:13:31.850
So this is broken object level authorization.

340
00:13:32.510 --> 00:13:33.750
This is Ebola vulnerability.

341
00:13:34.250 --> 00:13:35.610
If you wanted to go a little bit

342
00:13:35.610 --> 00:13:38.270
further, you may be able to harvest these

343
00:13:38.270 --> 00:13:40.730
tokens, take them into burp suite, do some

344
00:13:40.730 --> 00:13:44.650
analysis on them in sequencer, and find some

345
00:13:44.650 --> 00:13:46.690
more information there and see whether you can

346
00:13:46.690 --> 00:13:50.390
actually forge or easily brute force these IDs

347
00:13:50.390 --> 00:13:51.350
as well.

348
00:13:51.710 --> 00:13:54.030
So that's it for the mid-course capstone.

349
00:13:54.250 --> 00:13:56.670
I hope you enjoyed the challenge, and even

350
00:13:56.670 --> 00:13:59.490
though the application isn't very large, I wanted

351
00:13:59.490 --> 00:14:01.230
you to be able to focus on smaller

352
00:14:01.230 --> 00:14:04.110
parts of the application, understand how they work,

353
00:14:04.290 --> 00:14:06.070
and try to exploit them methodically.

354
00:14:06.490 --> 00:14:07.970
From now on, we'll be ramping it up

355
00:14:07.970 --> 00:14:09.510
a little bit and looking at slightly more

356
00:14:09.510 --> 00:14:12.430
complex attacks such as mass assignment and server

357
00:14:12.430 --> 00:14:14.550
-side request forgery, so I hope you enjoy

358
00:14:14.550 --> 00:14:15.630
the rest of the modules.

359
00:14:15.990 --> 00:14:16.950
See you in the next section!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: Mass Assignment

WEBVTT

1
00:00:00.410 --> 00:00:03.390
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Often frameworks or particular styles of coding allow

2
00:00:03.390 --> 00:00:06.230
us to write code that's flexible enough so

3
00:00:06.230 --> 00:00:09.090
that when we sign HTTP parameters to variables,

4
00:00:09.410 --> 00:00:10.790
it's done automatically.

5
00:00:11.270 --> 00:00:13.770
For example, some code might receive a request

6
00:00:13.770 --> 00:00:16.570
that contains information to create a new user.

7
00:00:17.390 --> 00:00:19.310
Some of these requests will have the username,

8
00:00:19.610 --> 00:00:21.790
email, and password to create that user.

9
00:00:22.270 --> 00:00:25.270
Others might include optional fields such as telephone

10
00:00:25.270 --> 00:00:27.890
number, address, favorite cheese, etc.

11
00:00:28.650 --> 00:00:32.450
As a we can sometimes leverage this flexibility

12
00:00:32.450 --> 00:00:35.490
to include or modify parameters that the developers

13
00:00:35.490 --> 00:00:36.710
did not expect.

14
00:00:37.430 --> 00:00:40.050
Parameters that might have some impact elsewhere in

15
00:00:40.050 --> 00:00:40.730
the application.

16
00:00:41.370 --> 00:00:43.490
For example, if all users have a privilege

17
00:00:43.490 --> 00:00:46.090
level by default, we might include a parameter

18
00:00:46.090 --> 00:00:48.670
in our request that sets the privilege level

19
00:00:48.670 --> 00:00:51.230
to 1, overriding the default value.

20
00:00:51.670 --> 00:00:54.430
This is mass assignment and it sits at

21
00:00:54.430 --> 00:00:56.770
the number 6 in the OWASP API top

22
00:00:56.770 --> 00:00:57.550
10 list.

23
00:00:57.990 --> 00:01:00.210
Definitely something we need to understand and test

24
00:01:00.210 --> 00:01:01.990
for when we're working with APIs.

25
00:01:02.470 --> 00:01:04.170
Now, you might be wondering, how do we

26
00:01:04.170 --> 00:01:06.190
find out what the parameter names need to

27
00:01:06.190 --> 00:01:08.170
be in order to exploit this vulnerability?

28
00:01:09.150 --> 00:01:11.990
And this is a great question because if

29
00:01:11.990 --> 00:01:14.210
we didn't know what an application tracked for

30
00:01:14.210 --> 00:01:16.310
its user privileges, and if we didn't know

31
00:01:16.310 --> 00:01:18.770
what the values were, in this example 0

32
00:01:18.770 --> 00:01:20.750
and 1, we may not be able to

33
00:01:20.750 --> 00:01:21.830
exploit this vulnerability.

34
00:01:22.650 --> 00:01:24.390
There are some ways we can find out

35
00:01:24.390 --> 00:01:25.750
this information, however.

36
00:01:25.750 --> 00:01:28.330
First off, if the application is open source,

37
00:01:28.570 --> 00:01:29.870
discovery is fairly trivial.

38
00:01:30.490 --> 00:01:33.870
Second, if the application uses JWTs, we can

39
00:01:33.870 --> 00:01:36.370
decode the token and see the claims of

40
00:01:36.370 --> 00:01:38.430
the user, and then try to set these

41
00:01:38.430 --> 00:01:40.130
claims on new user creation.

42
00:01:40.890 --> 00:01:42.670
We can also look at what information is

43
00:01:42.670 --> 00:01:43.690
returned by endpoints.

44
00:01:43.970 --> 00:01:46.350
So for example, if you browse to slash

45
00:01:46.350 --> 00:01:48.790
account, you may see all of the parameters

46
00:01:48.790 --> 00:01:50.650
tied to your user account returned.

47
00:01:50.970 --> 00:01:52.950
And if you see something like is admin

48
00:01:52.950 --> 00:01:55.270
false, you know you're on the right track.

49
00:01:55.790 --> 00:01:57.390
I think I've mentioned this a few times

50
00:01:57.390 --> 00:01:59.210
throughout the course, but getting to know the

51
00:01:59.210 --> 00:02:02.430
application and understanding its behavior is really key

52
00:02:02.430 --> 00:02:03.510
to being successful.

53
00:02:04.010 --> 00:02:06.390
The discovery and understanding is the hard part.

54
00:02:06.670 --> 00:02:09.250
Exploiting something once you find the vulnerability is

55
00:02:09.250 --> 00:02:10.130
generally trivial.

56
00:02:10.470 --> 00:02:11.910
In the next video, I'll walk you through

57
00:02:11.910 --> 00:02:14.270
some code of an example and demonstrate how

58
00:02:14.270 --> 00:02:16.510
to exploit the mass assignment vulnerability.

59
00:02:17.050 --> 00:02:17.550
See you there!


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.420 --> 00:00:02.420
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, so before we dive into the

2
00:00:02.420 --> 00:00:04.560
hands-on section, I wanted to walk you

3
00:00:04.560 --> 00:00:06.640
through some of the application code.

4
00:00:06.800 --> 00:00:10.220
First, it'll help us understand the vulnerability, and

5
00:00:10.220 --> 00:00:11.700
if you ever need to pass on the

6
00:00:11.700 --> 00:00:14.540
explanation of mass assignment in a report or

7
00:00:14.540 --> 00:00:17.040
a presentation to a client as part of

8
00:00:17.040 --> 00:00:19.280
your work, or maybe to some other developers,

9
00:00:19.700 --> 00:00:22.200
then you're welcome to use this example to

10
00:00:22.200 --> 00:00:22.900
support that.

11
00:00:23.260 --> 00:00:25.800
Secondly, I'm a big believer in code review,

12
00:00:26.220 --> 00:00:28.340
so if this is something that you're not

13
00:00:28.340 --> 00:00:30.900
used to but want to improve, then small

14
00:00:30.900 --> 00:00:33.200
applications like this are a great place to

15
00:00:33.200 --> 00:00:33.560
start.

16
00:00:34.040 --> 00:00:34.980
Let's take a look.

17
00:00:35.220 --> 00:00:36.640
I'm just going to pull you over to

18
00:00:36.640 --> 00:00:39.040
my VM, and what we're going to do

19
00:00:39.040 --> 00:00:41.460
is you can see that we have the

20
00:00:41.460 --> 00:00:45.860
apimassassignment.zip as usual, so we can just

21
00:00:45.860 --> 00:00:54.340
unzip apimassassignment, clear this, cd into apimassassignment, and

22
00:00:54.340 --> 00:00:56.480
then we can see the files in here.

23
00:00:56.940 --> 00:00:58.460
So I'm just going to open this up

24
00:00:58.460 --> 00:01:01.960
in Visual Studio Code, and we're going to

25
00:01:01.960 --> 00:01:04.160
take a quick look, so let's start off

26
00:01:04.160 --> 00:01:08.180
with index.js. We can see that line

27
00:01:08.180 --> 00:01:12.300
1 imports Express, and Express is a node

28
00:01:12.300 --> 00:01:15.340
framework that basically provides tools and functionality for

29
00:01:15.340 --> 00:01:17.780
us to create web applications a little bit

30
00:01:17.780 --> 00:01:18.380
more easily.

31
00:01:18.540 --> 00:01:19.900
Let me make this a little bit bigger

32
00:01:19.900 --> 00:01:22.960
for you, and also probably just move myself

33
00:01:22.960 --> 00:01:24.340
out of the way, because I will be

34
00:01:24.340 --> 00:01:25.620
in the way at some point.

35
00:01:26.160 --> 00:01:30.020
Next, we have Mongoose, which basically provides us

36
00:01:30.020 --> 00:01:32.780
with a way to interact with MongoDB using

37
00:01:32.780 --> 00:01:36.480
JavaScript objects and data structures, and if you're

38
00:01:36.480 --> 00:01:38.600
not sure what a data structure is, then

39
00:01:38.600 --> 00:01:40.520
we'll talk a little bit more about it

40
00:01:40.520 --> 00:01:42.300
in a minute when we come to look

41
00:01:42.300 --> 00:01:43.180
at our user.

42
00:01:43.860 --> 00:01:46.560
So the next line is const app equals

43
00:01:46.560 --> 00:01:47.160
Express.

44
00:01:47.420 --> 00:01:50.300
This creates an instance of the Express application,

45
00:01:50.940 --> 00:01:54.380
and then we have appset viewengine ejs.

46
00:01:54.560 --> 00:01:56.920
Now, this is for a templating engine that

47
00:01:56.920 --> 00:01:59.380
I like to use, which is ejs, and

48
00:01:59.380 --> 00:02:03.080
basically lets you embed JavaScript code into HTML

49
00:02:03.080 --> 00:02:03.880
templates.

50
00:02:04.300 --> 00:02:05.440
Nothing really out of the ordinary.

51
00:02:06.000 --> 00:02:07.120
Maybe we'll take a quick look at the

52
00:02:07.120 --> 00:02:08.139
template in a minute.

53
00:02:08.479 --> 00:02:12.240
app.use express.urlencoded. This line tells our

54
00:02:12.240 --> 00:02:15.540
application to use Express's urlencoded middleware.

55
00:02:15.940 --> 00:02:18.340
And the next line is Mongoose, so this

56
00:02:18.340 --> 00:02:19.600
is quite an important line.

57
00:02:20.120 --> 00:02:23.440
This block connects to the Mongo database using

58
00:02:23.440 --> 00:02:25.140
Mongoose's connect function.

59
00:02:25.480 --> 00:02:30.560
The database is at mongodb, mongo, 27017, and

60
00:02:30.560 --> 00:02:34.000
then slash nosqli-demo, and you can see

61
00:02:34.000 --> 00:02:36.680
that obviously I copied and pasted the previous

62
00:02:36.680 --> 00:02:38.200
lab to save a little bit of time,

63
00:02:38.360 --> 00:02:40.640
rather than creating it from scratch.

64
00:02:40.940 --> 00:02:43.260
And if the connection is successful, we get

65
00:02:43.260 --> 00:02:46.140
the .then method, which logs a message to

66
00:02:46.140 --> 00:02:48.360
MongoDB saying MongoDB connected.

67
00:02:49.520 --> 00:02:51.200
And when you run this, hopefully that's what

68
00:02:51.200 --> 00:02:52.000
you'll see in the log.

69
00:02:52.320 --> 00:02:55.460
And if it's unsuccessful, it'll trigger the .catch

70
00:02:55.460 --> 00:02:58.020
method, which will print the error message to

71
00:02:58.020 --> 00:02:58.560
the console.

72
00:02:58.900 --> 00:03:01.520
Next up, we have const user equals require,

73
00:03:01.780 --> 00:03:03.200
and then models slash user.

74
00:03:03.480 --> 00:03:06.480
Here, we're actually importing the user model from

75
00:03:06.480 --> 00:03:08.340
models slash user.

76
00:03:08.900 --> 00:03:11.700
Now, this represents the schema for user data,

77
00:03:12.360 --> 00:03:14.280
and you might be thinking, what the heck

78
00:03:14.280 --> 00:03:15.780
is a schema for a user?

79
00:03:16.260 --> 00:03:18.440
A schema is essentially a way of defining

80
00:03:18.440 --> 00:03:21.160
the structure and validation rules for the data

81
00:03:21.160 --> 00:03:22.860
that will be stored in the database.

82
00:03:23.560 --> 00:03:25.920
For example, the schema might say that all

83
00:03:25.920 --> 00:03:28.340
the users require a username and a password,

84
00:03:28.700 --> 00:03:30.580
and that the password is not allowed to

85
00:03:30.580 --> 00:03:33.300
be null, and the maximum length is 50

86
00:03:33.300 --> 00:03:33.760
characters.

87
00:03:33.760 --> 00:03:37.360
These constraints are all reflected in the schema.

88
00:03:37.620 --> 00:03:40.500
In fact, let's take a quick look at

89
00:03:40.500 --> 00:03:42.740
user.js. So, if we come into models

90
00:03:42.740 --> 00:03:46.460
and user.js, we have our first two

91
00:03:46.460 --> 00:03:46.820
lines.

92
00:03:47.220 --> 00:03:52.280
So, these two lines import the Mongoose library

93
00:03:52.280 --> 00:03:54.500
and create a new instance of the schema

94
00:03:54.500 --> 00:03:56.300
class that's provided by Mongoose.

95
00:03:56.860 --> 00:03:58.820
And as we now know, the schema class

96
00:03:58.820 --> 00:04:00.900
is used to define the structure and validation

97
00:04:00.900 --> 00:04:03.620
rules for data that we're going to store.

98
00:04:03.960 --> 00:04:06.300
This next section is our user schema.

99
00:04:07.180 --> 00:04:08.280
We have three fields.

100
00:04:08.500 --> 00:04:11.500
So, we have username, password, and privileges, and

101
00:04:11.500 --> 00:04:14.020
we also have some validation or constraints around

102
00:04:14.020 --> 00:04:14.940
these as well.

103
00:04:15.100 --> 00:04:16.760
So, for example, they all need to be

104
00:04:16.760 --> 00:04:20.579
strings, and the username and password are required.

105
00:04:21.540 --> 00:04:24.220
And also, the default value, oh, sorry, all

106
00:04:24.220 --> 00:04:25.880
three are required.

107
00:04:26.560 --> 00:04:30.800
So, username, password, privileges, and the default privilege

108
00:04:30.800 --> 00:04:31.680
is user.

109
00:04:32.000 --> 00:04:36.300
This final line, module.exports, equals user, Mongoose

110
00:04:36.300 --> 00:04:37.800
.model, user, user schema.

111
00:04:38.400 --> 00:04:41.060
This final line exports the user model so

112
00:04:41.060 --> 00:04:42.860
that we can use it in other files.

113
00:04:43.360 --> 00:04:45.060
And as we just saw in our index

114
00:04:45.060 --> 00:04:48.940
.js, the user equals require model slash user,

115
00:04:49.320 --> 00:04:52.280
it basically makes this schema available for us

116
00:04:52.280 --> 00:04:55.340
elsewhere in the application, and also allows us

117
00:04:55.340 --> 00:04:58.600
to do things like user.find, user.create,

118
00:04:58.780 --> 00:05:00.100
very handy stuff.

119
00:05:00.340 --> 00:05:03.280
So, coming back to the main index file,

120
00:05:03.640 --> 00:05:05.520
think of this as the rules we use

121
00:05:05.520 --> 00:05:08.340
to describe the constraints of our objects, such

122
00:05:08.340 --> 00:05:12.160
as users, products, posts, messages, and anything else

123
00:05:12.160 --> 00:05:14.580
that can be quantified within our web applications.

124
00:05:15.100 --> 00:05:16.680
Now, next up, we have some routing.

125
00:05:17.180 --> 00:05:19.760
So, our index page, this will trigger when

126
00:05:19.760 --> 00:05:21.820
a get request is sent to the root

127
00:05:21.820 --> 00:05:22.860
URL, so slash.

128
00:05:23.000 --> 00:05:26.540
So, if the website is www.tcm-sec

129
00:05:26.540 --> 00:05:29.160
.com, if you just go to that top

130
00:05:29.160 --> 00:05:31.780
level address, then this will be triggered.

131
00:05:31.980 --> 00:05:34.120
So, when this happens, we use the user

132
00:05:34.120 --> 00:05:37.060
.find method to grab all of the users

133
00:05:37.060 --> 00:05:39.260
out of the database, and then we render

134
00:05:39.260 --> 00:05:42.080
the index template, and we pass in the

135
00:05:42.080 --> 00:05:43.280
users that were found.

136
00:05:43.680 --> 00:05:45.980
After this, we have slash register.

137
00:05:46.420 --> 00:05:48.460
So, similar to the previous block of code,

138
00:05:48.780 --> 00:05:51.760
except that this will only accept post requests.

139
00:05:52.420 --> 00:05:54.660
So, if you post some data to slash

140
00:05:54.660 --> 00:05:58.840
register, this will trigger, and we have a

141
00:05:58.840 --> 00:06:02.140
const new user, which creates a new user

142
00:06:02.140 --> 00:06:05.520
object using the request body data, so the

143
00:06:05.520 --> 00:06:08.780
data that you're sending in the request, and

144
00:06:08.780 --> 00:06:11.260
then it saves this to the database.

145
00:06:11.460 --> 00:06:13.580
So, user.save, and then it saves this

146
00:06:13.580 --> 00:06:16.780
to the database using the new user.save

147
00:06:16.780 --> 00:06:17.320
method.

148
00:06:17.800 --> 00:06:20.200
Once the user data is saved, the application

149
00:06:20.200 --> 00:06:23.340
redirects us to the root URL.

150
00:06:23.720 --> 00:06:25.260
Next up, we have clear.

151
00:06:25.460 --> 00:06:27.700
I just added this so you had an

152
00:06:27.700 --> 00:06:29.720
easy way to clear the database if things

153
00:06:29.720 --> 00:06:32.040
got a little crazy with adding users and

154
00:06:32.040 --> 00:06:32.480
fuzzing.

155
00:06:32.880 --> 00:06:35.840
Something to consider when working on production environments

156
00:06:35.840 --> 00:06:39.280
is that the staff maintaining the application might

157
00:06:39.280 --> 00:06:42.420
not appreciate 10,000 new users, and in

158
00:06:42.420 --> 00:06:44.400
some bug bounty agreements, if you read through

159
00:06:44.400 --> 00:06:46.060
them, it might say that you're not allowed

160
00:06:46.060 --> 00:06:48.900
to carry out attacks that create excessive amounts

161
00:06:48.900 --> 00:06:51.680
of data or database entries like this.

162
00:06:51.820 --> 00:06:53.920
So, just be cautious when working on production

163
00:06:53.920 --> 00:06:54.580
applications.

164
00:06:55.440 --> 00:06:57.560
So, here we have a get request to

165
00:06:57.560 --> 00:06:58.180
slash clear.

166
00:06:58.380 --> 00:07:00.760
The application deletes all of the user data

167
00:07:00.760 --> 00:07:04.380
from the database using the user.deleteMany method,

168
00:07:04.500 --> 00:07:06.400
then forwards the user back to the root

169
00:07:06.400 --> 00:07:06.800
address.

170
00:07:07.300 --> 00:07:09.360
By the way, if you're interested in learning

171
00:07:09.360 --> 00:07:11.620
more about how to build web applications such

172
00:07:11.620 --> 00:07:14.500
as these, I personally like Brad Traversi's courses.

173
00:07:15.280 --> 00:07:17.320
I'm by no means associated with him, but

174
00:07:17.320 --> 00:07:19.420
I find that his courses are practical and

175
00:07:19.420 --> 00:07:20.480
the videos are good.

176
00:07:20.700 --> 00:07:22.340
I use them myself to keep up to

177
00:07:22.340 --> 00:07:24.760
date with development practices and technologies that I

178
00:07:24.760 --> 00:07:26.820
want to learn, so you can easily find

179
00:07:26.820 --> 00:07:28.020
his content on YouTube.

180
00:07:28.700 --> 00:07:30.480
I hope that this quick run-through of

181
00:07:30.480 --> 00:07:33.140
the code was helpful, and don't worry if

182
00:07:33.140 --> 00:07:34.900
it was a little overwhelming for now.

183
00:07:35.160 --> 00:07:36.480
We're going to run through the lab in

184
00:07:36.480 --> 00:07:38.400
the next video, so I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.270 --> 00:00:03.010
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, let's take a look at the

2
00:00:03.010 --> 00:00:03.970
hands-on lab.

3
00:00:04.170 --> 00:00:07.710
So I'm just going to sudo docker compose

4
00:00:07.710 --> 00:00:08.090
up.

5
00:00:09.010 --> 00:00:11.730
Give it a second to build the lab.

6
00:00:14.340 --> 00:00:15.580
Fingers crossed it works.

7
00:00:20.820 --> 00:00:22.540
So you can see that I've done a

8
00:00:22.540 --> 00:00:24.860
little bit of testing before, and so what

9
00:00:24.860 --> 00:00:25.860
I'm going to do is I'm just going

10
00:00:25.860 --> 00:00:27.640
to go to slash clear, which is an

11
00:00:27.640 --> 00:00:29.780
endpoint that I put in so that it

12
00:00:29.780 --> 00:00:31.320
just clears out the database for you.

13
00:00:31.360 --> 00:00:33.480
So if you're doing some testing and fuzzing

14
00:00:33.480 --> 00:00:35.260
and things like that, I think we saw

15
00:00:35.260 --> 00:00:37.300
the code in the code review in the

16
00:00:37.300 --> 00:00:39.080
last video, you can just go to slash

17
00:00:39.080 --> 00:00:41.000
clear, and then everything gets cleared out.

18
00:00:41.200 --> 00:00:44.580
So let's create a new user called Jeremy,

19
00:00:44.820 --> 00:00:47.280
and his password is just going to be

20
00:00:47.280 --> 00:00:48.680
something random like cheesecake.

21
00:00:49.400 --> 00:00:51.800
And you can see here, maybe text is

22
00:00:51.800 --> 00:00:53.940
a little bit small, that we have Jeremy,

23
00:00:54.280 --> 00:00:55.660
cheesecake, and user.

24
00:00:56.140 --> 00:00:59.200
And this user parameter is the privilege level.

25
00:01:00.000 --> 00:01:02.300
So what I want to do is here

26
00:01:02.300 --> 00:01:04.300
it says we can add some users by

27
00:01:04.300 --> 00:01:07.180
posting to slash register, or we could capture

28
00:01:07.180 --> 00:01:09.440
this request in bubsuite and then head to

29
00:01:09.440 --> 00:01:10.020
the repeater.

30
00:01:10.180 --> 00:01:12.340
But in this video, we'll use postman to

31
00:01:12.340 --> 00:01:13.160
do this.

32
00:01:13.540 --> 00:01:15.580
So what I'm going to do is I'm

33
00:01:15.580 --> 00:01:20.320
just going to hit new, HTTP request, and

34
00:01:20.320 --> 00:01:22.380
then there's a little useful icon down here

35
00:01:22.380 --> 00:01:24.340
that just hides the sidebar for us.

36
00:01:24.700 --> 00:01:26.560
And what we want to do is we

37
00:01:26.560 --> 00:01:32.300
want to post to HTTP localhost slash register,

38
00:01:32.580 --> 00:01:34.980
you can see I've already tested this, and

39
00:01:34.980 --> 00:01:37.240
we want to come into the body.

40
00:01:38.720 --> 00:01:40.480
And I'm pretty sure this is a form.

41
00:01:40.680 --> 00:01:43.160
So I'm just going to use the x

42
00:01:43.160 --> 00:01:46.440
www form URL and code, but you can

43
00:01:46.440 --> 00:01:49.060
double check this by intercepting the request or

44
00:01:49.060 --> 00:01:50.400
inspecting it further.

45
00:01:50.820 --> 00:01:53.340
So I'm just going to put in a

46
00:01:53.340 --> 00:01:53.900
username.

47
00:01:54.180 --> 00:01:57.660
And let's call this jessamy.

48
00:01:58.180 --> 00:02:00.140
And I'm going to put in a password.

49
00:02:00.540 --> 00:02:03.580
And jessamy's password is tiramisu.

50
00:02:04.160 --> 00:02:06.240
And let's send this to see whether this

51
00:02:06.240 --> 00:02:06.680
works.

52
00:02:07.259 --> 00:02:08.759
And we get a response back here.

53
00:02:08.880 --> 00:02:10.780
So I'm just going to scroll down in

54
00:02:10.780 --> 00:02:11.840
the response quickly.

55
00:02:12.000 --> 00:02:13.120
So I know it's kind of hard to

56
00:02:13.120 --> 00:02:13.360
see.

57
00:02:13.820 --> 00:02:17.180
But you can see we have jessamy, tiramisu

58
00:02:17.180 --> 00:02:20.140
and user and we can verify this in

59
00:02:20.140 --> 00:02:21.600
the UI as well.

60
00:02:23.100 --> 00:02:25.980
So to sign up a admin user, what

61
00:02:25.980 --> 00:02:28.760
we need to understand is where this user

62
00:02:28.760 --> 00:02:30.240
parameter is coming from.

63
00:02:30.720 --> 00:02:31.780
So there's a couple of ways to do

64
00:02:31.780 --> 00:02:34.200
this, as I think I mentioned in the

65
00:02:34.200 --> 00:02:35.020
introduction video.

66
00:02:35.400 --> 00:02:37.820
Obviously, if you have access to the application

67
00:02:37.820 --> 00:02:39.940
source code, it's very easy to find out

68
00:02:39.940 --> 00:02:42.740
because we can just come in and take

69
00:02:42.740 --> 00:02:44.580
a look at the user schema.

70
00:02:45.240 --> 00:02:47.560
And we can see that we have privileges

71
00:02:47.560 --> 00:02:47.980
here.

72
00:02:48.400 --> 00:02:50.180
We can also look at things like the

73
00:02:50.180 --> 00:02:53.480
account page, the JWT token, and all sorts

74
00:02:53.480 --> 00:02:55.100
of other things, we could fuzz for it

75
00:02:55.100 --> 00:02:55.520
as well.

76
00:02:55.620 --> 00:02:58.100
So we could send this to intruder and

77
00:02:58.100 --> 00:03:00.540
create thousands of users and see whether we

78
00:03:00.540 --> 00:03:03.140
get one that's created as the administrator.

79
00:03:03.760 --> 00:03:05.980
So I'm just going to put privilege and

80
00:03:05.980 --> 00:03:08.180
I'm going to try and put this as

81
00:03:08.180 --> 00:03:10.340
admin and we'll just call this jessamy2.

82
00:03:11.580 --> 00:03:13.860
And then we'll just come back to the

83
00:03:13.860 --> 00:03:16.680
UI and we're still user.

84
00:03:18.720 --> 00:03:22.020
Ah, because privilege is not privilege.

85
00:03:22.320 --> 00:03:25.100
We'll send this again, we see that there's

86
00:03:25.100 --> 00:03:26.860
no check in the DB to see whether

87
00:03:26.860 --> 00:03:28.580
the usernames are unique, but that's okay.

88
00:03:29.020 --> 00:03:32.840
And we have indeed created a admin user.

89
00:03:33.140 --> 00:03:36.420
This is mass assignments, this vulnerability right here.

90
00:03:36.520 --> 00:03:38.980
So it's actually quite simple once you kind

91
00:03:38.980 --> 00:03:41.220
of understand the application, how it's handling things,

92
00:03:41.220 --> 00:03:44.380
but obviously gaining that understanding can take time,

93
00:03:44.580 --> 00:03:45.780
can take a lot of analysis.

94
00:03:46.120 --> 00:03:47.800
But now you know the theory, you can

95
00:03:47.800 --> 00:03:51.000
apply that to your next engagement or scenario.

96
00:03:52.140 --> 00:03:54.380
So let's take a look at the vulnerable

97
00:03:54.380 --> 00:03:55.220
line of code.

98
00:03:55.500 --> 00:03:57.460
So if we just come back to Visual

99
00:03:57.460 --> 00:04:01.040
Studio code, come back to here, and here

100
00:04:01.040 --> 00:04:03.180
we have our vulnerable line of code.

101
00:04:03.500 --> 00:04:05.620
And if you want to pause the video

102
00:04:05.620 --> 00:04:07.200
a second and kind of do a little

103
00:04:07.200 --> 00:04:09.520
bit of research and figure out the reasoning

104
00:04:09.520 --> 00:04:11.880
behind it, by all means, feel free to

105
00:04:11.880 --> 00:04:12.820
pause the video and do that.

106
00:04:12.940 --> 00:04:16.560
It's good code review practice to understand small

107
00:04:16.560 --> 00:04:17.519
snippets of code.

108
00:04:17.899 --> 00:04:20.000
And I'll see you in a second if

109
00:04:20.000 --> 00:04:20.459
you did pause.

110
00:04:21.460 --> 00:04:25.240
All right, so the issue here is that

111
00:04:25.240 --> 00:04:27.980
we're using this dot dot dot, which is

112
00:04:27.980 --> 00:04:29.460
the spread operator.

113
00:04:30.180 --> 00:04:33.460
And this is used to pass parameters or

114
00:04:33.460 --> 00:04:37.560
properties from the request.body into our user

115
00:04:37.560 --> 00:04:38.240
object.

116
00:04:38.580 --> 00:04:40.940
And what it'll do is it'll automatically pass

117
00:04:40.940 --> 00:04:42.260
all of them in there.

118
00:04:42.320 --> 00:04:45.400
So in our postman request, for example, if

119
00:04:45.400 --> 00:04:47.860
I also define something like, I don't know,

120
00:04:48.560 --> 00:04:53.180
cheese and I put parmesan, it would try

121
00:04:53.180 --> 00:04:54.060
and pass that in.

122
00:04:54.400 --> 00:04:57.000
Now we do have the limitation of our

123
00:04:57.000 --> 00:04:59.580
schema, so that wouldn't get passed into the

124
00:04:59.580 --> 00:05:01.700
database, but it would still try and pass

125
00:05:01.700 --> 00:05:03.040
it into our object.

126
00:05:03.520 --> 00:05:05.020
A more secure way of writing this would

127
00:05:05.020 --> 00:05:12.600
be something like request.body. username, and request

128
00:05:12.600 --> 00:05:18.100
.body.password. And then the user can never

129
00:05:18.100 --> 00:05:21.700
define the privilege parameter, or the privileges parameter.

130
00:05:22.340 --> 00:05:25.580
And by default, our schema, it's created as

131
00:05:25.580 --> 00:05:26.120
user.

132
00:05:26.680 --> 00:05:28.100
And then probably what we would do is

133
00:05:28.100 --> 00:05:31.520
we'd implement some administrative functionality later on that

134
00:05:31.520 --> 00:05:35.320
allows the upgrade of users to admins, for

135
00:05:35.320 --> 00:05:35.800
example.

136
00:05:36.060 --> 00:05:38.200
But here, we don't want to include that

137
00:05:38.200 --> 00:05:38.700
functionality.

138
00:05:39.020 --> 00:05:42.280
So being quite specific is quite important when

139
00:05:42.280 --> 00:05:43.600
we're writing code like this.

140
00:05:43.820 --> 00:05:45.360
And one last thing I want to do

141
00:05:45.360 --> 00:05:47.600
before I give you all a challenge to

142
00:05:47.600 --> 00:05:50.700
take a look at is let's come and

143
00:05:50.700 --> 00:05:53.320
check the database and see, we sent a

144
00:05:53.320 --> 00:05:55.800
few different requests and see what's actually in

145
00:05:55.800 --> 00:05:55.980
there.

146
00:05:56.080 --> 00:06:00.540
So let's do sudo docker dsa.

147
00:06:01.720 --> 00:06:04.400
We have a couple of images here.

148
00:06:04.580 --> 00:06:08.080
So we want the Mongo one.

149
00:06:08.700 --> 00:06:14.000
And then sudo docker exec-it, drop into

150
00:06:14.000 --> 00:06:21.060
a shell, Mongo, show DBs, use Mongo mass,

151
00:06:21.340 --> 00:06:27.210
whoops, assignments, and then show collections.

152
00:06:28.430 --> 00:06:30.070
And then what we want to do is

153
00:06:30.070 --> 00:06:33.810
db.users.find like this.

154
00:06:34.150 --> 00:06:36.270
And then we can see everything that's in

155
00:06:36.270 --> 00:06:36.650
the database.

156
00:06:36.910 --> 00:06:38.210
So if you want to come in and

157
00:06:38.210 --> 00:06:40.490
see what you've done, or see how things

158
00:06:40.490 --> 00:06:42.370
have been entered into the database, you can

159
00:06:42.370 --> 00:06:43.230
come in and take a look.

160
00:06:43.770 --> 00:06:47.110
And when we accidentally sent jessamy, for example,

161
00:06:47.110 --> 00:06:50.210
with the privilege, instead of privileges, you can

162
00:06:50.210 --> 00:06:53.350
see that that value wasn't inserted again.

163
00:06:53.610 --> 00:06:56.810
So this data is conforming to the data

164
00:06:56.810 --> 00:06:58.850
structure that we set out, the user schema

165
00:06:58.850 --> 00:07:00.650
that we set out in our code.

166
00:07:01.070 --> 00:07:03.330
It won't just insert anything.

167
00:07:03.810 --> 00:07:04.230
All right.

168
00:07:04.350 --> 00:07:06.570
So as always, I have a little challenge

169
00:07:06.570 --> 00:07:07.770
for you as well.

170
00:07:07.970 --> 00:07:10.010
And then in the final video, we'll do

171
00:07:10.010 --> 00:07:11.590
a walkthrough of the challenge.

172
00:07:12.550 --> 00:07:15.270
So I'm just going to come out of

173
00:07:15.270 --> 00:07:15.570
this.

174
00:07:15.710 --> 00:07:17.430
In fact, let me pause for a second.

175
00:07:17.730 --> 00:07:19.470
And I'm going to spin up the crappy

176
00:07:19.470 --> 00:07:20.050
application.

177
00:07:20.390 --> 00:07:21.530
And I'll see you back here in a

178
00:07:21.530 --> 00:07:21.850
second.

179
00:07:22.410 --> 00:07:23.290
All right.

180
00:07:23.450 --> 00:07:24.890
It's challenge time.

181
00:07:25.350 --> 00:07:27.390
I'd like you to log into the crappy

182
00:07:27.390 --> 00:07:29.990
application and come to the shop page.

183
00:07:30.390 --> 00:07:33.310
Now, if we intercept the traffic, I'm just

184
00:07:33.310 --> 00:07:36.610
going to hit refresh, we'll see that we

185
00:07:36.610 --> 00:07:39.050
have this endpoint slash products.

186
00:07:39.530 --> 00:07:41.550
And this is the endpoint that I'd like

187
00:07:41.550 --> 00:07:43.730
you to work on to find this vulnerability.

188
00:07:44.770 --> 00:07:47.410
And if you're able to successfully exploit this

189
00:07:47.410 --> 00:07:50.590
vulnerability, you should be able to increase your

190
00:07:50.590 --> 00:07:51.570
account's balance.

191
00:07:51.950 --> 00:07:53.190
I do have one hint for you.

192
00:07:53.430 --> 00:07:55.270
But if you feel ready for the challenge,

193
00:07:55.370 --> 00:07:57.210
then feel free to stop the video here

194
00:07:57.210 --> 00:07:58.290
and dive straight in.

195
00:07:58.490 --> 00:08:00.310
And I'll catch up with you with you

196
00:08:00.310 --> 00:08:01.130
in the next one.

197
00:08:01.590 --> 00:08:03.850
If you do want the hint, then what

198
00:08:03.850 --> 00:08:06.650
I recommend is that don't just consider the

199
00:08:06.650 --> 00:08:08.910
payload that you're sending to this endpoint.

200
00:08:09.370 --> 00:08:12.290
Also consider the type of request you're sending

201
00:08:12.290 --> 00:08:13.070
as well.

202
00:08:13.350 --> 00:08:13.910
Give it a try.

203
00:08:14.130 --> 00:08:15.810
And as always, we'll walk through it together

204
00:08:15.810 --> 00:08:16.670
in the next video.

205
00:08:16.870 --> 00:08:17.470
I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.230 --> 00:00:02.670
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome back to the final video

2
00:00:02.670 --> 00:00:03.810
of this section.

3
00:00:04.110 --> 00:00:05.830
I hope you enjoyed the challenge.

4
00:00:06.090 --> 00:00:08.390
Congratulations if you solved it, and if you

5
00:00:08.390 --> 00:00:10.410
didn't solve it, as always, let's walk through

6
00:00:10.410 --> 00:00:12.330
it together and make sure you take good

7
00:00:12.330 --> 00:00:12.670
notes.

8
00:00:13.130 --> 00:00:14.690
Let's dive straight in.

9
00:00:16.110 --> 00:00:19.310
So here I have the crappy application as

10
00:00:19.310 --> 00:00:21.670
I just showed you all, and if we

11
00:00:21.670 --> 00:00:25.110
switch to Verbsuite, we have the endpoint that

12
00:00:25.110 --> 00:00:26.010
we want to attack.

13
00:00:26.190 --> 00:00:28.510
And I'm going to fuzz this endpoint really

14
00:00:28.510 --> 00:00:32.470
quickly, both with Intruder and FFUF, and see

15
00:00:32.470 --> 00:00:34.070
what results we get back.

16
00:00:34.250 --> 00:00:35.750
So I'm just going to hit Ctrl-I,

17
00:00:35.870 --> 00:00:39.370
send to Intruder, and I'm going to add

18
00:00:39.370 --> 00:00:42.990
our payload marker here, and then come to

19
00:00:42.990 --> 00:00:45.950
payloads, and I think in Verbsuite there is

20
00:00:45.950 --> 00:00:49.030
a HTTP verbs list.

21
00:00:49.130 --> 00:00:49.870
Yes, there it is.

22
00:00:50.490 --> 00:00:52.150
And then we can just hit start.

23
00:00:52.350 --> 00:00:54.290
So it's going to get post, head, connect,

24
00:00:54.430 --> 00:00:55.450
etc, etc.

25
00:00:56.010 --> 00:00:58.070
And as you can see, we get a

26
00:00:58.070 --> 00:01:03.349
200 response on things like get, head, options,

27
00:01:05.930 --> 00:01:07.370
can't see any others.

28
00:01:09.490 --> 00:01:11.830
So these are the request types that we

29
00:01:11.830 --> 00:01:15.310
should be analyzing or targeting in our pen

30
00:01:15.310 --> 00:01:17.790
test, or in our analysis.

31
00:01:18.470 --> 00:01:20.090
And if you want to do this in

32
00:01:20.090 --> 00:01:23.090
FFUF, let's quickly come over to the terminal,

33
00:01:23.710 --> 00:01:32.430
and we'll just do FFUF-U HTTP//localhost 8888,

34
00:01:32.430 --> 00:01:34.610
and then I just need the endpoint which

35
00:01:34.610 --> 00:01:36.790
I'm going to grab from Verbsuite.

36
00:01:40.630 --> 00:01:43.570
And then our word list, so users share

37
00:01:43.570 --> 00:01:46.690
seclists, and I always forget where the word

38
00:01:46.690 --> 00:01:49.770
lists are in here because it's not, in

39
00:01:49.770 --> 00:01:53.290
my opinion, laid out that well, but that's

40
00:01:53.290 --> 00:01:53.610
okay.

41
00:01:54.630 --> 00:01:58.590
And I think, yeah, we have HTTP request

42
00:01:58.590 --> 00:02:00.410
methods that we can use.

43
00:02:00.890 --> 00:02:02.990
And then we just do dash X for

44
00:02:02.990 --> 00:02:07.130
the request type, or the HTTP verb.

45
00:02:08.110 --> 00:02:09.830
And here you can see we get similar

46
00:02:09.830 --> 00:02:14.370
results, so we get 204 options, for example,

47
00:02:15.150 --> 00:02:19.350
and we have 401 for post, probably because

48
00:02:19.350 --> 00:02:20.710
there's no data.

49
00:02:20.870 --> 00:02:23.010
Interesting that this is different to what Verbsuite

50
00:02:23.010 --> 00:02:25.950
gave us, but different to the 405, which

51
00:02:25.950 --> 00:02:27.470
is the majority of them.

52
00:02:27.830 --> 00:02:29.650
So, and we can actually get rid of

53
00:02:29.650 --> 00:02:35.150
these by just doing dash FC 405, and

54
00:02:35.150 --> 00:02:37.410
then it gives us a slightly neater result,

55
00:02:37.530 --> 00:02:39.450
so just in case you missed that, dash

56
00:02:39.450 --> 00:02:42.050
FC will filter out all of the 405

57
00:02:42.050 --> 00:02:42.590
responses.

58
00:02:43.090 --> 00:02:46.390
So, options head, get, and post are the

59
00:02:46.390 --> 00:02:48.370
request types that we want to be using

60
00:02:48.370 --> 00:02:50.210
to analyze this endpoint.

61
00:02:51.070 --> 00:02:53.310
So, let's take a closer look at this

62
00:02:53.310 --> 00:02:54.930
endpoint now in repeater.

63
00:02:55.150 --> 00:02:57.550
So, I just hit control R for repeater,

64
00:02:58.090 --> 00:03:00.770
and let's send this request and see what

65
00:03:00.770 --> 00:03:01.330
comes back.

66
00:03:01.370 --> 00:03:03.770
And it comes back with a bunch of

67
00:03:03.770 --> 00:03:07.010
products, which, of course, are the two products

68
00:03:07.010 --> 00:03:08.410
that are on the page.

69
00:03:09.090 --> 00:03:11.710
Now, if we change this to post, for

70
00:03:11.710 --> 00:03:15.190
example, and send this, we get back 400

71
00:03:15.190 --> 00:03:18.150
bad requests, but we actually get back a

72
00:03:18.150 --> 00:03:22.710
bunch of variables or parameters that we might

73
00:03:22.710 --> 00:03:24.450
be able to use in an attack.

74
00:03:25.470 --> 00:03:28.270
We could also discover this by looking at

75
00:03:28.270 --> 00:03:31.090
the traffic, so we have ID, name, price,

76
00:03:31.290 --> 00:03:33.150
image URL, so these are quite easy to

77
00:03:33.150 --> 00:03:35.250
find, but these are the parameters that we're

78
00:03:35.250 --> 00:03:38.170
going to, like, inject into using our mass

79
00:03:38.170 --> 00:03:39.370
assignment vulnerability.

80
00:03:40.490 --> 00:03:43.270
So, if I just come here and use

81
00:03:43.270 --> 00:03:48.190
extensions, content type converter, convert to JSON, and

82
00:03:48.190 --> 00:03:50.190
then what I want to do is in

83
00:03:50.190 --> 00:03:52.150
my request, I want to add a name,

84
00:03:53.310 --> 00:03:56.530
and then let's just switch this to raw.

85
00:03:56.690 --> 00:03:58.570
It's a little bit easier to work with,

86
00:04:01.550 --> 00:04:04.990
and we're going to want three variables.

87
00:04:06.730 --> 00:04:09.850
So, we want price, and then we want

88
00:04:09.850 --> 00:04:11.770
image URL.

89
00:04:12.690 --> 00:04:17.430
So, here, let's put in some cheesecake, and

90
00:04:17.430 --> 00:04:19.730
the price, what we're going to do is

91
00:04:19.730 --> 00:04:21.990
we're going to put this to minus 500,

92
00:04:22.610 --> 00:04:27.270
and then the URL, let's just find a

93
00:04:27.270 --> 00:04:33.960
picture, copy image link, and we'll use the

94
00:04:33.960 --> 00:04:38.080
same one, so local host images, seat.svg,

95
00:04:38.360 --> 00:04:41.820
and interesting that that's a SVG, which is

96
00:04:41.820 --> 00:04:43.500
a scalable vector graphic.

97
00:04:43.660 --> 00:04:45.840
I think this is based off XML, so

98
00:04:45.840 --> 00:04:48.780
maybe if we have image upload, we also

99
00:04:48.780 --> 00:04:52.860
have XML injection via this as well.

100
00:04:53.540 --> 00:04:56.700
Anyway, I digress, and what we want to

101
00:04:56.700 --> 00:05:00.860
do is basically just send this request, and

102
00:05:00.860 --> 00:05:08.040
we get JSON pass error, expected property, this

103
00:05:08.040 --> 00:05:10.940
is because I had one extra comma, and

104
00:05:10.940 --> 00:05:12.460
if we switch it to pretty, you can

105
00:05:12.460 --> 00:05:15.160
more easily see what's going on, and then

106
00:05:15.160 --> 00:05:18.520
we get a HTTP 200 okay back, so

107
00:05:18.520 --> 00:05:22.620
id3, cheesecake, minus 500, and the seat.

108
00:05:22.820 --> 00:05:25.300
So, let's refresh this and see whether this

109
00:05:25.300 --> 00:05:26.540
has actually worked.

110
00:05:29.460 --> 00:05:30.940
Maybe we broke the application.

111
00:05:33.850 --> 00:05:34.250
All right.

112
00:05:34.410 --> 00:05:35.970
I'm not sure what happened there, but I

113
00:05:35.970 --> 00:05:39.290
switched off my proxy, and then refreshed, and

114
00:05:39.290 --> 00:05:40.070
it seems to be okay.

115
00:05:40.190 --> 00:05:42.910
So, maybe it's a problem with how Bubsuite

116
00:05:42.910 --> 00:05:46.790
is connecting to the application, but anyway, we

117
00:05:46.790 --> 00:05:49.990
can see that our new product was created,

118
00:05:50.330 --> 00:05:53.250
and it's minus $500, and then when we

119
00:05:53.250 --> 00:05:56.730
click buy, we get success, order sent successfully,

120
00:05:57.190 --> 00:05:59.910
and then we come back to the shop,

121
00:06:00.130 --> 00:06:02.670
and we can see that our available balance

122
00:06:02.670 --> 00:06:05.130
is higher, and every time we click it,

123
00:06:05.710 --> 00:06:08.030
we get more and more available balance.

124
00:06:08.470 --> 00:06:10.070
So, that's it for this section.

125
00:06:10.290 --> 00:06:12.370
There are a couple more mass assignment vulnerabilities

126
00:06:12.370 --> 00:06:15.750
inside of the crappy application, so if you

127
00:06:15.750 --> 00:06:18.930
have time, definitely challenge yourself and try to

128
00:06:18.930 --> 00:06:20.150
find and exploit them.

129
00:06:20.410 --> 00:06:21.550
I'll see you in the next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: Excessive Data Exposure

WEBVTT

1
00:00:00.340 --> 00:00:03.100
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So let's talk about excessive data exposure, a

2
00:00:03.100 --> 00:00:05.180
pretty simple issue that can come up for

3
00:00:05.180 --> 00:00:07.500
a number of reasons such as poor design

4
00:00:07.500 --> 00:00:10.280
or lack of security training for engineers.

5
00:00:10.920 --> 00:00:13.420
We've actually seen this already in a previous

6
00:00:13.420 --> 00:00:15.740
module where we needed to find a vehicle

7
00:00:15.740 --> 00:00:17.940
ID to exploit Ebola vulnerability.

8
00:00:18.800 --> 00:00:21.100
This was a great example because in well

9
00:00:21.100 --> 00:00:24.040
-defended applications we usually have to chain issues

10
00:00:24.040 --> 00:00:25.780
together to achieve exploitation.

11
00:00:26.420 --> 00:00:28.520
This is also something that a scanner can't

12
00:00:28.520 --> 00:00:30.600
do and as much as salespeople will tell

13
00:00:30.600 --> 00:00:32.220
you that their tool is amazing and powered

14
00:00:32.220 --> 00:00:34.520
by AI, I'm yet to see them successfully

15
00:00:34.520 --> 00:00:37.760
find complex issues such as second order or

16
00:00:37.760 --> 00:00:40.440
chain vulnerabilities within web applications.

17
00:00:41.000 --> 00:00:42.880
So again, I just want to stress that

18
00:00:42.880 --> 00:00:46.260
understanding the target application, what it's supposed to

19
00:00:46.260 --> 00:00:49.500
do and evaluating APIs in context is vital

20
00:00:49.500 --> 00:00:51.200
if you want to be successful.

21
00:00:51.660 --> 00:00:53.420
Let's take a look at some common examples

22
00:00:53.420 --> 00:00:56.640
of excessive data exposure and keep in mind

23
00:00:56.640 --> 00:00:58.880
that when you find it, always think okay,

24
00:00:59.680 --> 00:01:00.360
what's next?

25
00:01:00.640 --> 00:01:01.680
How can I use this?

26
00:01:02.060 --> 00:01:04.300
So there are a few techniques to thoroughly

27
00:01:04.300 --> 00:01:06.800
test for excessive data exposure.

28
00:01:07.300 --> 00:01:08.840
We want to be on the lookout for

29
00:01:08.840 --> 00:01:12.580
APIs returning full data objects and client-side

30
00:01:12.580 --> 00:01:15.100
filtering so we can easily verify this by

31
00:01:15.100 --> 00:01:17.360
looking at what we see in a response

32
00:01:17.360 --> 00:01:19.900
versus what we see on the page or

33
00:01:19.900 --> 00:01:21.120
within the web application.

34
00:01:21.720 --> 00:01:24.340
Now we've covered a lot of individual vulnerabilities

35
00:01:24.340 --> 00:01:27.020
during the course and using single endpoints as

36
00:01:27.020 --> 00:01:27.540
targets.

37
00:01:27.880 --> 00:01:29.860
Since we have the full set of endpoints

38
00:01:29.860 --> 00:01:32.960
for crappy available in Postman, what we're going

39
00:01:32.960 --> 00:01:35.060
to do next is run through them and

40
00:01:35.060 --> 00:01:37.180
see what we can find when we're evaluating

41
00:01:37.180 --> 00:01:39.520
one after the other after the other.

42
00:01:39.920 --> 00:01:40.920
I'll see you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.280 --> 00:00:03.460
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, so we have our crappy application

2
00:00:03.460 --> 00:00:07.480
running and we come into collections and our

3
00:00:07.480 --> 00:00:09.220
crappy postman collection.

4
00:00:10.320 --> 00:00:11.820
And all we're really going to do is

5
00:00:11.820 --> 00:00:13.140
we're going to start at the top and

6
00:00:13.140 --> 00:00:14.660
we're going to run down through some of

7
00:00:14.660 --> 00:00:17.400
the key endpoints and see what data comes

8
00:00:17.400 --> 00:00:17.820
back.

9
00:00:18.440 --> 00:00:20.640
Now of course the best thing to do

10
00:00:20.640 --> 00:00:23.000
is run through all of the endpoints, get

11
00:00:23.000 --> 00:00:24.960
an idea of how they work, what they're

12
00:00:24.960 --> 00:00:26.980
supposed to do, and then the ones that

13
00:00:26.980 --> 00:00:29.640
take parameters or the ones that we discover

14
00:00:29.640 --> 00:00:31.700
that we can post to or put to

15
00:00:31.700 --> 00:00:33.300
instead of just get, for example.

16
00:00:33.580 --> 00:00:35.860
We test in more depth to see whether

17
00:00:35.860 --> 00:00:37.900
they can leak further information.

18
00:00:38.400 --> 00:00:39.560
But to begin with, all we're going to

19
00:00:39.560 --> 00:00:41.340
do is go down the list and see

20
00:00:41.340 --> 00:00:43.820
whether we can find anything that looks out

21
00:00:43.820 --> 00:00:44.400
of the ordinary.

22
00:00:44.940 --> 00:00:46.020
So I'm just going to sign up a

23
00:00:46.020 --> 00:00:46.440
new account.

24
00:00:47.460 --> 00:00:50.840
We get user registered successfully and I'm just

25
00:00:50.840 --> 00:00:52.220
going to move myself out of the way

26
00:00:52.220 --> 00:00:54.620
so you can see all of the responses

27
00:00:54.620 --> 00:00:55.100
clearly.

28
00:00:56.540 --> 00:00:58.100
And then what we'll do is we'll come

29
00:00:58.100 --> 00:00:58.540
to login.

30
00:00:59.340 --> 00:01:00.420
We log ourselves in.

31
00:01:00.840 --> 00:01:02.700
We don't necessarily need to, but we can

32
00:01:02.700 --> 00:01:04.160
just verify our JWT.

33
00:01:05.040 --> 00:01:08.700
And then forgot password and the OTP one

34
00:01:08.700 --> 00:01:09.380
-time password.

35
00:01:09.680 --> 00:01:12.100
I think for now we'll skip over these.

36
00:01:13.480 --> 00:01:18.280
We can see things like recent vehicle, so

37
00:01:18.280 --> 00:01:20.480
we can have a look at get vehicles.

38
00:01:20.920 --> 00:01:21.780
Nothing's returned.

39
00:01:22.660 --> 00:01:24.020
Get recent posts.

40
00:01:25.060 --> 00:01:27.400
And here is the one that we found

41
00:01:27.400 --> 00:01:30.440
earlier, so we can see these email addresses

42
00:01:30.440 --> 00:01:34.680
listed and we can see the vehicle information,

43
00:01:34.880 --> 00:01:36.980
although this user doesn't have any vehicle yet.

44
00:01:37.880 --> 00:01:39.880
And then of course if we scroll down,

45
00:01:40.200 --> 00:01:43.680
we can see other users and other sensitive

46
00:01:43.680 --> 00:01:46.300
information that shouldn't be returned.

47
00:01:47.040 --> 00:01:50.000
So finding excessive data can be as simple

48
00:01:50.000 --> 00:01:51.640
as that, but it can also be quite

49
00:01:51.640 --> 00:01:52.900
complicated as well.

50
00:01:53.140 --> 00:01:54.720
So for example, if we have an endpoint

51
00:01:54.720 --> 00:01:57.620
that takes some data, for example the get

52
00:01:57.620 --> 00:01:59.980
reports, we may have to go in, create

53
00:01:59.980 --> 00:02:03.380
a report, send the report's id, and then

54
00:02:03.380 --> 00:02:04.700
review what comes back.

55
00:02:05.280 --> 00:02:08.220
And even if this isn't vulnerable to other

56
00:02:08.220 --> 00:02:12.760
things such as broken object level authorization, broken

57
00:02:12.760 --> 00:02:16.700
function level authorization, the endpoint might return sensitive

58
00:02:16.700 --> 00:02:18.780
data that it shouldn't return.

59
00:02:19.080 --> 00:02:21.960
And really there's no shortcut for understanding the

60
00:02:21.960 --> 00:02:25.640
application and going through methodically and thoroughly testing

61
00:02:25.640 --> 00:02:26.560
each endpoint.

62
00:02:27.360 --> 00:02:29.040
So now it's challenge time.

63
00:02:29.240 --> 00:02:31.440
There is at least one other endpoint that

64
00:02:31.440 --> 00:02:34.680
leaks some sensitive data, so your challenge is

65
00:02:34.680 --> 00:02:35.960
of course to find it.

66
00:02:36.100 --> 00:02:38.160
Make sure that you have sufficient data in

67
00:02:38.160 --> 00:02:39.980
the application to test, so at least a

68
00:02:39.980 --> 00:02:42.220
couple of users that are registered, add their

69
00:02:42.220 --> 00:02:44.400
vehicles, add a video, and so on.

70
00:02:44.760 --> 00:02:46.280
I'm not sure if I mentioned this already

71
00:02:46.280 --> 00:02:48.320
in a previous video, but setting up our

72
00:02:48.320 --> 00:02:50.920
target environment for testing is a crucial step

73
00:02:50.920 --> 00:02:52.540
to make sure that we don't miss out

74
00:02:52.540 --> 00:02:56.300
on some behavioral functionality within the application, regardless

75
00:02:56.300 --> 00:02:58.460
of it being intended or not.

76
00:02:58.600 --> 00:03:00.220
What I like to do is set up

77
00:03:00.220 --> 00:03:01.940
a few users and just add all of

78
00:03:01.940 --> 00:03:04.520
their details into my notes, such as their

79
00:03:04.520 --> 00:03:08.060
email address, password, id, phone number, video name,

80
00:03:08.460 --> 00:03:11.020
anything really that belongs to that user, so

81
00:03:11.020 --> 00:03:13.360
that you can quickly identify if you're a

82
00:03:13.360 --> 00:03:16.160
BOLA vulnerability or if you find a leaky

83
00:03:16.160 --> 00:03:18.560
endpoint that reveals excessive information.

84
00:03:18.920 --> 00:03:20.960
Good luck with the challenge and I'll see

85
00:03:20.960 --> 00:03:21.640
you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:01.850
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome back.

2
00:00:02.050 --> 00:00:03.690
I hope you had a good stab at

3
00:00:03.690 --> 00:00:06.130
the challenge and really got to know the

4
00:00:06.130 --> 00:00:09.290
crappy application and all of the endpoints, because

5
00:00:09.290 --> 00:00:11.570
in a chapter later on where we look

6
00:00:11.570 --> 00:00:13.790
at chaining vulnerabilities together, you're going to have

7
00:00:13.790 --> 00:00:16.450
to understand how the endpoints work, what they

8
00:00:16.450 --> 00:00:19.170
can give you, maybe more importantly, what they

9
00:00:19.170 --> 00:00:20.030
can't give you.

10
00:00:20.310 --> 00:00:22.910
So let's go down the list, and we

11
00:00:22.910 --> 00:00:25.270
checked a bunch of these already, and we

12
00:00:25.270 --> 00:00:29.610
found that originally, which one was it?

13
00:00:29.610 --> 00:00:33.390
The getRecentPosts endpoint returns quite a lot of

14
00:00:33.390 --> 00:00:36.250
data, and obviously was quite sensitive.

15
00:00:37.210 --> 00:00:39.890
And interestingly enough, it also returns the user

16
00:00:39.890 --> 00:00:40.750
ID as well.

17
00:00:40.870 --> 00:00:45.630
So for example, Adam007, his user ID is

18
00:00:45.630 --> 00:00:45.950
this.

19
00:00:46.070 --> 00:00:47.030
So what I'm going to do is I'm

20
00:00:47.030 --> 00:00:49.310
going to copy this, and then we're going

21
00:00:49.310 --> 00:00:51.310
to come down to the getPost.

22
00:00:52.210 --> 00:00:55.410
And when I send this, it obviously sends

23
00:00:55.410 --> 00:00:58.130
the ID, and what I'm going to do

24
00:00:58.130 --> 00:01:00.090
is I'm going to go jump into burp

25
00:01:00.090 --> 00:01:02.450
suites and further test this.

26
00:01:02.930 --> 00:01:05.770
Send to repeater, and send this.

27
00:01:06.310 --> 00:01:08.330
And as we can see, it actually, again,

28
00:01:08.450 --> 00:01:11.230
it leaks the email address and the vehicle

29
00:01:11.230 --> 00:01:13.670
ID if there is one, and basically leaks

30
00:01:13.670 --> 00:01:15.010
sensitive information.

31
00:01:15.850 --> 00:01:18.290
And if I put in another ID, for

32
00:01:18.290 --> 00:01:22.310
example, we get Adam007, so we can get

33
00:01:22.310 --> 00:01:25.290
the information of other users based on their

34
00:01:25.290 --> 00:01:26.390
ID as well.

35
00:01:26.570 --> 00:01:29.630
So if you found this endpoint, congratulations, good

36
00:01:29.630 --> 00:01:30.750
job on the challenge.

37
00:01:31.070 --> 00:01:33.110
And if you didn't, don't worry, make sure

38
00:01:33.110 --> 00:01:35.170
to update your notes, and I hope this

39
00:01:35.170 --> 00:01:37.970
improved your methodology and thinking a little bit.

40
00:01:38.390 --> 00:01:40.270
This was quite a short section, but of

41
00:01:40.270 --> 00:01:42.470
course, really, really important to always be on

42
00:01:42.470 --> 00:01:46.270
the lookout for extra information or parameters that

43
00:01:46.270 --> 00:01:47.830
endpoints shouldn't return.

44
00:01:48.130 --> 00:01:49.190
I'll see you in the next section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: SSRF - Server-side Request Forgery

WEBVTT

1
00:00:00.970 --> 00:00:03.450
(Transcribed by TurboScribe. Go Unlimited to remove this message.) SSRF, which stands for server-side request forgery,

2
00:00:03.710 --> 00:00:07.830
is a vulnerability that allows an attacker to

3
00:00:07.830 --> 00:00:11.430
have a server-side application send requests on

4
00:00:11.430 --> 00:00:14.970
their behalf, usually to an internal resource that

5
00:00:14.970 --> 00:00:16.850
is not externally available to them.

6
00:00:17.270 --> 00:00:19.410
So let's take a quick look at an

7
00:00:19.410 --> 00:00:19.850
example.

8
00:00:20.590 --> 00:00:23.850
Here we have an appointment booking application, and

9
00:00:23.850 --> 00:00:25.990
in this example we're going to make the

10
00:00:25.990 --> 00:00:29.290
server make requests to itself via the loopback

11
00:00:29.290 --> 00:00:34.130
address 127.0.0.1. The attacker, whilst

12
00:00:34.130 --> 00:00:36.670
in the user context, can invoke this request

13
00:00:36.670 --> 00:00:38.870
that gets the up-to-date list of

14
00:00:38.870 --> 00:00:40.150
available booking slots.

15
00:00:40.650 --> 00:00:42.770
The request contains the payload with the booking

16
00:00:42.770 --> 00:00:45.590
information request filters, such as the date range,

17
00:00:45.810 --> 00:00:48.550
and a legitimate request looks something like this.

18
00:00:48.750 --> 00:00:51.310
So to exploit this vulnerability, we simply need

19
00:00:51.310 --> 00:00:53.890
to intercept the request, drop in our own

20
00:00:53.890 --> 00:00:56.170
payload, and forward the request on.

21
00:00:56.450 --> 00:00:58.530
The request, instead of making a call to

22
00:00:58.530 --> 00:01:03.269
HTTP API booking example.com, calls the admin

23
00:01:03.269 --> 00:01:06.050
page on the loopback address, and because the

24
00:01:06.050 --> 00:01:08.870
server trusts itself, it serves up the page

25
00:01:08.870 --> 00:01:10.030
without complaints.

26
00:01:10.510 --> 00:01:13.110
So going back to our definition, the application

27
00:01:13.110 --> 00:01:16.510
we are exploiting is making requests, in this

28
00:01:16.510 --> 00:01:18.670
case to itself, on our behalf.

29
00:01:19.070 --> 00:01:21.290
Of course, we could also try and access

30
00:01:21.290 --> 00:01:24.470
other internal resources that the server has access

31
00:01:24.470 --> 00:01:27.230
to, but we don't have direct access to.

32
00:01:27.490 --> 00:01:29.390
In the next video, we'll walk through a

33
00:01:29.390 --> 00:01:31.810
practical example, and then we'll give you a

34
00:01:31.810 --> 00:01:32.770
challenge, as always.

35
00:01:33.090 --> 00:01:33.630
I'll see you then.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.480 --> 00:00:02.420
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Now for our demo this time around, we're

2
00:00:02.420 --> 00:00:04.220
actually going to be utilizing one of my

3
00:00:04.220 --> 00:00:07.700
favorite free resources, the Portswigger Academy.

4
00:00:08.100 --> 00:00:11.060
This is because the SSRF labs in the

5
00:00:11.060 --> 00:00:14.220
academy are API-driven and freely available.

6
00:00:14.620 --> 00:00:16.620
It's actually a great resource to further practice

7
00:00:16.620 --> 00:00:18.760
the tools and techniques that we've learned on

8
00:00:18.760 --> 00:00:20.840
the course, so I highly recommend you check

9
00:00:20.840 --> 00:00:21.160
it out.

10
00:00:21.640 --> 00:00:25.160
For now, let's dive into a SSRF lab.

11
00:00:25.540 --> 00:00:28.340
All right, so here I am at Portswigger's

12
00:00:28.340 --> 00:00:29.460
web security academy.

13
00:00:29.760 --> 00:00:31.980
If you want to sign up an account,

14
00:00:32.120 --> 00:00:34.040
or if you haven't used this before, simply

15
00:00:34.040 --> 00:00:37.480
go to portswigger.net, sign up a free

16
00:00:37.480 --> 00:00:40.220
account, and then come to the academy at

17
00:00:40.220 --> 00:00:42.320
the top, and you'll find all of their

18
00:00:42.320 --> 00:00:45.060
labs and tutorials on here.

19
00:00:45.320 --> 00:00:47.120
I've already clicked access the lab, so we'll

20
00:00:47.120 --> 00:00:50.420
just jump straight in, and here we have

21
00:00:50.420 --> 00:00:51.700
an application.

22
00:00:52.340 --> 00:00:54.620
We like to shop, and it just looks

23
00:00:54.620 --> 00:00:58.360
like a standard shopping application, and it looks

24
00:00:58.360 --> 00:01:01.100
like there's a my account, so username and

25
00:01:01.100 --> 00:01:01.560
password.

26
00:01:01.960 --> 00:01:04.700
It doesn't look like there's any registration functionality,

27
00:01:05.060 --> 00:01:08.660
so we don't get to register unfortunately, but

28
00:01:08.660 --> 00:01:13.320
let me come into the conversation controlling lemon.

29
00:01:13.800 --> 00:01:15.520
It looks like he's having a rough time

30
00:01:15.520 --> 00:01:15.920
with that.

31
00:01:17.440 --> 00:01:20.400
So here we have some functionality called check

32
00:01:20.400 --> 00:01:22.680
stock, and we're going to check the stock

33
00:01:22.680 --> 00:01:26.420
in London, and it comes back with 911

34
00:01:26.420 --> 00:01:27.020
units.

35
00:01:27.500 --> 00:01:30.120
This looks like an API request, because the

36
00:01:30.120 --> 00:01:32.500
page stayed the same, it didn't refresh, it

37
00:01:32.500 --> 00:01:34.020
just popped up with a little bit of

38
00:01:34.020 --> 00:01:34.860
extra data.

39
00:01:35.360 --> 00:01:37.100
So this is what we're going to check

40
00:01:37.100 --> 00:01:37.380
out.

41
00:01:37.940 --> 00:01:39.920
Now if I come over to web suite,

42
00:01:40.700 --> 00:01:43.300
and I come down to the bottom, so

43
00:01:43.300 --> 00:01:46.940
we see slash product slash stock, and we

44
00:01:46.940 --> 00:01:49.520
can see our original request and the response

45
00:01:49.520 --> 00:01:50.480
911.

46
00:01:51.840 --> 00:01:55.160
If I send this to repeater, click over,

47
00:01:55.560 --> 00:01:57.880
send it again, we actually get a slightly

48
00:01:57.880 --> 00:02:00.160
different response, which is slightly odd, but that's

49
00:02:00.160 --> 00:02:00.400
okay.

50
00:02:02.020 --> 00:02:04.560
And we can see in the request that

51
00:02:04.560 --> 00:02:09.060
we have this stock API equals HTTP, and

52
00:02:09.060 --> 00:02:11.500
it looks like a lot of encoded characters.

53
00:02:11.780 --> 00:02:14.920
So we can just control shift u to

54
00:02:14.920 --> 00:02:18.040
decode this, and I'm just going to get

55
00:02:18.040 --> 00:02:19.720
rid of that, so that we can see

56
00:02:19.720 --> 00:02:20.900
things a little bit better.

57
00:02:21.900 --> 00:02:25.660
And we have the HTTP stock dot we

58
00:02:25.660 --> 00:02:28.560
like to shop dot net 8080 product stock

59
00:02:28.560 --> 00:02:32.020
check, and the product ID is one, and

60
00:02:32.020 --> 00:02:34.280
the store ID is one.

61
00:02:34.780 --> 00:02:36.780
So if we go back to our lab,

62
00:02:36.920 --> 00:02:39.120
we know that the objective of the lab

63
00:02:39.120 --> 00:02:45.300
is to reach HTTP localhost slash admin, and

64
00:02:45.300 --> 00:02:46.920
to delete the user Carlos.

65
00:02:47.620 --> 00:02:49.740
So first of all, what we're going to

66
00:02:49.740 --> 00:02:56.820
do is let's change this to localhost slash

67
00:02:56.820 --> 00:03:00.900
admin, and notice that I'm going to leave

68
00:03:00.900 --> 00:03:03.320
the product ID and the store ID in,

69
00:03:03.400 --> 00:03:05.000
because there might be some kind of processing.

70
00:03:05.340 --> 00:03:06.960
Of course, we have time to test.

71
00:03:07.040 --> 00:03:08.960
We can take these out and test fully,

72
00:03:09.040 --> 00:03:10.720
but there's no harm in leaving them in

73
00:03:10.720 --> 00:03:11.320
for now.

74
00:03:12.280 --> 00:03:15.360
And we get a 200 okay, and if

75
00:03:15.360 --> 00:03:21.160
I scroll down, it looks like we have

76
00:03:21.160 --> 00:03:23.280
some kind of admin panel, as we can

77
00:03:23.280 --> 00:03:23.980
see here.

78
00:03:24.240 --> 00:03:26.200
So if I just render this page quickly,

79
00:03:26.920 --> 00:03:28.500
let me move myself out of the way,

80
00:03:29.160 --> 00:03:31.580
we can see that we are indeed on

81
00:03:31.580 --> 00:03:32.660
the admin panel.

82
00:03:32.900 --> 00:03:35.500
So we know our objective is to delete

83
00:03:35.500 --> 00:03:37.920
the user Carlos, and if we come down,

84
00:03:38.920 --> 00:03:42.000
we can see this endpoint, so slash admin

85
00:03:42.000 --> 00:03:44.960
slash delete username equals Carlos.

86
00:03:45.360 --> 00:03:51.050
So let's just copy this, replace this here,

87
00:03:52.710 --> 00:03:56.850
hit send, we get a 302 found, so

88
00:03:56.850 --> 00:03:59.350
we'll just follow the redirection, and we get

89
00:03:59.350 --> 00:04:02.690
a 401 unauthorized, but actually we still did

90
00:04:02.690 --> 00:04:04.310
manage to complete the lab.

91
00:04:04.530 --> 00:04:06.810
As you can see, we get congratulations, you

92
00:04:06.810 --> 00:04:08.990
solved the lab, and if we hit render,

93
00:04:09.670 --> 00:04:12.430
we get this congratulations message, and we get

94
00:04:12.430 --> 00:04:15.110
the admin interface is only available if logged

95
00:04:15.110 --> 00:04:18.029
in as an administrator, or if requested from

96
00:04:18.029 --> 00:04:18.670
the loopback.

97
00:04:18.670 --> 00:04:22.070
So what happened here was the server made

98
00:04:22.070 --> 00:04:24.710
the request on our behalf, so it went

99
00:04:24.710 --> 00:04:29.350
to localhost slash admin, delete, and deleted Carlos,

100
00:04:29.530 --> 00:04:31.910
but then we got a 302 back, and

101
00:04:31.910 --> 00:04:33.790
we got forwarded to slash admin.

102
00:04:34.290 --> 00:04:37.430
And unfortunately, because this request to slash admin

103
00:04:37.430 --> 00:04:39.610
came from us, we don't get access to

104
00:04:39.610 --> 00:04:40.470
the admin panel.

105
00:04:40.710 --> 00:04:42.810
But the action was still carried out behind

106
00:04:42.810 --> 00:04:44.670
the scenes, if that makes sense.

107
00:04:44.670 --> 00:04:47.150
This is a really, really powerful attack, and

108
00:04:47.150 --> 00:04:50.530
as we've seen with the increase of APIs

109
00:04:50.530 --> 00:04:54.470
and the increase of things like microservices, server

110
00:04:54.470 --> 00:04:57.410
-side request forgery is becoming more and more

111
00:04:57.410 --> 00:04:59.810
common, so definitely something to look out for.

112
00:05:00.650 --> 00:05:02.570
And of course, now you know one of

113
00:05:02.570 --> 00:05:05.230
the main things to look for is URLs

114
00:05:05.230 --> 00:05:08.450
or partial URLs that are passed in either

115
00:05:08.450 --> 00:05:11.430
the URI or the body of requests, or

116
00:05:11.430 --> 00:05:13.630
sometimes even the headers as well.

117
00:05:14.230 --> 00:05:15.990
So for our challenge, I'd like you to

118
00:05:15.990 --> 00:05:19.390
spin up the crappy application and identify a

119
00:05:19.390 --> 00:05:21.570
server-side request forgery vulnerability.

120
00:05:22.650 --> 00:05:24.730
Now I'm purposefully not giving you an endpoint

121
00:05:24.730 --> 00:05:27.070
to look at this time, because we want

122
00:05:27.070 --> 00:05:29.330
to start getting into the process of stepping

123
00:05:29.330 --> 00:05:33.010
through an application methodically, identifying things that are

124
00:05:33.010 --> 00:05:36.890
suspicious, or finding potential indicators of a vulnerability.

125
00:05:37.650 --> 00:05:39.450
And since we already know the vulnerability that

126
00:05:39.450 --> 00:05:41.470
we're looking for, I have confidence that you

127
00:05:41.470 --> 00:05:42.090
can find it.

128
00:05:42.910 --> 00:05:45.750
This is also an opportunity to decide what

129
00:05:45.750 --> 00:05:47.690
tool you think is most suitable for the

130
00:05:47.690 --> 00:05:50.810
task at hand, and start solidifying your workflow.

131
00:05:51.210 --> 00:05:53.310
As always, we'll walk through the challenge together

132
00:05:53.310 --> 00:05:54.250
in the next video.

133
00:05:54.470 --> 00:05:55.050
I'll see you there.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:01.040 --> 00:00:03.340
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, let's take a look at the challenge

2
00:00:03.340 --> 00:00:04.040
walkthrough.

3
00:00:04.500 --> 00:00:06.240
I hope you all got on well and

4
00:00:06.240 --> 00:00:10.100
found the server-side request forgery SSRF vulnerability,

5
00:00:10.500 --> 00:00:12.740
but if not, let's take a look and

6
00:00:12.740 --> 00:00:13.660
we'll walk through it together.

7
00:00:14.760 --> 00:00:17.100
So I'm just going to come to the

8
00:00:17.100 --> 00:00:23.960
crappy application and sign myself in, like this,

9
00:00:24.180 --> 00:00:26.460
and you can see that we have the

10
00:00:26.460 --> 00:00:30.340
dashboard page, and this vulnerability is actually in

11
00:00:30.340 --> 00:00:33.220
an endpoint that we looked at previously, so

12
00:00:33.220 --> 00:00:36.240
it's in the contact mechanic endpoint here.

13
00:00:36.380 --> 00:00:39.680
So if we just click on this, we

14
00:00:39.680 --> 00:00:41.460
get this form, so we just need to

15
00:00:41.460 --> 00:00:44.460
choose a mechanic and we need to put

16
00:00:44.460 --> 00:00:45.180
in a problem.

17
00:00:45.720 --> 00:00:50.120
So we'll file off and then we can

18
00:00:50.120 --> 00:00:52.980
send the service request, and we get a

19
00:00:52.980 --> 00:00:56.400
success message saying the service request sent to

20
00:00:56.400 --> 00:00:58.380
the mechanic, and we can just click okay.

21
00:00:59.220 --> 00:01:02.060
Now if we come to Bep Suites and

22
00:01:02.060 --> 00:01:04.140
we find the post request that was made,

23
00:01:04.920 --> 00:01:08.080
we can close the inspector, make this a

24
00:01:08.080 --> 00:01:09.700
little bit bigger, and I'm just going to

25
00:01:09.700 --> 00:01:11.060
move myself out of the way.

26
00:01:12.160 --> 00:01:12.980
There we go.

27
00:01:13.980 --> 00:01:16.600
You can see in the request we actually

28
00:01:16.600 --> 00:01:19.840
have a mechanic API field and a URL

29
00:01:19.840 --> 00:01:20.900
in that field.

30
00:01:21.280 --> 00:01:23.040
So let's test this out.

31
00:01:23.120 --> 00:01:25.400
Let's take this to repeater with ctrl-r,

32
00:01:26.120 --> 00:01:29.120
come over to repeater, and what I'm going

33
00:01:29.120 --> 00:01:31.080
to do is I'm going to test this

34
00:01:31.080 --> 00:01:34.080
against a website that I know will probably

35
00:01:34.080 --> 00:01:34.640
respond.

36
00:01:35.340 --> 00:01:40.880
So https://www.google.com.

37
00:01:41.280 --> 00:01:43.000
Now I should say that if you're working

38
00:01:43.000 --> 00:01:44.920
in a production environment or you're working on

39
00:01:44.920 --> 00:01:47.160
bug bounty, when you're testing for things like

40
00:01:47.160 --> 00:01:49.960
service add request forgery, probably it's not wise

41
00:01:49.960 --> 00:01:52.340
to use things like request bin or Google

42
00:01:52.340 --> 00:01:55.380
and other services, because you might potentially leak

43
00:01:55.380 --> 00:01:56.560
sensitive information.

44
00:01:57.160 --> 00:01:58.800
But in this case, because it's just a

45
00:01:58.800 --> 00:01:59.540
lab, it's okay.

46
00:01:59.860 --> 00:02:01.720
An alternative to this is to spin up

47
00:02:01.720 --> 00:02:03.900
something locally and connect to that.

48
00:02:05.540 --> 00:02:08.380
So I'm just going to click send, and

49
00:02:08.380 --> 00:02:09.220
here we are.

50
00:02:09.340 --> 00:02:12.060
We get a response from mechanic API, and

51
00:02:12.060 --> 00:02:15.100
this does indeed look like a response from

52
00:02:15.100 --> 00:02:15.580
Google.

53
00:02:15.780 --> 00:02:17.560
So if I just type in the keyword,

54
00:02:17.820 --> 00:02:19.980
you can see that we get the Google

55
00:02:19.980 --> 00:02:22.100
homepage back, and you can see this in

56
00:02:22.100 --> 00:02:22.980
the title here.

57
00:02:23.060 --> 00:02:25.640
So from this, and as in our demo,

58
00:02:25.760 --> 00:02:27.600
what we'd want to start thinking about is

59
00:02:27.600 --> 00:02:31.160
what functionality can we connect to locally or

60
00:02:31.160 --> 00:02:33.780
within the target environment, and how can we

61
00:02:33.780 --> 00:02:36.180
use service side request forgery to get to

62
00:02:36.180 --> 00:02:37.940
things that we shouldn't be able to get

63
00:02:37.940 --> 00:02:38.180
to.

64
00:02:38.600 --> 00:02:40.440
And we'll talk a little bit more about

65
00:02:40.440 --> 00:02:43.180
that in the final section, chaining vulnerabilities.

66
00:02:43.820 --> 00:02:45.140
So that's it for this section.

67
00:02:45.140 --> 00:02:47.620
Once again, congratulations if you solved the challenge,

68
00:02:47.840 --> 00:02:49.980
and if not, don't forget to update your

69
00:02:49.980 --> 00:02:52.060
notes, and I'll see you in the next

70
00:02:52.060 --> 00:02:52.340
section.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: Chaining Vulnerabilities

WEBVTT

1
00:00:00.410 --> 00:00:03.090
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome to the penultimate section of the course.

2
00:00:03.310 --> 00:00:05.530
We've covered a lot of materials so far

3
00:00:05.530 --> 00:00:07.730
and I really hope that we can start

4
00:00:07.730 --> 00:00:10.170
to bring this all together and explore some

5
00:00:10.170 --> 00:00:11.410
more complex scenarios.

6
00:00:11.910 --> 00:00:13.710
I'm going to keep this section quite short

7
00:00:13.710 --> 00:00:15.830
as it's really just a demo of stringing

8
00:00:15.830 --> 00:00:18.150
together things that we found along the way,

9
00:00:18.530 --> 00:00:20.250
but I wanted to include it as it

10
00:00:20.250 --> 00:00:21.810
actually took me quite a long time to

11
00:00:21.810 --> 00:00:24.350
find and exploit this vulnerability when I was

12
00:00:24.350 --> 00:00:26.930
actively working on the crappy application.

13
00:00:26.930 --> 00:00:29.310
However, before we dive in, I want to

14
00:00:29.310 --> 00:00:30.830
talk to you about command injection.

15
00:00:31.229 --> 00:00:33.930
Now, we didn't specifically cover this in the

16
00:00:33.930 --> 00:00:36.370
course and it's not really any different than

17
00:00:36.370 --> 00:00:39.610
other injection vulnerabilities such as SQL injection that

18
00:00:39.610 --> 00:00:40.310
we did cover.

19
00:00:40.750 --> 00:00:42.850
To achieve command injection, we need to find

20
00:00:42.850 --> 00:00:45.090
a place where our input is executed.

21
00:00:45.610 --> 00:00:47.810
Now, before we continue, I just want to

22
00:00:47.810 --> 00:00:50.810
mention that command injection can be really, really

23
00:00:50.810 --> 00:00:51.330
destructive.

24
00:00:51.830 --> 00:00:54.250
You might interfere with or crash your target

25
00:00:54.250 --> 00:00:54.850
application.

26
00:00:55.450 --> 00:00:57.590
So it's really important to consider the payloads

27
00:00:57.590 --> 00:01:00.390
you're sending, especially if you're working on a

28
00:01:00.390 --> 00:01:01.510
production system.

29
00:01:02.050 --> 00:01:04.790
A really common example of command injection that

30
00:01:04.790 --> 00:01:07.010
you'll see a lot in CTFs is when

31
00:01:07.010 --> 00:01:09.130
we have an endpoint that takes an IP

32
00:01:09.130 --> 00:01:12.470
address and we'll ping that IP address and

33
00:01:12.470 --> 00:01:13.550
return the results.

34
00:01:14.090 --> 00:01:16.370
In this case, the IP we provide is

35
00:01:16.370 --> 00:01:19.050
directly passed into a function that can execute

36
00:01:19.050 --> 00:01:20.010
it as code.

37
00:01:20.210 --> 00:01:23.350
If there is insufficient filtering or protection, we

38
00:01:23.350 --> 00:01:24.910
can simply append commands.

39
00:01:25.190 --> 00:01:26.870
So common ways to do this would be

40
00:01:26.870 --> 00:01:30.850
semicolon and then add your command or ampersand

41
00:01:30.850 --> 00:01:33.490
ampersand and add your command and so on.

42
00:01:33.890 --> 00:01:35.790
You can take a look at any command

43
00:01:35.790 --> 00:01:37.530
injection cheat sheet to get an idea.

44
00:01:38.090 --> 00:01:40.310
Of course, it's important to keep in mind

45
00:01:40.310 --> 00:01:44.050
that command injection will vary from application to

46
00:01:44.050 --> 00:01:46.350
application, but you get the idea.

47
00:01:47.210 --> 00:01:50.470
So why is chaining vulnerabilities really, really important?

48
00:01:50.830 --> 00:01:52.890
Well, a lot of vulnerabilities on their own

49
00:01:52.890 --> 00:01:56.230
have very little impact, but as penetration testers,

50
00:01:56.350 --> 00:01:58.870
we often have an objective that might be

51
00:01:58.870 --> 00:02:01.910
something like, can we steal customer data or

52
00:02:01.910 --> 00:02:04.510
can we take over the accounts of other

53
00:02:04.510 --> 00:02:05.030
users?

54
00:02:05.490 --> 00:02:08.050
Occasionally, you'll find a critical issue that lets

55
00:02:08.050 --> 00:02:10.990
us achieve this objective all at once, but

56
00:02:10.990 --> 00:02:13.590
more often than not, you'll only find things

57
00:02:13.590 --> 00:02:15.990
that are just a small piece of the

58
00:02:15.990 --> 00:02:16.350
puzzle.

59
00:02:17.430 --> 00:02:20.570
Within the crappy application, there is a chain

60
00:02:20.570 --> 00:02:23.210
of vulnerabilities that can lead us to remote

61
00:02:23.210 --> 00:02:24.110
code execution.

62
00:02:24.630 --> 00:02:27.530
Now, this is a completely optional challenge, so

63
00:02:27.530 --> 00:02:29.570
if you're feeling up to it, feel free

64
00:02:29.570 --> 00:02:31.450
to stop the video here or after I've

65
00:02:31.450 --> 00:02:33.870
given a few hints and have at it.

66
00:02:34.350 --> 00:02:36.030
Remember that you can always make a start

67
00:02:36.030 --> 00:02:38.530
and come back for hints later if you're

68
00:02:38.530 --> 00:02:38.870
stuck.

69
00:02:39.310 --> 00:02:41.770
You know yourselves, so I leave the decision

70
00:02:41.770 --> 00:02:42.550
up to you.

71
00:02:43.070 --> 00:02:44.530
If you're not feeling quite up to the

72
00:02:44.530 --> 00:02:45.890
challenge yet, don't worry.

73
00:02:46.170 --> 00:02:48.230
The capstone will help you hone your methodology

74
00:02:48.230 --> 00:02:50.090
and should increase your confidence.

75
00:02:50.770 --> 00:02:53.350
Maybe then go on and treat the crappy

76
00:02:53.350 --> 00:02:56.090
application as more of a research project or

77
00:02:56.090 --> 00:02:57.290
pushing your boundaries.

78
00:02:57.790 --> 00:02:59.270
All right, the first hint.

79
00:02:59.510 --> 00:03:01.430
So, pause now if you don't want to

80
00:03:01.430 --> 00:03:03.330
hear it, but if you do, then I

81
00:03:03.330 --> 00:03:05.650
suggest you check out the endpoints that deal

82
00:03:05.650 --> 00:03:07.310
with user videos.

83
00:03:07.910 --> 00:03:10.970
If you need a second hint, then let

84
00:03:10.970 --> 00:03:13.070
me give you the vulnerabilities in the chain.

85
00:03:13.210 --> 00:03:16.690
So, we're looking for mass assignments, server-side

86
00:03:16.690 --> 00:03:20.370
request forgery, and then, of course, command injection.

87
00:03:20.970 --> 00:03:22.710
Good luck with the challenge and I'll see

88
00:03:22.710 --> 00:03:24.310
you in the next video for the walkthrough.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:01.130 --> 00:00:04.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, let's do this challenge and I'm quite

2
00:00:04.130 --> 00:00:06.970
excited to walk through this because there's lots

3
00:00:06.970 --> 00:00:09.710
of different things that we've done which kind

4
00:00:09.710 --> 00:00:10.910
of come together nicely.

5
00:00:11.370 --> 00:00:14.810
So first, let's sign up a new account.

6
00:00:15.050 --> 00:00:17.270
So I'm just going to come in, call

7
00:00:17.270 --> 00:00:21.050
it Alex and let's just do j at

8
00:00:21.050 --> 00:00:24.350
j.com because I know I haven't used

9
00:00:24.350 --> 00:00:24.790
that yet.

10
00:00:25.470 --> 00:00:28.510
And we'll just give it a random phone

11
00:00:28.510 --> 00:00:31.920
number and a password.

12
00:00:37.740 --> 00:00:40.080
Alright, and then we can log in.

13
00:00:46.250 --> 00:00:47.910
So no vehicles found, so I'm just going

14
00:00:47.910 --> 00:00:49.770
to add the vehicle quickly.

15
00:00:49.990 --> 00:00:58.820
Whoops, grab the VIN and then grab the

16
00:00:58.820 --> 00:00:59.500
PIN code.

17
00:00:59.760 --> 00:01:01.360
I'm sure you've all done this many, many

18
00:01:01.360 --> 00:01:02.100
times now.

19
00:01:05.500 --> 00:01:06.100
And what do we get?

20
00:01:06.260 --> 00:01:06.800
Ah, BMW.

21
00:01:08.760 --> 00:01:09.320
Sigh.

22
00:01:09.940 --> 00:01:13.160
Alright, so what we want to do is

23
00:01:13.160 --> 00:01:19.790
come to our profile page.

24
00:01:21.490 --> 00:01:23.870
And then actually what we're going to do

25
00:01:23.870 --> 00:01:27.330
is let's come over to Postman first.

26
00:01:28.050 --> 00:01:31.150
And I'm just going to set up a

27
00:01:31.150 --> 00:01:40.120
quick account and then we can add a

28
00:01:40.120 --> 00:01:40.480
video.

29
00:01:43.880 --> 00:01:46.620
Let's re-add this video file.

30
00:01:48.480 --> 00:01:54.680
Car.mp4. And this is the request where

31
00:01:54.680 --> 00:01:58.420
I realized that code execution is likely possible,

32
00:01:58.900 --> 00:02:00.180
or we had a chance.

33
00:02:00.860 --> 00:02:02.820
And I don't know if you've spotted it,

34
00:02:02.920 --> 00:02:04.440
but take a look at these parameters.

35
00:02:04.980 --> 00:02:07.240
And one of these parameters, whoops, one of

36
00:02:07.240 --> 00:02:12.720
these parameters, one of these parameters actually has

37
00:02:12.720 --> 00:02:13.600
some code inside.

38
00:02:13.760 --> 00:02:15.560
So you can see here we have the

39
00:02:15.560 --> 00:02:18.980
conversion params and we have the dash v

40
00:02:18.980 --> 00:02:22.800
codec h264.

41
00:02:23.180 --> 00:02:26.500
So this is probably going to execute some

42
00:02:26.500 --> 00:02:28.560
code, some like conversion.

43
00:02:29.220 --> 00:02:30.160
Ah, I can't type in that bit.

44
00:02:31.060 --> 00:02:33.240
And it's going to pass these in.

45
00:02:33.660 --> 00:02:37.080
And we already know from previous modules that

46
00:02:37.080 --> 00:02:39.980
the application might be vulnerable to mass assignments.

47
00:02:40.340 --> 00:02:42.800
So we might be able to upload a

48
00:02:42.800 --> 00:02:45.820
video or edit a video and set this

49
00:02:45.820 --> 00:02:46.420
parameter.

50
00:02:46.840 --> 00:02:49.820
And that was the first clue that I

51
00:02:49.820 --> 00:02:52.800
spotted that led me to the remote code

52
00:02:52.800 --> 00:02:54.200
execution vulnerability.

53
00:02:54.780 --> 00:02:56.120
So let's do that.

54
00:02:56.200 --> 00:03:02.600
Let's upload a video and then upload this.

55
00:03:03.660 --> 00:03:04.640
Video uploaded.

56
00:03:05.910 --> 00:03:07.780
And then if we take a look in

57
00:03:07.780 --> 00:03:13.540
Bubsuite, this is our video upload.

58
00:03:16.200 --> 00:03:18.420
And you can see, if I just move

59
00:03:18.420 --> 00:03:21.500
myself out of the way, you can see,

60
00:03:21.700 --> 00:03:24.400
again, we get this conversion params.

61
00:03:25.340 --> 00:03:27.960
Now, instead of uploading a new video and

62
00:03:27.960 --> 00:03:30.940
defining this, what I found was, what we

63
00:03:30.940 --> 00:03:32.580
can do is we can actually come in

64
00:03:32.580 --> 00:03:34.980
and we can change the video name.

65
00:03:35.620 --> 00:03:36.980
And I want to change it to just

66
00:03:36.980 --> 00:03:40.820
test123 and press OK.

67
00:03:41.840 --> 00:03:44.540
And then we can see this put request

68
00:03:44.540 --> 00:03:44.960
here.

69
00:03:45.000 --> 00:03:47.300
And in the response, again, we see this

70
00:03:47.300 --> 00:03:48.480
conversion params.

71
00:03:48.480 --> 00:03:50.400
So I'm actually just going to right click

72
00:03:50.400 --> 00:03:53.620
and highlight this so that we don't lose

73
00:03:53.620 --> 00:03:53.920
it.

74
00:03:55.480 --> 00:03:57.160
Because I want to keep this request.

75
00:03:58.000 --> 00:04:00.000
And the same goes for this one.

76
00:04:01.640 --> 00:04:03.280
Usually when I'm working on a bunch of

77
00:04:03.280 --> 00:04:06.080
things, occasionally I'll highlight requests just so that

78
00:04:06.080 --> 00:04:07.800
I know that I need to come back

79
00:04:07.800 --> 00:04:11.480
and look at them more closely or carry

80
00:04:11.480 --> 00:04:12.320
on testing them.

81
00:04:13.260 --> 00:04:14.880
So we send this request.

82
00:04:15.440 --> 00:04:17.720
And here what I'm going to do is

83
00:04:17.720 --> 00:04:22.040
I'm going to just do colon paste.

84
00:04:23.100 --> 00:04:27.020
And usual remote code execution is we can

85
00:04:27.020 --> 00:04:28.800
do something like ampersand ampersand.

86
00:04:29.000 --> 00:04:31.720
And this will basically say, hey, once you're

87
00:04:31.720 --> 00:04:34.200
done with the previous command, please run the

88
00:04:34.200 --> 00:04:34.900
next command.

89
00:04:35.500 --> 00:04:37.280
And I'm just going to do something like

90
00:04:37.280 --> 00:04:43.620
touch temp and RCE, something really simple.

91
00:04:43.620 --> 00:04:46.780
And because we're testing locally, we can simply

92
00:04:46.780 --> 00:04:50.340
log into the docker container and check that

93
00:04:50.340 --> 00:04:51.400
this has actually worked.

94
00:04:51.700 --> 00:04:53.480
Or you could get it to ping you

95
00:04:53.480 --> 00:04:55.620
or you could even set up a reverse

96
00:04:55.620 --> 00:04:58.220
shell or you could get it to curl

97
00:04:58.220 --> 00:04:58.680
a website.

98
00:04:59.000 --> 00:05:03.100
So for example, webhook.site is quite a

99
00:05:03.100 --> 00:05:04.680
useful site.

100
00:05:04.860 --> 00:05:08.600
So you just copy in this URL here

101
00:05:08.600 --> 00:05:10.600
and then any requests that come in.

102
00:05:10.600 --> 00:05:11.900
So I'll just show you quickly.

103
00:05:12.160 --> 00:05:14.180
If we manage to invoke this, it's a

104
00:05:14.180 --> 00:05:16.200
good way to cross server-side request forgery.

105
00:05:16.400 --> 00:05:17.980
We'd see the request coming in.

106
00:05:18.400 --> 00:05:21.380
Obviously, don't do this with production systems where

107
00:05:21.380 --> 00:05:23.040
there's sensitive data and things like that.

108
00:05:23.100 --> 00:05:25.700
You don't know what webhook.sites are doing

109
00:05:25.700 --> 00:05:26.420
with their data.

110
00:05:27.160 --> 00:05:29.540
But for this, it's totally fine.

111
00:05:30.040 --> 00:05:31.100
Or you can just set up your own

112
00:05:31.100 --> 00:05:33.040
web server and call out to that.

113
00:05:33.940 --> 00:05:35.340
There are a lot of different options.

114
00:05:35.680 --> 00:05:37.580
So find one that works for you, that's

115
00:05:37.580 --> 00:05:40.020
kind of reliable and that you can play

116
00:05:40.020 --> 00:05:41.940
around with and then you should be good

117
00:05:41.940 --> 00:05:42.340
to go.

118
00:05:42.740 --> 00:05:44.460
Now, the next thing we need to do

119
00:05:44.460 --> 00:05:45.920
is actually trigger this.

120
00:05:46.280 --> 00:05:48.920
So when I was looking at the functionality,

121
00:05:49.340 --> 00:05:51.940
I saw this share video with community.

122
00:05:52.360 --> 00:05:55.040
So we can just click this and we

123
00:05:55.040 --> 00:05:55.640
get a failed.

124
00:05:55.720 --> 00:05:57.660
We get a could not convert video.

125
00:05:58.120 --> 00:05:59.820
So if we come back to web suite,

126
00:06:00.760 --> 00:06:07.100
come down here and we see the request

127
00:06:07.100 --> 00:06:07.460
here.

128
00:06:07.460 --> 00:06:11.440
So could not convert video ID 83.

129
00:06:12.020 --> 00:06:14.240
So I'm just going to highlight that, send

130
00:06:14.240 --> 00:06:16.580
it to the repeater, and let's just see

131
00:06:16.580 --> 00:06:17.380
what's happening.

132
00:06:18.720 --> 00:06:21.960
And this is a little bit like CTFE

133
00:06:21.960 --> 00:06:23.060
here, I would say.

134
00:06:23.600 --> 00:06:26.500
We could probably have found this without needing

135
00:06:26.500 --> 00:06:30.380
the message, but it says this endpoint should

136
00:06:30.380 --> 00:06:34.420
be accessed only internally and it gives us

137
00:06:34.420 --> 00:06:36.240
the endpoint URL as well.

138
00:06:36.240 --> 00:06:39.940
So if we're accessing this endpoint externally, obviously

139
00:06:39.940 --> 00:06:44.780
we're going to localhost 888 and this URI

140
00:06:44.780 --> 00:06:45.220
here.

141
00:06:45.620 --> 00:06:47.140
But if we're going to go to it

142
00:06:47.140 --> 00:06:50.640
locally, then we actually need to call HTTP

143
00:06:50.640 --> 00:06:54.440
crappy identity 8080, which is different to our

144
00:06:54.440 --> 00:06:57.320
8888, and then call it.

145
00:06:58.360 --> 00:07:00.200
So it took me a little bit of

146
00:07:00.200 --> 00:07:02.240
time to realize that this was different and

147
00:07:02.240 --> 00:07:03.040
the routing was different.

148
00:07:03.040 --> 00:07:05.900
It wasn't the same as the external, but,

149
00:07:06.140 --> 00:07:08.360
you know, we live and learn to look

150
00:07:08.360 --> 00:07:09.140
in the details.

151
00:07:09.440 --> 00:07:12.000
And I would say that occasionally an endpoint

152
00:07:12.000 --> 00:07:14.360
might be like, hey, you know, you can't

153
00:07:14.360 --> 00:07:16.520
reach this from where you are, or this

154
00:07:16.520 --> 00:07:18.240
resource isn't externally available.

155
00:07:18.880 --> 00:07:20.680
And again, that's kind of like a clue

156
00:07:20.680 --> 00:07:23.640
that maybe if we have SSRF or if

157
00:07:23.640 --> 00:07:25.640
we have another way to access it, then

158
00:07:25.640 --> 00:07:28.740
we might be able to trigger this vulnerability

159
00:07:28.740 --> 00:07:30.960
or at least get access to this endpoint.

160
00:07:30.960 --> 00:07:33.700
And if you look closely, we have this

161
00:07:33.700 --> 00:07:34.080
SSRF.

162
00:07:37.760 --> 00:07:39.620
So it's actually giving us a big clue.

163
00:07:39.940 --> 00:07:43.500
Luckily, we already discovered the SSRF endpoints in

164
00:07:43.500 --> 00:07:44.320
the application.

165
00:07:44.660 --> 00:07:47.860
So I'm just going to copy this and

166
00:07:47.860 --> 00:07:49.980
then we're going to click OK.

167
00:07:50.360 --> 00:07:52.080
And then we're going to go back to

168
00:07:52.080 --> 00:07:56.940
our trusty mechanic and test.

169
00:07:57.740 --> 00:07:58.560
Click OK.

170
00:08:00.590 --> 00:08:02.650
Come back to PubSuite.

171
00:08:06.530 --> 00:08:08.410
And I'm looking for a post request.

172
00:08:08.710 --> 00:08:09.330
Here we are.

173
00:08:12.140 --> 00:08:12.640
Get this.

174
00:08:14.040 --> 00:08:16.080
And then let's just send this to the

175
00:08:16.080 --> 00:08:17.380
repeater as well.

176
00:08:18.240 --> 00:08:19.600
And again, this highlighting is quite useful.

177
00:08:19.740 --> 00:08:20.620
If you're going to come back and do

178
00:08:20.620 --> 00:08:22.760
reporting and you're not taking very good notes

179
00:08:22.760 --> 00:08:24.400
as you go, that can be quite a

180
00:08:24.400 --> 00:08:25.500
handy thing to do.

181
00:08:27.820 --> 00:08:29.500
So I just send this and it says

182
00:08:29.500 --> 00:08:29.800
OK.

183
00:08:29.800 --> 00:08:33.520
And what we want to do is copy

184
00:08:33.520 --> 00:08:35.900
in our endpoint.

185
00:08:37.220 --> 00:08:38.360
Click send.

186
00:08:40.909 --> 00:08:43.590
And the video ID parameter is missing.

187
00:08:43.910 --> 00:08:46.430
So we need video 83.

188
00:08:51.760 --> 00:08:52.540
Click send.

189
00:08:55.030 --> 00:08:58.910
Video conversion bash command triggered.

190
00:09:06.170 --> 00:09:09.610
And I wasn't actually expecting that to come

191
00:09:09.610 --> 00:09:10.090
back.

192
00:09:10.150 --> 00:09:12.650
So let me double check the endpoint.

193
00:09:13.050 --> 00:09:15.870
Ah, I forgot to hit send on here.

194
00:09:15.950 --> 00:09:17.830
So we didn't actually update the video.

195
00:09:19.170 --> 00:09:22.850
So we just come back, hit send and

196
00:09:22.850 --> 00:09:24.530
we get this message.

197
00:09:25.010 --> 00:09:28.070
So all I'm going to do is copy

198
00:09:28.070 --> 00:09:28.410
this.

199
00:09:28.510 --> 00:09:29.830
Looks like base64.

200
00:09:31.210 --> 00:09:33.010
Come to the decoder.

201
00:09:34.510 --> 00:09:38.690
Decode as base64 and says, wow, look at

202
00:09:38.690 --> 00:09:38.930
you.

203
00:09:38.930 --> 00:09:42.590
Combining mass assignment and SSRF to exploit a

204
00:09:42.590 --> 00:09:43.970
hidden shell injection.

205
00:09:44.270 --> 00:09:45.270
We're very proud.

206
00:09:45.730 --> 00:09:46.530
I'm glad you're proud.

207
00:09:46.630 --> 00:09:48.830
It's nice to have somebody who's proud of

208
00:09:48.830 --> 00:09:49.010
you.

209
00:09:49.330 --> 00:09:49.910
You won the game.

210
00:09:50.170 --> 00:09:52.210
Unfortunately, we don't actually allow our pen tester

211
00:09:52.210 --> 00:09:55.890
to run arbitrary shell commands on our backend.

212
00:09:56.270 --> 00:09:58.490
Could be very expensive and annoying to maintain.

213
00:09:58.950 --> 00:10:01.090
Again, yeah, very easy to destroy a system,

214
00:10:01.230 --> 00:10:03.910
especially if you've got multiple students doing crazy

215
00:10:03.910 --> 00:10:04.350
things.

216
00:10:04.510 --> 00:10:05.910
So a little bit limiting there.

217
00:10:06.070 --> 00:10:07.550
But if you want to go ahead and

218
00:10:07.550 --> 00:10:10.390
get your shell, then feel free to follow

219
00:10:10.390 --> 00:10:14.630
the instructions and update the configuration and try

220
00:10:14.630 --> 00:10:15.370
it yourself.

221
00:10:15.750 --> 00:10:19.090
So that's it for the chain vulnerability walkthrough

222
00:10:19.090 --> 00:10:20.050
to RCE.

223
00:10:20.830 --> 00:10:24.010
And so I have a kitten on my

224
00:10:24.010 --> 00:10:24.810
on my desk.

225
00:10:24.970 --> 00:10:27.230
I'll see you in the next video for

226
00:10:27.230 --> 00:10:28.750
the capstone challenge.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: Final Capstone

WEBVTT

1
00:00:00.330 --> 00:00:04.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome to the final capstone challenge and I'm

2
00:00:04.130 --> 00:00:06.610
really excited that you've made it this far

3
00:00:06.610 --> 00:00:08.850
and I really hope you enjoyed the journey

4
00:00:08.850 --> 00:00:11.910
throughout this course and managed to learn some

5
00:00:11.910 --> 00:00:14.130
new things that you can add to your

6
00:00:14.130 --> 00:00:15.410
arsenal going forward.

7
00:00:15.650 --> 00:00:17.850
Now this final challenge is going to be

8
00:00:17.850 --> 00:00:21.470
purely focused on some API endpoints, so let

9
00:00:21.470 --> 00:00:22.810
me give you a bit of a briefing.

10
00:00:23.330 --> 00:00:26.330
A company is building a web app called

11
00:00:26.330 --> 00:00:27.550
the Pasta Mentor.

12
00:00:27.830 --> 00:00:29.990
There are a number of teams working on

13
00:00:29.990 --> 00:00:32.290
it and they feel like they're ready to

14
00:00:32.290 --> 00:00:34.550
have the back-end pen tested for issues

15
00:00:34.550 --> 00:00:37.710
before the front-end integration takes place.

16
00:00:38.150 --> 00:00:39.870
The tools that you use are up to

17
00:00:39.870 --> 00:00:41.350
you and you can take as long as

18
00:00:41.350 --> 00:00:43.270
you'd like to assess the application.

19
00:00:44.010 --> 00:00:46.110
The developers have provided a couple of things

20
00:00:46.110 --> 00:00:49.490
though, some basic documentation of the One of

21
00:00:49.490 --> 00:00:53.410
them has also kindly added an application reset

22
00:00:53.410 --> 00:00:55.430
endpoint for testing purposes.

23
00:00:56.010 --> 00:00:57.950
This clears out all of the data of

24
00:00:57.950 --> 00:01:00.650
the application and creates some new test data

25
00:01:00.650 --> 00:01:01.490
within the app.

26
00:01:01.750 --> 00:01:03.610
We're also given a heads-up that the

27
00:01:03.610 --> 00:01:07.050
application uses JSON, so whilst we're free to

28
00:01:07.050 --> 00:01:09.650
test other payload types for issues and things,

29
00:01:09.910 --> 00:01:12.070
we shouldn't let the content type header trip

30
00:01:12.070 --> 00:01:12.510
us up.

31
00:01:12.670 --> 00:01:15.850
Some sample data is also provided and this

32
00:01:15.850 --> 00:01:18.390
is somewhat similar to a situation where you

33
00:01:18.390 --> 00:01:20.730
might get a bunch of exported confluence pages

34
00:01:20.730 --> 00:01:22.290
or development notes.

35
00:01:22.530 --> 00:01:24.050
So let's take a quick look at this

36
00:01:24.050 --> 00:01:25.730
and then I'll let you dive in.

37
00:01:26.490 --> 00:01:29.210
So here we are and I have the

38
00:01:29.210 --> 00:01:33.350
api.finalcapstone.zip in this folder, so I'm

39
00:01:33.350 --> 00:01:37.030
just going to right click and extract here.

40
00:01:38.610 --> 00:01:41.610
Give it a second to run and then

41
00:01:41.610 --> 00:01:43.290
what I'm going to do is I'm going

42
00:01:43.290 --> 00:01:48.230
to open the terminal, cd into labs, cd

43
00:01:48.230 --> 00:01:54.910
into api.finalcapstone. Close this down and looks

44
00:01:54.910 --> 00:01:56.390
like we're all good to go.

45
00:01:56.550 --> 00:02:04.020
So sudo docker-compose up and we'll give

46
00:02:04.020 --> 00:02:05.560
it a second to load.

47
00:02:06.400 --> 00:02:08.400
That was pretty quick, so we get MongoDB

48
00:02:08.400 --> 00:02:09.020
connected.

49
00:02:09.699 --> 00:02:11.040
So the first thing we want to do

50
00:02:11.040 --> 00:02:18.260
is come to the application, so http//localhost, and

51
00:02:18.260 --> 00:02:19.960
it's running on 3000.

52
00:02:19.960 --> 00:02:22.860
If you're ever unsure where it's running, if

53
00:02:22.860 --> 00:02:30.340
you come into labs, cd api.finalcapstone. If

54
00:02:30.340 --> 00:02:32.100
we just look in the docker compose file,

55
00:02:32.200 --> 00:02:35.220
you can see that 3000 is open and

56
00:02:35.220 --> 00:02:37.140
routing to port 3000.

57
00:02:37.420 --> 00:02:39.340
So this is the web app we want

58
00:02:39.340 --> 00:02:43.080
to connect on port 3000.

59
00:02:44.040 --> 00:02:46.300
So I'll just switch my proxy off for

60
00:02:46.300 --> 00:02:49.020
the time being, and when we come to

61
00:02:49.020 --> 00:02:51.960
this we can see that we do indeed

62
00:02:51.960 --> 00:02:54.680
have some basic documentation.

63
00:02:55.360 --> 00:02:58.600
Although unfortunately it doesn't give us a full

64
00:02:58.600 --> 00:03:01.440
set of testable payloads, but it's a very

65
00:03:01.440 --> 00:03:03.040
useful place to begin.

66
00:03:04.460 --> 00:03:07.360
Something else that we want to just make

67
00:03:07.360 --> 00:03:09.660
note of before we started, so as I

68
00:03:09.660 --> 00:03:12.460
mentioned before, we have a reset function.

69
00:03:12.780 --> 00:03:15.580
So we have this controls slash reset.

70
00:03:16.140 --> 00:03:17.820
So if I just come into the application,

71
00:03:18.440 --> 00:03:27.790
type controls reset, and if I can spell

72
00:03:27.790 --> 00:03:32.010
it right, we get the application data is

73
00:03:32.010 --> 00:03:32.530
reset.

74
00:03:32.770 --> 00:03:34.310
So if that's a little bit small for

75
00:03:34.310 --> 00:03:34.510
you.

76
00:03:35.370 --> 00:03:37.850
So this is just for testing purposes, you

77
00:03:37.850 --> 00:03:40.610
can use this as much or as little

78
00:03:40.610 --> 00:03:41.550
as you'd like.

79
00:03:42.710 --> 00:03:46.070
One other thing to check out is if

80
00:03:46.070 --> 00:03:49.670
we come to slash controls, I think there

81
00:03:49.670 --> 00:03:52.770
is also a file called sample data as

82
00:03:52.770 --> 00:03:53.150
well.

83
00:03:53.330 --> 00:03:55.530
So you can come in here, and like

84
00:03:55.530 --> 00:03:58.610
I say, this kind of simulates some developer

85
00:03:58.610 --> 00:04:01.290
notes, or some old confluence pages, or some

86
00:04:01.290 --> 00:04:03.650
exports, things that the developers have been working

87
00:04:03.650 --> 00:04:06.670
on, and maybe their personal notes and payloads.

88
00:04:06.830 --> 00:04:08.550
So this is a really great place to

89
00:04:08.550 --> 00:04:10.470
start, it gives you a sample request to

90
00:04:10.470 --> 00:04:13.750
get started with the application, and for these

91
00:04:13.750 --> 00:04:16.810
endpoints that are listed here in swagger, you've

92
00:04:16.810 --> 00:04:19.329
got some test payloads as well.

93
00:04:19.829 --> 00:04:21.470
So I'm just going to quickly make a

94
00:04:21.470 --> 00:04:23.350
request to make sure everything is working.

95
00:04:23.650 --> 00:04:26.070
So what I'm going to do is actually,

96
00:04:26.610 --> 00:04:30.090
let's just split this and load up postman.

97
00:04:35.420 --> 00:04:40.540
Let's just create a new collection, rename this

98
00:04:40.540 --> 00:04:48.880
collection to final capstone, and then in here,

99
00:04:49.980 --> 00:04:50.780
add request.

100
00:04:51.900 --> 00:04:53.860
I'm just going to close this, close this,

101
00:04:54.080 --> 00:05:02.300
and what we'll do is we will, let's

102
00:05:02.300 --> 00:05:05.620
see, what request do we want to do?

103
00:05:06.300 --> 00:05:11.160
Let's post to register, so ctrl c on

104
00:05:11.160 --> 00:05:17.170
this, change this to post, and we want

105
00:05:17.170 --> 00:05:22.210
to put the full address in, localhost 3000,

106
00:05:23.550 --> 00:05:28.510
rename this to register, and in the body

107
00:05:28.510 --> 00:05:31.990
we want raw data, and we want it

108
00:05:31.990 --> 00:05:35.150
to be json, because that's what we've been

109
00:05:35.150 --> 00:05:35.890
given here.

110
00:05:36.130 --> 00:05:39.110
So, whoops, I'm just going to grab this,

111
00:05:39.850 --> 00:05:44.210
copy and paste, and then let's just hit

112
00:05:44.210 --> 00:05:48.530
send, and we get a registration successful, which

113
00:05:48.530 --> 00:05:48.950
is great.

114
00:05:49.010 --> 00:05:50.610
So that's exactly what we wanted to see,

115
00:05:50.610 --> 00:05:54.130
and again in burp, so make sure the

116
00:05:54.130 --> 00:05:56.070
application is working in burp suite.

117
00:05:57.170 --> 00:05:59.150
Let's not update right this second.

118
00:06:06.060 --> 00:06:07.860
What I'm going to do is I'm going

119
00:06:07.860 --> 00:06:13.240
to just switch on my proxy, hit refresh

120
00:06:13.240 --> 00:06:15.560
here, so that I've got a request coming

121
00:06:15.560 --> 00:06:24.300
in, send this to the repeater, change the

122
00:06:24.300 --> 00:06:26.840
request method, which changes it to a post.

123
00:06:27.460 --> 00:06:30.880
I have my sample data here, and I

124
00:06:30.880 --> 00:06:32.640
suspect it's going to throw an error if

125
00:06:32.640 --> 00:06:34.720
I just send test, although let's just give

126
00:06:34.720 --> 00:06:35.660
this a go anyway.

127
00:06:37.020 --> 00:06:40.160
And the content type, so we have application

128
00:06:41.480 --> 00:06:45.440
x www form, so I have actually an

129
00:06:45.440 --> 00:06:53.630
extension installed called content type converter, so you're

130
00:06:53.630 --> 00:06:55.830
welcome to go ahead and install this.

131
00:06:56.250 --> 00:06:58.630
So all it does is enables me to

132
00:06:58.630 --> 00:07:03.290
go extensions, whoops, content type converter, convert to

133
00:07:03.290 --> 00:07:06.630
json, or you can just manually change this,

134
00:07:07.010 --> 00:07:11.690
so for example this to json, like that.

135
00:07:11.930 --> 00:07:14.150
So it's up to you really, whatever you

136
00:07:14.150 --> 00:07:14.630
want to do.

137
00:07:16.680 --> 00:07:18.460
I'm just going to use this content type

138
00:07:18.460 --> 00:07:20.960
converter, and then click send.

139
00:07:23.780 --> 00:07:27.600
Whoops, I think I undid this, so this

140
00:07:27.600 --> 00:07:35.080
was v1 auth register, and we get, yeah,

141
00:07:35.340 --> 00:07:37.740
username already exists, so of course if we

142
00:07:37.740 --> 00:07:41.040
give it a unique username, hit send, we

143
00:07:41.040 --> 00:07:43.100
get registration successful, and we get a session

144
00:07:43.100 --> 00:07:43.700
id back.

145
00:07:44.240 --> 00:07:44.960
Okay, great.

146
00:07:45.320 --> 00:07:48.400
So the application is working, everything is set

147
00:07:48.400 --> 00:07:51.760
up, feel free to use bubsuite, or wfuzz,

148
00:07:51.900 --> 00:07:55.560
or postman, or any tool you want really.

149
00:07:56.040 --> 00:07:58.460
This is your assessment, make the most of

150
00:07:58.460 --> 00:08:01.180
it, try and find some critical issues that

151
00:08:01.180 --> 00:08:03.240
you'd be very happy to put at the

152
00:08:03.240 --> 00:08:06.420
top of a report, and put some recommendations

153
00:08:06.420 --> 00:08:06.960
into.

154
00:08:07.240 --> 00:08:08.960
Good luck, and I'll see you in the

155
00:08:08.960 --> 00:08:10.160
next video for the walkthrough.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:01.640
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, welcome back.

2
00:00:01.900 --> 00:00:05.660
Let's take a look at this application and

3
00:00:05.660 --> 00:00:07.720
I'm going to walk you through kind of

4
00:00:07.720 --> 00:00:10.100
how I would approach this and things that

5
00:00:10.100 --> 00:00:12.120
I would look out for and how I

6
00:00:12.120 --> 00:00:14.960
would kind of like follow my intuition to

7
00:00:14.960 --> 00:00:16.180
find vulnerabilities.

8
00:00:16.860 --> 00:00:19.680
And of course everybody's methodology is a little

9
00:00:19.680 --> 00:00:23.400
difference, but I quite enjoy manual testing and

10
00:00:23.400 --> 00:00:26.380
being thorough and stepping through the application step

11
00:00:26.380 --> 00:00:26.980
by step.

12
00:00:27.260 --> 00:00:30.640
Other people go for a more automated approach

13
00:00:30.640 --> 00:00:32.440
with lots of recon and then dive into

14
00:00:32.440 --> 00:00:35.980
things separately, and both are valid approaches.

15
00:00:36.540 --> 00:00:39.460
So do what's best for you and let's

16
00:00:39.460 --> 00:00:40.220
dive in.

17
00:00:41.800 --> 00:00:44.620
So first step, I'm going to come over

18
00:00:44.620 --> 00:00:46.180
to Postman.

19
00:00:46.420 --> 00:00:48.520
So we have this new collection here.

20
00:00:48.540 --> 00:00:50.260
I'm just going to delete this.

21
00:00:53.400 --> 00:00:54.600
So it's out of the way.

22
00:00:54.920 --> 00:00:58.940
And then we already have our register endpoints

23
00:00:58.940 --> 00:01:02.100
and it looks like we can register a

24
00:01:02.100 --> 00:01:04.220
new user and we get a session token.

25
00:01:04.740 --> 00:01:06.380
So what I'm going to do is, usually

26
00:01:06.380 --> 00:01:09.380
I use Obsidian for notes, but I run

27
00:01:09.380 --> 00:01:12.520
Obsidian on my host machine and just because

28
00:01:12.520 --> 00:01:13.680
of the way the camera is set up

29
00:01:13.680 --> 00:01:15.480
and capturing the VM, I'm just going to

30
00:01:15.480 --> 00:01:17.380
keep some notes in mousepad.

31
00:01:17.620 --> 00:01:19.740
So in fact, I might just keep it

32
00:01:19.740 --> 00:01:25.040
on another monitor, another workspace, sorry, because otherwise

33
00:01:25.040 --> 00:01:27.200
it's going to get very, very full on

34
00:01:27.200 --> 00:01:28.700
this one over here.

35
00:01:28.880 --> 00:01:32.700
So I'm just going to come in and

36
00:01:32.700 --> 00:01:34.500
just write test test.

37
00:01:35.720 --> 00:01:41.280
So this is our login credentials and our

38
00:01:41.280 --> 00:01:42.400
session ID.

39
00:01:42.820 --> 00:01:45.600
So just keeping some notes so that we

40
00:01:45.600 --> 00:01:46.620
can come back to them.

41
00:01:47.480 --> 00:01:52.780
And the next endpoint down is v1-auth

42
00:01:52.780 --> 00:01:53.280
-login.

43
00:01:54.560 --> 00:02:00.910
So let's come back to Postman and I'm

44
00:02:00.910 --> 00:02:05.680
just going to come in and add request.

45
00:02:07.660 --> 00:02:10.340
And let's call this login.

46
00:02:11.520 --> 00:02:14.180
And I'm just going to come here, copy

47
00:02:14.180 --> 00:02:20.910
this, paste, and then we'll come here.

48
00:02:22.690 --> 00:02:24.530
And it looks like it takes the same

49
00:02:24.530 --> 00:02:26.670
username and password as before.

50
00:02:26.670 --> 00:02:35.730
So let's just go body raw json and

51
00:02:35.730 --> 00:02:36.030
send.

52
00:02:38.220 --> 00:02:39.700
And it looks like we need to change

53
00:02:39.700 --> 00:02:40.500
the request method.

54
00:02:42.660 --> 00:02:43.580
Let's try that again.

55
00:02:44.100 --> 00:02:45.440
And we get login successful.

56
00:02:45.840 --> 00:02:47.940
So we probably get a new session ID

57
00:02:47.940 --> 00:02:51.440
now that we've logged in a separate time.

58
00:02:52.760 --> 00:02:56.280
Yeah, it looks kind of similar, which is

59
00:02:56.280 --> 00:03:00.800
interesting, but somewhat different towards the end.

60
00:03:03.170 --> 00:03:04.730
And what I'm going to do is actually

61
00:03:04.730 --> 00:03:06.690
send this request again.

62
00:03:07.650 --> 00:03:14.800
So come over to send and then grab

63
00:03:14.800 --> 00:03:15.300
this.

64
00:03:17.260 --> 00:03:19.920
It looks like the request is different again.

65
00:03:20.140 --> 00:03:24.100
So at this point, it looks like the

66
00:03:24.100 --> 00:03:27.420
session token that we're getting back, the session

67
00:03:27.420 --> 00:03:30.620
ID here, is quite short and looks like

68
00:03:30.620 --> 00:03:32.480
it's base64 encoded.

69
00:03:32.760 --> 00:03:35.480
So we can just come to pubsuite decoder,

70
00:03:37.560 --> 00:03:39.580
decode as base64.

71
00:03:40.380 --> 00:03:42.240
Yeah, and it looks like it's just our

72
00:03:42.240 --> 00:03:45.460
username and then some text or some random

73
00:03:45.460 --> 00:03:46.360
string afterwards.

74
00:03:46.540 --> 00:03:50.120
So we've got a lowercase, uppercase, and a

75
00:03:50.120 --> 00:03:51.240
number in there.

76
00:03:51.280 --> 00:03:52.880
This doesn't look very strong.

77
00:03:53.000 --> 00:03:55.100
So let's do a little bit of analysis

78
00:03:55.100 --> 00:03:56.140
on this.

79
00:03:56.880 --> 00:03:58.900
And what I want to do is come

80
00:03:58.900 --> 00:04:01.120
into repeater.

81
00:04:02.400 --> 00:04:04.460
And we're just going to change this to

82
00:04:04.460 --> 00:04:09.810
login, check that this works.

83
00:04:09.930 --> 00:04:11.310
So we get our login success.

84
00:04:12.090 --> 00:04:14.010
And then we're going to right click and

85
00:04:14.010 --> 00:04:15.550
send to sequencer.

86
00:04:17.149 --> 00:04:19.050
And then what we want to do is

87
00:04:19.050 --> 00:04:21.750
configure this so it knows where our session

88
00:04:21.750 --> 00:04:22.430
ID is.

89
00:04:23.070 --> 00:04:23.730
Click OK.

90
00:04:26.240 --> 00:04:28.800
And then since it's base64, again, I want

91
00:04:28.800 --> 00:04:31.740
to come to the analysis options and base64

92
00:04:31.740 --> 00:04:33.600
decode before analyzing.

93
00:04:34.480 --> 00:04:36.760
And then we'll just start the live capture.

94
00:04:38.680 --> 00:04:40.940
This won't take too long because it's a

95
00:04:40.940 --> 00:04:44.200
local instance.

96
00:04:49.200 --> 00:04:51.280
And while it's doing that, what we'll do

97
00:04:51.280 --> 00:04:54.580
is we can come back and test another

98
00:04:54.580 --> 00:04:55.120
endpoint.

99
00:04:55.900 --> 00:04:58.820
So we've got this v1 auth check.

100
00:05:01.700 --> 00:05:05.660
Actually, since we're harvesting IDs, we're probably going

101
00:05:07.360 --> 00:05:10.880
to be unsuccessful, because hopefully the IDs don't

102
00:05:10.880 --> 00:05:11.740
just last forever.

103
00:05:11.860 --> 00:05:13.560
Although that's something we should check for.

104
00:05:13.820 --> 00:05:16.460
Does an old session token still work even

105
00:05:16.460 --> 00:05:17.520
after we get a new one?

106
00:05:17.660 --> 00:05:19.240
Or is it invalidated?

107
00:05:22.880 --> 00:05:24.290
So I'm just going to come over to

108
00:05:24.290 --> 00:05:32.320
postman, add request, and just call this auth

109
00:05:32.320 --> 00:05:46.990
check, localhost 3000, grab

110
00:05:46.990 --> 00:05:53.860
the payload, raw, JSON, and put that in.

111
00:05:54.380 --> 00:05:55.280
We'll just send it.

112
00:05:55.900 --> 00:05:58.800
And we probably, again, need some changes to

113
00:05:58.800 --> 00:06:00.200
post, as I always forget.

114
00:06:00.700 --> 00:06:03.680
And then with the invalid session ID of

115
00:06:03.680 --> 00:06:05.780
test, of course, it's just going to come

116
00:06:05.780 --> 00:06:06.540
back unauthorized.

117
00:06:06.640 --> 00:06:09.560
But this endpoint is working, so that's useful

118
00:06:09.560 --> 00:06:10.000
to know.

119
00:06:18.000 --> 00:06:19.820
So the live capture is about halfway done,

120
00:06:19.960 --> 00:06:21.960
so I'll just wait for this to finish.

121
00:06:33.180 --> 00:06:35.420
All right, and it looks like it's finished.

122
00:06:35.620 --> 00:06:38.160
So we can just hit analyze now.

123
00:06:39.940 --> 00:06:43.200
And the overall result, so the overall quality

124
00:06:43.200 --> 00:06:45.860
of randomness within the sample is estimated to

125
00:06:45.860 --> 00:06:48.540
be poor, at a significance level of one

126
00:06:48.540 --> 00:06:51.480
percent, and the amount of effective entropy is

127
00:06:51.480 --> 00:06:54.080
estimated to be 30 bits.

128
00:06:55.240 --> 00:06:57.140
So if we come to the character level

129
00:06:57.140 --> 00:07:00.680
analysis, we can see that indeed we have

130
00:07:00.680 --> 00:07:03.260
our username, and this is highly predictable.

131
00:07:03.800 --> 00:07:05.840
And then we have a lot of random

132
00:07:05.840 --> 00:07:08.760
characters afterwards as well.

133
00:07:08.920 --> 00:07:12.100
So this is quite weak, and I think

134
00:07:13.920 --> 00:07:17.400
if you wanted to, you could probably brute

135
00:07:17.400 --> 00:07:17.960
force this.

136
00:07:18.040 --> 00:07:20.200
You could write a quick Python script that

137
00:07:20.200 --> 00:07:24.680
takes an input, generates six random characters, and

138
00:07:24.680 --> 00:07:27.120
then spits out a word list, and then

139
00:07:27.120 --> 00:07:29.320
you might be able to demonstrate this attack.

140
00:07:29.980 --> 00:07:32.840
And if you have some skeptical developers, or

141
00:07:32.840 --> 00:07:34.680
if you want to show this off in

142
00:07:34.680 --> 00:07:37.640
your reports, then I would definitely recommend doing

143
00:07:37.640 --> 00:07:43.940
this exercise, writing the script, and finding a

144
00:07:43.940 --> 00:07:45.840
session and taking it over.

145
00:07:48.700 --> 00:07:51.680
But for now, I think, given this summary,

146
00:07:51.920 --> 00:07:56.060
this is probably enough for reporting in most

147
00:07:56.060 --> 00:07:56.700
cases.

148
00:07:57.120 --> 00:08:01.780
So next up, we have v1-recipes.

149
00:08:02.080 --> 00:08:04.460
So we can search for a recipe.

150
00:08:04.800 --> 00:08:09.540
So let's come to here, and interesting that

151
00:08:10.500 --> 00:08:14.760
so get v1-recipe, get v1-recipe.

152
00:08:14.860 --> 00:08:17.720
Ah, so it has a parameter.

153
00:08:18.260 --> 00:08:20.580
So I'm just going to copy this, and

154
00:08:20.580 --> 00:08:23.760
then I'm going to pull this into bubsuite,

155
00:08:24.120 --> 00:08:25.800
come back to my repeater.

156
00:08:28.740 --> 00:08:30.400
Is it recipes or recipe?

157
00:08:30.680 --> 00:08:31.480
I can't remember.

158
00:08:32.520 --> 00:08:35.100
We can right click, change the request method

159
00:08:35.100 --> 00:08:43.520
to get, that's recipes, send this, and see

160
00:08:43.520 --> 00:08:44.480
what comes back.

161
00:08:44.940 --> 00:08:51.280
And we get an okay with no data

162
00:08:51.280 --> 00:08:52.280
coming back.

163
00:08:52.800 --> 00:08:57.080
So likely there are not any entries, so

164
00:08:57.080 --> 00:09:00.320
let's just leave this blank, and we do

165
00:09:00.320 --> 00:09:01.400
get some data back.

166
00:09:01.500 --> 00:09:03.980
So it looks like this is working, and

167
00:09:03.980 --> 00:09:08.240
we get the alfredo, and the spaghetti with

168
00:09:08.240 --> 00:09:09.000
meat sauce.

169
00:09:09.700 --> 00:09:14.100
And something that is interesting here is we

170
00:09:14.100 --> 00:09:16.840
need to pay attention to the intended behavior

171
00:09:16.840 --> 00:09:20.220
of the application, and this says is private

172
00:09:20.220 --> 00:09:20.720
true.

173
00:09:21.080 --> 00:09:24.020
So this is probably a little bit of

174
00:09:24.020 --> 00:09:25.960
a leaky API, and the point we can

175
00:09:25.960 --> 00:09:27.720
see the chef here is the admin, so

176
00:09:27.720 --> 00:09:29.260
this is probably the creator.

177
00:09:30.900 --> 00:09:33.760
And it's also useful to notice that we

178
00:09:33.760 --> 00:09:36.080
have some IDs here as well.

179
00:09:40.540 --> 00:09:43.420
So this is kind of some interesting points

180
00:09:43.420 --> 00:09:45.560
that we want to just take away from

181
00:09:45.560 --> 00:09:49.380
this endpoint and consider or think about.

182
00:09:49.560 --> 00:09:50.980
So I'm just going to add this one

183
00:09:50.980 --> 00:10:10.620
into my post mine collection, and then

184
00:10:10.620 --> 00:10:13.000
we can just check that it works, and

185
00:10:13.000 --> 00:10:14.300
we're good to go.

186
00:10:15.760 --> 00:10:23.480
All right, so next up we have post

187
00:10:23.480 --> 00:10:24.020
recipes.

188
00:10:24.880 --> 00:10:30.480
So interesting that in the developer notes that

189
00:10:30.480 --> 00:10:32.540
they gave us we have a post v1

190
00:10:32.540 --> 00:10:35.740
recipes, but in the swagger notes we don't

191
00:10:35.740 --> 00:10:37.220
have a post recipes.

192
00:10:37.380 --> 00:10:39.160
We have a put, which looks like it

193
00:10:39.160 --> 00:10:42.540
will update a recipe, but maybe they've missed

194
00:10:42.540 --> 00:10:44.060
this out in the documentation.

195
00:10:44.620 --> 00:10:46.840
And don't be surprised if this happens.

196
00:10:47.020 --> 00:10:49.620
This happens quite a lot where information is

197
00:10:49.620 --> 00:10:52.580
out of date or missing, and it basically

198
00:10:52.580 --> 00:10:54.920
signals to us that we need to do

199
00:10:54.920 --> 00:10:56.360
a little bit of fuzzing, we need to

200
00:10:56.360 --> 00:10:58.740
do a little bit of digging on our

201
00:10:58.740 --> 00:10:59.060
own.

202
00:10:59.360 --> 00:11:02.920
So let's go ahead and take this one.

203
00:11:03.560 --> 00:11:04.840
So I'm just going to come back into

204
00:11:04.840 --> 00:11:17.810
postman, add request, and

205
00:11:17.810 --> 00:11:24.070
then let's call this create recipe.

206
00:11:24.970 --> 00:11:28.250
It's going to be a post, and luckily

207
00:11:28.250 --> 00:11:31.490
they actually gave us some data to work

208
00:11:31.490 --> 00:11:31.870
with.

209
00:11:32.170 --> 00:11:34.430
So I'm just going to copy this, the

210
00:11:34.430 --> 00:11:39.230
pasta carbonara, drop this into the body, raw,

211
00:11:40.270 --> 00:11:41.010
json.

212
00:11:42.570 --> 00:11:46.030
Let's do this, and I suspect we need

213
00:11:46.030 --> 00:11:49.890
our session id as well, so let's grab

214
00:11:49.890 --> 00:11:50.330
that.

215
00:11:52.540 --> 00:11:53.860
Ah, we need to check what our most

216
00:11:53.860 --> 00:11:57.920
recent session id is because we've been fuzzing,

217
00:11:57.920 --> 00:12:04.820
so let's just do the login, send, got

218
00:12:04.820 --> 00:12:14.820
this session id, let's just replace these, hit

219
00:12:14.820 --> 00:12:26.060
send, and we get recipe created successfully, which

220
00:12:26.060 --> 00:12:26.620
is great.

221
00:12:27.000 --> 00:12:35.980
OK, so our next endpoint is puts.

222
00:12:37.580 --> 00:12:40.700
So we need a recipe id, so this

223
00:12:40.700 --> 00:12:44.460
is a good time to grab this id

224
00:12:44.460 --> 00:12:46.020
and store it for later.

225
00:12:53.450 --> 00:12:55.210
And is there any other information we want

226
00:12:55.210 --> 00:12:56.670
to grab out of here?

227
00:12:59.600 --> 00:13:00.920
No, I think we're all good.

228
00:13:01.540 --> 00:13:11.600
So let's create a new request, and

229
00:13:11.600 --> 00:13:37.420
this one is update recipe, and

230
00:13:37.420 --> 00:13:41.860
then we want the id, so let's give

231
00:13:41.860 --> 00:13:42.940
this a try.

232
00:13:44.780 --> 00:13:46.540
And actually, I think because we're updating, we

233
00:13:46.540 --> 00:13:49.620
probably need some data, so let's grab the

234
00:13:49.620 --> 00:14:01.950
data that they've provided us, and

235
00:14:01.950 --> 00:14:05.230
we'll also put in our session id as

236
00:14:05.230 --> 00:14:05.630
well.

237
00:14:12.320 --> 00:14:14.180
Recipe successfully updated.

238
00:14:16.080 --> 00:14:19.200
And interesting, something that also I've just spotted

239
00:14:19.200 --> 00:14:22.200
which I don't think was in, yeah, it

240
00:14:22.200 --> 00:14:25.140
wasn't in the recipe before, you see we

241
00:14:25.140 --> 00:14:29.300
have this original undefined, and here in the

242
00:14:29.300 --> 00:14:31.280
dev notes, we have a link to original

243
00:14:31.280 --> 00:14:31.840
recipes.

244
00:14:32.080 --> 00:14:33.800
This is probably something that we want to

245
00:14:33.800 --> 00:14:37.500
look at any time a payload or a

246
00:14:37.500 --> 00:14:40.900
URL is being asked for or passed in,

247
00:14:41.000 --> 00:14:43.020
we want to think about server-side request

248
00:14:43.020 --> 00:14:43.440
forgery.

249
00:14:43.600 --> 00:14:46.280
So we'll just think about this and put

250
00:14:46.280 --> 00:14:48.940
it in our notes to come back to

251
00:14:48.940 --> 00:14:49.320
later.

252
00:14:49.920 --> 00:14:51.160
So I'm just going to copy and paste

253
00:14:51.160 --> 00:15:00.810
this, and what I want to do now

254
00:15:00.810 --> 00:15:05.070
is just grab this, come to the search

255
00:15:05.070 --> 00:15:07.930
for recipes, hit send.

256
00:15:08.110 --> 00:15:12.600
Actually, I didn't even need the id, I

257
00:15:12.600 --> 00:15:15.240
just wanted to make sure that our new

258
00:15:15.240 --> 00:15:18.460
recipe was indeed here, and it looks like

259
00:15:18.460 --> 00:15:20.520
it's been added correctly, so we're all good

260
00:15:20.520 --> 00:15:21.060
basically.

261
00:15:21.760 --> 00:15:23.840
Always good to double check that it's doing

262
00:15:23.840 --> 00:15:25.260
what it says it's meant to be doing.

263
00:15:26.160 --> 00:15:28.900
So next up, let's keep going through these

264
00:15:28.900 --> 00:15:31.100
endpoints, and then we'll dive a little bit

265
00:15:31.100 --> 00:15:31.420
deeper.

266
00:15:31.800 --> 00:15:36.320
So we can add a request, v1 data

267
00:15:36.320 --> 00:15:40.760
title, so what is the description of this?

268
00:15:40.760 --> 00:15:42.360
Get a genius pasta pun.

269
00:15:43.000 --> 00:15:43.440
Nice.

270
00:15:44.800 --> 00:15:53.000
So get pun, and then so v1 data

271
00:15:53.000 --> 00:15:56.940
slash title, let's just send this.

272
00:15:58.280 --> 00:15:59.960
This too shall pasta.

273
00:16:01.000 --> 00:16:02.220
I'll send it again.

274
00:16:02.420 --> 00:16:03.060
Pasta la vista.

275
00:16:03.420 --> 00:16:05.400
Okay, so it seems like it gives us

276
00:16:05.400 --> 00:16:08.120
a random title each time, which is cool,

277
00:16:08.400 --> 00:16:12.540
and let's add the next request.

278
00:16:13.400 --> 00:16:16.200
So we have titles, so I think it

279
00:16:16.200 --> 00:16:18.540
looks like it's basically the same.

280
00:16:20.440 --> 00:16:24.620
Let's get all the puns.

281
00:16:27.780 --> 00:16:29.620
Yeah, indeed, we're correct.

282
00:16:29.740 --> 00:16:32.780
So it just returns all of them, which

283
00:16:32.780 --> 00:16:33.180
is great.

284
00:16:37.200 --> 00:16:39.920
All right, and the next one we have

285
00:16:39.920 --> 00:16:45.300
data internal action, so server maintenance only accessible

286
00:16:45.300 --> 00:16:45.840
locally.

287
00:16:46.500 --> 00:16:47.940
So again, this is kind of another red

288
00:16:47.940 --> 00:16:50.380
flag saying, hey, we should probably be checking

289
00:16:50.380 --> 00:16:54.300
for server-side request forgery, and if we

290
00:16:54.300 --> 00:17:00.980
compare this to the notes, we have v1

291
00:17:00.980 --> 00:17:02.740
data admin recipes.

292
00:17:04.780 --> 00:17:06.619
Ah, it is here.

293
00:17:06.839 --> 00:17:09.040
Sorry, I missed over this and skipped to

294
00:17:09.040 --> 00:17:10.720
the next one, and I was thinking that

295
00:17:10.720 --> 00:17:12.440
there was a discrepancy, but we're all good.

296
00:17:12.859 --> 00:17:14.280
So let's look at this one first.

297
00:17:14.720 --> 00:17:22.250
v1 data admin recipes, add request.

298
00:17:41.310 --> 00:17:42.590
So let's add this.

299
00:17:43.230 --> 00:17:46.890
We get unauthorized, and I think it looks

300
00:17:46.890 --> 00:17:55.520
like we need the session.

301
00:18:00.360 --> 00:18:01.560
Still unauthorized.

302
00:18:03.020 --> 00:18:04.920
Let's do one last check with a valid

303
00:18:04.920 --> 00:18:10.060
session id, and we're still unauthorized.

304
00:18:10.100 --> 00:18:12.300
So we might want to think about how

305
00:18:12.300 --> 00:18:15.420
can we create an invalid session id for

306
00:18:15.420 --> 00:18:17.340
the admin user, if we know what the

307
00:18:17.340 --> 00:18:20.560
admin user username is, because the first part

308
00:18:20.560 --> 00:18:23.800
of the session is the username, from what

309
00:18:23.800 --> 00:18:24.320
we can tell.

310
00:18:24.980 --> 00:18:27.480
And then the second part is random characters,

311
00:18:27.680 --> 00:18:29.640
so this might be something that we want

312
00:18:29.640 --> 00:18:31.360
to try, or something that we want to

313
00:18:31.360 --> 00:18:31.940
come back to.

314
00:18:34.940 --> 00:18:36.840
All right, so next up we have the

315
00:18:36.840 --> 00:18:43.320
v1 data internal action, and if we look

316
00:18:43.320 --> 00:18:46.320
at the sample request, we have slash uptime.

317
00:18:46.860 --> 00:18:48.500
So let's take a look at that.

318
00:18:49.060 --> 00:18:51.920
Interesting though, this is a variable, so it

319
00:18:51.920 --> 00:18:54.220
might be that there's more actions available.

320
00:18:54.560 --> 00:18:57.300
So this means, again, we probably want to

321
00:18:57.300 --> 00:18:58.200
think about fuzzing.

322
00:19:01.920 --> 00:19:11.350
So add request uptime, and then we're going

323
00:19:11.350 --> 00:19:22.690
to call this internal uptime, and

324
00:19:22.690 --> 00:19:25.430
we get, sorry, for security, this endpoint is

325
00:19:25.430 --> 00:19:28.030
only accessible locally.

326
00:19:28.370 --> 00:19:30.270
So yeah, seems like we're going to need

327
00:19:30.270 --> 00:19:33.090
to find a way around that and request

328
00:19:33.090 --> 00:19:34.750
it from another place.

329
00:19:39.560 --> 00:19:42.360
So generally speaking, this is kind of how

330
00:19:42.360 --> 00:19:43.620
I approach an application.

331
00:19:43.960 --> 00:19:47.060
I'll test each endpoint individually, get a feel

332
00:19:47.060 --> 00:19:49.700
for what it does, and then kind of

333
00:19:49.700 --> 00:19:52.120
form some thoughts or some ideas of where

334
00:19:52.120 --> 00:19:54.020
to go next, and then go next.

335
00:19:54.540 --> 00:19:56.380
Now this is a little bit different to,

336
00:19:56.720 --> 00:20:00.740
like, a vulnerability assessment situation, where you'll have

337
00:20:00.740 --> 00:20:03.260
a checklist or a number of things that

338
00:20:03.260 --> 00:20:04.080
you want to test.

339
00:20:04.300 --> 00:20:06.760
This approach is more like looking for critical

340
00:20:06.760 --> 00:20:09.700
vulnerabilities, but of course, in the real world,

341
00:20:09.720 --> 00:20:12.840
when you're attacking an application, you want to

342
00:20:12.840 --> 00:20:14.660
go through, you need to test the authentication,

343
00:20:15.320 --> 00:20:17.900
authorization, and everything else.

344
00:20:18.240 --> 00:20:20.480
But hopefully this gives you an idea of

345
00:20:20.480 --> 00:20:22.360
how I like to step through an application

346
00:20:22.360 --> 00:20:25.060
and really get to understand it, to find

347
00:20:25.060 --> 00:20:28.380
vulnerabilities that are not obvious to begin with,

348
00:20:28.400 --> 00:20:31.160
but usually quite critical later on.

349
00:20:32.300 --> 00:20:34.380
A couple of things that I thought about

350
00:20:34.380 --> 00:20:36.760
so far is that there seems to be

351
00:20:36.760 --> 00:20:39.480
no brute force protection, so collecting the session

352
00:20:39.480 --> 00:20:40.840
tokens was very easy.

353
00:20:41.020 --> 00:20:43.200
We haven't seen any cross-site request forgery

354
00:20:43.200 --> 00:20:46.260
tokens at all, and the session token looks

355
00:20:46.260 --> 00:20:48.500
very weak, so these are all findings that

356
00:20:48.500 --> 00:20:50.920
I would definitely put into my report so

357
00:20:50.920 --> 00:20:51.200
far.

358
00:20:56.330 --> 00:20:58.430
So the next thing I want to test

359
00:20:58.430 --> 00:21:03.310
is this internal endpoint, because I'm not convinced

360
00:21:03.310 --> 00:21:07.150
that this is the only endpoint that might

361
00:21:07.150 --> 00:21:09.690
be available, and there might be other internal

362
00:21:09.690 --> 00:21:13.690
endpoints that are not properly configured, and we

363
00:21:13.690 --> 00:21:15.370
might be able to get to some things.

364
00:21:15.570 --> 00:21:22.700
So I'm just going to grab this URL.

365
00:21:23.100 --> 00:21:24.620
In fact, we can just make a quick

366
00:21:24.620 --> 00:21:27.160
request to it, and we get the sorry

367
00:21:27.160 --> 00:21:30.920
message, and then we can come to perp

368
00:21:30.920 --> 00:21:35.540
suite proxy HTTP history and send this to

369
00:21:35.540 --> 00:21:36.600
the intruder.

370
00:21:39.440 --> 00:21:43.340
And I'm just going to add the selection

371
00:21:43.340 --> 00:21:48.460
here, come to payloads, and we'll just use..

372
00:21:48.460 --> 00:21:50.500
I think derp should be good, and then

373
00:21:50.500 --> 00:21:52.060
we use the big one since we're working

374
00:21:52.060 --> 00:21:52.520
locally.

375
00:21:52.780 --> 00:21:54.000
Should be fairly fast.

376
00:21:57.230 --> 00:21:58.890
Nothing too fancy at this point.

377
00:22:02.660 --> 00:22:07.000
All right, so we have this 401, and

378
00:22:07.000 --> 00:22:11.260
we get the response saying sorry, and this

379
00:22:11.260 --> 00:22:13.540
was our original request, so we're expecting that.

380
00:22:14.120 --> 00:22:16.240
And if we filter by our status codes,

381
00:22:16.300 --> 00:22:18.840
or order by the status codes, we also

382
00:22:18.840 --> 00:22:21.800
see a user's endpoint with 401.

383
00:22:22.080 --> 00:22:25.360
But unfortunately, we get the same message back,

384
00:22:25.480 --> 00:22:26.860
so it does look like we're going to

385
00:22:26.860 --> 00:22:29.680
have to go hunting for SSRF to be

386
00:22:29.680 --> 00:22:30.760
able to get to this.

387
00:22:31.240 --> 00:22:34.140
But uptime and users both sound quite dangerous.

388
00:22:34.340 --> 00:22:38.000
Uptime sounding like it returns the response of

389
00:22:38.000 --> 00:22:40.820
a command that's getting the uptime of the

390
00:22:40.820 --> 00:22:43.520
server, so we might think about command injection

391
00:22:43.520 --> 00:22:46.420
here, and the users, this might give us

392
00:22:46.420 --> 00:22:48.820
some sensitive information as well.

393
00:22:49.040 --> 00:22:52.040
So definitely worth looking at.

394
00:22:55.340 --> 00:22:57.060
So I'm going to come back to postman,

395
00:22:57.460 --> 00:23:01.020
and we're going to come to this here,

396
00:23:01.220 --> 00:23:02.540
and you can see it says get.

397
00:23:02.620 --> 00:23:04.740
I think if we save this, it should,

398
00:23:04.880 --> 00:23:06.280
yeah, there we go, yeah, updates.

399
00:23:06.480 --> 00:23:13.110
It doesn't save the post type automatically, so

400
00:23:13.110 --> 00:23:15.550
let's just go through and save these all

401
00:23:15.550 --> 00:23:16.070
quickly.

402
00:23:18.090 --> 00:23:21.830
And what I want to do is, we

403
00:23:21.830 --> 00:23:24.690
have this recipe, and we have this link

404
00:23:24.690 --> 00:23:27.030
to original recipe, so let's just test this

405
00:23:27.030 --> 00:23:27.370
quickly.

406
00:23:33.090 --> 00:23:36.930
https://www.google.com, and let's see what happens.

407
00:23:37.330 --> 00:23:40.450
So we get recipe successfully updated, so it

408
00:23:40.450 --> 00:23:45.370
was okay with it, and then we can't

409
00:23:45.370 --> 00:23:48.090
see the recipe id, but we know that

410
00:23:48.090 --> 00:23:59.810
we can search for all the recipes, and

411
00:23:59.810 --> 00:24:01.650
it doesn't look like it comes back with

412
00:24:01.650 --> 00:24:03.010
anything interesting.

413
00:24:03.010 --> 00:24:05.490
So I think we need to find an

414
00:24:05.490 --> 00:24:09.490
endpoint that is making use of this link,

415
00:24:09.730 --> 00:24:11.930
rather than just returning it.

416
00:24:17.360 --> 00:24:19.640
So let's go back and see if we

417
00:24:19.640 --> 00:24:20.520
missed anything.

418
00:24:24.340 --> 00:24:26.240
All right, sorry about that.

419
00:24:26.420 --> 00:24:29.460
So basically I spent about 30 minutes trying

420
00:24:29.460 --> 00:24:30.820
to figure out what was going on.

421
00:24:31.360 --> 00:24:33.620
It seems like the old swagger file had

422
00:24:33.620 --> 00:24:37.140
cached to my browser history, and it wasn't

423
00:24:37.140 --> 00:24:39.700
displaying the new one, but obviously you doing

424
00:24:39.700 --> 00:24:42.200
this lab, you'll have the up-to-date

425
00:24:42.200 --> 00:24:44.000
and working code.

426
00:24:44.380 --> 00:24:48.000
So we did miss out an endpoint as

427
00:24:48.000 --> 00:24:51.860
we were going through, and this one is,

428
00:24:51.940 --> 00:24:53.700
I'm just going to add it in here,

429
00:24:53.860 --> 00:25:02.310
add request, and then we're going to call

430
00:25:02.310 --> 00:25:14.170
it getRecipe, and

431
00:25:14.170 --> 00:25:21.460
this is going to be v1 recipes, and

432
00:25:21.460 --> 00:25:25.160
then an id, and as you can see

433
00:25:25.160 --> 00:25:26.260
I've already tested that.

434
00:25:26.500 --> 00:25:28.620
So here what I'm going to do is

435
00:25:28.620 --> 00:25:33.540
I'm going to grab, oops where's my mouse

436
00:25:33.540 --> 00:25:39.360
pad gone, ah it's changed windows, the recipe

437
00:25:39.360 --> 00:25:43.280
id from here, come back, paste this in,

438
00:25:43.560 --> 00:25:45.740
and send this away.

439
00:25:46.220 --> 00:25:48.220
And as you can see it comes back

440
00:25:48.220 --> 00:25:51.360
with our pasta carbonara, and this is the

441
00:25:51.360 --> 00:25:54.360
one that we changed our original link to,

442
00:25:54.820 --> 00:25:57.280
and you can see that what it does

443
00:25:57.280 --> 00:25:59.340
is it goes out to this link and

444
00:25:59.340 --> 00:26:01.400
then calls this the original recipe.

445
00:26:01.780 --> 00:26:04.920
So the intended functionality here is to link

446
00:26:04.920 --> 00:26:07.200
to other recipes, so if you had a

447
00:26:07.200 --> 00:26:10.360
pasta carbonara recipe that was a variation of

448
00:26:10.360 --> 00:26:12.560
another one, you could then put the old

449
00:26:12.560 --> 00:26:14.600
one or the original one, or the link

450
00:26:14.600 --> 00:26:16.240
to the original one, here.

451
00:26:16.480 --> 00:26:18.840
But in this case we easily get server

452
00:26:18.840 --> 00:26:20.540
-side request forgery.

453
00:26:21.120 --> 00:26:25.540
So let's test this against our uptime endpoint.

454
00:26:25.800 --> 00:26:28.960
So I'm just going to come here, copy

455
00:26:28.960 --> 00:26:38.450
this, come back to puts, update recipe, paste

456
00:26:38.450 --> 00:26:42.670
this in here, hit send, and then come

457
00:26:42.670 --> 00:26:46.550
back to get recipe, and we get a

458
00:26:46.550 --> 00:26:48.910
uptime back, which is great.

459
00:26:49.130 --> 00:26:51.430
So now in our report that we we

460
00:26:51.430 --> 00:26:54.850
can say that we can access internal services

461
00:26:54.850 --> 00:26:59.410
via the application, which is a critical finding.

462
00:27:00.010 --> 00:27:02.970
And something that's even more exciting is if

463
00:27:02.970 --> 00:27:06.430
we go back and recall that we found

464
00:27:06.430 --> 00:27:08.170
the user's endpoints.

465
00:27:08.370 --> 00:27:11.670
If you recall, we actually fuzzed the internal

466
00:27:11.670 --> 00:27:14.770
endpoints and found users, and if we add

467
00:27:14.770 --> 00:27:19.950
this in here, click send, recipe successfully updated,

468
00:27:20.430 --> 00:27:22.770
and then come back and get the recipe,

469
00:27:23.410 --> 00:27:26.610
we can list the users in the application.

470
00:27:27.250 --> 00:27:29.850
So this is quite interesting to see.

471
00:27:30.390 --> 00:27:32.290
And you can see a couple of users

472
00:27:32.290 --> 00:27:34.830
that looks like they were added, so test,

473
00:27:35.150 --> 00:27:37.430
and then test2, which we added.

474
00:27:37.750 --> 00:27:39.670
And there is an admin user as well,

475
00:27:39.730 --> 00:27:43.630
although the password is not hashed, and I

476
00:27:43.630 --> 00:27:46.470
suspect this is because this is added by

477
00:27:46.470 --> 00:27:49.170
the reset script, and the reset script probably

478
00:27:49.170 --> 00:27:52.450
just inserts it directly into the database rather

479
00:27:52.450 --> 00:27:55.310
than going through the registration endpoints.

480
00:27:55.450 --> 00:27:58.110
Now there's something else that's really interesting about

481
00:27:58.110 --> 00:28:00.790
this finding, even though this is obviously a

482
00:28:00.790 --> 00:28:03.950
critical issue and something that should be at

483
00:28:03.950 --> 00:28:05.790
the very front of our reports.

484
00:28:06.510 --> 00:28:10.570
We also see this user level parameter.

485
00:28:11.190 --> 00:28:13.330
So if we think back to one of

486
00:28:13.330 --> 00:28:17.370
our previous labs, when we create a user,

487
00:28:17.590 --> 00:28:20.050
we were able to pass in extra parameter

488
00:28:20.050 --> 00:28:22.950
values to set things for that user object.

489
00:28:23.190 --> 00:28:24.350
So let's give this a try.

490
00:28:24.430 --> 00:28:26.890
Let's create a new user and see whether,

491
00:28:27.630 --> 00:28:30.050
instead of what seems to be the default

492
00:28:30.050 --> 00:28:33.310
user level user, we can actually make it

493
00:28:33.310 --> 00:28:33.990
admin.

494
00:28:36.760 --> 00:28:38.860
And in turn, hopefully that will let us

495
00:28:38.860 --> 00:28:40.880
access the admin endpoints.

496
00:28:41.340 --> 00:28:46.420
So I'll come back to register, and I'm

497
00:28:46.420 --> 00:28:48.520
going to create a user.

498
00:28:49.120 --> 00:28:58.200
Let's just create one called Alex, and I

499
00:28:58.200 --> 00:29:00.620
think it was user level, if I recall.

500
00:29:06.510 --> 00:29:09.750
Hit send, and we get a registration successful.

501
00:29:10.650 --> 00:29:12.270
And what we want to do is we

502
00:29:12.270 --> 00:29:13.670
want to copy this session ID.

503
00:29:15.030 --> 00:29:17.550
So let's just add this to our notes,

504
00:29:18.330 --> 00:29:21.670
and we can probably verify this actually just

505
00:29:21.670 --> 00:29:24.090
by going to the get recipe, clicking send

506
00:29:24.090 --> 00:29:26.010
again, and seeing what's happened.

507
00:29:26.890 --> 00:29:28.650
And we can indeed see that we have

508
00:29:28.650 --> 00:29:31.470
the username Alex, and we have the user

509
00:29:31.470 --> 00:29:34.310
level admin, which is quite cool.

510
00:29:34.810 --> 00:29:38.570
And when we do the get recipes, here

511
00:29:38.570 --> 00:29:40.010
we had unauthorized.

512
00:29:40.770 --> 00:29:45.030
We can paste this in, and we do

513
00:29:45.030 --> 00:29:47.910
indeed list all of the recipes.

514
00:29:49.370 --> 00:29:52.210
And so that's it for the major vulnerabilities

515
00:29:52.210 --> 00:29:54.290
within this application.

516
00:29:54.870 --> 00:29:57.850
Now there are other smaller issues to uncover,

517
00:29:58.050 --> 00:29:58.790
of course, so


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:02.700
(Transcribed by TurboScribe. Go Unlimited to remove this message.) So that's it, and once again I just

2
00:00:02.700 --> 00:00:04.440
want to say how much I appreciate you

3
00:00:04.440 --> 00:00:06.700
going through this course and sticking with it

4
00:00:06.700 --> 00:00:07.320
to the end.

5
00:00:07.500 --> 00:00:09.000
It really means the world to me that

6
00:00:09.000 --> 00:00:11.640
I can share my passion with application security

7
00:00:11.640 --> 00:00:12.500
with you.

8
00:00:13.180 --> 00:00:15.379
Now, don't be a stranger, feel free to

9
00:00:15.379 --> 00:00:17.480
reach out and connect on LinkedIn or drop

10
00:00:17.480 --> 00:00:19.780
into the TCM Discord, and if you ever

11
00:00:19.780 --> 00:00:21.420
bump into me at a conference or a

12
00:00:21.420 --> 00:00:23.500
meetup, don't hesitate to say hello.

13
00:00:23.960 --> 00:00:25.820
Good luck with everything in the future, and

14
00:00:25.820 --> 00:00:27.560
until next time, all the best.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================
