import Database
import pandas as pd
import numpy as np


def health():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT 
                    t.userid,
                    t.taskKeyword,
                    t.type,
                    t.earnedPoints,
                    t.logDate
                FROM 
                    goqii_user_lifestyle_task_log t
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON t.userid = cr.friendId
                    AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395) 
                    AND cr.isDeleted = "N"
                    AND t.isDeleted = "N"
                WHERE
                    t.logdate >= (NOW()-INTERVAL 8 DAY) AND t.logDate < NOW()-1
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Task_Keyword', 'Type',
                                'Earned_Points', 'LogDate'])

        health_awareness = dataframe.groupby('Type').agg({'UserID': pd.Series.nunique})['UserID'].reset_index()
        health_awareness = health_awareness[health_awareness['Type'].isin(['sleep', 'nutrition', 'fitness',
                                                                         'cognition'])]
        health_awareness['Type'].replace('cognition', 'meditation', inplace=True)

        return health_awareness.to_json()

    except Exception as exc:
        print(exc)