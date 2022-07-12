#Eric Daily
#Github Username: edaily00
#7/12/2022
#This program opens a file and adds the numbers then writes the sum!

def file_sum(file_name):
#Here is where I wrote the accumulator
    sum = 0
    try:
        with open(file_name, "r") as infile:
            for line in infile:
                sum += float(line)
    except FileNotFoundError:
        print("File not found")



#Here I write the sum as a string to a new file
    with open("sum.txt", "w") as outfile:
        outfile.write(str(sum))

