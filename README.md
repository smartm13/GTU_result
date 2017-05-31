# GTU_result
small py-project to obtain data from result1.gtu.ac.in after cracking its captcha
It will save as and when any result is obtained once.

Still working on it.   :|

So no ui made.

Request ur result at:
http://ec2-35-166-11-103.us-west-2.compute.amazonaws.com:8082/result?enrol=140280116051&exam=besem5reg&html=1

Modify get params accordingly.
exam is short string for exam text as visible on http://result1.gtu.ac.in
(for "BE SEM 5 - Regular (DEC 2016)" it can be anything in besem5regulardec2016)
html=1 will append the html view of result along with spi and cpi data.

Sample stored result:
http://ec2-35-166-11-103.us-west-2.compute.amazonaws.com:8082/results/140280116051.html
