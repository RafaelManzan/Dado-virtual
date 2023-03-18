import random

response=input("Quer jogar um dado?(digite sim ou não)")

while True:
    if response=="sim":
        while True:
            no = random.randint(1,6)
            if no==1:
                print("[-----]")
                print("[     ]")
                print("[  1  ]")
                print("[     ]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break
            if no==2:
                print("[-----]")
                print("[2    ]")
                print("[     ]")
                print("[    2]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break
            if no==3:
                print("[-----]")
                print("[3    ]")
                print("[  3  ]")
                print("[    3]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break
            if no==4:
                print("[-----]")
                print("[4   4]")
                print("[     ]")
                print("[4   4]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break
            if no==5:
                print("[-----]")
                print("[5   5]")
                print("[  5  ]")
                print("[5   5]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break
            if no==6:
                print("[-----]")
                print("[6   6]")
                print("[6   6]")
                print("[6   6]")
                print("[-----]")
                response=input("Gostaria de jogar o dado novamente?(responda sim ou não)")
                break

    if response=="não":
        print("Ok, obrigado!")
        break
