import random as r

m=[r.randint(0,99999) for i in range(10**2)]

def quicksort(l):
   n=len(l)
   if n<1:
      return l
   p=l[0]
   return quicksort([e for e in l[1:] if e<p])+[p]+quicksort([e for e in l[1:] if e>=p])

def bubblesort(l):
   i=0
   n=len(l)-1
   while i<n:
      if l[i]>l[i+1]:
         l[i],l[i+1]=l[i+1],l[i]
         i=-1
      i+=1
   return l
      
def exchangesort(l):
   for i in range(len(l)-1):
      for j in range(i+1,len(l)):
         if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
   return l
      
def selectionsort(l):
   m=0
   for i in range(len(l)-1):
      for j in range(i,len(l)):
         if l[j]<l[m]:
            m=j
      l[m],l[i]=l[i],l[m]
   return l



print(selectionsort(m),"\n")
print(bubblesort(m),"\n")
print(exchangesort(m),"\n")
print(quicksort(m))
