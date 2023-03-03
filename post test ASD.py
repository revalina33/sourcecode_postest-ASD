import random

def menu():
    print("1.shell sort")
    print("2.quick sort")
    print("3.merge sort")
    print("4.selesai")
    
loop=True#berguna untuk melakukan perulangan
while True:
 menu()
 pilih=input("cara: ")

#shell sort(membandingkan angka pada suatu bilangan dengan jarak tertentu)
 def shell_sort(numlist):
       gap=(len(numlist)//2)
       a=0
       while gap>0:
        for i in range(gap,len(numlist)):
            value=numlist[i]
            j=i
            while j>=gap and numlist[j-gap]>value:
                numlist[j]=numlist[j-gap]
                j-=gap
                
            numlist[j]=value
        print("iterasi ke:",a,":",numlist,"dengan gap",gap)
        a+=1
        
        gap //=2
       return numlist
   #return berguna untuk mengembalikan nilai sehingga angka akan terurut

 if pilih=="1":
      numlist=random.sample(range(1,15),10)#import angka random
      print("data belum terurut:")
      print(numlist)#data yang belum terurut
      hasil=shell_sort(numlist)
      print("data terurut:",hasil)              

#quick sort adalah pengurutan data menggunakan pivot
 def quicksort(numlist):
      index=len(numlist)
      #jika index memiliki satu elemen/kurang kembalikan numlist
      if index<=1:
        return numlist
      else:
        pivot=numlist.pop()
        
      left_list=[]
      right_list=[]
      print(f"Pivot : {pivot}")
      for i in numlist:
        if i<pivot:
            left_list.append(i)
        else:
            right_list.append(i)
    
      return quicksort(left_list)+[pivot]+quicksort(right_list)
 if pilih=="2":
    numlist=random.sample(range(1,15),10)
    #import data random ,range adalah jangkauan data 
    print("data belum terurut:",numlist)
    hasil=quicksort(numlist)
    print("data terurut:",hasil)#data yang sudah terurut
 

 def mergesort(numlist):
     #menentukan index yang berada ditengah numlist lalu dipisahkan mennjadi dua bagian
      if len(numlist)>1:
        mid=len(numlist)//2
        left=numlist[:mid]
        right=numlist[mid:]
        
        mergesort(left)
        mergesort(right)
        
        i=0
        j=0
        k=0
    
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                numlist[k]=left[i]
                i+=1
            else:
                numlist[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            numlist[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            numlist[k]=right[j]
            j+=1
            k+=1
    
        return numlist 
 if pilih=="3":
    numlist=random.sample(range(1,15),10)
    print("data belum terurut:",numlist)
    print("data terurut:",mergesort(numlist))    

   
 def selesai():
    print("selesai")

 if pilih=="4":
    selesai() 
    break#berguna untuk menghentikan program
    