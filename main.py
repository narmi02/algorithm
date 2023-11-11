
print("Algorithm contains the following task")
print('''        1) Palindrome checker
        2) Find fibinocci sequence of n terms
        3) Frequency of words in a string\n''')
task=int(input("Select one task to perform : "))
# # function to check palindrome
def palindrome():
  string=input("Enter string : ")
  reverse_string=string[::-1]
  print(True) if (reverse_string==string) else print(False)
  
# fibinocci function

def fibfunction(n):
  if (n==0) or (n==1):
    return n
  else:
    return(fibfunction(n-1)+fibfunction(n-2))


# wordcounter function

def wordcounter():
  string=input("Enter string : ")
  word=string.split()
  word_count={}
  for i in word:
    if i  in word_count:
       word_count[i]+=1
    else:
      word_count[i]=1
  return word_count

match task:
  case 1:
    palindrome()
  case 2:
    n=int(input("Enter n :"))
    for i in range(0,n):
     print(fibfunction(i))
  case 3:
   print(wordcounter())
  case _:
   print("invalid option")
   

