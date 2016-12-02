import math


def travel_exp(lst, exp):  # Function to calculate total expenses.
    for coord_a in lst:
        tmp = {}  # Dictionary to store temporary values.
        for coord_b in lst:
            if coord_a == coord_b:  # To skip 0 distance bug.
                pass
            else:
                tmp[round(math.hypot(coord_a[0]-coord_b[0], coord_a[1]-coord_b[1]), 2)] = [coord_a, coord_b]
                # using math.hypot inbuilt function to calculate distance between two coordinate points.

        exp += min(tmp)  # expense calculation

        # removing minimum distance pair.
        lst.remove(tmp[min(tmp)][0])
        lst.remove(tmp[min(tmp)][1])

        # condition for left pairs in list.
        if lst:
            travel_exp(lst, exp)
        else:
            print "Total Expense is: ", exp  # Total Expense.


def main():
    try:
        num_people = int(input("Enter the Even number(2-16) of People:"))
        if num_people < 2 or num_people > 16 or num_people % 2 != 0:
            raise ValueError   # Raise ValueError as check
        lst = []
        for num in range(num_people):
            x = int(input("Enter X-coordinate(between 1 to 1000) for person-"+str(num+1)+": "))
            y = int(input("Enter Y-coordinate(between 1 to 1000) for person-"+str(num+1)+": "))
            if x <= 0 or x > 1000 or y <= 0 or y > 1000:
                raise ValueError  # Raise ValueError as check
            lst.append([x, y])  # list of lists is appended per person.
        travel_exp(lst=lst, exp=0)  # exp=0 is given to send 0 as initial expense

    except KeyboardInterrupt:
        print "\nCtrl+c Killed this program.\nGood-Bye."

    except ValueError:
        print '\nPlease provide Even Numerical value & within Specified Range.\n'
        main()

    except SyntaxError:
        print '\nUnexpected Input.\nPlease try again.\n'
        main()

    except TypeError:
        print '\nProgrammer Made mistake here.\nDo not Worry he will fix it in next version.\nPlease try again.\n'
        main()

    except:
        print '\nSomething went wrong with the Input.\nPlease Retry.\n'
        main()

    else:  # To execute after main()
        print "\nThank you.\nSee you again."

if __name__ == '__main__':
    main()
