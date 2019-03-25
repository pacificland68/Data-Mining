import os
from bs4 import BeautifulSoup
import re

path = "E:/HANGE/workplace/gap-html" 
fold= os.listdir(path)
for file_fold in fold: #get into fold: gap....
    content = ''
    fold_path = path+"/"+file_fold
    fold = os.listdir(fold_path)
    print(file_fold)
    for file in fold: #get html files
        file_path = fold_path+"/"+file
        f = open(file_path, 'r', encoding='utf-8')
        htmlhandle = f.read()
        soup = BeautifulSoup(htmlhandle, 'lxml')
        ct = soup.findAll("span",{"class":"ocr_cinfo"})
        for c in ct:
            content += re.sub(r"[^a-zA-Z ]", "",c.get_text()) + " "
    with open(file_fold+".txt","w") as f:
        for i in content:
            f.write(i)   
        # print(content)
        # for c in content:
        #     # print(c.get_text())
        #     c += re.sub(r"[^a-zA-Z ]", "", str(c.get_text()))
    # print(c)
        