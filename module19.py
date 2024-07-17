def Divisor_Queries(N, Q, a, Queries):
    result = []

    def smallest_prime_factor(x):
        for i in range(2, int(x**0.5) + 1):
            if x % i == 0:
                return i
        return x

    for query in Queries:
        query_type, l, r = query

        if query_type == 1:
            smallest_divisor = smallest_prime_factor(a[l - 1])
            for i in range(l - 1, r):
                a[i] //= smallest_divisor

        elif query_type == 2:
            result.append(sum(a[l:r]))

    for sum_value in result:
        print(sum_value)

# Custom input
N = 5
Q = 3
a = [10, 2, 8, 7, 6]
Queries = [[2, 1, 4], [1, 1, 4], [2, 1, 4]]

Divisor_Queries(N, Q, a, Queries)
