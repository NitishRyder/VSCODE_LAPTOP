def fruit_grading(diameter):
    if diameter < 5:
        return "Small"
    elif 5 <= diameter < 10:
        return "Medium"
    else:
        return "Large"

def main():
    try:
        diameter = float(input("Enter the diameter of the fruit (in centimeters): "))
        if diameter <= 0:
            print("Please enter a valid positive number for the diameter.")
        else:
            grade = fruit_grading(diameter)
            print(f"The fruit is classified as: {grade}")
    except ValueError:
        print("Invalid input. Please enter a valid number for the diameter.")

if __name__ == "__main__":
    main()
