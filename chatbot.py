# Building a chatbot with Deep NLP

# import the libraries
import numpy as np
import tensorflow as tf
import re 
import time

#### part 1 - data processsing ####

#import the dataset
lines = open('movie_lines.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')
conversations = open('movie_conversations.txt', encoding = 'utf-8', errors = 'ignore').read().split('\n')