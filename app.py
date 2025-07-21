import utils

def main():
    name = input("Enter your name: ")
    print("Hello " + name)

    # Bad practice: unused variable
    unused_var = 100

    result = utils.square(3)
    print("Square of 3 is:", result)

if __name__ == "__main__":
    main()
