def write_log(val):
    print(val)
    f = open("record.txt", "a")
    f.write(str(val) + "\n")
    f.close()

name = input("enter student name: ")
write_log(name)

age = int(input("enter age: "))
write_log(age)


marks = input("enter marks: ").split()
total = 0
for m in marks:
    total = total + int(m)
write_log(total)


avg = total / len(marks)
write_log(avg)

if avg >= 40:
    write_log("pass")
else:
    write_log("fail")
    
nums = []
n = int(input("how many numbers: "))
for i in range(n):
    x = int(input("enter number: "))
    nums.append(x)

write_log(nums)

write_log(even)
write_log(odd)

x = int(input("enter number for factorial: "))
fact = 1
for i in range(1, x + 1):
    fact = fact * i
write_log(fact)
