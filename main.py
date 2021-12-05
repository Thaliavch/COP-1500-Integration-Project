"""Thalia Valle Chavez
 The objective of this program is to  help Registered Behavior Technicians
 during a session with a client.
 An RBT needs to employ tools in order to asses behavior, among this tools
 there are graphs, data sheets, a timer and a notepad.
 The goal is to put all this tools in one application so it is easier for the
 technician to complete a task,
 and to provide feedback to the technician after a session.
 Documentation: RBT Essentials Handbook """
import random

y = "Yes"


def print_welcome():
    """ Presentation"""
    print("Welcome")
    name = input("What's your name?")
    print("Hi " + name)
    # A looping structure allows a block of code to be repeated one or more
    # times.
    # A while loop is one of the two looping structures available in Python,
    # and it is usually used when the number of times the function has to run
    # is unknown.
    # Parts of a while loop: Initialization(variable), Condition,
    # Increment(update variable)
    # A sentinel-controlled while loop is a loop that repeats the loop body
    # until the user enters a pre-
    # specified value. In this case, the next while loop is not a
    # sentinel-controlled while loop.


def main_program():
    """ Main program """
    while True:
        try:
            age = int(input("How old are you? ( Enter a whole number )"))
            break
        except:
            print("Please enter a valid number")
    # Conditional operators, also known as relational operators, are used to
    # compare the relationship
    # between two operands. Expressions whose result can only be true or false
    #  are known as Boolean
    # expressions. In this case the next line of coding is checking if the
    # value stored in
    # the variable "age" is less than 18.
    if age < 18:
        print("Sorry, to use our services you need to be eighteen years or"
              " older.")
    else:
        print("Thank you for your interest in using our services.")
        # Determine how much time the RBT will spend doing paper work outside
        # of session and the total of hours working per week.
        # Determine if the RBT currently has a part-time or full-time job
        outwork = input("Are you interested in knowing the average time you"
                        "may spend working outside of session? ( Answer with "
                        "Yes or No )")
        while True:
            # An if else statement is a conditional statement that runs a
            # different set of statements depending on whether an expression
            # is true or false
            # In our next line of code the condition is "outwork == 'Yes'"
            if outwork == "Yes":
                break
            # elif is the Python keyword that represents else if and allows
            # you to test for one of several options.
            # As soon as one of the tests is true, the rest are ignored.
            elif outwork == "No":
                break
            else:
                outwork = input("Please enter \"Yes\" or \"No\"")
        if outwork == y:
            while True:
                try:
                    sessions = int(
                        input("How many sessions do you have per week? ( Enter"
                              " a whole number )"))
                    break
                except:
                    print("Please enter a valid number")

            # numeric operators: *(multiplication), //(floor division),
            # %(modulus),+(addition).
            # numeric operators: **(exponent), -(subtraction), /(division).
            extra_time = 15 * sessions
            extra_hour = int(extra_time // 60)
            extra_minute = int(extra_time % 60)
            # Relational operators or Conditional operator "!=" means "it is
            # not equal to."
            if extra_hour != 1:
                # string operator ","(concatenates a string with an int/float
                # and with other objects like end= and sep=,
                # ex: ("hi", 2) == hi2)
                print("Expect to spend ", extra_hour, "hours and ", end=" ")
            elif extra_hour == 1:
                print("Expect to spend", extra_hour, "hour and ", end=" ")
            if extra_minute != 1:
                print(extra_minute, "minutes each week doing outside "
                                    "paperwork.")
            elif extra_minute == 1:
                print(extra_minute, "minute each week doing outside "
                                    "paperwork.")
            # Asking the total amount of hours working on the client's case
            week = input("Do you want to know about how many hours per week "
                         "you'll be working when including time outside "
                         "session? ( Answer with Yes or No )")
            while True:
                if week == "Yes":
                    break
                elif week == "No":
                    break
                else:
                    week = input("Please enter \"Yes\" or \"No\"")

            if week == y:
                while True:
                    try:
                        time = float(
                            input("How long are your sessions (in minutes)?"))
                        break
                    except:
                        print("Please enter a valid number.")

                total = extra_time + time * sessions
                hours = int(total // 60)
                minutes = int(total % 60)
                print("You are expected to \"work\" ( including time doing "
                      "paperwork ) a total of ", hours,
                      " hours and ", minutes, " minutes.", sep="", end=" ")
                if hours >= 35:
                    print("This means that you are considered to have a "
                          "full-time job.")
                else:
                    print("This means that you are considered to have a"
                          " part-time job.")
        elif outwork != y:
            print("Ok")
        # Reinforcement:
        # ...Pairing...
        print("""Pairing Session Assessment
                Please, answer the next questions with Yes or No """)
        obj1 = input("Did the costumer imitate your movements and vocals?")
        obj2 = input("Did the costumer accept items from you?")
        obj3 = input("Did the costumer approach you?")
        obj4 = input("Did the costumer tolerate talking?")
        obj5 = input("Did the costumer reach for items?")
        obj6 = input("Did the costumer looked at you and followed you?")
        # We can use logical operators to determine logic between conditions
        # (relational expressions).
        # You can use logical operators to create compound conditions. Examples
        # of logical operators are
        # "and", "or", and "not." In the next kind of code the program if
        # saying that it is True
        # if obj1, and obj2, and obj3, and so on are equal to the value stored
        # in the variable "y."
        if (obj1 == y and obj2 == y and obj3 == y and obj4 == y and
                obj5 == y and obj6 == y):
            print("Perfect! This means that your client likes you, and now you"
                  " can spend more time teaching instead of battling bad"
                  "behavior.", end=" ")
        # In this case the program is saying that if obj1, or obj2, or obj3,
        # and so on are
        # equal to the value stored in the variable "y," then the boolean
        # expression is True
        # Relational operators or Conditional operator "==" means "is equal to"
        elif (obj1 == y or obj2 == y or obj3 == y or obj4 == y or obj5 == y
              or obj6 == y):
            print("There is still work to do. \n Remember that is very "
                  "important to gain the trust of the costumers", end="")
            print(" because this allows you to teach them more effectively.")
        else:
            print("You may need to repeat the session. Talk to your BCBA for"
                  " feedback.")
        print("Now let's move on to the \"Preference Assessment!\"")
        # string operators "*"(prints the string an x number of times,
        # ex: "hi"*2 prints the word hi 2 times.)
        # string operator "+"(concatenates two strings,
        # ex: "hi " + "there." == hi there)
        ######################################################################
        # Preference Assessment it is a way to determine what the client wants.
        # Before we can reinforce behavior, we have to identify stimuli(things)
        # that will function as reinforcers
        print("." * 3 + "Preference Assessment" + "." * 3)
        print("." * 3 + "Indirect Preference Assessment" + "." * 3)
        print("Ask the caregiver the next questions, and write down their"
              " answers to later show them to your BCBA.")
        daily_action = input("What did they do today for fun?")
        alone_behavior = input("If left alone in a room what do they do?")
        eat_and_watch = input("What do they like to eat and watch?")

        indirect_preference_assessment_data = [daily_action, alone_behavior,
                                               eat_and_watch]
        print("These are the results from the indirect preference assessment:")
        for indirect in indirect_preference_assessment_data:
            print(indirect)
            print()

        print("Ask the client's caregiver about his/her five favorite toy"
              " or activities, and list them here:")
        obj_i_list = []
        # The Python predefined function - range() - is used to define a series
        # of numbers and can be used
        # in a FOR loop to determine the number of times the loop is executed.
        # In a FOR loop you can include
        # a list of values in place of the range() function;
        # ex: for x in [3,6,9,12,15,18]:
        # A looping structure for which you know the number of times it will
        # execute is known as a count-controlled loop.
        # The str() function converts what is the parentheses ( ) to a String.
        for x in range(1, 5 + 1):
            obj_i = input("Item number " + str(x) + " :")
            obj_i_list.append(obj_i)
        print("This are the results from the indirect preference assessment :",
              obj_i_list)
        print("Now let's go on to the  Direct Preference Assessment:")
        print("After knowing the results from the indirect preference"
              " assessment, pick five more objects to conduct the direct"
              " preference assessment.")
        obj_d_list = []
        count = 1
        while count < 6:
            obj_d = input("Item number " + str(count) + " :")
            obj_d_list.append(obj_d)
            # Short-cut operators provide a concise way of creating assignment
            # statements when the variable
            # on the left-hand side of the assignment statement is also on the
            # right-hand side. The addition
            # short-cut operator (+=) is usually used for incrementing a
            # variable. One example is the next line of code.
            count += 1
        obj_d_list.extend(obj_i_list)
        print("These are your direct preference assessment materials: ")
        for count1 in obj_d_list:
            print("." + count1, end="  ")
        print()
        print("...Starting Direct Preference Assessment...")
        while True:
            try:
                num_objects = int(input("Please enter the number of objects in"
                                        " each round."))
                break
            except:
                print("Please enter a valid number.")
        while True:
            try:
                num_rounds = int(input("Please enter how many rounds."))
                break
            except:
                print("Please enter a valid number.")
        for rounds in range(num_rounds):
            for objects in range(num_objects):
                objects_count = random.choice(obj_d_list)
                print("." + objects_count, end="  ")
            print()

        print()
        print("To be continued" + 3 * ".")
        print(
            "#################################################################"
            "###############################################\n")


def extra():
    """ This code is to use some numeric operators that I did not have the
    # chance to use in this program because it is not needed, (Sprint #1) """

    """In January a factory starts building a total of "x" chairs per week, but
     the production of chairs starts doubling in size each month,
    Q1-How many chairs will the factory produce on December of that same year?
    Q2-If the factory donates "y" chairs on December, how many chairs
    will be left to sell? Q3-If each chair is sold for "w" dollars, but half of
    the money is reinvested in production cost, what was the profit of the
    business in January (note: In January all chairs produced were sold)?"""
    print("Bonus code #0.\n")


# ####################################################################

# A function is a segment of code that performs a single task.
# A function definition is the segment of code that tells the program what to
# do when the function is
# executed. The first line of a function definition is known as the function
# header
# The Python keyword "def" indicates that a code segment is a function
# definition.
# The variable in the function call is known as an argument. The variable
# in the function definition is called a parameter.
# Functions that do not send back information are known as void functions.
# Functions often send back or return a result and are known
# as value returning functions.


def q1_chair(x):  # function definition of a value returning function with a
    # Calculating how many chairs the factory produced on December
    """
    :param x:
    :return:
    """
    # parameter.
    q1 = (x * 4) * 2 ** 12
    return q1


def q2_chair(x, z):
    # Calculating how many chairs are left after the donation ( z )
    """
    :param x:
    :param z:
    :return:
    """
    q2 = ((x * 4) * 2 ** 12) - z
    return q2


def q3_chair(x, w):
    # Calculating the profit in January
    """
    :param x:
    :param w:
    :return:
    """
    q3 = x * 4 * w / 2
    return q3


def chair_factory():  # function definition of a void function.
    """ function definition of a void function."""
    print("Please answer the next questions with whole numbers.")
    while True:
        try:
            x = int(
                input("How many chairs per week did the factory produce"
                      " in January?"))
            break
        except:
            print("Please enter a valid number.")
    while True:
        try:
            z = int(input(
                "How many chairs did the factory donate on December of that "
                "same year?"))
            break
        except:
            print("Please enter a valid number.")
    while True:
        try:
            w = int(input("How much does a chair cost?"))
            break
        except:
            print("Please enter a valid number.")
    # In the next code we going to call the function "q1_chair(x),"
    # in this case "x" is an argument.
    print("On December of the first year the factory will produce",
          q1_chair(x), "chairs.")
    # The function 'format' is used to format the output of an number.
    # In case of ".2f" is telling the computer to format the number to
    # have 2 decimal places, in the cas of "7d" the computer is formatting the
    # number to have a total length of 7 digits, including the decimal places.
    print("After donating " + str(z) + " chairs on December, the factory" 
          " has", format(q2_chair(x, z), "7d"),
          " chairs left to sell.", sep="")
    print("In January the business had a profit of $",
          format(q3_chair(x, w), ".2f"), ".", sep="")
    print()


def extra1():
    """Extra program"""
    # Bonus code #1
    print("Bonus code #1.")

    n = 3
    h = 5
    b = n > h
    if b is not True:  # Logical operator "not."
        print("False")
    elif b is True:
        print("True")


def main():
    """ Call to main """
    print_welcome()
    main_program()
    extra()
    chair_factory()
    extra1()


main()
