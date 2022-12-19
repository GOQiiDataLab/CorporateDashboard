import Database


def karma():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT 
                    SUM(userContribution)
                FROM 
                    goqii_userCauseRel c
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON c.userid = cr.friendId
                    AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                    AND cr.isDeleted = "N"
                WHERE
                    logcreatedtime >= (NOW()-INTERVAL 1 WEEK)
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        return ready_data[0][0]

    except Exception as exc:
        print(exc)