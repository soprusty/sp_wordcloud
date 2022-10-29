import sys
import subprocess

# implement pip as a subprocess:
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 
'wordcloud'])

import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


st.subheader('wordcloud app')
text=st.text_input('enter text')

if text:
  w=WordCloud(background_color='white').generate(text)
  plt.axis("off")
  plt.imshow(w)
  #plt.imshow(wordcloud, interpolation='bilinear')
  plt.show()
  st.pyplot()
