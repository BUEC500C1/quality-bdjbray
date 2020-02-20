def convert_to_roman(n):
    if not isinstance(n, int):
        return 'Please enter number'
    if n < 1 or n > 3999:
        return 'number out of range (must be between 1 and 4000)'
        
    thedict = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
    
    if n in thedict:
        return thedict[n]
        
    length = len(str(n))
    roman_num = ''
    for i in str(n):
        if length == 0:
            break
        dig_num = pow(10, length - 1)
        if int(i) in thedict:
            roman_num += thedict[dig_num * int(i)]
        elif int(i) < 4:
            roman_num += thedict[dig_num] * int(i)
        elif (int(i) == 4) or (int(i) == 9):
            roman_num += thedict[dig_num] + thedict[dig_num * (int(i) + 1)]
        elif int(i) > 5:
            roman_num += thedict[dig_num * 5] + (thedict[dig_num] * (int(i) - 5))
        length -= 1
    
    return roman_num
    
    

    




