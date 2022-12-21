import Database


def food():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                    Count(h.habitid)
                FROM
                    goqii_user_habits h
                    INNER JOIN goqii_user_habit_log hl
                    ON h.masterhabitid = hl.habitId
                    AND h.userID = hl.userId
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON h.userid = cr.friendId
                    AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                    AND cr.isDeleted = "N"
                WHERE
                    hl.logTime >= (NOW()-INTERVAL 1 Week)
                    AND hl.isDeleted = 'N'
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()
        print(ready_data[0][0])

        return ready_data[0][0]

    except Exception as exc:
        print(exc)


def getHealthyPercentage():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                Round(
                sum(if(f.healthmeterCategory='healthy',1,0)) ,
                sum(if(f.healthmeterCategory='unhealthy'||f.healthmeterCategory='healthy',1,0))) healthy_perc
                FROM
                    goqii_log_food f
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON f.userid = cr.friendId
                    #AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                    AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                    AND cr.isDeleted = "N"
                    AND f.isDeleted = "N"
                WHERE	
                    f.logDate >= (NOW()-INTERVAL 7 DAY)
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()
        print(ready_data[0][0])

        return ready_data[0][0]

    except Exception as exc:
        print(exc)



