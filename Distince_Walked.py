import Database
import pandas as pd
import numpy as np
import datetime


def distance_walked():
    try:
        db = Database.database()
        cursor = db.cursor()

        query1 = '''
                SELECT
                    cc.userid,
                    cc.deviceSteps,
                    cc.logDate
                FROM	
                    goqii_cumulative_count cc
                    INNER JOIN goqii_friend_user_clan_rel cr
                    ON cc.userid = cr.friendId
                    AND cr.clanId IN (19388, 19389, 19390, 19391,19392,19396,19395)
                    AND cr.isDeleted = "N"
                WHERE 
                    logDate >= (NOW()-INTERVAL 4 MONTH) AND logDate < NOW() - 1  
                 '''

        cursor.execute(query1)
        ready_data = cursor.fetchall()

        dataframe = pd.DataFrame(data=ready_data, columns=['UserID', 'Steps', 'Log Date'])
        dataframe['Week'] = pd.to_datetime(dataframe['Log Date'], errors='coerce').dt.isocalendar().week
        dataframe['Log Date'] = pd.to_datetime(dataframe['Log Date'])
        dataframe['Steps'] = np.round(pd.to_numeric(dataframe['Steps'])/1350, 0)

        steps_distribution = dataframe[dataframe['Log Date'] >= np.datetime64(datetime.datetime.now().date() -
            pd.to_timedelta(6, unit='d'))].groupby('UserID').agg({'Steps': 'sum'}).reset_index()

        def category(x):
            if x < 10:
                return 'Less than 10km'
            elif 10 <= x < 30:
                return '10km to 30km'
            elif 30 <= x < 50:
                return '30km to 50km'
            else:
                return 'Above 50km'

        steps_distribution['category'] = steps_distribution['Steps'].apply(category)

        steps_distribution = steps_distribution.groupby('category').agg({'UserID': 'count'}).reset_index()

        km_walked_week_over_week = dataframe[dataframe['Log Date'] >= np.datetime64(datetime.datetime.now().date()
            - pd.to_timedelta(14, unit='w'))].groupby('Week').agg({'Steps': 'sum'}).reset_index()

        steps = int((dataframe[dataframe['Log Date'] >= np.datetime64(
            datetime.datetime.now().date()-pd.to_timedelta(1, unit='w'))]['Steps']).sum())

        avg_steps = np.round(steps / dataframe[dataframe['Log Date'] >= np.datetime64(
            datetime.datetime.now().date()-pd.to_timedelta(1, unit='w'))]['UserID'].nunique(), 2)

        steps_last_week = dataframe[(dataframe['Log Date'] >= np.datetime64(datetime.datetime.now().date()-pd.to_timedelta(2, unit='w')))
            & (dataframe['Log Date'] < np.datetime64(datetime.datetime.now().date()-pd.to_timedelta(1, unit='w')))]['Steps'].sum()

        avg_steps_last_week = np.round(steps_last_week / dataframe[
        (dataframe['Log Date'] >= np.datetime64(datetime.datetime.now().date() - pd.to_timedelta(2, unit='w')))
        & (dataframe['Log Date'] < np.datetime64(datetime.datetime.now().date() - pd.to_timedelta(1, unit='w')))]['UserID'].nunique(), 2)

        return str(steps), str(np.round(avg_steps, 1)), str(np.round(avg_steps_last_week, 1)), \
               km_walked_week_over_week.to_json(), steps_distribution.to_json()

    except Exception as exc:
        print(exc)
