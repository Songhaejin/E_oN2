a = int(input("조각 수 : "))

arr= [1,1]

for i in range(2, a+1) :
	arr.append(arr[i-2] + arr[i-1])
print(arr[a])
