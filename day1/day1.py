elfWithMostCalories1 = 0
elfWithMostCalories2 = 0
elfWithMostCalories3 = 0
calorieCounterForElf = 0
with open('inputDay1.txt', 'r') as f:
    contents = f.readlines()
    for line in contents:
        if line.strip() != '':
            calorieCounterForElf += int(line)
        else:
            if(calorieCounterForElf > elfWithMostCalories1):
                elfWithMostCalories3 = elfWithMostCalories2
                elfWithMostCalories2 = elfWithMostCalories1
                elfWithMostCalories1 = calorieCounterForElf

            elif(calorieCounterForElf > elfWithMostCalories2):
                elfWithMostCalories3 = elfWithMostCalories2
                elfWithMostCalories2 = calorieCounterForElf
            elif(calorieCounterForElf > elfWithMostCalories3):
                elfWithMostCalories3 = calorieCounterForElf
            calorieCounterForElf=0

print(elfWithMostCalories1 + elfWithMostCalories2 + elfWithMostCalories3)
