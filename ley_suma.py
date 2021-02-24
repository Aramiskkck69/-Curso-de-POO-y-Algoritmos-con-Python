# def f(n):
#
#     for i in range(n):
#         print(i)
#
#
#     for i in range(n * n):
#         print(i)
#
#
# #O(n) + O(n * n) = 0(n + n^2 ) = 0(n^2)

# def f(n):
#     for i in range(n):
#         for j in range(n):
#             print(i, j)
#
# #O(n) * O(n) = O(n * n) = O(n^2)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



if __name__ == '__main__':
    n = int(input("Numero del fibonacci: "))
    print(fibonacci(n))