from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range
)
import random




class Player(BasePlayer):


    # Consent form fields
    consent_age = models.BooleanField(
        label="I am 18 years of age or older."
    )
    consent_read = models.BooleanField(
        label="I have read and understand the information above."
    )
    consent_participate = models.BooleanField(
        label="I want to participate in this research and continue with the study."
    )

    # Survey fields
    age_check = models.BooleanField(
        label="Are you 18 years of age or older?",
        choices=[
            [True, 'Yes'],
            [False, 'No'],
        ]
    )
    gender = models.StringField(
        label="What gender do you identify as?",
        choices=['Female', 'Non-binary', 'Male'],
        widget=widgets.RadioSelect
    )
    career = models.StringField(label="What is your major?")
    native_language = models.StringField(label="What is your native language?")
    university_year = models.StringField(label="What year are you in university?",
                                         choices=['First year', 'Second year', 'Third year', 'Fourth year', 'Graduate',
                                                  'Other'], widget=widgets.RadioSelect)
    gpa = models.FloatField(label="What is your current GPA? (0-4, up to 4 decimal places)", min=0, max=4)
    smoker = models.StringField(
        label="Are you a smoker?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )
    alcohol = models.StringField(
        label="Do you practice excessive alcohol consumption?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )
    drugs = models.StringField(
        label="Do you use recreational drugs?",
        choices=[['Yes', 'Yes'], ['No', 'No'], ['Prefer not to answer', 'Prefer not to answer']],
        widget=widgets.RadioSelect
    )

    weekly_spending = models.IntegerField(label="What is your weekly spending in USD?")

    # Cognitive Reflection Test
    crt_linda = models.StringField(
        label="Which of the following two alternatives is more likely?",
        choices=[
            'Linda is a bank teller.',
            'Linda is a bank teller and active in the feminist movement.'
        ],
        widget=widgets.RadioSelect
    )
    crt_bat = models.FloatField(label="How much does the ball cost in dollars?")
    crt_widget = models.IntegerField(label="How many minutes would it take 100 machines to make 100 widgets?")
    crt_lake = models.IntegerField(label="How many days would it take to cover half of the lake?")
    crt_double = models.StringField(
        label="In 2021, how much will you be able to buy with your income?:",
        choices=[
            'More than today.',
            'Exactly the same as today.',
            'Less than today.'
        ],
        widget=widgets.RadioSelect
    )

    # Financial Literacy
    fin_change = models.IntegerField(label="")
    fin_lottery = models.IntegerField(label="")
    fin_sale = models.IntegerField(label="")
    fin_cardealer = models.IntegerField(label="")
    fin_interest = models.IntegerField(label="")
    fin_disease = models.IntegerField(label="")

    # Risk Attitudes
    risk_general = models.IntegerField(label="How would you rate your willingness to take risks in general?", min=1,
                                       max=10)
    risk_driving = models.IntegerField(label="How would you rate your willingness to take risks while driving?", min=1,
                                       max=10)
    risk_career = models.IntegerField(
        label="How would you rate your willingness to take risks in your professional career?", min=1, max=10)
    risk_health = models.IntegerField(
        label="How would you rate your willingness to take risks with respect to your health?", min=1, max=10)

    # Decision Making Scenarios
    scenario_jar = models.StringField(
        label="Which jar do you prefer to guess the color of a ball from?",
        choices=[
            'I prefer to guess the color of a ball from jar 1.',
            'I am indifferent.',
            'I prefer to guess the color of a ball from jar 2.'
        ],
        widget=widgets.RadioSelect
    )
    monty_hall = models.StringField(
        label="Is it advantageous for you to change your choice?",
        choices=[
            'I prefer to keep my original choice (Door number 1).',
            'It does not matter if I change or not.',
            'I prefer to switch to Door number 2.'
        ],
        widget=widgets.RadioSelect
    )

    # Timing fields
    decision_time = models.FloatField()
    continue_field = models.StringField(label="")
    exit_survey_completed = models.BooleanField(initial=False)
    passed_comprehension = models.BooleanField(initial=False)

    # models.py
    question_1 = models.StringField(
        choices=['$0.2', '$0.5', '$0.8'],
        widget=widgets.RadioSelect()
    )

    question_2=models.StringField(
            choices=[
                "They always move in the same direction",
                "They always move in opposite directions",
                "Their movements are unrelated to each other",
                "They always provide the same returns"
            ],
        widget=widgets.RadioSelect()
    )

    question_3 = models.StringField(
        choices=['The chances of each possibility remain constant across all rounds.',
                 'The chances of each possibility can change from round to round.',
                 'The chances are unknown before the investment decision.',
                 'Investment returns are fixed and do not depend on the possibility.'
                 ],
                 widget = widgets.RadioSelect()
    )


# Fields from the second Player class
    alpha = models.FloatField(min=0, max=1)
    original_round_number = models.IntegerField()
    original_scenario_number = models.IntegerField()
    p = models.FloatField()
    one_minus_p = models.FloatField()
    x1_l = models.FloatField()
    x1_h = models.FloatField()
    x2_h = models.FloatField()
    x2_l = models.FloatField()

    # Add this new field for cognitive uncertainty

    certainty = models.IntegerField(
        min=0,
        max=100,
        label="On a scale from 0% to 100%, how certain are you that your current allocation maximizes your earning?"
    )

    # Fields to store the original round and scenario information
    original_round_number = models.IntegerField()
    original_scenario_number = models.IntegerField()


class Constants(BaseConstants):
    name_in_url = 'hedging'
    players_per_group = None
    num_rounds = 45
    individual_rounds = 45
    practice_rounds = 1

    scenarios = [
        # Scenario 1
        {
            'p_values': [50] * 9,
            'one_minus_p_values': [50] * 9,
            'x1_l_values': [-13.95, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60, ],
            'x1_h_values': [0.05, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
            'x2_h_values': [0.05, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
            'x2_l_values': [-13.95, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60]
        },

        # Scenario 2
        {
            'p_values': [10, 20, 30, 40, 50, 60, 70, 80, 90],
            'one_minus_p_values': [90, 80, 70, 60, 50, 40, 30, 20, 10],
            'x1_l_values': [-8.60, -6.00, -4.71, -4.02, -3.41, -2.92, -2.53, -2.11, -1.68],
            'x1_h_values': [0.08, 0.51, 0.97, 1.30, 1.80, 2.40, 3.15, 4.40, 7.00],
            'x2_h_values': [3.00, 1.80, 1.50, 1.35, 1.00, 0.70, 0.50, 0.25, 0.05],
            'x2_l_values': [-5.60, -4.65, -4.13, -3.92, -4.16, -4.57, -5.13, -6.20, -8.55]
        },

        # Scenario 3
        {
             'p_values': [10, 20, 30, 40, 50, 60, 70, 80, 90],
            'one_minus_p_values': [90, 80, 70, 60, 50, 40, 30, 20, 10],
            'x1_l_values': [-8.50, -6.00, -4.70, -4.00, -3.40, -2.90, -2.53, -2.10, -1.70],
            'x1_h_values': [0.09, 0.50, 0.97, 1.30, 1.80, 2.40, 3.15, 4.40, 6.96],
            'x2_h_values': [8.00, 7.00, 6.00, 5.00, 4.00, 3.00, 2.00, 1.00, 0.05],
            'x2_l_values': [-20.00, -14.00, -12.30, -12.10, -12.80, -14.10, -16.30, -20.00, -28.00]
        },

        # Scenario 4
        {
             'p_values': [10, 20, 30, 40, 50, 60, 70, 80, 90],
            'one_minus_p_values': [90, 80, 70, 60, 50, 40, 30, 20, 10],
            'x1_l_values': [-25.00, -17.60, -14.00, -11.80, -10.10, -8.70, -7.50, -6.30, -5.10],
            'x1_h_values': [0.01, 1.20, 2.40, 3.60, 4.90, 6.60, 8.90, 12.50, 20.00],
            'x2_h_values': [8.00, 7.00, 6.00, 5.00, 4.00, 3.04, 2.00, 1.00, 0.50],
            'x2_l_values': [-20.00, -14.00, -12.30, -12.10, -12.80, -14.10, -16.30, -20.00, -27.50]
        },

        # Scenario 5
        {
            'p_values': [50] * 9,
            'one_minus_p_values': [50] * 9,
            'x1_l_values': [-7.60] * 9,
            'x1_h_values': [6.40] * 9,
            'x2_h_values': [0.10, 0.80, 1.60, 2.40, 3.20, 4.00, 4.80, 5.60, 6.40],
            'x2_l_values': [-13.90, -13.20, -12.40, -11.60, -10.80, -10.00, -9.20, -8.40, -7.60]
        }
    ]

    practice_scenarios = [
        {
            'p_values': [30, 50],
            'one_minus_p_values': [70, 50],
            'x1_l_values': [-5, -7.6],
            'x1_h_values': [2, 6.4],
            'x2_h_values': [10, 6.4],
            'x2_l_values': [-5, -7.6]
        }]

    bonus_scenarios = [
        {
            'p_values': [50],
            'one_minus_p_values': [50],
            'x1_l_values': [-7.6],
            'x1_h_values': [6.4],
            'x2_h_values': [6.4],
            'x2_l_values': [-7.6]
        }]

class Subsession(BaseSubsession):
    def creating_session(self):
        if self.round_number == 1:
            shuffled_rounds = list(range(1, Constants.num_rounds + 1))
            random.shuffle(shuffled_rounds)
            self.session.vars['shuffled_rounds'] = shuffled_rounds

        # Assign scenario values based on the shuffled round order
        for player in self.get_players():
            # Get the shuffled round number for this player in this round
            shuffled_round = self.session.vars['shuffled_rounds'][player.round_number - 1]

            # Calculate scenario index and round in scenario based on the shuffled round
            scenario_index = (shuffled_round - 1) // 9
            round_in_scenario = (shuffled_round - 1) % 9
            scenario = Constants.scenarios[scenario_index]

            # Assign values to player fields
            player.original_round_number = shuffled_round
            player.p = scenario['p_values'][round_in_scenario]
            player.one_minus_p = round(100 - player.p, 2)
            player.x1_l = scenario['x1_l_values'][round_in_scenario]
            player.x1_h = scenario['x1_h_values'][round_in_scenario]
            player.x2_h = scenario['x2_h_values'][round_in_scenario]
            player.x2_l = scenario['x2_l_values'][round_in_scenario]


class Group(BaseGroup):
    pass
