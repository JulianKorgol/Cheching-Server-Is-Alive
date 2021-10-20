import os
hosts = [""] #Enter your hosts in the list.
print("Script for checking that servers are working.")
print("Author: Julian Korgol.")
print("https://juliankorgol.com/")
n = 0
numberOfHosts = len(hosts)
while n < numberOfHosts:
    answer = os.system("ping " +hosts[n])
    if answer == 0:
        print(hosts[n] + "\033[92m" + " It's working!")
    else:
        print(hosts[n] + "\033[91m" + " It's down!")
    n += 1
    print("\033[0m")
