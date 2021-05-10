#Провека скобок
string = input()
req_brack = input()
antibrack = ""
open_brackets = ['(','[','{','<']
close_brackets = [')',']','}','>']
brackets = ""
pos_brackets = {}
stack = []
no_error = True
error_brack = None
error_pos = None

for i in req_brack:
    antibrack += close_brackets[open_brackets.index(i)]

for i in range(len(string)):
    if(string[i] in open_brackets or string[i] in close_brackets):
        brackets += string[i]
        pos_brackets[string[i]] = i

for i in brackets:
    if (i in open_brackets and i in req_brack):
        stack.append(i)
    else:
        if (i in close_brackets and stack!=[] and stack[-1]==open_brackets[close_brackets.index(i)] and i in antibrack):
            stack.pop()
        elif (i in antibrack):
            stack.append(i)



if(stack!=[]):
    no_error = False
    for i in stack:
        if(i in close_brackets):
            error_pos = (i, pos_brackets.get(i))
            break
    
    error_brack = (stack[stack.index(error_pos[0])-1], pos_brackets.get(stack[stack.index(error_pos[0])-1]))
    
    

print(no_error,error_pos,error_brack,sep=", ")

            
        


