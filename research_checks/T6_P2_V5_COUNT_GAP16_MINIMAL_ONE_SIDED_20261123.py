"""Exact finite check for the T6 exact-v2=5 count-gap theorem.

The count congruence has an elementary proof in the companion note.
This script checks the one-sided 16-atom local-signature minimum.
"""

from functools import lru_cache


@lru_cache(None)
def partitions(total, maximum):
    if total == 0:
        return ((),)
    return tuple(
        (head,) + rest
        for head in range(min(total, maximum), 0, -1)
        for rest in partitions(total - head, head)
    )


def signature(js):
    return tuple(
        sum(pow(j, -k, 1 << k) for j in js) % (1 << k)
        for k in range(1, 7)
    )


def main():
    assert all(pow(j, -4, 16) == 1 for j in range(1, 64, 2))
    assert all(pow(j, -6, 16) == (9 if j % 8 in (3, 5) else 1)
               for j in range(1, 64, 2))

    counts = {}
    for excess in (0, 4, 8, 12, 16):
        accepted = []
        for parts in partitions(excess, excess):
            if len(parts) > 16:
                continue
            js = (1,) * (16 - len(parts)) + tuple(2 * part + 1 for part in parts)
            if signature(js) == (0, 0, 0, 0, 0, 0):
                accepted.append(tuple(sorted(js)))
        counts[excess] = len(accepted)
        print(f"excess={excess} sum_j={16 + 2*excess} "
              f"mass={496 + 64*excess} zero_signatures={len(accepted)}")
        if excess == 16:
            assert (1,) * 12 + (3,) * 3 + (27,) in accepted
    assert counts == {0: 0, 4: 0, 8: 0, 12: 0, 16: 22}
    print("PASS: minimal local signature-zero 16-atom mass is 1520; 22 minimum profiles")


if __name__ == "__main__":
    main()
