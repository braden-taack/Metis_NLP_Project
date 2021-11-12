'''
Make sure to install streamlit with `conda install -c conda-forge streamlit`.

Run `streamlit hello` to get started!

Streamlit is *V* cool, and it's only going to get cooler (as of February 2021):

https://discuss.streamlit.io/t/override-default-color-palette/9088/2

To run this app, run `streamlit run streamlit_app.py` from inside this directory
'''

#import necessary libraries 
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import pickle as pkl
import corextopic
import scipy

#set page configuration settings
#use this for cloud icon 'https://cdn-icons-png.flaticon.com/512/616/616682.png'
st.set_page_config(page_title = 'Music Tweets', 
    page_icon ='https://emoji.slack-edge.com/T01MF50RVGV/party-blob/16b9ca5fe1f173c7.gif')
st.config.set_option('theme.base','light') #picture is light so need dark text for readability

#add background image manually
page_bg_img = '''

<style>
section {
    background-image: url("https://images.unsplash.com/photo-1574504212584-29a03eb6e41e?ixid=MnwxMjA3fDB8MHxzZWFyY2h8NTl8fG11c2ljJTIwYmFja2dyb3VuZHxlbnwwfHwwfHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=900&q=60");
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


#print headers and project description
st.write(
'''
# Musical Tweets  
#### Braden Taack  
  
What are people talking about on Twitter with regard to music? Check out the results for my CorEx topic model
for tweets found using the keyword search 'music' from 2021-11-02 to 2021-11-09.   
*Advisory Warning*: Please note that I have tried to keep the integrity of the original Tweets, so there may be explicit material in the content.  

The data was scrapped using [Snscrape](https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af).

The background image has been sourced from [Antoine Julien's](https://unsplash.com/@antoinejulien) photo library on Unsplash.com.

See my Source Code [here](https://github.com/braden-taack/Metis_NLP_Project)!
___
''')

#import pickle data with loading messages
@st.cache
def load_data(filename):
    return pkl.load(open("Data/"+str(filename)+".pkl",'rb'))

data_load_state = st.text('Loading Corex Model...')
topic_model = load_data('corex_model')
data_load_state.text('Loading Corex Model...done!')

data_load_state.text('Loading Tweets...')
tweets_df = load_data('tweets_df')
data_load_state.text('Loading Tweets...done!')

#initialize topic labels
topic_labels = {'Astroworld Tragedy':0, 'Radio':1, 'Streaming':2, 'Video':3, 'Events':4, 'NFTs':5,
                   'New':6, 'Christmas':7,'Music Taste':8,'School':9,'Rap':10,'Rock':11,'Pop':12,'Jazz':13,
                   'Twitter':14,'Emojis':15,'BTS':16,'T Swift':17,'Music Note':18,'Feels':19,
                   'General Smack Talk':20,'General Smack Talk 2':21,'blackltdradio':22,'Misc 1':23,'Misc 2':24}

#function to display tweets and word mutual information
def analyze_topic(df, topic=0, n_tweets=10,n_words=10 ):
    topic_idx = topic_labels[topic]

    word_df = pd.DataFrame(topic_model.get_topics(n_words = n_words, topic = topic_idx))
    word_df.sort_values(by=1, ascending = True, ignore_index = True,inplace=True)

    fig_bar = px.bar(y = word_df[0], x=word_df[1]*word_df[2],orientation='h', 
        labels={'y':'Word','x':'Mutual Information (MI)'},title='Word MI in Topic: '+str(topic))
    st.plotly_chart(fig_bar,use_container_width=True)

    for i, x in enumerate(topic_model.get_top_docs(topic=topic_idx, n_docs=n_tweets, print_docs=False)):
        st.write('Tweet ' +str(i) +": "+df['content'][x[0]])

#trending topic header
st.write(
    '''
    ### Trending Topics
    ''')

#plot topics correlation
topic_bar = px.bar(x = range(topic_model.tcs.shape[0]),y = topic_model.tcs,
            orientation='v', labels={'x':'Topic','y':'Total Correlation (nats)'})
topic_bar.update_layout(
        xaxis = dict(
        tickmode = 'array',
        tickvals = tuple(range(topic_model.tcs.shape[0])),
        ticktext = list(topic_labels.keys())))
st.plotly_chart(topic_bar,use_container_width=True)

#topic analyze header
st.write(
    '''
    ___  

    ### Pick a Topic to Further Analyze
    ''')

#print top tweets and plot top words for a chosen topic
topic = st.selectbox('Please select a topic', list(topic_labels.keys()))
row0_1, row0_2 = st.columns(2)
with row0_1:
    n_tweets = st.slider('Select # of tweets to display: ', min_value=0, max_value=50, value=10)
with row0_2:
    n_words = st.slider('Select # of words to display: ', min_value=0, max_value=20, value=15)

analyze_topic(df = tweets_df,topic=topic, n_tweets=n_tweets,n_words=n_words)
data_load_state.text('') #remove loading text when tweets and plot are displayed

