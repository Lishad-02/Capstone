Build Ai agent that iteract with user
Based on user preferece give a career name (ML model based on bagladesh job data)
then AI will give x,y,z.. skills need for this job
then user again say "i have this this skills"
then based on the knowned skills the AI ask him some questions from beg to advanced level 
and assign marks for each quetion based on --
         How close are the ans to the actual ans ( we can do it by traing a dataset-like we make a custom dataset with questions,ques complexity, exact ans,close ans,wrong ans .. and also level marking based on that ans)

this marks will store in the dataset .Example: Hard question: got 2, easy ques: got 8.
And will always fetch this for a particular user when he give ans and always store the latest number. and based on the ans agent will also suggest you need to improve this part like: you need more learn about OOP in java. 

For efficient in a particular skills there would be threshold mark . when user pass it ,agent will say you expert in x. 
when learning all the skills have done, agent will say you are good to go for the job

initially we are doing it for a particular job for the ques,ans ,skill section. but for the first career skill model it will train on multiple job . 



--------------------------------------------------------------------------------------------------------------------
Ai Agent 

                                                                           ↓ 

User Share his/her interested career / his interest through chat 

↓ 

 Based on users chosen career suggest no of skills that need  

(use multi classification model train dataset) 

(And dataset build from international job portal) 

Or  

We can use Bert type model through prompt engineering 
Or 
XGboost + all miniLM L6 V2 (Hybrid)

↓ 

Skill Declaration by User 

Then user will say which skill he/she already has 

↓ 

Start evaluation of skills 

↓ 

Different difficulty level Question Generation (through Prompt Engineering) 

Difficulty will change based on user ans  

↓ 

Take user Answer 

↓ 

Evaluate answers (though prompt engineering technique)  

How much answer is related to actual answer, not just right or wrong evaluation 

↓ 

Give scores for each ques and saved score in Database 

↓ 

Give Feedback why answer is not correct or slightly correct  

(Give explanation) 

↓ 

Suggest Content needs to cover  

↓ 

Again, user test his skill after completing the content 

↓ 

Continue evaluation process  

↓ 

Also give an estimated time based on user's progress  

(Short term forecasting model) 

↓ 

There would be a threshold marks for each skill  

When the user passes the threshold marks for all the skills our agent will suggest “You are ready for this Job” 

**use rag for remembering chat
Project Based Evaluation**