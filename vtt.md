
# Section 4: sql_for_data_analytics

WEBVTT

1
00:00:06.470 --> 00:00:08.730
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Guys, from today's video, we are going to

2
00:00:08.730 --> 00:00:11.390
start a sequel and in the sequel, we

3
00:00:11.390 --> 00:00:15.650
will see why we needed this tool, first

4
00:00:15.650 --> 00:00:18.090
of all, we will answer this question, suppose

5
00:00:18.090 --> 00:00:20.730
you are Flipkart or Amazon and you have

6
00:00:20.730 --> 00:00:22.590
to see a lot of orders, that is,

7
00:00:22.630 --> 00:00:24.430
a lot of you get 10 crore orders

8
00:00:24.430 --> 00:00:25.970
in a day, suppose now what do you

9
00:00:25.970 --> 00:00:28.750
think where will 10 crore orders be saved,

10
00:00:29.330 --> 00:00:31.710
will this data be saved in Excel or

11
00:00:31.710 --> 00:00:32.470
will this data be saved in a text

12
00:00:32.470 --> 00:00:35.230
file, the answer is neither will it be

13
00:00:35.230 --> 00:00:36.330
saved in a text file nor will it

14
00:00:36.330 --> 00:00:37.850
be saved in Excel, it will be saved

15
00:00:37.850 --> 00:00:40.550
in the database, now the next question of

16
00:00:40.550 --> 00:00:42.750
many of you will be why we will

17
00:00:42.750 --> 00:00:45.450
store this data in the database, the real

18
00:00:45.450 --> 00:00:47.890
reason is that the database is such a

19
00:00:47.890 --> 00:00:50.330
software that has been designed to handle an

20
00:00:50.330 --> 00:00:54.750
enormous amount of data, Excel is very good

21
00:00:54.750 --> 00:00:56.730
for a limited data, text file is also

22
00:00:56.730 --> 00:00:58.490
a very good thing to store textual data,

23
00:00:58.790 --> 00:01:01.410
but when we have to do a lot

24
00:01:01.410 --> 00:01:05.610
of operations, read operations, write operations, update operations,

25
00:01:05.770 --> 00:01:09.130
delete operations, and we want our system not

26
00:01:09.130 --> 00:01:11.590
to collapse, then we have to use a

27
00:01:11.590 --> 00:01:15.630
database and MySQL is a database, SQL stands

28
00:01:15.630 --> 00:01:18.550
for Structured Query Language, which is a language,

29
00:01:18.730 --> 00:01:20.590
a special kind of language, which helps us

30
00:01:20.590 --> 00:01:22.850
talk to the customer, now let's talk a

31
00:01:22.850 --> 00:01:24.230
little bit about how this data will be,

32
00:01:25.430 --> 00:01:28.710
whenever you talk about Flipkart's orders, talk about

33
00:01:28.710 --> 00:01:31.990
Amazon's orders, talk about Mintra's orders, then the

34
00:01:31.990 --> 00:01:34.050
way the data will look, who ordered it,

35
00:01:34.270 --> 00:01:35.530
which address the order has to be delivered,

36
00:01:35.810 --> 00:01:37.670
what was the customer's phone number, what was

37
00:01:37.670 --> 00:01:39.890
the customer's email, what items did he order,

38
00:01:40.110 --> 00:01:42.830
all this data makes a row, the way

39
00:01:42.830 --> 00:01:44.690
we have a row in Excel, in the

40
00:01:44.690 --> 00:01:46.530
same way we have a row in the

41
00:01:46.530 --> 00:01:48.750
database, so in total the data is informational,

42
00:01:49.130 --> 00:01:51.290
but when we have an enormous amount of

43
00:01:51.290 --> 00:01:53.730
data, then we have to handle it properly,

44
00:01:54.350 --> 00:01:55.910
and for that we have to use a

45
00:01:55.910 --> 00:01:57.450
database, now many of you will have a

46
00:01:57.450 --> 00:01:59.790
question, we worked so hard to learn Excel,

47
00:02:00.210 --> 00:02:01.750
then why are you saying that this data

48
00:02:01.750 --> 00:02:03.210
cannot be kept in Excel, it is an

49
00:02:03.210 --> 00:02:05.970
enormous amount of data, or if today there

50
00:02:05.970 --> 00:02:07.570
is no enormous amount of data in any

51
00:02:07.570 --> 00:02:09.650
startup, then it expects that in the coming

52
00:02:09.650 --> 00:02:11.410
time it will have an enormous amount of

53
00:02:11.410 --> 00:02:13.090
data, the use case of Excel is different,

54
00:02:13.250 --> 00:02:15.170
the use case of database is different, the

55
00:02:15.170 --> 00:02:16.810
use case of Excel is that you have

56
00:02:16.810 --> 00:02:19.490
a data, which is 70,000, 80,000,

57
00:02:19.490 --> 00:02:20.770
1,00,000, 2,00,000 rows of

58
00:02:20.770 --> 00:02:23.610
data, but here you can have a number

59
00:02:23.610 --> 00:02:26.770
of rows in millions or billions, so when

60
00:02:26.770 --> 00:02:28.250
there will be so much data, then searching

61
00:02:28.250 --> 00:02:30.750
will be slow, writing will be slow, Excel

62
00:02:30.750 --> 00:02:33.810
is not made for such use cases, Excel

63
00:02:33.810 --> 00:02:36.310
is a small analysis tool, when I say

64
00:02:36.310 --> 00:02:38.590
small, I am talking about number of rows

65
00:02:38.590 --> 00:02:43.250
of range 100K, 200K, 500K, 500K means 5

66
00:02:43.250 --> 00:02:44.970
,00,000, definitely Excel does a great job,

67
00:02:45.430 --> 00:02:47.570
but when you have to store an enormous

68
00:02:47.570 --> 00:02:49.290
amount of data and you have to do

69
00:02:49.290 --> 00:02:51.610
read and write operations with it, database is

70
00:02:51.610 --> 00:02:53.110
the tool, so what is SQL, it is

71
00:02:53.110 --> 00:02:55.150
a language that we use to talk to

72
00:02:55.150 --> 00:02:58.210
the database, and which database will we talk

73
00:02:58.210 --> 00:03:01.410
to, we will talk to MySQL, MySQL is

74
00:03:01.410 --> 00:03:04.610
a popular relational database, now what does this

75
00:03:04.610 --> 00:03:06.690
mean, I will explain this to you in

76
00:03:06.690 --> 00:03:08.930
the next video, what is a relational database,

77
00:03:09.530 --> 00:03:11.930
but MySQL is a choice, we have another

78
00:03:11.930 --> 00:03:16.050
choice, PostgreSQL, we have another choice, MSSQL, MySQL

79
00:03:16.050 --> 00:03:19.050
is open source, you can use it for

80
00:03:19.050 --> 00:03:21.750
your database, and it is widely used, means

81
00:03:21.750 --> 00:03:24.210
you go to any company to do a

82
00:03:24.210 --> 00:03:25.450
job, there is a good chance that you

83
00:03:25.450 --> 00:03:27.810
will get MySQL used there, and I will

84
00:03:27.810 --> 00:03:30.830
tell you one more interesting thing, that once

85
00:03:30.830 --> 00:03:33.350
you have learned MySQL, then your transition to

86
00:03:33.350 --> 00:03:36.990
PostgreSQL will be very easy, so that's why

87
00:03:36.990 --> 00:03:39.550
I have chosen MySQL to teach you SQL,

88
00:03:40.190 --> 00:03:41.830
in the coming videos, I will tell you

89
00:03:41.830 --> 00:03:45.410
how exactly you can use SQL and what

90
00:03:45.410 --> 00:03:48.610
is a relational database, because it is very

91
00:03:48.610 --> 00:03:49.590
important for us to know this, then if

92
00:03:49.590 --> 00:03:50.990
it is not obvious yet, then I will

93
00:03:50.990 --> 00:03:52.910
tell you, in the coming time, once we

94
00:03:52.910 --> 00:03:55.830
have made a solid foundation, then we will

95
00:03:55.830 --> 00:03:58.070
also use AI, yes, we will use AI

96
00:03:58.070 --> 00:04:01.350
to write our SQL queries, to write those

97
00:04:01.350 --> 00:04:04.670
SQL queries, which may take us a lot

98
00:04:04.670 --> 00:04:06.170
of time to write manually, but one thing

99
00:04:06.170 --> 00:04:08.210
we have to avoid here is that we

100
00:04:08.210 --> 00:04:11.070
do not have to use AI blindly, we

101
00:04:11.070 --> 00:04:12.590
are not like that, we are not understanding

102
00:04:12.590 --> 00:04:14.590
anything, and we are using AI, and we

103
00:04:14.590 --> 00:04:16.149
are getting SQL written from AI, and we

104
00:04:16.149 --> 00:04:17.310
do not know what is going on, if

105
00:04:17.310 --> 00:04:19.370
you do this, you are just one bug

106
00:04:19.370 --> 00:04:22.550
away from breaking your entire software, from breaking

107
00:04:22.550 --> 00:04:24.410
your entire flow, just think that you are

108
00:04:24.410 --> 00:04:26.750
working, while doing it, you have done everything

109
00:04:26.750 --> 00:04:28.810
with AI, and at one time AI is

110
00:04:28.810 --> 00:04:30.670
not able to solve your problem, then you

111
00:04:30.670 --> 00:04:32.030
will get stuck there, so you do not

112
00:04:32.030 --> 00:04:32.810
have to do this, you have to use

113
00:04:32.810 --> 00:04:36.530
AI like a tool, your main skill is

114
00:04:36.530 --> 00:04:38.570
that AI will be an amplifier, I hope

115
00:04:38.570 --> 00:04:40.110
you got the point, I hope you are

116
00:04:40.110 --> 00:04:42.290
understanding what I am talking about, and why

117
00:04:42.290 --> 00:04:43.790
I am saying something like this, thank you

118
00:04:43.790 --> 00:04:45.850
so much guys for watching this video, and

119
00:04:45.850 --> 00:04:47.090
I will see you in the next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.490
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, let's move ahead and now let's

2
00:00:02.490 --> 00:00:05.930
talk about relational vs non-relational databases.

3
00:00:06.550 --> 00:00:10.070
Relational databases are those databases that store data

4
00:00:10.070 --> 00:00:13.490
in tables and a relationship can be made

5
00:00:13.490 --> 00:00:13.590
between those tables.

6
00:00:13.970 --> 00:00:15.590
For example, the customer table will be different,

7
00:00:15.850 --> 00:00:18.090
the orders table will be different, which customer's

8
00:00:18.090 --> 00:00:20.090
order can be matched.

9
00:00:20.910 --> 00:00:24.550
This makes retrieval fast, internal implementation is optimised,

10
00:00:25.090 --> 00:00:28.030
and a fixed schema is maintained by relational

11
00:00:28.030 --> 00:00:29.690
database management systems.

12
00:00:29.690 --> 00:00:31.830
The database we are going to use, MySQL,

13
00:00:31.970 --> 00:00:33.990
is a relational database management system.

14
00:00:34.130 --> 00:00:37.010
In relational database management system, tables can be

15
00:00:37.010 --> 00:00:39.350
connected to each other using relationships.

16
00:00:39.590 --> 00:00:41.230
For example, there is a user's table and

17
00:00:41.230 --> 00:00:42.010
an order's table.

18
00:00:42.210 --> 00:00:45.170
Which user placed which order, this user underscore

19
00:00:45.170 --> 00:00:47.530
ID can be stored in the order's table

20
00:00:47.530 --> 00:00:48.670
and found out.

21
00:00:49.010 --> 00:00:50.210
This links both the tables.

22
00:00:51.210 --> 00:00:52.950
And CRUD operations become easy.

23
00:00:53.450 --> 00:00:54.330
Now what are these CRUD operations?

24
00:00:55.150 --> 00:00:57.750
CRUD stands for Create, Read, Update, Delete.

25
00:00:57.750 --> 00:01:00.890
In any database, four operations are very important.

26
00:01:01.330 --> 00:01:03.510
Create means you create a table, create a

27
00:01:03.510 --> 00:01:04.710
record in the table.

28
00:01:05.310 --> 00:01:07.270
Read means you read that record.

29
00:01:08.110 --> 00:01:10.170
Update means you update a particular record.

30
00:01:11.090 --> 00:01:13.090
And Delete means you delete any record.

31
00:01:13.870 --> 00:01:15.850
These four are the most important operations.

32
00:01:16.290 --> 00:01:18.790
And in any database management system, relational or

33
00:01:18.790 --> 00:01:20.430
non-relational are very important.

34
00:01:20.810 --> 00:01:23.070
So which is that popular relational database management

35
00:01:23.070 --> 00:01:23.470
system?

36
00:01:23.550 --> 00:01:24.230
First of all, I will take the name

37
00:01:24.230 --> 00:01:24.710
of MySQL.

38
00:01:24.710 --> 00:01:26.730
Then comes PostgreSQL.

39
00:01:26.890 --> 00:01:28.230
Then comes MSSQL.

40
00:01:28.470 --> 00:01:29.350
Then there is a SQL Server.

41
00:01:29.790 --> 00:01:30.270
There is also Oracle.

42
00:01:30.730 --> 00:01:31.650
These are all examples.

43
00:01:31.870 --> 00:01:32.950
But I want to tell you one thing.

44
00:01:33.430 --> 00:01:37.930
Once you understand MySQL, how SQL works, after

45
00:01:37.930 --> 00:01:40.410
that you can use any relational database management

46
00:01:40.410 --> 00:01:42.710
system to run your SQL queries.

47
00:01:43.530 --> 00:01:45.530
You can analyse and manipulate data.

48
00:01:46.170 --> 00:01:48.330
Now let's talk about non-relational database management

49
00:01:48.330 --> 00:01:48.810
systems.

50
00:01:49.150 --> 00:01:51.410
These are the databases in which tables are

51
00:01:51.410 --> 00:01:51.870
not used.

52
00:01:52.610 --> 00:01:54.290
These are based on a flexible schema.

53
00:01:55.190 --> 00:01:57.570
For example, MongoDB stores data in JSON type

54
00:01:57.570 --> 00:01:58.250
format.

55
00:01:59.450 --> 00:02:00.830
And this JSON type format does not have

56
00:02:00.830 --> 00:02:01.350
to be consistent.

57
00:02:02.310 --> 00:02:04.050
For example, your one order can look something

58
00:02:04.050 --> 00:02:05.070
like this.

59
00:02:05.390 --> 00:02:07.750
Item 1, Item 2, and in your second

60
00:02:07.750 --> 00:02:09.630
order, instead of item, it can be ordered

61
00:02:09.630 --> 00:02:10.390
underscore item.

62
00:02:10.910 --> 00:02:12.230
It means there is no fixed structure.

63
00:02:12.550 --> 00:02:13.610
You can store anything in the database.

64
00:02:14.550 --> 00:02:15.590
Flexibility is given to you.

65
00:02:16.030 --> 00:02:17.050
Now it sounds good to hear.

66
00:02:17.310 --> 00:02:18.710
But your data does not have a set

67
00:02:18.710 --> 00:02:19.070
schema.

68
00:02:19.670 --> 00:02:20.890
Which can cause a lot of problems in

69
00:02:20.890 --> 00:02:21.190
the future.

70
00:02:21.190 --> 00:02:23.530
But if we talk about relational database management

71
00:02:23.530 --> 00:02:26.190
systems, discipline is maintained there.

72
00:02:26.390 --> 00:02:26.830
You have to insert data in a set

73
00:02:26.830 --> 00:02:27.230
schema.

74
00:02:28.650 --> 00:02:30.450
Otherwise, you cannot insert.

75
00:02:30.530 --> 00:02:31.330
Which is better?

76
00:02:31.510 --> 00:02:34.110
Relational database management system or non-relational database

77
00:02:34.110 --> 00:02:34.950
management system?

78
00:02:35.170 --> 00:02:37.450
Now if we talk about complex queries, in

79
00:02:37.450 --> 00:02:38.050
which we have to take relationships of different

80
00:02:38.050 --> 00:02:42.030
tables, then relational database management system is better.

81
00:02:42.210 --> 00:02:44.290
But if your queries are very simple and

82
00:02:44.290 --> 00:02:45.790
straightforward, and you want to scale the data

83
00:02:45.790 --> 00:02:49.450
horizontally, then non-relational database management system is

84
00:02:49.450 --> 00:02:49.750
better.

85
00:02:49.750 --> 00:02:52.350
Examples of non-relational database management systems are

86
00:02:52.350 --> 00:02:55.190
MongoDB, Neo4j, Cassandra, Redis.

87
00:02:55.370 --> 00:02:56.370
There are many more examples.

88
00:02:56.810 --> 00:02:58.330
But let's focus on MySQL.

89
00:02:58.710 --> 00:03:00.650
We will take a step back and focus

90
00:03:00.650 --> 00:03:01.490
on MySQL.

91
00:03:01.970 --> 00:03:04.170
Because we are going to use it in

92
00:03:04.170 --> 00:03:05.190
our data analysis.

93
00:03:05.510 --> 00:03:09.210
Now data format, schema, relationships, consistency, query language

94
00:03:09.210 --> 00:03:10.990
and analytics friendly or not?

95
00:03:11.490 --> 00:03:13.890
If we measure the performance of non-relational

96
00:03:13.890 --> 00:03:17.250
database management system on this, then you can

97
00:03:17.250 --> 00:03:19.650
see a quick comparison on your screen.

98
00:03:20.090 --> 00:03:21.990
Now in the coming videos, we will see

99
00:03:21.990 --> 00:03:25.410
how to instal MySQL, how to use it,

100
00:03:25.790 --> 00:03:26.790
what are the benefits we are going to

101
00:03:26.790 --> 00:03:29.710
get by using a particular tool like MySQL

102
00:03:29.710 --> 00:03:30.330
Workbench.

103
00:03:31.650 --> 00:03:33.930
We will see everything in the coming videos.

104
00:03:34.570 --> 00:03:35.870
See you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.910
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to instal

2
00:00:02.910 --> 00:00:03.990
MySQL.

3
00:00:04.110 --> 00:00:06.350
I am really very excited because we will

4
00:00:06.350 --> 00:00:07.410
start our journey from here.

5
00:00:07.770 --> 00:00:09.750
Let's go to the computer screen quickly and

6
00:00:09.750 --> 00:00:13.270
then quickly see how we can instal MySQL,

7
00:00:13.750 --> 00:00:16.590
how to run SQL queries and how to

8
00:00:16.590 --> 00:00:20.110
use this beautiful piece of software and master

9
00:00:20.110 --> 00:00:20.470
it.

10
00:00:20.690 --> 00:00:22.390
Alright guys, as you can see, I have

11
00:00:22.390 --> 00:00:24.510
come to my computer screen and here I

12
00:00:24.510 --> 00:00:27.870
will write Download MySQL Server.

13
00:00:54.970 --> 00:00:58.570
You can click on this and as soon

14
00:00:58.570 --> 00:01:00.850
as you click, the download will start.

15
00:01:01.110 --> 00:01:02.710
I will wait for the download to complete.

16
00:01:03.069 --> 00:01:06.210
As you can see, this installer has opened.

17
00:01:06.770 --> 00:01:09.670
Please wait while Windows configures MySQL installer.

18
00:01:10.050 --> 00:01:12.370
Let's wait and now we will wait.

19
00:01:12.970 --> 00:01:14.230
It has given one more pop-up and

20
00:01:14.230 --> 00:01:15.250
I have accepted it again.

21
00:01:15.750 --> 00:01:16.770
And here you can see that it is

22
00:01:16.770 --> 00:01:17.610
asking what do you want to instal.

23
00:01:17.990 --> 00:01:19.390
So I will click on server only and

24
00:01:19.390 --> 00:01:19.770
click on next.

25
00:01:20.570 --> 00:01:22.310
Then I will click on execute.

26
00:01:23.410 --> 00:01:25.110
And here we will wait.

27
00:01:25.390 --> 00:01:25.770
It is installing.

28
00:01:26.530 --> 00:01:27.270
We will do next again.

29
00:01:27.850 --> 00:01:28.610
We will do next again.

30
00:01:29.290 --> 00:01:30.930
And you leave it as default and do

31
00:01:30.930 --> 00:01:31.570
next again.

32
00:01:32.030 --> 00:01:32.690
Do next again.

33
00:01:32.950 --> 00:01:33.710
Now it is saying to choose a root

34
00:01:33.710 --> 00:01:34.110
password.

35
00:01:34.470 --> 00:01:35.990
So I choose a root password.

36
00:01:36.910 --> 00:01:40.130
And I am choosing a very simple root

37
00:01:40.130 --> 00:01:40.750
password on you.

38
00:01:40.990 --> 00:01:43.170
You can choose your root password.

39
00:01:43.490 --> 00:01:45.050
I will recommend it to you.

40
00:01:45.130 --> 00:01:46.550
You also choose a simple one because we

41
00:01:46.550 --> 00:01:48.650
are installing MySQL on our Windows PC for

42
00:01:48.650 --> 00:01:48.750
learning.

43
00:01:48.750 --> 00:01:51.250
So you don't have to choose a very

44
00:01:51.250 --> 00:01:51.950
strong password.

45
00:01:52.130 --> 00:01:53.270
Because no one is going to hack it.

46
00:01:54.310 --> 00:01:56.690
But when we deploy MySQL server on production,

47
00:01:57.430 --> 00:02:00.170
then your password strength should be very good.

48
00:02:00.430 --> 00:02:01.930
I click on next with that said.

49
00:02:02.510 --> 00:02:03.170
And we wait.

50
00:02:03.590 --> 00:02:04.650
And here you will click on next.

51
00:02:05.390 --> 00:02:06.210
And again click on next.

52
00:02:06.870 --> 00:02:07.410
Click on execute.

53
00:02:08.330 --> 00:02:10.390
And I am waiting here for it to

54
00:02:10.390 --> 00:02:11.730
instal and start.

55
00:02:12.390 --> 00:02:13.490
And here you can see that I will

56
00:02:13.490 --> 00:02:13.970
click on finish.

57
00:02:15.150 --> 00:02:16.710
Next and here finish.

58
00:02:16.710 --> 00:02:18.530
Means my MySQL server is installed.

59
00:02:18.830 --> 00:02:19.350
Now what to do?

60
00:02:19.670 --> 00:02:22.510
Now open a new tab and instal MySQL

61
00:02:22.510 --> 00:02:22.790
Workbench.

62
00:02:23.350 --> 00:02:24.310
Now you will ask what is this?

63
00:02:24.870 --> 00:02:26.430
You can download MySQL Workbench.

64
00:02:27.410 --> 00:02:29.390
Just like we downloaded MySQL server.

65
00:02:30.670 --> 00:02:31.190
Click on download.

66
00:02:32.510 --> 00:02:32.970
No thanks.

67
00:02:33.070 --> 00:02:33.970
Just start my download.

68
00:02:34.730 --> 00:02:36.690
And I will run the installer.

69
00:02:38.150 --> 00:02:40.170
And after that I will instal it too.

70
00:02:40.310 --> 00:02:41.350
Just like you instal a game.

71
00:02:41.510 --> 00:02:43.050
I will tell you what is the difference

72
00:02:43.050 --> 00:02:47.150
between MySQL server and MySQL Workbench.

73
00:02:47.450 --> 00:02:51.810
So basically MySQL server is the core engine

74
00:02:51.810 --> 00:02:52.930
of MySQL.

75
00:02:53.610 --> 00:02:57.810
But MySQL Workbench helps you to connect to

76
00:02:57.810 --> 00:02:59.590
this instance of MySQL server.

77
00:02:59.990 --> 00:03:01.670
If you don't understand, then you can understand

78
00:03:01.670 --> 00:03:05.230
that the main logic of SQL, means how

79
00:03:05.230 --> 00:03:08.050
SQL is being executed, the whole engine, in

80
00:03:08.050 --> 00:03:09.470
which definitely logic is written.

81
00:03:09.890 --> 00:03:12.350
And it takes your SQL queries, gives data,

82
00:03:13.230 --> 00:03:16.530
stores data, deletes data, performs all operations, that

83
00:03:16.530 --> 00:03:17.230
is MySQL.

84
00:03:17.710 --> 00:03:18.810
What is MySQL Workbench?

85
00:03:19.190 --> 00:03:20.110
It is a tool that helps us to

86
00:03:20.110 --> 00:03:20.650
connect to this MySQL.

87
00:03:22.530 --> 00:03:23.790
It will be clear to you later.

88
00:03:24.050 --> 00:03:25.410
But now we will instal MySQL Workbench.

89
00:03:25.970 --> 00:03:29.370
Next, next, next, instal and wait.

90
00:03:30.710 --> 00:03:31.890
And after that, as soon as we instal

91
00:03:31.890 --> 00:03:36.070
MySQL Workbench, we will run MySQL Workbench.

92
00:03:36.850 --> 00:03:39.190
And after running, we will connect to our

93
00:03:39.190 --> 00:03:40.190
MySQL instance.

94
00:03:40.190 --> 00:03:42.750
Means this MySQL server, which we have installed.

95
00:03:43.530 --> 00:03:44.330
We made a password, etc.

96
00:03:45.510 --> 00:03:46.210
Just a while ago.

97
00:03:46.370 --> 00:03:48.550
We will connect our MySQL Workbench to MySQL

98
00:03:48.550 --> 00:03:49.050
server.

99
00:03:50.290 --> 00:03:51.290
Ok, so this is happening.

100
00:03:51.370 --> 00:03:51.990
Let's wait for it.

101
00:03:52.170 --> 00:03:54.090
Now here you can see that the setup

102
00:03:54.090 --> 00:03:54.530
is finished.

103
00:03:54.870 --> 00:03:55.210
Click on finish.

104
00:03:55.990 --> 00:03:57.510
And now we are all set.

105
00:03:57.670 --> 00:04:00.510
As you can see, Welcome to MySQL Workbench

106
00:04:00.510 --> 00:04:00.870
is written here.

107
00:04:01.210 --> 00:04:02.370
Click on plus here.

108
00:04:02.550 --> 00:04:04.210
Because we don't have any MySQL connections yet.

109
00:04:04.950 --> 00:04:06.110
So we will click on plus here.

110
00:04:06.690 --> 00:04:08.050
And here we will click on OK.

111
00:04:08.050 --> 00:04:10.090
Let's give the connection name localhost.

112
00:04:10.270 --> 00:04:10.550
Click on OK.

113
00:04:11.390 --> 00:04:12.470
And when you connect to it, it will

114
00:04:12.470 --> 00:04:12.910
ask for the password.

115
00:04:13.250 --> 00:04:15.190
This is the same password that you set

116
00:04:15.190 --> 00:04:16.149
a while ago.

117
00:04:16.310 --> 00:04:18.390
So you can see here, you get to

118
00:04:18.390 --> 00:04:18.670
see something like this.

119
00:04:19.290 --> 00:04:21.570
It simply means that your MySQL has been

120
00:04:21.570 --> 00:04:22.650
installed completely successfully.

121
00:04:23.490 --> 00:04:23.670
Okay.

122
00:04:24.050 --> 00:04:24.970
You don't need to do anything.

123
00:04:26.070 --> 00:04:27.830
Now what you have to do simply, you

124
00:04:27.830 --> 00:04:28.790
have to write your queries here.

125
00:04:28.790 --> 00:04:29.970
And by clicking here, you have to run

126
00:04:29.970 --> 00:04:30.470
your queries.

127
00:04:31.310 --> 00:04:35.230
And after that, you will get the output

128
00:04:35.230 --> 00:04:35.990
of your queries here.

129
00:04:35.990 --> 00:04:37.470
We will see how to do this in

130
00:04:37.470 --> 00:04:38.290
a little while.

131
00:04:38.630 --> 00:04:39.970
But I hope you have reached this screen.

132
00:04:40.630 --> 00:04:41.830
Your MySQL has run.

133
00:04:42.090 --> 00:04:43.250
Your connection has been successful.

134
00:04:43.710 --> 00:04:45.550
And as I went, so did yours.

135
00:04:46.170 --> 00:04:49.170
In the coming videos, we will see MySQL

136
00:04:49.170 --> 00:04:49.270
in more detail.

137
00:04:49.350 --> 00:04:50.950
I hope you are enjoying this course so

138
00:04:50.950 --> 00:04:51.250
far.

139
00:04:51.810 --> 00:04:53.010
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:02.840
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, welcome back and now I will

2
00:00:02.840 --> 00:00:05.560
tell you how you can start mysql workbench.

3
00:00:06.600 --> 00:00:08.160
So what you have to do here is

4
00:00:08.160 --> 00:00:09.560
to write mysql workbench.

5
00:00:10.240 --> 00:00:13.200
Click on start and your mysql workbench will

6
00:00:13.200 --> 00:00:14.760
start as soon as you click on it.

7
00:00:15.180 --> 00:00:17.200
So you start it first and then I

8
00:00:17.200 --> 00:00:18.160
will tell you what to do.

9
00:00:18.560 --> 00:00:21.600
Once you have started it, you click here

10
00:00:21.600 --> 00:00:22.840
and you will be connected.

11
00:00:23.140 --> 00:00:24.220
Definitely you will have to enter the password

12
00:00:24.220 --> 00:00:26.100
and this is the same password that you

13
00:00:26.100 --> 00:00:27.400
had chosen at the time of installation.

14
00:00:28.000 --> 00:00:29.960
And here you can see, you will see

15
00:00:29.960 --> 00:00:30.640
something like this.

16
00:00:31.100 --> 00:00:32.160
Now what we will do is we will

17
00:00:32.160 --> 00:00:33.280
make our first database.

18
00:00:33.880 --> 00:00:35.220
But how do you make a database?

19
00:00:35.340 --> 00:00:35.860
You will ask me.

20
00:00:36.640 --> 00:00:38.320
It is very easy to make a database.

21
00:00:38.500 --> 00:00:42.420
Now write create database and then write the

22
00:00:42.420 --> 00:00:43.500
name of the database.

23
00:00:44.200 --> 00:00:45.120
Starter SQL.

24
00:00:45.360 --> 00:00:46.720
I have also put a semicolon here.

25
00:00:46.840 --> 00:00:47.560
Now see what I have written.

26
00:00:48.000 --> 00:00:50.580
In Create Capital, in Database Capital, in Starter

27
00:00:50.580 --> 00:00:51.220
SQL Small.

28
00:00:51.500 --> 00:00:52.040
And why have I written in small?

29
00:00:52.640 --> 00:00:54.260
I have written in small because I want

30
00:00:54.260 --> 00:00:56.220
this to be the name of my database.

31
00:00:56.220 --> 00:00:59.640
I have given my name to the database.

32
00:00:59.820 --> 00:01:00.580
If you want, you can give something else.

33
00:01:01.160 --> 00:01:02.560
If you want, you can give it the

34
00:01:02.560 --> 00:01:03.400
name ecom.

35
00:01:04.140 --> 00:01:05.260
You can also give starter SQL.

36
00:01:05.900 --> 00:01:06.300
You can also give ecom.

37
00:01:06.940 --> 00:01:09.700
Now you want your database to be used.

38
00:01:10.020 --> 00:01:12.420
So we will write here use ecom.

39
00:01:12.640 --> 00:01:15.040
So my database named ecom will be used.

40
00:01:15.400 --> 00:01:16.580
So this line is saying that make a

41
00:01:16.580 --> 00:01:18.160
new database whose name is ecom.

42
00:01:18.440 --> 00:01:20.160
And this line is saying that whatever queries

43
00:01:20.160 --> 00:01:21.000
will run from now will run on ecom.

44
00:01:21.860 --> 00:01:23.000
Because you can make multiple databases.

45
00:01:23.620 --> 00:01:24.580
And you will work on different databases.

46
00:01:24.580 --> 00:01:26.760
Suppose you are doing different projects.

47
00:01:27.100 --> 00:01:28.680
So you will make a different database for

48
00:01:28.680 --> 00:01:28.780
each project.

49
00:01:29.300 --> 00:01:31.380
For instance, if you have an ecommerce website.

50
00:01:31.920 --> 00:01:33.480
You will make a database named ecom for

51
00:01:33.480 --> 00:01:33.580
it.

52
00:01:34.320 --> 00:01:36.520
And suppose you have made a hobby project.

53
00:01:36.840 --> 00:01:38.640
In which you save pdf by merging.

54
00:01:38.880 --> 00:01:41.360
For that you will make another database whose

55
00:01:41.360 --> 00:01:42.740
name will be pdf utils.

56
00:01:43.160 --> 00:01:44.340
And if you have made a third project.

57
00:01:44.820 --> 00:01:46.900
Which let's say you have made an application

58
00:01:46.900 --> 00:01:48.040
for customer grievances.

59
00:01:50.100 --> 00:01:51.240
So you will name it something else.

60
00:01:51.500 --> 00:01:52.260
You got the point.

61
00:01:52.260 --> 00:01:54.400
Different databases will be made for different applications.

62
00:01:54.580 --> 00:01:55.440
And for this one we have named it

63
00:01:55.440 --> 00:01:55.780
ecom.

64
00:01:56.540 --> 00:01:57.720
Now you have written this script.

65
00:01:58.000 --> 00:01:58.800
Now how will you run this script?

66
00:01:59.580 --> 00:02:01.120
To run this script, you will click here.

67
00:02:01.260 --> 00:02:03.440
See here execute the selected portion of the

68
00:02:03.440 --> 00:02:04.220
script or everything.

69
00:02:04.440 --> 00:02:05.320
If there is no selection.

70
00:02:06.320 --> 00:02:06.980
I will click on this.

71
00:02:07.180 --> 00:02:08.400
And now see here I can see two

72
00:02:08.400 --> 00:02:08.780
messages.

73
00:02:09.120 --> 00:02:09.520
One is visible.

74
00:02:10.440 --> 00:02:12.700
Create database ecom one row affected.

75
00:02:12.800 --> 00:02:15.040
Means your query is running.

76
00:02:15.260 --> 00:02:16.200
See here green tick is coming.

77
00:02:16.660 --> 00:02:17.400
This is also running.

78
00:02:17.580 --> 00:02:18.200
Green tick is coming.

79
00:02:18.280 --> 00:02:19.080
Means these two are running.

80
00:02:19.640 --> 00:02:21.220
Now you can see here administration is written.

81
00:02:21.920 --> 00:02:22.560
Schemas is written.

82
00:02:22.800 --> 00:02:23.460
You click on schemas.

83
00:02:24.240 --> 00:02:25.140
As soon as you click on schemas.

84
00:02:25.660 --> 00:02:26.860
Your database will be visible here.

85
00:02:26.920 --> 00:02:27.280
Ecom.

86
00:02:27.380 --> 00:02:28.560
This database will not be visible before.

87
00:02:28.640 --> 00:02:29.140
It will be visible later.

88
00:02:29.380 --> 00:02:29.900
And if it is not visible.

89
00:02:30.040 --> 00:02:31.160
Then you click on refresh here.

90
00:02:31.620 --> 00:02:32.040
It will be visible.

91
00:02:32.900 --> 00:02:34.060
Let's see if we have tables in this

92
00:02:34.060 --> 00:02:34.720
database or not.

93
00:02:34.860 --> 00:02:35.940
No we don't have any table.

94
00:02:36.620 --> 00:02:37.740
And because we don't have a table.

95
00:02:38.140 --> 00:02:39.100
That's why we are going to make a

96
00:02:39.100 --> 00:02:39.300
table.

97
00:02:40.400 --> 00:02:41.480
And we will make a table in the

98
00:02:41.480 --> 00:02:41.880
next video.

99
00:02:42.760 --> 00:02:43.840
And we will also populate that table.

100
00:02:44.380 --> 00:02:45.400
I hope you got to know.

101
00:02:45.480 --> 00:02:46.400
Where do you run queries?

102
00:02:46.660 --> 00:02:47.360
You got to know.

103
00:02:47.540 --> 00:02:49.320
How you can see your tables etc.

104
00:02:49.900 --> 00:02:51.200
Now if you want.

105
00:02:51.380 --> 00:02:52.840
Then whatever script you have written.

106
00:02:53.120 --> 00:02:54.140
You can also save it.

107
00:02:54.740 --> 00:02:56.100
Now here my script is of only two

108
00:02:56.100 --> 00:02:56.360
lines.

109
00:02:56.680 --> 00:02:58.780
So I don't have any point to save

110
00:02:58.780 --> 00:02:58.880
here.

111
00:02:58.880 --> 00:03:00.160
Because I will type it again.

112
00:03:00.640 --> 00:03:01.880
Just think I would have written something.

113
00:03:01.980 --> 00:03:02.780
Which is of 40 lines.

114
00:03:03.040 --> 00:03:03.640
Which is of 50 lines.

115
00:03:03.900 --> 00:03:04.780
Which has a lot of data.

116
00:03:05.420 --> 00:03:06.240
Then I would want.

117
00:03:06.340 --> 00:03:07.360
That I don't write a script again and

118
00:03:07.360 --> 00:03:07.580
again.

119
00:03:08.080 --> 00:03:08.660
Or I can send it to my friends.

120
00:03:09.600 --> 00:03:10.040
Or I can send it to you.

121
00:03:10.880 --> 00:03:13.220
Because if I will send that script to

122
00:03:13.220 --> 00:03:13.320
you.

123
00:03:13.320 --> 00:03:14.540
Then you will also be able to run

124
00:03:14.540 --> 00:03:14.640
it.

125
00:03:14.780 --> 00:03:15.400
By copying and pasting.

126
00:03:15.760 --> 00:03:16.740
Or by opening.

127
00:03:17.420 --> 00:03:18.880
So how do you save a script?

128
00:03:18.880 --> 00:03:20.400
What do you do to save a script?

129
00:03:21.000 --> 00:03:21.820
Just click on file.

130
00:03:22.440 --> 00:03:23.200
When you click on file.

131
00:03:23.700 --> 00:03:24.560
You will see.

132
00:03:25.140 --> 00:03:27.080
Save script option Click on save script.

133
00:03:27.940 --> 00:03:29.060
And here it is saying to me.

134
00:03:29.460 --> 00:03:31.000
Save it on any location.

135
00:03:31.160 --> 00:03:31.680
So I will put its name.

136
00:03:33.220 --> 00:03:35.160
Sample.sql So I will write sample.

137
00:03:35.880 --> 00:03:36.480
Save it.

138
00:03:36.620 --> 00:03:39.480
Sample.sql will save it.

139
00:03:39.640 --> 00:03:41.460
And I can give this sample.sql file

140
00:03:41.460 --> 00:03:41.820
to anyone.

141
00:03:42.920 --> 00:03:44.700
So sample.sql file will come on my

142
00:03:44.700 --> 00:03:45.100
computer.

143
00:03:46.020 --> 00:03:47.780
And I can give that sample.sql file

144
00:03:47.780 --> 00:03:48.400
to anyone.

145
00:03:49.180 --> 00:03:50.680
I will show you, it has come in

146
00:03:50.680 --> 00:03:53.720
my PC, I will open my document folder,

147
00:03:54.440 --> 00:03:55.980
so you can see here this sample.sql

148
00:03:55.980 --> 00:03:58.420
file has come and I can send it

149
00:03:58.420 --> 00:04:00.440
to anyone, I can right click and open

150
00:04:00.440 --> 00:04:02.320
with code and it will open in VS

151
00:04:02.320 --> 00:04:04.500
code or I can open with mysql workbench

152
00:04:04.500 --> 00:04:07.540
directly, it will open in my workbench, so

153
00:04:07.540 --> 00:04:11.720
if you want you can send it easily

154
00:04:11.720 --> 00:04:23.580
to anyone or if you want to I

155
00:04:23.580 --> 00:04:25.380
hope you are enjoying this course so far,

156
00:04:25.880 --> 00:04:27.020
see you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.030
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now I will give you such

2
00:00:02.030 --> 00:00:04.370
a starter script which will make your life

3
00:00:04.370 --> 00:00:04.990
very easy.

4
00:00:05.250 --> 00:00:07.890
Plus, you will be able to bring your

5
00:00:07.890 --> 00:00:10.330
data into MySQL Workbench without much thinking.

6
00:00:10.890 --> 00:00:12.170
Let me tell you what I am talking

7
00:00:12.170 --> 00:00:12.270
about.

8
00:00:12.330 --> 00:00:13.970
First of all, let's open the Workbench and

9
00:00:13.970 --> 00:00:14.790
put your password etc.

10
00:00:15.790 --> 00:00:17.710
And click here and put the password you

11
00:00:17.710 --> 00:00:18.210
selected.

12
00:00:18.870 --> 00:00:20.190
Okay, I have also put it and my

13
00:00:20.190 --> 00:00:22.550
MySQL Workbench has opened.

14
00:00:22.790 --> 00:00:24.690
One thing you must have noted here that

15
00:00:24.690 --> 00:00:26.610
whatever script I had written here, whatever script

16
00:00:26.610 --> 00:00:28.110
I had opened earlier, it is already open

17
00:00:28.110 --> 00:00:28.330
here.

18
00:00:28.330 --> 00:00:30.050
So, if you want this script to be

19
00:00:30.050 --> 00:00:31.290
safe, you can close it.

20
00:00:31.409 --> 00:00:32.770
It will be safe wherever it is saved

21
00:00:32.770 --> 00:00:33.990
in your computer.

22
00:00:34.730 --> 00:00:36.490
Then you can click on the file and

23
00:00:36.490 --> 00:00:38.610
open the new script here.

24
00:00:39.190 --> 00:00:40.230
New query tab.

25
00:00:40.410 --> 00:00:41.110
There is a new query tab.

26
00:00:41.390 --> 00:00:41.770
There is no new script.

27
00:00:42.010 --> 00:00:42.730
There is a new query tab.

28
00:00:43.030 --> 00:00:43.990
Okay, that's it.

29
00:00:44.190 --> 00:00:45.330
Now, what will you do here?

30
00:00:45.670 --> 00:00:47.670
Here you will see which databases you have.

31
00:00:47.770 --> 00:00:48.830
Click on refresh here.

32
00:00:49.330 --> 00:00:50.170
Okay, now I have a database named Ecom.

33
00:00:51.330 --> 00:00:52.310
And I had made it.

34
00:00:52.790 --> 00:00:53.590
And I had made it in the last

35
00:00:53.590 --> 00:00:53.950
video.

36
00:00:54.570 --> 00:00:55.910
And there are no tables in it at

37
00:00:55.910 --> 00:00:56.190
all.

38
00:00:56.190 --> 00:00:57.310
It was just a database.

39
00:00:57.990 --> 00:00:59.570
So, what we will do here is that

40
00:00:59.570 --> 00:01:00.030
we will blow this database.

41
00:01:00.750 --> 00:01:02.050
What you have to do to blow it?

42
00:01:02.250 --> 00:01:04.610
You have to write drop database.

43
00:01:05.630 --> 00:01:06.510
Drop database.

44
00:01:06.730 --> 00:01:07.530
And after this, you write the name of

45
00:01:07.530 --> 00:01:08.070
this database.

46
00:01:09.010 --> 00:01:09.690
What will happen with this?

47
00:01:09.830 --> 00:01:10.750
Your database will be blown.

48
00:01:11.050 --> 00:01:12.910
But there is a better way than this.

49
00:01:13.710 --> 00:01:15.430
Drop database if exists.

50
00:01:16.210 --> 00:01:17.070
What will happen if you do this?

51
00:01:17.510 --> 00:01:19.570
If your database exists, it will be blown.

52
00:01:19.830 --> 00:01:20.870
If it does not exist, it will not

53
00:01:20.870 --> 00:01:21.090
be blown.

54
00:01:21.270 --> 00:01:22.070
Okay, it's a simple thing.

55
00:01:22.450 --> 00:01:23.130
So, I will run it.

56
00:01:23.130 --> 00:01:24.110
If I run it, you will see this

57
00:01:24.110 --> 00:01:24.810
green tick here.

58
00:01:24.910 --> 00:01:27.910
Which means that my query has run.

59
00:01:28.550 --> 00:01:30.090
And this database Ecom has been dropped.

60
00:01:30.390 --> 00:01:31.170
You can see here.

61
00:01:31.610 --> 00:01:33.010
And now I can do my work from

62
00:01:33.010 --> 00:01:33.110
the beginning.

63
00:01:33.510 --> 00:01:35.750
Before I tell you how we have to

64
00:01:35.750 --> 00:01:36.650
do the rest of the work.

65
00:01:37.150 --> 00:01:38.550
I want to tell you about CRUD operations.

66
00:01:39.590 --> 00:01:42.590
CRUD stands for create, read, update and delete.

67
00:01:42.730 --> 00:01:44.830
Create means you will create data.

68
00:01:45.230 --> 00:01:46.770
You will make a database, you will make

69
00:01:46.770 --> 00:01:46.870
a table.

70
00:01:46.990 --> 00:01:49.070
You will insert rows in it.

71
00:01:49.410 --> 00:01:50.350
After this comes read.

72
00:01:50.350 --> 00:01:53.150
Read means that you will read the data.

73
00:01:53.410 --> 00:01:55.290
That is, you will retrieve the data that

74
00:01:55.290 --> 00:01:56.110
you have saved.

75
00:01:56.770 --> 00:01:58.370
This work is done by using select.

76
00:01:58.910 --> 00:02:00.090
After this comes update.

77
00:02:00.290 --> 00:02:01.830
Which is done by using update.

78
00:02:02.590 --> 00:02:04.650
If you want to modify existing data.

79
00:02:04.810 --> 00:02:06.050
Then you do it with the update statement.

80
00:02:06.570 --> 00:02:07.509
And after this comes delete.

81
00:02:07.889 --> 00:02:09.350
And for delete, there is a delete statement.

82
00:02:09.530 --> 00:02:11.410
So, there are four basic operations.

83
00:02:11.850 --> 00:02:14.050
Create, read, update and delete.

84
00:02:14.450 --> 00:02:17.330
And these four basic operations can be performed

85
00:02:17.330 --> 00:02:18.390
on any database.

86
00:02:19.030 --> 00:02:21.430
So here we have a clean slate.

87
00:02:21.650 --> 00:02:23.270
We have not made any database at all.

88
00:02:23.570 --> 00:02:24.450
So what we will do from the beginning,

89
00:02:24.550 --> 00:02:24.930
we will make a database.

90
00:02:25.870 --> 00:02:29.210
And I will write here, create database ecom.

91
00:02:29.450 --> 00:02:32.110
And after this I will say, use ecom.

92
00:02:32.410 --> 00:02:33.970
So I made a database here.

93
00:02:34.070 --> 00:02:35.290
I have not run this query yet.

94
00:02:35.670 --> 00:02:37.130
As soon as I run it, all the

95
00:02:37.130 --> 00:02:37.850
queries will be executed line by line.

96
00:02:38.050 --> 00:02:39.450
Database will be made, database will be used.

97
00:02:40.130 --> 00:02:41.350
Now what I am going to write, you

98
00:02:41.350 --> 00:02:42.130
see here.

99
00:02:42.830 --> 00:02:43.810
Now what I will do.

100
00:02:44.570 --> 00:02:45.750
I will create a table called orders.

101
00:02:45.750 --> 00:02:49.110
And to create a table called orders, what

102
00:02:49.110 --> 00:02:49.530
I have to do.

103
00:02:49.810 --> 00:02:51.710
I have to write, create table.

104
00:02:52.430 --> 00:02:53.350
Create table.

105
00:02:54.150 --> 00:02:55.450
And after this, what I will do.

106
00:02:55.830 --> 00:02:56.850
I will write orders.

107
00:02:57.030 --> 00:02:59.030
And after writing this, what I will do.

108
00:02:59.630 --> 00:03:02.310
Here, I will tell you what kind of

109
00:03:02.310 --> 00:03:02.610
table it is.

110
00:03:02.690 --> 00:03:04.070
Here I will say, this is order underscore

111
00:03:04.070 --> 00:03:04.410
id.

112
00:03:04.950 --> 00:03:05.930
Its type is int.

113
00:03:06.350 --> 00:03:07.830
And this is a primary key.

114
00:03:07.930 --> 00:03:08.890
Now you will say, what is this primary

115
00:03:08.890 --> 00:03:09.130
key?

116
00:03:09.510 --> 00:03:10.370
We will study about this later.

117
00:03:11.130 --> 00:03:12.750
But for now, I will suggest you people.

118
00:03:13.410 --> 00:03:15.250
As it is.

119
00:03:17.430 --> 00:03:17.670
Copy from below.

120
00:03:18.370 --> 00:03:18.990
And paste it.

121
00:03:19.350 --> 00:03:20.290
Something like this.

122
00:03:20.570 --> 00:03:21.390
Something like this.

123
00:03:22.810 --> 00:03:24.090
But what is this?

124
00:03:24.190 --> 00:03:25.070
What is create table orders?

125
00:03:25.450 --> 00:03:25.830
You will ask.

126
00:03:26.170 --> 00:03:27.290
Explain this.

127
00:03:27.410 --> 00:03:28.690
We will understand everything in the coming time.

128
00:03:29.690 --> 00:03:30.630
Now you copy and paste.

129
00:03:30.890 --> 00:03:32.050
And the reason for copying and pasting is

130
00:03:32.050 --> 00:03:32.270
this.

131
00:03:32.270 --> 00:03:33.130
This is your starter script.

132
00:03:33.810 --> 00:03:35.750
If you run this, what will happen.

133
00:03:35.750 --> 00:03:37.250
Your table will be made.

134
00:03:37.390 --> 00:03:38.250
This will make your table.

135
00:03:39.110 --> 00:03:40.690
And after this, this data will be inserted.

136
00:03:41.290 --> 00:03:43.370
And you will get this with this video.

137
00:03:44.030 --> 00:03:44.410
Attached.

138
00:03:44.850 --> 00:03:45.850
So you can copy and paste it.

139
00:03:47.490 --> 00:03:49.050
You can copy and paste it.

140
00:03:49.170 --> 00:03:51.410
So what did we do?

141
00:03:51.610 --> 00:03:52.750
We made a database named ecom.

142
00:03:52.970 --> 00:03:53.870
We used it.

143
00:03:54.090 --> 00:03:55.770
We made a table named orders.

144
00:03:55.770 --> 00:03:57.490
And we explained it correctly.

145
00:03:58.770 --> 00:04:00.330
Which columns are going to be there.

146
00:04:00.730 --> 00:04:01.630
Order id is a column.

147
00:04:01.630 --> 00:04:02.670
Customer name is a column.

148
00:04:02.810 --> 00:04:03.470
City is a column.

149
00:04:03.590 --> 00:04:04.230
Product is a column.

150
00:04:04.410 --> 00:04:05.310
Category and so on.

151
00:04:06.190 --> 00:04:09.610
We gave exactly the data.

152
00:04:10.230 --> 00:04:10.990
What is the name of the customer?

153
00:04:11.650 --> 00:04:11.950
What is the city?

154
00:04:12.370 --> 00:04:12.690
What is the product?

155
00:04:13.050 --> 00:04:13.410
What is the category?

156
00:04:13.750 --> 00:04:14.110
What is the quantity?

157
00:04:14.510 --> 00:04:15.149
What is the price per unit?

158
00:04:15.769 --> 00:04:16.130
We told all this.

159
00:04:17.390 --> 00:04:19.149
And we inserted all these rows.

160
00:04:20.529 --> 00:04:21.010
We have done this much.

161
00:04:21.010 --> 00:04:22.490
Why did we do this?

162
00:04:22.530 --> 00:04:23.470
To add sample data.

163
00:04:24.270 --> 00:04:25.110
So let's run it.

164
00:04:25.550 --> 00:04:26.830
Let's run this SQL script.

165
00:04:27.950 --> 00:04:29.430
I will run it here.

166
00:04:30.630 --> 00:04:32.310
This SQL script has been run without any

167
00:04:32.310 --> 00:04:32.410
error.

168
00:04:33.150 --> 00:04:34.530
I will give this SQL script to you.

169
00:04:35.050 --> 00:04:36.490
And you can copy and paste it.

170
00:04:36.930 --> 00:04:38.750
This will make your order stable.

171
00:04:39.310 --> 00:04:42.550
And your sample data will be inserted.

172
00:04:43.130 --> 00:04:43.690
And your sample data will be inserted.

173
00:04:43.690 --> 00:04:44.730
After that, whatever we do, We will do

174
00:04:44.730 --> 00:04:45.390
it on this sample data.

175
00:04:46.030 --> 00:04:48.630
And how did this sample script get created?

176
00:04:48.630 --> 00:04:49.870
Don't take tension.

177
00:04:50.150 --> 00:04:50.890
I will explain this properly.

178
00:04:51.350 --> 00:04:52.570
You will understand each line and word.

179
00:04:53.430 --> 00:04:54.690
We are copying and pasting now.

180
00:04:54.770 --> 00:04:55.950
It doesn't mean that we will only copy

181
00:04:55.950 --> 00:04:56.310
and paste.

182
00:04:57.250 --> 00:04:58.450
SQL is very important.

183
00:04:58.670 --> 00:05:00.690
I will explain you line by line, word

184
00:05:00.690 --> 00:05:01.890
by word, character by character.

185
00:05:02.690 --> 00:05:03.590
I will click on the file.

186
00:05:04.850 --> 00:05:05.710
I will save this.

187
00:05:06.350 --> 00:05:09.410
I will name this Starter SQL.

188
00:05:11.570 --> 00:05:12.990
And you will get this file.

189
00:05:13.210 --> 00:05:14.890
You can either open it and run it.

190
00:05:14.910 --> 00:05:16.510
Or you can copy and paste it.

191
00:05:16.510 --> 00:05:16.790
You can copy and paste it.

192
00:05:17.030 --> 00:05:18.110
As you feel comfortable.

193
00:05:19.830 --> 00:05:21.370
Now I will close this.

194
00:05:22.390 --> 00:05:22.830
I will refresh.

195
00:05:23.130 --> 00:05:24.890
We have a database called Ecom.

196
00:05:25.130 --> 00:05:26.790
We have a table called Orders.

197
00:05:27.410 --> 00:05:28.670
There are columns in this.

198
00:05:29.070 --> 00:05:30.430
You can see it here.

199
00:05:32.670 --> 00:05:35.330
And we can also see What are the

200
00:05:35.330 --> 00:05:36.130
indexes in this?

201
00:05:36.130 --> 00:05:36.670
What are the foreign keys?

202
00:05:37.090 --> 00:05:37.410
What are the triggers?

203
00:05:37.790 --> 00:05:38.410
You will also understand this.

204
00:05:40.250 --> 00:05:41.730
For now, you understood the columns.

205
00:05:41.730 --> 00:05:43.610
What are the columns in this?

206
00:05:43.670 --> 00:05:44.350
These are all columns.

207
00:05:44.610 --> 00:05:47.630
Now we will click on the file.

208
00:05:48.270 --> 00:05:48.930
We will click on the new query tab.

209
00:05:49.770 --> 00:05:50.670
We will write a simple query.

210
00:05:58.290 --> 00:05:59.390
But which database do you want to use?

211
00:05:59.830 --> 00:06:01.310
You have to use Ecom.

212
00:06:02.310 --> 00:06:02.850
Use Ecom.

213
00:06:04.790 --> 00:06:05.890
Fetch everything from orders.

214
00:06:06.530 --> 00:06:07.050
Run it.

215
00:06:07.450 --> 00:06:08.450
You can see the data.

216
00:06:08.450 --> 00:06:09.990
This is the same data that we have

217
00:06:09.990 --> 00:06:10.470
inserted.

218
00:06:11.130 --> 00:06:12.510
Amish Sharma's city is Delhi.

219
00:06:12.810 --> 00:06:13.390
He ordered a laptop.

220
00:06:14.810 --> 00:06:15.710
Quantity 1 from category electronics.

221
00:06:15.830 --> 00:06:16.370
He ordered a laptop worth 65,000.

222
00:06:17.630 --> 00:06:18.990
He got a discount of 10%.

223
00:06:18.990 --> 00:06:20.610
He paid with a credit card.

224
00:06:20.810 --> 00:06:23.070
He gave a rating of 5 out of

225
00:06:23.070 --> 00:06:23.330
5.

226
00:06:23.570 --> 00:06:24.910
He enjoyed running the laptop.

227
00:06:25.890 --> 00:06:27.330
Neha Verma ordered a headphone.

228
00:06:28.210 --> 00:06:29.970
Rohit Gupta ordered a water bottle.

229
00:06:30.250 --> 00:06:30.770
And so on.

230
00:06:31.090 --> 00:06:31.910
You can see all this.

231
00:06:33.630 --> 00:06:35.230
Select star from orders.

232
00:06:35.230 --> 00:06:38.170
In the coming videos, we will see how

233
00:06:38.170 --> 00:06:40.610
we can do these operations individually.

234
00:06:41.230 --> 00:06:46.370
We will see how we can copy and

235
00:06:46.370 --> 00:06:50.030
paste Which data type is a date?

236
00:06:50.450 --> 00:06:50.950
What is a var char?

237
00:06:52.050 --> 00:06:53.350
What is int?

238
00:06:54.050 --> 00:06:55.750
We will see all this in detail.

239
00:06:56.330 --> 00:06:58.830
We will also see how we can make

240
00:06:58.830 --> 00:06:59.550
a table.

241
00:06:59.890 --> 00:07:01.410
If we want to design our own table,

242
00:07:01.410 --> 00:07:02.150
how will we do that?

243
00:07:02.630 --> 00:07:04.190
I hope you are enjoying this course so

244
00:07:04.190 --> 00:07:04.450
far.

245
00:07:05.030 --> 00:07:06.250
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:01.870
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, in the last video, we inserted

2
00:00:01.870 --> 00:00:04.930
data, made a database and used it, ran

3
00:00:04.930 --> 00:00:06.370
select query and insert query.

4
00:00:06.850 --> 00:00:09.010
But, we will take a step back and

5
00:00:09.010 --> 00:00:10.870
understand how things work.

6
00:00:11.650 --> 00:00:12.990
First of all, I want to tell you

7
00:00:12.990 --> 00:00:13.830
about data types.

8
00:00:14.250 --> 00:00:15.210
So, let's close this SQL file.

9
00:00:16.150 --> 00:00:17.750
To close the results, click here.

10
00:00:17.870 --> 00:00:19.190
As you can see here, click here.

11
00:00:19.390 --> 00:00:21.310
Since I have not saved any SQL file,

12
00:00:21.950 --> 00:00:24.730
I can delete it and write my code

13
00:00:24.730 --> 00:00:24.970
directly here.

14
00:00:25.730 --> 00:00:26.850
Right now, I have a database called Ecom,

15
00:00:26.850 --> 00:00:29.890
which has a table called Orders, which contains

16
00:00:29.890 --> 00:00:30.310
data.

17
00:00:30.770 --> 00:00:32.850
But, what I will do here is, I

18
00:00:32.850 --> 00:00:34.090
will take things from the beginning and explain

19
00:00:34.090 --> 00:00:38.110
to you how data types work in any

20
00:00:38.110 --> 00:00:40.470
SQL database table.

21
00:00:40.770 --> 00:00:41.290
Now, what is a table?

22
00:00:42.110 --> 00:00:45.770
A table is a place where we store

23
00:00:45.770 --> 00:00:45.870
data.

24
00:00:46.590 --> 00:00:48.150
So, there are tables in a database in

25
00:00:48.150 --> 00:00:48.850
which data is stored.

26
00:00:49.190 --> 00:00:53.130
In every table, we have columns and in

27
00:00:53.130 --> 00:00:55.150
every database, we have a lot of tables.

28
00:00:55.630 --> 00:00:57.890
I want to give you an analogy of

29
00:00:57.890 --> 00:00:57.990
this.

30
00:00:58.030 --> 00:00:58.430
Excel.

31
00:00:58.950 --> 00:00:59.590
I will tell you how Excel is an

32
00:00:59.590 --> 00:00:59.870
analogy.

33
00:01:01.130 --> 00:01:02.750
In an Excel workbook, there can be a

34
00:01:02.750 --> 00:01:03.230
lot of sheets.

35
00:01:03.629 --> 00:01:04.910
Here, you can consider sheets as tables.

36
00:01:06.010 --> 00:01:07.270
Suppose, this is my table 1.

37
00:01:07.750 --> 00:01:08.510
I am just giving an analogy.

38
00:01:08.810 --> 00:01:11.310
I am not saying that MySQL and Excel

39
00:01:11.310 --> 00:01:11.910
are the same thing.

40
00:01:12.030 --> 00:01:12.570
This is not the case at all.

41
00:01:13.150 --> 00:01:14.530
I am just giving you an analogy.

42
00:01:14.910 --> 00:01:16.470
Table 1, Table 2, there can be different

43
00:01:16.470 --> 00:01:17.290
tables here.

44
00:01:17.690 --> 00:01:19.090
And, there can be columns in the table.

45
00:01:19.190 --> 00:01:20.730
For example, there is a serial number, there

46
00:01:20.730 --> 00:01:24.190
is a name, there is an age, there

47
00:01:24.190 --> 00:01:28.590
is a company, there is a joining date,

48
00:01:28.850 --> 00:01:31.530
there is a joining underscore date, and here,

49
00:01:31.710 --> 00:01:32.830
you are inserting data.

50
00:01:33.330 --> 00:01:39.050
For example, the name is Savitri, the age

51
00:01:39.050 --> 00:01:46.970
is 67, the company is Microsoft, the joining

52
00:01:46.970 --> 00:01:52.210
date is June 12, 2000, and suppose, we

53
00:01:52.210 --> 00:01:55.250
have another employee, his name is Raghav, his

54
00:01:55.250 --> 00:01:59.950
age is 35, the company is Google, and

55
00:01:59.950 --> 00:02:03.990
the joining date is 12 January, let's say,

56
00:02:05.250 --> 00:02:05.770
2023.

57
00:02:07.190 --> 00:02:10.470
So, here, your data is being stored.

58
00:02:10.810 --> 00:02:11.670
There is a table 1, there is a

59
00:02:11.670 --> 00:02:12.850
table 2, there will be some more data

60
00:02:12.850 --> 00:02:13.170
stored.

61
00:02:13.830 --> 00:02:15.830
But, SQL does this work in a very

62
00:02:15.830 --> 00:02:16.530
optimal way.

63
00:02:16.890 --> 00:02:17.890
And, it can handle more rows than Excel.

64
00:02:18.510 --> 00:02:21.550
Plus, if you make a mistake, like, if

65
00:02:21.550 --> 00:02:23.450
I insert 56 here, it will take it.

66
00:02:23.770 --> 00:02:24.570
SQL will not take it.

67
00:02:24.610 --> 00:02:26.230
SQL will say that the company's data type

68
00:02:26.230 --> 00:02:28.130
is not matching, you cannot insert 56.

69
00:02:28.350 --> 00:02:30.810
You get to see such things in SQL.

70
00:02:31.190 --> 00:02:32.590
If you insert an invalid date, it will

71
00:02:32.590 --> 00:02:32.830
not take it.

72
00:02:33.210 --> 00:02:35.270
So, there are constraints in SQL.

73
00:02:35.470 --> 00:02:37.830
Plus, when you query the data, you will

74
00:02:37.830 --> 00:02:39.950
say that I want this row, where the

75
00:02:39.950 --> 00:02:42.490
joining date is, let's say, after 2005.

76
00:02:43.630 --> 00:02:44.830
So, you will get all those joining dates

77
00:02:44.830 --> 00:02:46.370
very quickly.

78
00:02:46.370 --> 00:02:48.130
SQL is optimised for that.

79
00:02:48.350 --> 00:02:50.270
But, now you understood what a database is.

80
00:02:50.370 --> 00:02:51.010
Database is like a workbook.

81
00:02:52.730 --> 00:02:53.530
Table is like a sheet.

82
00:02:53.970 --> 00:02:56.810
And, the data in the table, the rows

83
00:02:56.810 --> 00:02:58.830
in SQL, that is, the rows in our

84
00:02:58.830 --> 00:03:01.310
table, you can see it this way.

85
00:03:01.710 --> 00:03:02.790
You can also imagine it this way.

86
00:03:03.410 --> 00:03:04.730
Now, I will close Excel here.

87
00:03:05.030 --> 00:03:05.790
This was just an analogy.

88
00:03:06.330 --> 00:03:07.490
And, what we will do here, we will

89
00:03:07.490 --> 00:03:11.730
make a new table and understand which data

90
00:03:11.730 --> 00:03:12.850
types were used in it.

91
00:03:12.850 --> 00:03:15.470
So, first of all, I would like to

92
00:03:15.470 --> 00:03:18.310
tell you about var char data type.

93
00:03:18.870 --> 00:03:20.830
Var char means variable character.

94
00:03:21.230 --> 00:03:24.070
It stores text with fixed maximum length.

95
00:03:24.250 --> 00:03:25.710
That is, if you give a length, more

96
00:03:25.710 --> 00:03:26.590
characters cannot come.

97
00:03:27.010 --> 00:03:28.630
Int stores integers.

98
00:03:30.010 --> 00:03:33.470
And, primary key means it will uniquely identify

99
00:03:33.470 --> 00:03:34.490
a record.

100
00:03:34.890 --> 00:03:35.310
What does it mean?

101
00:03:36.150 --> 00:03:38.070
Let's say, I am making a table here.

102
00:03:38.270 --> 00:03:39.870
So, I will write create table here.

103
00:03:39.870 --> 00:03:42.410
And, I will write customers here.

104
00:03:42.430 --> 00:03:43.810
Let's say, I am making a table named

105
00:03:43.810 --> 00:03:43.910
customers.

106
00:03:44.490 --> 00:03:45.130
After that, I will open and close this

107
00:03:45.130 --> 00:03:46.570
bracket here in this way.

108
00:03:47.490 --> 00:03:51.410
And, I will write customer underscore id in

109
00:03:51.410 --> 00:03:52.630
it, which will be an integer.

110
00:03:53.830 --> 00:03:55.810
And, primary key will be there.

111
00:03:56.810 --> 00:03:58.590
And, auto increment will be there.

112
00:03:58.710 --> 00:03:59.650
Now, what did I say?

113
00:04:01.370 --> 00:04:02.490
Auto increment will be there.

114
00:04:02.530 --> 00:04:04.650
I said, customer id type is an integer.

115
00:04:05.470 --> 00:04:07.230
What is primary key and auto increment?

116
00:04:07.230 --> 00:04:07.730
I will tell you about auto increment in

117
00:04:07.730 --> 00:04:08.010
short.

118
00:04:08.490 --> 00:04:08.590
I will tell you more about it in

119
00:04:08.590 --> 00:04:09.490
upcoming videos.

120
00:04:09.850 --> 00:04:11.810
Primary key means, it cannot be duplicated.

121
00:04:12.830 --> 00:04:15.510
And, auto increment means, if it is 1,

122
00:04:15.610 --> 00:04:17.130
then next day it will be 2, then

123
00:04:17.130 --> 00:04:18.329
3, then 4, then 5.

124
00:04:18.750 --> 00:04:19.910
That means, you don't need to enter customer

125
00:04:19.910 --> 00:04:20.670
id again and again.

126
00:04:20.930 --> 00:04:21.790
Insert data directly.

127
00:04:21.950 --> 00:04:22.550
And, it will automatically take 1, 2, 3,

128
00:04:22.590 --> 00:04:22.690
4.

129
00:04:23.950 --> 00:04:26.450
We will see about this part later.

130
00:04:27.230 --> 00:04:28.390
Now, you just see this part and this

131
00:04:28.390 --> 00:04:28.650
part.

132
00:04:29.490 --> 00:04:30.950
Customer id is the name of column.

133
00:04:31.490 --> 00:04:32.470
Int means integer.

134
00:04:33.090 --> 00:04:34.830
This is its type, which is stored.

135
00:04:34.830 --> 00:04:36.970
After this, you put comma.

136
00:04:37.490 --> 00:04:38.210
You write name.

137
00:04:38.810 --> 00:04:40.050
I mean, I want to store name.

138
00:04:40.770 --> 00:04:42.650
And, here I will write VARCHAR.

139
00:04:42.890 --> 00:04:43.030
Okay?

140
00:04:43.330 --> 00:04:43.850
VARCHAR.

141
00:04:44.250 --> 00:04:45.190
And, here I will write 100.

142
00:04:45.830 --> 00:04:47.150
Then, we will put comma.

143
00:04:47.770 --> 00:04:49.010
And, I will write here.

144
00:04:49.070 --> 00:04:49.850
Let's copy and paste it.

145
00:04:50.150 --> 00:04:50.690
We will do CTRL-C.

146
00:04:51.470 --> 00:04:54.490
And, I will basically say here, do one

147
00:04:54.490 --> 00:04:54.710
thing.

148
00:04:55.490 --> 00:04:58.350
Make email 150.

149
00:04:58.810 --> 00:05:02.370
Now, see, I am writing reserved keywords of

150
00:05:02.370 --> 00:05:02.910
SQL in capital.

151
00:05:03.650 --> 00:05:06.830
And, I am writing column names in small.

152
00:05:07.150 --> 00:05:09.090
I am doing this purposefully to keep things

153
00:05:09.090 --> 00:05:09.470
clean.

154
00:05:09.970 --> 00:05:10.970
This is highly recommended.

155
00:05:11.150 --> 00:05:11.570
You should also do this.

156
00:05:12.510 --> 00:05:14.610
After this, we will write age and int.

157
00:05:15.590 --> 00:05:18.590
After this, we will write phone and VARCHAR

158
00:05:18.590 --> 00:05:18.990
15.

159
00:05:19.150 --> 00:05:20.110
According to me, phone number of 15 characters

160
00:05:20.110 --> 00:05:20.930
is enough.

161
00:05:21.910 --> 00:05:22.050
Okay?

162
00:05:23.010 --> 00:05:25.870
And, after this, we will write is underscore

163
00:05:25.870 --> 00:05:26.530
active.

164
00:05:26.970 --> 00:05:27.950
Which will be a boolean.

165
00:05:28.250 --> 00:05:30.450
Now, you will say, tell me what all

166
00:05:30.450 --> 00:05:30.550
these are.

167
00:05:30.550 --> 00:05:30.930
I will tell you.

168
00:05:31.030 --> 00:05:31.710
Be patient.

169
00:05:33.010 --> 00:05:35.630
Then, we will say signup underscore date.

170
00:05:36.050 --> 00:05:36.830
Which will be a date type.

171
00:05:37.230 --> 00:05:40.290
Then, we will write created underscore at.

172
00:05:40.610 --> 00:05:42.610
Which will be a date time.

173
00:05:42.970 --> 00:05:44.430
Date time is a different data type.

174
00:05:44.550 --> 00:05:45.550
Date is a different data type.

175
00:05:45.610 --> 00:05:47.070
I will tell you the difference between both.

176
00:05:47.070 --> 00:05:50.430
After this, total underscore spent.

177
00:05:50.990 --> 00:05:52.170
This will be decimal.

178
00:05:53.250 --> 00:05:53.390
Okay?

179
00:05:53.650 --> 00:05:55.530
And, here 10 comma 2.

180
00:05:55.650 --> 00:05:56.610
What is 10 comma 2?

181
00:05:56.670 --> 00:05:57.590
I will tell you in a while.

182
00:05:57.590 --> 00:05:59.670
First, I will run this query and show

183
00:05:59.670 --> 00:06:02.230
you that what we have written also works.

184
00:06:02.490 --> 00:06:03.510
So, I will run it.

185
00:06:03.970 --> 00:06:05.170
Here, you can see a green tick.

186
00:06:05.490 --> 00:06:07.790
It means that we have created a table.

187
00:06:08.690 --> 00:06:10.570
Here, I will refresh it.

188
00:06:10.710 --> 00:06:11.470
You can see that a new table has

189
00:06:11.470 --> 00:06:11.710
been created.

190
00:06:12.170 --> 00:06:13.090
Customers and orders.

191
00:06:13.410 --> 00:06:14.810
I have created a new table named customers.

192
00:06:16.010 --> 00:06:17.490
Is there any data in this table named

193
00:06:17.490 --> 00:06:17.590
customers?

194
00:06:18.430 --> 00:06:18.670
No.

195
00:06:18.790 --> 00:06:20.810
Maybe there is no data in this table

196
00:06:20.810 --> 00:06:20.910
named customers.

197
00:06:21.110 --> 00:06:22.090
So, what we will do?

198
00:06:22.510 --> 00:06:23.670
We will store data in this.

199
00:06:23.670 --> 00:06:26.190
So, guys, here we have the most important

200
00:06:26.190 --> 00:06:27.090
data type, integer.

201
00:06:27.290 --> 00:06:28.030
It stores whole numbers.

202
00:06:28.790 --> 00:06:31.350
If you want to store age, quantity, ID,

203
00:06:32.170 --> 00:06:33.130
this is ideal.

204
00:06:33.570 --> 00:06:35.310
After this, varchar will be used the most.

205
00:06:36.150 --> 00:06:38.270
Suppose, you want to store 10 characters in

206
00:06:38.270 --> 00:06:38.370
a phone number.

207
00:06:38.690 --> 00:06:42.410
You want to store 50 characters in a

208
00:06:42.410 --> 00:06:42.510
name.

209
00:06:42.510 --> 00:06:44.730
You can store any type of character.

210
00:06:45.410 --> 00:06:46.430
Maximum length is n.

211
00:06:46.830 --> 00:06:49.650
You can store name, email, city.

212
00:06:50.650 --> 00:06:52.490
After this, decimal p, s.

213
00:06:52.630 --> 00:06:54.710
p for precision and s for scale.

214
00:06:55.050 --> 00:06:57.150
It stores precise decimal numbers.

215
00:06:57.610 --> 00:06:59.190
Examples are, if you want to store price,

216
00:06:59.910 --> 00:07:04.510
salary, total amount which has been spent, you

217
00:07:04.510 --> 00:07:05.070
can store that.

218
00:07:05.250 --> 00:07:07.410
After this, we have boolean which stores true

219
00:07:07.410 --> 00:07:08.270
or false values.

220
00:07:09.350 --> 00:07:11.710
If you want to ban a user, you

221
00:07:11.710 --> 00:07:11.810
can activate it.

222
00:07:12.030 --> 00:07:12.890
You can make boolean true.

223
00:07:13.590 --> 00:07:14.750
After that, you can filter.

224
00:07:15.130 --> 00:07:17.230
You can only take users where boolean is

225
00:07:17.230 --> 00:07:17.330
false.

226
00:07:17.330 --> 00:07:20.630
Where boolean is true, users won't come to

227
00:07:20.630 --> 00:07:20.730
you.

228
00:07:20.770 --> 00:07:22.650
You can make a flag by activating is.

229
00:07:23.390 --> 00:07:24.290
True or false.

230
00:07:24.350 --> 00:07:27.290
If you want only one value, use boolean.

231
00:07:28.290 --> 00:07:30.110
Then, we have date which stores date.

232
00:07:30.610 --> 00:07:31.250
What does date time do?

233
00:07:32.090 --> 00:07:33.430
It stores date and time together.

234
00:07:34.270 --> 00:07:36.390
If time is also important for you, use

235
00:07:36.390 --> 00:07:36.750
date time.

236
00:07:37.130 --> 00:07:39.110
If you think only date will work, use

237
00:07:39.110 --> 00:07:39.850
date only.

238
00:07:39.970 --> 00:07:40.610
Don't use date time.

239
00:07:40.610 --> 00:07:43.470
You don't want extra data.

240
00:07:44.950 --> 00:07:47.330
These were our common SQL data types.

241
00:07:47.430 --> 00:07:48.290
We have learned how to make a table.

242
00:07:49.090 --> 00:07:50.310
You will get this code.

243
00:07:50.790 --> 00:07:53.290
If you want to write a code below

244
00:07:53.290 --> 00:07:53.390
it.

245
00:07:53.850 --> 00:07:56.730
After that, you want only that code to

246
00:07:56.730 --> 00:07:57.110
be executed.

247
00:07:57.610 --> 00:08:01.730
What do you mean by writing and not

248
00:08:01.730 --> 00:08:02.230
executing?

249
00:08:02.630 --> 00:08:03.510
If it is written, it will be executed.

250
00:08:04.170 --> 00:08:04.850
No.

251
00:08:05.890 --> 00:08:08.210
What you do is, press ctrl forward slash

252
00:08:08.210 --> 00:08:09.050
in your keyboard.

253
00:08:09.270 --> 00:08:11.490
As we comment out in VS code, press

254
00:08:11.490 --> 00:08:12.730
ctrl plus forward slash.

255
00:08:12.930 --> 00:08:14.670
It is on the left of right shift.

256
00:08:15.830 --> 00:08:18.150
Press ctrl forward slash and it will be

257
00:08:18.150 --> 00:08:18.890
commented out.

258
00:08:19.450 --> 00:08:21.990
As it is commented out, it won't work.

259
00:08:22.070 --> 00:08:23.890
There is nothing in this file.

260
00:08:24.270 --> 00:08:26.930
Now, we will delete this table.

261
00:08:27.230 --> 00:08:29.190
To delete this table, we have to write

262
00:08:29.190 --> 00:08:31.350
drop table and table name.

263
00:08:31.730 --> 00:08:32.770
In this case, it is customers.

264
00:08:33.049 --> 00:08:35.289
If I write drop table customers, what will

265
00:08:35.289 --> 00:08:35.389
happen?

266
00:08:35.850 --> 00:08:36.770
This table will be removed.

267
00:08:38.830 --> 00:08:41.210
Now, you can see customers and orders.

268
00:08:41.710 --> 00:08:44.310
I will run SQL statement.

269
00:08:44.890 --> 00:08:46.190
Now, you can see green tick.

270
00:08:46.490 --> 00:08:47.990
Drop table customers is executed.

271
00:08:48.730 --> 00:08:50.490
Now, if you refresh it, there are only

272
00:08:50.490 --> 00:08:50.830
orders.

273
00:08:51.470 --> 00:08:52.670
Customers table is gone.

274
00:08:53.250 --> 00:08:55.930
That was about how you can create a

275
00:08:55.930 --> 00:08:56.890
table, drop a table.

276
00:08:57.390 --> 00:09:01.010
If you comment this out, I will select

277
00:09:01.010 --> 00:09:02.110
it and comment it out.

278
00:09:02.110 --> 00:09:04.470
If I select it and comment it out

279
00:09:04.470 --> 00:09:05.130
again, it will be uncommented.

280
00:09:05.390 --> 00:09:07.170
If I run it again, customers table will

281
00:09:07.170 --> 00:09:07.350
be created.

282
00:09:07.510 --> 00:09:09.250
If I refresh it, you can see customers

283
00:09:09.250 --> 00:09:09.810
table again.

284
00:09:10.730 --> 00:09:15.190
Now, I want it to be my customers.

285
00:09:15.610 --> 00:09:17.130
I have commented out everything.

286
00:09:17.410 --> 00:09:18.670
Now, I will show you rename query.

287
00:09:19.250 --> 00:09:20.890
After that, we will learn how to insert

288
00:09:20.890 --> 00:09:21.870
data in next video.

289
00:09:23.270 --> 00:09:27.850
I will write alter table customers and I

290
00:09:27.850 --> 00:09:32.350
will write rename to clients.

291
00:09:32.430 --> 00:09:33.390
I want to name it clients.

292
00:09:35.630 --> 00:09:37.390
I will run it.

293
00:09:37.570 --> 00:09:38.190
Now, it is customers.

294
00:09:38.990 --> 00:09:41.470
I will run it and refresh it.

295
00:09:41.470 --> 00:09:42.150
Now, it is clients.

296
00:09:42.470 --> 00:09:43.690
You can rename it like this.

297
00:09:44.410 --> 00:09:45.990
You will get this code below.

298
00:09:46.390 --> 00:09:48.750
Select it and comment it out.

299
00:09:48.890 --> 00:09:51.430
You will get this code in handbook and

300
00:09:51.430 --> 00:09:51.910
for copying.

301
00:09:52.650 --> 00:09:54.010
You don't have to worry.

302
00:09:54.310 --> 00:09:56.410
I hope you are understanding everything.

303
00:09:56.410 --> 00:10:00.230
I hope you are enjoying this course so

304
00:10:00.230 --> 00:10:00.570
far.

305
00:10:00.890 --> 00:10:02.130
See you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:01.770
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right guys, in the last video we

2
00:00:01.770 --> 00:00:03.610
saw about data types, we took a good

3
00:00:03.610 --> 00:00:05.730
understanding that what is a varchar and what

4
00:00:05.730 --> 00:00:06.350
is a decimal.

5
00:00:06.750 --> 00:00:09.810
Now we will see how we can insert

6
00:00:09.810 --> 00:00:11.330
data in MySQL.

7
00:00:11.590 --> 00:00:12.950
So I will close this tab, go to

8
00:00:12.950 --> 00:00:16.490
file and tap on new query and here

9
00:00:16.490 --> 00:00:18.470
I will talk about inserting rows.

10
00:00:19.270 --> 00:00:21.110
So we have a table named clients here.

11
00:00:21.530 --> 00:00:22.770
First of all, I will see what is

12
00:00:22.770 --> 00:00:23.390
in this table.

13
00:00:23.950 --> 00:00:25.170
So for that we have to write select

14
00:00:25.170 --> 00:00:28.770
star from and write clients.

15
00:00:29.490 --> 00:00:31.670
But before that, is this database being used

16
00:00:31.670 --> 00:00:32.210
or not?

17
00:00:32.590 --> 00:00:35.810
To ensure this, we will write use ecom.

18
00:00:35.950 --> 00:00:37.670
Means whether our e-commerce database is being

19
00:00:37.670 --> 00:00:38.030
used or not.

20
00:00:38.790 --> 00:00:40.650
This line will ensure that use ecom only.

21
00:00:40.850 --> 00:00:41.950
This line is saying that give me all

22
00:00:41.950 --> 00:00:43.950
the rows from the table named clients.

23
00:00:44.710 --> 00:00:46.390
Let's see, there is nothing in our clients

24
00:00:46.390 --> 00:00:46.690
table.

25
00:00:46.850 --> 00:00:48.010
Come on, let's insert data in it.

26
00:00:48.630 --> 00:00:51.010
So what I will do, I will comment

27
00:00:51.010 --> 00:00:53.790
this out and now I will insert data

28
00:00:53.790 --> 00:00:53.890
here.

29
00:00:54.190 --> 00:00:55.230
So what will I do to insert data?

30
00:00:56.010 --> 00:01:00.910
I will say here, insert into clients.

31
00:01:01.170 --> 00:01:03.930
So I will write here, insert into clients.

32
00:01:04.290 --> 00:01:05.370
Or if the name of your table is

33
00:01:05.370 --> 00:01:07.890
customers, then you will write insert into customers.

34
00:01:08.750 --> 00:01:10.030
And what will you do after this?

35
00:01:10.410 --> 00:01:11.070
You will say, I am going to give

36
00:01:11.070 --> 00:01:11.770
all these things.

37
00:01:12.230 --> 00:01:13.790
I will give name, I will give email,

38
00:01:14.110 --> 00:01:15.250
I will give age, I will give phone,

39
00:01:15.590 --> 00:01:16.870
I will give is underscore active.

40
00:01:18.070 --> 00:01:20.830
And I will give signup underscore date.

41
00:01:20.830 --> 00:01:23.010
And I am writing all this by looking

42
00:01:23.010 --> 00:01:23.110
from here.

43
00:01:24.890 --> 00:01:28.610
And I will give created at, created underscore

44
00:01:28.610 --> 00:01:31.230
at, total underscore spent.

45
00:01:31.330 --> 00:01:32.070
Means I am saying that I will give

46
00:01:32.070 --> 00:01:32.530
all these things.

47
00:01:33.510 --> 00:01:38.210
In this, you have to insert values, values.

48
00:01:38.510 --> 00:01:39.130
What values?

49
00:01:39.590 --> 00:01:41.030
I am telling what values.

50
00:01:41.450 --> 00:01:42.390
First of all, what do you do?

51
00:01:42.550 --> 00:01:43.450
Insert this.

52
00:01:44.330 --> 00:01:46.470
Amit Sharma, okay.

53
00:01:46.470 --> 00:01:49.490
Email will be amit.gmail.com.

54
00:01:50.730 --> 00:01:53.130
And after this, let's say age is 28.

55
00:01:53.490 --> 00:01:55.130
Let's say the phone number is 1, 2,

56
00:01:55.210 --> 00:01:56.830
3, 4, 5, 6, 7, 8, 9, 10.

57
00:01:57.050 --> 00:01:58.190
Okay, let's say this is the phone number.

58
00:01:59.170 --> 00:02:01.690
Then after this, it is active, so it

59
00:02:01.690 --> 00:02:01.890
will be true.

60
00:02:02.370 --> 00:02:03.370
Then after this, we will take the date

61
00:02:03.370 --> 00:02:03.970
in this format.

62
00:02:05.330 --> 00:02:09.389
202501-10 That is, this is our date.

63
00:02:10.630 --> 00:02:12.450
10th January 2025.

64
00:02:12.930 --> 00:02:13.090
Okay.

65
00:02:14.030 --> 00:02:15.210
10th January 2025.

66
00:02:16.010 --> 00:02:17.790
And after this, what will we do?

67
00:02:18.790 --> 00:02:27.170
We will write 202501-10 and 10 colon

68
00:02:27.170 --> 00:02:28.970
30 colon 00.

69
00:02:29.250 --> 00:02:29.350
Okay.

70
00:02:29.910 --> 00:02:34.030
And here we will write 0.56, which

71
00:02:34.030 --> 00:02:34.770
is going to be our total spent.

72
00:02:35.170 --> 00:02:35.590
Okay.

73
00:02:36.230 --> 00:02:36.650
And that's it.

74
00:02:36.690 --> 00:02:37.590
After this, we will put semicolon.

75
00:02:38.250 --> 00:02:39.150
You have to do one more thing.

76
00:02:39.270 --> 00:02:40.850
Zoom out and see if there is any

77
00:02:40.850 --> 00:02:42.510
error of red colour coming here.

78
00:02:42.510 --> 00:02:43.910
Because if there is an error, it means

79
00:02:43.910 --> 00:02:44.630
you have made a mistake in your insert

80
00:02:44.630 --> 00:02:45.410
query.

81
00:02:45.650 --> 00:02:46.230
I didn't make any mistake.

82
00:02:46.570 --> 00:02:47.090
You can see.

83
00:02:47.630 --> 00:02:48.470
Instead of name, I wrote the name.

84
00:02:48.830 --> 00:02:49.490
I wrote email here.

85
00:02:50.010 --> 00:02:50.410
I wrote age here.

86
00:02:50.750 --> 00:02:51.350
I wrote phone here.

87
00:02:51.450 --> 00:02:52.110
It is active, true.

88
00:02:52.670 --> 00:02:53.710
And here is the signup date.

89
00:02:53.970 --> 00:02:54.570
Here is the created date.

90
00:02:54.830 --> 00:02:55.570
Total spend has come.

91
00:02:55.670 --> 00:02:55.790
Okay.

92
00:02:56.310 --> 00:02:57.230
We wrote all this here.

93
00:02:57.690 --> 00:02:58.570
Now we will run it.

94
00:02:58.910 --> 00:03:00.690
And as soon as we run it, our

95
00:03:00.690 --> 00:03:01.350
data has been inserted.

96
00:03:01.950 --> 00:03:02.910
How do I know it has been inserted?

97
00:03:03.830 --> 00:03:04.310
What will I do?

98
00:03:04.430 --> 00:03:05.250
I will comment out this insertion row.

99
00:03:06.630 --> 00:03:08.070
And I will uncomment it.

100
00:03:08.390 --> 00:03:09.930
Oops, I didn't select it properly.

101
00:03:10.690 --> 00:03:11.950
Make sure you select it properly.

102
00:03:11.950 --> 00:03:13.390
Then you press ctrl forward slash.

103
00:03:13.690 --> 00:03:14.490
Otherwise, you will have a problem.

104
00:03:15.690 --> 00:03:17.270
Select it completely and uncomment it.

105
00:03:17.450 --> 00:03:18.390
Now we will run it.

106
00:03:18.790 --> 00:03:20.110
And you see here I have got a

107
00:03:20.110 --> 00:03:21.750
row in which all this data has been

108
00:03:21.750 --> 00:03:22.130
inserted.

109
00:03:22.650 --> 00:03:22.850
Okay.

110
00:03:23.510 --> 00:03:25.870
Here our data has been inserted.

111
00:03:26.630 --> 00:03:29.310
Now let's say that I want to insert

112
00:03:29.310 --> 00:03:30.230
more data again.

113
00:03:31.390 --> 00:03:31.970
So what will I do?

114
00:03:32.130 --> 00:03:33.390
I will comment out this select one again.

115
00:03:34.690 --> 00:03:35.530
And what will I do this time?

116
00:03:35.750 --> 00:03:38.510
Let's say I will make Shubham Sharma instead

117
00:03:38.510 --> 00:03:38.610
of Amish Sharma.

118
00:03:38.610 --> 00:03:41.430
And after Shubham Sharma, what will I do

119
00:03:41.430 --> 00:03:41.530
here?

120
00:03:41.950 --> 00:03:43.330
Let's say I want to keep it 31st

121
00:03:43.330 --> 00:03:43.710
January.

122
00:03:45.130 --> 00:03:46.230
And now I will run it.

123
00:03:46.830 --> 00:03:48.090
And you see, as soon as I run

124
00:03:48.090 --> 00:03:48.950
it, it was also inserted.

125
00:03:49.270 --> 00:03:50.110
31st January.

126
00:03:50.490 --> 00:03:52.870
I will ctrl forward slash and select start

127
00:03:52.870 --> 00:03:53.390
from clients again.

128
00:03:53.710 --> 00:03:55.310
If I run it, you can see here.

129
00:03:55.850 --> 00:03:57.210
It is also 31st January.

130
00:03:57.770 --> 00:03:57.930
Okay.

131
00:03:58.510 --> 00:04:00.030
So it was 10th January here.

132
00:04:00.330 --> 00:04:01.270
Now it is 31st January.

133
00:04:02.030 --> 00:04:02.810
And I have done all the remaining things

134
00:04:02.810 --> 00:04:03.310
the same.

135
00:04:03.990 --> 00:04:04.530
I have also done the same email id.

136
00:04:05.870 --> 00:04:06.770
But that should be fine.

137
00:04:06.770 --> 00:04:10.570
And that's how you store data inside MySQL.

138
00:04:10.950 --> 00:04:12.230
Now what can you do?

139
00:04:13.190 --> 00:04:15.310
You can also insert multiple rows in one

140
00:04:15.310 --> 00:04:15.410
query.

141
00:04:15.790 --> 00:04:16.410
How will you do that?

142
00:04:16.870 --> 00:04:17.890
You will do that by putting a comma.

143
00:04:18.329 --> 00:04:19.310
So let me show you.

144
00:04:19.890 --> 00:04:22.510
Like I wrote Shubham Sharma here.

145
00:04:22.510 --> 00:04:24.850
And then I wrote Amit at the rate

146
00:04:24.850 --> 00:04:25.610
gmail dot com.

147
00:04:25.610 --> 00:04:26.430
I will put a comma here.

148
00:04:26.570 --> 00:04:27.090
I will hit enter.

149
00:04:27.910 --> 00:04:29.550
And I will insert another row here.

150
00:04:29.810 --> 00:04:30.630
Okay, let me show you how.

151
00:04:31.310 --> 00:04:32.910
Do ctrl c, do ctrl v.

152
00:04:33.410 --> 00:04:34.470
And what will I do here?

153
00:04:34.470 --> 00:04:37.230
I will change the data a little this

154
00:04:37.230 --> 00:04:37.470
time.

155
00:04:37.510 --> 00:04:38.570
I will make it Ragini Sharma.

156
00:04:39.390 --> 00:04:41.510
And I will do ragini at gmail dot

157
00:04:41.510 --> 00:04:41.870
com.

158
00:04:41.950 --> 00:04:43.730
Ragini's phone number starts with 87.

159
00:04:44.650 --> 00:04:45.050
Okay.

160
00:04:45.730 --> 00:04:47.330
And I will make it 2026.

161
00:04:47.810 --> 00:04:48.930
I will also make it 2026.

162
00:04:49.310 --> 00:04:50.190
I will make the date 22.

163
00:04:51.010 --> 00:04:53.830
And I will make it 11.5. And

164
00:04:53.830 --> 00:04:55.130
you can also add more rows like this.

165
00:04:56.150 --> 00:04:57.510
You can keep adding rows.

166
00:04:57.710 --> 00:04:59.750
You can add 10, 50, 100 rows here.

167
00:05:00.430 --> 00:05:02.930
The benefit of inserting multiple rows in one

168
00:05:02.930 --> 00:05:05.030
query is that things remain optimised.

169
00:05:05.690 --> 00:05:09.170
And you have to make multiple connections to

170
00:05:09.170 --> 00:05:09.270
insert one by one.

171
00:05:09.730 --> 00:05:11.710
Here you will do all the work at

172
00:05:11.710 --> 00:05:11.810
once.

173
00:05:11.950 --> 00:05:13.110
Which will be time efficient.

174
00:05:13.850 --> 00:05:14.010
Okay.

175
00:05:14.570 --> 00:05:15.110
So I will run.

176
00:05:15.770 --> 00:05:17.070
And you see as soon as I run.

177
00:05:18.150 --> 00:05:19.050
Basically what happened?

178
00:05:19.190 --> 00:05:20.350
Why didn't we see Ragini here?

179
00:05:20.490 --> 00:05:24.050
We didn't see Ragini because we first showed

180
00:05:24.050 --> 00:05:24.530
the data here.

181
00:05:24.550 --> 00:05:25.130
Then inserted.

182
00:05:25.930 --> 00:05:27.290
Now I will comment out this and show

183
00:05:27.290 --> 00:05:27.770
only the data.

184
00:05:27.890 --> 00:05:28.350
So I will also see Ragini.

185
00:05:28.770 --> 00:05:29.550
Shubham Sharma will be seen twice.

186
00:05:29.990 --> 00:05:30.510
I will show you.

187
00:05:30.990 --> 00:05:31.770
See, I saw it twice.

188
00:05:32.310 --> 00:05:32.510
Why?

189
00:05:32.510 --> 00:05:33.510
Because what are we doing here?

190
00:05:33.610 --> 00:05:34.570
First use ecom was done.

191
00:05:34.670 --> 00:05:36.470
Then he showed select star from clients.

192
00:05:36.770 --> 00:05:38.390
Insert was not done till then.

193
00:05:38.410 --> 00:05:38.670
Do you understand?

194
00:05:39.430 --> 00:05:40.610
By the way, if you are getting confused,

195
00:05:40.810 --> 00:05:41.690
then do not get confused at all.

196
00:05:41.970 --> 00:05:42.450
Run the query one by one.

197
00:05:44.250 --> 00:05:45.330
First run the insert query.

198
00:05:45.790 --> 00:05:47.310
Then run the select query after that.

199
00:05:47.770 --> 00:05:48.830
Now I will run it.

200
00:05:48.970 --> 00:05:49.870
So I am learning all these records.

201
00:05:50.450 --> 00:05:52.050
And I can insert multiple records at once.

202
00:05:52.610 --> 00:05:52.770
Okay.

203
00:05:53.450 --> 00:05:54.350
I hope you understood.

204
00:05:54.810 --> 00:05:55.310
Run one by one.

205
00:05:55.870 --> 00:05:56.490
Don't run together.

206
00:05:56.750 --> 00:05:57.430
Select and insert.

207
00:05:57.550 --> 00:05:58.170
Otherwise you will get confused.

208
00:05:59.110 --> 00:05:59.890
Basically there is nothing to get confused.

209
00:06:00.710 --> 00:06:02.730
Whenever you run SQL code, it runs from

210
00:06:02.730 --> 00:06:03.350
top to bottom.

211
00:06:03.930 --> 00:06:04.590
First run use ecom.

212
00:06:05.170 --> 00:06:06.730
Then whatever is the value of the client

213
00:06:06.730 --> 00:06:06.830
at this time.

214
00:06:06.830 --> 00:06:08.570
Means whatever the client table looks like, you

215
00:06:08.570 --> 00:06:08.990
will see the same.

216
00:06:09.390 --> 00:06:10.410
And after that the data will be inserted.

217
00:06:10.590 --> 00:06:11.930
So you will not see the inserted data.

218
00:06:12.050 --> 00:06:12.970
Because you saw the table first.

219
00:06:13.270 --> 00:06:14.130
Run the select query first.

220
00:06:15.210 --> 00:06:16.250
And then you inserted.

221
00:06:16.670 --> 00:06:18.550
So not to be confused by this.

222
00:06:18.670 --> 00:06:19.850
And to avoid this confusion.

223
00:06:20.770 --> 00:06:21.430
What do you do?

224
00:06:22.010 --> 00:06:22.330
Run one by one.

225
00:06:22.750 --> 00:06:23.350
First run the select query.

226
00:06:24.070 --> 00:06:25.190
Then comment out the select query.

227
00:06:25.870 --> 00:06:26.630
And run the insert query.

228
00:06:27.010 --> 00:06:28.250
And then run the select query and see

229
00:06:28.250 --> 00:06:28.830
what is in your table.

230
00:06:28.830 --> 00:06:29.350
Okay.

231
00:06:30.050 --> 00:06:31.170
I hope this is clear.

232
00:06:31.770 --> 00:06:34.170
And that's how you insert data into your

233
00:06:34.170 --> 00:06:34.450
table.

234
00:06:34.890 --> 00:06:36.450
I hope you are enjoying this course so

235
00:06:36.450 --> 00:06:36.730
far.

236
00:06:37.510 --> 00:06:38.490
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.560 --> 00:00:01.760
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to see

2
00:00:01.760 --> 00:00:04.340
how you can select from the data table.

3
00:00:04.600 --> 00:00:06.180
So, I will open the new query tab

4
00:00:06.180 --> 00:00:08.620
here and now I will switch to my

5
00:00:08.620 --> 00:00:09.460
orders table.

6
00:00:09.680 --> 00:00:11.620
So, first of all, I will run select

7
00:00:11.620 --> 00:00:15.260
star from orders and we will see what

8
00:00:15.260 --> 00:00:16.100
is in our orders table.

9
00:00:17.000 --> 00:00:19.020
Now see here we have Amish Sharma, Neha

10
00:00:19.020 --> 00:00:21.520
Verma, all this data and I had inserted

11
00:00:21.520 --> 00:00:21.620
this for you.

12
00:00:22.020 --> 00:00:23.680
Now see the delivery date here is null

13
00:00:23.680 --> 00:00:26.180
of Ananya Roy and here the delivery date

14
00:00:26.180 --> 00:00:28.020
of Arjun Mehta is null.

15
00:00:28.020 --> 00:00:31.840
So, here these values are null because this

16
00:00:31.840 --> 00:00:32.460
order has been cancelled.

17
00:00:32.720 --> 00:00:33.940
You can see that this order is pending

18
00:00:33.940 --> 00:00:34.880
that is why it has never been delivered.

19
00:00:35.240 --> 00:00:38.300
So, here you can see that the delivery

20
00:00:38.300 --> 00:00:39.000
date is null.

21
00:00:39.440 --> 00:00:41.000
So, what does null mean in SQL?

22
00:00:41.500 --> 00:00:42.620
We call nothing as null.

23
00:00:43.040 --> 00:00:45.140
Means nothing is null.

24
00:00:45.860 --> 00:00:47.620
Now here what we will do is we

25
00:00:47.620 --> 00:00:51.200
will see how we can select the data

26
00:00:51.200 --> 00:00:54.400
and how we can select some columns.

27
00:00:55.160 --> 00:00:56.960
So, I will close this result here.

28
00:00:56.960 --> 00:00:59.520
Now if I want here that I just

29
00:00:59.520 --> 00:01:05.040
want those orders where let's say a particular

30
00:01:05.040 --> 00:01:05.560
amount.

31
00:01:05.760 --> 00:01:06.460
So, first of all I will see all

32
00:01:06.460 --> 00:01:06.780
the orders.

33
00:01:07.680 --> 00:01:10.040
I want that discount percent is let's say

34
00:01:10.040 --> 00:01:10.360
20.

35
00:01:10.520 --> 00:01:12.500
I want that discount percent is equal to

36
00:01:12.500 --> 00:01:12.880
20.

37
00:01:13.240 --> 00:01:16.500
So, I will write here where and I

38
00:01:16.500 --> 00:01:19.740
will write here discount underscore percent and I

39
00:01:19.740 --> 00:01:23.140
will write here equals to let's say 20.

40
00:01:23.140 --> 00:01:25.060
And as soon as I will do this,

41
00:01:25.100 --> 00:01:26.040
you will see I will run this.

42
00:01:26.700 --> 00:01:29.220
So, I will get only those rows where

43
00:01:29.220 --> 00:01:30.540
discount percent is 20.

44
00:01:31.200 --> 00:01:33.800
If I want discount percent is less than

45
00:01:33.800 --> 00:01:35.460
20, then I will get those rows where

46
00:01:35.460 --> 00:01:37.560
discount percent is less than 20.

47
00:01:37.640 --> 00:01:39.260
You can see here 10, here 0, here

48
00:01:39.260 --> 00:01:39.600
15.

49
00:01:39.980 --> 00:01:41.600
So, you can use where clause and do

50
00:01:41.600 --> 00:01:42.120
filtering.

51
00:01:42.720 --> 00:01:44.480
And this is very useful in real world

52
00:01:44.480 --> 00:01:46.440
because what happens is when you work with

53
00:01:46.440 --> 00:01:48.160
real world data, then you will not work

54
00:01:48.160 --> 00:01:48.800
with 12 rows.

55
00:01:49.640 --> 00:01:50.100
You will not even work with 22.

56
00:01:50.100 --> 00:01:51.900
There is a good chance that you will

57
00:01:51.900 --> 00:01:54.160
work with thousands and even lakhs of rows.

58
00:01:55.180 --> 00:01:56.260
And when you will work with lakhs of

59
00:01:56.260 --> 00:01:59.280
rows, then you will have so much data

60
00:01:59.280 --> 00:01:59.960
that you will have to do filtering.

61
00:02:00.940 --> 00:02:02.880
And not basic filtering, you will have to

62
00:02:02.880 --> 00:02:04.080
do advanced level filtering.

63
00:02:05.140 --> 00:02:07.740
Now, let's say in this data, I just

64
00:02:07.740 --> 00:02:09.820
want customer's name and city.

65
00:02:10.500 --> 00:02:12.940
So, I will write instead of star, customer

66
00:02:12.940 --> 00:02:15.740
underscore name and I will write city with

67
00:02:15.740 --> 00:02:15.840
comma.

68
00:02:15.840 --> 00:02:17.580
And you see, as soon as you type,

69
00:02:17.800 --> 00:02:20.660
MySQL Workbench gives you smart recommendation.

70
00:02:21.020 --> 00:02:22.320
And it is saying that this is column

71
00:02:22.320 --> 00:02:22.800
name.

72
00:02:23.240 --> 00:02:23.820
Do you want to take?

73
00:02:24.040 --> 00:02:25.680
I said yes, I want to take city

74
00:02:25.680 --> 00:02:25.980
here.

75
00:02:26.400 --> 00:02:28.080
And when I run this, you see where

76
00:02:28.080 --> 00:02:31.460
all columns were visible, now only two columns

77
00:02:31.460 --> 00:02:31.720
will be visible here.

78
00:02:31.880 --> 00:02:33.300
One customer name and one city.

79
00:02:33.840 --> 00:02:37.060
So, you can take specific columns like this.

80
00:02:37.320 --> 00:02:38.560
You can add more if you want.

81
00:02:39.020 --> 00:02:40.860
See, I have selected this column here.

82
00:02:41.260 --> 00:02:41.740
So, I can see all columns of this

83
00:02:41.740 --> 00:02:43.060
table.

84
00:02:44.380 --> 00:02:46.480
So, let's say I want to see quantity

85
00:02:46.480 --> 00:02:46.920
also.

86
00:02:47.000 --> 00:02:48.240
So, I will write here.

87
00:02:48.240 --> 00:02:49.820
When I will write quantity, see it has

88
00:02:49.820 --> 00:02:50.960
recommended quantity.

89
00:02:51.200 --> 00:02:52.720
Now, when I run this, quantity will also

90
00:02:52.720 --> 00:02:52.880
come.

91
00:02:53.200 --> 00:02:54.400
And if I will write only one column

92
00:02:54.400 --> 00:02:56.320
name, then only that column name will come.

93
00:02:56.700 --> 00:02:58.040
So, you can do all these things very

94
00:02:58.040 --> 00:02:59.220
easily in SQL.

95
00:02:59.860 --> 00:03:03.920
Now, here we will see how you can

96
00:03:03.920 --> 00:03:07.440
filter using conditions.

97
00:03:07.880 --> 00:03:09.680
So, we have already seen greater than.

98
00:03:10.060 --> 00:03:11.280
I have shown you here.

99
00:03:11.300 --> 00:03:13.040
Discount percent is less than greater than.

100
00:03:13.040 --> 00:03:13.880
You can use all these things.

101
00:03:14.440 --> 00:03:18.040
Like we have used less than here, we

102
00:03:18.040 --> 00:03:18.560
can use greater than also.

103
00:03:19.140 --> 00:03:20.860
Now, see here, Ananya Roy Kolkata.

104
00:03:21.180 --> 00:03:22.660
And here quantity 1 has come.

105
00:03:22.900 --> 00:03:24.640
I will change this and start again.

106
00:03:24.920 --> 00:03:26.300
Because it is always good to see all

107
00:03:26.300 --> 00:03:26.760
the columns.

108
00:03:26.960 --> 00:03:27.720
Now, I will see all the columns.

109
00:03:28.880 --> 00:03:30.520
I have ordered study table from Ananya Roy

110
00:03:30.520 --> 00:03:30.620
Kolkata.

111
00:03:30.660 --> 00:03:32.160
There is furniture and they have not ordered.

112
00:03:32.440 --> 00:03:33.300
Their order has gone pending.

113
00:03:35.040 --> 00:03:37.860
Now, let's say I want to see which

114
00:03:37.860 --> 00:03:40.380
are those useless orders whose delivery date is

115
00:03:40.380 --> 00:03:40.480
not there.

116
00:03:40.480 --> 00:03:42.660
Means which are those orders whose delivery date

117
00:03:42.660 --> 00:03:43.960
is not there whose delivery has never happened.

118
00:03:44.360 --> 00:03:46.080
So, what I will do here, I will

119
00:03:46.080 --> 00:03:49.740
write delivery underscore date and here I will

120
00:03:49.740 --> 00:03:50.640
write equals to null.

121
00:03:50.780 --> 00:03:52.020
Now, here you see carefully, understand what I

122
00:03:52.020 --> 00:03:52.700
am saying.

123
00:03:52.820 --> 00:03:54.320
What I am telling here, listen to it

124
00:03:54.320 --> 00:03:54.840
with a little focus.

125
00:03:56.100 --> 00:03:58.740
If I will execute this, then you see,

126
00:03:58.820 --> 00:03:59.200
nothing is found.

127
00:04:00.120 --> 00:04:00.660
What happened?

128
00:04:01.320 --> 00:04:04.760
You will say, man, our delivery date equals

129
00:04:04.760 --> 00:04:06.440
to null columns were present here.

130
00:04:06.840 --> 00:04:08.100
So, why is this happening now?

131
00:04:08.100 --> 00:04:09.780
And I will tell you the reason for

132
00:04:09.780 --> 00:04:09.880
this.

133
00:04:10.420 --> 00:04:12.520
In SQL, we do not use equal to

134
00:04:12.520 --> 00:04:12.660
null.

135
00:04:13.440 --> 00:04:14.620
We use is null.

136
00:04:15.180 --> 00:04:17.399
Means whenever we see null, we write as

137
00:04:17.399 --> 00:04:18.079
is null.

138
00:04:18.880 --> 00:04:20.060
We do not write as equal to null.

139
00:04:20.980 --> 00:04:22.000
So, here I will not write equal to

140
00:04:22.000 --> 00:04:22.760
null but is null.

141
00:04:23.180 --> 00:04:24.280
You have to do this with null.

142
00:04:24.960 --> 00:04:26.180
And what is its reason?

143
00:04:26.880 --> 00:04:30.480
Its reason is that equal to null or

144
00:04:30.480 --> 00:04:32.380
is not equal to null will never return

145
00:04:32.380 --> 00:04:33.780
you rows.

146
00:04:34.740 --> 00:04:37.420
Is null or is not null In SQL,

147
00:04:37.620 --> 00:04:39.900
there are some special conditions which you have

148
00:04:39.900 --> 00:04:41.300
to use like this.

149
00:04:41.440 --> 00:04:42.120
So, I will run this.

150
00:04:42.340 --> 00:04:45.760
You see, here I got two rows.

151
00:04:46.020 --> 00:04:47.060
One is Arjun Mehta and one is Ananya

152
00:04:47.060 --> 00:04:47.280
Roy.

153
00:04:47.860 --> 00:04:48.680
Here delivery date was null.

154
00:04:49.400 --> 00:04:50.840
Here delivery date is null.

155
00:04:51.480 --> 00:04:53.940
And keep in mind, whenever you have to

156
00:04:53.940 --> 00:04:55.800
compare null, you will say is null.

157
00:04:56.200 --> 00:04:57.100
You will not say equal to null.

158
00:04:58.480 --> 00:05:00.340
So, this thing is very important.

159
00:05:00.880 --> 00:05:02.860
And you all should understand it with focus.

160
00:05:04.240 --> 00:05:05.200
So, we have seen all this.

161
00:05:05.200 --> 00:05:07.060
Now, I will show you how to use

162
00:05:07.060 --> 00:05:08.440
AND and OR.

163
00:05:09.220 --> 00:05:10.880
First, let's take an example of AND.

164
00:05:11.120 --> 00:05:12.800
So, I will write here select star from

165
00:05:12.800 --> 00:05:13.240
orders.

166
00:05:13.420 --> 00:05:14.800
I will write where city is equal to

167
00:05:14.800 --> 00:05:15.060
Delhi.

168
00:05:15.540 --> 00:05:18.680
I will write city equal to Delhi.

169
00:05:19.380 --> 00:05:21.400
And after this, I will write AND.

170
00:05:21.540 --> 00:05:23.180
AND means OR in Hindi.

171
00:05:23.860 --> 00:05:29.260
AND order status is equal to equals to

172
00:05:29.260 --> 00:05:29.800
delivered.

173
00:05:30.540 --> 00:05:32.480
We use single quote here.

174
00:05:34.180 --> 00:05:35.620
Let's run this query.

175
00:05:35.780 --> 00:05:36.560
What did I say?

176
00:05:36.640 --> 00:05:39.880
I said city should be Delhi OR Delhi

177
00:05:39.880 --> 00:05:42.940
should be city and order status should be

178
00:05:42.940 --> 00:05:43.260
delivered.

179
00:05:43.600 --> 00:05:45.280
Both should be same.

180
00:05:46.480 --> 00:05:47.620
Both should be same.

181
00:05:48.220 --> 00:05:51.560
City should be Delhi and order status should

182
00:05:51.560 --> 00:05:51.660
be delivered.

183
00:05:51.720 --> 00:05:52.200
Let's run.

184
00:05:53.200 --> 00:05:57.480
You will get all Delhi and order status

185
00:05:57.480 --> 00:05:57.900
should be delivered.

186
00:05:58.720 --> 00:06:00.760
So, this is one way to use AND.

187
00:06:00.760 --> 00:06:03.700
But, if I put OR here OR means

188
00:06:03.700 --> 00:06:05.500
here in Hindi.

189
00:06:05.580 --> 00:06:07.480
Either this or this.

190
00:06:08.560 --> 00:06:11.900
You can say either send me a person

191
00:06:11.900 --> 00:06:15.640
in my room who knows python or send

192
00:06:15.640 --> 00:06:16.800
a person from Delhi.

193
00:06:17.140 --> 00:06:18.140
So, if someone is from Delhi and doesn't

194
00:06:18.140 --> 00:06:20.700
know python you can call that person too.

195
00:06:21.080 --> 00:06:23.580
So, this is how I run it.

196
00:06:25.000 --> 00:06:26.600
City is Mumbai here.

197
00:06:26.740 --> 00:06:27.340
This is also here.

198
00:06:27.340 --> 00:06:29.080
This row is also here.

199
00:06:29.580 --> 00:06:30.520
Basically, this row is here.

200
00:06:31.980 --> 00:06:32.940
City was Mumbai.

201
00:06:34.220 --> 00:06:36.860
But, because order status was delivered, it was

202
00:06:36.860 --> 00:06:37.240
selected.

203
00:06:37.940 --> 00:06:40.380
We are not getting any other where order

204
00:06:40.380 --> 00:06:41.220
status is not delivered.

205
00:06:41.500 --> 00:06:43.640
But, we are getting a row where city

206
00:06:43.640 --> 00:06:45.100
is Delhi and order status is something else.

207
00:06:45.300 --> 00:06:47.400
So, if any of these two is true

208
00:06:47.400 --> 00:06:49.680
then OR will return true.

209
00:06:50.500 --> 00:06:51.660
So, this is how this query works.

210
00:06:54.060 --> 00:06:56.340
I will tell you in coming videos how

211
00:06:56.340 --> 00:06:57.880
to generate complex queries from AI.

212
00:06:58.880 --> 00:06:59.840
You can generate queries from chatGPT.

213
00:07:01.440 --> 00:07:02.960
But, again, we have to understand basics.

214
00:07:04.140 --> 00:07:05.600
It is very important for us to understand

215
00:07:05.600 --> 00:07:05.700
basics.

216
00:07:05.740 --> 00:07:07.420
So, I will not waste your time.

217
00:07:08.180 --> 00:07:09.980
I will not tell you to go to

218
00:07:09.980 --> 00:07:12.740
chatGPT and tell chatGPT to generate a query

219
00:07:13.460 --> 00:07:14.420
which does this.

220
00:07:14.700 --> 00:07:16.040
Yes, you will do it later.

221
00:07:16.500 --> 00:07:18.640
But, for now, no chatGPT.

222
00:07:18.800 --> 00:07:19.800
Because, we have to strengthen our basics.

223
00:07:21.040 --> 00:07:22.460
We have to strengthen our foundation.

224
00:07:22.460 --> 00:07:23.580
We have to strengthen our foundation.

225
00:07:24.260 --> 00:07:25.300
Very good.

226
00:07:25.580 --> 00:07:27.820
Now, if you want to sort data then

227
00:07:27.820 --> 00:07:37.240
select and write customer name and order date

228
00:07:37.240 --> 00:07:42.640
After order date, we will give price per

229
00:07:42.640 --> 00:07:42.880
unit.

230
00:07:43.340 --> 00:07:44.220
I will take one or two columns.

231
00:07:45.340 --> 00:07:49.020
Order underscore date Now, if I write price

232
00:07:49.020 --> 00:07:51.460
Why is it not coming?

233
00:07:51.860 --> 00:07:52.560
Why is it not coming?

234
00:07:52.660 --> 00:07:55.580
It is not coming.

235
00:07:55.920 --> 00:07:57.520
Sometimes, it does not come.

236
00:07:57.680 --> 00:08:00.500
My PC is slow because my C drive

237
00:08:00.500 --> 00:08:00.720
is full.

238
00:08:01.780 --> 00:08:05.500
After this, I will write from orders and

239
00:08:05.500 --> 00:08:08.260
I will write order by Now, first of

240
00:08:08.260 --> 00:08:08.720
all, understand this.

241
00:08:08.720 --> 00:08:09.360
What will happen if I do only this?

242
00:08:10.760 --> 00:08:11.460
What will happen if I do only this?

243
00:08:12.480 --> 00:08:14.140
I will see these three columns.

244
00:08:14.720 --> 00:08:15.860
We have already seen this.

245
00:08:15.860 --> 00:08:20.420
Now, I will write order by Now, whatever

246
00:08:20.420 --> 00:08:24.120
I am writing in capital those are reserved

247
00:08:24.120 --> 00:08:24.920
keywords in MySQL.

248
00:08:25.620 --> 00:08:30.380
order by order by order underscore date order

249
00:08:30.380 --> 00:08:32.620
underscore date Now, look here.

250
00:08:33.360 --> 00:08:35.539
Here, order date is 5 Here, it is

251
00:08:35.539 --> 00:08:38.179
10 Here, it is 12, 15, 18, 20,

252
00:08:38.260 --> 00:08:41.039
22, 25 Yes, it is ordered by order

253
00:08:41.039 --> 00:08:41.320
date.

254
00:08:41.419 --> 00:08:43.500
But, if I run it now So, you

255
00:08:43.500 --> 00:08:44.460
see, first 5 is coming.

256
00:08:44.680 --> 00:08:45.300
It is coming before 5th January.

257
00:08:46.180 --> 00:08:48.740
But, I want it to come before 5th

258
00:08:48.740 --> 00:08:49.040
February.

259
00:08:49.700 --> 00:08:51.740
I want to see the latest order above.

260
00:08:52.180 --> 00:08:53.860
So, I will write DESC.

261
00:08:54.120 --> 00:08:55.980
By default, it is in ascending order.

262
00:08:56.400 --> 00:08:58.720
But, if I write DESC then it will

263
00:08:58.720 --> 00:09:01.120
be sorted in descending order by order date.

264
00:09:01.300 --> 00:09:01.840
So, you see, you will get a new

265
00:09:01.840 --> 00:09:02.600
order above.

266
00:09:02.680 --> 00:09:05.720
You can see Pooja Nair above because she

267
00:09:05.720 --> 00:09:06.840
has placed an order recently.

268
00:09:07.440 --> 00:09:09.800
So, this thing is very important.

269
00:09:10.080 --> 00:09:11.500
The way you can do sorting.

270
00:09:11.500 --> 00:09:12.620
Let me tell you something.

271
00:09:13.020 --> 00:09:15.140
I will give you a handbook along with

272
00:09:15.140 --> 00:09:18.500
that, you will get the code very easily

273
00:09:18.500 --> 00:09:19.520
to copy and paste.

274
00:09:19.780 --> 00:09:21.180
So, you don't have to take any tension

275
00:09:21.180 --> 00:09:23.060
to note down, to write.

276
00:09:23.560 --> 00:09:26.020
Yes, type it, practice it.

277
00:09:26.020 --> 00:09:27.380
Practice will make you perfect.

278
00:09:27.680 --> 00:09:30.360
But, don't think that I will remember it

279
00:09:30.360 --> 00:09:33.020
or note down the queries I am writing

280
00:09:33.020 --> 00:09:34.420
thinking that you will never get it.

281
00:09:34.980 --> 00:09:36.060
I will give you everything.

282
00:09:36.780 --> 00:09:38.100
I have arranged everything for you.

283
00:09:38.560 --> 00:09:40.260
I hope you understood the topic of selecting

284
00:09:40.260 --> 00:09:40.840
data.

285
00:09:44.900 --> 00:09:46.520
Thank you so much guys for watching this

286
00:09:46.520 --> 00:09:48.240
video and I will see you in the

287
00:09:48.240 --> 00:09:48.680
next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.260 --> 00:00:03.680
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will see how you

2
00:00:03.680 --> 00:00:08.320
can update and delete data in MySQL.

3
00:00:08.600 --> 00:00:10.740
So, what I will do here is, I

4
00:00:10.740 --> 00:00:11.160
will close this.

5
00:00:11.560 --> 00:00:12.660
In fact, I have not saved any file,

6
00:00:13.300 --> 00:00:14.880
so I will start from a clean slate.

7
00:00:16.660 --> 00:00:18.220
And what I will do here is, I

8
00:00:18.220 --> 00:00:22.280
will write select star, star from orders.

9
00:00:23.140 --> 00:00:24.380
And I should see all the orders.

10
00:00:25.160 --> 00:00:26.400
These are all our orders.

11
00:00:27.060 --> 00:00:28.760
And here you can see all the customers,

12
00:00:28.800 --> 00:00:30.680
city, product, category, quantity.

13
00:00:30.860 --> 00:00:31.439
I can see all this.

14
00:00:32.420 --> 00:00:34.460
Now what I will do is, I will

15
00:00:34.460 --> 00:00:36.180
show you a single row update here.

16
00:00:36.840 --> 00:00:42.160
Let's say that I want this brother, Ananya

17
00:00:42.160 --> 00:00:42.380
Roy.

18
00:00:42.920 --> 00:00:43.900
She is a sister, not a brother.

19
00:00:44.880 --> 00:00:45.800
Let's deliver their order.

20
00:00:46.540 --> 00:00:48.540
Suppose they had called us.

21
00:00:48.680 --> 00:00:50.620
I found out that Ananya Roy had called.

22
00:00:50.620 --> 00:00:52.080
And said that I want a study table,

23
00:00:52.420 --> 00:00:53.620
I have exams, I want to study.

24
00:00:53.900 --> 00:00:55.060
Please deliver my order.

25
00:00:55.820 --> 00:00:56.760
And one of our employees went to their

26
00:00:56.760 --> 00:00:57.380
house and gave it.

27
00:00:58.140 --> 00:00:59.400
And he did not tell us this.

28
00:00:59.800 --> 00:01:01.040
And when he told us, we will have

29
00:01:01.040 --> 00:01:01.440
to update.

30
00:01:02.140 --> 00:01:03.400
Its status will have to be delivered.

31
00:01:03.860 --> 00:01:04.800
And he did not even tell us which

32
00:01:04.800 --> 00:01:05.480
date he delivered.

33
00:01:05.760 --> 00:01:06.580
So we left it null.

34
00:01:06.960 --> 00:01:08.040
We want to deliver here.

35
00:01:08.720 --> 00:01:10.360
So what we will do here, we will

36
00:01:10.360 --> 00:01:11.220
write update here.

37
00:01:12.040 --> 00:01:12.480
Update.

38
00:01:13.060 --> 00:01:13.520
We will write update.

39
00:01:14.120 --> 00:01:15.800
Then we will write which table, orders.

40
00:01:16.280 --> 00:01:17.740
And after this we will write set.

41
00:01:17.740 --> 00:01:18.540
Now I am writing on a new line.

42
00:01:18.900 --> 00:01:20.540
You can divide a query like this.

43
00:01:21.240 --> 00:01:23.980
In fact, it is a very standard practice.

44
00:01:24.620 --> 00:01:26.560
So here we are saying, set order status

45
00:01:26.560 --> 00:01:28.460
equals to delivered.

46
00:01:29.640 --> 00:01:30.020
Okay.

47
00:01:30.640 --> 00:01:32.900
And we will write a where clause here.

48
00:01:33.340 --> 00:01:36.360
Means where order underscore id is equal to

49
00:01:36.360 --> 00:01:36.660
10.

50
00:01:37.160 --> 00:01:39.100
Means we are basically saying here.

51
00:01:39.180 --> 00:01:40.480
We are saying here that brother.

52
00:01:40.700 --> 00:01:42.560
Where order id is equal to 10.

53
00:01:43.140 --> 00:01:44.200
What do you do there?

54
00:01:44.640 --> 00:01:45.320
Deliver the order status.

55
00:01:45.320 --> 00:01:49.120
But here the order status is pending.

56
00:01:49.320 --> 00:01:49.440
Yes.

57
00:01:49.560 --> 00:01:50.480
So we are updating it.

58
00:01:50.720 --> 00:01:52.080
Stop the 10th one.

59
00:01:52.360 --> 00:01:53.740
Means where order id is equal to 10.

60
00:01:53.920 --> 00:01:55.060
There we are saying, deliver it.

61
00:01:55.120 --> 00:01:55.620
Let's run it.

62
00:01:56.260 --> 00:01:57.540
And here you see a green tick.

63
00:01:57.760 --> 00:01:58.800
And here it is saying that brother.

64
00:01:59.320 --> 00:02:00.900
Order status equals to delivered.

65
00:02:01.500 --> 00:02:02.560
And now what we will do.

66
00:02:02.660 --> 00:02:03.580
So we will do comment out.

67
00:02:04.280 --> 00:02:07.840
And here we will run our select star

68
00:02:07.840 --> 00:02:09.320
from orders.

69
00:02:09.539 --> 00:02:11.340
And we will see whether Ananya Roy's order

70
00:02:11.340 --> 00:02:11.960
has been delivered or not.

71
00:02:13.180 --> 00:02:13.560
And yes.

72
00:02:13.560 --> 00:02:13.780
Yes.

73
00:02:13.780 --> 00:02:14.440
Her order has been delivered.

74
00:02:15.220 --> 00:02:16.120
That's very nice.

75
00:02:16.680 --> 00:02:17.040
Amazing.

76
00:02:17.360 --> 00:02:17.980
I like it.

77
00:02:18.560 --> 00:02:20.280
Ananya Roy has got her study table.

78
00:02:20.340 --> 00:02:21.580
Now she will be able to read happily.

79
00:02:22.300 --> 00:02:25.380
Now assume that we get a call from

80
00:02:25.380 --> 00:02:26.980
Neha Verma.

81
00:02:27.920 --> 00:02:31.480
Neha Verma says that Ananya Roy's table has

82
00:02:31.480 --> 00:02:31.860
been delivered.

83
00:02:32.700 --> 00:02:33.880
Increase my discount a little.

84
00:02:34.780 --> 00:02:35.820
My discount has been given zero.

85
00:02:36.140 --> 00:02:36.680
This is wrong.

86
00:02:37.800 --> 00:02:39.320
So our company will say.

87
00:02:39.420 --> 00:02:40.340
Okay Neha ji.

88
00:02:40.460 --> 00:02:41.020
Why do you worry?

89
00:02:41.020 --> 00:02:45.420
We will update you.

90
00:02:45.580 --> 00:02:46.720
What will we update you?

91
00:02:46.900 --> 00:02:47.760
Discount percent.

92
00:02:48.100 --> 00:02:49.080
And what we will do here.

93
00:02:49.220 --> 00:02:49.580
We will say.

94
00:02:51.020 --> 00:02:53.900
Discount underscore percent equals to ten.

95
00:02:54.460 --> 00:02:57.600
But I have already told you that you

96
00:02:57.600 --> 00:02:58.320
update like this.

97
00:02:58.660 --> 00:02:59.000
Yes.

98
00:02:59.140 --> 00:02:59.800
I have told you.

99
00:03:00.480 --> 00:03:01.120
And here we will say.

100
00:03:01.260 --> 00:03:02.780
Where customer name equals to.

101
00:03:03.800 --> 00:03:04.880
Here we write first.

102
00:03:05.120 --> 00:03:10.620
Where customer name equals to Neha Verma.

103
00:03:10.800 --> 00:03:10.940
Okay.

104
00:03:11.000 --> 00:03:12.360
And here.

105
00:03:13.000 --> 00:03:13.600
We will close it with a single quote.

106
00:03:14.160 --> 00:03:14.600
We will put a semicolon.

107
00:03:15.500 --> 00:03:17.580
I want to increase their discount percent to

108
00:03:17.580 --> 00:03:17.860
ten.

109
00:03:18.160 --> 00:03:19.360
And increase their rating to four.

110
00:03:19.960 --> 00:03:21.400
Increase the rating to four.

111
00:03:21.480 --> 00:03:21.900
They said.

112
00:03:22.040 --> 00:03:24.380
I like your shop very much.

113
00:03:25.340 --> 00:03:26.660
I would like to give it four ratings.

114
00:03:27.980 --> 00:03:29.560
But please give me a discount of ten.

115
00:03:30.000 --> 00:03:30.760
We said.

116
00:03:30.860 --> 00:03:31.700
Okay Neha ji.

117
00:03:31.880 --> 00:03:32.560
You are saying so lovingly.

118
00:03:32.840 --> 00:03:33.380
So why not?

119
00:03:33.820 --> 00:03:36.420
We gave Neha Verma a discount of ten.

120
00:03:36.780 --> 00:03:39.040
And they gave us a rating of four.

121
00:03:39.040 --> 00:03:40.060
So we are locking this thing in our

122
00:03:40.060 --> 00:03:40.420
database.

123
00:03:42.160 --> 00:03:43.660
So how will we lock?

124
00:03:43.940 --> 00:03:44.420
We will update.

125
00:03:44.680 --> 00:03:46.040
And then after that we will select start

126
00:03:46.040 --> 00:03:46.460
from orders.

127
00:03:46.740 --> 00:03:47.480
Or you can do it later.

128
00:03:47.940 --> 00:03:49.140
I have done control X now.

129
00:03:49.720 --> 00:03:50.140
It means that it has been copied in

130
00:03:50.140 --> 00:03:50.740
my clipboard.

131
00:03:51.580 --> 00:03:52.500
I will run it now.

132
00:03:53.600 --> 00:03:54.160
What happened?

133
00:03:54.420 --> 00:03:54.840
He is saying.

134
00:03:55.540 --> 00:03:58.040
Update order set discount percent equals to ten.

135
00:03:58.600 --> 00:04:00.860
You are using safe update mode.

136
00:04:01.140 --> 00:04:03.780
And you try to update a table without

137
00:04:03.780 --> 00:04:04.880
where clause.

138
00:04:05.380 --> 00:04:06.420
That uses a key column.

139
00:04:06.680 --> 00:04:07.400
What is this now?

140
00:04:07.540 --> 00:04:08.200
What is this now?

141
00:04:08.260 --> 00:04:09.020
Now I will tell you.

142
00:04:09.540 --> 00:04:12.740
This error is basically telling us that there

143
00:04:12.740 --> 00:04:14.460
is no primary key in the where clause.

144
00:04:14.840 --> 00:04:15.279
It means.

145
00:04:15.740 --> 00:04:18.339
It is possible that there are 50 customers

146
00:04:18.339 --> 00:04:18.439
named Neha Verma.

147
00:04:18.720 --> 00:04:19.300
It is possible.

148
00:04:19.480 --> 00:04:20.040
If you are operating on a very large

149
00:04:20.040 --> 00:04:20.339
scale.

150
00:04:21.019 --> 00:04:21.480
This will happen.

151
00:04:21.820 --> 00:04:22.940
In fact, if you search for Neha Verma

152
00:04:22.940 --> 00:04:23.680
on Google.

153
00:04:23.840 --> 00:04:25.060
Then you don't know who you will get.

154
00:04:25.220 --> 00:04:25.420
Okay.

155
00:04:26.120 --> 00:04:26.620
Don't search.

156
00:04:26.940 --> 00:04:27.620
I am telling you.

157
00:04:27.680 --> 00:04:28.240
Trust me.

158
00:04:28.540 --> 00:04:30.380
If you search, you will get a lot

159
00:04:30.380 --> 00:04:31.560
of people named Neha Verma.

160
00:04:31.700 --> 00:04:31.920
Okay.

161
00:04:32.440 --> 00:04:35.560
So it shouldn't be that Neha Verma gets

162
00:04:35.560 --> 00:04:37.000
updated to another Neha Verma.

163
00:04:37.800 --> 00:04:38.400
Do you understand?

164
00:04:38.400 --> 00:04:40.480
You are trying to update someone else's Neha

165
00:04:40.480 --> 00:04:41.000
Verma.

166
00:04:43.520 --> 00:04:44.120
For example.

167
00:04:44.620 --> 00:04:45.540
On our Amazon.

168
00:04:45.960 --> 00:04:47.700
It is possible that there are 500-600

169
00:04:47.700 --> 00:04:48.300
Neha Verma.

170
00:04:48.500 --> 00:04:49.920
Which is a very realistic number.

171
00:04:50.760 --> 00:04:51.040
So.

172
00:04:51.320 --> 00:04:52.340
Because it is a very common name.

173
00:04:52.920 --> 00:04:53.160
So.

174
00:04:53.600 --> 00:04:55.920
What can happen here is that your data

175
00:04:55.920 --> 00:04:56.200
can change accidentally.

176
00:04:56.500 --> 00:04:57.820
That's why SQL stopped you earlier.

177
00:04:58.640 --> 00:04:59.260
SQL said.

178
00:04:59.420 --> 00:05:00.400
What do you do?

179
00:05:00.800 --> 00:05:01.760
Disable the safe update.

180
00:05:02.520 --> 00:05:04.280
So the safe mode is on.

181
00:05:05.180 --> 00:05:05.720
In SQL.

182
00:05:05.720 --> 00:05:08.140
You will have to disable it.

183
00:05:08.620 --> 00:05:09.560
Which I don't recommend.

184
00:05:10.280 --> 00:05:10.500
And.

185
00:05:10.900 --> 00:05:12.280
You will disable it once.

186
00:05:13.080 --> 00:05:13.940
After that you will be able to run

187
00:05:13.940 --> 00:05:14.280
this query.

188
00:05:15.040 --> 00:05:15.160
Okay.

189
00:05:15.420 --> 00:05:16.360
So you can disable the safe update.

190
00:05:17.300 --> 00:05:18.540
This is an option.

191
00:05:18.880 --> 00:05:19.980
Which I do not recommend.

192
00:05:20.720 --> 00:05:22.200
How will you disable the safe update?

193
00:05:23.040 --> 00:05:24.340
You write here.

194
00:05:24.540 --> 00:05:25.760
Set SQL.

195
00:05:26.540 --> 00:05:27.180
Underscore.

196
00:05:27.540 --> 00:05:27.960
Safe.

197
00:05:29.420 --> 00:05:30.060
Underscore.

198
00:05:30.320 --> 00:05:30.960
Updates.

199
00:05:31.800 --> 00:05:32.900
Equals to zero.

200
00:05:33.220 --> 00:05:33.980
And what will this line do?

201
00:05:33.980 --> 00:05:35.020
This line will disable the safe update.

202
00:05:36.900 --> 00:05:38.180
I don't recommend this at all.

203
00:05:38.780 --> 00:05:39.280
But.

204
00:05:39.620 --> 00:05:40.440
Let's do it once.

205
00:05:41.140 --> 00:05:41.280
Okay.

206
00:05:41.660 --> 00:05:44.400
And after that I select star from orders.

207
00:05:44.580 --> 00:05:45.260
I do it all at once.

208
00:05:45.720 --> 00:05:47.640
So what will our SQL script do now?

209
00:05:48.100 --> 00:05:48.880
First of all, it will disable the safe

210
00:05:48.880 --> 00:05:49.240
updates.

211
00:05:50.340 --> 00:05:50.780
Okay.

212
00:05:51.160 --> 00:05:52.300
And after that it will run this query.

213
00:05:52.700 --> 00:05:54.660
That is, it will update the rating and

214
00:05:54.660 --> 00:05:55.840
discount percentage of Neha Verma.

215
00:05:56.440 --> 00:05:57.440
And after that it will show us all

216
00:05:57.440 --> 00:05:57.720
the orders.

217
00:05:58.320 --> 00:05:58.920
So let's go.

218
00:05:59.720 --> 00:06:00.220
And you see.

219
00:06:00.360 --> 00:06:01.540
We have been updated this time.

220
00:06:02.140 --> 00:06:03.720
And here you can see.

221
00:06:04.700 --> 00:06:06.160
The one who is Neha Verma.

222
00:06:07.240 --> 00:06:08.480
His order was done.

223
00:06:08.680 --> 00:06:09.160
What did we do?

224
00:06:09.340 --> 00:06:09.960
By the way, Neha Verma was given a

225
00:06:09.960 --> 00:06:10.640
discount of 10.

226
00:06:11.120 --> 00:06:12.000
Neha Verma got that too.

227
00:06:12.560 --> 00:06:13.140
We got a rating of 4.

228
00:06:13.820 --> 00:06:14.020
Okay.

229
00:06:14.240 --> 00:06:15.720
So here we can update multiple columns.

230
00:06:16.540 --> 00:06:17.440
Basically this is take away.

231
00:06:18.060 --> 00:06:19.320
You take take away.

232
00:06:19.600 --> 00:06:19.840
Okay.

233
00:06:19.920 --> 00:06:20.280
Understand this query.

234
00:06:21.020 --> 00:06:22.520
The discount percentage is 10.

235
00:06:23.000 --> 00:06:24.060
The rating is 4.

236
00:06:24.280 --> 00:06:24.500
Okay.

237
00:06:24.940 --> 00:06:27.180
So we made the discount percentage of Neha

238
00:06:27.180 --> 00:06:27.600
Verma 10.

239
00:06:27.680 --> 00:06:28.920
And made the rating 4.

240
00:06:28.920 --> 00:06:34.240
If there are 50 Neha Verma's in our

241
00:06:34.240 --> 00:06:34.340
database.

242
00:06:34.340 --> 00:06:36.740
If there are 50 Neha Verma's.

243
00:06:37.220 --> 00:06:40.400
Will all the Neha Verma's be updated?

244
00:06:40.740 --> 00:06:41.020
Yes.

245
00:06:41.320 --> 00:06:41.840
Absolutely right.

246
00:06:42.420 --> 00:06:42.860
Will be done.

247
00:06:43.000 --> 00:06:44.660
All Neha Verma's will be updated.

248
00:06:45.620 --> 00:06:46.200
That's true.

249
00:06:46.900 --> 00:06:47.060
Okay.

250
00:06:47.640 --> 00:06:50.180
I hope you understood how update works.

251
00:06:50.720 --> 00:06:52.380
This is our very basic update.

252
00:06:52.760 --> 00:06:56.640
You can also update multiple columns here.

253
00:06:56.640 --> 00:06:58.320
You can also update by putting multiple conditions.

254
00:06:59.580 --> 00:07:00.780
Like if you write here.

255
00:07:00.780 --> 00:07:03.180
Where customer name is equal to Neha Verma.

256
00:07:03.840 --> 00:07:04.920
And you can do something by writing AND

257
00:07:04.920 --> 00:07:05.780
here.

258
00:07:05.860 --> 00:07:07.100
You can say AND.

259
00:07:07.560 --> 00:07:09.440
And let's say you say AND.

260
00:07:10.240 --> 00:07:11.980
That order status is equal to delivered.

261
00:07:12.220 --> 00:07:12.340
Okay.

262
00:07:12.900 --> 00:07:14.180
So what will happen here?

263
00:07:14.920 --> 00:07:16.940
If the order status is delivered.

264
00:07:17.520 --> 00:07:20.040
Order status equals to delivered.

265
00:07:20.400 --> 00:07:21.040
Then only it will update.

266
00:07:21.220 --> 00:07:22.540
Means when these two conditions are true.

267
00:07:22.760 --> 00:07:24.260
Then only this update query will run.

268
00:07:24.360 --> 00:07:25.200
Otherwise it will not update.

269
00:07:25.420 --> 00:07:26.080
So I will run it.

270
00:07:26.080 --> 00:07:26.940
So you see here.

271
00:07:27.540 --> 00:07:29.180
Neha Verma update was already done.

272
00:07:29.840 --> 00:07:31.940
But if the order status is not delivered.

273
00:07:32.100 --> 00:07:33.240
Then Neha Verma does not update.

274
00:07:33.420 --> 00:07:34.680
Means this row does not update.

275
00:07:34.840 --> 00:07:34.940
Okay.

276
00:07:35.480 --> 00:07:36.340
I hope you understood.

277
00:07:37.060 --> 00:07:38.020
I hope you got the point.

278
00:07:38.680 --> 00:07:38.940
Good.

279
00:07:39.380 --> 00:07:41.580
Now as we put all the conditions in

280
00:07:41.580 --> 00:07:41.680
select.

281
00:07:42.300 --> 00:07:44.280
You can use all the conditions here in

282
00:07:44.280 --> 00:07:44.660
update.

283
00:07:45.540 --> 00:07:48.460
Greater than, less than or is null.

284
00:07:48.600 --> 00:07:49.920
You can use all that here.

285
00:07:50.060 --> 00:07:51.400
That thing does exactly the same thing.

286
00:07:52.240 --> 00:07:52.620
Okay.

287
00:07:52.620 --> 00:07:56.600
So you can use conditions here.

288
00:07:56.980 --> 00:07:58.680
Now what should you do here?

289
00:07:58.880 --> 00:08:00.600
I give you a tip.

290
00:08:01.080 --> 00:08:01.380
Tip.

291
00:08:01.460 --> 00:08:02.000
What is the tip?

292
00:08:02.320 --> 00:08:05.540
The tip is that whenever you are updating.

293
00:08:06.200 --> 00:08:09.040
Make sure that you run select first.

294
00:08:09.320 --> 00:08:10.780
See how your order table looks.

295
00:08:11.540 --> 00:08:12.900
You run your select with this where.

296
00:08:14.880 --> 00:08:16.140
Then run the update query.

297
00:08:16.460 --> 00:08:17.980
Because at least you will know what you

298
00:08:17.980 --> 00:08:18.340
are going to do.

299
00:08:18.500 --> 00:08:18.840
See, if you are making changes in the

300
00:08:18.840 --> 00:08:19.700
production database.

301
00:08:19.700 --> 00:08:20.460
Then you may have a problem.

302
00:08:22.740 --> 00:08:24.440
You have to run your queries very carefully.

303
00:08:24.780 --> 00:08:25.440
And by running the wrong query.

304
00:08:26.420 --> 00:08:27.880
A lot can go wrong.

305
00:08:28.220 --> 00:08:30.640
So whatever update query you are running first.

306
00:08:30.860 --> 00:08:32.500
Make it select and run it.

307
00:08:32.520 --> 00:08:33.860
Means select start from orders.

308
00:08:34.280 --> 00:08:35.919
Where customer name is equal to Neha Verma.

309
00:08:36.039 --> 00:08:37.260
And order status is equal to delivered.

310
00:08:37.380 --> 00:08:37.760
Run this.

311
00:08:38.700 --> 00:08:39.500
And after that.

312
00:08:41.360 --> 00:08:42.640
The view you will get.

313
00:08:42.780 --> 00:08:44.780
Means the output you will get of your

314
00:08:44.780 --> 00:08:45.100
query.

315
00:08:45.480 --> 00:08:46.380
See that.

316
00:08:46.580 --> 00:08:46.760
Okay.

317
00:08:47.320 --> 00:08:48.500
Customer name Neha Verma.

318
00:08:48.500 --> 00:08:49.540
And order status delivered.

319
00:08:49.860 --> 00:08:50.380
I am getting these rows.

320
00:08:50.980 --> 00:08:52.940
And I am going to update these rows.

321
00:08:53.420 --> 00:08:55.300
After that you run.

322
00:08:55.440 --> 00:08:55.640
Okay.

323
00:08:55.820 --> 00:08:57.540
I hope you got the point.

324
00:08:58.740 --> 00:08:58.980
Good.

325
00:08:59.900 --> 00:09:00.420
Very good.

326
00:09:00.680 --> 00:09:02.880
Now how will you delete?

327
00:09:03.920 --> 00:09:05.200
Let's understand this too.

328
00:09:05.460 --> 00:09:05.720
Okay.

329
00:09:06.100 --> 00:09:07.180
How will you delete rows?

330
00:09:07.680 --> 00:09:09.900
So if you want to delete any row.

331
00:09:10.520 --> 00:09:12.520
So what will you have to do for

332
00:09:12.520 --> 00:09:12.620
that?

333
00:09:12.680 --> 00:09:13.140
You will have to use delete.

334
00:09:14.220 --> 00:09:16.260
So as I am updating here.

335
00:09:16.260 --> 00:09:18.960
I can also delete rows in the same

336
00:09:18.960 --> 00:09:19.060
way.

337
00:09:19.140 --> 00:09:19.900
So I do one thing.

338
00:09:20.260 --> 00:09:20.980
I save it by pressing ctrl s.

339
00:09:21.940 --> 00:09:23.940
I name it update.

340
00:09:24.460 --> 00:09:24.940
Okay.

341
00:09:24.960 --> 00:09:27.140
Update.sql. You will get this sql file.

342
00:09:27.940 --> 00:09:28.540
By the way, I will give all this

343
00:09:28.540 --> 00:09:29.500
code to you already.

344
00:09:29.900 --> 00:09:30.440
But okay.

345
00:09:30.640 --> 00:09:31.280
You will get this too.

346
00:09:32.220 --> 00:09:32.900
Now what I will do here.

347
00:09:33.000 --> 00:09:34.080
I will close this script.

348
00:09:34.260 --> 00:09:35.520
And I will go to the file here.

349
00:09:36.640 --> 00:09:37.500
I will put a new query tab.

350
00:09:38.380 --> 00:09:40.380
The same thing I already recommend to you.

351
00:09:40.820 --> 00:09:42.920
First run select start from orders.

352
00:09:43.260 --> 00:09:44.660
Or whatever you are working on the table.

353
00:09:44.660 --> 00:09:48.140
See what kind of data you are seeing.

354
00:09:48.780 --> 00:09:49.840
Now suppose I want.

355
00:09:50.400 --> 00:09:51.540
I don't want these null ones.

356
00:09:52.180 --> 00:09:53.060
Where the delivery date is null.

357
00:09:53.200 --> 00:09:53.560
I want to delete.

358
00:09:54.280 --> 00:09:55.380
So what will I do here?

359
00:09:55.620 --> 00:09:56.600
I will run here.

360
00:09:56.940 --> 00:09:58.200
I will say delete.

361
00:09:59.860 --> 00:10:00.820
From orders.

362
00:10:01.080 --> 00:10:01.600
So I will write here.

363
00:10:01.680 --> 00:10:04.380
Delete from orders.

364
00:10:06.220 --> 00:10:06.700
Orders.

365
00:10:07.840 --> 00:10:08.320
Where.

366
00:10:10.620 --> 00:10:11.440
Let's say.

367
00:10:12.040 --> 00:10:14.200
Order id is equal to 5.

368
00:10:14.200 --> 00:10:15.140
Then I will make another query.

369
00:10:15.500 --> 00:10:17.560
Where order id is equal to.

370
00:10:17.720 --> 00:10:18.160
10.

371
00:10:18.860 --> 00:10:20.040
Then I will make another query.

372
00:10:20.540 --> 00:10:20.940
There are only two.

373
00:10:21.760 --> 00:10:23.580
So I can run these two individually.

374
00:10:23.940 --> 00:10:24.480
This will work.

375
00:10:25.240 --> 00:10:25.580
But.

376
00:10:25.940 --> 00:10:26.560
Let's say.

377
00:10:27.140 --> 00:10:28.280
I want this.

378
00:10:28.280 --> 00:10:29.560
That the order id.

379
00:10:30.420 --> 00:10:31.080
Is ours.

380
00:10:31.560 --> 00:10:33.720
I don't want to delete from it.

381
00:10:33.960 --> 00:10:34.080
I mean.

382
00:10:34.280 --> 00:10:35.800
Like I do it and show you here.

383
00:10:36.220 --> 00:10:38.600
Order underscore id is equal to 2.

384
00:10:38.700 --> 00:10:39.040
If I do.

385
00:10:39.100 --> 00:10:40.020
Then order id will be deleted.

386
00:10:40.240 --> 00:10:40.960
So if I run this.

387
00:10:41.640 --> 00:10:42.840
And I don't even do ctrl x.

388
00:10:42.840 --> 00:10:43.940
I just run this.

389
00:10:44.220 --> 00:10:45.020
See it is deleted.

390
00:10:45.360 --> 00:10:47.260
And if I run select start from orders.

391
00:10:47.600 --> 00:10:48.420
I will comment this.

392
00:10:48.560 --> 00:10:49.220
By pressing ctrl slash.

393
00:10:49.900 --> 00:10:50.580
So you see.

394
00:10:50.700 --> 00:10:51.420
Id is equal to 2.

395
00:10:51.540 --> 00:10:51.960
I deleted it.

396
00:10:52.120 --> 00:10:52.520
From this query.

397
00:10:52.980 --> 00:10:53.140
Okay.

398
00:10:53.640 --> 00:10:55.260
So this is one type of delete query.

399
00:10:55.520 --> 00:10:56.340
In which we can delete from order id.

400
00:10:57.340 --> 00:10:58.580
But what I want to do here.

401
00:10:58.720 --> 00:10:58.980
I am saying.

402
00:10:59.040 --> 00:11:00.040
Delivery date is null.

403
00:11:00.640 --> 00:11:01.580
Delete it there.

404
00:11:01.880 --> 00:11:03.120
So I will write here.

405
00:11:03.160 --> 00:11:04.500
Where delivery date.

406
00:11:05.020 --> 00:11:05.440
Is.

407
00:11:06.280 --> 00:11:06.540
Null.

408
00:11:06.780 --> 00:11:07.240
So what will happen?

409
00:11:08.320 --> 00:11:08.880
Five people.

410
00:11:08.900 --> 00:11:09.580
Arjun Mehta will fly.

411
00:11:09.760 --> 00:11:09.880
No.

412
00:11:09.880 --> 00:11:10.580
Arjun Mehta will not fly.

413
00:11:10.580 --> 00:11:10.820
Sorry.

414
00:11:11.420 --> 00:11:12.100
Arjun Mehta will fly.

415
00:11:12.960 --> 00:11:14.320
And Ananya Roy will also fly.

416
00:11:14.500 --> 00:11:14.920
Both will fly.

417
00:11:15.140 --> 00:11:15.260
Okay.

418
00:11:15.340 --> 00:11:15.780
Means will be deleted.

419
00:11:16.180 --> 00:11:16.340
Okay.

420
00:11:16.760 --> 00:11:18.700
So Arjun Mehta and Ananya Roy.

421
00:11:19.120 --> 00:11:19.640
Will be deleted.

422
00:11:20.480 --> 00:11:21.980
So I do ctrl x now.

423
00:11:22.500 --> 00:11:23.640
I run this delete query.

424
00:11:23.760 --> 00:11:24.400
And you see here.

425
00:11:24.500 --> 00:11:25.300
It is written two rows affected.

426
00:11:25.820 --> 00:11:27.760
The result below is very important.

427
00:11:28.300 --> 00:11:29.260
You know.

428
00:11:29.400 --> 00:11:31.440
How many rows your update query has affected.

429
00:11:31.860 --> 00:11:34.180
How many rows your delete query has affected.

430
00:11:34.500 --> 00:11:34.940
So this thing.

431
00:11:35.060 --> 00:11:36.240
Is very important information.

432
00:11:36.580 --> 00:11:37.500
You get to see below.

433
00:11:38.180 --> 00:11:39.460
And this green tick.

434
00:11:39.920 --> 00:11:40.560
And this cut tick.

435
00:11:40.560 --> 00:11:40.740
This also.

436
00:11:41.220 --> 00:11:43.340
Gives you a lot of information.

437
00:11:43.720 --> 00:11:44.720
Basically tells you.

438
00:11:44.820 --> 00:11:46.280
Whether your query is running properly or not.

439
00:11:46.600 --> 00:11:47.340
So here you see.

440
00:11:47.780 --> 00:11:48.820
Delete from orders.

441
00:11:48.920 --> 00:11:50.220
Where delivery date is null.

442
00:11:50.640 --> 00:11:51.120
I ran it.

443
00:11:51.200 --> 00:11:51.900
Two rows were affected.

444
00:11:52.500 --> 00:11:54.220
Now I will comment it out.

445
00:11:54.320 --> 00:11:54.700
And only this.

446
00:11:55.120 --> 00:11:56.360
Select start from orders.

447
00:11:56.420 --> 00:11:56.700
I will run it.

448
00:11:56.740 --> 00:11:57.920
And see if it is true or not.

449
00:11:58.580 --> 00:11:58.820
Yes.

450
00:11:58.880 --> 00:11:59.340
This is absolutely true.

451
00:11:59.480 --> 00:12:00.420
Now no delivery date is null.

452
00:12:01.220 --> 00:12:02.160
This means this happened.

453
00:12:02.820 --> 00:12:04.560
That I was able to successfully.

454
00:12:04.860 --> 00:12:05.660
Filter out.

455
00:12:06.160 --> 00:12:06.960
I will not even say filter out.

456
00:12:07.200 --> 00:12:07.520
I will say.

457
00:12:08.160 --> 00:12:08.600
Remove.

458
00:12:09.020 --> 00:12:09.560
The rows.

459
00:12:09.820 --> 00:12:10.540
Where delivery date is null.

460
00:12:11.920 --> 00:12:13.440
Where delivery date was null.

461
00:12:13.740 --> 00:12:13.840
Okay.

462
00:12:14.400 --> 00:12:14.860
Simple thing.

463
00:12:15.440 --> 00:12:16.280
I hope you understood.

464
00:12:16.440 --> 00:12:17.360
I hope you are enjoying.

465
00:12:17.500 --> 00:12:17.820
Understanding.

466
00:12:18.560 --> 00:12:19.020
Update.

467
00:12:19.260 --> 00:12:19.560
And delete.

468
00:12:19.740 --> 00:12:20.400
Are very similar.

469
00:12:20.740 --> 00:12:21.740
Run delete very carefully.

470
00:12:22.320 --> 00:12:23.600
Run delete very carefully.

471
00:12:23.900 --> 00:12:24.420
Because.

472
00:12:24.660 --> 00:12:25.720
If you run delete without a where clause.

473
00:12:26.840 --> 00:12:28.240
Then your whole table will be empty.

474
00:12:28.960 --> 00:12:30.400
Don't even run delete from orders by mistake.

475
00:12:31.820 --> 00:12:32.160
Run with where.

476
00:12:32.840 --> 00:12:34.380
And the tip I told you at the

477
00:12:34.380 --> 00:12:35.140
beginning of the video.

478
00:12:35.320 --> 00:12:37.020
First run the select query.

479
00:12:37.500 --> 00:12:37.980
By using your where.

480
00:12:38.680 --> 00:12:39.700
Whether you are updating.

481
00:12:39.840 --> 00:12:40.340
Or deleting.

482
00:12:56.560 --> 00:13:02.520
I hope you are enjoying this course so

483
00:13:02.520 --> 00:13:02.820
far.

484
00:13:03.180 --> 00:13:04.420
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.670
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will talk about how

2
00:00:02.670 --> 00:00:05.190
to alter a table in MySQL.

3
00:00:05.770 --> 00:00:07.590
So, if I show you my tables, we

4
00:00:07.590 --> 00:00:09.390
have a client's table and an order's table.

5
00:00:09.690 --> 00:00:11.530
Our client's table looks like this.

6
00:00:11.750 --> 00:00:14.030
As you can see here, name is varchar,

7
00:00:14.290 --> 00:00:18.170
email is varchar150, age is integer, phone number

8
00:00:18.170 --> 00:00:20.050
is varchar15 and so on.

9
00:00:20.330 --> 00:00:22.750
Now, I will tell you how to change

10
00:00:22.750 --> 00:00:22.850
this.

11
00:00:23.110 --> 00:00:25.930
So, by altering the table, you have a

12
00:00:25.930 --> 00:00:28.130
SQL command which helps you to change the

13
00:00:28.130 --> 00:00:28.230
table.

14
00:00:28.230 --> 00:00:30.290
So, what I will do here is, first

15
00:00:30.290 --> 00:00:33.370
of all, I will write use ecom, which

16
00:00:33.370 --> 00:00:34.610
will be used by our ecom database.

17
00:00:35.310 --> 00:00:38.090
After this, I will write select star from

18
00:00:38.090 --> 00:00:42.130
clients, just so that you can see how

19
00:00:42.130 --> 00:00:44.050
our client's table looks like.

20
00:00:44.530 --> 00:00:45.750
But let's do it for orders.

21
00:00:45.970 --> 00:00:49.770
After that, we can delete everything and run

22
00:00:49.770 --> 00:00:51.370
our started SQL script again.

23
00:00:51.950 --> 00:00:53.610
So, if I do this, you can see

24
00:00:53.610 --> 00:00:55.390
all my orders are visible to me.

25
00:00:56.110 --> 00:00:58.170
Now, let's say I want to change my

26
00:00:58.170 --> 00:01:03.269
delivery date or payment mode.

27
00:01:04.930 --> 00:01:07.290
Let's say I want to change it to

28
00:01:07.290 --> 00:01:08.630
varchar50.

29
00:01:09.110 --> 00:01:11.050
Let's see my order's table.

30
00:01:11.490 --> 00:01:13.630
My payment mode is varchar30.

31
00:01:13.770 --> 00:01:14.550
Let's say I want to change it to

32
00:01:14.550 --> 00:01:15.550
varchar50.

33
00:01:16.190 --> 00:01:17.230
So, how will I do that?

34
00:01:17.370 --> 00:01:18.970
So, what I will do here is, I

35
00:01:18.970 --> 00:01:22.370
will cut this and I will write alter

36
00:01:22.370 --> 00:01:23.450
table.

37
00:01:23.450 --> 00:01:25.870
I will write alter table.

38
00:01:28.570 --> 00:01:30.390
And I will write orders.

39
00:01:30.530 --> 00:01:31.750
So, basically, I am saying to alter order's

40
00:01:31.750 --> 00:01:32.090
table.

41
00:01:33.270 --> 00:01:35.690
Add a column and we will name that

42
00:01:35.690 --> 00:01:37.890
column as delivery partner.

43
00:01:38.030 --> 00:01:39.670
Let's say, who has delivered, it will be

44
00:01:39.670 --> 00:01:40.210
stored in this.

45
00:01:40.470 --> 00:01:42.310
So, I can add a column here.

46
00:01:42.970 --> 00:01:46.790
And I will write varchar and let's say

47
00:01:46.790 --> 00:01:47.390
varchar50.

48
00:01:47.730 --> 00:01:49.050
After this, I will also tell you how

49
00:01:49.050 --> 00:01:49.710
to change a given column.

50
00:01:50.430 --> 00:01:51.930
So, if I do this, I will put

51
00:01:51.930 --> 00:01:53.510
semicolon and close it.

52
00:01:54.250 --> 00:01:55.330
So, what will this line do?

53
00:01:55.490 --> 00:01:57.350
This line will alter my order's table.

54
00:01:57.670 --> 00:01:58.910
And it will add a new column in

55
00:01:58.910 --> 00:01:59.850
it, delivery partner.

56
00:02:00.110 --> 00:02:01.570
So, now my order's table looks like this.

57
00:02:01.710 --> 00:02:03.450
Now, look here, it is showing you how

58
00:02:03.450 --> 00:02:04.670
your order's table looks.

59
00:02:05.290 --> 00:02:07.110
But if I run it, then you see

60
00:02:07.110 --> 00:02:08.070
a green tick here.

61
00:02:08.470 --> 00:02:10.090
And it is saying that zero dose affected.

62
00:02:10.270 --> 00:02:11.210
But your table has been changed.

63
00:02:11.910 --> 00:02:13.450
And if I refresh it, then you see

64
00:02:13.450 --> 00:02:16.450
a new delivery partner column has been added

65
00:02:16.450 --> 00:02:16.550
here.

66
00:02:16.550 --> 00:02:19.390
Which means, if I do this, comment out.

67
00:02:19.870 --> 00:02:22.310
And I do select start from orders here.

68
00:02:22.390 --> 00:02:23.830
Then you will see a delivery partner.

69
00:02:24.470 --> 00:02:25.750
Obviously, its values will be null.

70
00:02:26.550 --> 00:02:28.070
But you got the point.

71
00:02:28.470 --> 00:02:29.950
You have got a new column added.

72
00:02:30.670 --> 00:02:31.690
Now, let's say I want to modify an

73
00:02:31.690 --> 00:02:32.710
existing column.

74
00:02:35.530 --> 00:02:37.430
So, what I will do here, I will

75
00:02:37.430 --> 00:02:40.530
write alter table orders.

76
00:02:40.750 --> 00:02:42.530
And after this, I will write modify.

77
00:02:42.530 --> 00:02:45.250
Let's say I want to modify price per

78
00:02:45.250 --> 00:02:45.610
unit.

79
00:02:46.950 --> 00:02:49.850
And I want to modify it to say

80
00:02:49.850 --> 00:02:51.970
decimal 12.2. So, now you see here

81
00:02:51.970 --> 00:02:53.610
it is decimal 10.2. I want to

82
00:02:53.610 --> 00:02:56.050
make it decimal 12.2. So, how will

83
00:02:56.050 --> 00:02:56.410
I do it?

84
00:02:56.770 --> 00:03:00.730
I will write here decimal 12.2. So,

85
00:03:00.810 --> 00:03:02.790
now it is decimal 10.2. And I

86
00:03:02.790 --> 00:03:04.510
am making it decimal 12.2. Or maybe

87
00:03:04.510 --> 00:03:05.510
I want to change something else, then I

88
00:03:05.510 --> 00:03:05.870
can do it.

89
00:03:06.150 --> 00:03:06.850
So, I will run it.

90
00:03:06.970 --> 00:03:07.910
Now, you see a green tick has come.

91
00:03:08.230 --> 00:03:09.970
And after that, my select start from orders

92
00:03:09.970 --> 00:03:10.190
worked.

93
00:03:10.190 --> 00:03:12.150
And if I refresh it, then you see

94
00:03:12.150 --> 00:03:13.890
here it is decimal 12.2. Earlier it

95
00:03:13.890 --> 00:03:15.070
was 10.2, now it is 12.2.

96
00:03:15.770 --> 00:03:17.590
So, in this way, you can modify a

97
00:03:17.590 --> 00:03:17.870
column.

98
00:03:19.810 --> 00:03:23.130
So, here you can also change the size

99
00:03:23.130 --> 00:03:23.230
of a column.

100
00:03:23.790 --> 00:03:25.030
For example, if a var char is 30,

101
00:03:25.250 --> 00:03:26.250
then make it var char 50.

102
00:03:26.850 --> 00:03:28.630
If a var char is 20, then make

103
00:03:28.630 --> 00:03:30.790
it var char 90 and so on.

104
00:03:31.250 --> 00:03:32.370
Now, let's say I want to rename a

105
00:03:32.370 --> 00:03:32.850
column.

106
00:03:34.210 --> 00:03:35.850
Let's say I don't like a name of

107
00:03:35.850 --> 00:03:36.150
a column.

108
00:03:36.690 --> 00:03:38.610
For example, if the name of this city

109
00:03:38.610 --> 00:03:41.730
is customer city, then it would have been

110
00:03:41.730 --> 00:03:41.910
nice.

111
00:03:42.450 --> 00:03:43.250
If someone asks why?

112
00:03:43.610 --> 00:03:46.210
I just feel like changing it.

113
00:03:46.770 --> 00:03:48.170
So, what we will do here?

114
00:03:48.290 --> 00:03:48.670
We will do alter.

115
00:03:49.050 --> 00:03:51.070
We will write alter table orders.

116
00:03:51.130 --> 00:03:51.970
This much is going to remain the same.

117
00:03:52.570 --> 00:03:54.730
Then we will write rename here.

118
00:03:55.270 --> 00:03:56.470
And we will say column.

119
00:03:57.190 --> 00:04:00.050
And here we will write city to customer

120
00:04:00.050 --> 00:04:01.130
underscore city.

121
00:04:01.270 --> 00:04:02.330
Or my customer city.

122
00:04:02.510 --> 00:04:03.810
In whichever column you want to rename.

123
00:04:04.190 --> 00:04:04.870
It's up to you.

124
00:04:04.870 --> 00:04:06.530
Whatever new name you want to give.

125
00:04:06.610 --> 00:04:10.070
So, you have basically changed its name.

126
00:04:10.450 --> 00:04:10.990
You have changed the name.

127
00:04:11.550 --> 00:04:12.230
You will run.

128
00:04:12.490 --> 00:04:13.930
You see where the city was coming, the

129
00:04:13.930 --> 00:04:14.730
customer city is coming.

130
00:04:15.149 --> 00:04:15.910
The city is written here.

131
00:04:16.269 --> 00:04:17.490
But if you refresh, it will become a

132
00:04:17.490 --> 00:04:17.990
customer city.

133
00:04:18.269 --> 00:04:19.110
So, you have to use this refresh button.

134
00:04:19.829 --> 00:04:21.410
Many people get confused in this matter.

135
00:04:21.950 --> 00:04:23.210
They feel that the table has not changed.

136
00:04:23.610 --> 00:04:24.470
Showing city here.

137
00:04:24.810 --> 00:04:26.110
Brother, refresh it once.

138
00:04:26.290 --> 00:04:27.690
See, it became a customer city.

139
00:04:28.350 --> 00:04:30.810
So, it becomes very important for you to

140
00:04:30.810 --> 00:04:30.910
refresh here.

141
00:04:31.870 --> 00:04:32.510
Very good.

142
00:04:32.510 --> 00:04:34.050
Now let's talk.

143
00:04:34.070 --> 00:04:35.730
If I have to remove a column.

144
00:04:35.950 --> 00:04:36.750
So, how will I remove it?

145
00:04:36.890 --> 00:04:37.970
Suppose I have to remove the delivery partner.

146
00:04:38.690 --> 00:04:39.710
I added a delivery partner.

147
00:04:40.310 --> 00:04:41.250
But now I have to remove it.

148
00:04:41.750 --> 00:04:43.010
I don't want it.

149
00:04:43.130 --> 00:04:44.210
I just did it to show you.

150
00:04:44.670 --> 00:04:45.510
Suppose I say something like this.

151
00:04:46.010 --> 00:04:47.930
So, I will keep alter table orders.

152
00:04:49.070 --> 00:04:51.670
Then I will say drop column.

153
00:04:52.550 --> 00:04:53.650
And whatever column I have to drop.

154
00:04:54.010 --> 00:04:55.010
Whether I have to drop the ratings column.

155
00:04:55.530 --> 00:04:56.210
Let's say I drop the rating.

156
00:04:56.890 --> 00:04:57.030
Okay.

157
00:04:57.290 --> 00:04:58.070
I drop the rating column.

158
00:04:58.990 --> 00:05:00.210
If I run it, see.

159
00:05:00.350 --> 00:05:01.590
There was a rating column here.

160
00:05:01.590 --> 00:05:03.130
See, there is a rating here.

161
00:05:03.230 --> 00:05:04.210
I will refresh it.

162
00:05:04.250 --> 00:05:04.550
It will disappear.

163
00:05:04.810 --> 00:05:04.910
See.

164
00:05:05.310 --> 00:05:07.190
So, I basically changed the structure of the

165
00:05:07.190 --> 00:05:07.290
table.

166
00:05:07.670 --> 00:05:09.110
If there is data in your table.

167
00:05:09.610 --> 00:05:10.010
Then it will go.

168
00:05:10.290 --> 00:05:10.990
Remember this.

169
00:05:11.250 --> 00:05:11.450
Okay.

170
00:05:12.070 --> 00:05:12.870
This is very important.

171
00:05:13.430 --> 00:05:14.190
And understand your thoughts.

172
00:05:14.550 --> 00:05:15.250
That's why you run your queries.

173
00:05:16.350 --> 00:05:17.330
So, what did we do now?

174
00:05:17.510 --> 00:05:18.130
Dropped the column.

175
00:05:19.470 --> 00:05:21.910
Now we will see how table data drops.

176
00:05:22.190 --> 00:05:23.510
And how table structure drops.

177
00:05:23.810 --> 00:05:24.910
Suppose you have a table.

178
00:05:25.310 --> 00:05:27.030
And you want that this table is not

179
00:05:27.030 --> 00:05:27.150
coming.

180
00:05:27.310 --> 00:05:29.130
Suppose this order table is not coming.

181
00:08:17.710 --> 00:08:21.470
If exists.

182
00:08:24.890 --> 00:08:26.210
If exists.

183
00:08:28.570 --> 00:08:30.610
So basically you are asking to drop the

184
00:08:30.610 --> 00:08:34.549
table if it exists, so basically you are

185
00:08:34.549 --> 00:08:36.510
asking to drop the table if it exists,

186
00:08:37.650 --> 00:08:39.669
so basically you are asking to drop the

187
00:08:39.669 --> 00:08:42.010
table if it exists, so basically you are

188
00:08:42.010 --> 00:08:42.750
asking to drop the table if it exists,

189
00:08:42.750 --> 00:08:43.850
so basically you are asking to drop the

190
00:08:43.850 --> 00:08:45.450
table if it exists, so basically you are

191
00:08:45.450 --> 00:08:45.570
asking to drop the table if it exists,

192
00:08:45.570 --> 00:08:45.710
so basically you are asking to drop the

193
00:08:45.710 --> 00:08:45.810
table if it exists, so basically you are

194
00:08:45.810 --> 00:08:45.910
asking to drop the table if it exists,

195
00:08:45.910 --> 00:08:46.490
so basically you are asking to drop the

196
00:08:46.490 --> 00:08:47.590
table if it exists, so basically you are

197
00:08:47.590 --> 00:08:50.030
asking to drop the table if it exists,

198
00:08:50.050 --> 00:08:51.810
so basically you are asking to drop the

199
00:08:51.810 --> 00:08:54.290
table if it exists, so basically you are

200
00:08:54.290 --> 00:08:54.930
asking to drop the table if it exists,

201
00:08:55.610 --> 00:08:56.910
so basically you are asking to drop the

202
00:08:56.910 --> 00:08:57.330
table if it exists, so basically you are

203
00:08:57.330 --> 00:08:57.430
asking to drop the table if it exists,

204
00:08:57.430 --> 00:08:57.530
so basically you are asking to drop the

205
00:08:57.530 --> 00:08:57.630
table if it exists, so basically you are

206
00:08:57.630 --> 00:08:57.730
asking to drop the table if it exists,

207
00:08:57.730 --> 00:08:57.830
so basically you are asking to drop the

208
00:08:57.830 --> 00:09:04.170
table if it exists, so basically you are

209
00:09:04.170 --> 00:09:17.110
asking

210
00:09:17.110 --> 00:09:20.890
to drop the table if it exists, so

211
00:09:20.890 --> 00:09:20.990
basically you are asking to drop the table

212
00:09:20.990 --> 00:09:21.090
if it exists, so basically you are asking

213
00:09:21.090 --> 00:09:21.190
to drop the table if it exists, so

214
00:09:21.190 --> 00:09:21.290
basically you are asking to drop the table

215
00:09:21.290 --> 00:09:21.610
if it exists, so basically you are asking

216
00:09:21.610 --> 00:09:21.710
to drop the table


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to see

2
00:00:02.130 --> 00:00:06.010
a very important thing which is called Transactions

3
00:00:06.010 --> 00:00:07.490
in MySQL.

4
00:00:08.170 --> 00:00:11.010
Why are transactions important and what are the

5
00:00:11.010 --> 00:00:13.030
transactions, let us understand this first.

6
00:00:13.310 --> 00:00:16.090
Before I write any query or show you

7
00:00:16.090 --> 00:00:19.350
what is there in my table, how you

8
00:00:19.350 --> 00:00:21.990
can make changes, before doing all this, I

9
00:00:21.990 --> 00:00:25.330
want to tell you why do we use

10
00:00:25.330 --> 00:00:25.430
transactions.

11
00:00:25.430 --> 00:00:27.530
Let us say you made a change and

12
00:00:27.530 --> 00:00:30.590
you updated a table and after updating this

13
00:00:30.590 --> 00:00:32.610
table, you came to know that oh no,

14
00:00:32.850 --> 00:00:34.750
what did I do, I should not have

15
00:00:34.750 --> 00:00:34.890
done this.

16
00:00:35.650 --> 00:00:38.810
We are humans, humans make mistakes and sometimes

17
00:00:38.810 --> 00:00:41.370
we want to avoid this mistake.

18
00:00:42.190 --> 00:00:43.390
So what are transactions basically?

19
00:00:44.070 --> 00:00:48.330
Until you commit, your query will not be

20
00:00:48.330 --> 00:00:50.310
saved permanently, it will be saved only temporarily.

21
00:00:50.310 --> 00:00:53.530
So understand this as a security layer that

22
00:00:53.530 --> 00:00:55.850
until you save, your file will not be

23
00:00:55.850 --> 00:00:56.110
saved.

24
00:00:56.450 --> 00:00:57.990
For example, whenever you write anything in VS

25
00:00:57.990 --> 00:01:00.330
code or notepad, let us say you wrote

26
00:01:00.330 --> 00:01:02.510
something like this and you did not save

27
00:01:02.510 --> 00:01:04.590
it, so until you do not save it,

28
00:01:04.610 --> 00:01:06.570
that change is temporary and as soon as

29
00:01:06.570 --> 00:01:08.770
you save it, that change becomes permanent.

30
00:01:09.510 --> 00:01:12.430
Whenever we open Microsoft Word, whatever you write

31
00:01:12.430 --> 00:01:13.510
in Microsoft Word, you close it, so it

32
00:01:13.510 --> 00:01:14.950
asks, do you want to save the changes,

33
00:01:15.110 --> 00:01:18.170
if you say yes, then your change is

34
00:01:18.170 --> 00:01:21.050
permanent or else your change is not saved.

35
00:01:21.610 --> 00:01:23.050
So in SQL, we get to see something

36
00:01:23.050 --> 00:01:25.550
like this.

37
00:01:26.830 --> 00:01:28.530
So what I am going to do now,

38
00:01:28.830 --> 00:01:31.790
first of all, our starter SQL, we wrote

39
00:01:31.790 --> 00:01:34.990
a starter SQL, if you remember, what we

40
00:01:34.990 --> 00:01:38.070
did in that starter SQL, we wrote a

41
00:01:38.070 --> 00:01:40.430
very basic script that populates our table.

42
00:01:41.430 --> 00:01:43.850
So I will quickly run those two queries

43
00:01:43.850 --> 00:01:50.050
because I will use ECOM first because my

44
00:01:50.050 --> 00:01:51.310
orders table has been deleted.

45
00:01:51.670 --> 00:01:53.870
We deleted it if you remember, so I

46
00:01:53.870 --> 00:01:57.430
did use ECOM and I am basically copying

47
00:01:57.430 --> 00:02:01.570
our old SQL and pasting it, so I

48
00:02:01.570 --> 00:02:03.390
am going to place all those values in

49
00:02:03.390 --> 00:02:08.490
order here, which we saw earlier as well.

50
00:02:08.710 --> 00:02:10.390
So if I run this, I will refresh

51
00:02:10.390 --> 00:02:14.170
it, orders are here, and now I will

52
00:02:14.170 --> 00:02:15.350
do select start from orders.

53
00:02:15.490 --> 00:02:16.610
So I will do one thing, I will

54
00:02:16.610 --> 00:02:19.950
do comment out, or I will delete it,

55
00:02:20.350 --> 00:02:21.410
or I will leave it because I want

56
00:02:21.410 --> 00:02:23.450
to give this SQL file to you, and

57
00:02:23.450 --> 00:02:33.350
I will write select start from orders and

58
00:02:33.350 --> 00:02:35.570
I will run this, so you see, after

59
00:02:35.570 --> 00:02:37.410
doing select start from orders, all the orders

60
00:02:37.410 --> 00:02:37.870
have come to us.

61
00:02:39.010 --> 00:02:41.130
Now what we will do here, you see

62
00:02:41.130 --> 00:02:45.430
carefully, before doing the transaction, you will have

63
00:02:45.430 --> 00:02:49.470
to turn off a flag, which is called

64
00:02:49.470 --> 00:02:52.230
auto commit, so here I do one thing,

65
00:02:52.610 --> 00:02:58.790
I write here, set auto commit equals to

66
00:02:58.790 --> 00:03:00.530
zero, now what are you doing, what are

67
00:03:00.530 --> 00:03:02.430
you writing, so basically what we are doing

68
00:03:02.430 --> 00:03:04.270
is, auto commit flag is by default 1,

69
00:03:04.930 --> 00:03:07.550
but we are making it zero here, so

70
00:03:07.550 --> 00:03:10.110
we are basically saying, don't commit automatically, commit

71
00:03:10.110 --> 00:03:13.930
means save, if you have worked in git,

72
00:03:14.490 --> 00:03:16.430
then you know what commit is, but if

73
00:03:16.430 --> 00:03:18.290
you haven't done it, then commit means, save

74
00:03:18.290 --> 00:03:22.270
anything, so here set auto commit is equal

75
00:03:22.270 --> 00:03:24.290
to zero, what will happen, we are basically

76
00:03:24.290 --> 00:03:29.450
saying, don't commit automatically, this tells SQL, don't

77
00:03:29.450 --> 00:03:37.330
save changes automatically, when auto commit is on,

78
00:03:38.250 --> 00:03:41.490
then insert, update and delete are saved immediately,

79
00:03:41.870 --> 00:03:44.150
and you can't undo, when auto commit is

80
00:03:44.150 --> 00:03:47.970
off, changes are temporary, and you can choose,

81
00:03:48.790 --> 00:03:51.430
either save them or undo them, so we

82
00:03:51.430 --> 00:03:52.610
have done the same, we have turned off

83
00:03:52.610 --> 00:03:55.170
auto commit, so I have turned off auto

84
00:03:55.170 --> 00:03:57.790
commit here, and now what I am going

85
00:03:57.790 --> 00:03:59.430
to do, now you see what I am

86
00:03:59.430 --> 00:04:01.890
going to do, I will update here, I

87
00:04:01.890 --> 00:04:05.490
will write update, and I will write orders,

88
00:04:05.910 --> 00:04:10.650
and I will write, set order status equals

89
00:04:10.650 --> 00:04:16.589
to, let's say, cancelled for order id, means

90
00:04:16.589 --> 00:04:19.709
where order underscore id is equal to 3,

91
00:04:19.850 --> 00:04:22.550
so this statement is basically saying, cancel order

92
00:04:22.550 --> 00:04:25.630
status for order id is equal to 3,

93
00:04:25.730 --> 00:04:28.550
simple thing, so I will do one thing,

94
00:04:28.870 --> 00:04:30.530
I will cut this, and I will write

95
00:04:30.530 --> 00:04:32.450
this later, so we will change this, and

96
00:04:32.450 --> 00:04:34.690
then we will see our orders, so I

97
00:04:34.690 --> 00:04:37.590
did this, I run this, oops, I have

98
00:04:37.590 --> 00:04:40.010
selected and run this, I have run this,

99
00:04:40.090 --> 00:04:42.990
and you can see here, order id is

100
00:04:42.990 --> 00:04:45.790
cancelled for 3, okay, so we have done

101
00:04:45.790 --> 00:04:50.090
this, but is this change permanent or temporary,

102
00:04:50.810 --> 00:04:52.990
the answer is, now we feel that it

103
00:04:52.990 --> 00:04:56.290
is permanent, but I have to tell mysql

104
00:04:56.290 --> 00:05:00.370
that this change is temporary or permanent, if

105
00:05:00.370 --> 00:05:03.310
I write commit, something like this, so I

106
00:05:03.310 --> 00:05:05.610
am basically telling mysql that this change is

107
00:05:05.610 --> 00:05:08.770
permanent, do this, commit, do this, save, when

108
00:05:08.770 --> 00:05:11.050
I write commit, I am basically saying save

109
00:05:11.050 --> 00:05:15.150
all the changes permanently, and changes cannot be

110
00:05:15.150 --> 00:05:43.170
undone after this, so basically this

111
00:05:43.170 --> 00:05:45.630
change is permanent, but if I do rollback,

112
00:05:45.890 --> 00:05:47.650
so what will happen, if I do this,

113
00:05:48.150 --> 00:05:52.670
I said rollback, so what will happen, if

114
00:05:52.670 --> 00:05:55.030
I do rollback, let's say I cancel 22

115
00:05:55.030 --> 00:05:57.890
here, and I said select start from order,

116
00:05:58.010 --> 00:06:00.450
I will remove this, I run this, and

117
00:06:00.450 --> 00:06:02.850
you see, I did rollback, so I did

118
00:06:02.850 --> 00:06:04.910
change here, and then I did rollback, so

119
00:06:04.910 --> 00:06:06.930
it means that I am taking my change

120
00:06:06.930 --> 00:06:08.990
back, so we have zeroed the auto-commit,

121
00:06:10.070 --> 00:06:12.810
it means that if we change anything, let

122
00:06:12.810 --> 00:06:14.210
me do one thing, I keep these things

123
00:06:14.210 --> 00:06:15.950
one by one, so let's say I did

124
00:06:15.950 --> 00:06:18.650
this, so what will happen, order status will

125
00:06:18.650 --> 00:06:21.650
be cancelled 22, so if I write here

126
00:06:21.650 --> 00:06:25.360
select start from orders, select start from orders,

127
00:06:26.370 --> 00:06:28.030
so what will you get to see, let

128
00:06:28.030 --> 00:06:30.510
me comment this out, so you will get

129
00:06:30.510 --> 00:06:33.170
to see cancel 22, you can see cancel

130
00:06:33.170 --> 00:06:36.970
22, but if after this, let me close

131
00:06:36.970 --> 00:06:39.110
this, and if after this I said rollback,

132
00:06:39.590 --> 00:06:43.010
so here after running this, I can undo

133
00:06:43.010 --> 00:06:45.430
this change, so I have basically undone this,

134
00:06:45.890 --> 00:06:47.310
and now if I do select start from

135
00:06:47.310 --> 00:06:50.150
orders, let me select this and do this,

136
00:06:50.290 --> 00:06:55.430
and comment out rollback, so you will see

137
00:06:55.430 --> 00:06:59.070
here cancel 22 is not there, so here

138
00:06:59.070 --> 00:07:02.110
you can see cancel 22 is not there

139
00:07:02.110 --> 00:07:04.410
for order id is equal to 3, I

140
00:07:04.410 --> 00:07:07.710
hope that you have understood that how this

141
00:07:08.610 --> 00:07:12.530
commit, auto-commit, rollback works, auto-commit is

142
00:07:12.530 --> 00:07:14.570
a flag which we have to zero, and

143
00:07:14.570 --> 00:07:16.790
after this, once you have zeroed it, so

144
00:07:16.790 --> 00:07:20.450
automatically changes will not be your commit, so

145
00:07:20.450 --> 00:07:22.170
if you change anything, then after that you

146
00:07:22.170 --> 00:07:23.610
will have to write either commit or rollback,

147
00:07:24.110 --> 00:07:26.170
if you do rollback, then you are basically

148
00:07:26.170 --> 00:07:28.810
saying that these things are final, if you

149
00:07:28.810 --> 00:07:30.410
are writing rollback, then basically you are saying

150
00:07:30.410 --> 00:07:32.670
that these things are not final, whatever I

151
00:07:32.670 --> 00:07:34.950
have done before the last commit, do all

152
00:07:34.950 --> 00:07:38.150
that rollback, so rollback is undo, so you

153
00:07:38.150 --> 00:07:40.430
must have committed first, till then the save

154
00:07:40.430 --> 00:07:42.170
will be there, after that the save will

155
00:07:42.170 --> 00:07:43.990
not be there, if you did rollback, so

156
00:07:43.990 --> 00:07:47.530
practise, I have given you the handbook, read

157
00:07:47.530 --> 00:07:49.730
that, you will read that well, so you

158
00:07:49.730 --> 00:07:51.870
will understand how these things are working, I

159
00:07:51.870 --> 00:07:54.890
hope that you are understanding thank you so

160
00:07:54.890 --> 00:07:57.110
much guys for watching this video, and I

161
00:07:57.110 --> 00:07:58.390
will see you in the next one


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.090
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will learn about constraints

2
00:00:02.090 --> 00:00:03.430
in mysql.

3
00:00:03.550 --> 00:00:04.710
So, what are constraints?

4
00:00:05.130 --> 00:00:08.030
Constraints are basically rules applied to table columns

5
00:00:08.030 --> 00:00:09.950
to control what data can be stored.

6
00:00:10.370 --> 00:00:13.770
Means, if I want that there should not

7
00:00:13.770 --> 00:00:15.930
be more than 3 values in a particular

8
00:00:15.930 --> 00:00:18.370
column, either 1 or 2 or 3, let's

9
00:00:18.370 --> 00:00:19.610
say I want this, then I can tell

10
00:00:19.610 --> 00:00:20.410
this through constraints.

11
00:00:21.730 --> 00:00:23.710
If I want that duplicate values should not

12
00:00:23.710 --> 00:00:25.010
be allowed, then I can tell this through

13
00:00:25.010 --> 00:00:25.550
constraints.

14
00:00:27.270 --> 00:00:29.410
So, we have 4 types of constraints.

15
00:00:29.410 --> 00:00:31.570
These 4 constraints are used the most.

16
00:00:31.910 --> 00:00:34.090
So, first we have unique constraint.

17
00:00:34.270 --> 00:00:37.830
We use unique constraint when we do not

18
00:00:37.830 --> 00:00:39.390
want duplicate values at any cost.

19
00:00:40.550 --> 00:00:45.090
Means, we want that all our values should

20
00:00:45.090 --> 00:00:47.370
be unique and there should not be duplicate

21
00:00:47.370 --> 00:00:47.830
in it.

22
00:00:48.290 --> 00:00:49.330
So, we will use unique constraint.

23
00:00:50.610 --> 00:00:52.830
Not null means, its name is telling, it

24
00:00:52.830 --> 00:00:55.970
ensures that null values cannot come in the

25
00:00:55.970 --> 00:00:56.070
column.

26
00:00:56.070 --> 00:00:58.450
Then after this, there is a check constraint,

27
00:00:58.870 --> 00:01:00.130
which we will understand through example.

28
00:01:01.290 --> 00:01:04.530
It checks the condition and checks that this

29
00:01:04.530 --> 00:01:06.370
condition is being satisfied, not for every value.

30
00:01:07.670 --> 00:01:09.870
If it is not satisfied for any value,

31
00:01:10.250 --> 00:01:12.310
then it will not allow insertion of that

32
00:01:12.310 --> 00:01:12.570
value.

33
00:01:12.650 --> 00:01:14.170
We will see this in detail and you

34
00:01:14.170 --> 00:01:14.870
will understand it well.

35
00:01:15.390 --> 00:01:18.010
Then after this, we have default constraint, which

36
00:01:18.010 --> 00:01:20.410
automatically assigns a default value.

37
00:01:21.550 --> 00:01:25.450
Let's say, you want that if you insert

38
00:01:25.450 --> 00:01:29.190
salary in any row, then by default salary

39
00:01:29.190 --> 00:01:29.830
is 30,000.

40
00:01:30.630 --> 00:01:32.850
So, we can keep that 30,000 as

41
00:01:32.850 --> 00:01:33.390
it is.

42
00:01:33.690 --> 00:01:35.170
I hope you got the point.

43
00:01:35.610 --> 00:01:38.230
Now, we will make a table named employees.

44
00:01:39.270 --> 00:01:40.830
I am making a table named employees.

45
00:01:41.270 --> 00:01:44.070
You will get the handbook, so don't worry.

46
00:01:44.070 --> 00:01:45.950
I will make arrangements for you to copy

47
00:01:45.950 --> 00:01:47.070
easily.

48
00:01:49.090 --> 00:01:50.270
You will be able to copy by clicking

49
00:01:50.270 --> 00:01:51.410
on a button below.

50
00:01:51.570 --> 00:01:52.090
So, you will get all those things.

51
00:01:53.550 --> 00:01:56.790
Let's create a new SQL script.

52
00:01:56.890 --> 00:01:57.830
No, not new SQL script.

53
00:01:58.110 --> 00:01:59.450
Not open SQL script.

54
00:01:59.910 --> 00:02:00.590
New query tab.

55
00:02:00.930 --> 00:02:03.210
Here, I am saying, make a table named

56
00:02:03.210 --> 00:02:03.310
employees.

57
00:02:03.490 --> 00:02:05.090
So, now I have a client's orders table.

58
00:02:05.190 --> 00:02:06.130
I will make a new table to do

59
00:02:06.130 --> 00:02:06.730
all these things.

60
00:02:07.610 --> 00:02:08.789
And then I will drop it later.

61
00:02:09.770 --> 00:02:11.250
Now, what I did is, I made a

62
00:02:11.250 --> 00:02:11.710
new table.

63
00:02:11.870 --> 00:02:12.370
Let's run it.

64
00:02:12.370 --> 00:02:14.010
So, basically a table is made with the

65
00:02:14.010 --> 00:02:14.370
name of employees.

66
00:02:14.770 --> 00:02:15.850
Let me refresh it.

67
00:02:15.950 --> 00:02:17.590
Now, you can see that a table is

68
00:02:17.590 --> 00:02:17.750
made with the name of employees.

69
00:02:17.850 --> 00:02:18.490
What is there in it?

70
00:02:18.970 --> 00:02:19.790
There is an employee ID.

71
00:02:20.050 --> 00:02:20.730
I said it will be an integer.

72
00:02:21.530 --> 00:02:23.770
I have put an auto increment of primary.

73
00:02:23.950 --> 00:02:25.250
I will tell you about it later.

74
00:02:25.730 --> 00:02:27.170
We will talk about the auto increment of

75
00:02:27.170 --> 00:02:28.150
primary in the next video.

76
00:02:28.830 --> 00:02:30.270
But, in short, what is the primary?

77
00:02:31.690 --> 00:02:33.590
It is a unique identifier, like a roll

78
00:02:33.590 --> 00:02:33.790
number.

79
00:02:34.030 --> 00:02:35.710
And auto increment means, it will automatically increase

80
00:02:35.710 --> 00:02:36.430
by 1, 2, 3, 4.

81
00:02:38.230 --> 00:02:39.210
Now, look here.

82
00:02:39.670 --> 00:02:40.650
I have used a unique constraint.

83
00:02:40.650 --> 00:02:43.750
And I have used not null here.

84
00:02:43.830 --> 00:02:45.530
Here, basically, we can have an email with

85
00:02:45.530 --> 00:02:47.770
a maximum of 150 characters.

86
00:02:50.010 --> 00:02:52.510
And I have said here that the name

87
00:02:52.510 --> 00:02:53.410
can be of 100 characters.

88
00:02:54.370 --> 00:02:55.110
The email will be unique.

89
00:02:55.590 --> 00:02:56.590
And you have to put the name.

90
00:02:56.950 --> 00:02:57.250
It cannot be null.

91
00:02:57.950 --> 00:02:59.750
So, I have put two constraints here.

92
00:03:00.190 --> 00:03:01.250
In email and name.

93
00:03:01.670 --> 00:03:02.810
Now, what I will do here is, I

94
00:03:02.810 --> 00:03:03.590
will comment this.

95
00:03:03.590 --> 00:03:04.390
And I will show you by inserting a

96
00:03:04.390 --> 00:03:04.690
value.

97
00:03:05.950 --> 00:03:08.530
So, I am copying exactly this query.

98
00:03:08.530 --> 00:03:10.350
I want to give you an example of

99
00:03:10.350 --> 00:03:12.910
a unique constraint here.

100
00:03:14.210 --> 00:03:16.310
And I want to show you that if

101
00:03:16.310 --> 00:03:16.950
I run this query.

102
00:03:17.950 --> 00:03:19.750
In which, I am basically saying that put

103
00:03:19.750 --> 00:03:20.170
this email.

104
00:03:20.810 --> 00:03:22.050
And put this name.

105
00:03:22.270 --> 00:03:22.910
Let's run this query.

106
00:03:23.630 --> 00:03:24.810
So, as soon as I run this query.

107
00:03:25.350 --> 00:03:26.190
You see, it is inserted.

108
00:03:26.550 --> 00:03:29.250
So, my email id is amit.company.com.

109
00:03:29.390 --> 00:03:31.050
And the name is Amit Sharma.

110
00:03:31.230 --> 00:03:32.410
So, I have put Amit Sharma here.

111
00:03:32.590 --> 00:03:34.450
And I have put amit.company.com here.

112
00:03:34.770 --> 00:03:37.130
Now, what I will do is, I will

113
00:03:37.130 --> 00:03:37.610
run it again.

114
00:03:37.610 --> 00:03:39.910
I will try to insert this record again.

115
00:03:40.630 --> 00:03:41.430
So, it is inserted once.

116
00:03:41.770 --> 00:03:42.790
I will try to insert it again.

117
00:03:43.590 --> 00:03:44.970
And you see, an error has come here.

118
00:03:45.290 --> 00:03:46.090
What error has come here?

119
00:03:46.250 --> 00:03:49.630
Duplicate entry amit.company.com for key employees

120
00:03:49.630 --> 00:03:52.770
.email Basically, it is saying that the email

121
00:03:52.770 --> 00:03:53.390
here should be unique.

122
00:03:54.250 --> 00:03:56.350
So, bring something where the email is unique.

123
00:03:57.190 --> 00:03:58.010
You will say, okay.

124
00:03:59.030 --> 00:04:00.110
I will change its name to Amit Sharma.

125
00:04:01.150 --> 00:04:01.630
No, no.

126
00:04:01.690 --> 00:04:02.590
The email should be unique.

127
00:04:03.410 --> 00:04:05.010
Assume that we try to insert this.

128
00:04:05.590 --> 00:04:06.470
The error has come again.

129
00:04:06.470 --> 00:04:07.850
You see, it is saying to change the

130
00:04:07.850 --> 00:04:08.250
email.

131
00:04:08.990 --> 00:04:12.450
If I put amit.company.com, then yes,

132
00:04:12.490 --> 00:04:12.830
it will be inserted.

133
00:04:13.290 --> 00:04:14.450
And if I let it be Amit Sharma,

134
00:04:14.890 --> 00:04:15.410
then it will work.

135
00:04:15.510 --> 00:04:16.649
You see, if I run it, then a

136
00:04:16.649 --> 00:04:17.190
green tick will come.

137
00:04:17.269 --> 00:04:18.089
You see, a green tick came.

138
00:04:18.450 --> 00:04:19.829
And it is inserted.

139
00:04:20.250 --> 00:04:22.490
So, what I will do is, if I

140
00:04:22.490 --> 00:04:26.790
write here, select star from employees.

141
00:04:26.910 --> 00:04:27.870
And I run it.

142
00:04:28.210 --> 00:04:28.970
So, you see here.

143
00:04:30.090 --> 00:04:31.750
I am getting to see amit.company.com

144
00:04:31.750 --> 00:04:33.950
Amit Sharma, amit.company.com Amit Sharma.

145
00:04:34.690 --> 00:04:36.870
So, this means that if I have put

146
00:04:36.870 --> 00:04:38.830
a unique constraint in the email, then the

147
00:04:38.830 --> 00:04:40.310
email should be unique.

148
00:04:41.350 --> 00:04:42.970
New emails can be inserted.

149
00:04:43.290 --> 00:04:44.210
The same email cannot be inserted.

150
00:04:45.090 --> 00:04:46.570
And if I say here that the name

151
00:04:46.570 --> 00:04:48.690
is not null, it means that I cannot

152
00:04:48.690 --> 00:04:49.330
null the name.

153
00:04:50.050 --> 00:04:51.230
So, let's do this and see.

154
00:04:51.490 --> 00:04:52.770
Let's do this and see.

155
00:04:53.270 --> 00:04:54.170
Now, I will do one thing.

156
00:04:54.390 --> 00:04:55.070
I will copy the same query.

157
00:04:56.210 --> 00:04:57.790
And I will paste it here.

158
00:04:58.270 --> 00:04:59.970
And what I will do is, I will

159
00:04:59.970 --> 00:05:00.490
try to null it.

160
00:05:00.490 --> 00:05:01.150
I will try to null it.

161
00:05:01.170 --> 00:05:02.770
I mean, I will take a completely new

162
00:05:02.770 --> 00:05:03.710
email id here.

163
00:05:03.890 --> 00:05:05.790
Let's say I do company2.com, which is

164
00:05:05.790 --> 00:05:06.470
a new email id.

165
00:05:06.550 --> 00:05:07.450
I have not used it yet.

166
00:05:07.570 --> 00:05:07.670
Okay.

167
00:05:08.130 --> 00:05:08.970
I will also make it hairy.

168
00:05:10.070 --> 00:05:11.410
It is a completely new email id.

169
00:05:11.830 --> 00:05:13.790
And here I am trying to insert null

170
00:05:13.790 --> 00:05:13.890
instead of name.

171
00:05:15.310 --> 00:05:16.210
Let's run this code.

172
00:05:16.390 --> 00:05:17.570
And you see, here it is saying that

173
00:05:17.570 --> 00:05:19.290
the column name cannot be null.

174
00:05:19.830 --> 00:05:21.430
Your column name cannot be null.

175
00:05:21.870 --> 00:05:22.750
You will have to put something or the

176
00:05:22.750 --> 00:05:22.850
other.

177
00:05:23.370 --> 00:05:26.030
So, these are our two constraints that we

178
00:05:26.030 --> 00:05:26.510
saw.

179
00:05:26.510 --> 00:05:26.610
Okay.

180
00:05:27.230 --> 00:05:29.090
Now, you must have noticed one thing here.

181
00:05:29.310 --> 00:05:30.070
That we have not put the employee id.

182
00:05:31.130 --> 00:05:32.670
Because this is a primary key and auto

183
00:05:32.670 --> 00:05:33.010
increment.

184
00:05:33.230 --> 00:05:34.630
That's why it will be automatically inserted.

185
00:05:34.910 --> 00:05:35.650
In the next video, I will explain you

186
00:05:35.650 --> 00:05:36.230
in a little more detail.

187
00:05:37.310 --> 00:05:39.830
But understand now, it is automatically inserted.

188
00:05:40.230 --> 00:05:41.550
Because of the primary key and auto increment

189
00:05:41.550 --> 00:05:42.130
that we have written.

190
00:05:42.750 --> 00:05:43.190
Okay.

191
00:05:43.890 --> 00:05:45.390
So, I hope you understood this thing.

192
00:05:46.170 --> 00:05:47.330
So, we saw a unique constraint.

193
00:05:47.650 --> 00:05:48.770
We saw a not null constraint.

194
00:05:49.070 --> 00:05:52.950
We saw that if we try to insert

195
00:05:52.950 --> 00:05:53.190
anything here.

196
00:05:53.950 --> 00:05:58.430
So that our table has null values.

197
00:05:58.990 --> 00:05:59.770
So, we cannot do that.

198
00:06:00.090 --> 00:06:00.190
Okay.

199
00:06:00.230 --> 00:06:01.290
We can null the rest.

200
00:06:01.610 --> 00:06:02.530
Now, look at our table.

201
00:06:03.170 --> 00:06:03.970
If I show it to you.

202
00:06:04.630 --> 00:06:06.010
So, it looks something like this.

203
00:06:06.130 --> 00:06:08.590
In which we have given varchar in email.

204
00:06:09.530 --> 00:06:10.510
We have given varchar in name.

205
00:06:10.870 --> 00:06:11.870
Now, what I will do here.

206
00:06:12.030 --> 00:06:12.650
I will drop this table.

207
00:06:13.510 --> 00:06:14.490
So, I will write here.

208
00:06:14.530 --> 00:06:16.590
Drop table employees.

209
00:06:16.970 --> 00:06:18.910
We have just seen two constraints.

210
00:06:19.210 --> 00:06:20.410
Now, I will do drop table employees.

211
00:06:20.890 --> 00:06:21.710
I blew the employees table.

212
00:06:21.710 --> 00:06:23.710
And now, I will make the employees table

213
00:06:23.710 --> 00:06:25.090
a little extended.

214
00:06:25.550 --> 00:06:26.630
Which I have given here in the handbook.

215
00:06:27.250 --> 00:06:28.290
I will make this employees table.

216
00:06:28.590 --> 00:06:30.190
In which there is employee id, email, name,

217
00:06:30.330 --> 00:06:31.870
age, department, salary, joining date.

218
00:06:32.210 --> 00:06:33.390
There are many more constraints.

219
00:06:33.830 --> 00:06:35.010
So, for now, you make this table.

220
00:06:35.630 --> 00:06:36.490
And you will get this code in the

221
00:06:36.490 --> 00:06:36.810
handbook.

222
00:06:37.230 --> 00:06:38.350
As I have already told you.

223
00:06:39.110 --> 00:06:40.090
We have already seen unique and not null.

224
00:06:41.350 --> 00:06:42.470
Now, let's see the check constraint.

225
00:06:42.930 --> 00:06:44.630
By inserting this query.

226
00:06:45.330 --> 00:06:46.190
So, what will I do first?

227
00:06:46.410 --> 00:06:47.070
I will run this.

228
00:06:47.210 --> 00:06:47.930
My table will be made.

229
00:06:48.090 --> 00:06:48.690
Green tick came.

230
00:06:48.770 --> 00:06:49.310
Table is made.

231
00:06:49.430 --> 00:06:49.530
Okay.

232
00:06:50.030 --> 00:06:50.910
Employee table is made.

233
00:06:50.950 --> 00:06:52.030
Let's refresh and check.

234
00:06:52.330 --> 00:06:52.890
Yes, it is made.

235
00:06:53.030 --> 00:06:53.890
See, all these things have come.

236
00:06:54.730 --> 00:06:55.690
Now, what we will do?

237
00:06:56.490 --> 00:06:57.090
We will copy this query.

238
00:06:57.810 --> 00:06:58.210
We will copy this query.

239
00:06:59.250 --> 00:07:00.710
And we will see here.

240
00:07:00.930 --> 00:07:01.790
What will happen by running this query?

241
00:07:02.690 --> 00:07:03.230
So, first of all.

242
00:07:03.770 --> 00:07:05.030
Let's step back and analyse.

243
00:07:05.910 --> 00:07:06.610
Email is this.

244
00:07:06.730 --> 00:07:07.430
Name is this.

245
00:07:07.730 --> 00:07:08.210
Age is this.

246
00:07:08.250 --> 00:07:08.770
Salary is this.

247
00:07:09.410 --> 00:07:09.990
Will there be an insertion?

248
00:07:10.450 --> 00:07:11.950
Is there anything that is required?

249
00:07:12.350 --> 00:07:13.270
See, email.

250
00:07:13.390 --> 00:07:13.950
This will be automatic.

251
00:07:14.270 --> 00:07:15.010
Email will also come.

252
00:07:15.230 --> 00:07:15.430
Okay.

253
00:07:15.570 --> 00:07:16.290
Name will also come.

254
00:07:16.430 --> 00:07:16.690
Okay.

255
00:07:16.690 --> 00:07:19.860
Will email amitatcompany.com come?

256
00:07:20.450 --> 00:07:21.030
Yes, it will come.

257
00:07:21.110 --> 00:07:22.510
Because I have just made the table empty.

258
00:07:23.430 --> 00:07:24.010
See here.

259
00:07:24.430 --> 00:07:26.330
And what we will do here?

260
00:07:26.910 --> 00:07:27.950
We have already inserted a check constraint in

261
00:07:27.950 --> 00:07:28.530
age.

262
00:07:29.270 --> 00:07:30.790
Age is greater than or equal to 18.

263
00:07:30.870 --> 00:07:31.370
So, it will fail.

264
00:07:31.610 --> 00:07:32.330
Because age is 25.

265
00:07:33.250 --> 00:07:33.710
Absolutely.

266
00:07:34.810 --> 00:07:35.410
It failed.

267
00:07:35.590 --> 00:07:36.090
Did it fail?

268
00:07:36.150 --> 00:07:37.230
No, it didn't.

269
00:07:37.250 --> 00:07:37.810
It didn't fail.

270
00:07:38.230 --> 00:07:38.970
Why didn't it fail?

271
00:07:39.230 --> 00:07:40.870
Didn't I insert a check constraint here?

272
00:07:42.270 --> 00:07:44.630
Didn't I insert a check constraint of age

273
00:07:44.630 --> 00:07:45.270
greater than 18?

274
00:07:45.270 --> 00:07:45.770
Okay.

275
00:07:45.930 --> 00:07:47.210
So, here age greater than 18 is already

276
00:07:47.210 --> 00:07:47.470
there.

277
00:07:47.550 --> 00:07:49.110
So, this is not a problematic thing.

278
00:07:49.550 --> 00:07:51.110
Now, if I make it 15 here.

279
00:07:51.190 --> 00:07:52.370
And let's say I make it amitasharma.

280
00:07:52.710 --> 00:07:54.890
I make it amitatcompany2.com.

281
00:07:55.190 --> 00:07:56.710
And if I run it, then you see

282
00:07:56.710 --> 00:07:57.230
it will not work.

283
00:07:57.370 --> 00:07:59.170
It didn't work because age greater than 18

284
00:07:59.170 --> 00:07:59.530
is not there.

285
00:07:59.790 --> 00:08:01.790
Now, see here it is saying employees chk

286
00:08:01.790 --> 00:08:03.370
underscore 1 is violated.

287
00:08:03.810 --> 00:08:04.490
Now, what is this?

288
00:08:04.610 --> 00:08:06.510
Employees chk underscore 1.

289
00:08:06.830 --> 00:08:07.710
If you look carefully.

290
00:08:08.230 --> 00:08:11.050
So, when I wrote age greater than or

291
00:08:11.050 --> 00:08:11.830
equal to 18.

292
00:08:12.510 --> 00:08:14.830
So, I didn't give any name of constraint

293
00:08:14.830 --> 00:08:14.930
in this.

294
00:08:14.930 --> 00:08:16.630
So, what happens is that by default it

295
00:08:16.630 --> 00:08:17.550
gives the name of constraint.

296
00:08:17.870 --> 00:08:19.310
So, here this constraint is violated.

297
00:08:19.490 --> 00:08:20.410
That's why error occurred.

298
00:08:20.630 --> 00:08:22.910
Now, let's see how the default constraint works.

299
00:08:23.850 --> 00:08:25.130
So, if you look carefully.

300
00:08:25.330 --> 00:08:25.950
When I made the table.

301
00:08:26.330 --> 00:08:27.530
So, I said something in my query.

302
00:08:28.330 --> 00:08:29.530
What did I say in my query?

303
00:08:29.650 --> 00:08:32.049
I said in my query that the joining

304
00:08:32.049 --> 00:08:34.110
date will be by default current date.

305
00:08:34.510 --> 00:08:34.630
Okay.

306
00:08:35.350 --> 00:08:36.070
Now, what is this current date?

307
00:08:36.270 --> 00:08:37.110
Current date is a function.

308
00:08:37.630 --> 00:08:40.090
But for now, you guys assume that by

309
00:08:40.090 --> 00:08:42.510
writing current underscore date, current date will come.

310
00:08:42.510 --> 00:08:43.330
So, even if I don't put the joining

311
00:08:43.330 --> 00:08:45.830
date, my joining date will come.

312
00:08:46.050 --> 00:08:47.570
So, if I show you guys here.

313
00:08:48.530 --> 00:08:52.550
Select star from and I write employees.

314
00:08:53.210 --> 00:08:54.250
So, you guys will get to see.

315
00:08:55.190 --> 00:08:56.850
That the joining date is here.

316
00:08:57.630 --> 00:08:59.390
By default, it has taken the current date.

317
00:08:59.950 --> 00:09:00.130
Okay.

318
00:09:00.450 --> 00:09:02.950
So, this is how you can use constraints

319
00:09:02.950 --> 00:09:04.010
in MySQL.

320
00:09:04.230 --> 00:09:05.730
Now, you guys can use alter to give

321
00:09:05.730 --> 00:09:06.410
the name of your constraint.

322
00:09:07.410 --> 00:09:09.990
For example, let's say for some reason.

323
00:09:09.990 --> 00:09:12.510
I want the age to be unique.

324
00:09:12.850 --> 00:09:13.550
This is a very strange thing.

325
00:09:13.850 --> 00:09:15.390
But let's say I want my age to

326
00:09:15.390 --> 00:09:15.810
be unique.

327
00:09:16.130 --> 00:09:17.210
So, what I will do here.

328
00:09:17.510 --> 00:09:18.410
I will use alter.

329
00:09:19.010 --> 00:09:20.710
And here I will say alter.

330
00:09:21.550 --> 00:09:22.110
Alter.

331
00:09:22.730 --> 00:09:23.710
I will delete this.

332
00:09:25.130 --> 00:09:28.450
I will write alter table employees.

333
00:09:28.870 --> 00:09:31.930
And after this, I will write add constraint.

334
00:09:32.210 --> 00:09:32.990
Which will add the constraint.

335
00:09:33.870 --> 00:09:35.370
And I will assume that I will name

336
00:09:35.370 --> 00:09:36.790
it my constraint.

337
00:09:36.790 --> 00:09:40.010
Or I will name it age underscore unique.

338
00:09:40.770 --> 00:09:43.870
And assume that I want my age to

339
00:09:43.870 --> 00:09:44.870
be unique.

340
00:09:45.370 --> 00:09:46.230
Which is a very strange thing.

341
00:09:46.450 --> 00:09:47.110
There is no point of age being unique.

342
00:09:47.890 --> 00:09:49.190
But let's say I want this.

343
00:09:49.410 --> 00:09:50.050
I will run this query.

344
00:09:50.710 --> 00:09:52.130
And you can see that my age will

345
00:09:52.130 --> 00:09:53.010
be unique.

346
00:09:53.710 --> 00:09:56.610
So, I just inserted a while ago.

347
00:09:57.170 --> 00:09:58.330
Let's say I insert this.

348
00:09:59.810 --> 00:10:01.110
And as soon as I insert this.

349
00:10:01.250 --> 00:10:02.850
Here one constraint is violated.

350
00:10:03.110 --> 00:10:03.870
I will do one thing.

351
00:10:03.870 --> 00:10:08.190
I will try to run this in this

352
00:10:08.190 --> 00:10:08.290
way.

353
00:10:09.190 --> 00:10:10.610
I think I am missing something.

354
00:10:10.710 --> 00:10:12.670
Let's see which constraint is being violated.

355
00:10:13.010 --> 00:10:14.230
Valcare 150.

356
00:10:14.550 --> 00:10:15.550
Name not null.

357
00:10:15.750 --> 00:10:16.770
I have given the name as well.

358
00:10:17.150 --> 00:10:17.470
Age.

359
00:10:17.610 --> 00:10:17.810
Okay.

360
00:10:17.970 --> 00:10:19.030
Age constraint is being violated.

361
00:10:19.310 --> 00:10:20.150
So, I will make it 55.

362
00:10:21.250 --> 00:10:21.790
And yes.

363
00:10:21.930 --> 00:10:22.510
Now, look at this.

364
00:10:22.550 --> 00:10:22.890
It got inserted.

365
00:10:23.470 --> 00:10:25.370
Now, if I make all this different.

366
00:10:25.990 --> 00:10:26.170
Okay.

367
00:10:26.890 --> 00:10:28.250
Let's say I make the salary different.

368
00:10:28.510 --> 00:10:29.370
And I try to insert this.

369
00:10:30.210 --> 00:10:30.770
So, it is saying.

370
00:10:32.390 --> 00:10:37.050
Duplicate entry 55 for key employee.age.unique.

371
00:10:37.310 --> 00:10:37.410
Okay.

372
00:10:37.930 --> 00:10:38.890
So, here it is telling me.

373
00:10:39.090 --> 00:10:42.230
That your duplicate key cannot come.

374
00:10:42.970 --> 00:10:45.930
That's why you have to run this query

375
00:10:45.930 --> 00:10:46.390
again.

376
00:10:47.730 --> 00:10:48.670
So, look here.

377
00:10:48.790 --> 00:10:49.330
Cross has come.

378
00:10:49.710 --> 00:10:51.950
So, in the same way, you can add

379
00:10:51.950 --> 00:10:54.850
your constraints by using alter.

380
00:10:54.990 --> 00:10:58.110
So, I will show you the SQL script.

381
00:10:58.110 --> 00:11:00.770
Where did it go?

382
00:11:00.770 --> 00:11:02.530
The alter SQL script.

383
00:11:02.610 --> 00:11:05.870
Here is our alter table script.

384
00:11:06.210 --> 00:11:09.090
And the script that I told you a

385
00:11:09.090 --> 00:11:09.750
little while ago.

386
00:11:09.990 --> 00:11:10.690
You will get it in the handbook.

387
00:11:11.410 --> 00:11:12.470
Along with that, I will add this in

388
00:11:12.470 --> 00:11:13.070
the handbook.

389
00:11:14.450 --> 00:11:15.650
So, you will get that as well.

390
00:11:16.030 --> 00:11:17.110
I hope you are enjoying it.

391
00:11:17.530 --> 00:11:20.070
You tell me how you are enjoying it.

392
00:11:20.090 --> 00:11:21.630
I will be very happy to hear that

393
00:11:21.630 --> 00:11:22.570
you are enjoying this course.

394
00:11:23.170 --> 00:11:23.770
So far.

395
00:11:23.990 --> 00:11:25.250
See you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:02.180
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will talk about primary

2
00:00:02.180 --> 00:00:03.520
key and auto-increment key.

3
00:00:03.820 --> 00:00:05.300
What I will do here is, first of

4
00:00:05.300 --> 00:00:06.500
all, I will drop the table.

5
00:00:06.620 --> 00:00:07.460
Which table I will drop?

6
00:00:08.380 --> 00:00:11.820
Drop table employees because I will recreate this

7
00:00:11.820 --> 00:00:14.620
employees table again in a different way.

8
00:00:14.940 --> 00:00:15.079
Okay.

9
00:00:15.840 --> 00:00:16.560
I will recreate it in a completely different

10
00:00:16.560 --> 00:00:17.000
way.

11
00:00:18.400 --> 00:00:20.880
And the way I will recreate it, I

12
00:00:20.880 --> 00:00:22.860
will copy it and paste it here.

13
00:00:22.980 --> 00:00:24.300
And I am basically saying that my employee

14
00:00:24.300 --> 00:00:26.800
id is an integer, primary key, auto-increment.

15
00:00:27.280 --> 00:00:28.840
So, you know what an integer is.

16
00:00:28.840 --> 00:00:29.480
It has a type.

17
00:00:29.900 --> 00:00:31.980
But, as I say here that it is

18
00:00:31.980 --> 00:00:33.420
a primary key and it will be auto

19
00:00:33.420 --> 00:00:33.760
-increment.

20
00:00:34.460 --> 00:00:35.020
So, what will happen?

21
00:00:35.280 --> 00:00:36.820
Automatically, I can just put email and name

22
00:00:36.820 --> 00:00:39.620
and insert data in it.

23
00:00:40.640 --> 00:00:43.180
And this part will be automatically taken care

24
00:00:43.180 --> 00:00:43.460
of.

25
00:00:43.800 --> 00:00:43.900
Okay.

26
00:00:44.180 --> 00:00:45.500
So, let's run it first so that it

27
00:00:45.500 --> 00:00:45.740
becomes a table.

28
00:00:46.000 --> 00:00:46.880
Employees table has been created.

29
00:00:47.040 --> 00:00:47.780
Refresh it and see.

30
00:00:48.120 --> 00:00:48.580
It has been created.

31
00:00:49.440 --> 00:00:51.080
And now what I will do here is,

32
00:00:51.080 --> 00:00:52.200
I will insert data in it.

33
00:00:52.500 --> 00:00:53.760
And it is very easy to insert data.

34
00:00:53.760 --> 00:00:55.140
For that, I will copy and paste because

35
00:00:55.140 --> 00:00:56.260
I want to save time.

36
00:00:56.460 --> 00:00:57.500
The more time is left, the better.

37
00:00:57.500 --> 00:00:59.660
Here you see, I insert Amit at company

38
00:00:59.660 --> 00:01:00.580
.com and Amit Sharma.

39
00:01:01.500 --> 00:01:02.180
I will run it.

40
00:01:02.380 --> 00:01:03.180
Amit Bhai has been inserted.

41
00:01:03.660 --> 00:01:03.800
Okay.

42
00:01:04.900 --> 00:01:06.480
Now what I will do here is, I

43
00:01:06.480 --> 00:01:06.980
will insert Shubham Bhai.

44
00:01:08.300 --> 00:01:08.960
I will insert Shubham Bhai.

45
00:01:10.420 --> 00:01:11.440
Shubham Sharma.

46
00:01:12.320 --> 00:01:14.820
And after this, Shubham Bhai.

47
00:01:16.420 --> 00:01:18.080
Let's also insert Shubham Bhai's brother.

48
00:01:19.600 --> 00:01:21.760
His name is Hrithik.

49
00:01:21.760 --> 00:01:27.880
And his name is Hrithu Sharma.

50
00:01:28.040 --> 00:01:29.320
Means he is called Hrithu in love.

51
00:01:29.700 --> 00:01:30.800
By the way, his name is Hrithik.

52
00:01:31.300 --> 00:01:31.980
But he is called Hrithu.

53
00:01:33.380 --> 00:01:36.540
So here you can see, Hrithik at company

54
00:01:36.540 --> 00:01:37.140
.com.

55
00:01:37.920 --> 00:01:38.740
Hrithu Sharma.

56
00:01:38.880 --> 00:01:39.000
Okay.

57
00:01:39.160 --> 00:01:41.940
Now what we will do is, select star

58
00:01:41.940 --> 00:01:44.140
from employees.

59
00:01:45.200 --> 00:01:45.720
Okay.

60
00:01:45.820 --> 00:01:48.580
Here you can see, Amit, Shubham, Hrithik.

61
00:01:48.680 --> 00:01:49.080
All three have come.

62
00:01:49.080 --> 00:01:50.200
But I didn't insert 1, 2, 3.

63
00:01:50.920 --> 00:01:51.480
How did it come?

64
00:01:51.900 --> 00:01:55.820
And this is what primary key auto-increment

65
00:01:55.820 --> 00:01:55.920
does.

66
00:01:56.260 --> 00:01:59.540
Basically, when we say that employee id is

67
00:01:59.540 --> 00:02:01.040
an integer, primary key auto-increment.

68
00:02:01.420 --> 00:02:03.080
So what happens is, primary key means that

69
00:02:03.080 --> 00:02:05.800
it will uniquely identify the record in the

70
00:02:05.800 --> 00:02:06.000
table.

71
00:02:06.120 --> 00:02:06.840
Means you can't duplicate.

72
00:02:07.380 --> 00:02:10.580
Means once this employee id becomes 1.

73
00:02:11.580 --> 00:02:13.380
No other record's employee id can be 1

74
00:02:13.380 --> 00:02:13.500
again.

75
00:02:14.080 --> 00:02:14.440
This is the first thing.

76
00:02:15.340 --> 00:02:19.020
Second thing, whenever you search with this, it

77
00:02:19.020 --> 00:02:19.760
will be a very fast search.

78
00:02:20.240 --> 00:02:20.380
Okay.

79
00:02:21.540 --> 00:02:22.600
After that, let me tell you one more

80
00:02:22.600 --> 00:02:23.200
thing.

81
00:02:23.740 --> 00:02:25.280
You don't need to put this again and

82
00:02:25.280 --> 00:02:25.380
again.

83
00:02:25.920 --> 00:02:28.820
Automatically, this thing, employee id will be populated

84
00:02:28.820 --> 00:02:30.160
when you insert email and name.

85
00:02:30.980 --> 00:02:31.900
Like we saw through this query.

86
00:02:33.040 --> 00:02:33.600
Okay.

87
00:02:34.180 --> 00:02:36.340
Here automatically, MySQL assigned employee id 1.

88
00:02:37.580 --> 00:02:39.420
So all these things happen automatically.

89
00:02:40.160 --> 00:02:42.940
A table can only have one primary key.

90
00:02:42.940 --> 00:02:44.360
Now if you say that I make email

91
00:02:44.360 --> 00:02:45.020
also as primary key.

92
00:02:46.060 --> 00:02:47.380
I make email also as primary key.

93
00:02:47.380 --> 00:02:47.640
What is the problem?

94
00:02:48.040 --> 00:02:50.100
You are saying alter table employees add primary

95
00:02:50.100 --> 00:02:50.620
key email.

96
00:02:51.200 --> 00:02:52.340
You can't do this.

97
00:02:52.720 --> 00:02:54.640
Multiple primary key defined error has come to

98
00:02:54.640 --> 00:02:54.840
you.

99
00:02:55.220 --> 00:02:57.260
And error code is also telling you 1068.

100
00:02:57.420 --> 00:02:58.400
So you can't do this thing.

101
00:02:58.700 --> 00:02:58.820
Okay.

102
00:02:59.600 --> 00:03:02.620
So here MySQL shows you the error properly.

103
00:03:03.360 --> 00:03:05.780
Whenever you try to do something that is

104
00:03:05.780 --> 00:03:06.100
not allowed.

105
00:03:06.880 --> 00:03:09.460
Now here emp underscore id is already of

106
00:03:09.460 --> 00:03:10.200
your primary key.

107
00:03:10.360 --> 00:03:12.040
So you can't do this.

108
00:03:12.040 --> 00:03:13.840
You can't make email as primary key.

109
00:03:15.140 --> 00:03:16.440
So why is primary key important?

110
00:03:17.140 --> 00:03:18.320
One is that rows become unique.

111
00:03:19.000 --> 00:03:20.700
That means you have at least one thing

112
00:03:20.700 --> 00:03:22.740
that can uniquely identify the row.

113
00:03:23.680 --> 00:03:24.380
Searching becomes fast.

114
00:03:24.800 --> 00:03:26.340
Like I told you that whenever you run

115
00:03:26.340 --> 00:03:28.220
select query with primary key, it becomes fast.

116
00:03:29.360 --> 00:03:30.040
Then after this, it is very important for

117
00:03:30.040 --> 00:03:30.860
table relationships.

118
00:03:31.680 --> 00:03:33.120
I will tell you what the meaning of

119
00:03:33.120 --> 00:03:33.740
relationships is.

120
00:03:34.520 --> 00:03:35.940
I hope you are enjoying this course.

121
00:03:36.280 --> 00:03:37.020
Tell me whether you are enjoying it or

122
00:03:37.020 --> 00:03:37.280
not.

123
00:03:38.060 --> 00:03:38.620
Tag me on Instagram.

124
00:03:39.340 --> 00:03:40.420
Tag me on Twitter.

125
00:03:40.420 --> 00:03:41.840
Tag me anywhere and tell me that you

126
00:03:41.840 --> 00:03:43.360
are watching this course and you are enjoying

127
00:03:43.360 --> 00:03:43.520
it.

128
00:03:43.620 --> 00:03:44.480
I will feel very good.

129
00:03:44.840 --> 00:03:46.300
Thank you so much guys for watching this

130
00:03:46.300 --> 00:03:46.620
video.

131
00:03:46.880 --> 00:03:48.020
And I will see you in the next

132
00:03:48.020 --> 00:03:48.280
one.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.260 --> 00:00:01.900
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Let us assume you are making a blog

2
00:00:01.900 --> 00:00:04.220
and you have to show the first 10

3
00:00:04.220 --> 00:00:05.480
blogs in it.

4
00:00:05.820 --> 00:00:06.960
You must have seen this in many places

5
00:00:06.960 --> 00:00:08.920
where you are shown the first 10 blogs.

6
00:00:09.660 --> 00:00:11.760
For example, if I just search for blogs,

7
00:00:12.260 --> 00:00:13.200
then I may get a blog.

8
00:00:13.520 --> 00:00:15.120
Maybe I get someone's blog where I can

9
00:00:15.120 --> 00:00:15.580
see the pagination.

10
00:00:16.540 --> 00:00:18.080
And then I can show you what pagination

11
00:00:18.080 --> 00:00:18.460
is.

12
00:00:19.740 --> 00:00:21.900
I just want to show you what pagination

13
00:00:21.900 --> 00:00:22.640
is, see this.

14
00:00:23.060 --> 00:00:24.760
Here you can see this next, by clicking

15
00:00:24.760 --> 00:00:25.540
here, next came.

16
00:00:25.700 --> 00:00:28.060
Then if I click again, next will come

17
00:00:28.060 --> 00:00:28.160
again.

18
00:00:28.160 --> 00:00:29.940
I basically want to show you a good

19
00:00:29.940 --> 00:00:30.560
example.

20
00:00:31.100 --> 00:00:32.480
As you can see here, this is the

21
00:00:32.480 --> 00:00:32.900
website of Hostinger.

22
00:00:33.800 --> 00:00:35.120
And this is their blog.

23
00:00:35.600 --> 00:00:37.020
And here you can see that we can

24
00:00:37.020 --> 00:00:38.140
see some limited blog posts.

25
00:00:38.960 --> 00:00:40.040
And after that, we will click here next.

26
00:00:41.200 --> 00:00:42.360
Then we will see page number 2.

27
00:00:43.140 --> 00:00:44.380
Then after this, we will click next and

28
00:00:44.380 --> 00:00:45.160
we will see page number 3.

29
00:00:45.920 --> 00:00:47.640
Assume that these people are using MySQL database.

30
00:00:48.160 --> 00:00:49.880
So how did these people implement it in

31
00:00:49.880 --> 00:00:50.280
the backend?

32
00:02:50.140 --> 00:02:54.020
MySQL workbench, you can try it, you will

33
00:02:54.020 --> 00:02:55.300
be fine, you will try it, you will

34
00:02:55.300 --> 00:02:57.580
see, there is no cost to try, right,

35
00:02:57.820 --> 00:02:59.660
you can run it, you can see in

36
00:02:59.660 --> 00:03:02.620
increasing order, very good, okay, but if you

37
00:03:02.620 --> 00:03:04.160
want to see it in decreasing order, then

38
00:03:04.160 --> 00:03:06.740
you will write DESC, and if you run

39
00:03:06.740 --> 00:03:07.360
it, then what will happen, it will come

40
00:03:07.360 --> 00:03:10.100
in decreasing order, very good, so this was

41
00:03:10.100 --> 00:03:12.680
order by, but now what I want to

42
00:03:12.680 --> 00:03:16.460
tell you is Limit Clause, by the way,

43
00:03:16.480 --> 00:03:17.700
you can also do order by date, you

44
00:03:17.700 --> 00:03:20.120
can also do order by delivery date, by

45
00:03:20.120 --> 00:03:21.160
the way, I guess it is already ordered

46
00:03:21.160 --> 00:03:23.020
by delivery date, it is not, it is

47
00:03:23.020 --> 00:03:24.700
not, okay, so let's order by delivery date,

48
00:03:25.220 --> 00:03:26.860
so if I say order by, then I

49
00:03:26.860 --> 00:03:29.840
will write delivery date here, and I will

50
00:03:29.840 --> 00:03:31.320
write DESC, it will be in decreasing order,

51
00:03:31.760 --> 00:03:34.400
you can see, the latest order has come

52
00:03:34.400 --> 00:03:37.620
up, and after that we are getting to

53
00:03:37.620 --> 00:03:40.280
see everything down, very good, by the way,

54
00:03:40.320 --> 00:03:41.580
you can also do order by multiple columns,

55
00:03:42.360 --> 00:03:43.800
suppose you want to do order by delivery

56
00:03:43.800 --> 00:03:46.200
date, and after that, whose delivery date is

57
00:03:46.200 --> 00:03:48.240
same, is anyone's delivery date same, no, no

58
00:03:48.240 --> 00:03:50.080
one's delivery date is same, so let's do

59
00:03:50.080 --> 00:03:52.440
one thing, let's do order by city, suppose

60
00:03:52.440 --> 00:03:55.720
I say order by city, okay, and I

61
00:03:55.720 --> 00:03:57.240
will do order by city, and you see

62
00:03:57.240 --> 00:03:59.800
here, it will be order by city, and

63
00:03:59.800 --> 00:04:01.700
here we have done DESC, so this A,

64
00:04:01.720 --> 00:04:03.440
B, C, D, A has come down, and

65
00:04:03.440 --> 00:04:05.780
S has come up, very good, now Delhi,

66
00:04:05.860 --> 00:04:07.220
Delhi, Delhi are three, okay, city of these

67
00:04:07.220 --> 00:04:09.500
three is Delhi, I want this to be

68
00:04:09.500 --> 00:04:11.320
order by price per unit, so I will

69
00:04:11.320 --> 00:04:15.339
say order by city, DESC, and after that

70
00:04:15.339 --> 00:04:18.420
what you do, you order price per unit

71
00:04:18.420 --> 00:04:23.000
ASC, okay, ASC is by default, you don't

72
00:04:23.000 --> 00:04:24.700
need to write ASC, it will be by

73
00:04:24.700 --> 00:04:27.320
default ASC, you need to write DESC, so

74
00:04:27.320 --> 00:04:29.240
I do one thing, I run it, and

75
00:04:29.240 --> 00:04:30.960
you can see here, where Delhi, Delhi, Delhi

76
00:04:30.960 --> 00:04:32.700
was there, in ascending order, your price per

77
00:04:32.700 --> 00:04:34.720
unit has been sorted, so in this way

78
00:04:34.720 --> 00:04:36.740
you can do sorting from multiple columns also,

79
00:04:36.740 --> 00:04:39.540
okay, use order by clause, you can use

80
00:04:39.540 --> 00:04:42.880
ASC, DESC, ASC is DESC, not DSC, I

81
00:04:42.880 --> 00:04:45.700
am sorry, it is DESC, okay, so yeah,

82
00:04:46.120 --> 00:04:47.900
that was how you can use order by

83
00:04:47.900 --> 00:04:50.460
clause, now I will tell you, if you

84
00:04:50.460 --> 00:04:52.480
want only three rows, it is possible that

85
00:04:52.480 --> 00:04:56.280
your MySQL table is full of millions of

86
00:04:56.280 --> 00:04:58.940
rows, and you don't want millions of rows

87
00:04:58.940 --> 00:05:01.340
data to come to you, so I want

88
00:05:01.340 --> 00:05:04.180
to take top 3 from here, so what

89
00:05:04.180 --> 00:05:09.380
I will do, I will write limit, and

90
00:05:09.380 --> 00:05:11.420
I will write 5, and I will run

91
00:05:11.420 --> 00:05:13.500
this query, so I will get only top

92
00:05:13.500 --> 00:05:17.480
5 results, okay, so yeah, that was how

93
00:05:17.480 --> 00:05:20.100
you can use limit, now after this, there

94
00:05:20.100 --> 00:05:22.140
is a very important thing, which is offset,

95
00:05:22.400 --> 00:05:25.840
I will tell you, what is offset, offset

96
00:05:25.840 --> 00:05:28.020
means that you skip 5, so if I

97
00:05:28.020 --> 00:05:29.780
write limit 5 and offset 5, then it

98
00:05:29.780 --> 00:05:31.980
will skip 5 and show 5, and then

99
00:05:31.980 --> 00:05:33.060
I will tell you how you can implement

100
00:05:33.060 --> 00:05:36.740
this kind of pagination, so what we will

101
00:05:36.740 --> 00:05:39.840
do here, we will select start from orders,

102
00:05:39.920 --> 00:05:42.820
order by city, DESC, price per unit, limit

103
00:05:42.820 --> 00:05:44.900
DESC, so what are the rows we are

104
00:05:44.900 --> 00:05:46.880
getting, you can remember them, Vikram, Kavita, okay,

105
00:05:47.840 --> 00:05:49.920
you can see from top, Ananya, Neha, Rohit,

106
00:05:50.120 --> 00:05:54.580
but if I write here offset 5, then

107
00:05:54.580 --> 00:05:56.080
the first 5 will get skipped, and the

108
00:05:56.080 --> 00:05:57.720
next 5 will come, you can see here,

109
00:05:58.640 --> 00:06:00.060
the name has been changed, this is not

110
00:06:00.060 --> 00:06:01.420
the name that you saw a while ago,

111
00:06:01.760 --> 00:06:04.340
because we have skipped the first 5, and

112
00:06:04.340 --> 00:06:07.380
we said limit 5, means show 5, but

113
00:06:07.380 --> 00:06:10.220
also skip 5, offset 5, so that was

114
00:06:10.220 --> 00:06:14.120
how you can implement pagination using MySQL, so

115
00:06:14.120 --> 00:06:16.540
let's say I have 100,000 blocks, yeah,

116
00:06:16.720 --> 00:06:19.940
I have 100,000 block posts, I will

117
00:06:19.940 --> 00:06:22.740
go to one page, I will count and

118
00:06:22.740 --> 00:06:23.660
tell you how many are there, they have

119
00:06:23.660 --> 00:06:25.600
shown 10 posts on one page, there are

120
00:06:25.600 --> 00:06:26.880
10 posts on one page, in which the

121
00:06:26.880 --> 00:06:29.660
topmost post looks like this, and the remaining

122
00:06:29.660 --> 00:06:31.960
9 posts look like this, so what query

123
00:06:31.960 --> 00:06:33.460
will I run, I will say select start

124
00:06:33.460 --> 00:06:36.000
from posts, suppose I have all the posts

125
00:06:36.000 --> 00:06:39.700
in my post table, I will say order

126
00:06:39.700 --> 00:06:41.360
by whatever I want to order by, let's

127
00:06:41.360 --> 00:06:42.040
say I want to do order by order

128
00:06:42.040 --> 00:06:45.620
id, blog id, let's say we have blog

129
00:06:45.620 --> 00:06:47.440
id in our table, then I will write

130
00:06:47.440 --> 00:06:49.800
limit 10, offset 10, so in the beginning

131
00:06:49.800 --> 00:06:51.220
I will do offset 0, so I will

132
00:06:51.220 --> 00:06:52.680
get 10 in the beginning, then I will

133
00:06:52.680 --> 00:06:53.760
do offset 10, I will get the next

134
00:06:53.760 --> 00:06:55.640
10, then I will do offset 20, I

135
00:06:55.640 --> 00:06:57.340
will get the next 10, then I will

136
00:06:57.340 --> 00:07:00.000
do offset 30, I will get the next

137
00:07:00.000 --> 00:07:02.700
10, and so on, so I will make

138
00:07:02.700 --> 00:07:04.140
my own function here, I will make an

139
00:07:04.140 --> 00:07:07.640
expression which I can use, and I can

140
00:07:07.640 --> 00:07:10.060
implement this type of pagination, I will get

141
00:07:10.060 --> 00:07:12.060
to see the data page by page, I

142
00:07:12.060 --> 00:07:13.560
hope that was easy, I hope you are

143
00:07:13.560 --> 00:07:16.120
understanding, I hope you are enjoying, thank you

144
00:07:16.120 --> 00:07:17.960
so much guys for watching this video, and

145
00:07:17.960 --> 00:07:19.260
I will see you in the next one.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:01.730
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to talk

2
00:00:01.730 --> 00:00:02.490
about functions.

3
00:00:02.770 --> 00:00:04.030
What are functions in SQL?

4
00:00:04.470 --> 00:00:07.010
If you have seen functions in Python or

5
00:00:07.010 --> 00:00:10.270
C language or if you have seen functions

6
00:00:10.270 --> 00:00:14.110
in any other programming language then somewhere functions

7
00:00:14.110 --> 00:00:15.830
are the same even in MySQL.

8
00:00:16.470 --> 00:00:17.770
I will click on File and open a

9
00:00:17.770 --> 00:00:19.310
new query tab so that I can write

10
00:00:19.310 --> 00:00:19.810
my queries.

11
00:00:20.550 --> 00:00:22.470
And here I will run select star from

12
00:00:22.470 --> 00:00:23.050
orders.

13
00:00:24.050 --> 00:00:25.190
But one thing you have to keep in

14
00:00:25.190 --> 00:00:25.290
mind.

15
00:00:25.290 --> 00:00:27.650
You have to write use ecom whatever is

16
00:00:27.650 --> 00:00:28.250
the name of your database.

17
00:00:30.890 --> 00:00:32.070
Otherwise it will be a problem.

18
00:00:32.370 --> 00:00:33.490
Now you see this database is being used

19
00:00:33.490 --> 00:00:34.550
and this is our data.

20
00:00:34.790 --> 00:00:37.310
Now I will tell you what is a

21
00:00:37.310 --> 00:00:37.410
function.

22
00:00:37.450 --> 00:00:41.230
Functions are built-in operations that perform calculations

23
00:00:41.230 --> 00:00:43.070
and transformations on data.

24
00:00:43.970 --> 00:00:45.710
These are commonly used for select queries.

25
00:00:46.730 --> 00:00:48.090
Now you will ask what is this?

26
00:00:48.410 --> 00:00:50.370
We will talk about some aggregate functions.

27
00:00:50.370 --> 00:00:52.730
These functions work on multiple rows and give

28
00:00:52.730 --> 00:00:53.810
a single value.

29
00:00:54.110 --> 00:00:55.890
For example, I want to know how many

30
00:00:55.890 --> 00:00:56.370
orders are there.

31
00:00:56.470 --> 00:00:57.950
So I will select count star from orders.

32
00:00:58.390 --> 00:00:59.410
And what will happen if I do this?

33
00:01:00.030 --> 00:01:02.670
I will get to see count of orders.

34
00:01:02.730 --> 00:01:05.130
So if I run this, I get to

35
00:01:05.130 --> 00:01:06.170
know that there are 12 orders.

36
00:01:06.550 --> 00:01:07.070
Very good.

37
00:01:07.270 --> 00:01:09.310
This was a very basic query.

38
00:01:10.090 --> 00:01:14.390
And I found out how many rows are

39
00:01:14.390 --> 00:01:15.690
there in my orders table.

40
00:01:15.690 --> 00:01:18.590
After this, what can we do?

41
00:01:19.050 --> 00:01:20.710
We can sum anything.

42
00:01:21.110 --> 00:01:23.810
For example, I want to sum quantity multiplied

43
00:01:23.810 --> 00:01:24.710
by price per unit.

44
00:01:24.990 --> 00:01:27.410
So I can say multiply quantity by price

45
00:01:27.410 --> 00:01:27.890
per unit.

46
00:01:28.390 --> 00:01:29.390
And sum it.

47
00:01:29.770 --> 00:01:32.130
Then bring that sum in a new column

48
00:01:32.130 --> 00:01:33.710
called total revenue.

49
00:01:33.810 --> 00:01:34.690
This is the meaning of this line.

50
00:01:35.350 --> 00:01:41.690
When we say select some quantity star price

51
00:01:41.690 --> 00:01:44.330
per unit as total revenue from orders, we

52
00:01:44.330 --> 00:01:46.970
are saying that first multiply quantity by price

53
00:01:46.970 --> 00:01:49.150
per unit and then sum all the values.

54
00:01:49.750 --> 00:01:51.870
And then show it in a total revenue

55
00:01:51.870 --> 00:01:52.430
column.

56
00:01:53.770 --> 00:01:55.990
So what I will do here I will

57
00:01:55.990 --> 00:01:57.650
run it like this.

58
00:01:57.670 --> 00:01:59.230
I will bring it down.

59
00:01:59.810 --> 00:02:01.670
If I run it, you can see that

60
00:02:01.670 --> 00:02:03.670
it is 145,200.

61
00:02:04.470 --> 00:02:05.930
What is this 145,200?

62
00:02:07.090 --> 00:02:10.550
If I do select star from orders and

63
00:02:10.550 --> 00:02:11.650
run it, I will get everything.

64
00:02:11.970 --> 00:02:13.990
So basically, this is multiplied by this and

65
00:02:13.990 --> 00:02:14.610
some value will come.

66
00:02:15.090 --> 00:02:16.450
This is multiplied by this and some value

67
00:02:16.450 --> 00:02:16.650
will come.

68
00:02:16.870 --> 00:02:18.390
This is multiplied by this and some value

69
00:02:18.390 --> 00:02:18.510
will come.

70
00:02:19.950 --> 00:02:22.010
And then the values that will come, sum

71
00:02:22.010 --> 00:02:25.290
them all The number we saw was 145

72
00:02:25.290 --> 00:02:25.710
,200.

73
00:02:26.730 --> 00:02:28.330
Then we will get that order, which will

74
00:02:28.330 --> 00:02:28.970
be total revenue.

75
00:02:29.210 --> 00:02:30.390
So basically what we are doing, we are

76
00:02:30.390 --> 00:02:32.070
saying how much money we have earned.

77
00:02:32.210 --> 00:02:33.830
How much money our company has earned.

78
00:02:33.830 --> 00:02:36.930
Like you see here, 65,000 x 1

79
00:02:36.930 --> 00:02:41.190
Then 2500 x 2 Then 12,000 x

80
00:02:41.190 --> 00:02:43.150
1 Then 80 x 10.

81
00:02:43.250 --> 00:02:44.730
Now you can say that this order got

82
00:02:44.730 --> 00:02:45.810
cancelled, why did you add it?

83
00:02:46.530 --> 00:02:48.690
Okay, we can add it, we will minus

84
00:02:48.690 --> 00:02:48.790
it later.

85
00:02:49.530 --> 00:02:52.190
Let's assume that the payment is done.

86
00:02:52.390 --> 00:02:53.450
Payment mode UPI has come.

87
00:02:53.950 --> 00:02:55.590
Arjun Mehta made the payment, got it cancelled

88
00:02:55.590 --> 00:02:55.690
later.

89
00:02:55.730 --> 00:03:00.290
So assume something like this and multiply both

90
00:03:00.290 --> 00:03:02.810
of them Sum it, this is basically what

91
00:03:02.810 --> 00:03:03.430
a query says.

92
00:03:04.310 --> 00:03:05.370
Now let's talk about the average.

93
00:03:05.550 --> 00:03:06.190
Assume that I have to find the average

94
00:03:06.190 --> 00:03:07.670
of price per unit.

95
00:03:08.970 --> 00:03:09.590
I have to find the average of this

96
00:03:09.590 --> 00:03:09.950
column.

97
00:03:13.410 --> 00:03:15.590
I will do one thing, I will take

98
00:03:15.590 --> 00:03:16.650
a screenshot of this.

99
00:03:16.650 --> 00:03:20.950
Windows, Shift and S I pressed this combination.

100
00:03:21.850 --> 00:03:23.550
Now some people may not be able to

101
00:03:23.550 --> 00:03:23.650
do this.

102
00:03:23.650 --> 00:03:24.930
I am telling you in advance that you

103
00:03:24.930 --> 00:03:25.830
may not be able to do this.

104
00:03:26.370 --> 00:03:28.150
Here is my screenshot.

105
00:03:29.310 --> 00:03:30.290
So at least I will be able to

106
00:03:30.290 --> 00:03:30.690
see all the data.

107
00:03:31.950 --> 00:03:33.650
So what I will do now is that

108
00:03:33.650 --> 00:03:34.870
I will copy this.

109
00:03:35.170 --> 00:03:37.870
Copy it and paste it here.

110
00:03:38.130 --> 00:03:40.570
So here I am getting 11440.

111
00:03:40.670 --> 00:03:41.050
What is this?

112
00:03:41.310 --> 00:03:42.930
This is the average of all these values.

113
00:03:43.110 --> 00:03:43.750
This is the average of price per unit

114
00:03:43.750 --> 00:03:44.770
values.

115
00:03:46.270 --> 00:03:49.110
So if you sum all this and divide

116
00:03:49.110 --> 00:03:50.550
it by 12, then this value will come.

117
00:03:50.910 --> 00:03:52.650
So you can find the average here.

118
00:03:52.650 --> 00:03:56.790
So if I say average as avg orders

119
00:03:57.870 --> 00:03:59.650
I want to keep a name of this

120
00:03:59.650 --> 00:03:59.970
column.

121
00:04:00.650 --> 00:04:02.410
So if I run it here, its name

122
00:04:02.410 --> 00:04:03.550
will come avg orders.

123
00:04:04.090 --> 00:04:07.070
So here our average will be returned as

124
00:04:07.070 --> 00:04:08.450
avg orders.

125
00:04:09.090 --> 00:04:09.870
Very good.

126
00:04:10.010 --> 00:04:11.790
Now what we will do is that if

127
00:04:11.790 --> 00:04:12.810
I want to find the minimum and maximum

128
00:04:13.450 --> 00:04:15.370
what is the price per unit, then I

129
00:04:15.370 --> 00:04:18.089
can find both minimum and maximum by running

130
00:04:18.089 --> 00:04:18.529
this query.

131
00:04:18.529 --> 00:04:21.070
So I will say here select min price

132
00:04:21.070 --> 00:04:23.530
per unit max price per unit from orders.

133
00:04:23.710 --> 00:04:24.710
So I will do this and I will

134
00:04:24.710 --> 00:04:26.350
get minimum and maximum.

135
00:04:26.890 --> 00:04:29.150
So if I want to get this as

136
00:04:29.150 --> 00:04:32.310
min underscore price and I want to get

137
00:04:32.310 --> 00:04:35.670
this as max underscore price So I have

138
00:04:35.670 --> 00:04:36.290
given the names of these columns.

139
00:04:37.010 --> 00:04:38.510
Now if I run this, the names of

140
00:04:38.510 --> 00:04:40.630
my columns will be min underscore price and

141
00:04:40.630 --> 00:04:41.570
max underscore price.

142
00:04:42.290 --> 00:04:43.430
Now look at the price per unit.

143
00:04:43.430 --> 00:04:45.410
In this column, my minimum price is 80

144
00:04:45.410 --> 00:04:48.570
and maximum price is 65,000.

145
00:04:48.770 --> 00:04:49.750
As you can see.

146
00:04:50.730 --> 00:04:53.510
In this column, the minimum value is 80

147
00:04:53.510 --> 00:04:56.150
and maximum value is 65,000.

148
00:04:57.030 --> 00:04:57.610
So we are getting this value.

149
00:04:59.550 --> 00:05:01.450
After this, we have scalar functions.

150
00:05:01.930 --> 00:05:03.510
These work on individual rows.

151
00:05:04.410 --> 00:05:05.590
For example, if I want to round the

152
00:05:05.590 --> 00:05:07.230
price per unit then I can use the

153
00:05:07.230 --> 00:05:07.770
round function.

154
00:05:07.770 --> 00:05:11.050
So here you see my price per unit

155
00:05:11.050 --> 00:05:15.510
is 0.00000 But I want to get

156
00:05:15.510 --> 00:05:17.850
a value after which there is no point.

157
00:05:18.110 --> 00:05:19.610
Basically, I am saying that there are 0

158
00:05:19.610 --> 00:05:20.070
decimals.

159
00:05:20.450 --> 00:05:24.910
I can also say here that select customer

160
00:05:24.910 --> 00:05:27.110
name and I can do something like this

161
00:05:27.110 --> 00:05:32.090
as n and round price per unit as

162
00:05:32.090 --> 00:05:33.630
p means you can put any name.

163
00:05:33.630 --> 00:05:35.950
I have put p and n here.

164
00:05:35.990 --> 00:05:36.730
Just to show you.

165
00:05:37.030 --> 00:05:40.850
You can change the name of columns by

166
00:05:40.850 --> 00:05:41.170
using as.

167
00:05:42.610 --> 00:05:44.390
We have already seen this a while ago.

168
00:05:45.130 --> 00:05:45.590
But again, you can change it by putting

169
00:05:45.590 --> 00:05:46.390
as in individual columns.

170
00:05:48.590 --> 00:05:50.070
Now what does upper and lower do?

171
00:05:50.230 --> 00:05:51.230
It converts to uppercase and lowercase.

172
00:05:51.890 --> 00:05:54.650
If you do upper customer name, then you

173
00:05:54.650 --> 00:05:56.210
will see the customer name in uppercase and

174
00:05:56.210 --> 00:05:57.270
the lower one will be seen in lowercase.

175
00:05:58.390 --> 00:05:58.970
So if you want to do something in

176
00:05:58.970 --> 00:06:03.850
lowercase, then lower function and if you want

177
00:06:03.850 --> 00:06:05.570
to do something in uppercase, then upper function.

178
00:06:05.730 --> 00:06:06.110
So you can do this.

179
00:06:06.990 --> 00:06:08.770
If you want to know the number of

180
00:06:08.770 --> 00:06:11.870
characters in a string then you can use

181
00:06:11.870 --> 00:06:13.150
length function.

182
00:06:14.570 --> 00:06:18.170
And as you can see here length customer

183
00:06:18.170 --> 00:06:20.110
name you will get to see something like

184
00:06:20.110 --> 00:06:20.210
this.

185
00:06:21.090 --> 00:06:23.210
So yeah, that was about some of the

186
00:06:23.210 --> 00:06:24.010
scalar functions.

187
00:06:24.010 --> 00:06:26.210
After this, we have some date functions.

188
00:06:26.570 --> 00:06:29.350
Like we have current date and current time.

189
00:06:29.970 --> 00:06:32.370
So if I just run current underscore date

190
00:06:32.370 --> 00:06:34.770
then what will happen?

191
00:06:35.110 --> 00:06:41.050
If I run current underscore time then I

192
00:06:41.050 --> 00:06:41.970
will get current time.

193
00:06:43.430 --> 00:06:46.670
So time and date you will get to

194
00:06:46.670 --> 00:06:46.770
know.

195
00:06:47.090 --> 00:06:49.430
Now we have to find the difference of

196
00:06:49.430 --> 00:06:49.530
date.

197
00:06:49.530 --> 00:06:51.790
How will you find it?

198
00:06:52.110 --> 00:06:54.710
Suppose you have two dates and you want

199
00:06:54.710 --> 00:06:57.610
to find how many days have passed since

200
00:06:57.610 --> 00:06:57.970
that date.

201
00:06:58.690 --> 00:07:00.090
So here we are saying delivery date and

202
00:07:00.090 --> 00:07:02.610
order date what is the difference?

203
00:07:04.010 --> 00:07:05.590
That will be our delivery date.

204
00:07:08.110 --> 00:07:15.710
Suppose Amish Sharma ordered on 5th and then

205
00:07:16.550 --> 00:07:22.750
he got the delivery on 8th so what

206
00:07:22.750 --> 00:07:23.070
will happen?

207
00:07:23.330 --> 00:07:26.230
His delivery time was delivered in 3 days.

208
00:07:27.050 --> 00:07:28.550
So let's calculate it.

209
00:07:28.970 --> 00:07:30.990
Who got the worst delivery?

210
00:07:31.850 --> 00:07:34.130
No, 3 got it in 8 days.

211
00:07:34.790 --> 00:07:37.330
So we will say apologies Rahul Khan.

212
00:07:39.010 --> 00:07:41.050
Your office chair has reached late in Delhi.

213
00:07:43.270 --> 00:07:49.250
I hope you understood how this thing works.

214
00:07:49.570 --> 00:07:54.550
Now we will see how to use where

215
00:07:54.550 --> 00:07:54.650
with functions.

216
00:07:55.410 --> 00:07:59.110
Suppose we want order date to be 2025

217
00:07:59.110 --> 00:08:00.470
which is the year of order date.

218
00:08:02.410 --> 00:08:05.670
Basically we are saying show us 2025 orders.

219
00:08:06.670 --> 00:08:10.950
Select start from order where the year of

220
00:08:10.950 --> 00:08:12.710
order date is equal to 2025.

221
00:08:15.670 --> 00:08:20.010
If we want to see 2026 then there

222
00:08:20.010 --> 00:08:20.110
is none.

223
00:08:22.410 --> 00:08:25.430
So this was functions in MySQL.

224
00:08:25.590 --> 00:08:27.070
I hope you enjoyed it.

225
00:08:27.190 --> 00:08:29.950
I hope you will try your personal combinations

226
00:08:30.670 --> 00:08:34.150
and make it more useful for your specific

227
00:08:34.150 --> 00:08:34.789
use case.

228
00:08:35.110 --> 00:08:37.049
Thank you so much for watching this video

229
00:08:37.049 --> 00:08:38.630
and I will see you in the next

230
00:08:38.630 --> 00:08:38.890
one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:02.180
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Guys, we have already seen how logical operators

2
00:00:02.180 --> 00:00:03.760
work in MySQL.

3
00:00:04.520 --> 00:00:07.320
Today, we will see how to use IN,

4
00:00:07.620 --> 00:00:09.720
NOT IN, BETWEEN and NOT BETWEEN.

5
00:00:10.500 --> 00:00:11.940
So, the first thing I am going to

6
00:00:11.940 --> 00:00:14.380
do is to select start from orders.

7
00:00:14.600 --> 00:00:16.260
Yes, a very basic query.

8
00:00:16.620 --> 00:00:17.500
What is there in my orders table?

9
00:00:18.220 --> 00:00:19.140
In some way, you can see the view

10
00:00:19.140 --> 00:00:21.800
of my orders table as you can see.

11
00:00:22.380 --> 00:00:24.660
There are so many columns in this table.

12
00:00:24.920 --> 00:00:25.840
Data is populated.

13
00:00:26.300 --> 00:00:28.160
Let's see how we use IN.

14
00:00:28.160 --> 00:00:29.860
See, I have already told you the basic

15
00:00:29.860 --> 00:00:30.320
conditions.

16
00:00:31.400 --> 00:00:33.400
Where you used to say something like this.

17
00:00:33.400 --> 00:00:36.980
Select start from orders where quantity is greater

18
00:00:36.980 --> 00:00:37.480
than 2.

19
00:00:37.700 --> 00:00:39.160
Quantity is less than or equal to 3.

20
00:00:39.700 --> 00:00:40.220
We have done all these things.

21
00:00:41.280 --> 00:00:42.940
But today's video is a little different.

22
00:00:43.140 --> 00:00:45.880
Because we will use IN, NOT IN, these

23
00:00:45.880 --> 00:00:46.900
kinds of logical operators.

24
00:00:47.580 --> 00:00:48.940
So, how to use IN?

25
00:00:49.300 --> 00:00:51.620
Suppose, I want to get only those orders

26
00:00:51.620 --> 00:00:53.980
where the city is either Delhi or Mumbai

27
00:00:53.980 --> 00:00:55.200
or Bangalore.

28
00:00:55.380 --> 00:00:56.640
So, I can use this query.

29
00:00:56.640 --> 00:00:58.660
And I can run this query.

30
00:00:59.220 --> 00:01:00.760
So, I will keep this query here and

31
00:01:00.760 --> 00:01:01.140
run it.

32
00:01:01.180 --> 00:01:03.319
And you see, only those cities have come

33
00:01:03.319 --> 00:01:04.519
here which are present in this list.

34
00:01:05.140 --> 00:01:06.960
So, you can give a list like this.

35
00:01:07.100 --> 00:01:09.840
And you can say, select start from orders

36
00:01:09.840 --> 00:01:13.500
where city is in Delhi, Mumbai or Bangalore.

37
00:01:13.780 --> 00:01:16.340
Along with this, you can use NOT IN.

38
00:01:17.360 --> 00:01:21.000
Suppose, I want to get those cities, sorry,

39
00:01:21.100 --> 00:01:23.940
those orders where city is in Delhi, Mumbai

40
00:01:23.940 --> 00:01:24.340
or Bangalore.

41
00:01:24.340 --> 00:01:29.300
So, you see, Ahmedabad, Pune, Hyderabad, Kolkata, Surat,

42
00:01:29.360 --> 00:01:30.500
Chennai have come to you.

43
00:01:30.800 --> 00:01:34.680
So, in this way, you can find out

44
00:01:34.680 --> 00:01:38.120
which are those orders where city is other

45
00:01:38.120 --> 00:01:38.520
than these three.

46
00:01:39.880 --> 00:01:40.820
I hope you have understood.

47
00:01:41.580 --> 00:01:43.440
Then if you want to run a similar

48
00:01:43.440 --> 00:01:45.340
type of query on payment method, you can

49
00:01:45.340 --> 00:01:45.800
do that too.

50
00:01:46.360 --> 00:01:47.860
For that, you will do something like this.

51
00:01:48.040 --> 00:01:50.940
I want debit card, I want credit card,

52
00:01:51.140 --> 00:01:51.920
I don't want cash and reply.

53
00:01:52.980 --> 00:01:54.760
Suppose, you want to take only those transactions

54
00:01:54.760 --> 00:01:57.800
where MDR is applied.

55
00:01:59.020 --> 00:02:00.100
Where charges are applied.

56
00:02:00.340 --> 00:02:02.460
In debit card, charges are applied, in credit

57
00:02:02.460 --> 00:02:03.400
card, charges are applied in many places.

58
00:02:03.980 --> 00:02:05.180
So, suppose you want to take only those

59
00:02:05.180 --> 00:02:08.539
orders where there is some other payment method

60
00:02:08.539 --> 00:02:08.639
other than cash and UPI.

61
00:02:08.720 --> 00:02:10.540
And you can see here, you got all

62
00:02:10.540 --> 00:02:14.340
those orders where payment method is something other

63
00:02:14.340 --> 00:02:15.380
than cash and UPI.

64
00:02:16.220 --> 00:02:16.880
You see, here we got to see all

65
00:02:16.880 --> 00:02:17.980
payment methods like credit card, debit card.

66
00:02:20.720 --> 00:02:22.600
Can we use IN or NOT IN somewhere

67
00:02:22.600 --> 00:02:23.340
else?

68
00:02:23.600 --> 00:02:24.400
You can use it on any column.

69
00:02:25.600 --> 00:02:28.460
But these were some very trivial examples.

70
00:02:29.020 --> 00:02:30.780
Here you see, now we will use between

71
00:02:30.780 --> 00:02:31.600
and not between.

72
00:02:32.580 --> 00:02:35.920
So, between and not between, we primarily use

73
00:02:35.920 --> 00:02:37.020
for numerical values.

74
00:02:37.620 --> 00:02:39.960
Suppose, I want that price per unit is

75
00:02:39.960 --> 00:02:40.940
between 1000 to 10,000.

76
00:02:40.940 --> 00:02:43.960
So, between 1000 to 10,000, if I

77
00:02:43.960 --> 00:02:47.120
want price per unit orders, then I will

78
00:02:47.120 --> 00:02:47.640
run this query.

79
00:02:48.560 --> 00:02:49.740
You see, it will not come 65,000.

80
00:02:50.260 --> 00:02:50.980
We will not get Sharma.

81
00:02:51.360 --> 00:02:52.500
ID number 1 will not come.

82
00:02:53.240 --> 00:02:53.840
I run it.

83
00:02:54.420 --> 00:02:55.700
You see, ID number 1 did not come.

84
00:02:55.840 --> 00:02:56.760
Everything else came.

85
00:02:57.260 --> 00:02:58.420
And where there is a price per unit

86
00:02:58.420 --> 00:03:01.540
between 1000 to 10,000, I got to

87
00:03:01.540 --> 00:03:02.400
see all those rows.

88
00:03:03.980 --> 00:03:04.820
Very good.

89
00:03:05.820 --> 00:03:06.860
We can also use not between.

90
00:03:06.860 --> 00:03:09.000
Like we saw IN and NOT IN.

91
00:03:09.380 --> 00:03:10.400
Between and not between.

92
00:03:10.720 --> 00:03:11.440
What will happen in not between?

93
00:03:11.980 --> 00:03:13.260
You will get to see all those orders

94
00:03:13.260 --> 00:03:16.100
where the price per unit is not between

95
00:03:16.100 --> 00:03:17.320
1000 to 10,000.

96
00:03:20.380 --> 00:03:21.540
Let's run this query.

97
00:03:21.720 --> 00:03:23.560
And you can see here that the price

98
00:03:23.560 --> 00:03:25.260
per unit is not between 1000 to 10

99
00:03:25.260 --> 00:03:25.780
,000.

100
00:03:26.300 --> 00:03:27.760
From 1000, it is small and from 10

101
00:03:27.760 --> 00:03:28.300
,000, it is big.

102
00:03:28.620 --> 00:03:31.740
You can see, we have only those entries.

103
00:03:32.680 --> 00:03:33.560
So, this is a way to use not

104
00:03:33.560 --> 00:03:33.900
between.

105
00:03:34.900 --> 00:03:38.040
After this, we have wildcards.

106
00:03:38.220 --> 00:03:40.520
They are very important for pattern matching.

107
00:03:41.320 --> 00:03:44.260
And with wildcard, you use like.

108
00:03:45.380 --> 00:03:48.920
Assume that I say, select start from orders

109
00:03:48.920 --> 00:03:52.360
where product, like.

110
00:03:53.380 --> 00:03:56.100
And if I use wildcard here, I will

111
00:03:56.100 --> 00:03:56.820
say L.

112
00:03:57.360 --> 00:03:58.360
And I say percent.

113
00:03:59.080 --> 00:04:01.300
Meaning, whatever happens after L, I will be

114
00:04:01.300 --> 00:04:01.400
fine.

115
00:04:01.400 --> 00:04:03.880
So, I will say product, like L percent.

116
00:04:04.560 --> 00:04:05.260
Run it.

117
00:04:05.340 --> 00:04:06.440
You can see, the laptop is here.

118
00:04:07.140 --> 00:04:09.380
Or I can say, city, like D.

119
00:04:10.020 --> 00:04:12.880
And here, if I do something like this.

120
00:04:13.140 --> 00:04:14.260
So, all the Delhi guys are here.

121
00:04:14.560 --> 00:04:16.060
Because after D, it will match any number

122
00:04:16.060 --> 00:04:16.560
of characters.

123
00:04:17.180 --> 00:04:18.540
D percent means, it starts from D.

124
00:04:19.360 --> 00:04:21.320
Now, if I write something like this.

125
00:04:21.500 --> 00:04:21.940
Percent.

126
00:04:22.580 --> 00:04:25.520
And I write here, H.I. So, you

127
00:04:25.520 --> 00:04:26.120
can see here.

128
00:04:26.820 --> 00:04:28.660
It ends with H.I. So, Delhi is

129
00:04:28.660 --> 00:04:28.780
here.

130
00:04:28.780 --> 00:04:29.240
Okay.

131
00:04:29.840 --> 00:04:31.760
Assume, it ends with A.

132
00:04:32.460 --> 00:04:33.600
So, Kolkata is here.

133
00:04:34.100 --> 00:04:35.580
Is it starting with D?

134
00:04:36.920 --> 00:04:38.120
Ahmedabad and Hyderabad.

135
00:04:38.600 --> 00:04:39.340
Okay, if I write bad.

136
00:04:40.100 --> 00:04:40.900
Both will be here.

137
00:04:42.380 --> 00:04:43.780
Ahmedabad and Hyderabad.

138
00:04:44.540 --> 00:04:45.980
Now, if I write Rabad.

139
00:04:47.140 --> 00:04:49.220
So, here I will get only Hyderabad.

140
00:04:49.500 --> 00:04:53.480
Because Rabad ends with Hyderabad.

141
00:04:54.140 --> 00:04:55.540
So, here I am saying, no matter how

142
00:04:55.540 --> 00:04:56.200
many characters there are.

143
00:04:56.260 --> 00:04:57.680
But it should not end with Rabad.

144
00:04:57.680 --> 00:04:58.740
So, in this way.

145
00:04:59.640 --> 00:05:00.580
We can use like.

146
00:05:01.640 --> 00:05:02.200
Very good.

147
00:05:03.340 --> 00:05:05.620
After this, we can use something like this.

148
00:05:06.260 --> 00:05:07.580
Here, basically we are saying.

149
00:05:07.740 --> 00:05:08.840
No matter where the table is.

150
00:05:09.160 --> 00:05:09.620
Assume.

151
00:05:10.520 --> 00:05:11.840
I put this thing in city.

152
00:05:12.600 --> 00:05:13.860
And I do Rab.

153
00:05:14.020 --> 00:05:16.200
After Rab, I say percent.

154
00:05:16.280 --> 00:05:17.880
Percentage means, no matter how many characters.

155
00:05:17.980 --> 00:05:18.960
No matter how many characters are here.

156
00:05:19.000 --> 00:05:19.920
No matter how many characters are here.

157
00:05:19.940 --> 00:05:21.300
But Rab should be in the middle.

158
00:05:22.340 --> 00:05:23.940
If I run, you see here.

159
00:05:24.540 --> 00:05:25.260
Hyderabad is here.

160
00:05:25.920 --> 00:05:26.980
Rab should be here.

161
00:05:27.020 --> 00:05:27.860
So, maybe nothing will come.

162
00:05:28.500 --> 00:05:30.000
If I say only B, then B will

163
00:05:30.000 --> 00:05:30.380
come in a lot of things.

164
00:05:30.800 --> 00:05:31.560
So, almost.

165
00:05:32.440 --> 00:05:34.060
Not all, but a lot came.

166
00:05:34.540 --> 00:05:36.400
Wherever B was in Mumbai, B was there.

167
00:05:36.480 --> 00:05:37.320
Before B, something was there.

168
00:05:37.320 --> 00:05:37.960
After B, something was there.

169
00:05:38.000 --> 00:05:39.020
Means, whatever is here.

170
00:05:39.680 --> 00:05:40.320
Whatever is here.

171
00:05:40.680 --> 00:05:41.540
So, you will get to see.

172
00:05:42.320 --> 00:05:43.440
And even if nothing happens.

173
00:05:43.480 --> 00:05:44.300
Even if I remove it.

174
00:05:44.660 --> 00:05:45.200
Even if I do B percent.

175
00:05:46.440 --> 00:05:48.680
So, here it will have to start with

176
00:05:48.680 --> 00:05:48.780
B.

177
00:05:49.060 --> 00:05:50.360
So, if I run it, then nothing will

178
00:05:50.360 --> 00:05:50.500
come.

179
00:05:50.560 --> 00:05:50.940
You see here.

180
00:05:51.620 --> 00:05:52.420
So, here.

181
00:05:52.420 --> 00:05:53.960
But, something or the other is necessary.

182
00:05:54.100 --> 00:05:55.400
Percent means something or the other is here.

183
00:05:55.900 --> 00:05:56.940
And something or the other after B.

184
00:05:57.700 --> 00:05:58.780
And B is in the middle.

185
00:05:59.000 --> 00:05:59.540
So, you will get to see a lot

186
00:05:59.540 --> 00:05:59.960
of things.

187
00:06:01.180 --> 00:06:02.000
You can see here.

188
00:06:02.660 --> 00:06:03.600
Never run by selecting.

189
00:06:04.180 --> 00:06:05.400
Because when you run by selecting.

190
00:06:05.640 --> 00:06:06.580
Then it runs the selected part.

191
00:06:07.560 --> 00:06:08.120
Which is MySQL.

192
00:06:08.380 --> 00:06:09.760
So, that's why you have to run it

193
00:06:09.760 --> 00:06:09.860
carefully.

194
00:06:10.400 --> 00:06:11.040
And you see here.

195
00:06:11.360 --> 00:06:11.800
Percentage.

196
00:06:12.400 --> 00:06:13.140
You can use it like this.

197
00:06:13.840 --> 00:06:15.220
I would like you guys.

198
00:06:15.520 --> 00:06:16.900
In your MySQL workbench.

199
00:06:17.380 --> 00:06:19.140
Run some of these queries yourself.

200
00:06:19.940 --> 00:06:21.480
Because if you run it yourself.

201
00:06:21.480 --> 00:06:23.460
Then you guys will have a lot of

202
00:06:23.460 --> 00:06:23.820
clarity.

203
00:06:24.520 --> 00:06:25.700
If you guys just watch videos.

204
00:06:26.200 --> 00:06:26.720
Watch the handbook.

205
00:06:27.280 --> 00:06:27.780
Understand the queries.

206
00:06:28.800 --> 00:06:29.940
And just read out.

207
00:06:30.160 --> 00:06:31.000
Will try to learn things.

208
00:06:32.340 --> 00:06:33.300
So, there is a good chance.

209
00:06:33.400 --> 00:06:34.620
That your practise will not be that good.

210
00:06:35.940 --> 00:06:36.860
So, that's why I want.

211
00:06:37.360 --> 00:06:38.840
That you guys practise.

212
00:06:39.060 --> 00:06:39.960
Now, we will see the wild card.

213
00:06:40.420 --> 00:06:41.960
Which matches exactly one character.

214
00:06:42.740 --> 00:06:43.580
This is very important.

215
00:06:43.980 --> 00:06:45.420
And here basically we are saying.

216
00:06:45.880 --> 00:06:47.180
That only one character.

217
00:06:47.420 --> 00:06:48.080
I tell you guys.

218
00:06:48.560 --> 00:06:49.760
If I say city like.

219
00:06:49.760 --> 00:06:51.080
I say it should be D.

220
00:06:52.580 --> 00:06:53.500
Here two characters.

221
00:06:53.620 --> 00:06:54.260
Or I say.

222
00:06:54.420 --> 00:06:55.500
Something should be matching like this.

223
00:06:55.680 --> 00:06:56.780
Here any character comes.

224
00:06:56.840 --> 00:06:57.120
It will work.

225
00:06:57.380 --> 00:06:57.500
Okay.

226
00:06:58.140 --> 00:06:59.060
Here the Delhi one has come.

227
00:06:59.160 --> 00:06:59.580
You can see.

228
00:07:00.100 --> 00:07:01.420
Now, if I say here.

229
00:07:01.600 --> 00:07:02.440
That the name is.

230
00:07:03.220 --> 00:07:04.780
There is something like this.

231
00:07:05.280 --> 00:07:06.160
I say name.

232
00:07:06.420 --> 00:07:07.340
And I say here.

233
00:07:08.520 --> 00:07:10.740
S A R.

234
00:07:11.780 --> 00:07:12.180
Underscore.

235
00:07:12.380 --> 00:07:12.860
Underscore.

236
00:07:13.140 --> 00:07:13.540
L I.

237
00:07:13.840 --> 00:07:14.500
And I run it.

238
00:07:15.540 --> 00:07:16.380
So, here.

239
00:07:16.740 --> 00:07:17.720
I am running it.

240
00:07:17.720 --> 00:07:18.320
Here.

241
00:07:18.480 --> 00:07:18.920
Actually.

242
00:07:19.240 --> 00:07:20.380
Customer name is.

243
00:07:21.040 --> 00:07:21.480
My bad.

244
00:07:21.760 --> 00:07:22.400
Now, if I run it.

245
00:07:22.560 --> 00:07:22.920
So, you see.

246
00:07:23.560 --> 00:07:24.040
Nothing has come.

247
00:07:24.200 --> 00:07:25.320
Not even Sara Ali has come.

248
00:07:25.400 --> 00:07:25.560
Okay.

249
00:07:25.640 --> 00:07:26.400
Sara is space Ali.

250
00:07:26.620 --> 00:07:27.260
So, I do one thing.

251
00:07:27.440 --> 00:07:27.940
I give space here.

252
00:07:28.200 --> 00:07:29.080
Now, Sara Ali will come.

253
00:07:29.300 --> 00:07:30.160
You can see here.

254
00:07:30.300 --> 00:07:30.980
Sara Ali has come.

255
00:07:31.100 --> 00:07:31.220
Okay.

256
00:07:31.480 --> 00:07:32.800
So, Sara Ali has matched here.

257
00:07:33.280 --> 00:07:33.900
So, in some way.

258
00:07:34.180 --> 00:07:34.660
You guys.

259
00:07:34.760 --> 00:07:35.980
You can use wild card character.

260
00:07:37.000 --> 00:07:38.240
So, basically wild card means.

261
00:07:38.580 --> 00:07:40.240
It will match exactly one character.

262
00:07:40.360 --> 00:07:41.940
And you can use this wild card.

263
00:07:43.020 --> 00:07:43.780
After like.

264
00:07:44.180 --> 00:07:45.700
So, this will match with Delhi.

265
00:07:46.640 --> 00:07:47.700
This will match with Sara Ali.

266
00:07:47.700 --> 00:07:50.100
You can match many more combinations.

267
00:07:51.040 --> 00:07:51.920
Just keep one thing in mind.

268
00:07:52.300 --> 00:07:52.520
Here.

269
00:07:53.560 --> 00:07:54.920
The column name you have to give.

270
00:07:55.280 --> 00:07:56.700
The entry inside it will match.

271
00:07:56.900 --> 00:07:57.060
Means.

272
00:07:57.260 --> 00:07:58.260
Customer name will be Sara Ali.

273
00:07:58.620 --> 00:07:58.980
Then it will come.

274
00:07:59.220 --> 00:07:59.900
You don't think.

275
00:08:00.200 --> 00:08:01.100
That you have written here.

276
00:08:01.120 --> 00:08:01.680
Customer name.

277
00:08:01.780 --> 00:08:01.980
And here.

278
00:08:02.240 --> 00:08:02.940
You write something like this.

279
00:08:03.040 --> 00:08:03.360
Delhi.

280
00:08:04.340 --> 00:08:05.220
D underscore.

281
00:08:05.440 --> 00:08:05.940
D E.

282
00:08:06.620 --> 00:08:07.940
And L H I.

283
00:08:08.320 --> 00:08:08.480
Assume.

284
00:08:08.600 --> 00:08:09.180
You do something like this.

285
00:08:09.380 --> 00:08:09.840
And you think.

286
00:08:10.000 --> 00:08:11.320
That my Delhi will match.

287
00:08:11.860 --> 00:08:12.300
No.

288
00:08:12.420 --> 00:08:13.060
Delhi will not match.

289
00:08:13.460 --> 00:08:13.840
Yes.

290
00:08:13.940 --> 00:08:15.000
If you write city here.

291
00:08:15.120 --> 00:08:15.920
Then surely Delhi will match.

292
00:08:16.600 --> 00:08:17.020
Okay.

293
00:08:17.240 --> 00:08:17.620
You can see.

294
00:08:18.520 --> 00:08:20.240
So, these are wild cards.

295
00:08:20.400 --> 00:08:20.980
They are very basic.

296
00:08:21.580 --> 00:08:22.300
Now, here you see.

297
00:08:22.480 --> 00:08:24.260
This will match with Delhi.

298
00:08:24.920 --> 00:08:25.320
But.

299
00:08:25.520 --> 00:08:26.380
It will not match with this and this.

300
00:08:26.820 --> 00:08:27.640
Because this is D.

301
00:08:28.100 --> 00:08:28.300
Here.

302
00:08:28.500 --> 00:08:28.900
E.

303
00:08:29.180 --> 00:08:29.780
It matched till here.

304
00:08:29.940 --> 00:08:30.380
This is L.

305
00:08:30.540 --> 00:08:30.940
This is H.

306
00:08:31.039 --> 00:08:31.500
So, it didn't match.

307
00:08:32.000 --> 00:08:32.280
And.

308
00:08:32.559 --> 00:08:33.299
Similarly, here.

309
00:08:33.440 --> 00:08:34.159
This DD matched.

310
00:08:34.520 --> 00:08:35.080
Instead of underscore.

311
00:08:35.480 --> 00:08:35.940
I came.

312
00:08:36.059 --> 00:08:36.320
Okay.

313
00:08:36.840 --> 00:08:37.480
LL matched.

314
00:08:37.760 --> 00:08:38.440
But this is H.

315
00:08:38.620 --> 00:08:39.140
This is L.

316
00:08:39.299 --> 00:08:40.320
So, it won't match.

317
00:08:40.659 --> 00:08:40.919
Okay.

318
00:08:41.760 --> 00:08:43.220
Now, you can combine.

319
00:08:43.760 --> 00:08:44.560
Logical conditions.

320
00:08:44.740 --> 00:08:45.640
We had already seen.

321
00:08:47.320 --> 00:08:47.800
And.

322
00:08:49.720 --> 00:08:50.200
And.

323
00:08:54.000 --> 00:08:54.480
And.

324
00:08:55.800 --> 00:08:56.280
And.

325
00:08:56.280 --> 00:08:56.380
And.

326
00:08:58.320 --> 00:08:58.800
And.

327
00:08:58.880 --> 00:08:59.360
And.

328
00:08:59.540 --> 00:08:59.740
And.

329
00:08:59.820 --> 00:09:00.000
And.

330
00:09:00.740 --> 00:09:01.220
And.

331
00:09:01.740 --> 00:09:02.220
And.

332
00:09:04.600 --> 00:09:05.080
And.

333
00:09:05.080 --> 00:09:05.560
And.

334
00:09:06.160 --> 00:09:06.640
And.

335
00:09:11.500 --> 00:09:11.980
And.

336
00:09:12.640 --> 00:09:13.120
And.

337
00:09:13.280 --> 00:09:13.520
And.

338
00:09:13.560 --> 00:09:14.040
And.

339
00:09:14.400 --> 00:09:14.880
And.

340
00:09:15.260 --> 00:09:15.740
And.

341
00:09:15.760 --> 00:09:15.860
And.

342
00:09:15.860 --> 00:09:15.960
And.

343
00:09:15.960 --> 00:09:16.580
And.

344
00:09:16.660 --> 00:09:17.320
And.

345
00:09:17.820 --> 00:09:18.900
And.

346
00:09:18.900 --> 00:09:19.740
And.

347
00:09:24.920 --> 00:09:26.040
And.

348
00:09:26.040 --> 00:09:26.260
And.

349
00:09:26.260 --> 00:09:26.360
And.

350
00:09:29.680 --> 00:09:30.800
And.

351
00:09:31.260 --> 00:09:32.380
And.

352
00:09:33.880 --> 00:09:35.000
And.

353
00:09:35.400 --> 00:09:35.600
And.

354
00:09:35.720 --> 00:09:36.480
And.

355
00:09:37.040 --> 00:09:38.160
And.

356
00:09:42.360 --> 00:09:43.480
And.

357
00:09:44.040 --> 00:09:45.040
And.

358
00:09:47.200 --> 00:09:47.500
And.

359
00:09:47.780 --> 00:09:48.760
And.

360
00:09:51.940 --> 00:09:53.220
And.

361
00:09:57.600 --> 00:09:58.880
And.

362
00:10:02.200 --> 00:10:03.480
And.

363
00:10:09.960 --> 00:10:11.240
And.

364
00:10:11.240 --> 00:10:11.340
And.

365
00:10:11.340 --> 00:10:11.440
And.

366
00:10:11.660 --> 00:10:12.020
And.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:01.730
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right guys, now what I am going

2
00:00:01.730 --> 00:00:03.230
to tell you, it confuses a lot of

3
00:00:03.230 --> 00:00:06.210
students and a lot of people say that

4
00:00:06.210 --> 00:00:07.070
I didn't understand this thing.

5
00:00:07.750 --> 00:00:09.650
But I want to assure you that after

6
00:00:09.650 --> 00:00:11.630
watching this video, you will never be afraid

7
00:00:11.630 --> 00:00:12.390
of foreign keys.

8
00:00:13.670 --> 00:00:15.350
The claim may seem very big to you,

9
00:00:15.850 --> 00:00:17.250
but I am going to live up to

10
00:00:17.250 --> 00:00:17.750
this claim.

11
00:00:18.230 --> 00:00:20.490
A foreign key connects two tables and ensures

12
00:00:20.490 --> 00:00:22.990
that the relationship between them is valid.

13
00:00:23.270 --> 00:00:25.970
It prevents orders from referencing sellers that do

14
00:00:25.970 --> 00:00:26.490
not exist.

15
00:00:26.490 --> 00:00:28.190
So we already had a table of orders,

16
00:00:28.270 --> 00:00:29.330
we had already seen it.

17
00:00:29.330 --> 00:00:29.990
If I show you by selecting start from

18
00:00:29.990 --> 00:00:33.230
orders quickly, then these were our orders.

19
00:00:33.870 --> 00:00:37.930
Now suppose I want to store which seller

20
00:00:37.930 --> 00:00:38.630
has received this order.

21
00:00:38.890 --> 00:00:40.730
If this is a laptop, then which seller

22
00:00:40.730 --> 00:00:41.810
is going to give it?

23
00:00:42.570 --> 00:00:45.110
Let's say we have a marketplace like Amazon

24
00:00:45.110 --> 00:00:47.450
and there are a lot of sellers, if

25
00:00:47.450 --> 00:00:47.990
you don't know.

26
00:00:48.490 --> 00:00:49.850
There are a lot of sellers on Amazon,

27
00:00:50.570 --> 00:00:52.310
those sellers can sell the same product.

28
00:00:52.990 --> 00:00:55.310
10 sellers can sell the same product and

29
00:00:55.310 --> 00:00:58.750
those 10 sellers compete with each other.

30
00:00:58.870 --> 00:00:59.810
Whoever will give a good price to the

31
00:00:59.810 --> 00:01:03.069
customer, that seller is going to win and

32
00:01:03.069 --> 00:01:03.510
he is going to get the order.

33
00:01:04.129 --> 00:01:05.490
So what we will do here, first of

34
00:01:05.490 --> 00:01:06.490
all, we will add a column of the

35
00:01:06.490 --> 00:01:08.990
seller and all the information of the seller.

36
00:01:09.110 --> 00:01:11.850
Either we increase the columns here, which may

37
00:01:11.850 --> 00:01:12.430
not be so ideal.

38
00:01:12.790 --> 00:01:15.110
Because when I order data, even if I

39
00:01:15.110 --> 00:01:16.170
don't know about the seller, I will have

40
00:01:16.170 --> 00:01:17.090
to order that data again and again.

41
00:01:17.690 --> 00:01:18.550
Or I will have to change my queries.

42
00:01:18.550 --> 00:01:21.930
But if I put a column of a

43
00:01:21.930 --> 00:01:23.910
seller here and write only seller id there

44
00:01:23.910 --> 00:01:25.590
and put the seller's data in another table,

45
00:01:26.130 --> 00:01:27.070
then how good it will be.

46
00:01:27.170 --> 00:01:29.310
So to do this, we have an already

47
00:01:29.310 --> 00:01:32.030
existing table called orders table and it stores

48
00:01:32.030 --> 00:01:32.550
orders.

49
00:01:33.410 --> 00:01:34.330
Now what we will do, we will make

50
00:01:34.330 --> 00:01:36.630
a new sellers table and make a very

51
00:01:36.630 --> 00:01:37.750
basic sellers table.

52
00:01:38.270 --> 00:01:39.330
So we will make my seller table.

53
00:01:40.810 --> 00:01:41.450
By the way, I want to tell you

54
00:01:41.450 --> 00:01:42.990
one thing that you can also open a

55
00:01:42.990 --> 00:01:45.030
new query tab here.

56
00:01:45.030 --> 00:01:46.270
And you can do different things in different

57
00:01:46.270 --> 00:01:46.810
query tabs.

58
00:01:48.050 --> 00:01:49.950
For example, I want to run this create

59
00:01:49.950 --> 00:01:52.030
table sellers and I will run it as

60
00:01:52.030 --> 00:01:53.810
soon as my seller table is made.

61
00:01:54.430 --> 00:01:57.090
And I will just select start from sellers

62
00:01:57.090 --> 00:01:58.310
here and run it.

63
00:01:58.450 --> 00:02:00.990
So I will get sellers and it is

64
00:02:00.990 --> 00:02:02.770
a very basic table, there is no data

65
00:02:02.770 --> 00:02:05.150
in it, at least as of now there

66
00:02:05.150 --> 00:02:05.490
is no data.

67
00:02:05.990 --> 00:02:08.090
Now what I will do here, in my

68
00:02:08.090 --> 00:02:10.790
orders table, which was my orders table, which

69
00:02:10.790 --> 00:02:11.350
looked like this.

70
00:02:11.970 --> 00:02:12.990
What I will do in that, I will

71
00:02:12.990 --> 00:02:14.150
put a column named seller here.

72
00:02:14.150 --> 00:02:16.750
Listen very carefully, this is a whole story,

73
00:02:16.910 --> 00:02:18.050
I have told a story from the starting

74
00:02:18.050 --> 00:02:18.830
of this video.

75
00:02:19.530 --> 00:02:21.170
Listen carefully to what is happening to it.

76
00:02:21.170 --> 00:02:23.370
There was an orders table, after that I

77
00:02:23.370 --> 00:02:24.430
made a new sellers table.

78
00:02:25.210 --> 00:02:27.650
By running this query, in which there is

79
00:02:27.650 --> 00:02:29.170
a seller id, seller name and city column.

80
00:02:29.530 --> 00:02:31.210
Definitely the seller's address can also be there,

81
00:02:31.270 --> 00:02:32.290
many things can be there.

82
00:02:32.390 --> 00:02:34.870
The seller's GST can be there, all the

83
00:02:34.870 --> 00:02:35.670
information of the seller can be there.

84
00:02:35.830 --> 00:02:37.710
But we will keep things simple now because

85
00:02:37.710 --> 00:02:40.570
we have to understand what is a foreign

86
00:02:40.570 --> 00:02:40.910
key.

87
00:02:40.910 --> 00:02:44.410
Now look here, in this SQL file, I

88
00:02:44.410 --> 00:02:45.370
have selected start from orders.

89
00:02:45.670 --> 00:02:46.890
Now what I will do in this orders

90
00:02:46.890 --> 00:02:50.050
table, to store the information of the seller,

91
00:02:51.270 --> 00:02:52.510
I will just make a seller id here.

92
00:02:52.670 --> 00:02:53.570
So what I will do here, I will

93
00:02:53.570 --> 00:02:54.030
add a column named seller id.

94
00:02:55.170 --> 00:02:57.030
And I will say that this seller id

95
00:02:57.030 --> 00:02:58.870
column should be added here.

96
00:02:59.310 --> 00:03:01.290
So what will I do for this, for

97
00:03:01.290 --> 00:03:04.070
this I will simply alter table orders, add

98
00:03:04.070 --> 00:03:05.650
column seller id int.

99
00:03:05.650 --> 00:03:07.150
I will run this and you will see

100
00:03:07.150 --> 00:03:08.290
that a seller id has come here.

101
00:03:08.810 --> 00:03:10.650
Definitely this is null, all these sellers are

102
00:03:10.650 --> 00:03:10.870
null.

103
00:03:11.290 --> 00:03:13.850
We have not assigned a seller to them

104
00:03:13.850 --> 00:03:15.290
yet and our seller table is also empty.

105
00:03:16.010 --> 00:03:18.530
But assume that all the orders that will

106
00:03:18.530 --> 00:03:20.030
come in the coming time, I want to

107
00:03:20.030 --> 00:03:24.470
say that we need a seller here.

108
00:03:24.930 --> 00:03:25.790
Very good.

109
00:03:25.790 --> 00:03:27.990
Now what we will do, we will say

110
00:03:27.990 --> 00:03:33.510
that this table and this table, I will

111
00:03:33.510 --> 00:03:40.990
use ecom and I will select start from

112
00:03:40.990 --> 00:03:42.750
sellers.

113
00:03:44.310 --> 00:03:47.430
Now see, this table and this table are

114
00:03:47.430 --> 00:03:48.190
linking us.

115
00:03:48.190 --> 00:03:50.050
I want to say that if seller id

116
00:03:50.050 --> 00:03:52.190
is 1 here, then we are talking about

117
00:03:52.190 --> 00:03:53.250
this seller which is 1.

118
00:03:53.530 --> 00:03:55.210
Assume that the name of the seller is

119
00:03:55.210 --> 00:03:58.050
Dontech Private Limited City Bangalore.

120
00:03:58.270 --> 00:03:59.870
So we are talking about this seller.

121
00:04:00.490 --> 00:04:02.210
So we have to link these two and

122
00:04:02.210 --> 00:04:03.910
this is the foreign key.

123
00:04:04.090 --> 00:04:07.330
So we link using a foreign key constraint.

124
00:04:07.750 --> 00:04:08.790
So what we will do, we will alter

125
00:04:08.790 --> 00:04:09.650
the orders table.

126
00:04:10.410 --> 00:04:11.830
We will say that we want to add

127
00:04:11.830 --> 00:04:13.010
a constraint.

128
00:04:13.890 --> 00:04:15.649
We are saying that the foreign key is

129
00:04:15.649 --> 00:04:21.290
seller id which is referencing the seller id

130
00:04:21.290 --> 00:04:21.410
of the sellers table.

131
00:04:22.230 --> 00:04:23.370
Whose seller id?

132
00:04:24.030 --> 00:04:25.370
This is the sellers table.

133
00:04:25.730 --> 00:04:27.370
So as soon as I run this code,

134
00:04:28.370 --> 00:04:29.950
what I am basically saying here, I am

135
00:04:29.950 --> 00:04:33.010
saying that change my orders table such that

136
00:04:33.010 --> 00:04:37.430
the seller id in my orders is linked

137
00:04:37.430 --> 00:04:39.970
to the seller id of the sellers table.

138
00:04:39.970 --> 00:04:41.930
So here I am saying a simple thing.

139
00:04:42.150 --> 00:04:44.790
This ensures every seller id in orders must

140
00:04:44.790 --> 00:04:45.690
exist in sellers.

141
00:04:46.250 --> 00:04:49.710
This will be ensure and invalid seller references

142
00:04:49.710 --> 00:04:50.590
are not allowed.

143
00:04:50.750 --> 00:04:52.970
So as soon as I run this, you

144
00:04:52.970 --> 00:04:54.510
guys see what will happen.

145
00:04:54.570 --> 00:04:55.610
So I run this first.

146
00:04:56.490 --> 00:04:57.570
So as soon as I try to run

147
00:04:57.570 --> 00:05:01.430
this, you see here, it is running.

148
00:05:01.690 --> 00:05:03.250
12 rows returned.

149
00:05:03.490 --> 00:05:05.170
There is no seller here.

150
00:05:05.250 --> 00:05:06.050
It is null null null null.

151
00:05:06.050 --> 00:05:09.790
And here we have run this alter command.

152
00:05:10.530 --> 00:05:11.870
In which we have said that the orders

153
00:05:11.870 --> 00:05:15.070
table has a seller id linked to its

154
00:05:15.070 --> 00:05:16.190
seller id.

155
00:05:16.670 --> 00:05:17.510
Very good.

156
00:05:18.010 --> 00:05:19.670
So I have also altered this table.

157
00:05:20.030 --> 00:05:23.550
Now our foreign key relationship has been created

158
00:05:23.550 --> 00:05:24.270
in both the tables.

159
00:05:24.470 --> 00:05:26.870
Now there is a relationship between these two

160
00:05:26.870 --> 00:05:26.970
tables.

161
00:05:27.210 --> 00:05:30.650
It means that the orders table has come

162
00:05:30.650 --> 00:05:31.610
into a relationship with the sellers table.

163
00:05:32.470 --> 00:05:33.050
In which has come?

164
00:05:33.370 --> 00:05:34.630
In relationship.

165
00:05:34.630 --> 00:05:35.270
Okay.

166
00:05:35.870 --> 00:05:38.870
Now these two orders and sellers are in

167
00:05:38.870 --> 00:05:39.870
a relationship.

168
00:05:40.290 --> 00:05:40.470
Okay.

169
00:05:41.130 --> 00:05:42.590
I hope you understood the story so far.

170
00:05:42.810 --> 00:05:44.130
Now I will add a seller in the

171
00:05:44.130 --> 00:05:46.630
sellers, whose name is Tech World Delhi.

172
00:05:47.050 --> 00:05:48.670
So here I will add it.

173
00:05:49.350 --> 00:05:50.890
I will run it and now see Tech

174
00:05:50.890 --> 00:05:51.590
World Delhi has come.

175
00:05:51.730 --> 00:05:52.830
Now let's say Tech World 2.

176
00:05:53.710 --> 00:05:55.490
Let's say this guy is in Bangalore.

177
00:05:56.970 --> 00:05:58.050
Let's add them too.

178
00:05:58.330 --> 00:05:58.490
Okay.

179
00:05:58.950 --> 00:05:59.850
Tech World 2 Bangalore.

180
00:05:59.930 --> 00:06:01.430
So I have added two sellers here.

181
00:06:01.430 --> 00:06:04.910
Now let's say I am adding a data

182
00:06:04.910 --> 00:06:05.470
point here.

183
00:06:06.190 --> 00:06:06.330
Oops.

184
00:06:06.590 --> 00:06:08.430
I have added it again by mistake.

185
00:06:09.430 --> 00:06:09.610
Okay.

186
00:06:09.850 --> 00:06:10.350
This is a good thing.

187
00:06:10.410 --> 00:06:10.790
There is a constraint.

188
00:06:11.090 --> 00:06:13.430
Our seller name should not be the same.

189
00:06:14.410 --> 00:06:15.010
No problem.

190
00:06:15.190 --> 00:06:16.410
So here we will insert in the orders.

191
00:06:17.430 --> 00:06:18.430
We will say that the seller id is

192
00:06:18.430 --> 00:06:18.630
1.

193
00:06:18.830 --> 00:06:19.610
The product is a laptop.

194
00:06:20.310 --> 00:06:21.550
And the quantity is 1.

195
00:06:22.010 --> 00:06:23.290
And the price per unit is Rs.

196
00:06:23.290 --> 00:06:23.770
65,000.

197
00:06:23.950 --> 00:06:24.090
Okay.

198
00:06:24.530 --> 00:06:26.290
We have put seller id 1 here.

199
00:06:26.350 --> 00:06:26.930
This is the seller id.

200
00:06:27.070 --> 00:06:27.790
This is not the order id.

201
00:06:27.930 --> 00:06:28.950
Remember this is the seller id.

202
00:06:28.950 --> 00:06:30.630
So as soon as I run it.

203
00:06:31.030 --> 00:06:31.690
You see here.

204
00:06:32.170 --> 00:06:33.530
An entry has become like this.

205
00:06:33.710 --> 00:06:34.970
In which all these things are empty.

206
00:06:35.170 --> 00:06:36.150
But the seller id is 1.

207
00:06:36.470 --> 00:06:36.570
Okay.

208
00:06:37.050 --> 00:06:38.030
What is the seller id here?

209
00:06:38.170 --> 00:06:38.630
Our 1 has come.

210
00:06:39.430 --> 00:06:39.850
Very good.

211
00:06:40.310 --> 00:06:41.090
So we have put a laptop with seller

212
00:06:41.090 --> 00:06:42.570
id 1 here.

213
00:06:42.770 --> 00:06:44.050
Let's say I do seller id 2.

214
00:06:44.870 --> 00:06:46.330
Let's put a lamp.

215
00:06:46.970 --> 00:06:47.170
Okay.

216
00:06:47.630 --> 00:06:49.750
And let's say the quantity is 13 lamps.

217
00:06:49.830 --> 00:06:50.650
Some brother has ordered it.

218
00:06:50.730 --> 00:06:50.830
Let's get it for Rs.

219
00:06:50.830 --> 00:06:51.170
5000.

220
00:06:51.690 --> 00:06:51.890
That's why.

221
00:06:52.610 --> 00:06:53.070
I will run.

222
00:06:53.270 --> 00:06:54.170
So see here it came.

223
00:06:54.230 --> 00:06:54.390
Okay.

224
00:06:54.390 --> 00:06:56.030
So now basically here.

225
00:06:56.030 --> 00:06:57.370
The seller id which is 2.

226
00:06:57.590 --> 00:06:59.930
It means that the seller is this brother.

227
00:07:00.290 --> 00:07:01.090
Which brother is it?

228
00:07:01.110 --> 00:07:01.430
Let me remove this.

229
00:07:02.370 --> 00:07:03.630
The seller is this brother.

230
00:07:04.030 --> 00:07:04.850
Tech world 2.

231
00:07:04.870 --> 00:07:05.290
He ordered from Bangalore.

232
00:07:06.590 --> 00:07:07.530
This lamp.

233
00:07:07.830 --> 00:07:08.850
And where did he order the laptop from?

234
00:07:09.190 --> 00:07:09.890
He ordered the laptop from Delhi.

235
00:07:11.730 --> 00:07:12.190
Look at this.

236
00:07:12.530 --> 00:07:12.950
He ordered from tech world.

237
00:07:13.430 --> 00:07:14.070
He is a laptop.

238
00:07:14.390 --> 00:07:14.490
Okay.

239
00:07:15.430 --> 00:07:17.250
So this is foreign.

240
00:07:17.490 --> 00:07:18.710
Now I will show you here.

241
00:07:19.090 --> 00:07:19.290
What will happen if you try to insert

242
00:07:19.290 --> 00:07:20.350
invalid data?

243
00:07:22.230 --> 00:07:23.570
Now let's say you get the seller id.

244
00:07:23.950 --> 00:07:24.130
Rs.

245
00:07:24.130 --> 00:07:24.370
999.

246
00:07:24.370 --> 00:07:26.750
You say that brother.

247
00:07:26.930 --> 00:07:28.130
I have to give the seller id.

248
00:07:29.050 --> 00:07:29.530
255.

249
00:07:30.610 --> 00:07:31.090
255.

250
00:07:31.170 --> 00:07:32.230
255 is not in this table.

251
00:07:33.730 --> 00:07:34.210
Yes.

252
00:07:34.310 --> 00:07:35.030
But you wrote it.

253
00:07:35.530 --> 00:07:35.870
Your wish.

254
00:07:36.350 --> 00:07:36.550
Okay.

255
00:07:36.910 --> 00:07:37.610
Your laptop.

256
00:07:38.330 --> 00:07:38.870
Your wish.

257
00:07:39.730 --> 00:07:40.410
You ran.

258
00:07:41.790 --> 00:07:42.870
So MySQL will say.

259
00:07:43.070 --> 00:07:44.270
Cannot add or update a child.

260
00:07:44.370 --> 00:07:46.270
Foreign key constraint fails.

261
00:07:47.370 --> 00:07:48.010
Means basically.

262
00:07:48.110 --> 00:07:48.590
In desi language.

263
00:07:48.790 --> 00:07:49.070
He is saying.

264
00:07:49.190 --> 00:07:49.330
Brother.

265
00:07:49.390 --> 00:07:49.910
Why are you writing 200 children?

266
00:07:50.310 --> 00:07:50.830
Seller id.

267
00:07:51.330 --> 00:07:52.050
There is no salary of 200 children.

268
00:07:53.790 --> 00:07:54.350
He said.

269
00:07:54.450 --> 00:07:55.130
How can you say this?

270
00:07:55.290 --> 00:07:55.410
If.

271
00:07:56.290 --> 00:07:57.990
There are 15 shops in a shopping complex.

272
00:07:58.150 --> 00:07:59.650
Shop number 1 to shop number 15.

273
00:07:59.730 --> 00:08:00.450
How can you say this?

274
00:08:00.510 --> 00:08:00.990
Shop number.

275
00:08:01.510 --> 00:08:01.870
Take goods from 222.

276
00:08:02.670 --> 00:08:03.070
How to take?

277
00:08:03.190 --> 00:08:03.310
Brother.

278
00:08:03.630 --> 00:08:04.070
Can't take.

279
00:08:04.290 --> 00:08:04.890
There is no shop.

280
00:08:05.090 --> 00:08:05.310
Okay.

281
00:08:05.950 --> 00:08:06.130
So.

282
00:08:06.450 --> 00:08:06.870
Something like this.

283
00:08:07.230 --> 00:08:07.890
Means the same thing happened.

284
00:08:08.170 --> 00:08:08.930
Come on 30th February.

285
00:08:09.330 --> 00:08:10.070
I will give a party on my birthday.

286
00:08:10.810 --> 00:08:10.990
Brother.

287
00:08:11.110 --> 00:08:11.310
All this.

288
00:08:11.730 --> 00:08:12.650
Jokes used to happen before.

289
00:08:12.790 --> 00:08:12.970
Okay.

290
00:08:13.450 --> 00:08:14.770
So here you are with MySQL.

291
00:08:15.130 --> 00:08:15.590
So don't do all this joke.

292
00:08:16.230 --> 00:08:16.470
Okay.

293
00:08:17.410 --> 00:08:19.250
So these are our foreign keys.

294
00:08:19.310 --> 00:08:20.350
It ensures data integrity.

295
00:08:20.350 --> 00:08:22.550
It saves from invalid relationships.

296
00:08:23.350 --> 00:08:24.610
This is a very important point.

297
00:08:25.410 --> 00:08:27.450
Prevents invalid relationships.

298
00:08:27.770 --> 00:08:27.870
Okay.

299
00:08:28.410 --> 00:08:29.590
Makes data consistent.

300
00:08:29.970 --> 00:08:31.510
Essential for relational databases.

301
00:08:31.710 --> 00:08:31.830
Okay.

302
00:08:31.909 --> 00:08:33.870
I hope you are enjoying this course so

303
00:08:33.870 --> 00:08:34.090
far.

304
00:08:34.250 --> 00:08:34.809
Tag me on Instagram.

305
00:08:35.370 --> 00:08:35.710
Do it on Twitter.

306
00:08:36.309 --> 00:08:36.809
Do it anywhere.

307
00:08:36.990 --> 00:08:38.330
Tell me that you are enjoying it.

308
00:08:38.570 --> 00:08:40.549
And I want you to tell me that

309
00:08:40.549 --> 00:08:41.270
you are enjoying it.

310
00:08:41.350 --> 00:08:42.789
I will get a lot of happiness from

311
00:08:42.789 --> 00:08:42.889
it.

312
00:08:43.230 --> 00:08:44.630
Thank you so much guys for watching this

313
00:08:44.630 --> 00:08:44.870
video.

314
00:08:45.070 --> 00:08:47.190
And I will see you in the next

315
00:08:47.190 --> 00:08:47.470
one.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:01.770
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right guys, in the last video, we

2
00:00:01.770 --> 00:00:03.910
saw foreign keys, we saw that we have

3
00:00:03.910 --> 00:00:05.650
a table, we have orders, we have a

4
00:00:05.650 --> 00:00:06.770
table, we have sellers.

5
00:00:07.290 --> 00:00:09.430
In the order, there is a seller id

6
00:00:09.430 --> 00:00:12.670
column, which is a foreign key, two tables

7
00:00:12.670 --> 00:00:14.250
sellers, so we saw all this.

8
00:00:14.430 --> 00:00:16.530
If I show our seller table, then there

9
00:00:16.530 --> 00:00:17.310
are two sellers in it, it looks something

10
00:00:17.310 --> 00:00:17.890
like this.

11
00:00:18.070 --> 00:00:20.030
And if I show you the orders table,

12
00:00:20.710 --> 00:00:23.130
I remove this insert line, then our orders

13
00:00:23.130 --> 00:00:24.050
table looks something like this.

14
00:00:25.010 --> 00:00:26.850
So far so good, you understood everything.

15
00:00:26.850 --> 00:00:30.910
Now I ask you a question and you

16
00:00:30.910 --> 00:00:33.490
have to tell my question, what will be

17
00:00:33.490 --> 00:00:34.150
the answer to it?

18
00:00:35.190 --> 00:00:40.250
Suppose I delete any particular seller.

19
00:00:40.770 --> 00:00:42.450
Suppose I say that seller 2 is gone,

20
00:00:42.830 --> 00:00:43.510
delete it.

21
00:00:44.330 --> 00:00:44.970
Now what will happen?

22
00:00:45.210 --> 00:00:47.210
If I delete the seller, then what will

23
00:00:47.210 --> 00:00:47.310
happen?

24
00:00:47.330 --> 00:00:48.410
You tell me by thinking.

25
00:00:48.830 --> 00:00:51.010
You will feel that you cannot delete the

26
00:00:51.010 --> 00:00:51.110
seller.

27
00:00:51.870 --> 00:00:54.690
And somewhere yes, you cannot delete the seller,

28
00:00:55.170 --> 00:00:55.650
you are right.

29
00:00:55.650 --> 00:00:59.870
So if I run here, delete from seller,

30
00:01:00.010 --> 00:01:01.390
so seller id is equal to 1, run

31
00:01:01.390 --> 00:01:01.670
it.

32
00:01:01.870 --> 00:01:02.690
So now see it is saying no.

33
00:01:03.290 --> 00:01:05.550
It is saying that cannot delete or update

34
00:01:05.550 --> 00:01:08.290
a parent row, a foreign key constraint fails.

35
00:01:08.510 --> 00:01:11.670
Basically it is saying that if you delete

36
00:01:11.670 --> 00:01:13.190
the seller, then what will happen to this

37
00:01:13.190 --> 00:01:13.450
table?

38
00:01:14.390 --> 00:01:16.570
Here we are using the seller, what will

39
00:01:16.570 --> 00:01:16.670
happen to it?

40
00:01:16.770 --> 00:01:17.270
This will be a problem.

41
00:01:18.150 --> 00:01:20.510
So yes, somewhere you will be right.

42
00:01:20.970 --> 00:01:22.450
And yes, you cannot delete.

43
00:01:24.250 --> 00:01:28.230
But when two tables are related, then deleting

44
00:01:28.230 --> 00:01:30.750
data from one table can break relationships.

45
00:01:30.930 --> 00:01:32.850
So now I will explain this to you

46
00:01:32.850 --> 00:01:34.250
by using the sellers and orders table.

47
00:01:35.270 --> 00:01:37.350
We have the current situation that sellers are

48
00:01:37.350 --> 00:01:39.630
our parent table, orders are our child table

49
00:01:39.630 --> 00:01:41.690
and seller id connects them.

50
00:01:41.810 --> 00:01:42.710
We know this much.

51
00:01:43.470 --> 00:01:44.990
Now because we have a relation between these

52
00:01:44.990 --> 00:01:48.750
two tables, that's why we were not able

53
00:01:48.750 --> 00:01:49.250
to delete the seller.

54
00:01:49.250 --> 00:01:51.890
Here I added a foreign key constraint.

55
00:01:52.510 --> 00:01:53.730
I will remove it now.

56
00:01:53.810 --> 00:01:54.990
We have three types of on delete.

57
00:01:55.850 --> 00:01:58.690
One is cascade, one is set null and

58
00:01:58.690 --> 00:02:00.670
one is restrict which is the default behavior.

59
00:02:01.110 --> 00:02:03.130
On delete restrict we saw a while ago

60
00:02:03.130 --> 00:02:05.750
where we tried to delete the seller but

61
00:02:05.750 --> 00:02:06.770
we were not able to delete the seller.

62
00:02:07.630 --> 00:02:09.970
And this was because the on delete was

63
00:02:09.970 --> 00:02:11.110
by default our restrict.

64
00:02:11.350 --> 00:02:12.550
So this is our by default.

65
00:02:13.010 --> 00:02:14.530
But now we will change our on delete

66
00:02:14.530 --> 00:02:17.070
to cascade and see what happens.

67
00:02:17.070 --> 00:02:18.550
So what do we have to do for

68
00:02:18.550 --> 00:02:18.650
this?

69
00:02:18.710 --> 00:02:19.330
First of all, we have to remove the

70
00:02:19.330 --> 00:02:20.570
foreign key from the orders table.

71
00:02:21.870 --> 00:02:22.670
Yes, we will remove the foreign key from

72
00:02:22.670 --> 00:02:24.290
our orders table.

73
00:02:25.050 --> 00:02:25.710
We will say that there is no foreign

74
00:02:25.710 --> 00:02:29.690
key constraint in the column in which we

75
00:02:29.690 --> 00:02:30.710
put this FK orders seller.

76
00:02:31.170 --> 00:02:32.410
We gave the name of foreign key constraint

77
00:02:32.410 --> 00:02:34.010
when we made this constraint.

78
00:02:35.010 --> 00:02:37.110
And if you want to check it, I

79
00:02:37.110 --> 00:02:38.810
will tell you where you can see it.

80
00:02:39.270 --> 00:02:41.590
You see FK underscore orders underscore seller.

81
00:02:42.050 --> 00:02:42.930
This was the name of our foreign key.

82
00:02:43.430 --> 00:02:44.150
Now I will run it.

83
00:02:44.810 --> 00:02:46.770
And now the foreign key constraint has been

84
00:02:46.770 --> 00:02:46.870
removed.

85
00:02:47.410 --> 00:02:48.950
Now I will put this foreign key constraint

86
00:02:48.950 --> 00:02:49.290
again.

87
00:02:49.410 --> 00:02:51.330
And this time I will say on delete

88
00:02:51.330 --> 00:02:51.730
cascade.

89
00:02:51.870 --> 00:02:53.330
So this is exactly the same command that

90
00:02:53.330 --> 00:02:54.230
we had run earlier.

91
00:02:54.550 --> 00:02:56.130
The only difference is that now we have

92
00:02:56.130 --> 00:02:57.750
added on delete cascade in it.

93
00:02:58.550 --> 00:02:59.870
So I will run it here.

94
00:03:00.410 --> 00:03:03.230
And after running it here, our foreign key

95
00:03:03.230 --> 00:03:04.350
constraint will be added again.

96
00:03:04.630 --> 00:03:07.690
So if you refresh it, you will see

97
00:03:07.690 --> 00:03:11.970
that our foreign key constraint has come here

98
00:03:11.970 --> 00:03:12.070
again.

99
00:03:12.070 --> 00:03:14.950
And if you click on it, it is

100
00:03:14.950 --> 00:03:15.430
also telling you here.

101
00:03:15.510 --> 00:03:17.450
On update, restrict, on delete cascade.

102
00:03:17.850 --> 00:03:20.370
So it is telling you what is the

103
00:03:20.370 --> 00:03:21.290
definition of foreign key constraint.

104
00:03:22.450 --> 00:03:23.970
Now we try to delete the seller.

105
00:03:24.410 --> 00:03:25.670
So now we are saying that delete seller

106
00:03:25.670 --> 00:03:26.150
id 1.

107
00:03:27.930 --> 00:03:28.810
And it was deleted.

108
00:03:29.130 --> 00:03:30.250
You see seller id 1 was deleted.

109
00:03:30.910 --> 00:03:33.190
But when we deleted seller id 1, I

110
00:03:33.190 --> 00:03:34.570
will comment it here.

111
00:03:35.470 --> 00:03:37.810
When we deleted seller id 1, what will

112
00:03:37.810 --> 00:03:37.990
happen to it?

113
00:03:38.430 --> 00:03:39.030
What will happen to this row?

114
00:03:39.030 --> 00:03:39.430
What will happen to this row?

115
00:03:40.430 --> 00:03:42.070
As soon as I run it, you see

116
00:03:42.070 --> 00:03:42.670
this row is also deleted.

117
00:03:43.050 --> 00:03:44.610
So what does on delete cascade do?

118
00:03:44.830 --> 00:03:47.810
On delete cascade, as soon as you delete

119
00:03:47.810 --> 00:03:49.290
the seller, all the orders that were linked

120
00:03:49.290 --> 00:03:50.670
to that seller will be deleted.

121
00:03:51.130 --> 00:03:52.410
You have to do this very carefully.

122
00:03:52.930 --> 00:03:55.130
If you say on delete cascade, then you

123
00:03:55.130 --> 00:03:56.390
are basically saying that when the seller is

124
00:03:56.390 --> 00:04:00.990
deleted, the customers who are related to that

125
00:04:00.990 --> 00:04:01.470
seller will be deleted.

126
00:04:02.550 --> 00:04:03.170
Do you understand?

127
00:04:03.170 --> 00:04:05.610
Means the customer who has a relationship with

128
00:04:05.610 --> 00:04:07.230
the seller, that customer is gone.

129
00:04:07.890 --> 00:04:08.450
That is also deleted.

130
00:04:09.170 --> 00:04:10.050
Because the seller has been deleted.

131
00:04:11.330 --> 00:04:15.070
You can understand it as if there is

132
00:04:15.070 --> 00:04:18.510
a building on a particular place, then if

133
00:04:18.510 --> 00:04:20.630
you break the foundation, the building will fall.

134
00:04:21.089 --> 00:04:22.270
So this is how on delete cascade works.

135
00:04:24.030 --> 00:04:25.390
But now what I will do here, I

136
00:04:25.390 --> 00:04:26.190
will alter the table.

137
00:04:26.670 --> 00:04:28.930
And I will do on delete, set null.

138
00:04:28.930 --> 00:04:30.870
So if you do on delete, set null

139
00:04:30.870 --> 00:04:34.630
and run it, refresh and see here, FK

140
00:04:34.630 --> 00:04:37.670
order seller, then you see, on delete is

141
00:04:37.670 --> 00:04:38.630
still a cascade, why is that?

142
00:04:39.230 --> 00:04:40.990
I have changed on delete.

143
00:04:41.270 --> 00:04:42.830
Actually, I will have to drop this constraint

144
00:04:42.830 --> 00:04:43.550
first.

145
00:04:44.130 --> 00:04:45.030
After that I will do this.

146
00:04:45.430 --> 00:04:47.190
So I do one thing, I do comment

147
00:04:47.190 --> 00:04:47.870
out and I show you.

148
00:04:48.350 --> 00:04:49.050
First of all, I have to drop this

149
00:04:49.050 --> 00:04:49.530
constraint.

150
00:04:51.130 --> 00:04:52.870
I have dropped this constraint, I will refresh

151
00:04:52.870 --> 00:04:53.070
it.

152
00:04:53.170 --> 00:04:53.770
So see, nothing is written in the foreign

153
00:04:53.770 --> 00:04:54.250
constraint.

154
00:04:54.250 --> 00:04:56.970
And now I will comment it out and

155
00:04:56.970 --> 00:04:58.430
run this SQL.

156
00:04:59.190 --> 00:05:01.310
So basically I am saying that I will

157
00:05:01.310 --> 00:05:02.830
close it so that you can see what

158
00:05:02.830 --> 00:05:03.170
I am running.

159
00:05:03.630 --> 00:05:04.750
And it stays on my use ecom.

160
00:05:05.530 --> 00:05:08.790
Here I have again added this foreign key

161
00:05:08.790 --> 00:05:09.270
constraint.

162
00:05:09.730 --> 00:05:11.010
And I am doing select start from orders.

163
00:05:11.730 --> 00:05:12.650
So what did I do this time?

164
00:05:13.030 --> 00:05:15.690
This time I said that on delete, set

165
00:05:15.690 --> 00:05:15.910
null.

166
00:05:16.190 --> 00:05:17.690
And you check it by refreshing it from

167
00:05:17.690 --> 00:05:17.950
here.

168
00:05:18.810 --> 00:05:20.270
That this time our on delete is set

169
00:05:20.270 --> 00:05:20.470
null.

170
00:05:20.970 --> 00:05:22.070
So what happens in on delete set null?

171
00:05:22.070 --> 00:05:23.010
What happens in on delete set null?

172
00:05:23.010 --> 00:05:26.410
That you are basically saying that if you

173
00:05:26.410 --> 00:05:28.910
delete this, delete the seller, which we have

174
00:05:28.910 --> 00:05:29.890
only one seller left.

175
00:05:30.170 --> 00:05:31.430
If you delete seller with id 2, then

176
00:05:31.430 --> 00:05:31.890
it will not be deleted.

177
00:05:32.290 --> 00:05:32.830
Here it will be null.

178
00:05:33.830 --> 00:05:36.750
And this is a practical scenario in many

179
00:05:36.750 --> 00:05:36.850
cases.

180
00:05:37.130 --> 00:05:39.550
Means you are basically saying that if I

181
00:05:39.550 --> 00:05:41.790
delete the seller, then the order of the

182
00:05:41.790 --> 00:05:44.770
customers from that seller, the seller column will

183
00:05:44.770 --> 00:05:45.070
be null in that order.

184
00:05:45.370 --> 00:05:46.630
This is a very practical thing.

185
00:05:46.990 --> 00:05:48.810
When I run it, as soon as I

186
00:05:48.810 --> 00:05:50.470
run it, you see the seller is gone

187
00:05:50.470 --> 00:05:50.770
from work.

188
00:05:51.450 --> 00:05:52.910
And I comment it out.

189
00:05:53.470 --> 00:05:56.210
And now I am running only one query.

190
00:05:56.330 --> 00:05:57.330
Select start from orders.

191
00:05:58.350 --> 00:05:59.470
And you see here it is null.

192
00:05:59.810 --> 00:06:00.710
Is there any other data of this?

193
00:06:00.910 --> 00:06:03.030
Our 14 customer.

194
00:06:03.710 --> 00:06:05.230
I have all the data of this.

195
00:06:05.230 --> 00:06:06.530
What was there earlier is that only the

196
00:06:06.530 --> 00:06:07.150
seller id is null.

197
00:06:08.030 --> 00:06:10.030
So this is a very practical scenario we

198
00:06:10.030 --> 00:06:10.290
have.

199
00:06:10.830 --> 00:06:13.930
And on delete set null you have to

200
00:06:13.930 --> 00:06:14.490
use as much as possible.

201
00:06:14.990 --> 00:06:15.750
Now I am saying that you have to

202
00:06:15.750 --> 00:06:16.450
use it, that's why you don't have to

203
00:06:16.450 --> 00:06:16.810
use it.

204
00:06:17.030 --> 00:06:18.350
But understand its practicality.

205
00:06:18.350 --> 00:06:21.330
That if you are deleting the seller, then

206
00:06:21.330 --> 00:06:21.850
the order is not deleted.

207
00:06:22.270 --> 00:06:22.970
This is an ideal scenario.

208
00:06:23.170 --> 00:06:23.730
You want to keep the data.

209
00:06:24.150 --> 00:06:26.410
In today's date, there is data, fuel, data,

210
00:06:26.530 --> 00:06:26.830
everything.

211
00:06:26.930 --> 00:06:27.770
You don't have to delete the data.

212
00:06:28.710 --> 00:06:30.470
Data is a very important thing.

213
00:06:30.590 --> 00:06:31.470
Data is the oil.

214
00:06:32.530 --> 00:06:35.310
So you have to save the data.

215
00:06:36.150 --> 00:06:38.290
And that's why you have to take decisions

216
00:06:38.290 --> 00:06:38.390
by thinking.

217
00:06:38.390 --> 00:06:41.170
But sometimes you will want that my on

218
00:06:41.170 --> 00:06:43.310
delete gets cascaded.

219
00:06:43.570 --> 00:06:46.310
If you delete the seller, then the customer

220
00:06:46.310 --> 00:06:46.790
is also deleted.

221
00:06:46.790 --> 00:06:48.310
So sometimes you will also want this.

222
00:06:48.570 --> 00:06:49.090
It will depend on the use case.

223
00:06:49.750 --> 00:06:50.950
But you have to use your brain.

224
00:06:51.710 --> 00:06:52.790
And do things accordingly.

225
00:06:53.710 --> 00:06:55.770
So yeah, we have three scenarios of on

226
00:06:55.770 --> 00:06:56.110
delete.

227
00:06:57.130 --> 00:06:59.670
Cascade means Order will be automatically deleted.

228
00:07:00.070 --> 00:07:02.150
If the seller is deleted, set null means

229
00:07:03.050 --> 00:07:04.630
Order will be there, the link of the

230
00:07:04.630 --> 00:07:04.790
seller will be removed.

231
00:07:05.010 --> 00:07:06.870
Means the seller will be null in our

232
00:07:06.870 --> 00:07:07.510
orders table.

233
00:07:08.550 --> 00:07:09.670
Restrict default behavior.

234
00:07:09.990 --> 00:07:12.610
And this seller deletion does not allow.

235
00:07:13.610 --> 00:07:15.730
If you try to delete the seller, you

236
00:07:15.730 --> 00:07:16.410
will get an error.

237
00:07:17.070 --> 00:07:18.650
As we saw in the starting of this

238
00:07:18.650 --> 00:07:18.930
video.

239
00:07:19.830 --> 00:07:22.130
So yeah, you have to take on delete

240
00:07:22.130 --> 00:07:22.630
decisions according to your business logic.

241
00:07:23.250 --> 00:07:24.850
And here I have given a very good

242
00:07:24.850 --> 00:07:26.810
scenario for you guys.

243
00:07:27.070 --> 00:07:29.970
If the marketplace is shutting down, then use

244
00:07:29.970 --> 00:07:30.330
cascade.

245
00:07:30.950 --> 00:07:32.330
The seller left the platform.

246
00:07:33.090 --> 00:07:34.490
If you want to keep orders, set null.

247
00:07:34.850 --> 00:07:37.070
If you want to avoid accidental deletion, use

248
00:07:37.070 --> 00:07:37.370
restrict.

249
00:07:37.890 --> 00:07:39.610
But again, use case to use case.

250
00:07:39.710 --> 00:07:40.190
Use your brain.

251
00:07:40.770 --> 00:07:42.450
You are a human, you have a brain.

252
00:07:43.130 --> 00:07:44.750
And you have been hired for that.

253
00:07:45.030 --> 00:07:45.670
So use it.

254
00:07:46.350 --> 00:07:47.690
Thank you so much guys for watching this

255
00:07:47.690 --> 00:07:47.970
video.

256
00:07:48.290 --> 00:07:49.990
And I will see you in the next

257
00:07:49.990 --> 00:07:50.290
one.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


WEBVTT

1
00:00:00.070 --> 00:00:02.310
(Transcribed by TurboScribe. Go Unlimited to remove this message.) All right guys, let's talk about joins in

2
00:00:02.310 --> 00:00:02.670
SQL.

3
00:00:02.970 --> 00:00:04.510
How can you use joins?

4
00:00:05.770 --> 00:00:07.310
It is very simple to use joins in

5
00:00:07.310 --> 00:00:07.650
SQL.

6
00:00:08.390 --> 00:00:10.210
Basically, what joins do is that it joins

7
00:00:10.210 --> 00:00:11.090
your table.

8
00:00:11.830 --> 00:00:12.490
It's a simple thing.

9
00:00:12.750 --> 00:00:14.590
You have one table, you have another table.

10
00:00:14.810 --> 00:00:15.670
What do you want to do?

11
00:00:15.930 --> 00:00:17.070
You want to join both of them.

12
00:00:17.610 --> 00:00:19.350
In this case, we have orders and we

13
00:00:19.350 --> 00:00:19.930
have sellers.

14
00:00:20.410 --> 00:00:21.210
What will I do here?

15
00:00:21.730 --> 00:00:23.130
First of all, I will show you how

16
00:00:23.130 --> 00:00:24.150
the orders look.

17
00:00:24.590 --> 00:00:26.630
So I backspace here and run it.

18
00:00:26.870 --> 00:00:27.950
And you see these orders.

19
00:00:27.950 --> 00:00:29.790
You see my orders look like this.

20
00:00:30.170 --> 00:00:31.009
Now what am I going to do?

21
00:00:31.130 --> 00:00:32.530
Now what am I simply going to do

22
00:00:32.530 --> 00:00:32.650
here?

23
00:00:33.070 --> 00:00:35.370
I am going to show you my sellers

24
00:00:35.370 --> 00:00:35.850
table.

25
00:00:36.830 --> 00:00:38.170
And after that we will join.

26
00:00:38.390 --> 00:00:41.150
Our seller table is completely empty.

27
00:00:41.770 --> 00:00:42.730
So what will we do here?

28
00:00:42.930 --> 00:00:43.370
Insert.

29
00:00:43.850 --> 00:00:46.010
Insert into sellers.

30
00:00:46.670 --> 00:00:47.990
And values.

31
00:00:48.250 --> 00:00:49.550
Okay, values.

32
00:00:50.430 --> 00:00:51.550
And what will we do here?

33
00:00:52.410 --> 00:00:53.050
Insert values.

34
00:00:53.950 --> 00:00:55.230
So what will I do here?

35
00:00:55.230 --> 00:00:59.670
I will write 1, Don, let's say Delhi.

36
00:00:59.990 --> 00:01:01.250
And after that I will insert it.

37
00:01:01.690 --> 00:01:02.590
I will run it here.

38
00:01:02.650 --> 00:01:04.250
And look here, 1 Don Delhi has come.

39
00:01:04.610 --> 00:01:06.410
Now I will insert one more here.

40
00:01:06.490 --> 00:01:09.810
I will write 2 Don Electronics here.

41
00:01:10.090 --> 00:01:10.970
And let's say this is also in Delhi.

42
00:01:11.690 --> 00:01:12.490
I have also inserted it.

43
00:01:12.910 --> 00:01:15.690
And let's say Knight Electronics is one.

44
00:01:15.710 --> 00:01:16.970
And let's say this is in Bangalore.

45
00:01:18.050 --> 00:01:19.410
And I have also inserted it.

46
00:01:19.590 --> 00:01:20.870
I think we have enough 3.

47
00:01:20.990 --> 00:01:21.690
What is the problem here?

48
00:01:21.890 --> 00:01:23.110
Okay, so I gave the same primary key.

49
00:01:23.930 --> 00:01:26.450
Now look here, 1, 2 and 3.

50
00:01:26.630 --> 00:01:26.970
Let's also insert a 4.

51
00:01:27.850 --> 00:01:28.710
Let's say there is a branch of Knight

52
00:01:28.710 --> 00:01:30.690
Electronics in Mumbai.

53
00:01:32.110 --> 00:01:32.630
Okay.

54
00:01:32.930 --> 00:01:34.090
And along with that, there is a branch

55
00:01:34.090 --> 00:01:35.270
of Knight Electronics in Dubai.

56
00:01:36.070 --> 00:01:36.350
Okay.

57
00:01:37.050 --> 00:01:37.710
We are not going to Dubai.

58
00:01:37.910 --> 00:01:38.170
Leave it.

59
00:01:38.370 --> 00:01:39.010
Let's do one thing.

60
00:01:39.230 --> 00:01:39.650
Let's write Kolkata.

61
00:01:40.610 --> 00:01:41.610
I mean, why outside India.

62
00:01:43.290 --> 00:01:44.290
Let me do 5.

63
00:01:44.770 --> 00:01:46.250
I have to make my seller sit.

64
00:01:46.850 --> 00:01:47.490
Let's not leave India.

65
00:01:47.730 --> 00:01:48.370
This commerce website.

66
00:01:49.290 --> 00:01:51.130
Okay, so here it is saying that Knight

67
00:01:51.130 --> 00:01:52.150
Electronics 2.

68
00:01:52.150 --> 00:01:53.690
Which is a duplicate entry.

69
00:01:53.850 --> 00:01:54.690
Knight Electronics 3.

70
00:01:54.810 --> 00:01:55.190
Let's do it.

71
00:01:55.310 --> 00:01:58.170
Now we have a very good data.

72
00:01:58.370 --> 00:01:58.530
Okay.

73
00:01:58.970 --> 00:01:59.450
So what will we do?

74
00:01:59.570 --> 00:02:00.090
We will comment it out.

75
00:02:00.390 --> 00:02:01.270
And here we have the data of the

76
00:02:01.270 --> 00:02:01.410
seller.

77
00:02:01.890 --> 00:02:02.870
And what do we have here?

78
00:02:03.410 --> 00:02:04.870
We have the data of the customer here.

79
00:02:05.270 --> 00:02:06.850
So what will we do here now?

80
00:02:07.229 --> 00:02:09.669
With the help of joins, we will see

81
00:02:09.669 --> 00:02:10.830
how two tables can be joined.

82
00:02:11.310 --> 00:02:12.930
Now I will run an update query here.

83
00:02:13.070 --> 00:02:14.390
And I will write update here.

84
00:02:14.530 --> 00:02:15.870
The name of our table is orders.

85
00:02:16.110 --> 00:02:16.990
I will write set.

86
00:02:17.750 --> 00:02:21.150
Seller underscore ID is equal to.

87
00:02:21.390 --> 00:02:22.950
Let's say we do seller ID 1.

88
00:02:23.570 --> 00:02:25.390
And here we will put a where clause.

89
00:02:25.810 --> 00:02:26.770
We will say where.

90
00:02:27.410 --> 00:02:31.190
And let's say order underscore ID in.

91
00:02:32.110 --> 00:02:33.490
And we will give value here.

92
00:02:33.590 --> 00:02:37.430
We will say 1, 4, 6 and 5

93
00:02:37.430 --> 00:02:37.950
and 9.

94
00:02:38.290 --> 00:02:38.830
Is it 9?

95
00:02:39.090 --> 00:02:39.650
Yes, it is 9.

96
00:02:40.650 --> 00:02:41.790
Do this.

97
00:02:42.130 --> 00:02:42.350
Okay.

98
00:02:42.550 --> 00:02:43.890
And we run it here.

99
00:02:43.890 --> 00:02:46.370
And here we have done seller ID 1.

100
00:02:46.750 --> 00:02:48.030
And we will say sell ID 2.

101
00:02:48.350 --> 00:02:48.550
Where?

102
00:02:49.530 --> 00:02:51.430
2, 3, 7, 8.

103
00:02:51.610 --> 00:02:51.710
Okay.

104
00:02:51.810 --> 00:02:52.750
2, 3, 7, 8.

105
00:02:52.890 --> 00:02:56.770
2, 3, 7, 8, 10, 11.

106
00:02:56.970 --> 00:02:57.090
Okay.

107
00:02:57.490 --> 00:02:58.490
Now you will say why are you doing

108
00:02:58.490 --> 00:02:58.590
this?

109
00:02:58.610 --> 00:02:59.510
This is basically what I am doing.

110
00:02:59.650 --> 00:03:01.210
Because I want my seller ID to be

111
00:03:01.210 --> 00:03:01.550
populated.

112
00:03:01.830 --> 00:03:01.970
Okay.

113
00:03:02.090 --> 00:03:02.590
Now look here.

114
00:03:02.610 --> 00:03:03.650
Our seller ID has been populated.

115
00:03:03.850 --> 00:03:04.970
Let's nullify them here.

116
00:03:04.970 --> 00:03:05.530
The last three.

117
00:03:06.130 --> 00:03:06.710
Let's do one thing.

118
00:03:07.330 --> 00:03:08.430
We also put seller ID in the last

119
00:03:08.430 --> 00:03:08.530
three.

120
00:03:09.030 --> 00:03:10.050
So what will we do in 11, 12,

121
00:03:10.110 --> 00:03:10.510
13?

122
00:03:11.630 --> 00:03:12.630
11, 12, 14.

123
00:03:12.630 --> 00:03:14.510
Let's put seller ID 3 in 11, 12,

124
00:03:14.510 --> 00:03:14.610
13.

125
00:03:14.990 --> 00:03:16.610
I think this should be good enough.

126
00:03:17.130 --> 00:03:19.010
And here you see what we have done.

127
00:03:19.850 --> 00:03:21.270
Seller ID has been put here.

128
00:03:21.410 --> 00:03:21.610
In all.

129
00:03:21.830 --> 00:03:22.710
Seller ID is in all.

130
00:03:22.710 --> 00:03:23.650
Now see what is join?

131
00:03:24.090 --> 00:03:25.150
We have two tables.

132
00:03:25.270 --> 00:03:26.330
Orders and sellers.

133
00:03:26.770 --> 00:03:27.250
What will we do?

134
00:03:27.450 --> 00:03:29.450
We will basically see three types of joins.

135
00:03:30.130 --> 00:03:32.910
Inner join, left join and right join.

136
00:03:33.210 --> 00:03:34.590
Now what do these joins do?

137
00:03:34.990 --> 00:03:37.390
These joins basically do different kinds of work.

138
00:03:37.650 --> 00:03:38.490
What does inner join do?

139
00:03:38.490 --> 00:03:41.450
It returns only those rows where the matching

140
00:03:41.450 --> 00:03:42.990
data exists on both sides.

141
00:03:43.410 --> 00:03:44.810
If there is a null in any particular

142
00:03:44.810 --> 00:03:45.510
row here.

143
00:03:45.950 --> 00:03:47.510
Or the matching data does not exist.

144
00:03:47.870 --> 00:03:48.750
Then it will not be returned.

145
00:03:49.230 --> 00:03:51.590
So how will we do this thing?

146
00:03:52.930 --> 00:03:53.830
What will we do?

147
00:03:53.910 --> 00:03:55.310
We will use the syntax of joins.

148
00:03:55.630 --> 00:03:56.970
So how does inner join work?

149
00:03:56.990 --> 00:03:57.270
I will show you.

150
00:03:58.050 --> 00:03:59.750
You will say select here.

151
00:03:59.870 --> 00:04:00.490
I will remove this query.

152
00:04:00.870 --> 00:04:01.670
Or I will comment it out.

153
00:04:02.750 --> 00:04:03.870
I will write select.

154
00:04:05.330 --> 00:04:06.570
And I will write here.

155
00:04:06.570 --> 00:04:07.270
Now what is O?

156
00:04:08.370 --> 00:04:12.190
O is our orders table.

157
00:04:12.710 --> 00:04:14.630
And we will name it S.

158
00:04:15.010 --> 00:04:15.890
Now what is O?

159
00:04:16.130 --> 00:04:17.089
You will understand what S is.

160
00:04:18.510 --> 00:04:19.890
I wrote O.order ID.

161
00:04:20.529 --> 00:04:20.750
I will put a comma.

162
00:04:21.070 --> 00:04:23.430
I will write O.product. I will put

163
00:04:23.430 --> 00:04:23.530
a comma.

164
00:04:23.630 --> 00:04:25.690
I will write O.city as.

165
00:04:26.770 --> 00:04:27.230
What will I write?

166
00:04:27.410 --> 00:04:29.030
Customer underscore city.

167
00:04:29.950 --> 00:04:30.570
And I will say.

168
00:04:31.170 --> 00:04:32.550
What do I want after that?

169
00:04:32.810 --> 00:04:35.110
I want S.seller name.

170
00:04:35.910 --> 00:04:37.150
Which I want from here.

171
00:04:37.390 --> 00:04:38.110
Now what is S and O?

172
00:04:38.450 --> 00:04:38.970
I will tell you.

173
00:04:39.090 --> 00:04:40.170
I want seller name from here.

174
00:04:40.510 --> 00:04:41.730
I want seller name from here.

175
00:04:42.170 --> 00:04:43.150
And order ID.

176
00:04:43.790 --> 00:04:44.370
And product.

177
00:04:44.590 --> 00:04:44.870
And city.

178
00:04:44.990 --> 00:04:45.630
And customer city.

179
00:04:45.730 --> 00:04:46.310
I want from here.

180
00:04:46.390 --> 00:04:47.950
I want city as customer city from here.

181
00:04:48.250 --> 00:04:49.490
The name of the city column will be

182
00:04:49.490 --> 00:04:50.070
customer city.

183
00:04:50.790 --> 00:04:52.430
We saw S a while ago.

184
00:04:52.550 --> 00:04:52.950
What happens?

185
00:04:53.530 --> 00:04:54.570
What will I do after this?

186
00:04:54.670 --> 00:04:55.350
I will write from.

187
00:04:55.630 --> 00:04:56.230
I will write orders.

188
00:04:56.790 --> 00:04:57.670
Which is O.

189
00:04:58.350 --> 00:04:59.870
Here I will write orders O.

190
00:05:00.490 --> 00:05:02.770
And after that I will write inner join.

191
00:05:04.070 --> 00:05:04.850
Sellers S.

192
00:05:04.850 --> 00:05:05.650
Now understand the syntax.

193
00:05:06.590 --> 00:05:08.250
Now I have said that the orders are

194
00:05:08.250 --> 00:05:08.490
O.

195
00:05:08.670 --> 00:05:09.610
Sellers are S.

196
00:05:10.110 --> 00:05:10.810
Now on.

197
00:05:10.970 --> 00:05:11.750
Where am I putting inner join?

198
00:05:13.870 --> 00:05:16.310
Where O.seller ID is equal to S

199
00:05:16.310 --> 00:05:17.490
.seller ID.

200
00:05:17.650 --> 00:05:19.170
Now understand this query carefully.

201
00:05:19.290 --> 00:05:20.590
We will take some time to understand.

202
00:05:21.050 --> 00:05:21.870
What are we saying here?

203
00:05:22.210 --> 00:05:22.630
We are saying.

204
00:05:22.970 --> 00:05:23.890
I want this and this.

205
00:05:24.370 --> 00:05:24.490
Okay.

206
00:05:25.450 --> 00:05:26.150
I want this and this.

207
00:05:26.610 --> 00:05:27.390
In and in table.

208
00:05:28.390 --> 00:05:29.270
I am basically.

209
00:05:30.130 --> 00:05:30.630
I am putting the inner join of order

210
00:05:30.630 --> 00:05:30.930
O.

211
00:05:31.710 --> 00:05:32.270
From seller S.

212
00:05:32.410 --> 00:05:33.670
Means seller S is my table S.

213
00:05:33.670 --> 00:05:34.810
And my table is O.

214
00:05:35.090 --> 00:05:35.610
According to that.

215
00:05:36.250 --> 00:05:36.390
Take this.

216
00:05:36.830 --> 00:05:38.190
And I am saying on.

217
00:05:39.150 --> 00:05:40.970
O.seller ID is equal to S.seller

218
00:05:40.970 --> 00:05:41.170
ID.

219
00:05:41.290 --> 00:05:41.430
Means.

220
00:05:41.830 --> 00:05:42.950
I want seller ID wherever it is equal.

221
00:05:44.230 --> 00:05:44.670
So.

222
00:05:45.410 --> 00:05:46.390
Wherever seller ID will be in both.

223
00:05:46.850 --> 00:05:47.470
You will get to see those records.

224
00:05:48.270 --> 00:05:49.150
So I will run it like this.

225
00:05:49.670 --> 00:05:50.350
You see here.

226
00:05:50.450 --> 00:05:51.690
We are only getting to see those records.

227
00:05:52.770 --> 00:05:53.090
Wherever.

228
00:05:54.630 --> 00:05:56.730
O.seller ID is equal to S.seller

229
00:05:56.730 --> 00:05:57.030
ID.

230
00:05:57.270 --> 00:05:58.210
And we will get the same records.

231
00:05:58.570 --> 00:05:59.290
Which will be in both the tables.

232
00:05:59.970 --> 00:06:01.270
This is our inner join.

233
00:06:01.790 --> 00:06:03.330
Now if I join it to the left.

234
00:06:03.330 --> 00:06:04.370
Now see how many are here.

235
00:06:04.430 --> 00:06:05.010
I have five.

236
00:06:05.330 --> 00:06:05.430
I.

237
00:06:06.070 --> 00:06:06.430
Oops.

238
00:06:06.670 --> 00:06:07.830
Here I am getting to see how many.

239
00:06:07.930 --> 00:06:09.090
1, 2, 3, 4, 5, 6, 7, 8.

240
00:06:09.170 --> 00:06:09.650
Almost all have come.

241
00:06:10.390 --> 00:06:11.870
Now if I join it to the left.

242
00:06:12.650 --> 00:06:13.730
What will happen if I join it to

243
00:06:13.730 --> 00:06:13.830
the left?

244
00:06:14.270 --> 00:06:15.530
So if I join it to the left.

245
00:06:15.870 --> 00:06:16.430
Then I.

246
00:06:16.970 --> 00:06:17.930
In the left table.

247
00:06:18.910 --> 00:06:19.890
All sellers will be seen.

248
00:06:20.790 --> 00:06:21.090
Even.

249
00:06:21.430 --> 00:06:21.950
All orders will be seen.

250
00:06:22.270 --> 00:06:23.090
The left one is our orders.

251
00:06:23.330 --> 00:06:24.370
The left one is our orders.

252
00:06:24.770 --> 00:06:25.590
All orders will be seen.

253
00:06:25.870 --> 00:06:27.070
Even if seller is missing.

254
00:06:27.210 --> 00:06:27.330
Okay.

255
00:06:27.690 --> 00:06:28.450
If seller is missing.

256
00:06:28.570 --> 00:06:29.190
Still we will get to see all orders.

257
00:06:30.030 --> 00:06:30.250
So.

258
00:06:30.570 --> 00:06:30.750
To show this.

259
00:06:31.170 --> 00:06:31.890
I will do one thing.

260
00:06:31.890 --> 00:06:32.310
That.

261
00:06:32.910 --> 00:06:34.330
I will do some changes in my table.

262
00:06:34.810 --> 00:06:35.770
And what changes I will do.

263
00:06:35.830 --> 00:06:36.090
I am showing you.

264
00:06:36.810 --> 00:06:37.470
What I will do.

265
00:06:37.770 --> 00:06:37.870
That.

266
00:06:38.430 --> 00:06:38.550
Some.

267
00:06:39.290 --> 00:06:40.010
Our items.

268
00:06:40.150 --> 00:06:40.750
I will null them.

269
00:06:40.950 --> 00:06:42.170
I null 11, 12, and 14.

270
00:06:42.790 --> 00:06:43.470
Or even I do one thing.

271
00:06:44.070 --> 00:06:45.110
I null 1, 9, and 14.

272
00:06:45.850 --> 00:06:46.010
Okay.

273
00:06:46.050 --> 00:06:46.930
I null 1, 9, and 14.

274
00:06:48.530 --> 00:06:48.890
Okay.

275
00:06:48.890 --> 00:06:49.290
I null 1, 9, and 14.

276
00:06:49.570 --> 00:06:49.930
Okay.

277
00:06:50.290 --> 00:06:50.550
I do this.

278
00:06:50.990 --> 00:06:52.130
And as soon as I do this.

279
00:06:52.570 --> 00:06:52.910
You see.

280
00:06:52.990 --> 00:06:53.510
I nulled the seller id.

281
00:06:56.090 --> 00:06:56.770
Now what will happen.

282
00:06:56.850 --> 00:06:57.170
Now you see.

283
00:06:57.610 --> 00:06:58.430
Now I do comment out.

284
00:06:59.350 --> 00:07:00.290
And now what I will do.

285
00:07:00.290 --> 00:07:01.530
Now I will run this query.

286
00:07:01.630 --> 00:07:02.470
Basically what I am doing.

287
00:07:02.610 --> 00:07:02.910
I am joining left.

288
00:07:03.490 --> 00:07:03.650
Okay.

289
00:07:03.730 --> 00:07:04.950
And I will do one more thing here.

290
00:07:05.450 --> 00:07:06.210
What I will do here.

291
00:07:06.790 --> 00:07:08.850
I will insert into seller.

292
00:07:09.090 --> 00:07:10.290
Where I will do.

293
00:07:11.070 --> 00:07:11.310
That.

294
00:07:12.410 --> 00:07:13.950
Here basically I will put a seller id.

295
00:07:14.350 --> 00:07:15.590
Which does not exist.

296
00:07:16.010 --> 00:07:17.550
I do this thing here.

297
00:07:17.670 --> 00:07:18.290
By commenting it.

298
00:07:19.250 --> 00:07:20.770
So give me a moment.

299
00:07:20.950 --> 00:07:21.490
I will do this quickly.

300
00:07:21.850 --> 00:07:23.090
Basically what I am doing here.

301
00:07:23.770 --> 00:07:26.850
2 and 7's seller id.

302
00:07:27.090 --> 00:07:27.510
I am doing.

303
00:07:28.310 --> 00:07:28.910
99.

304
00:07:29.710 --> 00:07:30.270
Okay.

305
00:07:30.270 --> 00:07:31.270
99.

306
00:07:33.030 --> 00:07:33.750
99.

307
00:07:36.690 --> 00:07:38.130
99.

308
00:07:44.450 --> 00:07:45.590
99.

309
00:07:47.850 --> 00:07:49.290
99.

310
00:07:51.350 --> 00:07:51.550
99.

311
00:07:52.130 --> 00:07:52.230
99.

312
00:07:52.230 --> 00:07:52.330
99.

313
00:07:52.330 --> 00:07:52.430
99.

314
00:07:52.430 --> 00:07:52.530
99.

315
00:07:52.530 --> 00:07:52.630
99.

316
00:07:55.750 --> 00:07:56.670
99.

317
00:07:58.770 --> 00:07:59.530
99.

318
00:08:03.890 --> 00:08:04.690
99.

319
00:08:05.330 --> 00:08:05.670
99.

320
00:08:10.470 --> 00:08:11.270
99.

321
00:08:11.470 --> 00:08:11.570
99.

322
00:08:11.570 --> 00:08:11.830
99.

323
00:08:18.730 --> 00:08:19.530
99.

324
00:08:24.610 --> 00:08:25.130
99.

325
00:08:25.810 --> 00:08:26.610
99.

326
00:08:26.630 --> 00:08:26.730
99.

327
00:08:26.730 --> 00:08:26.830
99.

328
00:08:26.830 --> 00:08:27.110
99.

329
00:08:27.110 --> 00:08:28.990
If possible, you can also delete your foreign

330
00:08:28.990 --> 00:08:37.250
key constraint and drop the foreign key and

331
00:08:37.250 --> 00:08:40.030
then insert the sample data by using insert,

332
00:08:40.929 --> 00:08:43.870
play around with this, you will definitely get

333
00:08:43.870 --> 00:08:45.770
a very good clarity if you go out

334
00:08:45.770 --> 00:08:49.090
of the query given by me and experiment

335
00:08:49.090 --> 00:08:50.930
with yourself, so guys this was our left

336
00:08:50.930 --> 00:08:55.210
join, right join and inner join and basically

337
00:08:55.210 --> 00:08:56.570
what does inner join do, it gives you

338
00:08:56.570 --> 00:08:58.050
all the data which is in both the

339
00:08:58.050 --> 00:09:01.390
tables, then left join gives all the values

340
00:09:01.390 --> 00:09:02.150
of the left table, but if it is

341
00:09:02.150 --> 00:09:03.630
missing in the right one, then it leaves

342
00:09:03.630 --> 00:09:05.870
them and here it gives all the values

343
00:09:05.870 --> 00:09:09.490
of the right table even if it is

344
00:09:09.490 --> 00:09:11.910
not being used in the left Now here

345
00:09:11.910 --> 00:09:12.650
you can also use it with the where

346
00:09:12.650 --> 00:09:15.410
clause and if you want me to get

347
00:09:15.410 --> 00:09:18.030
only those entries where the order status is

348
00:09:18.030 --> 00:09:19.950
delivered, then you can use it.

349
00:09:20.250 --> 00:09:22.710
So yeah that was about joins in SQL,

350
00:09:22.910 --> 00:09:24.410
I hope you are enjoying it, I hope

351
00:09:24.410 --> 00:09:26.750
you have understood how this thing is used,

352
00:09:27.050 --> 00:09:28.750
thank you so much guys for watching this

353
00:09:28.750 --> 00:09:30.490
video and I will see you in the

354
00:09:30.490 --> 00:09:30.970
next one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.070 --> 00:00:02.190
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now I want to talk to

2
00:00:02.190 --> 00:00:04.430
you about what are indexes in mysql.

3
00:00:05.130 --> 00:00:07.750
Index basically makes your search fast.

4
00:00:08.530 --> 00:00:09.110
Have you seen a book?

5
00:00:09.730 --> 00:00:10.370
What happens in a book?

6
00:00:10.450 --> 00:00:11.290
Index is there in the starting.

7
00:00:11.950 --> 00:00:14.630
This index helps you to reach any particular

8
00:00:14.630 --> 00:00:15.190
place in the book.

9
00:00:16.050 --> 00:00:17.350
Suppose you want to go to chapter number

10
00:00:17.350 --> 00:00:17.830
11.

11
00:00:18.690 --> 00:00:19.990
So you will come to the index, you

12
00:00:19.990 --> 00:00:21.050
will see which page is chapter number 11.

13
00:00:22.230 --> 00:00:24.230
And after that, you will read chapter number

14
00:00:24.230 --> 00:00:24.550
11 by navigating on that page.

15
00:00:25.230 --> 00:00:28.010
So the way index helps in searching in

16
00:00:28.010 --> 00:00:31.229
any book, In the same way, index helps

17
00:00:31.229 --> 00:00:34.590
you to run select queries fast in mysql

18
00:00:34.590 --> 00:00:34.690
table.

19
00:00:34.950 --> 00:00:36.610
So your select queries become very fast.

20
00:00:37.410 --> 00:00:40.510
Now here, you have to use indexes when

21
00:00:40.510 --> 00:00:42.730
the table is read more than it is

22
00:00:42.730 --> 00:00:43.050
updated.

23
00:00:43.130 --> 00:00:44.250
It is a very important thing.

24
00:00:44.390 --> 00:00:44.950
What do people do?

25
00:00:45.130 --> 00:00:47.830
They make useless indexes.

26
00:00:47.970 --> 00:00:50.070
I want to tell you that if you

27
00:00:50.070 --> 00:00:52.670
use indexes, then your update queries will be

28
00:00:52.670 --> 00:00:53.030
slow.

29
00:00:53.610 --> 00:00:55.390
Your insert queries will be slow.

30
00:00:55.810 --> 00:00:57.090
Your delete operations will also be slow.

31
00:00:57.090 --> 00:00:59.930
So indexes make select queries faster.

32
00:01:00.090 --> 00:01:02.450
But slow down insert update and delete operations.

33
00:01:02.830 --> 00:01:04.230
And in most of the cases, this is

34
00:01:04.230 --> 00:01:04.630
okay.

35
00:01:04.870 --> 00:01:06.430
Because you want your user to get the

36
00:01:06.430 --> 00:01:06.890
data fast.

37
00:01:07.370 --> 00:01:11.470
You don't want your insert update or delete

38
00:01:11.470 --> 00:01:13.750
operations to be fast with your select.

39
00:01:14.050 --> 00:01:16.430
But you want your user to get the

40
00:01:16.430 --> 00:01:17.030
data on time.

41
00:01:17.410 --> 00:01:18.330
He is happy.

42
00:01:18.510 --> 00:01:19.570
Let me give you an example of this.

43
00:01:20.210 --> 00:01:21.330
Suppose you have a blog.

44
00:01:22.070 --> 00:01:23.370
You update the blog.

45
00:01:23.750 --> 00:01:24.490
Suppose it is updated in a second.

46
00:01:24.490 --> 00:01:26.730
By the way, one second is a really

47
00:01:26.730 --> 00:01:28.150
long time for updating a blog.

48
00:01:28.650 --> 00:01:29.790
Suppose it takes a second to complete the

49
00:01:29.790 --> 00:01:30.030
update.

50
00:01:30.630 --> 00:01:31.630
So it will work for you.

51
00:01:31.750 --> 00:01:33.910
Okay, sometimes I will update my blog.

52
00:01:34.310 --> 00:01:35.150
I don't have any problem.

53
00:01:35.630 --> 00:01:36.790
I will also hit insert sometimes.

54
00:01:37.150 --> 00:01:37.970
I wrote such a big blog.

55
00:01:38.470 --> 00:01:39.690
It took a second to insert.

56
00:01:39.890 --> 00:01:40.910
It will take a second once.

57
00:01:40.910 --> 00:01:41.450
That's fine.

58
00:01:41.890 --> 00:01:43.970
But if millions of users are visiting your

59
00:01:43.970 --> 00:01:44.610
website.

60
00:01:45.530 --> 00:01:48.690
And they think if one second to load

61
00:01:48.690 --> 00:01:48.790
the blog.

62
00:01:48.890 --> 00:01:50.370
Means it takes a second to load the

63
00:01:50.370 --> 00:01:50.870
blog on your page.

64
00:01:51.550 --> 00:01:52.450
And other things are also happening.

65
00:01:52.950 --> 00:01:53.950
Your UI will be loaded.

66
00:01:53.950 --> 00:01:54.690
Everything will happen.

67
00:01:54.850 --> 00:01:56.010
So your page will be very slow.

68
00:01:56.290 --> 00:01:57.350
So people will say that its site is

69
00:01:57.350 --> 00:01:57.570
slow.

70
00:01:57.990 --> 00:02:00.090
So you will want to prioritise this thing.

71
00:02:00.310 --> 00:02:01.290
That's why indexes are made.

72
00:02:02.050 --> 00:02:02.330
What is index?

73
00:02:02.850 --> 00:02:03.570
It is a data structure.

74
00:02:03.770 --> 00:02:05.890
That helps my SQL find rows quickly without

75
00:02:05.890 --> 00:02:07.370
scanning the entire table.

76
00:02:07.910 --> 00:02:09.090
You can treat it like an index page

77
00:02:09.090 --> 00:02:09.530
or a book.

78
00:02:10.650 --> 00:02:11.590
You can understand it by taking an analogy.

79
00:02:12.850 --> 00:02:12.990
Okay.

80
00:02:13.670 --> 00:02:14.750
Now how to make an index?

81
00:02:15.010 --> 00:02:15.950
We have an orders table.

82
00:02:16.070 --> 00:02:16.490
By the way, I will come to the

83
00:02:16.490 --> 00:02:16.970
orders table.

84
00:02:17.610 --> 00:02:19.910
And I will quickly select start from orders

85
00:02:19.910 --> 00:02:20.010
here.

86
00:02:20.130 --> 00:02:20.650
I will close it.

87
00:02:21.290 --> 00:02:22.230
Select start from orders.

88
00:02:22.470 --> 00:02:22.990
I will delete everything.

89
00:02:22.990 --> 00:02:25.430
And here I will write select start from

90
00:02:25.430 --> 00:02:25.690
orders.

91
00:02:26.390 --> 00:02:27.390
By the way, I want to tell you

92
00:02:27.390 --> 00:02:29.530
that all the queries we are writing here.

93
00:02:29.770 --> 00:02:30.910
You will get all those queries in the

94
00:02:30.910 --> 00:02:31.350
handbook.

95
00:02:32.050 --> 00:02:33.990
You can copy paste from there.

96
00:02:34.450 --> 00:02:35.710
You have all the arrangements for everything.

97
00:02:36.130 --> 00:02:37.850
So you don't have to take any trouble.

98
00:02:37.970 --> 00:02:39.630
So this is our data basically.

99
00:02:39.750 --> 00:02:40.190
You can see.

100
00:02:40.710 --> 00:02:42.890
And here you see we have customer data.

101
00:02:43.350 --> 00:02:44.830
Now I want to tell you one thing

102
00:02:44.830 --> 00:02:45.410
before moving forward.

103
00:02:46.290 --> 00:02:47.590
Whenever you make a primary key.

104
00:02:48.070 --> 00:02:48.830
Like you have made the order ID as

105
00:02:48.830 --> 00:02:49.490
a primary key.

106
00:02:49.850 --> 00:02:50.850
If you come here and click on the

107
00:02:50.850 --> 00:02:51.590
orders table.

108
00:02:51.590 --> 00:02:54.090
Then see our order ID is of primary

109
00:02:54.090 --> 00:02:54.290
key.

110
00:02:54.390 --> 00:02:54.630
You have to write PK.

111
00:02:54.990 --> 00:02:55.730
But it is of primary key.

112
00:02:55.830 --> 00:02:56.230
There is an integer.

113
00:02:56.470 --> 00:02:57.030
There is auto increment.

114
00:02:57.210 --> 00:02:57.830
It is of primary key.

115
00:02:58.190 --> 00:02:59.310
So this order ID.

116
00:02:59.490 --> 00:03:00.470
Its index is already made.

117
00:03:01.490 --> 00:03:01.930
Okay.

118
00:03:02.090 --> 00:03:02.930
The index is made.

119
00:03:03.590 --> 00:03:03.870
Yes.

120
00:03:03.990 --> 00:03:04.670
Your index is made.

121
00:03:05.070 --> 00:03:05.550
You see.

122
00:03:05.630 --> 00:03:06.190
Here you will click.

123
00:03:06.350 --> 00:03:07.770
Your primary key index is made.

124
00:03:08.190 --> 00:03:08.350
Okay.

125
00:03:09.030 --> 00:03:09.390
But.

126
00:03:10.130 --> 00:03:10.790
Assume you find yourself.

127
00:03:11.770 --> 00:03:12.990
That you are searching more city wise.

128
00:03:14.090 --> 00:03:16.350
Or let's say you are searching more order

129
00:03:16.350 --> 00:03:16.930
date wise.

130
00:03:17.870 --> 00:03:19.010
Or let's say you are searching more order

131
00:03:19.010 --> 00:03:19.730
status wise.

132
00:03:19.730 --> 00:03:20.290
Or let's say you are searching city wise.

133
00:03:20.670 --> 00:03:21.550
The thing you are searching by putting it

134
00:03:21.550 --> 00:03:21.870
in where.

135
00:03:22.930 --> 00:03:23.650
Make the index of that thing.

136
00:03:24.050 --> 00:03:25.410
That query will be fast for you.

137
00:03:25.790 --> 00:03:27.350
Assume you find yourself searching city wise.

138
00:03:28.610 --> 00:03:29.090
So you say.

139
00:03:29.350 --> 00:03:30.590
I want to make an index on city.

140
00:03:31.030 --> 00:03:31.670
So you say here.

141
00:03:31.750 --> 00:03:32.530
Create index.

142
00:03:32.910 --> 00:03:34.010
Keep any name of index.

143
00:03:34.150 --> 00:03:34.910
You will also write your name.

144
00:03:35.110 --> 00:03:35.350
It will work.

145
00:03:35.450 --> 00:03:37.590
But idx underscore order underscore city is a

146
00:03:37.590 --> 00:03:38.210
standard name.

147
00:03:38.690 --> 00:03:39.630
And you are making it in the orders

148
00:03:39.630 --> 00:03:39.930
table.

149
00:03:40.530 --> 00:03:41.210
And you are making it on city.

150
00:03:41.310 --> 00:03:41.570
You are saying.

151
00:03:41.630 --> 00:03:41.950
Make it on city.

152
00:03:42.410 --> 00:03:43.810
Means make the index on this column.

153
00:03:44.350 --> 00:03:44.870
And on this column.

154
00:03:45.070 --> 00:03:45.530
You will make.

155
00:03:45.970 --> 00:03:46.210
If.

156
00:03:46.650 --> 00:03:46.970
Your index.

157
00:03:47.150 --> 00:03:48.590
So whenever you will search from this column.

158
00:03:48.850 --> 00:03:49.430
It will be very fast.

159
00:03:49.810 --> 00:03:50.970
So I want to show you people here.

160
00:03:52.570 --> 00:03:53.130
By the way.

161
00:03:53.230 --> 00:03:53.890
I will tell you one more thing.

162
00:03:54.230 --> 00:03:56.530
That this query is already very fast.

163
00:03:56.730 --> 00:03:57.110
Means see.

164
00:03:57.150 --> 00:03:58.250
If you run select query here.

165
00:03:58.350 --> 00:03:58.530
Then see.

166
00:03:58.550 --> 00:03:59.770
0.000 second.

167
00:04:00.330 --> 00:04:01.450
This data is so less.

168
00:04:01.650 --> 00:04:02.110
According to SQL.

169
00:04:03.010 --> 00:04:04.010
That you will not even know.

170
00:04:04.090 --> 00:04:04.970
That your query is getting fast.

171
00:04:05.570 --> 00:04:06.610
But if you have.

172
00:04:06.750 --> 00:04:07.530
Very big data.

173
00:04:07.690 --> 00:04:08.650
You have millions of rows.

174
00:04:09.050 --> 00:04:09.330
After that.

175
00:04:09.450 --> 00:04:09.770
If you search.

176
00:04:09.950 --> 00:04:10.530
Then you will know.

177
00:04:10.690 --> 00:04:12.830
How fast is our query.

178
00:04:13.110 --> 00:04:13.930
Where we are.

179
00:04:14.010 --> 00:04:14.650
Where city.

180
00:04:15.230 --> 00:04:16.310
Equals to let's say.

181
00:04:16.649 --> 00:04:16.950
City.

182
00:04:16.950 --> 00:04:17.730
Okay.

183
00:04:31.990 --> 00:04:33.010
But.

184
00:04:34.310 --> 00:04:36.350
But.

185
00:04:43.890 --> 00:04:45.930
But.

186
00:04:45.930 --> 00:04:46.090
But.

187
00:04:46.090 --> 00:04:46.190
But.

188
00:04:46.190 --> 00:04:46.290
But.

189
00:04:46.290 --> 00:04:46.390
But.

190
00:04:46.390 --> 00:04:47.250
But.

191
00:04:48.530 --> 00:04:50.610
But.

192
00:04:52.010 --> 00:04:53.910
But.

193
00:04:54.930 --> 00:04:57.010
But.

194
00:04:57.010 --> 00:04:58.050
But.

195
00:04:58.170 --> 00:05:00.150
But.

196
00:05:00.150 --> 00:05:01.610
But.

197
00:05:06.030 --> 00:05:08.110
But.

198
00:05:09.310 --> 00:05:11.390
But.

199
00:05:13.710 --> 00:05:14.490
But.

200
00:05:14.510 --> 00:05:14.610
But.

201
00:05:15.370 --> 00:05:15.890
But.

202
00:05:15.890 --> 00:05:16.410
But.

203
00:05:48.690 --> 00:05:49.650
But.

204
00:05:52.950 --> 00:05:53.370
But.

205
00:05:54.250 --> 00:05:55.210
But.

206
00:05:57.450 --> 00:05:57.750
But.

207
00:05:59.210 --> 00:06:00.170
But.

208
00:06:02.350 --> 00:06:03.310
But.

209
00:06:15.770 --> 00:06:15.870
But.

210
00:06:15.870 --> 00:06:15.970
But.

211
00:06:15.970 --> 00:06:16.070
But.

212
00:06:16.070 --> 00:06:16.170
But.

213
00:06:16.170 --> 00:06:16.770
But.

214
00:06:26.590 --> 00:06:31.470
But.

215
00:06:41.750 --> 00:06:45.830
But.

216
00:06:45.830 --> 00:06:46.230
But.

217
00:06:46.230 --> 00:06:46.330
But.

218
00:06:55.550 --> 00:06:58.830
But.

219
00:07:14.170 --> 00:07:15.810
But.

220
00:07:16.430 --> 00:07:18.550
Insert a lot of data in your table,

221
00:07:19.170 --> 00:07:21.690
by using insert, you can take the help

222
00:07:21.690 --> 00:07:24.110
of videos that I have made, you can

223
00:07:24.110 --> 00:07:26.610
go to the previous videos, and the data

224
00:07:26.610 --> 00:07:27.890
that we inserted, you can increase the script,

225
00:07:29.150 --> 00:07:31.470
maybe you do Amish Sharma 2, Delhi 2,

226
00:07:31.990 --> 00:07:32.930
or write the name of some other city,

227
00:07:33.510 --> 00:07:35.750
and generate a big data, you can even

228
00:07:35.750 --> 00:07:37.910
take help of chat GPT, you play chat

229
00:07:37.910 --> 00:07:39.790
GPT, and tell chat GPT to give me

230
00:07:39.790 --> 00:07:42.070
a very big data, which may be 10

231
00:07:42.070 --> 00:07:45.370
,000 rows, and you use it to insert

232
00:07:45.370 --> 00:07:48.450
in your database, and then compare your query

233
00:07:48.450 --> 00:07:50.310
performance, you will have a lot of fun,

234
00:07:50.770 --> 00:07:53.050
and your concept will be clear, so you

235
00:07:53.050 --> 00:07:56.310
have to do this exercise yourself, when not

236
00:07:56.310 --> 00:07:58.550
to use indexes, column with very few unique

237
00:07:58.550 --> 00:08:00.790
values, table with frequent updates, if you want

238
00:08:00.790 --> 00:08:02.590
to optimise the update, then don't do it,

239
00:08:02.630 --> 00:08:04.330
there is no difference between small tables, you

240
00:08:04.330 --> 00:08:05.890
can see here, it was 0, it is

241
00:08:05.890 --> 00:08:09.190
0, so there is no problem, so if

242
00:08:09.190 --> 00:08:11.250
everything is already fast, then why do you

243
00:08:11.250 --> 00:08:13.290
have to do it, indexes are not free,

244
00:08:13.830 --> 00:08:15.970
I am not talking about free money, they

245
00:08:15.970 --> 00:08:20.010
trade write performance for read speed, you are

246
00:08:20.010 --> 00:08:21.710
improving your read speed by spoiling write performance,

247
00:08:22.090 --> 00:08:23.850
it is a simple thing, you are not

248
00:08:23.850 --> 00:08:25.590
doing any magic by creating index, if there

249
00:08:25.590 --> 00:08:28.030
was magic by creating index, then MySQL would

250
00:08:28.030 --> 00:08:30.210
have done it by default for you, but

251
00:08:30.210 --> 00:08:32.350
because it has given you an option, so

252
00:08:32.350 --> 00:08:34.470
if you want to do this work, you

253
00:08:34.470 --> 00:08:35.870
want to speed up your read speed and

254
00:08:35.870 --> 00:08:39.530
spoil your write performance, it will work in

255
00:08:39.530 --> 00:08:41.070
your use case, that thing is fit battery,

256
00:08:41.169 --> 00:08:44.050
which is fine, then do it, it is

257
00:08:44.050 --> 00:08:47.170
a simple thing, now to remove index, you

258
00:08:47.170 --> 00:08:49.490
can do drop index, and your index will

259
00:08:49.490 --> 00:08:51.010
be deleted, so what I will do here,

260
00:08:51.150 --> 00:08:53.650
I will drop this, and I will drop

261
00:08:53.650 --> 00:08:54.370
this also, so I will do one thing,

262
00:08:54.970 --> 00:08:57.030
I will comment out this, and I will

263
00:08:57.030 --> 00:09:01.250
comment out this also, and I will drop

264
00:09:01.250 --> 00:09:03.470
both indexes, so what I will do here,

265
00:09:03.470 --> 00:09:07.770
so what I will do here, I will

266
00:09:07.770 --> 00:09:12.610
drop both indexes, so what I will do

267
00:09:12.610 --> 00:09:14.030
here, I will drop both indexes, so what

268
00:09:14.030 --> 00:09:15.150
I will do here, I will drop both

269
00:09:15.150 --> 00:09:17.030
indexes, so what I will do here, I

270
00:09:17.030 --> 00:09:19.890
will drop both indexes, so what I will

271
00:09:19.890 --> 00:09:21.070
do here, I will drop both indexes, so

272
00:09:21.070 --> 00:09:22.050
what I will do here, I will drop

273
00:09:22.050 --> 00:09:24.430
both indexes, so what I will do here,

274
00:09:24.430 --> 00:09:25.190
I will drop both indexes,



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.010 --> 00:00:02.890
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Now, we will see the concept of views

2
00:00:02.890 --> 00:00:05.230
in MySQL, which is very simple and straightforward.

3
00:00:05.590 --> 00:00:06.610
You will say that this is a select

4
00:00:06.610 --> 00:00:06.950
query.

5
00:00:07.390 --> 00:00:08.830
This is exactly what we have read in

6
00:00:08.830 --> 00:00:09.350
the select query.

7
00:00:09.850 --> 00:00:11.070
Yes, it is exactly the same.

8
00:00:11.630 --> 00:00:12.510
But it is also important to know this

9
00:00:12.510 --> 00:00:13.570
concept.

10
00:00:13.990 --> 00:00:15.090
Now see what happens here.

11
00:00:15.630 --> 00:00:17.590
A view is a saved SQL query that

12
00:00:17.590 --> 00:00:19.650
behaves like a virtual table.

13
00:00:20.350 --> 00:00:21.950
This is not a real table, but it

14
00:00:21.950 --> 00:00:22.550
behaves like a table.

15
00:00:23.450 --> 00:00:26.270
It does not store data, but behaves like

16
00:00:26.270 --> 00:00:28.090
a table by storing the query.

17
00:00:28.090 --> 00:00:30.590
Now I will give you a very realistic

18
00:00:30.590 --> 00:00:31.330
example.

19
00:00:31.810 --> 00:00:33.110
Let's say I make a complex query.

20
00:00:33.790 --> 00:00:36.430
Let's say I say that this is my

21
00:00:36.430 --> 00:00:36.810
query.

22
00:00:37.070 --> 00:00:38.010
I delete it.

23
00:00:38.110 --> 00:00:38.370
I delete everything.

24
00:00:39.250 --> 00:00:40.330
I say this is my query.

25
00:00:40.530 --> 00:00:42.590
I say that where city is equal to

26
00:00:42.590 --> 00:00:44.690
Delhi and my order status is delivered.

27
00:00:45.030 --> 00:00:45.890
I run this query.

28
00:00:47.290 --> 00:00:49.070
And I say one more thing here.

29
00:00:49.190 --> 00:00:51.810
I will add one more thing here.

30
00:00:51.810 --> 00:00:54.950
And I will say here simply that either

31
00:00:54.950 --> 00:00:59.990
this is it or city equals to let's

32
00:00:59.990 --> 00:01:00.430
say.

33
00:01:00.650 --> 00:01:02.010
What else did we have?

34
00:01:02.330 --> 00:01:02.910
Was it Ahmedabad?

35
00:01:03.690 --> 00:01:04.690
No, it was not Ahmedabad.

36
00:01:04.950 --> 00:01:05.350
Was it Bangalore?

37
00:01:05.630 --> 00:01:06.450
No, it was not Bangalore either.

38
00:01:06.530 --> 00:01:08.110
It was Mumbai as far as I remember.

39
00:01:08.950 --> 00:01:10.130
Now I will run this.

40
00:01:10.450 --> 00:01:12.870
So I also have city Mumbai here.

41
00:01:13.910 --> 00:01:16.690
Now I have written a complex SQL query.

42
00:01:17.710 --> 00:01:18.810
I can also write it like this by

43
00:01:18.810 --> 00:01:19.050
the way.

44
00:01:20.030 --> 00:01:20.670
It becomes a little readable.

45
00:01:21.390 --> 00:01:22.890
So I have written this query.

46
00:01:23.150 --> 00:01:24.690
But I don't want to write it again

47
00:01:24.690 --> 00:01:24.990
and again.

48
00:01:25.290 --> 00:01:26.830
I want it to behave like a table.

49
00:01:28.270 --> 00:01:29.550
I mean this query should behave like a

50
00:01:29.550 --> 00:01:29.830
table.

51
00:01:30.910 --> 00:01:31.830
So what I will do is I will

52
00:01:31.830 --> 00:01:32.870
make a view of this query.

53
00:01:33.150 --> 00:01:36.450
So I will say create view delivered orders

54
00:01:36.450 --> 00:01:39.870
as and your select query whatever it is.

55
00:01:40.690 --> 00:01:42.590
Whatever it is, it will become a view.

56
00:01:43.490 --> 00:01:44.310
I do one thing here.

57
00:01:44.430 --> 00:01:46.670
I name this view clients.

58
00:01:46.670 --> 00:01:49.610
So what I will simply do is I

59
00:01:49.610 --> 00:01:50.710
will say create view clients.

60
00:01:50.970 --> 00:01:53.730
So I will write create view here.

61
00:01:54.010 --> 00:01:55.670
And I will name this view clients.

62
00:01:57.090 --> 00:01:57.530
I do one thing.

63
00:01:57.770 --> 00:01:58.450
I name it clients.

64
00:01:59.490 --> 00:02:02.410
I name it tell underscore mum underscore clients.

65
00:02:02.710 --> 00:02:03.950
I mean these are Delhi Mumbai clients of

66
00:02:03.950 --> 00:02:04.070
mine.

67
00:02:05.190 --> 00:02:06.490
And what do I want to make a

68
00:02:06.490 --> 00:02:06.910
view of here?

69
00:02:07.810 --> 00:02:09.810
I want to make a view of this

70
00:02:09.810 --> 00:02:10.310
select query.

71
00:02:10.450 --> 00:02:11.650
So I will write here as.

72
00:02:11.990 --> 00:02:12.290
Okay.

73
00:02:12.930 --> 00:02:13.570
This is the syntax.

74
00:02:14.170 --> 00:02:14.630
This is the syntax.

75
00:02:14.630 --> 00:02:17.190
Don't run after remembering the syntax at all.

76
00:02:17.630 --> 00:02:18.810
This chat gpt will also give you.

77
00:02:19.210 --> 00:02:20.970
I mean I am telling you very realistically.

78
00:02:21.370 --> 00:02:21.950
Understand things.

79
00:02:22.250 --> 00:02:22.370
Okay.

80
00:02:23.050 --> 00:02:23.810
What will happen if I run it?

81
00:02:25.230 --> 00:02:26.010
Nothing happened.

82
00:02:27.130 --> 00:02:28.010
Something happened.

83
00:02:28.330 --> 00:02:28.710
What happened?

84
00:02:29.070 --> 00:02:29.710
A view has been made.

85
00:02:29.930 --> 00:02:31.010
You refresh it here.

86
00:02:31.470 --> 00:02:33.210
And now you do one thing here.

87
00:02:33.950 --> 00:02:35.270
You come to your orders table.

88
00:02:35.950 --> 00:02:38.710
And after that you come to views.

89
00:02:39.050 --> 00:02:39.470
Come here.

90
00:02:39.750 --> 00:02:40.690
You come to ecom in views.

91
00:02:41.090 --> 00:02:41.230
Okay.

92
00:02:41.790 --> 00:02:42.610
Delhi Mumbai clients.

93
00:02:42.610 --> 00:02:45.010
So there are tables in the ecom database.

94
00:02:46.510 --> 00:02:47.010
And there are views.

95
00:02:47.330 --> 00:02:47.830
What are the views?

96
00:02:48.370 --> 00:02:49.810
One view is Delhi Mumbai clients.

97
00:02:50.590 --> 00:02:50.790
Okay.

98
00:02:50.930 --> 00:02:53.530
Can I query Delhi Mumbai clients in this

99
00:02:53.530 --> 00:02:53.970
way?

100
00:02:54.690 --> 00:02:55.650
Can I say this way?

101
00:02:56.070 --> 00:03:00.870
Select star from Delhi Mumbai clients.

102
00:03:02.050 --> 00:03:02.610
Yes.

103
00:03:02.790 --> 00:03:03.370
I can do this.

104
00:03:03.930 --> 00:03:05.550
And it will behave exactly like a table.

105
00:03:06.390 --> 00:03:07.230
This is not actually a table.

106
00:03:07.550 --> 00:03:08.950
But it will update like a real-time

107
00:03:08.950 --> 00:03:09.390
table.

108
00:03:10.510 --> 00:03:10.950
Sorry.

109
00:03:10.950 --> 00:03:12.430
It will behave like a real-time table.

110
00:03:12.470 --> 00:03:15.070
And if I change anything like this.

111
00:03:15.390 --> 00:03:17.270
In my original orders table.

112
00:03:17.950 --> 00:03:18.110
For example.

113
00:03:18.890 --> 00:03:19.770
I am saying that by changing the name

114
00:03:19.770 --> 00:03:20.290
of Amish Sharma.

115
00:03:21.730 --> 00:03:23.590
I will change it to Dr. Amish Sharma.

116
00:03:23.770 --> 00:03:23.890
Okay.

117
00:03:24.610 --> 00:03:27.450
So will it show me in this too?

118
00:03:27.850 --> 00:03:28.770
Do you understand what I am saying?

119
00:03:28.870 --> 00:03:29.250
What is my question?

120
00:03:29.790 --> 00:03:30.530
My question is.

121
00:03:30.950 --> 00:03:32.390
That I run update query.

122
00:03:32.990 --> 00:03:34.050
I say update.

123
00:03:34.690 --> 00:03:36.630
And let's say I want to update.

124
00:03:37.190 --> 00:03:37.750
Orders.

125
00:03:38.370 --> 00:03:38.570
Okay.

126
00:03:38.970 --> 00:03:39.590
And I say.

127
00:03:39.590 --> 00:03:40.730
Set.

128
00:03:42.290 --> 00:03:43.350
Customer name.

129
00:03:44.490 --> 00:03:45.290
And let's say.

130
00:03:46.390 --> 00:03:47.430
I want to change it to Dr. Amit.

131
00:03:48.430 --> 00:03:48.550
Okay.

132
00:03:50.870 --> 00:03:51.830
Dr. Amit.

133
00:03:52.670 --> 00:03:53.970
And I set this.

134
00:03:54.070 --> 00:03:54.490
And I say.

135
00:03:54.670 --> 00:03:54.930
Where.

136
00:03:56.450 --> 00:03:59.710
Order underscore ID is equal to one.

137
00:04:00.650 --> 00:04:01.290
I run this update.

138
00:04:01.870 --> 00:04:03.090
And I will comment this out.

139
00:04:03.790 --> 00:04:04.930
So I run this update.

140
00:04:05.170 --> 00:04:05.670
So it got updated.

141
00:04:05.950 --> 00:04:06.110
Okay.

142
00:04:06.610 --> 00:04:08.010
And my original orders table must have been

143
00:04:08.010 --> 00:04:08.350
updated.

144
00:04:09.210 --> 00:04:09.450
Exactly.

145
00:04:09.570 --> 00:04:11.630
Do you agree or not?

146
00:04:11.890 --> 00:04:12.070
Yes.

147
00:04:12.250 --> 00:04:12.650
You said yes.

148
00:04:12.690 --> 00:04:13.030
I agree.

149
00:04:13.270 --> 00:04:13.370
Absolutely.

150
00:04:13.470 --> 00:04:13.670
Do you agree?

151
00:04:14.790 --> 00:04:15.970
Will Delmum clients be updated?

152
00:04:16.149 --> 00:04:16.930
The answer is yes.

153
00:04:17.610 --> 00:04:18.470
The answer is yes.

154
00:04:18.670 --> 00:04:19.709
You see Dr. Amit is here.

155
00:04:19.910 --> 00:04:21.890
So it is behaving like a table.

156
00:04:22.210 --> 00:04:22.610
But.

157
00:04:23.670 --> 00:04:24.690
It is running a query behind the scenes.

158
00:04:25.810 --> 00:04:26.830
And it is giving you a convenience.

159
00:04:27.170 --> 00:04:27.310
I mean.

160
00:04:27.370 --> 00:04:29.050
You said only Delmum clients.

161
00:04:30.130 --> 00:04:31.690
A very big query is working behind it.

162
00:04:32.090 --> 00:04:33.610
And this query can be very complex.

163
00:04:34.030 --> 00:04:35.470
I have written a very simple query right

164
00:04:35.470 --> 00:04:35.570
now.

165
00:04:35.990 --> 00:04:37.310
But now the query I have written.

166
00:04:37.510 --> 00:04:38.570
Where city is equal to Delhi.

167
00:04:38.670 --> 00:04:39.550
And order status is equal to Delhi.

168
00:04:39.550 --> 00:04:41.190
Or city is equal to Mumbai.

169
00:04:41.510 --> 00:04:43.070
What I have written is a very simple

170
00:04:43.070 --> 00:04:43.390
thing.

171
00:04:44.170 --> 00:04:45.250
In your life.

172
00:04:45.690 --> 00:04:47.930
In your data analyst journey.

173
00:04:48.910 --> 00:04:50.830
You will get to see such dangerous queries.

174
00:04:51.470 --> 00:04:51.830
You will say.

175
00:04:51.890 --> 00:04:52.290
What is a query?

176
00:04:52.910 --> 00:04:54.210
And today is the age of AI.

177
00:04:54.530 --> 00:04:55.570
AI makes such a good query.

178
00:04:56.070 --> 00:04:56.950
And it also checks the query.

179
00:04:57.510 --> 00:04:58.550
You give the query to AI.

180
00:04:59.070 --> 00:04:59.490
And say.

181
00:04:59.570 --> 00:05:00.570
Explain the query to me.

182
00:05:00.610 --> 00:05:01.630
We will come to that thing too.

183
00:05:01.970 --> 00:05:02.690
But I am telling you.

184
00:05:03.090 --> 00:05:03.990
So what happens in this.

185
00:05:04.130 --> 00:05:04.990
That you people.

186
00:05:05.630 --> 00:05:06.190
In some way.

187
00:05:06.550 --> 00:05:06.990
Easily.

188
00:05:07.130 --> 00:05:07.690
You will be able to query.

189
00:05:08.350 --> 00:05:08.610
Okay.

190
00:05:09.270 --> 00:05:09.970
Now here.

191
00:05:10.010 --> 00:05:10.890
The example I have taken in the handbook.

192
00:05:11.570 --> 00:05:12.350
That is of delivered order.

193
00:05:12.550 --> 00:05:12.650
Means.

194
00:05:12.870 --> 00:05:14.930
I am taking all those orders.

195
00:05:15.490 --> 00:05:16.690
Where the status is delivered.

196
00:05:16.870 --> 00:05:18.250
And I am selecting only a few columns

197
00:05:18.250 --> 00:05:18.390
of it.

198
00:05:19.130 --> 00:05:19.350
Okay.

199
00:05:19.690 --> 00:05:20.550
We have made a view.

200
00:05:20.910 --> 00:05:21.490
In the name of delivered orders.

201
00:05:22.250 --> 00:05:23.130
Then what did we do?

202
00:05:23.450 --> 00:05:24.830
We saw it.

203
00:05:25.010 --> 00:05:25.310
That brother.

204
00:05:25.770 --> 00:05:26.950
Is showing or not.

205
00:05:27.050 --> 00:05:27.570
So we do one thing.

206
00:05:27.810 --> 00:05:28.250
Let's do this.

207
00:05:28.250 --> 00:05:28.590
Okay.

208
00:05:29.550 --> 00:05:30.150
So I erase everything.

209
00:05:30.570 --> 00:05:31.090
I erase everything.

210
00:05:31.650 --> 00:05:32.750
And what will I do here?

211
00:05:34.230 --> 00:05:35.030
Create view.

212
00:05:35.210 --> 00:05:35.930
Delivered orders.

213
00:05:36.170 --> 00:05:36.490
As.

214
00:05:37.190 --> 00:05:37.690
And then after that.

215
00:05:37.830 --> 00:05:38.150
I ran a query.

216
00:05:38.510 --> 00:05:38.610
And here.

217
00:05:38.610 --> 00:05:40.090
After this.

218
00:05:40.510 --> 00:05:40.750
Let's do one thing.

219
00:05:40.950 --> 00:05:41.170
We say.

220
00:05:41.470 --> 00:05:42.550
Select star from.

221
00:05:42.810 --> 00:05:44.070
Select star from.

222
00:05:46.430 --> 00:05:46.910
Delivered.

223
00:05:47.130 --> 00:05:47.610
Underscore.

224
00:05:47.830 --> 00:05:48.190
Orders.

225
00:05:48.310 --> 00:05:48.410
Okay.

226
00:05:48.890 --> 00:05:49.750
We will run this query.

227
00:05:50.190 --> 00:05:50.990
Something like this.

228
00:05:51.430 --> 00:05:51.610
We.

229
00:05:51.610 --> 00:05:52.230
By the way.

230
00:05:52.270 --> 00:05:52.710
I have done Dr. Amit.

231
00:05:52.950 --> 00:05:53.670
Dr. Amit is visible.

232
00:05:54.050 --> 00:05:54.250
Okay.

233
00:05:54.530 --> 00:05:54.990
We have.

234
00:05:55.110 --> 00:05:55.870
Delivered orders.

235
00:05:56.110 --> 00:05:56.450
All.

236
00:05:56.550 --> 00:05:56.790
All.

237
00:05:56.970 --> 00:05:57.070
The.

238
00:05:58.170 --> 00:05:58.650
Values.

239
00:05:58.770 --> 00:05:59.310
We get to see.

240
00:05:59.530 --> 00:05:59.950
Basically.

241
00:06:00.170 --> 00:06:01.830
Behind the scenes.

242
00:06:01.970 --> 00:06:02.490
This is the query.

243
00:06:02.950 --> 00:06:03.390
This.

244
00:06:03.450 --> 00:06:04.270
This is the query.

245
00:06:04.630 --> 00:06:05.650
This is our view.

246
00:06:05.850 --> 00:06:06.230
Delivered.

247
00:06:06.310 --> 00:06:06.530
Orders.

248
00:06:06.790 --> 00:06:06.950
And.

249
00:06:08.210 --> 00:06:09.410
We select all these orders.

250
00:06:11.150 --> 00:06:11.590
Data.

251
00:06:11.790 --> 00:06:12.190
Okay.

252
00:06:12.690 --> 00:06:13.130
So.

253
00:06:13.490 --> 00:06:13.590
Now.

254
00:06:13.670 --> 00:06:14.530
We have selected everything from delivered orders.

255
00:06:16.230 --> 00:06:16.670
After this.

256
00:06:17.250 --> 00:06:18.070
What can we do?

257
00:06:18.470 --> 00:06:18.750
We.

258
00:06:19.050 --> 00:06:19.490
Delivered.

259
00:06:19.570 --> 00:06:19.730
Order.

260
00:06:19.850 --> 00:06:20.730
Can be used like a table.

261
00:06:21.410 --> 00:06:21.850
But.

262
00:06:22.030 --> 00:06:22.530
I want to tell you one more thing

263
00:06:22.530 --> 00:06:23.390
here.

264
00:06:24.090 --> 00:06:25.270
Can I update it?

265
00:06:25.750 --> 00:06:26.110
You will say.

266
00:06:26.150 --> 00:06:26.430
One minute.

267
00:06:26.650 --> 00:06:27.210
This is not a real table.

268
00:06:27.550 --> 00:06:28.270
This is not an original table.

269
00:06:28.590 --> 00:06:29.350
This is not a real table.

270
00:06:29.550 --> 00:06:30.630
This is a virtual table.

271
00:08:31.870 --> 00:08:33.130
Select start from orders.

272
00:08:34.510 --> 00:08:34.710
And

273
00:08:34.710 --> 00:08:47.630
let

274
00:08:47.630 --> 00:08:54.430
me do something.

275
00:09:01.230 --> 00:09:04.850
So you can try it out by copying

276
00:09:04.850 --> 00:09:06.690
it, everything is there in the handbook, I

277
00:09:06.690 --> 00:09:08.690
have also given you the code, you will

278
00:09:08.690 --> 00:09:10.450
get everything, you will get it with convenience.

279
00:09:11.610 --> 00:09:13.910
Now you can drop the view just like

280
00:09:13.910 --> 00:09:14.810
you drop the table.

281
00:09:16.410 --> 00:09:18.770
Delivered underscore orders was the name of the

282
00:09:18.770 --> 00:09:20.430
view, let me refresh it.

283
00:09:20.570 --> 00:09:21.990
One was delivered orders and the other was

284
00:09:21.990 --> 00:09:22.730
Del Mum Clients.

285
00:09:23.190 --> 00:09:25.290
So I delete the delivered orders first and

286
00:09:25.290 --> 00:09:26.090
see if it is deleted or not.

287
00:09:26.090 --> 00:09:27.010
It is here, there is no need to

288
00:09:27.010 --> 00:09:27.970
refresh it.

289
00:09:29.290 --> 00:09:31.210
Let's do Del Mum Clients too.

290
00:09:34.120 --> 00:09:36.960
So I will write drop view and I

291
00:09:36.960 --> 00:09:41.060
will do Del Mum Clients here.

292
00:09:42.420 --> 00:09:45.020
I will run it and it is giving

293
00:09:45.020 --> 00:09:45.940
me an error in delivered orders, it is

294
00:09:45.940 --> 00:09:47.060
saying that there are no delivered orders.

295
00:09:47.780 --> 00:09:49.160
So what do you want to drop?

296
00:09:50.100 --> 00:09:51.500
So let's do one thing here, let's run

297
00:09:51.500 --> 00:09:53.500
it and see here Del Mum Clients has

298
00:09:53.500 --> 00:09:53.800
been deleted.

299
00:09:54.660 --> 00:09:55.940
So we have nothing in views.

300
00:09:55.940 --> 00:09:59.800
So yeah, that was views in MySQL.

301
00:10:00.520 --> 00:10:01.500
Why will you use views?

302
00:10:01.860 --> 00:10:03.760
You will reuse complex queries, you will improve

303
00:10:03.760 --> 00:10:07.580
readability, you will restrict access for sensitive columns.

304
00:10:07.840 --> 00:10:11.340
Sometimes you want that your queries do not

305
00:10:11.340 --> 00:10:13.860
run by mistake so that you update the

306
00:10:13.860 --> 00:10:14.600
sensitive columns.

307
00:10:15.440 --> 00:10:16.680
Then you can keep the business logic in

308
00:10:16.680 --> 00:10:17.040
one place.

309
00:10:17.680 --> 00:10:19.080
Suppose you have made a query, you have

310
00:10:19.080 --> 00:10:21.080
used a very complex logic and you do

311
00:10:21.080 --> 00:10:22.940
not want every employee to use that logic

312
00:10:22.940 --> 00:10:23.080
again and again.

313
00:10:23.080 --> 00:10:25.040
Let's say I want to fetch last year's

314
00:10:25.040 --> 00:10:28.760
orders where the price per unit is less

315
00:10:28.760 --> 00:10:32.700
than 65,000 and along with that there

316
00:10:32.700 --> 00:10:33.500
are some other conditions.

317
00:10:33.740 --> 00:10:35.080
So I made a query, made a view

318
00:10:35.080 --> 00:10:36.720
of it and then I told my employees

319
00:10:36.720 --> 00:10:38.340
to work on these views.

320
00:10:38.600 --> 00:10:40.360
You do not make business logic again and

321
00:10:40.360 --> 00:10:41.500
again because they are humans, they will make

322
00:10:41.500 --> 00:10:41.600
mistakes.

323
00:10:42.380 --> 00:10:44.940
Even if they use AI, they make mistakes,

324
00:10:45.280 --> 00:10:46.240
humans make mistakes.

325
00:10:46.240 --> 00:10:48.720
By the way, AI also makes mistakes.

326
00:10:49.100 --> 00:10:50.160
AI also hallucinates.

327
00:10:50.420 --> 00:10:51.860
You should also know that if you ask

328
00:10:51.860 --> 00:10:53.940
something to AI, that answer will not be

329
00:10:53.940 --> 00:10:54.820
100% correct.

330
00:10:56.040 --> 00:10:58.460
Yes, but by using AI to a large

331
00:10:58.460 --> 00:11:00.480
extent, you will understand what AI can do

332
00:11:00.480 --> 00:11:01.280
right and what it can do wrong.

333
00:11:01.740 --> 00:11:03.660
So the limits of AI will be cleared

334
00:11:03.660 --> 00:11:05.700
very well as you use it.

335
00:11:06.700 --> 00:11:08.540
I hope you are enjoying this course so

336
00:11:08.540 --> 00:11:08.840
far.

337
00:11:14.660 --> 00:11:16.940
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.200 --> 00:00:02.420
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, I just woke up and as

2
00:00:02.420 --> 00:00:03.560
soon as I woke up, I didn't feel

3
00:00:03.560 --> 00:00:04.120
like doing anything.

4
00:00:04.760 --> 00:00:07.360
I directly opened my MySQL workbench here.

5
00:00:07.360 --> 00:00:08.940
I am so excited to make these videos.

6
00:00:09.820 --> 00:00:12.520
Here I will put the password and after

7
00:00:12.520 --> 00:00:13.960
that my MySQL workbench will open.

8
00:00:14.580 --> 00:00:16.420
And here what I will do is, I

9
00:00:16.420 --> 00:00:17.180
will remove all this and save it as

10
00:00:17.180 --> 00:00:17.340
a dot.

11
00:00:18.020 --> 00:00:19.600
You see, I will simply type a very

12
00:00:19.600 --> 00:00:22.680
simple select star from orders here.

13
00:00:23.260 --> 00:00:26.040
And I will not run any other query

14
00:00:26.040 --> 00:00:26.280
here.

15
00:00:26.440 --> 00:00:27.700
I will simply run select star from orders.

16
00:00:27.700 --> 00:00:29.980
And it is saying no database selected.

17
00:00:30.140 --> 00:00:36.810
Because I have just opened my MySQL workbench

18
00:00:36.810 --> 00:00:36.910
again.

19
00:00:36.910 --> 00:00:37.430
So I will run it.

20
00:00:37.670 --> 00:00:39.130
So you see, this is my table of

21
00:00:39.130 --> 00:00:39.230
orders.

22
00:00:39.730 --> 00:00:40.810
Do write the name of use and database

23
00:00:40.810 --> 00:00:42.510
at the top.

24
00:00:43.030 --> 00:00:44.330
By the way, once you have run the

25
00:00:44.330 --> 00:00:46.530
name of use and database, then you don't

26
00:00:46.530 --> 00:00:46.970
need to write this.

27
00:00:47.430 --> 00:00:48.690
But again, this is very important.

28
00:00:49.130 --> 00:00:49.990
Let's talk about subqueries.

29
00:00:50.230 --> 00:00:51.150
There is a very simple thing.

30
00:00:51.790 --> 00:00:53.530
Query within a query is subquery.

31
00:00:53.670 --> 00:00:55.290
Like we have a mathematical expression.

32
00:00:56.170 --> 00:00:58.190
There can be another mathematical expression inside the

33
00:00:58.190 --> 00:00:58.290
mathematical expression.

34
00:00:58.290 --> 00:01:00.010
Which means there can be something else.

35
00:01:00.890 --> 00:01:01.930
And what will happen after that?

36
00:01:02.370 --> 00:01:03.890
It means whatever will happen.

37
00:01:04.110 --> 00:01:05.650
It means whatever is there.

38
00:01:06.190 --> 00:01:08.350
It will be resolved and come.

39
00:01:09.110 --> 00:01:10.610
And this is subquery.

40
00:01:10.690 --> 00:01:11.310
It is a simple thing.

41
00:01:11.550 --> 00:01:13.050
Let me show you subquery.

42
00:01:13.910 --> 00:01:15.030
How can you use it?

43
00:01:15.590 --> 00:01:17.170
Now let me tell you.

44
00:01:17.550 --> 00:01:18.550
What is the average price per unit?

45
00:01:19.510 --> 00:01:20.790
Means what is the average price per unit?

46
00:01:22.070 --> 00:01:23.890
So you will say, brother, take it out.

47
00:01:24.130 --> 00:01:24.730
What are you asking?

48
00:01:25.370 --> 00:01:26.550
I mean, what are you asking me?

49
00:01:26.550 --> 00:01:27.030
I am remembering.

50
00:01:27.550 --> 00:01:28.910
You can directly ask from SQL.

51
00:01:29.970 --> 00:01:32.170
Price underscore per underscore unit.

52
00:01:32.350 --> 00:01:32.770
By writing like this.

53
00:01:33.010 --> 00:01:33.370
From order.

54
00:01:33.510 --> 00:01:33.830
Do this.

55
00:01:34.430 --> 00:01:35.150
And run it.

56
00:01:35.250 --> 00:01:36.110
You will get the price per unit.

57
00:01:36.170 --> 00:01:36.470
What is the problem?

58
00:01:37.750 --> 00:01:40.930
Okay, if I tell you what are those

59
00:01:40.930 --> 00:01:45.850
records where the price per unit is more

60
00:01:45.850 --> 00:01:46.730
than the average.

61
00:01:48.390 --> 00:01:49.870
Okay, that's a good question.

62
00:01:50.570 --> 00:01:51.730
But your question hurt me.

63
00:01:52.630 --> 00:01:53.730
The question did not hurt at all.

64
00:01:54.170 --> 00:01:55.590
Let me tell you how this question will

65
00:01:55.590 --> 00:01:55.690
be solved.

66
00:01:55.690 --> 00:01:57.030
So here select.

67
00:01:58.030 --> 00:02:00.170
And after that you will write star from

68
00:02:00.170 --> 00:02:01.030
orders.

69
00:02:01.750 --> 00:02:02.470
You always have to write the name of

70
00:02:02.470 --> 00:02:04.390
the orders table in small.

71
00:02:05.210 --> 00:02:10.970
Where price per unit is greater than.

72
00:02:11.490 --> 00:02:12.810
And the above query will come here.

73
00:02:13.010 --> 00:02:14.310
The above query will come here.

74
00:02:14.770 --> 00:02:15.910
And this is subquery.

75
00:02:16.030 --> 00:02:17.950
Means this query is returning a number.

76
00:02:18.550 --> 00:02:19.370
I know this.

77
00:02:19.370 --> 00:02:20.910
So I will cut it and put it

78
00:02:20.910 --> 00:02:21.010
here.

79
00:02:21.850 --> 00:02:23.550
And what am I basically saying here?

80
00:02:23.550 --> 00:02:27.650
I am saying that price per unit is

81
00:02:27.650 --> 00:02:28.550
greater than.

82
00:02:28.630 --> 00:02:30.430
And let me see what is the problem

83
00:02:30.430 --> 00:02:30.670
here.

84
00:02:31.390 --> 00:02:33.250
Why is it giving me an error like

85
00:02:33.250 --> 00:02:33.350
this?

86
00:02:33.370 --> 00:02:34.210
What is the problem here?

87
00:02:34.390 --> 00:02:35.290
I wrote here.

88
00:02:35.610 --> 00:02:39.590
Price per unit is greater than select average

89
00:02:39.590 --> 00:02:41.310
price per unit from orders.

90
00:02:41.690 --> 00:02:43.090
Okay, this semicolon does not come inside here.

91
00:02:43.210 --> 00:02:44.770
When you write subquery, semicolon does not come.

92
00:02:44.910 --> 00:02:45.590
It has to be written like this.

93
00:02:46.330 --> 00:02:47.290
And now you will run it.

94
00:02:48.110 --> 00:02:48.790
Very good.

95
00:02:48.790 --> 00:02:50.930
It has given me all those records.

96
00:02:51.530 --> 00:02:54.830
Where price per unit is greater than average

97
00:02:54.830 --> 00:02:55.650
price per unit.

98
00:02:56.170 --> 00:02:58.230
So in the query, query means subquery.

99
00:02:58.370 --> 00:02:59.010
This is what happens.

100
00:02:59.190 --> 00:02:59.290
Okay.

101
00:02:59.750 --> 00:03:00.810
I am telling you this is what happens.

102
00:03:01.210 --> 00:03:03.430
Now you will get to see its variations.

103
00:03:04.070 --> 00:03:05.190
Like I tell you.

104
00:03:05.590 --> 00:03:07.450
That you can say here.

105
00:03:08.150 --> 00:03:10.330
Give me those orders by returning.

106
00:03:11.150 --> 00:03:14.710
From those cities where electronics were sold.

107
00:03:15.110 --> 00:03:15.490
Okay.

108
00:03:15.490 --> 00:03:17.310
So here you can say.

109
00:03:17.870 --> 00:03:19.210
Okay, let's do one thing.

110
00:03:20.110 --> 00:03:21.890
Let's fetch those orders.

111
00:03:22.630 --> 00:03:23.490
Let's see what the question is.

112
00:03:23.510 --> 00:03:23.990
The question is this.

113
00:03:24.110 --> 00:03:25.030
I do one thing first.

114
00:03:25.130 --> 00:03:25.250
I do this.

115
00:03:25.550 --> 00:03:26.010
Comment out.

116
00:03:26.230 --> 00:03:26.370
Okay.

117
00:03:27.250 --> 00:03:28.930
And I put a semicolon on it.

118
00:03:29.470 --> 00:03:29.970
I am saying.

119
00:03:30.450 --> 00:03:33.110
Give me the orders of those cities.

120
00:03:34.390 --> 00:03:36.550
Where at least one electronic has been sold.

121
00:03:37.170 --> 00:03:39.030
Which are those cities where electronic has been

122
00:03:39.030 --> 00:03:39.130
sold?

123
00:03:39.850 --> 00:03:40.610
Laptop has been sold.

124
00:03:40.970 --> 00:03:41.810
Here in Delhi.

125
00:03:42.010 --> 00:03:42.510
Delhi is there.

126
00:03:42.550 --> 00:03:43.830
Mumbai is there.

127
00:03:43.850 --> 00:03:44.830
And Ahmedabad is there.

128
00:03:44.830 --> 00:03:45.630
Electronics is there.

129
00:03:45.790 --> 00:03:46.570
Hyderabad is also there.

130
00:03:46.950 --> 00:03:47.330
So I am saying.

131
00:03:47.490 --> 00:03:48.330
Give me all their orders.

132
00:03:49.190 --> 00:03:50.310
Now how will this question be solved?

133
00:03:50.850 --> 00:03:51.390
Means you understood.

134
00:03:51.510 --> 00:03:51.870
What is the question?

135
00:03:52.090 --> 00:03:52.850
The question is that.

136
00:03:54.150 --> 00:03:56.290
Give me all those city orders.

137
00:03:56.510 --> 00:03:57.770
Where electronic has been sold.

138
00:03:58.310 --> 00:03:58.650
Means.

139
00:03:59.610 --> 00:04:00.970
If electronic has been sold in Delhi.

140
00:04:01.030 --> 00:04:02.090
Then I want all the orders of Delhi.

141
00:04:02.210 --> 00:04:03.050
Means I want this one too.

142
00:04:03.250 --> 00:04:04.090
I want the home decor one too.

143
00:04:04.250 --> 00:04:04.550
I want everything.

144
00:04:05.090 --> 00:04:05.230
Okay.

145
00:04:06.230 --> 00:04:07.170
Come on, let's solve it.

146
00:04:07.590 --> 00:04:09.070
So what we will do basically.

147
00:04:09.390 --> 00:04:10.370
I am erasing it like this.

148
00:04:10.550 --> 00:04:11.790
Because the query etc.

149
00:04:11.810 --> 00:04:12.810
You will get all this in the handbook.

150
00:04:13.110 --> 00:04:14.250
And you can also make it yourself.

151
00:04:14.250 --> 00:04:14.730
And you can also type it from the

152
00:04:14.730 --> 00:04:14.930
video.

153
00:04:15.769 --> 00:04:16.750
So that's not a big deal.

154
00:04:17.450 --> 00:04:18.890
So I will write here where.

155
00:04:19.170 --> 00:04:20.390
And I will say city in.

156
00:04:20.870 --> 00:04:22.150
And now I need such a query.

157
00:04:22.810 --> 00:04:23.790
Now I need such a query.

158
00:04:24.690 --> 00:04:25.690
What should I do?

159
00:04:25.930 --> 00:04:27.250
Which gives me all those cities.

160
00:04:28.370 --> 00:04:30.190
Where the category is electronics.

161
00:04:30.790 --> 00:04:31.030
Okay.

162
00:04:31.370 --> 00:04:32.310
So I will write that.

163
00:04:32.510 --> 00:04:35.210
Select star from orders.

164
00:04:35.530 --> 00:04:35.830
Okay.

165
00:04:35.990 --> 00:04:36.890
Select city from orders.

166
00:04:36.970 --> 00:04:37.410
Not star.

167
00:04:39.430 --> 00:04:40.750
Select city from orders.

168
00:04:40.930 --> 00:04:41.290
Where.

169
00:04:42.550 --> 00:04:43.190
I will write.

170
00:04:44.150 --> 00:04:44.770
Where.

171
00:04:45.350 --> 00:04:45.970
Category.

172
00:04:46.770 --> 00:04:49.150
Is equal to electronics.

173
00:04:50.810 --> 00:04:51.370
And that's it.

174
00:04:51.710 --> 00:04:52.330
So what will happen here.

175
00:04:52.470 --> 00:04:54.330
This query will return all those cities.

176
00:04:54.710 --> 00:04:55.930
Where the category is electronics.

177
00:04:56.670 --> 00:04:58.510
And this upper query will return.

178
00:04:58.690 --> 00:05:00.050
Means the outer query will return.

179
00:05:00.770 --> 00:05:02.710
All those orders.

180
00:05:03.670 --> 00:05:06.430
Where the city is in these cities.

181
00:05:06.810 --> 00:05:07.710
Means all the orders of these cities.

182
00:05:08.210 --> 00:05:08.990
You will get to see.

183
00:05:09.990 --> 00:05:11.370
And if you run it.

184
00:05:11.530 --> 00:05:11.870
Then you see.

185
00:05:12.210 --> 00:05:13.070
All the orders of Delhi.

186
00:05:13.170 --> 00:05:14.010
All the orders of Mumbai.

187
00:05:14.850 --> 00:05:15.710
All the orders of Ahmedabad.

188
00:05:16.930 --> 00:05:17.610
You are getting to see.

189
00:05:17.990 --> 00:05:18.190
Why?

190
00:05:18.470 --> 00:05:19.870
Because the category here was electronics.

191
00:05:20.190 --> 00:05:21.310
So you can also see the furniture orders

192
00:05:21.310 --> 00:05:21.910
of this.

193
00:05:22.390 --> 00:05:23.530
Means the question was.

194
00:05:23.870 --> 00:05:24.910
We have to return.

195
00:05:25.370 --> 00:05:26.570
Orders from cities.

196
00:05:26.670 --> 00:05:27.830
Where electronics were sold.

197
00:05:28.950 --> 00:05:29.310
Okay.

198
00:05:29.650 --> 00:05:30.130
So this thing.

199
00:05:30.370 --> 00:05:31.390
Is a very simple thing.

200
00:05:31.910 --> 00:05:32.850
I hope you people.

201
00:05:32.910 --> 00:05:33.250
Will understand.

202
00:05:34.210 --> 00:05:34.690
Now assume.

203
00:05:34.790 --> 00:05:35.130
I want.

204
00:05:35.550 --> 00:05:36.590
That my orders.

205
00:05:37.590 --> 00:05:38.370
The query.

206
00:05:38.450 --> 00:05:39.590
Which is the select star from orders.

207
00:05:39.810 --> 00:05:40.950
It gives me something like this.

208
00:05:41.390 --> 00:05:42.470
Means something like this.

209
00:05:42.630 --> 00:05:42.850
Looks like.

210
00:05:42.850 --> 00:05:44.050
I want.

211
00:05:44.050 --> 00:05:46.010
To show me an average column here.

212
00:05:46.810 --> 00:05:48.070
So what I will do here.

213
00:05:48.210 --> 00:05:48.850
I will write here.

214
00:05:49.030 --> 00:05:50.830
Select order ID.

215
00:05:52.070 --> 00:05:53.190
Customer name.

216
00:05:54.710 --> 00:05:55.850
Price per unit.

217
00:05:57.830 --> 00:05:59.470
And I will write a sub query here.

218
00:05:59.730 --> 00:06:00.030
And I will say.

219
00:06:00.230 --> 00:06:01.150
And a sub query.

220
00:06:01.710 --> 00:06:02.790
From orders.

221
00:06:03.790 --> 00:06:04.390
And I will write here.

222
00:06:05.190 --> 00:06:06.130
Sub query what I will write.

223
00:06:06.270 --> 00:06:07.570
Sub query I will basically write.

224
00:06:08.510 --> 00:06:09.330
That select.

225
00:06:10.310 --> 00:06:10.870
Select.

226
00:06:11.690 --> 00:06:12.730
I hope I am writing right.

227
00:06:18.390 --> 00:06:18.950
From.

228
00:06:20.430 --> 00:06:20.990
Orders.

229
00:06:23.630 --> 00:06:24.750
Customer name.

230
00:06:24.990 --> 00:06:25.530
Price per unit.

231
00:06:27.530 --> 00:06:28.090
From.

232
00:06:30.950 --> 00:06:31.510
Orders.

233
00:06:32.130 --> 00:06:32.370
Customer name.

234
00:06:32.570 --> 00:06:32.710
Orders.

235
00:06:33.370 --> 00:06:33.630
Customer name.

236
00:06:33.690 --> 00:06:33.790
Orders.

237
00:06:34.550 --> 00:06:35.590
Customer name.

238
00:06:35.710 --> 00:06:36.130
Price per unit.

239
00:06:36.570 --> 00:06:37.130
From.

240
00:06:37.130 --> 00:06:37.510
Customer name.

241
00:06:37.510 --> 00:06:37.950
From.

242
00:06:37.950 --> 00:06:38.230
Customer name.

243
00:06:38.470 --> 00:06:38.610
Price per unit.

244
00:06:38.830 --> 00:06:38.930
From.

245
00:06:39.250 --> 00:06:39.590
Orders.

246
00:06:42.250 --> 00:06:42.810
Customer name.

247
00:06:45.550 --> 00:06:45.950
Orders.

248
00:06:56.910 --> 00:06:57.890
Price per unit.

249
00:06:58.330 --> 00:06:58.470
Orders.

250
00:06:58.510 --> 00:06:59.190
Price per unit.

251
00:06:59.190 --> 00:06:59.450
Orders.

252
00:07:03.670 --> 00:07:03.870
Orders.

253
00:07:04.230 --> 00:07:06.390
Price per unit.

254
00:07:06.570 --> 00:07:06.870
From.

255
00:07:16.210 --> 00:07:17.250
Orders.

256
00:07:18.150 --> 00:07:19.190
Orders.

257
00:07:21.490 --> 00:07:22.530
Orders.

258
00:07:23.030 --> 00:07:23.330
Orders.

259
00:07:28.390 --> 00:07:28.910
Exists.

260
00:07:30.290 --> 00:07:31.330
Start.

261
00:07:32.170 --> 00:07:32.550
From.

262
00:07:32.830 --> 00:07:33.350
Orders.

263
00:07:36.970 --> 00:07:39.270
You are right.

264
00:07:39.270 --> 00:07:41.710
I'm telling too much now if I say

265
00:07:41.710 --> 00:07:46.710
select star from orders Oh orders Oh and

266
00:07:46.710 --> 00:07:50.370
after that I say where and I write

267
00:07:50.370 --> 00:07:53.410
Exists and after that I put a subquery

268
00:07:53.410 --> 00:07:56.090
I will explain it well and you people

269
00:07:56.090 --> 00:07:57.930
don't freak out because I will explain it

270
00:07:58.470 --> 00:08:05.540
select one from orders where where city is

271
00:08:05.540 --> 00:08:10.520
equal to o dot city and and and

272
00:08:12.560 --> 00:08:16.320
Category is equal to furniture Now I will

273
00:08:16.320 --> 00:08:17.140
tell you how this query will work.

274
00:08:18.280 --> 00:08:19.880
So what did we do here?

275
00:08:19.960 --> 00:08:21.940
We put a subquery and what did we

276
00:08:21.940 --> 00:08:22.400
do here?

277
00:08:22.480 --> 00:08:24.000
We say select from all the orders.

278
00:08:24.640 --> 00:08:25.880
Select star from orders O.

279
00:08:26.220 --> 00:08:27.340
We named the orders O.

280
00:08:27.800 --> 00:08:29.640
Then we say where exists.

281
00:08:30.140 --> 00:08:31.100
What does where exists mean?

282
00:08:31.580 --> 00:08:34.360
In exists we just find out if any

283
00:08:34.360 --> 00:08:35.940
record has been returned or not.

284
00:08:35.940 --> 00:08:38.260
So if this query that I have selected

285
00:08:38.260 --> 00:08:40.380
select one from orders where city is equal

286
00:08:40.380 --> 00:08:41.980
to o dot city and category is equal

287
00:08:41.980 --> 00:08:43.760
to Furniture, if any record is returned then

288
00:08:43.760 --> 00:08:45.140
it will be true and you will get

289
00:08:45.140 --> 00:08:45.480
to see that row.

290
00:08:46.080 --> 00:08:46.800
So how does this work?

291
00:08:46.980 --> 00:08:47.540
I will tell you.

292
00:08:47.920 --> 00:08:49.620
When you write select star from orders O,

293
00:08:50.040 --> 00:08:52.480
then all the rows are checked one by

294
00:08:52.480 --> 00:08:52.580
one.

295
00:08:52.800 --> 00:08:54.140
So let's say we are on this row

296
00:08:54.140 --> 00:08:54.240
first.

297
00:08:54.420 --> 00:08:55.220
Dr. Amit's row.

298
00:08:55.500 --> 00:08:56.380
So what will happen?

299
00:08:56.880 --> 00:08:59.020
Select one from orders where city is equal

300
00:08:59.020 --> 00:08:59.620
to o dot city.

301
00:08:59.700 --> 00:09:02.480
It will be seen that what city is

302
00:09:02.480 --> 00:09:07.960
equal to Delhi and category is equal to

303
00:09:07.960 --> 00:09:08.440
Furniture.

304
00:09:09.080 --> 00:09:10.320
Is there any record like this?

305
00:09:11.500 --> 00:09:12.020
Furniture from Delhi.

306
00:09:12.100 --> 00:09:13.700
There is no Furniture from Delhi.

307
00:09:14.000 --> 00:09:16.260
Is there any record of Furniture from Delhi?

308
00:09:16.840 --> 00:09:18.620
There is no record of Furniture from Delhi.

309
00:09:19.160 --> 00:09:19.840
So this row will not be included.

310
00:09:21.020 --> 00:09:21.580
Then we will come to the next row.

311
00:09:22.360 --> 00:09:23.440
Then we will see if there is any

312
00:09:23.440 --> 00:09:24.320
record of Furniture from Mumbai.

313
00:09:24.580 --> 00:09:25.480
There is a kitchen from Mumbai.

314
00:09:26.080 --> 00:09:27.220
There is no record of Furniture from Mumbai.

315
00:09:28.120 --> 00:09:29.540
The second one will also not be done.

316
00:09:29.540 --> 00:09:31.980
There is a record of Furniture from Delhi,

317
00:09:32.460 --> 00:09:33.720
by the way, I'm sorry.

318
00:09:33.940 --> 00:09:34.860
So the first row will come.

319
00:09:35.300 --> 00:09:36.540
So this is how it will be checked.

320
00:09:36.660 --> 00:09:37.540
Now you will ask what is select one?

321
00:09:38.140 --> 00:09:41.300
Select one means that we don't care what

322
00:09:41.300 --> 00:09:42.380
data this query is returning.

323
00:09:42.680 --> 00:09:44.420
We just care whether it is returning something

324
00:09:44.420 --> 00:09:44.900
or not.

325
00:09:45.280 --> 00:09:47.420
So if this query returns anything, then the

326
00:09:47.420 --> 00:09:50.000
condition inside where exists will be true in

327
00:09:50.000 --> 00:09:50.100
a way.

328
00:09:50.360 --> 00:09:52.000
And as soon as I run this query,

329
00:09:52.180 --> 00:09:54.500
you see the first record came here, the

330
00:09:54.500 --> 00:09:55.780
second one came, the third one came, the

331
00:09:55.780 --> 00:09:56.380
fourth one came.

332
00:09:56.380 --> 00:09:56.720
Why?

333
00:09:57.240 --> 00:10:00.820
Because in their cities, there was a record

334
00:10:00.820 --> 00:10:01.980
of categories equal to furniture.

335
00:10:03.220 --> 00:10:04.400
It must be somewhere in the table.

336
00:10:04.540 --> 00:10:05.400
You can go and see.

337
00:10:05.760 --> 00:10:08.360
So this is a little complex query and

338
00:10:08.360 --> 00:10:11.120
it tells you the use of exists.

339
00:10:11.700 --> 00:10:14.060
I would like you to experiment with such

340
00:10:14.060 --> 00:10:16.980
queries, which will increase your clarity even more.

341
00:10:18.040 --> 00:10:20.000
And I hope you are enjoying it.

342
00:10:20.040 --> 00:10:21.640
So far, I will give you a handbook

343
00:10:21.640 --> 00:10:22.780
and you will get to see the whole

344
00:10:22.780 --> 00:10:23.020
code.

345
00:10:23.020 --> 00:10:26.080
So you don't have to worry about how

346
00:10:26.080 --> 00:10:28.920
the queries are working, what is happening.

347
00:10:29.340 --> 00:10:32.200
You will get all this to download clearly.

348
00:10:33.320 --> 00:10:34.680
Thank you so much guys for watching this

349
00:10:34.680 --> 00:10:36.900
video and I will see you in the

350
00:10:36.900 --> 00:10:37.360
next one.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:02.350 --> 00:00:05.170
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Group by is used to group rows that

2
00:00:05.170 --> 00:00:08.470
have the same values and perform calculations on

3
00:00:08.470 --> 00:00:09.030
each group.

4
00:00:09.190 --> 00:00:09.930
What is the meaning of this?

5
00:00:10.410 --> 00:00:13.350
If you want to group according to a

6
00:00:13.350 --> 00:00:16.190
particular column, then you use group by.

7
00:00:17.390 --> 00:00:21.370
And these aggregate functions like count and sum

8
00:00:21.370 --> 00:00:22.410
are used with them.

9
00:00:23.430 --> 00:00:25.810
So let's see how to use group by.

10
00:00:26.050 --> 00:00:27.010
And I will be able to explain it

11
00:00:27.010 --> 00:00:27.750
better than the example.

12
00:00:29.010 --> 00:00:31.210
So here I will show you select star

13
00:00:31.210 --> 00:00:31.910
from orders.

14
00:00:32.910 --> 00:00:34.770
My orders table has become very distorted.

15
00:00:35.310 --> 00:00:37.030
So you can do one thing, you can

16
00:00:37.030 --> 00:00:39.570
feel free to repopulate your orders table.

17
00:00:39.690 --> 00:00:40.290
How will you do that?

18
00:00:40.490 --> 00:00:44.030
In the beginning of our video, where we

19
00:00:44.030 --> 00:00:46.030
talked about the starter SQL, go there.

20
00:00:46.490 --> 00:00:48.750
And get the script from there and populate

21
00:00:48.750 --> 00:00:52.190
the orders table properly.

22
00:00:52.550 --> 00:00:53.530
But it will work like this too.

23
00:00:54.030 --> 00:00:55.910
Okay, no problem, it will work like this

24
00:00:55.910 --> 00:00:56.010
too.

25
00:00:56.010 --> 00:00:57.570
So what am I going to do here?

26
00:00:57.730 --> 00:00:58.490
I am going to show you group by.

27
00:00:59.110 --> 00:01:00.030
So what will I do here?

28
00:01:00.130 --> 00:01:01.630
I will write select city from orders.

29
00:01:01.810 --> 00:01:03.050
So if I do select city from orders,

30
00:01:03.390 --> 00:01:04.050
then I will get the city.

31
00:01:04.790 --> 00:01:06.150
No surprises there.

32
00:01:06.510 --> 00:01:08.670
But you see, the city is being repeated

33
00:01:08.670 --> 00:01:08.830
here.

34
00:01:08.910 --> 00:01:09.730
Delhi, Delhi.

35
00:01:10.330 --> 00:01:12.910
Now I say here that I know what

36
00:01:12.910 --> 00:01:13.190
I want.

37
00:01:13.270 --> 00:01:15.670
I want the city and I want to

38
00:01:15.670 --> 00:01:17.010
see what I am doing here carefully.

39
00:01:17.470 --> 00:01:22.290
And I want count star as let's say

40
00:01:22.290 --> 00:01:23.010
total orders.

41
00:01:23.010 --> 00:01:23.710
Okay.

42
00:01:23.850 --> 00:01:24.650
Means how many orders have come in a

43
00:01:24.650 --> 00:01:25.210
particular city.

44
00:01:26.110 --> 00:01:26.550
I need their count.

45
00:01:27.470 --> 00:01:29.090
And I want to do group by.

46
00:01:29.290 --> 00:01:30.490
I write this query like this.

47
00:01:31.210 --> 00:01:34.850
And I will write here group by city.

48
00:01:35.110 --> 00:01:36.190
Now what is this query saying?

49
00:01:36.490 --> 00:01:37.530
This query is saying that group it according

50
00:01:37.530 --> 00:01:38.630
to the city.

51
00:01:39.290 --> 00:01:40.530
I mean, this Delhi, Delhi is twice.

52
00:01:40.690 --> 00:01:41.730
I just need Delhi once.

53
00:01:42.250 --> 00:01:43.850
And give me the count of total orders.

54
00:01:44.250 --> 00:01:46.470
So I am saying here, select city and

55
00:01:46.470 --> 00:01:47.050
give me the count.

56
00:01:47.310 --> 00:01:49.070
How many orders have come from this city.

57
00:01:49.250 --> 00:01:50.030
Like this number will come for Delhi.

58
00:01:50.030 --> 00:01:50.830
This number will come for Delhi.

59
00:01:50.830 --> 00:01:52.870
One, two, three.

60
00:01:53.670 --> 00:01:54.170
Three will come.

61
00:01:54.370 --> 00:01:55.230
Okay, let's run it.

62
00:01:55.670 --> 00:01:56.150
Three came for Delhi.

63
00:01:56.770 --> 00:01:57.370
Two came for Mumbai.

64
00:01:57.470 --> 00:01:57.810
One came for Bangalore.

65
00:01:58.270 --> 00:01:58.670
One came for Ahmedabad.

66
00:01:59.250 --> 00:02:01.110
Now see, see what has come out of

67
00:02:01.110 --> 00:02:01.390
the data inside.

68
00:02:02.110 --> 00:02:04.050
I know how many orders have come from

69
00:02:04.050 --> 00:02:04.150
Delhi.

70
00:02:04.390 --> 00:02:05.970
I know how many orders have come from

71
00:02:05.970 --> 00:02:06.070
Mumbai.

72
00:02:06.070 --> 00:02:07.669
I know how many orders are from Bangalore.

73
00:02:07.930 --> 00:02:08.389
I know city wise.

74
00:02:08.970 --> 00:02:10.470
I can also sort by clicking here like

75
00:02:10.470 --> 00:02:10.570
this.

76
00:02:11.430 --> 00:02:12.770
Okay, the most orders have come from Delhi.

77
00:02:13.050 --> 00:02:13.490
Then what is Mumbai?

78
00:02:13.730 --> 00:02:14.430
I mean, focus on these two cities.

79
00:02:15.370 --> 00:02:17.750
So business insights come out of these things.

80
00:02:17.750 --> 00:02:19.410
So you should know this thing.

81
00:02:19.710 --> 00:02:23.630
Now assume that I want to group by

82
00:02:23.630 --> 00:02:24.270
category.

83
00:02:25.410 --> 00:02:26.510
Do it by category.

84
00:02:27.010 --> 00:02:27.930
And I do the same thing.

85
00:02:28.310 --> 00:02:29.990
So I can't do the same thing.

86
00:02:30.750 --> 00:02:32.370
Because I will have to do this.

87
00:02:33.070 --> 00:02:34.810
And you see, there are four orders of

88
00:02:34.810 --> 00:02:34.910
electronics.

89
00:02:34.970 --> 00:02:35.910
There are two orders of furniture.

90
00:02:36.130 --> 00:02:37.110
There is one order of stationery.

91
00:02:37.590 --> 00:02:38.310
So I can do this thing.

92
00:02:39.050 --> 00:02:41.370
But let's say, along with the count, I

93
00:02:41.370 --> 00:02:43.750
also want to see How much is the

94
00:02:43.750 --> 00:02:44.270
total sale?

95
00:02:44.830 --> 00:02:45.990
I mean, where is my money being made?

96
00:02:45.990 --> 00:02:48.950
So I will say sum of quantity.

97
00:02:49.410 --> 00:02:50.210
It was quantity.

98
00:02:50.750 --> 00:02:51.950
And what was the price?

99
00:02:51.990 --> 00:02:52.290
What was the price?

100
00:02:52.530 --> 00:02:53.130
So what will I do to see the

101
00:02:53.130 --> 00:02:53.350
price?

102
00:02:53.670 --> 00:02:54.250
I will also tell you this trick.

103
00:02:54.710 --> 00:02:56.510
Now see, I don't know what the price

104
00:02:56.510 --> 00:02:57.670
column was.

105
00:02:57.990 --> 00:02:59.130
Price per unit was.

106
00:02:59.270 --> 00:03:01.270
Price underscore unit was.

107
00:03:01.370 --> 00:03:01.710
What was it?

108
00:03:01.770 --> 00:03:02.530
I don't remember.

109
00:03:02.670 --> 00:03:03.690
Okay, let's say I don't remember.

110
00:03:04.150 --> 00:03:04.990
Okay, so what will I do?

111
00:03:05.690 --> 00:03:06.250
Look carefully.

112
00:03:06.950 --> 00:03:07.490
What will I do?

113
00:03:07.770 --> 00:03:09.570
I will open my table book of orders.

114
00:03:09.930 --> 00:03:10.830
I will click on it like this.

115
00:03:10.910 --> 00:03:11.150
Okay.

116
00:03:12.110 --> 00:03:14.190
Look here, I saw it.

117
00:03:14.190 --> 00:03:14.890
It was price per unit.

118
00:03:14.890 --> 00:03:15.530
It was this.

119
00:03:15.830 --> 00:03:16.010
Okay.

120
00:03:16.510 --> 00:03:17.090
It was this.

121
00:03:17.630 --> 00:03:18.730
And I can also copy this.

122
00:03:19.070 --> 00:03:19.250
Okay.

123
00:03:19.250 --> 00:03:20.830
If you select this and copy the quantity

124
00:03:20.830 --> 00:03:23.210
like this, You can paste it like this.

125
00:03:23.390 --> 00:03:24.030
Just saying.

126
00:03:24.190 --> 00:03:24.290
Okay.

127
00:03:24.350 --> 00:03:25.790
You can select this and do ctrl c

128
00:03:25.790 --> 00:03:26.530
like this.

129
00:03:26.870 --> 00:03:27.350
Okay.

130
00:03:27.410 --> 00:03:28.050
And you can also do ctrl v.

131
00:03:28.890 --> 00:03:30.770
So I said here that I need sum

132
00:03:30.770 --> 00:03:32.690
quantity into price per unit.

133
00:03:33.570 --> 00:03:34.050
As.

134
00:03:34.710 --> 00:03:35.190
As.

135
00:03:35.790 --> 00:03:36.750
Total sales.

136
00:03:37.050 --> 00:03:37.210
Okay.

137
00:03:37.770 --> 00:03:40.410
So I said here that give me category.

138
00:03:41.350 --> 00:03:42.570
Give count of total orders.

139
00:03:42.570 --> 00:03:42.890
Okay.

140
00:03:43.630 --> 00:03:44.970
And tell me the total sales.

141
00:03:45.470 --> 00:03:46.370
How much did I sell in electronics?

142
00:03:47.450 --> 00:03:48.430
How much did I sell in furniture?

143
00:03:49.970 --> 00:03:51.270
And I need this thing for all orders.

144
00:03:51.690 --> 00:03:52.150
That's why I am doing sum.

145
00:03:52.710 --> 00:03:53.430
So I will run this query.

146
00:03:54.750 --> 00:03:58.670
So here I can see that I sold

147
00:03:58.670 --> 00:03:59.890
1 lakh for electronics.

148
00:04:00.570 --> 00:04:02.310
For furniture, what did I sell the most

149
00:04:02.310 --> 00:04:02.550
for?

150
00:04:03.370 --> 00:04:04.330
I sold the most for electronics.

151
00:04:04.750 --> 00:04:06.350
After that, there is a null category.

152
00:04:06.670 --> 00:04:07.490
I sold for that.

153
00:04:07.830 --> 00:04:09.050
By the way, my data is a bit

154
00:04:09.050 --> 00:04:09.590
here and there.

155
00:04:10.270 --> 00:04:11.130
That's why this null is coming.

156
00:04:11.130 --> 00:04:12.590
Because if you look at the original table,

157
00:04:12.970 --> 00:04:13.910
then there is a sale on category null.

158
00:04:15.170 --> 00:04:15.270
Okay.

159
00:04:15.810 --> 00:04:19.029
So when I made the foreign key video,

160
00:04:19.269 --> 00:04:20.450
then I showed you some changes.

161
00:04:21.070 --> 00:04:22.150
So that's why it's coming.

162
00:04:22.250 --> 00:04:22.790
But that's fine.

163
00:04:23.650 --> 00:04:24.970
There are so many orders of furniture.

164
00:04:25.350 --> 00:04:26.290
There are so many orders of appliances.

165
00:04:26.450 --> 00:04:28.350
And one thing on which I can tell

166
00:04:28.350 --> 00:04:29.930
my employees, my management.

167
00:04:30.390 --> 00:04:31.490
Don't focus.

168
00:04:31.610 --> 00:04:32.730
Money is not being made here.

169
00:04:32.850 --> 00:04:33.590
That is stationery.

170
00:04:33.890 --> 00:04:34.930
I can say that we are selling stationery

171
00:04:34.930 --> 00:04:35.310
for 800.

172
00:04:36.190 --> 00:04:37.370
My mind is getting so bad.

173
00:04:37.930 --> 00:04:38.430
So do one thing.

174
00:04:38.910 --> 00:04:39.550
Don't think too much.

175
00:04:39.550 --> 00:04:41.190
Definitely sell this stuff.

176
00:04:41.330 --> 00:04:41.790
It's a good thing.

177
00:04:42.370 --> 00:04:44.770
But we are getting so little revenue on

178
00:04:44.770 --> 00:04:44.870
it.

179
00:04:44.890 --> 00:04:46.250
So we put a lot of mind and

180
00:04:46.250 --> 00:04:47.810
don't want to do a lot of good.

181
00:04:49.210 --> 00:04:49.950
That's one thing.

182
00:04:50.110 --> 00:04:50.370
Okay.

183
00:04:50.510 --> 00:04:51.550
I hope you got the point.

184
00:04:52.150 --> 00:04:53.470
So this is done with group by sum.

185
00:04:54.330 --> 00:04:55.070
Again, you can do the same thing with

186
00:04:55.070 --> 00:04:55.490
the average.

187
00:04:56.450 --> 00:04:59.310
You can say that, man, like, suppose you

188
00:04:59.310 --> 00:05:03.590
want that how much is the average price

189
00:05:03.590 --> 00:05:04.250
per unit in a city?

190
00:05:04.550 --> 00:05:04.870
Okay.

191
00:05:05.110 --> 00:05:06.070
So you will do group by city.

192
00:06:38.170 --> 00:06:45.870
I want to write count star as count,

193
00:06:45.950 --> 00:06:46.850
now what it will do, I will tell

194
00:06:46.850 --> 00:06:50.110
you, I said select city and order status

195
00:06:50.110 --> 00:06:51.770
and I want to group by city and

196
00:06:51.770 --> 00:06:56.150
order status, so if I run this query,

197
00:06:56.790 --> 00:06:57.990
then you see here I got the city,

198
00:06:58.410 --> 00:07:00.470
I got the order status and here I

199
00:07:00.470 --> 00:07:02.750
got the count, so basically what I did,

200
00:07:02.850 --> 00:07:05.810
I grouped according to two columns, so how

201
00:07:05.810 --> 00:07:08.370
many cancelled orders are there, one is there,

202
00:07:09.010 --> 00:07:10.590
how many delivered orders are there in Delhi,

203
00:07:10.690 --> 00:07:12.270
three are there, now you will get delivered

204
00:07:12.270 --> 00:07:14.350
orders of Delhi only once, Delhi is not

205
00:07:14.350 --> 00:07:18.430
delivered anywhere else, Ahmedabad is cancelled, now if

206
00:07:18.430 --> 00:07:21.150
I sort it according to the city, so

207
00:07:21.150 --> 00:07:24.710
I have Ahmedabad cancelled, if Ahmedabad delivered, if

208
00:07:24.710 --> 00:07:26.710
I had any order, then I would get

209
00:07:26.710 --> 00:07:29.210
a row of Ahmedabad delivered, here I got

210
00:07:29.210 --> 00:07:31.450
a row of Bangalore delivered, if Bangalore is

211
00:07:31.450 --> 00:07:42.130
cancelled, if there is any order,

212
00:07:48.090 --> 00:07:49.990
then I will show you one more thing,

213
00:07:52.810 --> 00:07:55.990
if I run two queries here, then you

214
00:07:55.990 --> 00:07:58.830
will get two tabs here, so I will

215
00:07:58.830 --> 00:08:00.030
show you here, there is no order of

216
00:08:00.030 --> 00:08:04.930
Ahmedabad delivered, Ahmedabad has only cancelled order, I

217
00:08:04.930 --> 00:08:07.090
will sort it according to the city, look

218
00:08:07.090 --> 00:08:10.490
at Delhi, we have delivered, delivered, delivered and

219
00:08:10.490 --> 00:08:13.310
we have delivered from Hyderabad, if you want,

220
00:08:13.430 --> 00:08:15.930
you can insert and you can see this

221
00:08:15.930 --> 00:08:17.750
by doing this, but again you got the

222
00:08:17.750 --> 00:08:20.250
point that you will get unique combinations of

223
00:08:20.250 --> 00:08:21.650
these two columns and you can group by

224
00:08:21.650 --> 00:08:25.150
multiple columns too, okay, I hope you got

225
00:08:25.150 --> 00:08:27.790
the point, and I hope you are enjoying

226
00:08:27.790 --> 00:08:29.670
this course so far, now we will see

227
00:08:29.670 --> 00:08:33.370
about having clause, what is having clause, now

228
00:08:33.370 --> 00:08:35.970
the work of having clause is to filter,

229
00:08:36.590 --> 00:08:38.110
for example, if you will do group by

230
00:08:38.110 --> 00:08:39.549
city status here, if you will try to

231
00:08:39.549 --> 00:08:44.190
use where here, then you people, if I

232
00:08:44.190 --> 00:08:46.890
do something like this, city in, and I

233
00:08:46.890 --> 00:08:51.350
write here like this, and I write Mumbai,

234
00:08:51.770 --> 00:08:53.790
okay, so here error has come, that you

235
00:08:53.790 --> 00:08:55.410
cannot do this, so MySQL is telling you

236
00:08:55.410 --> 00:08:56.650
that you cannot do this, what are you

237
00:08:56.650 --> 00:08:58.410
doing, and I will remove this too for

238
00:08:58.410 --> 00:09:01.010
now, so here MySQL is telling you that

239
00:09:01.010 --> 00:09:02.870
you cannot do this, it is wrong, why

240
00:09:02.870 --> 00:09:04.510
you cannot do this, where you cannot use,

241
00:09:04.910 --> 00:09:08.110
you have to use having, so if I

242
00:09:08.110 --> 00:09:11.010
run this, so here you see, you have

243
00:09:11.010 --> 00:09:13.030
an error in the SQL syntax, check the

244
00:09:13.030 --> 00:09:15.350
manual that corresponds to your, so here it

245
00:09:15.350 --> 00:09:18.010
is simply telling you that you cannot do

246
00:09:18.010 --> 00:09:19.350
this, so whenever you are using group by,

247
00:09:19.750 --> 00:09:21.790
you have to use having, and now if

248
00:09:21.790 --> 00:09:24.890
you run, you will see Delhi Mumbai, so

249
00:09:24.890 --> 00:09:26.730
whenever you are using group by, you have

250
00:09:26.730 --> 00:09:29.050
to filter, so do not use where, use

251
00:09:29.050 --> 00:09:31.030
having, this is the rule, this is the

252
00:09:31.030 --> 00:09:33.970
syntax of MySQL, I hope you got the

253
00:09:33.970 --> 00:09:36.370
point, now here can you do order by,

254
00:09:36.850 --> 00:09:39.610
so suppose you did group by, which we

255
00:09:39.610 --> 00:09:41.390
already did here, so if I run this,

256
00:09:41.530 --> 00:09:44.150
we did group by, now suppose I want

257
00:09:44.150 --> 00:09:46.970
to sort by count, that too in which

258
00:09:46.970 --> 00:09:49.630
order, in increasing order, so what I will

259
00:09:49.630 --> 00:09:53.290
do, I will write simply order by, and

260
00:09:53.290 --> 00:09:57.530
I will write, let's say count, count, okay,

261
00:09:57.590 --> 00:09:59.550
order by count, and as soon as I

262
00:09:59.550 --> 00:10:01.510
run this, you see in ascending order, I

263
00:10:01.510 --> 00:10:03.190
got to see here, if I say order

264
00:10:03.190 --> 00:10:05.730
by city, so here I will get this

265
00:10:05.730 --> 00:10:07.410
order according to the city, you see, Ahmedabad

266
00:10:07.410 --> 00:10:08.970
A will come first, B later, A, B,

267
00:10:09.010 --> 00:10:30.890
C, D, E, F, C,

268
00:10:30.890 --> 00:10:32.090
D, E, F, C, D, E, F, C,

269
00:10:32.090 --> 00:10:36.710
D, E, F, C, D, E, F, C,

270
00:10:36.830 --> 00:10:38.910
D, E, F, C, D, E, F, C,

271
00:10:38.910 --> 00:10:39.170
D, E, F, C, D, E, F, C,

272
00:10:39.170 --> 00:10:39.270
D, E, F, C, D, E, F, C,

273
00:10:39.270 --> 00:10:39.370
D, E, F, C, D, E, F, C,

274
00:10:39.370 --> 00:10:39.470
D, E, F, C, D, E, F, C,

275
00:10:39.470 --> 00:10:39.570
D, E, F, C, D, E, F, C,

276
00:10:39.570 --> 00:10:39.670
D, E, F, C, D, E, F, C,

277
00:10:39.670 --> 00:10:39.770
D, E, F, C, D, E, F, C,

278
00:10:39.770 --> 00:10:39.870
D, E, F, C, D, E, F, C,

279
00:10:39.870 --> 00:10:39.970
D, E, F, C, D, E, F, C,

280
00:10:39.970 --> 00:10:40.070
D, E, F, C, D, E, F, C,

281
00:10:40.070 --> 00:10:40.170
D, E, F, C, D, E If you

282
00:10:40.170 --> 00:10:42.190
have a lot of entries of Ahmedabad, then

283
00:10:42.190 --> 00:10:43.050
all those entries will be sorted according to

284
00:10:43.050 --> 00:10:43.770
the order status.

285
00:10:45.270 --> 00:10:46.390
I hope you got the point.

286
00:10:47.010 --> 00:10:49.570
So yeah, that was about Group Buy in

287
00:10:49.570 --> 00:10:50.130
SQL.

288
00:10:50.470 --> 00:10:51.590
I hope you got the point.

289
00:10:52.030 --> 00:10:53.650
You will get all the code and the

290
00:10:53.650 --> 00:10:54.170
handbook.

291
00:10:55.710 --> 00:10:56.910
There is no need to take tension.

292
00:10:57.830 --> 00:10:58.950
Focus on understanding.

293
00:11:00.590 --> 00:11:02.190
I hope you are enjoying this course so

294
00:11:02.190 --> 00:11:02.430
far.

295
00:11:02.870 --> 00:11:04.110
See you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:02.480
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will talk about what

2
00:00:02.480 --> 00:00:03.940
happens in union sql.

3
00:00:04.500 --> 00:00:07.780
So, union is used to combine result of

4
00:00:07.780 --> 00:00:10.140
multiple select queries into a single set.

5
00:00:10.300 --> 00:00:11.760
So, you have two select queries.

6
00:00:12.120 --> 00:00:13.200
Both of them are doing different work.

7
00:00:14.080 --> 00:00:14.780
What do you want?

8
00:00:14.920 --> 00:00:17.400
You want that both of them should get

9
00:00:17.400 --> 00:00:18.300
their results.

10
00:00:18.620 --> 00:00:19.560
But how should they get?

11
00:00:19.580 --> 00:00:20.440
What is the meaning of getting?

12
00:00:21.160 --> 00:00:24.000
Let's say, your first select query has returned

13
00:00:24.000 --> 00:00:26.160
5 rows.

14
00:00:26.520 --> 00:00:29.100
And your second select query has returned 4

15
00:00:29.100 --> 00:00:29.400
rows.

16
00:00:29.400 --> 00:00:32.380
So, your total should have returned 9 rows.

17
00:00:33.980 --> 00:00:37.040
And your results will come down one by

18
00:00:37.040 --> 00:00:37.860
one.

19
00:00:39.110 --> 00:00:41.260
So, here to demonstrate this, I will make

20
00:00:41.260 --> 00:00:41.940
one more table.

21
00:00:42.420 --> 00:00:45.340
Whose name is employee underscore orders table.

22
00:00:45.780 --> 00:00:47.360
And here what I am going to do

23
00:00:47.360 --> 00:00:49.920
is I will simply make employee underscore orders

24
00:00:49.920 --> 00:00:51.720
table.

25
00:00:53.300 --> 00:00:54.180
So, I will copy this.

26
00:00:54.620 --> 00:00:55.760
Create table command.

27
00:00:56.100 --> 00:00:57.300
You will get all this.

28
00:00:58.220 --> 00:01:00.140
And I will do this work quickly.

29
00:01:00.500 --> 00:01:02.340
So, basically what I will do is I

30
00:01:02.340 --> 00:01:03.340
will close this.

31
00:01:03.640 --> 00:01:04.660
So, basically what I will do is I

32
00:01:04.660 --> 00:01:06.080
will make employee underscore orders table.

33
00:01:06.680 --> 00:01:08.000
And the second thing which I am going

34
00:01:08.000 --> 00:01:11.180
to do is I will insert data in

35
00:01:11.180 --> 00:01:11.280
this.

36
00:01:11.440 --> 00:01:13.380
So, to insert data in this, I will

37
00:01:13.380 --> 00:01:14.060
copy this.

38
00:01:14.400 --> 00:01:16.460
And after copying this, what I will do

39
00:01:16.460 --> 00:01:17.180
is I will simply paste this.

40
00:01:17.400 --> 00:01:18.440
And I am not doing anything here.

41
00:01:18.500 --> 00:01:19.900
I have made a table named employee underscore

42
00:01:19.900 --> 00:01:20.280
orders.

43
00:01:20.940 --> 00:01:22.860
And I have stored some data in it.

44
00:01:23.500 --> 00:01:24.960
Then I will show you what is in

45
00:01:24.960 --> 00:01:26.040
my orders table.

46
00:01:26.800 --> 00:01:28.660
And what I will do is I will

47
00:01:28.660 --> 00:01:29.200
copy this.

48
00:01:30.340 --> 00:01:34.580
And here I Basically what I want is

49
00:01:34.580 --> 00:01:40.740
Employees underscore orders Employee underscore orders This select

50
00:01:40.740 --> 00:01:42.500
query and this select query What does it

51
00:01:42.500 --> 00:01:42.840
return?

52
00:01:43.280 --> 00:01:45.640
I want to show you this.

53
00:01:45.700 --> 00:01:50.180
So, my first select star query returned this.

54
00:01:50.220 --> 00:01:52.200
And the second query returned this.

55
00:01:52.460 --> 00:01:53.300
So, here you see one thing.

56
00:01:54.060 --> 00:01:57.100
Ananya Roy is here as well as here.

57
00:01:57.420 --> 00:01:58.480
And I have done this on purpose.

58
00:01:59.360 --> 00:02:02.000
Now, assume that I run two select queries.

59
00:02:02.620 --> 00:02:05.760
One select query is saying Order ID, Customer

60
00:02:05.760 --> 00:02:08.699
Name as Name, City, Product and Price per

61
00:02:08.699 --> 00:02:10.039
Unit Bring it from the order.

62
00:02:10.180 --> 00:02:11.160
What will happen with this?

63
00:02:11.420 --> 00:02:12.040
What will happen with this?

64
00:02:12.760 --> 00:02:13.720
It will be a very simple thing.

65
00:02:14.380 --> 00:02:15.740
All these things will come from the order.

66
00:02:15.840 --> 00:02:16.700
You know what will happen.

67
00:02:17.040 --> 00:02:18.460
So, I will run this.

68
00:02:18.760 --> 00:02:19.300
I will also put semicolon.

69
00:02:19.940 --> 00:02:21.840
I will run this.

70
00:02:21.840 --> 00:02:22.480
So, what will happen?

71
00:02:22.580 --> 00:02:23.040
What is the problem?

72
00:02:24.460 --> 00:02:25.440
What is the problem?

73
00:02:26.000 --> 00:02:26.380
Oh!

74
00:02:26.720 --> 00:02:28.300
The problem is that I have run this

75
00:02:28.300 --> 00:02:29.440
again by mistake.

76
00:02:29.600 --> 00:02:30.420
I have to comment this out.

77
00:02:30.660 --> 00:02:31.520
This table is already existing.

78
00:02:32.500 --> 00:02:32.960
So, it is saying why are you running

79
00:02:32.960 --> 00:02:33.440
create table?

80
00:02:34.060 --> 00:02:34.800
The table is already existing.

81
00:02:35.520 --> 00:02:36.140
No problem.

82
00:02:36.420 --> 00:02:37.980
So, here you got to see all this.

83
00:02:38.460 --> 00:02:40.400
We have taken Customer Name as Name here.

84
00:02:40.480 --> 00:02:41.300
That's why the name of this column is

85
00:02:41.300 --> 00:02:41.580
Name.

86
00:02:42.120 --> 00:02:42.980
Which is very obvious.

87
00:02:43.100 --> 00:02:44.700
And what is my second query saying?

88
00:02:45.020 --> 00:02:46.360
Bring it from Employee underscore orders.

89
00:02:47.240 --> 00:02:49.480
Order ID, Name, City, Product and Price per

90
00:02:49.480 --> 00:02:50.560
Unit Let's bring this too.

91
00:02:50.560 --> 00:02:50.820
Okay?

92
00:02:51.760 --> 00:02:52.860
So, I have run this too.

93
00:02:52.980 --> 00:02:53.420
So, I will get the results of both

94
00:02:53.420 --> 00:02:54.100
the queries.

95
00:02:55.220 --> 00:02:55.840
This is the result of the first query.

96
00:02:56.740 --> 00:02:57.380
This is the result of the second query.

97
00:02:58.140 --> 00:02:58.980
Now, look at one thing.

98
00:02:59.940 --> 00:03:02.600
That thing is that you can see this

99
00:03:02.600 --> 00:03:04.220
particular view.

100
00:03:04.660 --> 00:03:06.340
I mean, these four rows are visible and

101
00:03:06.340 --> 00:03:07.060
these columns are visible.

102
00:03:07.940 --> 00:03:08.980
And this particular view is visible.

103
00:03:09.120 --> 00:03:10.940
What are the similarities in this?

104
00:03:10.980 --> 00:03:13.260
The similarities are that its columns are the

105
00:03:13.260 --> 00:03:13.360
same.

106
00:03:13.560 --> 00:03:14.360
Its column is also the same.

107
00:03:14.500 --> 00:03:15.300
Its column is also the same.

108
00:03:15.880 --> 00:03:16.860
Suppose I want to see all this data

109
00:03:16.860 --> 00:03:17.420
at once.

110
00:03:18.020 --> 00:03:22.120
I want this data to be appended below

111
00:03:22.120 --> 00:03:22.220
this.

112
00:03:23.260 --> 00:03:24.000
What will I do?

113
00:03:24.600 --> 00:03:25.980
I can union these two queries.

114
00:03:26.920 --> 00:03:27.620
So, I will remove the semicolon.

115
00:03:28.080 --> 00:03:29.480
What will happen is that this query will

116
00:03:29.480 --> 00:03:30.060
not end here.

117
00:03:30.560 --> 00:03:32.280
And I will simply say Union here.

118
00:03:32.340 --> 00:03:33.580
I am saying that Union it.

119
00:03:33.620 --> 00:03:34.460
And these spaces are not necessary.

120
00:03:34.840 --> 00:03:34.940
Okay?

121
00:03:35.380 --> 00:03:37.340
I am saying that Union this query with

122
00:03:37.340 --> 00:03:37.900
this query.

123
00:03:38.560 --> 00:03:40.020
And return all the results at once.

124
00:03:40.700 --> 00:03:41.660
So, I will run this.

125
00:03:41.740 --> 00:03:42.120
So, you see.

126
00:03:42.960 --> 00:03:44.360
The results of the second query that I

127
00:03:44.360 --> 00:03:46.740
was returning have become one.

128
00:03:47.080 --> 00:03:48.240
Basically, I have merged two queries.

129
00:03:49.420 --> 00:03:50.480
It is a very simple thing.

130
00:03:51.100 --> 00:03:51.860
I have merged two queries.

131
00:03:53.200 --> 00:03:55.000
And I have written Union between them.

132
00:03:55.520 --> 00:03:57.100
And the results of those two have been

133
00:03:57.100 --> 00:03:57.980
appended one after the other.

134
00:03:58.620 --> 00:03:59.600
What will happen with this?

135
00:04:00.760 --> 00:04:02.380
Our customer orders will be combined.

136
00:04:02.920 --> 00:04:05.080
And employee orders will come in one result

137
00:04:05.080 --> 00:04:05.340
set.

138
00:04:06.140 --> 00:04:08.960
Duplicate rows are automatically removed here.

139
00:04:09.780 --> 00:04:12.900
So, Ananya Roy was removed here or not?

140
00:04:12.900 --> 00:04:14.140
Ananya Roy was not removed.

141
00:04:15.040 --> 00:04:17.540
Because the order ID was different.

142
00:04:17.959 --> 00:04:18.059
Okay?

143
00:04:18.440 --> 00:04:19.279
If I don't take the order ID.

144
00:04:20.019 --> 00:04:20.779
If I don't take the order ID.

145
00:04:21.440 --> 00:04:21.620
Okay?

146
00:04:22.360 --> 00:04:22.900
I will show you.

147
00:04:23.620 --> 00:04:24.680
If I just do this.

148
00:04:25.260 --> 00:04:26.720
So, now Ananya Roy has been removed.

149
00:04:27.320 --> 00:04:27.860
You see.

150
00:04:28.160 --> 00:04:29.020
Ananya Roy has been removed.

151
00:04:29.260 --> 00:04:29.920
Why has it been removed?

152
00:04:30.040 --> 00:04:31.260
Because Ananya Roy was already there.

153
00:04:31.340 --> 00:04:32.720
So, duplicates are automatically removed.

154
00:04:33.220 --> 00:04:33.400
Okay?

155
00:04:34.260 --> 00:04:35.900
Now, you want to remove duplicate rows.

156
00:04:36.180 --> 00:04:36.720
No, you don't.

157
00:04:36.720 --> 00:04:38.480
I don't want to remove duplicate rows.

158
00:04:39.120 --> 00:04:39.560
Why?

159
00:04:40.160 --> 00:04:41.300
SQL is doing this.

160
00:04:41.880 --> 00:04:43.260
So, you use union all.

161
00:04:44.040 --> 00:04:45.580
You will apply all after union.

162
00:04:45.740 --> 00:04:47.260
So, by applying all, you are basically saying.

163
00:04:47.620 --> 00:04:50.360
Don't automatically remove duplicates for me.

164
00:04:50.720 --> 00:04:53.120
I am happy with my appended result.

165
00:04:54.060 --> 00:04:56.060
I mean, if Ananya Roy is being repeated

166
00:04:56.060 --> 00:04:56.240
here.

167
00:04:56.300 --> 00:04:57.220
Then I don't have any problem.

168
00:04:57.480 --> 00:04:58.620
I just want to see my data.

169
00:04:59.620 --> 00:05:00.260
So, if you do this.

170
00:05:00.360 --> 00:05:01.720
You will get to see Ananya Roy here.

171
00:05:02.140 --> 00:05:03.300
It is a very simple thing.

172
00:05:03.840 --> 00:05:04.600
And that's all.

173
00:05:04.800 --> 00:05:06.300
Union removes duplicates.

174
00:05:06.620 --> 00:05:08.640
Union all keeps duplicates.

175
00:05:08.960 --> 00:05:09.720
And is faster.

176
00:05:09.840 --> 00:05:10.760
This is very important.

177
00:05:10.760 --> 00:05:11.380
And it is asked in the interview.

178
00:05:12.040 --> 00:05:13.300
That union all is fast.

179
00:05:13.580 --> 00:05:15.460
Because there is no need to remove duplicates.

180
00:05:16.400 --> 00:05:18.900
Removing duplicates is a time-consuming task.

181
00:05:19.480 --> 00:05:20.600
For MySQL engine.

182
00:05:21.240 --> 00:05:22.760
And what does union all do?

183
00:05:23.280 --> 00:05:23.960
It keeps duplicates.

184
00:05:24.560 --> 00:05:25.060
It doesn't remove them.

185
00:05:25.160 --> 00:05:26.440
It doesn't have to do extra work.

186
00:05:26.900 --> 00:05:29.640
Because of which union all is fast.

187
00:05:30.000 --> 00:05:31.020
Now, when do you want to use union?

188
00:05:31.580 --> 00:05:32.260
When do you want to use union all?

189
00:05:33.320 --> 00:05:34.220
When you want to combine.

190
00:05:35.080 --> 00:05:35.860
Similar data.

191
00:05:36.140 --> 00:05:36.580
Then use union.

192
00:05:37.280 --> 00:05:38.800
If you want to see combined report.

193
00:05:38.800 --> 00:05:40.620
Whether it is duplicated or not.

194
00:05:41.060 --> 00:05:41.500
Then use union.

195
00:05:41.880 --> 00:05:43.200
If you use union all.

196
00:05:43.820 --> 00:05:45.260
Then you should know.

197
00:05:46.080 --> 00:05:49.060
That your duplicates will not be automatically removed.

198
00:05:49.900 --> 00:05:52.240
So, duplicate rows will be removed from union.

199
00:05:52.240 --> 00:05:52.940
From union all.

200
00:05:53.260 --> 00:05:55.400
Duplicate rows will not be removed.

201
00:05:55.600 --> 00:05:57.620
And that's all about union and union all.

202
00:05:57.880 --> 00:05:59.380
Thank you so much guys for watching this

203
00:05:59.380 --> 00:05:59.680
video.

204
00:06:00.020 --> 00:06:01.940
And I will see you in the next

205
00:06:01.940 --> 00:06:02.280
one.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


WEBVTT

1
00:00:00.200 --> 00:00:02.060
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Guys, now we are going to talk about

2
00:00:02.060 --> 00:00:05.640
rollup, when rollup is used in MySQL and

3
00:00:05.640 --> 00:00:06.380
why it is used.

4
00:00:06.680 --> 00:00:08.140
So, first of all, I want to tell

5
00:00:08.140 --> 00:00:11.820
you that rollup is used with groupby to

6
00:00:11.820 --> 00:00:12.600
generate summary rows.

7
00:00:13.780 --> 00:00:16.700
This is very important in reporting and analytics.

8
00:00:17.400 --> 00:00:18.220
So, I want to give you a basic

9
00:00:18.220 --> 00:00:19.620
example of rollup.

10
00:00:20.660 --> 00:00:22.240
And before that, I want to show you

11
00:00:22.240 --> 00:00:28.080
that rollup is used when you already have

12
00:00:28.080 --> 00:00:29.200
a groupby query.

13
00:00:29.200 --> 00:00:30.040
So, I will delete all this.

14
00:00:30.320 --> 00:00:33.260
And here I will simply write, let's say,

15
00:00:33.340 --> 00:00:36.140
select city category.

16
00:00:36.620 --> 00:00:40.640
And let's say, we are summing quantity here.

17
00:00:41.380 --> 00:00:44.840
And we are multiplying it by price per

18
00:00:44.840 --> 00:00:45.180
unit.

19
00:00:45.180 --> 00:00:46.520
If you remember, we did this in the

20
00:00:46.520 --> 00:00:47.140
previous videos.

21
00:00:47.500 --> 00:00:49.960
And we said, bring it as total sales.

22
00:00:50.880 --> 00:00:55.060
And we will do this from orders, orders.

23
00:00:55.740 --> 00:01:01.220
And we will write here, groupby city category.

24
00:01:01.380 --> 00:01:02.080
Simple.

25
00:01:02.260 --> 00:01:03.920
It is a very simple SQL query.

26
00:01:04.120 --> 00:01:04.720
And what does it do?

27
00:01:04.980 --> 00:01:05.920
It groups city and category.

28
00:01:06.500 --> 00:01:08.760
That is, it shows unique combinations of city

29
00:01:08.760 --> 00:01:09.400
category to us.

30
00:01:09.980 --> 00:01:15.380
And shows total sales for corresponding city category

31
00:01:15.380 --> 00:01:15.900
combination.

32
00:01:16.720 --> 00:01:17.640
Very simple query.

33
00:01:17.760 --> 00:01:19.240
We discussed this in detail earlier.

34
00:01:19.240 --> 00:01:23.660
Now you see here, how you can use

35
00:01:23.660 --> 00:01:24.240
rollup.

36
00:01:25.380 --> 00:01:27.180
Now what you have to do is, you

37
00:01:27.180 --> 00:01:28.240
have to simply write rollup here.

38
00:01:29.160 --> 00:01:29.900
Just have to write rollup.

39
00:01:30.620 --> 00:01:31.920
And as soon as you write rollup here,

40
00:01:32.560 --> 00:01:33.100
what will happen?

41
00:01:33.380 --> 00:01:35.000
Here I have to write with rollup.

42
00:01:35.460 --> 00:01:36.940
Not rollup, have to write with rollup.

43
00:01:37.240 --> 00:01:38.120
And as soon as I write with rollup,

44
00:01:38.580 --> 00:01:39.380
what will happen?

45
00:01:39.760 --> 00:01:41.480
Now you can see here that you will

46
00:01:41.480 --> 00:01:41.960
get to see something like this.

47
00:01:42.800 --> 00:01:43.980
So what happened here?

48
00:01:43.980 --> 00:01:45.760
Here it is telling me that when the

49
00:01:45.760 --> 00:01:46.980
city was null, the category was null.

50
00:01:47.160 --> 00:01:47.840
So what was the total sales?

51
00:01:49.000 --> 00:01:49.840
65,000.

52
00:01:50.180 --> 00:01:51.440
Means 65,000 for null combination.

53
00:01:52.940 --> 00:01:54.920
Ahmedabad Electronics has 30,000.

54
00:01:55.360 --> 00:01:56.840
Ahmedabad Null has 30,000.

55
00:01:57.240 --> 00:01:58.760
Then Bangalore Null has 800.

56
00:01:59.160 --> 00:02:01.240
And at the end, you get to see

57
00:02:01.240 --> 00:02:01.360
this too.

58
00:02:02.160 --> 00:02:03.520
So what does this query do?

59
00:02:03.720 --> 00:02:06.500
This query also gives you group data.

60
00:02:07.039 --> 00:02:08.479
And along with that, it also gives you

61
00:02:08.479 --> 00:02:11.100
grand total at the end.

62
00:02:11.260 --> 00:02:11.420
Okay.

63
00:02:11.420 --> 00:02:13.160
So here you see that it is also

64
00:02:13.160 --> 00:02:14.380
giving you grand total.

65
00:02:15.500 --> 00:02:18.640
So 210301 is your grand total.

66
00:02:18.840 --> 00:02:20.220
If you sum all of them, then it

67
00:02:20.220 --> 00:02:20.500
will come.

68
00:02:20.800 --> 00:02:22.340
Now our data is a little distorted.

69
00:02:22.900 --> 00:02:24.720
And why don't I clean this data?

70
00:02:25.400 --> 00:02:27.020
So what will I do to clean this

71
00:02:27.020 --> 00:02:27.120
data?

72
00:02:27.600 --> 00:02:32.180
I will write select star from orders here.

73
00:02:32.260 --> 00:02:33.840
And what do we do for now?

74
00:02:34.460 --> 00:02:35.080
Comment out.

75
00:02:35.340 --> 00:02:36.580
And I will tell you how I will

76
00:02:36.580 --> 00:02:36.980
clean up this data.

77
00:02:38.040 --> 00:02:39.880
I will run row number 14.

78
00:02:39.880 --> 00:02:43.980
And I will run only row number 14.

79
00:02:44.340 --> 00:02:45.120
Because here it is null.

80
00:02:45.580 --> 00:02:47.900
If there is anything else null, then that

81
00:02:47.900 --> 00:02:48.440
is fine.

82
00:02:48.740 --> 00:02:50.140
So I have to run row number 14.

83
00:02:50.580 --> 00:02:55.820
So I will write delete from orders where

84
00:02:55.820 --> 00:03:00.860
order underscore id is equal to 14.

85
00:03:01.120 --> 00:03:02.620
And if I run it, what will happen?

86
00:03:02.900 --> 00:03:04.300
That my delete query has run.

87
00:03:04.740 --> 00:03:05.800
And now I will comment out the delete

88
00:03:05.800 --> 00:03:06.100
query.

89
00:03:06.100 --> 00:03:07.100
I will comment out the delete query.

90
00:03:07.440 --> 00:03:09.620
And you see that I have clean data

91
00:03:09.620 --> 00:03:10.140
here.

92
00:03:10.240 --> 00:03:14.040
And now I will run my rollup query.

93
00:03:15.540 --> 00:03:16.060
Okay.

94
00:03:16.280 --> 00:03:18.300
So as soon as I run it, you

95
00:03:18.300 --> 00:03:18.920
guys see here.

96
00:03:19.060 --> 00:03:20.040
Now I am getting to see a lot

97
00:03:20.040 --> 00:03:21.240
of sensible data here.

98
00:03:21.880 --> 00:03:23.660
See here, I am getting to see Ahmedabad

99
00:03:23.660 --> 00:03:24.800
Electronics 30,000.

100
00:03:24.880 --> 00:03:26.300
I have Ahmedabad Null here.

101
00:03:27.040 --> 00:03:30.540
If I show you this too, select start

102
00:03:30.540 --> 00:03:31.140
from orders.

103
00:03:32.200 --> 00:03:33.680
If we keep both side by side here.

104
00:03:33.680 --> 00:03:36.580
So you see here, Ahmedabad Null 30,000.

105
00:03:36.820 --> 00:03:37.060
Why is it coming?

106
00:03:37.420 --> 00:03:39.120
You see when our city is Ahmedabad.

107
00:03:39.680 --> 00:03:39.820
Okay.

108
00:03:40.780 --> 00:03:41.700
City is Ahmedabad.

109
00:03:42.000 --> 00:03:44.400
And category is our null.

110
00:03:44.580 --> 00:03:45.040
So what does it mean?

111
00:03:45.440 --> 00:03:48.180
It is telling me total sales for Ahmedabad.

112
00:03:48.640 --> 00:03:51.020
So the city category will show you normal

113
00:03:51.020 --> 00:03:51.560
group data.

114
00:03:51.800 --> 00:03:54.060
But city, null will show you total sales

115
00:03:54.060 --> 00:03:54.740
for that city.

116
00:03:55.060 --> 00:03:56.420
We understand this from the example of Delhi.

117
00:03:56.880 --> 00:03:57.840
Now look at the data carefully.

118
00:03:58.380 --> 00:04:00.040
Now see here, how much is Delhi furniture?

119
00:04:00.520 --> 00:04:01.340
65,101.

120
00:04:02.020 --> 00:04:02.700
How much is Delhi furniture?

121
00:04:03.260 --> 00:04:05.140
Sorry, Delhi electronics has 65,101.

122
00:04:05.260 --> 00:04:06.580
Delhi furniture has 12,000.

123
00:04:06.920 --> 00:04:08.180
Delhi home decor has 3,000.

124
00:04:08.280 --> 00:04:10.880
And if you sum these three, it will

125
00:04:10.880 --> 00:04:12.120
come around 80,000.

126
00:04:12.260 --> 00:04:13.340
If you want, you can try it.

127
00:04:13.800 --> 00:04:15.060
12, 3 is 15.

128
00:04:15.480 --> 00:04:17.660
And 65 and 15 is around 80, 101.

129
00:04:18.260 --> 00:04:19.040
In fact, it will come exactly.

130
00:04:19.660 --> 00:04:21.140
So Delhi null means, if you sum all

131
00:04:21.140 --> 00:04:24.760
the categories of Delhi city, it will come.

132
00:04:24.860 --> 00:04:27.760
So you guys can read this data like

133
00:04:27.760 --> 00:04:27.860
this.

134
00:04:28.000 --> 00:04:28.600
How to read roll-up results?

135
00:04:29.300 --> 00:04:30.000
I have included it in the handbook.

136
00:04:31.880 --> 00:04:33.040
Experiment with this thing.

137
00:04:33.300 --> 00:04:35.160
You will definitely get a lot of clarity.

138
00:04:35.680 --> 00:04:37.040
Now I have taken two columns here.

139
00:04:37.180 --> 00:04:38.060
If you want, you can also do group

140
00:04:38.060 --> 00:04:38.660
by category.

141
00:04:39.260 --> 00:04:40.480
If you only do group by category.

142
00:04:42.100 --> 00:04:43.220
Let's say I run this.

143
00:04:43.880 --> 00:04:46.100
So you guys see, group by...

144
00:04:46.100 --> 00:04:47.180
One minute, I'll remove the city from here.

145
00:04:48.480 --> 00:04:49.740
And I close it.

146
00:04:50.560 --> 00:04:51.840
One minute, I...

147
00:04:51.840 --> 00:04:53.660
So now you see, your result is coming

148
00:04:53.660 --> 00:04:54.160
like this.

149
00:04:54.440 --> 00:04:55.220
You can see here.

150
00:04:55.580 --> 00:04:56.460
Accessories, 5500.

151
00:04:56.620 --> 00:04:57.620
Appliances, 4200.

152
00:04:57.620 --> 00:04:58.940
So in the end, you guys get to

153
00:04:58.940 --> 00:05:00.880
see the result here.

154
00:05:01.060 --> 00:05:01.740
So what will it give you?

155
00:05:02.060 --> 00:05:03.240
It will give you order count per category.

156
00:05:03.780 --> 00:05:05.380
And along with that, it will give you

157
00:05:05.380 --> 00:05:06.300
the overall total sale.

158
00:05:06.740 --> 00:05:07.740
After this, it is very important for you

159
00:05:07.740 --> 00:05:08.820
guys to understand one thing.

160
00:05:10.100 --> 00:05:11.200
The query we ran.

161
00:05:11.420 --> 00:05:12.580
If I assume, I run such a query.

162
00:05:13.620 --> 00:05:14.880
I remove everything.

163
00:05:15.280 --> 00:05:16.080
If I run such a query.

164
00:05:16.400 --> 00:05:17.420
I am saying city category.

165
00:05:17.960 --> 00:05:19.820
Sum of quantity into price per unit as

166
00:05:19.820 --> 00:05:20.760
total sales from orders.

167
00:05:20.880 --> 00:05:22.640
Group by group, by city and category.

168
00:05:23.160 --> 00:05:24.120
If I run something like this.

169
00:05:24.380 --> 00:05:26.240
So don't think that null means missing value.

170
00:05:26.240 --> 00:05:27.600
Null doesn't mean missing value.

171
00:05:28.440 --> 00:05:29.380
Here, you understand this thing.

172
00:05:29.500 --> 00:05:30.540
Null doesn't mean missing value.

173
00:05:30.720 --> 00:05:31.780
Null basically means this.

174
00:05:32.080 --> 00:05:32.600
Sum of the above.

175
00:05:33.080 --> 00:05:36.520
Like here, all these three of Delhi's sum

176
00:05:36.520 --> 00:05:36.840
is this.

177
00:05:37.220 --> 00:05:37.820
80, 101.

178
00:05:38.000 --> 00:05:39.400
So it doesn't mean that Delhi and null

179
00:05:39.400 --> 00:05:39.640
is this.

180
00:05:40.300 --> 00:05:40.980
Don't think like this.

181
00:05:41.600 --> 00:05:44.600
So this thing is very confused by people.

182
00:05:45.080 --> 00:05:47.280
But again, you should be very very careful.

183
00:05:47.300 --> 00:05:48.080
When you are reading your data.

184
00:05:48.780 --> 00:05:50.460
Especially when you are using with rollup.

185
00:05:51.240 --> 00:05:53.240
With your group by queries.

186
00:05:53.240 --> 00:05:55.680
When will you use it in business reports.

187
00:05:55.840 --> 00:05:56.680
In sales summaries.

188
00:05:57.340 --> 00:05:59.000
And in your dashboard totals.

189
00:05:59.340 --> 00:06:00.560
In financial aggregations.

190
00:06:01.380 --> 00:06:04.280
And once you learn all this.

191
00:06:04.560 --> 00:06:06.680
Then you will know when to use it.

192
00:06:07.100 --> 00:06:09.180
And what is optimal to use.

193
00:06:09.280 --> 00:06:11.640
So if I summarize things quickly.

194
00:06:11.760 --> 00:06:13.540
Then rollup adds subtotals.

195
00:06:13.900 --> 00:06:14.340
Along with that.

196
00:06:15.280 --> 00:06:16.490
Order of columns.

197
00:06:17.140 --> 00:06:17.980
It matters in group by.

198
00:06:19.560 --> 00:06:21.040
And by using this.

199
00:06:21.040 --> 00:06:24.780
You can read your reports very well.

200
00:06:25.060 --> 00:06:26.780
And get details from it.

201
00:06:26.960 --> 00:06:28.580
I hope you are enjoying this course so

202
00:06:28.580 --> 00:06:28.880
far.

203
00:06:29.280 --> 00:06:30.360
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


WEBVTT

1
00:00:00.070 --> 00:00:04.130
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now let's see what is stored

2
00:00:04.130 --> 00:00:06.170
procedure and why do we need a stored

3
00:00:06.170 --> 00:00:07.690
procedure in MySQL.

4
00:00:08.050 --> 00:00:10.350
First of all, stored procedure is a saved

5
00:00:10.350 --> 00:00:12.650
block of SQL statements that run as a

6
00:00:12.650 --> 00:00:13.510
single unit.

7
00:00:13.630 --> 00:00:15.370
You can say that you have written a

8
00:00:15.370 --> 00:00:15.770
function.

9
00:00:16.110 --> 00:00:19.590
Like we write functions in Python, C, C++.

10
00:00:20.650 --> 00:00:22.250
By the way, these functions are quite similar

11
00:00:22.250 --> 00:00:22.350
somewhere.

12
00:00:23.370 --> 00:00:25.450
It helps in reusing logic.

13
00:00:26.290 --> 00:00:27.210
It reduces repetition.

14
00:00:27.210 --> 00:00:27.930
It reduces repetition.

15
00:00:28.170 --> 00:00:30.630
And it stores business logic in your database.

16
00:00:31.369 --> 00:00:32.310
That means you have stored logic.

17
00:00:32.930 --> 00:00:34.830
You won't issue queries again and again.

18
00:00:35.690 --> 00:00:37.710
Let's say you have a very big query.

19
00:00:38.090 --> 00:00:40.510
A query which is quite long and wide.

20
00:00:41.150 --> 00:00:42.270
You have issued it once.

21
00:00:43.170 --> 00:00:45.670
Now you say that I have issued this

22
00:00:45.670 --> 00:00:45.970
query.

23
00:00:46.610 --> 00:00:48.770
I will use it again and again.

24
00:00:49.590 --> 00:00:51.070
I will use it again and again.

25
00:00:51.310 --> 00:00:53.170
And I want to use it easily.

26
00:00:56.090 --> 00:00:57.930
Assume that it is a very big query.

27
00:00:58.490 --> 00:01:00.890
Select start from orders where order status is

28
00:01:00.890 --> 00:01:01.230
delivered.

29
00:01:01.550 --> 00:01:03.090
Assume that it is a very complex query.

30
00:01:03.670 --> 00:01:06.070
Which uses very complex conditions.

31
00:01:07.210 --> 00:01:09.110
Which uses very complex things.

32
00:01:10.570 --> 00:01:12.730
And you don't want to issue those queries

33
00:01:12.730 --> 00:01:14.630
to your employees again and again.

34
00:01:15.560 --> 00:01:17.950
How good it would be if you just

35
00:01:17.950 --> 00:01:19.110
write Get Delivered Orders.

36
00:01:19.250 --> 00:01:20.570
Write a name like this.

37
00:01:20.970 --> 00:01:22.770
And your whole query will run.

38
00:01:23.070 --> 00:01:27.050
And this is exactly what stored procedure does

39
00:01:27.050 --> 00:01:27.150
for us.

40
00:01:27.430 --> 00:01:28.730
So let's see stored procedure.

41
00:01:29.310 --> 00:01:33.630
To make stored procedure, we write create procedure.

42
00:01:35.450 --> 00:01:36.470
I have written it correctly.

43
00:01:37.030 --> 00:01:39.370
And I will write any name of my

44
00:01:39.370 --> 00:01:39.970
choice here.

45
00:01:40.170 --> 00:01:41.570
Let's give it the name Get Delivered Orders.

46
00:01:42.890 --> 00:01:44.850
And we will write like this.

47
00:01:45.370 --> 00:01:46.610
I have written Get Delivered Orders.

48
00:01:46.890 --> 00:01:49.050
Then we write begin and end.

49
00:01:49.170 --> 00:01:49.910
And whatever we write, we will write in

50
00:01:49.910 --> 00:01:50.710
between begin and end.

51
00:01:51.470 --> 00:01:52.730
Then after that we will write our query.

52
00:01:53.590 --> 00:01:59.790
Select start from orders where order status is

53
00:01:59.790 --> 00:02:03.570
equal to delivered.

54
00:02:05.580 --> 00:02:06.720
Something like this.

55
00:02:07.360 --> 00:02:10.580
And select start from orders.

56
00:02:10.580 --> 00:02:15.140
And let's say I want to select start

57
00:02:16.640 --> 00:02:20.320
from let's say employees.

58
00:02:21.440 --> 00:02:22.620
I want to do this too.

59
00:02:22.740 --> 00:02:23.800
Let's say I want to do these two

60
00:02:23.800 --> 00:02:24.120
things.

61
00:02:25.060 --> 00:02:26.660
So this is our stored procedure.

62
00:02:27.200 --> 00:02:28.460
But there is a problem.

63
00:02:28.900 --> 00:02:29.900
You see errors are coming.

64
00:02:30.240 --> 00:02:30.720
This error.

65
00:02:31.380 --> 00:02:31.880
This error.

66
00:02:31.980 --> 00:02:32.700
What is this error saying?

67
00:02:32.920 --> 00:02:34.040
Let's take an error on this.

68
00:02:34.680 --> 00:02:36.320
It says statement is incomplete.

69
00:02:36.580 --> 00:02:37.780
Expecting semicolon.

70
00:02:37.780 --> 00:02:39.620
So basically what is it?

71
00:02:40.000 --> 00:02:41.960
There are multiple select queries between my begin

72
00:02:41.960 --> 00:02:42.060
and end.

73
00:02:42.780 --> 00:02:44.200
And there are semicolons in them.

74
00:02:45.080 --> 00:02:47.020
But what is happening is that the MySQL

75
00:02:47.020 --> 00:02:48.020
is getting confused.

76
00:02:48.420 --> 00:02:51.100
It is saying that this MySQL somewhere you

77
00:02:51.100 --> 00:02:52.360
have not finished this entire query.

78
00:02:53.520 --> 00:02:54.800
Understand what the problem is here.

79
00:02:55.280 --> 00:02:57.180
The problem is that it is in itself

80
00:02:57.180 --> 00:02:57.680
in a way.

81
00:02:58.400 --> 00:02:58.860
I will not call it a query.

82
00:02:59.380 --> 00:03:00.460
It is the code of MySQL.

83
00:03:01.020 --> 00:03:03.520
Which will be terminated with semicolons.

84
00:03:04.140 --> 00:03:05.900
But I have to use semicolons inside it

85
00:03:05.900 --> 00:03:06.000
too.

86
00:03:06.000 --> 00:03:09.060
But if I use semicolons inside it.

87
00:03:09.780 --> 00:03:10.780
So what will happen?

88
00:03:11.000 --> 00:03:13.540
It seems to MySQL that I have written

89
00:03:13.540 --> 00:03:14.720
so much statement and it is invalid.

90
00:03:15.640 --> 00:03:16.800
So what do we do for this?

91
00:03:16.960 --> 00:03:17.540
Change the delimiter.

92
00:03:18.640 --> 00:03:21.100
So by default semicolon is our delimiter.

93
00:03:21.500 --> 00:03:25.400
Semicolon means that your query is ending by

94
00:03:25.400 --> 00:03:25.500
putting semicolon.

95
00:03:26.020 --> 00:03:27.540
I will change this thing here.

96
00:03:27.660 --> 00:03:28.020
I will say.

97
00:03:29.100 --> 00:03:30.120
Make my delimiter this.

98
00:03:31.000 --> 00:03:31.960
I can also make it dollar dollar.

99
00:03:31.960 --> 00:03:35.520
I basically said that from now on semicolon

100
00:03:35.520 --> 00:03:36.160
is not my delimiter.

101
00:03:36.600 --> 00:03:37.940
From now on this is my delimiter.

102
00:03:38.080 --> 00:03:39.520
When I will put this then my query

103
00:03:39.520 --> 00:03:39.760
will end.

104
00:03:40.680 --> 00:03:42.260
Or any MySQL code will end.

105
00:03:42.760 --> 00:03:44.080
But now where I used to use semicolon.

106
00:03:44.240 --> 00:03:46.020
I will use double forward slash here.

107
00:03:47.180 --> 00:03:49.020
And I will put double forward slash here.

108
00:03:49.480 --> 00:03:50.280
So what did I do?

109
00:03:50.340 --> 00:03:50.960
I changed the delimiter.

110
00:03:51.740 --> 00:03:53.120
I said I am making the delimiter.

111
00:03:53.860 --> 00:03:54.740
Double forward slash.

112
00:03:54.940 --> 00:03:56.360
And at the end.

113
00:03:57.720 --> 00:03:59.520
I will make the delimiter semicolon again.

114
00:03:59.520 --> 00:04:02.420
So here I temporarily changed my delimiter.

115
00:04:02.880 --> 00:04:04.420
To double forward slash.

116
00:04:05.040 --> 00:04:06.020
And after that what did I do?

117
00:04:06.720 --> 00:04:07.280
Delimiter.

118
00:04:07.560 --> 00:04:09.140
Towards the end of this file.

119
00:04:09.340 --> 00:04:10.860
I made the delimiter semicolon again.

120
00:04:11.000 --> 00:04:11.560
Which is default.

121
00:04:12.280 --> 00:04:13.400
Now I will run this.

122
00:04:13.940 --> 00:04:14.720
So you see here.

123
00:04:15.019 --> 00:04:16.160
My query is running.

124
00:04:16.540 --> 00:04:18.600
My procedure is done.

125
00:04:18.899 --> 00:04:19.060
Okay.

126
00:04:19.740 --> 00:04:20.279
Very good.

127
00:04:20.899 --> 00:04:23.280
So my stored procedure is done.

128
00:04:23.520 --> 00:04:24.200
Now what will I do?

129
00:04:24.340 --> 00:04:25.160
I will open a new query tab.

130
00:04:26.380 --> 00:04:27.220
New query tab.

131
00:04:27.260 --> 00:04:28.460
Because I don't want to change this.

132
00:04:28.460 --> 00:04:29.980
Now what will I do?

133
00:04:30.740 --> 00:04:32.560
I will call this here.

134
00:04:32.880 --> 00:04:34.000
Stored procedure.

135
00:04:34.600 --> 00:04:35.800
So to call stored procedure.

136
00:04:36.480 --> 00:04:37.220
You have to use call.

137
00:04:38.120 --> 00:04:39.380
You write call.

138
00:04:39.520 --> 00:04:40.780
And the name of your stored procedure.

139
00:04:43.300 --> 00:04:44.420
In this case it is.

140
00:04:44.880 --> 00:04:46.080
Get delivered orders.

141
00:04:46.460 --> 00:04:47.360
So I will say call.

142
00:04:47.480 --> 00:04:48.540
Get delivered orders.

143
00:04:48.720 --> 00:04:49.400
And I will run this.

144
00:04:49.980 --> 00:04:50.960
So basically what will happen?

145
00:04:51.040 --> 00:04:52.040
My two select queries will run.

146
00:04:52.300 --> 00:04:52.840
The first was.

147
00:04:53.340 --> 00:04:55.060
That I will get all my delivered orders.

148
00:04:55.780 --> 00:04:56.320
The second was.

149
00:04:56.400 --> 00:04:57.740
Select star from employees.

150
00:04:57.840 --> 00:04:58.380
These were my employees.

151
00:04:58.380 --> 00:05:00.220
So here you can see.

152
00:05:00.340 --> 00:05:01.180
I am getting these two results.

153
00:05:02.780 --> 00:05:03.620
Very good.

154
00:05:04.180 --> 00:05:05.820
So this get delivered orders.

155
00:05:06.360 --> 00:05:07.800
I made a stored procedure.

156
00:05:08.760 --> 00:05:10.400
After that I reset the delimiter.

157
00:05:11.120 --> 00:05:12.140
Then I called the stored procedure.

158
00:05:13.380 --> 00:05:14.780
Now we had called the stored procedure.

159
00:05:15.860 --> 00:05:17.440
There was no parameter in it.

160
00:05:18.440 --> 00:05:19.000
Just think.

161
00:05:19.340 --> 00:05:20.600
I also give the name of the city

162
00:05:20.600 --> 00:05:21.080
here.

163
00:05:21.700 --> 00:05:22.280
I made a procedure called get orders by

164
00:05:22.280 --> 00:05:22.500
city.

165
00:05:23.460 --> 00:05:25.840
And I want to give the name of

166
00:05:25.840 --> 00:05:25.940
the city here.

167
00:05:26.220 --> 00:05:27.580
And I get the orders of that city.

168
00:05:27.580 --> 00:05:29.100
Means I call like this.

169
00:05:29.660 --> 00:05:30.780
And I get.

170
00:05:31.300 --> 00:05:32.240
Something like this.

171
00:05:33.520 --> 00:05:34.600
What is the name of this procedure?

172
00:05:34.740 --> 00:05:35.600
Get orders by city.

173
00:05:36.200 --> 00:05:37.580
Means I want to make get orders by

174
00:05:37.580 --> 00:05:37.820
city.

175
00:05:39.340 --> 00:05:41.580
Get orders by city.

176
00:05:42.640 --> 00:05:43.540
And I want that.

177
00:05:43.660 --> 00:05:44.560
If I write Delhi here.

178
00:05:46.420 --> 00:05:48.020
Then I get all the orders of Delhi.

179
00:05:49.220 --> 00:05:49.560
Okay.

180
00:05:50.320 --> 00:05:51.520
How good it would be if this started

181
00:05:51.520 --> 00:05:51.840
working.

182
00:05:52.140 --> 00:05:52.880
Will it work now?

183
00:05:53.020 --> 00:05:53.660
Obviously not.

184
00:05:53.840 --> 00:05:55.100
Because I have not made this stored procedure.

185
00:05:55.900 --> 00:05:56.540
Procedure.

186
00:05:56.680 --> 00:05:59.400
Get orders by city does not exist.

187
00:06:00.100 --> 00:06:01.220
It does not exist.

188
00:06:01.720 --> 00:06:03.600
So what will we do to make this?

189
00:06:03.980 --> 00:06:05.980
We will do exactly the same thing.

190
00:06:06.560 --> 00:06:07.260
What I will do.

191
00:06:07.740 --> 00:06:09.120
What we did earlier.

192
00:06:09.860 --> 00:06:10.820
After removing that.

193
00:06:11.020 --> 00:06:11.720
This time I will write.

194
00:06:11.940 --> 00:06:13.760
Create procedure.

195
00:06:14.440 --> 00:06:15.140
And I will write here.

196
00:06:15.440 --> 00:06:19.100
Get orders by city.

197
00:06:20.360 --> 00:06:21.800
And after this what I will do.

198
00:06:22.060 --> 00:06:22.900
I will write in.

199
00:06:22.900 --> 00:06:24.980
City underscore name.

200
00:06:26.300 --> 00:06:26.620
Varchar.

201
00:06:26.640 --> 00:06:27.360
What does this mean?

202
00:06:27.500 --> 00:06:28.440
Varchar 50.

203
00:06:29.160 --> 00:06:31.340
I am saying that.

204
00:06:31.580 --> 00:06:34.160
This procedure will take an argument.

205
00:06:36.060 --> 00:06:36.780
And.

206
00:06:37.000 --> 00:06:38.340
That will be city name.

207
00:06:38.840 --> 00:06:38.940
Okay.

208
00:06:39.580 --> 00:06:40.840
After this it will be the same.

209
00:06:41.380 --> 00:06:42.980
We will write our code between begin and

210
00:06:42.980 --> 00:06:43.700
end.

211
00:06:45.360 --> 00:06:46.620
And this is a delimiter.

212
00:06:46.840 --> 00:06:48.040
To end this.

213
00:06:48.040 --> 00:06:49.880
To end this query.

214
00:06:49.880 --> 00:06:50.540
To end this query.

215
00:06:50.760 --> 00:06:51.540
Double forward slash.

216
00:06:53.840 --> 00:06:55.500
I will write here.

217
00:06:55.720 --> 00:06:57.940
Select star from orders.

218
00:06:58.960 --> 00:07:00.300
And I will write here.

219
00:07:00.320 --> 00:07:00.840
Where.

220
00:07:01.860 --> 00:07:03.160
Now see what I will do here.

221
00:07:03.240 --> 00:07:05.340
City is equal to city underscore name.

222
00:07:05.500 --> 00:07:06.720
Now I can use city underscore name.

223
00:07:08.540 --> 00:07:10.060
When I call it like this.

224
00:07:10.280 --> 00:07:11.980
City underscore name will be Delhi for me.

225
00:07:12.220 --> 00:07:12.860
It is like a function.

226
00:07:13.380 --> 00:07:14.200
It is like a function argument.

227
00:07:14.940 --> 00:07:16.960
City underscore name whatever you will give.

228
00:07:16.960 --> 00:07:17.660
It will come here.

229
00:07:17.820 --> 00:07:18.960
And your query will run.

230
00:07:19.780 --> 00:07:20.900
I will make this stored procedure.

231
00:07:21.380 --> 00:07:22.060
This procedure is made.

232
00:07:22.960 --> 00:07:24.080
Now I will run it.

233
00:07:24.700 --> 00:07:27.080
What is the problem here?

234
00:07:28.640 --> 00:07:30.260
Let me check.

235
00:07:30.700 --> 00:07:31.120
What is the problem?

236
00:07:31.540 --> 00:07:33.780
I wrote get orders by city.

237
00:07:35.160 --> 00:07:36.360
Delhi semicolon.

238
00:07:37.160 --> 00:07:37.760
Alright.

239
00:07:38.120 --> 00:07:39.980
I selected it and run it.

240
00:07:40.280 --> 00:07:41.620
Whenever you select and run.

241
00:07:41.820 --> 00:07:43.300
The same piece of code runs.

242
00:07:43.300 --> 00:07:45.300
And if it is an invalid piece of

243
00:07:45.300 --> 00:07:45.520
code.

244
00:07:45.700 --> 00:07:46.060
Then it does not run.

245
00:07:46.180 --> 00:07:47.780
Now I got all Delhi's orders.

246
00:07:48.800 --> 00:07:51.100
Can I take all Mumbai's orders like this?

247
00:07:52.540 --> 00:07:53.860
I run it like this.

248
00:07:54.040 --> 00:07:54.260
Yes.

249
00:07:54.500 --> 00:07:55.620
I can take all Mumbai's orders.

250
00:07:56.480 --> 00:07:57.800
Means I will get all Mumbai's orders.

251
00:07:58.640 --> 00:08:00.540
So it becomes very convenient for us.

252
00:08:00.640 --> 00:08:01.320
To use stored procedure.

253
00:08:02.860 --> 00:08:05.720
It helps us to reuse SQL logic.

254
00:08:06.780 --> 00:08:07.760
Maintainability improves.

255
00:08:08.240 --> 00:08:09.520
This is the most important thing.

256
00:08:10.060 --> 00:08:11.380
Network traffic reduces.

257
00:08:11.380 --> 00:08:13.560
If you are issuing long queries again and

258
00:08:13.560 --> 00:08:13.660
again.

259
00:08:13.700 --> 00:08:15.100
All that data is going to your SQL

260
00:08:15.100 --> 00:08:15.460
server.

261
00:08:15.760 --> 00:08:16.800
Suppose you are.

262
00:08:17.300 --> 00:08:20.040
In your hometown Delhi.

263
00:08:20.380 --> 00:08:22.020
Your server is in San Francisco.

264
00:08:22.220 --> 00:08:23.000
Your database server.

265
00:08:23.140 --> 00:08:24.480
For some reason it is in San Francisco.

266
00:08:25.460 --> 00:08:27.020
Your server is serving your app.

267
00:08:27.640 --> 00:08:28.040
It is in Delhi.

268
00:08:29.420 --> 00:08:30.820
Your server is serving your app.

269
00:08:31.299 --> 00:08:31.799
From Delhi.

270
00:08:32.360 --> 00:08:34.059
It will have to send the entire query

271
00:08:34.059 --> 00:08:34.860
data again and again.

272
00:08:35.100 --> 00:08:35.280
Where?

273
00:08:35.820 --> 00:08:36.539
San Francisco.

274
00:08:36.740 --> 00:08:39.039
Where your MySQL database is.

275
00:08:39.039 --> 00:08:41.260
So you don't want.

276
00:08:41.260 --> 00:08:41.840
So much.

277
00:08:42.620 --> 00:08:44.500
Go to the traffic network.

278
00:08:45.060 --> 00:08:46.520
Means so many long queries.

279
00:08:46.680 --> 00:08:48.880
Instead of sending a very long query like

280
00:08:48.880 --> 00:08:49.420
this.

281
00:08:49.700 --> 00:08:50.280
Which could have been even longer.

282
00:08:50.780 --> 00:08:51.980
So we took an example of a small

283
00:08:51.980 --> 00:08:52.300
query.

284
00:08:53.100 --> 00:08:55.220
You will want a small name to go.

285
00:08:55.340 --> 00:08:55.700
Only this much.

286
00:08:56.920 --> 00:08:58.040
And work.

287
00:08:58.520 --> 00:09:00.400
I hope you understood.

288
00:09:01.060 --> 00:09:03.440
How we use.

289
00:09:04.060 --> 00:09:05.540
MySQL stored procedure.

290
00:09:05.820 --> 00:09:07.380
Make your own stored procedures.

291
00:09:07.380 --> 00:09:09.460
Try out these things.

292
00:09:09.740 --> 00:09:11.160
Definitely you will get clarity.

293
00:09:11.760 --> 00:09:13.280
I hope you are enjoying this course so

294
00:09:13.280 --> 00:09:13.540
far.

295
00:09:14.040 --> 00:09:15.160
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


WEBVTT

1
00:00:00.200 --> 00:00:02.560
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we will talk about triggers.

2
00:00:03.140 --> 00:00:04.220
What are triggers?

3
00:00:04.560 --> 00:00:07.340
Trigger is a piece of SQL that automatically

4
00:00:07.340 --> 00:00:09.560
runs when a specific event happens.

5
00:00:09.740 --> 00:00:12.180
Suppose you have a table named Employee.

6
00:00:12.260 --> 00:00:15.079
In that you have a column named Salary.

7
00:00:15.580 --> 00:00:16.800
In that, there is a column named Bonus

8
00:00:16.800 --> 00:00:19.140
and another column named Total Salary.

9
00:00:19.520 --> 00:00:22.140
So, if you change the bonus, then you

10
00:00:22.140 --> 00:00:23.840
want the total salary to change as well.

11
00:00:24.020 --> 00:00:26.080
Total salary should be equal to salary plus

12
00:00:26.080 --> 00:00:26.480
bonus.

13
00:00:26.480 --> 00:00:29.800
So, you want inconsistency in your data.

14
00:00:30.280 --> 00:00:33.700
That's why if someone updates your bonus, then

15
00:00:33.700 --> 00:00:35.940
you want to update your total salary as

16
00:00:35.940 --> 00:00:36.260
well.

17
00:00:36.280 --> 00:00:38.160
And for this, there are triggers.

18
00:00:38.380 --> 00:00:40.440
That means, you did something and you want

19
00:00:40.440 --> 00:00:42.200
something else to happen additionally.

20
00:00:42.720 --> 00:00:45.400
Now, I will show you a practical scenario.

21
00:00:45.720 --> 00:00:47.200
Suppose, whenever an order gets cancelled.

22
00:00:47.640 --> 00:00:50.500
We want to store a record in the

23
00:00:50.500 --> 00:00:51.340
table of cancellations.

24
00:00:52.300 --> 00:00:54.200
And we want this to happen automatically.

25
00:00:54.200 --> 00:00:56.020
So, let's do one thing.

26
00:00:56.100 --> 00:00:57.000
We will make a table.

27
00:00:57.740 --> 00:00:59.520
And we will name that table as Order

28
00:00:59.520 --> 00:01:00.660
Underscore Cancellation.

29
00:01:01.340 --> 00:01:02.460
So, I will make this table.

30
00:01:02.840 --> 00:01:03.739
I will close this right now.

31
00:01:05.700 --> 00:01:07.340
And I will make a table named Order

32
00:01:07.340 --> 00:01:08.400
Underscore Cancellation.

33
00:01:09.560 --> 00:01:09.920
And I will make a trigger by making

34
00:01:09.920 --> 00:01:11.520
Order Underscore Cancellation table.

35
00:01:12.880 --> 00:01:14.020
So, now I will make this table only.

36
00:01:14.700 --> 00:01:15.200
I have made this table.

37
00:01:15.560 --> 00:01:16.340
You can see that there is a green

38
00:01:16.340 --> 00:01:16.780
tick here.

39
00:01:16.820 --> 00:01:18.120
That means, everything is fine.

40
00:01:19.240 --> 00:01:20.580
Now, I will comment this out.

41
00:01:20.880 --> 00:01:21.920
And what I will do here is, I

42
00:01:21.920 --> 00:01:22.600
will make a new trigger.

43
00:01:22.600 --> 00:01:25.900
So, what I am saying here is, Create

44
00:01:25.900 --> 00:01:26.880
Trigger.

45
00:01:27.740 --> 00:01:29.120
It can be any name of a trigger.

46
00:01:29.260 --> 00:01:31.040
Suppose, I make a trigger named Log Order

47
00:01:31.040 --> 00:01:32.040
Cancellation.

48
00:01:33.100 --> 00:01:36.040
And I will say here, After Update On.

49
00:01:36.160 --> 00:01:36.860
Now, what does this mean?

50
00:01:37.320 --> 00:01:39.800
Whenever there is an update in an order.

51
00:01:40.820 --> 00:01:41.520
So, what should I do?

52
00:01:41.740 --> 00:01:43.640
For each row, I will bring things between

53
00:01:43.640 --> 00:01:44.460
begin and end.

54
00:01:45.840 --> 00:01:47.680
But whenever we do this, we have to

55
00:01:47.680 --> 00:01:48.160
change the delimiter.

56
00:01:49.760 --> 00:01:51.520
So, let's double forward slash the delimiter.

57
00:01:51.520 --> 00:01:53.040
And now, let's write our logic between begin

58
00:01:53.040 --> 00:01:53.780
and end.

59
00:01:55.300 --> 00:01:56.520
So, what I will do here is, I

60
00:01:56.520 --> 00:01:57.020
will put a condition.

61
00:01:57.480 --> 00:02:01.320
And I will say, If new.OrderUnderscoreStatus is

62
00:02:01.320 --> 00:02:02.520
equal to Cancelled.

63
00:02:07.320 --> 00:02:12.960
And old.OrderUnderscoreStatus is not equal to Cancelled.

64
00:02:13.480 --> 00:02:15.240
This is our not equal to operator.

65
00:02:18.410 --> 00:02:19.590
Then, what we have to do?

66
00:02:19.750 --> 00:02:21.870
Then, we have checked a condition here.

67
00:02:22.690 --> 00:02:24.670
And if that condition is true, then what

68
00:02:24.670 --> 00:02:24.930
we will do?

69
00:02:25.130 --> 00:02:25.690
We will do anything.

70
00:02:25.690 --> 00:02:27.070
It can be an insert query.

71
00:02:27.830 --> 00:02:29.650
It can be an update query.

72
00:02:30.090 --> 00:02:30.870
What we are saying here?

73
00:02:31.050 --> 00:02:32.670
Basically, we are saying that populate our log

74
00:02:32.670 --> 00:02:35.230
table.

75
00:02:36.010 --> 00:02:36.870
So, I will copy this.

76
00:02:37.290 --> 00:02:38.390
And I will paste it here.

77
00:02:38.530 --> 00:02:40.310
So, basically, what I am doing here?

78
00:02:40.610 --> 00:02:41.710
Let me explain to you.

79
00:02:42.630 --> 00:02:47.270
I am inserting into orders underscore cancellations table.

80
00:02:47.470 --> 00:02:48.850
Order underscore cancellations table.

81
00:02:49.330 --> 00:02:51.090
Order ID, Cancelled On and Reason.

82
00:02:51.250 --> 00:02:52.990
And here, Order Reason is this.

83
00:02:52.990 --> 00:02:54.310
Order, Cancelled By User.

84
00:02:54.310 --> 00:02:55.930
And in Cancelled On, we are using Now

85
00:02:55.930 --> 00:02:56.330
function.

86
00:02:57.010 --> 00:02:57.650
Because what it will do?

87
00:02:57.830 --> 00:02:59.710
It will put the current time stamp in

88
00:02:59.710 --> 00:03:00.510
our database.

89
00:03:00.990 --> 00:03:02.990
And here, what is new.OrderUnderscoreID?

90
00:03:03.810 --> 00:03:05.250
It is the order ID after this update.

91
00:03:06.970 --> 00:03:07.670
And what is old?

92
00:03:08.170 --> 00:03:10.610
It is the order ID before the update.

93
00:03:12.950 --> 00:03:14.850
If we do old.OrderID, then it is

94
00:03:14.850 --> 00:03:15.230
order ID.

95
00:03:15.310 --> 00:03:16.490
If we do old.OrderStatus, then it is

96
00:03:16.490 --> 00:03:17.070
order status.

97
00:03:17.710 --> 00:03:18.130
So, this is all.

98
00:03:18.330 --> 00:03:19.370
So, basically, how is this working?

99
00:03:19.950 --> 00:03:21.090
And here, I am seeing what is the

100
00:03:21.090 --> 00:03:21.470
problem?

101
00:03:22.030 --> 00:03:23.890
The problem is that the delimiter is not

102
00:03:23.890 --> 00:03:24.350
changed.

103
00:03:24.570 --> 00:03:26.230
And I will change the delimiter at the

104
00:03:26.230 --> 00:03:26.330
end.

105
00:03:28.050 --> 00:03:29.010
Delimiter, semicolon.

106
00:03:29.870 --> 00:03:31.530
And here, you can see what we have

107
00:03:31.530 --> 00:03:32.510
done.

108
00:03:32.510 --> 00:03:34.350
And here, I have to end the if

109
00:03:34.350 --> 00:03:34.670
as well.

110
00:03:35.090 --> 00:03:35.950
This error is coming.

111
00:03:36.470 --> 00:03:38.290
So, I will end if here.

112
00:03:38.630 --> 00:03:39.490
And I will put a semicolon.

113
00:03:40.110 --> 00:03:41.950
So, this is a very complicated query.

114
00:03:41.990 --> 00:03:42.510
You can do it.

115
00:03:42.710 --> 00:03:44.050
But let me explain to you again.

116
00:03:44.410 --> 00:03:45.890
We have made a trigger whose name is

117
00:03:45.890 --> 00:03:46.070
this.

118
00:03:46.430 --> 00:03:46.530
Okay.

119
00:03:46.970 --> 00:03:48.510
And I wanted to name it as Cancel.

120
00:03:49.190 --> 00:03:50.730
C-E-L Okay.

121
00:03:50.870 --> 00:03:52.410
I am saying after update on orders.

122
00:03:52.570 --> 00:03:53.750
I mean, when the order table is updated.

123
00:03:53.950 --> 00:03:55.250
So, for every row, what you have to

124
00:03:55.250 --> 00:03:55.550
do?

125
00:03:56.690 --> 00:04:01.130
First of all, if new.orderStatus is cancelled.

126
00:04:01.270 --> 00:04:03.330
I mean, if the order status after updating

127
00:04:03.330 --> 00:04:03.990
is cancelled.

128
00:04:05.510 --> 00:04:07.530
And old.orderStatus is not cancelled.

129
00:04:08.270 --> 00:04:10.070
I mean, it has been cancelled.

130
00:04:10.970 --> 00:04:12.310
I mean, it was not cancelled earlier.

131
00:04:12.790 --> 00:04:13.810
Now, it is cancelled.

132
00:04:14.210 --> 00:04:14.950
So, what you have to do?

133
00:04:15.230 --> 00:04:17.649
Insert it in order underscore cancellation table.

134
00:04:18.470 --> 00:04:19.550
New order id.

135
00:04:19.810 --> 00:04:21.250
I mean, whatever the order id is.

136
00:04:21.390 --> 00:04:22.590
I mean, the order id after this update

137
00:04:22.590 --> 00:04:23.350
operation.

138
00:04:25.510 --> 00:04:26.930
Now, it is a function which will return

139
00:04:26.930 --> 00:04:27.970
the current timestamp.

140
00:04:28.830 --> 00:04:29.530
It will come in reason.

141
00:04:29.790 --> 00:04:31.170
Order cancelled by user.

142
00:04:32.030 --> 00:04:33.490
And after that, we are ending if.

143
00:04:33.690 --> 00:04:34.890
And the end of this begin is here.

144
00:04:35.110 --> 00:04:36.390
And then we have put a double forward

145
00:04:36.390 --> 00:04:36.970
slash here.

146
00:04:37.030 --> 00:04:38.090
Because this is our delimiter.

147
00:04:38.670 --> 00:04:39.990
And after this, we have changed the delimiter

148
00:04:39.990 --> 00:04:40.930
to semicolon.

149
00:04:41.810 --> 00:04:43.370
Let's run it and see if it is

150
00:04:43.370 --> 00:04:44.130
working or not.

151
00:04:44.370 --> 00:04:45.970
Because it is very important to test it.

152
00:04:45.970 --> 00:04:48.170
So, if I refresh here.

153
00:04:48.250 --> 00:04:49.130
You can see that I have got order

154
00:04:49.130 --> 00:04:50.530
underscore cancellation table.

155
00:04:51.930 --> 00:04:53.130
I will open a new query tab.

156
00:04:54.750 --> 00:05:02.290
And I will select star from order underscore

157
00:05:02.290 --> 00:05:03.370
cancellations here.

158
00:05:04.470 --> 00:05:06.450
And along with that, what I will do

159
00:05:06.450 --> 00:05:06.550
here?

160
00:05:07.070 --> 00:05:08.090
I will update before this.

161
00:05:08.190 --> 00:05:09.230
This table is empty now.

162
00:05:10.210 --> 00:05:13.550
So, I will say update orders.

163
00:05:13.730 --> 00:05:14.190
What to do?

164
00:05:14.190 --> 00:05:19.590
Let's set order underscore status is equal to

165
00:05:19.590 --> 00:05:21.310
cancelled.

166
00:05:21.870 --> 00:05:27.970
Where order id is equal to say 2.

167
00:05:28.850 --> 00:05:33.210
And after this, I will select star from

168
00:05:33.210 --> 00:05:34.850
orders.

169
00:05:37.010 --> 00:05:38.130
So, I will run this query.

170
00:05:38.690 --> 00:05:39.570
So, basically what I am doing?

171
00:05:39.750 --> 00:05:41.770
Order id 2 where my order is in

172
00:05:41.770 --> 00:05:42.010
the table.

173
00:05:42.550 --> 00:05:43.970
I am cancelling the order status there.

174
00:05:43.970 --> 00:05:46.310
And I will expect that my order underscore

175
00:05:46.310 --> 00:05:47.850
cancellations table will also populate.

176
00:05:48.350 --> 00:05:49.290
From a record.

177
00:05:49.690 --> 00:05:51.730
And in orders table, order id 2 will

178
00:05:51.730 --> 00:05:52.010
be cancelled.

179
00:05:52.470 --> 00:05:52.930
So, let's run.

180
00:05:54.190 --> 00:05:55.410
And see here, I have cancelled Neha Verma's

181
00:05:55.410 --> 00:05:55.570
order.

182
00:05:57.210 --> 00:05:59.190
And see here, order cancelled by user.

183
00:05:59.750 --> 00:06:00.870
So, basically what happened?

184
00:06:01.270 --> 00:06:03.950
My trigger was triggered.

185
00:06:04.930 --> 00:06:06.370
And what does trigger mean?

186
00:06:06.970 --> 00:06:07.950
Gun has a trigger.

187
00:06:08.190 --> 00:06:09.090
If you press it, something happens.

188
00:06:09.470 --> 00:06:10.570
So, we have made this trigger.

189
00:06:10.690 --> 00:06:12.010
If you do something, something happens.

190
00:06:12.010 --> 00:06:13.870
Like if you press the trigger, the bullet

191
00:06:13.870 --> 00:06:14.150
will fire.

192
00:06:14.750 --> 00:06:15.570
And what happens here?

193
00:06:16.590 --> 00:06:17.490
You have made a trigger.

194
00:06:17.790 --> 00:06:19.450
You are saying that if you update, this

195
00:06:19.450 --> 00:06:19.850
will happen.

196
00:06:20.490 --> 00:06:21.310
And this happened.

197
00:06:21.590 --> 00:06:21.710
Okay.

198
00:06:22.370 --> 00:06:23.970
You can also make more complicated triggers.

199
00:06:24.910 --> 00:06:25.870
In fact, you can make it with the

200
00:06:25.870 --> 00:06:26.170
help of AI.

201
00:06:27.050 --> 00:06:28.550
But again, you should understand this basic example.

202
00:06:29.630 --> 00:06:30.670
You have to ensure this.

203
00:06:30.810 --> 00:06:32.370
And if you don't understand this, it may

204
00:06:32.370 --> 00:06:33.850
seem a little complicated to you.

205
00:06:34.190 --> 00:06:35.130
It's very natural.

206
00:06:35.370 --> 00:06:35.470
Okay.

207
00:06:36.110 --> 00:06:38.750
If you find this a little complicated, So,

208
00:06:38.810 --> 00:06:39.730
I want to tell you this.

209
00:06:40.350 --> 00:06:42.490
Wait a little bit.

210
00:06:43.130 --> 00:06:45.610
Give yourself some time to understand.

211
00:06:46.050 --> 00:06:47.150
Learn it line by line.

212
00:06:47.350 --> 00:06:47.830
Understand it.

213
00:06:48.070 --> 00:06:49.270
You have chat GPT.

214
00:06:49.470 --> 00:06:50.370
You can also put it in chat GPT

215
00:06:50.370 --> 00:06:50.990
and ask.

216
00:06:51.250 --> 00:06:52.330
What is this and what is this?

217
00:06:52.770 --> 00:06:54.250
I hope you will definitely get a lot

218
00:06:54.250 --> 00:06:54.530
of help.

219
00:06:55.550 --> 00:06:55.870
So, yeah.

220
00:06:56.130 --> 00:06:59.550
That was about triggers in MySQL.

221
00:06:59.890 --> 00:07:01.810
Now, we have some more commonly used triggers.

222
00:07:02.030 --> 00:07:03.050
Like before insert.

223
00:07:03.190 --> 00:07:05.970
Which works before inserting any row.

224
00:07:06.690 --> 00:07:07.430
After insert.

225
00:07:07.430 --> 00:07:07.810
It will work after insert.

226
00:07:08.590 --> 00:07:09.490
Before update.

227
00:07:09.990 --> 00:07:10.670
Before delete.

228
00:07:11.010 --> 00:07:11.690
And after delete.

229
00:07:12.250 --> 00:07:13.230
These are very useful triggers.

230
00:07:13.710 --> 00:07:14.950
And you will have to use it.

231
00:07:15.370 --> 00:07:16.670
If you are working closely with MySQL database.

232
00:07:18.310 --> 00:07:20.030
Triggers are very very powerful.

233
00:07:20.510 --> 00:07:23.090
And their use is very obvious.

234
00:07:23.570 --> 00:07:25.290
And I know that you will find it

235
00:07:25.290 --> 00:07:27.550
very simple and straightforward.

236
00:07:28.350 --> 00:07:29.330
But again.

237
00:07:29.950 --> 00:07:30.750
They run automatically.

238
00:07:31.210 --> 00:07:32.530
You can't call them manually.

239
00:07:32.910 --> 00:07:33.910
Because they call themselves.

240
00:07:34.070 --> 00:07:35.690
Whenever you update.

241
00:07:35.690 --> 00:07:37.510
Or whenever you set a trigger.

242
00:07:37.670 --> 00:07:38.430
Whenever that thing will happen.

243
00:07:38.570 --> 00:07:39.150
Then they will run.

244
00:07:39.830 --> 00:07:41.130
And you have to use it very carefully.

245
00:07:42.350 --> 00:07:43.310
Because this is a wrong trigger.

246
00:07:43.430 --> 00:07:45.230
It can destroy your data completely.

247
00:07:46.310 --> 00:07:47.430
And you definitely don't want.

248
00:07:49.270 --> 00:07:50.670
Company's data to go bad because of you.

249
00:07:51.030 --> 00:07:52.070
At least not because of you.

250
00:07:52.830 --> 00:07:53.610
I'm kidding.

251
00:07:53.830 --> 00:07:55.090
You definitely don't want.

252
00:07:55.250 --> 00:07:56.730
Your company's data to go bad.

253
00:07:57.370 --> 00:07:58.250
You don't want in any case.

254
00:07:58.750 --> 00:07:59.770
But if it happens because of you.

255
00:08:00.090 --> 00:08:00.790
Then you will definitely feel very bad.

256
00:08:01.710 --> 00:08:02.070
So, yeah.

257
00:08:02.330 --> 00:08:03.410
I hope you are enjoying.

258
00:08:03.410 --> 00:08:05.430
So far in this course.

259
00:08:05.950 --> 00:08:07.390
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


WEBVTT

1
00:00:00.260 --> 00:00:02.140
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to see

2
00:00:02.140 --> 00:00:06.200
how you can import and export data in

3
00:00:06.200 --> 00:00:06.300
MySQL.

4
00:00:06.540 --> 00:00:09.860
Here as you can see, I have all

5
00:00:09.860 --> 00:00:11.940
the records of the orders table.

6
00:00:12.720 --> 00:00:14.600
Today I am going to tell you how

7
00:00:14.600 --> 00:00:18.820
you can use GUI, the MySQL workbench gives

8
00:00:18.820 --> 00:00:21.160
you GUI, how you can use it.

9
00:00:21.980 --> 00:00:23.240
Let's say I want to update something.

10
00:00:23.740 --> 00:00:25.280
Let's say I want to update the price

11
00:00:25.280 --> 00:00:26.840
per unit of Priya Singh, I want to

12
00:00:26.840 --> 00:00:28.520
update the price per unit of the notebook

13
00:00:28.520 --> 00:00:29.460
to 800.

14
00:00:30.360 --> 00:00:33.440
I get to know that this record was

15
00:00:33.440 --> 00:00:36.740
a wrong entry, and this notebook was of

16
00:00:36.740 --> 00:00:37.740
800 and not of 80.

17
00:00:38.380 --> 00:00:40.600
Let's say, so I will do 800 here,

18
00:00:41.320 --> 00:00:44.340
and after doing 800, you can see that

19
00:00:44.340 --> 00:00:46.240
it has changed.

20
00:00:46.520 --> 00:00:47.820
But did this change apply?

21
00:00:48.460 --> 00:00:49.460
No, it didn't apply.

22
00:00:49.680 --> 00:00:51.800
Now here you can either apply it or

23
00:00:51.800 --> 00:00:52.680
revert it.

24
00:00:52.820 --> 00:00:54.900
If you apply, then this change will be

25
00:00:54.900 --> 00:00:55.200
saved.

26
00:00:55.200 --> 00:00:58.220
If you apply once, then you can see,

27
00:00:58.440 --> 00:01:00.540
it says, review your SQL, this is going

28
00:01:00.540 --> 00:01:00.900
to apply.

29
00:01:01.220 --> 00:01:02.820
Basically, this SQL query is going to run.

30
00:01:03.420 --> 00:01:04.180
Do you want to run it?

31
00:01:04.680 --> 00:01:05.680
Yes, I want to run it.

32
00:01:05.760 --> 00:01:06.020
Apply.

33
00:01:06.460 --> 00:01:07.300
Alright, and finish.

34
00:01:07.500 --> 00:01:09.240
And this SQL query will be executed.

35
00:01:09.980 --> 00:01:12.800
And now if I run it again, then

36
00:01:12.800 --> 00:01:16.360
Priya Singh bought the notebook, and the price

37
00:01:16.360 --> 00:01:17.040
per unit is 800.

38
00:01:17.280 --> 00:01:20.960
Along with that, let's say I want to

39
00:01:20.960 --> 00:01:21.280
change something else.

40
00:01:21.280 --> 00:01:23.980
Let's say Dr. Amit, I get to know

41
00:01:23.980 --> 00:01:24.800
that he doesn't live in Delhi.

42
00:01:25.480 --> 00:01:30.180
Dr. Amit lives, let's say, in Begusarai.

43
00:01:31.000 --> 00:01:33.080
Alright, so I will make Dr. Amit's city

44
00:01:33.080 --> 00:01:33.660
Begusarai.

45
00:01:34.200 --> 00:01:36.700
And I will click on apply, and you

46
00:01:36.700 --> 00:01:37.580
can see that it has automatically generated the

47
00:01:37.580 --> 00:01:37.860
SQL.

48
00:01:38.580 --> 00:01:40.560
MySQL Workbench has applied, finish.

49
00:01:41.000 --> 00:01:42.600
And now if I run it again, then

50
00:01:42.600 --> 00:01:45.000
it is permanently saved in the database.

51
00:01:46.120 --> 00:01:47.840
Now let's say that someone made a mistake,

52
00:01:47.840 --> 00:01:49.380
he made a mistake in the data.

53
00:01:50.580 --> 00:01:52.180
He made a mistake in the fun.

54
00:01:53.660 --> 00:01:55.120
Now you see, what did he do with

55
00:01:55.120 --> 00:01:55.520
my data?

56
00:01:56.480 --> 00:01:57.820
Don't be scared, you can revert.

57
00:01:58.380 --> 00:01:59.700
Click on revert, everything will be fine.

58
00:02:00.420 --> 00:02:02.260
And if you run it again, then your

59
00:02:02.260 --> 00:02:03.180
data is fine, it hasn't gone anywhere.

60
00:02:03.840 --> 00:02:05.600
So you can apply, you can revert.

61
00:02:06.320 --> 00:02:07.979
Now sometimes what happens is that our record

62
00:02:07.979 --> 00:02:08.539
is very long.

63
00:02:08.900 --> 00:02:10.360
That means we have a lot of columns.

64
00:02:10.960 --> 00:02:13.620
And let's say that I take Arjun Mehta

65
00:02:13.620 --> 00:02:13.800
here.

66
00:02:14.600 --> 00:02:15.780
Arjun Mehta lives in Ahmedabad.

67
00:02:15.780 --> 00:02:16.740
Let's say I want to make a lot

68
00:02:16.740 --> 00:02:17.260
of changes for Arjun Mehta.

69
00:02:18.720 --> 00:02:19.080
So I will use form editor instead of

70
00:02:19.080 --> 00:02:19.860
result grade.

71
00:02:21.380 --> 00:02:21.960
Do you see this form editor?

72
00:02:22.560 --> 00:02:23.540
I will use this form editor.

73
00:02:25.120 --> 00:02:26.920
One very good advantage of using form editor

74
00:02:26.920 --> 00:02:28.360
is that I can see the data in

75
00:02:28.360 --> 00:02:28.700
form in this way.

76
00:02:29.480 --> 00:02:31.200
Let's say I want to do P capital

77
00:02:31.200 --> 00:02:31.720
of the smartphone.

78
00:02:32.320 --> 00:02:33.280
That I have to do P capital.

79
00:02:34.200 --> 00:02:35.800
And suppose I have a field in which

80
00:02:35.800 --> 00:02:37.020
there is a very long text.

81
00:02:37.540 --> 00:02:38.780
Or there is something that I want to

82
00:02:38.780 --> 00:02:39.040
see carefully.

83
00:02:39.840 --> 00:02:41.460
So I can do something like this, make

84
00:02:41.460 --> 00:02:42.960
changes and apply.

85
00:02:42.960 --> 00:02:47.640
And here you can see that an update

86
00:02:47.640 --> 00:02:48.780
SQL has been generated.

87
00:02:49.340 --> 00:02:50.920
I can apply it by applying it.

88
00:02:51.260 --> 00:02:51.960
I can finish it.

89
00:02:52.600 --> 00:02:54.960
Now if I run it again, you can

90
00:02:54.960 --> 00:02:55.700
see that the P capital of Arjun Mehta's

91
00:02:55.700 --> 00:02:56.940
smartphone has become.

92
00:02:57.360 --> 00:02:59.180
And if I want, I can revert it.

93
00:02:59.320 --> 00:03:00.860
I will apply it again like this.

94
00:03:03.260 --> 00:03:03.620
Apply.

95
00:03:04.300 --> 00:03:04.660
Apply.

96
00:03:05.140 --> 00:03:05.620
Finish.

97
00:03:05.720 --> 00:03:08.060
And if I run it again, you can

98
00:03:08.060 --> 00:03:10.560
see that it has been applied.

99
00:03:10.560 --> 00:03:13.440
Now I will tell you how you can

100
00:03:13.440 --> 00:03:14.360
export it in CSV.

101
00:03:15.620 --> 00:03:18.340
Let's say I want to have a CSV

102
00:03:18.340 --> 00:03:18.780
here.

103
00:03:18.940 --> 00:03:20.220
Data.csv or something.

104
00:03:20.960 --> 00:03:21.560
So what will I do?

105
00:03:22.120 --> 00:03:23.240
Can you see this export import?

106
00:03:23.820 --> 00:03:24.620
I will click here.

107
00:03:25.280 --> 00:03:26.700
And now see here it is asking me

108
00:03:26.700 --> 00:03:28.000
that brother, what name do you want to

109
00:03:28.000 --> 00:03:28.340
save?

110
00:03:28.380 --> 00:03:28.760
I will save it in the name of

111
00:03:28.760 --> 00:03:31.780
data.csv. And I should have a CSV

112
00:03:31.780 --> 00:03:32.460
here.

113
00:03:32.920 --> 00:03:33.520
It is made.

114
00:03:34.180 --> 00:03:35.240
Can I open it?

115
00:03:36.220 --> 00:03:36.560
Absolutely.

116
00:03:37.080 --> 00:03:37.720
This data is mine.

117
00:03:37.880 --> 00:03:38.480
I can open it.

118
00:03:39.300 --> 00:03:39.840
Very good.

119
00:03:39.840 --> 00:03:41.060
Now you can see this data.

120
00:03:42.000 --> 00:03:44.160
We have learned a little bit of Excel.

121
00:03:44.880 --> 00:03:46.860
You can see here that I can see

122
00:03:46.860 --> 00:03:47.400
the order date.

123
00:03:48.160 --> 00:03:48.600
I can see everything.

124
00:03:48.760 --> 00:03:49.340
Very good.

125
00:03:49.500 --> 00:03:51.180
I am very satisfied.

126
00:03:51.500 --> 00:03:51.620
Okay.

127
00:03:51.920 --> 00:03:52.740
I am very satisfied.

128
00:03:53.440 --> 00:03:54.320
I am getting to see all the data.

129
00:03:54.760 --> 00:03:55.880
So whenever you want to bring data from

130
00:03:55.880 --> 00:03:58.140
SQL to Excel, you can bring it.

131
00:03:59.040 --> 00:04:02.120
And you run your select star queries.

132
00:04:02.620 --> 00:04:03.080
Do filtering.

133
00:04:03.420 --> 00:04:04.260
A little bit of data will come.

134
00:04:04.340 --> 00:04:04.880
Take it in Excel.

135
00:04:05.060 --> 00:04:07.120
And after taking it in Excel, you can

136
00:04:07.120 --> 00:04:08.240
do the same analysis here.

137
00:04:08.240 --> 00:04:11.240
Which maybe you know very well.

138
00:04:11.780 --> 00:04:11.920
Okay.

139
00:04:12.480 --> 00:04:14.120
Now assume that I want to import some

140
00:04:14.120 --> 00:04:14.380
data.

141
00:04:15.100 --> 00:04:16.560
Let's say I have two rows.

142
00:04:16.760 --> 00:04:17.420
So I will do one thing.

143
00:04:17.860 --> 00:04:18.640
We had the order ID up to 12.

144
00:04:20.320 --> 00:04:21.100
What will I do?

145
00:04:21.320 --> 00:04:22.160
Order ID 13.

146
00:04:22.680 --> 00:04:23.540
And order ID 14.

147
00:04:24.300 --> 00:04:24.800
I will make its data.

148
00:04:25.560 --> 00:04:27.220
Assume that Shubham is there.

149
00:04:27.280 --> 00:04:28.420
And Vikrant is there.

150
00:04:28.500 --> 00:04:28.660
Okay.

151
00:04:28.840 --> 00:04:29.540
I will capitalize Vikrant's V.

152
00:04:30.120 --> 00:04:30.740
Otherwise he will get angry.

153
00:04:31.900 --> 00:04:32.140
Yes.

154
00:04:32.800 --> 00:04:36.320
And let's say Shubham's city is Jaipur.

155
00:04:36.320 --> 00:04:39.320
And let's say Vikrant's Bangalore.

156
00:04:40.600 --> 00:04:41.760
And let it be like this.

157
00:04:41.980 --> 00:04:43.000
Assume quantity is 3.

158
00:04:43.440 --> 00:04:45.800
And Vikrant has bought these 444 headphones.

159
00:04:46.340 --> 00:04:47.660
I don't know which song he will listen

160
00:04:47.660 --> 00:04:47.760
to.

161
00:04:48.400 --> 00:04:51.440
Now this is 566 and 900.

162
00:04:51.820 --> 00:04:52.320
1, 1.

163
00:04:52.900 --> 00:04:53.140
Sorry.

164
00:04:53.260 --> 00:04:53.700
This is 90,000.

165
00:04:54.780 --> 00:04:55.500
Price per unit.

166
00:04:55.600 --> 00:04:56.220
Which headphone is it?

167
00:04:56.320 --> 00:04:56.620
It is more expensive than Apple.

168
00:04:57.100 --> 00:04:57.260
Okay.

169
00:04:57.320 --> 00:04:57.600
No problem.

170
00:04:58.040 --> 00:04:59.540
Let's give a 12% discount.

171
00:04:59.720 --> 00:05:00.960
Let's give it 5%.

172
00:05:00.960 --> 00:05:02.640
Now here on the date, I want to

173
00:05:02.640 --> 00:05:03.600
give a very important tip.

174
00:05:04.820 --> 00:05:08.060
MySQL takes the date yyymmdd.

175
00:05:08.220 --> 00:05:09.080
Means you have to date in the format

176
00:05:09.080 --> 00:05:10.680
of yyymmdd.

177
00:05:12.360 --> 00:05:13.540
So you can go here.

178
00:05:14.200 --> 00:05:15.040
You can go to date.

179
00:05:16.220 --> 00:05:18.600
And here you will get yyymmdd.

180
00:05:19.520 --> 00:05:20.420
So you need this format.

181
00:05:21.280 --> 00:05:22.360
Because if you have not taken this format,

182
00:05:23.020 --> 00:05:23.980
then you will have a problem.

183
00:05:24.580 --> 00:05:25.640
Assume they got the same delivery.

184
00:05:26.220 --> 00:05:27.140
Let's do one thing.

185
00:05:27.140 --> 00:05:27.760
Let's give the delivery after a day.

186
00:05:29.320 --> 00:05:30.480
So you have to do this thing.

187
00:05:30.700 --> 00:05:31.620
Means you have to correct the format date.

188
00:05:32.420 --> 00:05:32.940
Otherwise it will not work.

189
00:05:32.940 --> 00:05:34.240
And assume both have been delivered.

190
00:05:34.820 --> 00:05:34.920
Okay.

191
00:05:35.940 --> 00:05:37.600
Assume both had a seller ID of 2.

192
00:05:38.360 --> 00:05:39.400
Rating 5, 4.

193
00:05:39.520 --> 00:05:39.720
Okay.

194
00:05:39.980 --> 00:05:40.760
Let's save it.

195
00:05:41.500 --> 00:05:42.920
Now I come to MySQL Workbench.

196
00:05:43.420 --> 00:05:43.920
This data.

197
00:05:44.080 --> 00:05:45.740
Which is my data.csv. Which I have

198
00:05:45.740 --> 00:05:46.080
just saved.

199
00:05:46.280 --> 00:05:47.080
I can import this.

200
00:05:47.380 --> 00:05:48.180
And I can add my rows.

201
00:05:49.320 --> 00:05:50.120
So I will click here.

202
00:05:51.060 --> 00:05:51.400
I will go to next.

203
00:05:52.820 --> 00:05:54.000
Use existing table.

204
00:05:54.100 --> 00:05:54.740
Either I can make a new table.

205
00:05:55.140 --> 00:05:55.760
Or I can add it in the existing

206
00:05:55.760 --> 00:05:56.240
table.

207
00:05:57.500 --> 00:05:58.800
Like I am going to do here in

208
00:05:58.800 --> 00:05:59.080
orders.

209
00:06:00.240 --> 00:06:00.920
Where did orders go?

210
00:06:01.040 --> 00:06:01.440
Here it is.

211
00:06:01.440 --> 00:06:03.040
Ecom.orders. Okay.

212
00:06:03.160 --> 00:06:03.660
I will show you.

213
00:06:03.780 --> 00:06:04.560
This is my orders table.

214
00:06:06.140 --> 00:06:06.960
After this I will do next.

215
00:06:08.420 --> 00:06:09.340
After doing next.

216
00:06:09.740 --> 00:06:10.580
It is telling me.

217
00:06:10.720 --> 00:06:11.160
Look brother.

218
00:06:11.320 --> 00:06:13.400
You are going to be inserted like this.

219
00:06:13.640 --> 00:06:14.000
Rows.

220
00:06:14.720 --> 00:06:15.400
I will do next.

221
00:06:16.280 --> 00:06:17.040
I will do next.

222
00:06:18.300 --> 00:06:19.520
And then I will do next again.

223
00:06:19.560 --> 00:06:20.160
And finish it.

224
00:06:20.300 --> 00:06:21.560
It is saying that 2 records have been

225
00:06:21.560 --> 00:06:21.920
imported.

226
00:06:23.460 --> 00:06:23.900
Finish.

227
00:06:24.100 --> 00:06:25.140
And if I run this query again.

228
00:06:25.480 --> 00:06:26.440
Select start from orders.

229
00:06:26.560 --> 00:06:26.800
You see.

230
00:06:26.880 --> 00:06:27.480
13 and 14.

231
00:06:27.600 --> 00:06:28.680
Shubham and Vikrant have been added.

232
00:06:28.920 --> 00:06:29.620
Jaipur Bangalore.

233
00:06:29.620 --> 00:06:30.040
Laptop.

234
00:06:30.100 --> 00:06:30.540
Headset.

235
00:06:31.360 --> 00:06:31.640
Headphones.

236
00:06:32.400 --> 00:06:32.960
Electronics.

237
00:06:33.200 --> 00:06:33.520
3.

238
00:06:33.780 --> 00:06:34.100
4.

239
00:06:34.180 --> 00:06:34.280
4.

240
00:06:34.300 --> 00:06:34.420
4.

241
00:06:34.480 --> 00:06:34.660
5.

242
00:06:34.680 --> 00:06:34.840
6.

243
00:06:34.840 --> 00:06:35.020
6.

244
00:06:35.080 --> 00:06:35.560
90,000.

245
00:06:35.680 --> 00:06:35.880
1.

246
00:06:35.920 --> 00:06:36.080
1.

247
00:06:36.960 --> 00:06:38.740
And all this data has been imported from

248
00:06:38.740 --> 00:06:38.840
here.

249
00:06:39.480 --> 00:06:41.000
So you can import data from an excel

250
00:06:41.000 --> 00:06:41.400
file.

251
00:06:41.580 --> 00:06:41.980
From CSV.

252
00:06:43.220 --> 00:06:45.120
In your SQL.

253
00:06:45.400 --> 00:06:46.300
In your database.

254
00:06:47.060 --> 00:06:48.760
And you can use that.

255
00:06:49.060 --> 00:06:49.760
To do that.

256
00:06:49.940 --> 00:06:51.140
MySQL workbench.

257
00:06:51.580 --> 00:06:53.440
And the export import of MySQL workbench.

258
00:06:53.680 --> 00:06:54.380
Works very well.

259
00:06:55.560 --> 00:06:57.180
You can export as CSV.

260
00:06:57.460 --> 00:06:59.120
You can import from CSV.

261
00:06:59.120 --> 00:06:59.880
Very good.

262
00:07:00.580 --> 00:07:01.140
Now suppose.

263
00:07:01.260 --> 00:07:02.160
I want to empty the data table.

264
00:07:03.520 --> 00:07:04.160
I see.

265
00:07:04.260 --> 00:07:04.900
Is the data table empty?

266
00:07:05.140 --> 00:07:05.300
No.

267
00:07:05.620 --> 00:07:06.380
The data table is not empty.

268
00:07:06.860 --> 00:07:07.860
Let's say I want to empty it.

269
00:07:08.400 --> 00:07:08.980
I will right click.

270
00:07:09.440 --> 00:07:10.460
And here I will do truncate table.

271
00:07:11.540 --> 00:07:12.500
I will review SQL.

272
00:07:12.680 --> 00:07:12.800
Okay.

273
00:07:13.080 --> 00:07:13.740
Truncate table.

274
00:07:13.860 --> 00:07:14.560
Truncate means.

275
00:07:14.780 --> 00:07:15.440
The table is getting empty.

276
00:07:15.620 --> 00:07:16.220
I will execute.

277
00:07:16.480 --> 00:07:17.040
And now I will run.

278
00:07:17.200 --> 00:07:17.520
You see.

279
00:07:17.620 --> 00:07:18.720
The table is completely empty here.

280
00:07:19.500 --> 00:07:19.680
So.

281
00:07:20.020 --> 00:07:20.880
You can do a lot of work from

282
00:07:20.880 --> 00:07:21.060
here.

283
00:07:22.080 --> 00:07:23.260
You can right click here.

284
00:07:23.340 --> 00:07:23.900
And refresh all.

285
00:07:24.280 --> 00:07:25.000
Everything will be refreshed.

286
00:07:25.560 --> 00:07:26.580
You can search table data.

287
00:07:27.460 --> 00:07:27.800
And here.

288
00:07:28.280 --> 00:07:28.560
You.

289
00:07:28.700 --> 00:07:29.100
You.

290
00:07:30.620 --> 00:07:30.860
You.

291
00:07:37.020 --> 00:07:37.260
You.

292
00:07:45.460 --> 00:07:45.700
You.

293
00:07:45.860 --> 00:07:46.100
You.

294
00:07:46.100 --> 00:07:46.280
You.

295
00:07:48.980 --> 00:07:49.220
You.

296
00:07:55.200 --> 00:07:55.440
You.

297
00:07:57.760 --> 00:07:58.000
You.

298
00:07:58.500 --> 00:07:58.740
You.

299
00:07:58.740 --> 00:07:58.840
You.

300
00:07:58.840 --> 00:07:58.940
You.

301
00:07:58.940 --> 00:07:59.040
You.

302
00:07:59.040 --> 00:07:59.140
You.

303
00:07:59.140 --> 00:07:59.240
You.

304
00:07:59.240 --> 00:07:59.340
You.

305
00:07:59.340 --> 00:07:59.440
You.

306
00:07:59.440 --> 00:07:59.540
You.

307
00:07:59.540 --> 00:07:59.640
You.

308
00:08:02.180 --> 00:08:02.740
You.

309
00:08:10.340 --> 00:08:10.900
You.

310
00:08:11.020 --> 00:08:11.120
You.

311
00:08:11.480 --> 00:08:12.040
You.

312
00:08:12.960 --> 00:08:13.520
You.

313
00:08:14.520 --> 00:08:14.860
You.

314
00:08:20.780 --> 00:08:21.340
You.

315
00:08:23.660 --> 00:08:24.220
You.

316
00:08:24.600 --> 00:08:24.880
You.

317
00:08:25.540 --> 00:08:25.700
You.

318
00:08:28.840 --> 00:08:28.940
You.

319
00:08:28.940 --> 00:08:29.040
You.

320
00:08:29.040 --> 00:08:29.140
You.

321
00:08:29.140 --> 00:08:29.240
You.

322
00:08:29.240 --> 00:08:29.340
You.

323
00:08:29.340 --> 00:08:33.100
I want to make one more index, I

324
00:08:33.100 --> 00:08:36.299
can do it by right clicking and selecting

325
00:08:36.299 --> 00:08:39.179
any column and click on create index for

326
00:08:39.179 --> 00:08:41.320
selected column and it will become an index.

327
00:08:41.860 --> 00:08:45.440
I highly strongly recommend that you make it

328
00:08:45.440 --> 00:08:47.740
from SQL only, i.e. by issuing queries

329
00:08:47.740 --> 00:08:48.360
only.

330
00:08:49.020 --> 00:08:51.740
Don't make too many changes here because your

331
00:08:51.740 --> 00:08:52.360
data can get corrupted.

332
00:08:53.120 --> 00:08:54.160
This is a warning from me.

333
00:08:54.800 --> 00:08:57.520
But again, you can do things like dropping

334
00:08:57.520 --> 00:08:58.020
a table.

335
00:08:58.660 --> 00:09:00.280
It becomes easy, i.e. who can write

336
00:09:00.280 --> 00:09:01.900
such a big SQL.

337
00:09:02.380 --> 00:09:04.840
And export-import, it is obvious that you

338
00:09:04.840 --> 00:09:05.180
can do it.

339
00:09:05.800 --> 00:09:07.920
So, if you right click and select rows

340
00:09:07.920 --> 00:09:09.660
here, you have to see the data quickly.

341
00:09:09.800 --> 00:09:11.160
So, where will you write select star from?

342
00:09:11.700 --> 00:09:13.620
Right click and click on select rows.

343
00:09:14.460 --> 00:09:15.020
You will see the data.

344
00:09:15.400 --> 00:09:17.680
Suppose, I want to see order cancellation, I

345
00:09:17.680 --> 00:09:19.180
will select rows and data will be seen.

346
00:09:19.540 --> 00:09:21.260
So, you can do such quick operations.

347
00:09:22.240 --> 00:09:25.640
I hope that you got to use the

348
00:09:25.640 --> 00:09:27.540
GUI editor of MySQL Workbench.

349
00:09:30.200 --> 00:09:31.960
And I hope you are enjoying this course

350
00:09:31.960 --> 00:09:32.460
so far.

351
00:09:32.900 --> 00:09:34.380
See you in the next video.


━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.330 --> 00:00:03.210
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, as you might have seen what

2
00:00:03.210 --> 00:00:04.050
is open here.

3
00:00:04.390 --> 00:00:06.030
And whenever it opens, it is fun.

4
00:00:06.990 --> 00:00:10.010
ChatGPT 5.2 Yes, we are going to

5
00:00:10.010 --> 00:00:12.230
generate queries with the help of AI.

6
00:00:12.750 --> 00:00:14.170
So, how to do it?

7
00:00:14.550 --> 00:00:16.790
What kind of things we have to do?

8
00:00:17.270 --> 00:00:18.650
What kind of greed we have to avoid?

9
00:00:18.870 --> 00:00:19.570
I will tell you all this.

10
00:00:20.330 --> 00:00:22.970
So see, AI will amplify your SQL skills.

11
00:00:23.930 --> 00:00:24.790
First of all, understand this.

12
00:00:25.150 --> 00:00:26.550
Don't think that the one who doesn't know

13
00:00:26.550 --> 00:00:29.430
SQL, he will do a lot by using

14
00:00:29.430 --> 00:00:29.530
AI.

15
00:00:29.530 --> 00:00:30.710
If you don't know all the SQL that

16
00:00:30.710 --> 00:00:33.650
I have taught you till now, then you

17
00:00:33.650 --> 00:00:34.790
can't do anything with AI.

18
00:00:35.070 --> 00:00:36.850
You yourself tell me one thing.

19
00:00:36.990 --> 00:00:38.710
Suppose someone brings a bad car to you.

20
00:00:39.410 --> 00:00:40.790
I am assuming that you don't know how

21
00:00:40.790 --> 00:00:41.350
to repair a car.

22
00:00:41.630 --> 00:00:42.530
We are talking about a four-wheeler car.

23
00:00:42.990 --> 00:00:44.790
Suppose someone brought a Fortuner, his car broke

24
00:00:44.790 --> 00:00:45.650
down, he said that it is not working.

25
00:00:46.050 --> 00:00:48.210
Now you say that I will do it

26
00:00:48.210 --> 00:00:48.310
with AI.

27
00:00:48.890 --> 00:00:50.590
You will ask AI that this Fortuner is

28
00:00:50.590 --> 00:00:50.890
not starting.

29
00:00:51.690 --> 00:00:53.270
So what should I do?

30
00:00:53.710 --> 00:00:55.410
And behave like a car mechanic.

31
00:00:56.230 --> 00:00:57.950
And tell me how to repair a Fortuner.

32
00:00:58.350 --> 00:00:59.030
You won't be able to do it.

33
00:00:59.510 --> 00:01:01.270
If you ask AI, it will tell you.

34
00:01:01.710 --> 00:01:03.370
And even after that, you won't be able

35
00:01:03.370 --> 00:01:03.470
to do anything.

36
00:01:03.610 --> 00:01:05.910
But an existing mechanic who has 5 years

37
00:01:05.910 --> 00:01:08.730
of experience, he can amplify his knowledge or

38
00:01:08.730 --> 00:01:09.330
information.

39
00:01:12.050 --> 00:01:13.830
And by amplifying, if he doesn't know anything,

40
00:01:14.430 --> 00:01:16.450
he can ask AI to do this or

41
00:01:16.450 --> 00:01:16.750
that.

42
00:01:16.870 --> 00:01:18.070
Then AI will tell you not to do

43
00:01:18.070 --> 00:01:19.230
this, do this because this happens.

44
00:01:19.830 --> 00:01:21.130
Do you understand what I am saying?

45
00:01:21.130 --> 00:01:23.930
And the person who understood this application of

46
00:01:23.930 --> 00:01:26.250
AI, he became successful.

47
00:01:27.050 --> 00:01:27.730
It's a simple thing.

48
00:01:28.030 --> 00:01:31.590
So let's see how we will use AI.

49
00:01:32.090 --> 00:01:33.490
So what will I do here?

50
00:01:33.650 --> 00:01:35.350
I haven't made my order stable here.

51
00:01:35.690 --> 00:01:37.210
I wish I hadn't made the order stable.

52
00:01:37.490 --> 00:01:39.170
And if I had made it, then I

53
00:01:39.170 --> 00:01:39.270
would have generated the order stable from the

54
00:01:39.270 --> 00:01:40.050
starter SQL.

55
00:01:42.050 --> 00:01:43.130
I didn't make it, so this is my

56
00:01:43.130 --> 00:01:43.690
order stable.

57
00:01:44.130 --> 00:01:45.070
So what will I do now?

58
00:01:45.110 --> 00:01:46.210
I will click on orders here.

59
00:01:46.430 --> 00:01:47.850
You see how I am doing things.

60
00:01:48.510 --> 00:01:50.030
You have to learn to copy this first.

61
00:01:51.010 --> 00:01:53.070
You tell it, this is my order stable.

62
00:01:53.310 --> 00:01:54.310
You gave it a table.

63
00:01:55.450 --> 00:01:59.030
You tell it, this is my order stable.

64
00:01:59.670 --> 00:02:03.610
Tell me how to get all the delivered

65
00:02:03.610 --> 00:02:07.110
orders in MySQL.

66
00:02:08.090 --> 00:02:09.970
Now tell me which SQL are you using?

67
00:02:10.090 --> 00:02:10.670
Are you using MySQL?

68
00:02:11.290 --> 00:02:11.870
Are you using Postgres?

69
00:02:12.730 --> 00:02:13.930
And it will give it to you.

70
00:02:14.070 --> 00:02:14.930
It has given it to you.

71
00:02:15.090 --> 00:02:15.870
You copy it here.

72
00:02:16.370 --> 00:02:19.230
And as you copied it here, you see

73
00:02:19.230 --> 00:02:20.930
here, paste it.

74
00:02:21.290 --> 00:02:22.450
And run it.

75
00:02:22.750 --> 00:02:23.590
And you see, it will give all the

76
00:02:23.590 --> 00:02:24.230
delivered orders.

77
00:02:25.210 --> 00:02:28.690
Now if I tell it, Now return all

78
00:02:28.690 --> 00:02:35.830
the delivered orders using orders.

79
00:02:36.090 --> 00:02:40.790
And they should be paid using UPI.

80
00:02:41.910 --> 00:02:42.850
Now see here.

81
00:02:43.470 --> 00:02:45.090
Now it doesn't know that in payment mode,

82
00:02:45.270 --> 00:02:46.650
my UPI is written like this.

83
00:02:46.650 --> 00:02:49.550
Maybe UPI is written in small.

84
00:02:50.170 --> 00:02:52.270
But here it is telling me that if

85
00:02:52.270 --> 00:02:54.110
UPI is written like this in your database,

86
00:02:54.270 --> 00:02:54.870
then use this.

87
00:02:54.990 --> 00:02:57.230
If you are sure that UPI is in

88
00:02:57.230 --> 00:02:58.050
capital, then use this.

89
00:02:58.950 --> 00:02:59.970
So let's use this.

90
00:03:01.150 --> 00:03:02.410
And in this way, you can also use

91
00:03:02.410 --> 00:03:02.990
UPI.

92
00:03:03.890 --> 00:03:06.690
If I give it complex things, then it

93
00:03:06.690 --> 00:03:08.290
will also generate complex queries for me.

94
00:03:09.350 --> 00:03:11.170
Now if I say it like this, I

95
00:03:11.170 --> 00:03:15.830
want all the orders where at least one

96
00:03:15.830 --> 00:03:22.450
of the items are from other category.

97
00:03:23.110 --> 00:03:24.230
Let me see, category, yes.

98
00:03:25.150 --> 00:03:26.150
Other category.

99
00:03:26.670 --> 00:03:28.490
I am saying, I want all orders where

100
00:03:28.490 --> 00:03:33.930
there is at least one of the items

101
00:03:33.930 --> 00:03:35.270
from another category.

102
00:03:35.850 --> 00:03:36.790
Do you understand what I said?

103
00:03:36.790 --> 00:03:39.590
I said that it should also be of

104
00:03:39.590 --> 00:03:40.390
another category.

105
00:03:41.170 --> 00:03:43.010
And here you see, it will create logic.

106
00:03:43.610 --> 00:03:44.390
And see, it has created logic.

107
00:03:44.910 --> 00:03:46.070
Now if you use this logic in your

108
00:03:46.070 --> 00:03:48.310
mind, then it will take time.

109
00:03:48.690 --> 00:03:50.810
But at the same time, sometimes AI can

110
00:03:50.810 --> 00:03:51.890
also misunderstand you.

111
00:03:52.370 --> 00:03:53.490
So what you have to do is, you

112
00:03:53.490 --> 00:03:53.870
have to wed this query.

113
00:03:54.570 --> 00:03:55.110
Now see here.

114
00:03:55.510 --> 00:03:57.050
We are saying, select start from orders where

115
00:03:57.050 --> 00:03:58.210
order ID in.

116
00:03:58.690 --> 00:03:59.410
And this is subquery.

117
00:03:59.570 --> 00:04:00.790
Now you know what subquery is.

118
00:04:00.970 --> 00:04:02.470
If you don't know what subquery is, then

119
00:04:02.470 --> 00:04:03.270
what will you do with AI?

120
00:04:03.870 --> 00:04:06.050
So what we are saying is, select order

121
00:04:06.050 --> 00:04:08.990
ID from orders, group by order ID, having

122
00:04:08.990 --> 00:04:11.430
count distinct category greater than 1.

123
00:04:12.150 --> 00:04:14.150
Now why didn't it give me anything?

124
00:04:14.330 --> 00:04:15.630
Why didn't it give me anything?

125
00:04:16.290 --> 00:04:17.910
To know this, we will select start from

126
00:04:17.910 --> 00:04:18.170
orders.

127
00:04:18.670 --> 00:04:20.130
And we will understand why it didn't give.

128
00:04:20.390 --> 00:04:22.010
So see, what did we say here?

129
00:04:22.330 --> 00:04:24.250
That at least, there should be another order

130
00:04:24.250 --> 00:04:27.210
from some other category.

131
00:04:27.710 --> 00:04:29.610
Now it is matching order ID here.

132
00:04:29.690 --> 00:04:31.730
But my question is, I didn't ask correctly

133
00:04:31.730 --> 00:04:31.870
here.

134
00:04:32.150 --> 00:04:36.270
I want all orders where the city has

135
00:04:36.270 --> 00:04:40.210
I should have written, the city has at

136
00:04:40.210 --> 00:04:42.210
least one of the items from another category.

137
00:04:42.530 --> 00:04:43.730
I should have said this.

138
00:04:44.070 --> 00:04:45.410
Now it will do it on city, not

139
00:04:45.410 --> 00:04:45.810
on order ID.

140
00:04:46.290 --> 00:04:47.150
Now see here.

141
00:04:47.870 --> 00:04:49.910
It has made something like this.

142
00:04:50.450 --> 00:04:51.350
Using exists.

143
00:04:51.870 --> 00:04:52.790
We will copy this.

144
00:04:53.010 --> 00:04:54.710
Now it has understood me correctly.

145
00:04:55.170 --> 00:04:56.010
I will run this.

146
00:04:56.590 --> 00:04:58.750
Now see, I have only got those orders

147
00:04:58.750 --> 00:05:02.610
where at least there is one item from

148
00:05:02.610 --> 00:05:03.210
another category.

149
00:05:03.210 --> 00:05:04.630
See, it has taken Mumbai city.

150
00:05:05.170 --> 00:05:06.670
Because it is a headphone and water bottle.

151
00:05:06.930 --> 00:05:08.350
It has taken Delhi, because there is a

152
00:05:08.350 --> 00:05:08.850
table lamp in Delhi.

153
00:05:09.210 --> 00:05:10.790
It has taken Bangalore, because there is a

154
00:05:10.790 --> 00:05:11.210
headphone in Bangalore.

155
00:05:11.630 --> 00:05:12.930
So here, what did we simply do?

156
00:05:13.090 --> 00:05:17.510
We said, where there exists one such at

157
00:05:17.510 --> 00:05:21.390
least one such order where O2.city is

158
00:05:21.390 --> 00:05:22.730
equal to O1.city. Now what is O1?

159
00:05:22.970 --> 00:05:23.570
O1 is this.

160
00:05:23.930 --> 00:05:24.410
All rows.

161
00:05:24.490 --> 00:05:26.170
Its first row is O1.

162
00:05:26.350 --> 00:05:28.570
And after that, we are comparing it with

163
00:05:28.570 --> 00:05:29.010
O2.

164
00:05:29.570 --> 00:05:31.570
So basically, we are iterating here to get

165
00:05:31.570 --> 00:05:32.070
O2 back.

166
00:05:32.370 --> 00:05:33.250
And this is the right query.

167
00:05:33.490 --> 00:05:33.890
And it will work.

168
00:05:34.150 --> 00:05:35.790
So in this way, you can generate a

169
00:05:35.790 --> 00:05:38.950
query from chat.gpt. Let me tell you

170
00:05:38.950 --> 00:05:39.270
something.

171
00:05:39.630 --> 00:05:41.030
If you are doing English to SQL.

172
00:05:41.570 --> 00:05:43.110
Basically, I will call it prompt to SQL

173
00:05:43.110 --> 00:05:43.870
or English to SQL.

174
00:05:44.530 --> 00:05:46.390
Whenever you are doing English to SQL, tell

175
00:05:46.390 --> 00:05:48.250
it to understand.

176
00:05:48.450 --> 00:05:49.330
By the way, it is explaining.

177
00:05:49.590 --> 00:05:50.550
You don't ignore it.

178
00:05:50.690 --> 00:05:51.270
Definitely read it.

179
00:05:51.350 --> 00:05:53.090
And it will tell you how it works.

180
00:05:53.750 --> 00:05:57.050
If your query doesn't work, then you definitely

181
00:05:57.630 --> 00:05:59.970
have to ask why it isn't working.

182
00:06:00.250 --> 00:06:01.470
And you have to fix it instead of

183
00:06:01.470 --> 00:06:02.290
new query.

184
00:06:02.410 --> 00:06:04.670
I am saying find total sales per category.

185
00:06:05.410 --> 00:06:07.770
And this is a very simple group by

186
00:06:07.770 --> 00:06:08.270
question.

187
00:06:09.210 --> 00:06:10.610
We already did group by.

188
00:06:10.830 --> 00:06:11.490
And see here.

189
00:06:11.730 --> 00:06:12.430
It has done group by.

190
00:06:13.150 --> 00:06:13.630
Category.

191
00:06:14.370 --> 00:06:14.910
And see here.

192
00:06:15.010 --> 00:06:15.990
It has given us total sales.

193
00:06:16.330 --> 00:06:16.470
Okay.

194
00:06:16.830 --> 00:06:18.750
And we have used sum function.

195
00:06:19.510 --> 00:06:20.070
Okay.

196
00:06:21.030 --> 00:06:21.550
Alright.

197
00:06:21.950 --> 00:06:22.810
Now you can fix your queries.

198
00:06:24.050 --> 00:06:26.750
You can use AI to speed up writing.

199
00:06:26.750 --> 00:06:28.910
Always read it.

200
00:06:28.990 --> 00:06:30.150
Understand it.

201
00:06:30.370 --> 00:06:32.810
And how it generates your query.

202
00:06:33.290 --> 00:06:34.650
Focus on it.

203
00:06:34.790 --> 00:06:38.370
Not simply generate SQL from chatgbd.

204
00:06:39.070 --> 00:06:40.930
AI is a co-pilot.

205
00:06:41.170 --> 00:06:41.610
It is not a pilot.

206
00:06:42.050 --> 00:06:42.990
You are the pilot.

207
00:06:43.590 --> 00:06:43.810
Okay.

208
00:06:43.990 --> 00:06:45.130
This is not a shortcut.

209
00:06:45.630 --> 00:06:46.390
You don't have to learn SQL.

210
00:06:48.190 --> 00:06:50.750
The better you know the basics of SQL,

211
00:06:51.170 --> 00:06:52.490
the better AI will help you.

212
00:06:52.690 --> 00:06:53.990
I hope you got the point.

213
00:06:54.090 --> 00:06:55.370
I hope you are enjoying what I have

214
00:06:55.370 --> 00:06:55.890
said so far.

215
00:06:57.210 --> 00:06:58.510
See you in the next video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

WEBVTT

1
00:00:00.140 --> 00:00:02.640
(Transcribed by TurboScribe. Go Unlimited to remove this message.) Alright guys, now we are going to do

2
00:00:02.640 --> 00:00:04.220
a project in which we will design a

3
00:00:04.220 --> 00:00:07.200
database for an e-commerce store.

4
00:00:07.640 --> 00:00:09.880
So, let us say that Harry shop is

5
00:00:09.880 --> 00:00:12.740
a merchandise store where we sell hoodies, mugs,

6
00:00:12.900 --> 00:00:15.480
stickers, notebooks, maybe phone covers.

7
00:00:16.380 --> 00:00:17.720
What we have to do is design a

8
00:00:17.720 --> 00:00:21.860
database, set up correct table relationships, then we

9
00:00:21.860 --> 00:00:22.800
have to set up the right foreign keys

10
00:00:22.800 --> 00:00:26.040
and put realistic demo data and along with

11
00:00:26.040 --> 00:00:29.440
that we have to write some SQL queries

12
00:00:29.440 --> 00:00:30.780
which will analyse our business.

13
00:00:32.220 --> 00:00:33.380
So far we were in a database called

14
00:00:33.380 --> 00:00:35.160
e-com or maybe you are working on

15
00:00:35.160 --> 00:00:36.000
some other database.

16
00:00:36.900 --> 00:00:38.780
The first thing I will recommend to you

17
00:00:38.780 --> 00:00:40.660
is to make a new database for this

18
00:00:40.660 --> 00:00:41.120
work.

19
00:00:41.420 --> 00:00:41.520
It is highly recommended to make a new

20
00:00:41.520 --> 00:00:43.420
database for every particular project.

21
00:00:47.640 --> 00:00:50.380
So, what we will do for this particular

22
00:00:50.380 --> 00:00:55.860
use case, we will say create database and

23
00:00:55.860 --> 00:00:58.120
we will give the name as Harry shop

24
00:00:58.120 --> 00:01:01.040
and along with that we will say use

25
00:01:01.040 --> 00:01:06.860
Harry shop, use Harry shop.

26
00:01:07.680 --> 00:01:09.580
So, I have made a new database here

27
00:01:09.580 --> 00:01:10.940
with the name of Harry shop and I

28
00:01:10.940 --> 00:01:11.480
will use it.

29
00:01:12.180 --> 00:01:13.520
I run it and I got green ticks

30
00:01:13.520 --> 00:01:15.980
in both my queries which means that I

31
00:01:15.980 --> 00:01:17.320
have successfully made a database.

32
00:01:18.240 --> 00:01:20.300
Now, what I will do is, I will

33
00:01:20.300 --> 00:01:26.620
simply create a table, customers, so what we

34
00:01:26.620 --> 00:01:28.080
will do here is, we will add the

35
00:01:28.080 --> 00:01:31.240
primary key, I will call it customer ID,

36
00:01:32.160 --> 00:01:37.420
this will be an integer, int, this will

37
00:01:37.420 --> 00:01:40.500
be a primary key and along with that

38
00:01:40.500 --> 00:01:43.440
we will write primary key and along with

39
00:01:43.440 --> 00:01:46.800
that we will write auto increment.

40
00:01:47.220 --> 00:01:50.540
After this, I will have a name, then

41
00:01:50.540 --> 00:01:55.620
email, then city, then signup underscore date.

42
00:01:55.700 --> 00:01:56.460
Now, what will be the data types?

43
00:01:56.940 --> 00:01:57.840
Let's write the data types.

44
00:01:58.720 --> 00:02:01.720
Name will be my varchar 100, I think

45
00:02:01.720 --> 00:02:03.140
100 characters are more than enough.

46
00:02:03.900 --> 00:02:08.060
Email will be varchar 150, I think 150

47
00:02:08.060 --> 00:02:10.280
characters are more than enough for email.

48
00:02:10.280 --> 00:02:12.040
But what I will do here is, I

49
00:02:12.040 --> 00:02:15.700
will write unique and along with that I

50
00:02:15.700 --> 00:02:19.600
will write varchar 50 for my city which

51
00:02:19.600 --> 00:02:21.220
is more than enough I guess and I

52
00:02:21.220 --> 00:02:21.960
will date it here.

53
00:02:22.540 --> 00:02:23.540
So, now I want to tell you about

54
00:02:23.540 --> 00:02:25.680
this, the second button that you can see.

55
00:02:25.920 --> 00:02:29.340
Assume that you have placed your cursor somewhere

56
00:02:29.340 --> 00:02:29.440
in the middle of this query.

57
00:02:30.020 --> 00:02:33.280
After that, if you click here, then only

58
00:02:33.280 --> 00:02:34.440
this query will be executed.

59
00:02:34.440 --> 00:02:36.760
So, here I have already created my table.

60
00:02:37.460 --> 00:02:39.380
But again, what I did here is, if

61
00:02:39.380 --> 00:02:41.880
I want to run this query, then I

62
00:02:41.880 --> 00:02:42.780
will place the cursor anywhere in the middle

63
00:02:42.780 --> 00:02:43.900
and I will use this button.

64
00:02:44.740 --> 00:02:46.400
Clicking this button means that you run only

65
00:02:46.400 --> 00:02:48.580
the same query where the cursor is.

66
00:02:48.740 --> 00:02:50.340
Like in this case, only use Harry shop

67
00:02:50.340 --> 00:02:50.580
will work.

68
00:02:51.320 --> 00:02:52.820
You see, here only use Harry shop worked.

69
00:02:53.240 --> 00:02:54.060
If I want to run only create database

70
00:02:54.060 --> 00:02:56.040
Harry shop, then I will click here.

71
00:02:56.420 --> 00:02:58.220
And you see, this query failed, but again

72
00:02:58.220 --> 00:02:59.260
only this query will work.

73
00:02:59.260 --> 00:03:01.980
So, wherever you press the cursor and click

74
00:03:01.980 --> 00:03:05.100
here, then only the same line will run

75
00:03:05.100 --> 00:03:05.880
where the cursor is.

76
00:03:06.020 --> 00:03:07.320
So, this is a handy way to execute

77
00:03:07.320 --> 00:03:08.300
a particular line.

78
00:03:09.220 --> 00:03:10.860
So, what we did that time, we made

79
00:03:10.860 --> 00:03:11.540
a customer table.

80
00:03:12.240 --> 00:03:13.380
First, we made a database in the name

81
00:03:13.380 --> 00:03:13.780
of Harry shop.

82
00:03:14.720 --> 00:03:15.380
Then we made a table.

83
00:03:15.660 --> 00:03:17.400
We said that we will have to save

84
00:03:17.400 --> 00:03:17.500
all our customers.

85
00:03:17.900 --> 00:03:20.240
We have the customer ID of the customer.

86
00:03:20.280 --> 00:03:23.020
Along with that, we have name, email, city

87
00:03:23.020 --> 00:03:23.840
and signup date.

88
00:03:23.960 --> 00:03:24.520
Very good.

89
00:03:25.380 --> 00:03:26.080
Now, what we will do is, we will

90
00:03:26.080 --> 00:03:26.700
make a product table.

91
00:03:26.700 --> 00:03:28.780
And what I will do for this?

92
00:03:28.920 --> 00:03:32.020
For that, I will write create table products.

93
00:03:33.800 --> 00:03:35.660
And what we are going to do here?

94
00:03:36.900 --> 00:03:38.400
First of all, product ID.

95
00:03:39.920 --> 00:03:41.120
Now, I will write its types later.

96
00:03:42.380 --> 00:03:43.520
First of all, I will see what will

97
00:03:43.520 --> 00:03:43.720
happen.

98
00:03:45.280 --> 00:03:46.240
Then category.

99
00:03:46.420 --> 00:03:47.740
What is the category of our product?

100
00:03:48.180 --> 00:03:50.220
Product ID will be of auto increment primary

101
00:03:50.220 --> 00:03:50.620
key.

102
00:03:51.140 --> 00:03:51.580
Integer.

103
00:03:52.160 --> 00:03:52.960
Our product name.

104
00:03:53.340 --> 00:03:54.040
What is the name of our product?

105
00:03:54.420 --> 00:03:55.320
Is it a laptop or a desktop?

106
00:03:55.580 --> 00:03:56.120
What is it?

107
00:03:56.120 --> 00:03:56.620
Is it a mouse?

108
00:03:57.000 --> 00:03:57.440
Is it an SSD?

109
00:03:58.520 --> 00:03:58.660
Okay.

110
00:03:59.060 --> 00:03:59.820
After this, category.

111
00:03:59.940 --> 00:04:00.440
Is it electronics?

112
00:04:00.960 --> 00:04:01.480
Is it furniture?

113
00:04:02.080 --> 00:04:02.760
What is it?

114
00:04:02.760 --> 00:04:03.440
Is it a kitchen appliance?

115
00:04:03.600 --> 00:04:04.140
What is it?

116
00:04:04.380 --> 00:04:05.720
So, this will be our category.

117
00:04:06.740 --> 00:04:08.380
Then after this, price and stock.

118
00:04:08.540 --> 00:04:09.240
Price means how much?

119
00:04:09.380 --> 00:04:11.040
Stock means how much quantity is available.

120
00:04:12.300 --> 00:04:14.240
So, I will write integer here.

121
00:04:14.960 --> 00:04:16.880
And after this, we will make it decimal.

122
00:04:17.700 --> 00:04:18.260
10, 2.

123
00:04:18.680 --> 00:04:20.480
I think 10, 2 decimal is good.

124
00:04:21.220 --> 00:04:22.740
Then after this, I will make it 50.

125
00:04:23.860 --> 00:04:26.100
And product name, I think 100.

126
00:04:26.100 --> 00:04:26.540
100.

127
00:04:27.900 --> 00:04:29.740
Yes, 100 should be good.

128
00:04:30.660 --> 00:04:31.960
And let's write this quickly.

129
00:04:32.480 --> 00:04:36.140
Int primary key auto underscore increment.

130
00:04:36.980 --> 00:04:38.240
Okay, many people make a mistake.

131
00:04:38.480 --> 00:04:39.400
They write auto space increment.

132
00:04:39.760 --> 00:04:40.540
Because of which there is a problem.

133
00:04:40.900 --> 00:04:42.680
See, primary key has primary space key.

134
00:04:42.960 --> 00:04:44.720
And auto increment has auto underscore increment.

135
00:04:45.200 --> 00:04:46.300
Now, I want only this query of create

136
00:04:46.300 --> 00:04:47.440
table products to run.

137
00:04:47.520 --> 00:04:48.420
So, I will bring the cursor here.

138
00:04:48.500 --> 00:04:48.820
I will press this one.

139
00:04:49.860 --> 00:04:52.040
And now see, my create table products query

140
00:04:52.040 --> 00:04:52.360
has run.

141
00:04:53.300 --> 00:04:53.480
Okay.

142
00:04:54.040 --> 00:04:54.480
Very good.

143
00:04:54.780 --> 00:04:55.960
So, we have made a product stable.

144
00:04:56.080 --> 00:04:58.360
So far, we have saved customers.

145
00:04:59.260 --> 00:05:00.000
We have saved products.

146
00:05:01.180 --> 00:05:04.900
And along with that, we will make a

147
00:05:04.900 --> 00:05:05.200
table for orders.

148
00:05:05.920 --> 00:05:09.700
So, we will say create table orders.

149
00:05:10.360 --> 00:05:12.340
And after this, we will take the first

150
00:05:12.340 --> 00:05:13.200
thing here.

151
00:05:13.300 --> 00:05:13.920
Order id.

152
00:05:14.600 --> 00:05:16.800
Then we will take customer id.

153
00:05:17.160 --> 00:05:19.120
Then we will take order date.

154
00:05:19.740 --> 00:05:21.880
Then we will take order status.

155
00:05:22.500 --> 00:05:25.340
Then after that, that's it.

156
00:05:25.940 --> 00:05:26.060
So, we have made a table for orders.

157
00:05:31.900 --> 00:05:36.020
And after that, we will

158
00:05:36.020 --> 00:05:44.960
take order date.

159
00:05:48.600 --> 00:05:49.780
And after that, we will take order status.

160
00:05:51.040 --> 00:05:51.620
And after that, we will take order date.

161
00:05:51.620 --> 00:05:52.020
And after that, we will take order status.

162
00:06:58.860 --> 00:07:02.240
So, what I will do is, I will

163
00:07:02.240 --> 00:07:05.140
make an order item table, in which the

164
00:07:05.140 --> 00:07:08.200
details of my order items will be there,

165
00:07:08.540 --> 00:07:14.860
like which product is there, how much quantity

166
00:07:14.860 --> 00:07:18.420
is there, and in which order ID it

167
00:07:18.420 --> 00:07:21.200
is, so what I will do is, I

168
00:07:21.200 --> 00:07:22.780
will make a new table, and you keep

169
00:07:22.780 --> 00:07:23.740
watching how I will do it.

170
00:07:23.740 --> 00:07:25.640
I will say one more thing before moving

171
00:07:25.640 --> 00:07:27.540
ahead, that a particular database can be designed

172
00:07:27.540 --> 00:07:30.100
in different ways, I am taking one approach,

173
00:07:30.660 --> 00:07:33.140
you can take another approach, but the approach

174
00:07:33.140 --> 00:07:34.880
I am taking is going to be scalable.

175
00:07:34.880 --> 00:07:38.460
So, I will write here, create table order

176
00:07:38.460 --> 00:07:42.240
items, what it will do is, it will

177
00:07:42.240 --> 00:07:45.820
store my order items, so here first of

178
00:07:45.820 --> 00:07:50.840
all, order item ID, order item ID, second

179
00:07:50.840 --> 00:07:53.260
will be order ID, which will come from

180
00:07:53.260 --> 00:07:55.760
here, we will link in this, it will

181
00:07:55.760 --> 00:07:58.560
have an ID, whose details will be here

182
00:07:58.560 --> 00:08:00.800
in order table, definitely I will make foreign

183
00:08:00.800 --> 00:08:04.580
one, then product ID, which product is there,

184
00:08:04.760 --> 00:08:06.660
so it is telling which order is there,

185
00:08:06.740 --> 00:08:10.580
which product is there, and then this quantity,

186
00:08:10.580 --> 00:08:14.020
for example, you have ordered on Amazon, you

187
00:08:14.020 --> 00:08:15.560
have ordered an item, your item no.1

188
00:08:15.560 --> 00:08:16.700
is laptop, so it will go to your

189
00:08:16.700 --> 00:08:19.840
order item table, the order you have placed

190
00:08:19.840 --> 00:08:21.560
will have an ID, which will link to

191
00:08:21.560 --> 00:08:25.420
it, and the product you have purchased will

192
00:08:25.420 --> 00:08:26.380
have an ID, which will come from this

193
00:08:26.380 --> 00:08:30.680
table, and here order item ID is of

194
00:08:30.680 --> 00:08:33.380
this table's primary key, which will be auto

195
00:08:33.380 --> 00:08:36.400
-increment, and I will also copy it, because

196
00:08:36.400 --> 00:08:38.179
I am feeling lazy, how much should I

197
00:08:38.179 --> 00:08:41.080
type, why should I copy and paste it,

198
00:08:42.179 --> 00:08:44.280
then after this, order ID is going to

199
00:08:44.280 --> 00:08:47.500
be an integer, or product ID is also

200
00:08:47.500 --> 00:08:50.360
going to be an integer, or quantity is

201
00:08:50.360 --> 00:08:53.760
going to be an integer, and here foreign

202
00:08:53.760 --> 00:09:05.450
key, order ID, references, orders, order

203
00:09:05.450 --> 00:09:10.490
underscore ID, and foreign key, product ID, product

204
00:09:10.490 --> 00:09:13.270
ID is basically in product table, product underscore

205
00:09:13.270 --> 00:09:22.250
ID, references, products, and

206
00:09:22.250 --> 00:09:26.250
product ID, I hope I have done everything

207
00:09:26.250 --> 00:09:29.090
correctly, we have made so many tables, what

208
00:09:29.090 --> 00:09:31.110
is comma doing here, there will be space

209
00:09:31.110 --> 00:09:35.010
here, there is no error in our statement,

210
00:09:35.010 --> 00:09:38.170
so we will make all these tables one

211
00:09:38.170 --> 00:09:40.930
by one, we have made customer's table and

212
00:09:40.930 --> 00:09:46.890
product's table, now we have to make order's

213
00:09:46.890 --> 00:09:49.170
table, let's run the SQL, order's table is

214
00:09:49.170 --> 00:09:52.890
also made, order's table is made or not,

215
00:09:53.150 --> 00:09:55.890
I have taken my arrow here, I have

216
00:09:55.890 --> 00:09:57.990
run it, so I have to press this,

217
00:09:58.250 --> 00:09:59.910
what am I pressing, I will press this,

218
00:09:59.990 --> 00:10:03.150
it is saying fail to open the reference

219
00:10:03.150 --> 00:10:09.470
table customer, our customer's table is not made,

220
00:10:09.470 --> 00:10:16.010
I have written customer, now this table is

221
00:10:16.010 --> 00:10:19.770
made, now I have to make order items

222
00:10:19.770 --> 00:10:22.730
table, this is also made, I hope I

223
00:10:22.730 --> 00:10:52.370
have done everything correctly, I

224
00:10:52.370 --> 00:10:52.470
hope I have done everything correctly, I hope

225
00:10:52.470 --> 00:10:52.570
I have done everything correctly, I hope I

226
00:10:52.570 --> 00:10:52.670
have done everything correctly, I hope I have

227
00:10:52.670 --> 00:10:52.770
done everything correctly, I hope I have done

228
00:10:52.770 --> 00:10:52.870
everything correctly, I hope I have done everything

229
00:10:52.870 --> 00:10:52.970
correctly, I hope I have done everything correctly,

230
00:10:52.970 --> 00:10:53.070
I hope I have done everything correctly, I

231
00:10:53.070 --> 00:10:53.170
hope I have done everything correctly, I hope

232
00:10:53.170 --> 00:10:53.270
I have done everything correctly, I hope I

233
00:10:53.270 --> 00:10:53.370
have done everything correctly, I hope I have

234
00:10:53.370 --> 00:10:53.470
done everything correctly, I hope I have done

235
00:10:53.470 --> 00:10:53.570
everything correctly, I hope I have done everything

236
00:10:53.570 --> 00:10:53.670
correctly, I hope I have done everything correctly,

237
00:10:53.670 --> 00:10:53.770
I hope I have done everything correctly, I

238
00:10:53.770 --> 00:10:53.870
hope I have done everything correctly, I hope

239
00:10:53.870 --> 00:10:53.970
I have done everything correctly, I hope I

240
00:10:53.970 --> 00:10:54.070
have done everything correctly, I hope I have

241
00:10:54.070 --> 00:10:54.170
done everything correctly, I hope I have done

242
00:10:54.170 --> 00:10:54.270
everything correctly, I hope I have done everything

243
00:10:54.270 --> 00:10:54.370
correctly, I hope I have done everything correctly,

244
00:10:54.370 --> 00:10:54.470
I hope I have done everything correctly, I

245
00:10:54.470 --> 00:10:54.570
hope I have done everything correctly, I hope

246
00:10:54.570 --> 00:10:54.670
I have done everything correctly, I hope I

247
00:10:54.670 --> 00:10:54.770
have done everything correctly, I hope I have

248
00:10:54.770 --> 00:11:01.990
done everything correctly, I

249
00:11:01.990 --> 00:11:18.690
hope

250
00:11:18.690 --> 00:11:20.710
I have done everything correctly, I hope I

251
00:11:20.710 --> 00:11:21.830
have done everything correctly, I hope I have

252
00:11:21.830 --> 00:11:21.930
done everything correctly, I hope I have done

253
00:11:21.930 --> 00:11:22.030
everything correctly, I hope I have done everything

254
00:11:22.030 --> 00:11:22.130
correctly, I hope I have done everything correctly,

255
00:11:22.130 --> 00:11:22.230
I hope I have done everything correctly, I

256
00:11:22.230 --> 00:11:22.330
hope I have done everything correctly, I hope

257
00:11:22.330 --> 00:11:22.430
I have done everything correctly, I hope I

258
00:11:22.430 --> 00:11:22.530
have done everything correctly, I hope I have

259
00:11:22.530 --> 00:11:22.630
done everything correctly, I hope I have done

260
00:11:22.630 --> 00:11:22.730
everything correctly, I hope I have done everything

261
00:11:22.730 --> 00:11:22.830
correctly, I hope I have done everything correctly,

262
00:11:22.830 --> 00:11:22.930
I hope I have done everything correctly, I

263
00:11:22.930 --> 00:11:23.030
hope I have done everything correctly, I hope

264
00:11:23.030 --> 00:11:23.130
I have done everything correctly, I hope I

265
00:11:23.130 --> 00:11:23.230
have done everything correctly, I hope I have

266
00:11:23.230 --> 00:11:23.330
done everything correctly, I hope I have done

267
00:11:23.330 --> 00:11:23.430
everything correctly, I hope I have done everything

268
00:11:23.430 --> 00:11:23.530
correctly, I hope I have done everything correctly,

269
00:11:23.530 --> 00:11:23.630
I hope I have done everything correctly, I

270
00:11:23.630 --> 00:11:23.730
hope I have done everything correctly, I hope

271
00:11:23.730 --> 00:11:23.830
I have done everything correctly, I hope I

272
00:11:23.830 --> 00:11:23.930
have done everything correctly, I hope I have

273
00:11:23.930 --> 00:11:42.250
done everything correctly, I hope I

274
00:11:42.250 --> 00:11:47.230
have done everything correctly, I hope I have

275
00:11:47.230 --> 00:11:50.250
done everything correctly, I hope I have done

276
00:11:50.250 --> 00:11:55.010
everything correctly, I hope I have done everything

277
00:11:55.010 --> 00:11:55.110
correctly, I hope I have done everything correctly,

278
00:11:55.110 --> 00:11:55.210
I hope I have done everything correctly, I

279
00:11:55.210 --> 00:11:55.310
hope I have done everything correctly, I hope

280
00:11:55.310 --> 00:11:55.410
I have done everything correctly, I hope I

281
00:11:55.410 --> 00:11:55.510
have done everything correctly, I hope I have

282
00:11:55.510 --> 00:11:55.610
done everything correctly, I hope I have done

283
00:11:55.610 --> 00:11:55.710
everything correctly, I hope I have done everything

284
00:11:55.710 --> 00:11:55.810
correctly, I hope I have done everything correctly,

285
00:11:55.810 --> 00:11:55.910
I hope I have done everything correctly, I

286
00:11:55.910 --> 00:11:56.010
hope I have done everything correctly, I hope

287
00:11:56.010 --> 00:11:56.110
I have done everything correctly, I hope I

288
00:11:56.110 --> 00:11:56.210
have done everything correctly, I hope I have

289
00:11:56.210 --> 00:11:56.310
done everything correctly, I hope I have done

290
00:11:56.310 --> 00:11:56.410
everything correctly, I hope I have done everything

291
00:11:56.410 --> 00:11:56.510
correctly, I hope I have done everything correctly,

292
00:11:56.510 --> 00:11:56.610
I hope I have done everything correctly, I

293
00:11:56.610 --> 00:11:56.710
hope I have done everything correctly, I hope

294
00:11:56.710 --> 00:11:56.810
I have done everything correctly, I hope I

295
00:11:56.810 --> 00:11:56.910
have done everything correctly, I hope I have

296
00:11:56.910 --> 00:11:57.010
done everything correctly, I hope I have done

297
00:11:57.010 --> 00:11:57.110
everything correctly, I hope I have done everything

298
00:11:57.110 --> 00:12:09.770
correctly I

299
00:12:09.770 --> 00:12:16.910
hope I have done

300
00:12:16.910 --> 00:12:22.650
everything correctly, I hope I have done everything

301
00:12:22.650 --> 00:12:24.430
correctly, I hope I have done everything correctly,

302
00:12:24.430 --> 00:12:24.530
I hope I have done everything correctly, I

303
00:12:24.530 --> 00:12:24.630
hope I have done everything correctly, I hope

304
00:12:24.630 --> 00:12:24.730
I have done everything correctly, I hope I

305
00:12:24.730 --> 00:12:24.830
have done everything correctly, I hope I have

306
00:12:24.830 --> 00:12:24.930
done everything correctly, I hope I have done

307
00:12:24.930 --> 00:12:25.030
everything correctly, I hope I have done everything

308
00:12:25.030 --> 00:12:25.130
correctly, I hope I have done everything correctly,

309
00:12:25.130 --> 00:12:25.230
I hope I have done everything correctly, I

310
00:12:25.230 --> 00:12:25.330
hope I have done everything correctly, I hope

311
00:12:25.330 --> 00:12:25.430
I have done everything correctly, I hope I

312
00:12:25.430 --> 00:12:25.530
have done everything correctly, I hope I have

313
00:12:25.530 --> 00:12:25.630
done everything correctly, I hope I have done

314
00:12:25.630 --> 00:12:25.730
everything correctly, I hope I have done everything

315
00:12:25.730 --> 00:12:25.830
correctly, I hope I have done everything correctly,

316
00:12:25.830 --> 00:12:25.930
I hope I have done everything correctly, I

317
00:12:25.930 --> 00:12:26.030
hope I have done everything correctly, I hope

318
00:12:26.030 --> 00:12:26.130
I have done everything correctly, I hope I

319
00:12:26.130 --> 00:12:26.230
have done everything correctly, I hope I have

320
00:12:26.230 --> 00:12:26.330
done everything correctly, I hope I have done

321
00:12:26.330 --> 00:12:26.430
everything correctly, I hope I have done everything

322
00:12:26.430 --> 00:12:26.530
correctly, I hope I have done everything correctly,

323
00:12:26.530 --> 00:12:45.450
I hope I have done everything

324
00:12:45.450 --> 00:12:53.150
correctly, I hope I have done everything correctly,

325
00:12:53.150 --> 00:12:53.430
I hope I have done everything correctly, I

326
00:12:53.430 --> 00:12:54.290
hope I have done everything correctly, I hope

327
00:12:54.290 --> 00:12:54.390
I have done everything correctly, I hope I

328
00:12:54.390 --> 00:12:54.490
have done everything correctly, I hope I have

329
00:12:54.490 --> 00:12:54.590
done everything correctly, I hope I have done

330
00:12:54.590 --> 00:12:54.690
everything correctly, I hope I have done everything

331
00:12:54.690 --> 00:12:54.790
correctly, I hope I have done everything correctly,

332
00:12:54.790 --> 00:12:54.890
I hope I have done everything correctly, I

333
00:12:54.890 --> 00:12:54.990
hope I have done everything correctly, I hope

334
00:12:54.990 --> 00:12:55.090
I have done everything correctly, I hope I

335
00:12:55.090 --> 00:12:55.190
have done everything correctly, I hope I have

336
00:12:55.190 --> 00:12:55.290
done everything correctly, I hope I have done

337
00:12:55.290 --> 00:12:55.390
everything correctly, I hope I have done everything

338
00:12:55.390 --> 00:12:55.490
correctly, I hope I have done everything correctly,

339
00:12:55.490 --> 00:12:55.590
I hope I have done everything correctly, I

340
00:12:55.590 --> 00:12:55.690
hope I have done everything correctly, I hope

341
00:12:55.690 --> 00:12:55.790
I have done everything correctly, I hope I

342
00:12:55.790 --> 00:12:55.890
have done everything correctly, I hope I have

343
00:12:55.890 --> 00:12:55.990
done everything correctly, I hope I have done

344
00:12:55.990 --> 00:12:56.090
everything correctly, I hope I have done everything

345
00:12:56.090 --> 00:12:56.190
correctly, I hope I have done everything correctly,

346
00:12:56.190 --> 00:12:56.290
I hope I have done everything correctly, I

347
00:12:56.290 --> 00:12:56.390
hope I have done everything correctly, I hope

348
00:13:00.530 --> 00:13:01.010
I have

349
00:13:01.010 --> 00:13:11.570
done

350
00:13:11.570 --> 00:13:21.250
everything correctly, I hope I have done everything

351
00:13:21.250 --> 00:13:22.650
correctly, I hope I have done everything correctly,

352
00:13:23.070 --> 00:13:24.310
I hope I have done everything correctly, I

353
00:13:24.310 --> 00:13:24.510
hope I have done everything correctly, I hope

354
00:13:24.510 --> 00:13:24.610
I have done everything correctly, I hope I

355
00:13:24.610 --> 00:13:24.710
have done everything correctly, I hope I have

356
00:13:24.710 --> 00:13:24.810
done everything correctly, I hope I have done

357
00:13:24.810 --> 00:13:24.910
everything correctly, I hope I have done everything

358
00:13:24.910 --> 00:13:25.010
correctly, I hope I have done everything correctly,

359
00:13:25.010 --> 00:13:25.110
I hope I have done everything correctly, I

360
00:13:25.110 --> 00:13:25.210
hope I have done everything correctly, I hope

361
00:13:25.210 --> 00:13:25.310
I have done everything correctly, I hope I

362
00:13:25.310 --> 00:13:25.410
have done everything correctly, I hope I have

363
00:13:25.410 --> 00:13:25.510
done everything correctly, I hope I have done

364
00:13:25.510 --> 00:13:25.610
everything correctly, I hope I have done everything

365
00:13:25.610 --> 00:13:25.710
correctly, I hope I have done everything correctly,

366
00:13:25.710 --> 00:13:25.810
I hope I have done everything correctly, I

367
00:13:25.810 --> 00:13:25.910
hope I have done everything correctly, I hope

368
00:13:25.910 --> 00:13:26.010
I have done everything correctly, I hope I

369
00:13:26.010 --> 00:13:26.110
have done everything correctly, I hope I have

370
00:13:26.110 --> 00:13:26.210
done everything correctly, I hope I have done

371
00:13:26.210 --> 00:13:26.310
everything correctly, I hope I have done everything

372
00:13:26.310 --> 00:13:26.410
correctly, I hope I have done everything correctly,

373
00:13:26.410 --> 00:13:31.150
I hope I have done everything correctly I

374
00:13:31.150 --> 00:13:31.270
hope

375
00:13:31.270 --> 00:13:44.130
I

376
00:13:44.130 --> 00:13:44.590
have done everything correctly, I hope I have

377
00:13:44.590 --> 00:13:48.810
done everything correctly, I hope I have done

378
00:13:48.810 --> 00:13:52.110
everything correctly, I hope I have done everything

379
00:13:52.110 --> 00:13:52.250
correctly, I hope I have done everything correctly,

380
00:13:52.250 --> 00:13:52.510
I hope I have done everything correctly, I

381
00:13:52.510 --> 00:13:52.950
hope I have done everything correctly, I hope

382
00:13:52.950 --> 00:13:53.050
I have done everything correctly, I hope I

383
00:13:53.050 --> 00:13:53.150
have done everything correctly, I hope I have

384
00:13:53.150 --> 00:13:53.250
done everything correctly, I hope I have done

385
00:13:53.250 --> 00:13:53.350
everything correctly, I hope I have done everything

386
00:13:53.350 --> 00:13:53.450
correctly, I hope I have done everything correctly,

387
00:13:53.450 --> 00:13:53.550
I hope I have done everything correctly, I

388
00:13:53.550 --> 00:13:53.650
hope I have done everything correctly, I hope

389
00:13:53.650 --> 00:13:53.750
I have done everything correctly, I hope I

390
00:13:53.750 --> 00:13:53.850
have done everything correctly, I hope I have

391
00:13:53.850 --> 00:13:53.950
done everything correctly, I hope I have done

392
00:13:53.950 --> 00:13:54.050
everything correctly, I hope I have done everything

393
00:13:54.050 --> 00:13:54.150
correctly, I hope I have done everything correctly,

394
00:13:54.150 --> 00:13:54.250
I hope I have done everything correctly, I

395
00:13:54.250 --> 00:13:54.350
hope I have done everything correctly, I hope

396
00:13:54.350 --> 00:13:54.450
I have done everything correctly, I hope I

397
00:13:54.450 --> 00:13:54.550
have done everything correctly, I hope I have

398
00:13:54.550 --> 00:13:54.650
done everything correctly, I hope I have done

399
00:13:54.650 --> 00:14:10.710
everything correctly, I hope I have done everything

400
00:14:10.710 --> 00:14:13.750
correctly, I hope I have done everything correctly,

401
00:14:13.750 --> 00:14:15.390
I hope I have done everything correctly, I

402
00:14:15.390 --> 00:14:18.110
hope I have done everything correctly, I hope

403
00:14:18.110 --> 00:14:19.970
I have done everything correctly, I hope I

404
00:14:19.970 --> 00:14:20.070
have done everything correctly, I hope I have

405
00:14:20.070 --> 00:14:20.170
done everything correctly, I hope I have done

406
00:14:20.170 --> 00:14:20.270
everything correctly, I hope I have done everything

407
00:14:20.270 --> 00:14:20.370
correctly, I hope I have done everything correctly,

408
00:14:20.370 --> 00:14:20.470
I hope I have done everything correctly, I

409
00:14:20.470 --> 00:14:20.570
hope I have done everything correctly, I hope

410
00:14:20.570 --> 00:14:20.670
I have done everything correctly, I hope I

411
00:14:20.670 --> 00:14:20.770
have done everything correctly, I hope I have

412
00:14:20.770 --> 00:14:21.510
done everything correctly, I hope I have done

413
00:14:21.510 --> 00:14:22.530
everything correctly, I hope I have done everything

414
00:14:22.530 --> 00:14:22.630
correctly, I hope I have done everything correctly,

415
00:14:22.630 --> 00:14:22.730
I hope I have done everything correctly, I

416
00:14:22.730 --> 00:14:22.830
hope I have done everything correctly, I hope

417
00:14:22.830 --> 00:14:22.930
I have done everything correctly, I hope I

418
00:14:22.930 --> 00:14:23.030
have done everything correctly, I hope I have

419
00:14:23.030 --> 00:14:23.130
done everything correctly, I hope I have done

420
00:14:23.130 --> 00:14:23.230
everything correctly, I hope I have done everything

421
00:14:23.230 --> 00:14:23.330
correctly, I hope I have done everything correctly,

422
00:14:23.330 --> 00:14:23.430
I hope I have done everything correctly, I

423
00:14:23.430 --> 00:14:24.170
hope I have done everything correctly, I hope

424
00:14:38.190 --> 00:14:43.370
I have done

425
00:14:43.370 --> 00:14:51.050
everything correctly, I hope I have done everything

426
00:14:51.050 --> 00:14:52.110
correctly, I hope I have done everything correctly,

427
00:14:52.110 --> 00:14:52.530
I hope I have done everything correctly, I

428
00:14:52.530 --> 00:14:52.730
hope I have done everything correctly, I hope

429
00:14:52.730 --> 00:14:52.830
I have done everything correctly, I hope I

430
00:14:52.830 --> 00:14:53.010
have done everything correctly, I hope I have

431
00:14:53.010 --> 00:14:53.110
done everything correctly, I hope I have done

432
00:14:53.110 --> 00:14:53.210
everything correctly, I hope I have done everything

433
00:14:53.210 --> 00:14:53.310
correctly, I hope I have done everything correctly,

434
00:14:53.310 --> 00:14:53.410
I hope I have done everything correctly, I

435
00:14:53.410 --> 00:14:53.510
hope I have done everything correctly, I hope

436
00:14:53.510 --> 00:14:53.610
I have done everything correctly, I hope I

437
00:14:53.610 --> 00:14:53.710
have done everything correctly, I hope I have

438
00:14:53.710 --> 00:14:53.810
done everything correctly, I hope I have done

439
00:14:53.810 --> 00:14:53.910
everything correctly, I hope I have done everything

440
00:14:53.910 --> 00:14:54.010
correctly, I hope I have done everything correctly,

441
00:14:54.010 --> 00:14:54.110
I hope I have done everything correctly, I

442
00:14:54.110 --> 00:14:54.210
hope I have done everything correctly, I hope

443
00:14:54.210 --> 00:14:54.310
I have done everything correctly, I hope I

444
00:14:54.310 --> 00:14:54.410
have done everything correctly, I hope I have

445
00:14:54.410 --> 00:14:54.510
done everything correctly, I hope I have done

446
00:14:54.510 --> 00:14:54.610
everything correctly, I hope I have done everything

447
00:14:54.610 --> 00:14:54.710
correctly, I hope I have done everything correctly,

448
00:14:54.710 --> 00:15:05.590
I hope I have done everything correctly I

449
00:15:05.590 --> 00:15:06.350
hope

450
00:15:06.350 --> 00:15:19.490
I

451
00:15:19.490 --> 00:15:22.750
have done everything correctly, I hope I have

452
00:15:22.750 --> 00:15:24.030
done everything correctly, I hope I have done

453
00:15:24.030 --> 00:15:24.130
everything correctly, I hope I have done everything

454
00:15:24.130 --> 00:15:24.230
correctly, I hope I have done everything correctly,

455
00:15:24.230 --> 00:15:24.330
I hope I have done everything correctly, I

456
00:15:24.330 --> 00:15:24.430
hope I have done everything correctly, I hope

457
00:15:24.430 --> 00:15:24.530
I have done everything correctly, I hope I

458
00:15:24.530 --> 00:15:24.630
have done everything correctly, I hope I have

459
00:15:24.630 --> 00:15:24.730
done everything correctly, I hope I have done

460
00:15:24.730 --> 00:15:24.830
everything correctly, I hope I have done everything

461
00:15:24.830 --> 00:15:24.930
correctly, I hope I have done everything correctly,

462
00:15:24.930 --> 00:15:25.030
I hope I have done everything correctly, I

463
00:15:25.030 --> 00:15:25.130
hope I have done everything correctly, I hope

464
00:15:25.130 --> 00:15:25.230
I have done everything correctly, I hope I

465
00:15:25.230 --> 00:15:25.330
have done everything correctly, I hope I have

466
00:15:25.330 --> 00:15:25.430
done everything correctly, I hope I have done

467
00:15:25.430 --> 00:15:25.530
everything correctly, I hope I have done everything

468
00:15:25.530 --> 00:15:25.630
correctly, I hope I have done everything correctly,

469
00:15:25.630 --> 00:15:25.730
I hope I have done everything correctly, I

470
00:15:25.730 --> 00:15:25.830
hope I have done everything correctly, I hope

471
00:15:25.830 --> 00:15:25.930
I have done everything correctly, I hope I

472
00:15:25.930 --> 00:15:26.030
have done everything correctly, I hope I have

473
00:15:26.030 --> 00:15:26.130
done everything correctly, I hope I have done

474
00:15:26.130 --> 00:15:26.230
everything correctly, I hope I have done

475
00:15:26.230 --> 00:15:53.390
everything

476
00:15:53.390 --> 00:15:54.110
correctly, I hope I have done everything correctly,

477
00:15:54.110 --> 00:15:54.210
I hope I have done everything correctly, I

478
00:15:54.210 --> 00:15:54.310
hope I have done everything correctly, I hope

479
00:15:54.310 --> 00:15:54.410
I have done everything correctly, I hope I

480
00:15:54.410 --> 00:15:54.510
have done everything correctly, I hope I have

481
00:15:54.510 --> 00:15:54.610
done everything correctly, I hope I have done

482
00:15:54.610 --> 00:15:54.710
everything correctly, I hope I have done everything

483
00:15:54.710 --> 00:15:54.810
correctly, I hope I have done everything correctly,

484
00:15:54.810 --> 00:15:54.910
I hope I have done everything correctly, I

485
00:15:54.910 --> 00:15:55.010
hope I have done everything correctly, I hope

486
00:15:55.010 --> 00:15:55.110
I have done everything correctly, I hope I

487
00:15:55.110 --> 00:15:55.210
have done everything correctly, I hope I have

488
00:15:55.210 --> 00:15:55.310
done everything correctly, I hope I have done

489
00:15:55.310 --> 00:15:55.410
everything correctly, I hope I have done everything

490
00:15:55.410 --> 00:15:55.510
correctly, I hope I have done everything correctly,

491
00:15:55.510 --> 00:15:55.610
I hope I have done everything correctly, I

492
00:15:55.610 --> 00:15:55.710
hope I have done everything correctly, I hope

493
00:15:55.710 --> 00:15:55.810
I have done everything correctly, I hope I

494
00:15:55.810 --> 00:15:55.910
have done everything correctly, I hope I have

495
00:15:55.910 --> 00:15:56.010
done everything correctly, I hope I have done

496
00:15:56.010 --> 00:15:56.110
everything correctly, I hope I have done everything

497
00:15:56.110 --> 00:15:56.210
correctly, I hope I have done everything correctly,

498
00:15:56.210 --> 00:15:56.310
I hope I have done everything correctly, I

499
00:15:56.310 --> 00:15:56.410
hope I have done everything correctly, I hope

500
00:16:05.170 --> 00:16:12.370
I have done

501
00:16:12.370 --> 00:16:19.970
everything correctly, I hope I have done everything

502
00:16:19.970 --> 00:16:22.490
correctly, I hope I have done everything correctly,

503
00:16:22.490 --> 00:16:23.750
I hope I have done everything correctly, I

504
00:16:23.750 --> 00:16:23.850
hope I have done everything correctly, I hope

505
00:16:23.850 --> 00:16:23.950
I have done everything correctly, I hope I

506
00:16:23.950 --> 00:16:24.050
have done everything correctly, I hope I have

507
00:16:24.050 --> 00:16:24.150
done everything correctly, I hope I have done

508
00:16:24.150 --> 00:16:24.250
everything correctly, I hope I have done everything

509
00:16:24.250 --> 00:16:24.350
correctly, I hope I have done everything correctly,

510
00:16:24.350 --> 00:16:24.450
I hope I have done everything correctly, I

511
00:16:24.450 --> 00:16:24.550
hope I have done everything correctly, I hope

512
00:16:24.550 --> 00:16:24.650
I have done everything correctly, I hope I

513
00:16:24.650 --> 00:16:24.750
have done everything correctly, I hope I have

514
00:16:24.750 --> 00:16:24.850
done everything correctly, I hope I have done

515
00:16:24.850 --> 00:16:24.950
everything correctly, I hope I have done everything

516
00:16:24.950 --> 00:16:25.050
correctly, I hope I have done everything correctly,

517
00:16:25.050 --> 00:16:25.150
I hope I have done everything correctly, I

518
00:16:25.150 --> 00:16:25.250
hope I have done everything correctly, I hope

519
00:16:25.250 --> 00:16:25.350
I have done everything correctly, I hope I

520
00:16:25.350 --> 00:16:25.450
have done everything correctly, I hope I have

521
00:16:25.450 --> 00:16:25.550
done everything correctly, I hope I have done

522
00:16:25.550 --> 00:16:25.650
everything correctly, I hope I have done everything

523
00:16:25.650 --> 00:16:25.750
correctly, I hope I have done everything correctly,

524
00:16:25.750 --> 00:16:25.850
I hope I have done everything correctly Now

525
00:16:25.850 --> 00:16:26.310
what I want to do, I want to

526
00:16:26.310 --> 00:16:28.470
see how much revenue we have made, so

527
00:16:28.470 --> 00:16:30.610
I will remove all these select queries because

528
00:16:30.610 --> 00:16:32.150
they are very basic, you can write them,

529
00:16:32.810 --> 00:16:36.390
what I will do here is that I

530
00:16:36.390 --> 00:16:43.020
will write select sum of amount because I

531
00:16:43.020 --> 00:16:46.060
want to sum the amount, which table are

532
00:16:46.060 --> 00:16:47.900
we talking about here, here we are talking

533
00:16:47.900 --> 00:16:50.340
about the payments table, because that table of

534
00:16:50.340 --> 00:16:52.460
mine, the table of payments, which I have

535
00:16:52.460 --> 00:16:56.340
not even displayed here, I want to see

536
00:16:56.340 --> 00:16:59.460
the sum of amount from that table, as

537
00:16:59.460 --> 00:17:03.780
total revenue, so I am saying sum of

538
00:17:03.780 --> 00:17:12.500
amount as total revenue from payments, from payments,

539
00:17:12.839 --> 00:17:14.720
the name of our table is in the

540
00:17:14.720 --> 00:17:18.099
small case, and if I show you how

541
00:17:18.099 --> 00:17:20.579
our payment table looks like, In this, it

542
00:17:20.579 --> 00:17:22.780
is written how each order has been paid,

543
00:17:23.060 --> 00:17:26.760
now some of our orders must have been

544
00:17:26.760 --> 00:17:30.280
cancelled, so if our order has been cancelled,

545
00:17:30.680 --> 00:17:32.980
then we will not consider it, so you

546
00:17:32.980 --> 00:17:35.720
might want to filter and you might want

547
00:17:35.720 --> 00:17:37.580
to say that the orders that are not

548
00:17:37.580 --> 00:17:39.680
cancelled, just add them or those that are

549
00:17:39.680 --> 00:17:42.520
not pending, but for now, we assume that

550
00:17:42.520 --> 00:17:44.280
this is our total revenue, which has come

551
00:17:44.280 --> 00:17:45.340
to us, now it is a matter of

552
00:17:45.340 --> 00:17:48.100
what has been cancelled, our revenue has been

553
00:17:48.100 --> 00:17:50.020
made, so I will run this and you

554
00:17:50.020 --> 00:17:50.520
can see that we have earned Rs.

555
00:17:50.520 --> 00:17:55.720
21,225 here, as you can see, now

556
00:17:55.720 --> 00:17:57.300
assume that I want to see product by

557
00:17:57.300 --> 00:18:00.700
product revenue, so what will I do, so

558
00:18:00.700 --> 00:18:06.820
I will write here, select p.product name,

559
00:18:07.140 --> 00:18:09.300
now see what I am doing here, p

560
00:18:09.300 --> 00:18:14.220
.product name and sum of, now see what

561
00:18:14.220 --> 00:18:15.720
I will do here, I will join these

562
00:18:15.720 --> 00:18:18.180
two tables, and how I will join smartly,

563
00:18:18.300 --> 00:18:21.040
you have to see, y.quantity, what is

564
00:18:21.040 --> 00:18:24.700
y, y is our order item table, and

565
00:18:24.700 --> 00:18:26.700
what is p, p is our product table,

566
00:18:26.860 --> 00:18:29.480
so I will do sum y.quantity, multiply,

567
00:18:30.120 --> 00:18:32.620
p.price, so what I am doing here,

568
00:18:32.660 --> 00:18:37.340
our order items, which we have stored in

569
00:18:37.340 --> 00:18:39.840
this table, order items, I am saying take

570
00:18:39.840 --> 00:18:41.560
quantity from this table and price from the

571
00:18:41.560 --> 00:18:44.760
product table, okay, and multiply both of them,

572
00:18:44.760 --> 00:18:49.580
and take that as revenue, okay, take that

573
00:18:49.580 --> 00:18:53.080
as revenue, and from where we will select,

574
00:18:53.840 --> 00:18:58.720
from order underscore items, y, and where we

575
00:18:58.720 --> 00:19:00.840
will join, now see where we are joining,

576
00:19:01.380 --> 00:19:02.840
you have to understand this very carefully, okay,

577
00:19:03.260 --> 00:19:06.680
we are joining this in product table, and

578
00:19:06.680 --> 00:19:08.200
we have considered product as p, and after

579
00:19:08.200 --> 00:19:11.580
this we will put another join, and here

580
00:19:11.580 --> 00:19:14.300
we will write orders o, okay, so basically

581
00:19:14.300 --> 00:19:15.060
what we are doing is, we are joining

582
00:19:15.060 --> 00:19:18.580
order item table from product and orders table,

583
00:19:18.680 --> 00:19:22.040
and we have given their names here, y

584
00:19:22.040 --> 00:19:23.860
is our order item table, p is our

585
00:19:23.860 --> 00:19:26.280
product table, and o is our orders table,

586
00:19:26.420 --> 00:19:28.140
okay, now here the join which we are

587
00:19:28.140 --> 00:19:29.500
going to put, how we will put it,

588
00:19:29.580 --> 00:19:32.540
we will say, y.product id should be

589
00:19:32.540 --> 00:19:34.800
equal to p.product id, means add product

590
00:19:34.800 --> 00:19:38.200
id and layout records, then here we will

591
00:19:38.200 --> 00:19:42.880
say, add order id and layout records, okay,

592
00:19:43.340 --> 00:19:44.980
and after this we will put a filter

593
00:19:44.980 --> 00:19:49.340
here, we will say that our order should

594
00:19:49.340 --> 00:19:52.020
be delivered, so o is our order, o

595
00:19:52.020 --> 00:19:55.140
.order status, see our order table has an

596
00:19:55.140 --> 00:19:57.500
order status, it has to be delivered, okay,

597
00:19:59.240 --> 00:20:05.220
status should be equal to delivered, and after

598
00:20:05.220 --> 00:20:07.480
that we can group by, we will say

599
00:20:07.480 --> 00:20:14.040
group by p.product name, okay, and that's

600
00:20:14.040 --> 00:20:16.140
it, I will see what mistake I have

601
00:20:16.140 --> 00:20:20.000
done here, orders o on, on, on, I

602
00:20:20.000 --> 00:20:22.060
forgot to write on, now I will run

603
00:20:22.060 --> 00:20:23.580
it, and see how much revenue we got

604
00:20:23.580 --> 00:20:26.600
from python od, we got to know that,

605
00:20:26.600 --> 00:20:28.940
we also got to know that how much

606
00:20:28.940 --> 00:20:31.240
revenue we got from sticker pack, how much

607
00:20:31.240 --> 00:20:32.680
revenue we got from debugging mug, okay, if

608
00:20:32.680 --> 00:20:34.800
I want to know that which product earned

609
00:20:34.800 --> 00:20:36.400
the most money, then what I will do,

610
00:20:36.640 --> 00:20:41.180
then I will write, order by revenue desc,

611
00:20:42.100 --> 00:20:43.440
so the one who is at the top

612
00:20:43.440 --> 00:20:45.240
earned the most, python od earned the most,

613
00:20:45.780 --> 00:20:47.580
then AI nerd t-shirt also earned the

614
00:20:47.580 --> 00:20:50.480
most, then late night hoodie also earned the

615
00:20:50.480 --> 00:20:53.260
most, at least sticker pack and terminal stickers

616
00:20:53.260 --> 00:20:55.540
earned the most, which is fine, okay, that's

617
00:20:55.540 --> 00:20:58.980
fine, so in this way you can find

618
00:20:58.980 --> 00:21:02.900
out that which product earned the most revenue,

619
00:21:03.880 --> 00:21:04.900
now suppose I want to know the name

620
00:21:04.900 --> 00:21:08.200
of those customers who have spent the most,

621
00:21:09.100 --> 00:21:10.660
so what I will do, I will join

622
00:21:10.660 --> 00:21:15.000
customer table in orders and payments table, so

623
00:21:15.000 --> 00:21:16.040
what I will do, I will join customer

624
00:21:16.040 --> 00:21:18.880
table in order table, because my customer table,

625
00:21:19.580 --> 00:21:21.600
I have to join customer table in order

626
00:21:21.600 --> 00:21:25.700
table, or suppose I have customer id in

627
00:21:25.700 --> 00:21:26.040
my orders table, so I will join these

628
00:21:26.040 --> 00:21:28.260
two, after joining these two, I will make

629
00:21:28.260 --> 00:21:31.540
data, after that you can see our payments

630
00:21:31.540 --> 00:21:36.560
table, what is there in payments table, there

631
00:21:36.560 --> 00:21:39.220
is order id in it, and where I

632
00:21:39.220 --> 00:21:40.860
have to match this order id, I have

633
00:21:40.860 --> 00:21:43.500
to match it with orders order id, so

634
00:21:43.500 --> 00:21:45.040
you can find out that which are your

635
00:21:45.040 --> 00:21:48.520
top customers who have spent, and I want

636
00:21:48.520 --> 00:21:52.320
you to understand this thing properly, so first

637
00:21:52.320 --> 00:21:53.520
of all, you have to try this question,

638
00:21:54.440 --> 00:21:56.300
that if you want to find top customers

639
00:21:56.300 --> 00:21:58.700
by spend, that which customers have spent the

640
00:21:58.700 --> 00:22:02.280
most, then what type of query you have

641
00:22:02.280 --> 00:22:04.740
to make, and once if you try to

642
00:22:04.740 --> 00:22:06.900
make query and you are not able to

643
00:22:06.900 --> 00:22:10.280
make it, then you can find the solution

644
00:22:10.280 --> 00:22:13.660
in the handbook, after this I have also

645
00:22:13.660 --> 00:22:15.380
told you how you can make best selling

646
00:22:15.380 --> 00:22:16.960
products, so that you can find out best

647
00:22:16.960 --> 00:22:19.700
selling products, and to find out best selling

648
00:22:19.700 --> 00:22:21.840
products, what you have to do is, you

649
00:22:21.840 --> 00:22:23.260
don't have to look at revenue, now many

650
00:22:23.260 --> 00:22:24.560
of you will argue that this is not

651
00:22:24.560 --> 00:22:25.860
a best selling product, you have to look

652
00:22:25.860 --> 00:22:27.340
at it according to quantity, you have to

653
00:22:27.340 --> 00:22:31.660
find out that which product has sold the

654
00:22:31.660 --> 00:22:35.460
most, means which product has sold the most,

655
00:22:35.460 --> 00:22:38.900
so you have to sum the quantity, you

656
00:22:38.900 --> 00:22:39.540
will also get the answer to this in

657
00:22:39.540 --> 00:22:42.280
the handbook, now let's say I want to

658
00:22:42.280 --> 00:22:43.120
find out that how many orders have been

659
00:22:43.120 --> 00:22:47.440
cancelled, so if I want to find out

660
00:22:47.440 --> 00:22:48.520
the count of cancelled orders, then how will

661
00:22:48.520 --> 00:22:50.120
I find it out, so I will write

662
00:22:50.120 --> 00:22:55.320
select count star, and I will write as

663
00:22:55.320 --> 00:22:58.740
cancelled, and after this I will write from

664
00:22:58.740 --> 00:23:04.780
orders, and I will write where, and simply

665
00:23:04.780 --> 00:23:08.460
I will write order status is equal to

666
00:23:08.460 --> 00:23:13.820
cancelled, and it's that simple, that's it, there

667
00:23:13.820 --> 00:23:15.520
are 3 cancelled orders, this was very simple,

668
00:23:15.860 --> 00:23:17.900
now you can get many insights like this,

669
00:23:19.160 --> 00:23:22.560
and I hope you enjoyed this project, because

670
00:23:22.560 --> 00:23:25.760
here we have designed a database which can

671
00:23:25.760 --> 00:23:28.620
be passed on to a web developer, and

672
00:23:28.620 --> 00:23:29.100
he can make a whole website on this

673
00:23:29.100 --> 00:23:34.160
database design, so you guys have done your

674
00:23:34.160 --> 00:23:36.480
work as a data analyst, you have designed

675
00:23:36.480 --> 00:23:40.980
a good SQL database with tables, with correct

676
00:23:40.980 --> 00:23:44.140
foreign keys, with correct primary keys, I hope

677
00:23:44.140 --> 00:23:47.300
you guys liked this project, and along with

678
00:23:47.300 --> 00:23:49.500
that you guys have chat gpt, you can

679
00:23:49.500 --> 00:23:53.160
ask chat gpt to design it, and you

680
00:23:53.160 --> 00:23:56.040
can ask more questions regarding your data from

681
00:23:56.040 --> 00:23:57.620
chat gpt, I have also told you how

682
00:23:57.620 --> 00:23:58.800
to do that, you guys have to watch

683
00:23:58.800 --> 00:24:01.740
the chat gpt video, if you haven't watched

684
00:24:01.740 --> 00:24:03.280
it, I hope you have watched it, in

685
00:24:03.280 --> 00:24:04.200
which I have told you how to use

686
00:24:04.200 --> 00:24:07.700
chat gpt, I hope you guys are enjoying

687
00:24:07.700 --> 00:24:10.280
this project so far, and I hope you

688
00:24:10.280 --> 00:24:13.520
understood SQL, before ending this project, I want

689
00:24:13.520 --> 00:24:15.020
to tell you that you will have to

690
00:24:15.020 --> 00:24:17.860
practise a lot to clean your hands in

691
00:24:17.860 --> 00:24:19.100
SQL, because it will take you a lot

692
00:24:19.100 --> 00:24:21.020
of time to become an expert, it will

693
00:24:21.020 --> 00:24:22.420
take you a lot of time to gain

694
00:24:22.420 --> 00:24:24.400
fluency, so I want you guys to gain

695
00:24:24.400 --> 00:24:28.400
that fluency, I hope you guys enjoyed this

696
00:24:28.400 --> 00:24:30.320
project, and I hope you guys enjoyed the

697
00:24:30.320 --> 00:24:32.960
course so far, see you in the next

698
00:24:32.960 --> 00:24:33.240
video.



━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

==================================================================================

# Section 5: Advanced_python




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━




━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━








