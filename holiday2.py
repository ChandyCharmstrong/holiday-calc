# Hotel cost function
def hotel_cost(num_nights):
    price_per_night = 100  # Price per night
    return num_nights * price_per_night

# Flight cost function
def plane_cost(city_flight):
    if city_flight == "New York":
        return 800  # Flight cost for New York
    elif city_flight == "Paris":
        return 240  # Flight cost for Paris
    elif city_flight == "Budapest":
        return 65  # Flight cost for Budapest
    elif city_flight == "Milan":
        return 300  # Flight cost for Milan

# Car rental function
def car_rental(rental_days):
    daily_rental_cost = 50  # Daily rental cost
    return rental_days * daily_rental_cost

# Holiday cost function
def holiday_cost(hotel_cost, plane_cost, car_rental):
    return hotel_cost + plane_cost + car_rental

# Get user inputs, call the functions, and print the results
def calculate_holiday():
    print("Available Flights:")
    print("- New York")
    print("- Paris")
    print("- Budapest")
    print("- Milan")

    available_flights = ["New York", "Paris", "Budapest", "Milan"]

    # Validate user input for city_flight
    while True:
        city_flight = input("Enter the city you will be flying to: ").title()
        if city_flight not in available_flights:
            print("Invalid flight entered. Please try again.")
        else:
            break

    # Validate user input for num_nights
    valid_number = False
    while not valid_number:
        try:
            num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
            if num_nights < 0:
                print("Invalid number of nights entered. Please try again.")
            else:
                valid_number = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Validate user input for rental_days
    valid_number = False
    while not valid_number:
        try:
            rental_days = int(input("Enter the number of days you will be renting a car: "))
            if rental_days < 0:
                print("Invalid number of rental days entered. Please try again.")
            else:
                valid_number = True
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    hotel_total_cost = hotel_cost(num_nights)
    plane_total_cost = plane_cost(city_flight)
    car_rental_total_cost = car_rental(rental_days)
    total_cost = holiday_cost(hotel_total_cost, plane_total_cost, car_rental_total_cost)

    # Print holiday details
    print("\n-------- Holiday Details --------\n") # love this
    print(f"City Flight: {city_flight}")
    print(f"Number of Nights: {num_nights}")
    print(f"Number of Rental Days: {rental_days}")
    print(f"Hotel Cost: ${hotel_total_cost}")
    print(f"Flight Cost: ${plane_total_cost}")
    print(f"Car Rental Cost: ${car_rental_total_cost}")
    print(f"Total Cost: ${total_cost}")

# Main program loop
while True:
    calculate_holiday()
    print()
    choice = input("Would you like to calculate more holiday datails? (yes/no): ")
    if choice.lower() != "yes":
        break

# Works great - feels like I've built something here! 