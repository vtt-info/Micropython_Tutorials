# a = 10
# b = 0
# 
# while b < a:
#     print(b)
#     b += 1
 
i = 0
while True:
    print(i)
    i += 1
    if i == 1000:
        break
    
for i in range(0, 1000):
    if i % 4 == 0:
        continue
    else:
        print(i)

   
