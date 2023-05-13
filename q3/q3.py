import csv
import matplotlib.pyplot as plt

def main() :
    
    f = open('jejupop.csv', encoding = 'cp949')

    data = csv.reader(f)
    header = next(data)

    man = []
    woman= []

    #start 3 by 4 is man pop
    #start 4 by 4 is woman pop
    
    for row in data :
        for i in range(3,33,4) :
            man.append(int(row[i].replace(',','')))
        for k in range(4,33,4) :
            woman.append(int(row[k].replace(',','')))

    plt.title('15\'~22\' Jeju Population Graph')
    plt.barh(range(2015,2023,1),man,label='man')
    plt.barh(range(2015,2023,1),woman,label='woman')

    
    plt.legend()
    plt.show()
    
    
if __name__ == "__main__" :
    main()
