# Задача 12. Реализовать конечный автомат Мили или конечный автомат Мура
# Способ 2 - оператор сопоставления с образцом match (PEP 636).

class MooreMachine:
    def __init__(self):
        self.state = 'n5'
        self.edge_count = {}
        self.seen_states = {'n5'}

    def get_output(self):
        if self.state in ('n0', 'n1', 'n2', 'n4', 'n6', 'n8',):
            return 'U0'
        return 'U1'

    # Возвращает число переходов между парой состояний-аргументов
    def seen_edge(self, from_state, to_state):
        key = (from_state, to_state)
        return self.edge_count.get(key, 0)

    def _increment_edge(self, from_state, to_state):
        key = (from_state, to_state)
        self.edge_count[key] = self.edge_count.get(key, 0) + 1

    def select(self, action):
        if action == 'erase':
            return self._select_erase()
        elif action == 'link':
            return self._select_link()
        elif action == 'model':
            return self._select_model()
        elif action == 'step':
            return self._select_step()
        elif action == 'trash':
            return self._select_trash()
        elif action == 'tweak':
            return self._select_tweak()
        elif action == 'warp':
            return self._select_warp()
        elif action == 'widen':
            return self._select_widen()
        else:
            return 'unknown'

    def _select_erase(self):
        current = self.state
        match current:
            case 'n2':
                self.state = 'n6'
            case 'n7':
                self.state = 'n1'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_link(self):
        current = self.state
        match current:
            case 'n1':
                self.state = 'n7'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_model(self):
        current = self.state
        match current:
            case 'n6':
                self.state = 'n8'
            case 'n8':
                self.state = 'n4'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_step(self):
        current = self.state
        match current:
            case 'n2':
                self.state = 'n3'
            case 'n5':
                self.state = 'n9'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_trash(self):
        current = self.state
        match current:
            case 'n0':
                self.state = 'n2'
            case 'n4':
                self.state = 'n3'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_tweak(self):
        current = self.state
        match current:
            case 'n3':
                self.state = 'n7'
            case 'n7':
                self.state = 'n9'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_warp(self):
        current = self.state
        match current:
            case 'n0':
                self.state = 'n0'
            case 'n4':
                self.state = 'n9'
            case 'n8':
                self.state = 'n5'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    def _select_widen(self):
        current = self.state
        match current:
            case 'n9':
                self.state = 'n0'
            case _:
                return 'unsupported'
        self._increment_edge(current, self.state)
        self.seen_states.add(self.state)

    # Метод, сообщающий было ли указанное состояние уже посещено
    def seen_state(self, state):
        if state not in self.seen_states:
            return False
        return True

    # Метод, сообщающий является ли текущее состояние частью
    # какого-либо цикла графа
    def part_of_loop(self):
        return True


def main():
    return MooreMachine()


