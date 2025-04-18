import numpy as np
from scipy import stats
import pandas as pd

# Organize data
individual_paper = [0.25, -0.75, -0.25, 0.25, 0, 0, 0.5, 0, -0.25, 0, 0.25, 0, 0, 0, 0, 0.25, 0.25, 0.5, 0.25, 0, -0.25, 0, 0.25, 0.5, 0, 0.25, 0, -0.25, -0.25, 0.25, 0.5, -0.25, 0, 0, 0.25, 0.5, 0, 0]

individual_realized = [-0.25, -0.25, 0, -0.25, 0.25, -0.25, -0.25, 0.25, -0.5, 0, 0.5, 0, 0, 0, 0.25, 0.25, -0.25, 0, 0.25, -0.25, 0.25, 0, -0.25, -0.25, 0, -0.25, 0, -0.5, 0, 0, -0.5, 0, 0, 0, -0.25, 0.75]

group_paper = [-0.5, -0.5, -0.25, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.25, 0.25, 0.25, 0.5, 0, 0.25, 0, -0.25, -0.25, 0, -0.25, 0.25, -0.5, 0.25, -0.5]

group_realized = [-0.5, 0, 0, 0, 0, -0.25, 0, 0.25, 0, 0.25, -0.25, 0, 0.25, 0, 0.25, 0.25, -0.25, 0, 0, 0, 0, -0.25, 0, 0, -0.25, 0.5]

# Calculate basic statistics
def get_stats(data):
    return {
        'mean': np.mean(data),
        'median': np.median(data),
        'std': np.std(data),
        'n': len(data)
    }

stats_ip = get_stats(individual_paper)
stats_ir = get_stats(individual_realized)
stats_gp = get_stats(group_paper)
stats_gr = get_stats(group_realized)

# Perform t-tests
t_ind_paper_vs_realized = stats.ttest_ind(individual_paper, individual_realized)
t_group_paper_vs_realized = stats.ttest_ind(group_paper, group_realized)
t_paper_ind_vs_group = stats.ttest_ind(individual_paper, group_paper)
t_realized_ind_vs_group = stats.ttest_ind(individual_realized, group_realized)

# Print results
print("\nDescriptive Statistics:")
print("\nIndividual Paper Loss:")
print(f"Mean: {stats_ip['mean']:.3f}, Std: {stats_ip['std']:.3f}, N: {stats_ip['n']}")
print("\nIndividual Realized Loss:")
print(f"Mean: {stats_ir['mean']:.3f}, Std: {stats_ir['std']:.3f}, N: {stats_ir['n']}")
print("\nGroup Paper Loss:")
print(f"Mean: {stats_gp['mean']:.3f}, Std: {stats_gp['std']:.3f}, N: {stats_gp['n']}")
print("\nGroup Realized Loss:")
print(f"Mean: {stats_gr['mean']:.3f}, Std: {stats_gr['std']:.3f}, N: {stats_gr['n']}")

print("\nT-Test Results:")
print("\nIndividual Paper vs Realized:")
print(f"t-statistic: {t_ind_paper_vs_realized.statistic:.3f}, p-value: {t_ind_paper_vs_realized.pvalue:.3f}")
print("\nGroup Paper vs Realized:")
print(f"t-statistic: {t_group_paper_vs_realized.statistic:.3f}, p-value: {t_group_paper_vs_realized.pvalue:.3f}")
print("\nPaper Loss - Individual vs Group:")
print(f"t-statistic: {t_paper_ind_vs_group.statistic:.3f}, p-value: {t_paper_ind_vs_group.pvalue:.3f}")
print("\nRealized Loss - Individual vs Group:")
print(f"t-statistic: {t_realized_ind_vs_group.statistic:.3f}, p-value: {t_realized_ind_vs_group.pvalue:.3f}")