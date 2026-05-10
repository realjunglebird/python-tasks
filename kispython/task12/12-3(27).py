class MealyMachine:
    def __init__(self):
        self.state = 'Y5'

        # Переходы от каждой вершины, в формате
        # 'имя_метода': ('вершина_назначения', 'возвращаемое_значение')
        self.transitions = {
            'Y0': {
                'merge': ('Y0', 'd3'),
                'post': ('Y6', 'd7'),
            },
            'Y1': {},
            'Y2': {
                'get': ('Y4', 'd3'),
                'open': ('Y7', 'd8'),
            },
            'Y3': {
                'post': ('Y1', 'd3'),
            },
            'Y4': {
                'check': ('Y0', 'd4'),
                'post': ('Y7', 'd0'),
                'throw': ('Y2', 'd7'),
            },
            'Y5': {
                'make': ('Y4', 'd6'),
                'merge': ('Y2', 'd2'),
            },
            'Y6': {
                'merge': ('Y3', 'd0'),
            },
            'Y7': {
                'post': ('Y8', 'd4'),
            },
            'Y8': {
                'merge': ('Y9', 'd0'),
                'post': ('Y5', 'd7'),
            },
            'Y9': {
                'check': ('Y0', 'd1'),
            },
        }
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
    def part_of_loop(self):
        start = self.state
        visited = set()
        return self._dfs_loop_check(start, start, visited)
    
    # Вспомогательный метод для проверки, является ли вершина частью цикла
    def _dfs_loop_check(self, state, start, visited):
        if state in visited:
            return False
        visited.add(state)
        for next_state in self.transitions[state].values():
            if next_state[0] == start or self._dfs_loop_check(
                    next_state[0], start, visited):
                return True
        return False
    
    def move(self, method):
        if method not in self.transitions[self.state]:
            return 'unsupported'
        
        current_state = self.state
        self.state = self.transitions[current_state][method][0]
        self.methods[method] += 1
        return self.transitions[current_state][method][1]
    
    def move_check(self):
        return self.move('check')
    
    def move_get(self):
        return self.move('get')
    
    def move_make(self):
        return self.move('make')
    
    def move_merge(self):
        return self.move('merge')
    
    def move_open(self):
        return self.move('open')
    
    def move_post(self):
        return self.move('post')
    
    def move_throw(self):
        return self.move('throw')


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

    # Проверка неизвестных атрибутов
    assert obj.unknown_attribute is None

test()