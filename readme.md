![image](https://github.com/lupeluna/README_FILES/blob/main/NLP%20Project%20Predicting%20READMEs-3.gif)


by: Forrest McCrosky, Lupe Luna, Anna Vu

Hello,

Welcome to the README file for our [NLP Project](https://nbviewer.jupyter.org/github/Vu-Luna-McCrosky-NLP-Project/NLP_Project_Predicting_Readme_s/blob/master/final_nlp.ipynb) 

Here, you will find our work on the NLP_df.csv file which contains Github repos that include the README contents.  You will also find the data dictionary to help offer more insight to the variables being used.
<br>

## Table of Contents
---

A.   [Project Overview             ](#a-project-overview)
1.   [Project Description          ](#1-project-description)
2.   [Project Deliverables         ](#2-project-deliverables)

B.  [Project Summary               ](#b-project-summary)
1.   [Goals                        ](#1-goals)
2.   [Initial Thoughts & Hypothesis](#2-hypothesis)
3.   [Findings & Next Steps        ](#3-findings--next-steps)

C. [Data Context                 ](#c-data-context)
1.   [About the Pokedex Data        ](#1-about-the-pokedex-data)
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
_______________________

## Abstract

XXXXXXXXXXXXXXXXXX


_______________________

## GOAL:

Our goal is to build a model that can predict what programming language a respoitory is, given the text of the README file.

______________________



## Planning process

Below you will see the TRELLO pipleline we used which can also be found in this link: [Trello](https://trello.com/b/DlD8CmLW/nlp-project)



___________________________

-  Please use this data dictionary as a reference for the variables used within in the data set.



|   Feature      |  Data Type   | Description    |
| :------------- | :----------: | -----------: |
| XXXXX | XXXXX   | XXXXX    |
| XXXXX | XXXXX   | XXXXX    |
| XXXXX | XXXXX   | XXXXX    |
| XXXXX | XXXXX   | XXXXX    |


-------------------
 
 
#### Initial Hypotheses

> - **Hypothesis 1 -** 
> - XXXXXX
> - $H_o$: XXXXX  
> - $H_a$: XXXXX 

> - **Hypothesis 2 -** 
> - alpha = .05
> - $H_o$: 
> - $H_a$: 


<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Conclusions & Next Steps
<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

> - Recommendations & next steps:

 * XXXXX
 * With more time, we would XXXXX



<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Pipeline Stages Breakdown

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

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

#### Acquire
> - Store functions that are needed to acquire the repository and README data from the Github website.
> - The final function will return a pandas DataFrame


#### Prepare
> - Store functions needed to prepare the Github data
> - Import the prepare functions created by using prepare.py


#### Explore
> - Explore the data that has been scraped.
> - What are the most common words in READMEs?
> - What does the distribution of IDFs look like for the most common words?
> - Does the length of the README vary by programming language?
> - Do different programming languages use a different number of unique words?


#### Model
> - Establish a baseline accuracy and try fitting several different models using TF-IDF values for each.

#### Deliver
> - Deliver the findings in a Google Slide presention.



<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

### Data Dictionary

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

### Reproduce Our Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run our final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and NLP_df.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_nlp.ipynb notebook

