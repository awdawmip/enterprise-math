"""Exact scalar edge, terminal weights, and composed maps of the C62 model."""
from fractions import Fraction as Q


def edge_parameters(r, c):
    """Yield (hidden count, tau, rho) for every legal next block 5^m 23."""
    K = 2*r+1
    h0_over_h2, h1_over_h2 = Q(1), Q(1)
    for m in range(c-1):
        y = c-m
        tau = h0_over_h2 * Q(28*(K+4*y)*(K+4*y-1), (4*K+y)*(K+y-1))
        rho = h1_over_h2 * Q(K+4*y, K+y)
        yield m, tau, rho
        h0_over_h2 *= Q(K+4*y, 4*(4*K+y))
        h1_over_h2 *= Q(K+4*y, 4*(K+y))


def terminal_weights(c):
    w0 = w1 = w2 = Q(1)
    for x in range(3, c+1):
        w0 *= Q(x, x+4)
        w1 *= Q(x, x+1)
        w2 *= Q(4*x, 4*x+1)
    return w0, w1, w2


def terminal_lower(c):
    w0, w1, w2 = terminal_weights(c)
    return w2*(7*w0+w1)/(7*w0+w2)**2


def transition_list(r, c, suffix):
    """Yield parameters for internal edges, and return the terminal inventory."""
    assert len(suffix) == r+1 and sum(suffix) == c-2
    steps = []
    for m in suffix[:-1]:
        _, tau, rho = next(edge for edge in edge_parameters(r, c) if edge[0] == m)
        steps.append((tau,rho))
        c -= m
        r -= 1
    assert r == 0 and c == suffix[-1]+2
    return steps, c


def word_tv(k, schedule):
    """Read u=0,1 forwards; return exact TV via the decreasing last coordinate."""
    steps, c = transition_list(k-1, k+1-schedule[0], schedule[1:])
    u, v = Q(0), Q(1)
    for tau, rho in steps:
        u, v = (tau/(tau+1+(rho-1)*x) for x in (u,v))
    w0, w1, w2 = terminal_weights(c)

    def third(x):
        return (1-x)*w2/(7*w0+x*w1+(1-x)*w2)

    return abs(third(u)-third(v))


def slope_range(r, c, suffix):
    """Exact min/max of |d p_last/du| for the entire suffix on [0,1]."""
    steps, c = transition_list(r, c, suffix)
    w0, w1, w2 = terminal_weights(c)
    p, q, h, t = -w2, w2, w1-w2, 7*w0+w2
    for tau, rho in reversed(steps):
        # Compose [[p,q],[h,t]] with [[0,tau],[rho-1,tau+1]].
        p, q, h, t = q*(rho-1), p*tau+q*(tau+1), t*(rho-1), h*tau+t*(tau+1)
    determinant = abs(p*t-q*h)
    return determinant/max(t,t+h)**2, determinant/min(t,t+h)**2


def standard_three(k):
    return ((1,)*(k-1)+(0,0), (1,)*(k-2)+(0,1,0), (1,)*(k-2)+(0,0,1))


def ordered_three(k):
    if k == 3:
        return ((1,1,0,0), (0,0,2,0), (0,1,1,0))
    return standard_three(k)
