scenarios = [
    # Scenario 1
    {
        'p_values': [0.5] * 9,
        'one_minus_p_values': [0.5] * 9,
        'x1_l_values': [-13.95, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60],
        'x1_h_values': [0.05, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
        'x2_h_values': [0.05, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
        'x2_l_values': [-13.95, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60]
    },

    # Scenario 2
    {
        'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
        'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
        'x1_l_values': [-8.60, -6.00, -4.71, -4.02, -3.41, -2.92, -2.53, -2.11, -1.68],
        'x1_h_values': [0.08, 0.51, 0.97, 1.30, 1.80, 2.40, 3.15, 4.40, 7.00],
        'x2_h_values': [3.00, 1.80, 1.50, 1.35, 1.00, 0.70, 0.50, 0.25, 0.05],
        'x2_l_values': [-5.60, -4.65, -4.13, -3.92, -4.16, -4.57, -5.13, -6.20, -8.55]
    },

    # Scenario 3
    {
        'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
        'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
        'x1_l_values': [-8.50, -6.00, -4.70, -4.00, -3.40, -2.90, -2.53, -2.10, -1.70],
        'x1_h_values': [0.09, 0.50, 0.97, 1.30, 1.80, 2.40, 3.15, 4.40, 6.96],
        'x2_h_values': [8.00, 7.00, 6.00, 5.00, 4.00, 3.00, 2.00, 1.00, 0.05],
        'x2_l_values': [-20.00, -14.00, -12.30, -12.10, -12.80, -14.10, -16.30, -20.00, -28.00]
    },

    # Scenario 4
    {
        'p_values': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9],
        'one_minus_p_values': [0.9, 0.8, 0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1],
        'x1_l_values': [-25.00, -17.60, -14.00, -11.80, -10.10, -8.70, -7.50, -6.30, -5.10],
        'x1_h_values': [0.01, 1.20, 2.40, 3.60, 4.90, 6.60, 8.90, 12.50, 20.00],
        'x2_h_values': [8.00, 7.00, 6.00, 5.00, 4.00, 3.04, 2.00, 1.00, 0.50],
        'x2_l_values': [-20.00, -14.00, -12.30, -12.10, -12.80, -14.10, -16.30, -20.00, -27.50]
    },

    # Scenario 5
    {
        'p_values': [0.5] * 9,
        'one_minus_p_values': [0.5] * 9,
        'x1_l_values': [-7.60] * 9,
        'x1_h_values': [6.40] * 9,
        'x2_h_values': [0.10, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
        'x2_l_values': [-13.90, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60]
    }
]


def analyze_scenarios(scenarios):
    combinations = set()
    repeats = []

    for scenario_index, scenario in enumerate(scenarios, 1):
        for round_index in range(9):
            l1 = (
                round(scenario['x1_l_values'][round_index], 2),
                round(scenario['x1_h_values'][round_index], 2)
            )
            l2 = (
                round(scenario['x2_l_values'][round_index], 2),
                round(scenario['x2_h_values'][round_index], 2)
            )
            combination = (l1, l2)

            if combination in combinations:
                repeats.append((scenario_index, round_index + 1, combination))
            else:
                combinations.add(combination)

    return repeats


repeating_combinations = analyze_scenarios(scenarios)

print("Repeating L1, L2 combinations:")
for repeat in repeating_combinations:
    scenario, round_num, combination = repeat
    print(f"Scenario {scenario}, Round {round_num}: {combination}")

if not repeating_combinations:
    print("No repeating L1, L2 combinations found across the 45 rounds.")