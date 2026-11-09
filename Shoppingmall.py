# 실행화면
# 부모 클래스
class Shoppingmall:
    def __init__(self, item , price, stock):
        self.item = item
        self.price = price
        self.stock = stock
    
shoppingmalls =  [           # 객체 
    Shoppingmall ("무선이어폰", 89000, 3),
    Shoppingmall ("텀블러", 15000, 10),
    Shoppingmall ("보조배터리", 32000, 5),
    Shoppingmall ("마우스패드", 9000, 0),
    Shoppingmall ("USB 허브", 18000, 4)
]

# 상속 클래스
class Item(Shoppingmall): 
    def __init__(self):
        self.bucket = []
    def add_item(self, item):
        self.bucket.append(item)
        
    def remove_item(self, item):
        self.bucket.remove(item)

    def show_item(self):
        return self.bucket


while True: 
    print("-"*30)
    print("1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
    print("-"*30)
    menu = input("메뉴 중에 선택하시오.")

    # 1. 상품목록 기능
    if menu == 1:
        print ("선택 : 1")
        #클래스 
        for Shoppingmall in Shoppingmalls:
            print(f"{self.item}   {self.price}원 (재고{self.stock}개)")

    # 2. 담기 기능
    if menu == 2:
        def add_item(self, item):
            pass
    break
