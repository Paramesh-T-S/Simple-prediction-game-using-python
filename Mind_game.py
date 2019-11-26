class Mind_game:
    def permission(self, prompt, yes_values={"y", "yes"}, no_values={"n", "no"}):
        while True:
            response = input(prompt).strip().lower()
            if response in yes_values:
                return True
            elif response in no_values:
                return False

    def get_int(self, prompt, start=None, end=None):
        while True:
            try:
                value = int(input(prompt))
                if (start is None or start <= value) and (end is None or value <= end):
                    return Value
            except ValueError:
                pass

    def get_one_of(self, prompt, values):
        while True:
            value = input(prompt).strip().lower()
            if value in values:
                return value

    def main(self):
        if obj.permission(
                "Hey! Please guess a number between 1 and 100. I will try to guess what you have guessed. Press 'Y' to play 'N' to exit"):
            start, end = 1, 100
            got_it = False
            for i in range(1, 8):
                mid = (start + end) // 2
                print("I guess {}!".format(mid))
                temp = obj.get_one_of("Is that correct? Write 'Y' for Yes or 'N' or No", {"y", "n"})
                if temp == "y":
                    got_it = True
                    print("You Guessed {} !".format(mid))
                    break

                elif temp == "n":
                    temp1 = obj.get_one_of(
                        "Is the number greater or lesser than {}? Type G for greater and L for Lesser.".format(mid),
                        {"g", "l"})
                    if temp1 == "g":
                        start = mid + 1
                    else:  # temp1 == "l":
                        end = mid - 1
                    if start > end:
                        break

            if got_it:
                print("Guessed it in  {} guesses!".format(i))
            else:
                print("Sry Try again")
        else:
            print("Bye!")


if __name__ == "__main__":
    obj = Mind_game()
    obj.main()
