from replit import clear
from art import logo
print(logo)

bids = {}
bid_finish = False


def highest_bid (bid_record):
    most_highest_bid = 0
    winner = ""
    for bids in bid_record:
        bid_amount = bid_record[bids]
        if bid_amount > most_highest_bid:
            most_highest_bid = bid_amount
            winner = bids

    print (f"The winner is {name} with amount of Rs.{price}")


while not bid_finish:
    name = input("whats ur name?")
    price = int(input("whats ur bid? Rs."))
    bids[name]=price
    go_ahead= input("Any more bidders? 'y/n'")
        
    if go_ahead == 'n':
        bid_finish=True
        highest_bid(bids)
    elif go_ahead == 'n':
        clear()
        
