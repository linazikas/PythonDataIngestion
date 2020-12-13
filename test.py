import pandas as pd
df = pd.read_csv (r'Documents/LinkedIn Learning/Ex_Files_Data_Ingestion_Python/Exercise Files/Ch02/Challenge/taxi.csv.bz2')
df.to_json (r'Documents\LinkedIn Learning\Ex_Files_Data_Ingestion_Python\Exercise Files\Ch02\Test.json')