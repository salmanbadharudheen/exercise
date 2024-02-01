def calculate_bmi(height, weight):
    height_in_meters = height / 100
    return weight / (height_in_meters ** 2)

def determine_age_group(age):
    lower_bound = int(age // 5) * 5
    upper_bound = lower_bound + 4.9
    return f"{lower_bound}-{upper_bound}"

def highest_average_bmi(data):
    age_groups = {}
    age_group_counts = {}

    for person in data:
        bmi = calculate_bmi(person['height'], person['weight'])
        age_group = determine_age_group(person['age'])

        if age_group not in age_groups:
            age_groups[age_group] = 0
            age_group_counts[age_group] = 0

        age_groups[age_group] += bmi
        age_group_counts[age_group] += 1

    max_average_bmi = 0
    max_age_group = ""

    for age_group in age_groups:
        average_bmi = age_groups[age_group] / age_group_counts[age_group]
        if average_bmi > max_average_bmi:
            max_average_bmi = average_bmi
            max_age_group = age_group

    return {'ageGroup': max_age_group, 'averageBmi': round(max_average_bmi, 2)}


print(highest_average_bmi([
    {'height': 175, 'weight': 50, 'age': 21},
    {'height': 170, 'weight': 77, 'age': 22},
    {'height': 175, 'weight': 70, 'age': 24},
    {'height': 175, 'weight': 75, 'age': 26},
    {'height': 175, 'weight': 50, 'age': 29},
    {'height': 170, 'weight': 77, 'age': 34}
]))

print(highest_average_bmi([
    {'height': 175, 'weight': 50, 'age': 24.9},
    {'height': 170, 'weight': 80, 'age': 25},
    {'height': 170, 'weight': 90, 'age': 29.9},
    {'height': 175, 'weight': 90, 'age': 32},
    {'height': 175, 'weight': 50, 'age': 39},
    {'height': 170, 'weight': 77, 'age': 44}
]))
