while True:
    
    print("Which option would you like to perform: \n1. Calculator \n2. List \n3. Phrase \n4. Stop ")
    
    option = input()


    if option == '1':
        def Addition(a, b):
            add_calculation = a + b
            return add_calculation
        def Subtraction(a, b):
            sub_calculation = a - b
            return sub_calculation
        def Multiplication(a, b):
            mult_calculation = a * b
            return mult_calculation
        def Division(a, b):
            try:
                div_calculation = a / b
            except ZeroDivisionError:
                print("Error")
                div_calculation = None
                return div_calculation
                
        while True:
            
            print("What would you like to calculate: \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit ")
            
            calc_operation = input()
            
            if calc_operation == '1':
                add_num1 = eval(input("Choose the first number: "))
                add_num2 = eval(input("Choose the second number: "))
                result = Addition(add_num1, add_num2)
                print(result)
            elif calc_operation == '2':
                sub_num1 = eval(input("Choose the first number: "))
                sub_num2 = eval(input("Choose the second number: "))
                result = Subtraction(sub_num1, sub_num2)
                print(result)
            elif calc_operation == '3':
                mult_num1 = eval(input("Choose the first number: "))
                mult_num2 = eval(input("Choose the second number: "))
                result = Multiplication(mult_num1, mult_num2)
                print(result)
            elif calc_operation == '4':
                div_num1 = eval(input("Choose the first number: "))
                div_num2 = eval(input("Choose the second number: "))
                result = Division(div_num1, div_num2)
                if result is not None:
                    print(result)
                else:
                    print("You cannot divide with the number Zero")
            elif calc_operation == '5':
                break
            else:
                print("Invalid Choice.")

    elif option == '2':
        
        list = ['String', 'Int', 'Float']
        print(list)
        while True:
            #print(list)
            
            print("1. Add to the list \n2. Subtract from the list \n3. Exit ")
            
            list_operation = input()
            
            if list_operation == '1':
                list_add = input("What would you like to add to the list: ")
                new_list = list.append(list_add)
                print(list)
                
                
            elif list_operation == '2':
                list_subtract = input("What would you like to subtract from the list: ")
                if list_subtract not in list:
                    print("That is not on the list.")
                else:
                    list.remove(list_subtract)
                    print(list)
            elif list_operation == '3':
                break
            else:
                print("Invalid Option.")
                
    elif option == '3':
        
        print("Hey, this is a test code that compiles all the major programs I have done so far.")
        while True:
            def only_count(a):
                count = len(a)
                return count
            
            phrase = str("Hey, this is a test code that compiles all the major programs I have done so far.")
            
            print("""\nChoose what you would like to do:
                  \n1. Find out how many letters there are.\n2. Find out how many characters there are.\n3. Make everything uppercase.\n4. Make everything lowercase.\n5. Nevermind. """)
            phrase_operation = input()
            
            if phrase_operation == '1':
                only_letters = [char for char in phrase if char.isalpha()]
                Count = only_count(only_letters)
                print(Count)
            elif phrase_operation == '2':
                only_characters = sum(1 for char in phrase if not char.isalpha())
                print(only_characters)
            elif phrase_operation == '3':
                uppercase_phrase = phrase.upper()
                print(uppercase_phrase)
            elif phrase_operation == '4':
                lowercase_phrase = phrase.lower()
                print(lowercase_phrase)
            elif phrase_operation == '5':
                break
            else:
                print("Invalid Option")          
                
    elif option == '4':
        print("Thank you for using the program, have a great day.")
        break
    else:
        print("Invalid Option.")