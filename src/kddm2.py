import numpy as np
import pandas as pd

TASK1_SWITCH_DISTRIBUTIONS = [0.5, 0.5]
TASK1_CISCO_ENV_DISTRIBUTION = [0.7, 0.3]
TASK1_ARUBA_ENV_DISTRIBUTION = [0.3, 0.7]

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
    print(df.head())


def main():
    task1()


main()
