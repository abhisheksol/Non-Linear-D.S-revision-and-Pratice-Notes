prices = [7,1,5,3,6,4]

buy=0
sell=1
maxp=0
while sell< len(prices):
    if prices[buy]<prices[sell]:
        profit=prices[sell]-prices[buy]
        maxp=max(maxp,profit)
    else:
        buy=sell
    sell+=1
print(maxp)
    


