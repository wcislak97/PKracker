import hashlib
import itertools

lowerCaseList = list(map(chr, range(97,123)))
upperCaseList = list(map(chr, range(65,91)))
specialCharactersList1 = list(map(chr, range(32,48)))
specialCharactersList2 = list(map(chr, range(58,64)))
specialCharactersList3 = list(map(chr, range(91,97)))
specialCharactersList4 = list(map(chr, range(123,127)))
specialCharactersListTotal = specialCharactersList1 + specialCharactersList2 + specialCharactersList3 + specialCharactersList4
digitsList = list(map(chr, range(48,58)))
# print(lowerCaseList)
# print(upperCaseList)
# print(specialCharactersList1)
# print(specialCharactersList2)
# print(specialCharactersList3)
# print(specialCharactersList4)
# print(digitsList)

def decryptBruteForce(myHash, maxLen):
	# Flag for founded hash
	found = False
	# Generate all combinations of the characters
	for x in range(1, maxLen + 1):
		combinations = itertools.product(lowerCaseList, repeat=x)
		# Print each combination
		for combination in combinations:
			investigatedHash = hashlib.md5((''.join(combination)).encode('utf-8')).hexdigest()
			if myHash == investigatedHash:
				print("Found matching hash:", myHash)
				found = True
				break
		x += 1
	if found == False:
		print("No matching hash found.")


decryptBruteForce("900150983cd24fb0d6963f7d28e17f72",3)