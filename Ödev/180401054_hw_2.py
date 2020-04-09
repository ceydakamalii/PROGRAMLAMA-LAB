import sys ,csv
liste=[]
with open(sys.argv[1]+"/input_hw_2.csv","r") as csv_file:
    for i in csv_file:
        liste.append(int(i.split(";")[3].split("-")[1]))

print(liste)
def bubble_sort(liste):
    n=len(liste)
    print(liste)
    for i in range (n-1,-1,-1):
        for j in range(0,i):
            if not (liste[j]<liste[j+1]):
                temp=liste[j]
                liste[j]=liste[j+1]
                liste[j+1]=temp
    return liste
liste1=bubble_sort(liste)
print(liste1)

def my_frequency_with_dict(liste):
    frequency_dict={}
    for item in liste:
        if item in frequency_dict.keys():
            frequency_dict[item]=frequency_dict[item]+1
        else:
            frequency_dict[item]=1
    return frequency_dict
histogram=my_frequency_with_dict(liste1)
print(histogram)

hist1=list(histogram.values())


def my_median(my_list):
    my_list=bubble_sort(my_list)
    n=len(my_list)

    if n%2==1:
        middle=int(n/2)+1
        median=my_list[middle]
    else:
        middle_1 = int(n / 2) - 1
        middle_2 = middle_1 + 1
        median=(my_list[middle_1]+my_list[middle_2])/2
    return median


def my_mean(my_list):
    s,t=0,0
    for item in my_list:
        s=s+1
        t=t+item

    mean_=t/s

    return mean_

ort=int(my_mean(hist1))
medyan=my_median(hist1)


with open(sys.argv[2]+"180401054_hw_2_output.txt","w")as file:
   ## file.write("ortalama=")
    ##file.write(str(my_mean()))
   ## file.write("\n")
   ## file.write("medyan=")
  ## file.write(str(my_median()))
  file.write("ortalama:"+str(ort)+"\n"+"medyan:"+str(medyan))
