import csv

# Function to add an entry (income/expense)
def add_entry(entries, entry_type):
    description = input(f"Enter {entry_type} description: ").strip()
    while not description:
        print("Description cannot be empty.")
        description = input(f"Enter {entry_type} description: ").strip()
    
    while True:
        try:
            amount = float(input(f"Enter {entry_type} amount: "))
            if amount <= 0:
                raise ValueError("Amount must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid amount.")
    
    entry = {"type": entry_type, "description": description, "amount": amount}
    entries.append(entry)
    print(f"{entry_type.capitalize()} of {amount} added.\n")

# Function to display all entries and calculate the balance
def display_entries(entries):
    income_total = 0
    expense_total = 0
    print("\nSummary of Transactions:")
    print(f"{'Type':<10} | {'Description':<20} | {'Amount':>10}")
    print("-" * 45)
    
    for entry in entries:
        print(f"{entry['type']:<10} | {entry['description']:<20} | {entry['amount']:>10.2f}")
        if entry["type"] == "income":
            income_total += entry["amount"]
        else:
            expense_total += entry["amount"]

    balance = income_total - expense_total
    print("-" * 45)
    print(f"Total Income: {income_total:.2f}")
    print(f"Total Expenses: {expense_total:.2f}")
    print(f"Current Balance: {balance:.2f}\n")

def save_to_file(entries, filename=None):
    if not filename:
        filename = input("Enter filename to save (default: entries.csv): ").strip() or "entries.csv"
    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["type", "description", "amount"])
        writer.writeheader()
        writer.writerows(entries)
    print(f"Entries saved to {filename}.\n")

def load_from_file(filename=None):
    if not filename:
        filename = input("Enter filename to load (default: entries.csv): ").strip() or "entries.csv"
    entries = []
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                entries.append(row)
        print(f"Entries loaded from {filename}.\n")
    except FileNotFoundError:
        print(f"No previous entries found in {filename}. Starting fresh.\n")
    return entries

# Main function
def main():
    print("Welcome to the Basic Expense Tracker!")
    entries = load_from_file()  # Load previous entries from file if they exist

    while True:
        print("Menu:")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Summary")
        print("4. Save and Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            add_entry(entries, "income")
        elif choice == "2":
            add_entry(entries, "expense")
        elif choice == "3":
            display_entries(entries)
        elif choice == "4":
            save_to_file(entries)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
