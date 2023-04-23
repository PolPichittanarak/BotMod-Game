import random 
import time
import os
import sys
from time import sleep

class Coordinates:
	def __init__(self):
		self.x = 0
		self.y = 0



PW_unit = 175
Width, Height = 10, 10
robot = Coordinates()
robot.x = 0
robot.y = 0



def Typing_effect(text):
	for char in text:
		sleep(0.03)
		print(char, end='', flush=True)
	print()


def menu():
	print("""WELCOME! to Botmod
your terrain is 10x10 

Directions allowed include:
Left = 'A'
Right = 'D'
Up = 'W'
Down = 'S'
""")

	print("to begin the game, press e to enter your garage...")
	keyentered = ""
	while keyentered != "e":
		keyentered = input()
	robot_opt = robot_option()
	return robot_opt



def robot_option():
	robot_opt = []
	garage_menu = """
welcome to your garage, here you can modify your robot that it suits the best for your terrain

Here are some information about the Traction:
"""
	Typing_effect(garage_menu)
	print("""
Traction  | Moving on       | Moving on     | Moving on     |
type      | grassland:      | rocks:        | ice :         |
-------------------------------------------------------------
wheels    | 1 PU consumed   | 2 PU consumed | 3 PU consumed |
------------------------------------------------------------- 
tracks    | 3 PU consumed   | 1 PU consumed | 2 PU consumed |
-------------------------------------------------------------
skis      | 2 PU consumed   | 3 PU consumed | 1 PU consumed |
-------------------------------------------------------------

""")
	script2 = "moving on each terrain type consumed different amount of energy regarding the traction type shown above"
	Typing_effect(script2)
	traction = ""
	while traction.lower() not in ['wheels', 'tracks', 'skis']:
		traction = input("which traction type do you prefer : ")
	robot_opt.append(traction)

	script3= "\nnow, you can also customize the size of your robot. Larger robot can carry more passengers but of course will consume more power \nHere are some information about the size of the robot:"
	Typing_effect(script3)
	print("""
Passenger    | Maximum          | EXTRA PU      |
bay size     | no. of passengers| consumed:     |
-------------------------------------------------
large        |      3           |     2         |
-------------------------------------------------
medium       |      2           |     1         |
-------------------------------------------------
small        |      1           |     0         |
-------------------------------------------------""")
	size = ""
	while size.lower() not in ['large', 'medium', 'small']:
		size = input("which passenger bay size do you prefer : ")
	robot_opt.append(size)
	return robot_opt



#put parameters in a list
def PowerUnit(Terrain, traction, robot, size):
	TractionPw = CurrentTerPW(Terrain, robot, traction)
	if size == "large":
		SizePw = 2
	elif size == "medium":
		SizePw = 1
	elif size == "small":
		SizePw = 0

	Total_Pw = TractionPw + SizePw
	return Total_Pw

def CurrentTerPW(Terrain, robot, traction):
	PowerCon = 0
	for y, row in enumerate(Terrain):
		for x, cell in enumerate(row):
			if y == robot.x and x == robot.y:
				#print("Current cell is {}".format(cell))
				currentcell = cell
	if (traction == "wheels" and currentcell == "g") or  (traction == "tracks" and currentcell == "r") or (traction == "skis" and currentcell == "i"):
		PowerCon = 1
	elif (traction == "wheels" and currentcell == "r") or  (traction == "tracks" and currentcell == "i") or (traction == "skis" and currentcell == "g"):
		PowerCon = 2
	elif (traction == "wheels" and currentcell == "i") or  (traction == "tracks" and currentcell == "g") or (traction == "skis" and currentcell == "r"):
		PowerCon = 3
	return PowerCon

def Pla_direction(Pla_input, robot):
	Init_x, Init_y = robot.x, robot.y
	if Pla_input == "D":
		robot.y += 1
	elif Pla_input == "A":
		robot.y -= 1
	elif Pla_input == "W":
		robot.x -= 1
	elif Pla_input == "S":
		robot.x += 1
	if robot.x < 0 or robot.x > Width - 1 or robot.y < 0 or robot.y > Height - 1:
		print("Invalid move - you are exceeding the grid")
		robot.x, robot.y = Init_x, Init_y
	return robot


def Terrain_Grid():
	Terrain = []
	terrains = ["g", "r", "i"]
	for y in range(Height):
		Row = []
		for x in range(Width):
			Random_Ter = random.randint(0,2)
			Row.append(terrains[Random_Ter])
		Terrain.append(Row)
	for i in range(10):
		playerx, playery = random.randint(0, Width-1), random.randint(0,Height-1)
		Terrain[playery][playerx] = "P"

	campsite_x, campsite_y = random.randint(0, Width-1), random.randint(0,Height-1)
	Terrain[campsite_y][campsite_x] = "*"
	return Terrain


def CheckPassCollect(terrain, robot):
	indexX, indexY = robot.x, robot.y
	indices = [indexX, indexY]
	return indices


