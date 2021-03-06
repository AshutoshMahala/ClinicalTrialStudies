![Was It Active](https://www.flaticon.com/svg/static/icons/png/128/3017/3017586.png) 

# ClinicalTrialStudies
This API provides data directly from https://clinicaltrials.gov/
It checks if the disease was active in last n days

Uselful link:
https://prsinfo.clinicaltrials.gov/prs-xml-schemas.html

Aim: Given a tuple of Disease and RSS feeds, determine which disease had no activity for a given number of days
 
RSS feeds from ClinicalTrials.gov as an example 
*	Wolman Disease https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=14&cond=Wolman+Disease&count=10000
*	Alzheimer Disease https://clinicaltrials.gov/ct2/results/rss.xml?rcv_d=30&cond=Alzheimer+Disease&count=10000
 

[![Testing on Postman](https://files.realpython.com/media/flask-nginx-gunicorn-architecture.012eb1c10f5e.jpg)](https://youtu.be/AF76jtQVJ8o)

## Requirements:
In order to run the RSSCrawler
1. intall Python 3
``` 
pip3 install feedparser 
```

In order to run flask server run below command
````
pip3 install flask
````

In order to run test cases
```
pip3 install pytest
```

## How to Run
1. To Run RSSCrawler provide 2 commandline argument when starting 
  1. Disease Name
  1. Number of Inactive days from now
  ```
  python3 RSSCrawler covid19 5
  ```
1. To Run Test case, run below commands
  ```
  pytest
  ```
1. To Run flask server, run below command
  ```
  flask run
  ```

### Attributions:
Icons made by https://www.flaticon.com/authors/smalllikeart at https://www.flaticon.com/
