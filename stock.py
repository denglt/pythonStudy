import easyquotation

quotation = easyquotation.use('sina')

# s = quotation.market_snapshot(prefix=True)
s = quotation.stocks(['300059'])
print('===================sina=======================')
print(s)

quotation = easyquotation.use('qq')

# s = quotation.market_snapshot(prefix=True)
s = quotation.stocks(['300059'])
print('===================qq=======================')
print(s)