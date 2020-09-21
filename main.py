def bubble_sort(x):
  for i in range(len(x)-1,0,-1):
    print("len(x)-1="+str(len(x)-1)+" i="+str(i))
    for j in range(i):
      print("j="+str(j))
      if x[j]>x[j+1]:
        temp = x[j]
        x[j]=x[j+1]
        print("x="+str(x))
        x[j+1]=temp
        print("x="+str(x))

val = [47,10,98,1001,8,79,100,55,78,18]
bubble_sort(val)
print(val)

"""
Berikut ini adalah gambaran dari algoritma bubble sort:
- Bandingkan nilai data ke-1 dan data ke-2
- Jika data ke-1 lebih besar dari data ke-2 maka tukar posisinya
- Kemudian data yg lebih besar tadi dibandingkan dengan data ke-3
- Lakukan langkah nomer 2 hingga selesai.
"""