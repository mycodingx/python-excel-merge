import pandas as pd
import os
import uuid


inputPath = os.getcwd() + '\sheets'
files = os.listdir(inputPath)

files_xlsx = [f for f in files if f[-4:] == 'xlsx']

df = pd.DataFrame()

for f in files_xlsx:
    data = pd.read_excel(inputPath + '\\' + f)
    df = df.append(data)

outputPath = os.getcwd() + '\output\\'
unique_filename = str(uuid.uuid4())
df.to_excel(outputPath + unique_filename + ".xlsx")
