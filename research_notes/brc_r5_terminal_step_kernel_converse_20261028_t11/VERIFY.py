from fractions import Fraction as F
from itertools import product

q = {
    ('A', F(1,2)): F(1,8),
    ('A', F(1)):   F(1,4),
    ('A', F(3,2)): F(1,8),
    ('B', F(1,2)): F(1,16),
    ('B', F(1)):   F(3,8),
    ('B', F(3,2)): F(1,16),
}
p = {(h,y): mass*y for (h,y),mass in q.items()}
assert len(q) == 6 and all(v>0 for v in q.values())
assert sum(q.values()) == sum(p.values()) == 1
assert all(sum(q[(h,y)] for y in (F(1,2),F(1),F(3,2))) == F(1,2) for h in 'AB')
assert all(sum(p[(h,y)] for y in (F(1,2),F(1),F(3,2))) == F(1,2) for h in 'AB')
Y=(F(1,2),F(1),F(3,2))
K = {h: tuple(q[(h,y)] / F(1,2) for y in Y) for h in 'AB'}
assert K['A'] == (F(1,4),F(1,2),F(1,4))
assert K['B'] == (F(1,8),F(3,4),F(1,8))
assert all(sum(k*y for k,y in zip(K[h],Y))==1 for h in 'AB')

def O(policy):
    eP=eQ=tP=tQ=F(0)
    for h in 'AB':
        stage1, terminal=policy[h]
        if stage1!='C':
            eP += F(stage1=='Q')*F(1,2)
            eQ += F(stage1=='P')*F(1,2)
            tP += F(1,2)
            tQ += F(1,2)
        else:
            for y,a in zip(Y,terminal):
                eP += F(a=='Q')*p[(h,y)]
                eQ += F(a=='P')*q[(h,y)]
                tP += 2*p[(h,y)]
                tQ += 2*q[(h,y)]
    return eP,eQ,tP,tQ

C=[('C',dec) for dec in product('PQ',repeat=3)]
choices=[('P',None),('Q',None)]+C
full=[O(dict(zip('AB',acts))) for acts in product(choices,repeat=2)]
lr=[O({'A':act,'B':act}) for act in choices]
k=F(3,32)
J=lambda x:x[0]+x[1]+k*x[3]
full_val=min(map(J,full));lr_val=min(map(J,lr))
assert len(full)==100 and len(lr)==10
assert full_val==F(69,64) and lr_val==F(70,64)
assert lr_val-full_val==F(1,64)
witness=O({'A':('C',('Q','P','P')),'B':('P',None)})
assert witness==(F(1,16),F(7,8),F(3,2),F(3,2))
assert J(witness)==full_val

def gain(h,z):
    return min(F(1),z)-sum(kh*min(y,z) for kh,y in zip(K[h],Y))
gA,gB=gain('A',F(1)),gain('B',F(1))
assert (gA,gB)==(F(1,8),F(1,16))
assert k==(gA+gB)/2
jensen=(max(gA-k,0)+max(gB-k,0))/2-max((gA+gB)/2-k,0)
assert jensen==lr_val-full_val==F(1,64)
assert len(set(full))>=len(set(lr))
print('SIX_POSITIVE_LEAVES',len(q))
print('P_Q_NORMALIZED',sum(p.values()),sum(q.values()))
print('CONDITIONAL_Q_KERNELS',K)
print('BELLMAN_GAINS',gA,gB)
print('STOPPING_PRICE',k)
print('DETERMINISTIC_FULL_LR_POLICIES',len(full),len(lr))
print('WITNESS_O',witness)
print('MIN_FULL',full_val)
print('MIN_LR',lr_val)
print('STRICT_GAP',lr_val-full_val)
print('JENSEN_FORMULA_CHECK',jensen)
print('ALL EXACT CHECKS PASSED')
