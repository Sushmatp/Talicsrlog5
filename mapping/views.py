from django.shortcuts import render
from rlogdata.models import *
from django.shortcuts import render, redirect
from records.forms import Staging_form
from django.http import HttpResponse
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import os
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.shortcuts import get_object_or_404
import json
from datetime import datetime,date
from pprint import pprint
from django.forms.models import model_to_dict
from django_pandas.io import read_frame
import re



# Create your views here.
CSV_STORAGE = os.path.join(os.getcwd(), 'static', 'csv')


def choose(request):
    if request.method == 'POST':
        if request.POST.get('checkBox') == None:
            return redirect('/import')

        return redirect('/import_p')
    else:
        return render(request, 'choose.html')


@csrf_exempt
def import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/fieldmatching?df=' + path_name)
    else:
        return render(request, 'import_data.html')


def fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Staging._meta.get_fields()]
        #df = df.transform(lambda x: x.fillna('TNone') if x.dtype == 'object' else x.fillna(0))
        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in fields}
            x = list(matched.keys())
            y = list(matched.values())
            dict = {}
            for key in y:
                for value in x:
                    dict[key] = value
                    print(dict)
                    x.remove(value)
                    break
            df.rename(columns=dict, inplace=True)
        # df.drop('id', axis=1, inplace=True)
        # df.set_index("id", drop=True, inplace=True)
        df = df.fillna('')
        print(df)
        dic={}

        # status validation start
        for index, row in df.iterrows():
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=1).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=1).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=1).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=1).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=2).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=2).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=2).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=2).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=3).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=3).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=3).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=3).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=4).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=4).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=4).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=4).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=5).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=5).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=5).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=5).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=6).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=6).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=6).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=6).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=7).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=7).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=7).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=7).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=8).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=8).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=8).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=8).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=9).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=9).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=9).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=9).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=10).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=10).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=10).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=10).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=11).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=11).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=11).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=11).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=12).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=12).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=12).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=12).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=13).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=13).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=13).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=13).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=14).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=14).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=14).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=14).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=15).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=15).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=15).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=15).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=16).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=16).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=16).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=16).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=17).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=17).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=17).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=17).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=18).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=18).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=18).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=18).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=19).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=19).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=19).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=19).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=20).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=20).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=20).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=20).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=21).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=21).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=21).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=21).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=22).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=22).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=22).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=22).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=23).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=23).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=23).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=23).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=24).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=24).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=24).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=24).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=25).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=25).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=25).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=25).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=26).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=26).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=26).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=26).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=27).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=27).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=27).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=27).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=28).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=28).StageID
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=28).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=28).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=29).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=29).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=29).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=29).StageName
                continue
            if row['current_status'] == '' and row['current_status_desc'] == CandidateStatus.objects.only('StageName').get(pk=30).StageName:
                df.at[index,'current_status']= CandidateStatus.objects.only('StageID').get(pk=30).StageID 
            elif row['current_status'] == CandidateStatus.objects.only('StageID').get(pk=30).StageID and row['current_status_desc']== '':
                df.at[index,'current_status_desc']= CandidateStatus.objects.only('StageName').get(pk=30).StageName
                continue

        print(df)
        # status validationn ends

        # date validation start 
        for index, row in df.iterrows():
            if row['reqt_date']== '' or row['date_cv_submitted']== '' or row['interview_date'] == '':       
                    row = df.loc[index]
                    a = index 
                    bad_dictionary = row.to_dict()
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
        print(df)
        # date validaiton ends

        # status with date validation starts
        for index, row in df.iterrows():
            if row['current_status'] == 104 or row['current_status'] == 4: # Telecon_Interview and tele_reject
                if row['Int_Tele_Date']== '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    print(bad_dictionary)
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
            if row['current_status'] == 105 or row['current_status'] == 5: # f2f_interview and reject
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    print(bad_dictionary)
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
                
            if row['current_status'] ==  106 or row['current_status'] ==  6: #'F2F Int 2 Reject' and reject
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
            #if row['current_status'] == ''  #'F2F int 3 Reject'
             #   if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date'] == '':
              #      row = df.loc[index]
               #     a = index
                #    bad_dictionary = row.to_dict()
                 #   bad_dictionary['reason'] = 'The dates are missing'
                  #  dic[a] = bad_dictionary
                   # df = df.drop(index)
                    #print(a)

            if row['current_status'] == 107 or row['current_status'] == 7: #'Final Int Reject' and reject
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date'] == '' or row['Int_Final_Date'] == '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
            if row['current_status'] == 108 or row['current_status'] == 8: #'HR Reject' and hr interview
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date']== '' or row['Int_Final_Date'] == '' or row['Int_HR_Date'] == '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
            if row['current_status'] == 111 or row['current_status'] == 11: #'Offer Declined' and declined
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date'] == '' or row['Int_Final_Date'] == '' or row['Int_HR_Date'] == '' or row['offer_date']=='':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
            if row['current_status'] == 109 or row['current_status'] == 9: #'Candidate lost interest' and candidate awaited
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date'] == '' or row['Int_Final_Date'] == '' or row['Int_HR_Date'] == '' or row['offer_date']=='':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    
                    
                print(df)
            if row['current_status'] == 114 or row['current_status'] == 14: #'Did not Join' and joined
                if row['Int_Tele_Date']== '' or row['Int_p1_Date'] == '' or row['Int_p2_Date'] == '' or row['Int_p3_Date'] == '' or row['Int_Final_Date'] == '' or row['Int_HR_Date'] == '' or row['offer_date']=='' or row['joining_date'] == '':
                    row = df.loc[index]
                    a = index
                    bad_dictionary = row.to_dict()
                    bad_dictionary['reason'] = 'The dates are missing'
                    dic[a] = bad_dictionary
                    df = df.drop(index)
                    print(a)
                    
                print(df)
            

        print(df)
        # date with status validation ends

        # for saving the bad records
        for index, object in dic.items():
            m = BadRecords()
            for k, v in object.items():
                setattr(m, k, v)
            setattr(m, 'id', index)
            m.save()
         
        # converstion to date tiem format   
        df['reqt_date']= pd.to_datetime(df['reqt_date'])
        df['date_cv_submitted']= pd.to_datetime(df['date_cv_submitted'])
                      
        if 'wk_year' not in names:
            df['wk_year'] = df['date_cv_submitted'].dt.year
        if 'week_number' not in names:
            df['week_number'] = df['date_cv_submitted'].dt.week
                    
                                                     
        df['interview_date']= pd.to_datetime(df['interview_date'])
            #df[['interview_date']] = df[['reqt_date']].fillna('')

        df['Int_Tele_Date']= pd.to_datetime(df['Int_Tele_Date'])
        df['Int_p1_Date']= pd.to_datetime(df['Int_p1_Date'])
        df['Int_p2_Date']= pd.to_datetime(df['Int_p2_Date'])
        df['Int_p3_Date']= pd.to_datetime(df['Int_p3_Date'])
        df['Int_Final_Date']= pd.to_datetime(df['Int_Final_Date'])
        df['Int_HR_Date']= pd.to_datetime(df['Int_HR_Date'])
        df['offer_date']= pd.to_datetime(df['offer_date'])
        df['joining_date']= pd.to_datetime(df['joining_date'])
        

        if 'DOB' in list(df.columns):
            #df['DOB'].replace({'None': ''}, inplace=True)                                       
            df['DOB']= pd.to_datetime(df['DOB'])
            #df[['DOB']] = df[['reqt_date']].fillna('')
            if 'month_of_birth' not in list(df.columns):
                df['month_of_birth'] = df['DOB'].dt.month
            if 'year_of_birth'  not in list(df.columns):
                df['year_of_birth'] = df['DOB'].dt.year
            #df.fillna('')
                                    
        print(df)
        print(df.dtypes)
        print(dic.keys())
        #df['Int_p1_Date'].fillna('1998-11-28', inplace = True)
        #df = df.transform(lambda x: x.fillna('TNone') if x.dtype == 'datetime' else pass)
        #Null = None
        #print(Null)
        
        df = df.replace({pd.NaT: None}) # allow null values
        print(df)

        # whole validation ends

        dictionary = df.to_dict(orient="index")
        #dictionary[0]['Int_p1_Date'] = None
        print(dictionary.keys())
        
        Mapping.objects.create(MappingFor='Staging', Mappings=dict)
        #print(Mapping.objects.all()[0].Mappings)
        save_dict(dictionary)
        return render(request, 'import_data.html')
    
    else:
        path_name = request.GET.get('df')
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Staging._meta.get_fields()]

        return render(request, 'fieldmatching.html',
                    {'fields': fields, 'path_name': path_name, 'names': names})


