# TwitOff

A web app for comparing Twitter users!

You select 2 users and make up a tweet and we tell you who is more likely to tweet that. If you don't see a user you want in the list, you can add them.

The data is pulled from Twitter's API and stored in a PostgreSQL Database. When you add a user, it collects their recent tweets. The model uses Basilica for word embeddings, and then a logistic regression to predict a probability of likelihood for each tweeter. 

Deployed using Flask and Heroku.


