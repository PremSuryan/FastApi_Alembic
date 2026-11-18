def validBrackets(queries):
    if not isinstance(queries, list):
        queries=[queries]
    result=[]
    pairs={
        ")":"(",
        "}":"{",
        "]":"["
    }

    for query in queries:
        stack =[]
        isValid = True

        for char in query:
            if char in pairs.values():
                stack.append(char)

            else:
                if not stack:
                    isValid=False
                    break

                top = stack.pop()
                
                if top!=pairs[char]:
                    isValid=False
                    break


        if isValid and not stack:
            result.append("YES")
        else:
            result.append("NO")


    return result


print(validBrackets(["[{()}]","[(])", "{{}", "())"]))
# print(validBrackets("[{()}]"))