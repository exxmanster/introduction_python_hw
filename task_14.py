#task_14

'''
Написать функцию, которая будет проверять четность некоторого числа.
		def is_even(number): # returns boolean value
			pass
'''

def is_even(number):
    if number %2==0:
        return True
    if number%2!=0:
        return False
print(is_even(6))