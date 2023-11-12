from time import time


def checkText(text, ans):
    errs = []
    small_err = 0

    if len(text) > len(ans):
        errs += [i for i in range(len(ans), len(text))]
        text = text[: len(ans)]

    elif len(text) < len(ans):
        small_err = len(ans) - len(text)

    for i in range(len(text)):
        if text[i] != ans[i]:
            errs.append(i)

    return errs, small_err


def calc_speed(text, time_taken):
    words = len(text) / 5
    return round(words / time_taken * 60, 1)


def_ques = "The quick brown fox jumps over the lazy dog."

ques = input(
    "Enter the text you will be typing during the test (leave empty to select default text)\n : "
)

if not ques:
    ques = def_ques

print(f"Type this :- '{ques}'")
input("Press ENTER whe you are ready")

start_time = time()
text = input()
end_time = time()

errors, small_len_err = checkText(text, ques)

print("\nYour Report:\n")

time_taken = round(end_time - start_time, 3)

print(f"Number of words: {len(text) / 5} (calculated as number of characters / 5)")
print(f"Time Taken: {time_taken}s")
print(f"Speed: {calc_speed(text, time_taken)}wpm")
print(f"Number of mistakes: {len(errors) + small_len_err}")

if len(errors) + small_len_err > 0:
    print("Your mistakes are highlighted by brakets around them")
    for i in range(len(text)):
        if i in errors:
            print(f"[{text[i]}]", end="")
        else:
            print(text[i], end="")
    if small_len_err:
        print(f" ({small_len_err} characters missing)")
