item=input('你想購買什麼物品?')
price=float(input('價格多少?'))
quantity=int(input('你需要多少件?'))

total=price*quantity

print(f'你購買了{quantity} {item}，總價為{total}元')