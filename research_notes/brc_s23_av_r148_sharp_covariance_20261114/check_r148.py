"""R148: exact rational verification of sharp CRT covariance and first positive length."""
from collections import Counter
from fractions import Fraction as Q
from math import gcd, lcm

def floor(q):
    return q.numerator // q.denominator

def ceil(q):
    return -floor(-q)

def support(w):
    s = [0]
    for digit in w:
        s.append(s[-1] + int(digit))
    m = len(w)
    alpha, beta = Q(0), Q(1)
    for i in range(m):
        for j in range(i + 1, m + 1):
            alpha = max(alpha, Q(s[j] - s[i] - 1, j - i))
            beta = min(beta, Q(s[j] - s[i] + 1, j - i))
    if alpha >= beta:
        return None
    a, b, c, d = alpha.numerator, alpha.denominator, beta.numerator, beta.denominator
    U = min(b * (s[j] + 1) - j * a for j in range(m + 1))
    V = max(d * s[j] - j * c for j in range(m + 1))
    return a, b, c, d, U, V

def covariance(a, b, c, d, U, V):
    g = gcd(b, d)
    mid = Q(g - 1, 2)
    gamma = sum(((Q((a*t-U) % g) - mid) * (Q((V-c*t) % g) - mid)
                 for t in range(g)), Q(0)) / (g*b*d)
    bound = Q(g*g - 1, 12*b*d)
    assert abs(gamma) <= bound
    if g > 1:
        positive = (a+c) % g == 0 and (U+V) % g == 0
        negative = (a-c) % g == 0 and (V-U+1) % g == 0
        assert (gamma == bound) == positive
        assert (gamma == -bound) == negative
    return g, gamma, bound

def direct_covariance(a, b, c, d, U, V):
    P = lcm(b, d)
    xs, etas = [], []
    for L in range(1, P + 1):
        A, B = Q(L*a-U, b), Q(L*c-V, d)
        C = ceil(B) - floor(A) - 1
        x, y = (L*a-U) % b, (L*c-V) % d
        eta = Q(0) if y == 0 else 1-Q(y, d)
        assert Q(C) - L*(Q(c,d)-Q(a,b)) == (Q(U,b)-Q(V,d)-1+Q(x,b)+eta)
        xs.append(Q(x,b)); etas.append(eta)
    meanx = sum(xs, Q(0))/P
    meany = sum(etas, Q(0))/P
    return sum(((x-meanx)*(y-meany) for x,y in zip(xs,etas)), Q(0))/P

def main():
    stats = Counter()
    positives = []
    for m in range(1, 16):
        for n in range(1 << m):
            w = format(n, f'0{m}b')
            p = support(w)
            if p is None:
                continue
            g, gamma, bound = covariance(*p)
            assert direct_covariance(*p) == gamma
            stats['words'] += 1
            stats['noncoprime'] += g > 1
            stats['positive'] += gamma > 0
            stats['negative'] += gamma < 0
            if gamma > 0:
                positives.append((m, w, p, str(gamma)))
    assert stats == Counter({'words':1906,'noncoprime':298,'negative':292,'positive':6})
    assert min(p[0] for p in positives) == 14
    assert positives[0] == (14,'00001000010000',(1,6,3,14,2,0),'1/336')

    param_checks = 0
    for b in range(1, 9):
        for d in range(1, 9):
            g = gcd(b,d)
            for a in range(b):
                if gcd(a,b) != 1: continue
                for c in range(1, d+1):
                    if gcd(c,d) != 1 or a*d >= b*c: continue
                    for U in range(g):
                        for V in range(g):
                            covariance(a,b,c,d,U,V)
                            param_checks += 1
    assert param_checks == 1765
    print('R148_SHARP_CRT_COVARIANCE_PASS')
    print({'word_lengths':'1..15',**dict(stats),'parameter_checks':param_checks,
           'first_positive':positives[0],'all_positive':positives})

if __name__ == '__main__':
    main()
