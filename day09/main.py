import sys
from circle_utils import calc_area, calc_circumference

def main():
    try:
        radius = float(sys.argv[1])  # or use input() if preferred
    except (IndexError, ValueError):
        print("Usage: python main.py <radius>")
        return

    area = calc_area(radius)
    circumference = calc_circumference(radius)

    print(f"The area of your circle is: {area}")
    print(f"The circumference of your circle is: {circumference}")

if __name__ == "__main__":
    main()
