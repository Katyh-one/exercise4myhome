form = web.input()

print(form.firstname)

print form.lastname


with open('formsubmissions.txt','w') as output:
    output.write('A wonderful bird is the pelican.\n')
    output.write('His bill holds more than his belican.\n')
    output.writelines(["He can take in his beak,\n", "Enough food for a week, \n", "But I'm damned if i see how the helican.\n"])
# as file is closed, we reopen in read mode to read the file and print the lines from the file
with open('pelican.txt', 'r') as file:
    for line in file:
        print(line[:-1])