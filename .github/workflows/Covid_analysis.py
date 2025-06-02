import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('data/covid_data.csv')

# Top 5 countries by total cases
top_cases = df.sort_values('total_cases', ascending=False).head(5)

# Top 5 countries by total deaths
top_deaths = df.sort_values('total_deaths', ascending=False).head(5)

# Print results
print("Top 5 countries by total cases:\n", top_cases[['location', 'total_cases']])
print("\nTop 5 countries by total deaths:\n", top_deaths[['location', 'total_deaths']])

# Plot
plt.figure(figsize=(10, 5))
plt.bar(top_cases['location'], top_cases['total_cases'], color='skyblue')
plt.title('Top 5 Countries by COVID-19 Cases')
plt.ylabel('Total Cases')
plt.xlabel('Country')
plt.tight_layout()
plt.show()
