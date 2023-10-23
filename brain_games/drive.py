def ans_validator(ans, right_ans, name, NUM_CORRECT_ANS):
    """

    :rtype: object
    """
    if str(right_ans) == str(ans):
        print("Correct!")
        NUM_CORRECT_ANS += 1
    else:
        print(f"'{ans}' is wrong answer ;(.", end="")
        print(f"' Correct answer was '{right_ans}'.", end="")
        print("'Let's try again, {0}!".format(name))
        NUM_CORRECT_ANS = 0
    if NUM_CORRECT_ANS == 3:
        print("Congratulations, {0}!".format(name))
    return NUM_CORRECT_ANS
