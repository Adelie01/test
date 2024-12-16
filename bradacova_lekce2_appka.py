try:
    weight = float (input("Kolik važíš?"))
except ValueError:
    weight = float(input("Zadejte číslo"))
bmr = weight*24.2
activityfactor=2
cml=bmr*activityfactor
cmlrounded= round(cml, 1)
print(f"Tvůj denní výdej je {cmlrounded} kcal za den.")