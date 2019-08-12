from ListStack import ListStack

def matchBrackets(bracket_array):
    bracket_stack = ListStack()
    open_per = ['{','(','[','<']
    close_per = ['}',')',']','>']
    for i in range(len(bracket_array)):
        #if the current character is an open bracket add it to the stack
        if (bracket_array[i] in open_per):
            bracket_stack.push(bracket_array[i])
            continue;
        # if we get past the first character and it's still empty we know it's impossible to have a matching bracket
        if bracket_stack.isEmpty():
            return False
        top_bracket = bracket_stack.pop()
        print(top_bracket)
        bracket_found = False
        if (top_bracket == open_per[0]) & (bracket_array[i] == close_per[0]):
            bracket_found == True
        if not bracket_found:
            print('Bracket not found')
            return False
    # if not bracket_stack.isEmpty():
    #     return False
    return True
        

print(matchBrackets(['{','}']))