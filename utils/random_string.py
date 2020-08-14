import random


def generate_short(length=1):
	characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
	return ''.join((random.choice(characters) for _ in range(length)))
