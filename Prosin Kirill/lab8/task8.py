def main():
    mas = []
    height = 36
    speed = 3
    fuel = 10
    gravity = 3
    thrust_step = 4
    mas.append(format_state(height, speed, fuel))
    while height > 0:
        command = input()
        if command == "exit":
            print("Полет прерван")
            return
        elif is_valid_command(command):
            if can_burn(command, fuel):
                height, speed, fuel = simulate_step(height, speed, fuel, power, gravity, thrust_step)
                mas.append(format_state(height, speed, fuel))
            else:
                print("Недостаточно топлива")
                return
        else:
            print("Ошибка команды")
    print(*mas, sep='\n')
    print(get_status(height, speed))
def is_valid_command(command):
    if command == "exit":
        return "exit"
    elif command in {"0", "1", "2"}:
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