def hourglassSum(arr):
    max_sum=0
    imax=len(arr)-2
    jmax=len(arr[0])-2
    for i in range(0,imax):
        for j in range(0,jmax):
            hg_sum=sum(arr[i][j:j+3])+sum(arr[i+2][j:j+3])+arr[i+1][j+1]            	
            print(i,j)
            print(arr[i][j:j+3])
            print([" ",arr[i+1][j+1],""])
            print(arr[i+2][j:j+3])
            print(hg_sum)

            if i==0 and j==0:
                max_sum=hg_sum
            elif hg_sum>max_sum:
                max_sum=hg_sum

    return(max_sum)

if __name__ == '__main__':
    #arr=[[1,1,1,0,0,0],[0,1,0,0,0,0],[1,1,1,0,0,0],[0,0,2,4,4,0],[0,0,0,2,0,0],[0,0,1,2,4,0]]
    arr=[[-1,-1,0,-9,-2,-2],[-2,-1,-6,-8,-2,-5],[-1,-1,-1,-2,-3,-4],[-1,-9,-2,-4,-4,-5],[-7,-3,-3,-2,-9,-9],[-1,-3,-1,-2,-4,-5]]
    res=hourglassSum(arr)
    print("result = {}".format(res))