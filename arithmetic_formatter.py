
problem = (["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])


def arithmetic_formatter(problem, args):

    if len(problem) > 5: 
        return "Error: Too many problems."

    #this represents the end all - turning it into a list or array format
    arranged_problems = []
       
    #We have to split each string so that we cann access each operand 
    for numbers in problem:
        numbers = numbers.split() 

        if numbers[1] not in '-+':
            return "Error: Operator must be '+' or '-'."
      
      #if length of either number in equation is greater than 4 than error
        if len(numbers[0]) > 4 or len(numbers[2]) > 4:
              return "Error: Numbers cannot be more than four digits."

        #this is taking the index 0 (first number) and index 2 (second) and making them into integars
        try:
            numbersOne = int(numbers[0])
            numbersTwo = int(numbers[2])
        #this solves the error in case the user puts something other than a possible integar
        except ValueError:
            return "Error: Numbers must only contain digits."

        #this section allows us to format the '-' and operator with the longest number in equation
        longest_val = max(len(numbers[0]), len(numbers[2]))
        #width is the longest val (such as 4) + 2 more spaces
        width = longest_val + 2   

        first = f"{numbers[0]:>{width}}" #fist line with first number
        second = numbers[1] + f"{numbers[2]:>{width-1}}" #second line which is operator + second number
        d = '-' * width  #this simply ensuring that our seperator is always with the width
        
        try:
            arranged_problems[0] += (' ' * 4) + first
        except IndexError:
            arranged_problems.append(first)

        try:
            arranged_problems[1] += (' ' * 4) + second
        except IndexError:
            arranged_problems.append(second)

        try:
            arranged_problems[2] += (' ' * 4) + d
        except IndexError:   
            arranged_problems.append(d)


        if args:
            if numbers[1] == '+':
                a = str(int(numbersOne) + int(numbersTwo))
            if numbers[1] == '-':
                a = str(int(numbersOne) - int(numbersTwo))
        
            answer = f"{a:>{width}}"
            try:
                arranged_problems[3] += (' ' * 4) + answer
            except IndexError:
                arranged_problems.append(answer)
      

    output = f"{arranged_problems[0]}\n{arranged_problems[1]}\n{arranged_problems[2]}"
    output = output + f"\n{arranged_problems[3]}" 
    
    return output
                            

print (arithmetic_formatter(problem,True))

