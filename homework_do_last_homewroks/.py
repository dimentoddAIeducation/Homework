sunny="Солнечно"
rainy="Дождливо"
snowy="Снежно"
wind="Ветренно"

temp=int(input("Введите температуру за окном: "))
weather=input("Введите погоду на улице: ")

if temp<0:
    if weather==snowy: print("На улице снег. Советую надеть теплую одежду")

    if weather==rainy: print("Ты чето борщишь")

    if weather==sunny: print("На улице светит солнце и холодно. Советую надеть теплую одежду и взять с собой очки")

    if weather==wind: print("На улице холодно и ветренно. Советую надеть теплую одежду и шарф")

else:
    if weather==rainy: print("На улице дождь. Советую взять с собой зонт")

    if weather==snowy: print("Ты чето борщишь")

    if weather==sunny: print("На улице светит солнце. Советую взять с собой очки и кепку")

    if weather==wind: print("На улице ветренно. Советую взять с собой одежду с воротником")


def car(model, year, body):
    print(f"Ваша машина: {model} {year} года выпуска в кузове {body}")

car("BMW", 2026, "другой машины")
