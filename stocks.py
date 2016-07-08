stockDict = {'GM': 'General Motors', 'CAT':'Caterpillar', 'EK':'Eastman Kodak'}

purchases = [('GM', 100, '10-sep-2001', 48 ),
 ('CAT', 100, '1-apr-1999', 24 ),
 ('GM', 200, '1-jul-1998', 56 ),
 ('EK', 200, '2-aug-2000', 39),
 ('EK', 40, '6-jun-2006', 50)]

summaryDict = dict()
for key, value in stockDict.items():
	summaryDict[key] = 0
for p in purchases:
	total_price = p[1] * p[3]
	summaryDict[p[0]] += total_price

# for p in purchases:
	# summaryDict[value] = [p[1]]
	# total_price = p[1] * p[3]
	print(total_price)
	company_ticker = p[0]
	company_name = stockDict[company_ticker]

	output = ['You bought {0} shares '.format(p[1])]
	#Could also be output = ['you bought %s shares ' % (p[1])]
	output.append('of {0} '.format(company_name))
	output.append('at ${0}/share '.format(p[3]))
	output.append('for a total price of ${0}'.format(total_price))
	print(''.join(string for string in output))

print(summaryDict)

import code
code.interact(local=locals())
