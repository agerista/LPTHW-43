import sys #only if delayed typing works
import time
import random
from random import randint
from sys import exit




class Scene(object):

	def enter(self):
		print "Scene enter()"
		exit(1)
		
	# Trying to make the whole game print out one character at a time for readability
	#def delay_print(s):
		
		#for c in s:
			
			#sys.stdout.write('%s' % c)
			#sys.stdout.flush()
			#time.sleep(0.25)
			
	#delay_print()
		
class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
			
		current_scene.enter()	
		
class Dead(Scene):

	def enter(self):
		
	
		group = {"The Gothons got you!", "The Gothon devours you",
				"You find yourself inside the Gothon's stomach.",
				"Sensing your hesitancy with their heightened sense of smell, they realize that you are not a Gothon at all. They eat you.",
				"You stumble into a Gothon who claws your face off.", 
				"Gothon doesn't like to be messed with, Gothon eats you.",
				"You become a delicious meal for the Gothon.", 
				"You have only a quick moment of clarity before the Gothon devours you.",
				"You are electrocuted and die!", 
				"Having failed your mission, you are immediately vaporized.",
				"Outnumbered by Gothons, they cut you up into bite snack size pieces.",
				
		}
		
		number = 1
		list = random.sample(group, number)
		first = list[0]
		print first	
		exit(1)	

class Finished(Scene):

	def enter(self):
		print "You hear your commander once again in your earpiece. >>Mission complete!"
		print "You have saved the galaxy from the wrath of the Gothons. You will go down"
		print "in history books as a legend and a hero! Now set your coordinates for your"
		print "next mission.  Time is of the essence, we are counting on you!" 
		exit(1)
		
