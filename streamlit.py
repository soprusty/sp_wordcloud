import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt


#st.title('Customer Transaction Predictor')
##st.image("""https://www.india.com/wp-content/uploads/2014/08/666.jpg""")
#st.header('Enter the characteristics of the Customer:')
etext = st.text_area("Enter Something here! ")
st.write(etext)
wordcloud = WordCloud().generate(etext)

##wordcloud = WordCloud(width = 800, height = 800,
 #               background_color ='white',
  #              stopwords = stopwords,
   #             min_font_size = 10).generate(etext)

##plt.figure(figsize = (8, 8), facecolor = None)
##plt.imshow(wordcloud)
##plt.tight_layout(pad = 0)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
