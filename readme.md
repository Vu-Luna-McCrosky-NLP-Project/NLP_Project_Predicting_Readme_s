![image](https://github.com/lupeluna/README_FILES/blob/main/NLP%20Project%20Predicting%20READMEs-3.gif)


by: Forrest McCrosky, Lupe Luna, Anna Vu

Hello,

Welcome to the README file for our [NLP Project](https://nbviewer.jupyter.org/github/Vu-Luna-McCrosky-NLP-Project/NLP_Project_Predicting_Readme_s/blob/master/final_nlp.ipynb) 

Find our project-planning [Trello here](https://trello.com/b/DlD8CmLW/nlp-project) 

Here, you will find our work on the NLP_df.csv file which contains Github repos that include the README contents.  You will also find the data dictionary to help offer more insight to the variables being used.
<br>

## Table of Contents
---

A.   [Project Overview             ](#a-project-overview)
1.   [Project Description          ](#1-project-description)
2.   [Project Deliverables         ](#2-project-deliverables)

B.  [Project Summary               ](#b-project-summary)
1.   [Goals                        ](#1-goals)
2.   [Initial Thoughts & Hypothesis](#2-initial-thoughts--hypothesis)
3.   [Findings & Next Steps        ](#3-findings--next-steps)

C. [Data Context                 ](#c-data-context)
1.   [About Our Data             ](#1-about-our-data)
2.   [Data Dictionary              ](#2-data-dictionary)

D.  [Pipeline                     ](#d-pipeline)
1.   [Project Planning             ](#1-project-planning)
2.   [Data Acquisition             ](#2-data-acquisition)
3.   [Data Preparation             ](#3-data-preparation)
4.   [Data Exploration             ](#4-data-exploration)
5.   [Modeling & Evaluation        ](#5-modeling--evaluation)
6.   [Product Delivery             ](#6-product-delivery)

E.   [Modules                      ](#e-modules)

F.  [Project Reproduction         ](#f-project-reproduction)


## A. Project Overview
---

### 1. Project Description
We will be using natural language processing (NLP) to see if we can predict a Github repository's most common programming language, based off of its README contents. 
<br>
<br>


### 2. Project Deliverables
 - Acquire, Prepare, and Explore Modules
 - Final Notebook (a walkthrough with comments)
 - Presentation Slides 
 - This README 
<br>
<br>


## B. Project Summary
---

### 1. Goals
Our goal is to be able to succesfully acquire the data, and follow through with the data science pipeline to create a multi-class classification model that will predict primary programming language, based off of the README contents, with a better accuracy than 53% (the baseline accuracy for assuming all results are the most common language type in our dataset.)
<br>
<br>

### 2.) Initial Thoughts & Hypothesis
> - **Hypothesis 1 -** 
> - XXXXXX
> - $H_o$: XXXXX  
> - $H_a$: XXXXX 

> - **Hypothesis 2 -** 
> - alpha = .05
> - $H_o$: 
> - $H_a$: 

XXXXXXXXXXXXXXXXXX
XXXXXXXXXXXXXXTBC


### 3.) Findings & Next Steps

We found that our KNN model, using 10 nearest neighbors, performed the best with a:
 - 87% score on accuracy
 - 87% score on precision
 - 82% score on recall
 
It does well with predicting JavaScript and Python languages, it has a little trouble between Go and Java.
With more time, we should add more repositories to our dataset in order to have it learn off of more contents. 
We believe that this will help it find more distinguishing features between the programming languages. 



## C. Data Context
--- 
### 1. About Our Data

Our data was acquired with web scraping. We scraped ~200 of the most starred repositories on Github with their most dominant programming language used, and their README. We only kept the ones with the top four most common languages from what was pulled: JavaScript, Python, Java, and Go. Since many programming languages acquired only had one repository that used it the most, we decided to drop these as they would not be helpful. Then after dropping duplicates and READMEs with less than 10 words: we ended with 107 repositories to use. 
<br>


### 2. Data Dictionary

| Column Name     | Description                                                         |
|-----------------|---------------------------------------------------------------------|
| repo            | the repository's given name                                         |
| language *      | the repository's most used programming language                     |
| readme_contents | the repository's readme contents                                    |
| original        | the readme contents in its original state (same as readme_contents) |
| clean           | lower cases string, removes special characters, and tokenizes       |
| stemmed         | stems the clean content                                             |
| lemmatized      | lemmatizes the clean content                                        |
| readme_length   | character count of the clean readme length                          |
| word_count      | the number of words in the clean readme contents                    |
 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  * Target variable

<br>
<br>

## D. Pipeline
--- 

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

#### 1. Project Planning
At a quick glance, the following is what needs to be done: 


##### **Plan ->** Acquire -> Prepare -> Explore -> Model -> Deliver
- [x] Create README.md with data dictionary, project and business goals
- [x] Acquire data - Decide on a list of GitHub repositories to scrape, and write the python code necessary to extract the text of the README file for each page, and the primary language of the repository. 
- [x] Clean and prepare data for the first iteration through the pipeline, MVP preparation. Create a function to automate the process, store the function in a prepare.py module, and prepare data in Final Report Notebook by importing and using the funtion(s).
- [x]  Clearly define two hypotheses, set an alpha, run the statistical tests needed, reject or fail to reject the Null Hypothesis, and document findings and takeaways.
- [x] Establish a baseline accuracy and document well.
- [x] Train 5 different models.
- [x] Evaluate models on train and validate datasets.
- [x] Choose the model with that performs the best and evaluate that single model on the test dataset.
- [x] Document conclusions, takeaways, and next steps in the Final Report Notebook.

___



#### 2. Data Acquisition
> - Use webscraping to bring in Github repositories, their READMEs, and information on the most used programming language
> - Save this data locally
> - Store function, in a module, that are needed to acquire the repository and README data from the Github website.
> - The final function will return a pandas DataFrame for our use


#### 3. Data Preparation
> - Clean our data: keep only non-special English characters, tokenize, stem or lemmatize if needed
> - Store functions needed to prepare the Github data
> - Import the prepare functions created by using prepare.py
> - Split the data into train, validate, and test sets


#### 4. Data Exploration
> - Explore the train data that has been scraped.
> - What are the most common words in READMEs?
> - What does the distribution of IDFs look like for the most common words?
> - Does the length of the README vary by programming language?
> - Do different programming languages use a different number of unique words?
> - Visualize! 


#### 5. Modeling & Evaluation
> - Establish a baseline accuracy 
> - Fit using TD-IDF Vectorizer
> - Evaluate decision tree, random forest, logistic regression, KNN, and Naive Bayes models
> - Emphasize on beating the baseline accuracy, and overall accuracy of the model. 


#### 6. Product Delivery
> - Deliver the findings in a Google Slide presentation.
> - Have a completed final notebook with comments to explain the walkthrough of our process
> - Acquire, prepare, and explore .py files completed with docstrings and used in our notebook
> - Completed README for project information (summary, pipeline, findings and next steps, etc.)

<br>
<br>

## E.) Modules
---
- acquire.py = contains data acquisiton functions used to scrape the data, as well as to bring it in from our local server
- prepare.py = contains preparation functions to filter and clean our data
- explore.py = contains explore functions that will generate visualizations 




## F. Project Reproduction
--- 


You will need your own env file with database credentials along with all the necessary files listed below to run our final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and NLP_df.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_nlp.ipynb notebook

