import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.subheader('wordcloud app')
text=st.text_input('enter text')

if text:
  w=WordCloud().generate(text)
  plt.imshow(w)
  st.pyplot()





#pip install streamlit-wordcloud
#pip install streamlit_wordcloud
#
#import streamlit_wordcloud as wordcloud



# Create some sample text
#text = 'Fun, fun, awesome, awesome, tubular, astounding, superb, great, amazing, amazing, amazing, amazing'

# Create and generate a word cloud image:
#wordcloud = WordCloud().generate(text)

# Display the generated image:
#plt.imshow(wordcloud, interpolation='bilinear')
#plt.axis("off")
#plt.show()
#st.pyplot()
