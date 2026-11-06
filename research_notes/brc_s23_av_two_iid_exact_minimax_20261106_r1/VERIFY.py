from fractions import Fraction as F

# Six output orbits: 11, (13,31), (14,41), 33, (34,43), 44.
K = (
 (F(0),F(0),F(0),F(1),F(0),F(0)),
 (F(0),F(11,21),F(1,4),F(0),F(5,28),F(1,21)),
 (F(340,441),F(2,21),F(59,441),F(0),F(0),F(0))
)
M = ((F(1),F(0),F(0)),(-F(1,2),F(2),-F(1,2)),(F(0),F(0),F(1)))
D = F(9,49)
EXPECTED = (
 ((F(9,49),F(89,896),F(61,392)),(F(95,686),F(15,196),F(9,49)),(F(142,2401),F(45,686),F(9,49))),
 ((F(142,2401),F(45,686),F(9,49)),(F(65,3136),F(1005,10976),F(9,49)),(F(69,784),F(1529,12544),F(1053,6272)))
)
def laws(a,c):
 z=(1-a)*c;u=1-a-z
 full=(a*a,2*a*z,2*a*u,z*z,2*z*u,u*u)
 binary=(z*z,2*z*(1-z),(1-z)**2)
 assert sum(full)==sum(binary)==1
 return z,full,binary
def E(a,c):
 _,t,w=laws(a,c)
 return tuple(t[j]-sum(w[i]*K[i][j] for i in range(3)) for j in range(6))
def h(e):
 assert sum(e)==0
 return sum(max(F(0),x) for x in e)
def controls(a0,a1,c0,c1):
 aa=(a0,(a0+a1)/2,a1);cc=(c0,(c0+c1)/2,c1)
 v=[[E(a,c) for c in cc] for a in aa]
 return tuple(tuple(tuple(sum(M[i][p]*v[p][q][j]*M[k][q]
         for p in range(3) for q in range(3)) for j in range(6))
         for k in range(3)) for i in range(3))
def run():
 n=0
 for row in K:
  assert min(row)>=0 and sum(row)==1;n+=1
 z0,t0,_=laws(F(1,2),F(1,2));z1,t1,_=laws(F(5,7),F(7,8))
 assert z0==z1==F(1,4);assert h(tuple(x-y for x,y in zip(t0,t1)))==F(18,49);n+=2
 for bi,(a0,a1,c0,c1) in enumerate(((F(1,2),F(5,7),F(1,2),F(7,8)),
                                    (F(5,7),F(7,8),F(1,2),F(7,8)))):
  b=controls(a0,a1,c0,c1);tab=[]
  for i in range(3):
   r=[]
   for j in range(3):
    v=b[i][j];assert sum(v)==0;n+=1
    signed=max(sum(v[k] for k in range(6) if mask & (1<<k)) for mask in range(64))
    assert signed==h(v) and signed<=D;n+=2
    r.append(signed)
   tab.append(tuple(r))
  assert tuple(tab)==EXPECTED[bi];n+=1
 for ai in range(17):
  for ci in range(17):
   a=F(1,2)+F(3*ai,128);c=F(1,2)+F(3*ci,128)
   assert h(E(a,c))<=D;n+=1
 assert h(E(F(1,2),F(1,2)))==D
 assert h(E(F(5,7),F(7,8)))==D;n+=2
 print('PASS_S23_TWO_IID_EXACT_DEFICIENCY_9_49_20261106')
 print('theorem delta_2 =',D)
 print('indistinguishable_fiber_diameter =',F(18,49))
 for bi,tab in enumerate(EXPECTED,1):
  print('box',bi,'Bernstein TV control certificate:')
  for row in tab:print('  ',' '.join(str(v) for v in row))
  print('box_max =',max(max(row) for row in tab))
 print('rational checks =',n)
 print('finite_grid = 17 x 17; global theorem = two Bernstein coefficient tables')
if __name__=='__main__':run()
