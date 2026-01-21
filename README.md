# squares_fibonacci_series
python script to show Fibonacci series in squares as per golden ratio 
the original turtle-based Fibonacci square spiral (animated)
the matplotlib static version
the updated turtle version (with labels, animation speed control, size scaling from ~2 cm to ~124 cm)

markdown

# Fibonacci Squares & Golden Spiral Visualizations

Three Python scripts that visualize the **Fibonacci sequence** through growing squares arranged in a spiral pattern — a beautiful demonstration of the connection between the Fibonacci numbers and the **golden ratio** (φ ≈ 1.618).

All three versions draw squares whose side lengths follow the Fibonacci sequence and (in two cases) approximate the golden spiral using quarter-circles.

## What is the Fibonacci Sequence?

The **Fibonacci sequence** is a series of numbers where each number is the sum of the two preceding ones. It usually starts with 0 and 1 (or sometimes 1 and 1):

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, ...
   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑
   F₀  F₁  F₂  F₃  F₄  F₅  F₆  F₇  F₈  F₉ F₁₀ F₁₁ F₁₂ F₁₃ F₁₄ F₁₅ F₁₆ ...

### Important properties

- The **ratio** of consecutive Fibonacci numbers approaches the **golden ratio** (φ = (1 + √5)/2 ≈ 1.6180339887...) as the numbers get larger:

  Fₙ₊₁ / Fₙ → φ    as n → ∞

Examples:
- 8 / 5   = 1.6
- 13 / 8  = 1.625
- 21 / 13 ≈ 1.6154
- 144 / 89 ≈ 1.61798
- 987 / 610 ≈ 1.61803

- This is why arranging squares with Fibonacci side lengths and connecting their corners with quarter-circles creates a very good approximation of the **golden spiral** — a logarithmic spiral whose growth factor is the golden ratio.

## The Three Scripts

| Script                     | Library     | Style                  | Features                                      | Best for                     |
|----------------------------|-------------|------------------------|-----------------------------------------------|------------------------------|
| `fibonacci_spiral_turtle.py` (original) | turtle     | Animated               | Simple, educational, draws in real time       | Beginners, live demo         |
| `fibonacci_spiral_matplotlib.py`        | matplotlib | Static plot            | Clean image, easy to save/export              | Publications, posters        |
| `fibonacci_spiral_turtle_advanced.py`   | turtle     | Animated + labels      | Square numbers, size control (~2–124 cm), speed | Presentations, teaching      |

### 1. Basic Animated Version (`fibonacci_spiral_turtle.py`)

Classic turtle graphics animation — draws one square after another.

```bash
python fibonacci_spiral_turtle.py

2. Static Matplotlib Version (fibonacci_spiral_matplotlib.py)Produces a high-quality static image (good for saving/exporting).bash

python fibonacci_spiral_matplotlib.py

3. Advanced Animated Version with Labels & Size Control (fibonacci_spiral_turtle_advanced.py)Most feature-rich version:Starts from small squares (~2–5 cm)
Ends near desired maximum size (default ~124 cm)
Shows square number and Fibonacci value next to each square
Adjustable animation speed
Adjustable pause between squares

bash

python fibonacci_spiral_turtle_advanced.py

Requirementsbash

pip install matplotlib
# turtle is included with standard Python

Customization examplespython

# Very large version
draw_fibonacci_spiral(max_side_cm=180, start_from_fib_index=5, animation_speed=3, pause_between_squares=0.6)

# Fast & dense
draw_fibonacci_spiral(max_side_cm=60, start_from_fib_index=3, animation_speed=9, pause_between_squares=0.08)

# Very slow & dramatic (good for classroom)
draw_fibonacci_spiral(max_side_cm=100, start_from_fib_index=4, animation_speed=2, pause_between_squares=1.2)

Golden Spiral approximation qualityThe quarter-circle method used here is a very good discrete approximation of the true golden spiral.
For even better visual match you can:Use more squares (increase n_squares or decrease start_from_fib_index)
Use true logarithmic spiral equation instead of quarter circles (requires different math)

LicenseMIT — feel free to use, modify, teach with, present, etc.Enjoy the beauty of mathematics! 

You can save this content as `README.md` in the folder containing all three scripts.

Let me know if you want to add screenshots, license file, or folder structure example to the readme.

