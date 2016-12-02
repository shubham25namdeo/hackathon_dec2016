def jump(start_pt, end_pt, count):
    if start_pt == end_pt:
        print "Minimum steps required: ", count

    if start_pt > end_pt:
        start_pt -= 1
        count += 1
        jump(start_pt=start_pt, end_pt=end_pt, count=count)

    elif start_pt < end_pt:
        start_pt *= 2
        count += 1
        jump(start_pt=start_pt, end_pt=end_pt, count=count)


def main():
    try:  # Expection handling with try-except-else.
        test_num = int(input("Enter the number(1-10) of test Cases:"))
        if test_num < 1 or test_num > 10:
            raise ValueError  # Raise ValueError as check
        for num in range(test_num):
            start_point = int(input("Enter Starting Point(1-1000): "))
            end_point = int(input("Enter Destination Point(1-1000): "))
            if start_point <= 0 or start_point > 1000 or end_point <= 0 or end_point > 1000:
                raise ValueError   # Raise ValueError as check
            jump(start_point, end_point, count=0)

    except KeyboardInterrupt:
        print "\nCtrl+c Killed this program.\nGood-Bye."

    except ValueError:
        print 'Please provide Numerical value & within Specified Range.\n'
        main()

    except:
        print 'Something went wrong with the Input.\nPlease Retry.\n'
        main()

    else:
        print "\nThank you.\nSee you again."

if __name__ == '__main__':
    main()
