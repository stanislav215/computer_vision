import numpy as np


# Dokoncit cvicenie po stranu 10 okrem vizualizacie
#Vizualizacia sa bude preberat nma dalsom cviceni

# odovzdat na gitlabe zadanie  do strany 10


#príklad na riadenie toku programu:
#MATLAB
#for i=1:2:7
#   i
#end

#for i=[5 13 -1]
#    if (i > 10)
#        disp('Larger than 10')
#        disp('Negative value')
#    else
#        disp('Something else')
#    end
#end
#-------------------------------------
#PYTHON

for i in range(1,7,2):
    print(i)

vec = np.array([5,13,-1])

for i in vec:
     if (i > 10):
         print("\nLarger than 10")
     elif (i < 0):
         print("\nNegative value")
     else:
         print("\nSomething else")
#odčítanie vektora od každého riadku matice
#MATLAB
# m = 50; n = 10; A = ones(m, n); v = 2 * rand(1, n);
# for i=1:m
#     A(i,:) = A(i,:) - v;
# end
#
# A = ones(m, n) - repmat(v, m, 1);
#-------------------------------------------------
#PYTHON
m = 50
n = 10
A = np.ones([m, n])
v = 2 * np.random.rand(1, n)
for i in range(1, m, 1):
    A[i][:] = A[i][:] - v
print(A)

A = np.ones([m, n]) - np.tile(v, (m, 1))
print(A)
#kopriovanie matice A do B
#MATLAB
# Matlab syntax z PDF
# B = zeros(m, n);
# for i=1:m
#     for j=1:n
#         if A(i, j) > 0
#             B(i, j) = A(i, j);
#         end
#     end
# end
#
# B = zeros(m, n);
# ind = find(A > 0);
# B(ind) = A(ind);
#-----------------------------------------------
#PYTHON
B = np.zeros([m, n])
for i in range(0, m):
        for j in range(1, n):
            if (A[i][j] > 0):
                B[i][j] = A[i][j]

print("Matica B vyuzitim for cyklu\n", B)

B = np.zeros([m, n])
ind = np.where(A > 0)
B[ind] = A[ind]

print("Matica B vyuzitim np.where\n", B)


#Pre-alokovanie si miesta + porovnanie času tic-toc
# MATLAB
# tic
# x = 0;
# for k = 2:1000000
#     x(k) = x(k - 1) + 5;
# end
# toc

# tic
# x = zeros(1, 1000000);
# for k = 2:1000000
#     x(k) = x(k - 1) + 5;
# end
# toc

#-----------------------------------------------------------
#PYTHON
import time

beginTime = time.time()
x = np.array([0])
for i in range(1, 1000000):
    x.resize((1, i+1)) # realokovanie miesta pre dalsi element
    x[0][i] = x[0][i-1] + 5
endTime = time.time()
print("Cas bez alokacie:\t", endTime - beginTime)

beginTime = time.time()
x = np.zeros([1, 1000000])
for i in range(1, 1000000):
    x[0][i] = x[0][i-1] + 5
endTime = time.time()
print("Cas s alokaciou:\t", endTime - beginTime)

# Práca so súbormi
#MATLAB
# save myfile
# save myfile a b
# clear a b
# clear
# load myfile
#-----------------------------------------------------------
#PYTHON
import sys
import dill
import hickle

dill.dump_session('myfile1.pkl') #ulozi vsetky premenne do suboru myfile

hickle.dump([A, B], 'myfile.pkl')#ulozi A,B do suboru myfile

del A, B #vymate A,B
dill.load_session('myfile1.pkl') #nacita premenne zo suboru myfile


#for name in dir():
    #print(name)
    #if not name.startswith('_'): #vymazanie premenných
        #del globals()[name]


#Funkcie
#MATLAB
#function y = myfunction(x)
#a = [-2 -1 0 1];
#y = a + x;

#function [y, z] = myotherfunction(a, b)
#y = a + b;
#z = a - b;
#---------------------------------------------------
#PYTHON
def myfunction(X):
    A = np.array([-2, -1, 0, 1])
    return A + X
def myotherfunction(a, b):
    return (a+b, a-b)

#test funkcii
a = np.array([1,2,3,4])
b = myfunction(2*a)
(c,d) = myotherfunction(a,b)