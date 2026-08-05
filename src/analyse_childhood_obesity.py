from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/raw/childhood_obesity.csv"
OUTPUT = ROOT / "data/processed/tableau_childhood_obesity.csv"
CHART = ROOT / "visuals/obesity_vs_physical_activity.png"
REQUIRED = {"Country", "Year", "Sex", "Age_group", "Overweight_prevalence", "Obesity_prevalence", "Physical_activity_prevalence"}


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Add the WHO data file here: {INPUT}")
    df = pd.read_csv(INPUT)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    for column in REQUIRED - {"Country", "Sex", "Age_group"}:
        df[column] = pd.to_numeric(df[column], errors="coerce")
    df = df.dropna(subset=["Country", "Year", "Obesity_prevalence"])
    df["Obesity_burden_quartile"] = pd.qcut(df["Obesity_prevalence"], 4, labels=["Low", "Moderate", "High", "Very high"], duplicates="drop")
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    sns.set_theme(style="whitegrid")
    ax = sns.scatterplot(data=df, x="Physical_activity_prevalence", y="Obesity_prevalence", hue="Sex", s=90)
    ax.set(title="Childhood obesity and physical activity", xlabel="Physical activity prevalence (%)", ylabel="Obesity prevalence (%)")
    plt.tight_layout()
    plt.savefig(CHART, dpi=200)
    print(f"Created {OUTPUT} and {CHART}")


if __name__ == "__main__":
    main()
