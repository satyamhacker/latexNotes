# Section 2: Penteration-Testing-Process

WEBVTT

1
00:00:00.140 --> 00:00:03.240
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk about the penetration testing process.

2
00:00:03.580 --> 00:00:05.900
So if you've never done a penetration testing

3
00:00:05.900 --> 00:00:08.700
course before, you'll have an understanding of the

4
00:00:08.700 --> 00:00:11.520
overall pen testing process and how it can

5
00:00:11.520 --> 00:00:14.520
actually fit in alongside the mobile pen testing

6
00:00:14.520 --> 00:00:15.840
process as well.

7
00:00:16.740 --> 00:00:19.840
So this is our penetration testing process, and

8
00:00:19.840 --> 00:00:22.060
it comes in six basic steps.

9
00:00:22.340 --> 00:00:24.960
We have our reconnaissance, which comes in two

10
00:00:24.960 --> 00:00:27.220
different flavors, active or passive.

11
00:00:27.220 --> 00:00:31.340
We have our scanning and enumeration phase, exploitation,

12
00:00:31.880 --> 00:00:36.200
privilege escalation, or also maintaining access, covering our

13
00:00:36.200 --> 00:00:38.400
tracks, and then finally reporting.

14
00:00:39.960 --> 00:00:44.000
So getting into the actual process, reconnaissance is

15
00:00:44.000 --> 00:00:47.500
basically gathering information about your target.

16
00:00:47.920 --> 00:00:50.300
So let's say, for example, that you're targeting

17
00:00:50.300 --> 00:00:51.500
some kind of a company.

18
00:00:52.020 --> 00:00:53.820
Let's say Uber, for example.

19
00:00:53.820 --> 00:00:56.840
We want to use a variety of sources

20
00:00:56.840 --> 00:00:59.640
to gain as much information about our target

21
00:00:59.640 --> 00:01:00.500
as possible.

22
00:01:01.200 --> 00:01:03.500
So we're going to use two different techniques

23
00:01:03.500 --> 00:01:04.580
for reconnaissance.

24
00:01:04.720 --> 00:01:07.660
We have active reconnaissance and our passive reconnaissance.

25
00:01:08.480 --> 00:01:11.220
Passive reconnaissance, you can basically think about this

26
00:01:11.220 --> 00:01:14.680
as gathering any information that is publicly available

27
00:01:14.680 --> 00:01:15.700
about your target.

28
00:01:16.180 --> 00:01:19.360
This can include using things like LinkedIn to

29
00:01:19.360 --> 00:01:21.580
do some enumeration about who might work for

30
00:01:21.580 --> 00:01:24.160
the company, using things like Google to do

31
00:01:24.160 --> 00:01:27.260
some basic research about the company, its goals,

32
00:01:27.740 --> 00:01:29.700
its executive board, things like that.

33
00:01:30.080 --> 00:01:33.420
Also, using things like earnings reports, news releases,

34
00:01:33.640 --> 00:01:36.000
or anything like that would be also considered

35
00:01:36.000 --> 00:01:37.300
passive reconnaissance.

36
00:01:38.020 --> 00:01:40.700
Now, active reconnaissance, you can think of this

37
00:01:40.700 --> 00:01:43.900
as putting your hands on some portion of

38
00:01:43.900 --> 00:01:46.320
the target, but you're not quite doing scanning

39
00:01:46.320 --> 00:01:47.560
or enumeration yet.

40
00:01:48.080 --> 00:01:51.400
So active reconnaissance could include things such as

41
00:01:51.400 --> 00:01:52.680
physical reconnaissance.

42
00:01:53.180 --> 00:01:55.060
Maybe you're going to the building, looking at

43
00:01:55.060 --> 00:01:58.240
the entrances, observing the people coming in, finding

44
00:01:58.240 --> 00:01:59.660
out where badge scanners are.

45
00:02:00.000 --> 00:02:03.100
Anything like that could be considered active reconnaissance.

46
00:02:03.520 --> 00:02:06.100
Also, if you're doing something like interacting with

47
00:02:06.100 --> 00:02:09.440
targets via social engineering, maybe you're connecting with

48
00:02:09.440 --> 00:02:12.300
someone on LinkedIn and asking them about a

49
00:02:12.300 --> 00:02:14.520
job posting that you found through your passive

50
00:02:14.520 --> 00:02:16.040
reconnaissance techniques, right?

51
00:02:16.040 --> 00:02:18.800
This would be a form of active reconnaissance

52
00:02:18.800 --> 00:02:22.380
to continue gathering some more information about our

53
00:02:22.380 --> 00:02:22.740
target.

54
00:02:23.300 --> 00:02:25.900
Now, remember that reconnaissance is actually like the

55
00:02:25.900 --> 00:02:29.780
most important aspect of penetration testing, because if

56
00:02:29.780 --> 00:02:32.060
you do not do a good job of

57
00:02:32.060 --> 00:02:34.520
your reconnaissance, then you're never going to be

58
00:02:34.520 --> 00:02:37.000
able to go further against the company.

59
00:02:37.640 --> 00:02:41.080
Your reconnaissance is only as good as the

60
00:02:41.080 --> 00:02:43.300
effort that you put in, and what comes

61
00:02:43.300 --> 00:02:46.000
out of the reconnaissance feeds into the rest

62
00:02:46.000 --> 00:02:46.660
of the process.

63
00:02:46.920 --> 00:02:47.940
So you want to make sure that you're

64
00:02:47.940 --> 00:02:50.680
doing a good job on the reconnaissance step.

65
00:02:51.260 --> 00:02:53.760
Now, the scanning and enumeration portion of the

66
00:02:53.760 --> 00:02:56.120
pen testing process is when we're actually using

67
00:02:56.120 --> 00:02:59.540
tools that can touch the target's physical or

68
00:02:59.540 --> 00:03:03.940
digital infrastructure to enumerate a vulnerability or things

69
00:03:03.940 --> 00:03:05.580
like open ports, for example.

70
00:03:06.080 --> 00:03:08.540
So common tools here in a pen tester's

71
00:03:08.540 --> 00:03:10.740
toolbox are tools like NMAP.

72
00:03:10.740 --> 00:03:13.440
What NMAP does is it allows us to

73
00:03:13.440 --> 00:03:16.060
enumerate the ports and services that are running

74
00:03:16.060 --> 00:03:18.480
on our target infrastructure.

75
00:03:18.780 --> 00:03:21.240
So for example, if the target has a

76
00:03:21.240 --> 00:03:23.140
web server out there or any kind of

77
00:03:23.140 --> 00:03:25.500
server that is exposed, we can go out

78
00:03:25.500 --> 00:03:27.940
there and use NMAP to discover what is

79
00:03:27.940 --> 00:03:28.300
running.

80
00:03:28.480 --> 00:03:32.280
Things like SSH, web servers, any variety of

81
00:03:32.280 --> 00:03:35.400
services we can actually enumerate by using NMAP.

82
00:03:36.200 --> 00:03:39.160
We can also use tools like DuraBee and

83
00:03:39.160 --> 00:03:42.960
Nikto to understand some information about a web

84
00:03:42.960 --> 00:03:48.840
application's underlying directories or also its underlying technology.

85
00:03:49.400 --> 00:03:51.120
So if we ran into a web application

86
00:03:51.120 --> 00:03:52.680
out there in the wild, we want to

