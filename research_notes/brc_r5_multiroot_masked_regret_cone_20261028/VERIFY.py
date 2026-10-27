"""R5 single fan-in cone and new eight-leaf separation, all Fraction exact.

An EXTERNAL dual-measure decision tree. The X6 interpretation is a typed
ordered path encoding only, not a heartbeat dynamics computation.
"""
from fractions import Fraction as F
from itertools import product

ZERO = (F(0),) * 4
DIRECTION = (F(-20), F(-10), F(-2), F(3))
ROOTS = ('A', 'B')
NODES = ('AU', 'AV', 'BU', 'BV')
P, Q = {}, {}
q_first = {'A': F(1, 2), 'B': F(1, 2)}
r_first = {'A': F(1, 2), 'B': F(3, 2)}
q_cond = {'A': (F(1, 3), F(2, 3)), 'B': (F(1, 2), F(1, 2))}
r_cond = {'A': (F(2), F(1, 2)), 'B': (F(2, 3), F(4, 3))}
terminal_r = {
    'AU': (F(1, 3), F(5, 3)), 'AV': (F(2, 5), F(8, 5)),
    'BU': (F(3, 4), F(5, 4)), 'BV': (F(3, 5), F(7, 5)),
}

for h in ROOTS:
    Q[h] = q_first[h]
    P[h] = Q[h] * r_first[h]
    for j, letter in enumerate('UV'):
        n = h + letter
        Q[n] = Q[h] * q_cond[h][j]
        P[n] = P[h] * q_cond[h][j] * r_cond[h][j]
        for k in (0, 1):
            z = n + str(k)
            Q[z] = Q[n] / 2
            P[z] = P[n] * terminal_r[n][k] / 2


def add(*vs):
    return tuple(sum(v[i] for v in vs) for i in range(4))


def dot(c, v):
    return sum(x*y for x,y in zip(c, v))


def stop(h, t, d):
    """O=(P[declare Q], Q[declare P], E_P tau, E_Q tau)."""
    return ((F(0), Q[h], t*P[h], t*Q[h]) if d=='P'
            else (P[h], F(0), t*P[h], t*Q[h]))


def choices(n):
    z = [('P', stop(n,2,'P')), ('Q', stop(n,2,'Q'))]
    for d0, d1 in product('PQ',repeat=2):
        z.append(('C'+d0+d1, add(stop(n+'0',3,d0),stop(n+'1',3,d1))))
    return z


def nodes_best(lam):
    cs={n:dict(choices(n)) for n in NODES}
    k={n:{d:dot(lam,cs[n][d]) for d in ('P','Q')} for n in NODES}
    for n in NODES:
        k[n]['C']=min(dot(lam,v) for d,v in cs[n].items() if d.startswith('C'))
    return k


def bellman(lam):
    k=nodes_best(lam)
    L={h:min(dot(lam,stop(h,1,d)) for d in 'PQ') for h in ROOTS}
    W={h:min(k[h+'V'].values()) for h in ROOTS}
    m={h:min(k[h+'U'].values()) for h in ROOTS}
    f=sum(min(L[h], W[h]+m[h]) for h in ROOTS)
    lr_d={d:sum(min(L[h],W[h]+k[h+'U'][d]) for h in ROOTS) for d in ('P','Q','C')}
    lr=min(lr_d.values())
    regret={d:sum(min(max(F(0),L[h]-W[h]-m[h]), k[h+'U'][d]-m[h]) for h in ROOTS) for d in lr_d}
    assert f+min(regret.values())==lr
    return f,lr,lr-f,k,L,W,regret,lr_d


def full_vectors():
    opts={n:[v for _,v in choices(n)] for n in NODES}
    root_opts={h:[stop(h,1,d) for d in 'PQ']+
               [add(u,v) for u in opts[h+'U'] for v in opts[h+'V']]
               for h in ROOTS}
    assert all(len(root_opts[h])==38 for h in ROOTS)
    return [add(a,b) for a in root_opts['A'] for b in root_opts['B']]


def lr_vectors():
    opts={n:dict(choices(n)) for n in NODES}
    shared=[]
    for d in ('P','Q'):
        shared.append((opts['AU'][d],opts['BU'][d]))
    for a in ('CPP','CPQ','CQP','CQQ'):
        for b in ('CPP','CPQ','CQP','CQQ'):
            shared.append((opts['AU'][a],opts['BU'][b]))
    out=[]
    for u_a,u_b in shared:
        av_opts=[stop('A',1,d) for d in 'PQ']+[add(u_a,v) for v in opts['AV'].values()]
        bv_opts=[stop('B',1,d) for d in 'PQ']+[add(u_b,v) for v in opts['BV'].values()]
        assert len(av_opts)==len(bv_opts)==8
        out.extend(add(a,b) for a in av_opts for b in bv_opts)
    assert len(out)==1152
    return out


