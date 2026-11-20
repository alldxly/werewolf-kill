import 狼人杀发牌器 as c
import copy
clergy=[]
ordinary=[]
werewolf=[]
for i in range(len(c.reid)):
    if i<4:
        clergy.append(c.reid[i])
    if 4<=i<8:
        werewolf.append(c.reid[i])
    if 8<=i<12:
        ordinary.append(c.reid[i])
recl=clergy.copy()
reor=ordinary.copy()
rewe=werewolf.copy()
pdict={}
for i in range(len(c.reid)):
    pdict[i+1]=c.players[i]
print(pdict)
pred=[]
alldi=[]
def yu(alldi,yun):#alldi：已死亡的序号，yun：已经查验的玩家序号
        try:
            while True:
                yunum=int(input('输入查验的号码'))
                if yunum in pred or yunum in alldi:
                    print('对方已被查验或死亡，请重新输入')
                    continue
                if yunum==yun:
                    print('无法查验自己，请重新输入')
                    continue
                pred.append(yunum)#添加被查验的序号
                break
            if pdict[yunum] not in werewolf:
                print(f'今晚查验的{yunum}号玩家为好人')
            else:
                print(f'今晚查验的{yunum}号玩家为狼人')
        except:
            print(f'今晚无人被查验')
def wes(pdict,clergy,werewolf,ordinary,alldi):#pdict：所有玩家身份，clergy：所有神职，werewolf：所有狼人，ordinary：所有平民，alldi：所有死亡的玩家
    try:
        while True:
            wenum=int(input('输入击杀的号码'))
            if wenum in alldi:
                print('对方已死亡，请重新输入')
                continue
            wedi=pdict[wenum]
            for j in range(len(clergy)):
                if wedi==clergy[j]:
                    del clergy[j]
                    break
            for k in range(len(werewolf)):
                if wedi==werewolf[k]:
                    del werewolf[k]
                    break
            for m in range(len(ordinary)):
                if wedi==ordinary[m]:
                    del ordinary[m]
                    break
            twed=pdict[wenum]
            pdict[wenum]='已死亡'
            break
    except:
        print('无人被击杀')
        wedi='a'
        wenum=-1
        twed=''
    return pdict,clergy,werewolf,ordinary,wedi,wenum,alldi,twed#wedi：狼人击杀的玩家，wenum：狼人击杀的玩家号码
def we(pdict,clergy,werewolf,ordinary,alldi):#pdict：所有玩家身份，clergy：所有神职，werewolf：所有狼人，ordinary：所有平民，alldi：所有死亡的玩家
    try:
        while True:
            wenum=int(input('输入击杀的号码'))
            if wenum in alldi:
                print('对方已死亡，请重新输入')
                continue
            wedi=pdict[wenum]
            for j in range(len(clergy)):
                if wedi==clergy[j]:
                    del clergy[j]
                    break
            for k in range(len(werewolf)):
                if wedi==werewolf[k]:
                    del werewolf[k]
                    break
            for m in range(len(ordinary)):
                if wedi==ordinary[m]:
                    del ordinary[m]
                    break
            
            pdict[wenum]='已死亡'
            break
    except:
        print('无人被击杀')
        wedi='a'
        wenum=-1
        
    return pdict,clergy,werewolf,ordinary,wedi,wenum,alldi#wedi：狼人击杀的玩家，wenum：狼人击杀的玩家号码

