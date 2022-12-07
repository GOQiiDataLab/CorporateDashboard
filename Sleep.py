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
                        AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
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

        cursor.execute(query1)
        ready_data = cursor.fetchall()
        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Log Date', 'Sleep Duration'])

        duration = dataframe['Sleep Duration'].mean() * 60
        hours = duration / 3600
        minutes = ((duration-(hours*3600)) % 3600)/60

        if len(str(int(hours))) == 1:
            h = "0" + str(str(int(hours)))
        else:
            h = hours

        if len(str(int(minutes))) == 1:
            m = "0" + str(str(int(minutes)))
        else:
            m = minutes

        return h + "h" + " " + m + "m"

    except Exception as exc:
        print(exc)
