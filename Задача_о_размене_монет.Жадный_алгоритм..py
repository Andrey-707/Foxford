# Задача о размене монет. Жадный алгоритм.
# Выдать введенную пользователем сумму доступными купюрами (наименьшим количеством).
# Вывести на экран эти купюры.
from rich import print


print("[bold magenta]Program start[/]")

B = [50, 100, 500, 1000, 2000, 5000] # доступные купюры в банкомате
S = int(input("Введите сумму: ")) # сумма, которую необходимо выдать
inf = 10**6 # бесконечность (такого значения для бесконечности для данной задачи достаточно)

# Вариант 1. Список предков. Prev
F = [0] + [inf]*S
Prev = [-1] * (S+1)
for i in range(1, S+1):
    for j in range(len(B)):
        if i - B[j] >= 0 and F[i - B[j]] < F[i]:
            F[i] = F[i - B[j]]
            Prev[i] = B[j]
    F[i] += 1
print("Количество банкнот: " + str(F[S]))
Ans = []
while S > 0:
    Ans.append(Prev[S])
    S -= Prev[S]
print(Ans)

# # Вариант 2. Решение обратным ходом (раскоментировать).
# F = [0] + [inf]*S
# Prev = [-1] * (S+1)
# for i in range(1, S+1):
#     for j in range(len(B)):
#         if i - B[j] >= 0 and F[i - B[j]] < F[i]:
#             F[i] = F[i - B[j]]
#             Prev[i] = B[j]
#     F[i] += 1
# print("Количество банкнот: " + str(F[S]))
# Ans = []
# curr = S
# while curr > 0:
#     for i in range(len(B)):
#         if curr - B[i] >= 0 and F[curr] == F[curr - B[i]] + 1:
#             Ans.append(B[i])
#             curr -= B[i]
# print(Ans)

print("[bold magenta]Program finish[/]")

input() 