def nvs(pdict,clergy,werewolf,ordinary,wedi,recl,rewe,reor,wenum,res,rep,alldi,shounu,twed):#recl，神职副本，用于女巫救人后添加回元素，rewe：狼人副本，reor：平民副本，res：伤药数量，rep：毒药数量，shounu：守卫号码
    try:
        if wedi!='a':
            if res==1 and rep==1:
                print(f'今晚{wenum}号玩家死亡')
                while True:
                    nvnum=int(input('输入0救人，或输入毒杀的号码，均不执行输入回车'))
                    if wedi=='女' and nvnum==0:
                        print('女巫无法自救，请重新输入')
                        continue
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    if nvnum==0:
                        res=0
                        if shounu!=wenum and ('守' in pdict.values() or twed=='守'):
                            if wedi in recl:
                                clergy.append(wedi)
                            if wedi in rewe:
                                werewolf.append(wedi)
                            if wedi in reor:
                                ordinary.append(wedi)
                            pdict[wenum]=wedi
                        else:
                            alldi.append(wenum)
                        du1=0
                        du2=0
                        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2#du1：猎人被读状态
                    else:
                        if shounu==wenum and ('守' in pdict.values() or twed=='守'):
                            if wedi in recl:
                                clergy.append(wedi)
                            if wedi in rewe:
                                werewolf.append(wedi)
                            if wedi in reor:
                                ordinary.append(wedi)
                            pdict[wenum]=wedi
                        else:
                            alldi.append(wenum)
                        nvdi=pdict[nvnum]
                        if  nvdi=='猎'or nvdi=='已死亡':
                            du1=1
                            du2=0
                        elif  nvdi=='狼枪' or nvdi=='已死亡':
                            du1=0
                            du2=1
                        else:
                            du1=0
                            du2=0
                        for j in range(len(clergy)):
                            if nvdi==clergy[j]:
                                del clergy[j]
                                break
                        for k in range(len(werewolf)):
                            if nvdi==werewolf[k]:
                                del werewolf[k]
                                break
                        for m in range(len(ordinary)):
                            if nvdi==ordinary[m]:
                                del ordinary[m]
                                break
                        pdict[nvnum]='已死亡'
                        rep=0
                        alldi.append(nvnum)
                        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==1 and rep==0:
                print(f'今晚{wenum}号玩家死亡')
                nvnum=int(input('输入0救人,不执行输入回车'))
                if wedi=='女' and nvnum==0:
                    print('女巫无法自救')
                    du1=0
                    du2=0
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
                if nvnum==0:
                    res=0
                    if shounu!=wenum and ('守' in pdict.values() or twed=='守'):
                        if wedi in recl:
                            clergy.append(wedi)
                        if wedi in rewe:
                            werewolf.append(wedi)
                        if wedi in reor:
                            ordinary.append(wedi)
                        pdict[wenum]=wedi
                    else:
                        alldi.append(wenum)
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==1:
                if shounu==wenum and ('守' in pdict.values() or twed=='守'):
                    if wedi in recl:
                        clergy.append(wedi)
                    if wedi in rewe:
                        werewolf.append(wedi)
                    if wedi in reor:
                        ordinary.append(wedi)
                    pdict[wenum]=wedi
                else:
                    alldi.append(wenum)
                while True:
                    nvnum=int(input('输入毒杀的号码，不执行输入回车'))
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if  nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif  nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep=0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==0:
                print('不可操作')
                du1=0
                du2=0
                if shounu==wenum and ('守' in pdict.values() or twed=='守'):
                    if wedi in recl:
                        clergy.append(wedi)
                    if wedi in rewe:
                        werewolf.append(wedi)
                    if wedi in reor:
                        ordinary.append(wedi)
                    pdict[wenum]=wedi
                else:
                    alldi.append(wenum)
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
        else:
            if res==1 and rep==1:
                while True:
                    nvnum=int(input('今晚无人死亡,输入毒杀的号码，不执行输入回车'))
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep==0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==1 and rep==0:
                print('今晚无人死亡')
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==1:
                while True:
                    nvnum=int(input('输入毒杀的号码，不执行输入回车'))
                    if nv in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep==0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==0:
                print('不可操作')
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
    except:
        if shounu==wenum and ('守' in pdict.values() or twed=='守'):
            if wedi in recl:
                clergy.append(wedi)
            if wedi in rewe:
                werewolf.append(wedi)
            if wedi in reor:
                ordinary.append(wedi)
            pdict[wenum]=wedi
        else:
            alldi.append(wenum)
        print('无人被救或被毒杀')
        du1=0
        du2=0
        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2


    
