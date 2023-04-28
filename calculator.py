def calculator():
  process = int(input(
    "Введи дію, використовуючи відповідне число: 1 Додавання, 2 Віднімання, 3 Множення, 4 Ділення: "
  ))
  b = int(input("Перше число: "))
  c = int(input("Друге число: "))
  if process == 1:
    a = b+c
    print("Додавання " + str(b) + " і " + str(c))
    print("Результат = " + str(a))
    calculator()

  elif process == 2:
    a = b-c
    print("Віднімання " + str(b) + " і " + str(c))
    print("Результат = " + str(a))
    calculator()

  elif process == 3:
    a = b*c
    print("Множення " + str(b) + " на " + str(c))
    print("Результат = " + str(a))
    calculator()

  elif process == 4:
    a = int(b)/int(c)
    print("Ділення " + str(b) + " на " + str(c))
    print("Результат = " + str(a))
    calculator()
    



print(calculator())
