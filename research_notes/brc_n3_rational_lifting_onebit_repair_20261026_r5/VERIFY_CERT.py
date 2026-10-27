from fractions import Fraction as F
R=(F(1,2),F(1),F(3,2))
Y=(F(1,4),F(1),F(2))
qa=(F(1,4),F(1,2),F(1,4));qb=(F(1,3),F(1,3),F(1,3))
mu=((F(5,7),F(1,4),F(1,28)),(F(3,7),F(1,4),F(9,28)),(F(1,7),F(1,4),F(17,28)))
assert all(sum(v)==1 and sum(y*p for y,p in zip(Y,v))==r and all(p>0 for p in v) for r,v in zip(R,mu))
z={
(0,0,'P'):F(50293,1612800),(0,0,'C'):F(1562507,1612800),
(1,1,'Q'):F(422459,806400),(1,1,'C'):F(717589,1612800),
(2,R[0],'P'):F(717589,5529600),(2,R[1],'P'):F(717589,3870720),
(2,R[2],'P'):F(4352659,38707200),(2,R[2],'Q'):F(619,100800),
(2,R[2],'C'):F(161,14400),
(3,Y[0],'P'):F(23,14400),(3,Y[1],'P'):F(161,57600),(3,Y[2],'P'):F(391,57600)
}
def w(t,s,a):return z.get((t,s,a),F(0))
def tot(t,s):return sum(w(t,s,a) for a in ('P','Q','C'))
assert all(v>=0 for v in z.values())
assert tot(0,0)==1 and tot(1,1)==w(0,0,'C')
for i,r in enumerate(R):assert tot(2,r)==(qa[i]+qb[i])*w(1,1,'C')/2
for j,y in enumerate(Y):assert tot(3,y)==sum(mu[i][j]*w(2,r,'C') for i,r in enumerate(R))
PE=w(0,0,'Q')+w(1,1,'Q')+sum(r*w(2,r,'Q') for r in R)+sum(y*w(3,y,'Q') for y in Y)
QE=w(0,0,'P')+w(1,1,'P')+sum(w(2,r,'P') for r in R)+sum(w(3,y,'P') for y in Y)
EP=w(0,0,'C')+w(1,1,'C')+sum(r*w(2,r,'C') for r in R)
EQ=w(0,0,'C')+w(1,1,'C')+sum(w(2,r,'C') for r in R)
O=(F(429887,806400),F(378989,806400),F(13733,9600),F(20519,14400))
assert (PE,QE,EP,EQ)==O and len(z)==12
print('EXACT_12_COLUMN_BRC_CERT_PASS',tuple(map(str,O)))
ob=(F(1,12),F(5,6),F(3,2),F(3,2))
J=2*ob[0]+2*ob[1]+F(5,48)*ob[3]
assert J==F(191,96) and F(2)-J==F(1,96)
print('UNSAFE_ONE_BIT_GAP_PASS',J,F(2)-J)
