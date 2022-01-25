from django.http import HttpResponse
from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib,base64
import csv
import os
import pandas as pd
import numpy as np
from sklearn import linear_model
global_pred=[]
def spark(request):
    return render(request, 'spark.html', )
def index(request):
    state_name=0
    year=0
    state_name = request.POST.get('state')
    category=request.POST.get('category')
    a=1
    if((state_name is None) or (category is None)):
        state_name=0
        category=0
    uri=0
    uri_pred=0
    

    a=(int(state_name))
    category=int(category)
    if(category==7):
        x=[]
        y=[]
        name=['Andaman Nicobar','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhatisgarh','Dadra & Nagar Haveli','Daman & Diu',
        'Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra',
        'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh',
        'Uttarakhand','West Bengal']
        i=1
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'rape.csv')
        with open(file_path,'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                x.append(row[1])
                y.append((row[a+3*(a+1)]))
                        
        f = plt.figure()
        f.set_figwidth(25)
        f.set_figheight(10)


        plt.plot(x, y, color = 'r', linestyle = 'solid',
        marker = 'o',label = "Crime Data")

        plt.xticks(rotation = 25)
        plt.xlabel('Year')
        plt.ylabel('Number of Cases')
        plt.title(f'Rape Cases in {name[a]} 2001-2010', fontsize = 35)
        plt.grid()
        plt.legend()
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string=base64.b64encode(buf.read())
        uri=urllib.parse.quote(string)
    elif(category==1):
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'corruption.csv')
        x = []
        y = []
        i=3
        j=0
        name=['Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Dadra & Nagar Haveli','Daman & Diu',
            'Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra',
            'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh',
            'Uttarakhand','West Bengal']

        a=int(state_name)
        with open(file_path,'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                if row[0]==name[a]:
                    x.append(row[1])
                    y.append(int(row[2]))

        f = plt.figure()
        f.set_figwidth(25)
        f.set_figheight(10)


        plt.plot(x, y, color = 'r', linestyle = 'dashed',
                    marker = 'o',label = "Crime Data")

        plt.xticks(rotation = 25)
        plt.xlabel('Year')
        plt.ylabel('Number of Cases')
        plt.title(f'Corruption Cases in {name[a]} 2001-2010', fontsize = 35)
        plt.grid()
        plt.legend()
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string=base64.b64encode(buf.read())
        uri=urllib.parse.quote(string)
    elif(category==5):
        x = []
        y = []
        i=3
        j=0
        name=['Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhatisgarh','Dadra & Nagar Haveli','Daman & Diu',
            'Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra',
            'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh',
            'Uttarakhand','West Bengal']

        a=int(state_name)
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'property.csv')
        with open(file_path,'r') as csvfile:
            lines = csv.reader(csvfile, delimiter=',')
            for row in lines:
                if row[0]==name[a]:
                    x.append(row[1])
                    y.append(int(row[2]))

        f = plt.figure()
        f.set_figwidth(25)
        f.set_figheight(10)


        plt.plot(x, y, color = 'r', linestyle = 'dashed',
                        marker = 'o',label = "Crime Data")

        plt.xticks(rotation = 25)
        plt.xlabel('Year')
        plt.ylabel('Number of Cases')
        plt.title(f'Property Dispute Cases in {name[a]} 2001-2010', fontsize = 35)
        plt.grid()
        plt.legend()
        fig=plt.gcf()
        buf=io.BytesIO()
        fig.savefig(buf,format='png')
        buf.seek(0)
        string=base64.b64encode(buf.read())
        uri=urllib.parse.quote(string)
# prediction begins here 


    state_pred=request.POST.get('state_pred')
    pred_year=request.POST.get('year_pred')
    pred_category=request.POST.get('category_pred')

    if((pred_category is None) or (state_pred is None) or (pred_year is None)):
        state_pred=0
        pred_year=0
        pred_category=0
    
    x = []
    y = []
    i=3
    j=0
    name=['Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhatisgarh','Dadra & Nagar Haveli','Daman & Diu',
        'Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra',
        'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh',
        'Uttarakhand','West Bengal']

    a=int(state_pred)
    yr=int(pred_year)
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'property.csv')
    with open(file_path,'r') as csvfile:
        lines = csv.reader(csvfile, delimiter=',')
        for row in lines:
            if row[0]==name[a]:
                x.append(int(row[1]))
                y.append(int(row[2]))

                
    year=pd.DataFrame(x)
    cases=pd.DataFrame(y)            


    f = plt.figure()
    f.set_figwidth(15)
    f.set_figheight(10)

    lm=linear_model.LinearRegression()
    model = lm.fit(year,cases)
    model.coef_
    model.intercept_
    model.score(year,cases)
    year_new=np.array([[yr]])

    cases_pred=model.predict(year_new)
    val=np.array(cases_pred)
    global_pred.append(val)
    print(global_pred[len(global_pred)-1])
    print(val)
    print(yr)
    if(yr == 0):
        val=0

    
        
    plt.title(f"Predicted value of Property Cases in {name[a]} in {yr} year")
    plt.legend(["Tested Cases", "Predicted Cases"])
    plt.xlabel("Year")
    plt.ylabel("Number of Cases")
    plt.scatter(year,cases,color='blue')
    plt.scatter(year_new,cases_pred,color='black',marker='d',label='predicted value')
    fig=plt.gcf()
    buf=io.BytesIO()
    fig.savefig(buf,format='png')
    buf.seek(0)
    string=base64.b64encode(buf.read())
    uri_pred=urllib.parse.quote(string)

        
    eid = request.POST.get('email')
    if(eid is not None):
        newval=val
        print("new : ",newval)
        print(name[state_pred])
        send_mail(eid,state_pred,newval)
    if(int(val)<0):
        val=0
    return render(request, 'index.html',{'data':uri,'pred_graph':uri_pred,'predicted':int(val)})
def send_mail(eid,state_pred,val):
    import smtplib
    name=['Andaman & Nicobar Islands','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhatisgarh','Dadra & Nagar Haveli','Daman & Diu',
        'Delhi','Goa','Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir','Jharkhand','Karnataka','Kerala','Lakshadweep','Madhya Pradesh','Maharashtra',
        'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab','Rajasthan','Sikkim','Tamil Nadu','Tripura','Uttar Pradesh',
        'Uttarakhand','West Bengal']
    server=smtplib.SMTP_SSL("smtp.gmail.com",465)
    server.login("mohdareeb.1224@gmail.com","zaidrayyan1224areeb")
    i=eid.index('@')
    name=eid[0:i]
    res=global_pred[len(global_pred)-1]
    msg="Hello " +name + ", the predicted cases are " + "1221"
    server.sendmail("mohdareeb.1224@gmail.com",eid,msg)
    quit

    