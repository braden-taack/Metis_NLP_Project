___
Braden Taack
###  Music Tweets Project Proposal 
#### November 3rd, 2021
___
  

#### Question/need:
* What is the framing question of your analysis, or the purpose of the model/system you plan to build?   
  
  Music is one of my favorite ways to pass the time, help me relax, or to get excited for a big day. I have always been interested in music and talking about new artists or shows. There are many discussion to be had about music and my goal with this project is to explore what people on Twitter are talking about when it comes to music. Are they tweeting about an up and coming star? Are they cyberbulling a famous musician? Are people discussing music academically? I want to gather a set of tweets about music from a recent time range and analyze them using NLP techniques in order to discover unique topics of musical conversation. 
  
* Who benefits from exploring this question or building this model/system?  
  
  Music lovers and data scientist can unionize their loves here to discover what exactly are people talking about on Twitter when it comes to music.  
  
#### Data Description:
* What dataset(s) do you plan to use, and how will you obtain the data?  
  
  I plan to make use of the [Twitter API](https://developer.twitter.com/en/portal/projects/1455703406828408832/apps/22385811/keys) for my project to search keywords on Twitter and download relevant tweets. I already have an example project up and running under a developers account. I hope to download as many tweets as my rate limit will allow. I will likely explore different keyword searches other than music to get a more diverse set of documents. I may look for certain genres such as rock or alternative, or certain artists like Dua Lipa. 

  
* What is an individual sample/unit of analysis in this project? What characteristics/features do you expect to work with?  
  
  An individual sample will be a single tweet. The features will be tokenized words, n-grams, and potentially other engineered features from techniques such as feature extraction. 
  
* If modeling, what will you predict as your target? 

  I am not anticipating including a model at this time. If I were to include one, I may try a classification model. However, the focus will be on NLP and EDA.  
  
#### Tools:
* How do you intend to meet the tools requirement of the project?  
 
  I will be using an API to pull in my data. For NLP tools, I plan on using NLTK and TextBlob to help me handle the text data. For any data visualization, I will likely use a combo of Matplotlib, Seaborn, and Plotly. 

#### MVP Goal:
* What would a [minimum viable product (MVP)](./mvp.md) look like for this project?  
  
  The goal for the MVP of my project would be to have my dataset downloaded, to have a text preprocessing pipeline established, and some basic NLP techniques applied to the data such that I can evaluate the most popular topics for the dataset. 
  
#### Alternate Project Idea:
  
  Should this project not work out, I may choose cryptocurrency as an alternate topic and look for a pre-made dataset from kaggle to proceed. 
