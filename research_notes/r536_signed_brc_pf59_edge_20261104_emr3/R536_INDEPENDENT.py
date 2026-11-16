"""Independent R536 check: Python math.comb + SymPy Berkowitz, no JS imports."""
import json, math
from functools import lru_cache
from pathlib import Path
from sympy import Matrix
M=59
BIN=lambda a,b:math.comb(a,b) if a>=0 and 0<=b<=a else 0
CAT=lambda k:BIN(2*k,k)//(k+1)
@lru_cache(None)
def H(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return BIN(r+t,2*t)*sum(BIN(r-t,q)*(BIN(2*t,r-2*q)-BIN(2*t,r-2*q-1)) for q in range(r-t+1))
@lru_cache(None)
def B(k,t):
 r=2*k+1
 if t<2 or t>r:return 0
 return BIN(r+t,2*t)*sum(BIN(t-1,2*q)*4**q*CAT(k-q) for q in range(min((t-1)//2,k)+1))
def D(k):
 p=B(k,2);h=[B(k,t) for t in range(3,M+3)];z=[1]
 for j in range(1,M+1):z.append(sum((-1)**(a-1)*h[a-1]*p**(a-1)*z[j-a] for a in range(1,j+1)))
 return z[-1]
def sgn(v):return '+' if v>0 else '-' if v<0 else '0'
def main():
 C=json.loads(Path(__file__).with_name('R536_EVIDENCE.json').read_text())
 assert C['status']=='R536_EXACT_JS_PASS' and C['order']==M and C['identity_checks']==355
 delta=list(map(int,C['delta_at_k1']));assert len(delta)==118
 L=int(C['L']); S=lambda k:sum(d*BIN(k-1,j) for j,d in enumerate(delta))
 G=lambda k:(k*(k+1)*(2*k+1)*(2*k+3))**M*(k+2)
 ks=[1,2,3,9,10,11,12,49,50,51,52,60];verified=[]
 for k in ks:
  raw=Matrix([[H(k,3+i-j) for j in range(M)] for i in range(M)]).berkowitz_det()
  rec=D(k)
  assert raw==rec,(k,'raw/rec')
  assert L*rec==CAT(k)**M*G(k)*S(k),(k,'poly')
  verified.append({'k':k,'sign':sgn(raw),'digits':len(str(abs(int(raw))))})
 cross=0
 for k in [1,4,10,11,12,49,50,51,52]:
  for t in range(2,M+3):assert H(k,t)==B(k,t),(k,t);cross+=1
 origin=C['tail_shift_origin_k'];assert origin==51
 tail=[]
 for j in range(118):
  v=sum((-1)**(j-a)*BIN(j,a)*S(origin+a) for a in range(j+1))
  assert str(v)==C['tail_newton'][j],j
  tail.append(sgn(v))
 assert set(tail)=={'+'}
 assert [sgn(S(k)) for k in range(1,51)]==['+']*10+['-']*40
 return {'status':'R536_INDEPENDENT_PASS','method':'Python math.comb + SymPy Berkowitz, exact integers','boundary_checks':verified,'raw_determinants':len(ks),'H_B_crosschecks':cross,'tail_newton_coefficients':len(tail),'tail_origin_k':origin,'sign_blocks':C['sign_blocks']}
if __name__=='__main__':print(json.dumps(main(),ensure_ascii=False,indent=2))
