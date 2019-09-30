height = float(input('少年，让叔叔给你摸摸你有多高：'))
weight = float(input('少年，让叔叔给你捏捏你有多重：'))
bmi=(weight/(height**2))

if bmi<18:
    print('弱鸡一个!!!')
elif bmi >=18.5 and bmi<=25:
    print('你的BMI是：',('%.2f'%bmi),'；','少年，你保持的不错')
elif bmi>25 and bmi<=28:
    print('你的BMI是：',('%.2f'%bmi),'；','少年，你过重了，加强锻炼~')
elif bmi>28 and bmi<=32:
    print('你的BMI是：',('%.2f'%bmi),'；','少年，你长这么胖，你妈妈知道么！')
elif bmi>32:
    print('你的BMI是：',('%.2f'%bmi),'；','少年，你是吃猪饲料长大的么？')