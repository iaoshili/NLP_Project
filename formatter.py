import sys
import re

p  = '|'
pp  = '|'

janp  = '(jan.*?\d\d?\s*,\s*20\d\d)'
febp  = '(feb.*?\d\d?\s*,\s*20\d\d)'
marp  = '(mar.*?\d\d?\s*,\s*20\d\d)'
aprp  = '(april.*?\d\d?\s*,\s*20\d\d)'
mayp  = '(may.*?\d\d?\s*,\s*20\d\d)'
junep = '(june.*?\d\d?\s*,\s*20\d\d)'
julyp = '(july.*?\d\d?\s*,\s*20\d\d)'
augp  = '(aug.*?\d\d?\s*,\s*20\d\d)'
sepp  = '(sep.*?\d\d?\s*,\s*20\d\d)'
octtp = '(oct.*?\d\d?\s*,\s*20\d\d)'
novp  = '(nov.*?\d\d?\s*,\s*20\d\d)'
decp  = '(dec.*?\d\d?\s*,\s*20\d\d)'

    
jan  = '(jan.*?\d\d?)'
feb  = '(feb.*?\d\d?)'
mar  = '(mar.*?\d\d?)'
apr  = '(april.*?\d\d?)'
may  = '(may.*?\d\d?)'
june = '(june.*?\d\d?)'
july = '(july.*?\d\d?)'
aug  = '(aug.*?\d\d?)'
sep  = '(sep.*?\d\d?)'
octt = '(oct.*?\d\d?)'
nov  = '(nov.*?\d\d?)'
dec  = '(dec.*?\d\d?)'

# 12/15/2014 or December 1
def formatter(s):
    # Todo:
    s = s.lower() 
    
    regexp1 = janp + pp + febp + pp + marp + pp + aprp + pp + mayp + pp + junep + pp + julyp + pp + augp + pp + sepp + pp + octtp + pp + novp + pp + decp
    regexp2 = jan + p + feb + p + mar + p + apr + p + may + p + june + p + july + p + aug + p + sep + p + octt + p + nov + p + dec
    regexp = regexp1 + p + regexp2
    m = re.search(regexp, s)

    if m == None:
        return 'Not Provided'
    
    s = m.group()
    
    return s



# while True:
#     s = raw_input()
#     print formatter(s)

    
    

    
