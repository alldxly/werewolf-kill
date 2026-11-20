import random
idtype={'标准':['预','女','猎','白','狼','狼','狼','狼','民','民','民','民'],
        '狼枪守卫':['预','女','猎','守','狼枪','狼','狼','狼','民','民','民','民'],
        '机械狼通灵师':['镜','女','猎','守','机械狼','狼','狼','狼','民','民','民','民']
        }
def newidtype(renshu):
    identities=[]
    for i in range(renshu):
        identity=eval('input("输入身份")')
        identities.append(identity)
    return identities
print('请输入板子类型：标准 或 狼枪守卫 或 机械狼通灵师，或输入其他录入新板子')
try:
    type=str((input()))
    if type in'机械狼通灵师'and type not in'狼枪守卫' and type!='':
        type='机械狼通灵师'
    if type in'狼枪守卫' and type!='':
        type='狼枪守卫'
    if type in'标准' and type!='':
        type='标准'
    identities=idtype[type]
    reid=[]
    reid=identities.copy()

except:
    renshu=int(input('输入板子人数'))
    identities=newidtype(renshu)
players=[]
for i in range(len(identities)):
    remain=len(identities)
    a=random.randint(0,remain-1)
    print(f'{i+1}号的身份是{identities[a]}')
    players.append(identities[a])
    del identities[a]
print(10*'\n')

