from database import DatabaseManager


class CourseFeeCalculator:
    CORE_FEE = 200000
    HOSTEL_FEE = 200000
    FOOD_MONTHLY = 2000
    TRANSPORT_SEMESTER = 13000

    def __init__(self):
        self.db = DatabaseManager()
        self.course_name = None
        self.analytics = False
        self.hostel = False
        self.food_months = 0
        self.transport = "none"

    def get_valid_input(self, prompt, options):
        """get validated user input"""
        while True:
            value = input(prompt).strip().upper()
            if value in options:
                return value
            print(f"choose from: {', '.join(options)}")

    def run(self):
        print("master fees calculator")
        print("=" * 50)

        if not self.db.connect():
            print("cannot connect to database!")
            return

        try:

            self.db.create_table()
            courses = self.db.get_courses()

            print("\navailable Courses:")
            for course in courses:
                print(f"  {course[0]}", end="")
                if course[1]:
                    print(" (analytics available)")
                else:
                    print()

            print("\n" + "=" * 50)
            self.course_name = self.get_valid_input(
                "enter course: ", [course[0] for course in courses]
            )

            analytics_avail = next(
                course[1] for course in courses if course[0] == self.course_name
            )
            if analytics_avail:
                self.analytics = (
                    self.get_valid_input("analytics? (Y/N): ", ["Y", "N"]) == "Y"
                )

            self.hostel = self.get_valid_input("hostel? (Y/N): ", ["Y", "N"]) == "Y"

            while True:
                try:
                    self.food_months = int(input("food months (0-12): "))
                    if 0 <= self.food_months <= 12:
                        break
                    print("enter 0-12 only!")
                except ValueError:
                    print("enter valid number!")

            self.transport = self.get_valid_input(
                "transport? (semester/annual/none): ", ["SEMESTER", "ANNUAL", "NONE"]
            ).lower()

            self.calculate_fees()
            self.display_breakdown()

        except KeyboardInterrupt:
            print("\nGoodbye!")
        except Exception as e:
            print(f"Error: {e}")
        finally:
            self.db.close()

    def calculate_fees(self):
        """calculate total fees"""
        self.course_fee = self.CORE_FEE
        if self.analytics:
            self.course_fee *= 1.10

        self.hostel_fee = self.HOSTEL_FEE if self.hostel else 0
        self.food_fee = self.food_months * self.FOOD_MONTHLY

        if self.transport == "semester":
            self.transport_fee = self.TRANSPORT_SEMESTER
        elif self.transport == "annual":
            self.transport_fee = self.TRANSPORT_SEMESTER * 2
        else:
            self.transport_fee = 0

        self.total_fee = (
            self.course_fee + self.hostel_fee + self.food_fee + self.transport_fee
        )

    def display_breakdown(self):
        """display fee breakdown"""
        print("\n" + "=" * 50)
        print("cost breakdown")
        print(f"course ({self.course_name}", end="")
        if self.analytics:
            print(" + analytics", end="")
        print(f"): Rs.{self.course_fee:,.0f}")

        print(f"hostel: Rs.{self.hostel_fee:,.0f}")
        print(f"food ({self.food_months} months): Rs.{self.food_fee:,.0f}")
        print(f"transport ({self.transport}): Rs.{self.transport_fee:,.0f}")
        print("=" * 50)
        print(f"total annual fees : Rs.{self.total_fee:,.0f}")
        print("=" * 50)


if __name__ == "__main__":
    calculator = CourseFeeCalculator()
    calculator.run()


