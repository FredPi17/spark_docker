##Case with hadoop

Run `docker-compose up -d`

At first, create a new directory directly in `hadoop/Utilities/Browse the file system`

Create a directory of your choice, in my case i created `/test`

And push the input.txt into the hadoop filesystem with this command: 

`hadoop fs -put input.txt /test`

Then, in the namenode container execute these commands: 

`hdfs fs -put input.txt /test`

