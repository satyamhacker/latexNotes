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