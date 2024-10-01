def find_common_char(string1, string2):
	set1 = set(string1)
	set2 = set(string2)
	commonLetters = {}
	for i in set1:
		if(i in set2):
			return i		

	return None

def find_occurence_word(string):
	word_occurence = {}
	words = string.split()
	for i in words:
		word_occurence[i]=word_occurence.get(i, 0) +1

	print(f"words and occurence: ", word_occurence)

def merge_lists(list1, list2):
	print(dict(zip(list1, list2)))

def find_nth_largest(array, n):
	array.sort()
	return array[n-1]

def merge_sorted_arrays(array1,array2):
	i=0
	j=0
	merged_array = []
	array1.sort()
	array2.sort()
	while(i<len(array1) and j<len(array2)):
		if(array1[i]<array2[j]):
			merged_array.append(array1[i])
			i+=1
		else:
			merged_array.append(array2[j])
			j+=1		
		
	while(i<len(array1)):
		merged_array.append(array1[i])
		i+=1

	while(j<len(array2)):
		merged_array.append(array2[j])
		j+=1

	return merged_array

#string1 = input("Enter 1st string: ")
#string2 = input("Enter 2nd string: ")
#print(f"common char is :", find_common_char(string1,string2))
#find_occurence_word(string1)
#merge_lists([1,2,3],["one","two","three"])
#print(f"result",find_nth_largest([8,4,6,1,0,4,7,3,25,7,3,0,24,8,6], 14))
print(f"Merged array", merge_sorted_arrays([2,9,0,5,6,1],[8,10,7,4,3,11]))