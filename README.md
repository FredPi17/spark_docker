##HOW TO RUN SPARK

- You have to set your input text you want to count in input.txt
- Change your configuration script in test.py if you want

Then run `docker-compose up -d` to run the master and two masters.

##HOW TO LAUNCH A JOB 

Connect into the docker image: 
`docker exec -ti spark-master /bin/bash`

Then go into: `/spark/bin `

And run: `./spark-submit test.py`