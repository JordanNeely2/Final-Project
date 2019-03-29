# a copy of the challenge 6, palindrome permutation

#read in the input
file = open('input.txt', 'r')
out = open('ouput.txt', 'w')

#check if the string is a palindrome
def isPal(s):
    count = 0

    for i in s:
        #make
        if i not in (' ', '!', '?', '.'):
            if s.count(i) % 2 != 0:
                count += 1;

    if count <= 1:
        out.write('"' + s + '"' + ' is a palindrome permutation\n')
    else:
        out.write('"' + s + '"' + ' is not a palindrome permutation\n')

#########################################################

#go through each phrase in the file
for f in file:
    s = f.strip('\n')
    isPal(s)

file.close()
out.close()
