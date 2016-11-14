from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image

import re
with open("test.txt") as f:
    lines = f.readlines()

text = "".join(lines)

freq = {}
stopwords=set(STOPWORDS)
stopwords.add('u')

mmask = np.array(Image.open('twiiter_mask.png'))

wordcloud = WordCloud(background_color="white", max_words=2000,mask=mmask,
               stopwords=stopwords)
wordcloud.generate(text)
wordcloud.to_file('c:\python27\wprdcloud.png')
image=wordcloud.to_image()
image.show()
