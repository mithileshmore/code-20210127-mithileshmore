"""Provides test data for bmi calc."""

sample_data = [
    {
        "Gender":"Male",
        "HeightCm":175,
        "WeightKg":75
   }
]

sample_data_with_bmi = [
    {
        "Gender":"Male",
        "HeightCm":175,
        "WeightKg":75,
        "bmi": 24.49
   }
]

summarized_data_return_data = {
    'count_under_weight': 0,
    'count_normal_weight': 1,
    'count_over_weight': 0,
    'count_mod_obese': 0,
    'count_sev_obese': 0,
    'count_very_sev_obese': 0
}
