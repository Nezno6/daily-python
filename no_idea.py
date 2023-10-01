def calc_happiness(value_board: list,set_positive: set,set_negative: set):
    positive_points = len([value for value in value_board if set_positive.__contains__(value)])
    negative_points = len([value for value in value_board if set_negative.__contains__(value)])
    return positive_points - negative_points

if __name__ == "__main__":
    _ = input()
    value_board =[int(value) for value in input().split(" ")]
    set_positive = {int(value) for value in input().split(" ")}
    set_negative = {int(value) for value in input().split(" ")}
    print(calc_happiness(value_board,set_positive,set_negative))