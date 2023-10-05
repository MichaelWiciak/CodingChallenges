This is a weird problem since there are a lot of things to take into account.

Rules
- 1. You only want to buy at price **x** if, at any point in the future, the price will be at least **x+1**
- If there is a **x+1** price, then we need to buy at x
- However, when should we hold the stock and when should we sell it instead?
- 2. So we have to calculate multiple possibilities and then pick the max. 

Approach
	At point p[x], get the price and see if there is a price in the future (further in the array) that is higher. Let's call that price **y**. If not, go to the next price, p[x+1], and repeat until the end of the array. If yes, we can buy it and sell it at that future price.
	However, this is where the complexity is coming from now.
	Once we have the stock, we can sell it at any point where p[x] < p[x+n]. There can be multiple p[x+n]. We could create a list of those p[x+n] and calculate which gives us the biggest profit.
	However, this might not always work as the value of n matters.
	If our prices look like this
		 [2,3,1,4]
	Then that approach will cause us to buy at 2 as there is a p[x] <p[x+n]. Actually, there are 2 of those values. Using max, we would sell at 4, giving us a profit of 2. 
	But if we bought at 2, sold at 3 bought at 1 and sold at 4, we have a profit of 1+3 = 4. So in this example, there are multiple ways of buying and selling
		buy at 2
			sell at 3
			sell at 4
		buy at 3
			sell at 4
		buy at 1
			sell at 4
	