![image](https://github.com/lupeluna/README_FILES/blob/main/NLP%20Project%20Predicting%20READMEs-3.gif)

This Repository will be used for our Natural Language Processing Project

by: Forrest McCrosky, Lupe Luna, Anna Vu

Hello,

Welcome to the README file for our "NLP Project"

Here, you will find our work on the NLP_df.csv file which contains Github repos that include the README contents.  You will also find the data dictionary to help offer more insight to the variables being used.  

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
> - $H_o$: There is no association between conductivity and potability.
> - $H_a$: There is an association between conductivity and potability.


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

### Reproduce My Project

<hr style="border-top: 10px groove blueviolet; margin-top: 1px; margin-bottom: 1px"></hr>

You will need your own env file with database credentials along with all the necessary files listed below to run my final project notebook. 
- [X] Read this README.md
- [ ] Download the aquire.py, prepare.py, and NLP_df.ipynb files into your working directory
- [ ] Add your own env file to your directory. (user, password, host)
- [ ] Run the final_nlp.ipynb notebook