87
00:03:52.680 --> 00:03:55.720
understand how that web application is coded, what

88
00:03:55.720 --> 00:03:57.980
kind of libraries it's using, and what kind

89
00:03:57.980 --> 00:04:00.820
of directories are available for us to use.

90
00:04:01.180 --> 00:04:03.680
Now, if we're talking about a physical enumeration,

91
00:04:04.180 --> 00:04:07.040
this could obviously be doing things like, you

92
00:04:07.040 --> 00:04:08.620
could think about this as trying to open

93
00:04:08.620 --> 00:04:12.420
the door or trying to use a falsified

94
00:04:12.420 --> 00:04:14.620
badge or anything like that that might touch

95
00:04:14.620 --> 00:04:16.820
the target's physical infrastructure.

96
00:04:19.320 --> 00:04:20.620
Now, it comes to exploitation.

97
00:04:21.180 --> 00:04:23.200
This is what most people believe that a

98
00:04:23.200 --> 00:04:26.580
pentester or a hacker does all day, right?

99
00:04:26.980 --> 00:04:29.900
But the exploitation is only taking advantage of

100
00:04:29.900 --> 00:04:32.560
the vulnerabilities that you discovered through your enumeration

101
00:04:32.560 --> 00:04:33.980
and reconnaissance, right?

102
00:04:34.260 --> 00:04:35.800
So if we're not doing a good job

103
00:04:35.800 --> 00:04:38.640
on our reconnaissance and enumeration phases, we might

104
00:04:38.640 --> 00:04:41.140
never even get to this exploitation stage.

105
00:04:41.240 --> 00:04:42.900
There's a lot of work that needs to

106
00:04:42.900 --> 00:04:45.680
go on before we can even reach exploitation.

107
00:04:46.280 --> 00:04:48.880
But just think of exploitation as we're actually

108
00:04:48.880 --> 00:04:50.600
taking advantage of the vulnerability.

109
00:04:51.140 --> 00:04:53.080
We're getting in the building, we're getting into

110
00:04:53.080 --> 00:04:55.740
the system, or we found some type of

111
00:04:55.740 --> 00:04:58.000
vulnerability in a web application that lets us

112
00:04:58.000 --> 00:04:59.120
do something malicious.

113
00:05:00.080 --> 00:05:03.040
Now, once we've done our exploitation, next we

114
00:05:03.040 --> 00:05:05.880
want to do something called privilege escalation.

115
00:05:05.880 --> 00:05:08.320
This is once we're inside of the system

116
00:05:08.320 --> 00:05:10.700
or the environment, we want to move in

117
00:05:10.700 --> 00:05:11.640
two different directions.

118
00:05:11.860 --> 00:05:13.840
We either want to move laterally, or we

119
00:05:13.840 --> 00:05:16.880
want to move vertically to gain more information

120
00:05:16.880 --> 00:05:18.940
about the system or move to a different

121
00:05:18.940 --> 00:05:19.760
user account.

122
00:05:20.600 --> 00:05:23.380
So a lateral privilege escalation would be moving

123
00:05:23.380 --> 00:05:26.120
from a device or a web application to

124
00:05:26.120 --> 00:05:28.920
another device or a web application as the

125
00:05:28.920 --> 00:05:32.480
same user or as a same privileged user.

126
00:05:32.480 --> 00:05:34.960
So for example, here, maybe we get into

127
00:05:34.960 --> 00:05:37.260
the organization as a low-level user.

128
00:05:37.580 --> 00:05:40.040
We want to move to a different device

129
00:05:40.040 --> 00:05:42.440
with the same username and password, or maybe

130
00:05:42.440 --> 00:05:45.540
another username and password that we discovered after

131
00:05:45.540 --> 00:05:47.040
we got onto that device.

132
00:05:48.080 --> 00:05:51.560
Next, we want to do vertical privilege escalation.

133
00:05:51.980 --> 00:05:53.520
And this is when we're moving from a

134
00:05:53.520 --> 00:05:55.940
low-level user account to a higher-level

135
00:05:55.940 --> 00:05:56.660
user account.

136
00:05:56.780 --> 00:05:58.220
So you can think of this as like,

137
00:05:58.640 --> 00:06:00.080
you know, going from a low-level user

138
00:06:00.080 --> 00:06:02.500
to the admin of the system or to

139
00:06:02.500 --> 00:06:04.520
a domain admin within the domain.

140
00:06:05.260 --> 00:06:07.160
So that is what privilege escalation is all

141
00:06:07.160 --> 00:06:07.480
about.

142
00:06:08.360 --> 00:06:11.220
And then what we don't usually do as

143
00:06:11.220 --> 00:06:13.740
a pen tester is this covering your tracks

144
00:06:13.740 --> 00:06:15.500
portion, but this is still part of the

145
00:06:15.500 --> 00:06:16.440
process technically.

146
00:06:16.900 --> 00:06:18.620
And this is when we're going out there

147
00:06:18.620 --> 00:06:21.460
and eliminating evidence that might incriminate you or

148
00:06:21.460 --> 00:06:23.200
leave signs of exploitation.

149
00:06:23.780 --> 00:06:25.500
So you can think of this as things

150
00:06:25.500 --> 00:06:27.880
like changing timestamps or if you have access

151
00:06:27.880 --> 00:06:30.180
to a physical system, maybe you're going to

152
00:06:30.180 --> 00:06:32.140
erase that video footage so they would never

153
00:06:32.140 --> 00:06:33.200
know that you were there.

154
00:06:33.680 --> 00:06:35.340
Now as pen testers, we usually do not

155
00:06:35.340 --> 00:06:37.480
do that because we want to leave evidence

156
00:06:37.480 --> 00:06:39.400
that we were there to see if people

157
00:06:39.400 --> 00:06:40.220
picked up on it.

158
00:06:40.580 --> 00:06:42.480
And also we want to leave the evidence

159
00:06:42.480 --> 00:06:44.700
there to say, hey, we were here at

160
00:06:44.700 --> 00:06:46.440
this time and you can go ahead and

161
00:06:46.440 --> 00:06:47.280
confirm it, right?

162
00:06:47.840 --> 00:06:50.080
And so we don't usually get a chance

163
00:06:50.080 --> 00:06:52.280
to cover our tracks as pen testers, but

164
00:06:52.280 --> 00:06:54.080
it is something that you should still know

165
00:06:54.900 --> 00:06:57.140
whenever you're doing an assessment if you want

166
00:06:57.140 --> 00:06:58.080
to be stealthy.

167
00:06:59.120 --> 00:07:01.680
Now, the final part of the pen testing

168
00:07:01.680 --> 00:07:03.360
process is reporting.

169
00:07:03.820 --> 00:07:05.620
And this is where we have the result

170
00:07:05.620 --> 00:07:06.920
of all of your hard work.

171
00:07:07.180 --> 00:07:09.240
And we're going to outline the vulnerabilities we

172
00:07:09.240 --> 00:07:12.560
discovered, how we exploited them, and most importantly,

173
00:07:12.740 --> 00:07:14.860
how the company can actually fix them.

174
00:07:15.200 --> 00:07:18.440
Remember that reporting and doing a good job

175
00:07:18.440 --> 00:07:21.160
on your report is exactly what separates an

176
00:07:21.160 --> 00:07:23.800
ethical hacker from the bad guys, right?

177
00:07:23.940 --> 00:07:26.360
Because we want to be the good guys

