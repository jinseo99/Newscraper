from nltk.cluster.util import cosine_distance
from nltk.corpus import stopwords
import numpy as np
import networkx as nx
import re
import pandas as pd
def read_article(file_name):
    file = open(file_name, "r")
    filedata = file.readlines() 
    article = filedata[0].split(". ")
    sentences = []

    #text_file = open("sentences.txt", "w")

    for sentence in article:
        all_letters = re.sub("[^a-zA-Z0-9]", " ", sentence).split(" ")

        all_letters = list(filter(lambda x: x != '', all_letters))
        #text_file.write(sentence)
        #text_file.write("\n")

        sentences.append(all_letters)
    #text_file.close()

    return sentences

a = True
def sentence_similarity(sent1, sent2, stopwords=None):    
    global a
    if stopwords is None:        
       stopwords = []     
    sent1 = [w.lower() for w in sent1]    


    sent2 = [w.lower() for w in sent2]     

    all_words = list(set(sent1 + sent2))  

    vector1 = [0] * len(all_words)    

    vector2 = [0] * len(all_words)     
    # build the vector for the first sentence   
    for w in sent1:       
        if w in stopwords:            
            continue        
        vector1[all_words.index(w)] += 1   
 
    # build the vector for the second sentence    
    for w in sent2:        
        if w in stopwords:           
            continue        
        vector2[all_words.index(w)] += 1     

    """
    if(a):
        print(vector1)
        print(vector2)
        print(1 - cosine_distance(vector1, vector2))
        a = False
    """
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
    return similarity_matrix

def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('english')
    #print(stop_words)

    summarize_text = []
    # Step 1 - Read text and tokenize
    sentences =  read_article(file_name)

    df = pd.DataFrame(sentences)
    #df.to_csv("sentences.csv")


    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)

    df = pd.DataFrame(sentence_similarity_martix)
    #df.to_csv("matrix.csv")

    
    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentence[i][1]))
        # Step 5 - Offcourse, output the summarize texr
        print("Summarize Text: \n", ". ".join(summarize_text))

generate_summary("article_file.txt", 2)

a = ["hi", "hey"]
b = ["hey","bye","later"]

c = list(set(a+b))
print(c)
