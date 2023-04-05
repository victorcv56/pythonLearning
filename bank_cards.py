import card_class as cc

wells_fargo = cc.Cards("wells", 18.49, 8800)
citi = cc.Cards("citi", 28.99, 2131.83)
costco = cc.Cards("costco", 19.74, 1938.46)
barclays = cc.Cards("barclays", 29.99, 1098.91)
amazon = cc.Cards("amazon", 26.99, 6068.62)

wells_card = wells_fargo.interest_owed()
citi_card = citi.interest_owed()
costco_card = costco.interest_owed()
bar_card = barclays.interest_owed()
amazon_card = amazon.interest_owed()

