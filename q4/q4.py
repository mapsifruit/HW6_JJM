import csv
import matplotlib.pyplot as plt
from matplotlib import rc

def main() :
    
    f = open('202303subway.csv')

    data = csv.reader(f)
    header = next(data)
    info = next(data)

    
    getin = 0
    getin_stn = {}
    getout_stn = {}
    use_stn = {}
    
    for row in data :
        temp = int(row[10]) + int(row[12])
        pmet = int(row[11]) + int(row[13])

        if row[3] in list(getin_stn.keys()) :
            getin_stn[row[3]]+=temp
            getout_stn[row[3]]+=pmet
            use_stn[row[3]]+=temp+pmet
        else :
            getin_stn[row[3]]=temp
            getout_stn[row[3]]=pmet
            use_stn[row[3]]=temp+pmet

    srt_gi = sorted(getin_stn.items(), reverse=True, key=lambda x:x[1])[:30]
    srt_go = sorted(getout_stn.items(), reverse = True, key=lambda x: x[1])[:30]
    srt_use = sorted(use_stn.items(), reverse = True, key=lambda x:x[1])[:30]

    gi_name = []
    gi_pop = []
    go_name = []
    go_pop = []
    use_name = []
    use_pop = []

    for i in range(30) :
        gi_name.append(srt_gi[i][0])
        gi_pop.append(srt_gi[i][1])
        go_name.append(srt_go[i][0])
        go_pop.append(srt_go[i][1])
        use_name.append(srt_use[i][0])
        use_pop.append(srt_use[i][1])

    rc('font',family='AppleGothic')
    plt.rcParams['axes.unicode_minus']=False

    plt.subplot(221)
    plt.title('2023-03 승차 인원')
    plt.barh(gi_name,gi_pop)

    plt.subplot(222)
    plt.title('2023-03 하차 인원')
    plt.barh(go_name,go_pop)

    plt.subplot(223)
    plt.title('2023-03 승하차 인원')
    plt.barh(use_name,use_pop)
    plt.show()


if __name__ == "__main__" :
    main()
