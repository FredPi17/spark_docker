##Case with hadoop

Run `docker-compose up -d`

At first, create a new directory directly in `hadoop/Utilities/Browse the file system`

Create a directory of your choice, in my case I created `/test`

And push the input.txt into the hadoop filesystem with this command: 

`hadoop fs -put input.txt /test`

Then, in the spark-master container execute these commands: 

`cd spark/bin`

`./spark-submit test.py `