class CentralCorridor(Scene):

	def enter(self):
		print "BEEP!, BEEP!, BEEP!, BEEP!" * 7
		print """
		 You wake up and find yourself on a strange ship.
		 >>HOLY SH*!
		 					>>I see one!
		 >>OH MY GOD!!!
		 					>>WHAT'S HAPPENING
		 (Lasers are shooting out of every direction)
		 >>Take cover!
		 										>>AHHHHHHHHH!
		 			>>Zorp, Derp, Gurrgggglllllle, Zoooorr!
		 (Pew, Pew, Pew)
		 >>They're...the...they're invading
				>>Gothons...Everywhere
		 (All men to your battlestations)
		 (We have a breach)																	
		 (All hands on deck)
		 \n\nYou notice your best mate is also here.
		 It's clear he needs help, he can't fight the Gothons alone!
		 Do you:
		 1. Grab your mate and make a run for it
		 2. Continue on your own
		 3. Tell your Mate you will send help
		"""
		
		mate = raw_input(">  ")
		
		if mate == "1":
			print "\n\nYou grab your mate and run for safety, dodging the lasers as best"
			print "you can. You realize your mate is in much worse shape than you"
			print "thought. You find a closet and ditch your friend inside."
			print "Assuring him that you will come back or send help. He's not too happy,"
			print "but he understands. As you exit the closet, you are confronted with a"
			print "Gothon. He, It, whatever, is HUGE and hairy. He, It, whatever, starts"
			print "growling and snarling at you. You know it is only a matter of time"
			print "before he tries to bite your face off. Frantically, you search for a"
			print "weapon. Realizing that you have nothing but your fists, you start to"
			print "fight. The Gothon is bigger and stronger than you. You don't last too"
			print "long."
			return 'dead'
			
			
		elif mate == "2":
			print "\n\nEvery man for himself. There was no way you would both make it out"
			print "alive. You duck into a closet for a moment to get your bearing and "
			print "hatch a plan. You see a lasergun lying on the ground!"
			grab_gun = False
			
			while True:
				gun = raw_input(">  ")
				
				if "grab gun" in gun or "take gun" in gun or "take lasergun" in gun or "grab lasergun" in gun:
					print "You grab the gun and leave the closet."
					grab_gun = True
					break
					
				elif "exit closet" in gun:
					print "You may find a gun useful later."
					grab_gun = False
					
				else:
					return 'dead'			
			
			print "\nAs you are stumbling out of the closet, you run into a mean looking"
			print "Gothon. He, It, whatever, is HUGE and hairy. He, It, whatever, starts"
			print "growling and snarling at you. You know it is only a matter of time"
			print "before he tries to bite your face off. You find a giant weapon that"
			print "looks like a pitchfork."
			grab_pitchfork = False
			
			while True:
				pitch = raw_input(">  ")
				
				if "grab pitchfork" in pitch or "take pitchfork" in pitch:
					print "You grab the pitchfork."
					grab_pitchfork = True
					break
				
				else:
					print "The pichfork might prove useful."
					
			print "\nThe Gothon lunges toward you."
			print """
			Do you:
			1. Make a low sweeping motion with the pitchfork, 
				taking the Gothon out at the knees.
			2. Notice that the prongs of the pitchfork are spaced to the same with of 
				the Gothons eyes. Thus, making a face stabbing a good idea.
			3. Run for it!	
			"""			
			
			choice = raw_input(">  ")
			
			if choice == "1":
				print "\nThe Gothon goes down, hard. You hear him moaning as you run down"
				print "the hall. You don't get very far before you see three Gothons in"
				print "front of you blocking your way. You start to fight them with your"
				print "pitchfork, but the biggest one takes it from you. Remembering"
				print "that you have a lasergun, you whip it out and start to shoot."
				print "You hit one of the Gothons, but the other Gothon swats the gun"
				print "from your hand. You scramble towards the gun. As you do so, the"
				print "third Gothon reaches down and shreds you into little tiny pieces."
				return 'dead'
				
			elif choice == "2":
				print "\nYou hear the sound of the Gothons eyes popping."
				print "The Gothon lets out a sound like nothing you have ever heard before."
				print "RRreeEAAaAHhhhrRRRrggGHHhkkSSMMGggffFFLLleeRREEAAHHrrfff!!!"
				time.sleep(2)
				print "\nUnfortunately, no one told you that the Gothons don't really "
				print "need their eyes. The Gothon starts gaining on you. As he, it,"
				print "whatever gets closer, he, it, whatever starts swiping at you."
				print """
				Do you:
				1. Run faster
				2. Remember your laser gun and shoot
				3. Find a closet to hide in?
				"""
				
				tactic = raw_input(">  ")
				
				if tactic == "1":
					print "You run as fast as you can. Usain Bolt couldn't go any faster."
					print "It becomes harder and harder to breathe. You start seeing"
					print "stars and suddenly, everything goes black. A warm sensation"
					print "envelops your body. You hear a faint roar."
					return 'dead'
					
					
				elif tactic == "2":
					print "\nAs you're running, you grab the laser gun from your"
					print "waistband. You turn just enough so you can shoot at the Gothon"
					print "behind you. RRreeEAAaAHhhhrRRRrgg. The Gothon goes down."
					print "You keep running down the Central Corridor. Ahead of you, you"
					print "see 3 mean looking Gothons. There is a door to your left, and"
					print "one to your right. Or you could continue down the hallway."
					
					route = raw_input(">  ")
					
					if "left" in route or "l" in route:
						print "\n\nYou open the door on the left, and walk into the room."
						print "You see what you think is a sleeping Gothon. Feeling oddly"
						print "brave, you move toward the Gothon. He, it, whatever, looks"
						print "oddly deflated. You take a deep breathe, and poke the"
						print "Gothon. Quickly, it becomes clear that this is no Gothon"
						print "at all. Your not sure why it's here. But it seems as"
						print "though you have found a Gothon disguise. You put on the"
						print "disguise and head back out into the Central Corridor."
						print "Immediately, the 3 Gothons surround you."
						print ">> Jokes, jokes, jokes."
						print "This suit must have a translator, "
						print "as you are suddenly able to understand the Gothons."
						print "Do you start telling jokes?"
						
						answer = raw_input("Yes or No  ")
						
						if "Yes" in answer or "yes" in answer or "y" in answer:
							group = {"Where does bad light end up? In a prism.", 
									 "What does a nosy pepper do? Get jalapeno buisness.",
									"Anything that doesn't matter has no mass.",
									 "What did one uranium-238 nucleus say to the other? Gotta split!",
									 "The Heineken Uncertainty Principle says, You can never be sure how many beers you had last night." }
							
							number = 3
							list = random.sample(group, number)
							first = list
							print first	
							
							print "\nYou really get the Gothons laughing."
							print "You slip passed them and continue walking."
							return 'laser_weapon_armory'
									
						else:	
							return 'dead'
								
							
					elif "right" in route or "r" in route:
						print "\n\nYou have stumbled into what seems to be a bar."
						print "Reaching into your pockets, you notice that you have a"
						print "payment pass. Not sure if it is loaded, you are a bit"
						print "hesitant. You also notice that you have what looks to be"
						print "an ancient coin in your pocket. You have heard that humans"
						print "used to use these to make decisions. You decide to use"
						print "this old tradition to decide whether or not to use the pay"
						print "pass.You assign heads to try out the pass, and tails the"
						print "opposite. When you are ready flip the coin."
								
						toss = raw_input("Enter flip or toss  ")
						
						rand = random.randint(1, 3)

						if rand == 1:
							print "\nHeads, lucky you!"
							print "You take a deep breath and head up to the bar."
							print "Zorglog catches your eye, so you order one."
							print "You present your payment pass and hope it works."
							print "The bar tender takes it, looks at it, at you, raises"
							print "an eyebrow. You smile your biggest smile."
							time.sleep(2)
							print "Success, it works!"
							print "You decide to stay and have another."
							print "The place is starting to fill up."
							print "Someone sits down next to you and orders a drink."
							print "You strike up a conversation."
							print "The zorglogs must be stronger than you thought."
							print "You have the sudden desire to do a stand-up routine."
							print "Do you start telling your neighbor jokes?"
							
							answer = raw_input("Yes or No  ")
						
							if "Yes" in answer or "yes" in answer or "y" in answer:
								group = {"Where does bad light end up? In a prism.", 
										"What does a nosy pepper do? Get jalapeno buisness.",
										"Anything that doesn't matter has no mass.",
										"What did one uranium-238 nucleus say to the other? Gotta split!",
									 	"The Heineken Uncertainty Principle says, You can never be sure how many beers you had last night." }
							
								number = 3
								list = random.sample(group, number)
								first = list
								print first	
								
								print "Your jokes get progressively worse and the"
								print "bartender kicks you out. You stumble out the door"
								print "and into the Central Corridor right into a Gothon."
								return 'dead'
							
						else:
							print "\nTails, it's time to pack up and go."
							print "You don't really want to leave, but decide not to"
							print "press your luck. It's not really the time to get drunk"
							print "anyway, there are Gothons to fight.You head for the"
							print "door, back into the Central Corridor. Just as you step"
							print "out the door, you run right into a Gothon."
							return 'dead'
							
							
							
							
					elif "continue" in route or "c" in route or "straight" in route or "s" in route:			
						print "\n\nYou decide that straight is your best option and"
						print "continue down the hallway. You place the pitchfork just"
						print "inside a door, out of the way, but quickly accessible."
						print "\n\nLasergun in hand you start shooting at the Gothons."
						print "Lasers are flying all around, and you are successfully"
						print "dodging them all. One of the Gothons is now right in front"
						print "of you. Suddenly, the kung fu classes you took as a kid"
						print "come back to you. You become some kind of super ninja,"
						print "kicking, flipping, and landing blows to the Gothons vital"
						print "organs. One Gothon down. \n\nYou double back flip and grab"
						print "the pitchfork. You take a flying leap toward the second"
						print "Gothon. The pitchfork stabs the second Gothon in the eye."
						print "You pirouette, bringing the pitchfork down to a low angle"
						print "and take him out at the knees. Quickly, you twirl the"
						print "pitchfork, bringing the butt end down repeatedly, hitting"
						print "all of the Gothons vital organs. He, it, whatever, won't"
						print "be gettting up for a while. \n\nTaking the knife from the"
						print "second Gothons holster, you head towards the third. You"
						print "are unstoppable. You do a low-sweeping turn kick that ends"
						print "with you stabbing the third Gothon in the stomach. He"
						print "seems unfazed. So you jump up high, levitating as you"
						print "reapeatedly kick the third Gothon in the face. The third"
						print "Gothon starts to wobble and stumble back. You take this"
						print "opportunity to stab him, it, whatever, repeatedly. When"
						print "your satisfied you continue on your mission. You go"
						print "southwest to Laser Weapon Armory."
						return 'laser_weapon_armory'	
							
					else:
						return 'dead'
					
				elif tactic == "3":
					print "\nYou see a closet door up ahead. When you are sure that the"
					print "Gothon is looking in the other direction, you slip inside." 
					print "No one told you that Gothons have a highly sensitive nose."
					print "They are very similar to dogs that way."
					print "You hear the Gothon ambling down the hallway."
					print "Before you know it, the Gothon is at the door."
					print "He, it, whatever, body checks the door and scoops you up."
					return 'dead'
				
				else:
					return 'dead'
				
			elif choice == "3":
				print "\nYou start running."
				print "You get about 10 feet before you feel breath on the back of your"
				print "neck. A split second later, you feel a giant paw."
				return 'dead'
				
				
			else:
				return 'dead'	  
			
		elif mate == "3":
			print "\nYou noticed that your mate wasn't fairing so well. You lean over him"
			print "and try to comfort him as much as possible. While you are doing so"
			print "a Gothon sneaks up behind you."
			return 'dead'
			
		else:
			return 'dead'		
		
