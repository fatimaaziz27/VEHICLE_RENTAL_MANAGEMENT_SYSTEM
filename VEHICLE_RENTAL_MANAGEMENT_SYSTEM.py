# Vehicle rental details
total_vehicles = 10
vehicles = []
rented_vehicles = []

# Function to show available vehicles
def show_vehicles():
    print(f"\nAvailable vehicles: {len(vehicles)} / {total_vehicles}")

    if not vehicles:
        print("No vehicles available.\n")
    else:
        for v in vehicles:
            print(f"ID: {v['id']}, Model: {v['model']}, Rate: Rs.{v['rate']}/hour")
        print()

# Function to add a vehicle
def add_vehicle():
    if len(vehicles) + len(rented_vehicles) >= total_vehicles:
        print("Vehicle limit reached!\n")
        return

    vehicle_id = input("Enter vehicle ID: ")

    for v in vehicles + rented_vehicles:
        if v["id"] == vehicle_id:
            print("Vehicle ID already exists!\n")
            return

    model = input("Enter vehicle model: ")
    rate = float(input("Enter rental rate per hour (Rs.): "))

    if rate <= 0:
        print("Rental rate must be greater than zero!\n")
        return

    vehicles.append({
        "id": vehicle_id,
        "model": model,
        "rate": rate
    })

    print("Vehicle added successfully!\n")

# Function to rent a vehicle
def rent_vehicle():
    if not vehicles:
        print("No vehicles available for rent!\n")
        return

    vehicle_id = input("Enter vehicle ID to rent: ")

    for v in vehicles:
        if v["id"] == vehicle_id:
            vehicles.remove(v)

            hours = int(input("Enter rental duration in hours: "))

            if hours <= 0:
                vehicles.append(v)
                print("Rental duration must be greater than zero!\n")
                return

            v["hours"] = hours
            v["fee"] = hours * v["rate"]

            rented_vehicles.append(v)

            print(f"Vehicle rented successfully!")
            print(f"Model: {v['model']}")
            print(f"Duration: {hours} hours")
            print(f"Total fee: Rs.{v['fee']}\n")
            return

    print("Vehicle not found!\n")

# Function to return a vehicle
def return_vehicle():
    vehicle_id = input("Enter vehicle ID to return: ")

    for v in rented_vehicles:
        if v["id"] == vehicle_id:
            rented_vehicles.remove(v)

            print(f"Vehicle '{v['model']}' returned successfully!")
            print(f"Rental fee: Rs.{v['fee']}\n")

            del v["hours"]
            del v["fee"]

            vehicles.append(v)
            return

    print("Rented vehicle not found!\n")

# Function to display rented vehicles
def show_rented_vehicles():
    if not rented_vehicles:
        print("No vehicles are currently rented.\n")
    else:
        print("\n--- Rented Vehicles ---")

        for v in rented_vehicles:
            print(
                f"ID: {v['id']}, "
                f"Model: {v['model']}, "
                f"Hours: {v['hours']}, "
                f"Fee: Rs.{v['fee']}"
            )

        print()

# Main loop
while True:
    print("0. Exit")
    print("1. Show Available Vehicles")
    print("2. Add Vehicle")
    print("3. Rent Vehicle")
    print("4. Return Vehicle")
    print("5. Show Rented Vehicles")

    choice = input("Enter your choice: ")

    if choice == "0":
        print("Exiting Vehicle Rental Management System...")
        break
    elif choice == "1":
        show_vehicles()
    elif choice == "2":
        add_vehicle()
    elif choice == "3":
        rent_vehicle()
    elif choice == "4":
        return_vehicle()
    elif choice == "5":
        show_rented_vehicles()
    else:
        print("Invalid choice, try again.\n")
