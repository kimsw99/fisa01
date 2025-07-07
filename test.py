alist = ['사과', '바나나', '딸기']
blist = ['Apple', 'Banana', 'Strawberry']

[print(idx, v0, v1) for idx, (v0, v1) in enumerate(zip(alist, blist))]