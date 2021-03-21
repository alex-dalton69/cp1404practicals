"""
Modified program from prac_01 to fit in with SRP.
"""


def main():
    score = float(input("Enter score: "))
    result_of_score = get_result(score)
    print(result_of_score)


def get_result(score):
    if score < 0:
        result_of_score = "Invalid score"
        return result_of_score
    elif score > 100:
        result_of_score = "Invalid score"
        return result_of_score
    else:
        if 50 <= score < 90:
            result_of_score = "Passable"
            return result_of_score
        if 90 <= score < 101:
            result_of_score = "Excellent"
            return result_of_score
        if 50 > score >= 0:
            result_of_score = "Bad"
            return result_of_score


main()
