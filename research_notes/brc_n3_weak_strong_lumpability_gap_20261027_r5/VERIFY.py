#!/usr/bin/env python3
"""Exact finite double-measure N=3 BRC coarse-vs-full test.
All computations use fractions.Fraction. No probabilistic/float optimizer.
"""
from fractions import Fraction as F
from itertools import product

u, gamma = F(3,4), F(11,200)
S = {'au':F(1,10),'av':F(2,5),'bu':F(1,5),'bv':F(3,10)}
root = {'a':(F(1,3),F(2)), 'b':(F(2,3),F(1,2))}
CH = {'a':[('au',F(1,8),F(1)),('av',F(1,8),F(1)),('aw',F(3,4),F(7,3))],
      'b':[('bu',F(1,8),F(1)),('bv',F(1,8),F(1)),('bw',F(3,4),F(1,3))]}
Y=[F(1,2),F(1),F(3,2)]

# Every node has unconditional Q mass, exact LR, depth and children.
nodes={'':{'q':F(1),'r':F(1),'t':0,'children':['a','b']}}
for h,(q,r) in root.items():
    nodes[h]={'q':q,'r':r,'t':1,'children':[c[0] for c in CH[h]]}
    for k,conditional,lr in CH[h]:
        qk=q*conditional
        suffixes = [(k+'0',S[k],Y[0]),(k+'1',1-2*S[k],Y[1]),(k+'2',S[k],Y[2])] if k in S else [(k+'0',F(1),lr)]
        nodes[k]={'q':qk,'r':lr,'t':2,'children':[v[0] for v in suffixes]}
        for leaf,w,ly in suffixes:
            nodes[leaf]={'q':qk*w,'r':ly,'t':3,'children':[]}

assert len([h for h in nodes if nodes[h]['t']==3])==14
assert len(nodes)==23
for h,n in nodes.items():
    assert n['q']>0 and n['r']>0
    if n['children']:
        assert sum((nodes[v]['q'] for v in n['children']),F(0))==n['q'],h
        assert sum((nodes[v]['q']*nodes[v]['r'] for v in n['children']),F(0))==n['q']*n['r'],h
assert sum((n['q'] for n in nodes.values() if n['t']==3),F(0))==1
assert sum((n['q']*n['r'] for n in nodes.values() if n['t']==3),F(0))==1

# Stopping decision with minimal e_P+u e_Q at a node:
# decide Q if LR<u, else decide P.
def score(policy, root_stop=False):
    result=[F(0) for _ in range(4)]
    def walk(h):
        node=nodes[h];q,r,t=node['q'],node['r'],node['t']
        if t==3 or (root_stop and t==0) or (t>0 and not policy(h)):
            if r<u: result[0]+=q*r # P makes error by deciding Q
            else: result[1]+=q # Q makes error by deciding P
            result[2]+=t*q*r
            result[3]+=t*q
        else:
            for child in node['children']:walk(child)
    walk('')
    return tuple(result)

def J(o): return o[0]+u*o[1]+gamma*o[3]

# Full policies: eight nonterminal histories. Real randomized minima are vertices.
full_states=('a','b','au','av','aw','bu','bv','bw')
full_min=None; full_arg=None; all_full=[]
for bits in product((0,1),repeat=len(full_states)):
    control=dict(zip(full_states,bits))
    o=score(lambda h: control[h])
    all_full.append(J(o))
    if full_min is None or J(o)<full_min:
        full_min,full_arg=J(o),(control,o)

# Seedless states: (1,2),(1,1/2),(2,1),(2,7/3),(2,1/3).
coarse_states=((1,F(2)),(1,F(1,2)),(2,F(1)),(2,F(7,3)),(2,F(1,3)))
seed_min=None; seed_arg=None; all_seed=[]
for bits in product((0,1),repeat=len(coarse_states)):
    control=dict(zip(coarse_states,bits))
    o=score(lambda h: control[(nodes[h]['t'],nodes[h]['r'])])
    all_seed.append(J(o))
    if seed_min is None or J(o)<seed_min:
        seed_min,seed_arg=J(o),(control,o)

