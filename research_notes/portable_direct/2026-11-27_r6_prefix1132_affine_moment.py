from pathlib import Path
exec(Path('root_joint_compact.py').read_text().split('# Point enclosure')[0])
ns={};exec(Path('prefix1127_verify.py').read_text().split('r=(R[0]')[0],ns)
R,C,T,x,c0=(ns[k] for k in ('R','C','T','x','c0'))
assert t.a<=T[0]<=x<=T[1]<=t.b
n=json.load(open('fixed_summary.json'))['normal'];s=-F(n[0],n[1]);w=F(n[2],n[1]);ex=json.load(open('extra_rows.json'))[0];scale=10**125
def jets(tr,j):
 out=[]
 for p,ta in zip(pp,tails):
  v=horner(dp(p,j),tr);e=sum(comb(j,k)*rowbound[k]*ta[j-k] for k in range(j+1));out.append(v+I(-e,e))
 return out
def ab(tr):
 D=198/tr**2+216/(4-tr**2)+216/(16-tr**2)
 Dp=-396/tr**3+432*tr/(4-tr**2)**2+432*tr/(16-tr**2)**2
 alpha=36/tr**2-2+(1-tr**2/36)*D/2; beta=9/tr-tr/4
 ap=-72/tr**3-tr*D/36+(1-tr**2/36)*Dp/2;bp=-9/tr**2-F(1,4)
 return alpha,beta,ap,bp
def dotI(a,b):return sum((u*v for u,v in zip(a,b)),I(0))
def bound(row):
 v=dotI(cc,row);r=sum(dotI(row,[inv[i][j] for i in range(6)]).mag() for j in range(6))+sum((v*d).mag() for v,d in zip(row,dr));return v+I(-r,r)
f0,f1,f2=[jets(I(x),j) for j in range(3)];a,b,ap,bp=ab(I(x))
row=[b*v+(a-c0)*u-s*z for z,u,v in zip(f0,f1,f2)]
center=dotI(cc,row)+w*F(ex['m'],scale)
cols=[dotI(row,[inv[i][j] for i in range(6)])+w*F(ex['cols'][j],scale) for j in range(6)]+[row[i]*dr[i]+w*F(ex['cols'][i+6],scale) for i in range(6)]
radq=sum(v.mag() for v in cols)+abs(w)*F(ex['error'],scale)
B=center+I(-radq,radq)
tr=I(*T);f1,f2,f3=[jets(tr,j) for j in range(1,4)];a,b,ap,bp=ab(tr)
A=bound(f1);D=bound([b*z+(bp+a-c0)*v+(ap-s)*u for u,v,z in zip(f1,f2,f3)]);assert A.b<0
rx=36/x**2-1;J=-x*x*tr**2/(36*(tr+x));S=D*J/A;kappa=(S.a+S.b)/2
P=B/A+(S-kappa)*I(R[0]-rx,R[1]-rx);shift=(P.a+P.b)/2;intercept=c0-kappa*rx+shift;P=P-shift
assert kappa>0
print('B',B.show(),'A',A.show(),'D',D.show(),'P',P.show(),'kappa',float(kappa),flush=True)
out={k:list(map(str,[v.a,v.b])) for k,v in [('B',B),('A',A),('D',D),('J',J),('S',S),('P',P)]};out.update(kappa=str(kappa),intercept=str(intercept),shift=str(shift),s=str(s),w=str(w));Path('affine_moment.json').write_text(json.dumps(out,indent=2)+'\n')
