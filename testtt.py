# given number is a palindrome or not using string conversion

"""numb = 1210
numb = str(numb)

left = 0
right = len(numb) - 1

while left < right:
    if numb[left] != numb[right]:
        print("No")
        break
    left =+1
    right -=1
else:
    print("not palindrome")
        """
        
        
# given number is a palindrome or not without using string conversion


numb = 51215
orginal = numb
reverse = 0

while numb > 0:
    digit = numb % 10   # to get the last digit 
    reverse = reverse * 10 + digit
    numb = numb // 10  # remove the last digit 

if orginal == reverse:
    print("palind")
else:
    print("not palind")

