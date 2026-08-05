from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "data/raw/childhood_obesity.csv"
OUTPUT = ROOT / "data/processed/tableau_childhood_obesity.csv"
CHART = ROOT / "visuals/latest_obesity_prevalence.png"
REQUIRED = {"Country", "Country_code", "Year", "Sex", "Age_group", "Obesity_prevalence", "Lower_CI", "Upper_CI"}


def main() -> None:
    if not INPUT.exists():
        raise FileNotFoundError(f"Add the WHO data file here: {INPUT}")
    df = pd.read_csv(INPUT)
    missing = REQUIRED - set(df.columns)
    if missing:
        raise ValueError(f"Missing columns: {sorted(missing)}")
    numeric = ["Year", "Obesity_prevalence", "Lower_CI", "Upper_CI"]
    df[numeric] = df[numeric].apply(pd.to_numeric, errors="coerce")
    df = df.dropna(subset=["Country", "Year", "Obesity_prevalence"])
    df["Obesity_burden_quartile"] = pd.qcut(df["Obesity_prevalence"].rank(method="first"), 4, labels=["Low", "Moderate", "High", "Very high"])
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUTPUT, index=False)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(11, 7))
    total = df[(df["Sex"] == "Total") & (df["Age_group"] == "Y5T19")]
    latest = total.sort_values("Year").groupby("Country", as_index=False).tail(1)
    top = latest.nlargest(15, "Obesity_prevalence").sort_values("Obesity_prevalence")
    ax = sns.barplot(data=top, x="Obesity_prevalence", y="Country", color="#E45756")
    ax.set(title="Latest obesity prevalence (ages 5–19)", xlabel="Obesity prevalence (%)", ylabel="Country")
    plt.tight_layout()
    plt.savefig(CHART, dpi=200)
    print(f"Created {OUTPUT} and {CHART}")


if __name__ == "__main__":
    main()
