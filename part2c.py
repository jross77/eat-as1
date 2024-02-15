import pandas as pd
import numpy as np
import math
from scipy.stats import gstd, gmean

def stratified_sampling(seg, sample_size):
    sample = pd.Series(dtype=float)
    seg = pd.Series(seg)
    sample = seg.sample(frac=sample_size, replace=False)
    
    return sample

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

def nf(mean, sd):
    value = mean*math.pow(sd, 1.645)
    return value

mat = np.array([0.7,1.0,0.4,2.5,1.2,0.9,0.5,1.3,0.2,2.1,1.6,0.8])
qual = np.array([2.1,2.5,2.0,2.0,2.3,1.7])
ship = np.array([1.6,0.6,2.4,0.6,0.8,1.0,2.4,1.1,0.9,0.6,0.7,2.0,2.2,0.5])
form = np.array([1.5,1.7,3.2,0.9,1.4,1.2,1.2,0.8,1.3,0.7,2.0,0.8,2.0,2.0,1.1,1.7,0.7,1.1])
prod = np.array([0.7,3.8,0.6,1.5,1.9,3.9,1.1,3.1,1.8,1.3,1.0,5.4,2.5,2.6,2.3,1.9,1.6,
                    0.5,1.8,2.4,2.4,1.8,3.8,3.5,1.3,7.2,7.2,5.4,2.6,1.1,1.9,3.6,0.8,2.8,1.0,
                    2.1,1.9,1.0,1.9,1.2,3.5,0.8,9.2,4.5,2.9,1.0,7.3,0.7,4.3,2.1,0.6,2.6,1.0,2.4])
'''
print("\nMaintenance:")
print("\n100 percent:")
calculate(mat)
print("\n50 percent:")
mat50 = stratified_sampling(mat, .5)
calculate(mat50)
print("\n20 percent:")
mat20 = stratified_sampling(mat, .2)
calculate(mat20)

print("\nQuality Control:")
print("\n20 percent:")
qual20 = stratified_sampling(qual, .2)
calculate(qual20)
print("\n50 percent:")
qual50 = stratified_sampling(qual, .5)
calculate(qual50)
print("\n100 percent:")
calculate(qual)

print("\nShipping:")
print("\n20 percent:")
ship20 = stratified_sampling(ship, .2)
calculate(ship20)
print("\n50 percent:")
ship50 = stratified_sampling(ship, .5)
calculate(ship50)
print("\n100 percent:")
calculate(ship)

print("\nForming:")
print("\n20 percent:")
form20 = stratified_sampling(form, .2)
calculate(form20)
print("\n50 percent:")
form50 = stratified_sampling(form, .5)
calculate(form50)
print("\n100 percent:")
calculate(form)

print("\nProduction:")
print("\n20 percent:")
prod20 = stratified_sampling(prod, .2)
calculate(prod20)
print("\n50 percent:")
prod50 = stratified_sampling(prod, .5)
calculate(prod50)
print("\n100 percent:")
calculate(prod)
'''
print("\nProduction:")
print("\n7 sample:")
prod7 = stratified_sampling(prod, .13)
calculate(prod7)

print("\nMaintenance:")
print("\n7 sample:")
mat7 = stratified_sampling(mat, .58)
calculate(mat7)


print("\nShipping:")
print("\n7 sample:")
ship7 = stratified_sampling(ship, .5)
calculate(ship7)

print("\nForming:")
print("\n7 sample:")
form7 = stratified_sampling(form, .39)
calculate(form7)

print("\nMaintenance:")
print("100%: "+str(nf(0.8950030892335079,2.0494272670019487)))
print("50%: "+str(nf(0.8377137083581049,1.6965733618898815)))
print("20%: "+str(nf( 0.8,2.665144142690225)))
print("7: "+str(nf(0.8919891746555878, 1.6658539949109679)))

print("\nQuality Control:")
print("100%: "+str(nf(2.0848077302407892,1.1416703166528315)))
print("50%: "+str(nf(1.925599970404374,1.1169903260843541)))
print("20%: ")
print("7: "+str(nf(2.0848077302407892,1.1416703166528315)))


print("\nShipping:")
print("100%: "+str(nf(1.0654112891069074,1.7726162107654533)))
print("50%: "+str(nf(1.1804160358420506,1.9341756339410279)))
print("20%: "+str(nf(0.9966554934125964,1.1055879616917743)))
print("7: "+str(nf(1.1470572008593307, 1.9172057833418659)))

print("\nForming:")
print("100%: "+str(nf(1.2910651552782957,1.5198371848735999)))
print("50%: "+str(nf(1.0730929887798122,1.4536714193746336)))
print("20%: "+str(nf(1.1940531619864039, 1.120453056750261)))
print("7: "+str(nf(1.174270464921672, 1.501518127959168)))


print("\nProduction:")
print("100%: "+str(nf(2.0261435251238047,2.0197807671275534)))
print("50%: "+str(nf(1.9211643759080035,2.011253747693941)))
print("20%: "+str(nf(1.6520512663849476, 2.022461682074302)))
print("7: "+str(nf(1.6380774380189016, 1.8350230125007465)))

print("\nMaintenance:")
print("\n7 sample:")
mat7 = stratified_sampling(mat, .58)
calculate(mat7)