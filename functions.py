def palindrome(a):
    copy=a
    rev=0
    while a>0:
        rev= (rev*10)+(a%10)
        a//=10
    if copy==rev:
        print(f"{copy} is a palindrome num")
    else:
        
        print(f"{copy} is not a palindrome num")

palindrome(212)
palindrome(122)
palindrome(123)
palindrome(444)