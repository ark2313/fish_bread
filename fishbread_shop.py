from fishbread_model import BreadShop


shop = BreadShop()


#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들거예요
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수가 있어요

#붕어빵 메인화면
while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자,재고, 종료): ") #주문
    #mode = "종료"
    if mode == "종료":
        shop.calculate_sales()
        print("시스템을 종료")
        break
    elif mode == "주문":
        shop.order_bread()
    elif mode == "관리자":
        shop.admin_mode()
    elif mode == "재고":
        shop.bread_num()

