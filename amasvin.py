class Drink:
  _cups = ["레귤러", "점보"]
  _ices = ["0%", "50%", "100%", "150%"]
  _sugars = ["0%", "50%", "100%", "150%"]
  _pearls = ["타피오카", "코코", "젤리", "알로에"]

  def __init__(self, name, price):
    self.name = name
    self.price = price
    self.cup = 0 #0 : 레귤러, 1 : 점보
    self.ice = 2 #0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%
    self.sugar = 2 #0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%

  def set_cup(self):
    self.cup = input("컵 사이즈를 선택하세요(0 : 레귤러, 1 : 점보)")
    if self.cup == "": #enter하면 빈 줄로 입력됨, enter하면 기본값으로 설정됨
      self.cup = 0
    else:
      self.cup = int(self.cup)

    # 점보 선택 시 가격 +500원
    if self.cup == 1:
      self.price += 500
  
  def set_ice(self):
    self.ice = input("얼음량을 선택하세요(0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%)")
    if self.ice == "":
      self.ice = 2
    else:
      self.ice = int(self.ice)

  def set_sugar(self):
    self.sugar = input("당도를 선택하세요(0 : 0%, 1 : 50%, 2 : 100%, 3 : 150%)")
    if self.sugar == "":
      self.sugar = 2
    else:
      self.sugar = int(self.sugar)

  def __str__(self):
    #이름 : self.name\t컵사이즈 : self.cup\t얼음량 : self.ice\t당도 : self.sugar
    return "이름 : "+self.name+"\t가격 : "+str(self.price)+"\t컵 사이즈 : "+self._cups[self.cup]+"\t얼음량 : "+self._ices[self.ice]+"\t당도 : "+self._sugars[self.sugar]

  def order(self):
    self.set_cup()
    self.set_ice()
    self.set_sugar() 

class Coffee(Drink):
  pass

class Bubbletea(Drink):
  def __init__(self, name, price):
    super().__init__(name, price)
    self.pearl = 0  #0 : 타피오카, 1 : 코코, 2 : 젤리, 3 : 알로에

  def set_pearl(self):
    self.pearl = input("펄을 선택하세요(0 : 타피오카, 1 : 코코, 2 : 젤리, 3 : 알로에)")
    if self.pearl == "":
      self.pearl = 0
    else:
      self.pearl = int(self.pearl)

  def __str__(self):
    return super().__str__() + "\t펄 : "+Drink._pearls[self.pearl] #Drink._pearls나 self._pearls나 똑같

  def order(self):
    # self.set_cup()
    # self.set_ice()
    # self.set_sugar()
    super().order()
    self.set_pearl()

class Order():
  def __init__(self):
    self.order_menu = []

  def show_menu(self):
    print("0 : 아메리카노 1800원, 1 : 딸기요거트 3500원")

  def order_drink(self):
    # 반복 ---
    while True:
      # show menu
      self.show_menu()

      # 주문받기, 음료 선택
      order = input("무엇을 고르시겠습니까 ?")
      
      if order == "":
        break
      #  _drinks = [Coffee("아메리카노", 1800), Bubbletea("딸기요거트", 3500)]
      # drink = _drinks[int(order)]
      if int(order) == 0:
        drink = Coffee("아메리카노", 1800)
      elif int(order) == 1:
        drink = Bubbletea("딸기요거트", 3500)
      # 음료 옵션 선택
      drink.order()
      
      self.order_menu.append(drink)
    # --- 반복 끝
    # 주문한 음료 내용 보여주기
    for d in self.order_menu:
      print(d)
    # 합계 금액 보여주기
    print("총금액 : "+str(self.sum_price())+"원")

  def sum_price(self):
    sum = 0
    for d in self.order_menu:
      sum += d.price

    return sum

o = Order()
o.order_drink()


# 아메리카노 = Coffee("아메리카노", 1800)
# 아메리카노.set_cup()
# 아메리카노.set_ice()
# 아메리카노.set_sugar()
# print(아메리카노)

# 하동녹차 = Bubbletea("하동녹차", 3800)
# 하동녹차.set_cup()
# 하동녹차.set_ice()
# 하동녹차.set_sugar()
# 하동녹차.set_pearl()
# print(하동녹차)

  