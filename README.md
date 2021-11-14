Braden Taack
### Musical Tweets NLP Project
#### November 12, 2021
---

#### Abstract
  
The goal of this project is to analyze Tweets about music using Natural Language Processing (NLP) and topic modeling techniques. The dataset of tweets was obtained using [snscrape](https://github.com/JustAnotherArchivist/snscrape). The data was initially stored in a pandas dataframe. The tweets were preprocessed using the NLTK library. Topic modeling was performed with Sci-kit Learn and the results were plotted with plotly. The final product consists of an interactive dashboard built with Streamlit and deployed with Heroku. The web app allows the user to select a topic and look at the top words and documents (tweets) associated with that topic. Follow the link to view the [Music Tweets Dashboard](https://metis-musical-tweets-project.herokuapp.com/)!


#### Design

Music is one of my favorite ways to pass the time, help me relax, or to get excited for a big day. I have always been interested in music and talking about new artists or shows. There are many discussion to be had about music and my goal with this project is to explore what people on Twitter are talking about when it comes to music. Are they tweeting about an up and coming star? Are they cyberbullying a famous musician? Are people discussing music academically? To explore these questions, I have gathered 50000 tweets from the week of 2021-11-02 to 2021-11-09. 

The general pipeline of the process is: data gathering, cleanup, text preprocessing, topic modeling, and visualization. 

#### Data
  
The datas was sourced using [snscrape](https://github.com/JustAnotherArchivist/snscrape). The library is an excellent resource for accessing different content or user information across different social media sites such as Reddit, Twitter, and Facebook. 50,000 Tweets were scrapped using 'music' as the keyword. The time range was limited from 2021-11-02 to 2021-11-09 in order to look at current topics and to keep processing quick. 3800 different word tokens were created after text preprocessing from the data. 
  
For the dashboard, the tweets dataframe and CorEx topic model were saved as pickle objects, which could be loaded into the webpage on the page request. 
  
#### Algorithms
  
*Data Cleanup* 
  
  The first issue with the data arose with different languages. Several of the text preprocessing steps and topic models would suffer with non-english vocabulary. Conveniently, the dataframe from snscrape had a feature that listed the language of the tweet. So, I simply masked the dataframe to only include english tweets. 
  
  The next issues actually came after text preprocessing: empty tweets and duplicate tweets. Empty tweets arose occasionally when a tweet was comprised entirely of items that are removed during the text preprocessing steps such as hyperlinks and @mentions. The empty tweet did not provide any additional information so they were removed. Similarly, duplicated tweets did not add any new words or information, so they were removed too. 
  
*Text Preprocessing*
  
  Extensive text preprocessing was needed for efficient and productive topic modeling. The final preprocessing steps were:
  1. Remove emojis  
    - Used emoji library
    - 'demojified' emojis to return text
    - i.e. 🙂 -> slightly smiley face
  3. Make all text lower case  
    - Apply .lower() to all text
  5. Remove special characters  
    - Uses regex substitutes 
      - '' for @mentions
      - '' for # hashtag symbol
      - '' for hyperlinks (https://...)
      - ' ' for numbers
      - ' ' for punctuation in string.punctuation
  7. Lemmatization  
      - Helped reduce overall word count and simplified some common tokens
  9. Remove stop words  
    - Included NLTK's stopwords.words('english') and Sci-kit Learn's ENGLISH_STOP_WORDS  
    - Added:
      - Music
      - Bit , ly - to account for missed links
      - com, net, org, co - some websites were listed without a link
      - like - was very common
  10. Tokenize  
      - Used CountVectorizer from Sci-Kit Learn
      - max_df = 0.1 (no words kept if in >10% of documents)
      - min_df = 15 (words must be in at least 15 documents)
  
*Topic Modeling*  
  
Three different topic models were created and compared: NMF, CorEx, and LDA. Numerous iterations for each model was undergone in search of decent topic modeling results. The criteria for a successful topic model consisted of clear topics based on both the top words and top documents, and high correlation metric results relative to previous efforts. I ran through many different parameter changes including the number of topics, different text preprocessing steps, different anchors and anchor strengths for CorEx, and use of CountVectorizer vs. TfidfVectorizer.  
  
In the end, I was happiest with the Corex model and focused in more with aggressive anchoring. I started with 50 topics and slowly began adding words from the most significant topics based on topic correlation as anchor words. I settled on 23 anchors with an anchor strength of 5 with a total of 25 topics. 
  
*Streamlit Application*  
  
1. Set Page Config Options  
    - Add custom background image
    - Set theme to be light so text would show up better
    - Change page header and icon (for fun)
2. Import Local Data from pickles  
    - Import tweets DataFrame 
    - Import CorEx topic model
    - Add loading message to application, clears when complete
3. Trending Topics Bar Plot  
    - Plots topic correlations from the model using Plotly
    - Updates xticks to be topic labels rather than numbered range
4. Analyze Topics Function  
    - User specified topic, number of tweets, and number of words to display
    - Creates word dataframe of top words in the given topic
    - Sorts words by absolute value of their respective Mutual Information (MI) value
    - Plots horizontal Plotly bar chart of words and MI values
    - Finds top documents for a given topic and prints them
  
#### Tools

- [snscrape](https://github.com/JustAnotherArchivist/snscrape) for Tweet scrapping
- NLTK, regex, sklearn.feature_extraction.text, and emoji libraries for text preprocessing
- Pandas for data ingestion and basic exploration
- sklearn.decomposition and corextopic for topic modeling
- Pickle for tweet dataframe and topic model storage
- Plotly for data visualization
- Streamlit for web application development
- Heroku for app deployment

#### Conclusions  
  
As my first project working with NLP techniques, I was satisfied with being able to get some reasonable topics from my dataset. I was also happy to see the topic model pick up on some real trends on Twitter such as Spotify wrapped and Christmas music, as each of these items take place at the end of the year people generally start talking about them now. However, with the complexity of language there is always more to explore and understand. There are lots of other topic modeling choices out there and I had not even attempted clustering with this data set!  
  
In the future, I would like to analyze this data set with clusters and also look at more specific searches (i.e. I already have 2 new data sets with keyword searches around Dua Lipa and Tame Impala, 2 of my favorite artists). 

