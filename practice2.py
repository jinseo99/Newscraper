import pandas as pd 
#csv_path = "csv_files/googlenews_results_03+49_06-04-2020.csv"
csv_path = "test_csv/googlenews_results_03+18_06-04-2020.csv"
df = pd.read_csv(csv_path)
print('reading ', csv_path)
print("number of rows ",df.shape[0])

#pd.set_option('max_colwidth', 800)
print(df.tail()[['title','date','link']].to_string())