# Childhood Obesity and Health Inequalities in Europe

## Public-health question

Which European countries show the highest childhood overweight and obesity prevalence, and how do physical activity and environmental indicators differ?

## Data

Download country-level indicators from the [WHO Europe Environment and Health Information System](https://gateway.euro.who.int/en/datasets/enhis/). Save the harmonised file as `data/raw/childhood_obesity.csv` with:

`Country, Year, Sex, Age_group, Overweight_prevalence, Obesity_prevalence, Physical_activity_prevalence`

## Analysis

- Cleans country, demographic and prevalence fields.
- Summarises obesity and overweight by country and sex.
- Identifies high-burden countries using quartiles.
- Exports `data/processed/tableau_childhood_obesity.csv` for Tableau.

## Run

```bash
pip install -r requirements.txt
python src/analyse_childhood_obesity.py
jupyter lab
```

## Tableau dashboard

Create a country map, obesity ranking, sex comparison, and scatterplot of physical activity versus obesity prevalence.

## Methods and limitations

These indicators are population estimates. Differences in survey years, age ranges and collection methods may affect comparisons.
