# #
# a = [1, 3, 5, 7, 9, 11, 11, 12]
# b = [1, 4, 6, 8, 12]
#
# result = []
# for i in a:
#     for j in b:
#         if i not in result and j not in result:
#             if i < j:
#                 result.append(i)
#             else:
#                 result.append(j)
#
# if len(a) == len(b):
#     result.append(max(a[-1], b[-1]))
# elif len(a) < len(b):
#     for i in b[len(a) - len(b) - 1:]:
#         if i not in result:
#             result.append(i)
# else:
#     for i in a[len(b) - len(a):]:
#         if i not in result:
#             result.append(i)
#
# print(result)



# path_a = sys.argv[1]
# path_b = sys.argv[2]
# path_result = sys.argv[3]



# -------------------------------------
#
a = [1, 2, 15, 19, 25]
b = [1, 3, 5, 7, 8, 9, 10, 11, 15, 16, 17, 18, 22, 23, 24]
result = []
i, j = 0, 0
while True:
    if j == len(b):
        while i != len(a):
            result.append(a[i])
            i += 1

    if i == len(a):
        while j != len(b):
            result.append(b[j])
            j += 1

    if i < len(a):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1

    if i == len(a) and j == len(b):
        break




    # if len(a) == len(b):
    #     result.append(max(a[-1], b[-1]))
    # elif len(a) < len(b):
    #     for i in b[len(a) - len(b) - 1:]:
    #         if i not in result:
    #             result.append(i)
    # else:
    #     for i in a[len(b) - len(a):]:
    #         if i not in result:
    #             result.append(i)

print(result)

# result = []
# for i in a:
#     for j in b:
#         if i not in result and j not in result:
#             if i < j:
#                 result.append(i)
#             else:
#                 result.append(j)
#
# if len(a) == len(b):
#     result.append(max(a[-1], b[-1]))
# elif len(a) < len(b):
#     for i in b[len(a) - len(b) - 1:]:
#         if i not in result:
#             result.append(i)
# else:
#     for i in a[len(b) - len(a):]:
#         if i not in result:
#             result.append(i)
#
# print(result)