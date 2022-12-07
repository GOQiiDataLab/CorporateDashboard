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
                    AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND cr.isDeleted = "N"
                WHERE
                    logcreatedtime >= (NOW()-INTERVAL 1 WEEK)
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        return ready_data[0][0]

    except Exception as exc:
        print(exc)