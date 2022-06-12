a = [1,2,3]
b = a 
print(id(a))
print(id(b)) ## id는 메모리 주소

print(a is b) ## 같은 주소면 true 출력

b = a[:] ## 새로운 값을 b에게 넣는것이기 때문에 다른주소를 가진다
a[1] = 4
print(a)
print(b)

from copy import copy
aa = [1,2,3]
bb = copy(aa) ## aa 값을 복사해서 bb에 넣어주는 것이기에 다른 주소를 간진다.
a[1] = 4
print(a)
print(b)

test = "1번"
test2 = "2번"
test , test2 = test2 , test 
## 변두 2개의 값을 서로 바꾸기 위함
print(test)
print(test2)