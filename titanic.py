#-*- coding:utf-8 -*-
import numpy as np
import pandas as pd

data = pd.read_csv("train.csv")
male_total = data[data['Sex']=='male'].shape[0]
female_total = data[data['Sex']=='female'].shape[0]

male_survived = data[data['Survived']==1][data['Sex']=='male']
female_survived = data[data['Survived']==1][data['Sex']=='female']
male_survived_Siblings_And_Spouse = male_survived["SibSp"]
female_survived_Siblings_And_Spouse = female_survived["SibSp"]
male_Parents_And_Childrens = male_survived["Parch"]
female_Parents_And_Childrens = female_survived["Parch"]

male_unsurvived = data[data['Survived']==0][data['Sex']=='male']
female_unsurvived = data[data['Survived']==0][data['Sex']=='female']
male_unsurvived_Siblings_And_Spouse = male_unsurvived["SibSp"]
female_unsurvived_Siblings_And_Spouse = female_unsurvived["SibSp"]
male_unsurvived_Parents_And_Childrens = male_unsurvived["Parch"]
female_unsurvived_Parents_And_Childrens = female_unsurvived["Parch"]





print("Total Records -",data.shape[0])
print("Male -")
print("	Total -",male_total)
print("	Survived -",male_survived.shape[0],"(",male_survived.shape[0]/male_total,") -> SibSp(",male_survived_Siblings_And_Spouse.unique(),"), Parch(",male_Parents_And_Childrens.unique(),")")
print("	UnSurvived -",male_unsurvived.shape[0],"(",male_unsurvived.shape[0]/male_total,") -> SibSp(",male_unsurvived_Siblings_And_Spouse.unique(),"), Parch(",male_unsurvived_Parents_And_Childrens.unique(),")")
print("Female -")
print("	Total -",female_total)
print("	Survived -",female_survived.shape[0],"(",female_survived.shape[0]/female_total,") -> SibSp(",female_survived_Siblings_And_Spouse.unique(),"), Parch(",female_Parents_And_Childrens.unique(),")")
print("	UnSurvived -",female_unsurvived.shape[0],"(",female_unsurvived.shape[0]/male_total,") -> SibSp(",female_unsurvived_Siblings_And_Spouse.unique(),"), Parch(",male_unsurvived_Parents_And_Childrens.unique(),")")