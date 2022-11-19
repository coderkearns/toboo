class Console:
    def ask(self, title, choices=[]):
        print(title)
        for i, choice in enumerate(choices):
            print(f"({i}) {choice}")

        while True:
            try:
                index = int(input("Choose an option: "))
                choice = choices[index]
                return choice
            except KeyboardInterrupt:
                print("\nExiting...")
                quit()
            except:
                print("Please enter a number in the options.")

    def do(self, title, *options):
        opt = self.ask(title, list(map(lambda opt: opt[0], options)))
        return [o[1] for o in options if o[0] == opt][0]()

    def input(self, question):
        try:
            return input(question + " ").strip()
        except KeyboardInterrupt:
            print("\nExiting...")
            quit()


console = Console()
