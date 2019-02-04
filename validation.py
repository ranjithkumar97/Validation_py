class Validation:

    def number_validation(self, l):
        while True:
            number =input()
            if number.isdigit():
                leng = len(number)
                if leng == l:
                    break
                else:
                    print("Invalid Length")
                    print("Enter a valid Input")
                    continue
            else:
                print("The field should be in numbers :")
                continue
        return number

    def alpha_number_validation(self, la):
        while True:
            self.alphanumber =input()
            print
            len(self.alphanumber)
            if self.alphanumber.isalnum():
                if len(self.alphanumber) == la:
                    print("Invalid Format")
                    print("Enter a valid input")
                else:
                    break
            else:
                print("The field should be in alpha numeric :")
                continue

        return self.alphanumber

    def string_validation(self):
        while True:
            self.name = raw_input()
            if self.name.isalpha():
                break
            else:
                print
                "Invalid Format"
        return self.name
