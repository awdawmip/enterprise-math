"""Exact author-side verification for R5 independent P/Q post-K2 time forks."""
from fractions import Fraction as F
from itertools import product

C = F(2, 3)
ALPHA = (F(1, 2), F(2, 3), F(1, 2), F(3, 4))
WSTAR = (F(1, 8), F(1, 6), F(1, 16), F(3, 32))
ZERO, ONE = F(0), F(1)
checks = 0


def assert_eq(a, b):
    global checks
    assert a == b, (a, b)
    checks += 1


def observer(x, bctl, ictl, zs, ts, ps, qs, aa, bb, lr=False):
    x, bctl, ictl = F(x), F(bctl), F(ictl)
    if lr:
        # bctl is shared upstream y; i=(1-x)*y; z and t are shared.
        imass = (1 - x) * bctl
        zs, ts = (F(zs),) * 4, (F(ts),) * 4
    else:
        imass = (1 - x) * ictl
    bmass = bctl
    w = (F(1, 4), (1-x)/4, bmass/8, imass/8)
    qflow = tuple(w[k]*ALPHA[k]*F(zs[k]) for k in range(4))
    sflow = tuple(C*qflow[k]*F(ts[k]) for k in range(4))
    d = bmass/16 + 3*imass/32
    r1, r2 = sum(qflow), sum(sflow)
    ep = F(107,128) - 21*x/128 + d/4 - sum(ps[k]*sflow[k] for k in range(4))
    eq = F(13,64) + 3*x/64 - d/2 + sum(qs[k]*sflow[k]/4 for k in range(4))
    tp = 3 + r1 + r2 + sum(aa[k]*sflow[k] for k in range(4))
    tq = 3 + r1/2 + r2/4 + sum(bb[k]*sflow[k]/4 for k in range(4))
    return (ep,eq,tp,tq), (r1,r2,d,qflow,sflow)


def all_full(ps, qs, aa, bb):
    for x,bc,ic in product((0,1), repeat=3):
        for bits in product((0,1), repeat=8):
            yield observer(x,bc,ic,bits[:4],bits[4:],ps,qs,aa,bb)


def all_lr(ps, qs, aa, bb):
    for x,y,z,t in product((0,1), repeat=4):
        yield observer(x,y,0,z,t,ps,qs,aa,bb,lr=True)


def dot(n, o):
    return sum(n[k]*o[k] for k in range(4))


def time_normal_gap(ps,qs,aa,bb):
    n=(ZERO,ZERO,-ONE,F(4))
    f=max(dot(n,v[0]) for v in all_full(ps,qs,aa,bb))
    l=max(dot(n,v[0]) for v in all_lr(ps,qs,aa,bb))
    deltas=[bb[s]-aa[s] for s in range(4)]
    a=sum(WSTAR)
    pos=sum(WSTAR[s]*max(ZERO,deltas[s]) for s in range(4))
    tot=sum(WSTAR[s]*deltas[s] for s in range(4))
    hf=9+a+C*pos
    hl=9+a+C*max(ZERO,tot)
    assert_eq(f,hf)
    assert_eq(l,hl)
    assert_eq(f-l,C*(pos-max(ZERO,tot)))
    assert_eq(f-l,C*min(pos,pos-tot))
    return f-l


def paired_example(low,high):
    aa=(low,high,low,high)
    bb=aa
    ps=tuple((ONE+r)/4 for r in aa)
    qs=ps
    avg=(18*low+25*high)/43
    k=C*(ONE+avg)
    n=(ZERO,ZERO,2+k,-4*(ONE+k))
    lr=list(all_lr(ps,qs,aa,bb))
    full=list(all_full(ps,qs,aa,bb))
    hf=max(dot(n,o) for o,_ in full)
    hl=max(dot(n,o) for o,_ in lr)
    expected=F(25,344)*(high-low)
    assert_eq(hf-hl,expected)
    assert_eq(hl,-6-9*k)
    # Exact global LR inequality G<=k*R1.
    for o,(r1,r2,d,qflow,sflow) in lr:
        g=sum((ONE+aa[s])*sflow[s] for s in range(4))
        assert_eq(g-k*r1 <= 0,True)
    # The entire FULL exposed K2 face for n0 maps to the LR segment.
    total=sum(WSTAR[s]*(ONE+aa[s]) for s in range(4))
    for ts in product((0,1),repeat=4):
        obj,_=observer(0,1,1,(1,1,1,1),ts,ps,qs,aa,bb)
        t=sum(WSTAR[s]*(ONE+aa[s])*ts[s] for s in range(4))/total
        image,_=observer(0,1,0,1,t,ps,qs,aa,bb,lr=True)
        assert_eq(obj,image)
    return ps,qs,aa,bb,n,expected


def main():
    half=(F(1,2),)*4
    mixed_a=(F(3,8),F(5,8),F(3,8),F(5,8))
    mixed_b=(F(5,8),F(3,8),F(5,8),F(3,8))
    tests=[
      (half,half,mixed_a,mixed_b,F(1,32)),
      (half,half,(F(1,16),F(1,32),F(3,32),F(1,8)),(F(1,8),F(1,16),F(3,16),F(1,4)),ZERO),
      (half,half,(F(1,4),F(1,3),F(1,2),F(2,3)),(F(3,4),F(1,2),F(1,4),F(1,3)),None),
      (half,half,(F(1,3),)*4,(F(1,3),)*4,ZERO)
    ]
    for ps,qs,aa,bb,want in tests:
        gap=time_normal_gap(ps,qs,aa,bb)
        if want is not None: assert_eq(gap,want)
    for low,high in ((F(1,4),F(1,2)),(F(1,8),F(2,3)),(F(1,3),F(3,4))):
        ps,qs,aa,bb,n,gap=paired_example(low,high)
        assert_eq(time_normal_gap(ps,qs,aa,bb),ZERO)
    ps,qs,aa,bb,n,gap=paired_example(F(1,4),F(1,2))
    witness,aux=observer(0,1,1,(0,1,0,1),(0,1,0,1),ps,qs,aa,bb)
    assert_eq(witness,(F(311,384),F(217,1536),F(169,48),F(409,128)))
    assert_eq(dot(n,witness),max(dot(n,o) for o,_ in all_full(ps,qs,aa,bb)))
    assert_eq(gap,F(25,1376))
    assert_eq(gap/sum(abs(v) for v in n),F(25,14656))
    # Test nonbinary real behavioural strategies on the compensated face.
    total=sum(WSTAR[s]*(ONE+aa[s]) for s in range(4))
    for j in range(1,121):
        ts=tuple(F((j*(s+2)+3*s)%29,29) for s in range(4))
        fv,_=observer(0,1,1,(1,)*4,ts,ps,qs,aa,bb)
        t=sum(WSTAR[s]*(ONE+aa[s])*ts[s] for s in range(4))/total
        lv,_=observer(0,1,0,1,t,ps,qs,aa,bb,lr=True)
        assert_eq(fv,lv)
    print('FULL_DETERMINISTIC_PER_KERNEL=2048')
    print('LR_DETERMINISTIC_PER_KERNEL=16')
    print('MIXED_TIME_SUPPORT_GAP=1/32')
    print('PAIRED_FACE_EQUAL_GLOBAL_GAP=25/1376')
    print('PAIRED_FULL_WITNESS='+str(witness))
    print('PAIRED_LINF_DISTANCE_LOWER=25/14656')
    print('EXACT_ASSERTIONS='+str(checks))
    print('PASS_EXACT_R5_INDEPENDENT_DELAY_EXPOSED_FACE_AND_GLOBAL_GAP')

if __name__=='__main__':
    main()
