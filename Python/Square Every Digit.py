# Square Every Digit
def square_digits(num):
    first_num = num
    answer = ""
    for i in str(first_num):
        answer += str(int(i) ** 2)
    answer = int(answer)
    return(answer)```
