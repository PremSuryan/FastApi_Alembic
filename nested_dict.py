#{'a':1,'b':2,{'c':2,{'d':3}}}

#Flatten Dict:

input_dic = {'a':1,'b':{'c':2},'c':{'b':{'d':3}}}


def flatten_dict(input_dic, sep=".", key=""):
    dic={}
    for k ,v in input_dic.items():
        new_key = f"{key}{sep}{k}" if key else k

        if isinstance(v, dict):
            dic.update(flatten_dict(v, sep, new_key))

        else:
            dic[new_key] = v

    return dic  

print(flatten_dict(input_dic))


#Nested list to Flatten list

arr = [1,2,[3,4],[7,8,[9,0]]]

def flatten_list(arr):
    # print(arr)

    out = []

    for i in arr:
        if isinstance(i, list):
            out.extend(flatten_list(i))
        else:
            out.append(i)

    return out

print(flatten_list(arr))



text = "He said, \"Hello!\""  #output = "He said Hello"
print(text.split())

rex = []
for i in text:
    string = ""
    if i == " " or i == "," or i == '"':
        rex.append(string) 

    string += i
    # rex.append(string) 

print(rex)