178
00:07:26.360 --> 00:07:27.040
for the system.

179
00:07:27.040 --> 00:07:28.740
We want to go in, we want to

180
00:07:28.740 --> 00:07:30.580
find the vulnerabilities, and we want to tell

181
00:07:30.580 --> 00:07:32.060
the business how to fix it.

182
00:07:32.480 --> 00:07:34.740
We also want to tell the business about

183
00:07:34.740 --> 00:07:37.140
the impact so that they can prioritize the

184
00:07:37.140 --> 00:07:39.380
findings and fix the things that are most

185
00:07:39.380 --> 00:07:40.260
critical first.

186
00:07:40.660 --> 00:07:42.200
So make sure you're keeping that in mind

187
00:07:42.200 --> 00:07:44.340
when we're talking about the reporting phase as

188
00:07:44.340 --> 00:07:44.680
well.

189
00:07:45.140 --> 00:07:46.940
We want to give them the highest criticality

190
00:07:46.940 --> 00:07:49.640
vulnerabilities to fix those first and tier the

191
00:07:49.640 --> 00:07:52.360
vulnerabilities so that, you know, the business knows

192
00:07:52.360 --> 00:07:55.020
exactly what order to go in and fix

193
00:07:55.020 --> 00:07:56.060
all the issues.

194
00:07:56.060 --> 00:07:58.720
Reporting is what separates us from the bad

195
00:07:58.720 --> 00:08:01.200
guys, and that's when we're giving the business

196
00:08:01.200 --> 00:08:03.480
everything that we found and helping them to

197
00:08:03.480 --> 00:08:05.120
fix their security posture.

198
00:08:05.620 --> 00:08:07.440
That's all I have for the pen testing

199
00:08:07.440 --> 00:08:08.600
process in a nutshell.

200
00:08:09.160 --> 00:08:11.100
Let's move over now to the mobile pen

201
00:08:11.100 --> 00:08:13.820
testing process and see how that relates to

202
00:08:13.820 --> 00:08:15.980
this pen testing process as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.660 --> 00:00:02.740
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk now about the mobile pen

2
00:00:02.740 --> 00:00:03.700
testing process.

3
00:00:04.720 --> 00:00:07.200
You can see on this slide that debatably

4
00:00:07.200 --> 00:00:10.240
this process is quite a bit more simple

5
00:00:10.240 --> 00:00:11.860
than the pen testing process.

6
00:00:12.400 --> 00:00:15.040
Here we only have four steps, and two

7
00:00:15.040 --> 00:00:17.400
of them are shared between the pen testing

8
00:00:17.400 --> 00:00:19.200
process and this process.

9
00:00:19.440 --> 00:00:21.540
So we have our reconnaissance, we have our

10
00:00:21.540 --> 00:00:25.320
static analysis, our dynamic analysis, and our reporting.

11
00:00:25.660 --> 00:00:29.320
The reconnaissance and reporting phases are shared between

12
00:00:29.320 --> 00:00:30.980
the pen testing process.

13
00:00:32.020 --> 00:00:34.100
Now let's talk about what we can do

14
00:00:34.100 --> 00:00:37.180
for reconnaissance when we come to mobile applications.

15
00:00:37.880 --> 00:00:40.440
So first thing obviously is just finding some

16
00:00:40.440 --> 00:00:42.520
general information about the company.

17
00:00:43.080 --> 00:00:45.600
Now good places to look for information about

18
00:00:45.600 --> 00:00:48.960
mobile applications is the earnings reports and also

19
00:00:48.960 --> 00:00:50.960
the press releases for the company.

20
00:00:51.240 --> 00:00:54.860
So earnings reports, they're often taking into those

21
00:00:54.860 --> 00:00:58.340
reports some information about increases of sales on

22
00:00:58.340 --> 00:01:02.020
mobile applications, and also press releases are obviously

23
00:01:02.020 --> 00:01:04.019
a great source for this as well.

24
00:01:04.319 --> 00:01:06.940
For a lot of companies, a new mobile

25
00:01:06.940 --> 00:01:09.480
application means a new way to sell to

26
00:01:09.480 --> 00:01:11.940
clients or a new way for their customers

27
00:01:11.940 --> 00:01:13.500
to interact with the company.

28
00:01:14.000 --> 00:01:16.620
So mobile apps often make the news in

29
00:01:16.620 --> 00:01:19.660
press releases or news about the company generally

30
00:01:19.660 --> 00:01:20.180
speaking.

31
00:01:20.520 --> 00:01:22.800
So if you're doing information about a company,

32
00:01:23.240 --> 00:01:25.500
in this video we'll be doing Uber, you

33
00:01:25.500 --> 00:01:27.380
can always go out and try to find

34
00:01:27.380 --> 00:01:30.560
some information about their newest mobile app releases.

35
00:01:31.180 --> 00:01:32.780
So the next thing you're going to do

36
00:01:32.780 --> 00:01:35.360
as part of the reconnaissance phase is finding

37
00:01:35.360 --> 00:01:37.860
the target application out there on the Google

38
00:01:37.860 --> 00:01:39.700
Play Store and the Apple Store.

39
00:01:40.380 --> 00:01:42.140
Again in our case we'll be using the

40
00:01:42.140 --> 00:01:43.900
Uber apps, but I want you to go

41
00:01:43.900 --> 00:01:45.940
out there, I want you to actually read

42
00:01:45.940 --> 00:01:48.660
customer reviews because this can give you some

43
00:01:48.660 --> 00:01:51.460
information about common bugs that customers have been

44
00:01:51.460 --> 00:01:54.960
experiencing and possibly some issues that might become

45
00:01:54.960 --> 00:01:57.600
a bug for you as a bug bounty

46
00:01:57.600 --> 00:01:57.920
hunter.

47
00:01:58.520 --> 00:01:59.420
I want you to go out to the

48
00:01:59.420 --> 00:02:01.760
app store and try to enumerate who created

49
00:02:01.760 --> 00:02:05.000
the application, find a specific email address that

50
00:02:05.000 --> 00:02:07.580
you might be able to use, or find

51
00:02:07.580 --> 00:02:09.560
out who actually developed the application.

52
00:02:09.720 --> 00:02:12.180
There's usually a person at the company who

53
00:02:12.180 --> 00:02:15.480
is responsible for releasing that mobile application out

54
00:02:15.480 --> 00:02:16.560
into the Play Store.

55
00:02:17.220 --> 00:02:19.680
Next you're going to enumerate the different application

56
00:02:19.680 --> 00:02:21.280
versions and patch notes.

57
00:02:21.720 --> 00:02:24.780
So many companies are patching mobile applications on

58
00:02:24.780 --> 00:02:27.260
a regular basis, and on these Play Stores

59
00:02:27.260 --> 00:02:29.260
you can actually see things like the patch

60
00:02:29.260 --> 00:02:31.640
notes and the different times and days that

61
00:02:31.640 --> 00:02:33.680
they've released different application versions.

62
00:02:34.200 --> 00:02:36.380
So this will give you some information not

63
00:02:36.380 --> 00:02:38.980
only about the application and what's changed over

64
00:02:38.980 --> 00:02:42.280
time, but how often they're actually releasing changes

65
00:02:42.280 --> 00:02:43.520
to the mobile app.

66
00:02:43.520 --> 00:02:45.720
The other thing you're going to do out

