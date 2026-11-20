"""X6 R53: exact Fraction checks for a parametric sharp noise radius.

Typed carrier: previously derived R44/R47 conditional once-only named-triad
positive BRC root observer (F, FT, FF, FRF), common bias and per-channel
symmetric error. Does not check a native P000 release/reoccupation law.
"""
from fractions import Fraction as Q
from json import dumps
from pathlib import Path

P_MIN = Q(19, 2158)
P_MAX = Q(79, 378)


def vector(n, s, product):
    return (n * s, (n - 1) * s, 2 * (n*n - 1) * product, 2*n*product)


def contrast(n, a):
    x, y, d, h = a
    c = n*n - n - 1
    return (d - h) - c*((x - y) - (x - h)/n)


def norm(n):
    return Q(2) if n == 1 else Q(2*n*(n-1))


def witness(P):
    true = vector(4, Q(1), P)
    s5 = (81 - 42*P)/100
    p5 = (1 + 118*P)/200
    bias5 = (378*P - 29)/200
    competitor = tuple(v + bias5 for v in vector(5, s5, p5))
    eta = (19 + 42*P)/400
    center = tuple((a+b)/2 for a,b in zip(true, competitor))
    assert Q(0) < P and P < Q(1,4)
    assert s5 > 0 and p5 > 0 and s5*s5 - 4*p5 >= 0
    assert all(abs(a-c) == eta for a,c in zip(true,center))
    assert all(abs(b-c) == eta for b,c in zip(competitor,center))
    assert tuple(a-b for a,b in zip(true,competitor)) == (2*eta,-2*eta,-2*eta,2*eta)
    assert contrast(5, true) == -norm(5)*2*eta
    assert contrast(5, competitor) == 0
    # Strictly positive one-Port product: its (D-H) is negative,
    # while true four-Port (D-H)=22P>0. Two radius-eta boxes
    # cannot overlap when eta <= 11P/2.
    assert eta <= Q(11,2)*P
    # p=4, q=2 and q=3 universal contrast lower bounds;
    # for q >= 6, the lower bound increases from q=6.
    assert eta < Q(1,8) and eta < Q(5,72) and eta < Q(29,360)
    for n in range(2,1001):
        if n in (4,5):
            continue
        assert abs(contrast(n, true)) / (2 * norm(n)) > eta
    return {'P':str(P), 'eta':str(eta), 'rival_sum':str(s5),
            'rival_product':str(p5), 'rival_bias':str(bias5),
            'true':list(map(str,true)), 'rival_shifted':list(map(str,competitor)),
            'common_measurement':list(map(str,center))}


def run():
    assert Q(79,378)<Q(1,4)
    # Rival discriminant numerator is 1764 P^2 - 30404 P + 6361.
    # It decreases across the entire declared range and is positive
    # at the upper endpoint, so it is positive everywhere.
    f = lambda p: 1764*p*p - 30404*p + 6361
    assert f(P_MAX) == Q(47500,567) > 0
    assert 3528*P_MAX-30404 < 0
    assert (19+42*P_MIN)/400 == Q(11,2)*P_MIN
    assert (19+42*P_MAX)/400 == Q(5,72)
    cases=[P_MIN,Q(99,10000),Q(1,100)]
    cases += [P_MIN + (P_MAX-P_MIN)*Q(i,250) for i in range(1,250)]
    output = [witness(v) for v in cases]
    result={'name':'X6 R53 parametric globally optimal BRC four-channel ambiguity radius',
            'status':'PASS', 'scientific_scope':'conditional positive BRC root masses; not native P000 event dynamics',
            'interval':'[19/2158,79/378)',
            'exact_formula':'eta_crit(P)=(19+42*P)/400',
            'sample_count':len(output), 'checked_competitor_q':'q=2..1000 excluding p=4 and witness q=5',
            'unbounded_q_proof':'q>=6 lower bound >=29/360 from monotonicity',
            'samples':{'lower':output[0], 'R52':output[1], 'one_hundredth':output[2], 'near_upper':output[-1]}}
    here=Path(__file__).resolve().parent
    (here/'x6_r53_parametric_ambiguity_results.json').write_text(dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(dumps({k:v for k,v in result.items() if k!='samples'},ensure_ascii=False,indent=2))


if __name__=='__main__':
    run()
