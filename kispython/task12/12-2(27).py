class MealyMachine:
    def __init__(self):
        self.state = 'Y5'
        self.methods = {
            'check': 0,
            'get': 0,
            'make': 0,
            'merge': 0,
            'open': 0,
            'post': 0,
            'throw': 0,
        }

    def __getattr__(self, name):
        if name.startswith('move_'):
            def move_unknown(*args, **kwargs):
                return 'unknown'
            return move_unknown

    # Метод, возвращающий истину, если текущее состояние имеет
    # максимальное число выходных дуг в графе
    def has_max_out_edges(self):
        return True if self.state == 'Y4' else False

    # Метод, возвращающий число успешных выполнений аргумента-метода
    def seen_method(self, method):
        return self.methods[method]

    # Метод, возвращающий истину, если текущее состояние является
    # частью какого-либо цикла
    # (для простоты просто сравниваем текущее состояние с
    # заранее найденным списком узлов-частей циклов)
    def part_of_loop(self):
        return self.state in ('Y0', 'Y2', 'Y4', 'Y5', 'Y7', 'Y8')

    # Метод check
    def move_check(self):
        current = self.state
        match current:
            case 'Y4':
                self.state = 'Y0'
                self.methods['check'] += 1
                return 'd4'
            case 'Y9':
                self.state = 'Y0'
                self.methods['check'] += 1
                return 'd1'
            case _:
                return 'unsupported'

    # Метод get
    def move_get(self):
        current = self.state
        match current:
            case 'Y2':
                self.state = 'Y4'
                self.methods['get'] += 1
                return 'd3'
            case _:
                return 'unsupported'

    # Метод make
    def move_make(self):
        current = self.state
        match current:
            case 'Y5':
                self.state = 'Y4'
                self.methods['make'] += 1
                return 'd6'
            case _:
                return 'unsupported'

    # Метод merge
    def move_merge(self):
        current = self.state
        match current:
            case 'Y0':
                self.state = 'Y0'
                self.methods['merge'] += 1
                return 'd3'
            case 'Y5':
                self.state = 'Y2'
                self.methods['merge'] += 1
                return 'd2'
            case 'Y6':
                self.state = 'Y3'
                self.methods['merge'] += 1
                return 'd0'
            case 'Y8':
                self.state = 'Y9'
                self.methods['merge'] += 1
                return 'd0'
            case _:
                return 'unsupported'

    # Метод open
    def move_open(self):
        current = self.state
        match current:
            case 'Y2':
                self.state = 'Y7'
                self.methods['open'] += 1
                return 'd8'
            case _:
                return 'unsupported'

    # Метод post
    def move_post(self):
        current = self.state
        match current:
            case 'Y0':
                self.state = 'Y6'
                self.methods['post'] += 1
                return 'd7'
            case 'Y3':
                self.state = 'Y1'
                self.methods['post'] += 1
                return 'd3'
            case 'Y4':
                self.state = 'Y7'
                self.methods['post'] += 1
                return 'd0'
            case 'Y7':
                self.state = 'Y8'
                self.methods['post'] += 1
                return 'd4'
            case 'Y8':
                self.state = 'Y5'
                self.methods['post'] += 1
                return 'd7'
            case _:
                return 'unsupported'

    # Метод throw
    def move_throw(self):
        current = self.state
        match current:
            case 'Y4':
                self.state = 'Y2'
                self.methods['throw'] += 1
                return 'd7'
            case _:
                return 'unsupported'


def main():
    return MealyMachine()


def test():
    # Создание экземпляра автомата
    obj = main()

    # Проверка начального состояния
    assert obj.state == 'Y5'

    # Проверка метода has_max_out_edges
    obj.state = 'Y0'
    assert obj.has_max_out_edges() is False
    obj.state = 'Y4'
    assert obj.has_max_out_edges() is True

    # Проверка метода seen_method
    assert obj.seen_method('post') == 0
    obj.move_post()
    assert obj.seen_method('post') == 1

    # Проверка метода part_of_loop
    obj.state = 'Y0'
    assert obj.part_of_loop() is True
    obj.state = 'Y1'
    assert obj.part_of_loop() is False
    obj.state = 'Y2'
    assert obj.part_of_loop() is True
    obj.state = 'Y3'
    assert obj.part_of_loop() is False
    obj.state = 'Y4'
    assert obj.part_of_loop() is True
    obj.state = 'Y5'
    assert obj.part_of_loop() is True
    obj.state = 'Y6'
    assert obj.part_of_loop() is False
    obj.state = 'Y7'
    assert obj.part_of_loop() is True
    obj.state = 'Y8'
    assert obj.part_of_loop() is True
    obj.state = 'Y9'
    assert obj.part_of_loop() is False

    # Проверка метода move_check
    obj.state = 'Y4'
    assert obj.move_check() == 'd4'
    obj.state = 'Y9'
    assert obj.move_check() == 'd1'
    obj.state = 'Y0'
    assert obj.move_check() == 'unsupported'

    # Проверка метода move_get
    obj.state = 'Y2'
    assert obj.move_get() == 'd3'

    # Проверка метода move_make
    obj.state = 'Y5'
    assert obj.move_make() == 'd6'

    # Проверка метода move_merge
    obj.state = 'Y0'
    assert obj.move_merge() == 'd3'
    obj.state = 'Y5'
    assert obj.move_merge() == 'd2'
    obj.state = 'Y6'
    assert obj.move_merge() == 'd0'
    obj.state = 'Y8'
    assert obj.move_merge() == 'd0'

    # Проверка метода move_open
    obj.state = 'Y2'
    assert obj.move_open() == 'd8'

    # Проверка метода move_post
    obj.state = 'Y0'
    assert obj.move_post() == 'd7'
    obj.state = 'Y3'
    assert obj.move_post() == 'd3'
    obj.state = 'Y4'
    assert obj.move_post() == 'd0'
    obj.state = 'Y7'
    assert obj.move_post() == 'd4'
    obj.state = 'Y8'
    assert obj.move_post() == 'd7'

    # Проверка метода move_throw
    obj.state = 'Y4'
    assert obj.move_throw() == 'd7'

    # Проверка вызова неизвестных методов
    assert obj.move_move() == 'unknown'

    # Проверка вызова неподдерживаемых методов
    obj.state = 'Y1'
    assert obj.move_check() == 'unsupported'
    assert obj.move_get() == 'unsupported'
    assert obj.move_make() == 'unsupported'
    assert obj.move_merge() == 'unsupported'
    assert obj.move_open() == 'unsupported'
    assert obj.move_post() == 'unsupported'
    assert obj.move_throw() == 'unsupported'

    # Проверка неизвестных атрибутов
    assert obj.unknown_attribute is None

test()
