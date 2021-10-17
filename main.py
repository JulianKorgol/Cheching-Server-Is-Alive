import os
numberOfHosts = 1 #Enter the number of hosts would you like to ping.
Hosts = [] #Enter your hosts in the list.
print("Script for checking that servers are working.")
print("Author: Julian Korgol.")
print("https://juliankorgol.com/")
n = 0
while n < numberOfHosts:
    answer = os.system("ping " +Hosts[n])
    if answer == 0:
        print(Hosts[n] + "\033[92m" + " It's working!")
        n += 1
    else:
        print(Hosts[n] + "\033[91m" + " It's down!")
        n += 1
    print("\033[0m")
