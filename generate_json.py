import json
import random


def main():
    generate_json()
    pick_weekly_exercises('config.json')


def generate_exercise_json(name, *args, **kwargs):
    last = kwargs.get('last', False)
    txt = f'\"{name}\": ' + '{'

    i = 1
    for arr in args:
        dur_type, dur_list = list(arr.items())[0]
        txt += f'\"{dur_type}\": ' + str(dur_list)
        if i != len(args):
            txt += ','
        i += 1
    txt += '}'
    if not last:
        txt += ','

    return txt


def generate_json():
    txt = '{' + f'\"exercises\": ' + '{'

    txt += generate_exercise_json('run', {"minutes": [duration for duration in range(30, 150, 30)]},
                                         {"miles": [distance for distance in range(2, 16)]})

    txt += generate_exercise_json('walk', {"minutes": [duration for duration in range(30, 150, 30)]},
                                          {"miles": [distance for distance in range(2, 16)]})

    txt += generate_exercise_json('swim', {"minutes": [duration for duration in range(30, 150, 30)]},
                                          {"miles": [int(distance/10) if float(distance/10).is_integer() else distance/10 for distance in range(5, 40, 5)]})

    txt += generate_exercise_json('pushup', {"times": [duration for duration in range(50, 100, 10)]})

    txt += generate_exercise_json('situps', {"times": [duration for duration in range(50, 200, 10)]})

    txt += generate_exercise_json('squats', {"times": [duration for duration in range(50, 200, 10)]})

    txt += generate_exercise_json('plank', {"minutes": [duration for duration in range(5, 25, 5)]})

    txt += generate_exercise_json('wall sit', {"minutes": [duration for duration in range(2, 11)]})

    txt += generate_exercise_json('lunge', {"times": [duration for duration in range(50, 450, 50)]})

    txt += generate_exercise_json('burpee', {"times": [duration for duration in range(50, 450, 50)]})

    txt += generate_exercise_json('russian twist', {"times": [duration for duration in range(50, 450, 50)]})

    txt += generate_exercise_json('try a new sport')

    txt += generate_exercise_json('participate in a public fitness event (5K, Bike Race, etc.)')

    txt += generate_exercise_json('go to the gym', {"times": [time for time in range(1, 5)]})

    txt += generate_exercise_json('walk a pet', {"times": [time for time in range(1, 8)]})

    txt += generate_exercise_json('climb stairs for', {"minutes": [duration * 10 for duration in range(2, 7)]})

    txt += generate_exercise_json('stretch for', {"minutes": [duration * 10 for duration in range(2, 7)]})

    txt += generate_exercise_json('do a calisthenics workout')

    txt += generate_exercise_json('lift weights for', {"minutes": [duration * 10 for duration in range(2, 7)]})

    txt += generate_exercise_json('jump rope for', {"minutes": [duration * 10 for duration in range(2, 7)]})

    txt += generate_exercise_json('bike', {"minutes": [duration for duration in range(30, 150, 30)]},
                                          {"miles": [distance for distance in range(20, 160, 10)]})

    txt += generate_exercise_json('hike', {"minutes": [duration for duration in range(30, 150, 30)]}, last = True)

    txt += '}}'
    with open('config.json', 'w') as f:
        f.write(txt)
        f.close()
    return txt


def pick_exercise(file):
    with open(file, 'r') as f:
        file_json = f.read()
        dic = json.loads(file_json)
        distance = dur_type = ''
        exercise_name, exercise_duration = random.choice(list(dic.get('exercises').items()))
        if exercise_duration:
            dur_type, dur_values = random.choice(list(exercise_duration.items()))
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


if __name__ == '__main__':
    main()
