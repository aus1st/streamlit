class Exceptions:

    def __init__(self):
        pass

    def handle_exception(self):
        try:
            
            print('Give me two numbers, I will devide them.')
            print('Enter q to quit')

            while True:
                first_number = input('\nFirst number: ')
                if first_number == 'q':
                    break
                second_number = input('Second number: ')
                if second_number == 'q':
                    break
                answer = int(first_number) / int(second_number)
                print(answer)
        except ZeroDivisionError:
            print("You can't divide by zero!")
            return True
        except Exception as e:
            print(e)
            return True
mExcept = Exceptions()
mExcept.handle_exception()