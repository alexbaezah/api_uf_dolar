import requests
import pandas as pd
url = "https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=186978803&pass=TjqSjcEQJ9kj&firstdate=2023-01-01&lastdate=2023-01-31&timeseries=F073.TCO.PRE.Z.D&function=GetSeries"
response = requests.get(url)
response = response.json()
response = response["Series"]["Obs"]

df_data = pd.DataFrame(response)
df_data.head() 

print(df_data)