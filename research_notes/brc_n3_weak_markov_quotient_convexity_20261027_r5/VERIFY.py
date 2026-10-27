"""Exact external finite probability audit; not native BRC/Heartbeat execution."""
from fractions import Fraction as F

R = (F(1, 2), F(1), F(3, 2))
Y = (F(1, 4), F(1), F(2))
QH = {'a': F(1, 2), 'b': F(1, 2)}
QR = {'a': (F(1, 4), F(1, 2), F(1, 4)),
      'b': (F(1, 3), F(1, 3), F(1, 3))}
MU = {R[0]: (F(5, 7), F(1, 4), F(1, 28)),
      R[1]: (F(15, 28), F(1, 16), F(45, 112)),
      R[2]: (F(1, 28), F(7, 16), F(59, 112))}
BAR = {r: sum(QH[h] * QR[h][i] for h in QH) for i, r in enumerate(R)}

# Policy: probabilities (continue, decide-Q) at root, t1 and each t2 r;
# t3 maps terminal y to probability decide-Q. Remainder means decide-P.
A = ((F(1), F(0)), (F(1, 2), F(0)),
     {r: x for r, x in zip(R, ((F(1, 3), F(1, 5)),
                                (F(2, 5), F(1, 3)),
                                (F(3, 4), F(1, 7))))},
     {y: x for y, x in zip(Y, (F(3, 4), F(1, 6), F(2, 9)))})
B = ((F(2, 3), F(1, 3)), (F(4, 5), F(1, 10)),
     {r: x for r, x in zip(R, ((F(4, 5), F(1, 10)),
                                (F(1, 4), F(1, 2)),
                                (F(1, 2), F(1, 4))))},
     {y: x for y, x in zip(Y, (F(1, 3), F(2, 5), F(5, 6)))})


def checks():
    assert QH['a'] == QH['b'] == F(1, 2)
    assert QR['a'] != QR['b']
    assert sum(BAR.values()) == 1
    assert sum(r * BAR[r] for r in R) == 1
    for h in QH:
        assert all(x > 0 for x in QR[h])
        assert sum(QR[h]) == sum(r * QR[h][i] for i, r in enumerate(R)) == 1
    for r in R:
        assert all(x > 0 for x in MU[r]) and sum(MU[r]) == 1
        assert sum(y * MU[r][i] for i, y in enumerate(Y)) == r
    # A previously published non-convex-order example is reused as input.
    call = lambda r: sum(MU[r][i] * max(y - 1, 0) for i, y in enumerate(Y))
    assert call(R[1]) - (call(R[0]) + call(R[2])) / 2 == F(27, 224)


def occupancy(policy):
    (root_c, root_q), (first_c, first_q), at2, at3 = policy
    def split(mass, c, q):
        assert c >= 0 and q >= 0 and c + q <= 1
        return (mass * c, mass * q, mass * (1 - c - q))
    flows = {'root': split(F(1), root_c, root_q)}
    flows['first'] = split(flows['root'][0], first_c, first_q)
    for r in R:
        flows[('second', r)] = split(flows['first'][0] * BAR[r], *at2[r])
    for i, y in enumerate(Y):
        incoming = sum(flows[('second', r)][0] * MU[r][i] for r in R)
        flows[('terminal', y)] = split(incoming, F(0), at3[y])
    return flows


def observe_flows(flows):
    lr = {'root': F(1), 'first': F(1)}
    lr.update({('second', r): r for r in R})
    lr.update({('terminal', y): y for y in Y})
    err_p = sum(lr[s] * (flow[1]) for s, flow in flows.items())
    err_q = sum(flow[2] for flow in flows.values())
    c0, c1 = flows['root'][0], flows['first'][0]
    tau_p = c0 + c1 + sum(r * flows[('second', r)][0] for r in R)
    tau_q = c0 + c1 + sum(flows[('second', r)][0] for r in R)
    return (err_p, err_q, tau_p, tau_q)


def observe_tree(policy):
    """Independent direct history-by-history P/Q terminal measure summation."""
    (rc, rq), (fc, fq), at2, at3 = policy
    acc = [F(0), F(0), F(0), F(0)]
    def action(depth, p, q, c, dq):
        assert 0 <= c and 0 <= dq and c + dq <= 1
        dp = 1 - c - dq
        acc[0] += p * dq
        acc[1] += q * dp
        acc[2] += depth * p * (dp + dq)
        acc[3] += depth * q * (dp + dq)
        return c
    c = action(0, F(1), F(1), rc, rq)
    for h in QH:
        q1, p1 = c * QH[h], c * QH[h]
        c1 = action(1, p1, q1, fc, fq)
        for i, r in enumerate(R):
            q2 = c1 * q1 * QR[h][i]
            p2 = c1 * p1 * QR[h][i] * r
            assert p2 == r * q2
            c2, dq2 = at2[r]
            c2 = action(2, p2, q2, c2, dq2)
            for j, y in enumerate(Y):
                q3 = c2 * q2 * MU[r][j]
                p3 = c2 * p2 * MU[r][j] * y / r
                assert p3 == y * q3
                action(3, p3, q3, F(0), at3[y])
    return tuple(acc)


def lift(flows):
    """Construct seedless time/LR policy from convex-combined Q action flows."""
    def divide(flow, total):
        if total == 0:
            assert all(v == 0 for v in flow)
            return (F(0), F(0))
        return (flow[0] / total, flow[1] / total)
    root = divide(flows['root'], F(1))
    first = divide(flows['first'], flows['root'][0])
    at2 = {r: divide(flows[('second', r)],
                     flows['first'][0] * BAR[r]) for r in R}
    at3 = {}
    for y in Y:
        f = flows[('terminal', y)]
        total = f[1] + f[2]
        at3[y] = f[1] / total if total else F(0)
    return root, first, at2, at3


def main():
    checks()
    fa, fb = occupancy(A), occupancy(B)
    va, vb = observe_flows(fa), observe_flows(fb)
    assert va == observe_tree(A)
    assert vb == observe_tree(B)
    mixed = {s: tuple((fa[s][j] + fb[s][j]) / 2 for j in range(3))
             for s in fa}
    C = lift(mixed)
    fc = occupancy(C)
    assert fc == mixed
    vc = observe_flows(fc)
    assert vc == observe_tree(C)
    assert vc == tuple((a + b) / 2 for a, b in zip(va, vb))
    print('input checks: PASS')
    print('direct full-tree vs occupation flow for A, B, lift: PASS')
    print('convex mixture exact flow recovery: PASS')
    print('O(A) =', va)
    print('O(B) =', vb)
    print('O(average) =', vc)
    print('lifted root (continue, decideQ) =', C[0])
    print('lifted t1 (continue, decideQ) =', C[1])
    print('lifted t2 [(r,continue,decideQ)] =',
          [(r, *C[2][r]) for r in R])
    print('lifted t3 [(y,decideQ)] =', [(y, C[3][y]) for y in Y])
    print('CONCLUSION: PASS (one exact constructive witness, not universal enumeration)')


if __name__ == '__main__':
    main()
