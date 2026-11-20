import pygame
import sys


# 初始化 Pygame
pygame.init()

WIDTH, HEIGHT = 1200, 700#全屏大小
pwidth,pheight = 200,300#单张身份牌大小
ppwidth,ppheight=100,150#所有身份牌大小
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('狼人杀身份发牌器')
clock = pygame.time.Clock()#时钟函数，确定帧数

# 颜色定义
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
BLUE = (100, 150, 255)
LIGHT_BLUE = (173, 216, 230)
GREEN = (100, 255, 100)
RED = (255, 80, 80)
ORANGE = (255, 165, 0)
PURPLE = (200, 100, 255)
BROWN = (210, 180, 140)
DARK_ORANGE = (255, 140, 0)

# 字体

font_title = pygame.font.SysFont('SimSun', 48)
font_large = pygame.font.SysFont('SimSun', 36)
font_medium = pygame.font.SysFont('SimSun', 28)
font_small = pygame.font.SysFont('SimSun', 20)

idtype = {
    '标准': ['预', '女', '猎', '白', '狼', '狼', '狼', '狼', '民', '民', '民', '民'],
    '狼枪守卫': ['预', '女', '猎', '守', '狼枪', '狼', '狼', '狼', '民', '民', '民', '民'],
    '机械狼通灵师': ['镜', '女', '猎', '守', '觉隐', '狼', '狼', '狼', '民', '民', '民', '民']
}

# 身份信息
role_info = {
    '预': {'name': '预言家', 'color': 'purple','image':'yu.jpg'},
    '女': {'name': '女巫', 'color': 'fuchsia','image':'nv.jpg'},
    '猎': {'name': '猎人', 'color': (50,200,100),'image':'lie.jpg'},
    '白': {'name': '白痴', 'color': 'pink','image':'bai.jpg'},
    '狼': {'name': '狼人', 'color': RED,'image':'we.jpg'},
    '狼枪': {'name': '狼枪', 'color': (200, 50, 50),'image':'wek.jpg'},
    '守': {'name': '守卫', 'color': 'orange','image':'shou.jpg'},
    '镜': {'name': '通灵师', 'color': 'lightblue','image':'jing.jpg'},
    '觉隐': {'name': '机械狼', 'color': 'gold','image':'jixielang.jpg'},
    '民':{'name':'平民','color':'olive','image':'min.jpg'}
}

# 游戏状态


def draw_button(text, x, y, width, height, color, text_color=BLACK):
    """绘制一个带文字的按钮，返回是否被点击"""
    mouse_x, mouse_y = pygame.mouse.get_pos()
    clicked = False#先初始赋值未被点击

    # 检测鼠标悬停
    rect = pygame.Rect(x, y, width, height)#确定被点击的矩形大小和位置
    is_hover = rect.collidepoint(mouse_x, mouse_y)#判断鼠标是否在上述矩形区内

    # 按钮颜色变化
    if is_hover:
        btn_color = (min(color[0] + 30, 255), min(color[1] + 30, 255), min(color[2] + 30, 255))#如果在区域内会有颜色变化
    else:
        btn_color = color

    # 绘制按钮
    pygame.draw.rect(screen, btn_color, rect, border_radius=10)#按照上述点击区域绘制按钮
    pygame.draw.rect(screen, BLACK, rect, width=2, border_radius=10)#增加边框

    # 绘制文字
    text_surface = font_medium.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surface, text_rect)

    # 检测点击
    if is_hover and pygame.mouse.get_pressed()[0]:
        clicked = True
        screen.fill(BLUE)
        pygame.display.update()

    return clicked, is_hover


def draw_single(identity, number,WIDTH,HEIGHT,pwidth,pheight):  # ===== 绘制身份牌 =====
    screen.fill(BLUE)
    info = role_info.get(identity, {'name': identity, 'color': GRAY})
    color = info['color']
    num = font_large.render(str(number), True, color)

    screen.blit(num, (WIDTH//2-num.get_width()//2, 105))



        # 显示身份
    picture=pygame.image.load(role_info[identity]['image'])
    uspi=pygame.transform.scale(picture,(pwidth,pheight))
    screen.blit(uspi, (WIDTH//2-pwidth//2, HEIGHT//2-pheight//2))
    pygame.display.update()



def draw_card(identity, number, ppwidth,ppheight,i):
    """绘制一张身份牌"""
    info = role_info.get(identity, {'name': identity, 'color': GRAY})
    color = info['color']
    picture = pygame.image.load(role_info[identity]['image'])
    uspi=pygame.transform.scale(picture,(ppwidth,ppheight))
    num_text = font_large.render(str(number), True, color)
    if i<=5:
        screen.blit(uspi,(150+i*160,150))
    else:
        screen.blit(uspi,(150+(i-6)*160,400))
    if number < 7:
        # 显示号码
        screen.blit(num_text, (196+i*160, 100))
    elif 7<=number<10:
        screen.blit(num_text, (194+ (i-6) * 160, 350))
    else:
        screen.blit(num_text, (186+(i-6)*160, 350))
# ===== 菜单界面 =====
def draw_menu():
    """绘制菜单界面"""
    # 背景
    screen.fill(BLUE)

    # 标题
    title = font_title.render("狼人杀身份发牌器", True, WHITE)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2 , 50))

    # 副标题
    subtitle = font_medium.render("请选择板子类型：", True, WHITE)
    screen.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, 140))

    # 三个板子按钮
    boards = [
        ('标准', 155, 220, 200, 60, (100, 200, 255)),
        ('狼枪守卫', 385, 220, 200, 60, (255, 200, 100)),
        ('机械狼通灵师', 615, 220, 200, 60, (200, 150, 255)),
        ('输入其他板子', 845, 220, 200, 60, (255, 165, 0))
    ]

    for name, x, y, w, h, color in boards:
        clicked, hover = draw_button(name, x, y, w, h, color, BLACK)
        if clicked:
            return name

    return None


def draw_list(players):
    list = []

    for i in range(len(players)):#
        list.append(players[i])
    times = 0
    listed = []
    while times <= 12:
        num = ''
        out = 0
        stop = 0
        if times < 12:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.unicode.isdigit():
                            num += event.unicode

                        if event.key == pygame.K_RETURN:
                            out = 1
                        if event.key == pygame.K_ESCAPE:
                            sys.exit()

                if out:
                    break
            if num != '':
                if 1 <= int(num) <= 12:
                    draw_single(list[int(num) - 1], int(num),WIDTH,HEIGHT,pwidth,pheight)
                    pygame.display.update()
                    if int(num) not in listed:
                        listed.append(int(num))
                        times += 1

        else:
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            stop = 1
                if stop:
                    break
            times += 1


# ===== 发牌结果界面 =====
def draw_result(players):
    """绘制发牌结果界面"""
    # 背景
    screen.fill(BLUE)

    # 显示所有身份牌
    for i, identity in enumerate(players):
        draw_card(identity, i+1, ppwidth, ppheight,i)

    # 返回按钮

    clicked, hover = draw_button("返回菜单", 510, 625, 180, 50, (200, 200, 200), BLACK)
    if clicked:
        return "menu"

    return None
