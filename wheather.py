import pyowm

token = 'a01bff19c34db14ebf253e1a3514b7c5'
owm = pyowm.OWM(token)
mgr = owm.weather_manager()

def predict(inp):
    global token, owm, mgr

    observation = mgr.weather_at_place(inp)
    w = observation.weather

    print("Погода - ", w.detailed_status)
    print("Ветер - ", w.wind())

    print("Влажность - ", w.humidity)
    print("Тепература - ", w.temperature())

try:
    while True:
        inp = input("Введите город: ")
        
        city = predict(inp)

except:
    print("Ошибка, введите существующий город!")
    break