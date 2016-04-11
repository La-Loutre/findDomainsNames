import whois
import time
import random as rd
import io
from unidecode import unidecode

result = open("availables.txt","w")
names_file = io.open("generated_domains_names.txt","r",encoding='utf8')

i = 0
for line in names_file:
    # We put random wait between whois call
    # to avoid been banned too rapidly
    # 200-300 ms
    line = unidecode(line)
    time.sleep(rd.randrange(200,350)/1000.)
    if '\n' in line:
        line = line[0:len(line)-1]

    w = whois.whois(line)

    if w["status"] == None:
        print("Found : "+line)
        result.write(line)
        result.write('\n')

result.close()
