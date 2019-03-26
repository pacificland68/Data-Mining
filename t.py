import os
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import xlwt
import re
from textblob import TextBlob
import xlsxwriter
import math

stop_words = set(stopwords.words('english')) 

def count_words(text):
    count = 0
    # words = TextBlob(text)
    # words = words.noun_phrases
    words = word_tokenize(text)
    for word in words:
            if word not in stop_words:
                count +=1
    return count

def create_freq_dict(text,o):
    freq_dict = {}
    # words = TextBlob(text)
    # words = words.noun_phrases
    words = word_tokenize(text)
    for word in words:
        if word not in stop_words:
            word = word.lower()
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1
            temp = {'doc_id':o, 'freq_dict': freq_dict}
    # for c in freq_dict:
    #     print(c)
    # for c in freDict_list:
    #     print(freDict_list[0])
    return freq_dict


def data_write(file_path, datas):
    workbook = xlsxwriter.Workbook(file_path)
    worksheet = workbook.add_worksheet()
    i = 0
    ii = 0
    for data in datas:
        for t in data['tf_scores']:
            worksheet.write(i,0,t)
            worksheet.write(i,1,data['tf_scores'][t])
            i += int(1)
        for t in data['idf_scores']:
            worksheet.write(ii,2,data['idf_scores'][t])
            ii += int(1)
    workbook.close()

def tf_idf(doc_info, count):
    print("tfidf")
    tf_idf = []
    for d in doc_info:
        d = d.lower()
        tf_scores = {}
        idf_scores = {}
        tf = int(doc_info[d]) / count
        tf_scores[d] = tf

        path = "E:/HANGE/workplace/text"
        fold = os.listdir(path)
        i = 0
        for filename in fold:
            file_path = path+"/"+filename
            file = open(file_path, 'r', encoding='utf-8')
            content = file.read().strip()
            content = content.lower()
            if d in content:#you need to use harsh
                i += int(1)
        idf_scores[d] = math.log(24 / i)
        temp = {'tf_scores': tf_scores, 'idf_scores': idf_scores}
        tf_idf.append(temp)
        # for c in tf_idf:
        #    for cc in c['tf_scores']:
        #        print(c['tf_scores'][cc])#value of tf_scores
    return tf_idf


path = "E:/HANGE/workplace/text" 
fold = os.listdir(path)
i = 0
for filename in fold:
    print(i)
    i += int(1)
    file_path = path+"/"+filename
    file = open(file_path, 'r', encoding='utf-8')
    content = file.read().strip()
    count = count_words(content)
    print('!')
    doc_info = create_freq_dict(content,i)
    print('!!')
    tfidf = tf_idf(doc_info, count)
    filename = re.sub(r".txt", ".xlsx",filename)
    data_write("E:/HANGE/workplace/info/info_"+filename, tfidf)