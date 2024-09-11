def CheckPalindrome(n):
   formula = 0
   Copy = n
   while n > 0:
      lastDigit = n % 10
      formula = (formula*10)+lastDigit
      n = n//10
   if Copy == formula:
      print("Palindrome")
   else:
      print("Not Palindrome")
CheckPalindrome(4552)