import sys
import subprocess


#!pip3 install textblob
# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'textblob'])

##subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
##'textblob'])

python -m textblob.download_corpora

from textblob import TextBlob

import streamlit as st
from wordcloud import WordCloud,STOPWORDS
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.subheader('wordcloud app')
text=st.text_input('enter text')
SampleTextInBlobFormat = TextBlob(text)
NounPhrases=SampleTextInBlobFormat.noun_phrases

NewNounList=[]
for words in NounPhrases:
    NewNounList.append(words.replace(" ", "_"))

NewNounString=' '.join(NewNounList)    

if text:
  w=WordCloud(background_color='white',stopwords = STOPWORDS).generate(NewNounString)
  plt.axis("off")
  plt.imshow(w,interpolation='bilinear')
  #plt.imshow(wordcloud, interpolation='bilinear')
  plt.show()
  st.pyplot()
