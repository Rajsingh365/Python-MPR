# SIM.py

import random
# import numpy as np
# import matplotlib.pyplot as plt


def monte_carlo_simulation(monthly_savings, retirement_goal, age, retirement_age, scenario):
    # print(age)
    # print("\n\n")
    num_simulations = 1000  # Number of simulations for Monte Carlo
    retirement_funds = []   # List to store retirement funds from each simulation
    for _ in range(num_simulations):
        # Simulate investment returns based on scenario
        total_returns = simulate_investment_returns(monthly_savings, age, retirement_age, scenario)
        retirement_funds.append(total_returns)  # Add retirement fund from this simulation to the list
    print(retirement_funds)
    # Calculate probability of meeting retirement goal
    probability = sum(fund*100 >= retirement_goal for fund in retirement_funds) / num_simulations
    return probability

def simulate_investment_returns(monthly_savings, age, retirement_age, scenario):
    # Simulate investment returns based on scenario
    mean_returns = {'stocks': 0.1, 'gold': 0.05, 'mutual funds': 0.08, 'fixed deposit': 0.04, 'government schemes': 0.035}
    std_devs = {'stocks': 0.15, 'gold': 0.03, 'mutual funds': 0.1, 'fixed deposit': 0.02, 'government schemes': 0.015}
    total_returns = 0
    for investment_option, allocation_percentage in scenario.items():
        mean_return = mean_returns.get(investment_option, 0)
        std_dev = std_devs.get(investment_option, 0)
        investment_amount = monthly_savings * allocation_percentage
        # Simulate returns using Gaussian distribution
        investment_returns = random.gauss(mean_return, std_dev)
        total_returns += investment_amount * investment_returns
    return total_returns
