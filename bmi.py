# индекс массы тела
mass, height = input().split()
print(round(float(mass.replace(",", "."))/(float(height.replace(",", "."))**2), 1))

mass, height = [float(x) for x in input().replace(",", ".").split(" ")]
print(round(mass/height**2,1))

weight, height = map(float, input().replace(",", ".").split(" "))
print(round(weight/(height ** 2),1))