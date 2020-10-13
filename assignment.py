import nltk
from nltk.tokenize import sent_tokenize

#dependencies : nltk

import regex as re
global new_dataset
new_dataset = []
'''
This project is intent to analyze the data set which classify the type of question 
based on NPL,it will show classification 
'''

# Below subroutine take the input from desired path and split the contents
#params : psth
def input(psth):
    f = open(path,"r")
    constent = f.read()
    tokenize_constent = sent_tokenize(constent)
    for x in tokenize_constent:
        y = re.split("\s", x, 1)
        del y[0]
        new_dataset.append(y)
    f.close()


# Below subroutine will analyze the data set which classify the type of question
# based on NPL,it will show classification


def analyzeDataSet():
    for dataset in  new_dataset:
        for data in dataset:
            #text = "would"
            word = nltk.word_tokenize(data)
            token = nltk.pos_tag(word)
            # print(token)
            w = word[0].lower()
            if token[0][1] == "WP":
                if w == "who":
                    print(data + " ,,, " + w)
                elif w == "what":
                    if w == "what" and token[1][1] == "NN":
                        print(data + " ,,, when")
                    else:
                        print(data + " ,,, " + w)
                else:
                    continue
            elif token[0][1] == "WRB":
                if w == "when":
                    print(data + " ,,, " + w)
                else:
                    print(data + " ,,, Unknown")
            elif (token[0][1] == "MD") or (token[0][1] == "VB") or (token[0][1] == "VBD") or (token[0][1] == "VBZ") or (token[0][1] == "VBN") or (token[0][1] == "VBP") or (token[0][1] == "VBG"):
                print(data + " ,,, Affirmation")
            else:
                print(data + " ,,, Unknown")

if __name__ == "__main__":
    path = "C://Users//lenovo//Desktop//dataset.txt"
    print("This progrsm is using classify the question of what type")
    print("Enter the sepicific file path of the Data set : " + path)
    input(path)
    analyzeDataSet()
