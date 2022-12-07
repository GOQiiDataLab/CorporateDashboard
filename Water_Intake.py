import Database


def water_intake():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                    CONCAT(ROUND(SUM(Amount),0),' ltrs') AS Water_Card,
                    ROUND(AVG(Amount),2) AS Water_Intake_KPI
                FROM
                    (
                    SELECT
                        w.userId AS UserID,
                        w.logDate AS Log_Date,
                        SUM(w.amount*0.001) AS Amount,
                        SUM(w.quantity) AS Quantity
                    FROM
                        goqii_log_water w
                        INNER JOIN goqii_friend_user_clan_rel cr
                        ON w.userid = cr.friendId
                        AND cr.clanId IN (16069, 16071, 16072, 16073, 16075, 16077, 17489)
                        AND cr.isDeleted = "N"
                        AND w.isDeleted = "N"
                    WHERE	
                        w.logDate >= (NOW()-INTERVAL 7 DAY)
                    GROUP BY
                        w.userId,
                        w.logDate
                    ) a
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        return ready_data[0][0], str(ready_data[0][1])

    except Exception as exc:
        print(exc)