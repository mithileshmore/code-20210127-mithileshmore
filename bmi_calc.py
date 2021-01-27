from data import data


def summarize_data(data):
    summarized_data = {
            'count_under_weight': 0,
            'count_normal_weight': 0,
            'count_over_weight': 0,
            'count_mod_obese': 0,
            'count_sev_obese': 0,
            'count_very_sev_obese': 0
        }
    for item in data:
        if item['bmi'] <= 18.4:
            summarized_data['count_under_weight'] += 1
        elif item['bmi'] >= 18.5 and item['bmi'] <= 24.9:
            summarized_data['count_normal_weight'] += 1
        elif item['bmi'] >= 25 and item['bmi'] <= 29.9:
            summarized_data['count_over_weight'] += 1
        elif item['bmi'] >= 30 and item['bmi'] <= 34.9:
            summarized_data['count_mod_obese'] += 1
        elif item['bmi'] >= 35 and item['bmi'] <= 39.9:
            summarized_data['count_sev_obese'] += 1
        elif item['bmi'] >= 40:
            summarized_data['count_very_sev_obese'] += 1
    return summarized_data


def calculate_bmi(data):
    for item in data:
        item['bmi'] = round(item['WeightKg'] / ((item['HeightCm'] / 100) * (item['HeightCm'] / 100)), 2)


if __name__ == '__main__':
    print("Let's calculate BMIs!\n")
    calculate_bmi(data)
    summarized_data = summarize_data(data)
    print('Summary of the records given:-\n')
    print(f"Total underweight people: {summarized_data['count_under_weight']} \n"
        f"Total normal weighted people: {summarized_data['count_normal_weight']} \n"
        f"Total over weighted people: {summarized_data['count_over_weight']} \n"
        f"Total moderately obese people: {summarized_data['count_mod_obese']} \n"
        f"Total severe obese people: {summarized_data['count_sev_obese']} \n"
        f"Total very severe obese people: {summarized_data['count_very_sev_obese']}"
    )
