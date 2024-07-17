# [what is dynamic programming]
def fib(n):
    memo = {}

    def fib_help(n):
        if n in memo:
            return memo[n]
        if n <= 1:
            memo[n] = n
        else:
            memo[n] = fib_help(n - 1) + fib_help(n - 2)
        return memo[n]
    return fib_help(n)
n = int(input("Enter the value of n:"))
res = fib(n)
print(res)
#1 identify the subproblems:
#2 Define the recurrence relation:
#3 Create a Memoozation: 
#4 Build the solution:
#5 return final result:

