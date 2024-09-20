#Selling Cookies Exercise 

start_money = float(input("How much money did you start with? "))
cookies_sold = input("How many cookies were sold? ")

big_cookies = cookies_sold.count('b')
small_cookies = cookies_sold.count('c')

total_cookies = big_cookies + small_cookies 
profit = (big_cookies * 2.00) + (small_cookies * 1.25)
end_day = profit + start_money 

print(f"You sold {total_cookies} cookies.\nYou made a profit of ${profit}.\nThe end day amount is ${end_day}")