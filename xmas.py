import random

Kristin = {
	"name":"krispy",
	"index":1,
	"exclusions":[1,2]
}

Taylor = {
	"name":"tater",
	"index":2,
	"exclusions":[2,1]
}

Hannah = {
	"name":"spamster",
	"index":3,
	"exclusions":[3]
}

Thomas = {
	"name":"comets",
	"index":4,
	"exclusions":[4]
}

Wesley = {
	"name":"moosely",
	"index":5,
	"exclusions":[5]
}

participants = [Kristin, Taylor, Hannah, Thomas, Wesley]
translator = {1:"krispy",2:"tater",3:"spamster",4:"comets",5:"moosely"}
drawing = [1,2,3,4,5]
new = []

for x in drawing:
	placeholder = random.choice(drawing)
	
	for y in participants:
		if x == y["index"]:
			exclusion_placeholder = y["exclusions"]
	
	while True:
		if placeholder in new:
			print "the value was already selected"
			placeholder = random.choice(drawing)

		elif placeholder in exclusion_placeholder:
			print "value was unique but listed as an exclusion"
			placeholder = random.choice(drawing)
		
		else:
			print "unique value generated and not in excluded list"
			new.append(placeholder)
			break

counter = 1
for z in participants:
	result = new[counter - 1]
	print z["name"] + " has drawn " + translator[result] + "!!"
	counter += 1
		 
print str(new)