67
00:02:45.720 --> 00:02:47.700
on the Play Stores is try to enumerate

68
00:02:47.700 --> 00:02:49.360
the company's other applications.

69
00:02:50.060 --> 00:02:52.620
Some companies have a lot of applications on

70
00:02:52.620 --> 00:02:54.380
Android, none on iOS.

71
00:02:54.900 --> 00:02:57.800
Some have a balance of both, some on

72
00:02:57.800 --> 00:02:59.020
iOS, some on Android.

73
00:02:59.440 --> 00:03:01.840
Some have one or two different on Android

74
00:03:01.840 --> 00:03:02.400
and iOS.

75
00:03:02.960 --> 00:03:05.640
So understanding the differences between the two different

76
00:03:05.640 --> 00:03:08.260
Play Stores can give you some information about

77
00:03:08.260 --> 00:03:11.240
what might be a new application or something

78
00:03:11.240 --> 00:03:13.940
not included for one reason or another on

79
00:03:13.940 --> 00:03:15.100
Android or iOS.

80
00:03:15.680 --> 00:03:17.580
So if it's a new application it's possible

81
00:03:17.580 --> 00:03:20.020
that it might actually have some additional bugs

82
00:03:20.020 --> 00:03:23.280
that the developer hasn't gotten around to yet,

83
00:03:23.380 --> 00:03:25.120
so it could give you some more opportunity

84
00:03:25.120 --> 00:03:27.900
in terms of attack surface as an attacker.

85
00:03:28.420 --> 00:03:30.600
So let's hop out now to the Google

86
00:03:30.600 --> 00:03:32.880
Play Store and the Apple Store and take

87
00:03:32.880 --> 00:03:34.720
a look at Uber's applications.

88
00:03:35.740 --> 00:03:37.680
So I'm just going to go to Google

89
00:03:37.680 --> 00:03:41.820
here and search for Uber Play Store, Google

90
00:03:41.820 --> 00:03:45.880
Play, like this, and I'm also going to

91
00:03:45.880 --> 00:03:47.520
go to the Apple Store.

92
00:03:47.640 --> 00:03:49.360
You can see it's here on the results

93
00:03:49.360 --> 00:03:49.620
here.

94
00:03:49.660 --> 00:03:50.940
I'm going to open a new tab for

95
00:03:50.940 --> 00:03:53.040
this, pull up the screen so that you

96
00:03:53.040 --> 00:03:55.380
guys can see, and go to the Play

97
00:03:55.380 --> 00:03:56.680
Store for the Uber app.

98
00:03:57.080 --> 00:03:59.540
So here you can see some basic information

99
00:03:59.540 --> 00:04:02.160
about the Uber app, so you have Uber

100
00:04:02.160 --> 00:04:03.440
request a ride here.

101
00:04:03.440 --> 00:04:05.820
Now if you wanted to enumerate the different

102
00:04:05.820 --> 00:04:09.020
applications that are available for the Uber company

103
00:04:09.020 --> 00:04:10.920
out there on the Play Store, you can

104
00:04:10.920 --> 00:04:12.980
just click the Uber Technologies, Inc.

105
00:04:13.460 --> 00:04:16.000
link here, and it will automatically show you

106
00:04:16.000 --> 00:04:18.279
all of their applications that they've made.

107
00:04:18.399 --> 00:04:19.560
I'm going to click see more here.

108
00:04:19.920 --> 00:04:21.860
You can see they have all these different

109
00:04:21.860 --> 00:04:25.480
types of Android applications, right, and each one

110
00:04:25.480 --> 00:04:28.380
could possibly be developed by a different development

111
00:04:28.380 --> 00:04:30.260
team inside of the company.

112
00:04:30.660 --> 00:04:33.800
So that could give you some information about,

113
00:04:34.000 --> 00:04:35.860
you know, the different developers that are out

114
00:04:35.860 --> 00:04:38.120
there, the different types of customers this company

115
00:04:38.120 --> 00:04:39.540
is trying to appeal to.

116
00:04:40.680 --> 00:04:42.860
You can also see the differences in terms

117
00:04:42.860 --> 00:04:45.160
of the reviews, so things with bad reviews

118
00:04:45.160 --> 00:04:47.480
maybe are something that you want to look

119
00:04:47.480 --> 00:04:47.720
at.

120
00:04:48.500 --> 00:04:49.420
So I'm going to go back to the

121
00:04:49.420 --> 00:04:51.520
Google Play Store here and just scroll down

122
00:04:51.520 --> 00:04:52.100
a little bit.

123
00:04:52.360 --> 00:04:54.480
You can see it has some screenshots about

124
00:04:54.480 --> 00:04:58.160
the application, as well as a detailed description

125
00:04:58.160 --> 00:05:00.600
here that can give you some information about

126
00:05:00.600 --> 00:05:01.480
the app as well.

127
00:05:01.780 --> 00:05:03.820
You can see down here in the bottom

128
00:05:03.820 --> 00:05:06.440
of the description it has some URLs that

129
00:05:06.440 --> 00:05:07.920
might be helpful for you to go out

130
00:05:07.920 --> 00:05:11.040
to, like this uber.com help, Facebook and

131
00:05:11.040 --> 00:05:12.320
Twitter accounts as well.

132
00:05:12.800 --> 00:05:14.420
Also some more URLs.

133
00:05:14.880 --> 00:05:16.960
These Facebook and Twitter accounts can be helpful

134
00:05:16.960 --> 00:05:20.080
because that could also, when a new application

135
00:05:20.080 --> 00:05:22.480
version goes out, maybe they do a little

136
00:05:22.480 --> 00:05:24.980
announcement out there on the social media channels.

137
00:05:27.400 --> 00:05:30.140
Again, you can go to the reviews, take

138
00:05:30.140 --> 00:05:32.320
a look through some of these reviews, look

139
00:05:32.320 --> 00:05:34.840
at the bugs that users are experiencing, and

140
00:05:34.840 --> 00:05:37.100
that could possibly give you some hints on

141
00:05:37.100 --> 00:05:38.540
things that you could look at in terms

142
00:05:38.540 --> 00:05:40.920
of functionality that might have some bugs or

143
00:05:40.920 --> 00:05:42.540
security vulnerabilities in them.

144
00:05:42.940 --> 00:05:44.700
You can click read all reviews if you

145
00:05:44.700 --> 00:05:46.640
want to read every single review for the

146
00:05:46.640 --> 00:05:47.200
application.

147
00:05:48.440 --> 00:05:50.120
You can see here they say we update

148
00:05:50.120 --> 00:05:52.040
the Uber app as often as possible.

149
00:05:52.040 --> 00:05:54.540
Things about the patch notes will be featured

150
00:05:54.540 --> 00:05:56.780
here in the what's new section, so if

151
00:05:56.780 --> 00:05:59.400
they say they patched some security fixes or

152
00:05:59.400 --> 00:06:01.240
anything like that, it says things here like

153
00:06:01.240 --> 00:06:03.520
several bug fixes and performance improvements.

154
00:06:06.300 --> 00:06:08.160
You can get a quick view of the

155
00:06:08.160 --> 00:06:10.800
permissions that are required for this application by

156
00:06:10.800 --> 00:06:12.220
clicking the view details here.

157
00:06:12.660 --> 00:06:15.260
Basically what permissions are, it's everything that the

158
00:06:15.260 --> 00:06:18.080
application needs access to to function properly.