P_coors = []

def PassLocations(Terrain):
	Per_coor = []
	for indexY, row in enumerate(Terrain):
		for indexX, cell in enumerate(row):
			if cell == "P":
				Per_coor = [indexY, indexX]
				P_coors.append(Per_coor)
			

def PassCheck(Terrain, robot):
	indices = CheckPassCollect(Terrain,robot)
	for person in P_coors:
		 if person[0] == indices[0] and person[1] == indices[1]:
			 print("Passenger Found")
			 return True


def CollectPass(Terrain, robot):
	indexX, indexY = robot.x, robot.y
	terrains = ["g", "r", "i"]
	Random_Ter = random.randint(0,2)
	Terrain[indexY][indexX] = terrains[Random_Ter]
	return Terrain


def Display_Grid(robot, Terrain):
	print("_ " * 18)
	terrains = ["g", "r", "i"]

	for index_x, row in enumerate(Terrain):
		print("|", end="  ")
		for index_y, cell in enumerate(row):
			
			if index_x == robot.x and index_y == robot.y:
				print("X", end = "  ")
			elif cell == "P":
				print("P", end = "  ")
			elif cell == "*":
				print("*", end = "  ")
			elif cell in terrains:
				print(cell, end = "  ")

		print("|")
		print("|", end="                                ")
		print("|")

	print("_ " * 18)
	


def Passengers(size):
	if size == "large":
		seat_count = 3
	elif size == "medium":
		seat_count = 2
	elif size == "small":
		seat_count = 1
	return seat_count

def Display_seats(current_passnum, seat_count, collect):

	Passenger_seats = []
	ret_list = []
	for seat in range(seat_count):
		Passenger_seats.append(".")

	if collect:
		if current_passnum > seat_count:
			print("No seat available")
			current_passnum -= 1
			ret_list.append(current_passnum)
			ret_list.append(False)
		else:
			ret_list.append(current_passnum)
			ret_list.append(True)
	else:
		ret_list.append(current_passnum)
		ret_list.append(False)
	for seatocc in range(current_passnum):
				Passenger_seats[seatocc] = "P"
	print(Passenger_seats)
	return ret_list
	
	
def ResetCell(Set_Grid, robot):
	terrains = ["g", "r", "i"]
	Random_Ter = random.randint(0,2)
	Set_Grid[robot.x][robot.y] = terrains[Random_Ter]
	return Set_Grid

def Checkcamp(Terrain, robot):
	for y, row in enumerate(Terrain):
		for x, cell in enumerate(row):
			if y == robot.x and x == robot.y:
				#print("Current cell is {}".format(cell))
				currentcell = cell
	if currentcell == "*":
		return True
	else:
		return False

def Check_All_Pass(Terrain):
	for row in Terrain:
		for cell in row:
			if cell == "P":
				return False
		
	return True

##############Program begins here########################
robot_opt = menu()
traction_type, robot_size = robot_opt[0], robot_opt[1]

time.sleep(1.0)
os.system("clear")
print("\nyour robot traction type is {} and has {} passenger bay #size".format(robot_opt[0], robot_opt[1]))
print("Here is your terrain")
print("Your robot begins at (0,0)")


Set_Grid = Terrain_Grid()
Display_Grid(robot, Set_Grid)
RobotPos = robot
PassLocations(Set_Grid)
current_pass = 0
Total_Pass = 0
#Passengers(robot_size) 
All_Pass_coll = False


while PW_unit > 0 and All_Pass_coll == False:
	
	PlayerMove = ""
	while PlayerMove not in ['D','S','A','W']:
		PlayerMove = input("Which direction? \n").upper().strip()
	else:
		os.system("clear")
		RobotPos = Pla_direction(PlayerMove, robot)
		Display_Grid(RobotPos, Set_Grid)
		size = Passengers(robot_size)
		PassFound = PassCheck(Set_Grid, robot)
		if PassFound:
			#CollectPass(Set_Grid, robot)
			current_pass += 1
		ret_list = Display_seats(current_pass, size, PassFound)
		#ret_list returns [passnum, boolean check]
		current_pass = ret_list[0]
		if ret_list[1]:
			Set_Grid = ResetCell(Set_Grid, robot)
		if Checkcamp(Set_Grid, robot):
			Total_Pass += current_pass
			current_pass = 0
			Display_seats(current_pass, size, PassFound)
		print("PASSENGERS AT THE CAMP: {}".format(Total_Pass))
		print()
		PowerCon = PowerUnit(Set_Grid, traction_type, robot, robot_size)
		PW_unit -= PowerCon
		print("{} units consumed".format(PowerCon))
		print()
		print("Power Units remaining : {}".format(PW_unit))

		All_Pass_coll = Check_All_Pass(Set_Grid)
		if All_Pass_coll:
			break
if Check_All_Pass(Set_Grid):
	print("YOU WIN")
if PW_unit <= 0:
	print("YOU LOSE")





###############Program ends here########################




# returning to the menu after finished


