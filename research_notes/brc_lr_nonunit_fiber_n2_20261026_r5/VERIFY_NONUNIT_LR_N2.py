from fractions import Fraction as F
from itertools import product

H = ('h','k','z')
SYMS = ('x','y')
Q1 = {'h':F(1,6),'k':F(1,6),'z':F(2,3)}
L1 = {'h':F(2),'k':F(2),'z':F(1,2)}
P1 = {h:L1[h]*Q1[h] for h in H}
Q2 = {h:{'x':F(1,2),'y':F(1,2)} for h in H}
P2 = {'h':{'x':F(3,4),'y':F(1,4)},
      'k':{'x':F(1,2),'y':F(1,2)},
      'z':{'x':F(1,2),'y':F(1,2)}}
L2 = {(h,y):L1[h]*P2[h][y]/Q2[h][y] for h in H for y in SYMS}
assert sum(P1.values())==sum(Q1.values())==1
assert all(sum(P2[h].values())==sum(Q2[h].values())==1 for h in H)
assert all(P2[h][y]>0 and Q2[h][y]>0 for h in H for y in SYMS)
assert L2[('h','x')]==3 and L2[('h','y')]==1
assert L2[('k','x')]==L2[('k','y')]==2
assert L2[('z','x')]==L2[('z','y')]==F(1,2)
assert P2['h']['x']!=P2['k']['x']

def obs(root, action, dec):
    out=[]
    for idx in range(2):
        first=P1 if idx==0 else Q1
        cond=P2 if idx==0 else Q2
        if root!='C':
            err = F(root==('Q' if idx==0 else 'P'))
            time=F(0)
        else:
            err,time=F(0),F(1)
            for h in H:
                a=action[h]
                if a=='C':
                    time += first[h]
                    for y in SYMS:
                        d=dec[(h,y)]
                        err += first[h]*cond[h][y]*F(d==('Q' if idx==0 else 'P'))
                else:
                    err += first[h]*F(a==('Q' if idx==0 else 'P'))
        out.append((err,time))
    return (out[0][0],out[1][0],out[0][1],out[1][1])

def cost(o):return o[0]+2*o[1]+2*o[2]-F(15,4)*o[3]

witness_act={'h':'C','k':'P','z':'C'}
witness_dec={('h','x'):'P',('h','y'):'Q',('k','x'):'P',('k','y'):'P',('z','x'):'Q',('z','y'):'Q'}
witness=obs('C',witness_act,witness_dec)
assert witness==(F(5,12),F(1,4),F(5,3),F(11,6)),witness
assert cost(witness)==F(-21,8)

levels=sorted(set(L2.values()))
assert levels==[F(1,2),F(1),F(2),F(3)]
min_lr=None
count_lr=0
for root in ('P','Q','C'):
 for acts in product(('P','Q','C'),repeat=2):
  a={h:dict(zip((F(1,2),F(2)),acts))[L1[h]] for h in H}
  for decs in product(('P','Q'),repeat=len(levels)):
   choices=dict(zip(levels,decs))
   d={(h,y):choices[L2[(h,y)]] for h in H for y in SYMS}
   o=obs(root,a,d)
   c=cost(o)
   if min_lr is None or c<min_lr:min_lr=c
   count_lr+=1
assert count_lr==3*3**2*2**4==432
assert min_lr==F(-31,12),(min_lr,count_lr)
assert min_lr-cost(witness)==F(1,24)

A,B,C,D=F(1),F(2),F(2),F(-15,4)
def terminal_cost(r):return min(A*r,B)
def stage_val(h):
    early=min(A*L1[h],B)
    later=(C*L1[h]+D)+sum(Q2[h][y]*terminal_cost(L2[(h,y)]) for y in SYMS)
    return (early,later)
full_stage=sum(Q1[h]*min(stage_val(h)) for h in H)
class_stage=F(0)
for lr in sorted(set(L1.values())):
    sub=[h for h in H if L1[h]==lr]
    q=sum(Q1[h] for h in sub)
    stop=q*min(A*lr,B)
    cont=q*(C*lr+D)+sum(Q1[h]*sum(Q2[h][y]*terminal_cost(L2[(h,y)]) for y in SYMS) for h in sub)
    class_stage+=min(stop,cont)
root_cont=C+D
root_stop=min(A,B)
full_min=min(root_stop,root_cont+full_stage)
lr_min=min(root_stop,root_cont+class_stage)
assert full_min==F(-21,8)
assert lr_min==min_lr==F(-31,12)
assert [stage_val(h) for h in H]==[(F(2),F(7,4)),(F(2),F(9,4)),(F(1,2),F(-9,4))]
assert root_cont==F(-7,4)
assert [F(1,2),F(1),F(2),F(3)] == levels
print('ALL RAW P/Q BRANCHES POSITIVE: PASS')
print('FIRST LR CLASSES:',{h:str(L1[h]) for h in H})
print('TERMINAL LR:',{str(k):str(v) for k,v in L2.items()})
print('P-LUMPABILITY DEFECT AT FIRST LR=2:',P2['h']['x']-P2['k']['x'])
print('FULL WITNESS FOUR OBSERVERS:',tuple(map(str,witness)))
print('FULL SUPPORT MINIMUM:',full_min)
print('LR-ONLY SUPPORT MINIMUM:',lr_min)
print('STRICT EXACT SEPARATING GAP:',lr_min-full_min)
print('LR-ONLY DETERMINISTIC POLICIES EXHAUSTIVELY CHECKED:',count_lr)
print('EXACT BELLMAN / ENUMERATION AGREEMENT: PASS')
