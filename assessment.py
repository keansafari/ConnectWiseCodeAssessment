# Comments: The test did not specify what to do if:
# Name, city, and flags are left blank so I ERRORED out when the
# input file does not contain those 3 fields.

# Ex: (Name)Ally Jones
# (Age)25
# (City)
# (Flags)YYY
#
# this returns with Invalid data, unable to process because city was not given

from Person import Person

input = """(Name)John Doe
(Age)20
(City)Ashtabula, OH
(Flags)NYN

(Name)Jane Doe
(Flags)YNY
(City)N Kingsville, OH

(Name)Sally Jones
(Age)25
(City)Paris
(Flags)YYY"""

inputFile = open("./SampleInputFile.txt", "r")
input2 = inputFile.read()
inputFile.close()

def parseInput(input):
    inputSplit = input.split('\n\n')
    for p in inputSplit:
        name = age = city = flags = state = gender = employee = student = employee = ''
        createPerson = True
        pSplit = p.split('\n')
        for line in pSplit:
            #skip through whitespace lines
            if line == '':
                createPerson = False
                continue
            else:
                createPerson = True
                if line.find('(Name)') != -1:
                    name = line.split('(Name)')[1]
                elif line.find('(Age)') != -1:
                    age = line.split('(Age)')[1]
                elif line.find('City') != -1:
                    city = line.split('(City)')[1]
                    if city.find(',') != -1:
                        location = city.split(', ')
                        city = location[0]
                        state = location[1]
                    else:
                        state = 'N/A'
                elif line.find('(Flags)') != -1:
                    flags = line.split('(Flags)')[1]
                    if len(flags) > 0:
                        if flags[0] == 'Y':
                            gender = 'Female'
                        else:
                            gender = 'Male'
                        if flags[1] == 'Y':
                            student = 'Yes'
                        else:
                            student = 'No'
                        if flags[2] == 'Y':
                            employee = 'Yes'
                        else:
                            employee = 'No'

        if createPerson:
            person = Person(name, age, gender, city, state, student, employee)
            print(person.GetPerson())

parseInput(input)
parseInput(input2)

