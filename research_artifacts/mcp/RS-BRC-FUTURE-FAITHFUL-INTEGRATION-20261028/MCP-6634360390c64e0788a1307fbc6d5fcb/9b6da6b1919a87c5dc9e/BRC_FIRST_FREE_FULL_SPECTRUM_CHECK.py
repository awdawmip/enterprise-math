"""Exact first-free allocator reachability checker for r=1,...,6."""
from itertools import product

def check(r, target):
    reg = [None] * r
    slots = [None] * (r+1)
    for color in range(1, r+1):
        if color in target:
            slots[color] = target.index(color)
    free = [i for i in range(r) if i not in slots]
    if slots[r] is None:
        slots[r] = free.pop(0)
    slots[0] = slots[r]
    for color in range(1, r):
        if slots[color] is None:
            slots[color] = free.pop(0)
    current = None
    steps = 0
    def create():
        nonlocal current, steps
        assert current is None
        used = {v for v in reg if v is not None}
        current = next(v for v in range(r+1) if v not in used)
        steps += 1
        return current
    def bind(i):
        nonlocal steps
        assert current is not None
        reg[i] = current
        steps += 1
    def release():
        nonlocal current, steps
        current = None
        steps += 1
    for d in range(r):
        assert create() == d
        bind(slots[d])
        release()
    assert create() == r
    bind(slots[r])
    release()
    assert create() == 0
    for i in range(r):
        if reg[i] != target[i]:
            j = slots[target[i]]
            assert reg[j] == target[i]
            reg[i] = reg[j]
            steps += 1
    assert tuple(reg) == target and current == 0 and 0 not in reg
    assert steps == 3*r + 4 + (r-len(set(target)))
    return steps

total = 0
for r in range(1, 7):
    maximum = 0
    for c in product(range(1,r+1),repeat=r):
        maximum = max(maximum, check(r,c))
        total += 1
    print(r, r**r, maximum)
print("verified",total)
