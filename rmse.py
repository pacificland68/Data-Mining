import csv
with open('train_users_2-csv.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    age= [row[5] for row in reader]

    t_age = int(len(age) * 0.8)
    target = age[1:t_age]
    prediction = age[t_age:]

    
    error = []
    for i in range(len(target)):
        if(target[i] != "" and prediction[i] != ""):
            error.append(float(target[i]) - float(prediction[i]))
    
    
    print("Errors: "+error)