def nv(pdict,clergy,werewolf,ordinary,wedi,recl,rewe,reor,wenum,res,rep,alldi,shounu):#recl，神职副本，用于女巫救人后添加回元素，rewe：狼人副本，reor：平民副本，res：伤药数量，rep：毒药数量，shounu：守卫号码
    try:
        if wedi!='a':
            if res==1 and rep==1:
                print(f'今晚{wenum}号玩家死亡')
                while True:
                    nvnum=int(input('输入0救人，或输入毒杀的号码，均不执行输入回车'))
                    if wedi=='女' and nvnum==0:
                        print('女巫无法自救，请重新输入')
                        continue
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    if nvnum==0:
                        res=0
                        
                        if wedi in recl:
                            clergy.append(wedi)
                        if wedi in rewe:
                            werewolf.append(wedi)
                        if wedi in reor:
                            ordinary.append(wedi)
                        pdict[wenum]=wedi

                        du1=0
                        du2=0
                        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2#du1：猎人被读状态
                    else:
                        
                        alldi.append(wenum)
                        nvdi=pdict[nvnum]
                        if  nvdi=='猎'or nvdi=='已死亡':
                            du1=1
                            du2=0
                        elif  nvdi=='狼枪' or nvdi=='已死亡':
                            du1=0
                            du2=1
                        else:
                            du1=0
                            du2=0
                        for j in range(len(clergy)):
                            if nvdi==clergy[j]:
                                del clergy[j]
                                break
                        for k in range(len(werewolf)):
                            if nvdi==werewolf[k]:
                                del werewolf[k]
                                break
                        for m in range(len(ordinary)):
                            if nvdi==ordinary[m]:
                                del ordinary[m]
                                break
                        pdict[nvnum]='已死亡'
                        rep=0
                        alldi.append(nvnum)
                        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==1 and rep==0:
                print(f'今晚{wenum}号玩家死亡')
                nvnum=int(input('输入0救人,不执行输入回车'))
                if wedi=='女' and nvnum==0:
                    print('女巫无法自救')
                    du1=0
                    du2=0
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
                if nvnum==0:
                    res=0
                    pdict[wenum]=wedi
                else:
                    alldi.append(wenum)
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==1:
                alldi.append(wenum)
                while True:
                    nvnum=int(input('输入毒杀的号码，不执行输入回车'))
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if  nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif  nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep=0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==0:
                print('不可操作')
                du1=0
                du2=0
                alldi.append(wenum)
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
        else:
            if res==1 and rep==1:
                while True:
                    nvnum=int(input('今晚无人死亡,输入毒杀的号码，不执行输入回车'))
                    if nvnum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep==0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==1 and rep==0:
                print('今晚无人死亡')
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==1:
                while True:
                    nvnum=int(input('输入毒杀的号码，不执行输入回车'))
                    if nv in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    nvdi=pdict[nvnum]
                    if nvdi=='猎'or nvdi=='已死亡':
                        du1=1
                        du2=0
                    elif nvdi=='狼枪' or nvdi=='已死亡':
                        du1=0
                        du2=1
                    else:
                        du1=0
                        du2=0
                    for j in range(len(clergy)):
                        if nvdi==clergy[j]:
                            del clergy[j]
                            break
                    for k in range(len(werewolf)):
                        if nvdi==werewolf[k]:
                            del werewolf[k]
                            break
                    for m in range(len(ordinary)):
                        if nvdi==ordinary[m]:
                            del ordinary[m]
                            break
                    pdict[nvnum]='已死亡'
                    rep==0
                    alldi.append(nvnum)
                    return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
            if res==0 and rep==0:
                print('不可操作')
                du1=0
                du2=0
                return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2
    except:
        print('无人被救或被毒杀')
        du1=0
        du2=0
        return pdict,clergy,werewolf,ordinary,du1,res,rep,alldi,du2


    
def lie(pdict,clergy,werewolf,ordinary,alldi):
    try:
        while True:
            lienum=int(input('输入枪杀的号码'))
            if lienum in alldi:
                print('对方已死亡，请重新输入')
                continue
            liedi=pdict[lienum]
            for j in range(len(clergy)):
                if liedi==clergy[j]:
                    del clergy[j]
                    break
            for k in range(len(werewolf)):
                if liedi==werewolf[k]:
                    del werewolf[k]
                    break
            for m in range(len(ordinary)):
                if liedi==ordinary[m]:
                    del ordinary[m]
                    break
            pdict[lienum]='已死亡'
            used=1#猎人开枪状态
            alldi.append(lienum)#加入猎人枪杀的目标
            break
    except:
        print('无人被枪杀')
        used=1
    return pdict,clergy,werewolf,ordinary,used,alldi
