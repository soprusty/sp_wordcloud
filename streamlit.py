import sys
import subprocess


#!pip3 install textblob
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'textblob'])

##subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
##'textblob'])

import subprocess
cmd = ['python','-m','textblob.download_corpora']
subprocess.run(cmd)

import nltk
nltk.download('brown')
nltk.download('punkt')

#python3 -m textblob.download_corpora
from textblob import TextBlob

import streamlit as st
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.subheader('Build Summary')
text=st.text_area('Please Enter the text here')
SampleTextInBlobFormat = TextBlob(text)
NounPhrases=SampleTextInBlobFormat.noun_phrases

NewNounList=[]
for words in NounPhrases:
    NewNounList.append(words.replace(" ", "_"))

NewNounString=' '.join(NewNounList)    

if text:
  w=WordCloud(max_words=50,
              font_step=2,
              max_font_size=500,
              width=1000,
              height=720,
              background_color='white',
              stopwords = STOPWORDS).generate(NewNounString)
  plt.axis("off")
  plt.imshow(w,interpolation='bilinear')
  #plt.imshow(wordcloud, interpolation='bilinear')
  plt.show()
  st.pyplot()
