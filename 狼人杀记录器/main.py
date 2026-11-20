import pygame
import random
import sys
from collections import Counter
import function as f
import gprocess as g


class Game:
    MENU = 0
    SHOWING = 1

    def __init__(self):
        # 初始化 Pygame
        pygame.key.stop_text_input()

        # ===== 状态 =====
        self.game_state = self.MENU
        self.selected_board = None
        self.players = []
        self.newpainting = pygame.image.load('langrensha.jpg')
        pygame.display.set_icon(self.newpainting)
        self.offscreen = pygame.Surface((1200, 700))
        self.imscale = (310, 25, 100, 150)
        self.step = 1
        self.toupiao = {}
        self.toupiao2 = {}

        # ===== 主循环变量 =====
        self.pdict = {}
        self.saf = 1
        self.poi = 1
        self.shta = 0
        self.seer_target = 0
        self.seer_camp = None
        self.weta = 0
        self.nvta = 0
        self.dilist = []
        self.qiang = ''
        self.qita = 0
        self.qiangs = ''
        self.qitas = 0
        self.exe = 0
        self.exelist = []
        self.exelistp = []
        self.ytou = 0
        self.qiange = ''
        self.qitae = 0
        self.qianges = ''
        self.qitaes = 0
        self.sheriffed = 0

        self.recl = []
        self.rewe = []
        self.reor = []
        self.shtaed = 0
        self.yued = []
        self.werewolf = []
        self.day = 1
        self.operation = {'守': [], '预': [], '狼': [], '女': [],
                          '票': [], '猎': [], '狼枪': [], '警': []}
        self.sheriffrecord = {}
        self.sheriff = 0
        self.sherifflist = []
        self.sheriffpant = []
        self.replayers = []
        self.sherifflistp = []
        self.sheriffrecordp = {}

        # 原代码中在分支里临时出现、但跨状态被引用的变量，
        # 统一在这里初始化，避免 NameError（逻辑不变）
        self.top = []
        self.newnum = []
        self.newnum1 = []
        self.gameover = None

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_state += 1
                        break
                    if event.key == pygame.K_SPACE:
                        if self.step == 1:
                            pygame.image.save(f.screen, '身份情况.png')
                            self.step += 1
                        elif self.step == 2:
                            pygame.image.save(f.screen, '复盘情况.png')
                        else:
                            pygame.image.save(f.screen, '投票情况.png')

            if self.game_state == self.MENU:
                result = f.draw_menu()
                if result and result != '输入其他板子':
                    self.selected_board = result
                    identities = f.idtype[self.selected_board].copy()
                    random.shuffle(identities)
                    self.players = identities.copy()
                    self.game_state = self.SHOWING
                    tips = f.font_title.render('输入1到12数字显示身份', True, f.WHITE)
                    f.screen.blit(tips, (f.WIDTH // 2 - tips.get_width() // 2, 50))
                    pygame.display.flip()
                    f.draw_list(self.players)

                if result == '输入其他板子':
                    allrect = []
                    identities = []
                    y = 150
                    ids = 0
                    idlocations = {}
                    while ids < 12:
                        x = 125
                        update_rects = []
                        for i in (f.role_info.keys()):
                            tips = f.font_title.render('点击按钮添加身份', True, f.WHITE)
                            f.screen.blit(tips, (600 - tips.get_width() // 2, 50))
                            if x < 1000:
                                clicked, hover = f.draw_button(
                                    i, x, y, 150, 200,
                                    pygame.Color(f.role_info[i]['color']),
                                    text_color=f.BLACK)
                                idlocations[i] = pygame.Rect(x, 150, 150, 200)
                                allrect.append(idlocations[i])
                                image = pygame.image.load(f.role_info[i]['image'])
                                image = pygame.transform.scale(image, (150, 200))
                                self.offscreen.blit(image, idlocations[i])
                                x += 200
                            else:
                                clicked, hover = f.draw_button(
                                    i, x - 1000, y + 250, 150, 200,
                                    pygame.Color(f.role_info[i]['color']),
                                    text_color=f.BLACK)
                                idlocations[i] = pygame.Rect(x - 1000, 400, 150, 200)
                                allrect.append(idlocations[i])
                                image = pygame.image.load(f.role_info[i]['image'])
                                image = pygame.transform.scale(image, (150, 200))
                                self.offscreen.blit(image, idlocations[i])
                                x += 200

                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    sys.exit()
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    location = pygame.mouse.get_pos()
                                    for j, rect in idlocations.items():
                                        if rect.collidepoint(location):
                                            identities.append(j)
                                            ids += 1
                                            break

                            if ids == 12:
                                f.screen.fill(f.BLUE)
                                pygame.display.update()

                        if ids < 12:
                            f.screen.blit(self.offscreen, (0, 0))
                            pygame.display.update(allrect)

                    tips = f.font_title.render('输入1到12数字显示身份', True, f.WHITE)
                    f.screen.blit(tips, (600 - tips.get_width() // 2, 50))
                    pygame.display.flip()
                    random.shuffle(identities)
                    self.players = identities.copy()
                    self.game_state = self.SHOWING
                    f.draw_list(self.players)

            elif self.game_state == self.SHOWING:
                result = f.draw_result(self.players)
                if result == "menu":
                    self.game_state = self.MENU

            elif self.game_state == 2:
                self.pdict, self.werewolf = g.idtype(self.players, self.pdict)
                f.screen.fill(f.BLUE)
                start = f.font_title.render('初始化完毕', True, f.BLACK)
                f.screen.blit(start, (600 - start.get_width() // 2, 50))
                pygame.display.update()

            elif self.game_state == 3:
                if '守' in self.pdict.values():
                    f.screen.fill(f.BLUE)
                    if self.shta == 0:
                        picked = g.going('守', 150, 200, self.pdict)
                        if picked != 0 and self.shtaed != picked:
                            self.shta = picked
                            self.shtaed = self.shta
                            self.operation['守'].append(self.shta)
                    elif 1 <= self.shta <= 12:
                        result = f.font_title.render(f'你守护了{self.shta}号玩家', True, 'orange')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                    else:
                        result = f.font_title.render('本轮无操作', True, 'orange')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 1

            elif self.game_state == 4:
                if '预' in self.pdict.values():
                    f.screen.fill(f.BLUE)

                    if self.seer_target == 0:
                        picked = g.going('预', 150, 200, self.pdict)
                        if picked != 0 and picked not in self.yued:
                            self.seer_target = picked
                            self.seer_camp = g.yu(self.werewolf, picked, self.pdict)
                            self.operation['预'].append(self.seer_target)
                    elif 1 <= self.seer_target <= 12:
                        if self.seer_camp == 0:
                            text, color = '对方是好人', 'blue'
                        else:
                            text, color = '对方是狼人', 'red'
                        result = f.font_title.render(text, True, color)
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        if self.seer_target not in self.yued:
                            self.yued.append(self.seer_target)
                    else:
                        result = f.font_title.render('本轮无操作', True, 'grey')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))

                    pygame.display.flip()
                else:
                    self.game_state += 1

            elif self.game_state == 5:
                f.screen.fill(f.BLUE)

                if self.weta == 0:
                    picked = g.going('狼', 150, 200, self.pdict)
                    if picked != 0:
                        self.weta = picked
                        self.operation['狼'].append(self.weta)
                elif 1 <= self.weta <= 12:
                    result = f.font_title.render(f'本轮选择击杀{self.weta}号', True, 'red')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    result = f.font_title.render('本轮无操作', True, 'grey')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))

                pygame.display.flip()

            elif self.game_state == 6:
                if '女' in self.pdict.values():
                    f.screen.fill(f.BLUE)
                    if self.nvta == 0:
                        picked, self.saf, self.poi = g.going2(
                            '女', 150, 200, self.pdict, self.saf, self.poi, self.weta)
                        if picked != 0:
                            self.nvta = picked
                            self.operation['女'].append(self.nvta)
                    elif self.nvta == -2:
                        result = f.font_title.render(f'你救了{self.weta}号玩家', True, 'fuchsia')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                    elif 1 <= self.nvta <= 12:
                        result = f.font_title.render(f'你毒了{self.nvta}号玩家', True, 'green')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                    else:
                        result = f.font_title.render('本轮无操作', True, 'grey')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 1

            elif self.game_state == 7:
                f.screen.fill(f.BLUE)
                night = f.font_title.render('夜晚行动完毕', True, 'yellow')
                f.screen.blit(night, (600 - night.get_width() // 2, 50))

            elif self.game_state == 8:
                f.screen.fill(f.BLUE)
                if self.day == 1:
                    f.screen.fill(f.BLUE)
                    picked = g.going3(150, 200, self.pdict, '警')
                    if 1 <= picked <= 12 and picked not in self.sheriffpant and len(self.sheriffpant) < len(self.pdict):
                        self.sheriffpant.append(picked)
                else:
                    self.game_state += 5

            elif self.game_state == 9:
                f.screen.fill(f.BLUE)
                if len(self.sheriffpant) == 1:
                    self.sheriff = self.sheriffpant[0]
                    xianshi = f.font_title.render(f'{self.sheriff}号玩家自动当选警长', True, 'white')
                    f.screen.blit(xianshi, (600 - xianshi.get_width() // 2, 50))
                    if self.sheriff not in self.operation['警']:
                        self.operation['警'].append(self.sheriff)
                else:
                    for i in self.pdict.keys():
                        if i not in self.sheriffpant and i not in self.replayers:
                            self.replayers.append(i)
                    xianshi = f.font_title.render(f'{self.sheriffpant}号玩家竞选', True, 'white')
                    f.screen.blit(xianshi, (600 - xianshi.get_width() // 2, 50))
                    picked = g.going4(150, 200, self.sheriffpant, '警')
                    if (1 <= picked <= 12 or picked == -1) and len(self.sherifflist) < len(self.pdict) - len(self.sheriffpant):
                        self.sherifflist.append(picked)
                        picked = 0
                    elif len(self.sherifflist) >= len(self.pdict) - len(self.sheriffpant):
                        j = 0
                        for i in self.replayers:
                            self.sheriffrecord.setdefault(self.day, []).append((i, self.sherifflist[j]))
                            j += 1
                        self.game_state += 1

            elif self.game_state == 10:
                if len(self.sheriffpant) == 1:
                    self.game_state += 3
                else:
                    f.screen.fill(f.BLUE)
                    if self.sheriff == 0:
                        maximum = Counter(self.sherifflist)
                        player_votes = {k: v for k, v in maximum.items() if 1 <= k <= 12}

                        if len(player_votes) > 0:
                            maxall = max(player_votes.values())
                            self.top = [k for k, v in player_votes.items() if v == maxall]
                            if len(self.top) == 1:
                                self.sheriff = self.top[0]
                                self.operation['警'].append(self.sheriff)
                            else:
                                self.newnum1 = self.top
                                self.game_state += 1
                        else:
                            self.game_state += 2

                    elif 1 <= self.sheriff <= 12:
                        f.screen.fill(f.BLUE)
                        result = f.font_title.render(f'{self.sheriff}号玩家当选警长', True, 'black')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))

            elif self.game_state == 11:
                f.screen.fill(f.BLUE)
                if len(self.top) == 1:
                    self.game_state += 2
                else:
                    f.screen.fill(f.BLUE)
                    picked = g.going4(150, 200, self.newnum1, '警')
                    action = f.font_title.render('平票：选择支持的玩家', True, 'white')
                    f.screen.blit(action, (600 - action.get_width() // 2, 50))

                    newpdict1 = self.pdict.copy()
                    for i in self.newnum1:
                        if i in newpdict1:
                            del newpdict1[i]

                    if (1 <= picked <= 12 or picked == -1) and len(self.sherifflistp) < len(newpdict1):
                        self.sherifflistp.append(picked)
                        picked = 0
                    elif len(self.sherifflistp) >= len(newpdict1):
                        j = 0
                        for i in newpdict1.keys():
                            self.sheriffrecordp.setdefault(self.day, []).append((i, self.sherifflistp[j]))
                            j += 1
                        self.game_state += 1

            elif self.game_state == 12:
                f.screen.fill(f.BLUE)
                if self.sheriff == 0:
                    maximum = Counter(self.sherifflistp)
                    player_votes = {k: v for k, v in maximum.items() if 1 <= k <= 12}

                    if len(player_votes) > 0:
                        maxall = max(player_votes.values())
                        self.top = [k for k, v in player_votes.items() if v == maxall]
                        if len(self.top) == 1:
                            self.sheriff = self.top[0]
                            self.operation['警'].append(self.exe)
                        else:
                            self.sheriff = -1
                            self.operation['警'].append(self.exe)
                    else:
                        self.sheriff = -1
                elif 1 <= self.sheriff <= 12:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render(f'{self.sheriff}号玩家当选警长', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render('无人当选警长', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))

            elif self.game_state == 13:
                f.screen.fill(f.BLUE)
                if self.pdict.get(self.weta) and ((self.nvta == -2 and self.shta == self.weta) or (self.nvta != -2 and self.shta != self.weta)):
                    self.qiang = self.pdict.get(self.weta)
                    self.dilist.append(self.weta)
                    del self.pdict[self.weta]
                if self.pdict.get(self.nvta) and 1 <= self.nvta <= 12:
                    if self.nvta != self.weta:
                        self.dilist.append(self.nvta)
                        del self.pdict[self.nvta]
                if self.weta == self.nvta:
                    self.qiang = ''

                if '民' not in self.pdict.values() or ('守' not in self.pdict.values() and '预' not in self.pdict.values() and '女' not in self.pdict.values() and '猎' not in self.pdict.values()):
                    self.gameover = f.font_title.render('狼人胜利', True, 'red')
                    self.game_state += 12
                elif '狼' not in self.pdict.values() and '狼枪' not in self.pdict.values():
                    self.gameover = f.font_title.render('好人胜利', True, 'blue')
                    self.game_state += 12
                else:
                    if len(self.dilist) > 0:
                        f.screen.fill(f.BLUE)
                        die = f.font_title.render(f'今晚{self.dilist}号玩家死亡', True, 'grey')
                        f.screen.blit(die, (600 - die.get_width() // 2, 50))
                        pygame.display.flip()
                    else:
                        f.screen.fill(f.BLUE)
                        pingan = f.font_title.render('今晚是平安夜', True, 'yellow')
                        f.screen.blit(pingan, (600 - pingan.get_width() // 2, 50))
                        pygame.display.flip()

            elif self.game_state == 14:
                f.screen.fill(f.BLUE)
                if self.sheriff in self.dilist:
                    self.sheriffed = self.sheriff
                    picked = g.going3(100, 150, self.pdict, '')
                    jinghui = f.font_title.render('移交警徽', True, 'white')
                    f.screen.blit(jinghui, (600 - jinghui.get_width() // 2, 50))
                    if picked != 0:
                        self.sheriff = picked
                elif self.sheriffed != 0:
                    if self.sheriff != -1:
                        xianshi = f.font_title.render(f'{self.sheriffed}号把警徽移交给{self.sheriff}号', True, 'yellow')
                    else:
                        xianshi = f.font_title.render(f'{self.sheriffed}号放弃移交警徽', True, 'yellow')
                    if (self.sheriffed, self.sheriff) not in self.operation['警']:
                        self.operation['警'].append((self.sheriffed, self.sheriff))
                    f.screen.blit(xianshi, (600 - xianshi.get_width() // 2, 50))
                else:
                    self.game_state += 1

            elif self.game_state == 15:
                f.screen.fill(f.BLUE)
                if self.qiang == '猎' or self.qiang == '狼枪':
                    if self.qita == 0:
                        picked = g.going(self.qiang, 150, 200, self.pdict)
                        if picked != 0:
                            self.qita = picked
                            if self.qiang == '猎':
                                self.operation['猎'].append((self.day, self.qita))
                            else:
                                self.operation['狼枪'].append((self.day, self.qita))
                    elif 1 <= self.qita <= 12:
                        if self.qiang == '猎':
                            result = f.font_title.render(f'选择枪杀{self.qita}号玩家', True, f.role_info['猎']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        else:
                            result = f.font_title.render(f'选择反杀{self.qita}号玩家', True, f.role_info['狼枪']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        if self.pdict.get(self.qita):
                            self.qiangs = self.pdict[self.qita]
                            del self.pdict[self.qita]
                    else:
                        result = f.font_title.render('未发动技能', True, 'white')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 2

            elif self.game_state == 16:
                f.screen.fill(f.BLUE)
                if self.qiangs == '猎' or self.qiangs == '狼枪':
                    if self.qitas == 0:
                        picked = g.going(self.qiangs, 150, 200, self.pdict)
                        if picked != 0:
                            self.qitas = picked
                            if self.qiangs == '猎':
                                self.operation['猎'].append((self.day, self.qitas))
                            else:
                                self.operation['狼枪'].append((self.day, self.qitas))
                    elif 1 <= self.qitas <= 12:
                        if self.qiangs == '猎':
                            result = f.font_title.render(f'选择枪杀{self.qitas}号玩家', True, f.role_info['猎']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        else:
                            result = f.font_title.render(f'选择反杀{self.qitas}号玩家', True, f.role_info['狼枪']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        if self.pdict.get(self.qitas):
                            del self.pdict[self.qitas]
                    else:
                        result = f.font_title.render('未发动技能', True, 'white')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 1

            elif self.game_state == 17:
                f.screen.fill(f.BLUE)
                picked = g.going3(150, 200, self.pdict, '票')
                if (1 <= picked <= 12 or picked == -1) and len(self.exelist) < len(self.pdict):
                    self.exelist.append(picked)
                    picked = 0
                elif len(self.exelist) >= len(self.pdict):
                    j = 0
                    for i in self.pdict.keys():
                        self.toupiao.setdefault(self.day, []).append((i, self.exelist[j]))
                        j += 1
                    self.game_state += 1

            elif self.game_state == 18:
                f.screen.fill(f.BLUE)
                if self.exe == 0:
                    maximum = Counter(self.exelist)
                    player_votes = {k: v for k, v in maximum.items() if 1 <= k <= 12}

                    if len(player_votes) > 0:
                        maxall = max(player_votes.values())
                        self.top = [k for k, v in player_votes.items() if v == maxall]
                        if len(self.top) == 1:
                            self.exe = self.top[0]
                            self.operation['票'].append(self.exe)
                        else:
                            if self.exelist[self.sheriff - 1] not in self.top:
                                self.newnum = self.top
                                self.game_state += 1
                            else:
                                self.exe = self.exelist[self.sheriff - 1]
                                self.top = [self.exe]
                    else:
                        self.game_state += 2

                elif 1 <= self.exe <= 12:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render(f'处决{self.exe}号玩家', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))
                    if self.pdict.get(self.exe):
                        self.qiange = self.pdict[self.exe]
                        del self.pdict[self.exe]
                else:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render('无人被处决', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))

            elif self.game_state == 19:
                if len(self.top) == 1:
                    self.game_state += 2
                else:
                    f.screen.fill(f.BLUE)
                    picked = g.going4(150, 200, self.newnum, '票')

                    newpdict = self.pdict.copy()
                    for i in self.newnum:
                        if i in newpdict:
                            del newpdict[i]

                    if (1 <= picked <= 12 or picked == -1) and len(self.exelistp) < len(newpdict):
                        self.exelistp.append(picked)
                        picked = 0
                    elif len(self.exelistp) >= len(newpdict):
                        j = 0
                        for i in newpdict.keys():
                            self.toupiao2.setdefault(self.day, []).append((i, self.exelistp[j]))
                            j += 1
                        self.game_state += 1

            elif self.game_state == 20:
                f.screen.fill(f.BLUE)
                if self.exe == 0:
                    maximum = Counter(self.exelistp)
                    player_votes = {k: v for k, v in maximum.items() if 1 <= k <= 12}

                    if len(player_votes) > 0:
                        maxall = max(player_votes.values())
                        self.top = [k for k, v in player_votes.items() if v == maxall]
                        if len(self.top) == 1:
                            self.exe = self.top[0]
                            self.operation['票'].append(self.exe)
                        else:
                            if self.exelistp[self.sheriff - 1] not in self.top:
                                self.exe = -1
                                self.operation['票'].append(self.exe)
                            else:
                                self.exe = self.exelistp[self.sheriff - 1]
                                self.operation['票'].append(self.exe)
                    else:
                        self.exe = -1
                elif 1 <= self.exe <= 12:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render(f'处决{self.exe}号玩家', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))
                    if self.pdict.get(self.exe):
                        self.qiange = self.pdict[self.exe]
                        del self.pdict[self.exe]
                else:
                    f.screen.fill(f.BLUE)
                    result = f.font_title.render('无人被处决', True, 'black')
                    f.screen.blit(result, (600 - result.get_width() // 2, 50))

            elif self.game_state == 21:
                f.screen.fill(f.BLUE)
                if self.qiange == '猎' or self.qiange == '狼枪':
                    if self.qitae == 0:
                        picked = g.going(self.qiange, 150, 200, self.pdict)
                        if picked != 0:
                            self.qitae = picked
                            if self.qiange == '猎':
                                self.operation['猎'].append((self.day, self.qitae))
                            else:
                                self.operation['狼枪'].append((self.day, self.qitae))
                    elif 1 <= self.qitae <= 12:
                        if self.qiange == '猎':
                            result = f.font_title.render(f'选择枪杀{self.qitae}号玩家', True, f.role_info['猎']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        else:
                            result = f.font_title.render(f'选择反杀{self.qitae}号玩家', True, f.role_info['狼枪']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                        if self.pdict.get(self.qitae):
                            self.qianges = self.pdict[self.qitae]
                            del self.pdict[self.qitae]
                    else:
                        result = f.font_title.render('未发动技能', True, 'white')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 2

            elif self.game_state == 22:
                f.screen.fill(f.BLUE)
                if self.qianges == '猎' or self.qianges == '狼枪':
                    if self.qitaes == 0:
                        picked = g.going(self.qianges, 150, 200, self.pdict)
                        if picked != 0:
                            self.qitaes = picked
                            if self.qianges == '猎':
                                self.operation['猎'].append((self.day, self.qitaes))
                            else:
                                self.operation['狼枪'].append((self.day, self.qitaes))
                    elif 1 <= self.qitaes <= 12:
                        if self.qianges == '猎':
                            result = f.font_title.render(f'选择枪杀{self.qitaes}号玩家', True, f.role_info['猎']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                            self.operation['猎'].append((self.day, self.qitaes))
                        else:
                            result = f.font_title.render(f'选择反杀{self.qitaes}号玩家', True, f.role_info['狼枪']['color'])
                            f.screen.blit(result, (600 - result.get_width() // 2, 50))
                            self.operation['狼枪'].append((self.day, self.qitaes))
                        if self.pdict.get(self.qitaes):
                            del self.pdict[self.qitaes]
                    else:
                        result = f.font_title.render('未发动技能', True, 'white')
                        f.screen.blit(result, (600 - result.get_width() // 2, 50))
                else:
                    self.game_state += 1

            elif self.game_state == 23:
                f.screen.fill(f.BLUE)
                if self.sheriff == self.qitaes or self.sheriff == self.qitae or self.sheriff == self.exe:
                    self.sheriffed = self.sheriff
                    picked = g.going3(100, 150, self.pdict, '')
                    jinghui = f.font_title.render('移交警徽', True, 'white')
                    f.screen.blit(jinghui, (600 - jinghui.get_width() // 2, 50))
                    if picked != 0:
                        self.sheriff = picked
                elif self.sheriffed != 0:
                    if self.sheriff != -1:
                        xianshi = f.font_title.render(f'{self.sheriffed}号把警徽移交给{self.sheriff}号', True, 'yellow')
                    else:
                        xianshi = f.font_title.render(f'{self.sheriffed}号放弃移交警徽', True, 'yellow')
                    f.screen.blit(xianshi, (600 - xianshi.get_width() // 2, 50))
                    if (self.sheriffed, self.sheriff) not in self.operation['警']:
                        self.operation['警'].append((self.sheriffed, self.sheriff))
                else:
                    self.game_state += 1

            elif self.game_state == 24:
                f.screen.fill(f.BLUE)
                if '民' not in self.pdict.values() or ('守' not in self.pdict.values() and '预' not in self.pdict.values() and '女' not in self.pdict.values() and '猎' not in self.pdict.values()):
                    self.gameover = f.font_title.render('狼人胜利', True, 'red')
                    self.game_state += 2
                elif '狼' not in self.pdict.values() and '狼枪' not in self.pdict.values():
                    self.gameover = f.font_title.render('好人胜利', True, 'blue')
                    self.game_state += 2
                else:
                    self.game_state += 1

            elif self.game_state == 25:
                self.game_state = 3
                self.shta = 0
                self.seer_target = 0
                self.seer_camp = None
                self.weta = 0
                self.nvta = 0
                self.dilist = []
                self.qiang = ''
                self.exe = 0
                self.exelist = []
                self.exelistp = []
                self.ytou = 0
                self.qiange = ''
                self.qitae = 0
                self.qianges = ''
                self.qitaes = 0
                self.day += 1
                self.sheriffed = 0

            elif self.game_state == 26:
                f.screen.blit(self.gameover, (600 - self.gameover.get_width() // 2, 200))

            elif self.game_state == 27:
                f.screen.fill(f.BLUE)
                g.result(self.operation, self.day, 20)

            else:
                f.screen.fill(f.BLUE)
                g.result2(self.sheriffrecord, self.sheriffrecordp, self.day, 20, 1000, 'white')
                g.result2(self.toupiao, self.toupiao2, self.day, 20, 100, 'black')

            pygame.display.flip()
            f.clock.tick(60)

        pygame.quit()
        sys.exit()


if __name__ == '__main__':
    Game().run()