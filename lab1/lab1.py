import os
import random
from pathlib import Path

os.environ["MPLCONFIGDIR"] = "tmp_mpl_config"

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


VARIANT = 3
SIDES_BY_VARIANT = {
    1: 4,
    2: 6,
    3: 8,
    4: 12,
    5: 20,
}
SAMPLE_SIZES = [10, 100, 1000, 1000]

# Seed = input("Введіть свій seed: ")

def simulate_rolls(sides, n):
    counts = [0] * sides

    for _ in range(n):
        number = random.randint(1, sides)
        counts[number - 1] += 1

    frequencies = []
    for count in counts:
        frequencies.append(count / n)

    return counts, frequencies


def main():
    sides = SIDES_BY_VARIANT[VARIANT]
    theoretical_probability = 1 / sides
    output_file = f"lab1_results/variant_{VARIANT}_histograms.png"

    #random.seed(int(Seed))
    random.seed
    Path("tmp_mpl_config").mkdir(exist_ok=True)
    Path("lab1_results").mkdir(exist_ok=True)

    fig, axes = plt.subplots(2, 2, figsize=(12, 8))
    x_values = list(range(1, sides + 1))

    for i in range(len(SAMPLE_SIZES)):
        n = SAMPLE_SIZES[i]
        counts, frequencies = simulate_rolls(sides, n)

        print(f"N = {n}")
        for k in range(sides):
            print(
                f"Грань {k + 1}: кількість = {counts[k]}, частота = {frequencies[k]:.4f}"
            )
        print()

        ax = axes[i // 2][i % 2]
        ax.bar(x_values, frequencies, color="skyblue", edgecolor="black")
        ax.axhline(
            theoretical_probability,
            color="red",
            linestyle="--",
            label=f"P = {theoretical_probability:.4f}",
        )
        ax.set_title(f"N = {n}")
        ax.set_xlabel("Номер грані")
        ax.set_ylabel("Частота")
        ax.set_xticks(x_values)
        ax.legend()
        ax.grid(axis="y", alpha=0.3)

    plt.tight_layout()
    plt.savefig(output_file, dpi=200)
    plt.close()

    print(f"Гістограми збережено у файл {output_file}")


if __name__ == "__main__":
    main()
