class MooreMachine:
    def __init__(self):
        self.state = 'S4'
        self.outputs = {
            'S0': 'r5', 'S1': 'r0', 'S2': 'r6',
            'S3': 'r5', 'S4': 'r4', 'S5': 'r3',
            'S6': 'r1', 'S7': 'r6', 'S8': 'r0'
        }

        self.transitions = {
            'S4': {'skew': 'S4', 'swap': 'S7'},
            'S7': {'look': 'S8'},
            'S8': {'mix': 'S4', 'rev': 'S6', 'swap': 'S5'},
            'S5': {'skew': 'S0'},
            'S6': {'mix': 'S1'},
            'S0': {'rev': 'S1', 'get': 'S3'},
            'S1': {'swap': 'S5', 'split': 'S2'},
            'S2': {'swap': 'S3'},
            'S3': {'get': 'S2'}
        }

        self.all_methods = {
            'skew', 'swap', 'look', 'mix',
            'rev', 'get', 'split'
        }

        self.used_methods = set()
        self.loop_states = set(self.outputs.keys())
        self.max_out = max(len(v) for v in self.transitions.values())

    def _call(self, name):
        if name not in self.all_methods:
            return 'unknown'
        if name not in self.transitions.get(self.state, {}):
            return 'unsupported'

        self.state = self.transitions[self.state][name]
        self.used_methods.add(name)
        return None

    def __getattr__(self, name):
        if name.startswith('select_'):
            method = name.replace('select_', '')

            def wrapper():
                return self._call(method)

            return wrapper

        raise AttributeError(name)

    def get_output(self):
        return self.outputs[self.state]

    def part_of_loop(self):
        return self.state in self.loop_states

    def seen_method(self, name):
        return name in self.used_methods

    def has_max_out_edges(self):
        return len(self.transitions.get(self.state, {})) == self.max_out


def main():
    return MooreMachine()


def test():
    # Создание экземпляра автомата
    obj = main()

    # Проверка начального состояния
    assert obj.state == 'S4'
    assert obj.get_output() == 'r4'

    # Проверки для part_of_loop
    obj.state = 'S0'
    assert obj.part_of_loop() is True
    obj.state = 'S1'
    assert obj.part_of_loop() is True
    obj.state = 'S2'
    assert obj.part_of_loop() is True
    obj.state = 'S3'
    assert obj.part_of_loop() is True
    obj.state = 'S4'
    assert obj.part_of_loop() is True
    obj.state = 'S5'
    assert obj.part_of_loop() is True
    obj.state = 'S6'
    assert obj.part_of_loop() is True
    obj.state = 'S7'
    assert obj.part_of_loop() is True
    obj.state = 'S8'
    assert obj.part_of_loop() is True

    # Проверки для seen_method
    assert obj.seen_method('swap') is False
    obj.select_swap()
    assert obj.seen_method('swap') is True
    assert obj.seen_method('get') is False

    # Проверки для has_max_out_edges
    obj.state = 'S0'
    assert obj.has_max_out_edges() is False
    obj.state = 'S8'
    assert obj.has_max_out_edges() is True

    # Проверки для get_output
    obj.state = 'S0'
    assert obj.get_output() == 'r5'
    obj.state = 'S1'
    assert obj.get_output() == 'r0'
    obj.state = 'S2'
    assert obj.get_output() == 'r6'
    obj.state = 'S3'
    assert obj.get_output() == 'r5'
    obj.state = 'S4'
    assert obj.get_output() == 'r4'
    obj.state = 'S5'
    assert obj.get_output() == 'r3'
    obj.state = 'S6'
    assert obj.get_output() == 'r1'
    obj.state = 'S7'
    assert obj.get_output() == 'r6'
    obj.state = 'S8'
    assert obj.get_output() == 'r0'

    # Проверки для метода get
    obj.state = 'S0'
    obj.select_get()
    assert obj.state == 'S3'

    obj.state = 'S3'
    obj.select_get()
    assert obj.state == 'S2'

    # Проверки для метода look
    obj.state = 'S7'
    obj.select_look()
    assert obj.state == 'S8'

    # Проверки для метода mix
    obj.state = 'S6'
    obj.select_mix()
    assert obj.state == 'S1'

    obj.state = 'S8'
    obj.select_mix()
    assert obj.state == 'S4'

    # Проверки для метода rev
    obj.state = 'S0'
    obj.select_rev()
    assert obj.state == 'S1'

    obj.state = 'S8'
    obj.select_rev()
    assert obj.state == 'S6'

    # Проверки для метода skew
    obj.state = 'S4'
    obj.select_skew()
    assert obj.state == 'S4'

    obj.state = 'S5'
    obj.select_skew()
    assert obj.state == 'S0'

    # Проверки для метода split
    obj.state = 'S1'
    obj.select_split()
    assert obj.state == 'S2'

    # Проверки для метода swap
    obj.state = 'S1'
    obj.select_swap()
    assert obj.state == 'S5'

    obj.state = 'S2'
    obj.select_swap()
    assert obj.state == 'S3'

    obj.state = 'S4'
    obj.select_swap()
    assert obj.state == 'S7'

    obj.state = 'S8'
    obj.select_swap()
    assert obj.state == 'S5'

    # Проверки для неподдерживаемых методов
    obj.state = 'S0'
    assert obj.select_look() == 'unsupported'
    assert obj.select_mix() == 'unsupported'
    assert obj.select_skew() == 'unsupported'
    assert obj.select_split() == 'unsupported'
    assert obj.select_swap() == 'unsupported'

    obj.state = 'S1'
    assert obj.select_get() == 'unsupported'
    assert obj.select_rev() == 'unsupported'

    # Проверки для неизвестных методов
    assert obj.select_paste() == 'unknown'

    # Проверки для атрибутов, не начинающихся с select_ (покрытие raise AttributeError)
    attribute_error_raised = False
    try:
        obj.undefined_attribute_name
    except AttributeError:
        attribute_error_raised = True
        
    assert attribute_error_raised, "AttributeError не был вызван"

test()
