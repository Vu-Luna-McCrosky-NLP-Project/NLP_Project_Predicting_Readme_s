import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud
from PIL import Image



def javascript_barh(word_counts):
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "javascript": "orange"})
    plt.title('JavaScript vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()

    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'java']].plot.barh(figsize=(18,10), color={"java": "brown", "javascript": "orange"})
    plt.title('JavaScript vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "javascript": "orange"})
    plt.title('JavaScript vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    
def python_barh(word_counts):
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['javascript', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "javascript": "orange"})
    plt.title('JavaScript vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()

    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['python', 'java']].plot.barh(figsize=(18,10), color={"java": "brown", "python": "blue"})
    plt.title('Python vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['python', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "python": "blue"})
    plt.title('Python vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
def java_barh(word_counts):
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'javascript']].plot.barh(figsize=(18,10), color={"java": "brown", "javascript": "orange"})
    plt.title('Java vs. JavaScript Words')
    plt.xlabel('\nFrequency')
    plt.show()

    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'python']].plot.barh(figsize=(18,10), color={"python": "blue", "java": "brown"})
    plt.title('Java vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['java', 'go']].plot.barh(figsize=(18,10), color={"go": "aqua", "java": "brown"})
    plt.title('Java vs. Go Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
def go_barh(word_counts):
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'javascript']].plot.barh(figsize=(18,10), color={"go": "aqua", "javascript": "orange"})
    plt.title('Go vs. JavaScript Words')
    plt.xlabel('\nFrequency')
    plt.show()

    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'python']].plot.barh(figsize=(18,10), color={"go": "aqua", "python": "blue"})
    plt.title('Go vs. Python Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
    plt.rc('font', size=18)
    word_counts.sort_values('all', ascending=False).head(20)[['go', 'java']].plot.barh(figsize=(18,10), color={"go": "aqua", "java": "brown"})
    plt.title('Go vs. Java Words')
    plt.xlabel('\nFrequency')
    plt.show()
    
def simple_wordcloud(language):
    img = WordCloud(background_color='white', colormap = 'ocean', width=800, height=600).generate(language)
    plt.figure(figsize=(12,6))
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def simple_wordclouds(language_words):
    print('JavaScript, Python, Java, and Go Wordclouds (single words)')
    for i in language_words:
        simple_wordcloud(i)
        print('\n')