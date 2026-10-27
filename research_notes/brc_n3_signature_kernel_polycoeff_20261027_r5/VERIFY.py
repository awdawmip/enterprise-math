"""Exact rational checker for the 2026-10-27 R5 policy-invariant signature gate.
External finite two-measure decision-tree model; no native Heartbeat simulation.
"""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product

HALF = F(1, 2)


def tree(params):
    """Build Q masses and LR labels, deriving every P mass as LR*Q."""
    nodes = {}
    def add(name, depth, mass, lr, anc):
        assert mass > 0 and lr > 0
        nodes[name] = dict(t=depth, q=mass, r=lr, anc=anc, kids=[])
    add('', 0, F(1), F(1), ())
    add('a', 1, F(1, 3), F(2), ('',))
    add('b', 1, F(2, 3), F(1, 2), ('',))
    nodes['']['kids'] = ['a', 'b']
    for name, rmid in [('a', F(7, 3)), ('b', F(1, 3))]:
        parent = nodes[name]
        for suffix, weight, r in [('u', F(1, 8), F(1)),
                                  ('v', F(1, 8), F(1)),
                                  ('w', F(3, 4), rmid)]:
            child = name + suffix
            add(child, 2, parent['q'] * weight, r, parent['anc'] + (name,))
            parent['kids'].append(child)
    likelihoods = (F(1, 2), F(1), F(3, 2))
    for name in ['au','av','bu','bv']:
        s = params[name]
        assert 0 < s < HALF
        par = nodes[name]
        for j, (r, prob) in enumerate(zip(likelihoods, (s, F(1)-2*s, s))):
            child = name + str(j)
            add(child, 3, par['q'] * prob, r, par['anc'] + (name,))
            par['kids'].append(child)
    for name in ['aw','bw']:
        par=nodes[name]
        child=name+'0'
        add(child,3,par['q'],par['r'],par['anc'] + (name,))
        par['kids'].append(child)
    for name,node in nodes.items():
        if node['kids']:
            assert sum((nodes[k]['q'] for k in node['kids']),F(0)) == node['q'], (name,'Q')
            assert sum((nodes[k]['q']*nodes[k]['r'] for k in node['kids']),F(0)) == node['q']*node['r'], (name,'P')
    assert sum((z['q'] for z in nodes.values() if z['t']==3), F(0)) == 1
    assert sum((z['q']*z['r'] for z in nodes.values() if z['t']==3), F(0)) == 1
    return nodes


def signature_data(nodes):
    """Return coefficient kernels indexed by (t, LR, ancestral coarse-signature)."""
    data=defaultdict(lambda:defaultdict(lambda: {'den':F(0),'num':defaultdict(F)}))
    for name,n in nodes.items():
        if not n['kids']:
            continue
        state=(n['t'],n['r'])
        sig=tuple((nodes[a]['t'], nodes[a]['r']) for a in n['anc'])
        d=data[state][sig]
        d['den'] += n['q']
        for ch in n['kids']:
            z=nodes[ch]
            d['num'][z['r']] += z['q']
    ans={}
    for state,by_sig in data.items():
        ans[state]={}
        for sig,v in by_sig.items():
            ker={r:q/v['den'] for r,q in v['num'].items()}
            assert sum(ker.values(), F(0))==1
            ans[state][sig]=ker
    return ans


def invariant(states):
    failures=[]
    for state, signatures in states.items():
        vals=list(signatures.values())
        if any(v != vals[0] for v in vals[1:]):
            failures.append(state)
    return failures


def conditional_kernel(nodes, ca, cb, target=(2,F(1))):
    weights=defaultdict(F)
    mass=F(0)
    continuation={ (0,F(1)): F(1), (1,F(2)): ca, (1,F(1,2)): cb }
    for name,n in nodes.items():
        if (n['t'],n['r'])!=target or not n['kids']:
            continue
        w=n['q']
        for a in n['anc']:
            s=(nodes[a]['t'],nodes[a]['r'])
            w *= continuation.get(s, F(1))
        mass+=w
        for child in n['kids']:
            weights[nodes[child]['r']] += w*nodes[child]['q']/n['q']
    assert mass>0
    return {r:w/mass for r,w in weights.items()}


def main():
    safe={'au':F(1,10),'av':F(2,5),'bu':F(1,5),'bv':F(3,10)}
    unsafe=dict(safe, bv=F(1,4))
    a,b=tree(safe),tree(unsafe)
    dsa,dun=signature_data(a),signature_data(b)
    assert len([n for n in a.values() if n['t']==3]) == 14
    assert len(a)==1+2+6+14
    assert invariant(dsa)==[], invariant(dsa)
    assert invariant(dun)==[(2,F(1))], invariant(dun)
    assert len(dsa[(2,F(1))])==2
    expected={F(1,2):F(1,4), F(1):F(1,2), F(3,2):F(1,4)}
    assert all(k==expected for k in dsa[(2,F(1))].values())
    expect_a=F(1,4); expect_b=F(9,40)
    by_signature=list(dun[(2,F(1))].items())
    assert {ker[F(1,2)] for sig,ker in by_signature}=={expect_a, expect_b}
    ka=conditional_kernel(b,F(1),F(1))
    kb=conditional_kernel(b,F(1),F(1,2))
    assert ka[F(1,2)] == F(7,30)
    assert kb[F(1,2)] == F(19,80)
    assert kb[F(1,2)]-ka[F(1,2)] == F(1,240)
    for x,y in product((F(1,3),F(2,3)), repeat=2):
        assert conditional_kernel(a,x,y)==expected
    kgrid={conditional_kernel(b,x,y)[F(1,2)] for x,y in product((F(1,3),F(2,3)),repeat=2)}
    assert len(kgrid)>1
    print('EXACT TREE: 23 nodes, 14 leaves; all branch Q/P masses positive and conserved: PASS')
    print('SAFE: all coarse-state ancestral-signature coefficient kernels agree: PASS')
    print('SAFE: collision (t=2, LR=1) common terminal K:', str(expected))
    print('UNSAFE: only noninvariant coarse state (2,1):', invariant(dun))
    print('UNSAFE: two signature outer probabilities:', sorted(str(x) for x in (expect_a,expect_b)))
    print('UNSAFE: K_(2,1)(LR3=1/2) at (x_a,x_b)=(1,1):',ka[F(1,2)])
    print('UNSAFE: K_(2,1)(LR3=1/2) at (1,1/2):',kb[F(1,2)])
    print('UNSAFE: exact difference:',kb[F(1,2)]-ka[F(1,2)])
    print('INTERIOR two-level grid: SAFE invariant; UNSAFE varying: PASS')
    print('ALL EXACT CHECKS PASSED')

if __name__=='__main__':
    main()
