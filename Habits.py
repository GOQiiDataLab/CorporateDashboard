import Database


def habits():
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

        return ready_data[0][0]

    except Exception as exc:
        print(exc)