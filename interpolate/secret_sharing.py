import matplotlib.pyplot as plt

from interpolate.interpolate import interpolate
from interpolate.polynomial import Polynomial

secret = 1234
original = Polynomial([secret, 17, 9])

shares = [(x, original(x)) for x in range(1, 6)]
selected = [shares[0], shares[2], shares[4]]
reconstructed = interpolate(selected)

# Sample the curves densely enough to draw smooth lines.
xs = [i / 100 for i in range(551)]

fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

axes[0].plot(
    xs, [original(x) for x in xs],
    label="Original polynomial",
)
axes[0].scatter(
    *zip(*shares), color="tab:blue", s=65, zorder=3,
    label="All 5 shares",
)
for x, y in shares:
    axes[0].annotate(
        f"({x}, {y})", (x, y),
        xytext=(6, 8), textcoords="offset points",
    )
axes[0].set_title("Split: distribute one point per participant")

axes[1].plot(
    xs, [reconstructed(x) for x in xs],
    color="tab:orange", linestyle="--",
    label="Reconstructed polynomial",
)
axes[1].scatter(
    *zip(*selected), color="tab:orange", s=65, zorder=3,
    label="Any 3 shares",
)
axes[1].set_title("Recover: interpolate 3 shares")

for ax in axes:
    ax.scatter(
        [0], [secret], color="tab:red", marker="*", s=180,
        zorder=4, label=f"Secret: f(0) = {secret}",
    )
    ax.set_xlabel("x — participant index")
    ax.grid(alpha=0.25)
    ax.legend()

axes[0].set_ylabel("f(x)")
fig.tight_layout()
plt.show()
