import csv
import matplotlib.pyplot as plt

def main() :
    
    w_weather = []
    s_weather = []
    b_weather = []
    d_weather = []
    j_weather = []
    month = [1,2,3,4,5,6,7,8,9,10,11,12]

    w = open("wholecountry.csv", encoding='cp949')
    w_data = csv.reader(w)
    w_header = next(w_data)


    for row in w_data :
        if row[1] == '전국' :
            w_weather.append(float(row[2]))

    w.close()

    c = open("seoul.csv", encoding='cp949')
    c_data = csv.reader(c)
    c_header = next(c_data)


    for row in c_data :
        if row[1] == '108' :
            s_weather.append(float(row[2]))

    c.close()

    c = open("busan.csv", encoding='cp949')
    c_data = csv.reader(c)
    c_header = next(c_data)

    for row in c_data :
        if row[1] == '159' :
            b_weather.append(float(row[2]))

    c.close()

    c = open("daegeon.csv", encoding='cp949')
    c_data = csv.reader(c)
    c_header = next(c_data)

    for row in c_data :
        if row[1] == '133' :
            d_weather.append(float(row[2]))

    c.close()

    c = open("jeju.csv", encoding='cp949')
    c_data = csv.reader(c)
    c_header = next(c_data)

    for row in c_data :
        if row[1] == '184' :
            j_weather.append(float(row[2]))

    c.close()


    plt.title("2022 Montly country Weather")
    plt.plot(month,w_weather, label="Whole", color="black")
    plt.plot(month,s_weather, label="Seoul")
    plt.plot(month,b_weather, label="Busan")
    plt.plot(month,d_weather, label="Daejeon")
    plt.plot(month,j_weather, label="JeJu")
    plt.legend()
    plt.show()
    

if __name__ == "__main__":
    main()