def tou(pdict,alldi):
    cop=copy.deepcopy(pdict)
    total=[0,0,0,0,0,0,0,0,0,0,0,0,0]
    list={}
    for i in range(len(pdict.keys())):
        try:
            if pdict[i+1]!='已死亡':
                while True:
                    tounum=int(input('输入投票处决的对象'))
                    if tounum in alldi:
                        print('对方已死亡，请重新输入')
                        continue
                    break
                total[tounum]+=1#对应列表人数得票加一
                list[i+1]=tounum#记录名单，从1号开始投票的是谁。
        except:
            continue
    if len(list)>0:
        for i in list.keys():
            print(f'第{i}名玩家投票给{list[i]}')
        maxinum=max(total)
        maxx=[]
        for i in range(len(total)):
            if maxinum==total[i]:
                maxx.append(i)
        if len(maxx)==1:
            exe=maxx[0]
        else:
            print(maxx)
            list={}
            total=[0,0,0,0,0,0,0,0,0,0,0,0,0]
            for i in maxx:
                if i in cop:
                    del cop[i]
            for i in range(len(cop.keys())):
                try:
                    
                    while True:
                        tounum=int(input('输入投票处决的对象'))
                        if tounum not in maxx:
                            print('请在平票的人中投票')
                            continue
                        break
                    total[tounum]+=1#对应列表人数得票加一
                    list[i+1]=tounum#记录名单，从1号开始投票的是谁。
                except:
                    continue
            for i in list.keys():
                print(f'第{i}号玩家投票给{list[i]}')
                maxinum=max(total)
            maxx=[]
            for i in range(len(total)):
                if maxinum==total[i]:
                    maxx.append(i)
            if len(maxx)==1:
                exe=maxx[0]
            else:
                exe='a'
        return exe
    else:
        print('全部玩家弃票')
        return 'a'
    
    
    
            
                    
def pi(pdict,clergy,werewolf,ordinary,alldi,exe):
    try:
        while True:
            pinum=exe
            pidi=pdict[pinum]
            if pidi!='白':
                for j in range(len(clergy)):
                    if pidi==clergy[j]:
                        del clergy[j]
                        break
                for k in range(len(werewolf)):
                    if pidi==werewolf[k]:
                        del werewolf[k]
                        break
                for m in range(len(ordinary)):
                    if pidi==ordinary[m]:
                        del ordinary[m]
                        break
                pdict[pinum]='已死亡'
                alldi.append(pinum)
                print(f'处决的是{exe}号玩家')
                break
            else:
                print('被处决的为白痴，免除本次处决')
                break
    except:
        print('无人被处决')
    return pdict,clergy,werewolf,ordinary,alldi
def shou(alldi,shoued):
    try:
        while True:
            shounu=int(input('输入守护的目标'))
            if shounu==shoued:
                print('无法连续守护同一玩家，请重新输入')
                continue
            if shounu in alldi:
                print('对方已死亡，请重新输入')
                continue
            shoued=shounu
            break
        return shoued
    except:
        print('无人被守护')
def langq(pdict,clergy,werewolf,ordinary,alldi):
    try:
        while True:
            langqnu=int(input('输入反杀的玩家'))
            if langqnu in alldi:
                print('对方已死亡，请重新输入')
                continue
            langqdi=pdict[langqnu]
            for j in range(len(clergy)):
                if langqdi==clergy[j]:
                    del clergy[j]
                    break
            for k in range(len(werewolf)):
                if langqdi==werewolf[k]:
                    del werewolf[k]
                    break
            for m in range(len(ordinary)):
                if langqdi==ordinary[m]:
                    del ordinary[m]
                    break
            pdict[langqnu]='已死亡'
            used1=1#狼枪击杀状态
            alldi.append(langqnu)#加入狼枪击杀的目标
            break
    except:
        print('无人被反杀')
        used1=1
    return pdict,clergy,werewolf,ordinary,used1,alldi
    
            
        
            

        
        


