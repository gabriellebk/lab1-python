# Author: Gabrielle Brunner-King gsb5225@psu.edu    
# Collaborator: Eric Benditt erb5623@psu.edu  
# Collaborator: Bakhtiar Reza erb5623@psu.edu 
# Collaborator: Khalid AlMahmood kfa5270@psu.edu 

temp = input("Enter temperature: ")
unit = input("Enter unit in F/f or C/c: ")
temp = float(temp)
if (unit == "F" or unit == "f"):
  print(f"{temp}° in Fahrenheit is equivalant to {(temp-32)*(5/9)}° Celsius.")
elif (unit == "C" or unit == "c"):
  print(f"{temp}° in Celsius is equivalent to {(temp*1.8)+32}° Fahrenheit.")
else:
  print("Invalid unit(" + unit +"). ")
