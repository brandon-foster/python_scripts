from sys import exit
prompt = "> "
def gold_room():
	print "This room is full of gold. How much do you take?"
	
	next = raw_input(prompt)
	if "0" in next or "1" in next:
		how_much = int(next)
	else:
		dead("Man, learn to type a number.")
		
	if how_much < 50:
		print "Nice, you're not greedy, you win!"
		exit(0)
	else:
		dead("You greedy person!")
		
def bear_room():
	print "There is a bear here."
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False
	
	while True:
		next = raw_input(prompt)
		
		if next == "take honey":
			dead("The bear looks at you then hugs your face off.")
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go through it now."
			bear_moved = True
		elif next == "Taunt bear" and bear_moved:
			dead("The bear gets upset and hugs your leg off.")
		elif next == "open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means."
				
def cthulhu_room():
	print "Here you see the great evil Cthulhu."
	print "He, it whatever stares at you and you go insane."
	print "Do you flee for your life?"
	
	next = raw_input(prompt)
	
	if "flee" in next:
		start()
	elif "stay" in next:
		dead("You chose to stay.")
	else:
		cthulhu_room()

def dead(why):
	print why, "Good, job!"
	exit(0)
	
def start():
	print "You are in a dark room."
	print "There is a door to your right and left."
	print "Which one do you take?"
	
	next = raw_input(prompt)
	
	if next == "left":
		bear_room()
	elif next == "right":
		cthulhu_rom()
	else:
		dead("You stumble around the room.")
		
start()
