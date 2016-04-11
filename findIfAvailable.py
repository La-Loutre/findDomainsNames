import whois
import time
import random as rd

result = open("availables.txt","w")
names_file = open("generated_domains_names.txt","r")

i = 0
for line in names_file:
    # We put random wait between whois call
    # to avoid been banned too rapidly
    # 200-300 ms
    time.sleep(rd.randrange(200,350)/1000.)
    print(line)
    w = whois.whois(line)
    if w["status"] == None:
        print("Found : "+line)
        result.write(line)
        result.write('\n')
result.close()
