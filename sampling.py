import plotly.figure_factory as ff
import pandas as pd
import statistics
import random

df=pd.read_csv("data.csv")
data= df["data"].tolist()

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0, counter):
        random_index= random.randint(0, len(data)-1)
        value= data[random_index]
        dataset.append(value)
    mean= statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean= statistics.mean(df)
    fig=ff.create_distplot([df], ["data"], show_hist=False)
    fig.show()

def setup():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean=statistics.mean(mean_list)
    print("Mean of the sampling distribution is: ", mean)

setup()

population_mean= statistics.mean(data)
print("Population mean is: ", population_mean)

def std_dev():
    mean_list=[]
    for i in range(0, 1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation=statistics.stdev(mean_list)
    print("Standard Deviation of the sampling distribution is: ", std_deviation)

std_dev()

population_stdev=statistics.stdev(data)
print("Standard Deviation of the population is: ", population_stdev)