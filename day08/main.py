from circle_module import get_radius, calculate_area, calculate_circumference, print_results

def main():
    r = get_radius()
    area = calculate_area(r)
    circumference = calculate_circumference(r)
    print_results(area, circumference)

if __name__ == "__main__":
    main()
