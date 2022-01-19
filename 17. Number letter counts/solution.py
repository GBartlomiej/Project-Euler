numbers = {1 : "one",
           2 : "two",
           3 : "three",
           4 : "four",
           5 : "five",
           6 : "six",
           7 : "seven",
           8 : "eight",
           9 : "nine",
           10 : "ten",
           11 : "eleven",
           12 : "twelve",
           13 : "thirteen",
           14 : "fourteen",
           15 : "fifteen",
           16 : "sixteen",
           17 : "seventeen",
           18 : "eighteen",
           19 : "nineteen",
           20 : "twenty",
           30 : "thirty",
           40 : "forty",
           50 : "fifty",
           60 : "sixty",
           70 : "seventy",
           80 : "eighty",
           90 : "ninety",
           1000: "one thousand"}

def prepare_string(n : int):
    as_str = str(n)
    length=len(as_str)
    if n in numbers.keys():
        return numbers[n]
    elif length<3:
        return numbers[int(as_str[0]+"0")] +"-"+ numbers[int(as_str[1])]
    elif as_str[1:]=="00":
        return numbers[int(as_str[0])]+" hundred"
    elif int(as_str[1:]) in numbers.keys():
        return numbers[int(as_str[0])]+" hundred and "+numbers[int(as_str[1:])]
    else:
        return numbers[int(as_str[0])]+" hundred and "+ numbers[int(as_str[1]+"0")] +"-"+numbers[int(as_str[2])]

print(sum(len(prepare_string(i).replace(" ", "").replace("-", "")) for i in range(1, 1001)))
