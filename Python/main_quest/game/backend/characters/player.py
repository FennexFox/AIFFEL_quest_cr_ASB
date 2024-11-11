# Player 클래스
# Character를 상속 받기
# 레벨 1, 체력 100, 공격력 25, 방어력 5로 초기화하기
# Player 클래스는 경험치 속성을 추가로 가짐
# 인수로 받은 정수 만큼 경험치를 획득하는 gain_experience 메서드 만들기
# 현재 경험치가 50이상이면 레벨을 1, 공격력을 10, 방어력을 5씩 올리는 level_up 메서드 만들기

from .character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.level = 1
        self.health = 100
        self.attack_power = 25
        self.defense_power = 5
        self.exp = 0

    def __str__(self):
        super().__str__()
        print(self.exp)

    def gain_experience(self, exp):
        self.exp += exp
        print(f'{self.name}이 {exp} exp를 얻었습니다.')
        while self.exp >= 50:
            self.level_up()
            self.exp -= 50

    def level_up(self):
            self.level += 1
            self.attack_power += 10
            self.defense_power += 5
            print(f'{self.name}의 레벨이 {self.level - 1}에서 {self.level}로 상승했습니다.')
