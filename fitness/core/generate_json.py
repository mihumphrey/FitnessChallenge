import json
import random
from django.contrib.auth.models import User
from .models import Activity

def generate_exercise(name, *args, weight = 3):
    return [{name: [arg for arg in args]}] * weight


def generate_json():
    dict = {}
    dict['exercises'] = []
    dict['exercises'].extend(generate_exercise('run', {"minutes": [duration for duration in range(30, 150, 30)]}, {"miles": [distance for distance in range(2, 16)]}))
    dict['exercises'].extend(generate_exercise('walk', {"minutes": [duration for duration in range(30, 150, 30)]}, {"miles": [distance for distance in range(2, 16)]}))
    dict['exercises'].extend(generate_exercise('swim', {"minutes": [duration for duration in range(30, 150, 30)]}, {"miles": [int(distance/10) if float(distance/10).is_integer() else distance/10 for distance in range(5, 40, 5)]}))
    dict['exercises'].extend(generate_exercise('pushup', {"times": [duration for duration in range(50, 100, 10)]}))
    dict['exercises'].extend(generate_exercise('situps', {"times": [duration for duration in range(50, 200, 10)]}))
    dict['exercises'].extend(generate_exercise('squats', {"times": [duration for duration in range(50, 200, 10)]}))
    dict['exercises'].extend(generate_exercise('plank', {"minutes": [duration for duration in range(5, 25, 5)]}))
    dict['exercises'].extend(generate_exercise('wall sit', {"minutes": [duration for duration in range(2, 11)]}))
    dict['exercises'].extend(generate_exercise('lunge', {"times": [duration for duration in range(50, 450, 50)]}))
    dict['exercises'].extend(generate_exercise('burpee', {"times": [duration for duration in range(50, 450, 50)]}))
    dict['exercises'].extend(generate_exercise('russian twist', {"times": [duration for duration in range(50, 450, 50)]}))
    dict['exercises'].extend(generate_exercise('participate in a public fitness event (5K, Bike Race, etc.)'))
    dict['exercises'].extend(generate_exercise('go to the gym', {"times": [time for time in range(1, 5)]}))
    dict['exercises'].extend(generate_exercise('walk a pet', {"times": [time for time in range(1, 8)]}))
    dict['exercises'].extend(generate_exercise('climb stairs for', {"minutes": [duration * 10 for duration in range(2, 7)]}))
    dict['exercises'].extend(generate_exercise('stretch for', {"minutes": [duration * 10 for duration in range(2, 7)]}))
    dict['exercises'].extend(generate_exercise('do a calisthenics workout'))
    dict['exercises'].extend(generate_exercise('lift weights for', {"minutes": [duration * 10 for duration in range(2, 7)]}))
    dict['exercises'].extend(generate_exercise('jump rope for', {"minutes": [duration * 10 for duration in range(2, 7)]}))
    dict['exercises'].extend(generate_exercise('bike', {"minutes": [duration for duration in range(30, 150, 30)]}, {"miles": [distance for distance in range(20, 160, 10)]}))
    dict['exercises'].extend(generate_exercise('hike', {"minutes": [duration for duration in range(30, 150, 30)]}))
    sports = ['baseball', 'football', 'basketball', 'volleyball', 'soccer', 'tennis', 'golf', 'table tennis', 'badminton', 'racquetball', 'pickleball', 'BJJ', 'wrestling', 'handball', 'surfing', 'bowling', 'shooting/hunting', 'canoeing', 'skiing/snowboarding', 'lacrosse']
    for sport in sports:
        dict['exercises'].extend(generate_exercise(f'try a sport: {sport}', weight = 1))


    with open('config.json', 'w') as f:
        f.write(json.dumps(dict))
        f.close()


def pick_exercise(file):
    with open(file, 'r') as f:
        file_json = f.read()
        dic = json.loads(file_json)
        distance = dur_type = ''
        exercise_name, exercise_duration = list(random.choice(dic.get('exercises')).items())[0]
        if exercise_duration:
            dur_type, dur_values = list(random.choice(exercise_duration).items())[0]
            distance = random.choice(dur_values)
    f.close()
    return exercise_name, distance, dur_type


def pick_weekly_exercises(file):
    num_exercises = 5
    exercise_names = []
    exercises = []
    for _ in range(num_exercises):
        while True:
            exercise_name, distance, dur_type = pick_exercise(file)
            if exercise_name in exercise_names:
                continue
            break
        exercise_names.append(exercise_name)
        exercises.append(exercise_name.title() + ' ' + str(distance) + ' ' + dur_type.title())
    for exercise in exercises:
        print(exercise)
        for user in User.objects.all():
            a = Activity()
            a.name = exercise
            a.user = user
            a.save()