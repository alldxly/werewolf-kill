import function as f
import pygame

imscale=(310,25,100,150)
clergy=[]
werewolf=[]
ordinary=[]


def num(x,y,pdict):
    for i in pdict.keys():
        if x<960:
            f.draw_button(str(i),x,y,100,50,f.WHITE)
            x+=160
        else:
            f.draw_button(str(i),x-960,y+200,100,50,f.WHITE)
            x+=160
def yu(werewolf,yunum,pdict):
    if 1<=yunum<=12:
        if pdict[yunum] in werewolf:
            c=1
        else:
            c=0
        return c
    else:
        return 2
def idtype(players,pdict):
    for i in range(len(players)):
        pdict[i + 1] = players[i]
        if '狼' in players[i]:
            werewolf.append(players[i])

    return pdict,werewolf
def going(id, x, y, pdict):
    """只返回本帧被点击的玩家编号；没点中返回 0。不保存状态。"""
    clicked_target = 0
    actdict = {'预':'选择查验的玩家','女':'救人或选择毒杀的玩家',
               '猎':'选择枪杀的玩家','守':'选择守护的玩家',
               '狼':'选择击杀的玩家','狼枪':'选择反杀的玩家'}
    action = f.font_title.render(actdict[id], True, f.role_info[id]['color'])
    f.screen.blit(action, (600 - action.get_width() // 2, 50))
    image = pygame.image.load(f.role_info[id]['image'])
    image = pygame.transform.scale(image, (100, 150))
    f.screen.blit(image, imscale)

    start_x = x
    for i in pdict.keys():
        if start_x < 960:
            clicked, a = f.draw_button(str(i), start_x, y, 100, 50, f.WHITE)
            start_x += 160
        else:
            clicked, a= f.draw_button(str(i), start_x - 960, y + 200, 100, 50, f.WHITE)
            start_x += 160

        flip,a=f.draw_button('跳过',550, y + 400, 100, 50, f.WHITE)

        if clicked:
            clicked_target = i
        if flip:
            clicked_target = -1
    return clicked_target
def going2(id, x, y, pdict,saf,poi,weta):
    clicked_target = 0
    actdict = {'预':'选择查验的玩家','女':'救人或选择毒杀的玩家',
               '猎':'选择枪杀的玩家','守':'选择守护的玩家',
               '狼':'选择击杀的玩家','狼枪':'选择反杀的玩家'}
    action = f.font_title.render(actdict[id], True, 'fuchsia')
    f.screen.blit(action, (700 - action.get_width() // 2, 50))
    image = pygame.image.load(f.role_info[id]['image'])
    image = pygame.transform.scale(image, (100, 150))
    f.screen.blit(image, imscale)

    start_x = x
    for i in pdict.keys():
        if start_x < 960:
            clicked, a = f.draw_button(str(i), start_x, y, 100, 50, f.WHITE)
            start_x += 160
        else:
            clicked, a= f.draw_button(str(i), start_x - 960, y + 200, 100, 50, f.WHITE)
            start_x += 160

        flip,a=f.draw_button('跳过',630, y + 400, 100, 50, f.WHITE)
        if saf==1:
            killed=f.font_title.render(f'本轮被杀的是{weta}号',True, 'fuchsia')
            f.screen.blit(killed, (700 - action.get_width() // 2, 120))
            safe,b=f.draw_button('救',470, y + 400, 100, 50, (255,0,255))
            if safe and pdict[weta]!=('女'):
                saf-=1
                clicked_target = -2



        if poi and clicked:
            clicked_target = i
            poi-=1
        if flip:
            clicked_target = -1
    return clicked_target,saf,poi

_mouse_was_down = False

def going3(x, y, pdict,type):
    """只返回本帧被点击的玩家编号；没点中返回 0。不保存状态。"""
    global _mouse_was_down

    clicked_target = 0
    if type=='警':


        action = f.font_title.render('竞选警长', True, 'white')
        f.screen.blit(action, (600 - action.get_width() // 2, 50))
    elif type=='票':
        action = f.font_title.render('投票：选择处决的玩家', True, 'white')
        f.screen.blit(action, (600 - action.get_width() // 2, 50))

    # ---- 边沿检测：只有"这一帧按下 且 上一帧没按下"才算一次有效点击 ----
    now_down = pygame.mouse.get_pressed()[0]
    fresh_click = now_down and not _mouse_was_down
    _mouse_was_down = now_down
    # ----------------------------------------------------------------

    start_x = x
    for i in pdict.keys():
        # 先把按钮画出来（绘制不受边沿检测影响，保证画面正常）
        if start_x<=960:
            clicked, a = f.draw_button(str(i), start_x, y, 100, 50, f.WHITE)
            if fresh_click and clicked:
                clicked_target = i
            start_x += 160
        else:
            clicked, a = f.draw_button(str(i), start_x-960, y+200, 100, 50, f.WHITE)
            if fresh_click and clicked:
                clicked_target = i
            start_x += 160


    # “跳过”只画一次，且同样只在边沿帧生效
    flip, a = f.draw_button('跳过', 550, y + 400, 100, 50, f.WHITE)
    if fresh_click and flip:
        clicked_target = -1

    return clicked_target
def going4(x, y, list,type):
    """只返回本帧被点击的玩家编号；没点中返回 0。不保存状态。"""
    global _mouse_was_down

    clicked_target = 0
    if type=='票':



        action = f.font_title.render('平票：选择处决的玩家', True, 'white')
        f.screen.blit(action, (600 - action.get_width() // 2, 50))

    # ---- 边沿检测：只有"这一帧按下 且 上一帧没按下"才算一次有效点击 ----
    now_down = pygame.mouse.get_pressed()[0]
    fresh_click = now_down and not _mouse_was_down
    _mouse_was_down = now_down
    # ----------------------------------------------------------------

    start_x = x
    for i in list:
        # 先把按钮画出来（绘制不受边沿检测影响，保证画面正常）
        if start_x <= 960:
            clicked, a = f.draw_button(str(i), start_x, y, 100, 50, f.WHITE)
            if fresh_click and clicked:
                clicked_target = i
            start_x += 160
        else:
            clicked, a = f.draw_button(str(i), start_x - 960, y + 200, 100, 50, f.WHITE)
            if fresh_click and clicked:
                clicked_target = i
            start_x += 160

    # “跳过”只画一次，且同样只在边沿帧生效
    flip, a = f.draw_button('跳过', 550, y + 400, 100, 50, f.WHITE)
    if fresh_click and flip:
        clicked_target = -1

    return clicked_target
def result(operation,day,y):
    x=100
    for i in range(day):
        tian=f.font_medium.render(f'第{i+1}天',True,'black')
        f.screen.blit(tian, (600 - tian.get_width() // 2, y+100*i))
        if len(operation['守'])>i:
            if 1<=operation['守'][i]<=12:
                shou=f.font_small.render(f'守护了{operation['守'][i]}号',True,f.role_info['守']['color'])
                f.screen.blit(shou, (x, y+50+100*i))
            else :
                shou = f.font_small.render(f'未使用技能', True, f.role_info['守']['color'])
                f.screen.blit(shou, (x, y + 50+100*i))
            image=pygame.image.load(f.role_info['守']['image'])
            image=pygame.transform.scale(image,(50,75))
            f.screen.blit(image, (x-60, y+50+100*i))
        if len(operation['预'])>i:
            if 1<=operation['预'][i]<=12:
                yu=f.font_small.render(f'查验了{operation['预'][i]}号',True,f.role_info['预']['color'])
                f.screen.blit(yu, (x+200, y+50+100*i))
            else :
                yu = f.font_small.render('未使用技能', True, f.role_info['预']['color'])
                f.screen.blit(yu, (x + 200, y + 50 + 100 * i))
            image = pygame.image.load(f.role_info['预']['image'])
            image = pygame.transform.scale(image, (50, 75))
            f.screen.blit(image, (x - 60+200, y + 50 + 100 * i))
        if len(operation['狼'])>i:
            if 1<=operation['狼'][i]<=12:
                we=f.font_small.render(f'击杀{operation['狼'][i]}号',True,f.role_info['狼']['color'])
                f.screen.blit(we, (x+400, y + 50 + 100 * i))
            else :
                we = f.font_small.render('未使用技能', True, f.role_info['狼']['color'])
                f.screen.blit(we, (x + 400, y + 50 + 100 * i))
            image = pygame.image.load(f.role_info['狼']['image'])
            image = pygame.transform.scale(image, (50, 75))
            f.screen.blit(image, (x - 60+400, y + 50 + 100 * i))
        if len(operation['女'])>i:
            if 1<=operation['女'][i]<=12:
                nv=f.font_small.render(f'毒杀{operation['女'][i]}号',True,f.role_info['女']['color'])
                f.screen.blit(nv, (x + 600, y + 50 + 100 * i))
            elif operation['女'][i]==-2:
                nv = f.font_small.render(f'救活{operation['狼'][i]}号', True, f.role_info['女']['color'])
                f.screen.blit(nv, (x + 600, y + 50 + 100 * i))
            else:
                nv = f.font_small.render('未使用技能', True, f.role_info['女']['color'])
                f.screen.blit(nv, (x + 600, y + 50 + 100* i))
            image = pygame.image.load(f.role_info['女']['image'])
            image = pygame.transform.scale(image, (50, 75))
            f.screen.blit(image, (x - 60+600, y + 50 + 100 * i))
        if len(operation['警']) > i and i==0:
            if 1 <= operation['警'][i] <= 12 :

                piao = f.font_small.render(f'{operation['警'][i]}号当选警长', True, 'white')
                f.screen.blit(piao, (x + 800, y + 35 + 100 * i))


            else:
                piao = f.font_small.render('没有玩家当选警长', True, 'white')
                f.screen.blit(piao, (x + 800, y + 35 + 100 * i))
        elif len(operation['警']) > i and i!=0:
            if operation['警'][i][1] != -1:
                piao = f.font_small.render(f'{operation['警'][i][0]}号把警徽移交给{operation['警'][i][1]}号', True,
                                           'white')
                f.screen.blit(piao, (x + 800, y + 35 + 100 * i))
            else:
                piao = f.font_small.render(f'{operation['警'][i][0]}号放弃移交警徽', True, 'white')
                f.screen.blit(piao, (x + 800, y + 35 + 100 * i))
        if len(operation['票'])>i:
            if 1<=operation['票'][i]<=12:
                piao=f.font_small.render(f'处决{operation['票'][i]}号',True,'white')
                f.screen.blit(piao, (x + 800, y + 65 + 100 * i))
            else:
                piao = f.font_small.render('未处决玩家', True,'white')
                f.screen.blit(piao, (x + 800, y + 65 + 100 * i))
    if len(operation['猎'])!=0:
        lie=f.font_small.render(f'第{operation['猎'][0][0]}天枪杀{operation['猎'][0][1]}号',True,f.role_info['猎']['color'])
        f.screen.blit(lie, (300, y + 50 + 100*day))
        image = pygame.image.load(f.role_info['猎']['image'])
        image = pygame.transform.scale(image, (50, 75))
        f.screen.blit(image, (240, y + 50 + 100 * day))
    if len(operation['狼枪'])!=0:
        langq=f.font_small.render(f'第{operation['狼枪'][0][0]}天反杀{operation['狼枪'][0][1]}号',True,f.role_info['狼枪']['color'])
        f.screen.blit(langq, (700, y + 50 + 100 * day))
        image = pygame.image.load(f.role_info['狼枪']['image'])
        image = pygame.transform.scale(image, (50, 75))
        f.screen.blit(image, (640, y + 50 + 100 * day))
def result2(toupiao,toupiao2,day,y,x,color):


    for i in range(day):
        a = 0
        b = 0
        tian = f.font_medium.render(f'第{i + 1}天', True, 'black')
        f.screen.blit(tian, (x - tian.get_width() // 2+200*i, y ))
        if i+1 in toupiao:
            for j in toupiao[i+1]:
                if j[1]!=-1:
                    xianshi=f.font_small.render(f'{j[0]}号玩家投票给{j[1]}号', True, color)
                    f.screen.blit(xianshi, (x - tian.get_width() // 2 + 200*i, y+30+20*a ))

                else:
                    xianshi = f.font_small.render(f'{j[0]}号玩家弃票', True, color)
                    f.screen.blit(xianshi, (x - tian.get_width() // 2 + 200*i, y+30+20*a))
                a+=1

        if i+1 in toupiao2:
            for k in toupiao2[i+1]:
                if k[1] != -1:
                    xianshi2 = f.font_small.render(f'{k[0]}号玩家投票给{k[1]}号',True, color)
                    f.screen.blit(xianshi2, (x - tian.get_width() // 2 + 200 * i, y+250+20*b))
                else:
                    xianshi2=f.font_small.render(f'{k[0]}号玩家弃票', True, color)
                    f.screen.blit(xianshi2, (x - tian.get_width() // 2 + 200 * i, y+250+20*b))
                b+=1
        if color=='white':
            break











