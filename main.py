import random

def on_click(event):
	lucky_number1 = random.randint(1, 59)
	lucky_number2 = random.randint(1, 59)
	lucky_number3 = random.randint(1, 59)
	lucky_number4 = random.randint(1, 59)
	lucky_number5 = random.randint(1, 59)
	lucky_number6 = random.randint(1, 59)

	lucky_numbers = f'{lucky_number1}, {lucky_number2}, {lucky_number3}, {lucky_number4}, {lucky_number5}, {lucky_number6}'

	button = document.getElementById('lucky-button')
	button.style.animation = 'none'
	button.style.width = 'auto'
	button.style.height = 'auto'
	button.innerHTML = lucky_numbers