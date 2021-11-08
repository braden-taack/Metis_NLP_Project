Braden Taack
### Music Tweets NLP Project MVP
#### November 8th, 2021
___

#### MVP
  
Music is one of my favorite ways to pass the time, help me relax, or to get excited for a big day. I have always been interested in music and talking about new artists or shows. There are many discussion to be had about music and my goal with this project is to explore what people on Twitter are talking about when it comes to music. Are they tweeting about an up and coming star? Are they cyberbulling a famous musician? Are people discussing music academically? I want to gather a set of tweets about music from a recent time range and analyze them using NLP techniques in order to discover unique topics of musical conversation.

For this project, 10,000 tweets have been downloaded using the keyword search: music. The snscrape libaray was used for the tweet downloads as it makes it easier to get large amounts of tweets in a short amount of time. It does not have as much flexbility as the Twitter API v2 does, but the Twiiter API is much more limited on rate. They only allow the standard developer's account to gather 900 tweets every 15 minutes. Also, my developer acccount was suspended which made snscrape an easy choice for this project. 

Thus far, I have successfully created a text preprocessing pipeline for my tweets. The pipeline processess in the following order:

  1. Remove Emojis
  2. Make all text lowercase
  3. Remove mentions, hashtags, punctuation, numbers, hyperlinks
  4. Remove non-english words
  5. Remove tweets if empty due to character removal
  6. Remove duplicate cleaned tweets

I have also created a basic 5 component NMF model with minor success. I have arbitrarily chosen 5 components for exploratory work with the data. As far as I can make out so far, the 5 topics are: liking/listening to music, offical music videos, music taste, new releases, and applemusic (leas).

#### Further Work  
I would like to incorporate more text preprocessing with lammetization. I currently am getting about 7000 words for my 10,000 tweets so I could still likely benefit from further dimensionality reduction.  
  
I am also going to try and LDA model in order to leverage pyLDAvis which may help my topic modeling. Further, I also intend to do some work with clustering to gather more information about my data. 

Lastly, if the data does not produce good enough results. I will gather more tweets and get more specific with my keyword search (i.e. alternative music, or Tame Impala, etc). 
