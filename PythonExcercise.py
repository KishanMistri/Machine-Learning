
'''
#===================|| Date Time Basic ||=======================
#Que-1
import sys
print("Version: "+sys.version[:5])
print("")

#Que-2
import time
H=int(time.strftime("%H"))
if H>12:
    H=H-12
    ampm='PM'
else:
    ampm='AM'
print("Current time is: "+str(H)+":"+time.strftime("%M:%S ")+ampm)

#Que-3
print(' '.join(reversed(sys.argv[1:])))


#Que-4
String=input("Sample Data: ")
LIST=String.split(",")
TUPLE=tuple(String.split(","))
print("Output \nList : "+str(LIST))
print("Tuple : "+str(TUPLE))

#Que-5
String=input("Sample filename :  ")
extension=String.split(".")
print(extension[-1])

#Que-6
color_list = ["Red","Green","White" ,"Black"]
print(str(color_list[0])+" "+str(color_list[-1]))

#Que-7
exam_st_date = (11, 12, 2014)
print("Sample Output : The examination will start from : "+str(exam_st_date[0])+"/"+str(exam_st_date[1])+"/"+str(exam_st_date[2]))

#Que-8
help(print("Expected Results: "+str(input("Enter Function name for more information: "))))

#Que-9
import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))


date1 = date(2014, 7, 2)
date2 = date(2014, 7, 11)
diff = abs(date1 - date2)
print(diff.days)



#Que-10
from datetime import date
d1=input("Input date1 in (yyyy-mm-dd) format:  ")
d2=input("Input date2 in (yyyy-mm-dd) format:  ")

d1Element=d1.split("-")
d2Element=d2.split("-")

date1=date(int(d1Element[0]),int(d1Element[1]),int(d1Element[2]))
date2=date(int(d2Element[0]),int(d2Element[1]),int(d2Element[2]))

diff = abs(date1 - date2)
print(diff.days)


#Que-11. Write a Python program to test whether a number is within 100 of 1000 or 2000.  
num=int(input("Enter Number to test: "))
if num >= 100 and num<=1000 :
    print("It is in Range[100,1000]")

elif num >= 100 and num<=2000 :
    print("It is in Range[100,2000]")

else:
    print("It is not in Range")


#Que-12. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.  


while (1):
    string=input("Enter String: ")
    if  string[0:2] != 'If':
        print("If"+string)
    else:
        print(string)
        break

#Que-13. Write a Python program to get a string which is n (non-negative integer) copies of a given string.  
string=input("Enter String : ")
Mul=int(input("Enter number to multiply: "))
print(string*Mul)


#Que- 14. Write a Python program to check whether a specified value is contained in a group of values.  
listData=[1,3,5,7,9,11,13,15,17]
val=int(input("Enter Number to check: "))
if val in listData:
    print('TRUE')
else:
    print('FALSE')

#Que-15. Write a Python program to create a histogram from a given list of integers.  
#histogram
import matplotlib.pyplot as plt
String=input("Enter data[0,100] saperated by commas: ")
population=String.split(',')
beans=[00,10,20,30,40,50,60,70,80,90,100]
plt.hist(population,beans,histtype="bar",rwidth=0.4)
plt.legend()
plt.show()

#Que-16. Write a Python program to concatenate all elements in a list into a string and return it.  

lst=['k','i','s','h','a','n']
res=" ".join(lst)
print(res)


#Que-17. Write a Python program to print all even numbers from a given numbers list in the same order and stop the printing if any numbers that come after 237 in the sequence.  

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958,743, 527]

for num in numbers:
    if num == 237 :
            break
    else:
        if num %2 ==0 :
            print(num)
'''    
        
        
#===================|| String Lists ||=======================
'''

#Que-1. Write a Python program to count the number of characters (character frequency) in a string.   
def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(char_frequency('google.com'))

#Que-2. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead the empty string.   

def ret_F2L2(str1):
    strlen=len(str1)
    if strlen<2:
        print("Empty String")
    else:
        print(str1[0:2]+""+str1[-2:])
ret_F2L2('ki')

#Que-3. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.   

def change2dollar(str1):
    fc=str1[0]
    strlen=len(str1)
    for count in range(1,strlen-1):
        if str1[count] == fc:
            new = list(str1)
            new[count] = '$'
            str1=''.join(new)
    print(str1)
change2dollar('KishankishanKishan')
  
#Que-4. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.   

def changeWord(str1):
    spaceIdx=str1.index(' ')
    char1=str1[spaceIdx-1]
    char2=str1[len(str1)-1]
    new = list(str1)
    new[spaceIdx-1] = char2
    new[len(str1)-1] = char1
    str1=''.join(new)
    words=str1.split(' ')
    words.reverse()
    print(' '.join(words))
changeWord('kishan mistri')    
  
#Que-5. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string is already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.   

def ingFun(str1):
    if len(str1) <= 2:  
        print(str1)
    else:
        if str1[len(str1)-3:] == 'ing':
            str1+='ly'
            print(str1)
        else :
            str1+='ing'
            print(str1)
                                                                        
ingFun('ru')

#Que-6. Write a Python function that takes a list of words and returns the length of the longest one.   

def longestStrlen(list1):
    return len(max(list1,key=len)),max(list1,key=len)
list1=['Kishan mistri','Sanjay chandlekar','Shah rutvik','Shukla aditya','Aditya pattani','Ashish musani','Savan Matariya','Hitesh bothra']
print(longestStrlen(list1))

#Que-7. Write a Python program to remove the nth index character from a non empty string.  
def chardel(str1 , idx):
    if len(str1) < idx:
        return 'Error: Out of index...!'
    new= list(str1)
    new[idx]=''
    str1=''.join(new)
    return str1
print(chardel('Kishan',10))

#Que-8. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.  
def changestr(new,old):
    fc=old[0]
    lc=old[len(old)-1]
    newList=list(new)
    newList[0]=fc
    newList[len(new)-1]=lc
    str1="".join(newList)
    return str1
print(changestr("Kishan Mistri","Sanjay Chandlekar"))

#Que-9. Write a Python program to remove the characters which have odd index values of a given string.  
def removeOdd(str1):
    new=list(str1)
    for i in range(1,len(str1)+1,2):
        new[i]=""
    str1=''.join(new)
    return str1
print(removeOdd('kishanmistri'))
                                                  

#Que-10. Write a Python program to count the occurrences of each word in a given sentence.  
def wordOcc(str1):
    strList=str1.split(' ')
    dict = {}
    for n in strList:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(wordOcc('I love dog and dog loves me'))    

#Que-11. Write a Python script that takes input from the user and displays that input back in upper and lower cases.  

def UpperLower(str1):
    return str1.upper() , str1.lower()
print(UpperLower('KIshAn MisTrI'))

#Que-12. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).  
def DisplayUnique(items):
    words = [word for word in items.split(",")]
    return (",".join(sorted(list(set(words)))))
print(DisplayUnique('red, white, black, red, green, black'))

#Que-13. Write a Python function to create the HTML string with tags around the word(s).  
#Sample function and result : 
#add_tags('i', 'Python') -> '<i>Python</i>'
#add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'
def addTags(tag,str1):
    return ('<'+tag+'>'+str1+'</'+tag+'>')
print(addTags('i','Kishan Mistri'))

#Que-14. Write a Python function to insert a string in the middle of a string.  
#Sample function and result : 
#insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]
#insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
from math import floor
def Insert_String_middle(str1,str2):
    return str1[:floor(len(str1)/2)]+str2+str1[floor(len(str1)/2):]
print(Insert_String_middle('<<>>','Kishan'))


#Que-15. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2). 
#Sample function and result : 
#insert_end('Python') -> onononon
#insert_end('Exercises') -> eseseses
def a1(str1):
    return str1[-2:]*4
print(a1('Python'))

#Que-16. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
#Sample function and result : 
#first_three('ipy') -> ipy
#first_three('python') -> pyt

def retFirst3char(str1):
    if len(str1)<=3:
        return str1
    else:
        return str1[:3]
    
print(retFirst3char('x124yz123'))


#Que-17. Write a Python function to get the first half of a specified string of even length.
#Sample function and result : 
#string_first_half('Python') -> Pyt
from math import floor

def firstHalf(str1):
    return str1[:floor(len(str1)/2)]
print(firstHalf('Kishan mistri 123'))

#Que-18. Write a Python function to reverses a string if it's length is a multiple of 4.
from math import floor
def revstr(str1):
    if len(str1)%4==0:
        temp=0
        new=list(str1)
        for i in range(0,floor(len(str1)/2)):
            temp=new[i]
            print(temp)
            new[i]=new[len(new)-1-i]
            print(new[i])
            new[len(new)-1-i]=temp
            str1=''.join(new)        
    return str1
print(revstr('Kishan12'))

#Que-19. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters

def condUpper(str1):
    substr=str1[:4]
    countUpper=0
    for i in substr:
        if i.isupper():
            countUpper+=1
    if countUpper>1:
        return str1.upper()
    else: 
        return str1
print(condUpper('Kishan MIstri'))
'''

