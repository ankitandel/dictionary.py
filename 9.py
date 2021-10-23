dic={

    'sonu':85,

    'Kartik':90,

    'Deepak':96,

    'Aman':76,

    'Somesh':60,

    'Umesh':85,

    'Amarpal':70,

    'Roshan':57,

    'Riyaz':98,

    'Shabid':56

}

i=0
a={}
while i<10:
    r=input("enter the keys")
    s=int(input("enter the valuse"))
    a.update({r:s})
    i=i+1
print(a)

