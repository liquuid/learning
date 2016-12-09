# Declare second integer, double, and String variables.

i = 4
d = 4.0
s = 'HackerRank '

a = 1
b = 1.0
c = "char"
# Read and save an integer, double, and String to your variables.
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

a, b, c = lines
a = int(a)
b = float(b)
c = str(c)
# Print the sum of both integer variables on a new line.
print(i+a)
# Print the sum of the double variables on a new line.
print(d+b)
# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print(s + ' ' + c)
