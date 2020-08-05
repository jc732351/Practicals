
def main():
    score = float(input("Enter score: "))
    get_score(score)
    random_score(score)

def get_score(score):
        print("Bad")
    elif 50 <= score < 90:
        print("Passable")
    elif 90 <= score <= 100:
        print("Excellent")
    else:
        print("Invalid score")
    return score


from random import randint
def random_score(score):
    score=randint(1,100)
    print(score)

main()