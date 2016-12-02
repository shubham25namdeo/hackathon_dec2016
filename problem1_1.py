import re


def count_occurs(word_given, string_val):
    count = 0
    for found in re.finditer(word_given, string_val):
        count += 1
    if count > 0:
        print "A). Word: '"+word_given+"' occurred "+str(count)+" times."
        string_val = re.sub(word_given, "", string_val)
        print "B). String after removal of "+word_given+": "+string_val
        print "C). Word appended into string equal to number of occurrences:\n "+string_val+((" "+word_given)*count)
    else:
        print word_given+" does not exist in "+string_val


def main():
    try:
        word_given = raw_input("Enter Word: ")
        string_val = raw_input("Enter String: ")
        if len(word_given) < 1 or len(string_val) < 1:
            print "nothing to check"
        count_occurs(word_given=word_given, string_val=string_val.lower())

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