159
00:06:18.080 --> 00:06:20.720
For the Uber app, we can obviously imagine

160
00:06:20.720 --> 00:06:25.380
things like the microphone, your identity, photos, video,

161
00:06:25.700 --> 00:06:26.640
camera, etc.

162
00:06:27.160 --> 00:06:29.620
Anything like this could be all used by

163
00:06:29.620 --> 00:06:30.280
the application.

164
00:06:30.880 --> 00:06:33.120
This can actually give you some information about

165
00:06:33.120 --> 00:06:34.760
the types of data that the app is

166
00:06:34.760 --> 00:06:37.940
collecting and the areas of your phone that

167
00:06:37.940 --> 00:06:39.160
it's going to need access to.

168
00:06:39.540 --> 00:06:41.140
That will also come back when we look

169
00:06:41.140 --> 00:06:44.220
at the static analysis section for this course.

170
00:06:45.420 --> 00:06:47.720
You can see the current version here says

171
00:06:47.720 --> 00:06:50.120
varies with device, so depending on what kind

172
00:06:50.120 --> 00:06:51.980
of Android device you're using, you get a

173
00:06:51.980 --> 00:06:53.620
different version of the application.

174
00:06:53.780 --> 00:06:55.960
It can be something useful when we're downloading

175
00:06:55.960 --> 00:06:57.980
the app from the Play Store and installing

176
00:06:57.980 --> 00:06:59.600
it on our different devices.

177
00:07:01.120 --> 00:07:03.480
Going down here you can see information about

178
00:07:03.480 --> 00:07:05.560
the developer, such as the support at uber

179
00:07:05.560 --> 00:07:06.960
.com email address.

180
00:07:07.180 --> 00:07:09.100
That might be something of interest to you.

181
00:07:09.340 --> 00:07:11.300
You can also look at the privacy policy

182
00:07:11.300 --> 00:07:13.680
on Uber's website, and maybe this is a

183
00:07:13.680 --> 00:07:15.800
link to other areas of the website as

184
00:07:15.800 --> 00:07:16.060
well.

185
00:07:16.760 --> 00:07:18.880
That's about it for the Google Play Store.

186
00:07:19.340 --> 00:07:21.140
Let's move over to the Apple Store and

187
00:07:21.140 --> 00:07:22.340
see what's available there.

188
00:07:22.900 --> 00:07:25.060
Here is the exact same app on the

189
00:07:25.060 --> 00:07:25.880
Apple Store.

190
00:07:26.260 --> 00:07:28.720
Again, you can click this Uber Technologies Inc.

191
00:07:28.760 --> 00:07:29.900
I'm going to open this in a new

192
00:07:29.900 --> 00:07:30.320
tab.

193
00:07:30.840 --> 00:07:33.400
You can see that there's these applications here

194
00:07:33.400 --> 00:07:33.860
as well.

195
00:07:34.340 --> 00:07:36.840
We can see some differences in the Uber

196
00:07:36.840 --> 00:07:37.480
app here.

197
00:07:37.560 --> 00:07:39.880
We have 1, 2, 3, 4, 5, 6,

198
00:07:40.000 --> 00:07:41.360
7, 8.

199
00:07:41.420 --> 00:07:43.420
This one doesn't really count to Apple Watch,

200
00:07:43.540 --> 00:07:43.680
right?

201
00:07:43.680 --> 00:07:46.600
So there's really 7 different applications here.

202
00:07:47.140 --> 00:07:49.140
On the Android side we have 1, 2,

203
00:07:49.260 --> 00:07:52.640
3, 4, 5, 6, 7, 8 applications, right?

204
00:07:53.000 --> 00:07:54.960
And what's different between these two?

205
00:07:55.120 --> 00:07:57.480
So we have Uber Eats Manager, Uber Eats

206
00:07:57.480 --> 00:08:01.820
Orders, or Uber Freight, Uber Driver, Uber Eats.

207
00:08:02.560 --> 00:08:06.360
The difference looks like it's this Uber Fleet

208
00:08:06.360 --> 00:08:06.780
app.

209
00:08:07.100 --> 00:08:09.880
So this might be a brand new application

210
00:08:09.880 --> 00:08:12.620
on the Android side, this Uber Fleet app.

211
00:08:12.620 --> 00:08:14.480
So that is something as a bug bounty

212
00:08:14.480 --> 00:08:15.960
hunter you can go out and look at

213
00:08:15.960 --> 00:08:18.620
because it's probably a brand new application since

214
00:08:18.620 --> 00:08:20.020
it's not on iOS yet.

215
00:08:20.560 --> 00:08:24.520
So maybe they're doing some testing or beta

216
00:08:24.520 --> 00:08:26.860
testing out there on Android before they move

217
00:08:26.860 --> 00:08:27.660
this to iOS.

218
00:08:27.920 --> 00:08:29.320
So it could be something that would be

219
00:08:29.320 --> 00:08:31.299
interesting from a pen tester's perspective.

220
00:08:32.200 --> 00:08:34.580
Going back to the Uber app here on

221
00:08:34.580 --> 00:08:37.360
the Apple Store, you can see similarly it

222
00:08:37.360 --> 00:08:38.960
has a lot of screenshots here.

223
00:08:40.020 --> 00:08:41.200
I'm going to click more here.

224
00:08:41.200 --> 00:08:43.500
Their description is pretty much the same.

225
00:08:43.820 --> 00:08:45.520
Again you still want to look through this

226
00:08:45.520 --> 00:08:47.580
in case there's a different URL or a

227
00:08:47.580 --> 00:08:48.180
different website.

228
00:08:48.780 --> 00:08:50.780
What's really nice about the Apple Store as

229
00:08:50.780 --> 00:08:52.240
well is that we can actually click this

230
00:08:52.240 --> 00:08:54.720
version history here and it will show us

231
00:08:54.720 --> 00:08:57.260
a bunch of different versions of the application,

232
00:08:57.740 --> 00:09:00.300
their version number, and it also shows you

233
00:09:00.300 --> 00:09:01.940
the things like the patch notes, right?

234
00:09:02.360 --> 00:09:05.240
So this can give you some information about

235
00:09:05.240 --> 00:09:07.220
what they might have changed in the application.

236
00:09:07.500 --> 00:09:09.820
If they're disclosing some information in this patch

237
00:09:09.820 --> 00:09:13.420
notes, maybe about security vulnerabilities or bug fixes.

238
00:09:13.960 --> 00:09:16.020
Here everything looks to be pretty much the

239
00:09:16.020 --> 00:09:17.680
same on every single release.

240
00:09:18.200 --> 00:09:19.760
So they're doing a good job there.

241
00:09:20.020 --> 00:09:21.940
Now the other thing that you can get

242
00:09:21.940 --> 00:09:23.960
out of this though is the day that

243
00:09:23.960 --> 00:09:24.440
they release.

244
00:09:24.600 --> 00:09:27.700
So this is September 7th, August 30th, August

245
00:09:27.700 --> 00:09:29.880
23rd, August 21st.

246
00:09:29.880 --> 00:09:32.700
For some reason they released one on a

247
00:09:32.700 --> 00:09:35.280
different cadence there, but it mostly looks like

248
00:09:35.280 --> 00:09:38.140
this application is updated about every seven days.

249
00:09:38.600 --> 00:09:40.520
So that can give you some information about

