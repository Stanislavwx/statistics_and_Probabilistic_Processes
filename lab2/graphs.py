import matplotlib.pyplot as plt

def plot_bayesian_updates():
    faces = [2, 4, 6, 8, 12, 20]
    names = ['Монета (2)', 'Тетраедр (4)', 'Куб (6)', 'Октаедр (8)', 'Додекаедр (12)', 'Ікосаедр (20)']

    user_input = input("Введіть результати кидків через пробіл: ")
    try:
        rolls = [int(x) for x in user_input.split()]
    except ValueError:
        print("Помилка: будь ласка, вводьте лише цілі числа через пробіл.")
        return

    print(f"\nАналізуємо масив кидків: {rolls}")

  
    history = {name: [1.0 / len(faces)] for name in names}
    priors = [1.0 / len(faces)] * len(faces)

    for step, roll in enumerate(rolls, start=1):
        likelihoods = []
        for f in faces:
            if roll > f:
                likelihoods.append(0.0)
            else:
                likelihoods.append(1.0 / f)

        unnormalized = [p * l for p, l in zip(priors, likelihoods)]
        marginal = sum(unnormalized)

        if marginal == 0:
            posteriors = [0.0] * len(faces)
            print(f"Попередження: На кроці {step} випало число {roll}, яке не може згенерувати жодна фігура!")
        else:
            posteriors = [u / marginal for u in unnormalized]

        for i, name in enumerate(names):
            history[name].append(posteriors[i])
        
        priors = posteriors

    print("\n--- ФІНАЛЬНІ ЙМОВІРНОСТІ ---")
    for name, p in zip(names, priors):
        print(f"{name}: {p * 100:.4f}%")

    plt.figure(figsize=(12, 7))
    x_values = range(len(rolls) + 1) 

    for name in names:
        plt.plot(x_values, history[name], marker='o', linewidth=2, label=name)

    plt.title('Залежність імовірності вибору фігури $P(B_i|A)$ від номера експерименту', fontsize=14, pad=15)
    plt.xlabel('Порядковий номер експерименту (кидка)', fontsize=12)
    plt.ylabel('Ймовірність', fontsize=12)
    plt.xticks(x_values)
    plt.ylim(-0.05, 1.05)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.legend(title='Фігури', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout() 
    plt.show()

if __name__ == "__main__":
    plot_bayesian_updates()