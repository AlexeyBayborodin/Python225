# n = [int(input("-> ")) for i in range(int(input("n = ")))]
#
# for i in range(len(n)):
#     if i % 2 == 0:
#         print(n[i], end=" ")

n1 = [2, 9, 4, 6, 3, 5]
for i in range(len(n1) - 1):
    a = n1[i]
    i += 1
    b = n1[i]
    if a < b:
        print(b, end=" ")