class LaserWeaponArmory(Scene):

	def enter(self):
		print "\n\nYou have entered the Laser Weapon Armory."
		print "This hallway is actively trying to keep you out in any way possible."
		print "To proceed, you must first answer a riddle."
		print "I am the beginning of the end, the end of every place." 
		print "I am the beginning of eternity, the end of time and space. What am I?"
		
		tries_allowed = 2
		tries = 1
		win = False
		
		while True and tries <= 5:
			tries += 1
			solve = raw_input(">  ")
			
			if solve == "the letter e":
				print "You solved the riddle!"
				win = True
				break
				
			elif solve == "i don't know":
				print "phone a friend"
				time.sleep(5)
				print "Your friend says it might have to do with letters."
				
			else:
				print "That's not the answer, try again."
				
		else:
			print "You failed to guess in time!"
			return 'dead'
							
		# Hall of quick sand		
		print "\nImmediately after solving the riddle, you begin to sink, "
		print "like you're slowly falling into a hole."
		print "You begin to panic and thrash about."
		print "The more you panic, the faster you fall."
		print "Realizing this, you get become angrier and angrier. It doesn't help."
		print "You tell yourself to relax and begin breathing deeper."
		print "Your fall starts to slow."
		print "You hear a voice in your head saying 'lay back', so you do."
		print "All of the sudden, you are floating up to where you started."
		print "When you reach solid ground, you stand up."
		print "\nAhead of you is a door. You hit the open button."
		print "A small window at eye level opens and someone looks out at you."
		print 'The voice demands >>"Whats the password?" '
		password = False
		
		# expand below?
		# Password
		tries_allowed = 5
		tries = 1
		win = False
		
		while True and tries <= 5:
			tries += 1
			answer = raw_input(">  ")
			
			group = {"percal", "aliens", "invasion", "riddler", "lasers"}
			
			number = 1
			list = random.sample(group, number)
			first = list[0]
			
			if answer in first:
				print "\nYou may enter."
				win = True
				break
				
			else:
				print "\nTry again."
				password = False
		
		else: 
			print "\nYou failed to guess in time!"
			return 'dead'			
		
		# Hologram Gothon appears				
		print "\n\nA Gothon forms from thin air in front of you."
		print "RRreeEAAaAHhhhrRRRrggGHHhkkSSMMGggffFFLLleeRREEAAHHrrfff!!!"
		print "It appears that he is very angry."
		print "The Gothon begins clawing at your face."
		print "Blood running into your eye, you knee him in the groin."
		print "The Gothon throws you to the floor."
		print "He, it, whatever, hovers over you and bares his teeth."
		print "RRreeEAAaAHhhhrRRRrggGHHhkkSSMMGggffFFLLleeRREEAAHHrrfff!!!"
		print "Out of the corner of your eye, you find a transporter."
		print "You reach for it, but it is just out of reach."
		print "The Gothon rips your shirt of and licks his lips."
		print "If you don't get the transporter soon, you'll be Gothon snacks."
		print "You somehow make your way to your feet."
		print "The Gothon tries to push you back down, but misses."
		print "You do a spinning turn kick, taking the Gothon out at the knees."
		print "You rush to the transporter, and hit the button."
		print "The Gothon starts dissolving into thin air, he, it, "
		print "whatever is someone else's problem now."
		
		# Find a neutron bomb
		print "\nYou keep walking forward and see a room full of objects."
		print "After assessing all of the objects, the following seem the most useful."
		print "Some ropes are located to your left."
		print "Laserguns, so many laserguns to your right."
		print "A neutron bomb."
		print "You have room for two items, what do you take?"
		
		take = raw_input("Enter two items  ")
		print "%r taken" % take
		
		if "neutron bomb and laserguns" in take:
			print "\n\nGood choice!"
			print "As you are taking these items, an earpiece drops to the floor."
			print "You pick it up from the floor and place it in your ear."
			print "There is a bunch of horrible feedback at first."
			print "You take a moment to look at the earpiece and fix the problem."
			print "Back in your ear, you hear a voice speaking to you."
			print "It is your commander."
			print ">>We don't have much time."
			print ">>It is imperative that you place the neutron bomb on the bridge."
			print ">>Get yourself to an escape pod and get out."
			print ">>We'll talk more later, for now, you have your mission."
			print "You can go northeast towards the bridge."
			return 'the_bridge'
			
		elif "neutron bomb and ropes" in take:
			print "\n\nSure, that'll work."
			print "As you are taking these items, an earpiece drops to the floor."
			print "You pick it up from the floor and place it in your ear."
			print "There is a bunch of horrible feedback at first."
			print "You take a moment to look at the earpiece and fix the problem."
			print "Back in your ear, you hear a voice speaking to you."
			print "It is your commander."
			print ">>We don't have much time."
			print ">>It is imperative that you place the neutron bomb on the bridge."
			print ">>Get yourself to an escape pod and get out."
			print ">>We'll talk more later, for now, you have your mission."
			print "You can go northeast towards the bridge."
			return 'the_bridge'
			
		elif "ropes and laserguns" in take:
			print "\n\nYou pick it up from the floor and place it in your ear."
			print "There is a bunch of horrible feedback at first."
			print "You take a moment to look at the earpiece and fix the problem."
			print "Back in your ear, you hear a voice speaking to you."
			print "It is your commander."
			print ">>We don't have much time."
			print ">>It is imperative that you place the neutron bomb on the bridge."
			print ">>Get yourself to an escape pod and get out."
			print ">>We'll talk more later, for now, you have your mission."
			print "You try to go back to the room and retrieve the neutron bomb, "
			print "but the room has disappeared."
			return 'dead'
			
		else:
			print "\nBare fists only get you so far."
			return 'dead'	
		

