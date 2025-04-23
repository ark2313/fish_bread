#주문, 관리자, 종료 이 3가지 선택을 통해서 각각 기능이 작동되도록 만들거예요
#input()을 통해서 3가지 중 한가지를 입력받아서 작동시킬 수가 있어요

stock = {   #key값을 이용해서 value  딕셔너리를 써야하는 상황은 어떤 스토리 기반으로 데이터가 구성되었을때 
    "팥붕어빵": 10,
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5
}

sales = {
    "팥붕어빵": 0,
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0
}

#붕어빵 주문 기능
def order_bread():
    while True:    
        bread_type = input("주문할 붕어빵을 선택하세요(팥붕어빵, 슈크림붕어빵, 초코붕어빵) 만약 뒤로가길 원하시면 뒤로가기를 입력해주세요: ")
        if bread_type == "뒤로가기":
            break
        if bread_type in stock:
            bread_count = int(input("주문할 개수를 입력하세요: ")) #8
            if  stock[bread_type] >= bread_count:
                stock[bread_type] -= bread_count
                sales[bread_type] += bread_count
                print(f"{bread_type} {bread_count}개가 판매되었습니다.")
            else:
                print(f"재고가 부족합니다. 현재 {stock[bread_type]}개만 주문 가능합니다.")
        else:
            print("정신을 똑바로 차리시고 주문을 다시해주세요👺")


#붕어빵 admin 기능
def admin_mode():
    #추가할 붕어빵 맛을 받는다 근데 종료나 뒤로가기 입려되면 거기서 종료
    #붕어빵 맛을 담는 변수 = bread_type
    #bread_count = 붕어빵 갯수
    #stock에 붕어빵 맛을 찾고 거기에 추가할 개수를 더해서 반영
   while True:
    bread_type = input("붕어빵 종류입력(팥,슈크림,초코) 뒤로가길 원한다면 뒤로가기")
    if bread_type == "뒤로가기":
        break
    if bread_type in stock:
            bread_count = int(input("창고에 채워넣을 개수를 입력하세요: ")) #8
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고가{bread_count}개 추가되어, 현재 {stock[bread_type]}개 입니다")
    else:
            print("정신을 똑바로 차리시고 주문을 다시해주세요👺")
    print()

#붕어빵 재고 확인
def bread_num():
    while True:
     bread_type = input("붕어빵 종류입력(팥붕어빵,슈크림붕어빵,초코붕어빵) 뒤로가길 원한다면 뒤로가기")
     if bread_type == "뒤로가기":
        break

    if bread_type in stock:
            bread_count = int(input("재고를 확인할 붕어빵 종류를 입력하세요 (팥,슈크림,초코): ")) #8
            stock[bread_type] += bread_count
            print(f"{bread_type}의 재고는 현재 {stock[bread_type]}개 입니다")
    else:
            print("정신을 똑바로 차리시고 주문을 다시해주세요👺")
    print()



#붕어빵 메인화면

while True:
    mode = input("원하는 모드를 선택하세요(주문, 관리자,재고, 종료): ") #주문
    #mode = "종료"
    if mode == "종료":
        break
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()
    elif mode == "재고":
        bread_num()

