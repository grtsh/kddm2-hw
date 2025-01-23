import numpy as np
import pandas as pd

TASK1_SWITCH_DISTRIBUTIONS = [0.5, 0.5]
TASK1_CISCO_ENV_DISTRIBUTION = [0.8, 0.2]
TASK1_ARUBA_ENV_DISTRIBUTION = [0.2, 0.8]

TASK1_LIFE_EXPECTANCY_CISCO_BAD_MEAN = 3 * 365
TASK1_LIFE_EXPECTANCY_CISCO_BAD_STDDEV = 0.5 * 365

TASK1_LIFE_EXPECTANCY_CISCO_GOOD_MEAN = 6 * 365
TASK1_LIFE_EXPECTANCY_CISCO_GOOD_STDDEV = 1 * 365

TASK1_LIFE_EXPECTANCY_ARUBA_BAD_MEAN = 2 * 365
TASK1_LIFE_EXPECTANCY_ARUBA_BAD_STDDEV = 0.5 * 365

TASK1_LIFE_EXPECTANCY_ARUBA_GOOD_MEAN = 5 * 365
TASK1_LIFE_EXPECTANCY_ARUBA_GOOD_STDDEV = 1 * 365


def task1(n=1000, seed=4):
    np.random.seed(seed)

    def _get_lifspan(maker, env):
        if maker == "CISCO":
            return (
                np.random.normal(
                    TASK1_LIFE_EXPECTANCY_CISCO_GOOD_MEAN,
                    TASK1_LIFE_EXPECTANCY_CISCO_GOOD_STDDEV,
                )
                if env
                else np.random.normal(
                    TASK1_LIFE_EXPECTANCY_CISCO_BAD_MEAN,
                    TASK1_LIFE_EXPECTANCY_CISCO_BAD_STDDEV,
                )
            )
        elif maker == "ARUBA":
            return (
                np.random.normal(
                    TASK1_LIFE_EXPECTANCY_ARUBA_GOOD_MEAN,
                    TASK1_LIFE_EXPECTANCY_ARUBA_GOOD_STDDEV,
                )
                if env
                else np.random.normal(
                    TASK1_LIFE_EXPECTANCY_ARUBA_BAD_MEAN,
                    TASK1_LIFE_EXPECTANCY_ARUBA_BAD_STDDEV,
                )
            )

    df = {"maker": [], "enviroment": [], "lifespan": []}

    for _ in range(n):
        df["maker"].append(
            np.random.choice(["ARUBA", "CISCO"], p=TASK1_SWITCH_DISTRIBUTIONS)
        )
        df["enviroment"].append(
            np.random.choice(
                [0, 1],
                p=TASK1_CISCO_ENV_DISTRIBUTION
                if df["maker"][-1] == "CISCO"
                else TASK1_ARUBA_ENV_DISTRIBUTION,
            )
        )
        df["lifespan"].append(int(_get_lifspan(df["maker"][-1], df["enviroment"][-1])))

    df = pd.DataFrame(df)
    df.to_csv("results/1a_simpsons_paradox.csv", index=False)
    print("Data saved to results/1a_simpsons_paradox.csv")


def task1_table():
    file_path = 'results/1a_simpsons_paradox.csv'
    df = pd.read_csv(file_path)
    mean_lifespan_by_maker = df.groupby("maker")["lifespan"].mean()
    mean_lifespan_by_maker_and_env = df.groupby(["maker", "enviroment"])["lifespan"].mean()
    combined_results = pd.concat(
        [mean_lifespan_by_maker.rename("Overall Lifespan"),
        mean_lifespan_by_maker_and_env.unstack().rename(columns={0: "Bad Environment", 1: "Good Environment"})],
        axis=1
    )
    markdown_table = combined_results.to_markdown()

    return markdown_table


def main():
    task1()
    print(task1_table())


main()
