
def sockMerchant(n, ar):
    color_set=set(ar)
    pair_cnt=0
    print(color_set)
    for c in color_set:
        c_cnt=ar.count(c)
        print("{},{}".format(c,c_cnt))
        if c_cnt > 1:
        	#print("I am here")
            pair_cnt += int(c_cnt/2)
            print(pair_cnt)
    
    return pair_cnt

if __name__ == '__main__':

	result=sockMerchant(9,[1,2,3,4,5,2,3,4,56])
	print(result)