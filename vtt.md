# Section 1: Not of use


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================


# Section 2: Introduction & Fundamentals

1
00:00:01,680 --> 00:00:06,560
Now, here are some of the bug bounty tips that I want to share with all the participants to keep in

2
00:00:06,560 --> 00:00:08,280
mind before we begin the session.

3
00:00:08,680 --> 00:00:11,800
First is think creatively and out of the box.

4
00:00:12,080 --> 00:00:26,320
Remember, I, or any given technology would be able to help you perform given tasks, but only when

5
00:00:26,360 --> 00:00:27,960
you think out of the box.

6
00:00:28,240 --> 00:00:36,720
Okay, so these are assisted technologies which are going to assist you to help you be more efficient

7
00:00:36,720 --> 00:00:37,800
and scalable.

8
00:00:38,080 --> 00:00:47,360
But you have to give a prompt to the LLM or the AI bot so that it does what you are thinking.

9
00:00:47,560 --> 00:00:59,160
So it is definitely not like that, that utilizing AI or doing AI, uh, amalgamation or uh, composition

10
00:00:59,160 --> 00:01:05,880
with bug bounties or red teaming would let you identify various different types of zero days.

11
00:01:06,280 --> 00:01:12,440
It can definitely help in assisting and doing that, but when you think out of the box and creative.

12
00:01:13,440 --> 00:01:23,400
So our agenda and motive during the five days boot camp is going to be that we focus on how we can try

13
00:01:23,400 --> 00:01:25,720
to cater creative thinking.

14
00:01:26,480 --> 00:01:32,880
Hence, we are going to get exposed to a lot of scenarios where we would be seeing how just by thinking

15
00:01:32,880 --> 00:01:39,400
out of the box, we are able to identify a lot of new things hidden attack surface, hidden assets,

16
00:01:39,960 --> 00:01:43,640
hidden content when we do discovery in the reconnaissance phase.

17
00:01:44,440 --> 00:01:45,880
Second is being efficient.

18
00:01:46,040 --> 00:01:48,160
Scripting or programming is helpful.

19
00:01:48,280 --> 00:01:50,680
So eventually I recommend shell scripting.

20
00:01:50,680 --> 00:01:53,760
We would be doing a lot of shell scripting during these sessions as well.

21
00:01:54,160 --> 00:02:00,880
And this helps us be more efficient so that we don't do the low level, low code stuff repeatedly and

22
00:02:00,880 --> 00:02:08,840
be focused more on identifying new type of vulnerabilities or upscaling our methodology.

23
00:02:09,080 --> 00:02:10,640
Practice, practice, practice.

24
00:02:10,640 --> 00:02:17,360
Because if you don't practice what you have learned or undergone during the session, you won't be able

25
00:02:17,360 --> 00:02:24,800
to master it or else it will just be like a nice two hours amazing session.

26
00:02:24,800 --> 00:02:28,960
Watching how AI can be used with bug, bounty and Pentesting methodology.

27
00:02:28,960 --> 00:02:32,880
But if you don't practice, you will not be able to make the max out of it.

28
00:02:33,640 --> 00:02:37,560
Last is don't discriminate with programs or bug categories while reporting.

29
00:02:37,840 --> 00:02:44,280
I have seen this largely people discriminate discriminate with the kind of vulnerabilities that they

30
00:02:44,280 --> 00:02:45,120
don't like.

31
00:02:45,480 --> 00:02:54,200
I have seen talk to more than 50,000 bug bounty hunters personally, and I can say that everyone have

32
00:02:54,240 --> 00:03:00,930
a choice of or a set of vulnerabilities that they usually try to find or hunt onto programs.

33
00:03:00,930 --> 00:03:06,330
And they would say, ah, I only like to hunt for broken access control vulnerabilities.

34
00:03:06,370 --> 00:03:11,290
I usually skip on vulnerabilities like ssrf because I don't usually find them.

35
00:03:11,290 --> 00:03:14,490
Hence I don't add them in my methodology, so I skip them.

36
00:03:15,090 --> 00:03:16,490
It doesn't work like that.

37
00:03:16,770 --> 00:03:23,010
A program is going to be vulnerable with all sort of vulnerabilities, and it is important for us that

38
00:03:23,010 --> 00:03:30,250
we knock the door of the organization with all the level of vulnerabilities that are that could be potentially

39
00:03:30,250 --> 00:03:32,010
present on the given target.

40
00:03:32,170 --> 00:03:39,330
So, uh, I would recommend to try, learn and keep all vulnerabilities in your into your methodology

41
00:03:39,330 --> 00:03:44,330
and just don't stick with 1 or 2 of your favorite vulnerabilities that you usually do.

42
00:03:44,370 --> 00:03:52,250
That is always a good approach, but expanding your horizon so that you are able to identify other set

43
00:03:52,250 --> 00:03:56,610
of vulnerabilities as well is going to be very, very helpful.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,440 --> 00:00:01,040
Okay.

2
00:00:01,400 --> 00:00:04,160
Uh, some of the key values that you should keep in mind.

3
00:00:04,200 --> 00:00:07,480
Be respectful to the traders and companies.

4
00:00:07,480 --> 00:00:13,720
So, uh, by the end of this program, you are going to learn a lot of different types of techniques

5
00:00:13,720 --> 00:00:18,320
and methodologies through which you would be able to uncover and identify vulnerabilities.

6
00:00:18,720 --> 00:00:24,360
Make sure that when you report to the traders or the organizations, you be respectful to them because

7
00:00:24,560 --> 00:00:30,880
they are also humans like you, and they might tend to sometimes overlook something that you have sent

8
00:00:31,040 --> 00:00:37,840
as as a bug report to them, or they might not be able to quickly assess the impact that you are trying

9
00:00:37,840 --> 00:00:39,680
to tell to the Trijet.

10
00:00:39,840 --> 00:00:43,720
So it is always important that you elaborate the bug report.

11
00:00:43,760 --> 00:00:50,680
Make sure it is clear, concise for someone to understand and why it is important for the company so

12
00:00:50,680 --> 00:00:56,760
that you save that extra two and fro time that you are going to do in discussion with the trigger.

13
00:00:56,960 --> 00:01:02,680
Even if the trigger doesn't understand what you are trying to elaborate with your bug report, make

14
00:01:02,720 --> 00:01:04,640
sure that you explain him.

15
00:01:04,640 --> 00:01:10,590
What is the impact of this bug on the organization, or the employees, or the type of data that the

16
00:01:10,590 --> 00:01:14,270
organization stores or holds or exchanges, etc..

17
00:01:14,310 --> 00:01:20,590
I'm sure the traders would be able to understand your situation and triage your report with appropriate

18
00:01:20,590 --> 00:01:21,430
severity.

19
00:01:22,150 --> 00:01:25,070
Community contributions are very important.

20
00:01:25,070 --> 00:01:30,630
I personally believe I have learned a lot from the community with various different types of tools,

21
00:01:30,630 --> 00:01:37,870
techniques that were available and were open sourced by various different types of, uh, respectful,

22
00:01:38,150 --> 00:01:41,550
uh, personalities in the cybersecurity domain.

23
00:01:41,670 --> 00:01:47,990
So I also believe the same you should also have the similar values that you also do community contribution

24
00:01:47,990 --> 00:01:54,390
and let others benefit from your knowledge or learning or toolsets or scripts that you make because

25
00:01:54,390 --> 00:01:56,110
it is always a give and take.

26
00:01:56,910 --> 00:01:57,710
Last one.

27
00:01:57,750 --> 00:02:03,470
Knowing limits in bug hunting, you should know what assets and data is critical on target.

28
00:02:03,510 --> 00:02:07,830
If you spot more than required access, it is found by you.

29
00:02:07,830 --> 00:02:10,630
Please pause and acknowledge the target program.

30
00:02:10,950 --> 00:02:17,910
This is because I have seen in past of several of my sessions, uh, participants have been able to

31
00:02:17,950 --> 00:02:25,260
get May then require access to the organization's assets or systems, let's say through SQL injection,

32
00:02:25,260 --> 00:02:26,860
they got access to the database.

33
00:02:26,860 --> 00:02:30,540
Now, the biggest mistake that they start doing is to prove the impact.

34
00:02:30,540 --> 00:02:37,060
They start dumping all of the critical information, KYC information or PII from the database.

35
00:02:37,300 --> 00:02:41,260
That is absolutely not the right way to approach it.

36
00:02:41,700 --> 00:02:48,060
Whenever you have access to a database, let's say immediately pause their take, required screenshots

37
00:02:48,100 --> 00:02:55,580
or video POC, report it to the target and let them know about these impact of this.

38
00:02:55,980 --> 00:03:02,300
Take prior permission that should you now go ahead or take an additional step from here.

39
00:03:02,780 --> 00:03:12,580
If you don't do that, and if you just not do not respect the target scope, exclusion or policies,

40
00:03:12,580 --> 00:03:17,300
then this can definitely turn out to be problematic on both the sides.

41
00:03:17,460 --> 00:03:20,580
So make sure that you know your limits in bug hunting.

42
00:03:20,580 --> 00:03:28,500
Always try to be respectful to the triggers and try to ask the organization that should you go deeper

43
00:03:28,500 --> 00:03:29,060
or not.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,280 --> 00:00:02,000
All right.

2
00:00:02,000 --> 00:00:05,760
So now let's understand about the goals and the strategies.

3
00:00:06,000 --> 00:00:12,600
So in the given bootcamp we are primarily going to focus from the beginning.

4
00:00:12,600 --> 00:00:15,560
That is recon to reporting.

5
00:00:15,920 --> 00:00:18,600
So what is primarily recon.

6
00:00:18,640 --> 00:00:23,800
All of you those who have joined this session would be very much familiar with the word reconnaissance.

7
00:00:24,680 --> 00:00:33,120
We would be in reconnaissance doing identity or identify attack surface management or do identify attack

8
00:00:33,120 --> 00:00:34,480
surface for the organization.

9
00:00:34,480 --> 00:00:41,520
That includes asset discovery, content discovery, uh, hidden assets identification, etc..

10
00:00:41,840 --> 00:00:46,720
But all of this would be assisted with the help of AI.

11
00:00:47,160 --> 00:00:58,160
So AI is going to help us perform the given tasks much faster in an efficient manner that probably would,

12
00:00:58,600 --> 00:01:04,080
uh, would take maybe days or weeks to do the similar task.

13
00:01:04,440 --> 00:01:11,000
In addition to that, uh, the recon techniques are going to help us find untouched targets that might

14
00:01:11,000 --> 00:01:20,600
not have been found earlier, or our recon techniques is going to help us spot commonly overlooked areas

15
00:01:20,600 --> 00:01:30,150
that people are does not tend to look deeply, which allows them to maybe or allows them to miss a lot

16
00:01:30,150 --> 00:01:32,510
of information or targets over there.

17
00:01:32,870 --> 00:01:37,910
I have been identifying various different types of targets in the past.

18
00:01:38,390 --> 00:01:46,550
I have also shown some of those targets and POCs in previous, uh, of my sessions on YouTube, etc.,

19
00:01:46,710 --> 00:01:52,830
wherein I have shown how I was able to discover a lot of different types of vulnerabilities that were

20
00:01:53,150 --> 00:01:58,910
that were commonly overlooked, uh, by pentesters or bug bounty researchers.

21
00:01:58,910 --> 00:02:06,990
So we would be focusing on those areas which are different and helps us identify the hidden attack surface,

22
00:02:06,990 --> 00:02:09,470
which is going to assist us in the next steps.

23
00:02:10,390 --> 00:02:15,790
Now, in the reporting part, we are going to do make sure that we mention the overall impact of the

24
00:02:15,830 --> 00:02:16,350
bug.

25
00:02:16,390 --> 00:02:18,790
We make a clear, concise steps to reproduce.

26
00:02:18,990 --> 00:02:21,350
We take screenshots and video POCs.

27
00:02:21,350 --> 00:02:25,110
That is going to be helpful for us and for doing this as well.

28
00:02:25,110 --> 00:02:33,310
We are going to utilize AI capabilities, which is going to help us, uh, create automated reports

29
00:02:33,310 --> 00:02:38,630
so that we do not put most of our times in the manual reporting work.

30
00:02:38,630 --> 00:02:46,150
Rather, we put our time and efforts in upskilling our methodology and doing more technical findings.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Bug Bounty Techniques

1
00:00:01,640 --> 00:00:09,880
So here are some of the program hunting techniques that I have found based on my research in the past

2
00:00:09,880 --> 00:00:12,080
that would help participants.

3
00:00:12,360 --> 00:00:18,400
So we all know to start with bug bounty hunting, let's say we need a target.

4
00:00:19,120 --> 00:00:26,440
There are various different types of bug bounty platforms that are available like Bugcrowd, Hackerone,

5
00:00:26,480 --> 00:00:30,880
integrity, and then zero, and so on.

6
00:00:31,200 --> 00:00:42,040
Now these bug bounty platforms are amazing to start with, but these platforms sometimes, as they are

7
00:00:42,040 --> 00:00:46,320
available for anyone to sign up and explore, could be crowded.

8
00:00:46,600 --> 00:00:49,480
That means there could be some security.

9
00:00:49,480 --> 00:00:55,680
Researchers have already picked up programs on old programs which have been lying over there, and it

10
00:00:55,680 --> 00:01:02,000
can be a difficult situation for a beginner who might not be able to choose or pick the right program

11
00:01:02,000 --> 00:01:03,800
and identify vulnerabilities.

12
00:01:04,320 --> 00:01:12,890
Hence, here is one of the technique that can help beginners or maybe the experts as well, to identify

13
00:01:13,530 --> 00:01:19,690
those bug bounty programs that that might not have been listed yet on these platforms.

14
00:01:20,050 --> 00:01:28,050
So here participants, we see that we are currently utilizing a website that is startup dot jobs.

15
00:01:28,210 --> 00:01:30,850
So so this is basically a job portal.

16
00:01:31,090 --> 00:01:40,570
So from this job portal we are able to identify various different types of job postings that are specifically

17
00:01:41,010 --> 00:01:42,970
with the keyword bug bounty.

18
00:01:43,090 --> 00:01:52,210
So for example, uh, if you look carefully then here we can see senior security engineer application

19
00:01:52,210 --> 00:01:54,890
security for Blue Apron is required.

20
00:01:54,890 --> 00:01:56,050
As we can see here.

21
00:01:56,250 --> 00:02:01,210
Support and evolve the bug bounty program and improve our program efficiency.

22
00:02:01,410 --> 00:02:02,090
Excellent.

23
00:02:02,210 --> 00:02:05,290
So let's try to do the similar keyword search.

24
00:02:05,450 --> 00:02:07,290
So I'm going to say site.

25
00:02:09,650 --> 00:02:11,810
Startup dot jobs.

26
00:02:12,290 --> 00:02:14,490
And we are going to search for bug bounty.

27
00:02:15,530 --> 00:02:23,050
And we can see we are able to identify that these organizations are looking at product security engineer

28
00:02:23,050 --> 00:02:28,530
or maybe a security researcher to manage their program, as we can see over here.

29
00:02:28,850 --> 00:02:37,730
And there are a lot of posts like this through which you would be able to identify private or hidden

30
00:02:37,970 --> 00:02:40,090
bug bounty programs as well here.

31
00:02:40,290 --> 00:02:48,050
Now, in this screenshot, we were able to see that there is a opening for a senior security engineer

32
00:02:48,050 --> 00:02:50,650
at Blue Apron, as we can see over here.

33
00:02:50,970 --> 00:02:51,330
So.

34
00:02:56,370 --> 00:03:02,490
So when we go over here we are able to see oh Blue Apron which is a part of vendor group has now uh

35
00:03:02,930 --> 00:03:05,770
came up on this as we can see.

36
00:03:07,010 --> 00:03:07,250
Yeah.

37
00:03:07,290 --> 00:03:08,050
Over here.

38
00:03:08,410 --> 00:03:14,730
And yes, it has now posted a bug bounty program here as well.

39
00:03:15,210 --> 00:03:22,210
Uh, as we can see and if you see here, then Blue Apron started using Hackerone today on March 25th.

40
00:03:22,250 --> 00:03:23,850
March 2025.

41
00:03:23,890 --> 00:03:29,500
So we could see just a month ago they have started using, uh, the hacker one platform.

42
00:03:29,500 --> 00:03:33,500
So, uh, I was able to identify this program a year ago.

43
00:03:33,700 --> 00:03:34,660
It was present.

44
00:03:34,660 --> 00:03:40,620
They were managing the program privately, but they came publicly a year later on.

45
00:03:40,780 --> 00:03:43,100
I have reported a couple of bugs on this program.

46
00:03:43,100 --> 00:03:44,380
How did I identify it?

47
00:03:44,380 --> 00:03:47,500
Based on the job posting that they they did.

48
00:03:47,660 --> 00:03:50,100
From there I came to know, okay, so they run a program.

49
00:03:50,100 --> 00:03:54,860
They are still not very mature towards security for their targets.

50
00:03:54,860 --> 00:04:01,140
It is a good chance that before it launches onto a platform like hacker one, let's try to manage to

51
00:04:01,180 --> 00:04:02,900
identify bugs onto that program.

52
00:04:02,900 --> 00:04:08,980
So it's not been even a month, uh, that they have been coming posted or uh, come up on the Hacker

53
00:04:08,980 --> 00:04:09,580
One platform.

54
00:04:09,580 --> 00:04:13,940
But there were a couple of issues that were that were already found by me onto their platform.

55
00:04:14,900 --> 00:04:17,660
So this was one such example as we saw here.

56
00:04:17,660 --> 00:04:20,260
There are more examples over here that you can see.

57
00:04:20,740 --> 00:04:28,620
And here you can see Blue Apron has already has rewarded $100 with 50 bonus for some of the bugs that

58
00:04:28,620 --> 00:04:33,260
I reported onto their, uh, target, as you can see in this screenshot.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:07,840 --> 00:00:08,600
Excellent.

2
00:00:08,600 --> 00:00:10,440
So here was our first technique.

3
00:00:10,440 --> 00:00:14,080
We would be seeing more techniques of how you can similarly do that.

4
00:00:14,320 --> 00:00:23,880
Now we can see here is another job posting a job portal or job posting portal which is Monster.com.

5
00:00:24,040 --> 00:00:31,240
So I just went to Google and did site Monster.com, Bug Bounty, and we can see there are job posts

6
00:00:31,240 --> 00:00:36,640
that have been done, for example, monitor the bug bounty program and forward valid findings to the

7
00:00:36,640 --> 00:00:38,640
engineering team for the remediation.

8
00:00:38,800 --> 00:00:40,320
We can see Ninja one.

9
00:00:40,360 --> 00:00:44,760
Ninja one is the organization which is currently running a bug bounty program.

10
00:00:45,160 --> 00:00:50,840
Similarly, we can here see they are looking for a Director of Security who can manage our bug bounty

11
00:00:50,840 --> 00:00:51,360
program.

12
00:00:51,360 --> 00:00:58,440
The program is every sort, so maybe we can go on Google and say every sort.

13
00:01:02,640 --> 00:01:08,440
So here we can see every sort is an AI powered contract management software suit.

14
00:01:08,600 --> 00:01:10,600
Let us see if they are running a program.

15
00:01:11,080 --> 00:01:12,800
Yeah they are.

16
00:01:12,920 --> 00:01:15,040
They have a vulnerability disclosure program.

17
00:01:15,040 --> 00:01:20,980
And here we can see they have a form as well where we can submit a bug report over here.

18
00:01:21,220 --> 00:01:22,380
So that is correct.

19
00:01:22,380 --> 00:01:26,180
We managed to successfully find the right program.

20
00:01:26,540 --> 00:01:26,900
Uh, that.

21
00:01:26,940 --> 00:01:28,860
Yes, indeed, it has a bug bounty program.

22
00:01:28,860 --> 00:01:37,660
Similarly, let's look up for Ninja one, Ninja one, top rated U, e, m and IT management software

23
00:01:37,660 --> 00:01:40,060
service, let's say Bug Bounty.

24
00:01:40,940 --> 00:01:46,620
Yes, they also have a bug bounty program and we are able to see that yes, it indeed had a program.

25
00:01:46,620 --> 00:01:51,820
And we can send a bug report to vulnerability at that Ninja One.com, as we can see over here.

26
00:01:52,100 --> 00:01:54,140
So that is absolutely right.

27
00:01:54,140 --> 00:01:58,780
And through this we were able to identify successfully the right programs.

28
00:01:58,980 --> 00:02:01,380
And we can report it to them as well.

29
00:02:01,740 --> 00:02:05,260
Now let's assume our first step is completed.

30
00:02:05,260 --> 00:02:13,940
We are able to identify programs, private programs from uh, platforms like Bugcrowd, hacker one zero

31
00:02:14,420 --> 00:02:18,060
integrity and then job posting portals.

32
00:02:18,100 --> 00:02:23,980
Now, what do we do with this targets or what do we do with this programs.

33
00:02:23,980 --> 00:02:31,100
So we are now going to initiate and learn about how effective reconnaissance can be done onto these

34
00:02:31,100 --> 00:02:37,060
programs, and what are the different types of techniques through which we can do attack surface mapping

35
00:02:37,060 --> 00:02:37,740
for them?


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,160 --> 00:00:03,400
Now let's assume our first step is completed.

2
00:00:03,400 --> 00:00:11,080
We are able to identify programs, private programs from other platforms like Bugcrowd, hacker one

3
00:00:11,640 --> 00:00:16,160
zero integrity, and then job posting portals.

4
00:00:16,200 --> 00:00:22,000
Now what do we do with this targets or what do we do with this programs?

5
00:00:22,080 --> 00:00:29,200
So we are now going to initiate and learn about how effective reconnaissance can be done onto these

6
00:00:29,200 --> 00:00:35,160
programs, and what are the different types of techniques through which we can do attack surface mapping

7
00:00:35,160 --> 00:00:35,800
for them.

8
00:00:36,480 --> 00:00:44,920
So in addition to this, uh, I would highly recommend, uh, participants to see bug bounty targets

9
00:00:44,960 --> 00:00:46,880
data GitHub repository.

10
00:00:47,360 --> 00:00:52,240
So this is the GitHub repository which keeps on updating hourly.

11
00:00:52,240 --> 00:00:56,720
So this repo contains hourly updated data dumps of the bug bounty scopes.

12
00:00:57,240 --> 00:01:06,700
It has currently, uh program data for five different bug bounty platforms Bugcrowd, Hackerone, Phaedrus,

13
00:01:07,100 --> 00:01:09,340
integrity and yes, we hack.

14
00:01:09,660 --> 00:01:14,860
So you can simply go to data and then you can see this will keep on updating every hour.

15
00:01:14,860 --> 00:01:19,820
So maybe if you go to Bugcrowd data JSON you would be able to see the programs.

16
00:01:19,980 --> 00:01:24,580
So here's the first program acorns grow the max payout.

17
00:01:25,660 --> 00:01:29,300
The website that is currently in scope is acorns.

18
00:01:29,820 --> 00:01:39,340
And they also have all of the subdomains of acorns as well over here star.com.

19
00:01:39,340 --> 00:01:43,580
And you would be able to see they also have their accounts for iOS application.

20
00:01:43,580 --> 00:01:48,020
They have GraphQL API and they have an Android application as well.

21
00:01:48,020 --> 00:01:49,340
They also have more assets.

22
00:01:49,380 --> 00:01:56,700
Go Henry picks picks.fr and they and the out of scope is share dot acorns grow dot accounts store dot

23
00:01:56,700 --> 00:01:57,260
accounts.

24
00:01:57,300 --> 00:01:57,780
Yeah.

25
00:01:57,780 --> 00:02:02,950
So we are able to see and understand the entire program structure directly from the JSON data.

26
00:02:02,950 --> 00:02:03,230
We.

27
00:02:03,270 --> 00:02:08,390
It is very, very easy to parse this with basic shell scripting on the terminal.

28
00:02:08,630 --> 00:02:16,270
That is going to help us stay focused and on track on the in scope targets for the current program.

29
00:02:16,270 --> 00:02:17,430
That is, accounts grow.

30
00:02:17,590 --> 00:02:18,430
And we saw that.

31
00:02:18,470 --> 00:02:18,870
Yeah.

32
00:02:19,470 --> 00:02:26,310
Uh, it has a entire sub domains, uh, range also in scope for the program.

33
00:02:26,310 --> 00:02:30,190
And the max payout is also, uh, fair.

34
00:02:30,390 --> 00:02:35,350
So we can take up this target, for instance, and we can focus on that as well.

35
00:02:36,190 --> 00:02:41,430
Uh, now, a very common questions question that has been asked usually is, uh, does this list contains

36
00:02:41,430 --> 00:02:43,550
private list of programs.

37
00:02:43,550 --> 00:02:45,310
So the answer to that is no.

38
00:02:45,550 --> 00:02:52,630
It only contains scraped publicly available programs that comes on, uh, platforms.

39
00:02:52,630 --> 00:02:59,710
So all the public programs that you are able to see on Bucktrout, those programs are being listed over

40
00:02:59,710 --> 00:03:07,970
here in the JSON format as well as all of the collected domains are also being added directly in the

41
00:03:08,010 --> 00:03:08,570
domains dot.

42
00:03:08,570 --> 00:03:09,330
TXT file.

43
00:03:09,330 --> 00:03:12,530
So here we can see Akons GraphQL Akons.

44
00:03:12,570 --> 00:03:15,170
Go Henry picks up that we saw.

45
00:03:15,330 --> 00:03:18,610
So these are the targets for the uh not this one.

46
00:03:18,610 --> 00:03:23,570
This is for the iOS application which is hosted.

47
00:03:23,570 --> 00:03:26,210
But these are the targets for the Accounts Grow program.

48
00:03:26,370 --> 00:03:30,010
So we can parse the data directly from the JSON file as well.

49
00:03:30,050 --> 00:03:34,770
Or maybe we can use the domains dot txt file as well to identify a list of targets.

50
00:03:35,010 --> 00:03:35,730
Excellent.

51
00:03:36,090 --> 00:03:40,210
Now we have uh, found a very good source from where we can take data.

52
00:03:40,530 --> 00:03:42,130
So I'll just add it over here.

53
00:03:42,450 --> 00:03:51,970
So first thing was private docs from startup Dot jobs and Monster.com.

54
00:03:55,810 --> 00:04:03,410
And second was this given URL from where we were able to identify our data for given bug bounty program.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Reconnaissance

1
00:00:00,480 --> 00:00:01,360
Uh, great.

2
00:00:01,760 --> 00:00:09,440
Now, participants, the first thing that we are going to do under reconnaissance or recon is going

3
00:00:09,440 --> 00:00:10,040
to be.

4
00:00:12,120 --> 00:00:16,480
Let me just change this to Python.

5
00:00:16,680 --> 00:00:17,120
Okay.

6
00:00:17,360 --> 00:00:24,280
The first thing that we are going to do in recon for a target like acorns is we are going to see what

7
00:00:24,280 --> 00:00:25,040
is their scope.

8
00:00:25,040 --> 00:00:29,560
And we saw that the scope says all of the targets are in scope.

9
00:00:29,560 --> 00:00:35,720
So this star, this this star basically means all subdomains are in scope.

10
00:00:36,160 --> 00:00:46,640
So we are going to now focus on how are the different techniques that we can utilize to perform reconnaissance.

11
00:00:47,000 --> 00:00:52,160
So the first thing that we are going to do is subdomain enumeration.

12
00:00:52,360 --> 00:01:00,590
But it is not going to be the usual subdomain enumeration that is always done, but new and effective

13
00:01:00,590 --> 00:01:08,390
ways that we can utilize and to do subdomain enumeration that can help us find those assets which are

14
00:01:08,390 --> 00:01:10,350
not found by others.

15
00:01:10,510 --> 00:01:15,870
So I will be showing you some practical examples here, uh, in which you would be able to see how to

16
00:01:15,870 --> 00:01:23,470
do effective subdomain enumeration to find those hidden assets that leads you to identify, uh, good

17
00:01:23,510 --> 00:01:23,990
bugs.

18
00:01:24,990 --> 00:01:29,030
So, uh, the approach that we are going to see right now is manual.

19
00:01:29,070 --> 00:01:35,990
The same approach is going to be then, uh, performed using an AI, lm as well.

20
00:01:36,190 --> 00:01:37,950
So we are going to set up.

21
00:01:38,590 --> 00:01:39,350
Uh olama.

22
00:01:39,350 --> 00:01:43,230
So I am I currently have olama running, as we can see over here.

23
00:01:43,390 --> 00:01:49,550
So we will be discussing more on what is Olama then how you can set up a local LM with open web UI,

24
00:01:49,670 --> 00:01:56,710
and then how you can utilize that to translate, uh, your commands that you would see send to the given

25
00:01:56,710 --> 00:02:03,940
target through your MCP server, as you can see over here, that lists down all of the given output

26
00:02:03,940 --> 00:02:10,780
for you automatically and prints that onto your web dashboard so you don't have to then remember commands.

27
00:02:10,780 --> 00:02:20,700
You just have to give prompts to your AI chatbot, which is completely running offline with the without

28
00:02:20,700 --> 00:02:23,140
any subscription or GPT API keys.

29
00:02:23,580 --> 00:02:25,260
Uh, a completely open source.

30
00:02:25,260 --> 00:02:32,340
And I will also show you how you can create more and more toolsets inside it that will help you, uh,

31
00:02:32,420 --> 00:02:38,580
make your MCP server much more, uh, larger and scalable.

32
00:02:38,780 --> 00:02:41,300
So we will be coming on this in just a moment.

33
00:02:41,340 --> 00:02:44,940
But before that, let's discuss about subdomain enumeration.

34
00:02:45,420 --> 00:02:51,780
We all know that there are multiple subdomain enumeration techniques like passive and active passive

35
00:02:51,820 --> 00:02:54,820
techniques utilizes past data sets.

36
00:02:56,860 --> 00:03:05,330
Past data sets and active techniques are basically on fresh or current data sets.

37
00:03:05,610 --> 00:03:15,770
So this passive techniques includes relying on various different data sources, search engines, etc.

38
00:03:15,770 --> 00:03:18,010
so that we can get data sets from them.

39
00:03:18,010 --> 00:03:19,730
This is usually faster.

40
00:03:20,250 --> 00:03:28,850
It is faster, but might you might end up missing finding a lot of things.

41
00:03:29,290 --> 00:03:34,290
So we could focus on active recall techniques.

42
00:03:34,450 --> 00:03:42,410
This is comparatively slower because you are tending to identify fresh assets fresh content for target,

43
00:03:42,410 --> 00:03:48,770
but this can be absolutely game changer for you even though it is slower.

44
00:03:48,770 --> 00:03:55,890
But it can help you identify a lot of useful stuff out there that can help you identify good bugs as

45
00:03:55,890 --> 00:03:56,250
well.

46
00:03:56,970 --> 00:04:04,200
So I'm going to show you one quick example of subdomain enumeration that usually is done using passive

47
00:04:04,200 --> 00:04:09,040
methods that most of the security researchers would do, which is faster.

48
00:04:09,240 --> 00:04:11,160
And why this is.

49
00:04:15,120 --> 00:04:23,760
Why this is not recommended every time or might miss out identification of some vulnerabilities.

50
00:04:23,800 --> 00:04:23,960
Okay.

51
00:04:23,960 --> 00:04:24,880
So I'll just write here.

52
00:04:24,920 --> 00:04:26,080
Not recommended.

53
00:04:26,080 --> 00:04:27,520
It is not like that.

54
00:04:27,520 --> 00:04:30,720
I totally discourage passive subdomain enumeration.

55
00:04:30,720 --> 00:04:36,440
It can definitely always add value to reconnaissance and attack surface mapping that you are doing.

56
00:04:36,440 --> 00:04:42,480
But if you only rely on that, then you are going to miss on pretty much a lot of new things.

57
00:04:42,840 --> 00:04:48,000
For an example, let's go to Google and search for a target.

58
00:04:50,880 --> 00:04:55,160
Yeah, I have prepared a mind map as well, so we would be following this with the AI tools that we

59
00:04:55,160 --> 00:04:57,160
would be developing and creating.

60
00:04:57,360 --> 00:04:58,240
We'll come to this in a.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:03,880
I'm going to go to a website which is Tata, AIG.

2
00:00:03,920 --> 00:00:09,160
Let's say here, in this case, we are not going to perform any attack or exploit or test case over

3
00:00:09,160 --> 00:00:09,480
here.

4
00:00:09,480 --> 00:00:14,720
I'm just going to show you basic subdomain enumeration for this given target.

5
00:00:15,040 --> 00:00:21,720
So when I go here on this target, uh, I'm going to use a passive subdomain enumeration technique.

6
00:00:21,720 --> 00:00:24,640
Maybe it could be sub finder.

7
00:00:24,680 --> 00:00:33,960
We all almost rely on sub finder because it has a very large, uh, data sources set with it.

8
00:00:34,080 --> 00:00:35,760
So I'm going to go to Sub Finder.

9
00:00:36,400 --> 00:00:41,680
Uh, there are more tools like sub list or -- find domain that you can use.

10
00:00:41,880 --> 00:00:46,440
Uh but usually sub finder contains a very large list of data sources.

11
00:00:46,840 --> 00:00:47,200
So.

12
00:00:50,120 --> 00:00:50,600
Yeah.

13
00:00:50,760 --> 00:00:56,000
Here we can see the total number of data sources that it uses.

14
00:00:58,000 --> 00:00:58,960
Features.

15
00:01:05,120 --> 00:01:08,760
Okay, maybe I can go to their documentation and from there I can show you.

16
00:01:08,760 --> 00:01:11,320
So it it has more than 30 data sources.

17
00:01:11,680 --> 00:01:16,600
Uh, this is what I have seen from their, uh, docs in the past.

18
00:01:16,920 --> 00:01:21,240
Uh, that can help you identify various different types of subdomains.

19
00:01:21,240 --> 00:01:23,720
So it's a fast passive subdomain enumeration tool.

20
00:01:24,040 --> 00:01:25,680
Uh, so we are going to run this.

21
00:01:25,680 --> 00:01:31,640
There are data sources, uh, that are present includes you can see in the screenshot VirusTotal site

22
00:01:31,680 --> 00:01:42,200
Dodger passive total security trail archive is search dot and uh Shodan Censys etc. for which you would

23
00:01:42,200 --> 00:01:46,880
have to definitely add some API keys as well that helps you identify more assets.

24
00:01:46,880 --> 00:01:49,440
But on to us out of the box.

25
00:01:50,000 --> 00:01:56,560
Uh, running sub Finder just out of the box from here will definitely hurt your results.

26
00:01:56,600 --> 00:01:57,400
Let's see how.

27
00:01:58,120 --> 00:02:02,040
So I'm going to go here and I'm going to run Sub Finder.

28
00:02:02,280 --> 00:02:05,850
This is just a very simple example on this targeted domain.

29
00:02:06,090 --> 00:02:13,450
I have ran this same experiment on various different types of targets, including bug bounty programs

30
00:02:13,450 --> 00:02:18,850
like Snapchat and Uber, and I have seen considerable amount of differences over there.

31
00:02:18,890 --> 00:02:20,850
Hence, I want to share this technique with you.

32
00:02:21,210 --> 00:02:29,090
So I'm going to take a target and save this results for this target into a file called as Tata AIG.

33
00:02:29,650 --> 00:02:32,730
Let's call it as passive dot txt and hit enter.

34
00:02:34,930 --> 00:02:42,570
If you want to see what are the data sources that it is using, you can also add a flag which is hyphen

35
00:02:42,570 --> 00:02:48,170
v verbose output so that you should be able to see what all data sources and from where the results

36
00:02:48,170 --> 00:02:50,930
is, is coming to this given file.

37
00:02:51,690 --> 00:02:52,090
Okay.

38
00:02:53,170 --> 00:02:55,610
So now we have this.

39
00:02:56,370 --> 00:02:57,490
Let me see.

40
00:02:57,530 --> 00:02:57,930
Yeah.

41
00:02:58,130 --> 00:03:02,370
So we can see the results are coming from search dot asset certificate transparency.

42
00:03:02,650 --> 00:03:06,370
Then we have hacker target Alienvault And.

43
00:03:09,410 --> 00:03:09,810
Yeah.

44
00:03:10,130 --> 00:03:16,490
So for example, like if we did not specify a API key so that was not used.

45
00:03:16,490 --> 00:03:20,690
And these are some of the targets where API key was not provided because of which the output did not

46
00:03:20,690 --> 00:03:21,090
come.

47
00:03:21,370 --> 00:03:25,610
As I said, we are using it out of the box not configuring anything.

48
00:03:25,890 --> 00:03:33,650
Now we can see we have found 218 subdomains for this given target in two seconds and 177 milliseconds.

49
00:03:33,850 --> 00:03:40,690
That is very good, because we already understood that passive data sets or passive recon techniques

50
00:03:40,690 --> 00:03:46,090
like sub finder for doing subdomain enumeration can be very faster, but it can sometimes hurt your

51
00:03:46,090 --> 00:03:46,730
results.

52
00:03:46,770 --> 00:03:47,650
Let us see how.

53
00:03:48,050 --> 00:03:54,210
Now from here we can do an endif, or we can do a comparison between the targets that we have found

54
00:03:54,250 --> 00:04:04,010
now and the assets that we might tend to identify later on with a customized word list.

55
00:04:04,290 --> 00:04:08,530
So I have a customized word list, uh, present with me.

56
00:04:08,810 --> 00:04:10,890
So I'm going to utilize that word list.

57
00:04:13,610 --> 00:04:15,250
Yeah, it's in the same folder.

58
00:04:15,370 --> 00:04:17,410
So let me just run that first.

59
00:04:22,330 --> 00:04:22,850
Okay.

60
00:04:22,890 --> 00:04:24,890
So I'm going to run a script.

61
00:04:24,890 --> 00:04:29,410
We can see a simple shell script is running onto the target that has been provided.

62
00:04:29,530 --> 00:04:37,210
And it is attempting to identify, uh, some hosts over here or subdomains over here, uh, for our

63
00:04:37,210 --> 00:04:38,610
reference that we can see.

64
00:04:39,010 --> 00:04:43,410
Now, let me just duplicate this tab quickly.

65
00:04:45,970 --> 00:04:46,370
Yeah.

66
00:04:46,570 --> 00:04:49,650
And let me show you the script, what it is running.

67
00:04:49,890 --> 00:04:51,690
So this is the shell script.

68
00:04:51,690 --> 00:05:00,570
We can we can run this shell script in the background and operate it with the help of an chat as well.

69
00:05:00,650 --> 00:05:04,050
So this is the chat view that we can see.

70
00:05:04,050 --> 00:05:11,050
We would be now, uh, seeing how you can set up your own LM model within Chat view, where you can

71
00:05:11,050 --> 00:05:16,050
simply give a command over here that can do the same thing for you in the background.

72
00:05:16,050 --> 00:05:21,170
You don't need to run the commands, you don't need to remember the commands as well.

73
00:05:21,170 --> 00:05:22,610
Simply with the help of prompts.

74
00:05:22,610 --> 00:05:27,730
You would be able to do the tasks, but it it would not be appropriate.

75
00:05:27,730 --> 00:05:34,090
If you don't see how things work in the back end or the background, uh, before automating them with,

76
00:05:34,250 --> 00:05:37,130
uh, lm uh, bot right now.

77
00:05:37,130 --> 00:05:43,290
So hence I'm showing you it raw and bare so that you understand it, how it functions in the background.

78
00:05:43,290 --> 00:05:50,410
And then we automate it very simply using an MCP server and uh, llama three okay.

79
00:05:50,450 --> 00:05:52,010
So now this this was the script.

80
00:05:52,010 --> 00:05:53,970
The script is basically very simple.

81
00:05:53,970 --> 00:06:03,290
It is just a loop where it is taking an input and running a host command and taking word words or subdomains

82
00:06:03,290 --> 00:06:04,050
from this file.

83
00:06:04,050 --> 00:06:05,610
Which is best DNS word list.

84
00:06:05,970 --> 00:06:13,420
So this word list currently contains around 95 lakh, uh, 44,000 words, as we can see over here.

85
00:06:13,420 --> 00:06:19,740
And it is simply trying to replace each word here in the place of sub and domain is what we have taken

86
00:06:19,740 --> 00:06:26,780
as an input, which I entered here, and it is simply doing a DNS resolver DNS resolving.

87
00:06:26,780 --> 00:06:30,340
Right now I am currently using Cloudflare DNS resolver.

88
00:06:30,340 --> 00:06:39,260
So I have set it up that in my DNS 1.1.1.1, because it is very fast and it is able to give me output

89
00:06:39,260 --> 00:06:40,660
as well as we see here.

90
00:06:41,260 --> 00:06:41,860
Awesome.

91
00:06:41,900 --> 00:06:48,060
Now participants, if you see from the output that we have just got, it has not also completed running

92
00:06:48,060 --> 00:06:48,260
this.

93
00:06:48,260 --> 00:06:54,700
We have just hardly done ran it for two minutes and I've got one of the assets that I can see which

94
00:06:54,700 --> 00:06:56,660
is spark.com.

95
00:06:56,900 --> 00:06:59,900
Now let's do a quick manual grep.

96
00:07:00,180 --> 00:07:05,380
You can also automate this with the help of endif or a new.

97
00:07:05,540 --> 00:07:07,420
We will also see how to do that.

98
00:07:07,420 --> 00:07:11,020
But as of now let's do a manual review that.

99
00:07:11,140 --> 00:07:13,540
Did we identify spark or no.

100
00:07:13,740 --> 00:07:14,860
So I'm going to say cat.

101
00:07:14,900 --> 00:07:18,260
Tata AIG passive results that we have.

102
00:07:18,460 --> 00:07:21,300
And I'm going to grep spark from this.

103
00:07:21,940 --> 00:07:22,860
Let's hit enter.

104
00:07:23,260 --> 00:07:26,420
And we saw that it does not contain spark.

105
00:07:26,460 --> 00:07:29,940
Let us try to manually search for it in this file.

106
00:07:31,100 --> 00:07:34,140
So I'm going to search control F spark.

107
00:07:34,660 --> 00:07:38,620
And we can see it does not contain spark domain into this.

108
00:07:38,940 --> 00:07:42,380
That means we could definitely miss this asset.

109
00:07:42,420 --> 00:07:44,820
Now let us see what is this asset running.

110
00:07:45,140 --> 00:07:47,340
So can we go here.

111
00:07:47,540 --> 00:07:47,980
Okay.

112
00:07:47,980 --> 00:07:52,700
So we can see that the asset is currently running a login portal.

113
00:07:52,820 --> 00:08:00,540
And we know as in security researcher login portals are gold mines because there could be issues like

114
00:08:00,540 --> 00:08:09,540
default credentials, the SQL injection authentication bypass broken access control and whatnot.

115
00:08:09,700 --> 00:08:12,060
We can identify on login panels.

116
00:08:12,260 --> 00:08:20,180
So this current login panel would have been definitely missed if I would have only relied on passive

117
00:08:20,180 --> 00:08:26,860
subdomain enumeration or a tool like sub finder, which is very common to see, uh, in the community

118
00:08:26,860 --> 00:08:30,540
that has been done by most of the researchers or beginners.

119
00:08:30,780 --> 00:08:31,220
Now.

120
00:08:33,300 --> 00:08:38,220
As we are running a shell script over here, uh, it is identifying the assets for us, but this is

121
00:08:38,220 --> 00:08:39,940
comparatively slower.

122
00:08:43,420 --> 00:08:48,820
Uh, can we see spark if we find if we use subdomain finder or any other tool?

123
00:08:48,820 --> 00:08:49,620
Definitely.

124
00:08:49,620 --> 00:08:49,940
Yes.

125
00:08:49,940 --> 00:08:51,580
We can definitely try that.

126
00:08:51,900 --> 00:08:59,420
Uh, in fact, subdomain finder is one of the data source that is used by sub finder to identify assets.

127
00:08:59,580 --> 00:08:59,980
So.

128
00:09:02,060 --> 00:09:07,820
Uh, so, uh, we are assuming that we won't be able to find it, but we can still try that out.

129
00:09:07,820 --> 00:09:12,180
So I'm going to go to sub domain sub domain finder.

130
00:09:13,540 --> 00:09:14,660
See 99.

131
00:09:25,180 --> 00:09:25,620
Okay.

132
00:09:25,620 --> 00:09:27,300
So we are going to look for assets.

133
00:09:27,660 --> 00:09:31,140
Uh, it was very fast because it utilizes passive techniques.

134
00:09:32,500 --> 00:09:35,340
So here is the output we can see.

135
00:09:35,540 --> 00:09:42,580
And uh I'm going to just export this given output from download CSV.

136
00:09:42,860 --> 00:09:45,780
Let's download the CSV and open the CSV.

137
00:09:53,940 --> 00:09:54,340
Okay.

138
00:09:54,380 --> 00:10:02,420
And we are able to see that there are only bunch of targets that we have got 25 targets.

139
00:10:02,620 --> 00:10:10,700
And when we try to do a search for spark, uh, it was not found, uh, the way that we were assuming

140
00:10:10,700 --> 00:10:12,900
that it wouldn't be found, uh, that was correct.

141
00:10:12,900 --> 00:10:16,420
And we saw that it was not found in this target list.

142
00:10:16,420 --> 00:10:19,710
So if we only rely again on Sub finder itself.

143
00:10:19,750 --> 00:10:24,270
You would not have been able to identify that given asset by search here.

144
00:10:24,750 --> 00:10:27,390
We can see this asset is again not found here.

145
00:10:27,990 --> 00:10:28,630
Uh, yes.

146
00:10:28,950 --> 00:10:36,630
Now, uh, this is evident that, uh, passive subdomain enumeration technique that is commonly used

147
00:10:36,630 --> 00:10:40,750
would miss out a lot of hidden assets for us.

148
00:10:40,990 --> 00:10:43,070
Here we get an added advantage.

149
00:10:43,270 --> 00:10:52,310
That other security researcher, uh, other security researchers who are only relying on subdomain techniques

150
00:10:52,310 --> 00:10:55,190
through passive mode might be missing a lot of assets.

151
00:10:55,430 --> 00:10:57,270
So that is the first prominent thing.

152
00:10:57,270 --> 00:10:58,790
I'm going to stop this now.

153
00:10:59,190 --> 00:11:05,470
Uh, as we can see for the assets that we have found, we could basically save this assets into a file

154
00:11:05,590 --> 00:11:12,030
and then combine the results of this file with the passive file so that we have a larger data set of

155
00:11:12,030 --> 00:11:12,670
results.

156
00:11:14,390 --> 00:11:16,790
We have larger data set of results.

157
00:11:16,790 --> 00:11:20,270
And then we could basically utilize that in our next step.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: LLM Tools Overview

1
00:00:00,440 --> 00:00:05,280
Now let us see the first technique that we have just understood.

2
00:00:05,720 --> 00:00:16,600
Now we will try to see how we can implement the relatively the same thing using an agent LM agent that

3
00:00:16,600 --> 00:00:17,840
is going to help us.

4
00:00:18,080 --> 00:00:21,640
So before that, we need to do some test bed setup.

5
00:00:21,640 --> 00:00:23,600
That is going to be helpful for us.

6
00:00:23,880 --> 00:00:29,680
And then we are going to automate the same task that we did manually with the LM agent.

7
00:00:30,400 --> 00:00:35,440
So for that there are various different types of tools that are available that we can use.

8
00:00:36,320 --> 00:00:42,800
And I am going to recommend some of the tools that I have used personally, because I have gone through

9
00:00:42,840 --> 00:00:50,560
most of the tools that are available out there, which either works onto a limited amount of searches

10
00:00:50,560 --> 00:00:57,320
that you can do, maybe with the free version or after which it allows you to not do, or some searches

11
00:00:57,320 --> 00:00:59,760
for a period of six hours, etc., etc..

12
00:01:00,000 --> 00:01:07,100
So a great IT tool is cloud desktop or cloud AI desktop that you can use.

13
00:01:07,300 --> 00:01:14,580
Uh, it allows um, it allows you to download this on Mac OS, windows, uh, both of the platform and

14
00:01:14,580 --> 00:01:16,020
you can start utilizing it.

15
00:01:16,020 --> 00:01:17,140
I have utilized this.

16
00:01:17,180 --> 00:01:25,620
It is the most easiest desktop LM agent that you can use and configure it within MCP, which is the

17
00:01:25,620 --> 00:01:33,420
Model Context Protocol server, which can then run commands on, on your system, uh, that you have.

18
00:01:35,020 --> 00:01:37,580
So you can utilize this very, very easily.

19
00:01:38,420 --> 00:01:42,660
Uh, this is currently not available for Linux as of now.

20
00:01:43,020 --> 00:01:46,340
So Klod cannot be used on Linux as of now.

21
00:01:46,340 --> 00:01:49,980
But don't worry, we are not going to use cloud AI.

22
00:01:50,500 --> 00:01:53,500
Instead we are going to use another tool.

23
00:01:53,620 --> 00:01:54,620
So what is cloud?

24
00:01:54,620 --> 00:01:57,540
Cloud is not like a VM, it's in software.

25
00:01:57,540 --> 00:01:59,340
So you can see here cloud.

26
00:01:59,500 --> 00:02:00,820
So I'm going to start it.

27
00:02:00,860 --> 00:02:11,480
It is basically uh Similar to ChatGPT, where you can run commands that you can see over here, like

28
00:02:11,480 --> 00:02:19,720
in the prompt, and it basically connects to it's one of the other model, which is cloud 3.7 sonnet.

29
00:02:19,960 --> 00:02:21,800
So I'm currently on a free plan.

30
00:02:21,800 --> 00:02:25,880
I've just installed this and where I can do some chats that I want.

31
00:02:25,920 --> 00:02:28,200
So maybe I can ask questions or whatever that I want.

32
00:02:28,240 --> 00:02:35,360
And it is going to connect to cloud 3.7, uh, which is one of its free model available for us to use.

33
00:02:35,360 --> 00:02:40,600
So I have downloaded the desktop application and, uh, I have logged into my account.

34
00:02:40,600 --> 00:02:44,760
You can see I'm currently I've just logged into my account and I'm onto a free plan.

35
00:02:44,760 --> 00:02:50,320
And I can ask questions like what is subdomain enumeration?

36
00:02:50,520 --> 00:02:52,320
Or maybe any questions like this.

37
00:02:52,680 --> 00:03:01,320
Uh, the problem is, uh, cloud AI desktop allows only, uh, specific searches that I can make onto

38
00:03:01,360 --> 00:03:02,400
its free plan.

39
00:03:02,720 --> 00:03:08,150
Here's the output that you're getting Trading post, which it is going to ask you to subscribe to its

40
00:03:08,150 --> 00:03:08,750
Pro version.

41
00:03:08,750 --> 00:03:09,110
Or maybe.

42
00:03:09,150 --> 00:03:19,870
It is going to wait for 5 to 6 hours, but it is very, very easy to use because it has an inbuilt configuration

43
00:03:19,870 --> 00:03:23,510
where you can set up MCP tools, as you can see over here.

44
00:03:23,510 --> 00:03:31,270
So we can analyze HTTP service, TLS configuration, do enumerate assets with tools like Go-buster or

45
00:03:31,270 --> 00:03:33,710
any other tools that you want for those endpoints.

46
00:03:33,710 --> 00:03:40,630
So I have set it up an external MCP server, and I have integrated that with cloud AI, which can help

47
00:03:40,630 --> 00:03:45,270
us do scanning of subdomain scanning of ports, fuzzing of endpoints, etc..

48
00:03:45,590 --> 00:03:51,030
So for example scan subdomains or hacker 1.com.

49
00:03:58,030 --> 00:03:58,550
Okay.

50
00:03:58,550 --> 00:04:00,030
So I'm going to allow this chat.

51
00:04:00,030 --> 00:04:02,190
And then it is going to find those.

52
00:04:03,110 --> 00:04:03,710
Uh yes.

53
00:04:03,750 --> 00:04:05,470
Currently my server is not running.

54
00:04:05,470 --> 00:04:11,050
Hence you would be able to see an error connection issue error, but that would run later on.

55
00:04:11,090 --> 00:04:13,370
Okay, so what is MCP.

56
00:04:13,410 --> 00:04:14,490
Yes, very good question.

57
00:04:14,490 --> 00:04:15,850
I'm going to answer that now.

58
00:04:15,850 --> 00:04:22,210
And I'm going to help make you understand that with the help of a diagram as well, that what is MCP,

59
00:04:22,450 --> 00:04:24,770
how it can be utilized for us.

60
00:04:24,810 --> 00:04:25,210
Okay.

61
00:04:25,850 --> 00:04:29,770
Uh, now we are going to dump this, not use this right now.

62
00:04:30,410 --> 00:04:36,170
Rather, we want to use something which is completely open source for us and does not.

63
00:04:39,010 --> 00:04:43,850
Uh, make us stop, uh, on the searches or queries that we make.

64
00:04:44,050 --> 00:04:46,650
Hence, we are going to go and use olama.

65
00:04:47,090 --> 00:04:56,850
So I'm going to say Olama Olama is supported on windows, Mac OS and Linux, so it is available for

66
00:04:56,850 --> 00:04:59,370
all of the major platforms that you see.

67
00:04:59,610 --> 00:05:03,850
So if anyone is using Linux then you can definitely download Olama.

68
00:05:03,850 --> 00:05:06,810
It is going to work absolutely fine on your system.

69
00:05:07,090 --> 00:05:13,230
So our first step is we are going to download and model which is Olama.

70
00:05:13,270 --> 00:05:14,150
What is Olama?

71
00:05:14,470 --> 00:05:19,230
Olama is an open source AI model.

72
00:05:19,230 --> 00:05:26,590
Or you can say large language model LLM, which is going to help us perform various different types

73
00:05:26,590 --> 00:05:29,030
of activities and tasks that we want.

74
00:05:29,670 --> 00:05:32,910
Now here these there are different types of models.

75
00:05:32,910 --> 00:05:41,270
When I go to model section where you can see for example, uh three Mistral Llama 3.3 and then llama

76
00:05:41,270 --> 00:05:42,830
3.1, etc..

77
00:05:43,030 --> 00:05:50,110
So for example, if you go to llama 3.1, it is the new state of the art model from meta, which is

78
00:05:50,110 --> 00:05:53,710
in sizes of 8 billion, 70,000,000,044.

79
00:05:53,750 --> 00:05:55,590
Zero 5 billion parameter.

80
00:05:55,870 --> 00:05:56,310
Now.

81
00:05:58,710 --> 00:06:01,150
What is this, uh, parameters.

82
00:06:01,150 --> 00:06:04,550
And how does this, uh, is helpful for us?

83
00:06:04,550 --> 00:06:10,730
So basically these models are trained on various different types of knowledge.

84
00:06:11,090 --> 00:06:17,970
It could be knowledge about maybe, uh, chemistry, physics, science, mathematics, stats, general

85
00:06:17,970 --> 00:06:18,650
knowledge.

86
00:06:19,290 --> 00:06:19,690
Okay.

87
00:06:19,730 --> 00:06:23,130
So all of that information has been trained onto a model.

88
00:06:23,250 --> 00:06:31,090
So if a model is 8 billion parameters, then you can say, uh, in a very simple layman language to

89
00:06:31,090 --> 00:06:36,330
understand that it has 8 billion parameters of knowledge that it has been trained on.

90
00:06:36,970 --> 00:06:45,090
When you see a larger size or parameter of knowledge, that means that model is more capable of doing

91
00:06:45,090 --> 00:06:52,010
things, but the size of its or the model and the vector database is going to be much larger.

92
00:06:52,210 --> 00:06:59,510
So for example, if I have a system which is not very powerful, then I could basically use llama 3.18

93
00:06:59,510 --> 00:07:01,770
billion parameter trained model.

94
00:07:02,010 --> 00:07:10,240
If I have a very large, uh, setup where I have a good GPU, CPU, maybe I have 128 gig, 128 GB of

95
00:07:10,240 --> 00:07:11,920
Ram and very nice GPU.

96
00:07:11,960 --> 00:07:16,840
I might use a 405 billion parameter size, so always recommended.

97
00:07:16,840 --> 00:07:21,400
Use a smaller size based on your system preferences that you have.

98
00:07:21,720 --> 00:07:27,840
So these are the three family of models that are trained on various different types of knowledge.

99
00:07:28,160 --> 00:07:30,160
Here is a comparison that we can see.

100
00:07:30,480 --> 00:07:35,640
So llama 3.1 uh four zero 5 billion parameters.

101
00:07:35,640 --> 00:07:43,360
You can see the statistics in comparison to other models like GPT four and cloud 3.5, which we just

102
00:07:43,360 --> 00:07:44,280
used right now.

103
00:07:44,560 --> 00:07:52,760
And we can see that this is almost very, very similar in terms of the benchmark results with other

104
00:07:52,760 --> 00:07:53,440
models.

105
00:07:53,600 --> 00:07:59,480
And it has outperformed as well other models in some of the parameters as you could see over here.

106
00:08:02,480 --> 00:08:02,840
Yes.

107
00:08:03,360 --> 00:08:13,100
So yeah, so basically it is a excellent model for our use case that we are going to use and we are

108
00:08:13,100 --> 00:08:14,700
going to configure it as well.

109
00:08:18,100 --> 00:08:25,020
So a very common question usually asked are, are there any cybersecurity specific train models that

110
00:08:25,020 --> 00:08:25,620
we have.

111
00:08:25,900 --> 00:08:32,300
Uh, so that we don't have to configure them from uh, maybe we don't have to do the rack based training

112
00:08:32,300 --> 00:08:33,780
or fine tuning of this.

113
00:08:33,860 --> 00:08:37,260
So, uh, most likely the answer is no.

114
00:08:37,260 --> 00:08:37,700
For that.

115
00:08:37,700 --> 00:08:41,620
We don't have any cybersecurity specific trained models out there.

116
00:08:41,860 --> 00:08:42,340
Yes.

117
00:08:43,060 --> 00:08:52,260
Uh, there are, uh, a lot of efforts that are being made right now where researchers and other scholars

118
00:08:52,260 --> 00:08:58,820
are trying to train the models, and they are also ready to share those model vector databases, uh,

119
00:08:58,980 --> 00:09:03,980
with the community, where you don't have to do the training of these models from scratch.

120
00:09:04,460 --> 00:09:08,140
So, uh, yes, that is still happening, evolving.

121
00:09:08,300 --> 00:09:15,880
And, uh, we would be able to basically utilize that, uh, as well in the back end, uh, later on,

122
00:09:17,320 --> 00:09:19,880
uh, now, what does GPT use in the back end?

123
00:09:19,920 --> 00:09:21,600
Yes, it uses Pentest.

124
00:09:21,600 --> 00:09:23,560
GPT uses OpenAI.

125
00:09:24,120 --> 00:09:26,280
Um, it uses OpenAI.

126
00:09:26,800 --> 00:09:32,760
And there are various types of GPT models available or plugins, you can say, which are being created

127
00:09:32,760 --> 00:09:33,920
in GPT.

128
00:09:34,480 --> 00:09:43,480
And you can also, uh, view and explore various new GPT models or plugins that has been created on

129
00:09:43,480 --> 00:09:44,080
OpenAI.

130
00:09:45,080 --> 00:09:54,840
So OpenAI is again one of the most widely and famous used, uh, chat based LLM platform that runs on

131
00:09:54,840 --> 00:09:56,640
GPT four, uh, model.

132
00:09:56,680 --> 00:10:03,160
GPT four is the most successful and current used model, but it is not open source.

133
00:10:03,160 --> 00:10:06,080
That means you cannot train it.

134
00:10:06,080 --> 00:10:10,320
You cannot, uh, do rag modeling with it.

135
00:10:10,320 --> 00:10:14,260
Or maybe you cannot, uh, modify Instructions.

136
00:10:14,300 --> 00:10:16,820
System instructions etc. that you want with it.

137
00:10:16,820 --> 00:10:20,420
But with other open source models like llama, you can do that.

138
00:10:20,420 --> 00:10:23,700
You can do a lot of variety of tasks and things with it.

139
00:10:23,740 --> 00:10:25,260
Hence we are going to use llama.

140
00:10:25,700 --> 00:10:28,260
Okay, so we understood about what is llama.

141
00:10:28,300 --> 00:10:33,580
Now we are going to uh download and set up this quickly.

142
00:10:33,860 --> 00:10:35,860
So let's go to download.

143
00:10:36,420 --> 00:10:39,100
Click on Mac OS and click on download for Mac OS.

144
00:10:41,460 --> 00:10:42,740
It is going to download.

145
00:10:42,900 --> 00:10:44,940
I have already downloaded this.

146
00:10:44,940 --> 00:10:48,020
You just need to download it and run it.

147
00:10:48,780 --> 00:10:54,460
The next step of installation process is fairly simple and it is automated.

148
00:10:54,500 --> 00:11:00,260
Okay, so once this has been downloaded you are going to see an icon like this, uh, where you can

149
00:11:00,260 --> 00:11:03,180
see, oh llama has been successfully installed and running.

150
00:11:03,660 --> 00:11:05,060
Uh, unfortunately.

151
00:11:05,100 --> 00:11:09,980
Oh llama is completely CLI command line interface.

152
00:11:09,980 --> 00:11:12,460
It does not have a GUI interface.

153
00:11:12,740 --> 00:11:13,220
Okay.

154
00:11:13,260 --> 00:11:15,810
That means if you want to interact with Obama.

155
00:11:15,850 --> 00:11:19,730
If you've successfully started it, then you are going to give commands to it.

156
00:11:24,970 --> 00:11:28,410
Okay, so wait, I'm already running olama.

157
00:11:29,050 --> 00:11:29,490
Yeah.

158
00:11:32,170 --> 00:11:36,290
Okay, so I'm going to say Olama run llama three.

159
00:11:36,290 --> 00:11:39,130
So I'm currently running the llama three default model.

160
00:11:39,490 --> 00:11:43,650
I can also ask what is the version by asking giving the version command.

161
00:11:45,490 --> 00:11:45,890
Okay.

162
00:11:46,130 --> 00:11:50,010
What is the version of the model?

163
00:11:55,530 --> 00:11:58,850
And you can see the output that we are getting currently on my screen.

164
00:11:58,890 --> 00:11:59,330
Okay.

165
00:11:59,330 --> 00:12:06,650
So what we are doing we are currently running llama three model as we see over here.

166
00:12:10,930 --> 00:12:12,530
With the help of llama command.

167
00:12:12,530 --> 00:12:13,770
So this command is very simple.

168
00:12:13,970 --> 00:12:15,410
Llama llama three.

169
00:12:15,930 --> 00:12:17,990
Uh let me just start it once again.

170
00:12:19,190 --> 00:12:22,790
So I'm going to say slash bye to exit from the model.

171
00:12:23,470 --> 00:12:23,910
Okay.

172
00:12:24,030 --> 00:12:25,470
So how to start the model.

173
00:12:25,470 --> 00:12:28,470
Simply after installation you can say oh llama.

174
00:12:30,710 --> 00:12:31,310
Run.

175
00:12:31,710 --> 00:12:37,390
Or if you type in hit enter you will be able to see the commands available serve, create, show, run,

176
00:12:37,430 --> 00:12:37,870
etc..

177
00:12:37,870 --> 00:12:41,870
So I'm going to say Llama Llama three.

178
00:12:42,910 --> 00:12:48,830
And once you do that you will be able to see a CLI interface like this where you can say, what can

179
00:12:48,830 --> 00:12:49,950
you do for me?

180
00:12:50,110 --> 00:12:51,830
What can you do for me?

181
00:12:52,230 --> 00:12:55,190
And it will reply, uh, I can do a range of tasks.

182
00:12:55,190 --> 00:12:56,510
Here are some of the example.

183
00:12:56,550 --> 00:13:01,110
Ask, answer, question, generate ideas, summarize content and participants.

184
00:13:01,110 --> 00:13:03,910
Everything that you see currently is happening offline.

185
00:13:03,910 --> 00:13:08,990
So it's in local uh model that we have currently.

186
00:13:09,030 --> 00:13:13,390
It is not requiring any kind of internet to run the commands.

187
00:13:13,390 --> 00:13:18,630
Everything is happening totally offline uh, and locally into your system.

188
00:13:18,670 --> 00:13:18,830
Okay.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:06,440
I can ask more questions to this, but this looks a little weird that interacting onto a terminal,

2
00:00:06,720 --> 00:00:11,120
I'm not able to get a formatted or justified output.

3
00:00:11,520 --> 00:00:17,440
Uh, as we as you, as we see over here, and it's looking very, uh, untidy.

4
00:00:17,760 --> 00:00:23,040
So let us try to set up a web chat GPT like interface for this.

5
00:00:23,280 --> 00:00:28,400
So to do that we are going to go and use open web UI.

6
00:00:29,920 --> 00:00:31,280
What is open Web UI.

7
00:00:31,400 --> 00:00:37,360
So open web UI is a web front end front end dashboard.

8
00:00:37,800 --> 00:00:46,720
Uh, that is going to be helpful for us, which is going to give the UI to the CLI model that we have.

9
00:00:47,000 --> 00:00:55,640
So we can see user friendly interface which supports Obama and other platforms or models.

10
00:00:56,200 --> 00:00:58,240
So uh, we are going to set this up.

11
00:00:58,240 --> 00:01:05,320
This is going to give you a similar kind of interface that you have with ChatGPT, and so that you have

12
00:01:05,320 --> 00:01:10,040
a similar interface and similar web UI.

13
00:01:10,480 --> 00:01:12,480
So we are going to set this up now.

14
00:01:15,480 --> 00:01:15,760
Too.

15
00:01:15,800 --> 00:01:20,760
So to set this up where there are various different types of commands or ways that you can set this

16
00:01:20,760 --> 00:01:27,240
up, for example, uh, with Python's pip library, you can install it and then you can serve it.

17
00:01:27,240 --> 00:01:31,760
Or if you want to start it with a Docker container, you can also start it with Docker container.

18
00:01:31,960 --> 00:01:34,840
So I already have it installed onto my computer.

19
00:01:35,120 --> 00:01:39,240
Then we can simply start this using the docker command.

20
00:01:39,360 --> 00:01:43,480
So you can you can see over here we are going to run the docker command.

21
00:01:44,000 --> 00:01:48,200
Uh detached mode port 3000 is going to be exposed from internal service.

22
00:01:48,720 --> 00:01:52,000
And 8080 is the port that is going to be used.

23
00:01:52,400 --> 00:01:55,640
And uh, we are going to run this.

24
00:01:57,040 --> 00:02:06,000
And from its official source it is going to download the Open Web UI files and start the container and

25
00:02:06,000 --> 00:02:07,320
assign it a name as well.

26
00:02:07,520 --> 00:02:08,240
Very nice.

27
00:02:08,240 --> 00:02:11,080
So I'm going to run this, uh, copy this command.

28
00:02:11,120 --> 00:02:16,120
Go to your terminal, make sure that Obama is up and running.

29
00:02:16,400 --> 00:02:18,600
So let this terminal open like this.

30
00:02:18,600 --> 00:02:21,160
And you can then run the command.

31
00:02:21,440 --> 00:02:23,960
So I'm going to run this command here and hit enter.

32
00:02:24,320 --> 00:02:28,880
And you can see there's a conflict because there is a container already with that name.

33
00:02:29,120 --> 00:02:33,520
Because before the class I have already run this earlier.

34
00:02:33,800 --> 00:02:36,240
So you can see the container name is open Web UI.

35
00:02:36,280 --> 00:02:38,560
It has been running from last four hours.

36
00:02:38,800 --> 00:02:41,160
And we can simply click on this.

37
00:02:41,160 --> 00:02:46,760
So this is Docker Desktop because I choose to run web UI in a Docker container.

38
00:02:46,920 --> 00:02:50,400
If you want you can run it outside as well directly.

39
00:02:50,440 --> 00:02:50,840
Okay.

40
00:02:52,600 --> 00:02:53,160
Yes.

41
00:02:53,160 --> 00:02:58,200
So let me first close cloud because we don't want to use it.

42
00:02:58,520 --> 00:02:58,920
Yeah.

43
00:02:58,960 --> 00:03:00,520
Now I can simply go to this.

44
00:03:01,920 --> 00:03:06,280
Your endpoint and awesome participants.

45
00:03:06,600 --> 00:03:18,400
We have our own, uh, setup of and local local LLM available for us with a GUI which is currently using

46
00:03:18,440 --> 00:03:19,880
llama three.

47
00:03:19,920 --> 00:03:22,280
8 billion parameter model available for us.

48
00:03:22,280 --> 00:03:24,000
The size is 4.3 GB.

49
00:03:24,560 --> 00:03:28,520
Uh, if you want to use a larger model, you can see the size is 24 GB.

50
00:03:28,560 --> 00:03:30,200
You can use that as well.

51
00:03:30,200 --> 00:03:33,360
So if you choose that, the model will start downloading automatically.

52
00:03:33,720 --> 00:03:40,080
And if you have the sufficient amount of, uh, system requirements or hard disk space, you can utilize

53
00:03:40,080 --> 00:03:40,480
this.

54
00:03:40,480 --> 00:03:44,520
I'm going to keep it on a small default 8 billion parameter model as of now.

55
00:03:45,080 --> 00:03:50,200
Uh, because we are going to use very we are going to use the natural natural language processing of

56
00:03:50,200 --> 00:03:51,040
this model.

57
00:03:51,040 --> 00:03:59,520
But in addition to that, our main task is to set up the MCP, uh, protocol with with this so that

58
00:03:59,520 --> 00:04:06,360
it can, uh, basically get capabilities to interact with my system and other toolsets that we have.

59
00:04:06,360 --> 00:04:08,360
So the basic model is also fine.

60
00:04:09,280 --> 00:04:09,720
Yes.

61
00:04:10,120 --> 00:04:18,000
So now once you have selected the model, uh, you, you would you would be prompted to set up a username

62
00:04:18,000 --> 00:04:18,480
and password.

63
00:04:18,480 --> 00:04:20,920
So I've already set it up a username and password.

64
00:04:21,320 --> 00:04:23,520
And I have logged in right now as you can see.

65
00:04:23,720 --> 00:04:28,200
So once you start this you should be able to see a portal like this.

66
00:04:28,480 --> 00:04:29,440
Please sign in.

67
00:04:30,440 --> 00:04:32,280
Uh, it will ask you to create a password.

68
00:04:32,280 --> 00:04:34,000
Everything is happening locally.

69
00:04:34,000 --> 00:04:40,000
You can see everything is happening offline and you don't require internet after you have downloaded

70
00:04:40,000 --> 00:04:40,520
the model.

71
00:04:40,520 --> 00:04:42,720
So for downloading the model, the internet is required.

72
00:04:42,720 --> 00:04:44,320
After that, no internet is required.

73
00:04:44,800 --> 00:04:51,120
You can see you can capture images, upload files, uh, use the code interpreter.

74
00:04:51,120 --> 00:04:55,680
So you have to input your code into the ticks back ticks.

75
00:04:56,160 --> 00:04:58,520
And it can interpret that for you as well.

76
00:04:58,760 --> 00:05:04,710
Or uh, you can also record your voice and do a lot of things with Lama3 right now.

77
00:05:05,070 --> 00:05:11,230
Now, uh, before we do anything with the web UI interface right now, there are some settings that

78
00:05:11,230 --> 00:05:12,110
we need to do.

79
00:05:12,430 --> 00:05:14,790
So we will simply go to the admin panel.

80
00:05:16,030 --> 00:05:16,550
Okay.

81
00:05:16,590 --> 00:05:21,110
So I have created a user I signed up when this started.

82
00:05:21,110 --> 00:05:24,630
You just need to choose an email and a password.

83
00:05:24,950 --> 00:05:26,630
Now we will go to settings.

84
00:05:26,750 --> 00:05:32,110
So once you go to the settings you have to go to the model.

85
00:05:32,270 --> 00:05:35,030
And currently you can see Mistral and Llama three.

86
00:05:35,030 --> 00:05:38,670
Both are the models that are currently enabled for us to use.

87
00:05:39,070 --> 00:05:43,110
I'll go to documents and this might be default for default.

88
00:05:43,310 --> 00:05:44,750
Uh, disabled for you.

89
00:05:46,030 --> 00:05:49,870
Content extraction engine and PDF extract images.

90
00:05:49,870 --> 00:05:50,990
This would be off.

91
00:05:50,990 --> 00:05:53,950
Please turn this on because that is going to be helpful for us.

92
00:05:54,350 --> 00:05:57,110
If you want you can do the integration with Google Drive as well.

93
00:05:57,430 --> 00:06:03,870
So automatically all the documents in your Google Drive will also be synced with your, uh, current

94
00:06:03,870 --> 00:06:04,670
open web UI.

95
00:06:05,150 --> 00:06:13,470
And your model, which is llama 3.1, would be able to read your documents from your drive, any specific

96
00:06:13,470 --> 00:06:20,550
folder that you want to specify, and then use, uh, those documents to extract information and help

97
00:06:20,550 --> 00:06:21,670
you with if you want.

98
00:06:22,030 --> 00:06:24,870
I'm not going to do that as of now, but that can also be done.

99
00:06:24,910 --> 00:06:30,750
You can also choose the maximum upload, minimum upload size of documents that you want to give to your

100
00:06:30,750 --> 00:06:31,270
model.

101
00:06:31,870 --> 00:06:35,150
Next, go to Web search and you can enable the web search as well.

102
00:06:35,150 --> 00:06:39,830
So your model gains capabilities to search the internet if required.

103
00:06:40,030 --> 00:06:48,590
Uh, if you plan to use the model app offline, then this feature can be turned off.

104
00:06:48,630 --> 00:06:53,710
Like we don't need to turn that on, but if you want that, your model should also have the capabilities

105
00:06:53,710 --> 00:07:00,190
to, uh, search queries on Google search engine or other search engines.

106
00:07:00,190 --> 00:07:00,790
You can choose this.

107
00:07:00,790 --> 00:07:08,110
There are multiple search engines like Bing, brave, Google, etc. you need the API key of all of these

108
00:07:08,430 --> 00:07:09,470
search engines.

109
00:07:09,470 --> 00:07:12,910
So for example, if I go to brave, I need to enter the brave API key.

110
00:07:13,070 --> 00:07:15,950
You can get that for absolutely free and set this up.

111
00:07:16,070 --> 00:07:17,310
Currently I don't want that.

112
00:07:17,310 --> 00:07:19,790
So I'm not going to make any changes over there.

113
00:07:20,790 --> 00:07:22,590
Uh code execution you have to enable.

114
00:07:22,590 --> 00:07:33,750
Yes because I want model, uh, my llama three model to have the capabilities to execute code on the

115
00:07:33,750 --> 00:07:39,390
system so that we have any commands that we want to run so that commands can be run in the background.

116
00:07:41,310 --> 00:07:46,270
In addition to this, in the interface part, you can see if you want to change any interface changes

117
00:07:46,270 --> 00:07:53,470
or any prompts, etc. if you want your model to behave like a specific expert, then you can do those

118
00:07:53,470 --> 00:07:54,110
things over here.

119
00:07:54,110 --> 00:07:55,950
But as of now, that is not required.

120
00:07:56,110 --> 00:07:57,630
When it is when it would be required.

121
00:07:57,630 --> 00:07:58,510
I will let you know.

122
00:07:58,830 --> 00:08:01,750
Let's go to New chat and let's start with the chat.

123
00:08:02,590 --> 00:08:04,790
So I'm going to send my first question.

124
00:08:06,190 --> 00:08:09,710
Who are you and how can you help me?

125
00:08:10,390 --> 00:08:18,350
So so we can see, uh, this is the exact same thing that we were doing earlier here.

126
00:08:20,430 --> 00:08:22,270
Um, yeah.

127
00:08:22,310 --> 00:08:22,710
Here.

128
00:08:23,030 --> 00:08:27,590
So the same thing that we did on the CLI, now we are doing it on the GUI.

129
00:08:27,990 --> 00:08:34,030
So all of the questions that you ask, you would be able to get the output on the front end on the web

130
00:08:34,070 --> 00:08:36,470
UI, as you can see over here.

131
00:08:42,190 --> 00:08:43,350
Uh, no.

132
00:08:43,350 --> 00:08:45,590
So llama model by default.

133
00:08:46,590 --> 00:08:47,750
Uh, a very common question.

134
00:08:47,750 --> 00:08:50,830
Llama model by default does not connect to the internet.

135
00:08:51,390 --> 00:08:53,070
Uh, for doing searches for you.

136
00:08:53,110 --> 00:08:55,270
It runs totally offline.

137
00:08:55,270 --> 00:09:01,230
If you want to enhance the capabilities, then then you can use the open web UI to explicitly allow

138
00:09:01,230 --> 00:09:06,110
it to search the web or search engines like that.

139
00:09:07,870 --> 00:09:11,190
Otherwise, everything happens completely offline over here.

140
00:09:11,230 --> 00:09:16,030
Now this was my first question, and we can see we have got a similar kind of ChatGPT interface that

141
00:09:16,030 --> 00:09:19,470
is running, but everything is running offline completely for me.

142
00:09:19,830 --> 00:09:32,710
And yes, so our first initial setup of the lab of setting up the LLM, which is llama, and setting

143
00:09:32,710 --> 00:09:36,790
up an open web UI interface on it, is successfully completed.

144
00:09:37,310 --> 00:09:42,350
I hope all participants have understood this of how you can configure this locally.

145
00:09:42,670 --> 00:09:51,830
This does not require any kind of internet connectivity or uh, any subscription etc. to run.

146
00:09:51,870 --> 00:09:58,790
It runs absolutely offline, uh, with no requirement of web search or engine.

147
00:09:59,190 --> 00:10:02,270
Uh, if you do not explicitly granted permission.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:00,560
Awesome.

2
00:00:00,960 --> 00:00:02,880
Now we also understood about.

3
00:00:05,440 --> 00:00:06,880
The MCP protocol.

4
00:00:07,200 --> 00:00:16,520
So we are going to now utilize the MCP protocol to perform a given practical that helps us do automation.

5
00:00:17,040 --> 00:00:28,160
So before doing that with open web UI and just matter of fact for all participants till now on Open

6
00:00:28,160 --> 00:00:38,800
Web UI, no one in the community has ever done this setup because only seven days ago this feature was

7
00:00:38,800 --> 00:00:40,440
released in Open Web UI.

8
00:00:40,600 --> 00:00:49,320
So we would be the first ones who are going to set up the MCP protocol with Open Web UI for reconnaissance

9
00:00:49,320 --> 00:00:50,560
for cybersecurity.

10
00:00:50,760 --> 00:00:59,280
There are some, uh, attempts that have been done in past in which reconnaissance tools have been set

11
00:00:59,280 --> 00:01:00,840
up with cloud AI.

12
00:01:01,160 --> 00:01:08,900
But as I mentioned in express last time, Claude I MCP server has restrictions.

13
00:01:09,020 --> 00:01:14,660
That is, you can only do 15 to 30 queries, after which you have to wait for six hours.

14
00:01:14,700 --> 00:01:21,180
Okay, so first I will show you Claude I as well, and then we'll move to the completely free version

15
00:01:21,180 --> 00:01:22,140
on Open Web UI.

16
00:01:22,180 --> 00:01:22,580
Okay.

17
00:01:22,820 --> 00:01:26,820
So I'm going to start Claude I.

18
00:01:26,980 --> 00:01:27,940
So what is Claudia?

19
00:01:27,980 --> 00:01:29,580
Claudia is basically.

20
00:01:34,780 --> 00:01:36,420
An AI agent.

21
00:01:36,820 --> 00:01:40,700
Uh, you can download it for your system so you can say Claude AI desktop.

22
00:01:40,860 --> 00:01:46,940
Quickly download Claudia from here for Mac OS.

23
00:01:46,980 --> 00:01:50,820
I click for Mac OS and you can download it and install it.

24
00:01:50,820 --> 00:01:55,660
So once you start it, you can see this is how Claudia would look like I have installed I have logged

25
00:01:55,660 --> 00:02:00,860
in with my free plan right now, and currently I'm using Claude 3.7 sonnet.

26
00:02:00,860 --> 00:02:02,910
So this is the current model.

27
00:02:03,310 --> 00:02:05,230
Now participants are.

28
00:02:05,270 --> 00:02:11,350
It is important for me to show you how to use cloud AI, MCP server as well so that if you want to do

29
00:02:11,390 --> 00:02:17,470
your own tweaking, research and make your own tools that are compatible with cloud AI, you should

30
00:02:17,470 --> 00:02:18,270
be able to do it.

31
00:02:18,270 --> 00:02:18,670
Okay.

32
00:02:18,950 --> 00:02:20,910
So let's see this how to do it.

33
00:02:21,110 --> 00:02:23,550
But as I said, it comes with a drawback.

34
00:02:23,950 --> 00:02:26,830
You you are only allowed to do limited search queries.

35
00:02:26,830 --> 00:02:31,710
But again as I said it is important for you to know how it works.

36
00:02:31,710 --> 00:02:34,990
Hence I'm going to show you first this and then we go to Open web UI.

37
00:02:35,270 --> 00:02:35,790
Okay.

38
00:02:35,830 --> 00:02:37,070
So first things first.

39
00:02:37,310 --> 00:02:42,270
Uh, when you start cloud AI, simply go to the settings of cloud AI.

40
00:02:42,750 --> 00:02:47,270
So once you go to the settings tab this is how you should be able to see this.

41
00:02:47,630 --> 00:02:54,870
Now you need to go to the developer menu developer menu click on Edit Config okay.

42
00:02:55,070 --> 00:03:00,750
So once you click on edit config there will be a cloud desktop config dot JSON file.

43
00:03:00,750 --> 00:03:03,210
This is your first step Okay.

44
00:03:03,250 --> 00:03:04,610
Please open that file.

45
00:03:05,010 --> 00:03:09,330
Once you open that file, you should be able to see that the file is currently empty.

46
00:03:09,690 --> 00:03:10,650
It should be empty.

47
00:03:10,690 --> 00:03:15,610
Let me zoom this so you will only see this two curly brackets.

48
00:03:15,610 --> 00:03:16,410
Or maybe nothing.

49
00:03:16,410 --> 00:03:17,490
It will be empty.

50
00:03:17,810 --> 00:03:21,050
You need to paste this command in this file.

51
00:03:21,090 --> 00:03:21,530
Okay.

52
00:03:22,130 --> 00:03:23,810
Now what does this command do.

53
00:03:24,210 --> 00:03:32,090
This command basically is telling cloud AI that we have an external MCP server.

54
00:03:32,090 --> 00:03:33,050
One server okay.

55
00:03:33,090 --> 00:03:33,970
This is one server.

56
00:03:33,970 --> 00:03:35,570
We can have multiple servers.

57
00:03:36,250 --> 00:03:39,410
The MCP server name is external attacker MCP.

58
00:03:39,410 --> 00:03:41,050
This is the name okay.

59
00:03:42,050 --> 00:03:46,010
The command to start the server is by using Python three.

60
00:03:46,290 --> 00:03:49,450
And the arguments is this.

61
00:03:49,650 --> 00:03:53,370
This argument basically means start this Python file okay.

62
00:03:53,370 --> 00:03:58,370
So this is in Python flask application that is going to be started with Python three.

63
00:03:58,370 --> 00:04:04,580
And this is the name of the MCP protocol sorry MCP uh application.

64
00:04:04,620 --> 00:04:06,380
The name is external attacker.

65
00:04:07,260 --> 00:04:09,380
It is going to be started with Python three.

66
00:04:09,380 --> 00:04:11,660
And this is the path where the file is.

67
00:04:11,700 --> 00:04:12,380
Is this clear?

68
00:04:12,380 --> 00:04:13,300
Participants.

69
00:04:13,460 --> 00:04:14,860
Very simple to understand.

70
00:04:16,260 --> 00:04:17,020
Please let me know.

71
00:04:17,020 --> 00:04:18,420
Are you all with me so far?

72
00:04:22,020 --> 00:04:26,900
Okay, I'm going to give you this project code as well so that you can use it.

73
00:04:26,900 --> 00:04:27,380
Okay.

74
00:04:27,540 --> 00:04:30,420
Now let me just go to go to that path first.

75
00:04:40,940 --> 00:04:41,460
Okay.

76
00:04:41,460 --> 00:04:46,900
So once we go to that path participants, we can see there are multiple files over here.

77
00:04:47,140 --> 00:04:51,620
Out of all of these files, only two files are important for us to understand.

78
00:04:51,620 --> 00:04:52,060
Okay.

79
00:04:52,260 --> 00:04:57,620
First is the external attacker app.py and external attacker mcp.py.

80
00:05:00,340 --> 00:05:02,260
Uh, what is the project code all about?

81
00:05:02,420 --> 00:05:03,180
Uh, yes.

82
00:05:03,180 --> 00:05:07,560
So what we are going to do is we are going to tell Claudia.

83
00:05:09,600 --> 00:05:11,440
We are going to give a prompt.

84
00:05:11,440 --> 00:05:11,760
Okay.

85
00:05:11,760 --> 00:05:14,000
So so it basically works like this.

86
00:05:24,480 --> 00:05:24,920
Okay.

87
00:05:24,960 --> 00:05:34,480
Claud, I or I would say any LM agent is we are going to basically give a prompt.

88
00:05:34,480 --> 00:05:38,400
So let me say user gives a prompt.

89
00:05:41,720 --> 00:05:42,200
Okay.

90
00:05:42,600 --> 00:05:49,800
Uh, when a user gives a prompt to the agent, let's say the prompt is do subdomain enumeration okay.

91
00:05:49,920 --> 00:05:57,040
When we say do subdomain enumeration on tesla.com that prompt has been given to cloud AI.

92
00:05:57,680 --> 00:05:59,840
Now it's a natural language prompt.

93
00:05:59,840 --> 00:06:05,730
It can be given in any different forms of language as well, or maybe another sentence, etc..

94
00:06:05,970 --> 00:06:13,570
Now what what Claudia does is it understands the prompt that do some subdomain enumeration for tesla.com.

95
00:06:14,010 --> 00:06:23,290
And the agent is going to now give this prompt that it has understood, based on which it is now going

96
00:06:23,290 --> 00:06:28,210
to check if there is a MCP server connected to it.

97
00:06:28,770 --> 00:06:34,610
And as it finds that yes, there is an MCP server, one which has been connected, which is this in

98
00:06:34,610 --> 00:06:35,370
our case.

99
00:06:42,170 --> 00:06:42,570
Yeah.

100
00:06:43,250 --> 00:06:44,850
External attacker MCP.

101
00:06:44,850 --> 00:06:48,050
This is the MCP server, one that has been connected.

102
00:06:48,370 --> 00:06:55,570
So now what it is going to do is it is going to check in the MCP server code.

103
00:06:56,250 --> 00:07:00,650
What to do when a user asks to do subdomain enumeration.

104
00:07:00,690 --> 00:07:01,170
Okay.

105
00:07:01,210 --> 00:07:09,710
So now now here we are going to see the command of what to do when a user wants to do a subdomain enumeration.

106
00:07:09,750 --> 00:07:10,110
Okay.

107
00:07:10,390 --> 00:07:14,910
So we are going to open the file external attacker app dot pi.

108
00:07:15,350 --> 00:07:18,070
So this is in Python flask application.

109
00:07:18,350 --> 00:07:20,870
It has these many tools support.

110
00:07:20,870 --> 00:07:25,590
We are going to utilize sub finder or sub for doing subdomain enumeration.

111
00:07:25,630 --> 00:07:26,030
Okay.

112
00:07:26,670 --> 00:07:31,710
Now let us go to let's skip all of this okay.

113
00:07:31,790 --> 00:07:39,230
So there is a root which means what the LM agent does is it sends a Post request to a run endpoint.

114
00:07:39,670 --> 00:07:42,630
Now API run endpoint.

115
00:07:42,630 --> 00:07:45,790
And it is going to ask to do something okay.

116
00:07:46,190 --> 00:07:50,310
And it is going to ask to okay let's skip all of this.

117
00:08:02,910 --> 00:08:03,350
Yeah.

118
00:08:03,630 --> 00:08:09,120
So here we can see a prompt Its arguments and a command.

119
00:08:09,160 --> 00:08:13,320
Okay, so scan target domains for sub domain using sub finder binary.

120
00:08:13,440 --> 00:08:20,440
So if this prompt is being given or a similar prompt is given then the arguments will be taken in consideration.

121
00:08:20,440 --> 00:08:22,200
The first argument is the target.

122
00:08:22,440 --> 00:08:29,200
These arguments are basically given to run the given program that is sub finder.

123
00:08:29,200 --> 00:08:33,600
So we are currently using this sub finder binary to generate sub domains.

124
00:08:33,840 --> 00:08:39,320
So one one first or the first thing is the target, second is the domain.

125
00:08:40,320 --> 00:08:44,960
And third is the number of concurrent threads that are going to be utilized to do this task.

126
00:08:45,000 --> 00:08:45,400
Okay.

127
00:08:46,040 --> 00:08:49,480
And next is to find open ports and so on other things.

128
00:08:49,480 --> 00:08:53,920
But we'll stick to the first thing only for simplicity as of now.

129
00:08:53,920 --> 00:08:59,640
So we understood how the code has been written over here which is going to help do subdomain enumeration.

130
00:08:59,680 --> 00:09:00,080
Okay.

131
00:09:00,200 --> 00:09:03,360
So now we are going to run the server.

132
00:09:03,720 --> 00:09:07,490
So I'm going to say Python three external attacker.

133
00:09:07,530 --> 00:09:08,650
MCP.

134
00:09:09,690 --> 00:09:11,490
The server has started successfully.

135
00:09:11,930 --> 00:09:17,570
Let's go to cloud AI and we can see the server is successfully running.

136
00:09:18,490 --> 00:09:19,090
Great.

137
00:09:19,730 --> 00:09:24,170
Now you would be able to see if running message appears there.

138
00:09:24,410 --> 00:09:26,770
You can see this tool button this tool.

139
00:09:26,970 --> 00:09:28,170
Please click on that.

140
00:09:28,650 --> 00:09:33,610
And you would be able to see scan sub domains scan ports resolve DNS.

141
00:09:33,650 --> 00:09:37,210
These are all the functions from the Python file that has now come here.

142
00:09:37,450 --> 00:09:41,450
Okay so we are ready to use the scan sub domains function.

143
00:09:41,810 --> 00:09:42,610
What does it do.

144
00:09:42,650 --> 00:09:46,250
Scan targeted sub domains using the sub finder binary.

145
00:09:46,690 --> 00:09:51,050
And it takes the argument as a domain file and number of concurrent threads to use.

146
00:09:51,050 --> 00:09:52,450
It will take it by default.

147
00:09:52,770 --> 00:09:57,450
So all of these MCP tools are coming from which project external attacker MCP.

148
00:09:57,810 --> 00:09:58,370
Great.

149
00:09:58,410 --> 00:10:00,130
Now let us run the command.

150
00:10:00,170 --> 00:10:06,330
So I'll say do sub domain enumeration using sub finder.

151
00:10:06,530 --> 00:10:11,430
Or simply I can say do sub subdomain enumeration for tesla.com hit enter.

152
00:10:16,710 --> 00:10:21,350
And here you can see it will ask you allow the tool to run local commands.

153
00:10:21,350 --> 00:10:22,310
Please say allow.

154
00:10:23,070 --> 00:10:26,750
And once you do that in the background it is going to.

155
00:10:27,510 --> 00:10:27,750
Yeah.

156
00:10:27,750 --> 00:10:28,710
Let us allow that.

157
00:10:28,710 --> 00:10:31,950
Once again you can see target is Tesla.com.

158
00:10:34,470 --> 00:10:35,070
Allow.

159
00:10:42,590 --> 00:10:42,990
Yeah.

160
00:10:44,390 --> 00:10:49,950
And it is able to get us the uh subdomains over here.

161
00:10:49,950 --> 00:10:52,510
It was facing some issue initially.

162
00:10:54,350 --> 00:10:56,390
Connection pool local host.

163
00:11:00,550 --> 00:11:02,070
Connection refused okay.

164
00:11:02,110 --> 00:11:02,910
Just a second.

165
00:11:10,360 --> 00:11:12,600
Let me do that command once again.

166
00:11:16,160 --> 00:11:18,600
Do subdomain enumeration for tesla.com.

167
00:11:25,520 --> 00:11:26,080
Yes.

168
00:11:27,480 --> 00:11:27,960
Okay.

169
00:11:27,960 --> 00:11:30,000
You can see the server app is running.

170
00:11:30,000 --> 00:11:32,440
The server MCP is running.

171
00:11:32,440 --> 00:11:32,640
Now.

172
00:11:32,640 --> 00:11:33,400
Let's wait.

173
00:11:34,720 --> 00:11:40,600
Uh, we have actually taken a large long target or a large target, so it is going to take some time.

174
00:11:42,560 --> 00:11:42,840
Mm.

175
00:11:43,200 --> 00:11:43,960
Let's wait.

176
00:11:57,880 --> 00:11:58,400
Awesome.

177
00:11:58,560 --> 00:12:01,080
I have successfully enumerated the subdomains for Tesla.

178
00:12:01,080 --> 00:12:02,440
Let me run the scan for you.

179
00:12:02,520 --> 00:12:02,880
Okay.

180
00:12:03,000 --> 00:12:06,240
So it has found more than 200 unique subdomains.

181
00:12:06,240 --> 00:12:09,000
Here are some of the most interesting categories.

182
00:12:09,060 --> 00:12:09,460
Okay.

183
00:12:09,740 --> 00:12:19,740
So here you can see the subdomains cyber Tesla Tesla and then files English EU cloud dot Tesla and so

184
00:12:19,740 --> 00:12:20,060
on.

185
00:12:20,140 --> 00:12:26,860
So now once it identifies it will also print the list of interesting subdomains based on the categories

186
00:12:27,060 --> 00:12:33,260
like core websites are these shop or static and other websites like this as you can see over here.

187
00:12:33,780 --> 00:12:41,500
So uh, the output is uh, also going to be saved in the same folder from where you can get the output

188
00:12:41,700 --> 00:12:43,340
for the Tesla scan.

189
00:12:43,340 --> 00:12:50,580
And we can see here a Post request was sent to API run from where this from where this 200 unique subdomains

190
00:12:50,580 --> 00:12:51,460
have been found.

191
00:12:51,700 --> 00:13:01,980
Let's do one more scan subdomains for uh let's say hacker or hacker dot n okay.

192
00:13:02,020 --> 00:13:04,740
So now it is again going to send a Post request.

193
00:13:05,380 --> 00:13:11,430
And it will set the target and start doing subdomain enumeration for the target and it will print the

194
00:13:11,430 --> 00:13:15,110
results for you automatically over here.

195
00:13:15,110 --> 00:13:20,070
So we are currently utilizing only one functionality that is subdomain enumeration.

196
00:13:20,070 --> 00:13:21,910
But there can be more.

197
00:13:24,190 --> 00:13:29,230
Functionalities that we can do currently that has been supported by the tool currently.

198
00:13:29,230 --> 00:13:30,870
So what are more functionalities?

199
00:13:31,350 --> 00:13:38,510
Apart from scan subdomain scan ports, resolve DNS fuzz endpoints, enumerate assets, detect content

200
00:13:38,510 --> 00:13:46,470
delivery network or CDN, analyze TLS configuration and identify the HTTP services.

201
00:13:46,870 --> 00:13:51,110
And now you can see very interestingly it also gives us the context.

202
00:13:51,350 --> 00:13:58,470
For example stage dot dot in it is a staging and the development platform learn is it is a learning

203
00:13:58,470 --> 00:13:59,150
platform.

204
00:13:59,430 --> 00:14:01,550
Cyber scoreboard dot dot in.

205
00:14:01,590 --> 00:14:03,990
It is a scoreboard for an event named cyber.

206
00:14:04,390 --> 00:14:05,150
Very nice.

207
00:14:05,150 --> 00:14:11,390
So it is also giving more context to the subdomains that has been identified by the given tool.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,240 --> 00:00:01,760
Okay.

2
00:00:01,920 --> 00:00:04,080
If you want to perform any other.

3
00:00:07,520 --> 00:00:10,000
Tasks from here, you can definitely do it.

4
00:00:10,000 --> 00:00:10,480
Okay.

5
00:00:10,760 --> 00:00:12,440
Uh, let's say scan port.

6
00:00:12,440 --> 00:00:18,240
So I'm going to say scan ports for nmap.org.

7
00:00:19,880 --> 00:00:22,160
And it is going to give us the output.

8
00:00:24,440 --> 00:00:28,240
So you can see it is what it what and how it is doing.

9
00:00:28,240 --> 00:00:36,080
It is basically taking my input as a natural language, process it in the back end through the MCP server

10
00:00:36,080 --> 00:00:39,480
by which is basically running a flask application.

11
00:00:39,640 --> 00:00:46,320
So it is sending a Post request to API run, and it is identifying what is the current function that

12
00:00:46,320 --> 00:00:47,440
does port scanning.

13
00:00:47,720 --> 00:00:51,560
And then it basically does a port scan and gives the output.

14
00:00:52,200 --> 00:00:54,760
And here you can see this is the output for the port scan.

15
00:00:55,760 --> 00:00:56,160
So.

16
00:01:00,040 --> 00:01:04,240
Yeah port 8443 2221 and 25.

17
00:01:04,480 --> 00:01:09,080
These are the open ports for currently nmap.org domain that we have scanned.

18
00:01:09,320 --> 00:01:12,580
And you can see it also gives us the information.

19
00:01:12,620 --> 00:01:20,100
Port 443 is running web server Apache 2.46, and this is the title of the website response status,

20
00:01:20,100 --> 00:01:21,940
content, size and other information.

21
00:01:21,940 --> 00:01:23,140
As you can see over here.

22
00:01:24,300 --> 00:01:30,940
Okay, now participants, there is going to be a problem here, which is after certain search queries

23
00:01:30,940 --> 00:01:36,260
that we make as we are on a free plan, we are going to exhaust our search queries and eventually it

24
00:01:36,260 --> 00:01:42,980
is going to give us an prompt or an pop up saying that please try again after five hours.

25
00:01:43,020 --> 00:01:43,420
Okay.

26
00:01:43,660 --> 00:01:51,140
Hence, uh, we would not be able to perform more searches or operations like this that we are currently

27
00:01:51,140 --> 00:01:51,580
doing.

28
00:01:51,980 --> 00:01:52,420
Okay.

29
00:01:52,420 --> 00:01:58,860
So to overcome that, we are going to now switch to Olama, which is completely open source model,

30
00:01:58,860 --> 00:02:04,620
and set up an NCP protocol server for it again from scratch.

31
00:02:04,820 --> 00:02:07,580
Okay, so let's go there.

32
00:02:07,580 --> 00:02:12,500
But before that I'm going to close the cloud desktop IDE that we are using.

33
00:02:12,500 --> 00:02:15,060
I hope everyone has understood how to do this.

34
00:02:15,100 --> 00:02:20,220
If you face any issues or any errors please let me know.

35
00:02:20,220 --> 00:02:21,980
I would be very happy to help you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: Prompt Engineering

1
00:00:00,400 --> 00:00:03,880
First is let's learn about fine tuning because that is important.

2
00:00:04,200 --> 00:00:14,240
So we can configure our model in a manner where we can allow the model to create a vector database based

3
00:00:14,240 --> 00:00:21,960
on the information or knowledge that we will provide, and then it will help us then answer a lot of

4
00:00:21,960 --> 00:00:24,520
different types of questions that we want from it.

5
00:00:24,520 --> 00:00:30,360
So we are basically trying to enhance the knowledge of the given model that, uh, that we want it to

6
00:00:30,400 --> 00:00:31,600
do for us.

7
00:00:32,320 --> 00:00:32,800
Okay.

8
00:00:32,920 --> 00:00:44,240
So for example, I'm going to give a command now, uh, do subdomain enumeration for hacker 1.com and

9
00:00:44,240 --> 00:00:46,920
hit enter okay.

10
00:00:54,240 --> 00:00:54,880
Great.

11
00:00:54,880 --> 00:00:59,480
So we got an output right now I would be happy to help with the subdomain enumeration of hacker one.

12
00:00:59,520 --> 00:01:01,480
The output is again very good.

13
00:01:01,760 --> 00:01:05,580
Subdomains found are API, blog, challenge and so on.

14
00:01:05,780 --> 00:01:10,900
I was able to find 15 subdomains using various online tools and techniques that is passive.

15
00:01:11,260 --> 00:01:17,780
Some of the subdomains might not be active and listed potential subdomains that could be used.

16
00:01:18,260 --> 00:01:23,100
I've used a combined tools and techniques to perform subdomain enumeration, and the tools that have

17
00:01:23,100 --> 00:01:24,940
been currently used are sub listed.

18
00:01:25,820 --> 00:01:29,740
Amos and DNS recon are to give you the output.

19
00:01:29,740 --> 00:01:30,180
Okay.

20
00:01:30,220 --> 00:01:35,420
Now let's say again do subdomain enumeration for.

21
00:01:40,100 --> 00:01:44,220
Tesla.com because that's a large target a popular target.

22
00:01:44,220 --> 00:01:45,540
So let us see the output.

23
00:01:55,180 --> 00:01:55,740
Okay.

24
00:01:55,740 --> 00:02:00,220
So I was able to find 34 subdomains as we can see over here.

25
00:02:00,460 --> 00:02:04,180
And it has also tried to give some notes that it is a knowledge base.

26
00:02:04,420 --> 00:02:09,080
And this subdomain is related to Tesla model X electric vehicle.

27
00:02:09,080 --> 00:02:12,480
This is related to Tesla model three electric vehicle and so on.

28
00:02:12,680 --> 00:02:17,480
This is something which is good because we also want the model to give us the context.

29
00:02:17,640 --> 00:02:24,800
So we will also train it in a manner other in future wherein it gives us the context.

30
00:02:25,000 --> 00:02:30,520
So uh, it gives us an idea that this subdomain might be used for QA purposes, or maybe it's a dev

31
00:02:30,520 --> 00:02:32,240
or a staging subdomain, etc..

32
00:02:32,920 --> 00:02:40,000
Uh, now let us say give me the entire list of subdomains.

33
00:02:40,720 --> 00:02:45,080
The full list for Tesla.

34
00:02:57,640 --> 00:03:00,160
So earlier we had around 34 results.

35
00:03:04,920 --> 00:03:10,480
Uh, this time we got 60 results, as we can see over here, uh, available over here.

36
00:03:10,480 --> 00:03:13,420
So all the results that you see currently.

37
00:03:13,740 --> 00:03:21,140
These results are actually saved in the knowledge base of the current model from where it is able to

38
00:03:21,180 --> 00:03:22,860
find these targets for us.

39
00:03:23,500 --> 00:03:30,740
Uh, it is not currently configured to run or execute any tools or commands in the back end, because

40
00:03:30,740 --> 00:03:37,380
we have not set up any external tool to run with the current model, but still it is doing a good,

41
00:03:37,420 --> 00:03:39,340
pretty good job to give us the output.

42
00:03:39,540 --> 00:03:45,300
We will enhance the capabilities more so it gives not good but better output or maybe the best output

43
00:03:45,300 --> 00:03:46,100
that we want.

44
00:03:48,500 --> 00:03:51,900
Uh, we can definitely add more more sources to this.

45
00:03:51,900 --> 00:03:52,340
That is.

46
00:03:52,380 --> 00:03:53,540
Absolutely yes.

47
00:03:53,540 --> 00:04:00,900
We will add more sources like uh, sub domain finder, sub finder, etc. we would be doing that.

48
00:04:00,940 --> 00:04:07,140
Now let's do a last prompt and let's try to see for Tata AIG is able to identify anything.

49
00:04:23,760 --> 00:04:24,360
Yes.

50
00:04:24,360 --> 00:04:29,200
So we can see we found 26 such sub domains that we can see over here.

51
00:04:29,680 --> 00:04:36,120
Uh, and it does not contains spark as we can see, uh, we attempt to find it over here.

52
00:04:36,480 --> 00:04:38,360
So, uh, yes.

53
00:04:38,360 --> 00:04:40,280
So this is how we have got the output.

54
00:04:40,560 --> 00:04:43,000
Uh, good output, decent output.

55
00:04:43,000 --> 00:04:47,640
But it is not the expected output that we want of our choice over here.

56
00:04:47,840 --> 00:04:53,480
So we are going to configure this to run externally for us and then give us extended output.

57
00:04:55,400 --> 00:04:56,080
All right.

58
00:04:56,080 --> 00:04:58,280
So this is what we have understood now.

59
00:04:58,320 --> 00:05:02,120
Now we will gradually move forward to understand.

60
00:05:02,760 --> 00:05:06,520
Uh yes it can do it for Apple.com as well.

61
00:05:11,360 --> 00:05:11,960
CMS.

62
00:05:12,000 --> 00:05:12,280
Yes.

63
00:05:12,280 --> 00:05:14,000
It can also identify CMS.

64
00:05:14,200 --> 00:05:17,160
It can do tech detection with HTTP as well.

65
00:05:32,950 --> 00:05:33,270
Okay.

66
00:05:33,270 --> 00:05:34,910
So we will say okay great.

67
00:05:35,870 --> 00:05:39,830
Do tech detection of the above.

68
00:05:55,230 --> 00:05:55,790
Okay.

69
00:05:55,790 --> 00:06:02,230
So we can see over here uh, it is able to identify which given assets or targets are using what.

70
00:06:02,270 --> 00:06:08,030
So we can see Apple Insider is running on WordPress uh which is great for PHP and MySQL.

71
00:06:08,150 --> 00:06:15,470
So we know WordPress is a CMS which uses a lot of plugins, themes, etc. so that means this can be

72
00:06:15,470 --> 00:06:23,590
a good target for us where we can go on Apple insider.apple.com and see uh, okay DNS probe possible.

73
00:06:23,830 --> 00:06:29,570
We'll try to again attempt to open this target, maybe in some time, and then see if it is able to

74
00:06:29,570 --> 00:06:30,410
be accessed.

75
00:06:32,210 --> 00:06:35,410
And we can also see the chat prompts or pop ups that will come over here.

76
00:06:35,410 --> 00:06:38,290
And we are able to see that based on the text detection.

77
00:06:38,970 --> 00:06:40,010
Uh, yes.

78
00:06:40,370 --> 00:06:46,250
Based on the prompts that we are able to do, it is able to do text detection and help us identify.

79
00:06:46,290 --> 00:06:51,130
Now, what we'll do is we'll say, uh, let's say if you're only attempting to identify targets that

80
00:06:51,130 --> 00:06:53,690
are related to WordPress because.

81
00:06:56,050 --> 00:07:03,130
Because WordPress has, let's say, a, a latest exploit or a CV available.

82
00:07:03,130 --> 00:07:10,530
So we are going to say list down word press text detected targets only.

83
00:07:13,370 --> 00:07:21,690
Because okay, let's not let's not give more context, uh, detected targets from above because we want

84
00:07:21,690 --> 00:07:27,010
to run a because we don't want to run a WordPress exploit.

85
00:07:27,130 --> 00:07:29,070
So let's say WordPress has a latest CV.

86
00:07:29,110 --> 00:07:31,350
Let's assume that as of now for this.

87
00:07:31,870 --> 00:07:34,310
So it also gives you gives you alerts that okay.

88
00:07:34,470 --> 00:07:39,750
Based on the tech detection results, here are the WordPress related targets that appears, uh, there

89
00:07:39,750 --> 00:07:40,470
for you.

90
00:07:40,470 --> 00:07:42,230
So we can directly use this.

91
00:07:42,430 --> 00:07:48,470
So you can see news, job info, gift, get started, FAQ, blog, Apple Insider, etc. as the targets

92
00:07:48,470 --> 00:07:54,910
that are available for us, uh, that we can utilize and we have got the result now we can copy this

93
00:07:54,910 --> 00:07:59,150
results that is appearing from here, and we can then use it somewhere else.

94
00:08:01,190 --> 00:08:01,590
Okay.

95
00:08:01,750 --> 00:08:10,710
And uh, you can also currently this does not have the capability to uh, basically uh, create, uh,

96
00:08:10,950 --> 00:08:17,110
external file for us, uh, if you will ask it, to generate this into a JSON response, uh, it will

97
00:08:17,110 --> 00:08:22,550
generate it for you or maybe a tabular response to saving it to a file, but currently it does not have

98
00:08:22,550 --> 00:08:25,310
the capability to directly export it into a file.

99
00:08:25,590 --> 00:08:26,910
We will enhance that.

100
00:08:26,910 --> 00:08:32,070
And we will add that capability to the model where it is also able to generate files for us, uh, so

101
00:08:32,070 --> 00:08:33,370
that we can directly use it.

102
00:08:33,370 --> 00:08:39,650
But yeah, as of now, if you want this to be processed into another file format, it can definitely

103
00:08:39,850 --> 00:08:40,810
do it for us.

104
00:08:43,090 --> 00:08:43,690
Uh, yes.

105
00:08:43,690 --> 00:08:48,930
Can you save the let's see, can you save the output in PDF format?

106
00:08:50,890 --> 00:08:51,370
Okay.

107
00:08:51,370 --> 00:08:58,890
So it does not have a capability to currently create a PDF file, but uh, it can generate text based

108
00:08:58,890 --> 00:09:02,290
summary which we can use and then utilize into adding into a file.

109
00:09:02,330 --> 00:09:02,730
Okay.

110
00:09:03,090 --> 00:09:09,410
Uh, this feature currently is not available with this model, but but uh, it is not like that.

111
00:09:09,410 --> 00:09:10,130
We cannot do it.

112
00:09:10,170 --> 00:09:11,370
We can still do it.

113
00:09:11,410 --> 00:09:14,530
We will do some changes in the configuration.

114
00:09:14,770 --> 00:09:20,650
And then it would allow us to also generate CSV and PDF files uh, as well.

115
00:09:20,690 --> 00:09:21,090
Okay.

116
00:09:21,290 --> 00:09:22,890
As of now it is not able to do it.

117
00:09:22,890 --> 00:09:29,930
But we will add some more capabilities or configuration changes where it is using not only text generation,

118
00:09:30,050 --> 00:09:35,050
uh capability, but also it can help us create files.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:02,200
Okay, so let us continue.

2
00:00:04,040 --> 00:00:04,640
Thank you.

3
00:00:05,000 --> 00:00:05,960
Let us continue.

4
00:00:06,080 --> 00:00:13,080
So, uh, participants, we are going to understand how you can perform fine tuning of the model and

5
00:00:13,080 --> 00:00:20,680
let the model create a vector database where this technique is going to help you uncover.

6
00:00:23,280 --> 00:00:25,920
A lot of different types of vulnerabilities.

7
00:00:26,720 --> 00:00:37,600
So for instance, what I am going to do is I'm going to upload a postman collection to our LM model.

8
00:00:37,800 --> 00:00:40,960
So what is postman collection for participants who are not aware.

9
00:00:41,280 --> 00:00:51,080
So whenever we do API Pentesting, uh, whenever we do API Pentesting, we usually utilize its documentation.

10
00:00:51,080 --> 00:00:53,760
So you might have heard about swagger documentation.

11
00:00:53,800 --> 00:00:54,200
Okay.

12
00:00:54,400 --> 00:01:03,660
So here participants, you can see there is a -- vulnerable API, which you can use.

13
00:01:03,660 --> 00:01:05,900
So it's a -- vulnerable API project.

14
00:01:06,220 --> 00:01:13,380
Now here are there is ten test cases which you can see over here.

15
00:01:16,020 --> 00:01:16,420
Yeah.

16
00:01:16,820 --> 00:01:21,380
There are ten scenarios that you can do for the exercises and different types of test cases that you

17
00:01:21,380 --> 00:01:21,900
can do.

18
00:01:22,220 --> 00:01:30,380
Now our test cases that is from OWASp top ten like broken object level authorization, insecure data

19
00:01:30,380 --> 00:01:33,100
storage, explosive data exposure, etc., etc..

20
00:01:33,140 --> 00:01:41,700
Now when we go to this public workspace here, you will be able to see the collection and let's say

21
00:01:41,700 --> 00:01:42,380
API one.

22
00:01:42,380 --> 00:01:46,740
So this API one teaches about broken object level authorization.

23
00:01:46,900 --> 00:01:51,380
So you can create a user, get a user update a user.

24
00:01:51,380 --> 00:01:54,820
So these are test cases that you can do to learn API Pentesting.

25
00:01:54,860 --> 00:01:55,140
Okay.

26
00:01:55,180 --> 00:02:00,750
That is based this project is basically aiming towards teaching you about API pentesting.

27
00:02:00,990 --> 00:02:10,590
Now if we see here carefully, then all of the API test cases or APIs that are being created by developers

28
00:02:10,590 --> 00:02:12,910
worldwide comes with a documentation.

29
00:02:13,190 --> 00:02:24,030
That documentation basically has all the list of endpoints, parameters, uh, head, body, token,

30
00:02:24,030 --> 00:02:28,070
etc. that is going to be useful for a developer to understand.

31
00:02:28,070 --> 00:02:30,030
How does that API actually work?

32
00:02:30,430 --> 00:02:33,190
So currently we also have an API collection here.

33
00:02:33,230 --> 00:02:41,230
So if I go to postman and uh we API postman collection, then we can see the entire collection.

34
00:02:41,350 --> 00:02:44,110
This is the same collection that has been loaded over here.

35
00:02:44,110 --> 00:02:47,830
So when I go to collections you can see the overview.

36
00:02:48,070 --> 00:02:53,270
And in the overview, uh, yeah, I go to view complete documentation.

37
00:02:53,470 --> 00:03:02,330
This is the entire documentation available for API test cases API one, API one, API two, API three,

38
00:03:02,370 --> 00:03:03,330
etc. and so on.

39
00:03:03,330 --> 00:03:03,770
Okay.

40
00:03:03,850 --> 00:03:08,290
So here is the entire documentation available on how these all API test cases work.

41
00:03:08,690 --> 00:03:14,650
Now I'm going to take this API documentation so I can download this JSON file.

42
00:03:14,650 --> 00:03:18,370
So I'm going to click on this download and download this.

43
00:03:18,650 --> 00:03:28,690
Now once I've downloaded this collection I'm going to go to our llama local AI agent.

44
00:03:28,930 --> 00:03:30,490
And I'm going to upload this.

45
00:03:30,490 --> 00:03:32,410
So I'm going to click on Upload files.

46
00:03:32,410 --> 00:03:34,090
And I'm going to go to downloads.

47
00:03:34,090 --> 00:03:35,850
And I'm going to say collection.

48
00:03:44,090 --> 00:03:46,450
Collection okay.

49
00:03:47,330 --> 00:03:49,850
The name V API postman collection.

50
00:03:50,690 --> 00:03:56,750
Postman collection okay let's upload once again Downloads via API.

51
00:03:59,350 --> 00:03:59,870
Yeah.

52
00:03:59,870 --> 00:04:07,430
So here is also a PDF document which contains the same collection okay.

53
00:04:07,830 --> 00:04:12,230
Here you can see it has the same collection that is pasted into a PDF format.

54
00:04:12,430 --> 00:04:14,270
So I think this should also work.

55
00:04:14,270 --> 00:04:17,550
So I'm going to load this one.

56
00:04:17,590 --> 00:04:18,550
Zero eight KB.

57
00:04:18,550 --> 00:04:25,750
And then I'm going to say uh understand this document thoroughly.

58
00:04:28,870 --> 00:04:29,310
Okay.

59
00:04:31,910 --> 00:04:38,510
Now there are various different types of APIs that let the model understand the documentation for now.

60
00:04:41,550 --> 00:04:41,990
Okay.

61
00:04:42,030 --> 00:04:50,710
And it started giving me output, uh, for each target that we provided.

62
00:04:50,710 --> 00:04:51,190
Okay.

63
00:04:51,190 --> 00:05:01,490
Now we are going to say uh, explain the or list down the endpoints available.

64
00:05:03,610 --> 00:05:08,050
In the API documentation I.

65
00:05:10,090 --> 00:05:10,650
Loaded.

66
00:05:16,690 --> 00:05:17,330
So now.

67
00:05:20,810 --> 00:05:21,330
Yes.

68
00:05:21,330 --> 00:05:23,010
So this is the API documentation.

69
00:05:23,010 --> 00:05:24,890
This is the content out of it.

70
00:05:25,690 --> 00:05:28,090
Uh, if okay.

71
00:05:28,090 --> 00:05:30,450
So it says I did not had any documents.

72
00:05:30,450 --> 00:05:31,850
So I'm going to again upload it.

73
00:05:35,170 --> 00:05:38,050
And say list sorry.

74
00:05:38,850 --> 00:05:39,370
Yes.

75
00:05:40,530 --> 00:05:46,010
List down all the endpoints available in the API documentation and let us see what is the output.

76
00:05:49,610 --> 00:05:53,020
So Well PDF document.

77
00:06:03,820 --> 00:06:08,060
Okay, this is not working appropriately as of now, but we can fix this.

78
00:06:08,180 --> 00:06:13,700
So I'm going to check the configuration in the files that we have just uploaded.

79
00:06:13,700 --> 00:06:16,460
And I'm going to change the prompt to use it appropriately.

80
00:06:16,940 --> 00:06:19,460
Till then I'll show you an alternative of the same test case.

81
00:06:19,500 --> 00:06:19,860
Okay.

82
00:06:23,460 --> 00:06:27,260
I have a open source model called as GPT for all.

83
00:06:27,820 --> 00:06:30,580
You can download this for windows, Ubuntu Mac OS.

84
00:06:30,620 --> 00:06:32,860
I have downloaded it for already for Mac OS.

85
00:06:32,900 --> 00:06:34,100
No internet required.

86
00:06:36,140 --> 00:06:37,220
GPT for all.

87
00:06:37,220 --> 00:06:39,740
I'm going to start GPT for law for all.

88
00:06:39,740 --> 00:06:40,180
Sorry.

89
00:06:40,420 --> 00:06:45,900
And I'm going to create a vector database to do the same thing that did not work correctly as of now.

90
00:06:45,940 --> 00:06:48,580
I will fix that and show it in the next session.

91
00:06:50,840 --> 00:06:53,760
You can upload both the collection or the documentation.

92
00:06:53,760 --> 00:06:54,880
Anything is fine.

93
00:06:54,920 --> 00:06:56,720
Okay, now we can see.

94
00:06:56,720 --> 00:07:00,360
Welcome to the GPT for all the privacy first LLM chat application.

95
00:07:00,360 --> 00:07:07,880
That is basically what it is an alternative to Open web UI which is connecting in local llama model

96
00:07:07,880 --> 00:07:08,640
in the background.

97
00:07:08,640 --> 00:07:11,960
So you can go to find models and see the models available.

98
00:07:12,360 --> 00:07:17,920
Reasoner version one eight GB Ram required four GB file size of the model 8 billion parameters.

99
00:07:17,920 --> 00:07:21,800
Trained on llama three 8 billion, which is the current model that we are using.

100
00:07:21,800 --> 00:07:24,520
You can click on download and you can use it.

101
00:07:24,520 --> 00:07:30,200
I already have a model that is downloaded which is llama 3.1 and Mini Orca.

102
00:07:30,400 --> 00:07:32,600
So this is of 4.34 GB.

103
00:07:32,640 --> 00:07:34,280
This is 1.84 GB.

104
00:07:34,280 --> 00:07:35,520
I'm going to use that.

105
00:07:35,520 --> 00:07:40,680
Before that I'm going to go with local docs and I'm going to set up a local document folder which is

106
00:07:40,680 --> 00:07:41,880
currently in this path.

107
00:07:41,920 --> 00:07:44,080
User document class testing document.

108
00:07:44,080 --> 00:07:45,600
Let me go to that path quickly.

109
00:07:50,500 --> 00:07:51,980
User documents.

110
00:07:55,380 --> 00:07:55,820
Yeah.

111
00:08:00,940 --> 00:08:01,460
Okay.

112
00:08:01,460 --> 00:08:08,220
So this current folder you have one, two, three and four documents.

113
00:08:08,380 --> 00:08:10,380
First document.

114
00:08:10,580 --> 00:08:12,060
Look carefully participants.

115
00:08:12,180 --> 00:08:17,340
This contains a log file a log file that I have extracted from a system.

116
00:08:17,620 --> 00:08:18,060
Okay.

117
00:08:18,300 --> 00:08:23,500
To ask the model to explain me what kind of attack might have happened in the system.

118
00:08:23,540 --> 00:08:27,660
Okay, this is for also helpful not only for red teamers.

119
00:08:29,300 --> 00:08:34,620
Uh, but it is also going to be helpful for, uh, blue teamers and SOC teams as well.

120
00:08:34,660 --> 00:08:35,060
Okay.

121
00:08:35,500 --> 00:08:42,460
Uh, why did we just hop to a GPT for all is because of the current test case that I wanted to show,

122
00:08:42,500 --> 00:08:45,140
as it did not appropriately work in open web UI.

123
00:08:45,430 --> 00:08:52,830
I'm showing an absolutely same open source alternative of it that I have configured in my system, uh,

124
00:08:52,990 --> 00:08:54,430
for your understanding.

125
00:08:55,470 --> 00:09:02,230
So in GPT four all I'm going to configure the local docs folder in which there are four files, which

126
00:09:02,230 --> 00:09:03,790
contains one a lock file.

127
00:09:04,270 --> 00:09:11,910
Second contains a document which is a naval doctrine naval warfare document of around 88 pages.

128
00:09:12,870 --> 00:09:23,270
Next is a very, very specific topic of somatosensory system that basically means how skin works or

129
00:09:23,270 --> 00:09:24,430
how skin system works.

130
00:09:24,430 --> 00:09:25,950
This is a very specific topic.

131
00:09:25,990 --> 00:09:29,030
A general model would not have been trained on this.

132
00:09:29,510 --> 00:09:34,270
And then our documentation which is vulnerable API documentation.

133
00:09:34,270 --> 00:09:38,030
So there are four different types of documents of different different knowledge.

134
00:09:38,670 --> 00:09:41,470
Now we are going to add the collection.

135
00:09:41,470 --> 00:09:42,310
How to do that.

136
00:09:42,310 --> 00:09:43,310
Create a folder.

137
00:09:44,010 --> 00:09:48,170
go to Folder Path and in the folder path add any files that you want.

138
00:09:48,370 --> 00:09:50,370
So if I go ahead and paste a file here.

139
00:09:50,570 --> 00:09:52,530
So let's say Tata AIG passive.

140
00:09:52,690 --> 00:09:54,450
Let me go and paste it here.

141
00:09:54,850 --> 00:09:56,530
So now there is a new file available.

142
00:09:56,530 --> 00:09:57,690
Total five files.

143
00:09:58,290 --> 00:09:59,650
Now let's go to the model.

144
00:10:00,650 --> 00:10:02,570
And currently there are five files.

145
00:10:02,570 --> 00:10:08,290
It has also automatically found that and it has indexed it as well okay.

146
00:10:08,330 --> 00:10:09,170
And it is ready.

147
00:10:09,330 --> 00:10:13,490
If you think it is not indexed you can rebuild when new files are being added.

148
00:10:13,490 --> 00:10:18,530
Click on rebuild and it is going to embed it a new file.

149
00:10:18,570 --> 00:10:21,930
Tata AIG NDP 1st April 2020.

150
00:10:21,930 --> 00:10:22,970
Which is this.

151
00:10:22,970 --> 00:10:27,450
Then somatosensory and other documents will also be processed right now.

152
00:10:27,650 --> 00:10:29,690
And the vector embeddings will be saved.

153
00:10:34,090 --> 00:10:37,050
You can see 300 out of 370 embeddings.

154
00:10:39,570 --> 00:10:40,130
Ready?

155
00:10:40,490 --> 00:10:40,890
Awesome.

156
00:10:40,890 --> 00:10:42,030
Now this is ready to use.

157
00:10:42,030 --> 00:10:43,030
Let's go to chat.

158
00:10:43,910 --> 00:10:45,150
Let's choose a model.

159
00:10:45,150 --> 00:10:46,430
Let's choose metal armor.

160
00:10:47,550 --> 00:10:49,310
Give it a few seconds to load.

161
00:10:52,430 --> 00:10:52,990
Yes.

162
00:10:52,990 --> 00:10:56,990
So how do we connect GPT for all to Allama?

163
00:10:57,030 --> 00:10:57,750
Very simple.

164
00:10:57,790 --> 00:10:58,750
Install it.

165
00:10:59,230 --> 00:11:05,710
After installing simply go to model and from model you can choose the model available.

166
00:11:06,110 --> 00:11:12,150
Okay, it will as you already have llama 3.1 installed, it will automatically detect it from your system

167
00:11:12,390 --> 00:11:13,550
so you can choose it.

168
00:11:13,830 --> 00:11:18,150
Also, when you go to chat, it will again ask you which model you want to use.

169
00:11:18,150 --> 00:11:24,110
So if you don't want to use the llama 3.1, you can eject this model so you can see the model is ejected

170
00:11:24,310 --> 00:11:26,510
and then you can choose whatever model you want.

171
00:11:26,550 --> 00:11:30,950
I have two models Mini Orca which is very small, and llama.

172
00:11:31,230 --> 00:11:33,030
So now I'm going to use llama.

173
00:11:33,310 --> 00:11:40,970
I'm going to click on local docks and I'm going to say please utilize this collection document To answer

174
00:11:41,370 --> 00:11:44,010
specific output that I want.

175
00:11:44,050 --> 00:11:44,450
Okay.

176
00:11:44,610 --> 00:11:46,170
Now I'm going to ask a question.

177
00:11:46,370 --> 00:11:46,770
Hi.

178
00:11:48,090 --> 00:11:58,690
List all the endpoints and parameters for the vap p.

179
00:12:01,130 --> 00:12:04,330
API documentation.

180
00:12:05,570 --> 00:12:05,970
Yeah.

181
00:12:08,530 --> 00:12:10,090
And you're able to see.

182
00:12:10,130 --> 00:12:17,890
Now you all the API endpoints that are currently in the document are also present.

183
00:12:18,050 --> 00:12:22,010
In addition to that we can see a follow up question has also been given to us.

184
00:12:22,850 --> 00:12:26,730
What has been expected as a response or from this given endpoint.

185
00:12:26,730 --> 00:12:33,050
And now we are able to see that we found the endpoint, we found the method the endpoint uses, and

186
00:12:33,050 --> 00:12:36,810
all the parameters that are currently present in the given endpoint.

187
00:12:36,850 --> 00:12:41,460
As you see, isn't that really nice for us to use?

188
00:12:46,900 --> 00:12:49,100
Uh, why did we use the other documents?

189
00:12:49,100 --> 00:12:56,420
It is, uh, just for example, I wanted to show that we can, uh, out of five documents correctly,

190
00:12:57,140 --> 00:13:03,660
the current llama model is able to identify that the user is trying to ask a question from the given

191
00:13:03,980 --> 00:13:06,660
data set or data source that we have uploaded.

192
00:13:06,660 --> 00:13:13,620
Now, I can switch my question, and I can ask information from any other data source or vector that

193
00:13:13,620 --> 00:13:20,100
has been added that is just to show the model's capabilities that it correctly identifies from where

194
00:13:20,140 --> 00:13:23,740
to fetch the data for the user that it has been requested for.

195
00:13:28,940 --> 00:13:29,620
Participants.

196
00:13:29,620 --> 00:13:31,100
Are you all with me so far?

197
00:13:31,500 --> 00:13:37,180
We can see here the source is the VAE API documentation from where it identified this.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,040 --> 00:00:08,680
Now we are more interested towards letting the model help us identify vulnerabilities or specific test

2
00:00:08,680 --> 00:00:19,440
cases so that we can do let the model help us point in a direction and it says potentially you are trying

3
00:00:19,440 --> 00:00:25,720
to potentially here is where the bug can be, which you can replicate.

4
00:00:25,720 --> 00:00:29,440
Or maybe you can then find it and confirm.

5
00:00:29,440 --> 00:00:33,440
So the model can be the model is going to help us.

6
00:00:34,520 --> 00:00:40,080
So from 100 things it is going to point out that point us out in a direction saying this.

7
00:00:40,120 --> 00:00:42,360
Here are two things which look suspicious.

8
00:00:42,600 --> 00:00:44,520
And this is a generated test case.

9
00:00:44,520 --> 00:00:46,280
Please confirm it manually.

10
00:00:46,320 --> 00:00:46,720
Okay.

11
00:00:47,080 --> 00:00:52,680
Now this is just an example that I've shown you for currently for the API documentation.

12
00:00:52,960 --> 00:00:55,400
I have a very great test case for this.

13
00:00:55,680 --> 00:01:04,410
That is, uh, how the model can help us do JavaScript analysis of n number of files of our choice.

14
00:01:04,730 --> 00:01:11,370
So just for example, in the same folder I'm going to run a command that is Wayback URLs.

15
00:01:11,370 --> 00:01:17,970
And I'm going to pull URLs from Wayback Machine for active dot in target.

16
00:01:18,170 --> 00:01:23,570
And then I'm going to grep the dot js files that are present.

17
00:01:25,610 --> 00:01:34,090
Yeah I'm going to grep all the JS files that are present and save it into a file that is called as active

18
00:01:35,570 --> 00:01:37,970
js dot txt.

19
00:01:38,010 --> 00:01:41,890
What we are currently doing we are pulling all the URLs from all those URLs.

20
00:01:41,890 --> 00:01:48,930
We only want those urls endpoints that contains dot js and it could be in case sensitive format as well.

21
00:01:48,930 --> 00:01:54,250
It could be capital JS as well and save all the output in this file.

22
00:01:54,530 --> 00:01:54,930
Okay.

23
00:01:57,490 --> 00:02:00,690
Uh what did we do wrong?

24
00:02:01,010 --> 00:02:02,130
Let me see.

25
00:02:05,970 --> 00:02:08,250
Sanctify from this output.

26
00:02:08,250 --> 00:02:09,050
Grip this.

27
00:02:14,210 --> 00:02:16,450
Okay, let's do one thing.

28
00:02:22,330 --> 00:02:23,570
Oh, I'm so sorry.

29
00:02:23,570 --> 00:02:24,450
That is correct.

30
00:02:25,050 --> 00:02:25,570
Grip.

31
00:02:25,610 --> 00:02:25,970
I.

32
00:02:28,410 --> 00:02:31,890
Guess we did not add this option.

33
00:02:33,330 --> 00:02:38,930
Now what it is going to do, it is going to find all the URLs, and it is going to only print the URLs

34
00:02:38,930 --> 00:02:40,490
that contains dot js.

35
00:02:40,530 --> 00:02:49,050
As you can see now we have a nice file with us currently with uh with us which contains how many URLs.

36
00:02:49,090 --> 00:02:52,290
JS js file endpoints or URLs for us.

37
00:02:54,570 --> 00:02:55,650
610.

38
00:02:55,690 --> 00:02:56,130
Wow.

39
00:02:56,610 --> 00:03:05,980
Now participants I want my model to automatically find all the parameters endpoints from the JavaScript

40
00:03:05,980 --> 00:03:07,740
files that I can use for fuzzing.

41
00:03:07,780 --> 00:03:16,660
Wouldn't that be great if I fuzz the target based on the functions function name based on the URL endpoints

42
00:03:16,660 --> 00:03:21,620
that are available in the JavaScript file, or maybe to find secrets tokens API keys.

43
00:03:21,780 --> 00:03:30,340
Not only that, I will show you how I have been successful in past in taking the function names or the

44
00:03:30,340 --> 00:03:36,020
variable names from the JavaScript file, and use it to find new subdomains for the target.

45
00:03:36,060 --> 00:03:36,500
Why?

46
00:03:36,900 --> 00:03:44,980
Because all type of targets like let's say a bank, a bank sector, the developer would be using functions

47
00:03:44,980 --> 00:03:47,980
or variable names that would be more specific to a bank.

48
00:03:48,220 --> 00:03:56,740
Let's say a function name ledger of a variable name, which is let's say a bank account or maybe banking,

49
00:03:57,060 --> 00:03:57,820
etc..

50
00:03:57,860 --> 00:03:59,420
Now these functions are variable.

51
00:03:59,420 --> 00:04:03,060
Names are likely to be in the subdomains as well.

52
00:04:03,060 --> 00:04:09,820
And maybe this word list does not works on Tesla because Tesla's developer utilizes something else in

53
00:04:09,820 --> 00:04:11,180
their variables and functions.

54
00:04:11,180 --> 00:04:17,180
Hence, we are creating target specific word list that increases the chances of us to find more hidden

55
00:04:17,220 --> 00:04:17,740
assets.

56
00:04:17,780 --> 00:04:23,780
We would be seeing that in our next session, but as of now, let me show you now how all of these files

57
00:04:23,780 --> 00:04:29,060
can be processed by the lm r agent quickly for us.

58
00:04:29,260 --> 00:04:34,260
So now currently we only have a file which contains the URL endpoints.

59
00:04:34,260 --> 00:04:36,020
Let's quickly download them.

60
00:04:36,260 --> 00:04:39,620
So to download them we are going to run this command.

61
00:04:42,420 --> 00:04:44,740
W get w get w get.

62
00:04:54,140 --> 00:04:54,500
Name.

63
00:04:57,100 --> 00:04:57,860
Blessing.

64
00:04:57,900 --> 00:04:58,540
Chase.

65
00:05:04,150 --> 00:05:06,630
Okay, let's just download them manually.

66
00:05:06,870 --> 00:05:20,630
So cat the file and then we are going to say while read host do do curl silently insecurely on the given

67
00:05:20,630 --> 00:05:26,350
URL endpoint and make sure that it sends an insecure.

68
00:05:26,790 --> 00:05:31,470
Even if there is no SSL certificate, it downloads that file and closes the loop.

69
00:05:32,350 --> 00:05:33,710
Uh, okay.

70
00:05:33,710 --> 00:05:34,590
Let's verify.

71
00:05:34,750 --> 00:05:35,550
Read the file.

72
00:05:35,550 --> 00:05:37,590
Read each URL one by one host.

73
00:05:37,750 --> 00:05:39,310
Save it into the host variable.

74
00:05:39,630 --> 00:05:47,030
Send a curl request on the target that is basically download js file and securely and save it.

75
00:05:47,070 --> 00:05:47,510
Done.

76
00:05:47,870 --> 00:05:49,070
I think this should work.

77
00:06:06,950 --> 00:06:07,390
Okay.

78
00:06:07,670 --> 00:06:11,270
Instead of curl, let's not send a open ended request.

79
00:06:11,270 --> 00:06:13,590
Let's send a get request.

80
00:06:14,310 --> 00:06:17,110
So insecure.

81
00:06:17,870 --> 00:06:18,270
Yeah.

82
00:06:24,070 --> 00:06:24,710
Nice.

83
00:06:24,710 --> 00:06:28,710
So you can see it is basically sending requests to the endpoints.

84
00:06:28,710 --> 00:06:30,110
And it is trying to download it.

85
00:06:30,110 --> 00:06:31,830
So it could not found the above file.

86
00:06:31,830 --> 00:06:35,390
Hence it says 404 404 for this file as well.

87
00:06:35,630 --> 00:06:36,950
But for this file okay.

88
00:06:36,990 --> 00:06:40,590
Again note not found not found not found.

89
00:06:40,590 --> 00:06:43,550
But yeah we can see for this file main dot js.

90
00:06:43,590 --> 00:06:46,990
It downloaded that file as we can see over here.

91
00:06:46,990 --> 00:06:47,750
Very nice.

92
00:06:47,950 --> 00:06:49,590
The file size was eight KB.

93
00:06:49,710 --> 00:06:53,430
And we are going to now see these files that have been generated.

94
00:06:53,430 --> 00:06:54,110
Excellent.

95
00:06:54,150 --> 00:06:56,710
Let's wait for this for a minute quickly.

96
00:06:56,870 --> 00:07:05,990
And let's go to the agent the model now And let's go to the local docks and again rebuild it.

97
00:07:06,750 --> 00:07:08,990
Now you can see it is indexing six files.

98
00:07:10,390 --> 00:07:12,310
Or there are new files coming up here.

99
00:07:16,910 --> 00:07:17,430
Yes.

100
00:07:18,470 --> 00:07:22,150
Participants you can see not only six files, but there are so many files.

101
00:07:22,150 --> 00:07:28,350
For example, if you see this current script dot js file, let me open it and it contains JavaScript.

102
00:07:28,830 --> 00:07:29,590
Very nice.

103
00:07:29,990 --> 00:07:34,150
Uh, if you go back we can see uh tweenmax dot js.

104
00:07:34,190 --> 00:07:35,070
Let's open it.

105
00:07:35,390 --> 00:07:42,150
It contains some JavaScript that is going to be used in the target functionality somewhere, etc.,

106
00:07:42,190 --> 00:07:42,590
etc..

107
00:07:42,630 --> 00:07:47,230
Okay, email decode Main.js might be using some functionality over there, etc..

108
00:07:47,270 --> 00:07:52,550
Okay, so I think I think these many JavaScript files are fine as of now.

109
00:07:52,550 --> 00:07:54,710
So let me just stop downloading more.

110
00:07:55,230 --> 00:07:55,830
Nice.

111
00:07:56,110 --> 00:07:57,590
And let's go to the model.

112
00:07:59,230 --> 00:07:59,590
Yeah.

113
00:07:59,830 --> 00:08:01,960
And rebuild this once more.

114
00:08:30,200 --> 00:08:31,640
Okay, it is taking some time.

115
00:08:31,640 --> 00:08:32,360
Let's wait.

116
00:08:39,760 --> 00:08:40,880
It is processing.

117
00:08:43,680 --> 00:08:45,200
Let me add a new collection.

118
00:08:47,200 --> 00:08:49,880
Let's call it as JS folder path.

119
00:09:12,490 --> 00:09:14,410
Uh, let's provide a folder path.

120
00:09:16,530 --> 00:09:17,850
Let's create the collection.

121
00:09:27,090 --> 00:09:28,170
It is embedding right now.

122
00:09:28,170 --> 00:09:28,890
Let's wait.

123
00:09:41,770 --> 00:09:47,730
I think it is not reading the JS file due to some reason because it says only two files, but still

124
00:09:47,730 --> 00:09:48,850
we can try it out.

125
00:09:48,890 --> 00:09:50,530
Let's go back here and say hi.

126
00:09:52,010 --> 00:09:54,890
Let's select the JS folder that we just created and say hi.

127
00:09:55,610 --> 00:10:14,570
Can you find the can you find An API secret key, comma password comma token in the available files

128
00:10:15,170 --> 00:10:16,450
in the documents.

129
00:10:25,410 --> 00:10:28,570
Okay, so currently it is able to find it.

130
00:10:28,570 --> 00:10:32,170
But in the API documentation only.

131
00:10:32,170 --> 00:10:35,610
As we can see it has taken this source.

132
00:10:35,770 --> 00:10:36,970
Uh not sure.

133
00:10:36,970 --> 00:10:43,970
I will just try to fix this that to uh, load the JavaScript file appropriately because our approach

134
00:10:44,010 --> 00:10:51,130
is or our aim is that it finds the API secret password or token from the JavaScript files that we have

135
00:10:51,130 --> 00:10:58,610
just uploaded, because these files definitely contains a keyword like, uh, keyword, like token,

136
00:10:58,610 --> 00:10:59,250
etc..

137
00:10:59,250 --> 00:11:04,420
So let me do a grep recursive grep of I.

138
00:11:05,620 --> 00:11:14,060
I token and password and api and secret.

139
00:11:14,460 --> 00:11:24,660
So I do a recursive grep of this in the entire folder here, and do an extended grep of multiple strings.

140
00:11:24,940 --> 00:11:27,420
And you can see it definitely finds the output.

141
00:11:27,900 --> 00:11:28,940
Let's highlight it.

142
00:11:29,060 --> 00:11:32,540
So I'm going to say please throw some colors.

143
00:11:34,060 --> 00:11:34,460
Yeah.

144
00:11:39,260 --> 00:11:39,740
Okay.

145
00:11:39,860 --> 00:11:45,820
So here we can see it has password token password token.

146
00:11:45,820 --> 00:11:50,420
So there are some kinds of functions or variables that are appearing over here.

147
00:11:50,660 --> 00:11:54,380
Uh there are no there are no actual or real passwords.

148
00:11:54,380 --> 00:12:00,660
But yes, this can definitely turn out to be very, very useful for us, uh, when we are going to find

149
00:12:00,700 --> 00:12:01,500
secrets into it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Web AI Deployment

1
00:00:00,120 --> 00:00:11,800
Standing what is exactly MCP so participants can see on the screen right now a image which depicts how

2
00:00:11,920 --> 00:00:13,720
primarily MCP works.

3
00:00:13,720 --> 00:00:22,560
So you might have heard a lot about MCP as well on social media, if you are following uh, LM and Agentic,

4
00:00:22,560 --> 00:00:24,160
I cursor, AI, etc..

5
00:00:24,160 --> 00:00:28,440
So let's just understand how it exactly works.

6
00:00:28,440 --> 00:00:34,160
And then we are going to set up an MCP server for, uh, the lab setup that we have done yesterday.

7
00:00:35,000 --> 00:00:38,960
So primarily MCP stands for Model Context Protocol.

8
00:00:39,360 --> 00:00:44,960
It is an open standard protocol that has been developed by anthropic AI.

9
00:00:45,400 --> 00:00:48,640
So that's an organization who has developed this given protocol.

10
00:00:48,960 --> 00:00:52,680
Now what's so fancy about this protocol that everyone is talking about?

11
00:00:53,600 --> 00:01:01,160
It is a it is usually a similar protocol that we have for other of our communication purposes.

12
00:01:01,480 --> 00:01:03,280
I will give you an example here.

13
00:01:03,640 --> 00:01:06,800
So let's say uh status codes.

14
00:01:07,200 --> 00:01:13,720
So when a client sends a request to the server, the server responds with a status code.

15
00:01:13,760 --> 00:01:15,200
Let's say 200.

16
00:01:15,240 --> 00:01:15,640
Okay.

17
00:01:16,120 --> 00:01:18,160
Your request is successfully fulfilled.

18
00:01:18,320 --> 00:01:19,760
Or maybe 404.

19
00:01:20,120 --> 00:01:21,440
This isn't standard.

20
00:01:21,720 --> 00:01:25,600
The server gives the status code in the form of 200.

21
00:01:25,640 --> 00:01:25,920
Okay.

22
00:01:25,920 --> 00:01:34,680
It does not give us anything else apart from this because this is a standard that has been created similarly

23
00:01:34,880 --> 00:01:42,320
for communication, for communication for the LMS that we have, which is the large language models

24
00:01:43,520 --> 00:01:49,360
to do a communication with another set of applications, we have a protocol that is going to bridge

25
00:01:49,360 --> 00:01:52,680
this and that is known as Model Context protocol.

26
00:01:53,080 --> 00:02:00,840
This protocol helps the LM to convert natural language processing, that is, the input that has been

27
00:02:00,840 --> 00:02:07,040
given to be connected and executed to n number of applications or tasks.

28
00:02:08,360 --> 00:02:16,470
Let me give you one very simple example between what is the difference or what an LLM cannot do that

29
00:02:16,510 --> 00:02:21,070
MCP can do with enhancing the capabilities of an LLM.

30
00:02:21,110 --> 00:02:21,470
Okay.

31
00:02:22,070 --> 00:02:24,590
So all of us uses ChatGPT, right?

32
00:02:25,630 --> 00:02:31,870
Now you can ask ChatGPT to write an professional email content for you.

33
00:02:32,190 --> 00:02:34,310
Yes, ChatGPT can do that.

34
00:02:34,310 --> 00:02:40,990
But ChatGPT cannot send that email to your recipient or your friend when you will ask it to do it.

35
00:02:41,030 --> 00:02:46,870
It says I cannot do it because it does not have the capabilities to do it.

36
00:02:47,430 --> 00:02:48,870
Let's say one more example.

37
00:02:49,150 --> 00:02:58,350
You ask ChatGPT to write a program for you, but it cannot execute the program and show you the preview,

38
00:02:58,870 --> 00:02:59,390
right?

39
00:02:59,830 --> 00:03:04,310
I hope everyone is able to understand and they would agree with me.

40
00:03:04,870 --> 00:03:10,350
Now the MCP protocol enhances the capabilities of ChatGPT.

41
00:03:10,390 --> 00:03:17,430
Here, for instance, wherein when the email is being written, it also sends the email to the dedicated

42
00:03:17,430 --> 00:03:19,910
or intended recipient of my choice.

43
00:03:19,950 --> 00:03:22,750
Let's say I want to send this email to my friend who is Jerry.

44
00:03:22,950 --> 00:03:31,190
So I will ask the LM or the chat agent to write a professional email, and please send it to Jerry at

45
00:03:31,230 --> 00:03:32,950
maybe 8 p.m..

46
00:03:33,470 --> 00:03:36,070
So everything is automated over here.

47
00:03:36,070 --> 00:03:43,550
So these additional capabilities that the given agent LM agent gets is through the MCP protocol.

48
00:03:43,910 --> 00:03:47,350
So what does exactly MCP protocol do.

49
00:03:47,510 --> 00:03:54,750
So the agent over here, which is ChatGPT or Lama, gets this enhanced capabilities and power in their

50
00:03:54,750 --> 00:03:55,150
hand.

51
00:03:55,590 --> 00:04:02,030
It basically works like an USB port.

52
00:04:02,070 --> 00:04:02,310
Okay.

53
00:04:02,310 --> 00:04:04,550
Let's understand this with a very simple example.

54
00:04:04,590 --> 00:04:05,030
Okay.

55
00:04:05,070 --> 00:04:11,750
So let's say I am currently sitting in front of my laptop or my system, and MCP protocol is going to

56
00:04:11,790 --> 00:04:19,950
behave like a USB port where I can attach maybe a keyboard, a mouse, a keyboard to maybe give inputs

57
00:04:19,950 --> 00:04:24,430
to type something, a mouse to operate the trackpad, and then I can attach a.

58
00:04:24,710 --> 00:04:29,470
A large screen to see a bigger version of the screen, or maybe a projector, or maybe.

59
00:04:29,510 --> 00:04:31,030
A hard disk or a hard drive.

60
00:04:31,470 --> 00:04:39,350
So this basically means that my system, which is currently, uh, the agent, let's say ChatGPT, it's,

61
00:04:39,710 --> 00:04:48,390
it is getting enhanced its capabilities via the USB-C port, which is the MCP protocol, to get additional

62
00:04:48,390 --> 00:04:50,950
capabilities of doing something else.

63
00:04:50,950 --> 00:04:57,550
So let's say if I connect an external projector, it has the capabilities now to give the output on

64
00:04:57,550 --> 00:04:59,110
a very large screen.

65
00:04:59,310 --> 00:05:02,230
If I connect maybe a Bluetooth device now.

66
00:05:02,350 --> 00:05:08,550
So it has the capabilities to connect to external Bluetooth devices or external Bluetooth speakers or

67
00:05:08,550 --> 00:05:09,950
Chromecast, etc..

68
00:05:10,630 --> 00:05:17,950
Uh, so this is how MCP works in a very simple, in a nutshell, uh, example that I have given, uh,

69
00:05:17,990 --> 00:05:24,070
participants, if you just see in the image as well, we can see at the bottom here is the AI application.

70
00:05:24,070 --> 00:05:32,140
And with the help of the MCP protocol, it is gaining more capabilities to connect to a database, fetch,

71
00:05:32,420 --> 00:05:36,500
retrieve, update, delete information from the database.

72
00:05:36,700 --> 00:05:38,340
Previously, it could not do that.

73
00:05:38,380 --> 00:05:43,820
It could generate the SQL code for you, but it could not connect to the database, it could not execute

74
00:05:43,820 --> 00:05:49,140
the query, etc. similarly, you could not send an email earlier on Gmail.

75
00:05:49,140 --> 00:05:51,860
You could not copy all your files.

76
00:05:51,900 --> 00:05:59,260
Now, with the help of MCP protocol, if you give a command to your LM agent, which is here in our

77
00:05:59,260 --> 00:06:06,860
case, and say copy all files from desktop to C drive, it would do that automatically because now it

78
00:06:06,860 --> 00:06:08,620
has access to your file system.

79
00:06:11,980 --> 00:06:12,780
Ah, yes.

80
00:06:13,140 --> 00:06:16,460
So it would basically copy all the files and move to the file system.

81
00:06:16,460 --> 00:06:23,180
If you say copy all the pictures that are currently in the pictures folder to documents folder, it

82
00:06:23,180 --> 00:06:24,420
would do that for you.

83
00:06:24,420 --> 00:06:31,460
So this is how it is now enhancing its capabilities to also execute actions on your system.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:00,560
Works.

2
00:00:00,600 --> 00:00:06,960
If anyone is interested to learn or read more about it, they can definitely go to the official website

3
00:00:06,960 --> 00:00:10,840
which is Model Context protocol.io and read about it.

4
00:00:10,880 --> 00:00:14,280
Okay, so here is one more example that we just discussed.

5
00:00:14,520 --> 00:00:16,720
We have this is your computer.

6
00:00:16,720 --> 00:00:19,760
Your computer contains the host with the MCP client.

7
00:00:20,000 --> 00:00:21,760
The client can be cloud AI.

8
00:00:21,800 --> 00:00:23,600
It could be VSCode IDE.

9
00:00:23,640 --> 00:00:24,960
It could be any other tools.

10
00:00:25,200 --> 00:00:31,200
Then we have multiple MCP servers MCP server a, MCP server B, MCP server C.

11
00:00:31,560 --> 00:00:36,840
These are different servers which are which are designed to perform different tasks.

12
00:00:37,480 --> 00:00:41,120
Uh, in our context that we are going to see today.

13
00:00:42,200 --> 00:00:44,320
Remember it like this or understand it like this.

14
00:00:44,360 --> 00:00:49,160
MCP server A is designed to perform subdomain enumeration.

15
00:00:49,480 --> 00:00:53,600
MCP server B is designed to perform technology detection.

16
00:00:53,880 --> 00:01:01,440
MCP server C is designed to maybe do, uh, crawling of the URLs or taking screenshot of the subdomains

17
00:01:01,440 --> 00:01:02,760
that has been identified.

18
00:01:02,920 --> 00:01:03,360
Okay.

19
00:01:04,920 --> 00:01:11,230
Now, uh, all of this is being connected to local data sources and it can.

20
00:01:11,270 --> 00:01:19,910
These MCP servers can also be controlled through a web API from a remote service that is connected over

21
00:01:19,910 --> 00:01:20,430
the internet.

22
00:01:20,430 --> 00:01:27,790
That basically means participants that my server, which is being which is running currently on the

23
00:01:27,790 --> 00:01:39,830
local host, can also be exposed on the internet, and I can remotely access, uh, my local LM that

24
00:01:39,830 --> 00:01:40,750
has been running.

25
00:01:40,750 --> 00:01:45,870
And not only that, I can execute commands sitting from maybe any part of the world.

26
00:01:45,910 --> 00:01:50,110
Okay, to do this, you can simply utilize Ngrok.

27
00:01:50,150 --> 00:02:01,470
Okay, so Ngrok is a free tool or service that you can utilize that will help you expose your systems,

28
00:02:01,950 --> 00:02:05,750
uh, local connections to public connection.

29
00:02:05,790 --> 00:02:06,230
Okay.

30
00:02:06,270 --> 00:02:09,190
So you can definitely do this with the help of Ngrok.

31
00:02:09,390 --> 00:02:11,630
You can log in.

32
00:02:13,830 --> 00:02:15,690
Let me just login into my account.

33
00:02:16,050 --> 00:02:18,730
So I have just logged in and I'm onto a free account.

34
00:02:19,090 --> 00:02:22,650
Uh, my system is Mac OS, so I'm going to install Ngrok.

35
00:02:23,010 --> 00:02:31,690
Uh, my current, uh, tool that I used to install or, uh, yeah, is brew.

36
00:02:31,690 --> 00:02:33,370
So my package manager is brew.

37
00:02:33,730 --> 00:02:39,570
Uh, if you're on windows, you can choose another platform, go to windows and simply download it using

38
00:02:39,570 --> 00:02:40,010
charcoal.

39
00:02:40,010 --> 00:02:43,290
And if you don't have a package manager go to download and download it.

40
00:02:43,330 --> 00:02:45,610
Download the binary from here directly.

41
00:02:45,650 --> 00:02:48,810
Okay, I can also download the binary directly from here.

42
00:02:48,810 --> 00:02:50,810
So once you download it, you can install it.

43
00:02:50,810 --> 00:02:53,250
You can configure your authentication token.

44
00:02:53,250 --> 00:02:53,970
That's it.

45
00:02:54,010 --> 00:02:55,090
It was so simple.

46
00:02:55,250 --> 00:03:03,810
Now you will see how I will expose my current local LM which is running on port 3000 to the web.

47
00:03:03,850 --> 00:03:06,770
And you guys will be able to access it as well remotely.

48
00:03:07,050 --> 00:03:10,130
So to do that I'm going to say Ngrok http.

49
00:03:10,890 --> 00:03:17,650
That means start uh, an HTTP service and expose my local 3000 port.

50
00:03:17,890 --> 00:03:21,930
So I'm going to expose my local 3000 port and that's it.

51
00:03:21,930 --> 00:03:23,440
The command was so simple.

52
00:03:23,840 --> 00:03:32,920
Once you do that, you can see over here my session is online and this is my forwarding IP.

53
00:03:34,440 --> 00:03:40,800
Now I have my forwarding IP so I can copy this and simply go to my browser and paste it.

54
00:03:41,160 --> 00:03:44,440
Once I do that, you will be able to access my open web UI.

55
00:03:44,800 --> 00:03:47,280
So let me paste this link in the chat as well.

56
00:03:47,320 --> 00:03:47,880
Participants.

57
00:03:47,880 --> 00:03:53,640
You can try to access it and you would be able to access it as well.

58
00:03:53,880 --> 00:03:59,280
My email is Rohit at the rate dot n and my password is root.

59
00:03:59,600 --> 00:04:00,720
So once you do that.

60
00:04:02,960 --> 00:04:10,840
You should be able to see this window appearing in front of you where you can see my past chats that

61
00:04:10,840 --> 00:04:12,760
I have done and the web interface.

62
00:04:12,760 --> 00:04:18,400
And I can just I can point this to maybe a simple DNS service as well.

63
00:04:18,640 --> 00:04:22,480
And I can open this at any point of time that I want in future.

64
00:04:22,480 --> 00:04:32,140
So this is like a public facing ChatGPT instance for me, but running my own private LM service on my

65
00:04:32,140 --> 00:04:40,260
local system, with 100% privacy and no sharing of my chats or queries or etc. to the third party server

66
00:04:40,300 --> 00:04:41,180
like ChatGPT.

67
00:04:41,260 --> 00:04:47,780
So this is a completely offline local solution, but which is exposed currently over web so that I can

68
00:04:47,780 --> 00:04:50,220
access it remotely anywhere that I want.

69
00:04:51,340 --> 00:04:51,820
Okay.

70
00:04:51,860 --> 00:04:52,940
How did we do that?

71
00:04:52,980 --> 00:04:55,540
We simply signed up on NBC.com.

72
00:04:55,540 --> 00:05:01,180
We downloaded the binary, we unzipped it, and then we added our authentication token.

73
00:05:01,180 --> 00:05:05,140
So so this authentication token is binded to your email address.

74
00:05:05,140 --> 00:05:12,300
Hence it automatically identifies that this authentication token is pertaining to a user which is rohith

75
00:05:12,300 --> 00:05:12,860
at the Red hat.

76
00:05:13,180 --> 00:05:13,940
And that's it.

77
00:05:14,180 --> 00:05:17,260
Your public web address is started.

78
00:05:21,860 --> 00:05:22,260
Okay.

79
00:05:22,260 --> 00:05:27,900
So I can see a lot of attempts of participants coming up over here in the HTTP request.

80
00:05:27,900 --> 00:05:30,900
So you might be attempting to access this.

81
00:05:31,100 --> 00:05:38,180
So once you access this you would be able to log in and you would be able to access my local setup over

82
00:05:38,180 --> 00:05:38,620
here.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:02,960
We are going to go back to Obama.

2
00:00:03,680 --> 00:00:09,120
So Obama is currently running, we can see here go to Open Web UI.

3
00:00:09,160 --> 00:00:09,680
Awesome.

4
00:00:12,920 --> 00:00:13,320
Yeah.

5
00:00:16,360 --> 00:00:16,960
Great.

6
00:00:17,000 --> 00:00:23,360
Now once we are at Open Web UI, we are going to do a small configuration change.

7
00:00:23,480 --> 00:00:27,400
So to be sure that it runs perfectly fine.

8
00:00:27,400 --> 00:00:29,720
And our MCP server is configured.

9
00:00:29,720 --> 00:00:31,160
So you need to go to settings.

10
00:00:32,400 --> 00:00:35,360
And in the settings you need to go to the tools section.

11
00:00:35,400 --> 00:00:35,840
Okay.

12
00:00:36,280 --> 00:00:39,800
Once you go to the tools section you need to click on this add connection.

13
00:00:40,040 --> 00:00:43,720
And here you are going to set up your MCP server.

14
00:00:43,760 --> 00:00:44,200
Okay.

15
00:00:44,480 --> 00:00:47,320
Now there is a small catch over here.

16
00:00:48,520 --> 00:00:59,880
That is the open web UI interface only supports MCP server with a valid open API structure.

17
00:01:00,160 --> 00:01:04,500
So how to make open API API structure for your tool.

18
00:01:04,620 --> 00:01:06,980
It is absolutely dead simple.

19
00:01:07,220 --> 00:01:09,100
Okay, so I'll show you how to do that.

20
00:01:09,100 --> 00:01:10,860
And then we add the connection over here.

21
00:01:10,860 --> 00:01:12,420
And then we test out our tool.

22
00:01:12,700 --> 00:01:13,180
Okay.

23
00:01:13,220 --> 00:01:20,380
So let's first create a simple uh app dot pi or a flask application to do our task.

24
00:01:20,660 --> 00:01:24,900
So before the session I have already created an app dot pi.

25
00:01:26,340 --> 00:01:27,820
Uh, so I'm going to show you that.

26
00:01:27,820 --> 00:01:29,740
So let me show you the code for it.

27
00:01:38,620 --> 00:01:39,060
Yeah.

28
00:01:43,500 --> 00:01:52,100
Okay, so this file, it might look very, uh, long or a lot of code would be there, but it is very,

29
00:01:52,100 --> 00:01:52,980
very simple.

30
00:01:53,180 --> 00:01:58,020
Let me just keep only run sub finder method and I'll remove everything else.

31
00:02:03,180 --> 00:02:03,660
Okay.

32
00:02:03,900 --> 00:02:06,660
So let me let me remove HTTP.

33
00:02:06,950 --> 00:02:09,910
We don't want to use HTTP go.

34
00:02:10,390 --> 00:02:14,590
So just to be very very keep it very very simple for you to understand.

35
00:02:14,630 --> 00:02:14,990
Okay.

36
00:02:15,670 --> 00:02:16,230
Nice.

37
00:02:16,390 --> 00:02:22,030
So this is the very simple project which is going to help us set up an MVP server.

38
00:02:22,070 --> 00:02:22,230
Okay.

39
00:02:22,270 --> 00:02:23,670
So let's understand this.

40
00:02:23,750 --> 00:02:25,150
So first is the boilerplate.

41
00:02:25,150 --> 00:02:32,070
We are going to import flask to run a flask server and a subprocess to run subprocess and OS to run

42
00:02:32,070 --> 00:02:32,910
OS commands.

43
00:02:33,190 --> 00:02:40,990
And open web UI requires us to also use course configuration correctly.

44
00:02:40,990 --> 00:02:48,070
You can see here course must be properly configured by the provider to allow request from open web UI.

45
00:02:48,190 --> 00:02:53,710
It is saying that it won't connect to MCP servers that do not specify course policy.

46
00:02:53,750 --> 00:02:59,790
Hence we are going to now import course as well so that we can write a simple course policy.

47
00:03:00,110 --> 00:03:00,790
That's it.

48
00:03:00,830 --> 00:03:04,150
Now uh app course app.

49
00:03:04,150 --> 00:03:05,270
So this is the name.

50
00:03:05,790 --> 00:03:11,610
And what we are going to do is I'll skip this part because this is a function which says run the tool

51
00:03:11,850 --> 00:03:14,490
and there is a route that we have created.

52
00:03:14,490 --> 00:03:20,410
Run sub finder with the method post and we are going to run the tool.

53
00:03:21,290 --> 00:03:28,450
The tool name is sub finder hyphen D domain name, and the domain that will be given from the chat.

54
00:03:28,730 --> 00:03:33,090
Using natural language processing, that input will be taken as an.

55
00:03:33,090 --> 00:03:37,610
A silent flag is given over here, and the output and the sub finder tool will be run.

56
00:03:38,170 --> 00:03:42,050
So once the command is being run it is going to give us the output.

57
00:03:42,090 --> 00:03:42,570
Okay.

58
00:03:42,610 --> 00:03:44,010
So this is how it works.

59
00:03:44,050 --> 00:03:50,210
Now there is one more route over here which is for open API, a simple route.

60
00:03:50,210 --> 00:03:56,330
And it says that the open API dot JSON file is in the static web well-known folder.

61
00:03:56,770 --> 00:03:57,610
And that's it.

62
00:03:57,610 --> 00:04:01,810
The application should run on any address on port 5050.

63
00:04:02,810 --> 00:04:06,050
Uh, a very, very simple flask application.

64
00:04:06,290 --> 00:04:10,810
You can generate these types of flask application with the help of Allama.

65
00:04:10,850 --> 00:04:13,140
Also I'll give you this sample.

66
00:04:13,140 --> 00:04:17,300
Don't worry if you are not familiar with Python programming.

67
00:04:18,060 --> 00:04:18,820
Copy this.

68
00:04:19,140 --> 00:04:21,260
Give it to your local ulama.

69
00:04:21,780 --> 00:04:23,020
Uh, agent.

70
00:04:23,380 --> 00:04:23,780
Okay.

71
00:04:23,820 --> 00:04:28,700
And ask it to add more tools for you over here.

72
00:04:28,700 --> 00:04:32,380
And automatically it is going to add new routes and new tools.

73
00:04:32,740 --> 00:04:33,020
Okay.

74
00:04:33,060 --> 00:04:39,580
The way that I had so I had tools that were Wayback URLs and nuclei.

75
00:04:39,780 --> 00:04:43,100
But I've removed that just for simplicity for your understanding.

76
00:04:43,140 --> 00:04:43,500
Okay.

77
00:04:43,540 --> 00:04:48,660
So this was the main, uh, main program, main Python application.

78
00:04:48,860 --> 00:04:52,820
And let's see quickly the open API, JSON as well.

79
00:04:52,820 --> 00:04:54,180
And then we will set this up.

80
00:04:54,940 --> 00:04:56,260
That is very dead simple.

81
00:04:56,260 --> 00:04:58,860
Again let's see the OpenAPI JSON file.

82
00:04:59,180 --> 00:04:59,660
Yeah.

83
00:04:59,660 --> 00:05:01,460
So this is the OpenAPI JSON file.

84
00:05:02,380 --> 00:05:04,420
It is still here only.

85
00:05:05,100 --> 00:05:11,980
The next part is for HTTP and then nuclei and doing Wayback URLs, Screenshotting etc. etc..

86
00:05:12,020 --> 00:05:12,420
Okay.

87
00:05:12,540 --> 00:05:13,900
It is still here only.

88
00:05:14,140 --> 00:05:15,440
So let's understand this.

89
00:05:16,560 --> 00:05:20,760
Uh, currently we are using OpenAI API version three info.

90
00:05:20,880 --> 00:05:24,520
So the name of the API is MCP recon API.

91
00:05:24,560 --> 00:05:25,680
This is our version.

92
00:05:26,080 --> 00:05:28,240
You can give anything that you want over here.

93
00:05:28,480 --> 00:05:29,600
This is the main part.

94
00:05:31,960 --> 00:05:32,320
Yeah.

95
00:05:32,800 --> 00:05:35,360
So we are going to give a path that is run sub finder.

96
00:05:35,360 --> 00:05:43,080
Because this is the same path that we specified in our app dot Pi here which is run sub finder.

97
00:05:43,480 --> 00:05:44,760
So this is our route.

98
00:05:45,120 --> 00:05:53,720
So the same thing is in our API configuration and operation ID run sub finder summary run sub finder.

99
00:05:53,960 --> 00:05:55,440
We require a body.

100
00:05:55,720 --> 00:05:56,960
Yes we require it.

101
00:05:57,400 --> 00:05:59,320
The content is in JSON format.

102
00:05:59,560 --> 00:06:00,320
What is required?

103
00:06:00,320 --> 00:06:01,600
A domain is required.

104
00:06:01,720 --> 00:06:02,760
Okay that's it.

105
00:06:03,760 --> 00:06:06,200
The responses give a description.

106
00:06:06,200 --> 00:06:09,760
Sub domains discovered successfully when the task is completed.

107
00:06:09,760 --> 00:06:10,880
Very very simple.

108
00:06:11,160 --> 00:06:13,440
Now you have a JSON file ready.

109
00:06:13,440 --> 00:06:14,960
OpenAPI JSON file ready.

110
00:06:14,960 --> 00:06:17,200
You have the Python code ready.

111
00:06:17,200 --> 00:06:18,450
So let's run this.

112
00:06:18,490 --> 00:06:18,890
Okay.

113
00:06:18,930 --> 00:06:20,770
So I'm going to run the Python code.

114
00:06:21,330 --> 00:06:25,770
To run that you can simply say Python three app dot pi and hit enter.

115
00:06:26,050 --> 00:06:32,330
Before that participants you have to make sure that your OpenAPI dot JSON file is currently in the static

116
00:06:32,330 --> 00:06:32,890
folder.

117
00:06:33,010 --> 00:06:37,810
So go to static folder and create a hidden folder which is dot well-known.

118
00:06:38,370 --> 00:06:39,610
Go to Dot well-known.

119
00:06:40,090 --> 00:06:45,370
And here you can see that your open API dot JSON file is there that we just created.

120
00:06:45,930 --> 00:06:51,770
So this is the run sub MCP sub finder executor where I have given this name.

121
00:06:51,770 --> 00:06:59,250
You can give any name that you want which basically does what it simply only runs sub finder and do

122
00:06:59,290 --> 00:07:01,330
sub domain enumeration for us.

123
00:07:01,330 --> 00:07:01,970
That's it.

124
00:07:02,290 --> 00:07:02,730
Okay.

125
00:07:03,130 --> 00:07:03,850
Looks good.

126
00:07:04,170 --> 00:07:05,330
Let's go back.

127
00:07:08,970 --> 00:07:12,810
And yeah let's go back.

128
00:07:12,810 --> 00:07:14,130
And we are going to run this.

129
00:07:14,330 --> 00:07:16,490
So Python three app dot pi.

130
00:07:17,210 --> 00:07:22,390
So once you run this you can see your server has started successfully on port 5050.

131
00:07:22,950 --> 00:07:26,870
As we saw in the code run on 5050.

132
00:07:27,110 --> 00:07:28,790
And listen on any address.

133
00:07:28,830 --> 00:07:29,550
Excellent.

134
00:07:29,950 --> 00:07:32,310
Now participant comes the last step.

135
00:07:32,670 --> 00:07:35,270
Go to your browser.

136
00:07:35,670 --> 00:07:36,950
Go to your settings.

137
00:07:36,950 --> 00:07:37,990
How to go to the settings.

138
00:07:37,990 --> 00:07:38,750
Click here.

139
00:07:38,790 --> 00:07:39,750
Go to settings.

140
00:07:40,110 --> 00:07:42,790
Go to tools manage tool servers.

141
00:07:42,910 --> 00:07:43,990
Click on plus.

142
00:07:44,350 --> 00:07:45,710
That is add connection.

143
00:07:46,390 --> 00:07:49,750
And once you do add connection you should be able to see a window like this.

144
00:07:50,350 --> 00:07:52,230
Add your server address.

145
00:07:52,510 --> 00:07:56,230
Copy the address from here and paste it here.

146
00:07:56,870 --> 00:08:01,230
Okay, now you need to give the path here as well.

147
00:08:01,230 --> 00:08:03,190
Open API dot JSON path.

148
00:08:03,310 --> 00:08:05,550
So where is your open API dot JSON path.

149
00:08:05,590 --> 00:08:09,590
It is at dot well known open API dot JSON.

150
00:08:09,750 --> 00:08:14,990
Okay, once you do this we don't have any authentication.

151
00:08:15,230 --> 00:08:18,150
That means our API is not behind a username and password.

152
00:08:18,150 --> 00:08:22,310
So keep this blank and click on this Verify connection button.

153
00:08:22,590 --> 00:08:24,520
Once you click this and you get a connection.

154
00:08:24,520 --> 00:08:25,400
Successful.

155
00:08:25,400 --> 00:08:26,720
Congratulations.

156
00:08:26,920 --> 00:08:34,680
Your MCP server has been successfully connected with Open Web UI which is running in the back end.

157
00:08:34,880 --> 00:08:36,960
Your Olama LM model.

158
00:08:36,960 --> 00:08:37,960
Congratulations!

159
00:08:38,400 --> 00:08:41,840
Click on save and you will see setting saved successfully.

160
00:08:41,840 --> 00:08:46,520
Click on save once again and close this now participant.

161
00:08:46,520 --> 00:08:48,200
Can you see this plus button?

162
00:08:48,200 --> 00:08:53,160
Please click on the plus button and you will be able to see here MCP Sub Finder.

163
00:08:53,200 --> 00:08:54,040
What is this?

164
00:08:54,200 --> 00:08:59,120
This is the MCP tool that we have just configured and this is the name of it.

165
00:08:59,160 --> 00:09:02,000
We gave the name as MCP Sub Finder executed.

166
00:09:02,040 --> 00:09:03,560
You have to enable this.

167
00:09:03,640 --> 00:09:06,040
Once you enable this you click here.

168
00:09:06,240 --> 00:09:08,960
And you can see we have two tools currently.

169
00:09:09,960 --> 00:09:11,240
Uh two tools for us.

170
00:09:11,240 --> 00:09:20,240
First is MCP sub finder Executor which basically runs sub run sub finder root and do sub domain enumeration

171
00:09:20,240 --> 00:09:20,920
for us.

172
00:09:20,920 --> 00:09:22,840
And second is the MCP sub finder executor.

173
00:09:22,840 --> 00:09:25,280
So I had two tools that I have added over here.

174
00:09:25,720 --> 00:09:26,360
Excellent.

175
00:09:26,600 --> 00:09:27,040
Now.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: Tool-Based Recon

1
00:00:01,520 --> 00:00:03,360
Please make sure that it is on.

2
00:00:03,800 --> 00:00:07,320
Once this is on, let's test this out.

3
00:00:07,320 --> 00:00:08,600
So I'm going to give in command.

4
00:00:08,600 --> 00:00:14,600
So participants, you might have noticed yesterday we were getting less number of output of sub domains.

5
00:00:14,800 --> 00:00:17,440
Now today you will see more output.

6
00:00:17,440 --> 00:00:20,160
So I'm going to say use tool.

7
00:00:22,200 --> 00:00:30,240
Do subdomain enumeration for tesla.com and print all the sub domains.

8
00:00:32,040 --> 00:00:32,640
That's it.

9
00:00:32,640 --> 00:00:33,640
Let's hit enter.

10
00:00:34,080 --> 00:00:36,720
You should be able to see a hit coming up over here.

11
00:00:37,040 --> 00:00:41,960
So first your open API has been read and fetched okay.

12
00:00:42,000 --> 00:00:51,640
And now you can see a run sub finder request will be sent automatically and it will execute in the background

13
00:00:51,640 --> 00:00:52,160
for you.

14
00:00:53,000 --> 00:00:56,680
Get all the sub domains identified and printed on your screen.

15
00:01:04,700 --> 00:01:10,060
And you can see over here the list of subdomains starts have been started printing for you.

16
00:01:13,820 --> 00:01:19,260
You can see a Post request has been sent successfully on run sub finder.

17
00:01:21,620 --> 00:01:24,940
Route and you can see your output over here.

18
00:01:25,220 --> 00:01:27,380
Okay congratulations participants.

19
00:01:27,380 --> 00:01:35,140
We have successfully configured our MCP server with Open web UI with unlimited search queries that you

20
00:01:35,140 --> 00:01:39,900
want to do, and it has now successfully identified all the subdomains for you.

21
00:01:41,100 --> 00:01:41,380
Yes.

22
00:01:41,380 --> 00:01:43,180
Participants, are you all with me?

23
00:01:43,220 --> 00:01:44,300
Able to understand?

24
00:01:45,860 --> 00:01:52,180
There might be a lot of steps involved over here, but it is only one time configuration.

25
00:01:52,220 --> 00:01:55,220
Don't worry about that once you do it only once.

26
00:01:55,540 --> 00:01:59,100
Uh, then from future, you don't have to do all of those configurations.

27
00:01:59,100 --> 00:02:05,110
You just have to add keep on adding your tools to the Python application and that's it.

28
00:02:05,310 --> 00:02:12,630
And we will use Olama only to modify the Python application to add more tools.

29
00:02:12,830 --> 00:02:13,670
Let's see how.

30
00:02:19,270 --> 00:02:20,590
Okay I'm going to copy this.

31
00:02:21,270 --> 00:02:22,110
I'm going to say hi.

32
00:02:22,830 --> 00:02:33,550
Read the below Python flask application and enhance the.

33
00:02:45,590 --> 00:02:46,230
To do.

34
00:02:53,630 --> 00:02:57,670
Detection using HTTP tool.

35
00:02:58,070 --> 00:02:58,390
Okay.

36
00:03:00,170 --> 00:03:00,690
Okay.

37
00:03:00,850 --> 00:03:02,130
Let's give the code.

38
00:03:04,850 --> 00:03:06,690
For starts from here, let's hit enter.

39
00:03:08,370 --> 00:03:08,610
Yeah.

40
00:03:08,610 --> 00:03:09,850
It was a passive enumeration.

41
00:03:09,850 --> 00:03:13,410
So it has listed all of the subdomains for us right.

42
00:03:16,490 --> 00:03:16,810
Okay.

43
00:03:16,810 --> 00:03:22,130
So now it is going to again run this and it is going to enhance the application for us and give us the

44
00:03:22,130 --> 00:03:22,850
output.

45
00:03:23,290 --> 00:03:26,690
And based on that you can keep on adding more and more tools.

46
00:03:26,690 --> 00:03:29,690
So after doing subdomain enumeration what do you want to do.

47
00:03:29,730 --> 00:03:31,690
You want to do technology detection.

48
00:03:32,050 --> 00:03:33,410
After technology detection.

49
00:03:33,410 --> 00:03:34,370
What do you want to do?

50
00:03:34,410 --> 00:03:37,650
You want to do, uh, crawling of URLs?

51
00:03:37,810 --> 00:03:40,010
After crawling of URLs, what do you want to do?

52
00:03:40,050 --> 00:03:43,210
You want to take screenshots and so on.

53
00:03:43,210 --> 00:03:43,690
Okay.

54
00:03:43,730 --> 00:03:48,250
So now you can see it has automatically said created the updated code for you.

55
00:03:48,290 --> 00:03:49,010
Excellent.

56
00:03:49,290 --> 00:03:54,690
And it says the new endpoint is run HTTP detection with a JSON payload.

57
00:03:54,930 --> 00:03:59,990
Uh, that it is going to request and it is going to run this uh using HTTP.

58
00:04:00,470 --> 00:04:01,030
Excellent.

59
00:04:01,030 --> 00:04:02,430
Looks very very nice.

60
00:04:02,630 --> 00:04:04,110
And now we can run this.

61
00:04:04,470 --> 00:04:09,310
So to run this we are going to run it directly here.

62
00:04:09,310 --> 00:04:12,030
And we are going to expect the output.

63
00:04:14,150 --> 00:04:14,590
Okay.

64
00:04:15,390 --> 00:04:17,070
Here we got an error.

65
00:04:17,110 --> 00:04:18,270
No module name.

66
00:04:19,590 --> 00:04:19,870
Okay.

67
00:04:19,910 --> 00:04:21,510
Did it not import flask.

68
00:04:21,550 --> 00:04:21,910
Okay.

69
00:04:22,270 --> 00:04:25,110
Let me copy this and run it again.

70
00:04:28,110 --> 00:04:36,230
So this time I'm going to stop this and I'm going to say nano app Dot Pi or let's say app one dot Pi.

71
00:04:36,670 --> 00:04:42,270
Paste this and I'm going to say Python three app one dot pi.

72
00:04:42,790 --> 00:04:43,310
Awesome.

73
00:04:43,310 --> 00:04:44,270
It has started.

74
00:04:44,670 --> 00:04:52,510
Now let's go back to, uh, Open Web UI and llama and refresh this.

75
00:04:53,670 --> 00:05:00,810
Once you refresh this let's go to When available tools and okay, it has not loaded.

76
00:05:00,850 --> 00:05:06,810
Oh, it has not loaded that because our open API JSON configuration is still not updated.

77
00:05:06,810 --> 00:05:07,170
Okay.

78
00:05:07,210 --> 00:05:12,210
So let's update that because you can see it first fetches your open API configuration.

79
00:05:12,410 --> 00:05:13,690
And we did not update it.

80
00:05:13,690 --> 00:05:14,890
So let's update that.

81
00:05:16,130 --> 00:05:17,530
So I'm going to copy this.

82
00:05:31,810 --> 00:05:33,290
And give it here.

83
00:05:35,010 --> 00:05:37,330
Yes we are creating the route.

84
00:05:37,330 --> 00:05:38,930
It will automatically create the route.

85
00:05:39,530 --> 00:05:46,490
Also update the JSON file and make the route.

86
00:05:56,900 --> 00:06:04,980
If you want to use a tool that is configured in NCP tool configured, yes, you need to tell llama,

87
00:06:05,580 --> 00:06:10,820
uh, your prompt that and your prompt should start with use tool so it automatically understands that

88
00:06:10,820 --> 00:06:11,940
you want to use a tool.

89
00:06:14,740 --> 00:06:15,100
Okay.

90
00:06:15,260 --> 00:06:19,620
Now you can see here's the updated route run HTTP text detection.

91
00:06:20,340 --> 00:06:20,660
Awesome.

92
00:06:20,660 --> 00:06:23,300
And you can see you can use this route in the flask application.

93
00:06:23,300 --> 00:06:24,900
The route is already added.

94
00:06:24,900 --> 00:06:26,140
It is also added here.

95
00:06:26,140 --> 00:06:31,260
So I'm going to copy this and I'm going to go to the.

96
00:06:34,380 --> 00:06:35,220
Folder.

97
00:06:40,300 --> 00:06:44,340
And say go to static LRS hyphen.

98
00:06:44,380 --> 00:06:56,000
All go to well-known LS hyphen all open open API dot JSON modify sorry modify it because now it has

99
00:06:56,000 --> 00:06:56,840
a new route.

100
00:06:57,200 --> 00:06:57,720
Awesome.

101
00:06:58,240 --> 00:06:59,120
Let's go back.

102
00:07:00,880 --> 00:07:05,680
And yeah, the route has been added successfully.

103
00:07:07,800 --> 00:07:12,120
Uh, successfully in open API dot JSON.

104
00:07:12,120 --> 00:07:13,720
We just added the new route.

105
00:07:14,080 --> 00:07:20,400
Let's go to Open Web UI and go to the tools.

106
00:07:22,840 --> 00:07:31,200
And congratulations, we have successfully added a new HTTP tag detection module with our MVP server.

107
00:07:31,200 --> 00:07:36,760
That was that two was generated by the same LM agent for us.

108
00:07:36,920 --> 00:07:37,560
Did you see that?

109
00:07:37,600 --> 00:07:38,720
How easy it was.

110
00:07:39,120 --> 00:07:45,160
So we you we created our first code block to do subdomain enumeration.

111
00:07:45,160 --> 00:07:53,160
And then we asked llama itself to modify it and add a new functionality of technology detection in the

112
00:07:53,160 --> 00:07:53,720
code.

113
00:07:53,840 --> 00:07:56,020
And we also updated the API.

114
00:07:56,460 --> 00:08:00,820
And after doing that successfully here, we just refreshed.

115
00:08:00,980 --> 00:08:06,260
And now you are able to see a new added functionality that we have that is run HTTP detection.

116
00:08:06,260 --> 00:08:07,740
Now it's time to use that.

117
00:08:08,180 --> 00:08:18,980
Okay so do subdomain enumeration use tool do subdomain enumeration on app dot n.

118
00:08:24,220 --> 00:08:28,180
And then perform technology.

119
00:08:28,500 --> 00:08:32,980
Technology detection on them using HTTP.

120
00:08:33,940 --> 00:08:34,940
Let's hit enter.

121
00:08:40,740 --> 00:08:44,900
We have started slow so that we don't get confused.

122
00:08:44,900 --> 00:08:45,900
Participants.

123
00:08:45,900 --> 00:08:50,020
We have successfully created one block of MCP server.

124
00:08:56,440 --> 00:09:00,520
Let's run Shop Finder to do this and http right.

125
00:09:00,840 --> 00:09:02,920
Yeah we have we have all of these tools.

126
00:09:03,080 --> 00:09:03,480
Okay.

127
00:09:04,120 --> 00:09:09,000
I think uh, it did not appropriately get what we wanted to do.

128
00:09:13,200 --> 00:09:13,560
Yeah.

129
00:09:13,720 --> 00:09:14,760
Because it was off.

130
00:09:15,120 --> 00:09:15,440
Yes.

131
00:09:15,440 --> 00:09:16,800
We did not enable it.

132
00:09:17,040 --> 00:09:18,280
Now let's enable it.

133
00:09:18,920 --> 00:09:19,280
Uh, yes.

134
00:09:19,280 --> 00:09:19,840
You are right.

135
00:09:20,120 --> 00:09:21,200
We did not enable it.

136
00:09:21,200 --> 00:09:22,840
Now, once we have enabled it.

137
00:09:22,840 --> 00:09:24,320
Now, let's do this once more.

138
00:09:26,040 --> 00:09:27,760
You can see it is enabled now.

139
00:09:48,960 --> 00:09:49,600
Yes.

140
00:09:49,600 --> 00:09:50,560
Did you see this?

141
00:09:50,880 --> 00:09:54,050
Uh, we have already found the subdomains output here.

142
00:09:54,210 --> 00:09:59,450
I'm not sure why we received this output, because it is, I think, using the context of our previous

143
00:10:00,370 --> 00:10:00,930
chat.

144
00:10:00,970 --> 00:10:07,410
But you can see the output for results for dot in and the text detection.

145
00:10:11,010 --> 00:10:11,410
Okay.

146
00:10:11,930 --> 00:10:14,370
The text detection did not happen appropriately.

147
00:10:14,370 --> 00:10:15,770
There was an internal server error.

148
00:10:15,770 --> 00:10:17,290
We can try that once again.

149
00:10:17,290 --> 00:10:24,250
But yes, we were able to successfully see the output of the subdomain enumeration for dot in correctly

150
00:10:24,250 --> 00:10:24,810
over here.

151
00:10:25,210 --> 00:10:28,930
I think we should start a new chat and then do the same thing.

152
00:10:28,970 --> 00:10:31,410
It should work appropriately.

153
00:10:37,210 --> 00:10:37,370
Okay.

154
00:10:37,410 --> 00:10:40,010
Enabled use of finder.

155
00:10:40,530 --> 00:10:40,810
Sorry.

156
00:10:40,850 --> 00:10:41,650
Use tool.

157
00:10:42,530 --> 00:10:51,650
Run sub finder to root subdomain enumeration on slack account.

158
00:11:07,030 --> 00:11:12,150
Yes, we can see we have received a Post request to run a sub finder and.

159
00:11:14,430 --> 00:11:22,430
Found 123 sub domains and Output.txt is the file that will save the results.

160
00:11:22,430 --> 00:11:24,030
So you should be able to see the output dot.

161
00:11:24,030 --> 00:11:25,270
TXT file as well.

162
00:11:25,670 --> 00:11:29,230
And all of those results will be saved into that file.

163
00:11:30,350 --> 00:11:37,270
Okay so in the output dot txt file you can see all of these 123 sub domains created successfully.

164
00:11:37,790 --> 00:11:38,070
Okay.

165
00:11:38,070 --> 00:11:39,670
Which means this was successful.

166
00:11:39,710 --> 00:11:42,190
Now we can say uh.

167
00:11:45,590 --> 00:11:50,230
Run HTTP extract detection only found.

168
00:11:52,490 --> 00:11:54,930
Some domains above.

169
00:11:59,410 --> 00:12:03,290
And now it should call the post run HTTP extract detection module.

170
00:12:12,250 --> 00:12:14,090
I think there is an attribute error.

171
00:12:14,090 --> 00:12:14,730
Let's see.

172
00:12:14,730 --> 00:12:16,090
Let's see the output first.

173
00:12:29,930 --> 00:12:38,970
Okay I guess uh we there could be a small indentation or other issue I guess in the file.

174
00:12:38,970 --> 00:12:41,090
Hence we have got a 500 internal server error.

175
00:12:41,090 --> 00:12:42,730
Hence we are not able to get the output.

176
00:12:42,730 --> 00:12:44,170
But that can be fixed.

177
00:12:44,210 --> 00:12:46,490
Of course we can fix that.

178
00:12:46,490 --> 00:12:52,780
And then we will be able to detect detection similarly of how we were able to do the subdomain enumeration

179
00:12:52,780 --> 00:12:54,420
by running the sub finder module.

180
00:12:56,060 --> 00:13:00,740
I hope participants you are with me and able to understand the same thing.

181
00:13:07,380 --> 00:13:09,660
Okay, it started doing.

182
00:13:12,900 --> 00:13:13,300
Okay.

183
00:13:15,580 --> 00:13:21,980
It started doing partially the tech detection of some of the domains, as you can see over here.

184
00:13:22,940 --> 00:13:23,420
Okay.

185
00:13:23,540 --> 00:13:25,100
Uh, participants, please let me know.

186
00:13:25,540 --> 00:13:31,100
Are you all with me or is it overwhelming for all participants here?

187
00:13:33,940 --> 00:13:34,940
Uh, please let me know.

188
00:13:34,980 --> 00:13:36,060
Are you all with me?

189
00:13:36,940 --> 00:13:40,740
Able to understand slowly and steadily.

190
00:13:40,740 --> 00:13:41,260
Yes.

191
00:13:46,460 --> 00:13:47,020
Yes.

192
00:13:47,740 --> 00:13:49,220
Uh, I have received very less.

193
00:13:49,240 --> 00:13:49,600
Yes.

194
00:13:49,600 --> 00:13:53,280
Participants, please let me know if you all are with me.

195
00:13:55,560 --> 00:13:57,480
Excellent, excellent.

196
00:14:01,200 --> 00:14:01,840
Excellent.

197
00:14:03,440 --> 00:14:10,960
So if you have any, if you have any queries that you come across while you practice, I'm going to

198
00:14:10,960 --> 00:14:11,440
help you.

199
00:14:11,480 --> 00:14:12,680
Don't worry about it.

200
00:14:13,040 --> 00:14:14,360
I can definitely understand.

201
00:14:14,360 --> 00:14:21,120
This is something which is very new for all participants, so they you might not be able to grasp it

202
00:14:21,160 --> 00:14:22,560
in the first attempt.

203
00:14:22,560 --> 00:14:23,080
Maybe.

204
00:14:23,800 --> 00:14:26,240
Uh, I can definitely understand that.

205
00:14:26,240 --> 00:14:34,760
You need to you need to run this same, uh, setup once when on your system, and then you would be

206
00:14:34,760 --> 00:14:37,640
able to do it very, very easily.

207
00:14:37,680 --> 00:14:37,960
Okay.

208
00:14:38,000 --> 00:14:42,720
It's just a one time setup configuration, uh, thing.

209
00:14:42,720 --> 00:14:46,640
And once you are able to do it successfully, then you can run it as many as times you want.

210
00:14:46,680 --> 00:14:47,120
Okay.

211
00:14:47,320 --> 00:14:48,900
As we were able to do it.

212
00:14:48,900 --> 00:14:51,220
So we did a subdomain enumeration initially.

213
00:14:51,220 --> 00:14:53,940
Then we added a HTTP tag detection module.

214
00:14:53,940 --> 00:15:01,060
Similarly, you can keep on adding modules to it and you can make an make an and very nice MVP server

215
00:15:01,060 --> 00:15:03,980
that automatically does all of these tasks for you.

216
00:15:04,260 --> 00:15:10,420
Okay, so I'm also planning to do the same as we eventually move forward for our sessions.

217
00:15:11,060 --> 00:15:11,540
Okay.

218
00:15:11,580 --> 00:15:17,700
We would gradually try to give more features and functionalities to our tool.

219
00:15:18,060 --> 00:15:25,420
So by the end of the fifth day, our tool would be capable to do, let's say, 5 to 6 or 5 to 7 tasks

220
00:15:25,780 --> 00:15:28,580
for us with the help of the MCP protocol.

221
00:15:28,580 --> 00:15:37,060
So we are just going to input chat commands to the Lama using the open web UI, and it automatically

222
00:15:37,060 --> 00:15:39,180
does all of the tasks in the background for us.

223
00:15:39,220 --> 00:15:45,940
Okay, these specific tasks are for recon, but you can ask it to do any of other tasks that you want

224
00:15:45,980 --> 00:15:46,580
as well.

225
00:15:46,740 --> 00:15:50,920
The same code block can also be created with the help of lemma 3.1.

226
00:15:50,960 --> 00:15:59,960
You can ask the model itself to generate the program for you, and then you can add it to the App.py

227
00:16:00,000 --> 00:16:02,080
as well as the API dot JSON file.

228
00:16:03,960 --> 00:16:04,200
Yes.

229
00:16:04,200 --> 00:16:05,040
Participants.

230
00:16:06,360 --> 00:16:08,520
Uh, we have added the code for http.

231
00:16:08,760 --> 00:16:11,080
Do we need HTTP to be installed on the system?

232
00:16:11,080 --> 00:16:11,480
Yes.

233
00:16:11,760 --> 00:16:18,200
So all of those tools that you are adding in the code to run should be installed into your system,

234
00:16:18,440 --> 00:16:25,000
uh, be it HTTP nuclei or any other tools that you want to be executed, it should be a part of your

235
00:16:25,000 --> 00:16:25,520
system.

236
00:16:31,200 --> 00:16:33,040
Uh, yes we can.

237
00:16:35,440 --> 00:16:36,760
Yes, that is correct.

238
00:16:37,200 --> 00:16:41,440
The current, uh, configurations that we have done is for passive recon.

239
00:16:41,720 --> 00:16:43,800
The same can be done for active recon.

240
00:16:44,360 --> 00:16:50,930
Uh, so participants, if you can recall Call yesterday's session, we created a script subgroup.sh,

241
00:16:51,330 --> 00:16:57,370
which was running in the background, which helped us identify a sub domain that we did not found using

242
00:16:57,370 --> 00:16:58,210
passive sub domain.

243
00:16:58,210 --> 00:17:00,970
That was spark.com.

244
00:17:01,490 --> 00:17:11,530
You can actually ask, uh, the llama agent or the llama model to run subgroup sh in the background.

245
00:17:11,970 --> 00:17:14,370
Okay, wait for its completion.

246
00:17:14,570 --> 00:17:22,730
We can obviously speed that up by giving more threads and then print those output on the chat screen.

247
00:17:22,770 --> 00:17:23,210
Okay.

248
00:17:23,370 --> 00:17:25,050
It is very simple to do that.

249
00:17:25,250 --> 00:17:26,770
How how will we do that?

250
00:17:26,970 --> 00:17:33,050
We have to create a route in the App.py flask application to run sub route.

251
00:17:33,290 --> 00:17:38,970
And we have to create a similar route in the OpenAPI dot JSON file.

252
00:17:38,970 --> 00:17:39,970
That's it then.

253
00:17:40,450 --> 00:17:45,570
Now you would be also able to do active reconnaissance with the help of simply chat or commands that

254
00:17:45,570 --> 00:17:46,770
you give to your model.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: JavaScript Analysis

1
00:00:00,200 --> 00:00:09,160
How we can utilize the Open Web UI to configure various different types of MCP server.

2
00:00:09,400 --> 00:00:15,120
We saw that how we were able to successfully configure the MCP server called as Sub Finder.

3
00:00:16,240 --> 00:00:18,440
Then we enabled it from the settings.

4
00:00:18,800 --> 00:00:22,280
We configured it from the settings, we enabled it over here.

5
00:00:22,480 --> 00:00:25,760
And then we were able to use it successfully as you can see.

6
00:00:26,040 --> 00:00:29,920
Now what is going to be your to do task or a homework.

7
00:00:30,200 --> 00:00:33,640
You have to set up the same thing in your system.

8
00:00:33,640 --> 00:00:39,200
I'm going to provide all the necessary files that I have in my computer that I'm currently using.

9
00:00:39,400 --> 00:00:46,760
So the app dot Pi and the static folder that contains the API JSON file, I'm going to provide that

10
00:00:46,760 --> 00:00:49,240
on my GitHub so you can find it over there.

11
00:00:49,240 --> 00:00:51,000
No need to worry about that.

12
00:00:51,000 --> 00:01:00,080
And you can utilize the same code to increase or enhance the capabilities to not only do subdomain Domain

13
00:01:00,080 --> 00:01:04,360
enumeration, HTTP detection, but active reconnaissance using Subroute.

14
00:01:04,520 --> 00:01:11,520
I will also provide those scripts on my GitHub, so you can find it over there and add it to your MCP,

15
00:01:12,440 --> 00:01:21,560
uh, program that helps you basically run commands directly from your lama tree and gets interpreted

16
00:01:21,560 --> 00:01:24,280
or get executed in the back end for you.

17
00:01:24,640 --> 00:01:28,000
Okay, so that is going to be a to do task for participants.

18
00:01:28,440 --> 00:01:29,320
Uh, please do that.

19
00:01:29,320 --> 00:01:35,120
I would be very happy in the next session if you if you guys are able to do it, or at least by the

20
00:01:35,120 --> 00:01:41,440
end of this boot camp, I would I would be very happy to see participants at configuring at least one

21
00:01:41,480 --> 00:01:48,640
extra functionality that they can do in their own MCP server and utilizing it.

22
00:01:48,640 --> 00:01:49,040
Okay.

23
00:01:51,360 --> 00:01:51,800
Yeah.

24
00:01:52,280 --> 00:01:59,600
Now, uh, one quick thing that I want to let participants know is that when you are going to run.

25
00:02:01,160 --> 00:02:05,240
uh, open web UI from a container like me that I'm currently running.

26
00:02:05,600 --> 00:02:09,120
I'm running it from the container that is the Docker service.

27
00:02:09,520 --> 00:02:12,680
Uh, which is the easiest way to do it that we discussed yesterday.

28
00:02:13,160 --> 00:02:14,680
Please make sure please.

29
00:02:14,680 --> 00:02:21,120
Because, uh, this was this is a common error or a common issue that all of you will face whenever

30
00:02:21,120 --> 00:02:23,640
you are going to set up the tool server.

31
00:02:23,920 --> 00:02:32,800
Please don't give here local host or loopback address because, uh, the open web UI is currently running

32
00:02:32,800 --> 00:02:39,400
in a Docker container and our files are outside in my Mac OS, or it will be you for you, it will be

33
00:02:39,400 --> 00:02:46,360
in your windows system, so the container cannot reach to your Mac OS file system.

34
00:02:46,360 --> 00:02:54,000
If you say localhost over here, it will try to find this open API file in the Docker container itself

35
00:02:54,200 --> 00:02:55,960
where it would not be present.

36
00:02:55,960 --> 00:02:56,800
So what will happen?

37
00:02:56,800 --> 00:02:59,440
You will keep on getting error error like this.

38
00:03:02,560 --> 00:03:06,320
Okay, if you add localhost, you will keep on getting error like this.

39
00:03:06,320 --> 00:03:11,880
Or if you add loopback address you will keep on getting error like this.

40
00:03:11,880 --> 00:03:14,720
So I just want to be sure that you don't get errors.

41
00:03:14,720 --> 00:03:18,600
So please specify the complete IP address of your local machine.

42
00:03:18,800 --> 00:03:23,160
How to find the IP address for Linux systems please grab the.

43
00:03:23,200 --> 00:03:32,360
Please use the command ifconfig and grep your IP and for windows system ipconfig is the command.

44
00:03:32,480 --> 00:03:39,600
Please run this command, get your IP address and then specify that and then verify the connection.

45
00:03:39,640 --> 00:03:41,200
Okay let me see.

46
00:03:45,120 --> 00:03:48,160
Oh I closed I closed that server.

47
00:03:48,960 --> 00:03:56,960
Oh wait yes it is not running Python three app dot pi.

48
00:03:57,000 --> 00:03:58,200
Yeah now it is running.

49
00:04:03,400 --> 00:04:03,920
Go here.

50
00:04:03,960 --> 00:04:06,800
Go here and click connection successful okay.

51
00:04:07,080 --> 00:04:11,600
So make sure that you give this only if you give localhost it will.

52
00:04:13,440 --> 00:04:14,560
Uh okay.

53
00:04:14,560 --> 00:04:17,320
It was able to communicate here in this case luckily.

54
00:04:17,320 --> 00:04:19,400
But eventually you will not see that.

55
00:04:19,400 --> 00:04:22,760
So make sure that you always give the full IP address.

56
00:04:23,000 --> 00:04:24,600
Only then it would work.

57
00:04:24,640 --> 00:04:25,080
Okay.

58
00:04:25,120 --> 00:04:29,120
So make sure that you give the full complete IP address so that it works smoothly.

59
00:04:29,840 --> 00:04:33,920
Okay, so this was one important note that I wanted participants to keep in mind.

60
00:04:34,200 --> 00:04:35,720
Uh, let us proceed now.

61
00:04:38,680 --> 00:04:47,400
Uh, participants now, uh, we are going to understand about JavaScript analysis, uh, very, very

62
00:04:47,400 --> 00:04:51,240
important technique that is going to be very, very helpful for you.

63
00:04:51,440 --> 00:04:58,280
Because if you go ahead and see hacker one reports for sensitive information disclosure via JavaScript

64
00:04:58,360 --> 00:05:05,200
files, you would be able to see how security researchers or bug bounty hunters were able to identify

65
00:05:05,200 --> 00:05:08,720
a lot of sensitive information through JavaScript files.

66
00:05:08,960 --> 00:05:11,520
Okay, so that is where that is.

67
00:05:11,960 --> 00:05:19,320
Uh, 100% agreed that JavaScript files are goldmine, but because it can have a lot of information for

68
00:05:19,320 --> 00:05:25,440
us that can we can directly use against the program in Pentesting or Bug bounty.

69
00:05:25,600 --> 00:05:31,520
In addition to that, JavaScript files serves a very important purpose for us to do content and asset

70
00:05:31,520 --> 00:05:32,320
discovery.

71
00:05:32,320 --> 00:05:39,680
So we'll see today how we can do this and how we can also utilize the AI capabilities to enhance our

72
00:05:39,680 --> 00:05:40,360
workflow.

73
00:05:40,400 --> 00:05:40,800
Okay.

74
00:05:40,960 --> 00:05:45,080
So to do this participant, the first and the foremost thing that we are going to do is.

75
00:05:47,360 --> 00:05:55,440
We are going to yeah, we are going to first identify all of the URLs for a target.

76
00:05:55,480 --> 00:05:56,000
Okay.

77
00:05:56,040 --> 00:06:03,400
So to identify All the URLs, we are going to use a tool which is way back URLs, or the tool which

78
00:06:03,400 --> 00:06:04,040
is go.

79
00:06:13,760 --> 00:06:15,800
Way back URLs or go.

80
00:06:15,840 --> 00:06:18,000
So what are these both tools going to do?

81
00:06:18,000 --> 00:06:19,240
Both are open source tools.

82
00:06:19,240 --> 00:06:23,400
They are going to identify all the URLs for us for a given target.

83
00:06:23,640 --> 00:06:25,760
So I'm going to use Wayback URLs here.

84
00:06:26,240 --> 00:06:29,320
And I'm going to specify a target which is active dot in.

85
00:06:29,520 --> 00:06:33,200
And then I'm going to say grep dot j.

86
00:06:38,400 --> 00:06:39,760
Dot j s.

87
00:06:40,520 --> 00:06:43,520
Uh I don't want Jason I don't I only want js.

88
00:06:43,520 --> 00:06:45,360
So I'm going to say backslash dot js.

89
00:06:45,400 --> 00:06:51,640
That means I only want files that are ending with JS and save this results into a file called js dot

90
00:06:51,640 --> 00:06:52,280
txt.

91
00:06:52,720 --> 00:06:53,640
Let's hit enter.

92
00:06:53,840 --> 00:06:57,720
What is going to happen way back URLs is going to run.

93
00:06:57,960 --> 00:06:59,240
Oh, it was very fast.

94
00:06:59,560 --> 00:06:59,960
Way back.

95
00:07:00,000 --> 00:07:02,400
Earls is going to run on this target.

96
00:07:02,560 --> 00:07:04,880
It is going to grip all the Earls.

97
00:07:05,240 --> 00:07:14,720
I means I means case insensitive that if somewhere JS is in capital, those earls also should be found

98
00:07:14,880 --> 00:07:17,320
an extended grip if I want to find anything else.

99
00:07:17,320 --> 00:07:18,400
So I is extra here.

100
00:07:18,400 --> 00:07:20,840
If you don't use it then also it is fine.

101
00:07:22,160 --> 00:07:23,440
Uh, yes.

102
00:07:23,440 --> 00:07:25,040
So that is optional here.

103
00:07:25,040 --> 00:07:28,680
We don't want JSON, we only want j s.

104
00:07:28,720 --> 00:07:29,160
Okay.

105
00:07:29,200 --> 00:07:31,560
J is also found here.

106
00:07:31,560 --> 00:07:37,960
Maybe we can avoid that by escaping it from here now.

107
00:07:38,160 --> 00:07:40,680
So we can say.

108
00:07:42,880 --> 00:07:49,120
Uh, pipe grip and we can say V inverse grip.

109
00:07:49,760 --> 00:07:50,880
We don't want JSON.

110
00:07:52,040 --> 00:07:53,480
Sorry, we don't want JSON.

111
00:07:53,480 --> 00:07:53,960
Okay.

112
00:07:54,000 --> 00:08:00,520
And when you do inverse grip JSON will not be printed, and only you will only get the required files

113
00:08:00,520 --> 00:08:02,760
in the js dot txt.

114
00:08:03,560 --> 00:08:04,360
Let's run this.

115
00:08:04,360 --> 00:08:06,960
And now you can see all the JSON files are gone.

116
00:08:07,760 --> 00:08:13,080
There are no JSON, there are only js files as you can see over here.

117
00:08:14,280 --> 00:08:16,400
Okay so we did a inverse grep.

118
00:08:16,400 --> 00:08:18,640
So first we did a grep for js.

119
00:08:18,680 --> 00:08:20,640
Then we did a inverse grep for JSON.

120
00:08:20,640 --> 00:08:22,280
And we removed all those files.

121
00:08:22,280 --> 00:08:25,600
And now we have a final file called js dot txt.

122
00:08:26,080 --> 00:08:26,680
Awesome.

123
00:08:26,720 --> 00:08:31,640
Now let us try to see how many URLs are there for JS files.

124
00:08:31,920 --> 00:08:33,360
600 URLs.

125
00:08:33,760 --> 00:08:34,920
Would you like to see it?

126
00:08:35,880 --> 00:08:36,480
Yes.

127
00:08:37,120 --> 00:08:40,400
So this is the given file that we have currently participants.

128
00:08:40,560 --> 00:08:41,640
Let me zoom this.

129
00:08:43,680 --> 00:08:46,480
The file currently contains a bunch of URLs.

130
00:08:46,480 --> 00:08:50,840
You can see invisible dot js, but we can see the files are also repeating.

131
00:08:52,600 --> 00:08:54,480
Yes they are also repeating here.

132
00:08:54,960 --> 00:08:58,960
See invisible dot js One, 2345 times.

133
00:08:58,960 --> 00:09:02,680
So let's do a sort unique on this file.

134
00:09:02,680 --> 00:09:04,720
So basically remove duplicates.

135
00:09:05,120 --> 00:09:12,200
So we'll say sort unique and do word count okay.

136
00:09:13,080 --> 00:09:15,600
Uh unique.

137
00:09:19,120 --> 00:09:19,560
Okay.

138
00:09:19,800 --> 00:09:22,200
It it it ran unique.

139
00:09:22,200 --> 00:09:28,560
But you can see all of these file names are unique because you can see T s contains a different number.

140
00:09:28,600 --> 00:09:31,160
Different number 440720.

141
00:09:31,160 --> 00:09:37,240
So it is basically considering all of these files as uh, all of these files as unique.

142
00:09:37,960 --> 00:09:44,320
So maybe what we can do is we can just remove all of these parameters after JS, after JS, whatever

143
00:09:44,320 --> 00:09:47,040
is written, we can remove that and again run.

144
00:09:49,200 --> 00:09:52,040
Uh, again run the command to do that.

145
00:09:52,040 --> 00:09:56,400
So to do that we can say if I s dot txt.

146
00:09:57,400 --> 00:10:05,600
Uh, search for search for dot js and replace everything.

147
00:10:10,360 --> 00:10:11,720
After it.

148
00:10:11,720 --> 00:10:12,120
So.

149
00:10:14,960 --> 00:10:16,160
Let it get removed.

150
00:10:18,000 --> 00:10:25,320
Uh, search JS and remove everything after it okay.

151
00:10:52,880 --> 00:10:55,960
Dot js Start.

152
00:11:00,760 --> 00:11:01,680
And recreate with.

153
00:11:01,680 --> 00:11:02,080
Yes.

154
00:11:04,440 --> 00:11:05,040
Perfect.

155
00:11:05,360 --> 00:11:05,800
Now.

156
00:11:06,440 --> 00:11:06,840
Okay.

157
00:11:07,920 --> 00:11:09,040
Dot version.

158
00:11:10,560 --> 00:11:14,560
I think it did not get removed very well.

159
00:11:15,160 --> 00:11:16,280
Dot js.

160
00:11:39,640 --> 00:11:40,040
Okay.

161
00:11:40,080 --> 00:11:41,200
Let me run this.

162
00:11:53,440 --> 00:11:57,760
Okay, so maybe we can run the command like this.

163
00:11:58,280 --> 00:12:01,480
Uh, that can help us remove all the JS patterns.

164
00:12:02,200 --> 00:12:04,800
Yes, yes, yes.

165
00:12:04,800 --> 00:12:05,280
This worked.

166
00:12:05,320 --> 00:12:08,320
Thank you, uh, for sharing this.

167
00:12:08,320 --> 00:12:13,840
So we can see now all of these extra patterns, extra values, parameters has been removed.

168
00:12:13,840 --> 00:12:15,480
Now let's do a sort unique.

169
00:12:15,720 --> 00:12:21,160
So sort hyphen u and unique and let's do a word count.

170
00:12:21,840 --> 00:12:24,200
And now you can see we have 275.

171
00:12:24,760 --> 00:12:27,920
Uh, if you remember initially we had 600.

172
00:12:28,080 --> 00:12:32,720
So out of 600 we have reduced down to 275 unique.

173
00:12:33,120 --> 00:12:38,040
So let's save this into a file called as JS unique dot txt.

174
00:12:38,960 --> 00:12:39,800
Excellent.

175
00:12:40,000 --> 00:12:43,880
Now we have JS unique dot txt file.

176
00:12:44,520 --> 00:12:47,800
We can open it as well here.

177
00:12:47,800 --> 00:12:53,960
So this is the given file which contains the JS files which are unique in nature.

178
00:12:54,240 --> 00:12:55,080
Excellent.

179
00:12:55,080 --> 00:12:59,000
And now we will try to download the contents of this JS file.

180
00:12:59,040 --> 00:12:59,400
Okay.

181
00:13:01,680 --> 00:13:05,280
So I'm before that I'm pasting the command.

182
00:13:07,920 --> 00:13:10,200
On the chat if anyone wants to use it.

183
00:13:11,840 --> 00:13:12,320
Okay.

184
00:13:12,360 --> 00:13:14,600
Now we are going to download all the files.

185
00:13:14,600 --> 00:13:19,840
So to download all the files we are going to say uh let's make a folder.

186
00:13:20,120 --> 00:13:33,440
Let's call it as JS, download and copy active fi js files to J download.

187
00:13:33,560 --> 00:13:35,240
Now let's go to JS download.

188
00:13:35,360 --> 00:13:41,560
And here participants uh we are going to download all the JS files which are in the URLs, so that we

189
00:13:41,560 --> 00:13:45,360
can give those files for analysis to our LLM.

190
00:13:45,800 --> 00:13:55,280
So I'm going to say cat this file and then run a loop while read host do do Who do w get?

191
00:13:56,040 --> 00:13:56,160
Uh.

192
00:13:56,160 --> 00:14:03,280
That is, run a loop and download all the files and say done.

193
00:14:05,000 --> 00:14:09,240
Okay, now you can see all of these JS files have been started to download.

194
00:14:09,640 --> 00:14:11,120
So frugal loop.

195
00:14:11,160 --> 00:14:13,800
Two dot min dot js has been downloaded.

196
00:14:13,840 --> 00:14:15,880
Now it will again try to connect to main dot.

197
00:14:15,920 --> 00:14:17,240
It is now attempting to download.

198
00:14:17,240 --> 00:14:19,040
This file means dot js.

199
00:14:19,200 --> 00:14:24,800
It attempted first to download frugal loop to min dot js and it downloaded that.

200
00:14:27,840 --> 00:14:29,960
Uh, if you are unable to copy that command, no problem.

201
00:14:29,960 --> 00:14:35,160
I'll paste it again in the group WhatsApp group so you can copy it from there, as well as I'll paste

202
00:14:35,160 --> 00:14:36,920
it on the GitHub.

203
00:14:39,480 --> 00:14:39,880
Okay.

204
00:14:39,920 --> 00:14:40,240
Yeah.

205
00:14:40,240 --> 00:14:45,920
So you can see the file downloading download process has begun successfully and all of the JavaScript

206
00:14:45,920 --> 00:14:49,320
files have been downloading currently for this given target.

207
00:14:49,360 --> 00:14:49,880
Awesome.

208
00:14:50,160 --> 00:14:57,080
Let it download for a certain period of time and then we will see how many files, uh, we have successfully

209
00:14:57,080 --> 00:14:57,680
found.

210
00:15:04,680 --> 00:15:10,960
And currently we have only one file two dot min dot js.

211
00:15:11,400 --> 00:15:14,640
And there are more files which are attempting to be downloaded.

212
00:15:15,480 --> 00:15:16,560
We can keep this running.

213
00:15:16,560 --> 00:15:18,280
Yeah, it has downloaded more files.

214
00:15:18,480 --> 00:15:24,720
You can see jquery, dot js, isotope, dot js, bootstrap, dot js and more files like this.

215
00:15:31,000 --> 00:15:31,840
Can you see this?

216
00:15:31,840 --> 00:15:33,840
These files have been successfully downloaded.

217
00:15:33,840 --> 00:15:36,000
More files have been downloaded.

218
00:15:36,000 --> 00:15:39,640
So files will keep on populating, uh, over here.

219
00:15:39,880 --> 00:15:46,000
And then, uh, we are going to use these files for analysis in just a moment okay.

220
00:15:46,520 --> 00:15:49,720
So let's wait for this to completely download.

221
00:15:49,720 --> 00:15:52,400
Let's give it maybe few more seconds.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,400 --> 00:00:01,680
This is happening.

2
00:00:01,720 --> 00:00:04,400
Until then, what we are going to do with all of these files?

3
00:00:04,400 --> 00:00:07,640
We are going to give these files to our agent for analysis.

4
00:00:07,680 --> 00:00:08,080
Okay.

5
00:00:08,400 --> 00:00:12,400
So you're going to copy all of these files that you have just got.

6
00:00:12,920 --> 00:00:17,040
And remember participants we have used GPT for all yesterday.

7
00:00:17,440 --> 00:00:25,160
So there was a there is a configuration that you need to make for it to automatically index index JavaScript

8
00:00:25,160 --> 00:00:25,680
files.

9
00:00:26,080 --> 00:00:27,040
Go to settings.

10
00:00:28,000 --> 00:00:30,560
So I hope you have installed GPT for all.

11
00:00:30,560 --> 00:00:33,160
If you have not installed, you can please install it.

12
00:00:33,160 --> 00:00:36,040
The website is GPT for all.

13
00:00:36,040 --> 00:00:40,000
It's an completely open source tool that you can use.

14
00:00:40,000 --> 00:00:43,480
You can download it for windows, ubuntu, Linux and Mac OS.

15
00:00:43,520 --> 00:00:45,240
I have downloaded for Mac OS.

16
00:00:45,760 --> 00:00:49,600
It uses in the back end the same llama 3.1.

17
00:00:49,640 --> 00:00:58,360
Okay, now once you start GPT for all, go to settings, go to local docs and you can see allowed file

18
00:00:58,360 --> 00:01:02,200
extensions in the Allowed File Extensions feature.

19
00:01:02,480 --> 00:01:04,760
Please add JS.

20
00:01:05,120 --> 00:01:06,520
It would not be there.

21
00:01:06,880 --> 00:01:11,440
So your JavaScript file would not be analyzed by llama model.

22
00:01:11,600 --> 00:01:15,280
You need to add JS over here once to once you add JS over here.

23
00:01:15,600 --> 00:01:17,120
Please go to local docs.

24
00:01:18,040 --> 00:01:20,760
Please add a collection of whatever your folder is.

25
00:01:20,760 --> 00:01:23,440
So I'm going to add a collection which is JS.

26
00:01:23,760 --> 00:01:27,840
And I'm going to give a path as well where all of our files are getting saved.

27
00:01:28,160 --> 00:01:34,600
So all of our files are getting saved in JS download folder inside a folder.

28
00:01:34,600 --> 00:01:39,960
So let's go to ro hit I js download.

29
00:01:39,960 --> 00:01:41,960
These are all the files that we downloaded.

30
00:01:41,960 --> 00:01:42,920
Click on open.

31
00:01:43,200 --> 00:01:44,240
Click on create.

32
00:01:44,760 --> 00:01:50,040
Now you can see there are 15 files 49482.

33
00:01:50,120 --> 00:01:57,240
Total number of words inside this file and the embeddings are are being are getting progressed right

34
00:01:57,240 --> 00:01:57,600
now.

35
00:01:57,960 --> 00:01:58,440
Okay.

36
00:01:58,480 --> 00:02:00,880
So you you can wait for this to get completed.

37
00:02:00,880 --> 00:02:03,480
It might take maybe few minutes.

38
00:02:03,480 --> 00:02:05,160
It's awesome.

39
00:02:05,160 --> 00:02:10,960
You can see tweenmax dot js file has been started to be understood by the LM.

40
00:02:11,000 --> 00:02:21,000
The LM is basically trying to convert it into a vector database, which is which it is going to store

41
00:02:21,280 --> 00:02:24,000
in the as embeddings in the database.

42
00:02:24,000 --> 00:02:28,840
And then we are going to ask questions based on these JavaScript files.

43
00:02:29,040 --> 00:02:34,560
What kind of questions we are going to see them now once this embedding is completed.

44
00:02:34,600 --> 00:02:34,800
Okay.

45
00:02:34,840 --> 00:02:37,200
Let's wait for the embeddings to happen.

46
00:02:37,200 --> 00:02:39,240
Let's give it maybe two minutes more.

47
00:02:40,720 --> 00:02:44,120
Until then, let us see if you are able to get more files.

48
00:02:44,120 --> 00:02:46,800
Yeah, it is still running to get more files.

49
00:02:46,800 --> 00:02:51,000
Let me stop this for now for demonstration purposes.

50
00:02:51,400 --> 00:02:55,120
Uh, I think 1815 files are sufficient for us.

51
00:02:55,400 --> 00:03:01,240
Uh, but when you would be doing this onto an actual target, maybe like, uh, target, like Tesla

52
00:03:01,240 --> 00:03:08,520
or maybe a bank target like Bank of America, etc., then you would be able to get much more larger

53
00:03:08,520 --> 00:03:10,200
number of files, not 15.

54
00:03:10,200 --> 00:03:16,960
Maybe you get 50 files or 60 files, so you can keep that running entirely, so that you have a good

55
00:03:17,200 --> 00:03:23,000
number of size of files and for you to analyze over there that you can then feed to the LM.

56
00:03:23,440 --> 00:03:33,760
So now it is trying to read the next file, jQuery 1.11.0. js and it is almost 40% completed.

57
00:03:34,360 --> 00:03:36,480
Uh, let's wait for this embedding to get completed.

58
00:03:36,480 --> 00:03:44,880
And then we are going to very smartly ask questions, uh, to the llama model for these files.

59
00:03:44,880 --> 00:03:45,320
Okay.

60
00:03:45,360 --> 00:03:49,240
Until this is happening, participants, let's keep this happening.

61
00:03:49,400 --> 00:03:55,360
I have a very, very interesting technique that I also want to show participants that is related to

62
00:03:55,400 --> 00:03:56,800
JavaScript file analysis.

63
00:03:56,840 --> 00:03:57,240
Okay.

64
00:03:57,920 --> 00:04:07,280
Trust me, that has this has worked for me in the past, uh, with so many targets, including bank

65
00:04:07,320 --> 00:04:08,160
targets as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 10: Web Exploitation

1
00:00:00,280 --> 00:00:03,040
So what I'm going to do is I'm going to quickly.

2
00:00:06,320 --> 00:00:11,000
Do Wayback URLs on a bank, let's say SBI.

3
00:00:11,320 --> 00:00:11,800
Okay.

4
00:00:12,000 --> 00:00:13,720
I'm just going to crawl the URLs.

5
00:00:13,720 --> 00:00:16,160
I'm not going to perform any attack on that target.

6
00:00:16,160 --> 00:00:23,960
I just want to show you how JavaScript files that contains variable names, functions, etc. are specific

7
00:00:23,960 --> 00:00:26,880
to targets or sector specific targets.

8
00:00:26,880 --> 00:00:32,360
For example, if we take a bank target, then the developer mindset would be that the variables and

9
00:00:32,360 --> 00:00:37,200
function names are of the bank bank related activity.

10
00:00:37,200 --> 00:00:43,760
So maybe like uh, it could be the name could be banking credit loan.

11
00:00:43,760 --> 00:00:45,160
These would be the functions.

12
00:00:45,160 --> 00:00:51,720
And the same could be also helping us to identify directories and endpoints and subdomains.

13
00:00:52,080 --> 00:00:52,520
Okay.

14
00:00:52,800 --> 00:00:54,840
And the same thing would not be for Tesla.

15
00:00:54,880 --> 00:00:59,530
Tesla would have maybe gears, tires uh motors, Words.

16
00:00:59,570 --> 00:01:02,490
Batteries, these types of variable names and functions.

17
00:01:02,530 --> 00:01:07,530
Okay, so first let's try to download all the URLs for a bank target.

18
00:01:07,530 --> 00:01:08,530
This is a bank.

19
00:01:09,130 --> 00:01:11,770
And let's just try to get the URLs.

20
00:01:11,770 --> 00:01:12,370
That's it.

21
00:01:12,810 --> 00:01:13,690
Nothing else.

22
00:01:13,690 --> 00:01:14,970
So I'm going to say grep.

23
00:01:25,730 --> 00:01:29,090
Uh get js I don't want JSON files.

24
00:01:30,090 --> 00:01:32,850
And then save this results to a file.

25
00:01:34,730 --> 00:01:35,170
Yeah.

26
00:01:40,290 --> 00:01:44,690
Called as sbi mf js dot txt.

27
00:01:45,370 --> 00:01:46,330
Let's run this.

28
00:01:54,130 --> 00:01:56,570
So we are trying to get all of the URLs.

29
00:01:56,730 --> 00:02:01,620
And then we are going to filter those URLs for JavaScript files, we are going to remove JSON files

30
00:02:01,620 --> 00:02:04,380
from it, and then we are going to save these results into a.

31
00:02:04,540 --> 00:02:08,860
TXT file called as sbi dot js dot txt.

32
00:02:09,180 --> 00:02:09,500
Awesome!

33
00:02:09,500 --> 00:02:14,300
It was very fast and now let's remove the duplicates as we did here.

34
00:02:14,540 --> 00:02:17,260
So to do that I'm going to run this command.

35
00:02:17,300 --> 00:02:19,820
So cat sbi JS.

36
00:02:22,020 --> 00:02:23,460
Remove this extra pipe.

37
00:02:27,860 --> 00:02:35,860
And let's say sbi mf JS unique hit enter.

38
00:02:36,020 --> 00:02:36,540
Awesome.

39
00:02:36,820 --> 00:02:39,820
Now let's see how many unique results are there for us.

40
00:02:41,820 --> 00:02:42,260
So.

41
00:02:42,460 --> 00:02:43,460
Oh nice.

42
00:02:43,580 --> 00:02:50,300
Did you see that considerable amount of difference for if we had only 15 JavaScript unique files?

43
00:02:51,180 --> 00:02:52,980
I think we've downloaded 15.

44
00:02:53,180 --> 00:02:56,100
So here we have 1610 files.

45
00:02:56,220 --> 00:02:57,260
Really really awesome.

46
00:02:57,480 --> 00:02:59,880
Now let's quickly download them as well.

47
00:02:59,880 --> 00:03:03,960
So we are going to say read this file on a loop.

48
00:03:05,360 --> 00:03:11,200
Store the file names or the URL names in host variable and do send a w.

49
00:03:11,200 --> 00:03:14,040
Get command on the host and close the loop.

50
00:03:14,800 --> 00:03:17,360
Now it is going to download the JavaScript files.

51
00:03:17,360 --> 00:03:22,800
For example moment dot min dot js is currently being downloaded in this folder.

52
00:03:23,080 --> 00:03:26,160
Similarly, more files would also be downloaded in this folder.

53
00:03:27,800 --> 00:03:28,240
Okay.

54
00:03:30,960 --> 00:03:34,280
Uh, let's wait for this to happen automatically in the background.

55
00:03:34,320 --> 00:03:36,280
Till then, let's go to.

56
00:03:36,400 --> 00:03:39,480
I think we should download all of these files in a folder.

57
00:03:39,920 --> 00:03:45,040
Let's say let's make this folder and let's run this command in that folder.

58
00:03:53,600 --> 00:03:54,040
Yeah.

59
00:03:54,680 --> 00:03:57,850
So that we have all files coming into the same folder.

60
00:03:58,130 --> 00:04:00,810
Okay, let's go to GPT for all and see what is happening.

61
00:04:01,250 --> 00:04:02,450
Ah, did you see that?

62
00:04:02,650 --> 00:04:04,930
That is why I created a different folder.

63
00:04:05,250 --> 00:04:10,290
Uh, because now it is going to embed all of those new files as well here.

64
00:04:12,490 --> 00:04:13,250
No problem.

65
00:04:13,370 --> 00:04:18,010
Uh, let's wait for this to get completed quickly, and then we can go to the chat feature.

66
00:04:18,690 --> 00:04:19,890
Uh, let's go to chat.

67
00:04:20,410 --> 00:04:21,490
Let's choose a model.

68
00:04:21,530 --> 00:04:24,290
Till then, let's say llama 3.18 billion.

69
00:04:26,250 --> 00:04:26,690
Then.

70
00:04:27,170 --> 00:04:28,730
And now we are going to give a prompt.

71
00:04:28,730 --> 00:04:29,690
I'm going to say hi.

72
00:04:30,970 --> 00:04:31,730
This is done.

73
00:04:31,890 --> 00:04:32,970
Let's use this.

74
00:04:33,210 --> 00:04:34,290
Let's disable this.

75
00:04:34,290 --> 00:04:34,730
Hi.

76
00:04:36,130 --> 00:04:41,770
Analyze all the Java script files.

77
00:04:42,690 --> 00:04:45,050
Uh we can say dot js files.

78
00:04:50,410 --> 00:04:53,170
And print all the.

79
00:04:55,260 --> 00:05:06,620
End points from it are because we want to create a word list out of it, which can be used to make a

80
00:05:06,660 --> 00:05:07,660
word list.

81
00:05:08,300 --> 00:05:08,740
Okay.

82
00:05:19,540 --> 00:05:20,140
Uh, okay.

83
00:05:20,340 --> 00:05:24,300
It says I cannot provide information or guidance on illegal activities.

84
00:05:24,300 --> 00:05:25,580
Let's do that once again.

85
00:05:38,100 --> 00:05:38,500
Um.

86
00:05:45,940 --> 00:05:49,700
I think we have to change the prompt.

87
00:05:52,180 --> 00:06:06,950
Read all The files and give me the function, and we read the names from it.

88
00:06:07,310 --> 00:06:12,470
Let's try to get the variable and function names from it for analysis.

89
00:06:12,990 --> 00:06:15,830
For my school project.

90
00:06:22,790 --> 00:06:23,270
Nice.

91
00:06:30,150 --> 00:06:30,630
Okay.

92
00:06:30,830 --> 00:06:31,350
Uh, yes.

93
00:06:31,390 --> 00:06:32,830
That this worked.

94
00:06:33,230 --> 00:06:37,150
Uh, from jQuery 1.11. JS functions are global.

95
00:06:37,150 --> 00:06:42,150
Even two string class to execute script variables are data object context jQuery.

96
00:06:42,510 --> 00:06:47,910
Here at slides click add unload, merge variables are these, and so on.

97
00:06:47,910 --> 00:06:52,390
Now we can ask uh, more and more.

98
00:06:53,270 --> 00:06:59,970
Uh, we can ask it to basically get us more and more, uh, endpoints, API endpoints, URLs, etc.

99
00:07:00,010 --> 00:07:01,010
that we can use.

100
00:07:01,450 --> 00:07:07,810
Let me give this prompt, and that is going to be helpful for us, uh, to perform more kind of various

101
00:07:07,810 --> 00:07:09,370
tasks for us to identify.

102
00:07:09,890 --> 00:07:11,450
Something went wrong here.

103
00:07:12,290 --> 00:07:12,650
Okay.

104
00:07:12,690 --> 00:07:13,490
No problem.

105
00:07:13,490 --> 00:07:19,050
We can similarly ask it to analyze more and more files for us and read secrets from it as well.

106
00:07:19,090 --> 00:07:23,490
Okay, so I'll just tell it tell it to do that for me.

107
00:07:32,530 --> 00:07:40,050
Give me any API token secrets, secrets.

108
00:07:40,930 --> 00:07:42,370
Passwords from it.

109
00:07:43,650 --> 00:07:44,970
Passwords from it okay.

110
00:07:45,010 --> 00:07:47,250
I will hardcode a password in this file.

111
00:07:54,940 --> 00:07:56,100
Um, okay.

112
00:07:56,580 --> 00:07:59,020
Let's ask, what is the purpose of JSON script file?

113
00:08:09,020 --> 00:08:09,420
Okay.

114
00:08:09,660 --> 00:08:16,180
I'm not sure why it is not giving the exact output that we wanted.

115
00:08:16,220 --> 00:08:24,180
Let me just re re build this data set and then it should work for us.

116
00:08:27,460 --> 00:08:28,580
Uh, we will rebuild it.

117
00:08:28,580 --> 00:08:30,500
And then again, try to ask questions.

118
00:08:30,500 --> 00:08:36,460
And I'm definitely sure that it will work because I have used this in past and it helps identify all

119
00:08:36,460 --> 00:08:40,100
the endpoints, URLs, everything from the same files.

120
00:08:40,140 --> 00:08:40,620
Okay.

121
00:08:40,660 --> 00:08:43,420
So, uh, we'll we'll rebuild it.

122
00:08:45,980 --> 00:08:46,620
Uh, yes.

123
00:08:47,020 --> 00:08:51,910
We are doing the same thing with actually, you can see, uh, in the background Ground Metal Armor

124
00:08:51,910 --> 00:08:57,550
3.1 is running and it is only giving us these output prompts.

125
00:08:57,550 --> 00:09:00,990
I'm not sure why it is not giving us the exact same output prompt.

126
00:09:01,390 --> 00:09:04,470
Uh, we will try this once again with open web UI as well.

127
00:09:04,510 --> 00:09:12,070
Okay, uh, but before that, one more thing that I wanted to show participants is there is one more

128
00:09:12,070 --> 00:09:21,350
technique to basically get words identified from files for creating a word list for fuzzing as well

129
00:09:21,350 --> 00:09:22,830
as subdomain enumeration.

130
00:09:22,990 --> 00:09:28,910
And I'm going to run that python3 uh get js.

131
00:09:35,630 --> 00:09:36,110
Yeah.

132
00:09:36,110 --> 00:09:42,830
So I uh, so there's a file called as get js words.py I'm going to run that Python get.

133
00:09:44,510 --> 00:09:44,870
Yeah.

134
00:09:45,230 --> 00:09:51,640
And it is going to help us basically to get all the words from a given file So we can give any file

135
00:09:51,640 --> 00:09:52,360
name to it.

136
00:09:52,360 --> 00:09:54,360
And it is going to basically, uh.

137
00:09:56,440 --> 00:10:02,240
Identify all the words from that given file that is JavaScript file and help us create a word list.

138
00:10:02,280 --> 00:10:02,640
Okay.

139
00:10:02,960 --> 00:10:05,120
So let me just do that.

140
00:10:07,280 --> 00:10:08,960
First let me show you what is inside it.

141
00:10:13,960 --> 00:10:14,560
Yeah.

142
00:10:14,560 --> 00:10:16,280
So it is going to basically.

143
00:10:18,320 --> 00:10:21,160
It is going to uh read that file.

144
00:10:21,400 --> 00:10:27,520
It is going to JS, beautify the JavaScript file, and it is going to remove the blacklisted words like

145
00:10:27,560 --> 00:10:30,440
away break case, catch class constant.

146
00:10:30,440 --> 00:10:34,480
Because these are these are the common words that are used for JavaScript files.

147
00:10:34,480 --> 00:10:35,720
We don't want these words.

148
00:10:35,720 --> 00:10:36,120
Why?

149
00:10:36,440 --> 00:10:40,760
Because these are not going to be uh, the subdomain or end points for fuzzing.

150
00:10:40,760 --> 00:10:47,960
So we have blacklisted the most common words that are required in context to JavaScript files.

151
00:10:47,960 --> 00:10:53,620
So those words are blocked Blog and other words apart from this would be found that are custom made

152
00:10:53,620 --> 00:10:54,580
by the developer.

153
00:10:54,620 --> 00:10:57,260
Okay, so let's run this once again.

154
00:10:57,260 --> 00:11:00,180
So to run this we are going to say Python three.

155
00:11:00,220 --> 00:11:05,100
Get js.py and we are going to provide the file name of JavaScript.

156
00:11:05,220 --> 00:11:07,580
So let's provide a JavaScript file.

157
00:11:09,860 --> 00:11:12,540
Uh let's say in.

158
00:11:14,620 --> 00:11:18,140
JS download any JavaScript file.

159
00:11:18,140 --> 00:11:22,220
So let's say uh email decode or maybe Main.js.

160
00:11:22,220 --> 00:11:24,140
So let's say Main.js and hit enter.

161
00:11:25,940 --> 00:11:27,020
Oh okay.

162
00:11:27,460 --> 00:11:29,900
It is expecting a URL, not a file.

163
00:11:29,900 --> 00:11:32,780
So let's provide the URL now.

164
00:11:33,260 --> 00:11:35,460
So I have a URL.

165
00:11:41,100 --> 00:11:41,620
That.

166
00:11:44,620 --> 00:11:49,670
Act if I js dot txt Let's say head.

167
00:11:50,790 --> 00:11:54,070
Let's see if this file is present.

168
00:11:57,790 --> 00:11:58,150
Okay.

169
00:12:21,950 --> 00:12:22,430
Yes.

170
00:12:22,430 --> 00:12:23,350
Did you see that?

171
00:12:23,790 --> 00:12:32,150
Now our JS file our txt file is basically sending request to the JavaScript file and get js words.

172
00:12:32,150 --> 00:12:34,750
Dot py is basically extracting words out of it.

173
00:12:35,270 --> 00:12:36,550
Did you see these words?

174
00:12:36,950 --> 00:12:38,870
Now let me stop this.

175
00:12:39,190 --> 00:12:44,590
Let me stop this and let me do the same thing for copy.

176
00:12:44,630 --> 00:12:48,120
Get JS words.py five into space.

177
00:12:55,880 --> 00:12:57,200
And let's do the same thing here.

178
00:12:57,200 --> 00:13:02,880
So let's say that SBI MF way back.

179
00:13:04,920 --> 00:13:05,560
Way back.

180
00:13:05,600 --> 00:13:09,560
JavaScript and Python three get JS words.

181
00:13:09,760 --> 00:13:14,360
What we are doing currently here we are reading all the JavaScript files and we are extracting words

182
00:13:14,360 --> 00:13:16,520
from it that is going to be used for us.

183
00:13:17,000 --> 00:13:21,520
So look participant mutual fund, SBI mutual fund.

184
00:13:21,520 --> 00:13:27,480
It's a very common word that can be an endpoint or it can be a subdomain okay.

185
00:13:28,240 --> 00:13:29,400
Hidden pan.

186
00:13:29,640 --> 00:13:34,520
Pan can be a specific word KYC form as you can see over here.

187
00:13:34,920 --> 00:13:36,720
Then let us see more words.

188
00:13:36,760 --> 00:13:40,240
Quick investment quick investment form.

189
00:13:41,240 --> 00:13:46,570
And similarly you would be able to see uh markets Its risks.

190
00:13:46,810 --> 00:13:51,890
These are all the words that are going to be helpful for us that we will be using for fuzzing.

191
00:13:52,130 --> 00:13:54,690
This is very targets.

192
00:13:55,010 --> 00:13:57,330
This is very, very target specific.

193
00:13:57,810 --> 00:14:04,730
Uh, wordlist generation technique that helps you to get Swpp calculator.

194
00:14:04,770 --> 00:14:12,130
STP calculator I'm sure that the there would be subdomains or endpoints for these investments retirement

195
00:14:12,130 --> 00:14:15,130
calculator.sbi.com, etc..

196
00:14:15,130 --> 00:14:22,130
So this is very specific technique for generation of wordlist for banking specific targets that you

197
00:14:22,130 --> 00:14:25,410
can utilize later on as well on other targets as well.

198
00:14:25,410 --> 00:14:27,410
And this is going to yield you very good results.

199
00:14:27,450 --> 00:14:27,850
Okay.

200
00:14:28,010 --> 00:14:30,650
So we did not save these results earlier in a file.

201
00:14:30,650 --> 00:14:31,770
Let me save these results.

202
00:14:31,770 --> 00:14:38,330
And then I'll quickly run a subdomain enumeration using the same wordlist to show you how successful

203
00:14:38,330 --> 00:14:38,770
we get.

204
00:14:38,770 --> 00:14:39,250
Okay.

205
00:14:39,290 --> 00:14:41,770
So let me just save these results quickly into a file.

206
00:14:41,770 --> 00:14:45,870
Let's call it as sbi mf wordlist list dot txt.

207
00:14:48,190 --> 00:14:51,790
Okay, now this word list dot txt is being generated.

208
00:14:51,790 --> 00:14:52,630
Excellent.

209
00:14:52,910 --> 00:14:57,310
Now let me show you that how you much useful this is.

210
00:14:57,590 --> 00:15:00,350
So I'm going to go into that same folder.

211
00:15:14,550 --> 00:15:15,750
CDs by.

212
00:15:20,030 --> 00:15:20,750
Wayback.

213
00:15:21,830 --> 00:15:23,190
It is not a directory.

214
00:15:23,670 --> 00:15:25,070
What is the directory name?

215
00:15:25,110 --> 00:15:25,830
Just a second.

216
00:15:28,670 --> 00:15:31,870
I think these many words are sufficient that we have found.

217
00:15:31,870 --> 00:15:33,390
So I'll just close this.

218
00:15:33,430 --> 00:15:33,830
Okay.

219
00:15:34,150 --> 00:15:40,270
So now we have a lot of words that we have found and added to SVM word list.

220
00:15:40,470 --> 00:15:41,910
You want to see the word list.

221
00:15:46,080 --> 00:15:50,200
This is the word list that we have currently, which is having all of these words.

222
00:15:50,400 --> 00:15:50,920
Okay.

223
00:15:50,960 --> 00:15:53,080
Approximately how many words we have found.

224
00:15:56,160 --> 00:15:59,000
Uh, 25.

225
00:15:59,680 --> 00:16:05,520
Uh, sorry, two lakh 51,281 words, uh, for a specific target.

226
00:16:05,560 --> 00:16:10,520
Now, let us use this to do subdomain enumeration to do, uh, asset discovery.

227
00:16:10,560 --> 00:16:10,960
Okay.

228
00:16:11,120 --> 00:16:12,880
So I'm going to run subroute.

229
00:16:15,120 --> 00:16:20,000
Before that we are going to specify that please use this word list.

230
00:16:25,760 --> 00:16:30,360
And time to start on the target.

231
00:16:30,760 --> 00:16:32,400
Let's hit enter and wait.

232
00:16:39,960 --> 00:16:41,600
Did you see that participants.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:02,400 --> 00:00:10,000
We have a target specific word list that is used for us here.

2
00:00:10,040 --> 00:00:15,280
Any other word list wouldn't work if you go ahead and take maybe Jason headaches, all dot, txt or

3
00:00:15,280 --> 00:00:25,120
best DNS word list, etc. they might not be appropriate here because this developer who has been working

4
00:00:25,120 --> 00:00:30,560
for this organization, or maybe he's also working as a DevOps engineer or system admin.

5
00:00:30,600 --> 00:00:35,480
He would be doing a lot of things over here for this target that he knows.

6
00:00:35,480 --> 00:00:39,360
So maybe that given subdomain name might not be in other common word list.

7
00:00:39,400 --> 00:00:47,680
Maybe, just for example, if he has created a subdomain which is known as thanos.com.

8
00:00:48,040 --> 00:00:50,600
And definitely that's not a common subdomain.

9
00:00:50,880 --> 00:00:56,320
So that word not might not be there in other subdomain or word list that you have.

10
00:00:56,360 --> 00:00:58,480
Okay, now you are getting repetitive.

11
00:00:58,480 --> 00:01:02,480
It is because, uh, we did not clean the word list.

12
00:01:02,520 --> 00:01:06,810
Uh, ideally we should have cleaned that word list to remove duplicates.

13
00:01:07,130 --> 00:01:11,730
And as we did not do that, you are able to see repeated words identified over here.

14
00:01:11,890 --> 00:01:12,250
Okay.

15
00:01:12,650 --> 00:01:17,570
Uh, anyways, we can go here to just confirm that the asset that we have found is correct.

16
00:01:17,890 --> 00:01:19,770
And congratulation.

17
00:01:20,050 --> 00:01:21,930
You have found a sign in page.

18
00:01:22,810 --> 00:01:23,250
Okay.

19
00:01:23,930 --> 00:01:26,930
On learning.com.

20
00:01:27,490 --> 00:01:27,850
Okay.

21
00:01:28,050 --> 00:01:29,330
You can see corporate.

22
00:01:29,930 --> 00:01:31,130
Let's go to corporate.

23
00:01:32,130 --> 00:01:32,690
Yes.

24
00:01:33,090 --> 00:01:36,370
We have found a successful page that has a login button over here.

25
00:01:36,610 --> 00:01:37,290
Excellent.

26
00:01:37,570 --> 00:01:38,130
Then we have.

27
00:01:38,130 --> 00:01:38,570
Hi.

28
00:01:38,810 --> 00:01:40,010
Maybe we can go to hi.

29
00:01:40,290 --> 00:01:47,850
And just, uh, we are going here just to confirm that the the output that we are getting is accurate

30
00:01:47,850 --> 00:01:48,850
and correct.

31
00:01:48,850 --> 00:01:49,450
So you can see.

32
00:01:49,450 --> 00:01:49,770
Yes.

33
00:01:49,770 --> 00:01:50,210
Hi dot.

34
00:01:50,210 --> 00:01:53,930
SBI MF also is present okay.

35
00:01:53,970 --> 00:01:54,530
Excellent.

36
00:01:54,570 --> 00:01:55,850
Now let me stop this.

37
00:01:56,290 --> 00:02:01,530
And we can just remove duplicates from here.

38
00:02:01,770 --> 00:02:03,650
So let me show you with duplicates.

39
00:02:03,650 --> 00:02:06,050
It is two lakh 51,000.

40
00:02:06,090 --> 00:02:07,410
Let's remove duplicates.

41
00:02:07,450 --> 00:02:11,700
Sort What you need and you need.

42
00:02:13,420 --> 00:02:17,660
Okay, so we have 914 unique words in this word list okay.

43
00:02:18,060 --> 00:02:20,820
Now let's save them in the in a file.

44
00:02:21,020 --> 00:02:25,340
SBI MF word list one dot txt.

45
00:02:26,380 --> 00:02:26,780
Okay.

46
00:02:27,860 --> 00:02:29,340
Uh, did we do that right?

47
00:02:29,340 --> 00:02:29,820
Yes.

48
00:02:31,580 --> 00:02:32,140
Nice.

49
00:02:32,260 --> 00:02:34,460
So now we are going to do that subroute once again.

50
00:02:34,460 --> 00:02:40,980
But we are going to say use this new word list as MF one list one dot txt and start this.

51
00:02:42,900 --> 00:02:47,460
So we have around 900 words now approximately 900 words.

52
00:02:47,700 --> 00:02:49,820
And you will see duplicates will not be there.

53
00:02:50,060 --> 00:02:53,620
So you can see corporate high learning services.

54
00:02:53,900 --> 00:03:00,580
These are four unique subdomains found from a word list that we generated from JavaScript files, from

55
00:03:00,580 --> 00:03:06,620
functions and variables for the given target, so that we be successful then other users.

56
00:03:06,660 --> 00:03:07,060
Okay.

57
00:03:07,420 --> 00:03:14,260
Ah, one small thing you can see services capital services small when we do removing or deduplicates

58
00:03:14,620 --> 00:03:17,260
because S is capital, it did not consider it same.

59
00:03:17,260 --> 00:03:25,380
But yes, these types of cases can also be removed uh by doing case insensitive remove of duplicate.

60
00:03:25,380 --> 00:03:25,780
Okay.

61
00:03:25,940 --> 00:03:28,100
But anyways, you can see this got completed.

62
00:03:28,100 --> 00:03:29,100
It was very fast.

63
00:03:29,260 --> 00:03:33,700
It iterated over 900 words and found these results for us.

64
00:03:33,700 --> 00:03:41,020
We we actually closed the task of get JS words because it would have taken a lot of time for us, but

65
00:03:41,060 --> 00:03:44,820
eventually to show you and confirm that yes, we are successful.

66
00:03:44,820 --> 00:03:49,620
And this technique is definitely a very useful technique to identify hidden assets.

67
00:03:49,940 --> 00:03:57,020
Now, participants, as we have done in asset discovery to find subdomains that are active, I want

68
00:03:57,020 --> 00:04:02,660
you to practice doing, uh, content discovery.

69
00:04:02,660 --> 00:04:12,380
Please utilize the same word list using a tool like WFirst or Fuf or directory Buster, or directory

70
00:04:12,420 --> 00:04:16,060
search and see how many endpoints you are able to find.

71
00:04:16,110 --> 00:04:22,470
Okay, use this word list to to identify or to to to do directory enumeration.

72
00:04:22,470 --> 00:04:29,150
And you would be able to see that you find a lot of very useful endpoints and directories, uh, through

73
00:04:29,150 --> 00:04:30,390
this given word list.

74
00:04:31,790 --> 00:04:32,070
Okay.

75
00:04:32,070 --> 00:04:34,630
Participants, are you all with me able to understand?

76
00:04:34,630 --> 00:04:35,550
Please confirm.

77
00:04:44,350 --> 00:04:44,990
Great.

78
00:04:45,590 --> 00:04:48,430
Now, one last thing for today's session.

79
00:04:48,430 --> 00:04:54,150
All of those words that you have actually generated, participants, you can give give this word list.

80
00:04:54,150 --> 00:04:56,310
You can put them into a txt file.

81
00:04:56,510 --> 00:05:02,270
And you can give it to our olama and ask it to generate permutations for you.

82
00:05:02,590 --> 00:05:02,950
Okay.

83
00:05:02,990 --> 00:05:09,910
For example hi hyphen learning.sbf.com can be a subdomain.

84
00:05:09,910 --> 00:05:18,270
So based on hi and learning, we can ask Allama to generate a new combination for us that we are going

85
00:05:18,270 --> 00:05:24,360
to utilize to do more better subdomain enumeration or or asset discovery over here.

86
00:05:24,400 --> 00:05:24,800
Okay.

87
00:05:25,080 --> 00:05:28,640
So that is a task that will keep leave up to you.

88
00:05:28,960 --> 00:05:35,440
You can use this file to give it to your open web UI Olama that you are currently running, and ask

89
00:05:35,440 --> 00:05:43,480
it to generate permutation, combination and combinations for you and utilize that to again do the same,

90
00:05:43,840 --> 00:05:45,840
uh, discovery of assets.

91
00:05:45,840 --> 00:05:50,400
And you will be surprised to see a lot of assets that you were able to find.

92
00:05:50,840 --> 00:05:51,280
Okay.

93
00:05:52,880 --> 00:05:58,160
Uh, these permutations help you identify more and more assets.

94
00:05:58,200 --> 00:05:58,840
Hidden assets.

95
00:05:58,880 --> 00:05:59,080
Okay.

96
00:05:59,120 --> 00:06:07,240
Just for example, I'll tell you, let's say Rohit dot dot in is a domain, is a subdomain.

97
00:06:07,240 --> 00:06:07,640
Okay.

98
00:06:08,000 --> 00:06:14,760
Uh, that I have created and there is dev dot dot in which is created.

99
00:06:14,920 --> 00:06:21,920
Now the, the chances are high that there could be a subdomain which is created.

100
00:06:21,920 --> 00:06:26,410
That is Rohit Dev .5. n.

101
00:06:26,450 --> 00:06:27,930
Okay, but I don't know.

102
00:06:27,930 --> 00:06:31,410
This subdomain is there using passive techniques.

103
00:06:31,410 --> 00:06:33,490
But I have got these two subdomains.

104
00:06:33,850 --> 00:06:39,090
So what I will do is I will ask Ola to generate combinations for me of subdomains.

105
00:06:39,090 --> 00:06:44,250
So Ola says try rohit.dev and try dev dot Rohit as well.

106
00:06:45,370 --> 00:06:51,810
Okay as in valid subdomain for the task for the target.

107
00:06:51,810 --> 00:06:52,250
Sorry.

108
00:06:52,570 --> 00:06:59,050
And by doing this, you would be surprised to see that actually there have been plenty of test cases

109
00:06:59,050 --> 00:07:05,810
where combination of subdomains have turned out to be present on targets, and you would be able to

110
00:07:05,810 --> 00:07:10,290
see a lot of subdomains like these, which you can find with the permutation technique.

111
00:07:10,770 --> 00:07:11,970
So you can give it a try.

112
00:07:12,010 --> 00:07:19,330
Participants, please try it out and let me know what were your results if you are not able to do it,

113
00:07:19,330 --> 00:07:21,090
no problem in the next session.

114
00:07:21,090 --> 00:07:24,570
Tomorrow I will also show how to do that practically.

115
00:07:32,170 --> 00:07:32,410
Uh.

116
00:07:32,450 --> 00:07:35,610
Why such subdomains are not identified in the first place.

117
00:07:36,010 --> 00:07:42,650
Uh, it is because these subdomains, if these subdomains are created fairly, these are new, fairly

118
00:07:42,650 --> 00:07:47,130
new, then these subdomains would not be found by passive techniques because they might not have been

119
00:07:47,130 --> 00:07:47,930
crawled yet.

120
00:07:48,530 --> 00:07:50,130
So that is the first thing.

121
00:07:50,290 --> 00:07:56,930
Second is, uh, when you are doing active, uh, subdomain enumeration and you have a word list that

122
00:07:56,930 --> 00:08:01,730
contains only Rohit and Dev, but not Rohit dev, then you will miss this again.

123
00:08:01,970 --> 00:08:08,930
So to get this, we are now doing permutations of both passive domains that we have found, active domains

124
00:08:08,930 --> 00:08:14,050
we have found and generate new domains and then test it out if this these exist or not.

125
00:08:18,570 --> 00:08:19,090
Yep.

126
00:08:19,250 --> 00:08:23,090
Uh, I hope uh, that is clear.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,440 --> 00:00:02,200
Uh, let's start participants.

2
00:00:02,280 --> 00:00:09,600
So currently, what you can see in front of me is the open web UI instance, which has been running,

3
00:00:10,080 --> 00:00:12,280
uh, we have already seen how to configure this.

4
00:00:12,280 --> 00:00:16,160
This is running currently into a Docker container, as you can see over here.

5
00:00:16,560 --> 00:00:21,760
And uh, it is currently utilizing the model which is a llama 3.1.

6
00:00:21,920 --> 00:00:24,640
And you can see llama is currently running over here.

7
00:00:24,760 --> 00:00:30,720
And if you see one of my terminals then you can also see uh, llama three is currently running in the

8
00:00:30,720 --> 00:00:31,320
background.

9
00:00:31,760 --> 00:00:32,440
Excellent.

10
00:00:32,800 --> 00:00:42,720
Now let us start, uh, today's session by understanding about what is exactly rag modeling.

11
00:00:42,760 --> 00:00:46,240
Okay, so if I can show you a diagram.

12
00:00:46,680 --> 00:00:51,400
So so basically Rag stands for retrieval augmented generation.

13
00:00:51,560 --> 00:00:53,640
So let me help.

14
00:00:53,800 --> 00:00:59,360
Let me take an diagram to explain you that rag modeling.

15
00:01:02,800 --> 00:01:03,200
Um.

16
00:01:12,630 --> 00:01:13,030
Yeah.

17
00:01:16,830 --> 00:01:19,230
I think this is this is good.

18
00:01:19,270 --> 00:01:20,230
Simple to understand.

19
00:01:20,230 --> 00:01:20,670
Okay.

20
00:01:20,790 --> 00:01:23,270
So first of all, what is Rag modeling.

21
00:01:23,270 --> 00:01:28,990
It is one of the techniques that is used to train your large language model.

22
00:01:28,990 --> 00:01:30,790
What is our large language model here?

23
00:01:30,830 --> 00:01:37,310
Oh llama 3.18 billion instruction is the model that we are LM model that we are using.

24
00:01:37,310 --> 00:01:38,110
What is rag?

25
00:01:38,310 --> 00:01:45,750
Rag is one of the techniques through which you can enhance the knowledge base of your model without

26
00:01:45,790 --> 00:01:47,510
training it from the scratch.

27
00:01:47,670 --> 00:01:49,710
Now for training a model from scratch.

28
00:01:49,710 --> 00:01:56,230
It is going to take a lot of computational power and a lot of large knowledge base.

29
00:01:56,270 --> 00:02:01,230
We currently do not have that capability to train the model from scratch.

30
00:02:01,390 --> 00:02:08,990
Hence, we are going to use a pre-built or a model that already has its knowledge to add on the knowledge

31
00:02:08,990 --> 00:02:17,780
that we want it to do and in reality, this is a good approach to do so that the model itself has its

32
00:02:17,780 --> 00:02:24,300
own prior knowledge and information in and on top of that, we train it specific to the area or domain

33
00:02:24,300 --> 00:02:25,140
that we want.

34
00:02:25,380 --> 00:02:33,140
For today's practical, we are going to train the model on pen testing and bug bounties and then see

35
00:02:33,140 --> 00:02:36,580
what is the different type of responses that we are able to get from the model.

36
00:02:36,900 --> 00:02:38,020
So what is rag?

37
00:02:38,420 --> 00:02:45,340
Rag is a technique that enhances the capabilities of the LLM by integrating external knowledge that

38
00:02:45,340 --> 00:02:46,020
we want.

39
00:02:46,500 --> 00:02:50,580
Now, as we can see over here participant, we give a prompt.

40
00:02:50,860 --> 00:02:56,580
When we give a prompt, what basically happens is our prompt goes to the LLM.

41
00:02:56,940 --> 00:03:05,340
Now the LLM has a document store where it is going to store all of the, uh, information or knowledge

42
00:03:05,780 --> 00:03:08,020
into small chunks of data.

43
00:03:08,620 --> 00:03:14,500
That data that has been broken down into chunks is usually stored in the form of a vector database.

44
00:03:14,860 --> 00:03:21,250
Now to explain this, we might also understand about how a neural network works, but as of now, in

45
00:03:21,290 --> 00:03:28,250
a simple, simplified version, we can understand this, that when you give a prompt to a LLM, the

46
00:03:28,290 --> 00:03:30,210
your request goes to the document store.

47
00:03:30,210 --> 00:03:34,610
And then data is being retrieved from the knowledge base that you have fed.

48
00:03:34,890 --> 00:03:38,090
Knowledge base can be in the form of documents.

49
00:03:38,090 --> 00:03:39,890
It could be in the form of audio.

50
00:03:39,890 --> 00:03:41,810
It could be in the form of video.

51
00:03:42,250 --> 00:03:51,330
The current model that we are going to use that is llama 3.1 is a model that is textual text conceptual

52
00:03:51,330 --> 00:03:51,930
model.

53
00:03:51,930 --> 00:03:55,330
That means it can understand text based information.

54
00:03:55,610 --> 00:03:59,330
There are more models given by Facebook or Meta like llama.

55
00:03:59,330 --> 00:04:00,890
We have we have llama.

56
00:04:01,290 --> 00:04:05,530
Llama is again a free model that is more helpful for doing coding related tasks.

57
00:04:05,730 --> 00:04:11,010
Then we have Mistral model given by Facebook, which is again open source, which is capable of doing

58
00:04:11,010 --> 00:04:13,250
more tasks with audio as well.

59
00:04:13,250 --> 00:04:17,970
And similarly, we have more different types of open source models that we can use based on different

60
00:04:17,970 --> 00:04:20,530
different data sources that we want to feed.

61
00:04:20,770 --> 00:04:25,430
For today, we are going to feed textual based data to the given model.

62
00:04:25,790 --> 00:04:35,390
Hence, we are going to utilize our knowledge base in the form of documents or documents can be of any

63
00:04:35,430 --> 00:04:35,990
file type.

64
00:04:35,990 --> 00:04:41,590
It could be a PDF or a word document, a JavaScript file, a markdown file, a Python code, anything

65
00:04:41,590 --> 00:04:42,230
like that.

66
00:04:42,590 --> 00:04:49,150
Now this retrieved document is going to be processed by the generator.

67
00:04:49,590 --> 00:04:56,510
Generator is basically the language model generation technique uh which it utilizes.

68
00:04:56,510 --> 00:04:58,070
And then it gives the response.

69
00:04:58,190 --> 00:05:07,030
So just imagine if the this part that you see currently on the screen, if it was not present, if it

70
00:05:07,030 --> 00:05:12,070
was not present, then your prompt would go to the language models generator.

71
00:05:12,070 --> 00:05:14,070
And then it is going to give you a response.

72
00:05:14,110 --> 00:05:19,830
Let us say I am going to ask my model a question that what is somatosensory system?

73
00:05:19,950 --> 00:05:30,180
Somatosensory system is basically a human body system which works on how skin our body skin behaves

74
00:05:30,380 --> 00:05:33,020
when we feel something hot or cold.

75
00:05:33,060 --> 00:05:40,060
Now, this is a very specialized topic in biology, and maybe my model is not trained on to very specialized

76
00:05:40,060 --> 00:05:41,420
topics of biology.

77
00:05:41,420 --> 00:05:46,580
So it might say very basic information about somatosensory system as an example.

78
00:05:46,580 --> 00:05:49,140
Or it might not give an efficient output as well.

79
00:05:49,140 --> 00:05:55,300
It might say, okay, I'm not aware about much about this, or maybe just only two lines about it,

80
00:05:55,660 --> 00:06:04,740
but rather when I give a research paper as an A document to the model to understand and expand its knowledge

81
00:06:04,740 --> 00:06:12,660
base, then it is going to be giving me more effective, detailed output about that domain knowledge

82
00:06:12,660 --> 00:06:16,700
and explains about what somatosensory system is.

83
00:06:17,140 --> 00:06:21,900
So this is primarily in a nutshell, how a rag modeling works.

84
00:06:21,900 --> 00:06:28,460
We are enhancing the capabilities of a language model by giving external knowledge sources and training

85
00:06:28,460 --> 00:06:29,740
it onto that data.

86
00:06:30,580 --> 00:06:33,300
I hope this is clear with all participants.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,640 --> 00:00:03,440
So this is how basically the Rag modeling works.

2
00:00:03,440 --> 00:00:13,320
And now it's important for us that as we have been utilizing the given model from last two of our sessions,

3
00:00:13,760 --> 00:00:21,240
and we have not trained the model yet, so that it effectively works in a manner that it gives us more

4
00:00:21,240 --> 00:00:25,120
refined, specialized, and better output.

5
00:00:25,240 --> 00:00:31,680
So to do that, we are going to train the model with external knowledge resource.

6
00:00:32,360 --> 00:00:38,640
And it is absolutely very, very simple and straightforward process.

7
00:00:38,680 --> 00:00:40,240
Let's see how do we do it.

8
00:00:40,760 --> 00:00:45,560
So to do that participants on your open web UI please go to workspace.

9
00:00:46,240 --> 00:00:51,120
Once you go to workspace participants you can go to the knowledge option.

10
00:00:51,920 --> 00:00:57,720
So if you see on the knowledge option currently you can see there are two knowledge base for me.

11
00:00:57,760 --> 00:01:00,680
First is Vaf and second is API knowledge base.

12
00:01:00,800 --> 00:01:06,990
I have created this for demonstration that I will show you today, but for you they might not be present,

13
00:01:07,190 --> 00:01:09,030
so you might see an empty window.

14
00:01:09,030 --> 00:01:12,470
Here you can simply go to this plus icon and see.

15
00:01:14,950 --> 00:01:18,150
A message in front of you which says create a knowledge base.

16
00:01:18,830 --> 00:01:24,790
Now you can fill up basic information about what this knowledge base is going to be about.

17
00:01:25,390 --> 00:01:28,590
So let's say this knowledge base is about uh.

18
00:01:30,910 --> 00:01:34,470
Let's say human body, just for an example.

19
00:01:35,230 --> 00:01:37,190
And what are you trying to achieve?

20
00:01:37,310 --> 00:01:38,790
You can give anything that you want.

21
00:01:38,790 --> 00:01:41,750
This is just for your reference and will not be used anywhere.

22
00:01:42,870 --> 00:01:50,670
Detailed analysis of human body and how skin works.

23
00:01:50,710 --> 00:01:52,550
Okay, this is just an example.

24
00:01:53,270 --> 00:01:54,350
Uh, visibility.

25
00:01:54,390 --> 00:02:02,270
Now as in our open UI web dashboard, you can also create from the admin panel multiple users and give

26
00:02:02,270 --> 00:02:04,670
them access control of what they can do.

27
00:02:04,790 --> 00:02:11,630
So for example, I want to share the access of my open web UI that is currently running onto a trained

28
00:02:11,630 --> 00:02:17,630
model to my friend, let's say Jerry, so that he can also access it, do activities, whatever he want.

29
00:02:17,670 --> 00:02:20,590
But I want to restrict what more things he can do.

30
00:02:20,630 --> 00:02:25,390
He cannot change the system prompt, he cannot change settings from the tool menu, etc. so all of that

31
00:02:25,390 --> 00:02:26,070
can be done.

32
00:02:26,390 --> 00:02:30,350
So you can choose the visibility here I'll choose the visibility as public.

33
00:02:30,350 --> 00:02:36,910
That means all the users currently on my Open Web UI dashboard have access to this knowledge base.

34
00:02:36,910 --> 00:02:39,110
Let's create click on Create Knowledge.

35
00:02:40,030 --> 00:02:45,790
Once you do that participant here you can see it is now asking you to add collection.

36
00:02:45,790 --> 00:02:48,270
So we can see our collection is currently empty.

37
00:02:48,550 --> 00:02:54,030
You can click on plus and you can see it will ask you to upload files directories.

38
00:02:54,030 --> 00:02:58,670
You can sync a directory or you can add text content directly over here.

39
00:02:58,870 --> 00:03:00,910
So I recommend here.

40
00:03:00,910 --> 00:03:08,950
In this step we can take examples of many research papers on human body and feed it to our model.

41
00:03:08,990 --> 00:03:09,430
Okay.

42
00:03:09,470 --> 00:03:11,030
This is just an example.

43
00:03:11,150 --> 00:03:16,980
We are going to do the same thing for pen testing and red teaming related RFPs.

44
00:03:17,140 --> 00:03:20,700
So what does RF uh RFCs.

45
00:03:20,820 --> 00:03:21,860
RFC sorry.

46
00:03:22,140 --> 00:03:24,980
So request for comments.

47
00:03:25,260 --> 00:03:32,020
Uh, are basically standards that are being created in this world of how things work.

48
00:03:32,020 --> 00:03:34,980
So let's say http rfc.

49
00:03:35,700 --> 00:03:40,260
So HTTP is is basically the protocol Hypertext Transfer Protocol.

50
00:03:40,260 --> 00:03:43,220
So how does HTTP work.

51
00:03:43,620 --> 00:03:45,580
This is the guide which is the RFC.

52
00:03:45,620 --> 00:03:50,060
It is absolutely boring to go ahead and read about an RFC.

53
00:03:50,300 --> 00:03:59,820
But trust me, participants all of the world's best security researchers or research that you see in

54
00:03:59,820 --> 00:04:06,860
which they have identified classic vulnerabilities and zero days are only based on RFCs.

55
00:04:06,900 --> 00:04:15,900
And I cannot stop mentioning, reading or understanding RFCs to understand how different types of protocol

56
00:04:15,900 --> 00:04:22,020
works to identify security flaws from it, you can research and google more about it.

57
00:04:22,060 --> 00:04:29,540
Many security reputed security researchers or bug bounty hunters have stressed on the importance of

58
00:04:29,540 --> 00:04:33,980
RFCs in leading to discovery of new vulnerabilities.

59
00:04:33,980 --> 00:04:40,180
But I can totally understand RFCs are very, very boring documents, so we cannot read it manually.

60
00:04:40,180 --> 00:04:49,180
But when we have AI capabilities, it can definitely read it for us and give us the summary or the crux

61
00:04:49,180 --> 00:04:50,820
about how RFC works.

62
00:04:50,980 --> 00:04:56,980
So for example, in this RFC we can see about different types of protocol.

63
00:04:57,180 --> 00:05:00,500
So let's say sorry a status codes.

64
00:05:00,660 --> 00:05:09,940
So we can see status code starting from 100 means continue 101 is switching protocols 200 okay 20120223203204.

65
00:05:10,060 --> 00:05:13,660
So maybe if I want to read more about 204, I can go to that page.

66
00:05:13,860 --> 00:05:18,540
And I can read what 204 status code means.

67
00:05:18,740 --> 00:05:21,380
And trust me, it has.

68
00:05:21,540 --> 00:05:25,500
Reading RFCs has been very, very helpful for me in the past as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:01,600
Abilities on targets.

2
00:00:01,840 --> 00:00:04,000
And here specifically I want to give.

3
00:00:04,040 --> 00:00:06,360
I want to quote and give an example of an.

4
00:00:06,400 --> 00:00:11,520
Vulnerability that I found on Apple Bug Bounty program, and it was an account takeover.

5
00:00:11,560 --> 00:00:18,600
Into their Apple ID sign up process by with the help of an RFC document wherein.

6
00:00:19,000 --> 00:00:24,160
Status code 204 means uh response.

7
00:00:24,160 --> 00:00:27,440
So so it basically means the request has been succeeded.

8
00:00:27,440 --> 00:00:33,000
But it is it do not want to return the body uh, or anything in the body.

9
00:00:33,000 --> 00:00:34,400
So that means 204.

10
00:00:34,560 --> 00:00:40,640
So 1 in 1 of the test cases participants, I got a response that was bad request and I modified it to

11
00:00:40,680 --> 00:00:41,720
204.

12
00:00:42,200 --> 00:00:45,840
And when I did that it actually did not ask me the OTP.

13
00:00:45,840 --> 00:00:47,440
I still have the video POC.

14
00:00:47,720 --> 00:00:50,840
I will share it with you participants and you can see it.

15
00:00:50,880 --> 00:00:53,160
Maybe I'll just try to show you quickly.

16
00:00:59,240 --> 00:00:59,680
Yeah.

17
00:00:59,880 --> 00:01:07,560
So here is an POC, uh, a vulnerability that I reported to Apple in the year 2020 for an authentication

18
00:01:07,670 --> 00:01:10,150
bypass on Apple ID creation process.

19
00:01:10,150 --> 00:01:13,110
I'll skip everything and just directly jump to the main part.

20
00:01:14,270 --> 00:01:22,590
So here you can see I have I have received an OTP on my email currently and this is the OTP.

21
00:01:22,630 --> 00:01:27,470
Verify your Apple ID 132797 and I'll take this OTP.

22
00:01:27,510 --> 00:01:28,310
Go here.

23
00:01:28,630 --> 00:01:29,510
Enter it.

24
00:01:29,910 --> 00:01:32,830
So I'm going to change the last digit to six over here.

25
00:01:36,510 --> 00:01:38,830
From my Burpsuite.

26
00:01:38,830 --> 00:01:41,190
So you can see it is seven I'm going to change it to six.

27
00:01:44,070 --> 00:01:49,230
And when I change the OTP to six to verify my Apple ID, it is going to give me an error.

28
00:01:49,270 --> 00:01:50,230
Do you all agree.

29
00:01:51,750 --> 00:01:53,550
Because that's an OTP right?

30
00:01:55,830 --> 00:01:56,750
Do you all agree?

31
00:01:57,270 --> 00:01:57,790
Yes.

32
00:01:59,350 --> 00:01:59,910
Yes.

33
00:02:00,310 --> 00:02:00,830
Right.

34
00:02:00,830 --> 00:02:02,950
So I'll change this 7 to 6.

35
00:02:02,950 --> 00:02:06,750
And now I forward the request and I want to see the response.

36
00:02:06,950 --> 00:02:08,230
And you can see here.

37
00:02:10,510 --> 00:02:13,190
I got a 400 status code.

38
00:02:13,390 --> 00:02:16,550
You can see the message incorrect verification code.

39
00:02:16,710 --> 00:02:20,110
It is an incorrect verification code and 400 bad request.

40
00:02:20,150 --> 00:02:26,390
Now if you go back to the RFC, we can read about what 400 bad 400 status code it is.

41
00:02:26,550 --> 00:02:28,190
It is basically bad request.

42
00:02:28,190 --> 00:02:30,630
But I'm going to change this to 204.

43
00:02:30,910 --> 00:02:35,590
If you can see over here and I will forward the request.

44
00:02:36,830 --> 00:02:42,150
Did you see that we just went to the next step now which is verification of phone.

45
00:02:43,830 --> 00:02:48,190
So we bypass the email ID verification.

46
00:02:48,190 --> 00:02:51,150
And now we are on the phone verification page.

47
00:02:51,350 --> 00:02:51,870
Okay.

48
00:02:51,910 --> 00:02:55,550
Similarly we'll do this do this, do the same thing here.

49
00:02:55,550 --> 00:02:59,230
And we will be able to successfully create our account as we can see over here.

50
00:02:59,710 --> 00:03:00,030
Okay.

51
00:03:00,070 --> 00:03:08,070
I'm just trying to log in and show you that I've successfully able to get inside without the without

52
00:03:08,070 --> 00:03:11,550
the right OTP or without the correct email verification code.

53
00:03:11,550 --> 00:03:17,630
So this this was just an example of how RFCs can be important for us, but it can definitely be very

54
00:03:17,630 --> 00:03:18,750
boring to read them.

55
00:03:18,750 --> 00:03:23,030
But with the help of our llama model, we can automate the same process.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:00,960
Our knowledge base.

2
00:00:01,320 --> 00:00:05,680
Uh, we are going to train current model on how human body works.

3
00:00:05,680 --> 00:00:08,600
So I have a document that I'm going to feed it over here.

4
00:00:10,160 --> 00:00:12,960
And the document is going to be about.

5
00:00:16,400 --> 00:00:19,040
Document is going to be about.

6
00:00:19,400 --> 00:00:19,960
Yeah.

7
00:00:19,960 --> 00:00:23,840
So this is the document Anatomy of Somatosensory System.

8
00:00:24,000 --> 00:00:30,800
I have downloaded this four page document to explain how skin works and how human body skin actually

9
00:00:30,800 --> 00:00:34,440
reacts to whenever, uh, we feel hot or cold.

10
00:00:34,480 --> 00:00:34,840
Okay.

11
00:00:34,880 --> 00:00:40,480
It is just an off topic document, but I just want to show you as an example here.

12
00:00:40,480 --> 00:00:43,200
So I'm going to just take this document and drop it over here.

13
00:00:43,960 --> 00:00:45,600
File is added successfully.

14
00:00:47,400 --> 00:00:47,920
Done.

15
00:00:48,080 --> 00:00:49,800
Now we can click on this file.

16
00:00:49,800 --> 00:00:56,920
And you can see all of the data from the PDF format has been converted into textual format.

17
00:00:56,960 --> 00:00:57,440
Okay.

18
00:00:57,480 --> 00:01:00,520
Now once my knowledge base has been set up, as we can see.

19
00:01:00,560 --> 00:01:01,560
Yeah it's here.

20
00:01:01,880 --> 00:01:04,400
Now you can go back to workspace.

21
00:01:04,960 --> 00:01:06,360
Please go to models.

22
00:01:06,600 --> 00:01:14,250
Now we want to choose a model which only utilizes this information or the knowledge base that we have

23
00:01:14,250 --> 00:01:14,890
created.

24
00:01:14,970 --> 00:01:19,010
So we are going to set up a model to understand this given knowledge base.

25
00:01:19,090 --> 00:01:23,970
So I'm going to click on this plus icon and wait for a few seconds.

26
00:01:32,650 --> 00:01:33,210
Awesome.

27
00:01:33,330 --> 00:01:36,770
Now once you see this we are going to set up a new model.

28
00:01:36,770 --> 00:01:42,610
Let's give this model name as Human Body Llama.

29
00:01:43,410 --> 00:01:50,330
Okay, now we are going to choose a model which is going to be trained on the knowledge source.

30
00:01:50,330 --> 00:01:55,170
We have defined a knowledge source currently to open web UI.

31
00:01:55,330 --> 00:02:03,290
And now it is going to connect a model which is going to utilize that knowledge source and be more specific

32
00:02:03,330 --> 00:02:06,010
about the information that we want.

33
00:02:06,090 --> 00:02:08,210
So you can choose both of the any of the models.

34
00:02:08,210 --> 00:02:10,450
I'm going to choose llama three as of now.

35
00:02:10,890 --> 00:02:12,490
If you want you can give a description.

36
00:02:12,730 --> 00:02:15,070
So I'll just give a description here.

37
00:02:15,510 --> 00:02:21,390
I'll keep the visibility as public so all of the people in my account can access that.

38
00:02:21,870 --> 00:02:26,830
And if you want, you can put up a system prompt here, uh, of what the model is going to do.

39
00:02:26,830 --> 00:02:28,550
So I'm going to put a system prompt.

40
00:02:28,670 --> 00:02:36,390
You are an expert now in somato sensory systems.

41
00:02:38,550 --> 00:02:38,950
Okay.

42
00:02:39,430 --> 00:02:41,630
And we are going to select the knowledge.

43
00:02:41,790 --> 00:02:46,950
So now the knowledge is going to be the human body, the knowledge base that we have created.

44
00:02:46,950 --> 00:02:49,150
And click on Save and Create.

45
00:02:50,270 --> 00:02:50,790
Awesome.

46
00:02:50,910 --> 00:02:58,430
So we have successfully completed creating a model of our choice which is human body lava.

47
00:02:58,830 --> 00:02:59,710
Excellent.

48
00:02:59,750 --> 00:03:02,430
We have successfully created a knowledge base.

49
00:03:02,430 --> 00:03:06,630
We have successfully created a model and now it's time to use this.

50
00:03:06,630 --> 00:03:08,030
So let's go to new chat.

51
00:03:08,710 --> 00:03:14,270
Once you go to new chat, please choose the model that you want to use.

52
00:03:14,470 --> 00:03:19,790
We are going to use the model that we have trained right now which is Human Body Llama.

53
00:03:20,150 --> 00:03:23,760
I will choose that given model, which you can see here.

54
00:03:23,840 --> 00:03:28,160
You can also set this set that as default if you always want to use the same model.

55
00:03:28,520 --> 00:03:32,920
Uh, for our case we will be now creating a pen testing and bug bounty model.

56
00:03:32,920 --> 00:03:37,200
And we'll set that as default and not set human body as default.

57
00:03:37,360 --> 00:03:48,760
And I will ask, can you explain what is Somato sensory system?

58
00:03:51,040 --> 00:03:53,640
In nutshell.

59
00:04:04,360 --> 00:04:05,080
Excellent.

60
00:04:05,640 --> 00:04:08,040
So you can read more about it.

61
00:04:08,080 --> 00:04:13,200
It is a system of your body which can sense touch, pressure, temperature, vibration, pain.

62
00:04:13,440 --> 00:04:19,800
To put it simply, it feels touch different texture, temperature and pressure on your skin, body awareness,

63
00:04:19,800 --> 00:04:21,360
pain perception and everything.

64
00:04:21,480 --> 00:04:29,460
So you can just see how our four page document was converted into a vector database textual context

65
00:04:29,460 --> 00:04:36,260
form, and based on that, we are now able to identify information from the given prompt.

66
00:04:36,500 --> 00:04:38,180
Uh, yes.

67
00:04:38,540 --> 00:04:41,220
I think the prompt the response did not complete.

68
00:04:41,220 --> 00:04:44,900
So I'm going to click on yeah continue response.

69
00:04:44,900 --> 00:04:47,660
And you can see the references first and second.

70
00:04:47,860 --> 00:04:50,220
Now this is the response that we have received.

71
00:04:50,220 --> 00:04:53,060
You can copy the response if you want to hear the response.

72
00:04:53,140 --> 00:04:55,020
Somatosensory system refers.

73
00:04:55,260 --> 00:04:57,300
You can listen to that as well.

74
00:04:57,300 --> 00:05:04,500
And you can also export this conversation that we have done right now using the download feature.

75
00:05:04,500 --> 00:05:11,740
So I can download this into a PDF format and I can use it later on whenever I want.

76
00:05:11,900 --> 00:05:13,780
So this is the prompt that I gave.

77
00:05:13,780 --> 00:05:18,820
And this is the outcome that I have received specifically for the given prompt.

78
00:05:18,860 --> 00:05:21,860
You can also copy the conversation that has just happened.

79
00:05:22,100 --> 00:05:22,820
Paste it.

80
00:05:22,820 --> 00:05:24,780
So this is how conversation would look like.

81
00:05:25,100 --> 00:05:31,260
The user asked question and the assistant answered uh, question.

82
00:05:31,300 --> 00:05:31,700
Sorry.

83
00:05:31,700 --> 00:05:33,540
The assistant answered answer.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,080 --> 00:00:00,920
Is -- good.

2
00:00:01,280 --> 00:00:02,000
Absolutely.

3
00:00:02,000 --> 00:00:02,560
Yes.

4
00:00:02,560 --> 00:00:13,080
This is going to be a very good, uh, assistant for us because it is now going to make us, uh, help

5
00:00:13,280 --> 00:00:19,240
in a lot of specific information that we want to train our model on.

6
00:00:19,240 --> 00:00:24,080
And whenever you don't want to use this model and you want to use a common model, you can switch back

7
00:00:24,080 --> 00:00:28,200
to your llama three version that you want.

8
00:00:28,240 --> 00:00:30,960
Or maybe you want to choose any other models that you want.

9
00:00:31,280 --> 00:00:37,560
I've already trained a model on APIs where I have given API documentation for it to use, and now I

10
00:00:37,560 --> 00:00:40,960
can ask it API related questions of my choice.

11
00:00:40,960 --> 00:00:48,080
For example, I will give an API swagger API documentation to it and I will ask it to explain it to

12
00:00:48,080 --> 00:00:48,640
me.

13
00:00:48,680 --> 00:00:56,200
Identify all API endpoints, URLs, etc. and then I can then ask more questions and I can ask it to

14
00:00:56,320 --> 00:00:58,320
create test cases for me as well.

15
00:00:58,680 --> 00:01:06,130
So as I expressed that, I'm going to take an example of a bug bounty program right now for API security.

16
00:01:06,490 --> 00:01:10,370
So I'm going to say take Bentley as an example.

17
00:01:10,970 --> 00:01:14,450
Bentley, the car company, has a bug bounty program.

18
00:01:14,450 --> 00:01:18,130
Let me also show you that so we can go to Bentley Systems.

19
00:01:18,610 --> 00:01:26,290
And it has a bug bounty program where we can file a report and send an bug bounty report.

20
00:01:26,290 --> 00:01:33,690
They have a compensation matrix as well, when they where they pay up to 450 and $500 for issues, as

21
00:01:33,690 --> 00:01:34,810
you can see over here.

22
00:01:34,810 --> 00:01:35,490
Excellent.

23
00:01:35,810 --> 00:01:43,730
Now let's go on Google and say we are only specifically looking for Bentley bug bounty programs, uh,

24
00:01:43,770 --> 00:01:44,810
API hacking.

25
00:01:44,810 --> 00:01:54,410
So I'm going to say site Bentley, find out all the swagger API endpoints for me, which I will be using,

26
00:01:54,410 --> 00:02:02,930
because usually swagger API or swagger UI is the front end that is being used to run APIs in the background.

27
00:02:03,090 --> 00:02:05,370
So I can see def connect component.

28
00:02:06,970 --> 00:02:07,290
source.

29
00:02:07,570 --> 00:02:12,770
Component center service.com as in swagger API available here for me.

30
00:02:12,770 --> 00:02:21,050
So what I'm going to do is I'm going to take all of these requests one by one and feed it to my, uh,

31
00:02:21,970 --> 00:02:22,570
model.

32
00:02:22,570 --> 00:02:26,690
And I'm going to ask the model to understand what how does this work okay.

33
00:02:26,810 --> 00:02:30,530
So so you you need to simply click on swagger one Swagger.json.

34
00:02:30,570 --> 00:02:34,170
This is the swagger API which contains all the endpoints.

35
00:02:34,530 --> 00:02:41,490
Uh, there will be all endpoints for the target available over here that you saw on the screen.

36
00:02:43,210 --> 00:02:43,650
Yeah.

37
00:02:43,690 --> 00:02:47,250
For example API one context catalogs documents.

38
00:02:47,410 --> 00:02:54,450
So you can go here catalog data catalog okay.

39
00:02:54,690 --> 00:02:58,290
Context uh, shared catalogs documents etc..

40
00:02:58,290 --> 00:03:07,780
So now I will just copy this and I'm going to paste this into my API knowledge base.

41
00:03:07,780 --> 00:03:11,700
So to do that I'm going to go to workspace API.

42
00:03:11,740 --> 00:03:12,220
Llama.

43
00:03:13,740 --> 00:03:14,220
Sorry.

44
00:03:14,860 --> 00:03:20,860
Uh, knowledge api knowledge base I have added some JavaScript dummy files as well here.

45
00:03:21,140 --> 00:03:23,100
Uh, you can just ignore them.

46
00:03:23,100 --> 00:03:26,060
And I'm going to uh, choose the text feature.

47
00:03:31,380 --> 00:03:32,660
And textual contact.

48
00:03:36,620 --> 00:03:39,060
Uh, yes and yes.

49
00:03:39,060 --> 00:03:40,020
That is possible.

50
00:03:40,500 --> 00:03:43,380
Uh, that is possible in a certain manner.

51
00:03:43,380 --> 00:03:49,220
We have to do one configuration change, and we can allow llama to read content directly from websites.

52
00:03:49,220 --> 00:03:50,260
Yes, that is possible.

53
00:03:50,260 --> 00:03:52,500
That is not that is absolutely possible.

54
00:03:52,500 --> 00:03:55,020
It is, uh, one of the features that we have.

55
00:03:55,620 --> 00:03:57,780
Uh, but we'll enable that later.

56
00:03:57,820 --> 00:04:02,700
You can see this is the entire documentation that I have currently fed to this model.

57
00:04:02,700 --> 00:04:04,100
And I'm going to click on save.

58
00:04:04,580 --> 00:04:06,020
Uh, the file is added successfully.

59
00:04:06,020 --> 00:04:07,740
I should have given a name to the file.

60
00:04:08,620 --> 00:04:10,020
Uh, Uh, anyways.

61
00:04:10,020 --> 00:04:10,220
Okay.

62
00:04:10,220 --> 00:04:11,260
I did not give a name.

63
00:04:11,260 --> 00:04:12,100
That's okay.

64
00:04:12,100 --> 00:04:18,020
But I have added all the swagger API documentation for this given target now.

65
00:04:19,140 --> 00:04:27,460
Now what I can do is I can simply go to the new chat feature, open the API model, and ask it to parse

66
00:04:27,500 --> 00:04:29,500
the given API file for me.

67
00:04:29,660 --> 00:04:30,100
Okay.

68
00:04:30,340 --> 00:04:33,100
So I'll do that as well in a moment.

69
00:04:33,100 --> 00:04:38,620
Before that, let me go to knowledge API knowledge base and I'm going to remove all the files.

70
00:04:42,580 --> 00:04:45,300
These are all dummy files which have got added.

71
00:04:45,300 --> 00:04:45,860
Perfect.

72
00:04:47,660 --> 00:04:55,740
And this is the given file that we have just added, which contains the entire large API documentation

73
00:04:55,740 --> 00:04:57,100
for the given target.

74
00:04:57,540 --> 00:04:57,900
Okay.

75
00:04:58,420 --> 00:05:01,060
If you want you can give a name to that file as well.

76
00:05:02,140 --> 00:05:03,420
Uh, yeah.

77
00:05:04,180 --> 00:05:04,380
Okay.

78
00:05:04,380 --> 00:05:05,940
You can rename that file as well.

79
00:05:05,940 --> 00:05:07,180
I'll not rename it.

80
00:05:07,620 --> 00:05:08,660
Click on save.

81
00:05:10,540 --> 00:05:12,060
So this will help you in API.

82
00:05:12,100 --> 00:05:12,420
Okay.

83
00:05:12,420 --> 00:05:12,940
Let's go to new.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,280 --> 00:00:16,800
Let's go to API Lama and let's say, can you help me understand the API structure and structure and

2
00:00:17,440 --> 00:00:20,880
give me the endpoints.

3
00:00:25,280 --> 00:00:25,800
Okay.

4
00:00:25,800 --> 00:00:29,560
So now you can see it says the API structure to be RESTful.

5
00:00:29,560 --> 00:00:30,480
That is correct.

6
00:00:30,480 --> 00:00:32,400
The root endpoint is API one.

7
00:00:32,400 --> 00:00:34,520
There are several endpoints for retrieving.

8
00:00:34,520 --> 00:00:39,160
Here is an overview of the main endpoints API version one data ID data.

9
00:00:39,320 --> 00:00:44,320
Now we can ask it to list or list down all of the root endpoints.

10
00:00:44,360 --> 00:00:46,360
Okay, we just don't want the overview.

11
00:00:48,040 --> 00:00:48,960
Excellent.

12
00:00:49,000 --> 00:00:57,960
List down the entire list of end points in list format.

13
00:01:04,350 --> 00:01:07,790
Okay, now it is giving us the list of more endpoints.

14
00:01:08,110 --> 00:01:12,590
Uh, and it is also giving context to that.

15
00:01:12,590 --> 00:01:16,630
For example, API version one data gives retrieves a list of data sets.

16
00:01:16,870 --> 00:01:20,350
Uh, this gives us specific data set based on an ID.

17
00:01:20,590 --> 00:01:23,430
And this gives us a new data set provided with data okay.

18
00:01:23,470 --> 00:01:28,870
So this way it is giving us we can play with this give more prompts that you can ask it to give you

19
00:01:28,870 --> 00:01:30,950
the parameters which are there.

20
00:01:30,950 --> 00:01:38,510
You can ask it to formulate a http uh request that you can utilize directly, maybe in Burp Suite etc.

21
00:01:38,510 --> 00:01:40,630
or you can also do vice versa as well.

22
00:01:40,630 --> 00:01:43,390
So all of those things you can be very creative to do.

23
00:01:43,590 --> 00:01:46,470
This is one very simple example that I've shown.

24
00:01:46,470 --> 00:01:53,990
You can see Bentley highly relies on not only Bentley, but all of the bug bounty programs out there

25
00:01:54,030 --> 00:01:58,190
relies on APIs and their documentation can be found.

26
00:01:58,190 --> 00:01:59,910
For example annotation.

27
00:02:00,030 --> 00:02:06,940
There is a swagger UI documentation for this target for dev connect connect SAP project Dev connect

28
00:02:07,460 --> 00:02:10,100
then QA k dot feature.

29
00:02:10,140 --> 00:02:17,260
Let's go to the second page and there is tons of swagger API documentation available over here for you

30
00:02:17,260 --> 00:02:18,500
to have a look at.

31
00:02:19,100 --> 00:02:23,980
Not only Bentley, maybe let's take another target and let's say.

32
00:02:27,420 --> 00:02:30,260
Snapchat okay.

33
00:02:38,580 --> 00:02:39,820
Swagger okay.

34
00:02:39,820 --> 00:02:43,260
These are the user names I should say swagger UI.

35
00:02:43,380 --> 00:02:47,180
So we are getting specific results okay.

36
00:02:47,220 --> 00:02:49,340
These are names of the profiles.

37
00:02:49,340 --> 00:02:50,540
So that's not correct.

38
00:02:51,620 --> 00:02:58,780
Uh, maybe then we can try to first then find slash v one related endpoints, as we have seen here.

39
00:02:58,780 --> 00:03:05,410
Or maybe swagger endpoints like this for Snapchat or any other target as such, are, I hope, participants,

40
00:03:05,410 --> 00:03:08,010
you have got an idea for the same thing.

41
00:03:08,250 --> 00:03:13,410
How we can expand the knowledge base for the current model.

42
00:03:16,210 --> 00:03:18,250
Uh, yes, we can use this.

43
00:03:20,050 --> 00:03:21,890
Yes we can.

44
00:03:22,050 --> 00:03:22,650
Thank you.

45
00:03:22,850 --> 00:03:23,730
Uh, we can use this.

46
00:03:23,730 --> 00:03:26,610
And we can see there are Snapchat APIs here.

47
00:03:26,650 --> 00:03:32,850
And if you are able to get the JSON of that as well, or maybe the docs, we can directly feed that.

48
00:03:33,530 --> 00:03:34,090
Yes.

49
00:03:35,050 --> 00:03:38,130
There are API documentation.

50
00:03:41,410 --> 00:03:45,450
That we can directly feed it to the model that can help us.

51
00:03:45,850 --> 00:03:46,490
Excellent.

52
00:03:46,650 --> 00:03:48,690
Uh, here we can see the API reference.

53
00:03:48,850 --> 00:03:55,610
We have the API reference of how Orkut, iOS, Android works, etc., etc. we can feed this API documentation

54
00:03:55,810 --> 00:04:00,810
to the model to help us assist in API Pentesting more.

55
00:04:02,290 --> 00:04:02,730
Yes.

56
00:04:03,050 --> 00:04:04,050
Uh, yes.

57
00:04:05,040 --> 00:04:11,080
As one very common question, we need additional storage to run Olama as we are expanding expanding

58
00:04:11,080 --> 00:04:12,360
the number of knowledge bases.

59
00:04:12,360 --> 00:04:13,840
That is absolutely correct.

60
00:04:14,040 --> 00:04:19,360
So make sure that you when you run the container, you have sufficient amount of storage.

61
00:04:19,920 --> 00:04:23,920
I have given currently eight GB Ram to my container.

62
00:04:23,920 --> 00:04:26,240
It is currently utilizing one GB of Ram.

63
00:04:26,520 --> 00:04:29,480
That is very nice and very less CPU.

64
00:04:29,640 --> 00:04:32,840
And make sure that you give the give more storage to the container.

65
00:04:32,840 --> 00:04:34,640
You can increase that from the settings.

66
00:04:34,960 --> 00:04:39,000
You can increase the volume of the container that it is going to use.

67
00:04:40,080 --> 00:04:41,040
Uh, yeah.

68
00:04:41,040 --> 00:04:45,400
So that it does not gives you an error which says out of storage.

69
00:04:45,440 --> 00:04:51,400
Eventually that would happen when you would be increasing more and more, uh, knowledge base.

70
00:04:51,400 --> 00:04:59,760
So make sure you give at least 40 to 50 GB of storage to the given container so that it does not goes

71
00:04:59,760 --> 00:05:01,160
out of memory.

72
00:05:03,000 --> 00:05:03,560
Yes.

73
00:05:04,480 --> 00:05:11,560
Now we are going to do actually more interesting stuff with Lama and enhance its capabilities to see

74
00:05:11,600 --> 00:05:14,480
what more exciting things it can do for us.

75
00:05:15,520 --> 00:05:18,720
So, uh, it's now up to you participants.

76
00:05:18,880 --> 00:05:22,240
It will be your to do task, or you can take it up as a homework.

77
00:05:22,440 --> 00:05:25,240
You need to add a new knowledge base.

78
00:05:25,640 --> 00:05:33,440
Once you add a new knowledge base, you are going to then create a model and then ask specifically questions

79
00:05:33,440 --> 00:05:36,680
to it about pen testing, red teaming, etc..

80
00:05:36,880 --> 00:05:42,120
So I recommend you can take hat tricks as an example.

81
00:05:42,120 --> 00:05:43,520
Knowledge base base.

82
00:05:43,720 --> 00:05:53,120
It is an excellent, uh, you can say cheat sheet based, uh, cheat sheet based techniques or methodologies

83
00:05:53,120 --> 00:06:00,720
that are available over here for all type of test cases that is related to web security, then mobile

84
00:06:00,720 --> 00:06:06,000
security, then uh, infrastructure security, IoT security, etc..

85
00:06:06,000 --> 00:06:09,950
So it's a very nice knowledge base that you can use.

86
00:06:09,950 --> 00:06:11,430
So let me go to pen test.

87
00:06:12,590 --> 00:06:20,510
Uh, and here you can see pen testing methodology or let's go to web test cases networking.

88
00:06:25,270 --> 00:06:30,590
Uh let's go to maybe Clickjacking.

89
00:06:31,430 --> 00:06:31,870
Okay.

90
00:06:31,870 --> 00:06:33,150
So what is Clickjacking.

91
00:06:33,350 --> 00:06:35,030
Basic payload for Clickjacking.

92
00:06:35,070 --> 00:06:36,310
Multi-step payload.

93
00:06:36,350 --> 00:06:37,750
Drag and drop payload.

94
00:06:37,870 --> 00:06:44,550
So this is an excellent, uh, knowledge base for you to train your model.

95
00:06:44,590 --> 00:06:46,190
Okay, so how do you do that?

96
00:06:46,230 --> 00:06:46,910
It's very simple.

97
00:06:46,910 --> 00:06:55,670
You can scrape the entire website, uh, into an HTML form and then provide it to the model to do it.

98
00:06:55,670 --> 00:06:55,870
Okay.

99
00:06:55,870 --> 00:06:59,190
There are various different types of tools available to scrape the website.

100
00:07:00,430 --> 00:07:04,630
Uh, one of the tool that I use is H rack.

101
00:07:04,910 --> 00:07:08,500
So h there are several other bunch of free tools available.

102
00:07:08,500 --> 00:07:13,620
I use this tool to scrape websites, and there are other tools of your choice that you want.

103
00:07:13,620 --> 00:07:14,820
You can use that as well.

104
00:07:15,140 --> 00:07:22,380
It has a GUI for windows, but it does not have a GUI for Linux and Mac OS, so you can use it on terminal.

105
00:07:22,380 --> 00:07:28,180
It is available for all platforms, windows with GUI and for Mac OS and Linux.

106
00:07:28,180 --> 00:07:29,380
It has a CLI.

107
00:07:29,540 --> 00:07:30,820
Now you can use this tool.

108
00:07:30,980 --> 00:07:32,700
Scrape the entire website.

109
00:07:33,220 --> 00:07:37,260
Once you scrape the entire website with all of the techniques, you know what to do.

110
00:07:37,300 --> 00:07:42,540
You need to go and add that entire folder and in the knowledge base over here.

111
00:07:42,540 --> 00:07:51,060
And then you have your in-house ready model with specific knowledge base for all different types of

112
00:07:51,060 --> 00:07:52,820
web security attacks.

113
00:07:52,820 --> 00:07:59,700
And then you can ask as many as questions that you want to the model to give you tips, techniques,

114
00:07:59,700 --> 00:08:03,260
methodologies to perform various different types of test cases.

115
00:08:03,260 --> 00:08:10,370
For any bug, let's say you want to do Clickjacking go ahead to the model, simply say, I want to do

116
00:08:10,410 --> 00:08:11,290
clickjacking.

117
00:08:11,330 --> 00:08:17,250
Give me the script or give me the code, or generate a payload, etc..

118
00:08:17,290 --> 00:08:18,410
Okay, so you can do that.

119
00:08:18,810 --> 00:08:22,050
Uh, the tool name to copy the website is httrack.

120
00:08:25,130 --> 00:08:29,930
Or, and the website that we are going to clone is Hattricks.

121
00:08:30,170 --> 00:08:36,330
It contains, uh, methodology, tips, tricks, techniques in the form of a cheat sheet format.

122
00:08:38,290 --> 00:08:42,610
Uh, I already have this entire website cloned with me locally.

123
00:08:42,730 --> 00:08:49,530
Uh, don't worry about cloning it again if you don't want to, uh, just on my GitHub after the session,

124
00:08:49,770 --> 00:08:53,290
uh, I'll upload it over here and you can download it from there.

125
00:08:53,610 --> 00:08:54,730
Does that sounds good?

126
00:08:58,370 --> 00:08:58,850
Yes.

127
00:08:59,290 --> 00:09:05,250
So you can download the entire, uh, website project and from my GitHub, and then you can feed it

128
00:09:05,250 --> 00:09:09,250
to your, uh, Olama model as a knowledge base.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 11: WAF & Core Concepts

1
00:00:00,840 --> 00:00:03,920
Okay, participants, now let's create.

2
00:00:04,520 --> 00:00:11,080
Let's move forward to the most interesting part of today's session that is going to be firewalls.

3
00:00:11,600 --> 00:00:12,080
Okay.

4
00:00:12,120 --> 00:00:18,360
So as we were discussing about how firewall works, we are going to create a knowledge base around it.

5
00:00:18,360 --> 00:00:23,360
So I've already created a knowledge collection called as firewalls called as WAF.

6
00:00:23,360 --> 00:00:23,800
Sorry.

7
00:00:24,160 --> 00:00:26,160
And in which I'm going to add some data.

8
00:00:30,520 --> 00:00:37,040
Now what kind of data I'm going to add I'm going to add the core rule sets rules over here.

9
00:00:37,040 --> 00:00:42,160
So before we understand the core rule sets what is exactly core rule set.

10
00:00:42,560 --> 00:00:50,440
Core rule set is the project that has been now taken up by OWASp, OWASp Core Rule Set.

11
00:00:50,840 --> 00:00:53,680
So we all know about OWASp Foundation.

12
00:00:53,680 --> 00:01:00,080
And they have this first line of defense core rule set project that is available for the community.

13
00:01:00,280 --> 00:01:10,260
And trust me, 50% plus more than 50% of the world's website utilizes smart security.

14
00:01:10,700 --> 00:01:18,580
So Smart Security is the software and core rule set are the rules or signatures that run that software

15
00:01:19,020 --> 00:01:24,180
and provides web application firewall capabilities.

16
00:01:24,180 --> 00:01:30,780
So the software is more security, but it won't work without the rules.

17
00:01:30,900 --> 00:01:33,820
So rules is the heart of the firewall.

18
00:01:34,140 --> 00:01:35,540
So these are the rules.

19
00:01:35,700 --> 00:01:43,460
The latest version is four point 13.0 which we are going to use which is very recently released.

20
00:01:44,100 --> 00:01:46,740
And this supports attack categories.

21
00:01:46,740 --> 00:01:55,220
So this is a firewall which is going to block SQL injection XSS local file inclusion, remote file inclusion

22
00:01:55,220 --> 00:01:57,820
and other type of attacks as we can see over here.

23
00:01:59,580 --> 00:02:08,560
Now for participants who do not know what a firewall is or web application firewall is, uh, a quick.

24
00:02:11,800 --> 00:02:13,200
Intro about a firewall.

25
00:02:13,440 --> 00:02:18,400
So a web application firewall is a kind of software?

26
00:02:18,440 --> 00:02:23,000
Mostly it is a software, but firewalls can also be hardware appliances.

27
00:02:23,360 --> 00:02:29,120
We are going to focus on software firewall which is more security, and Cloudflare for today's demonstration.

28
00:02:30,040 --> 00:02:35,360
Now assume that this destination server is your banking application.

29
00:02:35,680 --> 00:02:39,000
So this is your bank.

30
00:02:39,680 --> 00:02:42,000
Now there are legitimate users.

31
00:02:42,000 --> 00:02:43,960
So this is the legitimate user one.

32
00:02:43,960 --> 00:02:45,320
Let's say this is Jerry.

33
00:02:45,520 --> 00:02:47,760
This is legitimate user two.

34
00:02:47,960 --> 00:02:50,720
Let's say this user is naman.

35
00:02:50,960 --> 00:02:53,120
So there are two users Jerry and naman.

36
00:02:53,280 --> 00:02:55,440
And this is the attacker.

37
00:02:55,840 --> 00:02:58,120
Let's assume this attacker is Rohit.

38
00:02:58,440 --> 00:03:05,040
Now user one sends a request to the server.

39
00:03:05,200 --> 00:03:08,960
And when the request is going to go to the server it direct.

40
00:03:09,000 --> 00:03:10,600
It does not goes directly.

41
00:03:10,640 --> 00:03:12,990
It has to first go to the firewall.

42
00:03:13,310 --> 00:03:15,830
The firewall is going to read that request.

43
00:03:15,830 --> 00:03:20,990
That is that request containing any harmful payload or any malicious query.

44
00:03:20,990 --> 00:03:22,790
Or is it normal traffic?

45
00:03:23,230 --> 00:03:26,910
The firewall is the one who is going to read it, filter it.

46
00:03:26,910 --> 00:03:34,790
So it is like an we can say a watchman to this building, who is going to read a request and allow that

47
00:03:34,790 --> 00:03:37,630
visitor to reach to the building gate.

48
00:03:37,670 --> 00:03:47,270
If the watchman thinks that this given user or a visitor is not appropriate, or he has bad intentions,

49
00:03:47,270 --> 00:03:51,070
he would be blocked here and he has to go out.

50
00:03:51,070 --> 00:03:54,390
He cannot go inside that building or the destination server.

51
00:03:55,150 --> 00:04:00,150
So let's say user one is allowed to send the traffic to the server because he is legitimate.

52
00:04:00,190 --> 00:04:05,630
Now user two, which is Jerry, is also allowed to send the traffic because he is legitimate.

53
00:04:05,830 --> 00:04:15,030
But when the attacker attempts to send some traffic, let's say this Rohit sends a traffic request or

54
00:04:15,070 --> 00:04:19,730
a login request with a malicious payload like XSS.

55
00:04:19,970 --> 00:04:22,210
So what is the firewall solution is going to do?

56
00:04:22,490 --> 00:04:30,050
It takes the input, reads the input, and then it compares the input with the rules or signatures that

57
00:04:30,050 --> 00:04:30,690
it has.

58
00:04:30,730 --> 00:04:34,290
And it says wait, Rohit, you cannot go forward.

59
00:04:34,290 --> 00:04:36,170
Your request has been dropped.

60
00:04:36,810 --> 00:04:38,210
Rohit makes another request.

61
00:04:38,210 --> 00:04:45,170
Malicious request firewall says hey, this request is also malicious because it matches with our signature

62
00:04:45,170 --> 00:04:46,250
or core rule set.

63
00:04:46,290 --> 00:04:48,010
Your request is dropped.

64
00:04:48,170 --> 00:04:55,130
So none of my request actually goes to the destination server because firewall is protecting the server

65
00:04:55,130 --> 00:04:56,570
and dropping my request.

66
00:04:56,730 --> 00:05:05,410
So in a nutshell, if you can say the firewall checks all inbound requests and takes a decision on it

67
00:05:05,450 --> 00:05:09,730
if that request should be sent forward to the destination server.

68
00:05:09,930 --> 00:05:16,690
If the request is found to be malicious, the firewall is going to drop that request immediately by

69
00:05:16,690 --> 00:05:20,570
blocking the user's attempt or any kind of actions.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:00,760
Now.

2
00:00:00,760 --> 00:00:01,760
Thank you so much.

3
00:00:01,960 --> 00:00:05,520
Now we are going to go to OWASp Modsecurity.

4
00:00:06,560 --> 00:00:13,000
OWASp Modsecurity project is an open source web application firewall engine.

5
00:00:13,240 --> 00:00:19,040
So this is the firewall software, which cannot work without its heart.

6
00:00:19,200 --> 00:00:21,240
And the heart is the rules.

7
00:00:21,760 --> 00:00:24,120
And here are the rules.

8
00:00:24,600 --> 00:00:29,360
Now we are going to go and see the rules of OWASp core rule set.

9
00:00:29,560 --> 00:00:31,960
So I'm going to go and click on the latest rules.

10
00:00:32,280 --> 00:00:33,640
Here are the rules.

11
00:00:34,000 --> 00:00:38,760
And you can see this project has been released three weeks ago only.

12
00:00:38,760 --> 00:00:41,160
And it is very latest very nice.

13
00:00:41,480 --> 00:00:48,600
Now this is the project we can try to understand about this project or these rules, how they how do

14
00:00:48,600 --> 00:00:49,240
they work.

15
00:00:49,440 --> 00:00:55,440
So you have to focus participants in this given folder which is known as rules.

16
00:00:55,920 --> 00:00:57,880
So let's go to the rules folder.

17
00:00:58,360 --> 00:01:04,100
And here participants you can see there are multiple configuration files.

18
00:01:04,260 --> 00:01:12,540
Conf so these configuration files are actually the signatures or rules which will help mod security

19
00:01:12,580 --> 00:01:16,420
take a decision that is either allow or block.

20
00:01:17,020 --> 00:01:26,980
And you can see they also have a number naming convention like request 905 common exceptions, 911 method

21
00:01:26,980 --> 00:01:28,580
enforcement, and so on.

22
00:01:28,780 --> 00:01:35,060
So let's go to one of the configuration file, which is very common common for us to understand foreign

23
00:01:35,060 --> 00:01:36,860
common attack which is XSS okay.

24
00:01:37,340 --> 00:01:42,900
So request 941 application attack XSS dot conf.

25
00:01:43,260 --> 00:01:46,260
So let's go ahead and understand this configuration file.

26
00:01:46,820 --> 00:01:54,420
Now I'm sure that you might not be able to in the first go or the first attempt, understand the entire

27
00:01:54,420 --> 00:01:54,820
file.

28
00:01:54,820 --> 00:02:00,700
If you have not seen this earlier, but I still want you to just have a look at it.

29
00:02:01,940 --> 00:02:03,570
So what does it actually do?

30
00:02:03,890 --> 00:02:06,770
It basically detects excessive excesses.

31
00:02:07,010 --> 00:02:10,090
So library injection excesses detection module.

32
00:02:10,690 --> 00:02:16,610
And it is going to check the request cookies and other part.

33
00:02:16,770 --> 00:02:24,490
And it will try to see if excess has been detected in anywhere maybe in user agent arguments headers

34
00:02:24,530 --> 00:02:25,330
cookies.

35
00:02:25,650 --> 00:02:31,330
And it is going to give a message which says excess attack detected via Lib injection.

36
00:02:31,370 --> 00:02:31,770
Okay.

37
00:02:32,130 --> 00:02:39,410
Let's go forward script base excess vectors like script alert one should be blocked if they are passed

38
00:02:39,410 --> 00:02:48,010
in cookies, cookie names, file names, file names, file headers, user agent, request header, referrer

39
00:02:48,050 --> 00:02:49,930
argument name, or anywhere.

40
00:02:50,290 --> 00:02:57,730
And once this is blocked, you will get a message XSS filter category one script tag vector blocked.

41
00:02:57,770 --> 00:03:00,730
Now similarly we can go to filter category three.

42
00:03:01,050 --> 00:03:04,870
It will say that the user should be blocked based on a regex pattern.

43
00:03:05,110 --> 00:03:07,110
And you can see payloads over here.

44
00:03:07,110 --> 00:03:10,510
So let me show you some payloads.

45
00:03:10,510 --> 00:03:17,750
So this is the most common, uh, detection tags that are most common direct HTML injection points in

46
00:03:17,750 --> 00:03:18,390
the file.

47
00:03:18,550 --> 00:03:24,030
So for example, if you use a payload like image source equals to x onerror equals to anything.

48
00:03:24,230 --> 00:03:28,950
Alert one, confirm one prompt one alert to confirm two prompt two.

49
00:03:28,990 --> 00:03:37,070
You will be blocked because this is a filter and a regex pattern in the file that blocks your attempt.

50
00:03:37,070 --> 00:03:43,670
You can see there are more payloads body onload embed source then iframe payloads and other payloads

51
00:03:43,670 --> 00:03:44,070
here.

52
00:03:44,750 --> 00:03:51,270
So I hope participants are able to correlate this and understand how this configuration file contains

53
00:03:51,270 --> 00:04:01,150
various regex patterns and commonly used XSS payloads and HTML injection points based on which whenever

54
00:04:01,150 --> 00:04:04,550
you give an input to a website, your input will be blocked.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,320 --> 00:00:01,000
Yes.

2
00:00:01,000 --> 00:00:10,480
So now what we would do is let's try to see this practically and onto a live application of how this

3
00:00:10,480 --> 00:00:12,160
core rule set would behave.

4
00:00:12,480 --> 00:00:20,880
So to save time from the session, I have already set this up onto one of the web application and practically.

5
00:00:20,880 --> 00:00:25,240
So I want to show you how does it actually behave in a live environment?

6
00:00:25,240 --> 00:00:25,640
Okay.

7
00:00:25,680 --> 00:00:34,400
I'll send you the instruction or the link to the article from official source of how you can set up

8
00:00:34,680 --> 00:00:40,920
OWASp Modsecurity on any website or web application for your practice and research.

9
00:00:41,160 --> 00:00:41,640
Okay.

10
00:00:41,680 --> 00:00:47,480
It will not take more than ten minutes, but just to save time, I've already done the setup, so I

11
00:00:47,520 --> 00:00:52,400
have done the setup into my Linux machine, so I'm going to power that on.

12
00:00:55,400 --> 00:00:58,960
The setup is very, very simple.

13
00:01:00,620 --> 00:01:03,860
Okay, so now my machine has started successfully.

14
00:01:05,420 --> 00:01:07,260
Okay, just a second.

15
00:02:25,720 --> 00:02:26,160
Okay.

16
00:02:35,000 --> 00:02:35,480
Okay.

17
00:02:35,520 --> 00:02:36,400
Participants.

18
00:02:36,640 --> 00:02:38,000
You can see over here.

19
00:02:38,280 --> 00:02:42,960
I am currently running a web server, which is Apache.

20
00:02:44,520 --> 00:02:46,360
So I'll go into that directory.

21
00:02:46,880 --> 00:02:53,560
And here you can see that index dot HTML file is there which is currently loaded over here.

22
00:02:53,800 --> 00:02:56,240
Let me show you the content of index dot HTML.

23
00:02:56,900 --> 00:02:59,660
so you can see it contains this works message.

24
00:02:59,860 --> 00:03:01,700
And the same has been loaded over here.

25
00:03:01,700 --> 00:03:05,260
So I will refresh this to show you that the website is currently running.

26
00:03:05,660 --> 00:03:11,460
Now as I said, I have already set it up mod security onto this.

27
00:03:11,700 --> 00:03:16,260
How do I know which domain or which target contains which firewall?

28
00:03:16,420 --> 00:03:18,180
So for that we have a tool.

29
00:03:18,420 --> 00:03:21,380
So we are going to use a tool which is WAF.

30
00:03:21,420 --> 00:03:21,980
Woof.

31
00:03:22,460 --> 00:03:30,260
Woof woof is a tool which is actually pre-installed or comes pre-installed into Kali Linux system.

32
00:03:30,820 --> 00:03:36,300
So I'm going to say woof and send a request to the local host website.

33
00:03:36,980 --> 00:03:40,140
And once we do that we can see this sign.

34
00:03:40,180 --> 00:03:44,460
This site is behind a WAF or some sort of security solution.

35
00:03:44,620 --> 00:03:51,980
It did not give the name Mod security, but it still told us that it is behind a security solution because

36
00:03:51,980 --> 00:03:56,880
the reason is that the server returns a different response code when the attack string is used.

37
00:03:56,920 --> 00:04:06,560
Okay, now I can send a request to maybe cloudflare.com and okay, my internet is down just a sec.

38
00:04:33,160 --> 00:04:34,320
Restart the machine.

39
00:04:56,060 --> 00:04:56,740
Nice.

40
00:04:57,020 --> 00:04:57,820
Let's see.

41
00:04:57,860 --> 00:04:58,060
Yeah.

42
00:04:58,100 --> 00:04:59,740
Now we have the internet connectivity.

43
00:05:00,020 --> 00:05:05,340
So let's send a request to Cloudflare and we can see the site Cloudflare is behind Cloudflare WAF.

44
00:05:05,740 --> 00:05:10,940
Obviously these Cloudflare website is behind their own security solution.

45
00:05:10,980 --> 00:05:11,340
Okay.

46
00:05:11,540 --> 00:05:15,540
Now let me send a request to zing.

47
00:05:16,140 --> 00:05:17,980
Com and let's hit send.

48
00:05:18,620 --> 00:05:19,660
Let's hit enter.

49
00:05:19,780 --> 00:05:22,460
And we can see it is also behind some kind of security solution.

50
00:05:22,460 --> 00:05:24,260
But it did not identify which is it.

51
00:05:24,460 --> 00:05:28,780
Now let's send a request to imperva.com.

52
00:05:34,660 --> 00:05:38,660
So you can see this is behind Incapsula Imperva WAF.

53
00:05:39,140 --> 00:05:39,940
Very nice.

54
00:05:39,940 --> 00:05:46,140
Now let's send a request to rectify and see that this website is behind which with which firewall.

55
00:05:56,440 --> 00:05:56,920
Okay.

56
00:05:56,960 --> 00:05:57,480
Sorry.

57
00:05:57,880 --> 00:05:59,000
Https.

58
00:06:20,520 --> 00:06:20,880
Mm.

59
00:06:24,080 --> 00:06:25,560
Let me run it once again.

60
00:06:29,040 --> 00:06:31,640
Ideally, it should be able to identify it for us.

61
00:06:31,840 --> 00:06:37,200
Uh, our website is behind Cloudflare, so it should give us the response that it is behind Cloudflare.

62
00:06:40,200 --> 00:06:41,760
Something went wrong.

63
00:06:41,760 --> 00:06:45,160
I think the website is resetting the connection.

64
00:06:45,800 --> 00:06:47,040
Uh, that has been sent by.

65
00:06:47,760 --> 00:06:48,560
No problem.

66
00:06:48,800 --> 00:06:53,420
Uh, but the website is behind Cloudflare and you should receive a response like this whenever you try

67
00:06:53,420 --> 00:06:54,900
to scan it later on, maybe.

68
00:06:54,940 --> 00:06:59,100
And I'll also show you from Cloudflare dashboard that activation is protected over there.

69
00:06:59,140 --> 00:07:00,740
Anyways, let's come back here.

70
00:07:00,980 --> 00:07:08,420
And now we can see when we attempt to send a request here, let's say a malicious payload.

71
00:07:08,740 --> 00:07:13,540
This is a very common payload script alert one script tag close.

72
00:07:15,980 --> 00:07:16,340
Yes.

73
00:07:16,340 --> 00:07:17,180
Participants.

74
00:07:17,180 --> 00:07:18,940
This is the very common payload.

75
00:07:22,700 --> 00:07:23,220
Yes.

76
00:07:23,420 --> 00:07:28,540
And in our documentation this payload is listed.

77
00:07:31,700 --> 00:07:34,380
Here okay.

78
00:07:34,500 --> 00:07:39,460
So we are definitely going to get blocked whenever we are going to run script alert.

79
00:07:39,940 --> 00:07:40,940
Uh payload okay.

80
00:07:40,980 --> 00:07:42,460
So let us see the response.

81
00:07:42,460 --> 00:07:43,860
So I'm going to hit enter.

82
00:07:44,980 --> 00:07:46,260
And did you see that.

83
00:07:46,260 --> 00:07:46,980
Forbidden.

84
00:07:47,460 --> 00:07:50,350
You don't have permission to access this resource and we are blocked.

85
00:07:50,630 --> 00:07:56,150
Participants I also want to show you that we have got blocked because of the.

86
00:07:59,190 --> 00:07:59,750
Request.

87
00:07:59,790 --> 00:08:05,070
Nine for one application attack access dot configuration file only.

88
00:08:05,070 --> 00:08:08,350
So to do that let me show you the logs of this service okay.

89
00:08:08,550 --> 00:08:10,870
So to see the logs I'm going to say tail.

90
00:08:11,510 --> 00:08:20,990
Tail is to see the last ten lines f uh to read in real time or stream the output of the file which is

91
00:08:21,030 --> 00:08:22,910
var log apache2 error dot log.

92
00:08:22,910 --> 00:08:23,830
Let's hit enter.

93
00:08:24,230 --> 00:08:29,470
And here you can see all the logs of the mod security firewall participants.

94
00:08:29,470 --> 00:08:35,630
If you have a closer look at the mod security firewall rule set, then you can see currently here,

95
00:08:36,110 --> 00:08:42,870
uh, if you see exactly it's here in the argument, you can say x is the parameter.

96
00:08:42,910 --> 00:08:43,870
Yes, that is correct.

97
00:08:43,870 --> 00:08:50,570
We can see x is the parameter here and the payload is script alert one script tag close that was added.

98
00:08:50,770 --> 00:08:53,010
That is also absolutely correct.

99
00:08:53,010 --> 00:08:55,010
And why did we get blocked?

100
00:08:55,050 --> 00:08:59,250
We got blocked because of the file which is inside, etc..

101
00:08:59,370 --> 00:09:07,650
Apache2 Modsecurity core rule set rules request number nine for one application attack XSS conf.

102
00:09:07,970 --> 00:09:16,730
This is exactly the same attack configuration file that we have read over here, and which tells you

103
00:09:16,850 --> 00:09:24,490
that you that the firewall should block the attempt of any user who is attempting to do the XSS attack.

104
00:09:24,530 --> 00:09:31,010
Let's change this payload and instead of alert one, let me say row, row, hit and hit enter and let

105
00:09:31,010 --> 00:09:32,010
us see how does it behave.

106
00:09:32,010 --> 00:09:33,610
Okay, let's hit enter.

107
00:09:34,010 --> 00:09:34,970
We got blocked.

108
00:09:35,290 --> 00:09:38,010
Uh, that was obvious that we would be blocked.

109
00:09:38,050 --> 00:09:39,730
Now let's examine the logs.

110
00:09:40,170 --> 00:09:43,290
So arguments script alert row.

111
00:09:43,330 --> 00:09:44,850
Hit script tag close.

112
00:09:45,130 --> 00:09:46,350
This has been blocked.

113
00:09:46,390 --> 00:09:47,030
Severity.

114
00:09:47,070 --> 00:09:49,750
Critical as per OWASp rule sets.

115
00:09:49,790 --> 00:09:50,710
Core rule set.

116
00:09:50,870 --> 00:09:52,910
And this is the rule that has got triggered.

117
00:09:53,950 --> 00:09:54,390
Okay.

118
00:09:54,390 --> 00:10:02,270
So we got a concrete understanding about how we are getting blocked continuously by the Mod security

119
00:10:02,310 --> 00:10:03,070
firewall.

120
00:10:03,270 --> 00:10:08,670
For any payload that we attempt or try to do you will be blocked participants.

121
00:10:09,430 --> 00:10:13,870
Let's try to change the script tag to another tag.

122
00:10:14,030 --> 00:10:15,310
Let us say image tag.

123
00:10:15,310 --> 00:10:20,550
So I will say image source equals to x on error equals to alert one.

124
00:10:22,030 --> 00:10:25,270
Okay let's try to use this payload over here.

125
00:10:25,270 --> 00:10:26,950
And let's see what is the response.

126
00:10:27,190 --> 00:10:29,150
I will remove this paste it.

127
00:10:29,750 --> 00:10:33,110
But yes participants you are right.

128
00:10:33,110 --> 00:10:34,430
We have got blocked.

129
00:10:35,150 --> 00:10:36,910
Let us see the logs.

130
00:10:37,070 --> 00:10:44,350
And in the logs you can see image source equals to x onerror found within the arguments.

131
00:10:45,250 --> 00:10:47,250
And here is the exact payload.

132
00:10:47,530 --> 00:10:49,010
And we have got blocked.

133
00:10:49,050 --> 00:10:49,450
Why?

134
00:10:49,610 --> 00:10:52,330
Because of the same configuration file.

135
00:10:52,370 --> 00:10:52,850
Okay.

136
00:10:53,010 --> 00:10:55,810
So now what should we do instead of alert?

137
00:10:55,810 --> 00:10:57,050
Let's try to say prompt.

138
00:10:58,210 --> 00:11:02,090
We are trying to change the event handler okay.

139
00:11:02,290 --> 00:11:09,810
So if it if we try to change the event handler from onerror to onload and the function from prompt to

140
00:11:09,850 --> 00:11:12,970
alert, let's try to be a little bit more creative.

141
00:11:13,450 --> 00:11:14,410
We got blocked.

142
00:11:15,010 --> 00:11:17,330
We can examine the logs here as well.

143
00:11:17,690 --> 00:11:23,210
We have tried a new event handler onload and a new function instead of alert.

144
00:11:23,210 --> 00:11:24,410
Let us try prompt.

145
00:11:25,290 --> 00:11:28,450
We got blocked again.

146
00:11:28,730 --> 00:11:30,210
Instead of prompt.

147
00:11:31,370 --> 00:11:36,970
Uh, we can try another payload which is confirmed and we got blocked again.

148
00:11:37,450 --> 00:11:37,890
Alert.

149
00:11:37,890 --> 00:11:38,290
Prompt.

150
00:11:38,290 --> 00:11:39,730
Confirm or got blocked.

151
00:11:43,670 --> 00:11:46,470
Yes, you're absolutely right.

152
00:11:46,910 --> 00:11:52,030
Ah, it also shows that line number 199, because of which we are getting blocked.

153
00:11:52,070 --> 00:11:53,390
You're absolutely right.

154
00:11:54,190 --> 00:11:54,830
Ah, yes.

155
00:11:55,110 --> 00:12:02,590
So yes, definitely we can check any, any other as well instead of nine, four, one.

156
00:12:02,870 --> 00:12:04,550
Uh, we can attack.

157
00:12:04,550 --> 00:12:07,150
We can perform another attack as well and see the same.

158
00:12:07,190 --> 00:12:08,630
I'll do that in a moment.

159
00:12:08,670 --> 00:12:15,950
Uh, before that, let's, uh, copy paste a payload that one of the user has shared in the chat to

160
00:12:15,950 --> 00:12:16,790
see if that works.

161
00:12:16,830 --> 00:12:17,230
Okay.

162
00:12:17,390 --> 00:12:21,510
Image slash source slash x on error equals to print.

163
00:12:21,670 --> 00:12:22,990
And we got blocked.

164
00:12:23,270 --> 00:12:25,190
Unfortunately it did not work.

165
00:12:26,190 --> 00:12:29,190
And we are again blocked over here.

166
00:12:29,430 --> 00:12:29,870
Okay.

167
00:12:30,470 --> 00:12:30,950
Now.

168
00:12:33,030 --> 00:12:33,470
Yeah.

169
00:12:33,510 --> 00:12:40,030
Now let's try to send another payload over here and see if it checks another configuration file.

170
00:12:40,310 --> 00:12:43,770
So Let's try to maybe do a SQL injection.

171
00:12:44,050 --> 00:12:48,410
So file number 942 is the file that it.

172
00:12:48,450 --> 00:12:51,170
It should check for SQL injection.

173
00:12:51,170 --> 00:12:54,490
So I'm going to take one of the payload from here itself.

174
00:12:54,890 --> 00:12:56,370
Um let's say.

175
00:12:58,690 --> 00:12:59,530
Single quote.

176
00:13:02,930 --> 00:13:08,250
One single quote or single quote.

177
00:13:09,330 --> 00:13:12,970
One single quote equals single quote.

178
00:13:13,010 --> 00:13:15,970
One we got blocked.

179
00:13:16,410 --> 00:13:27,210
Uh, it's a very simple and common access, uh, query payload to do, uh, balance balance out and

180
00:13:27,210 --> 00:13:28,890
do authentication bypass.

181
00:13:29,130 --> 00:13:36,130
And here we can see uh request number 942 application attack SQL injection dot conf file has triggered

182
00:13:36,370 --> 00:13:38,370
the argument with this payload.

183
00:13:38,370 --> 00:13:39,970
And we are currently blocked.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,840 --> 00:00:12,080
One of the world's biggest firewall provider has is effectively working correctly, and it is blocking

2
00:00:12,080 --> 00:00:14,760
all our attempts that we make over here.

3
00:00:15,160 --> 00:00:26,560
Now we are going to see how Obama can help us circumvent this firewall and generate a bypass for us.

4
00:00:26,880 --> 00:00:33,920
Okay, so for doing that, we need to first provide some knowledge to the model and then see if that

5
00:00:33,920 --> 00:00:35,080
works out for us.

6
00:00:35,120 --> 00:00:35,560
Okay.

7
00:00:35,880 --> 00:00:43,400
So I'm going to go back and we are going to do a very boring job now.

8
00:00:43,520 --> 00:00:50,320
And that is reading documentation about how JavaScript web APIs work.

9
00:00:50,360 --> 00:00:50,800
Okay.

10
00:00:51,040 --> 00:00:57,240
Although we would not really read it, but we would just supply the entire documentation of how web

11
00:00:57,240 --> 00:01:01,560
APIs and context of JavaScript works and provide it to the Lama as knowledge base.

12
00:01:01,600 --> 00:01:01,960
Okay.

13
00:01:02,210 --> 00:01:09,570
So I'm going to go to MDN docs and read the web API documentation.

14
00:01:10,890 --> 00:01:11,410
Okay.

15
00:01:11,410 --> 00:01:16,250
So here is the web API documentation, the entire specification of how it works.

16
00:01:17,730 --> 00:01:21,970
Uh we are more interested towards specific handlers.

17
00:01:21,970 --> 00:01:23,650
So I'll just say prompt for now.

18
00:01:24,090 --> 00:01:25,130
Prompt method.

19
00:01:31,850 --> 00:01:32,410
Okay.

20
00:01:32,410 --> 00:01:35,330
So uh, why did I choose prompt method.

21
00:01:35,530 --> 00:01:38,490
Uh to just come to the web API windows.

22
00:01:38,490 --> 00:01:40,970
We are going to use multiple windows from here.

23
00:01:41,010 --> 00:01:46,970
Now to obtain or to generate a payload that will help us bypass the given firewall.

24
00:01:47,010 --> 00:01:47,450
Okay.

25
00:01:47,490 --> 00:01:53,130
So in the window section you can see different types of methods available for us.

26
00:01:53,450 --> 00:01:57,250
Uh I'll simply jump to the method which is alert.

27
00:01:57,530 --> 00:01:58,090
Yeah.

28
00:01:58,090 --> 00:01:59,890
So here you can see an alert method.

29
00:01:59,890 --> 00:02:01,330
Let me go and click on it.

30
00:02:02,690 --> 00:02:04,010
So what does alert do?

31
00:02:04,170 --> 00:02:08,490
Because our payload contains an alert script alert.

32
00:02:08,650 --> 00:02:12,290
So we are going to use one of the window method that is alert.

33
00:02:12,330 --> 00:02:16,330
Then we have confirm, as you can see over here that we also tried confirm.

34
00:02:16,490 --> 00:02:17,890
So what does confirm do.

35
00:02:18,050 --> 00:02:24,770
It basically uh instructs the browser to display a dialog with an optional message that we want confirm

36
00:02:24,770 --> 00:02:27,130
message will give a message that you want.

37
00:02:27,530 --> 00:02:28,250
Very nice.

38
00:02:28,570 --> 00:02:31,170
Now we also saw alert.

39
00:02:33,010 --> 00:02:33,530
Sorry.

40
00:02:33,730 --> 00:02:37,330
Confirm and prompt.

41
00:02:38,330 --> 00:02:39,890
Let's go and see what it's prompt.

42
00:02:40,930 --> 00:02:41,890
So here is prompt.

43
00:02:41,890 --> 00:02:43,810
And we can read about prompt as well.

44
00:02:43,970 --> 00:02:48,010
So window dot prompt instructs the browser to use a dialog with optional message that we want.

45
00:02:48,050 --> 00:02:50,730
And this is the syntax of using it in JavaScript.

46
00:02:50,770 --> 00:02:51,490
Excellent.

47
00:02:51,490 --> 00:02:57,610
So here are some of the documentation for how web APIs Windows standard works.

48
00:02:57,970 --> 00:03:00,450
And trust me participants.

49
00:03:00,650 --> 00:03:02,090
This is a gold mine.

50
00:03:02,650 --> 00:03:08,860
Although these are just web standards, but these are gold mines for us to understand about various

51
00:03:08,860 --> 00:03:11,500
different things, that is going to be important for us.

52
00:03:11,660 --> 00:03:13,020
So what do we do now?

53
00:03:13,460 --> 00:03:23,980
Uh, we are going to save this given page with all of the information that we have currently, and we

54
00:03:23,980 --> 00:03:29,460
are going to, uh, give it as a knowledge base to llama.

55
00:03:29,460 --> 00:03:31,300
So I'm going to save this current page.

56
00:03:31,300 --> 00:03:33,540
You can also scrape it with HDD rack.

57
00:03:33,820 --> 00:03:35,980
And I'm going to just save this as PDF.

58
00:03:38,820 --> 00:03:44,500
Or you can save it as HTML as well save as PDF.

59
00:03:44,540 --> 00:03:46,140
Yes 26 pages.

60
00:03:47,300 --> 00:03:50,260
Save uh window web APIs.

61
00:03:50,300 --> 00:03:50,820
Million.

62
00:03:50,820 --> 00:03:51,380
Right.

63
00:03:51,780 --> 00:03:53,980
Let's save it to WAF rules.

64
00:03:54,100 --> 00:03:56,260
I've created a folder called as WAF rules.

65
00:03:56,620 --> 00:03:57,540
Let's save this.

66
00:03:58,140 --> 00:03:58,660
Nice.

67
00:03:58,700 --> 00:03:59,500
This is saved.

68
00:03:59,540 --> 00:04:03,740
You can scrape it to have more web APIs saved over there as well.

69
00:04:04,060 --> 00:04:05,500
Uh, you can do that as well.

70
00:04:05,740 --> 00:04:14,060
As of now, I would have done is I've created a folder called as WAF rules, which contains, uh, the

71
00:04:14,100 --> 00:04:17,340
documentation that we just downloaded available here.

72
00:04:17,340 --> 00:04:18,100
And participants.

73
00:04:18,100 --> 00:04:22,420
What I have also done is I have downloaded the rules as well from GitHub.

74
00:04:22,540 --> 00:04:28,580
So these rules are actually, uh, where the rules go.

75
00:04:28,620 --> 00:04:29,020
Yeah.

76
00:04:29,340 --> 00:04:32,140
These are the, these rules available over here.

77
00:04:32,140 --> 00:04:33,620
So I have downloaded them.

78
00:04:33,620 --> 00:04:34,420
How to download it.

79
00:04:34,420 --> 00:04:35,940
Simply go to Core Rule set.

80
00:04:36,340 --> 00:04:38,540
Click on code and click on Download zip.

81
00:04:38,940 --> 00:04:41,700
So once you download zip the folder will be downloaded.

82
00:04:41,700 --> 00:04:46,860
And I have just unzipped it and I have deleted all other files because I only wanted rules folder.

83
00:04:47,100 --> 00:04:52,020
So the rules folder contains all the files available over here.

84
00:04:52,020 --> 00:05:01,500
So request 941 application attack on application attack access dot conf can be read.

85
00:05:01,500 --> 00:05:03,420
This is the same configuration file.

86
00:05:03,420 --> 00:05:07,950
Nothing else okay so what we have done, we have created a folder.

87
00:05:07,950 --> 00:05:14,230
And the folder basically contains the web API documents as well as the core rule sets.

88
00:05:14,270 --> 00:05:18,870
Now I'm going to provide this to the llama model.

89
00:05:18,870 --> 00:05:20,950
So let's go to the model.

90
00:05:21,670 --> 00:05:26,590
And in the web knowledge base we are going to provide.

91
00:05:28,150 --> 00:05:28,430
Yeah.

92
00:05:28,430 --> 00:05:29,710
So the rules are already there.

93
00:05:29,710 --> 00:05:31,950
It has loaded those rules already.

94
00:05:32,430 --> 00:05:32,750
Uh.

95
00:05:32,750 --> 00:05:38,270
And it should also automatically load this because it is in the same folder.

96
00:05:38,630 --> 00:05:44,430
If it doesn't drag and drop this and it should be able to load it, you can see over here the file is

97
00:05:44,430 --> 00:05:45,830
added automatically.

98
00:05:45,830 --> 00:05:47,590
Windows web API is named.

99
00:05:47,590 --> 00:05:48,590
And click on that.

100
00:05:48,590 --> 00:05:52,630
And it will be loaded and converted to its format that it want.

101
00:05:53,710 --> 00:05:54,270
Nice.

102
00:05:54,430 --> 00:05:58,870
So we have our knowledge base setup which is Vaf which contains WAF bypass techniques.

103
00:05:58,870 --> 00:06:00,230
Let's go to workspace.

104
00:06:00,590 --> 00:06:02,550
Let's go to models.

105
00:06:02,550 --> 00:06:10,310
Let's click on plus and set up a new model to use the previous knowledge and then we'll see some magic

106
00:06:10,310 --> 00:06:10,870
happening.

107
00:06:11,830 --> 00:06:13,350
Okay, let's wait for this.

108
00:06:13,990 --> 00:06:15,310
Let's give it a few seconds.

109
00:06:15,310 --> 00:06:20,670
Let's give the model as WAF, bypass or Modsec.

110
00:06:22,070 --> 00:06:23,350
Select a base model.

111
00:06:23,510 --> 00:06:25,910
Choose Lambda three or whatever you want.

112
00:06:25,950 --> 00:06:27,750
This time I'm going to choose mixed rule.

113
00:06:30,710 --> 00:06:32,030
Uh, what is the difference?

114
00:06:32,030 --> 00:06:36,990
Mixed rule is trained on a larger, uh, knowledge base.

115
00:06:36,990 --> 00:06:41,110
So mixed rule by default I think has 40 billion parameters.

116
00:06:41,110 --> 00:06:47,590
So if you choose mixed rule it is going to consume more system requirements, more Ram, more storage.

117
00:06:47,630 --> 00:06:48,030
Okay.

118
00:06:48,070 --> 00:06:49,310
That's the only difference.

119
00:06:49,750 --> 00:06:52,950
Uh, it has been trained on a large number of parameters.

120
00:06:53,510 --> 00:06:54,670
Visibility public.

121
00:06:56,790 --> 00:06:58,950
Select knowledge WAF.

122
00:07:00,990 --> 00:07:04,150
If you want to add some tools and other things, you can do all of those here.

123
00:07:04,150 --> 00:07:05,110
I'm not going to do that.

124
00:07:05,110 --> 00:07:07,470
I'm going to just click save and create.

125
00:07:07,830 --> 00:07:08,630
Excellent.

126
00:07:08,670 --> 00:07:08,950
Now let's.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,040 --> 00:00:01,040
Go to new chart.

2
00:00:01,480 --> 00:00:02,960
Let's choose the new model.

3
00:00:04,160 --> 00:00:07,040
And our model is here for us.

4
00:00:07,520 --> 00:00:08,200
Excellent.

5
00:00:08,240 --> 00:00:14,080
Now, uh, we are going to ask questions to the model, and it is going to give us some very, very

6
00:00:14,080 --> 00:00:16,160
interesting answers.

7
00:00:16,160 --> 00:00:18,960
That is going to be very, very helpful to us.

8
00:00:19,360 --> 00:00:19,600
Okay.

9
00:00:19,640 --> 00:00:28,560
So let's start with what are some of the common web API methods?

10
00:00:30,680 --> 00:00:30,920
Uh.

11
00:00:33,280 --> 00:00:33,840
Okay.

12
00:00:35,040 --> 00:00:37,080
There is an error with my Docker.

13
00:00:39,400 --> 00:00:40,000
Wait.

14
00:00:40,040 --> 00:00:41,320
Something went wrong.

15
00:00:45,360 --> 00:00:45,720
Okay.

16
00:00:45,720 --> 00:00:47,280
Let me just try that once again.

17
00:00:50,200 --> 00:00:51,760
There was a response error.

18
00:00:53,120 --> 00:00:55,760
Let me just reload the web UI.

19
00:01:02,710 --> 00:01:03,470
Container.

20
00:01:08,910 --> 00:01:09,910
What is wrong?

21
00:01:12,910 --> 00:01:13,590
Time out.

22
00:01:13,630 --> 00:01:14,510
We got a timeout.

23
00:01:14,550 --> 00:01:15,350
Not sure why.

24
00:01:16,150 --> 00:01:19,070
Anyways, uh, it started again.

25
00:01:20,310 --> 00:01:22,230
What are some of the common web API methods?

26
00:01:22,230 --> 00:01:23,510
It is now running this.

27
00:01:23,510 --> 00:01:24,310
Let's wait.

28
00:01:26,990 --> 00:01:28,630
Yes, it is running.

29
00:01:28,670 --> 00:01:30,870
It has started that chat for us.

30
00:01:31,350 --> 00:01:33,070
Same chat in the.

31
00:01:33,110 --> 00:01:36,150
So I'm just seeing the logs of the container.

32
00:01:36,190 --> 00:01:37,150
What went wrong?

33
00:01:37,470 --> 00:01:38,990
It just said timeout.

34
00:01:39,030 --> 00:01:41,190
Not sure why, but yeah, it is running the task.

35
00:01:41,390 --> 00:01:42,510
Let's wait for this.

36
00:02:01,020 --> 00:02:01,420
Mm.

37
00:02:04,860 --> 00:02:07,100
Okay, let me just send one more.

38
00:02:07,700 --> 00:02:12,020
Uh, there is some thing wrong with my container.

39
00:02:12,580 --> 00:02:13,420
Just a second.

40
00:02:13,700 --> 00:02:15,340
Let me just stop this.

41
00:02:17,500 --> 00:02:19,940
And start it once again.

42
00:02:50,020 --> 00:02:50,460
Yeah.

43
00:02:50,740 --> 00:02:51,820
Now it is started.

44
00:02:52,580 --> 00:02:54,540
Now let's ask the same question.

45
00:02:58,450 --> 00:02:59,050
Oops.

46
00:03:06,170 --> 00:03:10,050
Uh, I think, uh, this is an unexpected error.

47
00:03:10,050 --> 00:03:14,410
I'm not sure why it is giving us an error.

48
00:03:15,290 --> 00:03:16,890
This was not happening earlier.

49
00:03:17,210 --> 00:03:18,970
Maybe I'll try to fix this error.

50
00:03:20,730 --> 00:03:25,490
Uh, once again, let me just attempt to restart the docker.

51
00:03:25,730 --> 00:03:30,890
I think we are doing a lot of, uh, activities, which are.

52
00:03:33,810 --> 00:03:37,490
More than expected for the container.

53
00:03:37,490 --> 00:03:38,810
Hence it is going down.

54
00:03:49,570 --> 00:03:55,640
It is not able to take our pentesting attempts that we are making.

55
00:03:55,640 --> 00:03:59,720
So yeah, let's say hi first.

56
00:04:01,200 --> 00:04:01,640
Okay.

57
00:04:01,680 --> 00:04:04,040
I think something is wrong with the container.

58
00:04:07,680 --> 00:04:11,200
Uh, I will try to fix this.

59
00:04:11,920 --> 00:04:13,680
Uh, so let's do one thing.

60
00:04:13,680 --> 00:04:16,240
Let's go for a quick five minute.

61
00:04:17,560 --> 00:04:20,720
Uh, yes, I, I, I think something is going wrong.

62
00:04:22,280 --> 00:04:23,640
Something is going wrong.

63
00:04:28,000 --> 00:04:29,360
Uh, okay, I got it.

64
00:04:29,400 --> 00:04:30,120
What is wrong?

65
00:04:30,480 --> 00:04:36,480
Uh, as we have choosed the mixture model, I guess, uh, as it is trained on 47 billion parameters,

66
00:04:36,480 --> 00:04:40,840
it is taking high level of, uh, CPU usage and memory.

67
00:04:41,040 --> 00:04:47,200
And my container is currently running two models, which is miss uh llama and mixture, because of which

68
00:04:47,240 --> 00:04:49,520
it is going offline again and again.

69
00:04:49,560 --> 00:04:50,440
Uh, I guess you are right.

70
00:04:51,080 --> 00:04:56,950
So what we'll do is we'll delete this and we'll again set up a new, uh, model.

71
00:04:56,950 --> 00:04:59,230
But this time we don't use the mistral.

72
00:04:59,910 --> 00:05:05,390
The mistral is consuming full memory, and it is crashing our Docker container.

73
00:05:06,110 --> 00:05:09,230
Okay, so let me just again create the model.

74
00:05:21,990 --> 00:05:23,110
Yeah, you are right.

75
00:05:23,510 --> 00:05:25,470
Uh, we are on the peak of the.

76
00:05:26,150 --> 00:05:28,910
We are using the peak of this consumption, I guess.

77
00:05:41,590 --> 00:05:45,870
Okay, let me just start with again the smaller model.

78
00:05:46,630 --> 00:05:50,630
Uh, by pass mod sack.

79
00:05:51,110 --> 00:05:52,590
Choose llama.

80
00:05:52,590 --> 00:05:52,620
Lama.

81
00:05:55,980 --> 00:05:59,700
Public knowledge graph.

82
00:06:00,940 --> 00:06:01,460
Save.

83
00:06:02,300 --> 00:06:02,820
Awesome.

84
00:06:03,100 --> 00:06:05,580
Then let's go to New Chat.

85
00:06:05,820 --> 00:06:06,500
And.

86
00:06:07,980 --> 00:06:08,220
Okay.

87
00:06:08,260 --> 00:06:18,820
What prompt was, uh, give the list of most common web API methods.

88
00:06:29,780 --> 00:06:33,460
Uh, is it good to develop one model for Pentesting or different model for each type?

89
00:06:33,660 --> 00:06:40,020
I recommend using each different model, uh, for, uh, specific things.

90
00:06:40,060 --> 00:06:45,540
Say for example, for web you can create a model for API, you can create a model, etc. if you want

91
00:06:45,540 --> 00:06:46,460
to keep it combined.

92
00:06:46,460 --> 00:06:47,740
You can also do that.

93
00:06:47,940 --> 00:06:51,260
Uh, but it is recommended that you have a larger.

94
00:06:52,610 --> 00:06:58,530
computational power, large system, large memory, because you would be stacking up a lot of knowledge

95
00:06:58,530 --> 00:06:59,530
for that model.

96
00:06:59,530 --> 00:07:02,730
So eventually it is going to consume more and more power.

97
00:07:02,730 --> 00:07:09,130
And if you do not provide it adequate power and resources, it would give you slower responses or eventually

98
00:07:09,130 --> 00:07:12,890
keep on crashing the same way that it was crashing for us right now.

99
00:07:13,810 --> 00:07:14,250
Okay.

100
00:07:14,690 --> 00:07:15,090
Yeah.

101
00:07:16,370 --> 00:07:17,050
Very nice.

102
00:07:17,170 --> 00:07:19,610
Uh, participant we can see some of the, uh.

103
00:07:19,610 --> 00:07:20,370
Your welcome.

104
00:07:20,730 --> 00:07:25,370
Some common web API methods like alert, confirm, prompt status, stop, and so on.

105
00:07:25,410 --> 00:07:25,730
Okay.

106
00:07:25,770 --> 00:07:35,450
Now we can say list the entire web API methods that you know.

107
00:07:42,050 --> 00:07:42,490
Okay.

108
00:07:42,770 --> 00:07:44,530
Uh, it gave us HTTP methods.

109
00:07:44,530 --> 00:07:47,370
We did not wanted HTTP methods, rather API methods.

110
00:07:47,370 --> 00:07:53,440
So we'll again give that prompt and try to ask information about, and you can see it is currently referencing

111
00:07:53,440 --> 00:07:58,200
and trying to read all API methods from different, different, different different kinds of documents

112
00:07:58,200 --> 00:07:59,400
that are available for here.

113
00:07:59,440 --> 00:08:03,080
Okay, now I'm going to, uh, to keep it cut short.

114
00:08:03,080 --> 00:08:09,640
And due to the less amount of time that we have, I'm going to choose some methods from here and some

115
00:08:09,640 --> 00:08:10,600
event handlers.

116
00:08:10,920 --> 00:08:19,360
So the first method that is of importance for me is I'm going to choose a method that is a print or

117
00:08:19,360 --> 00:08:21,840
I'll say window dot print.

118
00:08:23,000 --> 00:08:23,440
Okay.

119
00:08:24,800 --> 00:08:27,920
So we can take the print method okay.

120
00:08:27,960 --> 00:08:32,680
Eventually Lama sorry Lama will give you the response.

121
00:08:32,680 --> 00:08:34,320
That print is a method okay.

122
00:08:34,360 --> 00:08:38,200
Once you keep on asking iterating it will tell you that print is a method.

123
00:08:38,520 --> 00:08:40,560
And how does print works.

124
00:08:40,560 --> 00:08:43,120
Print basically is in it.

125
00:08:43,120 --> 00:08:44,960
It supports JavaScript as well.

126
00:08:44,960 --> 00:08:49,990
You can see it supports JS and print will open up the print Preview dialog box for you.

127
00:08:50,230 --> 00:08:55,190
So when you do this, it opens up this Print Preview dialog box.

128
00:08:55,310 --> 00:09:01,590
Similarly, in JavaScript, you can open that print preview dialog as well.

129
00:09:01,830 --> 00:09:03,870
When you send a print function like this.

130
00:09:04,710 --> 00:09:04,990
Sorry.

131
00:09:04,990 --> 00:09:06,750
Print method like this okay.

132
00:09:06,910 --> 00:09:16,150
And here you're able to see that this means if if the firewall does not block in the rejects the print

133
00:09:16,150 --> 00:09:18,790
method, then we can utilize it okay.

134
00:09:18,830 --> 00:09:21,510
This is confirmed.

135
00:09:22,030 --> 00:09:24,910
I mean this is one of the attempt that we are going to make now.

136
00:09:24,990 --> 00:09:30,470
So I'm going to make a I'm going to use a method that is print that is fixed.

137
00:09:31,950 --> 00:09:34,630
Now I'm going to use a handler.

138
00:09:35,430 --> 00:09:41,590
So handlers are on load on confirm etc..

139
00:09:41,590 --> 00:09:43,990
So let's let me show you on load first.

140
00:09:59,660 --> 00:10:00,060
Yeah.

141
00:10:03,300 --> 00:10:03,860
Yes.

142
00:10:03,860 --> 00:10:05,380
So we can see load.

143
00:10:05,580 --> 00:10:08,780
Then we have on error.

144
00:10:17,220 --> 00:10:17,940
Error event.

145
00:10:17,940 --> 00:10:19,500
We have the error event here.

146
00:10:19,780 --> 00:10:21,140
So an on error.

147
00:10:21,460 --> 00:10:26,540
So I will choose an which is mouse uh.

148
00:10:28,700 --> 00:10:33,300
Web API on mouse mouse event.

149
00:10:34,820 --> 00:10:36,540
So let's read about the mouse event.

150
00:10:36,700 --> 00:10:42,300
And in the mouse event we can see there are different types of handlers that we can choose.

151
00:10:44,420 --> 00:10:45,460
Mouse move.

152
00:10:45,770 --> 00:10:46,730
Mouse over.

153
00:10:46,890 --> 00:10:47,730
Mouse out.

154
00:10:47,770 --> 00:10:48,490
Mouse down.

155
00:10:48,530 --> 00:10:49,530
Mouse enter.

156
00:10:49,570 --> 00:10:50,450
Mouse leave.

157
00:10:50,810 --> 00:10:51,650
Mouse up.

158
00:10:51,970 --> 00:10:52,570
And we'll.

159
00:10:52,570 --> 00:10:53,370
That is drag.

160
00:10:53,690 --> 00:10:55,490
Drag your wheel on the mouse.

161
00:10:55,810 --> 00:10:56,210
Okay.

162
00:10:56,210 --> 00:10:58,930
So we have different types of events that we can use now.

163
00:10:59,090 --> 00:11:02,850
So you can ask Lama to give you more events that you can use.

164
00:11:02,890 --> 00:11:03,050
Okay.

165
00:11:03,050 --> 00:11:06,250
So you can give it give a quick prompt here and it will give you the list.

166
00:11:06,250 --> 00:11:08,010
And then you can ask to compare.

167
00:11:08,890 --> 00:11:17,050
So you can say hey check the uh request line for the application attack request.

168
00:11:19,410 --> 00:11:26,730
Nine for one file to understand the okay.

169
00:11:26,730 --> 00:11:28,370
So let's say file.

170
00:11:28,410 --> 00:11:34,850
Hey, check the file and explain what does it do.

171
00:11:38,370 --> 00:11:42,530
Let's try to understand the XSS attack configuration file.

172
00:11:42,570 --> 00:11:42,970
Okay.

173
00:11:48,490 --> 00:11:50,490
Oh, no.

174
00:11:51,570 --> 00:11:53,090
What is it trying to do?

175
00:11:55,250 --> 00:12:00,050
Okay, it it did not find the entire file name because we did not give the file name.

176
00:12:00,290 --> 00:12:01,330
I guess it should have.

177
00:12:02,410 --> 00:12:05,050
Uh, we should have given the entire file name.

178
00:12:05,050 --> 00:12:06,810
So now I'm going to give the entire file name.

179
00:12:15,890 --> 00:12:16,290
Yeah.

180
00:12:17,570 --> 00:12:18,530
Explain.

181
00:12:18,530 --> 00:12:23,370
What is this file?

182
00:12:32,610 --> 00:12:38,250
Okay, now it is saying that this file appears to be a configuration file related to application attack

183
00:12:38,530 --> 00:12:42,930
and on detection for XSS attack by Apache Modsecurity core rule sets.

184
00:12:43,000 --> 00:12:43,600
Very nice.

185
00:12:44,240 --> 00:12:58,000
And, uh, yeah, now we are going to say, can you please identify the parameters or event handlers

186
00:12:59,520 --> 00:13:09,920
or functions or methods which are not in the above file?

187
00:13:28,560 --> 00:13:29,080
Uh, yes.

188
00:13:29,080 --> 00:13:30,800
There is a web file as possible.

189
00:13:31,000 --> 00:13:35,920
So based on the Python code interpreter tool I'll execute some code to identify the parameters.

190
00:13:35,920 --> 00:13:36,160
Okay.

191
00:13:36,160 --> 00:13:39,760
So it is trying to basically create a script Python script.

192
00:13:39,760 --> 00:13:48,110
We can run that script and see what it does, so it will try to match if some kind of payloads are there

193
00:13:48,110 --> 00:13:49,430
into that file or not.

194
00:13:49,630 --> 00:13:51,590
We can try to give a better prompt to it.

195
00:13:51,630 --> 00:13:52,310
Of course.

196
00:13:52,750 --> 00:13:59,270
Uh, from where we can, uh, basically try to ask it to do this correctly, appropriately, appropriately,

197
00:13:59,270 --> 00:14:06,790
and see if the methods handler's functions are which are not there in the file from the Mozilla web

198
00:14:07,830 --> 00:14:09,670
developer notes that we have provided.

199
00:14:09,950 --> 00:14:15,110
Eventually it will give you the output that it gave me in the past that I was running.

200
00:14:15,350 --> 00:14:16,950
In one of my previous prompts.

201
00:14:16,950 --> 00:14:18,870
I'll show you those prompts as well.

202
00:14:19,150 --> 00:14:21,870
It came up with something very interesting.

203
00:14:22,070 --> 00:14:30,950
It showed me some handlers and a method and which said which it said is not part of the configuration

204
00:14:30,950 --> 00:14:31,390
file.

205
00:14:31,710 --> 00:14:34,910
And this was the given payload that I got.

206
00:14:35,350 --> 00:14:36,990
I was able to generate.

207
00:14:37,630 --> 00:14:42,740
So it gave me an Event on mouse Over.

208
00:14:42,980 --> 00:14:50,660
Then it gave me a method which is window dot print, and it told that it is not there in the rule set.

209
00:14:50,980 --> 00:14:57,020
Now participants, this is the payload that it that it generated for us.

210
00:14:57,060 --> 00:14:57,660
Group okay.

211
00:14:57,900 --> 00:15:02,660
And now I'm going to try this payload here and see how does it react.

212
00:15:02,700 --> 00:15:03,140
Okay.

213
00:15:03,420 --> 00:15:08,180
So I'm going to remove this and paste it here and hit enter.

214
00:15:08,820 --> 00:15:14,900
Did you see that participants we are not blocked anymore.

215
00:15:15,180 --> 00:15:15,660
Okay.

216
00:15:16,300 --> 00:15:23,140
We successfully bypass the WAF and the first line of defense.

217
00:15:23,140 --> 00:15:25,220
And my payload has reached the back end.

218
00:15:25,260 --> 00:15:28,900
Now why it did not got executed?

219
00:15:28,900 --> 00:15:33,220
Because my index dot HTML file only contains a text string like this.

220
00:15:33,260 --> 00:15:39,810
It does not contains a JavaScript function or an input to execute this, but I will still show you.

221
00:15:39,970 --> 00:15:42,890
I will execute this onto a live website and show you.

222
00:15:42,890 --> 00:15:45,690
But congratulations!

223
00:15:45,690 --> 00:15:54,210
We are successful in generating a payload that is not triggered by Mod security and participants.

224
00:15:54,490 --> 00:16:04,250
If you just recall, at the beginning of the session, we discussed that all of the or most of the WAF

225
00:16:04,250 --> 00:16:07,130
companies are built on Mod security.

226
00:16:07,370 --> 00:16:12,210
That means Cloudflare should also allow this payload.

227
00:16:12,210 --> 00:16:13,650
So let's go ahead and see that.

228
00:16:13,890 --> 00:16:15,610
So let's go to Cloudflare.

229
00:16:18,050 --> 00:16:22,690
And first let's do a quick test on Cloudflare by entering this payload.

230
00:16:23,330 --> 00:16:27,370
So let me say question mark X equals to this payload hit enter.

231
00:16:28,090 --> 00:16:28,610
Yes.

232
00:16:28,930 --> 00:16:29,570
Participants.

233
00:16:29,570 --> 00:16:34,050
We have been blocked because we tried to send a payload which is known to Cloudflare.

234
00:16:34,250 --> 00:16:38,000
Now I'll send the payload and we will be Blocked.

235
00:16:38,800 --> 00:16:39,360
Awesome.

236
00:16:39,760 --> 00:16:41,480
This is what was expected.

237
00:16:41,520 --> 00:16:49,760
Now, participants, let's use the payload that was generated by the LLM for us and was not blocked

238
00:16:49,760 --> 00:16:52,280
on Mod security to see what happens here.

239
00:16:52,680 --> 00:16:55,600
And I'm going to hit enter and observe.

240
00:16:56,960 --> 00:16:57,440
Hooray!

241
00:16:57,760 --> 00:16:59,520
Congratulation participants.

242
00:17:00,040 --> 00:17:06,560
We have a working payload that is not being detected by two major firewalls.

243
00:17:06,760 --> 00:17:11,080
First is mod security and second one is Cloudflare.

244
00:17:11,880 --> 00:17:12,520
Excellent.

245
00:17:12,560 --> 00:17:16,560
Now how do we confirm that this is even a valid payload?

246
00:17:16,600 --> 00:17:17,960
We can confirm that.

247
00:17:17,960 --> 00:17:22,240
Let's go to test PHP and confirm that this is a valid payload.

248
00:17:24,360 --> 00:17:24,840
Okay.

249
00:17:25,200 --> 00:17:25,640
Yeah.

250
00:17:25,920 --> 00:17:27,800
Now let me go to the search menu.

251
00:17:28,000 --> 00:17:33,680
Paste this payload to show you that it satisfies the JavaScript syntax.

252
00:17:33,800 --> 00:17:34,920
So let me hit go.

253
00:17:35,160 --> 00:17:37,710
And what was the payload?

254
00:17:37,750 --> 00:17:41,190
The payload was on mouseover.

255
00:17:41,430 --> 00:17:42,550
Window dot print.

256
00:17:42,590 --> 00:17:43,390
Activate.

257
00:17:43,510 --> 00:17:44,510
That means when.

258
00:17:44,550 --> 00:17:48,470
When you take your mouse where is printed, you will get.

259
00:17:48,470 --> 00:17:50,590
The execution is printed.

260
00:17:50,590 --> 00:17:52,870
Here I'm taking the mouse and.

261
00:17:56,150 --> 00:17:57,950
Okay, let's do that once again.

262
00:18:00,510 --> 00:18:00,990
Okay.

263
00:18:01,030 --> 00:18:02,670
It did not give us an alert.

264
00:18:02,670 --> 00:18:03,630
Let's see why.

265
00:18:07,230 --> 00:18:08,070
Okay.

266
00:18:10,070 --> 00:18:11,430
Let's again do that.

267
00:18:17,790 --> 00:18:18,070
Um.

268
00:18:23,030 --> 00:18:23,470
Wait.

269
00:18:30,310 --> 00:18:32,350
Let me just change this a little bit, okay?

270
00:18:32,910 --> 00:18:33,270
Um.

271
00:18:36,780 --> 00:18:37,060
Mm.

272
00:18:56,620 --> 00:18:57,100
Okay.

273
00:18:57,460 --> 00:19:01,380
Uh, it did not trigger because my payload got encoded, but it got triggered now.

274
00:19:01,420 --> 00:19:01,620
Okay.

275
00:19:01,660 --> 00:19:02,460
Participants.

276
00:19:02,580 --> 00:19:04,940
So let me show you the right payload.

277
00:19:19,260 --> 00:19:20,140
And.

278
00:19:21,220 --> 00:19:23,220
Yeah, here's the right payload.

279
00:19:26,980 --> 00:19:27,460
Hooray!

280
00:19:27,780 --> 00:19:28,820
Did you see that?

281
00:19:28,820 --> 00:19:30,820
I have URL decoded the payload.

282
00:19:30,860 --> 00:19:32,660
The payload is again on the chat.

283
00:19:33,610 --> 00:19:34,170
Yes.

284
00:19:34,370 --> 00:19:39,570
And whenever I take my mouse on the keyboard, you can see the excess execution.

285
00:19:39,770 --> 00:19:43,850
Now, participants, this confirms that the payload is absolutely valid.

286
00:19:44,010 --> 00:19:46,650
Let me hit this on Cloudflare.

287
00:19:47,530 --> 00:19:48,490
Not blocked.

288
00:19:49,090 --> 00:19:51,010
Let's hit this on Modsec.

289
00:19:51,570 --> 00:19:52,450
Not blocked.

290
00:19:52,650 --> 00:19:56,530
Now let us run this onto a website that is protected by Cloudflare.

291
00:19:56,850 --> 00:19:59,530
So I'm going to go to my Cloudflare configuration.

292
00:20:00,250 --> 00:20:01,090
Yeah here.

293
00:20:01,330 --> 00:20:07,330
So this is my personal account on Cloudflare where you can see my dot in live traffic.

294
00:20:07,690 --> 00:20:10,330
So this is the live traffic in last 24 hours.

295
00:20:10,930 --> 00:20:16,490
41,000 requests for attacks mitigated, 29,000 requests served by Cloudflare.

296
00:20:16,850 --> 00:20:22,730
And one web application exploit was running and is being blocked.

297
00:20:22,770 --> 00:20:27,570
Okay, so this is basically the traffic that has been currently flowing on the live website.

298
00:20:27,610 --> 00:20:28,010
Okay.

299
00:20:28,250 --> 00:20:31,410
And my website is also protected by Cloudflare.

300
00:20:31,650 --> 00:20:35,640
Now I have created a test page called as XSS one dot PHP.

301
00:20:36,240 --> 00:20:37,480
You guys can go there.

302
00:20:37,640 --> 00:20:39,480
It is for testing purposes.

303
00:20:39,960 --> 00:20:45,800
If you go in the username field and you give a username Rohit or any username, it will do the reflection.

304
00:20:45,800 --> 00:20:46,760
Welcome, Rohit.

305
00:20:46,800 --> 00:20:50,120
So it is a test page for you to test this out.

306
00:20:50,120 --> 00:20:58,720
And I'm going to paste the payload hit submit and take my mouse pointer here.

307
00:20:58,720 --> 00:21:04,960
And you can see the XSS execution onto a Cloudflare protected website.

308
00:21:05,160 --> 00:21:13,120
That means now on any website in this or on any bug bounty program or pentesting targets.

309
00:21:13,120 --> 00:21:20,120
If it is running Cloudflare as well, you have a working bypass with you that you can run on any Cloudflare

310
00:21:20,160 --> 00:21:22,360
or Mod security protected website.

311
00:21:22,400 --> 00:21:23,240
Isn't that awesome?

312
00:21:23,240 --> 00:21:24,080
Participants?

313
00:21:27,400 --> 00:21:27,960
Yes.

314
00:21:33,190 --> 00:21:33,710
Awesome.

315
00:21:34,990 --> 00:21:35,550
Great.

316
00:21:53,110 --> 00:21:53,750
Uh, yes.

317
00:21:53,750 --> 00:21:56,550
So what happened was my payload.

318
00:21:56,550 --> 00:22:03,510
I actually copied the payload before the class from the URL, because of which my payload got URL encoded.

319
00:22:04,110 --> 00:22:09,710
Uh, this is how it got URL in, because whenever you copy anything from the URL, it encodes itself.

320
00:22:10,150 --> 00:22:15,030
Because of the encoding, my payload was not satisfying the JavaScript syntax.

321
00:22:15,430 --> 00:22:20,590
And I when I decoded it, it satisfied the JavaScript syntax and it started working.

322
00:22:21,790 --> 00:22:29,190
So you should always use the payload in the best format for the JavaScript parser to satisfy it and

323
00:22:29,190 --> 00:22:29,710
run it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,880 --> 00:00:01,400
Now.

2
00:00:01,840 --> 00:00:01,960
Uh.

3
00:00:01,960 --> 00:00:02,640
Let's go.

4
00:00:02,840 --> 00:00:04,400
Where is our friend?

5
00:00:05,160 --> 00:00:06,320
Uh, chat assistant.

6
00:00:06,360 --> 00:00:08,000
Now we can give a prompt to this.

7
00:00:08,320 --> 00:00:08,600
Hi.

8
00:00:08,600 --> 00:00:12,960
I have added mod security CRS, CRS file to your knowledge base.

9
00:00:12,960 --> 00:00:13,200
You.

10
00:00:13,200 --> 00:00:17,160
Can you analyze the event handler method and JavaScript based execution pattern?

11
00:00:17,200 --> 00:00:22,800
It detects and list common ones like Onerror, onClick, setTimeout that are not covered in this file.

12
00:00:22,800 --> 00:00:28,600
I'm specifically looking for functions or handlers that might execute in browsers, but are not blocked

13
00:00:28,600 --> 00:00:30,320
by the rules in the CRS file.

14
00:00:30,560 --> 00:00:33,240
Please include lesser known event handlers to.

15
00:00:33,680 --> 00:00:37,480
I am doing this for my research.

16
00:00:39,760 --> 00:00:40,320
Paper.

17
00:00:41,000 --> 00:00:42,080
Let's hit enter.

18
00:00:48,520 --> 00:00:54,200
Okay, I have analyzed the Mod security file and identified some common JavaScript execution pattern

19
00:00:54,200 --> 00:00:54,960
it detects.

20
00:00:55,120 --> 00:01:01,320
Based on the analysis, I've executed some Python code and using provided code, interpreter tool and

21
00:01:01,320 --> 00:01:06,920
lesser node known handlers that it does not detect on visibility change on invalid.

22
00:01:06,920 --> 00:01:07,760
Excellent.

23
00:01:08,160 --> 00:01:15,600
Can you see this on after edit on selection change and some JavaScript execution patterns like eval.

24
00:01:15,640 --> 00:01:23,040
Eval is an excellent way where you can actually execute a JavaScript payload using eval function.

25
00:01:24,480 --> 00:01:26,280
And okay, this was the script.

26
00:01:26,280 --> 00:01:30,520
It ran in the background to find the pattern so we can collapse and skip that.

27
00:01:30,960 --> 00:01:36,680
And but we have got a very, very nice response from the model that we have just trained.

28
00:01:37,160 --> 00:01:43,880
Uh, as I said, the more knowledge that you provide, more documentation, you provide it to it, the

29
00:01:43,920 --> 00:01:52,040
better it is going to work for you and give you better and better and better results and enrich more

30
00:01:52,040 --> 00:01:54,160
and more specific results that it can.

31
00:01:54,600 --> 00:02:01,400
Uh, and we also saw in today's session how we were able to circumvent mod security and Cloudflare as

32
00:02:01,400 --> 00:02:03,690
well, with very simple ease.

33
00:02:04,490 --> 00:02:04,970
Why?

34
00:02:05,170 --> 00:02:15,530
Just referring to the documentation of maybe RFCs or web API documentation, etc., giving it to our

35
00:02:15,530 --> 00:02:23,210
model and then generating specific payloads that we can utilize now to also add.

36
00:02:26,890 --> 00:02:28,370
Yes, that is correct.

37
00:02:31,130 --> 00:02:32,290
That is correct.

38
00:02:32,290 --> 00:02:37,290
The model is comparing that with the MDN documentation that that we have provided.

39
00:02:37,290 --> 00:02:40,730
We can give more and more, more and more documentation to it.

40
00:02:40,730 --> 00:02:44,690
So it works more in a more better manner.

41
00:02:48,170 --> 00:02:48,770
Yes.

42
00:02:50,930 --> 00:02:55,650
Now are participants to make this more better?

43
00:02:55,890 --> 00:03:05,610
What we can do is we can actually create a MCP server and let, uh, do the second half of the process

44
00:03:05,610 --> 00:03:08,210
that we are doing, we can automate that process as well.

45
00:03:08,250 --> 00:03:16,930
How we can create a simple Python script which takes all of these inputs that Chad, that Obama has

46
00:03:16,930 --> 00:03:21,610
given us and send this to the URL of the target.

47
00:03:21,770 --> 00:03:29,130
So it sends this to the URL target and checks if what event handler, what method is blocked or not

48
00:03:29,130 --> 00:03:29,610
blocked.

49
00:03:29,850 --> 00:03:32,650
So this will be again really really awesome.

50
00:03:32,650 --> 00:03:38,370
So you just give a prompt to your model to generate new payloads and even test them in the background,

51
00:03:38,370 --> 00:03:44,730
and then only give you the response or summary of what has worked and what not has worked.

52
00:03:45,490 --> 00:03:46,970
Wouldn't that be really awesome?

53
00:03:47,690 --> 00:03:56,050
So let's try to do generate a script that works in the background, identifies the methods, functions,

54
00:03:56,250 --> 00:03:58,650
and adds it to a file.

55
00:03:58,930 --> 00:04:04,210
So just to save time, I have already created a script and I'll share it with you now.

56
00:04:07,810 --> 00:04:08,970
Which works like this.

57
00:04:08,970 --> 00:04:10,250
So what does it do?

58
00:04:10,450 --> 00:04:19,930
It basically is going to you're going to you're going to run an MCP server that starts Cloudflare Test.py,

59
00:04:20,330 --> 00:04:27,650
and it is going to test payloads against the Cloudflare WAF automatically by on Cloudflare Comm.

60
00:04:27,810 --> 00:04:34,850
And it is going to give you what are the allowed special characters and that what are the blocked payloads

61
00:04:35,050 --> 00:04:39,530
and whatever has worked and whatever has allowed payloads and blocked payloads.

62
00:04:39,530 --> 00:04:47,890
It will give you a list and then you can automatically utilize this to generate a valid, valid payload

63
00:04:47,890 --> 00:04:48,770
that you can use it.

64
00:04:48,770 --> 00:04:49,170
Okay.

65
00:04:49,330 --> 00:04:50,530
So how does it work?

66
00:04:50,850 --> 00:04:53,130
It basically reads three files.

67
00:04:53,130 --> 00:04:54,530
First is event handler.

68
00:04:55,410 --> 00:04:57,570
Let me show you what event handler contains.

69
00:04:59,410 --> 00:05:06,730
So what I am doing is I am actually collecting all the event handlers by asking a prompt to Allama.

70
00:05:06,820 --> 00:05:14,140
And I'm saying give me all the event handlers in a list format from the Mozilla Web API documentation.

71
00:05:14,140 --> 00:05:15,620
So it gave me these many.

72
00:05:15,980 --> 00:05:20,660
Now I gave another prompt give me all the functions from the documentation.

73
00:05:20,660 --> 00:05:22,620
So it gave me these many functions.

74
00:05:22,900 --> 00:05:27,900
Next prompt I gave give me all special characters that are currently available to use.

75
00:05:27,900 --> 00:05:32,900
So it gave me these special characters through which we can create a payload like double quote, single

76
00:05:32,900 --> 00:05:37,340
quote, opening bracket, curly bracket, backticks, forward slash and backward slash.

77
00:05:37,340 --> 00:05:42,580
So we have functions, we have special characters, we have event handlers.

78
00:05:43,260 --> 00:05:46,300
Now we are going to run a script.

79
00:05:46,300 --> 00:05:48,300
So let me also show you that script.

80
00:05:50,140 --> 00:05:50,540
Yeah.

81
00:05:50,820 --> 00:05:54,380
So this script is going to send a request to Cloudflare.

82
00:05:54,900 --> 00:06:00,940
And it is going to tell us with what is blocked and what is allowed based on these three files.

83
00:06:00,940 --> 00:06:07,460
So it is going to load all events from event handler load functions from function dot, txt and load

84
00:06:07,460 --> 00:06:09,020
characters from special characters.

85
00:06:09,020 --> 00:06:09,700
Dot txt.

86
00:06:09,940 --> 00:06:10,340
Okay.

87
00:06:10,500 --> 00:06:12,140
And then it will generate the payload.

88
00:06:12,420 --> 00:06:13,980
Test it automatically.

89
00:06:13,980 --> 00:06:18,100
And if 403 response code is received then it will say you are blocked.

90
00:06:18,220 --> 00:06:20,660
If it is not received then it will say it is allowed.

91
00:06:20,820 --> 00:06:27,300
Isn't that very simple logic to do detection on mix and match permutation?

92
00:06:27,300 --> 00:06:33,980
Combination of handlers, functions and special characters to generate a valid payload that can bypass

93
00:06:34,020 --> 00:06:35,060
a Cloudflare WAF?

94
00:06:35,420 --> 00:06:43,660
Now this can be run directly through a prompt through Olama with the help of setting up a MCP server.

95
00:06:43,700 --> 00:06:52,980
So to do that, we can simply now create a API dot JSON file in which we can run a like write a route.

96
00:06:53,060 --> 00:06:56,900
To run this whenever we type a command run Cloudflare test.

97
00:06:57,220 --> 00:06:57,540
Okay.

98
00:06:57,580 --> 00:06:59,020
You always have to make sure.

99
00:07:01,300 --> 00:07:02,020
Yes.

100
00:07:02,060 --> 00:07:08,060
You always have to make sure that you update these handlers and functions, uh, periodically for new

101
00:07:08,060 --> 00:07:14,740
new types of handler or functions that you come across so that your list gets updated up to date and

102
00:07:14,740 --> 00:07:17,540
you are able to perform more and more test cases.

103
00:07:17,580 --> 00:07:18,020
Okay.

104
00:07:18,060 --> 00:07:22,540
So as of now I have very limited functions event handlers in special characters.

105
00:07:22,540 --> 00:07:25,820
I'm going to still run the script and show you manually.

106
00:07:25,980 --> 00:07:29,860
Then we can automate this to run it with the MCP server as well.

107
00:07:29,980 --> 00:07:30,340
Okay.

108
00:07:30,380 --> 00:07:32,100
So let me run this manually first.

109
00:07:40,860 --> 00:07:41,260
Then.

110
00:07:41,300 --> 00:07:42,500
So this is the summary.

111
00:07:42,500 --> 00:07:48,740
And in the summary you can see it says almost all of these are blocked and none of them are allowed.

112
00:07:48,780 --> 00:07:49,220
Okay.

113
00:07:49,260 --> 00:07:53,020
Now let me add the payload that we had found.

114
00:07:58,140 --> 00:07:59,540
In window dot print.

115
00:07:59,700 --> 00:08:01,820
Did it use window dot print on mouse.

116
00:08:01,820 --> 00:08:02,180
Over.

117
00:08:04,860 --> 00:08:06,700
On mouse leave on.

118
00:08:06,700 --> 00:08:10,140
Click on focus on mouse enter on.

119
00:08:10,230 --> 00:08:10,990
Mouse over.

120
00:08:11,030 --> 00:08:16,270
Okay, so you can see we only had on mouse enter and on mouse leave.

121
00:08:16,670 --> 00:08:17,270
That's it.

122
00:08:17,270 --> 00:08:18,910
We did not have on.

123
00:08:18,950 --> 00:08:20,230
We had for mouse.

124
00:08:20,230 --> 00:08:21,550
We have only these many.

125
00:08:25,470 --> 00:08:26,510
Event handlers.

126
00:08:28,390 --> 00:08:32,430
Now I'm going to give a handler additional handler on mouse over.

127
00:08:33,350 --> 00:08:33,630
Okay.

128
00:08:33,630 --> 00:08:34,390
It was there.

129
00:08:34,550 --> 00:08:35,070
Sorry.

130
00:08:39,230 --> 00:08:42,590
And uh, window dot print.

131
00:08:48,150 --> 00:08:48,670
Yes.

132
00:08:48,910 --> 00:08:51,830
Uh, now we can we can also give HTML entities.

133
00:08:51,830 --> 00:08:54,070
We have not given HTML entities to it.

134
00:08:54,070 --> 00:09:04,150
So we can give HTML entities like href, uh, iframe, etc., etc. as well so that it can generate that

135
00:09:04,150 --> 00:09:04,990
valid payload.

136
00:09:05,430 --> 00:09:11,870
And then we can connect this to the server and we can do the entire automation from there itself.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 12: Introduction of Shell Globbing

1
00:00:01,800 --> 00:00:02,400
Yes.

2
00:00:02,640 --> 00:00:08,600
So let us start by understanding what is shell globbing technique.

3
00:00:09,240 --> 00:00:09,440
Ah.

4
00:00:09,720 --> 00:00:18,400
So before we understand shell globbing one very important fun fact for participants, uh, the entire

5
00:00:18,440 --> 00:00:31,880
world that runs server 90% of the world's servers that you see run on Linux, that means you should

6
00:00:31,880 --> 00:00:34,800
be familiar with how Linux system works.

7
00:00:35,200 --> 00:00:41,640
What is the directory structure for Linux, or what are the commands that you will be using in Linux,

8
00:00:42,120 --> 00:00:48,280
or how to configure tools, how what are the permissions, access control, etc. in Linux?

9
00:00:48,400 --> 00:00:54,640
So if you are aware about the basics, that is sufficient for you to perform various types of, uh,

10
00:00:54,640 --> 00:00:56,040
test cases in Linux.

11
00:00:56,280 --> 00:01:04,080
So today I have two publicly available links that I want to share with participants.

12
00:01:04,720 --> 00:01:15,120
So this is not exactly RFC, I would say, but it is the standard documentation of how shell Globbing

13
00:01:15,120 --> 00:01:15,720
works.

14
00:01:16,080 --> 00:01:25,840
This documentation is actually coming from the official Posix documentation that was used to create

15
00:01:25,840 --> 00:01:27,520
Unix and Linux.

16
00:01:28,400 --> 00:01:32,960
Now these are two good articles that I wanted to share with participants, where you can understand

17
00:01:32,960 --> 00:01:42,000
about what is shell globbing and how commands work into Linux system commands to do arithmetic expansion,

18
00:01:42,040 --> 00:01:45,800
expansion, redirection, etc., etc..

19
00:01:45,800 --> 00:01:50,120
So basically normally how commands work now.

20
00:01:50,600 --> 00:01:54,400
Uh, so so you can read more about it.

21
00:01:54,400 --> 00:01:59,120
So you can see the sh command is basically to execute a system shell.

22
00:01:59,680 --> 00:02:06,650
Uh that is a function that defines system interfaces in the volume of 6.1 2017.

23
00:02:06,690 --> 00:02:12,490
It's a very large documentation that you that you can also read more about.

24
00:02:12,730 --> 00:02:15,850
Uh, but of course we are not going to read it manually.

25
00:02:15,850 --> 00:02:23,810
Rather, we are going to give this to our LM agent, which is going to summarize it for us and help

26
00:02:23,810 --> 00:02:25,850
us understand all the information from it.

27
00:02:25,850 --> 00:02:26,250
Okay.

28
00:02:26,530 --> 00:02:33,170
So here's the new documentation, new website over here of IEEE standards for Posix, newer standards

29
00:02:33,170 --> 00:02:34,810
where you can read more about it.

30
00:02:35,170 --> 00:02:37,490
So I'll simply search for globbing here.

31
00:02:48,050 --> 00:02:48,450
Okay.

32
00:02:48,450 --> 00:02:50,610
Let me do a search once again.

33
00:02:50,930 --> 00:02:56,690
Let's you can do a Google search as well to find it on a new version of the website.

34
00:02:56,690 --> 00:02:58,930
Or we can just simply see here as well.

35
00:02:59,410 --> 00:03:02,650
So here we can understand about shell introduction.

36
00:03:02,650 --> 00:03:06,130
We can understand about how coating works in shell.

37
00:03:06,450 --> 00:03:07,850
So we can see there's a pipe.

38
00:03:07,890 --> 00:03:11,010
There's an ampersand semicolon.

39
00:03:13,130 --> 00:03:24,050
Tags braces round braces then uh a dollar sign which is a shell variable, etc. we can see escape characters.

40
00:03:24,050 --> 00:03:32,530
We can see single quotes, we can see double quotes, then backslash and a lot of useful information

41
00:03:32,530 --> 00:03:33,090
for us.

42
00:03:33,970 --> 00:03:42,370
Similarly here in globbing techniques we can understand that how uh commands work in Linux.

43
00:03:42,530 --> 00:03:50,330
So for example when I do an LS hyphen, all that is list all the files with their properties.

44
00:03:50,330 --> 00:03:53,530
I can see that there are currently two files that can be seen.

45
00:03:55,690 --> 00:04:01,100
Which is yeah T-2 dot sh and t test one dot txt.

46
00:04:01,140 --> 00:04:06,500
These files are currently empty files or you can say temporary files that has been created.

47
00:04:06,500 --> 00:04:08,100
Hence they were not counted here.

48
00:04:08,860 --> 00:04:10,340
Uh, so there are two files over here.

49
00:04:10,380 --> 00:04:14,620
Now when I say hyphen all t question mark.sh.

50
00:04:14,940 --> 00:04:21,580
So primarily what I'm doing is I don't know which files exist over here, but I just want to list a

51
00:04:21,580 --> 00:04:25,060
file from all these files or maybe these two files.

52
00:04:25,420 --> 00:04:28,820
The file that has t question mark.

53
00:04:28,820 --> 00:04:33,780
So both of the files actually starts with the t uh, as a first character.

54
00:04:33,780 --> 00:04:36,620
But I've specified something over here that is.sh.

55
00:04:36,940 --> 00:04:40,340
That means, uh, shell script or it ends with sh.

56
00:04:40,700 --> 00:04:42,860
So this file is being matched over here.

57
00:04:46,860 --> 00:04:47,940
Just give me a second.

58
00:04:47,940 --> 00:04:49,180
I'll just disable this.

59
00:04:59,220 --> 00:04:59,700
Okay.

60
00:05:08,980 --> 00:05:11,140
Okay, so here we are.

61
00:05:11,340 --> 00:05:11,700
Yeah.

62
00:05:11,700 --> 00:05:13,460
We can see T2 dot s h.

63
00:05:13,900 --> 00:05:18,220
So this is basically going to match and identify that file for us.

64
00:05:18,260 --> 00:05:21,300
Now see the next command ls hyphen all.

65
00:05:21,580 --> 00:05:26,180
And then we are saying a and B in box bracket and star.

66
00:05:26,220 --> 00:05:30,140
So what it is going to do it is going to say it is going to identify.

67
00:05:30,140 --> 00:05:32,420
So it is like a regex pattern here.

68
00:05:32,580 --> 00:05:36,460
It is going to find files that contains a or b.

69
00:05:37,020 --> 00:05:40,700
We have not specified the extension and it is able to find it.

70
00:05:41,060 --> 00:05:47,700
Similarly, now we see a range so a from a to c, so a b, c.

71
00:05:47,740 --> 00:05:49,060
We are trying to give a range.

72
00:05:49,060 --> 00:05:51,700
And we can see all these three files have been listed here.

73
00:05:52,580 --> 00:05:54,460
Now here we can see hyphen all.

74
00:05:54,460 --> 00:05:59,590
And we can see a hat given to a B bee and a star.

75
00:05:59,710 --> 00:06:07,830
So this basically means the files that does not contains A and B, they should not be printed.

76
00:06:07,990 --> 00:06:12,510
So you can see you can say that it is a not expression over here.

77
00:06:13,110 --> 00:06:23,630
Similarly HL7 all B star that means include b c star that means include C and star S star.

78
00:06:23,790 --> 00:06:28,150
That means include something that contains est which matches here.

79
00:06:28,510 --> 00:06:31,430
So this is how we were able to get this file.

80
00:06:32,230 --> 00:06:39,150
Now we can do also bash can also perform file name expansion and uncoded command line arguments as we

81
00:06:39,150 --> 00:06:40,190
can see over here.

82
00:06:40,790 --> 00:06:42,390
Now let's understand.

83
00:06:42,390 --> 00:06:46,750
So this was some of the basics for you to understand because this is the technique that we are going

84
00:06:46,750 --> 00:06:50,110
to use now which is globbing.

85
00:06:50,670 --> 00:06:54,390
So bash interprets special characters in the Globbing range.

86
00:06:54,430 --> 00:06:54,830
Okay.

87
00:06:55,030 --> 00:07:00,710
So uh, for example here we can see we have specified an IFS.

88
00:07:00,790 --> 00:07:05,110
So that basically means a variable which is dollar printf.

89
00:07:05,470 --> 00:07:09,830
The current the correct glob use for this would be.

90
00:07:10,310 --> 00:07:10,630
Yeah.

91
00:07:10,630 --> 00:07:14,470
So if you see this uh simple loop.

92
00:07:16,630 --> 00:07:22,190
Then we are saying file for file in the current directory okay.

93
00:07:22,230 --> 00:07:29,950
All the files do what uh do check if the file is there and it is not empty.

94
00:07:30,110 --> 00:07:32,070
So we are currently checking a file.

95
00:07:32,750 --> 00:07:33,190
Uh, sorry.

96
00:07:33,230 --> 00:07:36,110
Checking the file is not empty or the file exists.

97
00:07:36,350 --> 00:07:38,230
So hyphen E is used to check that.

98
00:07:38,230 --> 00:07:39,590
So we are able to check that.

99
00:07:39,830 --> 00:07:42,070
And uh it will be printed.

100
00:07:42,070 --> 00:07:44,510
Whatever the file name is it will be printed.

101
00:07:44,550 --> 00:07:46,630
Dollar file loop is closed.

102
00:07:46,950 --> 00:07:49,030
And yeah the loop is closed here.

103
00:07:49,030 --> 00:07:51,030
So so what does this basically do.

104
00:07:51,030 --> 00:07:56,590
It will print out files that exist in the current directory because we are trying to find all files

105
00:07:56,950 --> 00:07:58,110
uh listed over here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,240 --> 00:00:08,200
Uh, I'm currently running Mac OS, which is bare bones Linux in the background.

2
00:00:08,400 --> 00:00:10,960
So Mac OS is built on Linux.

3
00:00:11,280 --> 00:00:15,920
That means if I execute few commands like we can see a clear command when I.

4
00:00:15,960 --> 00:00:19,800
When I say uname command, I'm able to see the name.

5
00:00:19,800 --> 00:00:26,040
When I say id command, I'm able to see the ID, etc. so basically all the Linux commands work on Mac

6
00:00:26,040 --> 00:00:29,280
OS as well because it is inbuilt built on Linux.

7
00:00:30,160 --> 00:00:30,680
Great.

8
00:00:31,520 --> 00:00:36,320
Now, as we have understood about shell globbing technique, let me use one of the technique that will

9
00:00:36,320 --> 00:00:38,760
be helpful for here, uh, for us.

10
00:00:38,760 --> 00:00:41,560
So I'm going to execute a command that is date command.

11
00:00:42,200 --> 00:00:42,680
Okay.

12
00:00:42,720 --> 00:00:47,360
And we are able to see the output over here that this is the current or today's date.

13
00:00:47,720 --> 00:00:53,000
Now instead of the E I'm going to specify a question mark over here.

14
00:00:53,000 --> 00:00:54,800
And I will print enter.

15
00:00:54,840 --> 00:00:55,360
Okay.

16
00:00:55,400 --> 00:00:58,720
So we saw that no match is found for this command.

17
00:00:58,720 --> 00:01:00,080
And it did not execute.

18
00:01:00,440 --> 00:01:05,050
Now I'm going to say which date, which date.

19
00:01:05,450 --> 00:01:13,090
Now, if you understand Linux file system a little bit more, then we would be able to understand that

20
00:01:13,090 --> 00:01:16,370
all the commands are actually binaries.

21
00:01:16,370 --> 00:01:17,690
These are files.

22
00:01:18,130 --> 00:01:21,570
So date command is actually listed in the binary directory.

23
00:01:21,570 --> 00:01:22,930
And here is the command.

24
00:01:23,330 --> 00:01:29,050
So if I say cat bin date you can see this current binary.

25
00:01:29,250 --> 00:01:35,410
Now I'm not able to read that binary because it contains some code or program in itself.

26
00:01:35,410 --> 00:01:40,610
You can see a little bit functions in clear text, but we are not able to read it.

27
00:01:40,610 --> 00:01:43,290
We are able to execute that binary.

28
00:01:43,290 --> 00:01:45,930
So we are able to execute that binary.

29
00:01:46,930 --> 00:01:54,410
So instead of cat, if I want to execute this binary, then I can execute it directly from here as well

30
00:01:55,170 --> 00:01:55,610
okay.

31
00:01:55,730 --> 00:01:57,450
So it gets executed.

32
00:01:57,490 --> 00:02:01,010
Now if I say bash and then try to execute it, would that work?

33
00:02:01,010 --> 00:02:07,730
The answer is yes, because that is actually a binary intended to run onto a Linux file system.

34
00:02:08,490 --> 00:02:13,770
Now, instead of executing a binary, let's try to read a file.

35
00:02:14,170 --> 00:02:20,410
So I'm going to read a file so we can read any files that are in the configuration directory or specifically

36
00:02:20,450 --> 00:02:21,890
etc. directory as well.

37
00:02:22,170 --> 00:02:24,210
So let's go to the etc. directory.

38
00:02:24,530 --> 00:02:24,890
Etc..

39
00:02:24,890 --> 00:02:28,410
Directory is a similar directory that we have in windows.

40
00:02:29,090 --> 00:02:31,850
Windows file system that is program files.

41
00:02:31,850 --> 00:02:37,330
So any programs that are user installed would go into etc. and system installed programs also go in

42
00:02:37,330 --> 00:02:37,850
etc..

43
00:02:38,330 --> 00:02:42,770
Now when I do an LS we can see there are a lot of files present over here.

44
00:02:43,090 --> 00:02:45,730
For example np dot conf.

45
00:02:45,930 --> 00:02:52,250
So this file is used to sync my system time with the server time.

46
00:02:52,290 --> 00:02:53,010
Network time.

47
00:02:53,010 --> 00:02:55,290
Protocol port number 123.

48
00:02:55,570 --> 00:03:01,890
So this file is basically used to make sure that my system is always synced with the current time.

49
00:03:02,340 --> 00:03:06,940
In addition to that, if you can see, you'll be able to see more commands as well as files.

50
00:03:07,220 --> 00:03:11,620
Hosts file contains the entries for DNS resolution.

51
00:03:11,780 --> 00:03:14,740
Then we have sudoers files and so on.

52
00:03:14,780 --> 00:03:15,180
Okay.

53
00:03:15,220 --> 00:03:19,220
I'm interested in a file which is this file which is passwd.

54
00:03:19,340 --> 00:03:23,100
So let us execute the file command on passwd.

55
00:03:23,340 --> 00:03:33,500
And we can see that this is an Ascii text file wherein when you say file date then oops let's say bin

56
00:03:33,500 --> 00:03:33,980
date.

57
00:03:34,460 --> 00:03:45,260
Then we can see that it is in a mac OS 64 bit executable file that works on x64 architecture as well

58
00:03:45,260 --> 00:03:47,340
as ARM architecture that is Apple silicon.

59
00:03:47,620 --> 00:03:52,300
Whereas when we did file passwd it told us that it is an Ascii text file.

60
00:03:52,340 --> 00:03:52,860
Great.

61
00:03:53,180 --> 00:03:54,980
Now we want to read this file.

62
00:03:54,980 --> 00:03:56,460
So how do we read it.

63
00:03:56,460 --> 00:03:59,780
So I can say cat passwd.

64
00:04:00,140 --> 00:04:05,590
And yes it was Ascii text file type, and we are able to read the contents of this file.

65
00:04:06,230 --> 00:04:06,830
Nice.

66
00:04:07,110 --> 00:04:07,830
Very nice.

67
00:04:08,150 --> 00:04:10,230
What does this file actually contains?

68
00:04:10,230 --> 00:04:15,790
Or what is the responsibility of this file or significance of this file?

69
00:04:15,950 --> 00:04:26,550
So passwd file in Linux systems is used to give information about the users that exist in the system.

70
00:04:26,750 --> 00:04:29,830
I currently have a user called as nobody root.

71
00:04:30,030 --> 00:04:34,910
Then these are default users daemon, UCP and so on.

72
00:04:34,910 --> 00:04:38,630
You can see a lot of users are there in my system.

73
00:04:39,550 --> 00:04:45,950
So possibility file basically is a file that contains the information about users.

74
00:04:46,390 --> 00:04:47,030
Excellent.

75
00:04:47,470 --> 00:04:53,030
Now as I said the possibility file is a file that is in the etc. directory.

76
00:04:53,470 --> 00:04:59,950
How do I confirm that I can execute the PWD present working directory command to see where I am, and

77
00:04:59,950 --> 00:05:01,430
I'm in the etc. directory?

78
00:05:01,790 --> 00:05:03,950
Let me go back to go back.

79
00:05:03,950 --> 00:05:06,230
I'm saying CD space dot dot.

80
00:05:06,230 --> 00:05:09,790
So I go one step back now to read that file.

81
00:05:09,790 --> 00:05:17,710
I can simply say cat etc. passwd and hit enter and we are able to read that file absolutely fine.

82
00:05:19,030 --> 00:05:27,310
Now participants, when I run this command, I'm getting an output of that command that confirms that

83
00:05:27,350 --> 00:05:33,710
me as a user who is rohith, is able to execute a command on the Linux system, and the command has

84
00:05:33,750 --> 00:05:41,670
executed successfully and is allowing me to see the output which is the contents of the given file.

85
00:05:41,910 --> 00:05:42,390
Great.

86
00:05:42,870 --> 00:05:46,830
So this means that this is a valid Linux command.

87
00:05:47,230 --> 00:05:49,270
Let's go on Cloudflare.

88
00:05:51,430 --> 00:05:54,990
So Cloudflare again is an excellent and great Faf.

89
00:05:55,270 --> 00:06:01,710
So I'm going to go here and I'm going to write the command etc. passwd and cat.

90
00:06:02,030 --> 00:06:10,160
So let us just try to see if the Cloudflare firewall triggers a warning or blocks us, because this

91
00:06:10,160 --> 00:06:17,480
is a very common payload that is used to hack into a website or do a code injection or code execution.

92
00:06:17,480 --> 00:06:19,200
So I'm going to hit enter.

93
00:06:20,040 --> 00:06:20,400
Nice.

94
00:06:20,400 --> 00:06:21,720
We did not got blocked.

95
00:06:25,560 --> 00:06:26,160
Yes.

96
00:06:27,880 --> 00:06:29,280
Uh, let me just say it.

97
00:06:29,320 --> 00:06:30,280
Sorry, sorry.

98
00:06:30,680 --> 00:06:31,960
It is the password.

99
00:06:34,720 --> 00:06:35,120
Okay.

100
00:06:35,600 --> 00:06:43,000
Uh, this did not trigger a, uh, did not trigger the firewall.

101
00:06:43,240 --> 00:06:45,560
Let us go and launch.

102
00:06:49,080 --> 00:06:51,040
Ideally, it should have triggered.

103
00:06:51,040 --> 00:06:54,840
Let us see what is the behavior with mod mod security.

104
00:06:55,960 --> 00:07:10,760
Okay, so I'm going to go here and I'm going to say that EDC password, hit enter and we are able to

105
00:07:10,760 --> 00:07:12,360
see an output that is forbidden.

106
00:07:12,720 --> 00:07:14,440
Okay, just give me a moment.

107
00:07:25,800 --> 00:07:26,560
Yes.

108
00:07:26,560 --> 00:07:28,880
So participants, we can see over here that we are.

109
00:07:29,040 --> 00:07:31,040
We have got blocked.

110
00:07:31,080 --> 00:07:36,960
We are blocked over here because, uh, cat ADC passwd is a malicious command.

111
00:07:36,960 --> 00:07:46,440
And if you see in the logs as well, this is the, uh, response 980 correlation.

112
00:07:46,440 --> 00:07:46,800
Yeah.

113
00:07:46,840 --> 00:07:54,200
See this one here we can see the current request 932 application attack RC remote code execution is

114
00:07:54,200 --> 00:07:59,280
triggered because it says that someone has tried to execute etc. passwd command.

115
00:07:59,840 --> 00:08:02,840
Uh, as we can see over here, that is absolutely correct.

116
00:08:03,080 --> 00:08:04,800
And we got blocked now.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,400 --> 00:00:01,680
What do we do next?

2
00:00:02,080 --> 00:00:10,680
So with the help of the current technique that we were understanding, that is shell Globbing and the

3
00:00:10,680 --> 00:00:17,520
examples that we saw here, we are going to do the same thing over here.

4
00:00:17,880 --> 00:00:18,320
Okay.

5
00:00:20,400 --> 00:00:20,760
Yes.

6
00:00:20,760 --> 00:00:23,480
So we are going to do the same thing over here.

7
00:00:23,800 --> 00:00:29,800
So to do that we are going to first understand how shell Globbing works.

8
00:00:29,800 --> 00:00:33,840
And I'm going to say cat adc p a s s wd.

9
00:00:33,840 --> 00:00:39,240
So instead of executing this command participants I'm going to specify a wildcard character.

10
00:00:39,800 --> 00:00:42,680
The current wildcard character that you see is a question mark.

11
00:00:42,680 --> 00:00:43,200
Question mark.

12
00:00:43,200 --> 00:00:43,960
Question mark.

13
00:00:44,520 --> 00:00:47,840
Now when I hit enter let us observe the output.

14
00:00:48,840 --> 00:00:49,360
Great.

15
00:00:49,640 --> 00:00:57,720
We are able to get the exact same output as if we are executing the passwd command, as we can see over

16
00:00:57,720 --> 00:00:58,160
here.

17
00:00:58,560 --> 00:01:02,720
So when we executed this command, we got the same exact output.

18
00:01:03,120 --> 00:01:04,400
Wow, isn't that cool?

19
00:01:05,880 --> 00:01:06,760
Participants.

20
00:01:07,520 --> 00:01:08,400
Are you with me?

21
00:01:13,400 --> 00:01:13,920
Yes.

22
00:01:17,160 --> 00:01:18,040
Super amazing.

23
00:01:19,520 --> 00:01:20,120
Yes.

24
00:01:20,800 --> 00:01:22,600
Uh, great.

25
00:01:22,960 --> 00:01:27,200
We are going to see more interesting things now.

26
00:01:28,760 --> 00:01:37,080
So let's try to execute the same payload and see how does mod security behave.

27
00:01:37,120 --> 00:01:39,240
So I'm going to replace that with question mark.

28
00:01:39,240 --> 00:01:40,040
Question mark.

29
00:01:41,920 --> 00:01:44,360
And uh we are going to hit enter.

30
00:01:44,600 --> 00:01:49,880
Uh no that is absolutely fine because Rohit is currently not a privileged user on this system.

31
00:01:50,640 --> 00:01:56,160
Uh, root is so I could execute that command from root as well and get the same desired output.

32
00:01:58,000 --> 00:02:01,560
Now, let us execute this command, and let's try to trick the firewall.

33
00:02:02,240 --> 00:02:04,090
And did you see that?

34
00:02:05,490 --> 00:02:06,730
Let's do this once again.

35
00:02:06,730 --> 00:02:09,610
So when we try to read passwd file we got blocked.

36
00:02:09,730 --> 00:02:12,930
But when we say cat btc p a question mark.

37
00:02:12,930 --> 00:02:14,890
Question mark we did not got blocked.

38
00:02:15,170 --> 00:02:16,850
Isn't that really interesting.

39
00:02:17,450 --> 00:02:28,450
So this first shell globbing technique gives us an idea that when we try to send or execute a command

40
00:02:28,450 --> 00:02:37,250
like this, the firewall, which is the first line of defense, would not understand this command and

41
00:02:37,250 --> 00:02:42,650
would allow this command to go to the origin server.

42
00:02:42,930 --> 00:02:50,290
This could lead to a WAF bypass for a given target where we are trying to execute commands.

43
00:02:51,090 --> 00:02:57,650
So it's a classic example that we have seen right now, and we would be able to now fetch that file

44
00:02:58,370 --> 00:03:03,210
uh, as well from the background and read that password file as well.

45
00:03:03,250 --> 00:03:03,690
Okay.

46
00:03:03,730 --> 00:03:05,770
So we'll do that as well in a moment.

47
00:03:06,370 --> 00:03:12,330
Uh, but yes, we saw that first shell globbing technique using a question mark has worked really,

48
00:03:12,330 --> 00:03:13,650
really nice for us.

49
00:03:14,050 --> 00:03:17,450
Now let's try to be a little bit more creative here.

50
00:03:18,250 --> 00:03:26,450
Now cat etc. passwd is the command that we are executing participants.

51
00:03:26,690 --> 00:03:31,330
Now cat is again a command which is executed from the bin directory.

52
00:03:31,330 --> 00:03:33,610
Isn't it that what we learned initially.

53
00:03:33,890 --> 00:03:36,570
So now our command is going to be like this.

54
00:03:36,570 --> 00:03:37,970
And let us see if that works.

55
00:03:38,330 --> 00:03:39,770
Yes that works.

56
00:03:39,770 --> 00:03:41,370
We have got the same output.

57
00:03:41,530 --> 00:03:42,250
Excellent.

58
00:03:43,010 --> 00:03:48,530
Now let us try to see how much wildcard we can use over here.

59
00:03:48,650 --> 00:03:53,650
So I'm going to say p a question mark, question mark, question mark and question mark.

60
00:03:53,650 --> 00:03:54,650
Let us hit enter.

61
00:03:55,330 --> 00:04:00,330
And did you see that we are still able to get the desired output.

62
00:04:00,770 --> 00:04:02,210
Let us do the same thing here.

63
00:04:02,250 --> 00:04:04,930
Let's say instead of e let's say e question mark.

64
00:04:04,970 --> 00:04:05,290
See.

65
00:04:06,090 --> 00:04:10,130
And did you see that we are able to get the same desired output?

66
00:04:10,490 --> 00:04:11,850
So let's copy this.

67
00:04:11,890 --> 00:04:16,130
And let us see how does the firewall behaves over here.

68
00:04:16,770 --> 00:04:18,170
So I'm going to hit enter.

69
00:04:19,290 --> 00:04:20,570
Oops sorry.

70
00:04:22,650 --> 00:04:23,130
Yeah.

71
00:04:23,170 --> 00:04:25,290
Cat bin sorry.

72
00:04:27,450 --> 00:04:27,850
Yeah.

73
00:04:27,890 --> 00:04:29,770
Bin cat etc. passwd.

74
00:04:29,810 --> 00:04:30,810
Let's hit enter.

75
00:04:35,090 --> 00:04:39,570
Uh it is trying to redirect so let me just do it manually.

76
00:04:42,490 --> 00:04:43,010
Yes.

77
00:04:43,170 --> 00:04:44,050
And we can see.

78
00:04:47,090 --> 00:04:50,370
We can see that we have not blocked over here as well.

79
00:04:50,370 --> 00:04:52,450
That is really really nice.

80
00:04:52,970 --> 00:04:53,650
Great.

81
00:04:53,650 --> 00:05:01,250
So now we can also say here slash bin slash cat.

82
00:05:01,290 --> 00:05:03,250
Oh did you see that now.

83
00:05:03,410 --> 00:05:09,740
So the firewall catches the bin bien execution or the bin directory.

84
00:05:09,940 --> 00:05:13,220
So inbound anomaly critical.

85
00:05:14,380 --> 00:05:15,540
Um, yeah.

86
00:05:15,700 --> 00:05:18,660
So it detects when we send the command bin.

87
00:05:19,060 --> 00:05:23,020
So and let's try to say b question mark N and it works.

88
00:05:23,420 --> 00:05:24,380
Did you see that.

89
00:05:24,460 --> 00:05:32,780
So the the latest version of the mod security core rule set firewall detects bin but does not detects

90
00:05:32,820 --> 00:05:34,020
B question mark N.

91
00:05:34,220 --> 00:05:35,940
And is this a valid command.

92
00:05:37,340 --> 00:05:37,900
Yes.

93
00:05:38,260 --> 00:05:42,820
Let's copy this and let's try to execute it on the terminal here itself.

94
00:05:44,180 --> 00:05:48,660
And absolutely yes that's a valid command as we can see over here.

95
00:05:48,940 --> 00:05:54,020
So our first shell globbing technique has worked absolutely fine.

96
00:05:54,020 --> 00:05:56,340
And we are able to get the desired output.

97
00:05:56,380 --> 00:06:01,620
Now let us see as we are not getting blocked we have breached the first line of defense.

98
00:06:01,740 --> 00:06:09,900
Let us try to see if we can also bypass and filter an additional filter that someone might apply.

99
00:06:09,900 --> 00:06:13,620
So let's say there is a large organization, a very big organization.

100
00:06:13,620 --> 00:06:17,300
They rely on firewall, but we are able to breach the firewall.

101
00:06:17,300 --> 00:06:22,860
But as an added security practice they also add some custom rules.

102
00:06:22,860 --> 00:06:29,780
So I'm going to add a custom rule on a Cloudflare protected website right now and we'll see what happens.

103
00:06:30,100 --> 00:06:32,500
So I'm going to log in into my Cloudflare account.

104
00:06:32,540 --> 00:06:33,860
Just give me a moment.

105
00:06:46,620 --> 00:06:49,220
And let's go to security.

106
00:06:49,220 --> 00:06:51,380
And let's go to security rules.

107
00:06:55,180 --> 00:06:55,620
Okay.

108
00:06:55,780 --> 00:07:00,900
So participants if you see here then I have written a rule.

109
00:07:01,460 --> 00:07:09,540
The rule contains if anyone tries to send etc. passwd on any website, take an action that is blocked

110
00:07:09,820 --> 00:07:17,420
and you can see the actions that has been taken in past 13,000 actions have been taken in past.

111
00:07:17,420 --> 00:07:21,180
So anyone who tries to read this file from the server would get blocked.

112
00:07:21,220 --> 00:07:23,140
Okay, so we can see these logs as well.

113
00:07:23,900 --> 00:07:24,740
Let me go on that.

114
00:07:24,740 --> 00:07:27,980
And these are all of these logs which has been triggered.

115
00:07:27,980 --> 00:07:31,900
So anyone who tries to basically read that file would be blocked.

116
00:07:32,700 --> 00:07:33,140
Okay.

117
00:07:33,340 --> 00:07:36,660
Now let's take the example of this rule itself.

118
00:07:37,940 --> 00:07:40,780
So we have got a request.

119
00:07:41,180 --> 00:07:42,660
Uh, yeah.

120
00:07:42,660 --> 00:07:45,580
We have got a request on April 24th, 832.

121
00:07:45,580 --> 00:07:50,020
So just so just few minutes ago, it's 840 right now.

122
00:07:50,340 --> 00:07:56,420
And our custom rule is taking an action that is block on an endpoint that is host XYZ dot PHP.

123
00:07:56,420 --> 00:07:57,540
So let's go over there.

124
00:07:57,900 --> 00:08:04,420
So I go to hack dot n uh first let me just say cat passwd and let's see the response.

125
00:08:07,020 --> 00:08:08,060
Did you see that.

126
00:08:08,180 --> 00:08:09,540
So we are blocked.

127
00:08:09,540 --> 00:08:10,700
And why are we blocked.

128
00:08:10,750 --> 00:08:11,990
because of Cloudflare?

129
00:08:12,670 --> 00:08:17,150
Uh, the action that you just performed that triggered the security solution.

130
00:08:17,150 --> 00:08:19,150
Performance and security by Cloudflare.

131
00:08:19,390 --> 00:08:20,350
Very interesting.

132
00:08:20,470 --> 00:08:21,430
We got blocked.

133
00:08:21,470 --> 00:08:23,670
Now let's go to a given endpoint.

134
00:08:25,470 --> 00:08:29,670
Let's go to a given endpoint that is host x y z dot PHP.

135
00:08:30,350 --> 00:08:39,150
And once we go to this given endpoint we can hear uh that's dummy information written over here.

136
00:08:40,190 --> 00:08:46,350
Now we can try to execute a possible command over here.

137
00:08:47,750 --> 00:08:48,110
Yeah.

138
00:08:49,230 --> 00:08:59,310
And we can see when I try to say host equals to cat etc. passwd.

139
00:08:59,990 --> 00:09:02,910
Did you see we have not got blocked.

140
00:09:03,430 --> 00:09:05,430
We are not blocked over here.

141
00:09:05,430 --> 00:09:07,070
But initially we got blocked.

142
00:09:07,670 --> 00:09:08,390
Wouldn't be.

143
00:09:08,750 --> 00:09:13,950
Wouldn't it be awesome that we are able to actually read the passwd file for active server.

144
00:09:14,310 --> 00:09:16,630
So yes, definitely we can do that.

145
00:09:16,750 --> 00:09:18,750
So let's try that out.

146
00:09:19,070 --> 00:09:28,990
So let me just log in and let me create a temporary file, a PHP file that allows us to read the contents

147
00:09:28,990 --> 00:09:31,950
of the server temporarily for demonstration.

148
00:10:18,350 --> 00:10:18,830
Okay.

149
00:10:18,830 --> 00:10:22,390
So we have a file called as host x y z backup dot php.

150
00:10:22,870 --> 00:10:25,110
So this contains a PHP code.

151
00:10:25,310 --> 00:10:31,270
We can see the code says uh if is set get.

152
00:10:31,270 --> 00:10:33,310
So it is it is having a get variable.

153
00:10:33,710 --> 00:10:37,790
Uh and it is going to use a host parameter.

154
00:10:38,150 --> 00:10:43,630
Anything that has been supplied in the host parameter has been executed as a system level command with

155
00:10:43,670 --> 00:10:44,110
dig.

156
00:10:44,310 --> 00:10:46,710
So a system command will be executed.

157
00:10:46,710 --> 00:10:47,390
That is dig.

158
00:10:47,390 --> 00:10:52,910
So Dig command is basically used to do DNS lookup and whatever input has been taken from the user.

159
00:10:52,910 --> 00:10:53,630
So dig.

160
00:10:53,870 --> 00:10:55,710
If the input is google.com then dig.

161
00:10:55,710 --> 00:10:58,910
Google.com will be the command that will be executed.

162
00:10:59,310 --> 00:11:06,350
So let's go to hack dot n host x y z backup dot php.

163
00:11:08,630 --> 00:11:09,350
Uh, yes.

164
00:11:09,470 --> 00:11:13,750
So once we go here, we are able to see the current message that has been printed.

165
00:11:13,750 --> 00:11:16,120
Yes, it is getting printed from here.

166
00:11:16,120 --> 00:11:19,440
And there is a host parameter over here available.

167
00:11:19,560 --> 00:11:21,080
So let's say question mark.

168
00:11:21,480 --> 00:11:22,200
Host.

169
00:11:22,680 --> 00:11:30,080
And when we give anything into host yes I will share material for learning shell Globbing techniques

170
00:11:30,080 --> 00:11:30,560
okay.

171
00:11:30,600 --> 00:11:34,480
And when I say host google.com see the output.

172
00:11:34,760 --> 00:11:38,000
We are able to get the output of the dig command.

173
00:11:38,040 --> 00:11:41,320
So you can also run the dig command in your Linux system.

174
00:11:41,680 --> 00:11:44,960
And this is the output dig google.com.

175
00:11:45,280 --> 00:11:45,800
Sorry.

176
00:11:47,120 --> 00:11:48,800
And you will be able to get the output.

177
00:11:48,800 --> 00:11:51,640
Currently internet is disabled in my Kali Linux.

178
00:11:51,640 --> 00:11:53,560
So I'll execute this command rather here.

179
00:11:54,080 --> 00:12:01,400
And when you run the dig google.com command yes you can combine regex expression and shell globbing

180
00:12:01,400 --> 00:12:01,880
both.

181
00:12:02,400 --> 00:12:07,280
So once we do dig google.com we are able to see google.com has given an answer.

182
00:12:07,440 --> 00:12:08,800
And this is the A record.

183
00:12:08,800 --> 00:12:11,720
So basically we do we are doing simple DNS lookup.

184
00:12:12,200 --> 00:12:18,720
Now participants when I said google.com we are able to see the output of google.com and its DNS a record

185
00:12:19,000 --> 00:12:20,840
now in Linux.

186
00:12:20,880 --> 00:12:24,120
We can combine multiple commands with the help of a semicolon.

187
00:12:25,400 --> 00:12:29,440
So let me try to read the passwd file of this server.

188
00:12:29,680 --> 00:12:33,920
And bang we got blocked.

189
00:12:34,360 --> 00:12:35,560
Why did we got blocked?

190
00:12:35,560 --> 00:12:36,880
Because we performed.

191
00:12:37,160 --> 00:12:40,520
We performed an action that triggered the security solution.

192
00:12:41,160 --> 00:12:52,520
And if you go back to here and traffic sorry rules and you would be able to see here.

193
00:12:55,240 --> 00:12:55,680
Yeah.

194
00:12:58,960 --> 00:13:07,040
In the logs this is the current timestamp 843, where we have triggered a request that I just sent from

195
00:13:07,040 --> 00:13:08,280
my Macintosh.

196
00:13:08,840 --> 00:13:11,520
We are sending a request to host XYZ backup.

197
00:13:11,680 --> 00:13:16,320
This is the request that we said google.com, cat etc. passwd and we got blocked.

198
00:13:16,640 --> 00:13:17,680
Excellent.

199
00:13:18,320 --> 00:13:22,760
The security solution is working absolutely fine and it is blocking us.

200
00:13:22,920 --> 00:13:26,680
Let's bypass that using shell globbing.

201
00:13:27,000 --> 00:13:36,240
So I'm going to now say instead of question mark, question mark, question mark, let's hit enter and

202
00:13:36,240 --> 00:13:37,120
reveal this.

203
00:13:38,840 --> 00:13:39,200
Okay.

204
00:13:39,240 --> 00:13:39,560
Yes.

205
00:13:39,560 --> 00:13:42,560
Because there was a rule in cloud saying EDC password to be blocked.

206
00:13:42,560 --> 00:13:44,360
So now we use this to bypass okay.

207
00:13:44,480 --> 00:13:45,560
So let's hit enter.

208
00:13:45,560 --> 00:13:46,160
And.

209
00:13:49,720 --> 00:13:51,200
Congratulations.

210
00:13:51,840 --> 00:13:55,440
We were able to steal the passwd file.

211
00:13:55,720 --> 00:14:00,000
So the current user is bug b z h y which is logged in.

212
00:14:00,000 --> 00:14:01,440
And other users as you see.

213
00:14:01,680 --> 00:14:03,360
So congratulation participants.

214
00:14:03,720 --> 00:14:12,040
We were able to successfully trick the Cloudflare rules as well with the first shell globbing technique.

215
00:14:13,600 --> 00:14:14,040
Yes.

216
00:14:14,080 --> 00:14:17,040
Isn't that really, really awesome?

217
00:14:23,090 --> 00:14:23,450
Yes.

218
00:14:23,450 --> 00:14:24,650
Participants, are you with me?

219
00:14:24,690 --> 00:14:25,730
Able to understand?

220
00:14:25,730 --> 00:14:27,210
Everyone is able to understand.

221
00:14:34,250 --> 00:14:34,850
Awesome!

222
00:14:37,010 --> 00:14:38,010
That is awesome.

223
00:14:43,490 --> 00:14:44,250
Awesome.

224
00:14:44,250 --> 00:14:47,810
Okay, now we have just tried to retrieve a file.

225
00:14:48,330 --> 00:14:56,490
Let us see what would be what would go possibly wrong when with the help of the shell Globbing technique,

226
00:14:56,650 --> 00:15:01,890
we are able to also write write as an output over here.

227
00:15:02,250 --> 00:15:09,330
So I'm going to change Azadi ka Amrit Mahotsav written into the current file to something else.

228
00:15:09,370 --> 00:15:13,690
Okay, but before that let me make a backup of this file.

229
00:15:19,530 --> 00:15:20,570
Okay, so.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,240 --> 00:00:02,480
We have just tried to retrieve a file.

2
00:00:02,960 --> 00:00:11,120
Let us see what would be what would go possibly wrong when, with the help of the shell globbing technique,

3
00:00:11,280 --> 00:00:16,560
we are able to also write write as an output over here.

4
00:00:16,880 --> 00:00:23,960
So I'm going to change Azadi ka Amrit Mahotsav written into the current file to something else.

5
00:00:24,000 --> 00:00:24,480
Okay.

6
00:00:24,520 --> 00:00:28,320
But before that, let me make a backup of this file.

7
00:00:34,160 --> 00:00:34,600
Okay.

8
00:00:34,880 --> 00:00:38,080
So let us try to execute a command.

9
00:00:38,080 --> 00:00:39,280
We have executed a command.

10
00:00:39,320 --> 00:00:40,680
We are able to read a file.

11
00:00:40,680 --> 00:00:42,400
Now I'm going to write a file okay.

12
00:00:42,680 --> 00:00:49,280
So I'm going to say echo or let us simply say PWD present working directory.

13
00:00:49,400 --> 00:00:52,240
We are currently in this present working directory.

14
00:00:52,560 --> 00:00:54,520
So I'm going to say now echo.

15
00:00:57,120 --> 00:00:57,760
Hagged.

16
00:00:58,640 --> 00:01:05,280
And we are going to write into this directory and the given file which is which is this file.

17
00:01:05,440 --> 00:01:11,800
So we are going to change the contents of this file to the contents that we want right now which is

18
00:01:11,800 --> 00:01:12,560
echo hacked.

19
00:01:12,840 --> 00:01:14,640
And let us see the output.

20
00:01:14,960 --> 00:01:15,960
Let's hit enter.

21
00:01:18,640 --> 00:01:20,000
Uh, done.

22
00:01:20,000 --> 00:01:21,400
The command has executed.

23
00:01:21,960 --> 00:01:23,880
Now let us just try to refresh.

24
00:01:28,920 --> 00:01:30,200
Congratulations.

25
00:01:30,480 --> 00:01:36,960
You have the right access on the server that is currently protected behind Cloudflare.

26
00:01:37,440 --> 00:01:43,160
And you can see we were able to successfully overwrite the contents of the given file by executing a

27
00:01:43,160 --> 00:01:45,600
command using shell globbing technique.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 13: Techniques of Shell Globbing

1
00:00:00,320 --> 00:00:06,680
Okay so participants continuing are for from the shell globbing techniques.

2
00:00:06,680 --> 00:00:10,800
I have also uploaded the same thing on my GitHub as well.

3
00:00:11,120 --> 00:00:16,640
So when you go to my GitHub, you will be able to see a repository called as shell Globbing.

4
00:00:17,080 --> 00:00:25,280
And here in the Readme, I have uploaded two such articles so that you can read about shell globbing

5
00:00:25,600 --> 00:00:28,040
and one of the payload that we discussed.

6
00:00:28,520 --> 00:00:32,840
More versions or variants of this payloads are in the session recording.

7
00:00:32,880 --> 00:00:35,000
You can please have a look at there.

8
00:00:35,960 --> 00:00:41,840
Now continuing the same shell globbing technique, let's see one more additional technique that will

9
00:00:41,840 --> 00:00:42,960
be helpful for us.

10
00:00:43,360 --> 00:00:46,520
So I have searched for shell Globbing patterns.

11
00:00:46,680 --> 00:00:52,240
Now when we go to some of the websites, we would be able to understand that question mark matches a

12
00:00:52,240 --> 00:00:53,600
single character.

13
00:00:53,760 --> 00:01:02,020
So for example see a question mark dot txt would match car dot, txt XD and Kat dot txt but not cart

14
00:01:02,060 --> 00:01:02,660
dot txt.

15
00:01:02,700 --> 00:01:02,900
Why?

16
00:01:02,940 --> 00:01:06,500
Because we have used a single wild card over here.

17
00:01:06,780 --> 00:01:12,940
So this globbing pattern as there is only a single question mark, or a wild card or a globbing pattern,

18
00:01:12,940 --> 00:01:14,900
it will only match these two files.

19
00:01:15,180 --> 00:01:22,860
So it would guess that is if a card or txt file is present in your system, then it will match car and

20
00:01:22,860 --> 00:01:24,180
cat both the files.

21
00:01:24,780 --> 00:01:25,820
Uh, yeah.

22
00:01:25,820 --> 00:01:26,580
You can have.

23
00:01:26,700 --> 00:01:28,380
You can use a wild card more than once.

24
00:01:28,380 --> 00:01:36,020
For example p question mark p.cf will match pappa dot c fm and pi dot CFC.

25
00:01:36,460 --> 00:01:39,540
So this is one of the technique that we have and all.

26
00:01:39,820 --> 00:01:41,420
Now second is the star.

27
00:01:41,980 --> 00:01:44,580
Double star as you can see over here.

28
00:01:44,580 --> 00:01:51,380
So this given article uh gives understanding about 2 to 3 different types of globbing patterns.

29
00:01:51,620 --> 00:01:52,580
First is question mark.

30
00:01:52,580 --> 00:01:53,460
Second is star.

31
00:01:53,460 --> 00:01:55,500
And then using two stars.

32
00:01:56,300 --> 00:01:58,440
Uh, if you see more about glob patterns.

33
00:01:58,440 --> 00:02:01,720
This article did not cover all of the different types of glob patterns.

34
00:02:02,080 --> 00:02:09,200
If you see others, you would be able to see that there is a box bracket as well that is also considered

35
00:02:09,200 --> 00:02:14,400
as a glob pattern that you can read or search about.

36
00:02:14,840 --> 00:02:16,240
As you can see over here.

37
00:02:18,400 --> 00:02:19,400
As you can see over here.

38
00:02:19,400 --> 00:02:21,920
So that helps you read or find all.

39
00:02:22,200 --> 00:02:27,080
If you use a glob pattern like this, it helps you find all uppercase letters from A to Z.

40
00:02:27,240 --> 00:02:29,640
This is to find all lowercase letters.

41
00:02:29,640 --> 00:02:34,880
This is to find all numbers from 0 to 9.

42
00:02:36,720 --> 00:02:43,720
Uh, now we can also use exclamation characters and backslashes as well, because that is also considered

43
00:02:43,760 --> 00:02:45,640
a useful glob pattern.

44
00:02:46,120 --> 00:02:52,760
So let us try to see more given, uh, references and articles about it.

45
00:02:52,760 --> 00:03:00,500
So basically whatever articles or references that you are able to collect if you save all of them into

46
00:03:00,540 --> 00:03:08,460
a PDF format, similar to how we save JavaScript basics document, and you give it to our llama model.

47
00:03:10,660 --> 00:03:11,060
Yeah.

48
00:03:11,100 --> 00:03:11,740
It's here.

49
00:03:12,340 --> 00:03:12,780
Let me see.

50
00:03:12,780 --> 00:03:13,420
It's running.

51
00:03:15,060 --> 00:03:16,460
Yes, llama is up.

52
00:03:16,700 --> 00:03:18,060
My docker is also up.

53
00:03:23,780 --> 00:03:25,900
Yeah, llama is up and running.

54
00:03:26,180 --> 00:03:29,020
So you would be able to go to the workspace.

55
00:03:29,500 --> 00:03:35,780
You can have llama model set it up correctly with the glob patterns data knowledge.

56
00:03:35,780 --> 00:03:43,340
And then you can utilize that to generate various different complex uh payloads or glob patterns to

57
00:03:43,380 --> 00:03:44,540
do a WAF bypass.

58
00:03:44,580 --> 00:03:52,380
Okay, so here are some of the, uh, some of the most common glob pattern techniques that I want to

59
00:03:52,420 --> 00:03:54,980
show, show, and share with you participants.

60
00:03:55,720 --> 00:03:59,640
are that is going to be helpful for you to do bypasses.

61
00:03:59,680 --> 00:04:00,040
Okay.

62
00:04:00,360 --> 00:04:05,200
So I'm going to first show open up my terminal.

63
00:04:10,920 --> 00:04:11,480
Okay.

64
00:04:11,480 --> 00:04:15,560
So the first technique we have already seen that is wild card characters.

65
00:04:16,360 --> 00:04:22,160
So when I go ahead and type cat ATC passwd we are able to see the output of the passwd command over

66
00:04:22,160 --> 00:04:22,600
here.

67
00:04:22,800 --> 00:04:28,680
So the wild card character question mark is helping us to identify the given file.

68
00:04:28,680 --> 00:04:30,280
So what Linux file system is doing.

69
00:04:30,280 --> 00:04:35,960
It is trying to find files that contains or matches very closely these words.

70
00:04:35,960 --> 00:04:39,640
As you can see over here, which is a question mark, question mark.

71
00:04:40,320 --> 00:04:42,200
And we are able to retrieve that file.

72
00:04:42,360 --> 00:04:50,720
And we saw that how firewall signature or rules, if are not written appropriately then the attacker

73
00:04:50,720 --> 00:04:54,820
would be able to read these files as we were able to do in this case.

74
00:04:55,300 --> 00:04:58,780
Now there is another glob pattern which is of single quotes.

75
00:04:59,020 --> 00:05:06,820
So if you see this given payload over here, I have divided the same command with single quotes.

76
00:05:06,820 --> 00:05:08,540
You can see be single quote.

77
00:05:08,580 --> 00:05:15,060
I single quote and see single quote, a single quote t, then space etc. passwd.

78
00:05:15,140 --> 00:05:20,620
So I'm going to copy this command, and I'm going to show you that this is a valid command or no.

79
00:05:20,780 --> 00:05:29,220
This looks very odd or weird to see as of now, but Linux File System understands it.

80
00:05:29,260 --> 00:05:30,460
Understands it.

81
00:05:30,500 --> 00:05:31,380
Absolutely.

82
00:05:31,540 --> 00:05:32,020
Okay.

83
00:05:32,060 --> 00:05:35,620
So I'm going to say hit enter for this command.

84
00:05:35,620 --> 00:05:37,260
And excellent.

85
00:05:37,500 --> 00:05:40,460
We are able to retrieve the same file.

86
00:05:40,660 --> 00:05:47,140
That means if we use single quotes which we saw into one of the articles as well on Google recently,

87
00:05:47,140 --> 00:05:51,780
that we can use single quotes and double quotes, then we are able to also read the given file.

88
00:05:51,960 --> 00:06:01,440
This technique is going to also help us identify, uh, or read this file from the server, even if

89
00:06:01,440 --> 00:06:03,680
it has been protected by a firewall.

90
00:06:04,720 --> 00:06:07,800
Next technique is using empty variables.

91
00:06:07,920 --> 00:06:11,160
So I'm using I'm using empty variable dollar q.

92
00:06:11,560 --> 00:06:16,880
So if there are any different types of uh instead of you you wants to you, you want to use any different

93
00:06:16,880 --> 00:06:18,200
variable that is also fine.

94
00:06:18,520 --> 00:06:23,720
That means if you go and say cat etc. passwd dollar you.

95
00:06:24,120 --> 00:06:32,800
This is a glob pattern where you have not initialized a variable you but you are using it.

96
00:06:32,800 --> 00:06:34,520
So what does Linux system does?

97
00:06:34,520 --> 00:06:36,400
It simply ignores it.

98
00:06:36,800 --> 00:06:40,320
But does it consider it as a valid command?

99
00:06:40,320 --> 00:06:41,000
Let us see.

100
00:06:41,680 --> 00:06:42,880
Let's hit enter.

101
00:06:46,240 --> 00:06:53,060
And yes it considered it considers its this as a valid command.

102
00:06:53,580 --> 00:07:01,700
This is extremely helpful when there is a regex match condition by a mod security or any other cloud

103
00:07:01,700 --> 00:07:07,580
firewall as such, where it is trying to block the given payload that we are going to supply.

104
00:07:07,740 --> 00:07:11,820
So if you use any variable, it works instead of you.

105
00:07:12,020 --> 00:07:14,540
You can use any other variables of your choice.

106
00:07:14,540 --> 00:07:16,940
I'm currently using a dummy variable dollar U.

107
00:07:17,300 --> 00:07:21,020
We have not initialized the variable anywhere, but we are attempting to use it.

108
00:07:21,020 --> 00:07:24,140
Hence Linux system simply ignores it.

109
00:07:25,300 --> 00:07:25,980
Excellent.

110
00:07:26,380 --> 00:07:30,660
Let's see the next one which is escape sequence or backslash.

111
00:07:30,860 --> 00:07:35,020
We just read read here about.

112
00:07:37,380 --> 00:07:37,660
Here.

113
00:07:37,700 --> 00:07:38,180
Here.

114
00:07:43,340 --> 00:07:45,060
About Backslashes.

115
00:07:45,380 --> 00:07:49,220
Yeah, we can use Backslashes as well.

116
00:07:49,250 --> 00:07:54,170
That can be helpful for us as an complement in shell globbing.

117
00:07:54,370 --> 00:08:01,290
So if you see this command, you can execute this command or without the round brackets as well.

118
00:08:01,290 --> 00:08:04,410
But I'm just going to try to execute it like this.

119
00:08:04,890 --> 00:08:08,650
And you would be able to see that this command actually works.

120
00:08:08,730 --> 00:08:12,610
So what we have done is the command is broken with backslashes.

121
00:08:12,890 --> 00:08:18,050
And wherever there is a forward slash we have added that because that is how a directory etc. would

122
00:08:18,050 --> 00:08:18,690
be found.

123
00:08:18,850 --> 00:08:25,410
So backslash sorry forward slash backslash then backslash again forward slash.

124
00:08:25,410 --> 00:08:29,490
So this directory becomes etc. and then passwd let's hit enter.

125
00:08:29,890 --> 00:08:32,250
And awesome.

126
00:08:32,530 --> 00:08:36,930
Did you see that the command has executed successfully.

127
00:08:37,370 --> 00:08:40,450
Let us see once more and hit enter.

128
00:08:40,810 --> 00:08:48,310
And we are able to see that the command has successfully executed over here.

129
00:08:49,110 --> 00:08:49,870
Are you all with me?

130
00:08:49,910 --> 00:08:52,990
Participants able to understand?

131
00:08:55,790 --> 00:08:58,430
Uh, give me a quick heads up if you all are with me.

132
00:08:58,430 --> 00:08:59,110
So far.

133
00:09:01,950 --> 00:09:02,390
Great.

134
00:09:06,950 --> 00:09:07,630
Wonderful.

135
00:09:08,030 --> 00:09:15,990
Now, let us try out all of them one by one and see how does the firewall behaves.

136
00:09:16,030 --> 00:09:19,830
Because we have understood that all of these are valid commands.

137
00:09:20,070 --> 00:09:27,030
So I'm going to just turn on my Linux machine, which contains the mod security that is protecting the

138
00:09:27,030 --> 00:09:28,390
Apache server here.

139
00:09:28,670 --> 00:09:35,510
So when I say yeah, when I execute this command, it gets executed without any problem.

140
00:09:35,510 --> 00:09:41,990
And when I try to execute this command, it will block because it is successfully detecting this.

141
00:09:42,030 --> 00:09:42,430
Okay.

142
00:09:42,470 --> 00:09:44,750
So we are running the mod security firewall.

143
00:09:44,750 --> 00:09:51,050
And as we have discussed majority of the organizations which are which are having commercial where.

144
00:09:51,090 --> 00:10:00,650
Softwares or firewalls or any other security vendors utilizes Mod security baseline core rule sets to

145
00:10:00,690 --> 00:10:03,210
develop additional rules onto it.

146
00:10:03,210 --> 00:10:09,810
That means if you are able to, with research, identify bypasses for Mod security, the likelihood

147
00:10:09,810 --> 00:10:13,370
is more that these would work on other targets.

148
00:10:13,690 --> 00:10:14,330
All right.

149
00:10:14,330 --> 00:10:20,370
So now let us go ahead and try the techniques that we have just identified and see if that would work.

150
00:10:20,410 --> 00:10:20,810
Okay.

151
00:10:21,010 --> 00:10:23,410
So I'm going to try the single quote technique first.

152
00:10:23,970 --> 00:10:30,730
And I want to know from participants in the chat, uh, can you just guess what would happen when we

153
00:10:30,770 --> 00:10:31,530
hit enter.

154
00:10:31,650 --> 00:10:33,210
Would that be bypass?

155
00:10:33,250 --> 00:10:35,210
Would it work or would we get blocked?

156
00:10:36,690 --> 00:10:43,530
So let's take a quick acknowledgement from participants and then we will see what is the outcome.

157
00:10:53,670 --> 00:10:57,430
Okay, so should execute work, work.

158
00:10:57,470 --> 00:10:58,390
It will work.

159
00:10:58,790 --> 00:10:59,710
Very nice.

160
00:10:59,710 --> 00:11:00,750
Pass allowed.

161
00:11:01,670 --> 00:11:02,190
Excellent.

162
00:11:02,190 --> 00:11:07,790
So most likely all participants have said are positive that it should work.

163
00:11:07,790 --> 00:11:09,590
Let's hit enter and see the outcome.

164
00:11:09,630 --> 00:11:09,950
Okay.

165
00:11:09,950 --> 00:11:11,070
So I'm going to hit enter.

166
00:11:11,070 --> 00:11:12,750
Now please observe.

167
00:11:13,790 --> 00:11:14,750
We got blocked.

168
00:11:15,990 --> 00:11:17,910
Uh, this is weird.

169
00:11:18,150 --> 00:11:19,270
Wouldn't you agree?

170
00:11:19,270 --> 00:11:24,350
Let's go ahead in the logs and see what exactly happened.

171
00:11:24,350 --> 00:11:26,950
And how did it identify it okay.

172
00:11:27,230 --> 00:11:29,990
So let's go here.

173
00:11:37,710 --> 00:11:38,270
Yes.

174
00:11:40,190 --> 00:11:42,390
If you see here, then what?

175
00:11:42,430 --> 00:11:48,930
What most likely has happened here participants that it is blocking our request with the help of this

176
00:11:48,930 --> 00:11:50,370
configuration file.

177
00:11:50,490 --> 00:11:53,170
So what it did, it matched some data.

178
00:11:53,170 --> 00:11:58,810
So if you see here matched data etc. passwd found within the arguments this.

179
00:11:59,170 --> 00:11:59,650
Okay.

180
00:11:59,650 --> 00:12:00,930
So what happened exactly.

181
00:12:00,930 --> 00:12:08,290
It matched that there is cat passwd in the current argument because of which it blocked us.

182
00:12:08,650 --> 00:12:21,690
So now I think if we copy this payload and go to Lama, which is our AI model, and ask it to, uh,

183
00:12:22,890 --> 00:12:27,970
to basically generate a new version of the payload with other globbing techniques, then let us see

184
00:12:27,970 --> 00:12:29,290
what is the outcome that we get.

185
00:12:29,330 --> 00:12:29,650
Okay.

186
00:12:29,690 --> 00:12:34,770
But before we do that, let us try the second technique and let's see what is the outcome okay.

187
00:12:38,890 --> 00:12:42,270
Uh, what do you think, Guys.

188
00:12:43,030 --> 00:12:44,750
What will happen for this payload?

189
00:12:47,390 --> 00:12:48,550
Would it get blocked?

190
00:12:48,830 --> 00:12:59,230
Okay, so now we are getting the response blocked because it contains usual etc. passwd uh string.

191
00:12:59,390 --> 00:13:01,950
So most likely it might get blocked.

192
00:13:01,950 --> 00:13:02,630
Someone.

193
00:13:02,670 --> 00:13:04,590
Some participants are saying it will work.

194
00:13:04,670 --> 00:13:05,910
Okay let's try it.

195
00:13:06,030 --> 00:13:06,550
Try it out.

196
00:13:06,550 --> 00:13:07,030
What happens?

197
00:13:07,070 --> 00:13:07,230
Okay.

198
00:13:07,230 --> 00:13:08,830
So I'm going to hit enter and.

199
00:13:12,190 --> 00:13:15,230
Observe how we got blocked once again.

200
00:13:15,830 --> 00:13:16,270
Okay.

201
00:13:16,430 --> 00:13:17,550
We have got blocked.

202
00:13:17,550 --> 00:13:18,030
And.

203
00:13:23,870 --> 00:13:24,230
Okay.

204
00:13:24,230 --> 00:13:26,590
Let us just enter once again.

205
00:13:28,070 --> 00:13:28,630
Yeah.

206
00:13:28,630 --> 00:13:30,030
We have got blocked.

207
00:13:30,430 --> 00:13:31,030
And.

208
00:13:42,570 --> 00:13:43,010
Yeah.

209
00:13:43,050 --> 00:13:46,130
This did not got blocked but this got blocked.

210
00:13:46,450 --> 00:13:49,650
So we can confirm that we are getting indeed blocked.

211
00:13:50,090 --> 00:13:51,730
We just restart this error log.

212
00:13:52,130 --> 00:13:53,970
Yeah we are getting indeed blocked.

213
00:13:53,970 --> 00:13:56,850
And it is not working because it is identifying.

214
00:13:56,890 --> 00:13:57,170
Yeah.

215
00:13:57,210 --> 00:14:03,610
Here you can see cat etc. passwd edc passwd found within passwd empty variable.

216
00:14:03,810 --> 00:14:05,210
Okay no problem.

217
00:14:05,210 --> 00:14:06,250
Let us go ahead.

218
00:14:06,290 --> 00:14:07,490
Try the next technique.

219
00:14:12,170 --> 00:14:15,450
And let me just go ahead and hit enter and observe.

220
00:14:15,450 --> 00:14:16,490
What is the response.

221
00:14:16,930 --> 00:14:19,610
And we can see that we again got blocked.

222
00:14:20,730 --> 00:14:26,170
If you see the outcome or output over here we can see cat EDC passwd is there.

223
00:14:26,330 --> 00:14:29,330
And it was able to detect it appropriately.

224
00:14:29,570 --> 00:14:34,530
Uh, that this is something which is not very common in uh we have got blocked.

225
00:14:35,770 --> 00:14:36,010
Yes.

226
00:14:36,010 --> 00:14:36,930
Participants.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,480 --> 00:00:08,000
Let's go to Olama and take help from it and then see how does the firewall behave.

2
00:00:08,040 --> 00:00:08,400
Okay.

3
00:00:08,720 --> 00:00:12,400
So I'm going to go web is parsing the input.

4
00:00:12,400 --> 00:00:13,200
That is correct.

5
00:00:13,920 --> 00:00:14,920
Absolutely correct.

6
00:00:14,920 --> 00:00:18,800
So I'm going to go and take help.

7
00:00:22,400 --> 00:00:22,760
Hmm.

8
00:00:24,560 --> 00:00:25,800
Let's go to a new chat.

9
00:00:26,160 --> 00:00:27,360
Enable the web search.

10
00:00:27,640 --> 00:00:28,040
Hi.

11
00:00:29,160 --> 00:00:38,400
I'm not setting up a system prompt, but I'm rather setting a user prompt behave like a Unix six.

12
00:00:40,680 --> 00:00:44,640
And Linux export.

13
00:00:48,680 --> 00:00:58,360
Understand the below shell globbing techniques and use the.

14
00:01:00,520 --> 00:01:05,000
Web Search option to look for more.

15
00:01:05,400 --> 00:01:11,040
More tech know if possible.

16
00:01:13,680 --> 00:01:15,880
Search and techniques if possible.

17
00:01:20,400 --> 00:01:38,360
And generate some mutations which are valid working commands that shell will interpret interpret.

18
00:01:40,080 --> 00:01:47,400
Okay now let's paste this and give output.

19
00:01:47,640 --> 00:01:48,560
Let's hit enter.

20
00:01:50,280 --> 00:01:53,680
Oh I think I should have chosen a new chart.

21
00:01:57,880 --> 00:01:58,320
Okay.

22
00:01:58,840 --> 00:02:00,360
Anyways it is trying to google.

23
00:02:36,230 --> 00:02:38,070
Okay, let's wait for the output.

24
00:02:58,070 --> 00:02:58,390
Okay.

25
00:02:58,470 --> 00:03:04,790
It gave us some outcome, as we can see over here where we can see cat EDC PA would look for these files

26
00:03:04,790 --> 00:03:13,150
and all of these stuff, and it basically explained us all of all of those for it, uh, explained it

27
00:03:13,350 --> 00:03:17,190
to us in a very nice manner, but it did not generate a mutation.

28
00:03:17,190 --> 00:03:34,270
So let's say use all of all of the above techniques and generate a mutated, mutated payload that uses

29
00:03:34,470 --> 00:03:36,790
all of them.

30
00:03:38,310 --> 00:03:38,550
Okay.

31
00:03:38,550 --> 00:03:39,470
Let's say command.

32
00:03:46,430 --> 00:03:46,790
Okay.

33
00:03:46,790 --> 00:03:48,030
So let's wait for this.

34
00:04:06,700 --> 00:04:07,700
What a challenge here.

35
00:04:07,700 --> 00:04:09,460
It's a mutated version of the payload.

36
00:04:09,740 --> 00:04:10,180
Wow.

37
00:04:10,540 --> 00:04:11,500
Did you see this?

38
00:04:13,260 --> 00:04:15,420
Let's try this payload.

39
00:04:16,260 --> 00:04:18,980
First, let us see if this payload is in valid payload.

40
00:04:18,980 --> 00:04:20,020
And does it work?

41
00:04:20,420 --> 00:04:20,860
Okay.

42
00:04:25,940 --> 00:04:26,980
Very nice.

43
00:04:27,860 --> 00:04:32,100
And let us try to see if this is a valid payload.

44
00:04:32,100 --> 00:04:33,220
And does it work?

45
00:04:39,780 --> 00:04:40,100
Yes.

46
00:04:40,100 --> 00:04:42,380
I will share that on the chat in just a second.

47
00:04:43,740 --> 00:04:44,780
Uh, okay.

48
00:04:44,820 --> 00:04:50,940
We have received a error bin cat EDC WG John shadow, not a directory.

49
00:04:50,940 --> 00:04:51,340
Okay.

50
00:04:51,460 --> 00:04:53,340
Let me see once again.

51
00:05:08,460 --> 00:05:08,780
She.

52
00:05:10,060 --> 00:05:10,700
John.

53
00:05:12,780 --> 00:05:13,180
Okay.

54
00:05:14,220 --> 00:05:15,380
Not a directory.

55
00:05:15,500 --> 00:05:16,660
Let's try it out here.

56
00:05:23,620 --> 00:05:29,380
Okay, so what has happened here is replace dollar you with John since he wants to search files owned

57
00:05:29,380 --> 00:05:29,900
by John.

58
00:05:29,900 --> 00:05:30,100
Okay.

59
00:05:30,100 --> 00:05:31,460
We don't want to do that.

60
00:05:32,100 --> 00:05:32,420
Uh, okay.

61
00:05:32,420 --> 00:05:35,300
So it is basically trying to search directories owned by John.

62
00:05:35,300 --> 00:05:36,140
We don't want to do that.

63
00:05:36,140 --> 00:05:40,140
So I'm going to write a new prompt and ask it to give me a new version of the payload.

64
00:05:40,140 --> 00:05:40,500
Okay.

65
00:05:40,740 --> 00:05:46,700
But uh, so, so it will basically give me a new version of the payload that does not use John over

66
00:05:46,700 --> 00:05:48,980
there, because of which we are receiving an error.

67
00:05:49,100 --> 00:05:55,260
So if you do some more trial and error, okay, then you would get an command which uh, sorry, which

68
00:05:55,300 --> 00:05:57,100
an output which looks like this.

69
00:05:57,100 --> 00:06:01,140
This is the output that I have received from the same output.

70
00:06:01,140 --> 00:06:04,540
And the output the outcome is or the output is something like this.

71
00:06:06,050 --> 00:06:07,850
Forward slash backslash.

72
00:06:09,890 --> 00:06:15,490
B single quote I single quote n that is bin.

73
00:06:15,970 --> 00:06:19,810
Then dollar u which is an empty variable.

74
00:06:20,250 --> 00:06:30,570
Backslash forward slash c single quote a single quote t, and then again using an empty variable dollar

75
00:06:30,610 --> 00:06:32,730
u and make a space.

76
00:06:32,730 --> 00:06:41,650
Because we have completed our bin cat command backslash, forward slash and e single quote single quote

77
00:06:41,690 --> 00:06:57,250
c then we use a backslash forward slash p a s s, w d, and then an empty variable like this.

78
00:06:57,730 --> 00:07:03,090
Okay, so this is the outcome that I received from by generating multiple trial errors.

79
00:07:03,090 --> 00:07:05,690
And let us see if this is a valid command or no first.

80
00:07:05,690 --> 00:07:07,130
Okay, let's hit enter.

81
00:07:08,410 --> 00:07:09,010
Awesome.

82
00:07:09,210 --> 00:07:10,130
Did you see that?

83
00:07:10,650 --> 00:07:12,090
It's a valid command.

84
00:07:12,090 --> 00:07:19,330
So this is a mutation or mutated version of the payload that we have generated with the help of all

85
00:07:19,370 --> 00:07:23,170
the combinations of our shell globbing technique.

86
00:07:23,330 --> 00:07:24,050
Now, let us see.

87
00:07:24,050 --> 00:07:26,250
How does it behave with this?

88
00:07:27,650 --> 00:07:30,050
Let's paste it here and hit enter.

89
00:07:30,250 --> 00:07:32,770
Congratulations, participants.

90
00:07:32,770 --> 00:07:40,170
We have an absolutely working version of the mutated payload for us, which is a valid command.

91
00:07:40,970 --> 00:07:42,370
Isn't that really awesome?

92
00:07:45,170 --> 00:07:45,850
Please let me know.

93
00:07:45,850 --> 00:07:48,450
Participants, are you all with me?

94
00:07:58,130 --> 00:07:58,690
Yes.

95
00:07:58,690 --> 00:08:00,290
Everyone is able to understand.

96
00:08:07,320 --> 00:08:07,640
Mm.

97
00:08:09,240 --> 00:08:09,800
Yes.

98
00:08:10,000 --> 00:08:11,040
Did you see that?

99
00:08:11,480 --> 00:08:21,080
Uh, the firewall did not recognize now the mutated version of the command, because of which we saw

100
00:08:21,080 --> 00:08:23,480
that it is not blocking us anymore.

101
00:08:23,800 --> 00:08:27,600
If we see here and it's a valid command.

102
00:08:29,800 --> 00:08:32,880
Yes, it is absolutely a valid command.

103
00:08:32,880 --> 00:08:39,440
As we can see here, I've also pasted the command on the chat that you can have a look at, and this

104
00:08:39,440 --> 00:08:41,280
will be helpful for you in future as well.

105
00:08:41,280 --> 00:08:50,040
Participants where uh if you encounter any firewall this then the firewall is definitely not going to

106
00:08:50,040 --> 00:08:52,760
understand this mutation version of the payload.

107
00:08:53,800 --> 00:08:55,080
Explain this.

108
00:08:55,080 --> 00:09:01,280
Or you can say generate again with out John User.

109
00:09:04,640 --> 00:09:06,680
And you will be able to get more responses.

110
00:09:06,760 --> 00:09:12,640
Try do trial and error with all of those responses, and I'm sure that you would be able to, uh, reach

111
00:09:12,640 --> 00:09:16,560
to this given payload that we have just generated.

112
00:09:16,600 --> 00:09:21,760
I'm going to anyways, uh, save this on the GitHub.

113
00:09:21,760 --> 00:09:27,840
So from where you can copy paste this and also run it onto your terminal and try it out as well.

114
00:09:31,240 --> 00:09:31,640
Uh, yes.

115
00:09:31,640 --> 00:09:32,480
Participants.

116
00:09:32,680 --> 00:09:34,840
Everyone is with me able to understand.

117
00:09:37,640 --> 00:09:38,560
Please confirm.

118
00:09:41,520 --> 00:09:42,120
Yes.

119
00:09:42,600 --> 00:09:43,240
Okay.

120
00:09:43,280 --> 00:09:43,960
Excellent.

121
00:09:46,520 --> 00:09:47,280
Excellent.

122
00:09:50,240 --> 00:09:50,640
Yeah.

123
00:09:50,640 --> 00:09:52,680
So now let us proceed forward.

124
00:09:54,480 --> 00:09:55,960
Uh, let's wait for this output.

125
00:09:55,960 --> 00:10:02,960
It has looked up 50 websites, and you can see Linux bash geeks for geeks and other websites to generate

126
00:10:02,960 --> 00:10:03,800
the mutation.

127
00:10:07,750 --> 00:10:08,190
Okay.

128
00:10:08,390 --> 00:10:09,630
And this is the mutation.

129
00:10:09,630 --> 00:10:13,230
So you can basically try this mutation once again to see if that works.

130
00:10:13,230 --> 00:10:19,830
If it doesn't work, try to give more prompts, uh, to basically generate a newer version of the payload.

131
00:10:19,870 --> 00:10:20,270
Okay.

132
00:10:22,830 --> 00:10:23,750
How's this?

133
00:10:25,750 --> 00:10:26,310
Okay.

134
00:10:26,350 --> 00:10:31,350
And it will be able to generate newer versions of the payload to you automatically that you can use

135
00:10:31,350 --> 00:10:33,110
with multiple changes.

136
00:10:33,670 --> 00:10:39,070
Uh, with trials and error, you would be able to generate these same and better versions of the mutated

137
00:10:39,070 --> 00:10:39,990
payload as well.

138
00:10:41,910 --> 00:10:42,390
Okay.

139
00:10:42,430 --> 00:10:44,230
So this was about shell globbing.

140
00:10:44,230 --> 00:10:46,270
We have understood shell globbing.

141
00:10:48,350 --> 00:10:49,030
Uh, yes.

142
00:10:49,310 --> 00:10:56,150
Uh, if you would not be able to copy the commands from here, there is a restriction, uh, host restriction.

143
00:10:56,150 --> 00:11:00,870
But don't worry, I'll paste all of the commands on GitHub so you can get it from there.

144
00:11:08,030 --> 00:11:08,470
Okay.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 14. LLMs & Automation

1
00:00:00,360 --> 00:00:03,120
Now participants, we did this manually.

2
00:00:03,480 --> 00:00:11,840
Let us try to use LM, which is our lemma, to basically understand all of this that is in the current

3
00:00:11,840 --> 00:00:16,240
chapter, and then give us some commands that would be useful for us okay.

4
00:00:16,400 --> 00:00:17,880
So I'm going to go here.

5
00:00:18,720 --> 00:00:19,440
Um, yeah.

6
00:00:19,440 --> 00:00:24,480
I also wanted to show you, uh, a setting that you can make in open web UI.

7
00:00:24,880 --> 00:00:27,200
So you can go to the controls.

8
00:00:27,240 --> 00:00:27,640
Sorry.

9
00:00:27,680 --> 00:00:31,120
You can go to the admin admin panel.

10
00:00:31,600 --> 00:00:32,600
Go to settings.

11
00:00:33,120 --> 00:00:34,240
Go to web search.

12
00:00:34,840 --> 00:00:40,280
Enable the web search if it is disabled and set your search engine to DuckDuckGo.

13
00:00:40,520 --> 00:00:46,080
It wouldn't ask you for an API key, and you can use as many as search queries that you want to do with

14
00:00:46,080 --> 00:00:48,560
DuckDuckGo, as in search engine.

15
00:00:48,840 --> 00:00:51,360
You can also mention the result counts that you want.

16
00:00:51,400 --> 00:00:59,680
So up to ten results and ten concurrent requests to, uh, be below the threshold to avoid rate limit

17
00:01:00,000 --> 00:01:00,520
hits.

18
00:01:01,000 --> 00:01:01,720
Save this.

19
00:01:02,000 --> 00:01:08,360
And now your olama is ready to interact with the web.

20
00:01:09,240 --> 00:01:10,200
Here's a question.

21
00:01:10,360 --> 00:01:12,600
Can you check what dot n does?

22
00:01:12,880 --> 00:01:14,640
So I've checked out dot n.

23
00:01:14,720 --> 00:01:16,120
And here's what I found.

24
00:01:16,160 --> 00:01:20,400
It's in penetration testing company that helps businesses protect themselves from cyber threats.

25
00:01:20,640 --> 00:01:24,720
Services are pen test compliance advisory services and so on.

26
00:01:25,080 --> 00:01:27,320
Can you find all functionalities of active.

27
00:01:28,080 --> 00:01:30,160
Then it says it gives services.

28
00:01:30,160 --> 00:01:31,520
It gives training.

29
00:01:31,680 --> 00:01:33,440
It has its own tools.

30
00:01:33,440 --> 00:01:35,040
It gives consulting.

31
00:01:35,200 --> 00:01:36,840
It has features like blocks.

32
00:01:36,840 --> 00:01:37,760
That is right.

33
00:01:37,800 --> 00:01:40,560
We have some white papers, case studies uploaded on the website.

34
00:01:40,560 --> 00:01:42,040
And we also do webinars.

35
00:01:42,160 --> 00:01:43,200
Absolutely right.

36
00:01:43,600 --> 00:01:46,840
Then I asked what is the trending news in cybersecurity today.

37
00:01:47,000 --> 00:01:52,880
So it gave me news about following attacks or things that are currently happening.

38
00:01:53,120 --> 00:01:59,480
So participants we are simply utilizing the DuckDuckGo search engine with our locally created Lama.

39
00:01:59,760 --> 00:02:04,880
And it is utilizing or doing a web search as well and bringing the results over here.

40
00:02:04,920 --> 00:02:11,400
Okay, so as you can see over here, this is the feature that you need to turn on once you are here.

41
00:02:11,400 --> 00:02:15,120
And then it will start pulling the results from for you from DuckDuckGo?

42
00:02:15,320 --> 00:02:22,760
So let's say what's trending today on Product Hunt.

43
00:02:26,440 --> 00:02:31,160
So Product Hunt is a website that basically lists down the top, uh, new products.

44
00:02:35,240 --> 00:02:36,080
Or startups.

45
00:02:42,520 --> 00:02:42,800
Okay.

46
00:02:42,800 --> 00:02:44,400
So it is basically again.

47
00:02:46,880 --> 00:02:48,440
Yes, we can do Dawking as well.

48
00:02:48,440 --> 00:02:49,760
That is absolutely right.

49
00:02:49,960 --> 00:02:54,080
So I will show you some docs as well that we will put here, and you will get the results directly on

50
00:02:54,080 --> 00:02:54,600
your dashboard.

51
00:02:54,600 --> 00:02:58,680
You don't need to go to Google or open up a new tab.

52
00:02:58,680 --> 00:03:00,440
You can do it directly from here.

53
00:03:00,840 --> 00:03:07,320
Run docs and get their responses directly here for subdomains.

54
00:03:15,120 --> 00:03:17,560
Okay, so let me just refresh this.

55
00:03:17,560 --> 00:03:20,680
Not sure what what happened now.

56
00:03:21,560 --> 00:03:25,560
Okay, let me just disable the MCP server.

57
00:03:25,960 --> 00:03:29,200
I think my system started in my IP has changed because of this.

58
00:03:29,200 --> 00:03:30,760
The connection is failing.

59
00:03:31,440 --> 00:03:36,400
So let me just say, okay, I'm not going to use it for some time.

60
00:03:38,120 --> 00:03:38,480
Yeah.

61
00:03:43,040 --> 00:03:44,320
Let's start a new chat.

62
00:03:45,240 --> 00:03:45,640
Hi.

63
00:03:49,080 --> 00:04:00,840
What does active dot n does and what are their latest services or trainings?

64
00:04:06,240 --> 00:04:07,440
Uh, just a simple search.

65
00:04:07,520 --> 00:04:09,240
Uh, you can also search for.

66
00:04:11,320 --> 00:04:13,000
Uh, other things as well.

67
00:04:13,000 --> 00:04:16,760
Is there a risk of exposing my usage history when we integrated web search?

68
00:04:17,040 --> 00:04:26,320
Uh, technically, no, it is because, uh, you have the entire control of Olama, uh, with you locally.

69
00:04:26,320 --> 00:04:28,520
Everything is on your Docker container.

70
00:04:28,680 --> 00:04:32,440
So so basically you have the entire control over here.

71
00:04:32,440 --> 00:04:40,480
But yes, when you would be searching about some contents and it uses some, uh, resources from the

72
00:04:40,520 --> 00:04:49,000
internet that are not genuine, then you might get some in accurate or inappropriate outcome or output.

73
00:04:49,320 --> 00:04:55,040
So that's it, because it is only fetching the requests and responses and giving it to you.

74
00:04:55,040 --> 00:04:59,880
It is not sharing any information to any third party or external services.

75
00:05:00,240 --> 00:05:04,720
Uh, unlike how ChatGPT or Copilot or cloud AI does.

76
00:05:04,720 --> 00:05:06,880
So you have the entire control of this.

77
00:05:06,880 --> 00:05:12,320
But yes, some of the results that you might not intend to see might appear because it is simply doing

78
00:05:12,320 --> 00:05:15,360
a web crawling over here to give you the results.

79
00:05:16,960 --> 00:05:17,880
Uh, yes.

80
00:05:17,880 --> 00:05:19,760
I hope that answers the question.

81
00:05:23,200 --> 00:05:23,520
Okay.

82
00:05:23,520 --> 00:05:24,040
Thank you.

83
00:05:25,080 --> 00:05:29,480
Uh, we can see that it looked 20 websites or 20 endpoints.

84
00:05:29,480 --> 00:05:33,240
Can you see here active I think effect courses LinkedIn page.

85
00:05:33,680 --> 00:05:35,880
And then again internship portal.

86
00:05:35,920 --> 00:05:40,960
The current course AI for cybersecurity Boot camp and everything is being listed over here.

87
00:05:41,160 --> 00:05:46,360
Now similarly, you can check for new things that are happening around the world for Apple.

88
00:05:46,360 --> 00:05:53,000
So did Apple do any new acquisitions recently?

89
00:05:53,640 --> 00:05:54,120
Okay.

90
00:05:54,160 --> 00:05:54,960
Why this?

91
00:05:54,960 --> 00:06:04,440
Because participants, you know, large scope programs like Apple, Google, Facebook, Yahoo, they

92
00:06:04,440 --> 00:06:08,200
also have their acquisitions in scope for their bug bounty program.

93
00:06:08,200 --> 00:06:14,920
That means if you hunt a bug, if you want to hunt a bug for Apple's bug bounty program, you can actually

94
00:06:14,960 --> 00:06:16,920
hunt bugs on Shazam.

95
00:06:17,200 --> 00:06:26,240
You can hunt bugs on, uh, turing.com or beats or any other of their services which are not commonly

96
00:06:26,240 --> 00:06:27,280
looked by people.

97
00:06:27,520 --> 00:06:34,640
I'll show you many examples as such, uh, as well, wherein I have reported bugs on 100 of their acquisitions,

98
00:06:34,640 --> 00:06:37,360
which potentially people will not trying to identify.

99
00:06:37,520 --> 00:06:42,960
And it allowed me to identify those quick bugs which were overlooked by others.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:01,720 --> 00:00:03,680
So until this query is happening.

2
00:00:30,360 --> 00:00:37,200
Okay, so Turing.com, as you can see over here, it is a asset of Apple.

3
00:00:37,240 --> 00:00:39,120
And under their Apple Bug bounty program.

4
00:00:39,120 --> 00:00:44,040
And you can see they have reported $500 for an issue that I reported to them.

5
00:00:44,040 --> 00:00:45,640
So what is Tricom.

6
00:00:45,680 --> 00:00:47,920
Tricom belongs to Apple.

7
00:00:48,200 --> 00:00:49,880
How how would I know that?

8
00:00:49,920 --> 00:00:50,760
How would I know that?

9
00:00:50,760 --> 00:00:51,360
Simple.

10
00:00:51,400 --> 00:00:54,720
Doing an acquisition search about it next.

11
00:00:55,040 --> 00:00:57,600
Uh, shazam.com.

12
00:01:01,280 --> 00:01:03,120
Okay, so here you can see.

13
00:01:06,520 --> 00:01:09,730
Apple is pleased to award you $6,000 for reporting an issue.

14
00:01:09,730 --> 00:01:11,810
And the bug was on Shazam.

15
00:01:11,850 --> 00:01:12,490
Com.

16
00:01:12,530 --> 00:01:13,810
Let me show you the report.

17
00:01:14,450 --> 00:01:15,850
Duck duck duck duck duck duck.

18
00:01:18,610 --> 00:01:19,010
Yeah.

19
00:01:19,290 --> 00:01:20,170
Did you see this?

20
00:01:21,410 --> 00:01:21,930
Shazam!

21
00:01:21,970 --> 00:01:22,490
Dot com.

22
00:01:22,530 --> 00:01:28,890
Okay, uh, let me show you the same results that we were able to identify using the LM now.

23
00:01:28,930 --> 00:01:29,370
Okay.

24
00:01:29,730 --> 00:01:31,010
This is two examples.

25
00:01:31,010 --> 00:01:32,730
Let me give you more examples.

26
00:01:33,010 --> 00:01:33,610
Data.

27
00:01:34,610 --> 00:01:39,650
You might not even have heard about these types of targets earlier.

28
00:01:41,490 --> 00:01:46,610
Uh, $500 for reporting an issue in data tiger.com.

29
00:01:48,330 --> 00:01:48,690
Yes.

30
00:01:48,690 --> 00:01:49,530
Participants.

31
00:01:49,530 --> 00:01:52,010
I hope, uh, things are making more sense now.

32
00:01:52,170 --> 00:01:53,490
You are able to understand.

33
00:01:55,090 --> 00:01:56,050
Please let me know.

34
00:01:56,290 --> 00:02:04,810
So acquisitions are in a great way to identify risks for targets which are usually not looked by others

35
00:02:04,810 --> 00:02:08,330
and can help you identify bugs very, very quickly.

36
00:02:10,850 --> 00:02:11,170
Yes.

37
00:02:11,170 --> 00:02:12,050
Participants.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,880 --> 00:00:01,440
Agreed.

2
00:00:01,440 --> 00:00:01,920
Awesome.

3
00:00:02,480 --> 00:00:03,840
Now let's go to open Web UI.

4
00:00:05,640 --> 00:00:06,160
Yeah.

5
00:00:06,400 --> 00:00:11,000
So few notable acquisition in recent times, some more significant.

6
00:00:11,000 --> 00:00:19,040
So we can see a glimpse in 2016 ImageMagick cube spectra I latest data.

7
00:00:19,200 --> 00:00:24,960
So these are the new assets that have been basically recently acquired.

8
00:00:25,080 --> 00:00:42,800
So I'm going to say hey list all of them in a C in a table format and give and sort them based on recent

9
00:00:43,720 --> 00:00:45,360
acquisitions.

10
00:00:47,400 --> 00:00:52,840
So I'm going to take this data and then I'm going to give a next query to Lama.

11
00:00:53,040 --> 00:00:56,440
And I'm going to say do subdomain enumeration for all of them.

12
00:00:56,480 --> 00:01:00,160
Do text detection and give me the results for the acquisitions.

13
00:01:02,370 --> 00:01:06,250
I have personally, to be honest, not tested these targets yet.

14
00:01:06,250 --> 00:01:10,410
I have seen these targets coming first time over here.

15
00:01:11,210 --> 00:01:14,010
So yeah, definitely good targets that you can test for.

16
00:01:14,010 --> 00:01:16,130
And these are the resources that it has used.

17
00:01:16,130 --> 00:01:21,370
So it has used Wikipedia, BBC, ZDNet, Money Inc, MacRumors.

18
00:01:21,570 --> 00:01:27,730
One of the best websites that you should follow Macrumors.com for identifying if you are going to hunt

19
00:01:27,770 --> 00:01:32,650
on Apple Bug Bounty program because they are the first ones who give Apple Insider news.

20
00:01:33,010 --> 00:01:34,890
Uh, also Apple Insider and merger.

21
00:01:34,890 --> 00:01:37,530
Com is great website to track acquisitions.

22
00:01:38,970 --> 00:01:43,210
Okay, so now we can see uh QB January 2020.

23
00:01:43,210 --> 00:01:51,210
So you can see into an descending order 2020, then 2019 and then 2017, 2016, 2004.

24
00:01:51,530 --> 00:01:59,450
So now, uh, what I want to basically show participants you is that you have your, uh, in-house ready,

25
00:02:00,330 --> 00:02:02,450
a similar, uh.

26
00:02:03,550 --> 00:02:06,110
exact same clone of ChatGPT.

27
00:02:06,750 --> 00:02:07,470
Absolutely.

28
00:02:07,470 --> 00:02:10,950
For free, where you can do as many as search queries that you want.

29
00:02:10,990 --> 00:02:18,390
It is utilizing DuckDuckGo in the back end, and you have very less comparative restrictions compared

30
00:02:18,390 --> 00:02:23,750
to ChatGPT, because OpenAI would enforce a lot of restrictions on things that you want to do, and

31
00:02:23,910 --> 00:02:28,270
you need a pro version to basically execute a lot of queries, after which they're going to throttle

32
00:02:28,310 --> 00:02:34,830
your request, etc. but here you are basically going to do an unlimited number of searches, queries

33
00:02:34,830 --> 00:02:36,790
that you want to do over here.

34
00:02:36,830 --> 00:02:41,510
Not only that, you can train the model for your specific task that you want to do.

35
00:02:41,510 --> 00:02:43,870
For example, I can give a system prompt.

36
00:02:43,870 --> 00:02:46,750
So yeah, I wanted to also let you know about system prompt.

37
00:02:46,950 --> 00:02:53,590
So in system Prompt you can uh, tell the current model llama three latest or you can choose any model

38
00:02:53,910 --> 00:02:58,430
and you can say behave like and penetration tester.

39
00:02:58,550 --> 00:03:03,760
And whenever I ask for acquisitions always give me the acquisitions in this format.

40
00:03:04,120 --> 00:03:04,720
Comma.

41
00:03:05,320 --> 00:03:09,160
Next, immediately after the acquisitions are being found.

42
00:03:09,200 --> 00:03:13,600
Do subdomain enumeration on them and do tech detection.

43
00:03:13,600 --> 00:03:17,440
There is a default system prompt that this model will always do.

44
00:03:17,440 --> 00:03:19,160
So I can give this model a name.

45
00:03:19,560 --> 00:03:22,920
Uh, maybe I can give this model a name as acquisition model.

46
00:03:23,120 --> 00:03:29,040
So whenever I come to acquisition model and I simply give a target name, let's say apple.com, the

47
00:03:29,040 --> 00:03:31,920
system prompt knows what it wants to do here.

48
00:03:31,920 --> 00:03:34,280
So it is going to now take my input.

49
00:03:34,320 --> 00:03:39,360
Do print a table with acquisitions in descending sort.

50
00:03:39,480 --> 00:03:44,360
And then uh from latest uh to down dates.

51
00:03:44,360 --> 00:03:47,760
And then it is going to do a subdomain enumeration tech detection.

52
00:03:48,000 --> 00:03:53,080
And maybe if I ask it to do a vulnerability scan using nuclear it also it will also do that on the latest

53
00:03:53,080 --> 00:03:53,720
targets.

54
00:03:53,720 --> 00:04:00,400
So you are going to be the first movers or the first ones who are going to scan any new asset that comes

55
00:04:00,400 --> 00:04:01,120
on the web.

56
00:04:01,120 --> 00:04:07,130
If any news comes on the internet, you simply come to your model every day, type apple.com.

57
00:04:07,130 --> 00:04:08,810
It is going to scrape on the web.

58
00:04:08,970 --> 00:04:16,890
If MacRumors or Apple Insider, anyone has new published a new blog or an information about an acquisition,

59
00:04:16,890 --> 00:04:19,450
it will pick it up based on your sort.

60
00:04:20,130 --> 00:04:21,930
The latest was one at the top.

61
00:04:21,970 --> 00:04:26,210
Do subdomain enumeration, do text detection, do vulnerability scan and give you the output?

62
00:04:26,250 --> 00:04:27,210
Wouldn't that be awesome?

63
00:04:27,210 --> 00:04:28,050
Participants?

64
00:04:30,650 --> 00:04:31,170
Yes.

65
00:04:40,850 --> 00:04:41,530
Yes.

66
00:04:41,530 --> 00:04:48,410
So you have a you have a you have your personalized model now, which basically does each and everything

67
00:04:48,410 --> 00:04:50,090
for you whenever you want.

68
00:04:50,130 --> 00:04:55,570
You you just simply give the target to it and it automatically does everything in the background.

69
00:04:56,130 --> 00:04:57,810
Uh, yes, I can show you that.

70
00:05:00,050 --> 00:05:01,530
Let me show you a system prompt.

71
00:05:01,530 --> 00:05:03,290
I have already written a prompt.

72
00:05:05,140 --> 00:05:06,540
Oh, let me show you.

73
00:05:10,860 --> 00:05:14,420
Okay, so let me write a prompt system prompt here and let me just save it.

74
00:05:14,420 --> 00:05:14,860
Yes.

75
00:05:21,220 --> 00:05:21,500
Okay.

76
00:05:21,540 --> 00:05:29,700
So behave like a behave like a penetration tester.

77
00:05:30,860 --> 00:05:31,980
Uh, expert.

78
00:05:33,460 --> 00:05:44,580
Whenever I give a name or let's say domain name of any target, quickly.

79
00:05:46,860 --> 00:05:58,980
Do a web search and find all access for it in a table format.

80
00:06:02,700 --> 00:06:06,720
In Latest to old.

81
00:06:08,880 --> 00:06:23,880
Or maybe in recent top to bottom order next immediately start subdomain enumeration.

82
00:06:26,840 --> 00:06:28,280
Yes, that is correct.

83
00:06:29,160 --> 00:06:30,280
That is correct.

84
00:06:31,600 --> 00:06:37,160
Uh, so, uh, our personal install of ulama is limited to specific cut off date.

85
00:06:37,160 --> 00:06:39,720
Will it use DuckDuckGo to look for more current information?

86
00:06:39,720 --> 00:06:43,280
It will use the latest information that is currently available on the website.

87
00:06:43,600 --> 00:06:50,240
So as I said, if you would have seen this this prompt, what does active do and their latest service

88
00:06:50,240 --> 00:06:54,920
or training, you're able to see that it was able to actually identify the current page for the current

89
00:06:54,960 --> 00:06:58,400
training, the AI for cybersecurity, and bug bounty.

90
00:06:58,400 --> 00:07:00,440
So it will do a search.

91
00:07:00,440 --> 00:07:05,280
And the latest results that are available on the web would be scraped and found over here.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,200 --> 00:00:01,680
Let me just.

2
00:00:04,480 --> 00:00:04,800
Okay.

3
00:00:04,840 --> 00:00:06,200
Save this prompt here.

4
00:00:16,800 --> 00:00:17,200
Okay.

5
00:00:17,240 --> 00:00:18,480
System prompt.

6
00:00:18,520 --> 00:00:26,200
Then I read the system prompt and reply.

7
00:00:26,640 --> 00:00:27,680
Understood.

8
00:00:28,520 --> 00:00:29,960
Uh, okay.

9
00:00:30,320 --> 00:00:31,080
And one more thing.

10
00:00:31,120 --> 00:00:32,040
Participants.

11
00:00:32,040 --> 00:00:33,680
You can also enable memory.

12
00:00:33,880 --> 00:00:35,480
So go to settings.

13
00:00:38,240 --> 00:00:39,000
Settings.

14
00:00:40,320 --> 00:00:40,720
Uh.

15
00:00:43,760 --> 00:00:46,040
Yeah I can also add the system prompt here.

16
00:00:46,480 --> 00:00:47,240
Save this.

17
00:00:47,640 --> 00:00:49,680
Uh I wanted to show you memory.

18
00:00:49,680 --> 00:00:54,480
So when you enable the memory it is going to basically remember your previous commands.

19
00:00:54,480 --> 00:00:54,880
Yeah.

20
00:00:55,080 --> 00:00:58,440
Going personal personalization and enable this memory feature.

21
00:00:58,760 --> 00:01:03,120
So when you add this you can personalize the interaction with by adding memories through it.

22
00:01:03,120 --> 00:01:10,480
So it is basically like if you did something yesterday, you can remind the model to be specific to

23
00:01:10,520 --> 00:01:12,240
that and give you a tailored result.

24
00:01:12,240 --> 00:01:19,960
For example, as we did subdomain enumeration on Apple.com yesterday, print the list again for me or

25
00:01:19,960 --> 00:01:21,080
something like that.

26
00:01:21,120 --> 00:01:27,160
Okay, so please enable the memory feature from personalization okay.

27
00:01:27,200 --> 00:01:30,160
So that was one thing right.

28
00:01:30,160 --> 00:01:31,280
The system prompt.

29
00:01:31,320 --> 00:01:32,240
Save it here.

30
00:01:33,040 --> 00:01:36,200
Understood I'm ready to assist with penetration testing tools.

31
00:01:36,200 --> 00:01:38,320
Please provide the target domain name.

32
00:01:38,320 --> 00:01:43,920
You would like to work and quickly do a web search for acquisition in a table format, and then immediately

33
00:01:43,920 --> 00:01:46,160
start subdomain enumeration and print the results.

34
00:01:46,360 --> 00:01:52,080
Wouldn't that be awesome that you have your own hacking machine ready, which is just going to take

35
00:01:52,080 --> 00:01:53,880
your input like this.

36
00:01:54,560 --> 00:02:01,120
Just come to your LLM setup, give your input and sit back and relax.

37
00:02:01,120 --> 00:02:03,040
It is going to do everything for you.

38
00:02:05,720 --> 00:02:06,680
Automatically.

39
00:02:19,280 --> 00:02:19,800
Okay.

40
00:02:19,960 --> 00:02:22,440
We have got the first result and.

41
00:02:24,520 --> 00:02:25,160
Yes.

42
00:02:31,160 --> 00:02:31,720
Okay.

43
00:02:31,720 --> 00:02:34,920
So yes, we have got the output.

44
00:02:35,320 --> 00:02:40,240
Now in the output participants it did an acquisition on Apple.

45
00:02:40,560 --> 00:02:43,760
It is because my prompt was maybe not very good.

46
00:02:43,800 --> 00:02:52,080
So I'm going to say change the prompt and I'll say do acquisition on all the sorry do subdomain enumeration

47
00:02:52,080 --> 00:02:54,800
all the found acquisitions okay.

48
00:02:54,840 --> 00:03:00,240
So I hope you can understand that you can write a better prompt than a prompt that I have written right

49
00:03:00,240 --> 00:03:04,200
now, but it is going to do exactly the same thing that you want it to do.

50
00:03:04,240 --> 00:03:04,760
Okay.

51
00:03:04,800 --> 00:03:10,240
So I'm going to write a better prompt now and it would follow my instructions that I want.

52
00:03:11,160 --> 00:03:19,600
Are you all with me, able to understand that how we are going more deeper and able to make an hacking

53
00:03:19,600 --> 00:03:22,520
machine that works automatically for us?

54
00:03:22,520 --> 00:03:29,080
You can choose multiple models as well that automate your automates your tasks that you want to do.

55
00:03:29,320 --> 00:03:36,280
And after enabling the memory feature, you can actually come back after a week as well to your model

56
00:03:36,280 --> 00:03:41,160
and ask it to do a task that you left over maybe a week ago.

57
00:03:41,680 --> 00:03:48,120
Okay, until you reset or reset everything, it is going to keep that remembered.

58
00:03:48,440 --> 00:03:50,000
So this is how it is going to work.

59
00:03:50,000 --> 00:03:56,400
Now I can basically fix my system, prompt a little bit more, and then it would be able to do better

60
00:03:56,400 --> 00:03:57,600
things for us.

61
00:04:03,000 --> 00:04:06,800
Let's go to Settings System Prompt.

62
00:04:24,840 --> 00:04:29,880
Okay, so now my system prompt is you are an expert penetration tester with deep knowledge of recon

63
00:04:30,240 --> 00:04:31,040
and domain.

64
00:04:31,040 --> 00:04:34,640
When provided with a domain name, perform the following steps in the order.

65
00:04:34,960 --> 00:04:36,040
First is acquisition.

66
00:04:36,040 --> 00:04:36,840
Discovery.

67
00:04:37,040 --> 00:04:40,560
Conduct a web search to identify all acquisitions of parent companies.

68
00:04:40,760 --> 00:04:48,920
Each entry must include an acquired entry, entity name, acquisition date, source reference notes,

69
00:04:49,080 --> 00:04:55,080
and then perform subdomain enumeration immediately within a subdomain enumeration for the given domain

70
00:04:55,080 --> 00:05:02,680
using Osint tools and etc. or I can say use sub finder tool from the MCP server and return the results

71
00:05:03,640 --> 00:05:12,920
for the given domains that are found in the Previous step of.

72
00:05:15,480 --> 00:05:16,360
Acquisition.

73
00:05:16,480 --> 00:05:23,480
Now I have my, uh, system prompt, which is much better than earlier and ready.

74
00:05:23,480 --> 00:05:31,240
Let's save this and let's say read the new system.

75
00:05:36,240 --> 00:05:39,560
Prompt and reply.

76
00:05:39,960 --> 00:05:40,840
Understood.

77
00:05:41,120 --> 00:05:42,080
If you got it.

78
00:06:01,640 --> 00:06:03,200
Let's start a new chat.

79
00:06:09,400 --> 00:06:09,960
Yes.

80
00:06:11,440 --> 00:06:11,880
Hi.

81
00:06:13,640 --> 00:06:17,120
Read the system prompt and reply.

82
00:06:18,480 --> 00:06:19,480
Understood?

83
00:06:20,760 --> 00:06:22,800
Okay, I got the previous response.

84
00:06:22,800 --> 00:06:25,880
Now it says understood but I've started a new chat anyways.

85
00:06:26,400 --> 00:06:26,920
Uh, understood.

86
00:06:26,920 --> 00:06:29,320
I'm ready to perform pentesting on a given domain.

87
00:06:29,360 --> 00:06:30,280
Please provide the domain name.

88
00:06:30,280 --> 00:06:33,960
I'll get the acquisition, discovery and subdomain enumeration as per the steps outlined.

89
00:06:34,280 --> 00:06:34,920
Excellent.

90
00:06:35,000 --> 00:06:36,640
Uh, let's do apple.com again.

91
00:06:38,400 --> 00:06:39,040
That's it.

92
00:06:39,280 --> 00:06:40,520
Uh, come back to your.

93
00:06:40,840 --> 00:06:45,920
We can come back here after a moment and see what is our expected outcome and results.

94
00:06:45,960 --> 00:06:47,600
Oh, participants, can you see this?

95
00:06:48,840 --> 00:06:50,400
It is running a Google doc.

96
00:06:50,400 --> 00:06:51,360
Very smart.

97
00:06:52,080 --> 00:06:55,280
So our our model is very smart.

98
00:06:55,280 --> 00:07:02,400
And if you have noticed, it actually was running a Google doc and getting the target list from Google.

99
00:07:05,360 --> 00:07:05,960
Awesome.

100
00:07:05,960 --> 00:07:08,760
Now we are getting really, really nice output.

101
00:07:09,120 --> 00:07:14,930
Uh, so we got Beats Electronics, glimpse and E magic and subdomain enumeration found.

102
00:07:14,930 --> 00:07:19,250
Various using Osint techniques are this for Apple iCloud.

103
00:07:19,290 --> 00:07:21,410
Apple apple.com dot China.

104
00:07:21,450 --> 00:07:21,770
Mm.

105
00:07:22,130 --> 00:07:22,450
Okay.

106
00:07:22,730 --> 00:07:28,650
Uh, I think we have to tweak our prompt a little bit more so that it does subdomain discovery for the

107
00:07:28,650 --> 00:07:29,970
acquired entity name.

108
00:07:30,090 --> 00:07:34,370
So in the prompt I'll say do subdomain discovery for the acquired entity name.

109
00:07:34,370 --> 00:07:36,010
So it gives us the better results.

110
00:07:36,410 --> 00:07:41,130
Uh, but I hope, uh, you have understood how to do it with few trials and errors.

111
00:07:41,130 --> 00:07:44,610
With your system prompt, I think you can make a perfect system prompt.

112
00:07:44,850 --> 00:07:51,730
And, uh, your given model would be ready to assist you in doing the same.

113
00:07:52,850 --> 00:07:55,050
Yes, we can do tech detection as well.

114
00:07:55,290 --> 00:08:00,290
Uh, so, yes, Hakeem, we can do all sort of steps, not only subdomain enumeration.

115
00:08:00,290 --> 00:08:02,450
We can do technology detection.

116
00:08:02,450 --> 00:08:03,810
As I said, we you.

117
00:08:03,850 --> 00:08:09,690
Then you can do vulnerability, uh, hacking or vulnerability detection using nuclei.

118
00:08:14,010 --> 00:08:15,290
Thank you so much, Seth.

119
00:08:15,290 --> 00:08:15,330
that?

120
00:08:16,970 --> 00:08:20,810
Uh, you can definitely train a better model.

121
00:08:20,810 --> 00:08:25,130
I would say, uh, by tweaking your model a little bit more.

122
00:08:25,410 --> 00:08:32,450
I have been doing, uh, these things and researching on these from a long time, and I can say that

123
00:08:32,450 --> 00:08:38,370
you will never miss using ChatGPT, because now you would have full control over your model, where

124
00:08:38,410 --> 00:08:46,770
step by step, you are basically making your model so much more knowledgeable, uh, about a specific

125
00:08:46,770 --> 00:08:50,490
niche domain like red teaming or penetration testing.

126
00:08:50,490 --> 00:08:56,970
You might have also seen yesterday we have given the knowledge of hack tricks utilizing that as well.

127
00:08:57,290 --> 00:09:04,970
Uh, we can actually generate better, uh, outcomes and outputs for tasks or techniques that we do.

128
00:09:05,290 --> 00:09:11,290
So I'm sure that all of these things are going to be very, very valuable and useful for all of you.

129
00:09:12,730 --> 00:09:17,890
And it is going to help you aid your tasks in a much more better form.

130
00:09:20,330 --> 00:09:21,650
Uh, yes.

131
00:09:22,170 --> 00:09:24,530
We cannot change the system prompt.

132
00:09:24,730 --> 00:09:29,450
Uh, so system prompt is the prompt that each model has its.

133
00:09:29,490 --> 00:09:31,930
So it is like the first prompt for the model.

134
00:09:32,290 --> 00:09:38,490
You are not allowed to change system prompts, but you can give user prompts which a model like a model

135
00:09:38,490 --> 00:09:46,890
like ChatGPT, uh, GPT 4.0 can understand, but it will forget that prompt later on because, uh,

136
00:09:47,090 --> 00:09:51,370
it is not designed to keep that that as a system prompt.

137
00:09:51,370 --> 00:09:53,010
And secondly, uh.

138
00:09:55,130 --> 00:09:59,210
OpenAI has system prompts which are going to override user prompts.

139
00:09:59,410 --> 00:10:07,610
So system prompt prompt might have keywords which might say, uh, blacklist or do not reply or say

140
00:10:07,610 --> 00:10:08,570
this is unethical.

141
00:10:08,570 --> 00:10:15,650
When any user writes a prompt which contains hacking or maybe subdomain enumeration or recon, etc..

142
00:10:15,650 --> 00:10:24,450
So that is why, uh, User prompts are are usually superseded by system level prompts.

143
00:10:24,650 --> 00:10:29,810
So that is why you might see there are different agents on the internet that are specialized to do some

144
00:10:29,810 --> 00:10:33,170
specific tasks based on their system prompts.

145
00:10:33,690 --> 00:10:44,370
There is an excellent system prompts leak that was that happened uh, that as you asked this.

146
00:10:44,410 --> 00:10:50,170
Let me just share that, uh, it was in news as well for a long period of time.

147
00:10:50,170 --> 00:10:57,090
You can definitely read about this system prompts and models of AI tool where very famous, uh, AI

148
00:10:57,130 --> 00:10:58,130
tools like Devin.

149
00:10:58,130 --> 00:11:06,410
I love their system prompts were leaked and it was very, very you would say, uh, the community was

150
00:11:06,410 --> 00:11:14,530
very, uh, surprised to see that such large billion dollar companies are using such prompts in which

151
00:11:14,530 --> 00:11:16,570
their base model is actually olama.

152
00:11:16,770 --> 00:11:18,050
So you can see this prompt.

153
00:11:18,210 --> 00:11:21,770
Your Devin, a software engineer, using a real computer operating system.

154
00:11:21,770 --> 00:11:22,850
Your real code base.

155
00:11:22,890 --> 00:11:25,490
Few programmers are as talented as you are.

156
00:11:25,530 --> 00:11:26,930
Understanding code bases.

157
00:11:27,250 --> 00:11:30,890
Write functional clean code and iterating on your changes until they are correct.

158
00:11:30,930 --> 00:11:31,530
Blah blah.

159
00:11:31,930 --> 00:11:32,170
When.

160
00:11:32,170 --> 00:11:32,650
Communicate.

161
00:11:32,690 --> 00:11:33,930
When to communicate with user.

162
00:11:33,930 --> 00:11:37,330
When encountering environment issues, share deliverables, and so on.

163
00:11:37,330 --> 00:11:40,690
So this is the system prompt for Devin I.

164
00:11:42,970 --> 00:11:50,930
So Devin I is basically a artificial intelligence assistant tool created by Cognition Cognition Labs.

165
00:11:51,250 --> 00:11:53,810
And it's a paid AI bot.

166
00:11:53,850 --> 00:11:54,890
As you can see over here.

167
00:11:54,890 --> 00:11:56,090
So let me go over there.

168
00:11:56,490 --> 00:12:00,250
So it's a collaborative tool that can help you do a lot of things.

169
00:12:00,690 --> 00:12:06,490
Uh, you can basically ask it to code, generate repositories, etc., etc..

170
00:12:07,010 --> 00:12:12,690
When these prompts were leaked, the usually these prompts are leaked due to some vulnerabilities that

171
00:12:12,690 --> 00:12:21,170
users or researchers find in the, uh, organizations LM itself, or sometimes the internal employees

172
00:12:21,170 --> 00:12:23,250
or workers leak their system prompts.

173
00:12:23,250 --> 00:12:24,130
That means.

174
00:12:24,690 --> 00:12:31,130
That means if you have a system prompt of an model, you can actually replicate the entire model.

175
00:12:31,730 --> 00:12:33,970
And that's absolutely possible.

176
00:12:34,090 --> 00:12:40,730
So if I copy this prompt and give it to a llama, llama would definitely understand everything and do

177
00:12:40,730 --> 00:12:43,290
the exact same thing that I would do.

178
00:12:44,370 --> 00:12:44,810
Yeah.

179
00:12:44,810 --> 00:12:49,730
In addition to that, there would be some capabilities or plugins that I have to add to open web UI

180
00:12:49,770 --> 00:12:53,370
that we will see in the next section how you can add plugins.

181
00:12:53,370 --> 00:12:59,810
So my my llama model is more capable of doing things, for example, giving a prompt and generating

182
00:12:59,810 --> 00:13:06,130
video content out of it to maybe make a YouTube video or a reel which is not capable of doing so, but

183
00:13:06,130 --> 00:13:08,170
with the help of plugins, it can do that.

184
00:13:08,170 --> 00:13:09,010
We will see that.

185
00:13:09,010 --> 00:13:15,170
So if I give this system prompt to llama right now, it would exactly behave the way Devin I does.

186
00:13:15,690 --> 00:13:17,370
So wouldn't that be really awesome?

187
00:13:17,410 --> 00:13:24,490
Hence, organizations don't want their system prompts to be leaked or people to know about them.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 15: HTTPX & Screenshots

1
00:00:00,120 --> 00:00:00,640
Okay.

2
00:00:00,640 --> 00:00:07,000
So now we move ahead to let's see visual reconnaissance.

3
00:00:07,160 --> 00:00:18,160
So to do that uh I'm going to use a tool which is http ex that has been created by Project Discovery.

4
00:00:18,360 --> 00:00:21,040
So let's go to Project Discovery HTTP.

5
00:00:21,280 --> 00:00:27,000
It is available for windows, Linux and Mac OS, all types of binaries.

6
00:00:27,000 --> 00:00:29,960
Currently we are on the documentation page of HTTP.

7
00:00:30,880 --> 00:00:34,320
It's really good and fast tool.

8
00:00:34,880 --> 00:00:37,400
Uh, across all the tools that I've used in past.

9
00:00:37,400 --> 00:00:39,800
I highly recommend using HTTP.

10
00:00:40,600 --> 00:00:42,480
So let's go ahead and install this.

11
00:00:42,520 --> 00:00:45,520
So to install this you need to say http GitHub.

12
00:00:46,240 --> 00:00:51,800
Go to the first search result.

13
00:00:51,800 --> 00:00:54,440
Uh you should see that it is created by Project Discovery.

14
00:00:54,440 --> 00:00:56,760
This is the correct unofficial repository.

15
00:00:57,000 --> 00:00:58,840
Please go to the releases section.

16
00:01:00,020 --> 00:01:04,580
and you can download the compatible asset or version for your system.

17
00:01:04,700 --> 00:01:08,900
So if you are on Linux 32 bit, please use this version.

18
00:01:09,060 --> 00:01:17,060
64 bit ARM architecture Arm64 Mac OS, Intel chip, Mac OS Silicon chip.

19
00:01:17,220 --> 00:01:19,300
Windows 32, windows 64.

20
00:01:19,780 --> 00:01:22,540
I'm going to use Mac OS, arm 64.

21
00:01:22,580 --> 00:01:24,300
I have already downloaded it.

22
00:01:24,700 --> 00:01:28,260
Once you download it, unzip it and you should be able to see the binary.

23
00:01:28,700 --> 00:01:36,140
So once you type the command http and hit enter, you should be able to see a banner message like this

24
00:01:36,500 --> 00:01:38,860
HTTP by Project Discovery.

25
00:01:39,260 --> 00:01:42,220
And my current version is outdated.

26
00:01:42,220 --> 00:01:46,540
So let me just write update and it should update itself automatically.

27
00:01:47,460 --> 00:01:48,380
Permission denied.

28
00:01:48,420 --> 00:01:53,100
Okay, sudo reboot and it will update itself.

29
00:01:56,220 --> 00:01:56,660
Then.

30
00:01:56,840 --> 00:02:02,800
So now we have the latest version of http x with us available.

31
00:02:03,120 --> 00:02:03,800
Excellent.

32
00:02:03,800 --> 00:02:09,720
So now to use this participants, what we are going to do is we are going to use the Screenshotting

33
00:02:09,760 --> 00:02:10,920
feature of this.

34
00:02:10,960 --> 00:02:13,160
It uses a headless chromium browser.

35
00:02:13,400 --> 00:02:18,920
So it will first on your first run on your system it is going to download it.

36
00:02:18,960 --> 00:02:23,760
It is it will be around 100 to 150 MB of file size.

37
00:02:23,920 --> 00:02:29,320
Once it is downloaded then it will not download it again and the first run can be slower.

38
00:02:29,320 --> 00:02:34,160
But from the second run when you run this against a target, it will be very fast.

39
00:02:34,920 --> 00:02:35,920
Uh, let us see this.

40
00:02:35,920 --> 00:02:37,720
So how to use this?

41
00:02:38,320 --> 00:02:44,680
Let me go to the AI folder CD, CD, CD, I yeah.

42
00:02:45,400 --> 00:02:47,240
Now I'm going to say http x.

43
00:02:47,640 --> 00:02:50,280
Uh, but before that let me find some subdomains.

44
00:02:50,280 --> 00:02:57,820
So I'm going to find some subdomains for maybe five dot in and save this results to rectify dot txt

45
00:02:58,020 --> 00:03:04,860
or I can simply pass these results to HTTP and say hyphen screenshot ss.

46
00:03:05,380 --> 00:03:08,500
SS is the flag for screenshot participants.

47
00:03:08,740 --> 00:03:09,980
And then I say hyphen.

48
00:03:10,580 --> 00:03:20,780
Hyphen o means output in the current directory in the output new folder or output folder, whatever

49
00:03:20,780 --> 00:03:22,060
name that you want to give.

50
00:03:22,100 --> 00:03:30,660
Okay, let's understand once again find the subdomains for a domain dot in pipe the results as standard.

51
00:03:30,700 --> 00:03:35,620
The standard output of this command is given as a standard input to HTTP.

52
00:03:36,220 --> 00:03:40,300
We enable the screenshot feature using headless Chrome browser.

53
00:03:40,540 --> 00:03:44,980
We send the output in the current directory whose name is output.

54
00:03:45,740 --> 00:03:46,820
Let's hit enter.

55
00:03:48,940 --> 00:03:53,440
You can see it is downloading the browser currently chromium.

56
00:03:54,080 --> 00:03:56,440
Headless chromium browser for Mac.

57
00:03:57,040 --> 00:04:00,160
Arm for Mac system so it will download it.

58
00:04:00,960 --> 00:04:03,480
It will take around few seconds.

59
00:04:05,840 --> 00:04:08,560
5,660% downloading has completed.

60
00:04:12,200 --> 00:04:19,360
This is only one one time process and it will not happen again, so it will automatically use that downloaded

61
00:04:19,360 --> 00:04:19,680
version.

62
00:04:19,680 --> 00:04:22,800
You can see it has downloaded this and it is unzipping it.

63
00:04:22,800 --> 00:04:25,280
Let me give the password so it unzips.

64
00:04:25,280 --> 00:04:27,200
And please allow all.

65
00:04:27,360 --> 00:04:31,320
So it does that every time automatically unzipping it.

66
00:04:31,320 --> 00:04:31,960
Download it.

67
00:04:31,960 --> 00:04:42,560
And now you can see subdomain enumeration has begun and the screenshotting has also begun in the background.

68
00:04:44,840 --> 00:04:47,520
Let's wait for this results to complete.

69
00:04:48,080 --> 00:04:48,840
Awesome.

70
00:04:48,840 --> 00:04:50,400
The task has been completed.

71
00:04:50,720 --> 00:04:58,030
Let's lets open the current folder participants and when we open the current folder, let's go to.

72
00:05:00,710 --> 00:05:02,190
Let's go to.

73
00:05:06,750 --> 00:05:08,870
Let's go to output file.

74
00:05:11,510 --> 00:05:12,270
Okay.

75
00:05:18,510 --> 00:05:25,990
Uh, it prompted for a password because in my Mac OS, I have disabled installing any external tools

76
00:05:25,990 --> 00:05:28,590
or libraries by default without sudo privileges.

77
00:05:28,590 --> 00:05:29,870
So it asked me for a password.

78
00:05:29,870 --> 00:05:31,590
It might not ask you for a password.

79
00:05:31,750 --> 00:05:33,750
And that was my system password, right?

80
00:05:37,510 --> 00:05:38,110
Uh, yes.

81
00:05:38,310 --> 00:05:44,270
Uh, we did one thing that is not right.

82
00:05:44,870 --> 00:05:48,390
Uh, output active files and file that has been created.

83
00:05:48,390 --> 00:05:50,890
So you should not do this like this.

84
00:05:51,170 --> 00:05:52,410
Just simply say output.

85
00:05:52,770 --> 00:05:57,090
If I delete this, don't give dot slash.

86
00:06:04,170 --> 00:06:04,770
Let me see.

87
00:06:04,810 --> 00:06:06,370
Output is created.

88
00:06:23,290 --> 00:06:23,690
Oh.

89
00:06:26,050 --> 00:06:26,810
Wait.

90
00:06:27,250 --> 00:06:29,170
Something is wrong.

91
00:06:31,130 --> 00:06:32,330
Wait, let me just.

92
00:06:32,330 --> 00:06:34,050
Just check the flag once more.

93
00:06:35,930 --> 00:06:37,970
Uh, before the class, I have run this tool already.

94
00:06:37,970 --> 00:06:43,570
You can see the output folder here, and it contains the response and the screenshots here.

95
00:06:44,370 --> 00:06:45,290
Uh, let me.

96
00:06:45,330 --> 00:06:45,530
Okay.

97
00:06:45,570 --> 00:06:46,930
First, let me show you the output.

98
00:06:46,930 --> 00:06:48,430
Then I'll show you the right flag.

99
00:06:50,550 --> 00:06:57,030
So you can see the subdomains that are being found are segregated into folders like blogspot dot n,

100
00:06:57,030 --> 00:06:58,590
claim me dot dot n.

101
00:06:58,630 --> 00:07:00,950
You can open that and you can see the screenshot.

102
00:07:01,550 --> 00:07:09,230
The screenshot of the current domain blogspot dot n and you can see the file has been given a random

103
00:07:09,230 --> 00:07:09,590
name.

104
00:07:09,590 --> 00:07:11,590
This is basically the response code.

105
00:07:11,830 --> 00:07:17,350
You can check the same response code in the response folder here, and you can see the get request that

106
00:07:17,350 --> 00:07:23,590
was sent, the response that was received, and at the end the targeted subdomain name.

107
00:07:23,590 --> 00:07:24,270
Like this.

108
00:07:25,750 --> 00:07:26,470
Very interesting.

109
00:07:26,470 --> 00:07:28,110
This is going to be very helpful for us.

110
00:07:28,110 --> 00:07:29,070
The responses.

111
00:07:29,310 --> 00:07:30,350
Now let's go to screenshots.

112
00:07:30,390 --> 00:07:33,870
Now I'm definitely not going to go in each folder and see the screenshots.

113
00:07:33,910 --> 00:07:41,750
Hence I'm going to open this screenshot at HTML file in my browser, and it gives a very nice output

114
00:07:41,790 --> 00:07:44,710
of screenshots as we can see over here.

115
00:07:45,250 --> 00:07:47,450
So blocks dot dot in.

116
00:07:47,450 --> 00:07:49,930
I can see the screenshot that is running nice.

117
00:07:50,410 --> 00:07:51,170
Shopify.

118
00:07:53,690 --> 00:07:54,770
Something went wrong.

119
00:07:54,770 --> 00:07:56,730
It did not load the screenshot correctly.

120
00:07:56,850 --> 00:07:58,170
Wait yeah.

121
00:07:58,370 --> 00:08:00,010
Here you can see the screenshots.

122
00:08:02,290 --> 00:08:06,410
Uh, something went wrong I guess with the file.

123
00:08:06,570 --> 00:08:07,850
So I'll do that once again.

124
00:08:07,850 --> 00:08:11,130
And you should be able to see all the screenshot available over here.

125
00:08:11,890 --> 00:08:12,370
Okay.

126
00:08:12,930 --> 00:08:16,290
Uh, participants able to understand?

127
00:08:26,090 --> 00:08:26,690
Yes.

128
00:08:34,210 --> 00:08:34,770
Nice.

129
00:08:34,770 --> 00:08:37,610
Let me give the prompt or sorry, the command once again.

130
00:08:38,490 --> 00:08:42,170
Uh, sub finder hyphen d active dot in.

131
00:08:45,190 --> 00:08:47,630
Silently http screenshot.

132
00:08:47,670 --> 00:08:49,910
You can say hyphen, ss or screenshot.

133
00:08:50,030 --> 00:08:51,470
The screenshot directory.

134
00:08:51,470 --> 00:08:56,270
Let's call it as screenshots and hit enter.

135
00:09:01,150 --> 00:09:05,950
RM screenshots directory not specified.

136
00:09:13,870 --> 00:09:14,270
Yeah.

137
00:09:20,310 --> 00:09:21,230
Screenshot.

138
00:10:07,290 --> 00:10:07,730
Okay.

139
00:10:07,730 --> 00:10:10,410
So we can see the output coming here.

140
00:10:10,410 --> 00:10:11,530
Let me see.

141
00:11:30,910 --> 00:11:34,030
This is not loading up appropriately.

142
00:11:42,410 --> 00:11:43,930
Yep, the output is saved.

143
00:11:44,570 --> 00:11:45,050
Uh, sorry.

144
00:11:45,050 --> 00:11:47,970
The outcome has printed on the screen.

145
00:11:48,330 --> 00:11:50,410
It is just the correct flag.

146
00:11:50,650 --> 00:11:54,410
I have not been able to see what is the right flag.

147
00:12:00,290 --> 00:12:02,850
HTTP screenshot.

148
00:12:10,450 --> 00:12:10,890
Yeah.

149
00:12:14,330 --> 00:12:15,290
Screenshot option.

150
00:12:15,290 --> 00:12:15,610
Yes.

151
00:12:15,610 --> 00:12:17,570
We can do that using.

152
00:12:21,490 --> 00:12:23,450
Yes we can ask Lama as well.

153
00:12:24,690 --> 00:12:32,530
Uh, I have used it so many times in past, but I'm not sure why it is not giving me screenshot are

154
00:12:32,530 --> 00:12:34,650
stored in the output screenshot directly by default.

155
00:12:34,650 --> 00:12:44,270
Okay, to specify a custom output, use Srhd option in response to this path.

156
00:12:44,310 --> 00:12:46,350
Got it, got it, got it.

157
00:12:46,350 --> 00:12:47,510
Thank you so much.

158
00:12:48,990 --> 00:12:51,710
And let's do the same thing now.

159
00:12:52,950 --> 00:12:54,470
So we are going to say SRT.

160
00:13:04,670 --> 00:13:06,430
And specify a directory.

161
00:13:06,430 --> 00:13:08,470
So let's say the directory is output.

162
00:13:09,590 --> 00:13:11,430
Do we have the output directory here by the way.

163
00:13:11,470 --> 00:13:11,830
No.

164
00:13:11,830 --> 00:13:15,270
So let's make it as output and hit enter.

165
00:13:17,790 --> 00:13:20,230
Yes yes.

166
00:13:20,230 --> 00:13:22,990
Now we have again it it is working now.

167
00:13:22,990 --> 00:13:25,430
And we have the screenshots now coming up over here.

168
00:13:27,550 --> 00:13:28,270
Excellent.

169
00:13:33,900 --> 00:13:35,700
You have the responses coming here.

170
00:13:35,700 --> 00:13:38,140
So the correct flag is s r d.

171
00:13:38,940 --> 00:13:39,340
Okay.

172
00:13:40,220 --> 00:13:45,380
Save store response then for directory.

173
00:13:45,380 --> 00:13:46,860
So whatever is the directory name.

174
00:13:46,860 --> 00:13:47,980
And this is completed.

175
00:13:48,260 --> 00:13:49,900
Now we can go to screenshots.

176
00:13:49,940 --> 00:13:53,540
And we can actually see the screenshots coming very nicely over here.

177
00:13:53,780 --> 00:13:58,620
So for activate we did not got a screenshot because that subdomain do not exist.

178
00:13:58,620 --> 00:14:03,460
So ideally you should you you should do what you should first filter out live targets and then take

179
00:14:03,460 --> 00:14:04,260
screenshots.

180
00:14:04,300 --> 00:14:10,340
Anyways, we just ran it all over that and you can see for Shopify Dot activate and we are able to see

181
00:14:10,340 --> 00:14:16,540
that oh, there is a subdomain takeover possible over here because the store is currently not taken.

182
00:14:16,780 --> 00:14:21,060
Oh, there is a login page available at web mail blogs.

183
00:14:21,060 --> 00:14:25,860
Oh there are some blogs written, but there is a search functionality here and here where an XSS can

184
00:14:25,860 --> 00:14:26,620
be attempted.

185
00:14:27,220 --> 00:14:29,260
Other of these do not exist.

186
00:14:29,260 --> 00:14:30,180
Most likely.

187
00:14:30,220 --> 00:14:30,580
Hence.

188
00:14:30,860 --> 00:14:33,960
Hence you are able to see that we did not get a response over there.

189
00:14:34,480 --> 00:14:36,800
Uh, so this is one thing.

190
00:14:37,160 --> 00:14:45,760
Again, maybe what I would also recommend is when you are taking a screenshot, uh, you can increase

191
00:14:46,160 --> 00:14:52,360
the timing, uh, to wait and to skip to the next asset.

192
00:14:52,520 --> 00:15:00,080
So this way, what happens if his when HTTP is not able to connect correctly to the target in a certain

193
00:15:00,080 --> 00:15:02,080
period of time, it should not skip it.

194
00:15:02,320 --> 00:15:07,400
Or if it is not able to connect for five seconds, then it should skip it and go to the next target.

195
00:15:07,800 --> 00:15:08,280
Okay.

196
00:15:08,320 --> 00:15:09,680
So you can do that.

197
00:15:09,840 --> 00:15:17,680
To do that you can use this option screenshot timeout value set timeout for screenshot in seconds and

198
00:15:17,720 --> 00:15:18,360
idle value.

199
00:15:18,400 --> 00:15:21,040
Set idle value before taking screenshot in seconds.

200
00:15:21,360 --> 00:15:28,960
So I think this option will be helpful for us that it should timeout after some time and we should have

201
00:15:28,960 --> 00:15:32,740
an ideal value as well, which is the time difference between two screenshots.

202
00:15:32,740 --> 00:15:39,580
So you can say Sid five, take five or maybe 3 or 4 seconds of delay between each screenshots and timeout

203
00:15:39,940 --> 00:15:40,620
from a website.

204
00:15:40,620 --> 00:15:43,260
If you're not able to take screenshot in 10s.

205
00:15:45,500 --> 00:15:45,820
Got it.

206
00:15:45,820 --> 00:15:46,700
Participants.

207
00:15:47,340 --> 00:15:52,900
And then you can simply use this HTML viewer to take and to see all the output that is available over

208
00:15:52,900 --> 00:15:58,940
here very nicely, and utilize this as your visual reconnaissance approach.

209
00:15:59,500 --> 00:16:01,980
The same thing can also be automated with your llama.

210
00:16:02,260 --> 00:16:08,620
You can create an MVP for the same thing for the command that we are running over here.

211
00:16:09,060 --> 00:16:13,500
And just give the command to llama, uh, using your prompt.

212
00:16:13,500 --> 00:16:16,340
And it would do that in the background automatically for you.

213
00:16:19,140 --> 00:16:19,380
Yes.

214
00:16:19,380 --> 00:16:22,140
Participants, are you all with me able to understand?

215
00:16:22,140 --> 00:16:23,700
Please give me a quick heads up.

216
00:16:32,480 --> 00:16:32,960
Yes.

217
00:16:33,160 --> 00:16:34,400
Uh, there's a question.

218
00:16:34,440 --> 00:16:37,680
The downloaded GPT for all will be updated with all features.

219
00:16:37,680 --> 00:16:40,240
The reason I ask is that it is running on local host.

220
00:16:40,600 --> 00:16:41,920
How do we seem to get updates?

221
00:16:41,920 --> 00:16:42,360
Yes.

222
00:16:42,600 --> 00:16:49,200
So, uh, automatically from time to time, we would be able to see the new models that has been released.

223
00:16:49,520 --> 00:16:53,960
So whenever a new model is released, uh, we can automatically download that model.

224
00:16:54,400 --> 00:17:01,800
Uh, so for example, we are currently, if you see on my terminal, uh, we are running.

225
00:17:01,840 --> 00:17:03,640
Yeah, we are running Lama here.

226
00:17:04,920 --> 00:17:06,920
So Lama run Lama three.

227
00:17:06,920 --> 00:17:08,360
So let me just say bye.

228
00:17:08,600 --> 00:17:12,200
And then we can run Lama and help menu.

229
00:17:12,200 --> 00:17:15,160
And we can pull a new model from a registry.

230
00:17:15,440 --> 00:17:18,160
So whenever a new model is launched, we can give the model name.

231
00:17:18,160 --> 00:17:19,360
And that will be pulled.

232
00:17:19,560 --> 00:17:23,680
So we have a new model now connected to open web UI or GPT four.

233
00:17:24,920 --> 00:17:25,360
Okay.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 16: VAPT Report Generation

1
00:00:09,760 --> 00:00:10,080
Yeah.

2
00:00:10,080 --> 00:00:11,160
So, participants.

3
00:00:11,200 --> 00:00:15,000
Now we shall move forward and let's understand about.

4
00:00:17,280 --> 00:00:24,480
Creating clear, concise reports for bug bounties or VIP.

5
00:00:25,680 --> 00:00:33,120
One of the most boring I would say, or tiring task for any security researcher is writing the report

6
00:00:33,120 --> 00:00:36,680
from scratch, because that usually takes a lot of time.

7
00:00:37,200 --> 00:00:45,520
I am not discouraging that writing professional reports, uh, is not a good thing, but you should

8
00:00:45,520 --> 00:00:48,720
definitely know about how professional report looks looks.

9
00:00:48,840 --> 00:00:56,000
But when you want to scale up and you want to send multiple reports to private program, then doing

10
00:00:56,000 --> 00:01:01,660
the same monotonous thing, do it from scratch wouldn't be very, very efficient.

11
00:01:01,860 --> 00:01:07,860
In that case, we will understand today practically with example of how.

12
00:01:10,860 --> 00:01:12,020
AI can help us.

13
00:01:12,020 --> 00:01:17,060
So we are going to set up a knowledge base for our model.

14
00:01:17,180 --> 00:01:22,580
And then we are going to ask the model to help us understand the same thing and generate reports.

15
00:01:23,060 --> 00:01:26,100
So you just have to give the vulnerability name to the model.

16
00:01:26,100 --> 00:01:30,060
And it is going to generate the entire report for you from scratch.

17
00:01:30,540 --> 00:01:32,660
So I have to save time.

18
00:01:32,900 --> 00:01:35,860
I have already created a knowledge base.

19
00:01:36,300 --> 00:01:38,580
The knowledge base is known as RT reporting.

20
00:01:38,580 --> 00:01:39,540
Let me go there.

21
00:01:40,980 --> 00:01:47,020
Uh, participants, if you see over here in this knowledge base, I have given the name as RT reporting,

22
00:01:47,340 --> 00:01:49,180
uh, penetration testing, reporting.

23
00:01:49,340 --> 00:01:55,620
And I have uploaded one document, uh, which is an a docs report or word doc report, as you can see

24
00:01:55,620 --> 00:01:56,340
over here.

25
00:01:59,500 --> 00:01:59,900
Yeah.

26
00:02:00,140 --> 00:02:08,960
This is the word report, uh, from a program that was reported to, uh, Indian government program.

27
00:02:09,560 --> 00:02:18,000
So you can see the name, the summary about the vulnerability, the severity, the payload complexity

28
00:02:18,200 --> 00:02:22,680
from impact affected IP recommendation, references and proof of concept.

29
00:02:23,040 --> 00:02:26,200
So here you can see participants very simply.

30
00:02:26,720 --> 00:02:33,840
Uh, there is an access report which contains, uh, all the necessary details like summary, severity,

31
00:02:33,880 --> 00:02:40,720
payload, uh, and other necessary details like affected IP complexity from and then references.

32
00:02:40,720 --> 00:02:44,960
And then we finally have the section for proof of concept wherein we have a screenshot.

33
00:02:46,160 --> 00:02:46,720
Nice.

34
00:02:46,880 --> 00:02:52,160
So I'm going to feed this document as a knowledge base to our model.

35
00:02:52,360 --> 00:02:55,400
So to do that I'm going to upload that document here.

36
00:02:55,920 --> 00:02:57,840
The document is already uploaded.

37
00:02:57,840 --> 00:03:04,580
And you can see over here the outcome which is parsed from it into a text contextual form.

38
00:03:05,140 --> 00:03:05,660
Nice.

39
00:03:06,020 --> 00:03:11,740
Once this has been done, I'm going to go to models and I'm going to set up a new model.

40
00:03:11,860 --> 00:03:13,220
So you need to click plus.

41
00:03:13,700 --> 00:03:15,700
I have already set up this model.

42
00:03:15,700 --> 00:03:17,780
So I'm going to show you the settings for it.

43
00:03:17,780 --> 00:03:19,180
Let me click on edit.

44
00:03:21,460 --> 00:03:23,980
And you need to give the name to the model first.

45
00:03:24,020 --> 00:03:26,540
I have given a name as Vapt report.

46
00:03:26,940 --> 00:03:27,180
Yeah.

47
00:03:27,180 --> 00:03:29,420
One very interesting fun fun thing.

48
00:03:29,420 --> 00:03:34,420
You can also set up images for your model so you don't have to basically read their names.

49
00:03:34,420 --> 00:03:34,820
If you want.

50
00:03:34,820 --> 00:03:42,300
You can have fancy images or profile pictures for your models to help you identify what the model is

51
00:03:42,300 --> 00:03:42,940
going to do.

52
00:03:43,180 --> 00:03:45,780
So this model basically is for the Vapt report.

53
00:03:45,780 --> 00:03:50,460
So I can give a report or notebook kind of an image over here.

54
00:03:50,700 --> 00:03:51,860
So that helps me understand.

55
00:03:51,900 --> 00:03:52,060
Okay.

56
00:03:52,100 --> 00:03:53,460
So this is for notebook.

57
00:03:54,500 --> 00:03:56,020
This does not look notebook.

58
00:03:56,580 --> 00:03:56,900
Okay.

59
00:03:56,940 --> 00:03:58,740
Anyways let me use this image.

60
00:04:00,780 --> 00:04:01,300
Okay.

61
00:04:01,330 --> 00:04:03,250
So nice.

62
00:04:03,250 --> 00:04:05,570
Once you do that, you can choose the model.

63
00:04:05,570 --> 00:04:10,730
We can have the we can choose the llama model over here, and then you can read my system prompt that

64
00:04:10,730 --> 00:04:11,450
I have given.

65
00:04:12,170 --> 00:04:19,890
So I'm saying here in the system prompt from the model understand the bug report that is added and in

66
00:04:19,890 --> 00:04:26,210
the knowledge added in the knowledge and when anyone sorry when anyone gives the input about any type

67
00:04:26,210 --> 00:04:32,530
of vulnerability or bug, please generate a similar kind of professional report and give the output

68
00:04:32,530 --> 00:04:33,370
to the user.

69
00:04:33,730 --> 00:04:38,490
You can use internet or web search to find information about the bug type if required.

70
00:04:38,890 --> 00:04:43,250
Also give a follow up prompt that if everything is okay or any changes are required.

71
00:04:43,250 --> 00:04:45,730
So this is my system prompt that I have given.

72
00:04:46,290 --> 00:04:47,330
Okay participants.

73
00:04:48,290 --> 00:04:50,370
Then we are going to set up the knowledge.

74
00:04:50,370 --> 00:04:53,850
So I'm going to go and select the knowledge that is RT reporting.

75
00:04:53,850 --> 00:04:55,850
And I'll click on Save and Update.

76
00:04:57,050 --> 00:04:58,890
So I'm going to click on Save and Update.

77
00:04:59,130 --> 00:05:00,890
My model is saved and updated.

78
00:05:00,890 --> 00:05:05,110
And we we can see a nice image appearing over here.

79
00:05:07,590 --> 00:05:09,750
My nice image appearing over here.

80
00:05:10,190 --> 00:05:13,350
So now it's time to interact with the model.

81
00:05:13,390 --> 00:05:14,630
So how do we do that?

82
00:05:14,670 --> 00:05:17,350
So to interact with the model please go to New chat.

83
00:05:17,910 --> 00:05:19,710
Please select the model.

84
00:05:19,710 --> 00:05:22,350
The current model is Bebe vaped.

85
00:05:22,630 --> 00:05:23,150
Okay.

86
00:05:23,230 --> 00:05:26,110
Now let's just give the vulnerability name.

87
00:05:26,390 --> 00:05:33,230
So I'm going to say make a report for SQL injection.

88
00:05:33,670 --> 00:05:39,110
Let's assume I have I'm doing a testing of vulnerability onto a target program.

89
00:05:39,430 --> 00:05:44,710
Maybe let's say a pen test for my organization for an internal application.

90
00:05:44,710 --> 00:05:48,230
And I found a bug, or let's say a bug bounty program, which is a private program.

91
00:05:48,230 --> 00:05:50,750
And I found a bug which is SQL injection.

92
00:05:50,990 --> 00:05:54,270
I don't want to put everything from scratch.

93
00:05:54,390 --> 00:06:00,430
So first let's generate a sample report which contains all the details like summary about the bug or

94
00:06:00,470 --> 00:06:07,010
description And and other things, recommendations, etc. so let us see what and what kind of report

95
00:06:07,010 --> 00:06:09,370
or output we are able to generate with this.

96
00:06:15,170 --> 00:06:21,890
And we can see, uh, a really, really good output has been generated for us.

97
00:06:21,890 --> 00:06:25,050
Let us now try to understand this.

98
00:06:25,050 --> 00:06:30,130
So participants if you see here you can see first is the summary.

99
00:06:30,130 --> 00:06:31,690
So what is SQL injection.

100
00:06:31,690 --> 00:06:34,170
Very nice then description.

101
00:06:34,170 --> 00:06:39,450
When SQL injection occurs when a user input is not sanitized and validated very nice.

102
00:06:39,730 --> 00:06:40,890
Severity is high.

103
00:06:41,250 --> 00:06:43,810
No specific payload required for this vulnerability.

104
00:06:43,810 --> 00:06:47,250
The attacker involves injecting malicious SQL code through user input.

105
00:06:47,290 --> 00:06:50,850
Okay, we can change this to our payload complexity.

106
00:06:50,850 --> 00:06:54,490
Easy done from remote attacker can execute SQL commands.

107
00:06:54,730 --> 00:07:01,090
Affected IP you can specify currently it is not there now to prevent SQL injection it is essential to

108
00:07:01,130 --> 00:07:02,350
sanitize user input.

109
00:07:02,350 --> 00:07:03,590
So that's a recommendation.

110
00:07:03,830 --> 00:07:07,110
And now you can also see a reference that is given by OWASp.

111
00:07:07,670 --> 00:07:10,630
And there is POC section where you can provide the POC.

112
00:07:10,990 --> 00:07:12,310
Isn't that really nice.

113
00:07:12,310 --> 00:07:21,670
You have a draft template ready for you participants that you can use for uh, making an SQL injection

114
00:07:21,670 --> 00:07:23,790
report and submitting it to the program.

115
00:07:24,790 --> 00:07:25,550
Are you all with me?

116
00:07:25,590 --> 00:07:27,230
Participants able to understand?

117
00:07:32,630 --> 00:07:33,310
Yes.

118
00:07:33,310 --> 00:07:35,630
Now let me enable the web search here.

119
00:07:35,950 --> 00:07:40,430
Web search here so that it finds more references as well.

120
00:07:40,630 --> 00:07:43,870
And let us say again generate a.

121
00:07:46,390 --> 00:07:48,830
SQL injection report.

122
00:07:59,750 --> 00:08:00,390
Yes.

123
00:08:00,390 --> 00:08:09,250
So we can include our steps in the command or in the prompt itself, and it will add down those steps.

124
00:08:09,250 --> 00:08:14,770
So we'll what we will do is we will modify the system prompt and ask the system prompt to basically

125
00:08:14,810 --> 00:08:18,490
ask information from the user about.

126
00:08:20,850 --> 00:08:23,650
The steps to reproduce that can be added.

127
00:08:23,930 --> 00:08:27,650
And it will be basically replace that and add it over here okay.

128
00:08:27,890 --> 00:08:34,090
And now you can see uh the report is a little bit more refined report.

129
00:08:34,490 --> 00:08:38,970
So details about the SQL injection report date whenever you want to generate it.

130
00:08:39,210 --> 00:08:41,730
Risk class classification is critical.

131
00:08:41,730 --> 00:08:42,370
Summary.

132
00:08:42,610 --> 00:08:45,090
Vulnerability description exploit path.

133
00:08:45,410 --> 00:08:46,490
Technical details.

134
00:08:46,490 --> 00:08:50,290
There is an SQL injection command as well for your example.

135
00:08:50,290 --> 00:08:51,290
Payload example.

136
00:08:51,530 --> 00:08:53,770
Mitigation steps, recommendation steps.

137
00:08:54,210 --> 00:08:55,290
References steps.

138
00:08:55,530 --> 00:09:00,770
And now it says please confirm that you would like me to provide additional information on the report.

139
00:09:00,890 --> 00:09:03,470
Schedule a meeting to discuss remediation.

140
00:09:03,470 --> 00:09:05,990
Generate an updated report with change in the findings.

141
00:09:05,990 --> 00:09:07,990
Please respond with any above points.

142
00:09:08,150 --> 00:09:14,230
So now we are going to say, uh, we want to change something in the report.

143
00:09:16,270 --> 00:09:18,270
So I'm going to say choose option three.

144
00:09:20,550 --> 00:09:25,110
And add steps to reproduce.

145
00:09:28,550 --> 00:09:36,310
Where I have found a SQL injection in injection in test

146
00:09:37,390 --> 00:09:42,670
p.com/uh let's say index.

147
00:09:44,510 --> 00:09:47,310
This is just for the dummy reference.

148
00:09:47,310 --> 00:09:50,870
Let's let's say we found SQL injection in the artist parameter.

149
00:09:57,470 --> 00:10:00,030
Let's hit enter and let's wait for the outcome.

150
00:10:29,900 --> 00:10:30,340
Okay.

151
00:10:30,740 --> 00:10:35,140
So participants, if you see now you have a much better report generated.

152
00:10:35,460 --> 00:10:37,420
So SQL injection on test PHP.

153
00:10:37,660 --> 00:10:38,260
Nice.

154
00:10:38,700 --> 00:10:46,660
Uh, this report details the discovery of an SQL injection found on PHP Web.com artist parameter, which

155
00:10:46,700 --> 00:10:48,980
allows attacker to inject malicious SQL code.

156
00:10:49,020 --> 00:10:49,700
Nice.

157
00:10:50,060 --> 00:10:51,700
Let's go to the exploit path.

158
00:10:52,300 --> 00:10:56,660
Uh, identify vulnerable endpoint, inject malicious code through the artist parameter.

159
00:10:56,660 --> 00:10:57,500
Very nice.

160
00:10:57,660 --> 00:11:00,820
And you would be able to see the code is executing in technical details.

161
00:11:00,820 --> 00:11:03,720
We can see artist equals to is being added.

162
00:11:03,760 --> 00:11:05,600
Our test parameter is also added.

163
00:11:05,880 --> 00:11:07,920
An exploitable query is also been given.

164
00:11:07,920 --> 00:11:09,640
So this is a dummy query here.

165
00:11:09,840 --> 00:11:15,640
You can definitely replace this with your query or command from SQL map tool, or maybe manually.

166
00:11:15,640 --> 00:11:22,280
If you have done that, it is trying to give you the steps to reproduce in which on the current URL

167
00:11:22,280 --> 00:11:23,040
endpoint.

168
00:11:23,200 --> 00:11:29,240
In the artist parameter, we have attempted to add a payload, which is an SQL injection or query,

169
00:11:29,760 --> 00:11:34,320
and we can observe the response from the server, which should indicate a successful execution of the

170
00:11:34,320 --> 00:11:35,240
injected code.

171
00:11:35,840 --> 00:11:36,600
Very nice.

172
00:11:36,600 --> 00:11:43,640
So now it gives give us more personalized, uh, report for the given target.

173
00:11:43,800 --> 00:11:47,640
And it has filled all the gaps that were there earlier.

174
00:11:47,960 --> 00:11:54,080
So this is now much more refined or personalized report for the given target, where we specified the

175
00:11:54,120 --> 00:11:58,640
URL and the parameter that was expected to be vulnerable.

176
00:11:58,880 --> 00:12:03,520
And then mitigation recommendation and references, as you can see over here.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,040 --> 00:00:04,880
What you can do is you can simply, uh, whenever you find a vulnerability.

2
00:00:04,880 --> 00:00:08,080
So let us say we found a vulnerability on test PHP.

3
00:00:10,280 --> 00:00:15,120
Um, categories, let's say posters.

4
00:00:15,400 --> 00:00:18,760
Let's say this is vulnerable cat equals to one is vulnerable.

5
00:00:18,760 --> 00:00:23,840
And when I put an XSS payload over here, uh, it basically triggers an XSS.

6
00:00:23,840 --> 00:00:25,080
So I'm going to copy this.

7
00:00:25,680 --> 00:00:30,080
Go to my local setup my LM.

8
00:00:30,960 --> 00:00:42,560
And I'm going to say hey I found a XSS vulnerability in the URL okay.

9
00:00:43,200 --> 00:00:50,000
Generate uh professional report.

10
00:00:50,760 --> 00:00:55,000
Now let us see how does it gives us the outcome or output that we need.

11
00:00:55,120 --> 00:01:01,240
So we have specified that we have found a bug that is XSS in the target.

12
00:01:01,520 --> 00:01:03,440
And the parameter is cat.

13
00:01:03,440 --> 00:01:07,800
Let us see if it understands that automatically and generates this similar kind of professional report

14
00:01:07,800 --> 00:01:08,280
for us.

15
00:01:08,800 --> 00:01:09,080
Okay.

16
00:01:09,080 --> 00:01:10,480
So let's wait for the output.

17
00:01:47,840 --> 00:01:48,360
Okay.

18
00:01:49,040 --> 00:01:49,640
Very nice.

19
00:01:49,640 --> 00:01:51,400
We have the output now.

20
00:01:51,560 --> 00:01:54,840
So we are able to see a report that is successfully generated.

21
00:01:55,240 --> 00:01:59,120
Uh cross site scripting report vulnerability name is correct.

22
00:01:59,120 --> 00:02:01,760
You can enter the date from next time onwards.

23
00:02:01,760 --> 00:02:07,200
We'll ask it to add the date as well of which is today's date.

24
00:02:07,200 --> 00:02:10,150
So in your system prompt actually you can modify that.

25
00:02:10,510 --> 00:02:18,750
So so what will happen automatically uh, when you are writing this, the report date, uh, is automatically

26
00:02:18,750 --> 00:02:19,990
updated to the latest date.

27
00:02:19,990 --> 00:02:21,430
So we'll do that in a moment.

28
00:02:21,670 --> 00:02:22,870
Risk level summary.

29
00:02:22,870 --> 00:02:24,150
Vulnerability description.

30
00:02:24,190 --> 00:02:24,470
Okay.

31
00:02:24,510 --> 00:02:24,990
Nice.

32
00:02:25,230 --> 00:02:27,110
You can see where you are coming here.

33
00:02:27,630 --> 00:02:30,750
Uh, injecting the malicious JavaScript code in the cat parameter.

34
00:02:30,750 --> 00:02:31,510
Very nice.

35
00:02:31,830 --> 00:02:33,670
Our injection point is cat parameter.

36
00:02:33,670 --> 00:02:34,390
Very good.

37
00:02:34,790 --> 00:02:35,830
Exploitable payload.

38
00:02:35,830 --> 00:02:38,790
It also gave a sample exploitation payload.

39
00:02:39,790 --> 00:02:40,990
Steps to reproduce.

40
00:02:40,990 --> 00:02:43,030
It told cat parameter is vulnerable.

41
00:02:43,550 --> 00:02:50,030
Uh, for example, an alert XSS attack payload can be given and we can see the response which indicates

42
00:02:50,230 --> 00:02:52,150
the injected code has been successful.

43
00:02:52,430 --> 00:02:55,390
And then other important part of the report like mitigations.

44
00:02:55,750 --> 00:02:59,670
It correctly said that please use input validation and sanitization.

45
00:02:59,910 --> 00:03:07,710
Use content security policy regularly update dependencies, correct recommendations and references from

46
00:03:07,750 --> 00:03:09,830
official OWASp and Sans.

47
00:03:10,110 --> 00:03:16,350
So we have got a pretty much very nice and decent are report that has been generated for us.

48
00:03:16,630 --> 00:03:23,190
So you can utilize this always to save your time on report writing by simply giving the target URL to

49
00:03:24,390 --> 00:03:29,550
your LLM and let it generate the entire report for you, which you can directly copy it from here.

50
00:03:29,590 --> 00:03:35,390
Not only that, if you want this you to be in the PDF format, you can go to download and choose the

51
00:03:35,390 --> 00:03:36,430
PDF format.

52
00:03:39,950 --> 00:03:40,390
Okay.

53
00:03:40,990 --> 00:03:47,110
Although you would not directly send this output from the from here, instead, you can simply copy

54
00:03:47,110 --> 00:03:53,950
the the main part of the report that you want, uh, with minor changes that you want to make here and

55
00:03:53,950 --> 00:03:54,190
there.

56
00:03:54,190 --> 00:03:55,430
And then you can send it.

57
00:03:56,430 --> 00:03:56,750
Okay.

58
00:03:56,790 --> 00:04:04,550
Now let me modify the system prompt and let's say please input the correct date or current date appropriately.

59
00:04:06,790 --> 00:04:14,230
Please add the current date in the report date field.

60
00:04:17,060 --> 00:04:17,700
Save.

61
00:04:19,140 --> 00:04:24,220
Go to SQL injection and we are going to say again the same thing this time.

62
00:04:27,100 --> 00:04:28,380
Let us see the response.

63
00:04:58,140 --> 00:04:58,500
Okay.

64
00:04:58,500 --> 00:05:03,020
We got the output are not sure why it says date of report generation okay.

65
00:05:03,060 --> 00:05:06,900
It should have instead generated the report.

66
00:05:09,420 --> 00:05:10,540
With the current date.

67
00:05:11,140 --> 00:05:14,620
Let us see if it is added appropriately.

68
00:05:27,020 --> 00:05:28,420
Maybe I'll do a new chat.

69
00:05:29,580 --> 00:05:29,940
Okay.

70
00:05:32,540 --> 00:05:40,300
Generate a SSR report for it should be colon slash slash example.com.

71
00:05:40,300 --> 00:05:43,540
Slash id equals to one.

72
00:05:46,540 --> 00:05:48,340
Uh, yes, that is right.

73
00:06:06,980 --> 00:06:07,380
Hmm.

74
00:06:07,580 --> 00:06:12,100
I think this is not pretty much the right output that we expected, because it is giving the same report

75
00:06:12,100 --> 00:06:14,100
that I have saved and saved in the background.

76
00:06:14,820 --> 00:06:21,860
Uh, not sure why, but yeah, I'll again try the same thing and get a better response again.

77
00:06:24,180 --> 00:06:32,620
Uh, so you guys can basically try the same thing, and I am definitely sure that it will help you generate

78
00:06:32,620 --> 00:06:34,340
the report appropriately.

79
00:06:34,740 --> 00:06:43,580
Maybe what I'll do is I'll give a better system prompt, cancel this, analyze the report, and use

80
00:06:43,580 --> 00:06:46,860
embedded knowledge to generate well structured professional report format.

81
00:06:47,540 --> 00:06:48,100
Yes.

82
00:06:49,900 --> 00:06:54,940
Uh, when a user submits information about a vulnerability or bug, respond with comprehensive technical

83
00:06:54,980 --> 00:06:55,620
write up.

84
00:06:55,860 --> 00:06:56,460
If needed.

85
00:06:56,500 --> 00:06:57,940
Utilize internet or web search.

86
00:06:57,940 --> 00:06:59,940
Always include the current date and the report date field.

87
00:06:59,940 --> 00:07:01,620
Additionally, provide clear follow up prompts.

88
00:07:01,620 --> 00:07:02,300
Very nice.

89
00:07:02,740 --> 00:07:04,820
So I'm going to say save.

90
00:07:07,420 --> 00:07:08,260
New chat.

91
00:07:12,260 --> 00:07:19,380
Generate a report for XSS which is found on.

92
00:07:54,290 --> 00:07:59,010
Okay, we have got the output this time and it has not added the report as well.

93
00:07:59,250 --> 00:08:02,650
Let me enable the web search option and again try that.

94
00:08:03,570 --> 00:08:06,890
Sorry it has not added the date but that is fine.

95
00:08:06,930 --> 00:08:10,210
I think that you can do it manually as well.

96
00:08:10,250 --> 00:08:14,450
Or maybe modify the prompt once again so it helps you do that stuff.

97
00:08:15,130 --> 00:08:18,610
I hope participants you have got familiar with how to generate reports.

98
00:08:19,010 --> 00:08:26,410
Uh, it is it is always better that you give more knowledge to the model so that it generates, uh.

99
00:08:29,330 --> 00:08:32,650
Uh, reports of your format that you are looking for.

100
00:08:34,210 --> 00:08:34,610
Okay.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 17: Nuclei & YAML Automation

1
00:00:01,960 --> 00:00:02,800
Perfect.

2
00:00:02,800 --> 00:00:08,760
So now let's move ahead to exploit template generation.

3
00:00:09,840 --> 00:00:12,440
So I'm going to go to Nuclear Templates participant.

4
00:00:12,840 --> 00:00:23,760
And we are going to feed some nuclei template of get and post type to our model so that it understands

5
00:00:23,760 --> 00:00:25,440
about how these templates work.

6
00:00:25,840 --> 00:00:32,440
So I'm going to go to http http and I'm going to take some CV base templates.

7
00:00:32,600 --> 00:00:40,080
Or maybe let me just search for some templates that I have submitted and contributed here.

8
00:00:41,200 --> 00:00:42,880
Maybe let's let me take this one.

9
00:00:43,840 --> 00:00:51,840
So Moodle access Moodle is a very famous LMS that is used worldwide with many universities and corporate

10
00:00:51,840 --> 00:00:52,960
organization.

11
00:00:53,520 --> 00:01:04,550
Uh, I managed to find a XSS vulnerability into, uh, a version of Moodle Wherein you can see the path

12
00:01:04,550 --> 00:01:06,150
when we provide like this.

13
00:01:06,670 --> 00:01:08,830
That is mod, LTI or PHP.

14
00:01:08,870 --> 00:01:10,590
This is the fixed hardcoded path.

15
00:01:10,870 --> 00:01:12,630
And here I am able to give the payload.

16
00:01:13,030 --> 00:01:19,310
So when a HTTP request is being sent by the nuclei tool in the response, the matcher condition matches

17
00:01:19,310 --> 00:01:21,990
for the output which has the same random string.

18
00:01:21,990 --> 00:01:28,510
So this is the variable which nuclei will add automatically when it is going to run, and JavaScript

19
00:01:28,510 --> 00:01:31,270
alert in the response as well if it is reflected.

20
00:01:31,710 --> 00:01:39,670
If this is not, if it if this is reflected as it is in the response not converted to HTML encoding

21
00:01:39,670 --> 00:01:43,510
or any other type of encoding and appears like this.

22
00:01:43,830 --> 00:01:48,310
And status code is 200 okay, output is in text HTML format.

23
00:01:48,470 --> 00:01:54,230
Then this will give output as XSS found successfully.

24
00:01:54,630 --> 00:01:59,550
Okay, so uh, if you want we can also search for some Moodle XSS.

25
00:01:59,550 --> 00:01:59,650
Success.

26
00:02:00,010 --> 00:02:00,490
So.

27
00:02:00,530 --> 00:02:01,650
Moodle.

28
00:02:02,730 --> 00:02:03,130
Moodle.

29
00:02:03,170 --> 00:02:03,530
Target.

30
00:02:03,570 --> 00:02:04,010
Sorry.

31
00:02:04,210 --> 00:02:10,090
So I'm going to say search for any websites that contains Moodle.

32
00:02:12,810 --> 00:02:17,730
Okay so here this is the official websites and open source LMS.

33
00:02:18,170 --> 00:02:23,330
And there are multiple websites in this world uh which are using Moodle.

34
00:02:23,330 --> 00:02:27,770
For example Bitnami you can see is powered by Moodle.

35
00:02:27,770 --> 00:02:32,610
And there are multiple more websites that are using Moodle.

36
00:02:32,850 --> 00:02:34,530
So let me search for Moodle.

37
00:02:43,170 --> 00:02:53,330
Okay so I found a Google Doc participants which we can use to search for Moodle based targets in your

38
00:02:53,370 --> 00:02:55,210
Moodle login index dot PHP.

39
00:02:55,210 --> 00:02:57,650
And now we can see some targets running Moodle.

40
00:02:57,930 --> 00:03:04,560
So let me go to maybe 4 or 5 and let us see if there are vulnerable or no.

41
00:03:04,600 --> 00:03:05,000
Okay.

42
00:03:06,480 --> 00:03:13,720
So to find if these targets are vulnerable I'm going to run the nuclei template to do that.

43
00:03:13,720 --> 00:03:23,720
It's very simple nuclei hyphen you and I'm so sorry nuclei hyphen u u stands for the URL.

44
00:03:24,160 --> 00:03:25,840
Uh I'm going to take this URL.

45
00:03:26,600 --> 00:03:37,120
Let's take let's take this website for instance and specify the t flag T means the template.

46
00:03:37,640 --> 00:03:44,200
Please download this template repository locally into your system and provide the path of which template

47
00:03:44,200 --> 00:03:45,120
you want to use.

48
00:03:45,520 --> 00:03:50,200
So I'm going to use Moodle access dot yml which is inside Moodle folder.

49
00:03:50,320 --> 00:03:54,240
Inside vulnerability inside HTTP folder inside nuclei template.

50
00:03:54,240 --> 00:04:04,750
So nuclei templates HTTP slash Vulnerabilities Moodle and Moodle .0..

51
00:04:04,790 --> 00:04:05,350
YML.

52
00:04:05,670 --> 00:04:06,630
This is the template.

53
00:04:06,630 --> 00:04:07,630
Let's hit enter.

54
00:04:14,950 --> 00:04:16,350
Target loaded for scan.

55
00:04:16,350 --> 00:04:17,310
No result found.

56
00:04:17,310 --> 00:04:19,750
This means the target is not vulnerable.

57
00:04:19,790 --> 00:04:21,310
Okay no problem.

58
00:04:21,310 --> 00:04:25,710
We will add the next target now and try to scan that if it is vulnerable or no.

59
00:04:33,590 --> 00:04:36,110
Let's take this one for instance.

60
00:04:39,830 --> 00:04:40,750
Not vulnerable.

61
00:04:42,550 --> 00:04:43,710
Let's take this one.

62
00:04:54,590 --> 00:04:54,870
Okay.

63
00:04:54,990 --> 00:04:55,830
Not vulnerable.

64
00:05:05,570 --> 00:05:08,690
Uh, this is a old vulnerability that I have reported.

65
00:05:08,690 --> 00:05:14,370
It's like 2 to 3 years old, so we might not immediately find a target that is vulnerable.

66
00:05:15,210 --> 00:05:16,570
But let us see.

67
00:05:16,610 --> 00:05:16,930
Okay.

68
00:05:16,970 --> 00:05:18,490
This one is also not vulnerable.

69
00:05:19,010 --> 00:05:20,570
Let's test this one.

70
00:05:32,290 --> 00:05:32,730
Okay.

71
00:05:33,130 --> 00:05:34,690
Now I want more targets.

72
00:05:34,690 --> 00:05:35,690
So I'm going to copy this.

73
00:05:35,690 --> 00:05:38,690
Doc, go to our lama and I'm going to say hey.

74
00:05:40,730 --> 00:05:52,810
Hey use this Google doc and find the websites that appear and list them in a table form for me.

75
00:05:53,130 --> 00:05:58,360
Make the list very exhaustive and find.

76
00:05:59,280 --> 00:06:03,600
Find at least 1010 targets.

77
00:06:04,320 --> 00:06:05,880
Ten websites.

78
00:06:09,160 --> 00:06:10,520
Ten domains, let's say.

79
00:06:15,600 --> 00:06:18,760
Let's get the output of the targets from here.

80
00:06:27,440 --> 00:06:31,240
We can see more more docs that it is trying.

81
00:06:45,040 --> 00:06:45,480
Uh.

82
00:06:51,240 --> 00:06:51,920
Okay.

83
00:06:53,000 --> 00:06:54,920
List the websites

84
00:06:56,910 --> 00:07:03,270
Found on web search using this.

85
00:07:09,390 --> 00:07:10,430
Now we'll wait for this.

86
00:07:10,750 --> 00:07:17,710
And till then, we can also look up for some more targets that basically runs Moodle.

87
00:07:18,830 --> 00:07:26,510
Uh, our objective primarily is to identify certain websites that might be running Moodle here, for

88
00:07:26,510 --> 00:07:27,190
instance.

89
00:07:27,430 --> 00:07:30,670
And we can exploit it or we can basically do an exercise.

90
00:07:30,750 --> 00:07:31,190
Okay.

91
00:07:31,390 --> 00:07:37,910
Now, uh, you should be able to see an output here which says uh, target detected successfully miss

92
00:07:37,910 --> 00:07:38,630
Vulnerable.

93
00:07:38,830 --> 00:07:47,670
So so now what we can do is, uh, let us assume we we found a valid target, and this template is working

94
00:07:47,710 --> 00:07:49,030
absolutely fine.

95
00:07:49,470 --> 00:07:55,630
Okay, now we can we can actually take up a more one more target from maybe Shodan.

96
00:07:58,530 --> 00:08:02,970
I'm sure there would be some old targets from this entire list.

97
00:08:33,690 --> 00:08:34,090
Okay.

98
00:08:46,770 --> 00:08:47,290
Thanks.

99
00:08:47,690 --> 00:08:49,170
Uh, we've got a target.

100
00:08:49,170 --> 00:08:51,970
This target is currently vulnerable to modal XSS.

101
00:08:53,090 --> 00:08:56,760
I'm going to specify this target now to a template.

102
00:09:04,600 --> 00:09:05,960
And we hit enter.

103
00:09:07,760 --> 00:09:08,240
Yes.

104
00:09:08,520 --> 00:09:16,480
And participants, if you observe here now, uh, we have got an output which says Moodle, XSS, http

105
00:09:16,480 --> 00:09:21,120
template medium vulnerability has been found.

106
00:09:21,120 --> 00:09:22,640
And this is the alert.

107
00:09:22,840 --> 00:09:25,640
This is the random string that was added in the runtime.

108
00:09:25,840 --> 00:09:28,080
So yeah we successfully found this.

109
00:09:28,080 --> 00:09:28,800
Very nice.

110
00:09:29,200 --> 00:09:38,200
Now I can not only specify one URL like this, I can actually make a list of targets.

111
00:09:38,200 --> 00:09:40,960
So I'll make a file called targets dot txt.

112
00:09:41,200 --> 00:09:44,160
And I can add a bunch of targets in this file.

113
00:09:44,480 --> 00:09:46,160
So I'll do that now.

114
00:09:46,320 --> 00:09:51,600
So I'm going to copy this and take a few targets from here.

115
00:09:59,990 --> 00:10:01,110
Just for the reference.

116
00:10:01,110 --> 00:10:02,950
I'll take maybe five of them.

117
00:10:31,990 --> 00:10:32,470
Okay.

118
00:10:32,470 --> 00:10:33,630
Let's try on these.

119
00:10:33,670 --> 00:10:33,870
Okay.

120
00:10:33,870 --> 00:10:39,390
So I'm going to just change the flag.

121
00:10:45,750 --> 00:10:47,790
From you are.

122
00:10:47,790 --> 00:10:52,310
So basically you means the URL and we don't want to specify the URL now.

123
00:10:52,510 --> 00:10:57,690
Rather we want to specify the target list.

124
00:10:57,690 --> 00:11:02,610
So I'm going to go to nuclei in the usage.

125
00:11:03,450 --> 00:11:03,850
Yeah.

126
00:11:04,330 --> 00:11:08,130
So you can scan multiple targets with the help of list feature.

127
00:11:08,250 --> 00:11:10,610
So I'm going to say hyphen list.

128
00:11:11,570 --> 00:11:13,930
And the list name is targets dot txt.

129
00:11:14,170 --> 00:11:16,250
So now what we are doing we are scaling up.

130
00:11:16,410 --> 00:11:22,810
We are scaling to scan multiple targets with nuclei for a current vulnerability type which is this.

131
00:11:22,810 --> 00:11:23,810
Let's hit enter.

132
00:11:25,010 --> 00:11:25,330
Okay.

133
00:11:25,370 --> 00:11:26,650
And it found that.

134
00:11:29,370 --> 00:11:34,770
This given website is currently vulnerable and which was our earlier website.

135
00:11:34,810 --> 00:11:35,250
Yeah.

136
00:11:35,250 --> 00:11:37,770
So this was our earlier website which was vulnerable.

137
00:11:37,770 --> 00:11:38,370
Did you see that.

138
00:11:38,370 --> 00:11:41,330
We found two targets to be vulnerable now.

139
00:11:41,850 --> 00:11:46,610
So this is my platform one which is vulnerable.

140
00:11:46,770 --> 00:11:50,890
And earlier we had uh it leon.edu.

141
00:11:51,090 --> 00:11:54,850
So now we have two targets which are vulnerable as we can see over here.

142
00:11:55,010 --> 00:11:55,570
Perfect.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,120 --> 00:00:01,120
Now participants.

2
00:00:01,440 --> 00:00:04,160
Our objective is not to run nuclei on these targets.

3
00:00:04,160 --> 00:00:05,000
We can do that.

4
00:00:05,400 --> 00:00:13,840
Our objective is to generate similar kind of templates with the help of the LM that we have.

5
00:00:13,840 --> 00:00:22,440
That will help us basically to convert our HTTP request that we have, that we have into similar kind

6
00:00:22,440 --> 00:00:30,480
of templates so that we can scale it across not single, but hundreds of other such types of targets.

7
00:00:30,960 --> 00:00:41,920
Hence, I'm going to feed the entire nuclei template repository as a knowledge base to the LM model

8
00:00:41,920 --> 00:00:50,600
and ask it to create similar kind of HTTP templates for us in future, based on raw requests that we

9
00:00:50,600 --> 00:00:53,160
specify from burp suit.

10
00:00:53,200 --> 00:00:53,520
Okay.

11
00:00:53,560 --> 00:00:54,960
So I'm going to do that now.

12
00:00:55,240 --> 00:01:00,560
So let us simply go to New Chat and say hi.

13
00:01:02,290 --> 00:01:09,570
Read this nuclei template and remember it.

14
00:01:10,690 --> 00:01:16,050
Uh, I it is always better that you create a new model, but I'm going to create a temporary chart and

15
00:01:16,050 --> 00:01:28,010
show you I will paste raw HTTP requests from burp suit repeater tab.

16
00:01:29,450 --> 00:01:43,970
You need to make similar nuclei y ml templates for me in future, which are error free in this.

17
00:02:10,510 --> 00:02:10,870
Okay.

18
00:02:10,870 --> 00:02:14,470
Please go ahead and paste the raw HTTP request and it will do that for us.

19
00:02:14,870 --> 00:02:19,950
Uh, did you see we also did not specify the nuclei template.

20
00:02:20,150 --> 00:02:25,990
It automatically understood that from multiple website sources that we had because my web search was

21
00:02:25,990 --> 00:02:26,430
on.

22
00:02:26,430 --> 00:02:27,230
Very nice.

23
00:02:27,270 --> 00:02:34,550
Now let us go that go ahead and create a template exploit template for a vulnerability.

24
00:02:35,350 --> 00:02:37,030
So let's go to proxy.

25
00:02:39,990 --> 00:02:40,990
Open browser.

26
00:02:41,630 --> 00:02:43,390
Let me open a pre-configured browser.

27
00:02:43,430 --> 00:02:44,150
Browser.

28
00:02:44,750 --> 00:02:46,390
Uh let's go to test PHP.

29
00:02:47,510 --> 00:02:49,430
Um artist.

30
00:02:52,790 --> 00:02:53,310
Okay.

31
00:02:53,310 --> 00:02:55,750
Let me see if this is vulnerable to XSS.

32
00:02:56,350 --> 00:02:57,790
This artist parameter.

33
00:02:57,790 --> 00:02:59,110
So I'm going to say script.

34
00:03:01,520 --> 00:03:02,000
Script.

35
00:03:02,000 --> 00:03:05,040
Close alert one.

36
00:03:06,560 --> 00:03:07,160
Very nice.

37
00:03:07,160 --> 00:03:07,680
It is one.

38
00:03:08,360 --> 00:03:10,400
So let's go to burp.

39
00:03:11,000 --> 00:03:12,120
Let's go to burp.

40
00:03:13,640 --> 00:03:17,840
Capture this request and send it to the repeater tab.

41
00:03:17,840 --> 00:03:18,240
Now.

42
00:03:20,120 --> 00:03:21,480
Yes, this is working.

43
00:03:21,680 --> 00:03:25,680
So my payload is successfully executing.

44
00:03:25,880 --> 00:03:27,120
As we can see here.

45
00:03:27,680 --> 00:03:28,240
And.

46
00:03:32,760 --> 00:03:38,360
In the response also we can see alert one coming up over here.

47
00:03:39,760 --> 00:03:41,360
You can see my payload is coming as it is.

48
00:03:41,360 --> 00:03:41,760
Excellent.

49
00:03:41,760 --> 00:03:44,560
So I'm now going to copy this request.

50
00:03:44,560 --> 00:03:47,000
So I'm going to use the copy feature of burp.

51
00:03:47,640 --> 00:03:56,920
Go to our model and say Create Nuclei template for this.

52
00:03:59,640 --> 00:04:04,530
Let us see how It is going to create the template for us okay.

53
00:04:04,570 --> 00:04:06,290
And then we'll test out the template.

54
00:04:18,810 --> 00:04:19,530
Awesome.

55
00:04:35,210 --> 00:04:35,810
Did you see that?

56
00:04:35,810 --> 00:04:36,690
Participants.

57
00:04:44,970 --> 00:04:46,010
Very nice.

58
00:04:47,290 --> 00:04:50,010
Now it's time to test it out if this is okay.

59
00:04:50,450 --> 00:04:52,730
So let's copy this.

60
00:04:53,210 --> 00:04:56,810
You can also save this, uh, in the back end.

61
00:04:56,810 --> 00:04:57,970
Or you can copy this.

62
00:04:58,010 --> 00:05:02,990
Now, once you copy this, I am I am very keen to see if this is correct or no.

63
00:05:03,190 --> 00:05:08,990
So I'm going to go to YAML lint, which is a YAML validator based here, and see if there are any errors.

64
00:05:09,910 --> 00:05:10,350
Perfect.

65
00:05:10,350 --> 00:05:11,510
There were no errors.

66
00:05:11,950 --> 00:05:15,390
Very happy to see this that it is able to generate a template for us.

67
00:05:16,350 --> 00:05:24,350
Uh, now we can basically run this template and see the outcome of how, uh, how it is able to work.

68
00:05:24,630 --> 00:05:29,270
And are we able to get it, get the bug or.

69
00:05:29,310 --> 00:05:29,470
No.

70
00:05:29,510 --> 00:05:29,870
Okay.

71
00:05:30,590 --> 00:05:40,550
So now we can go ahead in our terminal, generate a create a YAML template so we can say access custom

72
00:05:40,590 --> 00:05:42,310
dot y AML.

73
00:05:42,750 --> 00:05:43,910
Paste it over here.

74
00:05:44,110 --> 00:05:51,070
And then we can run this uh using nuclei uh for the current target that we have for our choice.

75
00:05:51,310 --> 00:05:57,230
And then we would be able to see the output that is able to identify that the target is vulnerable.

76
00:05:57,590 --> 00:06:02,910
So that way it will be very, very helpful for us to determining if the target is vulnerable.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,400 --> 00:00:07,200
The second way, or the recommended way, is that you make a in your workspace a knowledge base with

2
00:00:07,200 --> 00:00:17,040
all the templates in the background, and then ask your model to to generate an appropriate, uh, or

3
00:00:17,080 --> 00:00:25,040
any kind of nuclear template of your choice that you want, uh, so you can go to knowledge, go to

4
00:00:25,080 --> 00:00:28,200
plus nuclei templates.

5
00:00:33,800 --> 00:00:35,760
And we are going to provide the templates here.

6
00:01:04,480 --> 00:01:05,040
Okay.

7
00:01:05,080 --> 00:01:10,920
So I think files are added, but folders are not added, it seems.

8
00:01:13,800 --> 00:01:17,440
Let's say I upload a directory downloads.

9
00:01:43,680 --> 00:01:45,200
So it is going to take some time.

10
00:01:45,200 --> 00:01:49,960
You can see there are 10,000 are approximate 10,000 files.

11
00:01:49,960 --> 00:01:51,560
So what are these 10,000 files.

12
00:01:51,560 --> 00:01:54,560
Actually these 10,000 sorry.

13
00:01:54,920 --> 00:02:01,880
These 10,000 files are actually templates uh, exploit templates.

14
00:02:02,000 --> 00:02:08,320
So now we are enhancing the knowledge of our model with nuclei templates.

15
00:02:08,520 --> 00:02:16,910
So it is going to better perform when we ask questions specific to a template, or we ask it to create

16
00:02:16,910 --> 00:02:23,550
a template, because now it would have its own older knowledge so that it generates better formatted

17
00:02:24,030 --> 00:02:30,590
and error free templates for us that are directly compatible for us to run it with nuclei.

18
00:02:30,630 --> 00:02:33,670
Okay, so it is still adding files over here.

19
00:02:33,670 --> 00:02:38,390
It might take some more time to add that to the knowledge base.

20
00:02:40,510 --> 00:02:42,110
Because there is only 2% done.

21
00:02:42,110 --> 00:02:44,670
So we'll keep that happening in the background.

22
00:02:44,910 --> 00:02:49,110
And let's till then create a new model workspace.

23
00:02:49,830 --> 00:02:50,990
Let's click on plus.

24
00:02:53,670 --> 00:02:59,670
New cli ai template generator.

25
00:03:01,990 --> 00:03:03,430
Let's choose llama model.

26
00:03:09,190 --> 00:03:09,590
Okay.

27
00:03:15,110 --> 00:03:24,390
Read And understand the knowledge of nuclei.

28
00:03:25,150 --> 00:03:31,070
Why ML templates thoroughly when a user.

29
00:03:34,390 --> 00:03:42,990
Gives you a HTTP request from burp repeater or anywhere?

30
00:03:43,190 --> 00:03:49,030
Maybe if I even give a curl request, it should change that repeater tab or curl request.

31
00:03:50,750 --> 00:03:57,430
Convert it into a nuclei compatible.

32
00:04:03,270 --> 00:04:05,390
Email template.

33
00:04:07,230 --> 00:04:10,350
And if output.

34
00:04:12,470 --> 00:04:14,950
Then let's click on save.

35
00:04:17,030 --> 00:04:22,580
Uh, let us see what is the output that is generated now because our data or knowledge is still being

36
00:04:22,900 --> 00:04:24,780
upgraded in the back end.

37
00:04:25,100 --> 00:04:26,380
So let's go to new chat.

38
00:04:26,740 --> 00:04:34,020
Let's use nuclear template generator and let's simply go ahead and put that request.

39
00:04:39,140 --> 00:04:40,900
Here is your sorry.

40
00:04:41,180 --> 00:04:42,580
Here is your request.

41
00:04:50,460 --> 00:04:52,100
So you can see now it is searching knowledge.

42
00:04:52,660 --> 00:04:53,980
Uh, I just said hi.

43
00:04:54,380 --> 00:04:56,020
Here is your request.

44
00:04:56,020 --> 00:04:56,620
And.

45
00:04:58,660 --> 00:04:59,260
Let's see.

46
00:04:59,300 --> 00:05:00,620
Let's wait for the output.

47
00:05:18,860 --> 00:05:28,690
Oh, I think our container crashed because we have we have uploaded more than required large files.

48
00:05:31,770 --> 00:05:32,050
Mm.

49
00:05:38,210 --> 00:05:38,770
Yes.

50
00:05:39,250 --> 00:05:43,610
Uh, we are trying to write more than required data.

51
00:05:43,810 --> 00:05:46,730
Because of which I think our container is crashing.

52
00:05:47,250 --> 00:05:55,450
Uh, so I think, uh, this demonstration is sufficient for you to understand that how it is, how it

53
00:05:55,450 --> 00:05:57,290
is going to generate templates.

54
00:05:57,690 --> 00:05:58,610
Uh, it crashed.

55
00:05:58,610 --> 00:06:00,330
It did not generate it appropriately.

56
00:06:00,330 --> 00:06:02,690
We wanted it to generate a YAML template.

57
00:06:02,690 --> 00:06:03,690
So I'm going to give it again.

58
00:06:03,690 --> 00:06:06,530
And I'm going to ask it to generate a YAML template.

59
00:06:07,770 --> 00:06:09,730
Generate a nuclei.

60
00:06:10,810 --> 00:06:13,210
Why a template.

61
00:06:21,770 --> 00:06:22,930
In this format.

62
00:06:48,250 --> 00:06:48,890
Nice.

63
00:06:59,170 --> 00:06:59,810
Participants.

64
00:06:59,810 --> 00:07:02,170
You can see it is generating the report very nicely.

65
00:07:09,930 --> 00:07:11,770
Uh, it will keep on crashing.

66
00:07:11,770 --> 00:07:14,650
This is because two things are happening simultaneously.

67
00:07:15,410 --> 00:07:18,490
Uh, first thing is our knowledge base is getting updated.

68
00:07:18,530 --> 00:07:23,890
Second, we are trying to use it in runtime because of which we are getting this errors.

69
00:07:24,090 --> 00:07:26,370
Uh, but I hope you got the got the idea.

70
00:07:26,410 --> 00:07:32,450
It was generating a valid YAML template that you could that you could use it in future.

71
00:07:33,850 --> 00:07:34,090
Yes.

72
00:07:34,090 --> 00:07:34,650
Participants.

73
00:07:34,650 --> 00:07:36,730
Are you all with me able to understand it?

74
00:07:37,330 --> 00:07:37,570
Please.

75
00:07:37,570 --> 00:07:38,490
Give me a heads up.

76
00:07:47,890 --> 00:07:48,530
Yes.

77
00:07:49,490 --> 00:07:50,250
Excellent.

78
00:08:00,690 --> 00:08:01,170
Okay.

79
00:08:02,610 --> 00:08:03,050
Very good.

80
00:08:03,050 --> 00:08:03,890
Participants.

81
00:08:04,770 --> 00:08:07,810
So now you have your own nuclear template generator with.

82
00:08:09,250 --> 00:08:09,810
Yes.

83
00:08:10,050 --> 00:08:10,690
No problem.

84
00:08:10,690 --> 00:08:12,050
You can learn about nuclei.

85
00:08:12,050 --> 00:08:15,970
It's an amazing open source vulnerability scanner that is going to help you a lot.

86
00:08:18,170 --> 00:08:25,290
And this nuclei template generator is again going to be very very helpful for you because it is going

87
00:08:25,290 --> 00:08:31,810
to uh help you generate multiple types of nuclei templates that will be very, very useful for you later

88
00:08:31,810 --> 00:08:39,850
on to basically scale up your bug bounty or your pentest game across multiple types of targets that

89
00:08:39,850 --> 00:08:40,490
you choose.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:03,680 --> 00:00:04,280
Yes.

2
00:00:04,560 --> 00:00:07,320
So now let us understand about the AI.

3
00:00:08,120 --> 00:00:12,760
So we have understood how we can leverage AI for automatic POC scripting and exploit template generation.

4
00:00:12,880 --> 00:00:14,960
I can also give a curl request.

5
00:00:15,280 --> 00:00:17,240
I can give a curl request and that can.

6
00:00:17,280 --> 00:00:20,080
The curl request can also be generated into a new template.

7
00:00:20,080 --> 00:00:27,960
For example, if I say https colon, slash slash example.com, and let's say my method is going to be

8
00:00:27,960 --> 00:00:29,160
a get request.

9
00:00:29,480 --> 00:00:32,640
And what do we do with this?

10
00:00:32,920 --> 00:00:36,560
Let's send a request to index dot p.

11
00:00:37,480 --> 00:00:41,440
And let's say id parameter is vulnerable to cross-site scripting.

12
00:00:41,560 --> 00:00:44,840
So let's say script alert one script tag close.

13
00:00:45,320 --> 00:00:50,000
So I'm going to send this request uh yeah.

14
00:00:50,040 --> 00:00:51,000
And hit enter.

15
00:00:51,040 --> 00:00:52,080
The request will be sent.

16
00:00:52,080 --> 00:00:54,240
And this is the output that we have received.

17
00:00:54,520 --> 00:01:02,040
Now let's say as of now this is a malformed request or this is not a valid request because example.com

18
00:01:02,080 --> 00:01:07,990
does not contains uh index dot php in this specific ID parameter, but this is just for your reference.

19
00:01:08,030 --> 00:01:08,470
Okay.

20
00:01:08,510 --> 00:01:24,190
So I'm going to copy this curl request and ask my AI bot hey generate nuclei compatible com Patible

21
00:01:25,150 --> 00:01:32,070
uh YAML template using this curl request.

22
00:01:32,110 --> 00:01:33,430
Let us see how does this behave.

23
00:01:33,470 --> 00:01:33,910
Okay.

24
00:01:55,150 --> 00:01:56,030
Excellent.

25
00:01:58,750 --> 00:01:59,630
Did you see that?

26
00:01:59,950 --> 00:02:05,230
So please note that nuclei is designed to mimic the request and detect potential vulnerabilities in

27
00:02:05,230 --> 00:02:07,910
similar manner as burp repeater or curl request.

28
00:02:07,950 --> 00:02:08,590
Very good.

29
00:02:08,750 --> 00:02:09,350
Did you see that?

30
00:02:09,350 --> 00:02:16,780
So we have generated a successful request the name type HTTP targets, whatever will be specified URI

31
00:02:16,980 --> 00:02:18,900
and the payload is also added over here.

32
00:02:18,900 --> 00:02:22,700
So it does pretty much the job that we want.

33
00:02:22,700 --> 00:02:27,340
You can enhance more maybe where you can say that right?

34
00:02:27,340 --> 00:02:35,180
The name of the author as your name in the template, as the author name was added in the template that

35
00:02:35,180 --> 00:02:36,740
I have submitted here.

36
00:02:38,380 --> 00:02:38,780
Yeah.

37
00:02:39,700 --> 00:02:43,340
And other such fields can definitely be added as well.

38
00:02:43,340 --> 00:02:45,620
So in the system prompt itself you can add that.

39
00:02:45,620 --> 00:02:51,540
And those modifications will happen automatically in the runtime for you, uh, so that you are able

40
00:02:51,540 --> 00:02:55,340
to generate a valid, uh, template of your choice.

41
00:02:55,340 --> 00:02:58,700
And not only that, you can also submit these templates to nuclei.

42
00:02:59,100 --> 00:03:05,460
So if you want to make community contribution nuclei templates are an excellent place where you can

43
00:03:05,460 --> 00:03:06,820
showcase your skill sets.

44
00:03:06,980 --> 00:03:12,780
And not only this, you can also add this to your CV or your resume as well that you have been an active

45
00:03:12,780 --> 00:03:17,730
contributor to the open source community, uh, through nuclear templates.

46
00:03:17,850 --> 00:03:19,210
So it's very simple.

47
00:03:19,210 --> 00:03:27,290
You go to uh issues and go a new issue and then do select template contribution.

48
00:03:27,410 --> 00:03:33,610
Once you select a template contribution template uh please submit your template.

49
00:03:34,010 --> 00:03:38,130
Choose I have already searched the existing templates and this template is new.

50
00:03:39,050 --> 00:03:43,650
And uh, if any response you want to add, you can add it over here.

51
00:03:43,650 --> 00:03:45,970
And if you want to write anything you can write it over here.

52
00:03:45,970 --> 00:03:52,970
So basically whatever templates have been generated from your local LLM bot, uh, you can submit it

53
00:03:53,250 --> 00:03:54,810
over here after testing it out.

54
00:03:54,810 --> 00:03:58,290
It is proper and working and you can simply create and click on create.

55
00:03:58,290 --> 00:04:01,090
If you want to add more reports you can click Create More.

56
00:04:01,850 --> 00:04:07,290
And once you submit, you will again see a prompt where you can submit more reports of your choice.

57
00:04:07,530 --> 00:04:07,970
Okay.

58
00:04:08,010 --> 00:04:11,090
So this way template contribution can be done over here.

59
00:04:11,090 --> 00:04:17,410
And once the report has been uh, successfully given, for example let us see this multiple template

60
00:04:17,410 --> 00:04:18,530
contributions over here.

61
00:04:18,530 --> 00:04:21,690
Let's take an example of this one.

62
00:04:22,320 --> 00:04:30,520
So someone has with this name has contributed this template which says FTP weak credential.

63
00:04:30,760 --> 00:04:40,000
So if an FTP service can have an easily guessed credentials like admin root as username and password

64
00:04:40,000 --> 00:04:43,120
as this, then it is considered to be vulnerable.

65
00:04:43,480 --> 00:04:47,160
Here we can see nuclear is running on this target.

66
00:04:47,280 --> 00:04:55,720
And this is the response where where where the username and password, if it has been submitted as correct

67
00:04:55,760 --> 00:04:57,640
would be shown over here automatically.

68
00:05:01,440 --> 00:05:01,720
Yeah.

69
00:05:01,720 --> 00:05:03,360
So this is how the output looks like.

70
00:05:05,360 --> 00:05:06,880
Uh yeah.

71
00:05:06,880 --> 00:05:12,680
So now this template was added GitHub actions assigned the template to automatically a user who is going

72
00:05:12,680 --> 00:05:14,680
to validate that template is correct.

73
00:05:14,840 --> 00:05:19,880
And once that template is correct then it will be automatically added.

74
00:05:20,000 --> 00:05:25,400
So once the template is added it would then be coming to the Nuclei templates official repository.

75
00:05:25,880 --> 00:05:29,950
Uh and it will be it will be used by other community members.

76
00:05:29,950 --> 00:05:33,350
So this is an excellent contribution that you can do.

77
00:05:33,510 --> 00:05:39,190
Not only that, uh, you can put this on your resume as well, that you have been an active contributor

78
00:05:39,230 --> 00:05:40,590
of two multiple templates.

79
00:05:40,790 --> 00:05:47,830
So I myself has contributed many, many templates over here, uh, in the past.

80
00:05:48,030 --> 00:05:54,190
And I have multiple more templates that I have created that I still use.

81
00:05:54,190 --> 00:06:00,550
So if you want to, if you want to look for my templates that I have contributed, you can search for

82
00:06:01,070 --> 00:06:01,430
them.

83
00:06:01,830 --> 00:06:09,350
And you can see, uh, those ten, ten templates that I have submitted over here in the past, uh,

84
00:06:09,350 --> 00:06:11,750
for most likely access.

85
00:06:11,790 --> 00:06:17,630
And here is a WAF bypass Wordfence WAF bypass XSS, uh, template that I have submitted.

86
00:06:17,630 --> 00:06:23,550
So WordPress Wordfence is a WAF, which is usually compatible with WordPress based websites.

87
00:06:23,550 --> 00:06:30,630
So you can use these, uh, of my old templates as well to run it across bug bounty programs or Pentest

88
00:06:30,630 --> 00:06:32,350
target, where it will be useful.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 18: Postman Usage

1
00:00:00,160 --> 00:00:04,480
Ceiling forward to learn about AI driven API fuzzing using postman.

2
00:00:05,720 --> 00:00:09,680
So first things first we need to download postman.

3
00:00:09,920 --> 00:00:11,160
So what is postman?

4
00:00:11,160 --> 00:00:14,280
So postman is a tool similar to Burpsuite.

5
00:00:14,480 --> 00:00:19,200
It is not a proxy tool or a vulnerability scanner.

6
00:00:19,440 --> 00:00:29,440
It is a tool that is used basically to, uh, help you test or audit API requests.

7
00:00:30,040 --> 00:00:36,000
Uh, it is a tool that is used by developers as well, because this gives them the entire coverage of

8
00:00:36,240 --> 00:00:41,040
integrations that they can make with their APIs, back end and front end.

9
00:00:41,520 --> 00:00:48,480
And they can basically utilize this for doing for doing a lot of alpha beta testing, passing it through,

10
00:00:49,080 --> 00:00:51,680
uh, dev and staging environments, etc..

11
00:00:52,320 --> 00:01:00,270
And uh, postman not only supports Rest based API, but it supports, It's, uh, GraphQL.

12
00:01:00,310 --> 00:01:04,550
It supports, uh, soap rest.

13
00:01:04,710 --> 00:01:08,230
It's supposed gRPC, WebSockets, Socket.io or it.

14
00:01:08,270 --> 00:01:12,830
And it also supports MQTT IoT protocol requests as well.

15
00:01:13,030 --> 00:01:21,590
So it's pretty much very, very, uh, dynamic in nature wherein it supports multiple types of API requests.

16
00:01:21,750 --> 00:01:23,910
Now let us see how we can use this.

17
00:01:24,230 --> 00:01:27,510
So what I'm going to do first is I'm going to download postman.

18
00:01:27,630 --> 00:01:36,230
So you you need to say postman download go to this link and pasting this link in the chat where you

19
00:01:36,230 --> 00:01:38,750
can download the compatible version for postman.

20
00:01:39,110 --> 00:01:40,190
Absolutely for free.

21
00:01:40,470 --> 00:01:45,350
So I'm currently using Mac, so I'm going to download the Mac Apple chip version.

22
00:01:45,710 --> 00:01:47,390
Uh you can download it for windows.

23
00:01:47,390 --> 00:01:53,070
So you can choose windows x64 from here and it will start downloading okay.

24
00:01:53,430 --> 00:01:56,190
Uh I'm using Mac, so I'll download the Mac version.

25
00:01:56,190 --> 00:02:00,900
I already have downloaded this, so let me start postman and show you how it looks.

26
00:02:03,260 --> 00:02:03,860
Awesome.

27
00:02:03,860 --> 00:02:05,540
So this is how postman looks.

28
00:02:05,540 --> 00:02:07,780
Basically, let me go to the home window.

29
00:02:07,780 --> 00:02:09,100
So this is how it looks.

30
00:02:09,460 --> 00:02:12,340
Uh, now it has first started.

31
00:02:12,740 --> 00:02:13,780
This is the home page.

32
00:02:14,020 --> 00:02:19,500
Uh, the first thing that I would recommend when you set up postman is create an account, create a

33
00:02:19,500 --> 00:02:20,220
free account.

34
00:02:20,620 --> 00:02:27,740
So to create a free account, simply click here on this dot and choose create a Free account.

35
00:02:27,900 --> 00:02:31,100
Uh I am I am currently logged in.

36
00:02:31,140 --> 00:02:33,340
Yeah I'm currently logged in.

37
00:02:34,300 --> 00:02:36,420
That is why you are able to see my account.

38
00:02:37,300 --> 00:02:38,700
Uh, yeah.

39
00:02:38,740 --> 00:02:40,660
I'm logged in with my account for you.

40
00:02:40,660 --> 00:02:41,740
You would not be logged in.

41
00:02:41,740 --> 00:02:44,220
So please create a free account and log in with your account.

42
00:02:44,220 --> 00:02:44,620
Why?

43
00:02:45,020 --> 00:02:45,260
Why?

44
00:02:45,260 --> 00:02:51,180
It is important to log in so that you are able to track your previous request or testing or data that

45
00:02:51,180 --> 00:02:56,810
you have done, uh, so that it is again saved with your account automatically and synced.

46
00:02:57,650 --> 00:03:01,450
Okay, so once you log in, what is the first thing that you need to do?

47
00:03:01,690 --> 00:03:04,730
You need to go to workspaces.

48
00:03:04,970 --> 00:03:05,210
Okay.

49
00:03:05,210 --> 00:03:07,130
So you need to you need to go to a workspace.

50
00:03:07,130 --> 00:03:08,730
You need to create a workspace.

51
00:03:08,730 --> 00:03:10,170
Click on create a workspace.

52
00:03:10,410 --> 00:03:14,250
You can choose any name of that workspace whatever you want.

53
00:03:14,370 --> 00:03:15,850
Or you can choose a blank workspace.

54
00:03:15,850 --> 00:03:17,370
I'm choosing a blank workspace.

55
00:03:17,370 --> 00:03:18,170
Click next.

56
00:03:18,370 --> 00:03:19,250
Give any name.

57
00:03:19,290 --> 00:03:20,410
So let's say API.

58
00:03:22,450 --> 00:03:23,290
Testing.

59
00:03:23,290 --> 00:03:26,210
With AI you can give any name.

60
00:03:26,890 --> 00:03:29,450
Uh, keep it internal so that it is private to you.

61
00:03:29,450 --> 00:03:36,290
If it make if you make it public, uh, then developers can also access or people can others can also

62
00:03:36,290 --> 00:03:39,090
access your API.

63
00:03:39,530 --> 00:03:41,810
So once you do that hit okay.

64
00:03:41,810 --> 00:03:45,930
And now you would be able to see this screen API testing with API.

65
00:03:45,970 --> 00:03:46,690
Very nice.

66
00:03:47,170 --> 00:03:52,130
Now first thing after you create a workspace is to create a collection.

67
00:03:52,330 --> 00:03:56,800
So you can click on create a Collection and start creating this collection.

68
00:03:56,840 --> 00:04:00,440
Now we are not an API developer, so we're not going to create a collection.

69
00:04:00,440 --> 00:04:02,880
Rather we are going to import a collection.

70
00:04:03,000 --> 00:04:07,440
So I'm going to delete this new collection and I'm going to choose this import option.

71
00:04:08,000 --> 00:04:10,880
Now it is asking us to import a collection.

72
00:04:10,880 --> 00:04:12,600
So you can give the URL.

73
00:04:12,720 --> 00:04:16,600
Or maybe download that collection manually and drag and drop it.

74
00:04:16,760 --> 00:04:27,160
So for testing purposes I'm going to use this project which is V API vulnerable API vulnerable adversarial

75
00:04:27,200 --> 00:04:36,480
Adversarially programmed API is an API project which mimics API top ten scenarios.

76
00:04:36,840 --> 00:04:40,080
Uh, that is basically vulnerable API test cases.

77
00:04:40,680 --> 00:04:44,800
Now, once you are at this project, let me also paste this link in the chat.

78
00:04:46,240 --> 00:04:48,280
You can go to postman.

79
00:04:50,080 --> 00:04:55,640
Please go to postman and then you can see we API postman collection dot JSON.

80
00:04:56,120 --> 00:04:59,600
So once you click on that you can copy this URL.

81
00:05:00,400 --> 00:05:00,840
Okay.

82
00:05:01,880 --> 00:05:08,400
Or rather copying that URL click on raw.

83
00:05:09,120 --> 00:05:18,040
So once you click on raw, copy the raw URL now and go to your postman.

84
00:05:18,880 --> 00:05:20,720
Paste the raw URL.

85
00:05:21,280 --> 00:05:30,080
So paste it there and congratulations V API is automatically set it up into your system.

86
00:05:30,160 --> 00:05:36,400
So not completely set it up with the back end, but at least the all the API requests are set up.

87
00:05:36,440 --> 00:05:40,200
You can see the complete documentation from here about what is API.

88
00:05:41,160 --> 00:05:42,440
All the API test cases.

89
00:05:42,440 --> 00:05:44,560
So there are in total ten test cases.

90
00:05:45,000 --> 00:05:49,880
First one is broken object level authorization and you can see read about it.

91
00:05:50,310 --> 00:05:55,630
So API one contains three request post request to create a user.

92
00:05:56,110 --> 00:05:59,870
Get request to get a user put request to update a user.

93
00:06:00,310 --> 00:06:01,750
Let's go to the first one.

94
00:06:02,150 --> 00:06:06,230
And then you can basically play with that API request before that.

95
00:06:06,230 --> 00:06:08,430
Currently we are seeing the documentation.

96
00:06:08,430 --> 00:06:11,830
So you can see API one contains Post request which looks like this.

97
00:06:12,310 --> 00:06:13,430
This is the body.

98
00:06:13,830 --> 00:06:17,790
This is the Get request where it is going to fetch the API id of the user.

99
00:06:18,510 --> 00:06:23,190
To fetch the user name, you can click on Open Request and directly reach there, or you can click on

100
00:06:23,190 --> 00:06:24,670
here as well to reach there.

101
00:06:25,550 --> 00:06:29,590
Then put request to update this information.

102
00:06:29,750 --> 00:06:34,830
Maybe a username, name or password of that given user with api id.

103
00:06:35,110 --> 00:06:38,030
So let's go ahead and do this.

104
00:06:38,310 --> 00:06:41,230
So to do this we are going to go and click on API.

105
00:06:45,510 --> 00:06:49,740
Uh please show again how you post pose the API link to the postman.

106
00:06:49,900 --> 00:06:50,660
Very simple.

107
00:06:51,220 --> 00:06:54,700
Once you create a workspace, this is my workspace.

108
00:06:55,140 --> 00:06:57,300
Please go to on your left hand side.

109
00:06:57,340 --> 00:06:58,460
Choose collections.

110
00:06:59,340 --> 00:07:04,740
Choose import and here you can paste the URL.

111
00:07:04,780 --> 00:07:05,980
How to paste the URL.

112
00:07:07,140 --> 00:07:11,540
Go to API sorry GitHub page.

113
00:07:12,140 --> 00:07:13,140
Go to postman.

114
00:07:13,900 --> 00:07:19,580
Go to collection dot JSON, then go to raw.

115
00:07:20,740 --> 00:07:24,940
Then you'll be able to see the raw contents of the API collection.

116
00:07:25,380 --> 00:07:34,940
Now simply copy the URL, go to your postman and paste it so it will say your collection is already

117
00:07:34,940 --> 00:07:35,340
there.

118
00:07:36,100 --> 00:07:37,620
Uh, do you want to import a copy?

119
00:07:37,620 --> 00:07:38,300
I'll say no.

120
00:07:38,300 --> 00:07:45,300
I'll just say replace the old and you can see the entire collection will come here and you can see this.

121
00:07:45,340 --> 00:07:47,100
I hope you are able to understand it.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1
00:00:00,040 --> 00:00:00,720
Very simple.

2
00:00:01,240 --> 00:00:04,720
Once you create a workspace, this is my workspace.

3
00:00:05,160 --> 00:00:06,160
Please go to.

4
00:00:06,320 --> 00:00:14,760
On your left hand side, choose collections, choose import and here you can paste the URL.

5
00:00:14,800 --> 00:00:16,000
How to paste the URL.

6
00:00:17,160 --> 00:00:21,600
Go to API sorry GitHub page.

7
00:00:22,120 --> 00:00:23,160
Go to postman.

8
00:00:23,960 --> 00:00:29,600
Go to collection dot JSON, then go to raw.

9
00:00:30,760 --> 00:00:34,960
Then you'll be able to see the raw contents of the API collection.

10
00:00:35,400 --> 00:00:44,960
Now simply copy the URL, go to your postman and paste it so it will say your collection is already

11
00:00:44,960 --> 00:00:45,360
there.

12
00:00:46,120 --> 00:00:47,640
Uh, do you want to import a copy?

13
00:00:47,640 --> 00:00:48,320
I'll say no.

14
00:00:48,320 --> 00:00:55,360
I'll just say replace the old and you can see the entire collection will come here and you can see this.

15
00:00:55,360 --> 00:00:57,080
I hope you're able to understand it.

16
00:00:59,680 --> 00:01:00,240
Very good.

17
00:01:02,080 --> 00:01:11,390
Now, participants, you can actually not send a request right now Because the API front end is loaded.

18
00:01:11,390 --> 00:01:12,390
But where's the backend?

19
00:01:12,430 --> 00:01:13,990
The backend is not still active.

20
00:01:14,310 --> 00:01:14,990
So you will see.

21
00:01:14,990 --> 00:01:19,790
When I send my first post request to create a user, you will see an error.

22
00:01:21,910 --> 00:01:24,670
Could not send a request because my backend is not ready.

23
00:01:25,110 --> 00:01:26,630
So let's set up the backend.

24
00:01:27,510 --> 00:01:32,150
So to set up the backend go to the API project.

25
00:01:33,310 --> 00:01:37,910
Scroll down, scroll down, scroll down, scroll down until you see.

26
00:01:40,190 --> 00:01:41,110
Installation.

27
00:01:41,830 --> 00:01:43,550
Let us see how to install this.

28
00:01:43,710 --> 00:01:44,710
So it's Docker.

29
00:01:44,710 --> 00:01:49,310
Installation is pretty straightforward and manual installation requires multiple steps.

30
00:01:49,590 --> 00:01:51,150
We'll follow Docker installation.

31
00:01:51,550 --> 00:01:57,710
So there's only one single command that you need to run docker compose up into detached mode.

32
00:01:58,070 --> 00:01:59,990
So let's download this project.

33
00:01:59,990 --> 00:02:03,670
And inside that project folder we'll run the docker compose command.

34
00:02:04,630 --> 00:02:07,470
So let me go to the AI folder first.

35
00:02:13,630 --> 00:02:17,890
Let's git clone, let's git clone vip.

36
00:02:18,250 --> 00:02:21,210
I already have done this, so it is saying it is already there.

37
00:02:21,450 --> 00:02:22,770
Let's go to the app folder.

38
00:02:24,370 --> 00:02:28,690
And these are all the files inside the folder that we just downloaded from GitHub.

39
00:02:29,370 --> 00:02:34,570
Now docker compose up in detached mode.

40
00:02:34,570 --> 00:02:38,090
Hit enter and you'll be able to see the container is started.

41
00:02:38,370 --> 00:02:39,090
Excellent.

42
00:02:39,530 --> 00:02:44,210
Let's see Docker running processes by running the docker PS command.

43
00:02:44,730 --> 00:02:49,010
And you can see six seconds ago VIP dub dub dub is started.

44
00:02:49,010 --> 00:02:58,010
First container six seconds ago docker PS phpmyadmin is started and six seconds ago the SQL service

45
00:02:58,010 --> 00:02:59,450
is also started for web.

46
00:02:59,490 --> 00:03:01,050
So this is the database for web.

47
00:03:01,050 --> 00:03:06,650
This is phpMyAdmin and this is the uh which is basically the main back end.

48
00:03:07,530 --> 00:03:11,450
Uh, it is exposed on port 8000.

49
00:03:11,690 --> 00:03:13,370
Let's go to 8000.

50
00:03:13,690 --> 00:03:14,850
And congratulations.

51
00:03:14,890 --> 00:03:15,970
Web is running here.

52
00:03:16,370 --> 00:03:18,130
Let's go to the API endpoint.

53
00:03:18,370 --> 00:03:21,810
And you can see the entire documentation available for here.

54
00:03:22,090 --> 00:03:22,370
So.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 19: API Vulnerability Testing

1
00:00:00,160 --> 00:00:03,840
You can simply put all of this documentation to Lama.

2
00:00:04,040 --> 00:00:11,240
And Lama can then give you what is the URL endpoints, sorry, API endpoints, what are the parameters

3
00:00:11,240 --> 00:00:15,400
body, etc. um, that you can use.

4
00:00:15,400 --> 00:00:21,480
So I'm going to give the entire folder to lama to understand it, to give us the API endpoints, parameters,

5
00:00:21,480 --> 00:00:24,240
body, etc. before doing doing that.

6
00:00:26,360 --> 00:00:26,640
Yeah.

7
00:00:26,680 --> 00:00:31,360
Before doing that we can see that my app is currently running on port 8000.

8
00:00:32,000 --> 00:00:34,240
So I'm going to go back to postman.

9
00:00:35,520 --> 00:00:43,280
And you can see in the collection the post request is going to a host variable.

10
00:00:43,440 --> 00:00:50,840
So we need to replace this host variable with the current app service which is running which is this.

11
00:00:51,280 --> 00:00:56,480
Hence you need to go to environments choose on new.

12
00:00:58,560 --> 00:00:58,960
Okay.

13
00:00:59,600 --> 00:01:01,760
Choose global environment.

14
00:01:01,760 --> 00:01:02,320
Global.

15
00:01:02,680 --> 00:01:04,320
Choose a variable name host.

16
00:01:04,440 --> 00:01:05,760
Why did we choose host?

17
00:01:05,760 --> 00:01:09,080
Because in the collection the variable is host.

18
00:01:09,520 --> 00:01:15,680
So go to environment global host type default initial value.

19
00:01:15,720 --> 00:01:17,520
Is this.

20
00:01:17,800 --> 00:01:20,960
So in the place of host we want to replace this.

21
00:01:21,840 --> 00:01:24,440
And in the current value also we want to replace this.

22
00:01:24,440 --> 00:01:25,440
Please click save.

23
00:01:26,800 --> 00:01:31,480
Once you click save you have a global variable for a workspace ready for you.

24
00:01:31,960 --> 00:01:32,560
Nice.

25
00:01:32,680 --> 00:01:33,920
Let's go to collections.

26
00:01:34,120 --> 00:01:35,440
Let's go to Create user.

27
00:01:35,920 --> 00:01:43,080
And the host variable is now taking a value from a global variable which is this.

28
00:01:43,080 --> 00:01:47,120
So basically you are now going to send a request to the endpoint which is this.

29
00:01:48,200 --> 00:01:50,200
And the host is running on here.

30
00:01:50,600 --> 00:01:52,440
So let's try to create a user.

31
00:01:52,440 --> 00:01:53,880
So let's fill.

32
00:01:54,080 --> 00:01:55,720
So this is the endpoint.

33
00:01:55,720 --> 00:01:56,720
This is the body.

34
00:01:56,920 --> 00:01:58,640
So let me fill some information here.

35
00:01:58,720 --> 00:02:01,600
So I'm going to say user name equals to.

36
00:02:05,520 --> 00:02:06,360
Going body.

37
00:02:06,520 --> 00:02:10,720
Username equals to Rohit name equals to Rohit ji.

38
00:02:11,200 --> 00:02:16,480
Course equals to API hacking and password equals to root.

39
00:02:16,800 --> 00:02:19,160
So I have added some contents in the body.

40
00:02:19,720 --> 00:02:21,080
Let's hit send.

41
00:02:21,920 --> 00:02:26,640
And it says duplicate entry for Rohit because that username is already used.

42
00:02:26,840 --> 00:02:30,440
So I'll say Rohit ji and name Rohit ji.

43
00:02:30,480 --> 00:02:33,960
Okay now let's send a request and congratulations.

44
00:02:34,280 --> 00:02:36,360
Did you see this 2001 created?

45
00:02:36,680 --> 00:02:41,640
That means that we have successfully created a user in the back end.

46
00:02:42,720 --> 00:02:46,480
And the ID of this current user is seven.

47
00:02:46,840 --> 00:02:56,080
Now let's go click and on get user, which is now going to fetch a user from the same API endpoint and

48
00:02:56,120 --> 00:02:58,480
it is requesting an API id.

49
00:02:58,760 --> 00:03:00,920
So let's put an API id.

50
00:03:00,920 --> 00:03:02,520
So let's put a value one.

51
00:03:03,480 --> 00:03:04,000
Uh sorry.

52
00:03:04,000 --> 00:03:05,480
Let's put a value seven.

53
00:03:05,840 --> 00:03:07,320
Or you can put it here as well.

54
00:03:07,680 --> 00:03:11,280
So what is the seven api id user Rohit ji.

55
00:03:11,480 --> 00:03:12,440
Let's hit send.

56
00:03:15,240 --> 00:03:18,640
Uh internal server error okay.

57
00:03:18,880 --> 00:03:19,800
Let's hit send.

58
00:03:36,600 --> 00:03:36,960
Okay.

59
00:03:36,960 --> 00:03:47,760
Let me just generate a new user once again let's say Shiva Shiva ji and send.

60
00:03:48,320 --> 00:03:49,760
So a new user is added.

61
00:03:54,320 --> 00:03:55,200
Get user.

62
00:03:55,440 --> 00:03:56,160
Fetch it.

63
00:04:03,080 --> 00:04:07,040
There is some thing wrong.

64
00:04:07,680 --> 00:04:10,560
It is not able to fetch the API authentication.

65
00:04:10,560 --> 00:04:12,120
Okay, so let's do one thing.

66
00:04:13,640 --> 00:04:18,560
Uh, go to environment, go to import and let's import the environment as well.

67
00:04:18,880 --> 00:04:19,920
Available here.

68
00:04:20,520 --> 00:04:23,960
Postman environment.

69
00:04:26,200 --> 00:04:32,000
Your raw copy paste it.

70
00:04:33,400 --> 00:04:39,920
Now we have the environment import successful which you can see.

71
00:04:40,480 --> 00:04:41,160
Looks good.

72
00:04:41,680 --> 00:04:42,920
Let's go to collections.

73
00:04:43,240 --> 00:04:47,680
Create a user for g g g g.

74
00:04:48,680 --> 00:04:51,280
Send a new user has been created.

75
00:04:51,480 --> 00:04:52,400
Get user.

76
00:05:03,400 --> 00:05:03,720
Mm.

77
00:05:15,480 --> 00:05:17,040
There is something wrong.

78
00:05:17,080 --> 00:05:22,080
Let me just figure out why it is not taking the previous.

79
00:05:24,280 --> 00:05:26,960
Cookie from the header.

80
00:05:29,400 --> 00:05:29,720
Oh.

81
00:05:30,400 --> 00:05:32,480
Inherit from parent.

82
00:05:33,000 --> 00:05:33,400
Okay.

83
00:05:33,680 --> 00:05:41,080
Uh, body g g g g g g g x n.

84
00:05:42,400 --> 00:05:42,720
Okay.

85
00:05:42,760 --> 00:05:44,160
A new user is created.

86
00:05:44,320 --> 00:05:45,800
Let's try to get that user.

87
00:05:54,520 --> 00:05:58,880
So there is something wrong with the authorization.

88
00:05:59,360 --> 00:06:06,400
So what should ideally happen is it should automatically take the authentication token from the previous

89
00:06:06,400 --> 00:06:09,680
request and work appropriately.

90
00:06:11,640 --> 00:06:13,400
I'm not sure why that did.

91
00:06:14,240 --> 00:06:18,240
That did not happen correctly, because of which we are not able to send the second request.

92
00:06:18,800 --> 00:06:23,200
And this request will also fail because we are not able to add the authorization part.

93
00:06:23,520 --> 00:06:29,840
So I'll delete this, and I'll restore this same collection to see what is the exact same problem.

94
00:06:30,200 --> 00:06:37,440
Uh, but yes, our objective is, uh, whenever you load a API collection and you want to test it with

95
00:06:37,440 --> 00:06:39,440
I, this is how you do it, okay.

96
00:06:40,200 --> 00:06:42,880
Participants, please have a look at Post Bot.

97
00:06:43,240 --> 00:06:54,520
Post bot is an AI based tool that is integrated with postman that can actually help you write test cases.

98
00:06:54,800 --> 00:06:55,280
Okay.

99
00:06:55,280 --> 00:07:02,960
So I'm going to say hi, test the current uh.

100
00:07:05,440 --> 00:07:08,640
Request for XSS.

101
00:07:09,280 --> 00:07:09,880
That's it.

102
00:07:09,920 --> 00:07:10,600
Hit send.

103
00:07:14,000 --> 00:07:15,080
Did you see that?

104
00:07:16,080 --> 00:07:18,440
The script is ready for us.

105
00:07:18,920 --> 00:07:26,200
And it is going to basically send a script tag, and it is going to test that out for us if it is vulnerable

106
00:07:26,240 --> 00:07:26,720
or not.

107
00:07:26,920 --> 00:07:29,320
So I've added a test to check for XSS vulnerability.

108
00:07:29,320 --> 00:07:32,080
Let me know if this looks good or if you want anything else.

109
00:07:32,080 --> 00:07:37,040
So I'm going to say okay, that looks good and I'm going to say test for response.

110
00:07:42,440 --> 00:07:42,920
Okay.

111
00:07:42,960 --> 00:07:48,120
So now it is going to send a request and it is going to check our response for a specific criteria that

112
00:07:48,120 --> 00:07:48,760
we want.

113
00:07:49,000 --> 00:07:50,160
Everything looks good.

114
00:07:50,400 --> 00:07:54,950
Now we can simply send this request that we want.

115
00:07:58,270 --> 00:07:59,390
Let me change the body.

116
00:08:07,710 --> 00:08:08,190
Yeah.

117
00:08:17,790 --> 00:08:18,310
Right.

118
00:08:19,550 --> 00:08:26,070
So we can send this request, we can test out if the given request is vulnerable to XSS or no.

119
00:08:26,070 --> 00:08:37,750
Or I can just go here and say test all OWASp top ten issues for the current request.

120
00:08:39,910 --> 00:08:42,230
So it is going to test XSS.

121
00:08:42,270 --> 00:08:43,470
It is going to test.

122
00:08:43,750 --> 00:08:46,070
Uh, yeah.

123
00:08:46,070 --> 00:08:47,910
It is said that I have added all test cases.

124
00:08:47,910 --> 00:08:52,270
So let's say uh, first is Stress, uh, excess.

125
00:08:52,270 --> 00:08:58,950
So it is checking if user name contains XSS name contains XSS course should not contain XSS.

126
00:08:58,990 --> 00:09:00,270
It is going to test that.

127
00:09:00,270 --> 00:09:04,390
Then it is going to test broken authentication and session management.

128
00:09:04,390 --> 00:09:10,350
Then it is going to test it automatically in the ID, password and admin field.

129
00:09:10,350 --> 00:09:15,230
Then it is going to test for security misconfiguration in uh the other request.

130
00:09:15,230 --> 00:09:20,310
So this way we are basically making multiple scripts over here.

131
00:09:20,670 --> 00:09:26,670
And with the help of these scripts that you are creating participants, you can actually send requests.

132
00:09:26,670 --> 00:09:28,150
So this is the code snippet.

133
00:09:28,470 --> 00:09:33,870
You can actually send all of those requests that you that you want from here.

134
00:09:34,110 --> 00:09:41,470
And you can test out a given request against a vulnerability of your choice automatically from here.

135
00:09:41,750 --> 00:09:44,110
So it would basically in the runtime.

136
00:09:46,590 --> 00:09:46,990
Okay.

137
00:09:47,030 --> 00:09:50,270
In runtime test that out and give you the output.

138
00:09:50,270 --> 00:09:55,830
So, uh, request data stored does not contain XSS vulnerability.

139
00:09:56,510 --> 00:09:58,150
Let me run this once more.

140
00:10:12,430 --> 00:10:17,110
I guess something just went wrong because of the collection.

141
00:10:17,110 --> 00:10:19,110
Did not import it appropriately.

142
00:10:20,190 --> 00:10:21,510
Uh, so we can do that once again.

143
00:10:21,510 --> 00:10:22,990
So we have our script ready.

144
00:10:22,990 --> 00:10:23,990
We can send it.

145
00:10:29,310 --> 00:10:32,030
Uh, we can send it, and then we can check what is happening wrong.

146
00:10:32,030 --> 00:10:37,590
And I hope you saw the test results over here, where we saw that the target is not vulnerable with

147
00:10:37,590 --> 00:10:39,590
XSS, etc., etc..

148
00:10:43,990 --> 00:10:47,710
Yes, we have got some errors here, so I'll just replace I'll remove that.

149
00:10:47,750 --> 00:10:50,390
I'll actually remove the entire script as well.

150
00:10:51,750 --> 00:11:00,790
And I'm going to say, hey, post bot check for XSS in the current request.

151
00:11:09,630 --> 00:11:14,990
Then okay, so you can see it also gave us the test result passed.

152
00:11:15,390 --> 00:11:22,990
Uh, that means the target is currently not vulnerable because, uh, it has passed this result successfully

153
00:11:22,990 --> 00:11:24,190
and it did not.

154
00:11:24,350 --> 00:11:28,790
Uh, so basically it is not allowing script tag in any of the fields.

155
00:11:29,670 --> 00:11:31,830
Participants, I hope you are able to understand this.

156
00:11:31,830 --> 00:11:33,030
Please give me a heads up.

157
00:11:43,710 --> 00:11:44,390
Nice.

158
00:11:44,390 --> 00:11:50,390
So what you can do is now, whenever you you're having multiple test cases like this, let's say user

159
00:11:50,390 --> 00:11:57,430
login test case, here you can specify an email ID and password and then simply go to Post Bot and ask

160
00:11:57,430 --> 00:12:00,270
Post Bot to basically test for a response.

161
00:12:00,310 --> 00:12:06,870
So let's say uh, check for excesses in this request.

162
00:12:07,150 --> 00:12:07,750
That's it.

163
00:12:08,110 --> 00:12:08,750
It's in.

164
00:12:23,510 --> 00:12:24,790
Uh, yeah.

165
00:12:25,910 --> 00:12:28,670
Send generate test.

166
00:12:33,430 --> 00:12:34,910
Okay, so we got an error.

167
00:12:34,910 --> 00:12:35,550
Here it is.

168
00:12:35,550 --> 00:12:42,710
Because the current request requires a email and password and something is not right in our environment.

169
00:12:44,270 --> 00:12:48,750
So that is why we have got getting a 401 unauthorized test output.

170
00:12:48,750 --> 00:12:49,670
But that's okay.

171
00:12:50,110 --> 00:12:55,390
But I hope you have got the crux when you are testing multiple type of requests.

172
00:12:55,870 --> 00:13:00,910
Uh, let's say you're testing a form, uh, user profile, profile form.

173
00:13:00,910 --> 00:13:05,790
You can test that against XSS quickly or SQL injection or any other different types of vulnerability

174
00:13:05,790 --> 00:13:07,430
by simply giving prompts over here.

175
00:13:07,590 --> 00:13:10,110
And there are unlimited prompts that you can make.

176
00:13:10,110 --> 00:13:14,630
This is absolutely free, okay, that you can do over here.

177
00:13:14,790 --> 00:13:19,310
You can also send these requests to Burp Suite as well by starting a proxy.

178
00:13:19,310 --> 00:13:23,710
And from there also you can examine the requests that you want to do in runtime.

179
00:13:25,470 --> 00:13:29,430
So this makes your API testing very, very simple and easy.

180
00:13:29,430 --> 00:13:34,230
By just simply typing the test cases, it is going to generate them for you, and then it is going to

181
00:13:34,390 --> 00:13:36,430
test it out and run it as well.

182
00:13:36,430 --> 00:13:40,910
And it is going to say pass or failed from where you can evaluate the responses.

183
00:13:40,910 --> 00:13:45,270
And this can help you identify quick vulnerabilities and bugs as well.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================