#=====================||Numbers and List||========================
'''
#Que-1. Write a Python program to sum all the items in a list.  
list1=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
print(sum(list1))

#Que-2. Write a Python program to multiplies all the items in a list.  
def mul(list1):
    mul=1
    for num in list1:
        mul*=num
        
    return mul
list1=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
print(mul(list1))

#Que-3. Write a Python program to get the largest number from a list.  
list2=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
list1=[2468216486484,281686,312616333,381263872637263,263826386323,236282762681638]
print(max(list1))
print(max(list2))


#Que-4. Write a Python program to get the smallest number from a list.  
list2=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
list1=[2468216486484,281686,312616333,381263872637263,263826386323,236282762681638]
print(min(list1))
print(min(list2))


#Que-5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.   
#Sample List : ['abc', 'xyz', 'aba', '1221']
#Expected Result : 2
def ex1(list1):
    count=0
    for string in list1:
        if len(string)>2 and string[0]==string[len(string)-1]:
           count+=1
    return count
List1=['abc', 'xyz', 'aba', '1221']
print(ex1(List1))


#Que-6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.   
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

def last(n): return n[-1]  
      
def sort_list_last(tuples):  
  return sorted(tuples, key=last)  
  
print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))

#Que-7. Write a Python program to remove duplicates from a list.  
list1=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
print(set(list1))


#Que-8. Write a Python program to check a list is empty or not.  
list1=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
list2=[]
def isEmpty(list1):
    if len(list1)>0:
        return False
    else:
        return True
print(isEmpty(list1))
print(isEmpty(list2))

#Que-9. Write a Python program to clone or copy a list.  
def copyList(oriList,copiedList):
    copiedList=[]
    for num in oriList:
        copiedList.append(num)
    return copiedList
list1=[1,2,1,2,4,1,3,4,12,3,45,2,4,5,2,2,54,6,43,2,1,4,65,2]
list2=[]
copyList(list1,list2)
print(list2)

#Que-10. Write a Python program to find the list of words that are longer than n from a given list of words.  
def findLongerWords(list1,number):
    substr=[]
    for string in list1:
        if len(string) > number:
            substr.append(string)
    return substr    
list1=['abakjbjdsbv','dabka','sa','sakba','dbvkbce','skbjd']
print(findLongerWords(list1,10))

#Que-11. Write a Python function that takes two lists and returns True if they have at least one common member.  
def hasEqLen(list1,number):
    substr=[]
    for string in list1:
        if len(string) == number:
            substr.append(string)
    return substr    
def hasCommon(list1,list2):
    if len(list1)<len(list2):
        selList=list1
        comList=list2
    else:
        selList=list2
        comList=list1
    for string in selList:
        resList=hasEqLen(comList,len(string))
        for comStr in resList:
            if string==comStr:
                print(string+"  FOUND")
                break
list1=['abakjbjdsbv','dabka','sa','sakba','dbvkbce','skbjd']
list2=['absa','sakba','dbe','sa']
hasCommon(list1,list2)

#Que-12. Write a Python program to print a specified list after removing the 0th, 2nd, 4th and 5th elements.  
#Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#Expected Output : ['Green', 'White', 'Black']

def removeEle(list1,idxes):
    list2=[]
    sorted(idxes)
    for i in range(0,len(list1)-1):
        if i in idxes:
            continue
        else:
            list2.append(list1[i])
    return list2
List1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
indexes=[0,2,4,5]
print(removeEle(List1,indexes))

#Que-13. Write a Python program to generate a 3*4*6 3D array whose each element is *.  
def create3DArr(l,m,n):
    return [[['*' for _ in range(n)] for _ in range(m)] for _ in range(l)]
print(create3DArr(3,4,6))

#Que-14. Write a Python program to print the numbers of a specified list after removing even numbers from it.  
def removeEle(list1,wanted):
    list2=[]
    sorted(wanted)
    for i in range(0,len(list1)-1):
        if i%2!=0:
            list2.append(list1[i])        
        if i in wanted:
            list1.append()
    print(list2)    
    return list2
List1 = ['Red', 'Green', 'White', 'Black', 'Pink','Yellow','magenta','Violet']
wanted=[0,1]
print(removeEle(List1,wanted))

#Que-15. Write a Python program to shuffle and print a specified list.  
from random import shuffle
list1=['sdvgre','sdnvlks','sdnvl','ds','dsbk','dsds','djvsdjv']
print (list1)
shuffle(list1)
print (list1)

#Que-16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).  
list1=[]
for i in range(1,6):
    list1.append(i)
    list1.append(31-i)
    
    list1.append(i*i)
    list1.append((31-i)*(31-i))
print(sorted(list1))

#Que-17. Write a Python program to generate and print a list except the first 5 elements, where the values are square of numbers between 1 and 30 (both included).

'''
#===============||Dictionary||========================
'''
#Que-1. Write a Python script to sort (ascending and descending) a dictionary by value.

                                                                                                                                                  