assert full_min == F(379,600), (full_min,full_arg)
assert seed_min == F(1517,2400), (seed_min,seed_arg)
assert seed_min-full_min == F(1,2400)
assert full_arg[1] == (F(43,240),F(19,40),F(17,12),F(7,4)),full_arg
assert seed_arg[1] == (F(3,16),F(11,24),F(3,2),F(11,6)),seed_arg
assert J(full_arg[1])==full_min and J(seed_arg[1])==seed_min
assert min([F(3,4)]+all_full)==full_min
assert min([F(3,4)]+all_seed)==seed_min

def kernel(h):
    q=nodes[h]['q']
    return tuple(sum((nodes[z]['q']/q for z in nodes[h]['children'] if nodes[z]['r']==y),F(0)) for y in Y)
ka=tuple((kernel('au')[i]+kernel('av')[i])/2 for i in range(3))
kb=tuple((kernel('bu')[i]+kernel('bv')[i])/2 for i in range(3))
assert ka==kb==(F(1,4),F(1,2),F(1,4))
assert kernel('au')!=kernel('av') and kernel('bu')!=kernel('bv')
for x_a,x_b in product((F(1,3),F(2,3),F(1)),repeat=2):
    ar=nodes['au']['q']*x_a+nodes['av']['q']*x_a
    br=nodes['bu']['q']*x_b+nodes['bv']['q']*x_b
    assert ar>0 and br>0
    out=tuple((sum((x_a*nodes[h]['q']*kernel(h)[i] for h in ('au','av')),F(0))+
              sum((x_b*nodes[h]['q']*kernel(h)[i] for h in ('bu','bv')),F(0)))/(ar+br) for i in range(3))
    assert out==ka

def stop_value(h): return min(nodes[h]['r'],u)
def terminal(h): return stop_value(h)
def t2_value(h):
    return min(stop_value(h),gamma+sum((nodes[z]['q']/nodes[h]['q']*terminal(z) for z in nodes[h]['children']),F(0)))
def t1_value(h,which):
    return min(stop_value(h),gamma+sum((nodes[z]['q']/nodes[h]['q']*which(z) for z in nodes[h]['children']),F(0)))
DP_full=gamma+sum((nodes[h]['q']*t1_value(h,t2_value) for h in ('a','b')),F(0))
assert DP_full==full_min
def t2_shared(h,theta):
    return (1-theta)*stop_value(h)+theta*(gamma+sum((nodes[z]['q']/nodes[h]['q']*terminal(z) for z in nodes[h]['children']),F(0))) if nodes[h]['r']==1 else t2_value(h)
DP_seed=min(gamma+sum((nodes[h]['q']*t1_value(h,lambda z:t2_shared(z,theta)) for h in ('a','b')),F(0)) for theta in (0,1))
assert DP_seed==seed_min

print('SNAPSHOT: finite external Q/P probability tree, N=3, 23 nodes, 14 leaves')
print('OBJECTIVE: J=e_P+(3/4)e_Q+(11/200)E_Q(tau)')
print('POSITIVITY_NORMALIZATION_PQ_LR: PASS')
print('WEAK_SIGNATURE_INVARIANCE: K_a=K_b='+str(ka))
print('POINTWISE_STRONG_LUMPABILITY: FAIL (e.g. K_au='+str(kernel('au'))+', K_av='+str(kernel('av'))+')')
print('CONTINUATION_POLICY_TEST_GRID: PASS (9 positive rational pairs)')
print('FULL_DETERMINISTIC_POLICIES: '+str(len(all_full)))
print('SEEDLESS_DETERMINISTIC_POLICIES: '+str(len(all_seed)))
print('FULL_OPTIMAL_STOP_CONTROL: '+str(full_arg[0]))
print('SEEDLESS_OPTIMAL_STOP_CONTROL: '+str({str(k):v for k,v in seed_arg[0].items()}))
print('O_FULL='+str(full_arg[1]))
print('O_SEEDLESS='+str(seed_arg[1]))
print('V_FULL='+str(full_min))
print('V_SEEDLESS='+str(seed_min))
print('EXACT_SUPPORT_GAP='+str(seed_min-full_min))
print('BELLMAN_CROSSCHECK: PASS')
print('ROOT_OPTIONAL_STOP_CHECK: PASS; J_rootstop=3/4')
print('GLOBAL_REAL_RANDOM_POLICY_EXTREMA: guaranteed by depth-wise multi-affinity + Bayes decisions')
print('ALL EXACT CHECKS PASSED')