250
00:09:40.520 --> 00:09:43.880
when the application is updated, and if they

251
00:09:43.880 --> 00:09:45.540
do something that's kind of out of the

252
00:09:45.540 --> 00:09:47.700
norm, maybe that will tell you that they

253
00:09:47.700 --> 00:09:50.160
patched something important in that version.

254
00:09:51.120 --> 00:09:53.460
Again going down through the Apple Store you

255
00:09:53.460 --> 00:09:55.180
can look at the reviews and see some

256
00:09:55.180 --> 00:09:57.180
of the bugs and things like that, and

257
00:09:57.180 --> 00:09:58.800
of course the Apple Store does a good

258
00:09:58.800 --> 00:10:00.900
job of showing you what data is used

259
00:10:00.900 --> 00:10:03.180
to track you as well as the data

260
00:10:03.180 --> 00:10:05.220
linked to you that might be utilised throughout

261
00:10:05.220 --> 00:10:06.060
this application.

262
00:10:06.960 --> 00:10:09.080
You can also click the see details here

263
00:10:09.080 --> 00:10:10.680
if you want to see the really detailed

264
00:10:10.680 --> 00:10:11.100
list.

265
00:10:11.940 --> 00:10:13.700
And going down here you can also see

266
00:10:13.700 --> 00:10:16.740
the compatibility with different types of iOS, and

267
00:10:16.740 --> 00:10:18.720
this can be useful for us as pen

268
00:10:18.720 --> 00:10:20.360
testers because if we can run this on

269
00:10:20.360 --> 00:10:23.100
something as far back as like iOS 12,

270
00:10:23.480 --> 00:10:25.480
it can actually help us to inspect some

271
00:10:25.480 --> 00:10:27.820
of the application traffic without having to deal

272
00:10:27.820 --> 00:10:29.000
with SSL pinning.

273
00:10:29.000 --> 00:10:32.680
So going back to iOS 12, there's not

274
00:10:32.680 --> 00:10:34.920
really any validation on the certificates for the

275
00:10:34.920 --> 00:10:37.560
applications I don't think, and we could actually

276
00:10:37.560 --> 00:10:40.600
intercept this without having to bypass SSL pinning,

277
00:10:40.760 --> 00:10:43.020
which you'll learn more about throughout this course.

278
00:10:43.400 --> 00:10:45.140
You can also look at the languages that

279
00:10:45.140 --> 00:10:47.060
are supported by the application here.

280
00:10:47.420 --> 00:10:49.980
Maybe that is of interest to you, you

281
00:10:49.980 --> 00:10:52.680
know, if you're looking for hardcoded strings in

282
00:10:52.680 --> 00:10:53.480
different languages.

283
00:10:54.560 --> 00:10:57.060
Obviously there's links here for the developer website

284
00:10:57.060 --> 00:10:58.300
leading to uber.com.

285
00:10:58.300 --> 00:11:01.020
Again, the help.uber.com and the privacy

286
00:11:01.020 --> 00:11:02.240
policy as well.

287
00:11:02.980 --> 00:11:04.580
You can scroll down and see the more

288
00:11:04.580 --> 00:11:06.880
by this developer, but that's pretty much everything

289
00:11:06.880 --> 00:11:08.640
that's out there on the Apple Store.

290
00:11:10.000 --> 00:11:11.760
That's how I would kind of do a

291
00:11:11.760 --> 00:11:14.540
reconnaissance overall when I'm looking at an application

292
00:11:14.540 --> 00:11:16.400
from the App Store perspective.

293
00:11:17.460 --> 00:11:19.740
Coming back to our slides here, let's move

294
00:11:19.740 --> 00:11:21.320
into the static analysis.

295
00:11:21.860 --> 00:11:23.560
So when we get to the static analysis

296
00:11:23.560 --> 00:11:26.800
section of our mobile pen testing process, we

297
00:11:26.800 --> 00:11:29.380
want to be reading the application source code

298
00:11:29.380 --> 00:11:32.740
via manual or automated tools to assess the

299
00:11:32.740 --> 00:11:33.160
security.

300
00:11:33.540 --> 00:11:35.280
What we'll be doing here is looking for

301
00:11:35.280 --> 00:11:38.500
things like hardcoded strings, things that might indicate

302
00:11:38.500 --> 00:11:43.340
security misconfigurations, maybe things like emails, usernames, passwords,

303
00:11:43.820 --> 00:11:47.440
API keys, anything like that that will be

304
00:11:47.440 --> 00:11:49.040
used throughout this application.

305
00:11:49.620 --> 00:11:52.060
The cool thing about our static analysis is

306
00:11:52.060 --> 00:11:54.080
that this can actually result in the pen

307
00:11:54.080 --> 00:11:55.600
testing process being triggered.

308
00:11:56.080 --> 00:11:59.220
So if we find something like, say, a

309
00:11:59.220 --> 00:12:01.640
URL, maybe a website we did not know

310
00:12:01.640 --> 00:12:05.880
about before, or an email address, a storage

311
00:12:05.880 --> 00:12:08.200
bucket, anything like that, that can be very

312
00:12:08.200 --> 00:12:10.800
useful for us as pen testers, because once

313
00:12:10.800 --> 00:12:12.520
we find that URL, we can go out,

314
00:12:12.620 --> 00:12:14.460
we can do some reconnaissance on that URL,

315
00:12:14.920 --> 00:12:17.100
we can enumerate some information about that URL,

316
00:12:17.220 --> 00:12:18.760
and maybe it leads us to a new

317
00:12:18.760 --> 00:12:21.680
exploitation path that was only available when we

318
00:12:21.680 --> 00:12:22.980
found this new URL.

319
00:12:22.980 --> 00:12:25.380
Now something to keep in mind, too, is

320
00:12:25.380 --> 00:12:27.580
that a lot of companies use a special

321
00:12:27.580 --> 00:12:30.560
API gateway for their mobile applications.

322
00:12:31.140 --> 00:12:33.800
Sometimes they will have configuration files for that

323
00:12:33.800 --> 00:12:36.020
mobile app stored out there on their traditional

324
00:12:36.020 --> 00:12:39.000
website under a special directory, or maybe it

325
00:12:39.000 --> 00:12:41.740
goes to a completely different API gateway that

326
00:12:41.740 --> 00:12:43.580
is not the same one for their traditional

327
00:12:43.580 --> 00:12:44.160
website.

328
00:12:44.580 --> 00:12:46.620
So when we're looking at the traditional website

329
00:12:46.620 --> 00:12:49.040
versus the mobile app, maybe we will find

330
00:12:49.040 --> 00:12:51.240
some new information that we did not know

331
00:12:51.240 --> 00:12:52.040
about before.

332
00:12:52.920 --> 00:12:56.080
Obviously, we find things like emails or usernames,

333
00:12:56.440 --> 00:12:59.020
we can do some reconnaissance using phonebook.cz

334
00:12:59.020 --> 00:13:02.140
or try to look up if that email,

335
00:13:02.400 --> 00:13:04.940
username, or password has been exploited in the

336
00:13:04.940 --> 00:13:05.360
past.

337
00:13:05.860 --> 00:13:07.460
If we find a storage bucket, we're going

338
00:13:07.460 --> 00:13:09.440
to go out and do some reconnaissance on

339
00:13:09.440 --> 00:13:11.480
that as well, find out if the storage

