import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image

#all colors were based off of Github's assigned colors for each language, although JavaScript is orange because the Github's color
#was yellow, and it made it hard to see


def javascript_barh(word_counts):
    '''
    this function will take in a word_counts series, find the top 20 most common words and plot JavaScript vs
    our other languages with respect to how often each language uses those words
    '''
    #set font size, take 20 most common words, javascript vs. python
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "javascript": "orange"})
    plt.title('JavaScript vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()

    #set font size, take 20 most common words, javascript vs. java
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'java']].plot.barh(figsize=(18,10), color={"java": "brown", "javascript": "orange"})
    plt.title('JavaScript vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    #set font size, take 20 most common words, javascript vs. go
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "javascript": "orange"})
    plt.title('JavaScript vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
def python_barh(word_counts):
    '''
    this function will take in a word_counts series, find the top 20 most common words and plot Python vs
    our other languages with respect to how often each language uses those words
    '''
    #set font size, take 20 most common words, python vs javascript
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "javascript": "orange"})
    plt.title('JavaScript vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()

    #set font size, take 20 most common words, python vs java
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['python', 'java']].plot.barh(figsize=(18,10), color={"java": "brown", "python": "blue"})
    plt.title('Python vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    #set font size, take 20 most common words, python vs go
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['python', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "python": "blue"})
    plt.title('Python vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
def java_barh(word_counts):
    '''
    this function will take in a word_counts series, find the top 20 most common words and plot Java vs
    our other languages with respect to how often each language uses those words
    '''
    #set font size, take 20 most common words, java vs javascript
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'javascript']].plot.barh(figsize=(18,10), color={"java": "brown", "javascript": "orange"})
    plt.title('Java vs. JavaScript Words')
    plt.xlabel('\nFrequency')
    plt.show()

    #set font size, take 20 most common words, java vs python
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "java": "brown"})
    plt.title('Java vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    #set font size, take 20 most common words, java vs go
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "java": "brown"})
    plt.title('Java vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
def go_barh(word_counts):
    '''
    this function will take in a word_counts series, find the top 20 most common words and plot Go vs
    our other languages with respect to how often each language uses those words
    '''
    #set font size, take 20 most common words, go vs javascript
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'javascript']].plot.barh(figsize=(18,10), color={"go": "aqua", "javascript": "orange"})
    plt.title('Go vs. JavaScript Words')
    plt.xlabel('\nFrequency')
    plt.show()

    #set font size, take 20 most common words, go vs python
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'python']].plot.barh(figsize=(18,10), color={"go": "aqua", "python": "blue"})
    plt.title('Go vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    #set font size, take 20 most common words, go vs java
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'java']].plot.barh(figsize=(18,10), color={"go": "aqua", "java": "brown"})
    plt.title('Go vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
def simple_wordcloud(language):
    '''
    this function will generate a wordcloud (single words only) based on the target language inputted
    '''
    #initialize word cloud 
    img = WordCloud(background_color='white', colormap = 'ocean', width=800, height=600).generate(language)
    plt.figure(figsize=(12,6))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def simple_wordclouds(language_words):
    '''
    this function will print out all of the simple word clouds
    '''
    print('JavaScript, Python, Java, and Go Wordclouds (single words)')
    for i in language_words:
        simple_wordcloud(i)
        print('\n')