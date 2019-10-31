import pandas as pd
import csv
import os
import json

path="../data/W-2019.csv"

class CSVmanager:

    def csvtojson(path):
        data=pd.read_csv(path)

        column=list(data.columns)

        for i in range(len(column)):
            column[i]=column[i].replace('.','_')

        data.columns=column

        result=data.to_json(orient='records')

        return result
