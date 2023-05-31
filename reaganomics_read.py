with open('reaganomics.txt') as file:
    with open('new_file.txt', 'w') as new_file:
        for line in file:
            if 'Federal income tax and payroll tax levels' in line:
                break
            else:
                new_file.write(line)