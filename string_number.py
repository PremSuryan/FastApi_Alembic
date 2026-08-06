#String count

s = "aabcccdd"

dic={}

for i in range(len(s)):
    if s[i] in dic:
        dic[s[i]] += 1
        
    else:
        dic[s[i]] = 1
    
out = ""
for k,v in dic.items():
    out += f"{k}{v}"

print(out)