import pandas as pd
from datetime import datetime
import operator

def load(path):
    df = pd.read_csv(path)
    return df

def q1(path):
    df = load(path)
    df_bdv = df.loc[df['country_id'] == "BDV"]  # Filter all rows where country is BDV
    grouped_df = df_bdv.groupby("site_id")  # Group results by side_id
    grouped_df = grouped_df.agg({"user_id": "nunique"})  # Aggregate for unique user_ids
    grouped_df = grouped_df.reset_index()
    print(grouped_df.iloc[grouped_df["user_id"].argmax()])  # Print the row with max user_id

    # site_id    5NPAU
    # user_id      544

def q2(path):
    df = load(path)
    df["ts"] = pd.to_datetime(df["ts"]) #Convert ts to dataframe
    ts_from = datetime.fromisoformat("2019-02-03 00:00:00")
    ts_to = datetime.fromisoformat("2019-02-04 23:59:59")
    mask = (df["ts"] >= ts_from) & (df["ts"] <= ts_to) #Create range
    df_inrange = df.loc[mask] #Select only the rows where ts is in range

    grouped = df_inrange.groupby(["user_id","site_id"]).size() #Group by user_id and site_id and count
    grouped = grouped.reset_index()

    print(grouped.loc[grouped[0] > 10] ) #Select those with count >10

    # 3    LC06C3   N0OTG  25
    # 417  LC3A59   N0OTG  26
    # 485  LC3C7E   3POLC  15
    # 493  LC3C9D   N0OTG  17

def q3(path):
    df = load(path)
    users = set(df["user_id"]) #Find all unique users
    sites_count = {} #Dictionary of sites and how many users have their last visit there
    for user in users:
        user_df = df.loc[df["user_id"] == user]
        last_site = user_df.loc[user_df['ts'] == max(user_df['ts'])]['site_id']._ndarray_values[0] #Last site accessed by user
        if(last_site in sites_count.keys()):
            sites_count[last_site] = sites_count[last_site] + 1 #Add to dictionary
        else:
            sites_count[last_site] = 1

    sorted_x = sorted(sites_count.items(), key=operator.itemgetter(1))[::-1] #Sort the dictonary
    print(sorted_x)

    # [('5NPAU', 992), ('N0OTG', 561), ('QGO3G', 289), ('GVOFK', 42), ('3POLC', 28), ('RT9Z6', 2), ('JSUUP', 1), ('EUZ/Q', 1)]



def q4(path):
    df = load(path)

if __name__ == '__main__':
    q3("Data/user_website_data.csv")