a=float(input(' 1 - koeffesentni kiriting == '))
b=float(input(' 2 - koeffisentni kiriting == '))
c=float(input(' ozod hadni kiriting kiriting == '))
D=b**2-4*a*c
if D<0 :
    print('diskiriminant manfiy tenglama yechimga ega emas  ')
    g=int(input('koeffitsentlarni qaytadan kiritasizmi ha bolsa 1 ni bosing agar tugatmoqchi bolsangiz 0 ni bosing  ' ))
    if g==1:
        a=float(input(' 1 - koeffesentni kiriting == '))
        b=float(input(' 2 - koeffisentni kiriting == '))
        c=float(input(' ozod hadni kiriting kiriting == '))
        D=b**2-4*a*c
        x1=(-b+D**0.5)/2*a
        x2=(-b-D**0.5)/2*a
        if D==0:
            print('tenglama yagona haqiqiy ildizga ega')
            print('x1 = ',x1)
        if D>0:
             print('tenglama ikkita haqiqiy ildizga ega')
             print('x1 = ',x1)
             print('x2 = ',x2)
    if g==0 :
        print('dastur tugatildi')

x1=(-b+D**0.5)/2*a
x2=(-b-D**0.5)/2*a

if D==0:
    print('tenglama yagona haqiqiy ildizga ega')
    print('x1 = ',x1)

if D>0:
    print('tenglama ikkita haqiqiy ildizga ega')
    print('x1 = ',x1)
    print('x2 = ',x2)