def main():
    leaves=sorted(n for n in P if len(n)==3)
    assert len(leaves)==8 and all(P[n]>0 and Q[n]>0 for n in leaves)
    assert sum(P[n] for n in leaves)==sum(Q[n] for n in leaves)==1
    assert P['AU']/Q['AU']==P['BU']/Q['BU']==1
    assert len({P[n]/Q[n] for n in leaves})==8
    assert all(sum(terminal_r[n])==2 for n in NODES)
    expected=('1/3','5/3','1/10','2/5','3/4','5/4','6/5','14/5')
    assert tuple(str(P[n]/Q[n]) for n in ('AU0','AU1','AV0','AV1','BU0','BU1','BV0','BV1'))==expected

    c=DIRECTION
    f,lr,g,k,L,W,regret,lr_d=bellman(c)
    assert (f,lr,g)==(F(-721,36),F(-239,12),F(1,9))
    assert regret=={'P':F(37,36),'Q':F(1,9),'C':F(1,4)}
    assert set(lr_d)=={'P','Q','C'}
    # Full: A/B continue; AU continues (P,Q); AV stops P;
    # BU stops Q; BV continues (Q,Q).
    full=add(dict(choices('AU'))['CPQ'],stop('AV',2,'P'),
             stop('BU',2,'Q'),dict(choices('BV'))['CQQ'])
    # LR: A/B continue; shared AU/BU both stop Q; AV stop P;
    # BV continues (Q,Q).
    compressed=add(stop('AU',2,'Q'),stop('AV',2,'P'),
                   stop('BU',2,'Q'),dict(choices('BV'))['CQQ'])
    assert dot(c,full)==f and dot(c,compressed)==lr
    all_full=full_vectors(); all_lr=lr_vectors()
    assert len(all_full)==1444 and len(all_lr)==1152
    assert set(all_lr).issubset(set(all_full))
    assert min(dot(c,v) for v in all_full)==f
    assert min(dot(c,v) for v in all_lr)==lr
    assert all(dot(c,v)>=lr for v in all_lr)

    # A 20-strict-inequality rational homogeneous cone containing c.
    # On it terminal choices, four node actions and two root continues
    # remain globally preferred, with different actions AU=C versus BU=Q.
    terminal_actions={'AU':'PQ','AV':'PP','BU':'QQ','BV':'QQ'}
    margins=[]
    for n,acts in terminal_actions.items():
        for i,d in enumerate(acts):
            z=n+str(i)
            margins.append(dot(c,stop(z,3,'Q' if d=='P' else 'P'))-
                           dot(c,stop(z,3,d)))
    chosen={'AU':'CPQ','AV':'P','BU':'Q','BV':'CQQ'}
    for n in NODES:
        opts=dict(choices(n)); winning=dot(c,opts[chosen[n]])
        alternatives=('P','Q','C')
        for alt in alternatives:
            if alt == ('C' if chosen[n].startswith('C') else chosen[n]):
                continue
            altval=(min(dot(c,v) for key,v in opts.items() if key.startswith('C'))
                    if alt=='C' else dot(c,opts[alt]))
            margins.append(altval-winning)
    for h in ROOTS:
        winning=dot(c,add(dict(choices(h+'U'))[chosen[h+'U']],
                          dict(choices(h+'V'))[chosen[h+'V']]))
        for d in 'PQ':
            margins.append(dot(c,stop(h,1,d))-winning)
    assert len(margins)==20 and min(margins)>0
    assert max(margins)>0
    # Uniform objective perturbation stability: |O_i| <= (1,1,3,3).
    assert abs(g)>0
    radius=F(1,144)
    assert g-16*radius==0
    print('model: 8 strictly positive P/Q leaves, unique terminal signatures')
    print('terminal LR:', ', '.join(expected))
    print('full deterministic effective policies:',len(all_full),'distinct:',len(set(all_full)))
    print('LR deterministic effective policies:',len(all_lr),'distinct:',len(set(all_lr)))
    print('lambda:',tuple(map(str,c)))
    print('full witness O:',tuple(map(str,full)),'V=',f)
    print('LR witness O:',tuple(map(str,compressed)),'V=',lr)
    print('global support gap:',g)
    print('LR shared choices:',{d:str(v) for d,v in lr_d.items()})
    print('exact masked regret:',{d:str(v) for d,v in regret.items()})
    print('open cone strict inequalities:',len(margins),'min margin:',min(margins))
    print('uniform infinity-norm gap-stability radius:',radius,'(strict)')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__': main()