def save_dict(dictionary):
    for index, object in dictionary.items():
        m = Staging()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', index)
        m.save()


def save_dict_call(dictionary, q):
    for index, object in dictionary.items():
        m = Staging()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', q)
        q = q + 1;
        m.save()


def import_data_p(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        df = pd.read_csv(path_name)
        df = df.transform(lambda x: x.fillna('None') if x.dtype == 'object' else x.fillna(0))
        # declare store dictionary i.e we want dict
        p = Mapping.objects.order_by('-id').filter(MappingFor = 'Staging')[0].Mappings
        print(p)
        dict = {}
        #print(dict)
        if not bool(p):
            print("No Previous Matching Columns Found")
            return redirect('/choose')
        else:
            df.rename(columns=p, inplace=True)
            engine = create_engine('postgresql://postgres:password123@1@localhost:5432/rlog')
            #df.to_sql(name='Staging', con=engine, if_exists='append', index=False)
            q = Staging.objects.count()
            print(q)
            #q = q + 1
            # df.set_index('id', drop=True, inplace=True)
            dictionary = df.to_dict(orient="index")
            save_dict_call(dictionary, q)
            print("columns found")
        # save_dict(dictionary)
        return render(request, 'import_data.html')
    else:
        return render(request, 'import_data.html')






def mandate_choose(request):
    if request.method == 'POST':
        if request.POST.get('checkBox') == None:
            return redirect('/mandate_import')

        return redirect('/mandate_import_p')
    else:
        return render(request, 'mandate-choose.html')


@csrf_exempt
def mandate_import_data(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        return redirect('/mandate_fieldmatching?df=' + path_name)
    else:
        return render(request, 'mandate-import_data.html')

def mandate_fieldmatching(request):
    if request.method == 'POST':
        path_name = request.POST['path_name']
        df = pd.read_csv(path_name)
        names = list(df.columns)
        fields = [field.name for field in Mandates._meta.get_fields()]
        df = df.transform(lambda x: x.fillna('TNone') if x.dtype == 'object' else x.fillna(0))
        if request.POST.get('checkBox') == None:
            matched = {key: request.POST.get(key, False) for key in fields}
            x = list(matched.keys())
            y = list(matched.values())
            dict = {}
            for key in y:
                for value in x:
                    dict[key] = value
                    print(dict)
                    x.remove(value)
                    break
            df.rename(columns=dict, inplace=True)


        dictionary = df.to_dict(orient="index")
        Mapping.objects.create(MappingFor='Mandates', Mappings=dict)
        print(Mapping.objects.all()[0].Mappings)
        mandate_save_dict(dictionary)
        return render(request, 'mandate-import_data.html')
    else:
            path_name = request.GET.get('df')
            df = pd.read_csv(path_name)
            names = list(df.columns)
            fields = [field.name for field in Mandates._meta.get_fields()]
    
            
            return render(request, 'mandate-fieldmatching.html',
                      {'fields': fields, 'path_name': path_name, 'names': names})

def mandate_save_dict(dictionary):
    for index, object in dictionary.items():
        m = Mandates()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', index)
        m.save()


def mandate_save_dict_call(dictionary, q):
    for index, object in dictionary.items():
        m = Mandates()
        for k, v in object.items():
            setattr(m, k, v)
        setattr(m, 'id', q)
        q = q + 1;
        m.save()


def mandate_import_data_p(request):
    if request.method == 'POST':
        new_students = request.FILES['myfile']
        if new_students.content_type == 'text/csv':
            df = pd.read_csv(new_students)
        else:
            df = pd.read_excel(new_students)  # make sure that there' no header
        path_name = os.path.join('static', 'tempcsv', 'temp.csv')
        df.to_csv(path_name, index=False)
        df = pd.read_csv(path_name)
        df = df.transform(lambda x: x.fillna('None') if x.dtype == 'object' else x.fillna(0))
        # declare store dictionary i.e we want dict
        p = Mapping.objects.order_by('-id').filter(MappingFor = 'Mandates')[0].Mappings
        print(p)
        dict = {}
        #print(dict)
        if not bool(p):
            print("No Previous Matching Columns Found")
            return redirect('/mandate_choose')
        else:
            df.rename(columns=p, inplace=True)
            engine = create_engine('postgresql://postgres:password123@1@localhost:5432/rlog')
            #df.to_sql(name='Mandate', con=engine, if_exists='append', index=False)
            q = Mandates.objects.count()
            print(q)
            #q = q + 1
            # df.set_index('id', drop=True, inplace=True)
            dictionary = df.to_dict(orient="index")
            mandate_save_dict_call(dictionary, q)
            print("columns found")
        # save_dict(dictionary)
        return render(request, 'mandate-import_data.html')
    else:
        q = Mapping.objects.order_by('-id').filter(MappingFor = 'Staging')[0].Mappings
        print(q)
        p = Mapping.objects.order_by('-id').filter(MappingFor = 'Mandates')[0].Mappings
        print(p)
        return render(request, 'mandate-import_data.html')

'''def index2(request):

    df = read_frame(Staging.objects.all())
    #good = read_frame(GoodRecords.objects.all())
    #bad = read_frame(BadRecords.objects.all())
    df = df.astype(str)
    token = []
    bad = pd.DataFrame()
    good = pd.DataFrame()
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

    for index, row in df.iterrows():
        dict = {}

        # reqt_date = datetime.strptime(row['reqt_date'], "%Y-%m-%d").date()
        # print(reqt_date)
        # if datetime.strptime(row['date_cv_submitted'], "%Y-%m-%d").date() < reqt_date:
        #     dict['date_cv_submitted'] = 'Should be after reqt date'
        #     row['reason'] = dict

        if row['recruiter'] not in User.objects.values_list('FullName', flat = True):
            dict['recruiter'] = 'Not in the List'

        if row['client'] not in Client.objects.values_list('ClientName', flat = True):
            dict['client'] = 'Not in the List'

        if row['vacancy_code'] not in Mandates.objects.values_list('VacancyCode', flat = True):
            dict['vacancy_code'] = 'Not in the List'

        if row['reqt_date'] not in Mandates.objects.values_list('AssignedDate', flat = True):
            dict['reqt_date'] = 'Not in the List'


        if 'client' not in dict.keys() or 'vacancy_code' not in dict.keys():
            pass
        else:
            k = row['client'] + row['vacancy_code']
            if k in token:
                dict['candidate_name'] = 'Not unique'
            else:
                token.append(k)



        if CandidateStatus.objects.filter(StageID = row['current_status']).exists():
            stagedb = CandidateStatus.objects.filter(StageID = row['current_status']).values_list('StageName', flat = True)
            if row['current_status_desc'] not in stagedb:
                dict['current_status_desc'] = 'Mismatch!'

        else:
            dict['current_status'] = 'Not in the List'



        if len(row['contact_details_mobile']) != 10:
            dict['contact_details_mobile'] = 'Not 10 digits'

        ph = []
        if len(row['contact_details_phone2']) != 10:
            ph.append('Not 10 digits')
            dict['contact_details_phone2'] = ph


        if row['contact_details_phone2'] == row['contact_details_mobile']:
            if dict['contact_details_phone2']:
                ph.append('Repeated Contact')
                dict['contact_details_phone2'] = ph


        if not row['total_exp'].replace('.', '', 1).isdigit():
            dict['total_exp'] = 'Invalid format'


        if not re.search(regex,row['email']):
            dict['email'] = 'Invalid Email'


        if (not row['current_salary'].replace('.', '', 1).isdigit()) and row['current_salary'] > '9999':
            dict['current_salary'] = 'Invalid Amount'


        if not row['expected_salary_percentage'].replace('.', '', 1).isdigit():
            dict['expected_salary_percentage'] = 'Not Numeric'


        if (not row['expected_salary_amt'].replace('.', '', 1).isdigit()) and row['expected_salary_amt'] > '9999':
                dict['expected_salary_amt'] = 'Invalid Amount'

        if not row['notice_period'].replace('.', '', 1).isdigit():
            dict['notice_period'] = 'Not Numeric'

        # not updated
        status = row['current_status']
        if status != 0:

            # type select
            if int(status) < 100:

                if row['date_cv_submitted'] < row['reqt_date']:
                    dict['date_cv_submitted'] = 'Should be after reqt date'

                if row['interview_date'] < row['date_cv_submitted']:
                    dict['interview_date'] = 'Should be after cv submitted'
                    row['reason'] = dict

                if row['Int_Tele_Date'] < row['interview_date']:
                    dict['Int_Tele_Date'] = 'Should be after interview date'
                    row['reason'] = dict

                if row['Int_p1_Date'] < row['interview_date']:
                    dict['Int_p1_Date'] = 'Should be after interview date'
                    row['reason'] = dict

                if row['Int_p2_Date'] < row['Int_p1_Date']:
                    dict['Int_p2_Date'] = 'Should be after p1'
                    row['reason'] = dict

                if row['Int_p3_Date'] < row['Int_p2_Date']:
                    dict['Int_p3_Date'] = 'Should be after p2'
                    row['reason'] = dict

                if row['Int_Final_Date'] < row['Int_p3_Date']:
                    dict['Int_Final_Date'] = 'Should be after p3'
                    row['reason'] = dict

                if row['Int_Final_Date'] != None:
                    if row['Int_HR_Date'] < row['Int_Final_Date']:
                        dict['Int_HR_Date'] = 'Should be after final date'
                        row['reason'] = dict
                else:
                    if row['Int_HR_Date'] < row['interview_date']:
                        dict['Int_HR_Date'] = 'Should be after interview date'
                        row['reason'] = dict

                if row['offer_date'] < row['Int_Final_Date'] or row['offer_date'] < row['interview_date'] :
                    dict['offer_date'] = 'Should be after final/interview date'
                    row['reason'] = dict

                if row['joining_date'] < row['offer_date']:
                    dict['joining_date'] = 'Should be after offer date'
                    row['reason'] = dict

                # if row['offer_amt'] != None:
                if (not row['offer_amt'].replace('.', '', 1).isdigit()) and row['offer_amt'] < '9999':
                    dict['offer_amt'] = 'Invalid Amount'

            # type reject
            else:

                if status > 102:

                    if status > 104:

                         if status > 105:

                            if status > 106:

                                if status > 107:

                                    if status > 108:

                                        if status > 110:

                                            if status > 112:

                                                # 115
                                                if row['joining_date'] < row['offer_date']:
                                                    dict['joining_date'] = 'Should be after offer date'
                                                    row['reason'] = dict

                                            # 112
                                            if row['offer_date'] < row['Int_Final_Date'] or row['offer_date'] < row['interview_date'] :
                                                dict['offer_date'] = 'Should be after final/interview date'
                                                row['reason'] = dict

                                        # 110/109
                                        if row['Int_Final_Date'] != None:
                                            if row['Int_HR_Date'] < row['Int_Final_Date']:
                                                dict['Int_HR_Date'] = 'Should be after final date'
                                                row['reason'] = dict
                                        else:
                                            if row['Int_HR_Date'] < row['interview_date']:
                                                dict['Int_HR_Date'] = 'Should be after interview date'
                                                row['reason'] = dict
                                    # 108
                                    if row['Int_Final_Date'] < row['Int_p3_Date']:
                                        dict['Int_Final_Date'] = 'Should be after p3'
                                        row['reason'] = dict

                                # 107
                                if row['Int_p2_Date'] < row['Int_p1_Date']:
                                    dict['Int_p2_Date'] = 'Should be after p1'
                                    row['reason'] = dict

                                if row['Int_p3_Date'] < row['Int_p2_Date']:
                                    dict['Int_p3_Date'] = 'Should be after p2'
                                    row['reason'] = dict

                            # 106
                            if row['Int_p1_Date'] < row['interview_date']:
                                dict['Int_p1_Date'] = 'Should be after interview date'
                                row['reason'] = dict

                        # 105
                        if row['Int_Tele_Date'] < row['interview_date']:
                            dict['Int_Tele_Date'] = 'Should be after interview date'
                            row['reason'] = dict

                    #103
                    if row['interview_date'] < row['date_cv_submitted']:
                        dict['interview_date'] = 'Should be after cv submitted'
                        row['reason'] = dict

                # 101/102
                if row['date_cv_submitted'] < row['reqt_date']:
                    dict['date_cv_submitted'] = 'Should be after reqt date'


        row['reason'] = dict


        if row['reason'] != {}:

            bad = df.loc[df['reason'] != {}]

            # BadRecords.objects.bulk_create(
            #     BadRecords(**recs) for recs in df.to_dict('row')
            # )
            print("BAD")

        else:
            good = df.loc[df['reason'] == {}]

            # GoodRecords.objects.bulk_create(
            #     GoodRecords(**recs) for recs in df.to_dict('row')
            # )
            print("GOOD")


        # Staging.objects.get(id = row['id']).delete()
        # df.drop(index)
        print("DONE")


    return HttpResponse(df.to_html())'''