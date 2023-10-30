import pyautogui as PAG
import random
import os
import json

points = 0

file_path = 'C:/Users/annem/source/repos/PythonDoesSlimstampen/dic.txt'
if os.path.exists(file_path):
    # Open the file and load the dictionary
    with open(file_path, 'r') as f:
        dictionary = json.load(f)
    print(dictionary)
else:
    print(f"The file {file_path} does not exist.")

def Start():
	global points
	#choose what you wanna do
	ask = PAG.confirm(text='', title='', buttons=['new dictionary', 'new word', 'view dictionary', 'delete', 'test', 'cancel'])
	if ask == 'new dictionary':
		NewDictionary(dictionary)
	elif ask == 'new word':
		NewWord(dictionary)
	elif ask == 'view dictionary':
		View()
	elif ask == 'delete':
		Delete()
	elif ask == 'cancel':
		with open(file_path, 'w') as f:
			json.dump(dictionary, f, indent=4)
		exit()
	elif ask == 'test':
		Test()

def NewDictionary(dictionary):
	#makes a new dictionary
	text = PAG.prompt(text='text', title='', default='')
	if text != '':
		dictionary[text] = {}
	Start()

def NewWord(dictionary):
	#selects a deictionary and makes a new word in that dictionary
	ask = PAG.confirm(text='select a dictionary', title='select', buttons=[key for key in dictionary.keys()])
	text = PAG.prompt(text='word 1', title='', default='')
	text2 = PAG.prompt(text='word 2', title='', default='')
	if text and text2 != '':
		dictionary[ask][text] = text2
	Start()


def View():
	#selects a dictionary to view the contents of
	ask = PAG.confirm(text='select a dictionary', title='select', buttons=[key for key in dictionary.keys()])
	PAG.alert(text=dictionary[ask], title='', button='OK')
	Start()

def Delete():
	ask = PAG.confirm(text='what do you want to delete?', title='select', buttons=['word', 'dictionary', 'cancel'])
	if ask == 'word':
		askDict = PAG.confirm(text='select a dictionary', title='select', buttons=[key for key in dictionary.keys()])
		for k,v in dictionary[askDict].items():
			print(f"{k}:{v}")
		print("what wordset would you like to delete ")
		delet = input("")
		print("")
		if delet in dictionary[askDict]:
			del dictionary[askDict][delet]
			print(dictionary)
			print("done")
			print("")
		else:
			print('that aint real')
	Start()

def Test():
	global points
	correct = 0
	#make this select a dictionary and then select a random word from the dictionary
	ask = PAG.confirm(text='select a dictionary', title='select', buttons=[key for key in dictionary.keys()])
	times = PAG.prompt(text='how many times do you wanna get a word', title='', default='')
	if times.isdigit():
		for i in range(int(times)):
			randomWord = random.choice(list(dictionary[ask].keys()))
			#promt with this word and check if it is the correct translation of the word if yes give a point if no take away a point
			promt = PAG.prompt(text=randomWord, title='give the translation of this word', default='')
			if str(promt) == str(dictionary[ask][randomWord]):
				correct += 1
			#also maybe do it like if you give the correct answer you dont get that word anymore
		PAG.alert(text='you got: ' + str(correct) + '/' + str(times) + ' correct', title='')
	Start()

Start()