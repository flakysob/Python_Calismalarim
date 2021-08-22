a = 1
b = 1

fibonacci = [a,b]

for i in range(20):
    a,b = b,a+b #a'ya b'nin eski değeri, b'ye de a+b atandı
    fibonacci.append(b)
print(fibonacci)
