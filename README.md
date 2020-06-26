# Dialogue system (Chatbot) with a personality
In this Project, I have explored a dialogue system (Building a chatbot) with 3 different
Datasets.
1. Cornell Movie Dialogues
2. QA Dataset
3. SQUAD (Stanford Question Answering Dataset) [Incomplete]

I have trained the chatbot both individually and combined to compare the performance of
the chatbot. Due to memory restrictions and time constraints, I was only able to train the
Cornell Movie dialogue dataset for 30000 iterations and QA dataset up to 2
600 iterations,

but as I have got a pretty significant improvement for loss of QA dataset, So I have stopped
training the chatbot any further.

For the 3rd dataset, I was not able to train the chatbot due to some errors, Still, I have
described the process and attached the code for performed for SQUAD Dataset.
For the second improvement, I have created a chatbot with the personality of Barney
Stinson by adding his signature character traits and dialogues in the initial greeting and
some extent of questions.

I have tested Initial and improved chatting experience 3 times (6 times in total) which can
be checked in output_convo.txt.
Overall, we have noticed a significant improvement in chatting experience when trained
with both the datasets when compared to individual ones even though the QA dataset
individually provided a noticeable improvement in the loss.


There are 7 files present in the repository : 
1. Data folder - Contains Datasets used in the experiments
2. model.py - Contains specification of the model.
3. data.py - Contains script to do all the data-related tasks, to make data ready for training.
4. config.py - Contains configuration hyperparameters for the model.
5. chatbot.py -  Contains Driver code to train or to chat with your chatbot.  
6. Report.pdf - Contains report of findings and description of improvement performed for the project.
7. output_convo.txt - Contains chat logs of the experiments performed.


Changes for Datasets  :

1. Change in Config file - Variables for dataset paths and file names
2. Change in Data file - in Main function get_QA_Dataset2() instead of prepare_raw_data()
Rest of the changes are inline.

Execution : 
python3 chatbot.py --mode chat


