import random

def simulate_dice_rolls(num_rolls=10):
    faces = [2, 4, 6, 8, 12, 20]
    names = ['Монета (2)', 'Тетраедр (4)', 'Куб (6)', 'Октаедр (8)', 'Додекаедр (12)', 'Ікосаедр (20)']

    chosen_idx = random.randint(0, len(faces) - 1)
    chosen_faces = faces[chosen_idx]
    chosen_name = names[chosen_idx]

    rolls = [random.randint(1, chosen_faces) for _ in range(num_rolls)]
    
    print(f"--- РЕЗУЛЬТАТИ ГЕНЕРАЦІЇ ---")
    print(f"Справжня обрана фігура (прихована від алгоритму): {chosen_name}")
    print(f"Результати {num_rolls} кидків: {rolls}\n")

    priors = [1 / len(faces)] * len(faces) 
    likelihoods = []

    for f in faces:
        if any(r > f for r in rolls):
            likelihoods.append(0.0)
        else:
            likelihoods.append((1 / f) ** num_rolls)

        unnormalized_posteriors = [p * l for p, l in zip(priors, likelihoods)]
        
    marginal_likelihood = sum(unnormalized_posteriors)

    if marginal_likelihood == 0:
        posteriors = [0] * len(faces)
    else:
        posteriors = [up / marginal_likelihood for up in unnormalized_posteriors]

    print("--- АНАЛІЗ ЙМОВІРНОСТЕЙ ---")
    for name, p in zip(names, posteriors):
        print(f"{name}: {p * 100:.4f}%")

if __name__ == "__main__":
    simulate_dice_rolls(10)