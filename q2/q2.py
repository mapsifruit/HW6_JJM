import csv
import random as r
import matplotlib.pyplot as plt

def main() :
    f = open("result.csv","w")

    temp = []
    for i in range(100) :
        temp.append(r.randint(1,6))
    temp = str(temp).replace('[','')
    temp = temp.replace(']','')
    f.write(temp)
    f.write("\n")

    temp = []
    for i in range(1000) :
        temp.append(r.randint(1,6))
    temp = str(temp).replace('[','')
    temp = temp.replace(']','')
    f.write(temp)
    f.write("\n")

    temp = []
    for i in range(10000) :
        temp.append(r.randint(1,6))
    temp = str(temp).replace('[','')
    temp = temp.replace(']','')
    f.write(temp)
    f.write("\n")

    temp = []
    for i in range(100000) :
        temp.append(r.randint(1,6))
    temp = str(temp).replace('[','')
    temp = temp.replace(']','')
    f.write(temp)
    f.write("\n")

    f.close()



    f = open('result.csv')
    
    data = csv.reader(f)

    rap = [[],[],[],[]]
    i = 0
    
    for row in data :
        for rlt in row :
            rap[i].append(int(rlt))
        i+=1

        
    plt.subplot(221)
    plt.title('Do 100')
    plt.hist(rap[0])

    plt.subplot(222)
    plt.title('Do 1000')
    plt.hist(rap[1])

    plt.subplot(223)
    plt.title('Do 10000')
    plt.hist(rap[2])

    plt.subplot(224)
    plt.title('Do 100000')
    plt.hist(rap[3])

    plt.show()

    f.close()


    
if __name__ == "__main__" :
    main()
