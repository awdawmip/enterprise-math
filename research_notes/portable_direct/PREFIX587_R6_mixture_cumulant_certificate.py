#!/usr/bin/env python3
"""Exact law of total third cumulance for native frozen 96-port BRC, depth 2."""
from PREFIX565_positive_marginal_certificate import edge,ACTIONS,ZERO_ROOT,SCIENCE_PIN
import json
assert SCIENCE_PIN == "f42f2906d77f24085c123f3ccfe9667d41caa96d"
from fractions import Fraction as F
from collections import Counter

stats=[]
for port in range(96):
    data=[]
    for a in ACTIONS:
        j,w=edge(port,a,ZERO_ROOT)
        y=192*w[6]-5*w[0]+w[1]-5*w[2]+w[3]+4*w[4]+4*w[5]
        p=[w[0]+w[1],w[2]+w[3],w[4]+w[5]]
        for b in ACTIONS:
            k,v=edge(j,b,ZERO_ROOT)
            y2=y+192*v[6]-5*v[0]+v[1]-5*v[2]+v[3]+4*v[4]+4*v[5]
            p2=[p[i]+v[2*i]+v[2*i+1] for i in range(3)]
            data.append((F(y2,192), p2))
    def E(f):return sum((f(y,p) for y,p in data),F())/36
    muY=E(lambda y,p:y)
    muP=[E(lambda y,p:p[i]) for i in range(3)]
    Cyp=[E(lambda y,p:y*p[i])-muY*muP[i] for i in range(3)]
    Cpp=[[E(lambda y,p:p[i]*p[j])-muP[i]*muP[j] for j in range(3)] for i in range(3)]
    K=[[E(lambda y,p,i=i,j=j:y*p[i]*p[j])-muY*E(lambda y,p,i=i,j=j:p[i]*p[j])-muP[i]*E(lambda y,p,j=j:y*p[j])-muP[j]*E(lambda y,p,i=i:y*p[i])+2*muY*muP[i]*muP[j] for j in range(3)] for i in range(3)]
    stats.append((muY,muP,Cyp,Cpp,K,data))

def mean(xs):return sum(xs,F())/len(xs)
def cov(xs,ys):return mean([x*y for x,y in zip(xs,ys)])-mean(xs)*mean(ys)
def cum3(xs,ys,zs):return mean([x*y*z for x,y,z in zip(xs,ys,zs)])-mean(xs)*mean([y*z for y,z in zip(ys,zs)])-mean(ys)*mean([x*z for x,z in zip(xs,zs)])-mean(zs)*mean([x*y for x,y in zip(xs,ys)])+2*mean(xs)*mean(ys)*mean(zs)
terms=[]
for func in [
 lambda i,j:mean([a[4][i][j] for a in stats]),
 lambda i,j:cum3([a[0] for a in stats],[a[1][i] for a in stats],[a[1][j] for a in stats]),
 lambda i,j:cov([a[0] for a in stats],[a[3][i][j] for a in stats]),
 lambda i,j:cov([a[1][i] for a in stats],[a[2][j] for a in stats]),
 lambda i,j:cov([a[1][j] for a in stats],[a[2][i] for a in stats]),
]:
 terms.append([[func(i,j) for j in range(3)] for i in range(3)])
M=[[0,1,-1],[1,-1,0],[-1,0,1]]
assert len(stats)==96 and all(len(a[5])==36 for a in stats)
E_local, C_means, C_between, B_left, B_right = terms
B_cross=[[B_left[i][j]+B_right[i][j] for j in range(3)] for i in range(3)]
check_expected=[(E_local,F(0)),(C_means,F(1,7776)),(C_between,-F(1,1296)),(B_cross,-F(1,1944))]
for mat,coef in check_expected:
    assert mat == [[coef*m for m in row] for row in M]
full=[[sum((t[i][j] for t in terms),F()) for j in range(3)] for i in range(3)]
assert full==[[-F(m,864) for m in row] for row in M]
# Independent direct third cumulant on all 3456 original labeled two-step paths:
all_paths=[x for st in stats for x in st[5]]
assert len(all_paths)==3456
def direct(f):return sum((f(y,p) for y,p in all_paths),F())/3456
my=direct(lambda y,p:y)
mp=[direct(lambda y,p:p[i]) for i in range(3)]
pooled=[[direct(lambda y,p,i=i,j=j:y*p[i]*p[j])-my*direct(lambda y,p,i=i,j=j:p[i]*p[j])-mp[i]*direct(lambda y,p,j=j:y*p[j])-mp[j]*direct(lambda y,p,i=i:y*p[i])+2*my*mp[i]*mp[j] for j in range(3)] for i in range(3)]
assert pooled == full
output={
 'schema':'PREFIX587_R6_LAW_OF_TOTAL_CUMULANCE_V1',
 'status':'ALL_CHECKS_PASS',
 'science_pin':SCIENCE_PIN,
 'ports':96,'actions':6,'ordered_length_two_paths':3456,
 'conditional_local_cumulant_average':'0*M',
 'conditional_means_third_cumulant':'(1/7776)*M',
 'cov_meanY_conditional_pair_cov':'(-1/1296)*M',
 'cross_meanPair_conditional_Ypair_cov_sum':'(-1/1944)*M',
 'pooled_cumulant':'(-1/864)*M',
 'direct_pooled_check':True,
 'matrix_M':M,
 'proof':'finite exhaustive native two-step path law and exact third-order law of total cumulance; exact rational arithmetic',
 'conclusion':'Uniform-start depth-two cubic matrix arises completely from between-initial-port mixing terms; conditional local matrices cancel in their uniform mean.'
}
print(json.dumps(output,indent=2,ensure_ascii=False))
