a = [1,5,2,6,3,7,4]

print(a)


def solution(c):
     b = list(map(int,input("i, j , k 수를 입력 :  ").split(",")))
     c = c[b[0]-1 : b[1]]
     c.sort()
     print(c)
     c = c[b[2]-1]
     return c

print(" k번째의 수는 : ", solution(c)) 
