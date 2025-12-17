import random
import matplotlib.pyplot as plt

def simulate_dice(n: int):
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(n):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1
    probs = {s: counts[s] / n for s in counts}
    return counts, probs

def analytic_probs():
    ways = {2:1,3:2,4:3,5:4,6:5,7:6,8:5,9:4,10:3,11:2,12:1}
    return {s: ways[s] / 36 for s in ways}

if __name__ == "__main__":
    N = 200_000
    _, mc = simulate_dice(N)
    an = analytic_probs()

    print(f"N={N}")
    print("Sum | MonteCarlo | Analytic | AbsError")
    for s in range(2, 13):
        err = abs(mc[s] - an[s])
        print(f"{s:>3} | {mc[s]:.5f}     | {an[s]:.5f}   | {err:.5f}")

    sums = list(range(2, 13))
    mc_vals = [mc[s] for s in sums]
    an_vals = [an[s] for s in sums]

    plt.figure(figsize=(10, 5))
    plt.plot(sums, mc_vals, marker="o", label="Monte Carlo")
    plt.plot(sums, an_vals, marker="o", label="Analytic")
    plt.xlabel("Sum")
    plt.ylabel("Probability")
    plt.title("Two Dice: Monte Carlo vs Analytic")
    plt.grid(True)
    plt.legend()
    plt.show()
