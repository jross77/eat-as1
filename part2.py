import pandas as pd
import numpy as np
from scipy.stats import gstd, gmean

def stratified_sampling(df, sample_size):
    sample = pd.DataFrame()
    
    for group in df:
        stratum_sample = df[group].sample(frac=sample_size, replace=False, random_state=7)
        sample = sample.append(stratum_sample)
    
    return sample

mat = np.array([0.7,1.0,0.4,2.5,1.2,0.9,0.5,1.3,0.2,2.1,1.6,0.8])
qual = np.array([2.1,2.5,2.0,2.0,2.3,1.7])
ship = np.array([1.6,0.6,2.4,0.6,0.8,1.0,2.4,1.1,0.9,0.6,0.7,2.0,2.2,0.5])
form = np.array([1.5,1.7,3.2,0.9,1.4,1.2,1.2,0.8,1.3,0.7,2.0,0.8,2.0,2.0,1.1,1.7,0.7,1.1])
prod = np.array([0.7,3.8,0.6,1.5,1.9,3.9,1.1,3.1,1.8,1.3,1.0,5.4,2.5,2.6,2.3,1.9,1.6,
                    0.5,1.8,2.4,2.4,1.8,3.8,3.5,1.3,7.2,7.2,5.4,2.6,1.1,1.9,3.6,0.8,2.8,1.0,
                    2.1,1.9,1.0,1.9,1.2,3.5,0.8,9.2,4.5,2.9,1.0,7.3,0.7,4.3,2.1,0.6,2.6,1.0,2.4])
data = {
        'Maintenance':pd.Series(mat), 
        'Quality Control': pd.Series(qual),
        'Shipping': pd.Series(ship),
        'Forming': pd.Series(form),
        'Production': pd.Series(prod)
        }

def find_min_max(data):
    min = 125
    max = -1
    above_OEL = 0
    for x in data:
        for i in data[x]:
            if i < min:
                min = i
            elif i > max:
                max = i
            if i > 3.5:
                above_OEL += 1
    print("Max: " + str(max))
    print("Min: " + str(min))
    print("Above OEL: "+str(above_OEL))

def find_med(mat, qual, ship, form, prod):
    med = -1
    full_list = mat
    for i in [qual, ship, form, prod]:
        full_list = np.concatenate((full_list, i))
    print("Full min: "+str(np.min(full_list)))
    print("Full max: "+str(np.max(full_list)))
    full_list = np.sort(full_list)
    print("Length: "+ str(len(full_list)))
    print("Full median: "+str(np.median(full_list)))
    print("Full mean: "+str(np.mean(full_list)))
    print("Full GM: "+str(gmean(full_list)))
    print("Full GSD: "+str(gstd(full_list)))
    above_OEL = sum(full_list > 3.5)
    print("Above OEL: "+str(above_OEL))

df = pd.DataFrame(data)

sample = stratified_sampling(df, .2)
sample2 = stratified_sampling(df, .33)
sample3 = stratified_sampling(df, .54)
print(sample)
print(sample2)
print(sample3)
#find_min_max(df)
mat1 = sample.iloc[0].dropna().values
qual1 = sample.iloc[1].dropna().values
ship1 = sample.iloc[2].dropna().values
form1= sample.iloc[3].dropna().values
prod1=sample.iloc[4].dropna().values

mat2 = sample2.iloc[0].dropna().values
qual2 = sample2.iloc[1].dropna().values
ship2 = sample2.iloc[2].dropna().values
form2= sample2.iloc[3].dropna().values
prod2=sample2.iloc[4].dropna().values

mat3 = sample3.iloc[0].dropna().values
qual3 = sample3.iloc[1].dropna().values
ship3 = sample3.iloc[2].dropna().values
form3= sample3.iloc[3].dropna().values
prod3=sample3.iloc[4].dropna().values

#find_med(mat, qual, ship, form, prod)


#print("\nSample n = 19 data: ")
#find_med(mat1, qual1, ship1, form1, prod1)
#print("\nSample n = 29 data: ")
#find_med(mat2, qual2, ship2, form2, prod2)
#print("\nSample n = 48 data: ")
#find_med(mat3, qual3, ship3, form3, prod3)




def calculate(seg):
    print("Full min: "+str(np.min(seg)))
    print("Full max: "+str(np.max(seg)))
    seg = np.sort(seg)
    print("Length: "+ str(len(seg)))
    print("Full median: "+str(np.median(seg)))
    print("Full mean: "+str(np.mean(seg)))
    print("Full GM: "+str(gmean(seg)))
    if len(seg)>1:
        print("Full GSD: "+str(gstd(seg)))
    above_OEL = sum(seg > 3.5)
    print("Above OEL: "+str(above_OEL))

print("\nData for Maintenance n=20")
calculate(mat1)
print("\nData for Maintenance n=50")
calculate(mat3)
print("\nData for Maintenance n=100")
calculate(mat)

print("\nData for Quality Control n=20")
calculate(qual1)
print("\nData for Quality Control n=50")
print(qual3)
calculate(qual3)
print("\nData for Quality Control n=100")
calculate(qual)

print("\nData for Shipping n=20")
calculate(ship1)
print("\nData for Shipping n=50")
calculate(ship3)
print("\nData for Shipping n=100")
calculate(ship)

print("\nData for Forming n=20")
calculate(form1)
print("\nData for Forming n=50")
calculate(form3)
print("\nData for Forming n=100")
calculate(form)

print("\nData for Production n=20")
calculate(prod1)
print("\nData for Production n=50")
calculate(prod3)
print("\nData for Production n=100")
calculate(prod)