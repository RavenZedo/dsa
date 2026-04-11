#palindrome number
def isPalindrome(n):  
    if n < 0:
        return False
    num=n
    result=0
    while num>0:
        digit=num%10
        result=result*10+digit
        num=num//10
    return result==n     