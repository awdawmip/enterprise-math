"""Exact author checker for auxiliary R5 global 3-response no-go; not native X6."""
from fractions import Fraction as F
from itertools import product

ALPHA=(F(1,4),F(1,5)); KAPPA=(F(3,4),F(1,6))
LEAF={'A':(1,F(1)),'D':(2,F(1,2)),'Y':(2,F(3,2)),
      'C':(2,F(1)),'DH':(3,F(1,4)),'YH':(3,F(2)),
      'L':(3,F(1)),'L4':(4,F(1))}
FULL_KEYS=('A','D','Y','LD','LY','LC')
LR_KEYS=('A','D','Y','L')
WITNESS=(1,1,0,1,0,1,0,0,0,0,0,0)
RANK_POLICIES=((0,0,0,0),(1,0,0,0),(1,0,0,1),(1,0,1,0),(1,1,0,0))

def leaf_flows(actions):
    flow={name:F(0) for name in LEAF}
    for i,(a,k) in enumerate(zip(ALPHA,KAPPA)):
        decisions=actions[i]; o=F(1,2)
        if not decisions['A']:
            flow['A']+=o; continue
        d=y=o*a; c=o*(1-2*a)
        if decisions['D']:
            flow['DH']+=d*F(2,3)
            flow['L4' if decisions['LD'] else 'L']+=d/3
        else: flow['D']+=d
        if decisions['Y']:
            flow['YH']+=y/2
            flow['L4' if decisions['LY'] else 'L']+=y/2
        else: flow['Y']+=y
        flow['C']+=c*(1-k)
        flow['L4' if decisions['LC'] else 'L']+=c*k
    assert sum(flow.values())==1
    assert sum(m*LEAF[t][1] for t,m in flow.items())==1
    assert all(m>=0 for m in flow.values())
    return flow

def full(bits):
    return leaf_flows([dict(zip(FULL_KEYS,bits[6*i:6*i+6])) for i in (0,1)])

def lr(bits):
    b=dict(zip(LR_KEYS,bits))
    return leaf_flows([dict((n,b['L' if n.startswith('L') else n]) for n in FULL_KEYS)]*2)

def feature(flow):
    tq=sum(m*LEAF[name][0] for name,m in flow.items())
    tp=sum(m*LEAF[name][0]*LEAF[name][1] for name,m in flow.items())
    x,y,u=flow['DH'],flow['L4'],flow['YH']
    assert tp-tq==u-F(3,4)*x
    return (x,y,u,tq)

def observe(ft,v,w,z):
    x,y,u,tq=ft
    return (F(1,2)+v*x/4+w*y+2*z*u,
            F(1,2)+v*x+w*y+z*u,
            tq+u-F(3,4)*x,tq)

def inverse(o,v,w,z):
    assert w!=0 and z!=v
    ep,eq,tp,tq=o
    x=F(4,3)*(ep-eq-z*(tp-tq))/(z-v)
    u=tp-tq+F(3,4)*x
    y=(eq-F(1,2)-v*x-z*u)/w
    return (x,y,u,tq)

def sep(ft):
    x,y,u,tq=ft
    return F(985,8)*x+70*y-130*u-23*tq

def det4(rows):
    a=[list(r) for r in rows]; result=F(1)
    for j in range(4):
        k=next((k for k in range(j,4) if a[k][j]),None)
        if k is None: return F(0)
        if j!=k:
            a[j],a[k]=a[k],a[j]; result=-result
        pivot=a[j][j]; result*=pivot
        for i in range(j+1,4):
            fac=a[i][j]/pivot
            for c in range(j,4):
                a[i][c]-=fac*a[j][c]
    return result

def differences(rows):
    base=rows[0]
    return [tuple(r[j]-base[j] for j in range(4)) for r in rows[1:]]

def main():
    assert [(1+k*(1-2*a))/a for a,k in zip(ALPHA,KAPPA)]==[F(11,2)]*2
    lrf={b:feature(lr(b)) for b in product((0,1),repeat=4)}
    fullf={b:feature(full(b)) for b in product((0,1),repeat=12)}
    assert len(lrf)==16 and len(fullf)==4096
    dfeat=det4(differences([lrf[b] for b in RANK_POLICIES]))
    assert dfeat==-F(50787,10240000)
    table=[sep(ft) for b,ft in lrf.items() if b[0]==1]
    assert table==[-F(4117,80),-F(403,10),-F(5701,80),-F(877,16),
                   -F(6107,160),-F(3757,160),-F(1855,32),-F(6079,160)]
    assert max(sep(ft) for ft in lrf.values())==-23
    f=fullf[WITNESS]
    assert f==(F(1,12),F(11,48),F(0),F(49,24))
    assert sep(f)==-F(661,32)
    assert sep(f)-max(sep(ft) for ft in lrf.values())==F(75,32)
    cases=((F(1,8),F(1,4),F(0)),(F(1,8),F(1,4),F(1,8)),
           (F(1,8),F(0),F(1,4)),(F(0),F(1,4),F(1,4)),
           (F(1,2),-F(1,2),-F(1,2)),(-F(1,2),F(1,3),F(1,2)),
           (F(0),F(1,4),F(0)))
    for v,w,z in cases:
        assert all(-F(1,2)<=t<=F(1,2) for t in (v,w,z))
        d=det4(differences([observe(lrf[b],v,w,z) for b in RANK_POLICIES]))
        assert d==dfeat*F(3,4)*w*(z-v)
        if w*(z-v):
            for ft in lrf.values():
                assert inverse(observe(ft,v,w,z),v,w,z)==ft
            assert inverse(observe(f,v,w,z),v,w,z)==f
            assert sep(inverse(observe(f,v,w,z),v,w,z))-max(
                sep(inverse(observe(ft,v,w,z),v,w,z)) for ft in lrf.values()
            )==F(75,32)
        print(f'CASE v={v} w={w} z={z} rank_minor={d} full_rank={bool(w*(z-v))}')
    print(f'LR_FEATURE_RANK_MINOR={dfeat}')
    print('UNIVERSAL_TIME_IDENTITY: TP-TQ=u-3*x/4 for 4096 FULL and 16 LR policies')
    print('OBSERVATION_JACOBIAN=3*w*(z-v)/4')
    print('LR_OBSERVATION_MINOR=-152361*w*(z-v)/40960000')
    print(f'LR_FEATURE_MAX=-23; FULL_WITNESS_FEATURE={f}; FULL_VALUE={sep(f)}; GAP=75/32')
    print('RANK4_IFF w*(z-v)!=0; ELSE_RANK<=3')
    print('PASS_EXACT_R5_GLOBAL_THREE_RESPONSE_OBSERVER_NO_GO')

if __name__=='__main__': main()
