import sys
customer = 'blank'
agentJpref = 'coffee'
agentQpref = 'decaf coffee'
agentSpref = 'coffee'
agentMpref = 'tea'

coffee_available = False
tea_available = True
decaf_available = True
argv = customer

if sys.argv[2] == 'J':
    if coffee_available == True:
        print("Agent J prefers coffee and we have plenty")
    else:
        print("Agent J prefers coffee, but we are out, Agent J will have tea instead")
if sys.argv[2] == 'Q':
    if decaf_available == True:
        print("Agent Q prefers decaf coffee and we have plenty")
    else:
        print("Agent Q prefers decaf coffee but we are out of decaf")
if sys.argv[2] == 'S':
    if coffee_available == True:
        print("Agent S prefers coffee and we have plenty")
    else:
        print("Agent S prefers coffee but we are out, so Agent S will have decaf instead")
if sys.argv[2] == 'M':
    if tea_available == True:
        print("Agent M prefers tea and we have plenty")
    else:
        print("Agent M prefers tea but we are out")
if sys.argv[2] == 'T':
	if coffee_available == True:
		print("We do not have any preferences for Agent T, but try coffee")
	else:
		print("We do not have any preferences for Agent T, and we are out of coffee, so try tea?")
