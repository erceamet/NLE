import re

#some extra examples were added which can be removed
#the last 4 matches are the ones from the BBC article
print("PART 1 MATCHING CURRENCY")

regex = r"([$£€]+\d+[,.]*\d*\w*)|(\d+(?:milion|mil|m|bilion|bil|bn|b|pence|p)[ ]*(?:euros|euro)*)|([$£€]+\d+[,.]+\d+)"

test_str = ("$131bn\n"
	"$17.4bn\n"
	"£50,000\n"
	"€50.000\n"
	"£40,000\n"
	"£117.3m\n"
	"30p\n"
	"500m euro\n"
	"338bn euros\n"
	"$15bn\n"
	"$15m\n"
	"$92.88\n"
	"€29\n"
	"€2\n\n"
	"The US economy expanded at an annual pace of 3% during the three months to the end of September, which was stronger than expected.\n\n"
	"The growth extended the robust activity reported in the previous quarter, when US GDP grew at an annual pace of 3.1%.\n\n"
	"Analysts had been expecting a sharp slowdown after back-to-back hurricanes battered several states in the quarter.\n\n"
	"But consumer spending held steady, despite a drop in homebuilding investment.\n\n"
	"Together the two quarters mark the strongest six months of economic activity for the US since 2014, the Commerce Department said.\n\n"
	"\"Overall, this is a very solid performance, given the disruption caused by Hurricanes Harvey and Irma,\" wrote Ian Shepherdson of Pantheon Macroeconomics.\n\n"
	"\"Their net effect seems to have been smaller and shorter than we expected.\"\n\n"
	"What went into the figure?\n"
	"Consumer spending, which increased at a hearty 3.3% rate in the second quarter, slowed to 2.4% growth - a deceleration probably caused by the hurricanes.\n\n"
	"Construction spending also fell, but exports and business investments in equipment and intellectual property accelerated from the previous quarter\n\n"
	"Economists warned that estimates of business inventories, a major factor in the GDP rise, can vary significantly quarter-to-quarter.\n\n"
	"Excluding that category, GDP - a broad measure of goods and services made in the US - increased at an annual pace of 2.3%.\n\n"
	"The Commerce Department cautioned that its figures did not capture all the losses caused by the storms, which caused widespread closures of factories, offices and airports in states such as Florida and Texas.\n\n"
	"Its GDP estimates, for example, do not measure activity in US territories, such as Puerto Rico, which suffered some of the most severe damage.\n\n"
	"The Commerce Department estimated that storm-related damage to fixed assets, such as homes and government buildings, totalled more than $131bn (£100bn).\n\n"
	"It also said it expected the government and insurers to pay more than $100bn in insurance claims, with foreign companies accounting for more than $17.4bn.\n\n"
	"chart of US GDP growth by president\n"
	"Commerce Department Secretary Wilbur Ross claimed Friday's GDP report a sign of progress, calling it a \"remarkable achievement in light of the recent hurricanes\".\n\n"
	"President Donald Trump has made hitting annual GDP growth of 3% a goal, and pledged tax cuts and other policies intended to reach that pace or higher.\n\n"
	"\"President Trump's bold agenda is steadily overcoming the dismal economy inherited from the previous administration,\" Mr Ross said. \"As the President's tax cut plan is implemented, our entire economy will continue to come roaring back.\"\n\n"
	"On a year-on-year basis, GDP was up 2.3%, the Commerce Department said in its report, which is an advance estimate that will be revised as more data is collected.\n\n"
	"That pace is roughly in line with US expansion since the 2007-2009 recession.\n\n"
	"Kenneth Rogoff, a professor of economics at Harvard University, said the growth reflects improvement in the labour market and other areas that date back to the Obama administration.\n\n"
	"While some of the president's plans may boost growth, they're not in place yet, he said.\n\n"
	"\"Let's make no mistake - this was a very good number,\" he said. \"Jobs have been improving, consumption's been improving, businesses are doing better, there is a profound inequality problem but the US economy, despite not much from President Trump, has been doing well.\"\n\n"
	"Economists said the underlying economic strength shown in the report makes it more likely that central bankers at the US Federal Reserve will raise interest rates again by the end of the year, as expected.\n\n"
	"The price index for consumer spending, a closely-watched measure of inflation, increased at 1.3% in the third quarter, excluding food and energy. That remains below the Federal Reserve's 2% target.")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))


print("PART 1 MATCHING PHONE NUMBERS")

regex = r"(\d+[.]\d+[.]\d+)|([+]*\d+[-]+[(]*\d+[)]*[-]+\d+[-]\d+)|(\d+(?:[-.]*|[ ])\d+(?:[-]*|[ ])\d+)|([(]\d*[)](?:[-]*|[ ])\d+(?:[-]*|[ ])\d+)"

test_str = ("555.123.4565\n"
	"+1-(800)-545-2468\n"
	"2-(800)-545-2468\n"
	"3-800-545-2468\n"
	"555-123-3456\n"
	"555 222 3342\n"
	"(234) 234 2442\n"
	"(243)-234-2342\n"
	"1234567890\n"
	"123.456.7890\n"
	"123.4567\n"
	"123-4567\n"
	"1234567900\n"
	"12345678900")

matches = re.finditer(regex, test_str, re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
    
    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
