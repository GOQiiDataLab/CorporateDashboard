from flask import Flask
import Activity
import Distince_Walked
import Water_Intake
import Habits
import Sleep
import HRA
import Karma
import User_Information
import HealthAwareness

# init app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get():
    activity_time, top_activities = Activity.activity()
    distance_walked, average_steps, avg_steps_last_week, week_over_week, steps_distribution = Distince_Walked.distance_walked()
    water_card, water_kpi = Water_Intake.water_intake()
    habits = Habits.habits()
    avg_sleep, sleep_quality  = Sleep.sleep()
    hra = HRA.hra()
    karma = Karma.karma()
    player_count, top_active_players = User_Information.user_information()
    health_awareness = HealthAwareness.health()

    main_return = {'activity_time': activity_time, 'distance_walked': distance_walked, 'water_card': water_card,
                   'water_KPI': water_kpi, 'habits': habits, 'avg_sleep': avg_sleep, 'hra': hra, 'karma': karma,
                   'average_steps': average_steps, 'week_over_week': week_over_week,
                   'steps_distribution': steps_distribution, 'top_activities': top_activities,
                   'player_count': player_count, 'top_active_players': top_active_players,
                   'health_awareness': health_awareness, 'sleep_quality': sleep_quality,
                   'avg_steps_last_week': avg_steps_last_week}

    return main_return


if __name__ == '__main__':
    app.run(debug=True)

# Things let to code:
# 2. Quality of nutrition
# 4. Average Sleep Score correction