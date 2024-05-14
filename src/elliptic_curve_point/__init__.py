def display_elliptic_curve_points(a: int, b: int, p: int) -> None:
    for x in range(p):
        for y in range(p):
            if (y ** 2) % p == (x ** 3 + a * x + b) % p:
                print(f"({x}, {y})")

def main() -> int:
    display_elliptic_curve_points(0, 7, 11)
    return 0
