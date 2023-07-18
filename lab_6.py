
# method adds 3 to each digit in given password
def encode(password):
	encoded_password = ''
	for idx, num in enumerate(password):    # for-loop iterates over given password
		num = int(num) + 3
		num = str(num)
		encoded_password += num

	return encoded_password     # returns new password which each digit shifted up 3 numbers


# method subtracts 3 from each digit in given encoded password
def decode(encoded_password):
	decoded_password = ''
	for idx, num in enumerate(encoded_password):    # for-loop iterates over encoded_password
		num = int(num) - 3
		num = str(num)
		decoded_password += num

	return decoded_password      # returns original password given by user


# method prints the menu options
def menu():
	print('Menu')
	print('-------------')
	print('1. Encode')
	print('2. Decode')
	print('3. Quit')


# this is the main function
def main():
	program_continue = True
	while program_continue:       # iterates while program_continue = True
		menu()
		print()
		user_option = input('Please enter an option: ')

		# if user_option equals '1', the given password is encoded
		if user_option == '1':
			password = input('Please enter your password to encode: ')
			encoded_password = encode(password)
			print('Your password has been encoded and stored!')
			print()

		# if user_option equals '2', the encoded password is decoded back to original password
		elif user_option == '2':
			decoded_password = decode(encoded_password)
			print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')
			print()

		# if user_option equals '3', the program ends
		elif user_option == '3':
			program_continue = False


if __name__ == '__main__':
	main()
