import math
from nltk import sent_tokenize, word_tokenize, PorterStemmer
from nltk.corpus import stopwords

# computing IDF and TF

#tags = tags_tokenize(tags_from_db) 

#mood_descriptors = ["sad", "happy", "weird"]

# we can create lists from synonyms
mood_descriptors = {
                    "happy" : ["happy", "exciting"],
                    "sad" : ["sad", "depressing"]
                    }
tags = ["hello world, sad, depressing, happiness ", "I don't have friends, happy,exciting,happy,exciting weird,sad", "it is what it is, depressing."]

#we have to count total number of
#every mood descriptor in every tag

def create_frequency_matrix(tags):
    frequency_matrix = []
    stop_words = set(stopwords.words("english"))
    ps = PorterStemmer() # sityva dayavs fudzeze

    for tag in tags:
        freq_table = {}
        words = word_tokenize(tag) #tag-i davanawilot sityvebad
        for word in words:
            word = word.lower()
            word = ps.stem(word) # turn happyness and happy in stem happi
            
            if word in stop_words:
                continue
            for mood_descriptor, sub_moods in mood_descriptors.items(): 
                for sub_mood in sub_moods:
                    sub_mood = ps.stem(sub_mood)
                    if word == sub_mood:
         
                        if mood_descriptor in freq_table:
                            freq_table[mood_descriptor] +=1
                        else:
                            freq_table[mood_descriptor] = 1
                    #garcheva ro shevdzlo
        frequency_matrix.append(freq_table)

    return frequency_matrix

def create_tf_matrix(freq_matrix):
    tf_matrix = []

    for f_table in freq_matrix:
        tf_table = {}

        #this part should be optimized
        #looks ugly
        count_words_in_tag = 0
        for mood,count in f_table.items():
            count_words_in_tag += count
            
        for mood, count in f_table.items():
            tf_table[mood] = count / count_words_in_tag

        tf_matrix.append(tf_table)

    return tf_matrix

print("These are frequencies:\n")
print (create_frequency_matrix(tags))
print("\nThis are tf-s\n")
print (create_tf_matrix(create_frequency_matrix(tags)))




