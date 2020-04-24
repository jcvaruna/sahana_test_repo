# adding conflict comment
import string
count=int(raw_input())
str_lst=[]
for i in range(count):
    str_lst.append(raw_input())
    

alpha_list=list(string.ascii_lowercase)

for i in range(count):
    all_characters_present=True
    for alpha in alpha_list:
        if alpha not in str_lst[i]:
            print("NO")
            all_characters_present=False
            break
    
    if all_characters_present:
        print("YES")
