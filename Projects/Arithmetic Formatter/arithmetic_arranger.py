def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    first_line = ""
    second_line = ""
    dash_line = ""
    answer_line = ""

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator != "+" and operator != "-":
            return "Error: Operator must be '+' or '-'."

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        width = max(len(num1), len(num2)) + 2

        first_line += num1.rjust(width) + "    "
        second_line += operator + " " + num2.rjust(width - 2) + "    "
        dash_line += "-" * width + "    "

        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line += answer.rjust(width) + "    "

    arranged_problems += first_line.rstrip() + "\n"
    arranged_problems += second_line.rstrip() + "\n"
    arranged_problems += dash_line.rstrip()
    
    if show_answers:
        arranged_problems += "\n" + answer_line.rstrip()

    return arranged_problems


