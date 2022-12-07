import Database
import pandas as pd
import numpy as np


def activity():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                    a.userId AS UserID,
                    a.Name AS Activity_Name,
                    COUNT(*) AS Number_Of_Times_Activity_Done,
                    SUM(a.duration) AS Duration,
                    SUM(a.duration/60) AS Duration_Hours
                FROM
                    goqii_userActivityRel a
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON a.userid = cr.friendId
                    AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND cr.isDeleted = "N"
                    AND a.isDeleted = "N"
                WHERE
                    a.logDate >= (NOW()-INTERVAL 7 DAY)
                GROUP BY
                    a.userId,
                    a.Name
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Activity_Name',
                                'Number_Of_Times_Activity_Done', 'Duration', 'Duration_Hours'])

        activity_time = str(np.round(dataframe['Duration_Hours'].sum(), 0)) + ' hrs'
        top_activities = dataframe.groupby('Activity_Name').agg({'Number_Of_Times_Activity_Done': 'sum'})['Number_Of_Times_Activity_Done'].nlargest(5).reset_index()

        return activity_time, top_activities.to_json()

    except Exception as exc:
        print(exc)