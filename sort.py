import random as r

m=[r.randint(0,99999) for i in range(10**2)]

def quicksort(l):
   n=len(l)
   if n<1:
      return l
   p=l[0]
   return quicksort([e for e in l[1:] if e<p])+[p]+quicksort([e for e in l[1:] if e>=p])

def gnomesort(a):
   i,j,size = 1,2,len(a)
   while i < size:
      if a[i-1] <= a[i]:
         i,j = j, j+1
      else:
         a[i-1],a[i] = a[i],a[i-1]
         i -= 1
         if i == 0:
            i,j = j, j+1
   return a
      
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

def bubblesort(a):
    fin = len(a)-1#-2 en vrai
    en_desordre = True
    while en_desordre:
        en_desordre = False
        for i in range(fin):
            if a[i]>a[i+1]:
                en_desordre = True
                a[i],a[i+1]=a[i+1],a[i]
        fin-=1
        print(a)
    return a
    
def cocktailshakersort(a):
   deb =0
   fin = len(a)-1#-2 en vrai
   en_desordre = True
   while en_desordre:
      en_desordre = False
      for i in range(deb,fin):
         if a[i]>a[i+1]:
            en_desordre = True
            a[i],a[i+1]=a[i+1],a[i]
      fin-=1
      for i in range(fin,deb-1,-1): #pas de -1 en vrai
         if a[i]>a[i+1]:
            en_desordre = True
            a[i],a[i+1]=a[i+1],a[i]
      deb+=1
      print(a)
   return a
