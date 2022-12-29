from flask import Flask, request, make_response
import Activity
import Distince_Walked
import Water_Intake
import Habits
import Sleep
import HRA
import Karma
import User_Information
import HealthAwareness
import Food
import json
import enc_dec_demo
import codecs
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
    args = request.args.get("e")

    activity_time, top_activities = Activity.activity()
    distance_walked, average_steps, avg_steps_last_week, week_over_week, steps_distribution = Distince_Walked.distance_walked()
    water_card, water_kpi = Water_Intake.water_intake()
    habits = Habits.habits()
    avg_sleep, sleep_quality = Sleep.sleep()
    hra = HRA.hra()
    karma = Karma.karma()
    player_count, top_active_players, lifestyle_players, active_24_hours, new_elites, \
    consistent_elites, clan_player_count, best_performing_clan, \
    under_performing_clan = User_Information.user_information()
    health_awareness = HealthAwareness.health()
    healthy_perc = int(Food.getHealthyPercentage())
    h_per = {"healthy_perc": str(healthy_perc), "unhealthy_perc": str(100 - healthy_perc)}
    json_h_perc = json.dumps(h_per)
    main_return = {"activity_time": activity_time, "distance_walked": distance_walked, "water_card": water_card,
                   "water_KPI": water_kpi, "habits": habits, "avg_sleep": avg_sleep, "hra": hra, "karma": karma,
                   "average_steps": average_steps, "week_over_week": week_over_week,
                   "steps_distribution": steps_distribution, "top_activities": top_activities,
                   "player_count": player_count, "top_active_players": top_active_players,
                   "lifestyle_players": lifestyle_players, "active_24_hours": active_24_hours,
                   "new_elites": new_elites, "consistent_elites": consistent_elites,
                   "clan_player_count": clan_player_count, "best_performing_clan": best_performing_clan,
                   "under_performing_clan": under_performing_clan, "health_awareness": health_awareness,
                   "sleep_quality": sleep_quality,
                   "avg_steps_last_week": avg_steps_last_week,
                   "healthy_percentage": json_h_perc
                   }
    main_return = json.dumps(main_return)
    if args == 'f':
        res = {"data": main_return}

    else:
        res = {"data": (enc_dec_demo.encrypt_message(main_return))}

    # str(enc_dec_demo.encrypt_message(main_return))
    res = make_response(res, 200)
    res.headers['Access-Control-Allow-Origin'] = "*"
    return res


@app.route('/user_information', methods=['GET', 'POST'])
def user_information():
    player_count, top_active_players, lifestyle_players, active_24_hours, new_elites, consistent_elites = User_Information.user_information()

    main_return = {
        'player_count': player_count,
        'top_active_players': top_active_players,
        'lifestyle_players': lifestyle_players,
        'active_24_hours': active_24_hours,
        'new_elites': new_elites,
        'consistent_elites': consistent_elites
    }

    return main_return


@app.route('/posttest', methods=['POST'])
def postTest():
    data = request.data
    # print(data.data)
    d = codecs.decode(data, 'UTF-8')
    # (json.loads(d))['data']
    # res = {"data": enc_dec_demo.decrypt_message((json.loads(d))['data'])}
    res = enc_dec_demo.decrypt_message((json.loads(d))['data'])
    res = json.dumps(res)
    res = {"data": res}

    print(res)
    res = make_response(res, 200)
    res.headers['Access-Control-Allow-Origin'] = "*"
    res.headers['Content-Type'] = "application/json"

    return res


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host='0.0.0.0', port=81)
