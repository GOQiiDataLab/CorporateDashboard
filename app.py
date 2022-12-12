from flask import Flask, request,make_response
import Activity
import Distince_Walked
import Water_Intake
import Habits
import Sleep
import HRA
import Karma
import User_Information
import HealthAwareness
from flask import jsonify
# init app
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def get():
    res = make_response("Success", 200)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res

@app.route('/getdata', methods=['GET', 'POST'])
def getdata():
    activity_time, top_activities = Activity.activity()
    distance_walked, average_steps, avg_steps_last_week, week_over_week, steps_distribution = Distince_Walked.distance_walked()
    water_card, water_kpi = Water_Intake.water_intake()
    habits = Habits.habits()
    avg_sleep, sleep_quality = Sleep.sleep()
    hra = HRA.hra()
    karma = Karma.karma()
    player_count, top_active_players, lifestyle_players, active_24_hours, new_elites, consistent_elites = User_Information.user_information()
    health_awareness = HealthAwareness.health()

    main_return = {'activity_time': activity_time, 'distance_walked': distance_walked, 'water_card': water_card,
                   'water_KPI': water_kpi, 'habits': habits, 'avg_sleep': avg_sleep, 'hra': hra, 'karma': karma,
                   'average_steps': average_steps, 'week_over_week': week_over_week,
                   'steps_distribution': steps_distribution, 'top_activities': top_activities,
                   'player_count': player_count, 'top_active_players': top_active_players,
                   'lifestyle_players': lifestyle_players, 'active_24_hours': active_24_hours,
                   'new_elites': new_elites, 'consistent_elites': consistent_elites,
                   'health_awareness': health_awareness, 'sleep_quality': sleep_quality,
                   'avg_steps_last_week': avg_steps_last_week}

    print(main_return)

    res = make_response(main_return, 200)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res



@app.route('/user_information', methods=['GET', 'POST'])
def user_information():
    player_count, top_active_players, lifestyle_players, active_24_hours, new_elites, consistent_elites = User_Information.user_information()

    main_return = {
        'player_count': player_count,
        'top_active_players': top_active_players
        ,'lifestyle_players':lifestyle_players,
        'active_24_hours':active_24_hours,
        'new_elites':new_elites,
        'consistent_elites':consistent_elites
    }

    return main_return


if __name__ == '__main__':
    app.run(debug=True)

# Things let to code:
# 2. Quality of nutrition
# 4. Average Sleep Score correction
