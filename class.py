# 클래스
class BreadMold:
    category = "크림빵"

    def make_bread(self):
        print("{}을 만들어 냅니다.".format(self.category))


bread = BreadMold()
bread_choco = BreadMold()

bread.price = 3000
bread_choco.category = "초코 크림빵"

print("{}의 가격은 {}입니다.".format(bread.category, bread.price))

bread.make_bread()
bread_choco.make_bread()
