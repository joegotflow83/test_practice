def add(x, y):

	return x + y

def sub(x, y):

	return x - y

def conditional(age):

	if age < 21:

		return 'You can not drink'

	else:

		return 'You can drink'

def is_prime(num):

	divisors = [x for x in range(num) if x != 0]

	for digit in divisors:

		if digit == 1:

			continue

		elif num % digit == 0:

			return 'This number is not prime'
			break

	else:

		return 'This number is prime'

is_prime(45)
