# blind auction
bid_dictionary = {

}
more_bidders = True

def make_bid():
    name = input("Please enter the bidders name:\n")
    bid_price = int(input("Please input the bidders price:\n"))
    bid_dictionary[name] = bid_price

def ask_if_more_bidders(continue_bidding):
    question = input("Are there any more bidders? Yes or No\n")
    if question.lower() == "no":
        continue_bidding = False
        return continue_bidding



while more_bidders:
    make_bid()
    more_bidders = ask_if_more_bidders(more_bidders)

print(bid_dictionary)