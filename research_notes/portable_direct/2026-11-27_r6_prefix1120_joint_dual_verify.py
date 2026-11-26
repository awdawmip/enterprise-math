from fractions import Fraction as F
from pathlib import Path
from math import gcd
import hashlib,json
G=10**85; E=400000; L0=10**8
raw=Path('root_8800_result.json').read_bytes()
assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()=='e03d50ec3c79588577e8aaef7e194adf7562f2c8'
data=json.loads(raw); R,C,T=tuple(tuple(F(int(v),G) for v in data[k]) for k in ('rho','c','d'))
M=16225927682921336339157801028812800000000
Q0=544447235321021556325566186117974922692
P=72486411641368782354423090020719211170157
Qw=3380890274893182433251695995418378677023
assert gcd(P,Qw)==1 and Q0<Qw
eta=max(abs(v-F(P,Qw)) for v in R)
margin=F(1,Qw)-Q0*eta-(T[1]*Q0+2*E)/M**2
assert margin>0
qmin=Q0+1; assert qmin>16*E/T[0]
K=9*T[1]/8; J=16*E/T[0]; H=2*T[1]+F(4*E,qmin)
assert 1-T[1]/10-F(2*E,L0)>0 and F(2*E,L0**2)<1
x,y=sum(R)/2,sum(C)/2; wr,wc=(R[1]-R[0])/2,(C[1]-C[0])/2
rows=[(13241695572016246280452795405,-614903515325433031059117378,-586453816401334287434546),(1182616791650392258028253444,-74796824988556406807726418,4246778208283374384362279),(-7752265403315380654172299023,382363756442351370763912993,-4494886358260478563501531)]
a,b,c=rows; det=a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0]); assert abs(det)==1
Q=18*10**50
# For triple windows q^2<=J L, hence q*delta<=K J^2/q^3, q*|gamma|<=H J/q.
ep=Q*wr+K*J**2/qmin**3; eh=Q*wc+H*J/qmin
bounds=[Q*abs(a+b*x+c*y)+abs(b)*ep+abs(c)*eh for a,b,c in rows]
assert max(bounds)<1
# For any pair with L>=Lpair, q<=Q, use the pair bounds directly.
Lpair=10**80
ep2=Q*(wr+K/Lpair**2);eh2=Q*(wc+H/Lpair)
pair_bounds=[Q*abs(a+b*x+c*y)+abs(b)*ep2+abs(c)*eh2 for a,b,c in rows]
assert max(pair_bounds)<1
# On fixed dyadic grid no triple window before M by PREFIX-1119.
Lmin=F((Q+1)**2)/J
Ldy=M
while Ldy<Lmin:Ldy*=2
second=F(Ldy**3,(18*E)**2)
assert Lmin>10**96 and second>10**276
out={'root_sha256':hashlib.sha256(raw).hexdigest(),'M':M,'q0':Q0,'qmin':qmin,'witness':[P,Qw],'small_q_margin':str(margin),'rows':rows,'det':det,'Q':Q,'triple_bounds':[str(z) for z in bounds],'pair_L':Lpair,'pair_bounds':[str(z) for z in pair_bounds],'first_triple_L_min':str(Lmin),'first_dyadic_L_min':Ldy,'second_distinct_dyadic_slope_L_min':str(second)}
Path('prefix1120_result.json').write_text(json.dumps(out,indent=2)+'\n')
print('qmin',qmin,'small q margin',float(margin),'det',det)
print('triple bounds',*[float(v) for v in bounds]);print('pair bounds',*[float(v) for v in pair_bounds]);print('first triple L',float(Lmin),'first dyadic',float(Ldy),'second distinct dyadic',float(second))
