import card_class as cc

cards = {}

#method to add cards to empty list
def add_to_list(cards, card):
    cards.append(card)
    return cards

#creating card objects and passing attributes 
wells_fargo = cc.Cards("wells", 18.49, 8800)
citi = cc.Cards("citi", 28.99, 2131.83)
costco = cc.Cards("costco", 19.74, 1938.46)
barclays = cc.Cards("barclays", 29.99, 1098.91)
amazon = cc.Cards("amazon", 26.99, 6068.62)


add_to_list(cards, wells_fargo)
add_to_list(cards, citi)
add_to_list(cards, costco)
add_to_list(cards, barclays)
add_to_list(cards, amazon)


wells_card = wells_fargo.interest_owed()
citi_card = citi.interest_owed()
costco_card = costco.interest_owed()
bar_card = barclays.interest_owed()
amazon_card = amazon.interest_owed()

for card in cards:
    print(card.apr)