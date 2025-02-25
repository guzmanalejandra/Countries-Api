import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from ipywidgets import interact, widgets

# Fetch data from the REST Countries API
url = "https://restcountries.com/v3.1/all"
response = requests.get(url)
response.raise_for_status()
countries_data = response.json()

# Process the data
data = []
for country in countries_data:
    data.append({
        "Name": country.get("name", {}).get("common", "N/A"),
        "Region": country.get("region", "N/A"),
        "Subregion": country.get("subregion", "N/A"),
        "Population": country.get("population", 0),
        "Area": country.get("area", 0),
        "GDP": country.get("gdp", {}).get("nominal", 0),
        "Languages": ", ".join(country.get("languages", {}).values()),
    })

df = pd.DataFrame(data)

# Clean the data
df = df[df["Population"] > 0]
df = df[df["Area"] > 0]

# Function to plot interactive scatter plot
def plot_population_vs_area(region):
    plt.figure(figsize=(12, 8))
    filtered_df = df[df["Region"] == region] if region != "All" else df
    sns.scatterplot(
        data=filtered_df,
        x="Area",
        y="Population",
        hue="Subregion",
        size="Population",
        sizes=(20, 2000),
        alpha=0.7,
        palette="tab10",
    )
    plt.xscale('log')
    plt.yscale('log')
    plt.title(f'Population vs Area (Region: {region})')
    plt.xlabel('Area (log scale)')
    plt.ylabel('Population (log scale)')
    plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
    plt.show()

# Interactive widget to select region
regions = ["All"] + sorted(df["Region"].unique())
interact(plot_population_vs_area, region=widgets.Dropdown(options=regions, value="All", description="Region:"))

# Function to display top N countries by population or area
def top_countries(metric, top_n):
    top_df = df.sort_values(by=metric, ascending=False).head(top_n)
    plt.figure(figsize=(12, 8))
    sns.barplot(x=metric, y="Name", data=top_df, palette="viridis")
    plt.title(f"Top {top_n} Countries by {metric}")
    plt.xlabel(metric)
    plt.ylabel("Country")
    plt.show()

# Interactive widgets for top countries
interact(
    top_countries,
    metric=widgets.Dropdown(options=["Population", "Area"], description="Metric:"),
    top_n=widgets.IntSlider(value=10, min=5, max=20, step=1, description="Top N:")
)
