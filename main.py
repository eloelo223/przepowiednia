import random
import webbrowser as wb
import time

lista = ["Szczęśliwe życie", "Żmudne życie", "Nudne życie", "Chujowe życie"]

imie = input("jak masz na imię:")
print("cześć", imie)
time.sleep(3)
if imie == 'wersow':
    print("gratulacje odblokowałeś easter egga")
    wb.open('https://www.glamour.pl/media/cache/default_view/uploads/media/default/0005/57/wersow-i-friz-zdradzili-swoje-slubne-plany-wiemy-ile-maja-zamiar-wydac-na-wesele-kwota-robi-wrazenie_1.jpeg')
    time.sleep(6)
    exit()

przepowiednia = input("co chcesz zrobic: przepowiednia albo smierc")


if przepowiednia == 'smierc':
    time.sleep(6)
    exit()


if przepowiednia == 'przepowiednia':
    print(imie , "będziesz miał", str(lista[random.randint(0, len(lista)-1)]))
    time.sleep(6)
    exit()

else:
    print("spróbuj ponownie i wpisz odpowiednie polecenie ")
    time.sleep(6)
    exit()