340
00:13:11.480 --> 00:13:15.480
bucket is properly protected by security measures, we

341
00:13:15.480 --> 00:13:18.340
do some enumeration on the company's cloud resources

342
00:13:18.340 --> 00:13:18.960
as well.

343
00:13:21.450 --> 00:13:23.730
And the thing about static analysis that I'm

344
00:13:23.730 --> 00:13:26.270
trying to show in this diagram is that

345
00:13:26.270 --> 00:13:28.730
static analysis can lead you to a bunch

346
00:13:28.730 --> 00:13:30.010
of different areas, right?

347
00:13:30.090 --> 00:13:32.430
So our static analysis, maybe we find a

348
00:13:32.430 --> 00:13:34.610
storage bucket URL shown in the top of

349
00:13:34.610 --> 00:13:35.110
the screen.

350
00:13:35.430 --> 00:13:36.830
We want to go out there, check the

351
00:13:36.830 --> 00:13:39.590
bucket security, and check for additional company buckets.

352
00:13:40.150 --> 00:13:42.570
Maybe we find a Firebase URL in the

353
00:13:42.570 --> 00:13:43.850
green boxes here on the right.

354
00:13:43.850 --> 00:13:45.690
We want to go out there, check the

355
00:13:45.690 --> 00:13:48.290
Firebase security, look for what kind of data

356
00:13:48.290 --> 00:13:50.590
is being collected in that Firebase database.

357
00:13:51.230 --> 00:13:53.410
Maybe we also want to do some reconnaissance

358
00:13:53.410 --> 00:13:55.270
and find out if the company has other

359
00:13:55.270 --> 00:13:57.610
Firebase databases that are out there that are

360
00:13:57.610 --> 00:13:58.510
similarly named.

361
00:13:58.890 --> 00:14:01.130
For example, you might have a storage bucket

362
00:14:01.130 --> 00:14:06.450
or a Firebase database called uber.qa versus

363
00:14:06.450 --> 00:14:09.850
uber.prod versus uber.test, and maybe those

364
00:14:09.850 --> 00:14:12.870
all have a different security configuration with them.

365
00:14:12.870 --> 00:14:16.030
So looking for common vectors like that could

366
00:14:16.030 --> 00:14:18.170
also lead to some exploitation.

367
00:14:19.010 --> 00:14:21.130
In our static analysis, we also want to

368
00:14:21.130 --> 00:14:24.070
be looking for things like API URLs and

369
00:14:24.070 --> 00:14:26.830
also anywhere that the application is using hard

370
00:14:26.830 --> 00:14:30.550
-coded API keys like client credentials or a

371
00:14:30.550 --> 00:14:33.190
hard-coded username and password to access those

372
00:14:33.190 --> 00:14:34.770
API locations.

373
00:14:35.050 --> 00:14:36.950
It's also possible that we could find some

374
00:14:36.950 --> 00:14:39.450
Swagger documentation out there as well that could

375
00:14:39.450 --> 00:14:41.230
tell us a little bit about the different

376
00:14:41.230 --> 00:14:43.250
types of requests that are allowed in the

377
00:14:43.250 --> 00:14:43.590
API.

378
00:14:44.970 --> 00:14:47.290
Obviously, if we find a URL, we want

379
00:14:47.290 --> 00:14:49.690
to try to enumerate as many company websites

380
00:14:49.690 --> 00:14:53.830
or URLs as possible, and sometimes mobile applications

381
00:14:53.830 --> 00:14:56.650
will be calling a specific directory that maybe

382
00:14:56.650 --> 00:14:58.570
isn't available to any other source.

383
00:14:58.690 --> 00:15:00.770
Maybe there's a special header in there that

384
00:15:00.770 --> 00:15:02.430
says, hey, I'm a mobile app, so give

385
00:15:02.430 --> 00:15:03.810
me this config file, right?

386
00:15:03.810 --> 00:15:06.990
That can be something that can be a

387
00:15:06.990 --> 00:15:10.290
good target for us as well when we're

388
00:15:10.290 --> 00:15:11.930
doing our static analysis.

389
00:15:12.670 --> 00:15:14.490
Also in static analysis, we want to look

390
00:15:14.490 --> 00:15:16.350
for things related to SQL statements.

391
00:15:16.910 --> 00:15:19.230
So we can do things like SQL injection

392
00:15:19.230 --> 00:15:22.210
later when we're doing dynamic analysis, or look

393
00:15:22.210 --> 00:15:24.870
for where SQL databases might actually be stored

394
00:15:24.870 --> 00:15:25.950
in the mobile app.

395
00:15:26.470 --> 00:15:29.270
Also we can look for any generic variables

396
00:15:29.270 --> 00:15:30.990
so that we can try to fuzz them

397
00:15:30.990 --> 00:15:31.410
as well.

398
00:15:31.410 --> 00:15:34.310
Maybe in the mobile application, you only have

399
00:15:34.310 --> 00:15:36.730
the option for five or six different options,

400
00:15:37.070 --> 00:15:38.910
but when we're doing our dynamic analysis, we

401
00:15:38.910 --> 00:15:42.250
can actually change that option and maybe it

402
00:15:42.250 --> 00:15:44.170
gives us an error message or something like

403
00:15:44.170 --> 00:15:44.710
that, right?

404
00:15:44.770 --> 00:15:46.350
So we want to look at what variables

405
00:15:46.350 --> 00:15:49.010
are being stored, how they're being stored, and

406
00:15:49.010 --> 00:15:50.730
try to fuzz them as well when we

407
00:15:50.730 --> 00:15:52.490
get to the dynamic analysis section.

408
00:15:52.990 --> 00:15:55.390
And finally, when we're doing our static analysis,

409
00:15:55.570 --> 00:15:57.990
we want to look for local storage locations

410
00:15:57.990 --> 00:15:58.530
as well.

411
00:15:58.530 --> 00:16:00.910
We want to look through the phone storage

412
00:16:00.910 --> 00:16:02.790
and see what is being stored there.

413
00:16:03.130 --> 00:16:05.530
Try to find things like sensitive customer data,

414
00:16:05.730 --> 00:16:08.150
SQLite databases, and the strings that they might

415
00:16:08.150 --> 00:16:11.070
contain, as well as anything like default accounts

416
00:16:11.070 --> 00:16:13.470
or credentials that might be being stored on

417
00:16:13.470 --> 00:16:14.530
the Android phone.

418
00:16:15.970 --> 00:16:19.190
Now moving into dynamic analysis, this is when

419
00:16:19.190 --> 00:16:21.650
we'll be actually running the application and trying

420
00:16:21.650 --> 00:16:22.550
to manipulate it.

421
00:16:22.650 --> 00:16:25.790
So we'll be intercepting application traffic with tools

422
00:16:25.790 --> 00:16:27.710
like Burp Suite and ProxyMan so we can

423
00:16:27.710 --> 00:16:29.730
try to mess with some of the parameters

424
00:16:29.730 --> 00:16:32.130
that are being sent by the mobile application.

425
00:16:32.730 --> 00:16:34.870
We'll also be trying to dump memory addresses

426
00:16:34.870 --> 00:16:37.370
from the application to check for anything that's

427
00:16:37.370 --> 00:16:38.910
stored insecurely in memory.

428
00:16:39.230 --> 00:16:42.230
We'll be checking local storage for files that

429
00:16:42.230 --> 00:16:45.330
are created at runtime, things like SQLite databases

