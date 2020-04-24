testcase_count=int(raw_input())

tc_input_lst=[]
for tc in range(0,testcase_count):
    tmp_input=[int(i) for i in raw_input().split()]
    tc_input_lst.append(tmp_input)
    for pair in range(0,tmp_input[1]):
        tmp_pair_input=[int(i) for i in raw_input().split()]
        tc_input_lst.append(tmp_pair_input)
        
tc_input_lst_index=0
for tc in range(0,testcase_count):
    n=tc_input_lst[tc_input_lst_index][0]
    m=tc_input_lst[tc_input_lst_index][1]
    print("tc_input_lst_index={}".format(tc_input_lst_index))
    print("n={}".format(n))
    print("m={}".format(m))
    
    for i in range(m):
        tc_pair_index=tc_input_lst_index+(i+1)
        print("tc_pair_index={}".format(tc_pair_index))
        repeat_count=[0,0]
        for j in range((tc_input_lst_index+1),tc_input_lst_index+m):
            if j == tc_pair_index:
                continue
            if tc_input_lst[tc_pair_index][0] in tc_input_lst[j]:
                repeat_count[0]+=1
            
            if tc_input_lst[tc_pair_index][1] in tc_input_lst[j]:
                repeat_count[1]+=1
            
        if repeat_count[0] > 1 or repeat_count[1] > 1:
            print ("NO")
            break
        
    if repeat_count[0] < 2 and repeat_count[1] < 2:
        print ("YES")

    tc_input_lst_index += (m+1)
    
