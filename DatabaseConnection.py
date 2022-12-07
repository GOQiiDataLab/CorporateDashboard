from flask import Flask
import Activity
import Distince_Walked
import Water_Intake
import Habits
import Sleep
import HRA
import Karma
import User_Information

# init app
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def get():
    activity_time, top_activities = Activity.activity()
    distance_walked, average_steps, week_over_week, steps_distribution = Distince_Walked.distance_walked()
    water_card, water_kpi = Water_Intake.water_intake()
    habits = Habits.habits()
    sleep = Sleep.sleep()
    hra = HRA.hra()
    karma = Karma.karma()
    player_count, top_active_players = User_Information.user_information()

    main_return = {'activity_time': activity_time, 'distance_walked': distance_walked, 'water_card': water_card,
                   'water_KPI': water_kpi, 'habits': habits, 'sleep': sleep, 'hra': hra, 'karma': karma,
                   'average_steps': average_steps, 'week_over_week': week_over_week,
                   'steps_distribution': steps_distribution, 'top_activities': top_activities,
                   'player_count': player_count, 'top_active_players': top_active_players}

    return main_return


if __name__ == '__main__':
    app.run(debug=True)

# Things let to code:
# 1. Sleep KPI
# 2. Health Awareness
# 3. Quality of nutrition
# 4. Last week steps and percentage change
# 5. Average Sleep Score correction