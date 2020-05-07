import pandas as pd
from datetime import datetime
import operator

def load(path):
    df = pd.read_csv(path)
    return df

def q1(path):
    """
     We filter the rows of country BDV. Then we group the results by site_id and afterwards
     aggregate by unique user_id. In the end we find the row(site) with max user count and print it.
    """
    df = load(path)
    df_bdv = df.loc[df['country_id'] == "BDV"]  # Filter all rows where country is BDV
    grouped_df = df_bdv.groupby("site_id")  # Group results by site_id
    grouped_df = grouped_df.agg({"user_id": "nunique"})  # Aggregate for unique user_ids
    grouped_df = grouped_df.reset_index()
    print(grouped_df.iloc[grouped_df["user_id"].argmax()])  # Print the row with max user_id

    # site_id    5NPAU
    # user_id      544

def q2(path):
    """
    We convert the timestamps to a datetime format. We select a subset of the original set in range of the two timestamps.
    We group the dataset by user_id and site_id, and count.
    In the end, we select those with more than 10 visits and print.
    """
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
    """
    First, we find all the unique users. We create a dictionary sites -> number of users.
    For each user, select the parts of the original dataframe relevant to that user; find the max time stamp; select that site.
    If the site is not in the dictionary, we add it with count 1 as the value. If it is there, we increase the value by 1.
    In the end, we sort the list of sites and counts, and print it.
    """
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
    """
    First, we find a list of unique users. We create dictionaries user:site for the first and last site.
    We iterate through the list of unique users. For each user, select the parts of the original dataframe relevant to that user;
    select the site corresponding to the row with the lowest timestamp and append that in the first site dictionary. Repeat the same
    with the highest time stamp.
    In the end, loop through the dictionaries with users as keys. If the first and last site are the same, increase the count variable.
    """

    df = load(path)
    users = set(df["user_id"])  # Find all unique users
    user_firstsite = {} #Dictionary of users -> first site
    user_lastsite = {} #Dictionary of uesrs -> last site

    for user in users:
        user_df = df.loc[df["user_id"] == user]
        first_site = user_df.loc[user_df['ts'] == min(user_df['ts'])]['site_id']._ndarray_values[0]
        last_site = user_df.loc[user_df['ts'] == max(user_df['ts'])]['site_id']._ndarray_values[0] # Last site accessed by user

        #Add it in the dict
        user_lastsite[user] = last_site
        user_firstsite[user] = first_site

    count = 0
    for user in users:
        if(user_firstsite[user] == user_lastsite[user]): count = count + 1

    print(count)
    #1670

if __name__ == '__main__':
    q4("Data/user_website_data.csv")