class TheBridge(Scene):

	def enter(self):
		print "\n\nTo enter the bridge, you will need a passcode."
		print "This pass code is 3 digits."
		
		code = "537"
		tries_allowed = 10
		tries = 1
		win = False
		
		while True:
			tries += 1
			tries <= tries_allowed
			attempt = raw_input(">  ")
			
			if "537" in attempt:
				print "Acces granted!"
				win = True
				break
				
			elif "007" in attempt:
				print "Access granted!"
				win = True
				break
				
			else:
				print "Access denied, please enter a valid code."
				
		else:
			print "That is not a valid code!"
			return 'dead'
						
		# Expand this battle.
		print "\nYou've made your way into the bridge," 
		print "but the staff here are not too happy."
		print "They immediately assessed you as a threat, "
		print "and they are all walking towards you, slowly encircling you."
		print "You take the neutron bomb out of your pack and place it on the floor."
		print "The staff slowly backs away and start running for the escape pods."
		print "You place the bomb and set the timer. Running out the door, you blast the"
		print "lock, and continue down the Central Corridor to the Escape Pods."
		print "There are staff and Gothons in your way.  You push, shoot, and trip anyone"
		print "standing in your way.  Time is of the essence, you will not go down with"
		print "this burning ship."
		return 'escape_pod'
		
		
class EscapePod(Scene):

	def enter(self):
		print "\nFinally, you find a row of escape pods, 10 in total."
		print "Time is of the essence. If you make a mistake now, you will die."
		print "You must pick one of the escape pods and hope that it works."
		print "The escape pods are labelled, 1-10, which one do you choose?"
		
		x = random.randrange(1, 10)
		tries = 1
		tries_allowed = 2
		pod = False


		while True and tries <= 2:
			tries += 1
			number = raw_input("Enter a number  ")
		
			if x == int(number):
				pod = True
				break
			
			elif x != int(number):	
		
				group = {"You find two Gothons going at it", 
						"Everything is in a language you don't understand",
						"The pod is not functional", "It has no fuel",
						"Gothons are standing guard, just inside the doors"}
		
				number = 1
				list = random.sample(group, number)
				first = list[0]
				print first	
				pod = False
				
			else:
				return 'dead'	
				
		print "This pod seems functional. You hit the button and are thrust out into"
		print "space.  You look back at the ship just as it explodes into a massive"
		print "fireball." 
		return 'finished'		
		
class Map(object):

	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'dead': Dead(),
		'finished': Finished(),
	}	
	
	def __init__(self, start_scene):
		self.start_scene = start_scene
		
	def	next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()																		