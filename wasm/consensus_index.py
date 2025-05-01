

import marimo

__generated_with = "0.13.3"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns

    return mo, np, pd, plt, sns


@app.cell
def _(mo):
    max_n_element = mo.ui.number(start=10, step=1, label="Maximum number of labels")
    ballast_element = mo.ui.number(
        start=1, step=1, label="Ballast: The number of agreements and disagreeement to add."
    )
    max_n_element, ballast_element
    return ballast_element, max_n_element


@app.cell
def _(ballast_element, max_n_element, np):
    max_n = max_n_element.value
    ballast = ballast_element.value
    ns = np.arange(1, max_n)
    return ballast, ns


@app.cell
def _(ballast, np, ns, pd, plt, sns):
    def get_smoothed_agreement(n_total, n_agreed, ballast=1):
        return (n_agreed + ballast) / (n_total + 2 * ballast)

    grid = np.array(
        [(n_total, n_agreed) for n_total in ns for n_agreed in ns if n_agreed <= n_total]
    )

    grid = np.concatenate(
        (
            grid,
            np.array(
                [
                    get_smoothed_agreement(n_total, n_agreed, ballast=ballast)
                    for (n_total, n_agreed) in grid
                ]
            )[:, np.newaxis],
        ),
        axis=1,
    )

    df = pd.DataFrame(grid, columns=["n_total", "n_agreed", "smoothed_agreement"])

    # Plot heatmap
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        df.pivot_table(
            index="n_total",
            columns="n_agreed",
            values="smoothed_agreement",
        ),
        annot=True,
        cmap="Greens",
        cbar_kws={"label": "Smoothed Agreement"},
    )
    plt.title("Heatmap of Smoothed Agreement")
    plt.show()

    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
