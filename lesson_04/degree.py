print('"Назождение наибольшей целой степени двойки"')
n = int(input('Введите натуральное число: '))
if n <= 0:
    print('Это число не натуральное, попробуйте еще раз.')
else:
    dgr = 2
    cnt = 0
    while dgr <= n:
        dgr *= 2
        cnt += 1
    print(n, '\t', cnt, dgr // 2, '\t2 **', cnt, '=', dgr // 2)
