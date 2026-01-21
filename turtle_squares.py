import turtle
import math

# =============================================
#   Fibonacci Squares + Golden Spiral_madakixo
# =============================================

def draw_fibonacci_spiral(n_squares=12, scale=5):
    """
    Draws squares whose sides follow the Fibonacci sequence
    and connects their corners with a golden spiral approximation.
    
    Parameters:
        n_squares : how many Fibonacci squares to draw
        scale     : multiplier to make the drawing bigger on screen
    """
    
    # Turtle setup
    turtle.speed(0)           # fastest drawing
    turtle.bgcolor("black")
    turtle.pencolor("gold")
    turtle.pensize(2)
    turtle.hideturtle()
    
    # Start position
    turtle.penup()
    turtle.goto(-200, -200)
    turtle.pendown()
    
    # Fibonacci sequence generation
    fib = [0, 1]
    for i in range(2, n_squares + 2):
        fib.append(fib[-1] + fib[-2])
    
    # We usually skip the first 0 or 1 to get nicer sizes
    fib = fib[2:]   # start from 1,1,2,3,5,8,...
    
    # Directions: right, up, left, down, right, ...
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    dir_index = 0
    
    # We'll collect corner points to draw the spiral later
    corners = []
    
    for i in range(min(n_squares, len(fib))):
        side = fib[i] * scale
        
        # Remember starting corner for spiral
        x, y = turtle.pos()
        corners.append((x, y))
        
        # Draw square
        for _ in range(4):
            turtle.forward(side)
            turtle.left(90)
        
        # Move to next position (slide along the last side)
        dx, dy = directions[dir_index]
        turtle.penup()
        turtle.forward(side * dx)
        turtle.right(90 * dy)   # small adjustment for next turn
        turtle.pendown()
        
        # Rotate direction for next square
        dir_index = (dir_index + 1) % 4
    
    # ───────────────────────────────────────────────
    # Draw golden spiral approximation using quarter-circles
    # ───────────────────────────────────────────────
    
    turtle.penup()
    turtle.goto(corners[0])     # start at first square corner
    turtle.pendown()
    turtle.pencolor("cyan")
    turtle.pensize(3)
    
    for i in range(1, len(corners)):
        # Center of the quarter circle is the opposite corner of current square
        prev_x, prev_y = corners[i-1]
        curr_x, curr_y = corners[i]
        
        # Simple quarter-circle between corners
        radius = math.hypot(curr_x - prev_x, curr_y - prev_y)
        
        # Determine direction (clockwise or counterclockwise)
        if i % 2 == 1:
            turtle.circle(-radius, 90)   # clockwise
        else:
            turtle.circle(radius, 90)    # counterclockwise
    
    turtle.penup()
    turtle.goto(0, -250)
    turtle.pendown()
    turtle.color("white")
    turtle.write(f"Fibonacci spiral — {n_squares} squares  (scale = {scale})",
                 align="center", font=("Arial", 14, "normal"))
    
    turtle.hideturtle()
    turtle.done()


# =======================
#        Run it!
# =======================

if __name__ == "__main__":
    # Try different values!
    draw_fibonacci_spiral(n_squares=15, scale=6)
    # draw_fibonacci_spiral(18, 8)   # bigger
    # draw_fibonacci_spiral(12, 4)   # smaller & more dense
