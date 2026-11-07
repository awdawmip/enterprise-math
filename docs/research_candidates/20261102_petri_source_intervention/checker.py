from fractions import Fraction as Q


def net(swap=False, remove_a=False):
    a, b = ('z', 'y') if swap else ('y', 'z')
    return {
        'p0': [('pa', Q(1, 2), ''), ('pb', Q(1, 2), '')] if not remove_a else
              [('abort', Q(1, 2), '⊥'), ('pb', Q(1, 2), '')],
        'pa': [('p' + a, Q(1), a)],
        'pb': [('p' + b, Q(1), b)],
        'py': [('pf', Q(1), '')],
        'pz': [('pf', Q(1), '')],
        'pf': [('pf', Q(1), '')],
        'abort': [('abort', Q(1), '')],
    }


def trace(n, steps):
    state = [('p0', '', Q(1))]
    for _ in range(steps):
        state = [(v, word + s, w * mass) for u, word, w in state
                 for v, mass, s in n[u]]
    output = {}
    for _, word, mass in state:
        output[word] = output.get(word, Q(0)) + mass
    assert sum(output.values()) == 1
    return output


for t in range(9):
    x, y = trace(net(), t), trace(net(True), t)
    assert x == y
    if t >= 2:
        assert x == {'y': Q(1, 2), 'z': Q(1, 2)}
        assert trace(net(False, True), t) == {'⊥': Q(1, 2), 'z': Q(1, 2)}
        assert trace(net(True, True), t) == {'⊥': Q(1, 2), 'y': Q(1, 2)}
print('PASS exact rational finite horizons 0..8')
