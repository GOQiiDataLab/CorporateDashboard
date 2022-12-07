import Database
import pandas as pd
import numpy as np


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
                    c.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND rd.isDeleted = "N"
                    AND cr.isDeleted = "N"
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Player_Name',
                                'User_Image', 'Lifestyle', 'Rolling_Points', 'Lifestyle_Change_Date',
                                'Last_Active_Date', 'ClanID', 'Clan_Name'])

        player_count = dataframe.shape[0]
        most_active_players = dataframe.nlargest(3, 'Rolling_Points')[['User_Image', 'Player_Name', 'Lifestyle']]

        return player_count, most_active_players.to_json()

    except Exception as exc:
        print(exc)