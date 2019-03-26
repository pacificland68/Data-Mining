from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import os
import xlsxwriter
import re

path = "E:/HANGE/workplace/text" 
fold = os.listdir(path)
content = [] 
for filename in fold:
    c = ''
    file_path = path+"/"+filename
    file = open(file_path, 'r', encoding='utf-8')
    c += file.read().strip()
    content.append(c)
    
vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(content))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重

print(len(weight))
# for filename in fold:
for i in range(len(weight)):
    t = 0
    # filename = re.sub(r".txt", ".xlsx",filename)
    # filename = re.sub(r"text", "info",filename)
    filepath = "E:/HANGE/workplace/info2/"+str(i)+".xlsx"
    workbook = xlsxwriter.Workbook(filepath)
    worksheet = workbook.add_worksheet()

    for j in range(len(word)):
        # print word[j],weight[i][j]
        worksheet.write(t,0,word[j])
        worksheet.write(t,1,weight[i][j])
        t += int(1)
    workbook.close()

    


    
# print(len(word))
# print(tfidf.toarray().size)