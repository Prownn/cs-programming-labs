import sys

def main():
    height = 36
    speed = 3
    fuel = 10
    gravity = 3
    thrust_step = 4
    while height > 0:
        command = input()
        if is_valid_command(command) and can_burn(command, fuel):
            height, speed, fuel = simulate_step(height, speed, fuel, power, gravity, thrust_step)
        else:
            return print("Ошибка команды")
        print(format_state(height, speed, fuel))
    print(get_status(height, speed))

def is_valid_command(command):
    if command == "exit":
        print("Полет прерван")
        sys.exit()
    elif int(command) <= 2:
        global power
        power = int(command)
        return True
    else:
        return False
def can_burn(power, fuel):
    if fuel > 0:
        if int(fuel) - int(power) > 0:
            return True
        else:
            return False
    else:
        return False
def simulate_step(height, speed, fuel, power, gravity, thrust_step):
    if can_burn(power, fuel):
        speed = speed + gravity - thrust_step * power
        if speed <= 0:
            speed = 0
        fuel = fuel - power
        height = height - speed
        if height <= 0:
            height = 0
    return height, speed, fuel
def get_status(height, speed, safe_speed=2):
    if height > 0:
        return "В полете"
    elif height == 0 and speed <= safe_speed:
        return "Посадка успешна"
    elif height == 0 and speed > safe_speed:
        return "Авария"
def format_state(height, speed, fuel):
    return f"Высота: {height} | Скорость: {speed} | Топливо: {fuel}"

main()