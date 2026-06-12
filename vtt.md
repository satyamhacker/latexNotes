# Section 1: Authentication Bypass

0
1
00:00:00,930 --> 00:00:01,230
Yes.
1

2
00:00:01,250 --> 00:00:03,240
So welcome guys.
2

3
00:00:03,240 --> 00:00:09,000
Today we're going to see authentication bypass vulnerability
3

4
00:00:09,240 --> 00:00:12,190
So what is the authentication bypass.
4

5
00:00:12,330 --> 00:00:16,140
Why are we going to do authentication bypass.
5

6
00:00:16,350 --> 00:00:23,680
What is the severity of this attack and what are the different ways to do account takeovers.
6

7
00:00:23,820 --> 00:00:29,760
Basically all this will be achieved in further slides
7

8
00:00:32,410 --> 00:00:36,360
so let's see how Auth bypass works.
8

9
00:00:36,880 --> 00:00:45,430
As we can see on the client end at the left site and at the right side of the server end when the client
9

10
00:00:45,670 --> 00:00:53,800
is communicating with the server and sending one request to the server the server will respond to the
10

11
00:00:53,800 --> 00:01:05,680
request by sending a response and when the client is able to modify the response let's say instead
11

12
00:01:05,680 --> 00:01:15,310
of client attacker is able to modify the response then there becomes authentication bypass if the
12

13
00:01:15,610 --> 00:01:22,540
application is just checking the client side code instead of checking the server side code
13

14
00:01:26,320 --> 00:01:35,170
so we're going to see authentication bypass in which we will see OTP bypass one time passwords bypass
14

15
00:01:36,370 --> 00:01:45,100
so basically checking whether the OTP's are right or wrong improperly leads to this type of bypass
15

16
00:01:46,780 --> 00:01:56,190
verifying and the client side only and taking decisions is very dangerous only allowing logging in to
16

17
00:01:56,820 --> 00:02:04,620
the application based on true or false conditions are also very dangerous.
17

18
00:02:04,620 --> 00:02:12,700
So it's practical time and let's see one of the OTP bypass vulnerability under authentication bypass
18

19
00:02:12,720 --> 00:02:21,700
attack as you can see there is an application called as healthie.in on which I am just making an
19

20
00:02:21,750 --> 00:02:28,770
account I am signing up using my details in which I have entered my name, my email address, my mobile
20

21
00:02:28,770 --> 00:02:30,120
number and a password
21

22
00:02:36,400 --> 00:02:45,280
and now I'm going to hit sign up after clicking and sign up as you can see the application has sent
22

23
00:02:45,310 --> 00:02:57,930
an OTP to my numbered so let me just enter the OTP as 0000 any random four digits and
23

24
00:02:57,930 --> 00:03:02,250
the application application will tell me it is an incorrect OTP.
24

25
00:03:02,310 --> 00:03:07,430
Obviously guys because this is a wrong to that I have entered into the application
25

26
00:03:11,920 --> 00:03:20,230
now what I will do I will go in my burpsuite and I will again enter the wrong OTP
26

27
00:03:23,610 --> 00:03:30,720
as you can see guys this is the request which is going to the API of healthie.in and this is an
27

28
00:03:30,810 --> 00:03:38,610
API call request which is going to the web server and in the API request you can see this is a post
28

29
00:03:38,610 --> 00:03:43,700
type of request and the body contains the mobile number.
29

30
00:03:43,920 --> 00:03:44,730
The OTP
30

31
00:03:49,860 --> 00:03:53,170
so I will forward this request now.
31

32
00:03:54,960 --> 00:03:58,810
And before forwarding I did a response.
32

33
00:03:59,190 --> 00:04:01,620
I want to see the response of this request.
33

34
00:04:01,620 --> 00:04:04,950
So I did intercept that response.
34

35
00:04:04,960 --> 00:04:12,510
Now I will forward this request and as I did intercept response to this request option I am able to
35

36
00:04:12,510 --> 00:04:22,020
see the response of this API request that was sent and in the response guys you can see in the body
36

37
00:04:22,140 --> 00:04:31,090
it is saying status : 0 message : incorrect OTP please try again as we already saw on that website that says
37

38
00:04:31,120 --> 00:04:34,470
OTP is wrong and there comes a error message.
38

39
00:04:34,470 --> 00:04:36,630
This is incorrect OTP.
39

40
00:04:36,660 --> 00:04:39,920
Please try again.
40

41
00:04:39,960 --> 00:04:45,570
So now what we are going to do is we are going to modify the status as 1 and we are going to write
41

42
00:04:45,570 --> 00:04:54,480
in the message correct OTP and forward this response to our browser and let's wait for the browser
42

43
00:04:57,450 --> 00:05:00,630
and the browser will get automatically refreshed.
43

44
00:05:00,630 --> 00:05:10,140
The application has now logged me in to my healthie account as you can see I cannot change the number.
44

45
00:05:10,230 --> 00:05:13,600
The e-mail and I'm inside the application.
45

46
00:05:14,190 --> 00:05:20,700
So through this way I was able to perform a valid authentication bypass.
46

47
00:05:21,090 --> 00:05:30,000
So basically a OTP bypass into into a healthie.in application wherein I achieved this attack by doing
47

48
00:05:30,000 --> 00:05:38,190
the response manipulation as the application was vulnerable as the application was only checking at the
48

49
00:05:38,190 --> 00:05:41,500
client site called Thank You.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,260 --> 00:00:03,290
Hello everyone.
1

2
00:00:03,600 --> 00:00:10,260
As this is the second video proof of concept for authentication bypass attack.
2

3
00:00:11,040 --> 00:00:19,830
So in this video we're going to see a vulnerability onto a very famous brand that is BMW.
3

4
00:00:19,830 --> 00:00:24,320
So I'm going to show you authentication bypass attack on BMW.
4

5
00:00:24,370 --> 00:00:24,930
Website
5

6
00:00:28,090 --> 00:00:35,060
so I will just search for BMW India and I will go to its Web site
6

7
00:00:43,070 --> 00:00:50,040
so let me just go to BMW India co.in Web site
7

8
00:00:53,170 --> 00:00:54,650
for requesting a test drive.
8

9
00:00:55,660 --> 00:00:56,200
Yes.
9

10
00:00:56,410 --> 00:01:05,260
So this is the website on which I have to take a test drive and forward making the request for a test
10

11
00:01:05,260 --> 00:01:06,150
drive.
11

12
00:01:06,220 --> 00:01:13,810
I have to submit my details so a mobile verification is there into the place.
12

13
00:01:13,830 --> 00:01:21,040
So I have to first verify my mobile number by giving the right mobile number and the OTP.
13

14
00:01:21,240 --> 00:01:31,140
So I'm going to enter my mobile number into the mobile number field and I'm going to hit send.
14

15
00:01:31,140 --> 00:01:35,190
Now I will get a OTP right now onto my phone
15

16
00:01:52,210 --> 00:01:54,880
so I'm not still yet received the OTP.
16

17
00:01:54,970 --> 00:01:56,490
Yes.
17

18
00:01:56,740 --> 00:02:01,710
So I have received a OTP but I'm to type it wrong OTP here.
18

19
00:02:02,710 --> 00:02:08,470
So let's say for instance we take a OTP that is 00000.
19

20
00:02:10,000 --> 00:02:10,280
Yeah.
20

21
00:02:10,660 --> 00:02:15,070
So we are basically going to take a wrong with OTP and I'm going to submit this.
21

22
00:02:15,370 --> 00:02:22,540
Obviously the application will not be able to verify this wrong  OTP as this is a wrong 
22

23
00:02:22,540 --> 00:02:22,780
OTP
23

24
00:02:23,080 --> 00:02:23,470
Yes
24

25
00:02:33,130 --> 00:02:35,940
the application is still loading the wrong OTP.
25

26
00:02:36,230 --> 00:02:38,700
But it did not but it is not taking me further.
26

27
00:02:39,530 --> 00:02:45,050
Basically it is not verifying the wrong OTP and taking me to the next step.
27

28
00:02:47,030 --> 00:02:49,130
So what I'm going to do right now is
28

29
00:02:53,620 --> 00:02:55,720
I'm going to take up my burpsuite
29

30
00:02:59,380 --> 00:03:04,460
and I will again hit enter to verify this wrong OTP.
30

31
00:03:04,630 --> 00:03:10,780
So as you can see this is the request that is going which contains the OTP I'm going to do. do
31

32
00:03:10,780 --> 00:03:19,120
intercept response to this request and you can see here the response body contains something that was
32

33
00:03:19,240 --> 00:03:26,950
error I just forwarded that response onto my application on the browser and you can see nothing happened
33

34
00:03:27,520 --> 00:03:35,500
because the OTP is wrong, one more time I'm repeating the steps and this time I'm going to make
34

35
00:03:37,970 --> 00:03:44,690
the error message to success as you can see I made it to success and to intercept off go to the web
35

36
00:03:44,690 --> 00:03:47,510
application and check what happened on the browser.
36

37
00:03:47,750 --> 00:03:48,840
Yes.
37

38
00:03:49,010 --> 00:03:57,950
So can you see I have bypassed the verification mobile verification process and now I am able to book
38

39
00:03:58,040 --> 00:04:06,890
a test drive of BMW on behalf of me so I can do this on behalf of anyone basically.
39

40
00:04:06,890 --> 00:04:13,910
So I'm just submitting this request and I will get a call from a BMW executive regarding a test drive
40

41
00:04:13,910 --> 00:04:17,150
for BMW 3 series.
41

42
00:04:17,150 --> 00:04:19,730
I hope you guys understood.
42

43
00:04:19,760 --> 00:04:20,890
Thank you.
43

44
00:04:20,900 --> 00:04:21,740
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,650 --> 00:00:03,070
Hello everyone.
1

2
00:00:03,120 --> 00:00:09,700
So we are going to see one more POC for authentication bypass.
2

3
00:00:09,700 --> 00:00:11,530
That is OTP bypass
3

4
00:00:14,700 --> 00:00:21,600
so here is the application of 99 acres and I'm going to sign up onto the application using my details
4

5
00:00:22,320 --> 00:00:28,290
as you can see I have given my phone number, name,email i'd and the application is creating my account
5

6
00:00:29,580 --> 00:00:33,030
now for the verification purposes.
6

7
00:00:33,030 --> 00:00:40,950
The application is going to ask me a OTP as you can see on the screen it is asking me to enter a code.
7

8
00:00:40,950 --> 00:00:48,010
So this time I'm goingto enter again a wrong code that is 0 0 0 0 and I'm going to hit on verify.
8

9
00:00:48,720 --> 00:00:52,800
And as you can see the application give a error that is invalid
9

10
00:01:01,250 --> 00:01:03,780
let me just configure the proxy again.
10

11
00:01:03,950 --> 00:01:04,430
Yeah.
11

12
00:01:04,520 --> 00:01:11,810
So again I'm going to hit the wrong code and this time in burp I'm going to do intercept on and one
12

13
00:01:11,810 --> 00:01:18,800
more time I'm going to hit the wrong code and you can see the request came into my Burpsuite for mobile
13

14
00:01:18,800 --> 00:01:19,890
verification.
14

15
00:01:19,970 --> 00:01:26,410
I will do,do intercept response to this request and I will see this is the response of this request.
15

16
00:01:26,840 --> 00:01:35,270
As you can see in the request the verification status is false which means that OTP that I supplied
16

17
00:01:35,420 --> 00:01:40,200
is wrong as we already saw on the screen that the OTP was wrong.
17

18
00:01:40,340 --> 00:01:40,950
Okay.
18

19
00:01:41,090 --> 00:01:48,460
So I will just modify this verification status failed or false to verification status True.
19

20
00:01:49,610 --> 00:01:52,270
And let's see what happens.
20

21
00:01:52,280 --> 00:01:58,020
So I just manipulated the response of the wrong OTP to the right one.
21

22
00:01:58,280 --> 00:02:03,050
And I'm going to forward this response to my browser.
22

23
00:02:03,050 --> 00:02:07,960
As you can see I'm logged into the application right now.
23

24
00:02:08,120 --> 00:02:12,520
I will just go into my profile my account to show you guys.
24

25
00:02:12,560 --> 00:02:15,080
So as soon as I click on modify profile
25

26
00:02:22,070 --> 00:02:25,920
I will be able to see my profile.
26

27
00:02:26,190 --> 00:02:27,330
Let me click again.
27

28
00:02:27,390 --> 00:02:31,660
And now you can see my profile.
28

29
00:02:32,110 --> 00:02:32,720
OK.
29

30
00:02:32,850 --> 00:02:36,480
Wherein my e-mail my phone number everything is there.
30

31
00:02:36,480 --> 00:02:38,330
Onto the website.
31

32
00:02:38,400 --> 00:02:38,670
OK.
32

33
00:02:38,670 --> 00:02:39,360
Thank you.
33

34
00:02:39,360 --> 00:02:42,180
Your profile has been updated successfully.
34

35
00:02:42,600 --> 00:02:47,870
So this way we can do our account takeover of anyone.
35

36
00:02:47,940 --> 00:02:48,450
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,160 --> 00:00:03,520
Hello everyone.
1

2
00:00:03,690 --> 00:00:12,120
So yea I I'm going to share a very interesting one regulating that I found out on a website of 
2

3
00:00:12,120 --> 00:00:13,450
starquik.com.
3

4
00:00:13,470 --> 00:00:17,560
This is a product of Tata enterprise.
4

5
00:00:17,580 --> 00:00:23,710
This is basically used for online shopping and groceries ordering and other stuff.
5

6
00:00:23,790 --> 00:00:29,820
I was able to identify a very very interesting vulnerability under this application.
6

7
00:00:29,820 --> 00:00:34,750
So there was a logic flaw in the application verification process.
7

8
00:00:34,950 --> 00:00:41,340
So I'm just going to demonstrate that for that I'm going to sign up is you using a new user as you
8

9
00:00:41,340 --> 00:00:49,250
can see I have given the name as Rahul my email address, phone number and password that application said
9

10
00:00:49,260 --> 00:00:55,050
user already registered because my this email id is register so I will use my new Mail id to sign up
10

11
00:00:56,730 --> 00:00:59,930
and I will hit create an account.
11

12
00:00:59,940 --> 00:01:08,490
Now this application is asking me to enter the OTP and I'm going to hit the OTP that is 0 0 0 0 and
12

13
00:01:08,490 --> 00:01:13,520
I will click on verify as you guys can notice here.
13

14
00:01:13,560 --> 00:01:17,630
This is obviously the wrong OTP that I have given to the application.
14

15
00:01:17,670 --> 00:01:20,600
It is not the correct OTP that I have received on my phone.
15

16
00:01:21,340 --> 00:01:29,910
And I will click on verify once I clicked on verify the application is verifying that OTP and you can
16

17
00:01:29,910 --> 00:01:34,840
see I was successfully logged in into the application.
17

18
00:01:35,040 --> 00:01:43,260
You must have noticed I have not touched the burpsuit till now neither I have DID ANY RESPONSE manipulation
18

19
00:01:43,470 --> 00:01:45,740
for this website.
19

20
00:01:45,810 --> 00:01:53,550
So I finally want to conclude that I was able to find out a logic flaw into the application where the
20

21
00:01:53,550 --> 00:02:01,820
developer made a very big mistake in developing the verification flow or to process becausewhen i tried
21

22
00:02:01,920 --> 00:02:08,190
with another OTP's  for example 1234 or 6789 the application gave
22

23
00:02:08,430 --> 00:02:16,690
always one error and did not allow me to bypass the verification flaw but whenever I use OTP
23

24
00:02:16,710 --> 00:02:24,420
0 0 0 it always allowed me to log in with anyone's phone number so I could have taken over anyone's
24

25
00:02:24,420 --> 00:02:35,040
phone number so you can think like the developer kept a master OTP that is 0 0 0 for anyone's verification
25

26
00:02:35,130 --> 00:02:39,170
which could allow anyone's verification into the application.
26

27
00:02:39,810 --> 00:02:50,520
And I was able to successfully log in and take anyone's phone number and successfully to account takeovers.
27

28
00:02:51,010 --> 00:02:52,600
Let's continue.
28

29
00:02:52,600 --> 00:02:57,550
When I successfully made account under the application I will just go into my profile.
29

30
00:02:58,260 --> 00:03:03,900
And as you guys can see it there is also option of wallet balance.
30

31
00:03:03,960 --> 00:03:10,920
This makes this attack more dangerous because you are able to take up anyone's phone number.
31

32
00:03:10,920 --> 00:03:13,100
I just showed how to do sign up.
32

33
00:03:13,170 --> 00:03:21,720
You can also bypass this verification flaw on login and you can log in into anyone's account who have
33

34
00:03:21,930 --> 00:03:27,330
wallet balance into their account which can be further misused by any attacker.
34

35
00:03:28,920 --> 00:03:37,220
So this basically increases the severity because this deals with payment and money.
35

36
00:03:37,260 --> 00:03:38,530
I hope you cleared.
36

37
00:03:38,730 --> 00:03:39,210
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,770 --> 00:00:03,210
Hello everyone.
1

2
00:00:03,210 --> 00:00:11,880
So in this video we are going to learn authentication bypass and I'm going to show you authentication
2

3
00:00:11,880 --> 00:00:17,670
by bus onto a very famous website that is stylecracker.com.
3

4
00:00:17,670 --> 00:00:24,250
Basically this Web site is being funded by an Indian Bollywood actress named Alia.
4

5
00:00:24,270 --> 00:00:24,720
Bhatt.
5

6
00:00:25,320 --> 00:00:32,620
And this Web site runs a clothing brand wherein they sell stylish clothes.
6

7
00:00:32,690 --> 00:00:39,870
So I was able to find out I vulnerability onto this website that I'm going to teach you guys into this
7

8
00:00:39,870 --> 00:00:41,280
video.
8

9
00:00:41,700 --> 00:00:47,080
So what I'm going to do is I'm just going to make an account onto the website first.
9

10
00:00:47,310 --> 00:00:52,590
So I will just go onto the sign up page and enter my details.
10

11
00:00:52,590 --> 00:00:54,790
So I'm entering my details.
11

12
00:00:55,080 --> 00:00:57,410
I've chosen the name as RAHUL MISHRA.
12

13
00:00:57,660 --> 00:01:07,080
I'm entering the date of birth and the phone number and I'm going to take a phone number in the email
13

14
00:01:07,080 --> 00:01:14,700
field I'm going to take my email address and then the password field I'm going to choose a password
14

15
00:01:16,360 --> 00:01:17,160
profession.
15

16
00:01:17,160 --> 00:01:24,630
Let's say corporate and I'm going to hit on sign up as you can see when I hit the sign that I'm able to
16

17
00:01:24,630 --> 00:01:29,650
see the request into my burpsuite.
17

18
00:01:30,030 --> 00:01:38,000
I will just do intercept response to this request and I will forward this request.
18

19
00:01:40,730 --> 00:01:43,860
OK so when I forwarded this request.
19

20
00:01:43,860 --> 00:01:50,920
Now as you can see on the screen it is saying our verification code has been sent to my phone number.
20

21
00:01:51,000 --> 00:01:55,840
Kindly enter the verification code that I have received onto my mobile phone.
21

22
00:01:56,460 --> 00:02:02,760
But instead of giving the right verification code I am going to give a wrong code.
22

23
00:02:03,000 --> 00:02:10,050
In this scenario I'm not even giving a phone number and giving alphabet.
23

24
00:02:10,050 --> 00:02:20,090
That is X X X X and I'm going to hit on verify as I can see it give an error that is invalid OTP.
24

25
00:02:20,190 --> 00:02:27,540
Again I'm going to give X Y Z X and I'm going to click on verify.
25

26
00:02:28,340 --> 00:02:36,550
Let me again give 0000 click on verify and intercept the request in burpsuite.
26

27
00:02:36,890 --> 00:02:42,670
As you can see the request POST request has been intercepted in Burpsuite.
27

28
00:02:42,800 --> 00:02:45,800
Now I want to see the response of this request
28

29
00:02:49,260 --> 00:02:50,130
also.
29

30
00:02:50,250 --> 00:03:03,810
Instead of putting the number digit into the OTP I am writing character strings into the OTP field.
30

31
00:03:04,110 --> 00:03:11,720
Now I'm going to do a, do intercept response to this request and see the response of this request.
31

32
00:03:12,270 --> 00:03:17,430
As you can see I'm not getting anything into the response right now.
32

33
00:03:17,430 --> 00:03:25,920
This looks interesting because when there is a wrong verification code entered the application does
33

34
00:03:25,920 --> 00:03:37,730
not passes anything into the body but I know the application when validate the right OTP give something
34

35
00:03:37,730 --> 00:03:38,670
into the body.
35

36
00:03:38,780 --> 00:03:47,900
So I'm going to try my giving something into the body that is 1 and forward and do intercept off and
36

37
00:03:47,900 --> 00:03:51,460
you can see I have logged in into the account.
37

38
00:03:51,680 --> 00:03:58,780
I'm going to skip everything and I'm going to try to go to my profile settings and again see my e-mail
38

39
00:03:58,800 --> 00:04:05,170
email and phone number my email I.D. and phone number has been taken to the account.
39

40
00:04:05,210 --> 00:04:13,380
So this was from the interesting way that through which we did authentication bypass on this website.
40

41
00:04:13,760 --> 00:04:21,200
I'm just trying to log in again to verify that I have taken over the phone number and the email I.D.
41

42
00:04:22,010 --> 00:04:28,880
as you can see I logged in I will just again go to my profile settings to verify and yes I have successfully
42

43
00:04:28,880 --> 00:04:32,170
taken over the phone number.
43

44
00:04:32,210 --> 00:04:32,750
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,590 --> 00:00:03,210
Welcome everyone.
1

2
00:00:03,210 --> 00:00:12,180
As in the previous videos we saw authentication bypass using OTP bypass attacks.
2

3
00:00:12,180 --> 00:00:22,020
So in this video we are going to learn how to do captcha bypass onto web applications.
3

4
00:00:22,020 --> 00:00:26,150
So we are going to use a response manipulation.
4

5
00:00:26,140 --> 00:00:35,600
Also verifying at the client side only and taking decisions is a very very dangerous for any application.
5

6
00:00:35,640 --> 00:00:46,020
The application should properly validate at the server and also if not this type of vulnerability will
6

7
00:00:46,170 --> 00:00:47,770
arise.
7

8
00:00:47,820 --> 00:00:51,840
So it's the practical time and let's see the practical
8

9
00:00:57,250 --> 00:01:01,750
so as you can see guys I am going to
9

10
00:01:04,940 --> 00:01:07,890
reset a password for my phone number.
10

11
00:01:08,390 --> 00:01:10,390
So I have entered my phone number.
11

12
00:01:10,820 --> 00:01:20,000
Now the application is asking for the six digit OTP code and a captcha as you can see I have supplied
12

13
00:01:20,000 --> 00:01:28,460
the right six digit OTP code but I will give a wrong captcha and let's see what the application says
13

14
00:01:28,850 --> 00:01:31,310
or what error does the application give.
14

15
00:01:32,420 --> 00:01:43,170
So in the captcha field I'm going to write captcha captch's are weak and I'm going to submit this as
15

16
00:01:43,170 --> 00:01:50,900
you can see this is the post request which is going to the website again in which it contains the OTP
16

17
00:01:50,900 --> 00:01:57,440
value as well as the captcha value the capture value is captchsareweak.
17

18
00:01:57,440 --> 00:02:03,950
I'm just going to do action do intercept response to this request because I want to see the response
18

19
00:02:04,100 --> 00:02:08,960
for this request.
19

20
00:02:10,670 --> 00:02:16,840
As you can see I got the response and in the body and I'm getting a number that is seven.
20

21
00:02:17,030 --> 00:02:20,930
I have modified that number from 7 to 1.
21

22
00:02:21,590 --> 00:02:30,050
And you can see I was able to bypass the captcha and here I'm able to reset the password for my account
22

23
00:02:30,320 --> 00:02:38,510
successfully so I will just change the password and hit submit and again see password successfully updated
23

24
00:02:38,720 --> 00:02:40,170
please log in.
24

25
00:02:40,190 --> 00:02:47,640
So this way I was able to bypass the captcha into the application thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,640 --> 00:00:04,560
Hello everyone.
1

2
00:00:04,590 --> 00:00:06,350
So in this video.
2

3
00:00:06,360 --> 00:00:16,710
We are going to learn about how to do ACCOUNT TAKEOVER based on user I.D. So mapping users as per the
3

4
00:00:16,710 --> 00:00:25,560
user I.D. That is uid, or group I.D. gidand other parameters like user_id on user
4

5
00:00:25,560 --> 00:00:37,490
equals to etc. is a is a good practice until proper checks and access control is put into place.
5

6
00:00:37,690 --> 00:00:47,130
Logging in to other users account by just using their user I.D. leads to account take over for this
6

7
00:00:47,130 --> 00:00:48,030
demonstration.
7

8
00:00:48,030 --> 00:00:58,680
I'm going to show you some websites on which we will do  account take or what based on user I.D. So practical
8

9
00:00:58,680 --> 00:00:59,400
time.
9

10
00:00:59,400 --> 00:01:01,080
And let's see the practical
10

11
00:01:06,000 --> 00:01:08,530
so for doing this practical.
11

12
00:01:08,760 --> 00:01:13,540
I'm going to take a website which is a live website.
12

13
00:01:13,550 --> 00:01:21,030
W for woman after coming to this website I'm going to log in into this Website.
13

14
00:01:21,690 --> 00:01:28,050
So I'm just giving my phone number here and the application sends OTP onto the full number as soon
14

15
00:01:28,050 --> 00:01:30,530
as I type my phone number.
15

16
00:01:31,110 --> 00:01:35,100
Now I have got a OTP on my number but
16

17
00:01:39,320 --> 00:01:39,740
yes.
17

18
00:01:40,010 --> 00:01:46,790
So I have given the right OTP and you can see I logged in into my account that the right OTP was given and
18

19
00:01:46,790 --> 00:01:52,580
I logged into my account as you can see this is my account and this is my email address.
19

20
00:01:53,960 --> 00:01:56,410
That I used to sign up.
20

21
00:01:56,450 --> 00:02:04,070
Now what I'm going to do here is I'm going to login into someone's else's account using my phone
21

22
00:02:04,070 --> 00:02:04,940
number.
22

23
00:02:05,060 --> 00:02:07,760
So let's see what I do.
23

24
00:02:08,000 --> 00:02:09,620
I have successfully logged out.
24

25
00:02:10,880 --> 00:02:14,410
I will again give my phone number for logging in.
25

26
00:02:16,460 --> 00:02:23,660
And again the application will send OTP on to my phone number at this time as you can see
26

27
00:02:23,920 --> 00:02:28,900
OTP validation failed because I give a wrong OTP here.
27

28
00:02:28,970 --> 00:02:34,130
So what I'm going to do is I'm going to start burpsuit
28

29
00:02:36,970 --> 00:02:45,820
as you can see this is the wrong way to be that is going and I will forward this request as you can see
29

30
00:02:46,180 --> 00:02:54,370
the success message is false and OTP OTP verification failed which means this OTP is wrong.
30

31
00:02:55,840 --> 00:02:58,420
So let me just give the right OTP this time
31

32
00:03:03,240 --> 00:03:07,150
we are not trying the simple OTP response manipulation.
32

33
00:03:07,290 --> 00:03:16,150
We are going to do account takeover this time so as you can see the OTP that is going is 5449
33

34
00:03:16,170 --> 00:03:23,670
so I will just head action to intercept a response to this request because I want to see the
34

35
00:03:23,670 --> 00:03:30,210
response to this post request which contains the phone number and OTP into its body
35

36
00:03:33,580 --> 00:03:43,170
so as you can see I have got the response for that specific request which was going to the API and in
36

37
00:03:43,180 --> 00:03:52,780
the response body if you look closely then you can see that the customer I.D. value which is here the
37

38
00:03:52,780 --> 00:04:00,520
customer I.D. value is 3 1 8 6 2 1 which is the customer I.D. value for my account.
38

39
00:04:00,610 --> 00:04:06,910
What I'm going to do is and I'm just going to change the I.D. of the customer as we are going to do
39

40
00:04:06,910 --> 00:04:10,720
account takeover for users I.D..
40

41
00:04:10,900 --> 00:04:15,310
So I'm going to just change it to 2 0 and I'm going to forward this
41

42
00:04:19,350 --> 00:04:28,410
I will do intercept off and I will go back to the application and you can see I got inside someone else's
42

43
00:04:28,410 --> 00:04:32,730
account I was able to log it into someone else's account.
43

44
00:04:32,730 --> 00:04:38,370
This is someone else's account that I am logged in also I can see the email address of someone else
44

45
00:04:38,940 --> 00:04:41,760
also I can see the phone number of someone else.
45

46
00:04:41,820 --> 00:04:50,810
Also there is a order a decent order which was done in 2020 of first 1799.
46

47
00:04:51,160 --> 00:04:57,660
So yes I was able to log in into someone else's account but I'm not going to perform any activity into
47

48
00:04:57,660 --> 00:05:00,400
this account just for proof.
48

49
00:05:00,600 --> 00:05:04,070
I have logged in and I'm going to show you the details of this account.
49

50
00:05:04,080 --> 00:05:12,030
The payment method say this be you shipping to this address which is in Andra Pradesh.
50

51
00:05:12,320 --> 00:05:12,670
Okay.
51

52
00:05:12,680 --> 00:05:15,240
And what was ordered it was.
52

53
00:05:15,960 --> 00:05:19,650
It's a lady's dress I suppose which was ordered.
53

54
00:05:19,650 --> 00:05:20,380
Yes right.
54

55
00:05:20,940 --> 00:05:21,520
Okay.
55

56
00:05:21,670 --> 00:05:25,100
So nothing to do much more with this order.
56

57
00:05:25,210 --> 00:05:32,220
We have successfully demonstration demonstrated the attack and I hope you guys were able to understand
57

58
00:05:32,220 --> 00:05:34,110
this and learn from this attack.
58

59
00:05:34,110 --> 00:05:34,560
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,860 --> 00:00:03,300
Hello everyone.
1

2
00:00:03,300 --> 00:00:11,880
So in this video we are going to learn authentication bypass based on user I.D. as we saw in the previous
2

3
00:00:11,880 --> 00:00:12,740
video.
3

4
00:00:12,780 --> 00:00:18,590
We are going to again do our account takeover by the user id.
4

5
00:00:18,610 --> 00:00:26,760
value for this I am going to take a website which is misrii.com.
5

6
00:00:28,500 --> 00:00:35,150
So I will just come onto this Web site and I will try to India Fights Corona.
6

7
00:00:35,630 --> 00:00:36,380
Okay.
7

8
00:00:36,720 --> 00:00:43,550
So I will just try to logging into the application so I'm going to give my phone number.
8

9
00:00:43,710 --> 00:00:48,030
That is a double 8200805621 and then OTP for logging.
9

10
00:00:49,410 --> 00:00:57,810
Now you can see the application has sent OTP onto my phone so I am willing to give the right OTP and
10

11
00:00:57,810 --> 00:01:02,650
you can see by giving the right OTP have logged in into my account.
11

12
00:01:03,660 --> 00:01:06,930
So this is my account.
12

13
00:01:07,020 --> 00:01:08,220
This is my phone number.
13

14
00:01:08,430 --> 00:01:10,020
And this is my account details
14

15
00:01:13,600 --> 00:01:23,290
I will just log off this account right now and what I'm going to do is kindly observe I'm going to
15

16
00:01:23,410 --> 00:01:33,340
again logging into my account with an OTP but this time I'm going to log in into someone else's account.
16

17
00:01:33,340 --> 00:01:39,490
So I'm going to enter the right OTP again that I have received onto my mobile phone.
17

18
00:01:40,810 --> 00:01:47,080
But before doing continue I'm going to start burp and I'm going to do intercept
18

19
00:01:51,770 --> 00:01:59,990
so I will quickly send this request to burp AS YOU CAN SEE THIS IS THE POST request that is going to
19

20
00:01:59,990 --> 00:02:10,130
that website which contains the parameters of mobile number and the verification code.
20

21
00:02:10,190 --> 00:02:16,130
Now I will click on action do intercept response to this request because I want to see the response
21

22
00:02:16,220 --> 00:02:18,620
of this verification request
22

23
00:02:22,420 --> 00:02:30,580
as you can see the OTP is verified successfully but a very important thing to observe here into the
23

24
00:02:30,580 --> 00:02:40,600
body is this user I.D. parameter as you can see the user I.D. parameter  reveals and says the user
24

25
00:02:40,600 --> 00:02:41,860
I.D. for this user.
25

26
00:02:42,610 --> 00:02:48,180
So in this case I'm the user and my user I.D. 6 3 4 5.
26

27
00:02:49,120 --> 00:02:55,450
What if I just tried to change the user I.D. value so I'm going to change the user Id right now
27

28
00:02:56,110 --> 00:03:01,480
and I'm going to get logged in into someone else's account.
28

29
00:03:01,480 --> 00:03:05,590
I will just forward this request go back to the application and observe.
29

30
00:03:06,040 --> 00:03:07,000
Yes.
30

31
00:03:07,180 --> 00:03:10,480
So I'm logged in into someone else's account.
31

32
00:03:10,480 --> 00:03:17,680
I'll just go inside there and you can see that e-mail address is someone else's email address as well
32

33
00:03:17,680 --> 00:03:21,260
as the mobile number is also someone else's.
33

34
00:03:21,280 --> 00:03:22,120
obile number
34

35
00:03:22,630 --> 00:03:31,270
So basically I was able to log in into this user's account without even the right OTP and the right
35

36
00:03:31,270 --> 00:03:39,080
phone number I just logged in into this account by modifying the user I.D..
36

37
00:03:39,160 --> 00:03:48,250
So this is called s authentication bypass account taken with using user I.D. parameter.
37

38
00:03:48,870 --> 00:03:50,260
My hope you guys understood.
38

39
00:03:50,260 --> 00:03:50,740
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,990 --> 00:00:02,720
Hello everyone.
1

2
00:00:02,730 --> 00:00:10,650
So in this video we are going to see an interesting account takeover due to OTP exposure.
2

3
00:00:11,850 --> 00:00:13,740
So what is this.
3

4
00:00:14,160 --> 00:00:22,660
Some web applications reveal the right OTP or a verification code in the response itself.
4

5
00:00:23,040 --> 00:00:31,110
Yes so many websites are vulnerable to this attack within the Web site that reveals the verification
5

6
00:00:31,130 --> 00:00:37,750
code to the attacker prior which is going to be sent on the victims device.
6

7
00:00:37,950 --> 00:00:48,210
So that attacker well beforehand only know what OTP token is going to be send it on to the victim
7

8
00:00:48,210 --> 00:00:56,610
device which is sitting anywhere into the world so for showing this demonstration we are going to do
8

9
00:00:56,610 --> 00:01:08,640
this attack on two Web site one as a vegetable and food ordering website and another one is a very famous
9

10
00:01:08,640 --> 00:01:12,780
bank Web site worldwide.
10

11
00:01:12,780 --> 00:01:17,150
So quickly start with the practical.
11

12
00:01:17,250 --> 00:01:20,850
So it's practical time now and let's see the practical
12

13
00:01:30,490 --> 00:01:33,080
so as you can see it.
13

14
00:01:33,740 --> 00:01:37,460
I came to this Web site that is ICICI careers.com
14

15
00:01:37,580 --> 00:01:45,760
And after coming to this Web site I have opened the chat bot to talk with the customer support.
15

16
00:01:46,160 --> 00:01:47,320
OK.
16

17
00:01:47,780 --> 00:01:53,120
So when I click on the chatbot it says me to continue.
17

18
00:01:53,120 --> 00:01:57,220
You have to verify yourself and give your phone number.
18

19
00:01:57,590 --> 00:02:00,200
So you're I'm going to enter my phone numbers
19

20
00:02:07,050 --> 00:02:07,560
yes.
20

21
00:02:07,680 --> 00:02:17,550
As you can see I've given my phone number here and I'm going to go in burp and do intercept on to see what
21

22
00:02:17,550 --> 00:02:21,270
is the response and request coming to this specific
22

23
00:02:23,980 --> 00:02:24,610
request.
23

24
00:02:25,660 --> 00:02:31,940
So as you can see I did send in the request to Burpsuit.
24

25
00:02:31,990 --> 00:02:37,840
And you can see here the phone number is going into a post request.
25

26
00:02:38,020 --> 00:02:39,440
Right.
26

27
00:02:39,760 --> 00:02:43,120
Let's do intercept.
27

28
00:02:43,180 --> 00:02:55,750
The response of this request I will just forward this and see that what is the response for this request.
28

29
00:02:55,750 --> 00:03:02,580
As you can see the response contains the OTP that the user is going to get.
29

30
00:03:02,770 --> 00:03:08,760
As you can see that the OTP is being already shown and the OTP is 
30

31
00:03:08,810 --> 00:03:13,350
4800 that is going to go to the user.
31

32
00:03:14,260 --> 00:03:21,130
As you can see I'm going to show you my phone screen right now in which I am able to get that.
32

33
00:03:21,130 --> 00:03:28,630
Would you be onto my phone after a couple of seconds which is exactly the same with the attack that
33

34
00:03:28,630 --> 00:03:30,230
has already seen.
34

35
00:03:30,370 --> 00:03:34,320
So you can see that OTP is same 4800 4800
35

36
00:03:40,340 --> 00:03:41,920
yes the OTP same.
36

37
00:03:42,380 --> 00:03:51,410
So I'm just going to copy this OTP intercept off go in here and enter the OTP and click on verify as you
37

38
00:03:51,410 --> 00:03:52,220
can see.
38

39
00:03:52,220 --> 00:03:53,920
Welcome to the world of exciting.
39

40
00:03:53,950 --> 00:03:54,470
Yes.
40

41
00:03:55,220 --> 00:03:55,480
Yes.
41

42
00:03:55,490 --> 00:04:04,130
So I was able to bypass this verification and I was able to do account takeover for any one into
42

43
00:04:04,130 --> 00:04:08,100
this world onto this bank's Web site.
43

44
00:04:08,120 --> 00:04:08,630
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,700 --> 00:00:04,260
Hello everyone.
1

2
00:00:04,290 --> 00:00:13,950
So we're going to see one more proof of concept in this video for authentication bypass exposure of
2

3
00:00:14,220 --> 00:00:15,780
OTP in the response.
3

4
00:00:16,650 --> 00:00:23,290
So as you can see I'm on to this Web site and I'm onto the registry page now.
4

5
00:00:23,490 --> 00:00:26,670
I'm going to register my phone number onto this Web site
5

6
00:00:35,550 --> 00:00:39,930
so I have typed my phone number and I will fill the other fields too
6

7
00:00:46,230 --> 00:00:49,830
I have send the request to Burpsuite.
7

8
00:00:49,980 --> 00:00:57,480
As you can see I clicked on click here for verification OTP and I did intercept on into the Burpsuite
8

9
00:01:00,070 --> 00:01:07,690
as you can see this is the post request that is going to the Web site in the body as you can see my
9

10
00:01:07,690 --> 00:01:12,500
phone number is there with the contact parameter.
10

11
00:01:12,610 --> 00:01:21,700
Now I will do action do intercept response to this request because I want to see the response to this
11

12
00:01:21,700 --> 00:01:27,630
specific request after doing this I will forward this request.
12

13
00:01:27,940 --> 00:01:36,010
As you can see when I did forward to this request in the response I am able to see the OTP that I am
13

14
00:01:36,010 --> 00:01:41,850
going to receive right now or the victim is going to receive onto his or her phone.
14

15
00:01:41,890 --> 00:01:49,420
So here is one more example of OTP exposure into the response itself.
15

16
00:01:49,510 --> 00:01:57,100
So the attacker can take any arbitrary phone number and then send a verification code and he will be
16

17
00:01:57,100 --> 00:02:03,600
able to see the verification code into the response itself.
17

18
00:02:03,630 --> 00:02:10,710
So let me just copy this response and try to verify and check that this OTP is working or not.
18

19
00:02:11,700 --> 00:02:15,540
Let me just show you on my mobile phone also.
19

20
00:02:15,570 --> 00:02:17,670
I have received the same OTP
20

21
00:02:22,180 --> 00:02:28,400
as you can see I have received the same OTP onto my phone using
21

22
00:02:35,320 --> 00:02:35,940
now.
22

23
00:02:36,080 --> 00:02:39,520
I will put this verification code and click on verify
23

24
00:03:02,020 --> 00:03:06,880
as you can see my account is verified successfully.
24

25
00:03:06,880 --> 00:03:12,970
So this attack was successful and we were able to exploit this attack.
25

26
00:03:12,970 --> 00:03:13,450
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,900 --> 00:00:02,540
Hello everyone.
1

2
00:00:02,550 --> 00:00:08,750
So in this video we are going to see an interesting account take over due to a two factor authentication
2

3
00:00:08,760 --> 00:00:09,470
logic flaw.
3

4
00:00:10,380 --> 00:00:20,850
So in this video I was able to find out a flaw into a web application into which I was able to keep
4

5
00:00:20,850 --> 00:00:27,330
a two factor authentication onto the website after keeping the two factor authentication.
5

6
00:00:27,450 --> 00:00:32,070
The website made me log out of that specific account.
6

7
00:00:32,310 --> 00:00:39,360
And now when I tried to log in into the website it asked me for the 2 factor authentication code before I
7

8
00:00:39,360 --> 00:00:40,480
can log in.
8

9
00:00:40,680 --> 00:00:50,000
But I found a way through which I was able to bypass that 2 factor authentication verification window.
9

10
00:00:50,190 --> 00:00:52,830
So let's see how I was able to do that.
10

11
00:00:54,050 --> 00:00:55,530
So it's the practical time.
11

12
00:00:55,650 --> 00:00:58,330
And let's see the video POC
12

13
00:01:03,230 --> 00:01:11,880
as you can see I am on this account rohitshifa.officient.io and I have logged into my e-mail
13

14
00:01:11,880 --> 00:01:16,320
I.D. That is blackops.ruby@gmail.com.
14

15
00:01:16,500 --> 00:01:21,820
If you look at the bottom of the screen you can see 2 factor authentication is disabled right now
15

16
00:01:21,820 --> 00:01:24,550
Now I'm going to enable it.
16

17
00:01:25,060 --> 00:01:31,420
So when I tried to enable it you can see the application is saying Are you sure you will be logged out
17

18
00:01:31,510 --> 00:01:33,350
and you will need your smartphone to continue
18

19
00:01:33,370 --> 00:01:35,230
You can do so basically.
19

20
00:01:35,250 --> 00:01:43,510
Then I'm going to enable the 2 factor authentication the application will log me out so I will just hit.
20

21
00:01:43,750 --> 00:01:44,110
OK.
21

22
00:01:47,230 --> 00:01:53,420
And you can see I'm thrown out of the application now when I tried to log in into the application with
22

23
00:01:53,420 --> 00:02:01,410
my correct password the application will ask me the two factor authentication window.
23

24
00:02:01,750 --> 00:02:12,590
So it is asking me to authenticate with Google authenticator or Auth0 Guardian.
24

25
00:02:12,600 --> 00:02:15,030
So now I'm not able to log in into my account
25

26
00:02:19,500 --> 00:02:26,270
yes so how I'm able to bypass this.
26

27
00:02:26,360 --> 00:02:31,630
See I again tried prior method but I'm not able to log in I'm stuck here.
27

28
00:02:31,650 --> 00:02:34,110
I cannot for the proceed into my account.
28

29
00:02:34,620 --> 00:02:46,510
So I will go in burp again and I have captured that request for which I was keeping the two factor authentication
29

30
00:02:46,750 --> 00:02:47,320
on.
30

31
00:02:47,440 --> 00:02:57,800
As you can see a post request is going which says MFA and MFA enabled means multi factor authentication
31

32
00:02:57,880 --> 00:02:59,900
so it was 1.
32

33
00:02:59,900 --> 00:03:01,740
So now I did 0 here.
33

34
00:03:02,520 --> 00:03:03,050
OK.
34

35
00:03:03,080 --> 00:03:04,010
So I did.
35

36
00:03:04,330 --> 00:03:07,610
which means multi factor authentication enabled 0.
36

37
00:03:07,760 --> 00:03:10,030
I am turning it off.
37

38
00:03:10,190 --> 00:03:17,830
Now I will again go to the website and prior to logging with my the right password and I will hit log in.
38

39
00:03:18,020 --> 00:03:24,760
And now you can see the 2 factor authentication window has gone away from here
39

40
00:03:24,760 --> 00:03:29,000
And I am directly logged into my website yes.
40

41
00:03:29,130 --> 00:03:34,530
So I will just go there in settings and I will just try show you that 2 factor authentication is
41

42
00:03:34,800 --> 00:03:36,870
disabled Yes.
42

43
00:03:37,520 --> 00:03:38,920
So I hope you guys understood.
43

44
00:03:38,930 --> 00:03:39,320
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,630 --> 00:00:01,830
Hello everyone.
1

2
00:00:01,830 --> 00:00:09,180
So in this we do we are going to see an interesting account takeover of support person and CEO Email
2

3
00:00:09,630 --> 00:00:12,210
due to a logic flaw into a application.
3

4
00:00:12,780 --> 00:00:21,480
So in this video POC I'm going to show you how I was able to find out a vulnerability onto a
4

5
00:00:21,560 --> 00:00:27,450
website wherein I was able to takeover anyone's email address.
5

6
00:00:27,450 --> 00:00:32,440
So for proving this bug I took over my another email.
6

7
00:00:32,730 --> 00:00:39,660
And also I did took over the support email of that company and the CEO's e-mail and I reported the 
7

8
00:00:39,660 --> 00:00:41,070
vulnerability
8

9
00:00:41,070 --> 00:00:45,690
So the practical time and let's see how can we do this.
9

10
00:00:47,670 --> 00:00:52,600
So as you can see I'm on to a website in which I am on to my profile.
10

11
00:00:52,650 --> 00:00:54,830
This is my account and this is my profile
11

12
00:00:58,810 --> 00:01:06,180
as you can see my primary email address is blackops.ruby@gmail.com.
12

13
00:01:06,220 --> 00:01:12,230
Now you can see the application gives me one more option to add an email address.
13

14
00:01:12,310 --> 00:01:17,920
So I'm going to add one more email address.
14

15
00:01:17,920 --> 00:01:25,070
So for example I'm adding one more email address which is my email address 
15

16
00:01:25,070 --> 00:01:26,290
thesrsecure@gmail.com
16

17
00:01:29,450 --> 00:01:32,220
and I added the email address.
17

18
00:01:32,390 --> 00:01:40,970
Now as you can see the application sends activation e-mail on any new e-mail that has been added as
18

19
00:01:40,970 --> 00:01:46,310
you can see it is showing inactive and sender activation e-mail again.
19

20
00:01:46,310 --> 00:01:53,420
So my new e-mail address that is thesrsecure@gmail.com has got an e-mail verification
20

21
00:01:53,420 --> 00:02:02,840
link but I will bypass that and I will activate this e-mail without even clicking that verification
21

22
00:02:02,840 --> 00:02:03,470
link.
22

23
00:02:03,470 --> 00:02:04,510
This was the flaw.
23

24
00:02:04,700 --> 00:02:07,760
So let's see how to do this.
24

25
00:02:07,820 --> 00:02:12,970
So as you can see this is inactive right now.
25

26
00:02:13,130 --> 00:02:16,490
I will refresh and show again.
26

27
00:02:17,720 --> 00:02:21,260
It is inactive.
27

28
00:02:21,560 --> 00:02:23,830
I will just go to my account.
28

29
00:02:23,960 --> 00:02:27,580
Remember guys this is my blackops.Ruby account.
29

30
00:02:27,620 --> 00:02:28,070
OK.
30

31
00:02:28,190 --> 00:02:30,260
This is not thesrsecure account.
31

32
00:02:30,260 --> 00:02:32,660
This is Black Ops dot Ruby account.
32

33
00:02:32,660 --> 00:02:39,340
When I signed up on the website I got one link to activate my blackops.ruby account.
33

34
00:02:39,350 --> 00:02:39,880
OK.
34

35
00:02:40,010 --> 00:02:42,980
So I'm again going to click on the same link.
35

36
00:02:42,980 --> 00:02:49,700
I have already  clicked on this link once for verification of my account blackops.ruby and I was
36

37
00:02:49,700 --> 00:02:51,850
able to successfully make an account.
37

38
00:02:52,010 --> 00:02:59,240
I will again reuse the same link to verify the another account that that is the thesrsecure@gmail.com
38

39
00:02:59,260 --> 00:03:02,660
email address so I'm just going to
39

40
00:03:06,480 --> 00:03:11,800
I'm just going to click on the same link on the blackops.ruby
40

41
00:03:11,820 --> 00:03:16,630
Email address after clicking on the same link
41

42
00:03:20,790 --> 00:03:23,660
it will say account is activated.
42

43
00:03:23,880 --> 00:03:31,200
I know my account was already activated but the flaw lies here that when I click on the activation link
43

44
00:03:31,200 --> 00:03:39,720
of my primary email address any new email address which has been added into the applications will automatically
44

45
00:03:39,720 --> 00:03:41,090
get verified.
45

46
00:03:41,130 --> 00:03:42,570
So let's see this.
46

47
00:03:42,570 --> 00:03:49,190
Let me just try to reload this and you can see this inactive will go away and the application and the
47

48
00:03:49,200 --> 00:03:53,050
application has successfully verified the email address.
48

49
00:03:55,200 --> 00:04:03,930
Let me just again reload the browser and show you as you can see there is no again the inactive thing
49

50
00:04:03,930 --> 00:04:06,870
that is coming onto my Web application.
50

51
00:04:06,870 --> 00:04:13,540
So what I will do right now is I hope you guys understood this.
51

52
00:04:13,580 --> 00:04:19,970
What I'm going to do right now is I'm going to show you how I am going to log in through this email
52

53
00:04:19,970 --> 00:04:20,760
address.
53

54
00:04:20,840 --> 00:04:24,040
I will make this email address as a primary email address.
54

55
00:04:24,060 --> 00:04:29,780
Then I'm going to log in through that email address just to prove that I have successfully taken over
55

56
00:04:29,990 --> 00:04:31,570
this email address
56

57
00:04:41,980 --> 00:04:42,490
yes.
57

58
00:04:42,520 --> 00:04:45,430
So I will make this a primary email address
58

59
00:04:53,150 --> 00:04:58,940
as you can see this email address has been made a primary email address I will log out of this account
59

60
00:04:58,990 --> 00:05:00,560
now.
60

61
00:05:00,860 --> 00:05:05,880
So this time I'm going to log in through the new email address that we took over.
61

62
00:05:05,930 --> 00:05:10,090
That is thesrsecure@gmail.com
62

63
00:05:14,030 --> 00:05:20,490
so I will just click on login and I will give the new email address in the log in field
63

64
00:05:20,570 --> 00:05:24,430
I will hit continue and I will give the password of my account
64

65
00:05:29,550 --> 00:05:37,410
the password is admin 1 2 3 and now the application will successfully log me in into this account.
65

66
00:05:37,770 --> 00:05:42,890
So as you can see I am logged in into this account.
66

67
00:05:42,900 --> 00:05:49,790
Let me just go to the profile section and show you that these two are the email addresses and 
67

68
00:05:49,800 --> 00:05:57,020
thesrsecure@gmail.com is now my primary email address so I hope you guys understood.
68

69
00:05:57,030 --> 00:05:58,080
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,080 --> 00:00:02,430
Hello everyone.
1

2
00:00:02,430 --> 00:00:09,450
So in this we do we are going to see what are the mitigations for this one ability that is authentication
2

3
00:00:09,450 --> 00:00:11,210
bypass.
3

4
00:00:11,340 --> 00:00:13,250
So the first point.
4

5
00:00:13,260 --> 00:00:20,320
Do not rely on client side only make the checks at the server side.
5

6
00:00:20,340 --> 00:00:22,830
Also they are very important.
6

7
00:00:23,070 --> 00:00:28,710
You should not allow or you should not rely on just on the client side.
7

8
00:00:28,710 --> 00:00:31,780
If you make that then it becomes very dangerous.
8

9
00:00:32,080 --> 00:00:36,410
Verifying the client side and taking decisions is very very dangerous.
9

10
00:00:36,510 --> 00:00:45,360
As we saw into many of the videos and proof of concept that taking decisions on client site turns out to
10

11
00:00:45,360 --> 00:00:47,620
be very dangerous.
11

12
00:00:48,030 --> 00:00:54,690
Use authentication based on strong tokens such as json web token mechanism.
12

13
00:00:54,990 --> 00:01:01,950
Use authentication based on encrypted data which can be AES for example.
13

14
00:01:02,310 --> 00:01:11,090
So these are some of the points that one can use to mitigate this types of attacks.
14

15
00:01:11,100 --> 00:01:20,520
So in this authentication bypass we learned how one attacker can misuse the functionalities of the web
15

16
00:01:20,520 --> 00:01:28,950
application which are not securely configured and just which are mis configured and which the attacker
16

17
00:01:28,980 --> 00:01:33,540
can easily attack starting from a response.
17

18
00:01:33,540 --> 00:01:39,240
Manipulation, captcha bypas,s two factor authentication token bypass.
18

19
00:01:39,240 --> 00:01:45,250
We saw many different attacks and proof of concept in which we were able to bypass these.
19

20
00:01:45,270 --> 00:01:50,200
And lastly we saw what are the mitigations for these types of attacks.
20

21
00:01:50,220 --> 00:01:53,870
So I hope you guys understood that authentication bypass videos.
21

22
00:01:54,420 --> 00:01:55,530
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,870 --> 00:00:02,270
Hello everyone.
1

2
00:00:02,280 --> 00:00:07,950
So in this video we're going to see authentication bypass interview questions and the approach to answer
2

3
00:00:07,950 --> 00:00:08,190
them.
3

4
00:00:09,180 --> 00:00:13,150
So the first question the interviewer may ask you that.
4

5
00:00:13,320 --> 00:00:17,370
What is authentication bypass and what are the types.
5

6
00:00:17,370 --> 00:00:21,400
So basically in this question the interviewer wants to know that.
6

7
00:00:21,450 --> 00:00:23,270
Are you familiar with 
7

8
00:00:23,300 --> 00:00:24,610
Auth Bypass.
8

9
00:00:24,870 --> 00:00:28,290
So you can just give the answer based on what is authentication bypass.
9

10
00:00:28,710 --> 00:00:36,060
So this is a technique in which the attacker is able to bypass the authentication or authorization onto
10

11
00:00:36,060 --> 00:00:37,140
any Web site.
11

12
00:00:37,380 --> 00:00:42,080
For example the attacker can bypass two factor authentication.
12

13
00:00:42,150 --> 00:00:46,000
The attacker can bypass captcha verification.
13

14
00:00:46,110 --> 00:00:52,460
The attacker can bypass OTP verifications etc.. next.
14

15
00:00:52,490 --> 00:00:56,090
What is the severity the interviewer wants to know that.
15

16
00:00:56,150 --> 00:01:02,690
Do you know what is the real impact or the extreme impact of authentication bypass.
16

17
00:01:03,410 --> 00:01:12,390
So in this question you have to say like authentication bypass is the vulnerability with the highest severity.
17

18
00:01:12,400 --> 00:01:13,040
Why.
18

19
00:01:13,100 --> 00:01:16,750
Because you can do an account takeover.
19

20
00:01:16,880 --> 00:01:20,470
You can do a privilege escalation through this vulnerability
20

21
00:01:20,750 --> 00:01:24,740
In this question you need to explain that interview.
21

22
00:01:25,550 --> 00:01:34,280
And you need to convince the interviewer by explaining this bug can lead to a p0 level severity.
22

23
00:01:34,280 --> 00:01:45,770
Next question why it happens authentication bypass happens because not of proper validation or the application
23

24
00:01:45,830 --> 00:01:52,850
trust the client side and take decisions as we have already seen into the mitigations of authentication
24

25
00:01:52,850 --> 00:01:53,650
bypass.
25

26
00:01:53,840 --> 00:02:01,440
You can refer to that video to know about why it happens and how can we fix it.
26

27
00:02:01,490 --> 00:02:04,460
So what is the impact on business.
27

28
00:02:04,520 --> 00:02:12,560
This is the interviewer's favorite question where he wants to know that what authentication bypass can
28

29
00:02:12,560 --> 00:02:14,260
lead to the business.
29

30
00:02:14,270 --> 00:02:22,790
So in this question you have to explain the interviewer that how severe it can be for any attack ad to
30

31
00:02:23,000 --> 00:02:26,660
log in and see anyone's account.
31

32
00:02:26,660 --> 00:02:34,490
Any attacker could see the interviewers account details and for example if it is a banking environment
32

33
00:02:34,790 --> 00:02:42,170
he could see how much balance is there into his or her account or maybe try to transfer some funds.
33

34
00:02:42,320 --> 00:02:47,520
So the business impact of this vulnerability is very very critical.
34

35
00:02:47,960 --> 00:02:54,680
Next explain authentication bypass to a 10 year old kid a HR and a red team member.
35

36
00:02:55,430 --> 00:03:04,910
So in this question the interviewer wants to wants you to know that this vulnerability is a very very
36

37
00:03:04,910 --> 00:03:06,380
critical vulnerability.
37

38
00:03:06,380 --> 00:03:11,870
And do you know that in and out of this vulnerability so you can you explain this vulnerability to a
38

39
00:03:11,870 --> 00:03:12,650
10 year old kid.
39

40
00:03:12,920 --> 00:03:13,820
Yes.
40

41
00:03:13,850 --> 00:03:20,580
So basically you can login to anyone's account without the right username and password is the answer
41

42
00:03:21,050 --> 00:03:24,470
through my perspective for a 10 year old kid.
42

43
00:03:24,980 --> 00:03:31,240
So you can log in into his account without his username and password or without the right OTP coming on
43

44
00:03:31,240 --> 00:03:33,610
to his mobile phone.
44

45
00:03:33,740 --> 00:03:41,540
Now if explaining to a HR you again just explain the business impact how this can impact the business
45

46
00:03:41,720 --> 00:03:48,280
how it can impact the reputation how it can impact the shares, explaining it to a red team member.
46

47
00:03:48,290 --> 00:03:49,590
Wouldn't be that difficult.
47

48
00:03:49,670 --> 00:03:55,640
As we have seen a lot of videos and you can explain the technicality and the severity of this vulnerability
48

49
00:03:56,000 --> 00:03:58,490
to a security professional.
49

50
00:03:58,550 --> 00:03:59,880
So what is the fix.
50

51
00:03:59,930 --> 00:04:03,090
We have already seen the fixes into the mitigations video.
51

52
00:04:03,110 --> 00:04:04,190
You can refer to that.
52

53
00:04:04,970 --> 00:04:11,000
I hope you guys find this we do a useful for your interview preparations and you understand the approach
53

54
00:04:11,060 --> 00:04:13,210
of an interviewer.
54

55
00:04:13,220 --> 00:04:13,700
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 2: No Rate-Limit Attacks

0
1
00:00:00,960 --> 00:00:02,670
Hello and welcome.
1

2
00:00:02,670 --> 00:00:07,140
So today we're going to see a vulnerability which is No-Rate limit.
2

3
00:00:07,140 --> 00:00:12,930
So in this video series we will see what is No-Rate limit why it happens.
3

4
00:00:13,020 --> 00:00:15,450
What is the severity of No-Rate limit.
4

5
00:00:15,450 --> 00:00:18,340
And what are the different ways to do No-Rate limit.
5

6
00:00:19,080 --> 00:00:27,570
OK so how a No-Rate limit works as you can see on the screen the left side is the client the right
6

7
00:00:27,570 --> 00:00:29,190
side is the server.
7

8
00:00:29,250 --> 00:00:33,850
So when a client will send a request to the server the server will accept it.
8

9
00:00:33,850 --> 00:00:36,780
What if the client sends one more request.
9

10
00:00:36,780 --> 00:00:41,220
What if the client sends the third request and the fourth request.
10

11
00:00:41,220 --> 00:00:50,250
So the client sends X request and the server accepts all the X request and fulfill all those request
11

12
00:00:50,370 --> 00:00:55,350
and gives a response for all the request that is coming from the client.
12

13
00:00:55,370 --> 00:00:56,640
Here is a response.
13

14
00:00:56,640 --> 00:00:58,050
Get your results.
14

15
00:00:58,050 --> 00:01:06,120
So in this case the server is not properly handling or checking how many simultaneous requests
15

16
00:01:06,180 --> 00:01:08,310
are coming from the client.
16

17
00:01:08,310 --> 00:01:13,350
And this leads to a No-Rate limit.
17

18
00:01:13,350 --> 00:01:19,040
So how are we going to see this and how we are going to exploit.
18

19
00:01:19,050 --> 00:01:27,020
So the first thing that we are going to see the first vulnerability is No-Rate limit on account creation.
19

20
00:01:27,210 --> 00:01:34,050
So in here we will send X number of simultaneous requests to the server and the server will act on each
20

21
00:01:34,050 --> 00:01:40,980
request thus by making X number of email account onto the website.
21

22
00:01:40,980 --> 00:01:47,960
So no validation or limiting the request and taking decisions is very dangerous for an server.
22

23
00:01:48,030 --> 00:01:54,230
So let's go to the practical time and let's see a practical.
23

24
00:01:55,650 --> 00:02:04,180
So for practical I'm going to show you attack on this Web site Web site which is voot.com.
24

25
00:02:04,330 --> 00:02:09,440
So in this attack I'm going to sign up quickly onto the Web site using my email address.
25

26
00:02:09,970 --> 00:02:13,030
As you can see my e-mail addresses 
26

27
00:02:13,390 --> 00:02:20,710
sorry hacker.udemy@gmail.com and I'm going to signup user account not found is the
27

28
00:02:20,710 --> 00:02:27,670
error the application give me and automatically redirected me to the registration page.
28

29
00:02:27,940 --> 00:02:30,760
Now you can see I'm setting up a password for my account.
29

30
00:02:30,760 --> 00:02:33,250
I will just intercept this request and Burpsuite
30

31
00:02:39,330 --> 00:02:45,660
as you can see this is the request which is going of checking that the e-mail address exists or does
31

32
00:02:45,660 --> 00:02:48,480
not exist.
32

33
00:02:48,600 --> 00:02:53,850
So I'm just going to send this to repeater for backup purpose and I'm going to do it do intercept response
33

34
00:02:53,850 --> 00:02:59,830
to this request because I want to see what is the response to this request.
34

35
00:03:00,010 --> 00:03:08,140
And as you can see the response is is exist= false which means this user does not exist on the website
35

36
00:03:08,260 --> 00:03:11,760
and a user can sign up using this e-mail address
36

37
00:03:25,730 --> 00:03:30,380
so now as we go on back onto the web browser you can see
37

38
00:03:33,110 --> 00:03:39,380
that a registration form appears and I'm going to fill the registration form.
38

39
00:03:40,100 --> 00:03:43,520
So in the name field I'm going to type my name date of birth.
39

40
00:03:43,580 --> 00:03:45,500
I'm going to take any random values
40

41
00:03:53,050 --> 00:03:58,850
and in the gender I'll take male and languages English , Hindi the ok before submitting the request.
41

42
00:03:58,860 --> 00:04:05,880
I will do intercept on and I will hit submit a request and I will capture the request in burpsuite
42

43
00:04:06,120 --> 00:04:09,170
as you can see this is the request which I wanted.
43

44
00:04:09,180 --> 00:04:16,230
This request contains all the details that I have submitted onto the browser as you can see type traditional
44

45
00:04:16,500 --> 00:04:23,790
device I.D. Macintosh device brand Mac data e-mail address hacker.udemy@gmail.com password
45

46
00:04:23,820 --> 00:04:25,470
admin@123
46

47
00:04:25,500 --> 00:04:29,070
First name last name Rohit and other details as well.
47

48
00:04:29,730 --> 00:04:33,100
So this request is going to the server.
48

49
00:04:33,120 --> 00:04:34,660
I'll send this to repeater
49

50
00:04:35,070 --> 00:04:42,200
I'll send this to intruder because in intruder I'm going to perform the attack of No-Rate limit.
50

51
00:04:42,200 --> 00:04:47,460
I will also do intercept response to this request just to check what is the response coming from the
51

52
00:04:47,500 --> 00:04:47,880
server
52

53
00:04:51,700 --> 00:04:55,890
I will just forward this request and wait for the response from the server.
53

54
00:04:59,120 --> 00:05:04,080
And as you can see on the to the screen right now I've got the response from the server and the server
54

55
00:05:04,110 --> 00:05:11,730
has made the account for me as you can see I will just forward this request to intercept off again go
55

56
00:05:11,730 --> 00:05:12,970
to my web browser.
56

57
00:05:13,050 --> 00:05:16,470
You have successfully signed up onto voot.com.
57

58
00:05:16,470 --> 00:05:22,870
I will go into my settings to just show you that I have successfully made an account onto this Web site
58

59
00:05:23,340 --> 00:05:25,140
which means I have created an account
59

60
00:05:28,230 --> 00:05:31,200
now I will just go into the intruder.
60

61
00:05:31,290 --> 00:05:37,230
I will go into positions and I am going to set up position through which I'm going to make multiple
61

62
00:05:37,230 --> 00:05:40,850
account by sending multiple X request.
62

63
00:05:40,860 --> 00:05:45,180
So the position that I am going to take is the e-mail position.
63

64
00:05:45,230 --> 00:05:51,930
OK so I am going to just click on Add which means I want to take this position.
64

65
00:05:51,930 --> 00:05:58,050
Now I will go into the payload and I am going to supply arbitrary email addresses.
65

66
00:05:58,050 --> 00:06:04,050
So let me just write down some some of my email addresses that I'm going to use for attack.
66

67
00:06:04,050 --> 00:06:08,880
So let me just write down first e-mail and one more email address
67

68
00:06:15,500 --> 00:06:41,060
let's say one more email address.
68

69
00:06:41,270 --> 00:06:46,370
I will take around 10 email address for this attack.
69

70
00:07:24,610 --> 00:07:26,440
And one more last e-mail address.
70

71
00:07:30,580 --> 00:07:30,890
Yeah.
71

72
00:07:31,080 --> 00:07:33,810
So I have taken these many e-mail addresses.
72

73
00:07:33,810 --> 00:07:41,100
Let me just save this file and let me give the names email names.txt and let me just save this file
73

74
00:07:41,100 --> 00:07:43,580
on to my next desktop.
74

75
00:07:47,770 --> 00:07:49,270
Okay so I will just save this.
75

76
00:07:49,300 --> 00:07:50,800
Yeah I've saved this file.
76

77
00:07:51,100 --> 00:07:56,080
Let me copy this names and let me just paste into this payload.
77

78
00:07:56,580 --> 00:07:56,680
Okay
78

79
00:08:01,090 --> 00:08:01,290
okay.
79

80
00:08:01,300 --> 00:08:05,040
So I'm just going to click on paste.
80

81
00:08:05,080 --> 00:08:06,290
No I will not load.
81

82
00:08:06,310 --> 00:08:07,390
I will just click on paste.
82

83
00:08:07,410 --> 00:08:08,050
Yup.
83

84
00:08:08,140 --> 00:08:14,560
So as you can see I've pasted 10 e-mail addresses the position that I've given is the e-mail parameter.
84

85
00:08:14,620 --> 00:08:21,560
Now I will go to the options tab and going in options tab as you can see I'm going to give a throttle.
85

86
00:08:22,030 --> 00:08:28,960
So what is throttle throttle means the delay between two simultaneous request.
86

87
00:08:29,320 --> 00:08:32,530
So let's say the first request is going at one second.
87

88
00:08:32,530 --> 00:08:35,470
The second request will go after five seconds.
88

89
00:08:35,470 --> 00:08:35,750
Okay.
89

90
00:08:35,770 --> 00:08:42,850
Because I have given the throttle the delay in 5000 milliseconds 5000 milliseconds means five seconds.
90

91
00:08:42,850 --> 00:08:51,660
So each request will go after waiting for five seconds ok fine.
91

92
00:08:51,750 --> 00:08:55,600
Now I think everything is ready.
92

93
00:08:55,650 --> 00:08:57,090
I will just start the attack
93

94
00:09:01,650 --> 00:09:09,690
so let me just start the attack and let's wait to see if we are able to make multiple accounts in one
94

95
00:09:09,690 --> 00:09:13,840
go by exploiting No-Rate limit.
95

96
00:09:14,310 --> 00:09:17,770
So I can see the status is coming 400.
96

97
00:09:18,180 --> 00:09:21,120
Let me see why it is giving 400
97

98
00:09:31,420 --> 00:09:33,460
let me just go to the first e-mail.
98

99
00:09:33,520 --> 00:09:35,660
Go check in the response and check.
99

100
00:09:35,770 --> 00:09:37,840
So e-mail must be a valid e-mail.
100

101
00:09:37,840 --> 00:09:38,830
Let me see that e-mail.
101

102
00:09:38,890 --> 00:09:39,440
OK.
102

103
00:09:39,520 --> 00:09:42,560
The e-mail field has been encoded.
103

104
00:09:42,640 --> 00:09:44,580
Let me see for another e-mail.
104

105
00:09:44,590 --> 00:09:45,890
It is happening the same.
105

106
00:09:46,330 --> 00:09:46,630
Yes.
106

107
00:09:46,630 --> 00:09:48,150
E-mail must be a valid e-mail.
107

108
00:09:48,190 --> 00:09:54,460
So guys we can see my e-mail is getting encoded so I will just go back in to the payload options and
108

109
00:09:54,970 --> 00:09:56,250
payload encoding.
109

110
00:09:56,260 --> 00:09:57,180
I'll turn it off.
110

111
00:09:57,730 --> 00:09:58,220
OK.
111

112
00:09:58,300 --> 00:10:04,900
I have done the payload encoding off because my payload was getting encoded my email address for getting
112

113
00:10:04,900 --> 00:10:05,910
encoded.
113

114
00:10:05,980 --> 00:10:07,210
I will again start the attack
114

115
00:10:13,400 --> 00:10:16,990
the e-mail is already registered with us which is hacker.udemy
115

116
00:10:17,050 --> 00:10:18,130
Okay fine.
116

117
00:10:18,190 --> 00:10:24,910
Was we just made a account the second request is akz.ruby@gmail and let us see the response.
117

118
00:10:24,910 --> 00:10:26,230
Awesome.
118

119
00:10:26,230 --> 00:10:32,450
So we were successfully able to make account perfect.
119

120
00:10:32,530 --> 00:10:33,850
Let's see for this e-mail.
120

121
00:10:34,000 --> 00:10:35,590
I think this e-mail already exists.
121

122
00:10:35,590 --> 00:10:36,510
We made the account.
122

123
00:10:36,520 --> 00:10:37,510
Yes.
123

124
00:10:37,570 --> 00:10:41,430
So let's see for the next e-mail.
124

125
00:10:41,590 --> 00:10:41,800
Yeah.
125

126
00:10:41,830 --> 00:10:45,700
So we were able to make an account using this e-mail address.
126

127
00:10:45,700 --> 00:10:47,080
Let's see for this e-mail address.
127

128
00:10:47,080 --> 00:10:52,220
Yes we are all again able to make account for this e-mail address also.
128

129
00:10:52,580 --> 00:10:53,980
Let's see for this e-mail address.
129

130
00:10:54,010 --> 00:10:58,570
Yes we are able to make account for this for this hacktify testing.
130

131
00:10:58,570 --> 00:11:03,530
Yes we are able to make account for this e-mail address also.
131

132
00:11:03,550 --> 00:11:10,880
So basically we have right now made 10 account on the website by exploiting No-Rate limit.
132

133
00:11:10,920 --> 00:11:16,590
There was there should be a type of checking done a type of validation.
133

134
00:11:16,660 --> 00:11:19,010
So there is no validation for it.
134

135
00:11:19,150 --> 00:11:25,330
For example now I'm going to take this e-mail address that is hacktifytesting@gmail.com
135

136
00:11:25,330 --> 00:11:30,850
and I'm just going to show you by logging in that the e-mail account has been made or not.
136

137
00:11:32,890 --> 00:11:38,570
So I'm going to take this e-mail address hacktifytesting@gmail.com.
137

138
00:11:39,970 --> 00:11:48,280
I will go onto the website click on log in and I will just type hacktifytesting@gmail.com
138

139
00:11:48,280 --> 00:11:53,500
and continue this to verify that the e-mail account has been made or not
139

140
00:11:56,610 --> 00:11:59,370
as you can see it is asking me for a password.
140

141
00:11:59,370 --> 00:12:02,130
I will just give the right password and I will click log in
141

142
00:12:07,530 --> 00:12:11,290
so you have successfully logged in into this website.
142

143
00:12:11,310 --> 00:12:14,790
Let me just go to my settings and check that my details are there.
143

144
00:12:15,330 --> 00:12:16,140
Yes.
144

145
00:12:16,140 --> 00:12:22,020
So my details are there which means I was able to successfully make the account onto this website by
145

146
00:12:22,020 --> 00:12:25,140
exploiting No-Rate limit on account creation
146

147
00:12:27,940 --> 00:12:28,400
thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,530 --> 00:00:08,030
Hello, everyone, and I hope you are doing good, so in this video, I'm going to tell you a Burp
1

2
00:00:08,160 --> 00:00:14,430
alternative of Intruder tab, which is OWASP zap proxy.
2

3
00:00:14,910 --> 00:00:23,190
So the ZAP proxy is, again, a very, very awesome open source tool, which can be used as an alternative
3

4
00:00:23,190 --> 00:00:24,000
to Burp Suite.
4

5
00:00:24,990 --> 00:00:30,450
I have used the ZAP proxy for about a year and I totally love that tool.
5

6
00:00:31,350 --> 00:00:33,500
I've been using Burp since many years.
6

7
00:00:33,540 --> 00:00:38,220
That's why I am much more comfortable with the environment of Burp Suit.
7

8
00:00:38,640 --> 00:00:41,910
That's why I have included Burp Suite in most of the videos.
8

9
00:00:42,840 --> 00:00:49,470
But you are free to use the ZAP proxy because it is exactly the same and it works exactly the same.
9

10
00:00:49,470 --> 00:00:50,040
Like Burp.
10

11
00:00:51,110 --> 00:00:59,450
Now, there is a procedure in Bob into the intruder tab, which is the throttle request, so in case
11

12
00:00:59,450 --> 00:01:06,320
when we are doing Nor rate limit type of attack at that particular time, you may come across a feature,
12

13
00:01:06,320 --> 00:01:14,000
which is throttle, which basically means to delay the request and into the BURP community additions.
13

14
00:01:14,000 --> 00:01:16,500
That feature is not enabled for free.
14

15
00:01:17,360 --> 00:01:24,070
Now, for those students who have Burp, professional motion can easily go ahead.
15

16
00:01:24,770 --> 00:01:33,230
But for those who do not have, Burp Pro can not go ahead with the throttle option because it is disabled
16

17
00:01:33,230 --> 00:01:35,150
in the community free admission.
17

18
00:01:35,780 --> 00:01:42,260
So at that particular point of time, you can use OWASP Zap proxy to do that attack.
18

19
00:01:43,430 --> 00:01:51,450
Which I have shown in the last video of this particular section, which is burp alternative, OWASP
19

20
00:01:51,470 --> 00:01:55,520
Zap proxy intruder tab I hope you guys understood.
20

21
00:01:55,670 --> 00:01:56,240
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,710 --> 00:00:03,350
Hello everyone.
1

2
00:00:03,360 --> 00:00:09,530
So in this video we are going to see No-Rate limit leads to account takeover.
2

3
00:00:10,530 --> 00:00:19,560
So we will send X number of simultaneous request to the server and the server will act on each of the
3

4
00:00:19,560 --> 00:00:22,250
request that the client will send.
4

5
00:00:22,620 --> 00:00:31,110
Thus by sending x number of a right OTP tokens or password we can successfully crack the code and
5

6
00:00:31,110 --> 00:00:40,530
bypass the authentication no validation or limiting the request and taking decisions by the server is
6

7
00:00:40,530 --> 00:00:42,780
very very dangerous.
7

8
00:00:42,840 --> 00:00:51,540
So we are going to exploit this onto a live Web site where we are going to learn about how we can utilize
8

9
00:00:52,080 --> 00:01:01,540
No-Rate limit functionality and we are able to do an account takeover so practical time.
9

10
00:01:01,590 --> 00:01:06,670
And let's see the practical for this attack.
10

11
00:01:07,830 --> 00:01:17,460
As you can see I am onto a website netmeds.com and on this Web site and going to sign up using
11

12
00:01:17,460 --> 00:01:18,270
my phone number
12

13
00:01:23,920 --> 00:01:26,530
as you can see I gave my phone number.
13

14
00:01:26,530 --> 00:01:32,080
And now this application has sended an OTP onto my mobile number
14

15
00:01:35,180 --> 00:01:35,580
OK.
15

16
00:01:35,610 --> 00:01:37,390
Let me try again.
16

17
00:01:37,470 --> 00:01:41,360
Let me give my phone number once more.
17

18
00:01:41,670 --> 00:01:42,290
So this.
18

19
00:01:42,630 --> 00:01:48,900
This application allows us to log in using a password or OTP so I am choosing OTP option.
19

20
00:01:49,350 --> 00:01:57,320
And now it has successfully sent a OTP onto my phone this time I'm going to give a wrong OTP and I'm
20

21
00:01:57,330 --> 00:02:02,670
going to click on verify and I'm going to capture the request into burpsuit
21

22
00:02:05,790 --> 00:02:13,920
as you can see this is a request that is going to the server which contains the mobile number as well
22

23
00:02:13,920 --> 00:02:15,180
as the OTP code.
23

24
00:02:15,240 --> 00:02:18,940
That is 123456
24

25
00:02:19,110 --> 00:02:21,180
I want to see the response of this request.
25

26
00:02:21,330 --> 00:02:28,040
So I will click on action do intercept and response to this request.
26

27
00:02:28,140 --> 00:02:35,130
I will also send this request to intruder because we are going to perform a No-Rate limit attack onto
27

28
00:02:35,130 --> 00:02:35,520
this
28

29
00:02:39,390 --> 00:02:46,440
now I will just forward this request and if you observe the response and the response you can see the
29

30
00:02:46,440 --> 00:02:48,960
status is failed.
30

31
00:02:48,960 --> 00:02:51,650
The reason is invalid OTP.
31

32
00:02:51,870 --> 00:03:01,140
Yes because the OTP that we gave for the verification purposes was wrong.
32

33
00:03:01,260 --> 00:03:05,300
Now i will do intercept off go into the intruder tab.
33

34
00:03:06,990 --> 00:03:12,150
Now I'm going to set a position where I will brute force the OTP's.
34

35
00:03:13,830 --> 00:03:17,670
So I will just go into the payload option and choose numbers.
35

36
00:03:19,500 --> 00:03:21,180
So I have got to OTP.
36

37
00:03:21,240 --> 00:03:28,790
So I will set a range for that would you be for 25 or OTP's your guys.
37

38
00:03:28,790 --> 00:03:33,650
You have to notice that we have to prove the flaw of No-Rate limit.
38

39
00:03:33,720 --> 00:03:36,780
That's why we are choosing a number 25.
39

40
00:03:36,830 --> 00:03:45,110
We are going to submit 25 OTP's to the application and we are going to observe that the application blocks
40

41
00:03:45,230 --> 00:03:49,000
after these many numbers of attempts.
41

42
00:03:49,040 --> 00:03:55,900
So basically 15 to 20 attempts are more than enough to test a functionality of application.
42

43
00:03:56,030 --> 00:04:05,270
If the application is blocking us or not for verification purposes for our OTP you can just send around
43

44
00:04:05,270 --> 00:04:10,110
25 to 30 or OTP's to test if there is a flaw.
44

45
00:04:10,130 --> 00:04:17,150
I also tested this one ability by submitting 500 or OTP and the application did not block me at all
45

46
00:04:18,950 --> 00:04:21,280
for the video not to make it very long.
46

47
00:04:21,290 --> 00:04:27,020
I'm just going to take 25 OTP's and I'm going to submit that.
47

48
00:04:27,590 --> 00:04:34,820
So in the from range I'm going to put from where the OTP should start and tell you how many or the
48

49
00:04:34,820 --> 00:04:41,930
OTP's it should end . step means how many step of OTP you want to give.
49

50
00:04:41,930 --> 00:04:52,810
So for example the OTP will start from 901825 and the next OTP will be 901826 and so on till
50

51
00:04:52,880 --> 00:04:53,330
50
51

52
00:04:59,570 --> 00:05:06,180
I will just turn off the payload encoding go in the options tab and here you can see there is an option
52

53
00:05:06,430 --> 00:05:09,900
in the request engine that is throttle throttle.
53

54
00:05:09,900 --> 00:05:18,300
Basically means giving time delay between simultaneous request to each request is taking the OTP to
54

55
00:05:18,300 --> 00:05:24,190
the server but here we want to give a throttle between each request.
55

56
00:05:24,200 --> 00:05:24,700
Why.
56

57
00:05:25,740 --> 00:05:33,510
Because we do not want the server to think like someone is doing a DOS or DDOS attack by sending simultaneous
57

58
00:05:33,510 --> 00:05:43,870
request so we're going to give a throttle of three seconds between each seconds each request that is
58

59
00:05:43,870 --> 00:05:45,280
3000 milliseconds
59

60
00:05:48,440 --> 00:05:49,090
now.
60

61
00:05:49,250 --> 00:05:54,420
How will we know that the OTP that has been brute forced is the right one.
61

62
00:05:54,800 --> 00:05:59,390
For that we are going to use the option of greb match.
62

63
00:05:59,390 --> 00:06:03,560
So I will clear on this.
63

64
00:06:03,560 --> 00:06:11,090
I will go onto the website and I will see that whenever a person gives the invalid OTP the application
64

65
00:06:11,100 --> 00:06:13,000
says invalid OTP.
65

66
00:06:13,280 --> 00:06:16,790
But on the right OTP it will not say invalid OTP.
66

67
00:06:16,880 --> 00:06:20,470
It is obviously going to say something else.
67

68
00:06:21,050 --> 00:06:26,360
For this reason we are going to copy this and we are going to match this with all the response that
68

69
00:06:26,360 --> 00:06:31,040
we are getting by brute forcing all the applications into the No-Rate limit attack
69

70
00:06:33,990 --> 00:06:38,310
so I'm just going to paste it here click on Add and start to attack
70

71
00:06:42,640 --> 00:06:54,880
as you can see the request first request is matching invalid OTP into the response even the second third
71

72
00:06:55,060 --> 00:07:04,000
fourth fifth simultaneously all the OTP are matching invalid OTP text into their response which means
72

73
00:07:04,630 --> 00:07:14,110
this is the wrong would be we are going to wait for OTP which will not match this into its response.
73

74
00:07:14,110 --> 00:07:18,490
Also you can observe the status of each request as 400
74

75
00:07:21,280 --> 00:07:31,240
which is a bad request as you can see invalid OTP for each OTP's.
75

76
00:07:31,860 --> 00:07:38,340
Let me just scroll down and let us see.
76

77
00:07:38,640 --> 00:07:39,420
Yes.
77

78
00:07:39,600 --> 00:07:45,280
So there is a OTP which has missed invalid OTP flag right.
78

79
00:07:45,300 --> 00:07:55,890
So let's just go to that OTP and see the response in the status it is seeing success which means this
79

80
00:07:55,890 --> 00:08:02,340
is the right OTP that we have brute forced using the No-Rate limit attack when the attacker is able to
80

81
00:08:02,340 --> 00:08:04,800
brute force a lot of OTP's.
81

82
00:08:05,670 --> 00:08:16,080
So I'm just going to put that OTP in right now 9 0 1 8 4 1 and I'm going to click on verify and this
82

83
00:08:16,140 --> 00:08:17,930
application did not verify me.
83

84
00:08:17,980 --> 00:08:18,710
Why.
84

85
00:08:18,870 --> 00:08:24,550
Because the application has put a logic of 1 OTP only once.
85

86
00:08:24,630 --> 00:08:27,830
So one OTP can only be used once.
86

87
00:08:27,930 --> 00:08:29,340
No problem.
87

88
00:08:29,340 --> 00:08:32,520
But I already have the right response for the OTP.
88

89
00:08:32,610 --> 00:08:38,850
So this time I'm going to copy the right response of this OTP and I'm going to paste it into a wrong
89

90
00:08:38,850 --> 00:08:39,870
response.
90

91
00:08:39,930 --> 00:08:41,140
So how to do it.
91

92
00:08:41,190 --> 00:08:44,220
Let's see.
92

93
00:08:44,220 --> 00:08:46,830
I will just copy all this right response.
93

94
00:08:46,920 --> 00:08:58,110
I will give a wrong OTP going Burpsuit go in my proxy intercept on and click on verify after clicking
94

95
00:08:58,110 --> 00:09:05,640
on verify I want to do intercept response to this request as this is wrong OTP we are going to get
95

96
00:09:06,090 --> 00:09:12,810
a wrong response which says invalid OTP I'm just going to select all and replaced by the right response
96

97
00:09:12,810 --> 00:09:21,630
that we copied and I'm going to forward and to intercept off as you can see we have successfully logged
97

98
00:09:21,630 --> 00:09:30,780
in into the application we have successfully bypassed this and used no red No-Rate limit to log in into the
98

99
00:09:30,780 --> 00:09:33,640
application as you can see this is my mobile number.
99

100
00:09:34,200 --> 00:09:42,240
So we identified that our application has put a logic of 1 or OTP only once but has not put any type
100

101
00:09:42,240 --> 00:09:44,490
of No-Rate limit.
101

102
00:09:44,550 --> 00:09:49,450
So there is a vulnerability of No-Rate limit on this website.
102

103
00:09:49,590 --> 00:09:50,760
I hope you guys understood.
103

104
00:09:51,030 --> 00:09:51,960
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,200 --> 00:00:01,980
Hello everyone.
1

2
00:00:02,640 --> 00:00:08,940
So in this video we're going to see No-Rate limit on OTP verify which will lead to an account takeover.
2

3
00:00:09,630 --> 00:00:17,040
So in this video we're going to send X number of simultaneous request to the server and the server is
3

4
00:00:17,040 --> 00:00:21,400
going to act on each of our request that we have sent it.
4

5
00:00:22,500 --> 00:00:32,640
Thus by sending large number of X request of the OTP token we can successfully guess the right password
5

6
00:00:32,730 --> 00:00:34,320
or token.
6

7
00:00:34,320 --> 00:00:41,950
So here no validation or limiting the request and taking the decisions is very very dangerous.
7

8
00:00:43,290 --> 00:00:46,800
So now it's the practical time and let's see the practical
8

9
00:00:49,430 --> 00:00:56,530
so I'm going to perform this practical on a live Web site which is Limeroad.com on this website I'm
9

10
00:00:56,540 --> 00:01:01,100
going to go quickly and sign in option and I'm going to enter my phone number
10

11
00:01:05,390 --> 00:01:08,110
after I put my phone number and press next.
11

12
00:01:08,120 --> 00:01:13,690
The application is going to send a OTP onto my mobile phone.
12

13
00:01:13,880 --> 00:01:20,880
I have kept OTP that is 1234 which is obviously wrong otp i have captured the request
13

14
00:01:20,880 --> 00:01:26,900
in burpsuit and I have did do intercept response to this request because I went to see the response
14

15
00:01:26,900 --> 00:01:29,510
of this request.
15

16
00:01:29,570 --> 00:01:38,030
Now I will right click and send this request to repeater so I can use it later on I will just do Go
16

17
00:01:38,300 --> 00:01:46,100
and you can see the response of this request is status fail error message Please enter the correct OTP
17

18
00:01:46,730 --> 00:01:48,520
because this was the wrong OTP.
18

19
00:01:48,530 --> 00:01:49,810
1234 is wrong.
19

20
00:01:55,030 --> 00:01:56,100
Yes.
20

21
00:01:56,350 --> 00:02:04,060
So I have come to know that this is the wrong OTP but I have captured that request of verification
21

22
00:02:08,210 --> 00:02:11,570
so it is not in my intruder tab.
22

23
00:02:11,570 --> 00:02:11,830
OK.
23

24
00:02:11,840 --> 00:02:16,870
So I'm going to send this request again to the intruder tab I will just going intruder
24

25
00:02:16,940 --> 00:02:24,800
I will go in positions and I'm going to set a position first I will clear everything click on the OTP
25

26
00:02:24,800 --> 00:02:38,270
value add and then I'm going to choose numbers and I'm going to choose the values of OTP's from
26

27
00:02:38,270 --> 00:02:41,060
6 5 4 5 to 6 5 6 0
27

28
00:02:43,850 --> 00:02:47,820
for proving this vulnerability
28

29
00:02:48,230 --> 00:02:53,800
I'm going to test 16 OTP values.
29

30
00:02:53,810 --> 00:02:58,690
I will just go in option tab and put some throttle in between.
30

31
00:02:58,850 --> 00:03:06,380
So the server does not think that this is a DDOS attack happening or the IDS/IPS do not start alerting
31

32
00:03:06,380 --> 00:03:06,980
the admin
32

33
00:03:10,180 --> 00:03:16,450
I will just go down in grep match and I'm going to clear everything first and I'm going to add this
33

34
00:03:16,570 --> 00:03:19,630
please enter correct OTP into the grep match field
34

35
00:03:24,800 --> 00:03:29,570
after adding this successfully I will start the attack.
35

36
00:03:29,570 --> 00:03:37,670
As you can see the first request which contains the OTP 6 5 4 5 has matched this response which means
36

37
00:03:37,820 --> 00:03:44,820
this is the wrong OTP and the response you can see it is please enter the correct OTP.
37

38
00:03:44,870 --> 00:03:47,170
It is matching this which means this is wrong.
38

39
00:03:49,510 --> 00:03:52,660
So now we are going to wait for the right OTP to appear here.
39

40
00:03:58,120 --> 00:04:03,850
Again for this application I tested with 500 OTP's and it was working fine.
40

41
00:04:03,850 --> 00:04:07,090
The application did not perform any type of No-Rate limit
41

42
00:04:11,240 --> 00:04:12,510
as you can see.
42

43
00:04:12,830 --> 00:04:20,230
We have already found out OTP which is missing this please enter correct OTP value.
43

44
00:04:22,100 --> 00:04:27,680
As you can see in the response it is guessed false and some cookies has been generated.
44

45
00:04:27,680 --> 00:04:38,230
So I am going to use this OTP that is 6 5 5 7 onto the website and I'm going to hit verify as you
45

46
00:04:38,230 --> 00:04:42,900
can see I have successfully logged in into the application.
46

47
00:04:43,630 --> 00:04:51,340
So here we came to know the application is vulnerable to no rate limit attack on OTP as well as the application
47

48
00:04:51,400 --> 00:04:54,200
allowed the same OTP twice.
48

49
00:04:54,460 --> 00:05:01,300
Our intruder tested the OTP once we again reused the OTP to log in which means the application
49

50
00:05:01,300 --> 00:05:06,910
allows simultaneous times logging with the same OTP.
50

51
00:05:06,910 --> 00:05:13,060
Let me just go to my profile section to verify that I am logged in into the application
51

52
00:05:19,860 --> 00:05:21,840
as you can see this is my profile.
52

53
00:05:21,840 --> 00:05:25,350
Let me just go to settings and click on edit profile.
53

54
00:05:25,350 --> 00:05:28,380
This is my phone number.
54

55
00:05:28,650 --> 00:05:32,150
I hope you guys understood how to perform this attack.
55

56
00:05:32,160 --> 00:05:32,660
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,050 --> 00:00:02,400
Hello everyone.
1

2
00:00:02,400 --> 00:00:10,250
So in this video we are going to see a No-Rate limit attack onto a live website in this website.
2

3
00:00:10,290 --> 00:00:17,400
There was a vulnerability wherein I was able to perform brute force of OTP's and the application
3

4
00:00:17,400 --> 00:00:22,740
did not validate X number of attempts onto the OTP verification flaw.
4

5
00:00:24,330 --> 00:00:27,180
So this Web site is vulnerable to No-Rate limit.
5

6
00:00:27,180 --> 00:00:28,830
And let's see.
6

7
00:00:29,190 --> 00:00:33,420
So for instance I have sent it already.
7

8
00:00:33,420 --> 00:00:41,010
The verification request into my burpsuit and I have sent it that into the intruder tab I have set
8

9
00:00:41,010 --> 00:00:46,050
the position of the OTP and now I'm into the payload tab.
9

10
00:00:46,590 --> 00:00:54,400
I'm just going to set the payload from 1 1 6 4 0 1 to 1 1 6 4 2 0.
10

11
00:00:54,540 --> 00:01:03,390
So basically to prove the flaw I'm going to put twenty OTP's I tested on this website with 500 OTP's
11

12
00:01:03,480 --> 00:01:06,050
and it was working fine.
12

13
00:01:06,720 --> 00:01:14,250
I will just go into the options tab and I'm going to give some throttle of six seconds.
13

14
00:01:14,250 --> 00:01:16,800
That is six thousand milliseconds.
14

15
00:01:17,130 --> 00:01:23,580
So the application does not feel its a DDOS happening or IDS/IPS do not start alerting
15

16
00:01:27,560 --> 00:01:32,690
as you can see the first request has been sent.
16

17
00:01:33,250 --> 00:01:41,230
The second request has been sent you can notice here between both the request the length that has come
17

18
00:01:41,350 --> 00:01:43,720
is exactly the same.
18

19
00:01:43,720 --> 00:01:51,490
We have got the state as good as 200 but the length is exactly the same for all the wrong or OTP's
19

20
00:01:54,250 --> 00:02:09,200
so let's wait for a request which shows a different length.
20

21
00:02:09,850 --> 00:02:19,990
We have kept a throttle of six seconds so each request is going six seconds delayed so there is a six
21

22
00:02:19,990 --> 00:02:22,690
second delay between every simultaneous request
22

23
00:02:30,490 --> 00:02:38,210
as you can see the status is 200 but the length has changed for some requests as you can see 
23

24
00:02:38,220 --> 00:02:40,070
44883
24

25
00:02:40,600 --> 00:02:49,180
So in this length change that is something changed into the HTML page but if you look closely onto our
25

26
00:02:49,180 --> 00:02:56,950
request we have got a new status called that is 302 which is for the redirect and found.
26

27
00:02:57,520 --> 00:03:06,340
As you can see the length has also changed as well as the status code has always has also changed so
27

28
00:03:08,370 --> 00:03:10,050
what we are going to do right now is
28

29
00:03:15,330 --> 00:03:21,850
I'm just going to go and show you the response as you can see that there is a change in response as well
29

30
00:03:21,850 --> 00:03:23,570
as a change in the status code
30

31
00:03:28,310 --> 00:03:35,780
as we can see verify different change in the length as well as the status code
31

32
00:03:39,310 --> 00:03:40,230
in the response
32

33
00:03:47,980 --> 00:03:55,570
so this basically means that that this OTP worked because of No-Rate limit vulnerability
33

34
00:04:15,830 --> 00:04:26,800
so now I'm just going to go back to the application and reload this.
34

35
00:04:27,330 --> 00:04:30,000
Let me go to the dashboard and verify
35

36
00:04:37,130 --> 00:04:48,570
I'll copy this response and just go to the dashboard first and I will just reload this to verify that
36

37
00:04:48,570 --> 00:04:52,230
the OTP has been successfully activated or not.
37

38
00:04:52,550 --> 00:05:00,650
So yes as you can see I have taken over this phone number and I have successfully performed no rate
38

39
00:05:00,650 --> 00:05:09,040
limit on OTP verification and I am able to take over anyone's phone number on my combell account.
39

40
00:05:09,140 --> 00:05:10,910
I hope you guys understood.
40

41
00:05:10,910 --> 00:05:11,810
Thank you for watching.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,730 --> 00:00:03,440
Hello everyone.
1

2
00:00:03,440 --> 00:00:11,120
So in this video we are going to see one more No rate limit attack onto a very famous website..
2

3
00:00:11,270 --> 00:00:13,280
So this is no broker Web site.
3

4
00:00:13,280 --> 00:00:21,170
And we are going to see how we can bypass the verification process and do a no rate limit attack onto
4

5
00:00:21,170 --> 00:00:22,730
this Web site.
5

6
00:00:23,300 --> 00:00:28,030
So I'm going to go into the log in and sign up and I'm going to logging into my phone number.
6

7
00:00:29,930 --> 00:00:35,450
So I am just giving my phone number because I want to log in into my account.
7

8
00:00:35,450 --> 00:00:43,570
So I have given my phone number and you can see the application has sended an OTP onto my mobile phone
8

9
00:00:48,340 --> 00:00:55,750
so here for example I'm willing to give OTP that is 0 0 0 0 and I'm going to hit continue and capture
9

10
00:00:55,780 --> 00:01:01,280
the request and Burpsuit as you can see I've captured the request in Burpsuit.
10

11
00:01:01,320 --> 00:01:07,700
Now I'm going to send this request to the intruder tab before sending this to intruder.
11

12
00:01:07,690 --> 00:01:14,350
I'm going to do action do intercept response to this request because I want to see what is the response
12

13
00:01:14,560 --> 00:01:16,330
of a wrong OTP
13

14
00:01:28,910 --> 00:01:29,510
okay.
14

15
00:01:29,610 --> 00:01:32,720
So the response is incorrect OTP.
15

16
00:01:32,790 --> 00:01:33,330
All right
16

17
00:01:40,840 --> 00:01:46,660
so I will just go to the intruder type in the target section you can see my target is nobroken.in
17

18
00:01:46,730 --> 00:01:51,430
And and just go to the position tab clear all the positions.
18

19
00:01:51,490 --> 00:02:01,720
Select the OTP position click Add now go into the payload and choose numbers in the payload options.
19

20
00:02:01,750 --> 00:02:15,040
I'm going to start from where my OTP should start and untill where the OTP should end.
20

21
00:02:15,390 --> 00:02:23,820
Now I will go to the option tab and going to greb what we were able to see onto the website that
21

22
00:02:23,820 --> 00:02:25,080
is incorrect OTP.
22

23
00:02:25,090 --> 00:02:27,210
So I'm willing to greb this incorrect
23

24
00:02:30,500 --> 00:02:31,060
OTP
24

25
00:02:37,170 --> 00:02:38,030
yes.
25

26
00:02:38,070 --> 00:02:39,990
So now I have added this
26

27
00:02:47,220 --> 00:02:55,050
I have also added some throttle into this request which is nothing but time delay between each simultaneous
27

28
00:02:55,050 --> 00:02:56,690
request.
28

29
00:02:57,090 --> 00:03:03,860
As you can see these two OTP's are wrong OTP's as the response is matching incorrect OTP .
29

30
00:03:03,870 --> 00:03:04,440
Text
30

31
00:03:27,480 --> 00:03:34,290
so I am able to brute force all theOTP's and the application is still running.
31

32
00:03:34,300 --> 00:03:40,400
The application has not blocked me which means I am able to successfully send a large number of 
32

33
00:03:40,400 --> 00:03:42,020
OTP's
33

34
00:03:42,550 --> 00:03:48,170
As you can observe on the screen there is some change that is happening.
34

35
00:03:48,940 --> 00:04:00,250
If you see a OTP that is 3 1 8 2 in which there is no tick which means it is not matching the incorrect
35

36
00:04:00,340 --> 00:04:03,820
OTP into its response.
36

37
00:04:04,500 --> 00:04:11,980
So I will just click on it and again just see 3 1 8 2 is OTP in the response.
37

38
00:04:11,980 --> 00:04:18,310
You can see it as giving the message that is successful and it is giving my details
38

39
00:04:23,560 --> 00:04:24,120
yes.
39

40
00:04:24,170 --> 00:04:29,510
So what I'm going to do is I'm just going to copy all the right response from here
40

41
00:04:35,750 --> 00:04:37,360
I'm going to hit the wrong OTP
41

42
00:04:40,440 --> 00:04:47,760
click on action do intercept response to this request and you can see incorrect OTP and we need to replace
42

43
00:04:47,760 --> 00:04:55,080
this with the right response that we have received and I will just wait for the application to reload
43

44
00:04:56,220 --> 00:05:04,230
and yes you can see I have successfully logged in into my account I will just go on my profile to show
44

45
00:05:04,260 --> 00:05:06,440
I am successfully logged in into the account
45

46
00:05:15,730 --> 00:05:23,230
and yes you can see this is when profile my email address my mobile phone number so I hope you guys
46

47
00:05:23,230 --> 00:05:24,110
understood.
47

48
00:05:24,130 --> 00:05:25,020
Thank you for watching.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,200 --> 00:00:02,540
Hello everyone.
1

2
00:00:02,550 --> 00:00:11,220
So in this video we are going to see a No-Rate limit on sign up on this website as well as we are going
2

3
00:00:11,220 --> 00:00:16,330
to see a No-Rate limit on login onto this Web site.
3

4
00:00:16,410 --> 00:00:23,310
So yes I will just go to the sign up page and I'm going to fill all the details.
4

5
00:00:23,460 --> 00:00:26,070
So let me just put in the first name field.
5

6
00:00:26,070 --> 00:00:31,080
My name and the last name field the surname in the e-mail address.
6

7
00:00:31,100 --> 00:00:33,170
I'm going to give her e-mail address.
7

8
00:00:33,330 --> 00:00:39,330
That is the thesrsecure@gmail.com in the password field.
8

9
00:00:39,330 --> 00:00:41,040
I'm going to give a password
9

10
00:00:47,540 --> 00:00:53,280
in the phone number field and I'm going to give my phone number I will just
10

11
00:00:56,160 --> 00:01:01,880
hit on sign up and it is saying me mobile number is already registered so I'm going to use my another
11

12
00:01:01,890 --> 00:01:02,640
mobile number
12

13
00:01:13,440 --> 00:01:13,860
okay.
13

14
00:01:13,880 --> 00:01:15,900
So this number is also registered.
14

15
00:01:15,980 --> 00:01:18,640
So I'm going to use my other phone number
15

16
00:01:33,490 --> 00:01:33,970
yes.
16

17
00:01:34,180 --> 00:01:44,740
So this phone number was not used and yes the web application has sended a OTP code and I'm going to
17

18
00:01:46,210 --> 00:01:48,660
give OTP that is 1 1 1 1.
18

19
00:01:48,850 --> 00:01:56,590
And you can see this is the OTP which is going I'm going to intercept the response of this request
19

20
00:01:57,070 --> 00:01:59,530
and I'm going to send this to intruder.
20

21
00:02:01,090 --> 00:02:05,060
So I've sended this to an intruder tab first.
21

22
00:02:05,240 --> 00:02:06,880
Let's see in the repeater.
22

23
00:02:06,880 --> 00:02:08,710
What response do we get.
23

24
00:02:08,710 --> 00:02:13,810
As you can see Please enter a valid OTP because this is a wrong OTP.
24

25
00:02:13,810 --> 00:02:14,440
We know that
25

26
00:02:21,140 --> 00:02:29,520
so I'll go to the intruder tab in the position tabs I'm going to select the position for OTP code.
26

27
00:02:29,840 --> 00:02:31,120
So this is my position.
27

28
00:02:31,130 --> 00:02:38,060
I will click on add now I will go in the payload options and I'm going to choose numbers
28

29
00:02:42,400 --> 00:03:00,450
I'm willing to choose from number and to number.
29

30
00:03:00,690 --> 00:03:05,420
So as you can see I have given 44 2 0 till 4 4 6 0.
30

31
00:03:05,430 --> 00:03:10,670
Basically I'm giving 40 OTP's to test.
31

32
00:03:11,820 --> 00:03:13,650
Now I'll go into the options tab
32

33
00:03:16,500 --> 00:03:25,260
so I'm going to give some throttle of let's say five seconds I'll quickly go in greb match and clear
33

34
00:03:25,260 --> 00:03:32,610
the list and I'm going to put here which is Please enter a valid OTP and I'm going to hit add
34

35
00:03:40,710 --> 00:03:42,300
I have started the attack
35

36
00:03:46,150 --> 00:03:49,300
and let's let us wait.
36

37
00:03:49,530 --> 00:03:53,520
As you can see in the first OTP response it is showing.
37

38
00:03:53,520 --> 00:03:57,980
Please enter a valid OTP which means this is not the right OTP.
38

39
00:03:57,990 --> 00:03:59,430
It is the wrong one
39

40
00:04:03,990 --> 00:04:09,040
as you can see the four OTP's that we have tested are all wrong.
40

41
00:04:09,060 --> 00:04:12,800
Please enter a valid OTP text is matching into the response
41

42
00:04:25,140 --> 00:04:33,470
there is a time delay of five seconds between each request because of the throttle that we added from
42

43
00:04:33,470 --> 00:04:35,350
the request engine.
43

44
00:04:35,480 --> 00:04:39,290
We are just waiting for the right OTP to get brute forced
44

45
00:04:55,160 --> 00:04:57,230
I will just scroll down to check
45

46
00:05:22,440 --> 00:05:25,740
so we are still waiting for the right OTP to crack.
46

47
00:05:34,260 --> 00:05:45,120
And as you can see on to this 4 4 4 0 you can see it is not matching this text which is Please enter
47

48
00:05:45,120 --> 00:05:48,790
a valid OTP and onto the response at the bottom.
48

49
00:05:48,810 --> 00:05:55,830
You can see success=1 your account has been created successfully.
49

50
00:05:55,830 --> 00:05:56,480
Perfect.
50

51
00:05:56,550 --> 00:05:59,070
So you are able to bypass this
51

52
00:06:02,120 --> 00:06:04,480
and we have successfully created an account
52

53
00:06:28,660 --> 00:06:34,850
so I've put that OTP again and you can see success your account has been created.
53

54
00:06:34,860 --> 00:06:41,840
I'm inside this account as you can see this is my profile that I've opened.
54

55
00:06:43,420 --> 00:06:48,480
I will just go to the mobile number field and the email field perfect.
55

56
00:06:48,720 --> 00:06:54,220
So as you can see we were able to do an Account takeover through this attack.
56

57
00:06:54,220 --> 00:06:55,390
I hope you guys understood.
57

58
00:06:55,780 --> 00:06:56,260
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,110 --> 00:00:02,810
Hello everyone.
1

2
00:00:02,820 --> 00:00:09,140
So in this video we are again going to see the no-rate limit when vulnerability onto the website.
2

3
00:00:09,480 --> 00:00:13,410
We already saw a sign up bypass that we were able to do.
3

4
00:00:13,410 --> 00:00:20,500
Now we are going to do a login bypass by exploiting the same endpoint.
4

5
00:00:20,610 --> 00:00:23,970
So let's start as you can see.
5

6
00:00:23,970 --> 00:00:26,010
I will go into the login option option
6

7
00:00:29,330 --> 00:00:35,770
and I'm willing to give my phone number to log in.
7

8
00:00:37,200 --> 00:00:39,820
I will just go to the forget password now.
8

9
00:00:40,230 --> 00:00:44,980
I will give the phone number to forget the password and I will click on send OTP.
9

10
00:00:45,420 --> 00:00:53,880
The application will send a OTP onto my phone number but I'm going to give a wrong OTP here and I'm
10

11
00:00:53,880 --> 00:00:59,840
going to send this request to burpsuite.
11

12
00:01:00,670 --> 00:01:11,240
So this is a wrong OTP.
12

13
00:01:11,540 --> 00:01:15,080
Let me just open a burp.
13

14
00:01:16,040 --> 00:01:20,210
We do intercept on goto the application.
14

15
00:01:20,210 --> 00:01:26,310
click on verify I have successfully captured the request in burpsuite.
15

16
00:01:26,510 --> 00:01:31,520
I will send this request to repeater and I will send this request to intruder for brute forcing
16

17
00:01:34,570 --> 00:01:35,980
after going and repeater.
17

18
00:01:35,980 --> 00:01:43,480
I will just send a request and you can observe I have got a response that is please enter a valid OTP
18

19
00:01:43,990 --> 00:01:49,900
so I'm going to copy this response that is please enter a valid OTP and I'm going to perform a grep
19

20
00:01:49,900 --> 00:01:53,440
match I will quickly go to the intruder tab
20

21
00:01:57,160 --> 00:02:04,210
and you can see my target is this website I'll go in position tab and I will select the position of
21

22
00:02:04,210 --> 00:02:05,380
the OTP code1
22

23
00:02:08,380 --> 00:02:16,070
after selecting this position I will click on Add after doing this I will go into the payload section
23

24
00:02:16,370 --> 00:02:18,980
and then the payload type I'm going to choose numbers
24

25
00:02:21,980 --> 00:02:26,900
I'm going to give a range of OTP's in the from and to option
25

26
00:02:37,360 --> 00:02:46,550
so I have given around twenty five OTP's to brute force as you can see in the number format I'm
26

27
00:02:46,570 --> 00:02:55,510
giving minimum integer digits and maximum digits as 4 because OTP is four digits long I will go
27

28
00:02:55,510 --> 00:03:02,430
in the options tab and I'm going to set the throttle to five seconds which is 5000 milliseconds I'll
28

29
00:03:02,470 --> 00:03:09,640
quickly go to the grep match option and add please enter a valid OTP to match this into our
29

30
00:03:10,360 --> 00:03:19,000
responses of the wrong OTP's and I will click on Start To Attack as you can see the attack is starting
30

31
00:03:19,330 --> 00:03:26,440
and there is a significant delay of five seconds between each request all these requests are
31

32
00:03:26,440 --> 00:03:35,500
matching Please enter a valid OTP text which means these are the wrong would be we will wait for the
32

33
00:03:35,500 --> 00:03:38,980
application to brute force the right to OTP and give it to us
33

34
00:04:08,210 --> 00:04:13,190
as you can see all the OTP's has the same response that is please enter a valid OTP
34

35
00:04:36,550 --> 00:04:44,160
the application is still trying for the OTP's and you can see there is one OTP which is missing this
35

36
00:04:44,160 --> 00:04:50,730
text which is please enter a valid OTP as you can see onto the screen I will just double click on that
36

37
00:04:50,760 --> 00:04:58,710
please enter the correct OTP and the OTP which did did not match this text will automatically
37

38
00:04:58,710 --> 00:05:07,440
come up as you can see the right otp i can see is 9 7 6 3 so I'm going to try using this OTP
38

39
00:05:17,600 --> 00:05:19,990
and then I'm going to login through this OTP
39

40
00:05:37,560 --> 00:05:43,940
I will just go to the application back again and I'm going to put the right OTP that I guessed from
40

41
00:05:43,940 --> 00:05:54,890
the intruder tab OTP was 9 7 6 3 I will click on verify and wait for the application and yes I
41

42
00:05:54,890 --> 00:06:01,100
am inside the application I will just go to my account to show you the details of my account and yes
42

43
00:06:02,180 --> 00:06:08,450
I have successfully bypassed the OTP verification process for this website I hope you guys
43

44
00:06:08,450 --> 00:06:09,030
understood.
44

45
00:06:09,050 --> 00:06:09,490
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,030 --> 00:00:01,520
Hello everyone.
1

2
00:00:01,560 --> 00:00:06,180
This is No-Rate limit protection bypass number one in this video.
2

3
00:00:06,190 --> 00:00:12,150
We're going to see how we can achieve a rate limit production bypass.
3

4
00:00:12,420 --> 00:00:19,770
So we will send X number of simultaneous request to the server and the server will act on each request.
4

5
00:00:19,770 --> 00:00:24,510
We will do the bypass for No-Rate limit using race conditions and IP address.
5

6
00:00:24,750 --> 00:00:31,980
Thus by sending x number of right or OTP tokens and password we can successfully cracked the code.
6

7
00:00:32,010 --> 00:00:37,500
No validation or limiting the request and taking decisions is very very dangerous.
7

8
00:00:37,500 --> 00:00:41,200
The best example for this attack is Instagram.
8

9
00:00:41,790 --> 00:00:49,110
So let's see of a vulnerability that was found out by a security researcher on Instagram wherein he was able
9

10
00:00:49,110 --> 00:00:54,840
to bypass no rate limit protection and was awarded with thirty thousand dollars bounty.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,500 --> 00:00:02,780
Hello everyone.
1

2
00:00:02,850 --> 00:00:09,120
So this is a very interesting attack that happened on Instagram.
2

3
00:00:09,180 --> 00:00:16,560
So there was an Indian security researcher who was able to hack any Instagram account using no rate
3

4
00:00:16,560 --> 00:00:17,010
limit.
4

5
00:00:17,310 --> 00:00:21,380
So let's see this report how the user was able to do so.
5

6
00:00:21,690 --> 00:00:29,590
And yes Facebook awarded dollars 30000 as a part of their bug bounty program to the security researcher.
6

7
00:00:29,640 --> 00:00:37,890
So this was a very interesting bypass that the researcher was able to perform so that the researcher
7

8
00:00:38,400 --> 00:00:40,830
was testing for a forgot password endpoint.
8

9
00:00:40,860 --> 00:00:44,660
And the first thing that came to mind was aaccount takeover  vulnerability.
9

10
00:00:44,670 --> 00:00:45,800
Yes.
10

11
00:00:45,810 --> 00:00:54,150
So the user tries to enter his or her mobile number that sends a six digit passcode onto their mobile
11

12
00:00:54,150 --> 00:00:55,000
phone.
12

13
00:00:55,020 --> 00:00:59,350
Now they have to enter it to change the password now.
13

14
00:00:59,400 --> 00:01:04,280
So he was testing to show the presence of rate limiting.
14

15
00:01:04,290 --> 00:01:11,290
So he sent it around 1000 request 250 requests went through and rest 750 requests were rate limited
15

16
00:01:11,850 --> 00:01:12,690
tried.
16

17
00:01:12,810 --> 00:01:14,760
One more time 1000 request.
17

18
00:01:14,820 --> 00:01:16,710
But they also got rate limited.
18

19
00:01:16,710 --> 00:01:21,120
So the systems are validating the rate limit requests properly.
19

20
00:01:21,150 --> 00:01:28,750
So what this user tried he tried for two things that allowed to bypass the rate limit mechanism
20

21
00:01:28,770 --> 00:01:29,290
Race Hazard.
21

22
00:01:29,490 --> 00:01:30,040
That's it.
22

23
00:01:30,090 --> 00:01:32,250
There is nothing but race conditions.
23

24
00:01:32,700 --> 00:01:43,230
And second this IP rotation. Race condition means when any user is able to send a lot of high number
24

25
00:01:43,230 --> 00:01:47,070
of request in a very small time frame.
25

26
00:01:47,420 --> 00:01:51,850
We will see how can we do these conditions using Burpsuite.
26

27
00:01:51,870 --> 00:01:56,680
You just have to go into the intruder tab and then you have to increase that threads.
27

28
00:01:56,790 --> 00:02:02,750
So let's say you can give around 100 to 200 threads and you can fire the request.
28

29
00:02:02,820 --> 00:02:11,250
OK IP rotation IP rotation is nothing but it's just it's with each request you are able to send a new
29

30
00:02:11,340 --> 00:02:17,490
IP address to the server so the server will think that request is not just coming from one computer
30

31
00:02:17,550 --> 00:02:18,690
or one user.
31

32
00:02:18,900 --> 00:02:24,060
The request is coming from many other users and many other computers from the world.
32

33
00:02:24,120 --> 00:02:32,970
So this two things helped the researcher to bypass the rate limit process and Instagram and he was awarded
33

34
00:02:33,240 --> 00:02:35,880
with bounty 30000 U.S. dollars.
34

35
00:02:37,500 --> 00:02:43,590
So it's a very nice article which has written wherein he was able to bypass this as you can see this
35

36
00:02:43,590 --> 00:02:46,970
is the POC in which this is the post request.
36

37
00:02:47,010 --> 00:02:47,390
OK.
37

38
00:02:47,430 --> 00:02:56,460
In the post request he have got a verification code onto his phone and this is the verification request
38

39
00:02:56,520 --> 00:03:00,930
which contains the recovery code 123456.
39

40
00:03:00,960 --> 00:03:05,440
Now we need to brute force this end point using multiple IP's for that.
40

41
00:03:05,790 --> 00:03:12,030
He used many IP's through aws he was able to send around 200 request from a single
41

42
00:03:12,030 --> 00:03:13,800
IP without hitting the rate limit.
42

43
00:03:14,430 --> 00:03:20,850
So for this demonstration he used around 1000 different machines to achieve concurrency and APIs to
43

44
00:03:20,850 --> 00:03:29,310
send around 200k request and Facebook quickly had acknowledge of this issue and they awarded thirty
44

45
00:03:29,350 --> 00:03:32,340
thousand dollars for this awesome find.
45

46
00:03:33,530 --> 00:03:35,050
So I hope you guys understood.
46

47
00:03:35,070 --> 00:03:40,410
I will put the link in the description where you can watch this POC how this user was able to do
47

48
00:03:40,410 --> 00:03:41,730
the same thing.
48

49
00:03:41,850 --> 00:03:51,450
Lesson learned into this vulnerability report was you can still bypass than the rate limit by two things.
49

50
00:03:51,510 --> 00:03:58,500
The first thing is a race condition by sending very fast request in a very small time frame through
50

51
00:03:58,590 --> 00:04:01,530
intruder tab by increasing the threads.
51

52
00:04:01,650 --> 00:04:06,670
Second IP rotation if you can change your IP with each request.
52

53
00:04:06,690 --> 00:04:11,750
You can also achieve no rate limit on to websites.
53

54
00:04:11,760 --> 00:04:12,880
I hope you guys understood.
54

55
00:04:13,290 --> 00:04:14,130
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,440 --> 00:00:03,110
Hello everyone.
1

2
00:00:03,180 --> 00:00:13,200
So we are going to see a report in which a security researcher was able to bypass a rate limit it was
2

3
00:00:13,200 --> 00:00:16,530
a very interesting vulnerability that was reported.
3

4
00:00:16,530 --> 00:00:22,800
That's why we are going to understand this and we are going to break down and see how the researcher
4

5
00:00:23,220 --> 00:00:27,250
was able to achieve this rate limit bypass.
5

6
00:00:27,420 --> 00:00:35,370
So as you can see here the researcher sended a lot of requests to user_sign_in and the
6

7
00:00:35,370 --> 00:00:39,880
application rate limited saying too many requests.
7

8
00:00:40,290 --> 00:00:48,700
Later on the researcher found out a way by adding a null byte as you can see he just added another byte.
8

9
00:00:48,720 --> 00:00:50,690
That is %00.
9

10
00:00:50,700 --> 00:00:58,740
And he added this into the e-mail field in the e-mail field as he added into the e-mail field.
10

11
00:00:58,890 --> 00:01:02,830
As you can see over here null byte is added in the e-mail.
11

12
00:01:02,970 --> 00:01:13,530
And when he keeps adding this he was able to bypass this and he continuously got e-mails from hackerone
12

13
00:01:13,530 --> 00:01:17,400
for reset password instruction.
13

14
00:01:17,400 --> 00:01:18,430
Yes.
14

15
00:01:18,600 --> 00:01:25,260
So he said I thought it was worth reporting this because the rate limit bypass might exist in other
15

16
00:01:25,260 --> 00:01:25,960
areas.
16

17
00:01:26,160 --> 00:01:35,160
But with the use of null byte he was able to bypass this the staff quickly made it to not applicable
17

18
00:01:35,220 --> 00:01:42,450
as it thought that automated e-mails spamming is out of scope but this vulnerability was something else
18

19
00:01:43,620 --> 00:01:49,470
as the researcher again explained that by using a null byte he can bypass the rate limit.
19

20
00:01:49,470 --> 00:01:57,270
And this was indeed an issue apart from spamming e-mails.
20

21
00:01:58,080 --> 00:02:02,690
They say it makes sense and they were able to reproduce that issue.
21

22
00:02:02,810 --> 00:02:06,090
Now the researcher
22

23
00:02:09,300 --> 00:02:17,850
was said to again try for this vulnerability as you can see as you can see they have put protection
23

24
00:02:17,850 --> 00:02:21,480
in place that would prevent this issue from occurring.
24

25
00:02:21,480 --> 00:02:26,460
Now the attacker was able to again bypass using this.
25

26
00:02:26,460 --> 00:02:37,050
He was able to add this into the e-mail field and this was basically backspace but he was able to bypass
26

27
00:02:37,050 --> 00:02:37,480
this.
27

28
00:02:37,530 --> 00:02:42,280
So there was no fix that happened actually.
28

29
00:02:42,570 --> 00:02:44,340
Let's go more down.
29

30
00:02:44,340 --> 00:02:48,350
And you can see they fixed this.
30

31
00:02:48,360 --> 00:02:49,440
OK.
31

32
00:02:49,720 --> 00:02:56,990
Now that fixed it they released a patch and they asked Can you try breaking it again.
32

33
00:02:57,270 --> 00:02:59,980
Again this researcher was able to bypass this.
33

34
00:03:00,030 --> 00:03:06,690
So I re-tested and it seems we can still use %09 over and over again to bypass the rate limit
34

35
00:03:07,020 --> 00:03:10,350
as you can see in this is the post request field.
35

36
00:03:10,350 --> 00:03:17,160
And in the e-mail field this is the e-mail field he was able to add 0 9 0 9 0 9 %09
36

37
00:03:17,160 --> 00:03:23,440
%09  %09 through which he was able to again bypass this.
37

38
00:03:23,910 --> 00:03:28,860
As you can see looking at your most recent case adding 0 9 onto the end would not be targeting the
38

39
00:03:29,040 --> 00:03:34,950
of e-mail I.D. but there was again a confusion and it was solved again.
39

40
00:03:34,950 --> 00:03:44,760
As you can bypass the rate limit by appending %09 over and over the team again reproduced the
40

41
00:03:44,790 --> 00:03:51,060
same vulnerability using burpuit and fixed it and now successfully this was fixed.
41

42
00:03:51,660 --> 00:03:54,660
The researcher was awarded with five hundred dollar bounty.
42

43
00:03:55,290 --> 00:04:03,410
So this was a awesome find according to us that this is that this researcher found out in that web application.
43

44
00:04:04,190 --> 00:04:05,540
OK.
44

45
00:04:05,790 --> 00:04:09,580
So what are the lessons learned.
45

46
00:04:09,600 --> 00:04:15,080
We will send X numbers of simultaneous requests to the server and the server will act on each request.
46

47
00:04:15,270 --> 00:04:18,420
We will do bypass for no rate limit using null byte.
47

48
00:04:18,570 --> 00:04:22,380
The first thing that we did was null byte as you can see it.
48

49
00:04:22,380 --> 00:04:28,530
We added the null byte at the end of the e-mail address and keep adding %00 0 every time your rate
49

50
00:04:28,560 --> 00:04:29,060
limited.
50

51
00:04:29,280 --> 00:04:34,440
After a while you can go back to just %09 as it reset after so long.
51

52
00:04:34,470 --> 00:04:37,660
This was the one first method first approach.
52

53
00:04:37,680 --> 00:04:46,800
Second he was able to bypass using %0d %0a and achieve the same results by increasing 
53

54
00:04:46,800 --> 00:04:48,100
%0d %0a
54

55
00:04:48,210 --> 00:04:49,850
When we hit too many request.
55

56
00:04:49,860 --> 00:04:53,220
This was the second bypass third bypass.
56

57
00:04:53,640 --> 00:04:59,540
So I retested and it seems we can still use %09 over and over again  to bypass the rate limit.
57

58
00:04:59,550 --> 00:05:01,560
So no not fixed yet.
58

59
00:05:01,590 --> 00:05:10,350
So in this video the lesson learned is we are able to still bypass the rate limit by adding these types
59

60
00:05:10,350 --> 00:05:18,910
of null byte characters and we can achieve no rate limit on the web applications.
60

61
00:05:19,080 --> 00:05:27,050
So I hope you guys understood the break down of this vulnerability that was reported on hackerone.
61

62
00:05:27,090 --> 00:05:27,590
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,590 --> 00:00:03,030
Hello everyone.
1

2
00:00:03,030 --> 00:00:07,870
So in this video we are going to see how we can achieve No-Rate limit protection bypass.
2

3
00:00:07,890 --> 00:00:09,380
Number two.
3

4
00:00:09,570 --> 00:00:21,300
So in this video we will see how we can bypass No-Rate limit using x forwarded host header into any request.
4

5
00:00:21,300 --> 00:00:29,700
So for this we are going to see a report right now to understand this better of bypassing rate limit
5

6
00:00:29,700 --> 00:00:33,710
protection by spoofing originating IP.
6

7
00:00:34,200 --> 00:00:38,150
So let's see what the user was able to do.
7

8
00:00:38,520 --> 00:00:45,540
The first screenshot They blocked my IP as you can see this user was performing an action in which there
8

9
00:00:45,540 --> 00:00:53,820
is a WAF which is blocking as you can see 403 forbidden now trying to host header injection which means
9

10
00:00:53,910 --> 00:01:02,190
modifying the host from the www.example.com to www.xyz.com
10

11
00:01:02,190 --> 00:01:07,320
adding x forwarded host hacker.com but still no success.
11

12
00:01:07,320 --> 00:01:14,140
Now trying for X forwarded for option to spoof originating IP address.
12

13
00:01:14,190 --> 00:01:22,360
So we are going to give a random IP address in X forwarded for still no success.
13

14
00:01:22,470 --> 00:01:31,770
Now trying with X forwarded for IP header into the request twice two times instead of one thing and
14

15
00:01:31,770 --> 00:01:37,830
you can see we were successfully able to bypass this No-Rate limit protection because the application
15

16
00:01:37,830 --> 00:01:40,740
is giving 200 ok right now.
16

17
00:01:40,860 --> 00:01:49,460
So what is the lesson learned the lesson learned is that you can bypass no rate limit by applying or
17

18
00:01:49,470 --> 00:01:58,950
digital header it like X forwarded for or X forwarded in the request X for x-forwarded host in the request.
18

19
00:01:58,950 --> 00:02:06,660
So let's get back to the presentation and let us No-Rate limit by ad adding some specific headers
19

20
00:02:07,530 --> 00:02:14,070
so you can add headers with the request like x-originating IP and you can give any random IP X
20

21
00:02:14,070 --> 00:02:22,290
forwarded for that we already saw into the report X remote IP, X remote address, x client IP X host and
21

22
00:02:22,380 --> 00:02:29,670
X forwarded host we already saw X forwarded host and X forwarded for through which the user was able to bypass
22

23
00:02:29,670 --> 00:02:30,760
the no rate limit.
23

24
00:02:31,710 --> 00:02:39,840
So this is one of the way in the bypass number two in which you can bypass the no rate limit protection
24

25
00:02:43,010 --> 00:02:49,700
so the first one understood we understood the second one also third is remote IP remote address client
25

26
00:02:49,700 --> 00:02:54,980
IP X host and X forwarded host so practical time.
26

27
00:02:55,130 --> 00:03:00,400
So let's see what we can achieve through this.
27

28
00:03:01,070 --> 00:03:06,970
And I have written a small script to explain this to you guys.
28

29
00:03:06,980 --> 00:03:09,770
So let me just open the script.
29

30
00:03:09,780 --> 00:03:11,300
nano check.py
30

31
00:03:11,930 --> 00:03:20,480
So this is a Python script which basically add these headers the headers that we understood into the
31

32
00:03:20,480 --> 00:03:26,020
slide and sent the request to the specific target you want to send to.
32

33
00:03:26,300 --> 00:03:26,850
Okay.
33

34
00:03:27,050 --> 00:03:34,700
So you have to use like this python check IP domain name.
34

35
00:03:34,730 --> 00:03:36,030
http or https
35

36
00:03:36,080 --> 00:03:37,380
And you have to send the request.
36

37
00:03:37,400 --> 00:03:39,360
So let's see how to use this.
37

38
00:03:39,410 --> 00:03:48,410
I already run it couple of times so you can see from your python check.py www.udemy.com 
38

39
00:03:48,410 --> 00:03:55,280
HTTPS  as you can see for the first header we added the status code was 200 response-size was this.
39

40
00:03:55,310 --> 00:04:03,920
This is nothing but the response length x-forwarded host a response and changed remote IP length change
40

41
00:04:04,250 --> 00:04:12,140
at a remote address length changed client IP length remains the same  X host Length change forwarded host 
41

42
00:04:12,710 --> 00:04:15,020
length remains the same X this one and this one.
42

43
00:04:15,560 --> 00:04:22,820
So basically in this we can see the application that is udemy.com behaves in a different manner
43

44
00:04:23,020 --> 00:04:26,970
when different different headers are been sent.
44

45
00:04:27,050 --> 00:04:33,950
So yeah we can try for no rate limit by adding a new header each time as we can see there is some change
45

46
00:04:34,010 --> 00:04:36,110
into the response.
46

47
00:04:36,110 --> 00:04:39,380
Similarly I tried on Instagram and Instagram.
47

48
00:04:39,380 --> 00:04:44,300
Also we were able to see changes into the into the response by adding new headers.
48

49
00:04:45,380 --> 00:04:52,310
Similarly I tried on no broker but this time the response was same for everything because they are not
49

50
00:04:52,310 --> 00:04:59,270
parsing anything like this and no rate limit is fixed on their website and which cannot be bypassed
50

51
00:04:59,330 --> 00:05:00,480
anymore.
51

52
00:05:00,830 --> 00:05:05,250
99 acers is still the same on Tinder.com still the same.
52

53
00:05:05,250 --> 00:05:13,910
We are not able to perform no rate limit by bypassing by adding any of the headers I will attach this
53

54
00:05:13,910 --> 00:05:18,820
code in the description and you guys can utilize this for your testing.
54

55
00:05:18,830 --> 00:05:20,000
I hope you guys understood.
55

56
00:05:20,150 --> 00:05:20,990
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,080 --> 00:00:02,130
Hello everyone.
1

2
00:00:02,130 --> 00:00:09,230
So in this video we're going to see how we can use this one burp extension and how we can bypass 
2

3
00:00:09,300 --> 00:00:11,050
Rate limit attacks onto the website.
3

4
00:00:13,350 --> 00:00:19,110
If any Web site has put any kind of protection for rate limit and which is checking based on IP
4

5
00:00:19,110 --> 00:00:27,440
addresses we can bypass this as we already saw how this researcher was able to bypass that Instagram when
5

6
00:00:27,530 --> 00:00:29,660
vulnerability in a similar manner.
6

7
00:00:29,730 --> 00:00:38,850
We can make similar proof of concept for a website which do rate limiting based on IP addresses.
7

8
00:00:38,850 --> 00:00:43,920
So we are going to install this extension and I'm going to guide you how you can install this and how
8

9
00:00:43,920 --> 00:00:45,360
you can use it.
9

10
00:00:45,360 --> 00:00:51,310
Then we are going to see a proof of concept on a website that are able to bypass the rate limit on the
10

11
00:00:51,310 --> 00:00:51,840
website.
11

12
00:00:53,130 --> 00:00:53,850
Yes.
12

13
00:00:53,850 --> 00:01:02,820
So as you can see here this extension name is fake IP and we are going to load this into our burp suit.
13

14
00:01:02,820 --> 00:01:09,560
This extension gives us fake specified IP's local IP's random IP's and random IP blasting.
14

15
00:01:09,780 --> 00:01:10,490
OK.
15

16
00:01:10,770 --> 00:01:13,960
So as you can see please and put your IP.
16

17
00:01:14,160 --> 00:01:18,450
You can see here we are able to add new IP's new IP's.
17

18
00:01:18,450 --> 00:01:19,110
Yes.
18

19
00:01:19,110 --> 00:01:23,370
So let's quickly see how can we use this for that.
19

20
00:01:23,430 --> 00:01:26,580
First you need to go to your burpsuite in a burpsuite .
20

21
00:01:26,580 --> 00:01:29,410
You need to go to your extender and in extender.
21

22
00:01:29,410 --> 00:01:35,760
You need to go to the options tab and you need to set up the python environment for setting up the python
22

23
00:01:35,760 --> 00:01:36,410
environment.
23

24
00:01:36,420 --> 00:01:42,330
You need to download Jython standard standalone jar for downloading Jython.
24

25
00:01:42,330 --> 00:01:48,930
You just have to go to Jython.org/download this website and you can click on this Jython
25

26
00:01:48,960 --> 00:01:52,520
stand alone and you can download this after downloading.
26

27
00:01:52,530 --> 00:01:56,450
You just need to go into the burpsuite  and give the path where you have downloaded.
27

28
00:01:56,910 --> 00:02:02,270
So I've already selected the path of this Jython standalone after completing this.
28

29
00:02:02,280 --> 00:02:06,570
You have to go to the extensions in going after going in extensions.
29

30
00:02:06,570 --> 00:02:14,610
You have to add a new extension select python from here then it will .py file and just select
30

31
00:02:14,880 --> 00:02:17,820
fake IP (.py) already selected you.
31

32
00:02:17,910 --> 00:02:23,980
And just click next you will be able to see that fake IP extension is loaded here.
32

33
00:02:24,150 --> 00:02:26,220
Okay fine.
33

34
00:02:26,220 --> 00:02:28,860
So how do we test this.
34

35
00:02:28,890 --> 00:02:35,160
I am just going to say it show this how do we use this onto one of the request that is going to cloud
35

36
00:02:35,160 --> 00:02:35,640
flare
36

37
00:02:36,630 --> 00:02:41,020
I will just click anywhere right click and you can see option of fake IP.
37

38
00:02:41,190 --> 00:02:46,310
So there are three options input IP, the local host IP and a random IP.
38

39
00:02:46,380 --> 00:02:52,600
So I will just click on local host IP and you can see it is giving the local lost IP.
39

40
00:02:52,650 --> 00:02:59,270
So let me just clear everything because I already added these things into my when I was testing.
40

41
00:02:59,280 --> 00:03:00,600
Let me just delete everything.
41

42
00:03:01,190 --> 00:03:01,390
Yeah.
42

43
00:03:01,920 --> 00:03:03,990
So let me again just click right click.
43

44
00:03:03,990 --> 00:03:13,380
Fake IP and look back IP it as you can see this little extension is adding new IP addresses with new
44

45
00:03:13,860 --> 00:03:22,650
headers as you can see IP is the local loop back IP localized IP and x-forwarded for X-forwarded host client
45

46
00:03:22,680 --> 00:03:25,020
IP remote IP etc.. etc...
46

47
00:03:25,250 --> 00:03:26,190
Okay.
47

48
00:03:26,340 --> 00:03:32,840
In a similar manner you can right click you can click on fake IP you can input your own IP if you want.
48

49
00:03:32,840 --> 00:03:37,430
For let's say this and I input 192.168.1.1 and hit.
49

50
00:03:37,440 --> 00:03:38,020
Okay.
50

51
00:03:38,130 --> 00:03:41,590
So it will enter those IP.
51

52
00:03:42,180 --> 00:03:48,230
The last option is the random IP you click on random IP and it will automatically take the random IP.
52

53
00:03:48,240 --> 00:03:50,120
So let me just delete everything for you.
53

54
00:03:51,100 --> 00:03:51,530
Okay.
54

55
00:03:51,570 --> 00:03:57,360
So I hope you guys understood that how to use this fake IP extension in burp suite and you can try to
55

56
00:03:57,360 --> 00:04:00,450
bypass a lot of Web sites.
56

57
00:04:00,450 --> 00:04:00,930
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,060 --> 00:00:01,380
Hello everyone.
1

2
00:00:01,380 --> 00:00:09,040
So in this video I'm going to teach you guys how you can bypass rate limit on to websites.
2

3
00:00:09,060 --> 00:00:16,290
So we're going to test on this cloudfare's testing page on which we will test the rate limit on this
3

4
00:00:16,290 --> 00:00:16,740
page.
4

5
00:00:16,740 --> 00:00:24,020
If you refresh the browser 10 times in under one minute this page will block your IP basically rate
5

6
00:00:24,030 --> 00:00:26,590
limit your IP for one minute.
6

7
00:00:26,730 --> 00:00:34,290
The approach that I'm going to teach you on this Web site is what you can try on all other live websites
7

8
00:00:34,890 --> 00:00:39,270
and you will be able to find vulnerability.
8

9
00:00:39,690 --> 00:00:47,070
You can try this approach to hunt bugs for any Web site that you like which implements a rate limit
9

10
00:00:47,250 --> 00:00:48,690
and you will be able to bypass it.
10

11
00:00:50,130 --> 00:00:57,600
So I'm going to try on this Web site that am I able to bypass this rate limit test or not.
11

12
00:00:57,600 --> 00:00:58,910
It's for testing purposes.
12

13
00:00:58,920 --> 00:01:03,280
What I'm going to do is I'm going to take this request into my Burpsuit.
13

14
00:01:04,080 --> 00:01:07,030
So I've taken the request already in my Burpsuit.
14

15
00:01:07,050 --> 00:01:11,210
Let me just hit go and you can see I've already sent it one request and I'm getting 200.
15

16
00:01:11,220 --> 00:01:11,880
OK.
16

17
00:01:11,910 --> 00:01:14,890
Which means the website is not rate limiting.
17

18
00:01:15,030 --> 00:01:17,900
Let me reload it once more.
18

19
00:01:18,090 --> 00:01:19,680
It is not rate limiting yet.
19

20
00:01:19,680 --> 00:01:20,130
Yes.
20

21
00:01:20,610 --> 00:01:27,570
So what I'm going to do is I'm going to put a timer of one minute before putting the timer.
21

22
00:01:27,570 --> 00:01:32,910
And let's by putting the timer I'm going to check that if the Web site is rate limiting me or am I
22

23
00:01:32,920 --> 00:01:36,150
able to bypass the rate limit process under one minute.
23

24
00:01:36,150 --> 00:01:42,190
So I will just quickly go to my I I'll send this request to intruder and I've already sent this to intruder.
24

25
00:01:42,840 --> 00:01:43,670
OK.
25

26
00:01:44,040 --> 00:01:45,290
In my intruder tab.
26

27
00:01:45,720 --> 00:01:52,530
I'll just go to my payload options and choose null payloads because I don't want to add any position.
27

28
00:01:52,530 --> 00:01:58,590
I just want to send all the null payloads as it is as you can see I'm generating 12 payloads which
28

29
00:01:58,590 --> 00:02:03,050
means I'm going to hit the request twelve times in the options tab.
29

30
00:02:03,090 --> 00:02:11,670
I'm going to set the threads and request engine that is 100 threads which means I'm going to raise the request
30

31
00:02:12,000 --> 00:02:13,540
very fast.
31

32
00:02:13,590 --> 00:02:20,910
Remember guys this option can also be used for attacks like race conditions.
32

33
00:02:21,060 --> 00:02:21,450
Fine.
33

34
00:02:21,450 --> 00:02:23,730
I think everything is ready to go.
34

35
00:02:24,030 --> 00:02:25,920
So I'm just going to start this attack now.
35

36
00:02:26,910 --> 00:02:29,830
So before starting the attack let me start the timer.
36

37
00:02:29,910 --> 00:02:30,900
I have started the timer.
37

38
00:02:30,900 --> 00:02:31,900
Let me go quickly.
38

39
00:02:31,920 --> 00:02:32,970
Start the attack.
39

40
00:02:33,210 --> 00:02:36,220
And you can see that my all 12 payload have been sent.
40

41
00:02:36,290 --> 00:02:38,160
Okay let me just cancel this.
41

42
00:02:38,160 --> 00:02:39,460
Go to repeater hit.
42

43
00:02:39,480 --> 00:02:43,650
Go and you can see I'll be rate limited yes to any request I'm rate limited.
43

44
00:02:43,650 --> 00:02:45,240
Let me just go to fake IP.
44

45
00:02:45,240 --> 00:02:47,570
give a loop back IP too many request.
45

46
00:02:47,580 --> 00:02:53,150
Let me again try once more let's say again loop back IP and let me try to go.
46

47
00:02:53,220 --> 00:02:54,410
too Many request.
47

48
00:02:54,600 --> 00:03:01,530
Let me try a random IP so when I'm doing this you guys can see this application keeps on adding new
48

49
00:03:01,530 --> 00:03:02,590
IP addresses.
49

50
00:03:02,600 --> 00:03:13,020
So let me again try to give a loop back IP and still not able to bypass random IP right click fake IP
50

51
00:03:13,080 --> 00:03:17,140
let's say in put IP we give IP that is 180 to 18 audit trail.
51

52
00:03:17,640 --> 00:03:19,560
Well let it go.
52

53
00:03:19,810 --> 00:03:21,680
Too many request fake IP.
53

54
00:03:21,690 --> 00:03:23,440
Let's again give a look back IP.
54

55
00:03:23,460 --> 00:03:27,720
So basically we are giving a lot so many headers fake IP.
55

56
00:03:27,840 --> 00:03:30,880
Again this to go.
56

57
00:03:31,730 --> 00:03:32,800
One more time.
57

58
00:03:33,000 --> 00:03:35,040
So our timer is up guys.
58

59
00:03:35,950 --> 00:03:36,990
And let's see.
59

60
00:03:38,670 --> 00:03:41,750
Yes the timer is up and we were not able to bypass this.
60

61
00:03:41,760 --> 00:03:45,570
Now it came to a net again after a low after the one minute.
61

62
00:03:45,570 --> 00:03:47,790
So let me just mute this.
62

63
00:03:47,790 --> 00:03:48,390
Yes.
63

64
00:03:48,390 --> 00:03:52,290
So this is one way that you can test for rate limiting bugs.
64

65
00:03:52,590 --> 00:03:59,940
So we were not able to bypass that age limit on them onto this page obviously because this page blocks
65

66
00:03:59,970 --> 00:04:02,900
the request on CloudFlare server.
66

67
00:04:03,420 --> 00:04:06,510
So this was one of the ways that you can test for these types of bugs.
67

68
00:04:06,570 --> 00:04:07,830
I hope you guys understood.
68

69
00:04:07,830 --> 00:04:08,730
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,560 --> 00:00:02,910
Hello everyone.
1

2
00:00:02,910 --> 00:00:08,510
So in this video we are going to see what are the mitigations to stop this attack.
2

3
00:00:08,500 --> 00:00:20,540
Of  rate limit so always limit the request by any user which means the rate limit should be on a user
3

4
00:00:20,630 --> 00:00:21,410
basis.
4

5
00:00:22,140 --> 00:00:24,140
OK very fine.
5

6
00:00:24,170 --> 00:00:33,560
At the client side only and taking decisions is very very dangerous rate limiting users based on an
6

7
00:00:33,590 --> 00:00:34,720
IP No.
7

8
00:00:34,970 --> 00:00:45,760
This will never work as we already see in report in which Instagram vulnerability was exploited.
8

9
00:00:45,890 --> 00:00:46,770
Right.
9

10
00:00:46,820 --> 00:00:56,000
So you should not rate limit based on IP's because IP's can be changed headers like X forwarded
10

11
00:00:56,000 --> 00:00:58,530
host or X forwarded for.
11

12
00:00:58,580 --> 00:01:07,910
We already saw a lot of headers which can be used to achieve IP based spoofing and we can bypass the
12

13
00:01:07,910 --> 00:01:08,660
rate limit.
13

14
00:01:09,890 --> 00:01:17,500
So the application should not use IP based rate limit then what it should use.
14

15
00:01:17,840 --> 00:01:22,070
Number of attempts for an account at the server site checks.
15

16
00:01:22,250 --> 00:01:30,830
So any server should always verify that how many simultaneous requests is coming for the number
16

17
00:01:30,950 --> 00:01:34,620
of attempts of action that needs to be performed.
17

18
00:01:34,970 --> 00:01:43,640
For example a OTP brute force the server side check should be done on how many number of attempts
18

19
00:01:44,540 --> 00:01:48,860
is made for a specific action that is verification.
19

20
00:01:48,860 --> 00:01:51,080
In this example.
20

21
00:01:51,080 --> 00:01:56,780
And do blocking based on those actions.
21

22
00:01:56,780 --> 00:02:02,550
So I hope you guys understood that what are the mitigation's of no rate limit.
22

23
00:02:02,570 --> 00:02:03,040
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,240 --> 00:00:01,020
Hello everyone.
1

2
00:00:01,470 --> 00:00:08,280
So I searched for no rate limit Hackerone reports and I have got a couple of reports so I'm going to do
2

3
00:00:08,640 --> 00:00:09,420
a breakdown.
3

4
00:00:09,420 --> 00:00:16,570
Forms that what to look for whenever you're testing for No-Rate limit into the websites.
4

5
00:00:16,830 --> 00:00:20,940
So let's see the first report No-Rate limit on forgot password.
5

6
00:00:20,940 --> 00:00:24,720
Page of NordVPN bounty awarded 500 dollars.
6

7
00:00:24,720 --> 00:00:27,950
So let's see what this researcher was able to do.
7

8
00:00:28,140 --> 00:00:34,980
So after I read this report I was able to understand that the researcher was able to send forget password
8

9
00:00:34,980 --> 00:00:41,010
links onto his email address by intercepting the request into the Burpsuite.
9

10
00:00:41,010 --> 00:00:48,480
He was able to send a lot of Forgot password emails to his e-mail OK.
10

11
00:00:49,380 --> 00:00:55,260
By sending this to intruder and repeating it a hundred times he was able to send hundred emails to his
11

12
00:00:55,380 --> 00:01:00,220
inbox which was a business a business impact issue.
12

13
00:01:00,730 --> 00:01:01,310
Okay.
13

14
00:01:01,350 --> 00:01:06,660
So as you can see he was able to get a lot of e-mails into his inbox which was obviously of his business
14

15
00:01:06,660 --> 00:01:10,530
impact issue because it would be spamming anyone.
15

16
00:01:10,530 --> 00:01:14,270
So nordVPN awarded five hundred dollars for this issue.
16

17
00:01:14,310 --> 00:01:18,200
Let's see the second report Rate limiting missing at room login
17

18
00:01:18,240 --> 00:01:25,150
So there was an issue in this application of chaturbate in which there was a issue on the room 
18

19
00:01:25,150 --> 00:01:25,750
login user.
19

20
00:01:26,250 --> 00:01:35,220
So how this a user was able to reproduce was he made two accounts account A and Account B protect A's
20

21
00:01:35,220 --> 00:01:41,260
room with a password and login B account and then tried to access A room with random password.
21

22
00:01:41,310 --> 00:01:44,090
Obviously you wouldn't be able to log in with a random password.
22

23
00:01:44,100 --> 00:01:45,740
You need the right password.
23

24
00:01:45,780 --> 00:01:54,270
So this user is going to brute force the A room's password by using intruder and he will test for no
24

25
00:01:54,270 --> 00:01:55,230
rate limit.
25

26
00:01:55,230 --> 00:02:02,490
If the application allows to test a lot of passwords and does not hit a limit then that is then.
26

27
00:02:02,490 --> 00:02:09,390
This is vulnerable to no rate limit as you can see the user was able to request the intruder and he ran
27

28
00:02:09,390 --> 00:02:11,820
the intruder until he get the right password.
28

29
00:02:12,180 --> 00:02:18,390
OK so this was the second report wherein the user was able to brute force the password.
29

30
00:02:18,390 --> 00:02:20,520
So bounty awarded five hundred dollars.
30

31
00:02:20,550 --> 00:02:25,470
Let's see another report No-Rate limit on affiliate stats API endpoint.
31

32
00:02:26,340 --> 00:02:35,670
So in this case this is again the report on the same program that is chaturbate the user was able to brute
32

33
00:02:35,670 --> 00:02:42,600
force a token the affiliate stats API link is vulnerable to brute forcing the token as you can see.
33

34
00:02:42,720 --> 00:02:46,420
I used my profile and my token to check the brute force and the correct token return.
34

35
00:02:46,430 --> 00:02:47,010
Two hundred.
35

36
00:02:47,010 --> 00:02:47,680
OK.
36

37
00:02:47,880 --> 00:02:50,430
So what did this user did this user took.
37

38
00:02:50,430 --> 00:02:54,880
This particular request and he brute force the token one by one.
38

39
00:02:55,170 --> 00:03:00,720
And from the intruder tab he was able to achieve the right token.
39

40
00:03:01,590 --> 00:03:08,550
So we can finally conclude that this application was vulnerable to no rate limit as this user would was
40

41
00:03:08,550 --> 00:03:10,420
able to brute force a lot of tokens.
41

42
00:03:10,590 --> 00:03:17,130
And there was no limit on to the website bounty awarded 150 dollars.
42

43
00:03:17,130 --> 00:03:19,400
Let's see more reports.
43

44
00:03:19,440 --> 00:03:20,840
This is again the same report.
44

45
00:03:20,850 --> 00:03:22,800
No Rate limit on password reset function.
45

46
00:03:22,800 --> 00:03:26,020
We have already seen video POC's for this.
46

47
00:03:26,130 --> 00:03:30,480
No rate limit on reset password request again.
47

48
00:03:30,480 --> 00:03:31,620
Let's see this report.
48

49
00:03:31,620 --> 00:03:34,440
We have already discussed this report.
49

50
00:03:34,440 --> 00:03:36,790
This is on reset password.
50

51
00:03:36,860 --> 00:03:39,920
We had no rate limit on forget password.
51

52
00:03:40,800 --> 00:03:46,380
And the last one no limit on starting up a bot which is basically sign up.
52

53
00:03:46,380 --> 00:03:52,250
So we have seen all the reports on hacker one which leads to no rateblimit.
53

54
00:03:52,290 --> 00:03:59,760
So let's do a quick breakdown of these reports limit production bypass of hacker one report what are
54

55
00:03:59,760 --> 00:04:01,740
the lessons learned.
55

56
00:04:01,740 --> 00:04:08,690
Password Reset is the key functionality to test by sending x number of e-mails to your account.
56

57
00:04:08,700 --> 00:04:15,000
If they're able to do that then the application is vulnerable to no rate limit attack check for no rate
57

58
00:04:15,000 --> 00:04:21,390
limit at the OTP and verification process if they're able to brute force it and you are able to bypass
58

59
00:04:21,390 --> 00:04:27,990
the verification flow then it is vulnerable to No-Rate limit checking the No-Rate limit on the sign
59

60
00:04:27,990 --> 00:04:32,840
up creation process if we will be able to make X number of accounts on the application.
60

61
00:04:33,030 --> 00:04:40,200
And there is no limit on the the application then it is vulnerable to sign up creation check no limit
61

62
00:04:40,230 --> 00:04:46,560
on the password functionality in some cases as we saw the uplink the user was able to log in into a
62

63
00:04:46,560 --> 00:04:49,960
user A's account into the charurbate  report of hackerone
63

64
00:04:51,690 --> 00:04:54,450
Similarly you can test for password functionalities.
64

65
00:04:54,450 --> 00:04:58,950
And the last report that we saw was that the tokens.
65

66
00:04:58,950 --> 00:05:04,840
So checking No-Rate limit on tokens by guessing the correct tokens and if the application allows you to
66

67
00:05:04,840 --> 00:05:09,020
login or give out some sensitive information.
67

68
00:05:09,250 --> 00:05:14,150
So I hope you understood the breakdown of the hackerone report for No-Rate limit protection.
68

69
00:05:14,170 --> 00:05:14,680
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,580 --> 00:00:03,390
Hello, everyone.
1

2
00:00:04,290 --> 00:00:14,850
This video we are going to see OWASP Zap, so this is an excellent alternative to Burp Suite, but the tools
2

3
00:00:14,850 --> 00:00:25,470
are awesome into their own kind and both of those do pretty the same job OWASP Zap is an open source
3

4
00:00:25,470 --> 00:00:29,790
tool wherein Burp is a paid version.
4

5
00:00:31,020 --> 00:00:36,420
Anyone who is interested in using a WASP zap can easily use that.
5

6
00:00:36,420 --> 00:00:42,030
It is free to use this and it does the same job that we are going to do with Burp.
6

7
00:00:43,680 --> 00:00:50,220
On my personal side, I like using Burp more because I've been using that tool since many years that's why
7

8
00:00:50,220 --> 00:00:56,010
I have been more familiar with the options onto that particular tool.
8

9
00:00:56,910 --> 00:01:02,280
But I've also used a OWASP Zap for around one year and I really love this tool as well.
9

10
00:01:03,480 --> 00:01:07,950
Now there are some limitations in Burp community addition.
10

11
00:01:09,220 --> 00:01:19,440
One of the limitation is that we cannot use the intruder option in burp in the community addition.
11

12
00:01:20,880 --> 00:01:27,720
Actually, we can use the intruder version, but we cannot throttle our request, which means if you
12

13
00:01:27,720 --> 00:01:33,570
want to brute force something so let's say we are testing for No rate limit, then you can test it obviously
13

14
00:01:33,570 --> 00:01:41,360
with Burp Suit, but you cannot put delay between your two request or you cannot throttle your two requests.
14

15
00:01:42,690 --> 00:01:50,460
So for that, for those who do not have a premium version of Burp Suite, you can always use OWASP Zap.
15

16
00:01:51,370 --> 00:01:58,090
So we are going to see how you can use ZAP for doing No rate limit type of attacks in case you do not
16

17
00:01:58,090 --> 00:02:00,690
have a premium version of Burp Suite Prp.
17

18
00:02:02,080 --> 00:02:02,520
All right.
18

19
00:02:02,530 --> 00:02:06,430
So this is the website of ZAP, which is owasp.org
19

20
00:02:07,060 --> 00:02:12,910
You just need to come on to this particular website and you can see a download now button and just simply click
20

21
00:02:12,910 --> 00:02:13,570
on this button.
21

22
00:02:14,410 --> 00:02:21,580
And according to your operating system or distribution, you can download this tool.
22

23
00:02:22,030 --> 00:02:31,030
As you can see, Windows 64 bit, Windows 32, Linux, Mac OS or any other cross platform package for
23

24
00:02:31,030 --> 00:02:31,520
my computer.
24

25
00:02:31,540 --> 00:02:36,250
I'm going to download the Mac installer version, so I just need to click on download.
25

26
00:02:36,760 --> 00:02:38,060
I have already done this.
26

27
00:02:38,230 --> 00:02:39,610
Let me just show you.
27

28
00:02:41,450 --> 00:02:45,030
In my download, and you can see it over here.
28

29
00:02:45,950 --> 00:02:52,820
So if I need to install it, I just need to double click it and drag and drop it over here.
29

30
00:02:53,450 --> 00:02:55,340
It is going to ask me to replace.
30

31
00:02:55,490 --> 00:02:57,460
So I'm not going to replace it.
31

32
00:02:57,490 --> 00:02:58,850
I'll just stop it.
32

33
00:03:00,470 --> 00:03:06,380
That's it for Mac OS installation and for others, for Windows and Linux, it is pretty much very,
33

34
00:03:06,380 --> 00:03:11,530
very simple and you will be able to install it without any issues.
34

35
00:03:11,540 --> 00:03:13,400
In case you come up with any issues.
35

36
00:03:13,400 --> 00:03:15,920
You can post it into the Q&A.
36

37
00:03:16,370 --> 00:03:18,020
I would love to help.
37

38
00:03:18,980 --> 00:03:19,490
All right.
38

39
00:03:19,520 --> 00:03:26,660
So let's quickly start OWASP Zap and see how does it looks like how is that UI and how you can use it?
39

40
00:03:27,770 --> 00:03:29,030
So I'm going to start Zap
40

41
00:03:31,230 --> 00:03:36,870
So it looks something like this and 2.9.0 is the latest version that we can see
41

42
00:03:37,260 --> 00:03:38,340
on the website.
42

43
00:03:38,610 --> 00:03:45,000
Also now it will ask you if you want to save your session for this particular task that you are going
43

44
00:03:45,000 --> 00:03:45,620
to perform.
44

45
00:03:46,260 --> 00:03:49,990
So I'm not going to save it for now.
45

46
00:03:50,730 --> 00:03:53,670
So what I'm going to do now, this is how your ZAP looks like.
46

47
00:03:55,290 --> 00:04:02,180
So I need to open up a browser with pre configured proxy, so I just need to click it over here.
47

48
00:04:02,190 --> 00:04:05,500
As you can see, a small little Firefox icon.
48

49
00:04:06,390 --> 00:04:12,120
Now you can see explore your application with Zap, browser is automatically configured to proxy via ZAP
49

50
00:04:12,120 --> 00:04:14,420
and we ignore certificate warnings.
50

51
00:04:15,000 --> 00:04:23,070
So this is one of the best feature of ZAP in which your browsers get automatically configure, although
51

52
00:04:23,070 --> 00:04:30,180
Burp has also released this particular feature into their latest release, the latest update recently.
52

53
00:04:30,180 --> 00:04:31,800
But this feature was there already.
53

54
00:04:31,800 --> 00:04:35,020
in Burp, in Zap, I'm sorry, since many years.
54

55
00:04:35,520 --> 00:04:36,000
All right.
55

56
00:04:36,210 --> 00:04:42,000
So now let us open up Google dot com and confirm if this is working perfectly fine.
56

57
00:04:42,420 --> 00:04:50,010
And we can see the request automatically started coming over here and our browser is configured to work
57

58
00:04:50,010 --> 00:04:50,530
properly.
58

59
00:04:52,020 --> 00:04:59,340
Now, let us go to our target application for where we are going to test this particular vulnerability.
59

60
00:05:00,120 --> 00:05:06,300
So I'm going to go on this website, which is food cloud, and we are going to try no rate limit over
60

61
00:05:06,300 --> 00:05:06,680
here.
61

62
00:05:08,920 --> 00:05:14,980
I just open this particular website and go into the login feature.
62

63
00:05:17,210 --> 00:05:23,960
On the Login with phone numbers, I'm going to go on Log-in with OTP and I'm going to put my phone number.
63

64
00:05:26,220 --> 00:05:31,240
Now, I'm going to click on Send OTP and the request will come over here.
64

65
00:05:31,530 --> 00:05:32,280
So just.
65

66
00:05:35,480 --> 00:05:43,910
See, I have clicked and now I'm going to put a wrong OTP, so let's say I put one, two, three,
66

67
00:05:43,910 --> 00:05:47,090
four over here and I click on Verify.
67

68
00:05:47,120 --> 00:05:52,700
Remember, this is a wrong OTP that I have entered because I want to capture the request in my ZAP.
68

69
00:05:53,480 --> 00:05:59,040
So I'm going to see where is the request for food cloud and I'm going to use that particular request.
69

70
00:05:59,720 --> 00:06:05,690
Now you can see over here in Food Cloud, this particular request is the post request, which contains
70

71
00:06:05,690 --> 00:06:07,810
the OTP code and phone number.
71

72
00:06:08,540 --> 00:06:17,900
And if I click this particular request and send it to my fUZZ, then you can see over here, this is
72

73
00:06:17,900 --> 00:06:18,800
the code.
73

74
00:06:18,830 --> 00:06:19,820
This is the phone number.
74

75
00:06:20,480 --> 00:06:24,040
And we have given the code as one, two, three, four.
75

76
00:06:24,980 --> 00:06:29,450
If you click on, if I will cancel this, let me show it over here as well.
76

77
00:06:29,960 --> 00:06:35,180
If I click on Request, you can see the request as well, you and the response as well.
77

78
00:06:35,180 --> 00:06:38,970
And the response is OTP code error, please.
78

79
00:06:38,990 --> 00:06:40,700
enter a valid OTP, obviously
79

80
00:06:40,700 --> 00:06:41,000
guys.
80

81
00:06:41,030 --> 00:06:41,630
This is wrong 
81

82
00:06:41,630 --> 00:06:43,100
OTP that I have entered?
82

83
00:06:43,610 --> 00:06:45,770
That's why I have got an error message.
83

84
00:06:46,670 --> 00:06:51,790
Now I'm just going to right click, click on attack and click on FUZZ.
84

85
00:06:52,910 --> 00:07:00,220
Now the intruder tab of Burp Suite is fuzzer tab of OWASP zap.
85

86
00:07:00,680 --> 00:07:01,160
All right.
86

87
00:07:01,640 --> 00:07:10,850
Now let's quickly FUZZ or basically brute force or do red intruder with the right OTP to perform No rate
87

88
00:07:10,850 --> 00:07:12,740
limit on this website.
88

89
00:07:13,790 --> 00:07:16,430
Now I have to choose this as my injection point.
89

90
00:07:16,430 --> 00:07:22,310
So I'm going to double click the one, two, three, four OTP code and I'm going to click add.
90

91
00:07:22,520 --> 00:07:30,620
As we can see on the right hand side, once I click that it is going to ask me the payload window that
91

92
00:07:30,980 --> 00:07:32,630
do I want to add payload.
92

93
00:07:33,200 --> 00:07:38,690
So I need to click on ADD and then it will open up a new window over here.
93

94
00:07:39,380 --> 00:07:46,550
Now my OTP is in the form of numbers, so I'm going to choose numbers over here and the range that I
94

95
00:07:46,550 --> 00:07:47,270
want to choose.
95

96
00:07:47,450 --> 00:07:48,950
So I'm going to choose a range.
96

97
00:07:49,280 --> 00:07:50,630
So the range would be.
97

98
00:07:56,430 --> 00:08:01,470
So I have got the OTP, which is 2431, so I'm going to choose the range, which is.
98

99
00:08:03,450 --> 00:08:04,830
24
99

100
00:08:07,370 --> 00:08:19,460
20 to 2435, and you can leave the increment to one, this increment one means
100

101
00:08:19,820 --> 00:08:26,750
it is going to start the OTP from two four two zero to two four three five.
101

102
00:08:26,750 --> 00:08:32,420
And it is going to increment each by one, which basically means the first OTP will be two four two
102

103
00:08:32,420 --> 00:08:32,740
zero.
103

104
00:08:33,080 --> 00:08:37,160
Next would be two four two one,    two four two two and so on.
104

105
00:08:37,760 --> 00:08:42,260
If you want to see the preview, you can click on Generate Preview as well and you will be able to see
105

106
00:08:42,560 --> 00:08:48,200
whatever payloads you are going to put or whatever what piece our Zap is going to put.
106

107
00:08:48,470 --> 00:08:58,580
Now I will click on add and click on OK, now we need to go in options and over here you can see the
107

108
00:08:58,580 --> 00:08:59,320
delay button.
108

109
00:09:00,470 --> 00:09:02,210
There is also concurrency.
109

110
00:09:02,540 --> 00:09:09,500
If you want to increase the concurrency, you can increase that as well so that our request will go much
110

111
00:09:09,500 --> 00:09:10,290
more faster.
111

112
00:09:10,400 --> 00:09:15,080
I do not want to increase the concurrency, so I'll just decrease it because I want one.
112

113
00:09:15,080 --> 00:09:23,140
thread per scan also I'm going to increase the delay in fuzzing that is to one thousand milliseconds
113

114
00:09:24,170 --> 00:09:29,900
now I'm going to start the fuzzer and let's wait and see what happens.
114

115
00:09:30,560 --> 00:09:36,770
As you can see, the fuzzer has started successfully over here, the total number of message sent,
115

116
00:09:36,770 --> 00:09:41,750
which is basically the number of request and the request can be seen over here.
116

117
00:09:47,740 --> 00:09:53,440
Now we are waiting for this to complete, and as this has successfully complete, we will be able to
117

118
00:09:53,440 --> 00:09:55,840
see the right be court.
118

119
00:09:56,650 --> 00:10:03,130
So once this is 100 percent, then we are going to see the difference that has been there into this
119

120
00:10:03,130 --> 00:10:03,760
request.
120

121
00:10:05,470 --> 00:10:07,390
Yes, so this is completed now.
121

122
00:10:07,810 --> 00:10:14,190
Now, these are all the 16 request that was done, which is known as message sent over here.
122

123
00:10:14,710 --> 00:10:21,760
And what I'm going to do is I'm going to double click on size a response body.
123

124
00:10:22,150 --> 00:10:26,170
So I'm just going to double click and you can see the biggest size response body.
124

125
00:10:27,130 --> 00:10:28,390
Now, what does this mean?
125

126
00:10:29,590 --> 00:10:34,180
This means our OTP was correct and successfully verified.
126

127
00:10:34,180 --> 00:10:36,370
As you can see, the OTP was two, four, three, one.
127

128
00:10:36,880 --> 00:10:40,630
And the response that we have received for this particular OTP is success.
128

129
00:10:41,260 --> 00:10:44,120
And the message is your account has been successfully created.
129

130
00:10:45,160 --> 00:10:52,270
Now, if you see other OTPs, let's say the next one over here, you can see the OTP that was supplied
130

131
00:10:52,270 --> 00:10:53,440
was one, two, three, four.
131

132
00:10:53,950 --> 00:10:58,000
And the response which was received was error OTP code.
132

133
00:10:58,600 --> 00:11:02,500
Please enter a valid OTP and the response body is 49 bytes.
133

134
00:11:03,100 --> 00:11:09,400
And if you notice, then all the particular requests that have been supplied has the same response body,
134

135
00:11:09,430 --> 00:11:10,690
which is forty nine bytes.
135

136
00:11:11,260 --> 00:11:19,720
Through this we can easily detect in case any rate OTP is going to pass, it is going to show some different
136

137
00:11:19,720 --> 00:11:26,890
response, which will be different from the wrong one, which is going to be not matched with the wrong
137

138
00:11:26,890 --> 00:11:35,110
one because of which a new response body will be changed or something is going to change into the response,
138

139
00:11:35,110 --> 00:11:42,370
as we can see or hear, due to which the response body size is going to change and we are going to identify
139

140
00:11:42,370 --> 00:11:43,090
based on that.
140

141
00:11:44,440 --> 00:11:45,910
If you see other piece.
141

142
00:11:46,250 --> 00:11:52,450
Let me just go back to a request and show you this is 2422which is wrong, 2423 
142

143
00:11:52,450 --> 00:11:54,640
2424    2425
143

144
00:11:54,970 --> 00:12:01,810
And the response model remains the same for all the wrong responses, but for the right one, it changes.
144

145
00:12:02,170 --> 00:12:10,740
And we are able to identify that by double clicking on this particular size response body button.
145

146
00:12:11,950 --> 00:12:20,100
So I hope you guys understood how you can utilize OWASP Zap for performing no rate limit types of attacks.
146

147
00:12:20,860 --> 00:12:21,400
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 3: Cross Site Scripting (XSS)

0
1
00:00:00,060 --> 00:00:07,200
Hello Everyone so in this video we are going to learn about XSS that is cross site scripting.
1

2
00:00:09,210 --> 00:00:15,530
So in this video series we will be seeing what is XSS? why XSS happenes.
2

3
00:00:15,660 --> 00:00:17,880
What is the severity of XSS?.
3

4
00:00:17,910 --> 00:00:24,150
What are the types of XSS and different ways to do XSS vulnerability and you will be able
4

5
00:00:24,150 --> 00:00:28,110
to hunt this vulnerability on all the live websites
5

6
00:00:31,960 --> 00:00:34,260
what are the types of XSS.
6

7
00:00:34,270 --> 00:00:43,300
There are three types of XSS reflected wherein the input gets reflected on to the web application.
7

8
00:00:43,300 --> 00:00:51,130
For example if you give input that is your name into a search bar of any website let's say you gave
8

9
00:00:51,190 --> 00:00:54,880
Rohit and Rohit is again reflected on the website.
9

10
00:00:55,060 --> 00:01:02,150
For example No results found for the query to hit then this is a reflected type.
10

11
00:01:02,350 --> 00:01:09,670
You can try to search by reflected XSS there next is stored XSS.
11

12
00:01:09,760 --> 00:01:16,960
If the input gets stored into the server then this type of vulnerability is known as stored XSS
12

13
00:01:18,010 --> 00:01:25,090
in DOM accesses if the input passes through the DOM
which is basically through the source and comes
13

14
00:01:25,090 --> 00:01:27,670
out of the sink.
14

15
00:01:28,000 --> 00:01:30,030
How a XSS works.
15

16
00:01:30,040 --> 00:01:37,840
So here is an example through which you will understand how a basic XSS works.
16

17
00:01:37,840 --> 00:01:41,730
As you can see there is a client on the left side on the right side.
17

18
00:01:41,740 --> 00:01:43,950
It is a server and there is the attacker.
18

19
00:01:45,490 --> 00:01:51,210
So the attacker sends a link to the client.
19

20
00:01:51,580 --> 00:02:00,550
The client will click on that link and the client or the victim will authenticated with the server.
20

21
00:02:00,550 --> 00:02:08,670
Remember the link contains the malicious payload after the victim has authenticated with the server.
21

22
00:02:08,740 --> 00:02:13,850
The server will send the cookie to the attacker.
22

23
00:02:14,050 --> 00:02:17,800
Which cookie the authenticated cookie of the client.
23

24
00:02:17,800 --> 00:02:25,720
Now the attacker has got the cookie of the client and now attacker can log in as the victim or the client.
24

25
00:02:25,720 --> 00:02:29,340
So basically he's able to do an account takeover
25

26
00:02:33,700 --> 00:02:37,050
so first we are going to see XSS reflected.
26

27
00:02:37,570 --> 00:02:45,130
Check for if input gets reflected in the page source, body or URL so you should check whenever
27

28
00:02:45,130 --> 00:02:52,090
you give any input into a web page that it is getting reflected in the page source in the body or in
28

29
00:02:52,090 --> 00:02:54,680
the you URL next.
29

30
00:02:54,910 --> 00:03:03,100
If the input gets reflected we can hunt for reflected XSS sending a simple javascript to execute
30

31
00:03:03,190 --> 00:03:04,660
and prove XSS.
31

32
00:03:04,660 --> 00:03:11,290
We are going to do if there is no input validation or sanitization then it is very dangerous and there
32

33
00:03:11,290 --> 00:03:13,840
can be a vulnerability of XSS.
33

34
00:03:15,760 --> 00:03:24,340
So yes this is the practical time now and let's see reflected XSS how it can be done.
34

35
00:03:24,850 --> 00:03:33,940
So as you can see I am on to a web application which is testphp.vulnweb.com on left say you
35

36
00:03:33,940 --> 00:03:38,210
can see there is a search box in which I am going to type hacktify
36

37
00:03:41,890 --> 00:03:45,310
and I will hit go after typing hacktify.
37

38
00:03:45,330 --> 00:03:50,200
You can see it has got reflected onto the website as you can see here.
38

39
00:03:50,200 --> 00:03:59,130
It has got reflected which means there is a reflection so I can try for reflected XSS.
39

40
00:03:59,380 --> 00:04:07,210
I'm just going to try a very basic javascript and see that that if this javascript gets reflected
40

41
00:04:07,480 --> 00:04:16,060
or executed if this javascript gets executed then there is a vulnerability of reflected XSS.
41

42
00:04:17,560 --> 00:04:23,790
So a simple javascript looks like script alert something into that alert box.
42

43
00:04:23,800 --> 00:04:25,750
Lets say 2 and script close
43

44
00:04:34,480 --> 00:04:39,610
let me open a sublime text editor and show you what the script looked like.
44

45
00:04:39,880 --> 00:04:47,800
So the script starts the script ends and in the middle you can see there is a alert which says 2.
45

46
00:04:47,950 --> 00:04:54,160
So when this script is going to get executed there should be a alert box with the number two.
46

47
00:04:57,130 --> 00:04:58,130
Yes.
47

48
00:04:58,270 --> 00:05:06,110
So the application is successfully executing our  javascript which means this application is vulnerable
48

49
00:05:06,160 --> 00:05:10,890
to reflected XSS.
49

50
00:05:10,900 --> 00:05:18,730
Now what we're going to do is instead of two I'm going to type document.domain in which I am going
50

51
00:05:18,730 --> 00:05:26,440
to see the name of the web application the web application name is testphp.vulnweb 
51

52
00:05:27,010 --> 00:05:30,880
Let's see if we can get the name.
52

53
00:05:30,880 --> 00:05:31,600
Yes.
53

54
00:05:31,690 --> 00:05:34,210
So we have got the name.
54

55
00:05:34,750 --> 00:05:39,690
Now let's try to get a cookie from this application.
55

56
00:05:39,760 --> 00:05:47,790
So for that we are going to type document.cookie and we are going to execute this javascript and
56

57
00:05:47,800 --> 00:05:49,990
I hit enter and press go.
57

58
00:05:50,380 --> 00:05:59,080
As you can see this has got executed but not showing any type of cookie because that we are not authenticated
58

59
00:05:59,140 --> 00:06:00,400
into the website right now.
59

60
00:06:00,460 --> 00:06:09,700
So the website has not generated any cookie for the user.
60

61
00:06:10,060 --> 00:06:13,230
I hope you guys understood what is reflected XSS.
61

62
00:06:13,240 --> 00:06:13,690
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,020 --> 00:00:01,800
Hello everyone.
1

2
00:00:02,190 --> 00:00:10,650
So in this video we are going to see XSS balancing which is a very important part of XSS.
2

3
00:00:10,680 --> 00:00:19,030
So in this video we will learn how to balance XSS and execute our javascript so.
3

4
00:00:19,140 --> 00:00:24,460
See this in the practical time.
4

5
00:00:25,410 --> 00:00:32,660
So I'm on to a website which is orientalbirdimages.org as you can see there is a search parameter
5

6
00:00:32,760 --> 00:00:38,030
so I'm just going to quickly search my name.
6

7
00:00:38,160 --> 00:00:43,370
So let's say I search for hacktify and I click go just to check that.
7

8
00:00:43,410 --> 00:00:47,900
Is this getting reflected as you can observe in the url.
8

9
00:00:48,090 --> 00:00:52,200
It is getting reflected into a parameter which is keyword parameter.
9

10
00:00:53,800 --> 00:01:02,640
OK so now what I'm going to do is I'm going to quickly give a very simple basic payload of javascript
10

11
00:01:03,000 --> 00:01:06,440
to check if this gets executed or not.
11

12
00:01:06,510 --> 00:01:09,460
So I will just hit go and wait.
12

13
00:01:09,570 --> 00:01:12,970
No this did not get executed.
13

14
00:01:13,010 --> 00:01:14,130
Why.
14

15
00:01:14,280 --> 00:01:16,940
So let's see into the page source.
15

16
00:01:16,980 --> 00:01:18,570
What happened in the background
16

17
00:01:21,960 --> 00:01:25,860
as you can see in the page source.
17

18
00:01:25,890 --> 00:01:30,740
I searched for hacktify and you can see one of one match found here at the bottom.
18

19
00:01:31,170 --> 00:01:35,940
So now my payload has become of value.
19

20
00:01:35,940 --> 00:01:41,710
If you look closely here my payload has become the value of the parameter value.
20

21
00:01:41,730 --> 00:01:42,400
Right.
21

22
00:01:42,420 --> 00:01:44,200
So my payload is here.
22

23
00:01:44,280 --> 00:01:51,590
I need to take out my payload outside of this value which is in this double quotes as you can see the
23

24
00:01:51,590 --> 00:01:53,290
double quotes.
24

25
00:01:53,640 --> 00:01:58,740
So I need to take out this payload outside to execute it.
25

26
00:01:58,770 --> 00:01:59,390
OK.
26

27
00:01:59,430 --> 00:02:06,440
So what I'm going to do is if you look closely my payload starts from hacktify than script alert.
27

28
00:02:06,460 --> 00:02:16,020
One script tag close and it is between this double quotes what if I gave this ending double quote here.
28

29
00:02:17,160 --> 00:02:20,780
So the application will think value double quote start.
29

30
00:02:20,840 --> 00:02:23,460
Hacktify doublt quote close.
30

31
00:02:23,520 --> 00:02:29,650
Also I give this closing braces bracket over here over here
31

32
00:02:29,660 --> 00:02:37,250
The application will think that this has ended over here and this is not into the value of the parameter.
32

33
00:02:37,380 --> 00:02:41,480
So let's see what do we do.
33

34
00:02:41,580 --> 00:02:50,840
I'm just going to copy the whole payload and I have seen how it gets ended or closed.
34

35
00:02:50,910 --> 00:02:59,100
So I'll just go here and end this by this by giving this and hit on go as you can see I have successfully
35

36
00:02:59,430 --> 00:03:09,660
executed the payload which means I was able to do a successful balancing.
36

37
00:03:09,660 --> 00:03:10,750
I hope you guys understood.
37

38
00:03:10,950 --> 00:03:11,430
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,500 --> 00:00:03,000
Hello everyone.
1

2
00:00:03,000 --> 00:00:12,090
So here it is one more proof of concept for explaining our reflected type of XSS a RXSS.
2

3
00:00:12,870 --> 00:00:14,450
So what happens in reflected XSS.
3

4
00:00:14,500 --> 00:00:23,010
XSS is whenever a user gives input to the web application the web application will take that input
4

5
00:00:23,370 --> 00:00:32,700
interpret it and basically reflect it in this case when we are going to give an input that is going to
5

6
00:00:32,700 --> 00:00:39,930
be our XSS payload the application will take that input and instead of reflecting it it is going
6

7
00:00:39,930 --> 00:00:41,910
to execute it.
7

8
00:00:42,060 --> 00:00:50,070
If any application is executing the arbitrary supplied payload or input and the application is vulnerable
8

9
00:00:50,070 --> 00:00:55,320
to XSS in case of JavaScript execution.
9

10
00:00:55,500 --> 00:01:02,130
So let's see this as you can see there is a search field and gaing to type hacktify into the search
10

11
00:01:02,130 --> 00:01:03,090
field right now
11

12
00:01:08,700 --> 00:01:15,920
along with this I'm going to give the simple basic payload that we know that a script alert one script
12

13
00:01:15,920 --> 00:01:20,370
tag close and I'm going to hit enter.
13

14
00:01:20,370 --> 00:01:30,310
As you can see the application executed our payload which means this application is vulnerable to our
14

15
00:01:30,750 --> 00:01:33,760
reflected XSS attack.
15

16
00:01:33,810 --> 00:01:35,340
I hope you guys understood.
16

17
00:01:35,340 --> 00:01:35,820
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


0
1
00:00:01,530 --> 00:00:03,050
Hello everyone.
1

2
00:00:03,060 --> 00:00:10,170
So in this video we are going to see how to do manual XSS payload building.
2

3
00:00:11,250 --> 00:00:18,440
So this is very important because we know we find XSS everywhere in most of the Web site.
3

4
00:00:18,480 --> 00:00:24,120
So in this video we will learn how we can do manual XSS payload building.
4

5
00:00:24,570 --> 00:00:27,210
So let's see this.
5

6
00:00:27,210 --> 00:00:31,210
I'm onto this Web site which is orientedbirdimages.com.
6

7
00:00:31,620 --> 00:00:38,010
So I'm just going to search for hacktify in the input that is search and after I can see it is getting
7

8
00:00:38,010 --> 00:00:43,530
reflected where it is getting reflected into the url bar as you can see or here.
8

9
00:00:43,620 --> 00:00:44,820
Perfect.
9

10
00:00:44,820 --> 00:00:51,540
So I will just go to the page source by clicking on view page Source as you can see this is the page
10

11
00:00:51,540 --> 00:00:56,610
source I'm going to copy this and go to our editor.
11

12
00:00:56,610 --> 00:00:59,940
Now I'm going to paste the page source into this notepad editor.
12

13
00:01:01,980 --> 00:01:09,370
So after just pasting it over here I'm going to search for the input that I gave and I gave hacktify
13

14
00:01:09,390 --> 00:01:11,470
and you can see there is one match.
14

15
00:01:11,490 --> 00:01:12,810
Perfect.
15

16
00:01:12,810 --> 00:01:20,090
So as you can see over here hacktify is the input which is coming in the parameter that is value.
16

17
00:01:20,250 --> 00:01:26,250
So the parameter is value and the input that has been given which is the value is over here between
17

18
00:01:26,250 --> 00:01:33,030
the double quotes if we can see the double quotes here and the double quotes here and the value is which means the input
18

19
00:01:33,150 --> 00:01:34,840
is into this double quotes.
19

20
00:01:34,890 --> 00:01:35,390
Perfect.
20

21
00:01:36,570 --> 00:01:42,900
So by this we can conclude that whatever we give as an input into this Web site comes into these types
21

22
00:01:42,900 --> 00:01:44,030
of double quotes.
22

23
00:01:44,070 --> 00:01:51,060
So if we give the payload XSS payload it will also come between this double quotes perfect
23

24
00:01:51,840 --> 00:01:57,450
as you can see over here there is also a closing bracket which indicates this is the closing bracket
24

25
00:01:57,450 --> 00:02:00,580
for this opening bracket which is input type.
25

26
00:02:01,530 --> 00:02:02,100
Yes.
26

27
00:02:02,100 --> 00:02:03,340
So let's see.
27

28
00:02:03,360 --> 00:02:04,050
Furthermore
28

29
00:02:10,680 --> 00:02:13,330
our input comes between this double quotes.
29

30
00:02:13,380 --> 00:02:15,250
We have already seen that.
30

31
00:02:15,510 --> 00:02:19,830
And now let's say if I give XSS payload onto that search field.
31

32
00:02:19,830 --> 00:02:25,740
It is going to come like this into the input somewhat like this.
32

33
00:02:27,480 --> 00:02:29,130
Yes.
33

34
00:02:29,940 --> 00:02:35,250
A simple XSS payload that a script alert one and script tag close.
34

35
00:02:35,250 --> 00:02:39,000
Now as you can see my payload has become the value.
35

36
00:02:39,000 --> 00:02:44,060
And if my payload becomes a value I cannot do XSS .
36

37
00:02:44,070 --> 00:02:49,640
So let me just try to hit it over here and hit go as you can see nothing happened.
37

38
00:02:49,680 --> 00:02:53,280
No execution therefore no XSS 
38

39
00:02:57,110 --> 00:03:04,310
which means I need to balance this I need to balance the input which is going over here my input is
39

40
00:03:04,310 --> 00:03:06,560
becoming value between these double quotes.
40

41
00:03:06,620 --> 00:03:16,550
So what if I try to I try to make this value come out of those double quotes.
41

42
00:03:16,610 --> 00:03:23,340
How so the application logic is any input should come between the quotes.
42

43
00:03:23,570 --> 00:03:27,900
What if I give a double quote into my payload itself.
43

44
00:03:27,950 --> 00:03:33,020
The application will get tricked and the application will thing let's say if I give a double quote
44

45
00:03:33,020 --> 00:03:39,170
over here after hacktify the application will think that the value is completed or here the input
45

46
00:03:39,170 --> 00:03:46,310
is completed over here and it will treat this as out of outside of the value and it will try to execute
46

47
00:03:46,310 --> 00:03:47,450
it perfect.
47

48
00:03:48,350 --> 00:03:55,160
So I'm just going to copy this double quotes and closing bracket and I'm going to tell that the 
48

49
00:03:55,160 --> 00:04:04,310
gets closed over here and basically that the value gets closed over here whatever the attacker is going
49

50
00:04:04,310 --> 00:04:04,810
to give.
50

51
00:04:04,850 --> 00:04:09,710
In our case we're going to give hacktify and XSS payload so a double quotes here and then I'm
51

52
00:04:09,710 --> 00:04:13,580
going to close this by this closing bracket of this input type
52

53
00:04:17,150 --> 00:04:21,750
so I'll just do that quickly and double quotes and closing bracket.
53

54
00:04:21,800 --> 00:04:22,290
Perfect.
54

55
00:04:22,880 --> 00:04:29,750
So now my payload is this what is my payload my payload is hacktify double quotes closing bracket
55

56
00:04:30,050 --> 00:04:32,330
and then script alert one script tag close.
56

57
00:04:33,140 --> 00:04:39,530
Let me just so save the source code into a file which is balance1.html and let's try
57

58
00:04:39,530 --> 00:04:48,110
to open this balance1.html into our browser if we get a XSS execution then we have successfully
58

59
00:04:48,110 --> 00:04:52,950
balanced our payload so let's try to see this perfect we got one.
59

60
00:04:53,000 --> 00:04:58,310
Let's try to reload this and we are getting an XSS execution which means we have successfully
60

61
00:04:59,420 --> 00:05:00,720
balanced our payload.
61

62
00:05:00,830 --> 00:05:01,310
Perfect.
62

63
00:05:01,640 --> 00:05:08,450
So let's take this payload from here now payload starts from hacktify till script tag close till here
63

64
00:05:09,140 --> 00:05:16,220
let's copy this go on to the website and paste it over here   put it and hit go.
64

65
00:05:16,220 --> 00:05:16,910
Perfect.
65

66
00:05:16,970 --> 00:05:20,920
We have successfully balanced our payload.
66

67
00:05:21,060 --> 00:05:23,060
Let's go to one more website.
67

68
00:05:23,060 --> 00:05:24,600
This is bewakoof.com.
68

69
00:05:25,740 --> 00:05:29,820
Let's try to search for hacktify over here and hit enter.
69

70
00:05:30,680 --> 00:05:33,980
Now you can see I'm getting a reflection of hacktify.
70

71
00:05:34,460 --> 00:05:39,710
Now I will right click and do view page Source because I want to see the source code and just copy this
71

72
00:05:40,370 --> 00:05:43,740
go into my favorite editor again and paste it over here.
72

73
00:05:44,000 --> 00:05:46,990
Now I'm going to search for the input that is hacktify.
73

74
00:05:47,450 --> 00:05:55,040
As you can see there are total 17 matches which means it is getting reflected and 17 positions 17 different
74

75
00:05:55,040 --> 00:05:57,560
positions into the page source.
75

76
00:05:57,620 --> 00:06:00,020
So I'm going to take one of the source that I want.
76

77
00:06:00,570 --> 00:06:05,450
So let's see which source do we take Mm hmm.
77

78
00:06:05,670 --> 00:06:06,480
not this one.
78

79
00:06:06,510 --> 00:06:13,500
Let's try to take a source which is let's say param equals to value type.
79

80
00:06:13,580 --> 00:06:17,320
So yeah let's take this one over here.
80

81
00:06:17,340 --> 00:06:21,250
You can see hacktify is getting reflected.
81

82
00:06:21,330 --> 00:06:27,290
Now what if I instead of hacktify I give the XSS payload with hacktify
82

83
00:06:27,600 --> 00:06:35,280
So it is going to look somewhat like this into the page source hacktify  script alert one script tag
83

84
00:06:35,280 --> 00:06:37,230
close a basic XSS payload
84

85
00:06:41,730 --> 00:06:42,890
as you can see over here
85

86
00:06:43,230 --> 00:06:46,570
It would look somewhat like this if I am given the input.
86

87
00:06:46,860 --> 00:06:52,630
Now as you can see it has not got balanced because it has become of value.
87

88
00:06:52,740 --> 00:06:59,650
So I do not want my payload to become value so I'm going to take this out of the value tag.
88

89
00:07:00,150 --> 00:07:01,480
How do I take it out.
89

90
00:07:01,500 --> 00:07:05,870
I've seen there's this meta property tag gets closed like this.
90

91
00:07:06,000 --> 00:07:07,120
So I'm going to close it.
91

92
00:07:07,120 --> 00:07:15,990
here only into my input payload so my payload is now hacktify double quote slash closing brace and then
92

93
00:07:16,100 --> 00:07:17,730
the XSS payload.
93

94
00:07:17,730 --> 00:07:18,740
Perfect.
94

95
00:07:18,750 --> 00:07:21,200
Let's try to save this.
95

96
00:07:21,600 --> 00:07:28,700
Go to the browser and let's try to reload this and see if we're able to get the XSS execution or not
96

97
00:07:29,370 --> 00:07:30,020
if we get it.
97

98
00:07:30,270 --> 00:07:34,320
Then we have successfully balanced our XSS payload and it works perfectly fine.
98

99
00:07:35,160 --> 00:07:42,630
So yes when I reload this I have got the XSS execution which means we have successfully balanced
99

100
00:07:42,660 --> 00:07:44,440
our attack vector.
100

101
00:07:44,610 --> 00:07:45,600
Perfect.
101

102
00:07:45,600 --> 00:07:46,070
Let's go.
102

103
00:07:46,080 --> 00:07:51,830
Go to the third Web site in which we are going to see again XSS balancing.
103

104
00:07:52,470 --> 00:07:59,930
So in this I search for hacktify I'll go to the page source and I'm getting there for reflection.
104

105
00:07:59,940 --> 00:08:06,400
I'm going to just copy this go onto my notepad editor I'm going to paste it here and search for hacktify.
105

106
00:08:06,570 --> 00:08:12,300
As you can see this is the input which I searched for is getting reflected at only one position.
106

107
00:08:12,300 --> 00:08:13,320
Perfect.
107

108
00:08:13,320 --> 00:08:19,440
So here if I've given the input as an XSS payload with hacktify it would have looked somewhat like
108

109
00:08:19,440 --> 00:08:26,030
this script alert one script tag close and I wrote a extra script tag.
109

110
00:08:26,040 --> 00:08:27,540
Let me just delete this one
110

111
00:08:30,320 --> 00:08:30,650
yeah.
111

112
00:08:30,820 --> 00:08:33,720
So now it's perfect hacktify script.
112

113
00:08:33,760 --> 00:08:35,190
alert one script tag close.
113

114
00:08:35,200 --> 00:08:37,510
This is what the input will be given.
114

115
00:08:37,510 --> 00:08:40,660
Now it is not balanced case.
115

116
00:08:40,740 --> 00:08:44,050
So for balancing let me see how can I try to balance this.
116

117
00:08:44,500 --> 00:08:51,320
So let me go here and you can see that this is going to be get ended somewhere here.
117

118
00:08:51,340 --> 00:08:55,660
Script tag is getting closed so maybe a new script tag will start.
118

119
00:08:55,660 --> 00:08:59,500
And let me try to end the script tag over here only.
119

120
00:08:59,500 --> 00:09:08,700
So let's say if I end a script tag like this and script tag close and then execute the script.
120

121
00:09:08,880 --> 00:09:09,940
the XSS payloads.
121

122
00:09:10,000 --> 00:09:12,760
Let's try to go here and reload this perfect.
122

123
00:09:12,760 --> 00:09:16,150
We are getting an XSS execution over here.
123

124
00:09:16,360 --> 00:09:24,580
So yes we are able to execute this and we are able to successfully build an manual XSS attack
124

125
00:09:24,580 --> 00:09:25,590
vector.
125

126
00:09:25,690 --> 00:09:31,690
So I hope you guys understood that whenever onto any application if you're not able to get an XSS 
126

127
00:09:32,110 --> 00:09:35,860
maybe your Miss missing the most important thing that is balancing it.
127

128
00:09:36,520 --> 00:09:43,180
So this was one of the manual approach of balancing and XSS my looking at the page source.
128

129
00:09:43,630 --> 00:09:45,040
I hope this helps.
129

130
00:09:45,190 --> 00:09:46,960
And thank you.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,350 --> 00:00:02,730
Hello everyone.
1

2
00:00:02,730 --> 00:00:07,770
So in this video we are going to see one more case for XSS.
2

3
00:00:07,950 --> 00:00:11,700
And we will also see the balancing of the XSS.
3

4
00:00:11,700 --> 00:00:14,710
So as you can see there is a search parameter.
4

5
00:00:14,880 --> 00:00:23,430
I'm going to search into this parameter hacktify  and I will hit enter and you can see the parameter
5

6
00:00:23,430 --> 00:00:25,690
is getting reflected right.
6

7
00:00:25,710 --> 00:00:29,300
So I'm going to test for reflected XSS.
7

8
00:00:29,640 --> 00:00:37,020
So I will just give hacktify and the simple payload here as you can see script alert one script
8

9
00:00:37,040 --> 00:00:41,610
tag close and hit enter.
9

10
00:00:41,610 --> 00:00:50,440
As you can see our javascript payload did not execute something stopped the payload from executing.
10

11
00:00:50,670 --> 00:00:56,930
So let's see what stopped this from executing by opening the page source and let us search for hacktify
11

12
00:00:57,480 --> 00:01:00,500
to see where does it get reflected.
12

13
00:01:00,660 --> 00:01:07,540
As you can see it is getting reflected over here so there are total 66 matches where it is getting the
13

14
00:01:07,650 --> 00:01:08,310
reflected
14

15
00:01:14,030 --> 00:01:17,290
checking all of them.
15

16
00:01:17,360 --> 00:01:22,600
We realize that we need to balance our payload.
16

17
00:01:22,700 --> 00:01:29,440
There are total 66 reflection where hacktify  gets reflected right.
17

18
00:01:29,810 --> 00:01:38,640
So what I'm going to do right now is I am going to balance my payload.
18

19
00:01:38,930 --> 00:01:39,380
Yes.
19

20
00:01:39,410 --> 00:01:40,340
As you can see here
20

21
00:01:45,480 --> 00:01:52,330
if you will if you can look closely here you can see this gets ended by this.
21

22
00:01:52,340 --> 00:01:56,000
This whole place holder gets ended by this.
22

23
00:01:56,010 --> 00:02:05,310
So what I'm going to do is in the value parameter where my payload is getting input reflected I'm going
23

24
00:02:05,310 --> 00:02:13,650
to end this payload itself okay and make this payload come out of the value.
24

25
00:02:14,370 --> 00:02:18,430
So I'm going to end this by adding this empty start
25

26
00:02:30,530 --> 00:02:34,730
so let me just go back to the website and this time
26

27
00:02:37,970 --> 00:02:42,400
let me use a new payload and also try to balance it.
27

28
00:02:42,530 --> 00:02:47,570
So I'm using image source payload image source equals to X.
28

29
00:02:47,600 --> 00:02:49,130
Is there any source like that.
29

30
00:02:49,130 --> 00:02:49,910
No.
30

31
00:02:49,910 --> 00:02:51,770
This is invalid source.
31

32
00:02:51,860 --> 00:03:00,750
So the application will throw Error on and we have given on error confirm one
32

33
00:03:05,450 --> 00:03:13,750
okay and did not get reflected it got reflected but it did not got executed.
33

34
00:03:13,770 --> 00:03:20,310
So what we're going to do is as we saw into the page source we are going to balance it like this and
34

35
00:03:20,310 --> 00:03:21,450
we are going to hit enter.
35

36
00:03:22,200 --> 00:03:22,630
Yes.
36

37
00:03:22,650 --> 00:03:32,430
And you can see we got our alert which means we were successfully successfully able to execute the JS 
37

38
00:03:32,670 --> 00:03:37,400
and successfully able to exploit the XSS vulnerability.
38

39
00:03:37,410 --> 00:03:38,400
I hope you understood.
39

40
00:03:38,550 --> 00:03:39,030
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,380 --> 00:00:02,850
Hello everyone.
1

2
00:00:02,850 --> 00:00:08,520
So in this video we are going to see XSS in limited inputs.
2

3
00:00:08,750 --> 00:00:11,090
We will see how to do XSS.
3

4
00:00:11,220 --> 00:00:20,380
If the script tags are blocked into any web application so practical time and let let's see how can
4

5
00:00:20,380 --> 00:00:28,290
we bypass any website which is blocking a script tag as you can see I'm onto this website which has
5

6
00:00:28,290 --> 00:00:37,260
bata.in and so I will just go into the search bar and I will hit hacktify and enter this to check
6

7
00:00:37,350 --> 00:00:37,650
that.
7

8
00:00:37,650 --> 00:00:44,000
Is there any reflection and you can see there is a reflection happening so I'm going to try a reflected
8

9
00:00:44,040 --> 00:00:48,860
XSS over here.
9

10
00:00:49,440 --> 00:00:58,060
Now I'm going to take a very basic payload that is script alert one script tag close I'll just copy this
10

11
00:00:58,420 --> 00:01:07,270
go into the application type hacktify and enter the payload and hit enter as you can see 
11

12
00:01:07,270 --> 00:01:10,090
our pay;oad did not get executed.
12

13
00:01:10,090 --> 00:01:11,890
Let's see what happened.
13

14
00:01:11,890 --> 00:01:15,830
Go into the page source and search for hacktify.
14

15
00:01:16,540 --> 00:01:26,440
As you can see there is only hacktify and one where did our script start script end and  alert go.
15

16
00:01:26,440 --> 00:01:38,990
So we came to a conclusion that the developer has used stripping of the script tags so whenever any
16

17
00:01:38,990 --> 00:01:48,080
user gives the input of script tags the application will strip those script tags and also and strip
17

18
00:01:48,290 --> 00:01:51,870
the alert function.
18

19
00:01:52,130 --> 00:02:00,530
Okay so now we are going to not use script alert because it get stripped out.
19

20
00:02:00,530 --> 00:02:04,330
This is what the developers logic is.
20

21
00:02:04,850 --> 00:02:06,140
Let's go back.
21

22
00:02:06,470 --> 00:02:11,570
And now we are going to use a new payload that is image source equals to X..
22

23
00:02:11,900 --> 00:02:13,550
Is there any image source like this.
23

24
00:02:13,550 --> 00:02:13,810
No.
24

25
00:02:13,820 --> 00:02:20,690
There is no source like no source like X therefore it is going to give a error when it will try to load a image
25

26
00:02:20,750 --> 00:02:25,480
from a source that is X when it will give an error.
26

27
00:02:25,490 --> 00:02:30,730
We have written a function which says on error equals to confirm one why have we written confirm
27

28
00:02:30,980 --> 00:02:32,800
Why have the origin confirm.
28

29
00:02:32,810 --> 00:02:37,990
Because we saw already the application blocks the alert function.
29

30
00:02:38,420 --> 00:02:42,760
So that's why we have used to confirm do remember guys.
30

31
00:02:43,130 --> 00:02:48,970
Instead of alert we can use confirm as well as we can use prompt.
31

32
00:02:49,040 --> 00:02:57,840
So let's just take this payload go back to the website and give this payload and hit enter and let us
32

33
00:02:58,040 --> 00:03:09,140
observe yes successfully we have executed our javascript XSS payload into the website I hope you
33

34
00:03:09,140 --> 00:03:16,940
guys understood this we do that how we can bypass if any application is putting any stripping mechanism
34

35
00:03:16,970 --> 00:03:18,140
for any tanks.
35

36
00:03:18,140 --> 00:03:18,680
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,170 --> 00:00:02,640
Hello everyone.
1

2
00:00:02,640 --> 00:00:10,470
So in this video we are again going to see XSS in limited input wherein the web application that
2

3
00:00:10,470 --> 00:00:19,470
is carid.com is going to strip some part of our XSS payload and will try to block us from
3

4
00:00:19,680 --> 00:00:29,010
performing a XSS attack on the website but we will try to form a payload through which we are going
4

5
00:00:29,010 --> 00:00:34,600
to make a successful XSS attack on this website.
5

6
00:00:34,620 --> 00:00:40,740
So let's get started and let us see this into the search option.
6

7
00:00:40,740 --> 00:00:47,700
I'm going to type hacktify as you can see it is getting reflected onto the web application which means
7

8
00:00:48,060 --> 00:00:52,420
you can be a possibility of reflected XSS.
8

9
00:00:52,470 --> 00:00:56,370
So I'm going to hunt a reflected XSS here.
9

10
00:00:56,730 --> 00:01:03,960
I will just go there and give a simple payload that we know that a script alert one script tag close
10

11
00:01:05,130 --> 00:01:11,960
if you look closely into what is getting reflected here is only hacktify and alert.
11

12
00:01:12,390 --> 00:01:21,660
Which means this website developer has put a logic to strip any input which contains script tag open
12

13
00:01:21,780 --> 00:01:23,950
and script tag close.
13

14
00:01:24,120 --> 00:01:30,960
Therefore our this payload is not working on the application and we are not able to generate XSS 
14

15
00:01:31,050 --> 00:01:42,910
attack.
15

16
00:01:42,980 --> 00:01:49,340
So now we are going to bypass this by using another payload which does not contain a script tag.
16

17
00:01:50,540 --> 00:01:58,400
So we are going to use image source equals to X which is not a right source which is a malfunctioned
17

18
00:01:58,670 --> 00:01:59,240
source.
18

19
00:01:59,240 --> 00:02:01,400
There is no source like that.
19

20
00:02:01,400 --> 00:02:07,730
So the application when try to load our image from this source will give an error and we have told
20

21
00:02:07,730 --> 00:02:12,520
an application that on error function give a alert 
21

22
00:02:12,530 --> 00:02:21,860
That is 1 when I will just try to write this and hit enter and let's see what happens after hitting enter
22

23
00:02:22,010 --> 00:02:23,990
as we can observe onto the screen.
23

24
00:02:24,020 --> 00:02:30,130
There is going to be a alert as you have seen here the application tried to load an image.
24

25
00:02:30,200 --> 00:02:36,290
If you look closely here and the application was not able to load the image from our source that was
25

26
00:02:36,410 --> 00:02:43,310
X and the image was not able to get loaded and the application gave a error.
26

27
00:02:43,310 --> 00:02:47,960
That is one as you can see over here I hope you guys understood.
27

28
00:02:48,350 --> 00:02:49,580
Thank you for watching this.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,590 --> 00:00:03,090
Hello everyone.
1

2
00:00:03,090 --> 00:00:11,190
So in this video we are going to see how can we do XSS in request headers so we can do XSS 
2

3
00:00:11,220 --> 00:00:17,160
by giving the arbitrary javascript payload into the request headers.
3

4
00:00:17,160 --> 00:00:24,750
And if the application interpreted and executes it then the application is vulnerable to cross site
4

5
00:00:24,750 --> 00:00:26,930
scripting attack.
5

6
00:00:27,240 --> 00:00:33,590
You can choose any request headed for example we are going to choose a header that is a referer.
6

7
00:00:35,130 --> 00:00:44,400
No sanitization or decisions and taking decisions is very very dangerous for the application as you
7

8
00:00:44,400 --> 00:00:50,040
can see there is a header on this website when we perform the curl request.
8

9
00:00:50,250 --> 00:00:58,290
The header is X thanks for this awesome bug bounty course can also try a XSS  there so practical
9

10
00:00:58,290 --> 00:01:00,300
time and let us see this in action
10

11
00:01:03,420 --> 00:01:04,490
yes.
11

12
00:01:04,590 --> 00:01:08,070
So as you can see I went to a website which is media dot net
12

13
00:01:11,030 --> 00:01:14,240
I will just quickly capture this request into my burpsuite
13

14
00:01:25,050 --> 00:01:27,630
as you can see I have captured the request and Burpsuite.
14

15
00:01:27,660 --> 00:01:34,940
I will send this request to repeater after sending this into the repeater tab.
15

16
00:01:35,130 --> 00:01:41,280
I'm going to hit go and I'm going to check the response as you can see in the request I'm going to
16

17
00:01:41,280 --> 00:01:45,510
change the request method from get to post
17

18
00:01:49,230 --> 00:01:53,580
and now I'm going to add a new header that is a refrer headers
18

19
00:01:57,940 --> 00:02:05,070
and in the reference header I'm going to type as https://google.com and I just want to check that
19

20
00:02:05,190 --> 00:02:09,500
this Google gets reflected into the response or not with a question mark.
20

21
00:02:09,600 --> 00:02:10,020
Yes.
21

22
00:02:10,410 --> 00:02:14,900
So this header is getting reflected into the response.
22

23
00:02:15,510 --> 00:02:22,620
So let me give a parameter equals to value like Q parameter and the value hacktify and let's verify
23

24
00:02:22,800 --> 00:02:24,580
does this get reflected.
24

25
00:02:24,630 --> 00:02:25,680
Perfect.
25

26
00:02:25,680 --> 00:02:27,690
This is getting reflected into the response.
26

27
00:02:27,690 --> 00:02:33,290
Also as you can notice this is a hidden response.
27

28
00:02:33,510 --> 00:02:43,560
Now I can see that this gets ended by double quotes forward slash closing bracket so I'm going to balance
28

29
00:02:43,560 --> 00:02:47,580
my payload like this and I'm going to put a payload
29

30
00:02:51,480 --> 00:03:04,080
so a double quote slash and I'm going to give my payload as script alert one script tag close I will
30

31
00:03:04,080 --> 00:03:07,910
just hit go and check if this is getting reflected or not
31

32
00:03:12,280 --> 00:03:17,720
as we can see we have successfully balanced this and this is getting reflected into the response it would
32

33
00:03:17,720 --> 00:03:26,840
just right click show response in browser and let me go to the browser before putting this let me open
33

34
00:03:26,840 --> 00:03:35,810
up a new tab yes and paste it and you can see how I'm able to get a XSS through the request headers
34

35
00:03:36,260 --> 00:03:44,120
I hope you guys understood how I was able to do a XSS by using a header that was a referrer thank
35

36
00:03:44,120 --> 00:03:44,330
you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,140 --> 00:00:02,610
Hello everyone.
1

2
00:00:02,610 --> 00:00:11,420
So in this video we are going to see how can we perform XSS in the user agent and also save our payload
2

3
00:00:11,570 --> 00:00:16,700
into the caching server attacking many people at one time.
3

4
00:00:16,770 --> 00:00:23,160
So basically we are going to perform XSS as attacking the user agent and will make the caching that
4

5
00:00:23,160 --> 00:00:26,140
were save it into the cache.
5

6
00:00:26,250 --> 00:00:33,390
So anyone who visits that particular U.R.L. will automatically get attacked by our attack vector until
6

7
00:00:33,390 --> 00:00:35,850
the cache is flushed.
7

8
00:00:35,850 --> 00:00:40,670
So we will attack the website using XSS and user agent in the web application.
8

9
00:00:40,680 --> 00:00:46,350
We will also see what a payload into the caching server in the form of miss and hit.
9

10
00:00:46,350 --> 00:00:49,800
We are going to understand this in the practical.
10

11
00:00:50,100 --> 00:00:56,700
Whenever anyone visits the U.R.L. which is cached by the server in this case there is a.
11

12
00:00:56,730 --> 00:01:07,620
So sukuri based caching server and it will lead to XSS XSS will remain into the cachingserver
12

13
00:01:07,770 --> 00:01:13,390
until the cache is flushed so practical time.
13

14
00:01:13,480 --> 00:01:25,100
And let's see the practical that how can we perform this attack into the user agent and poison the cache.
14

15
00:01:25,270 --> 00:01:31,600
So yes let me open up my terminal quickly and on the terminal.
15

16
00:01:31,780 --> 00:01:33,540
I'm going to type the command.
16

17
00:01:33,550 --> 00:01:34,460
That is curl.
17

18
00:01:35,380 --> 00:01:36,200
OK.
18

19
00:01:36,460 --> 00:01:43,360
After typing curl I'm going to give the target my target is brute logic dot com dot br slash lab
19

20
00:01:43,360 --> 00:01:46,890
slash header dot php OK.
20

21
00:01:47,110 --> 00:01:50,310
I will just give a question mark Rohit
21

22
00:01:54,620 --> 00:01:55,550
yes.
22

23
00:01:55,880 --> 00:02:00,930
After giving this question mark Rohit I'm going to hit enter.
23

24
00:02:01,010 --> 00:02:08,150
So basically I'm going to see the response as you can see this is the response that I'm getting.
24

25
00:02:08,150 --> 00:02:14,570
I will just do -I just to see the headers not the response.
25

26
00:02:14,590 --> 00:02:21,770
So I want to see what are the headers coming so we can see the headers are server nginx date content
26

27
00:02:21,770 --> 00:02:29,820
type x-sukuri-id because there is a sukuri WAF and caching server x-sukuri-cache
27

28
00:02:29,840 --> 00:02:34,450
So basically this request is not saved in the into the caching server.
28

29
00:02:34,490 --> 00:02:42,050
That's why it is saying cache missed if this request would be coming from the cache then it would say cache
29

30
00:02:42,230 --> 00:02:42,680
hit.
30

31
00:02:43,160 --> 00:02:49,790
So now Miss Means this is not saved into the caching server  but now it will get saved automatically.
31

32
00:02:49,790 --> 00:02:51,440
So let me again make the request
32

33
00:02:54,600 --> 00:02:58,740
and this time let's observe what happens.
33

34
00:02:58,740 --> 00:02:59,670
Perfect.
34

35
00:02:59,670 --> 00:03:05,190
So this time this request is coming from the cached server from the sukuri server.
35

36
00:03:05,670 --> 00:03:06,750
Awesome.
36

37
00:03:06,750 --> 00:03:17,810
So let's move further and let's try to poison the cache by giving arbitrary header.
37

38
00:03:17,970 --> 00:03:25,690
So let's say we give a header we which is called as XSS and let me type a simple basic payload here
38

39
00:03:25,760 --> 00:03:30,450
lets say SVG onload alert zero.
39

40
00:03:31,780 --> 00:03:35,310
OK so let me try to hit enter and let's see what happens.
40

41
00:03:36,000 --> 00:03:37,490
So it is saying hit.
41

42
00:03:37,970 --> 00:03:38,820
OK.
42

43
00:03:39,070 --> 00:03:43,150
So this payload is not saved.
43

44
00:03:43,500 --> 00:03:44,820
Again it is giving hit.
44

45
00:03:44,970 --> 00:03:47,370
Let me try one more time.
45

46
00:03:47,460 --> 00:03:49,750
Again it is giving hit.
46

47
00:03:49,890 --> 00:03:52,050
Let me try it one more time.
47

48
00:03:52,170 --> 00:03:52,460
Yes.
48

49
00:03:52,470 --> 00:03:58,520
So again it is getting hit which means I am getting the response from the caching server only till now.
49

50
00:03:58,590 --> 00:04:03,270
And this user agent is not being saved into the application.
50

51
00:04:03,270 --> 00:04:10,270
Let's verify by going onto the browser as you can see nothing is coming onto my browser.
51

52
00:04:10,440 --> 00:04:13,240
No XSS prompt or alert.
52

53
00:04:13,890 --> 00:04:22,290
So what I'm going to do is I am going to save a new end point into the caching server this time.
53

54
00:04:22,380 --> 00:04:31,060
So let's say instead of Rohit I give Rohit1 and hit enter so let me just hit enter.
54

55
00:04:33,040 --> 00:04:35,920
And now you can observe.
55

56
00:04:36,010 --> 00:04:37,230
Perfect.
56

57
00:04:37,270 --> 00:04:44,320
The cache has missed this time which means that this request is being saved into the caching server
57

58
00:04:44,530 --> 00:04:47,600
this time because we are not getting ahead.
58

59
00:04:47,620 --> 00:04:53,890
We are getting a miss the cache has missed and this request has been will be now saved by the caching
59

60
00:04:53,890 --> 00:04:54,590
server.
60

61
00:04:54,590 --> 00:04:56,250
Let us verify.
61

62
00:04:56,350 --> 00:05:01,610
Let's give the same request again and this time we should get a cache hit.
62

63
00:05:02,050 --> 00:05:05,300
So let's check if we get a cache hit.
63

64
00:05:05,620 --> 00:05:06,430
We got a Miss
64

65
00:05:10,030 --> 00:05:12,640
let's try one more time.
65

66
00:05:12,640 --> 00:05:13,460
Perfect.
66

67
00:05:13,510 --> 00:05:14,140
Perfect.
67

68
00:05:14,680 --> 00:05:15,270
Yes.
68

69
00:05:15,340 --> 00:05:20,990
So we are able to make this payload save into the caching server.
69

70
00:05:21,790 --> 00:05:28,910
Yes let's verify by sending a request to the end point.
70

71
00:05:28,930 --> 00:05:29,800
Let let's verify.
71

72
00:05:30,280 --> 00:05:36,130
So I am sending a request to the end point and let's verify we have got output and perfet in the
72

73
00:05:36,130 --> 00:05:36,710
body.
73

74
00:05:36,730 --> 00:05:45,130
Can you see our arbitrary XSS header has been added into that end point because this response is
74

75
00:05:45,130 --> 00:05:47,080
coming from the caching server.
75

76
00:05:47,130 --> 00:05:49,960
Let us go onto the website and let's test this.
76

77
00:05:49,960 --> 00:05:51,230
Let me just do Rohit1
77

78
00:05:51,240 --> 00:05:55,810
hit enter and now you guys observe what happens.
78

79
00:05:55,980 --> 00:05:56,910
Okay.
79

80
00:05:58,000 --> 00:06:00,610
So perfect.
80

81
00:06:00,610 --> 00:06:06,810
We have got a alert onto the screen which means we have successfully demonstrated an XSS .
81

82
00:06:06,860 --> 00:06:15,380
And if I will send this request to anyone then he will get a XSS onto his computer.
82

83
00:06:15,460 --> 00:06:22,630
So basically you were able to exploit XSS in the user agent also we are able to store our payload
83

84
00:06:22,840 --> 00:06:24,710
into the caching server.
84

85
00:06:24,730 --> 00:06:32,180
Now this is stored in the caching server until the cache automatically flushes itself and makes new cache.
85

86
00:06:32,230 --> 00:06:36,820
I hope you guys understood in this video how we exploited it.
86

87
00:06:37,480 --> 00:06:38,560
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,970 --> 00:00:03,720
Hello everyone.
1

2
00:00:04,320 --> 00:00:12,260
So in this video we are going to see XSS in e-mail login fields with limited input.
2

3
00:00:12,250 --> 00:00:21,240
So here we are going to attack the website using the XSS into the login field to be specific into the
3

4
00:00:21,250 --> 00:00:22,350
e-mail field.
4

5
00:00:22,350 --> 00:00:25,260
In any web application.
5

6
00:00:25,260 --> 00:00:29,770
So according to RFC822 e-mail address validator.
6

7
00:00:29,880 --> 00:00:39,440
We will make our own payload and we will try to attack into the e-mail field of any login page.
7

8
00:00:39,750 --> 00:00:46,620
If we are able to do so and if we achieve XSS then it is a win win condition for us.
8

9
00:00:46,620 --> 00:00:48,360
So it's the practical time.
9

10
00:00:48,360 --> 00:00:57,350
And let's quickly see the practical for this attack.
10

11
00:00:57,920 --> 00:01:06,800
So for doing the attack first let's go to the e-mail address validated and let me try to submit an e-mail
11

12
00:01:06,800 --> 00:01:07,720
address here.
12

13
00:01:07,760 --> 00:01:16,490
So let's say if I type Rohit or let's say I type hacker.udemy@gmail.com 
13

14
00:01:17,390 --> 00:01:25,400
and sorry gmail.com and click on check it can see this is the e-mail address validator
14

15
00:01:26,120 --> 00:01:36,020
and it is saying this is a valid e-mail in effect a hacker or let's say like this script alert one
15

16
00:01:36,530 --> 00:01:46,310
script  close or alert ones script tag close and try and check.
16

17
00:01:46,310 --> 00:01:49,010
So it is going to say it is invalid.
17

18
00:01:49,010 --> 00:01:51,480
This is not a valid payload.
18

19
00:01:51,650 --> 00:01:54,020
What if it give another payload that is
19

20
00:01:54,020 --> 00:01:57,560
image src equals to x onerror equals to
20

21
00:01:57,770 --> 00:01:59,620
confirm
21

22
00:01:59,690 --> 00:02:07,170
Let's say one and this time I give @gmail.com let's see what happens.
22

23
00:02:07,190 --> 00:02:13,220
Yep it is again detecting that this is a invalid e-mail.
23

24
00:02:13,220 --> 00:02:20,360
So for this I am going to give a payload here which will bypass this.
24

25
00:02:20,360 --> 00:02:26,980
So let's see this in this payload you can see I'm giving this payload and I'm going to hit on check.
25

26
00:02:27,230 --> 00:02:29,900
So let's check this perfect
26

27
00:02:30,170 --> 00:02:33,890
So according to the RFC822 email address validator.
27

28
00:02:33,890 --> 00:02:39,390
This is a valid e-mail address which is a payload till here.
28

29
00:02:39,680 --> 00:02:44,970
And this is the domain that is @gmail.com look alike.
29

30
00:02:45,110 --> 00:02:45,620
Perfect.
30

31
00:02:45,620 --> 00:02:51,920
So now we're going to see and we are going to check this payload and we're going to see if we're able
31

32
00:02:51,920 --> 00:02:55,400
to exploit any website using this payload.
32

33
00:02:55,400 --> 00:03:00,790
So for the attack perspective we are going to go into this website.
33

34
00:03:01,430 --> 00:03:06,500
Perfect as you can see there is a field of user name and password.
34

35
00:03:06,500 --> 00:03:11,780
So when the user name field I'm gaoing to give my payload and in the password field let's say I type
35

36
00:03:11,840 --> 00:03:13,060
anything randomly.
36

37
00:03:13,190 --> 00:03:22,180
So let me just type admin123 and I'm going to hit submit before submitting this request.
37

38
00:03:22,970 --> 00:03:28,970
I want you guys to understand that if we give anything else into the user name field it is going to
38

39
00:03:28,970 --> 00:03:30,970
give our input validation error.
39

40
00:03:31,400 --> 00:03:38,330
So if you try to put a simple script alert 1 payload into the input field it is going to validate that
40

41
00:03:38,450 --> 00:03:44,660
and it is going to say that this is not the right e-mail address because there is a validation which
41

42
00:03:44,660 --> 00:03:51,400
is put into place by the developer according to RFC822 email validator.
42

43
00:03:51,590 --> 00:03:57,770
But as we saw that this payload is able to bypass that e-mail validation and now we are going to try
43

44
00:03:58,160 --> 00:04:05,360
with this payload and check that if this payload is working onto this website or not we can also check
44

45
00:04:05,360 --> 00:04:10,140
this payload on different different Web sites which contain email-id and password.
45

46
00:04:10,130 --> 00:04:13,400
So let's try to submit this now and verify.
46

47
00:04:13,820 --> 00:04:17,910
So let up let us submit this and see what happens.
47

48
00:04:17,930 --> 00:04:21,040
So I've clicked on submit and perfect.
48

49
00:04:21,560 --> 00:04:22,070
Yes.
49

50
00:04:22,280 --> 00:04:27,500
So can you see that the application has executed or what payload.
50

51
00:04:27,500 --> 00:04:30,360
Which means the e-mail address field.
51

52
00:04:30,380 --> 00:04:38,990
There was there was vulnerable to this attack and we have successfully made a cross site scripting attack
52

53
00:04:39,350 --> 00:04:43,430
into the e-mail field with limited inputs.
53

54
00:04:43,490 --> 00:04:45,970
I hope everyone understood.
54

55
00:04:45,980 --> 00:04:46,550
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,660 --> 00:00:01,890
Hello everyone.
1

2
00:00:01,890 --> 00:00:11,070
So in this video we are going to see how can we do XSS protection bypass by doing a base 64 encoding
2

3
00:00:11,100 --> 00:00:14,320
and decoding of our payload.
3

4
00:00:14,550 --> 00:00:21,300
So here in we are going to see your application which is protected by XSS attacks.
4

5
00:00:21,300 --> 00:00:28,020
And if you try to do an XSS attack the application will just block us but we are going to bypass
5

6
00:00:28,020 --> 00:00:36,320
that by using base64 encoding and we will successfully execute our XSS attack.
6

7
00:00:36,330 --> 00:00:43,350
We will bypass an XSS where there is improper input sanitization or proper HTML encoding
7

8
00:00:44,490 --> 00:00:48,660
the application as proper checks for other XSS payloads and blocks it.
8

9
00:00:48,990 --> 00:00:56,370
But that is improper encoding or escaping and taking decisions based on this is very very dangerous.
9

10
00:00:58,770 --> 00:01:04,220
So it is practical time and let's see how can we do this type of XSS.
10

11
00:01:04,260 --> 00:01:04,920
Attacks
11

12
00:01:08,720 --> 00:01:09,200
Yes
12

13
00:01:11,990 --> 00:01:15,500
so you can see my target is droom.in
13

14
00:01:16,430 --> 00:01:24,600
So what I'm going to do is I searched for hacktify as you can see parameters q equals to hacktify.
14

15
00:01:25,160 --> 00:01:33,290
I'm just going to put a simple payload there quickly just to show you guys that there is a WAF which
15

16
00:01:33,440 --> 00:01:37,460
is blocking me right now as you can see Access Denied
16

17
00:01:40,740 --> 00:01:46,400
so I cannot do an XSS on this search parameter that is q.
17

18
00:01:47,190 --> 00:01:53,670
So what I'm going to do right now is I have logged in into the application after logging it into the
18

19
00:01:53,730 --> 00:02:01,020
application I will just go choose any car and go into the cars dashboard
19

20
00:02:07,820 --> 00:02:09,650
so let me just wait
20

21
00:02:14,800 --> 00:02:16,960
try to intercept this request.
21

22
00:02:17,380 --> 00:02:17,920
Yes.
22

23
00:02:18,430 --> 00:02:26,620
So I will just have intercepted this request and you can see the request contain something called Get
23

24
00:02:26,710 --> 00:02:32,540
dashboard because I have logged in into the dashboard and source equals to a very long string.
24

25
00:02:32,740 --> 00:02:35,760
And that's going to take this long string send it to the decoder
25

26
00:02:38,850 --> 00:02:45,300
so I've sanded it to the decoder and you can see after decoding it clicking on base64
26

27
00:02:49,550 --> 00:02:52,730
oops! are let me just try to decode it again.
27

28
00:02:52,730 --> 00:02:53,870
Wait no.
28

29
00:02:54,020 --> 00:02:55,910
So let me just click back on.
29

30
00:02:55,930 --> 00:02:56,240
Yeah.
30

31
00:02:56,690 --> 00:03:03,380
So as you can see this string contains Yeah.
31

32
00:03:03,430 --> 00:03:04,410
Let me just decoded.
32

33
00:03:04,420 --> 00:03:05,500
Yes to this.
33

34
00:03:05,950 --> 00:03:10,970
This long string contains base64 encoded values.
34

35
00:03:11,020 --> 00:03:21,280
As you can see the base 64 encoded values are these make equals to Tata, model equals to nano, Gen-X.
35

36
00:03:21,460 --> 00:03:24,670
Year equals to 2015 trim Xt location.
36

37
00:03:24,670 --> 00:03:31,950
This this and I'm and in the location parameter I'm gaoing to give my payload as you can see I view
37

38
00:03:31,950 --> 00:03:39,320
in the payload as chandigarh and balance the script script alert one script tag close so I'm going
38

39
00:03:39,330 --> 00:03:40,720
to give this payload
39

40
00:03:45,650 --> 00:03:50,420
OK so what I'm going to do is I'm going to just remove this and add it to here
40

41
00:03:55,230 --> 00:03:59,700
so let's just verify the application blocks our blocks us or not.
41

42
00:03:59,760 --> 00:04:02,150
The application is not blocking us.
42

43
00:04:02,470 --> 00:04:07,410
Let's go back to the dashboard and let's try to verify if we're able to do XSS 
43

44
00:04:12,500 --> 00:04:14,810
so let's wait for it to load.
44

45
00:04:15,110 --> 00:04:18,800
And if we get a alert then the website is vulnerable to XSS 
45

46
00:04:25,470 --> 00:04:25,880
okay.
46

47
00:04:25,910 --> 00:04:29,010
So let's go back to the repeater tab.
47

48
00:04:29,490 --> 00:04:32,070
Let's see what mistake we did.
48

49
00:04:32,120 --> 00:04:39,040
So let me just try to copy this payload again going to the repeater tab and replace this.
49

50
00:04:39,170 --> 00:04:43,500
So if I try to put a base64 encoded payload it is not happening.
50

51
00:04:43,760 --> 00:04:46,660
So I did base64 to url encode.
51

52
00:04:48,130 --> 00:04:49,090
Okay.
52

53
00:04:49,520 --> 00:04:53,350
So after doing it you are all encoding now.
53

54
00:04:53,540 --> 00:04:54,560
It may tend to work.
54

55
00:04:54,650 --> 00:04:58,550
Let me just hit on go and it can see it was 200.
55

56
00:04:58,570 --> 00:04:58,980
Okay.
56

57
00:04:59,000 --> 00:05:00,330
Into the response.
57

58
00:05:00,590 --> 00:05:01,280
I did not got
58

59
00:05:01,290 --> 00:05:04,520
BLOCK Let me just paste it into the browser and.
59

60
00:05:04,540 --> 00:05:06,340
Perfect.
60

61
00:05:06,410 --> 00:05:07,530
Can you see.
61

62
00:05:07,550 --> 00:05:08,330
Yes.
62

63
00:05:08,480 --> 00:05:14,270
We are able to bypass the protection by doing a base 64 encoding and then url encoding of our
63

64
00:05:14,270 --> 00:05:14,810
payload.
64

65
00:05:15,560 --> 00:05:21,060
And we were able to bypass the block that was happening onto this website.
65

66
00:05:21,560 --> 00:05:30,260
So this was an very interesting scenario of how we can achieve XSS in base by doing base64 encoding
66

67
00:05:30,290 --> 00:05:31,920
and you are encoding.
67

68
00:05:32,150 --> 00:05:33,410
I hope you guys understood.
68

69
00:05:33,410 --> 00:05:34,510
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,500 --> 00:00:03,080
Hello everyone.
1

2
00:00:03,090 --> 00:00:10,300
So in this we do we are going to see a XSS prediction bypass on a bank website.
2

3
00:00:10,770 --> 00:00:18,360
So we will bypass an XSS where there is improper input sanitization on HTML encoding with
3

4
00:00:18,360 --> 00:00:19,510
limited inputs.
4

5
00:00:21,210 --> 00:00:28,980
So in this example we are waiting to see how we were able to perform XSS attack onto a bank website
5

6
00:00:29,880 --> 00:00:37,970
and the payload is going to be very very tiny because of limited input into the website.
6

7
00:00:37,980 --> 00:00:43,170
So it is practical time and let's see how we can achieve this exercise.
7

8
00:00:45,930 --> 00:00:46,470
Yes.
8

9
00:00:47,010 --> 00:00:49,740
So let's quickly see this.
9

10
00:00:49,750 --> 00:00:52,260
So the website is ICICI Bank.
10

11
00:00:52,320 --> 00:00:54,190
careers dot com.
11

12
00:00:54,210 --> 00:01:03,480
Now I will just go into the search and apply feature wherein I'm willing to apply for a career into
12

13
00:01:03,480 --> 00:01:06,580
this website as you can see
13

14
00:01:06,600 --> 00:01:10,060
There is option of keyword job keyword search.
14

15
00:01:10,500 --> 00:01:14,280
So I'm going to type hacktify there and I am going to search
15

16
00:01:17,800 --> 00:01:19,110
as soon as I click on Search.
16

17
00:01:19,120 --> 00:01:23,470
You can see there is a reflection into the url perfect.
17

18
00:01:23,530 --> 00:01:25,720
So we have found a reflection.
18

19
00:01:25,780 --> 00:01:27,580
Now let me just go into the Burp suite
19

20
00:01:31,450 --> 00:01:36,640
let me just go into the Burpsuite and take this request into the burp
20

21
00:01:40,000 --> 00:01:45,300
as you can see it is coming empty because we did not give anything.
21

22
00:01:45,670 --> 00:01:47,980
So let me just send this to repeater
22

23
00:02:01,250 --> 00:02:09,980
let me just type again and let me take this yup so you can see how hacktify is something which is
23

24
00:02:09,980 --> 00:02:11,460
getting reflected.
24

25
00:02:11,460 --> 00:02:15,540
So instead of empty I'm going to type hacktify
25

26
00:02:15,650 --> 00:02:16,790
Perfect.
26

27
00:02:16,900 --> 00:02:21,160
Now I will hit go and I will see the reflection into the response.
27

28
00:02:21,230 --> 00:02:24,860
So I'm getting a reflection of two matches.
28

29
00:02:24,860 --> 00:02:25,430
Perfect.
29

30
00:02:27,920 --> 00:02:31,220
So this is the first and this is the second one.
30

31
00:02:31,220 --> 00:02:32,190
Fine.
31

32
00:02:32,270 --> 00:02:38,070
So what I'm going to do is the first thing that comes to my mind mind is putting a payload.
32

33
00:02:38,250 --> 00:02:38,580
Okay.
33

34
00:02:38,600 --> 00:02:46,060
So I've already balanced this payload from seeing from here and I'm putting the payload of script alert one
34

35
00:02:46,070 --> 00:02:48,170
script tag close
35

36
00:02:51,500 --> 00:03:00,870
and I will hit go and when I will do this you can see the application is not allowing me to do this.
36

37
00:03:00,980 --> 00:03:03,080
It is giving bad request.
37

38
00:03:03,080 --> 00:03:03,800
No problem.
38

39
00:03:03,800 --> 00:03:11,270
I'm going to use another payload that is a image source equals to X on error confirm one which in this
39

40
00:03:11,270 --> 00:03:17,110
payload we have given an arbitrary image source that is X and no such source exists.
40

41
00:03:17,120 --> 00:03:26,480
So the application is going to give an error and we have said on error confirm with one and said go
41

42
00:03:27,740 --> 00:03:28,380
No.
42

43
00:03:28,460 --> 00:03:34,130
The application is still giving a error which means how can we achieve a XSS .
43

44
00:03:34,130 --> 00:03:39,010
Now that was basically we tried to put anything the application blocks us.
44

45
00:03:39,230 --> 00:03:43,610
I tried here base64 encoding also the application blocks me.
45

46
00:03:43,610 --> 00:03:46,060
So I tried everything the application was blocking me.
46

47
00:03:46,790 --> 00:03:54,680
So as you can see now I just put the double quotes and the closing bracket just to check the application
47

48
00:03:54,710 --> 00:03:58,640
is validating this I'm not able to perform any type of
48

49
00:04:01,250 --> 00:04:07,160
XSS payload I'm not able to form XSS as payload in here as you can see it is giving me bad request
49

50
00:04:07,160 --> 00:04:09,160
for anything that I'm giving.
50

51
00:04:09,170 --> 00:04:16,560
So what if I tried to give single quote and let's verify if this payload works or not.
51

52
00:04:16,640 --> 00:04:19,850
So I will just go and you can see.
52

53
00:04:19,920 --> 00:04:21,090
Perfect.
53

54
00:04:21,170 --> 00:04:22,180
I got a 200.
54

55
00:04:22,190 --> 00:04:22,540
Okay.
55

56
00:04:22,550 --> 00:04:23,660
In my response.
56

57
00:04:23,750 --> 00:04:26,120
And it did not block me.
57

58
00:04:26,210 --> 00:04:32,090
So let's see the reflections first reflection here and your second reflection here.
58

59
00:04:32,300 --> 00:04:34,550
So let's just quickly do this.
59

60
00:04:34,580 --> 00:04:38,160
show response and browser and pasted here.
60

61
00:04:38,240 --> 00:04:42,020
And let's see this.
61

62
00:04:42,020 --> 00:04:51,740
And perfect yes you can see we were able to do XSS onto this website successfully.
62

63
00:04:52,040 --> 00:05:01,220
So this was an XSS in which we were able to bypass the protection that the developer has kept as
63

64
00:05:01,220 --> 00:05:07,210
by mitigating all the double quotes script tags base 64 encoding anything.
64

65
00:05:07,790 --> 00:05:08,470
Right.
65

66
00:05:08,480 --> 00:05:14,150
And also there was a limited input and a very small payload that we used into this attack.
66

67
00:05:14,150 --> 00:05:15,740
I hope you guys understood.
67

68
00:05:15,740 --> 00:05:16,270
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,580 --> 00:00:04,380
Hello everyone.
1

2
00:00:04,380 --> 00:00:10,820
So in this video we are going to learn how can we find XSS by using spiders.
2

3
00:00:12,000 --> 00:00:21,630
So if we do not get any parameter directly from the application sometimes what will happen is you will
3

4
00:00:21,630 --> 00:00:25,680
not be able to see any parameters directly.
4

5
00:00:25,680 --> 00:00:27,960
Many parameters will not be visible to you.
5

6
00:00:28,680 --> 00:00:36,550
So in that case what you can do is you can find a lot of parameters using Burpsuite.
6

7
00:00:36,930 --> 00:00:38,440
How to Find parameters.
7

8
00:00:38,820 --> 00:00:41,780
And that's going to show using Burpsuite.
8

9
00:00:41,850 --> 00:00:48,510
So we will find injection point from those parameters using the spider feature.
9

10
00:00:50,190 --> 00:00:57,870
And then after finding the injection point we are going to inject the XSS payload in the param and Boom!
10

11
00:00:57,900 --> 00:01:02,890
we will be able to exploit the XSS.
11

12
00:01:02,940 --> 00:01:09,420
So let's see the proof of concept as this is the practical time.
12

13
00:01:09,480 --> 00:01:09,960
Let's see
13

14
00:01:14,420 --> 00:01:19,640
so for doing this attack we have chosen this Web site that this is optimizely.com.
14

15
00:01:20,510 --> 00:01:24,310
So this is a website which is active on bugcrowd.
15

16
00:01:24,470 --> 00:01:26,390
So we have targeted this Web site.
16

17
00:01:26,490 --> 00:01:29,200
So let's see this in action.
17

18
00:01:29,240 --> 00:01:36,350
So what I'm going to do is as you can see under the screen there is no input field I can see anywhere.
18

19
00:01:36,350 --> 00:01:40,430
So where to put my XSS payload I cannot see any input field.
19

20
00:01:40,730 --> 00:01:47,930
So what I'm going to do is I'm going to run a Burp Spider and I'm going to crawl this Web site and get
20

21
00:01:48,620 --> 00:01:51,320
parameters or injection point.
21

22
00:01:53,600 --> 00:02:00,520
So I'm going to reload this website and this and this request will come into my burp.
22

23
00:02:00,710 --> 00:02:03,490
I will just click on send to spider.
23

24
00:02:03,500 --> 00:02:05,510
It will ask me to add in scope.
24

25
00:02:05,870 --> 00:02:08,140
So I want to add this into scope also.
25

26
00:02:08,420 --> 00:02:12,350
I want to log everything for the proxy history so I will hit.
26

27
00:02:12,380 --> 00:02:13,820
Yes.
27

28
00:02:13,820 --> 00:02:14,220
All right.
28

29
00:02:14,240 --> 00:02:16,130
Also I will send this to repeater.
29

30
00:02:16,130 --> 00:02:25,130
So in case I want to use this request again as you can see I will go to the target site map window and
30

31
00:02:25,130 --> 00:02:30,810
now my target's name is w w w dot optimized dot com.
31

32
00:02:31,010 --> 00:02:36,290
So I'm going to check with www.optimislycom right and I'm going
32

33
00:02:36,290 --> 00:02:43,850
to add this to scope as this has already added to scope I will just click on the filter and click on
33

34
00:02:44,180 --> 00:02:47,000
Show only in scope items.
34

35
00:02:47,000 --> 00:02:51,290
So I just want to see what are the items which are in scope.
35

36
00:02:51,290 --> 00:02:58,490
So this is my only one Web site which I'm going to work on right now and all other sites which I'm going
36

37
00:02:58,490 --> 00:03:03,470
to serve in the background will not be able to seen onto my site map window.
37

38
00:03:04,470 --> 00:03:08,750
Okay so we do this basically not to get confused.
38

39
00:03:08,750 --> 00:03:12,840
We're putting a lot of things into the scope as now.
39

40
00:03:12,840 --> 00:03:15,080
And I just want to work onto this target.
40

41
00:03:15,110 --> 00:03:20,320
So I just want to view all the request and response of this target only.
41

42
00:03:21,590 --> 00:03:28,920
Yes so now you can see there are a lot of requests that are coming.
42

43
00:03:28,920 --> 00:03:33,830
I will just double click on the params , params means parameters.
43

44
00:03:34,140 --> 00:03:39,980
So use you can see all the url that contains the parameters will come here
44

45
00:03:40,860 --> 00:03:41,480
OK.
45

46
00:03:41,580 --> 00:03:48,600
So the Burp spider is happening and the spider is crawling the web application and it is trying to find
46

47
00:03:48,600 --> 00:03:57,270
out more and more parameters in just some minutes 10 to 15 minutes it will able to crawl everything
47

48
00:03:57,360 --> 00:03:59,340
and it will find a lot of parameters.
48

49
00:04:00,600 --> 00:04:09,460
So I already done this crawling because I do not want to exceed the timing of this video
49

50
00:04:09,600 --> 00:04:14,400
So I will just tell you that what parameter I found out using Burp crawl.
50

51
00:04:15,330 --> 00:04:18,910
So the parameter was q=
51

52
00:04:19,110 --> 00:04:27,960
So I found this parameter and I'm just going to type hacktify in q parameter just to check that does
52

53
00:04:28,020 --> 00:04:30,460
it get reflected or not.
53

54
00:04:30,480 --> 00:04:32,650
So let me just quickly go into the page source
54

55
00:04:36,060 --> 00:04:40,340
and verify even is even hacktify getting reflected.
55

56
00:04:40,560 --> 00:04:42,840
Yes I got two reflections.
56

57
00:04:43,290 --> 00:04:47,040
Perfect.
57

58
00:04:47,220 --> 00:04:58,720
So now I'm going to give my payload that is script alert 1 and script tag close so let's see if we get
58

59
00:04:58,720 --> 00:05:01,530
XSS and we are waiting for the XSS prompt.
59

60
00:05:01,580 --> 00:05:04,860
But no we did not get why.
60

61
00:05:04,880 --> 00:05:06,890
Let's check.
61

62
00:05:06,890 --> 00:05:08,480
So as you can see it is got.
62

63
00:05:08,480 --> 00:05:13,130
url encoded here and here we can see perfectly fine.
63

64
00:05:13,130 --> 00:05:21,700
The payload is here Awesome but guys as you can see over be has become a value.
64

65
00:05:21,970 --> 00:05:24,120
What payload has become a value.
65

66
00:05:24,200 --> 00:05:26,900
But we do not want our payload to become value.
66

67
00:05:26,900 --> 00:05:29,590
We wanted to come outside of the value.
67

68
00:05:30,560 --> 00:05:37,280
So now what we're going to do is we're going to balance our payload.
68

69
00:05:38,420 --> 00:05:42,320
So let's see where does this end where it is reflecting.
69

70
00:05:42,320 --> 00:05:49,370
So it is reflecting somewhere into the script and it is going to ended and this script is basically
70

71
00:05:49,370 --> 00:05:52,130
going to end by script close.
71

72
00:05:52,130 --> 00:05:52,820
Okay fine.
72

73
00:05:53,450 --> 00:06:01,600
So I what I'm going to do right now is I'm going to close this beforehand only by giving a script tag
73

74
00:06:01,600 --> 00:06:03,980
close and hit enter
74

75
00:06:07,200 --> 00:06:10,170
and let's just wait for the application and.
75

76
00:06:10,200 --> 00:06:11,030
Perfect.
76

77
00:06:11,160 --> 00:06:11,750
Perfect.
77

78
00:06:12,240 --> 00:06:18,040
Yes so I'm able to get a XSS onto the web application by using burp Spider.
78

79
00:06:18,780 --> 00:06:22,850
So I hope you guys understood that how I'm able to achieve this.
79

80
00:06:22,890 --> 00:06:26,670
I hope you guys understood.
80

81
00:06:26,670 --> 00:06:27,240
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,230 --> 00:00:02,910
Hello everyone.
1

2
00:00:02,910 --> 00:00:09,830
So in this video are going to see XSS protection bypassed by a poorly validated website.
2

3
00:00:11,010 --> 00:00:18,330
So we will bypass an XSS where there is an improper input standardization or html encoding.
3

4
00:00:18,930 --> 00:00:20,960
And the developer is very smart.
4

5
00:00:21,000 --> 00:00:30,570
He may right clicks off so cheers to the developer but no proper encoding or escaping and taking decisions
5

6
00:00:30,690 --> 00:00:32,860
is very very dangerous.
6

7
00:00:33,060 --> 00:00:36,500
Also never understood underestimate the power of view.
7

8
00:00:36,690 --> 00:00:39,270
Hyphen source or burp.
8

9
00:00:40,200 --> 00:00:44,160
So let's see this in action and let's see the proof of concept for this attack.
9

10
00:00:46,500 --> 00:00:50,220
So it is the practical time and let's go to the practical.
10

11
00:00:52,470 --> 00:01:00,840
So in here I'm going to search for the website which seawatersports.com after going onto this
11

12
00:01:00,870 --> 00:01:08,950
website and just navigate quickly onto this Goa and scuba diving field after going onto this Web site.
12

13
00:01:09,150 --> 00:01:14,790
I can see that there is a book now feature I will just click on the Booknow feature.
13

14
00:01:15,090 --> 00:01:21,600
And now you can see the total amount for the trip to goa.
14

15
00:01:21,750 --> 00:01:30,670
So basically the activity is scuba diving at island is for 2250 rupees 2 2 5 0 rupees.
15

16
00:01:31,020 --> 00:01:34,140
As you can see there are so many details need to be filled.
16

17
00:01:34,140 --> 00:01:36,180
I'm not going to fill all those details.
17

18
00:01:38,130 --> 00:01:47,880
If you look closely into the url you will be able to find an interesting parameter equals to
18

19
00:01:47,880 --> 00:01:50,410
value is passing.
19

20
00:01:50,700 --> 00:01:52,530
Are you guys able to spot it.
20

21
00:01:52,530 --> 00:01:53,150
Yes.
21

22
00:01:53,250 --> 00:02:02,640
So it is activity type equal to parameter which contains a value and the value is scuba diving.
22

23
00:02:03,030 --> 00:02:08,140
And I can see this value is reflecting somewhere here scuba diving.
23

24
00:02:08,360 --> 00:02:11,590
So let's see this.
24

25
00:02:13,830 --> 00:02:21,990
Now what I'm going to do is I'm going to remove this scuba diving at Island and I'm going to replace
25

26
00:02:21,990 --> 00:02:30,630
this is active I just to check that if I give a new input is this new input going to reflect in this
26

27
00:02:30,630 --> 00:02:31,150
place.
27

28
00:02:31,560 --> 00:02:37,420
So let's verify by just hitting enter and for.
28

29
00:02:37,470 --> 00:02:38,670
Yes.
29

30
00:02:38,820 --> 00:02:43,680
So whatever the input I'm giving is being reflected on the website.
30

31
00:02:43,710 --> 00:02:44,100
Yes.
31

32
00:02:44,130 --> 00:02:47,010
So we are doing it right.
32

33
00:02:47,010 --> 00:02:48,720
What if.
33

34
00:02:48,720 --> 00:02:52,730
Now I try to give a accesses input.
34

35
00:02:52,750 --> 00:02:53,820
I exercise payload.
35

36
00:02:54,420 --> 00:02:58,580
So let me just quickly give script a loved one and script tag.
36

37
00:02:58,590 --> 00:03:03,750
Close a very simple payload and let me just hit enter.
37

38
00:03:04,380 --> 00:03:11,160
So let's see if we give a exercise payload into this input as we already saw.
38

39
00:03:11,280 --> 00:03:13,670
Whatever we give is getting reflected.
39

40
00:03:14,100 --> 00:03:23,160
If this gets executed instead of getting it afflicted then we can finally conclude that we have found
40

41
00:03:23,250 --> 00:03:27,990
a valid exercise log onto this website.
41

42
00:03:28,380 --> 00:03:33,320
So let's continue.
42

43
00:03:33,390 --> 00:03:34,560
Yes perfect.
43

44
00:03:34,800 --> 00:03:43,100
As you can see I am able to see the exercise onto my screen which confirms that this validation website
44

45
00:03:43,170 --> 00:03:49,590
in which I was not able to double click anywhere to see the page source but still the website was one
45

46
00:03:49,600 --> 00:03:57,240
rebel to US attack because I spotted that there was a parameter passing and the parameter was activity
46

47
00:03:57,240 --> 00:04:04,500
type equals 2 which was reflecting anything that I gave into the input as I gave active.
47

48
00:04:04,860 --> 00:04:10,230
And then I gave my payload and it just executed my malicious payload.
48

49
00:04:10,500 --> 00:04:12,750
So I hope you guys understood this.
49

50
00:04:12,750 --> 00:04:13,260
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,820 --> 00:00:04,230
Hello everyone.
1

2
00:00:04,230 --> 00:00:09,340
So in this video we are going to see exploitation of blind XSS.
2

3
00:00:09,420 --> 00:00:16,120
So before going to blind XSS let's see what actually is blind XSS.
3

4
00:00:16,770 --> 00:00:18,260
So whenever.
4

5
00:00:18,270 --> 00:00:27,780
You come across any feedback form or a chat bot or whatever any form in which you submit the request
5

6
00:00:28,140 --> 00:00:31,900
but you do not know what has happened in the background.
6

7
00:00:32,220 --> 00:00:38,430
When you put your XSS payload into the submit request and the request has been sent successfully
7

8
00:00:39,150 --> 00:00:49,360
what has happened at the server and what has happened has the eXSS has been exploited executed.
8

9
00:00:49,470 --> 00:00:50,190
You don't know.
9

10
00:00:51,510 --> 00:00:54,970
So in this case you are missing very critical bugs.
10

11
00:00:56,070 --> 00:01:04,110
So we are going to learn in this video series how can we do exploitation of blind XSS and identify
11

12
00:01:04,230 --> 00:01:07,340
those types of XSS.
12

13
00:01:07,350 --> 00:01:17,360
So yes we learned through any form that you submit you can test for blind excesses on vulnerability.
13

14
00:01:17,580 --> 00:01:23,780
So we will submit a feedback form or a chat bot request but we will not know if there exist 
14

15
00:01:23,780 --> 00:01:26,040
vulnerability of XSS.
15

16
00:01:26,100 --> 00:01:32,140
So we're going to give a payload which will make a request to the server and the payload is executed.
16

17
00:01:32,160 --> 00:01:39,550
So a very good tool that we are going to use for this demonstration is XSS Hunter.
17

18
00:01:39,720 --> 00:01:41,840
So yes this is the practical time now.
18

19
00:01:42,320 --> 00:01:45,590
So let's see how we're going to do the practical.
19

20
00:01:46,570 --> 00:01:52,760
So before starting with the practical I want to say to you guys that you can go on this website.
20

21
00:01:52,770 --> 00:01:59,310
That is https XSShunter dot com after going onto this Web site just go into the sign up
21

22
00:01:59,310 --> 00:02:08,190
tab after going here you can just fill this details full name user name your password the email that
22

23
00:02:08,190 --> 00:02:12,050
you want to use and your custom domain in custom domain.
23

24
00:02:12,060 --> 00:02:19,710
You just have to type whatever custom domain you want for let's say I'm taking Hacktify blind XSS
24

25
00:02:20,100 --> 00:02:20,640
dot.
25

26
00:02:21,480 --> 00:02:24,030
So basically you don't have to type anything.
26

27
00:02:24,060 --> 00:02:31,110
just this name and you will be assigned a custom domain that is hacktify blind  XSS dot XSS
27

28
00:02:31,170 --> 00:02:39,420
dot Hunter ht you have to just click on I'm not a robot my typing what I want beside name you want
28

29
00:02:39,660 --> 00:02:46,230
and click on sign up once you click on sign up you will need to verify your email address and you will
29

30
00:02:46,260 --> 00:02:49,290
then be logged in into the application.
30

31
00:02:49,290 --> 00:02:56,010
So let me just log into the application right now and show you that I already have an account onto this
31

32
00:02:56,090 --> 00:02:56,670
Web site
32

33
00:02:59,240 --> 00:03:00,320
yes.
33

34
00:03:00,710 --> 00:03:03,600
So I already have an account on this website.
34

35
00:03:03,620 --> 00:03:04,910
So let's see the attacks now.
35

36
00:03:06,080 --> 00:03:13,090
So for doing exploitation of blind XSS we are going to use this Web site that is testphp.vuln
36

37
00:03:13,100 --> 00:03:13,820
web dot com.
37

38
00:03:15,980 --> 00:03:23,560
So as you can see there is a your profile field.
38

39
00:03:23,950 --> 00:03:31,880
I have logged in into the application using the user name test and the password test , again see in
39

40
00:03:31,880 --> 00:03:39,580
the name field I'm going to give the payload that I got from XSS Hunter.
40

41
00:03:40,370 --> 00:03:46,490
You just have to go into the payload section after you log in and from there you can copy the script
41

42
00:03:46,490 --> 00:03:48,320
tag basic payload.
42

43
00:03:48,530 --> 00:03:53,630
You just have to click here copy payload to clipboard or you can manually copy from here.
43

44
00:03:53,960 --> 00:03:57,170
And this is the payload that I'm giving into the field.
44

45
00:03:58,010 --> 00:04:04,600
So I've given it into the first name field second credit card number field third e-mail field fourth
45

46
00:04:04,610 --> 00:04:09,890
full number and fifth address field and I will just hit on Update button
46

47
00:04:12,950 --> 00:04:15,570
after hitting onto the update button.
47

48
00:04:15,620 --> 00:04:19,500
Now as you can see the website is loading now.
48

49
00:04:19,550 --> 00:04:27,770
I will just go to the first tab XSS fires to check if my XSS payload has been fired by
49

50
00:04:27,830 --> 00:04:30,040
any application.
50

51
00:04:30,080 --> 00:04:33,620
Basically it means has it been executed or not.
51

52
00:04:37,240 --> 00:04:38,230
So we are waiting
52

53
00:04:46,830 --> 00:04:54,170
you may also get an email on to your signed up email that you have used while making an account
53

54
00:04:59,310 --> 00:05:05,040
let's just wait for some more seconds and we'll be able to see it.
54

55
00:05:09,480 --> 00:05:11,480
Perfect as you can see now.
55

56
00:05:12,150 --> 00:05:20,690
here are 1 2 3 4 clicks that have been made so that this is the victim's IP and this is the vulnerable
56

57
00:05:20,690 --> 00:05:21,140
page.
57

58
00:05:21,170 --> 00:05:24,010
That was user info dot  PHP.
58

59
00:05:24,380 --> 00:05:24,850
Perfect
59

60
00:05:28,580 --> 00:05:37,520
so I hope you guys understood this POC in which we were able to attack and we were able to get a
60

61
00:05:37,520 --> 00:05:39,200
hit on to our server.
61

62
00:05:39,200 --> 00:05:42,350
Which means it was clicked.
62

63
00:05:42,680 --> 00:05:45,200
This can be submitted in the proof of concept.
63

64
00:05:45,230 --> 00:05:50,690
If you are reporting any vulnerability onto any website I hope you guys understood.
64

65
00:05:50,900 --> 00:05:52,070
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,170 --> 00:00:02,870
Hello everyone.
1

2
00:00:02,880 --> 00:00:09,630
So in this video we are going to learn what is XSS type store.
2

3
00:00:09,810 --> 00:00:15,140
So basically a store XSS into any application.
3

4
00:00:15,210 --> 00:00:24,080
So what is it if any application stores your input but into an unsafe manner.
4

5
00:00:24,240 --> 00:00:25,160
Always try.
5

6
00:00:25,350 --> 00:00:31,900
where you can save the input as XSS payload where the server saves the payload.
6

7
00:00:32,010 --> 00:00:40,870
For example you can save the payload in edit profile support chat bots anywhere in the server.
7

8
00:00:41,010 --> 00:00:43,350
where something is stored basically.
8

9
00:00:43,980 --> 00:00:50,880
So we are going to try this attack in which we are going to save our payload onto the server.
9

10
00:00:50,880 --> 00:01:00,300
And if anyone sees that particular payload or reaches to that profile the payload will get executed
10

11
00:01:00,720 --> 00:01:05,380
and we will be able to achieve a store XSS vulnerability.
11

12
00:01:06,180 --> 00:01:11,550
So let's see this into action practical time.
12

13
00:01:11,650 --> 00:01:18,300
So let's see the practical of this attack.
13

14
00:01:18,470 --> 00:01:26,140
So for doing this attack I'm going to choose this Web site that is woodland worldwide dot com after
14

15
00:01:26,140 --> 00:01:27,340
going into the website.
15

16
00:01:27,370 --> 00:01:30,310
I will just try to log in into the website.
16

17
00:01:30,390 --> 00:01:32,940
It is showing a covid 19 message.
17

18
00:01:33,490 --> 00:01:34,850
OK thanks.
18

19
00:01:34,860 --> 00:01:41,830
So I will just go into the loggin option and I will try to sign in with Google.
19

20
00:01:42,040 --> 00:01:52,370
Let me just sign in using my e-mail id hacker dot udemy @gmail dot com.
20

21
00:01:53,470 --> 00:01:55,180
Let me choose the password
21

22
00:02:00,310 --> 00:02:00,740
yeah.
22

23
00:02:00,860 --> 00:02:03,950
So I am currently logging in to the application
23

24
00:02:10,240 --> 00:02:18,280
so after logging in what we are going to do as guys we are going to go into the edit profile option
24

25
00:02:18,580 --> 00:02:19,900
as you can see.
25

26
00:02:19,900 --> 00:02:23,260
Welcome Baby.
26

27
00:02:23,630 --> 00:02:29,200
I'll just click here and go to my personal information into my profile section.
27

28
00:02:29,900 --> 00:02:36,680
As you can see here is my personal information of my account in the name field.
28

29
00:02:36,740 --> 00:02:41,920
I'm just going to type the open and closing brackets.
29

30
00:02:42,050 --> 00:02:45,170
Let me choose some arbitrary date of birth
30

31
00:02:47,940 --> 00:02:48,640
and month.
31

32
00:02:48,680 --> 00:02:49,830
Anything indeed.
32

33
00:02:49,880 --> 00:02:59,530
Anything that we choose that address to anything let's say I type mumbai address to again Mumbai are we
33

34
00:02:59,530 --> 00:03:06,170
choose the country India state anything let's say Maharashtra City Bombay
34

35
00:03:09,830 --> 00:03:18,260
ZIP Code Four double zero six four mobile number I will give my mobile number and I will click on
35

36
00:03:18,280 --> 00:03:27,350
update as you can see the application gave an error and did not allow to update as you can see there is
36

37
00:03:27,350 --> 00:03:35,600
are input validation into the first name and the last name field as it detected that along with the
37

38
00:03:35,600 --> 00:03:39,050
characters some special characters are also given.
38

39
00:03:39,680 --> 00:03:48,380
So the first name and the last name field is validated using input validation where it will only take
39

40
00:03:48,500 --> 00:03:52,840
alphabet and not any type of special character.
40

41
00:03:53,180 --> 00:03:57,530
So how we are going to put our payload in this case.
41

42
00:03:57,530 --> 00:04:05,180
So for this scenario we are going to take the help of Burpe suite so I will remove this opening and closing
42

43
00:04:05,450 --> 00:04:15,430
bracket first we are not able to put it directly through the Web site.
43

44
00:04:15,430 --> 00:04:18,010
So now we're going to put that using Burpe suite
44

45
00:04:22,030 --> 00:04:29,980
I will do intercept on and click on update ,now you can see this is the post request that is going to
45

46
00:04:29,980 --> 00:04:34,810
the server which contains the detail as you can see in the body first name.
46

47
00:04:34,900 --> 00:04:38,810
equals to baby last name equals to hacker over here.
47

48
00:04:39,070 --> 00:04:39,250
Okay
48

49
00:04:42,520 --> 00:04:46,520
so I will try to give the special characters here
49

50
00:04:46,520 --> 00:04:49,180
First let me send this to the repeaters
50

51
00:04:53,590 --> 00:05:00,550
let me give these characters and let me just hit GO let's verify.
51

52
00:05:00,550 --> 00:05:02,140
Let me drop all this request.
52

53
00:05:02,140 --> 00:05:05,700
I do not want this to overwrite the request.
53

54
00:05:05,740 --> 00:05:08,790
Let me just refresh because we have saved it using repeater.
54

55
00:05:08,860 --> 00:05:15,430
And yes we can observe here that the validation was only.
55

56
00:05:15,480 --> 00:05:20,180
The client side the validation is not at the server side.
56

57
00:05:20,290 --> 00:05:26,880
So the application is allowing to store the special characters also.
57

58
00:05:26,980 --> 00:05:32,410
So it was all it was only the client side validation which we have successfully bypassed
58

59
00:05:36,580 --> 00:05:37,220
now.
59

60
00:05:37,420 --> 00:05:41,240
Our main motive is performing a store XSS
60

61
00:05:41,260 --> 00:05:46,960
So what I'm going to do right now is in the first name field I am going to give the payload as an
61

62
00:05:47,020 --> 00:05:49,890
input a simple payload script.
62

63
00:05:49,900 --> 00:05:53,630
alert one script tag close in the last name field.
63

64
00:05:53,710 --> 00:06:00,610
Also I'm willing to give the payload script alert two this time and script tag close because I want
64

65
00:06:00,610 --> 00:06:03,190
to see that which I field is vulnerable.
65

66
00:06:03,190 --> 00:06:06,840
First Name field or last name field.
66

67
00:06:07,510 --> 00:06:11,470
If I get a pop up of one which means the first name field is vulnerable.
67

68
00:06:11,470 --> 00:06:15,810
If I get a pop up of two that means the last name field is vulnerable.
68

69
00:06:15,870 --> 00:06:19,480
Let us first verify by refreshing the browser
69

70
00:06:23,700 --> 00:06:31,020
as you can see the payload is saved into the first name and the last name field but unfortunately it
70

71
00:06:31,020 --> 00:06:40,390
did not execute and did not execute which means that we were not able to successfully perform our store
71

72
00:06:40,390 --> 00:06:41,480
XSS why.
72

73
00:06:42,330 --> 00:06:44,780
Let's see what happened into the background.
73

74
00:06:45,120 --> 00:06:53,370
So let's see the response into Burpe suite what we are missing actually here is very important thing that
74

75
00:06:53,370 --> 00:07:01,470
is balancing we did not balance our payload as you can see I will just search the first thing that is
75

76
00:07:01,470 --> 00:07:07,840
baby and you can see my payload has become the value as you can see here.
76

77
00:07:07,950 --> 00:07:10,710
The payload has become of value.
77

78
00:07:10,710 --> 00:07:17,700
I want to take out my payload that is script alert for the script tag close out of this value time and
78

79
00:07:17,700 --> 00:07:23,220
I can see this value tag is getting closer by this tags.
79

80
00:07:23,360 --> 00:07:27,360
Okay double quoate forward slash closing bracket.
80

81
00:07:27,840 --> 00:07:37,060
So what I'm looking to do right now is I'm going to pass the ending tags with my payload.
81

82
00:07:37,430 --> 00:07:38,220
Okay.
82

83
00:07:38,580 --> 00:07:42,390
So I will just copy that and I'm going to pass it.
83

84
00:07:42,390 --> 00:07:44,820
over here at this position after Baby
84

85
00:07:47,630 --> 00:07:53,740
Okay so let me just go here and let me just hit it like this.
85

86
00:07:53,740 --> 00:07:54,070
Okay.
86

87
00:07:54,250 --> 00:08:02,110
Let me do the same into the last name field to balance last name also and I will hit Go.
87

88
00:08:02,380 --> 00:08:03,490
Now let's verify.
88

89
00:08:03,490 --> 00:08:08,800
Are you able to balance it and our payload has come out of the value field or not.
89

90
00:08:08,800 --> 00:08:10,980
So yes perfectly all right.
90

91
00:08:10,990 --> 00:08:19,960
We can see that our payload has come out of the value field and it has successfully got balanced.
91

92
00:08:19,960 --> 00:08:20,470
Perfect.
92

93
00:08:21,300 --> 00:08:24,240
Now let's go into the browser and verify that.
93

94
00:08:24,250 --> 00:08:25,510
Is this working or not.
94

95
00:08:27,130 --> 00:08:29,200
So let me just reload this website.
95

96
00:08:29,200 --> 00:08:29,960
Perfect.
96

97
00:08:29,980 --> 00:08:33,720
We got alert for one as well as we got alert for two.
97

98
00:08:33,970 --> 00:08:38,110
Which means the first name field and the last name field.
98

99
00:08:38,110 --> 00:08:41,520
Both were vulnerable to store XSS attack.
99

100
00:08:42,730 --> 00:08:50,350
So I I hope you guys understood this attack in which we were able to successfully save our payload at
100

101
00:08:50,350 --> 00:08:50,990
the servers end.
101

102
00:08:51,040 --> 00:08:59,080
And now whenever I will log in into this account this execution will always happen.
102

103
00:08:59,080 --> 00:08:59,780
Why.
103

104
00:08:59,800 --> 00:09:04,750
Because the payload is permanently stored at the server side.
104

105
00:09:04,750 --> 00:09:15,160
So store  XSS is more dangerous because in this case the payload get stored and the server side.
105

106
00:09:15,160 --> 00:09:16,500
I hope you guys understood.
106

107
00:09:16,510 --> 00:09:16,980
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,350 --> 00:00:02,850
Hello everyone.
1

2
00:00:02,850 --> 00:00:12,210
So in this we do we are going to see XSS type DOM,dom stands for Document Object Model which is
2

3
00:00:12,210 --> 00:00:19,830
basically a client side vulnerability and the DOM remains into your browser only.
3

4
00:00:21,060 --> 00:00:23,390
So why does vulnerability arises.
4

5
00:00:23,520 --> 00:00:31,290
This arises when the dom is used to generate dynamic content containing the user's input that can be
5

6
00:00:31,290 --> 00:00:36,800
processed without properly checking or validating it.
6

7
00:00:36,810 --> 00:00:38,120
This is a client side attack.
7

8
00:00:38,130 --> 00:00:46,770
As I already said that the input comes into the DOM which is also known as source and it comes out or
8

9
00:00:46,770 --> 00:00:50,670
gets executed through the DOM which is known as sink.
9

10
00:00:51,780 --> 00:00:59,400
So here you would understand that when your input which is an XSS payload a dangerous query
10

11
00:00:59,820 --> 00:01:05,130
goes into the DOM is known as source and then comes out is known as sink
11

12
00:01:08,850 --> 00:01:15,660
as you can see a vulnerable html code which is written over here.
12

13
00:01:15,910 --> 00:01:20,740
It starts by html  and html close body.
13

14
00:01:20,860 --> 00:01:26,590
Script tag and in the script tag you can see a variable source is defined which says hello.
14

15
00:01:26,740 --> 00:01:33,930
Let's decode URI Component in which it is written location dot hash dot split and given a URI
15

16
00:01:33,930 --> 00:01:36,430
fragment that is hash.
16

17
00:01:36,430 --> 00:01:38,000
So this is basically the source.
17

18
00:01:38,630 --> 00:01:45,970
And if you look below var divElement documents dot create element divElement dot inner html
18

19
00:01:46,690 --> 00:01:47,740
is equal to source.
19

20
00:01:47,740 --> 00:01:54,570
This is basically the sink where anything that has been given into it will come out.
20

21
00:01:54,940 --> 00:02:03,550
If we look at the bottom exploitable code in which if any attacker sends a get request to the vulnerable
21

22
00:02:03,600 --> 00:02:14,050
website which has the above code running and you can see clearly that sending a get request to w w w
22

23
00:02:14,050 --> 00:02:23,700
dot vulnerable hyphen Web site dot example and a URI fragment that is hash which is into our source.
23

24
00:02:23,800 --> 00:02:31,150
So if we give an XSS payload that is image source equals to test on error alert XSS into
24

25
00:02:31,150 --> 00:02:38,790
the source wherein the. URI fragment parameter is that hash it will automatically come out of the sink.
25

26
00:02:38,830 --> 00:02:42,350
That is the output and we will get a alert.
26

27
00:02:42,400 --> 00:02:48,780
I hope you guys understood a very basic example of DOM based XSS 
27

28
00:02:48,880 --> 00:02:57,370
So what are some dangerous source list and sink list if you ever come across any website and you try
28

29
00:02:57,370 --> 00:03:07,030
to analyze the Dom if you're able to see into the source if any application users document  dot url
29

30
00:03:07,020 --> 00:03:09,000
document dot refer.
30

31
00:03:09,160 --> 00:03:16,280
Location location dot href, location dot search ,location dot hash ,or location dot path name.
31

32
00:03:16,510 --> 00:03:25,420
Then in these types of cases sometimes it may become vulnerable and the payload must go into the source
32

33
00:03:25,510 --> 00:03:29,260
and sometimes come out of the sink which can be dangerous.
33

34
00:03:29,620 --> 00:03:37,330
If you look at some dangerous sink you can be seen as eval set time out set interval, document
34

35
00:03:37,330 --> 00:03:44,150
dot write or element.innnerHTML is a dangerous type of sink
35

36
00:03:44,230 --> 00:03:50,890
So these are the sink and source with you should look into any applications source code.
36

37
00:03:51,010 --> 00:03:58,390
If you are able to see that then you may try to check the vulnerability of DOM XSS .
37

38
00:03:58,390 --> 00:04:07,590
So it's the practical time now and let's see a practical based on DOM XSS  to application.
38

39
00:04:07,640 --> 00:04:15,340
OK and now here I'm going to exploit the DOM XSS  so before exploiting their DOM XSS  let's
39

40
00:04:15,340 --> 00:04:25,160
see what is into the source and what is into the sink so I will right click and click on View page source.
40

41
00:04:25,310 --> 00:04:35,770
If you if you look closely there is a document sink which says variable user name search parameter
41

42
00:04:35,770 --> 00:04:45,430
dot get name and it comes out from inner HTML Hello plus user name.
42

43
00:04:45,510 --> 00:04:48,740
OK so hello plus whatever the user name is given.
43

44
00:04:49,540 --> 00:04:58,110
So here in we understand that that dangerous source which comes out of the sink is name.
44

45
00:04:58,330 --> 00:05:05,320
So I will just go onto this website again and I will try to exploit this Dom in which I will just try
45

46
00:05:05,320 --> 00:05:13,900
to show you when I type name equal to that is the parameter equals to a value it gets reflected in  to the
46

47
00:05:14,080 --> 00:05:15,010
sink.
47

48
00:05:15,010 --> 00:05:15,940
Awesome.
48

49
00:05:15,940 --> 00:05:20,060
So what if I tried to give a XSS payload into here.
49

50
00:05:20,170 --> 00:05:20,920
What will happen.
50

51
00:05:21,550 --> 00:05:30,700
So let me just try to quickly exploit this by giving an XSS payload and let's see if it comes
51

52
00:05:30,700 --> 00:05:32,140
out or execute.
52

53
00:05:33,190 --> 00:05:42,910
So I am giving a payload image source equal to x on error equals to alert one and let me just hit enter by
53

54
00:05:42,910 --> 00:05:47,750
giving this dangerous payload as input and when I hit enter.
54

55
00:05:47,830 --> 00:05:48,810
Perfect.
55

56
00:05:48,880 --> 00:05:52,250
Can you see I was able to explode the DOM XSS .
56

57
00:05:52,270 --> 00:05:52,680
Why.
57

58
00:05:52,960 --> 00:06:01,060
Because I saw the vlnreablesource and sink wherein name parameter was coming out directly without any
58

59
00:06:01,600 --> 00:06:03,640
sanitization.
59

60
00:06:03,670 --> 00:06:06,860
I hope you understood the first video of DOM XSS .
60

61
00:06:06,970 --> 00:06:07,360
We'll see.
61

62
00:06:07,360 --> 00:06:09,650
Couple of more examples into the next video.
62

63
00:06:10,150 --> 00:06:10,600
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,510 --> 00:00:01,710
Hello everyone.
1

2
00:00:01,710 --> 00:00:09,630
So in this video we are going to see how can we exploit DOM XSS as we already saw in the first
2

3
00:00:09,630 --> 00:00:10,140
video.
3

4
00:00:10,200 --> 00:00:17,010
That we were able to exploit the Name field and that was coming out of the sink without getting
4

5
00:00:17,010 --> 00:00:18,180
sanitized.
5

6
00:00:18,180 --> 00:00:19,620
So let's see into this video.
6

7
00:00:20,160 --> 00:00:30,360
So coming onto this website I'd directly go into the source code if you were able to see there is location
7

8
00:00:30,360 --> 00:00:36,090
sink in which I'm able to see that the redirect is into the sink.
8

9
00:00:36,090 --> 00:00:38,780
That is document dot location.
9

10
00:00:39,000 --> 00:00:45,980
If you're trying to recall into the presentation that we saw we saw different types of sources and sinks.
10

11
00:00:46,140 --> 00:00:49,390
Document dot location is one of them.
11

12
00:00:49,410 --> 00:00:49,820
OK.
12

13
00:00:49,830 --> 00:00:56,780
So I came to know that redirect is coming out now sink  of document dot location.
13

14
00:00:57,390 --> 00:01:04,540
So what if I try to give here redirect equal to and try to give a website name.
14

15
00:01:04,980 --> 00:01:09,850
Let's see if this website gets redirected to the another website.
15

16
00:01:09,870 --> 00:01:11,940
That is Google dot com.
16

17
00:01:11,940 --> 00:01:16,540
So by giving redirect equals to Google dot com.
17

18
00:01:16,590 --> 00:01:21,120
I will try to hit enter and observe what happens.
18

19
00:01:21,960 --> 00:01:25,350
As you can see I got redirected to another Web site.
19

20
00:01:25,620 --> 00:01:26,300
Yes.
20

21
00:01:26,370 --> 00:01:29,390
Which means that this is properly working.
21

22
00:01:29,520 --> 00:01:37,240
And whatever I tried to give into this parameter execute out of the sink without any issue.
22

23
00:01:37,410 --> 00:01:44,130
What if I tried to give an XSS payload or I tried to do a alert.
23

24
00:01:44,250 --> 00:01:49,040
So if you look closely I'm giving an alert in to redirect parameter.
24

25
00:01:49,220 --> 00:01:51,540
And yes perfect.
25

26
00:01:51,550 --> 00:02:00,690
I'm able to get XSS over here if I tried to go into the source and just try to show you.
26

27
00:02:01,410 --> 00:02:01,840
Yes.
27

28
00:02:01,860 --> 00:02:07,740
As you can see here this is a dangerous sink because of which this type of behavior has been happening
28

29
00:02:08,010 --> 00:02:11,550
and I'm able to achieve XSS.
29

30
00:02:11,730 --> 00:02:13,010
I hope you guys understood.
30

31
00:02:13,080 --> 00:02:18,190
We will see one more video in which we are going to exploit DOM based XSS  again.
31

32
00:02:18,240 --> 00:02:18,750
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,950 --> 00:00:03,390
Hello everyone.
1

2
00:00:03,390 --> 00:00:09,970
So in this video we're going to see one more exploration of Dombase XSS.
2

3
00:00:10,050 --> 00:00:16,770
So I will directly go into the page source to see what is the source code of this website
3

4
00:00:20,060 --> 00:00:31,760
as you can see the execution sink is var index equals to searchparams. get index dot toString
4

5
00:00:32,570 --> 00:00:37,000
which means this is execution sink.
5

6
00:00:37,040 --> 00:00:44,150
So if you try to recall into the presentation I told about some dangerous things and eval is one of
6

7
00:00:44,150 --> 00:00:44,920
them.
7

8
00:00:45,170 --> 00:00:53,120
If it looked below this line you're at a certain event which is it is going to violate whatever is given
8

9
00:00:53,360 --> 00:00:57,060
into the index.
9

10
00:00:57,350 --> 00:01:02,550
So below if you see also they are using in a dot HDMI.
10

11
00:01:02,690 --> 00:01:09,170
If you're trying to see in order Yemen and whatever it is given is comes out of this that is current
11

12
00:01:09,350 --> 00:01:13,850
market index plus market dot index.
12

13
00:01:13,850 --> 00:01:19,490
So I came to know that they're using index without proper sanitization.
13

14
00:01:19,550 --> 00:01:29,990
So what if I tried to give the index equal to one two three or let's say Rohit and if index and get
14

15
00:01:30,170 --> 00:01:37,340
reflected or the application I will come to know OK this is getting reflected whatever I try to give
15

16
00:01:37,360 --> 00:01:46,490
into the source comes out of the same.
16

17
00:01:46,540 --> 00:01:53,030
So let me just try to do a lot and perfect.
17

18
00:01:53,650 --> 00:02:02,320
So I given a lot and you can see after giving a lot I got an exercise which means I was able to exploit
18

19
00:02:02,410 --> 00:02:09,520
the dumbest excesses as also you can see under the application it is saying current money market index
19

20
00:02:09,580 --> 00:02:18,040
is undefined if you go back to the source you can see current market index is market dot index and what
20

21
00:02:18,040 --> 00:02:23,650
we give into that index value is an alert that's why it is showing undefined.
21

22
00:02:23,650 --> 00:02:30,630
I hope you guys understood this dumbest exercise example of index in which it was a wonderful resource
22

23
00:02:30,640 --> 00:02:38,980
and think whenever I give an input into the index that is the one rebel source without proper sanitization
23

24
00:02:39,880 --> 00:02:46,570
it came out and it just got exploded and we are able to achieve exercise I hope you guys understood
24

25
00:02:47,290 --> 00:02:48,000
this video.
25

26
00:02:48,610 --> 00:02:49,690
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,720 --> 00:00:01,530
Hello, everyone.
1

2
00:00:02,040 --> 00:00:11,250
So in this video, we are going to use a tool which is named as a findom -xss, which is
2

3
00:00:11,250 --> 00:00:17,660
basically a tool of very fast tool for finding DOM based xss venerability scanner.
3

4
00:00:19,350 --> 00:00:23,040
So as the system says, A DOM based xss vulnerabaility scanner.
4

5
00:00:23,130 --> 00:00:24,630
Obviously, we are going to type.
5

6
00:00:24,720 --> 00:00:29,550
We are going to find the types of vulnerabilities, which is DOM xss.
6

7
00:00:30,540 --> 00:00:30,950
All right.
7

8
00:00:31,290 --> 00:00:34,080
So the usage of this tool is pretty simple.
8

9
00:00:34,170 --> 00:00:39,600
And I have tested this tool and it works out to be walking pretty fine.
9

10
00:00:40,620 --> 00:00:43,920
So let us see, how do we use this particular tool?
10

11
00:00:44,760 --> 00:00:50,340
So you have to quickly jump onto this particular github  repo once you are over here.
11

12
00:00:50,460 --> 00:00:52,680
You have to basically clone the repo.
12

13
00:00:52,770 --> 00:00:59,370
So you will just click over here or you can just copy this, go to your terminal and take the command,
13

14
00:00:59,370 --> 00:01:02,700
which is git clone and the repository.
14

15
00:01:03,330 --> 00:01:04,380
And you have to hit enter.
15

16
00:01:05,400 --> 00:01:11,760
Once you hit, enter, the repository will get Clone and you will see something like this inside that
16

17
00:01:11,760 --> 00:01:13,320
particular repository.
17

18
00:01:14,810 --> 00:01:15,110
All right.
18

19
00:01:15,990 --> 00:01:21,690
So this particular tool has a dependency that you need to install.
19

20
00:01:22,090 --> 00:01:24,330
That dependency is linkfinder
20

21
00:01:24,840 --> 00:01:33,210
So when I will click on a link, find it, I will just come to this particular repository and it says
21

22
00:01:33,210 --> 00:01:34,440
you need to install this.
22

23
00:01:34,530 --> 00:01:36,510
So we have to also install this.
23

24
00:01:36,630 --> 00:01:44,810
So I would just copy this, go back there and do it git clone and linkfinder, the same step.
24

25
00:01:46,320 --> 00:01:50,730
So git clone and hit enter.
25

26
00:01:51,390 --> 00:01:57,330
As you can see, the part already exist because I have already downloaded the particular software.
26

27
00:01:57,930 --> 00:02:03,090
So what you have to do is quickly go into that particular folder after going inside.
27

28
00:02:03,120 --> 00:02:04,260
Let me show you what is there.
28

29
00:02:04,350 --> 00:02:10,980
So there are a couple of files and the link finder script is Python file, basically.
29

30
00:02:11,370 --> 00:02:16,220
So before running that particular file, you need to set up two things.
30

31
00:02:16,230 --> 00:02:18,520
First is the requirement.txt file
31

32
00:02:19,230 --> 00:02:20,790
Second one is the setup file.
32

33
00:02:21,420 --> 00:02:30,630
So before installing would these dependencies, I will show you that this particular tool is only compatible
33

34
00:02:30,690 --> 00:02:31,740
with Python three.
34

35
00:02:31,920 --> 00:02:36,090
So you need to have Python three installed into your computers.
35

36
00:02:36,770 --> 00:02:37,090
All right.
36

37
00:02:37,230 --> 00:02:38,810
So we have Python three installed.
37

38
00:02:38,970 --> 00:02:46,710
So first thing that we are going to do is we are going to perform a PIP install and read hyphen stands
38

39
00:02:46,710 --> 00:02:49,850
for read the particular file, which is a requirement.txt
39

40
00:02:49,980 --> 00:02:53,920
So we are going to install all the requirements, in my particular system.
40

41
00:02:54,000 --> 00:02:55,750
All the requirements are installed.
41

42
00:02:55,860 --> 00:03:00,090
So it just got finished very quickly in your system.
42

43
00:03:00,150 --> 00:03:02,370
It may take some few minutes.
43

44
00:03:03,920 --> 00:03:04,350
All right.
44

45
00:03:04,560 --> 00:03:06,330
The second is Setup.py file.
45

46
00:03:06,570 --> 00:03:09,960
So we need to also install the setup.py for that.
46

47
00:03:09,960 --> 00:03:11,680
You have to type the command python3
47

48
00:03:12,180 --> 00:03:16,880
And space setup.py install
48

49
00:03:17,430 --> 00:03:18,400
And hit enter.
49

50
00:03:19,110 --> 00:03:22,670
As you can see, we have also installed the setup file.
50

51
00:03:23,130 --> 00:03:25,020
And now we're good to go.
51

52
00:03:25,320 --> 00:03:33,160
Let's quickly just check if Linkfind that is working or is it giving any error or asking for any dependencies.
52

53
00:03:33,870 --> 00:03:35,120
So when I hit enter.
53

54
00:03:35,250 --> 00:03:40,200
You can see the tool has successfully initiated, which means that tool is successfully installed.
54

55
00:03:41,850 --> 00:03:42,270
All right.
55

56
00:03:42,300 --> 00:03:45,870
So we have successfully installed our dependency.
56

57
00:03:45,960 --> 00:03:46,830
That was link.
57

58
00:03:46,830 --> 00:03:47,270
Finder
58

59
00:03:47,820 --> 00:03:50,910
Let's come back to particular this tool, which is fine.
59

60
00:03:50,940 --> 00:03:52,140
DOM-xss
60

61
00:03:53,480 --> 00:03:56,020
Now, one changed.
61

62
00:03:56,100 --> 00:04:03,510
You have to do is into the configuration file and the change that you have to perform is on line number
62

63
00:04:03,510 --> 00:04:03,900
three.
63

64
00:04:04,260 --> 00:04:06,660
So let me just show you the change that we need to do.
64

65
00:04:07,410 --> 00:04:09,870
It is a very simple change that you have to do.
65

66
00:04:10,410 --> 00:04:15,500
The developer has basically hardcoded the path of link finder as we can see
66

67
00:04:15,540 --> 00:04:20,820
This is the path for his computer home/dw1/Tools/Linkfinder
67

68
00:04:20,820 --> 00:04:22,670
/Linkfinder.py
68

69
00:04:23,400 --> 00:04:28,140
So we need to modify this particular line into our Bash script.
69

70
00:04:28,410 --> 00:04:30,060
So let me just show you where to do it.
70

71
00:04:31,350 --> 00:04:32,880
So this is a particular Bash script.
71

72
00:04:32,940 --> 00:04:35,460
So we are going to open it.
72

73
00:04:39,090 --> 00:04:39,630
I'm sorry.
73

74
00:04:47,250 --> 00:04:48,720
So again, let's open it.
74

75
00:04:54,300 --> 00:04:54,580
Yes.
75

76
00:04:54,650 --> 00:04:56,930
So now we are inside this particular directory.
76

77
00:04:57,360 --> 00:05:01,260
And you can see your you have to give your particular path
77

78
00:05:01,350 --> 00:05:06,990
So this is the part that I have given for my particular tool, which I have installed.
78

79
00:05:07,050 --> 00:05:07,300
OK.
79

80
00:05:07,680 --> 00:05:09,200
So how to get the path
80

81
00:05:09,330 --> 00:05:14,420
So just type the command pwd and it will show you the present working directory.
81

82
00:05:14,550 --> 00:05:14,760
OK.
82

83
00:05:15,090 --> 00:05:17,360
So I'm into the findom xss right now.
83

84
00:05:17,430 --> 00:05:18,890
I need to go in link finder.
84

85
00:05:20,100 --> 00:05:21,440
Let me just go in Link finder.
85

86
00:05:22,230 --> 00:05:23,830
And again, the command pwd
86

87
00:05:23,880 --> 00:05:27,000
And you can see this is the path that you have to paste towards it.
87

88
00:05:27,990 --> 00:05:28,230
OK.
88

89
00:05:28,380 --> 00:05:30,900
This is the path and the file name as well.
89

90
00:05:31,470 --> 00:05:33,930
The file is lying over here.
90

91
00:05:34,170 --> 00:05:35,100
And this is the file.
91

92
00:05:35,190 --> 00:05:37,620
So the whole part you have to give it over there
92

93
00:05:38,790 --> 00:05:39,150
All right.
93

94
00:05:39,390 --> 00:05:45,660
So let's come out of that particular folder and come back to findom-xss.sh script.
94

95
00:05:46,350 --> 00:05:52,670
So let us see how efficient is this particular script for finding dom xss vulnerability
95

96
00:05:54,330 --> 00:05:58,680
So let's quickly run and see if this has been configured or not.
96

97
00:05:58,950 --> 00:06:00,960
I will just click enter there and you can see.
97

98
00:06:01,320 --> 00:06:06,660
This tool is successfully configured and has started for now.
98

99
00:06:07,590 --> 00:06:15,390
Now let's see if this particular tool gives us the accurate output for any Web site that we give it.
99

100
00:06:16,200 --> 00:06:18,510
So we are going to do.
100

101
00:06:18,720 --> 00:06:20,610
Are practical for dom-xss.
101

102
00:06:20,700 --> 00:06:26,280
So if you do a basic Google search saying domxss practice web site, you will guess you will
102

103
00:06:26,280 --> 00:06:27,470
get this particular Web site.
103

104
00:06:27,570 --> 00:06:30,150
The first one, which is Domxss.com.
104

105
00:06:30,750 --> 00:06:36,540
Just go to that particular Web site and just click on the start button start the domxss exercise.
105

106
00:06:37,080 --> 00:06:41,600
So you will jump on this particular exercise inline secript document.
106

107
00:06:41,790 --> 00:06:42,120
Right.
107

108
00:06:42,510 --> 00:06:42,900
All right.
108

109
00:06:44,070 --> 00:06:49,060
So we are going to not do it manually this time, as we have already seen.
109

110
00:06:49,410 --> 00:06:53,790
But this time now we are going to do it with the automated scanner.
110

111
00:06:54,210 --> 00:06:57,710
So I'm just going to copy this particular url and go back to the tool.
111

112
00:06:58,440 --> 00:07:03,300
As you can see, the usage says, run this particular script and give your target.
112

113
00:07:03,960 --> 00:07:04,290
All right.
113

114
00:07:04,320 --> 00:07:05,220
So let's do that.
114

115
00:07:06,150 --> 00:07:07,830
So this is the particular script.
115

116
00:07:08,940 --> 00:07:11,430
And this is the particular target that we have given.
116

117
00:07:11,520 --> 00:07:15,060
And I will hit enter once I hit enter.
117

118
00:07:15,750 --> 00:07:22,050
You can see the scan has been started over here for the particular target that we have given.
118

119
00:07:23,220 --> 00:07:28,140
It says document.url something it has flagged.
119

120
00:07:28,230 --> 00:07:32,690
And it says document.url is the vulnerable  sync.
120

121
00:07:33,240 --> 00:07:33,730
All right.
121

122
00:07:33,780 --> 00:07:35,130
So let's check this.
122

123
00:07:35,190 --> 00:07:38,550
If this is giving a right output or not.
123

124
00:07:39,270 --> 00:07:40,230
So I will just right.
124

125
00:07:40,230 --> 00:07:42,120
Click and click on view page Source.
125

126
00:07:42,570 --> 00:07:47,360
I already opened my page source over here and I will search for documents.url
126

127
00:07:47,580 --> 00:07:48,170
As you can see.
127

128
00:07:48,200 --> 00:07:48,510
Yep.
128

129
00:07:48,840 --> 00:07:51,930
Document.url is present over there.
129

130
00:07:53,580 --> 00:07:59,700
Now you can see here document.url.index of Name equals two is given.
130

131
00:07:59,930 --> 00:08:00,180
Okay.
131

132
00:08:00,630 --> 00:08:02,640
Well you can see over here.
132

133
00:08:02,820 --> 00:08:12,060
So let us just go back to this particular web application and let us give something into the name parameter
133

134
00:08:12,390 --> 00:08:14,520
and let's see if it works or not.
134

135
00:08:14,700 --> 00:08:16,640
So let us give a simple image.
135

136
00:08:16,680 --> 00:08:20,220
source payload that we have seen in on the videos.
136

137
00:08:20,880 --> 00:08:24,300
So image source equals two X. This is invalid source.
137

138
00:08:24,750 --> 00:08:25,350
So 
138

139
00:08:25,410 --> 00:08:25,860
onerror
139

140
00:08:28,260 --> 00:08:30,180
confirm that?
140

141
00:08:30,300 --> 00:08:31,050
An alert.
141

142
00:08:31,740 --> 00:08:36,060
And in that alert, give one, lets it enter and see if you get exercise.
142

143
00:08:44,030 --> 00:08:45,140
So we are waiting
143

144
00:08:49,310 --> 00:08:53,140
If everything is right, then we will get a.xss 
144

145
00:08:53,780 --> 00:09:02,360
Alert confirming that our xss payload that we have formatted at that particular parameter.
145

146
00:09:02,450 --> 00:09:02,870
That was. name
146

147
00:09:03,580 --> 00:09:08,750
It's been successfully getting injected and is executing our xss payload.
147

148
00:09:10,010 --> 00:09:11,030
Let me just try again.
148

149
00:09:17,120 --> 00:09:19,760
Something is not right with the Internet.
149

150
00:09:20,660 --> 00:09:21,230
Yes.
150

151
00:09:21,950 --> 00:09:29,150
So there is an Internet issue, which I can see over here because of which the Web application is
151

152
00:09:29,150 --> 00:09:30,980
not loading correctly.
152

153
00:09:31,700 --> 00:09:33,800
So we are almost done with the practical.
153

154
00:09:34,670 --> 00:09:41,570
I just need to show you the xss alert over here, but it's not working.
154

155
00:09:41,780 --> 00:09:42,860
Let us
155

156
00:09:47,630 --> 00:09:52,670
just sort of thing and see if where is the particular error we are getting.
156

157
00:10:00,090 --> 00:10:02,230
So the request is going to our router
157

158
00:10:02,910 --> 00:10:08,550
And from the router we are having, the area which is basically at the ISP level.
158

159
00:10:08,850 --> 00:10:11,160
So the ISP is giving some kind of error.
159

160
00:10:11,970 --> 00:10:14,280
That's why we are not able to connect.
160

161
00:10:14,550 --> 00:10:15,090
No problem.
161

162
00:10:15,390 --> 00:10:21,550
Let me just quickly switch the Wi-Fi network to another Wi-Fi.
162

163
00:10:21,900 --> 00:10:23,100
Just give me a second.
163

164
00:10:29,220 --> 00:10:32,670
OK, so let me just switch this to particular Wi-Fi network.
164

165
00:10:40,810 --> 00:10:43,330
OK, so now we are connected to the new network.
165

166
00:10:49,260 --> 00:10:52,860
And let us try again doing the traceroute
166

167
00:10:58,110 --> 00:10:59,440
Let's bring in check.
167

168
00:11:00,690 --> 00:11:00,810
Yeah.
168

169
00:11:00,840 --> 00:11:05,250
So we are receiving the ping, which means our Internet has been successfully connected.
169

170
00:11:05,940 --> 00:11:08,400
I apologize for whatever happened over here.
170

171
00:11:08,580 --> 00:11:10,680
Let's quickly get back to the application.
171

172
00:11:11,970 --> 00:11:16,190
So over here, we are overhear lets reload the application.
172

173
00:11:16,270 --> 00:11:23,130
The application has reloaded successfully and we were waiting to type the particular vulnerable parameter that
173

174
00:11:23,130 --> 00:11:24,380
we had found out was name.
174

175
00:11:24,920 --> 00:11:29,200
So name equals to script or let us use them.
175

176
00:11:29,200 --> 00:11:39,540
a source payload in which image source equals two X one error equals to confirm(1) or it's zero anything and
176

177
00:11:39,540 --> 00:11:40,140
hit enter.
177

178
00:11:42,480 --> 00:11:43,140
Yes.
178

179
00:11:43,590 --> 00:11:50,970
So we're able to get a xss, which means this particular web application is vulnerable to this
179

180
00:11:51,060 --> 00:11:52,700
Dom xss attack.
180

181
00:11:53,400 --> 00:12:00,000
So I hope you guys understood how you can utilize this particular tool to identify the vulnerable things
181

182
00:12:00,300 --> 00:12:03,000
and then you can do the attack over there.
182

183
00:12:04,530 --> 00:12:05,010
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,580 --> 00:00:04,700
Hello everyone.
1

2
00:00:04,710 --> 00:00:14,640
So in this video I'm going to show you how we can achieve XSS by giving or adding a new parameters
2

3
00:00:14,850 --> 00:00:17,780
into the headers of any application.
3

4
00:00:17,820 --> 00:00:26,250
So in this video I'm going to exploit this Web site that is optimizely dot com by giving an extra
4

5
00:00:27,270 --> 00:00:33,660
header into the web application and it will get reflected and I will try to exploit it.
5

6
00:00:34,680 --> 00:00:35,150
Yes.
6

7
00:00:35,520 --> 00:00:47,430
So if I go onto this website I will just try to go and try to take that request into burpe suite as you
7

8
00:00:47,430 --> 00:00:53,460
can see I have already taken the request into the Burpe suite and this is the request that is going to
8

9
00:00:53,580 --> 00:00:59,250
optimizely dot com as I can see you over here and that request is a GET request to utm.
9

10
00:00:59,250 --> 00:01:00,930
Campaign equals two.
10

11
00:01:01,440 --> 00:01:02,310
As you can see it.
11

12
00:01:05,280 --> 00:01:06,820
So how did I got this.
12

13
00:01:06,840 --> 00:01:13,920
I got this by intercepting optimizely dot com and then I performed a spider.
13

14
00:01:14,250 --> 00:01:22,320
And then after performing a spider I tried to see the parameters and I was able to see this.
14

15
00:01:22,890 --> 00:01:25,960
The first step was spider after spidering.
15

16
00:01:25,960 --> 00:01:33,670
You will get a lot of options and then just send one off the request of the parameters into the Burpe
16

17
00:01:33,670 --> 00:01:36,510
suite.
17

18
00:01:36,730 --> 00:01:46,670
So as you can see I gave a parameter that is utm campaign value and the value is hacktify.
18

19
00:01:47,170 --> 00:01:54,910
So if you try to see this hacktify is getting reflected into the header that is XWDF right.
19

20
00:01:55,660 --> 00:01:59,290
And it is also getting reflected at two other places.
20

21
00:01:59,350 --> 00:02:03,660
So there are total three matches into this application.
21

22
00:02:04,020 --> 00:02:04,360
Fine.
22

23
00:02:05,560 --> 00:02:15,250
So what I'm going to do right now is I'm going to give a question mark and I'm going to give a new parameter
23

24
00:02:15,310 --> 00:02:17,550
that is q equals to.
24

25
00:02:17,620 --> 00:02:25,720
So I'm adding a new param that is q equals to and I'm giving the XSS payload script alert
25

26
00:02:25,780 --> 00:02:34,780
one script close and you can see it is getting reflected as it is the new param is also getting added
26

27
00:02:34,930 --> 00:02:36,280
into the application.
27

28
00:02:36,310 --> 00:02:37,740
If you look closely.
28

29
00:02:37,840 --> 00:02:43,150
Yes perfect as it can see what you're the new parameter has been added.
29

30
00:02:43,150 --> 00:02:49,660
So the application is accepting any new arbitrary parameter that is given and the value which is the
30

31
00:02:49,670 --> 00:02:50,780
XSS payload.
31

32
00:02:51,760 --> 00:02:54,310
And it has got perfectly balance between here.
32

33
00:02:54,820 --> 00:03:00,820
So what I'm going to do right now is I'm going to just right click show response into the browser go
33

34
00:03:00,820 --> 00:03:02,710
into the website and hit enter.
34

35
00:03:03,580 --> 00:03:09,940
And if you can see that I'm able to achieve the XSS into this Web site.
35

36
00:03:09,940 --> 00:03:16,960
So in this video we learn how we can achieve XSS by adding your own parameters sometimes into the
36

37
00:03:16,960 --> 00:03:18,040
web application.
37

38
00:03:18,160 --> 00:03:20,840
You can achieve XSS.
38

39
00:03:21,130 --> 00:03:22,390
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,600 --> 00:00:02,760
Hello everyone.
1

2
00:00:02,760 --> 00:00:09,630
So till now we saw how you were able to achieve XSS by giving in characters through the keyboard
2

3
00:00:09,630 --> 00:00:11,520
input.
3

4
00:00:11,790 --> 00:00:20,600
What if a keyboard input is blocked you can still perform XSS using mouse using mouse input.
4

5
00:00:21,000 --> 00:00:25,630
So there are a variety of mouse payloads that you can use.
5

6
00:00:25,770 --> 00:00:35,820
For example on mouse over ,on mouse move ,on mouse up ,on mouse enter ,on mouse leave ,on mouse view and
6

7
00:00:35,910 --> 00:00:38,670
on mouse out.
7

8
00:00:38,670 --> 00:00:40,560
Why this mouse payload.
8

9
00:00:40,590 --> 00:00:45,210
Because they're effective in bypassing many keyboard input checks.
9

10
00:00:45,450 --> 00:00:54,780
And it is easy way so I hope you guys understood why we are going to use mouse based XSS payloads.
10

11
00:00:54,840 --> 00:01:04,290
So let's quickly go to the practical time and let's see a practical example wherein we will be able
11

12
00:01:04,290 --> 00:01:08,520
to use mouse based payloads to perform XSS.
12

13
00:01:08,950 --> 00:01:15,300
I've got one this application that there is a search field some just quickly going to type hacktify and
13

14
00:01:15,300 --> 00:01:20,870
I will hit go to see if my input is getting reflected or not.
14

15
00:01:21,750 --> 00:01:26,160
I come to know that my input is getting perfectly reflected.
15

16
00:01:26,370 --> 00:01:34,320
So now I'm going to put a payload into the reflection where it was happening into the input.
16

17
00:01:35,010 --> 00:01:43,920
So here I'm using a payload that is href that is hyper reference javascript alert work
17

18
00:01:44,730 --> 00:01:46,390
it should give alert one.
18

19
00:01:46,390 --> 00:01:52,070
when it should give the event is on mouse over what should happen.
19

20
00:01:52,070 --> 00:01:53,350
The alert ones should happen.
20

21
00:01:53,550 --> 00:01:59,940
So on mouse over alert one and I'm saying that it should be shown us.
21

22
00:01:59,950 --> 00:02:01,230
Hover me please.
22

23
00:02:02,040 --> 00:02:03,190
OK.
23

24
00:02:03,440 --> 00:02:05,780
So I'm just going to copy this payload.
24

25
00:02:06,060 --> 00:02:07,150
I'm going to paste it here .
25

26
00:02:07,160 --> 00:02:14,370
And when I let go you will be able to see that searched for hacktify in that place.
26

27
00:02:14,370 --> 00:02:15,050
There will be.
27

28
00:02:15,050 --> 00:02:18,500
Hold me please Yes.
28

29
00:02:18,500 --> 00:02:19,220
Perfect.
29

30
00:02:19,220 --> 00:02:26,620
So as you can see it is hover me please and then I will try to take my mouse pointer on hover me 
30

31
00:02:26,630 --> 00:02:27,400
please.
31

32
00:02:27,500 --> 00:02:33,160
You will be able to see that and XSS will happen.
32

33
00:02:33,160 --> 00:02:34,160
So let me just go there.
33

34
00:02:34,190 --> 00:02:34,850
Perfect.
34

35
00:02:34,910 --> 00:02:35,810
As you can see.
35

36
00:02:35,840 --> 00:02:37,010
Let me jagain do that.
36

37
00:02:37,310 --> 00:02:39,200
Yes once more.
37

38
00:02:39,200 --> 00:02:39,840
Yes.
38

39
00:02:39,860 --> 00:02:47,760
So whenever I'm taking my mouse pointer to hover me please I'm getting an XSS.
39

40
00:02:47,810 --> 00:02:53,050
I hope you guys understood how we can perform XSS using mouse.
40

41
00:02:53,090 --> 00:02:53,540
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,750 --> 00:00:03,530
Hello everyone.
1

2
00:00:03,540 --> 00:00:10,740
So in this video we are going to see XSS with the help of mouse on a live application.
2

3
00:00:10,740 --> 00:00:13,800
So as we can see I'm on to a website.
3

4
00:00:13,860 --> 00:00:15,180
UbrainTV.com.
4

5
00:00:16,350 --> 00:00:17,840
So what I'm going to do is.
5

6
00:00:17,850 --> 00:00:21,710
And first I'm going to show you that a reflection is happening here.
6

7
00:00:21,720 --> 00:00:30,030
So I'm just going to type hacktify and do a search as you can see that hacktify is getting reflected
7

8
00:00:30,120 --> 00:00:31,200
over here.
8

9
00:00:31,260 --> 00:00:32,220
Perfect.
9

10
00:00:32,220 --> 00:00:39,450
So what I'm going to do is I'm going to take the mouse payload and I'm going to put it in the place
10

11
00:00:39,510 --> 00:00:48,510
of hacktify that I searched for the same payload and gong to go here I'm going to put it here and
11

12
00:00:48,570 --> 00:00:55,290
I will do a search as you can see it is getting reflected in.
12

13
00:00:55,290 --> 00:00:58,210
Hover me please.
13

14
00:00:58,230 --> 00:01:03,840
So now I will try to take my mouse pointer to hover me please.
14

15
00:01:04,110 --> 00:01:07,900
And we will observe that an XSS will happen.
15

16
00:01:08,070 --> 00:01:14,910
Perfect as you can see an XSS occurs when I try to take my most payload into.
16

17
00:01:14,970 --> 00:01:16,940
Hover me please.
17

18
00:01:17,040 --> 00:01:19,260
Mouse pointer on hover me please.
18

19
00:01:19,260 --> 00:01:23,910
Because of the mouse payload for our XSS.
19

20
00:01:23,910 --> 00:01:30,840
I hope you guys understood how we can achieve XSS using mouse payload.
20

21
00:01:30,840 --> 00:01:39,480
Also in the next video I'm going to show you a lot of mouse based payload through which you can achieve
21

22
00:01:39,810 --> 00:01:40,620
XSS.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,570 --> 00:00:03,710
Hello everyone.
1

2
00:00:03,710 --> 00:00:12,380
So in this video we are going to see how we can do different types of XSS using mouse base payloads.
2

3
00:00:12,380 --> 00:00:18,470
So in this video we will see a lot of mouse based event through which we can achieve XSS.
3

4
00:00:19,910 --> 00:00:25,940
So let's start by giving something into the search box.
4

5
00:00:26,060 --> 00:00:33,860
So what I'm going to do is let's say I'm going to try the first payload that is mouse over so I'm just
5

6
00:00:33,860 --> 00:00:35,480
giving the mouse over payload.
6

7
00:00:35,480 --> 00:00:46,250
And if you see if I take my mouse over to the image where the reflection is I will get XSS alert
7

8
00:00:46,970 --> 00:00:52,550
why I'm getting this exercise alert because this payload is off on mouse over.
8

9
00:00:52,760 --> 00:01:01,580
So if you look closely then image source equals two X. This is not a valid source obviously.
9

10
00:01:01,580 --> 00:01:07,790
Then if my mouse goes onto that specific image source then there should be a alert.
10

11
00:01:08,090 --> 00:01:09,860
So I'm getting alert.
11

12
00:01:09,920 --> 00:01:11,000
OK.
12

13
00:01:11,020 --> 00:01:17,440
And I have encoded alert one to string dot from character code 88 83 88.
13

14
00:01:17,510 --> 00:01:17,850
OK.
14

15
00:01:17,900 --> 00:01:20,660
So this is basically the encoded version.
15

16
00:01:20,660 --> 00:01:23,020
Do not worry about that.
16

17
00:01:23,060 --> 00:01:30,920
So this is the first type in which I have shown you how we can get a XSS by on mouse over.
17

18
00:01:31,730 --> 00:01:32,480
OK fine.
18

19
00:01:33,170 --> 00:01:40,560
So now what I'm going to do is I'm going to choose another payload that is on mouse move.
19

20
00:01:41,030 --> 00:01:49,930
So basically when I will move my mouse over my reflection I will get an XSS.
20

21
00:01:49,970 --> 00:01:52,310
So let me just take my mouse over there.
21

22
00:01:52,340 --> 00:01:53,540
Let me try to show you again.
22

23
00:01:53,810 --> 00:02:00,100
So whenever I'm taking my mouse over to the reflection I'm getting a XSS.
23

24
00:02:00,170 --> 00:02:01,520
Let me try one more payload.
24

25
00:02:01,580 --> 00:02:04,520
And this is on mouse wheel.
25

26
00:02:04,880 --> 00:02:14,270
This means whenever I'm trying to move my mouse wheel over the reflection of the payload I will get
26

27
00:02:14,270 --> 00:02:15,350
an XSS.
27

28
00:02:15,380 --> 00:02:16,370
So let's see this.
28

29
00:02:17,330 --> 00:02:26,440
I've copied that payloadi will pasted here and I will hit Go Now if I take my mouse pointer onto the reflection
29

30
00:02:26,540 --> 00:02:32,570
I will get to XSS because this is not an on mouse over or on most move payload.
30

31
00:02:32,570 --> 00:02:35,280
This is on mouse wheel.
31

32
00:02:35,390 --> 00:02:37,080
You can see on most scroll also.
32

33
00:02:37,830 --> 00:02:42,350
So I will just take my pointer over there so you can see it is not happening XSS.
33

34
00:02:42,590 --> 00:02:46,270
But when I scrolled my mouse I'll again take that and I will scroll.
34

35
00:02:46,290 --> 00:02:48,050
I will give a scroll to my mouse.
35

36
00:02:48,050 --> 00:02:49,220
Perfect.
36

37
00:02:49,220 --> 00:02:51,090
So it is working perfectly fine.
37

38
00:02:51,200 --> 00:02:55,740
Whenever I tried to scroll my mouse I'm getting an XSS.
38

39
00:02:55,760 --> 00:03:03,320
Similarly there are other payloads like on mouse up on most out on most down and a variety of XSS
39

40
00:03:03,320 --> 00:03:05,820
payloads based on mouse events.
40

41
00:03:06,260 --> 00:03:12,150
So I'm going to share this list into the description that you guys can take it.
41

42
00:03:12,380 --> 00:03:18,830
So I hope you guys understood how we can achieve XSS through mouse payloads and mouse events whenever
42

43
00:03:18,830 --> 00:03:20,180
the keyboard input is blocked.
43

44
00:03:21,800 --> 00:03:22,880
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,080 --> 00:00:02,400
Hello everyone.
1

2
00:00:02,400 --> 00:00:08,340
So in this video we are going to see what are XSS polyglot.
2

3
00:00:08,340 --> 00:00:10,700
So what does a polyglot mean.
3

4
00:00:10,710 --> 00:00:17,640
So according to the dictionary definition polyglot is something which is multilingual or the person
4

5
00:00:17,880 --> 00:00:22,610
who knows many languages  is known as polyglot.
5

6
00:00:22,680 --> 00:00:27,190
So how we are going to use polyglot in XSS.
6

7
00:00:27,210 --> 00:00:37,080
So basically we are going to combine XSS payloads different types of payloads to make one new payload
7

8
00:00:37,380 --> 00:00:40,240
which will be called as a polyglot.
8

9
00:00:41,430 --> 00:00:43,380
So why do we use polyglot.
9

10
00:00:43,650 --> 00:00:50,340
Because it is effective in bypassing many input checks and we get easy win.
10

11
00:00:50,950 --> 00:00:51,570
Okay.
11

12
00:00:51,720 --> 00:01:01,050
So it's practical time now and let's see how can we use a polyglot which is nothing just but a mixture
12

13
00:01:01,050 --> 00:01:10,410
of many different XSS payloads which will help us achieve success in executing and exploiting XSS.
13

14
00:01:11,400 --> 00:01:13,210
So let's see the practical now.
14

15
00:01:13,560 --> 00:01:21,000
I'm on to a website which is optimizely.com so I'm going to find XSS onto this website using
15

16
00:01:21,000 --> 00:01:22,710
an XSS polyglot
16

17
00:01:26,750 --> 00:01:34,330
so well what I'm going to do is I'm just going to capture the request of optimizely into Burpe suite
17

18
00:01:34,340 --> 00:01:35,570
first.
18

19
00:01:35,570 --> 00:01:38,540
So I have captured the request right.
19

20
00:01:38,660 --> 00:01:45,530
I'm just going to send this to spiders because I want to Spider many more parameters as I'm not able
20

21
00:01:45,530 --> 00:01:50,450
to get any parameters right now from the web application as there is no input.
21

22
00:01:50,750 --> 00:01:57,170
So I'm just going to send this request to a spider so the spider will crawl forward many url and
22

23
00:01:57,170 --> 00:01:59,380
try to find a parameter for me
23

24
00:02:03,600 --> 00:02:04,820
I will turn this off.
24

25
00:02:04,830 --> 00:02:09,240
I'll go in spider and you can see spider is running.
25

26
00:02:09,240 --> 00:02:10,560
I will go to the target.
26

27
00:02:10,620 --> 00:02:18,120
I will click on filter and I will click show only in scope items because I only want to see all the
27

28
00:02:18,120 --> 00:02:22,950
requests for optimizely only because optimizely in my scope.
28

29
00:02:22,950 --> 00:02:28,790
Now if you see the optimizely is being added into my scope I'm going to right click and do a spider
29

30
00:02:28,810 --> 00:02:34,200
again because I want to get many more url which contains some parameter.
30

31
00:02:34,710 --> 00:02:42,210
So as you can see you are listed on the Url which contains parameters as I will double click on parameter
31

32
00:02:42,570 --> 00:02:47,670
so all the parameters will automatically come up.
32

33
00:02:47,670 --> 00:02:54,150
Now what I'm going to do is I'm going to search for a parameter using the search feature of burpe.
33

34
00:02:54,600 --> 00:03:00,990
So I clicked on burpe and search now and moved the search for a parameter that is UTM underscore
34

35
00:03:01,260 --> 00:03:01,770
source
35

36
00:03:04,500 --> 00:03:07,200
it is not necessary that you search for this parameter.
36

37
00:03:07,200 --> 00:03:10,520
Only you can try to get any parameter you want.
37

38
00:03:10,560 --> 00:03:14,580
I have just taken for instance a parameter that is UTM underscore.
38

39
00:03:14,590 --> 00:03:15,000
Source
39

40
00:03:17,920 --> 00:03:24,430
I would click on in scope only because optimizer is in my scope and I want to see only from 
40

41
00:03:24,440 --> 00:03:25,710
optimizely.
41

42
00:03:26,410 --> 00:03:32,440
I will uncheck Response Headers and response body because I do not want this parameter to be searched
42

43
00:03:32,470 --> 00:03:33,200
in response.
43

44
00:03:33,280 --> 00:03:37,670
I want this parameter in request only I will hit go.
44

45
00:03:37,780 --> 00:03:44,140
As you can see it is searching for this parameters and you can closely see that I've already got this
45

46
00:03:44,140 --> 00:03:46,380
parameter in utm campaign.
46

47
00:03:46,480 --> 00:03:50,510
Primary nav Academy dark utm campaign Academy light.
47

48
00:03:50,530 --> 00:03:52,750
So the parameter is already there
48

49
00:03:55,690 --> 00:04:02,290
and it can see here also the parameter is there and the parameter is again the here and here.
49

50
00:04:03,010 --> 00:04:08,760
So I'm going to choose any of the specific requests and I'm going to send this request into the
50

51
00:04:08,760 --> 00:04:09,360
repeater tab
51

52
00:04:12,130 --> 00:04:14,440
after sending this request to the repeater.
52

53
00:04:14,440 --> 00:04:20,620
You can see utm campaign parameter is here and the value is already there.
53

54
00:04:21,580 --> 00:04:28,720
So what I'm going to do is I'm going to send this to intruder now because we are going to attack this
54

55
00:04:28,870 --> 00:04:34,130
parameter for XSS polyglot after sending this to intruder.
55

56
00:04:34,150 --> 00:04:37,010
I will quickly go into the intruder tab.
56

57
00:04:37,420 --> 00:04:42,740
I will go into the position tab and I'm going to set a position for this attack to happen.
57

58
00:04:42,880 --> 00:04:48,870
So my injecations point or position you can see is utm underscore campaign equals two.
58

59
00:04:49,120 --> 00:04:55,550
So I'm going to choose primary nav Academy light because this is the value of the parameter and I'm
59

60
00:04:55,570 --> 00:04:57,380
going to click on add.
60

61
00:04:57,640 --> 00:05:00,380
So here is my injection point.
61

62
00:05:00,490 --> 00:05:07,080
So I'll just move on to the payload tab and I'm going to load the payload which contains the XSS
62

63
00:05:07,080 --> 00:05:10,070
as polyglot and I'm going to start attacking.
63

64
00:05:10,690 --> 00:05:16,530
I'm going to give the payload polyglot list into the description with this video.
64

65
00:05:17,380 --> 00:05:23,140
As soon as I start to attack you can see the attackers running and all the polyglots are been hitting
65

66
00:05:23,140 --> 00:05:23,440
there.
66

67
00:05:24,910 --> 00:05:32,910
Let's wait for the response length which becomes the maximum.
67

68
00:05:33,220 --> 00:05:38,540
Any request with the maximum length means our payload has successfully executed.
68

69
00:05:38,590 --> 00:05:40,500
So let me double click on length.
69

70
00:05:40,570 --> 00:05:47,610
As you can see this specific request has the maximum length so I'm going to see the payload here.
70

71
00:05:47,950 --> 00:05:49,780
Yeah I can see the payload.
71

72
00:05:49,930 --> 00:05:56,470
Let me just right click and do show response in browser and let me show the response in browser and
72

73
00:05:56,470 --> 00:06:00,980
check that XSS has happened or not.
73

74
00:06:01,110 --> 00:06:13,160
So let me just hit enter and wait and perfect as you can see I am able to achieve XSS to this polyglot.
74

75
00:06:13,270 --> 00:06:13,790
Perfect.
75

76
00:06:14,200 --> 00:06:17,580
Let me send this to decoder and do a smart decode.
76

77
00:06:17,750 --> 00:06:19,390
And now you can see the payload.
77

78
00:06:19,390 --> 00:06:26,650
This is the payload that was hit into the injection point and because of this I am able to achieve my
78

79
00:06:26,970 --> 00:06:28,290
XSS.
79

80
00:06:28,570 --> 00:06:36,450
So I hope you guys understood that how you can do XSS by using a polyglot and the burpe suite intruder
80

81
00:06:36,500 --> 00:06:39,690
the function in the next video.
81

82
00:06:39,730 --> 00:06:45,730
I'm going to show you how we can break down the polyglot and we are going to understand that what
82

83
00:06:45,820 --> 00:06:50,840
actually happened in the background because of which the XSS came.
83

84
00:06:51,100 --> 00:06:51,600
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,840 --> 00:00:02,480
Hello everyone.
1

2
00:00:02,490 --> 00:00:09,600
So in the previous feed you we saw how we were able to achieve our XSS on our website which was
2

3
00:00:09,630 --> 00:00:14,190
optimizely dot.com com using XSS polyglot.
3

4
00:00:14,250 --> 00:00:22,860
So in the previous video we achieved the XSS by giving a polyglot XSS payload to Burpe intruder
4

5
00:00:22,860 --> 00:00:27,880
functionality and we achieved successful XSS.
5

6
00:00:27,960 --> 00:00:37,800
So in this video we are going to do a break down of that specific polyglot payload that we used.
6

7
00:00:37,800 --> 00:00:43,290
So let's see how we were able to achieve the XSS using that payload.
7

8
00:00:44,730 --> 00:00:51,780
So as you can see these are the marquee tags which are basically nothing but does the marquee function
8

9
00:00:52,080 --> 00:00:55,660
which we did not use into our attack.
9

10
00:00:55,950 --> 00:00:58,470
Second is a simple image payload.
10

11
00:00:58,470 --> 00:00:59,400
We know this.
11

12
00:00:59,460 --> 00:01:03,510
This is image source equals to X no source like that.
12

13
00:01:03,510 --> 00:01:05,600
So it is going to give a error on error.
13

14
00:01:05,610 --> 00:01:09,050
It should say confirm one next is nothing.
14

15
00:01:09,060 --> 00:01:15,760
This plaintext tags plaintext dart and plaintext close next is on mouse over prompt one.
15

16
00:01:15,840 --> 00:01:18,600
This is an mouseover payload that we use.
16

17
00:01:18,600 --> 00:01:23,830
We already saw what our mouseover payload into the mouse of over video section.
17

18
00:01:23,850 --> 00:01:25,740
Next is script prompt one.
18

19
00:01:25,740 --> 00:01:28,640
This is basic a simple script payload again.
19

20
00:01:29,130 --> 00:01:35,820
Next added is gmail dot com which is extracted which is of no use into a polyglot.
20

21
00:01:35,820 --> 00:01:42,930
Next is index formaction = javascript alert XSS types submit which is XSS on submit
21

22
00:01:43,710 --> 00:01:50,610
next is script alert one with the same as the simple script payload and the last one is simple image
22

23
00:01:50,610 --> 00:01:51,030
payload.
23

24
00:01:51,030 --> 00:01:54,270
But again of no use into this attack.
24

25
00:01:54,270 --> 00:02:02,700
So I hope you guys understood how this polyglot was made by the mixture of different XSS attack
25

26
00:02:02,700 --> 00:02:10,950
vectors combined into one XSS payload which we used on a web application and we were able to achieve
26

27
00:02:11,030 --> 00:02:16,090
a successful XSS so thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,990 --> 00:00:02,610
Hello everyone.
1

2
00:00:02,880 --> 00:00:07,500
And this video we are waiting to see XSS exploitation.
2

3
00:00:07,500 --> 00:00:13,820
So we will do XSS exploitation to url redirection.
3

4
00:00:13,830 --> 00:00:18,780
here we are going to make the victim redirect to what evil web site.
4

5
00:00:19,540 --> 00:00:22,260
Basically we will find the injection point.
5

6
00:00:22,260 --> 00:00:29,370
We can find it either manually or either using Burpe suite spider feature.
6

7
00:00:29,370 --> 00:00:37,800
You guys already know how to use Burpe suite spider feature and take parameters from that after finding
7

8
00:00:37,790 --> 00:00:38,650
a parameter.
8

9
00:00:38,730 --> 00:00:44,840
You have to inject the XSS payload in the parameter and further you have to check that if you're
9

10
00:00:44,880 --> 00:00:47,030
able to explain the excesses.
10

11
00:00:48,000 --> 00:00:54,000
So in this video we are going to do a url redirection into one of the parameter and we will
11

12
00:00:54,000 --> 00:00:55,830
see that can we achieve.
12

13
00:00:55,830 --> 00:01:01,960
url redirect and make the victim redirect to our evil web site.
13

14
00:01:02,010 --> 00:01:08,280
If the victim redirects to the evil web site then this is a successful exploitation of XSS using
14

15
00:01:08,400 --> 00:01:10,690
url redirection.
15

16
00:01:10,770 --> 00:01:16,440
So let's see the video in action in which you are going to successfully exploit it
16

17
00:01:21,110 --> 00:01:24,600
so yes we are going to see that.
17

18
00:01:24,620 --> 00:01:26,360
I went to a web application.
18

19
00:01:26,520 --> 00:01:32,420
I'm just going to search hacktify and I'm going to head go as you can see hacktify is getting reflected
19

20
00:01:32,480 --> 00:01:34,510
through this input box.
20

21
00:01:34,550 --> 00:01:35,070
Perfect.
21

22
00:01:35,600 --> 00:01:43,730
So what I'm going to do is I am going to put a payload into the search box and that payload is written
22

23
00:01:43,740 --> 00:01:44,810
over here.
23

24
00:01:44,930 --> 00:01:47,090
So the payload is something like this.
24

25
00:01:47,270 --> 00:01:50,060
Script tag document dot location.
25

26
00:01:50,060 --> 00:01:54,500
dot href for reference and a website name.
26

27
00:01:54,500 --> 00:01:58,900
That is  http.hacktify.in and script tag close.
27

28
00:01:58,910 --> 00:02:00,870
So I'm going to copy this payload.
28

29
00:02:01,040 --> 00:02:05,280
I'm going to go into the search tab and I'm going to search for this.
29

30
00:02:05,480 --> 00:02:13,280
And if this Web site redirect me to that evil dot com for instance in this case hacktify.in
30

31
00:02:13,340 --> 00:02:20,550
in line we have successfully exploited XSS to url  redirection and let's see this.
31

32
00:02:20,930 --> 00:02:25,690
And this Web site successfully transfers to hacktify.in Web site.
32

33
00:02:25,760 --> 00:02:26,310
Perfect.
33

34
00:02:27,470 --> 00:02:31,610
So now let's do this on a live Web site.
34

35
00:02:31,610 --> 00:02:35,630
I'm going to search for hacktify and search.
35

36
00:02:35,630 --> 00:02:37,170
Do I get the reflection.
36

37
00:02:37,310 --> 00:02:37,810
Perfect.
37

38
00:02:37,810 --> 00:02:39,320
I get the reflection.
38

39
00:02:39,320 --> 00:02:44,130
So now here i m going to put the same payload and hit search.
39

40
00:02:44,450 --> 00:02:50,840
If this live web site redirects me then it is vulnerable and it does so.
40

41
00:02:51,280 --> 00:02:51,980
Perfect.
41

42
00:02:51,980 --> 00:02:54,970
I'll just go back and show you that I was onto this Web site.
42

43
00:02:54,980 --> 00:02:58,420
Ubrain TV and it has redirected me to hacktify.in.
43

44
00:02:58,460 --> 00:02:59,920
That is the attackers Web site.
44

45
00:03:00,590 --> 00:03:09,200
So I hope you understood how we can do successful exploitation of XSS to URL redirection and
45

46
00:03:09,230 --> 00:03:11,390
willing to share this payload with every one of you.
46

47
00:03:11,960 --> 00:03:13,410
Okay.
47

48
00:03:13,940 --> 00:03:20,510
So in this video we are going to see one more thing that URL redirection with a click.
48

49
00:03:21,030 --> 00:03:22,080
Okay.
49

50
00:03:22,490 --> 00:03:27,950
So now the website was automatically getting redirected to the evil dot com.
50

51
00:03:28,380 --> 00:03:34,700
But now we will see that we can make the redirect based on a click.
51

52
00:03:34,710 --> 00:03:38,370
Also for us for that we are going to give a href.
52

53
00:03:38,450 --> 00:03:45,890
So as you can see I've given a href that is hacktify.in and I am writing the log in here.
53

54
00:03:46,160 --> 00:03:51,690
What I'm going to do is I'm going to copy this payload and go again to the search functionality head
54

55
00:03:51,700 --> 00:03:52,490
go.
55

56
00:03:52,700 --> 00:03:56,140
And you can see log in here is reflected.
56

57
00:03:56,150 --> 00:04:03,260
But this time when the victim will click on log in here he will be redirected automatically to the evil
57

58
00:04:03,260 --> 00:04:05,730
web site that is haktify.in Web site.
58

59
00:04:05,750 --> 00:04:07,720
Let's do this onto the live Web site.
59

60
00:04:07,740 --> 00:04:14,980
Also as you can see it I'm going to search this payload and you can see there is a button which is log
60

61
00:04:14,980 --> 00:04:16,140
in here.
61

62
00:04:16,490 --> 00:04:22,790
It is reflected now when the victim tries to click that by thinking that this is the log in button and
62

63
00:04:22,790 --> 00:04:24,530
it clicks on log in here.
63

64
00:04:24,680 --> 00:04:28,340
He will be redirected to the evil web site.
64

65
00:04:29,990 --> 00:04:30,500
OK.
65

66
00:04:30,500 --> 00:04:37,020
So I hope you guys understood both the test cases of URL redirection through XSS.
66

67
00:04:37,040 --> 00:04:37,520
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,140 --> 00:00:02,250
Hello everyone.
1

2
00:00:02,250 --> 00:00:10,140
So in this video of XSS exploitation we are going to see how can we perform phishing using XSS.
2

3
00:00:10,290 --> 00:00:16,660
So here we are going to make the victim logging into phishing Web site or an evil web site.
3

4
00:00:16,890 --> 00:00:24,570
We will confuse the victim that he may be get tricked into logging into the attackers Web site.
4

5
00:00:24,570 --> 00:00:31,470
So here again we will try to find a injection point using Burpe suite spider feature or manually and
5

6
00:00:31,470 --> 00:00:38,520
then we are going to inject the XSS payload in the parameter and we will finally achieve phishing
6

7
00:00:38,640 --> 00:00:40,440
through XSS.
7

8
00:00:40,860 --> 00:00:43,230
And the last thing i frames are love.
8

9
00:00:43,230 --> 00:00:49,320
They are very important in achieving fishing using XSS exploitation.
9

10
00:00:49,320 --> 00:00:56,750
So let's see the practical in how we can achieve this phishing using XSS.
10

11
00:00:56,980 --> 00:00:58,530
I went on this Web site.
11

12
00:00:58,530 --> 00:01:00,570
So you're into the search box.
12

13
00:01:00,570 --> 00:01:04,920
I'm going to again search for hacktify and see the reflection.
13

14
00:01:04,920 --> 00:01:08,560
Yes I'm getting the reflection now.
14

15
00:01:08,600 --> 00:01:09,030
here in.
15

16
00:01:09,050 --> 00:01:16,020
I'm going to put a payload as you can see the payload iframe source equals to hacktify.in
16

17
00:01:16,020 --> 00:01:16,930
Web site.
17

18
00:01:17,040 --> 00:01:21,630
height equals to 100%,width equals to 100% and iframe close.
18

19
00:01:21,690 --> 00:01:24,540
So I'm just going to copy this payload.
19

20
00:01:24,570 --> 00:01:31,790
This is basically a iframe payload to copy this go here paste it and hit go
20

21
00:01:34,730 --> 00:01:35,240
awesome.
21

22
00:01:35,250 --> 00:01:39,870
So as you can see this Web site is loading  a iframe.
22

23
00:01:39,870 --> 00:01:42,750
This Web site is loading a iframe for me.
23

24
00:01:42,870 --> 00:01:45,060
Let me just go to another one.
24

25
00:01:45,060 --> 00:01:46,240
Let me just go here.
25

26
00:01:46,300 --> 00:01:48,550
Try to put it here and let's see.
26

27
00:01:48,690 --> 00:01:49,510
Yes.
27

28
00:01:49,590 --> 00:01:56,700
So in another parameter also this Web site is loading in a frame which means this Web site is vulnerable
28

29
00:01:56,700 --> 00:01:57,490
to phishing.
29

30
00:01:57,550 --> 00:01:57,880
How.
30

31
00:01:58,440 --> 00:02:05,460
If I adjust the width and height properly according to the page then this hacktify.in can overlay
31

32
00:02:05,490 --> 00:02:11,680
the whole Web site and through which I can achieve phishing I can make a similar look like Web site
32

33
00:02:12,150 --> 00:02:13,800
like the victims Web site.
33

34
00:02:13,800 --> 00:02:22,140
And this way I can trick the user in logging in into my attacker's application.
34

35
00:02:22,290 --> 00:02:25,480
So let's see the example onto a live application also.
35

36
00:02:25,920 --> 00:02:32,720
So in this Web site I'm going to take the same payload hit it here and hit search.
36

37
00:02:33,150 --> 00:02:37,020
As you can see the website will be loaded into a iframe.
37

38
00:02:38,700 --> 00:02:46,890
Similarly if I set the width and height then I can make this overlay on the whole Web site and make
38

39
00:02:47,220 --> 00:02:52,320
the user trick into logging into the attackers Web site.
39

40
00:02:52,320 --> 00:02:56,890
Now for one more demonstration what I'm going to do is this is my Web site.
40

41
00:02:56,890 --> 00:03:04,900
This is that is srsecure.xyz and I have made png image which is your Web site is hacked by 
41

42
00:03:04,900 --> 00:03:05,450
hacktify.
42

43
00:03:05,680 --> 00:03:06,960
How would website is down.
43

44
00:03:06,960 --> 00:03:08,600
Kindly go to its https.
44

45
00:03:08,670 --> 00:03:09,960
Evil dot com.
45

46
00:03:10,170 --> 00:03:15,930
So I'm just going to take this image and I'm going to put this into an image source and I'm going to
46

47
00:03:15,930 --> 00:03:25,660
call this specific image source and this image into onto Harvard Web site.
47

48
00:03:25,680 --> 00:03:32,490
So in this Harvard Web site I was able to load my image.
48

49
00:03:33,330 --> 00:03:33,790
Yes.
49

50
00:03:33,810 --> 00:03:35,080
So can you see this.
50

51
00:03:35,130 --> 00:03:42,690
This is also our type of phishing attack in which I can send this link to any user and the user will
51

52
00:03:42,690 --> 00:03:48,770
think oh no the Harvard University website is down or it is hacked by hacktify.
52

53
00:03:49,020 --> 00:03:52,590
I need to go to the new Web site link that is evil dot com.
53

54
00:03:52,950 --> 00:03:59,920
So this is also a part of phishing that we can achieve to XSS exploitation.
54

55
00:03:59,970 --> 00:04:02,160
I hope you guys understood.
55

56
00:04:02,160 --> 00:04:02,640
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,870 --> 00:00:02,540
Hello everyone.
1

2
00:00:02,550 --> 00:00:08,360
So in this video we are going to see XSS exploitation of cookie stealer.
2

3
00:00:09,720 --> 00:00:15,960
So as you can see I went to an application were in on the left side I can see there is a search field.
3

4
00:00:16,710 --> 00:00:20,460
So in the search field I'm going to type something.
4

5
00:00:20,700 --> 00:00:23,740
Let's say I type hacktify and head go.
5

6
00:00:23,760 --> 00:00:31,290
So as you can see hacktify is getting reflected which means there is a possibility wherein I can try
6

7
00:00:31,290 --> 00:00:38,700
to put an payload and it may get reflected or executed.
7

8
00:00:38,700 --> 00:00:45,030
So what I'm going to do right now is I will just show you by putting this payload that we already know
8

9
00:00:45,510 --> 00:00:47,550
which is document dot cookie.
9

10
00:00:47,580 --> 00:00:52,890
So by hitting this payload we're going to see the cookie of this application.
10

11
00:00:52,890 --> 00:00:55,830
So let's see if we're able to get the cookie.
11

12
00:00:55,830 --> 00:00:56,310
Perfect.
12

13
00:00:57,090 --> 00:01:01,600
So as you can see we got our alert but the alert was empty.
13

14
00:01:01,620 --> 00:01:02,850
Why.
14

15
00:01:02,910 --> 00:01:06,180
Because the application did not give us any cookie.
15

16
00:01:06,240 --> 00:01:15,540
So the first prerequisite of doing cookies stealing exploitation on XSS is the user must be logged
16

17
00:01:15,720 --> 00:01:16,800
into the application.
17

18
00:01:16,800 --> 00:01:23,250
Obviously if the user is not logged in into the application the application will not assign a cookie
18

19
00:01:23,280 --> 00:01:25,610
to that specific user.
19

20
00:01:25,830 --> 00:01:26,530
Fine.
20

21
00:01:26,550 --> 00:01:30,120
So let's just quickly log into the application
21

22
00:01:33,970 --> 00:01:34,950
before logging in.
22

23
00:01:34,960 --> 00:01:36,780
Let's understand this payload.
23

24
00:01:36,850 --> 00:01:44,550
So this is script document dot location dot href which means this is the location of the new hyperlink.
24

25
00:01:45,540 --> 00:01:48,930
were in this is the link.
25

26
00:01:49,250 --> 00:01:55,890
This is the IP address of the attacker which contains a port number that is one two three four.
26

27
00:01:56,110 --> 00:01:59,060
And then it is the end point which is Cookie.
27

28
00:01:59,410 --> 00:02:06,160
And to this end point what will come it is going to come document dot cookie.
28

29
00:02:06,220 --> 00:02:12,790
So whatever the output of document dot cookie it will be send it to this particular IP address on this
29

30
00:02:12,790 --> 00:02:13,550
port.
30

31
00:02:13,750 --> 00:02:16,580
And on this end point that is Cookie.
31

32
00:02:16,810 --> 00:02:20,470
Remember you can take this end point whatever you want.
32

33
00:02:20,470 --> 00:02:23,540
I have just taken the name is Cookie.
33

34
00:02:24,280 --> 00:02:25,900
You can choose anything that you want.
34

35
00:02:26,080 --> 00:02:29,260
And finally I will close the script tag.
35

36
00:02:29,260 --> 00:02:30,430
Perfect.
36

37
00:02:30,430 --> 00:02:34,390
So we have made our payload.
37

38
00:02:34,390 --> 00:02:42,550
But to do this attack we need to start our listener that is our server wherein we will get the cookie
38

39
00:02:42,700 --> 00:02:43,930
of the user.
39

40
00:02:43,930 --> 00:02:44,800
Right.
40

41
00:02:44,830 --> 00:02:54,430
So for that we just open up your terminal and you should have Python installed as a prerequisite, installation
41

42
00:02:54,430 --> 00:02:55,780
of Python is very simple.
42

43
00:02:55,780 --> 00:03:01,990
For Windows based computers as well as Linux based computers for Windows computers you can download it
43

44
00:03:01,990 --> 00:03:03,770
from Python dot --, python.
44

45
00:03:03,790 --> 00:03:06,550
2.7 and you can just install it.
45

46
00:03:06,550 --> 00:03:09,830
It's very simple process after installation.
46

47
00:03:10,210 --> 00:03:14,630
You can start a listener or a server with just I'm going to show right now.
47

48
00:03:14,920 --> 00:03:21,840
For those users who are using  kali Linux or parrot os basically they've been based OS do not worry.
48

49
00:03:21,840 --> 00:03:25,240
Python is pre installed into these types of destros.
49

50
00:03:25,360 --> 00:03:26,860
Perfect.
50

51
00:03:26,890 --> 00:03:29,150
So you're in.
51

52
00:03:29,710 --> 00:03:38,020
I'm going to try Python then hyphen M hyphen M stands for module I'm going to start a module that is
52

53
00:03:38,260 --> 00:03:41,040
simple http server.
53

54
00:03:41,090 --> 00:03:49,970
Remember you have to type this the same way as I have typed ,s capital http capital and server s capital.
54

55
00:03:50,470 --> 00:03:52,080
Okay perfect.
55

56
00:03:52,090 --> 00:03:53,770
So let's move further.
56

57
00:03:54,040 --> 00:03:58,370
Now I'm going to type the port number wherein you want to start the server.
57

58
00:03:58,420 --> 00:04:00,310
So I have given the port number.
58

59
00:04:00,310 --> 00:04:02,210
That is one two three four.
59

60
00:04:02,380 --> 00:04:03,580
Perfect.
60

61
00:04:03,580 --> 00:04:07,000
So let's see what is the IP address of the attacker.
61

62
00:04:07,510 --> 00:04:13,150
So I'm going to type ifconfig and ifconfig will list down the IP addresses for my machine
62

63
00:04:13,660 --> 00:04:15,070
for Windows based computers.
63

64
00:04:15,070 --> 00:04:17,650
The command this IPconfig.
64

65
00:04:17,650 --> 00:04:24,920
Perfect as you can see this is the IP address of my machine which is basically the attackers machine.
65

66
00:04:25,330 --> 00:04:32,500
I will just take this IP and this port number go into my script and write it over there as you can see
66

67
00:04:32,980 --> 00:04:35,320
I've given it over there.
67

68
00:04:35,350 --> 00:04:41,710
Next thing is this end point you can take this endpoint anything you want and i mjust going to take it
68

69
00:04:41,710 --> 00:04:45,640
as cookie you can write anything perfect.
69

70
00:04:45,700 --> 00:04:48,550
I already explained what is this document dot cookie.
70

71
00:04:48,700 --> 00:04:54,860
It is basically what will give the cookie of that vulnerable website.
71

72
00:04:55,030 --> 00:04:55,530
Perfect.
72

73
00:04:56,260 --> 00:04:57,940
So now we are ready with our payload
73

74
00:05:00,670 --> 00:05:02,510
through which we are going to perform.
74

75
00:05:02,530 --> 00:05:08,540
Cookie stealing let's before doing the cookie stealing.
75

76
00:05:08,540 --> 00:05:15,580
Let's understand that our listeners or the attackers python server is working or not.
76

77
00:05:15,700 --> 00:05:18,820
Let's check that so for that I'm going to.
77

78
00:05:18,820 --> 00:05:24,130
In my browser and I'm going to give this endpoint and I'm just going to type.
78

79
00:05:25,000 --> 00:05:33,880
Let's say Cookie equals to checking if this works and I'm going to enter.
79

80
00:05:33,910 --> 00:05:39,040
Obviously I'm going to get to error because there is no end point like Cookie equals to checking if this
80

81
00:05:39,040 --> 00:05:42,290
works but the attacker will get this.
81

82
00:05:42,310 --> 00:05:48,250
So let's see the attacker has got this perfect attacker has got to know that someone interacted with
82

83
00:05:48,250 --> 00:05:53,590
this IP with this port number and that end point that is Cookie equals to.
83

84
00:05:53,950 --> 00:05:57,890
As you can see my interaction happened perfect.
84

85
00:05:58,270 --> 00:06:05,050
So this means our server is working perfectly fine so let's take this let's copy this.
85

86
00:06:05,050 --> 00:06:08,440
Let's go over here and let's hit it and hit go.
86

87
00:06:08,440 --> 00:06:15,730
So now this vulnerable application will send the cookie to the attacker server.
87

88
00:06:16,690 --> 00:06:19,510
Let's go and check to attacker server.
88

89
00:06:19,510 --> 00:06:20,440
Have we got something.
89

90
00:06:20,530 --> 00:06:21,580
Perfect.
90

91
00:06:21,580 --> 00:06:29,230
We have got a request which means someone has interacted with us and tried to send us the cookie.
91

92
00:06:29,380 --> 00:06:36,150
but as you know guys I told a prerequisite the user must be logged in into the application.
92

93
00:06:36,310 --> 00:06:38,830
So right now the user is not logged in.
93

94
00:06:38,830 --> 00:06:41,580
That's why we are getting a blank cookie.
94

95
00:06:41,620 --> 00:06:42,530
Perfect.
95

96
00:06:42,580 --> 00:06:47,960
So now user needs to log in into the application to get a valid cookie as you can see a blank cookie
96

97
00:06:47,960 --> 00:06:49,850
over here.
97

98
00:06:50,050 --> 00:06:53,710
Let's go in my profile section and let's try to log in with my credentials.
98

99
00:06:53,710 --> 00:06:56,490
That is test and test.
99

100
00:06:56,560 --> 00:07:01,270
Let's hit on log in after log in as you can see I have logged in into the application.
100

101
00:07:01,270 --> 00:07:11,620
Let me try to give this payload in all the fields over here and let me just hit on update so I know
101

102
00:07:12,310 --> 00:07:15,960
that after hitting update what is going to happen.
102

103
00:07:16,000 --> 00:07:23,580
I am going to get some interaction on to the attacker server the python server that we have started.
103

104
00:07:23,770 --> 00:07:25,900
And what will be that interaction.
104

105
00:07:25,900 --> 00:07:33,200
The cookie value through which we are going to do a successful XSS cookie stealer exploitation.
105

106
00:07:33,580 --> 00:07:36,570
So have hit the update button.
106

107
00:07:36,570 --> 00:07:40,410
Let us go to a terminal and let's see if we have got the cookie.
107

108
00:07:40,450 --> 00:07:41,200
Perfect.
108

109
00:07:42,370 --> 00:07:45,110
Our payload has successfully executed.
109

110
00:07:45,130 --> 00:07:50,580
That was document dot location dot href the attacker server.
110

111
00:07:50,620 --> 00:07:56,950
The end point that is Cookie and the document dot cookie payload which gave the cookie that was test
111

112
00:07:57,070 --> 00:07:58,720
and test perfect.
112

113
00:07:58,720 --> 00:08:07,680
We got the cookie over here as you can see now we will verify if this is the right cookie or not.
113

114
00:08:07,910 --> 00:08:13,310
Are we able to use this cookie to do an account takeover cookie stealing.
114

115
00:08:13,660 --> 00:08:16,480
So let me just log out of this application right now.
115

116
00:08:16,930 --> 00:08:21,130
So the user has logged out and we have got the cookie for the user.
116

117
00:08:21,130 --> 00:08:28,120
Let me just go to your profile section and I m going to use a cookie manager you can install this cookie
117

118
00:08:28,120 --> 00:08:28,790
manager.
118

119
00:08:28,960 --> 00:08:33,190
It is free for Chrome as well as Firefox.
119

120
00:08:33,190 --> 00:08:43,440
This extension is free of cost after clicking on this extension just paste the name of the key.
120

121
00:08:43,780 --> 00:08:49,250
So the cookie name is log in and the value is test percent 2 F test.
121

122
00:08:49,420 --> 00:08:54,290
And I'm going to save this cookie and again click in order and again click on save.
122

123
00:08:54,310 --> 00:08:56,890
So perfect the cookie has been saved.
123

124
00:08:56,890 --> 00:09:01,990
Let's see if this cookie value was correct.
124

125
00:09:01,990 --> 00:09:06,760
And it allows the attacker to take over the victim's account.
125

126
00:09:06,760 --> 00:09:09,360
So we have saved the cookie successfully.
126

127
00:09:09,550 --> 00:09:12,460
And let's try to just reload the application.
127

128
00:09:12,460 --> 00:09:18,850
So after reloading the application if we get logged in into the account then we have successfully then
128

129
00:09:18,850 --> 00:09:23,110
that XSS exploitation using cookie stealing.
129

130
00:09:23,470 --> 00:09:34,470
So let me just try to reload and perfect as you can see the user account has been here.
130

131
00:09:34,600 --> 00:09:36,700
The attacker has logged in into the user's account.
131

132
00:09:36,700 --> 00:09:42,720
Let me just go to home and let me just again go to my profile section to show you guys.
132

133
00:09:43,450 --> 00:09:52,210
And yes the attacker has successfully logged in into the victim's account by stealing the cookie.
133

134
00:09:52,300 --> 00:09:53,180
Perfect.
134

135
00:09:53,200 --> 00:10:01,350
So this was a demonstration of cookie stealing into a lab basically into your own same network.
135

136
00:10:01,630 --> 00:10:07,750
And the next video we're going to see how we can do cookie stealing onto a wide area network or onto
136

137
00:10:07,750 --> 00:10:09,940
a public network.
137

138
00:10:09,970 --> 00:10:11,290
I hope you guys understood.
138

139
00:10:11,290 --> 00:10:11,820
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,710 --> 00:00:03,370
Hello everyone.
1

2
00:00:03,420 --> 00:00:09,710
So this is the video of XSS exploitation of cookie stealing.
2

3
00:00:09,750 --> 00:00:17,040
So in this video I'm going to show you how I came across a very interesting scenario while doing the
3

4
00:00:17,140 --> 00:00:19,560
XSS cookie stealing.
4

5
00:00:19,710 --> 00:00:22,780
So let's just see.
5

6
00:00:23,010 --> 00:00:26,510
So this is a Web site book my phone dot in.
6

7
00:00:26,580 --> 00:00:28,170
OK.
7

8
00:00:28,170 --> 00:00:34,400
Remember guys this is Cookie stealing on a live Web site that is on the wan network that is public network.
8

9
00:00:34,410 --> 00:00:34,820
OK.
9

10
00:00:34,970 --> 00:00:41,340
So in the previous video we did cookie stealing on a local network by making an Python server in this
10

11
00:00:41,340 --> 00:00:41,920
video.
11

12
00:00:41,940 --> 00:00:45,340
We are going to make a server through Burpe suite.
12

13
00:00:45,360 --> 00:00:46,650
That is Burpe collaborator.
13

14
00:00:47,190 --> 00:00:50,770
So let's see this how can we do this on to public Websites.
14

15
00:00:50,800 --> 00:00:52,800
Whenever you are doing your bug hunting
15

16
00:01:02,440 --> 00:01:09,070
so firstly I'm logged in into the application as you can see that is the prerequisite.
16

17
00:01:09,850 --> 00:01:14,810
I'm just going to type hacktify and search to show you the reflection.
17

18
00:01:14,890 --> 00:01:15,180
Yes.
18

19
00:01:15,190 --> 00:01:23,800
As you can see the reflection is over here and now I'm going to give the payload that is script alert
19

20
00:01:27,310 --> 00:01:28,140
as you can see.
20

21
00:01:28,210 --> 00:01:30,020
This is vulnerable.
21

22
00:01:30,880 --> 00:01:38,650
Now what I'm going to do is I'm going to fire this payload as you can see.
22

23
00:01:39,610 --> 00:01:44,360
Image source equals to X on erroe equals to this dot source.
23

24
00:01:44,710 --> 00:01:48,500
And you have to give server name here.
24

25
00:01:48,520 --> 00:01:55,240
So in this case I'm going to give the server name that is this server name which is basically some
25

26
00:01:55,240 --> 00:01:59,630
strings long strings dot burpecollaborator dot net.
26

27
00:01:59,770 --> 00:02:07,150
What is this and how I have got this , I have got this through the burpe so I'm just going to show how
27

28
00:02:07,150 --> 00:02:08,170
I got this.
28

29
00:02:08,200 --> 00:02:13,120
You have to put the name of this collaborator over here then question mark.
29

30
00:02:13,120 --> 00:02:14,510
Any parameter you want.
30

31
00:02:14,530 --> 00:02:21,210
I'm taking a parameter C for cookies where I'm going to get the cookie value document dot cookies
31

32
00:02:21,220 --> 00:02:22,300
value.
32

33
00:02:22,300 --> 00:02:22,970
Perfect.
33

34
00:02:24,370 --> 00:02:26,200
So how to make a collaborator.
34

35
00:02:26,200 --> 00:02:34,330
You just have to go to Burpe and click on Burpe collaborater client after clicking on this copy to clipboard
35

36
00:02:34,990 --> 00:02:37,000
as soon as you copy on clipboard.
36

37
00:02:37,210 --> 00:02:43,210
The book collaborators server's address will be copied and Poll collaborator interaction.
37

38
00:02:43,210 --> 00:02:50,860
You have to give Poll every one second which means every one second it is going to refresh and check
38

39
00:02:50,980 --> 00:02:54,040
if there is any request coming onto our listener.
39

40
00:02:54,790 --> 00:03:00,460
So basically we saw a local listener using Python and this is a public listener perfect
40

41
00:03:03,260 --> 00:03:07,550
so I will just go back and
41

42
00:03:12,620 --> 00:03:18,570
here and I will paste the collaborater server which we copied perfect.
42

43
00:03:19,190 --> 00:03:22,610
And I'm going to type here http colon slash slash.
43

44
00:03:23,200 --> 00:03:24,520
OK.
44

45
00:03:24,980 --> 00:03:26,810
So I'm going to take this payload.
45

46
00:03:26,810 --> 00:03:33,350
I'm going to go here and enter it and hit search after hiting search.
46

47
00:03:33,420 --> 00:03:41,030
Let's go and check onto our listener that we have got any hit rate or not.
47

48
00:03:41,030 --> 00:03:42,980
Have we got any cookie.
48

49
00:03:43,040 --> 00:03:43,700
Let's wait.
49

50
00:03:43,730 --> 00:03:45,370
Let's click on Poll now.
50

51
00:03:45,660 --> 00:03:46,250
perect.
51

52
00:03:46,280 --> 00:03:49,650
We have got the cookies as you can see.
52

53
00:03:49,830 --> 00:03:51,010
So let me just click on it.
53

54
00:03:51,040 --> 00:03:52,690
http and DNS.
54

55
00:03:52,700 --> 00:03:55,340
We have got two types of hit.
55

56
00:03:55,370 --> 00:04:00,100
first is DNS, DNS is not important for us.
56

57
00:04:00,170 --> 00:04:03,310
http is important as you can see in http.
57

58
00:04:03,330 --> 00:04:08,230
I'm able to get the cookie in the C parameter, C equals to the.
58

59
00:04:08,240 --> 00:04:10,210
This is the long cookie name.
59

60
00:04:10,250 --> 00:04:10,860
Perfect.
60

61
00:04:10,870 --> 00:04:11,720
i have got the cookie
61

62
00:04:15,920 --> 00:04:24,300
if I see the DNS one, the DNS one only says that I have got a hit from the IP address which is this.
62

63
00:04:24,380 --> 00:04:31,810
This is basically the IP address of book my phone and I have got a request from them onto my server.
63

64
00:04:31,910 --> 00:04:33,020
That is my listener.
64

65
00:04:33,050 --> 00:04:34,820
Perfect.
65

66
00:04:34,820 --> 00:04:40,680
So for doing cookie stealing http hit or HTTP interaction is important.
66

67
00:04:40,700 --> 00:04:43,520
And I have got a http interaction with the cookie.
67

68
00:04:43,520 --> 00:04:45,950
So I have successfully done the cookie stealing
68

69
00:04:50,440 --> 00:04:53,260
now I'm going to log out the application
69

70
00:04:56,980 --> 00:04:59,530
as soon as a log out of the application.
70

71
00:04:59,530 --> 00:05:05,350
Now I am trying to use those cookies and I will try to log in into this account.
71

72
00:05:05,350 --> 00:05:09,270
Okay so here and I'm giving the wrong credentials and I'm trying to log in.
72

73
00:05:09,430 --> 00:05:18,130
Basically a bunch of wrong strings and I will try to log in ,as you can see this is a wrong email address
73

74
00:05:18,160 --> 00:05:19,960
as well as wrong password.
74

75
00:05:19,960 --> 00:05:20,410
And.
75

76
00:05:20,470 --> 00:05:29,080
This time I'm going to use these cookies now while doing this practical case I noticed a very strange
76

77
00:05:29,080 --> 00:05:30,250
thing.
77

78
00:05:30,430 --> 00:05:39,970
The application invalidated all the cookies once the user has logged out but the server the application
78

79
00:05:39,970 --> 00:05:42,690
gave these cookies to someone else.
79

80
00:05:42,760 --> 00:05:50,020
So one strange behavior that I observed and this practically was these cookies were assigned to someone
80

81
00:05:50,110 --> 00:05:50,960
else.
81

82
00:05:51,190 --> 00:05:57,670
And when I'm going to use this cookies to log in I will be logged into someone else's account.
82

83
00:05:57,670 --> 00:05:58,450
So let's see this
83

84
00:06:10,500 --> 00:06:17,220
So I am going to copy and replace the cookies over here with the wrong credentials.
84

85
00:06:17,220 --> 00:06:20,760
And I'm going to do do intercept response because I want to see the response
85

86
00:06:24,270 --> 00:06:24,670
OK.
86

87
00:06:24,690 --> 00:06:27,930
The response is the result falls invalid combination.
87

88
00:06:27,930 --> 00:06:34,180
I know this is wrong and they have assigned a php session ID .
88

89
00:06:34,300 --> 00:06:42,050
Okay fine I will just replace that with the cookie that I've got and try to see what happens.
89

90
00:06:42,060 --> 00:06:42,470
Fine.
90

91
00:06:42,480 --> 00:06:43,740
I'm not logged in.
91

92
00:06:43,740 --> 00:06:45,320
Let me try once more.
92

93
00:06:45,810 --> 00:06:56,110
Let me try to reload the application go in burpe replace this cookie by the cookie that I have got and
93

94
00:06:56,140 --> 00:07:00,940
let me just put it here and remove the space.
94

95
00:07:00,940 --> 00:07:06,910
forward This again forward this forward this forward this forward forward forward forward.
95

96
00:07:06,910 --> 00:07:12,380
This also forward all the request which are not important for me.
96

97
00:07:12,490 --> 00:07:16,380
Go back to the browser see at the application.
97

98
00:07:16,430 --> 00:07:17,690
OK.
98

99
00:07:17,980 --> 00:07:24,070
So here I noticed I was not able to log in and I'm going to do a third attempt again.
99

100
00:07:24,160 --> 00:07:32,290
So here in I will again reload this application and you can see this time the End Point is Cart.
100

101
00:07:33,200 --> 00:07:33,680
Okay.
101

102
00:07:33,790 --> 00:07:35,800
As you can see the end point is cart.
102

103
00:07:35,850 --> 00:07:37,040
Fine.
103

104
00:07:37,090 --> 00:07:45,040
So this time nine point that I've got in Burpe suite is also cart, I am going to replace these cookies I replaced
104

105
00:07:45,190 --> 00:07:45,780
the cookies.
105

106
00:07:45,790 --> 00:07:54,250
I'll forward this I'll do intercept off and application is assigned a session ID and I will do off and
106

107
00:07:54,250 --> 00:07:55,940
you can notice here.
107

108
00:07:56,440 --> 00:08:02,600
Perfect as you can see guys I have logged in into someone else's cart.
108

109
00:08:03,310 --> 00:08:07,590
And this is someone's niyish named user.
109

110
00:08:07,660 --> 00:08:08,860
This is the mobile number.
110

111
00:08:08,860 --> 00:08:10,200
This is the e-mail 
111

112
00:08:10,210 --> 00:08:17,660
This is the address from Lucknow and a phone someone has added which is speria note 9.
112

113
00:08:17,970 --> 00:08:18,600
Worth rupees.
113

114
00:08:18,610 --> 00:08:19,460
This much.
114

115
00:08:20,290 --> 00:08:27,400
So yes we were able to do a successful exploitation of cookie stealing through which we were able to
115

116
00:08:27,490 --> 00:08:30,310
access someone else's cart.
116

117
00:08:30,370 --> 00:08:32,080
So I hope you guys understand this.
117

118
00:08:32,080 --> 00:08:32,520
video.
118

119
00:08:33,520 --> 00:08:34,500
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,160 --> 00:00:03,480
Hello everyone.
1

2
00:00:03,480 --> 00:00:10,230
So in this video of XSS exploitation through file upload we're going to see one more way through
2

3
00:00:10,230 --> 00:00:13,170
which we can do XSS through file upload.
3

4
00:00:14,880 --> 00:00:23,040
So what basically I'm going to do is I'm going to upload a file onto this application wherein the application
4

5
00:00:23,130 --> 00:00:25,370
allows File Uploading functionality.
5

6
00:00:26,310 --> 00:00:31,970
So what I'm going to do is I'm going to upload a file which I just made.
6

7
00:00:32,100 --> 00:00:33,630
So the filing is
7

8
00:00:38,500 --> 00:00:41,280
I think I made the file with coolsvg.
8

9
00:00:41,780 --> 00:00:43,000
So let me just try to search it.
9

10
00:00:43,030 --> 00:00:44,420
Yes it is over here.
10

11
00:00:44,770 --> 00:00:54,250
So basically I'm going to upload an svg vector files and I'll just intercept this request to show
11

12
00:00:54,250 --> 00:01:00,560
you guys how the file is getting uploaded and I will just click on dump after clicking over there.
12

13
00:01:00,580 --> 00:01:01,940
I'll go here.
13

14
00:01:02,260 --> 00:01:08,410
Now if you look closely the file name is coolsvg.svg
14

15
00:01:08,440 --> 00:01:11,230
Basically this is a svg file vectors.
15

16
00:01:11,470 --> 00:01:21,340
And if you look here then the payload that I've written is basically this the svg boilerplate format.
16

17
00:01:21,340 --> 00:01:25,960
And basically after that onload alert document dot domain.
17

18
00:01:26,500 --> 00:01:33,340
So I have written something and then I have written onload if this gets loaded properly alert the
18

19
00:01:33,340 --> 00:01:38,220
document a domain document dot domain means the domain name.
19

20
00:01:38,230 --> 00:01:42,760
So in this case the domain name is srsecure.xyz.
20

21
00:01:42,760 --> 00:01:52,630
So fine we're going to upload this file with the payload inside it let me just do intercept response
21

22
00:01:52,630 --> 00:01:56,350
to this request because I want to see the response also.
22

23
00:01:56,350 --> 00:02:04,680
I'll just forward this and do an intercept off and it's getting uploaded.
23

24
00:02:04,900 --> 00:02:11,610
This is the payload that we entered as we already saw on load alert document dot domain.
24

25
00:02:11,620 --> 00:02:12,460
It is getting uploaded.
25

26
00:02:12,460 --> 00:02:13,660
Let me go in Burpe inject.
26

27
00:02:13,690 --> 00:02:14,650
Yep it was on.
27

28
00:02:14,680 --> 00:02:20,500
Let me just turn it off and you can see the file coolsvg.svg job done is uploaded.
28

29
00:02:21,190 --> 00:02:22,280
Perfect.
29

30
00:02:22,360 --> 00:02:27,460
So let's try to see if we can get a XSS through this file or not.
30

31
00:02:27,700 --> 00:02:32,380
Let me just quickly navigate to the uploads folder after navigating.
31

32
00:02:32,380 --> 00:02:39,160
Let me just give the file name that we just uploaded that is coolsvg.svg and the wait
32

33
00:02:39,160 --> 00:02:46,260
for the application and perfect as it can see our XSS has been successfully executed.
33

34
00:02:46,690 --> 00:02:53,970
And here you can see srsecure. xyz which is basically because of document dot domain payload
34

35
00:02:54,390 --> 00:02:56,920
here in we are able to see the name of the domain.
35

36
00:02:58,180 --> 00:03:04,130
So I hope you guys understood the exploitation of XSS using file upload.
36

37
00:03:04,210 --> 00:03:04,660
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,110 --> 00:00:02,780
Hello everyone.
1

2
00:00:02,780 --> 00:00:11,790
So in this video we are going to see how we can do XSS using file upload with changing the metadata
2

3
00:00:11,910 --> 00:00:13,770
of any file.
3

4
00:00:13,860 --> 00:00:21,840
So in the first two videos we saw that how we uploaded a html file and a payload inside it achieved
4

5
00:00:21,900 --> 00:00:27,040
us in getting it successful  XSS, in the second video.
5

6
00:00:27,090 --> 00:00:36,720
We saw how we compromised and misused and SVG vectors and we ended up getting an XSS ,in this third
6

7
00:00:36,720 --> 00:00:37,640
video.
7

8
00:00:37,640 --> 00:00:44,910
We are going to see how we can abuse a file upload functionality and get a XSS by changing the
8

9
00:00:45,000 --> 00:00:48,490
exif data or the metadata of any file.
9

10
00:00:49,050 --> 00:00:51,610
So let's see this how to do this.
10

11
00:00:51,630 --> 00:00:57,780
So for this I'll just head under the Google because we want to file in which we are going to make some
11

12
00:00:57,780 --> 00:00:58,380
changes.
12

13
00:00:58,770 --> 00:01:06,330
So I will just type EXIF samples github and you will be able to see the first link is a github link
13

14
00:01:06,870 --> 00:01:09,700
wherein I am able to get some images.
14

15
00:01:09,720 --> 00:01:10,730
OK.
15

16
00:01:11,040 --> 00:01:17,940
So I'll just click on jpg and I will click on the first image let's say that is canon 40D dot
16

17
00:01:17,940 --> 00:01:18,630
jpg.
17

18
00:01:18,690 --> 00:01:20,130
It is an image.
18

19
00:01:20,130 --> 00:01:22,270
So I have downloaded this image.
19

20
00:01:22,290 --> 00:01:28,360
I'll open this as you can see this is the image that I have downloaded.
20

21
00:01:28,960 --> 00:01:33,660
I'm opening up a terminal over here after opening a terminal.
21

22
00:01:33,690 --> 00:01:40,760
I'm just going to type exif tool just to verify that I have exif tool installed into my which virtual machine.
22

23
00:01:40,770 --> 00:01:49,020
So basically this is a padded Linux OS which is our debian based Linux penetration testing os.
23

24
00:01:49,110 --> 00:01:53,390
You can also run this on kali linux.
24

25
00:01:53,390 --> 00:01:56,760
exif Tool is  pre installed in both the operating system.
25

26
00:01:56,760 --> 00:02:03,330
If you do not have exit tool or you are running onto another operating system like Ubuntu or RedHat
26

27
00:02:03,690 --> 00:02:08,280
you can install exif tool by typing apt hyphen get install EXIF tool.
27

28
00:02:09,090 --> 00:02:14,400
I'm just making sure I have tools that I have this tool installed so I'm going to type enter and you
28

29
00:02:14,400 --> 00:02:22,660
can see I have this tool installed already into my machine so I'm going to give EXIF tool and the
29

30
00:02:22,730 --> 00:02:25,920
filing that I have downloaded and I will hit enter.
30

31
00:02:27,960 --> 00:02:28,620
Perfect.
31

32
00:02:28,620 --> 00:02:34,620
So as you can see this is the metadata of the image which contains a lot of values different different
32

33
00:02:34,620 --> 00:02:36,580
types of values.
33

34
00:02:36,690 --> 00:02:37,350
Perfect.
34

35
00:02:37,560 --> 00:02:39,810
So I'm able to see everything.
35

36
00:02:39,870 --> 00:02:50,160
Now what I'm going to do something interesting is I am going to add a new attribute basically or add
36

37
00:02:50,520 --> 00:02:53,530
a new metadata into this specific file.
37

38
00:02:54,270 --> 00:02:57,150
So for that I'm going to type a command.
38

39
00:02:58,440 --> 00:03:08,990
So for that what I'm going to do is I'm going to type EXIF tool space hyphen artist or basically I'm
39

40
00:03:08,990 --> 00:03:16,080
willing to add a new metadata that is or a new attribute that is artist and I'm going to type
40

41
00:03:20,430 --> 00:03:24,970
equals to.
41

42
00:03:25,120 --> 00:03:30,670
So what should be the value for artist value should be an XSS payload.
42

43
00:03:30,790 --> 00:03:36,100
So I have given here image source equal to X on error equals to alert
43

44
00:03:38,980 --> 00:03:41,730
document dot domain.
44

45
00:03:41,770 --> 00:03:43,160
Perfect.
45

46
00:03:43,180 --> 00:03:49,780
Now remember guys you have to give whatever value you want in to the single quotes.
46

47
00:03:49,810 --> 00:03:51,530
So this is the starting single quote.
47

48
00:03:51,910 --> 00:03:57,080
This is this is the ending single quote and in between here is my payload.
48

49
00:03:57,320 --> 00:03:57,880
OK.
49

50
00:03:57,940 --> 00:03:59,650
And then the final name.
50

51
00:03:59,920 --> 00:04:03,010
So the file name is this and I will just press enter
51

52
00:04:07,330 --> 00:04:08,710
after hitting enter.
52

53
00:04:08,740 --> 00:04:11,880
You can see a new file has been created.
53

54
00:04:11,980 --> 00:04:19,180
And this is the original file and this is the new file modified file with this XSS payload.
54

55
00:04:19,520 --> 00:04:24,340
So let's verify if okay.
55

56
00:04:24,400 --> 00:04:29,410
So I'm making again a new file and I am putting this payload into this origional file.
56

57
00:04:29,440 --> 00:04:30,270
Perfect.
57

58
00:04:31,150 --> 00:04:32,990
So one image files is updated.
58

59
00:04:33,310 --> 00:04:34,690
Okay.
59

60
00:04:34,900 --> 00:04:37,270
So now let's verify this.
60

61
00:04:37,540 --> 00:04:39,640
So what I'm going to do now is
61

62
00:04:43,540 --> 00:04:52,920
I'm willing to type EXIF tool the file name and let's verify that we have got our payload stored in
62

63
00:04:52,920 --> 00:04:54,030
here or not.
63

64
00:04:54,750 --> 00:05:03,030
And you can see over here there is a new attribute or metadata which has been added and which is artist
64

65
00:05:03,320 --> 00:05:09,880
which was not before but we have added it and the value we have given is a payload over here.
65

66
00:05:09,870 --> 00:05:16,330
Perfect.
66

67
00:05:16,700 --> 00:05:22,790
So this is how we have created and file which contains a payload into it.
67

68
00:05:22,790 --> 00:05:32,250
Metadata and if any web server which parses a file metadata will be vulnerable to this type of XSS
68

69
00:05:32,280 --> 00:05:33,240
attack.
69

70
00:05:33,740 --> 00:05:39,890
So for testing you just need to upload this file and if you get XSS then you have successfully done
70

71
00:05:39,980 --> 00:05:43,680
exploitation using exif metadata of a file.
71

72
00:05:44,570 --> 00:05:47,190
Let me just upload it here and try to test this.
72

73
00:05:47,320 --> 00:05:52,010
And let me try to hit dump and you can see the file is uploaded
73

74
00:05:55,990 --> 00:06:03,690
that we're going uploads and tried to put the file name and just check.
74

75
00:06:03,690 --> 00:06:05,160
I mean getting XSS
75

76
00:06:07,540 --> 00:06:09,530
and not in this case.
76

77
00:06:09,540 --> 00:06:15,730
No because this server is not parsing the metadata of that file which contains a payload.
77

78
00:06:16,270 --> 00:06:24,460
Okay fine I hope you guys understood how we can achieve XSS through file upload using EXIF metadata
78

79
00:06:24,460 --> 00:06:25,650
modification.
79

80
00:06:25,870 --> 00:06:31,150
This can be useful in live hunting on many web applications.
80

81
00:06:31,150 --> 00:06:31,620
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,810 --> 00:00:02,560
Hello everyone.
1

2
00:00:03,010 --> 00:00:08,980
So in this video of XSS exploitation we are going to see how we can do XSS exploitation using
2

3
00:00:08,980 --> 00:00:10,510
file uploads.
3

4
00:00:10,750 --> 00:00:17,270
So we are going to upload a file and abuse the file upload functionality to achieve XSS.
4

5
00:00:17,290 --> 00:00:21,960
We will also find an injection point using Burpe suite spider feature or manually.
5

6
00:00:22,900 --> 00:00:26,410
Then we are going to inject the XSS payload into the upload feature.
6

7
00:00:27,280 --> 00:00:35,200
So basically we can also achieve XSS by any upload functionality into any application that you
7

8
00:00:35,200 --> 00:00:36,380
see.
8

9
00:00:36,550 --> 00:00:41,920
We generally see these types of functionalities are into added profile or whenever you tried to make
9

10
00:00:41,920 --> 00:00:43,290
an account.
10

11
00:00:43,360 --> 00:00:47,200
So let's see this how can you do a successful exploitation on that
11

12
00:00:50,320 --> 00:00:51,310
link to make a file.
12

13
00:00:52,270 --> 00:01:01,290
And in that file I'm just going to give a simple basic XSS payload that is script alert one script tag
13

14
00:01:01,360 --> 00:01:02,770
close.
14

15
00:01:02,830 --> 00:01:05,770
So this is what is going to be inside that file.
15

16
00:01:07,030 --> 00:01:16,860
Let me just save this file as a name that is let's say I give upload me plz dot html.
16

17
00:01:16,870 --> 00:01:22,480
So I'm going to save this file as uploadmeplz dot html and the content inside that file
17

18
00:01:22,540 --> 00:01:25,420
is XSS payload.
18

19
00:01:25,540 --> 00:01:32,650
Now I'll go to this website where there is upload form and I'm going to upload the file that I just
19

20
00:01:32,650 --> 00:01:36,190
made and the final is upload me please.
20

21
00:01:38,870 --> 00:01:46,040
Under this website before uploading what I like to do is I'm willing to capture this request in to Burpe
21

22
00:01:46,040 --> 00:01:55,670
suite and I will click on dump which is basically upload after pressing the dump button as you can see
22

23
00:01:55,700 --> 00:01:57,910
I have captured the request.
23

24
00:01:58,010 --> 00:01:58,680
The file name.
24

25
00:01:58,700 --> 00:02:05,660
As you can see over here is upload me please dot html and the content basically whatever the
25

26
00:02:05,660 --> 00:02:08,690
data is inside that file is reflected over here.
26

27
00:02:08,870 --> 00:02:14,090
So I will just press forward and also send this to repeater.
27

28
00:02:14,090 --> 00:02:20,570
So in case I want to use this request again and also I will do  intercept response to this request
28

29
00:02:21,020 --> 00:02:25,120
because I want to see what is the response the application shows me.
29

30
00:02:25,140 --> 00:02:28,570
when I tried to upload this file.
30

31
00:02:29,450 --> 00:02:37,130
I will just hit forward and wait for the application to upload this file let me do intercept off.
31

32
00:02:37,130 --> 00:02:38,140
Perfect.
32

33
00:02:38,150 --> 00:02:43,410
So as you can see the file upload me please dot html job done.
33

34
00:02:43,580 --> 00:02:46,580
Which means the file has been uploaded successfully.
34

35
00:02:48,410 --> 00:02:50,960
I'll just copy this name because I want to see this file.
35

36
00:02:53,240 --> 00:02:59,510
I will just try to paste the file over here into the upload directory because this any file that
36

37
00:02:59,570 --> 00:03:01,910
gets uploaded goes into the upload directory
37

38
00:03:05,310 --> 00:03:07,400
when I will try to locate this file.
38

39
00:03:07,440 --> 00:03:12,320
This file will show a successful XSS.
39

40
00:03:12,720 --> 00:03:17,910
This is how we can achieve XSS through file uploading feature.
40

41
00:03:17,910 --> 00:03:19,000
I hope you guys understood.
41

42
00:03:19,290 --> 00:03:20,370
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,780 --> 00:00:02,130
Hello everyone.
1

2
00:00:02,130 --> 00:00:10,030
So in this video we are going to see how to fix XSS or what are the mitigations to XSS.
2

3
00:00:10,080 --> 00:00:16,390
First point input sanitization input Sanitization is very very important.
3

4
00:00:16,470 --> 00:00:25,140
The interpreter should know that whatever data is coming inside any untrusted data should not be passed
4

5
00:00:25,320 --> 00:00:26,780
as it is.
5

6
00:00:26,910 --> 00:00:36,730
It should not be directly interpreting, second escaping encoding of all the input that a user ends with.
6

7
00:00:36,750 --> 00:00:44,220
So basically anything that has been given by a user should be escaped proper encoding should be done
7

8
00:00:44,640 --> 00:00:49,930
for instance html encoding should be possible.
8

9
00:00:50,070 --> 00:00:57,480
Strong input validation for limited input with sanitization which means limited input should be there
9

10
00:00:57,990 --> 00:01:07,760
for specific fields only wherein it will stop the chances of XSS a strong WAF.
10

11
00:01:07,800 --> 00:01:17,430
Of course Richard automatically detect and block XSS types of attacks, filter input on arrival as
11

12
00:01:17,430 --> 00:01:23,240
we already discussed it is input sanitization encoded on output.
12

13
00:01:23,250 --> 00:01:30,570
This is also basically html encoding which we discussed already use appropriate response headers.
13

14
00:01:30,570 --> 00:01:39,030
So in this application to prevent XSS can use Content Type Headers or ex content type option headers
14

15
00:01:39,180 --> 00:01:47,290
basically in the responses to prevent the browsers to interpret the response in the way attacker wants.
15

16
00:01:47,310 --> 00:01:55,440
And the last of this is the CSP policy which is the content security policy which can prevent the severity
16

17
00:01:55,440 --> 00:02:05,480
of XSS if it occurs so CSP will block if any website wants to send any cookie to any other website.
17

18
00:02:05,580 --> 00:02:14,010
So these other mitigations of XSS which can be placed into any web application which can fix these
18

19
00:02:14,010 --> 00:02:15,630
types of issues.
19

20
00:02:15,660 --> 00:02:16,780
I hope you guys understood.
20

21
00:02:17,160 --> 00:02:17,700
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,050 --> 00:00:02,570
Hello everyone.
1

2
00:00:02,580 --> 00:00:09,590
So in this video I'm going to share with you guys a bonus lecture in which you will see XSS.
2

3
00:00:09,600 --> 00:00:10,660
Bonus tricks.
3

4
00:00:11,700 --> 00:00:16,500
I'm going to show you some of the dirty tricks to find XSS everywhere.
4

5
00:00:17,540 --> 00:00:20,400
So let's see how can we do this.
5

6
00:00:22,620 --> 00:00:26,160
So for this I'm going to go on to
6

7
00:00:29,290 --> 00:00:34,290
this github repository named param spider
7

8
00:00:34,450 --> 00:00:42,810
So this is a tool which is made by an author which finds the parameters from the dark corners of the
8

9
00:00:42,940 --> 00:00:44,080
archives.
9

10
00:00:44,080 --> 00:00:53,050
So basically this tool crawls the way back machine and takes all the parameters and put them into a
10

11
00:00:53,050 --> 00:00:54,300
list.
11

12
00:00:54,490 --> 00:00:56,100
So we are going to download this tool.
12

13
00:00:56,110 --> 00:00:59,190
It's simple just you can get clone from here.
13

14
00:00:59,230 --> 00:01:00,600
You can just click on clone.
14

15
00:01:01,900 --> 00:01:13,150
And after that you can just go into a terminal and  just type git clone and the name just paste the link
15

16
00:01:13,300 --> 00:01:17,050
and you can see cloning and it will successfully clone it.
16

17
00:01:17,260 --> 00:01:20,890
After that you just need to go inside the tool for going.
17

18
00:01:20,890 --> 00:01:28,690
You have to type C.D. param spider after going inside do a ls to list whatever is inside.
18

19
00:01:28,720 --> 00:01:33,970
After that you can see there is a requirement dot txt  you have to install requirements dot txt
19

20
00:01:34,210 --> 00:01:41,890
using pip install hyphen R to read the file which is a requirement dot txt and hit enter.
20

21
00:01:41,890 --> 00:01:44,900
It will take some time to install into your computer systems.
21

22
00:01:44,920 --> 00:01:49,300
I've already installed all the requirements though it is saying that everything is install.
22

23
00:01:49,420 --> 00:01:53,300
Let me just clear the screen for you again do ls.
23

24
00:01:53,320 --> 00:02:02,650
And you can see I'm going to run param spider dot py so I'm going to run this tool on a subdomain of Google
24

25
00:02:03,430 --> 00:02:03,970
for that.
25

26
00:02:04,000 --> 00:02:10,180
I'm just going to type Python3 paramspider.py --domain.
26

27
00:02:10,330 --> 00:02:19,150
tez dot google dot com --exclude this extensions which are  php,jpg,svg  and make the level high as
27

28
00:02:19,150 --> 00:02:31,180
per the description onto the website which is made for this tool exclude excludes the extinctions level
28

29
00:02:31,180 --> 00:02:33,680
high gives nested parameters.
29

30
00:02:33,700 --> 00:02:41,440
So basically two parameters if there are into the way back archive machine let's go back to the tool
30

31
00:02:42,430 --> 00:02:49,620
and now I'm going to hit enter as you can see the tool has started and the tool has found total unique
31

32
00:02:49,690 --> 00:02:50,770
URL's.
32

33
00:02:50,980 --> 00:02:52,280
That is total eight.
33

34
00:02:52,360 --> 00:02:56,360
And it has saved the output into a folder output.
34

35
00:02:56,410 --> 00:02:59,350
And the file name tez.google.com.txt.
35

36
00:02:59,860 --> 00:03:07,120
OK so as you can see there are total eight number of URL's if you look closely onto this.
36

37
00:03:07,120 --> 00:03:07,600
URL.
37

38
00:03:07,690 --> 00:03:15,010
Which is https tez dot Google dot com slash referrals slash question Mark referrer underscore
38

39
00:03:15,040 --> 00:03:17,110
Id equals to fuzz.
39

40
00:03:17,200 --> 00:03:23,180
So basically the parameter here is the referrer Id and the value is fuzz.
40

41
00:03:23,290 --> 00:03:32,170
Let's go back to our browser and let me show you a report which was recently found out in March 27 2020
41

42
00:03:32,890 --> 00:03:39,010
which was an XSS on Google which was paid around 3000 dollars of bounty.
42

43
00:03:39,040 --> 00:03:45,160
So as you can see the researcher just did subdomain enumeration and he was able to find out a subdomain
43

44
00:03:45,190 --> 00:03:46,810
that is tez dot Google dot com.
44

45
00:03:48,100 --> 00:03:48,660
OK.
45

46
00:03:48,910 --> 00:03:57,280
So after that he tried for some Google Docs and he was able to identify a subdomain with URL that
46

47
00:03:57,280 --> 00:04:06,640
is tez dot Google dot com slash referrer underscore id equals to as you can see here this researcher
47

48
00:04:06,820 --> 00:04:09,670
use Google Docs operators to find this.
48

49
00:04:09,670 --> 00:04:17,320
We used wayback time machine which is a crawler which must have called this Web site earlier after
49

50
00:04:17,320 --> 00:04:21,290
going onto this Web site as you can see it.
50

51
00:04:21,370 --> 00:04:22,410
What he did.
51

52
00:04:22,420 --> 00:04:25,470
He took this parameter and this value.
52

53
00:04:25,510 --> 00:04:30,640
So as he saw that this value is getting reflected here onto the browser.
53

54
00:04:30,730 --> 00:04:37,240
He just ended up putting a XSS payload into that value after hitting enter.
54

55
00:04:37,300 --> 00:04:44,690
He can see that there was a alert document dot domain which is reflecting the name of the domain.
55

56
00:04:44,740 --> 00:04:52,510
So he reported this vulnerability to Google and Google rewarded the researcher with this much of bounty
56

57
00:04:52,660 --> 00:04:56,120
that is $3133.7.
57

58
00:04:56,410 --> 00:04:56,650
OK.
58

59
00:04:56,650 --> 00:05:04,480
So I hope you understood how we can utilize wayback archive time machine to find bugs everywhere you
59

60
00:05:04,480 --> 00:05:09,990
can find XSS in param equal to values everywhere from the way back archive.
60

61
00:05:10,480 --> 00:05:12,410
I hope this will help you guys.
61

62
00:05:12,430 --> 00:05:13,480
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,470 --> 00:00:02,910
Hello everyone.
1

2
00:00:02,910 --> 00:00:10,380
So in this video we are going to see the XSS break down of hacker one report.
2

3
00:00:10,800 --> 00:00:14,820
So we are going to see some of the very interesting test cases.
3

4
00:00:14,820 --> 00:00:20,460
And also we are going to understand the report which are submitted by other hackers on this awesome
4

5
00:00:20,460 --> 00:00:20,970
platform.
5

6
00:00:21,920 --> 00:00:29,430
So let's see the breakdown of all the hacker one reports as you can see when I go into Google and I
6

7
00:00:29,430 --> 00:00:36,670
tried to search XSS report hackerone I get a couple of reports right.
7

8
00:00:36,820 --> 00:00:40,760
Let me go into the another page and I have a lot more report.
8

9
00:00:40,930 --> 00:00:47,300
So let's do our analysis of all this report and see what all reports were submitted and how much bounty
9

10
00:00:47,310 --> 00:00:49,210
was provided.
10

11
00:00:49,210 --> 00:00:57,100
The most important thing to see here is that what are the XSS payloads that they have used and which
11

12
00:00:57,100 --> 00:01:00,130
we can also utilize into our bug hunting part.
12

13
00:01:01,450 --> 00:01:02,430
So let's see.
13

14
00:01:02,680 --> 00:01:09,160
This is a stored XSS report on Twitter which was submitted on April 1 2019 and bounty that was awarded
14

15
00:01:09,160 --> 00:01:10,360
was seven hundred dollars
15

16
00:01:15,350 --> 00:01:16,510
if I scroll down.
16

17
00:01:16,610 --> 00:01:24,320
You guys can see that it was this payload which was submitted and we all really learned this payload
17

18
00:01:24,940 --> 00:01:31,740
it is balancing the double quotes closing bracket image source equals to X on error it goes to alert
18

19
00:01:31,820 --> 00:01:39,460
document dot domain in the very very simple and the basic first payload that we learned into a video series.
19

20
00:01:39,500 --> 00:01:40,530
Cool.
20

21
00:01:40,550 --> 00:01:44,980
Let's move on to another report.
21

22
00:01:45,380 --> 00:01:52,670
As you can see stored XSS on activity reported to Shopify on 2018.
22

23
00:01:52,670 --> 00:01:56,760
August 15 bounty was was awarded two thousand dollars.
23

24
00:01:56,780 --> 00:01:58,390
Let's see the payload.
24

25
00:01:58,420 --> 00:02:04,640
Again the hacker tried to balance this by double quotes closing bracket and a very simple payload again
25

26
00:02:05,090 --> 00:02:09,590
which is a svg onload alert(2), perfect report.
26

27
00:02:09,980 --> 00:02:10,780
Let's see one more.
27

28
00:02:11,480 --> 00:02:20,330
This is IE only XSS vulnerability through program asset finder which was reported on hacker one and
28

29
00:02:20,330 --> 00:02:24,210
the bounty awarded was two thousand five hundred dollars.
29

30
00:02:24,230 --> 00:02:27,290
Let's see what's so interesting about this.
30

31
00:02:27,290 --> 00:02:32,020
And if you look closely the payload which is submitted is a very simple one.
31

32
00:02:32,660 --> 00:02:37,370
Again balancing with the double quotes closing bracket.
32

33
00:02:37,490 --> 00:02:47,010
Image source equals to X on error equals to prompt and instead of open and close round brackets the
33

34
00:02:47,010 --> 00:02:50,930
attacker has used single quote.
34

35
00:02:51,380 --> 00:02:51,870
Awesome.
35

36
00:02:52,550 --> 00:02:56,840
So perfect report with the perfect simple payload.
36

37
00:02:56,840 --> 00:03:05,090
Let's see one more stored XSS vulnerability on WordPress bounty awarded five hundred dollars.
37

38
00:03:05,090 --> 00:03:07,010
Let's see what is the payload.
38

39
00:03:07,010 --> 00:03:16,340
Again a very very simple payload balancing and then SVG onload alert document dot domain in which this
39

40
00:03:16,340 --> 00:03:17,410
payload will tell.
40

41
00:03:17,420 --> 00:03:22,370
What domain are you on, perfect payload for perfect bounty.
41

42
00:03:22,400 --> 00:03:29,930
Let's see more stored XSS on imgur profile bounty 650 dollars.
42

43
00:03:30,170 --> 00:03:36,650
Let's see the payload the payload here is the interesting one guys as you can see in my case I bypassed
43

44
00:03:36,650 --> 00:03:45,110
the filter using html entities for the alternation of opening bracket closing bracket because I
44

45
00:03:45,110 --> 00:03:47,830
noticed that it's filtering these types of brackets.
45

46
00:03:48,200 --> 00:03:55,700
So what this attacker did was instead of using opening bracket and closing bracket he used a LTGT wihch
46

47
00:03:55,700 --> 00:04:01,070
is the html encoded version of opening bracket and closing bracket.
47

48
00:04:01,070 --> 00:04:01,550
Perfect
48

49
00:04:04,670 --> 00:04:07,030
the payload was very simple script alert.
49

50
00:04:07,040 --> 00:04:08,870
One script tacked close
50

51
00:04:15,510 --> 00:04:16,470
so if a try.
51

52
00:04:16,980 --> 00:04:18,160
Yeah so perfect.
52

53
00:04:18,180 --> 00:04:22,520
So let's go to the other report this report.
53

54
00:04:22,550 --> 00:04:23,030
Yeah.
54

55
00:04:23,090 --> 00:04:31,010
So in this report it was submitted to Starbucks reflected XSS on www.Starbucks dot
55

56
00:04:31,010 --> 00:04:33,650
com bounty awarded 375 dollars.
56

57
00:04:33,710 --> 00:04:34,850
Let's see the payload.
57

58
00:04:35,000 --> 00:04:38,320
As you can see this is the payload which is URL encoded.
58

59
00:04:38,360 --> 00:04:39,470
So let's copy this.
59

60
00:04:39,470 --> 00:04:40,950
Quickly go on URL decoder.
60

61
00:04:41,510 --> 00:04:49,310
Let's try to put it here and you can see the payload is javascript alert document dot domain extra
61

62
00:04:49,310 --> 00:04:53,380
things which are added in to the payload in between.
62

63
00:04:53,510 --> 00:04:55,370
Does not makes a lot of sense.
63

64
00:04:55,750 --> 00:04:56,150
OK.
64

65
00:04:56,180 --> 00:04:58,340
It is added like that only.
65

66
00:04:58,520 --> 00:05:03,780
Without that also this payload can occur can trigger .
66

67
00:05:04,300 --> 00:05:04,890
Perfect.
67

68
00:05:04,900 --> 00:05:07,060
Let's see one more in this.
68

69
00:05:07,060 --> 00:05:13,010
You can see stored  XSS which was reported to alliance of american football bounty.
69

70
00:05:13,020 --> 00:05:15,700
awarded was 1500 dollars.
70

71
00:05:15,700 --> 00:05:16,660
Let's see the payload
71

72
00:05:20,700 --> 00:05:26,350
if you go down and you can see the payload is again we already have seen this type of payload that
72

73
00:05:26,400 --> 00:05:35,860
is balance  SVG onload prompt one perfect let's see one more reflected XSS on The academy dot
73

74
00:05:35,940 --> 00:05:41,800
upserve dot com which is basically Upserve this was reported and bounty 250 dollars.
74

75
00:05:41,830 --> 00:05:47,930
Let's see what is the payload ,Payload is balance body on load alert one.
75

76
00:05:48,130 --> 00:05:49,900
Perfect.
76

77
00:05:49,900 --> 00:05:53,860
One more XSS reflected on WordPress bounty fifty dollars.
77

78
00:05:53,890 --> 00:05:55,560
Let's see what is the payload.
78

79
00:05:55,660 --> 00:06:01,090
A very very simple payload again as you can see it is balance.
79

80
00:06:01,150 --> 00:06:04,800
Script alert document dot cookie script tag closed.
80

81
00:06:04,930 --> 00:06:09,990
We have used this payload multiple times into our video series of XSS.
81

82
00:06:12,120 --> 00:06:19,240
Let's see another report reflected XSS in www.olx.co.id
82

83
00:06:19,410 --> 00:06:21,060
Report submitted to olx.
83

84
00:06:21,090 --> 00:06:24,860
Let's see what is the payload, payload that is used.
84

85
00:06:24,960 --> 00:06:26,940
Again a very very simple version.
85

86
00:06:27,120 --> 00:06:30,860
As you can see here it is balancing script alert one.
86

87
00:06:30,870 --> 00:06:32,520
script tag closed.
87

88
00:06:32,520 --> 00:06:33,540
This is of no use.
88

89
00:06:33,540 --> 00:06:35,560
It is written like that only extra.
89

90
00:06:35,680 --> 00:06:40,200
Okay perfect.
90

91
00:06:40,770 --> 00:06:41,940
Let's see another report
91

92
00:06:45,280 --> 00:06:52,750
in this report stored XSS in link when sending message reported to Mail.ru.
92

93
00:06:52,750 --> 00:06:55,270
bounty awarded two fifty dollars.
93

94
00:06:55,270 --> 00:06:56,470
Let's see what is the payload
94

95
00:06:59,320 --> 00:07:02,440
and the payload is on mouse over javascript prompt 1.
95

96
00:07:02,950 --> 00:07:03,480
Awesome.
96

97
00:07:04,300 --> 00:07:09,880
So we have also covered on mouseover payload as you can see this is a very very simple and basic
97

98
00:07:09,880 --> 00:07:16,370
version of that payload that was submitted off on mouseover.
98

99
00:07:17,380 --> 00:07:19,590
Let's see one more report.
99

100
00:07:19,600 --> 00:07:27,010
XSS reflected XSS submitted on olx what is the payload a payload as you can see is on mouseover
100

101
00:07:27,190 --> 00:07:27,950
alert.
101

102
00:07:27,970 --> 00:07:34,000
Again the same payload are very very simple version of the payload that we have learned.
102

103
00:07:34,060 --> 00:07:34,600
Perfect.
103

104
00:07:35,740 --> 00:07:36,850
Let's see one more report
104

105
00:07:40,760 --> 00:07:48,290
and this is reflected XSS on uberinternal dot com domains bounty two thousand dollars ,in this.
105

106
00:07:48,290 --> 00:07:52,370
The payload has not been shown it has been deducted but no issues.
106

107
00:07:52,370 --> 00:08:01,790
We already know that it is a reflected XSS so it would be an reflected XSS payload which
107

108
00:08:01,790 --> 00:08:04,890
could have cost an XSS their.
108

109
00:08:05,090 --> 00:08:06,000
So perfect.
109

110
00:08:06,080 --> 00:08:13,190
We did a breakdown of many reports on hacker one and we have seen that we covered most of the types of
110

111
00:08:13,190 --> 00:08:21,460
payload that we can utilize into all our web application testing or bug bounty hunting test cases.
111

112
00:08:22,010 --> 00:08:24,140
I hope you guys understood this.
112

113
00:08:24,140 --> 00:08:28,380
Hacker one break down and it would be useful for every one of you.
113

114
00:08:28,400 --> 00:08:28,870
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,830 --> 00:00:03,500
Hello everyone.
1

2
00:00:03,600 --> 00:00:10,100
So this is the interview questions and approach video of XSS .
2

3
00:00:10,140 --> 00:00:18,630
So basically if you try to go anywhere to apply into any kinds of cybersecurity consultant or analyst
3

4
00:00:18,630 --> 00:00:25,440
position or do you go across any interview for web application and testing.
4

5
00:00:25,440 --> 00:00:30,140
They generally ask questions about or ask questions about OWASP and XSS 
5

6
00:00:30,240 --> 00:00:35,330
So understanding the interview questions for XSS is very important.
6

7
00:00:35,340 --> 00:00:41,520
So in this slide we are going to go to some of the famous interview questions and how you should tackle
7

8
00:00:41,520 --> 00:00:42,960
them.
8

9
00:00:42,960 --> 00:00:50,100
So I have listed down basically very important six questions that are very important to answer and you
9

10
00:00:50,100 --> 00:00:59,380
should know the approach that what the interviewer is asking from you so the first question is why XSS ?
10

11
00:00:59,470 --> 00:01:01,080
and how it happens.
11

12
00:01:01,450 --> 00:01:06,460
For this the interviewer is trying to ask you that.
12

13
00:01:06,550 --> 00:01:12,730
Do you know what is the root cause of XSS in this question.
13

14
00:01:12,730 --> 00:01:19,630
You don't have to start blindly saying XSS is cross-site scripting and it happens because the application
14

15
00:01:19,630 --> 00:01:29,680
is not properly validating and this question you have to be specific that why XSS is so prevalent
15

16
00:01:30,340 --> 00:01:36,580
in this you have to be on the developer perspective and you have to give the answer that way.
16

17
00:01:36,580 --> 00:01:42,970
Many applications worldwide is vulnerable to XSS although giving the definition of XSS is
17

18
00:01:42,970 --> 00:01:43,700
important.
18

19
00:01:43,810 --> 00:01:47,810
But why it happens is also very important.
19

20
00:01:48,580 --> 00:01:58,660
Okay so you can see for example XSS is a vulnerability which occurs because of no input sanitization
20

21
00:01:58,780 --> 00:02:03,940
or no proper encoding of data into any application.
21

22
00:02:03,940 --> 00:02:06,410
The root cause is javascript.
22

23
00:02:07,000 --> 00:02:10,750
All the applications in the world works on javascript.
23

24
00:02:11,170 --> 00:02:20,020
If any attacker is able to load his arbitrary javascript into the application and the application interprets
24

25
00:02:20,110 --> 00:02:24,640
it then the application is vulnerable to cross site scripting attack.
25

26
00:02:24,670 --> 00:02:25,120
This is.
26

27
00:02:25,120 --> 00:02:26,650
This answers the second part.
27

28
00:02:26,650 --> 00:02:29,310
That is how it happens.
28

29
00:02:29,350 --> 00:02:30,910
Next question.
29

30
00:02:30,910 --> 00:02:34,060
What is the severity of XSS in this question.
30

31
00:02:34,060 --> 00:02:42,640
The interviewer tries to know that what is the depth of penetration that you can perform using XSS 
31

32
00:02:43,120 --> 00:02:50,740
or how you can escalate the severity of XSS bug that you have found out by this the interviewer
32

33
00:02:50,740 --> 00:02:58,930
wants to know that what is the last step and approach that you will do if you found XSS and how
33

34
00:02:58,930 --> 00:03:02,530
you can make it to a P0 level bug.
34

35
00:03:02,830 --> 00:03:10,900
So your approach should be the severity of XSS can be very very dangerous.
35

36
00:03:10,900 --> 00:03:20,000
By doing a proper cookie stealing you can also do accounting takeovers also with the help of XSS.
36

37
00:03:20,080 --> 00:03:28,720
You can do what vertical and horizontal privilege escalation and so on that there are many many test cases
37

38
00:03:28,720 --> 00:03:37,260
that you can perform which includes account takeovers, privilege escalation, key loggers, phishing etc..
38

39
00:03:37,480 --> 00:03:42,010
Next what are the types of XSS and which is the most dangerous one.
39

40
00:03:42,310 --> 00:03:49,660
By this question the interviewer wants to know that you know through about XSS and what are the types
40

41
00:03:50,110 --> 00:03:55,870
have your then hands on on all the types of XSS practically and according to you he wants to know
41

42
00:03:56,230 --> 00:03:59,940
that which is the dangerous one and which you tend to find more.
42

43
00:04:01,000 --> 00:04:04,090
So for this question your answer should be first.
43

44
00:04:04,390 --> 00:04:09,880
The types of XSS are three as you already know the first one is reflected XSS.
44

45
00:04:09,880 --> 00:04:16,420
Second one is stored XSS and the third one is DOM based XSS which is the most dangerous type.
45

46
00:04:16,450 --> 00:04:21,440
It depends on the situation and scenario that you have on the XSS on.
46

47
00:04:21,790 --> 00:04:26,000
According to me the most dangerous XSS is the stored exercise.
47

48
00:04:26,000 --> 00:04:26,930
Why.
48

49
00:04:26,980 --> 00:04:30,120
Because you just have to store the payload once into the server.
49

50
00:04:30,550 --> 00:04:34,330
And anyone who visits it becomes vulnerable.
50

51
00:04:34,330 --> 00:04:41,800
I would like to give an example for let's say Facebook was vulnerable to store XSS and I upload
51

52
00:04:41,800 --> 00:04:43,780
a picture and into the comment box.
52

53
00:04:43,820 --> 00:04:45,880
I write please see this picture.
53

54
00:04:45,970 --> 00:04:47,430
here is an interesting comment.
54

55
00:04:48,310 --> 00:04:53,890
Anyone who comes to see that comment will automatically become vulnerable and I will be able to get
55

56
00:04:53,890 --> 00:04:54,950
his cookie.
56

57
00:04:55,300 --> 00:04:58,510
That's why stored XSS is very dangerous.
57

58
00:04:58,510 --> 00:05:04,480
But again this depends on the situation that you have been given and the application you want to test
58

59
00:05:04,480 --> 00:05:06,670
for.
59

60
00:05:07,070 --> 00:05:14,510
Next question Explain XSS to 10 year old kid HR and Red team member and this question the
60

61
00:05:14,510 --> 00:05:23,930
INTERVIEWER wants to know that you have been from base to level 10 and XSS  are your basics or
61

62
00:05:24,080 --> 00:05:33,200
your ground really very very clear about XSS so you can tackle this by explaining XSS to a
62

63
00:05:33,200 --> 00:05:40,200
10 year old kid by saying you can log in into anyone's account without their user name and password.
63

64
00:05:40,280 --> 00:05:42,850
In this scenario you are basically trying to explain.
64

65
00:05:42,890 --> 00:05:49,370
Cookie stealer how you can do an account take away if you want to explain XSS to an H.R. you can
65

66
00:05:49,370 --> 00:05:54,680
explain through a business perspective by saying if we do not fix the XSS vulnerability
66

67
00:05:54,680 --> 00:06:03,530
into our website any attacker or hacker can hack everyone's account and they can do transactions illegal
67

68
00:06:03,530 --> 00:06:09,800
transactions or some malicious activities through which there can be a very big business loss reputation
68

69
00:06:09,800 --> 00:06:17,780
loss into the market and we can lose our shares etc. explaining this to a team member wouldn't be much
69

70
00:06:17,780 --> 00:06:23,080
difficult for you as the person already knows the technicality and the severity of the bug.
70

71
00:06:25,190 --> 00:06:31,600
So the next question different ways to achieve XSS if script or alert tags are blocked.
71

72
00:06:31,910 --> 00:06:38,030
There are many examples to answer this question and in this question interviewer wants to know that
72

73
00:06:38,210 --> 00:06:41,990
have you perform different different ways of XSS.
73

74
00:06:42,050 --> 00:06:44,190
Have you used different event handlers.
74

75
00:06:44,270 --> 00:06:46,730
Have you used different types of payloads.
75

76
00:06:46,730 --> 00:06:48,680
Are you all aware about mouse payloads.
76

77
00:06:48,680 --> 00:06:50,430
Are you aware about polyglots.
77

78
00:06:50,870 --> 00:06:58,370
So for this you can see if script tag or if script tags are blocked you can use image based payloads, audio
78

79
00:06:58,370 --> 00:07:06,420
based payloads, payload video based payloads ,SVGpayload etc. Almost all payload for the other part.
79

80
00:07:06,440 --> 00:07:13,760
That is if alert tags are blocked you can be like instead of alert tags you can use confirm you can
80

81
00:07:13,760 --> 00:07:16,820
use prompt etc..
81

82
00:07:17,360 --> 00:07:21,370
So the last question is what is the fix of this vulnerability.
82

83
00:07:21,440 --> 00:07:28,080
So we already discuss what are the mitigation's of this XSS vulnerability in the previous video.
83

84
00:07:28,190 --> 00:07:29,550
You can refer to that video.
84

85
00:07:30,380 --> 00:07:32,260
So the basic answer for this.
85

86
00:07:32,300 --> 00:07:40,750
To sum up will be encoding, proper input sanitization, validation and a WAF
86

87
00:07:41,030 --> 00:07:43,090
I hope you guys like this video.
87

88
00:07:43,100 --> 00:07:44,000
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 4: Cross Site Request Forgery (CSRF)

0
1
00:00:01,610 --> 00:00:03,410
Hello everyone.
1

2
00:00:03,410 --> 00:00:14,300
So in this video we are going to learn about what is CSRF that means cross site request forgery.
2

3
00:00:14,390 --> 00:00:18,920
So we will cover what is CSRF why it happens.
3

4
00:00:18,920 --> 00:00:21,070
What is the severity of CSRF.
4

5
00:00:21,830 --> 00:00:32,510
And what are the different ways to do CSRF If so first let's see how this CSRF works.
5

6
00:00:32,970 --> 00:00:35,190
As you can see onto the screen.
6

7
00:00:35,190 --> 00:00:41,650
This is the client and this is a server on the right here is the attacker.
7

8
00:00:42,670 --> 00:00:58,120
OK so first the attacker sends a link with new e-mail and password to the client which is the victim.
8

9
00:00:58,230 --> 00:01:00,820
So the attacker is sending a link.
9

10
00:01:00,930 --> 00:01:10,410
By any means let's say by phishing he sends a link which contains a request of an email of attacker
10

11
00:01:10,920 --> 00:01:15,530
and a password off attacker client clicks on that link.
11

12
00:01:16,300 --> 00:01:23,390
Let's suppose that that link is for www dot bank dot com.
12

13
00:01:23,640 --> 00:01:34,820
As soon as client which means the victim the user clicks on that link his details will get updated onto
13

14
00:01:34,840 --> 00:01:43,020
bank dot com by the server the server accepts the new credentials which have been given by the client
14

15
00:01:43,680 --> 00:01:51,530
but the client unknowingly clicked on that specific link which contained the two things.
15

16
00:01:51,540 --> 00:01:58,470
That is a new email I.D. and a new password which got automatically updated.
16

17
00:01:58,470 --> 00:02:08,020
Now the attacker Log in with the new credentials and successfully does an account take over of client.
17

18
00:02:08,160 --> 00:02:16,140
So this is how CSRF works and CSRF is a very very dangerous vulnerability and can lead
18

19
00:02:16,170 --> 00:02:20,900
to successful account takeover sometimes.
19

20
00:02:21,090 --> 00:02:26,180
In this case the client is unable to log in into his own account.
20

21
00:02:26,190 --> 00:02:27,100
Why.
21

22
00:02:27,150 --> 00:02:34,880
Because his account is now accessible by the new credentials of the attackers.
22

23
00:02:35,270 --> 00:02:48,130
So I hope you guys understood how a basic CSRF vulnerability principle is now let's see how are we
23

24
00:02:48,130 --> 00:02:56,700
going to test for CSRF if as we can see for testing CSRF vulnerabilities on any website whenever you
24

25
00:02:56,700 --> 00:03:03,610
are doing a penetration testing or you are doing a bug hunting you need to make two accounts the first
25

26
00:03:03,610 --> 00:03:06,000
account let's say is the victim account.
26

27
00:03:06,220 --> 00:03:09,910
The second account is the attackers account.
27

28
00:03:09,910 --> 00:03:16,430
Now what the attacker is going to do is the attacker is going to generate a link.
28

29
00:03:17,020 --> 00:03:21,410
Let's say the link for email and password change.
29

30
00:03:21,440 --> 00:03:22,750
OK.
30

31
00:03:23,470 --> 00:03:32,890
Generating the link he is going to send that malicious link with updated new e-mail and password or
31

32
00:03:32,950 --> 00:03:40,930
account details to the victim to the first account now as the victim interacts with that link and
32

33
00:03:40,930 --> 00:03:49,630
clicks on that link then you have to check that the data has been updated into the profile or not.
33

34
00:03:50,290 --> 00:03:59,980
So let's say the attackers sends the link which contains the first name change functionality which means
34

35
00:04:00,160 --> 00:04:05,900
the name should change to attacker when the victim clicks on that link.
35

36
00:04:06,100 --> 00:04:13,080
And in his profile his name first name changes to from victim to attacker.
36

37
00:04:13,090 --> 00:04:24,490
That means we have successfully achieved CSRF or in another dangerous test case if the attacker sends
37

38
00:04:24,490 --> 00:04:31,890
the link with email attacker @ gmail dot com and password attacker one two three.
38

39
00:04:31,900 --> 00:04:39,680
And if that gets change then it is an account takeover vulnerability.
39

40
00:04:39,760 --> 00:04:47,980
So I hope you guys understood that how we're going to test for CSRF vulnerabilities into our bug
40

41
00:04:47,980 --> 00:04:52,850
hunting and penetration testing part thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,320 --> 00:00:04,110
Hello, everyone, and welcome.
1

2
00:00:04,890 --> 00:00:14,520
So in some of the attacks that we are going to see in the upcoming videos, we have used Burp Suite professional
2

3
00:00:14,520 --> 00:00:18,690
version as I have the professional version with me.
3

4
00:00:18,690 --> 00:00:27,480
And I strongly believe that many of the viewers from the audience must be having a pro version, can
4

5
00:00:27,480 --> 00:00:34,330
easily go ahead with the videos and simulate the attacks that I have taught into this course.
5

6
00:00:35,190 --> 00:00:43,110
Now, for those who do not have a Burp Suite professional version but have a free version can also go ahead
6

7
00:00:43,110 --> 00:00:45,440
with no problems or no issues.
7

8
00:00:46,950 --> 00:00:51,510
So you're unwilling to tell an alternative to Burp Suite.
8

9
00:00:51,510 --> 00:00:59,160
You'd see a CSRF feature that you can utilize into the CSRF section.
9

10
00:00:59,850 --> 00:01:03,330
You will be seeing that I will perform the Burp Suite
10

11
00:01:03,330 --> 00:01:12,120
CSRF attack using the engagement tools, which is a professional feature which is available only
11

12
00:01:12,120 --> 00:01:13,300
in Burp Suite PRO
12

13
00:01:14,670 --> 00:01:23,460
But for those who do not have Burp SuitePro can utilize CSRF POC generator easily to do that
13

14
00:01:23,640 --> 00:01:24,180
attack.
14

15
00:01:25,410 --> 00:01:34,380
CSRF generator is a very, very simple to use tool and can easily simulate the same attack that we
15

16
00:01:34,380 --> 00:01:37,280
do using Burp Suite PRO engagement tools.
16

17
00:01:38,100 --> 00:01:46,350
I have added a video of how to use CSRF POC generator, which is an open source tool to create the CSRF
17

18
00:01:46,410 --> 00:01:54,870
attacks into the last video of the section with the name Alternative to Burp Suite POC generator.
18

19
00:01:55,680 --> 00:02:03,010
So you can directly jump on to the last video in case you want to see how you can utilize CSRF POC
19

20
00:02:03,030 --> 00:02:05,130
generator to perform the attacks.
20

21
00:02:05,400 --> 00:02:12,120
If you are going hand in hand with the videos and practicing side by side along with me.
21

22
00:02:13,210 --> 00:02:14,590
I hope you guys understood.
22

23
00:02:14,740 --> 00:02:15,280
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,170 --> 00:00:02,960
Hello everyone.
1

2
00:00:02,970 --> 00:00:08,340
So in this video we are going to see one more proof of concept of CSRF attack.
2

3
00:00:09,780 --> 00:00:17,610
So as you can see this is my web application and I also started my burpe suite.
3

4
00:00:17,970 --> 00:00:23,750
So as for the prerequisite the victim need to be logged in into the application.
4

5
00:00:24,140 --> 00:00:27,740
So the victim is logging into the application right now using his credentials.
5

6
00:00:27,740 --> 00:00:28,760
as test
6

7
00:00:34,820 --> 00:00:37,760
perfect the user has logged in into his account.
7

8
00:00:37,790 --> 00:00:42,210
Now the user is going to update his profile.
8

9
00:00:42,290 --> 00:00:51,310
So let's say he put the name as rohit and address as hacktify and update this account.
9

10
00:00:51,320 --> 00:00:56,030
Now what we're going to do is we are going to capture this request into burpe suite and we're going to
10

11
00:00:56,030 --> 00:01:04,660
right click and click on generate CRFP poc  we're going to copy this html and we are
11

12
00:01:04,660 --> 00:01:09,200
going to make a notepad file and paste it into that.
12

13
00:01:09,320 --> 00:01:17,850
Us quickly save this file as testphpcsrf.html perfect.
13

14
00:01:17,980 --> 00:01:18,250
Now
14

15
00:01:21,740 --> 00:01:25,440
let's try to reload this and let's see if the details are still there.
15

16
00:01:26,610 --> 00:01:27,840
Obviously it should be
16

17
00:01:31,310 --> 00:01:39,800
now what the attacker is going to do is attack it is going to make poc like this in which he is
17

18
00:01:39,800 --> 00:01:48,070
going to put the name as rohit attacker and the address as rohithacktify attacker.
18

19
00:01:50,060 --> 00:01:51,080
OK.
19

20
00:01:51,260 --> 00:01:56,760
So the attacker is going to change two fields of the victim.
20

21
00:01:57,980 --> 00:01:59,150
Let's verify this now.
21

22
00:02:00,930 --> 00:02:03,750
As you can see these are the details of the victim.
22

23
00:02:03,960 --> 00:02:14,180
Now the victim gets a link onto his e-mail let's say by phishing and the victim is going to interact
23

24
00:02:14,240 --> 00:02:15,560
with that e-mail.
24

25
00:02:15,980 --> 00:02:19,430
That e-mail contained the file that is the html file.
25

26
00:02:20,480 --> 00:02:25,830
And the victim unknowingly clicks on that file or lets say that request.
26

27
00:02:26,030 --> 00:02:33,680
And what happens with this account is his account gets updated with these details.
27

28
00:02:33,680 --> 00:02:39,620
That is the name got updated as well as the address got updated.
28

29
00:02:39,620 --> 00:02:48,050
So I hope you guys understood the concept of CSRF and you have no doubt into this CSRF proof of
29

30
00:02:48,050 --> 00:02:51,380
concept thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,440 --> 00:00:02,790
Hello everyone.
1

2
00:00:02,790 --> 00:00:13,990
So in this video are going to see how to perform a CSRFattack so first thing first CSRF on log
2

3
00:00:13,990 --> 00:00:16,680
in or log out is not a sensitive bug.
3

4
00:00:16,840 --> 00:00:20,260
And it is considered out of scope.
4

5
00:00:20,260 --> 00:00:28,900
I have seen many people doing logging log out CSRF so basically it does not hold any severity and is
5

6
00:00:28,900 --> 00:00:32,820
considered out of scope by all the programs.
6

7
00:00:32,830 --> 00:00:39,610
So what does log in  log out basically means and why it does not hold any critical severity.
7

8
00:00:41,320 --> 00:00:52,180
So basically if you're able to log out anyone from their account let's say someone sends a link to me
8

9
00:00:52,780 --> 00:00:59,490
onto my email I click on that link and I get log out of my account.
9

10
00:00:59,560 --> 00:01:00,550
So what.
10

11
00:01:00,550 --> 00:01:01,450
No issues.
11

12
00:01:01,450 --> 00:01:04,910
I'm again going to log in into my account.
12

13
00:01:05,110 --> 00:01:08,620
There is no security impact into this.
13

14
00:01:08,620 --> 00:01:16,570
And this vulnerability arises and lies in all the applications in the world.
14

15
00:01:16,960 --> 00:01:22,610
Even if you try to do this in gmail you will be able to perform this action.
15

16
00:01:23,230 --> 00:01:25,500
So log in log out.
16

17
00:01:25,570 --> 00:01:34,000
CSRF is not a valid CSRF if as I've been hearing by lot of people a lot of security researchers talking
17

18
00:01:34,000 --> 00:01:43,700
log in log out CSRF if it is out of scope and it is not valid the three a prerequisite that are
18

19
00:01:43,700 --> 00:01:54,200
very important for CSRF are first thing first the victims should be logged in into his account.
19

20
00:01:54,200 --> 00:02:03,270
Second whatever link you're going to send the victim the victim should click on it.
20

21
00:02:03,570 --> 00:02:06,840
Third  the application should be vulnerable to CSRF.
21

22
00:02:06,870 --> 00:02:15,120
For the CSRF to happen itself I hope you understood this three prerequisites for CSRF attack to happen.
22

23
00:02:16,650 --> 00:02:24,300
So let's begin checking for pages where sensitive data is stored and sensitive action can be performed
23

24
00:02:24,420 --> 00:02:33,060
is where we will hunt for CSRF making a CSRF POC and updating the data on the victim's account
24

25
00:02:33,150 --> 00:02:42,270
is considered a valid CSRF bug if the application does not do any input validation or sanitization and
25

26
00:02:42,270 --> 00:02:48,020
take actions is very very dangerous.
26

27
00:02:48,210 --> 00:02:59,290
So it's the practical time and let's see the demonstration of CSRF and how we can do this as you can
27

28
00:02:59,290 --> 00:03:07,740
see I am on this application where in I'm going to perform CSRF yes.
28

29
00:03:07,950 --> 00:03:16,500
So I will just go to this change or admin password functionality were in I'm going to change the password
29

30
00:03:16,650 --> 00:03:19,180
for this account.
30

31
00:03:19,350 --> 00:03:26,310
So as you can see and consider right now I am logged In into the victim's account.
31

32
00:03:26,490 --> 00:03:28,910
So consider this is a victim's account
32

33
00:03:33,950 --> 00:03:40,100
now the password that I'm going to change is admin so I will just type in admin ADMIN.
33

34
00:03:40,130 --> 00:03:41,620
Now I will change this password.
34

35
00:03:41,900 --> 00:03:45,140
So first password change attempt successful.
35

36
00:03:45,140 --> 00:03:47,980
And the password has been changed to admin ADMIN.
36

37
00:03:48,050 --> 00:03:49,050
Perfect.
37

38
00:03:49,070 --> 00:03:54,740
Now if I want to log in into the application I have to use the new password that is admin
38

39
00:03:58,200 --> 00:03:59,570
now.
39

40
00:04:00,120 --> 00:04:05,600
One way to do is I'm going to change the password to Rohit this time.
40

41
00:04:05,600 --> 00:04:11,260
So rohit and rohit  and before submitting this I'm going to capture this.
41

42
00:04:11,510 --> 00:04:16,010
So I will just hit change and I was unable to capture.
42

43
00:04:16,160 --> 00:04:21,150
Let me just set up the Burpe suite with my brousers.
43

44
00:04:21,200 --> 00:04:22,120
I missed this.
44

45
00:04:22,130 --> 00:04:26,180
So let me just quickly set up perfect.
45

46
00:04:26,390 --> 00:04:30,110
So now my Burpe suite is ready.
46

47
00:04:30,110 --> 00:04:31,670
I'm again going to change my password.
47

48
00:04:31,670 --> 00:04:36,070
Let's say this time  i"m going to keep it as hacktify.
48

49
00:04:36,080 --> 00:04:41,320
I will just go in Burpe suite intercept On I will click on change password.
49

50
00:04:41,390 --> 00:04:42,550
Perfect.
50

51
00:04:43,060 --> 00:04:49,400
I'll go into the Burpe suite and I can see that I have captured the request for password change.
51

52
00:04:49,390 --> 00:04:53,110
Now here comes the main thing within.
52

53
00:04:53,230 --> 00:04:55,970
I'm going to perform the CSRF attack.
53

54
00:04:57,080 --> 00:05:04,030
So for performing this attack I need to generate a CSRF POC that is CSRF.
54

55
00:05:04,040 --> 00:05:13,490
Proof of concept so I will just right click here go to engagement tools and click on generate CSRF POC
55

56
00:05:13,490 --> 00:05:15,380
the last option.
56

57
00:05:15,920 --> 00:05:20,660
As soon as I click on there as you can see two things are being generated.
57

58
00:05:20,660 --> 00:05:27,910
The first thing is the request and the second thing is the CSRF html perfect.
58

59
00:05:27,940 --> 00:05:35,780
So as you can see in the password field which I have highlighted is password new hacktify
59

60
00:05:36,130 --> 00:05:37,850
password confirm hactify.
60

61
00:05:40,840 --> 00:05:46,960
So I'm going to copy this by clicking on copy html and I'm going to open a notepad where in
61

62
00:05:46,960 --> 00:05:55,180
I'm going to paste this so I have pasted the html code that I generated from the POC generator and let
62

63
00:05:55,180 --> 00:05:57,760
me just make the new password as hacktify.
63

64
00:05:57,760 --> 00:05:59,440
One two three.
64

65
00:05:59,440 --> 00:06:05,930
Now this is the attacker who is changing the password to hacktify.
65

66
00:06:06,010 --> 00:06:07,150
One two three.
66

67
00:06:07,480 --> 00:06:13,280
This is the attacker which has generated the POC and has changed the password to one two three.
67

68
00:06:13,300 --> 00:06:13,840
Perfect.
68

69
00:06:15,790 --> 00:06:18,400
So let me save this
69

70
00:06:21,210 --> 00:06:28,830
let me name udemy CSRFdot html and let me save this in folder and click on
70

71
00:06:28,830 --> 00:06:29,250
Save
71

72
00:06:32,070 --> 00:06:39,880
fine, let me just close this and forward this request so my password has been changed to hacktify
72

73
00:06:39,890 --> 00:06:41,540
now let me just
73

74
00:06:44,940 --> 00:06:48,170
show you something now.
74

75
00:06:48,300 --> 00:06:54,510
Now imagine guys this who was logged in the victim was logged in.
75

76
00:06:54,510 --> 00:06:59,640
Now the victim gets a link onto his email OK.
76

77
00:07:00,090 --> 00:07:03,930
And that email contains the html page.
77

78
00:07:03,930 --> 00:07:11,970
So let's add this he got into the e-mail and when he interacts with the e-mail let's say by clicking
78

79
00:07:11,970 --> 00:07:16,680
on here the submit request assume this has been sent by the attacker.
79

80
00:07:17,520 --> 00:07:27,330
So when he clicks on this unknowingly something happens into this account as you can see something happened
80

81
00:07:27,480 --> 00:07:32,330
what happened the password has changed for the victim's account.
81

82
00:07:32,550 --> 00:07:33,070
Yes.
82

83
00:07:33,090 --> 00:07:36,840
So let's try to verify that the password changed or not.
83

84
00:07:38,790 --> 00:07:40,890
So let's try to log in.
84

85
00:07:40,890 --> 00:07:44,430
The name is admin and let me type the password as.
85

86
00:07:44,730 --> 00:07:50,760
First let me type the wrong password which was the password for victim and victim kept password that
86

87
00:07:50,760 --> 00:07:52,660
was hactify.
87

88
00:07:52,860 --> 00:07:58,200
So let me just copy this and pasted here and try to log in it will say log in failed.
88

89
00:07:58,200 --> 00:08:03,900
Now let me try with the password that the attacker kept on the victim's account.
89

90
00:08:04,560 --> 00:08:11,530
So the attacker sended a link which contained a password that was hacktify one two three.
90

91
00:08:11,910 --> 00:08:17,910
And let's try to log in with this password into the victim's account and perfect.
91

92
00:08:17,910 --> 00:08:23,400
The attacker has successfully taken over the victim's account.
92

93
00:08:23,400 --> 00:08:27,090
I hope you guys understood what we did into this video.
93

94
00:08:27,240 --> 00:08:36,320
So remember the three prerequisite that need to perform a successful CSRF attack.
94

95
00:08:36,510 --> 00:08:41,340
The first thing is the victim should be logged in into the application.
95

96
00:08:41,340 --> 00:08:45,930
Second thing is the victim should interact with the link.
96

97
00:08:45,930 --> 00:08:53,220
Third thing is the website or the web application should be vulnerable to CSRF itself.
97

98
00:08:53,250 --> 00:09:00,240
I hope you guys understood how we're able to perform a CSRF attack onto this application in the next
98

99
00:09:00,240 --> 00:09:05,410
videos we're going to see CSRF on live applications.
99

100
00:09:05,430 --> 00:09:05,910
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,160 --> 00:00:03,600
Hello everyone.
1

2
00:00:03,600 --> 00:00:12,670
So in this video we are going to see a CSRF on to Web site.
2

3
00:00:12,930 --> 00:00:18,580
I have already made PoC for CSRF so I will just clarify something.
3

4
00:00:18,580 --> 00:00:20,050
Not to get confused here.
4

5
00:00:20,470 --> 00:00:27,790
So I'm logged in into account as you can see I am logged in into account which is the srsecure
5

6
00:00:27,790 --> 00:00:30,080
@gmail dot com.
6

7
00:00:30,250 --> 00:00:34,970
I will just try to reload this account and try to show you the details.
7

8
00:00:35,200 --> 00:00:45,380
Over here in the business registration part if I submit this request as I can see the details over here.
8

9
00:00:48,070 --> 00:00:50,050
Which is the srsecure@gmail.
9

10
00:00:50,050 --> 00:00:55,670
Dot com will get updated to black ops dot Ruby @gmail.com.
10

11
00:00:55,720 --> 00:01:01,090
So in here the attacker sended a request.
11

12
00:01:01,570 --> 00:01:09,760
And this is the victim's account and victim tried to interact with that request when victim interacted
12

13
00:01:09,760 --> 00:01:11,650
with that request.
13

14
00:01:11,650 --> 00:01:15,610
The e-mail I.D. of the victim got changed.
14

15
00:01:15,910 --> 00:01:24,850
So I hope you guys understood this CSRF attack in which the e-mail was able to get changed and the attacker
15

16
00:01:24,940 --> 00:01:29,050
is able to do an account takeover onto this user.
16

17
00:01:29,090 --> 00:01:29,590
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,240 --> 00:00:02,740
Hello everyone.
1

2
00:00:02,740 --> 00:00:11,140
So in this video we are going to do CSRf account takeover so we are going to perform this attack
2

3
00:00:11,170 --> 00:00:14,810
by changing the e-mail I.D. and password of the victim.
3

4
00:00:15,760 --> 00:00:23,500
And through this attack the attacker is going to get complete access of the account of the victim account
4

5
00:00:24,580 --> 00:00:31,120
which will lead to permanent lock out of the user or the victim he or she may not be able to log in
5

6
00:00:31,240 --> 00:00:38,860
into his or her account anymore because both the details that are the email I.D. and the password will
6

7
00:00:38,860 --> 00:00:40,330
be changed by the attacker.
7

8
00:00:41,740 --> 00:00:46,460
So it's a practical time and let's see this in action.
8

9
00:00:46,600 --> 00:00:52,510
So I have found this Vulnerability onto our website which is bibme.
9

10
00:00:54,220 --> 00:00:56,290
So let's try to do this.
10

11
00:00:56,290 --> 00:00:58,510
So first I will open this Web site
11

12
00:01:02,390 --> 00:01:07,940
and yes I have also configured my Burpe suite with Mozilla Firefox.
12

13
00:01:07,940 --> 00:01:15,800
Let me just try to go and create two accounts first for your better understanding.
13

14
00:01:15,800 --> 00:01:20,470
So I will just go years and I will try to create the first account
14

15
00:01:32,170 --> 00:01:38,440
so let's say my first account details are my e-mail address and I will give a password.
15

16
00:01:39,580 --> 00:01:42,520
So I kept a very simple password.
16

17
00:01:42,520 --> 00:01:45,450
I will choose random details.
17

18
00:01:45,610 --> 00:01:49,510
And let me try to click on Create Account perfect
18

19
00:01:57,120 --> 00:01:57,490
OK.
19

20
00:01:57,500 --> 00:02:02,250
So I have successfully created an account on this Web site.
20

21
00:02:02,300 --> 00:02:06,320
So let me just go into my account.
21

22
00:02:06,680 --> 00:02:08,700
Let me click on my account again
22

23
00:02:13,130 --> 00:02:15,500
and see my account details
23

24
00:02:19,140 --> 00:02:19,640
okay.
24

25
00:02:19,730 --> 00:02:20,900
It is still loading.
25

26
00:02:21,100 --> 00:02:21,340
Yeah.
26

27
00:02:21,340 --> 00:02:22,470
Perfect.
27

28
00:02:22,480 --> 00:02:25,030
And I can see the added account option.
28

29
00:02:25,030 --> 00:02:31,870
So what I'm going to do is let me open one more private window as I have already made one victim account.
29

30
00:02:31,900 --> 00:02:34,750
Now I'm going to make an attacker account
30

31
00:02:37,510 --> 00:02:43,390
so let me open the website again and I'm going to sign up and make an attacker account
31

32
00:02:54,770 --> 00:02:55,000
Yeah.
32

33
00:02:55,120 --> 00:03:27,220
So let me just click on Create Account and this will redirect me to the account creation process.
33

34
00:03:27,260 --> 00:03:31,530
I think there is some issue Internet issue with the website.
34

35
00:03:31,580 --> 00:03:32,890
It is still loading.
35

36
00:03:33,380 --> 00:03:38,390
Okay so let's wait for this website to load because we need to make one more account.
36

37
00:03:38,390 --> 00:03:42,880
That is the attackers account to perform a successful .
37

38
00:03:42,890 --> 00:03:43,100
CSRF
38

39
00:03:58,840 --> 00:04:01,660
so as you can see this is the victim's account.
39

40
00:04:02,260 --> 00:04:07,190
Let me just till then fill the details of victims so I'm going to type.
40

41
00:04:07,190 --> 00:04:12,960
Victim in the first name in the last name I'm going to type account and let me save the changes
41

42
00:04:27,500 --> 00:04:28,430
yeah.
42

43
00:04:28,910 --> 00:04:31,000
I think this has opened.
43

44
00:04:31,010 --> 00:04:34,820
Let me create an account quickly.
44

45
00:04:35,000 --> 00:04:37,400
Which is going to be an attacker account.
45

46
00:04:37,490 --> 00:04:43,100
Or it is saying email already use so let me use my new email which is this and let me try to create
46

47
00:04:43,130 --> 00:04:46,860
one more account.
47

48
00:04:47,390 --> 00:04:57,290
Okay so let's use another e-mail and change the details let's say student middle schools 8 grade
48

49
00:04:58,100 --> 00:04:59,470
and create account.
49

50
00:04:59,600 --> 00:05:00,760
Yep perfect.
50

51
00:05:02,940 --> 00:05:11,560
So at the left side you can see is the victim's account at the right side of the screen is the attackers
51

52
00:05:11,560 --> 00:05:12,670
account.
52

53
00:05:12,670 --> 00:05:15,510
So the attacker has also made this account.
53

54
00:05:15,520 --> 00:05:23,850
Now let me just quickly navigate and move to my account as this account is been made by an email.
54

55
00:05:23,860 --> 00:05:27,400
That is the srsecure@gmail.com
55

56
00:05:30,120 --> 00:05:33,860
let me just wait for my account details to pop up.
56

57
00:05:40,820 --> 00:05:42,310
Let me click on my account details.
57

58
00:05:42,310 --> 00:05:43,270
Perfect.
58

59
00:05:43,270 --> 00:05:47,410
So I will just fill the first name as attacker and in the last name account.
59

60
00:05:47,650 --> 00:05:49,660
So this is attacker's account.
60

61
00:05:50,080 --> 00:05:52,210
And let me intercept this request quickly.
61

62
00:05:53,860 --> 00:05:55,670
Let me just forward this request.
62

63
00:05:55,690 --> 00:05:57,540
This request this request.
63

64
00:05:57,550 --> 00:06:05,290
This one this one until I see the right request which contains the data that is attackers account.
64

65
00:06:05,290 --> 00:06:05,790
Perfect.
65

66
00:06:06,220 --> 00:06:12,550
So as you can see this is the post request which is going to be 
bibme.org website.
66

67
00:06:12,730 --> 00:06:14,630
And this contains the detail.
67

68
00:06:14,650 --> 00:06:22,330
So let me just scroll down and type your attackers in the search bar and you can see it has 
68

69
00:06:22,330 --> 00:06:24,880
matched the first name position.
69

70
00:06:24,880 --> 00:06:32,010
So this is the post request which is going to the website for then change of the name.
70

71
00:06:32,170 --> 00:06:40,620
As you can see it also contains a lot of parameters which is first name last name and user e-mail.
71

72
00:06:40,660 --> 00:06:41,050
Also
72

73
00:06:43,800 --> 00:06:47,450
let me just generate CSRF POC quickly.
73

74
00:06:47,520 --> 00:06:53,210
Let me copy this and click on copy html.
74

75
00:06:53,430 --> 00:06:58,590
Let me just open a new notepad file quickly and let me paste all here.
75

76
00:06:59,310 --> 00:07:10,680
So now what this attacker is going to do his attacker has captured his own his own added profile request
76

77
00:07:10,890 --> 00:07:16,500
which contains the change in the first name and the last name that we're going to do right now.
77

78
00:07:17,160 --> 00:07:25,120
So let me just save this file first as bibme check CSRF dot html and quickly it is saved.
78

79
00:07:25,140 --> 00:07:28,640
Let me just turn this off.
79

80
00:07:29,560 --> 00:07:30,390
Yeah.
80

81
00:07:31,090 --> 00:07:37,740
And yes we have saved basically the request into the attackers account.
81

82
00:07:37,820 --> 00:07:38,630
Let me just show you.
82

83
00:07:38,630 --> 00:07:40,430
So this is basically the attackers account.
83

84
00:07:40,430 --> 00:07:42,570
We do not want this anymore.
84

85
00:07:42,590 --> 00:07:45,830
Now we are going to attack the victim.
85

86
00:07:46,820 --> 00:07:48,350
So what happens.
86

87
00:07:48,350 --> 00:07:52,240
Let me just go to my account and show you that this is a victim's account.
87

88
00:07:52,250 --> 00:07:52,760
Perfect.
88

89
00:07:54,050 --> 00:07:57,020
And the e-mail is hacker dot Udemy @gmail dot com.
89

90
00:07:57,020 --> 00:07:57,880
This is the victim.
90

91
00:07:57,890 --> 00:07:59,120
The first account.
91

92
00:07:59,240 --> 00:08:09,280
Now what the attacker does is attacker is going to change something.
92

93
00:08:09,500 --> 00:08:16,430
Attacker is going to change the e-mail address basically attacker is going to do a complete takeover
93

94
00:08:16,580 --> 00:08:18,140
of the victim's account.
94

95
00:08:21,980 --> 00:08:32,930
So Let me just try to save this and let me try to open it here and hit on submit request as you can
95

96
00:08:32,930 --> 00:08:38,900
see in this html file.
96

97
00:08:39,110 --> 00:08:45,750
There were a lot of things in the first name it was attackers.
97

98
00:08:46,070 --> 00:08:47,100
Right.
98

99
00:08:47,120 --> 00:08:53,340
So we are going to verify if the detail gets changed.
99

100
00:08:53,330 --> 00:08:58,670
So I'm going to open this html over in the victim's browser.
100

101
00:08:58,670 --> 00:09:06,170
So we're assuming the that the victim got this e-mail with this link victim interacted with it and now
101

102
00:09:07,430 --> 00:09:10,500
victims detail will get changed.
102

103
00:09:11,000 --> 00:09:13,330
Let's verify.
103

104
00:09:13,370 --> 00:09:14,810
Let me just go back here.
104

105
00:09:14,830 --> 00:09:17,040
Let me let me just try to reload this.
105

106
00:09:17,960 --> 00:09:20,140
Let's see if the details get changed.
106

107
00:09:27,360 --> 00:09:34,870
If the details get changed successfully by the attackers request then this is a successful account 
107

108
00:09:34,870 --> 00:09:35,800
takeover .
108

109
00:09:36,030 --> 00:09:41,080
Perfect as you can see the details have got to change first name is attacker.
109

110
00:09:41,130 --> 00:09:46,300
Last name is account e-mail address is the srsecure@gmail dot com.
110

111
00:09:46,320 --> 00:09:52,950
So basically the attacker has done a complete account takeover of the victim and for proof of concept
111

112
00:09:53,490 --> 00:09:59,940
we have changed the victim details and the detail is first name his attacker last name is account and
112

113
00:09:59,940 --> 00:10:03,710
the e-mail is the srsecure@gmail dot com.
113

114
00:10:04,380 --> 00:10:11,070
I hope you guys understood this demonstration of CSRF on the live Websites.
114

115
00:10:11,170 --> 00:10:11,720
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,020 --> 00:00:02,510
Hello everyone.
1

2
00:00:02,520 --> 00:00:09,530
So in this video we are going to see CSRF attack that is cross site request forgery.
2

3
00:00:09,780 --> 00:00:16,490
So as you can see on the screen there is an option to change your password so here in.
3

4
00:00:16,530 --> 00:00:22,920
I'm going to keep a password that is rohit so I'll type this into the new password field as well
4

5
00:00:22,920 --> 00:00:29,570
as into the retyped new password field before submitting change.
5

6
00:00:29,580 --> 00:00:37,570
I'm going to intercept the request into Burpe suite as you can see I have got a request into Burpe suite over
6

7
00:00:37,580 --> 00:00:44,800
here the new password is Rohit and the password can fulfill is also rohit.
7

8
00:00:44,820 --> 00:00:48,690
Let me just quickly click on action.
8

9
00:00:48,810 --> 00:00:52,560
Send this to repeater in case I want to use this request again.
9

10
00:00:52,560 --> 00:01:02,070
Click on engagement tools generate CSRF poc as you can see I've opened the CSR POC generator which
10

11
00:01:02,130 --> 00:01:05,750
I will utilize to do a CSRF attack.
11

12
00:01:06,330 --> 00:01:09,700
I will just quickly forward this as we can see onto the screen.
12

13
00:01:09,780 --> 00:01:12,970
The password has been changed successfully.
13

14
00:01:13,440 --> 00:01:14,040
Perfect.
14

15
00:01:14,220 --> 00:01:17,000
So I'll go back to my POC generator.
15

16
00:01:17,070 --> 00:01:24,450
I'm going to copy the CSRF html from here of this specific request.
16

17
00:01:24,450 --> 00:01:27,820
So let me just copy this.
17

18
00:01:27,840 --> 00:01:33,380
Yes after copying this let me try to paste it.
18

19
00:01:33,550 --> 00:01:33,980
here.
19

20
00:01:34,470 --> 00:01:36,270
So I have pasted it over here.
20

21
00:01:37,470 --> 00:01:37,770
OK.
21

22
00:01:37,800 --> 00:01:41,430
So now this is the attackers part.
22

23
00:01:41,820 --> 00:01:51,330
So now the attacker has made a POC that is CSRF POC and the attacker is setting a value
23

24
00:01:51,360 --> 00:01:52,310
that is a rohit.
24

25
00:01:52,300 --> 00:01:58,110
One two three as we can see what here in the password new field as well as password confirm field the
25

26
00:01:58,110 --> 00:01:59,030
same password.
26

27
00:02:00,240 --> 00:02:09,770
So the attacker has made a CSRF POC and he is going to save it like this let's say CSRF one dot html.
27

28
00:02:12,240 --> 00:02:21,900
That's udemycsrf1.html and now the attacker sends the CSRF page basically
28

29
00:02:21,900 --> 00:02:25,140
the link to the victim using phishing.
29

30
00:02:27,180 --> 00:02:34,270
So now you're going to open this  udemycsrf1.html  .
30

31
00:02:34,350 --> 00:02:40,920
Now this is the victim which is going to interact with that specific link as soon as the victim interacts
31

32
00:02:40,920 --> 00:02:41,620
with that link.
32

33
00:02:41,640 --> 00:02:44,850
Something happens as you can see what has happened.
33

34
00:02:44,850 --> 00:02:48,450
The password has been changed for the victim's account.
34

35
00:02:48,450 --> 00:02:50,840
Let's try to log out and check.
35

36
00:02:50,940 --> 00:02:56,280
So let's try to log in with user name B and let's try the password first.
36

37
00:02:56,310 --> 00:02:58,400
So the attackers password is roht.
37

38
00:02:58,410 --> 00:02:59,160
One two three.
38

39
00:02:59,160 --> 00:03:01,330
The user's password is only rohit.
39

40
00:03:01,350 --> 00:03:02,860
So let's try
40

41
00:03:02,940 --> 00:03:03,300
with rohit
41

42
00:03:03,300 --> 00:03:05,030
One two three and yes.
42

43
00:03:05,130 --> 00:03:06,210
Perfect.
43

44
00:03:06,210 --> 00:03:08,420
So we have been logged in into the application.
44

45
00:03:09,000 --> 00:03:16,590
So in this video we understood that how a CSRF happened and how an attacker can take over
45

46
00:03:17,040 --> 00:03:22,380
the victim's account by changing his or her password.
46

47
00:03:22,410 --> 00:03:25,020
So this is one of the ways to exploit CSRF.
47

48
00:03:25,230 --> 00:03:26,600
I hope you guys understood.
48

49
00:03:26,610 --> 00:03:27,060
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,330 --> 00:00:02,820
Hello everyone.
1

2
00:00:02,830 --> 00:00:11,740
So in this video we are going to again see one more type of CSRf as you can see in this CSRF the
2

3
00:00:11,740 --> 00:00:15,640
attacker is going to transfer some amount from the victim's account.
3

4
00:00:16,390 --> 00:00:22,560
So as you can see the victim currently has nine hundred and ninety six euros into his account.
4

5
00:00:23,350 --> 00:00:27,980
And the victim wants to transfer the money to let's say this account number.
5

6
00:00:28,060 --> 00:00:34,230
And what are the amount he wants to transfer as soon as the user clicks on transfer button.
6

7
00:00:34,240 --> 00:00:37,630
The amount will get transferred to this account number.
7

8
00:00:37,630 --> 00:00:38,530
So let's see this
8

9
00:00:42,620 --> 00:00:44,610
so this much is the account balance.
9

10
00:00:44,690 --> 00:00:47,950
If the victim wants to transfer this he will just keep on transfer.
10

11
00:00:47,960 --> 00:00:52,800
And you can see it gets one euro gets deducted.
11

12
00:00:52,850 --> 00:00:57,170
Similarly I performed one more and again the money got  detucted.
12

13
00:00:58,010 --> 00:01:01,170
So the victim is able to do transfers.
13

14
00:01:01,170 --> 00:01:08,560
Now we are going to capture this request in Burpe suite as you can see this is a request with the amount
14

15
00:01:08,560 --> 00:01:09,860
of one.
15

16
00:01:09,880 --> 00:01:14,820
Let's just quickly go to generate CSRF POC and this is the POC which has been generated.
16

17
00:01:14,920 --> 00:01:22,820
Let's quickly copy to html and let's go into our favorite editor and let's try to pate it all
17

18
00:01:22,820 --> 00:01:23,980
here.
18

19
00:01:24,370 --> 00:01:34,170
After pasting it as you can see this is the request which attacker is going to send to the victim and
19

20
00:01:34,170 --> 00:01:41,550
as soon as victim is going to interact with this specific link the amount will get transferred into
20

21
00:01:41,550 --> 00:01:43,220
the attackers account.
21

22
00:01:43,800 --> 00:01:50,120
So let's see this in the amount field the attacker is going to type.
22

23
00:01:50,120 --> 00:01:53,360
So let's say the balance is 991 euros.
23

24
00:01:53,390 --> 00:01:59,480
So the attacker is going to make the account empty by transferring 990 euros.
24

25
00:01:59,480 --> 00:02:00,480
Perfect.
25

26
00:02:00,500 --> 00:02:03,980
So there will be only one euro left into the victim's account.
26

27
00:02:03,980 --> 00:02:10,640
Now the attacker is going to save this quickly and after saving this we are going to search for this.
27

28
00:02:10,640 --> 00:02:11,250
Yep.
28

29
00:02:11,360 --> 00:02:14,530
So the attacker has sended this request to the victim.
29

30
00:02:14,540 --> 00:02:21,590
And as soon as the victim interacts with this request as we know this is the way to attack as soon as
30

31
00:02:21,590 --> 00:02:25,920
the victim clicks or interacts there will be a deduction.
31

32
00:02:26,000 --> 00:02:33,770
So let's try to reload the victim's account balance and when we try to reload this and see perfect there
32

33
00:02:33,770 --> 00:02:45,380
is zero euros which means all the amount has been successfully deducted from his account.
33

34
00:02:45,380 --> 00:02:57,500
So this was one of the ways in which transactions can also happen and the attacker can do funds transfer
34

35
00:02:57,680 --> 00:03:02,490
from victim's account by exploiting a successful CSRF.
35

36
00:03:03,170 --> 00:03:04,590
I hope you guys understood.
36

37
00:03:04,610 --> 00:03:05,090
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,930 --> 00:00:02,370
Hello everyone.
1

2
00:00:02,370 --> 00:00:10,740
So in this video we're going to see how we can do CSRF by changing the request method as we know
2

3
00:00:11,160 --> 00:00:18,670
some applications  validate based on post method for submitting the user data.
3

4
00:00:19,020 --> 00:00:26,250
So whenever the user tried to submit some details to the server the method that generally has been used
4

5
00:00:26,340 --> 00:00:28,900
is a post method.
5

6
00:00:29,040 --> 00:00:36,010
What if we tried to change the method  from post to get or sometimes vice versa.
6

7
00:00:36,150 --> 00:00:40,080
We will be able to successfully exploit the CSRF.
7

8
00:00:40,920 --> 00:00:49,380
So let's see this into a practical in which we will understand that how can we achieve CSRF by changing
8

9
00:00:49,380 --> 00:00:52,260
the request method.
9

10
00:00:52,260 --> 00:00:57,430
So it's the practical time and let's see this how we can do this.
10

11
00:00:57,450 --> 00:01:02,880
So as you can see on the screen I'm on to the CSRF change password.
11

12
00:01:03,240 --> 00:01:11,090
So I'm going to change the password for this account as you can see there are the two fields of password.
12

13
00:01:11,140 --> 00:01:17,740
So what I'm going to do right now is let's say I'm willing to take the password as hacktify let me
13

14
00:01:17,740 --> 00:01:27,150
just paste it here and let me just paste here and go in burp intercept on click on change.
14

15
00:01:27,280 --> 00:01:33,650
Let me goon burpe and you can see this is the request that I have got into Burpe suite.
15

16
00:01:34,120 --> 00:01:41,410
If you look closely the credentials of the password are going into which method it's a get method.
16

17
00:01:42,850 --> 00:01:52,710
So what I am going to quickly do is I'm going to change the request METHOD AND I WILL MAKE THIS FROM
17

18
00:01:52,710 --> 00:02:00,960
get to post as you can see whatever was going into URL has now become into the body.
18

19
00:02:00,960 --> 00:02:10,560
So this is one of the way of bypassing CSRF If sometimes post request can be made into get and sometimes
19

20
00:02:10,920 --> 00:02:14,280
get request can be changed to post.
20

21
00:02:14,430 --> 00:02:21,120
So let's continue and let's see how can we attack this.
21

22
00:02:21,270 --> 00:02:28,230
Let me just go to engagement tools quickly generate CSRF POC as we do it are always let's copy
22

23
00:02:28,230 --> 00:02:37,650
this html code remember guys this is the post request this time not the GET request we're going to copy
23

24
00:02:37,650 --> 00:02:38,290
this.
24

25
00:02:38,340 --> 00:02:40,170
Let me just drop this.
25

26
00:02:40,380 --> 00:02:43,970
So I dropped which means the password did not change.
26

27
00:02:44,070 --> 00:02:48,200
Let me just do back the password has not changed.
27

28
00:02:48,360 --> 00:02:51,820
Let me go to my favorite editor again and let me just paste it here.
28

29
00:02:52,620 --> 00:02:57,660
So as you can see I have pasted it here and now I'm going to open this
29

30
00:03:01,590 --> 00:03:08,170
udemycsrf1.html so the attacker has sended a link to the victim, victim is going to interact
30

31
00:03:08,170 --> 00:03:16,420
with the link and perfect as you can see the password has been successfully changed for this user.
31

32
00:03:16,420 --> 00:03:26,890
So we understood into this video that we can achieve CSRF by changing the method that is from get to
32

33
00:03:26,890 --> 00:03:29,380
post or post to get.
33

34
00:03:29,380 --> 00:03:30,700
I hope you guys understood.
34

35
00:03:30,700 --> 00:03:31,150
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,440 --> 00:00:02,220
Hello everyone.
1

2
00:00:02,820 --> 00:00:07,390
So in this video we are going to see CSRF to account takeover.
2

3
00:00:07,830 --> 00:00:16,320
So we will do an account takeover by either changing the email I.D. or the password or both getting
3

4
00:00:16,320 --> 00:00:24,330
the complete access of the account and making the permanent lock out of the user is considered a vulnerability
4

5
00:00:24,480 --> 00:00:27,840
of extreme severity.
5

6
00:00:27,840 --> 00:00:34,560
So in this case your bug can go to P1 severity.
6

7
00:00:34,560 --> 00:00:39,770
So let's see how can we achieve CSRF to account takeover.
7

8
00:00:39,810 --> 00:00:47,640
So this is a practical time and let's see this as I can see I'm on to our application right now so I'm
8

9
00:00:47,640 --> 00:00:50,780
quickly going to sign up on this website first.
9

10
00:00:52,620 --> 00:00:58,830
So let me just type my email address hacker.udemy@gmail.com and let me try
10

11
00:00:58,830 --> 00:01:13,980
to hit on sign up.
11

12
00:01:14,600 --> 00:01:16,380
OK let me again try to sign up
12

13
00:01:20,820 --> 00:01:22,040
so welcome.
13

14
00:01:22,040 --> 00:01:24,050
We have sent an e-mail with logging details.
14

15
00:01:24,060 --> 00:01:24,890
Perfect.
15

16
00:01:24,930 --> 00:01:28,830
So I have created an account onto this Web site.
16

17
00:01:29,110 --> 00:01:32,050
And yes I have got an e-mail.
17

18
00:01:32,160 --> 00:01:33,880
We have registered successfully.
18

19
00:01:33,900 --> 00:01:36,410
You can change your password using this below link.
19

20
00:01:36,430 --> 00:01:43,480
Perfect.
20

21
00:01:43,820 --> 00:01:47,690
So let me just go here and you can see I'm already logged in into this account.
21

22
00:01:52,550 --> 00:01:54,620
Let me just go to my profile
22

23
00:02:01,420 --> 00:02:04,250
after going into the profile section.
23

24
00:02:04,480 --> 00:02:12,460
Let me try to navigate to the account details.
24

25
00:02:13,030 --> 00:02:13,870
Perfect.
25

26
00:02:13,870 --> 00:02:21,890
So as you can see when I have clicked on account details here are the account details as can be seen.
26

27
00:02:22,000 --> 00:02:23,160
My name is user.
27

28
00:02:23,230 --> 00:02:27,440
My email I.D. my temporary password application generated.
28

29
00:02:27,520 --> 00:02:33,420
So let me just try to put the name as victim and let me just submit this.
29

30
00:02:33,430 --> 00:02:34,010
Perfect.
30

31
00:02:34,930 --> 00:02:46,590
So now you have understood that this is the victim account so now what I'm going to do is I'm going
31

32
00:02:46,590 --> 00:02:49,380
to make attacker account also.
32

33
00:02:49,620 --> 00:02:54,380
So let me just go into the private window open the same URL
33

34
00:02:59,580 --> 00:03:04,970
and over here as you can see I'm into a new private window.
34

35
00:03:04,990 --> 00:03:07,580
Let me just quickly try to register.
35

36
00:03:07,660 --> 00:03:11,860
So now this is the attacker which is doing this.
36

37
00:03:11,880 --> 00:03:15,940
First was the victim which made an account.
37

38
00:03:15,940 --> 00:03:18,130
Now the attacker is making an account.
38

39
00:03:18,370 --> 00:03:22,210
So the attacker quickly sign ups on the website
39

40
00:03:25,360 --> 00:03:30,430
welcome perfect.
40

41
00:03:31,060 --> 00:03:32,670
Let me go to my profile
41

42
00:03:38,740 --> 00:03:39,240
now.
42

43
00:03:39,320 --> 00:03:41,810
Let's go to the account details.
43

44
00:03:41,810 --> 00:03:44,600
As you can see this is the attackers account.
44

45
00:03:44,600 --> 00:03:49,750
The attacker goes into the edit profile and saves his name as attacker.
45

46
00:03:49,760 --> 00:03:53,810
Let me just before saving captured the request into the Burpe suite
46

47
00:03:57,270 --> 00:04:03,010
so let's go on the application and hit submit.
47

48
00:04:03,400 --> 00:04:05,320
This is not a request.
48

49
00:04:05,320 --> 00:04:06,340
What I'm looking for.
49

50
00:04:06,340 --> 00:04:07,210
Perfect.
50

51
00:04:07,210 --> 00:04:14,320
So this is the post request which is going to the server for changing the profile details as you can
51

52
00:04:14,320 --> 00:04:17,290
see the user's first name is written as attacker.
52

53
00:04:17,770 --> 00:04:23,030
So the attacker comes to know the application is vulnerable to CSRF.
53

54
00:04:23,410 --> 00:04:30,730
And he is making and proof of concept through which he is going to change the details of the victim.
54

55
00:04:30,760 --> 00:04:38,520
So what it does is he goes in action quickly and the engagement tools generate a CSRF POC as you
55

56
00:04:38,630 --> 00:04:41,650
can see the POC has been generated.
56

57
00:04:41,650 --> 00:04:49,480
Let me just leave the previous request because our work is done and I'm going to just copy this copy
57

58
00:04:49,550 --> 00:04:56,140
html  and I'm going to open a notepad and I'm going to paste this over there
58

59
00:05:00,930 --> 00:05:04,540
so I'll go to a notepad editors and pasted it over there.
59

60
00:05:04,770 --> 00:05:05,250
Perfect
60

61
00:05:10,620 --> 00:05:15,390
as you can see this is attackers details into this POC.
61

62
00:05:15,620 --> 00:05:25,630
Let me just save it using this name that is azacsrf.html and yep.
62

63
00:05:25,800 --> 00:05:27,130
So the name is attacker.
63

64
00:05:27,360 --> 00:05:34,480
The name over here in the first name field is attackers.
64

65
00:05:35,240 --> 00:05:43,850
Let me just make the name to attacker CSRF takeover and let me take the email address has black
65

66
00:05:43,850 --> 00:05:51,480
ops dot Ruby one because generally sometimes what happens you cannot make or you cannot take two
66

67
00:05:51,560 --> 00:05:58,750
email addresses onto our website because the e-mails are already saved into the website's DB database.
67

68
00:05:58,940 --> 00:06:05,150
So maybe this application may give a error for taking the same email address over here with another account.
68

69
00:06:05,270 --> 00:06:07,520
So I have taken another e-mail address.
69

70
00:06:07,520 --> 00:06:13,790
Let me just try to open up this POC that we just now created into the victim's account.
70

71
00:06:13,790 --> 00:06:15,930
As you can see this is not the private window.
71

72
00:06:15,950 --> 00:06:18,320
This is the victim's account where he has logged in
72

73
00:06:21,400 --> 00:06:30,940
so the attacker sends this specifying a specific crafted link to the victim , victim interacts with this
73

74
00:06:30,940 --> 00:06:34,020
link and you can see the status is okay.
74

75
00:06:34,690 --> 00:06:43,270
Now as you can see the victim tries to reload his account and the details will be changed over here.
75

76
00:06:43,420 --> 00:06:44,320
So let's see.
76

77
00:06:44,350 --> 00:06:48,870
Perfect as you can see the name field has been changed.
77

78
00:06:48,880 --> 00:06:56,830
That is attacker CSRF takeover as well as the e-mail address has been changed which means that through
78

79
00:06:56,860 --> 00:07:06,430
the attackers request of edit profile the details of the victim got changed and this is a successful
79

80
00:07:06,670 --> 00:07:10,260
CSRF so I hope you guys understood.
80

81
00:07:10,270 --> 00:07:11,260
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,770 --> 00:00:04,270
Hello everyone.
1

2
00:00:04,270 --> 00:00:14,350
So in this video we are going to see how we can do CSRF and lead to account takeover so we can achieve
2

3
00:00:14,490 --> 00:00:20,750
account takeover by changing the e-mail address and the password of the victim.
3

4
00:00:21,160 --> 00:00:27,430
So getting the complete access of the account and the permanent lock out of the user is considered a
4

5
00:00:27,430 --> 00:00:35,940
very very dangerous vulnerability which we can achieve using CSRF so it's a practical time.
5

6
00:00:35,940 --> 00:00:41,240
And let's see how we can exploit this vulnerability.
6

7
00:00:41,340 --> 00:00:52,890
Show you live Web site on which I was able to exploit this vulnerability so quickly let's go to this Web
7

8
00:00:52,880 --> 00:01:00,060
site that is shop.moneris.com and I'm going to logging into this web site using my first account
8

9
00:01:00,420 --> 00:01:05,670
that is this the password to this account is hacked one two three.
9

10
00:01:06,480 --> 00:01:10,740
So I'm just going to type the password over here and I'm going to sign it into the application
10

11
00:01:14,220 --> 00:01:20,130
as you can see I am logged in into the application and this is the attackers account as you can see.
11

12
00:01:20,160 --> 00:01:21,080
Hello attacker
12

13
00:01:27,960 --> 00:01:28,680
Yep.
13

14
00:01:28,720 --> 00:01:39,460
So what I'm going to do is as you can see I am making a change password request.
14

15
00:01:39,460 --> 00:01:40,120
Yep.
15

16
00:01:40,390 --> 00:01:50,020
So now I will turn on the burpe suite and I'm going to capture the request into the burpe suite of changing the
16

17
00:01:50,020 --> 00:01:58,930
password as you can see this is I have captured into the burpe suite
17

18
00:01:58,930 --> 00:02:02,190
So this is the attacker who is trying to change his password.
18

19
00:02:02,200 --> 00:02:03,070
Why.
19

20
00:02:03,130 --> 00:02:06,580
Because he is going to generate CSRF POC.
20

21
00:02:06,580 --> 00:02:09,790
Based on that post request.
21

22
00:02:09,910 --> 00:02:10,870
Perfect.
22

23
00:02:10,870 --> 00:02:14,090
So now the password is hacked.
23

24
00:02:14,110 --> 00:02:15,790
One two three four five.
24

25
00:02:15,790 --> 00:02:16,930
As you can see.
25

26
00:02:16,930 --> 00:02:19,450
So I will just quickly go to engagement tools.
26

27
00:02:19,660 --> 00:02:28,660
Click on generate CSRF POC and you'll be able to see that I am having POC into the html format.
27

28
00:02:28,660 --> 00:02:34,350
So as you can see the password has been updated for the attackers account.
28

29
00:02:34,480 --> 00:02:35,860
Perfect.
29

30
00:02:35,860 --> 00:02:41,190
The attacker has also generated a CSRF POC
30

31
00:02:41,500 --> 00:02:44,440
Now let's just log out of the attackers account
31

32
00:02:51,610 --> 00:02:56,620
Let's paste the POC that we generated into a notepad file
32

33
00:03:02,240 --> 00:03:06,920
so this is the POC as you can see the e-mail address of the attackers.
33

34
00:03:07,010 --> 00:03:09,350
The password of the attacker over here.
34

35
00:03:09,650 --> 00:03:11,010
The name is attacker.
35

36
00:03:11,030 --> 00:03:12,820
The password perfect
36

37
00:03:15,580 --> 00:03:17,030
so now here.
37

38
00:03:17,290 --> 00:03:22,090
I am going to change that e-mail address.
38

39
00:03:22,090 --> 00:03:28,990
As you can see I have changed the e-mail address so it is vidhivaghela@gmail.com
39

40
00:03:28,980 --> 00:03:32,920
is the e-mail address that I'm going to use for this POC
40

41
00:03:41,920 --> 00:03:45,160
now on this website.
41

42
00:03:45,190 --> 00:03:47,110
The victim is going to logged in
42

43
00:03:54,320 --> 00:03:57,920
so this is attacker account and this is the victim's account.
43

44
00:04:00,710 --> 00:04:03,010
And the password for the victim is admin.
44

45
00:04:03,020 --> 00:04:03,760
One two three.
45

46
00:04:04,400 --> 00:04:08,510
So the victim is currently logging in into the application
46

47
00:04:12,200 --> 00:04:12,760
as you can see.
47

48
00:04:12,770 --> 00:04:14,840
Hello victim.
48

49
00:04:14,840 --> 00:04:15,380
Perfect.
49

50
00:04:15,440 --> 00:04:19,820
So now the victim has logged in into his account.
50

51
00:04:19,820 --> 00:04:28,550
What happens when a victim gets a link onto his account onto his e-mail.
51

52
00:04:28,550 --> 00:04:38,130
So let's quickly save the POC that we generated and let's give a name as CSRF POC dot
52

53
00:04:38,140 --> 00:04:38,490
html
53

54
00:04:41,060 --> 00:04:41,770
perfect.
54

55
00:04:41,810 --> 00:04:45,770
So yes let's open this with
55

56
00:04:54,290 --> 00:04:58,340
notepad and let's just save this first.
56

57
00:04:58,340 --> 00:04:59,570
Yes we have saved this
57

58
00:05:03,150 --> 00:05:04,580
now.
58

59
00:05:04,920 --> 00:05:14,410
We are going to open this with Firefox so the prerequisite is satisfied that the user is logged in.
59

60
00:05:14,430 --> 00:05:20,490
Which means the victim is already logged into his account and he gets a link which he is going to interact
60

61
00:05:20,490 --> 00:05:21,460
with.
61

62
00:05:21,480 --> 00:05:27,990
So he is going to interact with this link and as soon as he interacts with this link it can see data
62

63
00:05:28,050 --> 00:05:29,770
saved successfully.
63

64
00:05:29,790 --> 00:05:32,190
So this was the request of the attacker.
64

65
00:05:32,850 --> 00:05:40,470
And this request came to the victim and it updated data into the victim's account.
65

66
00:05:40,470 --> 00:05:43,290
So this is the victim's account.
66

67
00:05:43,290 --> 00:05:45,750
Victim unknowingly clicked that link.
67

68
00:05:45,750 --> 00:05:54,410
And now when he tries to refresh it you can see the name has changed to attacker also guys.
68

69
00:05:54,870 --> 00:06:01,410
If you notice there was also a password change into that POC.
69

70
00:06:01,410 --> 00:06:08,340
So let's see if the attacker is able to change the password of this victim account or not.
70

71
00:06:08,340 --> 00:06:15,480
If the attacker is able to change the password then this is an account takeover wherein the victim gets
71

72
00:06:15,600 --> 00:06:19,410
permanently logged out of his account.
72

73
00:06:19,410 --> 00:06:21,570
So the password that we kept
73

74
00:06:24,780 --> 00:06:29,800
so let's try with this password First admin123 and try to sign in.
74

75
00:06:30,040 --> 00:06:31,730
So you can see it is giving error.
75

76
00:06:32,080 --> 00:06:37,450
So this was the victim's account password and he's not able to log in with his own password.
76

77
00:06:37,450 --> 00:06:38,260
Why.
77

78
00:06:38,290 --> 00:06:42,920
Because the password has been updated and the password is.
78

79
00:06:43,020 --> 00:06:44,960
hacked12345.
79

80
00:06:45,310 --> 00:06:49,150
And let's try to see if we can log in with this password.
80

81
00:06:49,150 --> 00:06:54,750
And when you tried to log in with this password we get logging into the account.
81

82
00:06:54,760 --> 00:07:01,450
Perfect as I can see the name is changed to attacker and the password has changed to the attackers password
82

83
00:07:01,690 --> 00:07:04,900
that he wanted to keep for this account.
83

84
00:07:04,900 --> 00:07:14,980
So I hope you guys understood how we were able to do a CSRF attack onto this website in which the
84

85
00:07:14,980 --> 00:07:21,900
attacker was able to do a complete account takeover by changing the password of a victim or a user.
85

86
00:07:22,270 --> 00:07:26,560
Hence this vulnerability goes in P1 category.
86

87
00:07:26,560 --> 00:07:29,720
That is priority one and becomes very critical.
87

88
00:07:29,740 --> 00:07:35,870
So I hope you guys understood this attack in this video on this live web application.
88

89
00:07:35,890 --> 00:07:36,340
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,020 --> 00:00:07,190
In this video we are going to see that how we can change CSRF with exercise.
1

2
00:00:07,260 --> 00:00:15,360
So if you are unable to perform a CSRF onto any website due to some kind of production into place
2

3
00:00:16,100 --> 00:00:22,530
and lets say all our requests are getting invalidated or the user account is not getting updated with
3

4
00:00:22,530 --> 00:00:24,440
the attackers detail.
4

5
00:00:24,510 --> 00:00:28,840
So in this case we are not able to perform a valid CSRF attack.
5

6
00:00:29,220 --> 00:00:35,680
So how can we exploit CSRF with the help of XSS.
6

7
00:00:35,690 --> 00:00:44,030
So we will get the CSRF token plus the cookie with the help of XSS as we already saw into the XSS
7

8
00:00:44,040 --> 00:00:52,520
videos that we are able to get the cookie and if the token is passing into the cookie which mostly does.
8

9
00:00:52,530 --> 00:01:00,040
We are able to achieve it now utilizing that CSRF token that we got from the cookie.
9

10
00:01:00,150 --> 00:01:06,960
We can further make a POC in which we can use the new token that we have generated to attack the
10

11
00:01:06,960 --> 00:01:10,940
victim thus by chaining XSS.
11

12
00:01:10,950 --> 00:01:18,360
We can do a successful bypass for the CSRF protection and you can submit a bug such as CSRF as well
12

13
00:01:18,360 --> 00:01:20,670
XSS
13

14
00:01:20,880 --> 00:01:29,860
So fixing CSRF but no other vulnerabilities through which the token can be leaked is very very dangerous.
14

15
00:01:29,940 --> 00:01:35,310
So this is the point that we should understand that in any application if we are not able to achieve
15

16
00:01:35,310 --> 00:01:41,400
CSRF and if we are able to achieve any other vulnerability through which you are able to get the cookie
16

17
00:01:41,730 --> 00:01:50,410
or the token of CSRF if then you can change it and you can do a successful exploitation of CSRF vulnerability.
17

18
00:01:50,820 --> 00:01:58,050
Last words in this video if anyone got the cookie of the account then you cannot protect CSRF basically
18

19
00:01:58,380 --> 00:02:07,200
because your token will be leaked to that particular attacker and then attacker can misuse that specific
19

20
00:02:07,200 --> 00:02:11,190
token and can for the lead to CSRF attacks.
20

21
00:02:11,940 --> 00:02:18,660
So I hope you guys understood of one basic and simple example of chaining of any different attacks with
21

22
00:02:18,660 --> 00:02:21,690
CSRF and how you can achieve it.
22

23
00:02:21,780 --> 00:02:24,620
I hope you guys understood this approach and said add you.
23

24
00:02:24,900 --> 00:02:25,440
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,990 --> 00:00:01,920
Hello everyone.
1

2
00:00:02,250 --> 00:00:07,500
So in this video we are going to see what are the CSRF mitigations.
2

3
00:00:07,530 --> 00:00:15,990
So the first thing check for all the request that comes to a server if it is coming from a legitimate
3

4
00:00:15,990 --> 00:00:20,630
source or not if it is not coming from a legitimate source.
4

5
00:00:20,760 --> 00:00:23,220
Do not accept that request.
5

6
00:00:23,220 --> 00:00:29,700
So how can you verify that it is coming from a legitimate source are not always use a rolling or dynamic
6

7
00:00:29,700 --> 00:00:31,200
tokens.
7

8
00:00:31,200 --> 00:00:40,680
So let's say a user X has authenticated with the server after the successful authentication the server
8

9
00:00:40,830 --> 00:00:45,110
will generate a token let's say A1.
9

10
00:00:45,150 --> 00:00:52,170
Now the server will keep a copy of the token A1 and send a copy of that token to the client which
10

11
00:00:52,170 --> 00:00:59,730
is the user who is logged in now as the user makes any other request to the server whenever he clicks
11

12
00:00:59,760 --> 00:01:02,520
onto any application.
12

13
00:01:02,520 --> 00:01:09,630
That particular request will contain that copy of the token that is A1 the server will try to match
13

14
00:01:09,810 --> 00:01:17,820
that token with the copy of token it has saved with him onto the server if both the token matches then
14

15
00:01:17,820 --> 00:01:20,170
the server will say OK fine.
15

16
00:01:20,190 --> 00:01:22,140
This is a legitimate source.
16

17
00:01:22,470 --> 00:01:29,070
If both the tokens does not match then the server will discard that particular request and not take
17

18
00:01:29,160 --> 00:01:33,230
any decisions on that specific request.
18

19
00:01:33,240 --> 00:01:41,060
This is one of the best way to achieve complete protection against CSRF attack.
19

20
00:01:41,500 --> 00:01:52,230
Remember use of tokens is good but your tokens should always change per request not per session.
20

21
00:01:52,530 --> 00:02:02,370
I have seen a lot of developers putting CSRF tokens per session which can be exploited by any other
21

22
00:02:02,380 --> 00:02:03,990
vulnerabilities.
22

23
00:02:03,990 --> 00:02:08,940
So keeping tokens static is a bad practice.
23

24
00:02:09,120 --> 00:02:18,130
You should always keep dynamic tokens which should keep changing per request and the last one authenticate
24

25
00:02:18,130 --> 00:02:23,520
a request by some kind of protection which can be xsrf or csrf tokens.
25

26
00:02:23,520 --> 00:02:29,870
As I already said you should authenticate the request by some kind of strong xsrf or csrf
26

27
00:02:29,870 --> 00:02:31,470
a set of tokens.
27

28
00:02:31,470 --> 00:02:34,980
And one more thing that is important is
28

29
00:02:37,530 --> 00:02:46,140
use higher entropy for the tokens that you generate your tokens should not be easily guessable.
29

30
00:02:46,230 --> 00:02:52,230
For example if any application is trying to make a token which contains the first name the last name
30

31
00:02:52,740 --> 00:03:00,990
and the user I.D. is a very weak entropy token any attacker can guess that token and can try to make
31

32
00:03:01,140 --> 00:03:06,180
new tokens based on what he researchers.
32

33
00:03:06,330 --> 00:03:12,760
So basically entropy of a token should be very difficult to crack for.
33

34
00:03:12,780 --> 00:03:19,770
So these are the mitigations that one should know for protecting against CSRF attacks.
34

35
00:03:19,770 --> 00:03:23,110
So I hope you guys understood what are the mitigations for this attack.
35

36
00:03:24,210 --> 00:03:24,750
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,440 --> 00:00:02,190
Hello everyone.
1

2
00:00:02,700 --> 00:00:07,140
So in this video you're going to see some bonus tricks to find CSRF.
2

3
00:00:08,520 --> 00:00:11,860
So the first one is remove the tokens.
3

4
00:00:11,940 --> 00:00:19,620
Some applications validate based on if the token parameter is present in the cookie rather than the
4

5
00:00:19,620 --> 00:00:20,940
correct value.
5

6
00:00:20,970 --> 00:00:26,910
So if you just try to remove the token and submit the request then it is a win win for you.
6

7
00:00:27,480 --> 00:00:34,080
Do not try to miss those end points or request wherein you are able to see some kinds of CSRF
7

8
00:00:34,080 --> 00:00:36,710
or XSRF token protection.
8

9
00:00:36,720 --> 00:00:43,440
You just should try to remove the token value and try to resubmit the request and check if there are
9

10
00:00:43,440 --> 00:00:47,180
proper validations and check at the server side.
10

11
00:00:47,580 --> 00:00:55,830
If there are not then you have found a successful CSRF , 
second bypass to see a side of protection
11

12
00:00:56,190 --> 00:01:00,990
by identifying the of tokens are static and doesn't change.
12

13
00:01:00,990 --> 00:01:07,410
So if you found out that one application is taking the same token again and again or the application
13

14
00:01:07,410 --> 00:01:16,170
is generating the same tokens on every action that you perform or any time you log in into the account
14

15
00:01:16,770 --> 00:01:24,090
if the tokens remain same or static then you will come to know the application is vulnerable to CSRF
15

16
00:01:24,090 --> 00:01:25,750
attack
16

17
00:01:26,220 --> 00:01:27,620
Perfect.
17

18
00:01:27,660 --> 00:01:37,080
So keeping static tokens is very very dangerous so applications validate based on tokens  is present
18

19
00:01:37,110 --> 00:01:44,450
of same entropy or not change the CSRF token but keep the length and the entropy same.
19

20
00:01:44,460 --> 00:01:51,710
And so in this video we have learned about some of the bonus tricks that we can use to try to find our
20

21
00:01:51,730 --> 00:01:52,410
CSRF
21

22
00:01:55,750 --> 00:02:02,890
I hope you guys understood that how you can utilize this tips and tricks to do your research for finding
22

23
00:02:03,010 --> 00:02:06,550
out CSRF on to live website and find bugs.
23

24
00:02:06,550 --> 00:02:08,650
I hope you guys like this video.
24

25
00:02:08,740 --> 00:02:09,220
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,560 --> 00:00:03,340
Hello everyone.
1

2
00:00:03,850 --> 00:00:11,850
So in this video we are going to do a complete breakdown of CSRF attack report that were submitted on
2

3
00:00:11,860 --> 00:00:12,400
Hackerone.
3

4
00:00:13,750 --> 00:00:22,680
So in here we will see what other security researchers or hackers submit csrf attacks onto the website.
4

5
00:00:22,690 --> 00:00:27,910
So I have searched for CSRF attack hackerone as you can see over here.
5

6
00:00:28,000 --> 00:00:35,170
So let's go to the first report and see what we got account takeover using linked accounts due to lack
6

7
00:00:35,170 --> 00:00:36,970
of CSRF protection.
7

8
00:00:37,000 --> 00:00:45,820
So as you can see the researcher was able to find out a weakness which is basically CSRF and they
8

9
00:00:45,820 --> 00:00:52,300
were able to create a malicious link that is nothing just the CSRF POC that we always create as
9

10
00:00:52,330 --> 00:00:58,660
we have seen into our videos which have clicked by the victim would under certain conditions give attacker
10

11
00:00:58,660 --> 00:01:03,310
access to victims social lab account as we can see.
11

12
00:01:03,310 --> 00:01:08,900
This was submitted to Rockstar Games and the bounty that was awarded was 1000 dollars.
12

13
00:01:09,010 --> 00:01:17,320
Let's see another report at a CSRF to add item to victims got automatically submitted to Starbucks
13

14
00:01:17,680 --> 00:01:19,780
bounty awarded two fifty dollars.
14

15
00:01:19,810 --> 00:01:21,250
So let's see.
15

16
00:01:21,250 --> 00:01:23,800
First victim log into their Starbucks account.
16

17
00:01:23,800 --> 00:01:25,250
Perfect.
17

18
00:01:25,270 --> 00:01:28,470
This is the first prerequisite victim should be logged in.
18

19
00:01:28,480 --> 00:01:35,960
Attackers send a form or link as we already did attacker need to send a form or a link that is 
19

20
00:01:35,960 --> 00:01:41,770
CSRF POC if the victim click or the form or link an item would automatically add to the victim's
20

21
00:01:41,770 --> 00:01:47,950
cart if victim did not find this item he or she would pay for this item which can greatly influence
21

22
00:01:47,950 --> 00:01:49,360
your reputation.
22

23
00:01:49,360 --> 00:01:50,170
Okay fine.
23

24
00:01:50,170 --> 00:01:57,190
So as you can see this is the POC in which the attacker was able to add something into the victim's
24

25
00:01:57,190 --> 00:01:57,660
cart.
25

26
00:01:58,390 --> 00:02:04,240
As you can see two fifty dollars were awarded for this vulnerability which was submitted to Starbucks.
26

27
00:02:04,240 --> 00:02:09,940
Next let's see one more report CSRF logs the victim into the attackers account.
27

28
00:02:10,660 --> 00:02:18,080
So in this vulnerability it was reported to unicorn bounty hundred dollars.
28

29
00:02:18,190 --> 00:02:23,280
In this you can see that a CSRF POC which was submitted replace the e-mail and password is
29

30
00:02:23,280 --> 00:02:29,470
valid credentials send the script to victim to make them click and they will when they will click.
30

31
00:02:29,470 --> 00:02:34,900
There will be a sensitive action on the victim's account.
31

32
00:02:34,900 --> 00:02:36,800
Let's see another report.
32

33
00:02:37,240 --> 00:02:44,660
It is logging CSRF in analytic start more pop dot com which was reported ttwitter bounty awarded was
33

34
00:02:44,680 --> 00:02:46,390
280.
34

35
00:02:46,480 --> 00:02:52,530
As you can see there is no CSRF token validation while logging into which leads to a successful CSRF attack.
35

36
00:02:53,530 --> 00:03:00,760
So this is again csrflogin.html and the username password open with the browser and you can
36

37
00:03:00,760 --> 00:03:05,190
see there will be some kind of changes into the user's account.
37

38
00:03:05,260 --> 00:03:07,720
Let's see the next report.
38

39
00:03:07,720 --> 00:03:14,790
As you can see over here this report is again of CSRF submitted to harvest.
39

40
00:03:14,800 --> 00:03:18,970
As you can see I found CSRF while made new category.
40

41
00:03:18,970 --> 00:03:25,510
this is a POC we just put user site and the name of the category on this html form and
41

42
00:03:25,510 --> 00:03:27,970
the category will be created to this account.
42

43
00:03:27,970 --> 00:03:30,210
There is no token to validate the request.
43

44
00:03:30,400 --> 00:03:34,810
So the attacker can use this to make a CSRF attack happen on any victim's account.
44

45
00:03:35,470 --> 00:03:44,680
So in this report the attacker was able to add a new category into the victim's account which was a
45

46
00:03:44,680 --> 00:03:50,310
sensitive action and for this hundred dollars of bounty was rewarded.
46

47
00:03:50,320 --> 00:03:51,410
Let's see the next report.
47

48
00:03:52,690 --> 00:03:58,870
So this is CSRF add item to victims carts automatically again to Starbucks.
48

49
00:03:58,870 --> 00:04:05,470
So yeah attacker can add any items into the victim's account.
49

50
00:04:05,470 --> 00:04:09,290
This is the CSRF POC through which he was able to do it.
50

51
00:04:09,370 --> 00:04:14,170
Let's see the next report as we have seen the previous kind of report already.
51

52
00:04:14,950 --> 00:04:20,450
So this is CSRF vulnerability on API endpoint allows account takeover.
52

53
00:04:20,650 --> 00:04:26,770
So let's see the vulnerable end point allows an authenticated user to change the e-mail address associated
53

54
00:04:26,770 --> 00:04:28,650
with there account.
54

55
00:04:28,690 --> 00:04:31,480
If they have not confirmed the current address.
55

56
00:04:31,690 --> 00:04:39,260
So this means basically the attacker was able to send the CSRF POC which contained the confirm
56

57
00:04:39,390 --> 00:04:39,970
e-mail.
57

58
00:04:40,060 --> 00:04:47,770
As you can see the request is going to sign up confirm e-mail and you can see this is the attackers e-mail
58

59
00:04:47,770 --> 00:04:48,640
address.
59

60
00:04:48,640 --> 00:04:54,130
So basically attackers e-mail address will be confirmed into the victim's account.
60

61
00:04:54,160 --> 00:04:54,670
Perfect.
61

62
00:04:55,450 --> 00:05:04,860
So this is common kind of account takeover in which an attacker can exploit the vulnerability to take
62

63
00:05:04,860 --> 00:05:07,460
over accounts by associating them with an address.
63

64
00:05:07,460 --> 00:05:14,990
controlled by the attacker then performing a password reset to take a successful account.
64

65
00:05:15,090 --> 00:05:22,950
A very good report submitted to Khan Academy by performing a successful account takeover.
65

66
00:05:23,000 --> 00:05:25,610
Let's see the next report critical.
66

67
00:05:25,620 --> 00:05:35,270
Full account takeover using CSRF perfect bounty awarded eight fifty two dollars reported to Badu.
67

68
00:05:35,570 --> 00:05:38,980
Again this report we have already seen.
68

69
00:05:39,050 --> 00:05:46,940
This is the POC in which the attacker is able to verify the email and he is able to add his email address
69

70
00:05:47,870 --> 00:05:51,440
into this user's account.
70

71
00:05:51,670 --> 00:05:52,740
Let's see the next report
71

72
00:05:55,580 --> 00:06:05,340
CSRF in the report are emoticon features and you can see bounty awarded to 250 dollars program chaturbate.
72

73
00:06:05,660 --> 00:06:11,660
Users can report emojis on bases of expressions but the request made to this particular end point was
73

74
00:06:11,660 --> 00:06:17,910
a get request which was not protected by CSRF header as you have already seen and get base CSRF
74

75
00:06:18,390 --> 00:06:18,940
and.
75

76
00:06:19,220 --> 00:06:20,880
How can we change that.
76

77
00:06:21,230 --> 00:06:28,140
http method that is from get to post post to get to achieve CSRF this is a kind.
77

78
00:06:28,160 --> 00:06:34,230
Same report that we already seen into our video lectures so fine.
78

79
00:06:34,250 --> 00:06:36,440
Let's see the next report.
79

80
00:06:36,440 --> 00:06:44,190
So this is CSRF in Add restaurant picture function reported as zomato bouty awarded  fifty dollars.
80

81
00:06:44,240 --> 00:06:53,570
So in this report the attacker is able to update the restaurant picture that he wants into any victim's
81

82
00:06:53,570 --> 00:06:57,020
account because that end point was not secure.
82

83
00:06:58,040 --> 00:07:07,200
So again a CSRF the next report CSRF for adding users to New Relic.
83

84
00:07:07,250 --> 00:07:15,650
So in this there was no check for authenticity token and the attacker was able to add new accounts to
84

85
00:07:15,650 --> 00:07:22,550
the user account the new accounts are basically some kinds of new users which the application allowed
85

86
00:07:22,550 --> 00:07:28,190
to add, perfect to the next report.
86

87
00:07:28,380 --> 00:07:32,940
So this report is kind of interesting that is reflected  XSS plus CSRF
87

88
00:07:32,970 --> 00:07:39,960
On secure.lahitapiola.fi OK.
88

89
00:07:39,970 --> 00:07:47,200
So this was the report that was submitted and the bounty awarded was 750 dollars within the
89

90
00:07:47,200 --> 00:07:49,060
researchers found out.
90

91
00:07:49,060 --> 00:07:55,960
End Point which was vulnerable to reflected XSS vulnerability and also the same functionality
91

92
00:07:56,350 --> 00:07:56,860
lagged.
92

93
00:07:56,920 --> 00:07:59,010
Any kind of CSRF protection.
93

94
00:07:59,020 --> 00:08:06,540
So basically we tried to find out two vulnerabilities on the same endpoint as you can see over here
94

95
00:08:07,180 --> 00:08:17,190
if he has put the perfect as you have put the payload  over here which is closed by no script script a document
95

96
00:08:17,200 --> 00:08:17,890
or domain.
96

97
00:08:17,890 --> 00:08:20,150
This is the XSS payload.
97

98
00:08:20,410 --> 00:08:22,970
And this is the POC for CSRF.
98

99
00:08:22,990 --> 00:08:25,370
As you can see you were here.
99

100
00:08:25,420 --> 00:08:29,680
Nice report and a nice bounty for that.
100

101
00:08:29,740 --> 00:08:35,280
Let's see another report CSRF trial 14 days express subscription.
101

102
00:08:35,350 --> 00:08:39,720
So this was submitted to instacart bounty awarded three hundred dollars.
102

103
00:08:41,050 --> 00:08:46,380
So in this vulnerability report the user who was CSRF.
103

104
00:08:46,630 --> 00:08:52,750
So the victim may believe that he is using the free version consuming trial time and missing the Express
104

105
00:08:52,750 --> 00:08:54,000
features.
105

106
00:08:54,040 --> 00:09:01,510
So when I read this report I came to a conclusion wherein the attacker was able to make the user take
106

107
00:09:01,810 --> 00:09:10,200
a trial from a trial vision to a premium version for 14 days so a user will be using the account of
107

108
00:09:10,210 --> 00:09:12,370
instacart for 14 days.
108

109
00:09:12,490 --> 00:09:18,280
But he will think that he is still using the normal account and he may miss some important features.
109

110
00:09:19,180 --> 00:09:29,380
So this was again a good report in which the attacker was able to make the user sign up for the extended
110

111
00:09:29,380 --> 00:09:30,490
features.
111

112
00:09:30,480 --> 00:09:34,520
And yeah it was a good report.
112

113
00:09:35,080 --> 00:09:43,900
Next as you can see CSRF Attack on m.badoo.com deleting account and erasing important context
113

114
00:09:44,830 --> 00:09:46,000
submitted to badu.
114

115
00:09:46,090 --> 00:09:48,460
Bounty awarded to two eighty dollars.
115

116
00:09:48,460 --> 00:09:57,860
As we understand from this report that the attacker was able to make and delete account CSRF and erase
116

117
00:09:57,890 --> 00:10:06,580
contact CSRF POC through which if he's sended this particular request or that html POC to the
117

118
00:10:06,580 --> 00:10:13,240
victim if the victim interacted with it or clicked it he could have deleted his account or erased all
118

119
00:10:13,240 --> 00:10:14,020
his contacts.
119

120
00:10:14,440 --> 00:10:21,580
So again an interesting report as we have already covered these types of scenarios into a video lectures.
120

121
00:10:21,580 --> 00:10:29,650
So it would be a easy task for you guys to find and hunt for a similar kind of vulnerabilities.
121

122
00:10:29,770 --> 00:10:34,410
Let's see the last report account removing using CSRF attack.
122

123
00:10:34,450 --> 00:10:42,190
So in this POC it was first reported to wepay and bounty awarded was 350 dollars.
123

124
00:10:42,190 --> 00:10:50,020
So in this POC this security researcher was able to remove any accounts as you can see this end
124

125
00:10:50,020 --> 00:10:59,260
point is www.wepay.com/settings/delete and we sended this particular POC to end user
125

126
00:10:59,650 --> 00:11:03,180
and the user interacted his account would get delete.
126

127
00:11:03,210 --> 00:11:03,880
Why.
127

128
00:11:04,000 --> 00:11:05,830
Because there was no confirmation.
128

129
00:11:05,980 --> 00:11:09,640
Second there was no proper CSRF protection.
129

130
00:11:09,670 --> 00:11:17,950
So again a good report with a lot of severity as the user's account is getting deleted.
130

131
00:11:17,950 --> 00:11:25,120
So I hope you guys understood by this breakdown of a lot of reports which will help you in trying to
131

132
00:11:25,120 --> 00:11:34,810
hunt for these kinds of vulnerabilities when you can replicate the same scenarios also utilize the
132

133
00:11:34,810 --> 00:11:44,590
tips tricks that we have used in the videos and try to find critical bugs and CSRF onto live websites
133

134
00:11:46,570 --> 00:11:56,540
so that's what are the lessons learned first thing always test CSRF on sensitive actions as we
134

135
00:11:56,540 --> 00:11:58,710
saw in many of the reports.
135

136
00:11:58,820 --> 00:12:03,800
No security researcher misses any sensitive action.
136

137
00:12:03,800 --> 00:12:14,180
So you do not miss any sensitive action to look for tokens that can be CSRF XSRF etc in sensitive
137

138
00:12:14,180 --> 00:12:15,350
fields.
138

139
00:12:15,350 --> 00:12:23,270
So if you were unable to find that then you may try for CSRF even if you find
139

140
00:12:23,270 --> 00:12:31,460
that check for the entropy trying to remove the value and try submitting from post to get or get to
140

141
00:12:31,460 --> 00:12:32,060
post.
141

142
00:12:32,090 --> 00:12:41,540
We have seen the scenarios already which will lead to a successful CSRF attack next try to change email
142

143
00:12:41,540 --> 00:12:46,520
and password to make an account takeover which will make it a P1 level bug.
143

144
00:12:46,520 --> 00:12:54,890
High security means high rewards and the last one always strive CSRF everywhere because it is an easy
144

145
00:12:54,890 --> 00:13:00,710
WIN as we understood from the breakdown of many hacker one reports.
145

146
00:13:00,860 --> 00:13:11,000
So I hope you guys understood this and this video helps you guys in finding the approach when you can
146

147
00:13:11,000 --> 00:13:15,810
find a lot of CSRF vulnerabilities onto the live website.
147

148
00:13:15,820 --> 00:13:16,370
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,590 --> 00:00:04,230
Hello everyone.
1

2
00:00:04,240 --> 00:00:13,120
So in this video we are going to see some interview questions and approach for CSRF so if you're planning
2

3
00:00:13,180 --> 00:00:20,410
to go out and apply for a job for cyber security consultant or an analyst  here are some important questions
3

4
00:00:20,440 --> 00:00:22,270
that you should not miss.
4

5
00:00:22,300 --> 00:00:25,860
And these are some favorite questions of any interviewer.
5

6
00:00:26,470 --> 00:00:32,610
So the first question is what is CSRF what is so unique about this bug.
6

7
00:00:32,650 --> 00:00:34,020
By asking this question.
7

8
00:00:34,090 --> 00:00:43,060
The interviewer tends to ask you that are you aware about CSRF and why is this bug different from
8

9
00:00:43,150 --> 00:00:45,640
other types of bugs in all owasp.
9

10
00:00:46,900 --> 00:00:52,510
So this for this question you need to be specific and you need to answer that.
10

11
00:00:52,870 --> 00:00:53,710
What is CSRF.
11

12
00:00:53,710 --> 00:01:00,160
First of all so CSRF stands for cross-site request forgery and this is the vulnerability which was in
12

13
00:01:00,160 --> 00:01:03,140
owasp 2013.
13

14
00:01:03,330 --> 00:01:09,900
What is unique about this book through this vulnerability  any attacker can perform sensitive actions
14

15
00:01:10,170 --> 00:01:12,360
into a user's account.
15

16
00:01:12,540 --> 00:01:22,680
Also the attacker can do an account takeover into the user's account attacker can also do some funds
16

17
00:01:23,160 --> 00:01:29,690
if that is a banking application or tried to do any kind of sensitive action.
17

18
00:01:29,820 --> 00:01:36,170
That's why this makes this vulnerability unique ,next.
18

19
00:01:36,180 --> 00:01:44,970
What is the difference between XSS and CSRF as both the both vulnerability start with cross
19

20
00:01:44,970 --> 00:01:53,160
site but cross-site scripting and cross site requests forgery both are different vulnerabilities as
20

21
00:01:53,160 --> 00:01:58,570
you already know XSS is all about injecting scripts.
21

22
00:01:58,920 --> 00:02:05,380
Basically Java script into our application and getting a desired output for that script.
22

23
00:02:05,400 --> 00:02:13,980
but CSRF stands for cross site requests Forgery is a different bug as we already know and we
23

24
00:02:13,980 --> 00:02:23,280
have seen into the video series that CSRF is a vulnerability in which the attacker is going to send some
24

25
00:02:23,280 --> 00:02:31,050
kind of request or a form to the victim and the victim is going to interact with that specific form
25

26
00:02:31,140 --> 00:02:41,210
or request and if there is no proper protection then that attacker can make the victim do desired results.
26

27
00:02:42,970 --> 00:02:46,160
Which can also lead to an account takeover.
27

28
00:02:46,510 --> 00:02:54,530
This is the basic difference between both  next what are the requirements to achieve this.
28

29
00:02:54,820 --> 00:02:56,770
By asking this question.
29

30
00:02:56,770 --> 00:02:58,630
The interviewer wants to know that.
30

31
00:02:58,630 --> 00:03:05,860
Are you fully aware about how a CSRF will happen and how will you test it into a penetration testing
31

32
00:03:05,860 --> 00:03:07,480
environment.
32

33
00:03:07,510 --> 00:03:11,680
So for this vulnerability  there are three requirements.
33

34
00:03:11,680 --> 00:03:15,340
As we already discussed into our videos.
34

35
00:03:15,340 --> 00:03:23,110
The first requirement is the victim or the user should be logged in into the application.
35

36
00:03:23,110 --> 00:03:31,480
The second requirement is the user or the victim should interact with the link or form that the attacker
36

37
00:03:31,480 --> 00:03:33,430
has sent.
37

38
00:03:33,440 --> 00:03:40,630
And the last requirement is the application should be vulnerable to CSRF itself ,next.
38

39
00:03:41,200 --> 00:03:42,240
What isthis you see.
39

40
00:03:42,280 --> 00:03:43,900
the severity of CSRF.
40

41
00:03:43,890 --> 00:03:55,210
If so this question varies as per the answers as the severity can escalate to even p1.
41

42
00:03:55,330 --> 00:03:57,100
That is a critical bug.
42

43
00:03:57,460 --> 00:04:03,730
If the attacker is able to change some of the details which are not sensitive then this bug may lead
43

44
00:04:04,240 --> 00:04:06,670
to a P2 or a P3.
44

45
00:04:07,480 --> 00:04:15,430
If the attacker is able to change a very sensitive details or do some kind of fund transfer or change
45

46
00:04:15,430 --> 00:04:24,910
the email id or password into a complete account takeover then this bug may lead to a P1 attack.
46

47
00:04:24,910 --> 00:04:31,060
Next why CSRF on logout and logging are not much severe
47

48
00:04:34,460 --> 00:04:37,840
by this question the interviewer wants to know that.
48

49
00:04:38,030 --> 00:04:42,610
Are you aware about CSRF on logging In or Logging out.
49

50
00:04:43,310 --> 00:04:50,420
So basically if you are able to make any use log out of his account is not considered a valid security
50

51
00:04:50,480 --> 00:04:59,540
issue or a very sensitive or issue which contains some kind of impact.
51

52
00:04:59,600 --> 00:05:04,780
So CSRF for logging on log out are not considered to be very sensitive.
52

53
00:05:07,960 --> 00:05:11,170
So the last question is what is the fix of this vulnerability.
53

54
00:05:11,320 --> 00:05:18,450
As we have already seen the mitigation video from that you can take the reference for this question.
54

55
00:05:18,910 --> 00:05:28,330
To sum up the fix could be a rolling tokens or dynamic tokens onto the web application within the server
55

56
00:05:28,720 --> 00:05:37,300
checks for each request and the server generates new token for each request or any action that is performed
56

57
00:05:37,720 --> 00:05:39,050
by the user.
57

58
00:05:40,960 --> 00:05:49,600
As soon as the user performs any specific action the server should invalidate the old token.
58

59
00:05:49,630 --> 00:05:54,140
Thus by making the application safe to CSRF attacks.
59

60
00:05:54,370 --> 00:06:02,470
So I hope you guys understood this and this video may help you in tackling some of the important questions
60

61
00:06:02,560 --> 00:06:05,830
and favorite questions of interviewers.
61

62
00:06:05,830 --> 00:06:06,310
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,210 --> 00:00:01,940
Hello, everyone.
1

2
00:00:02,950 --> 00:00:10,660
So in this video, we are going to do a CSRF POC generator, so what is this actually?
2

3
00:00:11,500 --> 00:00:19,060
So we are going to use a tool through which we can craft CSRF based POC
3

4
00:00:20,890 --> 00:00:29,890
So this can be also considered as an alternative to the Burp Suite CSRF POC generator
4

5
00:00:30,860 --> 00:00:39,080
For those who do not have a provision of Burp Suite Pro, there is a premium feature of generating
5

6
00:00:39,080 --> 00:00:41,990
a CSRF POC directly from Burp Suite
6

7
00:00:42,060 --> 00:00:50,600
You can also use this particular open source tool to generate the CSRF POC and further conduct the
7

8
00:00:50,600 --> 00:00:51,080
attack.
8

9
00:00:52,460 --> 00:00:55,210
So how this actually works is pretty simple.
9

10
00:00:55,940 --> 00:01:04,400
So it creates your HTML file that is basically POC for any particular form of any request that you
10

11
00:01:04,400 --> 00:01:05,180
want to capture.
11

12
00:01:07,100 --> 00:01:13,850
So it is the practical time and let's see how you can utilize this tool to create a CSRF POC 
12

13
00:01:13,850 --> 00:01:16,550
and further conduct the attack.
13

14
00:01:20,740 --> 00:01:27,820
So as you can see over here, this is the CSRF POC generator, which we are going to use, it is very
14

15
00:01:27,820 --> 00:01:32,180
simple and it's a very, very lightweight on your computer.
15

16
00:01:32,800 --> 00:01:37,060
So what do you have to do is quickly clone this GitHub repository?
16

17
00:01:37,060 --> 00:01:40,330
So I'm just going to clone this into my computer.
17

18
00:01:44,860 --> 00:01:53,300
Yes, so I'm just going to try to git clone and I'm going to clone this, so in case it gives you a
18

19
00:01:53,300 --> 00:01:57,160
error of permission denied, then you have to give permissions.
19

20
00:02:01,370 --> 00:02:08,960
Yes, and now I'm going to clone this, I have already cloned it, but I'm showing it again how to clone
20

21
00:02:08,960 --> 00:02:09,150
it.
21

22
00:02:09,650 --> 00:02:13,520
So, as you can see, this has successfully cloned.
22

23
00:02:13,520 --> 00:02:17,500
So let me do a list and you can see the folder.
23

24
00:02:17,510 --> 00:02:24,250
Let me just go inside that particular folder that we have just downloaded and let me list again and
24

25
00:02:24,260 --> 00:02:24,500
again.
25

26
00:02:24,500 --> 00:02:26,350
See, there are multiple files over here.
26

27
00:02:27,440 --> 00:02:32,930
The most important file for us is index.HTML.
27

28
00:02:33,320 --> 00:02:39,740
Through this we are going to utilize to make our CSRF POC how to do that.
28

29
00:02:40,550 --> 00:02:44,510
First, you need to create a HTTP server for that.
29

30
00:02:44,520 --> 00:02:48,910
You can use Python in case you do not have Python into your computer.
30

31
00:02:49,220 --> 00:02:57,170
You can simply go to Python dot org and download Python for your computer once you have Python for your
31

32
00:02:57,170 --> 00:02:57,690
computer.
32

33
00:02:58,370 --> 00:03:01,460
You need to install it after you have installed.
33

34
00:03:01,460 --> 00:03:10,490
You can simply run the command python -m SimpleHTTPServer and any port number that you
34

35
00:03:10,490 --> 00:03:11,120
want to give.
35

36
00:03:11,930 --> 00:03:15,600
So this way a simple server will be started for your computer.
36

37
00:03:16,520 --> 00:03:18,740
This command is for Python two point seven.
37

38
00:03:19,520 --> 00:03:27,440
If you have installed Python three point X or any version, which is about three linear command changes
38

39
00:03:27,440 --> 00:03:37,850
to http.server, then this is the particular module that you need to run in case of Python three.
39

40
00:03:38,120 --> 00:03:45,380
But here I am running it using Python two, so I'm going to type simple SimpleHTTPServer
40

41
00:03:45,870 --> 00:03:53,000
Remember, you need to type it the same way that I have written over here S should be capital HTTP should
41

42
00:03:53,000 --> 00:03:55,130
be capital and S should be capital.
42

43
00:03:55,130 --> 00:04:01,490
If you give it the other way or you give all of them lowercase, then it will say the module is not
43

44
00:04:01,490 --> 00:04:04,100
recognized or there is an error into the command.
44

45
00:04:05,360 --> 00:04:05,740
All right.
45

46
00:04:05,760 --> 00:04:11,040
So I'm just going to hit Enter before hitting in let's see the IP address of our computer.
46

47
00:04:11,060 --> 00:04:12,890
So for that, I'm going to type the command.
47

48
00:04:12,890 --> 00:04:16,700
I ifconfig and let's see the IP address.
48

49
00:04:18,220 --> 00:04:24,400
You can see my IP address is this, which is 192 168 zero one zero three.
49

50
00:04:24,560 --> 00:04:24,980
All right.
50

51
00:04:24,990 --> 00:04:27,890
Let me clear the screen now.
51

52
00:04:29,680 --> 00:04:32,080
I'm going to run the Python server quickly.
52

53
00:04:38,050 --> 00:04:45,130
On any port number that you want, so I'm using the port number, which is 8080, and I will hit enter once you
53

54
00:04:45,130 --> 00:04:53,290
see this message, which is serving HTTP on zero zero zero zero on Port 8080, which means you have successfully
54

55
00:04:53,290 --> 00:04:56,240
able to start your python server
55

56
00:04:56,980 --> 00:04:57,550
All right.
56

57
00:04:57,760 --> 00:04:59,500
Now, let's test this.
57

58
00:04:59,500 --> 00:05:07,150
If it is working fine, go to your browser, type in your IP address and the port number on which you
58

59
00:05:07,150 --> 00:05:09,360
have started your Python server and hit enter.
59

60
00:05:10,870 --> 00:05:18,250
If you are able to see this particular screen or this particular page, that means you have successfully
60

61
00:05:18,250 --> 00:05:24,520
started your Python server and it will see is out of CSRF POC generator has successfully initialized.
61

62
00:05:25,450 --> 00:05:30,900
So we are on to the perfect track and we are able to start our CSRF POC Generator.
62

63
00:05:32,030 --> 00:05:32,510
Perfect.
63

64
00:05:32,810 --> 00:05:39,710
Now it's time to test this, so we are going to see how we can test our CSRF POC generator
64

65
00:05:39,710 --> 00:05:41,190
and how it actually works.
65

66
00:05:42,290 --> 00:05:48,980
So for this, I'm going to test this on a DVWA web application, which is damn vulnerable Web application.
66

67
00:05:50,420 --> 00:05:57,290
What you can do is you can simply log on to me and you can see the dvwa application  here.
67

68
00:05:58,130 --> 00:06:06,230
So the interesting thing about me is it gives you sandbox applications, which means it hosts the application
68

69
00:06:06,230 --> 00:06:06,640
for you.
69

70
00:06:07,070 --> 00:06:08,720
You can simply test it over there.
70

71
00:06:08,780 --> 00:06:12,860
You do not need to download the whole DVWA into your computer.
71

72
00:06:12,870 --> 00:06:15,280
You do not need to host it onto your computer.
72

73
00:06:15,980 --> 00:06:21,230
You can simply host it over here and it's done for you.
73

74
00:06:21,230 --> 00:06:22,370
It's free of cost.
74

75
00:06:22,490 --> 00:06:25,700
You can simply utilize Hack.me me for your practice.
75

76
00:06:27,190 --> 00:06:31,810
All right, so once you're on Hack.me, you need to create account first, so I have created my account
76

77
00:06:31,810 --> 00:06:35,020
and I have logged into my account account.
77

78
00:06:35,020 --> 00:06:38,100
Creation is very simple and you will be able to do that.
78

79
00:06:38,890 --> 00:06:42,420
Now, you can see start now and get you a dedicated sandbox.
79

80
00:06:42,430 --> 00:06:48,730
So I just need to click on start and it will give me a sandbox involvement, which is basically my 
80

81
00:06:48,730 --> 00:06:52,370
DVWA Web application once this is started.
81

82
00:06:52,390 --> 00:06:56,190
Remember, guys, your default login is admin password.
82

83
00:06:56,200 --> 00:07:00,320
Remember these credentials and you can see my sandbox is ready.
83

84
00:07:00,340 --> 00:07:07,390
I just need to click on I agree and we will be redirected to our digital application, as you can see
84

85
00:07:07,390 --> 00:07:07,920
over here.
85

86
00:07:08,650 --> 00:07:12,580
So my credentials are admin and my password is password.
86

87
00:07:13,180 --> 00:07:15,910
Let me just log in and check if I get logged in.
87

88
00:07:16,030 --> 00:07:16,560
Perfect.
88

89
00:07:17,140 --> 00:07:22,710
So now we are able to start our DVWA web application and it looks something like this.
89

90
00:07:24,040 --> 00:07:26,100
So DVWA stands for damn
90

91
00:07:26,110 --> 00:07:32,050
Vulnerable Web application, which is an exact simulation of how a vulnerable Web application may look
91

92
00:07:32,050 --> 00:07:32,380
like.
92

93
00:07:33,010 --> 00:07:37,000
So you can practice all the vulnerabilities onto this particular Web application.
93

94
00:07:37,960 --> 00:07:45,100
So I'm going to move on to the CSR section on the left hand side and we are going to try SRF before
94

95
00:07:45,100 --> 00:07:45,860
trying CSRF.
95

96
00:07:45,860 --> 00:07:51,940
If I'm just going to go to the DVWA security and I'm going to lower the security for this particular video
96

97
00:07:52,390 --> 00:07:55,900
in which I'm going to show you how we can do this here sort of attack.
97

98
00:07:56,860 --> 00:08:02,410
Let's go back to see CSRF and you will be able to see change your admin password.
98

99
00:08:03,070 --> 00:08:08,480
So if I type here my new password, my password will get changed for this particular account.
99

100
00:08:09,460 --> 00:08:19,090
Now let me quickly start Burp Suite, so I'm starting Burp Suite Community Edition here and install it,
100

101
00:08:19,090 --> 00:08:21,670
use it at three.
101

102
00:08:22,060 --> 00:08:25,210
You do not need to pay anything for Burp Suite community additions.
102

103
00:08:26,020 --> 00:08:29,200
Let me quickly configure my Burp Suite community addition.
103

104
00:08:30,280 --> 00:08:33,800
So as a its 8080 port is busy we are going to choose other. port
104

105
00:08:33,820 --> 00:08:42,370
But let me start the servers and let me go back to my browser as well as I will configure my browser and
105

106
00:08:42,370 --> 00:08:46,980
we are going to use eight zero eight one when the same pool that we have selected in Burp Suite
106

107
00:08:48,730 --> 00:08:49,240
All right.
107

108
00:08:50,410 --> 00:08:57,790
Now I'm going to capture the request in my burp, so I just turn it on, go back here and I'm going
108

109
00:08:57,790 --> 00:09:03,880
to type the password, as rohit again rohit
109

110
00:09:04,510 --> 00:09:05,860
I'll go back to burp
110

111
00:09:07,170 --> 00:09:13,050
OK, so this is a keep alive request, I do not want this request, so I'll just forward it or I can
111

112
00:09:13,050 --> 00:09:13,980
even drop that.
112

113
00:09:15,030 --> 00:09:17,880
All right, so now I'm going to click on Change.
113

114
00:09:18,030 --> 00:09:24,540
I'll go back to my Burp Suite and you can see  a request over here a request is going, but in the password can be seen,
114

115
00:09:24,540 --> 00:09:26,490
as you can see, rohit and rohit
115

116
00:09:27,570 --> 00:09:28,110
All right.
116

117
00:09:28,590 --> 00:09:30,060
Now, what you can do is right.
117

118
00:09:30,060 --> 00:09:32,670
Click and send this request to repeater
118

119
00:09:33,660 --> 00:09:37,160
Once you have sent this to repeater here
119

120
00:09:37,170 --> 00:09:43,050
I have got my request now as we do not have the feature of.
120

121
00:09:43,050 --> 00:09:43,290
Right.
121

122
00:09:43,290 --> 00:09:50,870
Clicking and making a generator of you see as it is disabled right now for the community edition.
122

123
00:09:51,600 --> 00:09:55,700
What we are going to do is we are going to copy the whole request from here.
123

124
00:09:56,310 --> 00:09:59,100
So I'm just going to copy this now.
124

125
00:09:59,100 --> 00:10:03,280
Go to our POC generator and we are going to paste it over here.
125

126
00:10:04,950 --> 00:10:09,030
Now you have to select HTTP or HTTPS
126

127
00:10:09,420 --> 00:10:14,430
So the Web application we are running on, which is this is running on HTTP.
127

128
00:10:14,430 --> 00:10:21,240
As we can see from here, there is no secure padlock, which means this is running on HTTP, which we can also
128

129
00:10:21,240 --> 00:10:25,340
see from Burp Suite from here it is running on empty HTTP
129

130
00:10:26,640 --> 00:10:30,300
So you have to select HTTP and click on generate POC form.
130

131
00:10:31,110 --> 00:10:37,500
Once you click this our poc will simply be created in just a couple of milliseconds and you can
131

132
00:10:37,500 --> 00:10:40,140
see my see CSRF POC is ready.
132

133
00:10:41,400 --> 00:10:45,450
Now let me go to Burp and let me release this particular request.
133

134
00:10:45,850 --> 00:10:52,500
Remember if I will forward my password will get changed to rohit and I have forwarded this.
134

135
00:10:53,400 --> 00:10:55,730
Let's go back here and you can see password changed.
135

136
00:10:55,740 --> 00:10:57,750
So now my password is a rohit.
136

137
00:10:58,380 --> 00:11:05,460
All right, let's go back to the CSRF POC and I'm going to change this rule to shifa
137

138
00:11:06,360 --> 00:11:12,300
And over here, I'm going to change this to shifa as well, which is password new and password confirm.
138

139
00:11:13,200 --> 00:11:17,010
So now my csrf poc has been successfully generated.
139

140
00:11:17,850 --> 00:11:25,420
I can copy it, make empty file and save it in that, or there's a direct option of save as html
140

141
00:11:25,450 --> 00:11:28,710
I'm going to click on that and you can see I'm able to download this.
141

142
00:11:29,730 --> 00:11:33,540
So let me just quickly download this and let me open this.
142

143
00:11:35,840 --> 00:11:40,160
So I'm going to open this with my Firefox browser.
143

144
00:11:44,350 --> 00:11:51,160
And you can see over hear I'm going to click on Submit and I'm going to wait and you can see password
144

145
00:11:51,160 --> 00:11:56,520
changed because I see us out of poc contain the new password and the password was Shifa
145

146
00:11:56,530 --> 00:12:00,920
Let's confirm if the password has been changed for this particular application or not.
146

147
00:12:01,300 --> 00:12:03,610
So the username was admin the password.
147

148
00:12:03,610 --> 00:12:05,870
Should be rohit.
148

149
00:12:06,520 --> 00:12:15,130
Let me just write it over here and pasted over here and login and it would give me an error, as you
149

150
00:12:15,130 --> 00:12:20,530
can see here, because the attacker is able to change the password and now the password is changed to
150

151
00:12:20,800 --> 00:12:21,360
Shifa.
151

152
00:12:21,700 --> 00:12:25,740
So let me just copy this pasted over here and click on login.
152

153
00:12:26,950 --> 00:12:34,690
So once I have given the right password that is shifa, I'm able to login into the particular application.
153

154
00:12:36,760 --> 00:12:44,020
So I hope this is clear now how we are able to create a csrf pox using this sort of beauty generator
154

155
00:12:44,380 --> 00:12:52,690
in absence of having a Burp Suite professional edition, you can utilize this opensource application through which
155

156
00:12:52,690 --> 00:12:57,590
you can generate poc's for any particular target of a form that you want.
156

157
00:12:58,300 --> 00:12:59,510
I hope you guys understood.
157

158
00:12:59,800 --> 00:13:00,340
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Cross Origin Resource Sharing (CORS)

0
1
00:00:02,250 --> 00:00:11,790
Hello everyone so in this video we are going to study about cors which stands for cross origin
1

2
00:00:11,850 --> 00:00:14,130
resource sharing.
2

3
00:00:14,210 --> 00:00:20,910
So in this video we are going to learn about what is cors why it happens.
3

4
00:00:21,140 --> 00:00:25,810
What is the severity of cors and what are the different way to achieve.
4

5
00:00:25,820 --> 00:00:35,150
Cors ,so first let us understand how a cors attack works.
5

6
00:00:35,150 --> 00:00:41,930
As you can see on the left side is the client which is the user the right side is the server to which
6

7
00:00:41,930 --> 00:00:44,300
the client is going to communicate to.
7

8
00:00:44,480 --> 00:00:47,390
And their is attacker at the top.
8

9
00:00:47,390 --> 00:00:50,080
So first thing first.
9

10
00:00:50,090 --> 00:00:58,670
A client sends a request to the server and the request is that he wants to log in into www.bank
10

11
00:00:58,670 --> 00:01:00,180
.com.
11

12
00:01:00,380 --> 00:01:03,610
So the server responds fine.
12

13
00:01:03,770 --> 00:01:11,180
You can log in into the account with your credentials and when you have supplied the credentials the
13

14
00:01:11,180 --> 00:01:19,500
server says take your profile which is www.bank.com/User1/profile.
14

15
00:01:19,940 --> 00:01:25,290
So the client has been successfully authenticated with the server.
15

16
00:01:25,490 --> 00:01:26,080
Perfect.
16

17
00:01:26,600 --> 00:01:34,730
Now the attacker sends a request to the server and say yeah server.
17

18
00:01:34,730 --> 00:01:39,820
Please trust me and send me the victim's data of his profile.
18

19
00:01:40,550 --> 00:01:52,310
So the attacker is telling the server to trust this attacker and send the client data to the attacker.
19

20
00:01:52,310 --> 00:01:57,940
How we're going to do this the attacker is going to trick the server.
20

21
00:01:57,950 --> 00:02:06,480
Interesting that this attacker is a legitimate resource or a trusted resource.
21

22
00:02:06,980 --> 00:02:16,550
And this server will then transfer the data and this server will say  sure take the www.bank.com
22

23
00:02:16,550 --> 00:02:19,490
/user1/profile.
23

24
00:02:20,000 --> 00:02:29,660
And this contains the data of that client that was authenticated with the server just to wrap up how a cors works
24

25
00:02:29,690 --> 00:02:38,410
whenever a client authenticate to the server and the server has given the response to the client.
25

26
00:02:38,690 --> 00:02:48,080
And if the attacker is able to see the data of the client by asking it from the server and the server
26

27
00:02:48,530 --> 00:02:58,490
trust the attacker and sends the data to the attacker then this is a valid cors vulnerability.
27

28
00:02:59,240 --> 00:03:07,010
So I hope you guys understood that the principle of cors is basically trusting arbitrary domains and
28

29
00:03:07,010 --> 00:03:09,650
sending data.
29

30
00:03:09,650 --> 00:03:13,660
So I hope you guys like this we knew and understood the principle of cors.
30

31
00:03:14,750 --> 00:03:15,230
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,810 --> 00:00:02,870
Hello everyone.
1

2
00:00:02,880 --> 00:00:11,750
So in this video of cors we are going to see three very important cases for identification of cors
2

3
00:00:11,790 --> 00:00:13,790
vulnerability.
3

4
00:00:14,010 --> 00:00:21,720
So this is the first case which is the best case for this vulnerability as you can see under the left
4

5
00:00:21,720 --> 00:00:23,250
side.
5

6
00:00:23,250 --> 00:00:26,130
It is a request and onto the right side.
6

7
00:00:26,220 --> 00:00:28,180
It is a response.
7

8
00:00:28,260 --> 00:00:36,960
So if we try to add a header into the request and the header is origin and let's say we type any
8

9
00:00:36,960 --> 00:00:39,740
".com" which is a "attacker.com."
9

10
00:00:40,050 --> 00:00:48,780
And if this attacker.com gets reflected into the response in this two headers that is Access control
10

11
00:00:48,840 --> 00:00:56,850
allow origin: attacker.com and access control allow credentials true then this is vulnerable
11

12
00:00:57,940 --> 00:00:59,390
and which is the best case.
12

13
00:00:59,400 --> 00:01:09,610
Best  test case for us so we have understood the first and the best test case that whenever we tried to supply
13

14
00:01:09,610 --> 00:01:16,930
attacker.com into the origin into the request if we get the attacker.com as it is into the
14

15
00:01:16,930 --> 00:01:22,640
response then it is the best test case for that attack.
15

16
00:01:22,690 --> 00:01:23,470
So now let's see
16

17
00:01:26,820 --> 00:01:34,830
the second best test case for our exploitation. In the request it is attacker.com
17

18
00:01:38,370 --> 00:01:39,380
in the origin handle.
18

19
00:01:40,110 --> 00:01:51,060
And in the response, if it shows something like null in access control allow origin and in access control
19

20
00:01:51,060 --> 00:01:59,260
allow credentials if it is true then also it is the best test case for our attack.
20

21
00:01:59,490 --> 00:02:05,910
So I hope you guys understood the first and the second test case in the first test case we got attacker
21

22
00:02:05,940 --> 00:02:13,230
.com as it is by passing it in the request we got as it is into their response in the second Test
22

23
00:02:13,230 --> 00:02:23,460
Case we passed attacker.com and the response we got NULL which also means it is exploitable.
23

24
00:02:23,970 --> 00:02:32,160
So let's see the last test case which is the case 3 which is a bad implementation but not exploitable
24

25
00:02:32,250 --> 00:02:33,540
test case.
25

26
00:02:33,780 --> 00:02:36,870
We cannot exploit this test case.
26

27
00:02:36,870 --> 00:02:46,590
So in the request if attacker.com is passed into a header that is origin and in the response if
27

28
00:02:46,590 --> 00:02:50,090
we get a star in access control allow origin.
28

29
00:02:50,130 --> 00:02:54,870
If we get a star then it is not exploitable.
29

30
00:02:54,870 --> 00:02:57,850
This test case is not exploitable.
30

31
00:02:57,960 --> 00:03:00,210
We can not explain this.
31

32
00:03:00,210 --> 00:03:09,000
So to conclude the first two test cases we can exploit in which we are able to see a reflection of the
32

33
00:03:09,000 --> 00:03:11,880
origin into the response that is attacker.com.
33

34
00:03:11,880 --> 00:03:15,320
That is the first test case in the second test case.
34

35
00:03:15,450 --> 00:03:19,230
If we are able to see null then it is also exploitable.
35

36
00:03:19,350 --> 00:03:23,640
But if you're getting a star into the response it is not exploitable.
36

37
00:03:24,810 --> 00:03:28,710
So I hope you guys understood this and now it is the practical time.
37

38
00:03:29,220 --> 00:03:30,870
Let's see the practical for this
38

39
00:03:34,860 --> 00:03:39,330
as you can see I'm going to do a practical on this website.
39

40
00:03:39,570 --> 00:03:43,420
So we are going to do this practical using two ways.
40

41
00:03:43,440 --> 00:03:45,100
First is curl.
41

42
00:03:45,900 --> 00:03:55,600
And second is Burpe suit so now I'm going to start my burpe go in my proxy type and I'm going to intercept
42

43
00:03:55,660 --> 00:04:00,400
this request so I will go to the website and try to reload it.
43

44
00:04:00,550 --> 00:04:05,650
I will get a request into my Burpe suit after getting the request.
44

45
00:04:05,650 --> 00:04:13,690
I'm going to send this request to the repeater so that I can reuse this request again and again after
45

46
00:04:13,690 --> 00:04:21,010
sending it to the repeater I will leave the request and I will go in  repeater tab now here what
46

47
00:04:21,010 --> 00:04:29,900
I'm going to do is I'm going to add a new header and that header is origin as we saw into our test cases.
47

48
00:04:29,920 --> 00:04:32,120
So let me just add it over here.
48

49
00:04:32,290 --> 00:04:34,050
Someone to type origin.
49

50
00:04:34,660 --> 00:04:43,240
htpps// instead of attacker.com I'm going to type hacktify.in and I'm going to
50

51
00:04:43,240 --> 00:04:44,700
hit go.
51

52
00:04:44,770 --> 00:04:49,020
Let's see if we get that into the response.
52

53
00:04:49,030 --> 00:04:53,920
So let me just search here hacktify see if it is matching in the response.
53

54
00:04:53,920 --> 00:05:02,100
No it is not matching so if you look closely into the response that is something which is generated
54

55
00:05:02,580 --> 00:05:09,130
it is link and in the link I am getting one more end point of zinghr.com.
55

56
00:05:09,150 --> 00:05:13,980
So what if I tried to send a request to this endpoint with this.
56

57
00:05:13,980 --> 00:05:15,200
origin
57

58
00:05:15,270 --> 00:05:16,310
Let's see.
58

59
00:05:16,440 --> 00:05:25,670
Does hacktify.in get reflected into the response or not so this time when I did go perfect.
59

60
00:05:25,820 --> 00:05:33,350
So as you can see now the zinghr.com server has trusted this attackers server that is hacktify.in
60

61
00:05:33,350 --> 00:05:42,750
and is ready to exchange the data between the server so here.
61

62
00:05:42,850 --> 00:05:50,710
This website is vulnerable to cross origin resource sharing vulnerability as we can see access control
62

63
00:05:50,750 --> 00:05:57,450
allow origin is attacker.com which is reflected and access control allow credentialed is true.
63

64
00:05:57,490 --> 00:06:06,480
Now if you recall this is the first and the best test case in which our requirement is satisfied that
64

65
00:06:06,580 --> 00:06:12,540
attacker.com should reflect into the response so perfect.
65

66
00:06:12,580 --> 00:06:22,530
This is the perfect condition to exploit.
66

67
00:06:22,590 --> 00:06:24,880
Now we have found this through Burpe suit.
67

68
00:06:24,900 --> 00:06:28,120
Let's see how to do this manually also.
68

69
00:06:29,730 --> 00:06:36,260
So for doing this manually you have to fire up your terminal and just type curl for those who don't
69

70
00:06:36,260 --> 00:06:45,090
know what is curl. Curl is a simple utility which is responsible for sending a request to any target
70

71
00:06:45,210 --> 00:06:49,960
and getting a response so you're going to use curl
71

72
00:06:50,190 --> 00:06:56,400
And I'm going to type https://zinghr.com which is my target
72

73
00:06:56,850 --> 00:07:10,020
/wp-json and now I'm going to type -I which means I don't want to see the response
73

74
00:07:10,200 --> 00:07:18,810
I just want to see the response headers not the whole page or the page source so after hitting this
74

75
00:07:18,960 --> 00:07:26,040
I got the response headers as you can see the headers like this.
75

76
00:07:26,040 --> 00:07:26,700
Perfect.
76

77
00:07:27,120 --> 00:07:35,230
So now what I'm going to do is I'm going to add a new header into the request.
77

78
00:07:35,340 --> 00:07:38,190
How do we add using -H flag.
78

79
00:07:38,670 --> 00:07:44,640
So I'm going to add a new header that is origin as we did into the burpe suit and I'm going to type
79

80
00:07:44,640 --> 00:07:46,600
here hacktify.in.
80

81
00:07:46,650 --> 00:07:53,050
And let me just add https also.
81

82
00:07:53,100 --> 00:07:59,670
And now I'm going to hit enter and verify that this origin has been trusted by zinghr.com
82

83
00:07:59,670 --> 00:08:01,650
or not.
83

84
00:08:01,650 --> 00:08:08,350
If this is trusted it will reflect back into the response headers in access control allow credentials true
84

85
00:08:08,350 --> 00:08:14,750
an access control allow origin attacker.com which is hacktify.in
85

86
00:08:17,940 --> 00:08:21,370
so perfect as we can see.
86

87
00:08:21,420 --> 00:08:28,950
our best test case that if the first test case is been satisfied over here and we are able to get our
87

88
00:08:29,010 --> 00:08:33,330
attacker.com reflected into the response.
88

89
00:08:33,330 --> 00:08:39,720
So I hope you guys understood how to find this vulnerability using burpe suite as well as Curl.
89

90
00:08:40,080 --> 00:08:46,140
In the next video we are going to see how we can do successful exploitation of this vulnerability after
90

91
00:08:46,230 --> 00:08:50,130
Identification of a vulnerable target.
91

92
00:08:50,130 --> 00:08:50,610
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,010 --> 00:00:03,380
Hello everyone.
1

2
00:00:03,390 --> 00:00:09,930
So in this video we are going to see exploitation of cors  through reflection origin type.
2

3
00:00:11,040 --> 00:00:17,260
So in this video my target is synack.com/sensitive details.
3

4
00:00:17,640 --> 00:00:22,890
So basically synack.com is a red teaming global red teaming  company.
4

5
00:00:23,910 --> 00:00:30,960
I was invited for this to join as a member so I successfully completed my exam.
5

6
00:00:31,200 --> 00:00:39,780
And after that I just wanted to test the portal and I successfully found out a critical vulnerability that
6

7
00:00:39,780 --> 00:00:41,480
was cors.
7

8
00:00:41,790 --> 00:00:44,580
So this type was a reflection type.
8

9
00:00:44,700 --> 00:00:46,110
So let's see how to do this
9

10
00:00:49,700 --> 00:00:52,130
so it's the practical time and let's see.
10

11
00:00:53,630 --> 00:01:03,020
So as you can see here cors POC exploit as you can see in the page source the request is going to
11

12
00:01:03,020 --> 00:01:09,640
synack.mindflash.com/mm/ account/ trainee-config.
12

13
00:01:11,060 --> 00:01:15,620
So this end point is going to an account training config that will go here.
13

14
00:01:15,650 --> 00:01:21,590
Let me click on exploit , clicking on exploit as you can see my account idea is this.
14

15
00:01:21,590 --> 00:01:23,130
This is my account number.
15

16
00:01:23,480 --> 00:01:28,530
And if I scroll will be able to see my details containing my name.
16

17
00:01:28,670 --> 00:01:32,690
So let me just go to the details which contains my name.
17

18
00:01:32,690 --> 00:01:38,240
Perfect as you can see the first name is Rohit last name is gautam on this portal.
18

19
00:01:38,240 --> 00:01:43,030
That is an synack.mindfresh.com and it again contains a lot of sensitive information below.
19

20
00:01:43,310 --> 00:01:47,120
So I'm not going to show you that sensitive information for now.
20

21
00:01:47,240 --> 00:01:49,560
Let me just go.
21

22
00:01:50,150 --> 00:01:50,510
here
22

23
00:01:53,500 --> 00:02:05,140
as you can see this end point and here again as you can see and I am able to get the data.
23

24
00:02:05,500 --> 00:02:15,820
So this was the proof of concept of how I was able to achieve sensitive information from the line Web
24

25
00:02:15,820 --> 00:02:18,790
site to my attackers Web site.
25

26
00:02:18,790 --> 00:02:24,550
So I hope you guys understood that this is a very critical vulnerability in which a lot of sensitive
26

27
00:02:24,550 --> 00:02:29,270
information has been sended from the server to the attackers server.
27

28
00:02:30,520 --> 00:02:31,000
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,770 --> 00:00:03,150
Hello everyone.
1

2
00:00:03,150 --> 00:00:10,800
So in this we video we are going to see exploitation of cors which is a reflection of origin type.
2

3
00:00:10,860 --> 00:00:18,870
So if our origin is getting reflected into the response then this is a successful cors and we can do
3

4
00:00:18,870 --> 00:00:21,090
the exploitation of this type of attack.
4

5
00:00:22,200 --> 00:00:29,910
So how do we do this by adding a header that is origin.com into the request, if the attacker.com
5

6
00:00:29,920 --> 00:00:37,500
gets reflected into the response with Access Control allow origin and access control
6

7
00:00:37,590 --> 00:00:41,750
allow credentials true then we have a WIN.
7

8
00:00:41,850 --> 00:00:52,660
So we already know the reflection type of origin which will successfully lead to a cors attack.
8

9
00:00:52,670 --> 00:00:57,920
So now we are going to do exploitation on the GoPro website.
9

10
00:00:58,850 --> 00:01:07,070
As you can see our target will be as nttps://www.GoPro.com sensitive API endpoint.
10

11
00:01:07,910 --> 00:01:14,740
And we are going to get a credential which means the cookie data at the attacker server.
11

12
00:01:16,130 --> 00:01:19,460
So let's see this in action
12

13
00:01:23,150 --> 00:01:31,280
as you can see I have already made a cors quick poc exploit code and I'm going to hit on exploit
13

14
00:01:31,880 --> 00:01:33,690
before hitting an exploit.
14

15
00:01:33,710 --> 00:01:41,120
Let me show you the page source and you can see the request is going to API of GoPro.com and you
15

16
00:01:41,120 --> 00:01:45,970
can see version one account and this is the account number.
16

17
00:01:46,430 --> 00:01:52,940
So this is the account number of the user that I created.
17

18
00:01:53,210 --> 00:01:54,830
And let's see this.
18

19
00:01:54,830 --> 00:01:58,130
If I hit on exploit the way get the user details.
19

20
00:01:58,160 --> 00:01:59,060
Yes.
20

21
00:01:59,240 --> 00:02:04,970
As you can see I'm getting the details which is the first name is Yash and the payload which were saved
21

22
00:02:05,480 --> 00:02:15,260
the last name I kept was ASSD so perfect I am able to get the sensitive details of any user from the
22

23
00:02:15,320 --> 00:02:27,230
API of GoPro and GoPro is trusting my srsecure. xyz as an trusted source and is sending the data
23

24
00:02:27,290 --> 00:02:32,160
to this specific server which is vulnerability.
24

25
00:02:32,180 --> 00:02:38,480
So I hope you guys understood how we were able to exploit this vulnerability and this is a very critical
25

26
00:02:38,480 --> 00:02:45,340
vulnerability in this case because the website is trusting any other that Origin source and 
26

27
00:02:45,350 --> 00:02:48,430
it is sending the sensitive data to that server.
27

28
00:02:49,280 --> 00:02:54,980
Let me just open up the console by clicking Inspect Element.
28

29
00:02:54,980 --> 00:03:00,920
Let me just go here and again try to click on exploit and show you what happens in the background.
29

30
00:03:01,580 --> 00:03:11,370
So when I click on exploit when request is going as you can see xml http request is going and I get
30

31
00:03:11,380 --> 00:03:16,360
request and perfect that connection is established.
31

32
00:03:16,400 --> 00:03:25,970
As you can see on on to the right and I am getting the data from the GoPro api which is very sensitive
32

33
00:03:28,480 --> 00:03:34,390
so I hope you guys understood in this video how we were able to achieve this and how we were able to
33

34
00:03:34,390 --> 00:03:36,880
get the data.
34

35
00:03:36,880 --> 00:03:43,780
Let me just click on this request and just show you these are the response headers and the response
35

36
00:03:43,780 --> 00:03:50,770
headers I am able to see access control allow credentials true and access control allow origin
36

37
00:03:50,890 --> 00:03:53,200
https://srsecure.xyz.
37

38
00:03:54,010 --> 00:04:03,820
So if you try to recall guys then this is the first and the best test case for doing cors attack when
38

39
00:04:04,150 --> 00:04:11,710
we put attacker.com into the origin and it gets reflected into the response it is the best test case
39

40
00:04:11,710 --> 00:04:13,700
as you can see it is getting reflected.
40

41
00:04:14,320 --> 00:04:21,130
Let me just scroll down to the headers of request and you can see I have added the origin which is
41

42
00:04:21,230 --> 00:04:23,670
srsecure.xyz.
42

43
00:04:23,830 --> 00:04:31,900
So this successfully exploitation of cors is the first test case that we have done and we are able
43

44
00:04:31,900 --> 00:04:39,310
to get a lot of sensitive information from that api which is indeed a very critical issue.
44

45
00:04:40,120 --> 00:04:47,200
So I hope you guys understood into this exploitation of cors video that how we are able to achieve
45

46
00:04:47,200 --> 00:04:52,250
sensitive information from any other web server to our web server.
46

47
00:04:52,270 --> 00:04:52,750
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,070 --> 00:00:03,600
Hello everyone.
1

2
00:00:03,600 --> 00:00:10,350
So in this video we are going to see one more cors poc exploit for a website which is canva
2

3
00:00:10,350 --> 00:00:11,730
dot com.
3

4
00:00:11,730 --> 00:00:14,320
This bug was reported on background.
4

5
00:00:15,460 --> 00:00:19,620
So let me just show you the proof of concept.
5

6
00:00:19,680 --> 00:00:26,520
So as you can see all here I'm going to click on exploit and yes I'm getting the data from the server
6

7
00:00:26,580 --> 00:00:33,910
of canva.com which means canva is trusting the attackers Web site which is srscure.
7

8
00:00:33,960 --> 00:00:40,300
xyz and is sending the sensitive data onto this attacker server.
8

9
00:00:40,590 --> 00:00:41,350
Perfect.
9

10
00:00:41,370 --> 00:00:43,590
So let's see what is happening into the background.
10

11
00:00:44,100 --> 00:00:47,830
Let's quickly go into the Inspect Element and go to the console.
11

12
00:00:47,880 --> 00:00:54,720
Again hit on exploits and you can see request is going which is a xml https request.
12

13
00:00:54,720 --> 00:00:56,790
Let me click on here
13

14
00:00:56,940 --> 00:00:59,010
As you can see the request is of canva.
14

15
00:00:59,700 --> 00:01:03,920
Let's quickly see the response headers in response headers.
15

16
00:01:03,960 --> 00:01:10,290
This is access control allow origin true and access control allow credentials true which is the
16

17
00:01:10,290 --> 00:01:13,950
best test case for the attack as we have already studied about that
17

18
00:01:16,960 --> 00:01:24,820
and now let us go to the request headers and see the origin which is given as the attackers website.
18

19
00:01:24,910 --> 00:01:26,920
Let's go and check the page source.
19

20
00:01:26,920 --> 00:01:30,060
Also as you can see over here.
20

21
00:01:31,040 --> 00:01:32,660
End Point is of canva.
21

22
00:01:33,100 --> 00:01:42,010
So I hope you guys understood how you were successfully able to exploit canva.com Web site.
22

23
00:01:42,370 --> 00:01:42,860
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,540 --> 00:00:01,970
Hello everyone.
1

2
00:00:01,980 --> 00:00:09,210
So in this video I'm going to show you a cors which I was able to find out in one of the domains of
2

3
00:00:09,210 --> 00:00:11,290
Facebook.
3

4
00:00:11,720 --> 00:00:13,460
So let's see this action
4

5
00:00:17,710 --> 00:00:21,050
we can see here is the POC exploit and  i"ll just hit on exploit.
5

6
00:00:21,070 --> 00:00:24,060
And you can see I was able to get the data from Facebook
6

7
00:00:27,830 --> 00:00:28,320
yes.
7

8
00:00:28,370 --> 00:00:34,460
I'm getting the data from about.fb.com which is one of the domain which has been purchased
8

9
00:00:34,580 --> 00:00:42,430
by Facebook so let me show you what exactly happens into the console.
9

10
00:00:42,520 --> 00:00:44,710
What is happening into the background.
10

11
00:00:45,220 --> 00:00:53,170
So when I click on exploit you can see an xml http request is going and I'm getting the data from
11

12
00:00:53,170 --> 00:00:58,150
the Facebook server and is trusting the attackers server and it's sending the data.
12

13
00:00:58,150 --> 00:01:01,380
So let's see this by clicking on here.
13

14
00:01:01,450 --> 00:01:06,030
As you can see the target is about.fb.com.
14

15
00:01:06,040 --> 00:01:13,150
Let me just go over here and you can see these are the Response Headers which satisfy the first test case
15

16
00:01:13,180 --> 00:01:20,230
which is access control allow credentials true and access control allow origin attacker.com which
16

17
00:01:20,230 --> 00:01:22,770
is srsecure.xyz
17

18
00:01:22,770 --> 00:01:29,500
Let us just quickly move on to the request headers and again see we have given our origin into the headers.
18

19
00:01:29,500 --> 00:01:38,890
That is srsecure.xyz and due to which the website is the server of Facebook dot com is
19

20
00:01:38,890 --> 00:01:47,230
trusting us as you can see this is the end point about.FB.com /WP-json which is
20

21
00:01:47,350 --> 00:01:52,960
trusting the attacker server and is sending data to the attackers server.
21

22
00:01:54,310 --> 00:02:02,720
So I hope you guys understood how we exploited this cors onto this about.fb.com Web server.
22

23
00:02:02,770 --> 00:02:03,250
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,990 --> 00:00:02,480
Hello everyone.
1

2
00:00:02,490 --> 00:00:08,950
So in this video we are going to see exploitation of cors using prefix batch type.
2

3
00:00:10,260 --> 00:00:16,850
So our target to you all is hack on India dot org and here in.
3

4
00:00:16,860 --> 00:00:23,520
We are going to add evil dot com at the end of this Web site.
4

5
00:00:23,610 --> 00:00:29,470
So this attack type is known as prefix match exploitation of cors.
5

6
00:00:29,520 --> 00:00:33,390
So here in well testing.
6

7
00:00:33,510 --> 00:00:42,090
I noticed that whenever I tried to supply any arbitary origin and hack on India it does not take it.
7

8
00:00:43,020 --> 00:00:48,100
So if I type origin hack on dot com and send it it does not take it.
8

9
00:00:48,720 --> 00:00:49,710
Why.
9

10
00:00:49,770 --> 00:00:58,620
Because the website developer has kept a condition that in origin hack on India should come.
10

11
00:00:58,620 --> 00:01:04,770
So when a tried evil hack on India org it did not allow me.
11

12
00:01:04,770 --> 00:01:12,180
So basically the condition is like that that anything new cannot be added before the host name or the
12

13
00:01:12,180 --> 00:01:13,440
website me.
13

14
00:01:13,500 --> 00:01:21,510
So if I do any modifications before the hostname that is hack on India org it does not take that and
14

15
00:01:21,510 --> 00:01:31,170
just blocks it but then i tried this condition in which I added the attacker.com on evil dot
15

16
00:01:31,170 --> 00:01:41,910
com at the end and I was able to successfully achieve cors on this website as this got reflected
16

17
00:01:41,970 --> 00:01:44,760
into the response as it is.
17

18
00:01:44,760 --> 00:01:46,770
So what does this mean.
18

19
00:01:47,130 --> 00:01:52,820
Any attacker can purchase this website which is evil dot com and make a subdomain.
19

20
00:01:52,860 --> 00:02:00,260
And again a subdomain of that and do a successful exploitation of cors on this Web site.
20

21
00:02:01,620 --> 00:02:07,940
So let's see the practical as it is the practical time.
21

22
00:02:08,430 --> 00:02:15,480
So you're in you can see I'm going to search curl and the target name.
22

23
00:02:15,480 --> 00:02:24,480
So a target is this hyphen I because I only want to see the response headers as I can see I'm able to
23

24
00:02:24,480 --> 00:02:26,310
see the headers here.
24

25
00:02:26,340 --> 00:02:32,440
Now I will add the attacker dot com into the origin.
25

26
00:02:32,580 --> 00:02:41,580
So let me just give hyphen H which means header and the header we're going to give us origin and
26

27
00:02:42,000 --> 00:02:49,800
so hack on India dot org Dot evil dot com.
27

28
00:02:49,800 --> 00:02:54,630
This is what we are going to give and I will hit enter.
28

29
00:02:54,630 --> 00:03:02,820
So let's see if this gets reflected into the response and perfect it is getting reflected as we give
29

30
00:03:02,850 --> 00:03:04,200
into the request.
30

31
00:03:04,440 --> 00:03:10,830
It is getting reflected into the response as it is as you can see allow access control.
31

32
00:03:10,830 --> 00:03:17,250
Origin is hack on India dot org dot com and an access control allow credential.
32

33
00:03:17,250 --> 00:03:23,180
It is giving true which means this is the best test case that we have got.
33

34
00:03:23,460 --> 00:03:28,180
And we are able to successfully exploit this.
34

35
00:03:29,070 --> 00:03:38,790
So I hope you guys understood in this video how we are able to exploit this type of scenario in which
35

36
00:03:39,740 --> 00:03:46,800
we are going to use suffix match as well as  prefix match to bypass these types of conditions
36

37
00:03:47,220 --> 00:03:52,110
and achieve a successful course exploitation.
37

38
00:03:52,110 --> 00:03:53,290
So I hope you guys understood.
38

39
00:03:53,690 --> 00:03:54,150
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,310 --> 00:00:03,890
Hello everyone.
1

2
00:00:03,900 --> 00:00:11,880
So in this video we are going to see exploitation of cors the type suffix match.
2

3
00:00:12,450 --> 00:00:23,490
So in here  as you can see  teh URL and the target is https://ukrainianpeople.us/
3

4
00:00:23,820 --> 00:00:26,570
wp-json/.
4

5
00:00:26,670 --> 00:00:37,890
Now if we look closely in the origin what I'm going to supply is evil Ukrainian people dot us, because
5

6
00:00:37,890 --> 00:00:47,010
guys some websites block trusting arbitrary attackers website that is evil dot com.
6

7
00:00:47,010 --> 00:00:49,070
How do they do it.
7

8
00:00:49,110 --> 00:00:57,630
Basically the developer puts a logic that any origin which is coming any request which is coming with
8

9
00:00:57,690 --> 00:01:06,540
any origin to the server should contain the hostname which is the host website's name which is Ukrainian
9

10
00:01:06,540 --> 00:01:08,460
people.
10

11
00:01:08,460 --> 00:01:18,690
But it does not check if the attacker is adding something into the suffix for the host name of the website
11

12
00:01:18,840 --> 00:01:20,540
and sending something.
12

13
00:01:20,580 --> 00:01:27,870
So as you can see here you are able to bypass this condition onto the website where the website was
13

14
00:01:27,870 --> 00:01:35,230
checking that Ukrainian people should come into the origin by adding evil with it.
14

15
00:01:35,280 --> 00:01:43,080
Now when we will send this evil Ukrainian people dot us the website is going to trust this way because
15

16
00:01:43,080 --> 00:01:52,080
their condition only checks that Ukrainian people dot us comes into the origin which is satisfied and
16

17
00:01:53,130 --> 00:01:56,860
successfully this will get reflected into their response.
17

18
00:01:56,880 --> 00:02:05,160
Now the attacker can quickly go and purchase this domain which is evil Ukrainian people dot us and then
18

19
00:02:05,190 --> 00:02:10,020
he can do the further cors exploitation attack.
19

20
00:02:10,020 --> 00:02:18,630
So I hope you guys understood that how we can do suffix match so let's see the practical because this
20

21
00:02:18,630 --> 00:02:20,020
is the practical time.
21

22
00:02:21,240 --> 00:02:21,750
So now
22

23
00:02:26,200 --> 00:02:32,880
I'm going to start curl and I'm going to give the target in two double quotes that is https
23

24
00:02:33,310 --> 00:02:37,350
Ukrainian people dot us slash WP hyphen Json.
24

25
00:02:37,420 --> 00:02:38,470
Perfect.
25

26
00:02:38,500 --> 00:02:44,760
Now I'm going to add hyphen I to only see the response headers.
26

27
00:02:45,490 --> 00:02:51,140
Now you can see these are the headers that have come from that web server.
27

28
00:02:51,160 --> 00:02:58,990
Now we are going to add our arbitrary origin that is the attacker dot com and will make the website
28

29
00:02:59,080 --> 00:03:09,560
to trust us so hyphen edge means header and the headers name is origin and trust evil Ukrainian people
29

30
00:03:09,560 --> 00:03:14,740
dot us.
30

31
00:03:14,810 --> 00:03:20,420
Let me just remove this extra things and perfect.
31

32
00:03:20,450 --> 00:03:26,770
Let's see if the webserver our this suffix match condition.
32

33
00:03:27,230 --> 00:03:28,250
And let's see this.
33

34
00:03:28,280 --> 00:03:30,260
And perfect.
34

35
00:03:30,260 --> 00:03:36,280
So as you can see access control allow origin our origin has reflected and the credentials are also
35

36
00:03:36,290 --> 00:03:37,430
true.
36

37
00:03:37,430 --> 00:03:45,670
So guys this is the second way to do this when some website does the check or keeps a condition within
37

38
00:03:45,890 --> 00:03:50,870
the website name or the host name should be reflected into the response.
38

39
00:03:50,870 --> 00:03:53,860
So this is one of the way to bypass that check.
39

40
00:03:54,140 --> 00:03:58,660
And this is type 2 which is suffix match.
40

41
00:03:58,670 --> 00:04:06,380
So I hope you guys understood how an attacker can exploit this by purchasing this new domain and exploiting
41

42
00:04:06,380 --> 00:04:08,310
it.
42

43
00:04:08,530 --> 00:04:09,230
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:02,540 --> 00:00:04,030
Hello everyone.
1

2
00:00:04,070 --> 00:00:08,220
So this is the cor's mitigation video.
2

3
00:00:08,390 --> 00:00:12,900
In this we're going to learn that what are the mitigations for cors.
3

4
00:00:12,980 --> 00:00:20,420
So the first and the best mitigation for cors is a sop that is same origin policy.
4

5
00:00:20,450 --> 00:00:22,790
So what does this policy means.
5

6
00:00:22,790 --> 00:00:32,420
This policy means that the website or the web application should not transfer any kind of data to
6

7
00:00:32,480 --> 00:00:35,540
any other web application.
7

8
00:00:35,540 --> 00:00:46,320
So it should only communicate and transfer the data with the same origin or to the same website.
8

9
00:00:46,400 --> 00:00:53,430
Second do not trust any arbiter origin and communicate with it.
9

10
00:00:53,780 --> 00:01:03,470
If any web application is getting any orrigin header as a request they should not trust that arbitrary
10

11
00:01:03,470 --> 00:01:10,490
header and give out sensitive information.
11

12
00:01:10,490 --> 00:01:20,240
Basically whenever our attacker tries to do a reflective origin based cors the server should discard
12

13
00:01:20,240 --> 00:01:25,680
that and should not trust it and should not give out response to that server.
13

14
00:01:27,650 --> 00:01:37,400
Secondly if a suffix or a prefix based cors exploitation is performed the server should do proper validation
14

15
00:01:38,540 --> 00:01:44,390
not just limited to checking the hostname into the origin.
15

16
00:01:44,390 --> 00:01:51,530
We have already seen if a server is must configured and just checks for the name into the origin header
16

17
00:01:51,890 --> 00:01:59,150
and takes decisions based on that which is dangerous can lead to cors exploitation.
17

18
00:01:59,290 --> 00:01:59,590
Yeah.
18

19
00:02:00,020 --> 00:02:03,980
So do not trust any arbitrary origin and communicate with.
19

20
00:02:03,980 --> 00:02:07,740
It is the best mitigation for cors.
20

21
00:02:07,940 --> 00:02:11,150
So I hope you guys understood that mitigation for cars.
21

22
00:02:11,150 --> 00:02:11,660
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,860 --> 00:00:03,650
Hello everyone.
1

2
00:00:03,660 --> 00:00:09,210
So in this video you're going to see the cors hackerone reports breakdown.
2

3
00:00:10,050 --> 00:00:15,900
So as you can see I have searched for cors hackers one reports and I have got a couple of reports.
3

4
00:00:15,900 --> 00:00:22,380
So we are going to do a complete breakdown of each and every report and understand how the security
4

5
00:00:22,380 --> 00:00:26,690
researchers were able to earn bounty through these reports.
5

6
00:00:26,700 --> 00:00:33,530
So let's take the example of the first report cors Misconfiguration allows to steal customers data.
6

7
00:00:33,540 --> 00:00:42,000
This was reported on this website that is local typiola bounty was awarded two thousand one hundred
7

8
00:00:42,000 --> 00:00:43,250
dollars.
8

9
00:00:43,320 --> 00:00:45,330
So let's see this.
9

10
00:00:45,330 --> 00:00:52,020
This configuration allowed an hacker to get the sensitive data from the server as you can see.
10

11
00:00:52,020 --> 00:00:57,150
This is the POC the same POC that we use http dot open.
11

12
00:00:57,150 --> 00:01:04,010
a get request is going to that end point I do not know what language is this in.
12

13
00:01:04,230 --> 00:01:05,530
No problem.
13

14
00:01:05,610 --> 00:01:07,770
So credientials are true.
14

15
00:01:08,370 --> 00:01:13,570
So the attacker is able to get the sensitive information onto his server.
15

16
00:01:14,100 --> 00:01:15,910
Let's see another report.
16

17
00:01:15,960 --> 00:01:23,490
This is cors Misconfiguration which allows to steal clients password authorization token and customer
17

18
00:01:23,490 --> 00:01:28,200
details for example names,ssn, bank account etc.
18

19
00:01:28,260 --> 00:01:34,740
This was again submitted to the same program bounty awarded one thousand nine hundred and eighty four
19

20
00:01:34,740 --> 00:01:36,690
dollars.
20

21
00:01:36,690 --> 00:01:45,300
So it was again a faulty cors misconfiguration through which the attacker was able to send data to his
21

22
00:01:46,090 --> 00:01:47,480
web server.
22

23
00:01:47,610 --> 00:01:50,750
As you can see over here this is the end point.
23

24
00:01:51,120 --> 00:01:54,220
And he was able to send the data on his computer.
24

25
00:01:55,200 --> 00:02:02,370
So next is cross origin resource sharing misconfiguration and stealing users information.
25

26
00:02:02,370 --> 00:02:06,570
This was reported to sagebrush and bounty audit was 1000 dollars
26

27
00:02:09,610 --> 00:02:10,700
so let's see this.
27

28
00:02:10,700 --> 00:02:18,550
And perfect as you can see in the POC This is the request tab in which the attacker has added a origin
28

29
00:02:18,640 --> 00:02:25,660
and in origin he has written something random a random strings and this origin will get reflected into
29

30
00:02:25,660 --> 00:02:26,350
the response.
30

31
00:02:26,350 --> 00:02:28,340
Let's see if it has got reflected.
31

32
00:02:28,360 --> 00:02:29,350
Perfect.
32

33
00:02:29,350 --> 00:02:35,250
It has got reflected and access control allow origin and the credentials should also be true.
33

34
00:02:35,260 --> 00:02:36,840
So yes it is true.
34

35
00:02:37,000 --> 00:02:43,040
And we have seen that this is the best test case according to us.
35

36
00:02:43,360 --> 00:02:46,720
And this is this holds the maximum severity.
36

37
00:02:47,110 --> 00:02:51,200
So this was awarded 1000 dollars.
37

38
00:02:51,370 --> 00:02:57,670
Perfect let's move ahead.
38

39
00:02:57,960 --> 00:03:05,100
This is again the same POC that we use and also we have done this a couple of times into a video
39

40
00:03:05,100 --> 00:03:05,750
series.
40

41
00:03:06,030 --> 00:03:07,980
Let us go to the next report.
41

42
00:03:08,010 --> 00:03:15,380
This is as a zomato dot com cors Misconfiguration that could lead to disclosure of sensitive information.
42

43
00:03:15,390 --> 00:03:22,200
This report was submitted to the zomato and as you can see it was rewarded with five hundred and fifty
43

44
00:03:22,200 --> 00:03:22,690
dollars.
44

45
00:03:22,800 --> 00:03:27,330
So let's see the report quickly and you can see the proof of concept.
45

46
00:03:27,360 --> 00:03:31,270
This is the request record can request contain the origin.
46

47
00:03:31,410 --> 00:03:36,040
That is developers xzomato dot com.
47

48
00:03:36,060 --> 00:03:43,810
As you can see over here so guys this is a prefix match condition.
48

49
00:03:43,810 --> 00:03:50,650
We have already seen into our videos how we can attack using prefix match condition and here in the attacker
49

50
00:03:50,740 --> 00:03:54,170
apply the same logic and then the response.
50

51
00:03:54,190 --> 00:03:56,830
This is going to get reflected.
51

52
00:03:56,830 --> 00:03:58,610
Let's see if this gets reflected.
52

53
00:03:58,870 --> 00:03:59,480
Perfect.
53

54
00:03:59,500 --> 00:04:06,290
It gets reflected over the here and the credentials are also true with satisfies our condition number
54

55
00:04:06,290 --> 00:04:08,790
one which is the best case for attack.
55

56
00:04:09,760 --> 00:04:14,360
And this way the attacker was able to compromise this perfect.
56

57
00:04:14,470 --> 00:04:21,890
Let's go to the next report so cors misconfiguration leading to private information disclosure.
57

58
00:04:22,070 --> 00:04:29,920
This was reported to ubiquiti and the bounty that was awarded was five hundred dollars.
58

59
00:04:29,990 --> 00:04:36,920
So due to the mistake of the cors policy the sites that these two websites course policy allowed extra
59

60
00:04:36,920 --> 00:04:43,250
https requests to be made from certain sites which were outside ubnt dot com and  ui dot com which
60

61
00:04:43,250 --> 00:04:44,480
are owned by this website.
61

62
00:04:44,990 --> 00:04:51,920
So this basically in simple language means this website was trusting some under the attackers Web site
62

63
00:04:52,280 --> 00:04:55,470
and transferring data to them.
63

64
00:04:55,470 --> 00:04:55,910
Perfect
64

65
00:05:01,810 --> 00:05:03,130
let's see the next report.
65

66
00:05:06,060 --> 00:05:12,750
Exploiting misconfigured cors to steal user information submitted to Rockstar Games bounty ordered
66

67
00:05:12,750 --> 00:05:14,430
500 dollars.
67

68
00:05:14,490 --> 00:05:23,500
So in this report there was a cors Misconfiguration issue and the data was shared inappropriately.
68

69
00:05:23,550 --> 00:05:29,670
They also provided poc which showed how attacker could exploit this remotely and the attacker could
69

70
00:05:29,670 --> 00:05:33,460
have get the data of other users onto his server.
70

71
00:05:35,110 --> 00:05:45,600
Again a simple demonstration of poc exploit type one that is the best test case next cors
71

72
00:05:45,730 --> 00:05:47,900
misconfiguration on legal report.
72

73
00:05:47,920 --> 00:05:49,970
Bounty awarded 20 dollars.
73

74
00:05:50,020 --> 00:05:51,440
It is the same poc.
74

75
00:05:51,610 --> 00:05:57,830
If you can see you here let us try to find the origin and where is the origin.
75

76
00:05:57,830 --> 00:05:59,320
Perfect in origin.
76

77
00:05:59,320 --> 00:06:03,870
It was submitted something and an access control.
77

78
00:06:03,940 --> 00:06:06,130
The attacker was again able to bypass it.
78

79
00:06:06,520 --> 00:06:12,250
Let's see the next report cors Misconfiguration leading to a account takeover submitted to Twitter dot
79

80
00:06:12,250 --> 00:06:13,870
com.
80

81
00:06:13,870 --> 00:06:22,680
This was again the same vulnerability in which the attacker gave evil dot net instead of niche
81

82
00:06:22,700 --> 00:06:23,790
dot co
82

83
00:06:23,800 --> 00:06:29,980
This is the suffix type that we have already seen in to our previous videos and the attacker was able
83

84
00:06:29,980 --> 00:06:35,070
to achieve this using the same  poc code that we have used.
84

85
00:06:35,530 --> 00:06:43,460
Next report cors misconfiguration on nordvpn dot com leading to private information disclosure and account
85

86
00:06:43,460 --> 00:06:43,800
takeover.
86

87
00:06:45,700 --> 00:06:53,920
So this was the vulneraliability which was reported to Nord VPN and you can see in the origin
87

88
00:06:53,920 --> 00:06:55,320
The attacker has given.
88

89
00:06:55,330 --> 00:07:01,990
I'm so evil dot com which is the attackers website and it will get reflected into the response and access
89

90
00:07:01,990 --> 00:07:02,570
control.
90

91
00:07:02,620 --> 00:07:07,230
Allow origin to let us see this.
91

92
00:07:07,350 --> 00:07:10,050
Let's see the response quickly and perfect.
92

93
00:07:10,080 --> 00:07:17,220
It is getting reflected over here and the credentials are also true which makes this the best test case
93

94
00:07:17,220 --> 00:07:19,870
for the word attack.
94

95
00:07:20,100 --> 00:07:27,630
Let's see the next report cross sharing resource Misconfiguration on U.S. Department of Defense.
95

96
00:07:27,690 --> 00:07:34,650
So this was the report submitted there in which you can see if the origin was given attacker dot com
96

97
00:07:34,680 --> 00:07:36,020
or exploit dot com.
97

98
00:07:36,180 --> 00:07:42,390
It was getting reflected into the response headers the same POC exploit code that we have used has been
98

99
00:07:42,390 --> 00:07:48,110
used here again and it was  reported which was accepted and then later on dissolved.
99

100
00:07:48,960 --> 00:07:54,120
Let's see next cors misconfiguration on the zomato dot com.
100

101
00:07:54,120 --> 00:07:57,050
Let's see the screenshot.
101

102
00:07:57,090 --> 00:08:00,350
And let me just zoom this a little bit.
102

103
00:08:00,570 --> 00:08:07,290
Perfect as I can see this is the request in the request in the origin it is going notzomato dot
103

104
00:08:07,290 --> 00:08:13,770
com which is the attackers dot com or evil dot com and it is going to get reflected into the response
104

105
00:08:13,830 --> 00:08:15,540
as you can see over here.
105

106
00:08:15,720 --> 00:08:21,900
Access Control allow origin notzomato and access control allow credentials true which is the best
106

107
00:08:21,900 --> 00:08:25,190
test case for our attack.
107

108
00:08:25,590 --> 00:08:28,390
Let's see the last report permissive cors policy.
108

109
00:08:28,390 --> 00:08:36,210
Trusting arbitrary extensions  origin which basically means that reflected kind of origin so bounty
109

110
00:08:36,210 --> 00:08:41,220
awarded five hundred dollars program is grammarly.
110

111
00:08:41,520 --> 00:08:47,600
They have not shown the report but as we can understand from here.
111

112
00:08:48,240 --> 00:08:55,950
So this researcher foobar 7 identified them as configuration in cors and CSRF handling allowed malicious
112

113
00:08:55,950 --> 00:09:01,230
browser extentions which have permission to interact with grammarly dot com domain and to impersonate
113

114
00:09:01,230 --> 00:09:01,740
the user.
114

115
00:09:02,340 --> 00:09:09,600
So basically the attacker was able to do some sensitive action with this grammarly dot com.
115

116
00:09:09,870 --> 00:09:11,490
Perfect.
116

117
00:09:11,490 --> 00:09:18,270
So I hope you guys understood this breakdown of hacker one report and this may be helpful for you for
117

118
00:09:18,270 --> 00:09:27,420
your live hunting onto the Web websites and web applications and I hope that this turns out to be helpful
118

119
00:09:27,420 --> 00:09:28,150
for you.
119

120
00:09:28,230 --> 00:09:34,830
And whenever you're doing your bug hunting you'll find a lot of cors types of vulnerability and you
120

121
00:09:34,830 --> 00:09:39,040
can increase the severity by taking them.
121

122
00:09:39,120 --> 00:09:44,590
Taking out sensitive data from the users website.
122

123
00:09:44,790 --> 00:09:45,300
Perfect.
123

124
00:09:46,110 --> 00:09:51,000
So what are the lessons learned.
124

125
00:09:51,390 --> 00:09:53,210
So cors hackerone report.
125

126
00:09:53,220 --> 00:09:54,710
Lessons learned.
126

127
00:09:55,050 --> 00:10:01,850
Always tried to test the endpoint with Origin reflected origin prefix and suffix.
127

128
00:10:01,920 --> 00:10:08,470
We have already covered these types of attacks and types into our previous videos.
128

129
00:10:08,490 --> 00:10:11,480
Also we have seen these types of reports on hacker one.
129

130
00:10:12,390 --> 00:10:20,370
Second try to extract the sensitive data because if you take the sensitive data out of the website then
130

131
00:10:20,700 --> 00:10:22,950
it will become more more severe.
131

132
00:10:23,730 --> 00:10:30,480
So if you extract sensitive data the severity will increase which will help you in increasing the reward.
132

133
00:10:30,780 --> 00:10:37,430
As we already saw into our previous videos you were able to exfiltrate some sensitive data like from
133

134
00:10:37,470 --> 00:10:42,580
API endpoints on GoPro website as well as synack Web site.
134

135
00:10:43,140 --> 00:10:50,770
So I hope you guys understood cors and you will find cors on to many website.
135

136
00:10:50,780 --> 00:10:51,290
Thank you.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 6: How to start with Bug Bounty Platforms and Reporting

0
1
00:00:02,340 --> 00:00:03,180
Hello everyone.
1

2
00:00:03,840 --> 00:00:12,190
So in this video we are going to see how to start with a bug bounty.
2

3
00:00:12,270 --> 00:00:19,710
So this is the first platform that is bugcrowd so in this we do I'm going to teach you how you can
3

4
00:00:19,710 --> 00:00:21,710
start your journey on bugcrowd.
4

5
00:00:22,330 --> 00:00:28,650
Basically this is a road map video for hunting bugs on to this platform.
5

6
00:00:28,680 --> 00:00:33,980
So as you can see I have opened bugcrowd.com into my web browser.
6

7
00:00:33,990 --> 00:00:41,120
You can just type bugcrowd.com into your browser also just navigate to the researcher portal because
7

8
00:00:41,120 --> 00:00:46,770
it is such a portal is where we are going to sign up and start hunting for bugs.
8

9
00:00:47,730 --> 00:00:49,650
So after clicking one the researcher portal
9

10
00:00:53,160 --> 00:00:56,200
you can see this page.
10

11
00:00:56,460 --> 00:01:03,390
So just click on Create Account after creating after clicking on the Create Account trying to fill all
11

12
00:01:03,390 --> 00:01:05,380
the necessary details over here.
12

13
00:01:05,550 --> 00:01:10,050
So let's say user name I type baby hacker in the e-mail address.
13

14
00:01:10,050 --> 00:01:16,260
Let me take my e-mail address hacker.udemy@gmail.com and the password.
14

15
00:01:16,260 --> 00:01:18,600
Let me take our password for this account
15

16
00:01:21,490 --> 00:01:23,520
in the confirm password.
16

17
00:01:23,520 --> 00:01:26,640
Let me confirm the password.
17

18
00:01:28,110 --> 00:01:33,480
And let me just hit on sign up, perfect!
18

19
00:01:33,520 --> 00:01:38,730
So they have sent a confirmation mail let me check if I got a mail yes I got the mail right now.
19

20
00:01:38,860 --> 00:01:41,020
Let me just click on confirm my account.
20

21
00:01:41,020 --> 00:01:46,760
So after clicking over here, your account was successfully confirmed.
21

22
00:01:46,780 --> 00:01:47,260
Perfect.
22

23
00:01:47,260 --> 00:01:50,210
So I'm going to logging into my bugcrowd account right now.
23

24
00:01:50,290 --> 00:02:01,580
So let me use my e-mail address and my password to log in into this account.
24

25
00:02:01,630 --> 00:02:07,090
So after giving the right credentials you just have to hit on log in and you'll be logged in into your
25

26
00:02:07,090 --> 00:02:07,690
account.
26

27
00:02:07,810 --> 00:02:15,010
Just agree and accept whatever the terms are there as as you can see this is the first thing that you
27

28
00:02:15,010 --> 00:02:17,330
will see which is the dashboard.
28

29
00:02:17,430 --> 00:02:23,170
You are at the points when you will start hunting valid when vulnerabilities, valid bugs you will get some
29

30
00:02:23,170 --> 00:02:26,950
points and your current rank will get updated
30

31
00:02:31,280 --> 00:02:31,820
perfect.
31

32
00:02:32,150 --> 00:02:38,380
So this is the first thing that you will see when you will sign up and you come into your dashboard.
32

33
00:02:38,390 --> 00:02:41,300
Let's go to the program's function.
33

34
00:02:41,300 --> 00:02:48,040
And when I click on Programs, Here I can see a long list of programs that are there.
34

35
00:02:48,050 --> 00:02:52,460
So there are around 161 programs currently.
35

36
00:02:52,460 --> 00:02:57,560
Which keeps on updating over here as you can see on the first one it is showing waitlisted.
36

37
00:02:57,860 --> 00:02:59,680
What does waitlisted means.
37

38
00:02:59,930 --> 00:03:08,120
I cannot hunt bugs into this account because there are three requirements that I need to first do that
38

39
00:03:08,120 --> 00:03:11,820
is I need to at least submit three reports.
39

40
00:03:12,170 --> 00:03:17,900
Those are valid then only I'll be able to hunt bugs into this leading video game company.
40

41
00:03:17,900 --> 00:03:19,150
There's three easy payments.
41

42
00:03:19,170 --> 00:03:26,430
Okay so these are the programs wherein you have to be eligible by hunting valid bugs on the bugcrowd
42

43
00:03:26,750 --> 00:03:31,890
and they will basically see that your profile is strong enough to hunt and do these types of websites.
43

44
00:03:32,040 --> 00:03:39,260
Okay so no problem if you're not able to hunt in these two Web site when you just make a new account.
44

45
00:03:39,290 --> 00:03:41,480
Let's see what are the open programs.
45

46
00:03:41,510 --> 00:03:48,310
So as you can see transfer wire is an open program Here also you can see takeway is also open program.
46

47
00:03:48,320 --> 00:03:50,090
So let me just go to transfer wise
47

48
00:03:55,100 --> 00:03:56,320
from the submit report.
48

49
00:03:56,330 --> 00:03:58,700
You can just a submit vulnerabilty report to them.
49

50
00:03:58,820 --> 00:04:03,140
Let's click on Transfer Wise and let's see the details about this program.
50

51
00:04:03,980 --> 00:04:09,950
So as you can see the name of the program is Transfer Wise the reward from hundred dollar minimum to
51

52
00:04:09,950 --> 00:04:17,070
4000 dollars per vulnerability maximum reward they  have given a six thousand dollars.
52

53
00:04:17,250 --> 00:04:23,300
Safe our means you just have don't have to disclose the bugs anywhere until they are fixed.
53

54
00:04:24,320 --> 00:04:25,610
These are the program details.
54

55
00:04:25,620 --> 00:04:29,790
Ninety three vulnerabilities have been found into this program and rewarded.
55

56
00:04:29,840 --> 00:04:34,600
They basically validate in four days average pay out.
56

57
00:04:34,640 --> 00:04:37,770
They have been giving is two fifty five point five five dollars.
57

58
00:04:37,780 --> 00:04:43,250
Perfect 47 unique bugs have been reported to them out of some are duplicate.
58

59
00:04:43,260 --> 00:04:45,240
So in total bugs are 192. 
59

60
00:04:45,480 --> 00:04:51,260
here are the euro the total latest Hall of Famers and these are the people who have recently joined the
60

61
00:04:51,260 --> 00:04:55,060
program and started hunting on transferwise as you can see.
61

62
00:04:55,060 --> 00:04:59,840
I'll go into the announcement  tab and you can see they keep on updating the rewards.
62

63
00:04:59,900 --> 00:05:06,860
Bonus period has ended for transfer wise  program and cloud stream so cloud stream is a feature in
63

64
00:05:06,860 --> 00:05:17,090
which the website owner of transfer wise decide if they want to make their reports public so any
64

65
00:05:17,090 --> 00:05:23,690
vulnerabilities that has been reported after reporting the fix it and after it has been fixed it is their
65

66
00:05:23,690 --> 00:05:30,040
decision that they want to make this report public for the people so they can basically read it.
66

67
00:05:30,050 --> 00:05:35,990
Hacker one is a very good platform in which we have the option of reading the reports bugcrowd has just
67

68
00:05:35,990 --> 00:05:38,840
recently implemented crowdstream.
68

69
00:05:38,840 --> 00:05:44,960
So let's just try to go there and you can see these reports submission accepted but we cannot report
69

70
00:05:49,440 --> 00:05:52,620
basically read any type of reports because they are not public.
70

71
00:05:52,620 --> 00:05:55,380
This is the Hall of Fame.
71

72
00:05:55,470 --> 00:05:56,270
Perfect.
72

73
00:05:56,310 --> 00:06:00,750
Let's go down and you can see these are the rules.
73

74
00:06:00,750 --> 00:06:02,220
Not important for us right now.
74

75
00:06:02,220 --> 00:06:09,720
Let's go here reward range as important as you can see any value which comes under P1 severity that
75

76
00:06:09,720 --> 00:06:15,120
is critical and gets the reward range between 3000 dollars to 4000 dollars.
76

77
00:06:15,120 --> 00:06:21,110
Similarly P2 which is a severe bug goes to for 1000 to 1500 moderate and low.
77

78
00:06:21,960 --> 00:06:28,330
So the vulnerabilities that have been we have studied in previous videos like Auth bypass and
78

79
00:06:28,380 --> 00:06:37,710
no rate limit XXS CSRF and if you try to get sensitive data out of those vulnerabilities of any
79

80
00:06:37,710 --> 00:06:44,210
of the user accounts this vulnerability may go to P1 P2 and P3.
80

81
00:06:44,460 --> 00:06:45,050
Yes.
81

82
00:06:45,060 --> 00:06:52,220
So this is important to see which is what is in your scope to test so Transfer Wise dot com that 
82

83
00:06:52,230 --> 00:06:55,940
is the website is in scope for your testing.
83

84
00:06:56,110 --> 00:07:02,940
Total 41 unique bugs have been already reported as you can see these are the bugs which are reported
84

85
00:07:02,970 --> 00:07:10,280
and you can see CSRF is already reported 2 unique reports have been reported and nine duplicate reports.
85

86
00:07:10,470 --> 00:07:10,760
Okay
86

87
00:07:13,590 --> 00:07:17,800
and the ios app and android app and other things are into the scope.
87

88
00:07:17,800 --> 00:07:20,040
What is it out of scope is important for you.
88

89
00:07:20,050 --> 00:07:28,600
Because I do not want you guys to waste your time on hunting on websites which are kept out of scope.
89

90
00:07:28,600 --> 00:07:35,920
For example you can see tw.com or tw.ee or any subdomains of these two websites
90

91
00:07:35,980 --> 00:07:37,080
are out of scope.
91

92
00:07:38,170 --> 00:07:43,900
So if you try to find anyone vulnerabilities on these domains they will not be acknowledged or rewarded
92

93
00:07:43,960 --> 00:07:47,350
because those are out of scope.
93

94
00:07:47,520 --> 00:07:48,290
Let us go here.
94

95
00:07:48,310 --> 00:07:56,300
As you can see focus areas they want you to bypass roles unauthorized accounts do authentication bypass.
95

96
00:07:56,540 --> 00:07:57,170
Okay.
96

97
00:07:58,010 --> 00:08:02,300
Let's scroll down and let's see what is.
97

98
00:08:02,320 --> 00:08:09,610
These are out of scope for vulnerabilities which means low hanging fruit basically which should not
98

99
00:08:09,610 --> 00:08:10,240
be reported.
99

100
00:08:12,770 --> 00:08:14,370
These are out of scope bugs.
100

101
00:08:14,820 --> 00:08:16,270
And ya program rules.
101

102
00:08:16,280 --> 00:08:18,080
So basically this is it.
102

103
00:08:18,080 --> 00:08:21,000
The most important thing is to look forward here is the reward range.
103

104
00:08:21,020 --> 00:08:22,170
What is in scope.
104

105
00:08:22,580 --> 00:08:26,690
And how many will vulnerabilities have been reported to that program.
105

106
00:08:26,690 --> 00:08:27,570
Perfect.
106

107
00:08:27,590 --> 00:08:32,860
So let's assume now that you have found a valid vulnerability on to this Web site.
107

108
00:08:32,900 --> 00:08:35,340
So how to submit a report on to this program.
108

109
00:08:35,510 --> 00:08:39,370
We have read all the rules and everything but how to submit a report.
109

110
00:08:39,950 --> 00:08:42,290
So you can see there is the option of submit a report.
110

111
00:08:42,320 --> 00:08:48,000
You just have to click on that after clicking on submit report.
111

112
00:08:48,140 --> 00:08:51,710
The first thing that it is asking is summary title.
112

113
00:08:51,710 --> 00:08:58,230
So you have to provide a summary title which is basically let's say you have found a XXS on this Web
113

114
00:08:58,230 --> 00:08:58,830
site.
114

115
00:08:58,880 --> 00:09:01,250
So you have to type XSS on
115

116
00:09:04,000 --> 00:09:08,860
the www.transferwire.com
116

117
00:09:11,880 --> 00:09:16,190
you have to choose the target after choosing the target.
117

118
00:09:16,230 --> 00:09:21,580
Technical severity of the choose a bug so we can choose let's say XSS.
118

119
00:09:21,870 --> 00:09:24,350
As we have found a XSS in XSS.
119

120
00:09:24,360 --> 00:09:29,650
Let's say we have found reflected XSS so reflected XSS nonself.
120

121
00:09:29,850 --> 00:09:33,000
Obviously not a self XSS.
121

122
00:09:33,030 --> 00:09:38,000
So I'll go down vote as the URL or the end point that you have found.
122

123
00:09:38,030 --> 00:09:39,520
So let's say a transfer.
123

124
00:09:40,470 --> 00:09:43,850
wise.com/
124

125
00:09:43,920 --> 00:09:58,000
I have found xss on let's say this end point slash here is the injection point equals to xss.
125

126
00:09:58,080 --> 00:10:03,330
So let's say the parameter here is the injection point is vulnerable and i am able to put the excess payload
126

127
00:10:03,460 --> 00:10:03,990
over there.
127

128
00:10:04,650 --> 00:10:06,060
So you have to give it like this.
128

129
00:10:06,060 --> 00:10:13,270
So it becomes easy for the program owners to validate the issue and triage quickly.
129

130
00:10:13,380 --> 00:10:17,550
The most important thing here is the description and the description.
130

131
00:10:17,550 --> 00:10:21,780
There should be two to four things which are important for any report that you make.
131

132
00:10:21,780 --> 00:10:28,420
First is description, description signifies what vulnerability you have found out.
132

133
00:10:28,650 --> 00:10:32,730
The next is steps to reproduce.
133

134
00:10:32,880 --> 00:10:36,870
So in this you have to type what are the steps to reproduce in that you can type.
134

135
00:10:36,870 --> 00:10:44,370
Step 1 go to this U.R.L. Step 2 put this XSS payload here into the injection point.
135

136
00:10:44,400 --> 00:10:46,560
Step 3 when you will hit enter.
136

137
00:10:46,560 --> 00:10:54,780
You'll be able to see that XSS executes which confirms there is a valid vulnerability.
137

138
00:10:55,800 --> 00:10:59,660
So the next thing is proof of concept.
138

139
00:10:59,820 --> 00:11:04,140
So you have to attach a screenshot or a video.
139

140
00:11:04,140 --> 00:11:13,830
I generally believe attaching a video is more helpful in some cases and it is a very good practice that
140

141
00:11:13,860 --> 00:11:18,950
instead of attaching screenshots you can attach a quick POC video.
141

142
00:11:22,150 --> 00:11:25,380
And the last one is mitigations that how to fix this.
142

143
00:11:25,430 --> 00:11:30,700
So guys we have already seen the mitigations for each type of vulnerability into our videos.
143

144
00:11:30,860 --> 00:11:37,640
You can just try to give reference from those videos over here that what are the fixes and these are
144

145
00:11:37,640 --> 00:11:41,030
two or add any additional inputs you don't have to give anything over there.
145

146
00:11:41,030 --> 00:11:42,530
It is optional.
146

147
00:11:42,530 --> 00:11:44,140
Finally add attachments.
147

148
00:11:44,150 --> 00:11:47,410
You can add your video or screenshot over here.
148

149
00:11:47,510 --> 00:11:55,100
I recommend attaching videos for each and every one vulnerability that you found.
149

150
00:11:55,100 --> 00:11:57,490
Now the last step is just hit on this report.
150

151
00:11:57,530 --> 00:12:00,960
So here in i am going to submit a blank report right now.
151

152
00:12:01,010 --> 00:12:03,300
Obviously this is an invalid report.
152

153
00:12:03,980 --> 00:12:06,570
But just to show you guys have submitted a report.
153

154
00:12:06,590 --> 00:12:11,810
After that you have to go into a submissions tab and you can see the vulnerability that has been reported
154

155
00:12:11,810 --> 00:12:17,990
over there so the vulnerability is access on tranferwise dot com and the categories is P3.
155

156
00:12:17,990 --> 00:12:20,690
The vulnerability is new for now.
156

157
00:12:20,690 --> 00:12:25,030
As soon as this is accepted it will become as you can see it is in pending tab.
157

158
00:12:25,160 --> 00:12:33,610
As soon as it is accepted it will come over here accepted one if it is rejected it will go here.
158

159
00:12:33,610 --> 00:12:35,440
Obviously this is going to get rejected.
159

160
00:12:35,440 --> 00:12:36,590
It is going to go here.
160

161
00:12:36,820 --> 00:12:40,560
If it is a duplicate of any other vulnerability it will go over here.
161

162
00:12:40,570 --> 00:12:46,810
Collaboration means if two people have found out this vulnerability then it will go into the collaboration
162

163
00:12:46,900 --> 00:12:51,310
and the bounty will be splited between both what the two researchers.
163

164
00:12:51,310 --> 00:12:52,750
The last thing is the invitations.
164

165
00:12:52,750 --> 00:12:56,260
When you get private invites to your account.
165

166
00:12:56,260 --> 00:13:01,020
If you hunt valid vulnerabilities onto this program you get private invites.
166

167
00:13:01,030 --> 00:13:02,280
So what are private invites.
167

168
00:13:02,290 --> 00:13:05,230
We're going to discuss it.
168

169
00:13:05,230 --> 00:13:09,010
Let's just click on the submission that we have made.
169

170
00:13:09,130 --> 00:13:15,270
As you can see this is the reference number a reference number helps you guys a lot whenever you have.
170

171
00:13:15,370 --> 00:13:20,650
You are stuck on to a new report or the support or the program one that is not replying or they are
171

172
00:13:20,650 --> 00:13:26,470
not able to understand the scenario that you have reported or basically if there is any misunderstanding
172

173
00:13:26,500 --> 00:13:32,230
you can just take this reference number and you can report to the support of bugcrowd.
173

174
00:13:32,470 --> 00:13:38,860
They are pretty awesome and they reply in a very quick timeframe and they will help you resolve your
174

175
00:13:39,130 --> 00:13:40,450
query.
175

176
00:13:40,780 --> 00:13:46,980
Cool so as you can see the target location is this priority P3 the report.
176

177
00:13:47,490 --> 00:13:56,080
Okay so I have made a blank report obviously on 22 April so you can see everything from your submission
177

178
00:13:56,080 --> 00:13:56,690
tab.
178

179
00:13:59,800 --> 00:14:04,180
So for now what I'm going to do is I'll go to payments tab.
179

180
00:14:04,210 --> 00:14:07,200
And you can see my upcoming payments are nothing.
180

181
00:14:07,480 --> 00:14:10,420
I can set up your Paypal.
181

182
00:14:10,480 --> 00:14:12,570
This is the leader board and the leader board.
182

183
00:14:12,570 --> 00:14:20,290
You can see top security researchers  lets go to crowd stream crowd stream is a new feature which has been
183

184
00:14:20,300 --> 00:14:22,930
implemented by bugcrowd.
184

185
00:14:23,090 --> 00:14:26,980
where in you can try to read the reports.
185

186
00:14:27,010 --> 00:14:31,470
Let's go to that invite tab wherein you will get some private invites.
186

187
00:14:31,480 --> 00:14:33,010
What I was talking about.
187

188
00:14:33,040 --> 00:14:41,170
So basically private invites are invites for some special programs which are not public.
188

189
00:14:41,170 --> 00:14:48,970
So a limited security researchers will be hunting on that program which means the scope is more for
189

190
00:14:48,970 --> 00:14:53,660
you to hunt as there are less people hunting on that program.
190

191
00:14:53,680 --> 00:14:54,700
Perfect.
191

192
00:14:54,700 --> 00:14:59,680
You can fill up your details over here if you've done any certification credentials your personal
192

193
00:14:59,680 --> 00:15:06,880
details if you want to update in the account tab we can just update your password your swag details
193

194
00:15:06,910 --> 00:15:10,930
what kind of t shirt size do you have.
194

195
00:15:10,990 --> 00:15:17,400
Let's say I put a L size you can put your address whatever you want to do this is deactivate account
195

196
00:15:17,470 --> 00:15:19,870
in the payment details.
196

197
00:15:19,870 --> 00:15:26,170
Any of the payments you have if you have you can connect your Paypal over here.
197

198
00:15:26,350 --> 00:15:29,080
There are two options for payment on bugcrowd.
198

199
00:15:29,080 --> 00:15:30,460
First is the people.
199

200
00:15:30,460 --> 00:15:33,340
And second one is pioneer.
200

201
00:15:33,340 --> 00:15:34,420
I prefer PayPal
201

202
00:15:41,260 --> 00:15:42,370
OK so perfect.
202

203
00:15:42,370 --> 00:15:46,710
Here again see whenever you try to log in it will create a session.
203

204
00:15:46,720 --> 00:15:52,480
You can see over their last option is identity verification you can verify your identity because some
204

205
00:15:52,480 --> 00:16:01,390
programs need compulsory identity verification ,so you can do that if you want to hunt for
205

206
00:16:01,390 --> 00:16:02,710
some programs.
206

207
00:16:02,710 --> 00:16:09,220
Lastly the support you can do is try to contact the support if you're facing any issues onto the platform
207

208
00:16:10,360 --> 00:16:17,580
so you can just drop our e-mail at a researcher at the bugcrowd.com wherein you'll be supported
208

209
00:16:17,590 --> 00:16:18,280
very quickly
209

210
00:16:21,820 --> 00:16:22,160
OK.
210

211
00:16:22,190 --> 00:16:25,270
So I hope you understood a lot of things over here.
211

212
00:16:25,490 --> 00:16:33,450
The last option is the dark mode which makes your eyes a little cool so you can hunt vulnerabilities
212

213
00:16:33,740 --> 00:16:34,750
and nighttime.
213

214
00:16:34,760 --> 00:16:38,280
Also this white light will not reflect for you guys.
214

215
00:16:38,310 --> 00:16:44,810
So yeah I just I can go to the program features you can see there are a lot of programs which you can
215

216
00:16:44,810 --> 00:16:49,100
hunt for and you can start hunting and all the open programs.
216

217
00:16:49,100 --> 00:16:55,430
So let me just try to search for TripAdvisor as we already found the XSS into our videos.
217

218
00:16:55,640 --> 00:16:58,160
And yes this is a program on bugcrowd.
218

219
00:16:58,460 --> 00:17:04,940
I already reported this vulnerability on TripAdvisor and have been awarded with the bounty for this
219

220
00:17:04,940 --> 00:17:05,620
vulnerability.
220

221
00:17:05,630 --> 00:17:11,540
So no need to submit that vulnerability as it may.
221

222
00:17:11,540 --> 00:17:12,930
Go in duplicate.
222

223
00:17:13,280 --> 00:17:13,580
OK.
223

224
00:17:13,610 --> 00:17:19,640
So this is how basically you do bug bounty hunting on bugcrowd.com.
224

225
00:17:20,120 --> 00:17:25,420
So this video was the roadmap for doing bug bounty hunting on bugcrowd where in.
225

226
00:17:25,430 --> 00:17:31,970
I tried to explain each and every functionality of bugcrowd how to navigate and how to submit valid
226

227
00:17:31,970 --> 00:17:33,090
reports.
227

228
00:17:33,170 --> 00:17:38,360
So I hope this video helps you guys in hunting on to this platform.
228

229
00:17:39,110 --> 00:17:39,620
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,260 --> 00:00:02,010
Hello everyone.
1

2
00:00:02,280 --> 00:00:10,560
So in this video we are going to see hackerone roadmap so how to find vulnerabilities on hackerone
2

3
00:00:10,570 --> 00:00:16,110
how to report vulnerabilities and where in to navigate onto the portal.
3

4
00:00:17,220 --> 00:00:24,440
So this is the second video for seeing and reporting vulnerabilities on hacker one.
4

5
00:00:24,510 --> 00:00:26,650
So let's just quickly start.
5

6
00:00:26,700 --> 00:00:32,300
So as you can see you just have to type hackerone.com into the URL of your browser.
6

7
00:00:32,340 --> 00:00:39,100
This will get opened just quickly Go on sign up and you tried to make an account on this Web site.
7

8
00:00:39,390 --> 00:00:40,440
Just have to choose.
8

9
00:00:40,470 --> 00:00:46,560
I am a hacker feature because you are going to report vulnerabilities so you are a hacker.
9

10
00:00:46,560 --> 00:00:48,030
So start hacking today.
10

11
00:00:48,030 --> 00:00:48,680
Perfect.
11

12
00:00:48,690 --> 00:00:51,340
You just need to give your details over here.
12

13
00:00:51,660 --> 00:00:54,000
So I'm going to give my details.
13

14
00:00:54,060 --> 00:00:55,530
Let's say I give this name
14

15
00:00:58,710 --> 00:01:01,980
and in my user name I can give any username that I want.
15

16
00:01:01,980 --> 00:01:09,030
Or let's say I give the same name e-mail address I give my email address for sign up process.
16

17
00:01:09,360 --> 00:01:16,820
And yes the important thing over here is you need to keep a strong entropy for your password.
17

18
00:01:16,890 --> 00:01:25,290
Hacker 1 does not allow keeping weak passwords so it will give you continuously give you errors.
18

19
00:01:25,290 --> 00:01:28,050
So you need to have strong entropy.
19

20
00:01:28,140 --> 00:01:30,010
So I have got some errors.
20

21
00:01:30,030 --> 00:01:32,400
So this user name has been already taken.
21

22
00:01:32,430 --> 00:01:32,660
OK.
22

23
00:01:32,670 --> 00:01:39,480
So I'll just make it to one two three and I'm going to set a password again.
23

24
00:01:39,810 --> 00:01:42,570
So yes it read this password
24

25
00:01:46,740 --> 00:01:49,050
and let me try to sign up again.
25

26
00:01:50,280 --> 00:01:50,580
OK.
26

27
00:01:50,580 --> 00:01:52,740
It does not contain enough entropy.
27

28
00:01:52,740 --> 00:02:01,890
As I said you guys you need to set a password which is strong enough then only it will allow you to keep
28

29
00:02:02,700 --> 00:02:07,790
a valid password.
29

30
00:02:08,000 --> 00:02:10,310
Well let me try to get one more password
30

31
00:02:16,310 --> 00:02:16,730
OK.
31

32
00:02:16,750 --> 00:02:17,470
So
32

33
00:02:20,700 --> 00:02:21,900
this time it should work.
33

34
00:02:22,800 --> 00:02:24,360
Let me give a very strong password
34

35
00:02:32,910 --> 00:02:33,220
now.
35

36
00:02:33,220 --> 00:02:34,480
That's a great password.
36

37
00:02:34,840 --> 00:02:35,870
OK.
37

38
00:02:35,950 --> 00:02:37,810
So let's see if this works.
38

39
00:02:37,900 --> 00:02:39,600
And me hit on create account.
39

40
00:02:41,350 --> 00:02:42,150
I hope this works.
40

41
00:02:42,150 --> 00:02:42,670
Perfect.
41

42
00:02:42,670 --> 00:02:46,770
So this password worked now you can see please verify our e-mail.
42

43
00:02:46,780 --> 00:02:48,880
So I just got a e-mail right now.
43

44
00:02:48,880 --> 00:02:53,220
I'm going to click on confirm my e-mail address address.
44

45
00:02:53,320 --> 00:02:53,860
Perfect.
45

46
00:02:53,860 --> 00:02:57,100
My account is successfully confirmed.
46

47
00:02:57,190 --> 00:03:06,370
So let me just quickly log in with my account that I created right now in the password field I'm going
47

48
00:03:06,370 --> 00:03:07,840
to again type my password
48

49
00:03:11,150 --> 00:03:14,620
click on remember me and click on sign in.
49

50
00:03:15,230 --> 00:03:26,270
So after i signing into the application the first dashboard that I'm going to see is this.
50

51
00:03:26,270 --> 00:03:32,510
So I'll just quickly go into the directory tab because this is what is important and you will find a
51

52
00:03:32,510 --> 00:03:35,240
list of programs over there.
52

53
00:03:35,270 --> 00:03:39,150
So after going into the directory you can see there.
53

54
00:03:39,200 --> 00:03:46,670
These are all the programs which are being listed on two hacker one so you can try to hunt on any program.
54

55
00:03:46,670 --> 00:03:50,690
There are a lot of programs so let me just go for a program that is uber
55

56
00:03:54,290 --> 00:03:56,600
and you can see uber is already there.
56

57
00:03:56,960 --> 00:04:01,180
Since 2014 researchers are hunting on this.
57

58
00:04:01,520 --> 00:04:07,250
So whenever you open a program it looks like this.
58

59
00:04:07,700 --> 00:04:10,740
This is everything rules regulations.
59

60
00:04:10,940 --> 00:04:19,250
Important thing for us is what is in scope what is out of scope and how much do they give for bounties.
60

61
00:04:19,280 --> 00:04:20,990
So these are out of scope domains.
61

62
00:04:20,990 --> 00:04:27,690
You have to leave these domains and report everything as that is in scope.
62

63
00:04:27,800 --> 00:04:34,170
So let me just go to submit report and you can see they are not allowing me to report.
63

64
00:04:34,340 --> 00:04:35,060
Why?.
64

65
00:04:35,210 --> 00:04:38,810
Because I does not have significant reputation.
65

66
00:04:39,080 --> 00:04:42,470
My signal is not good and I cannot hunt or report.
66

67
00:04:42,470 --> 00:04:43,670
vulnerability to uber.
67

68
00:04:43,700 --> 00:04:44,270
No problem.
68

69
00:04:44,960 --> 00:04:49,220
I'm going to increase my signal.
69

70
00:04:49,220 --> 00:04:50,720
How to do that?.
70

71
00:04:50,730 --> 00:04:57,960
So basically you can try for solving some CTF which are over here.
71

72
00:04:58,240 --> 00:05:02,210
Also you can try for some open programs.
72

73
00:05:02,790 --> 00:05:03,680
You can start with them.
73

74
00:05:03,680 --> 00:05:05,920
Let me just go to my profile.
74

75
00:05:05,930 --> 00:05:10,880
As you can see this is my profile which is currently empty right now.
75

76
00:05:11,240 --> 00:05:17,040
Let's go to the inbox feature, inbox feature is wherever you are whenever you try to report vulnerabilities
76

77
00:05:17,070 --> 00:05:18,850
that will come over here.
77

78
00:05:18,860 --> 00:05:24,560
So any open report, pending disclosure which is accepted report and all.
78

79
00:05:24,610 --> 00:05:26,280
Total number of reports.
79

80
00:05:26,360 --> 00:05:33,470
Let's go to the hacker dashboard when you look and see this is my profile.
80

81
00:05:33,470 --> 00:05:35,280
You can submit a report from here.
81

82
00:05:35,360 --> 00:05:36,950
You can read about hacker 1.
82

83
00:05:37,050 --> 00:05:43,970
And yes we can see on the left side bookmark five programs on the directory just choose five programs
83

84
00:05:44,000 --> 00:05:52,490
that you want to hunt for upvote five items on activity earn 26 points on hacker 1 0 1 Capture the Flag.
84

85
00:05:52,490 --> 00:05:58,100
This is helpful data because you will get a couple of invite for your next program that you can hunt
85

86
00:05:58,100 --> 00:05:58,400
for.
86

87
00:05:58,550 --> 00:06:01,220
So you can just solve this.
87

88
00:06:01,340 --> 00:06:04,640
Hacker 1 0 1 CTF if you want.
88

89
00:06:04,640 --> 00:06:09,360
This will just give you some off invites to start hunt for.
89

90
00:06:10,970 --> 00:06:11,720
Let's go back
90

91
00:06:14,410 --> 00:06:18,950
to the hackerone dashboard.
91

92
00:06:19,180 --> 00:06:19,400
Yeah.
92

93
00:06:19,450 --> 00:06:23,270
So you're for your.
93

94
00:06:23,290 --> 00:06:25,070
It is.
94

95
00:06:25,090 --> 00:06:27,570
That's it.
95

96
00:06:27,780 --> 00:06:31,800
Let me go to the profile settings again and it all the settings that you want over here.
96

97
00:06:34,290 --> 00:06:37,330
And let's see some options from here.
97

98
00:06:37,350 --> 00:06:37,860
You can.
98

99
00:06:37,860 --> 00:06:44,670
These are very basic options that you can fill whatever you want according to your need in payments.
99

100
00:06:44,670 --> 00:06:49,820
You can you will be able to see what are the total payments that you are going to get.
100

101
00:06:49,830 --> 00:06:56,550
Now it is balance zero perfect ,payment beyond preferences.
101

102
00:06:56,580 --> 00:07:03,960
I'm going to show you some important things only you can observe other features by yourself and explore
102

103
00:07:03,960 --> 00:07:04,760
them.
103

104
00:07:04,860 --> 00:07:12,300
So in pay out you can add a pay out method either paypal or anything the best is Paypal if we get any
104

105
00:07:13,260 --> 00:07:18,700
private invite it will be into your inbox directory.
105

106
00:07:18,870 --> 00:07:24,030
And the last one is the activity tab which is important you're in.
106

107
00:07:24,040 --> 00:07:30,750
You will be able to read all the reports which are being submitted on hacker 1 and which are kept open
107

108
00:07:30,750 --> 00:07:31,710
to read.
108

109
00:07:31,710 --> 00:07:40,680
So basically we can read about those reports and yeah you can come to know who and which security researcher
109

110
00:07:40,680 --> 00:07:43,800
has reported what kind of vulnerability to what program.
110

111
00:07:43,800 --> 00:07:53,040
As you can see CSRF on connecting Paypal as payment provider has been reported on April 10 recently.
111

112
00:07:53,040 --> 00:07:56,130
And the bounty awarded was 500 dollars.
112

113
00:07:56,280 --> 00:07:56,790
Perfect
113

114
00:08:00,550 --> 00:08:01,140
I think.
114

115
00:08:01,330 --> 00:08:06,630
their is CSRF weak protection on adding PayPal at the payment provider with the protection is not good.
115

116
00:08:06,640 --> 00:08:07,520
Okay.
116

117
00:08:07,570 --> 00:08:14,800
So basically this user was able to do a CSRF and this was the bounty provided by Shopify.
117

118
00:08:15,910 --> 00:08:22,690
So I hope you guys understood that how we can try to hunt for when vulnerabilities on hacker when this was
118

119
00:08:23,620 --> 00:08:28,900
a brief overview of the hackerone platform and wherein you can try to hunt for vulnerabilities.
119

120
00:08:28,960 --> 00:08:36,020
This is again the dark more as we already see it you can utilize working at night.
120

121
00:08:36,290 --> 00:08:36,580
Yeah.
121

122
00:08:36,640 --> 00:08:37,630
So this is it.
122

123
00:08:37,660 --> 00:08:43,630
This is basically whatever important things that you need to keep in your mind when you are starting
123

124
00:08:43,630 --> 00:08:45,750
hunting on hacker one platform.
124

125
00:08:46,630 --> 00:08:52,630
So I hope this video helps you guys and you guys can start hunting on this platform.
125

126
00:08:53,440 --> 00:08:54,280
Thank you so much.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,660 --> 00:00:02,010
Hello everyone.
1

2
00:00:02,010 --> 00:00:10,200
So in this video we are going to see how we can start hunting on open bug bounty platform.
2

3
00:00:10,200 --> 00:00:15,350
So this is this video is basically about the roadmap on this platform.
3

4
00:00:15,450 --> 00:00:17,080
So let's start.
4

5
00:00:17,130 --> 00:00:22,940
So you just have to open this URL that is open bug bounty .-- into your browser.
5

6
00:00:23,580 --> 00:00:27,360
And after opening this website will look somewhat like this
6

7
00:00:33,960 --> 00:00:35,220
and yeah.
7

8
00:00:35,280 --> 00:00:39,420
So it looks like this I will just go to the vulnerability.
8

9
00:00:39,600 --> 00:00:43,260
You just have to remember guys to hunt on this platform.
9

10
00:00:43,260 --> 00:00:49,270
You should have a valid Twitter account and you need to log in using Twitter only.
10

11
00:00:49,320 --> 00:00:55,390
So yeah I have a Twitter account so I'm just going to sign it with my Twitter account over here.
11

12
00:00:56,280 --> 00:00:58,260
So I will click on authorize
12

13
00:01:03,830 --> 00:01:04,100
yes.
13

14
00:01:04,100 --> 00:01:07,310
So now I'm currently logged in into the application.
14

15
00:01:07,340 --> 00:01:13,400
I will just click on report vulnerability again and again see coordinated and responsible when vulnerability
15

16
00:01:13,430 --> 00:01:15,170
disclosure.
16

17
00:01:15,170 --> 00:01:15,700
Perfect.
17

18
00:01:15,710 --> 00:01:24,140
I will just quickly click on I agree with the above mentioned ethics guidelines and in the vulnerability
18

19
00:01:24,140 --> 00:01:28,510
detailed section I'm going to choose the one liability that I have found out.
19

20
00:01:28,550 --> 00:01:29,870
So let's say XSS.
20

21
00:01:30,530 --> 00:01:34,480
So yeah you can choose XSS CSRF anything.
21

22
00:01:34,490 --> 00:01:36,690
So I'm going to choose XSS.
22

23
00:01:36,860 --> 00:01:42,880
And in the XSS URL you have to give which website and which end point you've found the XSS
23

24
00:01:42,930 --> 00:01:51,290
for let's say https //example.com/parameter equals to XSS.
24

25
00:01:51,290 --> 00:01:57,530
Let's say this is the injection point in the post data you can just give the data from burp suit the
25

26
00:01:57,530 --> 00:02:04,370
post request which leads to this XSS.
26

27
00:02:04,400 --> 00:02:04,740
Okay.
27

28
00:02:04,760 --> 00:02:12,770
So perfect cookies if it is an authenticated one you can give your session cookies and in the application
28

29
00:02:12,770 --> 00:02:15,470
you just have to choose custom food that's it.
29

30
00:02:15,650 --> 00:02:21,610
And in the comment section you have to write the steps to reproduce so you can just type step one.
30

31
00:02:22,280 --> 00:02:31,220
Go to this URL step 2 hit enter into your browser and you'll be able to see an XSS alert executes
31

32
00:02:31,460 --> 00:02:37,930
which confirms that there is an XSS vulnerability ,you have to click on all of this.
32

33
00:02:37,940 --> 00:02:41,860
Basically check box everything and you have to click on submit.
33

34
00:02:44,030 --> 00:02:52,790
So after you click on submit your vulnerability report will be submitted to open bug bounty.
34

35
00:02:52,790 --> 00:02:53,450
So as you can see.
35

36
00:02:53,480 --> 00:02:54,140
Thank you.
36

37
00:02:54,140 --> 00:02:56,710
Public vulnerability submission will be verified soon.
37

38
00:02:57,230 --> 00:02:59,210
So my report has been submitted.
38

39
00:02:59,390 --> 00:03:05,590
Obviously this is a blank report which I submitted to demonstrate to you guys.
39

40
00:03:06,290 --> 00:03:08,950
And you can see I.D. has been assigned.
40

41
00:03:08,960 --> 00:03:18,710
That is 1 1 4 6 7 9 5 I.D. to this report submission date status spending and yeah basically this report
41

42
00:03:18,950 --> 00:03:23,970
is will be verified and it will go in with it.
42

43
00:03:24,070 --> 00:03:33,650
If it is a valid vulnerability is going to go into this on on hold section over here if it is not a
43

44
00:03:33,650 --> 00:03:36,530
valid report it is going to go in rejected submissions
44

45
00:03:42,210 --> 00:03:44,050
this are some blog post which you can read.
45

46
00:03:44,070 --> 00:03:47,190
People keep writing about the vulnerabilities that they find
46

47
00:03:50,100 --> 00:03:51,920
in the researcher account settings.
47

48
00:03:51,940 --> 00:03:54,670
Guys you can see you can keep your profile settings.
48

49
00:03:54,870 --> 00:03:59,670
You can write your intro how to contact  your contacts certifications if any.
49

50
00:04:00,240 --> 00:04:04,260
And hall of famers if you have done any and you can just save this profile
50

51
00:04:07,500 --> 00:04:09,030
so very simple.
51

52
00:04:12,060 --> 00:04:14,720
Functionality over this open.
52

53
00:04:14,720 --> 00:04:15,180
Bug bounty.
53

54
00:04:15,180 --> 00:04:16,970
platform. 
54

55
00:04:16,980 --> 00:04:21,740
It is very simple and very convenient to report vulnerabilities.
55

56
00:04:21,790 --> 00:04:28,620
Now one most important thing to remember guys in open book bounty it is not like programs or anything
56

57
00:04:29,160 --> 00:04:34,490
like we saw in hacker one bug crowd ,in open bug bounty.
57

58
00:04:34,500 --> 00:04:41,280
This is basically by open source community which means you can try to report any vulnerability that
58

59
00:04:41,280 --> 00:04:43,470
you find onto the Internet.
59

60
00:04:43,470 --> 00:04:51,210
So any vulnerability into any application of any country you can report that valid bug over here.
60

61
00:04:52,410 --> 00:05:00,210
Okay so there is a lot of big scope of you reporting valid vulnerabilities on OBB platforms because
61

62
00:05:00,210 --> 00:05:09,360
there are millions and millions of websites and you can just test them make them your testing playground.
62

63
00:05:09,360 --> 00:05:15,450
But remember Do not do any types of intrusive testing or any misuse of the data.
63

64
00:05:15,600 --> 00:05:20,440
If you have found a valid vulnerability on any website just try to report it over here.
64

65
00:05:20,640 --> 00:05:26,970
After reporting that vulnerability over your open bug bounty researchers team will try to connect with
65

66
00:05:26,970 --> 00:05:36,120
that program or that company and they will try to fix it after fixing those people will get in touch
66

67
00:05:36,120 --> 00:05:43,490
with you and they're going to reward you with some swag or Hall of Fame or maybe rewards.
67

68
00:05:43,890 --> 00:05:46,180
It depends on the company.
68

69
00:05:46,380 --> 00:05:54,390
If I go to my dashboard as you can see whatever I have done over the years so this is the first thing
69

70
00:05:54,420 --> 00:05:59,830
I'll go into a recommendation if anyone gives you a recommendation and it comes over here badges.
70

71
00:05:59,850 --> 00:06:04,950
If you own any badge so as you can see the first badges for 10 plus websites.
71

72
00:06:04,980 --> 00:06:09,230
Second best is for 50 plus 500 plus websites.
72

73
00:06:09,240 --> 00:06:14,290
If you report valid vulnerabilities last is 1000 plus.
73

74
00:06:14,610 --> 00:06:17,760
Similarly there are a lot of bad badges which can unlock.
74

75
00:06:17,790 --> 00:06:25,800
I have unlock one blog author batch which I wrote a year ago.
75

76
00:06:25,800 --> 00:06:27,620
OK so you can earn your badges.
76

77
00:06:27,630 --> 00:06:36,380
Statistics you can see whenever you are hunting blog you can write and you can read blogs perfect.
77

78
00:06:36,530 --> 00:06:38,670
So I hope you guys understood this.
78

79
00:06:38,680 --> 00:06:43,850
Let us go in the Hall of Fame top security researcher and see the top record security researchers list
79

80
00:06:44,430 --> 00:06:54,980
you can see as this research at risk with this calvin has helped in patching 1 7 4 1 6 programs so he
80

81
00:06:54,980 --> 00:06:57,190
has submitted those many reports.
81

82
00:06:57,360 --> 00:07:06,360
Let's go to the profile and you can see researcher reputation is this much fixed these many websites in the
82

83
00:07:06,360 --> 00:07:13,670
certificate you can see open bug bounty has given an outstanding research or certificate to this user
83

84
00:07:14,090 --> 00:07:23,480
because the user has submitted a lot of reports and help to fix a lot of vulnerabilities you guys can
84

85
00:07:23,630 --> 00:07:30,110
also get the certificate by reporting valid vulnerabilities for around 50 to 100 and you will also get
85

86
00:07:30,140 --> 00:07:30,980
a certification
86

87
00:07:34,440 --> 00:07:42,060
perfect you can see what are the reported vulnerabilities by this user is also.
87

88
00:07:42,960 --> 00:07:45,300
So yeah this is it.
88

89
00:07:45,300 --> 00:07:52,590
I hope you guys understood how we can create an account on this website and we can start our bug bounty
89

90
00:07:52,590 --> 00:07:55,440
hunting journey onto this platform.
90

91
00:07:55,440 --> 00:07:56,720
I hope this helps.
91

92
00:07:56,730 --> 00:07:57,480
Thank you guys.
92

93
00:07:58,110 --> 00:07:58,880
Thank you so much.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,470 --> 00:00:02,970
Hello everyone.
1

2
00:00:02,970 --> 00:00:12,220
So in this video we're going to see bug bounty reporting on NCIIPC.
2

3
00:00:12,420 --> 00:00:19,650
So basically NCIIPC is a unit of NTRO that is national technical research organization.
3

4
00:00:19,650 --> 00:00:20,670
Government of India.
4

5
00:00:21,480 --> 00:00:31,590
So this is an initiative by Government of India wherein security researchers from India as well as world
5

6
00:00:32,100 --> 00:00:41,610
can report valid security vulnerabilities to NCIIPC and can contribute in making India's critical
6

7
00:00:41,610 --> 00:00:44,440
infrastructure safe.
7

8
00:00:44,460 --> 00:00:54,720
So if you're able to find any valid vulnerability into any critical infrastructure or any government
8

9
00:00:54,740 --> 00:01:00,740
website then you can report to NCIIPC based on your report.
9

10
00:01:00,780 --> 00:01:08,500
They will verify and they will acknowledge you if you have sended a right report or not if you have sent
10

11
00:01:08,500 --> 00:01:12,780
it a valid report they will acknowledge you with appreciation.
11

12
00:01:14,490 --> 00:01:23,290
So NCIIPC is a important part for reporting vulnerabilities to secure our nation.
12

13
00:01:23,310 --> 00:01:24,230
So let's see this.
13

14
00:01:24,360 --> 00:01:27,130
How can we do this.
14

15
00:01:27,240 --> 00:01:36,230
So you just have to type NCIIPC.GOV.IN  to log onto this website after logging
15

16
00:01:36,230 --> 00:01:37,720
in onto this website.
16

17
00:01:37,770 --> 00:01:43,610
You just have to scroll down you can read about the mission and everything.
17

18
00:01:43,620 --> 00:01:50,490
These are the newsletters we are going to go and newsletter and we are going to see what is newsletters.
18

19
00:01:50,490 --> 00:01:57,760
These are the updates that keep on giving on Twitter vulnerability disclosure wherein we can send a
19

20
00:01:57,760 --> 00:01:58,900
report.
20

21
00:01:58,950 --> 00:02:04,830
If you see at the bottom of the page vulnerability disclosure they have given an email address that is
21

22
00:02:04,890 --> 00:02:09,190
rvdp at NCIIPC.GOV.IN.
22

23
00:02:09,200 --> 00:02:16,920
And so this is the email address where we are going to send all of our security reports any vulnerability
23

24
00:02:16,950 --> 00:02:25,220
that you find in the application of any government website needs to be sent it over here.
24

25
00:02:25,230 --> 00:02:25,790
Perfect.
25

26
00:02:25,800 --> 00:02:34,020
So I am just going to share our report which was shared to NCIIPC by my student.
26

27
00:02:34,020 --> 00:02:41,790
So this report was XSS vulnerability in worldfoodindia.gov.in so now we will see
27

28
00:02:41,940 --> 00:02:47,850
how to write an email to report to them as well as how to write a good report.
28

29
00:02:47,850 --> 00:02:52,960
And what are the important steps your report should cover and not miss.
29

30
00:02:52,980 --> 00:03:02,010
So as you can see the subject line should contain the responsible discourse report as
30

31
00:03:02,010 --> 00:03:09,240
well as the subject line should contain what is the vulnerability and in what website you have found this
31

32
00:03:09,240 --> 00:03:09,960
vulnerability
32

33
00:03:13,090 --> 00:03:23,950
this report needs to be sent it to rvdp as you can see this is the body and this is a report which
33

34
00:03:23,950 --> 00:03:25,250
was attached.
34

35
00:03:25,300 --> 00:03:29,740
So as you can see in this report there is a summary of XSS.
35

36
00:03:29,740 --> 00:03:40,250
So basically what is xss and description of xss is the severity as high as you can see.
36

37
00:03:41,050 --> 00:03:42,950
And next is the payload.
37

38
00:03:43,150 --> 00:03:50,560
So what is the payload that is allowing us to trigger the xss we can see an interesting payload
38

39
00:03:50,560 --> 00:03:55,040
to bypass LTTE which is a html encoding complexity.
39

40
00:03:55,060 --> 00:03:55,950
Easy.
40

41
00:03:56,050 --> 00:03:58,890
We have done this attack from remote external.
41

42
00:03:59,230 --> 00:04:01,610
What is the impact.
42

43
00:04:01,810 --> 00:04:04,760
What are the affected IP's it is worldforindia.gov.in.
43

44
00:04:04,780 --> 00:04:09,580
the URL itself what are the recommendations.
44

45
00:04:09,580 --> 00:04:11,620
And lastly what are the references
45

46
00:04:15,760 --> 00:04:16,640
perfect.
46

47
00:04:16,690 --> 00:04:21,760
So as you can see or what year these things should be included into our report.
47

48
00:04:21,760 --> 00:04:30,400
Do not worry I'm going to share this report template into the description so you guys can also utilize
48

49
00:04:30,430 --> 00:04:31,990
this report.
49

50
00:04:32,260 --> 00:04:40,030
Now the most important part is the proof of concept as you can see this is the POC which shows that
50

51
00:04:40,120 --> 00:04:42,950
xss happened over here.
51

52
00:04:43,840 --> 00:04:49,060
The figure number xss alert on host a website application.
52

53
00:04:49,280 --> 00:04:53,170
The payload again which cost the xss to happen.
53

54
00:04:58,050 --> 00:05:00,960
again a POC from the source code.
54

55
00:05:01,320 --> 00:05:03,180
And again the same payload.
55

56
00:05:05,040 --> 00:05:11,370
So I hope you guys understood how you can write a good report which contains all this necessary information
56

57
00:05:11,730 --> 00:05:19,820
that needs to be sent it to this email address and the email address is rvdp@
57

58
00:05:19,820 --> 00:05:26,730
NCIIPC.gov.in so you need to shoot the email to this security email
58

59
00:05:40,780 --> 00:05:41,680
Yeah.
59

60
00:05:42,180 --> 00:05:49,260
So when you have sent the email to them they will acknowledge you into 24 hours.
60

61
00:05:49,260 --> 00:05:58,020
Based on your report they will tell that it is a valid report or invalid report.
61

62
00:05:58,030 --> 00:06:04,650
Now let's go to the nciipc page and you're in an interesting thing is the newsletters so I'm
62

63
00:06:04,650 --> 00:06:09,770
just going to click the April 2020 newsletter which is the latest newsletter.
63

64
00:06:10,860 --> 00:06:20,070
So whenever security researchers report vulnerabilities to nciipc they release a newsletter every
64

65
00:06:20,070 --> 00:06:27,690
quarter that is three months in every three months and the list down the top security researchers of
65

66
00:06:27,690 --> 00:06:33,710
the country who have sent a valid report.
66

67
00:06:33,840 --> 00:06:40,980
The maximum valid reports that you sent increases the chances of your name to appear into this newsletter
67

68
00:06:41,250 --> 00:06:44,080
and to the top security researchers report.
68

69
00:06:44,970 --> 00:06:54,840
So as you can see this is the report I will just scroll down you can read many things from your articles
69

70
00:06:54,840 --> 00:06:55,590
and news.
70

71
00:06:55,710 --> 00:07:03,870
So basically I will come down to nciipc responsible vulnerability disclosure program over here.
71

72
00:07:03,900 --> 00:07:08,090
You can see the name that is Karthik.
72

73
00:07:08,340 --> 00:07:15,180
So these are the top 15 security researchers and they acknowledged them for the contributions during
73

74
00:07:15,180 --> 00:07:18,730
December 2019 to February 2020.
74

75
00:07:18,750 --> 00:07:20,500
Perfect.
75

76
00:07:20,640 --> 00:07:29,920
So the first student this is my student whom I have trained has been appeared into nciipc newsletter.
76

77
00:07:30,000 --> 00:07:32,600
This is the second student which is riddhi savla.
77

78
00:07:33,450 --> 00:07:41,190
Again I have trained her who has appeared into the newsletter and there is one more student.
78

79
00:07:41,400 --> 00:07:42,670
She is dhruvi mistry.
79

80
00:07:42,690 --> 00:07:50,340
I have trained her to for bug bounty hunting and these three students have been introduced into the
80

81
00:07:50,340 --> 00:07:54,860
top 15 security researchers.
81

82
00:07:54,960 --> 00:08:01,350
Similarly if you see the other newsletters also my students have been into top 15 security researchers
82

83
00:08:01,890 --> 00:08:04,080
newsletter lists thrice
83

84
00:08:07,230 --> 00:08:15,210
so I hope you guys understood how you can report vulnerabilities to nciipc how they will acknowledge
84

85
00:08:15,210 --> 00:08:22,560
you how you can write a good report and how you can see your name into the newsletter so I hope you
85

86
00:08:22,560 --> 00:08:24,350
guys understood.
86

87
00:08:24,420 --> 00:08:24,950
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:01,980 --> 00:00:03,980
Hello everyone.
1

2
00:00:03,990 --> 00:00:14,730
So in this video we are going to see the road map to report one vulnerabilities to all the responsible disclosure
2

3
00:00:14,730 --> 00:00:17,130
programs in the world.
3

4
00:00:17,280 --> 00:00:24,960
So there are many programs which are not listed on bugcrowd  as well as hackerone but they are running
4

5
00:00:25,020 --> 00:00:34,410
their own private programs which are also known as responsible disclosures so you can report vulnerabilities
5

6
00:00:34,410 --> 00:00:35,970
to them.
6

7
00:00:36,030 --> 00:00:42,860
Now how to identify which programs are running their private vulnerabilities disclosure programs.
7

8
00:00:43,020 --> 00:00:46,380
So to make your work more easier.
8

9
00:00:46,710 --> 00:00:53,520
I have hosted a GitHub repo onto my account which is this account as you can see.
9

10
00:00:53,520 --> 00:00:59,260
shifa123 bug bounty dorks  so you can just navigate over here.
10

11
00:00:59,670 --> 00:01:02,610
And after navigating over here you can just
11

12
00:01:07,450 --> 00:01:09,190
as you can see this as the account name.
12

13
00:01:09,190 --> 00:01:11,380
This is the repo that I have made.
13

14
00:01:11,560 --> 00:01:17,890
Just click on that repo name and you can see this report contains all the bug bounty docs sourced from
14

15
00:01:17,890 --> 00:01:21,490
different awesome sources and compiled at one place.
15

16
00:01:21,490 --> 00:01:30,760
So I will just click on B B dorks that is bug bounty dorks and again see there are 66 bug bounty dorks
16

17
00:01:31,030 --> 00:01:33,970
for finding different different types of programs.
17

18
00:01:35,440 --> 00:01:42,370
So I'm just going to take one of the dorks and going to explain you how you can identify different different
18

19
00:01:42,370 --> 00:01:45,650
types of private programs by modifying this dorks.
19

20
00:01:46,390 --> 00:01:50,010
So let me just copy this dork and let me just go
20

21
00:01:57,070 --> 00:02:00,330
over here and you can see.
21

22
00:02:00,490 --> 00:02:05,050
So I have pasted this dork into, I'm sorry
22

23
00:02:07,730 --> 00:02:09,000
let me just
23

24
00:02:19,200 --> 00:02:23,610
let's continue.
24

25
00:02:23,770 --> 00:02:30,690
So as you can see I have entered the dork and I'm yet getting valid programs based for those dorks.
25

26
00:02:30,970 --> 00:02:34,960
As you can see all these companies have their responsible disclosure programs.
26

27
00:02:37,630 --> 00:02:44,860
Yes, so let me just open one of the program that is Nykaa.
27

28
00:02:45,280 --> 00:02:47,400
As you can see I under this program right now.
28

29
00:02:47,500 --> 00:02:52,740
Nykaa responsible disclosure policy.
29

30
00:02:52,750 --> 00:02:58,410
We can see you can e-mail your findings at it-security@nykaa.com
30

31
00:02:58,420 --> 00:03:04,030
These are the researchers who have made recent contributions in 2020.
31

32
00:03:04,030 --> 00:03:04,510
Perfect
32

33
00:03:07,290 --> 00:03:16,920
so if you find anyone vulnerability  into Nykaa you can report to them and they will award you that certificate
33

34
00:03:16,920 --> 00:03:19,540
letter appreciation or a reward.
34

35
00:03:22,560 --> 00:03:26,600
Similarly you can report on a lot of website.
35

36
00:03:26,610 --> 00:03:27,090
So what.
36

37
00:03:27,090 --> 00:03:34,680
I'm just going to do is I'll go to the next second page next page and I will show you there are more
37

38
00:03:34,680 --> 00:03:39,030
dorks basically more programs where you can report.
38

39
00:03:39,030 --> 00:03:47,100
Let me just modify this ".com" to ".nl"and it is basically Netherlands so you will get all the bug bounty
39

40
00:03:47,100 --> 00:03:58,470
programs of Netherlands as you can surf.nl revnext.nl Internet.nl pggm.nl and ziver.eu
40

41
00:03:58,500 --> 00:03:59,230
dot
41

42
00:03:59,490 --> 00:04:01,620
vicompany.nl
42

43
00:04:01,810 --> 00:04:11,310
wefact.nl , Similarly you can modify this to EU and you will get programs of EU that is Europe.
43

44
00:04:11,910 --> 00:04:12,360
Perfect.
44

45
00:04:12,480 --> 00:04:19,320
So you can keep on modifying this to different countries countries top level domains and you will find
45

46
00:04:19,320 --> 00:04:23,860
programs for different different countries.
46

47
00:04:24,030 --> 00:04:28,380
So the possibilities are endless.
47

48
00:04:28,440 --> 00:04:33,150
You will find a lot of bug bounty private programs.
48

49
00:04:33,150 --> 00:04:36,510
There is no limit to report vulnerabilities.
49

50
00:04:36,570 --> 00:04:39,440
There is no limit to find targets.
50

51
00:04:39,450 --> 00:04:47,820
So if you hunting on bugcrowd and hackerone and open bug bounty you can also keep this as one of the
51

52
00:04:47,820 --> 00:04:51,390
option very you can send report to private programs.
52

53
00:04:51,420 --> 00:04:51,900
also
53

54
00:04:54,540 --> 00:05:01,560
similarly you guys can take another bug bounty dorks from here as you can see submit vulnerability report
54

55
00:05:01,680 --> 00:05:09,530
to let me just open this and you can see camcard.com submit vulnerability report  companyhub, punch security, oppo security
55

56
00:05:09,560 --> 00:05:16,790
security.she in td.com,Tencent.
56

57
00:05:17,610 --> 00:05:19,090
Let's go to the next page.
57

58
00:05:19,140 --> 00:05:24,000
As you can see security.alibaba and so on.
58

59
00:05:24,240 --> 00:05:30,240
So there are unlimited programs wherein you can report vulnerabilities.
59

60
00:05:30,460 --> 00:05:31,160
That's perfect.
60

61
00:05:31,650 --> 00:05:40,590
So these are called as responsible vulnerability disclosure programs RVDP wherein you can send
61

62
00:05:40,590 --> 00:05:41,700
reports to them.
62

63
00:05:46,910 --> 00:05:51,170
So I hope you guys understood how you can send reports to private.
63

64
00:05:51,180 --> 00:05:59,220
Are RVDP programs the report format is already been shown into the video and has been shared in the
64

65
00:05:59,290 --> 00:06:06,300
in the previous video and it's been shared with you that how we send the report to our RVDP you can utilize
65

66
00:06:06,300 --> 00:06:12,870
that template to make a report and you can and you can submit your report to these are RVDP programs
66

67
00:06:12,900 --> 00:06:13,430
also.
67

68
00:06:14,320 --> 00:06:20,260
So I hope you guys understood and this video may help you in sending more and more report to RVDP
68

69
00:06:20,310 --> 00:06:22,530
private programs.
69

70
00:06:22,530 --> 00:06:23,010
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 7: Exploitation of CVE 2020-5902 Remote Code Execution

0
1
00:00:00,240 --> 00:00:01,950
Hello and welcome, everyone.
1

2
00:00:02,040 --> 00:00:10,950
So we are here with the latest exploit, which has been circulating everywhere on the Internet, everywhere
2

3
00:00:10,950 --> 00:00:14,440
on Twitter and in all the platforms.
3

4
00:00:14,460 --> 00:00:20,190
People are just talking about the latest exploit, which is a CVE twenty twenty five nine zero two.
4

5
00:00:20,820 --> 00:00:28,470
So this is a particular remote code execution exploit, which has been found out for the big IP f5
5

6
00:00:28,470 --> 00:00:29,070
servers.
6

7
00:00:29,280 --> 00:00:32,670
And most of the servers are vulnerablel to this particular exploit.
7

8
00:00:33,720 --> 00:00:39,360
So in this video, we are going to see how you can utilize this particular ovulnerability of remote
8

9
00:00:39,360 --> 00:00:43,200
code execution for fun and profit for your bug bounties.
9

10
00:00:43,590 --> 00:00:45,450
So let's quickly get started.
10

11
00:00:46,830 --> 00:00:55,050
So you can see f5 Networks gave a tweet which said Big IP traffic management, user interface,
11

12
00:00:55,080 --> 00:00:59,750
that is tmui has a remote code execution vulnerability in its undisclosed pages.
12

13
00:00:59,820 --> 00:01:02,250
So this tweet was on July 3rd.
13

14
00:01:03,300 --> 00:01:09,480
Officially, they were tweeted they tweeted that they vulnerable to this particular vulnerability
14

15
00:01:09,510 --> 00:01:11,170
which was a dangerous one.
15

16
00:01:11,280 --> 00:01:13,050
And it was a remote code execution.
16

17
00:01:14,040 --> 00:01:14,460
So.
17

18
00:01:15,390 --> 00:01:16,140
There were.
18

19
00:01:17,570 --> 00:01:22,070
The big IP exploits started circulating over the Internet.
19

20
00:01:22,160 --> 00:01:26,090
And here are some of the exploits that we have collected.
20

21
00:01:26,720 --> 00:01:32,990
And we saw that researchers are using this particular exploit to attack the target.
21

22
00:01:33,800 --> 00:01:37,800
As you can see, or here, if you see the exploit, the exploit is pretty simple, wherein.
22

23
00:01:38,480 --> 00:01:42,720
This is the particular host and Tmui that we saw.
23

24
00:01:42,830 --> 00:01:49,040
And this is the particular file.read.jsp Endpoint where in the filename can easily be read.
24

25
00:01:49,850 --> 00:01:55,350
So this was these configurations in which we can also read the big IP configuration that has been set
25

26
00:01:55,350 --> 00:01:56,900
it up onto the target server.
26

27
00:01:58,010 --> 00:01:58,330
All right.
27

28
00:01:58,400 --> 00:02:01,430
So there was again and nmap exploits out there.
28

29
00:02:02,110 --> 00:02:07,580
And we can use that particular nmap exploit to identify if that particular target is vulnerable to
29

30
00:02:07,580 --> 00:02:12,070
this particular exploit that is five nine zero two.
30

31
00:02:13,670 --> 00:02:20,000
So as you can see in the screenshot, if we scan that particular target using this particular exploit
31

32
00:02:20,060 --> 00:02:25,910
nse, then we will come to know, OK, that target is vulnerable to the big 
32

33
00:02:25,940 --> 00:02:27,980
IP tmui vulnerability
33

34
00:02:30,240 --> 00:02:38,370
We can also do curl and identify if the target is a vulnerable so you can see on the screen we are using
34

35
00:02:38,370 --> 00:02:38,980
the curl.
35

36
00:02:39,390 --> 00:02:46,790
Particular command and the particular request that we are sending to the target within the perimeter
36

37
00:02:46,800 --> 00:02:53,670
file name is being given the etc passwd path wherein we will get that particular file.
37

38
00:02:54,320 --> 00:02:54,770
All right.
38

39
00:02:55,050 --> 00:02:57,280
So we can do it using curl  as well.
39

40
00:02:59,010 --> 00:02:59,220
Yeah.
40

41
00:02:59,400 --> 00:03:06,420
So Nuclei Team, the Project Discovery team, has also released the template for identifying this
41

42
00:03:06,420 --> 00:03:07,450
particular exploit.
42

43
00:03:07,510 --> 00:03:08,880
which is a very awesome.
43

44
00:03:08,930 --> 00:03:14,160
I've also given the source you can download from there and you can identify if it is vulnerable to that
44

45
00:03:14,160 --> 00:03:16,080
particular exploit.
45

46
00:03:16,200 --> 00:03:24,900
So this particular nuclei template helps to identify based on the previous slides that we have seen.
46

47
00:03:24,990 --> 00:03:28,800
It is the same actually the same payload that that has been sent.
47

48
00:03:28,830 --> 00:03:30,600
at the bottom over here.
48

49
00:03:30,630 --> 00:03:31,880
And it identifies that.
49

50
00:03:31,980 --> 00:03:33,570
Is it vulnerable or not?
50

51
00:03:34,920 --> 00:03:43,230
So on Twitter, nahamsec has tweeted that he finally got some working poc for CVE 2020
51

52
00:03:43,230 --> 00:03:43,450
5902
52

53
00:03:43,660 --> 00:03:51,960
So people have already started using this particular exploit for their bug bounties for fun and for
53

54
00:03:51,960 --> 00:03:52,500
profit.
54

55
00:03:52,800 --> 00:04:01,080
So we will see how we can also utilize this particular exploit to find a high value target and get.
55

56
00:04:02,010 --> 00:04:04,800
Something which is very, very sensitive over there.
56

57
00:04:06,090 --> 00:04:10,890
All right, so poc demo was given by a researcher.
57

58
00:04:10,950 --> 00:04:18,540
So let me just play this particular pocy for you, wherein you can see that he was able to do this,
58

59
00:04:18,540 --> 00:04:22,050
find this particular exploit over there.
59

60
00:04:22,110 --> 00:04:22,830
As you can see.
60

61
00:04:22,980 --> 00:04:24,780
But he has blurred the payload.
61

62
00:04:24,810 --> 00:04:24,920
OK.
62

63
00:04:24,990 --> 00:04:30,180
So we cannot see the payload, but he can see the output that we have got from that particular server.
63

64
00:04:30,920 --> 00:04:31,300
All right.
64

65
00:04:31,530 --> 00:04:34,020
So now not so blurred payload.
65

66
00:04:34,410 --> 00:04:39,360
So we have actually got the payload and the payload that works currently.
66

67
00:04:39,360 --> 00:04:45,210
Is this very you can use the curl payload, and the read file request as well.
67

68
00:04:45,260 --> 00:04:49,290
Well, then you can read the etc passwd path
68

69
00:04:49,650 --> 00:04:57,780
The above code gives the list of the art user admins rules, as you saw, into the previous blurred
69

70
00:04:59,850 --> 00:05:00,440
Poc
70

71
00:05:00,860 --> 00:05:01,170
All right.
71

72
00:05:01,230 --> 00:05:02,380
So testing them.
72

73
00:05:03,330 --> 00:05:07,740
This is the website where you can just simply go and test if it is vulnerable or not.
73

74
00:05:08,070 --> 00:05:09,820
And we can also do the automation.
74

75
00:05:09,870 --> 00:05:13,050
So I have created a exploit poc scenario.
75

76
00:05:13,440 --> 00:05:14,230
So let us see.
76

77
00:05:14,300 --> 00:05:16,620
Quickly and practical.
77

78
00:05:16,680 --> 00:05:18,720
A lot of theory and tocking has been done.
78

79
00:05:18,850 --> 00:05:20,910
Now, let's quickly jump onto the practical.
79

80
00:05:21,390 --> 00:05:26,950
So you can see I have taken this IP, which is 40.67.185.184
80

81
00:05:27,030 --> 00:05:31,450
And this IP, I, I've done a host and this IP belongs to Microsoft Corporation.
81

82
00:05:32,530 --> 00:05:32,800
All right.
82

83
00:05:32,880 --> 00:05:37,740
So what I'm going to do is I'm going to identify if this IP is vulnerable  to this particular attack or
83

84
00:05:37,740 --> 00:05:38,100
not.
84

85
00:05:38,910 --> 00:05:44,010
So what I'm going to do is I am going to run a nmap scan.
85

86
00:05:44,090 --> 00:05:44,300
Okay.
86

87
00:05:44,640 --> 00:05:52,530
So I will just run and nmap scans so nmap --script to this particular IP, let's say on port four, four,
87

88
00:05:52,530 --> 00:05:53,040
three.
88

89
00:05:53,100 --> 00:05:56,650
And let's see the output in verbose mode.
89

90
00:05:57,510 --> 00:05:58,980
The script name we have to give.
90

91
00:05:59,010 --> 00:06:00,960
So the script name is http
91

92
00:06:04,970 --> 00:06:05,190
OK.
92

93
00:06:05,490 --> 00:06:14,910
So just a second, let us go into the path where the script is there so you need to desktop work courses.
93

94
00:06:15,880 --> 00:06:16,720
udemy
94

95
00:06:18,030 --> 00:06:19,930
And it is you, udemy
95

96
00:06:20,160 --> 00:06:20,840
Come on.
96

97
00:06:20,940 --> 00:06:22,410
Let me just go there.
97

98
00:06:22,600 --> 00:06:22,830
Yeah.
98

99
00:06:23,400 --> 00:06:27,060
So now we're going to run the particular exploit.
99

100
00:06:27,250 --> 00:06:28,260
And yeah.
100

101
00:06:28,380 --> 00:06:28,830
So  here 
101

102
00:06:28,870 --> 00:06:30,460
Is the script that we are going to run.
102

103
00:06:30,930 --> 00:06:31,440
So.
103

104
00:06:31,790 --> 00:06:32,400
And nmap.
104

105
00:06:32,920 --> 00:06:33,330
Hyphen.
105

106
00:06:33,360 --> 00:06:34,500
Hyphen script.
106

107
00:06:37,260 --> 00:06:39,440
And the script named the script name is this.
107

108
00:06:39,480 --> 00:06:41,010
And then the target.
108

109
00:06:41,130 --> 00:06:41,910
What is our target?
109

110
00:06:41,940 --> 00:06:44,010
Our target is this particular IP address.
110

111
00:06:44,040 --> 00:06:45,800
And let's see the output in verbose mode.
111

112
00:06:46,560 --> 00:06:49,210
Let us also give the port number.
112

113
00:06:49,590 --> 00:06:51,360
And we have started the scan.
113

114
00:06:51,810 --> 00:06:53,880
So as you can see over here, we have got the output.
114

115
00:06:53,940 --> 00:07:00,360
And it says a vulnerable   big IP pmuI rce vulnerability exist into this particular server.
115

116
00:07:00,900 --> 00:07:01,290
All right.
116

117
00:07:02,400 --> 00:07:06,540
We can now exploit this and see if we are able to exploit it.
117

118
00:07:06,570 --> 00:07:08,040
But before exploiting.
118

119
00:07:08,100 --> 00:07:12,870
Let me show you some automation that we have done to find out.
119

120
00:07:12,960 --> 00:07:16,760
to fine vulnerable  target automatically from shodan
120

121
00:07:16,800 --> 00:07:22,290
Those who who do not know about shodan, shodan is an Internet connected search engine wherein you can
121

122
00:07:22,650 --> 00:07:27,090
directly see what all devices or servers are exposed.
122

123
00:07:27,300 --> 00:07:29,710
Based on your search queries and filters.
123

124
00:07:30,840 --> 00:07:33,900
So I have added my API key over here.
124

125
00:07:33,990 --> 00:07:36,270
And you can see it is successfully initialized.
125

126
00:07:36,630 --> 00:07:43,530
So after adding the API key, I'm going to use this particular command, which is first we have to install
126

127
00:07:43,530 --> 00:07:46,230
Shodan CLI after you are installed, install it.
127

128
00:07:46,320 --> 00:07:52,910
We have to basically run this command wherein we are going to run a particular search for a filter and
128

129
00:07:52,920 --> 00:07:54,060
for this particular port.
129

130
00:07:54,150 --> 00:07:58,260
And then we are going to get the ip's out from there.
130

131
00:07:58,290 --> 00:08:02,340
And it is going to automatically test for this particular vulnerability
131

132
00:08:02,370 --> 00:08:08,040
As you can see, here and we are going to see the etc passwd. file of these particular ip
132

133
00:08:08,340 --> 00:08:12,870
If the ip is vulnerable   it is just going to print vulnerable   and if it is not vulnerable  , it is going
133

134
00:08:12,870 --> 00:08:14,100
to print not vulnerable.
134

135
00:08:14,520 --> 00:08:19,000
So once we run this, as you can see, we have got a lot of ips.
135

136
00:08:19,050 --> 00:08:21,270
And I just stopped the scan in between.
136

137
00:08:21,690 --> 00:08:24,360
So I got the ip under 30 seconds.
137

138
00:08:24,390 --> 00:08:25,660
These many ip's are vulnerable  
138

139
00:08:25,890 --> 00:08:32,730
From that I have taken IP from here, which is this particular IP and this is the same IP of Microsoft.
139

140
00:08:32,820 --> 00:08:34,070
It is forty sixty seven.
140

141
00:08:34,070 --> 00:08:34,860
One eighty five.
141

142
00:08:34,940 --> 00:08:35,920
One eighty four.
142

143
00:08:36,570 --> 00:08:36,740
Okay.
143

144
00:08:36,950 --> 00:08:37,440
Let us see.
144

145
00:08:37,800 --> 00:08:41,010
So it is the same IP address which belongs to Microsoft.
145

146
00:08:42,820 --> 00:08:43,250
All right.
146

147
00:08:43,290 --> 00:08:46,740
So now let's see if this is a vulnerable  .
147

148
00:08:47,330 --> 00:08:47,480
Yeah.
148

149
00:08:47,550 --> 00:08:49,640
So we have already identified it as vulnerable.
149

150
00:08:49,680 --> 00:08:51,480
And let's try to exploit it.
150

151
00:08:51,600 --> 00:08:54,450
So I have the exploit over here.
151

152
00:08:55,020 --> 00:09:03,030
So after running the exploit, as you can see over here, let me just show you using curl.
152

153
00:09:03,390 --> 00:09:10,740
We have an exploit and we have actually got the output of the etc passwd file, which is actually
153

154
00:09:11,250 --> 00:09:12,420
very, very sensitive.
154

155
00:09:12,540 --> 00:09:19,350
So this particular vulnerability will go into a p1 level because this is a critical vulnerability
155

156
00:09:19,350 --> 00:09:24,780
wherein we are able to see directly the passwd file of the server, which is vulnerable.
156

157
00:09:25,170 --> 00:09:29,580
The best way is to hunt a lot of targets by just running the scan.
157

158
00:09:29,700 --> 00:09:34,650
And after you have run the scan, you will get a lot of high value targets.
158

159
00:09:34,950 --> 00:09:41,760
Once you get those targets, you can just run its HTTP probe or its HTTPX to see which of the ip's
159

160
00:09:41,850 --> 00:09:42,660
are alive.
160

161
00:09:42,720 --> 00:09:45,960
And then you can sort and filter those ip's into a file.
161

162
00:09:46,320 --> 00:09:47,640
After sorting and filtering.
162

163
00:09:47,640 --> 00:09:52,690
You can just run the exploit and check which of which of the ip's are vulnerable.
163

164
00:09:52,830 --> 00:09:57,870
And you can directly start reporting to those particular programs.
164

165
00:09:58,320 --> 00:10:01,320
So this is very, very helpful.
165

166
00:10:01,410 --> 00:10:07,830
If you want to do a mass scan of the Internet of all the APIs which are vulnerable  , and you will be
166

167
00:10:07,830 --> 00:10:11,970
able to report these types of high severity bugs to them.
167

168
00:10:12,540 --> 00:10:15,190
So I hope you guys understood through this particular video.
168

169
00:10:15,950 --> 00:10:18,820
I'm shooting this video in the morning 536.
169

170
00:10:19,020 --> 00:10:19,920
I have not slept.
170

171
00:10:19,980 --> 00:10:27,990
I was just researching about this and I was trying to find out that I should make a exploit video for
171

172
00:10:27,990 --> 00:10:32,430
everyone to understand because this is something which is going on every web.
172

173
00:10:32,520 --> 00:10:35,460
So I hope if you guys understood.
173

174
00:10:35,510 --> 00:10:36,110
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

0
1
00:00:00,420 --> 00:00:01,200
Hello, everyone.
1

2
00:00:01,710 --> 00:00:08,040
So in this video, we are going to see the resources that you can utilize for the attack that we saw
2

3
00:00:08,040 --> 00:00:09,360
into the previous video.
3

4
00:00:10,020 --> 00:00:14,160
There will CVE 2020 five nine zero two big IP attack.
4

5
00:00:15,240 --> 00:00:23,550
So when you will come to this particular repository, I will give the link into the resources section
5

6
00:00:23,550 --> 00:00:24,170
of mean.
6

7
00:00:25,390 --> 00:00:29,940
When you just come out here, you can see the first script is the nmap script.
7

8
00:00:30,570 --> 00:00:33,760
You can download the script using this W8get command.
8

9
00:00:33,870 --> 00:00:36,960
And it will get automatically downloaded into your computer.
9

10
00:00:38,100 --> 00:00:44,160
After that, if you want to check, the particular target is vulnerable, then just to replace the IP
10

11
00:00:44,160 --> 00:00:45,270
address over here.
11

12
00:00:45,750 --> 00:00:51,930
And run this particular nmap script and you will automatically come to know if the target is vulnerable.
12

13
00:00:52,800 --> 00:00:55,860
So this is the host identification part.
13

14
00:00:55,940 --> 00:01:02,490
When you will come to know if the target is a vulnerable   to this particular exploit, then if you want
14

15
00:01:02,490 --> 00:01:07,260
to perform the exploitation, then you have to come over here, which is the curl request.
15

16
00:01:08,160 --> 00:01:15,510
You can fire the first request, which is to read the users and the admin roles that have been given
16

17
00:01:15,720 --> 00:01:18,570
to that particular fibig IP server.
17

18
00:01:19,350 --> 00:01:22,160
If you want to read the passwd file, then you can fire
18

19
00:01:22,290 --> 00:01:28,770
This particular request and you'll be able to read the etc passwd. file of that particular server.
19

20
00:01:29,850 --> 00:01:36,210
Remember, in both the script, you have to change the host over here with the target server IP address,
20

21
00:01:36,300 --> 00:01:39,690
which you have identified to be vulnerable into the first step.
21

22
00:01:41,160 --> 00:01:49,260
And this way you will be able to exploit the particular server which is running and outdated or unpatched
22

23
00:01:49,350 --> 00:01:50,980
big IP server.
23

24
00:01:52,290 --> 00:01:56,940
If you want to automate the whole process, that is the step, number one and step number two.
24

25
00:01:57,420 --> 00:02:03,270
Then you can use this automation shodan script for mass exploitation, as I have used the script into
25

26
00:02:03,270 --> 00:02:06,700
the video for hunting of the targets from Showdown.
26

27
00:02:07,590 --> 00:02:14,850
We can simply use this particular script, which will automatically scrape off for the target based
27

28
00:02:14,880 --> 00:02:16,680
on the search filter, which you have given.
28

29
00:02:17,010 --> 00:02:23,340
So our search filter that is given is this particular search filter, and based on this, it will identify
29

30
00:02:23,940 --> 00:02:31,170
and match this particular hash for the big IP servers as this particular hash is for the big IP servers.
30

31
00:02:31,950 --> 00:02:36,090
And this is the content length that it will try to match into the response.
31

32
00:02:36,480 --> 00:02:42,000
So basically, content length is nothing but the length of the particular response page that we are
32

33
00:02:42,000 --> 00:02:42,680
getting to.
33

34
00:02:42,810 --> 00:02:46,470
This is by default, 392 for the content length.
34

35
00:02:46,500 --> 00:02:50,040
Whenever we try to load a big IP default log in page.
35

36
00:02:50,910 --> 00:02:56,510
This is the particular hash of the big IP server based on this only.
36

37
00:02:56,670 --> 00:03:00,340
We are filtering the target on shoown.
37

38
00:03:00,900 --> 00:03:08,880
So let us just discuss something more about hashes and what how can you identify a favicon hash for
38

39
00:03:08,970 --> 00:03:10,450
any other target?
39

40
00:03:10,530 --> 00:03:11,780
And you can search for a shodan.
40

41
00:03:12,660 --> 00:03:18,750
So first thing first, what is actually very con sometimes also known as a favorite icon.
41

42
00:03:19,290 --> 00:03:23,460
So when you visit any particular Web site, as you can see, what here I am on to Amazon.
42

43
00:03:24,360 --> 00:03:30,840
And when you will just simply write favicon.ico, you'll be able to see the favicon icon
43

44
00:03:30,850 --> 00:03:32,040
or the favorite icon.
44

45
00:03:33,840 --> 00:03:40,470
Now, if you want to search for all the Amazon servers on Shodan, then you can just simply convert
45

46
00:03:40,500 --> 00:03:47,930
the favicon dot icon into a hash and you can use that particular hash to search on the showdown.
46

47
00:03:48,960 --> 00:03:51,960
Now, how to convert this this very, very simple.
47

48
00:03:52,620 --> 00:03:56,990
Just come over to this particular get shodan favicon hash.py script.
48

49
00:03:57,150 --> 00:04:00,960
I will add the script into the resources section as well.
49

50
00:04:02,400 --> 00:04:04,380
So, yeah, there are two scripts.
50

51
00:04:04,530 --> 00:04:08,750
The first is the Python two script for Python, two users.
51

52
00:04:08,820 --> 00:04:12,180
Next is the Python three script, which you can utilize.
52

53
00:04:13,500 --> 00:04:20,220
So now you have to replace your target server, favicon, which you want to convert into hash, and
53

54
00:04:20,220 --> 00:04:22,660
then you can source that hash on to showdown.
54

55
00:04:23,520 --> 00:04:25,560
So first, let's convert a target.
55

56
00:04:25,800 --> 00:04:26,130
Sure.
56

57
00:04:26,160 --> 00:04:27,330
Let me just copy this.
57

58
00:04:27,420 --> 00:04:31,980
First, let me go to the terminal on the terminal.
58

59
00:04:32,100 --> 00:04:36,990
I'm going to first start Python and hit enter.
59

60
00:04:37,910 --> 00:04:43,530
And you can see I have started Python and now I will just paste it and enter.
60

61
00:04:44,190 --> 00:04:50,830
And you can see I'm able to get the hash of this particular server, which is cybersecurity.wtf
61

62
00:04:50,940 --> 00:04:52,120
favicon.ico
62

63
00:04:53,190 --> 00:04:54,450
That is the icon file.
63

64
00:04:54,870 --> 00:04:59,770
Now I can search this particular hash on two shodan and I will get.
64

65
00:04:59,860 --> 00:05:02,990
results for this particular service which have been hosting.
65

66
00:05:03,380 --> 00:05:09,280
So I will just go there to replace this particular server with this particular hash.
66

67
00:05:09,580 --> 00:05:12,430
So this is my search filter that I'm using right now.
67

68
00:05:13,090 --> 00:05:19,080
As you can see, no results found because this is a particular Web site, not our Web server or our
68

69
00:05:19,090 --> 00:05:21,640
application, which other companies uses.
69

70
00:05:22,060 --> 00:05:25,420
That's why we're not getting any results for this particular hash.
70

71
00:05:25,780 --> 00:05:32,770
But you may get the results for if you're using a dedicated server or software like Apache or nginx
71

72
00:05:32,830 --> 00:05:35,410
at that time, you will get a lot of results over here.
72

73
00:05:36,400 --> 00:05:40,770
So I hope you understood how you can use a hash for a search filter.
73

74
00:05:41,740 --> 00:05:47,500
Now, coming back over here, I remembered for doing this particular searches on Shodan.
74

75
00:05:47,770 --> 00:05:54,490
You will be requiring an api key by default if you sign up on showdown with a free account.
75

76
00:05:55,330 --> 00:06:02,500
Then you will get only hundred query credit as well as you can not use these types of advance a search
76

77
00:06:02,510 --> 00:06:05,860
filter to search for their target.
77

78
00:06:06,370 --> 00:06:07,230
Then what?
78

79
00:06:07,240 --> 00:06:09,010
You will not be able to perform the task.
79

80
00:06:09,970 --> 00:06:16,570
So I have a api key, which I'm going to release it as a bonus for everyone.
80

81
00:06:17,260 --> 00:06:22,240
So I have added the api key, which is this particular API key into your terminal.
81

82
00:06:22,540 --> 00:06:28,510
Just install Shodan installing Shodan
82

83
00:06:28,600 --> 00:06:30,460
It's pretty simple for your terminal.
83

84
00:06:30,490 --> 00:06:32,230
Let me show you how you can do that.
84

85
00:06:33,070 --> 00:06:34,660
Let me just clear the screen for you.
85

86
00:06:35,380 --> 00:06:40,420
You can use easy install to install Shodan.
86

87
00:06:41,050 --> 00:06:46,630
Make sure you have python installed into your computer after you have installed python just run 
87

88
00:06:46,690 --> 00:06:50,860
This command, which is easy, underscore, install shodan and hit enter.
88

89
00:06:51,970 --> 00:06:55,420
Now it may give you some error and say your do not have write access.
89

90
00:06:55,660 --> 00:06:58,600
So you just become the root user.
90

91
00:06:58,690 --> 00:07:00,640
Or you can use the command sudo itself as well.
91

92
00:07:01,360 --> 00:07:07,540
So I'm going to run this again and hit Enter is asking me for a password.
92

93
00:07:08,020 --> 00:07:14,030
I will enter and again see best match shodan one point twenty one point 3s, the latest version of Shodan
93

94
00:07:14,110 --> 00:07:16,090
and it is installed into my computer.
94

95
00:07:16,960 --> 00:07:18,790
The second way to install shodan is using pip
95

96
00:07:19,300 --> 00:07:29,140
So you can just type and install and shodan and it enters and you can see here requirement already satisfied.
96

97
00:07:29,170 --> 00:07:32,410
Which means I have already installed shodan in my computer.
97

98
00:07:33,040 --> 00:07:42,520
Let's verify shodan info and you'll be able to see I have this one many query credit available with my
98

99
00:07:42,520 --> 00:07:43,000
account.
99

100
00:07:44,380 --> 00:07:50,650
This is because I'm using a premium account for Shodan and I have also given an api key to every one
100

101
00:07:50,650 --> 00:07:50,980
of you.
101

102
00:07:51,010 --> 00:07:52,890
You can utilize this particular API key.
102

103
00:07:53,630 --> 00:07:55,420
Now how to use this API key.
103

104
00:07:55,540 --> 00:07:56,700
Just copy this particular.
104

105
00:07:56,710 --> 00:08:03,150
Come on, go into your terminal and paste this and hit enter once you will paste enter.
105

106
00:08:03,520 --> 00:08:05,650
You will see successfully initialized.
106

107
00:08:05,920 --> 00:08:11,100
Which means to initialize this particular api key into your terminal.
107

108
00:08:11,380 --> 00:08:16,570
And now you will be able to use a shodan cli which is the command language from here.
108

109
00:08:16,780 --> 00:08:20,780
And you can you will have these many numbers of query credit available.
109

110
00:08:22,870 --> 00:08:26,290
Remember, guys, this is as a bonus, which I'm giving to you.
110

111
00:08:27,760 --> 00:08:35,740
I'm not sure if all the students utilize all the query credits and the creating credits are over I will
111

112
00:08:35,740 --> 00:08:39,580
not be able to give a new api key to every one of you.
112

113
00:08:40,570 --> 00:08:45,340
You can purchase that shodan pro if you want to use short on advanced filters.
113

114
00:08:45,700 --> 00:08:48,080
Or you can just use the free account.
114

115
00:08:49,150 --> 00:08:57,400
So if this particular api key is exhausted with all this query credits, then I will not supply the new
115

116
00:08:57,400 --> 00:08:57,790
api
116

117
00:08:59,200 --> 00:08:59,540
All right.
117

118
00:08:59,650 --> 00:09:03,570
So we have understood how you can use the showdown CLI
118

119
00:09:03,790 --> 00:09:12,040
And how can you initialize and utilize the api key to run and search for advance search filters?
119

120
00:09:13,480 --> 00:09:16,220
So I hope you guys a understood in this particular video.
120

121
00:09:16,270 --> 00:09:21,730
How you can utilize this asset and how you can search for mass targets.
121

122
00:09:23,170 --> 00:09:23,650
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 8: Exploitation of CVE 2020-3452 File Read

0
1
00:00:00,450 --> 00:00:08,960
So in this video, we're going to discuss about the latest exploits of a Cisco, which is the twenty
1

2
00:00:08,960 --> 00:00:13,480
twenty three, four, five, two CVE I.D. which has been assigned.
2

3
00:00:14,370 --> 00:00:22,620
So basically this whole exploit is an arbitrary file read exploit, even though if you're authenticated
3

4
00:00:22,710 --> 00:00:31,230
or an authenticated, which basically means any attacker sitting at any place who does not need to be
4

5
00:00:31,320 --> 00:00:37,770
authenticated with that particular VPN server can read the files from the server.
5

6
00:00:38,820 --> 00:00:43,080
So we are going to discuss about all the CVE 2020 three, four, five, two.
6

7
00:00:43,370 --> 00:00:47,670
Then we are going to exploit some of the targets using a shodan.
7

8
00:00:48,180 --> 00:00:52,380
Then we are going to exploit some targets from subdomain enumeration.
8

9
00:00:53,040 --> 00:00:59,800
Then we are going to see a more arbitrary file read entry point, which will give us more when then
9

10
00:00:59,850 --> 00:01:02,520
we are going to see the nmap NSE detection.
10

11
00:01:03,210 --> 00:01:10,410
Then finally, automation to do hold to do Mass hunting by automating the whole process.
11

12
00:01:10,980 --> 00:01:13,840
Then a final word on this particular venerability.
12

13
00:01:14,160 --> 00:01:18,900
And in case you have any questions, then you can post questions into the Q&A section.
13

14
00:01:19,850 --> 00:01:20,280
All right.
14

15
00:01:20,580 --> 00:01:21,900
So what is a CVE?
15

16
00:01:21,910 --> 00:01:24,240
Twenty twenty three, four, five, two.
16

17
00:01:24,990 --> 00:01:29,160
So according to our advisory, which was released by Cisco.
17

18
00:01:29,460 --> 00:01:39,180
So Cisco Adaptive Security Appliance Software also called as a Cisco ASAand a Firepower Threat Defense
18

19
00:01:39,270 --> 00:01:46,830
software, which is FTD Web service, a read only part traversal vulnerability exist, which has been
19

20
00:01:46,920 --> 00:01:54,720
assigned this CV idee as against you would hear the CVSS score which has been assigned is based score
20

21
00:01:54,720 --> 00:02:00,960
of seven point five, which is again a high, critical, high type of vulnerability.
21

22
00:02:00,990 --> 00:02:04,410
It is not critical until and unless it is more than nine point five.
22

23
00:02:04,500 --> 00:02:04,910
All right.
23

24
00:02:05,370 --> 00:02:12,990
So still, the vulnerability is high because any attacker can read any arbitrary file from that particular
24

25
00:02:12,990 --> 00:02:17,150
server by simply sending a HTTP request.
25

26
00:02:18,000 --> 00:02:18,450
All right.
26

27
00:02:19,110 --> 00:02:20,250
So on.
27

28
00:02:20,370 --> 00:02:22,510
nvd.nist.gov
28

29
00:02:22,650 --> 00:02:26,340
You can see the base code is, again, the same seven point five.
29

30
00:02:26,430 --> 00:02:31,050
And you can see why does he CVSS score is given this particular base score.
30

31
00:02:32,150 --> 00:02:32,550
All right.
31

32
00:02:33,480 --> 00:02:41,450
So now this particular researcher who goes by the name Ahmed has released the first POC within
32

33
00:02:41,470 --> 00:02:42,230
in the POC
33

34
00:02:42,270 --> 00:02:43,380
As you can see.
34

35
00:02:44,910 --> 00:02:52,770
If you craft a special HTTP request and you send it to the particular server and you try to read the
35

36
00:02:52,770 --> 00:02:59,260
particular file, as you can see over here, the file, which has been tried to read is Portal I n c
36

37
00:02:59,280 --> 00:03:00,460
dot, lua
37

38
00:03:00,720 --> 00:03:06,120
So if you're trying to read this particular file, then you can see the output over here.
38

39
00:03:06,180 --> 00:03:10,290
And we are able to read the particular file, which was a portal.
39

40
00:03:10,330 --> 00:03:15,060
I nc, which is one of the configuration file for the server at.
40

41
00:03:16,520 --> 00:03:21,080
Now, this started getting exploited in the wild.
41

42
00:03:21,320 --> 00:03:27,020
And many people started to send this particular vulnerability, as you can see, I have a screenshot,
42

43
00:03:27,410 --> 00:03:32,870
but in this particular researcher was able to send the particular vulnerability
43

44
00:03:32,900 --> 00:03:35,360
That was a cve 20-20 three, four, five, two.
44

45
00:03:35,420 --> 00:03:37,610
And the report was a triaged.
45

46
00:03:37,760 --> 00:03:40,100
And you can see the severity is high.
46

47
00:03:41,650 --> 00:03:47,760
All right, so now, as we have understood, what is this particular vulnerability, let's exploit some
47

48
00:03:47,760 --> 00:03:49,530
target using shodan.
48

49
00:03:49,950 --> 00:03:55,650
So for that, you can just go on to shodan and you can just a search for C.
49

50
00:03:55,730 --> 00:03:55,990
S.
50

51
00:03:56,100 --> 00:03:56,430
C.
51

52
00:03:56,790 --> 00:03:57,060
OE.
52

53
00:03:58,080 --> 00:04:02,580
After you search this, you can see we have got one zero 4 the results.
53

54
00:04:03,330 --> 00:04:11,550
So from these results, you can take each target one by one and try to send the same HTTP  request
54

55
00:04:11,940 --> 00:04:16,430
as can be seen or here.
55

56
00:04:18,450 --> 00:04:23,610
This particular request, and after you send this particular request, which says that we want to read
56

57
00:04:23,640 --> 00:04:32,370
the portal I n c dot LRU a file, and then we will be able to confirm if we are able to read that particular
57

58
00:04:32,370 --> 00:04:32,760
file.
58

59
00:04:33,360 --> 00:04:40,260
So what we can do is instead of taking one by one each target, we can simply automate the whole process.
59

60
00:04:40,700 --> 00:04:48,060
So for that, as you can see over here, I have written the script, which you can utilize.
60

61
00:04:48,570 --> 00:04:49,080
So we're here.
61

62
00:04:49,080 --> 00:04:51,630
You can see shodan  search, Cisco, ASA
62

63
00:04:52,050 --> 00:04:57,570
So if you search for a Cisco ASA, let me show you how many targets you would get.
63

64
00:05:01,260 --> 00:05:06,160
So it is loading and you can see we have got to be one targets only.
64

65
00:05:06,450 --> 00:05:14,970
So instead of Cisco, is it you can search for the particular other Kuwaiti, which was plus CSCOE
65

66
00:05:15,030 --> 00:05:17,250
and you will get more results.
66

67
00:05:17,700 --> 00:05:24,690
Now, what you can do simply is run this particular script, which will search for the Cisco ASA servers.
67

68
00:05:24,780 --> 00:05:34,890
And also you can replace your search query by C, A, C O E, and when we will get the output output
68

69
00:05:34,890 --> 00:05:37,950
from that output, we are going to separate the IP address.
69

70
00:05:38,370 --> 00:05:43,550
And we are going to send that particular IP address to the curl request, which is nothing.
70

71
00:05:43,590 --> 00:05:45,480
But we are trying to read the same file.
71

72
00:05:45,960 --> 00:05:53,820
So because of this, while loop each and every IP from that particular search result is going to get submitted
72

73
00:05:53,880 --> 00:05:55,140
to the call request.
73

74
00:05:55,570 --> 00:05:55,960
All right.
74

75
00:05:56,050 --> 00:05:57,960
So let's run this.
75

76
00:05:58,410 --> 00:06:02,910
So I will hit enter and you'll be able to see in couple of seconds this will start.
76

77
00:06:03,240 --> 00:06:06,430
And if any target is vulnerability, we will be able to identify.
77

78
00:06:06,510 --> 00:06:08,130
As you can see into over here.
78

79
00:06:08,930 --> 00:06:09,330
Curl
79

80
00:06:09,720 --> 00:06:14,240
curl request has been sent to this particular target, which has been enumerated from shodan
80

81
00:06:14,730 --> 00:06:21,480
And it is trying to send that particular request to that particular target in case the target is 
81

82
00:06:21,480 --> 00:06:21,850
vulnerability
82

83
00:06:21,870 --> 00:06:24,690
We will be able to see the output over here.
83

84
00:06:24,780 --> 00:06:29,310
So what I'm going to do currently is I'm going to stop this scan as.
84

85
00:06:30,890 --> 00:06:32,330
It will take a lot of time.
85

86
00:06:32,360 --> 00:06:33,950
So you guys can try this.
86

87
00:06:34,010 --> 00:06:34,190
Okay.
87

88
00:06:34,680 --> 00:06:37,100
Now, what is the other way you can do this?
88

89
00:06:37,280 --> 00:06:44,630
Because shodan has a limited number of targets, as you can see over here, one zero four target.
89

90
00:06:45,170 --> 00:06:52,850
Now, in case you want to search the same vulnerability or the same exploit for other targets, how can
90

91
00:06:52,850 --> 00:06:53,390
you do that?
91

92
00:06:53,660 --> 00:06:57,440
The simple way is to do subdomain enumeration.
92

93
00:06:57,800 --> 00:07:04,210
So now we are going to do exploit some more targets from subdomain enumeration.
93

94
00:07:04,580 --> 00:07:10,730
For that, you can just simply jump on to this particular project, which is hosted by Project Discovery
94

95
00:07:10,730 --> 00:07:11,090
team.
95

96
00:07:11,600 --> 00:07:12,800
It is very awesome.
96

97
00:07:13,160 --> 00:07:19,760
And you will directly get all the sub domain enumeration list over here of all the bug bounty programs,
97

98
00:07:19,880 --> 00:07:23,800
which pays rewards or without rewards as well.
98

99
00:07:24,290 --> 00:07:30,020
So as you can see over here, if I will click on all, then you can see this all all programs are listed
99

100
00:07:30,110 --> 00:07:30,980
all over here.
100

101
00:07:31,730 --> 00:07:35,830
These programs are on Hacker one and  the other programs are on bug crowd
101

102
00:07:36,020 --> 00:07:41,270
As you can see over here, which has been demonstrated by the bug crowd symbol and hacker, one symbol.
102

103
00:07:41,380 --> 00:07:43,760
OK, so now I feel click on new programs.
103

104
00:07:43,780 --> 00:07:48,080
You'll be able to see any new programs if it is added on that particular target.
104

105
00:07:48,530 --> 00:07:49,240
New subdomains.
105

106
00:07:49,250 --> 00:07:53,870
You can see if new sub domains are being deployed by any of these target.
106

107
00:07:53,900 --> 00:08:01,580
So you can see AT&T and Amazon has deployed huge number of subdomains so you can start hunting on those
107

108
00:08:01,580 --> 00:08:02,330
targets as well.
108

109
00:08:02,750 --> 00:08:09,860
If you specifically want to hunt on programs on hackerone or bugcrowd you can also do that if you
109

110
00:08:09,860 --> 00:08:14,450
want the programs, which gives the rewards, who can just go to the rewards and you will be able to
110

111
00:08:14,450 --> 00:08:17,200
see these programs, which gives you rewards.
111

112
00:08:17,720 --> 00:08:22,850
So what I have done is I'm going to hunt on the target, which is a Bentley.
112

113
00:08:23,250 --> 00:08:23,420
OK.
113

114
00:08:23,690 --> 00:08:27,620
So I will just click on this particular cloud button, as you can see over here.
114

115
00:08:27,980 --> 00:08:33,200
And it is going to download a zip file, which will contain two, two, six, three subdomains.
115

116
00:08:33,380 --> 00:08:34,790
As you can see over here.
116

117
00:08:35,210 --> 00:08:37,950
So I have all the subdomains of Bently.
117

118
00:08:38,060 --> 00:08:39,290
Let me just zoom this for you.
118

119
00:08:39,830 --> 00:08:47,750
And from this, I can try on each and every target, the particular script and any of that target.
119

120
00:08:47,840 --> 00:08:51,770
If it is running on the Cisco A.S.A. VPN server.
120

121
00:08:51,860 --> 00:08:54,920
Then I will be able to do our arbitrary file.
121

122
00:08:54,920 --> 00:08:55,220
Read.
122

123
00:08:57,070 --> 00:08:57,470
All right.
123

124
00:08:57,560 --> 00:09:01,190
So now you can choose any target from here as well.
124

125
00:09:01,280 --> 00:09:04,190
And the script to do this is.
125

126
00:09:06,560 --> 00:09:07,280
Over here.
126

127
00:09:07,460 --> 00:09:15,990
So I have tried on all the programs are all the subdomains of Microsoft, I had I have reported a maximum
127

128
00:09:15,990 --> 00:09:16,970
of them.
128

129
00:09:17,720 --> 00:09:20,030
What you can do is for your demonstration.
129

130
00:09:20,090 --> 00:09:24,740
I'm going to show you on this particular target list.
130

131
00:09:24,770 --> 00:09:33,500
So as you can see, I have also found and reported for Benntley infosys  Microsoft and TATA.
131

132
00:09:33,980 --> 00:09:40,180
So let me just show you for demonstration targets.Jason contains my target.
132

133
00:09:40,220 --> 00:09:41,330
So let me just show you.
133

134
00:09:41,390 --> 00:09:43,280
Let me just get the file.
134

135
00:09:43,310 --> 00:09:46,190
And you can see these are all the subdomains for TATA.
135

136
00:09:46,730 --> 00:09:52,130
And out of these some of the subdomains are wonderful, which I have taken into this particular file,
136

137
00:09:52,550 --> 00:09:53,810
which is one vulnerable target.
137

138
00:09:53,870 --> 00:09:56,400
So let me just show you vulnerable target.
138

139
00:09:56,440 --> 00:09:57,580
Dot Json.
139

140
00:09:57,710 --> 00:10:00,650
And you can see these are the two vulnerability targets.
140

141
00:10:01,190 --> 00:10:06,740
So now I can just simply run the curl script to identify if they are vulnerable or not.
141

142
00:10:06,770 --> 00:10:08,630
So let us just do this quickly.
142

143
00:10:08,780 --> 00:10:10,220
So let me just copy this script.
143

144
00:10:12,240 --> 00:10:19,860
Let me past it over here and you can see I want to cat this particular file, which wasvulnerable  target.
144

145
00:10:24,530 --> 00:10:25,440
Target.json
145

146
00:10:25,530 --> 00:10:25,740
OK.
146

147
00:10:25,810 --> 00:10:31,570
So I will just hit enter and you can see it is reading that particular file and it is giving me the
147

148
00:10:31,570 --> 00:10:32,260
output.
148

149
00:10:32,320 --> 00:10:37,690
So as you can see, this is the output for the file that we are trying to read.
149

150
00:10:37,780 --> 00:10:39,970
And the file that we are reading is.
150

151
00:10:41,330 --> 00:10:46,230
AUL  file, which is the configuration file.
151

152
00:10:46,340 --> 00:10:46,910
So.
152

153
00:10:47,850 --> 00:10:48,270
Yes.
153

154
00:10:51,590 --> 00:10:52,520
As you're able to see.
154

155
00:10:52,700 --> 00:10:53,060
All right.
155

156
00:10:53,270 --> 00:10:58,740
So now you can see here the file that we are able to read is the portal_inc.lua
156

157
00:10:59,120 --> 00:11:01,280
and both the targets were vulnerable.
157

158
00:11:01,730 --> 00:11:05,600
So we are able to successfully read the particular file.
158

159
00:11:05,990 --> 00:11:11,060
So what you can do is you can just again, replace, the target name from here.
159

160
00:11:11,120 --> 00:11:11,960
You can save it.
160

161
00:11:12,290 --> 00:11:16,130
Save it in txt  format or json format, any format.
161

162
00:11:16,550 --> 00:11:21,550
And you can run this particular script which will try to do the arbitrary file read.
162

163
00:11:22,510 --> 00:11:22,690
OK.
163

164
00:11:23,840 --> 00:11:31,160
One of the three that I like is I like using find domain for the programs which are not listed over
164

165
00:11:31,160 --> 00:11:36,890
here on Project Discovery to identify the subdomains for any particular target.
165

166
00:11:37,460 --> 00:11:40,010
I use findomain so you can also use that.
166

167
00:11:40,610 --> 00:11:47,090
Simply go to the findomain GitHub repository and you need to clone that particular project.
167

168
00:11:47,510 --> 00:11:49,460
I have already cloned it and I have installed.
168

169
00:11:49,790 --> 00:11:56,150
So let me just show you find domain so you can use fine domain to find a lot of subdomains.
169

170
00:11:56,310 --> 00:12:01,340
So let's try to identify some subdomains, findomain.
170

171
00:12:02,150 --> 00:12:05,840
Let's say our target is infosys dot com.
171

172
00:12:06,140 --> 00:12:11,300
So we are going to identify the subdomains or let us choose on the target.
172

173
00:12:11,660 --> 00:12:14,240
For instance, let's say Starbucks.
173

174
00:12:16,660 --> 00:12:20,860
OK, so now I want to see which of the domains resolve.
174

175
00:12:20,950 --> 00:12:24,000
And I want to save the output in Starbucks dot com.txt
175

176
00:12:24,250 --> 00:12:25,220
And I will hit enter.
176

177
00:12:25,720 --> 00:12:33,550
So this will start enumerating all the subdomains for a Starbucks and it will save to a file, which
177

178
00:12:33,580 --> 00:12:36,970
is Starbucks dot com.txt
178

179
00:12:37,090 --> 00:12:44,620
And I can just take that particular list and I can give that subdomain list to this particular script.
179

180
00:12:44,950 --> 00:12:46,900
And it will automatically identify.
180

181
00:12:46,930 --> 00:12:49,540
And this way you can do mass hunting.
181

182
00:12:50,050 --> 00:13:00,010
So I'm just going to stop this scan for those users who do not want to set up and findomain into their
182

183
00:13:00,010 --> 00:13:07,540
computers or they do not want to run it from the terminal, can also use a very, very awesome resource,
183

184
00:13:07,880 --> 00:13:10,240
which is an 
nmmapper.com
184

185
00:13:10,570 --> 00:13:16,600
So just simply come over here and choose the fine domain when the last.
185

186
00:13:16,780 --> 00:13:19,270
And you can just give any target you want.
186

187
00:13:19,330 --> 00:13:28,360
So let me just give their target, which is star box, dot com and hit enter and it will just take some
187

188
00:13:28,360 --> 00:13:28,720
time.
188

189
00:13:28,810 --> 00:13:34,470
And you can see we have identify one six, four, five domains.
189

190
00:13:34,480 --> 00:13:41,600
So they are total 1645 domains which you can test for the same vulnerability.
190

191
00:13:41,710 --> 00:13:48,910
You can just copy paste from here, remove this host and save this into a text file and simply give
191

192
00:13:48,970 --> 00:13:51,250
it to this particular script.
192

193
00:13:51,700 --> 00:13:56,140
If any of the target is vulnerable, you will be able to read that particular file.
193

194
00:13:56,860 --> 00:13:57,260
All right.
194

195
00:13:57,550 --> 00:14:02,070
So now I hope you understood how you can do subdomain enumeration.
195

196
00:14:02,170 --> 00:14:03,370
And you can read the files.
196

197
00:14:04,000 --> 00:14:08,470
Now, more arbitrary file read entry points equals two more win.
197

198
00:14:08,710 --> 00:14:14,830
So this particular researcher gave only one file to read, which was the portal.
198

199
00:14:14,860 --> 00:14:16,290
dot inc doe iua
199

200
00:14:16,690 --> 00:14:21,620
So after seeing this particular POC, I was surprised that.
200

201
00:14:21,700 --> 00:14:26,440
And I was excited to read more files from that particular server to increase the severity.
201

202
00:14:26,830 --> 00:14:34,990
So I brute force to the SEC list all the particular word list of Json Had is, all the txt or other
202

203
00:14:34,990 --> 00:14:36,620
SEC list for LFI
203

204
00:14:37,180 --> 00:14:43,240
I also use the first DB for a brute forcing those files, but I did not get success.
204

205
00:14:43,990 --> 00:14:51,850
So after finding a lot of queries, which is basically the word list which contains all those words,
205

206
00:14:52,270 --> 00:14:58,420
I was able to enumerate some of the entry points which works on the Cisco ASA
206

207
00:14:59,020 --> 00:15:00,850
So I'm giving this file entry points.
207

208
00:15:00,940 --> 00:15:09,490
Also, I have tweeted into the same tweet over here, which you can read someone interested can read
208

209
00:15:09,490 --> 00:15:10,690
this file from the server.
209

210
00:15:10,720 --> 00:15:17,110
I have tested them so you can see the files which are http auth.html user dialog.html
210

211
00:15:17,120 --> 00:15:19,890
localization dot inc .iua
211

212
00:15:20,200 --> 00:15:26,620
So these are all the files which are being tested by me and they are working perfectly fine.
212

213
00:15:28,350 --> 00:15:28,650
All right.
213

214
00:15:28,780 --> 00:15:35,440
So you can also read this particular files, which may give you more sensitive information.
214

215
00:15:37,850 --> 00:15:40,880
So you can just increase the severity as well.
215

216
00:15:41,260 --> 00:15:41,620
All right.
216

217
00:15:41,870 --> 00:15:44,930
So these are all the file entry points.
217

218
00:15:44,960 --> 00:15:49,720
I'm willing to give this entry points in to the description into the resources, though.
218

219
00:15:49,880 --> 00:15:54,260
You can just refer that as well now and nmap NSE detection
219

220
00:15:54,770 --> 00:16:01,880
There is also a nmap script which you can utilize to detect if the targets are vulnerable
220

221
00:16:02,450 --> 00:16:04,560
So there in a nmap, NSE script is test.
221

222
00:16:04,630 --> 00:16:06,020
Cisco asa dot NSE.
222

223
00:16:08,280 --> 00:16:10,470
You can simply use this particular script.
223

224
00:16:10,590 --> 00:16:13,980
So let me use the script on vulnerable target dot json
224

225
00:16:14,370 --> 00:16:18,270
So I'm going to take the input list and my input list is vulnerable target.
225

226
00:16:18,530 --> 00:16:19,300
.json
226

227
00:16:19,920 --> 00:16:21,420
And I'm going to run the script.
227

228
00:16:22,260 --> 00:16:24,840
So a script and the script name.
228

229
00:16:25,500 --> 00:16:27,690
And let's say we do a service version detction
229

230
00:16:28,050 --> 00:16:31,230
Let's turn on the ping and lets it out.
230

231
00:16:31,270 --> 00:16:31,410
What.
231

232
00:16:31,410 --> 00:16:32,970
In verbose mode and hit enter.
232

233
00:16:33,450 --> 00:16:40,720
And if the target is vulnerable then it is going to tell us the target is vulnerable the c v e 202023 four
233

234
00:16:40,720 --> 00:16:44,490
five two which is the Cisco A.S.A. arbitrary file read.
234

235
00:16:45,920 --> 00:16:46,310
All right.
235

236
00:16:46,400 --> 00:16:52,160
Until our scan is running, let me just tell you the automation part.
236

237
00:16:52,480 --> 00:16:59,560
So we have already seen the automation part of it and we can automate of finding targets from shodan
237

238
00:16:59,560 --> 00:16:59,840
on.
238

239
00:17:00,100 --> 00:17:06,550
We can automate finding the target from the subdomain list that you have identified.
239

240
00:17:07,090 --> 00:17:14,620
I have reported all the targets for a Microsoft Bentley and other small targets for tcs and infosys
240

241
00:17:14,650 --> 00:17:15,040
as well.
241

242
00:17:15,970 --> 00:17:16,250
All right.
242

243
00:17:16,300 --> 00:17:21,610
So as you can see, over hear it will tell you that Target is a vulnerable to the read only For
243

244
00:17:22,000 --> 00:17:24,340
Reed, only for traversal vulnerability
244

245
00:17:24,730 --> 00:17:30,310
And it also gives you the verified, the arbitrary filed read, as you can see over here.
245

246
00:17:30,760 --> 00:17:36,340
But you can see what here it is giving you the same portal I iinc.aul file, which is given
246

247
00:17:36,340 --> 00:17:37,900
by the original researcher.
247

248
00:17:38,290 --> 00:17:43,960
But I am giving you more and more files to read so you can read these many files as well.
248

249
00:17:44,380 --> 00:17:46,960
This has not been posted anywhere by any researcher.
249

250
00:17:47,110 --> 00:17:53,470
So I think I'm the first one to post these files, which you can also read from that particular target
250

251
00:17:53,590 --> 00:17:54,130
server.
251

252
00:17:56,290 --> 00:17:56,620
All right.
252

253
00:17:56,730 --> 00:18:00,930
So I hope you guys understood how you can also use that and nmap script.
253

254
00:18:01,520 --> 00:18:06,060
I have shown you the automation for showdown as well as a subdomain enumeration.
254

255
00:18:06,390 --> 00:18:13,950
Now, my final words for this is, if you want to prove this particular vulnerability,  for any target,
255

256
00:18:13,980 --> 00:18:16,710
you can do the mass hunting as well as I have shown you.
256

257
00:18:17,010 --> 00:18:17,820
But I will.
257

258
00:18:17,940 --> 00:18:25,590
I would highly recommend to do not read much more sensitive files or do not download or dump any kinds
258

259
00:18:25,590 --> 00:18:32,970
of file does to prove you can read the simple aul file and you can tell them that there exist.
259

260
00:18:33,060 --> 00:18:38,360
This particular vulnerability you can identify obviously using that and nmap nse script.
260

261
00:18:38,670 --> 00:18:40,250
It will tell you if the target is vulnerable.
261

262
00:18:40,470 --> 00:18:46,350
And for the POC, you can just try to read a simple nonsensitive file.
262

263
00:18:46,430 --> 00:18:46,600
OK.
263

264
00:18:46,770 --> 00:18:54,510
So you can just read, load or Gi.F. or you can read ask Html or ping html  any file, which
264

265
00:18:54,600 --> 00:18:57,810
is not considered to be much more sensitive.
265

266
00:18:59,040 --> 00:18:59,360
All right.
266

267
00:18:59,430 --> 00:19:05,720
So in case you have any questions, you can just submit your questions into the resources section or
267

268
00:19:05,770 --> 00:19:08,070
into the Q&;A.
268

269
00:19:08,250 --> 00:19:14,820
And I would be happy to answer those questions regarding all the assets, file entry points and all
269

270
00:19:14,820 --> 00:19:15,330
the scripts.
270

271
00:19:15,360 --> 00:19:17,040
I'm going to give you everything.
271

272
00:19:17,850 --> 00:19:21,420
I hope you guys understood the video and liked the video.
272

273
00:19:21,720 --> 00:19:22,200
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 9: Exploitation of CVE 2020-3187 File Delete

0
1
00:00:00,130 --> 00:00:00,960
Hello, everyone.
1

2
00:00:01,050 --> 00:00:09,110
And we are back again, with , one more exploit, one more POC for the CVE.
2

3
00:00:09,430 --> 00:00:11,370
Twenty twenty three one eight seven.
3

4
00:00:11,790 --> 00:00:19,860
So this particular CV is unauthenticated arbitrary file deletion in the same as Cisco, ASA  FTD.
4

5
00:00:21,120 --> 00:00:29,610
We have already seen a CVE in to this particular software vision, a vision, a we were able to do arbitrary
5

6
00:00:29,850 --> 00:00:32,520
file read into that particular server.
6

7
00:00:33,090 --> 00:00:40,920
Now we have one more POC wherein we can delete any file on to that particular server.
7

8
00:00:41,430 --> 00:00:45,600
So the same user has released one more POC
8

9
00:00:46,250 --> 00:00:53,880
And in the POC we can see that he is able to delete a file from this particular server, which is
9

10
00:00:54,210 --> 00:00:57,060
the cisco logo dot gif file.
10

11
00:00:57,390 --> 00:01:05,370
So we try to hunt the same targets and we were able to find some of the live targets on which we were
11

12
00:01:05,490 --> 00:01:13,800
able to do the same task in which we were able to delete this particular file, which was the logo dot
12

13
00:01:13,800 --> 00:01:14,510
G.F..
13

14
00:01:15,390 --> 00:01:20,860
Now, what is the severity or impact of this particular one vulnerability?
14

15
00:01:20,910 --> 00:01:24,630
So this particular venerability is considered to be critical.
15

16
00:01:24,920 --> 00:01:25,360
Why?
16

17
00:01:25,650 --> 00:01:34,500
Because in this particular venerability, the attacker is able to delete any file from that particular
17

18
00:01:34,500 --> 00:01:34,980
server.
18

19
00:01:35,370 --> 00:01:43,110
So the CVSS score is assigned as nine point one, which is basically high, as you can see over here.
19

20
00:01:44,310 --> 00:01:47,250
Now, how this is possible.
20

21
00:01:47,430 --> 00:01:50,010
We are going to discuss that before that.
21

22
00:01:50,070 --> 00:01:54,510
Let's quickly identify a target and see alive.
22

23
00:01:54,600 --> 00:01:55,200
POC.
23

24
00:01:55,530 --> 00:01:59,760
So over here, this is the curl request that we are going to use.
24

25
00:01:59,940 --> 00:02:05,760
I'm willing to break down the cold request to make you understand actually what is happening behind
25

26
00:02:05,790 --> 00:02:06,240
the hood.
26

27
00:02:06,720 --> 00:02:12,480
Our target is this particular target, which is a VPN on tata Communications dot com.
27

28
00:02:12,900 --> 00:02:14,340
And we are going to delete a file.
28

29
00:02:14,710 --> 00:02:22,110
Remember, this is not recommended to delete any files on to do that particular server.
29

30
00:02:23,460 --> 00:02:32,280
In case if you delete any lua configuration files, then it maycause a denial of service and
30

31
00:02:32,400 --> 00:02:36,540
it will cause I dos then the server will become unusable.
31

32
00:02:36,630 --> 00:02:42,660
As you can see on this, this can lead to a dos on the VPN by deleting the lua source code files
32

33
00:02:42,660 --> 00:02:47,700
from the system which will break the web VPN interface until the device is rebooted.
33

34
00:02:48,180 --> 00:02:51,600
So do not try this on life targets on a bug bounty.
34

35
00:02:51,660 --> 00:02:53,850
This is highly, highly recommended.
35

36
00:02:54,330 --> 00:03:01,380
So for the demonstration, we are just going to delete the Gi.F., which is the Cisco logo.
36

37
00:03:01,590 --> 00:03:01,940
All right.
37

38
00:03:02,340 --> 00:03:03,900
So let's quickly jump onto this.
38

39
00:03:03,990 --> 00:03:06,030
And I have recorded a video.
39

40
00:03:06,150 --> 00:03:09,930
So let me just show you how and what we are going to do.
40

41
00:03:10,380 --> 00:03:16,410
So as you can see, this is our target and this is the logo which can be seen here.
41

42
00:03:16,470 --> 00:03:23,940
Let me just reload this for you to confirm that this is the particular logo we have set our target,
42

43
00:03:23,970 --> 00:03:27,600
which is this particular target, and we are going to delete the logo file.
43

44
00:03:27,810 --> 00:03:33,490
Now, we are going to do this particular task with the help of the curl request.
44

45
00:03:33,570 --> 00:03:35,790
So I'm just going to copy the curl request.
45

46
00:03:36,240 --> 00:03:42,730
I'm going to quickly jump onto my terminal and I'm going to paste the curl request now in the call request.
46

47
00:03:42,780 --> 00:03:47,970
You have to set the target for which you want to delete the file from that particular server.
47

48
00:03:48,550 --> 00:03:52,800
Remember, the server needs to be Cisco ASA and needs to be vulnerable.
48

49
00:03:53,400 --> 00:03:55,990
We have already identified this to be  vulnerable.
49

50
00:03:56,010 --> 00:03:59,010
And now we are going to do a arbitriray file delete.
50

51
00:04:00,480 --> 00:04:04,890
So over here, you can see at http colon slash slash target.
51

52
00:04:05,040 --> 00:04:08,460
So we're going to replace that target with our target.
52

53
00:04:08,940 --> 00:04:11,010
So let me just paste the target.
53

54
00:04:12,490 --> 00:04:21,340
And let me just write HTTPS over here as well  and hit enter now when I will hit enter that particular
54

55
00:04:21,340 --> 00:04:27,520
file should get deleted from the particular server, which is given over here in the header.
55

56
00:04:27,930 --> 00:04:32,650
We are going to understand how this actually happens and how the file gets deleted.
56

57
00:04:33,490 --> 00:04:35,350
Let me just fire the request first.
57

58
00:04:36,460 --> 00:04:39,220
Let us confirm if the file has been deleted or not.
58

59
00:04:39,400 --> 00:04:40,600
So let me just reload.
59

60
00:04:40,630 --> 00:04:44,200
And you can see file not found, which means a success.
60

61
00:04:44,740 --> 00:04:50,830
Our attack is a success and we are able to delete the file.
61

62
00:04:51,670 --> 00:04:59,440
So this way, if you want to delete, you can delete the source code, which is the lua files as
62

63
00:04:59,440 --> 00:04:59,830
well.
63

64
00:05:00,400 --> 00:05:08,050
I have a list of the files which are there for configuration and which should not be deleted.
64

65
00:05:08,170 --> 00:05:11,900
Let me just show you the files over here.
65

66
00:05:18,830 --> 00:05:19,460
So
66

67
00:05:20,810 --> 00:05:25,820
Let me just show you all the files which are considered to be important.
67

68
00:05:26,020 --> 00:05:26,190
Yeah.
68

69
00:05:26,660 --> 00:05:33,530
So these are the file entry points and these other files which are responsible for the server, to run
69

70
00:05:34,010 --> 00:05:38,270
http Auth.html, user dialogue, DOT, Html localization.
70

71
00:05:38,460 --> 00:05:41,400
inc dot alu  portal Inc dot alu.
71

72
00:05:41,540 --> 00:05:45,500
So these are all the files that java JavaScript files as well.
72

73
00:05:45,920 --> 00:05:52,150
Portal form dot js  log on form dot js  portal.js, session update.js
73

74
00:05:52,730 --> 00:05:59,120
So these are the important file entry points which are responsible for the particular VPN server to
74

75
00:05:59,120 --> 00:05:59,360
run.
75

76
00:05:59,750 --> 00:06:05,360
And you should not delete any of this files because it will create a dos.
76

77
00:06:05,780 --> 00:06:06,110
All right.
77

78
00:06:06,230 --> 00:06:10,010
Now it is time to understand file is being deleted.
78

79
00:06:10,370 --> 00:06:10,730
Sure.
79

80
00:06:10,730 --> 00:06:10,940
You.
80

81
00:06:11,600 --> 00:06:17,480
So as you can see, we are sending a particular curl request with the header and the header is cookie and
81

82
00:06:17,480 --> 00:06:22,760
we are giving the token is empty and we are giving the file name time as this particular file name, which
82

83
00:06:22,760 --> 00:06:27,380
is a Cisco logo dot G.F., and that particular request is going to the target.
83

84
00:06:27,740 --> 00:06:28,100
All right.
84

85
00:06:29,180 --> 00:06:30,470
Now how?
85

86
00:06:31,400 --> 00:06:35,240
By triggering this particular request, how the file is getting deleted.
86

87
00:06:35,540 --> 00:06:37,280
So for that, we have to see over here.
87

88
00:06:37,850 --> 00:06:44,720
This is the Lua file from that particular target and into the lua files,source code.
88

89
00:06:44,840 --> 00:06:51,880
You can see if a local name sessions request is going for this particular endpoint.
89

90
00:06:52,130 --> 00:06:54,680
Then you can see the code is os.remove.
90

91
00:06:57,110 --> 00:07:04,250
And this particular os.remove command is getting executed on the particular name, because this
91

92
00:07:04,250 --> 00:07:05,360
is getting executed.
92

93
00:07:05,480 --> 00:07:09,260
The file gets deleted from that particular server.
93

94
00:07:09,830 --> 00:07:17,090
So here we are sending the session token in which we are saying this particular file.
94

95
00:07:17,210 --> 00:07:21,980
It is reading was not remove and it is deleting the logo.gif file.
95

96
00:07:23,030 --> 00:07:29,530
So, yeah, remember the criticality and the severity for the server.
96

97
00:07:30,810 --> 00:07:38,670
Whenever this particular POC is executed is nine point one, as we have seen over here.
97

98
00:07:39,060 --> 00:07:46,260
Now, you should remember that you should not delete any arbitrary file from that particular server
98

99
00:07:46,530 --> 00:07:54,660
because it is considered to be a very, very dangerous as it may cause dos on to that particular server.
99

100
00:07:55,230 --> 00:08:00,650
So remember, this has a base of nine point one, the CVSS scored.
100

101
00:08:00,930 --> 00:08:07,290
You can identify this particular vulnerability on many, many servers which are still running.
101

102
00:08:07,320 --> 00:08:12,300
You can identify them from subdomain enumeration or shodan, whatever you like.
102

103
00:08:12,450 --> 00:08:15,480
And you can report this vulnerability to them.
103

104
00:08:16,170 --> 00:08:22,380
So I hope you guys understood how you can identify this one, the ability and how you can execute or
104

105
00:08:22,470 --> 00:08:25,140
exploit this vulnerability in the end.
105

106
00:08:25,260 --> 00:08:34,230
I am again telling do not try to execute the commands to delete the important files, which I have shown
106

107
00:08:34,230 --> 00:08:37,740
you because it will create a DOS onto that particular server.
107

108
00:08:37,830 --> 00:08:42,870
If you tried to delete these files, I hope you guys understood this video.
108

109
00:08:42,960 --> 00:08:43,530
Thank you.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================
