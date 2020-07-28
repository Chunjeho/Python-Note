import numpy as np
import matplotlib.pyplot as plt
import csv
from collections import Counter
import pandas as pd

def first():
    with open('data.csv') as file:
        reader = csv.DictReader(file)
        lan_counter = Counter()

        for row in reader:
            lan_counter.update(row['LanguagesWorkedWith'].split(';'))
    x = []
    y = []

    for item in lan_counter.most_common(15):
        x.append(item[0]) #Programming language
        y.append(item[1]) #Popularity

    x.reverse()
    y.reverse()

    plt.barh(x, y)

    plt.title('Programming Language Popularity')
    #plt.ylabel('Programming Language')
    plt.xlabel('Popularity')

    plt.tight_layout()

    plt.show()

def second():
    data = pd.read_csv('data.csv')
    ids = data['Responder_id']
    lan = data['LanguagesWorkedWith']
    lan_counter = Counter()

    for row in lan:
        lan_counter.update(row.split(';'))

    x = []
    y = []

    for item in lan_counter.most_common(15):
        x.append(item[0]) #Programming language
        y.append(item[1]) #Popularity

    x.reverse()
    y.reverse()

    plt.barh(x, y)

    plt.title('Programming Language Popularity')
    #plt.ylabel('Programming Language')
    plt.xlabel('Popularity')

    plt.tight_layout()

    plt.show()

first()
