def jumpingOnClouds(c):
    step_cnt=0
    i=0
    while i < (len(c)-3):
        if (c[i+1]==1) or (c[i+1]==0 and c[i+2]==0):
            i+=2
            print("c1")
        elif c[i+1]==0 and c[i+2]==1:
            i+=1
            print("c2")
        step_cnt+=1
    
    return step_cnt+1

if __name__ == '__main__':

	#res=jumpingOnClouds([0,0,1,0,0,1,0])
	res=jumpingOnClouds([0, 0, 0, 1, 0, 0])
	print("min steps = {}".format(res))