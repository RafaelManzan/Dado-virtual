import random

response=input("Quer jogar um dado?(digite s para sim ou n para não)")

while True:
    if response=="s":
        while True:
            no = random.randint(1,6)
            print("O número é: ", no)
            if no==1:
                print("[-----]")
                print("|     |")
                print("|  @  |")
                print("|     |")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break
            if no==2:
                print("[-----]")
                print("|@    |")
                print("|     |")
                print("|    @|")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break
            if no==3:
                print("[-----]")
                print("|@    |")
                print("|  @  |")
                print("|    @|")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break
            if no==4:
                print("[-----]")
                print("|@   @|")
                print("|     |")
                print("|@   @|")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break
            if no==5:
                print("[-----]")
                print("|@   @|")
                print("|  @  |")
                print("|@   @|")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break
            if no==6:
                print("[-----]")
                print("|@   @|")
                print("|@   @|")
                print("|@   @|")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(digite s para sim ou n para não)")
                break

    if response=="n":
        print("Ok, obrigado!")
        break
