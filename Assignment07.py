#------------------------------------------------#
#Title: Demo of Exception Handling and Pickling
#Description: exploring pickling and execption handling
#Course: IT FDN 110 A
#Kristina Binder, 3.3.2023, created script
#------------------------------------------------#

#declaring variables
Table = []
n_table = []
done = False

#present menu of options for the user
while (not done):
    print('')
    print('Demo Options')
    print('1. exception handling examples')
    print('2. pickling data example')
    print('3. combining pickling and exception handling')
    print('Please enter any other number to exit the program'+ '\n')
    choice = input('which demo would you like to see? ')
    print('')
    choice = int(choice)

    if choice == 1:
        # exception handling using try/except
        N1 = input('Please enter a number: ')
        N1 = int(N1)
        N2 = input('Please enter another number: ')
        N2 = int(N2)
        try:
            divid = N1/N2
            divid = str(divid)
            print(divid)
        except:
            print('Please make the second number not zero')

        #custom exceptions
        class NotMyAge(Exception):
            pass

        age = 21
        guess = input('please enter a guess for my age: ')
        guess = int(guess)
        try:
            if guess == age:
                print('you are correct!')
            else:
                raise NotMyAge
        except NotMyAge:
            print('incorrect guess')

    #pickling demonstration
    elif choice == 2:
        #collect data
        candy = input('please enter a candy: ')
        fav = input('is it your favorite (yes/no)? ')
        dicRow = {'candy':candy, 'favorite':fav}
        Table.append(dicRow)

        #saving data into file
        import pickle
        file = open('Demo.txt', 'wb')
        pickle.dump(Table, file)
        file.close()
        print('data saved to file!')

        #unpickling data from file
        import pickle
        print('this is the data from the file')
        with open('Demo.txt', 'rb') as file:
            open = pickle.load(file)
        print(open)
    elif choice == 3:
        class WrongNumber(Exception):
            pass

        anumber = 4
        print('thinking of a number between one and ten')
        number = input('please take a guess: ')
        number = int(number)
        import pickle

        exit = False
        while(not exit):
            try:
                if number == anumber:
                    print('congrats you are correct')
                    attempts = input('How many attempts did it take to guess the number: ')
                    f = open('DemoTwo.txt', 'wb')
                    pickle.dump(attempts, f)
                    f.close()
                    exit = True
                else:
                    raise WrongNumber
            except WrongNumber:
                print('sorry incorrect guess')
                exit = True
        attempt = input('would you like to see how many attempts it took previously? (yes/no) ')
        if attempt == 'yes':
            import pickle
            print('Number of attempts: ')
            with open('DemoTwo.txt', 'rb') as f:
                open = pickle.load(f)
            print(open)
        else:
            print('Try again soon!')
    else:
        print('Goodbye!')
        done = True



