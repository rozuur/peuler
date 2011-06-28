def even_fibs():
    # Generator for even fibonacci numbers
    a, b = 1, 2
    while True:
        yield b
        a, b = b, a+b # 2, 3
        a, b = b, a+b # 3, 5
        a, b = b, a+b # 5, 8
 
fsum = 0
for i in even_fibs():
    if i < 4000000:
        fsum += i
    else: break
 
print fsum
