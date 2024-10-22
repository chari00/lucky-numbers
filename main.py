import random

def on_click(event):
	lucky_numbers = []
	while len(lucky_numbers) < 6:
		num = random.randint(1, 59)
		if num not in lucky_numbers:
			lucky_numbers.append(num)

	button = document.getElementById('lucky-button')
	button.style.animation = 'none'
	button.style.width = 'auto'
	button.style.height = 'auto'
	button.innerHTML = lucky_numbers