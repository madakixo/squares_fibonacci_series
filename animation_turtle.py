import matplotlib.pyplot as plt
import numpy as np

def plot_fibonacci_squares(n=12, scale=1.0):
    fib = [0, 1]
    for _ in range(n):
        fib.append(fib[-1] + fib[-2])
    fib = fib[1:]  # 1,1,2,3,5,8,...

    fig, ax = plt.subplots(figsize=(10,10))
    ax.set_aspect('equal')
    ax.set_facecolor('black')

    x, y = 0, 0
    dx, dy = 1, 0   # initial direction: right

    colors = plt.cm.viridis(np.linspace(0, 1, n))

    for i in range(min(n, len(fib))):
        side = fib[i] * scale
        
        # Draw square
        rect = plt.Rectangle((x, y), side, side,
                            fill=False, edgecolor=colors[i],
                            linewidth=2.2, alpha=0.9)
        ax.add_patch(rect)
        
        # Next position
        x += dx * side
        y += dy * side
        
        # Rotate 90° clockwise: (dx,dy) → (dy, -dx)
        dx, dy = dy, -dx

    ax.set_xlim(-scale* fib[-1]*1.2, scale* fib[-1]*1.2)
    ax.set_ylim(-scale* fib[-1]*1.2, scale* fib[-1]*1.2)
    ax.axis('off')
    plt.title(f"Fibonacci Squares Spiral (n = {n})", color='white', fontsize=14)
    plt.show()


if __name__ == "__main__":
    plot_fibonacci_squares(n=14, scale=8)
