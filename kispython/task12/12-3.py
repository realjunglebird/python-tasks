# Задача 12. Реализовать конечный автомат Мили или конечный автомат Мура
# Способ 3 - описание графа переходов в виде словаря.

class MooreMachine:
    def __init__(self):
        self.state = 'n5'
        self.outputs = {
            'n0': 'U0', 'n1': 'U0', 'n2': 'U0',
            'n3': 'U1', 'n4': 'U0', 'n5': 'U1',
            'n6': 'U0', 'n7': 'U1', 'n8': 'U0',
            'n9': 'U1'
        }
        self.transitions = {
            'n0': {
                'trash': 'n2',
                'warp': 'n0',
            },
            'n1': {
                'link': 'n7',
            },
            'n2': {
                'erase': 'n6',
                'step': 'n3',
            },
            'n3': {
                'tweak': 'n7',
            },
            'n4': {
                'trash': 'n3',
                'warp': 'n9',
            },
            'n5': {
                'step': 'n9',
            },
            'n6': {
                'model': 'n8',
            },
            'n7': {
                'erase': 'n1',
                'tweak': 'n9',
            },
            'n8': {
                'model': 'n4',
                'warp': 'n5',
            },
            'n9': {
                'widen': 'n0',
            },
        }
        self.edge_count = {}
        self.seen_states = ['n5']
        self.actions = [
            'erase',
            'link',
            'model',
            'step',
            'trash',
            'tweak',
            'warp',
            'widen',
        ]

    def get_output(self):
        return self.outputs[self.state]

    # Возвращает число переходов между парой состояний-аргументов
    def seen_edge(self, from_state, to_state):
        key = (from_state, to_state)
        return self.edge_count.get(key, 0)

    def _increment_edge(self, from_state, to_state):
        key = (from_state, to_state)
        self.edge_count[key] = self.edge_count.get(key, 0) + 1

    def select(self, action):
        if action not in self.actions:
            return 'unknown'

        if action not in self.transitions[self.state]:
            return 'unsupported'

        old_state = self.state
        self.state = self.transitions[self.state][action]
        self._increment_edge(old_state, self.state)
        self.seen_states.append(self.state)

    # Метод, сообщающий было ли указанное состояние уже посещено
    def seen_state(self, state):
        if state not in self.seen_states:
            return False
        return True

    # Метод, сообщающий является ли текущее состояние частью
    # какого-либо цикла графа
    def part_of_loop(self):
        start = self.state
        visited = set()
        return self._dfs_loop_check(start, start, visited)

    def _dfs_loop_check(self, state, start, visited):
        if state in visited:
            return False
        visited.add(state)
        for next_state in self.transitions[state].values():
            if next_state == start or self._dfs_loop_check(
                    next_state, start, visited):
                return True
        return False


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

    # Проверки для неизвестных методов
    assert obj.select('jump') == 'unknown'

test()
