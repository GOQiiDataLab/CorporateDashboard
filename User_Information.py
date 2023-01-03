import json

import Database
import pandas as pd
import numpy as np
import datetime


def user_information():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT 
                    u.userid AS Userid, 
                    CONCAT(u.firstName," ", u.lastName) AS Player_Name,
                    u.userImageUrl AS User_Image,
                    rd.lifestyle AS Lifestyle,
                    rd.rollingPoints AS Rolling_Points,
                    rd.lifeStyleLastChangeDate AS Lifestyle_Change_Date,
                    DATEDIFF(NOW(), rd.lifeStyleLastChangeDate) AS Days_in_Elite,
                    rd.lastActiveDate AS Last_Active_Date, 
                    c.clanId AS ClanID,
                    c.clanName AS Clan_Name 
                FROM 
                    goqii_user u
                    INNER JOIN goqii_user_lifestyle_ready_data rd
                    ON u.userid = rd.userid
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON u.userid = cr.friendid
                    INNER JOIN goqii_clan c
                    ON cr.clanId = c.clanId
                WHERE 
                    c.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                    AND rd.isDeleted = "N"
                    AND cr.isDeleted = "N"
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Player_Name',
                                'User_Image', 'Lifestyle', 'Rolling_Points', 'Lifestyle_Change_Date',
                                'Days_in_Elite', 'Last_Active_Date', 'ClanID', 'Clan_Name'])

        safe = ['elite', 'fit', 'active', 'sedentary']
        lifestyle_players = {}
        for i in safe:
            if dataframe[dataframe['Lifestyle'] == i]['UserID'].count() > 0:
                lifestyle_players[i] = dataframe[dataframe['Lifestyle'] == i]['UserID'].count()
            else:
                lifestyle_players[i] = 0
        lifestyle_players = pd.DataFrame.from_dict(lifestyle_players, orient="index").reset_index()
        lifestyle_players.columns = ['Lifestyle','UserID']
        lifestyle_players.Lifestyle = lifestyle_players.Lifestyle.str.capitalize()

        player_count = dataframe.shape[0]

        most_active_players = dataframe.nlargest(3, 'Rolling_Points')[['User_Image', 'Player_Name', 'Lifestyle']]

        active_24_hours = dataframe[dataframe['Last_Active_Date'] >
                    np.datetime64(datetime.datetime.now().date()-pd.to_timedelta(1, unit='d'))]['UserID'].count()

        new_elites = dataframe[dataframe['Lifestyle'] == 'elite'].nlargest(3, 'Lifestyle_Change_Date')[
            ['User_Image', 'Player_Name', 'Lifestyle', 'Clan_Name', 'Lifestyle_Change_Date']]

        consistent_elites = dataframe[dataframe['Lifestyle'] == 'elite'].nlargest(3, 'Days_in_Elite')[
            ['User_Image', 'Player_Name', 'Lifestyle', 'Clan_Name', 'Lifestyle_Change_Date']]

        clan_player_count = dataframe.groupby('Clan_Name').UserID.count()

        elite_perc = dataframe.groupby('Clan_Name').apply(lambda x: (x[x['Lifestyle'] == 'elite'].
            count()/x['UserID'].count())*100)['UserID'].reset_index()

        best_performing_clan = elite_perc[elite_perc['UserID'] == elite_perc['UserID'].max()].values[0][0]

        under_performing_clan = elite_perc[elite_perc['UserID'] == elite_perc['UserID'].min()].values[0][0]

        return str(player_count), most_active_players.to_json(), lifestyle_players.to_json(), str(active_24_hours), \
               new_elites.to_json(), consistent_elites.to_json(), clan_player_count.to_json(), \
               best_performing_clan, under_performing_clan

    except Exception as exc:
        print(exc)
