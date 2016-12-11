import InputReader
import hashlib

class passwordGenerator:
    @staticmethod
    def generate(string):
        password = ''
        password2 = [None]*8  # empty list to put in found char to correct index
        salt = 0
        while len(password) < 8 or None in password2:
            md5 = hashlib.md5(string + str(salt))
            if md5.hexdigest()[0:5] == "00000":
                password += md5.hexdigest()[5]

                # check if 6th char in hash is an integer, is an index within bounds of pw and no previous value exists for the index
                [value, isInt] = passwordGenerator.intTryParse(md5.hexdigest()[5])
                if isInt and value < 8 and password2[value] is None:
                    password2[value] = md5.hexdigest()[6]

            salt += 1
        print("Generated password: {0}".format(password[0:8]))  # only first 8 chars form the password
        print("Password for second door: {0}".format(''.join(password2)))

    @staticmethod
    def intTryParse(value):
        try:
            return int(value), True
        except ValueError:
            return value, False


def run():
    data = InputReader.read("Inputs/5.txt")
    passwordGenerator.generate(data[0])

if __name__ == "__main__":
    run()
