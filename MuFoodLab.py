class MuFoodLab:
    def __init__(self):
        self.is_logged_in = False
        self.order_list = []
        self.order_list.append(f"Code\tPrice\tQty\tUnit\tTotal")
        self.total_cost = 0

    def login(self):
        while not self.is_logged_in:
            login_id = input("Enter Login ID: ")
            password = input("Enter Password: ")

            if login_id == "Musa" and password == "7517":
                self.is_logged_in = True
                print("Login Successful")
            else:
                print("Login Failed. Try Again.")

    def order_food(self):
        if not self.is_logged_in:
            print("You must log in first.")
            return

        print("\nHey Foodie! Order Food Now :)")
        print("Available Items\n=> Code 01.Chicken Biriyani = 160/=\n=> Code 02.Kacci Biriyani = 290/=\n=> Code 03.Egg Pulao = 60/=\n")
        z = 1
        while z != 0:
            l1 = input("Enter Item Code: ")
            l2 = self.get_item_price(l1, {
                "01": 160,
                "02": 290,
                "03": 60,
            })

            if l2 is None:
                print("Invalid item code. Please try again.")
                continue

            l3 = int(input("Enter Item Quantity: "))
            l5 = input("Enter Item Unit: ")
            l4 = l2 * l3
            self.order_list.append(f"\t{l1}\t{l2}\t{l3}\t{l5}\t{l4}")
            self.total_cost += l4
            z = int(input("Enter 1 to Continue and 0 to Stop: "))

    def breakfast(self):
        if not self.is_logged_in:
            print("You must log in first.")
            return

        print("\nLet's Enjoy Fresh and Healthy Breakfast :)")
        print("Available Items\n=> Code 04.Chicken Kisuri = 50/=\n=> Code 05.Vegetable Parata = 40/=\n=> Code 06.Chocolate Cake = 20/=\n")
        z = 1
        while z != 0:
            l1 = input("Enter Item Code: ")
            l2 = self.get_item_price(l1, {
                "04": 50,
                "05": 40,
                "06": 20,
            })

            if l2 is None:
                print("Invalid item code. Please try again.")
                continue

            l3 = int(input("Enter Item Quantity: "))
            l5 = input("Enter Item Unit: ")
            l4 = l2 * l3
            self.order_list.append(f"\t{l1}\t{l2}\t{l3}\t{l5}\t{l4}")
            self.total_cost += l4
            z = int(input("Enter 1 to Continue and 0 to Stop: "))

    def lunch(self):
        if not self.is_logged_in:
            print("You must log in first.")
            return

        print("\nOoh! Let's Take the Most Important Meal of the Day")
        print("\n !!Rice is Free With Dishes!!")
        print("Available Items\n=> Code 07.Fish = 150/=\n=> Code 08.Beef = 180/=\n=> Code 09.Chicken = 140/=\n")
        z = 1
        while z != 0:
            l1 = input("Enter Item Code: ")
            l2 = self.get_item_price(l1, {
                "07": 150,
                "08": 180,
                "09": 140,
            })

            if l2 is None:
                print("Invalid item code. Please try again.")
                continue

            l3 = int(input("Enter Item Quantity: "))
            l5 = input("Enter Item Unit: ")
            l4 = l2 * l3
            self.order_list.append(f"\t{l1}\t{l2}\t{l3}\t{l5}\t{l4}")
            self.total_cost += l4
            z = int(input("Enter 1 to Continue and 0 to Stop: "))

    def snacks(self):
        if not self.is_logged_in:
            print("You must log in first.")
            return

        print("\nHey Foodie! Order Snacks Now :)")
        print("Available Items\n=> Code 10.Singhara = 10/=\n=> Code 11.Samosa = 15/=\n=> Code 12.Burger = 65/=\n")
        z = 1
        while z != 0:
            l1 = input("Enter Item Code: ")
            l2 = self.get_item_price(l1, {
                "10": 10,
                "11": 15,
                "12": 65,
            })

            if l2 is None:
                print("Invalid item code. Please try again.")
                continue

            l3 = int(input("Enter Item Quantity: "))
            l5 = input("Enter Item Unit: ")
            l4 = l2 * l3
            self.order_list.append(f"\t{l1}\t{l2}\t{l3}\t{l5}\t{l4}")
            self.total_cost += l4
            z = int(input("Enter 1 to Continue and 0 to Stop: "))

    def get_item_price(self, item_code, item_prices):
        return item_prices.get(item_code)

    def view_order(self):
        if not self.is_logged_in:
            print("You must log in first.")
            return

        if self.order_list:
            for item in self.order_list:
                print(item)
            print(f"Total Cost: {self.total_cost} BDT")

    def exit_program(self):
        print("Thank you for using MU Food Lab. Have a great day!")
        if self.order_list:
            print("Your Final Invoice:")
            self.view_order()

    def run(self):
        while not self.is_logged_in:
            self.login()

        while True:
            print("\nChoose Your Option:")
            print("1: Order Food")
            print("2: Breakfast")
            print("3: Lunch")
            print("4: Snacks")
            print("5: Exit")

            option = input("Enter Number 1-5 to operate: ")

            if option == "1":
                self.order_food()
            elif option == "2":
                self.breakfast()
            elif option == "3":
                self.lunch()
            elif option == "4":
                self.snacks()
            elif option == "5":
                self.exit_program()
                break
            else:
                print("Invalid entry. Please enter a valid option.")

if __name__ == "__main__":
    food_order_system = MuFoodLab()
    food_order_system.run()
