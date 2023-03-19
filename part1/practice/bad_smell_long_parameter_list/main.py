# У нас есть какой-то юнит, которому мы в параметры передаем
# - наше игровое поле
# - х координату
# - у координату
# - направление смещения
# - летит ли он
# - крадется ли он
# - скорость
# В этом примере есть сразу несколько запахов плохого кода. Исправьте их
#   (длинный метод, длинный список параметров)


class Unit:
    
    def __init__(self, field, state, speed, x, y):
        self.field = field
        self.state = state
        self.speed = speed
        self.x = x
        self.y = y

    def move(self, button_direct):
        speed = self._get_speed()

        if button_direct == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x)
        elif button_direct == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x)
        elif button_direct == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed)
        elif button_direct == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed)

    def _get_speed(self):
        if self.state == 'fly':
            return self.speed * 1.2
        elif self.state == 'creep':
            return self.speed * 0.5
