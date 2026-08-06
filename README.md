# European Childhood Obesity Inequalities

A reproducible R Markdown project examining childhood and adolescent obesity prevalence, uncertainty and sex inequalities across the WHO European Region.

## Public-health question

Which European countries have the highest modelled obesity prevalence among children and adolescents aged 5–19 years, and how do estimates differ by sex and over time?

## Project structure

```text
european-childhood-obesity-inequalities/
├── childhood-obesity-analysis.Rmd    # Complete step-by-step analysis
├── README.md                         # Project guide
├── data/
│   ├── raw/
│   │   └── childhood_obesity.csv     # Original WHO-derived data
│   └── processed/
│       └── tableau_childhood_obesity.csv
└── visuals/
    ├── latest_obesity_prevalence.png
    ├── latest_sex_gap.png
    └── regional_obesity_trend.png
```

## Analysis workflow

The R Markdown report explains each stage:

1. Define the research question, objectives and unit of analysis.
2. Document the variables and WHO source.
3. Import the raw CSV using a reproducible relative path.
4. Validate required columns, missing values, duplicates and confidence limits.
5. Clean field types and create readable age-group labels.
6. Summarise the latest comparable estimates for ages 5–19.
7. Rank high-prevalence countries with confidence intervals.
8. Calculate the latest male–female prevalence gap.
9. Visualise long-term European trends.
10. Export a cleaned Tableau-ready dataset.
11. Explain interpretation, limitations and reproducibility.

## Data

The included raw file contains WHO modelled estimates for the European Region. Its fields are:

`Country, Country_code, Year, Sex, Age_group, Obesity_prevalence, Lower_CI, Upper_CI, Source`

Source: [WHO – Prevalence of obesity among children and adolescents aged 5–19 years](https://data.who.int/indicators/i/C6262EC/EF93DDB). WHO data licensing and attribution requirements apply.

## Run the project in RStudio

Install the required packages once:

```r
install.packages(c("dplyr", "ggplot2", "knitr", "rmarkdown", "tidyr"))
```

Then:

1. Clone or download this repository.
2. Open the repository folder in RStudio.
3. Open `childhood-obesity-analysis.Rmd`.
4. Click **Knit**.
5. Select **Knit to HTML** if RStudio asks for a format.

The report regenerates the plots in `visuals/` and the Tableau file in `data/processed/`.

## Main outputs

- Latest prevalence ranking with confidence intervals.
- Latest sex-gap analysis.
- Long-term trend chart by sex.
- Quality-control tables.
- White-background HTML report suitable for reading and portfolio presentation.
- Tableau-ready cleaned CSV.

![Latest childhood obesity prevalence ranking](visuals/latest_obesity_prevalence.png)

## Tableau suggestions

Use `data/processed/tableau_childhood_obesity.csv` to create:

- a country map coloured by obesity prevalence;
- a latest-year country ranking;
- a male–female inequality chart;
- a time-trend chart;
- confidence-interval tooltips; and
- filters for year, sex and age group.

## Interpretation

These are ecological, modelled estimates. Country rankings should be presented with confidence intervals, and the results cannot determine an individual child’s risk or the causes of cross-country differences.
