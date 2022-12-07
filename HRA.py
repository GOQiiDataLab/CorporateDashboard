import Database


def hra():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT 
                    Round(avg(hraScore),0)
                FROM 
                    goqii_user_hra_data h
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON h.userid = cr.friendId
                    AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND cr.isDeleted = "N"
                    AND h.isDeleted = 'N'
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        return ready_data[0][0]

    except Exception as exc:
        print(exc)