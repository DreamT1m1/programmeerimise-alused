from datetime import *


#1
today = date.today()
print(f"Today is {today.strftime("%m month, %Y year and %d day")}")
print(f"It's {30 - today.day} days til the end of the month, ~{(12 - today.month) * 30 + (30 - today.day)} days til year's end")

birthday = date(2002, 5, 8)
print(f"I was born on {birthday.strftime("%d.%m.%Y")}")
difference = today - birthday
print(f"So now I am {difference.days // 365} years,  {difference.days % 365 // 30} months, {difference.days % 365 % 30} days old")

#2
"""
Koosta programm on öeldud tehte 3 + 8 / (4 - 2) * 4 vastuse?
+Kuidas mõjutab sulgude kasutamine/kasutamata jätmine tööd?
+Katseta erinevaid kombinatsioone paralleelselt ning lisa ka selgitavad tekstid, et väljund oleks arusaadav.

Sulud mõjutavad seda, mis järjekorras tehteid tehakse, ehk annab prioriteedi
"""
print("Trying to solve 3 + 8 / (4 - 2) * 4")
print(f"First: {3 + 8 / (4 - 2) * 4}")
print(f"Second: {3 + (8 / 4) - 2 * 4}")
print(f"Third: {(3 + 8) / 4 - 2 * 4}")
print("Etc")

#3

