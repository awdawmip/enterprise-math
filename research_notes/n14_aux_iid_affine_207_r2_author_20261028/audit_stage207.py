"""Independent arithmetic audit of stored exact Stage207 witness certificate."""
import json
from fractions import Fraction as F
c=json.load(open("certificate207.json")); d=json.load(open("certificate208_dual.json"))
f=lambda x:tuple(map(F,x))
O=f(c["corners"]["00"]); Y=f(c["corners"]["10"])
Z=f(c["corners"]["01"]); YZ=f(c["corners"]["11"])
DY=tuple(y-o for y,o in zip(Y,O)); DZ=tuple(z-o for z,o in zip(Z,O))
assert DY==f(c["DY"]) and DZ==f(c["DZ"])
assert all(yz-y-z+o==0 for yz,y,z,o in zip(YZ,Y,Z,O))
e=lambda w:w[0]-w[1]
z0=-e(O)/e(DZ); slope=-e(DY)/e(DZ)
assert z0==F(c["coin"]["z0"]) and slope==F(c["coin"]["zs"])
assert 0<z0<z0+slope<1
obs=lambda u:tuple(O[i]+u*DY[i]+(z0+slope*u)*DZ[i] for i in range(4))
a,b=obs(F(0)),obs(F(1))
assert a[0]==a[1] and b[0]==b[1]
assert a[2]>a[3] and b[2]>b[3]
assert a[0]==F(c["left"]["alpha"]) and b[0]==F(c["right"]["alpha"])
assert a[2]==F(c["left"]["V"]) and b[2]==F(c["right"]["V"])
K=F(c["K207"]);H=F(c["H207"]);K2=F(d["K208"]);H2=F(d["H208"])
assert a[2]+2*K*a[0]==H==b[2]+2*K*b[0]
assert b[0]-a[0]==F(c["width"]) and K2<K
assert H2==H+2*b[0]*(K2-K)
print("STAGE207_INDEPENDENT_CERTIFICATE_ALGEBRA_PASS")
