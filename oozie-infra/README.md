##Configuration with OOZIE

Inspired by: 
https://github.com/ezra-quemuel/hadoop-oozie


Run `docker-compose up -d`

At first, create a new directory directly in `hadoop/Utilities/Browse the file system`

Create a directory of your choice, in my case I created `/test`

And push the input.txt into the hadoop filesystem with this command: 

`hadoop fs -put input.txt /test`

Then, in the spark-master container execute these commands: 

`cd spark/bin`

`./spark-submit test.py `

You can access to these web interfaces: 

- spark-master: http://localhost:8080
- oozie: http://localhost:11000
- hadoop: http://localhost:9870

Documentation on workflows: 
https://www.tutorialspoint.com/apache_oozie/apache_oozie_workflow.htm 

Documentation on Spark with oozie:
https://mapr.com/docs/home/Oozie/RunSparkJobswithOozie.html