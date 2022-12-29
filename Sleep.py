import json

import Database
import pandas as pd


def sleep():
    h = ""
    m = ""
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                    userId,
                    Log_Date,
                    AVG(Sleep_Duration) AS Sleep_Duration
                FROM
                    (
                    SELECT 
                        sd.userid AS UserID,
                        sd.logDate AS Log_Date,
                        sd.totalSleep AS Sleep_Duration
                    FROM 
                        goqii_user_sleep_data sd
                        INNER JOIN goqii_friend_user_clan_rel cr
                        ON sd.userid = cr.friendId
                    WHERE
                        sd.logDate >= (NOW()-INTERVAL 7 DAY)
                        AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                        AND sd.isDeleted = "N"
                    UNION ALL 
                    SELECT
                        ls.userid AS UserID,
                        ls.logDate AS Log_Date,
                        ls.duration AS Sleep_Duration
                    FROM
                        goqii_log_sleep ls
                        INNER JOIN goqii_friend_user_clan_rel cr
                        ON ls.userid = cr.friendId
                    WHERE
                        ls.logDate >= (NOW()-INTERVAL 7 DAY)
                        AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                        AND ls.isDeleted = "N"
                   ) u
                GROUP BY
                    userId,
                    Log_Date
                 '''

        query2 = '''
                SELECT 
                    sd.sleepObservation,
                    COUNT(sd.userId) AS user_count
                FROM 
                    goqii_user_sleep_data sd
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON sd.userid = cr.friendId
                WHERE
                    sd.logDate >= (NOW()-INTERVAL 8 DAY) AND sd.logDate < NOW()-1
                    AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND sd.isDeleted = "N"
                GROUP BY 
                    sd.sleepObservation
                '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()
        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Log Date', 'Sleep Duration'])

        cursor.execute(query2)
        ready_data = cursor.fetchall()
        sleep_quality = pd.DataFrame(data=ready_data, columns=['sleepObservation', 'user_count'])

        duration = dataframe['Sleep Duration'].mean() * 60
        hours = int(duration / 3600)
        minutes = int(((duration-(hours*3600))%3600)/60)

        if len(str(hours)) == 1:
            h = "0" + str(hours)
        else:
            h = str(hours)

        if len(str(minutes)) == 1:
            m = "0" + str(minutes)
        else:
            m = str(minutes)

        # sleep_quality_dict = {}
        # for i in range(len(sleep_quality)):
        #     sleep_quality_dict[sleep_quality['sleepObservation'][i]] = str(sleep_quality['user_count'][i])
        #
        # return (h + "h" + " " + m + "m"), json.dumps(sleep_quality_dict)

        return (h + ":" + m), sleep_quality.to_json()

    except Exception as exc:
        print(exc)