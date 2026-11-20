import random

def fitness(x):
    return x * x

population = [random.randint(-10, 10) for _ in range(6)]

for generation in range(10):
    population.sort(key=fitness, reverse=True)

    print("Generation", generation + 1, ":", population)

    parents = population[:2]
    new_population = parents.copy()

    while len(new_population) < 6:
        p1, p2 = random.sample(parents, 2)

        child = (p1 + p2) // 2

        if random.random() < 0.2:
            child += random.randint(-2, 2)

        child = max(-10, min(10, child))
        new_population.append(child)

    population = new_population

best = max(population, key=fitness)

print("\nBest Solution:", best)
print("Best Fitness:", fitness(best))
