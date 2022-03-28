import requests
import pandas as pd
apikey = "WnugwvU75RddvPG2NJh9wbarHU88ZyVgX4XL5EXV"
states = [ 'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY' ];
dataframe = pd.DataFrame()
for state in states:
    response = requests.get("https://api.eia.gov/series/?api_key={}&series_id=NG.N3010{}2.A".format(apikey, state))
    data = response.json()
    temp = pd.DataFrame(data['series'][0]['data'], columns=['year', 'consumption'])
    temp['State'] = ['AL']*len(data['series'][0]['data'])
    temp['Type'] = ['Natural Gas']*len(data['series'][0]['data'])
    dataframe.append(temp, ignore_index=True)