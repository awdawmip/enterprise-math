from fractions import Fraction as F
R=tuple(map(F,'1/10 1/2 3/4 1 5/4 3/2 19/10'.split()))
X=tuple(map(F,'999/1000 1/6 999/1000 1/20 29/240 11/160 1/120'.split()))
Y=tuple(map(F,'1 2002911/10904720 26095487/40892700 442758619/6542832000 11037627/68154500 394502727/2180944000 2002911/109047200'.split()))
D=tuple(map(F,'2502928/1477565 -18774008/1477565 2502928/1477565 6045767/1477565 -1139688/1477565 726533/1477565 0'.split()))
P={ (0,0):F('33553/432000'),(0,1):F('3997/368000'),(4,1):F('3997/690000'),(0,2):F('13091471/3762128400'),(2,2):F('8901809/21809440'),(4,2):F('170189123/37621284000'),(0,3):F('8294919533/677183112000'),(3,3):F('4095218743/29442744000'),(4,3):F('8294919533/188106420000'),(4,5):F('172449787/1363090000'),(5,5):F('219439/545236000'),(6,5):F('172449787/2180944000'),(6,6):F('38053/432000') }
DP={ (0,0):F(2),(0,1):-F(118,23),(4,1):-F(468,115),(0,2):F(72,23),(4,2):F(468,115),(5,5):F(-1),(5,1):F(1) }
def mass(f):
 g,a,b,u,v,w,z=f
 return (F(509,900)*u+F(47,180)*z+F(67,162)*(v-z)+w/100,
         F(13,40)*a+b/80-u,(g-a)/2,
         1-g+a/10+F(9,40)*b-v+F(191,450)*(u+w)+F(43,90)*z+F(14,81)*(v-z),
         (g-b)/2,F(3,40)*a+F(21,80)*b-w,
         u/100+F(47,180)*z+F(67,162)*(v-z)+F(509,900)*w)
def times(f):
 g,a,b,u,v,w,z=f
 return (1+g+F(3,8)*a+F(5,8)*b+u/2+v+F(3,2)*w,
         1+g+(a+b)/2+u+v+w)
def slacks(f):
 g,a,b,u,v,w,z=f
 return (a,g-a,1-g,b,g-b,u,F(13,40)*a+b/80-u,
         w,F(3,40)*a+F(21,80)*b-w,z,a/10-z,v-z,z+F(9,40)*b-v)
def edge(theta):
 return {e:P.get(e,F(0))+theta*DP.get(e,F(0)) for e in set(P)|set(DP)}
def xx(theta):return tuple(x+theta*d for x,d in zip(X,D))
nu0=mass(X); mu=mass(Y)
all_sources=[]
for k,(a,b) in enumerate(zip(slacks(X),slacks(xx(F(1))))):
 if b-a<0: all_sources.append((a/(a-b),'slack',k))
for e in P:
 if DP.get(e,F(0))<0: all_sources.append((P[e]/(-DP[e]),'edge',e))
all_sources.sort(key=lambda z:z[0]);print('upper limits first',all_sources[:8])
limit=all_sources[0][0]
for theta in (F(0),limit/2,limit):
 f=xx(theta); E=edge(theta)
 print('THETA', theta, 'MIN_SOURCE_SLACK', min(slacks(f)), 'MIN_EDGE', min(E.values()), 'POSITIVE_SUPPORT', sum(v>0 for v in E.values()))
 assert all(s>=0 for s in slacks(f)) and all(p>=0 for p in slacks(Y))
 assert times(f)==times(Y)
 assert sum(mass(f))==sum(mu)==1
 for i in range(7):assert sum(v for (ii,j),v in E.items() if ii==i)==mu[i]
 for j in range(7):
  assert sum(v for (i,jj),v in E.items() if jj==j)==mass(f)[j]
  assert sum(R[i]*v for (i,jj),v in E.items() if jj==j)==R[j]*mass(f)[j]
 nu=mass(f)
 Phi=F(23,5)*(mu[0]-nu[0])+3*(mu[1]-nu[1])+2*(mu[2]-nu[2])+(mu[3]-nu[3])
 print('PHI',Phi)
 assert Phi==theta
print('D=', D)
print('DP=', DP)
print('LIMIT',limit,'decimal',float(limit),'binding',all_sources[0])

# The complete physical source interval comes from the 13 affine slacks.
lower=[]; upper=[]
for k,(v0,v1) in enumerate(zip(slacks(X),slacks(xx(F(1))))):
    slope=v1-v0
    if slope>0: lower.append((-v0/slope,k))
    if slope<0: upper.append((v0/(-slope),k))
lo,low_index=max(lower); hi,high_index=min(upper)
assert (lo,low_index)==(F(-295513,24183068),5)
assert (hi,high_index)==(F(295513,500585600),2)
assert lo<0<limit<hi
for theta in (lo,F(0),limit,hi):
    assert all(z>=0 for z in slacks(xx(theta)))
    assert times(xx(theta))==times(Y)
    assert sum(mass(xx(theta)))==1

# Full 30-edge nonnegative dual certificate for Phi. Negative Phi
# excludes every legal nonnegative coupling, not only the chosen chart.
phi_row=[F(23,5),3,2,1,0,0,0]
phi_col=[-F(23,5),-5,-5,-5,0,0,0]
phi_mom=[0,4,4,4,0,0,0]
allowed=[(i,j) for j in (0,1,2,3,5,6) for i in range(7)
         if j not in (0,6) or i==j]
