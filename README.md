# twitter_bot
Twitter bot for analysing sentiment

To build docker image:

```console
docker build -t tweepy_bot:0.01 .
docker tag tweepy_bot:0.01 geccles17/tweepy_bot:latest
```
 
To run docker image:
Replace Keys and Search word with desired word to search tweets for.

```console
docker run -it -e CONSUMER_KEY="xxx" -e CONSUMER_SECRET="xxx" -e ACCESS_TOKEN="xxx-xxx" -e ACCESS_TOKEN_SECRET="xxx" -e SEARCH_WORD="xxx" geccles17/tweepy_bot
```

Example output for search word Arsenal:
![image](https://user-images.githubusercontent.com/60923586/185190635-636a28c1-9364-4abb-b24d-c125d164f492.png)

References:
https://realpython.com/twitter-bot-python-tweepy/
