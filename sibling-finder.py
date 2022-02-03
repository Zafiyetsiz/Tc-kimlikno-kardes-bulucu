#############################

#PROJECT 3 SIBLING FINDER 

#Language :Turkish 
  
#Turkey ID(identification) number SIBLING FINDER

#The simplest and the easiest way to find your simbling's ID number

#Contact me  on ;

#Telegram  : Zafiyetsiz0
#Instagram : Zafiyetsiz

##############################
a= input(" Kendi  tc kimlik numaranizin ilk 9 hanesini giriniz: ")

a= int(a)

print("Sizin tc kimlik numaranizin ilk 9 hanesi " , a)

print("----------------------------------------------")
print("Kardesiniz sizden buyuk ise")
Bk=(a + 29999) #buyuk kardes
print("Kardesinizin tc kimlik numarasinin ilk 9 hanesi" , Bk)

    
print("------------------------------------------")
print("Kardesiniz sizden kucuk ise")
Kk=(a - 29999) #kucuk kardes
print("Kardesinizin tc kimlik numarasinin ilk 9 hanesi" , Kk)

print("------------------------------------------")
print("------------------------------------------")

print(" Son 2 haneyi de bulmak icin Sizden (buyuk veya kucuk) kardesinizin  tc kimlik numarasini  teker teker girmenizi isteyecegiz :))) ")

print("------------------------------------------")
print("------------------------------------------")
print("Kardesinizin;")
print("tc  nin ilk 1. rakamını yazın")

a= input(" 1.rakam: ")
a= int(a)

print("tc  nin ilk 2. rakamını yazın")

b = input("2.rakam: ")
b= int(b)

print("tc  nin ilk 3. rakamını yazın")

c = input("3.rakam: ")
c= int(c)

print("tc  nin ilk 4. rakamını yazın")

d = input("4.rakam: ")
d= int(d)

print("tc  nin ilk 5. rakamını yazın")

e = input("5.rakam: ")
e= int(e)

print("tc  nin ilk 6. rakamını yazın")

f = input("6.rakam: ")
f= int(f)

print("tc  nin ilk 7. rakamını yazın")

g = input("7.rakam: ")
g= int(g)

print("tc  nin ilk 8. rakamını yazın")

h = input("8.rakam: ")
h= int(h)

print("tc  nin ilk 9. rakamını yazın")

i = input("9.rakam: ")
i= int(i)

print("------------------------------------------")
print("------------------------------------------")


tekler=(a + c + e + g + i)    # 1,3,5,7 ve 9. rakamların toplamı
tekler = int(tekler)
Çiftler=(b + d + f + h)       # 2,4,6 ve 8. rakamların toplamı
Çiftler = int(Çiftler)

x =(tekler * 7)
x = int(x)
y =(Çiftler * 9)
y = int(y)

qwe =(x+y)
z =(qwe % 10)
z =int(z)
print("10.rakam=" ,z) #10.rakamı yazdırma 




w=(a + b +c + d + e + f + g + h + i + z)
ğ=(w % 10)
print("11.rakam=" ,ğ)

print("Son 2 rakam=" ,z ,ğ )

print("Tc kimlik no nuz:")
print(a,b,c,d,e,f,g,h,i,z,ğ) 
