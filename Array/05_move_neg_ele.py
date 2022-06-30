class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        pos=0
        neg=len(arr)-1
        length=len(arr)-1
        temp_arr=arr.copy()
        for i,ele in enumerate(temp_arr):
            if temp_arr[i] !="#" and ele >0:
                arr[pos]=ele
                pos+=1
                temp_arr[i]="#"
            if temp_arr[length-i] !="#" and temp_arr[length-i]<0 :
                arr[neg]=temp_arr[length-i]
                neg-=1
                temp_arr[length-i]="#"
            if pos>neg:
                return
         
            
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()

