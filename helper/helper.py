def get_solution_1():
    i = 1
    answer = 0
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            answer += i
        i += 1

    return answer


def get_solution_2():
    answer = 0
    prev = 1
    curr = 2
    while curr < 4000000:
        if curr % 2 == 0:
            answer += curr

        next = prev + curr
        prev = curr
        curr = next

    return answer