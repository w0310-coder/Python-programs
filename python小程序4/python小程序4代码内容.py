# 以此代码演示了装饰器、闭包、多线程编程和随机数生成的综合应用
import random
import time
import threading
from typing import Callable, Any
def timer_decorator(func: Callable) -> Callable:
    """计时装饰器"""
    def wrapper(*args, **kwargs) -> Any:
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"\n游戏耗时: {end_time - start_time:.2f} 秒")
        return result
    return wrapper
def create_score_counter() -> Callable[[int], None]:
    """创建分数计数器闭包"""
    total_score = 0
    def update_score(points: int) -> None:
        nonlocal total_score
        total_score += points
        print(f"当前总分数: {total_score} 分")
    return update_score
def countdown_timer(seconds: int, game_active: list) -> None:
    """倒计时线程函数"""
    for i in range(seconds, 0, -1):
        if not game_active[0]:
            return
        print(f"\r剩余时间: {i} 秒", end="")
        time.sleep(1)
    if game_active[0]:
        print("\n时间到！游戏结束")
        game_active[0] = False
@timer_decorator
def play_game(update_score: Callable[[int], None]) -> None:
    """玩一局猜数字游戏"""
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    game_active = [True]
    print("\n===== 猜数字游戏 =====")
    print(f"我想了一个1-100之间的数字，你有{max_attempts}次机会猜")
    print("同时你有60秒的时间限制")
    # 启动倒计时线程
    timer_thread = threading.Thread(target=countdown_timer, args=(60, game_active))
    timer_thread.start()
    while attempts < max_attempts and game_active[0]:
        try:
            guess = input(f"\n第{attempts+1}次猜测，请输入你的数字: ")
            if not game_active[0]:
                break
            guess_num = int(guess)
            attempts += 1
            if guess_num < 1 or guess_num > 100:
                print("数字必须在1-100之间！")
                attempts -= 1
                continue
            if guess_num == secret_number:
                print(f"恭喜你猜对了！数字就是 {secret_number}")
                # 根据剩余次数计算分数
                points = (max_attempts - attempts + 1) * 10
                print(f"你用了 {attempts} 次猜对，获得 {points} 分")
                update_score(points)
                game_active[0] = False
                break
            elif guess_num < secret_number:
                print("太小了！再大一点")
            else:
                print("太大了！再小一点")
        except ValueError:
            print("请输入有效的数字！")
            attempts -= 1
    if game_active[0] and attempts >= max_attempts:
        print(f"\n很遗憾，你用完了所有机会！正确答案是 {secret_number}")
        game_active[0] = False
    # 等待倒计时线程结束
    timer_thread.join()
def main() -> None:
    """游戏主函数"""
    print("欢迎来到猜数字游戏升级版！")
    update_score = create_score_counter()
    while True:
        play_game(update_score)
        play_again = input("\n还要再玩一局吗？(y/n): ").strip().lower()
        if play_again != 'y':
            print("感谢游玩！再见！")
            break
if __name__ == "__main__":
    main()