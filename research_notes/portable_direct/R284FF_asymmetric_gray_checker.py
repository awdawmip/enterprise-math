"""Exact finite checks for asymmetric persistent omission budgets in Gray-group publication.

All arithmetic is integer/bitmask. This is an independent finite cross-check of the
analytic threshold K(q_down,q_up,u)=q_down+q_up+4*u+1, not a global coding theorem.
"""
import json
from itertools import product
from pathlib import Path


def ball(word, n, u):
    """All binary words at Hamming distance <= u."""
    return [x for x in range(1 << n) if (x ^ word).bit_count() <= u]


def check(q_down, q_up, u):
    n = q_down + q_up + 4*u + 1
    s0 = {x for x in range(1 << n) if x.bit_count() <= q_down}
    s1 = {x for x in range(1 << n) if (n - x.bit_count()) <= q_up}
    o0 = {x for x in range(1 << n) if x.bit_count() <= q_down + u}
    o1 = {x for x in range(1 << n) if x.bit_count() >= n - q_up - u}
    assert o0.isdisjoint(o1)
    read_checks = 0
    prefix_states = 0
    for x in range(1 << n):
        is0 = False
        is1 = False
        for y in ball(x, n, u):
            read_checks += 1
            if y in o0:
                is0 = True
            if y in o1:
                is1 = True
            if x in s0:
                assert y in o0 and y not in o1, (q_down,q_up,u,'stable0',x,y)
            if x in s1:
                assert y in o1 and y not in o0, (q_down,q_up,u,'stable1',x,y)
        assert not(is0 and is1), (q_down,q_up,u,'rollback',x)
        prefix_states += 1
        assert is0 == (x.bit_count() <= q_down+2*u)
        assert is1 == (x.bit_count() >= n-q_up-2*u)
    m=n-1
    om0={y for y in range(1<<m) if y.bit_count() <= q_down+u}
    om1={y for y in range(1<<m) if y.bit_count() >= m-q_up-u}
    witness=None
    for x in range(1<<m):
        bs=ball(x,m,u)
        y0=next((y for y in bs if y in om0),None)
        y1=next((y for y in bs if y in om1),None)
        if y0 is not None and y1 is not None:
            witness={'physical_word':x,'old_read':y0,'new_read':y1,
                'prefix_successful_writes':x.bit_count(),
                'old_read_corruptions':(x^y0).bit_count(),
                'new_read_corruptions':(x^y1).bit_count()}
            break
    assert witness is not None, (q_down,q_up,u,'missing lower witness')
    return dict(q_down=q_down,q_up=q_up,u=u,min_group_bits=n,
                tested_prefix_states=prefix_states,tested_readings=read_checks,
                one_bit_short_witness=witness)


def main():
    cases=[check(a,b,u) for a,b,u in product(range(3),range(3),range(2))]
    widths={"group0":1+2+4*1+1,"group1":0+0+4*1+1}
    assert widths == {'group0':8,'group1':5}
    assert sum(widths.values())==13
    uniform_baseline = 2*(2*2+4*1+1)
    assert uniform_baseline==18
    cert={"schema":"R284FF_ASYMMETRIC_GRAY_FINITE_CHECK_V1",
          "date":"2026-11-23", "model":"separable complete group flip; per-direction omission budgets; independent <=u read flips; stateless bitgroup decoder",
          "tested_cases":len(cases),
          "total_prefix_states":sum(c['tested_prefix_states'] for c in cases),
          "total_reading_checks":sum(c['tested_readings'] for c in cases),
          "all_assertions_passed":True,
          "four_cycle_example":{"edges":["00->01","01->11","11->10","10->00"],"omissions":[2,0,1,0],"u":1,"group_widths":widths,"total_bits":13,"uniform_max_budget_bits":uniform_baseline},
          "cases":cases}
    destination=Path(__file__).with_name('R284FF_asymmetric_gray_certificate.json')
    destination.write_text(json.dumps(cert,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in cert.items() if k!='cases'},ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
