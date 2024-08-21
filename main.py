# Dice sum probability calculator
# Författare: David Berno
# Datum: 2024-08-21

def main():
    user_input = input().split(" ")
    dice_one = int(user_input[0])
    dice_two = int(user_input[1])

    for d in range(1, dice_one + 1):
        for g in range(1, dice_two + 1):
            print(d+g)

if __name__ == "__main__":
    main()
