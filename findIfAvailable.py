import whois
import time
import random as rd
import io
result = open("availables.txt","w")
names_file = io.open("generated_domains_names.txt","r",encoding='utf8')

i = 0
for line in names_file:
    # We put random wait between whois call
    # to avoid been banned too rapidly
    # 200-300 ms
    time.sleep(rd.randrange(200,350)/1000.)
    w = whois.whois(line.strip())
    if w["status"] == None:
        print("Found : "+line)
        result.write(line)
        result.write('\n')

result.close()
