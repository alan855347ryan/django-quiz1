from django.shortcuts import render
import csv
import time
from random import randint

# set the lenght of questions to be asked
global quiz_lenght
quiz_lenght = 10


# initlize code and set variables to begin
global i
global color
global correct_color
correct_color = "success"
global no_of_questions
global no_of_jquestions
global score_answer
global current_question
global answer_a
global answer_b
global answer_c
global sq_questions
global sq_jquestions
global choice
global last_question_no

#Get the questions from the file
load_questions_gk = 'generalknowledge3.txt'
load_questions_jgk = 'juniorgeneralknowledge3.txt'

# open the file  and place questions,options and answers into a list called sq_questions



def home(request):
	#use the global counter variable not local
	global counter_variable
	counter_variable = 0
	#use the global score tracker variable not local and reset to zero
	global score_answer
	score_answer = 0
	# Make the list of questions available everywhere.
	global sq_questions
	# load the questions from file for general knowledge Quiz.
	sq_questions=[]
	# try this code
	with open(load_questions_gk, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			sq_questions.append(row)

    #Replaced code
	#f = open(load_questions_gk,"r")
	#reader = csv.reader(f)
	#for row in reader:
		#sq_questions.append(row)

	csv_file.close
	global no_of_questions
	no_of_questions = len(sq_questions)

	# load the questions from file for  juniorgeneral knowledge Quiz.
	global sq_jquestions
	sq_jquestions=[]
	with open(load_questions_jgk, mode='r') as csv_file:
		csv_reader = csv.DictReader(csv_file)
		for row in csv_reader:
			sq_questions.append(row)
	csv_file.close

	#f = open(load_questions_jgk,"r")
	#reader = csv.reader(f)
	#for row in reader:
	#	sq_jquestions.append(row)
	
	global no_of_jquestions
	no_of_jquestions = len(sq_jquestions)

	# Code to check responce from  retake  quizbuttons at end of quiz for generalknowledge or junior GK
	retake = request.POST.get('repeat')
	retake2 = request.POST.get('repeat2')
	if retake == "":
		counter_variable=counter_variable + 1
		current_question=sq_questions[i][0]
		answer_a = sq_questions[i][1]
		answer_b = sq_questions[i][2]
		answer_c = sq_questions[i][3]

		args = {'current_question':current_question,
				'answer_a':answer_a,
				'answer_b':answer_b,
				'answer_c':answer_c,
				'counter_variable':counter_variable,
				'quiz_lenght':quiz_lenght,
				} 

		return render(request, 'generalknowledge.html', args)


	elif retake2 == "":
		counter_variable=counter_variable + 1
		current_question=sq_jquestions[i][0]
		answer_a = sq_jquestions[i][1]
		answer_b = sq_jquestions[i][2]
		answer_c = sq_jquestions[i][3]

		args = {'current_question':current_question,
				'answer_a':answer_a,
				'answer_b':answer_b,
				'answer_c':answer_c,
				'counter_variable':counter_variable,
				'quiz_lenght':quiz_lenght,
				} 

		return render(request, 'history.html', args)
	
	# if retake the quiz is not selected return to the home page
	return render(request, 'home.html', {})
	
def results(request):
	pass


def results2(request):
	pass


def generalknowledge(request):
	#Action to be carried out when selection is made
	if request.method == "POST":
		# store the number of the last question in a variable
		global i
		global sq_questions
		global no_of_questions
		global last_question_no
		#i = last_question_no
		last_question_no = i

		a = request.POST.get('a')
		b = request.POST.get('b')
		c = request.POST.get('c')
		old_question = sq_questions[last_question_no][0]
		old_answer_a = sq_questions[last_question_no][1]
		old_answer_b = sq_questions[last_question_no][2]
		old_answer_c = sq_questions[last_question_no][3]
		old_correct_answer = sq_questions[last_question_no][4]
		#testing pop
		sq_questions.pop(last_question_no)
		no_of_questions = len(sq_questions)



		# change i to load new question
		i = randint(0,no_of_questions - 1)
	
		
		# check is the quiz over and carry out actions for options
		global counter_variable
		global score_answer
		if quiz_lenght > counter_variable:
			counter_variable = counter_variable + 1
			current_question=sq_questions[i][0]
			answer_a = sq_questions[i][1]
			answer_b = sq_questions[i][2]
			answer_c = sq_questions[i][3]


			if a == "":
				if old_answer_a == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_a + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif b == "":
				if old_answer_b == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_b + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif c == "":
				if old_answer_c == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_c + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question

			args = {'sq_questions':sq_questions,
					'no_of_questions':no_of_questions,
					'last_question_no': last_question_no,
					'color':color,
					'choice':choice,
					'current_question':current_question,
					'answer_a':answer_a,
					'answer_b':answer_b,
					'answer_c':answer_c,
					'counter_variable':counter_variable,
					'i':i,
					'quiz_lenght':quiz_lenght,
					}
			return render(request,'generalknowledge.html',args)

		#Action to be carried out when last question is asked.
		else:
			#reset counter as quiz finished.
			counter_variable = 0
			# Comprare the answer given to the correct one and display the results page.
			if a == "":
				if old_answer_a == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_a + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif b == "":
				if old_answer_b == old_correct_answer:
					color = correct_color
					score_answer = score_answer + 1
					choice = " Correct, " + old_answer_b + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif c == "":
				if old_answer_c == old_correct_answer:
					color = correct_color
					score_answer = score_answer + 1
					choice = " Correct, " + old_answer_c + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			
			# Compare the final score and give apprioate message for display
			# The final Score is also passed to the results page.
			if quiz_lenght == score_answer:
				message="Well Done you Got All The Questions Correct!"
			elif score_answer==0:
				message = " Oops, That Didn't go Well. Keep Trying."
			else:
				message=""

			# Pass info to page and load.
			var_results = {'color':color,
							'choice':choice,
							"message":message,
							"score_answer":score_answer,
							"quiz_lenght":quiz_lenght,
							"counter_variable":counter_variable,
							}
			return render(request, 'results.html',var_results)

	#Acrry out these actions on first load of page.

	# Set Counter Variable (Question x of Quizlenght) to 1 as 1st question to be loaded
	counter_variable = 1

	# Select a random question from the list
	i = randint(0,no_of_questions - 1)
	current_question=sq_questions[i][0]
	answer_a = sq_questions[i][1]
	answer_b = sq_questions[i][2]
	answer_c = sq_questions[i][3]
	
	# Pass info to page for loading and load the page.
	args = {'current_question':current_question,
			'answer_a':answer_a,
			'answer_b':answer_b,
			'answer_c':answer_c,
			'counter_variable':counter_variable,
			'quiz_lenght':quiz_lenght,
			} 

	return render(request, 'generalknowledge.html', args)




def history(request):
	#Action to be carried out when selection is made
	if request.method == "POST":
		# store the number of the last question in a variable
		global i
		global sq_jquestions
		global no_of_jquestions
		global last_question_no
		#i = last_question_no
		last_question_no = i

		a = request.POST.get('a')
		b = request.POST.get('b')
		c = request.POST.get('c')
		old_question = sq_jquestions[last_question_no][0]
		old_answer_a = sq_jquestions[last_question_no][1]
		old_answer_b = sq_jquestions[last_question_no][2]
		old_answer_c = sq_jquestions[last_question_no][3]
		old_correct_answer = sq_jquestions[last_question_no][4]
		#testing pop
		sq_jquestions.pop(last_question_no)
		no_of_jquestions = len(sq_jquestions)



		# change i to load new question
		i = randint(0,no_of_jquestions - 1)
	
		
		# check is the quiz over and carry out actions for options
		global counter_variable
		global score_answer
		if quiz_lenght > counter_variable:
			counter_variable = counter_variable + 1
			current_question=sq_jquestions[i][0]
			answer_a = sq_jquestions[i][1]
			answer_b = sq_jquestions[i][2]
			answer_c = sq_jquestions[i][3]


			if a == "":
				if old_answer_a == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_a + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif b == "":
				if old_answer_b == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_b + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif c == "":
				if old_answer_c == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_c + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question

			args = {'sq_jquestions':sq_jquestions,
					'no_of_jquestions':no_of_jquestions,
					'last_question_no': last_question_no,
					'color':color,
					'choice':choice,
					'current_question':current_question,
					'answer_a':answer_a,
					'answer_b':answer_b,
					'answer_c':answer_c,
					'counter_variable':counter_variable,
					'i':i,
					'quiz_lenght':quiz_lenght,
					}
			return render(request,'history.html',args)

		#Action to be carried out when last question is asked.
		else:
			#reset counter as quiz finished.
			counter_variable = 0
			# Comprare the answer given to the correct one and display the results page.
			if a == "":
				if old_answer_a == old_correct_answer:
					score_answer = score_answer + 1
					color = correct_color
					choice = " Correct, " + old_answer_a + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif b == "":
				if old_answer_b == old_correct_answer:
					color = correct_color
					score_answer = score_answer + 1
					choice = " Correct, " + old_answer_b + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			elif c == "":
				if old_answer_c == old_correct_answer:
					color = correct_color
					score_answer = score_answer + 1
					choice = " Correct, " + old_answer_c + " was the answer to " + old_question
				else:
					color = "danger"
					choice = "Incorrect, " + old_correct_answer + " is the correct answer to " + old_question
			
			# Compare the final score and give apprioate message for display
			# The final Score is also passed to the results page.
			if quiz_lenght == score_answer:
				message="Well Done you Got All The Questions Correct!"
			elif score_answer==0:
				message = " Oops, That Didn't go Well. Keep Trying."
			else:
				message=""

			# Pass info to page and load.
			var_results = {'color':color,
							'choice':choice,
							"message":message,
							"score_answer":score_answer,
							"quiz_lenght":quiz_lenght,
							"counter_variable":counter_variable,
							}
			return render(request, 'results2.html',var_results)

	#Acrry out these actions on first load of page.

	# Set Counter Variable (Question x of Quizlenght) to 1 as 1st question to be loaded
	counter_variable = 1

	# Select a random question from the list
	#global no_of_jquestions
	i = randint(0,no_of_jquestions - 1)
	current_question=sq_jquestions[i][0]
	answer_a = sq_jquestions[i][1]
	answer_b = sq_jquestions[i][2]
	answer_c = sq_jquestions[i][3]
	
	# Pass info to page for loading and load the page.
	args = {'current_question':current_question,
			'answer_a':answer_a,
			'answer_b':answer_b,
			'answer_c':answer_c,
			'counter_variable':counter_variable,
			'quiz_lenght':quiz_lenght,
			} 

	return render(request, 'history.html', args)







def about(request):
	return render(request, 'about.html',{} )

