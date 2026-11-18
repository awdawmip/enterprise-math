"""C79 original native-path rational oracle, from check_finite.py."""
from fractions import Fraction as Q


def native_tail_ratios(c, v, w):
    def consume(masses, stock, symbol):
        weights = []
        for rate, mass in zip((Q(1,4), Q(1), Q(4)), masses):
            den = stock[0] + stock[1] + rate*stock[2] + stock[3]
            weights.append(mass * stock[symbol] * (rate if symbol == 2 else 1) / den)
        stock[symbol] -= 1
        if symbol == 0:
            return [Q(0), weights[0], weights[1]+weights[2]]
        if symbol == 1:
            return [(7*sum(weights)+weights[0])/8, weights[1]/8, weights[2]/8]
        return weights

    body = [2]*(c-v) + [0,1] + [2]*(v-w) + [0,1] + [2]*(w-2)
    tails = ((2,2,3),(2,3,2),(3,2,2))
    rows = []
    for prep in (0, 1):
        state = [Q(7),Q(prep),Q(1-prep)]
        stock = [2,2,c,1]
        for symbol in body:
            state = consume(state,stock,symbol)
        vals = []
        for tail in tails:
            copy_stock, copy_state = stock.copy(), state.copy()
            for symbol in tail:
                copy_state = consume(copy_state,copy_stock,symbol)
            vals.append(sum(copy_state))
        assert sum(vals) == sum(state)
        rows.append(vals)
    return [b/a for a,b in zip(*rows)]
