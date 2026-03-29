import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], s=10)

    # Line of best fit using ALL data (1880 to 2050)
    slope1, intercept1, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended1 = range(1880, 2051)
    ax.plot(years_extended1, [slope1 * year + intercept1 for year in years_extended1], 'r', label='Best fit 1880-2050')

    # Line of best fit using data from year 2000 onwards (to 2050)
    df_2000 = df[df['Year'] >= 2000]
    slope2, intercept2, _, _, _ = linregress(df_2000['Year'], df_2000['CSIRO Adjusted Sea Level'])
    years_extended2 = range(2000, 2051)
    ax.plot(years_extended2, [slope2 * year + intercept2 for year in years_extended2], 'g', label='Best fit 2000-2050')

    # Labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    fig.savefig('sea_level_plot.png')
    return ax
