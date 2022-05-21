import time
import format

continue_timer = True
print("- Timer -")


def countdown():
    countdown_ans = input("Countdown? (Y/N): ")
    if countdown_ans.upper() == "Y":
        countdown_time = int(input("Enter countdown time in seconds: "))
        input("(Press ENTER to start countdown)\n")
        while countdown_time > 0:
            print(countdown_time)
            time.sleep(1)
            countdown_time -= 1

    elif countdown_ans.upper() == "N":
        input("(Press ENTER to start)")

def timer():
    init_time = time.time()
    print("\nSTART\n")
    input("(Press ENTER to stop)")
    fin_time = time.time()
    elapsed_time = round(fin_time - init_time, 3)
    return elapsed_time

while continue_timer:
    countdown()
    print(format.format_time(timer()))

    continue_ans = input("\nRestart timer? (Y/N): ")

    invalid_answer = True
    while invalid_answer:

        if continue_ans.upper() == "N":
            continue_timer = False
            invalid_answer = False
        elif continue_ans.upper() == "Y":
            continue_timer = True
            invalid_answer = False
        else:
            continue_ans = input("Please enter a valid answer (Y/N): ")                
                
