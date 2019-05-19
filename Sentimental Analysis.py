from textblob import TextBlob
from nltk.tokenize import word_tokenize

st=raw_input("Enter a word or sentence : ")
total=0
count=0

#tokenized_sents = [word_tokenize(i) for i in file]
#for i in tokenized_sents:
#        print i

for line in st:

    blob = TextBlob(line)
    blob.tags
    blob.noun_phrases  

    for sentence in blob.sentences:
        pol=float(sentence.sentiment.polarity)
        if pol!=0.0:
            total=total+pol
            count=count+1
value=total/count
print(value)
if value>0.0:
    print("It is a Positive Thinking")
if value<0.0:
    print("It is a Negative Thinking")
if value==0:
    print("not bad")



