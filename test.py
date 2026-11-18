import requests
import time
import random
from threading import Thread

# 你的本地服务器地址
BASE_URL = "http://127.0.0.1:8000"


class VirtualPlayer:
    def __init__(self, username):
        self.username = username
        self.session = requests.Session()
        self.room_code = None

    def login_and_enter(self):
        """1. 模拟注册/登录 (这里假设你的系统允许直接通过某种方式拿 session)"""
        # 注意：Django 默认有 CSRF 保护，实际测试时你可能需要在 settings.py 里临时关闭某个接口的 CSRF，或者先 GET 拿 token
        # 这里为了演示逻辑，假设直接用 post 登录
        res = self.session.post(f"{BASE_URL}/accounts/login/", data={
            "username": self.username,
            "password": "password123"
        })
        # print(f"[{self.username}] 登录状态: {res.status_code}")

    def join_room(self, room_code):
        """2. 加入房间"""
        self.room_code = room_code
        self.session.post(f"{BASE_URL}/rooms/dining/", data={"room_code": room_code})
        # print(f"[{self.username}] 尝试加入房间 {room_code}")

    def get_phase(self):
        """3. 获取当前游戏阶段"""
        res = self.session.get(f"{BASE_URL}/process/{self.room_code}/status_phase/")
        if res.status_code == 200:
            return res.json().get("phase")
        return None

    def act_vote(self, target_username):
        """模拟投票"""
        self.session.post(f"{BASE_URL}/process/{self.room_code}/sheriffing/", json={"target": target_username})

    def act_kill(self, target_username):
        """模拟狼人刀人"""
        self.session.post(f"{BASE_URL}/process/{self.room_code}/werewolf/", json={"target": target_username})


def run_full_game_test():
    print("🚀 开始 12 人全局自动化测试...")

    # 1. 初始化 12 个虚拟玩家
    players = [VirtualPlayer(f"bot_{i}") for i in range(1, 13)]

    # 2. 全体登录
    for p in players:
        p.login_and_enter()
    time.sleep(1)

    # 3. 第一个人建房，其他人加入（假设房间号是 9999）
    room_code = "9999"
    players[0].session.post(f"{BASE_URL}/rooms/dining/", data={"action": "create"})  # 假设有这个建房的 POST
    for p in players:
        p.join_room(room_code)

    # 4. 房主点击开始游戏
    print("房主点击开始游戏...")
    players[0].session.post(f"{BASE_URL}/process/start/{room_code}/")

    # 5. 进入主循环，不断查询状态机，直到游戏结束
    last_phase = None
    while True:
        time.sleep(1)  # 每秒轮询一次
        current_phase = players[0].get_phase()

        if current_phase != last_phase:
            print(f"▶▶▶ 当前阶段切换至: {current_phase}")
            last_phase = current_phase

            # ============ 阶段触发逻辑 ============
            if current_phase == "sheriffjoin":
                # 让前 5 个人上警
                for p in players[:5]:
                    p.session.post(f"{BASE_URL}/process/{room_code}/sheriffjoining/")
                    print(f"[{p.username}] 上警")

            elif current_phase in ("sheriff1", "sheriff2"):
                # 让所有人随便投给警上的人
                for p in players:
                    target = random.choice(players[:5]).username
                    p.act_vote(target)
                    print(f"[{p.username}] 投票给 {target}")

            elif current_phase == "night":
                # 狼人随机刀人
                for p in players:
                    target = random.choice(players).username
                    p.act_kill(target)
                    print(f"[{p.username}] 出刀 {target}")

            elif current_phase == "vote1":
                # 所有人随机投票
                for p in players:
                    target = random.choice(players).username
                    p.act_vote(target)

            elif current_phase == "result":
                print("🏆 游戏结束！测试完美跑通！")
                break

            if current_phase is None:
                print("❌ 获取不到状态，测试可能崩溃了。")
                break


if __name__ == '__main__':
    run_full_game_test()