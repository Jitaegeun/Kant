# 실행화면
# 상품
class Product:
    def __init__(self, item , price, stock):
        self.item = item
        self.price = price
        self.stock = stock

# 상품 등록 (객체)    
Products =  [            
    Product ("텀블러", 15000, 10),
    Product ("무선이어폰", 89000, 3),
    Product ("보조배터리", 32000, 5),
    Product ("마우스패드", 9000, 0),
    Product ("USB 허브", 18000, 4)
]

#장바구니
class Item: 
    def __init__(self):
        self.bucket = []
        
    def add_item(self, item):
        self.bucket.append(item)
        
    def remove_item(self, item):
        self.bucket.remove(item)

    def show_item(self):
        return self.bucket
    
# 상품목록 -> 선택한 상품 객체 전달 -> 선택한 상품 객체가 리스트에 추가되는것 구현


# 테스트 화면 --------------------------
while True: 
    print("-"*30)
    print("1. 상품목록 2. 담기 3. 빼기 4. 장바구니 5. 쿠폰 6. 결제 q. 종료")
    print("-"*30)

    menu = input("메뉴 중에 선택하시오.")
    
    # TODO : 입력값이 숫자인지 검사
 
    # TODO : 존재하는 번호인지 검사

    # 1. 상품목록 기능
    if menu == "1":
        print ("선택 : 1")
        #클래스 
        # for product in Products:
        #     print(f"{product.item}   {product.price}원 (재고{product.stock}개)")
        #     if product.stock == 0:
        #         print(f"{product.item} {product.price}원   (품절)")
    # 상품 번호 부여 enumerate
        for number, product in enumerate(Products, start=1):
            if product.stock == 0:
                print(f"{number}  {product.item} {product.price}원   (품절)")
            else:
                print(f"{number}  {product.item}  {product.price}원 (재고 {product.stock}개) ")            

    # 2. 담기 기능
    if menu == 2:
        def add_item(self, item):
            self.item = item
    
    if not (1 <= number <= len(Products)):
        print("존재하지 않는 상품입니다.")
        continue    
    # TODO : 상품 목록에서 선택한 객체 가져오기
    selected_product = Products[0]
    # TODO : 재고가 충분한지 검사
    cart_quantity = cart.bucket.count(selected_product)
    # TODO : 상품을 담으면 상품목록 재고조정
    if cart_quantity >= selected_product.stock:
        print("재고가 부족합니다.")
        continue
    # TODO : 상품을 빼면 상품목록 재고조정
    cart.add_item(selected_product)
    # 3. 빼기 기능
    if menu == 3:
        def remove_item(self,item):
            self.item = item
            
    break
