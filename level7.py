import re

cache = {}

def read_input(path,callback):
	with open(path,'r') as inputfile:
		return callback(inputfile)

def parse_rule_line(line):
	(source,contain) = line.split(' bags contain ')
	rule = {source:[]}
	if 'no other' in contain:
		return rule
	for obj in contain.replace('.','').strip().split(','):
		obj = obj.replace('bags','').replace('bag','').strip()
		arr = obj.split(' ')
		amount = int(arr[0])
		color = ' '.join(arr[1:])
		rule[source] += [color]*amount
	return rule



def readrules(inputfileobj):
	rules = {}
	for line in inputfileobj.readlines():
		rule = parse_rule_line(line)
		rules.update(rule)
	return rules

def find_top_bags(found,rules,color):

	for rule in rules:
		if color in rules[rule]:
			# print(found,rule)
			found.add(rule)
	mark = False
	for fcolor in found:
		if fcolor in rules:
			del rules[fcolor]
			mark = True

	if not mark:
		return found
	temp = list(found)
	for fcolor in temp:
		# print(found,rules,fcolor)
		found |= find_top_bags(found,rules,fcolor)
	return found

def find_internal_bags(count,rules,color,):
	print("start",count,color)
	for containedcolor in rules[color]:
		if containedcolor in cache:
			count+= cache[containedcolor]
		elif len(rules[containedcolor]) == 0 :
			print(containedcolor, "is empty")
			count +=1
		else:
			print("in else")
			cache[containedcolor] = find_internal_bags(0,rules,containedcolor)+1
			print(containedcolor,cache[containedcolor],rules[containedcolor])
			count += cache[containedcolor]
	return count

def main():
	inputpath = 'level7input'
	# inputpath = 'demoinput'
	rules = read_input(inputpath,readrules)
	# print(rules)
	# print(len(find_top_bags(set(),rules,'shiny gold')))
	print(find_internal_bags(0,rules,'shiny gold'))

if __name__ == '__main__':
	main()