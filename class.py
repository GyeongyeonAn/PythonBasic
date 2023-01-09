# 클래스
class BreadMold:
    category = "빵"

    # 생성자
    def __init__(self, category, price):
        self.category = category
        self.price = price
        print("빵을 만들었습니다.")

    # 출력 스트링 지정
    def __str__(self):
        return "{}의 가격은 {}원 입니다.".format(self.category, self.price)

    # 소멸자
    def __del__(self):
        print("{}이 없어졌습니다.".format(self.category))

    # 클래스 함수
    def make_bread(self):
        print("{}을 만들어 냅니다.".format(self.category))


# 생성자 사용
bread = BreadMold("크림빵", 3000)
bread_choco = BreadMold("초코크림빵", 2500)
bread1 = BreadMold("붕어빵", 3000)

print(bread)
print(bread_choco)
print(bread1)

bread.make_bread()
bread_choco.make_bread()
bread1.make_bread()

# dir() namespace 안에 있는 모든 속성을 리스트로 반환
print(dir(bread1))


# 상속
# super : 부모
# sub : 자식
class ParentRestaurant:
    price = 15000

    def __init__(self, name, menu, recipe):
        self.name = name
        self.menu = menu
        self.recipe = recipe

    def __str__(self):
        return "가게 이름: {}, 메뉴 {}, 조리법 : {}".format(self.name, self.menu, self.recipe)

    def __del__(self):
        pass


class ChildRestaurant(ParentRestaurant):
    price = 20000

    def __init__(self, name, menu, recipe, marketing):
        ParentRestaurant.__init__(self, name, menu, recipe)
        self.marketing = marketing

    def __str__(self):
        return super().__str__() + ", 마케팅 방법: {}".format(self.marketing)


restaurant_info = ChildRestaurant("자식의 가게", "붕어빵", "붕어빵을 굽는다.", "온라인")
print(restaurant_info)

# 부모 자식 관계 확인
print(issubclass(ChildRestaurant, ParentRestaurant))
print(issubclass(ParentRestaurant, ChildRestaurant))
