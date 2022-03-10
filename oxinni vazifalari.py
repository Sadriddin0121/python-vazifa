
#kiritgan sonni 3 yoki 5ga qoldiqsiz bulinishini chiqarish


a=int(input('son kiriting   '))

if a%3==0 and a%5==0 :
    print('kiritgan soningiz 3 ga ham 5 ga ham qoldiqsiz bulinadi')

if a%3==0 and a%5!=0 :
    print('kiritgan soningiz 3 ga bulinadi 5 ga esa bulinmaydi')
 
if a%3!=0 and a%5==0 :
    print('kiritgan soningiz 3 ga bulinmaydi 5 ga   bulinadi')


print('')
print('')

# 2 ta son kiritganda kattasini kichigiga bulib qoldigini chiqarish


son1=int(input('son kiriting   '))
son2=int(input('son kiriting   '))

b=max(son1,son2)
d=min(son1,son2)

print(b,'ni',d,'ga bulganda qoldiq',b%d)



print('')
print('')

# 2 ta son kiritib kattasini kichigiga bulib butun qismini chiqarish



b=max(son1,son2)
d=min(son1,son2)

print(b,'ni',d,'ga bulganda butun qismi',b//d)


print('')
print('')

# son kiritgnda juft yoki toqligini chiqarish


son1=int(input('son kiriting   '))

if son1%2==0 :
    print('kiritgan soningiz juft son')
else:
    print('kiritgan soningiz toq son')
    











