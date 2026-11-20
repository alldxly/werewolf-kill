import 狼人杀模拟器 as c
import 狼人杀发牌器 as d
used=0
used1=0
du1=0
du2=0
trdu1=0
trdu2=0
res=1
rep=1
shounu=0
if d.type=='狼枪守卫':
    for i in c.pdict.keys():
        if c.pdict[i] =='预':
            yun=i
    while True:
        if '守' in c.pdict.values():
            shounu=c.shou(c.alldi,shounu)
        
        if '预' in c.pdict.values():
            c.yu(c.alldi,yun)
        c.pdict,c.clergy,c.werewolf,c.ordinary,c.wedi,c.wenum,c.alldi,twed=c.wes(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '女' in c.pdict.values() or c.wedi=='女':
            c.pdict,c.clergy,c.werewolf,c.ordinary,du1,res,rep,c.alldi,du2=c.nvs(c.pdict,c.clergy,c.werewolf,c.ordinary,c.wedi,c.recl,c.rewe,c.reor,c.wenum,res,rep,c.alldi,shounu,twed)
            if du1==1:
                trdu1=1
            if du2==1:
                trdu2=1
        else:
            if c.wenum==shounu and  ('守' in c.pdict.values() or twed=='守'):
                if c.wedi in c.recl:
                    c.clergy.append(c.wedi)
                if c.wedi in c.rewe:
                    c.werewolf.append(c.wedi)
                if c.wedi in c.reor:
                    c.ordinary.append(c.wedi)
                c.pdict[c.wenum]=c.wedi
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        if '狼枪' not in c.pdict.values() and used1==0 and du2==0 and trdu2==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used1,c.alldi=c.langq(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '狼枪' not in c.pdict.values() and used1==0 and du2==0 and trdu2==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used1,c.alldi=c.langq(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        exe=c.tou(c.pdict,c.alldi)
        c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi=c.pi(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi,exe)
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '狼枪' not in c.pdict.values() and used1==0 and du2==0 and trdu2==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used1,c.alldi=c.langq(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '狼枪' not in c.pdict.values() and used1==0 and du2==0 and trdu2==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used1,c.alldi=c.langq(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)   
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        print(c.pdict)
if d.type=='标准':
    for i in c.pdict.keys():
        if c.pdict[i] =='预':
            yun=i
    while True:

        if '预' in c.pdict.values():
            c.yu(c.alldi,yun)
        c.pdict,c.clergy,c.werewolf,c.ordinary,c.wedi,c.wenum,c.alldi=c.we(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if '女' in c.pdict.values() or c.wedi=='女':
            c.pdict,c.clergy,c.werewolf,c.ordinary,du1,res,rep,c.alldi,du2=c.nv(c.pdict,c.clergy,c.werewolf,c.ordinary,c.wedi,c.recl,c.rewe,c.reor,c.wenum,res,rep,c.alldi,shounu)
            if du1==1:
                trdu1=1
            if du2==1:
                trdu2=1

        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        exe=c.tou(c.pdict,c.alldi)
        c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi=c.pi(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi,exe)
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        if '猎' not in c.pdict.values() and used==0 and du1==0 and trdu1==0:
            c.pdict,c.clergy,c.werewolf,c.ordinary,used,c.alldi=c.lie(c.pdict,c.clergy,c.werewolf,c.ordinary,c.alldi)
        if len(c.clergy)>0 and len(c.ordinary)>0 and len(c.werewolf)==0:
            print('好人胜利')
            break
        if len(c.clergy)<1 or len(c.ordinary)<1:
            print('狼人胜利')
            break
        print(c.pdict)
    

