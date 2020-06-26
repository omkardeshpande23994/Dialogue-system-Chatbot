""" A neural chatbot using sequence to sequence model with
attentional decoder. 
This is based on Google Translate Tensorflow model 
https://github.com/tensorflow/models/blob/master/tutorials/rnn/translate/
Sequence to sequence model by Cho et al.(2014)
Created by Chip Huyen (chiphuyen@cs.stanford.edu)
This file contains the hyperparameters for the model.
See README.md for instruction on how to run the starter code.
"""

# parameters for processing the dataset
DATA_PATH = "data/cornell_movie_dialogs_corpus/"
CONVO_FILE = "movie_conversations.txt"
LINE_FILE = "movie_lines.txt"

DATA_PATH2 = "data/Dataset2_QA/"
DATASET2_FILE1 = "S08_question_answer_pairs.csv"
DATASET2_FILE2 = "S09_question_answer_pairs.csv"
DATASET2_FILE3 = "S10_question_answer_pairs.csv"

# DATA_PATH3 = "data/SQUAD/"
# DATASET3_FILE = "Data.csv"

OUTPUT_FILE = "output_convo.txt"
PROCESSED_PATH = "processed"
CPT_PATH = "checkpoints"

THRESHOLD = 2

PAD_ID = 0
UNK_ID = 1
START_ID = 2
EOS_ID = 3

TESTSET_SIZE = 15000
TESTSET_SIZE_D2 = 500

BUCKETS = [(19, 19), (28, 28), (33, 33), (40, 43), (50, 53), (60, 63)]


CONTRACTIONS = [
    ("i ' m ", "i 'm "),
    ("' d ", "'d "),
    ("' s ", "'s "),
    ("don ' t ", "do n't "),
    ("didn ' t ", "did n't "),
    ("doesn ' t ", "does n't "),
    ("can ' t ", "ca n't "),
    ("shouldn ' t ", "should n't "),
    ("wouldn ' t ", "would n't "),
    ("' ve ", "'ve "),
    ("' re ", "'re "),
    ("in ' ", "in' "),
]

NUM_LAYERS = 3
HIDDEN_SIZE = 256
BATCH_SIZE = 64

LR = 0.5
MAX_GRAD_NORM = 5.0

NUM_SAMPLES = 512
ENC_VOCAB = 24405
DEC_VOCAB = 24569
ENC_VOCAB = 24965
DEC_VOCAB = 25207
ENC_VOCAB = 5147
DEC_VOCAB = 5121
ENC_VOCAB = 2150
DEC_VOCAB = 1546
ENC_VOCAB = 2112
DEC_VOCAB = 1436