prices={e:phi_row[e[0]]+phi_col[e[1]]+R[e[0]]*phi_mom[e[1]]
        for e in allowed}
assert len(allowed)==30 and all(v>=0 for v in prices.values())
assert prices[(5,1)]==1
for theta in (lo,lo/2,F(0),limit,hi):
    nu=mass(xx(theta))
    phi=F(23,5)*(mu[0]-nu[0])+3*(mu[1]-nu[1])+2*(mu[2]-nu[2])+(mu[3]-nu[3])
    assert phi==theta
assert all(slacks(Y)[k]==0 for k in (6,10,12))
print('PASS_ALL_30_DUAL_EDGE_PRICES_NONNEGATIVE')
print('PASS_COMPLETE_PHYSICAL_INTERVAL',lo,hi,'BINDING_CAPACITY_INDEX',low_index,high_index)
print('PASS_ZERO_FACE_CROSSING_PHI_EQUALS_THETA')
print('PASS_FULL_REAL_14_EDGE_TRANSVERSE_SEGMENT',F(0),limit)
print('PASS_NEGATIVE_SIDE_PHYSICALLY_LAWFUL_BUT_BLACKWELL_INFEASIBLE',lo,F(0))
print('PASS_SHARP_14_SUPPORT_CAPACITY_EDGE', (5,5),'AT',limit)

# Second carrier pivots at theta_0, replacing depleted (5,5) by (3,5).
THETA_0=F(219439,545236000)
THETA_PHYS=F(295513,500585600)
DP2={(0,0):F(2), (0,1):-F(123,23), (4,1):-F(328,115),
     (0,2):F(72,23), (4,2):F(468,115), (0,3):F(5,23),
     (3,3):-F(1), (4,3):F(18,23), (4,5):-F(2), (3,5):F(1)}
BASE_AT_PIVOT=edge(THETA_0)
def chart2(theta):
    t=theta-THETA_0
    return {e:BASE_AT_PIVOT.get(e,F(0))+t*DP2.get(e,F(0))
            for e in set(BASE_AT_PIVOT)|set(DP2)}
def verify_transport(E,theta):
    assert all(w>=0 for w in E.values())
    nu=mass(xx(theta));mu=mass(Y)
    for i in range(7):
        assert sum(v for (ii,j),v in E.items() if ii==i)==mu[i]
    for j in range(7):
        assert sum(v for (i,jj),v in E.items() if jj==j)==nu[j]
        assert sum(R[i]*v for (i,jj),v in E.items() if jj==j)==R[j]*nu[j]
    assert sum(E.values())==1
for t in (THETA_0,(THETA_0+THETA_PHYS)/2,THETA_PHYS):
    E=chart2(t)
    verify_transport(E,t)
    assert sum(w>0 for w in E.values()) == (13 if t==THETA_0 else 14)
    assert all(w>=0 for w in slacks(xx(t)))
    assert times(xx(t))==times(Y)

# Exact rational column elimination independently checks carrier ranks.
def rank_cols(edges):
    A=[[F(int(k==e[0])) if k<7 else
        F(int(k-7==e[1])) if k<14 else
        R[e[0]]*F(int(k-14==e[1])) for e in edges]
        for k in range(21)]
    pivot=0
    for c in range(len(edges)):
        row=next((j for j in range(pivot,21) if A[j][c]),None)
        if row is None:continue
        A[pivot],A[row]=A[row],A[pivot]
        z=A[pivot][c];A[pivot]=[v/z for v in A[pivot]]
        for j in range(pivot+1,21):
            if A[j][c]:
                factor=A[j][c]
                A[j]=[u-factor*v for u,v in zip(A[j],A[pivot])]
        pivot+=1
    return pivot
carrier1=tuple(set(P)|{(5,1)})
carrier2=tuple((set(P)|{(5,1),(3,5)})-{(5,5)})
assert len(carrier1)==len(carrier2)==14
print('CARRIER_RANKS',rank_cols(carrier1),rank_cols(carrier2))
assert rank_cols(carrier1)==rank_cols(carrier2)==14
assert all(v>0 for e,v in chart2(THETA_PHYS).items() if e in carrier2)
assert set(e for e,v in chart2(THETA_PHYS).items() if v>0)==set(carrier2)
for t in (THETA_0,THETA_PHYS):
    assert chart2(t)[(5,5)]==0
assert edge(THETA_0)[(5,5)]==0
assert all(chart2(THETA_0).get(e,F(0))==edge(THETA_0).get(e,F(0))
           for e in set(chart2(THETA_0))|set(edge(THETA_0)))
print('PASS_SECOND_EXACT_PIVOT_AT',THETA_0,'ADD_EDGE',(3,5),'DROP_EDGE',(5,5))
print('PASS_BOTH_14_EDGE_SUPPORT_MATRICES_FULL_RANK')
print('PASS_PIECEWISE_14_EDGE_TRANSPORT_ENTIRE_POSITIVE_PHYSICAL_HALF',F(0),THETA_PHYS)
print('THEOREM_COMPLETE_1D_PHYSICAL_BLACKWELL_FEASIBILITY_IFF_THETA_NONNEGATIVE')