def test():
    # Создание экземпляра автомата
    obj = main()

    # Проверка начального состояния
    assert obj.state == 'n5'
    assert obj.get_output() == 'U1'

    # Проверки для get_output
    obj.state = 'n0'
    assert obj.get_output() == 'U0'
    obj.state = 'n1'
    assert obj.get_output() == 'U0'
    obj.state = 'n2'
    assert obj.get_output() == 'U0'
    obj.state = 'n3'
    assert obj.get_output() == 'U1'
    obj.state = 'n4'
    assert obj.get_output() == 'U0'
    obj.state = 'n5'
    assert obj.get_output() == 'U1'
    obj.state = 'n6'
    assert obj.get_output() == 'U0'
    obj.state = 'n7'
    assert obj.get_output() == 'U1'
    obj.state = 'n8'
    assert obj.get_output() == 'U0'
    obj.state = 'n9'
    assert obj.get_output() == 'U1'

    # seen_edge и _increment_edge
    assert obj.seen_edge('n2', 'n7') == 0
    obj._increment_edge('n2', 'n7')
    assert obj.seen_edge('n2', 'n7') == 1
    obj._increment_edge('n2', 'n7')
    assert obj.seen_edge('n2', 'n7') == 2
    obj.edge_count.clear()

    # Проверки для erase
    obj.state = 'n2'
    obj.select('erase')
    assert obj.state == 'n6'
    assert obj.seen_edge('n2', 'n6') == 1
    obj.edge_count.clear()

    obj.state = 'n7'
    obj.select('erase')
    assert obj.state == 'n1'
    assert obj.seen_edge('n7', 'n1') == 1
    obj.edge_count.clear()

    # Тесты для link
    obj.state = 'n1'
    obj.select('link')
    assert obj.state == 'n7'
    assert obj.seen_edge('n1', 'n7') == 1
    obj.edge_count.clear()

    # Тесты для model
    obj.state = 'n6'
    obj.select('model')
    assert obj.state == 'n8'
    assert obj.seen_edge('n6', 'n8') == 1
    obj.edge_count.clear()

    obj.state = 'n8'
    obj.select('model')
    assert obj.state == 'n4'
    assert obj.seen_edge('n8', 'n4') == 1
    obj.edge_count.clear()

    # Тесты для step
    obj.state = 'n2'
    obj.select('step')
    assert obj.state == 'n3'
    assert obj.seen_edge('n2', 'n3') == 1
    obj.edge_count.clear()

    obj.state = 'n5'
    obj.select('step')
    assert obj.state == 'n9'
    assert obj.seen_edge('n5', 'n9') == 1
    obj.edge_count.clear()

    # Тесты для trash
    obj.state = 'n0'
    obj.select('trash')
    assert obj.state == 'n2'
    assert obj.seen_edge('n0', 'n2') == 1
    obj.edge_count.clear()

    obj.state = 'n4'
    obj.select('trash')
    assert obj.state == 'n3'
    assert obj.seen_edge('n4', 'n3') == 1
    obj.edge_count.clear()

    # Тесты для tweak
    obj.state = 'n3'
    obj.select('tweak')
    assert obj.state == 'n7'
    assert obj.seen_edge('n3', 'n7') == 1
    obj.edge_count.clear()

    obj.state = 'n7'
    obj.select('tweak')
    assert obj.state == 'n9'
    assert obj.seen_edge('n7', 'n9') == 1
    obj.edge_count.clear()

    # Тесты для warp
    obj.state = 'n0'
    obj.select('warp')
    assert obj.state == 'n0'
    assert obj.seen_edge('n0', 'n0') == 1
    obj.edge_count.clear()

    obj.state = 'n4'
    obj.select('warp')
    assert obj.state == 'n9'
    assert obj.seen_edge('n4', 'n9') == 1
    obj.edge_count.clear()

    obj.state = 'n8'
    obj.select('warp')
    assert obj.state == 'n5'
    assert obj.seen_edge('n8', 'n5') == 1
    obj.edge_count.clear()

    # Тесты для widen
    obj.state = 'n9'
    obj.select('widen')
    assert obj.state == 'n0'
    assert obj.seen_edge('n9', 'n0') == 1
    obj.edge_count.clear()

    # Проверки для неподдерживаемых методов
    obj.state = 'n0'
    assert obj.select('erase') == 'unsupported'
    assert obj.select('link') == 'unsupported'
    assert obj.select('model') == 'unsupported'
    assert obj.select('step') == 'unsupported'
    assert obj.select('tweak') == 'unsupported'
    assert obj.select('widen') == 'unsupported'

    obj.state = 'n1'
    assert obj.select('trash') == 'unsupported'
    assert obj.select('warp') == 'unsupported'

    # Проверки для seen_state
    assert obj.seen_state('n7') is True
    obj.seen_states.clear()
    assert obj.seen_state('n7') is False

    # Проверки для part_of_loop
    obj.state = 'n0'
    assert obj.part_of_loop() is True
    obj.state = 'n1'
    assert obj.part_of_loop() is True
    obj.state = 'n2'
    assert obj.part_of_loop() is True
    obj.state = 'n3'
    assert obj.part_of_loop() is True
    obj.state = 'n4'
    assert obj.part_of_loop() is True
    obj.state = 'n5'
    assert obj.part_of_loop() is True
    obj.state = 'n6'
    assert obj.part_of_loop() is True
    obj.state = 'n7'
    assert obj.part_of_loop() is True
    obj.state = 'n8'
    assert obj.part_of_loop() is True
    obj.state = 'n9'
    assert obj.part_of_loop() is True

    # Проверки для неизвестных методов
    assert obj.select('jump') == 'unknown'

test()
