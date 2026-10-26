"""Exact six-channel author-only signed Ward seam check; NOT native CM."""
CH=((0,2),(1,2),(0,3),(2,2),(1,3),(0,4))
def jets(p,mod):
 m=(p-1)//6; h=pow(2,-1,mod);u=[[0]*p for _ in range(5)];u[0][0]=1
 for j in range(1,p):
  den=pow(j*(j-p*h),-1,mod)
  for a in range(5):
   v=(j-1-m)*(j-1-2*m)*u[a][j-1]
   if a>=1:v+=3*j*u[a-1][j]-(3*(j-1)-4*m)*u[a-1][j-1]
   if a>=2:v+=2*u[a-2][j-1]
   u[a][j]=v*den%mod
 return u
def adjoint(p,mod):
 M=2*((p-1)//6)-1;neg={};pos={};v=0
 for n in range(-M,0):
  w=(1-6*n)*pow(2,n,mod)%mod
  v=(w+(p-2*n+1)*v)*pow(p-2*n,-1,mod)%mod;neg[n]=v
 xi=(1+(p+1)*v)%mod;v=0
 for n in range(1,M+1):
  w=(1-6*n)*pow(2,n,mod)%mod
  v=(w+(p-2*n+1)*v)*pow(p-2*n,-1,mod)%mod;pos[n]=v
 return xi,neg,pos
def cert(p):
 m=(p-1)//6;M=2*m-1;mod=p*p;u=jets(p,mod);h=pow(2,-1,mod)
 Y={ch:{n:0 for n in range(-M,M+2)} for ch in CH}
 for j in range(1,2*m+1):
  for ell in range(1,2*m+1):
   n=ell-j
   for a,b in CH:
    v=u[a][j]*u[b][p-ell]%mod
    Y[(a,b)][n]=(Y[(a,b)][n]+(j-(p-n)*h)*v)%mod
 assert all(Y[ch][M+1]==0 for ch in CH)
 xi,neg,pos=adjoint(p,mod)
 inv6=pow(6,-1,mod)
 w={(0,2):1,(1,2):-p*inv6,(0,3):-p*inv6,
    (2,2):p*p*pow(36,-1,mod),
    (1,3):p*p*pow(36,-1,mod),(0,4):p*p*pow(36,-1,mod)}
 residual={}
 for ch in CH:
  S={n:((p-2*n)*Y[ch][n]-(p-2*n-1)*Y[ch][n+1])%mod
     for n in range(-M,M+1)}
  lhs=sum((1-6*n)*pow(2,n,mod)*Y[ch][n] for n in range(-M,M+1))%mod
  rhs=(sum(neg[n]*S[n] for n in range(-M,0))
       +sum(pos[n]*S[n] for n in range(1,M+1)))%mod
  residual[ch]=(lhs-rhs)%mod
  assert residual[ch]==xi*Y[ch][0]%mod,(p,ch)
 y0=sum(w[ch]*Y[ch][0] for ch in CH)%mod
 r=sum(w[ch]*residual[ch] for ch in CH)%mod
 assert r==xi*y0%mod
 assert r%p==xi%p*Y[(0,2)][0]%p
 return {str(ch):Y[ch][0] for ch in CH},xi,y0,r
def main():
 a=cert(13);b=cert(733)
 assert a[0]=={'(0, 2)':41,'(1, 2)':6,'(0, 3)':20,
              '(2, 2)':136,'(1, 3)':106,'(0, 4)':138}
 assert b[0]=={'(0, 2)':334932,'(1, 2)':402190,'(0, 3)':202129,
              '(2, 2)':386294,'(1, 3)':154257,'(0, 4)':22613}
 assert a[1:]==(82,41,151)
 assert b[1:]==(28787,26339,106014)
 assert a[-1]%13==8 and b[-1]%733==462
 print("PASS exact corrected-Hasse six-channel signed Ward residual, p=13 and p=733")
 print(a);print(b)
if __name__=="__main__":main()