430
00:16:45.330 --> 00:16:47.050
and shared preferences as well.

431
00:16:47.470 --> 00:16:49.890
We also want to break SSL pinning if

432
00:16:49.890 --> 00:16:52.150
it's implemented in our mobile application.

433
00:16:52.670 --> 00:16:56.010
Now remember, dynamic analysis can often result in

434
00:16:56.010 --> 00:16:58.550
attacks related to the OWASP top 10.

435
00:16:58.790 --> 00:17:00.710
Now we're talking about the OWASP top 10

436
00:17:00.710 --> 00:17:01.570
for web here.

437
00:17:01.910 --> 00:17:04.250
So when we're doing our dynamic analysis, we

438
00:17:04.250 --> 00:17:06.210
want to be looking for things in attack

439
00:17:06.210 --> 00:17:09.790
vectors like SQL injection, cross-site scripting, indirect

440
00:17:09.790 --> 00:17:12.670
object references, XXE, etc.

441
00:17:13.010 --> 00:17:15.170
If you're not familiar with the OWASP top

442
00:17:15.170 --> 00:17:17.349
10 for web, I definitely recommend you go

443
00:17:17.349 --> 00:17:19.109
out there and read up on that because

444
00:17:19.109 --> 00:17:20.569
we're going to be using some of those

445
00:17:20.569 --> 00:17:23.329
attack vectors throughout our dynamic analysis as well,

446
00:17:23.730 --> 00:17:26.750
especially when we're trying to manipulate some application

447
00:17:26.750 --> 00:17:27.270
traffic.

448
00:17:27.870 --> 00:17:30.010
Now I will throw one caveat out there,

449
00:17:30.330 --> 00:17:32.250
and it's a note on cross-site scripting.

450
00:17:32.790 --> 00:17:35.970
So oftentimes with a mobile application, you will

451
00:17:35.970 --> 00:17:38.510
not get an XSS, a cross-site scripting

452
00:17:38.510 --> 00:17:42.130
vulnerability to fire within the mobile application itself,

453
00:17:42.370 --> 00:17:46.170
but remember that sometimes these mobile applications can

454
00:17:46.170 --> 00:17:48.870
actually affect the full version of the website.

455
00:17:48.870 --> 00:17:51.410
For example, if you have your name, you

456
00:17:51.410 --> 00:17:53.310
can change your name on the mobile app,

457
00:17:53.570 --> 00:17:56.350
that should also get affected on the full

458
00:17:56.350 --> 00:17:58.770
version of the website as well, if the

459
00:17:58.770 --> 00:18:01.390
company is supporting a full version of the

460
00:18:01.390 --> 00:18:02.170
website, right?

461
00:18:02.610 --> 00:18:06.990
So sometimes inputs from the mobile application are

462
00:18:06.990 --> 00:18:09.870
not sanitised as well as the inputs on

463
00:18:09.870 --> 00:18:10.410
the website.

464
00:18:11.070 --> 00:18:13.770
So sometimes we can actually get an XSS

465
00:18:13.770 --> 00:18:16.470
to go pass through the mobile app and

466
00:18:16.470 --> 00:18:18.850
then get reflected on the website as well.

467
00:18:19.190 --> 00:18:21.690
So if you're looking for XSS vulnerabilities, keep

468
00:18:21.690 --> 00:18:23.770
that in mind that mobile apps can still

469
00:18:23.770 --> 00:18:26.330
be a threat vector for our cross-site

470
00:18:26.330 --> 00:18:27.550
scripting payloads.

471
00:18:28.790 --> 00:18:31.230
Now when it comes to reporting, it's going

472
00:18:31.230 --> 00:18:32.890
to be the same as the pen testing

473
00:18:32.890 --> 00:18:33.890
process as well.

474
00:18:34.210 --> 00:18:37.310
Our reporting should contain an executive summary as

475
00:18:37.310 --> 00:18:40.130
well as the specific vulnerabilities that we've discovered.

476
00:18:40.470 --> 00:18:42.250
And I want you to write your reports

477
00:18:42.250 --> 00:18:44.990
with both the OWASP Top 10 Web and

478
00:18:44.990 --> 00:18:47.490
the OWASP Top 10 Mobile in mind, because

479
00:18:47.490 --> 00:18:49.630
these are common vectors, not for just web

480
00:18:49.630 --> 00:18:52.790
applications, but for web and mobile applications, right?

481
00:18:52.990 --> 00:18:55.170
We want to provide the business with the

482
00:18:55.170 --> 00:18:57.930
criticality as well as the steps to reproduce

483
00:18:57.930 --> 00:19:00.070
any vulnerabilities that we've discovered.

484
00:19:00.670 --> 00:19:03.690
So again, criticality is very important for the

485
00:19:03.690 --> 00:19:06.310
business so they know how to prioritise the

486
00:19:06.310 --> 00:19:09.910
remediation of these security vulnerabilities so that they're

487
00:19:09.910 --> 00:19:12.210
fixing the criticals and the highs first, and

488
00:19:12.210 --> 00:19:13.890
then anything else that you find that's more

489
00:19:13.890 --> 00:19:16.250
minor, they can fix those later, right?

490
00:19:16.970 --> 00:19:18.850
We want to provide the steps to reproduce

491
00:19:18.850 --> 00:19:21.750
so that a developer can go in, reproduce

492
00:19:21.750 --> 00:19:25.290
your steps and understand exactly how you got

493
00:19:25.290 --> 00:19:26.230
to where you got to.

494
00:19:26.870 --> 00:19:28.630
And something else I'll throw in there for

495
00:19:28.630 --> 00:19:31.450
reporting for both the pen testing process and

496
00:19:31.450 --> 00:19:33.630
for our mobile pen testing is you want

497
00:19:33.630 --> 00:19:36.990
to try to mention the positive security implementations

498
00:19:36.990 --> 00:19:37.750
where possible.

499
00:19:38.090 --> 00:19:41.290
No matter what, with any mobile application or

500
00:19:41.290 --> 00:19:44.630
any pen testing engagement, they're likely to have

501
00:19:44.630 --> 00:19:47.210
implemented at least some amount of security.

502
00:19:47.750 --> 00:19:50.190
So whatever you found is a positive security

503
00:19:50.190 --> 00:19:53.670
implementation, I definitely recommend including those in your

504
00:19:53.670 --> 00:19:55.890
report as well so that they do feel

505
00:19:55.890 --> 00:19:59.270
a little assurance that they've done some things

506
00:19:59.270 --> 00:19:59.650
right.

507
00:20:01.110 --> 00:20:04.250
In only severe, severe cases is there a

508
00:20:04.250 --> 00:20:07.450
case where a company has never implemented any

509
00:20:07.450 --> 00:20:10.630
security for their implementation, so make sure that

510
00:20:10.630 --> 00:20:12.710
you're actually going out there and highlighting the

511
00:20:12.710 --> 00:20:15.610
positives as well because it will help your

512
00:20:15.610 --> 00:20:18.590
client and it will also validate that they're

513
00:20:18.590 --> 00:20:20.150
definitely doing some things right.

514
00:20:20.610 --> 00:20:22.010
So that's all that I have for the

515
00:20:22.010 --> 00:20:24.250
mobile pen testing process and I'll see you

516
00:20:24.250 --> 00:20:25.270
in the next videos.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3:Android-Intro-and-Security-Architecture



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